from pathlib import Path
import json
from lesson_authoring import entry as E
BASE=Path(__file__).resolve().parents[1];OUT=BASE/'.cache/batch200/drafts/rewrite_spec'
ID='C0374';TAG='256_encephal';SHARED=['encephalitis','encephalopathy'];EXCLUDE_REASON='按当前范围暂略：冷门脑部医学细分类术语。'
W=[]
ROOT=dict(meaning='脑',core='从“头里面的”这个位置描述，发展成“脑”的名称。',image='cephal- 先给出头；希腊 en- 加上“在里面”，enkephalos 就把视线带到头颅中的脑。',intro='脑炎和脑病这两个词最适合一起学：开头告诉你部位都是脑，结尾则告诉你描述的是炎症，还是更宽泛的脑部疾病或功能异常。长词并非每个音节都要死记。',forms='希腊 en“在里面”与 kephalē“头”组成 enképhalos，表示脑；经医学拉丁 encephalon 提供 encephal-／encephalo-。它与日常英语 brain 不同源。',branches=[['强调炎症','encephalitis：encephal- 脑 + -itis 炎症'],['较宽泛的脑病名称','encephalopathy：encephalo- 脑 + -pathy 病变、功能异常']],contrasts='encephalitis 特别说脑的炎症；encephalopathy 范围更宽，不自动等于感染或炎症。词尾能帮你把两者区分开。',practice='先遮住词尾，只用 encephal- 猜部位；再分别加上 -itis 与 -pathy，解释两个词的范围怎样变化。',sources=['https://www.merriam-webster.com/dictionary/encephalon','https://www.etymonline.com/word/encephalitis'])
m=json.loads((BASE/'.cache/batch200/rewrite_spec.json').read_text());r=next(x for x in m['roots']if x['id']==ID);c=next(x for x in json.loads((BASE/'.cache/catalog.json').read_text())if x['id']==ID);keep={w['word']for w in W}|set(SHARED);excluded={w:EXCLUDE_REASON for w in(set(r['family'])|set(c['family'])|set(c.get('unmatched',[])))-keep}
ROOT['id']=ID;ROOT['words']=list(dict.fromkeys([w for w in r['family']if w in keep]+[w for w in SHARED if w not in r['family']]));ROOT['exclude']=excluded
assert all(w['word']in m['owned_words']for w in W)
assert not(set(c['family'])|set(c.get('unmatched',[])))-set(ROOT['words'])-set(excluded)
assert {w['word']for w in W}<=set(ROOT['words'])
for w in W:assert len(w['examples'])>=2 and all(len(n)==2 and all(isinstance(x,str)and x for x in n)for n in w['history'])
for k,d in [('roots',[ROOT]),('words',W)]: (OUT/f'{k}_batch200_spec_{TAG}.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
print(ID,len(W),'new,',len(SHARED),'shared')
