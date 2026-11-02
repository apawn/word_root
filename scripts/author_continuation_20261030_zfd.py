"""Sudden impacts, clashes, snares and early signs of discontent."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
def S(word,base):
 return ['https://en.wiktionary.org/wiki/'+word+'#English','https://www.etymonline.com/word/'+base]+(['https://dictionary.cambridge.org/dictionary/english/snare'] if base=='snare' else [])
EXISTING_ROOT_ADDITIONS={
 'B3319':dict(words=['bang','bangs','banged','banging'],label='bang 的突响、重敲与刘海等用法',note='bang 大概拟声或联系北欧敲击材料；美式 bangs 刘海或与骤然齐截的动作感有关，不能当作头发发出砰声的确定故事。'),
 'B4089':dict(words=['slap','slaps','slapped','slapping'],label='slap 的拍击、随手放与强加',note='slap 接中古英语拍击材料；现代 slapping 双写 p，再加完整 -ing，基础并非词尾一个 -ping。'),
 'B3348':dict(words=['clap','claps','clapped','clapping'],label='clap 的拍响、鼓掌及现代变化',note='clap 接古英语、古诺尔斯等日耳曼拍击材料；clapped 双写 p，拍手鼓掌是常见分支，不等于所有 clap 都是称赞。'),
 'B4418':dict(words=['bump','bumps','bumped','bumping'],label='bump：碰撞、凸包、偶遇与推高',note='碰撞、凸起材料的早期关系与来源有不同分析；bump into someone 偶遇、bump up 推高是固定搭配，不总是真撞击。'),
 'B4088':dict(words=['slam','slams','slammed','slamming'],label='slam 的猛关、重放与严厉批评',note='响声、重击动词接相应名词，可能联系北欧拟声材料；牌戏及体育 grand slam 的词源另有争议，不能都从关门推导。'),
 'A2238':dict(words=['snare','snares','snared','snaring','snarl'],label='snare 与缠结义 snarl 的套索材料',note='snare 联系古英语 snearu、北欧 snara 等套索材料；缠结 snarl 有小称、反复动作形式的分析，露齿低吼 snarl 另分近源。'),
 'A1741':dict(words=['rumble','rumbling','rumblings'],label='rumbling、rumblings：低声响与不满苗头',note='rumbling 的活动、声音名词再可有复数；rumblings of discontent 常写尚未公开、全面爆发的不满声或迹象。'),
 'A1760':dict(words='bang bangs banged banging whack whacks whacked whacking slap slaps slapped slapping clap claps clapped clapping crash crashes crashed crashing clash clashes clashed clashing bump bumps bumped bumping slam slams slammed slamming smack smacks smacked smacking snare snares snared snaring'.split(),label='敲击、相撞、冲突和捕住动词的变化',note='-ed、-ing 都接整个基础词。smack 的拍击、咂嘴与“有某种味道”分开近源；snare 的套索、鼓底响弦也分别说明借入发展。'),
}
BANG=[['十六世纪 bang → 现代 bang','大概模仿重击，或借北欧 banga 一系；响声、击打与语气用法扩展'],['现代不同场景','砰响、敲打；bangs 刘海；banging 在部分口语中还表示出色']]
W('bangs','/bæŋz/','砰响、重敲〔第三人称单数〕；砰声〔复数〕；〔美〕刘海',
 '门、锅盖“砰”响，用 bangs；看发型时，bangs 又是额前的刘海。后一种不能按“头发在响”去翻。',
 '声音动词、名词 bang + -s；刘海义通常用复数 bangs，或与齐截、突然截断的动作感有关，具体起名过程不完全确定。',BANG+[['bang + -s → bangs','它砰响；多声砰响；另有常用发型名词']],
 'bangs on the door 是砰砰敲门，have bangs 是留刘海。英式常说 fringe；hair bangs 是习惯复数，不能只认成三单。',
 'loud bangs 巨大砰响；cut her bangs 剪她的刘海。',
 'bangs 作刘海时看头发语境；two bangs 在声响语境是两声砰响，不是两撮刘海。',
 ('The loose door bangs in the wind.','松动的门被风吹得砰砰响。'),('She has short bangs above her eyebrows.','她眉毛上方留着短刘海。'),sources=S('bangs','bang'))
W('banged','/bæŋd/','砰地响了、重重敲了；撞痛了、重放了',
 '门砰地一关、拳头重敲、膝盖不小心撞到桌角，都可以用 banged。动作往往又猛又突然。',
 'bang + 完整 -ed，/ŋ/ 后读 /d/；ng 在这里读 /ŋ/，不另外加 /ɡ/。',BANG+[['bang + -ed → banged','过去重敲、砰响或撞到']],
 'banged on the door 是重重敲门，banged his knee 是撞了膝盖，banged the book down 是把书砰地一放。',
 'banged shut 砰地关上；banged into the table 猛撞桌子。',
 'banged 可以是碰到了，不必真有爆炸；写身体时通常是撞击动作，具体疼痛程度还看上下文。',
 ('He banged on the door but nobody answered.','他砰砰敲门，却没人回应。'),('I banged my knee on the edge of the desk.','我的膝盖撞到了桌沿。'),sources=S('banged','bang'))
W('banging','/ˈbæŋɪŋ/','正在重敲、砰响；砰砰声；〔口语〕很棒的、带劲的',
 '门、鼓或工具正猛地一下下响，叫 banging。部分口语里说 a banging tune，则是在夸曲子带劲、好听。',
 'bang + 完整 -ing，直接加；声音、击打分词和后来的夸赞形容词要按语境分，不双写 g。',BANG+[['bang + -ing → banging','砰响、重敲过程；后来口语有出色、带劲义']],
 'banging on the door 是正砰砰敲门，a banging noise 是砰砰声；a banging tune 不是曲子在敲门。',
 'stop banging 别再重敲；a banging bassline 带劲的低音线。',
 'banging 可以形容响声，也能在非正式语境夸好；选哪种中文，要看 noise、door 还是 tune、meal 等搭配。',
 ('The banging on the door grew louder.','砰砰敲门的声音越来越响。'),('The DJ played a banging tune that got everyone dancing.','DJ 放了一首带劲的曲子，大家都跳起舞来。'),sources=S('banging','bang'))
WHACK=[['十八世纪口语 whack 动词 → 名词','大概模仿重重、利落击打的声音'],['击打 → 尝试等搭配及口语强调','whacked 还说筋疲力尽；whacking 可强调数量、体积很大']]
W('whacks','/wæks/','猛击、重敲〔第三人称单数〕；一记记重击；尝试〔复数〕',
 '手、球拍或工具重重“啪”一下，用 whacks；名词复数则是几记利落的重击。take a whack at 又可说试一下。',
 'whack + -s，/k/ 后读 /s/；大概拟声基础词，现代直接变化，不从 wh 后面硬找一个古典词根。',WHACK+[['whack + -s → whacks','他、她猛击；多记重击或尝试']],
 'whacks the ball 是用力击球，a few whacks 是几下重敲；whack at a problem 可借击打画面说尝试解决。',
 'whacks it hard 猛击它；three sharp whacks 三记利落重击。',
 'whacks 与 taps 都能写敲，前者通常更重、更猛；不只是多一个声音大小的差别。',
 ('He whacks the ball hard towards the fence.','他用力把球击向围栏。'),('She gave the stuck lid a few whacks with a wooden spoon.','她用木勺把卡住的盖子重敲了几下。'),sources=S('whacks','whack'))
W('whacked','/wækt/','猛击了、重敲了；〔英口语〕累坏的',
 '刚才重重敲、打了一下，叫 whacked；一天忙完说 I’m whacked，则是累瘫了，不是真被谁打了一顿。',
 'whack + 完整 -ed，/k/ 后读 /t/；过去分词后来还可作疲惫的口语形容词，按场景分义。',WHACK+[['whack + -ed → whacked','过去猛击；后有筋疲力尽的口语状态']],
 'whacked the ball 是猛击了球，absolutely whacked 是累坏了；疲惫义在英式口语较常见。',
 'whacked it away 猛地把它击开；felt whacked 觉得累瘫了。',
 'whacked 的累不是 wounded 受伤；运动、工作一天也能让人 whacked，词本身不要求遭到击打。',
 ('She whacked the ball over the net.','她用力把球击过球网。'),('I was absolutely whacked after the long walk.','走了那么远，我累坏了。'),sources=S('whacked','whack'))
W('whacking','/ˈwækɪŋ/','正在猛击、重敲；〔口语〕极大的、非常',
 '人正一下一下重重打，是 whacking；a whacking great bill 则像把“大”重重敲给你，表示账单大得吓人。',
 'whack + 完整 -ing，直接加；在强调数量、体积的口语中，常由形容或副词性用法修饰 great、big 等词。',WHACK+[['whack + -ing → whacking','猛击过程；后来口语强调很大、很多']],
 'whacking the ball 是正在猛击球，a whacking great sum 是很大一笔钱；后一种没有真实击打动作。',
 'a whacking big hole 一个大得吓人的洞；keep whacking 不停重打。',
 'whacking great 是非正式强调；正式报告通常直接写 very large、substantial 等，具体看表达场合。',
 ('He was whacking the ball against the wall.','他正用力把球打向墙。'),('We were left with a whacking great bill.','最后留给我们一张大得吓人的账单。'),sources=S('whacking','whack'))
SLAP=[['中古英语 slap 名词、slappen 动词 → slap','拍击材料大概拟声，可与低地德语等形式比较'],['拍击 → 迅速、随意放上；强加处罚等用法','手掌、平面拍响的动作感，扩到贴、放或施加']]
W('slaps','/slæps/','拍、打、随手放上、强加〔第三人称单数〕；拍击〔复数〕',
 '用张开的手掌“啪”地拍一下，用 slaps；把文件、标签很随意地一放、一贴，也能借这个动作。',
 'slap + -s，/p/ 后读 /s/；动词三单与拍击名词复数同形，不双写 p。',SLAP+[['slap + -s → slaps','他、她拍、随手放、强加；多记拍击']],
 'slaps the table 是拍桌，slaps a label on it 是随手贴个标签；slaps a fine on someone 是对某人处以罚款。',
 'slaps him on the back 拍他的背；slaps on some paint 随意涂点漆。',
 'slaps 不一定是在伤害人：拍背祝贺、把东西啪地一放都有这个动作感；态度看对象、力度和情境。',
 ('He slaps his friend on the back in congratulations.','他拍朋友的背，表示祝贺。'),('She slaps a label on the box and moves to the next one.','她把标签啪地贴到箱子上，接着处理下一个。'),sources=S('slaps','slap'))
W('slapping','/ˈslæpɪŋ/','正在拍打、随手放、强加；拍击声、动作',
 '平平的表面一下一下拍到另一处，像水拍船身或人拍桌，是 slapping；也能写随手贴上、强加的动作。',
 'slap 双写 p + 完整 -ing → slapping；短元音重读单音节后单个辅音字母的变化，基础仍是 slap。',SLAP+[['slap 双写 p + -ing → slapping','拍打、随手放或强加的过程']],
 'water slapping against the hull 是水拍船壳；slapping labels on boxes 是随手贴标签。看对象分出声音或动作。',
 'slapping the table 拍桌；slapping paint on the wall 草草往墙上涂漆。',
 'slapping 与 clapping 都能拍，clapping 常指两手相击鼓掌；slapping 常是一只手或平面拍到别处。',
 ('We heard water slapping against the side of the boat.','我们听见水啪啪拍着船身。'),('He was slapping paint onto the fence in broad strokes.','他正大笔往栅栏上刷漆，刷得很随意。'),sources=S('slapping','slap'))
CLAP=[['古英语 clæppan、或北欧 klappa 的相关影响 → clap','日耳曼拍击、响声材料，大概有拟声基础'],['拍响 → 拍手鼓掌及其他快速拍动作','还可说拍肩、啪地合上；不必每次都在称赞']]
W('claps','/klæps/','鼓掌、拍手、啪地拍〔第三人称单数〕；拍响、鼓掌声〔复数〕',
 '两手“啪、啪”相碰，叫 claps；雷声突然一记炸响，也能用名词 claps of thunder。先抓快速拍响。',
 'clap + -s，/p/ 后读 /s/。基础 clap 接古英语、古诺尔斯等相关拍击材料，不从现代 clip 夹子换元音解释。',CLAP+[['clap + -s → claps','他、她拍手；多记拍响、炸雷']],
 'claps her hands 是拍手，claps him on the shoulder 是啪地拍肩；claps of thunder 是几记响雷。',
 'claps along with the music 随音乐拍手；loud claps 响亮的拍手声。',
 'claps 可以是拍手吸引注意、打节拍，也可以是赞赏；不等于每次都在说表演好。',
 ('She claps her hands to get the children’s attention.','她拍拍手，吸引孩子们注意。'),('We heard two loud claps of thunder.','我们听见两声响亮的炸雷。'),sources=S('claps','clap'))
W('clapped','/klæpt/','鼓掌了、拍手了；啪地拍、合上了',
 '刚才拍了手、拍了一下肩膀，或双手把东西啪地合上，用 clapped。鼓掌是常见义，动作还可以扩到别处。',
 'clap 双写 p + 完整 -ed → clapped，/p/ 后读 /t/；仍是一个音节。',CLAP+[['clap 双写 p + -ed → clapped','过去拍响、鼓掌、啪地拍']],
 'clapped for the performers 是为表演者鼓掌，clapped him on the back 是啪地拍他的背；不是所有 clapped 都要译鼓掌。',
 'clapped loudly 大声鼓掌；clapped her hands over her ears 迅速用手捂住耳朵。',
 'clapped someone on the back 常是鼓励、祝贺动作；与 slapped 都可写拍背，力度和态度仍看具体语境。',
 ('The audience clapped as the actors bowed.','演员鞠躬时，观众鼓掌。'),('He clapped me on the back and said, “Well done!”','他啪地拍我的背，说：“干得好！”'),sources=S('clapped','clap'))
CRASH=[['中古英语 crasschen → crash','打碎、响亮碰撞材料，大概拟声'],['巨响、撞碎 → 车辆碰撞、经济垮掉、系统崩溃','后来的用途各有领域；口语还可说留宿、倒头睡，或不请自来']]
W('crash','英 /kræʃ/；美 /kræʃ/','撞击、撞毁；巨响；系统崩溃、暴跌；〔口语〕留宿、倒头睡',
 '重东西撞上、碎落，“哗啦砰”地一下，是 crash。系统突然停摆、行情猛跌，也借这种突然垮掉的画面。',
 '承中古英语 crasschen，大概拟声；名词、动词后来扩到车辆、金融、计算机等。口语 crash at a place 又可指临时留宿。',CRASH,
 'a car crash 是车祸，the program crashed 是程序崩溃；crash at a friend’s place 是在朋友家凑合住一晚，属口语。',
 'crash into a wall 撞墙；a loud crash 一声巨响；a crash course 速成课。',
 'crash 比 bump 常更强烈、更可能伴损坏；计算机 crash 不是真硬件撞在一起，而是运行突然失败。',
 ('We heard a loud crash from the kitchen.','我们听见厨房一声巨响。'),('I saved the file before the program could crash.','我在程序可能崩溃前保存了文件。'),sources=S('crash','crash'))
W('crashes','/ˈkræʃɪz/','撞毁、崩溃、猛跌〔第三人称单数〕；碰撞、巨响、崩溃〔复数〕',
 '程序一运行到某一步就停摆，叫 crashes；车辆碰撞、突然巨响或系统故障有几次，也可用名词复数。',
 'crash + -es，/ʃ/ 后读 /ɪz/，多一个音节；现代变化接整个基础词，不拆出独立 -ash。',CRASH+[['crash + -es → crashes','它撞毁、崩溃；多次巨响、碰撞或故障']],
 'the app crashes 是应用崩溃，frequent crashes 是频繁崩溃；two car crashes 是两起车祸，具体领域由搭配分清。',
 'crashes on startup 一启动就崩溃；loud crashes 一阵阵巨响。',
 'crashes 和 clashes 只差一个字母，但前者常是撞毁、崩溃，后者是冲突、不搭；读到 schedule 常优先看 clash。',
 ('The app crashes whenever I try to open that file.','我每次试着打开那个文件，应用就崩溃。'),('The report describes several crashes at the same junction.','报告描述了同一路口发生的几起车祸。'),sources=S('crashes','crash'))
W('crashed','/kræʃt/','撞毁了、巨响着落下了；崩溃了、暴跌了；〔口语〕留宿、倒头睡了',
 '车刚才撞上、电脑程序突然停摆，都能用 crashed；口语说 crashed at his place，则是去他那里凑合过夜。',
 'crash + 完整 -ed，/ʃ/ 后读 /t/；不是 /ɪd/。不同领域的现代动词义按同一规则变化。',CRASH+[['crash + -ed → crashed','过去撞毁、垮掉；口语留宿等用法']],
 'crashed into a tree 是撞树了，the computer crashed 是电脑系统崩溃；crashed on the sofa 可以是倒在沙发睡了。',
 'crashed to the floor 哗啦坠地；crashed overnight 一夜间暴跌。',
 'crashed 描写突然失败、撞落或相应口语动作；clashed 则说两边不合、相冲，不能混写。',
 ('The car crashed into a barrier.','汽车撞上了护栏。'),('My computer crashed before I saved the document.','我还没保存文档，电脑就崩溃了。'),('We crashed at a friend’s place after the concert.','音乐会后，我们在朋友家凑合住了一晚。'),sources=S('crashed','crash'))
W('crashing','/ˈkræʃɪŋ/','正在撞击、坠落、崩溃；轰然的；〔口语〕极其、十足的',
 '重物正哗啦落下、波浪正猛拍岸，或系统正突然停摆，叫 crashing。a crashing bore 又是十足的大闷人、无聊透顶的事。',
 'crash + 完整 -ing；分词、形容用法之外，可在口语修饰中加强程度，不必每次真有碰撞。',CRASH+[['crash + -ing → crashing','撞落、崩溃过程；后有压倒性、十足的强调']],
 'crashing waves 是轰然拍岸的浪，keep crashing 是不断崩溃；a crashing bore 是极其无聊的人或事。',
 'crashing down 哗啦坠下；a crashing sound 轰然巨响。',
 'crashing 是碰撞、垮落等过程，clashing 是两边相冲；撞坏电脑与安排撞期，用不同基础词。',
 ('We listened to the crashing waves below the cliffs.','我们听着悬崖下海浪轰然拍岸。'),('The app keeps crashing when I edit large photos.','我一编辑大照片，这个应用就不断崩溃。'),sources=S('crashing','crash'))
CLASH=[['十六世纪 clash 动词、名词','大概拟声，也有 clap 与 crash 混合的分析，不能当作确定唯一来源'],['碰撞响声 → 对立、冲突、不协调','人意见顶上、日程同一时间、颜色不搭，各有常用搭配']]
W('clash','/klæʃ/','冲突、不合、撞期；不搭；碰撞响；冲突、碰撞声',
 '两边迎面顶上，谁也不顺谁，就是 clash 的核心画面：意见顶上、时间撞上、颜色放在一起扎眼，都能这样说。',
 '大概由碰撞声拟声发展，也有 clap、crash 混合分析；后来扩到非实体冲突、颜色不协调等。不是确定从现代 crash 换 r 为 l。',CLASH,
 'a clash of opinions 是意见冲突，a timetable clash 是安排撞期，red clashes with pink 是红色和粉色放一起不搭。',
 'clash with a colleague 与同事起冲突；a clash of colours 不协调的配色。',
 'clash 强调两边相冲、不合，crash 常强调撞毁、突然失败；two meetings clash 不表示两个会议崩溃。',
 ('There is a clash between the two meetings.','这两场会议时间撞上了。'),('The bright tie seems to clash with his shirt.','那条鲜亮领带看起来和他的衬衫不搭。'),sources=S('clash','clash'))
W('clashes','/ˈklæʃɪz/','相冲、不搭、撞期〔第三人称单数〕；冲突、对抗〔复数〕',
 '一件事碰到另一件事不合适，用 clashes；几次争执、对抗作为名词，也用这个形式。',
 'clash + -es，/ʃ/ 后读 /ɪz/，多一个音节；三单、名词复数共用拼写。',CLASH+[['clash + -es → clashes','它与别的相冲；多次冲突、对抗']],
 'clashes with my class 是和我的课撞期，personality clashes 是性格不合引起的冲突；不要求真有声音。',
 'clashes over policy 因政策起冲突；clashes with the decor 和装饰不搭。',
 'clashes 与 crashes 的中间辅音分别是 /l/、/r/；记住前者两边不合、后者撞毁或崩溃，搭配会更清楚。',
 ('The workshop clashes with my afternoon class.','这场工作坊和我下午的课撞期。'),('Their personality clashes made teamwork difficult.','他们性格不合、常起冲突，合作变得困难。'),sources=S('clashes','clash'))
W('clashed','/klæʃt/','起冲突了、意见不合了；撞期了、不搭了；碰撞响了',
 '两个人刚才争到一起，两个安排时间撞上，或颜色放在一起不协调，都可用 clashed。',
 'clash + 完整 -ed，/ʃ/ 后读 /t/；规则变化，和 crashed 相近但不是同一个词。',CLASH+[['clash + -ed → clashed','过去相冲、不协调、碰撞']],
 'clashed over the plan 是因计划争执了，clashed with another event 是和另一活动撞期；颜色也能 clashed。',
 'clashed repeatedly 反复起冲突；clashed with the curtains 和窗帘颜色不搭。',
 'clashed 不必升级成暴力冲突；讨论、个性、时间、配色都能互相不合，按对象选中文。',
 ('They clashed over how to spend the budget.','他们为预算怎么花起了争执。'),('The orange cushions clashed with the pink curtains.','橙色靠垫和粉色窗帘放一起不搭。'),sources=S('clashed','clash'))
W('clashing','/ˈklæʃɪŋ/','正在冲突、相撞；不合的、撞期的；不协调的',
 '两边的想法、要求或安排正顶在一起，叫 clashing；形容颜色、花纹时，是看着打架、不搭。',
 'clash + 完整 -ing，直接加；可表示过程，也可修饰互不相容的事物，不全是进行时。',CLASH+[['clash + -ing → clashing','冲突过程；不合、不搭、撞期的状态']],
 'clashing opinions 是相冲的意见，clashing patterns 是不协调的花纹，clashing schedules 是互相撞期的安排。',
 'clashing colours 不搭的颜色；clashing demands 相互冲突的要求。',
 'clashing colours 是审美、视觉上的不协调，不是颜料真的撞击；这类比喻保留两边互相顶住的感觉。',
 ('The room was full of clashing colours and patterns.','房间里各种颜色、花纹互相不搭。'),('Clashing schedules made it hard for us to meet.','日程互相撞期，让我们很难碰面。'),sources=S('clashing','clash'))
BUMP=[['十六、十七世纪 bump 的凸起、撞击材料','可能拟声，也有北欧来源分析；凸起、碰撞的先后关系不宜只凭直觉倒推'],['碰到 → 偶遇；推挪 → 推高、挤掉位置','名词还说包、凸点、颠簸；动作不都很重']]
W('bumps','/bʌmps/','碰撞、颠簸、推高〔第三人称单数〕；凸包、颠簸、碰撞〔复数〕',
 '车驶过路面一凸一点，或头碰到后鼓起一个包，是 bumps 的常见画面；动词则可写轻撞、颠簸。',
 'bump + -s，/p/ 后读 /s/；同一现代形式可作动词三单、名词复数，基础来源仍有不同分析。',BUMP+[['bump + -s → bumps','它碰、颠；多个包、凸点或碰撞']],
 'bumps in the road 是路面凸起，bumps into a friend 是偶遇朋友；bumps up the price 是把价钱推高。',
 'speed bumps 减速带；a few bumps 几次颠簸、几个包。',
 'bumps into 可以是真撞上，也可以只是碰巧遇见；主语、对象、场景共同分出，别总译成撞伤。',
 ('We slowed down for the bumps in the road.','遇到路面凸起，我们减了速。'),('He often bumps into old friends at the market.','他常在市场偶遇老朋友。'),sources=S('bumps','bump'))
W('bumped','/bʌmpt/','碰到了、颠簸了；偶遇了；被挤掉位置、推迟或提高了',
 '刚才肩膀、车或箱子碰到别处，用 bumped；bumped into an old friend 也能只是路上偶遇，没真的碰撞。',
 'bump + 完整 -ed，/p/ 后读 /t/；末尾已有 mp，不双写 p，元音保持 /ʌ/。',BUMP+[['bump + -ed → bumped','过去碰撞、偶遇或推挪位置、数额']],
 'bumped my head 是碰了头，bumped into him 是碰到或偶遇他，bumped up the price 是提高价钱；航班语境被 bumped 还可指座位被挤掉。',
 'bumped against a chair 碰到椅子；bumped to next week 被挪到下周。',
 'bumped 的物理碰撞通常比 crashed 更轻；bumped into a classmate 又可只说偶遇，完全没有碰撞动作。',
 ('I bumped my shoulder against the doorframe.','我的肩膀碰到了门框。'),('We bumped into an old classmate at the station.','我们在车站偶遇一位老同学。'),sources=S('bumped','bump'))
W('bumping','/ˈbʌmpɪŋ/','正在碰撞、颠簸；偶遇；正在推高、挪动',
 '车一路在不平处上下颠、东西互相碰，是 bumping；反复碰巧遇到某人，也能说 keep bumping into。',
 'bump + 完整 -ing，直接加；基础末尾 mp 两字母保留，不双写 p。',BUMP+[['bump + -ing → bumping','碰撞、颠簸过程；偶遇、推挪等搭配']],
 'bumping along a road 是沿路颠簸，bumping into people 是撞到或偶遇人，bumping up costs 是把成本推高。',
 'bumping over stones 越过石头一路颠；keep bumping into her 总是偶遇她。',
 'bumping along 常含不平路面的上下颠动，gliding along 更像平滑移动；动作质感很不同。',
 ('The bus went bumping along the rough road.','公交车沿崎岖路面一路颠簸。'),('I keep bumping into her at the library.','我老在图书馆偶遇她。'),sources=S('bumping','bump'))
SLAM=[['十七世纪 slam 重击名词 → 相应动词','可能联系北欧拟声材料；重击、猛关，再到严厉批评'],['牌戏 slam 另一条历史 → Grand Slam 等','早期牌戏词来源不明，后来扩到体育大满贯；不从摔门直接推来']]
W('slams','/slæmz/','猛关、猛放、抨击〔第三人称单数〕；重击、猛关声〔复数〕；〔Grand Slams〕大满贯',
 '门“砰”地猛关、东西重重一放，用 slams；批评把人说得很重，也能用。Grand Slams 则走牌戏、体育那条历史。',
 'slam + -s，/m/ 后读 /z/。响声动词、名词规则变化；大满贯中的 slam 近源有另一路，不都出自猛关门。',SLAM+[['slam + -s → slams','他、她猛关、抨击；多次重击或大满贯']],
 'slams the door 是猛关门，slams the proposal 是抨击提案，wins Grand Slams 是赢得大满贯；先看动作、评价还是比赛。',
 'slams on the brakes 猛踩刹车；door slams 猛关门声。',
 'slams 作批评动词常语气很重，比 neutrally criticizes 更猛烈；大满贯不是说运动员把门关得响。',
 ('He slams the door whenever he is annoyed.','他一恼火就猛地关门。'),('The newspaper slams the plan as unrealistic.','报纸抨击这项计划不切实际。'),('She dreams of winning Grand Slams.','她梦想赢得大满贯。'),sources=S('slams','slam'))
W('slammed','/slæmd/','猛关、猛放、猛撞了；严厉批评了',
 '把门、书或别的东西重重关、放、撞，用 slammed；媒体把一个做法狠狠批了一顿，也能这样写。',
 'slam 双写 m + 完整 -ed → slammed，词尾读 /d/；基础是短元音重读单音节，按规则双写。',SLAM+[['slam 双写 m + -ed → slammed','过去猛击、猛关或严厉批评']],
 'slammed the door 是猛关门，slammed the decision 是抨击决定；slammed on the brakes 是猛踩刹车。',
 'slammed shut 砰地关上；slammed into a wall 猛撞墙。',
 'slammed 在新闻评论里常是强烈批评，不是真有人动手打某项计划；宾语会提示是实体还是观点。',
 ('She slammed the book shut.','她把书啪地重重合上。'),('Critics slammed the decision as unfair.','批评者抨击这个决定不公平。'),sources=S('slammed','slam'))
W('slamming','/ˈslæmɪŋ/','正在猛关、猛击、重放；猛关声；正在抨击',
 '门正一遍遍砰地关、东西正被重重一放，叫 slamming；说话、写文章正猛批某事，也能借这种重击感。',
 'slam 双写 m + 完整 -ing → slamming；可以表示动作、声音，也可进入批评的比喻，不必每次都真击打。',SLAM+[['slam 双写 m + -ing → slamming','猛关、重击或抨击的过程']],
 'slamming doors 是猛关门，slamming the policy 是正抨击政策；the slamming of doors 可以整体说反复关门声。',
 'slamming on the brakes 猛踩刹车；slamming a cup down 重重放下杯子。',
 'slamming 与 closing 都能关门，前者额外交代猛、响；批评用法也保留这种力度很大的感觉。',
 ('The slamming of doors woke the baby.','砰砰关门的声音吵醒了婴儿。'),('The article is slamming the policy rather than explaining it.','这篇文章在猛烈抨击那项政策，却没有把政策解释清楚。'),sources=S('slamming','slam'))
SMACK=[['声音、拍击支线：咂嘴、响吻与重拍材料 → smack','大概拟声，低地德语等有可比较形式；具体借入分析不同'],['滋味支线：古英语 smæc、smæccan → smack、smack of','味道、气味 → 带某种意味；不是因为咂嘴才第一次产生味道义']]
W('smack','/smæk/','啪地打、拍击；咂嘴；啪声、响吻；〔smack of〕有某种意味',
 '一巴掌、一声响吻或嘴唇“吧嗒”一声，可用 smack；smack of desperation 则是“透着绝望的味道”，走另一条滋味来源。',
 '拍击、咂嘴联系拟声材料；smack of 联系古英语 smæc 味道、smæccan 品尝一系。不能编成先咂嘴才从中派生全部滋味义。',SMACK,
 'smack his lips 是咂嘴，a smack on the cheek 可说脸上一记拍打或响吻，smack of arrogance 是带傲慢意味。',
 'a loud smack 啪的一响；smack the ball 用力击球。',
 'smack 与 slap 在拍击义很近；smack of a cover-up 说有掩盖事情的嫌疑，既不是真打，也不是人在吃什么。',
 ('The door closed with a sharp smack.','门啪地一声关上。'),('That excuse seems to smack of desperation.','那个借口似乎透着走投无路的意味。'),('He began to smack his lips in anticipation of lunch.','他一想到午饭就开始咂嘴。'),sources=S('smack','smack'))
W('smacks','/smæks/','拍打、咂嘴〔第三人称单数〕；拍击、响吻〔复数〕；〔smacks of〕带某种意味',
 '嘴唇吧嗒响或手掌啪地拍，用 smacks；smacks of 后接欺骗、傲慢等，则是带这种味道、嫌疑。',
 '两条基础动词 smack 都可加 -s，/k/ 后读 /s/；名词复数也是同形，近源分支由上下文确定。',SMACK+[['smack + -s → smacks','他、她拍打、咂嘴；它带某种意味；数记拍击']],
 'smacks his lips 是咂嘴，smacks of dishonesty 是透着不诚实的嫌疑；滋味比喻常带负面评价。',
 'smacks the ball 猛击球；smacks of an excuse 像是在找借口。',
 'smacks of 的“味道”通常是抽象意味，不能译成闻到一个真实气味；更不能按声音支线翻成拍了某物。',
 ('The child smacks his lips after tasting the soup.','孩子尝完汤，咂了咂嘴。'),('The whole arrangement smacks of favouritism.','整套安排透着偏袒的味道。'),sources=S('smacks','smack'))
W('smacked','/smækt/','啪地打了、拍了；咂嘴了、响吻了；带有某种意味',
 '刚才手掌或球拍啪地击了一下，或嘴唇吧嗒一响，用 smacked；smacked of 则仍要看滋味比喻那条线。',
 'smack + 完整 -ed，/k/ 后读 /t/；ck 保留，不再添一个 k，也不多读 /ɪd/。',SMACK+[['smack + -ed → smacked','过去拍击、咂嘴；smacked of 带某种意味']],
 'smacked the ball 是猛击球，smacked his lips 是咂嘴，smacked of arrogance 是带傲慢意味；共同拼写不等于同一近源。',
 'smacked against the wall 啪地撞墙；smacked the table 啪地拍桌。',
 'smacked the ball 常带用力击球的感觉，tapped the ball 则更像轻轻一碰；力度是选词的一部分。',
 ('She smacked the ball across the court.','她用力把球击向球场另一边。'),('He smacked his lips after the first bite.','吃了第一口，他咂了咂嘴。'),sources=S('smacked','smack'))
W('smacking','/ˈsmækɪŋ/','正在拍打、咂嘴；拍击声、吧嗒声；〔smacking of〕带某种意味',
 '手掌或嘴唇正发出“啪、吧嗒”的动作声，叫 smacking；后接 of 观点、态度时，就转到带某种意味。',
 'smack + 完整 -ing，直接加；ck 两个字母保留，不双写末尾 k。声音、滋味两条动词都能按现代规则变化。',SMACK+[['smack + -ing → smacking','拍击、咂嘴过程；smacking of 的意味用法']],
 'lip smacking 是咂嘴，smacking the ball 是正在猛击球；smacking of dishonesty 是带不诚实的嫌疑。',
 'smacking his lips 咂嘴；a smacking sound 啪、吧嗒声。',
 'smacking 的咂嘴是嘴唇发声，不等于 chewing 咀嚼的全部动作；吃东西时可以有前者，也可以没有。',
 ('He was smacking his lips as he looked at the cake.','他看着蛋糕，咂着嘴。'),('We heard waves smacking against the rocks.','我们听见浪啪地拍在岩石上。'),sources=S('smacking','smack'))
SNARE=[['古英语 snearu 等、或另有北欧 snara 的借入 → snare 套索名词 → 动词','绳圈、圈套 → 套住、困住；与缠结义 snarl 的材料可相连'],['鼓的响弦支线：荷兰语 snaar 弦等 → snare；再有 snare drum 的简称','同一更远绳、弦词族的另一发展，不是先把捕兽套装上鼓才有名称']]
W('snare','英 /sneə/；美 /sner/','套索、圈套；套住、捕住；鼓底响弦；小军鼓',
 '一根绳形成的圈，把东西套住，是 snare 的核心画面；比喻看似好处却把人困住的安排，就是圈套。音乐里还可指鼓的响弦或小军鼓。',
 '套索义承古英语 snearu 等，也有北欧 snara 来源影响；鼓底弦义可能另借荷兰语 snaar 弦，同属更远的绳弦材料，不都从捕兽动作直接造。',SNARE,
 'caught in a snare 是落进套索或圈套；snare a victim 是诱捕受害者；play the snare 是打小军鼓，来自 snare drum 的简称。',
 'a hidden snare 隐藏的圈套；a snare drum 小军鼓、响弦鼓。',
 'snare、trap 都能说陷阱，snare 更容易保留绳圈套住的画面；音乐义与套索义有更远词族联系，近源发展要分开。',
 ('The fox had escaped from an old snare.','狐狸从一个旧套索里逃脱了。'),('She plays the snare in the marching band.','她在行进乐队里打小军鼓。'),sources=S('snare','snare'))
W('snares','英 /sneəz/；美 /snerz/','套住、捕住〔第三人称单数〕；套索、圈套、鼓响弦或小军鼓〔复数〕',
 '某件事像绳圈把人诱进去，用 snares；名词复数则是多个套索、圈套，音乐场景还可说鼓的响弦或几面小军鼓。',
 'snare + -s，保留 e；英式 /eə/ 后加 /z/，美式相应 r 音后加 /z/，现代词尾不改变基础词的多条来源。',SNARE+[['snare + -s → snares','它套住；多个套索、圈套或鼓的相关用法']],
 'snares its victims 是把受害者套住，avoid the snares 是避开圈套；音乐中的 snares 不按捕兽工具理解。',
 'hidden snares 隐藏圈套；snares unsuspecting people 套住毫无戒心的人。',
 'snares 与 snarls 不同：前者是套索、捕住，后者还可说缠成一团或露齿低吼；近形不意味着所有义互换。',
 ('The scheme snares people with promises of easy rewards.','这套骗局用轻松获利的承诺把人套进去。'),('We found several old snares beside the fence.','我们在栅栏旁发现几个旧套索。'),sources=S('snares','snare'))
W('snared','英 /sneəd/；美 /snerd/','被套住、捕住了；诱进圈套了；费力争取得到了',
 '人或动物落进圈套、被套牢，用 snared；新闻里 snared a major deal 也可比喻争取到一笔大交易，像终于抓住机会。',
 'snare 去 e + 完整 -ed，词尾读 /d/；形象从套索名词到套住动词，不与 snarled 的低吼混成一条义。',SNARE+[['snare 去 e + -ed → snared','过去套住、诱捕；比喻抓住机会、取得成果']],
 'snared in a trap 是被困进陷阱，snared by a scheme 是中了计；snared a contract 是争取到合同，带抓住机会的语感。',
 'snared by the promise 被承诺诱入；snared in the net 被网困住。',
 'snared 常强调被圈套困住或成功捕获；snarled 可以是龇牙低吼，也可以缠乱，拼写近但动作画面不同。',
 ('Several birds were snared in the abandoned net.','几只鸟被遗弃的网困住了。'),('The small studio snared a major advertising contract.','那家小工作室争取到一份重要广告合同。'),sources=S('snared','snare'))
W('snaring','英 /ˈsneərɪŋ/；美 /ˈsnerɪŋ/','正在套住、捕住、诱进圈套；争取得到',
 '绳圈、网或某个圈套正把目标抓住、困住，是 snaring；谈机会、合同也能比喻费力抓到手。',
 'snare 去 e + 完整 -ing；英式 r 在后接元音时发出来。基础是 snare，不是低吼 snarl 的变形。',SNARE+[['snare 去 e + -ing → snaring','捕住、诱入或抓住机会的过程']],
 'snaring victims 是诱捕受害者，snaring a contract 是争取得到合同；具体善恶、情境由主语和对象说明。',
 'snaring unsuspecting people 诱住没防备的人；snaring a major role 争取到重要角色。',
 'snaring 关注把目标抓到、套住，snarling 在声音语境则是威胁低吼；只看开头 snar- 容易混。',
 ('The scam was snaring people with promises of free prizes.','骗局正用免费奖品的承诺把人诱进去。'),('The young actor hoped for a chance of snaring a major role.','年轻演员希望有机会争取到一个重要角色。'),sources=S('snaring','snare'))
W('rumblings','/ˈrʌmblɪŋz/','隐约的隆隆声；不满、变化等的苗头、风声',
 '远处低低滚来的声音叫 rumblings；比喻还没全面爆发、但已经听得到的一点不满或变化，就是“苗头、风声”。',
 'rumble 去 e + 完整 -ing → rumbling 声音、活动名词，再加复数 -s，读 /z/。不是一次给动词加一个不可分的 -ings 后缀。',
 [['中古英语 rumblen → rumble','低沉、连续声响材料，大概拟声'],['rumble → rumbling → rumblings','隆隆声名词复数；低声抱怨、尚不明显的变化迹象']],
 'rumblings of discontent 是开始传出的不满，rumblings of change 是变化的苗头；不是每次都已形成公开的大抗议。',
 'distant rumblings 远处隆隆声；early rumblings 早期风声、迹象。',
 'rumblings 比 loud protests 更含隐约、尚在酝酿的感觉；与 rumours 传闻可在风声场景接近，但不必每次都是真假未定的消息。',
 ('Distant rumblings of thunder reached us from the hills.','远处山间的隆隆雷声传到我们这里。'),('There were rumblings of discontent about the new schedule.','对新时间表已经开始传出不满的声音。'),sources=S('rumblings','rumble'))
def extend_lessons():
 extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_zfd',ROOTS,WORDS)
 extend_lessons()
