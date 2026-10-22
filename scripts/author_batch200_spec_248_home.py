# -*- coding: utf-8 -*-
from pathlib import Path
import json
from lesson_authoring import entry as E
BASE=Path(__file__).resolve().parents[1];OUT=BASE/'.cache/batch200/drafts/rewrite_spec'
ID='C0565';TAG='248_home';SHARED=['homeopathy','homeopathic','homeostasis','homeostatic'];EXCLUDE_REASON='按用户当前范围暂略：专门拓扑概念、较少用的动物生理术语或变体。'
W=[E('homoeopathy','英 /ˌhəʊmiˈɒpəθi/，也读 /ˌhɒmiˈɒpəθi/','顺势疗法〔常见英式拼法〕','和 homeopathy 是同一个词，多一个 o 不代表另一种疗法。','源自德语 Homöopathie，用希腊 hómoios“相似”与 páthos“遭受、病苦”等材料命名。homoeo- 保留较完整的拉丁化拼写，homeo- 是常见简化形式；不能拆成英语 home“家”。',[['希腊 hómoios〔相似〕与 páthos〔遭受、病苦〕','两种材料并列，体现相似症状的命名理念'],['德语 Homöopathie','近代提出的疗法名称'],['英语 homoeopathy／homeopathy','同一术语的不同拼写']],'名称表达的是“相似者治疗相似者”的理论，相关制剂常经过高度稀释。认识这个词要把理论名称与疗效证据分开：目前没有可靠证据支持它作为具体疾病的有效治疗方式，也不能把它笼统理解为草药或家庭疗法。','the history of homoeopathy；research on homoeopathy。不可数；英式材料中常见这一拼法。','homoeopathy 与 homeopathy 含义相同；homeostasis 则是生理学中的稳态概念，与这种疗法不是一回事。',('The British journal uses the spelling homoeopathy throughout the article.','这份英国期刊在全文中都采用 homoeopathy 的拼法。'),('The exhibition examines the history of homoeopathy in Europe.','展览探讨了顺势疗法在欧洲的历史。'),sources=['https://www.oxfordlearnersdictionaries.com/definition/english/homoeopathy','https://en.wiktionary.org/wiki/homeopathy','https://www.nccih.nih.gov/health/homeopathy'])]
ROOT=dict(meaning='相似；相近',core='homeo- 表示相似，最值得记住的是“把状态维持在相近范围”这个稳态画面。',image='homeostasis 通过不断调节保持相对稳定；homeopathy 的名称则表达其自身的相似症状理论。',intro='相同词根被不同领域使用，并不代表这些领域有同一科学地位。稳态是生理调节概念；顺势疗法的名称只表达该理论的命名理念。',forms='希腊 hómoios“相似”有 homeo-、homoeo- 等拉丁化形式；不要把这里的 home- 当成英语“家”。',branches=[['生理调节','homeostasis、homeostatic'],['另一套理论的名称','homeopathy、homoeopathy、homeopathic']],contrasts='homeostasis 是通过变化来保持相对稳定，不是一动不动；homeopathy 则不能从名字推导出疗效。',practice='用体温调节解释 homeostasis，再说明为什么 homeopathy 不是“家庭疗法”。',sources=['https://en.wiktionary.org/wiki/homeostasis','https://www.nccih.nih.gov/health/homeopathy'])
m=json.loads((BASE/'.cache/batch200/rewrite_spec.json').read_text());r=next(x for x in m['roots']if x['id']==ID);c=next(x for x in json.loads((BASE/'.cache/catalog.json').read_text())if x['id']==ID);keep={w['word']for w in W}|set(SHARED);excluded={w:EXCLUDE_REASON for w in(set(r['family'])|set(c['family'])|set(c.get('unmatched',[])))-keep}
ROOT['id']=ID;ROOT['words']=list(dict.fromkeys([w for w in r['family']if w in keep]+[w for w in SHARED if w not in r['family']]));ROOT['exclude']=excluded
assert all(w['word']in m['owned_words']for w in W)
assert not(set(c['family'])|set(c.get('unmatched',[])))-set(ROOT['words'])-set(excluded)
assert {w['word']for w in W}<=set(ROOT['words'])
for w in W:assert len(w['examples'])>=2 and all(len(n)==2 and all(isinstance(x,str)and x for x in n)for n in w['history'])
for k,d in [('roots',[ROOT]),('words',W)]: (OUT/f'{k}_batch200_spec_{TAG}.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
print(ID,len(W),'new,',len(SHARED),'shared')
