"""Kidneys, thighs, plucking and ladders: common nouns and actions."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'A1776':dict(words=['kidney','kidneys','thigh','thighs','ladder','ladders'],label='常用部位与物品的单复数：kidney、thigh、ladder',note='这些词来源不同，本组按复数 s 的作用学习；thighs 保留开头 /θ/，复数结尾读 /z/。'),
 'A1760':dict(words=['pluck','plucked'],label='pluck → plucked：摘取、拔下与拨弦',note='pluck 末尾 ck 后直接加 ed，读 t；不把与拉丁拔毛词的有争议联系写成确定借入路线。'),
 'C0238':dict(words=['ladder','ladders'],label='远层同源比较：ladder 是靠着供攀登的梯子',note='ladder 接古英语 hlæder，更远通常重建到倾斜、靠的词族，与 clinare 的联系是远层比较；现代词形末尾 der 不是表示人的 er 后缀。'),
}
W('kidney','/ˈkɪdni/','肾、肾脏',
 '它是身体里帮助从血液去除代谢废物和多余水分的器官。外形像常说的腰豆，所以 kidney bean 借用了它的形状。',
 '中古英语已有 kidenere 等形式，更早来源不确定。有人提出与旧身体、蛋形词有关的复合解释，但证据不足，现代不要硬拆成 kid 小孩 + ney。',
 [['中古英语 kidenere 等 → kidney','肾脏名称；更早来源未定'],['kidney 的形状用于命名','kidney bean 按肾形命名的豆']],
 'a kidney 一个肾；kidney function 肾功能；kidney tissue 肾组织；a kidney bean 一粒腰豆。复数 kidneys。',
 'the left kidney；a model of a kidney。','kidney 是日常器官名称，renal 是医学中常见的肾的，来源接拉丁 ren；两个词表达有关概念，但不能把 renal 当作 kidney 直接换词尾。',
 ('The model shows a kidney and the blood vessels connected to it.','模型展示了一个肾脏及与它相连的血管。'),('The teacher explained the shape of a kidney.','老师讲解了肾脏的形状。'),sources=['https://www.etymonline.com/word/kidney','https://www.cancer.gov/publications/dictionaries/cancer-terms/def/kidney','https://en.wiktionary.org/wiki/kidney#English'])
W('kidneys','/ˈkɪdniz/','肾脏〔复数〕；食用腰子〔食物语境〕',
 '通常成对谈人体的肾时，用 kidneys。餐馆菜单里也可能是动物肾脏做成的食材，要按语境判断。',
 'kidney 末尾是元音字母 e + y，复数直接加 s，写 kidneys，结尾读 /z/。不套用 cherry → cherries 的辅音字母加 y 规则。',
 [['kidney','中古英语延续下来的肾脏名'],['kidney + -s → kidneys','多个肾脏；也可说相应食材']],
 'the kidneys 双肾、肾脏；both kidneys 两个肾；lamb kidneys 羊腰子；the role of the kidneys 肾脏的作用。',
 'a diagram of the kidneys；kidneys in a textbook。','kidneys 是器官或食材；kidney beans 是豆，通常前面的 kidney 作单数修饰语。不要把 kidneys 和 kidney beans 混成一种食物。',
 ('The diagram shows the position of the kidneys.','示意图显示了肾脏的位置。'),('The menu listed lamb kidneys as a starter.','菜单把羊腰子列为一道前菜。'),sources=['https://www.etymonline.com/word/kidney','https://en.wiktionary.org/wiki/kidneys#English'])
W('thigh','/θaɪ/','大腿；禽类等的大腿肉',
 '膝盖到髋部之间的上段腿，叫 thigh。鸡腿肉里的大腿部分也沿用这个名称。',
 '接古英语 þeoh、þeh，经中古英语 thigh 延续。更远有把它解释为较粗、饱满腿部的词源分析，但不是现代英语 thick 直接删掉词尾。gh 在常见现代读音中不发音。',
 [['古英语 þeoh、þeh → thigh','腿的上部；更早重建有不同分析'],['现代 thigh','人的大腿；动物、禽类相应部位和肉']],
 'the upper thigh 大腿上部；thigh muscles 大腿肌肉；a chicken thigh 一块鸡大腿；rest a hand on your thigh 把手放在大腿上。',
 'the back of the thigh；a thigh pocket。','leg 日常可说整条腿，thigh 明确是膝盖以上的上段。小腿不是 thigh；复数 thighs 保留开头 /θ/，结尾读 /z/。',
 ('She rested the notebook on her thigh.','她把笔记本搁在大腿上。'),('We cooked chicken thighs with onions and herbs.','我们用洋葱和香草烹调了鸡大腿肉。'),sources=['https://www.etymonline.com/word/thigh','https://en.wiktionary.org/wiki/thigh#English'])
W('thighs','/θaɪz/','大腿〔复数〕；禽类大腿肉〔复数〕',
 '说双侧大腿，或一盘里几块鸡大腿肉，常用 thighs。开头仍是 thigh 的 /θ/，词尾加 /z/。',
 'thigh + 复数 -s → thighs；gh 仍不发音，整个词一个音节。不要因为某些 th 结尾词有单复数变音，就让这个词的开头也跟着变音。',
 [['古英语腿上部名称 → thigh','大腿'],['thigh + -s → thighs','多个大腿、相应肉块；读 /θaɪz/']],
 'strong thighs 结实的大腿；inner thighs 大腿内侧；chicken thighs 鸡大腿肉；rest your hands on your thighs 把手放在大腿上。',
 'the backs of the thighs；roasted chicken thighs。','句中 thighs 可能是人的身体部位，也可能是食材。复数拼写保留 gh，发音仍无 /ɡ/ 或 /h/。',
 ('She rested her hands on her thighs.','她把双手放在大腿上。'),('The recipe calls for four chicken thighs.','这份食谱需要四块鸡大腿肉。'),sources=['https://en.wiktionary.org/wiki/thighs#English','https://yabancidiller.medeniyet.edu.tr/documents/yabancidiller/2021-2022%20AKADEM%C4%B0K%20YIL/%C3%96%C4%9Frenci%20Sekmesi/Kelime%20Listesi/efuppintwordlistb2.pdf'])
W('pluck','/plʌk/','摘下、拔下；拨〔弦〕；鼓起〔勇气〕；胆量、勇气〔名词〕',
 '抓住一个小东西，往外一拉：羽毛拔下来了，果实摘下来了。手指轻拉琴弦再放开，也叫 pluck。',
 '承接古英语 pluccian、ploccian 与中古英语 plukken 拔取。更远与拉丁拔毛词相连的解释存在历史证据问题，保留争议；英语后来又有拨弦和鼓起勇气的表达。',
 [['古英语拔取词 → 中古、现代 pluck','从表面、整体上拉出或摘下'],['动作的不同延伸','拨弦；pluck up courage 鼓起勇气；名词也说胆量']],
 'pluck a flower 摘花；pluck feathers 拔羽毛；pluck a guitar string 拨吉他弦；pluck up the courage 鼓起勇气；show pluck 表现勇气。',
 'pluck something from ...；pluck up courage to ask。','pluck 常突出一次拉、摘的小动作；pick 范围更广。名词 pluck 的勇气义有旧内脏、心胆比喻等发展，不只靠现代字面拉一下解释全部历史。',
 ('She plucked a leaf from the branch.','她从枝上摘下一片叶子。'),('He finally plucked up the courage to ask a question.','他终于鼓起勇气，问了一个问题。'),sources=['https://www.etymonline.com/word/pluck','https://en.wiktionary.org/wiki/pluck#English'])
W('plucked','/plʌkt/','摘下了、拔下了；拨动了；pluck 的过去式、过去分词',
 '花已经从枝上摘下，琴弦也已被手指拨响。plucked 把 pluck 的小幅拉取动作放到过去或完成的状态中。',
 'pluck 词尾 ck 保留，直接加 -ed；/k/ 后读 /t/，不增加音节。继承古英语拔取词的不同现代用法。',
 [['pluck','摘下、拔取；拨弦'],['pluck + -ed → plucked','过去做了这些动作；处于相应完成状态']],
 'freshly plucked flowers 刚摘的花；plucked strings 拨弦；plucked a feather 拔下一根羽毛；plucked up courage 鼓起了勇气。',
 'a plucked instrument；plucked from the tree。','plucked strings 指用拨动方式发声的弦或声部；bowed strings 则用弓拉。英语过去式的 ed 在这里读 /t/。',
 ('She plucked the strings gently with her fingers.','她用手指轻轻拨动琴弦。'),('He carried a handful of freshly plucked flowers.','他拿着一把刚摘下来的花。'),sources=['https://www.etymonline.com/word/pluck','https://en.wiktionary.org/wiki/plucked#English'])
W('ladder','英 /ˈlædə/；美 /ˈlædər/','梯子；晋升、等级的阶梯；丝袜抽丝〔英式〕',
 '两根长边中间横着一根根档，人能一级级往上爬，是 ladder。工作职位从低到高，也容易借成一架阶梯。',
 '来自古英语 hlæder，经中古英语 laddere 延续，更远通常联系倾斜、靠的词族。职业等级的比喻较早就出现；丝袜一串脱线像梯档，也可叫 ladder。',
 [['古英语 hlæder → ladder','供攀爬的梯子、梯级'],['梯档的不同比喻','晋升阶梯；丝袜脱线形成的梯形纹路']],
 'climb a ladder 爬梯子；a rope ladder 绳梯；the career ladder 职业晋升阶梯；a ladder in a stocking 丝袜的一道抽丝。',
 'at the top of the ladder；move up the ladder。','stairs 是楼梯的一段段固定踏步，ladder 常为带横档、靠立或悬挂的攀爬工具。单词末尾 der 是历史词形的一部分，不能按做某事的人来拆。',
 ('A wooden ladder leaned against the wall.','一架木梯靠在墙上。'),('She moved steadily up the career ladder.','她在职业道路上稳步晋升。'),sources=['https://www.etymonline.com/word/ladder','https://en.wiktionary.org/wiki/ladder#English'])
W('ladders','英 /ˈlædəz/；美 /ˈlædərz/','梯子〔复数〕；抽丝的梯形痕迹〔英式〕',
 '工具间有几架梯子，就用 ladders。英国英语里，袜子上不止一道像梯档的抽丝纹，也可这样说。',
 'ladder + -s，词尾读 /z/。保留古英语梯子的名称及现代按形状形成的比喻；现代也可能是动词第三人称单数，要看句法。',
 [['ladder','梯子；等级阶梯；抽丝纹路'],['ladder + -s → ladders','多个梯子、相应纹路等']],
 'wooden ladders 木梯；rope ladders 绳梯；a set of ladders 一套、几架梯子〔依语境〕；ladders in tights 连裤袜的抽丝痕迹。',
 'store the ladders；different career ladders。','one ladder 是一架，two ladders 是两架。a ladder in tights 的抽丝义英式常见，美式常用 a run，来自脱线后形似梯档的纹路。',
 ('The workers stored the ladders in the shed.','工人们把梯子收在工具棚里。'),('The course describes several different career ladders.','这门课介绍了几种不同的职业晋升路径。'),sources=['https://www.etymonline.com/word/ladder','https://en.wiktionary.org/wiki/ladders#English'])
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_vq',ROOTS,WORDS)
 extend_lessons()
