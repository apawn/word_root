"""Jog, pelt, canter, prance, trotters and mosey."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
def S(word,base):
 return ['https://en.wiktionary.org/wiki/'+word+'#English','https://www.etymonline.com/word/'+base]
EXISTING_ROOT_ADDITIONS={
 'A1741':dict(words='jog jogs jogged jogging jogger joggers'.split(),label='jog：轻轻一碰，到慢跑与运动裤',note='jog 较早有上下颠动、轻推等义，或接中古 shoggen 的变体，远源未定。健身慢跑义较晚流行；jogger 的现代慢跑者、joggers 运动裤也不能倒置成全部历史起点。'),
 'B2738':dict(words='pelt pelts pelted pelting'.split(),label='pelt：接连砸打，到急奔',note='与 beat 作反复击打的近义比较，不是现代 beat 的派生。pelt 动词远源有不同分析；毛皮名词另接法语皮肤材料、拉丁 pellis 等分析，不能把毛皮说成由砸打而来。'),
 'B4597':dict(words='canter canters cantered cantering prance prances pranced prancing'.split(),label='canter 与 prance：轻快跑步、昂首高抬步',note='与 horse 作马步场景比较，不是 horse 的后代。canter 的马步义缩自 Canterbury pace 等；prance 远源未定，马昂首高步与人的炫耀走姿都很早。'),
 'B3003':dict(words='trot trotter trotters'.split(),label='trotter：善快步跑的马；作为食材的蹄脚',note='trot 双写 t 加完整 -er；马、信使、作食材的四足兽脚等义都很早，不必编成某一现代义必先于另一义。'),
 'B3515':dict(words='mosey moseys moseyed moseying'.split(),label='mosey：慢悠悠走一趟',note='与 walk 作轻松口语比较，不是现代 walk 的派生。mosey 来源未定，有英国方言 mose about 或西班牙语 vamos 缩变等分析，不写成确定的西语借词。'),
}
JOG=[['jog 较早指颠动、轻推，可能接中古英语 shoggen 变体','远源未定，不把健身跑当作所有义的起点'],['轻推 → 提醒；有节奏移动 → 现代健身慢跑','jogger 后来常指慢跑者，joggers 也指运动裤']]
PELT=[['pelt 动词：反复击打，来源未定','有旧击打词、法语球击材料等分析，不认定唯一来源'],['接连砸打 → 脚步急促地打在地面、急奔','毛皮名词另接法语皮、拉丁 pellis 等材料分析']]
CANTER=[['Canterbury pace 等短语 → 缩略 canter','与前往坎特伯雷朝圣时从容的骑行步调相联'],['英语马的轻快跑步 → 动词、相应步态名词','此处整个基础词不是 cant 加人称 -er']]
PRANCE=[['较早 prance 写马精神足、昂首高抬步','来源未定，有日耳曼炫耀材料、其他语源等分析'],['马高步，到人得意、炫耀地走或蹦跳','马与人的相关义都很早，不强排简单单线先后']]
MOSEY=[['mosey 早期美式口语说离开、走开','来源未定，方言或西班牙语缩变等分析并存'],['现代常说慢悠悠、轻松地走去','旧记录不等于现代每次都要赶人快走']]
W('jogs','英 /dʒɒɡz/；美 /dʒɑɡz/','慢跑；轻碰；唤起记忆〔第三人称单数〕；几次慢跑',
 '每天轻松跑一段，是 jogs；一句提示让你想起某事，也是 jogs your memory，像把沉着的记忆轻轻碰醒。',
 'jog + -s，/ɡ/ 后读 /z/；动词三单和名词复数同形，慢跑义不是词的最早起点。',JOG+[['jog + -s → jogs','他或她慢跑、轻推；或多次慢跑']],
 'jogs every morning；jogs my memory；short jogs around the park。',
 'jogs someone’s elbow 轻碰某人手肘；jogs along the river。',
 'jogs my memory 是促使想起，loses my memory 才是失去记忆；这里借轻推的旧画面，不是记忆在跑步。',
 ('She jogs along the river every morning.','她每天早晨沿河慢跑。'),('That photograph jogs my memory of the old house.','那张照片唤起了我对老房子的记忆。'),sources=S('jogs','jog'))
W('jogged','英 /dʒɒɡd/；美 /dʒɑɡd/','慢跑了；轻碰、唤起记忆了',
 '昨天慢慢跑了一段，是 jogged；看到老照片，一下想起某人，也是 it jogged my memory。不要只背运动那一义。',
 'jog 双写 g 加完整 -ed，读 /d/；不增加 /ɪd/ 音节。',JOG+[['jog + -ed → jogged','双写 g，过去慢跑、轻推或提醒']],
 'jogged around the park；jogged my memory；jogged his elbow。',
 'jogged home；had jogged for twenty minutes。',
 'jogged 作为运动通常是轻松、持续的跑，sprinted 是冲刺；不是所有跑得动都属于同一速度。',
 ('We jogged around the park before breakfast.','早餐前，我们绕公园慢跑了一圈。'),('Her note jogged my memory about the meeting.','她的便条让我想起了那场会议。'),sources=S('jogged','jog'))
W('jogger','英 /ˈdʒɒɡə/；美 /ˈdʒɑɡɚ/','慢跑者',
 '穿着运动服，在河边轻松跑一段的人，是 a jogger。重点是以轻松、持续的跑步锻炼的人，不一定参加比赛。',
 'jog 双写 g，加完整 -er；早期做人称名词已有缓慢重步者、轻推者义，现代慢跑者用法后来流行。',JOG+[['jog + -er → jogger','双写 g，做这种动作的人']],
 'a morning jogger 晨跑者；a regular jogger 经常慢跑的人。',
 'an occasional jogger；a jogger on the riverside path。',
 'jogger 常说慢跑锻炼者，sprinter 是冲刺短跑者；跑步者的活动侧重点不同。',
 ('A jogger passed us on the riverside path.','一位慢跑者从河边小路上经过。'),('I am only an occasional jogger.','我只是偶尔慢跑的人。'),sources=S('jogger','jogger'))
W('joggers','英 /ˈdʒɒɡəz/；美 /ˈdʒɑɡɚz/','慢跑者〔复数〕；运动长裤〔常作复数〕',
 '公园里几个慢跑的人是 joggers；服装店里 a pair of joggers 则是一条运动长裤。前者是人，后者是适合休闲、运动的裤装名称。',
 'jogger + -s，读 /z/；既可按普通复数说多人，也有常用复数的服装义。',JOG+[['jogger + -s → joggers','多个慢跑者；服装义通常用复数形式']],
 'morning joggers；a pair of joggers；cotton joggers 棉质运动裤。',
 'joggers on the path；wear joggers。',
 'three joggers 常是三个人，three pairs of joggers 才常是三条裤子；计数单位帮你认出指代。',
 ('The path was busy with morning joggers.','早晨，那条小路上有不少慢跑的人。'),('He wore cotton joggers and a loose T-shirt.','他穿着棉质运动长裤和宽松的T恤。'),sources=S('joggers','jogger'))
W('pelt','/pelt/','接连投掷、砸打；急奔；毛皮',
 '雨点密密砸在窗上，是 pelt the window；人脚步急促地冲过去，也能 pelt。店里的 animal pelt 是毛皮，另有自己的来源。',
 '击打动词来源未定，有旧击打词或法语球击材料等分析。急奔义接快速脚步打地的画面；毛皮名词则另接法语皮肤、拉丁 pellis 等分析。',PELT,
 'pelt someone with questions 用一连串问题轰炸某人；at full pelt 全速。',
 'rain pelts the window；an animal pelt 动物毛皮。',
 'pelt 常有连续、密集的力道，hit 只说击中、打；毛皮 pelt 不能从投掷动作硬推来。',
 ('Rain began to pelt the windows.','雨开始密密地砸在窗上。'),('He ran down the lane at full pelt.','他沿小巷全速跑去。'),('The museum displayed a fox pelt.','博物馆展出了一张狐皮。'),sources=S('pelt','pelt'))
W('pelts','/pelts/','接连砸打、急奔〔第三人称单数〕；毛皮〔复数〕',
 '冰雹一颗接一颗打下来，是 pelts；展柜里的几张毛皮，也叫 pelts。相同形式在两条不同历史中使用。',
 'pelt + -s，/t/ 后读 /s/；击打动词三单、毛皮名词复数同形，不能混成一个来历。',PELT+[['pelt + -s → pelts','它连续砸打，或多张毛皮']],
 'hail pelts the roof；animal pelts；pelts down the road。',
 'rain pelts the ground；fur pelts。',
 'pelts the roof 是接连砸在屋顶上，covers the roof 只是覆盖；动作力度、频度不同。',
 ('Hail pelts the roof during the storm.','暴风雨中，冰雹密密砸在屋顶上。'),('The display includes several preserved animal pelts.','展品中有几张保存下来的动物毛皮。'),sources=S('pelts','pelt'))
W('pelted','/ˈpeltɪd/','接连投掷、砸打了；急奔了',
 '雨点一路打在人身上，或一阵急跑冲过街口，可以说 pelted。都是动作密、力道急，具体对象由句子来定。',
 'pelt + 完整 -ed，/t/ 后读 /ɪd/；不重复 t。',PELT+[['pelt + -ed → pelted','过去连续砸打，或急促跑过']],
 'rain pelted us；pelted down the road；pelted with questions。',
 'pelted across the yard；hail pelted the windows。',
 'pelted with questions 是比喻问题接连而来，不是在说问题真的像石头；看 with 后面的对象认搭配。',
 ('Rain pelted us as we crossed the field.','我们穿过田野时，雨点密密砸在身上。'),('She pelted down the road to catch the bus.','她沿路急奔，想赶上公交车。'),sources=S('pelted','pelt'))
W('pelting','/ˈpeltɪŋ/','正在接连砸打、倾泻；正在急奔',
 '雨大得像一把把洒下来，是 pelting down；孩子脚步急急跑回来，也是 came pelting back。它把密、急的动作推到眼前。',
 'pelt + -ing；击打和急奔共用这一过程形式。毛皮名词的普通复数则是 pelts。',PELT+[['pelt + -ing → pelting','连续砸打、急奔的过程']],
 'pelting rain 瓢泼大雨；rain is pelting down；came pelting back。',
 'pelting the roof；pelting along the path。',
 'pelting rain 比 light rain 强得多，drizzle 是毛毛雨；同是下雨，力度画面不同。',
 ('It was pelting down when we left the café.','我们离开咖啡馆时，外面正下着瓢泼大雨。'),('The children came pelting back across the field.','孩子们急急地跑过田野回来了。'),sources=S('pelting','pelt'))
W('canter','英 /ˈkæntə/；美 /ˈkæntɚ/','马轻快跑；马的慢跑步态',
 '马已经比快步 trot 更快，却没放到最快奔驰 gallop，是 canter。学习先看轻快、从容的跑，不必把它当成人的普通慢跑。',
 '马步义缩自 Canterbury pace、相关较长动词，与前往坎特伯雷的朝圣骑行步调相联。这里不是 cant 加做人称的 -er。',CANTER,
 'at a canter 轻快跑着；canter across a field；break into a canter。',
 'a gentle canter；canter along the beach。',
 '马的 trot、canter、gallop 是不同步态；日常先按小跑、轻快跑、放开奔驰区分，不把它们全译成同一跑法。',
 ('The horse moved into a canter.','马开始轻快地跑起来。'),('We watched the horses canter across the field.','我们看着马匹轻快地跑过田野。'),sources=S('canter','canter'))
W('canters','英 /ˈkæntəz/；美 /ˈkæntɚz/','马轻快跑〔第三人称单数〕；几段轻快跑',
 '马沿围栏从容跑着，是 canters；几次短程练习这种步态，也可叫 canters。主语、量词帮你认出词性。',
 'canter + -s，读 /z/；动词三单与步态名词复数同形，基础马步义缩自 Canterbury pace 等材料。',CANTER+[['canter + -s → canters','马轻快跑，或几次这种跑步']],
 'canters around the arena；short canters；canters along the track。',
 'gentle canters；canters towards the gate。',
 'canters 是马正在用这种步态跑，walks 可以只是走；有规律地前进不保证速度、步态一样。',
 ('The horse canters smoothly around the arena.','马绕着训练场轻快、平稳地跑着。'),('The lesson included several short canters.','那节课包括几段短距离的轻快跑练习。'),sources=S('canters','canter'))
W('cantered','英 /ˈkæntəd/；美 /ˈkæntɚd/','马轻快跑了；骑马以慢跑步态前进了',
 '沿海滩骑着马轻快跑了一段，可以说 cantered。人作主语时，也可是在说骑马采用这种步态前进。',
 'canter + 完整 -ed，读 /d/；不增加 /ɪd/ 音节，英美词尾 r 随口音不同。',CANTER+[['canter + -ed → cantered','过去马轻快跑，或骑马这样前进']],
 'cantered along the beach；cantered across the field；cantered away。',
 'cantered towards the gate；had cantered for a while。',
 'we cantered 常是我们骑马轻快跑，we jogged 通常是我们自己慢跑；主语同是人，场景、交通方式仍不同。',
 ('We cantered along the beach at sunrise.','日出时，我们骑着马沿海滩轻快跑了一段。'),('The horse cantered towards the open gate.','马轻快地跑向敞开的大门。'),sources=S('cantered','canter'))
W('cantering','英 /ˈkæntərɪŋ/；美 /ˈkæntərɪŋ/','马正在轻快跑；以马的慢跑步态前进',
 '马轻快地带着骑手向前，速度和节奏比快步 trot 更放开，是 cantering。它描述具体步态，不只是笼统说移动。',
 'canter + -ing；英式在元音后缀前读出 r，形成动作过程。',CANTER+[['canter + -ing → cantering','马用轻快跑步态前进的过程']],
 'cantering across the field；a cantering horse；cantering along the path。',
 'riders cantering on the beach；practise cantering。',
 'cantering 不等于 galloping 全速奔驰；都比走快，但马的动作节奏不同。',
 ('A rider was cantering across the field.','一位骑手骑着马，轻快地跑过田野。'),('The lesson focused on cantering smoothly.','那节课重点练习平稳地采用轻快跑步态。'),sources=S('cantering','canter'))
W('prance','英 /prɑːns/；美 /præns/','昂首高抬步；蹦蹦跳跳；得意地走',
 '马精神足，脚抬得高高地走；人穿上新衣服，得意地来回展示，都能 prance。它比普通 walk 多一层显眼、轻快或炫耀的姿态。',
 '较早写马高抬步，也很早用于人的得意走姿；远源未定，有日耳曼炫耀词等分析，不能定成现代 prank 和 dance 的简单拼合。',PRANCE,
 'prance around the room；prance across the stage；a horse begins to prance。',
 'prance about in a new outfit；prance past the mirror。',
 'prance 着重高步、蹦跳或炫耀，sneak 是悄悄行动；一个显眼，一个尽量不引人注意。',
 ('The children began to prance around the room.','孩子们开始在房间里蹦蹦跳跳。'),('He liked to prance around in his new coat.','他喜欢穿着新外套，得意地来回走。'),sources=S('prance','prance'))
W('prances','英 /ˈprɑːnsɪz/；美 /ˈprænsɪz/','昂首高步、蹦跳、得意地走〔第三人称单数〕',
 '她一听音乐就高兴地蹦着走，或马昂着头高抬步，是 prances。具体是快乐还是炫耀，要看人物和语气。',
 'prance + -s，拼写只添 -s，基础末音 /s/ 后读 /ɪz/。',PRANCE+[['prance + -s → prances','他、她或它高抬步、得意地走']],
 'prances across the stage；prances around the garden；prances in a new dress。',
 'the pony prances；prances past the crowd。',
 'prances 不只是跑得快，sprints 才主要写冲刺；高抬步、展示姿态可能速度并不快。',
 ('She prances across the stage in bright boots.','她穿着鲜艳的靴子，在舞台上轻快高步地走过。'),('The pony prances beside the fence.','小马在围栏旁昂首高步地走着。'),sources=S('prances','prance'))
W('pranced','英 /prɑːnst/；美 /prænst/','昂首高步、蹦跳、得意地走了',
 '穿上新衣服，在镜子前得意地走来走去，可以说 pranced。也可轻松写孩子高兴得蹦蹦跳跳。',
 'prance 去 e 加完整 -ed；/s/ 后读 /t/，不新增 /ɪd/ 音节。',PRANCE+[['prance + -ed → pranced','过去显眼、轻快或得意地高步行走']],
 'pranced around the room；pranced onto the stage；pranced past the mirror。',
 'pranced in her new shoes；the horse pranced。',
 'pranced 不必带贬义；写孩子高兴蹦跳时可很亲切，写成年人炫耀时才可能有揶揄。',
 ('The children pranced around the garden after the rain.','雨后，孩子们在花园里高兴地蹦跳。'),('He pranced past the mirror in his new jacket.','他穿着新夹克，得意地从镜子前走过。'),sources=S('pranced','prance'))
W('prancing','英 /ˈprɑːnsɪŋ/；美 /ˈprænsɪŋ/','正在昂首高步、蹦跳；轻快高步的',
 '马头昂着、脚抬得高，或人高兴得带着表演姿态走，是 prancing。它把姿势而不只是方向写出来。',
 'prance 去 e 加 -ing；过程分词也能形容马、动作的高步姿态。',PRANCE+[['prance + -ing → prancing','高抬步、蹦跳的过程或姿态']],
 'a prancing horse；prancing around the room；prancing across the stage。',
 'prancing in front of a mirror；prancing children。',
 'prancing 和 dancing 都可能有蹦跳，dancing 是跳舞；走得像表演也不一定真的在跳舞。',
 ('A prancing horse is painted on the sign.','牌子上画着一匹昂首高步的马。'),('They were prancing around in their new costumes.','他们穿着新服装，得意又兴奋地走来走去。'),sources=S('prancing','prance'))
W('trotter','英 /ˈtrɒtə/；美 /ˈtrɑtɚ/','善快步跑的马；作为食材的蹄、脚',
 '马场里的 a trotter 可以是善于快步跑的马。菜单里的 a pig’s trotter 则是猪蹄，食材这层不能按人称后缀直接译成跑步的人。',
 'trot 双写 t 加完整 -er；马、信使、作食材的四足兽脚等用法都很早。现代学习可先看小跑动作，不把次序当成精确历史年表。',
 [['trot + -er 的人、动物等做事者构词','较早有快步马、信使等材料'],['trotter 也早用于作为食材的四足兽脚','不是现代英语中所有 -er 都只表示人']],
 'a fine trotter 善快步跑的马；a pig’s trotter 猪蹄。',
 'train a trotter；braised pig’s trotter 卤猪蹄、炖猪蹄。',
 'trotter 是特定马匹或食材名称，trot 是步态、动作；菜单和马场里相同词的指代不同。',
 ('The horse was trained as a trotter.','那匹马被训练成快步赛马。'),('The menu included braised pig’s trotter.','菜单上有炖猪蹄。'),sources=S('trotter','trotter'))
W('trotters','英 /ˈtrɒtəz/；美 /ˈtrɑtɚz/','快步马〔复数〕；蹄、猪蹄等食材〔复数〕',
 '赛马场里几匹快步马是 trotters；餐桌上 pigs’ trotters 则是猪蹄。名词来自跑动材料，具体指代靠搭配定。',
 'trotter + -s，读 /z/；基础词由 trot 双写 t 加 -er，复数直接加 -s。',
 [['trot → trotter','快步跑的马；也有很早的蹄脚食材义'],['trotter + -s → trotters','多匹快步马，或多个蹄脚']],
 'pigs’ trotters 猪蹄；trained trotters 受训的快步马。',
 'braised trotters；a pair of trotters。',
 'trotters 在菜单上常是蹄脚，不是就餐的人；不能见 -er 就认成职业或人物。',
 ('The stall sold braised pigs’ trotters.','那个摊位卖卤猪蹄。'),('Several trotters were training on the track.','几匹快步马正在跑道上训练。'),sources=S('trotters','trotter'))
W('mosey','英 /ˈməʊzi/；美 /ˈmoʊzi/','慢悠悠地走、走一趟〔尤美式口语〕',
 '没赶时间，就轻轻松松走去咖啡馆，可以说 mosey over。说 Shall we mosey on? 也像轻松招呼：咱们接着走吧。',
 '早期美式口语有离开、走开义，来源未定；有英国方言 mose about 或西班牙语 vamos 缩变等分析。现代常用轻松、不着急的走法。',MOSEY,
 'mosey over 慢悠悠走过去；mosey on 继续走；mosey down to the café。',
 'mosey around town；mosey off home。',
 'mosey 口语、轻松，march 常有坚定、整齐的动作感；都能走到目的地，姿态语气不同。',
 ('We can mosey down to the café after lunch.','午饭后，我们可以慢悠悠走去咖啡馆。'),('I might mosey around the market for a while.','我可能去市场慢悠悠逛一会儿。'),sources=S('mosey','mosey'))
W('moseys','英 /ˈməʊziz/；美 /ˈmoʊziz/','慢悠悠地走、走去〔第三人称单数〕',
 '他吃完饭不着急，慢慢走到花园里去，是 moseys out to the garden。这个词常带悠闲、随意的口语味。',
 'mosey 末尾 y 前是元音字母 e，直接加 -s → moseys；不改成 mosies，读 /z/。',MOSEY+[['mosey + -s → moseys','保留 y，他或她慢悠悠走去']],
 'moseys down the street；moseys over to the door；moseys around the garden。',
 'moseys into town；moseys on home。',
 'moseys 轻松慢走，rushes 是赶、冲；不能都按不分速度语气的 go 机械翻译。',
 ('He moseys down to the garden after breakfast.','早餐后，他慢悠悠走到花园里。'),('She moseys around the market on Saturday mornings.','周六早晨，她会慢悠悠地逛市场。'),sources=S('moseys','mosey'))
W('moseyed','英 /ˈməʊzid/；美 /ˈmoʊzid/','慢悠悠地走去了',
 '刚才轻轻松松走到另一家店，或散着步回家，可以说 moseyed。它不给人赶路、冲刺的紧迫感。',
 'mosey 直接加完整 -ed，保留 y → moseyed；结尾读 /d/，原有 /i/ 不等于新加一个 /ɪd/ 音节。',MOSEY+[['mosey + -ed → moseyed','保留 y，过去慢悠悠地走']],
 'moseyed over to the café；moseyed home；moseyed along the street。',
 'moseyed around the shops；moseyed down to the river。',
 'moseyed 是轻松的走法，trudged 常有疲惫、沉重；同样走得慢，感受不同。',
 ('We moseyed over to the café after the film.','电影结束后，我们慢悠悠走去咖啡馆。'),('They moseyed along the river until sunset.','他们沿河慢悠悠走着，直到日落。'),sources=S('moseyed','mosey'))
W('moseying','英 /ˈməʊziɪŋ/；美 /ˈmoʊziɪŋ/','正在慢悠悠地走、闲逛',
 '不赶路，边走边看周围，就是 moseying。动作可以有目的地，也可以只是随意逛一逛，语气通常轻松。',
 'mosey 直接加 -ing，保留 y → moseying；不是 moseing，也不把 y 改成 i。',MOSEY+[['mosey + -ing → moseying','保留 y，慢悠悠走动的过程']],
 'moseying around town；moseying down the street；moseying along。',
 'moseying over to the café；just moseying around。',
 'moseying 有悠闲味，loitering 往往让人感到无明确事情地逗留；慢走与被认为不该久留的语气不同。',
 ('We spent the morning moseying around town.','我们一上午都在城里慢悠悠地逛。'),('He was moseying along the path, enjoying the sunshine.','他沿着小路慢悠悠走着，享受阳光。'),sources=S('moseying','mosey'))
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_zhu',ROOTS,WORDS)
 extend_lessons()
