# coding: utf-8
from pathlib import Path
import json
from lesson_authoring import entry as E
BASE=Path(__file__).resolve().parents[1];OUT=BASE/'.cache/batch200/drafts/rewrite_spec'
ID='C0004';TAG='274_ace';SHARED=['panacea'];EXCLUDE_REASON='按当前范围暂略罕见治疗学旧称和局部活性物质术语。'
W=[]
ROOT=dict(meaning='治疗；补救办法',core='表示能够医治、补救的东西；加上全部，便产生万能药的想象。',image='不是只解决一个问题的办法，而是被寄望于什么都能解决的那一剂药。',intro='先学这组最有用的 panacea。它的字面画面是治一切的药，现代常借来讨论政策、技术或管理方案能否解决所有问题。',forms='希腊 ákos 是治疗、补救；pan- 全部 + ákos 形成 panakḗs“全能治疗的”，再有 panákeia，经过拉丁 panacea 进入英语。',branches=[['全能补救的想象','panacea：万能药；包治百病的方案']],contrasts='panacea 常在否定中出现：不是解决一切问题的灵丹妙药。本组 ac- 表治疗，不是所有 ac- 开头单词都属这一来源。',practice='用一句话说明为什么一项新技术可以有帮助，却未必是 panacea。',sources=['https://www.etymonline.com/word/panacea'])
m=json.loads((BASE/'.cache/batch200/rewrite_spec.json').read_text());r=next(x for x in m['roots']if x['id']==ID);c=next(x for x in json.loads((BASE/'.cache/catalog.json').read_text())if x['id']==ID);keep={w['word']for w in W}|set(SHARED);excluded={w:EXCLUDE_REASON for w in(set(r['family'])|set(c['family'])|set(c.get('unmatched',[])))-keep}
ROOT['id']=ID;ROOT['words']=list(dict.fromkeys([w for w in r['family']if w in keep]+[w for w in SHARED if w not in r['family']]));ROOT['exclude']=excluded
assert all(w['word']in m['owned_words']for w in W)
assert not(set(c['family'])|set(c.get('unmatched',[])))-set(ROOT['words'])-set(excluded)
assert {w['word']for w in W}<=set(ROOT['words'])
for w in W:assert len(w['examples'])>=2 and all(len(n)==2 and all(isinstance(x,str)and x for x in n)for n in w['history'])
for k,d in [('roots',[ROOT]),('words',W)]: (OUT/f'{k}_batch200_spec_{TAG}.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
print(ID,len(W),'new,',len(SHARED),'shared')
