# coding: utf-8
from pathlib import Path
import json
from lesson_authoring import entry as E
BASE=Path(__file__).resolve().parents[1];OUT=BASE/'.cache/batch200/drafts/rewrite_spec'
ID='C1417';TAG='279_stern';SHARED=[];EXCLUDE_REASON='按当前范围暂略昆虫胸部骨板的细分名称，优先掌握人体胸骨及常见形容词。'
H=[['希腊 stérnon〔胸、胸骨〕','身体前方的胸部名称'],['新拉丁 sternum → 英语 sternum','解剖学中的胸骨']]
W=[E('sternum','英 /ˈstɜːnəm/；美 /ˈstɜːrnəm/','胸骨','胸前正中那块长而扁的骨。','经新拉丁 sternum 借入，接希腊 stérnon 胸部、胸骨。-um 是借词保留的名词形式，不能把它拆成英语 stern“严厉的”加后缀。',H,'把胸廓想成一个保护内部器官的框架：肋骨从两侧围过来，胸骨位于前方正中。若干肋骨借软骨与它相接，但不是所有肋骨都直接接到胸骨上。','the sternum；behind the sternum；sternum fracture。','breastbone 是胸骨的日常说法，sternum 是解剖名称。stern 还可表示严厉或船尾，都不是从这块胸骨派生。',('The diagram places the sternum in the centre of the chest.','图中把胸骨标在胸部正中。'),('The model shows cartilage linking the upper ribs to the sternum.','模型展示了连接上部肋骨与胸骨的软骨。'),sources=['https://www.etymonline.com/word/sternum','https://en.wiktionary.org/wiki/sternum','https://www.cancer.gov/publications/dictionaries/cancer-terms/def/sternum']),
E('sternal','英 /ˈstɜːnəl/；美 /ˈstɜːrnəl/','胸骨的；胸骨附近的','告诉你某个位置或结构与胸骨有关。','sternum 去掉借词词尾 -um，使用 stern- + -al 构成形容词。',H+[['英语 sternum → sternal','由骨名形成表示位置或关系的形容词']],'它像贴在解剖描述前的一个位置标签。sternal region 把范围缩到胸骨附近，sternal angle 则指胸骨上的特定角度与连接部位；单独一个 sternal 并不表示疾病。','the sternal region；the sternal angle；a sternal fracture。','sternal 指向胸骨，pectoral 指向胸部，范围更宽；sternal 也不是“严厉地”的意思。',('The textbook labels the sternal angle on the chest diagram.','课本在胸部图上标出了胸骨角。'),('The researcher measured movement in the sternal region.','研究人员测量了胸骨区域的运动。'),sources=['https://en.wiktionary.org/wiki/sternal','https://www.merriam-webster.com/dictionary/sternal','https://www.cancer.gov/publications/dictionaries/cancer-terms/def/sternum'])]
ROOT=dict(meaning='胸；胸骨',core='把身体前方正中的胸骨当作位置中心。',image='胸骨在胸前正中，肋骨从两侧围向它。',intro='stern- 的这一支来自希腊 stérnon，现代主要见于解剖名称 sternum 和形容词 sternal。两词足以覆盖一般阅读最常遇到的用途。',forms='sternum 是新拉丁借词；sternal 使用去掉 -um 后的 stern- 加 -al。',branches=[['骨骼名称','sternum：胸骨'],['位置与关系','sternal：胸骨的']],contrasts='英语 stern“严厉的”及 stern“船尾”另有来源，不要因为拼写相同就加入这条解剖词源线。',practice='遇到 sternal region 时，先在心里定位胸前正中的胸骨。',sources=['https://www.etymonline.com/word/sternum','https://en.wiktionary.org/wiki/sternal'])
m=json.loads((BASE/'.cache/batch200/rewrite_spec.json').read_text());r=next(x for x in m['roots']if x['id']==ID);c=next(x for x in json.loads((BASE/'.cache/catalog.json').read_text())if x['id']==ID);keep={w['word']for w in W}|set(SHARED);excluded={w:EXCLUDE_REASON for w in(set(r['family'])|set(c['family'])|set(c.get('unmatched',[])))-keep}
ROOT['id']=ID;ROOT['words']=list(dict.fromkeys([w for w in r['family']if w in keep]+[w for w in SHARED if w not in r['family']]));ROOT['exclude']=excluded
assert all(w['word']in m['owned_words']for w in W)
assert not(set(c['family'])|set(c.get('unmatched',[])))-set(ROOT['words'])-set(excluded)
assert {w['word']for w in W}<=set(ROOT['words'])
for w in W:assert len(w['examples'])>=2 and all(len(n)==2 and all(isinstance(x,str)and x for x in n)for n in w['history'])
for k,d in [('roots',[ROOT]),('words',W)]: (OUT/f'{k}_batch200_spec_{TAG}.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
print(ID,len(W),'new,',len(SHARED),'shared')
