# -*- coding: utf-8 -*-
"""C0574 hyal: transparent vitreous naming, not a glass ingredient."""
import json
from pathlib import Path
from lesson_authoring import entry as E
BASE=Path(__file__).resolve().parents[1];OUT=BASE/'.cache/batch200/drafts/rewrite_vid'
W=[E('hyaluronic','英 /ˌhaɪəlʊˈrɒnɪk/；美 /ˌhaɪəlʊˈrɑːnɪk/〔也可带 /j/ 音〕','透明质酸的；常见于 hyaluronic acid〔透明质酸，俗称玻尿酸〕','看到护肤品上的 hyaluronic acid，可以先想到一种能结合水、使周围环境保持黏润的长链糖类物质。它也天然存在于人体组织中，名字里的“玻”并不表示掺了玻璃。','1934 年的命名把 hyaloid“玻璃体的”缩取 hyal-，与 uronic acid“糖醛酸”结合。hyaloid 远接希腊 hyalos“玻璃”：研究者当时从牛眼的玻璃体中分离这种物质；另一部分指出其化学组成。',[['希腊 hyalos → hyaloid；化学词 uronic acid','玻璃 → 玻璃体的；糖醛酸'],['1934 年 hyal(oid) + uronic acid','将分离部位和化学成分结合命名'],['英语 hyaluronic acid','透明质酸；hyaluronic 通常作为名称中的形容词']],'它由重复的糖类单元构成长链，能形成黏性的含水环境，存在于皮肤、关节滑液、眼的玻璃体等部位。记名称时，把“透明、胶状的眼内物质”和“糖类长链”接在一起，比逐字硬译成“玻璃加尿”更准确。看到 acid 也不能直接把它等同于护肤语境里的去角质酸。','hyaluronic acid；a serum containing hyaluronic acid；hyaluronic acid in connective tissue。这个形容词最常和 acid 连用，中文通常按整个名称译。','hyaluronic acid 是一种具体物质的名称；hyal- 只是其中的历史命名材料，不是所有透明或保湿成分都叫这个名字。',('Hyaluronic acid is listed among the ingredients of this moisturizer.','这款保湿产品的成分表中列有透明质酸。'),('Hyaluronic acid occurs naturally in the fluid inside joints.','关节内的滑液中天然存在透明质酸。'),sources=['https://www.collinsdictionary.com/dictionary/english/hyaluronic-acid','https://www.merriam-webster.com/dictionary/hyaluronic%20acid','https://www.sciencedirect.com/science/article/pii/S0021925818753386','https://portlandpress.com/biochemj/article-pdf/235/3/903/586657/bj2350903.pdf','https://www.cancer.gov/publications/dictionaries/cancer-drug/def/hyaluronic-acid'])]
cat=next(x for x in json.loads((BASE/'.cache/catalog.json').read_text()) if x['id']=='C0574');names=[x['word'] for x in W]
EX={w:'较专门的组织透明外观或眼部膜结构术语，按当前常见阅读范围暂略。' for w in cat['family'] if w not in names}
ROOT=dict(id='C0574',meaning='玻璃；玻璃般透明',core='hyal- 接希腊 hyalos“玻璃”。科学词借的是透明、玻璃样的外观，随后也用于眼内透明胶状的玻璃体。',image='玻璃 hyalos → 玻璃体的 hyaloid → hyal(oid) + uronic acid → hyaluronic acid 透明质酸。',intro='最容易遇见它的地方是护肤成分表。名字记录了发现与命名的历史，理解这一点就不必把中文“玻尿酸”拆成两种日常物品。',forms='hyaluronic 中的 hyal- 经 hyaloid“玻璃体的”而来，后半与 uronic acid“糖醛酸”结合；整个化学名称是近代命名。',branches=[['透明组织与现代成分名称','hyaluronic']],contrasts='透明质酸不是玻璃颗粒；acid 在这个名称中表示化学性质，不能只靠一个后缀推断产品用途。',practice='读到 hyaluronic acid 时，说出完整名称“透明质酸”，再回忆“玻璃体＋糖醛酸”的命名线索。',words=names,exclude=EX)
if __name__=='__main__':
 for kind,data in [('roots',[ROOT]),('words',W)]: (OUT/(kind+'_batch200_vid_218.json')).write_text(json.dumps(data,ensure_ascii=False,indent=2))
 print('hyal: 1 word; 2 examples')
