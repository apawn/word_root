"""Bumping, prompting, pulling and effortful movement."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
def S(word,base):
 return ['https://en.wiktionary.org/wiki/'+word+'#English','https://www.etymonline.com/word/'+base]
EXISTING_ROOT_ADDITIONS={
 'A2238':dict(words='jostle jostles jostled jostling'.split(),label='jostle 的相撞材料与反复动作旧尾',note='jostle 早作 justle，联系 joust 的冲撞、比武材料与 -le；现代不发 t，后续变化去 e 加完整词尾。'),
 'B4411':dict(words='tug tugs tugged tugging'.split(),label='tug：抓着往回拉的劲',note='tug 接中古英语 tuggen 与较早英语拉拖词族；名词可说一拽、拖轮，现代 tugged、tugging 双写 g。'),
 'B3614':dict(words='tow tug tugs tugged tugging'.split(),label='tow、tug 的相关拉拖材料',note='两词历史同属日耳曼拉拖材料；tug 更像用力拽，tow 常借绳、链拖曳。现代不是从 tow 按字母替换造出 tug。'),
 'B2811':dict(words='jerk jerks jerked jerking'.split(),label='jerk：突然一拉、一顿；人物义另保留疑问',note='动作词更早来源未定，可比较 yerk；讨厌者人物名词的来路有争议，不把它确定说成身体突动直接引申。食物 jerk 另分来源。'),
 'B4282':dict(words='haul hauls hauled hauling'.split(),label='haul 的费力拉运与所得',note='haul 经中古英语 halen 等接法语、日耳曼拉拖材料；所获一批东西的名词可联系收网所得，长途名词又指运输距离。'),
 'A1760':dict(words='jostle jostles jostled jostling jolt jolts jolted jolting nudge nudges nudged nudging prod prods prodded prodding tug tugs tugged tugging yank yanks yanked yanking jerk jerks jerked jerking haul hauls hauled hauling heave heaves heaved heaving'.split(),label='挤碰、轻推、戳催、拉拽与费力抬动',note='nudged、yanked、jerked、heaved 去不发音 e 或直接加完整 -ed；nudged 读 /dʒd/，yanked、jerked 结尾读 /t/。prodded 词尾读 /ɪd/，双 d。'),
}
JOSTLE=[['较早 joust 的冲撞、比武材料 + -le → justle、jostle','靠近、相撞的材料进入反复动作形式'],['身体推挤 → 争抢位置、注意力等','空间挤在一起，借作利益或关注度的竞争']]
W('jostles','英 /ˈdʒɒsəlz/；美 /ˈdʒɑːsəlz/','挤碰、推挤；争抢位置〔第三人称单数〕；推挤动作〔复数〕',
 '人群里肩膀挤着肩膀，一下下碰，是 jostles；一排广告抢你注意，也像挤在一起争好位置。',
 'jostle + -s，/l/ 后读 /z/；基础 t 在现代通常不发音，末尾 e 保留。旧词联系 joust 与反复动作 -le。',JOSTLE+[['jostle + -s → jostles','它挤碰、争位；几下推挤']],
 'jostles someone in the crowd 是在人群里挤碰某人，jostles for attention 是争夺注意；常用 for 指出争的东西。',
 'jostles for space 争空间；jostles against other passengers 与其他乘客挤碰。',
 'jostles 常有互相挤、空间紧的感觉，nudges 则通常是对某人轻轻一碰；人群挤动未必是在提醒谁。',
 ('The crowd jostles us as we try to reach the exit.','我们想走到出口时，人群挤碰着我们。'),('Each bright sign jostles for attention.','每块鲜亮招牌都在争抢注意力。'),sources=S('jostles','jostle'))
W('jostled','英 /ˈdʒɒsəld/；美 /ˈdʒɑːsəld/','挤碰、推挤了；争抢位置了',
 '刚才被人群前后左右挤了几下，是 jostled；几个人都想占有利位置，也能 jostled for position。',
 'jostle 去末尾 e + 完整 -ed → jostled，/l/ 后读 /d/；t 仍通常不发音。',JOSTLE+[['jostle 去 e + -ed → jostled','过去发生挤碰或位置竞争']],
 'was jostled by the crowd 是被人群挤碰，jostled for a better view 是挤着争更好的视野；前者被动，后者主动。',
 'jostled in the queue 排队时被挤碰；jostled against one another 相互挤撞。',
 'jostled 不一定像 shoved 那样明确有一次用力推人的动作，也可能是拥挤中连续挤碰；是否故意要看上下文。',
 ('She was jostled by the crowd outside the stadium.','她在体育场外被人群挤碰。'),('The photographers jostled for a clear view.','摄影师们挤着争取不受遮挡的视野。'),sources=S('jostled','jostle'))
W('jostling','英 /ˈdʒɒsəlɪŋ/；美 /ˈdʒɑːsəlɪŋ/','正在推挤、挤碰、争位；推挤行为',
 '一群人都朝门口靠，你挤我、我挤你，是 jostling；企业都想抢显眼位置、注意力，也借这种拥挤竞争的画面。',
 'jostle 去末尾 e + 完整 -ing → jostling；t 通常不发音，分词也能把推挤当一类行为。',JOSTLE+[['jostle 去 e + -ing → jostling','身体挤碰或竞争位置的过程']],
 'jostling for position 是争抢位置，jostling through the crowd 是在人群里挤过去；后面 for 或方向能明确场景。',
 'jostling at the entrance 在入口推挤；companies jostling for attention 争抢关注的公司。',
 'jostling 的竞争像在拥挤空间里抢站位，competing 更宽；公平考试、远距离竞赛也可 competing，不必有这种挤的画面。',
 ('People were jostling for position near the entrance.','人们正挤在入口附近争位置。'),('Several new brands are jostling for attention.','几个新品牌正在争抢关注。'),sources=S('jostling','jostle'))
JOLT=[['十六世纪 jolt，可能联系更早敲打、推挤词形','有 jollen、旧 jot 等分析，更早来源尚未定'],['猛烈一震 → 惊醒、震动心理、促使行动','从平顺状态被突然撞醒、拉出，成为现代常见比喻']]
W('jolts','英 /dʒəʊlts/；美 /dʒoʊlts/','颠、震、使猛然醒悟〔第三人称单数〕；颠震、冲击〔复数〕',
 '车轮过坑，整个人被颠一下，是 jolts；突然的消息让人一下清醒，也像受到了猛震。几次颠震则是名词复数。',
 'jolt + -s，/t/ 后读 /s/，结尾 /lts/；三单和名词复数同形。基础词或联系旧敲打材料，远源未定。',JOLT+[['jolt + -s → jolts','它颠震、使惊醒；几次冲击']],
 'jolts the passengers 是颠得乘客一震，jolts someone awake 是把人猛然惊醒；a series of jolts 是接连颠震。',
 'sharp jolts 猛烈的颠震；jolts us into action 让我们一下行动起来。',
 'jolts 常是突然、有冲击的一下，sways 是左右摆；乘车时两种感觉可能都有，却不是同一种移动。',
 ('The bus jolts us whenever it crosses the rough patch.','公交车每次开过坑洼路段，都会把我们颠一下。'),('The old road gave us a series of sharp jolts.','那条旧路把我们接连颠得一震一震。'),sources=S('jolts','jolt'))
W('jolted','英 /ˈdʒəʊltɪd/；美 /ˈdʒoʊltɪd/','颠震、猛撞了；猛然惊醒、醒悟的',
 '刚才车一颠，把人从座位上顶起，是 jolted；听到警报突然醒来、被现实猛然点醒，也能用它。',
 'jolt + 完整 -ed，/t/ 后读 /ɪd/；lt 后直接加，基础元音英 /əʊ/、美 /oʊ/ 保留。',JOLT+[['jolt + -ed → jolted','过去受到颠震；被突然惊醒、点醒']],
 'jolted awake 是猛然惊醒，jolted out of a daydream 是从白日梦中被猛地拉回；by 后可指出触发因素。',
 'jolted into action 受刺激后立即行动；jolted to a stop 颠了一下停住。',
 'jolted awake 常有突然、一下被震醒的感觉，woke up 只说醒了；自然醒来也能 woke up。',
 ('The alarm jolted me awake.','闹钟把我猛然惊醒。'),('The car jolted as it crossed the pothole.','汽车开过坑洞时猛地颠了一下。'),sources=S('jolted','jolt'))
W('jolting','英 /ˈdʒəʊltɪŋ/；美 /ˈdʒoʊltɪŋ/','正在颠震；颠簸的；令人猛然震动、惊醒的',
 '车正一下下过坑，身体跟着震，是 jolting；某个消息突然把人从惯常想法中震出来，也有这种冲击感。',
 'jolt + 完整 -ing，直接加；分词可形容颠震过程，也能形容带来突然心理冲击的事物。',JOLT+[['jolt + -ing → jolting','突然颠震、冲击的过程或效果']],
 'a jolting ride 是颠簸的乘车体验，jolting along the track 是沿路颠着走；a jolting reminder 是让人猛然警醒的提醒。',
 'jolting us awake 把我们猛地惊醒；jolting over stones 越过石块时颠震。',
 'jolting 突出冲击感，rocking 更能说来回摇；摇篮 rocking 可平缓舒服，jolting 通常没那么平顺。',
 ('We spent an hour jolting along the rough track.','我们沿着坑洼小路颠了一个小时。'),('The bus kept jolting us out of our seats.','公交车不停颠得我们离开座位。'),sources=S('jolting','jolt'))
NUDGE=[['可能来自北欧碰擦材料 → 英语 nudge','较早说用胳膊肘轻推、轻碰，具体借入未定'],['轻碰示意 → 提醒、温和促动；小幅移向','像给停着的东西或犹豫的人一点小推力']]
W('nudge','/nʌdʒ/','轻推、轻碰；提醒、温和促使；小幅移动；轻推一下、提醒',
 '用胳膊肘轻碰朋友，示意他看前面，是 nudge；提醒一句，让迟迟没动的人迈出一步，也像轻轻推一把。',
 '可能接北欧语碰擦、推挤材料，早期重点是胳膊肘轻碰；提醒、促动义借这种不显眼的小动作扩展。',NUDGE,
 'nudge someone with your elbow 是用肘轻碰，nudge someone to reply 是提醒对方回复；nudge the chair aside 是轻推挪开椅子。',
 'give someone a nudge 提醒、轻推一下；nudge the price up 使价格小幅上移。',
 'nudge 往往力轻、促动温和，shove 是较用力推；提醒人做事的 nudge 通常也比 force 更有留给对方选择的感觉。',
 ('She gave me a nudge when our friend came into view.','朋友一出现在视线里，她就轻碰了我一下。'),('Could you nudge him to send the photos?','你能提醒他把照片发来吗？'),sources=S('nudge','nudge'))
W('nudges','/ˈnʌdʒɪz/','轻推、轻碰、提醒、微调〔第三人称单数〕；轻推、提醒〔复数〕',
 '一个人轻碰你一下示意，动词用 nudges；几句温和提醒，也像给你几下小推动，是名词 nudges。',
 'nudge + -s，基础已有末尾 e，直接加 s；/dʒ/ 后读 /ɪz/，多一个音节。',NUDGE+[['nudge + -s → nudges','他、她轻碰、提醒；几次小促动']],
 'nudges the door open 是轻推开门，nudges me to finish 是提醒我做完；gentle nudges 是温和提醒。',
 'nudges a cup aside 把杯子轻推开；friendly nudges 友好的提醒。',
 'nudges 可以很轻，也可说数值小幅上移；knocks 常更像敲、撞一下，不自动含有提醒和小幅调整。',
 ('He nudges the door open with his foot.','他用脚把门轻推开。'),('A few friendly nudges helped me finish the application.','几次友好的提醒帮助我把申请填完了。'),sources=S('nudges','nudge'))
W('nudged','/nʌdʒd/','轻推、轻碰、提醒了；小幅推动、挪动了',
 '刚才肘部碰朋友一下，或把杯子轻轻推远一点，是 nudged；一句话温和促成决定，也像小推力起了作用。',
 'nudge 去末尾 e + 完整 -ed → nudged；/dʒ/ 后读 /d/，结尾 /dʒd/，不多一个 /ɪd/ 音节。',NUDGE+[['nudge 去 e + -ed → nudged','过去轻碰、促动或微调']],
 'nudged me awake 是轻碰把我叫醒，nudged the chair closer 是把椅子轻推近；was nudged into trying 是被温和促成尝试。',
 'nudged with an elbow 用肘碰了一下；nudged it towards the edge 把它稍推向边缘。',
 'nudged 描述小力度，jerked 常是突然猛拉或一顿；同样让物体移动，动作的轻重、方向不一样。',
 ('She nudged me with her elbow and pointed at the sign.','她用肘碰了我一下，指向招牌。'),('He nudged the cup away from the edge of the table.','他把杯子从桌边轻轻往里推了推。'),sources=S('nudged','nudge'))
W('nudging','/ˈnʌdʒɪŋ/','正在轻推、轻碰、提醒、微调；温和促动',
 '手正把小东西轻推一点，或人正通过一点点提示让别人行动，是 nudging；重点像增加一小股推力。',
 'nudge 去末尾 e + 完整 -ing → nudging；g 在 i 前仍读 /dʒ/，形成动作分词、动作名词。',NUDGE+[['nudge 去 e + -ing → nudging','轻推、温和促使的过程']],
 'nudging someone to answer 是提醒人回答，nudging a door closed 是轻推关门；numbers nudging higher 是数字小幅走高。',
 'gentle nudging 温和促动；nudging it into place 轻推到位。',
 'nudging 更像提供小推动，ordering 明确下命令；同一个任务里，提醒与命令会让人感到不同的语气。',
 ('The dog kept nudging my hand for attention.','狗不停轻碰我的手，想让我理它。'),('Her gentle nudging encouraged me to try again.','她温和的催促鼓励我再试一次。'),sources=S('nudging','nudge'))
PROD=[['十六世纪 prod 的用棍戳动材料','来源未定，可能是旧 brod 一系变体，或有拟声基础'],['戳动 → 催促、激起行动；戳一下的名词','像给迟迟不动的对象一记较明确的刺激']]
W('prod','英 /prɒd/；美 /prɑːd/','戳、捅；催促、促使；戳一下、催促',
 '用棍子戳戳土、用手指戳一下靠垫，是 prod；催一个迟迟没动的人，也像戳一下让他赶紧行动。',
 '较早说拿棍子戳，来源未定；可能联系旧 brod、北欧尖刺材料，也有拟声分析。现代 prod 不当作 pro- 加一个字母 d 来拆。',PROD,
 'prod something with a stick 是拿棍戳，prod someone into action 是催人行动；give someone a prod 是催一下。',
 'prod gently 轻戳；prod someone to reply 催人回复。',
 'prod 比 nudge 更容易像明确戳、催一下，nudge 通常更轻、更含蓄；两者都可说提醒，但力度感觉不同。',
 ('He used a stick to prod the soft ground.','他拿棍子戳了戳松软地面。'),('She needed a prod to finish the report.','她需要有人催一下，才把报告写完。'),sources=S('prod','prod'))
W('prods','英 /prɒdz/；美 /prɑːdz/','戳、催促〔第三人称单数〕；戳动、催促〔复数〕',
 '一个人用手指或棍子戳，动词用 prods；几次提醒像小小刺激，叫 a few prods，催你从停着变成行动。',
 'prod + -s，/d/ 后读 /z/，结尾 /dz/；动词三单和戳动名词复数同形。',PROD+[['prod + -s → prods','他、她戳动、催促；几下戳动或提醒']],
 'prods the ground 是戳地面，prods me to reply 是催我回复；gentle prods 可以是几次轻戳，也可以温和催促。',
 'prods with a finger 用手指戳；needs a few prods 得催几下。',
 'prods 如果接动作、不定式，常说催促；如果接被戳物体和 with a stick，常是实际接触，句型能把两义接起来。',
 ('She prods the soil with a stick to test how soft it is.','她拿棍子戳土，试试有多软。'),('He needed a few gentle prods before he sent the form.','他得经过几次温和催促，才把表格寄出。'),sources=S('prods','prod'))
W('prodded','英 /ˈprɒdɪd/；美 /ˈprɑːdɪd/','戳了、捅了；催促、促使了',
 '刚才用棍、指头碰进去戳一下，是 prodded；一句提醒把人从拖延中推出来，也可以 prodded someone into action。',
 'prod 双写 d + 完整 -ed → prodded；/d/ 后词尾读 /ɪd/，整词两个音节。',PROD+[['prod 双写 d + -ed → prodded','过去戳动、催动']],
 'prodded the cushion 是戳靠垫，prodded her to apply 是催她申请；was prodded into action 是被催得行动起来。',
 'prodded with a stick 用棍戳了；prodded him gently 轻戳或温和催了他。',
 'prodded 是短元音、双 d、加 /ɪd/，而 nudged 末尾 /dʒd/ 不加音节；两者都能催促，形态和发音不同。',
 ('He prodded the cushion with one finger.','他用一根手指戳了戳靠垫。'),('Her question prodded me into checking the figures.','她的问题促使我去核对数字。'),sources=S('prodded','prod'))
W('prodding','英 /ˈprɒdɪŋ/；美 /ˈprɑːdɪŋ/','正在戳、捅、催促；催促、刺激',
 '指头正一下下戳，或有人一遍遍催你做事，是 prodding；名词用法把这些推动当作一个整体。',
 'prod 双写 d + 完整 -ing → prodding；动词分词或动作名词，基础短元音保留。',PROD+[['prod 双写 d + -ing → prodding','戳动、催促的过程或行为']],
 'stop prodding it 是别再戳它，after some prodding 是经过一点催促；第二种把催人看作一股刺激。',
 'with gentle prodding 在温和催促下；prodding someone into action 催人行动。',
 'prodding 常让人觉得原本没动、需要外界刺激；encouragement 更广，可以是鼓舞、支持，不必带催的感觉。',
 ('Stop prodding the cushion with your pencil.','别再拿铅笔戳靠垫了。'),('After some prodding, he finally shared his idea.','催了几次后，他终于说出了自己的想法。'),sources=S('prodding','prod'))
TUG=[['中古英语 tuggen 与较早英语拉拖词族 → tug','与 tow 的历史拉取材料相关，现代形式各自固定'],['用力拉 → 一拽、拖轮等名词','把东西拉近的动作，也借给引起牵挂、注意等心理感觉']]
W('tugs','/tʌɡz/','用力拽、拉扯〔第三人称单数〕；几下拽拉、拖轮〔复数〕',
 '孩子拉你的袖子想让你注意，动词用 tugs；码头上拉大船的小动力船也叫 tugs，名字来自它做的拉拖工作。',
 'tug + -s，/ɡ/ 后读 /z/；拉扯三单与拉动、拖轮名词复数同形，基础词联系较早拉拖材料。',TUG+[['tug + -s → tugs','他、她拉扯；几下拉动或多艘拖轮']],
 'tugs at a sleeve 是拉袖子，gives a few tugs 是拽几下；harbour tugs 是港内拖轮。',
 'tugs on the rope 拉绳；tugs at the heartstrings 触动心弦。',
 'tugs 常让人看到手抓住后用力拉，nudges 是小力度推碰；码头的 tugs 又是按拉拖用途命名的船。',
 ('The child tugs at her father\'s sleeve.','孩子拉着爸爸的袖子。'),('Two tugs guided the large ship into the harbour.','两艘拖轮引导大船驶进港口。'),sources=S('tugs','tug'))
W('tugged','/tʌɡd/','用力拽、拉扯了；牵动了',
 '刚才抓住绳、衣角使劲拉，是 tugged；某种情感像小手拉你回头，也能 tugged at something，说内心被牵动。',
 'tug 双写 g + 完整 -ed → tugged，/ɡ/ 后读 /d/；短元音重读单音节按规则双写。',TUG+[['tug 双写 g + -ed → tugged','过去用力拽、牵动']],
 'tugged at my sleeve 是拉了我的袖子，tugged the rope free 是拽脱绳子；at、on 可突出抓着某处拉。',
 'tugged hard 用力拉；tugged at her heartstrings 触动她的心弦。',
 'tugged 说用力拉的动作，dragged 更常写东西沿着表面被拖动；拽了一下没拉动，也能 tugged。',
 ('He tugged at the rope, but the knot held firm.','他拽了拽绳子，但结还是很牢。'),('The child tugged my sleeve to get my attention.','孩子拉了拉我的袖子，想让我注意他。'),sources=S('tugged','tug'))
W('tugging','/ˈtʌɡɪŋ/','正在用力拽、拉扯；拉扯动作、牵动',
 '手抓住绳头一下一下往回使劲，是 tugging；衣角被风不断牵拉，也可写成同一个反复拉扯画面。',
 'tug 双写 g + 完整 -ing → tugging；双写只保留拼写模式，不多发一遍 /ɡ/。',TUG+[['tug 双写 g + -ing → tugging','拉扯、牵动的过程']],
 'tugging at a sleeve 是正在拉袖子，tugging on a rope 是使劲拉绳；keep tugging 是继续拽。',
 'tugging it loose 使劲拽松；a tugging sensation 像被牵拉的感觉。',
 'tugging 往往能连续、反复，yanking 更常突出某一下突然猛拽；同一次拉扯里可以先 tug 再 yank。',
 ('She kept tugging at the stuck drawer.','她不停用力拉那个卡住的抽屉。'),('The wind was tugging at the loose corner of the tent.','风正不断扯动帐篷松开的角。'),sources=S('tugging','tug'))
YANK=[['近代苏格兰英语 yank','来源未定；较早名词有突然一击，动词说急拉，不能只按现代词性倒排先后'],['突然急拉 → 猛拽、迅速撤下、抽走','现代画面像抓住后一下把对象从原处拉走']]
W('yank','/jæŋk/','猛拉、猛拽；突然撤下、拿走；猛拽一下',
 '抓着卡住的绳子，突然使劲一拽，是 yank；一个节目被迅速撤掉，也像被人一下从原位拉走。',
 '动作词见于近代苏格兰英语，更早来源未定；较早名词已可说突然一击。大写 Yank 是 Yankee 的简称，近源另分。',YANK,
 'yank the door open 是猛拉开门，yank a cable out 是猛拽出线缆；yank a programme off the air 是突然撤下节目。',
 'give it a yank 猛拽一下；yank something away 猛地拉走。',
 'yank 比 pull 更突出突然、用力；pull 可以缓缓拉，yank 往往让人看见一次急促动作。',
 ('He gave the stuck handle a yank.','他猛拽了一下卡住的把手。'),('She had to yank the rope to free it from the branch.','她得猛拽绳子，才能把它从树枝上弄下来。'),sources=S('yank','yank'))
W('yanks','/jæŋks/','猛拉、猛拽、突然撤下〔第三人称单数〕；猛拽动作〔复数〕',
 '一个人抓住就用力急拉，是 yanks；几下突然猛拽也可当名词复数。别把轻轻调整也想成这种力度。',
 'yank + -s，/k/ 后读 /s/，结尾 /ŋks/；三单与猛拽名词复数同形，大写人物名另按自身来源理解。',YANK+[['yank + -s → yanks','他、她猛拽；几下急拉']],
 'yanks the handle 是猛拽把手，yanks it free 是猛拉使其脱开；a few yanks 是几下猛拽。',
 'yanks open the drawer 猛拉开抽屉；yanks it away 猛地把它拉走。',
 'yanks 与 nudges 的力感差很大：一个急拽，一个轻推碰；看不清动作时，别把二者都平平译作“动了一下”。',
 ('He yanks the bell rope to call the others.','他猛拉铃绳，叫其他人过来。'),('A few strong yanks freed the trapped rope.','猛拽了几下，卡住的绳子终于松脱。'),sources=S('yanks','yank'))
W('yanked','/jæŋkt/','猛拉、猛拽了；突然撤下、抽走了',
 '刚才突然用力一拉，把东西从原处拉开，是 yanked；一个人或节目被迅速撤出原来的位置，也保留这股一下拉走的感觉。',
 'yank + 完整 -ed，/k/ 后读 /t/，结尾 /ŋkt/；nk 后直接加，不双写 k。',YANK+[['yank + -ed → yanked','过去急拽或迅速撤走']],
 'yanked the rope 是猛拉绳子，yanked it out 是猛地拽出；was yanked from the schedule 是突然从安排中撤下。',
 'yanked open the door 猛拉开门；yanked away 突然拉走。',
 'yanked 把突然、用力的方式说出来，removed 只说移除结果；同一件事用 yanked 会更有动作感。',
 ('He yanked the drawer open and looked inside.','他猛地拉开抽屉，向里面看。'),('The show was yanked from the schedule after one episode.','那档节目播了一集就突然被撤出节目表。'),sources=S('yanked','yank'))
W('yanking','/ˈjæŋkɪŋ/','正在猛拉、猛拽、迅速撤走；猛拽行为',
 '正抓住东西一下下急拉，是 yanking；和温和晃松相比，它有明显突然用力的感觉。',
 'yank + 完整 -ing，直接加；nk 保留，词尾接到整个急拉动词上。',YANK+[['yank + -ing → yanking','猛拽、急拉的过程']],
 'yanking on the rope 是正在猛拽绳子，yanking something away 是猛地拉走；keep yanking 可以是几次接连急拽。',
 'yanking the handle 猛拽把手；yanking it free 猛拉使它脱开。',
 'yanking 强调急拉，hauling 常突出费力、较持续地拉运；一船货物慢慢拉进港，可以 hauling，不必一直猛拽。',
 ('He was yanking on the rope, trying to free the gate.','他正猛拽绳子，想把门弄开。'),('She opened the drawer by yanking hard on the handle.','她猛拽把手，把抽屉打开了。'),sources=S('yanking','yank'))
JERK=[['较早 jerk 的抽打、急拉材料','更远来源未定，可比较 yerk 等形式，不用统一来路包办所有同形词'],['突然一拉、一顿 → 突动名词；人物贬称另有争议','动作现代常见；讨厌者义不写成由突动直接引申的确定路线']]
W('jerks','英 /dʒɜːks/；美 /dʒɜːrks/','突然猛拉、猛动〔第三人称单数〕；突动、猛拉；讨厌的人〔复数〕',
 '身体、机器忽然一顿，动词用 jerks；走走停停的一下一下，是动作名词复数。骂人 jerks 则是说几个人没礼貌、惹人讨厌。',
 'jerk + -s，/k/ 后读 /s/；动作三单、突动名词与人物名词复数同形，人物义来源另有争议。',JERK+[['jerk + -s → jerks','它突然一动；几次突动；多人评价']],
 'jerks forward 是猛地向前一顿，in short jerks 是一顿一顿地；a bunch of jerks 是一群惹人讨厌的家伙。',
 'jerks the rope 猛拉绳子；sudden jerks 突然的几下抖动。',
 'jerks 的人物用法带贬义，动作里的短促抖动则不含人物评价；词性、句型会把它们分清。',
 ('The machine jerks forward when it starts.','机器启动时会猛地向前一顿。'),('The drawer came open in short jerks.','抽屉一顿一顿地被拉开了。'),sources=S('jerks','jerk'))
W('jerked','英 /dʒɜːkt/；美 /dʒɜːrkt/','突然猛拉、猛动了；一顿、抽动了',
 '手碰到烫处，立刻猛地缩回，是 jerked；车突然一顿，也能用它。核心是动作短、突然，不平顺。',
 'jerk + 完整 -ed，/k/ 后读 /t/；rk 后直接加词尾，结尾不是 /ɪd/。',JERK+[['jerk + -ed → jerked','过去急促拉动或突然一动']],
 'jerked his hand away 是猛地缩开手，jerked the door open 是猛拉开门；jerked awake 是猛然惊醒。',
 'jerked backwards 猛地向后一顿；jerked his head towards the door 突然转头示意门口。',
 'jerked 常更短促，hauled 更像花力气持续拉、搬；把重箱子一路拖进屋，用 hauled 比 jerked 更能交代全程。',
 ('He jerked his hand away from the hot handle.','他猛地把手从烫的把手上缩回来。'),('The bus jerked to a stop.','公交车猛地一顿停住了。'),sources=S('jerked','jerk'))
W('jerking','英 /ˈdʒɜːkɪŋ/；美 /ˈdʒɜːrkɪŋ/','正在猛拉、突动、抽动；一顿一顿的动作',
 '一根绳被急促拉几下，机器不是平顺动而是走一下顿一下，是 jerking。这个词让人看见动作被分成短促的冲击。',
 'jerk + 完整 -ing，直接加；rk 保留，可作分词或把突动看作一种动作的名词。',JERK+[['jerk + -ing → jerking','突然拉动、抖动的过程']],
 'jerking the rope 是正猛拉绳子，jerking forward 是一顿一顿向前；a jerking movement 是突然抽动。',
 'jerking from side to side 突然左右动；keep jerking 不停短促拉动。',
 'jerking 与 gliding 的移动感觉很不同：一个短促不连贯，一个顺滑；不只是在说哪个更快。',
 ('He was jerking the rope to loosen the knot.','他正急促拉动绳子，想把结弄松。'),('The old machine kept jerking forward.','旧机器一直一顿一顿地向前动。'),sources=S('jerking','jerk'))
HAUL=[['中古英语 halen，接法语、日耳曼拉拖材料 → haul','现代 haul 由较早变体、拼写演变固定下来'],['费力拉运 → 一批所得；一段运输路程','收网拉得的东西可作所得画面，路程名词另联系拉运距离']]
W('hauls','英 /hɔːlz/；美 /hɔːlz/','费力拉、搬运〔第三人称单数〕；所得、捕获、运输路程〔复数〕',
 '卡车把沉重货物一路运走，或人把大箱子费劲拉上去，动词用 hauls；几批收获、购得的东西，也能叫 hauls。',
 'haul + -s，/l/ 后读 /z/；动词三单和所得、运输路程等名词复数同形，现代多条分支接拉运画面。',HAUL+[['haul + -s → hauls','它拉运；多批所得或多段运输']],
 'hauls logs 是拉运木料，hauls himself up 是费劲把自己撑上去；shopping hauls 是几批买回来的东西。',
 'hauls the boat ashore 把船拖上岸；large hauls of fish 大批捕获的鱼。',
 'hauls 强调搬拉有重量、距离或费力感，carries 只要携带；轻松拿一本小书也可 carry，通常不必 haul。',
 ('The truck hauls timber down from the hills.','卡车把木料从山上运下来。'),('The fishermen returned with large hauls of fish.','渔民们带着大批捕获的鱼回来。'),sources=S('hauls','haul'))
W('hauled','英 /hɔːld/；美 /hɔːld/','费力拉、拖、搬运了；把自己撑起、拽上了',
 '刚才把重物拖过地面，或用手把自己拉上岸，是 hauled。它让人感觉到了重量、阻力和花的那股劲。',
 'haul + 完整 -ed，/l/ 后读 /d/；拼写直接加，au 仍保留基础长元音。',HAUL+[['haul + -ed → hauled','过去费力拉运或抬撑']],
 'hauled the box upstairs 是把箱子费力搬上楼，hauled himself out 是费劲把自己弄出来；动作可由人或车辆完成。',
 'hauled ashore 拖上岸；hauled away 拉运走。',
 'hauled 不限定往上拉，沿地面、长距离运送都可以；lifted 更明确离开支撑面向上抬。',
 ('We hauled the heavy boxes up the stairs.','我们费劲把重箱子搬上楼。'),('He hauled himself out of the water.','他费力把自己撑出水面。'),sources=S('hauled','haul'))
W('hauling','英 /ˈhɔːlɪŋ/；美 /ˈhɔːlɪŋ/','正在费力拉、拖、搬运；运输、拖运工作',
 '人抓着重箱把它一路往前拖，或车一趟趟运木料，是 hauling；可看作眼前动作，也可把拉运当一类工作。',
 'haul + 完整 -ing，直接加；分词、动作名词都保留较费力或带负载的移动感觉。',HAUL+[['haul + -ing → hauling','拉运过程；运输工作']],
 'hauling timber 是运木料，hauling a boat onto the beach 是把船拖上滩；hauling costs 是运输费用。',
 'heavy hauling 重货运输；hauling it upstairs 把它费劲搬上楼。',
 'hauling 比 tugging 更容易说较完整的搬运过程，tugging 常聚焦手抓着一处拽；可以先 tug 松，再 haul 走。',
 ('They spent the morning hauling branches out of the garden.','他们整个上午都在把树枝拖出花园。'),('The truck was hauling building materials to the site.','卡车正往工地运送建筑材料。'),sources=S('hauling','haul'))
HEAVE=[['古英语 hebban → 中古英语 heven → heave','举起、抬高，较远属于抓住、提起的材料'],['费力抬动 → 拉、投；身体起伏、用力叹气、干呕','现代看所带对象：重物、胸口、叹息或胃的反应会带出不同搭配']]
W('heaves','/hiːvz/','费力举、拉、投；起伏、干呕〔第三人称单数〕；用力抬拉、干呕〔复数〕',
 '人使劲把箱子提起，胸口剧烈起伏，或深深叹一口气，都能用 heaves。共同感觉像从身体里用上一股向上、向外的力。',
 'heave + -s，/v/ 后读 /z/，结尾 /vz/；动词三单、抬拉动作名词复数等同形。古义重点是举起、抬高。',HEAVE+[['heave + -s → heaves','他、她费力抬动；胸口等起伏；多次用力或干呕']],
 'heaves a sigh 是长叹一口气，chest heaves 是胸口明显起伏；the dry heaves 是干呕，不需要有东西抬起来。',
 'heaves the sack onto the truck 把袋子使劲抬上车；heaves with effort 使劲地起伏。',
 'heaves a sigh 把深重、长长一口气描出来，breathes 只说呼吸；喘、叹、干呕须由搭配分清。',
 ('She heaves the heavy bag onto the bench.','她使劲把重包抬上长椅。'),('He heaves a sigh of relief when the door opens.','门一开，他长长舒了一口气。'),sources=S('heaves','heave'))
W('heaved','/hiːvd/','费力抬、拉、投了；起伏、叹气、干呕了',
 '刚才鼓足劲把重箱抬进车里，是 heaved；终于放松后长叹一口气，也说 heaved a sigh。',
 'heave 去末尾 e + 完整 -ed → heaved，/v/ 后读 /d/；古英语曾是强变化动词，现代这个规则形式明确可用。',HEAVE+[['heave 去 e + -ed → heaved','现代规则过去式；过去用力、起伏或叹气']],
 'heaved the box onto the shelf 是使劲把箱子抬上架，heaved a sigh 是深叹一口气；the sea heaved 是海面起伏。',
 'heaved himself up 费力把自己撑起；heaved with sobs 抽泣得胸口起伏。',
 'heaved 比 lifted 多了用力、沉重的感觉；一根轻羽毛也能 lifted，而 heaved 往往让人感到负担、劲头。',
 ('We heaved the heavy box into the van.','我们使劲把重箱子抬进货车。'),('She heaved a long sigh and closed the book.','她长叹一口气，合上了书。'),sources=S('heaved','heave'))
W('heaving','/ˈhiːvɪŋ/','正在费力抬拉、起伏、干呕；〔英口语〕拥挤热闹的',
 '重物正被使劲抬，人的胸口正上下起伏，是 heaving；英国口语说 a heaving pub，则像一屋人挤满、动个不停，表示很挤很热闹。',
 'heave 去末尾 e + 完整 -ing → heaving；除动作分词外，还固定出拥挤、热闹的形容用法。',HEAVE+[['heave 去 e + -ing → heaving','用力、起伏过程；人多拥挤的形容']],
 'a heaving chest 是起伏明显的胸口，heaving a box 是正使劲抬箱子；the place was heaving 是那个地方挤满了人。',
 'heaving with people 挤满人；heaving up and down 上下起伏。',
 'heaving 的拥挤义是英式口语场景，crowded 更中性；说胸口 heaving 则仍在描写真实起伏。',
 ('He stood with his chest heaving after the run.','跑完后，他站在那里，胸口剧烈起伏。'),('The market was heaving with people by noon.','到中午时，市场已经挤满了人。'),sources=S('heaving','heave'))

def extend_lessons():
 extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_zfo',ROOTS,WORDS)
 extend_lessons()
