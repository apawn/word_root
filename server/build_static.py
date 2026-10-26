#!/usr/bin/env python3
"""Build a standalone GitHub Pages reader; no runtime Python or SQLite needed."""
import argparse
import contextlib
import hashlib
import json
import shutil
import tempfile
from pathlib import Path

import server


def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, separators=(',', ':')), encoding='utf-8')


def build(output):
    output = Path(output).resolve()
    # Never clear an existing directory: a typo must not destroy source files.
    if output.exists():
        raise ValueError(f'输出目录已存在，请换一个空路径或先手动删除：{output}')
    if output.is_relative_to(server.ROOT) and not any(p.startswith('.') for p in output.relative_to(server.ROOT).parts):
        raise ValueError('项目内输出目录须为隐藏目录（例如 .cache/pages），避免被本地索引再次扫描。')
    original_db = server.DB
    with tempfile.TemporaryDirectory() as temp:
        server.DB = Path(temp) / 'index.sqlite3'
        try:
            server.build_index()
            output.mkdir(parents=True)
            for name in ['app.js', 'style.css', 'static-api.js', 'static-worker.js', 'static-data.js']:
                shutil.copy2(server.HERE / name, output / name)
            shutil.copytree(server.HERE / 'vendor', output / 'vendor')
            html = (server.HERE / 'index.html').read_text(encoding='utf-8')
            html = html.replace('<html lang="zh-CN">', '<html lang="zh-CN" data-source="static">')
            html = html.replace('WORD ROOTS / LOCAL LIBRARY', 'WORD ROOTS / ONLINE LIBRARY')
            html = html.replace('本地资料库 · 离线可读', '在线资料库 · 按需加载')
            (output / 'index.html').write_text(html, encoding='utf-8')
            (output / '.nojekyll').touch()
            with contextlib.closing(server.connect()) as db:
                documents = [dict(r) for r in db.execute('SELECT * FROM documents ORDER BY category,path')]
                digest = hashlib.sha256()
                for doc in documents:
                    digest.update(doc['path'].encode())
                    digest.update((server.ROOT / doc['path']).read_bytes())
                digest.update((server.HERE / 'server.py').read_bytes())
                digest.update(Path(__file__).read_bytes())
                version = digest.hexdigest()[:20]
                data = output / 'data' / version
                for number, doc in enumerate(documents):
                    doc['id'] = str(number)
                    navigation = [dict(r) for r in db.execute('SELECT * FROM navigation WHERE path=? ORDER BY n', (doc['path'],))]
                    write_json(data / doc['id'] / 'navigation.json', navigation)
                    rows = db.execute('SELECT n,markdown FROM chunks WHERE path=? ORDER BY n', (doc['path'],))
                    page = 0
                    while batch := rows.fetchmany(8):
                        write_json(data / doc['id'] / f'{page}.json', [dict(r) for r in batch])
                        page += 1
                    source = output / 'source' / doc['path']
                    source.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(server.ROOT / doc['path'], source)
                doc_ids = {doc['path']: doc['id'] for doc in documents}
                # Compact, ordered shards keep substring/Chinese search exact while
                # bounding worker memory; identical labels remain separate results.
                rows = db.execute("SELECT * FROM navigation WHERE kind='word' ORDER BY label COLLATE NOCASE,path,n")
                shards = []
                while batch := rows.fetchmany(1500):
                    filename = f'words-{len(shards)}.json'
                    values = [[doc_ids[r['path']], r['n'], r['label'], r['detail'], r['anchor'], r['chunk'], r['level']] for r in batch]
                    write_json(data / filename, values)
                    shards.append(filename)
                stats = {'documents': len(documents),
                         'words': db.execute("SELECT count(DISTINCT label COLLATE NOCASE) FROM navigation WHERE kind='word'").fetchone()[0],
                         'categories': [dict(r) for r in db.execute('SELECT category,count(*) AS count FROM documents GROUP BY category ORDER BY category')]}
                write_json(output / 'manifest.json', {'data': f'data/{version}/', 'stats': stats, 'documents': documents, 'shards': shards})
            # Match the local server's source allowlist. No database, raw JSONL,
            # credentials, caches or authoring scripts enter the published site.
            import os
            for base, dirs, files in os.walk(server.ROOT):
                dirs[:] = sorted(d for d in dirs if not d.startswith('.') and d not in server.EXCLUDED)
                for name in files:
                    source = Path(base) / name
                    if source.suffix.lower() not in {'.svg', '.png', '.jpg', '.jpeg', '.gif', '.webp'}:
                        continue
                    if not source.resolve().is_relative_to(server.ROOT):
                        continue
                    dest = output / 'source' / source.relative_to(server.ROOT)
                    dest.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(source, dest)
            # README links to the reader screenshot; server/ is otherwise excluded.
            if (server.HERE / 'preview.jpg').exists():
                (output / 'source/server').mkdir(parents=True, exist_ok=True)
                shutil.copy2(server.HERE / 'preview.jpg', output / 'source/server/preview.jpg')
            size = sum(p.stat().st_size for p in output.rglob('*') if p.is_file())
            if size >= 1024 ** 3:
                raise ValueError('静态站点超过 GitHub Pages 的 1 GiB 上限。')
            print(f'静态站点：{output}\n{len(documents)} 份文档，{len(shards)} 个搜索分片，{size / 1024 ** 2:.1f} MiB')
        finally:
            server.DB = original_db


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=server.ROOT / '.cache/pages')
    args = parser.parse_args()
    build(args.output)
