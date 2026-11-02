"""Temper, ritual, recording, volcanoes and Latin endings."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
T=[['拉丁 temperare 调和、适度调节 → 古英语 temprian → temper','把各种成分、性质调到合适程度'],['材料状态、人的性情 → temper','材料经处理的性质；心境、脾气，后来常偏向怒气']]
W('temper','英 /ˈtempə/；美 /ˈtempər/','脾气、情绪；调和、缓和；给材料作调质、回火等处理',
 '把过强的东西调到合适程度，是 temper 的动词核心。人的 temper 则像各种性情混合后的状态，日常常指容易发作的脾气。',
 '接拉丁 temperare 按适当比例混合、节制，经古英语 temprian 等到英语。与 tempus 等更远联系有讨论，先抓调和、适度的可靠近义。',T,
 'lose one’s temper 发脾气，keep one’s temper 忍住脾气，temper enthusiasm with caution 用谨慎调和热情，temper steel 给钢作回火处理。',
 'lose one’s temper；keep one’s temper；temper ... with ...。',
 'temper 可以名词脾气，也可以动词缓和；材料处理看具体工艺，并不把所有 temper 都统一当淬火。',
 ('He lost his temper when the door jammed again.','门又卡住时，他发了脾气。'),('Her optimism was tempered by experience.','经历让她的乐观多了一份克制。'),sources=['https://en.wiktionary.org/wiki/temper#English','https://www.etymonline.com/word/temper'])
W('tempered','英 /ˈtempəd/；美 /ˈtempərd/','经过调节、处理的；缓和了的；具有某种脾气的',
 '一种力量被另一种因素拉回平衡，是 tempered；玻璃、金属经过特定处理，也用同一个词说状态。放进脾气组合时则描述人的性情。',
 'temper + -ed，末尾读 /d/，古英语已有相应分词。承调节、材料处理及性情各支；钢的回火与玻璃的钢化并非相同工艺。',T+[ ['temper + -ed → tempered','调节、处理完成的状态；带某种性情'] ],
 'tempered glass 钢化玻璃，tempered steel 回火钢，enthusiasm tempered by caution 被谨慎调和的热情；good-tempered 脾气好属常见组合。',
 'tempered glass；be tempered by experience。',
 'tempered glass 习惯译钢化玻璃，tempered steel 通常看回火等工艺；不按同一个中文动词包办。',
 ('The door has a panel of tempered glass.','这扇门嵌着一块钢化玻璃。'),('Their excitement was tempered by uncertainty.','不确定性使他们的兴奋多了一点克制。'))
W('temperance','英 /ˈtempərəns/；美 /ˈtempərəns/','节制、适度；节酒、禁酒运动相关的节制',
 '有欲望、有冲动，但把它控制在适当范围，便是 temperance。历史上谈 temperance movement 时，通常特别落在饮酒节制、禁酒倡议。',
 '经盎格鲁诺曼语 temperance 接拉丁 temperantia 节制，后者接 temperare 调节的分词词干。现代可看 temper + -ance 的性质联系。',T[:1]+[['temperantia → temperance','自我节制；饮酒节制、禁酒语境']],
 'the virtue of temperance 节制这一品德，the temperance movement 节酒、禁酒运动。',
 'temperance in eating；the temperance movement。',
 'temperance 泛义是节制；历史运动具体有主张少喝或完全禁酒的不同用法，读背景再决定中文。',
 ('The essay praises temperance in eating and spending.','文章赞扬饮食和花费上的节制。'),('The museum documents the history of the temperance movement.','博物馆记录了节酒与禁酒运动的历史。'))
R('B4460','调到适当程度，连接材料状态、性情与自我节制','TEMPER：太过了就调一调，性情与材料各有状态','temper → tempered；temperance 节制。',
 '乐观被经验调和，是情绪；钢、玻璃经处理，是材料；节制欲望，是行为。词族能串联，但具体工艺和历史运动仍按对象解释。',
 'temperare → temprian → temper；-ed 状态；temperantia → temperance，节制性质名。',
 [['调节、状态与节制','temper · tempered · temperance']],
 'tempered glass 与 tempered steel 具体工艺不同；temperance movement 要读饮酒历史背景。',
 'Experience tempered his enthusiasm and taught him temperance.\n\n经历让他的热情多了克制，也教会他节制。','temper tempered temperance')
Ri=[['拉丁 ritus 仪式 → ritualis','与仪式有关的'],['ritualis → ritual → ritually','仪式、固定程序；按仪式、习惯性地']]
W('ritual','/ˈrɪtʃuəl/','仪式、仪式化程序；仪式的',
 '按固定顺序做一套动作，并赋予意义，是 ritual。宗教典礼常见，早上磨豆、泡咖啡的一套个人程序也可以被亲切叫作 ritual。',
 '接拉丁 ritualis 仪式的，来自 ritus 仪式 + -alis。英语先有形容词，再用作仪式、固定动作程序的名词等。',Ri,
 'a religious ritual 宗教仪式，a daily ritual 每日固定程序，ritual objects 仪式用品。',
 'a daily ritual；perform a ritual；ritual practices。',
 'habit 可以是随手形成的习惯；ritual 更突出一套固定程序及其象征、情感意义。日常用法可重叠。',
 ('Making coffee had become his morning ritual.','煮咖啡成了他每天早上的固定仪式。'),('The objects were used in a religious ritual.','这些物品曾用于宗教仪式。'))
W('ritually','/ˈrɪtʃuəli/','依照仪式地；仪式性地；照例地',
 'ritual 是一套仪式，ritually 就说明动作按这套规定、传统来做。也能形容某种每次都重复的程序。',
 'ritual + -ly，-al + -ly 形成 -ally；由仪式的性质转为方式副词。',Ri[:1]+[['ritual + -ly → ritually','按仪式规定、重复程序进行']],
 'ritually wash 按仪式洗濯，ritually significant 有仪式意义的。',
 'ritually significant；ritually prepared。',
 'ritually 描述仪式背景；physically、hygienically 等说不同考察方面，不能相互替代。',
 ('Participants ritually washed their hands before entering.','参与者进入前按仪式洗手。'),('The doorway was ritually significant to the community.','这道门对该群体具有仪式意义。'))
R('B3844','一套按顺序执行、带意义的动作','RITUAL：程序反复做，也被赋予一种意义','ritual → ritually；ritualistic 强调仪式化特点。',
 '宗教典礼与晨间咖啡都能提供画面，具体意义、庄重程度不同。副词说怎样执行，ritualistic 则说行为带有仪式化特点。',
 'ritus → ritualis → ritual；-ly 方式；-istic 性质。',
 [['仪式、方式与仪式化性质','ritual · ritually · ritualistic']],
 'ritual 比普通 habit 更容易突出固定程序、意义；日常使用不必都是宗教。',
 'The ritual was performed in a ritually significant place.\n\n这套仪式在一个具有仪式意义的地点举行。','ritual ritually ritualistic')
Gr=[['希腊 graphein 写、描画 → -graphia → -graphy','写下、画出、记录、描述的活动及成果'],['后续学科、技术与作品集合','图像符号、历史写作、录像、射线成像、血管成像等']]
W('iconography','英 /ˌaɪkəˈnɒɡrəfi/；美 /ˌaɪkəˈnɑːɡrəfi/','图像学；一套象征图像、图像符号',
 '一幅画里的光环、钥匙、颜色为何代表某个人物或主题？iconography 研究、描述这套图像语言，也可直接指那套符号。',
 'icono- 图像，接希腊 eikon + -graphy 描述、记录。传统艺术、宗教图像中常见，后来也描述其他文化的视觉符号。',Gr[:1]+[['icono- + -graphy → iconography','图像的描述、研究及象征体系']],
 'religious iconography 宗教图像符号、图像学，the iconography of a painting 画作的象征图像。',
 'religious iconography；the iconography of the painting。',
 'iconography 重图像主题、符号及其含义；photography 摄影重成像、拍摄，两者研究对象和活动不同。',
 ('The guide explained the iconography of the altar painting.','讲解员解释了祭坛画里的象征图像。'),('The designer borrowed from the iconography of early space travel.','设计师借用了早期太空旅行的一套视觉符号。'))
W('historiography','英 /hɪˌstɒriˈɒɡrəfi/；美 /hɪˌstɔːriˈɑːɡrəfi/','历史编纂；史学史、历史书写研究',
 'history 可以问过去发生了什么；historiography 再问：后来的人怎样选史料、讲这段过去，为什么讲法变了？',
 '经中世纪拉丁语接希腊 historiographia，historia 叙事、历史 + -graphia 写作。既指历史书写，也指研究历代历史写法、方法。',Gr[:1]+[['historia + -graphia → historiographia → historiography','历史编写；对历史编写的研究']],
 'the historiography of an event 某事件的历史书写、研究史，modern historiography 现代史学、历史编纂。',
 'modern historiography；the historiography of the revolution。',
 'historiography 不是把 history 再写得更长；重点常在历史是怎样被研究、解释、写出来的。',
 ('The course compares the historiography of the revolution across different periods.','课程比较不同时期怎样书写这场革命。'),('Her essay examines how new archives changed the historiography of the war.','她的文章考察新档案怎样改变了这场战争的历史研究与书写。'),sources=['https://en.wiktionary.org/wiki/historiography#English','https://www.oxfordlearnersdictionaries.com/us/definition/english/historiography','https://history.berkeley.edu/sites/default/files/reading_historiography.pdf'])
W('videography','英 /ˌvɪdiˈɒɡrəfi/；美 /ˌvɪdiˈɑːɡrəfi/','摄像、录像制作；录像作品目录',
 '用移动影像记录、讲述，拍摄并处理视频，是 videography 的工作画面。放在艺人资料里，也可能是一份视频作品清单。',
 'video- 视频、录像 + -graphy 记录、相关制作或作品集合，现代混合构词。video 来自拉丁 videre 看这一词族。',Gr[:1]+[['video- + -graphy → videography','录像制作；特定语境中的录像作品目录']],
 'wedding videography 婚礼摄像，videography services 视频拍摄制作服务，an artist’s videography 艺人视频作品目录。',
 'wedding videography；documentary videography。',
 'videography 通常看视频拍摄制作，photography 通常看静态照片；实际从业工作可以重叠。',
 ('She offers wedding videography services.','她提供婚礼摄像服务。'),('His videography includes several music videos.','他的视频作品目录包括几部音乐录像。'))
W('radiography','英 /ˌreɪdiˈɒɡrəfi/；美 /ˌreɪdiˈɑːɡrəfi/','射线照相、放射摄影',
 '用射线穿过物体，不同部分留下不同影像，就是 radiography 的基本画面。医院能检查身体，工业也能看材料内部。',
 'radio- 射线、辐射 + -graphy 记录、成像，现代科学构词。这里 radio- 接射线义，不是广播节目。',Gr[:1]+[['radio- + -graphy → radiography','用射线产生影像']],
 'industrial radiography 工业射线照相，digital radiography 数字放射摄影，chest radiography 胸部放射摄影。',
 'digital radiography；industrial radiography。',
 'radiography 是一种成像过程；radiology 放射学范围更广，不只这个词命名的单一技术。',
 ('Industrial radiography revealed a defect inside the component.','工业射线照相显出了零件内部的缺陷。'),('The department uses digital radiography.','这个科室使用数字放射摄影。'))
W('angiography','英 /ˌændʒiˈɒɡrəfi/；美 /ˌændʒiˈɑːɡrəfi/','血管造影、血管成像',
 '把体内血管的走向、形态显示出来，像为隐藏的管道画路网，就是 angiography。angio- 指血管，-graphy 指成像记录。',
 'angio- 接希腊 angeion 容器，科学用法指血管 + -graphy 成像、记录。现代具体可见导管、CT、MR 等不同血管成像方式。',Gr[:1]+[['angio- + -graphy → angiography','血管成像、造影']],
 'coronary angiography 冠状动脉造影，CT angiography CT 血管成像，MR angiography 磁共振血管成像。',
 'coronary angiography；CT angiography；MR angiography。',
 'angiography 不是只给一个固定器械起名；具体技术及是否使用造影剂等看完整检查名称和方案。',
 ('The article compares CT angiography with MR angiography.','文章比较了 CT 血管成像与磁共振血管成像。'),('The angiography images showed the course of the blood vessels.','血管成像显示了血管的走行。'),sources=['https://en.wiktionary.org/wiki/angiography#English','https://www.nhs.uk/tests-and-treatments/angiography/'])
R('A1925','写、画、记录，扩展到描述学科、成像技术和作品目录','-GRAPHY：把信息写下、画出或留下记录','iconography 看图像符号；historiography 看历史书写；videography 看视频；radiography 看射线影像。',
 '有的词重研究，有的重记录技术，有的重作品集合。先问“前半是什么信息，后半怎样把它表现出来”，再读成熟的领域用法。',
 'graphein 写、画 → -graphia → -graphy；与不同对象、技术的组合成分相接。',
 [['影像、声音与作品目录','cinematography · videography · filmography · sonography'],['人群、历史、文化与地图','demography · ethnography · historiography · iconography · cartography'],['海洋、地层及晶体结构','oceanography · stratigraphy · crystallography'],['记录、书写与保密','orthography · telegraphy · cryptography'],['身体成像技术','tomography · mammography · radiography · angiography']],
 '-graphy 不必全译成学；filmography 是作品目录，angiography 是血管成像过程。',
 'The exhibition combines photography with videography and explains its religious iconography.\n\n展览结合照片与视频，也解释其中的宗教图像符号。',
 'cinematography videography filmography sonography demography ethnography historiography iconography cartography oceanography stratigraphy crystallography orthography telegraphy cryptography tomography mammography radiography angiography')
V=[['罗马火与金工神 Vulcanus → Vulcano 岛名','火山岛借神名命名'],['意大利 vulcano → volcano','岛名、火山相关名称成为普通火山名'],['volcan- + -ic、-ism','火山的；火山活动、作用']]
W('volcano','英 /vɒlˈkeɪnəʊ/；美 /vɑːlˈkeɪnoʊ/','火山',
 '地下熔融物、气体能沿通道到达地表，形成喷发和相关地形，这是 volcano 的画面。名字先经过一座火山岛，再成了普通名称。',
 '借自意大利 vulcano，联系意大利 Vulcano 岛，岛名接罗马火与金工神 Vulcanus。普通名由专名背景发展，不把它按英语小词硬拆。',V[:2],
 'an active volcano 活火山，volcano monitoring 火山监测，a volcanic eruption 火山喷发；复数 volcanoes、volcanos 均可见。',
 'an active volcano；a volcano erupts；volcano monitoring。',
 '火山不必正在喷发，也不全是典型尖锥山形；volcano 说火山系统、地形，eruption 才说一次喷发。',
 ('The island has an active volcano.','岛上有一座活火山。'),('Scientists monitor the volcano for changes.','科学家监测火山的变化。'),sources=['https://en.wiktionary.org/wiki/volcano#English','https://www.etymonline.com/word/volcano'])
W('volcanic','英 /vɒlˈkænɪk/；美 /vɑːlˈkænɪk/','火山的、火山形成的；爆发般猛烈的',
 '火山喷发留下岩石、灰和岛屿，这些可以 volcanic。人的愤怒一下爆开，也借火山爆发的形象说 volcanic anger。',
 '经法语 volcanique，或对应 volcano 去末尾 o + -ic；volcan- 是相应组合词干。重读元音与 volcano 不同。',V[:2]+[['volcan- + -ic／法语 volcanique → volcanic','火山相关的；借指爆发般的']],
 'volcanic rock 火山岩，volcanic ash 火山灰，volcanic activity 火山活动。',
 'volcanic rock；volcanic ash；volcanic activity。',
 'volcanic rock 是火成岩中的火山形成一类；不能把所有地下冷却形成的火成岩都叫火山岩。',
 ('The beach was covered with dark volcanic sand.','海滩铺满深色火山砂。'),('The report describes recent volcanic activity.','报告描述了近期火山活动。'))
W('volcanism','英 /ˈvɒlkənɪzəm/；美 /ˈvɑːlkənɪzəm/','火山作用、火山活动',
 '把火山形成、岩浆上升、喷发等相关自然过程合在一起谈，是 volcanism。-ism 在这里命名一类作用、现象。',
 '经法语 volcanisme，或对应 volcan(o) + -ism；与 volcano、volcanic 同族。',V[:2]+[['volcan- + -ism → volcanism','火山相关的自然活动、作用']],
 'the history of volcanism 火山活动史，volcanism on other planets 其他行星的火山作用。',
 'volcanism on the island；evidence of volcanism。',
 'volcanism 是总体活动、作用，an eruption 是一次喷发；-ism 不只表示思想主义。',
 ('The rocks preserve evidence of ancient volcanism.','这些岩石保留了古代火山作用的证据。'),('The lecture compared volcanism on Earth and Mars.','讲座比较了地球与火星的火山活动。'))
R('B4155','火神、火山岛的专名背景，再到普通火山与活动名称','VOLCAN-：地下力量涌上地表，物体、性质、过程各有词形','volcano → volcanic、volcanism。',
 '火山是物体、系统名称，火山岩是形成来源，火山作用是整体活动。神名与岛名解释借词历史，现代科学含义则按实际过程读。',
 'Vulcanus → Vulcano → 意大利 vulcano → volcano；volcan- + -ic、-ism。',
 [['火山、性质与作用','volcano · volcanic · volcanism']],
 'volcanism 不只一次喷发；volcanic 不包办所有地下形成的火成岩。',
 'The volcanic rocks record a long period of volcanism around the volcano.\n\n这些火山岩记录了火山周围长期的火山活动。','volcano volcanic volcanism')
Um=[['拉丁中性单数等语法形式保留在借词里','album、curriculum、medium 等各有具体原词结构'],['近代拉丁科学命名也使用 -um 等结尾','platinum 由西班牙语 platina 改造；不等于英语有万能 -um 单数规则']]
W('forum','英 /ˈfɔːrəm/；美 /ˈfɔːrəm/','论坛、讨论会；古罗马公共广场；网络论坛',
 '先有大家来往、交易、议事的公共广场，再有交换意见的场所。搬到网上，帖子与回复围成了一个 forum。',
 '借自拉丁 forum 公共场所、广场。-um 是拉丁原词形的一部分，英语整体借入；更远与外部、门等词族的联系有讨论。',Um[:1]+[['拉丁 forum 公共广场 → 英语 forum','讨论场所、会议；网络论坛']],
 'a public forum 公共讨论平台，an online forum 网络论坛，a forum for discussion 讨论场所。复数常 forums，也有拉丁式 fora。',
 'an online forum；a forum for debate；post on a forum。',
 'forum 强调讨论空间或组织起来的讨论；一个网站可以含论坛，但并非每个网站都是论坛。',
 ('She posted the question on an online forum.','她把问题发到了网络论坛。'),('The meeting provided a forum for residents to discuss the plan.','会议为居民讨论计划提供了场所。'))
W('datum','/ˈdeɪtəm/，也读 /ˈdætəm/','一项数据、已知事实；基准点、基准面',
 'data 一堆数据里单独拿出一项，可以叫 datum；测高程时先定一个共同参照面，这个参照也叫 datum。两者都像先放下一个用来推理、测量的依据。',
 '接拉丁 datum 给出的东西，是 dare 给的分词 datus 的中性单数名词用法；data 原是相应复数。英语保留该单项词及测量基准等专门义。',Um[:1]+[['dare 给 → datum 已给出的东西 → datum','作为依据的一项事实、数据；测量基准']],
 'a single datum 一项数据，a vertical datum 高程基准，a reference datum 参考基准。',
 'a single datum；a reference datum。',
 '现代 data 常按不可数集合名词使用，也有专业文体按复数；不必在普通英语里强行每次都换回 datum。',
 ('One datum was missing from the table.','表中缺少一项数据。'),('All heights were measured from the same datum.','所有高度都从同一个基准测起。'),sources=['https://en.wiktionary.org/wiki/datum#English','https://www.etymonline.com/word/datum'])
W('addendum','/əˈdendəm/','补遗、附加说明、补充文件',
 '正文写完了，还有一段需要加进去，就把它作为 addendum。名字本来就说“该加上的东西”。',
 '借自拉丁 addendum，是 addere 添加的动形词中性单数用法。ad- 朝向与 -dere 放、置的成分形成 addere；英语把整个形式用作补充内容名。',Um[:1]+[['addere 添加 → addendum 需要加上的东西 → addendum','文件、书籍的补遗、附加内容']],
 'an addendum to a report 报告补充说明，issue an addendum 发布补遗；复数常 addenda，也有 addendums。',
 'an addendum to；a short addendum。',
 'addendum 通常是对既有文本的补充；appendix 附录还可原本就是整体设计的一部分，两者有重叠。',
 ('The author added a short addendum to the report.','作者给报告加了一段简短补充。'),('The corrections appear in an addendum.','更正内容列在补遗里。'))
R('A1681','拉丁借词与近代科学名称保留的结尾','-UM：常是借入时留下的旧词形，先看整个词的历史','forum 讨论场所，datum 一项依据，addendum 该补上的内容；platinum 看近代元素命名。',
 '拉丁语里的语法结尾随着整个词进入英语，各词又按英语习惯发展。album、curriculum、medium 等并不因为同结尾就意义相同；科学名称的 -um 是另一种命名运用。',
 '拉丁原词形式 → 英语整体借入；datum／data、addendum／addenda 保留旧对举；forum 常复数 forums，album 常 albums。',
 [['讨论、依据与文件补充','forum · datum · addendum · memorandum'],['其他拉丁词形借入与学术用语','album · curriculum · medium · bacterium'],['近代元素名称的结尾','platinum']],
 '-um 不是英语通用单数后缀，也没有所有词都必须 -um 变 -a 的规则；逐词掌握通行复数。',
 'The forum discussed an addendum containing a missing datum.\n\n论坛讨论了一份补充文件，里面补入了缺失的一项数据。','forum datum addendum memorandum album curriculum medium bacterium platinum')
Mi=[['中世纪拉丁矿石相关词 → mineral','矿物、矿物的'],['mineral 一族 + -logist → mineralogist','研究矿物性质、结构、分类的人']]
W('mineralogist','英 /ˌmɪnəˈrælədʒɪst/；美 /ˌmɪnəˈrælədʒɪst/','矿物学家',
 '拿到一块标本，研究其中是什么矿物、晶体怎样排列、性质如何，这类专家是 mineralogist。重点在矿物本身。',
 'mineral 矿物 + -logist 研究某领域的人；与 mineralogy 矿物学相配。这里 -logist 是整组学科人物成分，不按普通 -ist 随意多拆一层。',Mi,
 'a mineralogist’s collection 矿物学家的收藏，a mineralogist examining a crystal 检查晶体的矿物学家。',
 'a mineralogist；a team of mineralogists。',
 'mineralogist 专门研究矿物；geologist 地质学家范围更广，两种身份可能重合。',
 ('The mineralogist examined the crystal under a microscope.','矿物学家在显微镜下观察晶体。'),('A mineralogist identified the minerals in the rock.','一位矿物学家鉴定了岩石中的矿物。'))
R('B4122','矿物名称，连接自然物质、形成作用和研究者','MINERAL：具体成分与结构的自然物，岩石可由它们组成','mineral → mineralization；mineralogist 是矿物学研究者。',
 '地质矿物看结构、成分，营养矿物质另有日常范围。形成、沉积等过程与专家人物名分别由后续成分命名。',
 'minera 等矿石词 → mineral；-ization 过程，-logist 研究者。',
 [['矿物、作用与研究者','mineral · mineralization · mineralogist']],
 '岩石与矿物不是同一层概念；营养矿物质也不是直接指一整块石头。',
 'The mineralogist studied mineralization in the region.\n\n矿物学家研究了该地区的矿化作用。','mineral mineralization mineralogist')
if __name__=='__main__':save('continuation_20261030_mz',ROOTS,WORDS)
