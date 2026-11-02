"""Activation, skills, hubs, lesbian and isolation."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
A=[['拉丁 actīvus → active','能行动、起作用的'],['active → activate','使进入活动、有效状态'],['activate + -or → activator','促使某物起作用的人、物质或装置']]
W('activator','英 /ˈæktɪveɪtə/；美 /ˈæktɪveɪtər/','激活物、活化剂；起激活作用的人或装置',
 '原本没有充分起作用的系统，被某个东西带动起来；这个起激活作用的东西就是 activator。具体是什么，要由所在领域来定。',
 'activate 去末尾 e 加 -or，形成执行或促成动作的名词；底层 active 表处于活动、起作用的状态。',A,
 'a chemical activator 化学活化剂，an enzyme activator 酶激活剂。名称说明它促成激活，具体作用机理需看上下文。',
 'an enzyme activator；add an activator。',
 'activator 说起激活作用的东西，activation 说激活过程；它与 catalyst 催化剂有联系，但两种名称不能在所有领域直接互换。',
 ('The researchers compared two different activators.','研究人员比较了两种不同的活化剂。'),('The reaction began after an activator was added.','加入活化剂后，反应开始了。'))
W('inactivate','/ɪˈnæktɪveɪt/','使失去活性；使不起作用',
 '东西可能还在那里，却不再发挥原来的作用。inactivate 突出把它变成无活性、无效的状态。',
 '可分析为 inactive + -ate，或否定前缀 in- + activate；两种分析都指向使不活跃、使失去作用。',A[:1]+[['inactive + -ate／in- + activate','使成为不活动、无活性的状态']],
 'inactivate an enzyme 使酶失活，inactivate a protein 使蛋白质失去活性。常见于技术、生物化学描述。',
 'inactivate an enzyme；be inactivated。',
 'inactivate 与 deactivate 有重叠；前者很常突出活性丧失，后者也常说停用设备、账号。不要把它们规定成绝对不能重叠的两类。',
 ('The treatment inactivated the enzyme.','这种处理使酶失去了活性。'),('The report explains how the protein becomes inactivated.','报告解释了这种蛋白质如何失去活性。'),sources=['https://en.wiktionary.org/wiki/inactivate#English','https://www.merriam-webster.com/dictionary/inactivate'])
R('B2800','使起作用、激活，以及使失去活性','ACTIVATE：让原本没运转的能力开始起作用','activate → activation、activator；deactivate、inactivate 停用或失活；reactivate 再次激活。',
 '先看起作用，再把过程、促成者和反向操作接起来。失去活性不一定是物体消失，重新激活则是恢复其作用。',
 'active → activate；-ation 过程，-or 促成者；de-、in- 在本组关联停用、无活性，re- 表再次。',
 [['激活、过程与促成者','activate · activation · activator'],['停用、失活与恢复','deactivate · inactivate · reactivate']],
 'activation 是过程，activator 是促成者；inactivate、deactivate 的范围有重叠，按语境选。',
 'The team studied activation and compared the effects of two activators.\n\n团队研究了激活过程，并比较两种活化剂的作用。','activate activation activator deactivate inactivate reactivate')
S=[['skill + -ed → skilled','具有相应技能、经过训练的'],['un- + skilled → unskilled','缺少特定技能训练；工作不要求专门训练']]
W('unskilled','/ʌnˈskɪld/','未经专门技能训练的；不要求专门技能的',
 '刚接触某种技术、还没受过相关训练的人可以 unskilled；工作本身若不要求事先掌握专门技术，也可以这样修饰。',
 'un- 否定 skilled；skilled 是 skill + -ed，表示具有相应技能。-ed 在这里参与形容词构成。',S,
 'an unskilled worker 未受相关专门训练的工人，unskilled work 不要求专门技能的工作。要看具体工种和训练范围。',
 'unskilled work；unskilled labour。',
 'unskilled 不意味着一个人什么本领都没有；它通常针对正在讨论的工作或专业技能。inexperienced 更直接说经验不足。',
 ('The factory offered training to unskilled workers.','工厂为没有相关专门技能的工人提供培训。'),('The advertisement described the position as unskilled work.','招聘广告把这个岗位列为不要求专门技能的工作。'))
R('B4427','具有或缺少特定技能训练','SKILLED：手里的这份活，是否已经受过训练、做得熟','skilled → unskilled。',
 '技能要放在具体任务里看：擅长一门手艺的人，也可能对另一项操作毫无经验。工作分类与人的全部能力分开理解。',
 'skill + -ed → skilled；un- + skilled → unskilled。',
 [['技能状态及其否定','skilled · unskilled']],
 'skilled 强调相应本领；experienced 强调经验；unskilled 通常有具体工作范围。',
 'Skilled workers helped train the unskilled newcomers.\n\n熟练工帮助培训尚无相关技能的新员工。','skilled unskilled')
H=[['早期 hubbe → hub','轮子中心部分；更远来源未定'],['中心实体 → 交通、服务等中心','许多连接集中于一点']]
W('hub','/hʌb/','轮毂；交通枢纽；活动、服务中心',
 '看自行车轮：辐条向中间汇拢的部分是 hub。许多航线、货流或活动汇到同一地方，也借这个中心画面。',
 '早期形式 hubbe，最初是方言词，与 hob 的部分旧形式有关，更远来源不确定。轮子中心义扩展成各种枢纽、中心。',H,
 'a transport hub 交通枢纽，a cultural hub 文化活动中心，a wheel hub 轮毂；a hub for something 是某类活动汇聚的中心。',
 'a transport hub；a hub for trade。',
 'hub 常突出许多联系或路线在此汇聚；centre 的范围更广，单纯几何中心也可用 centre。',
 ('The city became a major transport hub.','这座城市成为重要的交通枢纽。'),('The old warehouse is now a hub for local artists.','那座旧仓库如今是当地艺术家的活动中心。'),sources=['https://en.wiktionary.org/wiki/hub#English','https://www.etymonline.com/word/hub'])
Hu=[['husband 丈夫的口语截短','保留开头并产生昵称形式'],['截短形式 + -y → hubby','丈夫的亲昵、随意称呼']]
W('hubby','/ˈhʌbi/','〔口语、亲昵〕丈夫、老公',
 '不是在介绍正式身份，而是熟人间轻松说我老公、她老公。这个词常带亲昵、随意的口气。',
 'husband 的昵称式缩短，接亲昵后缀 -y；中间拼写发生变化，形成 hubby。这个常用义并非轮毂 hub + -y。',Hu,
 'my hubby 我老公，her hubby 她丈夫。适合亲友对话、随意文字；正式资料通常用 husband。',
 'my hubby；her hubby。',
 'hubby 是称呼风格，不是一种新的婚姻关系；不能把所有称丈夫的正式场合都换成昵称。',
 ('My hubby made dinner while I finished work.','我忙完工作时，老公把晚饭做好了。'),('She and her hubby met at university.','她和丈夫是在大学里认识的。'),sources=['https://en.wiktionary.org/wiki/hubby#English','https://www.etymonline.com/word/hubby'])
R('B3996','轮子中心扩展为枢纽；hubby 的常用义另有来源','HUB：许多连接向中心汇聚','hub 是中心；husband → hubby 是另一路昵称。',
 '从轮毂联想到交通、文化、贸易汇聚点很直观。hubby 虽然开头相同，常用丈夫义却来自 husband，单列在旁边辨清。',
 'hubbe → hub；husband 的截短昵称 + -y → hubby。',
 [['轮毂与枢纽','hub'],['不同来源的丈夫昵称','husband · hubby']],
 'hub 的枢纽义突出连接汇聚；hubby 常用义来自 husband，语体随意。',
 'Her hubby works near the city’s main transport hub.\n\n她丈夫在城市主要交通枢纽附近工作。','hub husband hubby')
L=[['希腊 Lesbos 莱斯博斯岛 → 相关地域形容词','拉丁语、欧洲语言中的相应地域称呼'],['岛上诗人萨福及其关于女性的诗歌','地域名称与女性之间的爱恋相联系'],['英语 lesbian','女同性恋者；女同性恋的']]
W('lesbian','/ˈlezbiən/','女同性恋者；女同性恋的',
 '可以指以女性为恋爱、性吸引对象的女性，也可修饰相关伴侣、作品、生活经历。作名词是人，作形容词说明相关属性。',
 '源头是希腊岛名 Lesbos，经过相关拉丁地域形式及欧洲语言的使用发展。现代义与岛上诗人萨福关于女性的诗歌联系有关，并非把岛上所有人的生活一概而论。',L,
 'a lesbian couple 一对女同性恋伴侣，lesbian literature 女同性恋文学，a lesbian 作人物名词。旧文中的大写 Lesbian 也可能只是地域称呼。',
 'a lesbian couple；lesbian literature。',
 'gay 可以用于同性恋者，lesbian 更具体指女性；名词、形容词的语法位置由句子决定。',
 ('She writes about her life as a lesbian.','她写自己的女同性恋生活经历。'),('The novel follows a lesbian couple moving to a new city.','小说讲述一对女同性恋伴侣迁居新城市后的故事。'),sources=['https://en.wiktionary.org/wiki/lesbian#English','https://www.etymonline.com/word/lesbian'])
W('lesbianism','/ˈlezbiənɪzəm/','女性同性恋；女性之间的同性情感、性取向',
 'lesbian 可以说具体的人，lesbianism 则把女性同性恋这种情感、性取向或相关生活现象拿来讨论。',
 'lesbian + -ism，形成状态、现象的抽象名词。-ism 在这里并不把词变成某种政治主张。',L+[['lesbian + -ism','由人物、属性名称形成抽象现象名词']],
 '常见于文学、历史、社会研究，讨论作品中的呈现、身份和关系；日常称具体人物多用 lesbian。',
 'representations of lesbianism；lesbianism in literature。',
 'lesbianism 通常不可数，不能用 a lesbianism 指一位女性；指人用 a lesbian。',
 ('The book examines representations of lesbianism in twentieth-century fiction.','这本书研究二十世纪小说如何呈现女性同性恋。'),('The exhibition explores lesbianism and women’s friendships in the artist’s work.','展览探讨这位艺术家作品中的女性同性恋与女性友谊。'))
R('B3362','地名经文学关联，形成女性同性恋的现代称呼','LESBIAN：从岛名到与女性之间爱恋相关的称呼','Lesbos → lesbian → lesbianism。',
 '地名成为人物、属性名称，再加后缀成为抽象现象。记住文学关联，就不必把现代意思硬塞进岛名字面。',
 'Lesbos 的地域称呼经过拉丁语及欧洲语言形式发展；lesbian + -ism → lesbianism。',
 [['人物、属性与抽象现象','lesbian · lesbianism']],
 'lesbian 可名词、形容词；lesbianism 通常抽象不可数。古代人物的生平与现代标签不宜简单画等号。',
 'The course discusses lesbian writers and representations of lesbianism in fiction.\n\n这门课讨论女同性恋作家，以及小说中对女性同性恋的呈现。','lesbian lesbianism')
I=[['拉丁 īnsula 岛 → 意大利 isolato、法语 isolé','像成为一座岛一样被隔开'],['英语 isolated → isolate','由已隔开的状态逆构出隔开动作'],['isolate + -or → isolator','实现隔离的装置']]
W('isolator','英 /ˈaɪsəleɪtə/；美 /ˈaɪsəleɪtər/','隔离器、隔离装置',
 '把一个部分和外界隔开，让它不直接受周围影响；承担这种隔离功能的装置就可以叫 isolator。',
 'isolate 去末尾 e 加 -or，形成装置名。isolate 的历史通向拉丁岛的名称，核心画面是像岛一样与周围分开。',I,
 'electrical isolator 电气隔离装置；实验环境中的 isolator 可将内部样品、操作区域与外部环境隔开。不同设备的具体结构、功能由领域决定。',
 'an electrical isolator；a sealed isolator。',
 'isolator 是装置，isolation 是隔离状态或过程；不能只因都译隔离，就把两个名词互换。',
 ('The samples were kept inside a sealed isolator.','样品放在密封隔离装置内。'),('The engineer marked the isolator on the drawing.','工程师在图纸上标出了隔离器。'),sources=['https://en.wiktionary.org/wiki/isolator#English','https://www.etymonline.com/word/isolate'])
R('B4191','像岛一样分开，动作、状态和装置连着理解','ISOLATE：从周围分离出来，像留出一座独立小岛','isolate → isolation、isolator。',
 '可以隔开人、设备或样品，也可以从复杂问题里单独找出一个因素。动作变成状态名词，再变成执行隔离的装置名称。',
 '拉丁 īnsula 岛 → 意大利 isolato、法语 isolé → 英语 isolated；isolate 有逆构过程；-ion 过程、状态，-or 装置。',
 [['隔开、隔离过程与装置','isolate · isolation · isolator']],
 'isolate 的岛意象属于词源，现代不要求真的四面环水；isolator 与 isolation 分别说装置和状态、过程。',
 'The isolator keeps the samples in isolation from the surrounding environment.\n\n隔离装置使样品与周围环境分开。','isolate isolation isolator')
if __name__=='__main__':save('continuation_20261030_lx',ROOTS,WORDS)
