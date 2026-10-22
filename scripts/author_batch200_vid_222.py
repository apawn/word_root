# -*- coding: utf-8 -*-
"""C0419 fet: a concrete, unpleasant smell."""
import json
from pathlib import Path
from lesson_authoring import entry as E
BASE=Path(__file__).resolve().parents[1];OUT=BASE/'.cache/batch200/drafts/rewrite_vid'
W=[E('fetid','/ˈfetɪd/〔英式也读 /ˈfiːtɪd/，也写 foetid〕','恶臭的；发臭的','推开一间久未清理、空气不流通的屋子，一股腐败的臭气迎面而来。fetid 抓住的就是让人想避开的难闻气味。','借拉丁 fetidus“发臭的”，来自动词 fetere“发臭”；英语在中古时期借入。foetid 是同一词的另一拼写，不能把 foe 当成“敌人”来拆。',[['拉丁 fetere','发出难闻气味'],['拉丁 fetidus〔也见 foetidus 拼写〕','臭的、发臭的'],['中古英语 → 英语 fetid／foetid','恶臭的，常见于书面描写']],'这个词比 bad-smelling 更有画面，常修饰 air、water、breath 等：臭气、臭水、难闻的口气。它描述嗅觉感受，不凭一个词就确定气味来自哪种疾病或哪种化学物质。','fetid air；fetid water；fetid breath；a fetid smell。偏正式或文学描写。','stuffy 重点是不通风、闷，未必恶臭；fetid 强调臭。fetal“胎儿的”虽字形相近，却不来自“发臭”这条来源。',('Fetid air escaped when they opened the cellar door.','他们打开地窖门时，一股臭气涌了出来。'),('The abandoned canal was filled with fetid water.','废弃的运河里满是发臭的水。'),sources=['https://www.etymonline.com/word/fetid','https://www.oxfordlearnersdictionaries.com/definition/english/fetid'])]
names=['fetid'];cat=next(x for x in json.loads((BASE/'.cache/catalog.json').read_text()) if x['id']=='C0419');EX={w:'较罕见、偏医学书面语的恶臭名词，按当前阅读范围暂略。' for w in cat['family'] if w not in names}
ROOT=dict(id='C0419',meaning='发臭',core='fet- 接拉丁 fetere“发臭”。不必寻找抽象寓意，先记住一股令人退后的臭气。',image='fetere 发臭 → fetidus 发臭的 → fetid／foetid 恶臭的。',intro='这条来源可以帮助读懂文学和环境描写中的 fetid。它写的是气味，不是单纯脏乱，也不是单纯缺少新鲜空气。',forms='fetid 是拉丁形容词借入英语，foetid 为另一拼写；英语里没有必要硬找一个独立的 fet 加 -id。',branches=[['臭气、臭水的描写','fetid']],contrasts='fetid 强调恶臭，stuffy 强调闷；fetal 与 fetus 属于另一条词源。',practice='把 fetid air 换成一句具体中文“空气里有一股臭味”，再体会它比“空气不好”多表达了什么。',words=names,exclude=EX)
if __name__=='__main__':
 for kind,data in [('roots',[ROOT]),('words',W)]: (OUT/(kind+'_batch200_vid_222.json')).write_text(json.dumps(data,ensure_ascii=False,indent=2))
 print('fet: 1 word; 2 examples')
