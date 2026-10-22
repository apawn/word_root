#!/usr/bin/env python3
"""Local, disk-indexed Markdown reader. Python standard library only."""
import argparse
import contextlib
import json
import mimetypes
import re
import sqlite3
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, unquote, urlsplit

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
DB = HERE / '.index.sqlite3'
VERSION = '4'
EXCLUDED = {'server', 'node_modules', '__pycache__'}
HEADING = re.compile(r'^(#{1,6})\s+(.+)$')
ANCHOR = re.compile(r'<a\s+(?:id|name)=["\']([^"\']+)["\']\s*>\s*</a>')
WORD = re.compile(r'^\d+[.、]\s+(.+?)(?:\s+[—–]\s+(.*))?$')


def plain(text):
    text = re.sub(r'\[([^]]+)\]\([^)]*\)', r'\1', text)
    return re.sub(r'[*`]', '', text).strip()


def slug(text):
    return re.sub(r'[^\w\-\s]', '', plain(text).lower()).strip().replace(' ', '-')


def split_document(text):
    """Keep Markdown blocks intact; split long tables with repeated headers.

    Heading/word anchors are attached to the next block, never an empty chunk.
    Returns bounded rendering units and navigation entries into those units.
    """
    chunks, navigation, buffer = [], [], []
    buffer_size = 0
    pending_anchor = None
    used_slugs = {}
    lines = text.splitlines()
    i = 0

    def flush():
        nonlocal buffer, buffer_size
        if buffer:
            chunks.append('\n'.join(buffer).strip() + '\n')
            buffer, buffer_size = [], 0

    while i < len(lines):
        line = lines[i]
        anchor = ANCHOR.fullmatch(line.strip())
        if anchor:
            flush()
            pending_anchor = anchor.group(1)
            i += 1
            continue
        heading = HEADING.match(line)
        if heading:
            flush()
            label = plain(heading.group(2))
            base = slug(label)
            occurrence = used_slugs.get(base, 0)
            used_slugs[base] = occurrence + 1
            heading_anchor = base + (f'-{occurrence}' if occurrence else '')
            word = WORD.match(label) if len(heading.group(1)) == 3 else None
            target = pending_anchor or heading_anchor
            navigation.append({'label': word.group(1) if word else label,
                               'detail': (word.group(2) or '') if word else '',
                               'anchor': target, 'chunk': len(chunks),
                               'kind': 'word' if word else 'heading',
                               'level': len(heading.group(1))})
            buffer.append(f'<a id="{heading_anchor}"></a>')
            if pending_anchor:
                buffer.append(f'<a id="{pending_anchor}"></a>')
                pending_anchor = None
            buffer.append(line + '\n')
            i += 1
            continue
        if not line.strip():
            buffer.append('') if buffer else None
            i += 1
            continue
        # Fenced code is indivisible; preserve its delimiter and blank lines.
        fence = re.match(r'^\s*(`{3,}|~{3,})', line)
        block = [line]
        i += 1
        if fence:
            while i < len(lines):
                block.append(lines[i])
                i += 1
                if re.match(r'^\s*' + re.escape(fence.group(1)[0]) + '{' + str(len(fence.group(1))) + r',}\s*$', block[-1]):
                    break
        else:
            while i < len(lines) and lines[i].strip() and not HEADING.match(lines[i]) and not ANCHOR.fullmatch(lines[i].strip()):
                block.append(lines[i])
                i += 1
        is_table = len(block) > 1 and '|' in block[0] and re.match(r'^\s*\|?\s*:?-{3,}', block[1])
        parts = [block]
        if is_table:
            parts = [block[:2] + block[j:j + 24] for j in range(2, len(block), 24)] or [block]
        elif len(block) > 40 and all(re.match(r'^[-*+]\s+', row) for row in block):
            # Flat Markdown lists may contain thousands of links without blanks.
            parts = [block[j:j + 32] for j in range(0, len(block), 32)]
        for part in parts:
            size = sum(len(s) for s in part)
            if buffer_size + size > 4800 and buffer_size:
                flush()
            buffer.extend(part + [''])
            buffer_size += size
            if size >= 4800 or is_table:
                flush()
    flush()
    # Old-style word pages keep the Chinese definition below the heading.
    for entry in navigation:
        if entry['kind'] == 'word' and not entry['detail']:
            snippet = '\n'.join(chunks[entry['chunk']:entry['chunk'] + 2])
            match = re.search(r'\*\*中文释义\*\*[：:]\s*([^\n]+)', snippet)
            if match:
                entry['detail'] = plain(match.group(1))[:500]
    return chunks or ['（空文档）'], navigation


def connect():
    db = sqlite3.connect(DB, timeout=30)
    db.row_factory = sqlite3.Row
    db.execute('PRAGMA cache_size=-4096')
    return db


