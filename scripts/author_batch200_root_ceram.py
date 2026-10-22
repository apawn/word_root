# coding: utf-8
import json
from pathlib import Path
from lesson_authoring import entry as E
B=[['古希腊 keramos → keramikos','制陶黏土、陶器 → 制陶的'],['英语 ceramic','陶瓷的；陶瓷材料']]
W=[
E('ceramic','英 /sɪˈræmɪk/；美 /səˈræmɪk/','陶瓷的；陶瓷材料','先想到窑里烧出的杯碗，再把范围扩展到工业里的陶瓷零件。','来自希腊 keramikos 制陶的，源于 keramos 制陶黏土、陶器；更早的来源有不同解释，不必硬拆成一个确定的燃烧词根。',B,'a ceramic mug 是陶瓷杯，ceramic tiles 是瓷砖。现代材料科学里的陶瓷范围比日常陶器更广，并不是每种都用黏土捏成，也不都只是餐具。作名词 a ceramic 可指一种陶瓷材料或陶瓷制品。','a ceramic bowl；ceramic tiles；a ceramic coating。','pottery 常把注意力放在黏土烧制的器物或制陶活动；ceramic 还能形容工程材料。porcelain 是瓷，不等于所有陶瓷。',('She drinks tea from a ceramic mug.','她用一个陶瓷杯喝茶。'),('The kitchen floor is covered with ceramic tiles.','厨房地面铺着瓷砖。'),sources=['https://www.etymonline.com/word/ceramic','https://ceramics.org/about/what-are-ceramics/']),
E('ceramics','英 /sɪˈræmɪks/；美 /səˈræmɪks/','陶瓷制品；陶艺；陶瓷学','可以指架子上那一批陶瓷，也可以指把这些东西做出来、研究明白的手艺和学科。','以 ceramic 为基础，-ics 可用于学科、技艺名称；另有 ceramic 作制品名词时的复数用法。',B+[['ceramic → ceramics','陶瓷制品；制陶技艺或研究领域']],'学科或技艺作整体时可用单数谓语：Ceramics is ...；若指一批器物，可用复数谓语：These ceramics are ...。take a ceramics class 通常是去上陶艺课，不一定是学工业材料科学。','a ceramics class；a collection of ceramics；ceramics research。','词尾 s 不总说明在数好几个东西。就像 physics，作为学科名时整体看待；但作为制品复数时又确实可以数一批器物。',('She takes a ceramics class on Saturday mornings.','她每周六上午上陶艺课。'),('These ceramics were made by local artists.','这些陶瓷制品是当地艺术家做的。'),('Ceramics is one of the subjects offered by the art school.','陶艺是这所艺术学校开设的课程之一。'),sources=['https://en.wiktionary.org/wiki/ceramics','https://ceramics.org/career-development/engineer-scientist-resources/'])
]
ROOT=dict(id='C0202',meaning='制陶黏土；陶器',core='CERAM = POTTERY',image='一团黏土做成杯子，经过烧制变成能使用的器物；现代词义又走进了工厂和实验室。',intro='希腊 keramos 指制陶黏土或陶器，keramikos 指制陶的。这个小词族先掌握 ceramic、ceramics 就足够常用：前者常形容材料，后者可指制品、陶艺或学科。',forms='希腊 k 在英语 ceramic 中写成 c，位于 e 前读 /s/。ceramics 的 s 有两种理解：制品的复数，或学科、技艺名称的一部分。',branches=[['材料和制品性质','ceramic'],['一批制品、技艺与学科','ceramics']],contrasts='陶瓷不只等于杯盘，现代工程陶瓷也不必全由黏土制成。ceramics 要根据句子判断是在说器物，还是一门技艺或研究领域。',practice='She studies ceramics and makes ceramic bowls in the studio.\n\n她学习陶艺，在工作室里做陶瓷碗。',words=[x['word'] for x in W],exclude={})
if __name__=='__main__':
 for name,data in [('roots_ceram',[ROOT]),('words_ceram',W)]:Path('.cache/batch200/drafts/root/'+name+'.json').write_text(json.dumps(data,ensure_ascii=False,indent=2))
 print(len(W),sum(len(x['examples']) for x in W))
