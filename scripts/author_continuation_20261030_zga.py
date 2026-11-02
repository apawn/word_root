"""Brief looks, fleeting views, fixed attention and effortful looking."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
def S(word,base):
 return ['https://en.wiktionary.org/wiki/'+word+'#English','https://www.etymonline.com/word/'+base]
EXISTING_ROOT_ADDITIONS={
 'C0483':dict(words='glance glances glanced glancing'.split(),label='glance 的斜擦与一眼扫过',note='glance 的斜擦材料常联系法语 glace 冰、glacier 滑；快速看义又可能受 glenten 影响。不是看一眼就必然由冰的核心意思直接推出。'),
 'B2591':dict(words='see glimpse glimpses glimpsed glimpsing'.split(),label='glimpse 与 see：短暂看到片段和一般看见',note='本支是近义画面对照，glimpse 与 see 不作同源归并。glimpse 可能接日耳曼发微光材料，推定古英语 *glimsian 不能当作实证；see 则有自己的古英语 seon 来源。'),
 'B2761':dict(words='look stare stares stared staring'.split(),label='stare 与 look：定住的目光和一般看',note='本支按近义动作对照，不把 stare 当作 look 的同源派生。stare 承古英语 starian，较远接僵直、固定材料；look 则承 locian，现代 stare 也不一律含无礼。'),
 'B4041':dict(words='gap gape gapes gaped gaping'.split(),label='gape：嘴张开，开口也张大',note='gape 与 gap 的张口、敞开材料相关；具体本族延续与北欧借入的分析有不同。现代 gaped 的 -ed 在 /p/ 后读 /t/。'),
 'A1760':dict(words='peer peered peering gaze gazes gazed gazing'.split(),label='peer、gaze 的不同凝视画面与词形',note='动词 peer 的费力看材料与名词 peer 同辈、贵族的拉丁 par 来源分开。gaze 可能接北欧凝看材料，具体远源未定；这里并列比较，不强接为一个词根。'),
}
GLANCE=[['古法语滑、斜擦材料 → 中古英语 glacen 等 → glance','现代带 n 的形式涉及历史变化，另有混合来源分析'],['斜擦、迅速闪过；快速看义可能另受 glenten 影响','现代用 glance 写很快扫一眼，也保留斜擦、擦过的用法']]
W('glances','英 /ˈɡlɑːnsɪz/；美 /ˈɡlænsɪz/','扫一眼〔第三人称单数〕；匆匆一瞥〔复数〕',
 '眼睛在钟面上一扫就移开，叫 glances at the clock；两个人交换几个短暂眼神，名词也用 glances。',
 'glance + -s，/s/ 后词尾读 /ɪz/；名词复数与动词三单同形。基础词有斜擦材料与快速看材料的复杂联系。',GLANCE+[['glance + -s → glances','他、她快速看；几次一瞥']],
 'glances at the clock 扫一眼钟；exchange glances 交换眼神；furtive glances 偷瞥。',
 'quick glances；glances around the room。',
 'glances 强调看的动作短，stares 强调目光停住；一眼看没看清，需再看上下文。',
 ('She glances at the clock before answering.','回答前，她扫了一眼钟。'),('We exchanged worried glances across the table.','我们隔着桌子交换了担忧的眼神。'),sources=S('glances','glance'))
W('glanced','英 /ɡlɑːnst/；美 /ɡlænst/','扫了一眼；斜擦、擦过了',
 '刚才目光飞快落一下就移开，是 glanced；球斜着碰到边缘又弹走，也可说 glanced off。两个画面都保留轻快、斜过的感觉，但历史来路不简化成唯一比喻。',
 'glance 去 e 加完整 -ed，/s/ 后词尾读 /t/，结尾 /nst/。',GLANCE+[['glance → glanced','过去快速看，或物体斜擦、偏开']],
 'glanced at someone 看了某人一眼；glanced through the report 粗略浏览报告；glanced off the post 斜擦过柱子。',
 'glanced over his shoulder 回头瞥一眼；glanced down at the screen。',
 'glanced through 是很快浏览，scrutinized 则是仔细审查；同样处理报告，投入的注意不同。',
 ('He glanced at the message and put his phone away.','他扫了一眼消息，就收起了手机。'),('The ball glanced off the post and went wide.','球斜擦过门柱，偏到了一边。'),sources=S('glanced','glance'))
W('glancing','英 /ˈɡlɑːnsɪŋ/；美 /ˈɡlænsɪŋ/','正在扫视；斜擦的；粗略的',
 '人正不时扫一眼门口，是 glancing at the door；击打只斜斜擦到、没正面打中，则是 a glancing blow。',
 'glance 去 e 加 -ing；可作进行形式，也可形容接触很浅、斜擦而过，或关注粗略。',GLANCE+[['glance → glancing','短暂看或斜擦正在发生；也描述轻浅、擦过的性质']],
 'glancing at a watch 扫一眼手表；a glancing blow 斜擦的一击；a glancing reference 一带而过的提及。',
 'kept glancing back 不停回头瞥；glancing over the page。',
 'glancing blow 重点是斜擦、未正面承受，不能只因有 glance 就译成用眼睛看的一击。',
 ('She kept glancing at the door while we talked.','我们谈话时，她不停往门口瞥。'),('The branch struck him a glancing blow on the shoulder.','树枝斜擦着击中了他的肩膀。'),sources=S('glancing','glance'))
GLIMPSE=[['中古英语闪光、发亮材料 → glimpse','可能联系推定古英语 *glimsian；带 p 的变化有语音解释，远源仍保留可能性'],['短暂、微弱地显现 → 不完整的一眼、短暂看见','现代常说 catch a glimpse of，看到一点而非完整细看；较早 glimpsing 记录也很早']]
W('glimpse','/ɡlɪmps/','瞥见；短暂、不完整的一眼；初步了解',
 '火车一闪而过，你只看到窗边一张脸；门开了一下，只看见里面一点，这份短暂、不完整的看见叫 a glimpse。',
 '接较早闪光、微现材料，可能承推定古英语 *glimsian；现代按整词保留，名词、动词都能用。',GLIMPSE,
 'catch a glimpse of someone 瞥见某人；glimpse the sea 短暂看见海；a glimpse into daily life 对日常生活的一点了解。',
 'a brief glimpse；a glimpse of the future。',
 'glance 更侧重快速看这个动作，glimpse 更侧重短暂看到的片段；glance at 可以没看清，catch a glimpse 则至少看见一点。',
 ('I caught a glimpse of the sea between the houses.','我从房屋间的缝隙里瞥见了大海。'),('The diary offers a glimpse into her daily life.','这本日记让人略知她的日常生活。'),sources=S('glimpse','glimpse'))
W('glimpses','/ˈɡlɪmpsɪz/','片刻、零星的看见〔复数〕；短暂瞥见〔第三人称单数〕',
 '帘子一动，看见一点；人群一散，又看见一点，这几次不完整的片段叫 glimpses；他短暂看到，动词也同形。',
 'glimpse + -s，基础 /s/ 后词尾读 /ɪz/，/mps/ 保留；名词复数与动词三单同形。',GLIMPSE+[['glimpse + -s → glimpses','多个短暂片段；他、她短暂看见']],
 'catch glimpses of 偶尔、片刻看见；glimpses into the past 对过去的一些片段了解。',
 'brief glimpses；glimpses of the mountain between clouds。',
 'glimpses 常暗示视野不完整或时间很短；a clear view 则强调看得清楚，两者关注点不同。',
 ('We caught glimpses of the mountain between the clouds.','我们从云缝里不时瞥见那座山。'),('The letters offer brief glimpses into their life together.','这些信让人零星了解他们共同生活的片段。'),sources=S('glimpses','glimpse'))
W('glimpsed','/ɡlɪmpst/','短暂瞥见了；看到了一点',
 '车窗一掠，远处的塔刚露出来又被挡住；这种只抓住一瞬的看见，过去式是 glimpsed。',
 'glimpse 去 e 加完整 -ed，/s/ 后词尾读 /t/，结尾 /mpst/；不把它读成多一个 /ɪd/。',GLIMPSE+[['glimpse → glimpsed','过去短暂看到一个片段']],
 'glimpsed a face 瞥见一张脸；glimpsed through the doorway 从门口短暂看到。',
 'briefly glimpsed；glimpsed in passing 路过时瞥见。',
 'glimpsed 常不要求故意去看；glanced at 则写目光主动短暂投向某物的动作。',
 ('I glimpsed her face through the train window.','我透过火车窗，短暂看见了她的脸。'),('We glimpsed a tower above the trees.','我们从树梢上方瞥见了一座塔。'),sources=S('glimpsed','glimpse'))
W('glimpsing','/ˈɡlɪmpsɪŋ/','正在短暂看见、瞥见；片刻看见的过程',
 '路边的树一段段挡住视线，你偶尔从缝里看到海，这种不完整的看见过程，可以写 glimpsing。',
 'glimpse 去 e 加 -ing，保留基础 /mps/；早期英语相关动作名词记录也很早，现代形式按 glimpse 加词尾理解。',GLIMPSE+[['glimpse → glimpsing','短暂、片段式看见的动作形式']],
 'glimpsing the sea 短暂看到海；without glimpsing a face 连脸的一瞥也没看到；after glimpsing 瞥见之后。',
 'keep glimpsing something 不时瞥见；glimpsing life beyond the town 略窥镇外生活。',
 'glimpsing 更像抓到片段，watching 可以持续观看；连续看一场演出通常不只用 glimpsing。',
 ('We kept glimpsing the sea through gaps in the trees.','我们不时从树木间的空隙里瞥见海。'),('After glimpsing the note, she quickly closed the drawer.','瞥见那张纸条后，她赶紧关上抽屉。'),sources=S('glimpsing','glimpse'))
PEER=[['中古英语 piren 等看、凝看的材料 → peer 动词','可能联系东弗里斯兰语材料，另受 appear 的缩短形式影响，远源未定'],['现代 peer：努力、仔细地看','同辈、贵族名词另接拉丁 par 相等；不能从同辈直接推成看']]
W('peered','英 /pɪəd/；美 /pɪrd/','仔细、费力地看了；探头看了',
 '光线暗、字太小，或东西被挡了一点，于是把头凑近、眼睛努力去看，过去这个动作叫 peered。',
 '看这个动词 peer + -ed，词尾读 /d/；同拼写的同辈名词是另一来源，不是这里的历史起点。',PEER+[['peer + -ed → peered','过去努力看清或仔细探看']],
 'peered into the darkness 向黑暗里费力看；peered over the glasses 从眼镜上方仔细看。',
 'peered through a crack；peered at the small print。',
 'stared 不一定看不清，只是目光停住；peered 常让人觉得对象不易看清，人在努力辨认。',
 ('She peered through the window to see whether anyone was inside.','她凑到窗边仔细看，想知道里面有没有人。'),('He peered at the tiny print on the ticket.','他费力地看票上那些小字。'),sources=S('peered','peer'))
W('peering','英 /ˈpɪərɪŋ/；美 /ˈpɪrɪŋ/','正在费力、仔细地看；网络对等互联',
 '凑近门缝、眯着眼辨认小字，正在努力看清的过程叫 peering；网络语境另有同辈、对等的 peer 派生出的互联名词。',
 '看这个动词 peer + -ing；网络名词也写 peering，但接对等的 peer 名词材料，词源分路，不能都从凝视推出。',PEER+[['peer + -ing → peering','看这一支是正在努力辨认；对等这一支另形成网络互联名词']],
 'peering into the distance 努力看远处；peering over a wall 探头看墙外；网络 peering agreement 是对等互联协议。',
 'peering through the fog；peering at the screen。',
 '读 peering 时先看是不是眼睛、视线的场景；网络协议里的同形名词需要回到对等的另一支理解。',
 ('He was peering into the fog, trying to find the path.','他正努力往雾里看，想找出小路。'),('She stood on tiptoe, peering over the wall.','她踮着脚，探头往墙外看。'),sources=S('peering','peer'))
STARE=[['古英语 starian → stare','睁着眼定定地看，较远接僵直、固定的日耳曼材料'],['固定的目光 → 惊讶、发呆、强硬对视等场景','现代可含不礼貌，但不是每次 stare 都带无礼；名词也表示一段定定的注视']]
W('stare','英 /steə/；美 /ster/','盯着看；凝视；定定的一眼',
 '眼睛停在一个地方，半天没移开，像目光被定住，就是 stare。可能惊讶、走神，也可能是在强硬地看人。',
 '承古英语 starian，较远联系固定、僵直的旧材料。现代名词也可指这种定定的注视。',STARE,
 'stare at someone 盯着某人；stare into space 发呆；give someone a stare 定定看某人一眼。',
 'a blank stare 茫然的目光；stare someone down 盯得某人先移开眼。',
 'stare 强调目光固定；gaze 更常让人感觉专注、入神，但两者在长时间看的场景有交叠。',
 ('It is hard not to stare at the enormous painting.','那幅画太大，让人很难不盯着看。'),('He gave me a blank stare.','他茫然地盯着我。'),sources=S('stare','stare'))
W('stares','英 /steəz/；美 /sterz/','盯着看〔第三人称单数〕；定定的注视〔复数〕',
 '她看着那面墙一动不动，动词用 stares；几个人把目光定在同一人身上，名词就能用 stares。',
 'stare + -s，词尾读 /z/；名词复数与动词三单同形，英式此处通常没有单独发出的 r。',STARE+[['stare + -s → stares','他、她定定看；多道、几次固定的目光']],
 'stares at the ceiling 盯着天花板；curious stares 好奇的注视；draws stares 引得人们盯着看。',
 'stares into space；uncomfortable stares。',
 'stares 可让被看的人不自在，但也能写惊奇、茫然；具体态度用 curious、blank、hostile 等补出来。',
 ('He stares at the ceiling when he cannot sleep.','睡不着时，他就盯着天花板。'),('Her unusual hat drew curious stares.','她那顶特别的帽子引来好奇的注视。'),sources=S('stares','stare'))
W('stared','英 /steəd/；美 /sterd/','盯着看了；定定地注视了',
 '刚才看到一件出乎意料的事，人一下不说话，目光停在那里，就可以说 stared。',
 'stare 去 e 加完整 -ed，词尾读 /d/；不是基础末尾有字母 e 就把词尾读成 /ɪd/。',STARE+[['stare → stared','过去睁眼定定地看']],
 'stared at the screen 盯着屏幕；stared in disbelief 难以置信地盯着看；stared into the distance 定定看远处。',
 'stared back 回看、对视；stared without speaking。',
 'stared back 可以是同样盯回去，不等于已经用目光压倒对方；stared someone down 才把对方先移开眼的意味带出来。',
 ('We stared at the screen in disbelief.','我们难以置信地盯着屏幕。'),('She stared back at him without saying a word.','她一言不发地回视着他。'),sources=S('stared','stare'))
W('staring','英 /ˈsteərɪŋ/；美 /ˈsterɪŋ/','正在盯着看；定定注视的',
 '镜头里的人目光还没移开，眼睛一直停在那儿，叫 staring。它能写发呆，也能写惊讶或盯得别人不自在。',
 'stare 去 e 加 -ing；英式在后接元音时发 /r/，所以与单独 stare 的读音衔接要注意。',STARE+[['stare → staring','固定注视正在进行；也修饰眼睛、目光等']],
 'staring at the screen 盯着屏幕；staring into space 发呆；wide, staring eyes 睁大而直盯的眼睛。',
 'caught someone staring 发现某人在盯着看；stop staring。',
 'staring into space 常是放空，不一定在观察某个目标；watching a match 才是持续看比赛进展。',
 ('He was staring into space when I entered.','我进去时，他正望着空处发呆。'),('She noticed that everyone was staring at her.','她注意到，所有人都在盯着她看。'),sources=S('staring','stare'))
GAZE=[['中古英语 gasen、gazen → gaze','可能借自北欧凝看、张口观看材料，具体远源未定'],['持续、专心地看 → 名词一段注视、目光','现代常写沉浸、出神、欣赏，也可由形容词补出冷漠等态度']]
W('gaze','/ɡeɪz/','凝视；注视；目光',
 '景色把注意力吸住，人一时不想把目光移开，这种看得入神的样子常用 gaze。名词则把那道目光、一段注视拿出来说。',
 '承中古英语 gasen、gazen，可能接北欧相关材料；名词由动词发展，现代整体保留，不强拆音节。',GAZE,
 'gaze at the stars 凝望星空；gaze out of the window 出神看窗外；meet someone’s gaze 迎上某人的目光。',
 'a steady gaze 稳定的注视；lower your gaze 垂下目光。',
 'gaze 常比 stare 更容易带入神、专注感，但不是固定等于温柔；a cold gaze 也可以很冷。',
 ('We sat quietly and let ourselves gaze at the stars.','我们安静坐着，任自己凝望星空。'),('She met his gaze without speaking.','她没有说话，迎上了他的目光。'),sources=S('gaze','gaze'))
W('gazes','/ˈɡeɪzɪz/','凝视、出神地看〔第三人称单数〕；目光、注视〔复数〕',
 '他每晚都往远处看得出神，动词用 gazes；几个人的目光汇到一处，名词也可以用 gazes。',
 'gaze + -s，基础 /z/ 后词尾读 /ɪz/；名词复数、动词三单同形。',GAZE+[['gaze + -s → gazes','他、她专注凝望；多道、几次目光']],
 'gazes out to sea 出神望海；gazes at the painting 凝视画作；their gazes met 他们目光相遇。',
 'gazes into the distance；steady gazes。',
 'gazes 描写目光停留的状态；glances 是短短一眼，两者的持续感不同。',
 ('She gazes out to sea from the balcony.','她在阳台上出神地望着大海。'),('Their gazes met across the crowded room.','隔着拥挤的房间，他们的目光相遇了。'),sources=S('gazes','gaze'))
W('gazed','/ɡeɪzd/','凝视、凝望了；出神地看了',
 '刚才被某个画面吸住，安静地看了一阵，叫 gazed。也可说认真望着某人，态度由上下文说明。',
 'gaze 去 e 加完整 -ed，/z/ 后词尾读 /d/；不是像三单 gazes 那样多出 /ɪz/。',GAZE+[['gaze → gazed','过去持续、专注地看']],
 'gazed at the horizon 凝望地平线；gazed into her eyes 凝视她的眼睛；gazed out of the window 出神望窗外。',
 'gazed in wonder 惊叹地望着；gazed silently。',
 'gazed 不要求目光始终带喜欢；gazed coldly 就是冷冷地注视，别把常见气氛当唯一词义。',
 ('We gazed at the mountains as the light faded.','天色渐暗时，我们凝望着群山。'),('She gazed out of the window for a long time.','她出神地望着窗外，看了很久。'),sources=S('gazed','gaze'))
W('gazing','/ˈɡeɪzɪŋ/','正在凝视、凝望；出神地看',
 '人还被眼前的景色、面孔吸住，目光慢慢停在那里，这段持续的注视叫 gazing。',
 'gaze 去 e 加 -ing，基础 /z/ 保留；可作进行形式，也可把凝望当作一项活动。',GAZE+[['gaze → gazing','持续凝望的过程；也作活动表达']],
 'gazing at the sky 凝望天空；gazing into the distance 出神望远处；spend time gazing 花时间凝望。',
 'gazing out over the fields；gazing at one another。',
 'gazing at 指向凝视对象，gazing out of 从某个出口往外看；at the stars、out of the window 分别说目标与视线通路。',
 ('She was gazing at the sky when the first star appeared.','第一颗星出现时，她正凝望天空。'),('We spent the evening gazing out over the fields.','傍晚，我们一直出神地望着外面的田野。'),sources=S('gazing','gaze'))
GAPE=[['较早日耳曼、北欧张口材料 → 中古英语 gapen → gape','可能借古诺尔斯语 gapa，也有本族旧词延续的分析'],['嘴张开 → 张嘴惊看；洞、开口也大大敞开','与 gap 缺口同族；现代不是只有看人的动作']]
W('gapes','/ɡeɪps/','张嘴惊看；大大敞开〔第三人称单数〕；张口、敞口〔复数〕',
 '人惊讶得嘴巴张着，眼睛定在那里，是 gapes；衣服、袋口有一处大大敞开，也能用同一个动作词。',
 'gape + -s，/p/ 后词尾读 /s/；名词复数也可同形，日常更常见动词的张开用法。',GAPE+[['gape + -s → gapes','它、他、她大张着嘴或敞开']],
 'gapes at the display 张嘴惊看展品；a hole gapes open 洞口大大敞着。',
 'gapes in amazement；the bag gapes open。',
 'gapes 比 stares 更把嘴张开的姿态写出来；gap 名词则指那个空隙、缺口。',
 ('The child gapes at the enormous model dinosaur.','孩子张着嘴，惊看那只巨大的恐龙模型。'),('The old bag gapes open where the seam has split.','旧包接缝裂开的地方大大敞着口。'),sources=S('gapes','gape'))
W('gaped','/ɡeɪpt/','张嘴惊看了；大大敞开了',
 '门里出现出乎意料的东西，人一下张着嘴看呆了，叫 gaped；开口裂得很大，也能写它当时 gaped open。',
 'gape 去 e 加完整 -ed，/p/ 后词尾读 /t/，结尾 /pt/；保留 /eɪ/。',GAPE+[['gape → gaped','过去张口惊看，或处于大大敞开的状态']],
 'gaped at the sight 张嘴惊看眼前景象；gaped in surprise 惊讶得张着嘴；gaped open 大大敞开。',
 'gaped at us；the empty doorway gaped open。',
 'gaped at 常是惊讶、惊看，gazed at 更常是专注、入神地看；嘴巴张开的画面让 gape 更鲜明。',
 ('We gaped at the size of the cake.','蛋糕大得让我们张着嘴看呆了。'),('The empty doorway gaped open in the dark.','黑暗里，空荡荡的门洞大大敞着。'),sources=S('gaped','gape'))
def extend_lessons():
 extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_zga',ROOTS,WORDS)
 extend_lessons()
