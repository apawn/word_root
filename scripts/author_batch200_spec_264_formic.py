from pathlib import Path
import json
from lesson_authoring import entry as E
BASE=Path(__file__).resolve().parents[1];OUT=BASE/'.cache/batch200/drafts/rewrite_spec'
ID='C0444';TAG='264_formic';SHARED=[];EXCLUDE_REASON='按用户要求暂略多词复合短语；相关名称在词内说明，不另建词条。'
W=[E('formaldehyde','英 /fɔːˈmældɪhaɪd/；美 /fɔːrˈmældɪhaɪd/','甲醛','材料和室内空气报道中常见的一种化学物质名。','formic aldehyde 的合并缩短形式；formic 来自拉丁 formīca“蚂蚁”，因为甲酸的旧名联系从蚂蚁取得的酸。甲醛沿化学命名关系借用了 form-，并不是 formal“正式的”加另一段字母。',[['拉丁 formīca','蚂蚁'],['近代 formic acid','甲酸的名称联系蚂蚁来源'],['formic 与 aldehyde 结合缩短 → formaldehyde','形成甲醛这一化学名称']],'这个词里“蚂蚁”的历史很远：它通过甲酸相关命名传到甲醛，不能推断甲醛就是从蚂蚁提取的。甲醛在常温下是气体；资料也会用 formaldehyde 指其水溶液，讨论保存标本等用途。','formaldehyde emissions；formaldehyde levels；a formaldehyde solution。','formaldehyde 是甲醛，formic acid 是甲酸，甲醇则是 methanol。它们有化学联系，却是不同物质。',('The laboratory measured formaldehyde levels in the air sample.','实验室测量了空气样本中的甲醛含量。'),('The report discusses formaldehyde emissions from some building materials.','报告讨论了某些建筑材料的甲醛释放。'),sources=['https://www.etymonline.com/word/formaldehyde','https://www.oxfordlearnersdictionaries.com/definition/english/formaldehyde'])]
ROOT=dict(meaning='蚂蚁；经甲酸名称进入相关化学词',core='蚂蚁先给一种酸提供名字，这个名字再被用于相关化学命名。',image='蚂蚁 → 甲酸的旧命名 → formic aldehyde 缩成 formaldehyde。箭头是名称传承，不是说物质逐个变成另一物质。',intro='这一根保留一个非常实用的阅读词 formaldehyde。关键是看清名字的间接来源：前半部分既不是“形状”的 form，也不是“正式的” formal。',forms='拉丁 formīca“蚂蚁”提供 formic；formaldehyde 把 formic 与 aldehyde 缩合。多词名称 formic acid 在讲解中说明，不另立词条。',branches=[['日常化学与材料报道','formaldehyde']],contrasts='甲酸、甲醛、甲醇的中文都有“甲”，英文名称也有联系，但不能混成一种物质。',practice='用一句话讲清 formaldehyde 怎样间接联系蚂蚁，并指出为什么不能拆成 formal。',sources=['https://www.etymonline.com/word/formaldehyde','https://www.oxfordlearnersdictionaries.com/definition/english/formaldehyde'])
m=json.loads((BASE/'.cache/batch200/rewrite_spec.json').read_text());r=next(x for x in m['roots']if x['id']==ID);c=next(x for x in json.loads((BASE/'.cache/catalog.json').read_text())if x['id']==ID);keep={w['word']for w in W}|set(SHARED);excluded={w:EXCLUDE_REASON for w in(set(r['family'])|set(c['family'])|set(c.get('unmatched',[])))-keep}
ROOT['id']=ID;ROOT['words']=list(dict.fromkeys([w for w in r['family']if w in keep]+[w for w in SHARED if w not in r['family']]));ROOT['exclude']=excluded
assert all(w['word']in m['owned_words']for w in W)
assert not(set(c['family'])|set(c.get('unmatched',[])))-set(ROOT['words'])-set(excluded)
assert {w['word']for w in W}<=set(ROOT['words'])
for w in W:assert len(w['examples'])>=2 and all(len(n)==2 and all(isinstance(x,str)and x for x in n)for n in w['history'])
for k,d in [('roots',[ROOT]),('words',W)]: (OUT/f'{k}_batch200_spec_{TAG}.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
print(ID,len(W),'new,',len(SHARED),'shared')
