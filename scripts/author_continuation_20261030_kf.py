"""Tale, access, rage, skip and tiger."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
T=[['古英语 talu → 中古英语 tale','叙述、计数等；与 tell 有历史联系'],['现代 tale','讲出的故事、遭遇；特定语境也可说谎话']]
W('tale','/teɪl/','故事、叙述；说法、传闻〔有时含不可信之意〕',
 '把一连串事情讲给别人听，就是 a tale。它常有讲故事的色彩；是真是假，要看修饰和场景。',
 '古英语 talu 经中古英语 tale 传下，旧义兼有叙述、计数等，与 tell 有历史联系。不能把现代 tale 每次都译成谎话。',T,
 'a fairy tale 童话，a cautionary tale 警示故事，a tale of adventure 冒险故事，tell tales 可指告状、说人闲话。',
 'a fairy tale；a cautionary tale；a tale of adventure。',
 'tale 与 tail 尾巴同音；story 的日常范围更广，tale 常强调讲述出来的一段故事或遭遇。',
 ('Grandpa told us a tale about a lost sailor.','爷爷给我们讲了一个迷路水手的故事。'),('The film is a cautionary tale about ambition.','电影讲了一个关于野心的警示故事。'))
R('B3571','把事情讲成故事，扩到民间故事与泄露迹象','TALE：讲出来的一段事情','tale → folktale 民间故事；telltale 可泄露秘密、暴露情况。',
 '先记 tale 的讲述感，再分别看 folk 说流传群体、tell 说把情况透露出来。',
 'talu → tale；folk + tale → folktale；tell + tale → telltale。',
 [['基础与民间故事','tale · folktale'],['把情况泄露出来','telltale']],
 'tale 不总是假的；tail 是尾巴；telltale signs 是透露实际情况的迹象。',
 'The old folktale became a cautionary tale for the children.\n\n这个古老民间故事成了提醒孩子们的警示故事。','tale folktale telltale')
R('B2443','能接近、进入、使用或理解','ACCESSIBLE：通路走得通，也让人用得上、看得懂','accessible → accessibility；inaccessible 不能接近、难懂等。',
 '大楼入口、网页功能、文章语言，都可能存在能不能顺利接触或使用的问题。无障碍语境还要看具体使用者的需要。',
 'access 接近、进入 + -ible 相应性质；-ity 性质名词；in- 否定。',
 [['性质、名词与否定','accessible · accessibility · inaccessible']],
 'accessible 不只是免费；易到达、易理解、适合使用者是不同维度。',
 'The guide makes the exhibition accessible to more visitors.\n\n这本指南让更多参观者能理解展览。','accessible accessibility inaccessible')
G=[['拉丁 rabiēs → 晚期拉丁 rabia → 古法语 rage','狂怒、愤怒'],['rage → enrage、raging 等','激怒；猛烈进行、强烈的状态'],['另一条来源：ultrā 越过 → 古法语 outrage','越过合理界限 → 暴行、令人愤慨之事与愤慨']]
W('rage','/reɪdʒ/','狂怒；猛烈进行、肆虐；风靡〔固定搭配〕',
 '怒气非常强，像压不住地爆出来，是 rage。大火、暴风、激烈争论持续猛烈，也可以 rage；all the rage 则转成一时大热的风尚。',
 '经中古英语、古法语 rage，来自晚期拉丁 rabia、拉丁 rabiēs。名词与动词相互关联，强烈、失控的形象扩到自然力量、争论等。',G[:2],
 'in a rage 勃然大怒，fly into a rage 突然发怒，a fire rages 大火肆虐，all the rage 风靡一时。',
 'in a rage；fly into a rage；all the rage。',
 'anger 范围更广，rage 通常强调猛烈。all the rage 是固定流行义，不是所有人都很愤怒。',
 ('He flew into a rage when he saw the broken model.','看到模型坏了，他勃然大怒。'),('Those little cameras were all the rage that summer.','那个夏天，那种小相机风靡一时。'))
W('raging','/ˈreɪdʒɪŋ/','狂怒的；猛烈、肆虐的；极强烈的',
 '人可以怒不可遏，火可以猛烈燃烧，讨论可以争得正激烈。raging 把 rage 的强度留在形容词里。',
 'rage + -ing，去 e。既可作动词分词，也固定为形容词，形容怒气、自然力量、争论等正在强烈进行。',G[:2]+[['rage + -ing → raging','处于猛烈、强烈活动的状态']],
 'a raging fire 熊熊大火，a raging storm 猛烈暴风雨，a raging debate 激烈争论。',
 'a raging fire；a raging storm；a raging debate。',
 'raging 不只形容发火的人。a raging debate 强调争论激烈，不能据此判断哪一方正确。',
 ('A raging storm kept the boats in the harbor.','猛烈的暴风雨让船留在港里。'),('The proposal sparked a raging debate.','提案引发了一场激烈争论。'))
W('enrage','/ɪnˈreɪdʒ/，也读 /enˈreɪdʒ/','激怒、使大怒',
 '某件事把人的情绪推到 rage 的程度：不是略微不高兴，而是惹得非常生气。',
 '来自古法语 enrager、enragier，现代对应 en- 使进入某状态 + rage。',G[:1]+[['en- + rage → enrage','使进入狂怒、激怒']],
 'enrage someone 激怒某人，be enraged by／at 因……大怒。多用于很强的反应。',
 'enrage someone；be enraged by something。',
 'annoy 可以是轻微烦扰，enrage 的强度大得多；它是使人发怒的动词，rage 则可直接说发怒。',
 ('The deliberate insult enraged her.','那句故意的侮辱把她激怒了。'),('The unfair decision enraged the spectators.','不公平的判决激怒了观众。'))
W('enraged','/ɪnˈreɪdʒd/，也读 /enˈreɪdʒd/','被激怒的、非常愤怒的',
 '某事已经把人惹怒，enraged 描写这个人的强烈情绪状态。',
 'enrage + -ed，保留一个 e，词尾 /d/。它有过去分词来源，也作表示状态的形容词。',G[:1]+[['enrage → enraged','激怒 → 被激怒、处于大怒状态']],
 'an enraged customer 愤怒的顾客，enraged at the news 听到消息大怒。',
 'an enraged customer；enraged by the remark。',
 'enraged 看人的反应状态；enraging 看某事令人愤怒的性质。',
 ('The enraged customer demanded an explanation.','愤怒的顾客要求解释。'),('She was enraged by the false accusation.','那项不实指控令她非常愤怒。'))
W('outrage','/ˈaʊtreɪdʒ/','愤慨、义愤；暴行、令人愤慨之事；使愤慨',
 '人觉得某事越过了可以接受的界限，会愤慨；那件过分的事本身也可以叫 an outrage。现代词里，事件与情绪互相照应。',
 '古法语 outrage、oultrage 上接通俗拉丁 *ultrāticum，来自 ultrā 越过。后来被重新理解为 out + rage，影响现代形式、联想；真实起点并非英语两个词相加。',G[2:]+[['越界、过分的行为 → 现代 outrage','暴行、恶劣之事 → 由此产生的愤慨']],
 'public outrage 公众愤慨，spark outrage 引发愤慨，an outrage against decency 有违基本体面的恶劣行为。This is an outrage! 太不像话了！',
 'public outrage；spark outrage；an outrage。',
 'rage 强调猛烈怒气；outrage 常带认为事情不公、过分、不可接受的判断。二者现代意义相邻，但直接词源不同。',
 ('The cruelty described in the report caused public outrage.','报告描述的残酷行为引起公众愤慨。'),('The passengers called the treatment an outrage.','乘客称这种对待方式太不像话。'),sources=['https://en.wiktionary.org/wiki/outrage#English','https://www.etymonline.com/word/outrage'])
W('outrageous','/aʊtˈreɪdʒəs/','骇人、令人愤慨的；离谱、过分的；大胆出格的',
 '行为过分到令人愤慨，是 outrageous；价格高得离谱、服装大胆出格，也可借同一越界感表达。具体褒贬看对象。',
 '来自古法语、盎格鲁法语 outrageus 等，现代对应 outrage + -ous。来源中的越过界限感，在离谱、出格等意义里仍很好理解。',G[2:]+[['outrage → 法语 outrageus 等 → outrageous','越界、过分 → 令人愤慨、离谱或大胆出格']],
 'an outrageous price 离谱的价格，outrageous behavior 过分行为，an outrageous costume 大胆出格的服装。',
 'an outrageous price；outrageous behavior。',
 'outrageous 不只是一点 unusual；它通常有明显超出常规、可接受程度的语气。有时故意夸张来赞叹大胆。',
 ('They wanted an outrageous price for a tiny room.','一间小屋，他们居然要了个离谱的价钱。'),('The actor arrived in an outrageous costume.','演员穿着一套大胆出格的服装到场。'))
R('B3960','猛烈怒气与肆虐状态，另分清越界义的 outrage','RAGE：强烈到压不住；OUTRAGE 另有越界来源','rage → raging；enrage → enraged；outrage → outrageous 是单列的不同来源对照。',
 '两条线今天都能说愤怒，所以特别容易混。学习时一边看强烈情绪，一边看被认为越界、过分的事件。',
 'rabia／rabiēs → rage；en- 使，-ed 状态；ultrā → outrage，-ous 性质。',
 [['怒气、猛烈状态与激怒','rage · raging · enrage · enraged'],['不同来源的越界、愤慨词','outrage · outrageous']],
 'outrage 历史上不是 out + rage；all the rage 是风靡一时；outrageous 可说离谱价格、出格服装。',
 'The outrageous charge enraged the customers and sparked public outrage.\n\n离谱的收费激怒了顾客，引发公众愤慨。','rage raging enrage enraged outrage outrageous')
K=[['中古英语 skippen，联系北日耳曼语跳跃形式','轻跳、跳着走'],['动作的扩展','跳过一部分、不参加；石头在水面弹跳'],['不同来源的容器名与简称','skip 废料斗另接筐、量器词；队长义可短自 skipper']]
W('skip','/skɪp/','蹦跳；跳过、略过；不参加；废料斗〔英式〕',
 '脚轻轻跳着前进，是 skip；做事时越过一项，也像跳了一格。英式英语的 a skip 废料斗，则来自另一条容器名称。',
 '跳跃义经中古英语 skippen，通常联系斯堪的纳维亚语言。废料斗义经 skep 等筐、量器形式；部分队长义又是 skipper 的简称。',K,
 'skip breakfast 不吃早饭，skip a chapter 跳过一章，skip class 不去上课，skip stones 打水漂；hire a skip 租废料斗。',
 'skip a chapter；skip breakfast；skip stones；hire a skip。',
 'skip 可有意略过，miss 也常说没赶上、无意漏掉。skip 的容器义与跳跃义要分开认。',
 ('You can skip the introduction and start with chapter one.','你可以略过引言，从第一章开始。'),('The builders put the broken tiles in a skip.','工人把碎瓷砖放进废料斗里。'))
W('skipjack','/ˈskɪpdʒæk/','鲣鱼等鱼的俗名；切萨皮克湾一类传统帆船',
 '现代最常在 skipjack tuna 里见到，通常指鲣鱼。名称中的 skip 有跳跃形象，jack 是可泛用在人、物和动物名称里的成分。',
 'skip 跳 + jack。历史上先有形容轻浮家伙的旧用法，后来用于会跳跃的鱼，也形成特定帆船名称。不是所有这些对象属于同一生物类别。',K[:1]+[['skip + jack → skipjack','跳跃相关旧称 → 鱼名；另有传统帆船名']],
 'skipjack tuna 鲣鱼，a skipjack boat 传统 skipjack 帆船。不同地区单说 skipjack 可能有不同鱼类所指。',
 'skipjack tuna；a skipjack boat。',
 'skipjack tuna 是具体鱼名，不能把所有 tuna 都改叫 skipjack；名称也不表示这种鱼一直在跳。',
 ('The label lists skipjack tuna as the main ingredient.','标签把鲣鱼列为主要原料。'),('The museum displays a model of a traditional skipjack.','博物馆展出一艘传统 skipjack 帆船的模型。'),sources=['https://en.wiktionary.org/wiki/skipjack#English','https://www.etymonline.com/word/skipjack'])
R('B4334','跳跃、跳过，与不同来源的容器及船长词对照','SKIP：轻轻越过一步，再比喻略过一项','skip → skipjack；skipper 的船长线来自 ship 的荷兰语同源词，与跳跃线分开。',
 '现代 skip 有好几条来源：跳跃、容器、队长简称。按真实来源分开，就不用把废料斗硬想成跳动的东西。',
 'skippen → 跳跃 skip；skep 等 → 容器 skip；schipper → skipper、简称 skip。',
 [['基础跳跃与容器同形词','skip'],['鱼、船的名称','skipjack'],['另一路船长名','skipper']],
 'skip class 不去上课；a skip 可是废料斗；船长 skipper 不宜硬拆成跳的人。',
 'We skipped one stop and watched a skipjack boat from the pier.\n\n我们略过一站，从码头看了一艘传统 skipjack 帆船。','skip skipjack skipper')
H=[['希腊 tigris → 拉丁 tigris','虎；更早或联系伊朗语形式，解释有不确定处'],['古英语及法语路径 → 中古英语 tigre → tiger','英语虎的名称'],['法语 tigresse／英语 tiger + -ess','雌虎']]
W('tiger','英 /ˈtaɪɡə/；美 /ˈtaɪɡər/','虎；凶猛、干劲足的人〔比喻〕',
 '先记亚洲的大型条纹猫科动物。形容一个人像 tiger，通常借它凶猛、劲头十足的形象；纸老虎则借反差说外强中干。',
 '中古英语 tigre，既有古英语 tigras 的传承，也受法语 tigre 影响，二者上接拉丁 tigris、希腊 tigris。更早或来自伊朗语，尖、箭的联系尚不能当成确定命名故事。',H[:2],
 'a Bengal tiger 孟加拉虎，a tiger cub 幼虎，a paper tiger 纸老虎。tiger 本身通常可泛指雌雄，需强调雌性时用 tigress。',
 'a tiger cub；a Bengal tiger；a paper tiger。',
 '带 tiger 的动物俗名可能按条纹、形象取名，并不都是真正的虎。Tasmanian tiger 是袋狼的旧称。',
 ('A tiger moved silently through the tall grass.','一只虎悄无声息地穿过高草。'),('The cub stayed close to the adult tiger.','幼虎紧跟在成年虎身边。'),sources=['https://en.wiktionary.org/wiki/tiger#English','https://www.etymonline.com/word/tiger'])
W('tigress','/ˈtaɪɡrəs/，也读 /ˈtaɪɡrɪs/','雌虎',
 '需要把性别说清楚时，用 tigress 指雌虎。这里 -ess 承担雌性名称的作用。',
 '来自法语 tigresse，现代对应 tiger + -ess。不是简单把 tiger 后面原样再加一段拼成 tigeress，而是已有固定词形。',H[1:],
 'a tigress and her cubs 雌虎和幼虎，a young tigress 一只年轻雌虎。',
 'a tigress and her cubs；a young tigress。',
 'tiger 可泛指虎，tigress 专指雌虎。幼虎仍叫 cub，不因母亲是 tigress 就改后缀。',
 ('The tigress rested while her cubs played nearby.','雌虎休息着，幼虎在旁边玩。'),('The researchers recognized the tigress by her stripes.','研究人员通过条纹认出了那只雌虎。'))
R('B2560','虎的动物名称与性别词、形象比喻','TIGER：完整动物名，TIGRESS 明确说雌虎','tiger → tigress；比喻借凶猛、力量或外形。',
 '这组重点是把完整借词、真实动物和比喻分清，不必为每个现代字母另找词根。',
 'tigris → 古英语／法语路径 → tiger；法语 tigresse 对应 -ess 雌性词形。',
 [['动物与性别名称','tiger · tigress']],
 '虎的远源解释有不确定处；tiger 可泛指雌雄；带 tiger 的俗名不都属于虎。',
 'The tigress watched her cubs from the shade.\n\n雌虎在阴凉处看着幼虎。','tiger tigress')
if __name__=='__main__':save('continuation_20261030_kf',ROOTS,WORDS)
