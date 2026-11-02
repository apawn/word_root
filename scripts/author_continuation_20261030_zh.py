"""Common people, processes and abstract things in the plural."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'C0769':dict(words=['emotion','emotions','movement','movements'],label='emotion → emotions；movement → movements：感受被激起、事物在移动',note='两个名词有各自借入历史，现代复数分别数情绪、动作或运动。'),
 'C1439':dict(words=['instruction','instructions'],label='instruction → instructions：教导、搭好做事步骤',note='拉丁 instructio 经法语借入，与 instruct 相关而非现代才造。'),
 'C0189':dict(words=['procedure','procedures'],label='procedure → procedures：事情怎样往下走',note='法语进行方式词借入，与拉丁 procedere 向前走相连。'),
 'C1454':dict(words=['consume','consumer','consumers'],label='consume → consumer → consumers：消耗与使用者',note='consume 加表示人的 er，现代消费者不局限于吃喝。'),
 'C0276':dict(words=['critic','critics'],label='critic → critics：作出判断的人',note='希腊善于判断词经拉丁、法语借入，不把评论等同挑错。'),
 'A1697':dict(words=['research','researcher','researchers'],label='research → researcher → researchers：深入查考的人',note='research 加人物 er，学术、市场等领域均可用。'),
 'C1280':dict(words=['science','sciences'],label='science → sciences：知识到各门科学',note='拉丁知道、知识词经法语借入，现代学科范围有历史变化。'),
 'C0609':dict(words=['interview','interviews'],label='interview → interviews：面对面交流到访谈、面试',note='法语相互看、会面的表达进入英语，现代有名词和动词用途。'),
 'C1550':dict(words=['contribution','contributions'],label='contribution → contributions：各拿出一份',note='拉丁一起分配、付出的名词词族，经法语及拉丁路线借入。'),
 'C1624':dict(words=['version','versions'],label='version → versions：转成的不同样子',note='法语及拉丁转变、翻译词，扩展到软件和叙述版本。'),
 'B3338':dict(words=['risk','risks'],label='risk → risks：可能出问题的地方',note='法语、意大利危险词借入，更远词源仍有分歧。'),
 'C0401':dict(words=['profit','profits','manufacturer','manufacturers'],label='profit → profits；manufacturer → manufacturers：收益与制造者',note='获益接拉丁前进、做词族；制造者另接手工制作的构成。'),
 'C1627':dict(words=['invest','investor','investors'],label='invest → investor → investors：投入资源的人或机构',note='现代投资义经历从赋予、包裹到资金投入的扩展。'),
 'C1580':dict(words=['university','universities'],label='university → universities：共同体到大学',note='拉丁整体、团体的词经法语进入高等教育语境。'),
}
W('emotions','英 /ɪˈməʊʃənz/；美 /ɪˈmoʊʃənz/','情绪、情感〔复数〕',
 '心里被一件事带动起来的感受，是 emotions 的直观线索：开心、失落、紧张可以同时翻涌，也可以一个接一个出现。',
 'emotion + -s，/n/ 后读 /z/。emotion 借法语 émotion，接 émouvoir 激起，较早拉丁 ēmovēre，ē- 向外 + movēre 移动；英语早有骚动义，情感义后来扩展。',
 [['拉丁 ēmovēre → 法语 émotion → emotion','搅动、激起 → 强烈感受，再泛指情绪'],['emotion + -s → emotions','不同情绪或多种情感体验']],
 'mixed emotions 五味杂陈；express emotions 表达情绪；control your emotions 控制情绪。',
 'a range of emotions 各种情绪；strong emotions 强烈感情。','emotions 常把不同感受分别看；emotion 也能泛说情感。mixed emotions 不是一种固定的坏心情，而是几种感受交织。',
 ('She felt mixed emotions about leaving home.','对于离家，她心里五味杂陈。'),('Music can help us express difficult emotions.','音乐可以帮助我们表达难以说出的情绪。'),sources=['https://en.wiktionary.org/wiki/emotions#English','https://www.etymonline.com/word/emotion'])
W('instructions','/ɪnˈstrʌkʃənz/','说明、操作步骤、指示〔复数〕',
 '告诉别人先做什么、再做什么，让事情按步骤搭起来，就是 instructions 最常见的用途。它可以是设备说明，也可以是别人交代的要求。',
 'instruction + -s，/n/ 后读 /z/。instruction 经古法语接拉丁 instructiō，联系 instruere 搭建、配备、教导；含 in- 与 struere 建造，不是英语先造 instruct 再才有全部名词义。',
 [['拉丁 instruere、instructiō → 法语 → instruction','搭建、配备 → 教导、指示'],['instruction + -s → instructions','一项项应做的事；整套使用说明']],
 'follow the instructions 按说明做；read the instructions 阅读说明；give clear instructions 给出清楚指示。',
 'instructions for use 使用说明；instructions on how to assemble it 组装步骤。','instruction 泛说教学时常不可数；instructions 多指具体说明或指令。instructions for assembling 指供人遵循的组装步骤。',
 ('Read the instructions before assembling the shelf.','组装架子前先阅读说明。'),('She left clear instructions for the next shift.','她给下一班留下了清楚的工作指示。'),sources=['https://en.wiktionary.org/wiki/instructions#English','https://en.wiktionary.org/wiki/instruction#English'])
W('procedures','英 /prəˈsiːdʒəz/；美 /prəˈsiːdʒərz/','程序、办事流程、操作规程；医疗操作〔复数〕',
 '事情从开始到完成，照什么顺序往下走，是 procedures 的流程画面。常是大家约定或机构规定的一套做法。',
 'procedure + -s，末尾读 /z/。procedure 借法语 procédure 进行的方式，接 proceder，较早拉丁 prō- 向前 + cēdere 走 → prōcēdere；不当作现代 proceed 随手接 ure。',
 [['拉丁 prōcēdere → 法语 procédure → procedure','往前进行 → 开展事情的方法、程序'],['procedure + -s → procedures','不同流程或分别进行的操作']],
 'safety procedures 安全规程；follow procedures 遵循流程；application procedures 申请程序。',
 'standard procedures 标准操作规程；procedures for reporting problems 问题上报流程。','procedure 强调做法和步骤；process 更广，也可指自然发生的过程。医疗中的 procedures 可能含检查、治疗操作，不能一律译成大手术。',
 ('All staff must learn the emergency procedures.','所有员工都必须学习应急规程。'),('The guide explains the procedures for applying.','指南说明了申请流程。'),sources=['https://en.wiktionary.org/wiki/procedures#English','https://www.etymonline.com/word/procedure'])
W('consumers','英 /kənˈsjuːməz/；美 /kənˈsuːmərz/','消费者；消耗资源的人或事物〔复数〕',
 '东西最后被谁买来用、花掉或消耗掉，谁就处在 consumer 的位置。consumers 可以是购物的人，也可以是大量用能的机构。',
 'consume 去末尾 e + -er → consumer，再加 -s。consume 经法语、拉丁 cōnsūmere 用尽词族，含 con- 与 sūmere 拿取；er 把焦点转到使用、消耗的一方。',
 [['consume + -er → consumer','消耗、使用 → 使用者、消费者'],['consumer + -s → consumers','多个消费者或消耗资源的主体']],
 'consumers of electricity 用电方；protect consumers 保护消费者；consumers’ needs 消费者的需要。',
 'ordinary consumers 普通消费者；major energy consumers 主要能源消耗方。','customer 强调与某个商家交易的顾客关系；consumer 强调最终使用、消耗商品或服务的角色。两者经常重合，观察角度不同。',
 ('Consumers are asking for clearer information on labels.','消费者正要求标签提供更清楚的信息。'),('Large factories are major consumers of electricity.','大型工厂是用电大户。'),sources=['https://en.wiktionary.org/wiki/consumers#English','https://en.wiktionary.org/wiki/consumer#English'])
W('critics','/ˈkrɪtɪks/','评论家、批评者〔复数〕',
 '看过一件作品或一个方案后，作出评价的人，是 critics。评价可以赞赏，也可以反对，不是每位 critic 都只会挑毛病。',
 'critic + -s，/k/ 后读 /s/。critic 借法语 critique 等，较早接拉丁 criticus、希腊 kritikos 善于判断，和 krinein 区分、判断的词族相连。',
 [['希腊 kritikos → 拉丁、法语 → critic','善于作判断 → 评论者、评价者'],['critic + -s → critics','多位评论家；提出批评的人']],
 'film critics 影评人；critics of the policy 政策的批评者；praised by critics 获评论界赞赏。',
 'leading critics 主要评论家；answer the critics 回应批评者。','critic 是人，criticism 是批评或评论内容。critics of a plan 往往偏反对者，film critics 则是职业或角色名称，立场不预先确定。',
 ('The film received praise from several critics.','这部电影获得了几位评论家的赞赏。'),('Critics of the plan asked for more evidence.','这项计划的批评者要求提供更多证据。'),sources=['https://en.wiktionary.org/wiki/critics#English','https://en.wiktionary.org/wiki/critic#English'])
W('researchers','英 /rɪˈsɜːtʃəz/；美 /ˈriːsɜːrtʃərz/，亦有后重音读法','研究人员、调查研究者〔复数〕',
 '不是只看一眼，而是持续找资料、核对、试验，想把问题弄明白的人，是 researchers。研究对象可以是自然现象，也可以是市场、历史或人的行为。',
 'research + -er → researcher，再加 -s，结尾读 /z/。research 经法语 recherche 等接查找、深入搜索词族；re- 在较早构成中常起加强作用，不能凡事译成再次。',
 [['法语查找词 → research；加 -er → researcher','深入查考 → 从事研究的人'],['researcher + -s → researchers','多位研究者']],
 'medical researchers 医学研究人员；researchers studying language 研究语言的人员；a team of researchers 研究团队。',
 'researchers at a university 某大学研究人员；market researchers 市场研究人员。','researcher 是身份、角色，不限定为有某种职称的科学家。research、researcher 的前后重音有变体，不能按专业领域硬分读法。',
 ('Researchers collected data from several schools.','研究人员从几所学校收集了数据。'),('The researchers compared the results of two experiments.','研究人员比较了两次实验的结果。'),sources=['https://en.wiktionary.org/wiki/researchers#English','https://en.wiktionary.org/wiki/researcher#English'])
W('sciences','/ˈsaɪənsɪz/','各门科学、科学学科〔复数〕',
 '把科学里的不同领域分别看作一门门学科，就是 sciences。它让人想到一套有方法、可检验和积累的知识领域。',
 'science + -s，/s/ 后增加 /ɪz/。science 经法语接拉丁 scientia 知识，关联 scīre 知道；英语早期知识范围较广，现代科学学科义逐渐发展。',
 [['拉丁 scientia → 法语 → science','知识、知道 → 科学知识与学科'],['science + -s → sciences','不同的科学领域']],
 'natural sciences 自然科学；social sciences 社会科学；the physical sciences 物理科学诸学科。',
 'courses in the sciences 理科课程；connections between the sciences 各科学领域之间的联系。','science 可以泛指科学，sciences 则把各门领域分开看。具体课程如何分 arts 与 sciences，要看学校和教育体系。',
 ('She is interested in both the natural and social sciences.','她对自然科学和社会科学都感兴趣。'),('The course explores connections between the sciences.','这门课程探讨各科学领域之间的联系。'),sources=['https://en.wiktionary.org/wiki/sciences#English','https://en.wiktionary.org/wiki/science#English'])
W('interviews','英 /ˈɪntəvjuːz/；美 /ˈɪntərvjuːz/','面试、采访、访谈〔复数〕；采访、面试〔第三人称单数〕',
 '双方专门坐下来，一方发问、另一方回应，是 interviews 最常见的场面。为工作筛选人，是面试；为了解经历或报道取材，是访谈、采访。',
 'interview + -s，/uː/ 后读 /z/。interview 借法语 entreveue 会面，相连 entre- 相互与 vue 看；英语后来有采访、面试及相应动词用途。',
 [['法语 entreveue → interview','相互见面 → 有目的的问答会谈'],['interview + -s → interviews','多次访谈、面试；单数主语进行采访或面试']],
 'job interviews 求职面试；interviews with local residents 对当地居民的访谈；conduct interviews 开展访谈。',
 'prepare for interviews 准备面试；interviews candidates 面试候选人。','interviews with somebody 是同某人的访谈，interviews somebody 则直接作动词。面试中提问者、应聘者双方都参与 interview，要看句中角色。',
 ('She has two job interviews next week.','她下周有两场求职面试。'),('The journalist interviews local artists for the programme.','记者为这个节目采访当地艺术家。'),sources=['https://en.wiktionary.org/wiki/interviews#English','https://en.wiktionary.org/wiki/interview#English'])
W('contributions','英 /ˌkɒntrɪˈbjuːʃənz/；美 /ˌkɑːntrɪˈbjuːʃənz/','贡献、捐助、投稿；缴付款项〔复数〕',
 '为了凑成一件更大的事，每人拿出自己的一份，是 contributions 的核心。可以拿出钱，也可以拿出想法、文章、时间或实际帮助。',
 'contribution + -s，/n/ 后读 /z/。名词接拉丁 contribūtiō，经法语、拉丁路线借入，较早 con- 一起 + tribuere 分配、给予 → contribuere；与 contribute 同族但名词有自身借入史。',
 [['拉丁 contribuere、contribūtiō → contribution','一起拿出、分担 → 一份贡献或交付'],['contribution + -s → contributions','不同人的贡献；多项捐助、投稿或缴款']],
 'contributions to the project 对项目的贡献；financial contributions 资金捐助；regular contributions 定期缴款。',
 'valuable contributions 有价值的贡献；contributions from readers 读者投稿。','contribution 不只捐钱，也可指推动事情前进的作用。to 后接受益的对象、领域或事业；具体是赞助还是约定缴款，要看语境。',
 ('The report acknowledges contributions from the whole team.','报告感谢了整个团队作出的贡献。'),('Small contributions helped pay for the new playground.','一笔笔小额捐助帮助支付了新操场的费用。'),sources=['https://en.wiktionary.org/wiki/contributions#English','https://en.wiktionary.org/wiki/contribution#English'])
W('movements','/ˈmuːvmənts/','动作、移动；运动、活动；乐章〔复数〕',
 '某个东西从原处动起来，是 movements 的起点。一个人的身体动作、一群人推动的社会运动、音乐作品里依次展开的大段落，都各有具体用法。',
 'movement + -s，/t/ 后读 /s/。movement 经法语 mouvement 等借入，现代可认 move + -ment；move 较早接拉丁 movēre 移动。复数在英语中形成。',
 [['拉丁 movēre → 法语 mouvement → movement','移动、动作；后有集体运动和乐章等义'],['movement + -s → movements','若干动作、活动或音乐段落']],
 'body movements 身体动作；social movements 社会运动；four movements 四个乐章。',
 'slow movements 缓慢的动作；movements of the camera 摄影机的移动。','movement 作乐章是音乐里的较大分段，要按作品结构理解。社会 movements 常有共同目标；身体 movements 则可只是手脚等的动作。',
 ('The camera followed the dancer’s movements.','摄像机跟随着舞者的动作。'),('The symphony has four movements.','这部交响曲有四个乐章。'),sources=['https://en.wiktionary.org/wiki/movements#English','https://en.wiktionary.org/wiki/movement#English'])
W('versions','英 /ˈvɜːʃənz/；美 /ˈvɜːrʒənz/','版本、不同形式；不同说法、译本〔复数〕',
 '同一个东西，被做成或讲成不同样子，就是 versions。核心仍认得出来，但文字、功能、语言或叙述角度可能不同。',
 'version + -s，/n/ 后读 /z/。version 经法语 version 及拉丁 versiō 转变、翻译词族，联系 vertere 转动；不是现代 verse 诗直接接 ion。',
 [['拉丁 versiō、法语 version → version','转变、转译 → 某种做成或表述的样子'],['version + -s → versions','多个版本、译本或事件说法']],
 'different versions 不同版本；earlier versions 早期版本；two versions of the story 同一故事的两种讲法。',
 'software versions 软件版本；English versions 英语译本、英语版本。','a version of events 是某人对事件的描述，不自动表示真实全貌。versions 可以并存，也可以是先后修改出的各版。',
 ('The two versions of the document contain different dates.','文件的两个版本写着不同的日期。'),('We heard several versions of the story.','我们听到了这个故事的几种讲法。'),sources=['https://en.wiktionary.org/wiki/versions#English','https://en.wiktionary.org/wiki/version#English'])
W('risks','/rɪsks/','风险、可能的危险〔复数〕；冒险做、使有遭受的危险〔第三人称单数〕',
 '事情还可能顺利，但也存在出问题的可能，这些可能出问题的地方就是 risks。动词则把自己或某样东西放到这种可能性里。',
 'risk + -s，/k/ 后读 /s/。risk 经法语接意大利危险、冒险相关词，更远有不同词源解释；不把礁石等某一故事写成定论。',
 [['法语、意大利相关词 → risk','面对危险或不确定损失的可能'],['risk + -s → risks','不同风险；单数主语冒某种风险']],
 'take risks 冒险；assess the risks 评估风险；risks losing the file 冒着丢失文件的风险。',
 'reduce risks 降低风险；risks associated with travel 与旅行相关的风险。','risk 是可能性，不等于坏结果已经发生。作动词可接名词或 -ing：risk a fall、risk falling；take a risk 是名词搭配。',
 ('The guide explains the risks of walking alone at night.','指南说明了夜间独自行走的风险。'),('She risks losing her work if she does not save the file.','如果不保存文件，她就有丢失工作成果的风险。'),sources=['https://en.wiktionary.org/wiki/risks#English','https://en.wiktionary.org/wiki/risk#English'])
W('profits','英 /ˈprɒfɪts/；美 /ˈprɑːfɪts/','利润、收益〔复数〕；获益〔第三人称单数〕',
 '做完一笔经营，把相关成本扣掉后留下的收益，是 profits 的常见意思。动词 profits 则说某个人或机构从中得到好处。',
 'profit + -s，/t/ 后读 /s/。profit 经古法语 profit 接拉丁 profectus 前进、进益，较早 prō- 向前 + facere 做 → proficere 前进、获益；动词另与法语及名词有关。',
 [['拉丁 proficere、profectus → 法语 → profit','前进、进益 → 收益、利润'],['profit + -s → profits','若干或多期利润；单数主语获益']],
 'annual profits 年度利润；share the profits 分享利润；profits from the arrangement 从这项安排中获益。',
 'profits rose 利润上升；profits after costs 扣除成本后的收益。','sales 是销售额，profits 是与成本比较后得到的利润；具体指标还要看 gross、net 等修饰。动词 profit from 表示从中获益。',
 ('The company used part of its profits to improve the workshop.','公司用部分利润改善了车间。'),('The report shows profits rising over three years.','报告显示利润连续三年上升。'),sources=['https://en.wiktionary.org/wiki/profits#English','https://en.wiktionary.org/wiki/profit#English'])
W('investors','英 /ɪnˈvestəz/；美 /ɪnˈvestərz/','投资者、投资机构〔复数〕',
 '把资源放进一个项目，期待它日后产生回报的人或机构，是 investors。投入可能带来收益，也可能有损失。',
 'invest + -or → investor，再加 -s，末尾读 /z/。invest 较早接拉丁 investīre 使穿上、覆盖，in- + vestīre 穿衣；英语资金投入义是后续扩展，or 表示行动主体。',
 [['拉丁 investīre → invest；金融用途扩展','赋予、投入 → 投入资源求回报'],['invest + -or + -s → investors','多位投资者或多家投资机构']],
 'private investors 私人投资者；potential investors 潜在投资者；attract investors 吸引投资者。',
 'investors in the project 项目的投资方；long-term investors 长期投资者。','investor 可以是个人，也可以是机构。shareholders 特指持有股份的一方，investors 的范围更广，不一定都采用持股形式。',
 ('The project attracted investors from several regions.','这个项目吸引了来自几个地区的投资者。'),('The company sent an update to its investors.','公司向投资方发送了最新进展。'),sources=['https://en.wiktionary.org/wiki/investors#English','https://en.wiktionary.org/wiki/investor#English'])
W('manufacturers','英 /ˌmænjuˈfæktʃərəz/；美 /ˌmænjuˈfæktʃərərz/','制造商、生产厂家〔复数〕',
 '把原料或零部件做成产品的一方，是 manufacturers。它们可能把成品交给店铺销售，也可能直接卖给使用者。',
 'manufacture 去 e + -er → manufacturer，再加 -s。manufacture 较早接拉丁 manū 用手与 factūra 制作的组合，经法语等进入英语；手工制作背景后来扩展到工业制造。',
 [['手与制作的拉丁组合 → manufacture','手工制作 → 制造、生产'],['manufacture + -er → manufacturer；加 -s','制造者、制造商 → 多家生产厂家']],
 'car manufacturers 汽车制造商；local manufacturers 当地厂家；manufacturers’ instructions 厂家的说明。',
 'manufacturers of electrical equipment 电气设备制造商；contact the manufacturers 联系厂家。','manufacturer 是制造方，seller 是销售方。两种角色可以由同一企业承担；拼写里的 -er 是完整后缀，不是把 manufacture 简单保留再加 r 的构词解释。',
 ('Several manufacturers produce parts for the same model.','几家制造商为同一型号生产零件。'),('The shop contacted the manufacturers about the fault.','商店就这个故障联系了厂家。'),sources=['https://en.wiktionary.org/wiki/manufacturers#English','https://en.wiktionary.org/wiki/manufacturer#English'])
W('universities','英 /ˌjuːnɪˈvɜːsɪtiz/；美 /ˌjuːnɪˈvɜːrsətiz/','大学〔复数〕',
 '把教师、学生组织到一起，从事高等学习和研究的共同体，是 university 的历史理解线索。universities 数不同的大学机构。',
 'university 的辅音字母 + y 改 ies。经盎格鲁法语、古法语接中世纪拉丁 ūniversitās 整体、团体，教育义连着师生共同体的短语；不是现代英语 universe 宇宙临时加 ity 才有大学。',
 [['拉丁 ūniversitās → 法语 → university','整体、团体 → 师生共同体、高等教育机构'],['university：y 改 ies → universities','多所大学']],
 'local universities 当地大学；apply to universities 申请大学；universities offering the course 开设这门课程的大学。',
 'cooperation between universities 大学之间的合作；students at several universities 几所大学的学生。','单数说 a university，因为开头读 /j/，不是按字母 u 选 an。不同国家 university 与 college 的机构关系各有习惯。',
 ('Several universities offer courses in this subject.','几所大学开设了这个学科的课程。'),('The project brings together researchers from three universities.','项目汇集了来自三所大学的研究人员。'),sources=['https://en.wiktionary.org/wiki/universities#English','https://www.etymonline.com/word/university'])
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_zh',ROOTS,WORDS)
 extend_lessons()
