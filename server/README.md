# 词根阅读室

在浏览器中阅读 `word_root` 下的 Markdown。文档原件保持不变，索引和网页均位于 `server/`。

## 启动

需要 Python 3.9 或以上，无须安装 Python 包或 Node.js 运行依赖。

```sh
# 在项目根目录执行
python3 server/server.py
```

打开 http://127.0.0.1:8765 。停止服务按 Ctrl+C。更换端口：

```sh
python3 server/server.py --port 9000
```

首次启动建立磁盘索引，每次打开或刷新页面时按文件修改时间和大小增量更新。新增、修改或删除 Markdown 后，刷新浏览器即可，无须重启服务。页面会等待索引同步完成后再加载列表和正文；滚动时不重复扫描资料库。不要直接双击 HTML：浏览器需通过本地服务按需读取资料。

## 使用

- 左栏列出所有资料 Markdown，可按分类筛选；“文档”搜索标题和路径，“全库单词”搜索单词及中文释义。全库单词结果按所在文档分别列出。
- 第二栏列出当前文档的单词，点击跳到讲解。滚动正文时自动高亮当前单词，并将侧栏对应条目滚入可见区域；章节导航也支持同步。筛选时保留搜索条件，不匹配的条目不会强行滚动列表。没有单词的导读、索引等文档默认显示章节。
- 右栏显示 Markdown；相对文档链接、`#w-N` 单词锚点、图片、表格及代码块均可阅读。
- 支持浏览器前进/后退、带锚点的书签链接、记住上次打开的文档/单词、字体调整、专注阅读、手机宽度下切换面板。
- `⌘K` / `Ctrl+K` 聚焦资料库搜索。虚拟渲染只保留附近内容，浏览器自带的 `⌘F` / `Ctrl+F` 仅能搜索当前已渲染正文；查全库或当前文档单词请用页面搜索框。搜索不包含所有正文段落。

扫描范围：项目里的 `.md` 文件，排除隐藏目录（如 `.cache`、`.venv`）、`node_modules`、`__pycache__` 和 `server`。现有资料库、项目 README 和 `content/精讲` 均包含在内。

## 内存与滚动

使用 **TanStack Virtual Core 3.19.6**；这是独立开源组件，不是 W3C 或 Google 官方组件。

- 两个侧栏固定行高虚拟渲染，接口每页 60 条，每栏最多缓存 8 页。
- 正文使用动态高度虚拟渲染，按可视区域加前后各 2 个块挂载，ResizeObserver 测量文本及图片加载后的高度。
- 每次请求 8 个正文块，最多缓存 48 个原始 Markdown 块；滚出窗口的 DOM 和图片节点移除，切换文档取消旧请求并清空缓存。浏览器自身的图片/HTTP 缓存由浏览器管理。
- 长表格每 24 行分块并重复表头；长的平铺无序列表每 32 行分块；其他段落按约 4,800 字符组合。代码围栏及不可拆的单段保留完整。高度与索引元数据随块数增长，正文和 DOM 不随滚动历史无限增长。
- SQLite 索引存于 `server/.index.sqlite3`，文档、导航和正文分页均在服务端查询，不预加载全部文件到浏览器。可删除索引文件，下一次启动会重新生成。
- 开发者控制台 `readerDiagnostics()` 可以查看已挂载块数、正文缓存块数和侧栏缓存页数。

本地服务仅监听 `127.0.0.1`，不上传资料。依赖已打包到 `vendor/`，日常阅读可离线；文档里原有的外部链接、外部图片仍需网络。

## 文件

- `index.html`：页面入口。
- `style.css`：三栏、窄屏和正文样式。
- `app.js`：搜索、分页、跳转和虚拟滚动。
- `server.py`：标准库 HTTP 服务、Markdown 分段和 SQLite 增量索引。
- `vendor/`：TanStack Virtual、Marked 18.1.1、DOMPurify 3.4.17 与许可证。
- `test_server.py`：分段完整性、单词锚点、中文搜索、分页、增量更新和文件访问边界测试。

修改虚拟列表依赖后重新打包（只有开发时需要 Node.js）：

```sh
cd server
npm ci
npm run build:vendor
```

验证：

```sh
python3 -m unittest discover -s server -p 'test_*.py'
node --check server/app.js
```

## GitHub Pages

在线地址：https://apawn.github.io/word_root/ 。`.github/workflows/pages.yml` 在 `main` 更新后测试、构建并发布，也支持手动触发。仓库 Settings → Pages 的发布来源设为 **GitHub Actions**。

本地服务继续使用 SQLite，启动及刷新同步方式不变。静态构建使用独立临时索引，不读取或修改本地 SQLite。

手动构建、预览（输出目录必须尚不存在）：

```sh
python3 server/build_static.py --output .cache/pages-preview
python3 -m http.server 9000 --directory .cache/pages-preview
```

打开 http://localhost:9000 。生成物不提交 Git，线上由 Actions 上传。静态包包含网页、Markdown 原文、图片、分块正文及搜索索引，不包含 SQLite、原始 JSONL 或本地缓存。

- 静态页与本地页共用 UI，支持仓库子路径、相对链接和原有 `#w-N` 书签。
- 首次打开加载目录索引；单词及中文释义搜索在 Web Worker 中逐片查询，首次搜索获取全部搜索分片，之后可利用浏览器 HTTP 缓存。
- Worker 最多缓存 8 份数据文件及最近一次搜索结果页；正文及 DOM 继续使用原有有限缓存。全库搜索速度受网络影响，不提供正文全文搜索。
- 更新后数据使用新的版本目录；长时间打开的旧页面如遇加载失败，刷新即可。线上页面需要网络，不保证离线可用。

静态接口与本地接口一致性验证：

```sh
node --test server/test_static.mjs
```
