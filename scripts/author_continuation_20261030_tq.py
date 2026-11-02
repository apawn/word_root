"""Texture adjectives, useful colloquialisms, and whirlwind compounds."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'A1699':dict(words=['crunch','crunchy','shag','shaggy','tack','tacky','nifty'],label='脆、蓬乱、黏与俗：-y 的感觉和独立词史',note='crunch + -y → crunchy；shag + -y → shaggy。tacky 的黏性义联系 tack 的黏附材料，俗气义却有另一段较早词史；nifty 更远来源未定。'),
 'B3011':dict(words=['wind','whirl','whirlwind'],label='旋风与旋风般快速的经历',note='whirl 旋转 + wind 风 → whirlwind；这里 wind 读 /wɪnd/，取空气流动这一支。'),
 'A1776':dict(words=['shenanigans'],label='常用复数形态：shenanigans',note='shenanigans 常用复数形式表示胡闹、恶作剧或不正当花招，较早 shenanigan 的更远来源不确定，不为它硬配一套爱尔兰词根故事。'),
}
W('crunch','/krʌntʃ/','嘎吱、咔嚓声；咬碎、压碎；大量处理数字',
 '牙齿咬碎硬脆食物，或脚踩碎薄冰、积雪，都会有 crunch 那种清脆挤碎声。crunch numbers 则形容把一堆数字拿来计算处理。',
 '接较早 craunch、cranch 等拟声性形式。由带声响的压碎、咬碎，扩展到处理数字以及局面吃紧等比喻。',
 [['较早拟声形式 → crunch','咬、压得咔嚓响；相应声响'],['现代口语、比喻发展','crunch numbers 处理数字；the crunch 吃紧、关键时刻']],
 'crunch an apple 嘎吱咬苹果；snow crunches underfoot 雪在脚下嘎吱作响；crunch the numbers 做大量数字计算。',
 'a loud crunch；a program that crunches numbers。','crush 泛指压碎、压坏；crunch 常还带清脆破碎的声响。crunch numbers 是处理数字的比喻，不限定只做一种算术。',
 ('The snow crunched under our boots.','雪在我们的靴子底下嘎吱作响。'),('The program can crunch thousands of numbers in seconds.','这个程序几秒钟就能处理数千个数字。'))
W('crunchy','/ˈkrʌntʃi/','松脆的、咬起来嘎吱响的',
 '咬下去有明显的脆响，能感觉到食物碎开。胡萝卜、坚果、炸脆的外层都可以 crunchy。',
 'crunch 咔嚓咬碎、发出脆响 + -y，形成具有这种声响和口感的形容词。',
 [['crunch 的声响、咬碎动作 + -y','带有相应性质'],['crunchy 的食物口感','咬起来有明显脆响、碎裂感的']],
 'crunchy carrots 脆胡萝卜；crunchy nuts 脆坚果；a crunchy topping 松脆的表层配料。',
 'a crunchy texture；crunchy cereal。','crispy 也说脆，常强调薄、轻、外层干脆；crunchy 常强调咬碎时明显的声响和实在的脆感，两者可有交集。',
 ('The carrots were fresh and crunchy.','胡萝卜新鲜爽脆。'),('She sprinkled crunchy nuts over the salad.','她在沙拉上撒了些脆坚果。'))
W('shag','/ʃæɡ/','粗长毛、长绒；长绒地毯等〔本条主要义〕',
 '一层长长、蓬蓬、甚至有点乱的毛。家居里的 shag rug 常指这种长绒地毯。',
 '毛、长绒这一支可能承接古英语 sceacga 等粗毛材料，传承细节有缺环；后来用于长绒织物、地毯。另有不同历史的同形动词。',
 [['较早粗毛材料 → 英语 shag 的毛、织物支','粗长毛、带绒织物'],['现代家居等用法','长绒、长绒地毯等']],
 'a shag carpet 长绒地毯；a shag rug 长绒小地毯；a shag of hair 一团蓬乱长发。',
 'deep shag pile；a white shag rug。','英式口语 shag 另有粗俗的性交义，通常另追动作词来源。学习 shaggy 时取的是粗毛、长绒这一支。',
 ('A thick shag rug covered the floor.','地上铺着一张厚厚的长绒地毯。'),('The room still had its old shag carpet.','房间里还铺着那张旧长绒地毯。'),sources=['https://www.etymonline.com/word/shag','https://en.wiktionary.org/wiki/shag#English'])
W('shaggy','/ˈʃæɡi/','毛发蓬长的、乱蓬蓬的；长绒的',
 '头发、狗毛长得蓬松不齐，边缘没有整齐收住，就是 shaggy 的画面。',
 'shag 粗长毛 + -y，短元音后双写 g。由毛发的蓬长扩展到织物等有相似外观的东西。',
 [['shag 粗长毛 + -y','覆盖着、具有长粗毛的'],['shaggy 的毛发和织物描述','蓬长、蓬乱、长绒的']],
 'shaggy hair 蓬乱长发；a shaggy dog 毛蓬长的狗；a shaggy coat 一身长毛，也可指长绒外套。',
 'a shaggy beard；a shaggy rug。','curly 说卷曲，shaggy 说长而蓬乱，卷发或直发都可能显得 shaggy。shaggy 本身不直接表示脏。',
 ('A shaggy dog followed them home.','一只毛发蓬长的狗跟着他们回了家。'),('His shaggy hair fell over his eyes.','他的蓬乱长发垂下来遮住了眼睛。'))
W('tack','/tæk/','小钉；钉住、附加；航向、做法；马具〔另支〕',
 '小钉把纸钉住，是具体的 tack；tack on a fee 是额外附加一笔费用。change tack 则借航海转向，说改换做法。',
 '小钉义经古北法语 taque 等借入；固定帆角等航海用法又发展成航向、行动方针。马具义则缩自 tackle 装备这一词。',
 [['法语钉、尖物材料 → 英语 tack','小钉；暂时固定、附加；航海固定帆角等'],['各支后续发展','航向 → 做法；tackle 缩短的马具义另记']],
 'a drawing tack 图钉；tack a note to the wall 把便条钉到墙上；tack on an extra charge 额外收费；try a different tack 换一种办法；a tack room 马具间。',
 'change tack；tack something onto a list。','change tack 是改换航向、做法；这里是 tack，不是 track 轨道。马具 tack 与小钉义也有不同的直接来源。',
 ('She tacked the note to the noticeboard.','她把便条钉在了公告栏上。'),('The first approach failed, so we tried a different tack.','第一种方法没奏效，我们就换了一种做法。'),('The stable has a separate room for tack.','马厩有一间单独存放马具的房间。'),sources=['https://www.etymonline.com/word/tack','https://en.wiktionary.org/wiki/tack#English'])
W('tacky','/ˈtæki/','黏手的、表面有黏性的；俗气的、品位差的〔另一支〕',
 '涂层还没干，摸着有点黏，是一支；装饰显得廉价、俗艳，是另一支。两种常用意思要分开追历史。',
 '黏性义联系 tack 的附着材料与 -y；俗气义接较早 tackey、tackie 劣马、寒酸者等旧用法，更远来源未定，后来用于审美评价。',
 [['tack 的附着材料 + -y','有黏性、黏手的'],['较早 tackey、tackie 等 → tacky 评价义','寒酸、劣质 → 俗气、品位差']],
 'tacky paint 仍有黏性的漆面；a tacky surface 黏手表面；tacky decorations 俗气装饰；a tacky joke 不得体的笑话。',
 'slightly tacky to the touch；a tacky souvenir。','sticky、tacky 可在黏性上相近；tacky 的俗气义却不能简单编成黏手所以俗气。这两支有不同词史。',
 ('The paint was still tacky the next morning.','第二天早晨，漆面摸着仍有些黏。'),('She thought the glittering decorations looked tacky.','她觉得那些亮闪闪的装饰显得很俗气。'),sources=['https://www.etymonline.com/word/tacky','https://en.wiktionary.org/wiki/tacky#English'])
W('nifty','/ˈnɪfti/','精巧好用的、很棒的〔口语〕',
 '一个小设计正好解决麻烦，轻巧、方便，让人觉得“这招真不错”，就常用 nifty 来夸。',
 '十九世纪美式口语已有，较早形容漂亮、时髦，更远来源未定；有缩略变化等不同猜测。现代常用于称赞精巧、实用的工具或做法。',
 [['十九世纪美式口语 nifty','漂亮、时髦、出色的'],['现代常用的轻松赞语','精巧、方便、好用、很不错的']],
 'a nifty gadget 精巧实用的小工具；a nifty trick 一个妙招；a nifty little feature 一个挺好用的小功能。',
 'a nifty solution；a nifty piece of design。','nifty 是轻松的称赞，不需要对象昂贵、宏大。它的更早形成未定，不宜按一个现代常用 nift 名词来硬拆。',
 ('This app has a nifty search feature.','这个应用有个挺好用的搜索功能。'),('She showed me a nifty trick for folding the map.','她教了我一个折地图的妙招。'),sources=['https://www.etymonline.com/word/nifty','https://en.wiktionary.org/wiki/nifty#English'])
W('whirlwind','英 /ˈwɜːlwɪnd/；美 /ˈwɜːrlwɪnd/','旋风；旋风般迅速、紧凑的一连串经历',
 '风旋着卷起来；比喻时，一连串事情来得又快又密，让人像被卷着往前走。',
 'whirl 旋转 + wind 风，中古英语已有相应复合词。由旋转风流的具体画面，扩展为快速、密集、令人应接不暇的活动。',
 [['whirl + wind → 中古英语相关复合词','旋转着的风'],['whirlwind 的现代比喻','旋风般迅速的经历、过程']],
 'a whirlwind tour 紧凑快速的游览、访问；a whirlwind romance 迅速发展的恋情；a whirlwind of activity 一连串忙乱活动。',
 'a whirlwind visit；caught in a whirlwind of events。','whirlwind 不等于所有 tornado 龙卷风的精确气象分类。日常比喻通常抓速度、密集感，而不需要真实风暴。',
 ('A whirlwind lifted dust from the dry field.','一阵旋风卷起了干地上的尘土。'),('They made a whirlwind tour of three cities.','他们匆匆游览了三座城市。'))
W('shenanigans','英 /ʃɪˈnænɪɡənz/；美 /ʃəˈnænɪɡənz/','胡闹、恶作剧；诡计、不正当的小动作〔常用复数〕',
 '可以是朋友调皮胡闹，也可能是在说账目、交易背后的鬼把戏。语气轻重取决于对象。',
 '较早美式英语 shenanigan 指花招、胡扯等，来源未定；现代常以加 -s 的复数形态 shenanigans 使用。',
 [['较早 shenanigan 的俚语使用','胡扯、欺骗、花招'],['现代常用复数 shenanigans','调皮胡闹；可疑、不正当的小动作']],
 'schoolboy shenanigans 学生式胡闹；financial shenanigans 财务上的鬼把戏；no more shenanigans 别再胡闹。',
 'political shenanigans；join in the shenanigans。','shenanigans 既能轻松说笑，也能指较严重的欺骗，不能只背恶作剧一种语气。通常保留词尾 -s，不随意改成单数来用。',
 ('The teacher had had enough of their shenanigans.','老师受够了他们的胡闹。'),('The report exposed financial shenanigans at the company.','报告揭露了公司财务上的不正当小动作。'),sources=['https://www.etymonline.com/word/shenanigan','https://en.wiktionary.org/wiki/shenanigans#English'])
def extend_lessons():
    extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
    save('continuation_20261030_tq',ROOTS,WORDS)
    extend_lessons()
