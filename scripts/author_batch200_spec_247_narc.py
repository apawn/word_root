# -*- coding: utf-8 -*-
from pathlib import Path
import json
from lesson_authoring import entry as E
BASE=Path(__file__).resolve().parents[1];OUT=BASE/'.cache/batch200/drafts/rewrite_spec'
ID='C0792';TAG='247_narc';SHARED=['narcolepsy'];EXCLUDE_REASON='按用户当前范围暂略：非常专门的麻木、麻醉相关术语。'
N=[['希腊 nárkē → narkoûn','麻木、迟钝 → 使失去感觉']]
W=[E('narcotic','英 /nɑːˈkɒtɪk/；美 /nɑːrˈkɑːtɪk/','麻醉性或使人迟钝的；麻醉性药物；〔常用复数〕毒品','从“让感觉钝下来”出发，到了新闻里却常泛指毒品。','名词经法语 narcotique 或中世纪拉丁 narcoticum，接希腊 narkōtikon；形容词另有法语、德语或拉丁 narcoticus 的借入路线。共同远源是 nárkē“麻木”，不是名词、形容词一定在英语内部互相派生。',N+[['希腊 narkōtikós／narkōtikon','使麻木的；相应物质名称'],['名词：法语 narcotique／拉丁 narcoticum；形容词：法语、德语或拉丁相关形式','并行借入路线'],['英语 narcotic','相关药物或性质；后来也泛用于非法药物语境']],'a narcotic 可以指使感觉迟钝、带来镇痛或嗜睡作用的药物；narcotics 在警务新闻中常泛指毒品。后一种用法不保证每种被提到的物质都有同样药理作用。形容音乐或气氛时，也可比喻使人昏沉。','narcotic drugs；a narcotic effect；a narcotics investigation。','narcotic 的医药含义与新闻、法律语境中的范围不完全相同。不能把这个词简单等同于所有麻醉技术，也不能仅凭它判断某物是否合法。',('The hospital keeps detailed records of narcotic medicines.','医院详细记录麻醉性药物的使用情况。'),('The novel describes the slow music as having a narcotic effect.','小说把缓慢音乐的效果描写得令人昏昏沉沉。'),sources=['https://www.etymonline.com/word/narcotic','https://en.wiktionary.org/wiki/narcotic']),
E('narcosis','英 /nɑːˈkəʊsɪs/；美 /nɑːrˈkoʊsɪs/','麻醉或昏沉状态','重点是感觉、意识变得迟钝的状态，而不是某一种药物。','借新拉丁 narcōsis，接希腊 nárkōsis“使麻木的过程”。现代可认出 narco- 与 -osis，但整个名称有古典借入历史，不是把英语 narcotic 换一个后缀。',N+[['希腊 nárkōsis → 新拉丁 narcōsis','使麻木及相关状态名称'],['英语 narcosis','化学或物理因素引起的昏沉、意识受抑状态']],'这个词强调一种状态，可用于药物影响，也可出现在潜水讨论中的 nitrogen narcosis“氮醉”。它不像 anesthesia 那样总是指医疗上安排的麻醉或感觉缺失，因此阅读时要看具体成因。','a state of narcosis；nitrogen narcosis；the effects of narcosis。','narcotic 可指物质或性质；narcosis 指状态。narcolepsy 则是另一种睡眠障碍名称，不是“使用麻醉药”的同义词。',('The diving course includes a lesson on nitrogen narcosis.','潜水课程包括一节关于氮醉的课。'),('Narcosis affected the diver’s judgement.','氮醉影响了这名潜水员的判断力。'),sources=['https://www.merriam-webster.com/dictionary/narcosis','https://www.etymonline.com/word/narcosis'])]
ROOT=dict(meaning='麻木；感觉迟钝、昏沉',core='narc- 的共同画面是感知变钝，不是所有相关词都表示“毒品”。',image='物质或作用性质是 narcotic；状态是 narcosis；睡眠障碍的名称有 narcolepsy。',intro='新闻、药理和睡眠科普会用到这一组，但各领域的具体含义不同。先分清词在指物质、状态还是疾病名称，比只记一个“麻醉”更有用。',forms='希腊 nárkē 及动词 narkoûn 提供 narc-/narco-；-osis 与 -lepsy 在不同名称中承担不同作用。',branches=[['物质与性质','narcotic'],['状态','narcosis'],['睡眠障碍名称','narcolepsy']],contrasts='narcotic 的泛指毒品用法不能反推所有同根词都与非法药物有关；narcolepsy 就不是这个意思。',practice='分别用“物质”“状态”“睡眠障碍名称”区分本组的三个核心词。',sources=['https://www.etymonline.com/word/narcotic','https://www.merriam-webster.com/dictionary/narcosis'])
m=json.loads((BASE/'.cache/batch200/rewrite_spec.json').read_text());r=next(x for x in m['roots']if x['id']==ID);c=next(x for x in json.loads((BASE/'.cache/catalog.json').read_text())if x['id']==ID);keep={w['word']for w in W}|set(SHARED);excluded={w:EXCLUDE_REASON for w in(set(r['family'])|set(c['family'])|set(c.get('unmatched',[])))-keep}
ROOT['id']=ID;ROOT['words']=list(dict.fromkeys([w for w in r['family']if w in keep]+[w for w in SHARED if w not in r['family']]));ROOT['exclude']=excluded
assert all(w['word']in m['owned_words']for w in W)
assert not(set(c['family'])|set(c.get('unmatched',[])))-set(ROOT['words'])-set(excluded)
assert {w['word']for w in W}<=set(ROOT['words'])
for w in W:assert len(w['examples'])>=2 and all(len(n)==2 and all(isinstance(x,str)and x for x in n)for n in w['history'])
for k,d in [('roots',[ROOT]),('words',W)]: (OUT/f'{k}_batch200_spec_{TAG}.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
print(ID,len(W),'new,',len(SHARED),'shared')
