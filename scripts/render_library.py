"""Render learning pages, with attribution collected in separate reference files."""
import collections
import csv
import html
import importlib.metadata
import json
import re
import shutil
import unicodedata
from pathlib import Path
from urllib.parse import quote
from wordfreq import zipf_frequency
from build_catalog import BASE, CACHE, OUT, load_lexicon, components
from explanatory import load_lessons,render_root,finish as finish_lessons,images_paused

LANG={'Latin':'拉丁语','Greek':'古希腊语','Latin from Greek':'拉丁语 ← 古希腊语','Latin and Greek':'拉丁语／古希腊语','Greek/Latin':'古希腊语／拉丁语','Latin, Greek':'拉丁语／古希腊语','Greek from Hebrew':'古希腊语 ← 希伯来语',
      'en':'英语','enm':'中古英语','ang':'古英语','la':'拉丁语','la-new':'新拉丁语','la-med':'中世纪拉丁语','grc':'古希腊语','fr':'法语','fro':'古法语','frm':'中古法语','de':'德语','gem-pro':'原始日耳曼语','gmw-pro':'原始西日耳曼语','ine-pro':'原始印欧语','non':'古诺尔斯语','nl':'荷兰语','it':'意大利语','es':'西班牙语','ar':'阿拉伯语','ota':'奥斯曼土耳其语','ja':'日语','zh':'汉语','hi':'印地语','sa':'梵语','fa':'波斯语','he':'希伯来语','pt':'葡萄牙语','itc-pro':'原始意大利语','el':'现代希腊语'}
POS={'noun':'名词','verb':'动词','adj':'形容词','adv':'副词','name':'专有名词','prefix':'前缀／前置成分','suffix':'后缀／后置成分','prep':'介词','conj':'连词','det':'限定词','pron':'代词','intj':'感叹词','num':'数词','particle':'小品词'}
CORPUS={}
AUTHOR_NOUNS=set('action agent reception perception conception deception capability recipient caption misconception preconception inspection spectator prediction dictionary construction structure submission transmission permission description manuscript biology biography photograph geography telephone formation vision conversion conclusion friendship water hand friend'.split())
AUTHOR_ADJS=set('active agile capable captive incipient capacious visible thermal handmade waterproof'.split())
AUTHORED={}
HYPHENS=set('-\u00ad\u2010\u2011\u2012\u2013\u2014\u2212\ufe63\uff0d')

def hyphenated_word(word):
    return any(char in HYPHENS for char in word)

def md(s):
    return re.sub(r'\s+',' ',str(s)).replace('|','\\|').replace('<','&lt;').replace('>','&gt;').replace('[','\\[').replace(']','\\]').replace('*','\\*').replace('_','\\_')

def source_link(w):return 'https://en.wiktionary.org/wiki/'+quote(w,safe='-')+'#English'

def strip_accents(s):
    return ''.join(x for x in unicodedata.normalize('NFD',s.lower()) if not unicodedata.combining(x))

def etym_text(d):
    s=d.get('etymology_text','')
    if s.startswith(('Etymology tree\n','PIE word\n','PIE root\n')):
        m=re.search(r'\n(?=(?:From|Borrowed|Inherited|By |Probably|Perhaps|Unknown|Uncertain|Compound|Coined|Clipping|Back-formation|Derived|Equivalent|Ultimately|A |An |First |Possibly|See |Of |Onomatopoeic))',s)
        s=s[m.end():] if m else ''
    # Do not render malformed template markup as authoritative prose.
    if 'data-lang=' in s or '"terms" :' in s:return ''
    return s.strip()

def chinese(w, ds, ec, prefer_dict=True):
    if prefer_dict:
        tr=ec.get(w,ec.get(w.lower(),{})).get('translation','')
        if tr:
            lines=tr.replace('\\n','\n').splitlines()
            return '；'.join(lines[:3]).strip()[:450], 'ECDICT'
    ts=[]
    for d in ds:
        for t in d.get('translations',[]):
            if t.get('word') and t['word'] not in ts:
                ts.append(t['word'])
    if ts:return '、'.join(ts[:8]), 'Wiktionary 汉语译词（参考，非逐义对齐）'
    return '', ''

