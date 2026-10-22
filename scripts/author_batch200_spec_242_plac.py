# -*- coding: utf-8 -*-
from pathlib import Path
import json
from lesson_authoring import entry as E
BASE=Path(__file__).resolve().parents[1];OUT=BASE/'.cache/batch200/drafts/rewrite_spec'
ID='C1052';TAG='242_plac';SHARED=[];EXCLUDE_REASON='按用户当前范围暂略：专门胚胎结构或动物分类名。'
P=[['希腊 plax／plak-〔平面〕及相关饼名','平展、扁平的形象'],['拉丁 placenta','一种扁平的饼'],['近代拉丁 placenta uterina','借饼状外形命名胎盘']]
W=[E('placenta','/pləˈsentə/','胎盘；植物的胎座','名字来自一张扁平的饼，指的却是生命发育时的一种重要结构。','借近代拉丁 placenta，是 placenta uterina“子宫中的饼”这类名称的简化。拉丁 placenta 原指扁饼，再往前接希腊平展、饼状的词族；现代英语不能拆成 place + nta。',P+[['英语 placenta','胎盘；植物学也用于胎座']],'在人类妊娠中，胎盘连接母体环境与胎儿，承担氧气、营养等物质的交换，也产生激素。它与脐带相关，但并不是脐带本身。植物学中的 placenta 则指胚珠着生的部分，是同一名称在另一领域的使用。','the placenta；the development of the placenta；placentas 或 placentae。','placenta 是胎盘；umbilical cord 是脐带。词源里的“饼”描述外形，不是在说其功能像食物。',('The diagram shows the placenta attached to the wall of the uterus.','示意图展示了胎盘附着在子宫壁上的位置。'),('In the flower diagram, the ovules are attached to the placenta.','在这张花的结构图中，胚珠着生于胎座。'),sources=['https://www.etymonline.com/word/placenta','https://www.merriam-webster.com/dictionary/placenta']),
E('placental','/pləˈsentəl/','胎盘的；有胎盘类的；有胎盘类哺乳动物','把话题限定到胎盘，或与它有关的一类哺乳动物。','历史上借近代拉丁 placentalis，来自 placenta；现代可按 placenta + -al 理解。并非仅因为英语已有 placenta 就断言形容词首次在英语中派生。',P+[['近代拉丁 placentalis','与胎盘相关的形容词'],['英语 placental','胎盘的；有胎盘类的，亦可作名词']],'placental tissue 是胎盘组织，placental development 是胎盘发育。说 placental mammals 时，它还是动物分类中的固定名称，例如人、狗、鲸所在的有胎盘类；这个分类名称不能简单理解为所有具有任何形式胎盘的动物。','placental tissue；placental mammals；a placental。最后一种是把分类形容词当名词用。','placenta 是结构名称；placental 通常用来修饰另一个词。分类义中也可指一只或一种有胎盘类动物。',('The study compares placental development in several mammals.','这项研究比较了几种哺乳动物的胎盘发育。'),('Whales are placental mammals, although they live in water.','鲸虽然生活在水中，却属于有胎盘类哺乳动物。'),sources=['https://www.etymonline.com/word/placental','https://www.merriam-webster.com/dictionary/placental'])]
ROOT=dict(meaning='平面；扁平的形状',core='这里的 plac- 先让你想到一张扁饼，再用这个外形认识 placenta。',image='平展的表面 → 扁平的饼 → 借外形命名胎盘。',intro='词源常按外形给器官取名。这种命名能帮助记忆，但器官真正的功能还要回到现代含义来理解。',forms='希腊 plax 的词干 plak- 在相关借词中写成 plac-；placenta 借自近代拉丁医学名称。',branches=[['结构名称','placenta'],['相关形容词和分类词','placental']],contrasts='这组接希腊“平展”的词族；不能把它当成 placate“安抚”或 please“使高兴”的同一直接来源。',practice='把 placenta 想成饼状结构，再用 placental 修饰 tissue 和 mammals，体会结构义与分类义的差别。',sources=['https://www.etymonline.com/word/placenta'])
m=json.loads((BASE/'.cache/batch200/rewrite_spec.json').read_text());r=next(x for x in m['roots']if x['id']==ID);c=next(x for x in json.loads((BASE/'.cache/catalog.json').read_text())if x['id']==ID);keep={w['word']for w in W}|set(SHARED);excluded={w:EXCLUDE_REASON for w in(set(r['family'])|set(c['family'])|set(c.get('unmatched',[])))-keep}
ROOT['id']=ID;ROOT['words']=list(dict.fromkeys([w for w in r['family']if w in keep]+[w for w in SHARED if w not in r['family']]));ROOT['exclude']=excluded
assert all(w['word']in m['owned_words']for w in W)
assert not(set(c['family'])|set(c.get('unmatched',[])))-set(ROOT['words'])-set(excluded)
assert {w['word']for w in W}<=set(ROOT['words'])
for w in W:assert len(w['examples'])>=2 and all(len(n)==2 and all(isinstance(x,str)and x for x in n)for n in w['history'])
for k,d in [('roots',[ROOT]),('words',W)]: (OUT/f'{k}_batch200_spec_{TAG}.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
print(ID,len(W),'new,',len(SHARED),'shared')
