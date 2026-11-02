"""Benches, gray tones and strings: objects becoming roles and abstractions."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
B=[['古英语 benċ → 中古英语 bench/benk','长凳、长座位'],['英语 bench 扩展','坐在那里的人、职位；工作台、运动替补席']]
W('bench','/bentʃ/','长凳；工作台；法官席、法官群体；替补席；让球员坐替补',
 '先是一条能坐几个人的长凳；法官坐的那边可以代表法官群体，球员没上场坐的那边就成了替补席。',
 '接古英语 benċ，同日耳曼语长凳词族。由座位转指坐在那里的人、身份，是意思扩展；健身里的 bench 动词还可缩短自 bench press 卧推。',B,
 'a park bench 公园长凳，the bench and bar 法官与律师群体，on the bench 坐替补或任法官，要看场景；bench a player 让球员坐替补。',
 'a park bench；a work bench；on the bench；bench a player。',
 'bench 不是一概板凳：a strong bench 说球队替补力量强；被 benched 未必遭开除，只是暂不上场或不担任原任务。',
 ('We sat on a bench beside the lake.','我们坐在湖边的一条长凳上。'),('The coach benched him for the first half.','教练上半场让他坐了替补。'))
W('backbench','/ˈbækbentʃ/','后排座位；议会后座、后座议员方面的',
 '议场前排坐主要发言和领导角色，后排的普通议员席便叫 backbench；距离前排的空间，变成政治角色的说法。',
 'back 后面 + bench 长凳。议会义由实际座位安排扩展，也可作定语说后座议员的意见；具体资格随议会制度而定。',B+[['back + bench → backbench','后排座位 → 议会后座、相关议员的']],
 'backbench MPs 后座议员，backbench support 后座议员支持，the backbenches 议会后座群体；普通房间也可有字面后排凳。',
 'backbench MPs；backbench support；on the backbenches。',
 'backbench 不等于反对党：执政党也有后座议员；frontbench 也不只属于执政方。后座是职位角色，不能直接译成无能的议员。',
 ('Several backbench MPs questioned the proposal.','几名后座议员对提案提出质疑。'),('The minister faced criticism from the backbenches.','那位大臣受到后座议员的批评。'))
R('B2563','长座位，转指工作、司法和议会角色','BENCH：从一条长凳，看坐在那里或在那里做事的人','bench → backbench；workbench 是工作台；benchmark 从标记、基准扩展为比较尺度。',
 '长凳是入口，后面的身份含义来自谁坐在那里。换成工作台时，重点又成了在台面上做事；基准含义要放回 benchmark 的专门历史理解。',
 'benċ → bench；back/work + bench；benchmark 的测量基准背景。',
 [['座位与角色','bench · backbench'],['工作面与比较尺度','workbench · benchmark']],
 'on the bench 可说法官或替补；backbench 不是反对党专名；benchmark 不能只死译成凳子上的记号。',
 'The coach praised the bench while the backbench MPs debated elsewhere.\n\n教练夸着替补阵容，另一边的后座议员则在辩论。',
 'bench backbench workbench benchmark')
G=[['古英语 grǣġ/grēġ → gray/grey','灰色，古老的方言形式延续出拼写变体'],['英语颜色的比喻','灰暗、头发变灰；界线不清的中间地带']]
W('gray','/ɡreɪ/','灰色的、灰色；灰暗的；界线不清的；变灰；戈瑞〔另源单位〕',
 '黑和白之间有一大片灰；天气可以灰蒙蒙，判断也可以落在说不清黑白的 gray area。',
 '颜色词接古英语 grǣġ 等；gray、grey 的拼写历史涉及旧方言差异，现代 gray 在美式更常见。辐射吸收剂量单位 gray 则纪念物理学家 Louis H. Gray，不能归成颜色义。',G+[['专名 Gray → 单位 gray〔Gy〕','人名纪念命名，来源另列']],
 'gray hair 灰白头发，a gray sky 阴灰天空，a gray area 界线不清的领域，go gray 头发变灰白。颜色可以作名词，paint it gray 把它漆成灰色。',
 'gray hair；a gray sky；a gray area；go gray。',
 'gray 和 grey 通常是同一颜色的两种拼写，不表示深浅不同；人名、品牌和单位等固定名称保留自己的拼写。',
 ('The sky turned gray before the rain.','下雨前，天空变得灰蒙蒙的。'),('The policy leaves a gray area around personal use.','这项规定对个人用途留下了界线不清的地带。'),sources=['https://en.wiktionary.org/wiki/gray#English','https://www.merriam-webster.com/dictionary/gray'])
W('grayish','/ˈɡreɪɪʃ/','略带灰色的、偏灰的',
 '不是肯定地说它就是标准灰，而是看起来带一点灰，像颜色描述上留了点余地。',
 'gray + -ish，-ish 表有些、带某种性质。接在颜色后常是近似色；这里不是表示来自某国的人。',G+[['gray + -ish → grayish','带点灰色，接近灰色']],
 'a grayish blue 偏灰的蓝，grayish water 看起来泛灰的水，a grayish tint 一点灰色调；也常写 greyish。',
 'grayish blue；a grayish tint；grayish clouds。',
 'grayish 不是非常灰，-ish 在这里反而降低确定程度；grayish blue 的主色仍是 blue，灰只是修饰色调。',
 ('The wall was painted a grayish blue.','墙刷成了偏灰的蓝色。'),('A grayish cloud hung over the hill.','一朵灰蒙蒙的云悬在山上方。'))
W('grayscale','/ˈɡreɪskeɪl/','灰阶、灰度；灰度图像的；转成灰度',
 '把彩色拿走，留下从黑到白的一串明暗台阶；图像靠这些深浅差别继续表现轮廓和层次。',
 'gray 灰 + scale 等级、刻度，指灰色调的层级。先可指检验影像明暗的阶梯色条，也用于灰度表示方式、相关图像和转换动作。',G+[['gray + scale → grayscale','按明暗分级的灰阶；灰度图像方式']],
 'a grayscale image 灰度图，convert to grayscale 转为灰度，print in grayscale 灰度打印。也常见 grey scale、greyscale 拼写。',
 'a grayscale image；convert to grayscale；print in grayscale。',
 'grayscale 通常有多级灰，不只是纯黑和纯白两种值；binary image 二值图才常只保留两类。black and white 日常说法可包含灰阶照片。',
 ('Convert the photograph to grayscale before printing.','打印前把照片转成灰度图。'),('The grayscale image still shows the texture of the stone.','灰度图仍能显示石头的纹理。'))
R('B2699','灰色及其近似色、明暗层级','GRAY：黑白之间的灰，也能形容界线不清','gray/grey 同色异拼；grayish 略灰；grayscale 用灰阶表达图像。',
 '先分清颜色本身、颜色近似和图像表示方式。抽象的 gray area 借的是黑白之间难划线的画面，不是所有灰色东西都含负面评价。',
 'grǣġ/grēġ → gray/grey；gray + -ish；gray + scale。单位 gray 来自人名，另一路。',
 [['颜色及近似','gray · grey · grayish'],['明暗层级','grayscale']],
 'gray/grey 不代表深浅差别；grayish 不等于很灰；grayscale 通常有多级灰；单位 gray 不从颜色演化。',
 'The grayish background looks almost white in the grayscale print.\n\n偏灰的背景在这张灰度打印件里看起来几乎是白的。',
 'gray grey grayish grayscale')
S=[['古英语 strenġ → 中古英语 streng/string → string','绳、线，联系绷紧的古老词族'],['英语意义扩展','弦；串在一起的物件 → 一连串事件、文字字符']]
W('string','/strɪŋ/','细绳、线；弦；一串、一系列；字符串；穿成串、给……装弦',
 '一根细绳能拴东西，也能把珠子串起来；把珠子换成事件、字母，就有一连串事情和字符串。',
 '接古英语 strenġ，与绷紧、绳索的日耳曼语词族相关，不是英语 strong 删字得到。动词由名词发展，常见过去式、分词 strung。',S,
 'a piece of string 一段细绳，guitar strings 吉他弦，a string of failures 一连串失败，a text string 文本字符串，string beads 把珠子穿成串。no strings attached 没有附带条件。',
 'a piece of string；a string of；guitar strings；no strings attached。',
 'string 绳线一般比 rope 细；a string of events 不要求东西真的挂在线上。计算机的字符串可含数字字符，但不因此自动成可运算的数值。',
 ('She tied the parcel with a piece of string.','她用一段细绳捆好包裹。'),('A string of small mistakes delayed the project.','一连串小错误拖慢了项目。'))
W('stringed','/strɪŋd/','有弦的、装弦的',
 '乐器上装着能振动发声的弦，就有 stringed 这个性质。',
 'string + -ed，接中古英语相应形式；这里 -ed 可以表装有、具有。结尾读 /d/，整个词不因 -ed 再多一个音节。',S+[['string + -ed → stringed','有弦的，装了弦的']],
 'a stringed instrument 弦乐器，a stringed musical instrument 有弦的乐器；吉他、竖琴、小提琴都可包含在广义里。',
 'a stringed instrument；stringed musical instruments。',
 'stringed 强调具有弦的性质；strung 常是 string 动词的过去分词。the strings 作乐队分部时常有更具体范围，不能机械等同所有带弦乐器。',
 ('The exhibition includes stringed instruments from several countries.','展览包括来自几个国家的弦乐器。'),('She chose a stringed instrument rather than a wind instrument.','她选择了弦乐器，而不是管乐器。'))
W('stringy','/ˈstrɪŋi/','纤维多而难嚼的；细长成丝的；瘦而筋腱明显的',
 '食物一口咬下去全是拉不断的丝，或头发结成一绺绺细条，都让人想到 string。',
 'string + -y，-y 表具有绳线般性质。可从材料组成走向咀嚼口感、外观；不同对象不能全译成像绳子。',S+[['string + -y → stringy','成丝、多纤维；细瘦而筋腱明显']],
 'stringy meat 纤维粗韧难嚼的肉，stringy celery 纤维多的芹菜，stringy hair 一绺绺的头发；评价外貌时常不太好听。',
 'stringy meat；stringy celery；stringy hair。',
 'stringy 和 stretchy 有时都能形容拉丝，但 stringy 强调丝条、纤维，stretchy 强调能拉伸。stringy meat 不只是肉被切成长条。',
 ('The meat was tough and stringy.','那块肉又老又多筋，嚼不动。'),('His wet hair hung in stringy strands.','他湿漉漉的头发一绺绺地垂着。'))
W('stringer','英 /ˈstrɪŋə/；美 /ˈstrɪŋər/','特约通讯员、非正式员工的供稿者；纵向支撑构件等',
 '新闻里是没有列入正式记者编制、按约为媒体供稿的人；工程图上则可能是一根沿长度方向支撑结构的构件。',
 'string + -er，早有做弓弦者等人物义，支撑构件借线条般长形命名。新闻义的具体来路并非确定；有词源解释联系把词串起来的写作者，不能断言是记者把稿子挂绳上量长度。',
 S+[['string + -er → stringer','制弦、穿串者；长条支撑件'],['新闻用法发展','非正式编制的通讯供稿者；具体命名路线有不确定性']],
 'a local stringer 当地特约通讯员，a freelance stringer 自由供稿通讯员，a stair stringer 楼梯侧面承托踏步的构件。',
 'a local stringer；a freelance stringer；a stair stringer。',
 'stringer 不保证一定业余或水平低，关键是工作关系；staff reporter 则是媒体正式记者。工程义也不是弹弦的人。',
 ('The newspaper relies on a local stringer for reports from the island.','报社依靠当地特约通讯员报道岛上的消息。'),('The carpenter checked the stair stringer before fitting the steps.','木工安装踏步前检查了楼梯侧梁。'),sources=['https://en.wiktionary.org/wiki/stringer#English','https://www.etymonline.com/word/stringer'])
W('shoestring','/ˈʃuːstrɪŋ/','鞋带；极少的钱、微薄预算；细长条',
 '字面是一根鞋带；说 on a shoestring，就像手里只剩一根细鞋带那么点资源，也得把事情做起来。',
 'shoe 鞋 + string 绳，先形成鞋带名词。极少资金是由细小、有限的形象发展出的习惯比喻，不是拿鞋带当货币的史实。',S+[['shoe + string → shoestring','鞋带 → 细长条；on a shoestring 用极少资金']],
 'on a shoestring 靠微薄预算，a shoestring budget 极低预算，shoestring fries 细条薯条。日常鞋带也常用 shoelace。',
 'on a shoestring；a shoestring budget；shoestring fries。',
 'a shoestring budget 是钱很少，不是预算写在鞋带上；shoestring fries 是形状细长，不是鞋带做的食物。',
 ('They made the film on a shoestring.','他们用极少的经费拍成了这部电影。'),('We ordered sandwiches and shoestring fries.','我们点了三明治和细条薯条。'))
W('drawstring','/ˈdrɔːstrɪŋ/','抽绳、束口绳',
 '拉一下绳，袋口或裤腰就收紧；绳在布边通道里滑动，把开口聚拢。',
 'draw 拉 + string 绳。draw 在这里不是画画；合成词指出绳的用途，常装在袋口、裤腰或兜帽边。',S+[['draw + string → drawstring','拉动就能收紧开口的绳']],
 'a drawstring bag 抽绳袋，a drawstring waist 抽绳裤腰，tighten the drawstring 拉紧抽绳。',
 'a drawstring bag；a drawstring waist；tighten the drawstring。',
 'drawstring 是具体结构和用途；shoelace 是鞋带。两者都可能用绳，但不能只因材料相同就随意互换。',
 ('Pull the drawstring to close the bag.','拉抽绳，把袋口收起来。'),('The trousers have a comfortable drawstring waist.','这条裤子的抽绳裤腰穿着很舒服。'))
W('hamstring','/ˈhæmstrɪŋ/','腘绳肌、膝后相关肌腱；严重妨碍、束缚',
 '腿后方有像绷紧绳索的肌腱，帮助腿活动；比喻中让一个项目迈不开腿，就是 hamstring it。',
 'ham 这里是膝后部的旧义 + string 绳、筋腱，现代也用来称大腿后侧肌群。动词借使腿失去行动力的画面表达严重限制；英语比喻义记录还早于字面伤害义，并非火腿捆绳。',S+[['ham 膝后部 + string → hamstring','腿后相关肌腱、肌群'],['动词比喻','借失去行动力的画面 → 严重妨碍项目、组织等']],
 'a hamstring injury 腘绳肌损伤，tight hamstrings 腿后肌群紧绷，be hamstrung by 缺乏某条件而受阻；过去式、分词常用 hamstrung。',
 'a hamstring injury；tight hamstrings；be hamstrung by。',
 'ham 在此不是熟食火腿；hamstring 项目是比喻限制行动，不是单说有一点不方便。',
 ('The player missed the match with a hamstring injury.','球员因腘绳肌损伤缺席比赛。'),('The research was hamstrung by a lack of funding.','资金短缺让研究难以推进。'))
R('B2994','细绳、弦，及绳般排列和束缚的扩展','STRING：细长能绷紧，也能把许多东西串起来','string → stringed/stringy/stringer；鞋、抽拉、膝后部分别和 string 组成有用途的词。',
 '先抓细线，再看拉紧、串连、支撑三种画面。字符串把字符排成一串；限制条件像牵制的绳；并非每个后来义都能追成一个确定的故事。',
 'strenġ → string；string + -ed/-y/-er；shoe/draw/ham + string；动词常见 string/strung/strung。',
 [['线、弦与性质角色','string · stringed · stringy · stringer'],['绳的用途与比喻','shoestring · drawstring · hamstring']],
 'draw 这里是拉；ham 是膝后旧义；stringed 有弦，strung 动词分词；stringer 新闻义不编造唯一来源；on a shoestring 说预算很少。',
 'The stringer covered the concert on a shoestring budget.\n\n那位特约通讯员用很少的预算报道了音乐会。',
 'string stringed stringy stringer shoestring drawstring hamstring')
if __name__=='__main__':save('continuation_20261030_hm',ROOTS,WORDS)