def ipa(ds, ecrow):
    sounds=[]
    for d in ds:
        for s in d['sounds']:
            ip=s.get('ipa','')
            if not ip or any(x in s.get('tags',[]) for x in ['obsolete','archaic','nonstandard']):continue
            if ip.startswith('['):continue
            tags=s.get('tags',[])
            if any(t in tags for t in ['Received-Pronunciation','General-British','UK']):label='英'
            elif any(t in tags for t in ['General-American','US']):label='美'
            elif not tags:label='通用／未标方言'
            else:label='/'.join(tags)
            if (label,ip) not in sounds:sounds.append((label,ip))
    selected=[]
    for target in ['英','美','通用／未标方言']:
        pair=next((s for s in sounds if s[0]==target),None)
        if pair:selected.append(pair)
        if len(selected)==2:break
    if not selected and sounds:selected=sounds[:1]
    if selected:return '；'.join(v if k=='通用／未标方言' else f'{k} {v}' for k,v in selected),'Wiktionary'
    p=ecrow.get('phonetic','')
    if p:
        p=p.replace("'",'ˈ').replace(':','ː').replace('ә','ə').replace('ɚ','ɚ')
        return '/'+p.strip('/')+'/', 'ECDICT（原库未逐词标明方言；规范化了重音及长度符号）'
    return '', ''

def pick_entry(w,r,lex):
    ds=lex[w]
    via=r['family'][w].get('via')
    tokens={strip_accents(t) for t in re.findall(r'[A-Za-zÀ-žΑ-ωἀ-῾]+',r.get('origin','')) if len(t)>3}
    def score(d):
        s=0
        if via and any(via in components(t) for t in d['etymology_templates']):s+=200
        if r['id'].startswith('C'):
            es=strip_accents(etym_text(d))
            s+=sum(8 for token in tokens if re.search(r'(?<!\w)'+re.escape(token)+r'(?!\w)',es))
        if etym_text(d):s+=4
        if w in AUTHORED and d['pos']==('noun' if w in AUTHOR_NOUNS else 'adj' if w in AUTHOR_ADJS else 'verb'):s+=5
        if any(s.get('examples') for s in d['senses']):s+=1
        if d.get('etymology_number') in [None,'1',1]:s+=2
        if d['pos'] in ['noun','verb','adj']:s+=1
        return s
    best=max(ds,key=score)
    same=[d for d in ds if d['pos']==best['pos'] and (etym_text(d)==etym_text(best) or (best.get('etymology_number') is not None and d.get('etymology_number')==best.get('etymology_number')))]
    return best,same

def make_word(w,r,lex,ec,authored):
    d,same=pick_entry(w,r,lex)
    main_etym=etym_text(lex[w][0])
    normal_sense=etym_text(d)==main_etym or not main_etym
    zh,zhsource=chinese(w,same,ec,normal_sense)
    ip,ipsource=ipa(same,ec.get(w,ec.get(w.lower(),{})))
    ety=etym_text(d)
    splits=[]
    for t in d['etymology_templates']:
        cs=components(t)
        if len(cs)>1:
            x=t.get('expansion','')
            if not x or len(x)>450 or any(z in x for z in ['"terms"','data-lang=','"keyword_label"','"lang_name"']):x=' + '.join(cs)
            if x not in splits:splits.append(x)
    exs=[]
    for sd in same:
        for s in sd['senses']:
            for ex in s.get('examples',[]):
                text=ex.get('text','')
                if ex.get('type')!='example' or len(text)>420:continue
                if not re.search(r'(?<![a-z])'+re.escape(w.lower())+r'(?:s|es|ed|ing)?(?![a-z])',text.lower()):continue
                complete=bool(re.search(r'[.!?][”"\']?$',text)) and len(text.split())>=4
                quality=100*complete-abs(len(text)-90)*0.1
                if 'collocation' in ex.get('tags',[]):quality-=20
                exs.append((quality,text,s['glosses'][-1]))
    example=translation=example_gloss=example_url=example_attribution=''
    exsource=''
    if w in authored and normal_sense:
        example,translation=authored[w];exsource='编写的学习例句'
    elif exs:
        _,example,example_gloss=max(exs,key=lambda x:x[0]);exsource='Wiktionary 用例'
    elif normal_sense and w.lower() in CORPUS:
        candidates=CORPUS[w.lower()]
        compatible=[e for e in candidates if e.get('pos')==d['pos']]
        if compatible:
            # Prefer a WordNet sense sharing content words with the selected definition.
            stop={'a','an','the','of','to','or','and','in','is','be','that','for','with','as','something','someone'}
            target=set(re.findall('[a-z]+',' '.join(s['glosses'][-1] for s in d['senses'][:3]).lower()))-stop
            chosen=max(compatible,key=lambda e:len(target&set(re.findall('[a-z]+',e['gloss'].lower()))))
            if not target&set(re.findall('[a-z]+',chosen['gloss'].lower())):chosen=None
        else:chosen=None
        if not chosen:chosen=next((e for e in candidates if e['source']=='Tatoeba'),None)
        if chosen:
            example=chosen['text'];example_gloss=chosen.get('gloss','');example_url=chosen['url'];exsource=chosen['source']
            example_attribution=('作者：'+chosen['author']+'；句子 #'+chosen['ref']+'；CC BY 2.0 FR') if exsource=='Tatoeba' else 'Princeton University；WordNet 3.0；synset '+chosen['ref']
    gs=[s['glosses'][-1] for s in d['senses'][:2]]
    return dict(word=w,pos=d['pos'],glosses=gs,zh=zh,zhsource=zhsource,ipa=ip,ipasource=ipsource,etym=ety,split=splits[:3],example=example,example_zh=translation,example_gloss=example_gloss,example_source=exsource,example_url=example_url,example_attribution=example_attribution,zipf=zipf_frequency(w,'en'),homograph=not normal_sense)

