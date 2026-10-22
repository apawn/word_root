from pathlib import Path
import json
from lesson_authoring import entry as E
BASE=Path(__file__).resolve().parents[1];OUT=BASE/'.cache/batch200/drafts/rewrite_spec'
ID='C0865';TAG='255_oed';SHARED=[];EXCLUDE_REASON='按当前范围暂略：临床细分类名称与低频形容词。'
H=[['希腊 oideîn → oídēma','肿起 → 肿胀'],['医学拉丁 oedema → 英语 oedema／edema','组织中液体积聚造成的水肿；两种拼写']]
W=[E('edema','/ɪˈdiːmə/','水肿〔美式常用拼写〕','组织间多积了液体，因而肿起来。','经医学拉丁 oedema，远源是希腊 oídēma“肿胀”，来自 oideîn“肿起”。现代美国英语通常省去开头的 o；不要拆成英语 ed 加 ema。',H,'想象组织像海绵，内部积进过多液体后变厚、变鼓，这就接近 edema 的基本画面。它描述一种身体变化，不是一个已经说明原因的病名；也不等于所有形式的肿胀。','edema in the legs；pulmonary edema；peripheral edema。常作不可数名词。','swelling 是更宽泛的“肿胀”；edema 特别强调液体积聚。inflammation 是炎症，两者也不是同一个词。',('The report notes edema around the injured ankle.','报告记录了受伤脚踝周围的水肿。'),('The diagram shows fluid accumulating in the tissues and causing edema.','图示展示了液体在组织中积聚并引起水肿。'),sources=['https://medlineplus.gov/edema.html','https://www.oxfordlearnersdictionaries.com/definition/english/oedema']),
E('oedema','/ɪˈdiːmə/','水肿〔英式常用拼写〕','开头的 oe 连在一起读，仍然是液体积聚形成的肿胀。','保留医学拉丁 oedema 的 oe 拼写，远接希腊 oídēma。oedema 与 edema 不是两种不同的水肿，只是常见地区拼写差别。',H,'英国材料常用 oedema。理解时先找前面的身体部位：例如 pulmonary 把范围限定到肺。词本身告诉你有液体积聚的变化，但没有单独说明形成原因。','pulmonary oedema；cerebral oedema；oedema of the legs。','oe 在这里不读作 /əʊ/，整词重音在第二音节。它和 edema 可以互相对应，正文通常统一一种拼写。',('The British textbook has a section on pulmonary oedema.','这本英国教材有一节介绍肺水肿。'),('The editor changed edema to oedema to match the journal’s spelling style.','编辑把 edema 改成 oedema，以符合期刊的拼写规范。'),sources=['https://www.oxfordlearnersdictionaries.com/definition/english/oedema','https://medlineplus.gov/edema.html'])]
ROOT=dict(meaning='肿起；肿胀',core='组织鼓起来；现代医学用 oedema／edema 特指液体积聚造成的水肿。',image='像海绵中积了更多水，组织因此变厚、变肿。这个比喻帮助理解状态，不代表每种肿胀都属于水肿。',intro='这组先掌握英美两种常见拼写即可。看懂部位修饰词，就能读懂基础科普中许多组合；没有必要把所有临床细分名称一起记下。',forms='希腊 oídēma 经拉丁化写成 oedema；美式常写 edema。开头 oe 或 e 在这里都读 /ɪ/。',branches=[['美式常用拼写','edema'],['英式常用拼写','oedema']],contrasts='水肿强调液体；炎症是一类反应，普通 swelling 则只说肿胀。不要把三个词直接画等号。',practice='用一句话说明 edema 与 oedema 的关系，再解释为什么 edema 不等于所有 swelling。',sources=['https://www.oxfordlearnersdictionaries.com/definition/english/oedema','https://medlineplus.gov/edema.html'])
m=json.loads((BASE/'.cache/batch200/rewrite_spec.json').read_text());r=next(x for x in m['roots']if x['id']==ID);c=next(x for x in json.loads((BASE/'.cache/catalog.json').read_text())if x['id']==ID);keep={w['word']for w in W}|set(SHARED);excluded={w:EXCLUDE_REASON for w in(set(r['family'])|set(c['family'])|set(c.get('unmatched',[])))-keep}
ROOT['id']=ID;ROOT['words']=list(dict.fromkeys([w for w in r['family']if w in keep]+[w for w in SHARED if w not in r['family']]));ROOT['exclude']=excluded
assert all(w['word']in m['owned_words']for w in W)
assert not(set(c['family'])|set(c.get('unmatched',[])))-set(ROOT['words'])-set(excluded)
assert {w['word']for w in W}<=set(ROOT['words'])
for w in W:assert len(w['examples'])>=2 and all(len(n)==2 and all(isinstance(x,str)and x for x in n)for n in w['history'])
for k,d in [('roots',[ROOT]),('words',W)]: (OUT/f'{k}_batch200_spec_{TAG}.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
print(ID,len(W),'new,',len(SHARED),'shared')
