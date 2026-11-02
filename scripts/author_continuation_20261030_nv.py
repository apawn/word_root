"""Alcohol, hedges, greasers, merriment, recklessness, society, urinals and -ia."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()

Al=[['alcohol + -ic → alcoholic','含酒精、与酒精有关；还可涉及酒精依赖'],['non- + alcoholic → nonalcoholic','不含酒精，或不由相关酒精因素造成']]
W('nonalcoholic','英 /ˌnɒnælkəˈhɒlɪk/；美 /ˌnɑːnælkəˈhɔːlɪk/','无酒精的；非酒精所致的',
 '饮料菜单上用 nonalcoholic 把无酒精选择分出来。医学等文本里还可能是在否定酒精相关成因，前缀否定的范围要看后面的整体名称。',
 'non- 非、无 + alcoholic，形成否定性质形容词。alcoholic 自身有含酒精、酒精相关等义，否定形式随具体对象选择分支。',Al,
 'a nonalcoholic drink 无酒精饮料；nonalcoholic options 无酒精选择；nonalcoholic causes 非酒精相关成因。',
 'a nonalcoholic drink；nonalcoholic options。',
 'nonalcoholic drink 说饮料性质，an alcoholic 作人物名词则指有酒精依赖的人，不能把前者硬译成不是酒鬼的饮料。',
 ('The menu includes several nonalcoholic drinks.','菜单上有几种无酒精饮料。'),('She asked whether there was a nonalcoholic option.','她问有没有无酒精的选择。'),sources=['https://en.wiktionary.org/wiki/nonalcoholic#English','https://www.merriam-webster.com/dictionary/nonalcoholic'])
R('B3685','酒精相关性质与否定，人物名词义另看句法','ALCOHOLIC：说含酒精或酒精相关，non- 再否定','alcoholic → nonalcoholic，饮料、成因与人物名词分别识别。',
 '同一个 alcoholic 可以作形容词也可作人物名词。先看后面跟饮料还是独立指人，再认 non- 否定哪一层，避免逐字翻错。',
 'alcohol + -ic → alcoholic；non- + alcoholic → nonalcoholic。',
 [['酒精性质与否定','alcoholic · nonalcoholic']],
 'alcoholic beverage 谈饮料，an alcoholic 谈人物，句法改变具体含义。',
 'The menu lists alcoholic and nonalcoholic drinks separately.\n\n菜单分列含酒精饮料与无酒精饮料。','alcoholic nonalcoholic')

He=[['古英语 hecg → 中古英语 hegge → hedge','围出边界的树篱、灌木屏障'],['围住、保护的动作 → 设防、对冲；留边界 → 言语保留','hedge + hog → 刺猬名称；hog 提供猪般形象']]
W('hedge','/hedʒ/','树篱；围住、设防；含糊其辞；对冲',
 '一排灌木把花园围出边界，是 hedge。说话不把自己押在绝对判断上，留一圈余地，也叫 hedge；风险语境则借保护屏障说对冲。',
 '承古英语 hecg、中古英语 hegge，原为篱、围栏。名词转动词形成围住、保护，再发展到限制承诺、安排抵消风险等比喻。',He,
 'a garden hedge 花园树篱；hedge an answer 回答有所保留；hedge one’s bets 给自己留后路；hedge against risk 对冲风险。',
 'a garden hedge；hedge one’s bets；hedge against。',
 'hedge 言语保留可以是谨慎，也可以是回避；金融 hedge 指抵消某类风险，不等于保证绝无损失。',
 ('A thick hedge separated the two gardens.','茂密的树篱把两座花园隔开。'),('He hedged when asked for a definite answer.','被要求明确作答时，他却说得含含糊糊。'))
W('hedgehog','英 /ˈhedʒhɒɡ/；美 /ˈhedʒhɑːɡ/','刺猬',
 '树篱边的小家伙，鼻脸、叫声或外形让人联想到猪，于是 hedge + hog 成了刺猬名。重点是生活场景与猪般形象，不是真有一只小猪长了刺。',
 '承中古英语 heyghoge 等，对应 hedge + hog，逐步取代英语里更早的一些刺猬名称。hog 的比拟细节不必固定为唯一一项特征。',He[:1]+[['hedge + hog → hedgehog','篱边小动物的复合名称，借猪般形象']],
 'a hedgehog in the garden 花园里的刺猬；a curled hedgehog 蜷起的刺猬。',
 'a hedgehog；a hedgehog’s spines。',
 'hedgehog 与 porcupine 豪猪是不同动物；都长刺不代表是同一个名字的大小版本。',
 ('A hedgehog rustled through the dry leaves.','一只刺猬沙沙地穿过干叶。'),('The hedgehog curled into a ball.','刺猬蜷成了一团。'),sources=['https://en.wiktionary.org/wiki/hedgehog#English','https://blog.oup.com/2026/04/hogs-hedges-hedgehogs-and-bas/'])
R('B4047','树篱的围护与边界，再借到言语保留和风险安排','HEDGE：围一圈保护，也给自己留些余地','hedge → hedgerow、hedgehog；动作比喻则看围住、设防、不作过满承诺。',
 '花园树篱是实物屏障；hedge an answer 是不把话说死，hedge one’s bets 是保留其他可能。刺猬名的 hog 借动物形象，不把它当成猪的种类。',
 'hecg → hegge → hedge；row 一排；hog 猪般形象。',
 [['树篱、篱墙与动物名','hedge · hedgerow · hedgehog']],
 'hedge 保留说法有谨慎和回避两种评价；hedgehog 与 porcupine 不同。',
 'The hedgehog disappeared beneath the hedge beside the hedgerow.\n\n刺猬钻进篱墙边的树篱下，不见了。','hedge hedgerow hedgehog')

Gr=[['grease 油脂、涂油 → grease + -er','涂油者、装置；工作中沾油的机械工称呼'],['发油造型 → greaser 的青年亚文化称呼','尤其联系某些年代的油亮后梳发型与穿着形象']]
W('greaser','英 /ˈɡriːsə/；美 /ˈɡriːsər/','涂油者、装置；〔口语〕机械工；发油青年',
 'grease 是油脂或上油，greaser 可以直接说做这件事的人、装置。电影、音乐史里常指把头发抹得油亮后梳的一类青年形象，名字抓的是发油造型。',
 'grease + -er，材料、动作词发展执行者名，再用于工作会沾油的机械工和发油造型群体。它也有针对族群的贬称历史，不能把所有人物用法都当中性职业名。',Gr,
 'a greaser hairstyle 发油后梳造型；a greaser character 发油青年形象；an automatic greaser 自动润滑装置。',
 'a greaser hairstyle；an automatic greaser。',
 'greaser 的机械、亚文化和贬称语境不同；复古造型描写看服装、头发等上下文。',
 ('The film’s greaser characters wore leather jackets.','电影里的发油青年角色穿着皮夹克。'),('The machine uses an automatic greaser.','这台机器使用自动润滑装置。'))
R('B3388','油脂、油腻性质与涂油人物、器具','GREASE：抹上去是润滑，沾在表面是油腻','grease → greasy、greaser，从材料到性质，再到使用者、器具和文化形象。',
 '润滑是功能，油腻是表面状态，greaser 的发油青年形象则按造型命名。不同人物称呼还带时代、语境评价，不可机械地都译成上油工。',
 'grease + -y → greasy；grease + -er → greaser；读音随具体词与地区有变体，逐词看音标。',
 [['油脂、性质与执行者或器具','grease · greasy · greaser']],
 'greasy 常说表面、食物油腻；greaser 的人物用法还需辨亚文化、职业或贬称。',
 'The greaser’s jacket looked greasy after the repair.\n\n那位机械工修理后，夹克看起来油乎乎的。','grease greasy greaser')

Me=[['古英语 myrge 愉快、悦耳 → 中古英语 merie 等 → merry','令人愉快与兴高采烈的性质'],['merrily、merriment；古英语 myrgth 等 → mirth','开心地；欢乐场面；欢笑中的喜悦']]
W('merry','/ˈmeri/','欢乐、兴高采烈的；热闹愉快的',
 '一群人有说有笑，气氛轻快热闹，是 merry 最好抓的场面。Merry Christmas 也是祝节日快乐，不是只说对方此刻正在笑。',
 '承古英语 myrge、myrige 的愉快、悦耳等义，经中古英语 merie 等到 merry。现代常强调欢乐、兴高采烈的气氛。',Me,
 'Merry Christmas 圣诞快乐；a merry laugh 快活的笑；make merry 纵情欢乐。',
 'Merry Christmas；a merry laugh；make merry。',
 'merry 常带热闹、轻快的神态；happy 范围更宽，也可说安静的满足。',
 ('The room was full of merry laughter.','房间里满是快活的笑声。'),('They wished us a merry Christmas.','他们祝我们圣诞快乐。'))
W('merrily','/ˈmerɪli/','快活地、兴高采烈地；〔有时〕毫不在意地',
 '人笑着唱歌，水咕噜咕噜欢快流动，可以 merrily。The printer merrily ignored the setting 还可能带讽刺：它倒是照旧干自己的，完全没理会设置。',
 '承古英语相应副词，经中古英语 myriely 等延续，现代 merry 的 y 改 i + -ly → merrily。欢乐方式后来也可带毫不在意的叙述语气。',Me[:1]+[['merry → merrily','以快活、轻快方式；有时带照旧、满不在乎语气']],
 'laugh merrily 快活地笑；sing merrily 欢快唱歌；merrily continue 照旧继续，需看语气。',
 'laugh merrily；sing merrily。',
 'merrily 不保证每次都在夸愉快，有时叙述者是在讽刺对方不顾问题仍照做。',
 ('The children sang merrily on the way home.','孩子们回家路上欢快地唱着歌。'),('The stream bubbled merrily over the stones.','溪流越过石块，欢快地咕噜作响。'))
W('mirth','英 /mɜːθ/；美 /mɜːrθ/','欢笑、欢乐',
 '一个笑话让大家笑出声，眼角都亮起来，那种由幽默带来的欢乐是 mirth。它比普通 happy 更容易让人听见笑声。',
 '承古英语 myrgth 等欢乐名词，经中古英语 myrthe、murhthe 到 mirth，与 merry 同族，历史有抽象名词 -th。不是现代把 merry 的拼写直接砍成 mir 再加 th。',Me[:1]+[['古英语 myrgth → 中古英语 myrthe 等 → mirth','与 merry 同族的欢乐、欢笑名词']],
 'a burst of mirth 一阵欢笑；eyes full of mirth 眼里满是笑意；with mirth 带着欢乐。',
 'a burst of mirth；full of mirth。',
 'mirth 常偏文学、书面并联系欢笑；happiness 是更广的快乐、幸福，使用场景不同。',
 ('Her eyes shone with mirth.','她眼里闪着笑意。'),('The joke caused a burst of mirth around the table.','笑话让桌旁的人爆发出一阵欢笑。'))
W('merriment','/ˈmerɪmənt/','欢笑、欢乐热闹的活动',
 '不只一个人心里开心，而是一群人笑闹、玩乐的欢乐劲头，常用 merriment。节庆、聚会、游戏场面很适合这个词。',
 '旧动词 merry 欢乐、使欢乐，加 -ment → merriment，y 改 i。现代可与形容词 merry 对照，但不能因此把历史简化为形容词直接加 -ment。',Me[:1]+[['旧动词 merry 欢乐、使欢乐 + -ment → merriment','欢乐状态、嬉笑玩乐']],
 'laughter and merriment 欢声笑语；much merriment 许多欢乐；join the merriment 加入欢乐场面。',
 'laughter and merriment；join the merriment。',
 'merriment 与 mirth 有重叠，前者更容易铺出玩乐的场面，不能硬说一个只许多人、一个只许一人。',
 ('The games brought much merriment to the party.','游戏给聚会带来了许多欢乐。'),('We could hear laughter and merriment from the next room.','我们听见隔壁传来欢声笑语。'))
R('B4320','愉快性质、快活方式与欢笑名词，同族旧形式一起读','MERRY：人有说有笑，场面轻快热闹','merry → merrily、merriment；mirth 是同族古老名词，单独保留历史词形。',
 'merry 描述人、声音和气氛，merrily 说怎样进行，mirth、merriment 把欢乐欢笑作为名词谈。它们有重叠，靠场景和文体理解。',
 'myrge → merie → 形容词 merry，接 -ly 对应 merrily；旧动词 merry 欢乐、使欢乐接 -ment 对应 merriment；myrgth → mirth，历史 -th 抽象名词。',
 [['性质、方式与欢笑名词','merry · merrily · merriment · mirth']],
 'mirth 偏书面欢笑，merriment 常铺出玩乐场面；不把两者硬划成人数规则。',
 'The merry group laughed merrily, filling the room with mirth and merriment.\n\n这群人兴高采烈地笑着，房间里满是欢乐。','merry merrily merriment mirth')

Re=[['旧动词 reck 顾虑、在意 + -less → 古英语 recelas 等','不顾虑、不在意后果的性质'],['reckless → recklessly、recklessness','不顾后果的方式；鲁莽性质']]
W('reckless','/ˈrekləs/','鲁莽的；不顾危险、后果的',
 '前面有明显风险，还不把后果放在心上就往前冲，是 reckless。重点不只是胆子大，而是该顾到的后果没有顾。',
 '承古英语 recelas、中古英语 reckeles 等，对应旧动词 reck 顾虑、在意 + -less 缺少。reck 现代不常单独用，词尾保留了旧构词。',Re,
 'reckless behaviour 鲁莽行为；a reckless decision 不顾后果的决定；reckless spending 不计后果地花钱。',
 'reckless behaviour；a reckless decision。',
 'brave 勇敢可以是在了解风险后仍行动；reckless 通常批评不顾风险，不是勇敢的普通同义词。',
 ('It was reckless to begin without checking the equipment.','不检查设备就开始，太鲁莽了。'),('The report criticised the team’s reckless approach.','报告批评团队做法不顾后果。'))
W('recklessly','/ˈrekləsli/','鲁莽地、不顾后果地',
 'reckless 是做法的性质，recklessly 把这种不顾危险的劲头放进具体动作。说 acted recklessly，不只是行动很快，而是缺少该有的顾虑。',
 '承古英语、英语中古阶段的对应副词，现代可拆 reckless + -ly。方式副词承接不顾后果的负面评价。',Re[:1]+[['reckless + -ly → recklessly','以不顾危险、后果的方式']],
 'act recklessly 鲁莽行事；spend recklessly 不计后果花钱；recklessly ignore 完全不顾地忽视。',
 'act recklessly；spend recklessly。',
 'quickly 只说快，recklessly 评价考虑后果不足；快不一定鲁莽，慢也可能鲁莽。',
 ('He recklessly ignored the clear warning.','他鲁莽地无视了明确警告。'),('They spent recklessly during the first month.','第一个月，他们花钱毫不考虑后果。'))
W('recklessness','/ˈrekləsnəs/','鲁莽；不顾后果的性质、行为',
 '把几次决定、整个做法里不顾后果的共同问题抽出来，就是 recklessness。它是对风险态度的评价，不只是一个动作速度快。',
 '承古英语 recelasnes、中古英语相应名词，现代对应 reckless + -ness。-less 与 -ness 各有作用：先是否定顾虑，再把整个性质名词化。',Re[:1]+[['reckless + -ness → recklessness','不顾后果的性质、程度']],
 'an act of recklessness 一次鲁莽行为；sheer recklessness 全然不顾后果；the recklessness of a decision 决定的鲁莽。',
 'an act of recklessness；sheer recklessness。',
 '-lessness 这里可分 -less + -ness，不是一个“越多越少”的绕口逻辑；名词谈的是不顾虑这份性质。',
 ('The accident exposed the recklessness of the earlier decision.','事故暴露了先前决定的鲁莽。'),('She saw the stunt as an act of recklessness.','她认为那次特技表演是鲁莽之举。'))
R('B4161','少了对危险后果的顾虑，方式与性质名词接着展开','RECKLESS：该想的后果没放在心上，就往前冲','reckless → recklessly、recklessness，从性质到动作方式，再到整体评价。',
 '旧 reck 顾虑的用法不常单独见了，但 -less 仍保留不顾虑的构词。勇敢与鲁莽最关键的区别之一，就是是否认真看待风险、后果。',
 'reck + -less → reckless；-ly 方式；-ness 性质，-less + -ness 两层后缀。',
 [['性质、方式与鲁莽程度','reckless · recklessly · recklessness']],
 'reckless 通常是批评，不是 brave 的普通替换；recklessness 把这种性质名词化。',
 'Acting recklessly, he mistook recklessness for courage.\n\n他行事鲁莽，却把不顾后果误认成勇气。','reckless recklessly recklessness')

Sc=[['拉丁语 socius 同伴、社会结合相关 → socio-','在复合词中限定社会、群体方面'],['socio- + linguistics／linguistic；与 -path 相关构词','社会与语言研究；社会病态相关人物旧称及形容词']]
W('sociolinguistics','英 /ˌsəʊsiəʊlɪŋˈɡwɪstɪks/；美 /ˌsoʊsioʊlɪŋˈɡwɪstɪks/','社会语言学',
 '为什么同一个人在朋友面前和面试时说话不同？为什么地区、阶层、群体影响用词？把语言放进社会关系里研究，就是 sociolinguistics。',
 'socio- 社会 + linguistics 语言学。前缀加入社会维度，研究语言与社会、文化的相互联系。学科名词尾虽有 s，通常按学科整体作单数。',Sc,
 'a course in sociolinguistics 社会语言学课程；research in sociolinguistics 社会语言学研究。',
 'a course in sociolinguistics；sociolinguistics research。',
 'sociolinguistics 不是学习几句社交套话，而是研究语言如何与群体、身份、场合等联系。',
 ('Sociolinguistics examines how language varies across social groups.','社会语言学研究不同社会群体的语言怎样变化。'),('The course in sociolinguistics includes interviews from several communities.','社会语言学课程包含几个社区的访谈材料。'))
W('sociolinguistic','英 /ˌsəʊsiəʊlɪŋˈɡwɪstɪk/；美 /ˌsoʊsioʊlɪŋˈɡwɪstɪk/','社会语言学的；语言与社会相关的',
 'sociolinguistics 是研究领域，sociolinguistic 描述相关问题、因素。a sociolinguistic difference 可以是人们因社会背景、身份不同而出现的语言差异。',
 'socio- + linguistic；与学科名 sociolinguistics 形成名词、形容词对应。不要把末尾 s 都当可有可无的同一词。',Sc[:1]+[['socio- + linguistic → sociolinguistic','语言与社会关系方面的性质']],
 'sociolinguistic variation 社会语言变异；sociolinguistic factors 社会语言学因素；a sociolinguistic study 社会语言学研究。',
 'sociolinguistic variation；sociolinguistic factors。',
 '学科名 sociolinguistics，形容词 sociolinguistic；同样的名词、性质区别还见 linguistics 与 linguistic。',
 ('The paper explores sociolinguistic variation in the city.','论文探讨城市里的社会语言变异。'),('Age and social setting were important sociolinguistic factors.','年龄和社交场景是重要的社会语言学因素。'))
W('sociopath','英 /ˈsəʊsiəʊpæθ/；美 /ˈsoʊsioʊpæθ/','社会病态人格者〔较旧、非正式人物称呼〕',
 '影视、旧资料中的 sociopath，常用来指长期无视他人权利、社会约束的人。它不是“不爱社交的人”，也不是凭一件自私行为就能准确贴上的诊断标签。',
 'socio- 社会 + -path 病态相关人物构词。历史上与反社会人格相关称呼相连，现代日常媒体用法又常较松散；不能只按社会 + 病人理解所有实际指称。',Sc[:1]+[['socio- + -path → sociopath','社会病态、反社会人格相关的旧称与非正式人物标签']],
 'a fictional sociopath 小说中的社会病态人格角色；the term sociopath 这个称呼。读人物评价时注意是谁在使用标签。',
 'a fictional sociopath；the term sociopath。',
 'sociopath 不等于 introvert 内向的人；社交偏好与长期侵犯他人权利不是同一维度。',
 ('The critic described the fictional villain as a sociopath.','评论者把小说反派称作社会病态人格者。'),('The article explains why sociopath is an imprecise everyday label.','文章解释为什么 sociopath 在日常使用中是个不够精确的标签。'),sources=['https://en.wiktionary.org/wiki/sociopath#English','https://dictionary.apa.org/antisocial-personality-disorder','https://www.apa.org/news/podcasts/speaking-of-psychology/psychopathy'])
W('sociopathic','英 /ˌsəʊsiəʊˈpæθɪk/；美 /ˌsoʊsioʊˈpæθɪk/','社会病态的；反社会人格相关的〔常见旧称、非正式用语〕',
 'sociopath 是人物标签，sociopathic 把相应特点当成形容性质。影视评论里 sociopathic behaviour 往往批评持续操纵、伤害别人，不是说某人安静、不愿聚会。',
 'socio- + -pathic，亦与 sociopath + -ic 的人物、性质关系对应。词源是社会与病态相关材料，具体历史和现代使用范围需看语境。',Sc[:1]+[['socio- + -pathic → sociopathic','与社会病态相关的性质、行为描述']],
 'sociopathic behaviour 社会病态行为；a sociopathic character 相应人物设定。用于实际人物时不是可靠的随意诊断。',
 'sociopathic behaviour；a sociopathic character。',
 'sociopathic 与 unsociable 不爱交际不同；反社会的权利侵犯含义不能被缩成不合群。',
 ('The novel portrays a character with sociopathic traits.','小说塑造了一个带有社会病态特征的人物。'),('The reviewer questioned the casual use of sociopathic to describe the character.','评论者质疑随意用 sociopathic 来描述这个角色。'),sources=['https://en.wiktionary.org/wiki/sociopathic#English','https://dictionary.apa.org/sociopathic-personality','https://www.apa.org/news/podcasts/speaking-of-psychology/psychopathy'])
R('A1990','社会、群体维度，接学科、文化或病态相关旧称','SOCIO-：把后面的事放进社会关系里看','sociology、sociocultural、sociolinguistics 等看社会研究维度；sociopath 词族另有术语历史。',
 '同一个前缀不决定后半含义。语言学看群体如何影响说话，文化词看社会文化联系；病态人物旧称则不能由字面升级成所有不合群的人。',
 'socius 同伴相关材料 → socio-；-logy 研究；cultural 文化；linguistics 语言学；-path、-pathic 病态相关构词。',
 [['社会、文化与语言研究','sociology · sociocultural · sociolinguistics · sociolinguistic'],['人物旧称与相应性质','sociopath · sociopathic']],
 'sociolinguistics 学科名与 sociolinguistic 形容词不同；sociopath 不等于内向、独处者。',
 'The sociolinguistic study examined sociocultural differences in everyday speech.\n\n社会语言学研究考察了日常说话中的社会文化差异。','sociology sociocultural sociolinguistics sociolinguistic sociopath sociopathic')

Ur=[['拉丁语 urina → urinalis → 法语 urinal → 英语 urinal','尿相关的器具名称'],['urinal → 尿壶、小便器等','早期便携容器与后来的固定卫生器具用途相接']]
W('urinal','英 /jʊəˈraɪnəl/；美 /ˈjʊrɪnəl/','小便器；尿壶',
 'urine 是尿，urinal 是用来接尿的器具。公共厕所墙上的小便器、某些便携尿壶都在这个词的范围，场景决定具体外形。',
 '经中古英语 urinal，借法语 urinal、orinal，上接拉丁语 urinalis 尿相关。现代可对应尿词干 + -al，但器具名早有独立借入历史。',Ur,
 'a wall urinal 壁挂小便器；a portable urinal 便携尿壶。英美常见读音重音、元音有区别，分别看音标。',
 'a wall urinal；a portable urinal。',
 'urinal 是器具，urine 是物质，urinate 是动作；三者不因中文都带尿就互换。',
 ('The restroom has three urinals.','洗手间里有三个小便器。'),('The catalogue includes a portable urinal.','目录里有一款便携尿壶。'))
R('B3636','物质、排出动作与容纳器具分层','URINE：尿是物质，urinate 是动作，urinal 是器具','urine → urinate、urinal，从同族物质名称走向动作与用品。',
 '明确谁是东西、谁是动作、谁是容器，句子就不会混乱。urinal 的英美读音有明显变体，不能只按 urine 直接接后缀猜读。',
 '拉丁 urina 及相关形式 → urine、urinate；urinalis → 法语 urinal → urinal。',
 [['物质、动作与容器','urine · urinate · urinal']],
 'urine 物质、urinate 动作、urinal 器具；urinal 的常见英美重音不同。',
 'The label identifies the urinal as a container for urine.\n\n标签说明尿壶是用于接尿的容器。','urine urinate urinal')

Ia=[['希腊、拉丁语 -ia 相关名词形式进入英语','状态、领域、群体、名称等多种历史用法'],['Poinsett 姓氏 + -ia → 植物属名 Poinsettia → poinsettia','以人名命名的植物，后来作常用植物名']]
W('poinsettia','/ˌpɔɪnˈsetiə/，也常读 /ˌpɔɪnˈsetə/','一品红、圣诞红',
 '节庆摆放的红绿相间盆栽，常是 poinsettia。显眼的红色部分主要是苞片，真正的花较小；名字则纪念 Poinsett 这个人，不是按红色硬拆出来。',
 '由旧植物属名 Poinsettia 转成通名，属名纪念 Joel Roberts Poinsett，对应 Poinsett + -ia。现代植物学归属与普通英语沿用的名字可不同。',Ia,
 'a potted poinsettia 一盆一品红；poinsettia bracts 一品红苞片；Christmas poinsettias 节庆一品红盆栽。',
 'a potted poinsettia；poinsettia bracts。',
 '红色苞片不等于整片都是真花瓣；读音里有时简化 -tia，但常见规范拼写仍是 poinsettia。',
 ('A red poinsettia stood beside the window.','窗边放着一盆红色一品红。'),('The display used poinsettias with bright red bracts.','布置用了红色苞片鲜艳的一品红。'),sources=['https://en.wiktionary.org/wiki/poinsettia#English','https://www.apsnet.org/edcenter/apsnetfeatures/Pages/PoinsettiaFlower.aspx','https://www.um.edu.mt/newspoint/news/2020/12/poinsetta-christmas-campus-1'])
R('A2040','借入的名词结尾，状态、领域、群体与专名各有历史','-IA：看见名词结尾，还要认前面具体在命名什么','insomnia 等状态名、suburbia 等集合名、poinsettia 人名植物名，不能被一个中文后缀包办。',
 '不少 -ia 词是古典语言整词或相关名词形式借入，也有现代按名称造词。它不独立说明某种疾病，更不表示每个词都能机械砍掉两个字母。',
 '希腊、拉丁语 -ia 等名词形式；insomnia、arrhythmia 等读各自历史；Poinsett + -ia → poinsettia。',
 [['状态、功能与文化名词','insomnia · arrhythmia · alexia · dyspepsia · psychedelia'],['地域群体与植物名','suburbia · poinsettia']],
 '-ia 不是统一的疾病标志；poinsettia 中它参与人名植物命名，suburbia 则指郊区生活、地区整体。',
 'The booklet places a poinsettia on its cover and explains several words ending in -ia.\n\n小册子封面画着一品红，内文解释几个以 -ia 结尾的词。','insomnia suburbia arrhythmia alexia psychedelia dyspepsia poinsettia')

if __name__=='__main__':save('continuation_20261030_nv',ROOTS,WORDS)
