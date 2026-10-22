# coding: utf-8
from pathlib import Path
import json
from lesson_authoring import entry as E
BASE=Path(__file__).resolve().parents[1];OUT=BASE/'.cache/batch200/drafts/rewrite_spec'
ID='C0031';TAG='293_alcyon';SHARED=[];EXCLUDE_REASON='按当前范围暂略冷门鸟名派生。'
W=[E('halcyon','/ˈhælsiən/','平静幸福的；安宁美好的；〔名词〕翠鸟','回想一段风平浪静、日子舒心的时光。','经拉丁 halcyon／alcyon 接希腊 alkyōn“翠鸟”。更早来源不确定；把它硬拆成“海＋怀孕”属于旧时附会，不能当作确定词源。',[['希腊 alkyōn → 拉丁 halcyon／alcyon','一种与冬日平静海面传说有关的鸟名'],['中古英语及现代英语 halcyon','鸟名；由传说中的平静日子引申为安宁幸福']],'古人传说，翠鸟在冬季海上筑巢时会有一段平静无风的日子，于是 halcyon days 留下“太平好日子”的意思。今天常带怀旧色彩：说起年轻时轻松快乐的日子，而不是在报告当天的天气。','the halcyon days of youth；those halcyon days；a halcyon period。','calm 只是平静；halcyon 通常更文学化，还带美好、幸福或繁荣的回忆。鸟在海上筑巢使风停下是传说，不是现代动物学解释。',('She often recalls the halcyon days of her first summer by the sea.','她常常回想起第一次在海边度过夏天的美好时光。'),('The photographs capture a halcyon period before the town became crowded.','这些照片留住了小镇变得拥挤之前那段安宁的日子。'),sources=['https://www.etymonline.com/word/halcyon','https://www.oxfordlearnersdictionaries.com/definition/english/halcyon'])]
ROOT=dict(meaning='翠鸟；由传说引申为安宁美好',core='一个鸟名，借古老传说变成了“风平浪静的好时光”。',image='回望一片平静的海面，联想到没有纷扰的一段日子。',intro='alcyon／halcyon 不是英语里仍能自由拼新词的常见前缀。这页最值得掌握的是 halcyon days：它从鸟的传说进入描写时光的语言。',forms='希腊 alkyōn 经拉丁 alcyon／halcyon 传入英语，现代常见形容词形态是 halcyon。',branches=[['安宁、美好的日子','halcyon；halcyon days']],contrasts='不要把神话当生物习性，也不要给来源不明的古鸟名硬套一个逐字分解。',practice='想一段自己会怀念的轻松时光，用 the halcyon days of... 写一句话。',sources=['https://www.etymonline.com/word/halcyon'])
m=json.loads((BASE/'.cache/batch200/rewrite_spec.json').read_text());r=next(x for x in m['roots']if x['id']==ID);c=next(x for x in json.loads((BASE/'.cache/catalog.json').read_text())if x['id']==ID);keep={w['word']for w in W}|set(SHARED);excluded={w:EXCLUDE_REASON for w in(set(r['family'])|set(c['family'])|set(c.get('unmatched',[])))-keep}
ROOT['id']=ID;ROOT['words']=list(dict.fromkeys([w for w in r['family']if w in keep]+[w for w in SHARED if w not in r['family']]));ROOT['exclude']=excluded
assert all(w['word']in m['owned_words']for w in W)
assert not(set(c['family'])|set(c.get('unmatched',[])))-set(ROOT['words'])-set(excluded)
assert {w['word']for w in W}<=set(ROOT['words'])
for w in W:assert len(w['examples'])>=2 and all(len(n)==2 and all(isinstance(x,str)and x for x in n)for n in w['history'])
for k,d in [('roots',[ROOT]),('words',W)]: (OUT/f'{k}_batch200_spec_{TAG}.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
print(ID,len(W),'new,',len(SHARED),'shared')
