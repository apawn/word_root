# -*- coding: utf-8 -*-
from pathlib import Path
import json
from lesson_authoring import entry as E
BASE=Path(__file__).resolve().parents[1];OUT=BASE/'.cache/batch200/drafts/rewrite_spec'
ID='C1570';TAG='246_typh';SHARED=['typhoid'];EXCLUDE_REASON='按用户当前范围暂略：少用的相关形容词，常用病名已保留。'
W=[E('typhus','/ˈtaɪfəs/','斑疹伤寒；相关的一组传染病','旧词源像“脑中蒙着烟雾”，现代则是明确的疾病名称。','经近代医学拉丁 typhus 接希腊 tŷphos，原有烟雾、发热时昏沉的含义。名称联系的是古人观察到的状态，不是说烟雾造成这种病。',[['希腊 tŷphos','烟雾；发热时昏沉的状态'],['近代医学拉丁 typhus','用于发热疾病的名称'],['英语 typhus','现代指斑疹伤寒等相关病类']],'现代 typhus fevers 包含几种由细菌引起、经虱、跳蚤或恙螨等传播的疾病。普通历史文章常见 epidemic typhus。不要因为中文也带“伤寒”，就把它与 typhoid 当作同一疾病。','an outbreak of typhus；epidemic typhus；typhus fever。病名本身通常不可数。','typhoid 最初有“像 typhus 的”命名意思，但现代指伤寒，与 typhus 的病原、传播方式不同。名字相似反映旧观察，不等于现代分类相同。',('The historian studied accounts of typhus in overcrowded camps.','历史学家研究了拥挤营地中斑疹伤寒的记录。'),('The textbook distinguishes typhus from typhoid fever.','教材区分了斑疹伤寒与伤寒。'),sources=['https://www.etymonline.com/word/typhus','https://www.cdc.gov/typhus/about/','https://www.cdc.gov/typhoid-fever/about/index.html'])]
ROOT=dict(meaning='烟雾；昏沉',core='typh- 把烟雾蒙住视线的画面，用来描述发热时的昏沉。',image='烟雾般昏沉的旧描述 → typhus 病名；“像它的”旧命名 → typhoid。',intro='这组主要帮助阅读疾病史与公共卫生文章。重点不是背两个相近拼写，而是知道现代医学已经把它们分为不同疾病。',forms='希腊 tŷphos 经医学拉丁成为 typhus；typhoid 的 -oid 本来表示“像……的”。',branches=[['病名','typhus'],['历史上相似、现代不同的病名','typhoid']],contrasts='词源中的烟雾是症状比喻，不是病因；typhus 与 typhoid 不能互换。',practice='用一句话解释 typhoid 为什么名字像 typhus，却不等于同一种病。',sources=['https://www.etymonline.com/word/typhus'])
m=json.loads((BASE/'.cache/batch200/rewrite_spec.json').read_text());r=next(x for x in m['roots']if x['id']==ID);c=next(x for x in json.loads((BASE/'.cache/catalog.json').read_text())if x['id']==ID);keep={w['word']for w in W}|set(SHARED);excluded={w:EXCLUDE_REASON for w in(set(r['family'])|set(c['family'])|set(c.get('unmatched',[])))-keep}
ROOT['id']=ID;ROOT['words']=list(dict.fromkeys([w for w in r['family']if w in keep]+[w for w in SHARED if w not in r['family']]));ROOT['exclude']=excluded
assert all(w['word']in m['owned_words']for w in W)
assert not(set(c['family'])|set(c.get('unmatched',[])))-set(ROOT['words'])-set(excluded)
assert {w['word']for w in W}<=set(ROOT['words'])
for w in W:assert len(w['examples'])>=2 and all(len(n)==2 and all(isinstance(x,str)and x for x in n)for n in w['history'])
for k,d in [('roots',[ROOT]),('words',W)]: (OUT/f'{k}_batch200_spec_{TAG}.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
print(ID,len(W),'new,',len(SHARED),'shared')
