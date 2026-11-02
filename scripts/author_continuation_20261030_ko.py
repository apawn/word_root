"""Hum, maid, bullet and lip."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
H=[['中古英语 hummen；通常看作拟声来源','哼、嗡嗡响、低声连续作响'],['声音与活动的比喻','机器低鸣、人哼曲；地方运转活跃'],['hum + -ing；hum + buck + -er','哼鸣声、哼鸣的；抑制电气嗡声的拾音器']]
W('hum','/hʌm/','哼曲；低声嗡鸣；嗡嗡声；忙碌运转',
 '嘴不唱清歌词，轻轻哼旋律，是 hum；冰箱、电机持续低响也像哼着。一个地方运作活跃，又可以说 it is humming。',
 '承中古英语 hummen 等，通常归于拟声词，并与其他日耳曼语言的嗡鸣形式相比。不是所有 hum 开头的词都取这个意思。',H[:2],
 'hum a tune 哼曲子，the hum of traffic 车流的低响，hum along 跟着哼，hum with activity 忙碌活跃地运作。',
 'hum a tune；the hum of traffic；hum with activity。',
 'hum 可轻轻哼唱，不必有词；sing 范围更广。humble 谦逊的来自另一词源，不能拆成 hum 嗡鸣 + -ble。',
 ('She hummed a tune while washing the dishes.','她洗碗时轻轻哼着曲子。'),('The refrigerator gave a steady hum.','冰箱发出持续的低鸣。'))
W('humming','/ˈhʌmɪŋ/','哼唱、嗡鸣声；嗡响、运转活跃的',
 '耳边一直有低低的声音，可以说 humming；工厂、办公室正活跃运作，也可借用机器嗡鸣的形象。',
 'hum + -ing，双写 m。名词说声音、行为，分词形容持续低响等状态。',H[:2]+[['hum + -ing → humming','哼唱、嗡鸣；正在活跃运转']],
 'a humming noise 嗡鸣声，the humming of a motor 电机嗡鸣，keep the business humming 让业务顺畅活跃地运行。',
 'a humming noise；the humming of a motor。',
 'humming 可以是唱歌，也可以是机器声或活跃比喻。hummingbird 是因翅膀声音得名的鸟，不是在唱歌词。',
 ('The humming of the fan filled the quiet room.','风扇的嗡鸣回荡在安静的房间里。'),('Orders kept the workshop humming all week.','订单让工场整周忙碌运转。'))
W('humbucker','英 /ˈhʌmbʌkə/；美 /ˈhʌmbʌkər/','双线圈消噪拾音器',
 '电吉他可能拾到讨厌的电气嗡声。humbucker 用两个线圈配合，抵消这种干扰，同时保留琴弦的信号；名字就是对抗嗡声的东西。',
 'hum 嗡声 + buck 抵抗、对抗 + -er 器具。buck 在这里不是雄鹿的动物义。',H[:1]+[['hum + buck + -er → humbucker','抵消电气嗡声的拾音器名称']],
 'a humbucker pickup 双线圈消噪拾音器，a guitar with humbuckers 装有这类拾音器的吉他。线圈可有不同布局，不能只按外观宽度判断。',
 'a humbucker pickup；a guitar with humbuckers。',
 'humbucker 抑制相应干扰，不意味着任何环境下都没有任何噪声。拾音器 pickup 与扩音器 amplifier 也不是同一设备。',
 ('The guitar has a humbucker near the bridge.','吉他在琴桥附近装了一个双线圈消噪拾音器。'),('She compared the humbucker with a single coil pickup.','她比较了双线圈消噪拾音器和单线圈拾音器。'),sources=['https://en.wiktionary.org/wiki/humbucker#English','https://www.fender.com/articles/maintenance/what-is-a-humbucker-and-how-does-it-buck-the-hum'])
R('B4189','低哼、低鸣及活跃运转的形象，技术中再命名消噪器件','HUM：连续低响，或轻轻哼出旋律','hum → humming；hummingbird 取翅膀声；humbucker 取抑制电气嗡声的功能。',
 '听觉画面很好用，但 hum 开头不保证同源。humble 来自拉丁卑下等词义，与本页嗡鸣分开。',
 'hummen 等 → hum；-ing 声音、活动；bird 鸟；buck 对抗，-er 器具。',
 [['低哼、低鸣与鸟名','hum · humming · hummingbird'],['抑制电气嗡声的器件','humbucker']],
 'hum 不必有歌词；hummingbird 借翅膀声音；humble 不是 hum 的派生。',
 'She hummed a tune while testing the guitar’s humbucker.\n\n她一边测试吉他的双线圈拾音器，一边轻哼曲子。','hum humming hummingbird humbucker')
ROOTS[-1]['exclude']['humble']='拉丁 humilis 等卑下、贴近地面词族的来源，不属于 hum 嗡鸣。'
M=[['古英语 mægden → 中古英语 maiden','女孩、未婚年轻女子等旧称'],['maiden 的截短 → maid','年轻女子；女仆、清洁服务人员等'],['复合词与首次的比喻','mermaid 海中女子；nursemaid 照料孩子者；maiden voyage 首航']]
W('maid','/meɪd/','女仆、女佣、女性清洁服务人员；少女〔旧、文学用法〕',
 '历史上先是年轻女子的称呼，后来一些工作角色也用 maid 命名。现代常在酒店、家务服务或历史故事里看到。',
 '中古英语 maid 是 maiden 的截短，后者承古英语 mægden。现代虽然 maid 更短，却不代表 maiden 一定是从现代 maid 新加后缀产生。',M[:2],
 'a hotel maid 酒店女清洁服务员，a lady’s maid 女主人的贴身女仆〔历史〕。今天具体工作也常用 housekeeper、cleaner 等名称。',
 'a hotel maid；a lady’s maid。',
 'maid 与 made 同音。历史 maiden、maid 的身份词义与现代岗位名称不同，不能据职业称呼推断婚姻、年龄。',
 ('The novel follows a maid in a large country house.','小说以乡间大宅里的一名女仆为主角。'),('The hotel maid found the missing scarf.','酒店女清洁员找到了遗失的围巾。'))
W('maiden','/ˈmeɪdən/','少女、未婚年轻女子〔旧、文学用法〕；首次的',
 '旧时说年轻、未婚女子，后来把尚未经历某事的形象用于首次：a maiden voyage 是船的第一次航行。',
 '古英语 mægden 经中古英语 maiden 传下，更早含旧小称形式。maid 反而是后来的截短，现代不要只凭较短词形倒推历史。',M[:1]+[M[2]],
 'a maiden voyage 首航，a maiden speech 首次演说，maiden name 婚前姓〔传统用法〕。名词少女义多见文学、旧语境。',
 'a maiden voyage；a maiden speech；maiden name。',
 'maiden 作首次的形容词时，不是在说船、演讲的性别；maiden name 也不是名字中的第一个词。',
 ('The ship began its maiden voyage in spring.','这艘船在春天开始首航。'),('Her maiden speech focused on education.','她的首次演说集中谈教育。'),sources=['https://en.wiktionary.org/wiki/maiden#English','https://www.etymonline.com/word/maiden'])
W('mermaid','英 /ˈmɜːmeɪd/；美 /ˈmɜːrmeɪd/','美人鱼',
 '故事中上半身是女人、下半身是鱼尾的海中人物，就是 mermaid。名称把水域和女子接在一起。',
 '中古英语 mermayde，由 mere 海、湖等水域旧词 + maid 女子。前半 mer- 不取法语 mère 母亲义。',M[:2]+[['mere + maid → mermaid','海、湖里的女子 → 美人鱼']],
 'a mermaid tale 美人鱼故事，a mermaid statue 美人鱼雕像。merman 是相应男性虚构形象的常见名称。',
 'a mermaid tale；a mermaid statue。',
 'mermaid 是神话、故事形象。manatee 海牛等真实动物与它不是同一分类名称。',
 ('The child drew a mermaid with a silver tail.','孩子画了一条银尾美人鱼。'),('A mermaid statue stands near the harbor.','一尊美人鱼雕像立在港边。'))
W('nursemaid','英 /ˈnɜːsmeɪd/；美 /ˈnɜːrsmeɪd/','照料孩子的女保姆〔常见于历史语境〕；事事照料、替人操心',
 'nurse 在这里取照料义，maid 取工作角色义，合起来是照顾孩子的人。动词再借这种角色说不停替人、某设备操心。',
 'nurse + maid。由照顾幼儿的工作名称，转成事事照看的动词。',M[:2]+[['nurse + maid → nursemaid','照顾孩子者 → 不断替人操心、照料']],
 'a child’s nursemaid 孩子的保姆，nursemaid a machine 不停照看一台不可靠的机器〔比喻〕。',
 'a child’s nursemaid；nursemaid a machine。',
 'nursemaid 不只看成医院护士加女佣；这里 nurse 的照料义更宽。动词对成年人使用时，常暗含不该需要如此照看的不耐烦。',
 ('The nursemaid took the children to the garden.','保姆带孩子们去了花园。'),('The unreliable printer needs nursemaiding all day.','那台不可靠的打印机整天都得有人照看。'))
R('B2806','年轻女子的旧称与服务角色，扩到故事和首次的比喻','MAID：历史上从 MAIDEN 截短，再形成不同角色名称','maiden → maid；mermaid、nursemaid 等组合；maiden voyage 首航是固定扩展。',
 '现代词形的长短与历史出现顺序不必一致。maid、maiden 的旧身份称呼和现代岗位、首次比喻，也要分开。',
 'mægden → maiden → maid；mer- 水域，nurse 照料；house、chamber、bar 等限定角色场所。',
 [['基础旧称与首次用法','maid · maiden'],['故事人物与照料角色','mermaid · nursemaid'],['其他工作、仪式角色','bridesmaid · housemaid · barmaid · chambermaid · handmaid · maidservant']],
 'maiden 历史早于截短 maid；maiden voyage 不说船的性别；nursemaid 的 nurse 取照料义。',
 'The nursemaid read the children a tale about a mermaid’s first voyage.\n\n保姆给孩子们读了一个美人鱼初次航行的故事。','maid maiden mermaid nursemaid bridesmaid housemaid barmaid chambermaid handmaid maidservant')
B=[['法语 boule 球 → bullete 等小称','小球；印记、标记等旧借词背景'],['英语 bullet 的固定用途','弹丸；版面项目符号；迅速运动的比喻']]
W('bullet','/ˈbʊlɪt/','子弹、弹头；项目符号；快速移动',
 '名称有小球的历史，现代弹头不必是圆球。排版里一颗实心圆点用来标条目，也因外形叫 bullet。',
 '借法语 bullete 等，联系 boule 球的小称，后来受 boulet、boulette 等影响。不是常用弹丸义由 bull 公牛 + -et 组成；小公牛的少见同形词是另回事。',B,
 'a bullet point 项目要点、带符号条目，a bullet list 项目列表，dodge a bullet 躲过一劫，bite the bullet 硬着头皮面对难事。',
 'a bullet point；dodge a bullet；bite the bullet。',
 '严格说 bullet 可指射出的弹头，cartridge 是包含壳体等的一整发；日常 bullet 也可能泛说整发。bulletproof 是防弹的或比喻难以攻破。',
 ('Please put the main ideas into bullet points.','请把主要想法列成项目要点。'),('They dodged a bullet when the broken branch missed the car.','断枝没砸中车，他们躲过一劫。'),sources=['https://en.wiktionary.org/wiki/bullet#English','https://www.etymonline.com/word/bullet'])
R('B3206','小球的历史走向弹丸、圆点符号与快速运动、风险比喻','BULLET：固定借词，现代不要求总是球形','bullet → bulletproof；bullet point、dodge a bullet 等看固定搭配。',
 '从物件形状到排版符号很直观；固定习语则学整句意义，不能只靠小球推出来。',
 'boule 球 → 法语小称 bullete 等 → bullet；proof 抵御、经受住的相关性质。',
 [['弹丸、符号与相关性质','bullet · bulletproof']],
 'bullet 常用义不来自 bull；bullet 与 cartridge 在精确语境中区分；dodge a bullet 可比喻躲过祸事。',
 'The guide uses bullet points to explain what bulletproof means.\n\n指南用项目要点解释 bulletproof 的意思。','bullet bulletproof')
L=[['古英语 lippa、lippe → 中古英语 lippe → lip','嘴唇'],['形状、位置与说话的扩展','容器凸边；顶嘴、不敬的话'],['-ed、-y 与化妆品简称','lipped 带凸边；lippy 顶嘴的，另可口语说口红']]
W('lip','/lɪp/','嘴唇；凸边、边缘；顶嘴、不敬的话〔口语〕',
 '嘴的上下边缘是 lips；杯、壶、托盘边缘向外或向上凸起，也像嘴唇。话从嘴里出来，lip 又能口语说顶嘴。',
 '承古英语 lippa、lippe，经中古英语 lippe 传下。身体部位转为相似边缘，再在口语里与说话态度相连。',L[:2],
 'the upper lip 上唇，the lip of a cup 杯口凸边，bite your lip 咬唇、忍住不说，give someone lip 顶嘴，My lips are sealed. 我会守口如瓶。',
 'the upper lip；the lip of a cup；give someone lip。',
 'lip 不是整个 mouth；rim 是更广的边缘名称。Don’t give me lip. 带斥责语气，不能当普通邀请别人说话。',
 ('She pressed her lips together to stop laughing.','她抿住嘴唇，忍着没笑。'),('A small chip was missing from the lip of the cup.','杯口边缘缺了一小块。'))
W('lipped','/lɪpt/','有嘴唇、带某类唇的；带凸边的',
 '物件边缘凸起像唇，可以 lipped。描述人的嘴唇时，通常还会加修饰成分，说唇是什么样。',
 'lip + -ed，双写 p，表具有某种结构；末尾读 /t/。这类 -ed 不是每次都表示被人做了一个动作。',L[:2]+[['lip + -ed → lipped','具有唇或唇状凸边']],
 'a lipped edge 凸起边缘，a lipped tray 带凸边托盘；人物外貌描写中多见带其他限定成分的组合。',
 'a lipped edge；a lipped tray。',
 'lipped 多说身体或结构特征，lippy 常说顶嘴的态度。凸边的托盘不因此有会说话的性格。',
 ('She chose a tray with a lipped edge.','她选了一个边缘凸起的托盘。'),('Each shelf has a lipped front to stop objects sliding off.','每层搁板前沿都有凸边，防止东西滑落。'))
W('lippy','/ˈlɪpi/','爱顶嘴、出言不逊的〔口语〕；口红、唇彩〔口语名词〕',
 '一个人总拿话顶回来，口语可以说 lippy。另一个名词用法则把 lipstick、lip gloss 缩成亲切的短名，常见于英式口语。',
 '态度义由 lip 顶嘴 + -y，双写 p；化妆品名词另由 lipstick、lip gloss 等截短再加口语 -y。两条现代构词作用不同。',L[:2]+[['lip + -y → lippy 形容词','顶嘴、不敬的态度'],['lipstick／lip gloss → lippy 名词','口红、唇彩的口语短称']],
 'get lippy 顶起嘴来，a lippy teenager 爱顶嘴的青少年，a tube of lippy 一管口红〔口语〕。',
 'get lippy；a tube of lippy。',
 'lippy 常含说话者不满对方态度的评价；化妆品名词没有这个态度义。看词性和搭配就能分开。',
 ('He got lippy when the teacher asked him to wait.','老师让他等一下，他却顶起嘴来。'),('She slipped a tube of lippy into her bag.','她把一管口红放进包里。'))
R('B3391','嘴唇的身体形象，扩到物件凸边和说话态度','LIP：口的边缘，也借来命名凸边和顶嘴','lip → lipped、lippy；lipstick 取嘴唇与棒状化妆品组合；lippy 名词是口语短称。',
 '嘴唇、容器边、顶嘴态度、口红昵称，按形状、行为与截短分别理解，不把一条构词关系套到底。',
 'lippa／lippe → lip；-ed 带有，-y 性质或口语短称；lip + stick → lipstick。',
 [['身体和结构','lip · lipped'],['化妆品与态度、昵称','lipstick · lippy']],
 'lipped 带凸边不等于 lippy 顶嘴；lippy 名词可说口红；lip 与 mouth 范围不同。',
 'She applied lipstick, then pressed her lips together.\n\n她涂上口红，然后抿了抿嘴唇。','lip lipped lipstick lippy')
if __name__=='__main__':save('continuation_20261030_ko',ROOTS,WORDS)
