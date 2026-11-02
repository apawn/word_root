"""Waists, arches, jaws, timber, vampires and algorithms."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
Wa=[['中古英语 wast、waste → waist','身体中部、衣服腰部；可能联系更早身材、生长词，来源未定'],['waist + -ed、line、band、coat','腰部形状、腰线与相关衣物']]
W('waist','/weɪst/','腰、腰部；衣服的腰部',
 '胸部以下、髋部以上，衣服常在这里收窄或系腰带，这是 waist。衣服的腰部设计可以比自然腰位更高或更低。',
 '接中古英语 wast、waste，可能联系古英语及日耳曼身材、生长相关词，但更早来源未定。现代多用 waist 拼写，与同音 waste 区分。',Wa,
 'around the waist 围着腰，a narrow waist 细腰，a dress with a fitted waist 腰部合身的连衣裙。',
 'around the waist；at the waist；a waist measurement。',
 'waist /weɪst/ 与 waste 浪费同音，意义、历史不同；腰部与臀部 hip 的位置也不同。',
 ('The belt fitted comfortably around her waist.','腰带围在她腰上，松紧舒服。'),('The dress is gathered at the waist.','连衣裙在腰部打了褶。'),sources=['https://en.wiktionary.org/wiki/waist#English','https://www.etymonline.com/word/waist'])
W('waisted','/ˈweɪstɪd/','具有某种腰形、腰位的；中间收窄的',
 '一件衣服怎样收腰、腰位在哪里，可以用 waisted 这部分来说明。the waisted shape 则突出中间比两边窄。',
 'waist + -ed，名词后表示带有某种特征；/t/ 后 -ed 读 /ɪd/。常出现于 high-waisted、low-waisted 等组合。',Wa[:1]+[['waist + -ed → waisted','有某种腰形、腰位；中段收窄']],
 'a waisted jacket 收腰夹克，high-waisted trousers 高腰裤；这些组合的连字符是正常写法。',
 'a waisted shape；a waisted jacket。',
 '-ed 在形容词 waisted 里说明具有的形状，不必把它理解成某人先做过一个“腰”的动作。',
 ('The jacket has a gently waisted shape.','夹克的轮廓略微收腰。'),('She chose a waisted coat for the occasion.','她为这个场合选了一件收腰外套。'))
W('waistline','/ˈweɪstlaɪn/','腰线；腰围',
 '绕腰画一圈，是身体 waistline；沿衣服收腰位置画一圈，是服装 waistline。谈一个人的腰线时，也常把周长腰围一起算进来。',
 'waist 腰 + line 线。由腰部周围的线，扩展到其周长，以及衣服腰部设计的位置。',Wa[:1]+[['waist + line → waistline','腰部轮廓、周长；衣服腰线']],
 'a high waistline 高腰线，measure the waistline 测腰围，a dress with a defined waistline 腰线明确的连衣裙。',
 'a fitted waistline；a high waistline。',
 'waistline 在服装里可说设计位置；实际身体腰围则是测量数值，两种用法不必落在同一高度。',
 ('The dress has a high waistline.','这条裙子采用高腰线设计。'),('The tailor measured the waistline before altering the trousers.','裁缝改裤子前量了腰围。'))
R('B3323','身体中段的腰，形成腰线、收腰性质与衣物名称','WAIST：衣服在身体中间收住的地方','waist → waisted、waistline；waistband 腰带部位，waistcoat 马甲。',
 '身体部位先提供位置，再看服装如何剪裁、围住或覆盖它。腰线是设计，腰围是量度，-ed 说明具有的外形。',
 'wast、waste → waist，远源未定；-ed 有……形状，line 线，band 带，coat 衣物。',
 [['腰部、形状及量度','waist · waisted · waistline'],['服装复合','waistband · waistcoat']],
 'waist 与 waste 同音不同义；服装腰线不一定就是身体自然腰位。',
 'The waistline of the waisted coat sits just above the waistband.\n\n收腰外套的腰线位于裤腰带部位稍上方。','waist waisted waistline waistband waistcoat')
Ar=[['拉丁 arcus 弓、弧 → 法语 arche → 英语 arch','弓形、建筑拱；动词拱起'],['另一路：希腊首要、领导的 arch- → arch 形容词','从首要到旧日大坏蛋等搭配，发展出狡黠调皮义']]
W('arch','英 /ɑːtʃ/；美 /ɑːrtʃ/','拱、拱门、弓形；使拱起；狡黠调皮的',
 '一条弯曲结构跨过中间空处，是 arch：石拱桥、拱门、足弓都能帮助记。an arch smile 却走另一条词源，形容像明知什么却故意逗人的狡黠笑意。',
 '拱义经古法语 arche 接拉丁 arcus 弓、弧，名词又作拱起的动词。调皮形容词另由 arch- 首要、主要的成分发展，不能从石拱形状推出。',Ar,
 'a stone arch 石拱，the arch of the foot 足弓，arch one’s back 弓起背，an arch smile 狡黠的笑。',
 'a stone arch；arch an eyebrow；an arch smile。',
 'arch 拱的 ch 常读 /tʃ/；architecture 的 ch 读 /k/，不能看同一字母串就复制发音与来源。',
 ('They walked under a stone arch.','他们从一道石拱下走过。'),('The cat arched its back.','猫弓起了背。'),('She gave him an arch smile.','她朝他狡黠地笑了笑。'))
R('B3502','弓形拱起，与狡黠形容词的另一来源分开','ARCH：弯曲结构跨过空处，脚底也有足弓','arch → archway；an arch smile 另接首要前缀的旧义发展。',
 '拱门、足弓、猫弓背共享形状；调皮的笑意则不能凭形状解释。用法在同一页对照，来源各自保留。',
 'arcus → arche → arch；way 通道形成 archway；形容词 arch 另由 arch- 发展。',
 [['拱形与通道','arch · archway']],
 'arch 的常见 /tʃ/ 与 architecture 的 /k/ 分清；形容词狡黠义另有来源。',
 'The archway was supported by a stone arch.\n\n那道拱形通道由石拱支撑。','arch archway')
Ja=[['中古英语 jawe、jowe → jaw','颌、下颌一带；法语借入与本族词等来源有争论'],['颌部形状、动作 → 工具夹爪、说话等','jawline 轮廓，jawed 特征，lockjaw 张口困难，jawbreaker 硬糖或难发音词']]
W('jaw','英 /dʒɔː/；美 /dʒɔː/','颌、下颌；工具夹爪；〔口语〕喋喋说、训斥',
 '嘴巴上下开合、牙齿附着的骨架区域，是 jaw。老虎钳两侧合拢夹住东西，也借颌的形状和动作叫 jaws。',
 '中古英语 jawe、jowe 指颌、脸下部，更早有法语借入、本族词等不同解释。由口部形状扩展到夹持工具；说话、训斥动词承嘴部动作比喻。',Ja,
 'the upper jaw 上颌，the lower jaw 下颌，the jaws of a vice 台钳夹爪，someone’s jaw dropped 惊得张大嘴。',
 'the lower jaw；jaw muscles；jaws of a vice。',
 'chin 下巴是脸部外观部位，jaw 更重颌骨、颌部；两者有关但不完全相同。',
 ('His jaw dropped when he saw the bill.','看到账单，他惊得张大了嘴。'),('The jaws of the vice held the wood firmly.','台钳的夹爪牢牢夹住木头。'))
W('jawline','英 /ˈdʒɔːlaɪn/；美 /ˈdʒɔːlaɪn/','下颌线、下颌轮廓',
 '沿脸侧往下，到下颌边缘勾出的一条轮廓，就是 jawline。jaw 是骨架区域，line 让你注意外侧边界。',
 'jaw 颌、下颌 + line 线，复合名词。由身体部位限定轮廓所在位置。',Ja[:1]+[['jaw + line → jawline','下颌形成的脸部边缘轮廓']],
 'a defined jawline 清晰的下颌线，a strong jawline 鲜明有力的下颌轮廓。',
 'a defined jawline；along the jawline。',
 'jawline 是轮廓线，jawbone 是骨头；外观描述与骨骼结构各有重点。',
 ('The portrait emphasised her jawline.','肖像突出了她的下颌轮廓。'),('A shadow ran along his jawline.','阴影沿着他的下颌线铺开。'))
W('jawed','英 /dʒɔːd/；美 /dʒɔːd/','有颌的；具有某种颌形的',
 '有 jaw，或者颌部呈某种形状，就是形容词 jawed。jawed vertebrates 说有颌脊椎动物，square-jawed 则在描述方下颌外形。',
 'jaw + -ed，名词后表示带有该结构、特征，末尾读 /d/。jaw 也可作说话等动词，其过去式同形，要看句法。',Ja[:1]+[['jaw + -ed → jawed','带有颌或特定颌部形状']],
 'jawed vertebrates 有颌脊椎动物，a square-jawed figure 下颌方正的人物。',
 'jawed vertebrates；a broad-jawed animal。',
 '这个 -ed 形容词可以表示具有结构，不要求先发生一个“装上颌”的动作。',
 ('The diagram compares jawed and jawless vertebrates.','图示比较了有颌与无颌脊椎动物。'),('The novel describes a square-jawed detective.','小说描写了一位下颌方正的侦探。'))
W('lockjaw','英 /ˈlɒkdʒɔː/；美 /ˈlɑːkdʒɔː/','牙关紧闭、张口受限；〔旧俗称〕破伤风',
 '颌部仿佛被锁住，嘴难以张开，lock + jaw 直接给出这个画面。历史上它也常作破伤风俗称，但张口受限并非只有这一种原因。',
 'lock 锁住 + jaw 颌。由颌部紧闭、张口困难的表现形成名称；破伤风因可能出现这种表现而有相关俗称。',Ja[:1]+[['lock + jaw → lockjaw','颌仿佛锁住的张口困难；也作破伤风俗称']],
 'develop lockjaw 出现牙关紧闭，lockjaw／trismus 张口受限；临床语境需看具体所指。',
 'lockjaw symptoms；the term lockjaw。',
 'lockjaw 可以描述症状，也可见作破伤风俗称；不能据这一个词替实际情况确定病因。',
 ('The leaflet explains lockjaw as difficulty opening the mouth fully.','说明册把 lockjaw 解释为难以充分张开嘴。'),('The article notes that lockjaw can have several causes.','文章指出，张口受限可能有多种原因。'),sources=['https://en.wiktionary.org/wiki/lockjaw#English','https://www.mskcc.org/cancer-care/patient-education/trismus','https://www.cdc.gov/tetanus/hcp/clinical-overview/'])
W('jawbreaker','英 /ˈdʒɔːbreɪkə/；美 /ˈdʒɔːbreɪkər/','大硬糖；难发音的长词',
 '糖太硬，像要把颌咬坏；词太长，像把嘴绕不过来。jawbreaker 用夸张方式给这两种东西命名。',
 'jaw 颌 + breaker 弄坏者、使断裂的东西，复合名词。糖果、难读词义都借颌部吃力来夸张。',Ja[:1]+[['jaw + breaker → jawbreaker','硬得难咬的糖；长得难读的词']],
 'a colourful jawbreaker 彩色大硬糖，a scientific jawbreaker 难念的科学长词。',
 'a jawbreaker candy；a real jawbreaker of a word。',
 'jawbreaker 的比喻不声称每次一定伤到颌；难发音义也不是字数长就自动适用。',
 ('The shop sold colourful jawbreakers in glass jars.','店里把彩色大硬糖装在玻璃罐里售卖。'),('That chemical name is a real jawbreaker.','那个化学名称真够拗口。'))
R('B3424','颌的部位与开合动作，发展轮廓、工具与固定比喻','JAW：嘴的骨架能开合，夹爪也能这样夹住','jaw → jawline、jawed、jawbone；lockjaw 看锁住画面，jawbreaker 看吃力夸张。',
 '骨头、外侧轮廓、有没有颌，是不同描述层次。夹爪借动作，张口困难借锁住，大硬糖与拗口词借颌部吃力。',
 'jawe、jowe → jaw，远源争论保留；line 轮廓，-ed 有……，bone 骨，lock 锁，breaker 破坏者。',
 [['部位、骨骼、轮廓与性质','jaw · jawbone · jawline · jawed'],['锁住与使颌吃力的复合','lockjaw · jawbreaker']],
 'lockjaw 不能单凭一个词确定病因；jawline 轮廓与 jawbone 骨头分清。',
 'The drawing shows the jawbone beneath the jawline.\n\n图示画出了下颌轮廓下方的颌骨。','jaw jawbone jawline jawed lockjaw jawbreaker')
Ti=[['古英语 timber 建筑、材料 → 中古英语 tymber → timber','造房材料 → 木材、梁木'],['timber + -ed、line、land','有林或木构的；树木生长界线；林地']]
W('timber','英 /ˈtɪmbə/；美 /ˈtɪmbər/','木材、用材林木；大梁、梁木',
 '原本和造房子有关，后来聚焦造房所用的木料。树还站着可当 timber 看用材来源，进了屋顶又可当承重梁。',
 '承古英语 timber，经中古英语 tymber 等延续，联系日耳曼及更远建造词族。旧建筑、材料义发展出木材、梁木等用法。',Ti,
 'building timber 建筑木材，timber beams 木梁，standing timber 立木；Timber! 也曾是提醒树正在倒下的喊声。',
 'timber beams；a timber frame；standing timber。',
 'wood 是更广的木、木质材料；timber 常把树木、木料当建筑等用途资源来谈。美式 lumber 也常指加工木材。',
 ('The roof is supported by heavy timber beams.','屋顶由粗重木梁支撑。'),('The yard stores timber for construction.','堆场储存建筑用木材。'))
W('timbered','英 /ˈtɪmbəd/；美 /ˈtɪmbərd/','有林木的；木构的、装有木梁的',
 '一片土地上长着可用木料的树，是 timbered；一栋房屋露出木框架，也能 timbered。地形还是建筑，决定哪种形象。',
 'timber + -ed，末尾读 /d/。形容具有林木、木梁等；动词 timber 给建筑装木料的分词也可形成相应状态。',Ti[:1]+[['timber + -ed → timbered','长有林木、带木构件的']],
 'a timbered hillside 长着林木的山坡，a timbered house 木构房屋；half-timbered 常说外墙显露木框架的建筑。',
 'a timbered hillside；a timbered building。',
 'timbered land 有树，timbered building 有木构件；同一词尾描述“具有”，对象不同。',
 ('They crossed a heavily timbered valley.','他们穿过一个林木茂密的山谷。'),('The village is known for its old timbered houses.','村庄以古老木构房屋闻名。'))
W('timberline','英 /ˈtɪmbəlaɪn/；美 /ˈtɪmbərlaɪn/','林线、树木生长界线',
 '往高山上走，树越来越矮、越来越稀，最后越过树木能正常生长的界线，这条线就是 timberline。',
 'timber 林木 + line 界线。复合词按树木生长范围命名，常见高山、极地边界语境。',Ti[:1]+[['timber + line → timberline','林木生长范围的边界']],
 'above the timberline 林线以上，near the timberline 林线附近；也常与 treeline 近义使用，具体生态学定义可有区分。',
 'above the timberline；the mountain timberline。',
 'timberline 不是画在山上的实体线，也不是全球统一海拔；气候、地形等会影响位置。',
 ('The trail climbed above the timberline.','小路升到了林线以上。'),('Only low plants grew near the timberline.','林线附近只长着低矮植物。'))
R('B3450','建造材料的旧义，聚焦木材与林木资源','TIMBER：树木能成为房梁，林地、木构与林线由此命名','timber → timbered、timberline、timberland。',
 '建筑看木料、梁，土地看林木。timbered 用 -ed 说明带有这些特征；line 画生长界线，land 画林地范围。',
 'timber → tymber → timber；-ed 具有，line 界线，land 土地。',
 [['木材、性质与生长界线','timber · timbered · timberline'],['林地复合','timberland']],
 'timberline 不是全球固定海拔；timbered 要看是在描写建筑还是土地。',
 'The timbered valley lay below the timberline.\n\n林木茂密的山谷位于林线以下。','timber timbered timberline timberland')
Va=[['斯拉夫相关吸血鬼词，经匈牙利、德语、法语等 → vampire','东欧传说随相关报道进入西欧语言；更早词源有争论'],['vampire → vampiric、vampirism','吸血鬼般的性质；传说中的状态、行为及剥削比喻']]
W('vampire','英 /ˈvæmpaɪə/；美 /ˈvæmpaɪər/','吸血鬼；吸血蝙蝠；榨取他人精力、资源者',
 '传说中靠吸食活人血液延续自身的怪物，是 vampire。现代也借来形容不断耗掉别人时间、精力的人；动物名 vampire bat 则是真实蝙蝠名称。',
 '经法语 vampire、德语 Vampir 等，联系匈牙利及斯拉夫相关词。英语随东欧传说、报道借入；更早突厥语等假说有争论。',Va,
 'a vampire story 吸血鬼故事，a vampire bat 吸血蝙蝠，an emotional vampire 比喻不断耗人情绪精力者。',
 'a vampire story；a vampire bat。',
 '神话怪物、真实蝙蝠与人物比喻是不同用法；不能把某种真实疾病直接当成吸血鬼存在的证明。',
 ('The novel tells the story of a lonely vampire.','小说讲述一个孤独吸血鬼的故事。'),('The documentary showed a vampire bat.','纪录片展示了一只吸血蝙蝠。'),sources=['https://en.wiktionary.org/wiki/vampire#English','https://www.etymonline.com/word/vampire'])
W('vampiric','英 /væmˈpɪrɪk/；美 /væmˈpɪrɪk/','吸血鬼的、吸血鬼般的；榨取式的',
 '人物有尖牙、吸血能力，是故事里的 vampiric traits；制度不断榨取资源，也可借这个词作强烈比喻。',
 'vampire 去末尾 e + -ic，重音及元音随派生词变化，vampir- 接性质后缀。',Va[:1]+[['vampir- + -ic → vampiric','有吸血鬼特点的']],
 'vampiric powers 吸血鬼能力，vampiric creatures 吸血鬼般怪物，vampiric exploitation 榨取式剥削。',
 'vampiric powers；vampiric traits。',
 'vampiric 比喻是强烈评价；描述经济、关系时须有语境，不等于客观诊断标签。',
 ('The game gives the character several vampiric powers.','游戏赋予角色几种吸血鬼能力。'),('The critic described the landlord’s demands as vampiric.','评论者形容房东的要求像吸血一样榨取人。'))
W('vampirism','英 /ˈvæmpaɪərɪzəm/；美 /ˈvæmpaɪrɪzəm/','吸血鬼状态、吸血鬼行为；榨取、剥削的比喻',
 'vampire 是怪物，vampirism 则把成为吸血鬼、吸食生命的状态与行为当成一个现象来说。它在评论里也能比喻榨取。',
 'vampire 去末尾 e + -ism，构成状态、行为现象名；不是只有政治思想才能用 -ism。',Va[:1]+[['vampir- + -ism → vampirism','吸血鬼的状态、行为；榨取比喻']],
 'vampirism in fiction 虚构作品中的吸血鬼现象，the mythology of vampirism 吸血鬼传说体系。',
 'vampirism in fiction；stories of vampirism。',
 '这里讲传说、虚构与比喻用法，不把它强套成真实医学疾病名。',
 ('The essay explores vampirism in Gothic fiction.','文章研究哥特小说中的吸血鬼现象。'),('Different films explain vampirism in different ways.','不同电影对吸血鬼状态给出了不同设定。'))
R('B3743','传说中的吸取生命，现代再借作榨取比喻','VAMPIR-：靠吸取别人的生命，成为怪物与剥削形象','vampire → vampiric、vampirism。',
 '怪物、性质和状态各由词形分工。真实动物名是借传说命名，人物评论则借吸取精力的形象；这些用法不能混成一项医学事实。',
 '斯拉夫相关词经匈牙利、德语、法语等 → vampire；去 e + -ic、-ism。',
 [['怪物、性质与现象','vampire · vampiric · vampirism']],
 '吸血鬼是传说、虚构形象；vampire bat 是真实动物名，词义层次分清。',
 'The vampire’s vampiric powers explain the story’s version of vampirism.\n\n吸血鬼的能力体现了这个故事对吸血鬼状态的设定。','vampire vampiric vampirism')
Al=[['数学家 al-Khwarizmi 的名字 → 中世纪拉丁 algorismus','与其著作传播相关的计算术名称'],['古法语 algorisme、法语 algorithme → algorithm','拼写受希腊 arithmos 数的影响；意义推广到计算步骤'],['algorithm + -ic → algorithmic','按算法、与算法相关的']]
W('algorithm','英 /ˈælɡərɪðəm/；美 /ˈælɡərɪðəm/','算法；一套明确的计算、解题步骤',
 '给定输入，一步一步按明确规则处理，得到结果，就是 algorithm 的基本想法。排序数字、规划路线都可以有算法；名字却从一位数学家的名字来。',
 '接数学家 al-Khwarizmi 的名字，经中世纪拉丁 algorismus、法语相关形式进入英语。由算术计算方法扩展到算法；-th- 拼写受希腊 arithmos 数的联想影响，非原本同源拆分。',Al[:2],
 'a sorting algorithm 排序算法，a search algorithm 搜索算法，a recommendation algorithm 推荐算法；口语 the algorithm 常简称平台推荐系统。',
 'a sorting algorithm；design an algorithm；a recommendation algorithm。',
 '算法是一套明确过程，代码是某种实现；algorithm 不等于人工智能，简单排序也有算法。',
 ('The algorithm sorts the numbers from smallest to largest.','算法把数字从小到大排列。'),('A different algorithm found the same result with fewer steps.','另一种算法用更少步骤得到了同样结果。'),sources=['https://en.wiktionary.org/wiki/algorithm#English','https://www.etymonline.com/word/algorithm'])
W('algorithmic','/ˌælɡəˈrɪðmɪk/','算法的；由算法完成、控制的',
 'algorithm 是步骤本身，algorithmic 把这种方式放在系统、决策、过程前面。algorithmic recommendation 就说推荐由算法规则完成。',
 'algorithm + -ic；与算法相关的性质形容词，重音转到后面的 /rɪðm/ 一带。',Al[:2]+[['algorithm + -ic → algorithmic','与算法有关、由算法处理的']],
 'algorithmic thinking 算法思维，algorithmic recommendation 算法推荐，algorithmic decision making 算法决策。',
 'algorithmic thinking；algorithmic recommendation。',
 'algorithmic 只说明使用算法，不保证决策公平、结果正确；这些要看目标、规则、数据和验证。',
 ('The course develops algorithmic thinking through small problems.','课程通过小问题培养算法思维。'),('The platform uses algorithmic recommendation to rank videos.','平台用算法推荐给视频排序。'))
R('B4121','人名成为计算术名称，再发展成明确步骤的方法名','ALGORITHM：一套可以照着执行的步骤，词名来自人名','algorithm → algorithmic。',
 '先用排序步骤建立概念，再回看数学家名字、拉丁与法语的传播。拼写中的 -th- 是后来的联想影响，不要据此编出原始词根拆分。',
 'al-Khwarizmi → algorismus → algorisme、algorithme → algorithm；+ -ic → algorithmic。',
 [['方法与性质','algorithm · algorithmic']],
 'algorithm 不等于人工智能；algorithmic 也不自动保证公平或正确。',
 'The algorithmic approach follows an explicit algorithm.\n\n这种算法式方法遵循一套明确步骤。','algorithm algorithmic')
if __name__=='__main__':save('continuation_20261030_na',ROOTS,WORDS)
