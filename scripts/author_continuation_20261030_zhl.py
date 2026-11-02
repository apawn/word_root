"""Putting things off, lingering, idling and lacking energy."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
def S(word,base):
 return ['https://en.wiktionary.org/wiki/'+word+'#English','https://www.etymonline.com/word/'+base]
EXISTING_ROOT_ADDITIONS={
 'C1130':dict(words='procrastinate procrastinates procrastinated procrastinating procrastination procrastinator procrastinators'.split(),label='procrastinate：总把事情推到明天',note='拉丁 pro 向前与 crastinus 明天的组成 procrastinare；英语动词可能由较早名词逆构，也可能接拉丁分词。学习先看动词，不表示英语历史上动词必先于名词。'),
 'B3069':dict(words='linger lingers lingered lingering'.split(),label='linger：拉长停留，迟迟不散',note='linger 经中古英语 lenger、lengen，接古英语 lengan 延长，与 long 同一日耳曼材料；不是直接从拉丁 longus 借来。原有 er 联系反复动作，不是做事者。'),
 'B4269':dict(words='idle idles idled idling idler idlers'.split(),label='idle：闲着，到发动机空转',note='idle 古英语早指空、无用，后来有不工作；英语动词由形容词发展。空转的是机器还在运转，但未带负载工作，不是完全熄火。'),
 'B3979':dict(words='laze lazes lazed lazing lazy'.split(),label='laze：懒洋洋地休息',note='laze 由较早 lazy 逆构，不能因为形式短就认定动词先有。lazy 更远来历未定，有低地德语等近源分析。'),
 'A1697':dict(words='loiter loiterer loiterers'.split(),label='loiterer：逗留不走、闲晃的人',note='loiter 或借自、或近于中古荷兰语 loteren 松动、晃动等材料；现代加完整 -er 表人，再加复数 -s。'),
 'A1740':dict(words='sluggish sluggishly sluggishness'.split(),label='sluggishly：慢吞吞、反应迟钝地',note='sluggish 的 slug 材料早有人懒散义，动物蛞蝓名称后来才发展；不能把形容词的全部历史都说成先看见蛞蝓。'),
 'C0384':dict(words='lethargy lethargic lethargically'.split(),label='lethargy：浑身提不起劲',note='希腊 lethargos 接遗忘与 argos 不活动材料，后者含否定 a 与 ergon 工作的同族材料；经希腊、拉丁语传入英语。lethargic 有自己的借入路线，不只是现代英语 lethargy 换后缀。'),
}
PRO=[['拉丁 pro 向前 + crastinus 明天的 → procrastinare','把事情往明天推；cras 就是明天'],['英语先已有 procrastination；procrastinate 可能逆构或接拉丁分词','现代指拖着该做的事，不只一般改期']]
LINGER=[['古英语 lengan 延长 → 中古英语 lengen、lenger','和 long 的日耳曼材料相连'],['延长停留 → 迟迟不走、一直不散','气味、印象、疑问也能留下不散']]
IDLE=[['古英语 idel 空、无用 → 不做事的 idle','后来也可说机器闲置、不工作'],['形容词 → 动词 idle','耗时间、使闲置，后来还有发动机空转义']]
LAZE=[['lazy 形容词较早，远源未定','有低地德语虚弱、疲倦材料等分析'],['由 lazy 逆构出 laze','现代常说放松、懒洋洋地消磨时间']]
LOITER=[['loiter 或借自、或接近中古荷兰语 loteren 等材料','有松动、晃动等意思；近源分析仍需保留可能性'],['英语闲耗时间、逗留 → loiterer','现代指无明确事情地逗留的人']]
LETH=[['希腊 lethe 遗忘 + argos 不活动的相关材料 → lethargos','像迟钝得没在响应外界，是帮助理解的画面'],['希腊、拉丁语材料 → 英语 lethargy / lethargic','无精打采的状态与相应性质，各有借入路线']]
W('procrastinates','英 /prəˈkræstɪneɪts/；美 /proʊˈkræstəneɪts/','拖着该做的事〔第三人称单数〕',
 '事情知道要做，却总说等会儿、明天再说，是 procrastinates。拖延的是行动，不一定因为不知道怎么做。',
 'procrastinate + -s，/t/ 后读 /s/；拉丁语内部可看到向前与明天的材料，英语这一层只是三单。',PRO+[['procrastinate + -s → procrastinates','他或她把该做的事拖后']],
 'procrastinates over paperwork 拖着不做文书工作；procrastinates until the deadline。',
 'often procrastinates；procrastinates instead of starting。',
 'postpones 可是有安排地改期，procrastinates 通常是在拖着该做的事，常带自我批评。',
 ('He procrastinates until the deadline is only hours away.','他总要拖到截止前只剩几个小时。'),('She procrastinates over paperwork but finishes practical tasks quickly.','她做文书工作爱拖延，动手的任务却完成得很快。'),sources=S('procrastinates','procrastinate'))
W('procrastinated','英 /prəˈkræstɪneɪtɪd/；美 /proʊˈkræstəneɪtɪd/','拖延了；把该做的事拖后了',
 '本来早就可以开始，却一直拖到后来，回头说 procrastinated。这里往往带本来不该拖这么久的感觉。',
 'procrastinate 去 e 加完整 -ed；基础末音 /t/ 后读 /ɪd/，新增一个音节。',PRO+[['procrastinate + -ed → procrastinated','过去曾拖着不做']],
 'procrastinated for weeks 拖延了几周；had procrastinated too long。',
 'procrastinated over the application；procrastinated until Friday。',
 'procrastinated 不等于计划后来才做；任务本来排在周五做，并不自动构成拖延。',
 ('I procrastinated for weeks before starting the application.','开始填申请前，我拖了好几个星期。'),('We procrastinated until the choice became much harder.','我们一直拖着，结果选择变得更难了。'),sources=S('procrastinated','procrastinate'))
W('procrastinating','英 /prəˈkræstɪneɪtɪŋ/；美 /proʊˈkræstəneɪtɪŋ/','正在拖延；拖着该做的事',
 '一边知道报告该写，一边不断整理无关紧要的东西，是 procrastinating。人可能很忙，但重要任务始终没动。',
 'procrastinate 去 e 加 -ing；-ate 中的 /t/ 保留，和过去式的 /ɪd/ 区分。',PRO+[['procrastinate + -ing → procrastinating','拖着行动的过程']],
 'stop procrastinating 停止拖延；procrastinating over a task。',
 'keep procrastinating 一直拖；a way of procrastinating。',
 'being busy 是忙，procrastinating 是重要任务被拖着；两者可以同时发生，不是非忙即闲。',
 ('I was tidying my desk as a way of procrastinating.','我用整理桌子的方式拖着不做正事。'),('Stop procrastinating and write the first sentence.','别拖了，先把第一句话写出来。'),sources=S('procrastinating','procrastinate'))
W('procrastinators','英 /prəˈkræstɪneɪtəz/；美 /proʊˈkræstəneɪtɚz/','爱拖延的人〔复数〕',
 '都说马上开始，却总要等到最后一刻的一群人，可以叫 procrastinators。它描述行动习惯，不表示这些人一定没有能力。',
 'procrastinator + -s，读 /z/；基础人称名词用拉丁式 -or 构成，对应做出拖延动作的人。',PRO+[['procrastinate → procrastinator → procrastinators','拖延，到拖延者，再到多人']],
 'chronic procrastinators 长期爱拖延的人；tips for procrastinators。',
 'a group of procrastinators；help procrastinators get started。',
 'procrastinators 常常有意愿却迟迟不行动，beginners 是新手；熟手也会拖，新手也可立刻开始。',
 ('Many procrastinators find starting harder than continuing.','很多爱拖延的人觉得开始比继续更难。'),('The workshop gives procrastinators a small task to finish first.','工作坊先让爱拖延的人完成一个小任务。'),sources=S('procrastinators','procrastinate'))
W('lingers','英 /ˈlɪŋɡəz/；美 /ˈlɪŋɡɚz/','逗留；迟迟不散、持续存在〔第三人称单数〕',
 '人已经走了，香味还在；争论结束了，疑问还没散，都可以说 lingers。像把结束的边缘往后拉长。',
 'linger + -s，读 /z/；linger 内部的 er 接旧反复动作材料，不是这里新造一个做事者。',LINGER+[['linger + -s → lingers','人或事物继续留着、不散']],
 'the smell lingers 气味不散；doubt lingers 疑虑仍在。',
 'lingers by the door 在门边迟迟不走；the memory lingers。',
 'remains 只是仍在，lingers 更让人感觉时间被拉长、迟迟不散；常用于气味、印象、余波。',
 ('The smell of fresh bread lingers in the kitchen.','厨房里还留着新鲜面包的香味。'),('A sense of unease lingers after the final scene.','最后一幕结束后，不安感仍挥之不去。'),sources=S('lingers','linger'))
W('lingered','英 /ˈlɪŋɡəd/；美 /ˈlɪŋɡɚd/','逗留了；迟迟没有散去',
 '聚会结束，大家还站在门口舍不得走；一句话说完很久还在脑中，都是 lingered。重点是多留了那一段。',
 'linger + 完整 -ed，读 /d/；英式这里不在词尾读 r，不新增 /ɪd/ 音节。',LINGER+[['linger + -ed → lingered','过去延续、逗留了一段时间']],
 'lingered after dinner 饭后逗留；the taste lingered 余味未散。',
 'lingered in her mind 一直留在她心中；lingered by the gate。',
 'lingered 可以因为喜欢、舍不得，loitered 更常有闲晃、没明确事情的感觉；逗留的语气不同。',
 ('We lingered over coffee after the meal.','饭后我们慢悠悠地喝咖啡，没有急着走。'),('His words lingered in my mind all evening.','他的话一整晚都留在我脑海里。'),sources=S('lingered','linger'))
W('idles','/ˈaɪdəlz/','空转；闲耗时间；使停工、闲置〔第三人称单数〕',
 '车停在那里，发动机还低速运转，是 idles。工厂有机器却让它不用，也可说使设备闲置；不同句子看是否有宾语。',
 'idle + -s，读 /z/；动词来自 idle 形容词，早期空、无用的材料后来发展出不工作、空转。',IDLE+[['idle + -s → idles','它空转，或使设备闲置']],
 'the engine idles 发动机空转；idles away the afternoon 闲耗一下午。',
 'idles at a low speed；idles production lines。',
 'an engine idles 是仍在运转，an engine stops 是停止；不能把空转理解成已经熄火。',
 ('The engine idles quietly while the driver checks the map.','司机看地图时，发动机轻轻地空转着。'),('He idles away the afternoon in the shade.','他在阴凉处懒洋洋地消磨了一下午。'),sources=S('idles','idle'))
W('idled','/ˈaɪdəld/','空转了；闲耗了；使停工、闲置了',
 '车等人的时候发动机没关，是 idled。工厂把生产线暂时停下来，也能用这个词，重点是本可工作却没有实际干活。',
 'idle 去 e 加完整 -ed，读 /d/；过去式、过去分词。',IDLE+[['idle + -ed → idled','过去空转、耗时间，或被闲置']],
 'the car idled 汽车发动机空转；idled the factory 使工厂停工。',
 'idled away the weekend；workers were idled 工人被迫停工。',
 'idled machinery 是让机器闲着，scrapped machinery 是报废设备；暂时不用不等于彻底扔掉。',
 ('The taxi idled outside the station.','出租车停在车站外，发动机空转着。'),('The company idled one production line during the slowdown.','业务放缓期间，公司让一条生产线暂停运转。'),sources=S('idled','idle'))
W('idling','/ˈaɪdəlɪŋ/','正在空转；闲耗时间；闲置、停工',
 '机器在响，却没有带动实际工作，是 idling；人坐着懒洋洋地消磨时间也能这样说。看清主语，就知道是发动机还是人。',
 'idle 去 e 加 -ing；不重复 l。形容词、动词原有的空、不工作材料，在这里进入动作过程。',IDLE+[['idle + -ing → idling','空转或闲耗的过程']],
 'an idling engine 空转的发动机；idling away the morning。',
 'cars idling in traffic；idling machinery。',
 'idling engine 仍在低速运转，idle engine 也可能只是闲着未用；-ing 在具体句中把动作写得更明确。',
 ('We could hear an engine idling outside.','我们听得到外面有发动机空转的声音。'),('He spent the morning idling by the pool.','他上午一直在泳池边懒洋洋地消磨时间。'),sources=S('idling','idle'))
W('idler','英 /ˈaɪdlə/；美 /ˈaɪdlɚ/','闲着不做事的人；惰轮、从动轮',
 '人这一义是闲着不干事的人，常带评价。机器里的 idler 则可以是传递、引导运动的从动轮，本身不一定是动力来源。',
 'idle 去 e 加完整 -er；做人称名词说闲着的人，也有机器部件义。不是只在 idle 后添一个 r。',IDLE+[['idle + -er → idler','做这种动作的人；也有机械部件用法']],
 'an idle dreamer and idler 爱空想、不做事的人；an idler pulley 惰轮。',
 'call someone an idler；a belt idler 皮带惰轮。',
 'idler 指人时常带责备，person at leisure 可以中性说休闲的人；休息和懒得做事不是同一种评价。',
 ('He disliked being called an idler.','他不喜欢被人叫作懒汉。'),('The mechanic replaced the worn idler pulley.','机械师更换了磨损的惰轮。'),sources=S('idler','idle'))
W('idlers','英 /ˈaɪdləz/；美 /ˈaɪdlɚz/','闲着不做事的人〔复数〕；惰轮〔复数〕',
 '几个人整天无所事事，可以被叫作 idlers；设备清单里列出的 idlers 则可能是多个惰轮。词尾复数相同，场景不同。',
 'idler + -s，读 /z/；idle 去 e 加 -er 的基础上，再说多个做事者或多个部件。',IDLE+[['idle → idler → idlers','基础动作，到人或部件，再到复数']],
 'a group of idlers 一群无所事事的人；conveyor idlers 输送机托辊。',
 'idlers in the square；inspect the idlers 检查从动轮、托辊。',
 'idlers 形容人常含懒散评价，visitors 只是访客；坐在广场上歇脚不自动等于懒汉。',
 ('The novel describes a group of wealthy idlers.','小说描写了一群富有却无所事事的人。'),('The technician checked the conveyor idlers for wear.','技术员检查了输送机托辊是否磨损。'),sources=S('idlers','idle'))
W('lazes','/ˈleɪzɪz/','懒洋洋地休息、消磨时间〔第三人称单数〕',
 '周日下午没什么安排，他就躺在花园里晒太阳，是 lazes。语气可以很放松，不一定像批评拖延那样不满。',
 'laze + -s，拼写加 -s，/z/ 后读 /ɪz/。laze 本身由较早 lazy 逆构，不是先有动词再加 -y 的简单历史。',LAZE+[['laze + -s → lazes','他或她懒洋洋地休息']],
 'lazes around the house 在家懒洋洋地闲着；lazes in the sun。',
 'lazes by the pool；lazes away the afternoon。',
 'lazes 常写舒服地闲着，procrastinates 是拖着该做的任务；没有待办任务的休息不必算拖延。',
 ('He lazes in the garden on Sunday afternoons.','星期天下午，他常在花园里懒洋洋地休息。'),('The cat lazes in a patch of sunlight.','猫懒洋洋地躺在一小片阳光里。'),sources=S('lazes','laze'))
W('lazed','/leɪzd/','懒洋洋地休息、消磨时间了',
 '昨天没有赶行程，只是晒太阳、看书、发呆，可以说 lazed。它把闲适的身体状态写出来，不只是说没工作。',
 'laze 去 e 加完整 -ed，/z/ 后读 /d/；不增加 /ɪd/ 音节。',LAZE+[['laze + -ed → lazed','过去懒洋洋地消磨时间']],
 'lazed on the beach 在海滩上懒洋洋地休息；lazed around all day。',
 'lazed in the sun；lazed away the weekend。',
 'lazed around 可以是悠闲休息，slept 是睡着；躺着不动未必睡着。',
 ('We lazed on the beach until sunset.','我们在海滩上懒洋洋地待到日落。'),('She lazed around the flat on her day off.','休息日，她就在公寓里懒洋洋地闲着。'),sources=S('lazed','laze'))
W('lazing','/ˈleɪzɪŋ/','正在懒洋洋地休息、消磨时间',
 '躺在阴凉处，手边一本书，没急着去哪儿，这是 lazing。这个词常有身体松下来、时间慢下来的感觉。',
 'laze 去 e 加 -ing → lazing；原有 z 保留一个。历史上 laze 由 lazy 逆构，现代再规则加 -ing。',LAZE+[['laze + -ing → lazing','懒洋洋地休息的过程']],
 'lazing in the sun 晒太阳闲躺；lazing about at home。',
 'lazing by the river；a day spent lazing。',
 'lazing 着眼于懒洋洋地享受空闲，resting 更宽，可以是为恢复体力而休息。',
 ('They spent the afternoon lazing in the shade.','他们一下午都懒洋洋地待在阴凉处。'),('I found him lazing on the sofa with a book.','我看见他拿着一本书，懒洋洋地躺在沙发上。'),sources=S('lazing','laze'))
W('loiterer','英 /ˈlɔɪtərə/；美 /ˈlɔɪtərɚ/','逗留不走、无所事事地闲晃的人',
 '门口有人待了很久，看不出要做什么，可能被叫作 a loiterer。它常带别人觉得此人不该久留的眼光。',
 'loiter + 完整 -er，表做这种动作的人；loiter 原有 er 是动词的一部分，后一个 -er 才是这里的人称后缀。',LOITER+[['loiter + -er → loiterer','在某处闲晃、逗留的人']],
 'a loiterer outside the shop 店外逗留的人；move a loiterer along。',
 'a lone loiterer；a loiterer near the entrance。',
 'loiterer 带无明确事情而逗留的感觉，passerby 是经过的人；经过和停着不走不是同一个动作。',
 ('A loiterer stood near the entrance for most of the afternoon.','一个人在入口附近闲待了大半个下午。'),('The guard asked the loiterer to move away from the doorway.','门卫请那个逗留的人离开门口。'),sources=S('loiterer','loiter'))
W('loiterers','英 /ˈlɔɪtərəz/；美 /ˈlɔɪtərɚz/','逗留不走、闲晃的人〔复数〕',
 '几个人待在商店门口没明确事情，可能被写作 loiterers。它是对逗留方式的描述，常含不欢迎他们久留的语气。',
 'loiterer + -s，读 /z/；由 loiter 加 -er 表人，再加复数。',LOITER+[['loiter → loiterer → loiterers','逗留动作，到逗留者，再到多人']],
 'loiterers outside the station 车站外逗留的人；discourage loiterers。',
 'a group of loiterers；ask loiterers to move on。',
 'loiterers 并不等于 customers；有人久留不一定在购物，客户也可能很快就走。',
 ('The shopkeeper asked the loiterers to keep the doorway clear.','店主请那些逗留的人别堵着门口。'),('A few loiterers remained in the square after the crowd left.','人群离开后，广场上还有几个闲晃的人没走。'),sources=S('loiterers','loiter'))
W('sluggishly','/ˈslʌɡɪʃli/','缓慢无力地；反应迟钝地',
 '点了按钮半天才响应，水流得有气无力，人也提不起速度，都能说 sluggishly。重点不只是慢，还像缺乏活力或阻力很大。',
 'sluggish + -ly；sluggish 接中古英语 slugge 懒散的人与 -ish。动物蛞蝓的 slug 名称较晚，不能把整个词族说成由动物先造出。',
 [['中古英语 slugge 懒散者 + -ish → sluggish','先形容人、精神，后来也说事物缺乏运动、反应慢'],['sluggish + -ly → sluggishly','把缓慢、迟钝这种性质变成动作方式']],
 'respond sluggishly 响应迟缓；flow sluggishly 缓慢地流。',
 'move sluggishly；an economy growing sluggishly。',
 'slowly 可以是有意放慢，sluggishly 往往像本想快却提不起速度；读书认真读得慢不一定迟钝。',
 ('The old computer responded sluggishly.','那台旧电脑响应很迟缓。'),('The river moved sluggishly through the flat countryside.','河水缓缓流过平坦的乡野，几乎看不出动势。'),sources=S('sluggishly','sluggish'))
W('lethargy','英 /ˈleθədʒi/；美 /ˈleθɚdʒi/','无精打采、提不起劲的状态；昏沉',
 '身体和脑子像没充上电，连平常愿意做的事都难以启动，是 lethargy。它说精神、活力低，不等于判断一个人品性懒。',
 '经中古、晚期拉丁语接希腊 lethargia、lethargos，内部有 lethe 遗忘与 argos 不活动的材料。不能按现代英文拼写把 leth 拆成死亡。',LETH,
 'a feeling of lethargy 一阵提不起劲；shake off lethargy 摆脱昏沉、打起精神。',
 'summer lethargy 夏日倦怠；a sense of lethargy。',
 'laziness 常评价不愿付出努力，lethargy 着重缺乏精力、反应迟钝；一个人想做事，也可能没有精神。',
 ('The afternoon heat brought a feeling of lethargy.','午后的炎热让人提不起劲。'),('A short walk helped her shake off the morning lethargy.','散了一小会儿步，帮她摆脱了早晨的昏沉。'),sources=S('lethargy','lethargy'))
W('lethargic','英 /ləˈθɑːdʒɪk/；美 /ləˈθɑrdʒɪk/','无精打采的；昏沉、反应迟缓的',
 '睡醒很久还像没开机，动作、反应都提不起精神，可以说 lethargic。也能形容市场、活动缺少活力，像整体没动起来。',
 '英语借拉丁 lethargicus，接希腊 lethargikos、lethargos。现代可对照 lethargy 的状态与 -ic 的性质认形，但不是确定的现代英语现场换后缀。',LETH+[['希腊 lethargikos → 拉丁 lethargicus → 英语 lethargic','表示昏沉、缺少活力的性质']],
 'feel lethargic 感到没精神；a lethargic response 迟缓无力的响应。',
 'a lethargic market 没活力的市场；look lethargic。',
 'sleepy 是困、想睡，lethargic 更广，是精力和反应都低；没想睡也可能感觉没劲。',
 ('I felt lethargic after sitting indoors all day.','在室内坐了一整天后，我觉得浑身没劲。'),('The team gave a lethargic performance in the first half.','球队上半场踢得有气无力。'),sources=S('lethargic','lethargic'))
W('lethargically','英 /ləˈθɑːdʒɪkli/；美 /ləˈθɑrdʒɪkli/','无精打采地；昏沉迟缓地',
 '听到叫声，过了好一会儿才慢慢抬头；动起来也像没力气，就是 lethargically。它把缺少精神落到具体动作上。',
 'lethargic + -ally → lethargically；-ic 形容词常用 -ically 构成副词，常读 /ɪkli/，不按字母逐个读出额外重音。',LETH+[['lethargic + -ally → lethargically','以缺乏活力、精神的方式行动']],
 'move lethargically 无精打采地移动；respond lethargically 反应迟缓。',
 'rise lethargically 慢吞吞、没精神地起身；look up lethargically。',
 'reluctantly 是不情愿，lethargically 是精神、反应低；不想做和提不起劲是不同观察角度。',
 ('He rose lethargically from the sofa.','他没精打采地从沙发上站起来。'),('The dog lifted its head lethargically in the afternoon heat.','午后闷热，狗没精神地抬了抬头。'),sources=S('lethargically','lethargic'))
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_zhl',ROOTS,WORDS)
 extend_lessons()
