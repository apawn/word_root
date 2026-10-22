# -*- coding: utf-8 -*-
"""C0887 onc: a mass, tumors, and the modern cancer specialty."""
import json
from pathlib import Path
from lesson_authoring import entry as E
BASE=Path(__file__).resolve().parents[1];OUT=BASE/'.cache/batch200/drafts/rewrite_vid'
W=[
E('oncology','英 /ɒŋˈkɒlədʒi/；美 /ɑːnˈkɑːlədʒi/','肿瘤学；肿瘤科','从“身体里异常长出的团块”这个画面入手，再想到专门研究、诊断和治疗肿瘤的医学领域。现代医院语境尤其围绕癌症。','onco- 接希腊 onkos“体积、团块、肿胀”等义，-logy 表示学问。英语在十九世纪用这些古典构件形成 oncology；不必编出一个古希腊就有的完整专科名称。',[['希腊 onkos → 现代组合形式 onco-','团块、肿胀 → 医学中的肿瘤'],['onco- + -logy → 英语 oncology','十九世纪构成肿瘤研究的学科名'],['现代医学 oncology','研究肿瘤，并专门诊断、治疗癌症的领域']],'读到 an oncology department，就是医院的肿瘤科。radiation oncology 是放射肿瘤学，surgical oncology 是肿瘤外科领域。词根里的“团块”帮助记来源，但不能由此反推每个肿块都是癌症，或每种癌症都形成一个实体肿块。','medical oncology；radiation oncology；surgical oncology；an oncology department。学科名一般不可数。','oncology 是领域，oncologist 是其中的专科医生；tumor 是肿瘤，可能良性也可能恶性，不与 cancer 在所有语境中完全相等。',('She works in the hospital’s oncology department.','她在医院的肿瘤科工作。'),('The conference brought together researchers from several branches of oncology.','这次会议汇集了肿瘤学多个分支的研究人员。'),sources=['https://www.cancer.gov/about-cancer/understanding/what-is-cancer','https://www.etymonline.com/word/oncology','https://www.oxfordlearnersdictionaries.com/definition/english/oncology','https://www.cancer.gov/publications/dictionaries/cancer-terms/def/oncology']),
E('oncologist','英 /ɒŋˈkɒlədʒɪst/；美 /ɑːnˈkɑːlədʒɪst/','肿瘤科医生；肿瘤学专家','看到 -ist，就把镜头从科室转到人：这是专门从事肿瘤诊疗的医生。','与 oncology 配套，用 -ist 表示从业者；也可分析为 onco- + -logist。古老材料仍是希腊 onkos“团块、肿胀”，整个职业名称是现代派生。',[['希腊 onkos → onco-；onco- + -logy → oncology','肿瘤概念 → 肿瘤学'],['oncology 的专业人员名称 oncologist','用 -ist 形成从事这一领域的人名词']],'an oncologist 通常是受过肿瘤诊疗专门训练的医生，并不只是“会研究团块的人”。前面再加 radiation、medical、surgical，会进一步说明专长。谈研究人员时也可能采用较宽的专家义，要结合所在机构和工作内容理解。','see an oncologist；a consultant oncologist；a radiation oncologist；an oncologist’s assessment。','oncologist 指专科身份；surgeon 指外科医生。surgical oncologist 两者兼有，但并非每位 oncologist 都以做手术为主要工作。',('The oncologist explained the report in plain language.','肿瘤科医生用通俗的话解释了这份报告。'),('A radiation oncologist joined the meeting to discuss the case.','一位放射肿瘤科医生参加会议，讨论这个病例。'),sources=['https://www.cancer.gov/about-cancer/understanding/what-is-cancer','https://www.etymonline.com/word/oncology','https://www.oxfordlearnersdictionaries.com/definition/english/oncologist','https://www.cancer.gov/publications/dictionaries/cancer-terms/def/oncologist']),
]
EX={w:'过于专门的细胞或病理分类术语，按常用阅读范围暂略。' for w in ['oncogenesis','oncocyte','oncocytoma']}
ROOT=dict(id='C0887',meaning='团块、肿胀；肿瘤',core='onkos 原本有团块、体积、肿胀的意思。近代医学取它来表示肿瘤，形成 onco- 这一组合形式。',image='onkos 团块、肿胀 → onco- 肿瘤 → oncology 肿瘤学／oncologist 肿瘤科医生；onco- + gene → oncogene 癌基因。',intro='本族常在医学报道和医院科室介绍里出现。先认出 oncology 是领域、oncologist 是人，再看 oncogene 所说的基因作用。',forms='onco- 的 o 是组合形式的一部分；onc- 也用于记录这条词根。希腊 onkos 更早来源并不确定，可靠学习路线从这个希腊名词开始。',branches=[['医学领域与专家','oncology, oncologist'],['基因与癌症机制','oncogene']],contrasts='肿块、肿瘤与癌症不是三个完全等价的词。词源提供记忆线索，现代医学词义仍要看每个完整词。',practice='an oncology clinic 是科室，an oncologist 是医生，an oncogene 是基因。先辨对象，就不会把这三个相似词混在一起。',words=[e['word'] for e in W]+['oncogene'],exclude=EX)
if __name__=='__main__':
 m=json.loads((BASE/'.cache/batch200/rewrite_vid.json').read_text());r=next(x for x in m['roots'] if x['id']==ROOT['id'])
 assert {w for w in r['family'] if '-' not in w}<=set(ROOT['words'])|set(EX)
 assert {e['word'] for e in W}<=set(m['owned_words'])
 for kind,data in [('roots',[ROOT]),('words',W)]: (OUT/(kind+'_batch200_vid_153.json')).write_text(json.dumps(data,ensure_ascii=False,indent=2))
 print('onc:',len(W),'words;',sum(len(e['examples']) for e in W),'examples')
