import {Virtualizer, elementScroll, observeElementRect, observeElementOffset} from './vendor/virtual.js';

const staticMode = document.documentElement.dataset.source === 'static';
const staticApi = staticMode ? import('./static-api.js') : null;
const sourceBase = new URL('./source/', import.meta.url);
const sourceURL = path => new URL(path.split('/').map(encodeURIComponent).join('/'), sourceBase);

const $ = (selector) => document.querySelector(selector);
const state = {path: '', doc: null, mode: 'documents', kind: 'word', anchor: '', openToken: 0};
const esc = (s = '') => String(s).replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const debounce = (fn, delay = 220) => {let timer; return (...args) => {clearTimeout(timer); timer = setTimeout(() => fn(...args), delay);};};
function toast(message) { $('#toast').textContent = message; $('#toast').hidden = false; clearTimeout(toast.timer); toast.timer = setTimeout(() => $('#toast').hidden = true, 6000); }
async function api(route, params = {}, signal) {
  if (staticMode) return (await staticApi).api(route, params, signal);
  const response = await fetch(`/api/${route}?${new URLSearchParams(params)}`, {signal});
  if (!response.ok) throw new Error((await response.json()).error || '加载失败，请重试');
  return response.json();
}
function virtualizer(element, count, size, onChange, overscan = 5) {
  const v = new Virtualizer({count, getScrollElement: () => element, estimateSize: () => size,
    observeElementRect, observeElementOffset, scrollToFn: elementScroll, overscan,
    onChange, useAnimationFrameWithResizeObserver: true});
  const cleanup = v._didMount();
  v._willUpdate();
  return {v, cleanup};
}

// Fixed-height, paginated navigation. Neither DOM nodes nor page data grow forever.
class PagedList {
  constructor(element, countLabel, row, choose, rowHeight = 76) {
    Object.assign(this, {element, countLabel, row, choose, rowHeight});
    this.space = element.firstElementChild;
    this.version = 0;
    this.nodes = new Map();
    element.addEventListener('click', e => {
      const button = e.target.closest('button[data-index]');
      if (!button) return;
      const item = this.item(Number(button.dataset.index));
      if (item) this.choose(item);
    });
  }
  item(index) {return this.pages.get(Math.floor(index / 60))?.[index % 60];}
  async reset(route, params) {
    this.version++;
    const version = this.version;
    this.controller?.abort();
    this.controller = new AbortController();
    this.cleanup?.();
    this.v = null;
    this.route = route;
    this.params = params;
    this.pages = new Map();
    this.pending = new Set();
    this.nodes.clear();
    this.pendingReveal = null;
    this.element.scrollTop = 0;
    this.space.style.height = 'auto';
    this.space.innerHTML = '<div class="list-empty">正在加载…</div>';
    try {
      const data = await api(route, {...params, limit: 60}, this.controller.signal);
      if (version !== this.version) return;
      this.total = data.total;
      this.countLabel.textContent = data.total.toLocaleString();
      this.pages.set(0, data.items);
      this.space.replaceChildren();
      if (!data.total) {
        this.space.innerHTML = '<div class="list-empty">没有找到匹配内容。<br>试试其他关键词，或切换上方分类。</div>';
        return;
      }
      const instance = virtualizer(this.element, data.total, this.rowHeight, () => this.schedule());
      Object.assign(this, instance);
      this.render();
    } catch (e) {
      if (e.name !== 'AbortError' && version === this.version) {
        this.space.innerHTML = '<div class="list-empty">加载失败，<button class="retry">点击重试</button></div>';
        this.space.querySelector('.retry').onclick = () => this.reset(route, params);
        toast(e.message);
      }
    }
  }
  schedule() {if (!this.frame) this.frame = requestAnimationFrame(() => {this.frame = null; this.render();});}
  reveal(index) {
    this.pendingReveal = index;
    this.schedule();
  }
  async load(page) {
    if (this.pending.has(page) || this.pages.has(page)) return;
    this.pending.add(page);
    const version = this.version;
    try {
      const data = await api(this.route, {...this.params, offset: page * 60, limit: 60}, this.controller.signal);
      if (version !== this.version) return;
      this.pages.set(page, data.items);
      while (this.pages.size > 8) {
        const farthest = [...this.pages.keys()].sort((a,b) => Math.abs(b-page)-Math.abs(a-page))[0];
        this.pages.delete(farthest);
      }
      this.pending.delete(page);
      this.schedule();
    } catch (e) {
      if (e.name !== 'AbortError' && version === this.version) {
        toast(e.message);
        // Keep a failed request marked until the user explicitly retries.
        for (const [index, node] of this.nodes) if (Math.floor(index/60) === page) {
          node.innerHTML = '<button class="retry">加载失败，点击重试</button>';
          node.firstChild.onclick = () => {this.pending.delete(page); this.load(page);};
        }
      }
    }
  }
  render() {
    if (!this.v) return;
    this.space.style.height = `${this.v.getTotalSize()}px`;
    if (this.pendingReveal !== null && this.element.clientHeight > 0) {
      const index = this.pendingReveal;
      this.pendingReveal = null;
      const top = index * this.rowHeight;
      const bottom = top + this.rowHeight;
      if (top < this.element.scrollTop || bottom > this.element.scrollTop + this.element.clientHeight) {
        this.v.scrollToIndex(index, {align: 'center'});
      }
    }
    const visible = this.v.getVirtualItems();
    const wanted = new Set(visible.map(x => x.index));
    for (const [index, node] of this.nodes) if (!wanted.has(index)) {node.remove(); this.nodes.delete(index);}
    for (const item of visible) {
      let node = this.nodes.get(item.index);
      if (!node) {node = document.createElement('div'); node.className = 'list-row'; this.nodes.set(item.index, node); this.space.append(node);}
      node.style.transform = `translateY(${item.start}px)`;
      node.style.height = `${item.size}px`;
      const data = this.item(item.index);
      if (data) {
        const content = this.row(data, item.index);
        if (node._html !== content) {node.innerHTML = content; node._html = content;}
      } else {
        node._html = null;
        node.innerHTML = '<div class="list-empty">加载中…</div>';
        this.load(Math.floor(item.index / 60));
      }
    }
  }
}

