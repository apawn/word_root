// Shared by the module worker and API parity tests; no DOM or UI dependencies.
export class StaticData {
  constructor(base, fetcher = (...args) => fetch(...args)) {
    this.base = new URL(base);
    this.fetcher = fetcher;
    this.cache = new Map();
  }
  async json(path, signal) {
    signal?.throwIfAborted();
    if (this.cache.has(path)) {
      const value = this.cache.get(path);
      this.cache.delete(path); this.cache.set(path, value);
      return value;
    }
    const response = await this.fetcher(new URL(path, this.base), {signal});
    if (!response.ok) throw new Error('在线资料加载失败，请检查网络或刷新页面重试。');
    const value = await response.json();
    signal?.throwIfAborted();
    this.cache.set(path, value);
    while (this.cache.size > 8) this.cache.delete(this.cache.keys().next().value);
    return value;
  }
  async init(signal) {
    if (this.manifest) return;
    const manifest = await this.json('manifest.json', signal);
    this.manifest = manifest;
    this.byPath = new Map(manifest.documents.map(doc => [doc.path, doc]));
    this.byId = new Map(manifest.documents.map(doc => [doc.id, doc]));
  }
  async api(route, params = {}, signal) {
    await this.init(signal);
    signal?.throwIfAborted();
    const {documents, stats, data, shards} = this.manifest;
    const q = String(params.q || '').slice(0, 200).trim().toLowerCase();
    const offset = Math.max(0, Number(params.offset) || 0);
    const limit = Math.max(1, Math.min(80, Number(params.limit) || 60));
    const matches = row => !q || row.label.toLowerCase().includes(q) || row.detail.toLowerCase().includes(q);
    const page = rows => ({total: rows.length, items: rows.slice(offset, offset + limit)});
    if (route === 'stats') return stats;
    if (route === 'documents') return page(documents.filter(doc =>
      (!params.category || doc.category === params.category) &&
      (!q || doc.title.toLowerCase().includes(q) || doc.path.toLowerCase().includes(q))));
    if (route === 'words' && !params.path) {
      // Cache only the most recent result page. Scan shards in order and retain
      // at most `limit` matches, even for an empty query matching the whole library.
      const key = JSON.stringify([q, params.category || '', offset, limit]);
      if (this.lastSearch?.key === key) return this.lastSearch.result;
      const items = [];
      let total = 0;
      for (let start = 0; start < shards.length; start += 4) {
        // Four bounded requests hide network latency without fetching all shards
        // concurrently; flatten only this small batch and preserve search order.
        const batch = await Promise.all(shards.slice(start, start + 4).map(shard => this.json(data + shard, signal)));
        signal?.throwIfAborted();
        const rows = batch.flat();
        for (const [id, n, label, detail, anchor, chunk, level] of rows) {
          const doc = this.byId.get(id);
          if (params.category && doc.category !== params.category) continue;
          if (!matches({label, detail})) continue;
          if (total >= offset && items.length < limit) items.push({path: doc.path, document_title: doc.title, n, label, detail, anchor, chunk, level, kind: 'word'});
          total++;
        }
      }
      const result = {total, items};
      this.lastSearch = {key, result};
      return result;
    }
    const doc = this.byPath.get(params.path);
    if (!doc) throw new Error('找不到这份 Markdown。');
    if (route === 'chunks') {
      const end = Math.min(doc.chunk_count, offset + Math.min(limit, 16));
      const items = [];
      for (let p = Math.floor(offset / 8); p < Math.ceil(end / 8); p++) {
        items.push(...await this.json(`${data}${doc.id}/${p}.json`, signal));
      }
      return {items: items.filter(item => item.n >= offset && item.n < end)};
    }
    const navigation = await this.json(`${data}${doc.id}/navigation.json`, signal);
    if (route === 'document') {
      const target = navigation.find(row => row.anchor === params.anchor);
      return {...doc, headings: navigation.filter(row => row.kind === 'heading').slice(0, 100),
        target: target ? {chunk: target.chunk, anchor: target.anchor} : null};
    }
    const kind = route === 'words' ? 'word' : params.kind || 'word';
    const rows = navigation.filter(row => row.kind === kind);
    if (route === 'navigation-position') {
      const chunk = Math.max(0, Number(params.chunk) || 0);
      const row = rows.findLast(row => row.chunk <= chunk);
      const index = row ? rows.filter(matches).findIndex(item => item.n === row.n) : -1;
      return {current: row ? {n: row.n, anchor: row.anchor, chunk: row.chunk} : null, index: index < 0 ? null : index};
    }
    if (route === 'navigation' || route === 'words') {
      return page(rows.filter(row => matches(row) && (!params.category || doc.category === params.category))
        .map(row => ({...row, document_title: doc.title})));
    }
    throw new Error('接口不存在');
  }
}