def diagram(r,display_zh):
    title=r['root']; words=list(r['family'])[:6]
    esc=html.escape
    title=title if len(title)<64 else title[:61]+'…'
    z=display_zh if len(display_zh)<35 else display_zh[:32]+'…'
    s=['<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="420" viewBox="0 0 1000 420">',
       '<rect width="1000" height="420" rx="20" fill="#f7f4ed"/>',
       '<style>text{font-family:Arial,"PingFang SC","Microsoft YaHei",sans-serif}.small{font-size:15px;fill:#53646c}.word{font-size:23px;fill:#183b43}</style>',
       f'<text x="36" y="40" class="small">{r["rank"]:04d} · {esc(r["kind"])} · 词族关系示意</text>',
       '<rect x="110" y="65" width="780" height="105" rx="15" fill="#173e43"/>',
       f'<text x="500" y="110" text-anchor="middle" font-size="{22 if len(title)>40 else 30}" fill="white">{esc(title)}</text>',
       f'<text x="500" y="146" text-anchor="middle" font-size="20" fill="#d2e6de">{esc(z)}</text>']
    for i,w in enumerate(words):
        x=175+(i%3)*325;y=235+(i//3)*90
        s.append(f'<path d="M500 170 L{x} {y-22}" fill="none" stroke="#afc6bc" stroke-width="2"/>')
    for i,w in enumerate(words):
        x=175+(i%3)*325;y=235+(i//3)*90
        s.extend([f'<rect x="{x-140}" y="{y-23}" width="280" height="58" rx="10" fill="white" stroke="#d1ded7"/>',
                  f'<text x="{x}" y="{y+13}" text-anchor="middle" class="word" font-size="{18 if len(w)>22 else 23}px">{esc(w[:32])}</text>'])
    s.append('<text x="36" y="397" class="small">连线表示本资料库中的词族归属，不表示所有词之间有直接派生关系；历史路线见正文。</text></svg>')
    (OUT/'assets'/f'{r["id"]}.svg').write_text('\n'.join(s))

def write(path,text):
    p=OUT/path;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(text)

def write_references(references):
    letters=collections.defaultdict(list)
    for word,ref in sorted(references.items(),key=lambda item:item[0].lower()):
        letter=word[0].upper()
        letters[letter if letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' else '其他'].append((word,ref))
    index=['# 词条与例句来源','', '[来源与许可](../来源与许可.md)','',
           '学习正文的词条链接、发音及释义出处、例句作者和许可集中保存在这里。','',
           '**[逐词精讲核对资料](逐词精讲核对资料.md)**：重写页面所用的词源和读音核对资料。精讲中的双语例句由 AI 逐词编写。','']
    for letter,items in sorted(letters.items()):
        filename=f'词条来源_{letter}.md'
        index.append(f'- [{letter}：{len(items):,} 个词]({filename})')
        lines=[f'# {letter}：词条与例句来源','', '[返回来源目录](README.md)','']
        for word,ref in items:
            lines += [f'## {md(word)}','',f'- [Wiktionary 词条与修订历史]({source_link(word)})']
            if ref['ipa']:lines.append('- 发音资料：'+'；'.join(sorted(ref['ipa'])))
            if ref['zh']:lines.append('- 中文释义资料：'+'；'.join(sorted(ref['zh'])))
            lines.append('')
            for example in sorted(ref['examples']):
                sentence,source,url,attribution=example
                origin=f'[{md(source+"；"+attribution)}]({url})' if url else md(source)
                lines += [f'> {md(sentence)}','',f'例句来源：{origin}','']
        write('参考资料/'+filename,'\n'.join(lines))
    write('参考资料/README.md','\n'.join(index)+'\n')

def main():
    global CORPUS,AUTHORED
    if (CACHE/'examples-index.json').exists():CORPUS=json.loads((CACHE/'examples-index.json').read_text())
    roots=json.loads((CACHE/'catalog.json').read_text());lex=load_lexicon()
    lessons,lesson_words=load_lessons()
    # Apply the reading preference to every derived view; retain the source
    # catalog so hyphenated vocabulary can be restored in a later edition.
    for r in roots:
        r['family']={word:relation for word,relation in r['family'].items() if not hyphenated_word(word)}
        r['unmatched']=[word for word in r['unmatched'] if not hyphenated_word(word)]
        if r['id'] in lessons:
            lesson=lessons[r['id']]
            for word in lesson.get('words',[]):
                assert word in lex,(word,'missing lexical evidence')
                r['family'].setdefault(word,dict(via=None,depth=0,evidence='逐词词源核对'))
            for word in lesson.get('exclude',[]):r['family'].pop(word,None)
            r['meaning_zh']=lesson['meaning']
        r['family']=dict(sorted(r['family'].items(),key=lambda item:(-zipf_frequency(item[0],'en'),item[0])))
        r['best_zipf']=max((zipf_frequency(word,'en') for word in r['family']),default=0)
        import math
        rates=[10**(zipf_frequency(word,'en')-9) for word in r['family'] if re.fullmatch('[a-z]+',word)][:20]
        r['score']=round(math.log10(sum(rates))+9,3) if rates else 0
    roots.sort(key=lambda r:(-r['score'],r['root'],r['id']))
    for rank,r in enumerate(roots,1):
        r['rank']=rank
        r['file']=re.sub(r'/\d{4}_',f'/{rank:04d}_',r['file'])
    expected={r['file'] for r in roots}
    for folder in ['01_古典词根','02_英语词基','03_词缀与组合形式']:
        for old in (OUT/folder).glob('[0-9][0-9][0-9][0-9]_*.md'):
            if str(old.relative_to(OUT)) not in expected:old.unlink()
    ec={row['word']:row for row in csv.DictReader((CACHE/'ecdict.csv').open())}
    notes=dict(line.rstrip('\n').split('\t',1) for line in (CACHE/'root-notes.tsv').open())
    authored={}
    if (CACHE/'examples.tsv').exists():
        for line in (CACHE/'examples.tsv').open():
            p=line.rstrip('\n').split('\t');authored[p[0]]=p[1:3]
    AUTHORED=authored
    (OUT/'assets').mkdir(parents=True,exist_ok=True)
    all_words=set();reverse=collections.defaultdict(list);quality=[];index=[];useddata={};references={}
    occurrence=collections.Counter();unique_has=collections.defaultdict(set)
    for r in roots:
        if not r['meaning_zh'] and r['headword']:
            r['meaning_zh']=chinese(r['headword'],lex[r['headword']],ec)[0]
        shortzh=r['meaning_zh'] or r['meaning']
        if not images_paused():diagram(r,shortzh)
        record=[make_word(w,r,lex,ec,authored) for w in r['family']]
        if r['id'] in lessons:
            for w in record:
                authored_word=lesson_words[w['word']]
                w.update(ipa=authored_word['ipa'],zh=authored_word['meaning'],
                         split=[authored_word['split']],etym=authored_word['explanation'],
                         example=authored_word['examples'][0][0],example_zh=authored_word['examples'][0][1],
                         example_source='逐词编写的学习例句',example_url='',example_attribution='',
                         ipasource='核对后整理；见逐词精讲核对资料',zhsource='逐词编写的中文释义')
        q=collections.Counter()
        for w in record:
            all_words.add(w['word']);reverse[w['word']].append(r)
            useddata[w['word']]=lex[w['word']]
            ref=references.setdefault(w['word'],dict(ipa=set(),zh=set(),examples=set()))
            if w['ipasource']:ref['ipa'].add(w['ipasource'])
            if w['zhsource']:ref['zh'].add(w['zhsource'])
            if w['example']:ref['examples'].add((w['example'],w['example_source'],w['example_url'],w['example_attribution']))
            for field in ['ipa','zh','etym','example','split']:
                if w[field]:q[field]+=1;occurrence[field]+=1;unique_has[field].add(w['word'])
        quality.append(dict(id=r['id'],root=r['root'],file=r['file'],words=len(record),**q,unmatched=len(r['unmatched'])))
        lines=[f'# {r["rank"]:04d} · {r["root"]} — {md(shortzh[:180])}',
               '', '[总目录](../00_总目录_按常用程度.md)', '',
               f'**类型**：{r["kind"]}　｜　**来源语言**：{LANG.get(r["language"],r["language"])}', '',
               '## 核心含义与来源', '',f'- 核心含义：{md(shortzh)}']
        if r['meaning']:lines.append(f'- 英文含义：{md(r["meaning"])}')
        lines += [f'- 词形：{md(", ".join(r["aliases"]) or r["root"])}','']
        if r['id'].startswith('C'):
            if r['origin']:lines += [f'**来源词形**：{md(r["origin"])}', '']
        else:
            histories={}
            for hd in lex[r['headword']]:
                if etym_text(hd):histories.setdefault(etym_text(hd),hd)
            if len(histories)>1:
                lines += ['**多个词源／构词路径**：同一拼写可能有不同来源；以下按词性和含义分别列出。','']
            for j,(history,hd) in enumerate(histories.items(),1):
                lines += [f'**来源记录 {j}**（{POS.get(hd["pos"],hd["pos"])}；{md(hd["senses"][0]["glosses"][-1])}）', '',md(history),'']
        if r['id'] in notes:lines += ['## 演化说明', '',notes[r['id']],'']
        lines += ['## 词族图', '',f'![{md(r["root"])} 词族图](../assets/{r["id"]}.svg)', '']
        if record:lines += ['## 单词速览（常用到不常用）', '', '| 单词 | 音标 | 释义 |','|---|---|---|']
        for i,w in enumerate(record,1):
            gloss=w['zh'] or '【英文】'+w['glosses'][0]
            lines.append(f'| [{md(w["word"])}](#w-{i}) | {md(w["ipa"])} | {md(gloss[:220])} |')
        if record:lines+=['','## 逐词详解','']
        for i,w in enumerate(record,1):
            pronunciation=f'　｜　**音标**：{md(w["ipa"])}' if w['ipa'] else ''
            lines += [f'<a id="w-{i}"></a>', '',f'### {i}. {w["word"]}', '',
                      f'**词性**：{POS.get(w["pos"],w["pos"])}{pronunciation}', '']
            if w['zh']:lines += [f'**中文释义**：{md(w["zh"])}','']
            lines += [f'**英文义项**：{" / ".join(md(g) for g in w["glosses"])}','']
            if w['split']:lines += ['**构词拆分**：'+'；'.join(md(x) for x in w['split']),'']
            if w['etym']:lines += ['**词源与演化**：', '',md(w['etym']),'']
            if w['example']:
                label='例句' if re.search(r'[.!?][”"\']?$',w['example']) and len(w['example'].split())>=4 else '用法示例／搭配（非完整句）'
                lines += [f'**{label}**：','',f'> {md(w["example"])}','']
                if w['example_zh']:lines += [w['example_zh'],'']
                elif w['example_gloss']:lines += [f'该用例对应义项：{md(w["example_gloss"])}','']
        if r['unmatched']:
            lines += ['## 其他候选词', '']
            lines += [f'- {md(w)}' for w in r['unmatched']]
            lines+=['']
        write(r['file'],'\n'.join(lines))
        if r['id'] in lessons:render_root(r,lessons[r['id']],lesson_words)
        index.append(r)
        if r['rank']%500==0:print('Rendered',r['rank'],flush=True)
    write_references(references)
    # Coverage and reproducibility data are kept outside learning pages.
    stats=dict(entries=len(roots),groups=dict(collections.Counter(r['group'] for r in roots)),unique_words=len(all_words),word_occurrences=sum(len(r['family']) for r in roots),field_occurrences=dict(occurrence),field_unique={k:len(v) for k,v in unique_has.items()},empty_entries=sum(not r['family'] for r in roots),source_rows=1680,manual_root_notes=len(notes),wordfreq_version=importlib.metadata.version('wordfreq'),date='2026-10-21')
    write('data/统计.json',json.dumps(stats,ensure_ascii=False,indent=2))
    write('data/条目清单.json',json.dumps(roots,ensure_ascii=False,indent=2))
    write('data/原始词根清单.json',(CACHE/'classical-roots.json').read_text())
    for name,rows in [('覆盖明细.csv',quality)]:
        with (OUT/'data'/name).open('w',newline='') as f:
            fields=['id','root','file','words','ipa','zh','etym','example','split','unmatched']
            wr=csv.DictWriter(f,fieldnames=fields);wr.writeheader();wr.writerows(rows)
    # Offline, word-level source records allow repairs without live network access.
    with (OUT/'data'/'词条来源.jsonl').open('w') as f:
        for w in sorted(useddata):
            for d in useddata[w]:f.write(json.dumps(d,ensure_ascii=False)+'\n')
    for title,items,path in [('总目录：按常用程度',roots,'00_总目录_按常用程度.md'),('字母索引',sorted(roots,key=lambda r:r['root'].strip('-').lower()),'00_字母索引.md'),('古典词根学习顺序',[r for r in roots if r['group']=='01_古典词根'],'00_古典词根学习顺序.md')]:
        ls=[f'# {title}','', '[逐词精讲目录](00_逐词精讲目录.md) · [使用说明](README.md) · [覆盖与缺项](覆盖与缺项.md)','', '同形异源条目分别保留；词缀和自由词基不计作纯词根。文件名前四位是本版全库排序号。','', '| 排序 | 条目 | 类型 | 核心义／释义 | 收词数 |','|---:|---|---|---|---:|']
        for r in items:ls.append(f'| {r["rank"]} | [{md(r["root"])}]({r["file"]}) | {r["kind"]} | {md((r["meaning_zh"] or r["meaning"])[:150])} | {len(r["family"])} |')
        write(path,'\n'.join(ls)+'\n')
    letters=collections.defaultdict(list)
    for w,rs in sorted(reverse.items(),key=lambda kv:kv[0].lower()):letters[w[0].upper()].append((w,rs))
    ls=['# 单词反查词根','', '**[优先查看已重写的精讲单词](00_精讲单词反查.md)**','', '一个词可能同时含多个构词成分；多个链接不自动意味着它们全部互为同源词。','']
    for letter,pairs in sorted(letters.items()):
        fn=f'索引/单词_{letter}.md';ls.append(f'- [{letter}：{len(pairs):,} 个词]({fn})')
        text=[f'# {letter}：单词 → 词根／词基','', '[返回反查入口](../00_单词反查.md)','', '| 单词 | 相关条目 |','|---|---|']
        for w,rs in pairs:text.append(f'| {md(w)} | '+ '、'.join(f'[{md(r["root"])}](../{r["file"]})' for r in rs)+' |')
        write(fn,'\n'.join(text)+'\n')
    write('00_单词反查.md','\n'.join(ls)+'\n')
    if lessons:print('Explanatory lessons',finish_lessons(roots,lessons,lesson_words),flush=True)
    print(json.dumps(stats,ensure_ascii=False,indent=2),flush=True)

if __name__=='__main__':main()
