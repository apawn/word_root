"""Frequent institutional words and compounds used in everyday work."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'B3595':dict(words=['ambassador','embassy'],label='ambassador 与 embassy：使者、使命与使馆',note='embassy 与 ambassador 经罗曼语不同形式接更早使者、随从材料；embassy 由使命、职务转指人员机构与馆舍，不能直接按英语 ambassador 换尾造词。'),
 'B2538':dict(words=['money','monetary'],label='monetary：铸币材料中的货币性质',note='monetary 接拉丁 monetarius 铸币、钱币相关的性质词，与 money 接 moneta 铸币处、钱币同族；不是现代 money 直接加 tary。'),
 'C0436':dict(words=['influence','influential'],label='influential：流入、影响到有影响力',note='influential 接中世纪拉丁 influentialis，与 influentia 影响、流入同族；现代可认词干 influenti- 与形容词材料，但需保留借入历史。'),
 'C0247':dict(words=['consult','counsel'],label='咨询、商议与 counsel 建议的对照',note='counsel 经法语接拉丁 consilium 计划、意见，传统常联系 com- 共同等材料，后部和 consult 的更远词源有不同分析；这里不声称 counsel 由现代 consult 直接派生。'),
 'C0189':dict(words=['exceed','excess'],label='exceed 与 excess：走过界限，及超出的量',note='exceed 接拉丁 excedere 走出去、超过，excess 接相应词干 excess- 的名词；动词和名词经不同形态进入英语。'),
 'B2898':dict(words=['back','backup'],label='backup：站在后面支持到备用、备份',note='backup 名词由 back up 支持、倒退等短语发展，现代常说支援、备用安排和数据备份；词类不同会影响合写或分写。'),
 'B2968':dict(words=['set','setup'],label='setup：把东西安排就位后的整体',note='setup 从 set up 设立、安排、装配的短语名词化，现代说配置、安排及设下的圈套等；不把名词直接当分写动词。'),
 'B2828':dict(words=['break','breakdown'],label='breakdown：整体失效，或把整体分成小项',note='breakdown 来自 break down，故障、崩溃线与分解、详细明细线分开举例，后者不意味着数据已经坏掉。'),
 'B2890':dict(words=['lay','layout'],label='layout：由 lay out 摊开、安排而来的布局',note='layout 来自使东西就位的 lay 与 out，接古英语 lecgan 的使动放置线；不接说谎的另源 lie。'),
 'A1675':dict(words=['entity'],label='entity：把存在作为性质和一个可指认单位',note='entity 接拉丁 entitas，由 ens、ent- 存在者与性质名词材料形成；现代常指可单独看待的事物、组织或对象。'),
 'A1904':dict(words=['fabric','fabricate'],label='fabrica 的借词对照：材料与制造',note='fabric 与 fabricate 共享拉丁 fabrica 作坊、制作、结构等材料，英语分别借入发展；不能把 fabric 的现代布料义当成所有 fabricate 都只制造布。'),
}
W('embassy','/ˈembəsi/','大使馆；大使及其工作人员、外交使团；出使使命〔历史等用法〕',
 '一位大使不是独自办事，还带着一群人执行外交使命。embassy 可以指这套机构和人员，也可以指他们办公的馆舍。',
 '经法语 embassee、ambassee 等使命、职务名称，接意大利语、普罗旺斯语相关形式，更早与 ambassador 的使者、随从材料同族。英语由使命、职务发展出使馆人员、馆舍义。',
 [['罗曼语的使者、使命词群 → embassy','执行使命、担任使者的职务'],['英语机构、处所用法','大使馆机构与人员；相应馆舍']],
 'contact the embassy 联系使馆；an embassy official 使馆官员；the embassy building 使馆馆舍；work at an embassy 在使馆工作。',
 'the embassy staff；an embassy reception。','ambassador 是大使这个人，embassy 是相应机构、人员或馆舍。embassy issued a statement 里 embassy 代表使馆机构；embassy building 才明确指馆舍。',
 ('She works at an embassy in the capital.','她在首都的一家大使馆工作。'),('The embassy issued a statement that afternoon.','使馆当天下午发表了声明。'),sources=['https://www.etymonline.com/word/embassy','https://en.wiktionary.org/wiki/embassy#English'])
W('monetary','英 /ˈmʌnɪtəri/；美 /ˈmʌnəteri/','货币的；金钱的、以钱衡量的',
 '问的是钱、货币或金钱数额，monetary 把这个范围圈出来。a monetary reward 就是以钱给出的奖励。',
 '接晚期拉丁 monetarius 钱币、铸币相关的，来自 moneta 铸币处、钱币，与 money 同族。英语较早强调货币、铸币，后来也泛说金钱相关。',
 [['拉丁 moneta → monetarius','铸币处、钱币 → 货币、钱币相关的'],['英语 monetary','货币的；金钱上的']],
 'monetary policy 货币政策；a monetary reward 金钱奖励；monetary value 金钱价值；monetary compensation 金钱补偿。',
 'a monetary amount；nonmonetary benefits。','monetary 常专指钱、货币层面；financial 范围更广，可涉及资金、财务安排。monetary value 不等于一个事物全部的情感或文化价值。',
 ('The reward has no monetary value.','这份奖励没有金钱价值。'),('The lecture introduced the basic idea of monetary policy.','讲座介绍了货币政策的基本概念。'),sources=['https://www.etymonline.com/word/monetary','https://en.wiktionary.org/wiki/monetary#English'])
W('influential','/ˌɪnfluˈenʃəl/','有影响力的；能影响决定或发展方向的',
 '这个人说一句话，能改变别人的想法；这本书写出一套观点，后来许多人沿着它走，都可以是 influential。',
 '接中世纪拉丁 influentialis，来自 influentia 影响、流入，上接 in- 向内与 fluere 流。较早占星用法把影响想成流入的力量，后来推广到人与事物的影响力。',
 [['拉丁 influere → influentia／influentialis','流入 → 产生影响的力量、相关性质'],['英语 influential','能影响人的选择、事物走向的']],
 'an influential writer 有影响力的作家；an influential study 影响深远的研究；be influential in doing 对某事起重要影响；highly influential 影响很大。',
 'an influential figure；an influential book。','famous 是许多人知道，influential 是能产生影响。一个研究者可能不为大众熟知，却深刻改变了专业领域。',
 ('Her work was influential in the development of the field.','她的工作对这个领域的发展有重要影响。'),('The book became highly influential among young designers.','这本书在年轻设计师中产生了很大影响。'),sources=['https://www.etymonline.com/word/influential','https://en.wiktionary.org/wiki/influential#English'])
W('counsel','/ˈkaʊnsəl/','建议、劝告〔较正式〕；律师、律师团；劝告、提供建议',
 '遇到难决定的事，找人商量，对方给你的郑重建议可以叫 counsel。以给法律意见为职责的人，也被称为 counsel。',
 '名词经法语 conseil 接拉丁 consilium 计划、意见、商议；动词接相关法语 conseiller、拉丁 consiliari。更远构词有不同分析，保留可靠近源，不把每个现代音节都硬配一个意思。',
 [['拉丁 consilium／consiliari → 法语相关词','计划、意见；商议、给建议'],['英语 counsel 名词、动词','建议、劝告；提供建议；法律语境的律师等']],
 'seek counsel 征求意见；wise counsel 明智建议；legal counsel 法律顾问、律师等；counsel someone to do 劝某人做；counsel caution 建议谨慎。',
 'take counsel；counsel someone against doing something。','council 常与 counsel 同音，但 council 是委员会、议会等机构；counsel 常是建议或提供建议的人。普通建议义通常不可数，不说 a counsel 表一条日常建议。',
 ('She sought counsel from a trusted colleague.','她向一位信任的同事征求意见。'),('He counselled patience while the results were checked.','核查结果期间，他建议耐心等候。'),('The company’s legal counsel reviewed the document.','公司的法律顾问审阅了文件。'),sources=['https://www.etymonline.com/word/counsel','https://en.wiktionary.org/wiki/counsel#English'])
W('excess','/ˈekses/；部分形容词用法亦 /ɪkˈses/','过量、过剩；超出的部分；额外的、多余的',
 '杯子只装得下这么多，再添进去的就是 excess。需求、限额也是一条界，超过它的量可以这样说。',
 '经法语 exces 接拉丁 excessus 走出去、超过，来自 excedere，ex- 向外与 cedere 走、退让。与 exceed 对应同一超过词族，但借入的词干形态不同。',
 [['拉丁 ex + cedere → excedere／excessus','向外走 → 越界、超出的程度或量'],['英语 excess','过量、超出的部分；超过所需的性质']],
 'excess water 多余水分；excess baggage 超额行李；in excess of 超过；an excess of supply 供应过剩；to excess 过度地。',
 'remove the excess；excess demand。','exceed 是动词：The cost exceeds the limit。excess 可作名词或修饰语：the excess；excess cost。两者不能只凭中文超过互换词性。',
 ('Wipe away any excess water.','擦去多余的水。'),('The number of visitors was in excess of our expectations.','游客数量超过了我们的预期。'),sources=['https://www.etymonline.com/word/excess','https://en.wiktionary.org/wiki/excess#English'])
W('backup','/ˈbækʌp/','备用、后备；支援；备份；拥堵、积压〔部分语境〕',
 '第一套安排顶不住时，后面还有东西接上，是 backup；文件另留一份，出问题还能接回来，就是备份。',
 '由 back up 的动词短语形成名词和修饰用法；back 从后面、支持，up 在短语中参与撑住、维持等意义。现代先有后备、支援的整体名词，再有计算机副本等专门用法。',
 [['back up 动词短语','在后面支持；另有倒退、积住等义'],['合写 backup 名词及修饰语','后备、支援；备份；积压等']],
 'a backup plan 备用方案；a backup copy 备份副本；ask for backup 请求支援；a traffic backup 交通拥堵；make a backup 做备份。',
 'backup equipment；a backup of the files。','名词、修饰语常合写 backup：a backup copy；动词通常分写 back up：back up the files。含代词时 back them up，把 them 放中间。',
 ('We need a backup plan in case it rains.','我们需要一套下雨时的备用方案。'),('I saved a backup before editing the file.','编辑文件前，我存了一份备份。'),('The rescue team asked for backup.','救援队请求支援。'),sources=['https://www.etymonline.com/word/backup','https://en.wiktionary.org/wiki/backup#English'])
W('setup','/ˈsetʌp/','安排、配置；装配、设置过程；整套装置；圈套、设计好的局',
 '桌子、设备、人员怎样摆好，形成一套能运作的安排，就是 setup。若这套安排专为引人上当，也能说 a setup。',
 '由 set up 放置、设立、安排的短语名词化。set 的使就位、设定线与 up 的建立、达到状态等用法结合，后来固定为安排、配置、布置好的局面。',
 [['set up','使就位；设立、装配、安排'],['名词 setup','安排好的整体；设置过程；有意设下的局']],
 'a simple setup 简单配置；the initial setup 初始设置；a recording setup 录音设备配置；the office setup 办公布局、工作安排；It was a setup 那是个圈套。',
 'a new setup；the setup process。','名词常合写 setup，动词用 set up：The setup is simple；We set up the equipment。set 的过去式仍是 set，不是 setted。',
 ('The initial setup took less than an hour.','初始设置用了不到一个小时。'),('The new office setup gives everyone more space.','新的办公安排给每个人留出了更多空间。'),sources=['https://en.wiktionary.org/wiki/setup#English'])
W('breakdown','/ˈbreɪkdaʊn/','故障、失灵；崩溃、中断；分类明细、分解',
 '整体撑不住而散掉，是故障、中断；主动把整体拆成小项看清楚，则是明细分解。同一个拆开画面，可以通向两种不同结果。',
 '由 break down 打破、坍下、失效、分解等短语名词化。故障、崩溃较早，分类分析、明细的名词用法后来发展；不是每个 breakdown 都表示坏事。',
 [['break + down 的动词短语','打破、散开；失效；拆成组成部分'],['名词 breakdown 的分支','故障、中断；崩溃；各部分的分析明细']],
 'a car breakdown 汽车故障；a breakdown in communication 沟通中断；a cost breakdown 费用明细；a breakdown by age 按年龄分类的明细。',
 'a detailed breakdown；the breakdown of negotiations。','breakdown 是名词，break down 是动词：a breakdown of costs；break the costs down。a breakdown of costs 是费用明细，a breakdown in talks 是谈判中断，后面的对象和介词能帮助分义。',
 ('A car breakdown delayed our trip.','汽车故障耽误了行程。'),('Could you send me a breakdown of the costs?','能把费用明细发给我吗？'),('There was a breakdown in communication between the two teams.','两个团队之间的沟通出了问题。'),sources=['https://www.etymonline.com/word/breakdown','https://en.wiktionary.org/wiki/breakdown#English'])
W('layout','/ˈleɪaʊt/','布局、排列；版式；布置设计',
 '把东西摊开、摆到各自位置，再看整体怎样排列。房间、网页、书页都可以有自己的 layout。',
 '由 lay out 摊开、安排各部分的动词短语形成名词。lay 接古英语 lecgan 使东西就位，和躺下 lie 的历史使动关系相连；out 参与展开、摆开的意思。',
 [['lay + out → lay out','放置并展开；安排各部分'],['名词 layout','已经安排好的整体；布局、版式']],
 'the layout of a room 房间布局；a page layout 页面版式；a keyboard layout 键盘布局；a clear layout 清楚的排列设计。',
 'change the layout；the layout of the site。','layout 是名词，lay out 是动词：change the layout；lay out the page。outlay 词序相反，常说支出，不能与 layout 布局互换。',
 ('The new layout makes the page easier to read.','新版式让页面更容易阅读。'),('I like the layout of the kitchen.','我喜欢厨房的布局。'),sources=['https://www.etymonline.com/word/layout','https://en.wiktionary.org/wiki/layout#English'])
W('entity','/ˈentəti/','实体；可单独看待的事物、组织或存在',
 '把它当成一件可以单独指认、讨论的东西，而不只是一团零散部分，就能说 an entity。它可以是机构，也可以是抽象对象。',
 '接中世纪拉丁 entitas 存在，来自 ens、词干 ent- 存在者与性质名词 -tas，较早联系 esse 是、存在。英语由存在这个抽象性质发展为一个存在的单位。',
 [['拉丁 ens／ent- + -tas → entitas','存在者 → 存在这一性质'],['英语 entity','存在；后来可指一个独立看待的事物、组织']],
 'a separate entity 一个独立单位；a legal entity 法律主体、法人等按文本看；a business entity 商业实体；a single entity 一个整体单位。',
 'treat something as an entity；distinct entities。','entity 不要求一定能摸到。数据库中的对象、讨论中的机构也可这样叫；physical entity 才特意强调物理上存在的东西。',
 ('The two departments operate as separate entities.','两个部门作为独立单位运作。'),('The system treats each customer as a distinct entity.','系统把每位客户作为一个单独的实体处理。'),sources=['https://www.etymonline.com/word/entity','https://en.wiktionary.org/wiki/entity#English'])
W('fabric','/ˈfæbrɪk/','布、织物；结构、组织体系',
 '做衣服要看这块 fabric 软不软、厚不厚；一座社会由许多关系交织起来，也可以谈 the fabric of society 这个整体结构。',
 '经法语 fabrique 接拉丁 fabrica 作坊、工艺、制作物、结构，来自 faber 工匠。英语较早有建筑、结构义，后来布料义常用；与 fabricate 同族，源头并非只指织布。',
 [['拉丁 faber → fabrica → 法语 fabrique','工匠 → 工艺、制作物、结构'],['英语 fabric','结构；后来常指布料、织物；保留抽象结构义']],
 'cotton fabric 棉织物；a soft fabric 柔软布料；fabric samples 布样；the social fabric 社会组织结构；the fabric of a building 建筑结构。',
 'a piece of fabric；the fabric of everyday life。','fabric 日常多说织物材料，cloth 也常说布；the fabric of society 中则是抽象的关系、组织结构。fabricate 可以制造物品，也可编造说法，不局限于处理布料。',
 ('She chose a light fabric for the summer curtains.','她给夏季窗帘选了轻薄布料。'),('Local clubs are part of the social fabric of the town.','当地社团是小镇社会结构的一部分。'),sources=['https://www.etymonline.com/word/fabric','https://en.wiktionary.org/wiki/fabric#English'])
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_ve',ROOTS,WORDS)
 extend_lessons()
