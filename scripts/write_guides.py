import collections
import csv
import hashlib
import importlib.metadata
import json
import shutil
from pathlib import Path

B=Path(__file__).resolve().parents[1];O=B/'英语词根资料库';C=B/'.cache'
S=json.loads((O/'data/统计.json').read_text());R=json.loads((O/'data/条目清单.json').read_text())
P=json.loads((O/'data/精讲进度.json').read_text())
groups=collections.Counter(r['group'] for r in R)
q=list(csv.DictReader((O/'data/覆盖明细.csv').open()))
classic=[r for r in R if r['id'].startswith('C')]
supp_aff=[r for r in R if r['id'].startswith('A')]
native=[r for r in R if r['id'].startswith('B')]
def put(p,t):(O/p).write_text(t)

put('README.md',f'''# 英语词根资料库

先打开 **[逐词精讲目录](00_逐词精讲目录.md)**。这里按常用到少见排列，每个词从一个能想象的画面讲起，再说明拆法、演化、用法和容易混淆的地方。

**已逐词重写 {P['root_pages']} 个词根页、{P['unique_words']} 个不同单词，配 {P['diagrams']} 张单词演化图和 {P['examples']} 条原创双语例句。**

后续先写正文，暂停生成图片；演化过程用文字箭头保留。需要补图的词根见 **[待补图清单](待补图清单.md)**。

全库还保留 {S['entries']:,} 个词根、词基和构词成分页，收录 {S['unique_words']:,} 个不同词形。其余页面仍是原来的资料整理版；完整目录不等于已经全部完成精讲。

## 从这里开始

- **[逐词精讲目录](00_逐词精讲目录.md)**：中文语感、拆分、文字演化或已有图示、搭配、双语例句和辨析；目前只包括已经逐词重写的页面。
- **[精讲单词反查](00_精讲单词反查.md)**：直接查一个词，跳到它的完整讲解。
- **[古典词根学习顺序](00_古典词根学习顺序.md)**：适合以拉丁／希腊词根扩充词汇量，从常用到少见。
- **[全库总目录：按常用程度](00_总目录_按常用程度.md)**：同时包括词根、自由词基和词缀。
- **[字母索引](00_字母索引.md)**：按词根或词基的拼写查找。
- **[单词反查](00_单词反查.md)**：从已知单词找到相关词族。
- [阅读方法](阅读方法.md)：音标、词源、拆分、图示和排序的解释。
- **[覆盖与缺项](覆盖与缺项.md)**：实际覆盖率、空缺条目和“全部”的明确边界。
- [来源与许可](来源与许可.md)：数据版本、作者归属和复用许可。

## 本版覆盖什么

| 范围 | 条目数 | 收录口径 |
|---|---:|---|
| 基础拉丁／希腊词根与构词成分 | {len(classic):,} | 完整接收来源表的 1,680 行；6 行明确的重复／异形记录归并，原行号保留 |
| 补充词缀与组合形式 | {len(supp_aff):,} | 开放词典有构词成分条目，且能由明确英语构词记录连到至少一个学习词 |
| 英语自由词基 | {len(native):,} | 词形 Zipf ≥ 3.5，有词源记录，且至少连接两个常用度达标的派生词；包含本源词与借词 |

**这三个数量不能相加后称作“纯词根总数”。** 自由词基可能仍可继续拆分；组合形式和语法词缀也不是同一个概念。同形而异源的条目原则上分开。

英语借词来源广泛，生产性复合和科技造词仍在发生；没有可据以保证“世界上所有英语词根均已穷尽”的封闭公认名单。本版能保证的是对上述有限清单和筛选规则的覆盖，不能声称字面意义上的绝对全部。医学专科、历史方言词、分类学名称、借词及更深层原始语言词根仍可能遗漏。

## 每篇包含什么

精讲页先把词根讲成一个具体画面，例如“把两样东西绑起来”或“伸手拿住”。接着说明这个画面怎样走到单词今天的意思，而不是把几个中文词根义硬加起来。

每个单词都有音标、简短释义、独立讲解、来源演化、常见搭配、至少两条英文例句及中文翻译。能现代拆分的就拆；经过借词、音变才成为今天词形的，则讲清来路。不确定的来源会明确保留不确定性。

例句由 AI 逐词编写，用来演示对应义项；不是冒充新闻或书籍的引文。词源与发音核对资料集中在[精讲参考资料](参考资料/逐词精讲核对资料.md)，旧版材料的出处和署名保存在[参考资料](参考资料/README.md)。

当前学习词表暂略带连字符的单词；词根和词缀名称中的连字符仍表示构词位置。

## 文件结构

```text
英语词根资料库/
├── README.md
├── 00_逐词精讲目录.md     已完整重写的词根页
├── 00_古典词根学习顺序.md
├── 00_总目录_按常用程度.md
├── 00_字母索引.md
├── 00_单词反查.md
├── 01_古典词根/           每条目一个 md
├── 02_英语词基/           每条目一个 md
├── 03_词缀与组合形式/     每条目一个 md
├── 索引/                 按字母拆分的单词反查
├── assets/               词根意义分支图
│   └── evolution/        已完成的单词纵向演化图
├── 参考资料/             集中保存词条出处和例句署名
├── data/                 原始清单、展开词条来源、覆盖统计
├── 来源与许可.md
└── LICENSES/             第三方许可证
```

文件名前面的数字是全库学习顺序。正文和图片均可离线阅读；在线词典链接用于进一步核对。打开 Markdown 时请保留整个文件夹，让相对图片路径继续有效。大词族可用页内单词表直接跳转。
''')

