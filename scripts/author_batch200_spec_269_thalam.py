# coding: utf-8
from pathlib import Path
import json
from lesson_authoring import entry as E
BASE=Path(__file__).resolve().parents[1];OUT=BASE/'.cache/batch200/drafts/rewrite_spec'
ID='C1504';TAG='269_thalam';SHARED=['hypothalamus'];EXCLUDE_REASON='按当前范围暂略婚礼诗旧称与冷门手术细分词。'
W=[E('thalamus','/ˈθæləməs/','丘脑','大脑深部一个重要的信息中转与协调区域。','借自解剖拉丁名称，远源是希腊 thálamos“内室、卧房”。它的字面来源是房间，不是英语 hill；中文丘脑并不是英文逐字翻译。',[['希腊 thálamos〔内室、卧房〕','房屋内部的空间'],['拉丁 thalamus；后用于解剖命名','旧词进入身体结构名称'],['英语 thalamus','脑部结构：丘脑']],'可先把它想成脑内的中转站：许多感觉信号在送往大脑皮层的途中，会在丘脑接受处理和转接。但它不是机械地接一下线，还参与注意、觉醒等活动；“中转站”是帮助入门的比喻。','the thalamus；signals passing through the thalamus；复数 thalami。','hypothalamus 是下丘脑，hypo- 指下方位置；它与体温、饥饿和激素调节密切相关。丘脑与下丘脑相邻，却不是同一块结构的两种叫法。',('The diagram places the thalamus deep inside the brain.','示意图把丘脑标在大脑深部。'),('Many sensory signals pass through the thalamus before reaching the cortex.','许多感觉信号在到达大脑皮层前，会经过丘脑。'),sources=['https://www.etymonline.com/word/thalamus','https://en.wiktionary.org/wiki/thalamus','https://www.nimh.nih.gov/news/science-updates/2017/brain-relay-also-key-to-holding-thoughts-in-mind','https://pubmed.ncbi.nlm.nih.gov/1678190/'])]
ROOT=dict(meaning='内室；解剖名中的丘脑',core='本来是屋里的内室，后来进入解剖命名。',image='记“内室”这个旧词义，再把现代 thalamus 放到脑深部的信息通路中。',intro='学这组最有用的是分清 thalamus 与 hypothalamus。词源帮助记名称，现代功能则要另外理解；不能从“房间”直接推演出完整脑功能。',forms='希腊 thálamos 经拉丁 thalamus 进入解剖词汇；hypo- 加在前面表示下方。',branches=[['丘脑','thalamus：重要的信息中转与协调区域'],['下丘脑','hypothalamus：位置在其下方，参与多种身体状态调节']],contrasts='不要把 hypo- 理解成丘脑功能减弱，也不要把两种结构互当同义词。',practice='用位置和主要作用分别说出丘脑、下丘脑的区别。',sources=['https://www.etymonline.com/word/thalamus','https://www.nimh.nih.gov/news/science-updates/2017/brain-relay-also-key-to-holding-thoughts-in-mind'])
m=json.loads((BASE/'.cache/batch200/rewrite_spec.json').read_text());r=next(x for x in m['roots']if x['id']==ID);c=next(x for x in json.loads((BASE/'.cache/catalog.json').read_text())if x['id']==ID);keep={w['word']for w in W}|set(SHARED);excluded={w:EXCLUDE_REASON for w in(set(r['family'])|set(c['family'])|set(c.get('unmatched',[])))-keep}
ROOT['id']=ID;ROOT['words']=list(dict.fromkeys([w for w in r['family']if w in keep]+[w for w in SHARED if w not in r['family']]));ROOT['exclude']=excluded
assert all(w['word']in m['owned_words']for w in W)
assert not(set(c['family'])|set(c.get('unmatched',[])))-set(ROOT['words'])-set(excluded)
assert {w['word']for w in W}<=set(ROOT['words'])
for w in W:assert len(w['examples'])>=2 and all(len(n)==2 and all(isinstance(x,str)and x for x in n)for n in w['history'])
for k,d in [('roots',[ROOT]),('words',W)]: (OUT/f'{k}_batch200_spec_{TAG}.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
print(ID,len(W),'new,',len(SHARED),'shared')
