"""Hind, building, process and park: frequent bases and useful contrasts."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
def C(a,b,w,m):return [[a+'；'+b,'并列构词部分'],[w,m]]
HI=[['古英语 hindan、behindan 等 → 中古英语形式','在后、在背面'],['英语 hind、behind','后部的；在后、落后、背后的原因等']]
W('hind','/haɪnd/','后部的；另有雌鹿义',
 '动物前腿、后腿一对照，后面那一对就是 hind legs；这是位置，不是动物名字。',
 '后部形容词接古英语 hindan 等在后形式；雌鹿名词有另一条古英语 hind 的来源，现代同形，不把两支强行串成雌鹿总走在后面。',HI,
 'hind legs 后腿，hind feet 后脚；stand on hind legs 用后腿站立。a hind 另可指雌鹿，常在自然、文学文本出现。',
 'hind legs；hind feet；hind limbs。',
 'hind 后部的，behind 常是介词、副词在后面；the hind legs 不能简单替成 the behind legs。',
 ('The dog stood on its hind legs.','狗用后腿站了起来。'),('The deer injured one of its hind feet.','鹿的一只后脚受了伤。'))
W('behind','/bɪˈhaɪnd/','在后面；落后；背后的原因、支持者；留下',
 '位置排在后面，进度也能落在后面；谁在推动一件事，又可说是谁站在它背后。',
 '古英语 behindan 已有组合，由 be- 与后方词根构成；be- 不是现代动词 be，不能按存在加后部理解所有句子。',HI,
 'behind the door 门后，behind schedule 进度落后；the person behind the idea 想法的提出、推动者，leave something behind 遗留东西；a behind 口语名词可指屁股。',
 'behind the door；behind schedule；leave behind；the reason behind。',
 'behind 在后，after 在时间、次序或追随关系中更宽；behind schedule 是比计划慢，不是计划结束后。',
 ('Your bag is behind the door.','你的包在门后。'),('The project is two weeks behind schedule.','项目比计划落后两周。'),('Who was behind the idea for the festival?','是谁提出并推动了这个节庆构想？'))
R('B4580','后部、在后面；落后及背后推动','HIND：后方的位置，再到进度和原因','hind legs 是后腿，behind the house 是屋后；behind schedule 把后方位置借给进度。',
 '后方分支接古英语 hindan、behindan 等，hindsight 则是回头看过去。雌鹿 hind 有另一来源，不拿动物行为编造位置词源。',
 'hind 后部 → behind 在后；hindsight 事后回看。',
 [['后方与在后面','hind · behind'],['事后回看','hindsight']],
 'hind legs 不说 behind legs；behind schedule 是落后计划；a hind 雌鹿另源。',
 'The dog’s hind feet were hidden behind the chair.\n\n狗的后脚藏在椅子后面。',
 'hind behind hindsight')
BU=[['古英语 byldan → 中古英语 bilden、builden → build','建造、建立'],['build + -ing → building','建造过程；建成的建筑物；抽象建立过程']]
W('shipbuilding','/ˈʃɪpbɪldɪŋ/','造船；造船业',
 '不是在船上盖房子，而是把船本身设计、制造出来。',
 'ship 船 + building 建造过程。building 在这里取 build 的动作名词义，不是现成的一座楼。',C('ship 船','building 建造过程','shipbuilding','造船活动、行业'),
 'the shipbuilding industry 造船业，a shipbuilding yard 造船厂；可以包括不同船型，不只木船或军舰。',
 'the shipbuilding industry；a shipbuilding yard；traditional shipbuilding。',
 'shipbuilding 造船，shipboard 船上的；a shipbuilding project 是造船项目，不是船上装修的所有工作。',
 ('Shipbuilding was once the town’s main industry.','造船业曾是这座城镇的主要产业。'),('The museum explains traditional shipbuilding techniques.','博物馆介绍传统造船技艺。'))
W('peacebuilding','/ˈpiːsbɪldɪŋ/','和平建设；巩固和平的工作',
 '停火之后还得让社会关系、制度和生活逐渐稳下来，减少再冲突的可能；把和平当成需要建立的东西。',
 'peace 和平 + building 建立，形成抽象建设名词。不是修一栋叫和平的大楼，也不只指战后某一天的一次谈判。',C('peace 和平','building 建立、建设','peacebuilding','建立、巩固和平条件的持续工作'),
 'community peacebuilding 社区和平建设，peacebuilding efforts 巩固和平的努力；可包含对话、制度、社区合作等多类工作。',
 'peacebuilding efforts；community peacebuilding；a peacebuilding programme。',
 'peacemaking 促成和平，peacekeeping 维持和平，peacebuilding 建立、巩固和平条件；实际工作会交叠，但词的焦点不同。',
 ('The programme supports local peacebuilding efforts.','项目支持当地巩固和平的努力。'),('Community dialogue became part of the peacebuilding process.','社区对话成了和平建设过程的一部分。'))
R('B2926','建造过程、建筑物；抽象建设','BUILDING：做出来的过程，和建成的东西分开','a building 是一座建筑，shipbuilding 是造船过程；peacebuilding 再把建立的动作借给社会和平。',
 'building 是 build 的 -ing 名词及形式。遇到复合词先判断后半说实体还是过程，不把所有 building 都译成大楼。',
 'build → building；ship、home、body、world、peace + building 分别建造、塑造不同对象；outbuilding 却是附属建筑实体。',
 [['基础及实体','building · outbuilding'],['制造和塑造过程','shipbuilding · homebuilding · bodybuilding · worldbuilding'],['社会和平建设','peacebuilding']],
 'shipbuilding 造船不等于船上建筑；building 的实体、过程要看可数性和前面的对象。',
 'The old building now houses a museum of shipbuilding.\n\n这座老建筑如今是一家造船博物馆。',
 'building outbuilding shipbuilding homebuilding bodybuilding worldbuilding peacebuilding')
PR=[['拉丁 prōcēdere → prōcessus → 法语 proces → 英语 process','向前推进 → 行进、进程、过程'],['英语 process 的动词和派生词','按程序处理；处理过的；执行处理的设备、人或机构']]
W('processed','英 /ˈprəʊsest/；美 /ˈprɑːsest/','处理过的；加工过的',
 '原材料、资料或申请已经经过了一道或多道处理；究竟怎样处理要看对象。',
 'process + -ed，过去式、过去分词并可作形容词；-ed 接在这里常读 /t/，不是额外完整的 /ɪd/ 音节。',PR+[['process + -ed → processed','处理 → 已处理、加工过的']],
 'processed food 加工食品，processed data 已处理数据；The application has been processed 申请已处理，不自动等于获批。',
 'processed food；processed data；a processed application。',
 'processed 说经过处理，approved 说得到批准；食品加工方式很多，不能仅凭这一个词推断具体营养或安全状况。',
 ('The processed data was ready for analysis.','处理后的数据已经可以分析了。'),('Your application has been processed, but a decision is still pending.','你的申请已处理，但决定仍待作出。'))
W('processor','英 /ˈprəʊsesə/；美 /ˈprɑːsesər/','处理器；加工设备、企业；处理某事者',
 '把东西送进去，按规则变成结果的那个人、设备或机构；电脑里处理指令的芯片是常见一例。',
 'process + -or，-or 形成执行作用的人、物名称。电脑处理器、食品加工机、加工企业等取不同对象，不是所有 processor 都是 CPU。',PR+[['process + -or → processor','处理 → 执行处理的人、设备、机构']],
 'a computer processor 计算机处理器，a food processor 食品加工机，a payment processor 支付处理服务商；word processor 文字处理软件或设备。',
 'a computer processor；a food processor；a payment processor；a word processor。',
 'processor 是执行处理的设备或主体，process 是过程或处理动作；processing 是处理活动，三者句法对象不同。',
 ('The laptop has a more powerful processor.','这台笔记本电脑有一个更强的处理器。'),('She chopped the vegetables in a food processor.','她用食品加工机切碎了蔬菜。'))
R('B3408','过程、处理；处理过的与处理主体','PROCESS：东西经过一套步骤，变成结果','申请、数据、食品都可以 process；processed 是处理过，processor 是处理它的设备、机构等。',
 'process 经法语接拉丁向前推进、进程词族。派生词保留处理关系，但不自动交代采用了什么算法、工艺或决定。',
 'process → processed；process + -or → processor。',
 [['过程、处理结果和主体','process · processed · processor']],
 'processed 申请已处理不等于 approved 获批；processor 不只电脑芯片；process、processing、processor 各有句法角色。',
 'The processor handled the data, and the processed results were stored.\n\n处理器处理了数据，处理后的结果被保存了下来。',
 'process processed processor')
PA=[['法语 parc → 中古英语 park','围起来的区域、园地，历史更远联系日耳曼语围栏词'],['英语 park','园地、公园、专门场区；动词有集中安放、停车等用法']]
W('park','英 /pɑːk/；美 /pɑːrk/','公园；专门园区；停车；暂时搁置',
 '名词是一片专作某种用途的区域；动词把东西安放在一处，现代最常见就是停车。',
 '经中古英语、法语 parc 接围起来的土地词族。名词由围地发展出公园等；动词经过集中安放等用法发展为停车，不能把所有公园说成原来就是停车场。',PA,
 'a city park 城市公园，a science park 科技园；park a car 停车，park an idea 暂时搁置一个想法。park oneself somewhere 口语说坐定、待在某处。',
 'a public park；a science park；park the car；park an idea。',
 'park 公园或停车动作，car park 英式是停车场；不能单靠中文公园的园字理解动词。',
 ('We walked through the park after lunch.','午饭后我们穿过公园散步。'),('Let’s park that idea and return to it tomorrow.','先把这个想法放一放，明天再讨论。'))
W('parking','英 /ˈpɑːkɪŋ/；美 /ˈpɑːrkɪŋ/','停车；停车位、停车设施',
 '可以说把车停下来的动作，也可整体说这里有没有地方停车。',
 'park 的停车义 + -ing，动作名词常不可数；不因结尾 -ing 就只表示此刻正在发生。',PA+[['park + -ing → parking','停车动作 → 停车空间、安排']],
 'No parking 禁止停车，free parking 免费停车；a parking space 一个停车位，parking fees 停车费。',
 'free parking；No parking；a parking space；parking fees。',
 'parking 通常不可数，找一个车位说 a parking space 或 a parking spot，不能照中文一个停车直接写 a parking。',
 ('The hotel offers free parking.','酒店提供免费停车。'),('It took us ten minutes to find a parking space.','我们花了十分钟才找到停车位。'))
W('parkway','英 /ˈpɑːkweɪ/；美 /ˈpɑːrkweɪ/','林荫大道；景观道路等固定道路名称',
 '道路两侧带景观、绿化，名字让人想到穿行园地的路；现代哪些道路这样命名，按当地历史和制度。',
 'park 园地 + way 道路，形成景观道路名称。英国某些车站名 Parkway 的历史、停车换乘联系另有具体背景，不把每个名称都说成同一即时组合。',C('park 园地','way 道路','parkway','与绿地景观联系的道路名称'),
 'a scenic parkway 风景道路，drive along the parkway 沿林荫、景观大道开车。现实路名不保证车辆类型、限速等全国统一。',
 'a scenic parkway；along the parkway；a tree-lined parkway。',
 'parkway 是固定道路类别或名称，不是 car park 停车场，也不是所有公园里小径的通用名称。',
 ('The parkway follows the edge of the valley.','景观道路沿着山谷边缘延伸。'),('We drove along a tree-lined parkway.','我们沿一条林荫大道开车。'))
W('ballpark','英 /ˈbɔːlpɑːk/；美 /ˈbɔːlpɑːrk/','棒球场；大概范围；粗略估算的',
 '实际是一座球场；估数时说在这个球场范围里，就像先圈出大概区间，还没精确到一个点。',
 'ball 球 + park 专用场区，先为棒球场名称。ballpark figure 等固定比喻后来指大概数值；用球场圈范围是帮助理解，不把比喻细节当已证实唯一起源。',C('ball 球','park 专用场区','ballpark','棒球场 → 固定比喻里的大概范围'),
 'a ballpark figure 大概数，a ballpark estimate 粗略估算，in the ballpark 在大致范围内；日常项目费用、时间讨论常见。',
 'a ballpark figure；a ballpark estimate；in the ballpark。',
 'ballpark estimate 不是精确报价，也不是完全乱猜；具体可靠程度取决于给估算的人和依据。',
 ('We watched a game at the new ballpark.','我们在新棒球场看了一场比赛。'),('Can you give me a ballpark figure for the cost?','你能给我一个费用的大概数吗？'))
W('skatepark','英 /ˈskeɪtpɑːk/；美 /ˈskeɪtpɑːrk/','滑板等轮式运动场地',
 '给滑板、轮滑等器材设置坡道、平台和障碍的专用场区。',
 'skate 滑行、滑轮运动 + park 专用场地，不是只要公园里有人玩滑板，整个公园就成了 skatepark。',C('skate 滑行、滑轮运动','park 专用场区','skatepark','为滑板等运动设计的场地'),
 'an indoor skatepark 室内滑板场，a local skatepark 当地滑板运动场；是否允许自行车、滑板车等要看场地规则。',
 'an indoor skatepark；a local skatepark；ramps at the skatepark。',
 'skatepark 通常围绕轮式运动设施，ice rink 是冰场；不能只因 skate 也能滑冰就当成同一种场地。',
 ('The town opened a new skatepark for local riders.','小镇为当地运动爱好者开放了一座新滑板场。'),('The skatepark has ramps for different skill levels.','滑板场有适合不同水平的坡道。'))
W('parkside','英 /ˈpɑːksaɪd/；美 /ˈpɑːrksaɪd/','公园旁的',
 '房子、街道在公园边上，名字说明相邻位置，不是说它属于公园。',
 'park 公园 + side 旁边，形成位置形容词。Parkside 大写也常见于路名、楼盘名，名称不一定能证明实际位置。',C('park 公园','side 旁边','parkside','位于公园边上的'),
 'a parkside café 公园旁咖啡馆，a parkside apartment 公园旁公寓；通常放在名词前。',
 'a parkside café；a parkside apartment；a parkside location。',
 'parkside 公园边，parking 停车；一个 parkside apartment 仍可能完全没有 parking。',
 ('They met at a small parkside café.','他们在一家公园旁的小咖啡馆见面。'),('The parkside apartment has large windows.','这套公园旁的公寓有大窗户。'))
R('B3781','公园、园区；停车与专门场区','PARK：一片区域，或把东西安放在一处','park 作名词是园地、专用区域，作动词常是停车；parking 看停车安排，parkside 看公园边位置。',
 'park 经法语接围地历史。不同现代词各自固定：parkway 景观道路，ballpark 棒球场及粗估，skatepark 轮式运动场。',
 'park → parking；park + side → parkside；parkland 园地；parkway 道路；ball、skate + park 看场区。',
 [['基础与停车','park · parking'],['公园周边和道路','parkside · parkland · parkway'],['专用运动场区','ballpark · skatepark']],
 'parkside 不是 parking；parkway 不是停车场；ballpark figure 是大概数，不是精确报价。',
 'The parkside café offers free parking near the skatepark.\n\n公园旁的咖啡馆提供免费停车，位置靠近滑板场。',
 'park parking parkside parkland parkway ballpark skatepark')
for item in WORDS:
    if item['word']=='peacebuilding':item['sources'].append('https://peacekeeping.un.org/en/terminology')
    if item['word']=='park':item['sources'].append('https://www.etymonline.com/word/park')
    if item['word']=='ballpark':item['sources'].append('https://www.etymonline.com/word/ballpark')
if __name__=='__main__':save('continuation_20261029_cv',ROOTS,WORDS)
