"""Keeping a purpose, or moving from place to place."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
def S(word,base):
 return ['https://en.wiktionary.org/wiki/'+word+'#English','https://www.etymonline.com/word/'+base]
EXISTING_ROOT_ADDITIONS={
 'C1328':dict(words='persevere perseveres persevered persevering perseverance'.split(),label='persevere：困难中继续做',note='拉丁 per- 加强程度与 severus 认真、严肃材料相接，再经 perseverare、法语等传入；不是 per 加英语 severe 就能把每句译成非常严厉。'),
 'B3195':dict(words='steadfast steadfastly steadfastness'.split(),label='steadfastly：稳稳守住立场',note='stead 地方、位置与 fast 牢固组成 steadfast；此处 fast 不是速度快，加 -ly 表坚定不移的方式。'),
 'C1364':dict(words='resolute resoluteness'.split(),label='resoluteness：已下定决心的坚定',note='resolute 接拉丁 resolutus，早有松开、分解义；通过分析、定下结论的意义发展到坚定，再加 -ness 表性质。不能把现代坚定义倒说成从未有松解背景。'),
 'B2969':dict(words='unshakable unshakeable unshakably'.split(),label='unshakable：摇不动，到信念不动摇',note='否定 un-、shake 与 -able 组成；unshakeable 保留 e，是同词的拼写变体。副词 unshakably 用 -able 到 -ably 的形式变化。'),
 'B3515':dict(words='traipse traipses traipsed traipsing rove roves roved roving'.split(),label='traipse、rove：四处走，去来没有固定点',note='与 walk 作近义比较，不是现代 walk 的派生。traipse 来源未定，有法语跨越或日耳曼踏行材料等分析；rove 也有北欧或法语漫游材料等分析，并可能受 rover 影响。'),
 'A1697':dict(words='ramble rambler ramblers stroll stroller strollers'.split(),label='rambler、stroller：漫步的人与供人推行的车',note='ramble 去 e 加完整 -er，stroll 直接加完整 -er，前者常指郊野漫步者、漫谈者，也可说蔓生植物；后者常见人称义与较晚的婴儿推车义。不能把词尾只写成 -r。'),
}
PERSEVERE=[['拉丁 per- 加强程度 + severus 认真、严肃 → perseverare','坚定地继续、坚持'],['经法语及拉丁材料进入英语 persevere','面对困难仍把已开始的事做下去']]
UNSHAKABLE=[['shake 摇晃，也早可指使信心、稳定动摇','物理摇动与抽象失稳的对应有历史依据'],['un- 否定 + shake + -able → unshakable / unshakeable','不能动摇；两个拼写变体意思相同']]
TRAIPSE=[['较早 traipse 有拖着、散漫、无目的地走等材料','来源未定，有法语跨越或日耳曼踏行等分析'],['现代拖着步子走，或一处处跑来跑去','常带路程麻烦、走得多的抱怨，也可写闲逛']]
ROVE=[['rove 的漫游来历有不同分析','可能接北方 rave、北欧 rafa，或法语漫游材料，并受 rover 影响'],['四处游走 → 目光游移、流动任职','不硬定为现代 rover 删 r 或某一来源的单线']]
W('perseveres','英 /ˌpɜːsɪˈvɪəz/；美 /ˌpɝsəˈvɪrz/','坚持做下去、不轻易放弃〔第三人称单数〕',
 '第一次不成，调整一下再试；过程慢，仍持续做，是 perseveres。重点是困难出现以后仍不松手。',
 'persevere + -s，读 /z/；基础词经法语、拉丁材料进入，内部 per- 加强坚定、认真的程度。',PERSEVERE+[['persevere + -s → perseveres','他或她面对困难仍坚持']],
 'perseveres despite setbacks；perseveres with the work。',
 'perseveres in her studies；perseveres until it works。',
 'continues 只是继续，perseveres 更强调有困难仍坚持；顺顺利利做完不必每次都强调毅力。',
 ('She perseveres even when progress is slow.','即使进展慢，她也坚持做下去。'),('He perseveres with difficult problems until he understands them.','面对难题，他会一直钻研到弄懂。'),sources=S('perseveres','persevere'))
W('persevered','英 /ˌpɜːsɪˈvɪəd/；美 /ˌpɝsəˈvɪrd/','坚持做下去了；没有轻易放弃',
 '当时很难，还是撑着继续练、继续改，过去这段坚持叫 persevered。它描述投入，不保证最终结果一定成功。',
 'persevere 去 e 加完整 -ed，读 /d/；不增加 /ɪd/ 音节，英美 r 的读法随口音不同。',PERSEVERE+[['persevere + -ed → persevered','过去面对困难仍继续']],
 'persevered despite failure；persevered with the training。',
 'persevered for years；had persevered through setbacks。',
 'persevered 是坚持过程，succeeded 是成功结果；坚持可能通向成功，但两个词不能直接互译。',
 ('They persevered despite several disappointing results.','几次结果令人失望，他们仍坚持了下来。'),('She persevered with the training until the movements felt natural.','她坚持练习，直到那些动作变得自然。'),sources=S('persevered','persevere'))
W('persevering','英 /ˌpɜːsɪˈvɪərɪŋ/；美 /ˌpɝsəˈvɪrɪŋ/','正在坚持；有毅力、不轻易放弃的',
 '进展不快，却不断回来接着做，是 persevering。也可形容人有耐心、有毅力，遇到困难不会立刻撒手。',
 'persevere 去 e 加 -ing；英式在元音开头后缀前读出 r。过程分词也能作形容词。',PERSEVERE+[['persevere + -ing → persevering','坚持的过程，或有毅力的性质']],
 'keep persevering 继续坚持；a persevering student 有毅力的学生。',
 'persevering with the task；patient and persevering。',
 'persevering 常肯定坚持，stubborn 可以批评不愿调整；持续做事仍可以边做边改办法。',
 ('Keep persevering; the first stage is often the hardest.','继续坚持，第一阶段往往最难。'),('Her patient, persevering work finally paid off.','她耐心而坚持不懈的付出终于有了回报。'),sources=S('persevering','persevere'))
W('steadfastly','英 /ˈstedfɑːstli/；美 /ˈstedfæstli/','坚定不移、始终如一地',
 '别人施压，立场却没有改；支持一件事也始终稳稳的，是 steadfastly。像脚下站牢，不因一点风就偏过去。',
 'steadfast + -ly；内部 stead 地方、位置 + fast 牢固。这里的 fast 用旧牢固义，不是越快越坚定。',
 [['古英语 stede 位置 + fæst 牢固 → steadfast','固定在原位，后来也说信念、忠诚坚定'],['steadfast + -ly → steadfastly','以不动摇、始终如一的方式']],
 'steadfastly refuse 始终坚决拒绝；steadfastly support。',
 'remain steadfastly loyal；steadfastly pursue a goal。',
 'steadfastly 说坚定稳定，quickly 说速度快；词中的 fast 不在这里表示赶速度。',
 ('She steadfastly refused to change her account.','她始终坚决不肯改变自己的叙述。'),('He remained steadfastly loyal to his old friends.','他一直坚定地忠于老朋友。'),sources=S('steadfastly','steadfast'))
W('resoluteness','英 /ˈrezəluːtnəs/；美 /ˈrezəlutnəs/','坚定、果断这种性质',
 '心里已经定下来，面对压力也不再摇摆，这种坚定叫 resoluteness。像一个问题已经想清，决定不再来回松动。',
 'resolute + -ness，保留末尾 e。resolute 接拉丁 resolutus，早有松解、分解义，后经分析、决定等意义发展为坚定。',
 [['拉丁 resolvere 松解、分解 → resolutus → 英语 resolute','较早有松散义，后来有已决定、坚定义'],['resolute + -ness → resoluteness','把坚定、果断这种性质作为名词谈']],
 'show resoluteness 表现出坚定；admire her resoluteness。',
 'resoluteness under pressure；calm resoluteness。',
 'resolution 还能指决议、分辨率、解决等多义，resoluteness 更集中说坚定的性质；不能把所有 resolution 都替成它。',
 ('Her calm resoluteness reassured the team.','她沉着坚定的态度让团队安心。'),('He showed unexpected resoluteness under pressure.','压力之下，他表现出了出人意料的坚定。'),sources=S('resoluteness','resolute'))
W('unshakable','/ʌnˈʃeɪkəbəl/','不可动摇的；稳固、坚定的',
 '信心像扎稳的柱子，坏消息也没把它摇松，是 unshakable。常形容信念、信任、决心，强调很难动摇。',
 'un- 否定 + shake 去 e 加完整 -able；表示不能被动摇。另有保留 e 的拼写 unshakeable。',UNSHAKABLE,
 'unshakable confidence 坚定的信心；unshakable belief。',
 'unshakable trust；an unshakable conviction。',
 'unshakable 说信念稳，true 说内容为真；信得很坚定并不自动证明事实正确。',
 ('She had unshakable confidence in the team.','她对团队有不可动摇的信心。'),('The experience gave him an unshakable belief in the value of education.','那段经历让他坚信教育的价值。'),sources=S('unshakable','unshakable'))
W('unshakeable','/ʌnˈʃeɪkəbəl/','不可动摇的、坚定的〔unshakable 的拼写变体〕',
 '和 unshakable 意思、读法相同：信心、信念、决心牢牢立住。看到多一个 e，不必再编出一层新的含义。',
 'un- + shake + -able，这种拼写保留 shake 的 e；与省 e 的 unshakable 对应。',UNSHAKABLE+[['unshakable ↔ unshakeable','省 e 与保留 e 的拼写变体，不是两个强度等级']],
 'unshakeable faith 坚定的信念；unshakeable trust。',
 'unshakeable confidence；an unshakeable sense of purpose。',
 'unshakeable 不比 unshakable 更强；选择一种惯用拼写并保持一致，理解上按同一个词学习。',
 ('Her faith in their friendship was unshakeable.','她对这段友谊的信任坚定不移。'),('He spoke with unshakeable confidence.','他说话时充满坚定的信心。'),sources=S('unshakeable','unshakable'))
W('unshakably','/ʌnˈʃeɪkəbli/','坚定不移地；毫不动摇地',
 '一直相信、一直支持，外面的变化没让立场松动，是 unshakably。它把不可动摇变成相信、确信等动作的方式。',
 'unshakable 的 -able 变成 -ably；可理解为末尾 le 换成 ly，不写成 unshakablely。',UNSHAKABLE+[['unshakable → unshakably','形容词 -able 对应方式副词 -ably']],
 'unshakably convinced 坚信不疑；unshakably loyal。',
 'believe unshakably；unshakably certain。',
 'unshakably convinced 说人确信的程度，conclusively proved 才说证明充分；信心和证据要分清。',
 ('She remained unshakably convinced that the plan could work.','她始终坚信计划能行得通。'),('He was unshakably loyal to the friends who had helped him.','他对帮助过他的朋友始终忠诚，毫不动摇。'),sources=S('unshakably','unshakable'))
W('traipse','/treɪps/','拖着步子走；费劲地四处跑、闲逛〔口语〕',
 '为买一样东西跑了好几家店，走得人不耐烦，可以说 traipse around。常带折腾、没必要走这么多的抱怨，也可轻松说到处逛。',
 '较早有散漫、拖着走、无目的走等意思，来源未定；有法语跨越或日耳曼踏行等分析，不能把某一猜测写成唯一链。',TRAIPSE,
 'traipse around the shops 跑遍商店；traipse across town。',
 'traipse through the mud；traipse after someone 跟着某人跑来跑去。',
 'stroll 常是悠闲散步，traipse 常嫌走得多、麻烦；同样逛商店，语气可以很不同。',
 ('I do not want to traipse around the shops all afternoon.','我可不想一下午都在各家店里跑来跑去。'),('We had to traipse across town to collect the parcel.','为了取那个包裹，我们得折腾着穿过大半座城。'),sources=S('traipse','traipse'))
W('traipses','/ˈtreɪpsɪz/','费劲地走来走去、闲逛〔第三人称单数〕',
 '她每周为找材料跑好几处，可以说 traipses around。句子往往让人感觉走得不少，甚至有点折腾。',
 'traipse + -s，拼写只添 -s；基础末音 /s/ 后读 /ɪz/ → /ˈtreɪpsɪz/。',TRAIPSE+[['traipse + -s → traipses','他或她走来走去、跑很多地方']],
 'traipses around markets；traipses across town。',
 'traipses after her friends；traipses from shop to shop。',
 'traipses 常带对奔走的主观感受，travels 只说移动、旅行；不能把每次出行都译成折腾。',
 ('She traipses around the markets looking for old records.','她为找老唱片，在各个市场里跑来跑去。'),('He traipses across town whenever he needs a particular ingredient.','每次缺某种配料，他都要跑过大半座城去买。'),sources=S('traipses','traipse'))
W('traipsed','/treɪpst/','拖着步子走了；跑来跑去、折腾着走过了',
 '昨天为了办几件小事跑了很多路，回头可以说 traipsed around all day。重点是那段奔走让人感到累、麻烦。',
 'traipse 去 e 加完整 -ed；/s/ 后读 /t/ → /treɪpst/，不添 /ɪd/ 音节。',TRAIPSE+[['traipse + -ed → traipsed','过去走了不少路、跑了很多地方']],
 'traipsed around town；traipsed through the mud。',
 'traipsed from office to office；traipsed back home。',
 'traipsed 不保证有明确计划，marched 更像有方向、有节奏地行进；跑来跑去和列队前进不是同一画面。',
 ('We traipsed from one office to another all morning.','我们一上午都在各个办公室之间跑来跑去。'),('They traipsed through the mud to reach the gate.','他们踩着泥，费劲地走到了大门口。'),sources=S('traipsed','traipse'))
W('traipsing','/ˈtreɪpsɪŋ/','正在走来走去、四处奔走、闲逛',
 '为了找一件东西，已经走了好几家，接着还在跑，是 traipsing。说话人常嫌这种奔走太折腾，也可能是轻松自嘲。',
 'traipse 去 e 加 -ing；/s/ 保留为 /s/，不是三单里的 /ɪz/。',TRAIPSE+[['traipse + -ing → traipsing','四处走、费劲奔走的过程']],
 'traipsing around the shops；traipsing across town。',
 'tired of traipsing；traipsing through the countryside。',
 'traipsing around 常写到处跑，commuting 常说固定往返通勤；都可能累，但路线、目的不同。',
 ('I spent the afternoon traipsing around looking for the right cable.','我一下午都在跑来跑去，找那根合适的连接线。'),('She was tired of traipsing from one appointment to another.','她厌倦了一个约见接一个约见地奔波。'),sources=S('traipsing','traipse'))
W('rove','英 /rəʊv/；美 /roʊv/','漫游、四处走动；目光游移',
 '今天在这儿，明天去那儿，没有固定停点，可以说 rove。眼睛在房间里这边看看、那边看看，也像在漫游。',
 '近源有不同分析：可能接北方 rave、古诺尔斯 rafa 漫游，或法语漫游材料，并可能受 rover 影响。不能把现代 rover 删一个 r 当成确定历史。',ROVE,
 'rove across the country 四处游历；eyes rove around the room。',
 'rove from place to place；let your eyes rove。',
 'rove 常强调走来走去、不固定，head for 强调朝某个目的地去；两种说法组织行程的角度不同。',
 ('The animals are free to rove across a wide area.','这些动物可以在大片区域内自由游走。'),('He let his eyes rove around the room.','他让目光在房间里四下游移。'),sources=S('rove','rove'))
W('roves','英 /rəʊvz/；美 /roʊvz/','漫游、四处走动；目光游移〔第三人称单数〕',
 '一只猫在附近东走西逛，是 roves；他的目光不断扫向房间各处，也能说 his gaze roves。不是只有人能做主语。',
 'rove + -s，/v/ 后读 /z/；这里讲漫游动词这一支，来源仍有不同分析。',ROVE+[['rove + -s → roves','他或它四处走，或目光游移']],
 'roves around the neighbourhood；his gaze roves。',
 'roves across the landscape；roves from place to place。',
 'roves 是四处移动，stares 是盯着看；目光游走和视线固定不同。',
 ('The cat roves around the neighbourhood at night.','那只猫晚上会在附近四处游走。'),('Her gaze roves across the crowded room.','她的目光在拥挤的房间里四下游移。'),sources=S('roves','rove'))
W('roved','英 /rəʊvd/；美 /roʊvd/','四处游走、游历了；目光游移了',
 '曾经走过许多地方，没有一直留在一处，可以说 roved。用在目光上，则是过去四下看过。',
 'rove 去 e 加完整 -ed；/v/ 后读 /d/ → /rəʊvd/，不新增 /ɪd/。',ROVE+[['rove + -ed → roved','过去四处移动，或目光扫过各处']],
 'roved across the countryside；her eyes roved over the shelves。',
 'roved from town to town；roved around the garden。',
 'roved through 是在其中游走，arrived at 是到达某一点；经过许多地方不等于只交代终点。',
 ('We roved through the countryside with no fixed plan.','我们没定计划，在乡间四处游走。'),('Her eyes roved over the shelves in search of the book.','她的目光扫过一排排书架，寻找那本书。'),sources=S('roved','rove'))
W('roving','英 /ˈrəʊvɪŋ/；美 /ˈroʊvɪŋ/','四处游走的；流动工作的；目光游移的',
 '记者不固定在一个地方，哪里有新闻就去哪儿，是 a roving reporter。roving eye 则常形容目光东看西看，有时特指容易被别的异性吸引。',
 'rove 去 e 加 -ing；过程分词也作形容词，表示不固定在一处、流动的性质。',ROVE+[['rove + -ing → roving','四处移动的过程，或流动工作的性质']],
 'a roving reporter 流动采访的记者；a roving eye。',
 'roving around the city；a roving team。',
 'roving reporter 强调到各处采访，local reporter 强调报道某地；流动和报道范围不是完全相反的身份。',
 ('She works as a roving reporter for the magazine.','她为那本杂志做流动采访记者。'),('A roving team visited several villages each week.','一个流动小组每周会走访几个村庄。'),sources=S('roving','rove'))
W('rambler','英 /ˈræmblə/；美 /ˈræmblɚ/','郊野漫步者；说话漫无边际的人；蔓生植物',
 '喜欢沿乡间小路走走的人，是 rambler；说话东拉西扯的人也能这样叫。园艺里的 rambler 常说枝条能蔓延的植物，像枝条也在到处走。',
 'ramble 去 e 加完整 -er；基础动词可能接 roam 的反复动作材料，也有荷兰语影响等分析。不同现代意义围绕漫步、延伸展开。',
 [['ramble 漫步、漫谈；近源有不同分析','走路方向游移，到话题游移'],['ramble + -er → rambler','漫步者、漫谈者，或枝条蔓延的植物']],
 'a keen rambler 热爱郊野漫步的人；a rambling rose / a rambler 蔓生月季。',
 'an experienced rambler；a talkative rambler。',
 'rambler 作为人常偏郊野漫步，rover 更宽泛地游走；植物义也不能直接译成一个散步的人。',
 ('An experienced rambler showed us the path across the fields.','一位有经验的郊野漫步者给我们指了穿过田野的小路。'),('We planted a rambler to cover the old arch.','我们种了一株蔓生月季，让它爬满旧拱架。'),sources=S('rambler','ramble'))
W('ramblers','英 /ˈræmbləz/；美 /ˈræmblɚz/','郊野漫步者〔复数〕；漫谈者；蔓生植物',
 '小路上一群结伴走乡野的人，是 ramblers；花园里几株向四处伸展的蔓生月季，也可能叫 ramblers。',
 'rambler + -s，读 /z/；先由 ramble 去 e 加 -er 成名词，再说多人、多株等。',
 [['ramble 漫步、漫谈 → rambler','人可在路径、话题间游移，植物可蔓延'],['rambler + -s → ramblers','多个漫步者、漫谈者或蔓生植物']],
 'a group of ramblers；a path popular with ramblers。',
 'rose ramblers 蔓生月季；ramblers over an arch。',
 'ramblers 是人或植物等名词，rambles 可说几次漫步、漫谈；一次行程和参加的人不是同一单位。',
 ('The path is popular with local ramblers.','这条小路很受当地郊野漫步者欢迎。'),('Pink ramblers covered the garden arch.','粉色蔓生月季爬满了花园拱架。'),sources=S('ramblers','ramble'))
W('stroller','英 /ˈstrəʊlə/；美 /ˈstroʊlɚ/','散步的人；婴儿推车〔尤美式〕',
 'stroll 是慢慢散步，stroller 原可说散步者。现在美式日常说 a stroller，常指推着幼儿出门的轻便婴儿车。',
 'stroll + 完整 -er；原词已有双 l，不另添。早期还见巡回表演者、游荡者义；婴儿推车义较晚，不是所有 -er 名词都只指人。',
 [['stroll 游走、散步 → stroller','较早可指巡回艺人、游荡或散步的人'],['stroller 后来常指婴儿推车','让孩子坐着、由大人推着行进的车']],
 'push a stroller 推婴儿车；an evening stroller 傍晚散步者。',
 'a folding stroller 折叠婴儿车；a stroller on the path。',
 'stroller 尤美式常指推车，British English 常说 pushchair；不是步行学步车的同一个物件。',
 ('She folded the stroller before getting on the bus.','上公交车前，她把婴儿推车折起来。'),('A lone stroller paused to watch the sunset.','一位独自散步的人停下来，看了看落日。'),sources=S('stroller','stroll'))
W('strollers','英 /ˈstrəʊləz/；美 /ˈstroʊlɚz/','散步的人〔复数〕；婴儿推车〔复数，尤美式〕',
 '公园里一群闲散步行的人，可以是 strollers；门口停着的几辆婴儿推车，也叫 strollers。看动词是在走，还是被推、停放。',
 'stroller + -s，读 /z/；stroll 加 -er 后再取复数，不是 strolls 动词三单的扩展拼法。',
 [['stroll → stroller','散步动作，到人；后来有婴儿推车义'],['stroller + -s → strollers','多人散步，或多辆婴儿推车']],
 'parents with strollers 推着婴儿车的家长；evening strollers。',
 'folding strollers；strollers along the promenade。',
 'strollers 可能是车也可能是人，walkers 也多义；阅读时靠具体动作、场景定指代。',
 ('Parents left their strollers near the entrance.','家长们把婴儿推车放在入口附近。'),('Evening strollers filled the riverside path.','傍晚散步的人走满了河边小路。'),sources=S('strollers','stroll'))
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_zhr',ROOTS,WORDS)
 extend_lessons()
