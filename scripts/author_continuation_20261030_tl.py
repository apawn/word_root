"""Participial-looking adjectives, stationers and reverse formation in burgle."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'A1760':dict(words=['wretch','wretched','gild','gilded','stud','studded'],label='悲惨、镀金与点缀：-ed 的三种具体理解',note='wretched 继承较早形容词形式并加形容词材料，不能凭结尾编出普通现代动词；gilded 是 gild 的分词，studded 则接装饰凸钉、布满这一支 stud。'),
 'A1699':dict(words=['station','stationary','stationer','stationery','burglar','burglary','burgle'],label='文具和入室行窃：名词词尾与借词历史',note='stationery 对应 stationer + -y，接文具商的货品；burglary 承接较早 burglaria，与 burglar 在现代可作对应。burgle 反而是从 burglar 逆构出来的动词；阅读放在一组，不把历史倒过来。'),
}
W('wretch','/retʃ/','可怜的人；可恶、卑鄙的家伙〔较文学〕',
 '同一个词可以带两种目光：poor wretch 是同情遭罪的人；叫人 a vile wretch，则在谴责这个人卑劣。',
 '古英语 wrecca 流亡者、被放逐的人，经中古英语 wrecche 延续。失去归属、身处困境的旧背景，联系悲惨、可怜以及贬斥义。',
 [['古英语 wrecca → 中古英语 wrecche','流亡、受苦、处境不幸的人'],['现代较文学的 wretch','可怜人；也可贬称可鄙的人']],
 'a poor wretch 可怜的人；a miserable wretch 悲惨的人；a cruel wretch 残酷的家伙。修饰语和语气常能帮助分辨同情还是厌恶。',
 'the poor wretch；a heartless wretch。','wretch /retʃ/ 是人，retch /retʃ/ 是干呕；两者同音。wretch 单独叫别人时可能带贬斥，不总是同情。',
 ('The poor wretch had nowhere to sleep.','那可怜的人连睡觉的地方都没有。'),('The villain was described as a heartless wretch.','那个反派被描述成一个冷酷无情的家伙。'))
W('wretched','英 /ˈretʃɪd/；美 /ˈretʃəd/','悲惨的、难受的；糟糕、可恶的',
 '人过得苦、心里难受，或生活条件很糟，都可以叫 wretched。说 that wretched noise，又是嫌那噪声讨厌。',
 '中古英语 wrecched 承接较早 wrecche 受苦、悲惨的形容词，与 wretch 人物词相连，另有 -ed 形容词材料。不是普通现代动词加过去式。',
 [['wretch 词族的受苦、悲惨材料','处境不幸、痛苦'],['较早形容词 → wretched','悲惨、难受；质量差、令人生厌']],
 'feel wretched 感觉难受、心情很糟；wretched conditions 恶劣条件；a wretched excuse 蹩脚借口。常用读音有两个音节。',
 'a wretched life；that wretched alarm。','wretched 在形容人时可侧重悲惨、难受，不一定是品德坏；形容行为、人品时才可能强调卑劣。看搭配判断。',
 ('The families lived in wretched conditions.','这些家庭生活条件十分恶劣。'),('I felt wretched after arguing with her.','和她争吵后，我心里很难受。'),sources=['https://www.etymonline.com/word/wretched','https://en.wiktionary.org/wiki/wretched#English'])
W('gild','/ɡɪld/','给……镀金、贴金；使表面显得美好',
 '在普通材料外面加一层薄金，外观看起来金光闪闪。比喻用法也常抓住给表面添光彩的感觉。',
 '古英语 gyldan 覆一层金，接 gold 的日耳曼词族，经中古英语 gilden 等延续。金属名称与动词的元音差异有历史来源。',
 [['日耳曼语金的词族 → 古英语 gyldan','用金覆盖表面'],['现代 gild 的具体与比喻义','镀金、贴金；给表面添光彩']],
 'gild a frame 给画框贴金；gild a statue 给雕像镀金；gild the lily 多此一举地美化本来已经很好的东西。',
 'gilded or gilt；gild the edges of a book。','gild 说给表面加金层；make something of gold 才说用金制成整个东西。guild /ɡɪld/ 行会和它同音，但词源不同。',
 ('The craftsperson gilded the wooden frame.','工匠给木画框贴了金。'),('The design is already elegant; extra decoration would gild the lily.','这个设计已经很雅致了，再加装饰会画蛇添足。'),sources=['https://www.etymonline.com/word/gild','https://en.wiktionary.org/wiki/gild#English'])
W('gilded','/ˈɡɪldɪd/','镀金、贴金的；金碧辉煌的、表面光鲜的',
 '先看到一层金色外表：可以是真贴金的镜框，也能借来写看上去奢华光鲜的生活。',
 'gild + -ed，形成分词和形容词。具体金层引出奢华外观、表面美好的比喻；gild 另有常见过去分词 gilt。',
 [['gild 镀金 + -ed','已经覆盖金层的'],['gilded 的形容词与比喻','金碧辉煌；表面光鲜、奢华']],
 'a gilded frame 镀金画框；a gilded ceiling 金饰天花板；a gilded cage 金笼，也比喻奢华却受限制的生活。',
 'gilded furniture；a gilded life。','golden 常说金色、黄金般的；gilded 更直接联系外层贴金。比喻时可能暗示表面光鲜，但每次出现不必都推断里面糟糕。',
 ('A gilded mirror hung above the fireplace.','壁炉上方挂着一面镀金边镜子。'),('She described her luxurious but restricted life as a gilded cage.','她把自己奢华却受束缚的生活形容为金笼。'))
W('stud','/stʌd/','饰钉、凸钉；耳钉；种公畜、种马等〔另一支〕',
 '衣服、鞋底上固定着的小凸点，是一支；a stud farm 里的 stud 则联系繁育马匹。先把这两支分开看。',
 '凸钉、支柱义接古英语 studu 支撑柱等，后来也说固定并突出的钉头、饰物；种畜义接古英语 stod 马群、养马处等另一条旧材料。',
 [['古英语 studu → 支柱、凸钉、饰物支','固定、突出的小构件；相应动词装钉、点缀'],['古英语 stod → 马群、种畜支','种马场、种公畜等']],
 'metal studs 金属饰钉；stud earrings 耳钉；a stud farm 种马场。人物俚语 stud 还可称性吸引力强或性能力强的男人，带明显口语色彩。',
 'diamond studs；a breeding stud。','studded with 的装饰、遍布义接凸钉这一支；stud farm、at stud 接繁育这一支。读音相同不代表可以把具体词义混接。',
 ('Her jacket was decorated with metal studs.','她的夹克上装饰着金属饰钉。'),('They visited a stud farm in the countryside.','他们参观了乡间的一家种马场。'),sources=['https://www.etymonline.com/word/stud','https://en.wiktionary.org/wiki/stud#English'])
W('studded','/ˈstʌdɪd/','镶有、布满、点缀着；装有饰钉的',
 '在一个表面上，许多醒目的小点固定在那里：外套上的饰钉、天空中的星星，都能形成 studded with 的画面。',
 'stud 装凸钉、镶嵌、布满 + -ed。由把一个个凸起饰物固定在表面的动作，扩展到小物分布其间。',
 [['stud 凸钉名词 → 装钉、点缀动词','在表面放置醒目的小物'],['stud + -ed → studded','装有饰钉；遍布、点缀着']],
 'studded with diamonds 镶满钻石；a sky studded with stars 星光点点的天空；a studded belt 饰钉腰带。',
 'studded with small islands；a studded leather jacket。','covered with 更宽泛地说覆盖；studded with 往往突出一个个明显的点、物体分布其中，未必把表面完全遮住。',
 ('The leather belt was studded with silver buttons.','那条皮带上镶着银色扣饰。'),('The dark sky was studded with stars.','漆黑的天空中繁星点点。'))
W('stationer','英 /ˈsteɪʃənə/；美 /ˈsteɪʃənər/','文具商；文具店〔尤英式〕',
 '历史上是在固定店铺卖东西、尤其卖书纸的人，后来职业范围收拢到文具。站定的一处店铺，帮你记住它与 station 的老联系。',
 '中古英语相关人物名词接中世纪拉丁语 stationarius 固定地点经营的商人等，与 statio 站立、位置同族。后来专用于书商、纸品商、文具商。',
 [['statio 位置 → stationarius 等商人称呼','在固定铺位经营的人'],['英语 stationer 的行业专门化','书纸商 → 文具商、文具店']],
 'buy envelopes from a stationer 从文具商处买信封；the stationer’s 文具店；a local stationer 当地文具商。',
 'a stationer’s shop；an independent stationer。','stationer 是商家，stationery 是文具用品。station 的现代车站义不能直接拿来把 stationer 解释成车站工作人员。',
 ('I bought the envelopes at the stationer’s.','我在文具店买了信封。'),('The local stationer sells notebooks and writing paper.','当地文具商出售笔记本和信纸。'),sources=['https://www.etymonline.com/word/stationery','https://en.wiktionary.org/wiki/stationer#English'])
W('stationery','英 /ˈsteɪʃənəri/；美 /ˈsteɪʃəneri/','文具、纸张信封等书写用品',
 '到 stationer 那里买的纸、信封、笔记本等用品，合起来就是 stationery。它把卖东西的人，连到他经营的货品。',
 'stationer 文具商 + 名词材料 -y，与较早 stationery wares 文具商所售货品相连，后来 stationery 单独作集合名词。',
 [['stationer 文具商 → stationery wares','文具商经营的用品'],['stationery 单独作名词','书写用品、纸张信封等文具']],
 'office stationery 办公文具；personalized stationery 印有个人姓名等的信纸、信封；a stationery shop 文具店。通常不可数。',
 'order stationery；a stationery cupboard。','stationary 是静止的，stationery 是文具，读音相同。记忆时可把 stationery 的 e 连到 envelopes，但这只是拼写记忆提示。',
 ('We need to order more office stationery.','我们需要再订一些办公文具。'),('She keeps her stationery in the top drawer.','她把文具放在最上层抽屉里。'),sources=['https://www.etymonline.com/word/stationery','https://en.wiktionary.org/wiki/stationery#English'])
W('burglar','英 /ˈbɜːɡlə/；美 /ˈbɜːrɡlər/','入室窃贼、闯入建筑行窃的人',
 '这个贼的典型画面是进入别人的建筑里偷东西。词的重心在闯入场所，不只是伸手拿走某件物品。',
 '接中世纪拉丁语 burgator、burglator 等形式，与 burgare 闯入等及 burgus 城堡、设防处相连；burgus 又有日耳曼来源。现代并非先有常用动词 burgle 再加后缀。',
 [['中世纪拉丁语 burgus、burgare、burglator 等','设防建筑的材料；闯入、闯入者'],['英语 burglar','入室窃贼；后来逆构出 burgle 动词']],
 'a burglar alarm 防盗警报器；a suspected burglar 嫌疑入室窃贼；a burglar entered through a window 窃贼从窗户进入。',
 'catch a burglar；the burglar broke in。','thief 是较宽泛的偷窃者；burglar 常突出进入建筑行窃，robber 常说抢劫者。这里帮助理解日常用法。',
 ('The burglar entered through an open window.','入室窃贼从一扇敞开的窗户进来了。'),('The noise frightened the burglar away.','那阵声响把窃贼吓跑了。'),sources=['https://www.etymonline.com/word/burglar','https://en.wiktionary.org/wiki/burglar#English'])
W('burglary','英 /ˈbɜːɡləri/；美 /ˈbɜːrɡləri/','入室盗窃、闯入建筑行窃',
 'burglar 说人，burglary 说这类闯入建筑行窃的行为或案件。常见于描述家中被盗、相关警情。',
 '借自较早英格兰拉丁语 burglaria 等行为名词；现代可用 burglar + -y 来认识人物名与行为名的对应。历史上的借入不等于近期加尾造词。',
 [['较早 burglaria 等名词 → 英语 burglary','闯入建筑的盗窃行为'],['burglary 与 burglar 的现代对应','行为、案件 ↔ 行为人']],
 'a burglary at a house 一起住宅入室盗窃；a series of burglaries 一系列入室盗窃案；report a burglary 报告入室被盗。',
 'a burglary investigation；several burglaries。','burglary 是行为、案件，burglar 是人。可数时说某起案件，不可数时谈这类行为；本页取常见语言用法。',
 ('There was a burglary at the house last night.','那栋房子昨晚发生了一起入室盗窃。'),('Several burglaries were reported in the neighbourhood.','附近报告了数起入室盗窃案。'),sources=['https://www.etymonline.com/word/burglary','https://en.wiktionary.org/wiki/burglary#English'])
W('burgle','英 /ˈbɜːɡəl/；美 /ˈbɜːrɡəl/','闯入……行窃、入室盗窃〔尤英式〕',
 '把 burglar 这个人物名倒着加工，人们后来造出了说行动的 burgle。My house was burgled 就是我家遭了入室盗窃。',
 '从 burglar 逆构：把人物词当作含有动作基础，于是补出动词 burgle。历史顺序是已有 burglar，后有 burgle。',
 [['英语已有 burglar 入室窃贼','人物名词在先'],['从 burglar 逆构 burgle','补出入室行窃的动词']],
 'burgle a house 闯入房屋行窃；be burgled 遭入室盗窃。美式还常用 burglarize，burgle 尤常见于英式。',
 'the flat was burgled；burgle an empty house。','很多人物词由动词加 -er 形成，但 burgle 展示逆构方向。学习顺序可以把动词与人物放一起，词源顺序仍须如实说明。',
 ('Their flat was burgled while they were away.','他们不在家时，公寓遭了入室盗窃。'),('Someone tried to burgle the shop during the night.','有人试图在夜间闯进商店行窃。'),sources=['https://www.etymonline.com/word/burgle','https://en.wiktionary.org/wiki/burgle#English'])
def extend_lessons():
    extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
    save('continuation_20261030_tl',ROOTS,WORDS)
    extend_lessons()
