# coding: utf-8
from pathlib import Path
import json
from lesson_authoring import entry as E
BASE=Path(__file__).resolve().parents[1];OUT=BASE/'.cache/batch200/drafts/rewrite_spec'
ID='C0535';TAG='291_hen';SHARED=['hyphen','hyphenate','hyphenated'];EXCLUDE_REASON='按当前常用阅读范围暂略神学、哲学及古修辞中的冷门术语。'
H=[['希腊 hypó〔在下面〕＋ hén〔一〕','两个构词材料合在一起'],['希腊 hyphén〔合在一起〕→ 后期拉丁 hyphen → 英语 hyphen','先有合为一体的意思，后用作连接符号名称']]
W=[E('hyphenation','/ˌhaɪfəˈneɪʃən/','连字符的使用；用连字符连接或断行','决定哪里需要那条短横线，以及断行时怎样把一个词分开。','英语 hyphen + -ation 构成行为名词；现代也可与动词 hyphenate 配套理解。不是从英语 one 变出 hen。',H+[['英语 hyphen + -ation → hyphenation','使用连字符的过程、方式或规则']],'编辑说 check the hyphenation，是让你检查该连的词有没有连、该断的地方断得对不对。排版软件中的 automatic hyphenation，通常让较长的词在行尾分开，好让文字排得更均匀。','automatic hyphenation；hyphenation rules；check the hyphenation。','hyphen 是符号本身；hyphenation 是使用它的做法。它既能涉及复合词，也能涉及同一个词的行尾断开，不能一律理解为造新词。',('Turn off automatic hyphenation before exporting the document.','导出文档前，先关闭自动断字功能。'),('The editor checked the spelling and hyphenation of every heading.','编辑检查了每个标题的拼写和连字符用法。'),sources=['https://www.etymonline.com/word/hyphenation','https://en.wiktionary.org/wiki/hyphenation#English','https://www.stylemanual.gov.au/grammar-punctuation-and-conventions/punctuation/hyphens'])]
ROOT=dict(meaning='一；成为一个整体',core='hén 的画面是“合成一个单位”，在 hyphen 里留下了清楚的痕迹。',image='短横线把两边拉到一起，让读者把它们当成一个单位看。',intro='希腊 hén 是“一”的形式之一。hypó“在下面”和 hén 组合成 hyphén，表示合在一起；这个词后来成了连字符的名称。日常最值得掌握的是这一小组排版、写作词。',forms='hyphen 是名词，也可作动词；hyphenate 是常见动词形式，hyphenated 描写带连字符的形式，hyphenation 指这种做法。',branches=[['符号与使用','hyphen；hyphenate；hyphenated；hyphenation']],contrasts='英语 hen“母鸡”来自日耳曼语，不属于希腊 hén“一”的这条线。不要看到 hen 字母相同就归类。',practice='打开一篇文档，找一个连字符，再区分这是连接复合词，还是单词在行尾断开。',sources=['https://www.etymonline.com/word/hyphen','https://www.oxfordlearnersdictionaries.com/definition/english/hyphen'])
m=json.loads((BASE/'.cache/batch200/rewrite_spec.json').read_text());r=next(x for x in m['roots']if x['id']==ID);c=next(x for x in json.loads((BASE/'.cache/catalog.json').read_text())if x['id']==ID);keep={w['word']for w in W}|set(SHARED);excluded={w:EXCLUDE_REASON for w in(set(r['family'])|set(c['family'])|set(c.get('unmatched',[])))-keep}
ROOT['id']=ID;ROOT['words']=list(dict.fromkeys([w for w in r['family']if w in keep]+[w for w in SHARED if w not in r['family']]));ROOT['exclude']=excluded
assert all(w['word']in m['owned_words']for w in W)
assert not(set(c['family'])|set(c.get('unmatched',[])))-set(ROOT['words'])-set(excluded)
assert {w['word']for w in W}<=set(ROOT['words'])
for w in W:assert len(w['examples'])>=2 and all(len(n)==2 and all(isinstance(x,str)and x for x in n)for n in w['history'])
for k,d in [('roots',[ROOT]),('words',W)]: (OUT/f'{k}_batch200_spec_{TAG}.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
print(ID,len(W),'new,',len(SHARED),'shared')
