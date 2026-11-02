"""Recommendations, responses, plans, people and things worth considering."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'C0707':dict(words=['recommendation','recommendations'],label='recommendation → recommendations：值得采用的建议、推荐',note='拉丁及法语推荐名词有自身借入路线，re 不必每次译为再次。'),
 'C1397':dict(words=['response','responses'],label='response → responses：接到信息后的回应',note='拉丁答复名词经法语借入，现代既可说言语答复，也可说反应。'),
 'C1431':dict(words=['strategy','strategies'],label='strategy → strategies：为目标安排整体办法',note='希腊军队、统领词族，经法语等形成统筹计划用途。'),
 'A1760':dict(words=['target','targets'],label='target → targets：小盾到瞄准对象',note='法语 targe 与指小材料，后有靶子、目标和瞄准动词。'),
 'C1656':dict(words=['volunteer','volunteers'],label='volunteer → volunteers：自愿出力、主动提出',note='法语自愿者词接拉丁意愿词族，英语动词后从名词发展。'),
 'B3503':dict(words=['witness','witnesses'],label='witness → witnesses：知道、证明与亲历者',note='古英语知识加名词材料，证言、人物及动词历史分别看。'),
 'B3322':dict(words=['characteristic','characteristics'],label='characteristic → characteristics：能认出它的特征',note='character 与 istic 的构成对应希腊模型，英语名词、形容词很早均有。'),
 'C1188':dict(words=['discussion','discussions'],label='discussion → discussions：拿出来审看、交流',note='拉丁查验名词经法语或直接借入，现代讨论义展开。'),
 'B2852':dict(words=['drive','drives'],label='drive → drives：推动、驾驶与驱动力',note='本族驱赶、推动动词，汽车、动机、存储设备等用途后扩展。'),
 'A1935':dict(words=['perform','performance','performances'],label='performance → performances：完成、表现与演出',note='perform 加 ance；较早法语 parfornir 完成词史保留。'),
 'B3929':dict(words=['consider','consideration'],label='consider → consideration：认真看、纳入思量',note='名词有法语和拉丁独立借入路线，更远星辰词源分析有分歧。'),
 'C1174':dict(words=['count','counts'],label='count → counts：计数、分项与算数',note='计数与伯爵两支经法语进入，拉丁远源不同。'),
 'C0268':dict(words=['create','creates'],label='create → creates：让新事物产生',note='拉丁 creare、creatus 词族进入英语，英语现在单数再加 s。'),
 'C0456':dict(words=['fund','funded'],label='fund → funded：财产底子到提供资金',note='拉丁底部、地产词经法语等发展为储备、资金，英语动词后转用。'),
 'A1761':dict(words=['guarantee','guaranteed'],label='guarantee → guaranteed：担保、作保证',note='法语担保词族，与 warranty 相关；ee 不是人物尾的简单套用。'),
 'C1353':dict(words=['exist','existed'],label='exist → existed：出现到存在',note='拉丁 ex 与 sistere 组合，经法语、拉丁相关路线进入。'),
}
W('recommendations','/ˌrekəmenˈdeɪʃənz/','建议、推荐；推荐证明〔复数〕',
 '觉得某个办法、人或事物值得考虑，把它指给别人，是 recommendations。报告可以给改进建议，朋友可以给书单推荐。',
 'recommendation + -s，/n/ 后读 /z/。名词经法语 recomendacion 等接中世纪拉丁 recommendātiō；现代可认 recommend + -ation 的关系，历史上名词有自身借入线。',
 [['拉丁 recommendātiō → 法语 → recommendation','托付、称赞、表示值得信任 → 推荐、建议'],['recommendation + -s → recommendations','多项建议、推荐或推荐材料']],
 'make recommendations 提出建议；recommendations for improvement 改进建议；book recommendations 图书推荐。',
 'follow the recommendations 采纳建议；recommendations from colleagues 同事的推荐。','recommendation 可以是建议做法，也可以是对人、物的推荐。它说明值得采用、考虑，不自动等于必须执行的命令。',
 ('The report makes several recommendations for improving access to the service.','报告提出几项让人更方便地使用服务的建议。'),('She asked her friends for book recommendations.','她向朋友征求图书推荐。'),sources=['https://en.wiktionary.org/wiki/recommendations#English','https://www.etymonline.com/word/recommendation'])
W('responses','英 /rɪˈspɒnsɪz/；美 /rɪˈspɑːnsɪz/','回应、回答；反应〔复数〕',
 '外面来了一句话、一件事或一种变化，接下来回过去的动作、信息，就是 responses。回复问卷和听到消息的表情，都是不同形式的回应。',
 'response + -s，/s/ 后增加 /ɪz/。response 经法语接拉丁 respōnsum 答复名词，来自 respondēre 回答的分词材料；英语名词有独立借入历史。',
 [['拉丁 respōnsum → 法语 → response','答复 → 言语、行为或身体反应'],['response + -s → responses','多份回答、多种反应']],
 'responses to the survey 调查回答；different responses 不同反应；receive responses 收到回复。',
 'positive responses 积极回应；responses from readers 读者回复。','response to 给对什么作回应；response from 给回应来自谁。responses 不必全是文字，也可能是动作、情绪、测得的反应。',
 ('The survey received responses from over a hundred people.','调查收到了百余人的回答。'),('The same question produced very different responses.','同一个问题引出了很不一样的回应。'),sources=['https://en.wiktionary.org/wiki/responses#English','https://en.wiktionary.org/wiki/response#English'])
W('strategies','/ˈstrætədʒiz/','策略、整体行动办法〔复数〕',
 '先看目标在哪里，再安排用什么路、什么资源去达到，是 strategies。它常关注整体走法，而不是单独一次临时动作。',
 'strategy 的辅音字母 + y 改 ies。希腊 stratos 军队与统领相关 agos 材料组成 strategos，相关 strategia 统帅之术经法语等路线进入英语，再扩到一般行动计划。',
 [['希腊军队、统领词族 → 法语等 → strategy','统筹军队的办法 → 为目标规划整体行动'],['strategy：y 改 ies → strategies','可比较的多种策略']],
 'learning strategies 学习策略；strategies for saving time 节时办法；develop strategies 制定策略。',
 'different strategies 不同策略；long-term strategies 长期策略。','strategy 常看整体办法，tactic 常偏实现办法时的一项具体动作；实际用法有重叠。strategy for doing 说明为完成什么目标。',
 ('The students shared strategies for remembering new words.','学生分享了记新单词的策略。'),('The team compared several strategies before choosing one.','团队比较了几种策略后选定其中一种。'),sources=['https://en.wiktionary.org/wiki/strategies#English','https://en.wiktionary.org/wiki/strategy#English'])
W('targets','英 /ˈtɑːɡɪts/；美 /ˈtɑːrɡɪts/','目标、指标；靶子、针对对象〔复数〕；瞄准、面向〔第三人称单数〕',
 '先指明想打到、达到的那个点，就是 targets。射箭有靶子，工作有指标，服务有面向的人群。',
 'target + -s，/t/ 后读 /s/。较早 target 是小盾，接 targe 及法语 targete 等指小形式，远接日耳曼盾框材料；后来成为射击目标，再有一般目标、瞄准动词。',
 [['法语小盾词 → target','小盾 → 靶子、瞄准对象 → 要达到的目标'],['target + -s → targets','多个目标、指标；单数主语针对']],
 'set targets 设定目标；meet targets 达到指标；targets new readers 面向新读者。',
 'targets for the year 年度目标；practice targets 练习靶。','target 作名词可以是可量化指标，也可以是被针对的人、物。targets somebody 作动词通常强调有选择地把行动指向谁。',
 ('The team set realistic targets for the month.','团队为本月设定了实际可行的目标。'),('The guide targets people learning the subject for the first time.','指南面向初次学习这个主题的人。'),sources=['https://en.wiktionary.org/wiki/targets#English','https://en.wiktionary.org/wiki/target#English'])
W('volunteers','英 /ˌvɒlənˈtɪəz/；美 /ˌvɑːlənˈtɪrz/','志愿者、自愿参与者〔复数〕；主动提出、自愿做〔第三人称单数〕',
 '不用别人强派，自己站出来说愿意做，是 volunteers 的自愿画面。可以是参加志愿服务，也可以是主动承担一次任务、提供信息。',
 'volunteer + -s，末尾读 /z/。名词经法语 volontaire 接拉丁 voluntārius 自愿的，联系 voluntās 意愿；早期常有自愿从军背景，英语动词后从名词发展。',
 [['拉丁 voluntārius → 法语 → volunteer','出于自己意愿的人 → 自愿参与者'],['volunteer + -s → volunteers','多位志愿者；单数主语主动提出做']],
 'local volunteers 当地志愿者；volunteers to help 主动提出帮忙；volunteers information 主动提供信息。',
 'a team of volunteers 志愿者团队；volunteers for the task 自愿承担任务。','志愿服务常是无薪帮助；volunteer 作动词还可以只是主动报名、提出一件事。是否有报酬、是否正式任职，要看所说的活动。',
 ('Volunteers helped visitors find their way around the museum.','志愿者帮助访客在博物馆里找路。'),('She volunteers to organise the next meeting.','她主动提出组织下次会议。'),sources=['https://en.wiktionary.org/wiki/volunteers#English','https://en.wiktionary.org/wiki/volunteer#English'])
W('witnesses','/ˈwɪtnəsɪz/','目击者、证人；见证者〔复数〕；目睹〔第三人称单数〕',
 '某个人亲眼看见、亲身经历，因而能为一件事作证，就是 witnesses 的人物画面。作动词时则是看见、经历了什么。',
 'witness + -es，/s/ 后增加 /ɪz/。接古英语 gewitnes 等知识、证言材料，可认旧 wit 知道 + -ness；人物、证言与动词用途逐步发展，wit 不按现代幽默直译。',
 [['古英语知识、证明词 → witness','知道、证言 → 能证明事情的人及目睹动作'],['witness + -es → witnesses','多位证人、目击者；单数主语目睹']],
 'witnesses to the event 事件的见证者；speak to witnesses 与目击者交谈；witnesses a change 亲眼看到变化。',
 'independent witnesses 独立证人；witnesses at the scene 现场目击者。','witnesses 作人物是能提供所见、证明的人，具体程序角色依场景。a city witnesses change 是拟人地说城市经历变化，不一定有一个人在旁说话。',
 ('Several witnesses described what they had seen.','几位目击者描述了他们所见的情况。'),('The historian spoke to witnesses of the event.','历史学家与事件见证者交谈。'),sources=['https://en.wiktionary.org/wiki/witnesses#English','https://en.wiktionary.org/wiki/witness#English'])
W('characteristics','/ˌkærəktəˈrɪstɪks/','特征、特点〔复数〕',
 '哪些地方让它和别的东西区分开、让你认出它，就是 characteristics。可以是人的做事方式，也可以是材料、动物、设备的可描述特征。',
 'characteristic + -s，/k/ 后读 /s/。character + -istic 的构成以希腊 kharaktēristikos 等为模型，较早 character 接刻痕、独特标记的词史；英语名词、形容词很早都存在。',
 [['character 独特标记、性质 + -istic → characteristic','能表明其独特之处 → 特征、特有的'],['名词 characteristic + -s → characteristics','多个能描述、识别对象的特点']],
 'key characteristics 关键特征；physical characteristics 外形、物理特征；characteristics of the material 材料特点。',
 'shared characteristics 共同特点；compare characteristics 比较特征。','characteristic 作形容词是特有的，characteristics 是特点名词复数。它不只描述人的性格，也可说声音、结构、材料性能。',
 ('The guide describes the main characteristics of each bird.','指南描述每种鸟的主要特征。'),('The two materials share several useful characteristics.','两种材料有几个共同的实用特点。'),sources=['https://en.wiktionary.org/wiki/characteristics#English','https://www.etymonline.com/word/characteristic'])
W('discussions','/dɪˈskʌʃənz/','讨论、商谈〔复数〕',
 '把一个问题放到大家面前，从不同角度查看、交换想法，就是 discussions。重点在围绕问题展开交流，而不是非得争个输赢。',
 'discussion + -s，/n/ 后读 /z/。名词经法语或直接接拉丁 discussiō 查验、审查，连到 discutere 摇开、检验的词族；英语较早也有检验义，谈论义后来突出。',
 [['拉丁 discussiō → 法语或直接 → discussion','摇开、审查问题 → 通过交流查看问题'],['discussion + -s → discussions','多次讨论、不同议题的商谈']],
 'hold discussions 举行讨论；discussions about the plan 关于计划的讨论；group discussions 小组讨论。',
 'discussions with colleagues 与同事商谈；discussions on the topic 关于主题的讨论。','discussion 是名词，常用 discussion about/on something；动词 discuss 通常直接接对象。discussions 不自动说明已经达成决定。',
 ('The plan changed after several discussions with local residents.','与当地居民讨论几次后，计划有了改变。'),('Small group discussions helped the students compare ideas.','小组讨论帮助学生比较不同想法。'),sources=['https://en.wiktionary.org/wiki/discussions#English','https://en.wiktionary.org/wiki/discussion#English'])
W('drives','/draɪvz/','驾驶、驱动、促使〔第三人称单数〕；驾车行程、驱动力、驱动器、动员活动等〔复数〕',
 '给一股力量，让人或东西朝一个方向走，是 drives 的线索。人驾驶车，动机推动人；电脑里的 drive 则沿带动设备工作的技术用途，成为驱动器的名称。',
 'drive + -s，/v/ 后读 /z/。drive 继承古英语 drīfan 驱赶、推动，早于汽车；驾车、心理动力、技术设备、募捐活动等名词或动词用途后续发展。',
 [['古英语 drīfan → drive','推动、驱赶 → 驾驶、促使'],['drive + -s → drives；名词用途','单数主语驾驶；多次驾车、设备或动员活动']],
 'drives to work 开车上班；drives change 推动改变；hard drives 硬盘；food drives 食品募集活动。',
 'long drives 长途驾车；drives people to improve 促使人们进步。','drives 可以是动词，也可以是具体可数的设备、活动。a drive for donations 是集中动员募集捐赠；日常核心仍是推动、驾驶的线索。',
 ('She drives to work twice a week.','她每周两次开车上班。'),('The files are stored on two separate drives.','文件存放在两个独立的驱动器上。'),sources=['https://en.wiktionary.org/wiki/drives#English','https://en.wiktionary.org/wiki/drive#English'])
W('performances','英 /pəˈfɔːmənsɪz/；美 /pərˈfɔːrmənsɪz/','演出、表演；各次表现〔复数〕',
 '把准备的本领在一次行动里做出来，就是 performance 的表现；搬到舞台上，是演出。performances 把不同场次、不同次表现分别数。',
 'performance + -s，/s/ 后读 /ɪz/。perform + -ance 的名词在中古英语已有；perform 经法语 parfornir 完成、充分提供等材料，词形曾受 forme 影响，不按拉丁形式词硬拼。',
 [['法语完成词 → perform；加 -ance → performance','完成、执行 → 实际表现、演出'],['performance + -s → performances','多场演出；分别发生的表现']],
 'live performances 现场演出；recent performances 最近几次表现；give performances 进行表演。',
 'performances at the theatre 剧院演出；strong performances 出色表现。','performance 泛说设备性能、工作表现时常不可数；performances 常数场次或一次次实际发挥。比较时要看是在说演出还是其他活动。',
 ('The festival includes performances by local musicians.','节庆包含当地音乐家的演出。'),('Her recent performances show how much she has improved.','她最近几次的表现显示，她进步了很多。'),sources=['https://en.wiktionary.org/wiki/performances#English','https://www.etymonline.com/word/performance'])
W('consideration','英 /kənˌsɪdəˈreɪʃən/；美 /kənˌsɪdəˈreɪʃən/','考虑、思量；应考虑的因素；体贴、顾及',
 '先把一件事认真放在心上，再决定怎么办，是 consideration。把别人的处境也放进去，就是体贴；需要放进去权衡的那一项，则是考虑因素。',
 '现代可认 consider + -ation 的配套关系；历史名词经法语 consideracion 或直接借拉丁 cōnsīderātiō，接 cōnsīderāre 仔细察看、思量，名词有独立且较早的英语记录。更早星辰词源分析有分歧。',
 [['拉丁 cōnsīderātiō → 法语或直接 → consideration','仔细察看、留在心上 → 思量、顾及'],['英语意义扩展','考虑的过程；权衡因素；对他人的体贴']],
 'under consideration 正在考虑中；take... into consideration 把……纳入考虑；show consideration for others 体谅别人。',
 'an important consideration 一个重要因素；out of consideration for somebody 出于对某人的顾及。','思量、体贴的 consideration 常不可数；一个要权衡的因素可以说 a consideration。不要把所有句子都译成抽象的考虑，先看是在权衡事情还是顾及别人。',
 ('The proposal is still under consideration.','提案仍在考虑中。'),('Cost is an important consideration when choosing materials.','选择材料时，成本是一个重要考虑因素。'),('Please show consideration for your neighbours.','请体谅一下邻居。'),sources=['https://en.wiktionary.org/wiki/consideration#English','https://www.etymonline.com/word/consideration'])
W('counts','/kaʊnts/','计数、计算；算数、重要〔第三人称单数〕；计数结果、项数；伯爵〔复数，另一来源〕',
 '把东西一项项纳入数里，是 counts 的计数动作；如果某件事应该算进去、产生分量，就有算数、重要的用法。',
 'count + -s，/t/ 后读 /s/。计数词经法语 conter、conte 接拉丁 computāre；伯爵名词另经法语接拉丁 comes 随从、同伴。现代同形，历史分支不同。',
 [['拉丁 computāre → 法语 → 计数 count；comes → 伯爵 count','计算与头衔两支分开'],['count + -s → counts','单数主语计数、起作用；多项计数或头衔人物']],
 'counts the chairs 数椅子；every minute counts 每一分钟都重要；counts as evidence 算作证据。',
 'counts of visitors 访客计数；on all counts 在各方面、各项上。','count as 是被算作某种身份、作用。It counts 强调这件事有分量、能计入，不必真的拿计算器。伯爵义按历史头衔场景判断。',
 ('She counts the chairs before the meeting.','她在会前数椅子。'),('When the train is about to leave, every minute counts.','火车快开时，每一分钟都重要。'),sources=['https://en.wiktionary.org/wiki/counts#English','https://en.wiktionary.org/wiki/count#English'])
W('creates','/kriˈeɪts/','创造、创作、造成〔第三人称单数〕',
 '让原来没有的东西出现，是 creates。可以创造作品、机会，也可以无意中造成麻烦，结果好坏要看宾语。',
 'create + -s，/t/ 后读 /s/。中古英语 create 接拉丁 creātus 分词词干，来自 creāre 使产生；现代单数现在式直接加 s。',
 [['拉丁 creāre、creātus → create','使产生 → 创造、造成'],['create + -s → creates','单数主语让某个新事物、局面出现']],
 'creates opportunities 创造机会；creates a problem 造成问题；creates a design 创作设计。',
 'creates space 腾出、创造空间；creates a sense of calm 营造平静感。','create 的对象可以是具体作品，也可以是条件、感受或问题。creates 不自带赞美，creates confusion 造成混乱同样常见。',
 ('The new layout creates more space for readers.','新布局为读者腾出了更多空间。'),('The unclear message creates confusion.','含糊的信息造成混乱。'),sources=['https://en.wiktionary.org/wiki/creates#English','https://en.wiktionary.org/wiki/create#English'])
W('funded','/ˈfʌndɪd/','资助了；有资金支持的〔过去式、过去分词〕',
 '给一件事垫上能运转的资金底子，就是 funded。项目、研究、修缮都要有人或机构提供经费。',
 'fund + -ed，/d/ 后读 /ɪd/。fund 名词经法语等接拉丁 fundus 底部、地产，后有财产、储备、资金义；英语动词再表示提供资金。',
 [['拉丁 fundus → 法语等 → fund 名词、动词','底部、财产 → 资金储备、提供资金'],['fund + -ed → funded','已经出资；得到经费支持']],
 'funded by donations 由捐款资助；a funded project 有经费的项目；publicly funded 公共资金支持的。',
 'fully funded 经费全部落实的；funded the repairs 出资维修。','funded 来自 fund 资助；founded 来自 found 建立，这两个过去形式不同。funded a school 可以是资助学校，founded a school 是创办学校。',
 ('The library project was funded by local donations.','图书馆项目由当地捐款资助。'),('The grant funded repairs to the old building.','这笔资助金支付了老建筑维修费用。'),sources=['https://en.wiktionary.org/wiki/funded#English','https://en.wiktionary.org/wiki/fund#English'])
W('guaranteed','/ˌɡærənˈtiːd/','保证了、担保了；有保证的〔过去式、过去分词〕',
 '有人正式站出来说这件事会兑现、会负责，是 guaranteed。可以保证座位、提供某项服务，或为产品承担约定责任。',
 'guarantee 去 e + -ed → guaranteed，保留 ee，末尾读 /d/。guarantee 接法语 guarantie 等担保词族，与 guaranty、warranty 有历史关系；英语动词及过去形式后发展。',
 [['法语担保词族 → guarantee','作保证、承担责任的安排'],['guarantee 去 e + -ed → guaranteed','过去作保证；被承诺能获得或实现']],
 'a guaranteed seat 保证有的座位；guaranteed delivery 有承诺的送达；guaranteed to work 被保证能奏效。',
 'guaranteed a place 保证给一个名额；guaranteed by the organiser 由主办方担保。','guaranteed 说明存在保证或作出承诺，具体保证什么、由谁负责，要看完整说法。The organiser guaranteed... 中是主办方在作保证。',
 ('Booking early guaranteed us seats on the train.','提前订票确保我们坐火车时有座位。'),('The organiser guaranteed that everyone would receive the materials.','主办方保证每个人都能收到材料。'),sources=['https://en.wiktionary.org/wiki/guaranteed#English','https://en.wiktionary.org/wiki/guarantee#English'])
W('existed','/ɪɡˈzɪstɪd/','存在过、存在着〔过去式、过去分词〕',
 '在某个时候，它确实在那里、有这个东西，就是 existed。可以是房子、制度、某种关系，也可以是一种尚未被察觉的问题。',
 'exist + -ed，/t/ 后读 /ɪd/。拉丁 ex- 向外 + sistere 站定 → exsistere 出现、存在，经法语和拉丁相关路线进入英语；现代过去式再加 ed。',
 [['拉丁 exsistere → 法语、英语 exist','站出来、出现 → 实际存在'],['exist + -ed → existed','在过去存在；已经持续存在过']],
 'existed before the town 在城镇出现前已存在；existed for years 已存在多年；never existed 从未存在。',
 'existed in several forms 以几种形式存在过；problems that existed 当时存在的问题。','exist 通常不及物，直接说明某物存在。has existed 给持续到相关时点的存在，existed 则可把时间放在过去叙述中。',
 ('The village existed long before the railway was built.','铁路修建很久以前，这个村庄就已经存在。'),('The records show that the problem existed for several years.','记录显示，这个问题当时已存在数年。'),sources=['https://en.wiktionary.org/wiki/existed#English','https://en.wiktionary.org/wiki/exist#English'])
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_zs',ROOTS,WORDS)
 extend_lessons()