function fileRow(item, index) {
  const isWord = state.mode === 'words';
  const title = isWord ? item.label : item.title.replace(/^\d+\s*·\s*/, '');
  const detail = isWord ? `${item.detail || ''} · ${item.document_title}` : `${item.category.replace(/^\d+_/, '')} · ${item.word_count} 个单词`;
  return `<button data-index="${index}" class="${item.path === state.path ? 'active' : ''}" title="${esc(isWord ? detail : item.path)}"><span class="row-title">${esc(title)}</span><span class="row-detail">${esc(detail)}</span></button>`;
}
function wordRow(item, index) {
  return `<button data-index="${index}" aria-current="${item.anchor === state.anchor ? 'location' : 'false'}" class="word-row ${item.anchor === state.anchor ? 'active' : ''}" title="${esc(item.label + ' ' + item.detail)}"><span class="row-title">${esc(item.label)}</span><span class="row-detail">${esc(item.detail || (item.kind === 'heading' ? '章节 · 点击跳转' : '点击阅读讲解'))}</span></button>`;
}
const files = new PagedList($('#file-list'), $('#file-count'), fileRow, item => openDocument(item.path, item.anchor || ''));
const words = new PagedList($('#word-list'), $('#word-count'), wordRow, item => jump(item.chunk, item.anchor));
function searchFiles() {return files.reset(state.mode === 'words' ? 'words' : 'documents', {q: $('#global-search').value.trim(), category: $('#category').value});}
async function searchWords() {
  if (!state.path) return;
  await words.reset('navigation', {path: state.path, kind: state.kind, q: $('#word-search').value.trim()});
  reader.schedule();
}

let sidebarSyncKey = '', sidebarSyncTimer, sidebarSyncController;
function queueSidebarSync(chunk) {
  if (!words.v || words.params.path !== state.path) return;
  const params = {...words.params, chunk};
  const version = words.version;
  const key = JSON.stringify([params, version]);
  if (key === sidebarSyncKey) return;
  sidebarSyncKey = key;
  clearTimeout(sidebarSyncTimer);
  sidebarSyncController?.abort();
  sidebarSyncController = new AbortController();
  const signal = sidebarSyncController.signal;
  // Coalesce fast scrolling; keep one tiny lookup in flight, not a full word list.
  sidebarSyncTimer = setTimeout(async () => {
    try {
      const result = await api('navigation-position', params, signal);
      if (key !== sidebarSyncKey || version !== words.version || params.path !== state.path || signal.aborted) return;
      state.anchor = result.current?.anchor || '';
      words.schedule();
      if (result.index !== null) words.reveal(result.index);
      else if (!result.current && !params.q && words.total) words.reveal(0);
      else words.pendingReveal = null;
    } catch (error) {
      if (error.name !== 'AbortError' && key === sidebarSyncKey) sidebarSyncKey = '';
    }
  }, 80);
}

