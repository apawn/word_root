# coding: utf-8
from pathlib import Path
import json
from lesson_authoring import entry as E
BASE=Path(__file__).resolve().parents[1];OUT=BASE/'.cache/batch200/drafts/rewrite_spec'
ID='C0026';TAG='285_agr';SHARED=['agronomy','agronomist','agronomic'];EXCLUDE_REASON='按当前常用范围暂略低频农业细分派生。'
W=[]
ROOT=dict(meaning='田地；农田',core='把研究对象放进田里：作物怎样长、土怎样管、水和养分怎样配合。',image='站在一块田里，同时看作物、土壤、水分和耕作安排。',intro='这里的 agr- 来自希腊 agrós“田地”。加上管理、规则的 -nom-，形成田地管理这一组词，后经法语学科名称进入英语农艺学。',forms='agr- 常用带连接元音的 agro-；agronomy 经法语 agronomie。agronomist 说专业人员，agronomic 说明农艺方面的性质。',branches=[['研究领域','agronomy：农艺学'],['人员与角度','agronomist：农艺师；agronomic：农艺方面的']],contrasts='agronomy 侧重田间作物与土壤管理；agriculture 是范围更大的农业。后者的 agri- 接拉丁 ager，与希腊 agrós 是相关的旁支，不能画成希腊 agronomy 直接变成 agriculture。',practice='看到 agronomic benefits，先问它怎样改善种植表现，不要直接等同于经济利润。',sources=['https://www.etymonline.com/word/agronomy','https://www.etymonline.com/word/agriculture','https://www.agronomy.org/about-society'])
m=json.loads((BASE/'.cache/batch200/rewrite_spec.json').read_text());r=next(x for x in m['roots']if x['id']==ID);c=next(x for x in json.loads((BASE/'.cache/catalog.json').read_text())if x['id']==ID);keep={w['word']for w in W}|set(SHARED);excluded={w:EXCLUDE_REASON for w in(set(r['family'])|set(c['family'])|set(c.get('unmatched',[])))-keep}
ROOT['id']=ID;ROOT['words']=list(dict.fromkeys([w for w in r['family']if w in keep]+[w for w in SHARED if w not in r['family']]));ROOT['exclude']=excluded
assert all(w['word']in m['owned_words']for w in W)
assert not(set(c['family'])|set(c.get('unmatched',[])))-set(ROOT['words'])-set(excluded)
assert {w['word']for w in W}<=set(ROOT['words'])
for w in W:assert len(w['examples'])>=2 and all(len(n)==2 and all(isinstance(x,str)and x for x in n)for n in w['history'])
for k,d in [('roots',[ROOT]),('words',W)]: (OUT/f'{k}_batch200_spec_{TAG}.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
print(ID,len(W),'new,',len(SHARED),'shared')
