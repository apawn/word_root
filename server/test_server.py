"""Run with: python3 -m unittest discover -s server -p 'test_*.py'."""
import contextlib
import importlib.util
import json
import sqlite3
import tempfile
import threading
import unittest
from unittest.mock import patch
from pathlib import Path
from urllib.error import HTTPError
from urllib.parse import urlencode, quote
from urllib.request import urlopen

spec = importlib.util.spec_from_file_location('reader_server', Path(__file__).with_name('server.py'))
server = importlib.util.module_from_spec(spec)
spec.loader.exec_module(server)


class ReaderTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.original = server.ROOT, server.DB
        server.ROOT = Path(self.temp.name).resolve()
        server.DB = server.ROOT / '.index.sqlite3'
        self.file = server.ROOT / '词根.md'
        self.file.write_text('# 词根\n\n## 单词\n\n<a id="w-1"></a>\n\n### 1. vendor — 卖方\n\n正文\n\n<a id="w-2"></a>\n\n### 2. vending\n\n**中文释义**：售卖\n', encoding='utf-8')
        server.build_index()

    def tearDown(self):
        server.ROOT, server.DB = self.original
        self.temp.cleanup()

    def test_word_targets_and_long_tables(self):
        text = self.file.read_text() + '\n## 索引\n\n| 单词 | 含义 |\n|---|---|\n' + '\n'.join(f'| word{i} | 第{i}项 |' for i in range(1500))
        chunks, entries = server.split_document(text)
        self.assertGreater(len(chunks), 60)
        self.assertLess(max(map(len, chunks)), 5000)
        words = [e for e in entries if e['kind'] == 'word']
        self.assertEqual([(w['label'], w['detail']) for w in words], [('vendor', '卖方'), ('vending', '售卖')])
        for word in words:
            self.assertIn(f'id="{word["anchor"]}"', chunks[word['chunk']])
            self.assertIn(word['label'], chunks[word['chunk']])
        self.assertIn('word1499', chunks[-1])
        self.assertTrue(all('| 单词 | 含义 |' in c for c in chunks if 'word' in c))

    def test_fences_and_long_lists(self):
        chunks, entries = server.split_document('# 标题\n\n```md\n### 1. not-a-word\n\ncode\n```\n\n' + '\n'.join(f'- [word{i}](file.md)' for i in range(1000)))
        self.assertEqual(len(entries), 1)
        self.assertTrue(any('```md\n### 1. not-a-word\n\ncode\n```' in c for c in chunks))
        self.assertLess(max(map(len, chunks)), 5000)
        self.assertIn('word999', chunks[-1])

    def test_index_update_and_deletion(self):
        self.file.write_text('# 修改\n\n### 1. changed\n\n更新正文', encoding='utf-8')
        server.build_index()
        with contextlib.closing(server.connect()) as db:
            self.assertEqual(db.execute('select title from documents').fetchone()[0], '修改')
            self.assertEqual(db.execute("select count(*) from navigation where kind='word'").fetchone()[0], 1)
        self.file.unlink()
        server.build_index()
        with contextlib.closing(server.connect()) as db:
            for table in ['documents', 'navigation', 'chunks']:
                self.assertEqual(db.execute(f'select count(*) from {table}').fetchone()[0], 0)

    def test_http_pagination_search_and_access(self):
        http = server.ThreadingHTTPServer(('127.0.0.1', 0), server.Handler)
        thread = threading.Thread(target=http.serve_forever, daemon=True)
        thread.start()
        base = f'http://127.0.0.1:{http.server_port}'
        def get(route, **params):
            return json.load(urlopen(base + '/api/' + route + '?' + urlencode(params)))
        try:
            self.assertEqual(get('documents')['total'], 1)
            self.assertEqual(get('words', q='售卖')['items'][0]['label'], 'vending')
            self.assertEqual(get('words', q='%')['total'], 0)
            self.assertEqual(get('navigation', path='词根.md', offset=1, limit=1)['items'][0]['label'], 'vending')
            target = get('document', path='词根.md', anchor='w-2')['target']
            self.assertIn('vending', get('chunks', path='词根.md', offset=target['chunk'], limit=1)['items'][0]['markdown'])
            self.assertIsNone(get('navigation-position', path='词根.md', chunk=0)['current'])
            current = get('navigation-position', path='词根.md', chunk=target['chunk'])
            self.assertEqual(current['current']['anchor'], 'w-2')
            self.assertEqual(current['index'], 1)
            # The same word spans following chunks, even without another heading.
            self.assertEqual(get('navigation-position', path='词根.md', chunk=target['chunk'] + 1)['index'], 1)
            self.assertEqual(get('navigation-position', path='词根.md', chunk=target['chunk'], q='售卖')['index'], 0)
            self.assertIsNone(get('navigation-position', path='词根.md', chunk=target['chunk'], q='vendor')['index'])
            heading = get('navigation-position', path='词根.md', kind='heading', chunk=target['chunk'])
            self.assertEqual(heading['current']['anchor'], '单词')
            self.assertEqual(heading['index'], 1)
            for route in ['/source/.index.sqlite3', '/server.py', '/source/%2e%2e/secret.md']:
                with self.assertRaises(HTTPError) as error:
                    urlopen(base + route)
                self.assertIn(error.exception.code, [400, 404])
        finally:
            http.shutdown(); http.server_close(); thread.join()

    def test_page_refresh_syncs_edits_additions_and_deletions(self):
        http = server.ThreadingHTTPServer(('127.0.0.1', 0), server.Handler)
        thread = threading.Thread(target=http.serve_forever, daemon=True)
        thread.start()
        base = f'http://127.0.0.1:{http.server_port}'

        def get(route, **params):
            with urlopen(base + '/api/' + route + '?' + urlencode(params)) as response:
                return json.load(response)

        try:
            # Match the browser: stats finishes before navigation/content loads.
            with patch.object(server, 'split_document', wraps=server.split_document) as parse:
                self.assertEqual(get('stats')['documents'], 1)
                parse.assert_not_called()
                self.file.write_text('# 新标题\n\n<a id="w-1"></a>\n\n### 1. particle — 微粒\n\n更新后的拆解：part + -icle。\n', encoding='utf-8')
                self.assertEqual(get('stats')['words'], 1)
                self.assertEqual(parse.call_count, 1)
                doc = get('document', path='词根.md', anchor='w-1')
                self.assertEqual(doc['title'], '新标题')
                self.assertEqual(get('words', q='vendor')['total'], 0)
                self.assertEqual(get('navigation', path='词根.md')['items'][0]['label'], 'particle')
                content = get('chunks', path='词根.md', offset=doc['target']['chunk'], limit=1)
                self.assertIn('更新后的拆解', content['items'][0]['markdown'])
                # Reading subsequent pages does not rescan/reparse the library.
                self.assertEqual(parse.call_count, 1)
                added = server.ROOT / '新增.md'
                added.write_text('# 新增文档\n\n新增内容', encoding='utf-8')
                self.assertEqual(get('stats')['documents'], 2)
                self.assertEqual(get('documents', q='新增')['total'], 1)
                self.assertEqual(parse.call_count, 2)
                self.file.unlink()
                self.assertEqual(get('stats')['documents'], 1)
                self.assertEqual(get('words', q='particle')['total'], 0)
                self.assertEqual(get('chunks', path='词根.md')['items'], [])
                self.assertEqual(parse.call_count, 2)
        finally:
            http.shutdown(); http.server_close(); thread.join()


if __name__ == '__main__':
    unittest.main()
