# -*- coding: utf-8 -*-
"""C1023 phloe: bark-derived name for sugar-conducting tissue."""
import json
from pathlib import Path
from lesson_authoring import entry as E
BASE=Path(__file__).resolve().parents[1];OUT=BASE/'.cache/batch200/drafts/rewrite_vid'
W=[E('phloem','英 /ˈfləʊem/；美 /ˈfloʊem/','韧皮部','叶片制造了糖，正在生长的芽、根或果实也需要这些物质。把糖等有机物从供应处运到使用或储存处的植物组织，就是 phloem。','来自 19 世纪德语植物学名称 Phloëm，由 Nägeli 取希腊 phloos／phloios“树皮、外皮”命名，并配以希腊式词尾。英语后来借入这个科学名词；不是英语 flow“流动”的变形。',[['希腊 phloos／phloios','树皮、外皮'],['德语植物学名称 Phloëm〔Nägeli，1858〕','用“树皮”相关材料命名植物组织'],['英语 phloem〔19 世纪后期〕','韧皮部：运输糖等有机物的维管组织']],'可以把它记成植物的“糖运输网络”，但它运的并不只有糖。运输方向由哪里提供、哪里需要来决定：有的通路向上，有的向下，不是固定只从叶片往根走。名称源于树皮，也不表示它等于整层树皮或只存在于树木中。','phloem tissue；transport through the phloem；phloem sap；xylem and phloem。通常不可数；开头 ph 读 /f/。','xylem 主要负责水和矿质的运输，也有支撑作用；phloem 主要运输糖等有机物。两者是植物内部不同组织，不能把前者叫木头、后者叫整张树皮就算解释完。',('Sugars move through the phloem from mature leaves to growing shoots.','糖通过韧皮部从成熟叶片运向正在生长的新梢。'),('The diagram distinguishes the phloem from the xylem in the stem.','图中区分了茎中的韧皮部与木质部。'),sources=['https://www.merriam-webster.com/dictionary/phloem','https://www.collinsdictionary.com/dictionary/english/phloem','https://www.oxfordlearnersdictionaries.com/definition/english/phloem','https://www.etymonline.com/word/phloem','https://openstax.org/books/biology/pages/30-5-transport-of-water-and-solutes-in-plants','https://openstax.org/books/biology/pages/30-1-the-plant-body'])]
names=['phloem'];cat=next(x for x in json.loads((BASE/'.cache/catalog.json').read_text()) if x['id']=='C1023');EX={w:'较冷门的树皮化学或细分生物学术语，当前先保留基础植物组织名称。' for w in cat['family'] if w not in names}
ROOT=dict(id='C1023',meaning='树皮；外皮',core='希腊 phloos／phloios 指树皮、外皮。近代植物学借这个名称形成 phloem，指承担糖等有机物运输的韧皮部。',image='phloos／phloios 树皮 → 德语植物学 Phloëm → 英语 phloem 韧皮部。',intro='先记“植物把叶片等处供应的糖送到需要的地方”，再记这个组织的名称。树皮是词源入口，运输组织才是现代概念。',forms='phloe- 接希腊 phloios；phloem 是经德语命名后进入英语的近代术语，不是古希腊已有完整植物生理学定义的原样搬运。',branches=[['植物的有机物运输组织','phloem']],contrasts='phloem 不等于整层树皮，也不是 flow 的派生词。它和 xylem 是不同组织，运输方向不能简单固定为“一个向上、一个向下”。',practice='用 phloem 把三个地点连起来：糖的供应处、运输通道、需要或储存糖的部位。',words=names,exclude=EX)
if __name__=='__main__':
 for kind,data in [('roots',[ROOT]),('words',W)]: (OUT/(kind+'_batch200_vid_251.json')).write_text(json.dumps(data,ensure_ascii=False,indent=2))
 print('phloe: 1 new; 2 examples')
