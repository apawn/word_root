"""Meters, beginnings, maiden, hose, measurement adjectives, organization, quiz and sect."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()

Mt=[['希腊 metron 量度 → 科学构词 -meter','测量装置、计量器'],['前部材料 + -meter → 各类仪器名','前部说明测量对象；整词可能有不同重音']]
W('spectrometer','英 /spekˈtrɒmɪtə/；美 /spekˈtrɑːmɪtər/','光谱仪；分谱测量仪器',
 '不是只看光有多亮，而是把信号按波长等性质分开，再测各部分。像把一锅混合信息排成谱，让不同部分露出来。',
 'spectro- 光谱、谱相关材料 + -meter 测量装置。现代还有 mass spectrometer 质谱仪等用法，不能一律限成测可见光吸收的机器。',Mt+[['spectro- + -meter → spectrometer','分谱并测量信号的仪器']],
 'an optical spectrometer 光谱仪；a mass spectrometer 质谱仪；具体仪器按波长、质量等不同性质进行分析。',
 'an optical spectrometer；a mass spectrometer。',
 'spectrometer 侧重分谱测量，thermometer 测温度；名字的 meter 并非每次都是长度单位米。',
 ('The spectrometer separated the light into its component wavelengths.','光谱仪把光按各组成波长分开。'),('The researcher compared the signals recorded by the spectrometer.','研究者比较了谱仪记录的信号。'),sources=['https://en.wiktionary.org/wiki/spectrometer#English','https://www.merriam-webster.com/dictionary/spectrometer'])
W('pedometer','英 /pɪˈdɒmɪtə/；美 /pɪˈdɑːmɪtər/','计步器',
 '走一步，它记一次。距离可以再估算，但 pedometer 最基本的是记步数，不是直接测脚有多长。',
 '经法语 pédomètre 等，前部接拉丁 pes、ped- 脚，后部接希腊测量材料。现代可按 pedo- 脚 + -meter 理解，是拉丁、希腊材料混合的科学词。',Mt+[['ped- 脚 + 连接元音 o + -meter → pedometer','以行走步数计量的装置']],
 'wear a pedometer 佩戴计步器；a pedometer app 计步应用；a pedometer reading 计步读数。',
 'wear a pedometer；a pedometer app。',
 'pedo- 在这里是脚的材料，不能与表示儿童的其他同形构词混读；计步器的距离值常由步数等估算。',
 ('Her pedometer recorded eight thousand steps.','她的计步器记录了八千步。'),('The phone has a built-in pedometer.','这部手机内置计步器。'))
W('voltmeter','英 /ˈvəʊltmiːtə/；美 /ˈvoʊltmiːtər/','电压表、伏特计',
 'volt 是电压单位伏特，voltmeter 就是读电压的表。这里的表和尺子不一样，测的是两点之间的电势差。',
 'volt 伏特 + -meter 仪表 → voltmeter；volt 源自物理学家 Volta 的姓，后作单位名。',Mt+[['volt + -meter → voltmeter','以伏特表示测量结果的电压表']],
 'a digital voltmeter 数字电压表；a voltmeter reading 电压表示数。',
 'a digital voltmeter；a voltmeter reading。',
 'voltmeter 测电压，ammeter 测电流；multimeter 可兼有多种测量功能，不是 voltmeter 的长拼写。',
 ('The digital voltmeter displayed a steady reading.','数字电压表显示着稳定的读数。'),('The diagram labels the voltmeter with the letter V.','图中用字母 V 标出了电压表。'))
R('A1974','测量装置，前半指出量什么','-METER：把某种量变成可读的数字','温度、气压、速度先看常见仪表，再把同一构词用于步数、电压和光谱。',
 '不要把每个 meter 都译成米。这个词尾常说计、仪、表；不同仪器量的对象和显示单位由前部与上下文决定。',
 '希腊 metron 量度 → -meter；部分词经法语借入，部分用科学材料造词；voltmeter 与 pedometer 的重音安排不同。',
 [['日常与交通仪表','thermometer · barometer · speedometer · pedometer · odometer · altimeter'],['电学与信号分析','voltmeter · multimeter · spectrometer · interferometer'],['其他代表测量装置','accelerometer · micrometer · chronometer · magnetometer · tachometer · radiometer · calorimeter']],
 '-meter 的仪器义与长度单位 metre／meter 要分开；micrometer 还可因读音与语境区别测微器和微米单位。',
 'The display shows readings from a thermometer and a voltmeter.\n\n显示屏列出了温度计和电压表的读数。','thermometer barometer speedometer pedometer odometer altimeter voltmeter multimeter spectrometer interferometer accelerometer micrometer chronometer magnetometer tachometer radiometer calorimeter')

Co=[['拉丁 com- + initiare 开始等 → 通俗拉丁相关形式','进入、开始某个阶段'],['古法语 comencier 等 → commence；commencement、recommence','开始；开始名词、毕业典礼；再次开始']]
W('commence','/kəˈmens/','〔正式〕开始、着手',
 '通知上说“会议将于九点开始”，常比聊天里的 start 正式一点，这时就可能用 commence。',
 '经中古英语及盎格鲁法语 comencer 等，上接通俗拉丁相关形式，由 com- 与 initiare 开始材料构成。不是 common 截短加一个现代词尾。',Co,
 'commence work 开始工作；commence at nine 九点开始；commence with a speech 以讲话开场。',
 'commence work；commence at；commence with。',
 'commence 比 begin、start 更正式，不代表一定规模更大。日常说开始看电影，用 start 通常更自然。',
 ('The ceremony will commence at ten.','典礼将于十点开始。'),('They commenced work on the new bridge in spring.','他们春天开始修建新桥。'))
W('commencement','/kəˈmensmənt/','开始、开端；〔尤美〕毕业典礼',
 '一个词既能说开始，也能说毕业典礼，看似反过来，其实旧大学用法看的是开始取得学位身份、资格的阶段。',
 '借法语 commencement，现代可对应 commence + -ment。毕业典礼义接大学开始取得学位相关身份、权利的旧用法；“人生新篇章”可帮助记忆，但不是足够的完整词源。',Co+[['法语 commencement → 英语 commencement','开始；大学新学位身份的进入 → 毕业典礼']],
 'the commencement of work 开工；a commencement ceremony 毕业典礼；a commencement address 毕业典礼致辞。',
 'the commencement of；a commencement address。',
 'graduation 可说毕业这件事，commencement 常特别说典礼；不同学校的典礼时间和实际毕业手续不一定完全相同。',
 ('The notice gives the commencement date for the work.','通知列出了工程的开工日期。'),('Her family attended the commencement ceremony.','她的家人参加了毕业典礼。'),sources=['https://en.wiktionary.org/wiki/commencement#English','https://www.etymonline.com/word/commencement'])
W('recommence','/ˌriːkəˈmens/','〔正式〕重新开始、恢复',
 '事情停过一会儿，再开始，就是 recommence。比 resume 更能看出 re- 再次 + commence 开始的构词。',
 '借法语 recommencer 等，相当于 re- 再次 + commence。不是 commence 加 -re，也不表示推荐 recommend。',Co+[['re- + commence／法语 recommencer → recommence','中断后再次开始']],
 'recommence work 恢复工作；recommence after a break 休息后重新开始。',
 'recommence work；recommence after。',
 'commence 可第一次开始，recommence 通常暗示已经开始过；重新开始可继续原事，不一定推倒重来。',
 ('Work will recommence after the holiday.','假期后将恢复工作。'),('The discussion recommenced when everyone returned.','大家回来后，讨论重新开始。'))
R('B3983','进入开始阶段，再分动作、名词与再次开始','COMMENCE：正式地说一件事开场了','commence → commencement；recommence 加上再次开始。',
 '先用 begin、start 理解基本动作，再感受正式通知的语气。commencement 的毕业典礼义要看旧大学的身份进入，不用单凭结束学业来猜反义。',
 'com- + initiare 的拉丁材料 → 法语 commencer 等 → commence；-ment 名词；re- 再次。',
 [['开始动作及对应名词','commence · commencement'],['重新开始','recommence']],
 'commencement 可是开端，也可是毕业典礼；recommence 与 recommend 推荐不同。',
 'After a short pause, the ceremony recommenced with a commencement address.\n\n短暂停顿后，典礼以毕业致辞重新开始。','commence commencement recommence')
R('B2807','年轻女子的旧称，发展出首次、尚未经历的修饰义','MAIDEN：从旧日少女称呼，借到头一次','maiden 先读年轻女子的旧义，再看 maiden voyage 首航等常见搭配。',
 '历史人物叙述中的 maiden 常带文学、旧时代色彩。现代航海、演讲等搭配中，它则常把还未经历、第一次的意味借给事物。',
 '古英语 mægden → 中古英语 maiden；maid 反而是后来的缩短，不能只看今天字母少就判定较早。',
 [['旧人物称呼与首次的修饰义','maiden']],
 'maiden name 是婚前姓的固定说法，maiden voyage 是首航；不能按词形推断任何人的真实经历。',
 'The ship completed its maiden voyage.\n\n这艘船完成了首航。','maiden')

Ho=[['古英语 hose、hosa 腿部覆盖衣物 → hose','袜、紧身腿衣等旧义'],['袜状管套形状 → 柔性输送管；hose 作喷水动词','衣物与软管通过管状外形联系'],['panty + hose；hose + -ing','连裤袜；喷水冲洗动作']]
W('hose','英 /həʊz/；美 /hoʊz/','软管、水管；〔衣物〕袜、袜裤；用软管冲洗',
 '花园里能弯的长水管是 hose，但历史上先有腿上穿的袜状衣物。两者都像一条空心套管，形状把新旧义连了起来。',
 '承古英语 hose、hosa 等腿部覆盖衣物名，经中古英语延续；再用来称管状物、输送液体软管，喷水动词由管名发展。',Ho,
 'a garden hose 花园水管；a fire hose 消防水带；hose down a wall 用水管冲墙。衣物义见 pantyhose、hosiery 等。',
 'a garden hose；hose down。',
 'pipe 可说刚性管道，hose 通常是可弯软管；衣物 hose 读音同样末尾 /z/，不是 horse 马。',
 ('She coiled the garden hose beside the shed.','她把花园水管盘好放在棚旁。'),('He hosed down the muddy path.','他用水管冲洗泥泞的小路。'),sources=['https://en.wiktionary.org/wiki/hose#English','https://www.etymonline.com/word/hose'])
W('pantyhose','英 /ˈpæntihəʊz/；美 /ˈpæntihoʊz/','〔尤美〕连裤袜',
 '不是一条水管，而是左右袜腿与上面的裤身连成一件的袜裤。这里 hose 保留衣物义。',
 'panty 内裤材料 + hose 袜类衣物 → pantyhose，现代服装复合名词；通常按复数衣物形式使用。',Ho[:1]+[['panty + hose → pantyhose','上部与袜腿相连的一件衣物']],
 'a pair of pantyhose 一条连裤袜；wear pantyhose 穿连裤袜。美式常见，英式常用 tights。',
 'a pair of pantyhose；wear pantyhose。',
 'pantyhose 与 tights 的范围随地区习惯重叠；不能把 pantyhose 拆译成内裤水管，也不等于单独一双 stockings。',
 ('She bought a new pair of pantyhose.','她买了一条新连裤袜。'),('The shop sells socks, stockings and pantyhose.','这家店卖短袜、长袜和连裤袜。'))
W('hosing','英 /ˈhəʊzɪŋ/；美 /ˈhoʊzɪŋ/','用软管冲洗；hose 的 -ing 形式',
 '拿着水管冲洗地面这个活动，可以说 hosing。hose 是工具名，也作动作；-ing 再把动作放进句子或当名词。',
 'hose 去末 e + -ing → hosing，不双写 s。常接 down 表把表面冲洗一遍。',Ho+[['hose + -ing → hosing','喷水冲洗活动；正在用水管冲']],
 'give something a hosing 用水管把某物冲洗一下；be hosing down 正在用水管冲洗。',
 'a thorough hosing；hosing down。',
 'hosing 末 s 读 /z/；housing 住房、中间常带 /aʊ/，多一个 u，意思不同。',
 ('The patio needed a thorough hosing after the party.','聚会后，露台得用水管好好冲一遍。'),('She was hosing down the chairs outside.','她正在外面用水管冲椅子。'))
R('B4474','腿部管状衣物的旧名，借形状发展为软管','HOSE：先是套腿的衣物，再是能输水的软管','hose → pantyhose；软管动词 → hosing。',
 '裤袜与水管看似很远，管状外形把它们连住。学复合词时先看保留哪一支义，不要把所有 hose 都翻成水管。',
 'hosa 等 → hose；panty + hose 衣物；hose 动词去 e 接 -ing。husk 的更早来源另有多种解释，不作确定的现代直接派生。',
 [['衣物与管形名词','hose · pantyhose'],['用软管冲洗','hosing']],
 'hose /həʊz/ 与 horse 马不同；hosing 不同于 housing；husk 不凭表面就拆成 hose 加词尾。',
 'The gardener was hosing down the path with a long hose.\n\n园丁正拿着长水管冲洗小路。','hose pantyhose hosing')
ROOTS[-1]['exclude']['husk']='其覆盖物远源有多种解释，不列作现代 hose 的确定直接扩展；另见独立词条。'

Mc=[['希腊 metron 量度 → -metric 量度相关的','也与 -metry 测量法等名词相对应'],['econo-、stoichi(o)- 等 + -metric','限定测什么、按什么比例计量']]
W('econometric','英 /ɪˌkɒnəˈmetrɪk/；美 /ɪˌkɑːnəˈmetrɪk/','计量经济学的；经济计量的',
 '把经济关系写成可用数据估计、检验的模型，是 econometric 的典型场景。它不是简单说经济、划算。',
 'econo- 经济材料 + -metric 计量相关，对应 econometrics 计量经济学的形容词形式。',Mc+[['econo- + -metric → econometric','用定量方法研究经济关系的']],
 'an econometric model 计量经济模型；econometric analysis 计量经济分析；econometric methods 计量经济方法。',
 'an econometric model；econometric analysis。',
 'economic 泛说经济相关，economical 常说节省；econometric 指向经济数据、统计模型的计量方法。',
 ('The paper uses an econometric model to study household spending.','论文用计量经济模型研究家庭支出。'),('She is taking a course in econometric methods.','她在上一门计量经济方法课。'))
W('stoichiometric','/ˌstɔɪkiəˈmetrɪk/','化学计量的；符合相应反应、组成比例的',
 '化学方程式不只告诉你用了什么，还告诉你各用多少的比例。stoichiometric 就和这种反应、组成的定量关系有关。',
 'stoichi(o)- 接希腊 stoikheion 元素、基本成分 + -metric 计量相关；对应 stoichiometry 化学计量。不是 stoic 冷静的形容词变化。',Mc+[['stoichi(o)- 基本成分 + -metric → stoichiometric','按化学组成、反应的定量关系理解']],
 'a stoichiometric ratio 化学计量比；stoichiometric calculations 化学计量计算；按方程式算比例，不是任意称重。',
 'a stoichiometric ratio；stoichiometric calculations。',
 'stoichiometric 的比例常以物质的量关系表达，不能把方程式系数一律当质量克数；metric 在这里也不只说公制。',
 ('The equation gives the stoichiometric ratio of the reactants.','方程式给出了反应物的化学计量比。'),('The students practised stoichiometric calculations in class.','学生在课上练习化学计量计算。'),sources=['https://en.wiktionary.org/wiki/stoichiometric#English','https://www.merriam-webster.com/dictionary/stoichiometric'])
R('A1898','计量相关的形容词材料，范围由前半决定','-METRIC：这套描述与哪一种量度有关','geometric 看几何，biometric 看生物特征，econometric 看经济计量。',
 '这个词尾不等于每个词都在说公制。接不同材料后，可说形状、身体特征、气压、光度或学科中的定量关系。',
 '希腊量度材料 → -metric；常与 -metry 名词对应；部分整词历经借入，不能统一说先在英语名词后加一个 c。',
 [['形状、身体与物理量','geometric · biometric · isometric · barometric · photometric'],['学科定量关系','econometric · stoichiometric']],
 'economic、economical、econometric 各有重心；stoichiometric 的计量不是只写数字或公制单位。',
 'The study combines geometric measurements with an econometric model.\n\n研究把几何测量与计量经济模型结合起来。','geometric biometric isometric barometric photometric econometric stoichiometric')

Or=[['organization + -al → organizational','组织或组织工作相关的'],['organizational + -ly → organizationally','从组织层面看；在组织安排方面']]
W('organizationally','英 /ˌɔːɡənaɪˈzeɪʃənəli/；美 /ˌɔːrɡənəˈzeɪʃənəli/','从组织上说；在组织、安排方面',
 '技术做得出，不代表人员、权限、协作已经安排好。organizationally 把观察角度切到组织这一层。',
 'organizational + -ly → organizationally，末 l 接 -ly 成 ll；长词里可按 organization → organizational → organizationally 分层。',Or,
 'organizationally complex 组织上复杂；organizationally separate 组织架构上分开的；organizationally ready 在组织安排上准备好。',
 'organizationally complex；organizationally separate。',
 'organizationally 不保证组织得好；它只是限定讨论层面，organizationally chaotic 也完全说得通。',
 ('The teams are organizationally separate but share the same building.','两个团队在组织架构上分开，但共用一栋楼。'),('The project is technically simple but organizationally complex.','项目技术上简单，组织协调上却很复杂。'))
R('B4527','组织相关性质与观察角度，别把长词整块硬背','ORGANIZATIONAL：看人员、结构与协作怎样安排','organizational → organizationally，形容词转组织层面的副词。',
 '先想组织结构与协作安排，再读 -al 性质、-ly 角度。这个词族本身不评价安排好坏，后面的 ready、complex 等才说结果。',
 'organization + -al → organizational；再接 -ly → organizationally，拼写 ll。',
 [['组织性质与观察角度','organizational · organizationally']],
 'organized 常说有条理、已组织好；organizational 只说与组织有关；副词也不自动有有序的褒义。',
 'An organizational change can be organizationally difficult even when it is technically simple.\n\n一次组织调整，即使技术上简单，在组织协调上也可能很难。','organizational organizationally')

Qu=[['十八世纪 quiz 奇怪的人、怪事等旧用法','确切起源未定，流传造词故事不可靠'],['quiz → 测验、盘问；+ -ical → quizzical','疑问、困惑或古怪的表情与语气']]
W('quiz','/kwɪz/','小测验；知识问答；测问、盘问',
 '出几道问题，看看你懂不懂，是课堂 quiz；一群人抢答常识题，也是 quiz。作动词则可以问得很细，不只是发一张试卷。',
 '十八世纪已有 quiz 奇人、怪事等用法，之后发展、交汇出测问与测验义，确切起源未定。剧院经理打赌一夜造词的故事不作为可靠词源。',Qu,
 'a vocabulary quiz 词汇小测；a pub quiz 酒吧知识问答；quiz someone about something 详细询问某人某事。复数 quizzes，过去式 quizzed。',
 'take a quiz；quiz someone about。',
 'quiz 通常比 exam 小、短或随意，但词本身不是统一的考试时长标准；动词也能说盘问，而非课堂测验。',
 ('We had a short vocabulary quiz at the end of class.','下课前，我们做了一个简短词汇测验。'),('The reporter quizzed her about the missing documents.','记者就丢失的文件详细询问了她。'),sources=['https://en.wiktionary.org/wiki/quiz#English','https://www.etymonline.com/word/quiz'])
W('quizzical','/ˈkwɪzɪkəl/','带疑问、困惑的；略带诧异或逗趣的',
 '眉毛一挑，表情像在问“这是什么意思？”——a quizzical look 常是这种不解里带点诧异的样子。',
 'quiz 的旧有怪异、逗趣、疑问材料 + -ical → quizzical，双写 z。不能只照今天 quiz 小考的意思翻成考试的。',Qu+[['quiz + -ical → quizzical','怪异、疑问材料 → 困惑、诧异的神情']],
 'a quizzical look 疑惑的神情；a quizzical smile 带疑问、逗趣的微笑；raise a quizzical eyebrow 疑惑地挑眉。',
 'a quizzical look；a quizzical smile。',
 'confused 可泛指困惑，quizzical 更常描写像在发问、略有诧异的表情；不是 quiz 的所有形容词用途都能用它。',
 ('She gave me a quizzical look when I asked for a spoon at the bakery.','我在面包店要勺子时，她疑惑地看了我一眼。'),('He raised one eyebrow in a quizzical expression.','他挑起一边眉毛，露出不解的表情。'))
R('B2436','从怪人、怪事等旧用法，走向问答、疑问神情','QUIZ：用问题测一测，也能问得人一脸疑惑','quiz → quizzical，旧义帮你理解为何形容词不是单纯考试的。',
 '先掌握课堂小测、知识问答与详细询问，再看 quizzical 的表情画面。确切起源未定，不靠一段戏剧化传说填满空白。',
 'quiz 起源未定；quizzes、quizzed 双写 z；+ -ical → quizzical。',
 [['问答与疑问表情','quiz · quizzical']],
 'quizzical 不是考试的通用形容词；一夜造出 quiz 的赌约故事不能当确定历史。',
 'A surprising question in the quiz brought a quizzical look to her face.\n\n测验里一个意外问题让她露出了疑惑的表情。','quiz quizzical')

Sc=[['拉丁 secta 路线、追随、学派等 → 古法语 secte → sect','共同遵循某种路线的群体'],['跟随与切分材料的历史存在交错；sectarian 接宗派分支','不把所有含 sect 的词当这个英语名词的派生']]
W('sect','/sekt/','宗派、教派；学派、小团体',
 '一群人共同追随一种教义、老师或思想路线，就可能被称为 sect。常指宗教中的一派，但并不自动等于邪教。',
 '经古法语 secte 接拉丁 secta 路线、追随、学派等。常联系 sequi 跟随，也有与 secare 切分材料的历史交错和不同解释，不能给出唯一的现代“切开”拼装。',Sc,
 'a religious sect 宗教派别；a small sect 一个小教派；a philosophical sect 某哲学学派。词可带局外人、较小分支的视角。',
 'a religious sect；a philosophical sect。',
 'sect 与 cult 在某些语境有重叠，但不能看见 sect 就下危险、欺骗的结论；intersect 则明确接拉丁切开材料，并非英语 sect 群体直接造出。',
 ('The historian compared the beliefs of several religious sects.','历史学家比较了几个宗教派别的信仰。'),('The book traces the growth of a small philosophical sect.','书中追溯了一个小哲学学派的发展。'),sources=['https://en.wiktionary.org/wiki/sect#English','https://www.etymonline.com/word/sect'])
R('B2509','共同追随的路线与群体，历史词形与切分材料有交错','SECT：沿着同一路线走的一群人','sect → sectarian，先群体，再宗派性质、立场。',
 '路线、学派、宗教派别能在近源意义上接起来。切分一派的解释也有历史交错，但不把所有字母 sect 都直接挂到现代名词 sect 下。',
 'secta → secte → sect；中世纪拉丁 sectarius 等 → sectarian；sequi 与 secare 材料的关联解释需保留历史差别。',
 [['群体与宗派性质','sect · sectarian']],
 'sect 不自动等于邪教；intersect 的切交结构另看 secare，不按 inter- + 一个宗派来解释。',
 'The article describes the sect without adopting its sectarian outlook.\n\n文章描述这个教派，但没有采纳它的宗派立场。','sect sectarian')
ROOTS[-1]['exclude']['intersect']='明确接拉丁 intersecare 的切开材料，不列作现代英语 sect 宗派名词的直接派生。'

if __name__=='__main__':save('continuation_20261030_og',ROOTS,WORDS)
