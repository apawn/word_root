# coding: utf-8
from pathlib import Path
import json
from lesson_authoring import entry as E
BASE=Path(__file__).resolve().parents[1];OUT=BASE/'.cache/batch200/drafts/rewrite_spec'
ID='C1153';TAG='272_psor';SHARED=[];EXCLUDE_REASON='按当前范围暂略旧病名、罕见形容词与植物病害名。'
W=[E('psoriasis','/səˈraɪəsɪs/','银屑病','一种与免疫活动有关的慢性炎症性疾病，常在皮肤上形成带鳞屑的斑块。','经医学拉丁 psoriasis，接希腊 psōríasis“发痒的状态”，来自 psōriân“发痒”、psṓra“痒”。词首 p 不发音，-iasis 是疾病状态形式。',[['希腊 psṓra → psōriân → psōríasis','痒 → 发痒 → 发痒的状态'],['拉丁及医学拉丁 psoriasis','旧病名进入医学命名，范围随时代变化'],['英语 psoriasis','现代特指银屑病']],'名称抓住了发痒这一旧观察，但现代含义并不等于“凡是痒的皮肤病”。常见表现是炎症性斑块和鳞屑；它不是通过日常接触传染的病。不要因为中文俗称带“癣”，就把它当作真菌感染。','have psoriasis；live with psoriasis；a psoriasis flare；通常不可数。','eczema 是湿疹，psoriasis 是银屑病；两者都可能痒或脱屑，不能仅凭共同表现把词当同义词。',('The article explains why psoriasis is not contagious.','这篇文章解释了银屑病为什么不会传染。'),('She wrote about living with psoriasis at school and at work.','她写了自己患有银屑病期间的校园和工作生活。'),sources=['https://www.etymonline.com/word/psoriasis','https://www.oxfordlearnersdictionaries.com/definition/english/psoriasis','https://www.aad.org/public/diseases/psoriasis/what/causes'])]
ROOT=dict(meaning='痒；发痒的状态',core='由痒这一感受形成旧病名，再进入现代医学名称。',image='词根记住痒，整个疾病名称则按现代概念理解。',intro='这组最值得先学 psoriasis。词源讲的是名称怎么来，不能用一个“痒”字代替现代疾病的含义。',forms='希腊 psōr- 表痒，psōríasis 经拉丁进入英语；英语词首 ps- 的 p 不发音。',branches=[['现代常见病名','psoriasis：银屑病']],contrasts='不是所有痒或有鳞屑的皮肤问题都叫 psoriasis；它也不是因日常接触传染的真菌病。',practice='说清 psoriasis 的读音为什么没有 /p/，以及词源的痒为什么不足以定义它。',sources=['https://www.etymonline.com/word/psoriasis','https://www.aad.org/public/diseases/psoriasis/what/causes'])
m=json.loads((BASE/'.cache/batch200/rewrite_spec.json').read_text());r=next(x for x in m['roots']if x['id']==ID);c=next(x for x in json.loads((BASE/'.cache/catalog.json').read_text())if x['id']==ID);keep={w['word']for w in W}|set(SHARED);excluded={w:EXCLUDE_REASON for w in(set(r['family'])|set(c['family'])|set(c.get('unmatched',[])))-keep}
ROOT['id']=ID;ROOT['words']=list(dict.fromkeys([w for w in r['family']if w in keep]+[w for w in SHARED if w not in r['family']]));ROOT['exclude']=excluded
assert all(w['word']in m['owned_words']for w in W)
assert not(set(c['family'])|set(c.get('unmatched',[])))-set(ROOT['words'])-set(excluded)
assert {w['word']for w in W}<=set(ROOT['words'])
for w in W:assert len(w['examples'])>=2 and all(len(n)==2 and all(isinstance(x,str)and x for x in n)for n in w['history'])
for k,d in [('roots',[ROOT]),('words',W)]: (OUT/f'{k}_batch200_spec_{TAG}.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
print(ID,len(W),'new,',len(SHARED),'shared')
