"""Hiking, hitchhiking, backpacking and straggling."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
def S(word,base):
 return ['https://en.wiktionary.org/wiki/'+word+'#English','https://www.etymonline.com/word/'+base]
EXISTING_ROOT_ADDITIONS={
 'B4160':dict(words='hike hikes hiked hiking hiker hikers hitchhike hitchhikes hitchhiked hitchhiking hitchhiker hitchhikers'.split(),label='hike 与 hitchhike：徒步、提价、搭便车',note='hike 方言来历未定，徒步支与上提、提价支的具体形成需分开；上提义或受 hitch 影响。hitchhike 是 hitch 挂接等材料与 hike 组成，较早已有搭接移动车辆的画面。'),
 'B4203':dict(words='backpack backpacks backpacked backpacking backpacker backpackers'.split(),label='backpack：背在身后的包，到背包旅行',note='back 背部 + pack 行囊先组成名词 backpack，后来动词说背着装备徒步、旅行，再有 -er 人称派生；不是把 back 当作返回前缀。'),
 'A2238':dict(words='straggle straggles straggled straggling straggler stragglers'.split(),label='straggle：走散、落在后面，或散乱延伸',note='straggle 接日耳曼行进材料，近源有北欧路线、旧英语动作词反复派生等分析；不是现代 struggle 的变元音形式，也不凭相近字形给它编确定来源。'),
 'B3398':dict(words='wayfarer wayfarers'.split(),label='wayfarer：走在路上的旅人',note='way 道路、路线 + fare 旧动词行进、旅行，再有 -er 做事者。wayfare 动词较晚可能由名词等逆构；不是一个购买车费的人。'),
 'B4119':dict(words='wanderer wanderers'.split(),label='wanderers：四处游走的人',note='wander + 完整 -er，再取复数；wander 承古英语 wandrian 等漫游材料。和 wonder 惊奇的现代意思、来路区分。'),
}
HIKE=[['hike 徒步支：英语方言材料，来源未定','较早有用力走、离开等意思'],['上提、提高价格等支发展','上提义可能与 hitch 相接，不把所有义硬说成登山向上']]
HITCHHIKE=[['hitch 挂接、借助移动车辆 + hike','较早名词、动词已有顺车行进的组合'],['hitchhike 搭便车 → hitchhiker','搭乘过路车辆的人，不一定自己拥有车辆']]
BACKPACK=[['back 背部 + pack 行囊 → backpack 名词','把装备背在背上的包'],['由背包名词发展出背包徒步、旅行的动词','再有 backpacker 与复数 backpackers']]
STRAGGLE=[['较早 straggle：偏离路径、同伴，走散','接日耳曼行进材料，具体近源有不同分析'],['离散、掉队 → 人落后、事物零散延伸','人群、房屋、枝条都可以形成不整齐的一线']]
WAYFARER=[['way 道路 + fare 旧动词行进、旅行的材料','fare 承古英语 faran 等，不是在这里说票价'],['构成旅人名词 wayfarer','wayfare 动词记录较晚，不以学习先后倒置历史']]
W('hikes','/haɪks/','徒步、远足〔第三人称单数〕；提高价格等；远足、涨幅〔复数〕',
 '周末上山步行可以说 hikes；账单里的 price hikes 是一次次涨价。前者走路，后者把数字往上提，基础词两支分别说明。',
 'hike + -s，/k/ 后读 /s/；动词三单、名词复数同形。不能把提价义直接解释成价格真的在山里走。',HIKE+[['hike + -s → hikes','他或她徒步、提高；多次远足、提价']],
 'hikes in the hills；price hikes 涨价；interest-rate hikes 加息。',
 'weekend hikes；hikes the fee 提高费用。',
 'hikes 是提高时常暗示明显上涨，cuts 才是降低；同一个 hike 还可说远足，要靠宾语定意思。',
 ('She hikes in the hills every weekend.','她每周末都在山里徒步。'),('The notice announced further price hikes.','通知宣布还会进一步涨价。'),sources=S('hikes','hike'))
W('hiked','/haɪkt/','徒步、远足了；提高、上提了',
 '昨天走了一段山路，是 hiked；票价被一下往上调，也可说 hiked。两个画面都常见，不只背成爬山。',
 'hike 去 e 加完整 -ed，/k/ 后读 /t/；不增加 /ɪd/ 音节。',HIKE+[['hike + -ed → hiked','过去徒步，或把数值、物件往上提']],
 'hiked through the forest；hiked the price；hiked up his trousers。',
 'hiked for three hours；fees were hiked。',
 'hiked the price 是提价，hiked the trail 是沿路徒步；同样作及物动词，宾语决定分支。',
 ('We hiked through the forest to the lake.','我们穿过森林，徒步到了湖边。'),('The company hiked the delivery fee last month.','那家公司上个月提高了配送费。'),sources=S('hiked','hike'))
W('hikers','英 /ˈhaɪkəz/；美 /ˈhaɪkɚz/','徒步、远足者〔复数〕',
 '沿山路、乡野路线走一段的人，是 hikers。它说参加步行活动的人，不是那些提高价格的人。',
 'hiker + -s，读 /z/；hike 去 e 加完整 -er，再取复数。',HIKE+[['hike → hiker → hikers','徒步动作，到徒步者，再到多人']],
 'experienced hikers；a group of hikers；a trail for hikers。',
 'hikers carrying backpacks；local hikers。',
 'hikers 着眼于徒步活动，climbers 更着眼于攀登；走山路不一定需要攀爬岩壁。',
 ('The hikers reached the lake before noon.','徒步者们中午前到了湖边。'),('The narrow trail is popular with experienced hikers.','那条窄路很受有经验的徒步者欢迎。'),sources=S('hikers','hike'))
W('hitchhikes','/ˈhɪtʃhaɪks/','搭便车旅行〔第三人称单数〕',
 '自己不一直走，也没开车，而是沿路搭过路人的车前进，是 hitchhikes。行程像一段段借别人的车接起来。',
 'hitchhike + -s，/k/ 后读 /s/；hitch 的挂接画面与 hike 结合，形成搭便车这个整体词。',HITCHHIKE+[['hitchhike + -s → hitchhikes','他或她沿路搭便车']],
 'hitchhikes across the country；hitchhikes from town to town。',
 'usually hitchhikes；hitchhikes with a friend。',
 'hitchhikes 说搭便车，hikes 说徒步；人可以一段步行、一段搭车，但不能把两个动词直接互换。',
 ('In the novel, he hitchhikes from town to town.','小说里，他搭着便车，在一个个城镇之间旅行。'),('The character hitchhikes across the country with a small backpack.','那个角色背着小包，搭便车穿越全国。'),sources=S('hitchhikes','hitchhike'))
W('hitchhiked','/ˈhɪtʃhaɪkt/','搭便车旅行了',
 '曾经一路搭过路车辆到了某地，可以说 hitchhiked。它交代出行方式，不是说坐了付费的长途客车。',
 'hitchhike 去 e 加完整 -ed，/k/ 后读 /t/；复合词按末尾 hike 的规则变形。',HITCHHIKE+[['hitchhike + -ed → hitchhiked','过去沿路搭便车前进']],
 'hitchhiked across Europe；hitchhiked to the coast。',
 'hitchhiked for several days；had hitchhiked there。',
 'hitchhiked 是搭便车，took a taxi 是乘出租车；普通交通叙述中两者不是同一种服务。',
 ('She hitchhiked to the coast during her student years.','学生时代，她曾搭便车去海边。'),('The memoir describes how they hitchhiked across Europe.','回忆录讲了他们如何搭便车穿越欧洲。'),sources=S('hitchhiked','hitchhike'))
W('hitchhiking','/ˈhɪtʃhaɪkɪŋ/','搭便车旅行；正在沿路搭车',
 '一段段借过路车辆走远路，这种出行方式叫 hitchhiking。可以说一次正在进行的行程，也可当作活动名词谈。',
 'hitchhike 去 e 加 -ing；外层变化落在末尾，不把 hitch 和 hike 各自都改一遍。',HITCHHIKE+[['hitchhike + -ing → hitchhiking','沿路搭便车的过程、活动']],
 'go hitchhiking；a hitchhiking trip；hitchhiking across the country。',
 'a story about hitchhiking；was hitchhiking north。',
 'carpooling 常是事先合乘、拼车安排，hitchhiking 常是沿途搭过路车辆；都能同车，组织方式不同。',
 ('The documentary follows two friends hitchhiking across the country.','纪录片跟拍两个朋友搭便车穿越全国。'),('His travel diary contains several stories about hitchhiking.','他的旅行日记里有几个搭便车的故事。'),sources=S('hitchhiking','hitchhike'))
W('hitchhiker','英 /ˈhɪtʃhaɪkə/；美 /ˈhɪtʃhaɪkɚ/','搭便车旅行的人',
 '站在路边等过路车捎一段的人，是 a hitchhiker。词里保留了借车走路程的意思，最外层 -er 指做这事的人。',
 'hitchhike 去 e 加完整 -er；不要只写 -r，完整人称后缀仍是 -er。',HITCHHIKE+[['hitchhike + -er → hitchhiker','沿路搭便车的人']],
 'a hitchhiker by the road；pick up a hitchhiker 捎上搭便车者。',
 'a lone hitchhiker；a hitchhiker carrying a backpack。',
 'hitchhiker 指搭便车者，hiker 指徒步者；同样背着包，前进方式可能不同。',
 ('The story begins with a hitchhiker waiting beside a country road.','故事从一个在乡间路边等车的搭便车者开始。'),('The driver offered the hitchhiker a lift to the next town.','司机愿意捎那位搭便车者到下一个镇。'),sources=S('hitchhiker','hitchhike'))
W('hitchhikers','英 /ˈhɪtʃhaɪkəz/；美 /ˈhɪtʃhaɪkɚz/','搭便车旅行的人〔复数〕',
 '几个人沿路借车旅行，是 hitchhikers。它数的是人，hitchhiking 才是他们做的事。',
 'hitchhiker + -s，读 /z/；先由 hitchhike 去 e 加 -er 表人，再用复数。',HITCHHIKE+[['hitchhike → hitchhiker → hitchhikers','搭便车，到搭车者，再到多人']],
 'two hitchhikers；hitchhikers beside the road；stories told by hitchhikers。',
 'a group of hitchhikers；pick up hitchhikers。',
 'passengers 是所有乘客，hitchhikers 特指搭便车的那类旅行者；乘车的人不一定都是沿路拦车。',
 ('Two hitchhikers stood beside the road with their bags.','两个搭便车者带着包，站在路边。'),('The book collects stories told by hitchhikers.','那本书收集了搭便车旅行者讲述的故事。'),sources=S('hitchhikers','hitchhike'))
W('backpacks','/ˈbækpæks/','背包〔复数〕；背包徒步、旅行〔第三人称单数〕',
 '学生背着的几个包，是 backpacks；他背着装备轻装旅行，也可以说 he backpacks。先认物件，再看它变成旅行方式。',
 'backpack + -s，/k/ 后读 /s/；back 背部 + pack 行囊先成名词，后来有背包旅行动词。',BACKPACK+[['backpack + -s → backpacks','多个背包，或他、她背包旅行']],
 'school backpacks 学生背包；backpacks around the country。',
 'carry heavy backpacks；backpacks through the hills。',
 'backpacks 是背在背上的包，suitcases 通常是手提、拉行的箱子；装东西的功能相同，携带方式不同。',
 ('The students left their backpacks by the door.','学生们把背包放在门边。'),('She backpacks through the hills every summer.','她每年夏天都背着包在山里徒步旅行。'),sources=S('backpacks','backpack'))
W('backpacked','/ˈbækpækt/','背着装备徒步、旅行了',
 '过去背着包走山路、换地方住，来一趟相对轻装的旅行，可以说 backpacked。重点是旅行方式，不只碰巧拎了一个包。',
 'backpack + 完整 -ed，/k/ 后读 /t/；词尾已有 ck，不再加一个 k。',BACKPACK+[['backpack + -ed → backpacked','过去背包徒步、旅行']],
 'backpacked across Europe；backpacked through the mountains。',
 'backpacked for a month；had backpacked there before。',
 'backpacked 是以背包方式旅行，packed a backpack 只是把包收拾好；准备行囊和已经出行不同。',
 ('We backpacked through the mountains for a week.','我们背着包在山里徒步旅行了一周。'),('She backpacked around Europe after graduation.','毕业后，她背包游历了欧洲。'),sources=S('backpacked','backpack'))
W('backpackers','英 /ˈbækpækəz/；美 /ˈbækpækɚz/','背包旅行者、背包徒步者〔复数〕',
 '把主要行李背在身上，一站站走、一处处住的旅行者，常叫 backpackers。它可能是山野徒步，也可能是轻装跨城旅行。',
 'backpacker + -s，读 /z/；backpack 加完整 -er 成人称名词，再加复数。',BACKPACK+[['backpack → backpacker → backpackers','背包旅行动作，到旅行者，再到多人']],
 'a hostel for backpackers 背包客旅舍；experienced backpackers。',
 'backpackers on the trail；a group of backpackers。',
 'backpackers 不必都是 hitchhikers；背包说行李、旅行方式，搭便车说某段路怎么乘车。',
 ('The hostel is popular with backpackers.','那家旅舍很受背包客欢迎。'),('The backpackers carried enough food for three days.','背包徒步者们带了够吃三天的食物。'),sources=S('backpackers','backpack'))
W('straggle','/ˈstræɡəl/','走散、掉在后面；零零散散地延伸',
 '队伍往前走，有人慢慢落到后面、离开整队，是 straggle。几间房子沿路零散排开，也像没聚拢的一队。',
 '接日耳曼行进材料，具体近源未定，有北欧或旧英语动作词反复派生等分析。不是现代 struggle 挣扎换一个元音造出来。',STRAGGLE,
 'straggle behind 掉队、落在后面；houses straggle along the road。',
 'straggle into camp 零零散散来到营地；straggle across the hillside。',
 'struggle 强调费劲挣扎，straggle 强调分散、掉队；一个人可在努力跟上，也可因闲聊而落后。',
 ('Try not to straggle behind the group.','尽量别落在队伍后面。'),('A few houses straggle along the hillside.','几幢房子零零散散分布在山坡上。'),sources=S('straggle','straggle'))
W('straggles','/ˈstræɡəlz/','落在后面、走散；零散延伸〔第三人称单数〕',
 '每次集合他都比别人晚一截，是 straggles behind；一排篱笆疏疏落落伸过去，也能说 straggles。',
 'straggle + -s，读 /z/；基础动词接旧行进材料，现代加三单，不因词形近就混成 struggle。',STRAGGLE+[['straggle + -s → straggles','他或它落后、走散，或零散延伸']],
 'straggles behind the others；a hedge straggles along the path。',
 'straggles into camp；straggles down the hill。',
 'straggles 不一定是迷路，gets lost 才说失去路线；还看得见队伍，也可能落在后面。',
 ('He often straggles behind the rest of the group.','他常常落在队伍其他人后面。'),('An untidy hedge straggles along the path.','一道不整齐的篱笆沿小路稀稀落落地伸展。'),sources=S('straggles','straggle'))
W('straggled','/ˈstræɡəld/','走散、掉队了；零零散散地延伸、到达了',
 '大家没一起到，而是一小拨一小拨慢慢进来，可以说 straggled in。散乱是重点，不必每个人都不知道去哪里。',
 'straggle 去 e 加完整 -ed，读 /d/；保留词干原有双 g，不额外再加。',STRAGGLE+[['straggle + -ed → straggled','过去分散、落后，或零零散散到达']],
 'straggled into the room；straggled behind；straggled along the road。',
 'straggled back to camp；houses straggled across the slope。',
 'straggled in 是零零散散、可能迟缓地进来，marched in 更像齐整、果断地进；场面组织不同。',
 ('The walkers straggled back to camp before dark.','步行的人们在天黑前零零散散回到营地。'),('The last few guests straggled in after dinner had begun.','晚饭开始后，最后几位客人才陆陆续续进来。'),sources=S('straggled','straggle'))
W('straggling','/ˈstræɡəlɪŋ/','正在走散、掉队；零散、杂乱延伸的',
 '走路的人被拉成松松的一线，是 straggling；头发、枝条杂乱向外伸，也可用这张散开的画面。',
 'straggle 去 e 加 -ing；分词写分散移动，也可形容稀疏、杂乱的排列。',STRAGGLE+[['straggle + -ing → straggling','走散的过程，或不整齐延伸的性质']],
 'a straggling line of walkers；straggling branches 零乱伸出的枝条。',
 'straggling behind；a straggling village 房屋分散的村庄。',
 'straggling 是分散、零乱，straight 是直；一条直路两边的房屋也可能分布得零零散散。',
 ('A straggling line of walkers crossed the field.','步行的人们拉成松散的一线，走过田野。'),('She trimmed the straggling branches.','她修剪了那些零乱伸出的枝条。'),sources=S('straggling','straggle'))
W('straggler','英 /ˈstræɡlə/；美 /ˈstræɡlɚ/','掉队、落后、晚来的人或动物；零散伸出的东西',
 '大伙已经走到前面，还有一个人没跟上，就是 a straggler。也可说最后才来的人，植物里则可能是一根多伸出的零乱枝条。',
 'straggle 去 e 加完整 -er；后缀常指做事者，现代也能指散出来、伸出来的东西。',STRAGGLE+[['straggle + -er → straggler','落在后面、偏离整队的人或动物等']],
 'wait for a straggler；the last straggler；a straggler from the flock。',
 'a lone straggler；round up a straggler 找回掉队者。',
 'straggler 是队伍或一组中的落后者，loner 常指习惯独处的人；暂时没跟上不等于喜欢独来独往。',
 ('The guide waited for the last straggler.','导游等着最后那个掉队的人。'),('A straggler from the flock stood near the gate.','羊群里一只掉队的羊站在门边。'),sources=S('straggler','straggle'))
W('stragglers','英 /ˈstræɡləz/；美 /ˈstræɡlɚz/','掉队、落后、晚来的人或动物〔复数〕',
 '前面的人都到了，后面还陆陆续续有人来，这些人可叫 stragglers。强调相对整队、整组落后，不必是永久落后。',
 'straggler + -s，读 /z/；straggle 去 e 加 -er 表个体，再取复数。',STRAGGLE+[['straggle → straggler → stragglers','分散、掉队，到掉队个体，再到复数']],
 'the last few stragglers；wait for stragglers；stragglers from the herd。',
 'round up the stragglers；stragglers arriving late。',
 'stragglers 可能只是走得慢、最后到，losers 才常指输的人；晚一点跟上不表示比赛输了。',
 ('We stopped at the gate to wait for the stragglers.','我们在门边停下，等掉队的人跟上。'),('A few stragglers arrived as the chairs were being put away.','椅子都开始收了，还有几位晚来的人陆续到场。'),sources=S('stragglers','straggle'))
W('wayfarer','英 /ˈweɪfeərə/；美 /ˈweɪˌferɚ/','旅人、行路人〔较文学，常指徒步〕',
 '旧故事里，一个人沿着长路走，天黑投宿，是 a wayfarer。比 traveller 更有在路上、慢慢走来的文学画面。',
 'way 道路 + fare 旧动词行进、旅行，再有 -er 表人。wayfare 动词记录较晚，不能把现代学习先学短动词当成确定历史。',WAYFARER,
 'a weary wayfarer 疲惫的行路人；a lone wayfarer。',
 'shelter for a wayfarer；the wayfarer on the road。',
 'fare 在这里是行进的旧动词，不是票价；wayfarer 不是按是否付车费来划分的旅客。',
 ('A weary wayfarer stopped at the inn.','一位疲惫的行路人在客栈停下。'),('The poem follows a lone wayfarer through the hills.','那首诗跟随一位孤独旅人走过群山。'),sources=S('wayfarer','wayfarer'))
W('wayfarers','英 /ˈweɪfeərəz/；美 /ˈweɪˌferɚz/','旅人、行路人〔复数，较文学〕',
 '几个人沿路长途行进，故事里可写 wayfarers。它自带一点旧时旅途、在路上讨生活或找落脚处的画面。',
 'wayfarer + -s，读 /z/；内部仍是 way、fare 行进与人称 -er，不把复数当成购买多张车票。',WAYFARER+[['wayfarer + -s → wayfarers','多个旅人、行路人']],
 'weary wayfarers 疲惫的行路人；shelter for wayfarers。',
 'wayfarers along the road；a group of wayfarers。',
 'wayfarers 较文学，travellers 更普通；是否走路也要结合上下文，不能把文学词机械当作精确交通分类。',
 ('The inn offered food and shelter to wayfarers.','客栈为过路旅人提供食宿。'),('The painting shows wayfarers resting beside a stream.','画里是几位旅人在溪边歇脚。'),sources=S('wayfarers','wayfarer'))
W('wanderers','英 /ˈwɒndərəz/；美 /ˈwɑndərɚz/','漫游、漂泊、四处游走的人或动物〔复数〕',
 '没有长期固定在一处，走过一个地方又去另一个地方的人，是 wanderers。它可以有自由感，也可以有漂泊、无归处的感觉。',
 'wanderer + -s，读 /z/；wander 加完整 -er 成做漫游动作的人，再取复数。基础词承古英语 wandrian 等材料。',
 [['古英语 wandrian 等 → wander 四处游走','不是 wonder 惊奇的现代派生'],['wander + -er → wanderer；再加 -s','漫游动作，到漫游者，再到多人']],
 'restless wanderers 不肯久留的漫游者；wanderers far from home。',
 'a group of wanderers；nomads and wanderers。',
 'wanderers 不一定是 lost people 迷路者；有人知道自己在哪，只是没有固定目的地或住所。',
 ('The novel follows a group of wanderers searching for a place to settle.','小说写了一群漂泊者寻找落脚之地的经历。'),('The island has long attracted artists and restless wanderers.','那座岛长期吸引着艺术家和不愿久留一处的漫游者。'),sources=S('wanderers','wander'))
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_zhs',ROOTS,WORDS)
 extend_lessons()
