"""Wandering, straying, leisurely walking and climbing through obstacles."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
def S(word,base):
 return ['https://en.wiktionary.org/wiki/'+word+'#English','https://www.etymonline.com/word/'+base]
EXISTING_ROOT_ADDITIONS={
 'B4119':dict(words='wander wanders wandered wandering'.split(),label='wander 的脚步、目光和思绪游走',note='wander 承古英语 wandrian，较远接转、绕材料；实体走动与思绪、目光游移按现代场景分别解释。'),
 'C0045':dict(words='amble ambles ambled ambling'.split(),label='amble：从平稳马步到轻松步行',note='经法语 ambler 接拉丁语 ambulare；早期英语主要用于马和骑行，后来也用于人。现代 -ed、-ing 去 e 加完整词尾。'),
 'A2238':dict(words='ramble rambles rambled rambling scramble scrambles scrambled scrambling'.split(),label='ramble、scramble 的不同旧动作材料',note='ramble 可联系旧漫游形式，scramble 可联系抓扒、scrabble 等；各自中间路线有争议，不因都写 -ble 就认成同一个现成现代基词。'),
 'B3446':dict(words='lounge lounges lounged lounging'.split(),label='lounge：懒洋洋休息及供休息的地方',note='lounge 来源未定，可能联系法语躺长等材料，也有其他分析；现代名词可说休息室、会客处和沙发，动词说闲坐、闲躺。'),
 'B3980':dict(words='climb clamber clambers clambered clambering'.split(),label='clamber 与 climb 的可能反复攀爬联系',note='clamber 可能接 climb、旧过去式 clamb 的反复动作形式，也有北欧同族材料分析；保留路线不确定性，现代动作常手脚并用、跨越障碍。'),
 'A1760':dict(words='wander wanders wandered stray strays strayed straying amble ambles ambled ambling ramble rambles rambled rambling stroll strolls strolled strolling loiter loiters loitered loitering lounge lounges lounged lounging clamber clambers clambered clambering scramble scrambles scrambled scrambling'.split(),label='走动、闲逛、偏路、攀爬与争抢的词形',note='本组规则过去词尾均读 /d/；strayed 保留 y，lounged 的结尾 /dʒd/ 不增 /ɪd/；ramble、scramble 去 e 加完整词尾。'),
}
WANDER=[['古英语 wandrian → 中古英语 wandren → wander','没有固定路线地走，较远联系转、绕的日耳曼材料'],['脚步游走 → 目光、心思离开眼前主线','现代可以是轻松闲逛，也可以是分心，不自动等于已经迷路']]
W('wanders','英 /ˈwɒndəz/；美 /ˈwɑːndərz/','漫游、闲走、走神、目光游移〔第三人称单数〕；闲逛〔复数〕',
 '一个人在街边这儿看那儿逛，或脑子听着听着跑到别处，用 wanders。核心像路线没有收在一条线上。',
 'wander + -s，读 /z/；常见动词三单，闲逛名词复数也同形。原来的 er 是基础旧形式的一部分。',WANDER+[['wander + -s → wanders','他、她走走逛逛；心思、目光游走']],
 'wanders through the market 是在市场闲逛，his mind wanders 是他走神；eyes wander 是目光四处游移。',
 'wanders off 走开、跑题；wanders around the town 在镇里闲逛。',
 'wanders 可以完全知道自己在哪里，只是没固定路线；gets lost 才明确说迷路。',
 ('She wanders through the market looking at the stalls.','她在市场里闲逛，看各个摊位。'),('His mind wanders during long explanations.','解释一长，他就走神。'),sources=S('wanders','wander'))
W('wandered','英 /ˈwɒndəd/；美 /ˈwɑːndərd/','漫游、闲逛了；走偏、走神、跑题了',
 '刚才没赶着去某处，只是边看边走，是 wandered；讨论的话题、脑子里的念头也能走着走着偏到别处。',
 'wander + 完整 -ed，读 /d/；基础 er 保留，英美元音不同，但现代规则过去词尾相同。',WANDER+[['wander + -ed → wandered','过去四处走动或注意、路线游移']],
 'wandered around the old town 是在老城闲逛，wandered off the path 是走离小路；the discussion wandered 是讨论跑题。',
 'wandered into a shop 闲走进一家店；thoughts wandered 思绪飘远。',
 'wandered into 常带并非一开始就直奔目标的感觉，headed straight for 则明确朝目标去；走到同一家店，路线意图不同。',
 ('We wandered through the old streets after lunch.','午饭后，我们在老街里闲逛。'),('My thoughts wandered back to our first meeting.','我的思绪飘回到我们第一次见面。'),sources=S('wandered','wander'))
STRAY=[['法语 estraier、estraié 等走失材料 → 英语 stray','更远有街路词族与“游到外面”两种分析，具体路线不统一'],['走离原处 → 走失动物；离散、偶然偏来的东西','名词走失动物在英语记录很早，不能全说现代动词之后才造出']]
W('stray','/streɪ/','偏离、走失；走失的、散落的、零星的；流浪动物',
 '羊离开羊群，脚步偏出小路，是 stray；一根头发从发束跑出来，或一个念头飘进脑海，也像离开原本该在的位置。',
 '接古法语走失、漫游材料，更远有 street 所属的路词族与 extra vagari 向外游走等不同分析。英语走失动物名词也有较早独立借入背景。',STRAY,
 'a stray cat 是流浪猫，stray from the path 是偏离小路，a stray thought 是偶然飘来的念头；a stray 可直接指走失动物。',
 'stray hairs 散开的几根头发；stray off topic 偏离话题。',
 'stray 比 wander 更突出离开原来、应该在的路或群体；wander 可以只是没有固定路线地闲逛。',
 ('We found a stray cat outside the station.','我们在车站外发现一只流浪猫。'),('Try not to stray from the main topic.','尽量别偏离主要话题。'),sources=S('stray','stray'))
W('strays','/streɪz/','走失动物〔复数〕；偏离、走失〔第三人称单数〕',
 '几只没人领回的猫狗，是 strays；一个人说着说着离开重点，动词用 strays。一个是走离原处的对象，一个是走偏动作。',
 'stray + -s，元音后读 /z/；ay 的 y 保留，不改 ies，名词复数与动词三单同形。',STRAY+[['stray + -s → strays','多个走失动物；它偏离原线']],
 'care for strays 是照顾流浪动物，strays from the topic 是偏离主题；strays too far 是走得离原路太远。',
 'strays into another field 跑到另一领域；cats and other strays 猫和其他流浪动物。',
 'strays 作为动物名词不自动说明野生；feral 更突出野化、未驯养，走失宠物同样可以是 a stray。',
 ('The shelter takes in strays from the neighbourhood.','收容所接收附近的走失、流浪动物。'),('His answer often strays from the question.','他的回答常偏离问题。'),sources=S('strays','stray'))
W('strayed','/streɪd/','走偏了；偏离了；走失了',
 '本来沿着一条路走，后来脚步出了这条线，就是 strayed；谈话也会从主题走偏。',
 'stray + -ed，元音字母 a 后的 y 保留，词尾读 /d/。不是把 y 改成 i。',STRAY+[['stray + -ed → strayed','过去偏离路线、主题或原来的群体']],
 'strayed from the path 走离小路；strayed into the garden 是误走、游荡进花园。',
 'strayed too far 离开得太远；strayed off topic 跑题了。',
 'strayed 强调离开原线；wandered 可以只是随意逛，未必偏离什么。',
 ('We strayed from the marked path in the fog.','雾里，我们走偏了，离开了有标记的小路。'),('The discussion strayed into personal matters.','讨论偏到了私人事情上。'),sources=S('strayed','stray'))
W('straying','/ˈstreɪɪŋ/','正在走偏、走失、偏离',
 '脚步一点点走出该走的路，话题一点点离开重点，正在发生时就是 straying。',
 'stray + -ing，y 保留；/eɪ/ 后接 /ɪŋ/，不要把整段压成一个音节。',STRAY+[['stray + -ing → straying','正在离开原路、原处或话题']],
 'straying from the subject 是说话正在跑题；straying onto private land 是走进别人的地界。',
 'keep someone from straying 防止某人走失、偏离；straying eyes 游移的目光。',
 'straying from 指离开某条线，straying into 指偏进某个地方、领域，介词把方向讲清楚。',
 ('The dog kept straying into the road.','那条狗老是乱跑到马路上。'),('We are straying from the point of the meeting.','我们正在偏离这次会议的重点。'),sources=S('straying','stray'))
AMBLE=[['拉丁语 ambulare 走路 → 古法语 ambler → 英语 amble','早期英语主要说马或骑马的人走得平稳'],['平稳的马步 → 人从容、悠闲地走','英语用于人的步行在较晚时期变得常见；不必把现代每个音节硬拆成拉丁词素']]
W('ambles','/ˈæmbəlz/','从容、悠闲地走〔第三人称单数〕；悠闲散步〔复数〕',
 '不赶时间，脚步放得慢而平稳，边走边看看，用 ambles。像把路走得松一点。',
 'amble + -s，词尾读 /z/；基础词经法语接拉丁语 ambulare，走路。',AMBLE+[['amble + -s → ambles','他、她慢悠悠地走；几次闲步']],
 'ambles along the lane 沿小巷悠闲走；ambles over to someone 慢慢走到某人身边。',
 'ambles through the park；lazy afternoon ambles 下午悠闲散步。',
 'ambles 突出轻松、不急的步态；strays 突出偏路，两者不是同一个画面。',
 ('He ambles to the bakery every Sunday morning.','每个星期天早上，他都慢悠悠地走到面包店。'),('She enjoys quiet ambles along the river.','她喜欢沿河安静地散步。'),sources=S('ambles','amble'))
W('ambled','/ˈæmbəld/','悠闲地走了；从容步行了',
 '刚才并没有匆忙赶过去，而是慢慢晃过去，就是 ambled。句子里常能感觉到人不着急。',
 'amble 去末尾不发音 e，加完整 -ed，词尾读 /d/；不是另加一个独立音节。',AMBLE+[['amble → ambled','把从容步行放进过去的场景']],
 'ambled into the room 慢悠悠走进房间；ambled back home 悠闲走回家。',
 'ambled across the square；ambled along beside someone 慢慢并肩走。',
 'strolled 和 ambled 都可说悠闲走；ambled 更容易让人注意那种松弛、慢吞吞的步子。',
 ('We ambled through the village after breakfast.','早饭后，我们在村子里悠闲地走了走。'),('He ambled over and asked what we were doing.','他慢悠悠走过来，问我们在干什么。'),sources=S('ambled','amble'))
W('ambling','/ˈæmbəlɪŋ/','正在悠闲步行；慢悠悠走着的',
 '人在往前走，却没有赶路的劲头；步子舒缓平稳，这种进行中的状态叫 ambling。',
 'amble 去 e 加 -ing；历史上先常说马的平稳步态，现代也自然用于人。',AMBLE+[['amble → ambling','悠闲走动正在进行；也可描述这种步态']],
 'ambling along 悠闲走着；an ambling pace 是不紧不慢的步速。',
 'ambling through the streets；come ambling over 慢悠悠走过来。',
 'ambling 表现走的样子，不保证路线曲折；meandering 更容易突出路线绕来绕去。',
 ('A couple were ambling along the beach.','一对伴侣正沿着海滩悠闲地走。'),('We spent the afternoon ambling around the old town.','我们整个下午都在老城里慢悠悠地逛。'),sources=S('ambling','amble'))
RAMBLE=[['中古英语 ramblen 等漫游形式 → ramble','可能联系 roam 的旧形式及反复动作词尾，也有荷兰语材料分析，具体路线不完全统一'],['没有固定路线地走 → 讲话没有收住主线','现代既能说愉快漫步，也能说东拉西扯；两种感情色彩要看场景']]
W('rambles','/ˈræmbəlz/','漫步〔复数〕；漫游、东拉西扯〔第三人称单数〕',
 '走路没有定死路线，想到哪儿走到哪儿；说话没有收住主线，想到哪儿说到哪儿，都能用 rambles。',
 'ramble + -s，词尾读 /z/；基础词的旧来路有争议，不把 ram 当成可确定的现代拆分。',RAMBLE+[['ramble + -s → rambles','几次漫步；他、她散漫地走或说']],
 'country rambles 乡间漫步；rambles on about something 没完没了地东说西说。',
 'rambles through the countryside；rambles on for hours。',
 'rambles 用于散步可以很愉快，用于讲话常暗示不够简洁，不能统一翻成负面的乱走。',
 ('We used to take long rambles in the hills.','我们过去常在山间长时间漫步。'),('He rambles on whenever someone asks about his travels.','只要有人问起旅行，他就东拉西扯地说个不停。'),sources=S('rambles','ramble'))
W('rambled','/ˈræmbəld/','漫步了；东拉西扯地说了',
 '脚步从一处随意走到另一处，或一句话牵出另一件事，过去发生的这种游走就是 rambled。',
 'ramble 去 e 加完整 -ed，词尾读 /d/；-ble 保留在基础词的历史形式中。',RAMBLE+[['ramble → rambled','过去漫游，或讲话不断岔出去']],
 'rambled through the woods 漫步穿过树林；rambled on about childhood 絮絮说起童年。',
 'rambled from one subject to another 从一个话题扯到另一个话题。',
 'rambled 并不要求走得快慢；ambled 主要写慢而松弛的步子，关注点不同。',
 ('We rambled through the fields until sunset.','我们在田野里漫步，一直到日落。'),('The speaker rambled for ten minutes without answering the question.','发言人东拉西扯了十分钟，也没回答问题。'),sources=S('rambled','ramble'))
W('rambling','/ˈræmbəlɪŋ/','漫步；正在漫游；漫无条理的；曲折延伸的',
 '一条路岔出去又接着伸，房子走过一间还有一间，讲话说到这里又扯到那里，都像 rambling：一路铺开，却没有一条紧收的主线。',
 'ramble 去 e 加 -ing，可作动作形式，也可作形容词；描述散布延伸与话题散漫都有较早使用。',RAMBLE+[['ramble → rambling','正在漫游；也把散开、岔出去的样子用于讲话和建筑']],
 'a rambling speech 是冗长散漫的讲话；a rambling old house 是房间多、布局曲折的老房子；go rambling 去徒步漫游。',
 'a rambling explanation；a rambling country walk。',
 'rambling explanation 常嫌不够有条理；detailed explanation 只说详细，并不自动表示跑题。',
 ('He gave a rambling answer that confused everyone.','他的回答东拉西扯，把大家都说糊涂了。'),('We spent the weekend rambling through the hills.','我们周末在山间徒步漫游。'),sources=S('rambling','ramble'))
STROLL=[['约十七世纪初 stroll 表示四处游荡','来源未定，可能接日耳曼语言中的流浪、游荡材料'],['游荡 → 不赶路、随意走一走','现代常指轻松散步，较远的语源猜测不拿来当确定拆分']]
W('stroll','英 /strəʊl/；美 /stroʊl/','散步；悠闲地走',
 '吃过饭，没有任务地出去走一走，就是 take a stroll。重点是轻松走走，不是赶着把一段路走完。',
 '基础词的来源未定，可能联系德语等语言的游荡词；现代不能可靠拆成更小的英语前后缀。',STROLL,
 'take a stroll、go for a stroll 都说出去散步；stroll along the river 是沿河悠闲走。名词和动词都很常见。',
 'an evening stroll 傍晚散步；stroll into a shop 悠闲走进商店。',
 'walk 是一般的走路；stroll 额外带轻松、不匆忙的感觉。通勤走得很急，通常只说 walk。',
 ('We went for a stroll after dinner.','晚饭后，我们出去散了散步。'),('You can stroll along the river and watch the boats.','你可以沿河悠闲地走，看来往的船。'),sources=S('stroll','stroll'))
W('strolls','英 /strəʊlz/；美 /stroʊlz/','散步〔复数〕；悠闲地走〔第三人称单数〕',
 '每天晚饭后的一段闲步，合起来是 evening strolls；他不紧不慢地走过去，动词用 strolls。',
 'stroll + -s，词尾读 /z/；双 l 保留，名词复数与动词三单同形。',STROLL+[['stroll + -s → strolls','几次散步；他、她悠闲地走']],
 'takes long strolls 长时间散步；strolls past the window 不紧不慢走过窗前。',
 'leisurely strolls；strolls around the neighbourhood。',
 'strolls in 可以描写人轻松走进来；若上下文是别人都很急，也可能带说话人对其悠闲姿态的评价。',
 ('She takes short strolls around the lake.','她常绕湖走一小段，散散步。'),('He strolls into the office with a cup of coffee.','他端着一杯咖啡，不紧不慢地走进办公室。'),sources=S('strolls','stroll'))
W('strolled','英 /strəʊld/；美 /stroʊld/','散步了；悠闲走过去了',
 '这段路是慢慢走过去、顺便看看周围的，不像赶任务，用 strolled 就能把这种松弛感带出来。',
 'stroll + -ed，词尾读 /d/；已有双 l，不需要再增一个 l。',STROLL+[['stroll + -ed → strolled','过去轻松、不匆忙地走']],
 'strolled home 悠闲走回家；strolled through the market 在市场里散步闲逛。',
 'strolled along the beach；strolled over to the table。',
 'strolled 强调从容步行；strayed 强调偏离路线。一个人可以 strolled home，路线完全没有走偏。',
 ('We strolled home under the streetlights.','我们在路灯下悠闲地走回家。'),('She strolled over to see what we were making.','她不紧不慢走过来，看看我们在做什么。'),sources=S('strolled','stroll'))
W('strolling','英 /ˈstrəʊlɪŋ/；美 /ˈstroʊlɪŋ/','正在散步；悠闲地走着',
 '把散步的镜头停在半路：人正慢慢往前走，可能聊天、看景，这时就是 strolling。',
 'stroll + -ing；基础词没有末尾不发音 e，直接接完整词尾。',STROLL+[['stroll + -ing → strolling','正在悠闲步行，也可描述边走边活动的人']],
 'strolling through the park 在公园散步；strolling musicians 是边走边表演的乐手。',
 'spend an hour strolling；people strolling by 悠闲走过的人。',
 'strolling 是放松走动；loitering 常突出在某处磨蹭、逗留，甚至让旁人觉得没什么明确目的。',
 ('People were strolling through the park in the evening sun.','人们在傍晚的阳光里逛公园。'),('We spent an hour strolling around the harbour.','我们在港口周围悠闲地走了一个小时。'),sources=S('strolling','stroll'))
LOITER=[['中古英语 loitren 等形式 → loiter','可能联系中古荷兰语摇晃、散漫行动的材料，远源未定'],['行动拖拉、不赶着做事 → 闲站、闲逛、逗留','相关 loitering 形式在英语记录也很早，不把所有词义强排成单线出现']]
W('loiter','英 /ˈlɔɪtə/；美 /ˈlɔɪtər/','闲逛、逗留；磨蹭、拖拉',
 '别人已经准备出发，你还在门口看看这儿、摸摸那儿；或者没明确事情做，却一直在一个地方晃，都可以说 loiter。',
 '中古英语已有，可能联系荷兰语松散、摇晃行动的词；末尾 er 是旧基础形式的一部分。',LOITER,
 'loiter outside a shop 在商店外逗留；loiter on the way home 是回家路上磨蹭。可以走动，也可以站着待着。',
 'loiter around the entrance；do not loiter 别磨蹭、别逗留。',
 'linger 常能带舍不得离开的感觉；loiter 更容易让人看到无明确目的或拖拖拉拉的状态。',
 ('Please do not loiter by the entrance.','请不要在入口处逗留。'),('We cannot loiter here all afternoon.','我们不能整个下午都在这儿磨蹭。'),sources=S('loiter','loiter'))
W('loiters','英 /ˈlɔɪtəz/；美 /ˈlɔɪtərz/','闲逛、逗留、磨蹭〔第三人称单数〕',
 '该往前走的时候，他还停停看看、迟迟不动；或总在同一个地方没事晃，动词就用 loiters。',
 'loiter + -s，词尾读 /z/；基础 er 保留，不是另外给动词加“某种人”的 -er。',LOITER+[['loiter + -s → loiters','他、她在某处闲逛、磨蹭']],
 'loiters near the gate 在门附近逗留；loiters over breakfast 吃早饭磨磨蹭蹭。',
 'loiters outside；loiters on the way。',
 'waits 可以是在等明确的人或事情；loiters 突出逗留、磨蹭的样子，未必有清楚的等待目标。',
 ('He loiters by the school gate after class.','下课后，他总在校门旁闲待着。'),('She loiters over breakfast whenever she has a free morning.','只要上午没事，她吃早饭就慢慢磨蹭。'),sources=S('loiters','loiter'))
W('loitered','英 /ˈlɔɪtəd/；美 /ˈlɔɪtərd/','逗留了；闲逛、磨蹭了',
 '事情没推进，人也没真正离开，就在那一片晃了一阵，过去的这个片段叫 loitered。',
 'loiter + -ed，词尾读 /d/；英式 er 中的 r 在后面没有元音时通常不发，美式通常发。',LOITER+[['loiter + -ed → loitered','过去闲待、拖拉或逗留']],
 'loitered in the corridor 在走廊里逗留；loitered on the way 回来、过去的路上磨蹭。',
 'loitered for a while；loitered outside the café。',
 'loitered 不等于一定做坏事；它描写的是没有明确行动目标或拖拖拉拉的样子，态度还得看上下文。',
 ('They loitered outside the café until it opened.','他们在咖啡馆外闲待着，一直到开门。'),('We loitered on the way and missed the start of the show.','我们路上磨蹭，错过了演出的开头。'),sources=S('loitered','loiter'))
W('loitering','英 /ˈlɔɪtərɪŋ/；美 /ˈlɔɪtərɪŋ/','正在逗留、闲逛；闲待、磨蹭的行为',
 '监控画面里，一个人在门口走来走去却一直不进去；同伴催你出发，你还原地晃着，这种状态可以叫 loitering。',
 'loiter + -ing；相关形式在中古英语已出现，现代仍能当进行式，也能作行为名词。',LOITER+[['loiter + -ing → loitering','把闲待、逗留、拖拉当作进行中的动作或一种行为']],
 'no loitering 常见于告示，意思是请勿逗留；loitering around the station 在车站附近闲逛。',
 'stop loitering 别再磨蹭；people loitering nearby 在附近闲待的人。',
 'strolling 多是轻松散步，loitering 更关心人一直在某处逗留、事情没往前走。',
 ('A few people were loitering near the entrance.','几个人在入口附近闲待着。'),('Stop loitering and help me carry these bags.','别磨蹭了，来帮我提这些袋子。'),sources=S('loitering','loiter'))
LOUNGE=[['苏格兰英语 lounge：闲待、懒散休息','来源未定，联系法语伸展身体等材料是一种分析，并非定论'],['懒洋洋休息 → 闲躺、闲坐；休息处和沙发等名词用法','现代动词表现人的放松姿态，名词依场景指休息室、会客处或沙发']]
W('lounges','/ˈlaʊndʒɪz/','休息室、会客厅、沙发〔复数〕；懒洋洋休息〔第三人称单数〕',
 '机场里坐着等候的房间可以是 lounges；一个人把身体松松地靠在椅子里，动词也用 lounges。词性决定你是在说地方还是姿态。',
 'lounge + -s，/dʒ/ 后词尾读 /ɪz/；现代 lounge 的地方名词与休息动作有关，更早来源未定。',LOUNGE+[['lounge + -s → lounges','多个休息处、沙发；他、她懒洋洋休息']],
 'airport lounges 机场休息室；lounges on the sofa 懒洋洋躺在沙发上。',
 'departure lounges 候机厅；lounges around the house 在家懒散待着。',
 'lounges 名词的具体家具义、房间义有地区差别；机场场景一般先理解成休息、等候的空间。',
 ('The airport has several quiet lounges.','这座机场有几个安静的休息室。'),('He lounges on the sofa after lunch.','午饭后，他懒洋洋地靠躺在沙发上。'),sources=S('lounges','lounge'))
W('lounged','/laʊndʒd/','懒洋洋地坐着、躺着休息了',
 '不用挺直坐好，也没急着干活，把身体放松地靠着、躺着，过去这样的休息状态叫 lounged。',
 'lounge 去不发音 e，加完整 -ed，词尾读 /d/；/dʒd/ 连着发，不加 /ɪd/。',LOUNGE+[['lounge → lounged','过去闲躺、闲坐着休息']],
 'lounged by the pool 在泳池边懒洋洋休息；lounged in a chair 放松靠坐在椅子里。',
 'lounged around all morning；lounged on the grass。',
 'rested 只说休息；lounged 会让人更容易看到身体松散、闲适的姿态。',
 ('We lounged by the pool all afternoon.','我们整个下午都在泳池边懒洋洋地休息。'),('She lounged in an armchair with a book.','她拿着一本书，放松地靠在扶手椅里。'),sources=S('lounged','lounge'))
W('lounging','/ˈlaʊndʒɪŋ/','正在闲坐、闲躺；适于放松休息的',
 '人舒服地靠着，暂时不想起身做事，这个进行中的画面就是 lounging；也能用来形容供人这样休息的区域。',
 'lounge 去 e 加 -ing；这次 /dʒ/ 后接的是 /ɪŋ/，与 lounged 的 /dʒd/ 区别开。',LOUNGE+[['lounge → lounging','正在懒洋洋休息；也可说明某处供这种休息使用']],
 'lounging on the couch 闲躺在长沙发上；a lounging area 是供人放松休息的区域。',
 'spend the day lounging；lounging around at home。',
 'lounging 关注松弛休息的姿态；loitering 关注闲待、逗留，可以站着来回晃，未必舒服地靠躺。',
 ('The cat was lounging in a patch of sunlight.','猫正懒洋洋地卧在一块阳光里。'),('We spent Sunday lounging around at home.','星期天我们就在家里懒洋洋地休息。'),sources=S('lounging','lounge'))
CLAMBER=[['中古英语 clambren 等攀爬形式 → clamber','可能联系 climb、旧过去式 clamb 的反复动作形式，也有北欧语言比较材料'],['抓住、撑住身体，手脚并用地前进','既可往高处爬，也可跨过岩石、障碍，不只表示垂直向上']]
W('clamber','英 /ˈklæmbə/；美 /ˈklæmbər/','手脚并用地爬；费力攀越',
 '台阶不好走，就用手抓一下、脚蹬一下，撑着身体翻过去，这比普通走路多了攀抓的动作，叫 clamber。',
 '可能接 climb 的旧形式 clamb 和反复动作材料，具体来路有不同分析。现代 clamber 的 b 要发音，climb 的 b 通常不发。',CLAMBER,
 'clamber over the rocks 爬过岩石；clamber into a boat 费劲地爬进船里；常用介词交代爬向哪里。',
 'clamber up the bank 爬上河岸；clamber out of a window 爬出窗户。',
 'climb 范围更宽；clamber 更容易让人看见手抓脚蹬、姿势不够利落的过程。',
 ('We had to clamber over the rocks to reach the beach.','我们得手脚并用爬过岩石，才能到海滩。'),('The children began to clamber into the tree house.','孩子们开始手脚并用地往树屋里爬。'),sources=S('clamber','clamber'))
W('clambers','英 /ˈklæmbəz/；美 /ˈklæmbərz/','手脚并用地攀爬〔第三人称单数〕',
 '他不是顺顺当当地迈过去，而是一边抓一边蹬、把身体撑过去，动词用 clambers。',
 'clamber + -s，词尾读 /z/；基础 /b/ 保留，末尾 er 是基础词的一部分。',CLAMBER+[['clamber + -s → clambers','他、她攀越障碍、费力爬动']],
 'clambers over a wall 爬过墙；clambers onto the seat 费力爬上座位。',
 'clambers up the rocks；clambers out of the boat。',
 'clambers 不要求爬得很高，小孩爬上高座椅也可以用；重点是动作需要攀、撑。',
 ('The toddler clambers onto the sofa by himself.','那个蹒跚学步的孩子自己手脚并用爬上沙发。'),('She clambers over the low wall and waves to us.','她爬过矮墙，向我们挥手。'),sources=S('clambers','clamber'))
W('clambered','英 /ˈklæmbəd/；美 /ˈklæmbərd/','手脚并用爬过去了；费力攀上、爬出了',
 '扶一下边缘、蹬一下脚，把身体一点点挪过去，过去发生的这一串动作就是 clambered。',
 'clamber + -ed，规则词尾读 /d/；不要因为可能与 climb 有历史联系，就套用 climbed 的拼写或读音。',CLAMBER+[['clamber + -ed → clambered','过去费力攀爬、跨越或爬进爬出']],
 'clambered ashore 费力爬上岸；clambered onto the roof 攀上屋顶。',
 'clambered through the opening；clambered down the slope。',
 'clambered down 也成立：这个词写手脚并用的动作，向上、向下都能由介词补充。',
 ('We clambered down the steep bank to the river.','我们手脚并用，沿陡岸爬到河边。'),('He clambered into the truck and pulled the door shut.','他费力爬进卡车，把门拉上。'),sources=S('clambered','clamber'))
W('clambering','英 /ˈklæmbərɪŋ/；美 /ˈklæmbərɪŋ/','正在手脚并用地攀爬、翻越',
 '镜头里的人正抓着边沿、找脚下的支点，身体还没完全过去，这种正在进行的攀越叫 clambering。',
 'clamber + -ing，基础 er 保留；英式在后接元音的这里也发出 /r/。',CLAMBER+[['clamber + -ing → clambering','把攀爬、翻越的过程放到眼前']],
 'clambering over fallen trees 爬过倒下的树；clambering up a ladder 沿梯子费力往上爬。',
 'children clambering on the rocks；come clambering out 爬着出来。',
 'clambering 主要表现攀撑过程；scrambling 也能写费力爬动，还更常带急忙、争着行动的意味。',
 ('The children were clambering over the fallen tree.','孩子们正手脚并用爬过倒下的树。'),('I heard someone clambering up the ladder.','我听见有人正费力地沿梯子往上爬。'),sources=S('clambering','clamber'))
SCRAMBLE=[['十六世纪英语 scramble：攀爬、争抢等急促动作','来源未定，可能联系 scrabble、抓扒等方言材料，不作确定的现代音节拆分'],['急促争着行动；另发展出把东西弄乱、混在一起的用法','现代的争抢、费力攀爬、打乱顺序和炒蛋要按场景分开理解']]
W('scrambles','/ˈskræmbəlz/','急忙攀爬、争抢、设法凑齐、打乱〔第三人称单数〕；争抢、费力攀爬〔复数〕',
 '车快来了，他急忙找齐东西；座位不够，大家争着占；坡不好走，手脚并用往上赶，这些都能用 scrambles。',
 'scramble + -s，词尾读 /z/；基础词远源未定，可能联系抓扒、scrabble 等材料。',SCRAMBLE+[['scramble + -s → scrambles','他、她急忙行动、攀爬或打乱东西；多次争抢、攀爬']],
 'scrambles for a seat 争着找座位；scrambles up the slope 急忙爬上坡；程序 scrambles the order 是打乱次序。',
 'scrambles to finish work 急着赶完工作；scrambles the letters 打乱字母。',
 'scrambles for 突出争取某物；scrambles to do 突出仓促设法完成某事，后面接法帮你选义。',
 ('He scrambles to find his keys when the taxi arrives.','出租车一到，他就手忙脚乱地找钥匙。'),('The program scrambles the order of the questions.','这个程序会打乱题目的顺序。'),sources=S('scrambles','scramble'))
W('scrambled','/ˈskræmbəld/','急忙行动、攀爬、争抢了；被打乱的；炒制搅散的〔鸡蛋〕',
 '人急着手脚并用爬过去，是 scrambled；卡片次序被搅乱，也可以是 scrambled；鸡蛋边搅边炒成小块，就是 scrambled eggs。',
 'scramble 去 e 加完整 -ed，词尾读 /d/；既能作过去动作，也能形容已经被弄乱、搅散的状态。',SCRAMBLE+[['scramble → scrambled','过去仓促行动；东西被混乱、搅散后的样子']],
 'scrambled up the bank 急忙爬上岸；scrambled eggs 炒蛋；scrambled letters 被打乱的字母。',
 'scrambled to get ready；a scrambled message 被扰乱、难以直接读懂的信息。',
 'scrambled eggs 是边搅散边炒；an omelette 通常摊成一片。打乱信号的 scrambled 也不保证采用了特定加密方法。',
 ('We scrambled up the bank before the rain started.','下雨前，我们急忙手脚并用爬上河岸。'),('I made scrambled eggs for breakfast.','我早餐做了炒蛋。'),sources=S('scrambled','scramble'))
W('scrambling','/ˈskræmbəlɪŋ/','正在急忙攀爬、争抢、设法应付；打乱、搅散',
 '资源突然不够，大家忙着凑、忙着抢；前面突然有事，人赶紧爬过去、赶紧应付，这种仓促行动的过程叫 scrambling。',
 'scramble 去 e 加 -ing；可作进行形式，也可指攀爬、打乱信号等过程，具体看宾语和介词。',SCRAMBLE+[['scramble → scrambling','仓促行动、争抢或打乱东西正在进行']],
 'scrambling for tickets 争抢票；scrambling to find a solution 急忙寻找解决办法；scrambling eggs 边搅边炒蛋。',
 'send people scrambling 让人一下子忙乱起来；scrambling over rocks 手脚并用爬过岩石。',
 'scrambling 常带忙、急、争的感觉；ambling 则是不紧不慢地走，两者场景很不一样。',
 ('The announcement sent everyone scrambling for tickets.','消息一公布，大家立刻争着抢票。'),('We were scrambling over rocks when the sun came out.','太阳出来时，我们正手脚并用爬过岩石。'),sources=S('scrambling','scramble'))
def extend_lessons():
 extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_zfu',ROOTS,WORDS)
 extend_lessons()
