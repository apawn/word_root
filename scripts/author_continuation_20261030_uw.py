"""Complaint family plus frequent nouns omitted from older root selections."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'C0221':dict(words=['circle','circuit'],label='circuit：绕一圈的路线与闭合通路',note='circuit 接拉丁 circuitus 绕行，含 circum 周围与 ire 去；英语路线、赛道、电路等分支分开解释。'),
 'B3165':dict(words=['poor','poverty'],label='poor 与 poverty：贫乏的性质',note='poverty 经法语接拉丁 paupertas 贫困，与 poor 经法语接 pauper 同族；不是英语 poor 简单换尾。'),
 'B3077':dict(words=['solid','soldier'],label='soldier：坚实金币名称到领军饷者',note='soldier 经法语接中世纪拉丁 soldarius 领军饷者，较早接 solidus 金币名；与 solid 同族，不来自英语 sold + -ier。'),
 'C0401':dict(words=['faculty'],label='faculty：做得到的能力与学术群体',note='faculty 接拉丁 facultas 能力、资源等词，较早与 facilis 易做的及 facere 做相连；院系、教师群体义各有学术史，非现代直接从能力任意推出。'),
 'C0369':dict(words=['premium'],label='premium：奖赏、额外价与优质标记',note='premium 接拉丁 praemium 奖赏、战利所得，含 prae 与取、买 emere 的历史材料；保费义另有意大利语同源词影响。'),
 'B3693':dict(words=['ward','reward','garage'],label='看顾词族的法语分支：reward 与 garage',note='reward、garage 经法语不同词借入，较早接日耳曼看顾、保护材料；与 ward 有历史联系，并非现代英语 ward 临时换几个字母。'),
 'B3806':dict(words=['column','colonel'],label='column 与 colonel：纵队及其军官',note='colonel 经意大利语、法语的纵队军官名称借入；拼写与读音分别保留不同历史层，因此有字母 l 却读出 r。'),
 'C0743':dict(words=['minute','menu'],label='menu：小的、细分的到逐项菜单',note='menu 借法语相应名词，较早接拉丁 minutus 小的、细分的；与 minute 同族，不是现代英语 minute 任意删字。'),
 'C0979':dict(words=['fee'],label='fee：牲畜财产到费用',note='fee 接古英语 feoh 牲畜、财产、钱财，也与法语封地相关词有合流影响；与拉丁 pecu 牲畜材料为更远同源比较，不是从拉丁直接借来。'),
}
R('C1058','击打；捶胸哀叹，发展出抱怨、申诉','PLANG／PLANCT：难受时捶胸、发出哀叹',
 '先想一个人在难过时捶胸叹息；再把身体动作放轻，保留用语言表达不满，就到 complain。',
 '拉丁 plangere 有击打、捶胸哀悼等义，分词词干 planct-。经较早复合动词与法语 complaindre，英语形成常用 complain、complaint 这一组。',
 'com- 在这一历史组合中有加强作用；plangere 经法语发生词形变化，不能从现代 complain 中强行找出完整 plang。complaint 来自法语相关名词，末尾 t 不是英语给 complain 普遍添加的名词规则。',
 [['用语言表达不满','complain'],['把不满作为一件事提出','complaint'],['抱怨的过程、语气','complaining']],
 'complain 是动词，complaint 是名词；complain about the noise 抱怨噪声，make a complaint about the noise 提出关于噪声的投诉。',
 'Instead of only complaining, she made a clear complaint about the noise.\n\n她没有只顾抱怨，而是就噪声清楚地提出了投诉。',
 'complain complaint complaining')
W('complain','/kəmˈpleɪn/','抱怨；投诉、申诉；诉说不适',
 '事情让你不舒服或觉得不公平，你把不满说出来。对朋友说可能是抱怨，对负责处理的人正式提出就可能是投诉。',
 '经法语 complaindre 接较早拉丁复合 *complangere，含加强用的 com- 与 plangere 击打、捶胸哀叹。身体上的哀痛表达逐渐转到用话语诉说痛苦、不满。',
 [['拉丁 plangere；较早复合 *complangere','击打、捶胸哀叹；表达痛苦'],['法语 complaindre → complain','哀叹 → 抱怨、申诉、诉说不适']],
 'complain about the noise 抱怨噪声；complain to the manager 向经理投诉；complain that ... 抱怨某个情况；complain of pain 诉说疼痛。',
 'nothing to complain about；can’t complain。','complain about 后接不满的事，complain to 后接听取投诉的人。普通用法不要直接说 complain the noise；名词要用 complaint。',
 ('The neighbours complained about the noise.','邻居们抱怨噪声。'),('She complained to the manager that the room was dirty.','她向经理投诉房间不干净。'),sources=['https://www.etymonline.com/word/complaint','https://en.wiktionary.org/wiki/complain#English'])
W('complaint','/kəmˈpleɪnt/','抱怨、投诉；诉状等正式指控；病痛、不适〔部分用法〕',
 'complain 是把不满说出来，a complaint 是提出的那件不满、投诉本身。它可以是一句话，也可以成为一份正式记录。',
 '借法语 complainte 哀叹、抱怨，原接 complaindre 的分词名词材料。它与 complain 同族，但末尾 t 有法语词形历史，不能推广为英语动词加 t 就成名词。',
 [['法语 complaindre → complainte','哀叹、表达不满 → 相应名词'],['英语 complaint','抱怨、投诉；正式指控；引起不适的病痛']],
 'make a complaint 提出投诉；a complaint about a service 对服务的投诉；a customer complaint 客户投诉；a common complaint 常见抱怨，也可能是常见病痛。',
 'handle complaints；a letter of complaint。','complaint 与 complain 差一个 t，词性不同：They complained；They made a complaint。medical complaint 中则常说病痛或不适，要看领域。',
 ('The hotel received several complaints about the heating.','酒店收到几起关于供暖的投诉。'),('Please put your complaint in writing.','请把投诉内容写下来。'),sources=['https://www.etymonline.com/word/complaint','https://en.wiktionary.org/wiki/complaint#English'])
W('complaining','/kəmˈpleɪnɪŋ/','抱怨、投诉；爱抱怨的、带抱怨语气的；complain 的 -ing 形式',
 '不满正在被反复说出来。Stop complaining 是叫人停止抱怨；a complaining voice 则在描写语气。',
 'complain + -ing，继承法语、拉丁哀叹词族；现代名词用法指抱怨活动，修饰语描写表达不满的性质。',
 [['complain','表达不满、诉说痛苦'],['complain + -ing → complaining','抱怨的过程；表达不满的语气、行为']],
 'keep complaining 不停抱怨；complaining about the weather 抱怨天气；a complaining tone 抱怨的口气；without complaining 不抱怨地。',
 'constant complaining；a complaining customer。','She is complaining about the delay 是她在表达不满；She is being complained about 是别人正在投诉她，动作方向相反。',
 ('He carried the heavy bags without complaining.','他提着沉重的袋子，没有抱怨。'),('Constant complaining made the meeting less productive.','不断的抱怨使会议成效降低了。'),sources=['https://www.etymonline.com/word/complaint','https://en.wiktionary.org/wiki/complaining#English'])
W('circuit','英 /ˈsɜːkɪt/；美 /ˈsɝːkɪt/','环行路线、赛道；电路；巡回活动范围',
 '从这里出发，绕一圈又接回来：这是 circuit 的老画面。跑道是一圈路线，闭合电路是连成回路的通道。',
 '经法语接拉丁 circuitus 绕行、周围路线，来自 circuire 绕着走，含 circum 周围与 ire 去。后来扩展到巡回路线、体育赛场网络和电路。',
 [['拉丁 circum + ire → circuire／circuitus','围绕着走 → 绕行、环形路线'],['英语 circuit','路线、赛道；巡回范围；电路']],
 'an electrical circuit 电路；a racing circuit 赛车赛道；a circuit of the island 绕岛一圈；the lecture circuit 巡回演讲活动圈。',
 'complete a circuit；a circuit board。','电路能有闭合、断开等状态，不能把词源的绕一圈误当成任何叫 circuit 的电路当前一定通电。circle 更直接说圆形，circuit 常强调路线或通路。',
 ('We walked a complete circuit of the lake.','我们绕湖走了完整一圈。'),('The switch opens and closes the circuit.','开关使电路断开或闭合。'),sources=['https://en.wiktionary.org/wiki/circuit#English'])
W('poverty','英 /ˈpɒvəti/；美 /ˈpɑːvərti/','贫困；贫乏、缺少',
 '生活所需的资源不够，日子难以维持，这是 poverty。再扩大一点，想象力、内容也可以少得贫乏。',
 '经法语 poverte、pauvrete 接拉丁 paupertas 贫困，来自 pauper 贫穷的。与 poor 同源，英语分别保留性质词与抽象名词的借入形式。',
 [['拉丁 pauper → paupertas','贫穷的 → 贫困状态'],['法语 → 英语 poverty','经济贫困；抽象的贫乏、缺少']],
 'live in poverty 生活贫困；reduce poverty 减少贫困；a poverty of imagination 想象力贫乏；the poverty line 贫困线。',
 'child poverty；extreme poverty。','poor 是形容词，poverty 是名词：poor families；families living in poverty。a poor performance 表现差，不能每次都机械换成 poverty。',
 ('The programme aims to reduce child poverty.','这项计划旨在减少儿童贫困。'),('The essay showed a poverty of imagination.','这篇文章显得缺少想象力。'),sources=['https://en.wiktionary.org/wiki/poverty#English'])
W('soldier','英 /ˈsəʊldʒə/；美 /ˈsoʊldʒər/','士兵、军人；坚持做下去〔soldier on〕',
 '现代先记军队里服役的人；名字的老线索却连到领军饷，再连到一种金币。soldier on 把艰难中继续前进的画面留下。',
 '经法语 soudier、soudeour 等接中世纪拉丁 soldarius 领军饷的军人，较早接 soldum、solidus 金币名称。solidus 原有坚实的性质义，与 solid 同族。',
 [['拉丁 solidus 金币 → soldum／soldarius','金币、军饷 → 领军饷服役的人'],['法语 → 英语 soldier','军人；后有 soldier on 坚持前行']],
 'a young soldier 年轻士兵；soldiers in uniform 穿制服的军人；soldier on 坚持下去；a soldier’s life 军旅生活。',
 'a former soldier；soldier on through difficulties。','soldier 中的 d 与后续声音形成 /dʒ/，不是 sold + 一个英语 -ier 临时拼成。现代并不因老军饷词源就只指雇佣兵。',
 ('The soldier returned home after several months away.','那位军人离家几个月后回到了家。'),('Despite the broken equipment, the team soldiered on.','尽管设备坏了，团队仍坚持继续干。'),sources=['https://www.etymonline.com/word/soldier','https://en.wiktionary.org/wiki/soldier#English'])
W('faculty','/ˈfækəlti/','能力、官能；学院、学部；全体教师〔尤美式〕',
 '人能看、能记、能判断，是具备相应 faculty；大学中掌握某类学问的分支和教师群体，也形成这个词的学术用法。',
 '经法语 faculte 接拉丁 facultas 能力、资源等，较早与 facilis 易做的、facere 做相连。学术的知识分支、院系和教师群体义有较长历史，并非现代从身体能力一次直接生造。',
 [['拉丁 facere／facilis → facultas','做、易做 → 能力、资源'],['法语 → 英语 faculty 的分支','能力、官能；知识分支、学院、教师群体']],
 'the faculty of memory 记忆能力；mental faculties 心智能力；the Faculty of Science 理学院等；faculty members 教师、教员；the faculty 全体教师，常见美式。',
 'a member of the faculty；retain one’s faculties。','a faculty 在大学名称里可能是学院，在美式教学语境 faculty 常指教师群体。facilities 是设施，拼写相像但不能替换。',
 ('The university appointed three new faculty members.','大学新聘了三位教师。'),('The course explores the human faculty of language.','这门课探讨人的语言能力。'),sources=['https://www.etymonline.com/word/faculty','https://en.wiktionary.org/wiki/faculty#English'])
W('premium','/ˈpriːmiəm/','额外价、溢价；保险费；奖赏；优质的、高档的',
 '为了更好的位置多付一笔，是 pay a premium；商品标着 premium，常是在强调更高档。保费则是保险领域固定下来的另一支。',
 '借拉丁 praemium 奖赏、战利所得，含 prae 在前与 emere 取、买的历史材料；保费义另接意大利语 premio 等影响。英语后来形成额外价格与优质修饰义。',
 [['拉丁 praemium','奖赏、所得；含取、买的旧材料'],['英语 premium 与同源借词影响','额外价、保费；优质的']],
 'pay a premium 多付溢价；an insurance premium 保险费；premium quality 优质；space is at a premium 空间紧缺、很宝贵。',
 'a monthly premium；premium services。','premium 不总等于保险。pay a premium for a sea view 说为海景多付钱；a premium service 是较高档的服务标签，实际内容要看说明。',
 ('Rooms with a sea view come at a premium.','海景房要多付一些钱。'),('Space is at a premium in this tiny kitchen.','这间小厨房里空间非常宝贵。'),sources=['https://www.etymonline.com/word/premium','https://en.wiktionary.org/wiki/premium#English'])
W('reward','/rɪˈwɔːd/；美 /rɪˈwɔːrd/','奖赏、回报；奖励、酬谢',
 '有人付出帮助、做出成绩，随后得到感谢或好处，这份回应是 reward。也可以说做某事本身带来的满足感。',
 '经法语 reward、rewarder 等看顾、酬报词，较早接 re- 与 warder 看守、关注的材料，属于日耳曼看顾词族。英语把注意、回应等历史意义发展成报答、奖赏。',
 [['法语 rewarder 等；较早看顾词族','看顾、重视 → 酬报'],['英语 reward','因行为、付出得到的奖赏、回报；奖励']],
 'a reward for information 提供信息的酬金；reward someone for doing 为某事奖励某人；the rewards of teaching 教学带来的回报；as a reward 作为奖励。',
 'offer a reward；hard work and its rewards。','award 常是评选、正式决定授予的奖；reward 更广，可说酬金、善行回报或工作中的满足。不是每份 reward 都有颁奖仪式。',
 ('They offered a reward for the return of the missing dog.','他们悬赏寻找走失的狗。'),('Seeing students gain confidence is one of the rewards of teaching.','看到学生变得自信，是教学带来的回报之一。'),sources=['https://en.wiktionary.org/wiki/reward#English'])
W('garage','英 /ˈɡærɑːʒ/、/ˈɡærɪdʒ/；美 /ɡəˈrɑːʒ/','车库；汽车修理厂、汽修店；把车存入车库',
 '给车一个能停放、遮护的地方，是 garage。某些地方的 garage 还负责修车，因此不能只凭这个词就认定是住宅车库。',
 '借法语 garage，来自 garer 遮护、停放、使船靠泊等动词及名词材料；较早接法语保护相关词，再联系日耳曼看顾、保护词族。',
 [['法语 garer → garage','遮护、安置 → 存放、遮护车辆的地方'],['英语 garage','车库；汽车修理业务场所；存车动词']],
 'park in the garage 停在车库；take the car to the garage 把车送去汽修店；a garage door 车库门；a parking garage 停车楼，常见美式。',
 'a local garage；a detached garage。','美式常把重音放后，英式常把重音放前，也有不同末音形式。the car is at the garage 在日常语境可能说车在修理厂，不是一定已经回家停好。',
 ('We keep our bicycles in the garage.','我们把自行车放在车库里。'),('The garage repaired the car by Friday.','汽修店到星期五就把车修好了。'),sources=['https://www.etymonline.com/word/garage','https://en.wiktionary.org/wiki/garage#English'])
W('colonel','英 /ˈkɜːnəl/；美 /ˈkɝːnəl/','上校；Colonel：相应称谓',
 '把士兵排成纵队 column，再想起指挥这类部队的军官。这是名称的老联系；今天 colonel 是军衔名称。',
 '经法语 coronel 等接意大利语 colonnello、colonnella 相关军官名称，上接 colonna 纵队、柱子及拉丁 columna。法语曾将一个 l 异化为 r；英语后来拼写靠回意大利语层，读音却保留 r 那层。',
 [['拉丁 columna → 意大利语纵队、军官词','柱子、纵列 → 相应部队的军官'],['法语 coronel 等 → 英语 colonel','拼写较后恢复 l；读音保留较早 r 形式']],
 'Colonel Smith 史密斯上校；a retired colonel 退役上校；the rank of colonel 上校军衔；缩写常见 Col.。',
 'serve as a colonel；speak to the colonel。','colonel 通常与 kernel 同音，不能按三个可见元音逐个读成三音节。现代军衔的具体职责随军队而异，基本中文对应上校。',
 ('The colonel addressed the soldiers before they left.','上校在士兵出发前向他们讲话。'),('She interviewed a retired colonel for the documentary.','她为纪录片采访了一位退役上校。'),sources=['https://www.etymonline.com/word/colonel','https://en.wiktionary.org/wiki/colonel#English'])
W('menu','英 /ˈmenjuː/；美 /ˈmenjuː/','菜单；可选项目清单；菜单栏中的选项表',
 '把能选的东西逐项列出来，客人选菜，电脑用户选操作。menu 的日常画面是这份可选择的项目表。',
 '借法语 menu 菜单，较早形容词指小的、细分的，来自拉丁 minutus 细小的、分成小份的。法语中接细列的内容发展出菜目清单，后英语扩到计算机选项。',
 [['拉丁 minutus → 法语 menu','细小、细分的 → 逐项列出的内容、菜目'],['英语 menu','餐饮菜单；可选项目表；计算机菜单']],
 'look at the menu 看菜单；on the menu 菜单上有的；a lunch menu 午餐菜单；a drop-down menu 下拉菜单；the main menu 主菜单。',
 'choose from the menu；a menu of options。','menu 是让你查看、选择项目的表；restaurant bill 是吃完后的账单。电脑上的 menu 同样提供选择，不是只指餐厅页面。',
 ('Could we see the menu, please?','请给我们看看菜单好吗？'),('Choose “Print” from the menu.','从菜单中选择“打印”。'),sources=['https://en.wiktionary.org/wiki/menu#English'])
W('fee','/fiː/','费用、服务费、报名费等；酬金',
 '为一项服务、许可或参加资格付的钱，常是 fee：上一门课、办一项手续、请人提供专业服务，都可能有相应费用。',
 '接古英语 feoh 牲畜、财产、钱财等材料，也与法语封地、占有相关词有合流影响。牲畜曾是财富的一种体现；这条日耳曼语词与拉丁 pecu 牲畜有更远同源关系。',
 [['古英语 feoh 及相关日耳曼语材料','牲畜、财产、钱财、支付'],['中古、现代英语 fee；法语相关词影响','服务或资格等所收取的费用、酬金']],
 'an entrance fee 入场费；tuition fees 学费；a membership fee 会费；a service fee 服务费；pay a fee 付费。',
 'charge a fee；an annual fee。','fee 常用于明确的一项服务、资格等收费；price 更广地说商品、服务价格。wages、salary 则通常说雇佣关系中的工资，不能都直接换成 fee。',
 ('The museum charges a small entrance fee.','博物馆收取少量入场费。'),('The course fee includes all the materials.','课程费用包含全部材料。'),sources=['https://www.etymonline.com/word/fee','https://en.wiktionary.org/wiki/fee#English'])
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_uw',ROOTS,WORDS)
 extend_lessons()
