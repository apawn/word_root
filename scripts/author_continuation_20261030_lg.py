"""Pig, runner, socialistic, bark and stack."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
P=[['古英语相关词形 → 中古英语 pigge','原先主要说小猪；更远来源不确定'],['pig 泛指猪','不再限于幼龄；也产生形象、材料等扩展'],['pig + -y、-let、skin','昵称、幼崽、猪皮；piggyback 另有改形历史']]
W('pig','/pɪɡ/','猪；〔pig out〕大吃一顿',
 '农场里那种长鼻拱地的动物是 pig。这个词原先偏小猪，后来长大了也能叫 pig；pig out 则借贪吃的刻板形象说放开吃一顿。',
 '中古英语 pigge，上接古英语相关词形，更早来源不确定。不要按今天的拼写任意拆出 p- 或 -ig。',P[:2],
 'a farm pig 农场里的猪，feed the pigs 喂猪，pig out on snacks 放开吃零食。用 pig 骂人会带贪婪、邋遢等侮辱意味。',
 'feed the pigs；pig out on。',
 'pig 说动物，pork 日常说猪肉。guinea pig 是豚鼠这个固定动物名，不是普通小猪。',
 ('The pigs were sleeping in the shade.','猪在阴凉处睡觉。'),('We pigged out on pizza after the long walk.','走了很长的路后，我们放开吃了一顿比萨。'),sources=['https://en.wiktionary.org/wiki/pig#English','https://www.etymonline.com/word/pig'])
W('piggy','/ˈpɪɡi/','小猪〔儿语、昵称〕；像猪的',
 '孩子把小猪叫 piggy，就像给动物加上一个亲昵的小尾巴。形容词用法也能说猪的样子，或带贬义说贪吃、邋遢。',
 'pig + -y；名词里 -y 是亲昵、小称后缀，形容词里 -y 表像猪的性质。都双写 g，但用法有别。',P[:2]+[['pig + -y → piggy','亲昵叫法的小猪；像猪的性质']],
 'a little piggy 一只小猪，a piggy bank 猪形储蓄罐，piggy eyes 常说小眼睛的外观，带评价意味。',
 'a little piggy；a piggy bank。',
 'piggy 作儿语常亲昵，拿来评价真人的外貌、行为可能贬损。piglet 则更直接指幼猪。',
 ('The child drew a pink piggy.','孩子画了一只粉红色小猪。'),('She dropped a coin into her piggy bank.','她往猪形储蓄罐里放了一枚硬币。'))
W('piglet','/ˈpɪɡlət/','小猪、幼猪',
 '不是把成年猪叫可爱一点，而是明确说尚未长大的幼猪。-let 给 pig 加上小、幼的意思。',
 'pig + -let，小称后缀，形成幼猪的名称。这里的 let 不是允许的动词。',P[:2]+[['pig + -let → piglet','幼小的猪']],
 'newborn piglets 新生小猪，a litter of piglets 一窝小猪。可以说真实动物，也可以作故事角色称呼。',
 'newborn piglets；a litter of piglets。',
 'piglet 强调幼龄；piggy 更像儿语昵称，也可以说像猪的性质。',
 ('The sow was followed by six piglets.','母猪后面跟着六只小猪。'),('The farmer checked the newborn piglets.','农场主查看了新生小猪。'))
W('pigskin','/ˈpɪɡskɪn/','猪皮、猪皮革；〔美口语〕美式橄榄球',
 'pig 的 skin 就是猪皮，制成皮革仍叫 pigskin。体育报道中 toss the pigskin 却是在说传橄榄球，这是保留下来的球的俗称。',
 'pig + skin 的复合词。由材料名称转称物件，形成美式橄榄球的俗称；不要凭昵称断定眼前的球一定是猪皮做的。',P[:2]+[['pig + skin → pigskin','猪皮、皮革 → 美式橄榄球俗称']],
 'pigskin leather 猪皮革，pigskin gloves 猪皮手套，throw the pigskin 传美式橄榄球。材料义通常不可数，球的俗称可数。',
 'pigskin leather；throw the pigskin。',
 'pigskin 的球义取决于体育语境；它不是所有足球、所有皮球的通用叫法。',
 ('The gloves are made of soft pigskin.','这副手套用柔软的猪皮革制成。'),('They tossed the pigskin in the park.','他们在公园里互传橄榄球。'),sources=['https://en.wiktionary.org/wiki/pigskin#English','https://www.merriam-webster.com/dictionary/pigskin'])
G=[['pick pack、pickapack 等旧形式','像背包袱一样放在背上、肩上'],['改形为 piggyback','受熟悉词形影响形成现代样子，并非原先就说小猪的背'],['背着 → 附带、借助','人背人；设备、计划依附已有系统']]
W('piggyback','/ˈpɪɡibæk/','背着、骑在背上；附带、借助已有事物',
 '孩子趴在大人背上，是 piggyback；新服务搭在已有系统上运行，也像搭了一个现成的背。',
 '由 pickapack、pickaback 等旧形式改形而来，原来联系背上的包袱。现代外形虽像 piggy + back，却不宜把猪背故事当真实起点。',G,
 'give someone a piggyback ride 背某人走，piggyback on an existing network 借助现有网络，piggyback services 附带服务。',
 'a piggyback ride；piggyback on。',
 'piggyback on 看的是搭载、借助关系，不一定有真实的背；是否合适、是否经许可，要由句子另行说明。',
 ('Her father gave her a piggyback ride home.','爸爸背着她回家。'),('The new service piggybacks on the existing delivery network.','新服务借助现有配送网络运行。'),sources=['https://en.wiktionary.org/wiki/piggyback#English','https://www.etymonline.com/word/piggyback'])
R('B3053','猪及幼崽、皮革、外形联想，另辨 piggyback 的改形','PIG：动物是起点，小称、材料和比喻分开理解','pig → piggy、piglet；pigskin、pigtail；piggyback 单列历史。',
 'pig 原先偏指小猪，后来泛指猪；幼崽可更明确说 piglet。piggyback 虽然外形熟悉，来源却不能硬套进猪这个动物。',
 'pigge → pig；-y 昵称或性质，-let 幼小，skin 皮，tail 尾。piggyback 来自旧背包袱说法的改形。',
 [['动物、小称与材料','pig · piggy · piglet · pigskin · pigtail'],['看似有关，另有历史','piggyback']],
 'pig 动物与 pork 食物常分用；pigskin 可是球的俗称；piggyback 的 piggy 不是可靠的原始动物拆分。',
 'The child carried a toy piggy while riding piggyback.\n\n孩子被背着走，手里抱着一只玩具小猪。','pig piggy piglet pigskin pigtail piggyback')
R('B3680','跑的人或运作角色，再由前项说明身份、位置','RUNNER：先有人在跑，再看前面加了什么','runner → forerunner、showrunner、roadrunner。',
 'forerunner 是走在前面的先驱、前身；showrunner 把节目运作起来；roadrunner 是会在地面奔跑的走鹃。相同后半并不代表它们全是运动员。',
 'run + -er，双写 n；fore 前面，show 节目，road 路，各自形成固定复合义。',
 [['基础人物与扩展角色','runner · forerunner · showrunner'],['复合动物名称','roadrunner']],
 'forerunner 可说事物前身；showrunner 是影视制作角色；roadrunner 是鸟名。',
 'The earlier device was a forerunner of the modern model.\n\n较早那台设备是现代型号的前身。','runner forerunner showrunner roadrunner')
So=[['social 社会的 → socialism、socialist','社会主义及其支持者、相关性质'],['socialist + -ic → socialistic','相关或带相应倾向；也可对应 socialism + -istic']]
W('socialistic','英 /ˌsəʊʃəˈlɪstɪk/；美 /ˌsoʊʃəˈlɪstɪk/','社会主义的、带社会主义倾向的',
 '不是只说人爱社交，而是把某种思想、制度、措施联系到 socialism。socialistic 常突出相关特点或倾向，具体指什么仍要看作者怎样定义。',
 '可按 socialist + -ic 理解，也可对应 socialism 的词干 + -istic；两种分析都联系同一词族的理念、人物、性质。',So,
 'socialistic ideas 带社会主义特点的思想，socialistic policies 相应政策。讨论中这个标签有时带作者立场，读出它所指的具体措施更重要。',
 'socialistic ideas；socialistic policies。',
 'social 是社会相关，sociable 是好交际；socialistic 进入政治经济理念。socialist 本身也可作形容词，两者没有各领域统一的绝对分界。',
 ('The essay examines socialistic ideas in the novel.','文章考察小说中的社会主义思想倾向。'),('Critics described the proposal as socialistic.','批评者把这项提议称为带社会主义倾向的。'),sources=['https://en.wiktionary.org/wiki/socialistic#English','https://www.merriam-webster.com/dictionary/socialistic'])
R('B3523','理念、支持者与相应特点','SOCIALIST：先辨理念、人物，再辨性质用法','socialist → socialistic。',
 'socialist 可说支持者，也能直接作相关形容词；socialistic 常说相应特点、倾向。不要把两个词硬规定为拥护与反对的区别。',
 'social 词族 → socialism、socialist；-ic 或 -istic 形成相关性质表达。',
 [['人物、性质及扩展形容词','socialist · socialistic']],
 'socialistic 不是善于社交；政治标签的具体范围取决于论述中的定义。',
 'The historian compared socialist movements and socialistic proposals.\n\n历史学家比较了社会主义运动和带社会主义倾向的提案。','socialist socialistic')
Ba=[['狗叫支线：古英语 beorcan → bark','突然而响的叫声，也比喻厉声说话'],['树皮支线：古诺尔斯语 börkr 等 → bark','树的外层覆盖物，来源与狗叫不同'],['船支线：法语 barque、晚期拉丁 barca → bark','船；embark 通过法语 embarquer 联系这条船义']]
W('bark','英 /bɑːk/；美 /bɑːrk/','吠、狗叫声；厉声说；树皮；船〔较专门义〕',
 '看到狗，bark 是汪汪叫；看到树，bark 是树皮。它们恰好同形，不是因为树皮像狗叫。还有较专门的船名词，常见另一拼写 barque。',
 '狗叫承古英语 beorcan；树皮借斯堪的纳维亚来源，联系古诺尔斯 börkr；船借法语 barque，联系晚期拉丁 barca。分三条记，不画成一个意义连续演化。',Ba,
 'bark at someone 朝某人叫、厉声说，bark an order 喝令，tree bark 树皮。bark up the wrong tree 比喻找错对象、弄错方向。',
 'bark at；bark an order；tree bark；bark up the wrong tree。',
 '狗叫义也有名词 a bark；树皮常作物质名词 bark。看到 embark，要联想船而非吠叫。',
 ('The dog barked at the passing bicycle.','狗朝经过的自行车叫。'),('The tree has thick, rough bark.','这棵树的树皮又厚又粗糙。'),sources=['https://en.wiktionary.org/wiki/bark#English','https://www.etymonline.com/word/bark'])
W('barking','英 /ˈbɑːkɪŋ/；美 /ˈbɑːrkɪŋ/','吠叫；正在叫的；〔英口语〕疯的、荒唐的',
 'bark 这个动作展开成一阵阵狗叫，就是 barking。the barking dog 说正在叫的狗；英式口语 barking mad 则是夸张说疯了、太荒唐。',
 '狗叫动词 bark + -ing，延续中古英语相应形式。另有树皮加工语境中的 bark 动词，但普通狗叫用法属于声音支线。',Ba[:1]+[['bark + -ing → barking','吠叫活动、相关状态；固定口语中有荒唐义']],
 'constant barking 不停的狗叫，a barking dog 正在叫的狗，barking mad 疯得厉害、荒唐透顶，属非正式表达。',
 'constant barking；a barking dog；barking mad。',
 'barking mad 是口语评价，不是医学诊断；单独 barking 也常只是狗叫的普通分词、名词。',
 ('The barking stopped when the owner came home.','主人回家后，狗叫停了。'),('A barking dog woke the neighbours.','一只狗的叫声吵醒了邻居。'))
W('barker','英 /ˈbɑːkə/；美 /ˈbɑːrkər/','叫吠者；大声招徕顾客的人；剥树皮机〔另源支线〕',
 '狗不停叫，可以是 a barker；游乐场门口大声喊着招客的人，也借响亮叫喊叫 barker。木材厂的同形词则可能是剥树皮机。',
 'bark + -er，但须分来源：招徕者联系狗叫、喊叫的 bark；剥树皮机联系树皮及去皮动作的 bark。相同后缀并没有把两条来源合并。',Ba[:2]+[['bark + -er → barker','喊叫者、招徕者；另一支为剥树皮装置']],
 'a carnival barker 游乐场招徕者，a persistent barker 总爱叫的狗，a log barker 原木剥皮机。先由地点判断身份。',
 'a carnival barker；a log barker。',
 'barker 不只是狗的别称；以人作对象时可说职业招徕者。木材设备的含义不能从声音推断。',
 ('A carnival barker called to the passing crowd.','游乐场招徕者向经过的人群大声吆喝。'),('Their dog is a frequent barker.','他们的狗经常叫。'))
E=[['en- 进入 + 法语 barque 船 → embarquer','把人、货装上船；登船'],['法语 → 英语 embark','登船出发 → 开始旅程或一项事业'],['相应名词与反向动作','embarkation 登乘；disembark 下船、下机等']]
W('embark','英 /ɪmˈbɑːk/；美 /ɪmˈbɑːrk/','登船、登乘；着手、开始',
 '脚踏上船，旅程开始了；把研究、事业也想成一段航程，embark on a project 就是踏上这段新旅程。',
 '借法语 embarquer，en- 进入在 b 前同化为 em-，加 barque 船。对应 bark 的船义，不是狗叫或树皮。',E[:2],
 'embark on a journey 开始旅程，embark on a career 开始职业生涯，embark on a project 着手项目。具体登乘可用 embark at a port 等。',
 'embark on a project；embark on a journey。',
 '抽象开始义常说 embark on，不随意省略 on 直接接 project。这个词较正式，常让开始带有新阶段、长过程的感觉。',
 ('Passengers embarked at the small harbour.','乘客在小港口登船。'),('The team embarked on a new research project.','团队着手一项新的研究项目。'),sources=['https://en.wiktionary.org/wiki/embark#English','https://www.etymonline.com/word/embark'])
W('embarkation','英 /ˌembɑːˈkeɪʃən/；美 /ˌembɑːrˈkeɪʃən/','登船、登乘；人员或货物的装载过程',
 'embark 是登上去，embarkation 把整个登乘、装载过程当成一件事：在哪儿开始，何时完成，都可以围着它说明。',
 '借法语 embarcation，现代可按 embark + -ation 对应动作名词。后缀把登乘动作名词化。',E,
 'an embarkation point 登乘点，an embarkation area 登乘区，before embarkation 登乘前。可用于船，也可用于其他交通、运输场景。',
 'an embarkation point；before embarkation。',
 'embarkation 不是船本身，也不是整段航程；boarding 在普通旅客场景中也很常用。',
 ('Signs directed passengers to the embarkation area.','标志指引乘客前往登乘区。'),('All documents were checked before embarkation.','登乘前检查了所有证件。'))
W('disembark','英 /ˌdɪsɪmˈbɑːk/；美 /ˌdɪsɪmˈbɑːrk/','下船、下机、离开所乘交通工具',
 'embark 是上去出发，disembark 是从所乘船、飞机等下来。镜头从踏上旅程换成到站离开。',
 'dis- 反向、离开 + embark，历史也联系法语 desembarquer。较早中心是从船上下到岸上，后来适用于其他交通工具。',E,
 'disembark from a ship 下船，passengers disembark 乘客下船、下机。可不带宾语，也有直接接交通工具的用法。',
 'disembark from；passengers disembark。',
 'disembark 强调离开所乘交通工具；arrive 是到达，车船到了不代表乘客已经下去。',
 ('We disembarked from the ferry just before noon.','我们快到中午时下了渡轮。'),('Passengers waited for permission to disembark.','乘客等候获准下机。'),sources=['https://en.wiktionary.org/wiki/disembark#English','https://www.etymonline.com/word/disembark'])
R('B3513','同形的狗叫、树皮、船，按真实来源分别学习','BARK：同样四个字母，有三幅不同画面','bark → barking、barker；船义旁接 embark → embarkation、disembark。',
 '狗会叫，树有皮，船可登。把三幅画面并排摆好，比硬找一条神奇的共同意义更容易用对。',
 '声音承 beorcan；树皮联系 börkr；船联系 barque、barca，en- + barque → embarquer → embark。',
 [['狗叫与响亮招徕','bark · barking · barker'],['船与登乘动作','embark · embarkation · disembark']],
 'barker 的剥皮机义属于树皮支线；embark on 开始一项事业；同形不表示同源。',
 'After the passengers disembarked, a dog began barking on the pier.\n\n乘客下船后，码头上有只狗叫了起来。','bark barking barker embark embarkation disembark')
St=[['斯堪的纳维亚词，联系古诺尔斯 stakkr → stack','草垛、堆放成堆的东西'],['名词 → 动词','一摞、一堆 → 堆起来；安排得偏向某方'],['复合与后缀','haystack 草垛；stacked 已堆好或占优；stacker 堆放者、装置；stackable 可堆叠']]
W('stack','/stæk/','摞、堆；堆放；〔计算机〕栈；烟囱等',
 '把盘子一个放在另一个上面，得到 a stack。动词 stack 就是这么堆；计算机的栈也像一摞盘子，最后放上的先拿走。',
 '中古英语 stack 等借自斯堪的纳维亚来源，联系古诺尔斯 stakkr 草垛。由堆的名词生出堆放动作，随后有技术、建筑等固定扩展。',St[:2],
 'a stack of papers 一摞纸，stack the chairs 把椅子叠起，stack the deck 预先做有利于某方的安排。the stacks 在图书馆可说书库、书架区。',
 'a stack of；stack up；stack the deck。',
 'stack 多让人想到上下堆叠，pile 范围更宽；技术栈也可能说一组配合的软件，须区别具体的数据结构义。',
 ('She placed a stack of plates on the counter.','她把一摞盘子放在台面上。'),('Please stack the chairs after the meeting.','会后请把椅子叠起来。'),sources=['https://en.wiktionary.org/wiki/stack#English','https://www.etymonline.com/word/stack'])
W('stacked','/stækt/','叠放好的；经倾向性安排的；阵容强大的',
 '盘子已经堆好，是 stacked；若好牌、高手都被堆到一方，也会说安排偏向那边，或阵容特别强。',
 'stack + -ed，过去分词及形容词。-ed 在 /k/ 后读 /t/，不是额外一整个音节。',St[:2]+[['stack + -ed → stacked','堆好 → 有意安排、优势集中']],
 'stacked chairs 叠放的椅子，the odds are stacked against us 形势很不利于我们，a stacked team 高手云集的队伍。',
 'stacked chairs；the odds are stacked against。',
 'stacked team 可是称赞阵容强；stacked committee 常批评成员安排偏向某方。不是所有 stacked 都意味着不公平。',
 ('The chairs were stacked neatly against the wall.','椅子整齐叠放在墙边。'),('They kept working even though the odds were stacked against them.','尽管形势很不利，他们仍继续努力。'))
W('haystack','/ˈheɪstæk/','干草堆、草垛；难以搜寻的大堆事物',
 'hay 是干草，stack 是堆，放在一起就是草垛。往里面找一根针很难，于是 a needle in a haystack 比喻目标埋在海量事物里。',
 'hay + stack，承中古英语相应复合形式。由真实草垛形成难找东西的比喻，现代也可用到数据搜索场景。',St[:1]+[['hay + stack → haystack','干草堆 → 海量杂物、数据等搜索背景']],
 'a haystack in a field 田里的草垛，look for a needle in a haystack 像在草垛里找针。中文常对应大海捞针，不必逐字硬译。',
 'a needle in a haystack；search the haystack。',
 'haystack 不是一根稻草，hay 也不自动等于 straw 秸秆；此处先抓储存干草的大堆。',
 ('A haystack stood beside the old barn.','旧谷仓旁有一座草垛。'),('Finding that receipt was like looking for a needle in a haystack.','找那张收据简直像大海捞针。'))
W('stacker','英 /ˈstækə/；美 /ˈstækər/','堆放者、码放工；堆垛机、叠放装置',
 'stack 是堆，stacker 就是干这件事的人或机器。超市里往货架码货的人、仓库里堆货的设备，都可能这样命名。',
 'stack + -er，施事或工具后缀；不因机器义就另造一个词根。',St[:1]+[['stack + -er → stacker','负责堆放的人、装置']],
 'a shelf stacker 货架理货员，a pallet stacker 托盘堆垛设备，an automatic stacker 自动叠放装置。前项通常告诉你在堆什么。',
 'a shelf stacker；a pallet stacker。',
 'stacker 不只指某一种叉车；设备名称的具体功能看场景，-er 也不一定都是人。',
 ('She worked as a shelf stacker during the summer.','夏天她做货架理货员。'),('The machine feeds sheets into an automatic stacker.','机器把纸张送入自动叠放装置。'))
W('stackable','/ˈstækəbəl/','可堆叠的；〔部分场景〕可叠加使用的',
 '椅子形状设计得能一把套一把叠起，就 stackable。优惠、功能也可能像层层叠加一样共同使用。',
 'stack + -able，形成能够被堆叠的性质；再由物理堆叠扩成可组合、累计的用法。',St[:1]+[['stack + -able → stackable','可堆叠 → 可共同叠加使用']],
 'stackable chairs 可叠放的椅子，stackable containers 可堆叠容器，stackable discounts 可叠加优惠，是否真能叠加以相应规则为准。',
 'stackable chairs；stackable containers。',
 'stacked 是已经堆好，stackable 是能够这样堆；能堆并不表示此刻已堆。',
 ('The hall uses stackable chairs to save space.','大厅使用可叠放椅子来节省空间。'),('These stackable containers fit neatly in the cupboard.','这些可堆叠容器能整齐收进橱柜。'))
R('B4093','草垛、堆放，扩成上下叠加或优势集中','STACK：一件放在一件上面，再看叠的是东西还是优势','stack → stacked、stacker、stackable；haystack、smokestack。',
 '先用盘子叠起来记住动作，再看后缀：已经叠好、负责叠、可以叠。烟囱是固定历史扩展，技术栈也有专门定义。',
 'stakkr → stack；-ed 状态，-er 人或工具，-able 能力；hay 干草，smoke 烟。',
 [['基础动作与后缀','stack · stacked · stacker · stackable'],['物体、设施与比喻','haystack · smokestack']],
 'stacked 与 stackable 分开；a needle in a haystack 是极难找；stacked 的不公平义须看场景。',
 'The stacker arranged the stackable trays into a tall stack.\n\n叠放装置把可堆叠托盘码成了高高一摞。','stack stacked stacker stackable haystack smokestack')
if __name__=='__main__':save('continuation_20261030_lg',ROOTS,WORDS)