put('阅读方法.md','''# 阅读方法

[返回入口](README.md) · [逐词精讲目录](00_逐词精讲目录.md)

## 先学一个画面，再记几个词

以 lig- 为例，先想“把两样东西绑起来”。人绑到同一个阵营里，可以理解 ally；骨头之间起连接作用的是 ligament；责任把一个人约束住，可以帮助理解 obligation。

这些画面帮助理解词义，不代替历史证据。比如 release 也有“解除束缚”的感觉，但不能因此说它来自 ligāre。

## 每个词怎样读

1. **先抓画面**：用一句大白话弄清这个词到底在说什么。
2. **看怎么拆**：区分现代英语还能看见的构词，和拉丁语、法语等语言里早已完成的构词。
3. **沿文字箭头或已有图往下走**：看来源词形怎样经过借入、变化，成为今天的英语词。
4. **读演化链后的说明**：理解具体动作为什么能说抽象事情，例如“拿住”怎样成为“理解”。
5. **带入例句**：看这个意思在句子里怎么用，再看与近义词的边界。

同一个词可能有多种常用意思。它们不一定能用一个画面全部解释，更不能为了整齐编造词源。遇到俚语、专业义或有争议的来源，会单独说明。

## 文字演化与已有图示

从 71 个词根页、3,729 个单词的已配图检查点之后，新写内容暂用文字箭头；后期补图位置见[待补图清单](待补图清单.md)。

## 图里有两种关系

**词根页顶端的分支图**按意义把同族词放在一起，帮助建立联系。它不表示这些英语词互相派生。

**单词下面的纵向图**展示经过核对的来源路径。有些节点合并了同一语言中的构词过程；文字会解释这些步骤。历史不明确时不补造祖先；来自同一祖先的两个旁支也不画成前后相传。

## 音标怎么看

`ˈ` 是主重音，`ˌ` 是次重音，`ː` 表示长音。先找到重读音节，再读整个词，不要把词根拆开后各自拼音。

精讲页选一种常见读音；英美差异或词性差异影响学习时会分别列出。例如 use 作名词的结尾通常是 /s/，作动词通常是 /z/。单列一种读法不表示其他标准读法都错。

## 怎样理解拆分

`unreliable = un- + reliable` 是现代还能使用的构词；`ally ← 古法语 alier ← 拉丁语 alligāre` 则是历史来源。你看不到 ally 中的 lig，不代表没有关系，只是词形在历史中变了。

历史上的异形也不是任意替换公式：receive / reception 可以帮助记忆，但不能把所有 -ceive 随手换成 -cept 来造词。

## 常用到不常用，怎么排

单词使用 wordfreq 的英语词频排序；词根根据词族中常见词的频率估计学习先后。正文保留顺序，不展示分数。它方便从熟悉的词走向陌生词，不是考试大纲，也不是词根自身的精确频率。

排序的数据版本与算法留在[来源资料](来源与许可.md)和生成脚本中。遇到自己的专业词，也可以先读，不必机械按编号背完。

## 精讲与原资料的区别

[逐词精讲目录](00_逐词精讲目录.md)列出的页面已逐词写成上述形式。全部例句都有中文翻译，每词至少两条。例句为 AI 原创，没有伪造外部出处。

其他页面仍保留原来的词典资料、词族归类和既有用例，讲解深度不同。原语料的出处与署名集中保存在参考资料中。全库具体覆盖情况见[覆盖统计](覆盖与缺项.md)。

带连字符的单词暂略；词根、前后缀名称中的连字符仍表示构词位置。
''')

