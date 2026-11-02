"""Data, third, pretty, hit, hear and grow: common families in priority order."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
def C(a,b,w,m):return [[a+'；'+b,'并列构词部分'],[w,m]]
DA=[['拉丁语 datum；复数 data','被给出的东西；给定事项'],['英语 data','供记录、研究、处理的数据、资料']]
W('data','常见 /ˈdeɪtə/；美式也 /ˈdætə/','数据；资料',
 '先收下已记录、给定的事实，再拿它们做比较、推理或处理。',
 '借自拉丁语 datum 的复数 data；datum 来自表示给的动词 dō 的分词形式。英语后来把 data 也发展成整体、不可数的资料概念。',DA,
 'collect data 收集数据，analyse data 分析数据。学术语境常用 the data are，普通和商业语境也广泛用 the data is；不要只凭拉丁语来源判后一用法一律错。',
 'collect data；analyse data；raw data；data on something；data protection。',
 'data 不只等于数字，文本、图像等也能构成数据；datum 是对应单数，但日常一个数据点也常直接说 a data point。',
 ('The study collected data from three schools.','研究从三所学校收集了数据。'),('The data are consistent with the earlier findings.','这些数据与先前发现一致。'),('The data is stored on a secure server.','数据存储在安全服务器上。'),sources=['https://en.wiktionary.org/wiki/data#English','https://dictionaryblog.cambridge.org/2020/05/13/gathering-compiling-and-analyzing-talking-about-data-1/'])
W('database','/ˈdeɪtəbeɪs/','数据库',
 '把相关数据有组织地放在一起，让人或系统能查找、更新和使用。',
 'data 数据 + base 基地、基础，复合为集中组织数据的系统、集合名称。不是只有一个普通表格文件才能叫 database。',C('data 数据','base 组织、存放的基础','database','有组织的数据集合、数据库'),
 'a customer database 客户数据库，search a database 查数据库。数据库可采用不同组织方式，并不全是同一种行列形式。',
 'a searchable database；update a database；database records。',
 'database 是有组织的数据集合或相关系统，datasheet 是说明数据、参数的一张资料表；名字都含 data，作用不同。',
 ('The library maintains a searchable database of old newspapers.','图书馆维护着一个可检索的旧报纸数据库。'),('Please update the customer’s address in the database.','请更新数据库中这位顾客的地址。'))
W('datasheet','/ˈdeɪtəʃiːt/','数据表；产品参数表',
 '把一个产品或材料的关键数据集中放在一页或一份说明里，方便查。',
 'data 数据 + sheet 表、纸页，形成参数资料表名称。数字文件也沿用 sheet，不一定真只有一张纸。',C('data 数据','sheet 表、页','datasheet','集中列出数据、参数的资料表'),
 'a product datasheet 产品参数表；check the datasheet 查看参数。电子器件、设备、材料说明中常见。',
 'a technical datasheet；a product datasheet；download the datasheet。',
 'datasheet 多突出规格、数据，user manual 用户手册多说明怎样使用；datasheet 不等于数据库。',
 ('The datasheet lists the sensor’s dimensions and operating range.','参数表列出了传感器的尺寸和工作范围。'),('She compared the two products using their datasheets.','她利用两款产品的参数表进行比较。'))
R('B3729','数据、资料；组织数据与描述数据','DATA：给出的记录，拿来分析与使用','先区别数据本身、组织数据的数据库、说明参数的资料表，再看描述数据的数据 metadata。',
 'data 原是拉丁语 datum 的复数，英语现代又有整体不可数用法。database、datasheet 是英语后来的复合名称。',
 'data → database、datasheet；meta- + data → metadata。',
 [['资料与组织','data · database'],['参数说明与数据描述','datasheet · metadata']],
 'data are 与 data is 都有实际使用场景；database 数据库，datasheet 参数表，metadata 描述数据的信息。',
 'The database stores product data, while each datasheet summarizes one product’s specifications.\n\n数据库存放产品数据，每份参数表则概述一个产品的规格。',
 'data database datasheet metadata')
TH=[['古英语 þridda → 中古英语 thirde / thridde','第三'],['英语 third','第三；三分之一；若干旧地理词的历史词族']]
W('third','英 /θɜːd/；美 /θɜːrd/','第三；三分之一',
 '顺着数，排在二之后；把整体均分三份，取一份也用 third。',
 '继承古英语 þridda，经中古英语发展。three 到 third 的形式变化有历史来路，不是现代只要把 three 加普通 -th 就得到 threeth。',TH,
 'the third floor 第三层，a third of the cake 三分之一蛋糕；two thirds 三分之二。楼层从哪一层开始编号，地区习惯不同，先看场景。',
 'the third time；a third of；two thirds；a third party。',
 'third 是序数或分数，three 是数量。a third party 是原来两方之外的第三方，不是必须排名第三的政党。',
 ('This is the third time I’ve called today.','这是我今天第三次打电话。'),('We saved a third of the cake for tomorrow.','我们留了三分之一蛋糕明天吃。'))
W('thirdly','英 /ˈθɜːdli/；美 /ˈθɜːrdli/','第三；第三点',
 '把讨论排成一列，现在轮到第三项。',
 'third + -ly，形成列举顺序的副词。这里不是说做事用了三倍力量。',TH+[['third → thirdly','第三 → 列举第三点']],
 'firstly, secondly, thirdly 第一、第二、第三。正式说明中可用，也常直接用 first、second、third 列举，保持风格一致即可。',
 'firstly, secondly, thirdly；thirdly, we need to...。',
 'thirdly 列出第三点，three times 是三次；不要把序列位置与发生次数混在一起。',
 ('Thirdly, we need a clear plan for maintaining the building.','第三，我们需要一份维护建筑的明确计划。'),('Thirdly, the survey does not include people under eighteen.','第三，调查不包括未满十八岁的人。'))
W('riding','/ˈraɪdɪŋ/','骑乘活动；另有历史行政区、加拿大选区义',
 '骑马这个 riding 与地理、选举报道中的 riding，看着一样，却不能都用骑马去猜。',
 '骑乘义来自 ride + -ing。地区名义另来自表示三分之一的古诺斯语词，经 trithing 等形式变化；与 north、east 等名称衔接时，开头音逐渐重新分界为 riding。不是骑马一天可绕完的地区。',TH+[['两条形式来路：ride + -ing；古诺斯语 þriðjungr → trithing → riding','骑乘活动；另有原三分区相关地理名称、后来的选区用法']],
 'horse riding 骑马；East Riding 等历史地名中的 Riding 与第三、三分区有亲缘。加拿大政治文字中 a riding 常指选区，现代选区并不要求只分三块。',
 'horse riding；the East Riding；an electoral riding。',
 'riding 的地区义不是由骑马覆盖距离定义；同形词要分历史来路。',
 ('She enjoys horse riding on weekends.','她喜欢周末骑马。'),('The historical map divides the county into three ridings.','历史地图把这个郡划为三个区。'),('The article compares voting patterns in neighbouring ridings.','文章比较相邻选区的投票模式。'))
R('B2576','第三；三分之一；旧地理词族','THIRD：顺序第三，整体中的三分之一','third 的现代基本用法很直接；riding 的地区名称则保留较难一眼看出的三分区历史。',
 'third 接古英语 þridda。riding 的行政地区义来自另一条古诺斯语三分之一词族路径，与骑乘同形却不是同一构词。',
 'third → thirdly；地区名 riding 与第三、三分区的历史亲缘另看。',
 [['位置、份额与列举','third · thirdly'],['同形不同来路的地区名','riding']],
 'three 数量，third 第三或三分之一；地理 riding 不由骑马一天覆盖的距离定义。',
 'Thirdly, the old document describes how the county was divided into three ridings.\n\n第三，旧文件描述了这个郡如何分成三个区。',
 'third thirdly riding')
PR=[['古英语 prættiġ → 中古英语 prety / praty','机巧、狡黠、巧妙等旧义'],['英语 pretty','后来发展出精巧、好看等义；现代也常作程度副词']]
W('pretty','/ˈprɪti/','漂亮的；相当、挺；有些固定口语用法',
 '作形容词是看着赏心悦目；作副词则像把程度往上推一点，说挺、相当。',
 '接古英语 prættiġ，旧义有机巧、狡黠，经巧妙、精巧等用法发展到好看。现代 pretty 并不表示这个人狡猾，不能拿古义反推性格。',PR,
 'a pretty garden 漂亮花园；pretty good 挺好，pretty sure 相当肯定。pretty 作程度副词不变成 prettily；pretty much 差不多、基本上。',
 'pretty good；pretty sure；pretty much；a pretty picture。',
 'pretty cold 是挺冷，不是漂亮地冷；prettily decorated 才是装饰得漂亮。pretty 的程度依语气变化，不是一个固定百分比。',
 ('The village has a pretty little square.','村里有个漂亮的小广场。'),('I’m pretty sure the shop closes at six.','我相当确定商店六点关门。'),('We’ve pretty much finished the work.','我们基本上做完了工作。'),sources=['https://en.wiktionary.org/wiki/pretty#English','https://www.etymonline.com/word/pretty'])
W('prettily','/ˈprɪtɪli/','漂亮地；精致地',
 '不是说程度挺高，而是做出来的外观、姿态让人觉得漂亮。',
 'pretty + -ly，y 变 i；副词修饰装饰、布置、动作等，保留好看的方式义。',PR+[['pretty → prettily','漂亮的 → 以漂亮、精致的方式']],
 'prettily decorated 布置得漂亮；arranged prettily 摆放得好看。与程度副词 pretty 的用法分开掌握。',
 'prettily decorated；prettily arranged；smile prettily。',
 'pretty well 挺好，prettily 是漂亮地；不能把 every pretty + adjective 都改成 prettily。',
 ('The cakes were prettily decorated with small flowers.','蛋糕用小花装饰得很漂亮。'),('She arranged the coloured stones prettily on the shelf.','她把彩色石头在架上摆得很精致。'))
W('prettiness','/ˈprɪtinəs/','漂亮；秀美、精致好看的性质',
 '把外观让人觉得好看这一点，拿出来当作一种特征。',
 'pretty + -ness，y 变 i。名词保留现代好看义，不是抽象化成机巧、狡诈。',PR+[['pretty → prettiness','漂亮的 → 漂亮这一性质']],
 'the prettiness of a village 村庄的秀美；mere prettiness 可表示只有好看、缺乏更深内容，这是上下文的评价。',
 'the prettiness of the setting；mere prettiness；delicate prettiness。',
 'prettiness 偏好看、精致的感受；beauty 范围更广，也能说壮美、深刻之美。两者有重叠，不是硬划等级。',
 ('The garden’s prettiness attracted visitors in spring.','春天，花园的秀美吸引了访客。'),('The review praised the film’s depth rather than its prettiness alone.','评论赞扬电影的深度，而不只是画面好看。'))
R('B3434','漂亮；程度副词相当、挺','PRETTY：好看与挺、相当分两种现代用法','pretty 自己就能作程度副词；prettily 才专门把漂亮的方式放到动作上。',
 'pretty 的旧来路有机巧、狡黠等义，后来发展出精巧、好看。古义有助看变化，不决定现代人的性格。',
 'pretty → prettily、prettiness；pretty good、pretty much 留在基础词中对照。',
 [['外观评价与程度','pretty'],['方式与性质','prettily · prettiness']],
 'pretty cold 挺冷，prettily decorated 装饰得漂亮；pretty 不等于只能夸外貌。',
 'The room was prettily decorated, and the view was pretty good too.\n\n房间装饰得漂亮，窗外风景也挺不错。',
 'pretty prettily prettiness')
HI=[['古诺斯语 hitta；英语早期 hittan → 中古英语 hitten','遇到、碰到、击中'],['英语 hit，过去式、过去分词仍为 hit','碰撞、击打；达到；成功作品']]
W('hit','/hɪt/','击中、碰撞；达到；突然影响；热门成功作品',
 '先想真的碰上一个目标；达到某个数字、突然遭遇困难，甚至作品获得成功，都有碰中、产生强烈作用的感觉。',
 '有古诺斯语 hitta 相遇、击中背景，经英语早期及中古英语发展。过去式、过去分词仍是 hit，不是 hitted。',HI,
 'hit the ball 击球，hit a target 达到目标，hit a problem 遇到问题。a hit song 热门歌曲；hit the road 口语是动身、上路。',
 'hit a target；hit a record high；a big hit；hit the road；be hit by。',
 'hit 不只暴力动作；a hit film 是成功电影，不是打架电影。名词 hit 在音乐、网络、体育中还有各自计数习惯。',
 ('The ball hit the window.','球撞上了窗户。'),('The song became a huge hit.','这首歌大获成功。'),('We hit a problem when we tried to book the tickets.','订票时，我们遇到了问题。'))
W('hitter','英 /ˈhɪtə/；美 /ˈhɪtər/','击球手；善于击打的人',
 '执行 hit 这个动作的人，体育里尤其常说击球表现。',
 'hit + -er，双写 t。还可见 heavy hitter 有影响力、实力强的人这一比喻搭配。',HI+[['hit → hitter','击打 → 击球手、击打者']],
 'a good hitter 好击球手；a heavy hitter 可是强力击球者，也可能是业界重量级人物。',
 'a powerful hitter；a consistent hitter；a heavy hitter。',
 'hitter 泛指做击打动作的人，不等于音乐热门作品制造者 hitmaker；比喻 heavy hitter 要看具体领域。',
 ('She is one of the team’s most reliable hitters.','她是队里最可靠的击球手之一。'),('The conference attracted several heavy hitters from the publishing industry.','会议吸引了出版业几位重量级人物。'))
W('hitmaker','英 /ˈhɪtmeɪkə/；美 /ˈhɪtmeɪkər/','热门作品创作者；金曲制作人',
 '做出来的作品常能大受欢迎，所以被称为制造 hit 的人。',
 'hit 热门成功作品 + maker 制作者；hit 在这里是作品成功的名词义，不是打人。',C('hit 热门作品','maker 创作者、制作人','hitmaker','制作热门作品的人'),
 'a pop hitmaker 流行金曲创作者；可能说歌手、词曲作者或制作人，具体角色由上下文决定。',
 'a pop hitmaker；a proven hitmaker；a successful hitmaker。',
 'hitmaker 不自动等于 singer 歌手；他也可能在幕后写歌、制作。',
 ('The producer became known as a reliable hitmaker.','这位制作人以屡出热门作品而闻名。'),('The show reunited several hitmakers from the same decade.','节目让同一个十年间的几位热门作品创作者重聚。'))
W('hitman','/ˈhɪtmæn/','受雇杀手',
 'hit 在某些犯罪俚语中指一次杀人行动，执行者因此被叫作 hitman。',
 'hit 犯罪俚语中的杀人行动 + man 执行者，形成名词；不是所有善于击球、能打的人都叫 hitman。',C('hit 特定犯罪俚语：杀人行动','man 执行者','hitman','受雇实施杀人的人'),
 'a fictional hitman 虚构的受雇杀手；犯罪小说、电影简介中常见。普通办公室负责难题的人并不因为很能干就自动是这个词。',
 'a fictional hitman；a retired hitman in a thriller；a film about a hitman。',
 'hitman 强调受雇杀手，hitter 体育里可说击球手，hitmaker 是热门作品创作者。',
 ('The thriller follows a retired hitman trying to leave his past behind.','惊悚片讲述一名退休杀手试图摆脱过去的故事。'),('The actor plays a hitman in the crime drama.','这位演员在犯罪剧中扮演受雇杀手。'))
R('B2878','击中；碰上；达到；热门作品','HIT：碰中目标，也可碰上问题、达到数字','现代 hit 不只暴力；体育、成功作品和固定俚语各自分开。',
 'hit 有古诺斯语 hitta 等历史背景，从相遇、碰中发展出各种作用、达到用法。过去式、过去分词与原形同形。',
 'hit → hitter；成功作品义 hit + maker → hitmaker；犯罪俚语 hit + man → hitman。',
 [['碰中及体育行动者','hit · hitter'],['不同固定名词义的组合','hitmaker · hitman']],
 'hitter 击球手，hitmaker 热门作品制作人，hitman 受雇杀手；三个名词不能因都含 hit 就互换。',
 'The hitmaker wrote a hit song for a film about a hitman.\n\n这位金曲创作者为一部讲杀手的电影写了一首热门歌曲。',
 'hit hitter hitmaker hitman')
HEAR=[['古英语 hīeran、hēran 等形式 → 中古英语 heren 等','听见'],['英语 hear；过去式、过去分词 heard','听见；听说；收到消息；听取、审理']]
W('hear','英 /hɪə/；美 /hɪr/','听见；听说；听取；收到消息',
 '声音进到耳里，或者消息到了自己这里；不一定是主动把耳朵凑过去。',
 '继承古英语 hīeran、hēran 等形式，经中古英语发展。过去式、过去分词 heard，英 /hɜːd/、美 /hɜːrd/；与 hear 的元音不同。',HEAR,
 'hear a sound 听到声音；hear from a friend 收到朋友消息，hear of someone 听说过某人。Hear me out 是先听我说完，a court hears a case 是法院审理案件。',
 'hear from；hear of；hear about；hear someone out；hear a sound。',
 'hear 强调听到、获知，listen to 强调主动听；listen to someone 不保证最终听清 hear what they said。',
 ('I heard a strange sound outside.','我听见外面有奇怪声响。'),('Have you heard from your sister recently?','你最近收到姐姐或妹妹的消息了吗？'),('Please hear me out before you decide.','请先听我说完再决定。'))
W('hearing','英 /ˈhɪərɪŋ/；美 /ˈhɪrɪŋ/','听觉、听力；听证、庭审；倾听的机会',
 '可以说听声音的能力，也可以是正式留出时间听取证据、说明。',
 'hear + -ing，形成能力、活动、程序等名词；正式程序义取听取双方或相关信息的意思。',HEAR+[['hear → hearing','听 → 听觉、听取活动或正式程序']],
 'good hearing 听力好；a public hearing 公开听证；give someone a fair hearing 公平听取某人意见。最后这个表达不一定真的在法庭里。',
 'hearing loss；a public hearing；a fair hearing；within hearing distance。',
 'hearing 作为能力常不可数，a hearing 作为一次正式程序或听取机会可数；听证不是听力测试。',
 ('Her hearing is excellent, even in a noisy room.','即使房间嘈杂，她的听力也很好。'),('The committee promised to give both sides a fair hearing.','委员会承诺公平听取双方意见。'))
W('hearer','英 /ˈhɪərə/；美 /ˈhɪrər/','听见者；听话人',
 '把交流中接收到声音或话语的那一方单独点出来。',
 'hear + -er，形成听的人这一名词；旧英语已有相应的人名词传统。',HEAR+[['hear + -er → hearer','听见 → 听见、接收话语的人']],
 'speaker and hearer 说话人与听话人；语言学、正式论述常见。日常节目受众通常说 listeners、audience 更自然。',
 'the speaker and the hearer；the hearer’s interpretation。',
 'hearer 点出接收话语的一方，不一定强调认真听；listener 在普通表达中常更自然，也常表示主动听的人。',
 ('The meaning depends partly on what the hearer already knows.','含义部分取决于听话人已经知道什么。'),('The lecturer explained the difference between speaker intention and hearer interpretation.','讲师解释了说话人意图与听话人理解之间的区别。'))
W('overhear','英 /ˌəʊvəˈhɪə/；美 /ˌoʊvərˈhɪr/','无意中听到；听见本来不是说给自己的话',
 '你没在对话中心，但声音传过来，耳朵接到了别人的话。',
 'over- + hear，旧英语已有 oferhīeran 等形式；历史义不只一个，现代常用义是听见并非直接说给自己的话，不必逐字译超过听。',HEAR+[['旧英语 oferhīeran → overhear','旧组合的听相关用法 → 现代常说偶然听到他人话语']],
 'overhear a conversation 偶然听见对话；overhear someone say... 听见某人说……。过去式、过去分词 overheard。',
 'overhear a conversation；overhear someone saying；be overheard。',
 'overhear 通常强调偶然、并非说给自己；eavesdrop 更明确是有意偷听。不能只看都是听别人说话就当成相同动机。',
 ('I overheard two passengers discussing the delay.','我无意中听见两位乘客讨论延误。'),('She lowered her voice so that nobody would overhear.','她压低声音，免得旁人听见。'))
R('B2740','听见；消息传来；听取','HEAR：声音或消息到了你这里','与 listen to 主动去听对照；hear 的信息来源还可以是信件、消息，而不只即时声波。',
 'hear 接旧英语听见词族，heard 保留不规则过去形式。hearing 把能力或听取程序名词化，overhear 是旧前缀组合发展出的现代固定用法。',
 'hear → hearing、hearer；over- + hear → overhear，过去式 overheard。',
 [['感知、能力与接收者','hear · hearing · hearer'],['旁听到别人的话','overhear']],
 'hear from 收到消息，hear of 听说过；hearing 是听力或听取程序；overhear 通常偶然，eavesdrop 更明确有意。',
 'I heard from a friend who had overheard an interesting conversation.\n\n我收到朋友消息，他无意中听到一段有意思的对话。',
 'hear hearing hearer overhear')
GROW=[['古英语 grōwan → 中古英语 growen','生长、增加、繁茂'],['英语 grow；过去式 grew，过去分词 grown','生长、增长；种植；逐渐变得']]
W('grow','英 /ɡrəʊ/；美 /ɡroʊ/','生长；增长；种植；逐渐变得',
 '从一点点长起来，借说数量增加、能力发展，甚至某种感觉逐渐出现。',
 '继承古英语 grōwan，经中古英语 growen 发展。过去式 grew /ɡruː/，过去分词 grown，英 /ɡrəʊn/、美 /ɡroʊn/。',GROW,
 'plants grow 植物生长；grow tomatoes 种番茄；grow tired 渐渐疲倦，grow to like something 渐渐喜欢上。grow up 是长大，不只是某一个尺寸变大。',
 'grow up；grow into；grow tired；grow to understand；grow a business。',
 'grow 可以自己生长，也可以及物说种植；grow tired 中 tired 是变得怎样，不是被种出来的东西。',
 ('The children have grown a lot since last year.','从去年到现在，孩子们长大了很多。'),('We grow herbs on the kitchen windowsill.','我们在厨房窗台种香草。'),('I grew to appreciate the quiet village.','我渐渐喜欢上这座安静村庄。'))
W('grown','英 /ɡrəʊn/；美 /ɡroʊn/','grow 的过去分词；长大的、成熟的',
 '生长已经发生；形容人时，常说不再是需要当小孩对待的人。',
 'grow 的不规则过去分词，延续旧英语生长动词的分词形式；也已形成长大的形容词。不要与 ground 混淆；后者可指地面，也是 grind 的过去式、过去分词。',GROW+[['grow → grew → grown','原形 → 过去式 → 过去分词；长大的']],
 'has grown 已长大、增长；a grown man 成年男子，grown children 已长大的子女。fully grown 常说身体已长成。',
 'a grown woman；grown children；fully grown；has grown。',
 'grown /ɡrəʊn/ 与 ground /ɡraʊnd/ 不同；形容长大不等于保证心理、行为在每方面都成熟。',
 ('Their children are grown and have moved away.','他们的孩子都长大并搬出去了。'),('The small company has grown into a national business.','这家小公司已经发展成全国性企业。'))
W('growth','英 /ɡrəʊθ/；美 /ɡroʊθ/','生长；增长；成长、发展',
 '把长起来、增加、发展的过程或结果，单独作为一件事来谈。',
 'grow + 形成抽象名词的 -th。现代词形不需要把 grow 里的每个读音保留后再机械加一个 th。',GROW+[['grow + -th → growth','生长、增长 → 相应过程、发展']],
 'plant growth 植物生长，economic growth 经济增长，personal growth 个人成长。增长什么、按什么指标衡量，要看后面的内容。',
 'rapid growth；growth in demand；personal growth；growth rate。',
 'growth 是名词，grow 是动词；growth rate 增长率不等于 growth 本身所有含义都按百分数表达。',
 ('The warm spring encouraged rapid plant growth.','暖和春季促进了植物迅速生长。'),('The project gave her opportunities for personal growth.','项目给了她个人成长的机会。'))
W('grower','英 /ˈɡrəʊə/；美 /ˈɡroʊər/','种植者、种植企业；以某种速度生长的东西',
 '常是让作物长起来的人，也可能是在比较某种植物自己长得多快。',
 'grow + -er，行动者或具有某种生长特征的事物名称。种植义与生长义都可成为基础。',GROW+[['grow → grower','种植、生长 → 种植者；某种生长者']],
 'a coffee grower 咖啡种植者；a slow grower 生长慢的植物等。This song is a grower 口语可说这歌越听越有味道。',
 'local growers；a fruit grower；a slow grower；a song that is a grower。',
 'grower 种植者与buyer买家、dealer经销商不同；同一个人可能兼任，但词义强调不同环节。',
 ('Local growers sell fresh vegetables at the market.','当地种植者在市场卖新鲜蔬菜。'),('This tree is a slow grower but lives for a long time.','这种树长得慢，但寿命很长。'))
W('regrow','英 /ˌriːˈɡrəʊ/；美 /ˌriːˈɡroʊ/','重新生长；使再长出来',
 '原有部分失去或被剪掉后，再一次长出来。',
 're- 再、重新 + grow 生长；保留 grow 的过去形式 regrew、regrown。',GROW+[['re- + grow → regrow','再次生长、使重新长出']],
 'regrow leaves 重新长叶，hair regrows 头发重新长出。具体生物能否长回、长到什么程度，要看对象，不由 re- 保证。',
 'regrow leaves；regrow after damage；new tissue regrows。',
 'regrow 是重新生长，rebuild 是重建，通常不是植物自身长出来；grow back 也常表达长回。',
 ('The plant regrew its leaves after the dry season.','旱季过后，植物重新长出了叶子。'),('The cut grass soon began to regrow.','剪过的草很快开始重新生长。'))
R('B2873','生长；增加；种植；逐渐变得','GROW：从长起来，到数量、能力、感觉的发展','自身生长、培育作物与逐渐变得是三种常用结构；先看后面接对象还是状态。',
 'grow 接古英语 grōwan。grew、grown 是不规则变化；growth 把过程名词化；regrow 再长，outgrow 长到不再适用。',
 'grow → grown、growth、grower；re- + grow → regrow；outgrow 与旧衣物、习惯等一起理解。',
 [['动作、分词、过程与种植者','grow · grown · growth · grower'],['再长与长过原有范围','regrow · outgrow']],
 'grow tomatoes 种番茄，grow tired 逐渐疲倦；grown 与 ground 分读分义；growth 是名词。',
 'The grower watched new leaves regrow as the young trees continued their growth.\n\n幼树继续生长，种植者看着新叶重新长出来。',
 'grow grown growth grower regrow outgrow')
for item in WORDS:
 if item['word']=='riding':
  item['history']=[['两条独立来路：英语 ride；古诺斯语 þriðjungr','前者为骑乘，后者为三分之一'],['ride + -ing；þriðjungr → trithing 等形式 → riding','骑乘活动；另一支为地区名称及后来的选区用法']]
  item['sources'].append('https://www.etymonline.com/word/riding')
 if item['word']=='database':item['sources'].append('https://www.oracle.com/database/what-is-database/')
if __name__ == '__main__':save('continuation_20261029_ce',ROOTS,WORDS)
