# -*- coding: utf-8 -*-
"""C0479 geran: the crane's bill in a plant name."""
import json
from pathlib import Path
from lesson_authoring import entry as E
BASE=Path(__file__).resolve().parents[1];OUT=BASE/'.cache/batch200/drafts/rewrite_vid'
W=[E('geranium','/dʒəˈreɪniəm/','天竺葵〔常见园艺称呼〕；老鹳草属植物','看一眼一些相关植物细长、尖尖的果实，想象鹤的长嘴，就能明白一个花名为什么藏着鸟的名字。','接希腊 geranos“鹤”，其指小形式 geranion 被用作植物名称，因果实形似鸟喙；经拉丁 geranium 以及植物命名传统进入英语。不是英语里把 geran 和 ium 临时拼成的花名。',[['希腊 geranos → geranion','鹤 → 因果实似鹤喙而用的植物名'],['拉丁及植物命名 geranium','沿用古典植物名称'],['英语 geranium','老鹳草属植物；日常也常称天竺葵属的园艺植物']],'园艺里的名称有个容易踩的坑：窗台花盆中常被叫作 geranium 的天竺葵，多属 Pelargonium；正式属名 Geranium 则是另一属，常见说法是 hardy geraniums。两者名称有历史联系，现代分类却要区分。','red geraniums；a pot of geraniums；hardy geraniums；scented geraniums。','小写常用名 geranium 的范围取决于场景；大写斜体属名 Geranium 指严格分类。别把一个日常花名直接当成唯一的科学属名。',('She placed a pot of red geraniums by the window.','她把一盆红色天竺葵放在窗边。'),('The guide distinguishes hardy geraniums from the pelargoniums commonly sold as geraniums.','指南区分了耐寒的老鹳草属植物和市面上常以 geraniums 称呼的天竺葵属植物。'),sources=['https://www.etymonline.com/word/geranium','https://www.oxfordlearnersdictionaries.com/definition/english/geranium','https://www.rhs.org.uk/plants/pelargonium?type=0'])]
m=json.loads((BASE/'.cache/batch200/rewrite_vid.json').read_text())
ROOT=dict(id='C0479',meaning='鹤',core='geran- 接希腊 geranos“鹤”。植物果实的细长尖端像鸟喙，于是鸟名成了植物命名的材料。',image='鹤 geranos → 似鹤喙的植物名 geranion → geranium。',intro='用鸟喙这个形状记住名称，再留意园艺俗名与科学分类不总是一对一。',forms='geranium 经希腊植物名和拉丁形式传入，词尾保留古典名词形态。现代日常 geranium 与正式属名 Geranium 的范围需要按语境分开。',branches=[['因果实形状得名的花卉','geranium']],contrasts='geranium 不是“花像一只鹤”的硬猜；可考的命名联系在果实的鸟喙形状。常见天竺葵属 Pelargonium 与 Geranium 属也不相同。',practice='先想象长鸟喙，再用一句话提醒自己：花店俗名不一定等于严格的植物属名。',words=['geranium'],exclude={})
if __name__=='__main__':
 assert {e['word'] for e in W}<=set(m['owned_words'])
 for kind,data in [('roots',[ROOT]),('words',W)]: (OUT/(kind+'_batch200_vid_208.json')).write_text(json.dumps(data,ensure_ascii=False,indent=2))
 print('geran:',len(W),'words;',sum(len(e['examples']) for e in W),'examples')