def markdown_files():
    import os
    for base, dirs, files in os.walk(ROOT):
        dirs[:] = sorted(d for d in dirs if not d.startswith('.') and d not in EXCLUDED)
        for name in sorted(files):
            if name.lower().endswith('.md'):
                path = Path(base) / name
                if path.resolve().is_relative_to(ROOT):
                    yield path


def build_index():
    start = time.monotonic()
    with contextlib.closing(connect()) as db:
        db.executescript('''
            PRAGMA journal_mode=WAL;
            CREATE TABLE IF NOT EXISTS settings (key TEXT PRIMARY KEY, value TEXT);
            CREATE TABLE IF NOT EXISTS documents (
              path TEXT PRIMARY KEY, title TEXT, category TEXT, size INTEGER,
              mtime INTEGER, chunk_count INTEGER, word_count INTEGER);
            CREATE TABLE IF NOT EXISTS chunks (path TEXT, n INTEGER, markdown TEXT,
              PRIMARY KEY(path,n));
            CREATE TABLE IF NOT EXISTS navigation (path TEXT, n INTEGER, label TEXT,
              detail TEXT, anchor TEXT, chunk INTEGER, kind TEXT, level INTEGER,
              PRIMARY KEY(path,n));
            CREATE INDEX IF NOT EXISTS nav_word ON navigation(kind,label COLLATE NOCASE);
            CREATE INDEX IF NOT EXISTS nav_anchor ON navigation(path,anchor);
        ''')
        old_version = db.execute("SELECT value FROM settings WHERE key='version'").fetchone()
        rebuild = not old_version or old_version[0] != VERSION
        previous = {r['path']: r for r in db.execute('SELECT path,mtime,size FROM documents')}
        seen, changed = set(), 0
        for file in markdown_files():
            path = file.relative_to(ROOT).as_posix()
            seen.add(path)
            stat = file.stat()
            old = previous.get(path)
            if not rebuild and old and old['mtime'] == stat.st_mtime_ns and old['size'] == stat.st_size:
                continue
            text = file.read_text(encoding='utf-8', errors='replace')
            chunks, entries = split_document(text)
            title = next((plain(s[2:]) for s in text.splitlines() if s.startswith('# ')), file.stem)
            parent = file.parent.relative_to(ROOT).as_posix()
            category = '资料库导读' if parent == '英语词根资料库' else parent.split('/')[-1]
            if category == '.':
                category = '项目说明'
            for table in ['chunks', 'navigation', 'documents']:
                db.execute(f'DELETE FROM {table} WHERE path=?', (path,))
            db.execute('INSERT INTO documents VALUES (?,?,?,?,?,?,?)',
                       (path, title, category, stat.st_size, stat.st_mtime_ns, len(chunks), sum(e['kind'] == 'word' for e in entries)))
            db.executemany('INSERT INTO chunks VALUES (?,?,?)', ((path, n, chunk) for n, chunk in enumerate(chunks)))
            db.executemany('INSERT INTO navigation VALUES (?,?,?,?,?,?,?,?)',
                           ((path, n, e['label'], e['detail'], e['anchor'], e['chunk'], e['kind'], e['level']) for n, e in enumerate(entries)))
            changed += 1
            if changed % 250 == 0:
                db.commit()
                print(f'已索引 {changed} 份文档…', flush=True)
        for path in previous.keys() - seen:
            for table in ['chunks', 'navigation', 'documents']:
                db.execute(f'DELETE FROM {table} WHERE path=?', (path,))
        db.execute("INSERT OR REPLACE INTO settings VALUES ('version',?)", (VERSION,))
        db.commit()
    print(f'索引完成：{len(seen)} 份 Markdown，更新 {changed} 份，耗时 {time.monotonic() - start:.1f}s', flush=True)


def like(value):
    return '%' + value.replace('\\', '\\\\').replace('%', '\\%').replace('_', '\\_') + '%'


