"""Butt, platform and wheel: separate homographs and group useful extensions."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
B=[['日耳曼、法语末端词相互影响 → butt〔端头〕','粗端、末端；与 buttock 等的历史关系有不同分析'],['法语 but〔目标〕→ butt〔笑柄〕','靶、目标 → 被嘲笑的对象'],['法语 buter、boter → butt〔顶撞〕','推、撞 → 用头顶、撞；插话'],['古法语 bot 等 → butt〔大桶〕','酒桶等容器名；不从屁股变来']]
W('butt','/bʌt/','屁股〔口语〕；粗端、烟头；嘲笑对象；顶撞；大桶〔另来源〕',
 'cigarette butt 是抽剩的末端，the butt of a joke 是笑话瞄准的对象，butt in 是硬挤进谈话；同拼写里有几条历史，不能都靠屁股解释。',
 '末端义有日耳曼、法语相关形式交织；身体义可能联系粗端或 buttock；目标义接法语 but，顶撞动词接 buter 等。桶名另有法语、拉丁容器路径。',B,
 'a cigarette butt 烟头，the butt of a joke 笑柄，butt in 插话，sit on your butt 坐着不动〔口语〕，a butt joint 平接接头。',
 'a cigarette butt；the butt of a joke；butt in；a butt joint。',
 'butt 与 but 同音；butter 黄油不是 butt + -er，halibut 的鱼名部分也另看扁鱼词，不能把所有字母 butt 都归屁股。',
 ('Please do not butt in while she is speaking.','她说话时请别插嘴。'),('He was tired of being the butt of every joke.','每个笑话都拿他取笑，他受够了。'),('A cigarette butt lay beside the bin.','垃圾桶旁躺着一个烟头。'),
 sources=['https://en.wiktionary.org/wiki/butt#English','https://www.etymonline.com/word/butt'])
W('buttock','/ˈbʌtək/','臀部的一侧；buttocks 臀部、屁股',
 '单数常说左右臀部的一侧，复数 buttocks 说两侧合起来的臀部；比口语 butt 更像中性的身体部位名称。',
 '中古英语 buttok，通常联系更早 buttuc 末端、小块之类形式，带旧小称后缀 -ock。不能把它编成 butt + rock 石头。',B[:1]+[['旧 buttuc、buttok 等 → buttock','末端、小块词形 → 身体臀部一侧'],['常用复数 buttocks','左右两侧的臀部']],
 'the left buttock 左侧臀部，the buttock muscles 臀部肌肉，both buttocks 两侧臀部。',
 'the left buttock；the buttock muscles；both buttocks。',
 'buttock 单侧、buttocks 常整体；butt 口语更宽泛，臀部并不等于所有后腰、后背区域。',
 ('The diagram labelled the buttock muscles.','示意图标出了臀部肌肉。'),('The costume had padding over both buttocks.','服装在两侧臀部位置都有衬垫。'))
W('butthole','英 /ˈbʌthəʊl/；美 /ˈbʌthoʊl/','肛门〔粗俗口语〕；讨厌的人〔骂语〕',
 '字面是屁股上的开口；骂人时又把这个部位名丢给讨厌的人，语气粗鲁，不能当普通称呼。',
 'butt 屁股 + hole 洞、开口；从身体部位再引申侮辱人物。不是 -hole 在所有组合里都自动骂人。',B[:1]+[['butt + hole → butthole','肛门的粗俗说法'],['部位名的辱骂用法','令人讨厌的人']],
 'the word butthole butthole 这个词，call someone a butthole 用粗俗词骂人，a crude insult 粗俗辱骂〔用法说明〕。',
 'call someone a butthole；a crude insult；use butthole as an insult。',
 '正式身体部位名用 anus；butthole 也可侮辱人，不能只按解剖意思翻译所有对话。',
 ('The glossary marked butthole as vulgar slang.','词汇表把 butthole 标为粗俗俚语。'),('The character calls his rival a butthole.','这个角色用 butthole 辱骂对手。'))
W('butthead','/ˈbʌthed/','讨厌鬼、蠢货〔粗鲁骂语〕',
 '把对方贬作很烦、很蠢的人，是一种粗鲁口语；不是身体真的长着某种形状的头。',
 'butt 屁股 + head 头，组合为辱骂人物名，和 headbutt 的组成顺序、作用完全不同。',B[:1]+[['butt + head → butthead','贬低人物的粗鲁称呼']],
 'call someone a butthead 骂某人讨厌鬼，stop being a butthead 别这么讨厌〔粗鲁〕，the insult butthead 辱骂词 butthead。',
 'call someone a butthead；stop being a butthead；a rude insult。',
 'butthead 骂人名词，headbutt 头撞动作；成分换序后不是同一个意思。',
 ('The subtitle translated butthead as a rude insult.','字幕把 butthead 翻成一句粗鲁骂语。'),('The brothers called each other buttheads in the comedy.','喜剧里的兄弟俩互骂讨厌鬼。'))
W('headbutt','/ˈhedbʌt/','头撞、用头猛撞',
 'head 给出用哪个部位，butt 是顶撞动作：用头去撞。可以名词一次头撞，也可作动词。',
 'head 头 + butt 顶撞，这里不接屁股义；词序与 butthead 骂语相反，意思不能互换。',B[2:3]+[['head + butt〔顶撞〕→ headbutt','以头部进行顶撞；一次头撞']],
 'a headbutt 一次头撞，headbutt the door 用头撞门，an accidental headbutt 意外头撞。',
 'a headbutt；an accidental headbutt；headbutt the door。',
 'headbutt 动作，butthead 侮辱人的名称；两词不是同一个动作的英美不同排列。',
 ('The referee stopped the match after the headbutt.','头撞发生后，裁判叫停了比赛。'),('In the cartoon, the goat headbutts the gate.','动画里，山羊用头顶撞大门。'))
W('abut','/əˈbʌt/','邻接、边缘相接；紧挨着',
 '两块地、两段墙的边碰到一起，就是 abut；只说接壤、接触，不要求大面积重叠。',
 '经法语 aboter、abouter、abuter 等进入英语，与朝向、末端相接、推抵的材料有关。现代可联想 a- 向 + butt 端头、接触，不是英语 a + but 连词。',B[2:3]+[['法语 a-、bout、boter 等相关接触词形 → abut','端部相接、边界接壤']],
 'abut a field 与田地相接，abut on a road 临着道路，two adjoining walls abut 两堵墙相接。',
 'abut a field；abut on；abut against。',
 'abut 相接、接壤，overlap 重叠范围；abut 的过去式 abutted 双写 t，不把它当名词 about 的误拼。',
 ('The garden abuts a small field.','花园与一小片田地相接。'),('The two walls abut at the corner.','两堵墙在角落相接。'),
 sources=['https://en.wiktionary.org/wiki/abut#English','https://www.etymonline.com/word/abut'])
R('B3890','末端、目标、顶撞分支分开，身体义再看语气','BUTT：同拼写有几条路，末端和撞击不能全译成屁股','butt → buttock、butthole、butthead、butthurt；headbutt 接顶撞；abut 接边缘相接。',
 '身体词有中性、粗俗、骂语区别；butter 黄油不是屁股人物后缀，鱼名 halibut 也另看扁鱼材料。',
 '日耳曼与法语末端、目标词 → butt 相应名词；buter 等 → 顶撞；buttuc → buttock；head + butt；法语相接词形 → abut。',
 [['身体与口语评价','butt · buttock · butthole · butthead · butthurt'],['顶撞和接壤','headbutt · abut']],
 'butt/but 同音；butthead/headbutt 词序意义不同；abut/overlap 相接重叠；butter 不按 butt+-er。',
 'The garden abuts the wall; the goat gave the gate a headbutt.\n\n花园紧挨着墙；山羊用头撞了大门一下。','butt buttock butthole butthead butthurt headbutt abut')
ROOTS[-1]['exclude']['butter']='黄油接古英语 butere 等，更早经拉丁希腊奶酪词族，不是 butt 加人物 -er。'
ROOTS[-1]['exclude']['halibut']='鱼名后半接日耳曼扁鱼名称，不能直接当现代屁股 butt 的合成词。'
F=[['法语 plate-forme 等 → platform','平的形态、平台 → 台面、站台、活动或软件基础'],['游戏语境的派生','platformer 平台跳跃游戏；platforming 平台跳跃活动']]
W('platformer','英 /ˈplætfɔːmə/；美 /ˈplætfɔːrmər/','平台跳跃游戏',
 '玩家在不同高低的平台之间跳跃、移动，这是游戏类型名称；-er 在这里不是站台工作人员。',
 'platform 平台 + -er，指以平台移动、跳跃为核心机制的一类游戏。',F,
 'a classic platformer 经典平台跳跃游戏，a puzzle platformer 解谜平台游戏，play a platformer 玩平台游戏。',
 'a classic platformer；a puzzle platformer；play a platformer。',
 'platformer 具体游戏类型，platform 软件平台、站台等基础词范围更广；不是所有在游戏平台上运行的游戏都叫 platformer。',
 ('The studio released a colourful platformer.','工作室推出了一款色彩鲜艳的平台跳跃游戏。'),('The puzzle platformer combines jumping with problem solving.','这款解谜平台游戏把跳跃与解题结合起来。'))
W('platforming','英 /ˈplætfɔːmɪŋ/；美 /ˈplætfɔːrmɪŋ/','平台跳跃操作、平台跳跃玩法；提供平台〔另语境〕',
 '游戏里一跳一落、在平台间找路线，这部分动作、玩法叫 platforming；它可以是一款游戏中的某段内容。',
 'platform + -ing；游戏义围绕在平台间移动。其他语境也可来自 platform 作动词提供发声、活动平台，不能只看后缀锁死一种含义。',F[:1]+[['platform + -ing → platforming','在平台间移动的玩法；按语境也有提供平台行为']],
 'precise platforming 精准平台跳跃操作，platforming sections 平台跳跃段落，platforming challenges 平台跳跃挑战。',
 'platforming sections；precise platforming；platforming challenges。',
 'platformer 一款游戏或类型，platforming 操作、玩法部分；非游戏文章需看是否指提供平台。',
 ('The game mixes puzzles with platforming.','游戏把解谜与平台跳跃玩法混在一起。'),('The final level has several difficult platforming sections.','最后一关有几段困难的平台跳跃。'))
R('B3156','平台作为站立、活动或运行的基础','PLATFORM：先有承托的台，再借给活动和软件基础','platform → platformer、platforming，游戏人物跳来跳去的台保留具体画面。',
 '站台、政策纲领、软件平台按场景理解；platformer 不是所有运行在平台上的程序。',
 'plate-forme 等 → platform；platform + -er/-ing。',
 [['基础平台与游戏玩法','platform · platformer · platforming']],
 'platformer 类型和作品；platforming 玩法；提供发声平台是另一动词语境。',
 'The platformer includes some demanding platforming.\n\n这款平台游戏包含一些操作要求较高的跳跃段落。','platform platformer platforming')
H=[['古英语 hwēol 等 → 中古英语 whel → wheel','轮子；更早重叠构词通常联系转、转动'],['现代名词动词扩展','轮转、车轮；方向盘和掌控；推着带轮器具移动'],['组合按部位、数量、功能命名','wheelbase 轴距；wheelbarrow 手推车；cartwheel 车轮与侧手翻']]
W('wheel','/wiːl/，部分口音保留 /hw/','轮子；方向盘；转动、转身；推着带轮物移动',
 '轮子转让车走，握方向盘的人控制方向；wheel a suitcase 则是让行李箱靠轮子走，不必把它高高举起来。',
 '接古英语 hwēol、hweogol 等，经中古英语到 wheel；较早重叠词形通常联系转动。名词再形成旋转、推轮行进的动词。',H,
 'a steering wheel 方向盘，behind the wheel 驾驶，reinvent the wheel 重复造轮子，wheel a suitcase 推着行李箱走。',
 'a steering wheel；behind the wheel；reinvent the wheel；wheel a suitcase。',
 'wheel 轮子，tyre/tire 轮胎只是车轮外部相关部件，不是同一对象；wheel 可动词，不只名词。',
 ('She wheeled her suitcase into the station.','她推着行李箱进了车站。'),('He sat behind the wheel and waited.','他坐在驾驶位上等待。'))
W('wheeler','英 /ˈwiːlə/；美 /ˈwiːlər/','操作轮具的人；有某数量车轮的车辆〔多见组合〕',
 'two-wheeler 是两轮车，four-wheeler 是四轮车等；这里 -er 把轮数特征接成车辆名称，不是在数四个造轮工人。',
 'wheel + -er，有人物、器具特征等不同构词用途；中古英语已有 whelere。现代车辆义常带数量词。',H[:1]+[['wheel + -er → wheeler','轮具操作者；按组合指某种轮数车辆']],
 'a two-wheeler 两轮车，a three-wheeler 三轮车，an eighteen-wheeler 大型多轮卡车〔美式常见〕。',
 'a two-wheeler；a three-wheeler；an eighteen-wheeler。',
 'wheeler 单独使用较受场景限制，常连前面数量一起记；不能只按 -er 全部译成骑车的人。',
 ('The company makes electric two-wheelers.','公司制造电动两轮车。'),('A three-wheeler waited outside the market.','一辆三轮车停在市场外等候。'))
W('wheelie','/ˈwiːli/','翘前轮行驶的动作',
 '前轮翘起，主要靠后轮继续前进，画面是一边抬、一边滚；这是动作名，不是一个很小的轮子。',
 'wheel + -ie，口语名词；词尾在这里形成动作名称，不保证是人物或小称。',H[:1]+[['wheel + -ie → wheelie','翘起前轮、后轮行进的动作名']],
 'do a wheelie 做翘前轮动作，pop a wheelie 翘起前轮，a bicycle wheelie 自行车翘轮动作。',
 'do a wheelie；pop a wheelie；a bicycle wheelie。',
 'wheelie 动作，wheeler 常按组合指车辆；小轮一般说 a small wheel，不能拿 -ie 作万能小称。',
 ('The video showed a rider doing a wheelie.','视频里，一位骑手正做翘前轮动作。'),('The crowd cheered at the final wheelie.','最后那个翘轮动作赢得了观众欢呼。'))
W('wheelbarrow','英 /ˈwiːlbærəʊ/；美 /ˈwiːlbæroʊ/','独轮手推车、园艺手推车',
 '前方有轮、后方有把手，人握把抬起后端推着走；常见独轮款，也有其他轮数设计。',
 'wheel 轮子 + barrow 搬运车、搬运架；中古英语已有 whelbarwe。不是 wheel + borrow 借入。',H[:1]+[['wheel + barrow → wheelbarrow','有轮的搬运车、手推车']],
 'push a wheelbarrow 推手推车，a wheelbarrow full of soil 一车土，a garden wheelbarrow 园艺手推车。',
 'push a wheelbarrow；a wheelbarrow full of soil；a garden wheelbarrow。',
 'barrow 搬运车与 borrow 借不是一词；wheelbarrow 常见一轮不等于所有产品严格只有一轮。',
 ('He pushed a wheelbarrow full of soil.','他推着一车土。'),('The gardener left the wheelbarrow by the shed.','园丁把手推车留在工具棚旁。'))
W('wheelbase','/ˈwiːlbeɪs/','轴距',
 '看车身前后两组车轮的轴之间有多远；它量的是前后支承位置，不是整个车长，也不是左右轮宽。',
 'wheel 轮 + base 基础、间距基准，组成车辆几何尺寸名；一般车辆语境指前后轴间距离。',H[:1]+[['wheel + base → wheelbase','车轮轴位置之间的前后距离']],
 'a long wheelbase 长轴距，a short wheelbase 短轴距，the vehicle’s wheelbase 车辆轴距。',
 'a long wheelbase；a short wheelbase；the vehicle’s wheelbase。',
 'wheelbase 轴距，track width 轮距是左右方向概念；overall length 车全长又包含前后悬等部分。',
 ('The brochure lists the car’s wheelbase.','宣传册列出了车的轴距。'),('The two models have different wheelbases.','这两种车型轴距不同。'))
W('cartwheel','英 /ˈkɑːtwiːl/；美 /ˈkɑːrtwiːl/','车轮；侧手翻、做侧手翻',
 '本来是车的轮子；人张开手脚侧着翻过去，四肢像轮辐依次过地，于是这个动作也叫 cartwheel。',
 'cart 车 + wheel 轮，先为实际车轮，后来按轮转外形借给体操动作，再可作动词。',H[:1]+[['cart + wheel → cartwheel','车的轮子'],['轮转形状 → 人体动作','侧手翻；做侧手翻']],
 'do a cartwheel 做侧手翻，turn a cartwheel 翻一个侧手翻，an old cartwheel 旧车轮。',
 'do a cartwheel；turn a cartwheel；an old cartwheel。',
 'cartwheel 侧向翻转动作，wheelie 是车翘前轮行驶；两者都像轮子，却不是同一种技巧。',
 ('The child did a cartwheel on the grass.','孩子在草地上做了一个侧手翻。'),('An old cartwheel hung on the barn wall.','谷仓墙上挂着一个旧车轮。'))
R('B3385','转动的圆轮及其部件、器具和比喻','WHEEL：轮子不停转，交通和动作名称跟着长出来','wheel → wheeler、wheelie；wheelchair、wheelbarrow、wheelbase、flywheel、wheelhouse 按功能部位分；cartwheel 接轮转动作。',
 '轮胎只是轮相关部件，轴距不是车长；wheelie 翘轮与 cartwheel 侧手翻分清，不能见 -wheel 都同一动作。',
 'hwēol 等经中古英语 → wheel；wheel + -er/-ie/chair/barrow/base/house；fly + wheel；cart + wheel。',
 [['基础、车辆称呼与翘轮动作','wheel · wheeler · wheelie'],['器具、部位与尺寸','wheelchair · wheelbarrow · wheelbase · flywheel · wheelhouse'],['车轮到体操动作','cartwheel']],
 'wheel/tyre 轮与胎；wheelbarrow/borrow 搬运车与借；wheelbase/track width 前后左右；cartwheel/wheelie 动作不同。',
 'The wheelbarrow had one wheel, while the cart had four.\n\n这辆手推车有一个轮子，那辆大车则有四个。','wheel wheeler wheelie wheelchair wheelbarrow wheelbase flywheel wheelhouse cartwheel')
if __name__=='__main__':save('continuation_20261030_ep',ROOTS,WORDS)
