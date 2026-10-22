"""Layout for individually authored Chinese lessons; no generated filler prose."""
import collections
import hashlib
import html
import json
import re
import unicodedata
from pathlib import Path

BASE=Path(__file__).resolve().parents[1]
CONTENT=BASE/'content/精讲'
OUT=BASE/'英语词根资料库'
PLAN_PATH=CONTENT/'配图计划.json'
IMAGE_PLAN=json.loads(PLAN_PATH.read_text()) if PLAN_PATH.exists() else {}

def images_paused():
    return IMAGE_PLAN.get('mode')=='defer'

def image_digest(value):
    return hashlib.sha256(json.dumps(value,ensure_ascii=False,sort_keys=True).encode()).hexdigest()

def history_filename(word):
    slug=re.sub('[^a-z0-9]+','-',word.lower()).strip('-')
    return f'{slug}-{hashlib.sha256(word.encode()).hexdigest()[:8]}.svg'

def word_has_image(w):
    return (OUT/'assets/evolution'/history_filename(w['word'])).exists() and (not images_paused() or IMAGE_PLAN.get('words',{}).get(w['word'])==image_digest(w['history']))

def root_has_image(r,lesson):
    signature={key:lesson[key] for key in ['core','image','branches']}
    return (OUT/'assets'/f'{r["id"]}.svg').exists() and (not images_paused() or IMAGE_PLAN.get('roots',{}).get(r['id'])==image_digest(signature))

def plain_markdown(value):
    # Diagram text is literal: preserve reconstruction stars and underscores.
    return re.sub(r'([\\`*_{}\[\]<>])',r'\\\1',value)

def load_lessons():
    words={}
    for path in sorted(CONTENT.glob('words_*.json')):
        for item in json.loads(path.read_text()):
            assert item['word'] not in words, item['word']
            for key in ['ipa','meaning','sense','split','history','explanation','usage','contrast','examples']:
                assert item.get(key), (item['word'],key)
            assert len(item['examples'])>=2,item['word']
            assert len(item['history'])>=2,item['word']
            words[item['word']]=item
    roots={}
    for path in sorted(CONTENT.glob('roots_*.json')):
        for item in json.loads(path.read_text()):
            assert item['id'] not in roots, ('duplicate root',item['id'])
            assert len(item['words'])==len(set(item['words'])), ('duplicate family word',item['id'])
            excluded=item.get('exclude',{})
            assert isinstance(excluded,(dict,list)) and all(isinstance(word,str) for word in excluded), (item['id'],'exclude must contain word keys, not entry objects')
            for key in ['meaning','core','image','intro','forms','contrasts','practice']:
                assert isinstance(item.get(key,''),str), (item['id'],key,'must be text')
            roots[item['id']]=item
    assert set(words)=={w for r in roots.values() for w in r['words']}, 'Authored words and lesson lists differ'
    return roots,words

def wrapped(value,max_width):
    lines=[];line='';width=0
    for char in value:
        step=2 if unicodedata.east_asian_width(char) in 'WF' else 1
        # Keep closing punctuation with the preceding phrase at a line boundary.
        if line and width+step>max_width and char in '，。；：！？、）》】」』”’.,;:!?)]':
            line+=char;width+=step
            continue
        if char=='\n' or width+step>max_width:
            # Keep Latin words intact when a mixed Chinese/English line wraps.
            tail=''
            if char!='\n' and re.match(r'[A-Za-zÀ-ž0-9]',char):
                match=re.search(r'[A-Za-zÀ-ž0-9_-]+$',line)
                if match and match.start()>0:
                    tail=match.group();line=line[:match.start()]
            lines.append(line.rstrip());line=tail
            width=sum(2 if unicodedata.east_asian_width(c) in 'WF' else 1 for c in tail)
            if char=='\n':continue
        if not line and char.isspace():continue
        line+=char;width+=step
    if line:lines.append(line)
    return lines

def svg_start(width,height,title):
    return [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img">',
            f'<title>{html.escape(title)}</title>',
            '<style>text{font-family:Arial,"PingFang SC","Microsoft YaHei",sans-serif;fill:#202020}.note{fill:#727272}</style>',
            f'<rect x="1" y="1" width="{width-2}" height="{height-2}" rx="18" fill="#fdfdfd" stroke="#dedede" stroke-width="1.5"/>']

def draw_history(word,nodes):
    assert not images_paused(), 'Image generation is paused at the user’s request'
    rows=[];height=38
    for label,meaning in nodes:
        a=wrapped(label,62);b=wrapped(meaning,68)
        h=len(a)*31+len(b)*27+46
        rows.append((a,b,h));height+=h
    height+=8
    svg=svg_start(1000,height,word+'：词形演化')
    y=42
    for i,(a,b,h) in enumerate(rows):
        for line in a:
            svg.append(f'<text x="500" y="{y}" text-anchor="middle" font-size="25" font-weight="600">{html.escape(line)}</text>');y+=31
        y+=5
        for line in b:
            svg.append(f'<text class="note" x="500" y="{y}" text-anchor="middle" font-size="20">{html.escape(line)}</text>');y+=27
        if i<len(rows)-1:
            svg.append(f'<text class="note" x="500" y="{y+12}" text-anchor="middle" font-size="29">↓</text>')
        y+=41
    svg.append('</svg>')
    name=history_filename(word)
    target=OUT/'assets/evolution'/name;target.parent.mkdir(parents=True,exist_ok=True)
    target.write_text('\n'.join(svg))
    return name

