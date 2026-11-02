"""Industrial forms, tie's spellings and tiers, climate's inclined zones."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
I=[['拉丁 industria → 法语 industriel 等 → industrial','勤勉、活动词族 → 劳作的、工业的'],['现代工业分支','工业、生产方式、产业经营者与工业化']]
W('industrial','/ɪnˈdʌstriəl/','工业的、产业的；供工业使用的',
 '工厂、生产设备、成规模制造这类场景相关；industrial cleaner 则是面向工业用途的清洁品。不是形容某个人很勤奋。',
 '借法语 industriel，上接中世纪拉丁 industrialis、拉丁 industria。现代对应 industry + -al 的词族变化，但保留法语借入路径。',I,
 'industrial production 工业生产，an industrial area 工业区，industrial equipment 工业设备，the Industrial Revolution 工业革命。',
 'industrial production；an industrial area；industrial equipment；the Industrial Revolution。',
 'industrial 工业的，industrious 勤奋的；二者历史相关，今天不能把勤劳学生一律叫 industrial student。',
 ('The town grew around a large industrial area.','小镇围绕一片大型工业区发展起来。'),('The factory produces industrial equipment.','工厂生产工业设备。'),
 sources=['https://en.wiktionary.org/wiki/industrial#English','https://www.etymonline.com/word/industrial'])
W('industrially','/ɪnˈdʌstriəli/','工业上；以工业方式、通过工业生产地',
 '谈生产规模、方法或一个地区的发展时，把角度放在工业领域；不是说这个动作做得很勤快。',
 'industrial + -ly，副词接工业的现代义。词尾 l 与 -ly 相接，拼写有 ll。',I[:1]+[['industrial + -ly → industrially','在工业方面、以工业方式']],
 'industrially produced 工业生产的，industrially developed 工业发达的，industrially important 工业上重要的。',
 'industrially produced；industrially developed；industrially important。',
 'industrially 以工业方式，industriously 勤奋地；一个手工作坊可以工作勤奋，却未必工业化大批生产。',
 ('The material is now produced industrially.','这种材料现在通过工业方式生产。'),('The region became industrially important in the nineteenth century.','这个地区在十九世纪成为工业重地。'))
W('industrialist','/ɪnˈdʌstriəlɪst/','工业家、实业家',
 '建立、拥有、经营重要工业企业的人，常在商业史、产业发展报道中见到。不是工厂里的每个工人的统称。',
 'industrial + -ist，人物后缀形成工业经营者、工业家的名称；现代常用义与普通 factory worker 工人分开。',I[:1]+[['industrial + -ist → industrialist','工业企业的重要经营、所有者等']],
 'a wealthy industrialist 富有的工业家，a leading industrialist 重要工业家，nineteenth-century industrialists 十九世纪工业家。',
 'a wealthy industrialist；a leading industrialist；local industrialists。',
 'industrialist 工业家，industrial worker 产业工人；-ist 可指从事、代表领域的人，实际词义不能一律翻成理论主义者。',
 ('The museum was funded by a local industrialist.','博物馆由当地一位实业家资助。'),('The biography follows the career of a nineteenth-century industrialist.','传记讲述了一位十九世纪工业家的生涯。'))
W('industrialize','/ɪnˈdʌstriəlaɪz/','使工业化；发展工业、实现工业化',
 '生产和经济越来越依靠工业体系、机器和成规模制造；不只是给一间屋子摆上机器就完成全部社会变化。',
 '借法语 industrialiser，现代对应 industrial + -ize。英式也常见 industrialise，历史借入与今天可认的构词材料分开看。',I[:1]+[['法语 industrialiser → industrialize；现代对应 industrial + -ize','使工业发展、以工业为重要基础']],
 'industrialize an economy 使经济工业化，rapidly industrialize 迅速工业化，an industrialized region 工业化地区。',
 'industrialize an economy；rapidly industrialize；an industrialized region。',
 'industrialize 工业化，modernize 现代化范围更宽；modernize 一座图书馆不一定是把它变成工厂。',
 ('The region industrialized rapidly during that period.','那个时期，这一地区迅速实现工业化。'),('The chapter explains how the country began to industrialize.','这一章解释了该国怎样开始发展工业。'))
W('industrialization','英 /ɪnˌdʌstriəlaɪˈzeɪʃən/；美 /ɪnˌdʌstriəlɪˈzeɪʃən/','工业化、工业化过程',
 '把工业逐渐成为生产、经济重要基础的变化过程作为一个现象讨论，可能伴随城市、职业、生活方式变化。',
 '与法语 industrialisation 相接，现代可分析 industrial + -ization，或 industrialize 对应的 -ation 名词。不是把英语 industrialize 的完整拼写直接贴上 ation。',
 I[:1]+[['法语 industrialisation、英语相应派生 → industrialization','工业发展的转变过程']],
 'rapid industrialization 快速工业化，the effects of industrialization 工业化影响，a period of industrialization 工业化时期。',
 'rapid industrialization；the effects of industrialization；a period of industrialization。',
 'industrialization 是转变过程，industry 是工业、行业或勤勉等；并非每条行业新闻都是在说工业化进程。',
 ('Industrialization changed the city’s population and jobs.','工业化改变了城市的人口与就业。'),('The course examines the social effects of industrialization.','课程研究工业化的社会影响。'))
R('B2522','工业、工业经营者与发展工业的过程','INDUSTRIAL：工作活动词族，现代主要落到工业体系','industrial → industrially、industrialist；industrialize → industrialization 紧随看变化。',
 'industrial 和 industrious 形似同族，今天工业与勤奋各有搭配；工业家不等于每个产业工人。',
 'industria → industriel 等 → industrial；industrial + -ly/-ist/-ize；industrialisation 等 → industrialization。',
 [['性质、方式与人物','industrial · industrially · industrialist'],['工业化动作与过程','industrialize · industrialization']],
 'industrial/industrious 工业与勤奋；industrialist/worker 工业家与工人；industrialize/modernize 范围不同。',
 'Industrialization brought more industrial jobs to the region.\n\n工业化为地区带来了更多工业岗位。','industrial industrially industrialist industrialize industrialization')
T=[['古英语 tēag、tēah → 中古英语 teye 等 → tie〔名词〕','绳、系带 → 连结物、关系、领带等'],['古英语 tīġan 等 → 中古英语 teien 等 → tie〔动词〕','绑、连接 → 系结；比赛打平']]
def TH(f,m):return T+[[f,m]]
W('tie','/taɪ/','系、绑；领带；联系；平局',
 '把两头连住，东西分不开；关系也是人与人连着。比赛里双方成绩相同、谁也没拉开，就能说 a tie。',
 '名词绳带与系结动词各有古英语形式，后来汇入现代 tie。领带是系在颈部的东西；关系、平局是不同应用，不当同一个中文绑字逐句替换。',T,
 'tie your shoes 系鞋带，family ties 家庭纽带，wear a tie 戴领带，end in a tie 打成平局，tie something to 把某物和某事联系。',
 'tie your shoes；family ties；wear a tie；end in a tie。',
 'tie 名词可领带或平局，看服饰、比赛语境；tie up 也可让人忙得脱不开身，不能每次当真的被绑。',
 ('She tied her shoes before leaving.','出门前，她系好鞋带。'),('The game ended in a tie.','比赛以平局结束。'))
W('tying','/ˈtaɪɪŋ/','系、绑、连接；正在系、打平',
 '正在把结打好或把两件事连起来。看到 tying，认回 tie，不要误以为另有一个动词 ty。',
 'tie 加 -ing 时，ie 改 y，形成 tying；相应动作名词也有古英语、中古英语旧形式。die → dying 也可帮助记这个拼写变化。',TH('tie + -ing → tying〔ie 变 y〕','正在系结、连接；相应动作名词'),
 'tying a knot 打结，tying shoelaces 系鞋带，tying ideas together 把想法串起来。',
 'tying a knot；tying shoelaces；tying ideas together。',
 'tying 是 tie 的 -ing，tiring 是 tire 使疲倦、变累的 -ing；两者差一个 r，读音意义都不同。',
 ('He was tying his shoelaces when the phone rang.','电话响时，他正在系鞋带。'),('The final paragraph is useful for tying the ideas together.','最后一段有助于把这些想法串起来。'))
W('untie','/ʌnˈtaɪ/','解开、松开绑结',
 '原来绑着、打着结，把结松开，让东西分开；un- 逆转之前系住的动作。',
 '现代对应 un- + tie，古英语 untīġan、中古英语 untien 等已有相应形式。不是现代临时将 tie 前加个否定就等于不穿领带。',TH('古英语 untīġan → 中古英语 untien → untie','解除系住、绑住状态'),
 'untie a knot 解开结，untie your shoes 解开鞋带，untie the rope 解开绳子。',
 'untie a knot；untie your shoes；untie the rope。',
 'untie 解除绳结，cut 切断；解开不必破坏绳本身。untie 也不是一场平局自动变获胜。',
 ('She untied the ribbon around the box.','她解开了绕在盒子上的丝带。'),('Can you help me untie this knot?','你能帮我解开这个结吗？'))
W('tiebreaker','英 /ˈtaɪbreɪkə/；美 /ˈtaɪbreɪkər/','打破平局的加赛、问题或决定因素',
 '双方分不出高下，再来一道题、一轮比赛，或用一个预定条件定胜负；breaker 打破的是平局。',
 'tie 平局 + breaker 打破者、打破用的东西，组成决胜安排名。不同项目规则不同，词义不限定某一种加赛。',TH('tie + breaker → tiebreaker','打破平局的安排、因素'),
 'a tiebreaker question 决胜题，a tiebreaker round 决胜轮，use cost as a tiebreaker 用成本作为其他条件相同时的决定因素。',
 'a tiebreaker question；a tiebreaker round；as a tiebreaker。',
 'tiebreaker 可人、条件、安排，tiebreak 常指决胜赛本身；不是打断别人的领带。',
 ('The quiz needed a tiebreaker question.','智力问答需要一道决胜题。'),('When the scores were equal, experience served as the tiebreaker.','分数相同时，经验成了决定因素。'))
W('tier','英 /tɪə/；美 /tɪər/','层、排；等级、档次〔与 tie 另源的常用义〕',
 '看台一层层向上，服务也可分基础档、高级档；每一层、档叫 a tier。',
 '常用层级词借法语 tire、tier 等排、序列词，更早通常联系 tirer 拉出等，深源有不同分析。不是 tie 系 + -er 的普通读法；另有罕见系结者同形词，读音不同，不与等级混。',
 [['古法语 tire、法语 tier 等 → 英语 tier','排、序列 → 一层、等级'],['现代 tier','物理分层及服务、能力等档次']],
 'the top tier 最高层级，a tier of seats 一层座位，pricing tiers 价格档位，a free tier 免费档。',
 'the top tier；a tier of seats；pricing tiers；a free tier。',
 '层级 tier /tɪə, tɪər/，tie /taɪ/；tear 眼泪可与 tier 同音，但撕裂的 tear 又是另一读音。',
 ('The stadium has three tiers of seats.','体育场有三层看台座位。'),('The service offers a free tier and a paid tier.','服务提供免费档和付费档。'),
 sources=['https://en.wiktionary.org/wiki/tier#English','https://www.etymonline.com/word/tier'])
R('B3365','绑住、连接、领带和平局；tier 另源辨析','TIE：连在一起分不开，成绩相同也没拉开','tie → tying、untie；necktie、bowtie 服饰组合；tiebreak、tiebreaker 接平局；tier 的常用层级义以形近异源对照另列。',
 'tying 的拼写例外值得单列：ie 变 y。tier 层级常用读音与 tie 系结不同，不按字母样子假设一定是人物后缀。',
 'tēag、tīġan 等 → tie；tie + -ing 为 tying；un- + tie；tie + breaker；tier 层级借法语，另源。',
 [['系结、动作变化与解除','tie · tying · untie'],['领带和比赛组合','necktie · bowtie · tiebreak · tiebreaker'],['常用层级词另源对照','tier']],
 'tying/tiring 系结与疲倦；tier 层级非普通tie加er；tiebreaker 可用决胜条件，不限运动项目。',
 'The quiz ended in a tie, so they used a tiebreaker.\n\n问答赛打平了，于是他们加了一道决胜题。','tie tying untie necktie bowtie tiebreak tiebreaker tier')
CL=[['古希腊 klíma〔倾斜、地带〕→ 拉丁 clima → 法语 climat → climate','古地理按纬度、日照角度等分带'],['现代 climate','某地长期冷暖、雨雪等规律；也比喻社会氛围']]
W('climate','/ˈklaɪmət/ 或 /ˈklaɪmɪt/','气候；社会、经济等环境、氛围',
 '不是今天有没有下雨，而是住在这里多年，大体会遇到怎样的冷暖、雨雪规律。商业 climate 则是做事所处的大环境。',
 '经法语、拉丁接希腊 klíma 倾斜、地带，古地理以纬度、日照角度等划带；后来从某片地区转向地区的长期天气特征，不直接按现代 climb 爬来拆。',CL,
 'a mild climate 温和气候，climate change 气候变化，the economic climate 经济环境，a climate of trust 信任氛围。',
 'a mild climate；climate change；the economic climate；a climate of。',
 'weather 短时天气，climate 长期规律；某天冷不冷不能单凭这一次就概括整个地区气候。比喻氛围义也非气温数字。',
 ('The island has a mild climate.','这座岛气候温和。'),('The changes created a climate of uncertainty.','这些变化造成了一种不确定的氛围。'),
 sources=['https://en.wiktionary.org/wiki/climate#English','https://www.etymonline.com/word/climate','https://oceanservice.noaa.gov/facts/weather_climate.html'])
W('climatic','/klaɪˈmætɪk/','气候的、与气候有关的',
 '把关注点放到冷暖、降水等长期条件：climatic conditions 就是气候条件。',
 'climate 的 climat- + -ic，与法语等对应形容词也相关。末尾 e 不保留，重音、元音也发生变化，不读成 climate 原读后添 ic。',CL[:1]+[['climat- + -ic → climatic','与气候有关的']],
 'climatic conditions 气候条件，climatic differences 气候差异，climatic factors 气候因素。',
 'climatic conditions；climatic differences；climatic factors。',
 'climatic 气候的，climactic 高潮的多一个 c，读 /klaɪˈmæktɪk/；电影高潮不说 climatic scene。',
 ('The plants need suitable climatic conditions.','这些植物需要合适的气候条件。'),('The study compares climatic differences between the regions.','研究比较各地区的气候差异。'))
W('climatology','英 /ˌklaɪməˈtɒlədʒi/；美 /ˌklaɪməˈtɑːlədʒi/','气候学',
 '把一个地方、全球的长期气候规律作为对象来研究，不是只给明早天气作一条预报。',
 'climat- 气候词干 + -ology 研究、学科，连接成气候研究领域名。',CL[:1]+[['climat- + -ology → climatology','研究气候规律的学科']],
 'study climatology 学气候学，a course in climatology 气候学课程，climatology research 气候学研究。',
 'study climatology；a course in climatology；climatology research。',
 'climatology 研究长期气候，meteorology 气象学范围也包含天气与大气过程；领域有关联，不只简单分谁看天谁不看天。',
 ('She took a course in climatology.','她选修了一门气候学课程。'),('The library has a section on climatology.','图书馆有气候学专区。'))
W('microclimate','/ˈmaɪkrəʊklaɪmət/〔英〕；/ˈmaɪkroʊklaɪmət/〔美〕','小气候、局地气候',
 '大地区天气气候相近，墙角、院子、山谷却因遮阴、挡风等形成较独特的长期局部条件，这一小块就是 microclimate。',
 'micro- 小尺度 + climate，命名局部环境的气候；micro- 不一定小到显微镜才能看。',CL[:1]+[['micro- + climate → microclimate','局部小范围的气候条件']],
 'a garden microclimate 花园小气候，a sheltered microclimate 避风小气候，urban microclimates 城市局地气候。',
 'a garden microclimate；a sheltered microclimate；urban microclimates。',
 'microclimate 与大区域 climate 的区别主要是空间尺度；不是某天持续五分钟的天气就叫一种全新气候。',
 ('The courtyard has a warmer microclimate than the open field.','院子的小气候比开阔田野更温暖。'),('Gardeners consider the microclimate before choosing plants.','园丁选植物前会考虑当地的小气候。'))
R('B3901','古地理分带到长期天气特征','CLIMATE：看长期规律，再看气候条件、研究与局部尺度','climate → climatic、climatology；microclimate 缩小空间范围。',
 '旧倾斜、地带语义关联纬度日照的分区，现代主要看长期条件。climatic 气候与 climactic 高潮只差一字母，现代词基、搭配却不同。',
 'klíma → clima → climat → climate；climat- + -ic/-ology；micro- + climate。',
 [['基础、性质与学科','climate · climatic · climatology'],['局部尺度','microclimate']],
 'climate/weather 长期规律与短时天气；climatic/climactic 气候与高潮；microclimate 小尺度非一瞬间天气。',
 'Climatology examines climatic patterns, including local microclimates.\n\n气候学研究气候规律，也包括局地小气候。','climate climatic climatology microclimate')
if __name__=='__main__':save('continuation_20261030_dx',ROOTS,WORDS)
