"""Initial, lack, worry and spread: useful distinctions in ordinary sentences."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
IN=[['拉丁 inīre → initium → initiālis','进去、开始 → 开端 → 开始的'],['经法语或拉丁借入 → initial','最初的；名字开头字母；后作签首字母动词']]
W('initial','/ɪˈnɪʃəl/','最初的；姓名首字母；签姓名首字母',
 '时间线上头一个阶段是 initial；名字开头的那个字母也叫 an initial。',
 '接法语 initial 或拉丁 initiālis，来自 initium 开始，远接 in- 进入 + īre 去。这里 in- 不是否定，itial 也不是现代独立词根。',IN,
 'an initial plan 初步计划，an initial reaction 第一反应，your initials 姓名首字母，initial each page 每页签姓名首字母。',
 'an initial plan；an initial reaction；your initials；initial each page。',
 'initial 最初不保证 final 最终采用；initials 姓名首字母不等于任何缩略词的统一名称。首字母签署与签全名在形式上不同。',
 ('My initial reaction was to refuse.','我的第一反应是拒绝。'),('Please write your initials in the box.','请在框里写下姓名首字母。'),sources=['https://www.etymonline.com/word/initial','https://en.wiktionary.org/wiki/initial#English'])
W('initially','/ɪˈnɪʃəli/','起初；最开始时',
 '先把镜头放到事情开头，常给后面情况发生改变留出位置。',
 'initial + -ly，形容词转副词。不是一直、从头到尾，只说明起点那段时间。',IN+[['initial + -ly → initially','在最初阶段、起初']],
 'Initially, ... 起初……，initially planned 最初计划的，initially reluctant 起初不愿意。',
 'initially planned；initially reluctant；initially successful。',
 'initially 最初，eventually 最后、终于；originally 有时最初，也可强调原本的来源、安排。',
 ('Initially, I thought the task would be easy.','起初，我以为任务会很简单。'),('The event was initially planned for June.','活动最初计划在六月举行。'))
W('initialize','/ɪˈnɪʃəlaɪz/','初始化；设定初始状态',
 '让程序、设备先具备开始工作所需的起点：给变量一个初值，把资源准备好。',
 'initial + -ize，使进入初始状态。英式也可拼 initialise；此处讲常见技术动词，不把每次初始化都说成清空所有数据。',IN+[['initial + -ize → initialize','设定开始所需的状态、数值或资源']],
 'initialize a variable 初始化变量，initialize the system 初始化系统；具体做了什么由那个系统的操作定义。',
 'initialize a variable；initialize the system；initialize the device。',
 'initialize 建立初始条件，reset 重置，restart 重启；操作可能有交叉，但名称不保证执行步骤和数据影响完全相同。',
 ('The program initializes the counter to zero.','程序把计数器初始化为零。'),('The device takes a few seconds to initialize.','设备需要几秒钟完成初始化。'))
R('B4328','进入、开始；初期、姓名首字母与初始状态','INITIAL：位于开头；INITIALIZE：把起始条件准备好','initial → initially → initialize；名字首字母和签署动作直接在 initial 中按场景解释。',
 '拉丁进入、开始的词系借入，不硬拆成否定 in-；最初状态可能后来改变。',
 'inīre → initium → initiālis → initial；initial + -ly/-ize。',
 [['开头、最初与起始设置','initial · initially · initialize']],
 'initial 不保证最终；initially 起初、eventually 最后；initialize/reset/restart 具体操作含义不由词形保证一致。',
 'Initially, the program initializes the counter to its initial value.\n\n起初，程序把计数器设为初始值。',
 'initial initially initialize')
LA=[['中古英语 lak、lakken → lack','缺少、不足；可能与低地日耳曼同族或未记录本族形式有关'],['现代 lack','缺少这个动作、状态；欠缺之处']]
W('lack','/læk/','缺少；不足、匮乏〔名词〕',
 '应该有或想要有的那一块没有、还不够；可以缺钱，也可以缺经验、解释。',
 '可靠记录接中古英语 lak、lakken，直接源头有不同分析，未记录古英语形式不能当成已见史料。现代名词和动词搭配不同。',LA,
 'lack experience 缺经验，a lack of time 时间不足，be lacking in detail 缺少细节。动词 lack 常直接接对象，不加 of。',
 'lack experience；a lack of time；for lack of；be lacking in。',
 'They lack money 动词直接接名词，a lack of money 名词接 of；没有钱用 lack money，不照名词结构写 lack of money 作完整谓语。',
 ('The team lacks experience in this area.','团队缺乏这一领域的经验。'),('The project failed for lack of funding.','项目因资金不足而失败。'),sources=['https://www.etymonline.com/word/lack','https://en.wiktionary.org/wiki/lack#English'])
W('lackluster','英 /ˈlæklʌstə/；美 /ˈlæklʌstər/','暗淡无光的；平淡、缺乏活力的',
 '本该闪亮却没光彩；表演、成绩也可以没起色、提不起劲。',
 'lack 缺少 + luster 光泽，最早记录用于眼神缺乏光彩，后用于表现、活力。英式常拼 lacklustre，意思相同。',LA+[['lack + luster → lackluster','少光泽 → 缺活力、表现平平']],
 'a lackluster performance 平淡表现，lackluster sales 不振销售，a lackluster response 冷淡回应。',
 'a lackluster performance；lackluster sales；a lackluster response。',
 'lackluster 常是没精神、没亮点，不必糟到 disastrous 灾难性；luster 是光泽，不是 cluster 一簇。',
 ('The team gave a lackluster performance.','队伍表现平平，没什么活力。'),('Sales remained lackluster throughout the summer.','整个夏天销售都没起色。'))
R('B4057','想要的那一块没有、不足；失去光彩的组合','LACK：欠一块、不够；LACKLUSTER：少光泽、没起色','lack 掌握动词与名词句式，再 lackluster；冷门 lackland 暂略。',
 '未记录旧词形只作假说，学习从可靠中古英语开始。实际表达先弄清 lack money 与 a lack of money。',
 'lack + luster；英式常见 lacklustre。',
 [['欠缺和表现平淡','lack · lackluster']],
 '动词 lack 直接接对象，名词 a lack of；lackluster 平淡无光不一定惨败。',
 'The lackluster performance showed a lack of preparation.\n\n平淡的表现显出了准备不足。',
 'lack lackluster')
WO=[['古英语 wyrġan → 中古英语 worien','勒、扼；咬住撕扯等旧用法'],['后有困扰、烦扰 → 现代 worry','使心里不安；自己担心；担忧与烦心事']]
def O(f,m):return WO+[[f,m]]
W('worry','英 /ˈwʌri/；美 /ˈwɜːri/〔亦有 /ˈwʌri/〕','担心；使担忧；忧虑、烦心事',
 '心里被一件没解决的事揪住，放不下；既可你自己担心，也可事情让你担心。',
 '古英语 wyrġan 原有扼、勒，中古英语还有咬住撕扯等动作；后来转向烦扰、心理困扰。揪住的学习画面有帮助，但不是今天 worry 就在做暴力动作。',WO,
 'worry about the exam 担心考试，The delay worries me. 延误让我担忧，a constant worry 持续烦心事。',
 'worry about；worry that；a constant worry；don’t worry。',
 'I worry about it 自己担心，It worries me 它使我担心；worry about 不宜一律机械改成 worry someone。',
 ('Don’t worry about the tickets; I have them.','别担心票，票在我这里。'),('The delay worries me.','延误让我担忧。'),sources=['https://www.etymonline.com/word/worry','https://en.wiktionary.org/wiki/worry#English'])
W('worried','英 /ˈwʌrid/；美 /ˈwɜːrid/','担心的；发愁的',
 '人心里已经揪着事情，是感受到担忧的这一方。',
 'worry 变 y 为 i + -ed，分词形容词；描述人的担忧状态，也可说担忧神情。',O('worry + -ed → worried','感到担心的、带担忧神情的'),
 'be worried about 担心……，a worried look 担忧神情，worried that 担心某事。',
 'worried about；a worried look；worried that。',
 'worried 感到担心，worrying 让人担心；I am worried 是我在担心，The news is worrying 是消息令人担心。',
 ('She looked worried when the bus failed to arrive.','公交迟迟不来，她显得很担忧。'),('I’m worried about the missing document.','我担心那份不见了的文件。'))
W('worrying','英 /ˈwʌriɪŋ/；美 /ˈwɜːriɪŋ/','令人担心的；担忧活动；worry 的 -ing 形式',
 '消息或趋势让别人心里不安；句子里也可说某人正在担心。',
 'worry + -ing 保留 y，相关活动名词有中古英语旧形。形容词取造成忧虑的效果，不是已经感到忧虑。',O('worry + -ing → worrying','担忧的过程；造成担忧的性质'),
 'a worrying sign 令人担忧的迹象，a worrying trend 令人担忧的趋势，stop worrying 别再担心。',
 'a worrying sign；a worrying trend；stop worrying。',
 'worrying 原因、效果与 worried 感受区分；worrier 又是容易担心的人，不是形容消息的词。',
 ('The report reveals a worrying trend.','报告揭示了一种令人担忧的趋势。'),('Stop worrying about what everyone thinks.','别再为每个人怎么想而担心了。'))
W('worrisome','英 /ˈwʌrisəm/；美 /ˈwɜːrisəm/','令人担忧、烦心的',
 '东西本身有让人放不下心的特点；和 worrying 意思常接近。',
 'worry + -some，-some 形成带某种性质、效果的形容词。拼写去掉词尾 y，接 i，不是独立 some 一些。',O('worry + -some → worrisome','带来忧虑、烦扰的'),
 'a worrisome development 令人担忧的进展，worrisome signs 令人不安的迹象。',
 'a worrisome development；worrisome signs；a worrisome delay。',
 'worrisome 常近 worrying，都是让人担心；worried 是自己担心的状态。不要把 a worried person 与 a worrisome situation 的角色倒过来。',
 ('The sudden silence was worrisome.','突然安静下来让人担心。'),('They discussed several worrisome signs in the report.','他们讨论了报告里的几处令人担忧的迹象。'))
W('worrier','英 /ˈwʌriə/；美 /ˈwɜːriər/','容易担心的人；爱操心的人',
 '事情还没发生，脑子先把各种坏结果都想一遍；按经常担心这个习惯称人。',
 'worry 变 y 为 i + -er。较早相应人物词也有接旧咬伤义的动物用法，今天常指容易忧虑的人。',O('worry + -er → worrier','旧执行者词；现代常指爱担心的人'),
 'a natural worrier 天生爱操心的人，a chronic worrier 总爱担心的人。常是日常性格描述。',
 'a natural worrier；a chronic worrier；be a worrier。',
 'worrier 爱担心的人，warrior /ˈwɒriə/〔英〕是战士；拼写、重音节内元音和词源都不同。',
 ('I’m a worrier, so I always arrive early.','我爱操心，所以总会提早到。'),('She is less of a worrier than her brother.','她没哥哥那么爱担心。'))
R('B4146','旧扼、咬、烦扰到现代心理担忧；原因与感受','WORRY：一件事揪住心，自己担心或使人担心','worry → worried、worrying 对照感受和原因，再 worrisome、worrier；每个词落到角色。',
 '旧动作到烦扰、担忧有历史过程，今天常用心理义。worried 与 worrying 先分好，理解例句会容易很多。',
 'worry + -ed/-ing/-some/-er；-ed/-er 变 y 为 i，-ing 保留 y。',
 [['动作与担忧状态','worry · worried'],['令人担忧与爱担心的人','worrying · worrisome · worrier']],
 'worried 感受、worrying/worrisome 原因；worrier 人不同于 warrior 战士；worry about 与 worry someone 句型分清。',
 'The worrier was worried by the worrying news.\n\n这个爱操心的人因令人担忧的消息而发愁。',
 'worry worried worrying worrisome worrier')
SD=[['古英语 sprǣdan → 中古英语 spreden → spread','铺开、展开、扩散'],['现代 spread','铺展、传播、涂抹；铺开的东西、酱料等名词']]
def S(f,m):return SD+[[f,m]]
W('spread','/spred/','展开、铺开；涂抹；传播、蔓延；涂抹酱料、丰盛一桌等',
 '从一处摊到更大范围：毯子铺开、黄油抹开、消息传开，都抓住覆盖面扩大。',
 '继承古英语 sprǣdan。变化 spread—spread—spread，拼写不变也仍有过去、分词语法；不要把过去式另读成 speed。',SD,
 'spread a blanket 铺毯子，spread butter 涂黄油，spread the news 传播消息，a generous spread 丰盛的一桌。',
 'spread a blanket；spread butter；spread the news；spread out。',
 'spread 铺展到更大范围，scatter 更强调散到各处；spread news 只说明消息传开了，不直接判断消息真假。',
 ('She spread butter on the toast.','她在吐司上抹了黄油。'),('The news spread quickly through the village.','消息很快传遍了村庄。'))
W('spreader','英 /ˈspredə/；美 /ˈspredər/','撒布器；涂抹工具；传播者',
 '把材料均匀铺出去的工具，或把东西、消息传播出去的执行者。',
 'spread + -er，后缀可人、机器、器具。具体是撒种、撒盐、涂酱还是传播，前面的对象说明。',S('spread + -er → spreader','执行铺撒、涂抹或传播的人、工具'),
 'a seed spreader 撒种器，a salt spreader 撒盐机，a butter spreader 黄油抹刀。',
 'a seed spreader；a salt spreader；a butter spreader。',
 'spreader 执行工具或人，spread 名词也可酱料；butter spreader 是抹黄油的器具，不是黄油酱本身。',
 ('The gardener used a spreader to distribute the seeds.','园丁用撒布器播撒种子。'),('A salt spreader moved slowly along the icy road.','撒盐机沿结冰道路缓慢行进。'))
W('spreadsheet','/ˈspredʃiːt/','电子表格；表格工作表',
 '把数据摊在一张有行有列的表上，再做计算、排序和核对；今天常指电子形式。',
 'spread 铺展开 + sheet 表、纸张，来自铺开的表页概念，后来成为电子表格术语。不是 spread 的过去式再接床单。',S('spread + sheet → spreadsheet','铺开的表页 → 电子表格术语'),
 'a budget spreadsheet 预算表，a spreadsheet formula 表格公式，enter data in a spreadsheet 在表格中录入数据。',
 'a budget spreadsheet；a spreadsheet formula；update a spreadsheet。',
 'spreadsheet 是表格文档、工作表或相应工具类别，database 数据库按另一套组织、查询概念称呼；不能仅因都有数据就当完全一样。',
 ('She tracks expenses in a spreadsheet.','她用电子表格记录支出。'),('The spreadsheet calculates the totals automatically.','电子表格会自动计算合计。'))
R('B2989','从一点铺开到更大范围；扩散、撒布和表页','SPREAD：摊开、抹开、传开，都在扩大范围','spread → spreader → spreadsheet；已有 widespread、bedspread 共享，分别看广泛与床上铺盖。',
 '铺开的动作能接实体、消息和数据表。过去、分词同形，靠句子时态识别。',
 'spread—spread—spread；spread + -er/sheet；wide/bed + spread。',
 [['动作与执行者','spread · spreader'],['表页与覆盖物、广泛性','spreadsheet · bedspread · widespread']],
 'spreadsheet 表、spreader 撒布工具；butter spreader 不是酱料；spread 三态同形，读音不换成 speed。',
 'The spreadsheet tracks where the spreader has distributed the seeds.\n\n表格记录撒布器已经在哪些地方播了种。',
 'spread spreader spreadsheet bedspread widespread')
if __name__=='__main__':save('continuation_20261030_bc',ROOTS,WORDS)
