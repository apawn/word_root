# -*- coding: utf-8 -*-
from pathlib import Path
import json
from lesson_authoring import entry as E
BASE=Path(__file__).resolve().parents[1];OUT=BASE/'.cache/batch200/drafts/rewrite_spec'
ID='C1506';TAG='244_than';SHARED=['euthanasia','euthanize'];EXCLUDE_REASON='按用户当前范围暂略：较冷门的死亡相关分类、恐惧症名称或诗学专门词。'
W=[E('thanatology','英 /ˌθænəˈtɒlədʒi/；美 /ˌθænəˈtɑːlədʒi/','死亡学；对死亡及相关心理社会现象的研究','研究的不仅是生命停止，也包括人怎样理解死亡、面对失去。','thanato- 来自希腊 thánatos“死亡”，加近代学科后缀 -logy，后者远接 lógos“论述”。是近代组合名称，不是古希腊已经存在一门同名现代学科。',[['希腊 thánatos〔死亡〕与 lógos〔论述〕','两个来源材料并列'],['近代 thanato- + -logy','形成死亡研究的学科名称'],['英语 thanatology','涵盖死亡现象、哀伤及相关社会心理问题']],'它可以讨论身体死亡，也可以讨论丧亲后的悲伤、临终经验以及文化如何纪念逝者。因而不能把它缩成“研究尸体”的技术学科，更不是赞成或实施某种结束生命的做法。','a course in thanatology；research in thanatology；the field of thanatology。通常不可数。','thanatology 是研究领域；euthanasia 是具有特定伦理和实践含义的词。共同的死亡成分不能抹掉两者的用途差别。',('Her course in thanatology examines how different cultures understand death.','她的死亡学课程探讨不同文化怎样理解死亡。'),('The article connects thanatology with research on grief and bereavement.','这篇文章把死亡学与哀伤、丧亲研究联系起来。'),sources=['https://www.merriam-webster.com/dictionary/thanatology','https://en.wiktionary.org/wiki/thanatology'])]
ROOT=dict(meaning='死亡',core='thanat- 指死亡这个主题，后面的成分决定是在讨论研究领域还是特定行为。',image='加 -logy 成为死亡研究；与 eu-“好、安适”结合则进入 euthanasia 的历史命名。',intro='这组适合用来理解社会、伦理和医疗文章里的用词。词根只交代死亡这一主题，具体词义不能全部压成一个“死”。',forms='希腊 thánatos 的构词形式常写 thanato-；在 euthanasia 中保留 thanas- 这一相关词形。',branches=[['死亡研究','thanatology'],['另一种特定概念及其动词','euthanasia、euthanize']],contrasts='than- 与英语比较词 than 只是字母相同；研究死亡也不等于赞同某一种死亡安排。',practice='分别用“研究领域”和“特定概念”说明 thanatology 与 euthanasia 为什么不能互换。',sources=['https://www.merriam-webster.com/dictionary/thanatology','https://www.etymonline.com/word/euthanasia'])
m=json.loads((BASE/'.cache/batch200/rewrite_spec.json').read_text());r=next(x for x in m['roots']if x['id']==ID);c=next(x for x in json.loads((BASE/'.cache/catalog.json').read_text())if x['id']==ID);keep={w['word']for w in W}|set(SHARED);excluded={w:EXCLUDE_REASON for w in(set(r['family'])|set(c['family'])|set(c.get('unmatched',[])))-keep}
ROOT['id']=ID;ROOT['words']=list(dict.fromkeys([w for w in r['family']if w in keep]+[w for w in SHARED if w not in r['family']]));ROOT['exclude']=excluded
assert all(w['word']in m['owned_words']for w in W)
assert not(set(c['family'])|set(c.get('unmatched',[])))-set(ROOT['words'])-set(excluded)
assert {w['word']for w in W}<=set(ROOT['words'])
for w in W:assert len(w['examples'])>=2 and all(len(n)==2 and all(isinstance(x,str)and x for x in n)for n in w['history'])
for k,d in [('roots',[ROOT]),('words',W)]: (OUT/f'{k}_batch200_spec_{TAG}.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
print(ID,len(W),'new,',len(SHARED),'shared')
