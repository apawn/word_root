# -*- coding: utf-8 -*-
"""C0484 gladi: a sword, a fighter, and sword-shaped leaves."""
import json
from pathlib import Path
from lesson_authoring import entry as E
BASE=Path(__file__).resolve().parents[1];OUT=BASE/'.cache/batch200/drafts/rewrite_vid'
W=[
E('gladiator','英 /ˈɡlædieɪtə/；美 /ˈɡlædieɪtər/','古罗马角斗士','名字来自“剑”，实际指在古罗马公开角斗表演中作战的人。记住竞技场与观众，比只记“拿剑的人”更准确。','拉丁 gladius“剑” → gladiator“角斗士、剑斗者” → 英语 gladiator。整个职业名词是借来的；不能凭 -ator 反造一个实际不存在的古典动词当作必经祖先。',[['拉丁 gladius','剑'],['拉丁 gladiator → 英语 gladiator','公开角斗中的战斗者、角斗士']],'角斗士并非普通士兵的别称。角斗有不同装备、规则与人员背景，不能因为名字来自剑，就断言每位角斗士只用同一种剑。现代标题偶尔借它形容公开竞争中的强硬人物，那是后来的比喻。','a Roman gladiator；a gladiator arena；gladiatorial combat〔相关形容词搭配〕。','soldier 是军人，gladiator 的典型舞台是供观众观看的角斗场。glad“高兴”与这个词的剑义无关。',('The exhibition displayed equipment once used by Roman gladiators.','展览陈列了古罗马角斗士曾使用的装备。'),('The film follows a gladiator’s life inside and outside the arena.','电影讲述了一名角斗士在竞技场内外的生活。'),sources=['https://www.etymonline.com/word/gladiator','https://www.oxfordlearnersdictionaries.com/definition/english/gladiator']),
E('gladiolus','英 /ˌɡlædiˈəʊləs/；美 /ˌɡlædiˈoʊləs/','唐菖蒲；剑兰','看它细长、挺立、像剑一样的叶子，“剑兰”这个中文名就能帮你记住拉丁名字里的“小剑”。','拉丁 gladius“剑”的指小形式 gladiolus“小剑”，古代已用作植物名称。英语较早有 gladdon、gladiol 等相关形式；现代 gladiolus 与后来重新借入拉丁植物名、近代植物分类名称有关，不必把所有旧词形串成一条直线。',[['拉丁 gladius → gladiolus','剑 → 小剑；因剑形叶子用于植物命名'],['早期英语 gladdon／gladiol 与后来的拉丁植物名借入','存在不同时间、形式的借词记录'],['现代英语 gladiolus','唐菖蒲、剑兰，常见于园艺和切花语境']],'常见园艺剑兰有细长叶片和沿花茎排列的彩色花朵。名称抓的是叶形，不是说花朵像兵器；古代相似植物的名称也不能直接等同于今天严格的属、种范围。它属于鸢尾科，中文有个“兰”字也不意味着是兰科兰花。','a gladiolus stem；gladiolus flowers；复数 gladioli，也可 gladioluses。gladioli 英常读 /ˌɡlædiˈəʊlaɪ/。','gladiator 与 gladiolus 同接“剑”，一个按持剑作战的人命名，一个按叶片形状命名，花并不是从英语“角斗士”派生的。',('A tall gladiolus stem stood above the other flowers in the vase.','花瓶里，一枝高高的剑兰花茎伸到了其他花的上方。'),('The narrow leaves explain the name gladiolus, meaning “little sword.”','细长的叶片解释了 gladiolus 这个意为“小剑”的名字。'),sources=['https://www.etymonline.com/word/gladiolus','https://www.oxfordlearnersdictionaries.com/definition/english/gladiolus','https://www.merriam-webster.com/dictionary/gladiolus','https://www.rhs.org.uk/plants/gladioli/growing-guide']),
]
m=json.loads((BASE/'.cache/batch200/rewrite_vid.json').read_text());r=next(x for x in m['roots'] if x['id']=='C0484')
ROOT=dict(id='C0484',meaning='剑',core='gladi- 来自拉丁 gladius“剑”。同一件物品，一条路命名使用它的人，一条路命名形状像它的植物。',image='gladius 剑 → gladiator 角斗士；gladius → gladiolus 小剑、剑形叶植物。',intro='这一族不用背抽象口诀：记住竞技场里的角斗士和花园里的剑形叶子，两个单词就各有画面。',forms='gladiator 是完整的拉丁名词借入；gladiolus 是 gladius 的指小形式用于植物名称，再进入英语。gladius 更早的来源有与凯尔特语剑名相连的讨论，不把尚不确定的远源强接为确定链。',branches=[['公开角斗的人','gladiator'],['剑形叶片的花','gladiolus']],contrasts='共同的是拉丁“剑”，不是英语 glad“高兴”。gladiolus 也不是 gladiator 加一个植物后缀。',practice='看到 gladiator 想人和竞技场；看到 gladiolus 想叶子细长如剑。',words=[e['word'] for e in W],exclude={})
if __name__=='__main__':
 assert {e['word'] for e in W}<=set(m['owned_words'])
 for kind,data in [('roots',[ROOT]),('words',W)]: (OUT/(kind+'_batch200_vid_172.json')).write_text(json.dumps(data,ensure_ascii=False,indent=2))
 print('gladi:',len(W),'words;',sum(len(e['examples']) for e in W),'examples')
