"""Deal, single, information and number: close useful gaps in common families."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
D=[['古英语 dǣl；相关动词 dǣlan → 中古英语 del、delen','一份；分开、分配'],['英语 deal','分发；经营、往来；交易、待遇；大量这一固定短语用法']]
W('deal','/diːl/','分发；处理、应对；交易；待遇；大量',
 '先是把东西分成份，再延伸到人与人分配、交换的交易；deal with 则已固定为处理、与人打交道。',
 '常用词族接古英语 dǣl 一份与 dǣlan 分配。名词和动词都有旧来路，不是所有名词义都由现代动词临时造出。木板、松木材料的同形 deal 另有借词背景，不硬归为一份。',D,
 'deal cards 发牌，make a deal 达成交易，a good deal 划算的交易；a great deal of time 大量时间。deal with a problem 处理问题，deal in antiques 经营古董。过去式、过去分词 dealt /delt/。',
 'deal with；deal in；make a deal；a raw deal；a great deal of。',
 'deal with 处理、与……打交道，deal in 经营某类商品；a good deal of 可表许多，不一定是在说一桩好买卖。',
 ('Who will deal the cards this time?','这次谁发牌？'),('We need to deal with the booking problem first.','我们得先处理预订问题。'),('The old house needs a great deal of work.','这所老房子需要做大量修整。'))
W('dealing','/ˈdiːlɪŋ/','经营、交易；发牌；处理、交往的过程',
 '把分发、买卖或应对当成正在进行的一种活动。',
 'deal + -ing，名词或分词用法。意思跟随当前 deal 是发牌、买卖还是处理问题来确定。',D+[['deal → dealing','分发、交易、处理 → 这些活动及进行状态']],
 'art dealing 艺术品交易；dealing with complaints 处理投诉。fair dealing 公平交易、诚实往来，还可在某些制度中形成专门术语。',
 'art dealing；dealing in antiques；dealing with customers；fair dealing。',
 'dealing in 说交易什么，dealing with 说处理什么、与谁打交道；不必看到 dealing 就理解成非法交易。',
 ('His business involves dealing in old maps and books.','他的生意涉及买卖旧地图和旧书。'),('Dealing with customers requires patience.','与顾客打交道需要耐心。'))
W('dealings','/ˈdiːlɪŋz/','往来；交易活动',
 '不只看某一桩成交，而是看人与人、机构与机构怎样打交道。',
 'dealing + 复数 -s，常以复数形式说一段交往、商业往来或活动。现代固定用法不等于随便给所有 -ing 都加 s。',D+[['dealing → dealings','交易、交往 → 具体或持续的往来活动']],
 'have dealings with 与……有往来；business dealings 商业往来；在调查报道中还可能说可疑交易，但词本身不自动含犯罪。',
 'have dealings with；business dealings；in all one’s dealings with。',
 'a deal 可以是一桩交易；dealings with a supplier 是与供应商的往来，不必只限某一个合同。',
 ('I have had no dealings with that supplier before.','我以前没和那家供应商打过交道。'),('She values honesty in all her business dealings.','她在所有商业往来中都重视诚信。'))
W('dealer','英 /ˈdiːlə/；美 /ˈdiːlər/','经销商；商人；发牌者',
 '一边是专门买卖某类东西的人或商家，另一边是给大家分牌的人。',
 'deal + -er，古英语已有相应名词 dǣlere。现代继承不同动词义，所以不是所有 dealer 都做同一种事。',D+[['deal → dealer','分发、经营 → 发牌者、经销商']],
 'a car dealer 汽车经销商，an art dealer 艺术品商人；card dealer 发牌者。drug dealer 是特定搭配，不能反过来把所有 dealer 都读成毒贩。',
 'a car dealer；an antiques dealer；an authorized dealer；the card dealer。',
 'dealer 常突出经营、经销具体商品，seller 泛指卖方；牌桌上的 dealer 却可以完全没有卖东西。',
 ('We bought the van from a local car dealer.','我们从当地一家汽车经销商买了这辆厢式车。'),('The dealer shuffled the cards before the next round.','发牌者在下一轮前洗了牌。'))
W('dealership','英 /ˈdiːləʃɪp/；美 /ˈdiːlərʃɪp/','经销业务；经销商店、公司；经销资格',
 '从做经销的人，转到他的业务、经营场所或被授予的经销身份。',
 'dealer + -ship，后缀表示业务、身份等；并不是 dealer 加船这个名词。',D+[['dealer + -ship → dealership','经销商 → 经销业务、机构或资格']],
 'a car dealership 汽车经销商店，open a dealership 开设经销店；a dealership agreement 是经销协议。到底说机构还是资格，要看句子。',
 'a car dealership；run a dealership；a dealership agreement。',
 'dealer 可以是商人或公司，dealership 更明确指经销业务、门店或资格；它不直接等于汽车制造厂。',
 ('She manages a small motorcycle dealership.','她管理一家小型摩托车经销店。'),('The company awarded him a dealership for the region.','公司授予他在该地区的经销资格。'))
R('B2428','分发；应对；经营、交易、往来','DEAL：从一份、分配，到交易和打交道','先用发牌理解把东西分给别人，再看交易、待遇与各种固定短语。处理义要连 with 一起掌握。',
 'deal 常用词族来自古英语 dǣl 一份、dǣlan 分配。过去式 dealt；木材同形词另有借词背景，不硬编入这条线。',
 'deal → dealing → dealings；deal → dealer → dealership。',
 [['动作、过程与往来','deal · dealing · dealings'],['经销者、经销业务和门店','dealer · dealership']],
 'deal with 处理、交往，deal in 经营某商品；dealer 不自动是毒贩；dealership 不一定指具体某个商人。',
 'The dealer’s dealings with the new supplier helped the dealership grow.\n\n经销商与新供应商的往来，帮助经销业务发展了起来。',
 'deal dealing dealings dealer dealership')
S=[['拉丁语 singulus → 古法语 sengle → 中古英语 single','一个的、单个的'],['英语 single','单个、单独；相关词按数量、状态或衣物名称继续发展']]
W('singlet','/ˈsɪŋɡlət/','背心；某些运动中的紧身单件服',
 '现在通常想到无袖贴身上衣；历史名字却抓住它没有里衬、单层这一点。',
 'single + 指小后缀 -let / -et 的构形，仿照 doublet 等衣物名称。早期用于无衬短上衣，后来发展为背心等服装名称；不是一份单人票。',S+[['single 的单层义 + 指小形式 → singlet','无衬衣物名称 → 背心、某类运动服']],
 'a running singlet 跑步背心；a wrestling singlet 摔跤紧身连体服。地区、项目不同，衣物具体样式也不同。',
 'a cotton singlet；a running singlet；a wrestling singlet。',
 'single 是单个的，singlet 是固定衣物名；不能给所有 single things 都改叫 singlet。',
 ('He wore a light running singlet for the race.','他比赛时穿了一件轻薄跑步背心。'),('The team’s singlets were blue with white numbers.','队员的比赛背心是蓝色的，印着白色号码。'),sources=['https://en.wiktionary.org/wiki/singlet#English','https://www.oxfordlearnersdictionaries.com/definition/english/singlet'])
W('singleness','/ˈsɪŋɡəlnəs/','单一；专一；单身状态',
 '可以说生活里没有伴侣，也可以说心思只朝一个方向、不分散。',
 'single + -ness，把单个、未婚、专一等性质变成名词。具体义由后面的修饰内容决定。',S+[['single → singleness','单一、单身、专一 → 相应状态、性质']],
 'singleness of purpose 目标专一；her singleness 她的单身状态。前者不是说目标没有结婚，而是心无旁骛。',
 'singleness of purpose；the experience of singleness；singleness of mind。',
 'singleness 单身不等于 loneliness 孤独；是否有伴侣与是否感到孤独不是同一个问题。',
 ('Her singleness of purpose helped the project survive many setbacks.','她目标专一，帮助项目挺过了多次挫折。'),('The essay discusses singleness without treating it as a problem.','文章讨论单身状态，并没有把它当成问题。'))
R('B3661','单个；单独；单一、单身与专一','SINGLE：一个，还是独立的一份','基础词已含数量与关系等多种用法；singleton、singly 紧接基础词，singleness 再讲状态，singlet 另看衣物历史。',
 'single 经古法语来自拉丁语 singulus。派生词要看后缀及具体历史，不能仅凭长得像就随意交换。',
 'single → singly、singleton、singleness；服装名称 singlet 单列。',
 [['一个、逐个与单个成员','single · singly · singleton'],['状态与固定衣物名','singleness · singlet']],
 'singleness of purpose 是目标专一；单身不等于孤独；singlet 是衣物名，不是所有单个事物的通用称呼。',
 'The runners entered singly, each wearing a numbered singlet.\n\n跑步者一个接一个入场，每人穿着带号码的比赛背心。',
 'single singly singleton singleness singlet')
I=[['拉丁语 informāre → informātiō 等词族形式','赋予形态；教导、告知；说明'],['经法语、英语历史发展 → information','信息、消息；现代又产生相关技术、学科名称']]
W('informational','英 /ˌɪnfəˈmeɪʃənəl/；美 /ˌɪnfərˈmeɪʃənəl/','提供信息的；与信息有关的',
 '目的主要是把情况说明白，让人知道怎么回事。',
 'information + -al，形成与信息相关的形容词；不是把 information 误看成动词后再加时态。',I+[['information + -al → informational','信息 → 提供信息、与信息有关的']],
 'an informational leaflet 信息说明传单；an informational meeting 介绍情况的会议；for informational purposes 供了解情况之用。',
 'informational materials；an informational video；for informational purposes。',
 'informational 常说明用途、类别；informative 常评价内容让人得到知识、很有信息量。两者有重叠，不是绝对互斥。',
 ('The library prepared an informational leaflet for new members.','图书馆为新会员准备了一份信息介绍传单。'),('The school held an informational meeting about the exchange programme.','学校举行了一次交流项目情况说明会。'))
W('informatics','英 /ˌɪnfəˈmætɪks/；美 /ˌɪnfərˈmætɪks/','信息学；信息处理及其应用研究',
 '研究信息怎样被获取、组织、处理、传递，以及这些过程怎样服务人和系统。',
 '20世纪形成的学科名称，构词与 information 的词干、学科后缀 -ics 有关，也有德语 Informatik、法语 informatique 等命名背景。不是说一堆信息的复数。',I+[['information 相关词干 + -ics → informatics','信息 → 研究信息处理及其应用的学科名称']],
 'health informatics 健康、医疗信息学；bioinformatics 生物信息学。学校、行业对 informatics 的具体边界可能不同，不能处处直接等同某一门编程课。',
 'study informatics；health informatics；a school of informatics。',
 'information 是信息，informatics 是研究领域；词尾 s 属于 -ics 学科名，通常说 Informatics is...，不是一定要用 are。',
 ('She studies informatics and is interested in how people use data.','她学习信息学，对人们如何使用数据很感兴趣。'),('The university offers a course in health informatics.','大学开设了一门健康信息学课程。'),sources=['https://en.wiktionary.org/wiki/informatics#English','https://informatics.ed.ac.uk/about/what-is-informatics','https://ischool.uw.edu/programs/informatics/what-is-informatics'])
R('B3188','信息；与信息相关的用途和研究','INFORMATION：让人知道情况，再看信息怎样处理','基础词是信息本身；informational 说明提供信息的用途，informatics 则是研究信息处理的领域。',
 'information 来自经拉丁语、法语发展的说明、教导词族；其现代技术学科名称形成得很晚，不能把计算机义塞进古拉丁语。',
 'information → informational、informatics；misinformation、disinformation 放在信息出错与蓄意误导一组对照。',
 [['信息、信息用途与信息学','information · informational · informatics'],['错误信息与蓄意误导','misinformation · disinformation']],
 'informational 常说用途，informative 常说内容有启发；informatics 学科名不是 information 的复数。',
 'The informational video explains what students can study in informatics.\n\n这段介绍视频说明了学生在信息学领域可以学习哪些内容。',
 'information informational informatics misinformation disinformation')
NU=[['拉丁语 numerus → 古法语 nombre → 中古英语 number','数；数量'],['英语 number','数字、数量、编号；还可作编号等动词']]
W('numberless','英 /ˈnʌmbələs/；美 /ˈnʌmbərləs/','无数的；没有号码的',
 '可以是多得数不过来，也可以按字面说没有给它分配号码。',
 'number + -less，没有……的；常用文学性义把没有可给出的数理解成数量极多，另有无编号的字面用法。',NU+[['number + -less → numberless','数、号码 → 无数；没有号码的']],
 'numberless stars 无数星辰；a numberless house 没有门牌号的房子。前者偏文学，日常很多场合直接说 countless、many。',
 'numberless stars；numberless times；a numberless door。',
 'numberless 不等于数量为零；无数与无编号由名词、上下文分清。numbered 则是有编号的。',
 ('Numberless stars filled the dark sky.','无数星辰布满夜空。'),('The address led us to a numberless door in a narrow lane.','地址把我们带到一条窄巷里一扇没有门牌号的门前。'))
R('B2458','数；数量；编号','NUMBER：数有多少，也给东西一个号码','number 的数量与编号两种功能分开看，才能读懂 numberless 的两种意思。',
 'number 经古法语 nombre 来自拉丁语 numerus。numbering 是编号、计数活动，outnumber 是数量多于。',
 'number → numbering；outnumber 比较数量；numberless 是否定数量可数尽或否定有号码。',
 [['数量、编号及其过程','number · numbering'],['数量比较与无数、无编号','outnumber · numberless']],
 'numberless 常是无数，不是零；a numberless door 则可以是没有门牌号码的门。',
 'The volunteers numbered the boxes, but two remained numberless.\n\n志愿者给箱子编号，但仍有两个没有标上号码。',
 'number numbering outnumber numberless')
if __name__ == '__main__':save('continuation_20261029_bw',ROOTS,WORDS)
