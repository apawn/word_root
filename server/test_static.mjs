import {test} from 'node:test';
import assert from 'node:assert/strict';
import {mkdtempSync, readFileSync, rmSync} from 'node:fs';
import {tmpdir} from 'node:os';
import {join} from 'node:path';
import {spawnSync} from 'node:child_process';
import {StaticData} from './static-data.js';

const queries = [
  ['stats', {}], ['documents', {}], ['documents', {q: '第二'}],
  ['documents', {category: '项目说明', offset: 1, limit: 1}],
  ['words', {}], ['words', {q: '售卖'}], ['words', {q: 'VEND', offset: 1, limit: 1}],
  ['words', {q: '%'}], ['words', {category: 'missing'}],
  ['navigation', {path: '词根.md'}], ['navigation', {path: '词根.md', q: '售卖'}],
  ['navigation', {path: '词根.md', kind: 'heading', offset: 1, limit: 1}],
  ['document', {path: '词根.md', anchor: 'w-80'}], ['document', {path: '词根.md', anchor: 'missing'}],
  ['chunks', {path: '词根.md', offset: 7, limit: 10}],
  ['chunks', {path: '词根.md', offset: 999, limit: 10}],
  ...[0, 2, 4, 30].flatMap(chunk => ['', 'vend', '售卖', 'missing'].map(q =>
    ['navigation-position', {path: '词根.md', chunk, q}]))
];
const temp = mkdtempSync(join(tmpdir(), 'word-root-static-'));
try {
  const script = `
import sys,json,contextlib
from pathlib import Path
sys.path.insert(0, 'server')
import server,build_static
root=Path(sys.argv[1]).resolve();server.ROOT=root;server.DB=root/'.index.sqlite3'
(root/'词根.md').write_text('# 词根\\n\\n## 单词\\n\\n<a id="w-80"></a>\\n\\n### 1. vendor — 卖方\\n\\n正文\\n\\n<a id="w-2"></a>\\n\\n### 2. vending\\n\\n**中文释义**：售卖\\n\\n' + '\\n\\n'.join('段落'+str(i)+'。'*5000 for i in range(18)))
(root/'second.md').write_text('# 第二份\\n\\n### 1. vendor — 供应商\\n')
(root/'secret.jsonl').write_text('not for publication')
(root/'.env').write_text('not for publication')
(root/'image.svg').write_text('<svg xmlns="http://www.w3.org/2000/svg"/>')
(root/'.hidden').mkdir();(root/'.hidden/private.md').write_text('# private')
build_static.build(root/'.site')
server.build_index(verbose=False)
handler=object.__new__(server.Handler)
results=[]
handler.send_data=lambda value,status=200: results.append(value)
with contextlib.closing(server.connect()) as db:
 for route,params in json.loads(sys.argv[2]):
  handler.api('/api/'+route,{k:[str(v)] for k,v in params.items()},db)
(root/'expected.json').write_text(json.dumps(results,ensure_ascii=False))
`;
  const build = spawnSync('python3', ['-c', script, temp, JSON.stringify(queries)], {encoding: 'utf8'});
  assert.equal(build.status, 0, build.stderr);
  const base = new URL('https://example.test/word_root/');
  const fetcher = async (url, {signal} = {}) => {
    signal?.throwIfAborted();
    assert.ok(url.pathname.startsWith(base.pathname));
    try {
      const content = readFileSync(join(temp, '.site', decodeURIComponent(url.pathname.slice(base.pathname.length))), 'utf8');
      return {ok: true, json: async () => JSON.parse(content)};
    } catch {return {ok: false};}
  };
  const api = new StaticData(base, fetcher);
  const expected = JSON.parse(readFileSync(join(temp, 'expected.json'), 'utf8'));
  const normalize = value => {
    if (Array.isArray(value)) return value.map(normalize);
    if (value && typeof value === 'object') return Object.fromEntries(Object.entries(value).filter(([k]) => k !== 'id').map(([k,v]) => [k, normalize(v)]));
    return value;
  };
  // document headings are intentionally compact in the local response.
  const normalizeResponse = (route, value) => {
    value = normalize(value);
    if (route === 'document') value.headings = value.headings.map(({label, anchor, chunk, level}) => ({label, anchor, chunk, level}));
    return value;
  };
  for (let i = 0; i < queries.length; i++) {
    const [route, params] = queries[i];
    await test(`static/local parity: ${route} ${JSON.stringify(params)}`, async () => {
      assert.deepEqual(normalizeResponse(route, await api.api(route, params)), normalizeResponse(route, expected[i]));
      assert.ok(api.cache.size <= 8);
    });
  }
  await test('cancellation, missing documents and safe static output', async () => {
    const controller = new AbortController(); controller.abort();
    await assert.rejects(api.api('words', {q: 'vend'}, controller.signal), {name: 'AbortError'});
    await assert.rejects(api.api('document', {path: 'missing.md'}), /找不到/);
    for (const path of ['source/.env', 'source/secret.jsonl', 'source/.hidden/private.md', 'server.py', '.index.sqlite3']) {
      assert.equal((await fetcher(new URL(path, base))).ok, false);
    }
    const html = readFileSync(join(temp, '.site/index.html'), 'utf8');
    assert.match(html, /data-source="static"/);
    assert.ok(!/\b(?:src|href)="\//.test(html));
    assert.match(readFileSync(join(temp, '.site/source/image.svg'), 'utf8'), /svg/);
  });
  await test('search scans every shard with bounded requests, cache and result page', async () => {
    let active = 0, maximum = 0;
    const manifest = {data: 'data/', documents: [{id: '0', path: 'test.md', title: 'Test', category: 'Test'}],
      shards: Array.from({length: 20}, (_, i) => `words-${i}.json`)};
    const bounded = new StaticData(base, async url => {
      if (url.pathname.endsWith('manifest.json')) return {ok: true, json: async () => manifest};
      active++; maximum = Math.max(maximum, active);
      await new Promise(resolve => setTimeout(resolve, 1));
      active--;
      const n = Number(url.pathname.match(/words-(\d+)/)[1]);
      return {ok: true, json: async () => [['0', n, `word${n}`, '售卖', `w-${n}`, n, 3]]};
    });
    const result = await bounded.api('words', {q: '售卖', offset: 14, limit: 2});
    assert.equal(result.total, 20);
    assert.deepEqual(result.items.map(row => row.n), [14, 15]);
    assert.equal(bounded.cache.size, 8);
    assert.equal(maximum, 4);
    assert.equal(bounded.lastSearch.result.items.length, 2);
  });
} finally {rmSync(temp, {recursive: true, force: true});}
