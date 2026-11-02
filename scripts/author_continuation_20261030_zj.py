"""People and institutions: ordinary vocabulary with precise usage."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'B2595':dict(words=['person','persons'],label='person → persons：一个人到正式逐人计数',note='拉丁 persona 经法语等借入；日常复数 people 与正式 persons 并看。'),
 'B3224':dict(words=['cop','cops'],label='cop → cops：抓捕者到警察口语称呼',note='通常缩自 copper，较远的抓、取动词来源未定。'),
 'B2588':dict(words=['king','kings'],label='king → kings：君王与突出者',note='古英语 cyning 延续，与 kin 亲族同族但命名细节未定。'),
 'B2589':dict(words=['queen','queens'],label='queen → queens：王室女性、蜂后与棋子',note='古英语女人、妻子词发展成王室头衔，其他用途后借用。'),
 'C0411':dict(words=['female','females'],label='female → females：女性、雌性',note='拉丁 femella 经法语借入，拼写受 male 影响。'),
 'B2682':dict(words=['male','males'],label='male → males：男性、雄性',note='拉丁 masculus 经法语借入，与 female 不是现代加减前缀关系。'),
 'C0093':dict(words=['athlete','athletes'],label='athlete → athletes：为比赛而训练的人',note='希腊为奖赏参赛的词经拉丁、可能法语路线借入。'),
 'C1630':dict(words=['veteran','veterans'],label='veteran → veterans：有经历的人、退伍军人',note='拉丁老、经验丰富的词经法语等进入英语。'),
 'C0743':dict(words=['minister','ministers'],label='minister → ministers：服务者到部长、教牧人员',note='名词和动词各有法语、拉丁借入路线。'),
 'C0737':dict(words=['immigrant','immigrants'],label='immigrant → immigrants：从迁入地看移民',note='拉丁 immigrans 分词词族，也可能受法语形式启发。'),
 'B3266':dict(words=['town','towns'],label='town → towns：围场、聚落到城镇',note='古英语 tun 的词史，城镇和城市的区别看当地惯例。'),
 'C0571':dict(words=['hospital','hospitals'],label='hospital → hospitals：接待处到医疗机构',note='拉丁主人、客人的待客词族经法语等借入。'),
 'C1503':dict(words=['text','texts'],label='text → texts：编织成的文字、文本与短信',note='拉丁 textus 接 texere 编织，经法语等借入，短信义为现代扩展。'),
 'C0369':dict(words=['sample','samples'],label='sample → samples：抽出一小份看整体',note='与 example 同接拉丁 exemplum，经法语、中古英语等传入。'),
 'C1026':dict(words=['photograph','photographs'],label='photograph → photographs：光与影像记录',note='十九世纪希腊来源构词，名词、动词在摄影背景发展。'),
 'C0351':dict(words=['produce','producer','producers'],label='produce → producer → producers：生产、制作的承担者',note='produce 去 e 加人物 er，再有英语规则复数。'),
}
W('persons','英 /ˈpɜːsənz/；美 /ˈpɜːrsənz/','人、个人〔较正式的复数〕',
 '把一个个人分别放进计数、登记或规则里，是 persons 常见的感觉。它比日常 people 更正式，容易见于告示、说明、名单。',
 'person + -s，/n/ 后读 /z/。person 经古法语等及拉丁 persōna，早有演员面具、角色等义，再指个人；更早来源有分歧，不把声音穿过面具的故事当定论。',
 [['拉丁 persōna → 法语等 → person','面具、角色与个人的词义发展'],['person + -s → persons','正式地把若干个人分别计数']],
 'missing persons 失踪人员；persons under sixteen 十六岁以下人员；a maximum of six persons 最多六人。',
 'persons listed below 以下列出的人；persons attending the event 参加活动的人员。','日常说 two people 很自然；persons 常见于正式说明。不要因为 people 不是 person 加 s 的样子，就把普通复数都改成 persons。',
 ('The lift can carry a maximum of six persons.','这部电梯最多可乘六人。'),('All persons listed on the form must sign it.','表格上列出的所有人都必须签字。'),sources=['https://en.wiktionary.org/wiki/persons#English','https://www.etymonline.com/word/person'])
W('cops','英 /kɒps/；美 /kɑːps/','警察〔复数，口语〕；抓取、得到等〔第三人称单数，口语〕',
 '日常口语中把几名警察叫 cops，常像中文随口说警察，而不是写正式职衔。它的警察义较早和抓捕者这个称呼相连。',
 'cop + -s，/p/ 后读 /s/。警察名词通常缩自 copper，后者接 cop 抓捕 + -er；抓、取动词更远或接法语、荷兰语等，尚未定论，不是职衔首字母缩写。',
 [['cop 抓捕 → copper → cop 警察','做抓捕工作的人 → 缩短的口语称呼'],['cop + -s → cops','多名警察；动词另可作现在单数变化']],
 'call the cops 叫警察；cops and robbers 警察捉强盗的游戏；two cops 两名警察。',
 'cops at the entrance 入口处的警察；a story about cops 一个讲警察的故事。','cops 属口语，正式报告常用 police officers。动词 cop 的其他口语搭配按整体学；本词最常见的名词复数是警察。',
 ('Two cops were directing traffic near the station.','两名警察正在车站附近指挥交通。'),('The children were playing cops and robbers.','孩子们正在玩警察捉强盗的游戏。'),sources=['https://en.wiktionary.org/wiki/cops#English','https://www.etymonline.com/word/cop'])
W('kings','/kɪŋz/','国王、君王；王棋〔复数〕',
 '一位位国王是 kings；把某个领域特别突出的人比作王，也借这种居于显眼位置的身份。棋类中则按具体规则认王棋。',
 'king + -s，/ŋ/ 后读 /z/。king 继承古英语 cyning 等形式，与 kin 亲族同族；从亲族材料到君王头衔的具体命名解释有讨论，不当现代 kin 加动名词 ing。',
 [['古英语 cyning → king','亲族相关词族中的君王称呼'],['king + -s → kings','多位国王；多枚或多张王类棋子、纸牌']],
 'kings and queens 国王与女王；ancient kings 古代君王；the kings in a pack of cards 一副牌里的 K。',
 'stories about kings 君王故事；the reigns of several kings 几位国王的统治时期。','kings 作纸牌或棋子名称时不是真人在场。通常说 king of a country；具体游戏中的王如何走、如何计分，要依规则理解。',
 ('The museum displays portraits of several kings.','博物馆展出几位国王的画像。'),('The children read stories about kings and queens.','孩子们阅读有关国王和女王的故事。'),sources=['https://en.wiktionary.org/wiki/kings#English','https://en.wiktionary.org/wiki/king#English'])
W('queens','/kwiːnz/','女王、王后；蜂后、后棋、Q 牌〔复数〕',
 'queens 可以数统治国家的女王，也可以数国王的配偶王后；蜂群、棋类或纸牌又借用了这个突出的女性王室称呼。',
 'queen + -s，/n/ 后读 /z/。queen 继承古英语 cwēn，较早接女人、妻子的日耳曼材料，后来王室头衔专门化；蜂后、棋子等为后续用途。',
 [['古英语 cwēn → queen','女人、妻子 → 王室女性头衔'],['queen + -s → queens；借义扩展','多位女王、王后；蜂后、棋后或 Q 牌']],
 'kings and queens 国王和女王、王后；queen bees 蜂后；the four queens 四张 Q 牌。',
 'portraits of queens 女王、王后的画像；queens in the history book 史书中的女王、王后。','queen 是执政女王还是王后，要看人物身份。谈蜜蜂时常见 queen 或 queen bee；国际象棋里的 queen 通常译成后，纸牌里则是 Q 牌。',
 ('The exhibition includes portraits of three queens.','展览包括三位女王或王后的画像。'),('The beekeeper checks that the colonies have healthy queens.','养蜂人检查各蜂群是否有健康的蜂后。'),sources=['https://en.wiktionary.org/wiki/queens#English','https://en.wiktionary.org/wiki/queen#English'])
W('females','/ˈfiːmeɪlz/','雌性动物；女性〔复数，分类或研究语境〕',
 '按性别把个体分组时，females 指雌性这一组。日常谈动物很常见；谈人时则常带分类、统计的语气。',
 'female + -s，/l/ 后读 /z/。拉丁 femella 年轻女子等，经法语 femelle → 英语 femele、female；拼写后来受 male 影响，历史不含一个表示女性的 fe- 前缀。',
 [['拉丁 femella → 法语 femelle → female','女性、雌性词；英语拼写受 male 影响'],['female + -s → females','分类中的多个雌性或女性个体']],
 'adult females 成年雌性；males and females 雄性和雌性；females in the sample 样本中的女性或雌性。',
 'female birds 雌鸟；the females of the species 这个物种的雌性。','谈人时，日常用 women、girls 往往更自然；female 作形容词如 female athletes 很普通。研究中 males、females 常为对称分类。',
 ('The females of this bird species are smaller than the males.','这种鸟的雌鸟比雄鸟小。'),('The researchers recorded the ages of the adult females.','研究人员记录了这些成年雌性个体的年龄。'),sources=['https://en.wiktionary.org/wiki/females#English','https://www.etymonline.com/word/female'])
W('males','/meɪlz/','雄性动物；男性〔复数，分类或研究语境〕',
 '把个体按性别分组，males 是雄性或男性这一组。它突出分类身份，常见于生物描述、研究统计。',
 'male + -s，/l/ 后读 /z/。male 经古法语 masle、male 接拉丁 masculus、mas 男性、雄性；和 female 的现代相似拼写并不是前者由后者规则删前缀造出。',
 [['拉丁 masculus → 古法语 → male','男性、雄性'],['male + -s → males','多个雄性或男性个体']],
 'adult males 成年雄性、成年男性；males and females 雄性与雌性；young males 年轻雄性个体。',
 'male birds 雄鸟；males of the species 这一物种的雄性。','日常谈男性通常用 men、boys 更自然；males 更像分类用语。males 和 mails 邮件常同音，意义按句子判断。',
 ('The males of this species have bright feathers.','这个物种的雄性长着鲜艳的羽毛。'),('The study compared adult males and females.','研究比较了成年雄性和雌性个体。'),sources=['https://en.wiktionary.org/wiki/males#English','https://en.wiktionary.org/wiki/male#English'])
W('athletes','/ˈæθliːts/','运动员、竞技选手〔复数〕',
 '为参加体育竞技而训练、比赛的人，是 athletes。这个词可以涵盖很多运动项目，重点是竞技和运动能力。',
 'athlete + -s，/t/ 后读 /s/。接希腊 athlētēs 参赛者，连着 athlein 为奖赏而比赛，经拉丁 athleta、也可能经法语路线进入英语。',
 [['希腊 athlētēs → 拉丁及可能法语路线 → athlete','为奖赏参赛的人 → 运动员'],['athlete + -s → athletes','多位运动员、竞技选手']],
 'professional athletes 职业运动员；young athletes 年轻运动员；athletes competing in the event 参加项目的选手。',
 'train athletes 训练运动员；support local athletes 支持当地运动员。','广义 athlete 可说各类运动员；某些英式语境会更偏田径运动员。athletes 的 /θl/ 连读要保留，不必在中间额外插入元音。',
 ('The athletes trained together before the competition.','运动员在比赛前一起训练。'),('The event gives young athletes a chance to compete.','这项活动给年轻运动员提供了参赛机会。'),sources=['https://en.wiktionary.org/wiki/athletes#English','https://en.wiktionary.org/wiki/athlete#English'])
W('veterans','英 /ˈvetərənz/；美 /ˈvetərənz/','退伍军人；老手、资深从业者〔复数〕',
 '在某种生活或工作里经历得久、积累过经验的人，是 veterans。军队语境常指退伍军人，行业语境可指老手。',
 'veteran + -s，/n/ 后读 /z/。veteran 经法语 vétéran 等接拉丁 veterānus 老的、经验丰富的，较早 vetus 老；现代不同语境分别保留军旅和经验用途。',
 [['拉丁 veterānus → 法语等 → veteran','老的、经验丰富的 → 老兵、资深者'],['veteran + -s → veterans','多位退伍军人或行业老手']],
 'war veterans 参战老兵、退伍军人；industry veterans 行业资深人士；veterans of the campaign 参加过那次活动的老手。',
 'support for veterans 给退伍军人的支持；a team of veterans 老手组成的团队。','veteran 不只按年龄判断：年轻退伍军人也可叫 veteran。行业中的 veterans 重点是经验，不能一律译成退伍军人。',
 ('The centre offers support to veterans and their families.','中心为退伍军人及其家属提供支持。'),('The project brought together newcomers and industry veterans.','项目汇集了新人和行业资深人士。'),sources=['https://en.wiktionary.org/wiki/veterans#English','https://en.wiktionary.org/wiki/veteran#English'])
W('ministers','英 /ˈmɪnɪstəz/；美 /ˈmɪnɪstərz/','部长、大臣；教牧人员〔复数〕；照料、服侍〔第三人称单数〕',
 '承担服务、照料事务职责，是 minister 较早的线索。现代在政府里常是部长，在教会里可指教牧人员；具体职责要看机构。',
 'minister + -s，末尾读 /z/。名词经法语 ministre、拉丁 minister 助手、服务者，与 minor、minus 较小同族；动词另接 ministrer、ministrāre 的服务词。',
 [['拉丁 minister、ministrāre → 法语 → minister','助手、服务者；服务、照料 → 不同公共或宗教职责'],['minister + -s → ministers','多位部长、教牧人员；单数主语照料']],
 'government ministers 政府部长；foreign ministers 外交部长；ministers to their needs 照料他们的需要。',
 'a meeting of ministers 部长会议；ministers in local churches 当地教会的教牧人员。','政府职务中的 ministers 按国家体制译为部长、大臣等；宗教中的范围依教派而异。动词 minister to somebody 是较正式的照料用法。',
 ('The ministers met to discuss transport policy.','部长们开会讨论交通政策。'),('The book describes the work of ministers in local churches.','这本书描述当地教会教牧人员的工作。'),sources=['https://en.wiktionary.org/wiki/ministers#English','https://en.wiktionary.org/wiki/minister#English'])
W('immigrants','/ˈɪmɪɡrənts/','移入的移民〔复数〕',
 '站在接收地看，从别处搬来定居的人，是 immigrants。同一个人离开原处、来到新处，可以从不同地点的视角被描述。',
 'immigrant + -s，/t/ 后读 /s/。immigrant 接拉丁 immigrans、immigrant-，是 immigrāre 迁入的现在分词，英语也可能受法语 immigrant 启发；in- 进入在 m 前同化，接 migrāre 迁移。',
 [['拉丁 immigrāre、immigrans → immigrant','迁入 → 从接收地看的新居民'],['immigrant + -s → immigrants','多位迁入定居的人']],
 'immigrants from another country 从另一国迁来的人；recent immigrants 新近迁入的移民；immigrant families 移民家庭。',
 'immigrants settling in the city 在城里定居的移民；support for new immigrants 给新移民的支持。','immigrant 从迁入地看，emigrant 从迁出地看；migrant 更广，强调迁移。具体身份、资格不能只凭这个词判断。',
 ('The library offers language classes for recent immigrants.','图书馆为新近迁入的移民开设语言课。'),('The exhibition tells the stories of immigrants who settled in the city.','展览讲述在这座城市定居的移民的故事。'),sources=['https://en.wiktionary.org/wiki/immigrants#English','https://www.etymonline.com/word/immigrant'])
W('towns','/taʊnz/','城镇、市镇〔复数〕',
 '人们住在一起，形成有街道、商店和公共设施的聚落，是 towns 常见的画面。它的历史起点可以追到围起来的场地、庄园。',
 'town + -s，/n/ 后读 /z/。town 继承古英语 tūn 围场、庄园、聚落，经中古英语扩展为城镇；地名里的 ton 常留着这个旧词的痕迹。',
 [['古英语 tūn → town','围场、庄园 → 聚落、城镇'],['town + -s → towns','多个城镇、市镇']],
 'small towns 小镇；nearby towns 附近城镇；towns along the coast 沿海城镇。',
 'connect the towns 连接这些城镇；residents of rural towns 乡村城镇的居民。','town、city 的行政、习惯区分因地区不同，不能仅凭人口定死。go into town 常指进镇上或去商业中心，不一定离开自己的居住城市。',
 ('The railway connects several small towns.','铁路连接了几个小镇。'),('Many towns in the region hold summer festivals.','这个地区的许多城镇举办夏季节庆。'),sources=['https://en.wiktionary.org/wiki/towns#English','https://en.wiktionary.org/wiki/town#English'])
W('hospitals','英 /ˈhɒspɪtəlz/；美 /ˈhɑːspɪtəlz/','医院〔复数〕',
 '接纳需要照料的人，后来专门发展成诊疗、护理病人的机构，就是 hospitals 的历史理解线索。现代通常直接指医院。',
 'hospital + -s，/l/ 后读 /z/。接拉丁 hospitālis 待客相关、hospitāle 接待处，经古法语 hospital 等借入，较早 hospes、hospit- 联系客人与主人。',
 [['拉丁待客、接待处词 → 法语 → hospital','接待、照料之处 → 医疗机构'],['hospital + -s → hospitals','多家医院']],
 'local hospitals 当地医院；children’s hospitals 儿童医院；hospitals in the region 地区内的医院。',
 'work in hospitals 在医院工作；equipment for hospitals 医院设备。','hospital 的医疗义是历史专门化，不是现代 host 加 pital。英式说病人住院常用 in hospital，美式常用 in the hospital。',
 ('The charity provides equipment for local hospitals.','慈善机构为当地医院提供设备。'),('Several hospitals took part in the study.','几家医院参与了研究。'),sources=['https://en.wiktionary.org/wiki/hospitals#English','https://en.wiktionary.org/wiki/hospital#English'])
W('texts','/teksts/','文本、课文、典籍；短信〔复数〕；发短信〔第三人称单数〕',
 '把一个个词编排成能读的整体，是 text 的编织画面。texts 可以是课文、古代文献，也可以是手机里发来的一条条文字消息。',
 'text + -s，/t/ 后读 /s/，结尾连读 /ksts/。text 经法语 texte 接拉丁 textus 编织物、篇章，关联 texere 编织；短信及发短信是现代扩展。',
 [['拉丁 textus、texere → 法语 → text','编织 → 连贯文字、篇章'],['text + -s → texts；现代通信扩展','多份文本、短信；单数主语发短信']],
 'ancient texts 古代典籍；reading texts 阅读篇章；send texts 发短信；texts her friend 给朋友发短信。',
 'texts used in class 课堂使用的课文；short texts 简短文本、短信。','texts 作内容时可能是长篇文献，不由长度决定；手机语境才常是短信。text somebody 是给某人发文字消息，名词 a text 是一条消息。',
 ('The course includes texts from different periods.','课程包括不同时期的文本。'),('She texts her brother when she gets home.','她到家后会给弟弟发短信。'),sources=['https://en.wiktionary.org/wiki/texts#English','https://en.wiktionary.org/wiki/text#English'])
W('samples','英 /ˈsɑːmpəlz/；美 /ˈsæmpəlz/','样品、样本、试用份〔复数〕；取样、试尝〔第三人称单数〕',
 '先拿出整体里的一小份，借它观察、试用或判断，是 samples。小块食物、实验样本、产品试用装，都能按一小份理解。',
 'sample + -s，/l/ 后读 /z/。sample 与 example 同接拉丁 exemplum 例子、样本，经法语 essample、saumple 等与中古英语缩短、借入的路线发展；动词后表取样、试用。',
 [['拉丁 exemplum → 法语、中古英语 → sample','例子、样本 → 代表整体的一小份'],['sample + -s → samples','多份样品；单数主语取样、试尝']],
 'soil samples 土壤样本；free samples 免费试用装；samples the food 试尝食物。',
 'collect samples 采集样本；samples from different places 不同地点的样本。','sample 是拿出的一部分，能否代表整体要看选取方法。sample a dish 常是尝一点，不能一律理解成正式科学检测。',
 ('The students collected soil samples from three sites.','学生从三处地点采集了土壤样本。'),('The shop offers small samples of the new cheese.','商店提供少量新品奶酪供人试吃。'),sources=['https://en.wiktionary.org/wiki/samples#English','https://en.wiktionary.org/wiki/sample#English'])
W('photographs','英 /ˈfəʊtəɡrɑːfs/；美 /ˈfoʊtəɡræfs/','照片〔复数〕；拍摄照片〔第三人称单数〕',
 '让光留下一个可保存的影像，就是 photograph 的构词画面。photographs 可以是几张成品照片，也可以说某个人拍照。',
 'photograph + -s，/f/ 后读 /s/。十九世纪用希腊来源 photo- 光与 graph 记录、图像构成摄影术语，名词、动词在早期摄影背景发展；复数不把 ph 改成 v。',
 [['photo- + -graph → photograph','光 + 记录、图像 → 照片、拍照'],['photograph + -s → photographs','多张照片；单数主语拍摄']],
 'family photographs 家庭照片；old photographs 老照片；photographs birds 拍摄鸟类。',
 'take photographs 拍照；photographs of the town 城镇照片。','take photographs 是常见名词搭配；photographs the town 中 photographs 直接作动词。photo 是 photograph 的常用短形式，复数 photos。',
 ('The exhibition includes photographs of the town a century ago.','展览包括一百年前这座城镇的照片。'),('She photographs birds in the local park.','她在当地公园拍摄鸟类。'),sources=['https://en.wiktionary.org/wiki/photographs#English','https://en.wiktionary.org/wiki/photograph#English'])
W('producers','英 /prəˈdjuːsəz/；美 /prəˈduːsərz/','生产者、生产企业；制片人、制作人〔复数〕',
 '承担把成果做出来这件事的一方，是 producers。农业中是生产者，影视、音乐中则常是统筹制作的人。',
 'produce 去 e + -er → producer，再加 -s，末尾读 /z/。produce 较早接拉丁 prō- 向前 + dūcere 带领 → prōdūcere 带出来；er 命名承担生产、制作的人或机构。',
 [['拉丁 prōdūcere → produce；加 -er → producer','带出来、产出 → 生产、制作的承担者'],['producer + -s → producers','多个生产方或制作人']],
 'food producers 食品生产者；film producers 电影制片人；local producers 当地生产者。',
 'producers of the programme 节目制作人；independent producers 独立制作人、独立生产商。','电影 producer 常统筹资金、人员、制作安排，director 则是导演；具体分工因项目而异。producers 的重音随动词 produce 在后部。',
 ('Local producers sell their food at the market.','当地生产者在市场出售食品。'),('The producers worked with the director to plan the film.','制片人与导演一起筹划这部电影。'),sources=['https://en.wiktionary.org/wiki/producers#English','https://en.wiktionary.org/wiki/producer#English'])
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_zj',ROOTS,WORDS)
 extend_lessons()
