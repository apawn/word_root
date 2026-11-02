"""Common -or people and instruments, with their useful base words."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
def O(word,ipa,meaning,base,base_meaning,sense,explanation,usage,contrast,*examples,history=None,sources=None):
 stem=base[:-1] if base.endswith('e') else base
 assert stem+'or'==word,(base,word)
 W(word,ipa,meaning,sense,f'现代对应 {base}'+(' 去 e' if base.endswith('e') else '')+f' 加 -or → {word}；词尾在这里形成做相关事情的人、装置或部件名称。',history or [[base,base_meaning],[word,meaning]],explanation,usage,contrast,*examples,sources=sources)
Ry=[['法语 realité 的财产、地产义 → 英语 realty','财产、地产；与 reality 同族'],['realty 的材料与 -or 类推 → realtor','房地产行业人员的命名；REALTOR® 有会员标识专义']]
W('realty','/ˈrɪəlti/','房地产、不动产〔尤美式、行业用语〕',
 '不是说东西真实，而是在谈土地、房产这一类不动产；公司名字、行业介绍里经常能看到 Realty。',
 '借法语 realité 的财产、地产相关旧义，与 reality 现实是同族的不同借入、意义发展。不能因为今天 real 是真实就把 realty 翻成真实性。',Ry,
 'commercial realty 商业房地产；realty services 房地产服务；a realty company 房地产公司。',
 'commercial realty；a realty company。',
 'realty 是地产，reality 是现实；两词都有 real 的历史材料，却不在现代随便互换。',
 ('The firm specialises in commercial realty.','这家公司专做商业房地产。'),('She works for a local realty company.','她在当地一家房地产公司工作。'))
W('realtor','英 /ˈrɪəltə/；美 /ˈriːəltər/','房地产经纪业人员；REALTOR® 正式指相关协会会员',
 '在美国地产语境里很常见。正式的 REALTOR® 是美国全国房地产经纪人协会的会员标识，不能把所有地产经纪人都默认算进这个身份。',
 '二十世纪初以 real estate、realty 的材料，类推 -or、-tor 人员名词而造；不是 real + 一个常用 tor 词根。',Ry,
 'a REALTOR® 房地产经纪人协会会员；work with a REALTOR® 与这样的地产专业人士合作。日常小写泛称用法与正式标识范围分清。',
 'a REALTOR®；REALTOR® membership。',
 'real-estate agent 是一般地产经纪人称呼；REALTOR® 还强调协会会员身份。这里解释词义范围，不由后缀推定执照、合同权利等。',
 ('The brochure identifies her as a REALTOR®.','宣传册注明她是 REALTOR® 会员。'),('Not every real-estate agent is a REALTOR®.','不是每位房地产经纪人都是 REALTOR® 会员。'),sources=['https://en.wiktionary.org/wiki/realtor#English','https://www.nar.realtor/membership-marks-manual'])
Cr=[['旧动词 carburet','使带有碳、烃类材料等旧化学用法'],['carburet + -or → carburetor、carburettor','相关装置；发动机中混合燃油与空气的化油器']]
W('carburetor','美 /ˈkɑːrbəreɪtər/；英式变体常 /ˌkɑːbəˈretə/','化油器〔常见美式拼写〕',
 '汽油机的一种部件，把燃油与空气调成能供发动机使用的混合物，这就是 carburetor。它的工作不是单纯存油。',
 '旧动词 carburet 的含碳、烃类混合材料 + -or，后来固定为化油器名称；开头不按现代 car 汽车加一串尾字母解释。',Cr,
 'an engine carburetor 发动机化油器；a carburetor adjustment 化油器调整。',
 'a carburetor；the engine’s carburetor。',
 'carburetor 是混合、供给相关部件，fuel tank 是油箱；不是所有发动机今天都使用化油器。',
 ('The mechanic inspected the old engine’s carburetor.','机械师检查了旧发动机的化油器。'),('The diagram shows how the carburetor mixes fuel and air.','示意图展示化油器如何混合燃油与空气。'))
W('carburettor','英 /ˌkɑːbəˈretə/；美 /ˈkɑːrbəreɪtər/','化油器〔常见英式拼写〕',
 '和 carburetor 是同一种发动机部件；这里双写 t 属拼写变体，不表示另一套工作原理。',
 'carburet 与 -or 的相应形式，英式常写 carburettor，美式常写 carburetor；词义相同，发音有常见地区差异。',Cr,
 'an engine carburettor 发动机化油器；发动机维修手册、老车介绍里常见。',
 'a carburettor；carburettor maintenance。',
 'carburettor 与 carburetor 是拼写变体，不等于一个只用于汽车、一个只用于摩托车。',
 ('The manual includes a drawing of the carburettor.','手册收有化油器示意图。'),('The museum displays an early engine with its original carburettor.','博物馆展出一台保留原化油器的早期发动机。'),sources=['https://en.wiktionary.org/wiki/carburettor#English','https://www.oxfordlearnersdictionaries.com/definition/english/carburettor'])
Gu=[['法语 guarantie、guarantir 等，远接日耳曼语相关材料','保护、担保、作保证'],['英语 guarantee、guarantor','保证；担保人、保证者']]
W('guarantee','/ˌɡærənˈtiː/','保证；担保；保修、保证承诺',
 '不是说大概会，而是明确承诺结果、质量或承担相应责任，可以说 guarantee；作名词就是这份保证。',
 '借法语 guarantie 等担保材料，与 guaranty、warranty 有历史联系；末尾不是表示小、人的 -ee 后缀就能解释全词。',Gu,
 'guarantee that 保证某事；a guarantee of quality 质量保证；under guarantee 在保修期内；no guarantee of success 不保证成功。',
 'guarantee that；no guarantee of；under guarantee。',
 'guarantee 常是明确保证，不等于 prediction 预测。具体承诺覆盖什么，仍看它实际说了什么。',
 ('The new method does not guarantee success.','新方法不保证一定成功。'),('The printer is still under guarantee.','打印机仍在保修期内。'))
W('guarantor','英 /ˌɡærənˈtɔː/；美 /ˌɡærənˈtɔːr/','担保人；保证者',
 'guarantee 是保证，guarantor 是站出来承担保证职责的人或机构。谈协议、租约等时要看具体为哪件事作保。',
 'guarantee 的 guarant- 词干材料 + -or，末段 ee 不保留；不是完整 guarantee 再原样加 or。',Gu,
 'act as guarantor 担任保证者；a guarantor for someone 为某人作保的担保人。',
 'act as a guarantor；a guarantor of。',
 'guarantor 是作保证的一方；borrower 是借款人。两种角色不同，不能因为都在一份文件里就混为同一人。',
 ('The document names her as the guarantor.','文件列明她为担保人。'),('The organisation agreed to act as guarantor of the arrangement.','组织同意担任该安排的保证者。'),sources=['https://en.wiktionary.org/wiki/guarantor#English','https://www.oxfordlearnersdictionaries.com/definition/english/guarantor'])
Ac=[['拉丁 actus → 中世纪拉丁 actuare、actuatus 等','行动；使付诸行动、使运转的材料'],['英语 actuate → actuator','驱动、使动作；执行器、驱动装置']]
W('actuate','英 /ˈæktʃueɪt/；也读 /ˈæktjueɪt/','使动作、驱动；促使行动〔正式〕',
 '传感器给出信号，某个机构真的动起来，actuate 就是让它动作。较正式地说人被某种动机促动，也能用这个词。',
 '借中世纪拉丁 actuatus 等，接 actus 行动材料；-ate 外形有借入历史，不只是拿现代 act 后面随意接 uate。',Ac,
 'actuate a valve 驱动阀门；actuated by pressure 由压力使之动作；actuated by curiosity 受好奇心促使，较正式。',
 'actuate a mechanism；be actuated by。',
 'actuate 使部件实际动作，activate 更广可说启用、激活系统；启用功能未必马上出现机械运动。',
 ('The signal actuates a small motor.','信号驱动一个小电机。'),('The valve is actuated by changes in pressure.','阀门由压力变化驱动。'))
O('actuator','英 /ˈæktʃueɪtə/；美 /ˈæktʃueɪtər/','执行器；驱动装置','actuate','使部件动作、驱动',
 '控制系统发出命令，还需要一个部件把命令变成实际运动；做这一步的装置常叫 actuator。',
 '电动、气动、液压等执行器有不同工作方式，共同点是按控制、输入产生相应动作。',
 'a valve actuator；an electric actuator。',
 'sensor 感知情况，actuator 执行动作；一个负责看见变化，一个负责让部件动起来，角色不同。',
 ('The actuator opens and closes the valve.','执行器控制阀门开闭。'),('The robot uses small actuators to move its fingers.','机器人用小型执行器活动手指。'),history=Ac)
O('impersonator','英 /ɪmˈpɜːsəneɪtə/；美 /ɪmˈpɜːrsəneɪtər/','模仿名人的演员；冒充他人者','impersonate','扮成、模仿或冒充另一个人',
 '在舞台上把某位歌手的声音、动作学得很像，是 impersonator；若冒充真实身份骗人，也可用这个词，场景决定性质。',
 'an Elvis impersonator 是猫王模仿演员，不自动等于身份诈骗者；这里重在扮成某个特定的人。',
 'a celebrity impersonator；a voice impersonator。',
 'imitator 更广指模仿者；impersonator 常是模仿、扮成特定人物，尤其声音、外貌、动作或身份。',
 ('The show featured a talented Elvis impersonator.','节目中有一位很有才的猫王模仿演员。'),('The platform removed the impersonator’s account.','平台移除了冒充他人者的账号。'))
O('accumulator','英 /əˈkjuːmjəleɪtə/；美 /əˈkjuːmjəleɪtər/','累加器；蓄积装置；蓄电池〔部分用法〕','accumulate','一点点累积、积攒',
 '数字不断往同一个总数里加，是程序里的 accumulator；某些装置把电能、压力等蓄起来，也沿着积存这个画面命名。',
 '不同领域有不同具体设备；看程序、汽车或液压文档时，先判断积起来的是什么。',
 'an accumulator variable；a hydraulic accumulator。',
 'accumulator 常突出累计、储存；generator 是发生器、发电机等。积存和产生不是同一个过程。',
 ('The loop adds each value to an accumulator.','循环把每个值加入累加器。'),('The diagram shows a hydraulic accumulator in the system.','示意图展示了系统中的液压蓄能器。'),history=[['拉丁 accumulare、accumulator 等','堆积、积攒；做相关事的人'],['英语 accumulator','累加器、不同领域的蓄积装置']])
O('defibrillator','英 /diːˈfɪbrɪleɪtə/；美 /diːˈfɪbrɪleɪtər/','除颤器','defibrillate','对特定异常心律施行除颤',
 '心脏有些危险的异常节律需要电击来纠正，施行这种电治疗的装置叫 defibrillator。公共场所常见的 AED 属自动体外除颤器这一类。',
 '命名指向除颤作用；设备形式、适用节律不同，不能把词义缩成对任何停止跳动都能电醒。',
 'an automated external defibrillator；an implantable defibrillator。',
 'defibrillator 纠正某些危险心律；pacemaker 起搏器主要通过电脉冲帮助调节心率。某些设备可兼有功能，名称侧重不同。',
 ('The airport installed a defibrillator near the main entrance.','机场在主入口附近安装了一台除颤器。'),('The training introduced the purpose of an automated external defibrillator.','培训介绍了自动体外除颤器的用途。'),history=[['de- + fibrillation 等 → defibrillate','去除、纠正心脏纤维颤动的相关命名'],['defibrillate + -or → defibrillator','除颤装置']],sources=['https://en.wiktionary.org/wiki/defibrillator#English','https://www.nhlbi.nih.gov/health/defibrillators'])
O('detonator','英 /ˈdetəneɪtə/；美 /ˈdetəneɪtər/','雷管；起爆器','detonate','爆炸、引爆',
 '在较大的爆炸系统里，用来启动爆炸的那个装置叫 detonator。它说的是起爆部件，不是所有爆炸物的统称。',
 'detonate 是引爆、爆炸，-or 在这里形成执行起爆作用的装置名。',
 'a detonator；a faulty detonator。',
 'detonator 是起爆部件，detonation 是爆炸、爆轰过程；装置和事件分开。',
 ('The report identified a fault in the detonator.','报告指出起爆器存在故障。'),('The museum display labels the detonator separately from the casing.','博物馆展板把起爆器与外壳分别标出。'))
O('liquidator','英 /ˈlɪkwɪdeɪtə/；美 /ˈlɪkwɪdeɪtər/','清算人；负责清理、处置业务资产的人','liquidate','清算、变卖资产、了结等',
 '公司进入清算，需要有人负责整理、处置资产、处理相关事务，这种角色叫 liquidator。不是把东西变成水的人。',
 'liquidate 有金融、商业中的清算义，-or 将该职责落到承担的人；具体职权由相应制度、委任决定。',
 'appoint a liquidator；the company’s liquidator。',
 'liquidator 是清算职责人员，receiver 是接管人；两者在一些制度里可有联系，但不凭相似中文就认为职权完全相同。',
 ('The company appointed a liquidator.','公司指定了一名清算人。'),('The liquidator prepared a report on the remaining assets.','清算人编写了剩余资产报告。'))
O('corrector','英 /kəˈrektə/；美 /kəˈrektər/','纠正者；校正器、校正用品','correct','纠正、校正',
 '把原来偏掉、写错的部分改正，做这个动作的人或用品可以叫 corrector；具体是文本、颜色还是光学，要看修饰词。',
 '不是所有 corrector 都是一个职业，现代常见于产品、功能名：colour corrector 是色彩校正用品、工具。',
 'a colour corrector；an error corrector。',
 'corrector 校正器、纠正者，correction 校正、修正结果；correct 本身还能是正确的形容词。',
 ('The software includes an automatic error corrector.','软件包含自动纠错功能。'),('She used a colour corrector before applying foundation.','她涂粉底前用了肤色校正用品。'),history=[['中古英语 corrector 等；对应 correct','纠正、校正相关的人、用途'],['现代 corrector','不同领域的校正工具、用品或人员']])
O('illuminator','英 /ɪˈluːmɪneɪtə/；美 /ɪˈluːmɪneɪtər/','照明装置；彩饰手稿的人；提亮用品','illuminate','照亮；阐明；彩饰手稿',
 '灯把对象照亮，是 illuminator 的设备义；中世纪给手稿做彩绘、装饰的人也可这样叫。现代化妆品里还可说提亮用品。',
 '同一 illuminate 词族在照明、手稿装饰、美妆里各有固定用法，不能把每个人员名都只译成开灯的人。',
 'an infrared illuminator；a manuscript illuminator。',
 'illuminator 是装置、人或用品，illumination 是照明、启发、彩饰等过程或结果，按场景分义。',
 ('The camera uses an infrared illuminator in low light.','相机在弱光下使用红外照明装置。'),('The manuscript was decorated by a skilled illuminator.','这份手稿由一位熟练的彩饰师装饰。'))
O('fabricator','英 /ˈfæbrɪkeɪtə/；美 /ˈfæbrɪkeɪtər/','制造、加工者；捏造者','fabricate','制造、加工；捏造、编造',
 '把金属部件加工成形，可以是 fabricator；把不存在的证据编出来，也是 fabricator 的另一义。要看做出来的是实体还是假故事。',
 'metal fabricator 常是金属加工厂商、工人；a fabricator of lies 则是编造谎言的人。',
 'a metal fabricator；a fabricator of evidence。',
 'fabricator 不只骗人者，也不只造布的人；fabricate 的制造义与捏造义都能形成对应人员名。',
 ('The project hired a local metal fabricator.','项目聘用了一家当地金属加工厂商。'),('The witness was exposed as a fabricator of evidence.','证人被揭露捏造了证据。'))
O('imitator','英 /ˈɪmɪteɪtə/；美 /ˈɪmɪteɪtər/','模仿者；仿效者','imitate','模仿、仿效',
 '学别人的风格、产品、做法，是 imitator；可以是学习，也可以是在批评缺少自己的东西。',
 '人物、品牌、创作者都可能被叫 imitator。判断好坏要看模仿目的、程度，词本身不自动等于犯法。',
 'an imitator of someone；a cheap imitator。',
 'imitator 泛指仿效者，impersonator 常具体扮成某个人；模仿画风的人不必扮成画家本人。',
 ('The successful design attracted many imitators.','成功的设计引来了许多模仿者。'),('She began as an imitator but later developed her own style.','她起初模仿别人，后来形成了自己的风格。'),history=[['拉丁 imitator、法语 imitateur 等','模仿者的相应词形'],['英语 imitator；对应 imitate + -or','模仿、仿效的人']])
O('infiltrator','英 /ˈɪnfɪltreɪtə/；美 /ˈɪnfɪltreɪtər/','渗透者；潜入者','infiltrate','逐渐渗入；秘密潜入',
 '不是公开从大门报名加入，而是隐瞒身份、目的进入某组织，故事、报道里这样的人可叫 infiltrator。',
 'infiltrate 的渗入、潜入义转成人员名；语境常涉及秘密进入，但也有不同领域的专门用法。',
 'an infiltrator in the group；identify an infiltrator。',
 'infiltrator 说秘密渗入者，intruder 更广说未经许可闯入者；闯进来未必一直隐藏身份。',
 ('The novel follows an infiltrator inside a criminal organisation.','小说追踪一个潜入犯罪组织的人的经历。'),('The group suspected that one member was an infiltrator.','这个团体怀疑一名成员是渗透者。'))
O('iterator','英 /ˈɪtəreɪtə/；美 /ˈɪtəreɪtər/','迭代器〔编程〕','iterate','重复、逐次进行',
 '把一串数据想成排队的人；程序按约定一次取下一个，提供这种逐项访问方式的对象常叫 iterator。',
 '不同语言接口不同。在 Python 中，迭代器能用 next 取下一个值；耗尽后按协议表示结束。它不是每次都把所有数据先装进列表。',
 'an iterator over a sequence；advance an iterator。',
 'iterator 是按协议逐项提供值的对象；iterable 是能从中取得迭代器的对象。Python 中二者有关但不是同一个概念。',
 ('The function returns an iterator over the rows.','函数返回一个逐行访问的迭代器。'),('The iterator is exhausted after the last item.','取完最后一项后，迭代器就耗尽了。'),sources=['https://en.wiktionary.org/wiki/iterator#English','https://docs.python.org/3/glossary.html#term-iterator'])
W('protractor','英 /prəˈtræktə/；美 /prəˈtræktər/','量角器',
 '把中心对准角的顶点，看另一条边对应多少度，课堂里用来量角的工具叫 protractor。词里有拉、画出的历史材料，不是拖拉机。',
 '接拉丁 protrahere 向前拉、引出及 protract- 变化词干，-or 作人员、工具名。英语早期另有延长某事的人等义，常用工具义后来固定到量角器。',
 [['拉丁 pro- + trahere → protract-','向前拉、引出、延长'],['protractor 的测绘用法','测量、画出角度的工具']],
 'a protractor and a ruler 量角器和直尺；measure an angle with a protractor 用量角器量角。',
 'use a protractor；a semicircular protractor。',
 'protractor 是量角器，tractor 是拖拉机、牵引设备；同有拉的历史词干，现代指的工具不同。',
 ('Use a protractor to measure the angle.','用量角器测这个角。'),('She packed a ruler and a protractor in her pencil case.','她把直尺和量角器放进铅笔盒。'),sources=['https://en.wiktionary.org/wiki/protractor#English','https://www.etymonline.com/word/protractor'])
R('A1761','做某事的人；具有相应功能的装置、部件','-OR：谁在做，或什么装置在起作用','imitate 模仿 → imitator 模仿者；actuate 使动作 → actuator 执行器；iterate 逐次进行 → iterator 迭代器。先抓动作，再看是人还是工具。',
 'actor 是人，elevator 是设备；同一个人员、工具名词尾，在不同领域会给不同对象命名。fabricator 既可制造部件，也可捏造证据，要随 fabricate 的义项区分；protractor 则已成为量角器这一固定工具名，不能只译成向前拉的人。',
 '常接拉丁、法语人员名词材料，如 -tor、-sor、-ator 等，英语又按动词继续构词。现代常见 -ate 去 e 加 -or：imitate → imitator、illuminate → illuminator；correct + -or → corrector；guarantee 使用 guarant- 词干 → guarantor。并非每个词都能把 -or 删除后得到完整英语动词，也不能认为所有结尾 or 都是做事的人：color、horror 等有另外的借入、词尾历史。-er 与 -or 的选择由单词形成和惯例决定，不随意互换。',
 [['地产与作保证的角色','real · realty · realtor · guarantee · guarantor'],['发动机和驱动部件','carburetor · carburettor · actuate · actuator'],['模仿、冒充与渗透的人','imitate · imitator · impersonate · impersonator · infiltrate · infiltrator'],['积累、照明和纠正的功能','accumulate · accumulator · illuminate · illuminator · correct · corrector'],['制造和清算','fabricate · fabricator · liquidate · liquidator'],['逐次访问数据','iterate · iterator'],['具体工具的固定名称','defibrillator · detonator · protractor']],
 'REALTOR® 正式指协会会员，不是所有地产代理人；carburetor／carburettor 是英美拼写变体；fabricator 可制造也可捏造；iterator 与 iterable 在 Python 中有关但不同；protractor 量角器与 tractor 拖拉机分开。',
 'The designer, fabricator and inspector each checked a different part of the project.\n\n设计者、加工者和检查员分别核查了项目的不同部分。',
 'real realty realtor carburetor carburettor guarantee guarantor actuate actuator impersonate impersonator accumulate accumulator defibrillator detonate detonator liquidate liquidator correct corrector illuminate illuminator fabricate fabricator imitate imitator infiltrate infiltrator iterate iterator protractor actor senator operator inspector chancellor instructor advisor survivor investor elevator generator coordinator processor investigator reactor narrator sailor contributor detector solicitor translator distributor regulator simulator calculator spectator connector illustrator accelerator projector compressor inhibitor radiator sculptor proprietor conveyor terminator capacitor selector incubator negotiator predictor debtor innovator resistor reflector ventilator communicator elector oscillator decorator suppressor animator demonstrator facilitator motivator originator injector interceptor manipulator alternator activator aggregator estimator incinerator insulator oppressor excavator respirator prospector agitator applicator integrator objector deflector evaporator adjudicator ejector eliminator stressor convenor licensor pollinator replicator cultivator franchisor compensator inheritor differentiator authenticator depositor orchestrator procrastinator bettor isolator')
for x in WORDS:
 if x['word']=='actuator':x['sources'].append('https://www.merriam-webster.com/dictionary/-or')
if __name__=='__main__':save('continuation_20261030_qd',ROOTS,WORDS)
