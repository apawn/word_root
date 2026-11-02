"""Swooping, rushing sounds, sharp points and common posture adjectives."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
def S(word,base):
 return ['https://en.wiktionary.org/wiki/'+word+'#English','https://www.etymonline.com/word/'+base]
EXISTING_ROOT_ADDITIONS={
 'B2996':dict(words='swoop swoops swooped swooping'.split(),label='swoop：弧线般掠下，与旧扫动材料的联系',note='swoop 很可能延续古英语 swapan 扫、挥动的方言材料，与 sweep 较早形式有关；猛禽扑下的名动用法有各自发展，不硬说现代 sweep 改几个字母便产生 swoop。'),
 'A1760':dict(words='swoosh swooshes swooshed swooshing'.split(),label='swoosh：把嗖、呼的声音变成词',note='swoosh 大体为拟声词，先有快速掠过的声音名词，再有动词。此处与其他规则过去式比较，不能因都以 sw- 开头就断为 sway、sweep 的同一派生链。'),
 'C1394':dict(words='spike spiked spiking spiky'.split(),label='spike：尖形、曲线尖峰与词义分支',note='尖钉 spike 接日耳曼、北欧材料，谷穗义另有拉丁 spica 借入。spiked、spiking 可写数值猛增、加尖刺或往饮料加料，各按具体句子理解；远源关系不全确定。'),
 'B2846':dict(words='dive dives dived diver divers'.split(),label='dive 的规则形式与潜水者',note='dive 接古英语两个相关浸入动词的合流，dived 是规则过去式、分词；北美常见过去式 dove 是后起类推，不等于原封不动保留古英语强变化。'),
 'B4227':dict(words='dip dips dipping'.split(),label='dip：轻蘸、低下去与短暂浏览',note='dip 接古英语 dyppan 等浸入材料。dips、dipping 既可写动作，也可由现代名词义理解；曲线 dip 本身不保证随后反弹。'),
 'B4087':dict(words='slouch slouchy'.split(),label='slouchy：松松垮垮的姿态、衣物',note='slouch 早期人物名词远源未定，或有北欧松垮材料联系；slouchy 加 -y 写姿态、衣物的松垮性质，不据衣服松垮判穿着者能力。'),
 'B4179':dict(words='sag saggy'.split(),label='saggy：撑不住、松垂下来的性质',note='saggy 接 sag 名词与 -y，双写 g；sag 较早来源有北欧、低地德语等分析。现代形容词写易松垂或已经松垂的外观。'),
 'B2843':dict(words='slink slinky'.split(),label='slinky：贴身流畅、曲线柔顺的性质',note='slinky 接 slink 与 -y；旧有瘦长、松垂义，现代服装义还说贴身、流线般柔顺，不能粗译成偷偷摸摸的衣服。'),
}
SWOOP=[['古英语 swapan 扫、挥动的方言材料 → swoop','近源通常如此分析，更远来源不全确定'],['旧扫动、打击材料 → 猛禽弧线般扑下','后来也说人突然赶来、采取行动']]
SWOOSH=[['英语拟声 swoosh 名词','模仿东西快速掠过空气的嗖、呼声'],['声音名词 → swoosh 动词','带着这类声响快速移动；再加现代词尾']]
SPIKE=[['尖钉 spike 接日耳曼、北欧等材料；谷穗义有拉丁 spica','具体借入、远源联系不应压成一个确定步骤'],['尖钉名词 → 加尖刺等动词 → 其他现代用法','尖峰形状可写数值突增；饮料加料、撤稿等须分别认搭配']]
DIVE=[['古英语 dufan 下潜与 dyfan 使浸入等 → dive','相关动词在中古英语合流'],['规则 dived 延续，后起类推过去式 dove 也常用','diver 是 dive 加人物、事物尾 -er']]
DIP=[['古英语 dyppan → dip','浸一下，属于与 deep 可比较的旧材料'],['动作 → 蘸酱、低处、短时下降等名词','现代 dips、dipping 依句子判断语法角色']]
W('swoop','/swuːp/','俯冲、掠下；突然赶来；一次猛扑',
 '老鹰不是笔直掉落，而是带着一道扫下来的弧线冲向猎物，这个动作很像 swoop。人突然出现、迅速行动，也能借这个画面。',
 '很可能延续古英语 swapan 扫、挥动的方言材料，与 sweep 的较早形式有关。旧动词、打击名词及后来猛禽扑击用法的先后较复杂，不能只写现代扫地动作变成抓鸟。',SWOOP,
 'swoop down 向下掠、俯冲；swoop in 突然赶来；in one fell swoop 一举、一下子。',
 'swoop over the water 掠过水面；a sudden swoop 一次突然猛扑。',
 'swoop 常带快速扫过、掠下的路径，dive 更直接写俯冲或扎入；二者可描述同一只鸟的不同侧面。',
 ('We watched the hawk swoop down towards the field.','我们看着鹰向田野俯冲下去。'),('The new rule removed several barriers in one fell swoop.','新规定一下子扫除了几道障碍。'),sources=S('swoop','swoop'))
W('swoops','/swuːps/','俯冲、掠下、突然赶来〔第三人称单数〕；猛扑动作〔复数〕',
 '一只燕子低低掠过池塘，可以说 it swoops；鸟飞行时一连串俯冲动作，则能叫 swoops。',
 'swoop + -s，/p/ 后读 /s/；动词三单、名词复数同形，内部 oo 读 /uː/。',SWOOP+[['swoop + -s → swoops','它掠下、突然赶来；多次猛扑']],
 'swoops over the pond 掠过池塘；swoops and turns 俯冲与转弯。',
 'swoops down from the roof；swoops in to help 突然赶来帮忙。',
 'swoops 常把动作写得快速、带弧线；hovers 则是悬停、盘旋在附近，不是同一种路径。',
 ('A swallow swoops low over the pond.','一只燕子低低掠过池塘。'),('The drone made a series of swoops and turns.','无人机做出一连串俯冲和转弯动作。'),sources=S('swoops','swoop'))
W('swooped','/swuːpt/','俯冲、掠下了；突然赶来行动了',
 '鸟从屋顶一下掠下来，或一队人忽然赶到现场开始行动，是 swooped。它把出现和动作连得很紧。',
 'swoop + 完整 -ed，/p/ 后读 /t/；没有新增音节。',SWOOP+[['swoop + -ed → swooped','过去快速掠下或突然赶来行动']],
 'swooped down 俯冲下来；swooped in 突然赶来。',
 'swooped over the crowd；swooped in to rescue。',
 'swooped in 常有迅速到场、立即行动的感觉，arrived 只说到达；不一定是警方或危险场景。',
 ('The gull swooped down and snatched a piece of bread.','海鸥俯冲下来，叼走了一块面包。'),('My sister swooped in to help with the last-minute preparations.','姐姐赶来帮忙处理最后关头的准备工作。'),sources=S('swooped','swoop'))
W('swooping','/ˈswuːpɪŋ/','正在俯冲、掠过的；大幅弯转的',
 '鸟的轨迹一弯，快速掠向低处，是 swooping；画里的线条像飞行轨迹一样大幅弯转，也能借这个词描写。',
 'swoop + -ing；动作形式可作修饰，强调扫过、弯转的路径，不必真有接触或抓住目标。',SWOOP+[['swoop + -ing → swooping','快速掠下的过程，或像扫过轨迹般的形态']],
 'swooping birds 掠飞的鸟；swooping curves 大幅弯转的曲线。',
 'swooping over the water；swooping down towards the ground。',
 'swooping 侧重掠动路径，soaring 侧重高飞、向上升；同一只鸟在不同阶段可以两种动作都有。',
 ('We stood watching birds swooping over the water.','我们站着看鸟儿在水面上掠飞。'),('The logo is made of long, swooping curves.','标志由几条长长的弯转曲线组成。'),sources=S('swooping','swoop'))
W('swoosh','/swuːʃ/','嗖、呼的掠过声；嗖地快速移动',
 '滑雪者从身边掠过，耳朵听到一声“呼——”，swoosh 就把这类声音写出来。它也能作动词，把动作和声音放在一起。',
 '拟声形成，较早名词写东西快速掠过空气的声响，后来转作动词。不是所有 sw- 开头的词都由同一现代词根拼出。',SWOOSH,
 'with a swoosh 呼地一下；swoosh past 嗖地掠过；the swoosh of skis 滑雪板的掠行声。',
 'a loud swoosh；swoosh through the snow。',
 'swoosh 比较突出掠过的声响，swoop 比较突出快速扫过、俯冲的路径；音近不代表它们是同一个词。',
 ('The skier passed us with a swoosh.','滑雪者呼地一下从我们身边掠过。'),('We heard the swoosh of a car on the wet road.','我们听见汽车驶过湿路面的唰唰声。'),sources=S('swoosh','swoosh'))
W('swooshes','/ˈswuːʃɪz/','嗖地掠过〔第三人称单数〕；嗖、呼声〔复数〕',
 '一阵阵东西掠过，声音可以叫 swooshes；主语是单数、说它呼地经过，也写 swooshes。',
 'swoosh + -es，/ʃ/ 后读 /ɪz/，多一个音节；名词复数、动词三单同形。',SWOOSH+[['swoosh + -es → swooshes','它嗖地掠过；一声声掠过声']],
 'swooshes past 呼地掠过；soft swooshes 轻轻的呼声。',
 'swooshes of passing traffic；a skirt swooshes 裙摆唰地摆过。',
 'swooshes 模仿快速掠动的声音，bangs 常是砰砰撞击声；不应把所有运动声都用一个拟声词。',
 ('Her long skirt swooshes as she turns.','她转身时，长裙唰地摆动。'),('We could hear the soft swooshes of passing cars.','我们能听见车辆驶过时轻轻的唰唰声。'),sources=S('swooshes','swoosh'))
W('swooshed','/swuːʃt/','嗖地、唰地掠过去了',
 '门唰地合上，球从耳边嗖地过去，swooshed 写过去发生的快速运动，也让读者仿佛听到声音。',
 'swoosh + 完整 -ed，/ʃ/ 后读 /t/；不另起 /ɪd/ 音节。',SWOOSH+[['swoosh + -ed → swooshed','过去带嗖、呼声快速移动']],
 'swooshed past 嗖地掠过；swooshed shut 唰地关上。',
 'swooshed down the slope；swooshed through the air。',
 'swooshed 是轻快或迅速掠动的声感，slammed 常是猛撞、砰地关；同是关门，力度、声音不同。',
 ('The automatic doors swooshed shut behind us.','自动门在我们身后唰地合上。'),('The ball swooshed past my ear.','球嗖地从我耳边飞过。'),sources=S('swooshed','swoosh'))
W('swooshing','/ˈswuːʃɪŋ/','正在嗖地移动；连续的呼、唰声',
 '夜里一辆辆车驶过湿路，声响连成唰唰一片，可以说 swooshing。它也可写滑雪板、人或物快速掠行的过程。',
 'swoosh + -ing；既可作动作形式，也可把反复、持续的这类声音当作名词来谈。',SWOOSH+[['swoosh + -ing → swooshing','带掠过声的动作过程，或这种持续声响']],
 'a swooshing sound 唰唰声；swooshing down the slope 呼地滑下坡。',
 'the swooshing of traffic 车辆来往的唰唰声；swooshing past。',
 'swooshing 强调声感，moving 只说移动；同一动作可以无须突出声音，也可以用拟声词营造现场感。',
 ('We heard a swooshing sound outside the tent.','我们听见帐篷外传来唰唰声。'),('The children went swooshing down the snowy slope.','孩子们呼地滑下雪坡。'),sources=S('swooshing','swoosh'))
W('spiked','/spaɪkt/','骤增了；有尖刺的；被加了酒或其他物质的',
 '曲线突然冒出尖峰、栅栏顶上长着尖刺、饮料里被加了东西，都可能用 spiked。先看对象，别把所有场景都硬译成尖刺。',
 'spike 去 e 加完整 -ed，/k/ 后读 /t/。既有动词过去、分词，也有形容词用法；加饮料成分与钉尖刺是已固定的不同词义分支。',SPIKE+[['spike + -ed → spiked','过去突增、加尖刺或加料；也描述处理后的状态']],
 'spiked hair 竖成尖束的头发；spiked shoes 钉鞋；spiked punch 加酒的潘趣酒。',
 'demand spiked 需求突增；spiked with rum 加了朗姆酒。',
 'spiked drink 不一概等于被下毒，需看加的是酒还是别的物质、是否知情；句子说明什么就理解到什么。',
 ('Electricity demand spiked during the heatwave.','热浪期间，用电需求突然猛增。'),('The punch was spiked with rum.','潘趣酒里加了朗姆酒。'),sources=S('spiked','spike'))
W('spiking','/ˈspaɪkɪŋ/','正在骤增；加尖刺、向饮料加料等动作',
 '屏幕上某项数据突然蹿出尖峰，可以说 it is spiking；排球里把球猛扣下去，也叫 spiking。对象不同，具体动作跟着变。',
 'spike 去不发音 e 加 -ing。名词尖钉形成动词后发展多条用法；数值、排球、饮料不能只凭一个词根义就互相套。',SPIKE+[['spike + -ing → spiking','具体句中的骤增、加料、扣球等动作过程']],
 'spiking demand 突增的需求；spiking the ball 扣球；drink spiking 往饮料中偷偷加料。',
 'temperatures are spiking；practise spiking 练习扣球。',
 'spiking the ball 在排球里是扣球，throwing the ball 是扔球；词义已跟运动场景结合，不必逐字翻成给球装尖刺。',
 ('Temperatures are spiking across the region.','整个地区的气温正在猛增。'),('The players spent the morning practising spiking.','队员们上午一直在练扣球。'),sources=S('spiking','spike'))
W('spiky','/ˈspaɪki/','有尖刺、尖突的；头发竖成尖束的；说话态度尖锐的',
 '仙人掌扎手的尖刺、头发竖起来的一束束尖，都是 spiky；人说话句句带刺，也能用它形容。',
 'spike 名词去 e 加 -y，写满是尖突或像尖刺一样的性质。现代态度义用带刺画面理解，不把它说成一个新的人物后缀。',SPIKE+[['spike + -y → spiky','有尖突，或态度像尖刺般扎人']],
 'spiky hair 尖束头发；spiky leaves 带尖刺的叶子；a spiky response 尖锐的回应。',
 'a spiky plant；a rather spiky character 个性有点带刺的人。',
 'spiky 突出一个个尖突，sharp 泛说尖、锋利或敏锐；一把平刃刀很 sharp，却不必是 spiky。',
 ('The plant has stiff, spiky leaves.','这种植物的叶子硬硬的，还带着尖刺。'),('His spiky reply ended the conversation.','他带刺的回答让谈话停了下来。'),sources=S('spiky','spiky'))
W('dives','/daɪvz/','潜入、俯冲〔第三人称单数〕；跳水、潜水、猛跌〔复数〕',
 '一只鸟扎进水里，是 it dives；一天下水好几次，则可以说 several dives。名词、动词的场景同样像一头扎下去。',
 'dive + -s，/v/ 后读 /z/；动词三单和名词复数同形。不要和 divers 潜水者的复数少看一个 r。',DIVE+[['dive + -s → dives','它下潜；多次下潜、俯冲等']],
 'deep dives 深潜，也可比喻深入研究；dives into the water 扎入水中。',
 'two dives a day 每天下潜两次；dives into a book 埋头读书。',
 'dives 是动作或次数，divers 是做动作的人；three dives 是三次下潜，不是三位潜水者。',
 ('The bird dives beneath the surface to catch fish.','那只鸟潜到水面下捕鱼。'),('We made two dives near the reef.','我们在珊瑚礁附近下潜了两次。'),sources=S('dives','dive'))
W('dived','/daɪvd/','潜入、跳入、俯冲了；一头投入了',
 '听到门铃响，他一头扎进衣服堆找外套；人跳进水里，也都可以说 dived。看对象，就知道是真下潜还是形容投入。',
 'dive 去 e 加完整 -ed，/v/ 后读 /d/；规则过去式、过去分词。dove 是常见于北美的后起过去式，过去分词通常仍是 dived。',DIVE+[['dive + -ed → dived','规则过去式、分词，和较后出现的过去式 dove 并存']],
 'dived into the pool 跳进泳池；dived into work 一头投入工作。',
 'dived for cover 猛扑着躲避；have dived 曾经潜过水。',
 'dived 在英美均可用，dove 作过去式尤常见于北美；dove 鸽子读 /dʌv/，并非动词过去式的读音。',
 ('She dived into the pool and swam to the other side.','她跳进泳池，游到了另一边。'),('We have dived here several times before.','我们以前在这里潜过好几次水。'),sources=S('dived','dive'))
W('divers','英 /ˈdaɪvəz/；美 /ˈdaɪvɚz/','潜水者、跳水者〔复数〕；〔旧式〕各种各样的',
 '戴着面镜和气瓶下水的几个人，是 divers。大多数现代句子里，先按“做 dive 的人”理解；旧文本里还有另一种同形词。',
 'diver + -s，读 /z/；内层 dive 去 e 加 -er。另一个旧式 divers 各种各样的来自法语、拉丁 diverse 的材料，并非潜水者变出的形容词。',DIVE+[['dive + -er → diver → divers','多人下潜或跳水；另有独立的旧式 divers 各种各样的']],
 'scuba divers 水肺潜水者；rescue divers 救援潜水员。',
 'experienced divers 有经验的潜水员；a team of divers。',
 'divers 潜水者读 /ˈdaɪvəz/ 等，diverse 多种多样的常重读后一音节；旧式 divers 另有自己的词源线，别都按职业名拆。',
 ('The divers checked their equipment before entering the water.','潜水员下水前检查了装备。'),('Rescue divers searched the area near the bridge.','救援潜水员搜索了桥附近的水域。'),sources=S('divers','diver')+['https://www.etymonline.com/word/divers'])
W('dips','/dɪps/','蘸、低下去〔第三人称单数〕；低处、下降、蘸酱〔复数〕',
 '一只手把画笔在水里蘸一下，是 dips；餐桌上几碗不同蘸酱，也是 dips。酱的名字来自把东西蘸进去这个动作。',
 'dip + -s，/p/ 后读 /s/；动词三单、名词复数同形。名词既可说低处、下降，也可说供蘸食的酱。',DIP+[['dip + -s → dips','它蘸、下降；多个低处、下降段或多种蘸酱']],
 'dips in the road 道路低洼处；a selection of dips 几种蘸酱。',
 'dips a brush in water；small dips in temperature。',
 'dips 可以只是小幅或短时下落，plunges 更容易让人感到突然、深的下降；词本身都不保证下一步趋势。',
 ('He dips the brush in water before changing colours.','他换颜色前先把画笔在水里蘸一下。'),('We served vegetables with three different dips.','我们上了蔬菜，配三种不同的蘸酱。'),sources=S('dips','dip'))
W('dipping','/ˈdɪpɪŋ/','正在蘸、浸一下、下降；供蘸用的',
 '饼干一头轻轻进茶里再拿出来，是 dipping；dipping sauce 则是用来让食物蘸着吃的酱。',
 'dip 双写 p 加 -ing，保留短元音词基的常见拼写模式。现代可说动作，也可放在 sauce 等名词前说明用途。',DIP+[['dip + -ing → dipping','蘸、短暂浸入或下降的过程；供蘸用的修饰']],
 'dipping sauce 蘸酱；dipping into a book 随手翻读书中几处。',
 'dipping below zero 降到零度以下；dipping bread in oil。',
 'dip into a book 常是选读、翻看几处；dive into a book 常更像一头投入阅读，投入程度的画面不同。',
 ('She was dipping bread into olive oil.','她正拿面包蘸橄榄油。'),('We made a spicy dipping sauce for the dumplings.','我们给饺子调了一碗辣蘸酱。'),sources=S('dipping','dip'))
W('slouchy','/ˈslaʊtʃi/','姿态松垮的；衣物宽松垂搭的',
 '宽针织衫软软地垂在身上，没撑出利落轮廓，就很 slouchy。它可以是刻意选择的休闲风格，不是在说穿衣者懒。',
 'slouch + -y。slouch 较早有人物名词，远源未定、可能联系北欧松垮材料；slouchy 写相应姿态或衣物性质。',
 [['旧 slouch 懒散人物、松垮材料','更远来源未定，不只由现代姿态动词临时产生'],['slouch + -y → slouchy','倾向松垮、垂搭的性质']],
 'a slouchy sweater 宽松垂搭的毛衣；a slouchy posture 松垮的姿势。',
 'a slouchy bag 软塌垂搭的包；slouchy boots 软筒靴。',
 'slouchy sweater 可形容设计风格，sloppy work 则批评工作马虎；别把外观的松垮直接当成人的能力评价。',
 ('She wore a slouchy sweater over her jeans.','她穿着宽松垂搭的毛衣，配一条牛仔裤。'),('The soft leather gave the bag a slouchy shape.','柔软的皮革让包呈现软塌垂搭的形状。'),sources=S('slouchy','slouchy'))
W('saggy','/ˈsæɡi/','松垂、下陷、松垮的',
 '旧沙发坐垫撑不住，中间塌下去；袜子弹力没了，松松往下堆，都像 saggy。看的是失去支撑后的外观。',
 'sag 名词 + -y，双写 g；sag 的较早来源有北欧、低地德语等不同分析，现代形容词这层构词清楚。',
 [['sag 动词、名词：下陷、松垂','较早借入路线未全定'],['sag + -y → saggy','容易松垂，或已松垮下陷的性质']],
 'a saggy sofa 下陷的沙发；saggy socks 松垮的袜子。',
 'saggy cushions；saggy fabric 松垂的布料。',
 'saggy 强调撑不住、向下塌，loose 只说不紧；一件宽松新衣服不一定已经松垂变形。',
 ('The old sofa was too saggy to sit on comfortably.','旧沙发塌得太厉害，坐着不舒服。'),('He replaced his saggy socks with a new pair.','他把松垮的袜子换成了一双新的。'),sources=S('saggy','saggy'))
W('slinky','/ˈslɪŋki/','贴身柔顺、显曲线的；动作柔滑的',
 '薄软衣料顺着身体曲线垂下来，走路时线条流畅，这种裙子可以叫 slinky。它不是简单说衣服“偷偷摸摸”。',
 'slink 与 -y 相接，较早有瘦长、松垂等义，后来常用于人、衣物的修长柔顺曲线。大写 Slinky 的弹簧玩具名称是后来的专名用途。',
 [['slink 的旧移动、瘦长等材料 + -y','早有瘦长、松垂的相应性质义'],['现代服装、动作中的 slinky','贴身流线、曲线柔顺；并非所有义都只是偷偷溜走']],
 'a slinky dress 贴身柔顺的连衣裙；slinky fabric 柔软贴身的布料。',
 'a slinky evening gown；a slinky movement 柔滑的动作。',
 'slinky 常带柔顺、显曲线的感觉，baggy 是宽大松垮；同为软衣料也可能做成完全不同的轮廓。',
 ('She chose a slinky black dress for the evening.','她为晚间活动选了一条柔顺贴身的黑裙子。'),('The slinky fabric followed the shape of the body.','柔软贴身的布料顺着身体曲线垂落。'),sources=S('slinky','slinky'))
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_zgz',ROOTS,WORDS)
 extend_lessons()
