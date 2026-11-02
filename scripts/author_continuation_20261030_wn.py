"""Mind, appearance, space and openings in common plural forms."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'B2612':dict(words=['mind','minds'],label='mind → minds：想法、心智；介意、照看',note='mind 接古英语 mynd／ġemynd 记忆、思想词族；minds 既可作复数，也可作动词第三人称。'),
 'B3023':dict(words=['brain','brains'],label='brain → brains：大脑与头脑、智力',note='brain 接古英语 bræġn／brægen 等；brains 可泛说智力，也可在 the brains behind 中说策划者。'),
 'B3347':dict(words=['skin','skins'],label='skin → skins：皮肤、外皮与外观主题',note='skin 接古诺尔斯语 skinn，后来通用于人的皮肤；外层、界面外观等义沿表层画面扩展。'),
 'B2764':dict(words=['hair','hairs'],label='hair → hairs：一头毛发与一根根毛发',note='hair 接古英语 hǣr；毛发整体常不可数，hairs 数一根根头发、毛。'),
 'C1654':dict(words=['voice','voices'],label='voice → voices：声音、发言权与说出来',note='voice 经法语接拉丁 vox／vocem；voices 在 /s/ 后加 /ɪz/，也可作表达意见的动词形式。'),
 'B2701':dict(words=['room','rooms'],label='room → rooms：空间与一间间房',note='room 继承古英语 rūm 空间、余地，房间义在这条历史中发展；rooms 用于数房间等。'),
 'B3040':dict(words=['door','doors'],label='door → doors：门；机会的入口',note='door 继承古英语 duru、dor 等，doors 常数门，也在 open doors 等搭配中比喻机会。'),
 'B2752':dict(words=['eye','window','windows'],label='window → windows：风之眼到窗户、界面窗口',note='window 借古诺尔斯语 vindauga，历史 vindr 风加 auga 眼；现代 windows 是英语词加复数，不是词干 wind 加新造 ow。'),
}
W('minds','/maɪndz/','心智、想法〔复数〕；介意、留意、照看〔mind 的第三人称单数〕',
 '人的思想、判断在 mind 里形成；minds 可以说多个人的头脑或看法。作动词时，可以是把注意力放在某事上，进而说介意或照看。',
 'mind + -s，/d/ 后读 /z/。mind 接古英语 mynd、gemynd 的记忆、思想词族，经中古英语 minde 等延续。',
 [['古英语 mynd／ġemynd → mind','记忆、思想；后来有注意、介意等动词义'],['mind 名词、动词 + -s → minds','多人的心智、看法；单数主语介意、照看']],
 'change their minds 改变主意；make up their minds 作出决定；open minds 开放的头脑；minds the shop 照看店铺；never minds helping 从不介意帮忙。',
 'in people’s minds；minds her own business。','minds 在 Their minds changed 中是名词，在 He never minds waiting 中是动词。mind doing 常说介意做某事，own business 搭配则是管好自己的事。',
 ('We changed our minds after seeing the room.','看过房间后，我们改变了主意。'),('He never minds answering a few extra questions.','他从不介意多回答几个问题。'),sources=['https://en.wiktionary.org/wiki/minds#English','https://en.wiktionary.org/wiki/mind#English'])
W('brains','/breɪnz/','大脑〔复数〕；头脑、智力；策划者、智囊〔the brains behind〕',
 '器官 brain 负责思考，brains 又可以直接说思考能力。the brains behind 某事，则把做主要构思的人叫作背后的头脑。',
 'brain + -s，/n/ 后读 /z/。brain 继承古英语 bræġn、brægen 等，更远来源有争议；智力、策划者等义由思考器官的名称发展。',
 [['古英语 bræġn／brægen → brain','脑；与思考能力相连的引申'],['brain + -s → brains','多个脑；智力；主要构思者']],
 'use your brains 动动脑筋；brains and patience 头脑与耐心；the brains behind the project 项目的主要策划者；pick someone’s brains 向某人请教、取经。',
 'a task that needs brains；the brains behind the design。','brains 表智力时，不是在说一个人长着几个脑。the brains behind 可以指一个人，也可按语境说一群策划者，人数由其他信息决定。',
 ('This puzzle needs patience as well as brains.','这道谜题既需要头脑，也需要耐心。'),('She is the brains behind the new exhibition.','她是这次新展览的主要策划者。'),sources=['https://en.wiktionary.org/wiki/brains#English','https://en.wiktionary.org/wiki/brain#English'])
W('skins','/skɪnz/','皮、外皮〔复数〕；界面外观、皮肤主题；去皮〔动词形式〕',
 '包在外面的那一层，是 skin 的核心画面：动物皮、果皮、某些食物的表皮，以及软件能换的外观，都可以沿这层外皮理解。',
 'skin + -s，/n/ 后读 /z/。skin 接古诺尔斯语 skinn，早期动物皮用法很重要，后来通用于皮肤、外层；动词去皮等由名词发展。',
 [['古诺尔斯语 skinn → skin','皮、毛皮 → 人的皮肤及其他外层'],['skin 名词、动词 + -s → skins','多张皮、多个外皮、外观主题；单数主语去皮']],
 'potato skins 土豆皮；animal skins 动物皮；thin skins 薄皮〔也可能比喻敏感〕；game skins 游戏外观、皮肤；skins the tomatoes 给番茄去皮。',
 'fruit skins；different interface skins。','skin 表一个人身体的皮肤时常不可数，skins 可数一张张皮、不同外皮或外观主题。软件 skins 通常改变外观，是否也改功能要看具体产品。',
 ('Leave the potato skins on for this recipe.','做这道菜时，土豆皮留着。'),('The app offers several skins for its main screen.','这个应用给主界面提供了几种外观主题。'),sources=['https://en.wiktionary.org/wiki/skins#English','https://en.wiktionary.org/wiki/skin#English'])
W('hairs','英 /heəz/；美 /herz/','一根根头发、毛发；hair 的可数复数',
 '把一头头发看成整体，常用 hair；盯住单独几根来数，就用 hairs。白头发、衣服上粘的毛，都可以一根根指出来。',
 'hair + -s，词尾读 /z/。hair 继承古英语 hǣr，现代同时保留整体毛发的不可数用法和单根毛发的可数用法。',
 [['古英语 hǣr → hair','毛发；现代可指整体，也可指一根'],['hair + -s → hairs','可数的一根根毛发']],
 'grey hairs 白发；a few hairs 几根毛；cat hairs 猫毛〔数根、散落毛发时〕；split hairs 过分计较细微区别；the hairs on the back of your neck 脖颈后的寒毛。',
 'three hairs；hairs on a jacket。','Her hair is long 说她的头发长，hair 作整体通常不可数；There are three hairs on the chair 数椅子上的三根毛。不能把两种场景都机械换成 hairs。',
 ('I found a few cat hairs on my jacket.','我在外套上发现了几根猫毛。'),('He noticed two grey hairs near his forehead.','他注意到额前有两根白发。'),sources=['https://en.wiktionary.org/wiki/hairs#English','https://en.wiktionary.org/wiki/hair#English'])
W('voices','/ˈvɔɪsɪz/','嗓音、说话声；意见、发言者；表达、说出〔voice 的第三人称单数〕',
 '人的声音把想法带出来，所以 voices 既能说听见的说话声，也能说表达意见的人。作动词时，就是把关切、想法说出口。',
 'voice 已有 e，加 s，/s/ 后增加 /ɪz/。经法语 voiz／vois 接拉丁 vox 的 vocem 形式；动词 voice 由英语名词转用。',
 [['拉丁 vox／vocem → 法语 voiz／vois → voice','嗓音、声音 → 意见、发言权等'],['voice 名词、动词 + -s → voices','多个声音、意见；单数主语表达']],
 'familiar voices 熟悉的声音；raise their voices 提高嗓门；different voices 不同声音、意见；voices concern 表示担忧；voices support 表达支持。',
 'voices in the corridor；voices an opinion。','voices 通常把注意力放在人的发声、意见上，sounds 范围更广，也包括铃声、车声等。She voices her concern 中 voices 是表达的动词。',
 ('We heard familiar voices in the corridor.','我们在走廊里听到了熟悉的声音。'),('She voices her concerns calmly and clearly.','她平静而清楚地表达自己的担忧。'),sources=['https://en.wiktionary.org/wiki/voices#English','https://en.wiktionary.org/wiki/voice#English'])
W('rooms','/ruːmz/，也有 /rʊmz/','房间〔复数〕；住所、套间〔部分语境〕；合住〔动词形式〕',
 'room 原有空间、余地的画面，后来也说划出的一间房。rooms 能数卧室、会议室等，某些住处语境还可说一套房间。',
 'room + -s，/m/ 后读 /z/。room 继承古英语 rūm、中古英语 roum，较早有空间、余地义；房间和居住动词等用法后来发展。',
 [['古英语 rūm → 中古英语 roum → room','空间、余地 → 房间'],['room 名词、动词 + -s → rooms','多间房；单数主语合住等']],
 'hotel rooms 酒店客房；meeting rooms 会议室；rooms to rent 待租房间；rooms with a friend 和朋友合住〔动词，尤见美式〕。',
 'two empty rooms；rooms on the first floor。','There is room for two more people 说还能容纳两个人，room 常不可数；There are two rooms 说有两间房。空间和房间的场景决定是否加复数。',
 ('The hotel has two meeting rooms on the ground floor.','酒店一楼有两间会议室。'),('The rooms at the back of the house are quieter.','房子后面的房间更安静。'),sources=['https://en.wiktionary.org/wiki/rooms#English','https://en.wiktionary.org/wiki/room#English'])
W('doors','英 /dɔːz/；美 /dɔːrz/','门；门口、入口；机会的通道等；door 的复数',
 '一扇扇门把外面和里面接起来。机会也常被看作可以走进去的一扇门，所以 doors 既能指实物，也能出现在机会的比喻里。',
 'door + -s，词尾 /z/。door 继承古英语 duru、dor 等古老门词，现代复数按 -s 形成。',
 [['古英语 duru／dor → door','门、入口'],['door + -s → doors','多扇门；机会入口等比喻']],
 'front doors 前门；automatic doors 自动门；behind closed doors 私下、闭门进行；open doors for someone 为某人打开机会；close its doors 停止营业。',
 'the doors of the hall；opens new doors。','behind closed doors 可能是门关着的实际位置，也常说不公开的讨论。close its doors 在店铺语境可能是歇业，不能只按关上门板理解。',
 ('The train doors opened on the left.','列车左侧的门打开了。'),('Learning another language can open new doors.','多学一门语言能带来新的机会。'),sources=['https://en.wiktionary.org/wiki/doors#English','https://en.wiktionary.org/wiki/door#English'])
W('windows','英 /ˈwɪndəʊz/；美 /ˈwɪndoʊz/','窗户；计算机窗口；时间窗口、机会时段；window 的复数',
 '墙上留一个口，让光和空气进来，是 window；屏幕里开出一块内容区域也叫窗口；时间上短暂开放的机会，又叫时间窗口。',
 'window + -s，元音后读 /z/。window 借古诺尔斯语 vindauga，历史 vindr 风 + auga 眼，像让风进来的眼睛；现代英语借入整词后再按规则变复数。',
 [['古诺尔斯语 vindr + auga → vindauga → 英语 window','风之眼 → 窗户'],['window + -s → windows','多扇窗；多个界面窗口、可用时段']],
 'open the windows 开窗；browser windows 浏览器窗口；delivery windows 可配送时段；windows of opportunity 有利机会、机会时段。',
 'two open windows；short windows of time。','windows 小写时是普通复数；Windows 大写还可能是软件专有名称。浏览器的 tabs 标签页与 windows 窗口有区别，一个窗口里可以有多个标签页。',
 ('Open the windows for a few minutes to let some air in.','把窗户开几分钟，透透气。'),('I accidentally opened the same page in two windows.','我不小心在两个窗口里打开了同一个页面。'),('The courier offers two delivery windows tomorrow.','快递公司明天提供两个可配送时段。'),sources=['https://en.wiktionary.org/wiki/windows#English','https://en.wiktionary.org/wiki/window#English'])
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_wn',ROOTS,WORDS)
 extend_lessons()
