"""Electromechanics, throat and throttling, maturity, and robots."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
W('electromechanical','英 /ɪˌlektrəʊməˈkænɪkəl/；美 /ɪˌlektroʊməˈkænɪkəl/','机电的，结合电与机械作用的',
 '电的控制或能量和实体部件的运动接在一起，比如通电后让触点、机械臂等动作。重点是电与机械两方面的配合。',
 'electro- 电 + mechanical 机械的。electro- 接 electric 的组合形式，mechanical 联系器械、力学一线；中间 o 用于组合，不是独立的或。',
 [['electric → electro-；mechanical 机械的','电的组合形式；机械作用和器械相关性质'],['electro- + mechanical → electromechanical','结合电气与机械作用的']],
 'an electromechanical relay 机电继电器，an electromechanical system 机电系统，electromechanical equipment 机电设备。',
 'an electromechanical relay；an electromechanical system。',
 'electromechanical 不只表示旁边放着电线和机器，通常强调两者在设备中共同作用；electronic 电子的又有自己的技术范围。',
 ('The device uses an electromechanical relay.','这台装置使用机电继电器。'),('The course covers the design of electromechanical systems.','这门课程涵盖机电系统设计。'))
R('B3692','器械、机械作用及不同领域的结合','MECHANICAL：器械或力学相关，也可形容像机械一样做事','mechanical → mechanically；bio-/electro- 指生物力学、机电结合。',
 '先认清 mechanical 的对象：机器、力学作用还是人的机械反应。前缀不是装饰，而是交代和哪一种领域结合。',
 'mechanic 旧器械相关形容词 + -al → mechanical；接 -ly；bio-/electro- + mechanical。',
 [['性质与动作方式','mechanical · mechanically'],['跨领域组合','biomechanical · electromechanical']],
 'mechanical 不只指汽车修理工相关；mechanically 可是机械地、无意识地；electromechanical 强调电与机械结合。',
 'The engineer mechanically repeated the name of the electromechanical component.\n\n工程师机械地重复着那个机电元件的名称。','mechanical mechanically biomechanical electromechanical')
T=[['古英语 þrote 等 → 中古英语 throte → throat','喉部、颈前部，及相应通道'],['部位与狭窄通道的比喻','窄口、喉部；相关旧形式发展出 throttle'],['throat + -y → throaty','从喉部发出的粗哑、低沉声质']]
W('throat','英 /θrəʊt/；美 /θroʊt/','喉咙、喉部；颈前部；窄口、喉状通道',
 '吃东西、发声、吞咽时，日常说喉咙就是这一区域。器具中收窄的入口，也能借这个像喉部通道的形状命名。',
 '接古英语 þrote 等旧词，经中古英语 throte → throat，更深词源有讨论。普通喉咙是区域名，不直接等同单一一根气管或食管。',T[:2],
 'a sore throat 嗓子疼，clear one’s throat 清嗓子，a lump in one’s throat 哽咽的感觉，the throat of a chimney 烟囱喉部窄口。',
 'a sore throat；clear one’s throat；a lump in one’s throat。',
 'throat 普通义是喉部、喉咙，neck 颈部范围更广；clear one’s throat 常为清嗓子或引起注意，不是拿工具清理一根管。',
 ('He cleared his throat before speaking.','他开口前清了清嗓子。'),('She felt a lump in her throat as she read the letter.','她读信时感到一阵哽咽。'))
W('throttle','英 /ˈθrɒtəl/；美 /ˈθrɑːtəl/','节流阀、油门控制；节流、限速；扼住喉部',
 '把通道收窄，流量就受到控制。机器中借来讲节流，网络中再借来讲限制处理或传输速率；具体哪一种流由语境决定。',
 '联系 throat 的旧形式 throtel、throtlen 等，名词、动词历史较复杂。末尾 -le 的具体作用有不同分析，不硬定全部等于小喉咙；机械阀用法后来固定发展。',T[:2]+[['throtel/throtlen 等相关形式 → throttle','喉部、扼住喉部等旧义；词形历史复杂'],['机械通道和抽象速率扩展','节流阀、调节流量 → 限制速度或吞吐量']],
 'open the throttle 加大油门、开大节流控制，at full throttle 全速、全力，throttle a connection 对连接限速，throttle requests 限制请求速率。',
 'at full throttle；open the throttle；throttle a connection；throttle requests。',
 'throttle 动词可广说控制，也常说限制、压低，throttle back 更明确减小。不是所有发动机都用同一结构的气流阀，现代油门称呼也可保留在不同系统里。',
 ('The engine was running at full throttle.','发动机正全速运转。'),('The service throttles requests when demand becomes too high.','需求过高时，服务会限制请求速率。'),sources=['https://en.wiktionary.org/wiki/throttle#English','https://www.etymonline.com/word/throttle'])
W('throaty','英 /ˈθrəʊti/；美 /ˈθroʊti/','喉音重的、低沉粗哑的〔声音〕',
 '一声低低、略粗哑的笑，听起来仿佛从喉部深处带出来。它说声音质地，不是自动说明嗓子生病。',
 'throat + -y，形成具有相应喉音特点的形容词。throat 的元音保留，字母组合 th 在 /θr/ 中仍读清辅音。',T[:1]+[['throat + -y → throaty','喉音较重、粗哑的声质']],
 'a throaty laugh 低沉的喉音笑声，a throaty voice 低沉粗哑的嗓音，a throaty engine sound 低沉轰响的发动机声。',
 'a throaty laugh；a throaty voice；a throaty engine sound。',
 'throaty 是声质描写，hoarse 嘶哑、husky 沙哑有交叠但不完全相同；也能比喻机器声音，不必真有人的喉咙。',
 ('She gave a low, throaty laugh.','她低低地笑了一声，带着喉音。'),('The car produced a throaty rumble.','汽车发出低沉的轰鸣。'))
R('B3909','喉部、收窄通道与声音质地','THROAT：部位、通道、声质分别扩展','throat → throaty；throttle 有复杂旧词形，再扩到机械节流和网络限速；cutthroat 是固定组合。',
 '一条管道的喉部是窄处，这个画面方便理解节流。不要为直观记忆把 -le 的争议历史编得比证据更确定。',
 'þrote → throte → throat；接 -y；相关 throtel/throtlen → throttle；cut + throat。',
 [['部位、声质与流量控制','throat · throaty · throttle'],['激烈竞争的固定比喻','cutthroat']],
 'throaty 不一定是病；throttle 不只说汽车；喉咙普通区域名不等于单一解剖管道。',
 'He cleared his throat, then described the engine’s throaty sound at full throttle.\n\n他清清嗓子，随后描述发动机全速时低沉的轰鸣。','throat throaty throttle cutthroat')
M=[['拉丁 mātūrus；mātūrāre','成熟、时机适当的；使成熟'],['法语、英语 mature 相关形式','长成、成熟；经验和思虑成熟；到期'],['各自派生与借入链','immature 未成熟；maturity 状态；maturation 过程；maturely 方式']]
W('mature','英 /məˈtjʊə/、/məˈtʃʊə/；美 /məˈtʃʊr/','成熟的、发育完全的、深思熟虑的；成熟、使成熟；到期',
 '果实长到可用，人做事考虑周全，计划发展到能落实，都可说 mature。不是只有年纪大才配这个词。',
 '形容词接法语、拉丁 mātūrus，动词联系 mātūrāre 使成熟，英语也经法语相关词形发展。金融到期义借已到相应时点，不是钞票像水果一样变甜。',M,
 'a mature response 成熟稳妥的回应，a mature tree 成树，a mature plan 成熟方案，mature cheese 熟成奶酪，a bond matures 债券到期。',
 'a mature response；a mature tree；a mature plan；mature cheese。',
 'mature 可说身体、心智、行业或产品的成熟，不能当作每个人统一的年龄判定；mature content 常是面向成年人的内容类别，另看作品分级语境。',
 ('She gave a mature response to the criticism.','她成熟稳妥地回应了批评。'),('The idea matured into a workable plan.','那个想法逐渐发展成可行的计划。'),sources=['https://en.wiktionary.org/wiki/mature#English','https://www.etymonline.com/word/mature'])
W('maturely','英 /məˈtjʊəli/、/məˈtʃʊəli/；美 /məˈtʃʊrli/','成熟地、稳妥理智地',
 '受了批评没有马上顶回去，而是听明白、想清楚再回应。这是描述处理方式 maturely，不是在报告年龄。',
 'mature + -ly，保留词尾 e；由成熟这一性质转成做事的方式。',M[:2]+[['mature + -ly → maturely','以成熟、理智或考虑周全的方式']],
 'respond maturely 成熟地回应，handle a disagreement maturely 稳妥处理分歧，behave maturely 表现成熟。',
 'respond maturely；handle a disagreement maturely；behave maturely。',
 'maturely 不等于 slowly 慢慢地；动作很快也能考虑周全。maturely 副词，maturity 是成熟这一状态或程度。',
 ('He handled the disagreement maturely.','他成熟稳妥地处理了分歧。'),('She responded maturely instead of blaming everyone else.','她理智地作了回应，没有把责任都推给别人。'))
W('immature','英 /ˌɪməˈtjʊə/、/ˌɪməˈtʃʊə/；美 /ˌɪməˈtʃʊr/','未成熟的、未发育完全的；幼稚的',
 '植物还没长成是发育状态，人处理事情孩子气是行为评价。不要把所有未成年的生命阶段都翻成贬义幼稚。',
 '经法语 immature，接拉丁 immātūrus。拉丁 in- 不在 m 前同化为 im-，加 mātūrus；现代可按 im- + mature 认形。',M[:1]+[['拉丁 in- + mātūrus → immātūrus → 法语、英语 immature','未到适当成熟时点、未成熟 → 行为幼稚']],
 'an immature plant 未成熟植株，immature behaviour 幼稚行为，an emotionally immature character 情绪处理不成熟的角色。',
 'an immature plant；immature behaviour；emotionally immature。',
 'immature 未成熟，premature 过早，两者不等于同一个时间判断。过早采取的行动也可能由成年人做出。',
 ('The guide distinguishes immature plants from fully grown ones.','指南区分未成熟植株和已经长成的植株。'),('His immature reaction made the discussion more difficult.','他幼稚的反应让讨论更难进行。'))
W('maturity','英 /məˈtjʊərəti/、/məˈtʃʊərəti/；美 /məˈtʃʊrəti/','成熟、成熟度；成年、发育成熟阶段；到期、到期日',
 'mature 说成熟的，maturity 把成熟状态、程度拿出来谈。一个回应显示 maturity，是说考虑事情有分寸。',
 '经中古英语 maturitee、法语 maturité 接拉丁 mātūritās。现代形态对应 mature 去 e + -ity，但名词早有自己的借入链。',M[:1]+[['拉丁 mātūritās → 法语 maturité → 英语 maturity','成熟这一状态、阶段或性质'],['到达约定时点的扩展','债务等到期、到期日']],
 'reach maturity 达到成熟阶段，emotional maturity 情绪处理上的成熟，product maturity 产品成熟度，a maturity date 到期日。',
 'reach maturity；emotional maturity；a maturity date。',
 'maturity 状态、程度，maturation 走向成熟的过程；到期日也不自动说明投资结果好坏。',
 ('The trees take several years to reach maturity.','这些树需要几年才能长成。'),('Her response showed considerable maturity.','她的回应显示出相当成熟的处事态度。'))
W('maturation','/ˌmætʃuˈreɪʃən/','成熟、熟成的过程；发育成熟',
 '不是只看已经成熟的结果，而是看东西怎样一步步发展到那个阶段。生物发育、奶酪熟成、思想发展都可进入这个过程名词。',
 '经法语 maturation 接拉丁 mātūrātiō，来自 mātūrāre 使成熟。现代对应 mature 与 -ation 的过程名词关系；英语早义也曾用于化脓成熟，现代常见读物更常见发育、熟成义。',M[:1]+[['mātūrāre → mātūrātiō → maturation','成熟、使成熟的过程']],
 'the maturation process 成熟过程，biological maturation 生物发育成熟，cheese maturation 奶酪熟成，the maturation of an idea 想法渐趋成熟。',
 'the maturation process；biological maturation；cheese maturation。',
 'maturation 偏过程，maturity 偏状态或程度；成熟过程快慢也不自动等于成品质量或人的价值高低。',
 ('The chapter describes the maturation of the nervous system.','这一章介绍神经系统的发育成熟过程。'),('The tour explains the maturation process of the cheese.','参观讲解介绍了奶酪的熟成过程。'),sources=['https://en.wiktionary.org/wiki/maturation#English','https://www.oxfordlearnersdictionaries.com/definition/english/maturation'])
R('B4312','长到适当阶段，及状态、过程、未成熟和过早','MATURE：长成、发展到位；还可问有没有到时点','mature → maturely；immature 未成熟，premature 过早；maturity 状态，maturation 过程。',
 '成熟可以是生长、心智、方案、产业，也可以是债务到期的比喻。未成熟与过早相互有关，却不说同一件事。',
 'mātūrus / mātūrāre → mature；immātūrus → immature；mātūritās → maturity；mātūrātiō → maturation；praemātūrus → premature。',
 [['基础性质与做事方式','mature · maturely'],['未成熟与时点过早','immature · premature'],['状态和发展过程','maturity · maturation']],
 'mature 不只是年纪大；immature 不全是贬义；maturity 有借入史，不只英语临时加 -ity；maturation 偏过程。',
 'The course follows the maturation process from an immature stage to maturity.\n\n课程追踪从未成熟阶段到成熟的发育过程。','mature maturely immature premature maturity maturation')
B=[['捷克语 robota','苦役、强制劳役、繁重劳动'],['恰佩克兄弟与戏剧 R.U.R. → robot','以人工劳动者命名；由卡雷尔的戏剧传播，约瑟夫建议这一名称'],['现代英语 robot → robotic / robotics','执行任务的机器；相关性质、设计和应用领域']]
W('robot','英 /ˈrəʊbɒt/；美 /ˈroʊbɑːt/','机器人；机械重复、缺乏个人反应的人〔比喻〕',
 '先想被安排来做任务的人工劳动者，后来成为自动执行任务的机器名称。它可以是工厂机械臂，不必长着人的脸。',
 '借捷克语 robot，接 robota 苦役、强制劳动。卡雷尔·恰佩克的戏剧 R.U.R. 让这个词传播，名称建议来自兄弟约瑟夫；不是英语 rob 抢 + ot。',B,
 'an industrial robot 工业机器人，a cleaning robot 清洁机器人，a robot arm 机械臂，act like a robot 像机器一样反应。',
 'an industrial robot；a cleaning robot；a robot arm。',
 'robot 不必像人，也不必具有人的意识。原剧人工劳动者和后来金属机械的典型形象有变化；软件 bot 又是相关缩称扩展，不能把所有机器人都限定同一种机身。',
 ('The factory uses robots to move heavy parts.','工厂用机器人搬运重型零件。'),('The actor deliberately spoke like a robot.','演员故意像机器人一样说话。'),sources=['https://en.wiktionary.org/wiki/robot#English','https://blog.sciencemuseum.org.uk/eric-goes-on-display/'])
W('robotic','英 /rəʊˈbɒtɪk/；美 /roʊˈbɑːtɪk/','机器人的、机器人技术相关的；机械呆板的',
 'robotic arm 说明那条机械臂的技术类型；robotic voice 则像说声音一板一眼、缺少自然变化，未必真由机器人发出。',
 'robot + -ic，相关或像……的形容词。重音从 robot 的开头移到 /bɒt/、/bɑːt/；技术义与比喻机械呆板义分开。',B[:2]+[['robot + -ic → robotic','机器人相关的；像机器人般机械、少变化的']],
 'a robotic arm 机械臂，robotic equipment 机器人设备，a robotic voice 呆板机械的声音，robotic movements 机械式动作。',
 'a robotic arm；robotic equipment；a robotic voice。',
 'robotic 描写设备时可中性，评价人的反应时常嫌生硬；不是每个 robotic device 都有人形外壳。',
 ('A robotic arm lifted the container.','一条机械臂抬起了容器。'),('His robotic delivery made the speech sound unnatural.','他机械呆板的表达让演讲显得不自然。'))
W('robotics','英 /rəʊˈbɒtɪks/；美 /roʊˈbɑːtɪks/','机器人学、机器人技术',
 'robot 是机器，robotics 是研究和实现它们怎样设计、制造、感知、控制、工作的领域。不是把很多 robotic 形容词堆成复数。',
 'robot + 学科、技术领域词尾 -ics；阿西莫夫的科幻作品使用、传播了这个技术领域名称。-ics 在此像 mechanics 等学科名词尾，不是普通名词复数。',B[:2]+[['robot + -ics → robotics','关于机器人的设计、制造、控制与应用的领域']],
 'study robotics 学机器人技术，a robotics club 机器人社团，robotics research 机器人学研究，a robotics project 机器人项目。',
 'study robotics；a robotics club；robotics research。',
 'robotics 作学科通常接单数谓语：Robotics is…；robots 才是 robot 的普通复数。robotic 是形容词，不能直接替换学科名。',
 ('She joined the school’s robotics club.','她加入了学校的机器人社团。'),('Robotics is a field that combines several branches of engineering.','机器人学是结合多个工程分支的领域。'),sources=['https://en.wiktionary.org/wiki/robotics#English','https://www.merriam-webster.com/dictionary/robotics'])
R('B2441','人工劳动者的戏剧名称，发展为机器与技术领域','ROBOT：承担任务的人工劳动者 → 现代机器人','robot 机器 → robotic 相关性质 → robotics 技术领域。',
 '名称从文学走进工程，外形和能力不必永远和最初作品相同。按名词、形容词、学科名分清，读音还要留意重音移动。',
 'robota → robot；robot + -ic / -ics。',
 [['机器、性质与学科','robot · robotic · robotics']],
 'robot 不只人形；robotic 可比喻机械反应；robotics 学科接单数谓语，robots 才是机器人的复数。',
 'The robotics club built a robot with a small robotic arm.\n\n机器人社团制作了一台带小机械臂的机器人。','robot robotic robotics')
if __name__=='__main__':save('continuation_20261030_is',ROOTS,WORDS)
