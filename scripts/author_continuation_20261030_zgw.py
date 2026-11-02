"""Swirls, whirling, billows, ripples and surges."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
def S(word,base):
 return ['https://en.wiktionary.org/wiki/'+word+'#English','https://www.etymonline.com/word/'+base]
EXISTING_ROOT_ADDITIONS={
 'A1741':dict(words='swirl swirls swirled swirling swirly'.split(),label='swirl：绕着转的运动与花纹',note='swirl 的名词、动词更早来源未定，有苏格兰、邻近日耳曼材料等分析。-ing、-y 的现代性质可以清楚拆，不把 swirl、whirl 自动定成同一个词的两种拼法。'),
 'B3011':dict(words='whirl whirls whirled whirling whirlwind whirlwinds'.split(),label='whirl 与 wind 在 whirlwind 中组合',note='whirl 可能接北欧旋转材料；whirlwind 为旋转与风的复合，可能仿照北欧同类词。这里共同出现在风词族页，不表示 whirl 是由现代 wind 换字母派生。'),
 'A1760':dict(words='billow billows billowed billowing'.split(),label='billow：大浪般鼓起、翻涌',note='billow 名词借北欧大浪材料，动词由名词发展；billowed、billowing 写烟、布、水等鼓起翻卷，不与 bellow 叫吼混为一词。'),
 'A2238':dict(words='ripple ripples rippled rippling'.split(),label='ripple：细波纹与向外传开的小影响',note='ripple 有褶皱、细小起伏的旧材料，远源分析不一致；不能硬说 rip 撕加 -le 小就等于水被撕开。现代词尾按基底整体分析。'),
 'C1459':dict(words='surge surges surged surging'.split(),label='surge：一股向上、向前涌起的力量',note='surge 接法语、拉丁 surgere 起来材料，具体名词、动词中介有不同分析；数量、情绪和水体都能突然增强，不只说海浪。'),
 'A1740':dict(words='gush gushing gushingly'.split(),label='gushingly：话、赞美像水一样涌出来',note='gush 来源有英语拟声、低地德语、北欧等分析；gushingly 写过分热情倾诉的方式，不把所有真诚赞扬都贬作虚假。'),
}
SWIRL=[['早期苏格兰等英语 swirl 名词、动词材料','涡流、打旋；远源未定，有邻近日耳曼形式等分析'],['打旋动作 → 旋涡形纹样、密集交织的事物','swirly 接名词 swirl 与 -y；不据现代短词先学就硬定所有年代']]
WHIRL=[['中古英语 whirlen，可能接古诺斯 hvirfla','绕圈、旋转，也与相关古英语转动词可比较'],['whirl → 旋转、忙乱；whirl + wind → whirlwind','旋风复合可能仿北欧同类词，后来也比喻旋风般密集活动']]
BILLOW=[['古诺斯 bylgja 等 → 英语 billow 名词','大浪，接更早膨胀、鼓起材料'],['大浪名词 → billow 动词','像浪一样隆起、翻卷，用于水、烟、布料等']]
RIPPLE=[['早期 riplen 等：起皱、形成细小起伏','远源分析不一致，有 rimple、rip 与反复尾等比较'],['动词 → 小波纹名词；扩展到声音、影响传开','水面细波一层层扩散的画面，有助理解现代 ripple through 等搭配']]
SURGE=[['拉丁 sub- 加 regere → surrigere、surgere','从低处挺起、起来'],['可能经法语 sourdre、sourge-、surgir 等 → surge','涌起、涌浪；名词、动词近源不只一个确定分析'],['现代水、客流、数量、情绪的 surge','一股力量突然增强、往上或往前涌']]
GUSH=[['中古英语 gushen → gush','可能拟声、借邻近语言或受其影响，远源路线未定'],['液体猛涌 → 话、赞美倾泻；gushing + -ly','热情说个不停，有时带说话人认为过度的评价']]
W('swirl','英 /swɜːl/；美 /swɝl/','打旋、回旋；轻搅成旋涡；旋纹、一阵交织活动',
 '奶倒进咖啡后绕出一圈圈花纹，或烟、叶子在风里兜圈，就是 swirl。既可写动作，也可写那一圈纹、那一团回旋。',
 '早期苏格兰英语等已有涡流、打旋材料，远源未定；动词有邻近日耳曼来源或由名词转用等分析。现代先把 swirl 视作整体，不强定一种远古拆法。',SWIRL,
 'swirl the liquid 轻搅液体成旋涡；a swirl of cream 一圈奶油纹；rumours swirl 传言纷起。',
 'swirl around 在周围打旋；a swirl of activity 一阵纷乱活动。',
 'swirl 着重绕圈运动，waft 着重被柔和带动；同一缕烟可轻飘又转圈，不是两词互相排斥。',
 ('Swirl the glass gently to mix the juice.','轻轻转动杯子，把果汁混匀。'),('A swirl of cream spread across the coffee.','一圈奶油纹在咖啡表面散开。'),sources=S('swirl','swirl'))
W('swirls','英 /swɜːlz/；美 /swɝlz/','打旋、轻搅〔第三人称单数〕；旋纹、涡流〔复数〕',
 '围巾上一个个卷转花纹是 swirls；风把叶子卷来卷去，动词也能用 swirls。看的是纹样，还是正在发生的动作，要放回句子。',
 'swirl + -s，/l/ 后读 /z/；名词复数和动词三单同形，远源未定。',SWIRL+[['swirl + -s → swirls','它打旋、使回旋；多个旋纹、涡流']],
 'swirls of smoke 旋动的团团烟；swirls of colour 盘绕的彩纹。',
 'smoke swirls around 烟在周围打旋；swirls the water。',
 'swirls of colour 强调颜色绕成卷纹，stripes 是条纹；都可能在布上，但不是同一种图案。',
 ('The scarf was covered in blue and green swirls.','围巾上布满蓝绿相间的旋纹。'),('Smoke swirls above the roof.','烟在屋顶上方打旋。'),sources=S('swirls','swirl'))
W('swirled','英 /swɜːld/；美 /swɝld/','打旋、回旋了；轻搅、转动了',
 '液体在杯子里转出圈，或风把落叶卷成一团转起来，过去发生了就是 swirled。它抓住运动路径的回旋。',
 'swirl + 完整 -ed，/l/ 后读 /d/；动词可以是自己打旋，也可以及物地把液体等轻搅成旋。',SWIRL+[['swirl + -ed → swirled','过去形成或造成回旋动作']],
 'swirled the liquid 转动、轻搅液体；leaves swirled 落叶打旋。',
 'swirled around her feet；swirled into the room 旋动着进入房间。',
 'swirled the water 写水绕圈，spilled the water 写水洒出；杯中转动不等于已经洒到外面。',
 ('Leaves swirled around our feet.','落叶在我们脚边打旋。'),('She swirled the liquid in the glass.','她轻轻转动杯中的液体。'),sources=S('swirled','swirl'))
W('swirling','英 /ˈswɜːlɪŋ/；美 /ˈswɝlɪŋ/','正在打旋、盘绕的；纷乱交织的',
 '雪、雾、烟一阵阵绕着转，叫 swirling；传言、情绪交织，也能像一团回旋的东西裹着人。',
 'swirl + -ing；动作形式也可形容盘绕、密集交织的性质，现代不同对象都抓住旋动意象。',SWIRL+[['swirl + -ing → swirling','回旋动作的过程，或像回旋一样交织']],
 'swirling snow 打旋的雪；swirling mist 回旋的雾；swirling rumours 纷起交织的传言。',
 'swirling around；swirling patterns 旋动般的图案。',
 'swirling rumours 常写消息交织、四起，不保证内容真；confirmed reports 才明确经过证实。',
 ('We could barely see through the swirling snow.','打旋的雪里，我们几乎看不清。'),('The painting was full of swirling patterns.','画里满是盘绕回旋般的图案。'),sources=S('swirling','swirl'))
W('swirly','英 /ˈswɜːli/；美 /ˈswɝli/','有旋纹的；卷曲盘绕的；打旋的',
 '糖霜、笔迹、布料上绕来绕去的卷纹，叫 swirly。它能写静态花纹，不一定东西此刻真在转。',
 'swirl 名词 + -y；把旋转、卷纹写成性质。swirl 远源未定，但这一层形容词构词清楚。',SWIRL+[['swirl + -y → swirly','有旋纹、卷曲盘绕或打旋的性质']],
 'swirly patterns 卷转花纹；swirly handwriting 卷曲花哨的笔迹。',
 'a swirly design；swirly icing 旋纹糖霜。',
 'swirly design 可以是静止的旋纹，swirling liquid 则常是液体正在打旋；性质、过程不可只按都像转圈就混用。',
 ('The cake had a swirly icing pattern.','蛋糕上的糖霜带着卷转花纹。'),('I found her swirly handwriting difficult to read.','她那卷曲花哨的笔迹让我不太好辨认。'),sources=S('swirly','swirl'))
W('whirls','英 /wɜːlz/；美 /wɝlz/','迅速旋转、使旋转〔第三人称单数〕；旋转动作〔复数〕',
 '舞者一转身，裙摆跟着绕圈，叫 whirls；一连串转圈动作也可以说 whirls。核心是快速绕着转。',
 'whirl + -s，/l/ 后读 /z/；动词三单和名词复数同形。基础词可能接古诺斯旋转材料，与 wind 风在 whirlwind 中组合，不从风名词直接造来。',WHIRL+[['whirl + -s → whirls','他或它快速旋转；多次转圈']],
 'whirls around 迅速转圈、转身；whirls past 旋动着掠过。',
 'the dancer whirls；a head that whirls 脑中混乱、发晕。',
 'whirls around 突出快速绕转，walks around 可以只是绕着走；转动本身与沿外围走的路径不同。',
 ('The dancer whirls across the stage.','舞者旋转着穿过舞台。'),('The wind whirls the leaves around the courtyard.','风把落叶卷得在庭院里转圈。'),sources=S('whirls','whirl'))
W('whirled','英 /wɜːld/；美 /wɝld/','迅速旋转、转身了；卷动了',
 '听到身后叫声，一下转过身，是 whirled around；一阵风把纸张卷着转，也能用 whirled。',
 'whirl + 完整 -ed，/l/ 后读 /d/；可不及物说自己转，也可及物说使别的东西转。',WHIRL+[['whirl + -ed → whirled','过去迅速绕转，或使某物卷转']],
 'whirled around 猛地转身；whirled the papers 卷动纸张。',
 'whirled across the floor；whirled in the wind。',
 'whirled around 常是一下迅速转身，turned around 可以更中性、平缓；速度和戏剧性不同。',
 ('She whirled around when she heard her name.','听到有人叫名字，她猛地转过身。'),('Dust whirled in the hot wind.','尘土在热风中旋转。'),sources=S('whirled','whirl'))
W('whirling','英 /ˈwɜːlɪŋ/；美 /ˈwɝlɪŋ/','正在快速旋转的；脑中纷乱、发晕的',
 '车轮、舞者、落叶不停快速绕转，是 whirling；消息太多，头脑仿佛转得停不住，也可说 my head is whirling。',
 'whirl + -ing；动作形式可描述物理快速旋转，也比喻纷乱思绪、发晕感。',WHIRL+[['whirl + -ing → whirling','快速旋转的过程；或脑中像在旋转的状态']],
 'whirling blades 旋转的叶片；whirling thoughts 纷乱思绪；head whirling 脑中一片混乱。',
 'whirling around the room；a whirling cloud of dust 一团旋动尘土。',
 'whirling 写快速旋转，waving 常写来回挥、摆；一圈圈转和左右摆不必相同。',
 ('The dancers formed a whirling circle.','舞者们组成一个旋转的圆圈。'),('My head was whirling after all the unexpected news.','那么多意外消息传来后，我脑中一片混乱。'),sources=S('whirling','whirl'))
W('whirlwinds','英 /ˈwɜːlwɪndz/；美 /ˈwɝlwɪndz/','旋风〔复数〕；旋风般快、密集的人或事',
 '风一股股卷着转，是 whirlwinds；小孩子进门就把安静气氛搅得动起来，也可比喻为 little whirlwinds。',
 'whirlwind + -s，读 /z/；内层 whirl 旋转 + wind 风，wind 在这里读 /wɪnd/。中古英语已有复合，可能仿北欧同类词。',WHIRL+[['whirl + wind → whirlwind → whirlwinds','多股旋风；也比喻一阵阵密集、迅猛活动']],
 'little whirlwinds 旋风般精力旺盛的孩子；whirlwinds of dust 卷尘旋风。',
 'a pair of whirlwinds；emotional whirlwinds 一阵阵强烈情绪。',
 'whirlwinds 是旋转的风，strong winds 只说风大；大风不一定形成一个局部旋转的风柱。',
 ('Small whirlwinds lifted dust from the dry ground.','一股股小旋风从干地上卷起尘土。'),('The twins were little whirlwinds, racing from room to room.','那对双胞胎像两股小旋风，在各个房间之间跑来跑去。'),sources=S('whirlwinds','whirlwind'))
W('billow','英 /ˈbɪləʊ/；美 /ˈbɪloʊ/','翻涌、鼓起；大浪；大团翻卷的烟、云等',
 '窗帘被风撑得鼓出一大团，烟像浪一样一团团涌上来，都可以 billow。它的形状比 ripple 的细波大、饱满。',
 '名词借古诺斯 bylgja 大浪等材料，接更早鼓起、膨胀词族；动词由名词发展，像大浪般翻涌。',BILLOW,
 'billow in the wind 在风中鼓起；billow from a chimney 从烟囱翻涌而出。',
 'a billow of smoke 一大团翻卷的烟；billow outwards 向外鼓起。',
 'billow 是大团鼓起、翻卷，bellow 是吼叫；一团烟会 billow，发怒的人可能 bellow，读音、来源分开。',
 ('The curtains began to billow in the breeze.','窗帘开始在微风中鼓起。'),('A dark billow of smoke rose above the roof.','一大团翻卷的黑烟升到屋顶上方。'),sources=S('billow','billow'))
W('billows','英 /ˈbɪləʊz/；美 /ˈbɪloʊz/','翻涌、鼓起〔第三人称单数〕；大浪、团团翻卷物〔复数〕',
 '烟不是细线一样飘，而是一大团一大团翻卷，是 billows of smoke；一面帆被风撑鼓，动词也用 billows。',
 'billow + -s，读 /z/；名词复数和动词三单同形，名词大浪义先有，动词翻卷后来发展。',BILLOW+[['billow + -s → billows','它像浪般鼓起；多团大浪、烟云']],
 'billows of smoke 团团翻卷的烟；the sail billows 帆鼓起来。',
 'white billows of cloud 大团白云；smoke billows out 烟翻涌而出。',
 'billows of smoke 常是大团翻卷，wisps of smoke 是细缕烟；同样是烟，体量、形态相差很大。',
 ('Billows of smoke rose from the hillside.','团团烟雾从山坡上翻涌升起。'),('The sail billows as the wind strengthens.','风力增强时，帆鼓了起来。'),sources=S('billows','billow'))
W('billowed','英 /ˈbɪləʊd/；美 /ˈbɪloʊd/','翻涌、鼓起了',
 '风一灌进来，窗帘鼓成一大团；或烟从缝里一团团涌出来，过去发生了就是 billowed。',
 'billow + 完整 -ed，词尾读 /d/；基础动词由大浪名词转用，写隆起、翻卷。',BILLOW+[['billow + -ed → billowed','过去像大浪一样鼓起、翻卷']],
 'billowed outwards 向外鼓起；billowed from the opening 从开口翻涌出来。',
 'curtains billowed 窗帘鼓起；smoke billowed 烟翻卷。',
 'billowed 是鼓成团、翻卷，fluttered 常更像轻薄部分快速扑动；一面旗、窗帘可能不同部位出现不同运动。',
 ('The white curtains billowed into the room.','白窗帘鼓起，向室内飘动。'),('Smoke billowed from the open doorway.','烟从敞开的门口翻涌而出。'),sources=S('billowed','billow'))
W('billowing','英 /ˈbɪləʊɪŋ/；美 /ˈbɪloʊɪŋ/','正在鼓起、翻涌；像大浪般蓬起的',
 '帆、窗帘一大块撑起，烟云一团团翻卷，都叫 billowing。像有体积的浪隆起，不只是轻轻抖一下。',
 'billow + -ing；动作形式也可形容大团鼓起、翻卷的性质。',BILLOW+[['billow + -ing → billowing','像大浪鼓起、翻卷的过程或外形']],
 'billowing smoke 翻涌的烟；billowing sails 鼓起的船帆；a billowing skirt 蓬起飘动的裙摆。',
 'clouds billowing upwards 云团向上翻涌；billowing out。',
 'billowing smoke 的重点是体积大、翻卷，rising smoke 只说上升；轻烟上升也未必能称 billowing。',
 ('A ship with billowing sails crossed the bay.','一艘鼓满风帆的船驶过海湾。'),('Dark smoke was billowing above the trees.','黑烟正在树梢上方一团团翻涌。'),sources=S('billowing','billow'))
W('ripples','/ˈrɪpəlz/','细波纹、涟漪〔复数〕；起波纹、逐渐传开〔第三人称单数〕',
 '小石子落下，一圈圈细纹向外走，是 ripples；一段消息引起反应，也像细波一样从一个人传到下一个人。',
 'ripple + -s，读 /z/；名词复数和动词三单同形，基础词的远源有不同分析，不能直接断定水面被 rip 撕开。',RIPPLE+[['ripple + -s → ripples','多个细波纹；它形成小起伏、传开']],
 'ripples on the water 水面涟漪；ripples of laughter 阵阵笑声；news ripples through the town 消息在镇上传开。',
 'send ripples through 影响逐渐传遍；small ripples。',
 'ripples 通常是小起伏，不等于 huge waves 大浪；影响的 ripple 比喻也常突出传播过程，而不是一开始就强烈冲击。',
 ('Ripples spread across the pond.','涟漪在池塘里散开。'),('Excitement ripples through the audience as the curtain rises.','幕布升起时，兴奋在观众中传开。'),sources=S('ripples','ripple'))
W('rippled','/ˈrɪpəld/','起细波纹了；如波纹传开了',
 '微风过来，水面起一层层小纹，是 rippled；一阵笑、惊讶从人群一头传到另一头，也像波纹散开。',
 'ripple 去 e 加完整 -ed，读 /d/；动词接旧起皱、形成细小起伏材料，英语不直接拿撕裂动作解释全部来源。',RIPPLE+[['ripple → rippled','过去形成细小波纹，或反应逐步传开']],
 'water rippled 水起涟漪；laughter rippled through the room 笑声在房间传开。',
 'rippled across the surface；rippled in the breeze。',
 'rippled through the audience 常是反应一个接一个传开，everyone shouted at once 则是同时大喊；时间、传播画面不同。',
 ('The water rippled in the light breeze.','水面在微风中泛起涟漪。'),('Laughter rippled through the room.','笑声在房间里传开。'),sources=S('rippled','ripple'))
W('rippling','/ˈrɪplɪŋ/','泛起细波纹的；像细波一样传开、起伏的',
 '水面、薄布上细细起伏，或笑声一阵阵传开，可以用 rippling。比大团翻卷轻、细，但不一定完全没有力量。',
 'ripple 去 e 加 -ing；动作形式可形容细波纹、连续小起伏的性质，常见读音中间收成 /pl/。',RIPPLE+[['ripple → rippling','细小起伏的过程；或像波纹般传动的性质']],
 'rippling water 泛细波的水；rippling laughter 一阵阵传开的笑声。',
 'rippling fabric 细细起伏的布；effects rippling through the system 影响逐层传过系统。',
 'rippling fabric 可以是正在细细起伏，ripped fabric 是撕破的布；两词历史关系有不同分析，现代含义却不能混读。',
 ('Sunlight flashed on the rippling water.','阳光在泛着细波的水面闪动。'),('The announcement sent excitement rippling through the crowd.','公告让兴奋一阵阵传遍人群。'),sources=S('rippling','ripple'))
W('surges','英 /ˈsɜːdʒɪz/；美 /ˈsɝdʒɪz/','猛增、涌起〔第三人称单数〕；一阵阵强烈涌动〔复数〕',
 '需求一下涨上去，是 demand surges；情绪、电流、水体一阵阵突然增强，则可说 surges。核心是一股力量涌起来。',
 'surge + -s，/dʒ/ 后词尾读 /ɪz/；动词三单和名词复数同形，承拉丁起来、法语涌起材料。',SURGE+[['surge + -s → surges','它突然增强、涌起；多阵强烈涌动']],
 'demand surges 需求激增；surges of excitement 阵阵兴奋；power surges 电流、电压突增。',
 'surges forward 向前涌；surges in demand 几轮需求激增。',
 'surges 强调短时间内明显增强，rises 可以只是逐渐上升；不是每次数字增长都足以叫 surge。',
 ('Demand for ice cream surges during hot weather.','天气炎热时，冰淇淋需求激增。'),('She felt sudden surges of excitement as the race began.','比赛开始时，她感到一阵阵兴奋突然涌起。'),sources=S('surges','surge'))
W('surged','英 /sɜːdʒd/；美 /sɝdʒd/','猛增、涌起、向前猛涌了',
 '人群一起朝前压，水一下涌上来，或数字突然跳高，过去发生了都可用 surged。比一般 went up 更有集中、突增的势头。',
 'surge 去 e 加完整 -ed，/dʒ/ 后读 /d/；末尾连成 /dʒd/，不另读 /ɪd/。',SURGE+[['surge → surged','过去突然增强、涌起或猛涌向前']],
 'surged forward 向前猛涌；prices surged 价格猛涨；water surged in 水猛涌进来。',
 'surged through the gates 涌过大门；confidence surged 信心猛增。',
 'surged forward 可能是人群合力涌动，darted forward 更像单个对象突然窜出；集体势头、短促动作不同。',
 ('The crowd surged forward when the gates opened.','大门打开时，人群向前涌去。'),('Orders surged after the product demonstration.','产品演示后，订单猛增。'),sources=S('surged','surge'))
W('surging','英 /ˈsɜːdʒɪŋ/；美 /ˈsɝdʒɪŋ/','正在猛增、涌动；急剧增强的',
 '不是缓缓加一点，而是一股股力量正往上、往前涌，是 surging。可以写海水、客流、需求、情绪。',
 'surge 去 e 加 -ing；动作形式也作形容词，描述快速增强、带强势头的过程。',SURGE+[['surge → surging','猛涌、急剧增强的过程或性质']],
 'surging demand 激增的需求；surging crowds 涌动的人群；surging waves 猛涌的波浪。',
 'surging ahead 迅猛前进；surging confidence 急升的信心。',
 'surging demand 强调需求强烈增长，steady demand 是稳定需求；增长势头和稳定水平是不同描述。',
 ('The company expanded to meet surging demand.','公司扩大规模，以应对激增的需求。'),('We watched waves surging against the rocks.','我们看着波浪一股股猛涌向礁石。'),sources=S('surging','surge'))
W('gushingly','/ˈɡʌʃɪŋli/','热情洋溢、滔滔不绝地；过分热情地',
 '赞美像水一样一股脑往外涌，停不下来，叫 gushingly。听者有时会觉得热情过头，但不自动表示赞美是假的。',
 'gushing + -ly；内层 gush + -ing，从液体猛涌到情感、话语倾泻，外层再修饰说、赞等方式。',GUSH+[['gush → gushing → gushingly','热情、赞美倾泻的性质，转成说话方式']],
 'spoke gushingly 热情地滔滔不绝；gushingly praised 热情满溢地称赞。',
 'gushingly enthusiastic 热情得有点过头；gushingly described。',
 'gushingly 常带情感流露很多、可能过头的评价，sincerely 才直接说真诚；热情程度与真假是两回事。',
 ('She spoke gushingly about her new job.','她热情洋溢地说个不停，谈自己的新工作。'),('He gushingly praised every detail of the performance.','他满怀热情，把表演的每个细节都夸了一遍。'),sources=S('gushingly','gush'))
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_zgw',ROOTS,WORDS)
 extend_lessons()