class Handler(BaseHTTPRequestHandler):
    def log_message(self, *_):
        pass

    def send_data(self, value, status=200):
        data = json.dumps(value, ensure_ascii=False).encode()
        self.send_response(status)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Content-Length', str(len(data)))
        self.send_header('Cache-Control', 'no-store')
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        try:
            url = urlsplit(self.path)
            if url.path.startswith('/api/'):
                with contextlib.closing(connect()) as db:
                    self.api(url.path, parse_qs(url.query), db)
            else:
                self.file(unquote(url.path))
        except (BrokenPipeError, ConnectionResetError):
            pass
        except ValueError as error:
            self.send_data({'error': str(error)}, 400)
        except Exception as error:
            print(f'Request error: {error}', flush=True)
            self.send_data({'error': '读取失败，请重新启动服务后重试。'}, 500)

    def api(self, route, query, db):
        arg = lambda key, default='': query.get(key, [default])[0]
        offset = max(0, int(arg('offset', '0')))
        limit = max(1, min(80, int(arg('limit', '60'))))
        path, q = arg('path'), arg('q')[:200].strip()
        if route == '/api/stats':
            return self.send_data({'documents': db.execute('SELECT count(*) FROM documents').fetchone()[0],
                                  'words': db.execute("SELECT count(DISTINCT label COLLATE NOCASE) FROM navigation WHERE kind='word'").fetchone()[0],
                                  'categories': [dict(r) for r in db.execute('SELECT category,count(*) AS count FROM documents GROUP BY category ORDER BY category')]})
        if route == '/api/documents':
            conditions, params = ['1=1'], []
            if arg('category'):
                conditions.append('category=?')
                params.append(arg('category'))
            if q:
                conditions.append("(title LIKE ? ESCAPE '\\' OR path LIKE ? ESCAPE '\\')")
                params.extend([like(q), like(q)])
            where = ' AND '.join(conditions)
            total = db.execute('SELECT count(*) FROM documents WHERE ' + where, params).fetchone()[0]
            rows = db.execute('SELECT * FROM documents WHERE ' + where + ' ORDER BY category,path LIMIT ? OFFSET ?', params + [limit, offset])
            return self.send_data({'total': total, 'items': [dict(r) for r in rows]})
        if route in ['/api/words', '/api/navigation']:
            conditions, params = ['1=1'], []
            if path:
                conditions.append('n.path=?')
                params.append(path)
            kind = 'word' if route == '/api/words' else arg('kind', 'word')
            conditions.append('n.kind=?')
            params.append(kind)
            if q:
                conditions.append("(n.label LIKE ? ESCAPE '\\' OR n.detail LIKE ? ESCAPE '\\')")
                params.extend([like(q), like(q)])
            if arg('category'):
                conditions.append('d.category=?')
                params.append(arg('category'))
            where = ' AND '.join(conditions)
            source = ' FROM navigation n JOIN documents d ON d.path=n.path WHERE ' + where
            total = db.execute('SELECT count(*)' + source, params).fetchone()[0]
            order = 'n.n' if path else 'n.label COLLATE NOCASE,n.path'
            rows = db.execute('SELECT n.*,d.title AS document_title' + source + ' ORDER BY ' + order + ' LIMIT ? OFFSET ?', params + [limit, offset])
            return self.send_data({'total': total, 'items': [dict(r) for r in rows]})
        if route == '/api/document':
            row = db.execute('SELECT * FROM documents WHERE path=?', (path,)).fetchone()
            if not row:
                return self.send_data({'error': '找不到这份 Markdown。'}, 404)
            result = dict(row)
            result['headings'] = [dict(r) for r in db.execute("SELECT label,anchor,chunk,level FROM navigation WHERE path=? AND kind='heading' ORDER BY n LIMIT 100", (path,))]
            result['target'] = None
            if arg('anchor'):
                target = db.execute('SELECT chunk,anchor FROM navigation WHERE path=? AND anchor=?', (path, arg('anchor'))).fetchone()
                result['target'] = dict(target) if target else None
            return self.send_data(result)
        if route == '/api/chunks':
            rows = db.execute('SELECT n,markdown FROM chunks WHERE path=? AND n>=? ORDER BY n LIMIT ?', (path, offset, min(limit, 16)))
            return self.send_data({'items': [dict(r) for r in rows]})
        self.send_data({'error': '接口不存在'}, 404)

    def file(self, url):
        if url.startswith('/source/'):
            path = (ROOT / url[len('/source/'):]).resolve()
            relative = path.relative_to(ROOT)
            if any(p.startswith('.') or p in EXCLUDED for p in relative.parts) or path.suffix.lower() not in {'.md', '.svg', '.png', '.jpg', '.jpeg', '.gif', '.webp'}:
                return self.send_error(404)
        else:
            relative = url.lstrip('/') or 'index.html'
            path = (HERE / relative).resolve()
            if not path.is_relative_to(HERE) or (relative not in {'index.html', 'app.js', 'style.css'} and not relative.startswith('vendor/')):
                return self.send_error(404)
        if not path.is_file():
            return self.send_error(404)
        self.send_response(200)
        self.send_header('Content-Type', mimetypes.guess_type(path)[0] or 'application/octet-stream')
        self.send_header('Content-Length', str(path.stat().st_size))
        self.send_header('X-Content-Type-Options', 'nosniff')
        self.send_header('Cache-Control', 'no-cache')
        self.send_header('Content-Security-Policy', "default-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline'; img-src 'self' data: https:; object-src 'none'; base-uri 'self'; frame-ancestors 'none'")
        self.end_headers()
        with path.open('rb') as source:
            while data := source.read(65536):
                self.wfile.write(data)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--port', type=int, default=8765)
    parser.add_argument('--index-only', action='store_true')
    args = parser.parse_args()
    build_index()
    if args.index_only:
        return
    server = ThreadingHTTPServer(('127.0.0.1', args.port), Handler)
    print(f'词根阅读室 → http://127.0.0.1:{args.port}', flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print('\n服务已停止。')
    finally:
        server.server_close()


if __name__ == '__main__':
    main()
