"""Common plural and third-person forms, grouped with their bases."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'B2670':dict(words=['wing','wings'],label='wing → wings：从翅膀到侧边分支',note='借入北欧翅膀词，现代可指机翼、建筑侧翼或组织派别。'),
 'B3767':dict(words=['block','blocks'],label='block → blocks：块状物、街区与阻挡',note='木块词经法语借入，实体块状和挡住的用途各自展开。'),
 'C0251':dict(words=['copy','copies'],label='copy → copies：充足材料到复制件',note='拉丁充足词发展出抄本、复制的名词和动词，进入路线并行。'),
 'B2933':dict(words=['crime','crimes'],label='crime → crimes：指控、罪行',note='拉丁 crimen 经法语借入，更远来源有讨论。'),
 'C0560':dict(words=['episode','episodes'],label='episode → episodes：插入戏剧场次到一集、一段',note='希腊额外进入的构成，借入英语有法语或直接古典来源分析。'),
 'B3410':dict(words=['farmer','farmers'],label='farmer → farmers：承租人到农业经营者',note='历史通过法语及拉丁承租、固定付款词族，现代可认 farm 与 er。'),
 'B3678':dict(words=['stage','stages'],label='stage → stages：站脚处、舞台与阶段',note='法语位置词接拉丁站立词族，现代名词、动词分开看。'),
 'B2541':dict(words=['winner','winners'],label='win → winner → winners：赢与获胜者',note='本族词加表示人的 er，复数再加 s。'),
 'B2844':dict(words=['cut','cuts'],label='cut → cuts：切开、切口与削减',note='中古英语切的动词，现代名词承接动作及结果。'),
 'B2522':dict(words=['industry','industries'],label='industry → industries：勤勉到产业',note='拉丁 industriā 的勤勉词经法语等借入，行业义后续发展。'),
 'C0623':dict(words=['judge','judges'],label='judge → judges：法官与作判断',note='拉丁 iudex 与 iudicare 的法语借入路线分别保留。'),
 'C0772':dict(words=['map','maps'],label='map → maps：布上的图到地图、映射',note='世界地图短语的缩短，保留的是拉丁 mappa 布的材料。'),
 'A1960':dict(words=['reference','references'],label='reference → references：指向资料、提及与推荐',note='名词有英语派生或法语借入分析，动词后来由名词转用。'),
 'C1447':dict(words=['support','supports'],label='support → supports：从下面托住',note='拉丁 sub 与 portare 结合，经法语等形成支撑、支持词族。'),
 'C0762':dict(words=['amount','amounts'],label='amount → amounts：往上累积到总量',note='法语向山上的表达发展成达到、合计的动词，英语名词较后。'),
 'C0707':dict(words=['demand','demands'],label='demand → demands：交付、询问到要求',note='拉丁 demandare 经法语发展，名词和动词有各自法语来源。'),
}
W('wings','/wɪŋz/','翅膀、机翼；侧翼、派别、建筑侧楼〔复数〕',
 '从身体两边伸出去的部分是 wings。飞机两侧、建筑两边、组织里不同的一支，也能借这个两侧展开的画面命名。',
 'wing + -s，/ŋ/ 后读 /z/。wing 经中古英语借古诺尔斯语 vængr 翅膀；更远与风、吹的联系未定。这里先学常见名词复数。',
 [['古诺尔斯语 vængr → wing','鸟的翅膀 → 两侧伸出的结构或分支'],['wing + -s → wings','若干翅膀、机翼、侧楼或派别']],
 'spread its wings 展开翅膀；the wings of a plane 飞机机翼；the two wings of a party 某政党的两派。',
 'wings on either side 两侧的翼部；wait in the wings 在侧幕等候、伺机接替。','建筑的 wings 是侧边伸展的楼体；the wings 在戏剧中常是舞台两旁观众看不到的位置。图形相似，实际位置按场景认。',
 ('The bird spread its wings and flew away.','鸟展开翅膀飞走了。'),('The museum has two wings connected by a hall.','博物馆有两座侧楼，由一个大厅相连。'),sources=['https://en.wiktionary.org/wiki/wings#English','https://en.wiktionary.org/wiki/wing#English'])
W('blocks','英 /blɒks/；美 /blɑːks/','块、楼群、街区；成段安排〔复数〕；挡住〔第三人称单数〕',
 '一整块东西，既能垒起来，也能挡在路上。blocks 的木块、楼块、时间块，抓完整的一块；动词则抓挡住去路。',
 'block + -s，/k/ 后读 /s/。底词经古法语 bloc 等接日耳曼木块、木料词。块状实体、成组单位和阻挡动作用途逐步扩展。',
 [['日耳曼木块词 → 法语 → block','木块 → 块状物、建筑或成组单位'],['block + -s → blocks','多个块、街区；单数主语阻挡']],
 'building blocks 积木、基础组成部分；two blocks away 两个街区远；blocks the entrance 挡住入口。',
 'blocks of time 整段时间；blocks the view 挡住视线。','城市街区大小并不固定，two blocks 是隔两个街区的路程，不是精确长度单位。block of flats 常是公寓楼。',
 ('The children built a tower with wooden blocks.','孩子们用木块搭了一座塔。'),('The parked truck blocks the entrance.','停着的卡车挡住了入口。'),sources=['https://en.wiktionary.org/wiki/blocks#English','https://en.wiktionary.org/wiki/block#English'])
W('copies','英 /ˈkɒpiz/；美 /ˈkɑːpiz/','副本、复制件、册〔复数〕；复制、模仿〔第三人称单数〕',
 '同一份内容再有一份，就是一份 copy；好几份是 copies。说书时数的是几本、几册，说动作时则是照着再做一份。',
 'copy 的辅音字母 + y 变 ies。名词经法语 copie、 中世纪拉丁 copia 抄本，最终接拉丁 cōpia 充足；动词另接法语 copier、拉丁 copiare 抄写。',
 [['拉丁 cōpia 充足 → 中世纪抄本词、法语 → copy','大量提供、抄写 → 内容相同的复制件'],['copy：y 改 ies → copies','多个副本；单数主语复制或模仿']],
 'two copies of the report 两份报告；sell a thousand copies 售出一千册；copies the file 复制文件。',
 'printed copies 纸质印刷件；copies her movements 模仿她的动作。','two copies of a book 是同一本书的两册。a copy of the original 是原件的一个副本。copies 的末尾读 /iz/，不是 /aɪz/。',
 ('Please bring three copies of the report.','请带三份报告来。'),('The software copies the files to another folder.','软件把这些文件复制到另一个文件夹。'),sources=['https://en.wiktionary.org/wiki/copies#English','https://www.etymonline.com/word/copy'])
W('crimes','/kraɪmz/','罪行、犯罪行为〔复数〕',
 '把一件件违反刑法的行为数出来，就是 crimes。这个词带有明确的严重性；日常说很糟糕的事情时，也有人夸张借用。',
 'crime + -s，/m/ 后读 /z/。crime 经古法语 crimne、crime 接拉丁 crīmen 指控、过错、罪行。更远与判断、区分的关系有不同分析。',
 [['拉丁 crīmen → 古法语 → crime','指控、罪 → 犯罪行为'],['crime + -s → crimes','把多起或多种罪行分别计数']],
 'commit crimes 犯罪；solve crimes 侦破案件；crimes against humanity 危害人类罪。',
 'serious crimes 严重罪行；investigate crimes 调查犯罪案件。','crime 可泛说犯罪这种现象，如 reduce crime；crimes 把不同事件或类型拿出来数。accusations 是指控，不能只凭指控就写成已证实的罪行。',
 ('The report compares different types of crimes.','报告比较了不同类型的犯罪。'),('The detective works on serious crimes.','这名侦探负责侦办严重犯罪案件。'),sources=['https://en.wiktionary.org/wiki/crimes#English','https://en.wiktionary.org/wiki/crime#English'])
W('episodes','英 /ˈepɪsəʊdz/；美 /ˈepɪsoʊdz/','集；一段段经历、事件、发作〔复数〕',
 '把连续的故事或生活切出一个个有起止的小段，就是 episodes。追剧时是一集集，回忆时是一段段经历。',
 'episode + -s，/d/ 后读 /z/。episode 经法语或直接接希腊 epeisódion，含 epi- 额外 + eisodos 进入，后者 eis 进入 + hodos 路；先有戏剧中插入场次的背景。',
 [['希腊 epeisódion → 法语或直接借入 → episode','插入戏剧的一段 → 叙事或经历中的一段'],['episode + -s → episodes；广播、电视扩展','连续节目中的各集；分别发生的事件']],
 'the first three episodes 前三集；episodes from her childhood 她童年的几段往事。',
 'new episodes every week 每周的新一集；separate episodes 分开的几次事件。','episode 强调一个有边界的小段，不要求每段都一样长。a series 常是整部系列节目，episodes 是其中各集。',
 ('We watched the first two episodes last night.','我们昨晚看了前两集。'),('The book recalls several episodes from her childhood.','这本书回忆了她童年的几段往事。'),sources=['https://en.wiktionary.org/wiki/episodes#English','https://www.etymonline.com/word/episode'])
W('farmers','英 /ˈfɑːməz/；美 /ˈfɑːrmərz/','农民、农场主、农业经营者〔复数〕',
 '经营农场、靠种植或养殖开展农业生产的人，是 farmers。这个称呼可以包含土地经营者，未必只指被雇来干农活的人。',
 'farmer + -s，末尾读 /z/；现代认形可接 farm + -er。历史 farmer 经法语 fermier 等接拉丁 firmārius，早有承租、收取固定款项的背景，农业义后来居于中心。',
 [['中世纪拉丁、法语承租词 → farmer','承租、固定付款相关人员 → 农业经营者'],['farmer + -s → farmers','多个从事或经营农业的人']],
 'local farmers 当地农民；dairy farmers 奶牛养殖户；farmers’ market 农夫市场、农产品直销市场。',
 'support local farmers 支持当地农民；farmers growing rice 种稻的农民。','farmer 强调农业生产或经营身份；farm worker 常强调在农场受雇劳动的人。farmer 的历史比现代直接 farm 加 er 更曲折。',
 ('Local farmers sell vegetables at the market.','当地农民在市场卖蔬菜。'),('The dry weather has caused problems for farmers.','干旱天气给农民带来了困难。'),sources=['https://en.wiktionary.org/wiki/farmers#English','https://www.etymonline.com/word/farmer'])
W('stages','/ˈsteɪdʒɪz/','阶段、舞台〔复数〕；上演、组织举行〔第三人称单数〕',
 '事情走到的一个位置、演员站着表演的平台，都是 stage 的常见画面；stages 可以数这些阶段或舞台，也可说某个团体上演活动。',
 'stage + -s，/dʒ/ 后增加 /ɪz/。stage 经古法语 estage 位置、居处等，接拉丁站立词族；英语舞台、阶段和动词上演义分别扩展。',
 [['拉丁站立词族 → 古法语 estage → stage','所处的位置 → 舞台、进展中的阶段'],['stage + -s → stages','多个阶段、舞台；单数主语组织上演']],
 'the early stages 初期阶段；in stages 分阶段；stages a play 上演一出戏。',
 'three stages of the project 项目的三个阶段；outdoor stages 户外舞台。','in stages 是分几步完成；on stage 是在舞台上。厨师实习的法语借词 stage 有另一读音，日常这些 stages 用 /steɪdʒɪz/。',
 ('The work will be completed in three stages.','这项工作将分三个阶段完成。'),('The school stages a play every summer.','学校每年夏天上演一出戏。'),sources=['https://en.wiktionary.org/wiki/stages#English','https://en.wiktionary.org/wiki/stage#English'])
W('winners','英 /ˈwɪnəz/；美 /ˈwɪnərz/','获胜者、得奖者；成功的事物〔复数〕',
 '在竞争或评选中赢出来的人、作品，是 winners。比喻使用时，也可以夸几个办法或产品很成功。',
 'win + -er → winner，双写 n；winner + -s → winners，末尾读 /z/。win 的本族词史接古英语 winnan 努力、争取等，获胜义逐渐成为中心。',
 [['古英语 winnan → win；win + -er → winner','努力争取、赢得 → 获胜或得奖者'],['winner + -s → winners','多名获胜者、多件得奖作品']],
 'prize winners 获奖者；the winners of the contest 比赛获胜者；pick winners 选出有成功潜力的人或事物。',
 'announce the winners 宣布获奖者；previous winners 往届得主。','winners 数赢的人或作品，wins 数胜利的次数。the winner of the race 是赛事获胜者，win the race 则是赢得比赛。',
 ('The judges announced the winners on Friday.','评委在周五宣布了获奖者。'),('All the winners received certificates.','所有获奖者都拿到了证书。'),sources=['https://en.wiktionary.org/wiki/winners#English','https://en.wiktionary.org/wiki/winner#English'])
W('cuts','/kʌts/','切口、伤口；削减、剪辑版本〔复数〕；切、削减〔第三人称单数〕',
 '切开会留一道口子；把预算切去一部分，就成了削减。cuts 可以数切出来的口子、减少的部分，也可以说某人正在做切、减这个动作。',
 'cut + -s，/t/ 后读 /s/。cut 接中古英语 cutten，常联系北日耳曼背景，但更远来源未定。名词承接切的动作、结果以及截出的部分。',
 [['中古英语 cutten → cut；名词用途','切开 → 切口、切下的部分、削减'],['cut + -s → cuts','多个切口、削减；单数主语切或减']],
 'cuts in spending 开支削减；paper cuts 纸划的小伤口；cuts the bread 切面包。',
 'budget cuts 预算削减；cuts the journey time 缩短路程耗时。','cuts 作动词是现在的第三人称单数；cut 的过去式仍是 cut。某人的 hands have cuts 是手上有伤口，cuts his hand 则是划伤手。',
 ('The council announced cuts in spending.','地方议会宣布削减开支。'),('This shortcut cuts the journey time in half.','这条近路让路程耗时缩短了一半。'),sources=['https://en.wiktionary.org/wiki/cuts#English','https://en.wiktionary.org/wiki/cut#English'])
W('industries','/ˈɪndəstriz/','产业、行业、工业部门〔复数〕',
 '把从事同类生产或服务的一群企业看作一个行业，再把不同领域分别数出来，就是 industries。软件、旅游也能成为 industry。',
 'industry 的辅音字母 + y 变 ies。industry 经法语 industrie、拉丁 industria 勤勉、活动等词义借入，后来用于系统经营的行业、工业；更早构成不强拆。',
 [['拉丁 industria → 法语、英语 industry','勤勉、活动 → 有组织的生产、经营领域'],['industry：y 改 ies → industries','多个产业或行业']],
 'creative industries 创意产业；local industries 当地产业；industries such as tourism 旅游等行业。',
 'different industries 不同行业；workers in several industries 几个行业的从业者。','industry 泛指工业或整个产业活动时可不可数；industries 是把不同领域分开数。并非只有冒烟的工厂才能叫 industry。',
 ('The town depends on several different industries.','这个城镇依靠几个不同的产业。'),('Digital tools are changing many industries.','数字工具正在改变许多行业。'),sources=['https://en.wiktionary.org/wiki/industries#English','https://en.wiktionary.org/wiki/industry#English'])
W('judges','/ˈdʒʌdʒɪz/','法官、裁判、评委〔复数〕；判断、评判〔第三人称单数〕',
 '听取材料后作出判定的人，是 judges；一个人根据线索作判断，也写 judges。法庭、比赛、评选里的判定职责不同。',
 'judge + -s，/dʒ/ 后增加 /ɪz/。名词经古法语 juge 接拉丁 iūdex 法官；动词经 jugier 等接 iūdicāre 判断，两条借入路线分开看。',
 [['拉丁 iūdex、iūdicāre → 法语 → judge 名词、动词','法官与作出判断的行为'],['judge + -s → judges','多位判定者；单数主语判断']],
 'a panel of judges 评审团；the judges’ decision 评委的决定；judges people by their actions 根据行为判断人。',
 'judges in the competition 比赛评委；judges the distance 判断距离。','judges 可以是法官，也可以是评委，不能见到这个词就认定在法庭。动词 judge something by... 说明用什么标准或线索来判断。',
 ('The judges gave each performance a score.','评委给每场表演打了分。'),('She judges the distance by looking at the trees.','她看着那些树判断距离。'),sources=['https://en.wiktionary.org/wiki/judges#English','https://en.wiktionary.org/wiki/judge#English'])
W('maps','/mæps/','地图；对应关系图〔复数〕；绘图、映射〔第三人称单数〕',
 '把地点或关系铺到一个可查看的平面上，是 map。maps 可以是几张地图，也可以是某个工具把一片地方画出来、把两组东西对应起来。',
 'map + -s，/p/ 后读 /s/。map 缩自中古英语世界地图词，也部分接法语 mappe；较早短语 mappa mundi 里的 mappa 是布，mundi 是世界的。',
 [['拉丁 mappa mundi → 中古英语、法语 → map','绘在布等材料上的世界地图 → 地图'],['map + -s → maps；动词用途','多张地图；单数主语绘制、建立对应']],
 'street maps 街道地图；maps of the area 这一地区的地图；maps out a route 规划路线。',
 'maps showing rivers 显示河流的地图；maps each code to a name 将每个代码对应到名称。','map 保留下来的是 mappa 的部分，不是 mundi 直接变短。现代技术语境 maps A to B 是建立 A 到 B 的对应关系。',
 ('The guide includes maps of the walking routes.','指南包含徒步路线地图。'),('The program maps each number to a different colour.','程序让每个数字对应一种不同的颜色。'),sources=['https://en.wiktionary.org/wiki/maps#English','https://www.etymonline.com/word/map'])
W('references','英 /ˈrefərənsɪz/；美 /ˈrefərənsɪz/','提及、引用、参考文献；推荐人、推荐证明〔复数〕；提到、引用〔第三人称单数〕',
 '把读者或听者指向另一个人、另一份材料，是 references 的线索。文末指向资料的条目、谈话里的提及、求职时可供核实的人，都从这个功能理解。',
 'reference + -s，/s/ 后读 /ɪz/。reference 可分析 refer + -ence，也有法语 référence 借入分析；后者较早常接标为重构的中世纪拉丁 *referentia。动词后来从名词转用。',
 [['refer 词族／法语 référence → reference','指向某处 → 提及、查考或证明资料'],['reference + -s → references；动词转用','多项引用、推荐资料；单数主语引用']],
 'a list of references 参考文献表；references to earlier work 对早期工作的提及；provide two references 提供两位推荐人或两份推荐证明。',
 'check the references 核对引文；references at the end of the article 文末参考文献。','求职中的 references 可能要人名和联系方式，也可能要书面推荐，按具体要求判断。文献引用只指明来源，不一定照抄原话。',
 ('The article includes references to earlier studies.','文章包含对早期研究的引用。'),('Please provide contact details for two references.','请提供两位推荐人的联系方式。'),sources=['https://en.wiktionary.org/wiki/references#English','https://en.wiktionary.org/wiki/reference#English'])
W('supports','英 /səˈpɔːts/；美 /səˈpɔːrts/','支撑物〔复数〕；支撑、支持、维持〔第三人称单数〕',
 '在下面托住，让东西不塌、不倒，是 supports 的基本画面；给人资源、给说法证据，也是让它站得住。',
 'support + -s，/t/ 后读 /s/。拉丁 sub- 下面 + portāre 承载 → supportāre，b 在 p 前同化；经法语等进入英语，名词还有相关法语及英语转用背景。',
 [['拉丁 supportāre → 法语、英语 support','从下承载 → 支撑、维持、支持'],['support + -s → supports','多个支撑物；单数主语提供支撑或支持']],
 'wooden supports 木支架；supports the roof 支撑屋顶；supports the conclusion 支持结论。',
 'supports the family 养家；supports local artists 支持当地艺术家。','support 表示支持这种行为或帮助时常不可数；supports 常是可数的实体支撑物。evidence supports a claim 是证据使主张站得住。',
 ('Two steel supports hold the roof in place.','两根钢支柱把屋顶固定住。'),('The evidence supports her explanation.','证据支持她的解释。'),sources=['https://en.wiktionary.org/wiki/supports#English','https://en.wiktionary.org/wiki/support#English'])
W('amounts','/əˈmaʊnts/','数量、总额〔复数〕；合计达到、相当于〔第三人称单数〕',
 '把一份份东西累起来，最后到了多少，是 amount 的线索。amounts 可数不同份量，amounts to 则给出累到的总数或实际效果。',
 'amount + -s，/t/ 后读 /s/。古法语 a mont 向山上 → amont、amonter 上升、达到，进入英语动词，再有总量名词；不是现代临时组合 a + mount。',
 [['古法语 a mont、amonter → amount 动词','向上、上升 → 合计达到'],['动词转名词 amount；加 -s → amounts','不同数量、数额；单数主语合计为']],
 'small amounts of water 少量水；equal amounts 等量；amounts to fifty pounds 合计五十英镑。',
 'varying amounts 数量不等的几份；amounts to a refusal 实际上等于拒绝。','amounts of 常接不可数名词，如 money、water；可数项目的数量一般用 numbers of。amounts to 还可以概括事情实际等于什么。',
 ('Add small amounts of water until the mixture is smooth.','少量多次加水，直到混合物变得均匀顺滑。'),('The total amounts to fifty pounds.','总额为五十英镑。'),sources=['https://en.wiktionary.org/wiki/amounts#English','https://en.wiktionary.org/wiki/amount#English'])
W('demands','英 /dɪˈmɑːndz/；美 /dɪˈmændz/','要求、所需投入〔复数〕；强烈要求、需要〔第三人称单数〕',
 '把要求明确推到别人面前，要对方回应，是 demands；任务本身也会向人要时间、精力，于是有工作的种种 demands。',
 'demand + -s，/d/ 后读 /z/。动词经法语 demander 询问、要求，接拉丁 dēmandāre 委托、交付；名词另经法语 demande。de- 在这里不机械译成向下。',
 [['拉丁 dēmandāre → 法语 demander、demande → demand','交付、委托 → 询问、要求'],['demand + -s → demands','多项要求、负担；单数主语要求或需要']],
 'meet the demands 满足要求；the demands of the job 工作所需投入；demands attention 需要注意。',
 'competing demands 相互争夺时间精力的要求；demands a clear answer 要求明确答复。','the demands of work 常是工作造成的负担；demand for a product 是市场对产品的需求，通常不数成一项项 demands。',
 ('She is trying to balance the demands of work and family.','她正努力平衡工作和家庭的种种需要。'),('The task demands patience and care.','这项任务需要耐心和细心。'),sources=['https://en.wiktionary.org/wiki/demands#English','https://en.wiktionary.org/wiki/demand#English'])
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_zf',ROOTS,WORDS)
 extend_lessons()
