"""Stick: related old noun and verb branches, familiar tools and physical comedy."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
ST=[['古英语 sticca〔名词〕→ stick','枝条、杆、棒；与刺、固定的同族背景相关'],['古英语 stician〔动词〕→ stick','刺入、扎住、固定 → 粘住、停留、坚持'],['现代名词与动词分工','条棒形状；固定、附着等动作并行，不是所有动词由现代木棍名词才造出']]
def S(f,m):return ST+[[f,m]]
W('stick','/stɪk/','棍、棒、条；粘贴、粘住；固定、卡住；坚持',
 '一根细棒是一条支线；另一条抓住扎进去就留在那里，后来胶粘住、原则坚持住也能接上。',
 '名词 sticca、动词 stician 都有古英语旧形式，同族但传承路径不同。动词从刺、固定走向附着、持续，不必编成木棍涂胶才有粘义。变化 stick—stuck—stuck。',ST,
 'a wooden stick 木棍，stick a label on 贴标签，stick to the plan 坚持计划，get stuck 卡住，stick around 留一会儿。',
 'a wooden stick；stick a label on；stick to；get stuck；stick around。',
 'stick to a plan 坚持计划，不是拿棍子；a stick of butter 一条黄油接条状物。stuck 是过去、分词，标准变化不写 sticked。',
 ('Stick the label on the outside of the box.','把标签贴在箱子外面。'),('We decided to stick to the original plan.','我们决定坚持原计划。'),sources=['https://www.etymonline.com/word/stick','https://en.wiktionary.org/wiki/stick#English'])
W('sticky','/ˈstɪki/','黏的；闷热潮湿的；棘手、难办的',
 '手碰上去粘住，问题碰上去也脱不开；天气让皮肤黏糊糊，也可以 sticky。',
 'stick 动词附着、卡住 + -y，描述相关性质。困难情形的比喻接摆脱不易，不是问题真涂了糖浆。',S('stick + -y → sticky','易粘；引申闷黏、棘手难脱身'),
 'sticky fingers 黏手指，sticky tape 胶带，sticky weather 闷热潮湿天气，a sticky situation 棘手局面。',
 'sticky tape；sticky fingers；sticky weather；a sticky situation。',
 'sticky 粘、难处理，stuck 已被卡住；a sticky door 难开、卡涩的门，与 I am stuck 我被困住角色不同。',
 ('The table was sticky with spilled juice.','桌上洒了果汁，黏糊糊的。'),('The mistake put us in a sticky situation.','错误让我们陷入了棘手局面。'))
W('sticker','英 /ˈstɪkə/；美 /ˈstɪkər/','贴纸；粘贴标签；数码表情贴图',
 '一面能粘，贴到本子、箱子上；聊天里也借来叫一张张表情贴图。',
 'stick 粘、附着 + -er，后缀形成器物名，不是所有 -er 都指人。数字贴纸名称后来沿用实体贴纸形象。',S('stick + -er → sticker','可粘贴标签；后有数码贴图用法'),
 'a price sticker 价格标签，a sticker on a notebook 本子贴纸，send a sticker 发送表情贴图；sticker price 是标价。',
 'a price sticker；a sticker on；send a sticker；sticker price。',
 'sticker 可自己粘，label 泛指标签，不必自带胶；sticker price 标出的价格，不保证最终交易价完全一样。',
 ('She put a star sticker on the notebook.','她在本子上贴了一张星星贴纸。'),('The child peeled the sticker off the box.','孩子把贴纸从箱子上揭下来。'))
W('lipstick','/ˈlɪpstɪk/','口红；唇膏〔着色化妆品〕',
 '给嘴唇上色的化妆品，名字保留了膏体做成条棒的传统外形。',
 'lip 嘴唇 + stick 条棒形物。今天也有液态等口红形式，不能由词名反推所有产品必须是一根硬棒。',S('lip + stick → lipstick','用于嘴唇的条状膏体 → 口红类别'),
 'red lipstick 红口红，put on lipstick 涂口红，a lipstick shade 口红色号。',
 'put on lipstick；a lipstick shade；red lipstick。',
 'lipstick 主要着色化妆品，lip balm 主要润唇类用品；具体产品可兼有功能，不能只靠两个词判断成分。',
 ('She put on lipstick before leaving.','出门前，她涂了口红。'),('The lipstick comes in several shades.','这款口红有几种色号。'))
W('chapstick','/ˈtʃæpstɪk/','条状润唇膏〔源自商标名〕',
 '嘴唇干裂，用膏体涂一层；英语有时用这个品牌名泛叫这种条状润唇膏。',
 '源自商标 ChapStick，chap 联系 chapped 干裂的 + stick 条状物。后来口语有泛用，但正式品牌名称仍常大写。',S('chap〔皮肤干裂相关〕+ stick → ChapStick → chapstick 泛用','商标形成 → 部分语境泛指条状润唇膏'),
 'a tube of chapstick 一管润唇膏，apply chapstick 涂润唇膏。通用类别名可用 lip balm。',
 'apply chapstick；a tube of chapstick；carry chapstick。',
 'chapstick 源自商标，lip balm 通用类别；chap 不指随便哪个伙计 chap，而接嘴唇干裂的用法。',
 ('He kept a tube of chapstick in his coat pocket.','他外套口袋里放着一管润唇膏。'),('She applied chapstick before going outside.','她出门前涂了润唇膏。'))
W('drumstick','/ˈdrʌmstɪk/','鼓槌；鸡、火鸡的小腿肉',
 '敲鼓用一头稍粗的棒；鸡小腿一头肉多、一端细，也借这种形状命名。',
 'drum 鼓 + stick 棒，先有鼓槌；禽类小腿用法后来按形状相似转用。不是吃鸡腿时一定拿来敲鼓。',S('drum + stick → drumstick','敲鼓的棒 → 禽类小腿形似鼓槌的名称'),
 'a pair of drumsticks 一对鼓槌，a chicken drumstick 鸡小腿，roasted drumsticks 烤鸡小腿。',
 'a pair of drumsticks；a chicken drumstick；roasted drumsticks。',
 'drumstick 鸡腿语境通常小腿那段，thigh 是大腿；菜单上的 chicken leg 有时范围更宽，不按中文一律同一块。',
 ('The drummer dropped one of his drumsticks.','鼓手掉了一根鼓槌。'),('The meal included two roasted chicken drumsticks.','这顿饭里有两只烤鸡小腿。'),sources=['https://www.etymonline.com/word/drumstick','https://en.wiktionary.org/wiki/drumstick#English'])
W('broomstick','/ˈbruːmstɪk/','扫帚柄；扫帚〔尤见巫婆骑的扫帚形象〕',
 '扫帚上供人握住的长杆；童话里骑着飞的那把扫帚，也常叫 broomstick。',
 'broom 扫帚 + stick 杆。部分使用从柄借指整件物品，是常见以部分称整体。',S('broom + stick → broomstick','扫帚长柄 → 部分场景借指整把扫帚'),
 'a wooden broomstick 木扫帚柄，ride a broomstick 骑扫帚〔童话〕。',
 'a wooden broomstick；ride a broomstick；a witch’s broomstick。',
 'broom 整把扫帚，broomstick 字面更着眼杆柄；故事里两者可都用于会飞的扫帚形象。',
 ('The old broomstick leaned against the wall.','旧扫帚柄靠在墙边。'),('In the story, the witch flies on a broomstick.','故事里，女巫骑着扫帚飞。'))
W('matchstick','/ˈmætʃstɪk/','火柴棍；细得像火柴棍的东西',
 '细细一根木杆，顶端带着火柴头；有时也借它形容特别细的腿、模型材料。',
 'match 火柴 + stick 小棒，前部不是比赛、匹配的同形 match。名称按火柴条棒结构组成。',S('match〔火柴〕+ stick → matchstick','火柴的细棍、火柴棍状物'),
 'a burnt matchstick 烧过的火柴棍，a matchstick model 火柴棍模型，matchstick legs 细腿〔可能带嘲讽〕。',
 'a burnt matchstick；a matchstick model；matchstick legs。',
 'matchstick 火柴棍，drumstick 鼓槌大小和用途不同；match 的比赛义不能套在这个词上。',
 ('A burnt matchstick lay beside the candle.','蜡烛旁放着一根烧过的火柴棍。'),('He built a small model from matchsticks.','他用火柴棍做了一个小模型。'))
W('dipstick','/ˈdɪpstɪk/','油尺、液面量杆；笨蛋〔英式口语贬称〕',
 '把细杆伸进液体，再看它沾到哪儿，就知道液面大致在哪；车辆里常指机油尺。',
 'dip 浸入 + stick 杆，按量测动作、外形命名。骂人笨蛋是另一路口语转用，不由工具结构直接证明人笨。',S('dip + stick → dipstick','浸入量测的杆；后有口语贬称'),
 'an oil dipstick 机油尺，read the dipstick 看量杆刻度；人物贬称语气不礼貌。',
 'an oil dipstick；read the dipstick；a dipstick reading。',
 'dipstick 量杆，sticker 贴纸；dip 的浸入与 stick 粘住不同，这里 stick 取杆名词。',
 ('The mechanic checked the oil level with the dipstick.','机械师用油尺检查机油液面。'),('The dipstick showed a clear mark.','量杆上显示出清楚的痕迹。'))
W('yardstick','英 /ˈjɑːdstɪk/；美 /ˈjɑːrdstɪk/','码尺；衡量标准',
 '先是一把一 yard 长的尺，再把它比作评判好坏、成败的参照。',
 'yard 长度单位码 + stick 杆。yard 这里不是房屋旁院子的那条来源、意义，现代名词又发展评价尺度的比喻。',S('yard〔码〕+ stick → yardstick','一码长的尺 → 衡量、评价标准'),
 'measure with a yardstick 用码尺量，a yardstick for success 衡量成功的标准。',
 'a yardstick for；a useful yardstick；measure against a yardstick。',
 'yardstick 强调参照尺度，goal 是想达到的目标；一个目标可以作评估标准，但两个词的角色不同。',
 ('The carpenter used a yardstick to measure the board.','木匠用码尺量了木板。'),('Exam results should not be the only yardstick for success.','考试成绩不应是衡量成功的唯一标准。'))
W('slapstick','/ˈslæpstɪk/','打闹、夸张肢体动作式喜剧；响板拍棍〔原义〕',
 '滑倒、追逐、夸张挨打这些身体动作逗人笑；名字最早来自能拍出响声的舞台棍具。',
 'slap 拍击 + stick 棍，原指两根相连、拍击会发出响声的舞台道具，后借指打闹式肢体喜剧。和意大利即兴喜剧道具名称有仿译背景。',S('slap + stick → slapstick','发响道具棍 → 夸张打闹式肢体喜剧'),
 'slapstick comedy 打闹喜剧，a slapstick scene 夸张肢体笑料场景。',
 'slapstick comedy；a slapstick scene；physical slapstick。',
 'slapstick 常靠身体动作笑料，wordplay 靠双关等语言技巧；作品可以两种都有，不能只把所有喜剧都叫 slapstick。',
 ('The film is full of slapstick comedy.','影片里满是夸张打闹式笑料。'),('The chase turns into a chaotic slapstick scene.','追逐变成了一段混乱的肢体喜剧场面。'),sources=['https://www.etymonline.com/word/slapstick','https://en.wiktionary.org/wiki/slapstick#English'])
W('nonstick','/ˌnɒnˈstɪk/〔英〕；/ˌnɑːnˈstɪk/〔美〕','不粘的〔尤指炊具表面〕',
 '食物不容易牢牢粘在表面上；名称抓住少粘这个效果，不是说锅完全没有任何摩擦。',
 'non- 非、不 + stick 粘住，形成常用炊具形容词。英式也常见带连字符拼写，本文用连写词头。',ST[1:]+[['non- + stick → nonstick','不易粘附；常指锅具表面特性']],
 'a nonstick pan 不粘锅，nonstick cookware 不粘炊具，a nonstick surface 不粘表面。',
 'a nonstick pan；nonstick cookware；a nonstick surface。',
 'nonstick 说不易粘，waterproof 防水，heatproof 耐热；这些是不同特性，不能只凭一种名称推断其他性能。',
 ('She cooked the eggs in a nonstick pan.','她用不粘锅做了鸡蛋。'),('The tray has a nonstick surface.','烤盘有不粘表面。'))
W('stickman','/ˈstɪkmæn/','简笔线条人、火柴人；特定岗位人员〔另有专门义〕',
 '头画一个圈，胳膊腿画几条细棒一样的线，就是常见火柴人形象。',
 'stick 细杆状线条 + man 人。另有赌场等岗位用法，此处先掌握绘画、动画、游戏里常见线条人物。',S('stick + man → stickman','用杆状线条表示的人；固定绘画称呼'),
 'draw a stickman 画火柴人，a stickman animation 火柴人动画；stick figure 也是常见同义表达。',
 'draw a stickman；a stickman animation；a simple stickman。',
 'stickman 火柴人画法，stuntman 特技替身演员不同；这里 man 表人物图像，不要求线条角色一定表现为男性。',
 ('The child drew a stickman beside the house.','孩子在房子旁画了个火柴人。'),('The animation uses a simple stickman to explain the movement.','动画用简单火柴人来解释动作。'))
R('B2990','条棒名词与刺、固定的旧动词；用途和粘附分组','STICK：细棒；另一支是扎住、固定，再到粘住和坚持','stick → sticky、sticker 接附着；条棒物按化妆、乐器、清扫、量测等用途分；slapstick 舞台道具到喜剧，nonstick 否定粘附。',
 '名词、动词都有旧英语路径，不编成现代木棍临时变粘贴。chapstick 商标背景、joystick 命名动机未全确定，保留原有共享精讲。',
 'stick—stuck—stuck；stick + -y/-er；lip/chap/drum/broom/match/dip/yard/slap/joy/candle + stick；non- + stick；stick + man。',
 [['基本词、附着和标签','stick · sticky · sticker · nonstick'],['外形、用品和操控','lipstick · chapstick · drumstick · broomstick · matchstick · joystick · candlestick'],['量测与比喻','dipstick · yardstick'],['舞台和线条人物','slapstick · stickman']],
 'stuck 过去分词；lipstick 口红、chapstick 源商标；drumstick 鼓槌或鸡小腿；yardstick 标准；slapstick 肢体喜剧。',
 'The sticker would not stick to the smooth nonstick surface.\n\n贴纸粘不住那块光滑的不粘表面。',
 'stick sticky sticker nonstick lipstick chapstick drumstick broomstick matchstick joystick candlestick dipstick yardstick slapstick stickman')
if __name__=='__main__':save('continuation_20261030_bu',ROOTS,WORDS)
