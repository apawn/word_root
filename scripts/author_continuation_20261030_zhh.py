"""Rake, glean, stash, reap and hoard: different kinds of collecting."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
def S(word,base):
 return ['https://en.wiktionary.org/wiki/'+word+'#English','https://www.etymonline.com/word/'+base]
EXISTING_ROOT_ADDITIONS={
 'A1760':dict(words='rake rakes raked raking glean gleans gleaned gleaning'.split(),label='rake、glean：耙拢与一点点搜集',note='耙子 rake 接古英语名词，动词近源有名词转用、较早动词或北欧材料等分析；浪荡者 rake 另由 rakehell 缩短。glean 经法语、晚期拉丁收集材料，远源未定；英语早有抽象用法，不能说英语先拾麦再学会搜信息。'),
 'A1741':dict(words='stash stashes stashed stashing hoard hoards hoarded hoarder hoarders'.split(),label='stash 与 hoard：藏起一份、积存不放',note='stash 远源未定，可能受 stow、cache 启发，不能定成已证实混成。hoard 接古英语藏存物、珍藏材料，hoarder 早还有财物保管者的人物义，现代储囤者不能只讲成新造。'),
 'A1697':dict(words='reap reaps reaped reaping reaper reapers'.split(),label='reap：收割庄稼与收获结果',note='reap 接古英语收割动词，比较 ripe 成熟；收获行为结果的比喻在英语很早已有。reaper 可说收割者、收割机，人物、工具尾 -er 同形而对象不同。'),
}
RAKE=[['古英语 raca、ræce → rake 耙子','拉拢、刮拢用的齿状工具'],['rake 动词近源有多种分析；浪荡者名词另线','现代可耙拢、搜查；rake in 大量获得']]
GLEAN=[['法语 glener ← 晚期拉丁 glennare 收集 → glean','远源未定'],['英语抽象搜集用法记录早于拾收剩余谷物义','田间拾穗画面有助记忆，不等于英语记录的先后']]
STASH=[['较早英语俚语 stash：藏起','远源未定，或受 stow、cache 等启发'],['动词 → 藏物、私藏存货的名词','现代普通物品也可用，不必总有违法含义']]
REAP=[['古英语 repan、reopan 等 → reap','收割，和 ripe 的旧成熟材料可比较'],['英语早有收获行为结果的比喻','现代 reaps、reaped、reaping；reapers 可指人、机器']]
HOARD=[['古英语 hord 藏存物、hordian 积存 → hoard','藏起来保存、留待以后用'],['hoarder 早有保管财物者，后有积存者、囤物者义','现代逐词看对象、评价，不由称呼直接下判断']]
W('rake','/reɪk/','耙子；用耙耙拢；彻底搜查；〔另线〕浪荡者',
 '一排齿把落叶往自己方向拉，叶子聚成堆，工具和动作都叫 rake。rake in money 则把钱像落叶一样一堆堆耙进来，是赚得多的画面。',
 '工具名接古英语 raca、ræce；动词有名词转用、失传旧动词、北欧相关材料等分析。浪荡者 rake 另由 rakehell 缩短，不从园艺工具硬推。',RAKE,
 'rake leaves 耙落叶；a garden rake 园艺耙；rake in profits 大量获利。',
 'rake through the files 彻底翻查文件；rake over the past 翻旧账。',
 'rake 常有齿状刮拢的动作感，sweep 常用扫帚扫；两者都能清叶子，工具与运动方式不同。',
 ('Use a rake to gather the leaves into a pile.','用耙子把落叶拢成一堆。'),('The successful show continues to rake in money.','那场成功的演出仍在赚大钱。'),sources=S('rake','rake'))
W('rakes','/reɪks/','耙子〔复数〕；耙拢、搜查、大量获得〔第三人称单数〕',
 '棚里几把长柄齿耙，是 rakes；一个人一拉一拉把落叶拢起来，动词也用 rakes。到赚钱场景里，常配 in。',
 'rake + -s，/k/ 后读 /s/；工具名词复数、动词三单同形，另一浪荡者人物名的复数也同形，须看对象。',RAKE+[['rake + -s → rakes','多个耙子，或它耙拢、翻查、赚入']],
 'garden rakes 园艺耙；rakes the leaves 耙落叶；rakes in money 赚进大钱。',
 'rakes through documents；rakes leaves into a pile。',
 'rakes in revenue 强调赚得多、收入不断进来，earns revenue 更中性；词本身不保证扣完费用后净利润多少。',
 ('Several rakes and shovels stood in the shed.','几把耙子和铲子立在棚里。'),('He rakes the leaves into a pile beside the fence.','他把落叶耙成一堆，放在篱笆旁。'),sources=S('rakes','rake'))
W('raked','/reɪkt/','耙拢、耙过、翻查了；〔raked in〕大量赚得了',
 '院子里落叶被拉成几堆，过去用耙做了这件事，就是 raked；报告里 raked through the records 则是像耙过地面一样彻底翻查。',
 'rake 去 e 加完整 -ed，/k/ 后读 /t/。动词各现代用法加同样词尾，不把词尾 k 改成别的基底。',RAKE+[['rake + -ed → raked','过去耙拢、搜查或大量获得']],
 'raked leaves 耙了落叶；raked in money 赚了大钱；raked through records 翻查记录。',
 'raked the soil smooth 把土耙平；raked into a heap。',
 'raked the soil 侧重耙动、平整表层，dug the soil 侧重挖开土；并非同一个园艺动作。',
 ('We raked the fallen leaves into two large piles.','我们把落叶耙成两大堆。'),('She raked through the files looking for the missing receipt.','她仔细翻查文件，寻找那张不见的收据。'),sources=S('raked','rake'))
W('raking','/ˈreɪkɪŋ/','正在耙拢、搜查；〔raking in〕大量赚入',
 '耙齿一遍遍拖过草地，把散叶拢起来，是 raking；一遍遍翻动过去的事情，raking over the past 就有翻旧账的感觉。',
 'rake 去 e 加 -ing；动作形式可说当前过程，也作活动名词谈耙地、翻查等。',RAKE+[['rake + -ing → raking','耙拢、搜查、大量赚入的过程']],
 'raking leaves 耙落叶；raking in profits 大量获利；raking over old arguments 翻旧争执。',
 'spent the morning raking；raking through drawers 翻查抽屉。',
 'raking over the past 常带反复翻旧事的评价，reviewing the past 更中性；是否值得回顾，单词本身并不替人决定。',
 ('He spent the morning raking leaves in the garden.','他一上午都在花园耙落叶。'),('There is little point in raking over the same old argument.','反复翻同一场旧争执没多大意义。'),sources=S('raking','rake'))
W('glean','/ɡliːn/','一点点搜集、获取；拾收割后剩下的谷物',
 '一篇旧信里找到一个线索，另一份记录里又找到一点，把零碎有用的东西拾起来，是 glean。田里收割后拾剩穗，也用这个词。',
 '经古法语 glener 接晚期拉丁 glennare 收集，远源未定。英语抽象搜集义的记录早于字面拾穗义；可以借拾穗画面理解，但别把英语历史顺序讲反。',GLEAN,
 'glean information from a report 从报告中获取零星信息；glean clues 从零碎材料找线索。',
 'glean what you can 尽可能搜集有用内容；glean grain 拾穗。',
 'glean 常像从散落、有限材料里一点点取得，collect 更泛；不是把整篇信息不加筛选地复制过来。',
 ('We tried to glean useful information from the old letters.','我们试着从旧信里一点点获取有用信息。'),('The villagers would glean grain left behind after the harvest.','村民们会拾收割后留在田里的谷物。'),sources=S('glean','glean'))
W('gleans','/ɡliːnz/','一点点搜集、获取；拾穗〔第三人称单数〕',
 '他翻一份份旧档案，从每份里拾一点有用信息，叫 gleans information。它不像整桶拿走，更像把有价值的碎片捡出来。',
 'glean + -s，/n/ 后读 /z/；基础词的英语抽象用法很早，现代三单依普通规则形成。',GLEAN+[['glean + -s → gleans','他或她一点点获取、拾集']],
 'gleans information from sources 从资料中搜集信息；gleans clues 获取线索。',
 'gleans insights from interviews；gleans facts from records。',
 'gleans insights 常有从材料中发现、提取理解的感觉，receives a report 只是收到报告；获得理解和收到文件不同。',
 ('She gleans clues from old photographs and letters.','她从旧照片、旧信里搜集线索。'),('The researcher gleans useful details from brief interviews.','研究者从简短访谈中提取有用细节。'),sources=S('gleans','glean'))
W('gleaned','/ɡliːnd/','一点点获取、搜集到了；拾集了',
 '材料很少，东拼一点、西找一点，最后获得的信息，可以说 information gleaned from…。它让人感到信息是从原材料中挑出来的。',
 'glean + 完整 -ed，/n/ 后读 /d/；可作过去式、分词，常接 from 说明信息来源。',GLEAN+[['glean + -ed → gleaned','过去搜集、获取，或已从材料中取得']],
 'information gleaned from interviews 从访谈获取的信息；gleaned a few facts 得到几个事实。',
 'gleaned from records；gleaned over many years 多年积累搜集到。',
 'gleaned information 只说明怎样取得信息，不保证内容已证实；verified information 才明确经过核实。',
 ('Much of what we know was gleaned from local records.','我们知道的很多内容，都来自对当地记录的搜集。'),('She gleaned a few useful facts from the conversation.','她从交谈中获取了几个有用事实。'),sources=S('gleaned','glean'))
W('gleaning','/ˈɡliːnɪŋ/','正在拾集、搜集；拾穗、零星获取的活动',
 '在成堆材料里耐心找出零散线索，是 gleaning；在收割过的田里拾剩下的谷物，也叫 gleaning。两种都像不放过有用碎片。',
 'glean + -ing，活动名词在中古英语已有；抽象搜集、字面拾穗不是必须在现代英语里按这个顺序新造出来。',GLEAN+[['glean + -ing → gleaning','零星获取、拾穗的过程或活动']],
 'gleaning information 搜集信息；gleaning after the harvest 收割后拾穗。',
 'gleaning clues from archives；the practice of gleaning。',
 'gleaning 常强调取得有用零碎，harvesting 常是整批收割；二者在农作场景中的工作阶段不同。',
 ('She spent weeks gleaning clues from the archives.','她花了几周从档案中搜集线索。'),('The painting shows people gleaning in a harvested field.','那幅画画的是人们在已收割的田里拾穗。'),sources=S('gleaning','glean'))
W('stash','/stæʃ/','藏起、存放；私藏的一份、储备',
 '留一包饼干在抽屉深处，想吃时再拿，这包私下存着的东西是 a stash，把它藏好是 stash it away。可以很日常，不必有犯罪情节。',
 '较早是藏匿俚语，来源未定，可能受 stow、cache 启发，但不能当作已证实的两词混成。名词后来由动词发展。',STASH,
 'stash something away 把东西藏好、存起；a stash of snacks 一份私藏零食。',
 'stash money in a drawer 把钱藏在抽屉；a secret stash 秘藏物。',
 'stash 常有放到不显眼处、留作私用的感觉，store 更中性；stash snacks 不代表零食是非法的。',
 ('I keep a stash of biscuits in my desk.','我在书桌里藏了一份饼干。'),('You can stash your bag under the seat for now.','你可以先把包塞到座位下面。'),sources=S('stash','stash'))
W('stashes','/ˈstæʃɪz/','藏起、存放〔第三人称单数〕；私藏储备〔复数〕',
 '他把零钱藏进旧盒子，是 he stashes it；几处各放一点应急零食，是 several stashes。动作和藏起来的一份东西同形。',
 'stash + -es，/ʃ/ 后读 /ɪz/，多一个音节；动词三单和名词复数同形。',STASH+[['stash + -es → stashes','他藏放；多份私藏物、储备']],
 'stashes money away 藏钱存起；secret stashes 几份秘藏储备。',
 'stashes snacks in a drawer；stashes of supplies 各处储备。',
 'stashes 名词常是一份份存着的物品，hiding places 是藏东西的位置；一个说物，一个说地方。',
 ('He stashes spare change in an old tin.','他把零钱藏在一个旧铁盒里。'),('We found little stashes of sweets in several drawers.','我们在几个抽屉里找到一份份私藏的糖果。'),sources=S('stashes','stash'))
W('stashed','/stæʃt/','藏起、塞好、存放了',
 '出门前把备用钥匙放到不显眼的地方，或把外套暂塞到座位下面，过去做了就是 stashed。常有收在一旁、留着再拿的感觉。',
 'stash + 完整 -ed，/ʃ/ 后读 /t/；没有新增音节。动词远源未定，现代过去式构词清楚。',STASH+[['stash + -ed → stashed','过去藏起、放在一处留用']],
 'stashed away 藏好、存起；stashed in a drawer 藏在抽屉里。',
 'stashed under the seat；had stashed some money away。',
 'stashed 常有特意收进不显眼位置的感觉，left 只说留下、放在某处；是不是隐蔽，后者不说明。',
 ('She stashed a spare key behind the plant pot.','她把一把备用钥匙藏在花盆后面。'),('We stashed our jackets under the seats.','我们把外套塞在座位下面。'),sources=S('stashed','stash'))
W('stashing','/ˈstæʃɪŋ/','正在藏起、收存',
 '把零钱一把把存到盒子里，或把备用物资藏在一旁留用，过程就是 stashing。它常比普通放下多一点藏存的用意。',
 'stash + -ing；现代动作形式。来源虽未全定，不能因此不拆这一层明确的 -ing。',STASH+[['stash + -ing → stashing','把东西藏存、放到一旁的过程']],
 'stashing money away 藏钱存起；stashing supplies 储藏物资。',
 'stashing snacks in a bag；stashing a coat under a seat。',
 'stashing 关注把东西放好、藏存，hoarding 更容易突出不断积存、舍不得用或不愿分出；不是每次存放都叫囤积。',
 ('He was stashing coins in a jar for the trip.','他正把硬币存进罐子，为旅行攒钱。'),('She had a habit of stashing snacks in every bag.','她习惯在每个包里藏点零食。'),sources=S('stashing','stash'))
W('reaps','/riːps/','收割；收获、得到相应结果〔第三人称单数〕',
 '庄稼长好了，把它收回来，是 reaps；前面做的事情，后来得到好处或承受后果，也像收获一样。结果未必都是奖励。',
 'reap + -s，/p/ 后读 /s/；reap 接古英语收割动词，抽象收获义在英语很早已有，不是现代才从农田借来。',REAP+[['reap + -s → reaps','他或它收割、收获相应结果']],
 'reaps the benefits 获得好处；reaps rewards 收获回报；reaps what he sows 自食其果、种什么得什么。',
 'reaps a harvest 收获庄稼；reaps the results。',
 'reaps benefits 强调得到前面行为带来的好处，receives a gift 只是收到礼物；前因后果的感觉不同。',
 ('The company reaps the benefits of years of research.','公司收获了多年研究带来的好处。'),('In the story, he finally reaps what he has sown.','故事里，他最终自食其果。'),sources=S('reaps','reap'))
W('reaped','/riːpt/','收割、收获了；得到相应结果了',
 '多年努力后终于得回报，叫 reaped the rewards；田里谷物收下来了，也叫 reaped。把先前投入与后来所得联系起来就好记。',
 'reap + 完整 -ed，/p/ 后读 /t/；过去式、过去分词。抽象、字面收割的旧用法都保留到现代。',REAP+[['reap + -ed → reaped','过去收割、收获或得到结果']],
 'reaped the rewards 收获回报；reaped a good harvest 收成好。',
 'reaped benefits from 从……得到好处；reaped the consequences 承受后果。',
 'reaped rewards 常对应此前努力，won a prize 只明确赢得奖；回报不一定是颁发的奖品。',
 ('After years of training, she reaped the rewards.','经过多年训练，她收获了回报。'),('The farmers reaped a good harvest that year.','那一年，农民获得了好收成。'),sources=S('reaped','reap'))
W('reaping','/ˈriːpɪŋ/','正在收割；收获、承受相应结果',
 '现在拿到从前努力带来的好处，是 reaping the benefits；若之前的选择不好，也可能正在承受后果。它把时间拉出前后呼应。',
 'reap + -ing；过程形式或活动名词。可对应字面收割、抽象收获，历史上抽象用法并非很晚的新奇比喻。',REAP+[['reap + -ing → reaping','收割、得到相应结果的过程']],
 'reaping benefits 收获好处；reaping rewards 收获回报。',
 'reaping the harvest 收割庄稼；a reaping machine 收割机。',
 'reaping 是收割、收获结果，sowing 是播种；比喻里也常用它们把先前做事与后来结果串起来。',
 ('The town is reaping the benefits of its new railway link.','小镇正在收获新铁路连接带来的好处。'),('The painting shows workers reaping wheat.','画中是工人在收割小麦。'),sources=S('reaping','reap'))
W('reapers','英 /ˈriːpəz/；美 /ˈriːpɚz/','收割者；收割机〔复数〕',
 '镰刀一挥挥，把庄稼割下来的人，是 reapers；把相应工作交给机器，也可以把机器叫 reapers。-er 指能做这动作的人或工具。',
 'reaper + -s，读 /z/；人物词接旧 reap、较早对应人物材料，机器义后来发展，现代可对应 reap + -er 认形。',REAP+[['reap + -er → reaper → reapers','收割者、收割机及其复数']],
 'reapers in the field 田间收割者；mechanical reapers 机械收割机。',
 'a line of reapers；early reapers 早期收割机，按设备语境认。',
 'reapers 收割主要庄稼，gleaners 拾收割后留下的穗；工作阶段、获取方式不同。',
 ('The reapers worked across the field in a long line.','收割者排成长队，在田里作业。'),('The museum displayed early mechanical reapers.','博物馆展出了早期机械收割机。'),sources=S('reapers','reap'))
W('hoards','英 /hɔːdz/；美 /hɔrdz/','囤积、积存〔第三人称单数〕；藏存物、宝藏〔复数〕',
 '东西已经很多，还不断攒着不拿出来，是 hoards；考古挖到几批藏在一起的硬币，也可叫 hoards。后者不自动批评古人囤物。',
 'hoard + -s，读 /z/；动词三单、名词复数同形，基础词接古英语 hord 藏存物及对应积存动词。',HOARD+[['hoard + -s → hoards','他积存；多批藏存物、宝藏']],
 'hoards supplies 囤积物资；coin hoards 藏存的一批批钱币。',
 'hoards old magazines 存着旧杂志不放；ancient hoards 古代藏存物。',
 'hoards coins 可以说积存钱币的动作，coin hoards 是一批批藏存的钱币；词序会改变整组意思。',
 ('He hoards old magazines instead of throwing them away.','他攒着旧杂志，不肯扔掉。'),('The museum has several ancient coin hoards on display.','博物馆展出了几批古代藏存钱币。'),sources=S('hoards','hoard'))
W('hoarded','英 /ˈhɔːdɪd/；美 /ˈhɔrdɪd/','囤积、藏存了；被积存的',
 '把纸、食物等不断往储藏室放，后来成了一大堆，过去做过这件事，就是 hoarded。是否带批评，要看积存是否过量、是否不肯拿出来。',
 'hoard + 完整 -ed，/d/ 后读 /ɪd/，增加音节；过去式、过去分词。',HOARD+[['hoard + -ed → hoarded','过去积存、囤起，或被这样保存']],
 'hoarded supplies 囤起的物资；hoarded wealth 积存的财富。',
 'hoarded in a cupboard 存在柜里；hoarded for years 积存多年。',
 'hoarded 常比 stored 更突出积攒、留着不放，stored 只中性说储存；同一箱东西可从不同态度描写。',
 ('They had hoarded enough firewood to fill the shed.','他们积存的柴火足以装满棚子。'),('The room was crowded with things he had hoarded for years.','房间里挤满他多年攒下的东西。'),sources=S('hoarded','hoard'))
W('hoarder','英 /ˈhɔːdə/；美 /ˈhɔrdɚ/','爱积存东西的人；囤积者',
 '用不上也舍不得丢，东西越堆越多，日常可以称这样的人 a hoarder。这个词常带评价，也可轻松自嘲，语气要结合说话场景。',
 '现代可对应 hoard + -er；古英语 hordere 已有财物保管者、司库义，后来才有普通积存者及更强负面用法。',HOARD+[['hoard 与旧人物材料 → hoarder','现代积存者、囤物者；较早人物义不只负面']],
 'a hoarder of books 攒书不放的人；a compulsive hoarder 强迫性囤物者。',
 'a lifelong hoarder 长年爱存东西的人；a bit of a hoarder 有点爱攒东西的人。',
 'hoarder 强调存着不放、常有过量感，collector 常有主动选择某类藏品的意思；不能只看物品多就完全等同。',
 ('I am a bit of a hoarder when it comes to old notebooks.','说到旧笔记本，我有点舍不得丢。'),('The character is a hoarder who keeps every letter he receives.','那个角色爱存东西，收到的每封信都留着。'),sources=S('hoarder','hoard'))
W('hoarders','英 /ˈhɔːdəz/；美 /ˈhɔrdɚz/','积存者、囤物者〔复数〕',
 '有些人存报纸，有些人攒空盒，留着不放、越堆越多，文章可以把他们叫 hoarders。称呼说的是积存习惯，具体程度还要看描述。',
 'hoarder + -s，读 /z/；人物词较早已有保管财物义，现代词义、评价不能只靠 -er 机械断定。',HOARD+[['hoarder + -s → hoarders','多位爱积存、囤起东西的人']],
 'hoarders of information 把信息攥在手里不分享的人；hoarders of old papers 攒旧纸不放的人。',
 'people described as hoarders；a group of hoarders。',
 'hoarders 是积存的人，hoards 是一批批积存物；有无 -er 改变了指人的角色层。',
 ('The article described people who had become hoarders of old newspapers.','文章描写了一些把旧报纸越攒越多、不舍得丢的人。'),('The essay criticised managers who acted as hoarders of information.','文章批评了那些把信息攥在手里不分享的经理。'),sources=S('hoarders','hoard'))
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_zhh',ROOTS,WORDS)
 extend_lessons()
