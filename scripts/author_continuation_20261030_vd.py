"""Carried goods, crossings, combined parts and the arm family."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'B2669':dict(words=['car','carry','cargo'],label='cargo：车载、装载材料中的货物',note='cargo 经西班牙语 cargar 装载相关名词接拉丁 carricare 装车，与 car、carry 共享更早车辆材料。'),
 'C1535':dict(words=['transit','transition'],label='transit：走过去、正在运送途中',note='拉丁 transire 由 trans 跨过与 ire 去组成，相应 transitus 借为 transit；公共交通是后来的领域义。'),
 'C1097':dict(words=['compose','compound'],label='compound：放在一起，及另源院落词',note='compound 合成、混合线接拉丁 componere 放在一起，含 com- 与 ponere；院落义另经马来语 kampong 相关借入形式受同形词影响，不强并。'),
 'B3166':dict(words=['suit','suite'],label='suit 与 suite：随从、相随的整组',note='suite 是法语同一跟随词族的另次借入，与 suit 同源异形；套房、组曲、软件套件都按配套整体理解。'),
 'C1115':dict(words=['preliminary'],label='preliminary：跨过门槛之前的',note='preliminary 经拉丁、法语相应形式，含 prae 在前与 limen 门槛、词干 limin-；准备性、初步性质是今天常用义。'),
 'A1675':dict(words=['quantity','quantify'],label='quantity：量的性质与可以数出来多少',note='quantity 经法语接拉丁 quantitas，来自 quantus 多少，末尾对应 -ity 的拉丁性质名词材料；quantify 再对照把数量确定下来。'),
 'A1776':dict(words=['quantum','quanta'],label='借词复数 quantum 与 quanta',note='quantum、quanta 保留拉丁中性名词的单复数材料，与 quantity 共享 quantus 多少的来源；不是任意把英语 -um 结尾都换成 -a。'),
 'C0401':dict(words=['deficit'],label='deficit：拉丁它缺少变成英语不足名词',note='deficit 接法语借拉丁 deficere 的第三人称单数形式，意为它不足，较早含 de- 与 facere 的变形；整个动词形式被英语当作名词使用。'),
 'B3064':dict(words=['dead','line','deadline'],label='deadline：不可越过的界线到时间限度',note='deadline 是 dead + line；时间限度义在出版业固定，较早还有不动线、禁越边界等用法，现代义与某一早期用法的直接演化关系并非完全确证。'),
}
R('C0132','手臂；用臂抱住，或像手臂一样环抱、支撑','BRACHI：伸出双臂，把东西抱住、撑住',
 '抱住一个人，是 embrace；像手臂一样撑住东西，是 brace；围在手臂、手腕上的饰物，是 bracelet。',
 '较近拉丁 bracchium 手臂、前臂，更早借希腊 brakhion。现代医学组合形式 brachi-、brachio- 直接保留较多字母；日常 brace、embrace、bracelet 经法语变化，字形更短。',
 'brace、bracelet、embrace 是同族不同借入形式。bracelet 还有法语小称历史，brace 的固定、支撑义由抱合、握牢等发展；不能把所有 brace 都只译成身体手臂。',
 [['抱住、接受','embrace'],['固定、撑住与准备承受','brace'],['相应装置的复数','braces'],['手臂、手腕上的饰物','bracelet']],
 'brace 支撑、绷紧；embrace 抱住或欣然接受；bracelet 是手链、手镯；braces 常为牙套、背带等，依语境分清。',
 'She adjusted her bracelet and braced herself before stepping on stage.\n\n她整了整手链，登台前稳住了自己。',
 'brace braces bracelet embrace')
W('cargo','英 /ˈkɑːɡəʊ/；美 /ˈkɑːrɡoʊ/','货物；船、飞机等运载的一批货',
 '人上船是乘客，装进货舱、准备运到别处的东西是 cargo。重点是作为运输对象的一批货。',
 '借西班牙语 cargo 装载、负担，来自 cargar 装载，上接晚期拉丁 carricare 给车装货及 carrus 车辆。与 carry、car 同源；cargo 是经过西班牙语单独借入的形式。',
 [['拉丁 carrus → carricare → 西班牙语 cargar／cargo','车辆 → 装载 → 所装的一批货'],['英语 cargo','运输货物；船、机等所载货物']],
 'air cargo 航空货物；a cargo ship 货船；a cargo of grain 一船、批谷物；load cargo 装货；cargo space 货舱空间。',
 'unload the cargo；a cargo terminal。','cargo 常作货物统称，a cargo of ... 可数一批装载物。luggage 常说旅客行李，不是每件随身行李都在日常叫 cargo。',
 ('The ship arrived with a cargo of grain.','船载着一批谷物抵达了。'),('The aircraft has extra space for cargo.','飞机有额外的货物空间。'),sources=['https://www.etymonline.com/word/cargo','https://en.wiktionary.org/wiki/cargo#English'])
W('transit','/ˈtrænzɪt/；亦 /ˈtrænsɪt/','运输、通过；中转；公共交通〔尤美式〕',
 '东西从 A 去 B，还在路上，就是 in transit。把人们来回运送的一套公共系统，也发展出 transit 的交通用法。',
 '接法语及拉丁 transitus 通过，来自 transire 走过去，含 trans 跨过与 ire 去。英语先有通过、通道，后来有公共运输等义；词尾 it 承接去的拉丁词干材料。',
 [['拉丁 trans + ire → transire／transitus','跨过 + 去 → 通过、通行'],['英语 transit','运输、途中；公共交通；跨过天体表面等专业义']],
 'in transit 在运输途中；transit passengers 中转旅客；public transit 公共交通；a transit system 公交系统；goods damaged in transit 运输途中受损的货物。',
 'a transit route；in transit to another country。','transit 常关注移动、通过这个过程；transition 常说状态、阶段的转变。in transit 是在途中，不表示已经抵达。',
 ('The parcel is still in transit.','包裹还在运输途中。'),('The city is improving its public transit system.','城市正在改善公共交通系统。'),sources=['https://www.etymonline.com/word/transit','https://en.wiktionary.org/wiki/transit#English'])
W('compound','名词、形容词：英 /ˈkɒmpaʊnd/、美 /ˈkɑːmpaʊnd/；动词 /kəmˈpaʊnd/','化合物；复合的；使加重、合成；另源：围起来的院落',
 '几部分放在一起，形成复合整体；问题再叠上一层，会 compound 变得更严重。围起来的院区那个 compound 则有另一条来源。',
 '合成线经法语接拉丁 componere，com- 一起、ponere 放；末尾 d 后来增生。院落线通常联系马来语 kampong 村落、建筑群，经欧洲语言借入后拼写受前一同形词影响。',
 [['拉丁 componere → 法语／英语合成线','放在一起 → 复合、合成；叠加影响'],['另源马来语 kampong 等 → compound 院落线','村落、建筑群 → 围起来的一片院区']],
 'a chemical compound 化合物；a compound word 复合词；compound the problem 使问题更严重；compound interest 复利；a residential compound 住宅院区。',
 'a compound of elements；a guarded compound。','名词通常重读开头，动词重读后面。化学 compound 不等于只是搅在一起的 mixture；院落义也不能硬从化学混合来推。',
 ('The class compared a chemical compound with a simple mixture.','课堂上比较了化合物与简单混合物。'),('The delay compounded our difficulties.','延误让我们的困难雪上加霜。'),('The office is inside a guarded compound.','办公室在一处有守卫的院区内。'),sources=['https://www.etymonline.com/word/compound','https://en.wiktionary.org/wiki/compound#English'])
W('suite','/swiːt/','套房；一套配套家具、软件等；组曲',
 '几间房相连、几件家具相配、几段乐曲接成一组，核心都是相随、成套地放在一起。',
 '直接借法语 suite 跟随、随从、序列，与较早借入的 suit 同源；更早接拉丁 sequi 跟随、secutus 的相关材料。套房、组曲等义有法语用法及再次借入、拼写影响。',
 [['拉丁跟随词族 → 法语 suite','相随、随从；一系列事物'],['英语 suite','配套的一组；相连房间、组曲、软件套件']],
 'a hotel suite 酒店套房；a suite of rooms 一套相连房间；a software suite 软件套件；an orchestral suite 管弦乐组曲；a bathroom suite 配套卫浴设备。',
 'a furniture suite；a suite of tools。','suite 通常与 sweet 同音 /swiːt/；suit 套装、适合读 /suːt/。两词同源，但现代读音、用法各自分工。',
 ('They booked a suite with a separate sitting room.','他们订了一套带独立起居室的套房。'),('The software suite includes tools for writing and drawing.','这套软件包含文字和绘图工具。'),sources=['https://www.etymonline.com/word/suite','https://en.wiktionary.org/wiki/suite#English'])
W('brace','/breɪs/','支撑件、支架；撑住、绷紧；准备承受',
 '像伸出双臂把东西稳稳撑住。brace a shelf 是撑牢架子，brace yourself 是先稳住自己，准备承受冲击或坏消息。',
 '经法语 brace 手臂等接拉丁 bracchia、bracchium 手臂，较早借希腊 brakhion。抱合、抓牢的动作发展出固定、支撑装置与绷紧、使稳的动词义。',
 [['希腊 brakhion → 拉丁 bracchium／bracchia → 法语 brace','手臂；环抱、固定相关材料'],['英语 brace','支撑、固定装置；撑住、绷紧、准备承受']],
 'a knee brace 护膝、膝关节支具；brace a structure 支撑结构；brace yourself for something 准备承受某事；brace against the wind 顶住风站稳。',
 'a support brace；brace oneself for bad news。','brace yourself 不是抱住自己，而是稳住、做好承受准备。embrace someone 才通常是伸臂拥抱某人；两词的现代动作方向要分清。',
 ('He braced the shelf with a wooden support.','他用木支撑把架子撑牢了。'),('She braced herself for the difficult conversation.','她做好心理准备，要面对那场艰难的谈话。'),sources=['https://www.etymonline.com/word/brace','https://en.wiktionary.org/wiki/brace#English'])
W('braces','/ˈbreɪsɪz/','牙齿矫正器、牙套；背带〔英式常见〕；支撑件；大括号',
 '几件东西把结构固定住、托起来。牙套把牙齿逐渐约束到位置，背带把裤子吊住；程序文字中的大括号也常以成对包住内容来命名。',
 'brace + -s，因末音 /s/，复数词尾读 /ɪz/。brace 更早接手臂、抱合、固定材料，复数在背带、矫正装置等具体用途上固定下来。',
 [['brace','固定、支撑、抱合的装置'],['brace + -s → braces','支撑件；成套背带、牙套；成对括号等']],
 'wear braces 戴牙套或系背带，依场景；dental braces 牙齿矫正器；trouser braces 裤子背带；curly braces 大括号 { }。',
 'get braces；a pair of braces。','英式 braces 可说裤子背带，美式这一义常用 suspenders；dental braces 则明确是牙套。单看 wear braces，先看人在讲牙齿还是衣着。',
 ('She wore braces when she was a teenager.','她十几岁时戴过牙套。'),('He used braces to hold up his trousers.','他用背带吊住裤子。'),('Put the expression inside curly braces.','把表达式放在大括号里。'),sources=['https://www.etymonline.com/word/brace','https://en.wiktionary.org/wiki/braces#English'])
W('bracelet','/ˈbreɪslət/','手链、手镯；戴在手腕上的带状饰物',
 '围在手腕上的一圈饰物，可以是金属环，也可以是串珠、链条。名字保留了手臂这一老材料。',
 '借法语 bracelet，是 bracel 手臂饰物的相应小称，较早接拉丁 bracchiale 臂环、bracchium 手臂。可用小称材料帮助认形，但不是今天把动词 brace 加 let 就现场造出手链。',
 [['拉丁 bracchium → bracchiale → 法语 bracel','手臂 → 臂环、手臂饰物'],['法语小称 bracelet → 英语 bracelet','相应小饰物名称 → 手链、手镯']],
 'a silver bracelet 银手链、银镯；a charm bracelet 挂有小饰件的手链；a beaded bracelet 串珠手链；wear a bracelet 戴手链。',
 'a bracelet on her wrist；a friendship bracelet。','bracelet 一般围在手腕，necklace 围在脖子；bangle 常指硬质环状手镯，bracelet 范围更广，也可包括软链。',
 ('She wore a silver bracelet on her left wrist.','她左手腕上戴着一只银手镯。'),('The children made beaded bracelets for one another.','孩子们互相做了串珠手链。'),sources=['https://www.etymonline.com/word/bracelet','https://en.wiktionary.org/wiki/bracelet#English'])
W('embrace','/ɪmˈbreɪs/','拥抱；欣然接受、采用；包含；拥抱〔名词〕',
 '伸开双臂把人抱进来，是 embrace；把新方法、新机会也迎进来，就有欣然接受的意思。',
 '经法语 embracer、embracier 等接表示在内的 en-／em- 与手臂 brace、braz，较早为拉丁 bracchium、希腊 brakhion。英语保留环抱，并发展出接受、涵盖等抽象义。',
 [['拉丁、法语手臂材料与在内前缀结合','把东西抱在双臂中'],['英语 embrace','拥抱；积极接纳；范围涵盖']],
 'embrace someone 拥抱某人；embrace change 欣然接受变化；embrace an opportunity 抓住、接受机会；a warm embrace 热情拥抱。',
 'embrace a new approach；hold someone in an embrace。','embrace an idea 通常比 accept 更主动、热情，不只是勉强不反对。embrace 可直接接对象，不用额外加 with 来引出被抱的人。',
 ('They embraced when they met at the station.','他们在车站见面时拥抱了。'),('The team embraced the new approach.','团队欣然采用了新方法。'),sources=['https://www.etymonline.com/word/embrace','https://en.wiktionary.org/wiki/embrace#English'])
W('preliminary','英 /prɪˈlɪmɪnəri/；美 /prɪˈlɪməneri/','初步的、预备的；准备步骤、初赛等〔常用复数〕',
 '正式进屋前先过门槛；正式工作前的检查、讨论、试验，就像还站在门槛前准备。preliminary 表这类初步、准备性质。',
 '经法语或新、中世纪拉丁相应形式 praeliminaris，prae- 在前 + limen 门槛、词干 limin- + 形容词材料。英语较早还有复数 preliminaries 准备事项的用法。',
 [['拉丁 prae + limen／limin- → praeliminaris','门槛之前 → 进入正式阶段前的'],['英语 preliminary','初步、预备的；准备步骤、初赛']],
 'a preliminary report 初步报告；preliminary results 初步结果；a preliminary discussion 预备讨论；the preliminaries 准备步骤或预赛。',
 'a preliminary assessment；preliminary findings。','preliminary 强调先行、初步，不等于最终认可。preliminary results 是先拿到的初步结果，后面可能还有复核、补充。',
 ('The team released a preliminary report.','团队发布了一份初步报告。'),('We held a preliminary discussion before drawing up the plan.','制定方案前，我们进行了预备讨论。'),sources=['https://www.etymonline.com/word/preliminary','https://en.wiktionary.org/wiki/preliminary#English'])
W('quantity','英 /ˈkwɒntəti/；美 /ˈkwɑːntəti/','数量、量；一批、一定量',
 '不是先问东西好不好，而是问有多少：多少水、多少件货、多少份材料，都在看 quantity。',
 '经法语 quantite 接拉丁 quantitas 数量、大小，来自 quantus 多少、多大。末尾接性质、状态名词材料，与英语 -ity 对应；quantum、quantify 共享较早的多少材料。',
 [['拉丁 quantus → quantitas → 法语 quantite','多少、多大 → 数量、量的性质'],['英语 quantity','数量；某一批、某一定量']],
 'a large quantity of water 大量水；small quantities 少量、几小批；in quantity 大量地；quantity and quality 数量与质量。',
 'the quantity of material；produce in large quantities。','quantity 关心多少，quality 关心好坏、品质。quantity 可以用于可数或不可数对象，不必把它只限成中文的件数。',
 ('Only a small quantity of water is needed.','只需要少量水。'),('The factory produces the parts in large quantities.','工厂大批量生产这些零件。'),sources=['https://www.etymonline.com/word/quantity','https://en.wiktionary.org/wiki/quantity#English'])
W('quantum','英 /ˈkwɒntəm/；美 /ˈkwɑːntəm/','量子；一份量；量子的〔修饰语〕',
 '有些变化在特定系统中按一份一份的离散量发生。物理术语 quantum 把这种一份量标出来，具体每份有多少要看系统和过程。',
 '借拉丁 quantum 多少、一定量，为 quantus 的中性形式。英语先有一定量、总量等用法，近代物理把词专门化为离散量单位；复数 quanta。',
 [['拉丁 quantus → quantum','多少、多大 → 一定量'],['英语一般量义与物理专门化','某份量；物理中的量子及相关修饰语']],
 'a quantum of energy 一个能量量子；quantum physics 量子物理；quantum mechanics 量子力学；a quantum leap 常比喻重大跃进。',
 'quantum theory；the quantum nature of light。','比喻 quantum leap 常说重大进步；物理术语的量子、跃迁关心离散性，不能据比喻的重大认定所有量子变化都宏观巨大。quantity 是普通数量词，quantum 的现代日常出现多带专业语境。',
 ('The lecture introduced the idea of a quantum of energy.','讲座介绍了能量量子的概念。'),('The new method was described as a quantum leap in accuracy.','新方法被形容为精度上的重大跃进。'),sources=['https://www.etymonline.com/word/quantum','https://www.iop.org/explore-physics/big-ideas-physics/quantum-mechanics','https://en.wiktionary.org/wiki/quantum#English'])
W('quanta','英 /ˈkwɒntə/；美 /ˈkwɑːntə/','量子〔quantum 的复数〕；一份份的量',
 '一份是 quantum，多份是 quanta。物理文字把能量等按一份份来讨论时，经常见到这个保留的拉丁复数。',
 '保留拉丁中性词形 quantum → quanta，-um 与 -a 对应单复数。英语沿用这一组，并不表示普通英语凡是 -um 都必须这样变。',
 [['拉丁 quantum → quanta','一定量的单数 → 复数'],['英语物理、数量语境中的 quanta','多个量子；分立的一份份量']],
 'energy quanta 能量量子；discrete quanta 一份份离散量；quanta of radiation 辐射量子。复数搭配 quanta are，不用 a quanta。',
 'exchange energy in quanta；individual quanta。','quantum /təm/ 是单数，quanta /tə/ 是复数。quanta 通常接复数动词；想数一份用 one quantum。',
 ('In this model, energy is exchanged in discrete quanta.','在这个模型中，能量以离散的量子交换。'),('The diagram represents the radiation as a stream of quanta.','示意图把辐射表示为一股量子流。'),sources=['https://en.wiktionary.org/wiki/quanta#English','https://www.iop.org/explore-physics/big-ideas-physics/quantum-mechanics'])
W('deficit','/ˈdefɪsɪt/','不足额、缺口；赤字',
 '需要十份，手里只有八份，差的两份是 deficit。预算里收入不够覆盖支出时，也在说这一类缺口。',
 '经法语 deficit 借拉丁 deficit 它缺少、它不足，是 deficere 失败、不足的第三人称单数现在时。deficere 含 de- 与 facere 做的词干变形；原来一个完整动词形式被借作英语名词。',
 [['拉丁 de- + facere 的变形 → deficere／deficit','不足、失效 → 它不足'],['法语 → 英语 deficit 名词','不足的差额；财政等领域的赤字']],
 'a budget deficit 预算赤字；a trade deficit 贸易逆差；a deficit of resources 资源不足；reduce a deficit 缩小缺口；make up a deficit 弥补不足。',
 'a funding deficit；a deficit of ten points。','deficit 说相对需求、收入或对方成绩差了多少；surplus 常说多出来的部分。体育语境 a ten-point deficit 是落后十分。',
 ('The team overcame a ten-point deficit to win.','球队克服了十分的落后劣势，赢得比赛。'),('The project faces a funding deficit.','项目面临资金缺口。'),sources=['https://www.etymonline.com/word/deficit','https://en.wiktionary.org/wiki/deficit#English'])
W('deadline','/ˈdedlaɪn/','截止时间、最后期限',
 '时间线上画了一条到这里为止的界：这轮申请、交稿、提交要在它之前完成。那条界就是 deadline。',
 'dead + line。历史上有不动的线、不可越过的边界及印刷限界等不同用法；现代时间限度义在出版业固定。监狱禁越线影响时间义的说法常见，但直接演化链证据有限，不当作唯一确定故事。',
 [['dead + line 的早期多种界线用法','固定、不动或不可越过的界线；印刷等使用'],['现代出版业及一般事务中的 deadline','最后可交稿的时间 → 一般截止期限']],
 'meet a deadline 赶在期限内完成；miss a deadline 错过截止；extend the deadline 延长期限；a deadline for applications 申请截止时间。',
 'a tight deadline；work to a deadline。','by the deadline 通常表示不晚于截止时间；before the deadline 更明确在它之前。meet 是按期完成，miss 是错过，extend 则是把期限向后延。',
 ('The deadline for applications is Friday.','申请的截止时间是星期五。'),('We worked together to meet the deadline.','我们一起努力，按期完成了工作。'),sources=['https://www.etymonline.com/word/deadline','https://en.wiktionary.org/wiki/deadline#English'])
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_vd',ROOTS,WORDS)
 extend_lessons()
