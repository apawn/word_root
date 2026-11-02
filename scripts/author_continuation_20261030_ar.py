"""Smoke and heat: physical scenes and the figurative uses people actually meet."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
SM=[['古英语 smoca、smocian 等 → 中古英语 smoke、smoken','烟；冒烟'],['现代 smoke','烟；吸烟；以烟熏制等用法']]
def S(f,m):return SM+[[f,m]]
W('smoke','英 /sməʊk/；美 /smoʊk/','烟；冒烟；吸烟；烟熏',
 '火里飘出的烟是起点；人吸烟、食物用烟熏、机器冒烟，都要靠对象分清动作。',
 '接古英语 smoca 名词和 smocian 动词等相关旧形。吸烟、熏食品是后来的专门用法，不要把所有动词例句都读成抽烟。',SM,
 'smoke rises 烟升起，smoke a cigarette 吸烟，smoke fish 熏鱼，go up in smoke 化为乌有。',
 'smoke rises；smoke a cigarette；smoke fish；go up in smoke。',
 'smoke 燃烧等产生的烟；steam 常是蒸汽、可见水雾的日常叫法；fog 雾。看到白色一团不能只凭颜色定词。',
 ('Smoke was rising from the chimney.','烟正从烟囱里升起。'),('The engine began to smoke on the hill.','发动机上坡时开始冒烟。'),sources=['https://www.etymonline.com/word/smoke','https://en.wiktionary.org/wiki/smoke#English'])
W('smoking','英 /ˈsməʊkɪŋ/；美 /ˈsmoʊkɪŋ/','吸烟；冒烟、烟熏；正在冒烟的',
 '把冒烟、吸烟当作活动；形容东西时也可以说它正在冒烟，不必然是人在抽。',
 'smoke 去末尾 e + -ing；相关分词、活动名词有中古英语及更旧形式。吸烟义随 tobacco 用法专门化。',S('smoke + -ing → smoking','冒烟、烟熏；吸烟活动及分词用法'),
 'No smoking. 禁止吸烟；a smoking chimney 冒烟烟囱。a smoking gun 比喻确凿证据，借刚开过火的枪的形象。',
 'No smoking；quit smoking；a smoking chimney；a smoking gun。',
 'smoking 是活动或分词，smoker 是吸烟者、烟熏设备；smoking gun 常讲证据，未必在讨论真实枪。',
 ('Smoking is not allowed inside the building.','楼内不允许吸烟。'),('The report did not contain the smoking gun that reporters expected.','报告里没有记者们期待的那种确凿证据。'))
W('smoked','英 /sməʊkt/；美 /smoʊkt/','烟熏的；熏黑、烟色的；smoke 的过去式、分词',
 '三文鱼是用烟熏过，玻璃则可做出暗暗的烟色；对象决定是哪种处理效果。',
 'smoke + -ed，中古英语已有同族分词。这里 -ed 在 /k/ 后读 /t/，不多加一个完整音节。',S('smoke + -ed → smoked','经历烟熏；形成烟色、熏黑外观'),
 'smoked salmon 烟熏三文鱼，smoked cheese 烟熏奶酪，smoked glass 烟色玻璃。',
 'smoked salmon；smoked cheese；smoked glass。',
 'smoked 常说被熏处理过，smoky 常说有烟、带烟味；smoked fish 与 a smoky room 着眼点不同。',
 ('The sandwich contains smoked salmon and cucumber.','三明治里有烟熏三文鱼和黄瓜。'),('The lamp has a shade made of smoked glass.','这盏灯的灯罩由烟色玻璃制成。'))
W('smoker','英 /ˈsməʊkə/；美 /ˈsmoʊkər/','吸烟者；烟熏设备',
 '做 smoke 动作的人可叫 smoker；用烟熏食物的设备也能用同一个执行者后缀。',
 'smoke + -er。-er 可指人，也可指做某事的器具，因此别把食谱里的 smoker 一概看成人。',S('smoke + -er → smoker','吸烟者；执行烟熏的设备'),
 'a heavy smoker 烟瘾大的人，a former smoker 曾吸烟的人，a food smoker 食品烟熏设备。',
 'a heavy smoker；a former smoker；a food smoker。',
 'smoker 人或器具，smoking 活动，smoky 有烟的；换后缀后，句中承担的角色不同。',
 ('The survey asked whether participants were smokers.','调查询问参与者是否吸烟。'),('He cooked the fish in an outdoor smoker.','他用室外烟熏设备制作了鱼。'))
W('smoky','英 /ˈsməʊki/；美 /ˈsmoʊki/','烟雾弥漫的；有烟味的；烟色、低沉沙哑的',
 '房间里飘着烟，食物里有熏香，颜色或声音也可借烟的朦胧、低暗感觉形容。',
 'smoke + -y，通常去末尾 e。中古英语已有同族形容词，后有味道、颜色、嗓音等专门用法。',S('smoke + -y → smoky','有烟、像烟；烟味、烟色及嗓音比喻'),
 'a smoky room 烟雾弥漫的房间，a smoky flavour 烟熏味，smoky eyes 烟熏眼妆。',
 'a smoky room；a smoky flavour；a smoky voice。',
 'smoky 有烟或烟味，smoked 经烟熏处理；smokeless 少烟、无烟。smoky 的常规拼写没有词基末尾 e。',
 ('We left the smoky room and went outside.','我们离开烟雾弥漫的房间，走到外面。'),('The cheese has a rich smoky flavour.','这块奶酪有浓郁的烟熏味。'))
W('smokeless','英 /ˈsməʊkləs/；美 /ˈsmoʊkləs/','无烟的；少烟的',
 '关注的是使用、燃烧时看得到的烟很少或没有；不是说东西完全不产生其他排放。',
 'smoke + -less，-less 表缺少、没有。工业、商品名称里常按可见烟量使用，不能由词形推断所有性质。',S('smoke + -less → smokeless','缺少可见烟；少烟或无烟'),
 'smokeless fuel 无烟燃料，a smokeless stove 少烟炉具。具体产品含义要看所指类别。',
 'smokeless fuel；a smokeless stove；smokeless combustion。',
 'smokeless 少烟、无烟不等于 odourless 无味；看不见烟仍可有气味，两个感官指标不同。',
 ('The stove was designed to burn smokeless fuel.','这台炉子设计用于燃烧无烟燃料。'),('The brochure describes it as a smokeless outdoor stove.','宣传册把它称作少烟户外炉具。'))
W('smokestack','英 /ˈsməʊkstæk/；美 /ˈsmoʊkstæk/','大烟囱；工厂、轮船的排烟筒',
 '工厂、船上高高伸出的排烟筒；stack 在这里是高筒、烟囱，不是把烟堆成一摞。',
 'smoke + stack 烟囱、高直立构件。还可借指传统重工业的形象，如 smokestack industries。',S('smoke + stack → smokestack','排烟的大烟囱；引申传统重工业形象'),
 'a factory smokestack 工厂烟囱，smokestack industries 传统重工业。',
 'a factory smokestack；a tall smokestack；smokestack industries。',
 'smokestack 通常让人想到工业、轮船大排烟筒；chimney 范围更广，也常用于住宅。',
 ('The factory’s smokestack rose above the town.','工厂烟囱高高耸立在小镇上方。'),('The old ship had two tall smokestacks.','那艘老船有两根高烟囱。'))
W('smog','英 /smɒɡ/；美 /smɑːɡ/','烟雾、烟霾；污染性雾霾',
 '空气像雾一样灰蒙蒙，还混着污染；名字把烟和雾压进了一个短词。',
 'smoke + fog 的混成词，20世纪初用于烟与雾混合的污染。现代 smog 也涵盖其他形成机制，不一定现场真有 fog 才能用。',S('smoke + fog → smog〔混成〕','烟与雾的名称组合 → 污染性烟霾'),
 'thick smog 浓重烟霾，a blanket of smog 笼罩的烟霾，photochemical smog 光化学烟雾。',
 'thick smog；a blanket of smog；photochemical smog。',
 'fog 是雾，smog 强调污染性烟霾；混成来源是历史命名线索，不是今天每种烟霾都必须满足烟加天然雾。',
 ('A layer of smog hung over the city.','一层烟霾笼罩着城市。'),('The mountains disappeared behind the smog.','群山消失在烟霾后面。'),sources=['https://www.etymonline.com/word/smog','https://en.wiktionary.org/wiki/smog#English'])
R('B3114','烟、冒烟、吸烟、烟熏；烟色形象与污染混成','SMOKE：烟飘出来，再按对象看吸入、熏制或遮挡','smoke → smoking、smoked、smoker、smoky、smokeless；smokestack 设备与 smog 混成分讲；smokescreen、smokehouse 既有共享。',
 '不要看到 smoke 家族就一律理解成吸烟。冒烟机器、熏制食品、迷惑视线和空气污染是不同场景。',
 'smoke + -ing/-ed/-er/-y/-less；smoke + stack/screen/house；smoke + fog → smog。',
 [['基本烟与活动','smoke · smoking'],['处理、执行者与性质','smoked · smoker · smoky · smokeless'],['设施、遮挡和污染','smokestack · smokehouse · smokescreen · smog']],
 'smoked 经熏制、smoky 有烟味或烟；smokeless 不等于无味；smoking gun 确凿证据；smog 不等于普通雾。',
 'The smoker gave the fish a smoky flavour, while the room filled with smoke.\n\n烟熏设备给鱼增添了熏香，房间里则飘起了烟。',
 'smoke smoking smoked smoker smoky smokeless smokestack smokehouse smokescreen smog')
HE=[['古英语 hǣtu〔名词〕、hǣtan〔动词〕→ heat','热、热情；使热、变热，与 hot 同族'],['现代 heat','热量、热度；加热；激烈情绪、压力及比赛分组等用法']]
def H(f,m):return HE+[[f,m]]
W('heat','/hiːt/','热、热量；压力、激烈情绪；加热；预赛一组',
 '手靠近炉子感到热；争论火气上来、压力逼人，也借热来讲。比赛中的一组 heat 是另一个固定用法。',
 '本族名词与动词分别有古英语旧形，与 hot 同族。比赛分组义可能经强烈的一轮努力、马匹热身跑等发展，不能编成天气热才叫预赛。',HE,
 'turn down the heat 调低火力，heat the soup 热汤，in the heat of the moment 一时激动；win your heat 赢得自己那组预赛。',
 'turn down the heat；heat the soup；in the heat of the moment；a qualifying heat。',
 'heat 名词热、动词加热，hot 形容词热的。heat 的比赛义并不规定每一种比赛制度都一样。',
 ('Heat the soup gently for a few minutes.','把汤用小火热几分钟。'),('She won her heat and reached the final.','她赢得了所在预赛小组的比赛，进入决赛。'),sources=['https://www.etymonline.com/word/heat','https://en.wiktionary.org/wiki/heat#English'])
W('heating','/ˈhiːtɪŋ/','加热；供暖；供暖系统',
 '把东西弄热的过程；家里说 the heating，往往就是让整间屋子暖起来的系统。',
 'heat + -ing，中古英语已有活动名词。供暖语境常由活动转指设备、系统，不必每次加 system 才成立。',H('heat + -ing → heating','加热过程 → 供暖及系统'),
 'central heating 中央供暖，turn on the heating 开暖气，heating costs 取暖费用。',
 'central heating；turn on the heating；heating costs。',
 'heating 系统或活动，heater 某件加热器；The heating is broken 可能是整套供暖出了问题。',
 ('We turned on the heating when the evenings became cold.','晚上冷起来后，我们开了暖气。'),('The new windows helped reduce heating costs.','新窗户帮助降低了取暖费用。'))
W('heater','英 /ˈhiːtə/；美 /ˈhiːtər/','加热器；取暖器',
 '专门把水、空气或其他东西加热的设备；前面的词通常说明热什么。',
 'heat + -er，后缀在这里形成器具名。不是凡是做饭、让人暖心的人都自然叫 heater。',H('heat + -er → heater','执行加热的器具'),
 'a water heater 热水器，an electric heater 电暖器，a space heater 局部取暖器。',
 'a water heater；an electric heater；a space heater。',
 'heater 通常指具体设备，heating 常指加热活动或供暖系统；hot water 是热水本身。',
 ('The water heater is in the cupboard.','热水器在柜子里。'),('He switched off the electric heater before leaving.','离开前，他关掉了电暖器。'))
W('heated','/ˈhiːtɪd/','加热的；激烈、情绪激动的',
 '座椅被加热会暖，讨论被情绪推高就会火热、激烈；两个场景共用热起来的形象。',
 'heat + -ed，/t/ 后 -ed 读 /ɪd/。分词形容词既保留实际受热，也发展出激动、争论激烈的用法。',H('heat + -ed → heated','受热、被加热；情绪激动、讨论激烈'),
 'heated seats 加热座椅，a heated debate 激烈辩论，a heated exchange 激烈交锋。',
 'heated seats；a heated debate；a heated exchange。',
 'heated debate 说情绪、交锋激烈；hot topic 热门话题不必人人吵起来。heated 不是简单比 hot 温度更高。',
 ('The car has heated seats.','这辆车有加热座椅。'),('The proposal led to a heated debate.','提议引发了激烈辩论。'))
W('heatwave','/ˈhiːtweɪv/','热浪；持续异常炎热天气',
 '炎热像一波天气过程持续压过来，不是短短一秒有热气扑脸。',
 'heat + wave 波、波次。这里 wave 借连续出现、扩展的一波，不是水面必须真有波浪。',H('heat + wave → heatwave','一波持续的异常炎热天气'),
 'a summer heatwave 夏季热浪，a prolonged heatwave 持续热浪；也常写成两词 heat wave。',
 'a summer heatwave；a prolonged heatwave；during the heatwave。',
 'heatwave 是一段炎热天气过程，a wave of heat 可更直观说一阵热气；具体气象判定标准因地区而异。',
 ('The heatwave lasted for more than a week.','这轮热浪持续了一周多。'),('The park opened earlier during the heatwave.','热浪期间，公园提早开放。'))
W('overheat','英 /ˌəʊvəˈhiːt/；美 /ˌoʊvərˈhiːt/','过热；使过热',
 '热过了适合的程度，设备可能开始出问题；人或经济也可借这个过头的形象表达。',
 'over- 过量 + heat，中古英语已有 overheten 等相应形式。可不及物自己过热，也可及物把某物弄过热。',H('over- + heat → overheat','加热过量、温度过高；后有发展过猛比喻'),
 'the engine overheats 发动机过热，an overheated room 过热的房间，an overheated economy 过热经济。',
 'an engine overheats；avoid overheating；an overheated room。',
 'overheat 是过热，preheat 是提前加热，reheat 是再次加热；三个前缀分别讲程度、时间、重复。',
 ('The laptop overheated during the long video call.','长时间视频通话时，笔记本电脑过热了。'),('Do not overheat the sauce.','别把酱汁加热过头。'))
W('reheat','/ˌriːˈhiːt/','重新加热；把熟食热一下',
 '东西已经热过、做过，现在凉了再热；不是从生到熟的整个过程都叫 reheat。',
 're- 再次 + heat，明确重复加热。日常多用于已经做好的饭菜。',H('re- + heat → reheat','再次加热、重新热食物'),
 'reheat the soup 重新热汤，reheat leftovers 热剩饭菜。',
 'reheat the soup；reheat leftovers；reheat in the oven。',
 'reheat 再热，preheat 预先热设备；preheat the oven 与 reheat the food 的对象和时间关系不同。',
 ('I reheated the soup for lunch.','我把汤重新热了，当午饭喝。'),('The instructions explain how to reheat the pie.','说明写了如何重新加热这块派。'))
R('B3332','热与加热；供暖、激烈情绪和重复程度','HEAT：热起来，先分过程、设备、情绪和比赛固定义','heat → heating、heater、heated；preheat、reheat、overheat 对照前缀，heatwave 单讲天气；preheat 共享既有词。',
 '热与 hot 本族相连。比喻能帮理解，比赛 heat 的具体历史仍保留不确定性，不按预赛天气猜源。',
 'heat + -ing/-er/-ed；pre-/re-/over- + heat；heat + wave。',
 [['过程、系统、设备和状态','heat · heating · heater · heated'],['提前、重复和过量','preheat · reheat · overheat'],['持续炎热','heatwave']],
 'heat 动词名词、hot 形容词；heating 系统、heater 器具；heated debate 激烈不等于热门；三个前缀分清。',
 'Preheat the oven, reheat the pie, and avoid overheating it.\n\n先预热烤箱，再把派热一下，别热过头。',
 'heat heating heater heated preheat reheat overheat heatwave')
if __name__=='__main__':save('continuation_20261030_ar',ROOTS,WORDS)