total=S['unique_words']
lines=['# 覆盖与缺项','', '[返回入口](README.md)','',
       '**本版没有完成“所有英语词根、所有单词、所有字段均齐全”的绝对目标。以下是可核对的实际范围。**','',
       f'全库 {S["entries"]:,} 个词根／词基／构词成分条目；{total:,} 个不重复词／词组；跨词族重复计数后有 {S["word_occurrences"]:,} 次词条展示。','',
       '## 字段覆盖（按不重复词形统计）','', '| 字段 | 至少在一处有资料的词形数 | 占比 | 缺项词形数 |','|---|---:|---:|---:|']
for k,name in [('ipa','音标'),('zh','中文参考释义'),('etym','词源原文'),('example','例句或用法示例'),('split','词典明确的构词拆分')]:
    n=S['field_unique'][k];lines.append(f'| {name} | {n:,} | {n/total:.1%} | {total-n:,} |')
lines += ['','同一拼写可能在不同页面选中不同词源组；“至少在一处有资料”不表示它在每个页面、每个义项下字段齐全。例句统计包含已标明的搭配，不等于同等数量的完整句。拆分缺项不一定是资料缺陷：有些词不适合做现代英语层面的拆分。','',
          '## 来源清单的覆盖','',
          '基础表 1,680 行全部保留在 `data/原始词根清单.json`，每行可通过 source_ids 找到所属 Markdown。6 行明确的重复／异形记录被归并为同一页。没有以此推断所有语言、所有专业领域的英语词根已经齐备。','',
          '以下条目在当前学习词表中没有可展开的英语词条；其中包括原资料未匹配的条目，以及略去连字符词后词表为空的条目。页面仍保留词根或来源说明：','']
for r in R:
    if not r['family']:lines.append(f'- [{r["root"]}]({r["file"]}) — {r["meaning_zh"] or r["meaning"]}；{r["id"]}')
lines+=['','## 仍需完成的内容','',
        '- 继续逐词核对词族关系，纠正原词根表和开放词典中的误归类。',
        '- 补齐上表中缺失的读音、中文释义和可靠例句，并逐项校对词性、词义与读音。',
        '- 扩充专科医学、冷僻科学分类词、历史方言、其他借词来源及较低频自由词基。',
        f'- 按精讲格式继续逐词重写。目前完成 {P["root_pages"]} 个词根页、{P["unique_words"]} 个不同单词；其余页面仍保留原资料。',
        '- 对同形多义造成的词频偏差、异源根的归并边界和源表重复分组继续复核。','',
        '## 可机器核对的文件','',
        '- [逐页字段覆盖 CSV](data/覆盖明细.csv)',
        '- [完整条目清单 JSON](data/条目清单.json)',
        '- [原始根表 JSON](data/原始词根清单.json)',
        '- [统计 JSON](data/统计.json)',
        '- `data/词条来源.jsonl`：本版使用的词典记录，供离线追溯和修订。','']
