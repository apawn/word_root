# coding: utf-8
from pathlib import Path
import json
from lesson_authoring import entry as E
BASE=Path(__file__).resolve().parents[1];OUT=BASE/'.cache/batch200/drafts/rewrite_spec'
ID='C1671';TAG='301_ze';SHARED=[];EXCLUDE_REASON='按当前通用阅读范围暂略仅在临床描述中较常见的派生形容词。'
W=[E('eczema','英 /ˈeksɪmə/；美常见 /ɪɡˈziːmə/ 或 /ˈeksəmə/','湿疹','皮肤一片片发炎、发痒，可能干燥、开裂或起疹。','希腊 ek-“向外”＋ zein“沸腾”组成 ekzein“涌出、冒出”，再形成名词 ekzema，经医学拉丁进入英语。是古人对皮疹冒出的形象说法，不是身体真的在沸腾。',[['希腊 ek-〔向外〕＋ zein〔沸腾〕→ ekzein','涌出、冒出'],['希腊 ekzema → 医学拉丁 eczema → 英语 eczema','皮疹名称 → 现代湿疹名称']],'eczema 可以统称一组使皮肤发炎、干燥和瘙痒的情况，日常尤其常指特应性湿疹。中文有个“湿”字，并不代表皮肤一定湿润；它也可能又干又裂。这个词通常不可数，说 have eczema。','have eczema；a flare of eczema；eczema on the hands。','rash 只说皮疹这种表现，eczema 是更具体的一组皮肤问题。eczema 的常见读法在英美之间差异较大，不要按字母逐个拼读。',('Her eczema sometimes makes it difficult to sleep.','她的湿疹有时让她难以入睡。'),('The article explains why eczema can affect both children and adults.','文章解释了为什么儿童和成人都可能出现湿疹。'),sources=['https://www.etymonline.com/word/eczema','https://en.wiktionary.org/wiki/eczema#English','https://www.nhs.uk/conditions/contact-dermatitis/','https://health.nih.gov/health-topics-a-z/eczema'])]
ROOT=dict(meaning='沸腾；冒出',core='ze- 的旧画面是翻沸冒泡，在 eczema 中借来描写皮疹冒出。',image='像东西从表面冒出来；这里只是古人的命名比喻。',intro='希腊 zein“沸腾”与 ek-“向外”组成 eczema 的历史前身。这个来源有助记住字形，但现代湿疹的范围和原因不能靠“沸腾”两字推断。',forms='ek- + zein → ekzein → ekzema；英语保留的形式是 eczema。',branches=[['日常健康词','eczema']],contrasts='不要把旧命名的热、冒出画面当病因解释；也不要把任何 rash 都等同于 eczema。',practice='用 have eczema 造句，再说清 eczema 和泛指皮疹的 rash 有何不同。',sources=['https://www.etymonline.com/word/eczema','https://health.nih.gov/health-topics-a-z/eczema'])
m=json.loads((BASE/'.cache/batch200/rewrite_spec.json').read_text());r=next(x for x in m['roots']if x['id']==ID);c=next(x for x in json.loads((BASE/'.cache/catalog.json').read_text())if x['id']==ID);keep={w['word']for w in W}|set(SHARED);excluded={w:EXCLUDE_REASON for w in(set(r['family'])|set(c['family'])|set(c.get('unmatched',[])))-keep}
ROOT['id']=ID;ROOT['words']=list(dict.fromkeys([w for w in r['family']if w in keep]+[w for w in SHARED if w not in r['family']]));ROOT['exclude']=excluded
assert all(w['word']in m['owned_words']for w in W)
assert not(set(c['family'])|set(c.get('unmatched',[])))-set(ROOT['words'])-set(excluded)
assert {w['word']for w in W}<=set(ROOT['words'])
for w in W:assert len(w['examples'])>=2 and all(len(n)==2 and all(isinstance(x,str)and x for x in n)for n in w['history'])
for k,d in [('roots',[ROOT]),('words',W)]: (OUT/f'{k}_batch200_spec_{TAG}.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
print(ID,len(W),'new,',len(SHARED),'shared')