def draw_root(r,lesson):
    assert not images_paused(), 'Image generation is paused at the user’s request'
    branches=lesson['branches'];width=1200
    core_lines=wrapped(lesson['core'],64)
    image_lines=wrapped(lesson['image'],90)
    image_y=62+(len(core_lines)-1)*38+41
    arrow_y=image_y+(len(image_lines)-1)*31+52
    first_row_y=arrow_y+60
    branch_lines=[(wrapped(b[0],26),wrapped(b[1],31)) for b in branches]
    row_heights=[]
    for start in range(0,len(branches),3):
        row_heights.append(max(150,max(len(a)*34+16+len(b)*26+38 for a,b in branch_lines[start:start+3])))
    height=first_row_y+sum(row_heights)
    svg=svg_start(width,height,r['root']+'：意义分支')
    for j,line in enumerate(core_lines):
        svg.append(f'<text x="600" y="{62+j*38}" text-anchor="middle" font-size="31" font-weight="600">{html.escape(line)}</text>')
    for j,line in enumerate(image_lines):
        svg.append(f'<text class="note" x="600" y="{image_y+j*31}" text-anchor="middle" font-size="22">{html.escape(line)}</text>')
    svg.append(f'<text class="note" x="600" y="{arrow_y}" text-anchor="middle" font-size="30">↓</text>')
    for i,(labels,words) in enumerate(branch_lines):
        x=200+(i%3)*400;y=first_row_y+sum(row_heights[:i//3])
        for j,line in enumerate(labels):
            svg.append(f'<text x="{x}" y="{y+j*34}" text-anchor="middle" font-size="26" font-weight="600">{html.escape(line)}</text>')
        for j,line in enumerate(words):
            svg.append(f'<text class="note" x="{x}" y="{y+len(labels)*34+6+j*26}" text-anchor="middle" font-size="19">{html.escape(line)}</text>')
    svg.append('</svg>');(OUT/'assets'/f'{r["id"]}.svg').write_text('\n'.join(svg))

def word_markdown(w,index):
    if not images_paused():draw_history(w['word'],w['history'])
    evolution=[f'![{w["word"]} 的词源演化](../assets/evolution/{history_filename(w["word"])})'] if word_has_image(w) else ['\n\n↓\n\n'.join(f'**{plain_markdown(label)}**  \n{plain_markdown(meaning)}' for label,meaning in w['history'])]
    lines=[f'<a id="w-{index}"></a>','',f'### {index}. {w["word"]} — {w["meaning"]}','',
           f'**音标**：{w["ipa"]}','', '**先抓住这个画面**','',w['sense'],'',
           '**怎么拆**','',w['split'],'', '**怎么变成今天的意思**','',
           *evolution,'',w['explanation'],'',
           '**常见搭配与例句**','',w['usage'],'']
    for en,zh in w['examples']:lines += ['> '+en,'',zh,'']
    lines += ['**别混淆**','',w['contrast'],'']
    return lines

def render_root(r,lesson,words):
    missing=set(r['family'])-words.keys()
    assert not missing,(r['id'],'unwritten words',sorted(missing))
    if not images_paused():draw_root(r,lesson)
    overview=[f'![{r["root"]} 的意义分支](../assets/{r["id"]}.svg)'] if root_has_image(r,lesson) else [f'**{lesson["core"]}**','',lesson['image'],'']+[f'- **{label}**：{examples}' for label,examples in lesson['branches']]
    lines=[f'# {r["rank"]:04d} · {r["root"]} — {lesson["meaning"]}','',
           '[逐词精讲目录](../00_逐词精讲目录.md) · [总目录](../00_总目录_按常用程度.md)','',
           '## 核心词根与来源','',lesson['intro'],'',
           *overview,'',
           '## 词形与演化规律','',lesson['forms'],'',
           '## 单词速览（常用到不常用）','', '| 单词 | 音标 | 核心意思 |','|---|---|---|']
    for i,name in enumerate(r['family'],1):
        w=words[name];lines.append(f'| [{name}](#w-{i}) | {w["ipa"]} | {w["meaning"]} |')
    lines+=['','## 逐词讲解','']
    for i,name in enumerate(r['family'],1):lines+=word_markdown(words[name],i)
    if lesson.get('contrasts'):lines+=['## 这一组要分清什么','',lesson['contrasts'],'']
    if lesson.get('practice'):lines+=['## 串起来练习','',lesson['practice'],'']
    (OUT/r['file']).write_text('\n'.join(lines))

def finish(roots,lessons,words):
    completed=[r for r in roots if r['id'] in lessons]
    used={w for r in completed for w in r['family']}
    lines=['# 逐词精讲目录','',
           '这里的词根页已逐词写成中文讲解，每个单词都有来源演化、构词分析、搭配、双语例句和辨析。按全库学习顺序排列。新增部分先用文字箭头记录演化，图片以后统一补。','',
           '[按单词查精讲](00_精讲单词反查.md) · [阅读方法](阅读方法.md) · [待补图清单](待补图清单.md)','',
           '| 词根 | 核心意象 | 逐词讲解数 |','|---|---|---:|']
    for r in completed:lines.append(f'| [{r["root"]}]({r["file"]}) | {lessons[r["id"]]["meaning"]} | {len(r["family"])} |')
    lines+=['',f'当前完成 {len(completed)} 个词根页、{len(used)} 个不同单词的逐词讲解。其余页面仍为旧版资料整理，尚未达到这里的讲解深度。','', '[全库目录](00_总目录_按常用程度.md)','']
    (OUT/'00_逐词精讲目录.md').write_text('\n'.join(lines))
    illustrated={w for w in used if word_has_image(words[w])}
    pending_words=used-illustrated
    pending_roots=[r for r in completed if not root_has_image(r,lessons[r['id']])]
    status={'root_pages':len(completed),'unique_words':len(used),'word_occurrences':sum(len(r['family']) for r in completed),'examples':sum(len(words[w]['examples']) for w in used),'diagrams':len(illustrated),'pending_word_diagrams':len(pending_words),'pending_root_diagrams':len(pending_roots),'image_generation':'deferred' if images_paused() else 'enabled','completed_root_ids':[r['id'] for r in completed]}
    status['authored_sha256']=hashlib.sha256(json.dumps({'roots':lessons,'words':words},ensure_ascii=False,sort_keys=True).encode()).hexdigest()
    (OUT/'data/精讲进度.json').write_text(json.dumps(status,ensure_ascii=False,indent=2))
    reverse=collections.defaultdict(list)
    for r in completed:
        for i,word in enumerate(r['family'],1):
            reverse[word].append(f'[{r["root"]}]({r["file"]}#w-{i})')
    word_index=['# 精讲单词反查','', '[按词根学习](00_逐词精讲目录.md)','',
                '这里只列已逐词完成精讲的单词。点击词根可直接跳到该单词的讲解。','',
                '| 单词 | 核心意思 | 进入讲解 |','|---|---|---|']
    for word in sorted(used):
        word_index.append(f'| {word} | {words[word]["meaning"]} | {" · ".join(reverse[word])} |')
    (OUT/'00_精讲单词反查.md').write_text('\n'.join(word_index)+'\n')
    pending=['# 待补图清单','', '[逐词精讲目录](00_逐词精讲目录.md)','',
             '2026-10-21 起，按要求暂停生成图片。暂停时已配图并校验完成 **71 个词根页、3,729 个单词**；这些已有图片保留。后续正文继续写，来源演化先以文字箭头呈现。','',
             '缺图从 **capit-（头）、fer-（承载）、ordin-（排列）、rect-/reg-（直与引导）、reg-/rex-（王权）、regul-（规则）** 这一批开始。文件前面的排序号可能变化，下面的链接会随目录同步更新。','',
             '下面只列需要补图的词根。进入对应页面即可查看已写好的文字演化链。','']
    pending_root_pages=[r for r in completed if r in pending_roots or any(word in pending_words for word in r['family'])]
    for r in pending_root_pages:pending.append(f'- [{r["root"]}]({r["file"]})')
    if not pending_root_pages:pending+=['目前没有需要补图的词根。']
    (OUT/'待补图清单.md').write_text('\n'.join(pending)+'\n')
    (OUT/'data/待补图清单.json').write_text(json.dumps({'checkpoint':IMAGE_PLAN.get('checkpoint',{}),'root_ids':[r['id'] for r in pending_roots],'words':sorted(pending_words),'root_files':{r['id']:r['file'] for r in pending_roots}},ensure_ascii=False,indent=2))
    refs=['# 逐词精讲核对资料','', '[来源与许可](../来源与许可.md)','',
          '中文讲解、语义说明及双语例句由 AI 逐词编写；例句不是引自下列网站。文字演化链与已有配图依据核对过的词形路径，必要的不确定性在正文说明；新增图片暂缓。下列资料用于词源和读音核对。旧版开放词典记录仍保存在 data/词条来源.jsonl。','']
    for word in sorted(used):
        refs += [f'## {word}','']
        for url in words[word].get('sources',[]):refs.append(f'- [{url.split("/")[2]}：{word}]({url})')
        refs.append('')
    (OUT/'参考资料/逐词精讲核对资料.md').write_text('\n'.join(refs))
    return status