put('覆盖与缺项.md','\n'.join(lines))

put('来源与许可.md','''# 来源、版本与许可

[返回入口](README.md)

整理和下载日期：2026-10-21。每个词条的在线链接指向其英文 Wiktionary 页面；修订历史可从该页面继续查看。词条链接、音标和释义出处、例句署名集中保存在[参考资料](参考资料/README.md)。在线页面之后可能变化，离线 JSONL 保留了本版采用的记录。

## 基础词根表

- [University of Vermont：Wikipedia-derived list of Greek and Latin roots](https://www.uvm.edu/~jbailly/courses/Etymology/additionalNotes/wikipedia_Derived%20list%20Greek%20and%20Latin%20roots.html)。采用其 1,680 行快照；HTML 表格经清理、同形检查、明确重复归并、中文核心义整理和词频排序。
- 原始贡献者：Wikipedia 各条目贡献者，大学课程页面保存其派生表。参见 [Wikipedia 的根表入口](https://en.wikipedia.org/wiki/List_of_Greek_and_Latin_roots_in_English) 与相应修订历史。来源表并非语言学界认定的英语全部词根名录。
- Wikipedia 衍生文字依 [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) 署名、标明修改并以相同方式共享。更早的页面可能另有其历史许可，原页面及修订记录为归属依据。

## 英文词典、词源、构词和发音

- [Kaikki 英语机器可读词典](https://kaikki.org/dictionary/English/index.html)，由 Tatu Ylonen 等维护的 Wiktextract 工具从 English Wiktionary 提取。
- 采用下载时网站标示的 **2026-09-02 Wiktionary dump，2026-10-03 提取版本**；主数据为网站 postprocessed English JSONL。完整输入有 1,492,836 条词性／词源记录，经筛选后再建立学习词族。
- [Wiktextract 项目](https://github.com/tatuylonen/wiktextract)；学术引用：Tatu Ylonen, *Wiktextract: Wiktionary as Machine-Readable Structured Data*, LREC 2022, pp. 1317–1325。
- 贡献者：各 Wiktionary 词条贡献者。每个词在参考资料中提供页面链接，满足词条层面的可追溯署名；参见 [Wiktionary 版权说明](https://en.wiktionary.org/wiki/Wiktionary:Copyrights)。本版按 **CC BY-SA 4.0** 使用其原创词典文字。
- 为避免把词典收录的第三方长引文当作可自由转载材料，本版仅采用 `type=example` 的用例，不复制 `type=quotation` 的新闻、小说等引文。
- 改动：筛选词性和词形，清理导出模板碎片，保留英文说明，增加中文学习注释、索引、排序和关系图。自动提取不能替代语言学审校。

## 中文参考释义与补充音标

- [ECDICT](https://github.com/skywind3000/ECDICT)，维护者 skywind3000 及贡献者；采用仓库的 ecdict.csv，770,611 行。
- 仓库标示 **MIT License**，原许可证保存在 [LICENSES/ECDICT-MIT.txt](LICENSES/ECDICT-MIT.txt)。中文释义可能同时包含多个词性和义项；不是逐词源组重新翻译。
- 补充音标只使用库中已存在的记录；重音和长度等字符作了规范化。源库音标仍可能存在转写差异或错误，不能把它当成全部人工校对的统一英式／美式音标。

## 用例补充

- **WordNet 3.0**：Princeton University，2006；通过 [NLTK 的原版语料镜像](https://github.com/nltk/nltk_data) 取得数据库。每条例句在参考资料中注明 synset 编号及来源。许可证原文见 [LICENSES/WordNet-3.0.txt](LICENSES/WordNet-3.0.txt)；[项目主页](https://wordnet.princeton.edu/)。句首和句末标点可能为阅读方便统一。
- **Tatoeba**：采用 [官方英语详细句子导出](https://downloads.tatoeba.org/exports/per_language/eng/eng_sentences_detailed.tsv.bz2)，每条被使用的句子在参考资料中署名作者，并链接原始句子 ID。依据其[下载许可说明](https://tatoeba.org/en/downloads)使用 **CC BY 2.0 FR**，其中部分句子亦可能采用 CC0；本版保守保留署名。具体句子保留原文，未提供中文翻译时不声称已翻译。
- 旧版另有 85 条学习例句及中文译文；精讲页的例句由 AI 逐词编写，数量见 [精讲进度](data/精讲进度.json)。
- 曾检查 ManyThings 的双语数据入口，但未取得其下载文件；本版不把它列为已使用的数据源。

## 常用度排序

- [wordfreq](https://github.com/rspeer/wordfreq)，Robyn Speer 等；使用版本 **3.1.1**。
- 词频主要反映截至约 **2021 年**的多来源语料。本版未声称它是 2026 年实时词频，也没有从频率推出考试等级或普遍适用的学习价值。
- 程序和数据的具体许可见仓库 [LICENSE.txt](https://github.com/rspeer/wordfreq/blob/master/LICENSE.txt) 与 [NOTICE.md](https://github.com/rspeer/wordfreq/blob/master/NOTICE.md)。本版只保存用到的派生分数；排序方法见[阅读方法](阅读方法.md)。

## 本资料库的整理内容

中文词根义、中文学习说明、原创例句、关系图、索引和编排与使用的 Wiktionary／Wikipedia 文字作为本汇编按 **CC BY-SA 4.0** 提供；ECDICT、WordNet、Tatoeba 的材料仍保留各自上述许可和归属。复用时保留本文件、相应许可证和词条／句子链接，标明你的修改。

SVG 是本地生成的图，没有外部照片授权依赖。词根分支图展示意义联系；精讲页的纵向图展示核对过的词形路径，必要的不确定性在文字中说明。

精讲页的中文讲解、语义联想和双语例句由 AI 逐词编写。事实核对所用的词典、词源网站等集中列于[逐词精讲核对资料](参考资料/逐词精讲核对资料.md)；没有把词典长篇释义或其引用的文学原文整段移入精讲正文。
''')
(O/'LICENSES').mkdir(exist_ok=True)
shutil.copyfile(C/'ecdict-LICENSE',O/'LICENSES/ECDICT-MIT.txt')
shutil.copyfile(C/'wordnet/wordnet/LICENSE',O/'LICENSES/WordNet-3.0.txt')
put('LICENSES/本汇编许可.md','''# 本汇编许可

本汇编的整理内容及其 CC BY-SA 来源文字按 [Creative Commons Attribution-ShareAlike 4.0 International](https://creativecommons.org/licenses/by-sa/4.0/) 提供。第三方材料保留各自许可证；详细署名和修改说明见 [来源与许可](../来源与许可.md)。

Tatoeba 句子适用 [CC BY 2.0 France](https://creativecommons.org/licenses/by/2.0/fr/) 或相应句子的更宽松许可；各句作者和链接在[参考资料](../参考资料/README.md)中保留。
''')

# Stable row-to-page mapping proves the finite-source coverage claim.
mapping={sid:r['file'] for r in R for sid in r['source_ids']}
assert set(mapping)=={f'C{i:04d}' for i in range(1,1681)}
put('data/原始行到页面.json',json.dumps(mapping,ensure_ascii=False,indent=2))
print('Guides written; source rows mapped',len(mapping))
