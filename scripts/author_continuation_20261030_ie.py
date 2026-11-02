"""Common -ization families, with missing everyday bases explained first."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
S=[['拉丁 sterilis → 法语 stérile → sterile','不生育、不结果 → 无产出'],['sterile + -ize → sterilize','使不能繁殖；医学中使达到无菌状态'],['sterilize + -ation → sterilization','上述处理的过程、结果']]
W('sterile','英 /ˈsteraɪl/；美 /ˈsterəl/','无菌的；不能生育、繁殖的；无成果、乏味的',
 '最老的核心是不产生后代、结不出成果；医学里强调没有可存活微生物，讨论里也可说怎么争都没结果。',
 '经法语接拉丁 sterilis 不育、无产出。无菌与不育有繁殖这一概念联系，但现代是不同判断：一个人不育，不等于其身体无菌。',S,
 'sterile equipment 无菌器械，a sterile container 无菌容器，sterile offspring 不能繁殖的后代，a sterile debate 无成果的争论。',
 'sterile equipment；a sterile container；a sterile debate。',
 'sterile 无菌不只是 visually clean 看着干净；sterile debate 不是没有细菌的辩论，而是空转无成果。',
 ('The sample was placed in a sterile container.','样品被放进无菌容器。'),('The meeting became a sterile debate about definitions.','会议变成一场围着定义空转、没有成果的争论。'),sources=['https://en.wiktionary.org/wiki/sterile#English','https://www.cdc.gov/infection-control/hcp/disinfection-sterilization/glossary.html'])
W('sterilize','英 /ˈsterɪlaɪz/；美 /ˈsterəlaɪz/','使无菌、灭菌；使不能繁殖、施行绝育',
 '把 sterile 这种状态做出来；面对器械说无菌，面对生殖能力则可能说绝育，不能只看一个中文消毒。',
 'sterile 去 e + -ize。医学灭菌与绝育是现代不同用法；英式也常见 sterilise。',S,
 'sterilize instruments 给器械灭菌，sterilize containers 给容器灭菌，sterilize an animal 使动物绝育。具体操作不是词尾本身给出的。',
 'sterilize instruments；sterilize containers；sterilize an animal。',
 'sterilize 灭菌与 disinfect 消毒不完全相同：前者以去除、消灭所有形式微生物为标准，后者并非都覆盖细菌芽孢。clean 清洁又是另一概念。',
 ('The instruments were sterilized before use.','器械使用前经过了灭菌。'),('The report distinguishes sterilizing equipment from simply cleaning it.','报告区分了器材灭菌和单纯清洁。'),sources=['https://en.wiktionary.org/wiki/sterilize#English','https://www.cdc.gov/infection-control/hcp/disinfection-sterilization/introduction-methods-definition-of-terms.html'])
W('sterilization','英 /ˌsterɪlaɪˈzeɪʃən/；美 /ˌsterələˈzeɪʃən/','灭菌；绝育〔另一用法〕',
 '将使无菌或使不能繁殖这件事，作为过程来谈；对象不同，词的中文落点不同。',
 'sterilize + -ation，也可认 sterile + -ization；去掉动词末尾 e 再接名词词尾。英式也写 sterilisation。',S,
 'equipment sterilization 设备灭菌，a sterilization process 灭菌过程，surgical sterilization 外科绝育。',
 'equipment sterilization；a sterilization process；surgical sterilization。',
 'sterilization 不等于所有 cleaning 清洁，也不能一见它就认为是在谈避孕绝育；先看 equipment、surgical 等搭配。',
 ('The laboratory keeps records of equipment sterilization.','实验室保存设备灭菌记录。'),('The chapter discusses sterilization in the history of reproductive medicine.','这一章讨论生殖医学史中的绝育。'),sources=['https://en.wiktionary.org/wiki/sterilization#English','https://www.cdc.gov/infection-control/hcp/disinfection-sterilization/glossary.html'])
I=[['拉丁 in- 不 + mūnus 义务、公共服务 → immūnis','免于某种负担、义务'],['法语相关形式 → immune','豁免 → 不易受某事影响；医学免疫'],['immunize / immunization','使产生免疫保护；形成保护的过程']]
W('immune','/ɪˈmjuːn/','免疫的；免于、不受某事影响的；免疫系统的',
 '先想某种本来会落到身上的影响被挡在外面：免缴义务是早期背景，不受疾病、批评影响是后来不同用法。',
 '经法语接拉丁 immūnis，in- 不在 m 前同化为 im-，后半 mūnus 是公共义务、服务等。医学免疫是豁免、免受影响的专门发展。',I,
 'immune to criticism 不受批评影响，immune to a particular disease 对特定疾病有免疫力，the immune system 免疫系统。',
 'immune to；immune from；the immune system。',
 'immune 通常说明对什么有保护，不等于对所有疾病绝对不会中招；immune to criticism 又常是比喻。immune system 是整体系统名。',
 ('No organization is immune to criticism.','没有哪个组织能免于批评。'),('The lesson explains how the immune system recognizes threats.','课程解释免疫系统怎样识别威胁。'),sources=['https://en.wiktionary.org/wiki/immune#English','https://www.cdc.gov/vaccines/basics/explaining-how-vaccines-work.html'])
W('immunize','/ˈɪmjʊnaɪz/','使免疫、使获得免疫保护',
 '不是只知道某种疾病，而是让身体具备应对它的保护；常见通过疫苗形成这种保护。',
 '借法语 immuniser，现代对应 immune 去 e + -ize。英式变体 immunise；不能把中间 immun- 拆成 in + 一个现代单词 mun。',I,
 'immunize against a disease 针对某种疾病使人获得免疫保护，an immunized population 获得相应免疫保护的人群；也可有使不受影响的比喻。',
 'immunize against；be immunized against。',
 'immunize 侧重使获得免疫保护，vaccinate 侧重接种疫苗的动作。两者常同一场景出现，但概念焦点不同。',
 ('The campaign aimed to immunize children against measles.','那次活动旨在让儿童获得针对麻疹的免疫保护。'),('The textbook explains how vaccines can immunize the body against specific infections.','教材解释疫苗如何让身体获得针对特定感染的免疫保护。'),sources=['https://en.wiktionary.org/wiki/immunize#English','https://www.cdc.gov/vaccines/basics/explaining-how-vaccines-work.html'])
W('immunization','英 /ˌɪmjʊnaɪˈzeɪʃən/；美 /ˌɪmjənəˈzeɪʃən/','免疫、使获得免疫保护的过程；预防接种〔常见用法〕',
 '把获得保护当作一个过程来看。日常免疫接种活动常用这个词，但它强调的不是针扎进去本身，而是形成相应保护。',
 '接法语 immunisation，现代对应 immunize + -ation 或 immune + -ization。immunisation 是常见英式拼写。',I,
 'an immunization programme 免疫接种项目，immunization records 预防接种记录，routine immunization 常规免疫接种。',
 'an immunization programme；immunization records；routine immunization。',
 'vaccination 是接种动作，immunization 是获得相应免疫保护的过程，常被日常近义使用；保护程度不由一个词保证绝对。',
 ('The school asked parents for their children’s immunization records.','学校请家长提供孩子的预防接种记录。'),('The chart summarizes the local immunization programme.','图表概述了当地免疫接种项目。'),sources=['https://en.wiktionary.org/wiki/immunization#English','https://medlineplus.gov/vaccines.html'])
H=[['拉丁 hibrida/hybrida → hybrid','混合血统的后代 → 混合来源的东西'],['hybrid + -ize → hybridize','让不同来源杂交、混合'],['hybridize + -ation → hybridization','杂交、杂化等专门过程']]
W('hybrid','/ˈhaɪbrɪd/','杂交后代；混合体；混合的；混合动力车',
 '把不同来源的材料、血统或工作方式放在同一个东西里；植物可杂交，课程可线上线下混合，汽车可用不同动力系统。',
 '接拉丁 hibrida/hybrida 混合血统后代等词。不是英文 high 高 + 某个 brid；现代意义已远超生物繁殖。',H,
 'a hybrid car 混合动力车，a hybrid model 混合模式，hybrid learning 混合式学习，a hybrid of two styles 两种风格的混合体。',
 'a hybrid car；a hybrid model；hybrid learning；a hybrid of。',
 'hybrid 不保证混合后一定更好，也不等于纯电动 electric；生物杂交后代也不是必然都不育，要看具体情况。',
 ('The course uses a hybrid model of online and classroom learning.','课程采用线上与课堂结合的混合模式。'),('The garden contains hybrids with several different flower colours.','花园里有几种花色不同的杂交品种。'))
W('hybridize','/ˈhaɪbrɪdaɪz/','使杂交、杂化；混合不同来源',
 'hybrid 是混合体，hybridize 是让混合发生。可以育种，也可以把不同设计传统结合。',
 'hybrid + -ize。生物学说杂交，化学、分子生物学等说杂化时有各自专门定义，不能直接把所有过程说成动物交配。',H,
 'hybridize two varieties 让两个品种杂交，hybridize different styles 混合不同风格，hybridized materials 杂化材料。',
 'hybridize two varieties；hybridize different styles。',
 'hybridize 与普通 mix 有重叠，但常强调不同来源成分结合成新结构或后代；具体学科里的结构由上下文限定。',
 ('Researchers hybridized two varieties of the plant.','研究人员让这种植物的两个品种杂交。'),('The designer hybridized traditional forms with digital techniques.','设计师把传统形式与数字技术结合起来。'))
W('hybridization','英 /ˌhaɪbrɪdaɪˈzeɪʃən/；美 /ˌhaɪbrədəˈzeɪʃən/','杂交；杂化；不同来源结合的过程',
 '关注两个原本不同的来源怎样结合：育种中产生后代，其他学科中形成某种混合关系。',
 'hybridize + -ation，或按 hybrid + -ization 识别。技术名词不能仅凭后缀推成同一套物理、生物过程。',H,
 'plant hybridization 植物杂交，cultural hybridization 文化混合，orbital hybridization 轨道杂化，DNA hybridization 核酸杂交。',
 'plant hybridization；cultural hybridization；orbital hybridization。',
 '核酸杂交说互补链配对，轨道杂化说数学模型中的轨道组合，二者不等于育种。共同构词感觉是结合，不是操作步骤相同。',
 ('The chapter describes hybridization between related plant varieties.','这一章描述相近植物品种之间的杂交。'),('The essay explores cultural hybridization in the city.','文章探讨城市中的文化混合。'))
Q=[['拉丁 ratio → rationalis → 法语、英语 rational','推理、计算、比率 → 理性的；可写成比率的'],['法语 rationaliser / rationalisation 等 → 英语相应词','使有条理、提高效率；为行为找合理说辞']]
W('rational','/ˈræʃənəl/','理性的、合理的；有理数的〔数学〕',
 '判断沿着理由、证据和推理走，而不是只被一时冲动推着走；数学里又抓能写成整数之比。',
 '经法语、拉丁 rationalis 接 ratio 推理、计算、比率。现代不能只从 ration 配给口粮的字面推断，虽然它们远处有词族联系。',Q,
 'a rational decision 理性决定，a rational explanation 合理解释，rational thought 理性思考，a rational number 有理数。',
 'a rational decision；a rational explanation；rational thought；a rational number。',
 'rational 不自动等于 morally right 道德上正确：推理可服务于不同目标。rational number 可写成两个整数之比，分母不能为零。',
 ('We need a rational explanation for the change.','我们需要对这个变化作合理解释。'),('One half is a rational number.','二分之一是有理数。'))
W('rationalize','/ˈræʃənəlaɪz/','使合理、有条理；调整以提高效率；为行为找借口；使有理化',
 '把流程理顺可能是真改善；把自己不光彩的决定包装成合理选择，则是另一种 rationalize。',
 '借法语 rationaliser，现代对应 rational + -ize。不能因为后缀说使成为，就认定每次 rationalize 都真使判断更理性。',Q,
 'rationalize production 整理生产流程提高效率，rationalize a decision 为决定找合理说辞，rationalize the denominator 使分母有理化。',
 'rationalize production；rationalize a decision；rationalize the denominator。',
 'rationalize 借口义常带自我辩护、遮掩真实动机；justify 更广说证明或说明正当，但也可能被批评。组织调整义不必等于裁员。',
 ('The company rationalized its ordering system to reduce duplicated work.','公司理顺了订货系统，减少重复工作。'),('He tried to rationalize the mistake instead of admitting it.','他试图给错误找理由，而不是承认它。'))
W('rationalization','英 /ˌræʃənəlaɪˈzeɪʃən/；美 /ˌræʃənələˈzeɪʃən/','合理化、整合以提高效率；自圆其说、为行为找理由；有理化',
 '同样叫合理化，可能是流程真的更顺，也可能只是把理由讲得更顺；看原本问题有没有被面对。',
 '接法语 rationalisation，现代对应 rationalize + -ation，或 rational + -ization。英式常见 rationalisation。',Q+[['rationalize → rationalization','改造流程、整理理由或数学有理化的过程']],
 'industrial rationalization 工业整合增效，a rationalization for failure 为失败作的辩解，rationalization of the denominator 分母有理化。',
 'industrial rationalization；a rationalization for；rationalization of the denominator。',
 'rationalization 是借口时，不保证理由真实；效率调整时也不一定指思想辩解。词形相同，使用对象让意思分开。',
 ('The merger was presented as a rationalization of services.','合并被说成是对服务的整合增效。'),('Her explanation sounded more like a rationalization than an honest account.','她的解释听着更像自我辩解，而非坦诚交代。'))
M=[['拉丁 margo/margin- → marginālis → marginal','边、边缘 → 边缘的、差距很小的'],['marginal + -ize → marginalize','让人或事退到边缘、失去重要位置'],['marginalize + -ation → marginalization','被排除、失去参与和发声空间的过程']]
W('marginal','英 /ˈmɑːdʒɪnəl/；美 /ˈmɑːrdʒɪnəl/','边缘的；很小的、勉强的；边际的〔专门义〕',
 '页边、群体边缘是位置；刚过一点线是程度；经济里的 marginal 则常问再增加一单位会多出什么。',
 '借中世纪拉丁 marginālis，现代对应 margin + -al。不同义都与边缘、差额有关，但不能全译成不重要。',M[:1]+[['英语 marginal 的程度、专门用法','小幅、接近底线；经济中再增加一单位所带来的变化']],
 'marginal notes 页边注，a marginal improvement 小幅改善，marginal land 勉强适宜耕作的土地，marginal cost 边际成本。',
 'marginal notes；a marginal improvement；marginal land；marginal cost。',
 'marginal cost 指增加一单位产出带来的额外成本，不是微不足道的成本；a marginal improvement 才通常说改善幅度小。',
 ('The new design offers only a marginal improvement.','新设计只带来小幅改善。'),('She added marginal notes beside the passage.','她在那段文字旁加了页边注。'))
W('marginalize','英 /ˈmɑːdʒɪnəlaɪz/；美 /ˈmɑːrdʒɪnəlaɪz/','使边缘化、排挤到次要位置',
 '人还在会议室，却总轮不到他说话；议题还在文件里，却被挤到无人处理的角落。这是影响力和参与空间被推到边上。',
 'marginal + -ize，使处于边缘。常说社会群体、观点、议题被削弱地位；统计学另有取边缘分布的专门义。',M,
 'marginalize a community 使一个群体边缘化，marginalized voices 被忽视的声音，marginalize an issue 把议题挤到次要位置。',
 'marginalize a community；marginalized voices；marginalize an issue。',
 'marginalize 不一定把人赶走，剥夺参与、重视、资源也可形成边缘化；marginal improvement 小幅改善不能照成边缘化改善。',
 ('The new process risks marginalizing smaller organizations.','新流程可能让较小机构更难参与、被挤到边缘。'),('Her concerns were marginalized during the discussion.','讨论中，她关心的问题被搁到了次要位置。'))
W('marginalization','英 /ˌmɑːdʒɪnəlaɪˈzeɪʃən/；美 /ˌmɑːrdʒɪnələˈzeɪʃən/','边缘化、被排斥到次要位置的过程或状态',
 '把人不断挤出重要的参与、资源和注意范围；不是一句边缘人物标签，而是怎样失去位置的过程。',
 'marginalize + -ation，也可按 marginal + -ization 识别。英式变体 marginalisation。',M,
 'social marginalization 社会边缘化，political marginalization 政治边缘化，the marginalization of local voices 地方声音被忽视、排除。',
 'social marginalization；political marginalization；the marginalization of。',
 'marginalization 不只是住在城市边缘；住中心也可能没有参与机会。它与 physical distance 空间距离不能画等号。',
 ('The study examines the social marginalization of older residents.','研究考察年长居民的社会边缘化。'),('The consultation aimed to prevent the marginalization of local voices.','协商旨在避免地方声音被排除在重要讨论之外。'))
N=[['中世纪拉丁 minera/minerale → 法语 mineral → mineral','矿石、矿物相关名称'],['mineral + -ize → mineralize','形成、沉积矿物质；转成无机形态等领域用法'],['mineralize + -ation → mineralization','矿化过程，具体变化按对象解释']]
W('mineral','/ˈmɪnərəl/','矿物；矿物质〔营养等语境〕；矿物的',
 '地质里是一类有自身成分和结构的自然物质；营养里则常指身体需要的钙、铁等无机元素，不是叫人去吃一块石头。',
 '经法语、中世纪拉丁矿石相关形式借入。不要把 min- 强拆成小；mineral 的核心与矿物来源、无机材料相连。',N[:1]+[['英语 mineral','地质矿物；营养所说无机营养元素等']],
 'quartz and other minerals 石英等矿物，mineral deposits 矿藏，vitamins and minerals 维生素和矿物质，mineral water 矿泉水。',
 'mineral deposits；vitamins and minerals；mineral water。',
 'rock 岩石与 mineral 矿物不是同一层概念，一块岩石可含多种矿物。营养 minerals 也不等于整块地质标本。',
 ('The collection includes quartz and several other minerals.','收藏里有石英和几种其他矿物。'),('The label lists vitamins and minerals.','标签列出了维生素和矿物质。'))
W('mineralize','/ˈmɪnərəlaɪz/','使矿化、形成或沉积矿物质；转成无机形态',
 '关键不是把东西塞进矿山，而是成分、结构进入矿物或无机形态；骨组织形成矿物部分，土壤有机养分转无机形态，方向各有专义。',
 'mineral + -ize，后缀给使成为、形成或赋予相关性质的方向。具体学科定义不靠一个中文矿化包办。',N,
 'mineralize bone 使骨组织矿化，mineralize organic nutrients 使有机养分转为无机形态，mineralized remains 矿化遗存。',
 'mineralized tissue；mineralize organic nutrients；mineralized remains。',
 'mineralize 不等于开矿 mine，也不等于把东西越做越小。土壤用法常关注有机养分变为无机形态，不要求形成石块。',
 ('The study tracks how the tissue begins to mineralize.','研究跟踪组织怎样开始矿化。'),('Soil microbes help mineralize organic nutrients.','土壤微生物帮助有机养分转成无机形态。'),sources=['https://en.wiktionary.org/wiki/mineralize#English','https://www.nrcs.usda.gov/sites/default/files/2022-10/National-Agronomy-Manual.pdf'])
W('mineralization','英 /ˌmɪnərəlaɪˈzeɪʃən/；美 /ˌmɪnərələˈzeɪʃən/','矿化、矿物质形成或沉积；有机物向无机形态转化〔依领域〕',
 '同名过程不一定长成同样的东西：土壤里释放无机养分，骨组织形成矿物部分，遗存被矿物填充或替代，各有对象。',
 'mineralize + -ation，也可按 mineral + -ization 识别。不要只因后缀相同，就以为所有领域的矿化是同一具体机制。',N,
 'soil mineralization 土壤矿化，bone mineralization 骨矿化，mineralization of organic matter 有机物矿化。',
 'soil mineralization；bone mineralization；mineralization of organic matter。',
 '土壤 mineralization 常指有机养分转成无机形态；矿床形成、组织矿物沉积等义又不同。翻译时要把过程对象保留下来。',
 ('Temperature affects the rate of mineralization in the soil.','温度会影响土壤中的矿化速率。'),('The diagram shows mineralization during bone formation.','图示展示了骨形成过程中的矿化。'),sources=['https://en.wiktionary.org/wiki/mineralization#English','https://www.nrcs.usda.gov/sites/default/files/2022-10/National-Agronomy-Manual.pdf'])
T=[['拉丁 minium → miniare → 意大利语 miniatura','红色颜料 → 手稿着色、彩绘'],['英语 miniature','小幅画、缩小作品 → 微型的'],['miniature + -ize / -ization','把设备等做小；小型化过程']]
W('miniature','英 /ˈmɪnɪtʃə/；美 /ˈmɪniətʃər/','微型的、小型的；缩小模型、小幅肖像画',
 '一座能放在桌上的城堡，是 miniature castle。它的历史起点却不是小，而是手稿彩绘：小幅画、精细小作品逐渐把名字带向尺寸。',
 '借意大利语 miniatura 手稿彩绘、小幅画，远接拉丁 miniare 涂红色、minium 红色颜料。小的意义还可能受 minor、minimum 等近音词影响；不是原本 mini + ature。',T[:2],
 'a miniature model 微缩模型，a miniature portrait 小幅肖像，in miniature 以缩小形式，miniature furniture 微型家具。',
 'a miniature model；a miniature portrait；in miniature。',
 'miniature 原始词源不等于 minimum 最小值；现代 mini- 反而从 miniature 等材料中抽出。微型模型也不保证内部功能完整。',
 ('The museum displayed a miniature of the old town.','博物馆展出了一座老城微缩模型。'),('The necklace contained a miniature portrait.','项链里嵌着一幅小肖像。'),sources=['https://en.wiktionary.org/wiki/miniature#English','https://www.etymonline.com/word/miniature'])
W('miniaturize','/ˈmɪnətʃəraɪz/','使小型化、微型化',
 '把原来占一大块地方的设备做得更小；常希望保留主要用途，而不只是把一张照片缩小。',
 'miniature 去 e + -ize，形成使成微型的动词；不是随意给 mini 后面接一大串没有意义的字母。英式也写 miniaturise。',T,
 'miniaturize electronic components 使电子元件小型化，miniaturize a device 使设备微型化，miniaturized equipment 微型化设备。',
 'miniaturize components；miniaturize a device；miniaturized equipment。',
 'miniaturize 说尺寸减小，不保证重量、价格、功耗都同时降低；缩小之后的功能取舍要另看。',
 ('Engineers miniaturized the sensor for use in a portable device.','工程师把传感器做小，装进便携设备。'),('The project aims to miniaturize the existing equipment.','项目旨在让现有设备小型化。'),sources=['https://en.wiktionary.org/wiki/miniaturize#English','https://www.oxfordlearnersdictionaries.com/definition/english/miniaturize'])
W('miniaturization','/ˌmɪnətʃəraɪˈzeɪʃən/','小型化、微型化；小型化成果',
 '把做小这件事当作技术过程：以前一柜子的东西，后来能装进手掌大小的设备。',
 'miniaturize + -ation，保留 miniatur- 词干；也可按 miniature + -ization 识别，去末尾 e。',T,
 'the miniaturization of electronics 电子设备小型化，advances in miniaturization 小型化技术进展，component miniaturization 元件小型化。',
 'the miniaturization of；advances in miniaturization；component miniaturization。',
 'miniaturization 不等于把功能随便砍掉；也不等于 minimum 数学最小值。是否保留功能、达到多小，由具体设计决定。',
 ('Miniaturization made the instrument easier to carry.','小型化让仪器更便于携带。'),('The article traces the miniaturization of electronic components.','文章追述电子元件的小型化。'))
E=[['希腊 daímōn → 拉丁 daemon/demon → 英语 demon','神灵、守护灵等 → 英语常见恶魔义'],['demonize 与相应拉丁形式','使成恶魔、说成邪恶'],['demonization','把人、群体等描绘成恶魔般邪恶的过程']]
W('demon','/ˈdiːmən/','恶魔；内心困扰、恐惧；某方面厉害的人〔比喻〕',
 '故事里是恶灵；fight your demons 中常是与内心阴影、困扰斗争，不要求真有一只鬼站在身边。',
 '经拉丁接希腊 daímōn，旧希腊语可以指神灵、守护力量等，不是一开始只等于邪恶。英语主流恶魔义受后来的宗教、文化使用塑形。',E[:1]+[['英语 demon 的常见比喻','困扰人的内在力量；或精力、技能特别突出者']],
 'a demon in a story 故事中的恶魔，inner demons 内心困扰，a speed demon 飞车狂、速度狂，a demon at chess 下棋很厉害的人〔口语〕。',
 'inner demons；fight one’s demons；a speed demon；a demon at chess。',
 'demon 比喻可以负面，也可夸某方面厉害；计算机 daemon 后台进程是相关词源下的专门拼法，不把软件自动当恶魔。',
 ('A demon guards the gate in the story.','故事里有个恶魔守着大门。'),('The memoir describes his struggle with inner demons.','回忆录描述了他与内心困扰的斗争。'))
W('demonize','/ˈdiːmənaɪz/','把……妖魔化、描述成邪恶',
 '不是认真讨论做错了哪件事，而是把对方整个人画成恶魔，让人先害怕、憎恨，再不愿听他的理由。',
 '现代对应 demon + -ize，历史也接中世纪拉丁 daemonizō 等形式。旧义可涉及成为或受恶魔影响，现代修辞常说将人描绘为邪恶。',E,
 'demonize opponents 妖魔化对手，demonize a group 妖魔化某群体，demonize technology 把技术描述成万恶来源。',
 'demonize opponents；demonize a group；demonize technology。',
 'demonize 常批评失衡、夸大的邪恶描写，不等于所有 criticize 批评；反对妖魔化也不表示不能指出具体错误。',
 ('The article warns against demonizing people who disagree.','文章提醒不要把意见不同的人妖魔化。'),('The film demonizes the rival without exploring his motives.','电影把对手描绘成恶人，却没有探究他的动机。'))
W('demonization','英 /ˌdiːmənaɪˈzeɪʃən/；美 /ˌdiːmənəˈzeɪʃən/','妖魔化，把对象塑造成邪恶形象',
 '把单个缺点或分歧，扩大成这个群体、人物全都邪恶的整体画像；demonization 是这套塑造过程。',
 'demonize + -ation，或按 demon + -ization 识别。英式也常写 demonisation，常用于评论宣传、公共争论等。',E,
 'the demonization of opponents 对对手的妖魔化，public demonization 公开妖魔化，resist demonization 反对妖魔化描写。',
 'the demonization of；public demonization；resist demonization。',
 '说某种描述是 demonization，是在批评其偏颇，不证明被描述者从未做错；要继续看具体证据和指控。',
 ('The essay examines the demonization of outsiders.','文章考察外来者怎样被妖魔化。'),('She distinguished careful criticism from demonization.','她区分了审慎批评与妖魔化。'))
W('formalization','英 /ˌfɔːməlaɪˈzeɪʃən/；美 /ˌfɔːrmələˈzeɪʃən/','正式确立；形式化、明确化',
 '原来只是口头默契，现在写成明确规则，是正式确立；原来凭直觉说，现在用清楚符号和步骤表达，是形式化。',
 'formalize + -ation，也可按 formal + -ization 看结构。formal 的正式与形式两支会让名词在制度、数学等场景落到不同含义。',
 [['formal → formalize','正式的、形式的 → 正式确立、用明确形式表达'],['formalize + -ation → formalization','上述确立、表达的过程或成果']],
 'the formalization of an agreement 协议正式确立，the formalization of a theory 理论的形式化，formalization of procedures 流程明确化。',
 'the formalization of an agreement；the formalization of a theory。',
 'formalization 不等于空走形式的 formalism 在所有语境用法；数学形式化是明确结构，不是把公式排得漂亮就算完成。',
 ('The document marked the formalization of their partnership.','文件标志着双方合作关系正式确立。'),('The paper presents a formalization of the verbal argument.','论文把口头论证作了形式化表达。'))
V=[['novel 小说 + -ize → novelize','把已有材料写成小说'],['novelize + -ation → novelization','小说改写过程及其成书作品']]
W('novelize','英 /ˈnɒvəlaɪz/；美 /ˈnɑːvəlaɪz/','把……改写成小说、小说化',
 '原来是电影、剧本或真实事件，把它展开为叙述、人物心理和场景文字，写成长篇小说。',
 'novel 取小说名词义 + -ize，不是取新奇的形容词就一律译创新。更远小说名词与新故事有关，现代直接构词仍看小说这一义。',V,
 'novelize a film 把电影改写成小说，novelize a screenplay 将剧本小说化，novelize historical events 把历史事件写成小说。',
 'novelize a film；novelize a screenplay；novelize historical events。',
 'novelize 常从其他材料变成小说；把小说拍成电影是 adapt a novel for film，方向相反。',
 ('She was hired to novelize the screenplay.','她受聘把剧本改写成小说。'),('The author novelized a series of historical events.','作者把一系列历史事件写成了小说。'))
W('novelization','英 /ˌnɒvəlaɪˈzeɪʃən/；美 /ˌnɑːvələˈzeɪʃən/','小说化改写；由电影、剧本等改写的小说',
 '不仅能说改写这件事，也能拿起一本书说：这是那部电影的小说版。',
 'novelize + -ation，形成过程、结果名词。英式也常写 novelisation；不是每一本 novel 小说都必须先有别的媒体版本。',V,
 'a novelization of the film 电影的小说版，an official novelization 官方小说改编版，screenplay novelization 剧本小说化。',
 'a novelization of；an official novelization；screenplay novelization。',
 'novelization 的改编方向常是影像、剧本等到小说；film adaptation of a novel 则从小说到电影，别把方向颠倒。',
 ('I read the novelization after watching the film.','看完电影后，我读了它的小说改编版。'),('The novelization adds scenes that are not in the screenplay.','小说改编版增加了剧本里没有的场景。'))
R('A1927','把使成为、发生变化的动词转为过程、结果名词','-IZATION：某种变化发生了，这件事叫一个名词','sterile → sterilize → sterilization；marginal → marginalize → marginalization；miniature → miniaturize → miniaturization。',
 '尾巴只提示过程或结果，不能代替核心解释：有的是灭菌，有的是把人挤到边缘，有的是把设备做小。还有一些词连同法语名词整体借入，现代可拆不表示英语动词一定先出现。',
 '-ize 的希腊、拉丁、法语等构词传统，与 -ation 动作名词词尾结合成 -ization；英式常有 -isation 变体。动词末尾 e 通常去掉。',
 [['无菌、免疫与混合来源','sterile · sterilize · sterilization · immune · immunize · immunization · hybrid · hybridize · hybridization'],['理性、效率与边缘位置','rational · rationalize · rationalization · marginal · marginalize · marginalization'],['材料与尺寸变化','mineral · mineralize · mineralization · miniature · miniaturize · miniaturization · crystallization · vaporization · pressurization'],['形象、规则与文本改写','demon · demonize · demonization · formalize · formalization · novel · novelize · novelization'],['社会、制度和个人变化','civilization · socialization · industrialization · commercialization · liberalization · democratization · nationalization · unionization · internationalization · institutionalization · collectivization · centralization · polarization · radicalization · victimization · dehumanization · sexualization · westernization'],['归类、组织与技术变化','generalization · normalization · criminalization · randomization · regularization · internalization · virtualization · digitalization · popularization · familiarization · periodization']],
 '-ization 不等于所有现代英语都是临时加尾巴；rationalization 可是找借口；marginalization 不只空间边缘；miniature 词源是手稿彩绘一路；novelization 的改写方向要分清。',
 'The report discusses miniaturization, not the marginalization of the people doing the work.\n\n报告讨论的是设备小型化，不是把工作人员挤到边缘。',
 'sterile sterilize sterilization immune immunize immunization hybrid hybridize hybridization rational rationalize rationalization marginal marginalize marginalization mineral mineralize mineralization miniature miniaturize miniaturization demon demonize demonization formalize formalization novel novelize novelization civilization polarization generalization industrialization socialization normalization commercialization liberalization victimization virtualization democratization nationalization centralization crystallization radicalization unionization internationalization criminalization randomization institutionalization dehumanization internalization pressurization collectivization regularization vaporization popularization sexualization westernization digitalization familiarization periodization')
if __name__=='__main__':save('continuation_20261030_ie',ROOTS,WORDS)