// Variable-height virtual Markdown. TanStack measures chunks, including late images.
class Reader {
  constructor() {this.element = $('#reader'); this.space = $('#reader-space'); this.nodes = new Map(); this.cache = new Map(); this.pending = new Set(); this.version = 0;}
  reset(doc) {
    this.cleanup?.(); this.controller?.abort(); this.controller = new AbortController(); this.version++;
    this.path = doc.path; this.count = doc.chunk_count;
    this.nodes.clear(); this.cache.clear(); this.pending.clear(); this.space.replaceChildren();
    this.element.scrollTop = 0;
    const instance = virtualizer(this.element, this.count, 650, () => this.schedule(), 2);
    Object.assign(this, instance);
    this.render();
  }
  schedule() {if (!this.frame) this.frame = requestAnimationFrame(() => {this.frame = null; this.render();});}
  async fetchPage(page) {
    if (this.pending.has(page)) return;
    this.pending.add(page);
    const version = this.version;
    try {
      const data = await api('chunks', {path: this.path, offset: page * 8, limit: 8}, this.controller.signal);
      if (version !== this.version) return;
      for (const item of data.items) this.cache.set(item.n, item.markdown);
      // Retain at most 48 chunks; the full Markdown is never held in the browser.
      const center = this.v.range?.startIndex || 0;
      const distant = [...this.cache.keys()].sort((a,b) => Math.abs(b-center)-Math.abs(a-center));
      while (this.cache.size > 48) this.cache.delete(distant.shift());
      this.pending.delete(page);
      this.schedule();
    } catch (e) {
      if (version === this.version && e.name !== 'AbortError') {
        toast(e.message);
        for (const [index, node] of this.nodes) if (Math.floor(index/8) === page && !node._loaded) {
          node.innerHTML = '<div class="chunk-loading"><button>加载失败，点击重试</button></div>';
          node.querySelector('button').onclick = () => {this.pending.delete(page); this.fetchPage(page);};
        }
      }
    }
  }
  render() {
    if (!this.v) return;
    this.space.style.height = `${this.v.getTotalSize()}px`;
    const visible = this.v.getVirtualItems();
    const wanted = new Set(visible.map(x => x.index));
    let removed = false;
    for (const [index, node] of this.nodes) if (!wanted.has(index)) {node.remove(); this.nodes.delete(index); removed = true;}
    if (removed) this.v.measureElement(null); // Disconnect observers of recycled DOM.
    for (const item of visible) {
      let node = this.nodes.get(item.index);
      if (!node) {
        node = document.createElement('section'); node.className = 'markdown-chunk'; node.dataset.index = item.index;
        this.nodes.set(item.index, node); this.space.append(node);
      }
      node.style.transform = `translateY(${item.start}px)`;
      const markdown = this.cache.get(item.index);
      if (markdown !== undefined && !node._loaded) {
        node.style.height = '';
        node.innerHTML = DOMPurify.sanitize(marked.parse(markdown), {FORBID_TAGS:['style','form','input','button','iframe'], FORBID_ATTR:['style']});
        node._loaded = true;
        this.prepare(node);
        this.v.measureElement(node);
      } else if (!node._loaded) {
        node.style.height = `${item.size}px`;
        if (!node.firstChild) node.innerHTML = '<div class="chunk-loading">正在加载正文…</div>';
        this.fetchPage(Math.floor(item.index/8));
      }
    }
    // Keep reading/accessibility order aligned with visual order when scrolling back.
    let next = null;
    for (const item of [...visible].reverse()) {
      const node = this.nodes.get(item.index);
      if (node.nextSibling !== next) this.space.insertBefore(node, next);
      next = node;
    }
    const first = this.v.range?.startIndex || 0;
    const total = this.v.getTotalSize();
    const percent = total <= this.element.clientHeight ? 100 : Math.min(100, Math.round(this.element.scrollTop / (total - this.element.clientHeight) * 100));
    $('#progress').style.width = `${percent}%`;
    $('#reading-status').textContent = `阅读进度 ${percent}% · 第 ${first + 1} / ${this.count} 段`;
    if (this.element.clientHeight > 0) {
      const atBottom = total > this.element.clientHeight && this.element.scrollTop + this.element.clientHeight >= total - 2;
      const position = this.element.scrollTop + 64;
      const current = visible.find(item => item.start <= position && item.end > position);
      const chunk = atBottom ? this.count - 1 : current?.index;
      if (chunk !== undefined && this.nodes.get(chunk)?._loaded) queueSidebarSync(chunk);
    }
  }
  prepare(node) {
    const base = sourceURL(this.path);
    for (const a of node.querySelectorAll('a[href]')) {
      const href = a.getAttribute('href');
      try {
        const url = new URL(href, base);
        if (url.origin === location.origin && url.pathname.startsWith(sourceBase.pathname) && /\.md$/i.test(url.pathname)) {
          a.href = '#' + new URLSearchParams({path: decodeURIComponent(url.pathname.slice(sourceBase.pathname.length)), anchor: decodeURIComponent(url.hash.slice(1))});
          a.dataset.document = decodeURIComponent(url.pathname.slice(sourceBase.pathname.length));
          a.dataset.anchor = decodeURIComponent(url.hash.slice(1));
        } else {a.href = url.href; a.target = '_blank'; a.rel = 'noopener noreferrer';}
      } catch {a.removeAttribute('href');}
    }
    for (const img of node.querySelectorAll('img')) {
      const src = img.getAttribute('src');
      if (src) img.src = new URL(src, base).href;
      img.loading = 'lazy'; img.decoding = 'async';
      // Library illustrations use a stable viewBox; reserve height before download.
      if (img.src.endsWith('.svg')) {img.style.aspectRatio = '1000 / 420'; img.addEventListener('load', () => {img.style.aspectRatio = `${img.naturalWidth} / ${img.naturalHeight}`;}, {once: true});}
      img.addEventListener('error', () => {const message = document.createElement('p'); message.className = 'row-detail'; message.textContent = `图片暂不可用：${img.alt || ''}`; img.replaceWith(message);}, {once:true});
    }
    for (const table of node.querySelectorAll('table')) {const wrapper = document.createElement('div'); wrapper.className = 'table-scroll'; table.replaceWith(wrapper); wrapper.append(table);}
  }
  async scrollTo(index) {
    index = Math.max(0, Math.min(this.count - 1, index));
    this.v.scrollToIndex(index, {align:'start'});
    this.schedule();
    // Fetch target page explicitly so distant navigation does not await scroll events.
    if (!this.cache.has(index)) await this.fetchPage(Math.floor(index/8));
    this.schedule();
  }
}
const reader = new Reader();
function saveRoute(path, anchor, replace = false) {
  const hash = '#' + new URLSearchParams({path, ...(anchor ? {anchor} : {})});
  if (location.hash !== hash) history[replace ? 'replaceState' : 'pushState'](null, '', hash);
  try {localStorage.setItem('word-root-route', JSON.stringify({path,anchor}));} catch {}
}
function selectPanel(panel) {
  document.body.dataset.panel = panel;
  document.querySelectorAll('.mobile-tabs button').forEach(b => b.classList.toggle('selected', b.dataset.panel === panel));
  files.v?._willUpdate(); words.v?._willUpdate(); reader.v?._willUpdate();
  words.schedule();
}
async function openDocument(path, anchor = '', updateRoute = true) {
  const token = ++state.openToken;
  try {
    const doc = await api('document', {path, anchor});
    if (token !== state.openToken) return;
    state.path = path; state.doc = doc; state.anchor = anchor;
    $('#reader-message').hidden = true;
    $('#breadcrumb').textContent = doc.category.replace(/^\d+_/, '') + ' / ' + path.split('/').pop();
    $('#current-root').textContent = doc.title.replace(/^\d+\s*·\s*/, '').split(' — ')[0];
    $('#current-root').title = doc.title;
    document.title = doc.title + ' · 词根阅读室';
    $('#source-link').href = sourceURL(path).href;
    $('#word-search').value = '';
    state.kind = doc.word_count ? 'word' : 'heading';
    updateNavTabs();
    selectPanel('reader');
    reader.reset(doc);
    searchWords(); files.schedule();
    if (updateRoute) saveRoute(path, anchor);
    if (doc.target) await reader.scrollTo(doc.target.chunk);
    else if (anchor) toast('未找到该定位标记，已打开文档开头。');
  } catch (e) {
    if (token !== state.openToken) return;
    toast(e.message);
    if (!state.doc) {$('#reader-message').hidden = false; $('#reader-message').textContent = '文档打开失败，请从左侧重新选择。';}
  }
}
async function jump(chunk, anchor) {
  state.anchor = anchor; saveRoute(state.path, anchor); words.schedule(); selectPanel('reader');
  await reader.scrollTo(chunk);
}
function updateNavTabs() {document.querySelectorAll('#nav-tabs button').forEach(b => b.classList.toggle('selected', b.dataset.kind === state.kind));}
$('#reader').addEventListener('click', e => {
  const a = e.target.closest('a[data-document]');
  if (!a || e.metaKey || e.ctrlKey || e.shiftKey) return;
  e.preventDefault();
  openDocument(a.dataset.document, a.dataset.anchor);
});
$('#global-search').addEventListener('input', debounce(searchFiles));
$('#word-search').addEventListener('input', debounce(searchWords));
$('#category').addEventListener('change', searchFiles);
$('#search-tabs').addEventListener('click', e => {
  if (!e.target.dataset.mode) return;
  state.mode = e.target.dataset.mode;
  $('#file-heading').textContent = state.mode === 'words' ? '单词搜索' : '所有文档';
  document.querySelectorAll('#search-tabs button').forEach(b => b.classList.toggle('selected', b.dataset.mode === state.mode));
  $('#global-search').placeholder = state.mode === 'words' ? '搜索单词、中文释义…' : '搜索文档、词根…';
  searchFiles();
});
$('#nav-tabs').addEventListener('click', e => {if (e.target.dataset.kind) {state.kind = e.target.dataset.kind; updateNavTabs(); searchWords();}});
$('.mobile-tabs').addEventListener('click', e => {if (e.target.dataset.panel) selectPanel(e.target.dataset.panel);});
$('#to-top').onclick = () => {if (state.path) {state.anchor = ''; saveRoute(state.path, ''); words.schedule(); reader.scrollTo(0);}};
$('#focus-toggle').onclick = () => {
  const focus = document.body.classList.toggle('focus');
  $('#focus-toggle').textContent = focus ? '显示侧栏' : '专注阅读';
  selectPanel('reader');
};
let fontSize = 16;
function changeFont(delta) {fontSize = Math.max(13, Math.min(23, fontSize + delta)); document.documentElement.style.setProperty('--body-size', fontSize + 'px');}
$('#font-smaller').onclick = () => changeFont(-1);
$('#font-larger').onclick = () => changeFont(1);
document.addEventListener('keydown', e => {
  if ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === 'k') {e.preventDefault(); document.body.classList.remove('focus'); $('#focus-toggle').textContent = '专注阅读'; selectPanel('files'); $('#global-search').focus();}
});
function readRoute() {
  const params = new URLSearchParams(location.hash.slice(1));
  return {path: params.get('path'), anchor: params.get('anchor') || ''};
}
const routeChanged = debounce(() => {const route = readRoute(); if (route.path !== state.path || route.anchor !== state.anchor) openDocument(route.path || '英语词根资料库/README.md', route.anchor, false);}, 0);
window.addEventListener('popstate', routeChanged);
window.addEventListener('hashchange', routeChanged);
async function init() {
  try {
    const stats = await api('stats');
    $('#library-stats').textContent = `${stats.documents.toLocaleString()} 份文档 / ${stats.words.toLocaleString()} 个单词`;
    for (const cat of stats.categories) {const option = document.createElement('option'); option.value = cat.category; option.textContent = `${cat.category.replace(/^\d+_/, '')} (${cat.count.toLocaleString()})`; $('#category').append(option);}
    searchFiles();
    let route = readRoute();
    if (!route.path) {try {route = JSON.parse(localStorage.getItem('word-root-route')) || route;} catch {}}
    await openDocument(route.path || '英语词根资料库/01_古典词根/2800_vend_C1615.md', route.anchor || '');
  } catch (e) {$('#reader-message').textContent = staticMode ? '在线资料加载失败，请检查网络并刷新重试。' : '无法连接本地服务，请运行 python3 server/server.py 后刷新。'; toast(e.message);}
}
init();
// Bounded metrics for manual QA; contains counts only, never Markdown content.
window.readerDiagnostics = () => ({document: state.path, chunks: reader.count, mountedChunks: reader.nodes.size, cachedChunks: reader.cache.size, fileRows: files.nodes.size, filePages: files.pages?.size, wordRows: words.nodes.size, wordPages: words.pages?.size});
