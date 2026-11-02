"""Common objects, responsibilities, tools and links."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'B2440':dict(words=['bone','bones'],label='bone → bones：骨头与支撑轮廓',note='本族骨词，实体与抽象骨架场景结合。'),
 'B3752':dict(words=['brand','brands'],label='brand → brands：火印到品牌',note='古英语燃烧木条词，烙印、商品标识用途逐步发展。'),
 'C0247':dict(words=['connection','connections'],label='connection → connections：接起来的纽带',note='拉丁 connexio 经法语、中古英语传入，现代拼写更接近 connect。'),
 'C0515':dict(words=['duty','duties'],label='duty → duties：应做的事与应缴的税',note='中古英语 due 加名词材料，远源是欠、应有词族。'),
 'B3493':dict(words=['guard','guards'],label='guard → guards：看守的人与防护物',note='日耳曼看守词经法语进入，与 ward 同源而路径不同。'),
 'B3572':dict(words=['instrument','instruments'],label='instrument → instruments：配备好的工具',note='拉丁 instrumentum 经法语借入，乐器、仪器和手段各有现代用途。'),
 'B2652':dict(words=['mother','mothers'],label='mother → mothers：母亲与照料',note='本族古老亲属词，名词、动词现代用途相连。'),
 'C0655':dict(words=['release','releases'],label='release → releases：松开、放出与发布',note='法语松开词接拉丁 relaxare，和 relax 同源。'),
 'C1478':dict(words=['technology','technologies'],label='technology → technologies：技艺知识与具体技术',note='希腊技艺加论述词，经拉丁化形式借入，现代不局限于电子产品。'),
 'B4101':dict(words=['trend','trends'],label='trend → trends：朝哪个方向走',note='本族转、滚、延伸的旧词发展为趋势，现代网络流行义后扩展。'),
 'B3375':dict(words=['trial','trials'],label='trial → trials：试验、审理与考验',note='法语试、挑选词族，名词有独立借入历史。'),
 'B2524':dict(words=['board','boards'],label='board → boards：木板、桌边议事与登上',note='古英语木板与船侧词史交叠，委员会和登交通工具的用途分别解释。'),
 'A1862':dict(words=['category','categories'],label='category → categories：说明属性到归类',note='希腊公开断言词进入逻辑范畴，再有一般分类用途。'),
 'C1437':dict(words=['district','districts','restriction','restrictions'],label='district → districts；restriction → restrictions：管辖范围与限制',note='共同接拉丁拉紧、约束词族，两组名词各有借入历史。'),
 'C1293':dict(words=['secret','secrets'],label='secret → secrets：分隔开不公开',note='拉丁分开、筛分词的分词及名词，经法语等形成秘密用途。'),
}
W('bones','英 /bəʊnz/；美 /boʊnz/','骨头、骨骼；基本骨架〔复数〕；剔骨〔第三人称单数〕',
 '身体里硬实、支撑形状的部分，是 bones。把一个计划最基本的轮廓叫 bare bones，也是在看还没填细节的骨架。',
 'bone + -s，/n/ 后读 /z/。bone 继承古英语 bān 骨头，名词可表材料或个体骨头；英语后来有给食材剔骨的动词。',
 [['古英语 bān → bone','骨头、骨质 → 支撑结构的比喻'],['bone + -s → bones','多块骨头、骨骼；单数主语剔骨']],
 'broken bones 骨折的骨头；fish bones 鱼刺；the bare bones of a plan 计划的基本框架。',
 'bones in the skeleton 骨骼中的各块骨头；bones the fish 给鱼剔刺。','bones 是一块块骨头，bone 还可作骨质材料。the bare bones 强调最基本的框架，常意味着细节尚待补足。',
 ('The museum displays the bones of a large animal.','博物馆展出一只大型动物的骨骼。'),('She outlined the bare bones of the plan.','她勾勒了计划的基本框架。'),sources=['https://en.wiktionary.org/wiki/bones#English','https://en.wiktionary.org/wiki/bone#English'])
W('brands','/brændz/','品牌、牌子；烙印〔复数〕；打烙印、将……称为〔第三人称单数〕',
 '用一个标记让人认出这是谁、属于哪家，是 brands 的品牌画面。较早的标记可以用火烙出来，后来转到商品名称和身份印象上。',
 'brand + -s，/d/ 后读 /z/。brand 接古英语 brand 燃烧木条、火把等，烙印及标识商品来源的用途后来发展；动词打烙印和贴上某种标签也相连。',
 [['古英语 brand → brand','燃烧物、火印 → 识别标记、商品品牌'],['brand + -s → brands','多个品牌、烙印；单数主语打标记、定性']],
 'different brands 不同牌子；local brands 当地品牌；brands it a failure 把它斥为失败。',
 'compare brands 比较品牌；well-known brands 知名品牌。','brand 强调识别来源和相关形象，product 是产品本身。brand somebody as... 作动词时常带强烈、负面的定性语气。',
 ('The shop sells several brands of tea.','商店出售几个牌子的茶。'),('She compared the ingredients used by different brands.','她比较了不同品牌使用的配料。'),sources=['https://en.wiktionary.org/wiki/brands#English','https://en.wiktionary.org/wiki/brand#English'])
W('connections','/kəˈnekʃənz/','连接、联系、关系；人脉；交通接续〔复数〕',
 '把两个点接起来，是 connections。接的是设备，就有连接；接的是人，就有关系；一程交通接上下一程，就是换乘衔接。',
 'connection + -s，/n/ 后读 /z/。名词经古法语 connexion 接拉丁 connexiō 联结，进入中古英语；后来的 connection 拼写受 connect 等影响，现代可认 connect 与 ion 的对应。',
 [['拉丁 connexiō → 法语 connexion → 中古英语','绑在一起、相连 → 联结、关系'],['connection + -s → connections','多处连接、多种关联；人际或交通接续']],
 'connections between ideas 概念间联系；electrical connections 电气连接；make connections 建立联系、看出关联。',
 'family connections 家庭关系；train connections 列车衔接班次。','connections 作人脉常指能联系到的人和关系；交通里则关注能否接上下段行程。具体含义看连起来的是什么。',
 ('The course helps students see connections between subjects.','课程帮助学生看见学科之间的联系。'),('The station has good connections to nearby towns.','这座车站有方便衔接附近城镇的交通线路。'),sources=['https://en.wiktionary.org/wiki/connections#English','https://www.etymonline.com/word/connection'])
W('duties','英 /ˈdjuːtiz/；美 /ˈduːtiz/','职责、应做的工作；税款、关税〔复数〕',
 '因为角色、承诺或规定，有些事是自己应当交出的那一份，这就是 duties 的责任画面。应缴的税也保留应交付的线索。',
 'duty 的辅音字母 + y 改 ies。中古英语 duete 接 due 应有、所欠与名词材料，较早经法语连到拉丁 dēbēre 欠；现代职责与税费用途分别发展。',
 [['due 词族 → 中古英语 duete → duty','应当给付的东西 → 应做之事、应缴税'],['duty：y 改 ies → duties','多项职责、工作或税款']],
 'daily duties 日常职责；carry out duties 履行职责；import duties 进口关税。',
 'duties of the manager 经理的职责；share the duties 分担任务。','duties 比普通 tasks 更强调因身份、角色而应负责。关税语境要看 import、customs 等搭配，不能译成进口工作。',
 ('Her duties include answering emails and arranging meetings.','她的职责包括回复邮件和安排会议。'),('The two assistants shared the daily duties.','两位助理分担日常工作。'),sources=['https://en.wiktionary.org/wiki/duties#English','https://en.wiktionary.org/wiki/duty#English'])
W('guards','英 /ɡɑːdz/；美 /ɡɑːrdz/','警卫、守卫；防护装置〔复数〕；保护、看守〔第三人称单数〕',
 '站在容易被侵入、伤到的位置，把危险挡住，是 guards。人可以做守卫，机器上的罩子也可以做防护装置。',
 'guard + -s，/d/ 后读 /z/。名词、动词经法语 garde、garder 等进入英语，背后接日耳曼看守词族；与本族 ward 同源，传入路径不同。',
 [['日耳曼看守词 → 法语 → guard','看守、保护 → 守卫者、防护物及动作'],['guard + -s → guards','多个警卫、防护装置；单数主语保护']],
 'security guards 保安人员；guards at the gate 门卫；guards the entrance 守住入口。',
 'guards on the machine 机器防护装置；guards against errors 防范错误。','guards 作人、装置都可能，先看场景。guard against 强调防止某种风险发生；guard something 则直接看守、保护对象。',
 ('Two guards stood beside the entrance.','两名警卫站在入口旁。'),('The cover guards the moving parts against dust.','这个罩子保护活动部件，防止灰尘进入。'),sources=['https://en.wiktionary.org/wiki/guards#English','https://en.wiktionary.org/wiki/guard#English'])
W('instruments','/ˈɪnstrəmənts/','乐器；仪器、工具；手段〔复数〕',
 '为了把某件事做成而配备的工具，是 instruments 的共同理解。音乐家拿它奏乐，实验人员拿它测量，组织也能把某种措施当作实现目标的手段。',
 'instrument + -s，/t/ 后读 /s/。经法语接拉丁 īnstrūmentum 配备、工具，来自 īnstruere 装配、备好与名词材料 mentum；整体早已在拉丁语形成。',
 [['拉丁 īnstruere、īnstrūmentum → 法语 → instrument','配备、准备 → 可用来做事的器具'],['instrument + -s → instruments','多件乐器、仪器；多种实现目标的手段']],
 'musical instruments 乐器；measuring instruments 测量仪器；instruments of change 推动改变的手段。',
 'play instruments 演奏乐器；check the instruments 检查仪表、仪器。','instrument 要看领域才能选中文：乐器、仪器、手段都常见。仪表盘上的 instruments 通常负责显示或测量，不是乐器。',
 ('The children tried several musical instruments.','孩子们尝试了几种乐器。'),('The researchers checked the measuring instruments.','研究人员检查了测量仪器。'),sources=['https://en.wiktionary.org/wiki/instruments#English','https://en.wiktionary.org/wiki/instrument#English'])
W('mothers','英 /ˈmʌðəz/；美 /ˈmʌðərz/','母亲〔复数〕；像母亲一样照料〔第三人称单数〕',
 'mothers 最直接就是几位母亲。作动词时，把另一个人当孩子般照顾、操心，能是关怀，也可能显得照顾过头。',
 'mother + -s，末尾读 /z/。mother 继承古英语 mōdor，经中古英语 moder 发展；与拉丁 māter 等是古老亲属词的同源关系，不是现代英语直接借了拉丁词。',
 [['古英语 mōdor → 中古英语 moder → mother','母亲；英语后有像母亲一样照料的动词'],['mother + -s → mothers','多位母亲；单数主语照料、操心']],
 'mothers and children 母亲和孩子；working mothers 在职母亲；mothers her younger siblings 像母亲一样照料弟妹。',
 'support for new mothers 给新手母亲的支持；mothers in the community 社区里的母亲。','mothers 是复数，mother’s 是单数所有格，mothers’ 是复数所有格。撇号位置会影响意思，和复数的 s 分清。',
 ('The group offers support to new mothers.','这个小组为新手母亲提供支持。'),('Several mothers helped organise the school event.','几位母亲帮助组织了学校活动。'),sources=['https://en.wiktionary.org/wiki/mothers#English','https://en.wiktionary.org/wiki/mother#English'])
W('releases','/rɪˈliːsɪz/','释放、放出、发布〔第三人称单数〕；发行物、发布消息等〔复数〕',
 '把原来受限制、未对外开放的东西放出来，是 releases 的线索。人被释放，气体被放出，影片、软件、消息则被公开提供。',
 'release + -s，/s/ 后读 /ɪz/。动词经古法语 relaisser、relesser 等接拉丁 relaxāre 松开，含 re- 与 laxāre 松；名词另有法语 reles 等来源，现代发布义后来扩展。',
 [['拉丁 relaxāre → 法语 → release','松开、放手 → 解除限制、释放'],['release + -s → releases；发布用途','单数主语放出；多次发布、发行物']],
 'releases information 发布信息；releases air 放出空气；new releases 新发行作品、版本。',
 'press releases 新闻稿；releases the button 松开按钮。','release 在这里和 relax 接同一较早词族。新发行作品叫 releases 时，数的是出版、发行项目；release a person 则是解除拘禁等限制。',
 ('The company releases a new version each year.','公司每年发布一个新版本。'),('The valve releases air when the pressure rises.','压力升高时，阀门会放气。'),sources=['https://en.wiktionary.org/wiki/releases#English','https://www.etymonline.com/word/release'])
W('technologies','英 /tekˈnɒlədʒiz/；美 /tekˈnɑːlədʒiz/','技术、工艺、技术系统〔复数〕',
 '把做事的方法变成可应用的一套本领，是 technologies 的技术画面。可以是净水、制造、通信等，不只指手里看得见的电子设备。',
 'technology 的辅音字母 + y 改 ies。接希腊 tekhnologia 的拉丁化形式，tekhnē 技艺 + logia 论述、系统研究；英语早期讲技艺的系统论述，现代具体技术义后扩展。',
 [['希腊技艺、论述词 → technology','系统讲解某种技艺 → 技术知识与应用'],['technology：y 改 ies → technologies','可分别说明的多种技术、工艺']],
 'new technologies 新技术；water-saving technologies 节水技术；communication technologies 通信技术。',
 'develop technologies 开发技术；technologies used in manufacturing 制造业采用的工艺。','technology 泛说技术领域可以不可数；technologies 把不同技术体系分开。techniques 常更具体地指某项操作方法，范围不总与 technologies 相同。',
 ('The project compares different technologies for cleaning water.','项目比较几种净水技术。'),('New technologies are changing how the products are made.','新技术正在改变这些产品的制造方式。'),sources=['https://en.wiktionary.org/wiki/technologies#English','https://www.etymonline.com/word/technology'])
W('trends','/trendz/','趋势、走向、流行风尚〔复数〕；趋向、成为热门〔第三人称单数〕',
 '许多变化连着看，整体朝一个方向走，就是 trends。穿衣可以有流行趋势，数据也可以有长期上升、下降的走势。',
 'trend + -s，/d/ 后读 /z/。trend 接古英语 trendan、中古英语 trenden 转、滚等旧动作，后有向某方向延伸的意思，现代再用于事情发展的趋势。',
 [['古英语、中古英语转动、延伸词 → trend','朝某方向延伸 → 变化走向、趋势'],['trend + -s → trends','多种趋势；单数主语趋向、成为热门']],
 'long-term trends 长期趋势；fashion trends 时尚潮流；trends in the data 数据中的趋势。',
 'identify trends 识别趋势；trends upward 总体上升。','trend 关注总体方向，短时一次波动不一定足以说明趋势。网络中 a topic trends 是话题成为热门，也要结合平台语境。',
 ('The report examines long-term trends in travel.','报告研究旅行方面的长期趋势。'),('The graph helps us see trends in the data.','图表帮助我们看清数据中的趋势。'),sources=['https://en.wiktionary.org/wiki/trends#English','https://en.wiktionary.org/wiki/trend#English'])
W('trials','/ˈtraɪəlz/','试验、试用；审理、庭审；考验〔复数〕',
 '把一件事放到实际检验中，看看是否成立、能否奏效，是 trials 的共同理解线索。技术试用、法院审理、人生考验，检验的对象不同。',
 'trial + -s，/l/ 后读 /z/。trial 经盎格鲁法语 trial、triel 接 trier 挑选、试验词族，与 try 有历史联系；al 在这条历史里是动作名词材料。',
 [['法语试、挑选词族 → trial','检验、尝试 → 试验、审理、考验'],['trial + -s → trials','多次试验、多场审理或多种考验']],
 'field trials 实地试验；free trials 免费试用；court trials 法庭审理；trials of everyday life 日常生活的考验。',
 'run trials 开展试验；early trials 早期试验。','trial 的试验义强调实际检验，trial 的庭审义按法律程序语境理解。作动词试用时也有 trials 形式，日常先掌握这些常见名词场景。',
 ('The team ran several trials before choosing the final design.','团队进行了几次试验才选定最终设计。'),('The book describes the trials of starting a small business.','这本书描述创办小企业面临的种种考验。'),sources=['https://en.wiktionary.org/wiki/trials#English','https://en.wiktionary.org/wiki/trial#English'])
W('boards','英 /bɔːdz/；美 /bɔːrdz/','木板、板面；委员会、董事会〔复数〕；登上〔第三人称单数〕',
 '一块板可以铺路、写字，也能成为桌子；围着桌子议事的人，后来有 board 委员会的用法。登交通工具的动词则联系船边、船上的另一路旧义。',
 'board + -s，/d/ 后读 /z/。古英语 bord 有木板、桌子以及船侧等旧用法，远处是否全同源有分歧，早期已交叠；委员会、伙食、登乘等用途分别发展。',
 [['古英语 bord 等 → board','木板、桌子；船边等旧义相互影响'],['board + -s → boards；领域扩展','多块板、多个委员会；单数主语登上交通工具']],
 'wooden boards 木板；notice boards 布告板；school boards 学校委员会；boards the train 上火车。',
 'boards of directors 董事会；boards the bus at noon 中午上公交。','委员会 board 沿围桌议事的用法发展；动词 board 直接接车船飞机。on board 是在交通工具上，也可说参与、支持某项安排。',
 ('They laid wooden boards across the muddy path.','他们把木板铺在泥泞小路上。'),('She boards the train at the next station.','她在下一站上火车。'),sources=['https://en.wiktionary.org/wiki/boards#English','https://en.wiktionary.org/wiki/board#English'])
W('categories','英 /ˈkætəɡəriz/；美 /ˈkætəɡɔːriz/','类别、门类、范畴〔复数〕',
 '把一堆东西按某个共同特点放到不同格子里，这些格子就是 categories。这个画面帮助理解现代分类义，较早词史则走过公开断言和逻辑范畴。',
 'category 的辅音字母 + y 改 ies。经法语 catégorie、拉丁 categoria 接希腊 katēgoria，较早 kata 与 agoreuein 公开说、断言等材料；逻辑里的范畴义再扩展为一般类别。',
 [['希腊 katēgoria → 拉丁、法语 → category','断言、逻辑范畴 → 一般分类'],['category：y 改 ies → categories','多个归类后的类别、门类']],
 'different categories 不同类别；sort into categories 按类整理；categories of books 图书类别。',
 'broad categories 大类；categories on the form 表格中的分类项。','category 的分法依目的、标准而定，同一对象可以在不同分类体系里放到不同格子。categorize 是分类动词，categories 是类别复数。',
 ('The library divides the books into several categories.','图书馆把图书分为几类。'),('Choose the categories that best describe your interests.','请选择最能描述你兴趣的类别。'),sources=['https://en.wiktionary.org/wiki/categories#English','https://www.etymonline.com/word/category'])
W('districts','/ˈdɪstrɪkts/','地区、区域；行政区〔复数〕',
 '把一片地方圈成能管辖、办事或按共同特点识别的范围，就是 districts。可以是行政区，也可以只是商业区、住宅区等地区。',
 'district + -s，/t/ 后读 /s/，结尾 /kts/ 连读。经法语接中世纪拉丁 districtus 管辖、管辖范围，关联 distringere 拉紧、约束、强制，较早 dis- 与 stringere 拉紧。',
 [['拉丁约束、管辖词 → 法语 → district','管得到的范围 → 地区、区域'],['district + -s → districts','多个行政区或按功能识别的地区']],
 'school districts 学区；shopping districts 购物区；rural districts 乡村地区。',
 'districts near the river 河边地区；residential districts 住宅区。','district 的边界可能由行政制度划定，也可能是一般地域称呼。school district 常有具体管理范围，不能一律译为城区。',
 ('The city is divided into several districts.','这座城市分为几个区。'),('The guide describes the main shopping districts.','指南介绍几个主要购物区。'),sources=['https://en.wiktionary.org/wiki/districts#English','https://en.wiktionary.org/wiki/district#English'])
W('restrictions','/rɪˈstrɪkʃənz/','限制、限制条件〔复数〕',
 '本来可做的范围，被绳子收紧了一圈，就是 restrictions 的限制画面。可以限制时间、人数、用途或进入某个地方的资格。',
 'restriction + -s，/n/ 后读 /z/。名词经法语 restriction 或晚期拉丁 restrictiō 借入，联系 re- 回与 stringere 拉紧的 restrict- 分词词干；英语名词早于现代 restrict 动词。',
 [['拉丁 restrictiō → 法语或直接 → restriction','拉紧、收住 → 限制条件'],['restriction + -s → restrictions','多项限制、约束条件']],
 'parking restrictions 停车限制；restrictions on use 使用限制；lift restrictions 解除限制。',
 'age restrictions 年龄限制；restrictions on access 进入、访问限制。','restriction on something 说明限制作用在哪方面；a restriction 不一定等于完全禁止，也可能限定次数、时段或范围。',
 ('The sign explains the parking restrictions.','标牌说明了停车限制。'),('There are restrictions on how the room may be used.','这个房间的使用方式受到限制。'),sources=['https://en.wiktionary.org/wiki/restrictions#English','https://en.wiktionary.org/wiki/restriction#English'])
W('secrets','/ˈsiːkrəts/','秘密、隐情；秘诀〔复数〕',
 '把一部分信息隔在外人看不到的地方，是 secrets。若某个关键办法别人不知道，它也可以是成功的秘诀。',
 'secret + -s，/t/ 后读 /s/。拉丁 sē- 分开 + cernere 筛分 → sēcernere，分词 sēcrētus 隔开的、隐蔽的与名词 sēcrētum，经法语等通向英语 secret。',
 [['拉丁 sēcernere、sēcrētus → 法语等 → secret','分隔出来、隐蔽 → 不公开的事'],['secret + -s → secrets','多项秘密、隐情；不易知道的关键方法']],
 'keep secrets 保守秘密；share secrets 分享秘密；secrets of the craft 这门手艺的诀窍。',
 'family secrets 家庭隐情；reveal secrets 透露秘密。','a secret 可以是故意保密的信息，也可以是尚不易被了解的诀窍。the secret to success 常说成功关键；保密行为则常说 keep a secret。',
 ('She trusted him to keep her secrets.','她信任他会保守她的秘密。'),('The book explains some of the secrets of good storytelling.','这本书讲解了一些讲好故事的诀窍。'),sources=['https://en.wiktionary.org/wiki/secrets#English','https://en.wiktionary.org/wiki/secret#English'])
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_zp',ROOTS,WORDS)
 extend_lessons()
