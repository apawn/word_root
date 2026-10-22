# coding: utf-8
from pathlib import Path
import json
from lesson_authoring import entry as E
BASE=Path(__file__).resolve().parents[1];OUT=BASE/'.cache/batch200/drafts/rewrite_spec'
ID='C0092';TAG='302_ather';SHARED=['atherosclerosis'];EXCLUDE_REASON='按当前基础阅读范围暂略促病机制的专业派生形容词。'
W=[E('atheroma','英 /ˌæθəˈrəʊmə/；美 /ˌæθəˈroʊmə/','动脉粥样斑块','动脉壁上逐渐形成的斑块，里面可含脂质等物质。','希腊 athēra“粥、糊状物”形成 athērōma，经拉丁及新拉丁医学用法传入。现代可认 ather- + -oma，但这里的 -oma 不能直接等同于癌。',[['希腊 athēra〔粥〕→ athērōma','以糊状内容物的外观命名肿块'],['拉丁 atheroma → 新拉丁医学用法 → 英语 atheroma','后来用于动脉壁中的粥样斑块']],'古人用“粥”形容某些病变内容物的外观，今天心血管材料里的 atheroma 主要指动脉粥样斑块。它不是一团吃进去的粥卡住血管，也不只是纯脂肪：斑块可以包含脂质、细胞、纤维组织和钙等。','an atheroma；coronary atheroma；atheroma in the arterial wall。','atheroma 偏重斑块或沉积病变；atherosclerosis 是相关的动脉粥样硬化疾病过程。看到 -oma 先查具体含义，不自动翻成肿瘤或癌。',('The diagram shows an atheroma narrowing the artery.','图中显示一块粥样斑块使动脉变窄。'),('The researchers examined the composition of the atheroma.','研究人员检查了这块粥样斑块的组成。'),sources=['https://www.merriam-webster.com/dictionary/atheroma','https://en.wiktionary.org/wiki/atheroma#English','https://medlineplus.gov/ency/article/000171.htm','https://www.nhlbi.nih.gov/health/coronary-heart-disease/causes'])]
ROOT=dict(meaning='粥；糊状物',core='ather- 借粥样外观命名，现代常见于动脉斑块与粥样硬化。',image='名称中的“粥”是对病变物质外观的旧比喻，不是说食物直接堵进血管。',intro='希腊 athēra 指粥或糊状物。atheroma 是斑块名称，atherosclerosis 再把这类病变与硬化联系起来。记住外观比喻即可，不用把名称当成完整的生理机制。',forms='ather-／athero-；-sclerosis 表示硬化；atheroma 的 -oma 保留肿块类旧命名，但现代含义要单独学。',branches=[['斑块','atheroma'],['动脉粥样硬化','atherosclerosis']],contrasts='arteriosclerosis 泛指动脉硬化，atherosclerosis 是其中与粥样斑块有关的一类，不是所有硬化都叫粥样硬化。',practice='分别用一个短语指出 atheroma 是什么，以及 atherosclerosis 描写怎样的病变过程。',sources=['https://www.merriam-webster.com/dictionary/atheroma','https://medlineplus.gov/ency/article/000171.htm'])
m=json.loads((BASE/'.cache/batch200/rewrite_spec.json').read_text());r=next(x for x in m['roots']if x['id']==ID);c=next(x for x in json.loads((BASE/'.cache/catalog.json').read_text())if x['id']==ID);keep={w['word']for w in W}|set(SHARED);excluded={w:EXCLUDE_REASON for w in(set(r['family'])|set(c['family'])|set(c.get('unmatched',[])))-keep}
ROOT['id']=ID;ROOT['words']=list(dict.fromkeys([w for w in r['family']if w in keep]+[w for w in SHARED if w not in r['family']]));ROOT['exclude']=excluded
assert all(w['word']in m['owned_words']for w in W)
assert not(set(c['family'])|set(c.get('unmatched',[])))-set(ROOT['words'])-set(excluded)
assert {w['word']for w in W}<=set(ROOT['words'])
for w in W:assert len(w['examples'])>=2 and all(len(n)==2 and all(isinstance(x,str)and x for x in n)for n in w['history'])
for k,d in [('roots',[ROOT]),('words',W)]: (OUT/f'{k}_batch200_spec_{TAG}.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
print(ID,len(W),'new,',len(SHARED),'shared')
