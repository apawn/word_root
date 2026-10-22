# -*- coding: utf-8 -*-
"""C1421 stich: a line of verse or a row in a register."""
import json
from pathlib import Path
from lesson_authoring import entry as E
BASE=Path(__file__).resolve().parents[1];OUT=BASE/'.cache/batch200/drafts/rewrite_vid'
W=[E('cadastre','英 /kəˈdæstə/；美 /kəˈdæstər/〔也写 cadaster〕','地籍；土地登记簿或地籍信息系统','把一片地方的土地分成一块块有编号的地块，每块对应边界、位置和相关登记资料。把这些资料有系统地连在一起，就是理解 cadastre 的入口。','借法语 cadastre，经意大利 catastro、较早 catastico，远接晚期希腊 katastichon“登记册”。里面的 kata stichon 是“逐行、按行”，所以它与 stichos“行”有关，不是英语 cast 或 disaster 的变体。',[['希腊 kata；stichos','按、依照；行'],['晚期希腊 katastichon','逐行记下的登记册'],['威尼斯／意大利 catastico → catastro → 法语 cadastre','登记册，发展为土地登记名称'],['英语 cadastre／cadaster','地籍登记；土地信息系统']],'旧式图像可以是一页页地块清册，现代则常是地图与数据库相互连接。它可服务于税收、土地管理、规划等用途；具体登记哪些权利和信息，取决于相应制度，不能把它简单看成一张普通街道地图。','a land cadastre；a digital cadastre；update the cadastre；cadastral maps〔地籍图〕。','map 可以只是地图；cadastre 通常把地块图形与登记资料关联。这个名称本身不说明某一条记录在每个地方都具有完全相同的法律效力。',('The new digital cadastre links each land parcel to its records.','新的数字地籍系统把每块土地与相应记录关联起来。'),('The survey team updated the boundaries shown in the cadastre.','测量团队更新了地籍资料中标示的边界。'),sources=['https://www.merriam-webster.com/dictionary/cadastre','https://www.collinsdictionary.com/dictionary/english/cadastre','https://en.wiktionary.org/wiki/cadastre#English','https://www.fig.net/organisation/comm/7/library/reports/cadastre/statement_on_cadastre.html'])]
names=['acrostic','cadastre'];cat=next(x for x in json.loads((BASE/'.cache/catalog.json').read_text()) if x['id']=='C1421');EX={w:'较冷门的诗律、排叶形态、行数或占卜细分术语，按当前通用阅读范围暂略。' for w in cat['family'] if w not in names}
ROOT=dict(id='C1421',meaning='行；一排；诗行',core='stich- 接希腊 stichos“一行、一排”。诗句一行行排开，账册也一行行登记；两个场景就能串起本页。',image='诗行的端头 → acrostic 藏头文字；逐行登记 kata stichon → katastichon → cadastre 地籍。',intro='acrostic 仍较容易看出诗行的残留；cadastre 经多个语言阶段后字形变化较大，必须沿历史才能认出“逐行登记”这一线索。',forms='acrostic 经希腊、拉丁、法语路线传来，-stich 后来受到 -ic 词尾形式影响；cadastre 经意大利与法语接晚期希腊登记册名称。',branches=[['诗行中的隐藏文字','acrostic'],['一行行登记土地','cadastre']],contrasts='acrostic 不是 acronym 的别名；cadastre 也不是普通地形图的同义词。共同的“行”只是历史材料，现代对象完全不同。',practice='先从几行诗的首字母找隐藏词，再想象逐行登记地块资料，分别回忆 acrostic 和 cadastre。',words=names,exclude=EX)
if __name__=='__main__':
 for kind,data in [('roots',[ROOT]),('words',W)]: (OUT/(kind+'_batch200_vid_232.json')).write_text(json.dumps(data,ensure_ascii=False,indent=2))
 print('stich: 1 new; 2 examples; 1 shared')
