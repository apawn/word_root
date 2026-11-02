"""Chemical -one, pests, bound directions, inactivity, breakers, nerds, crabs and dwarf."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()

On=[['化学酮名中的 -one → 科学命名词尾','常提示酮结构相关命名，不能只看结尾猜用途'],['pro-、gest- 与 -one → progesterone；化学缩略材料 → naloxone','激素、药物名有各自形成方式'],['silicone 的 -one 是历史类比命名','现代物质不因旧名而成为普通酮']]
W('progesterone','英 /prəˈdʒestərəʊn/；美 /proʊˈdʒestəroʊn/','孕酮、黄体酮',
 '这是参与月经周期、妊娠过程的一种激素名。词里 gest- 能联系承载、孕育的材料，但一个名字不足以概括它的全部生理作用。',
 '由 pro- 与 gestation、拉丁 gestare 承载的相关材料，再接化学 -one 形成名称。末尾是酮类化学命名材料，不是数字 one。',On[:2],
 'progesterone levels 孕酮水平；the role of progesterone 孕酮的作用。既可指身体产生的激素，也可指相应制剂中的物质。',
 'progesterone levels；the role of progesterone。',
 'progesterone 是具体物质名，hormone 是更广的激素类别；名称里的 pro- 不能单凭字面推出适用人群或效果。',
 ('The chapter explains the role of progesterone in the menstrual cycle.','这一章解释孕酮在月经周期中的作用。'),('The diagram labels progesterone as a steroid hormone.','图示把孕酮标为一种甾体激素。'),sources=['https://en.wiktionary.org/wiki/progesterone#English','https://www.cancer.gov/publications/dictionaries/cancer-terms/def/progesterone'])
W('naloxone','英 /nəˈlɒksəʊn/；美 /nəˈlɑːksoʊn/','纳洛酮',
 '公共健康新闻里常见的阿片受体拮抗药名，能逆转阿片类物质的相应作用。先记这是针对阿片作用的药，不是任何中毒都通用的解药名。',
 '名称压缩了 N-allyl 的 N-烯丙基材料、hydroxy- 羟基材料，再接 -one；不是一个可照字母直译疗效的日常复合词。',
 [['N-allyl、hydroxy- 与 -one 的化学命名材料','结构成分被缩短组合'],['naloxone 形成专门药名','阿片受体拮抗药名称']],
 'naloxone nasal spray 纳洛酮鼻喷制剂；naloxone distribution 纳洛酮分发，常见于公共健康报道。',
 'naloxone distribution；naloxone nasal spray。',
 'naloxone 是通用物质名，Narcan 是相应品牌名之一；-one 也不会让 acetone、progesterone 与它具有相同作用。',
 ('The article discusses naloxone distribution in the community.','文章讨论了社区中的纳洛酮分发。'),('The glossary defines naloxone as an opioid antagonist.','术语表把纳洛酮定义为阿片受体拮抗药。'),sources=['https://en.wiktionary.org/wiki/naloxone#English','https://www.merriam-webster.com/dictionary/naloxone'])
R('A1706','酮类化学命名材料及其历史类比，不等于数字一','-ONE：认出化学命名，别凭词尾猜用途','acetone 先学简单酮名；progesterone、naloxone 认专门物质；silicone 记历史类比与现代结构不同。',
 '同一个化学词尾可以出现在溶剂、激素、药物名里，性质、用途不能互相套。silicone 还提醒我们，历史命名并不总是现代结构的完美说明。',
 '酮名的 -one 推广为化学词尾；progesterone 接孕育材料；naloxone 压缩结构成分；silicone 原有酮类比，现代指硅氧骨架聚合物系列。',
 [['简单化学名与专门物质名','acetone · progesterone · naloxone'],['历史类比名','silicone']],
 'megaphone 的末尾实际是 -phone 声音，不能拆为这个 -one；silicone 不等于 silicon 元素硅，也不按旧名当普通酮。',
 'The glossary lists acetone, progesterone and naloxone as different chemical substances.\n\n术语表把丙酮、孕酮和纳洛酮列为不同化学物质。','acetone progesterone naloxone silicone')
ROOTS[-1]['exclude']['megaphone']='接 -phone 声音材料，不是化学 -one。'
ROOTS[-1]['exclude']['arachidonic']='相应脂肪酸形容词含 -ic 等构形，不作 -one 的直接词尾实例。'

Pe=[['拉丁 pestis 瘟疫、祸害 → 法语 peste → pest','严重危害的名称'],['pest → 有害生物、烦人者；pest + -icide → pesticide','危害、烦扰按对象变化；相关制剂名']]
W('pest','/pest/','有害生物、害虫；讨厌鬼、烦人的人',
 '吃掉庄稼、损坏物品的生物可叫 pest；总来烦你的人也能被抱怨为 a pest。核心是对某个对象造成危害、麻烦。',
 '十六世纪经法语 peste 接拉丁 pestis，早期指瘟疫、祸害，后扩成有害生物和烦人者。不能把它限制为一种特定昆虫。',Pe,
 'an agricultural pest 农业有害生物；pest control 有害生物防治；make a pest of yourself 不断烦人。',
 'pest control；an agricultural pest。',
 'pest 是与人类用途、处境有关的判断，不等于全部 insect 昆虫；pesticide 也不只指杀虫剂中的某一类。',
 ('The farmer identified the insect as a crop pest.','农民认出那种昆虫是农作物害虫。'),('Stop ringing the bell; you are making a pest of yourself.','别老按门铃了，你这样太烦人了。'))
R('B3660','瘟疫、祸害的旧材料转为有害生物与烦扰者','PEST：对当前对象有害、添麻烦的东西','pest → pesticide，先对象，再控制相应有害生物的制剂名。',
 '有害生物不限昆虫，烦人者也只是比喻。理解命名中谁对谁造成影响，比把 pest 背成一个虫字更准确。',
 'pestis → peste → pest；pest + -icide 杀灭材料 → pesticide。',
 [['有害对象与相关制剂','pest · pesticide']],
 '不是所有昆虫都是 pest；pesticide 的范围比一般杀虫剂中文印象更广。',
 'The guide identifies common pests before discussing pesticides.\n\n指南先辨认常见有害生物，再讨论农药。','pest pesticide')

R('A2254','朝某处前往与受限制是两条 bound，复合词需分源','-BOUND：要么正朝那去，要么被困在这儿','southbound 等看行进方向；snowbound 看受困；homebound、earthbound 可能两义。',
 '同样 bound，南行列车不是被南方绑住，困在家也不是正坐车回家。先看整个句子的行进、受限场景，再决定哪条来源。',
 '前往的 bound 接古诺尔斯准备、启程材料；受束缚的 bound 是 bind 的旧分词。方位、home、earth、snow 等分别限定。',
 [['行进方向','southbound · northbound · eastbound · westbound'],['受限或方向，按语境区分','snowbound · homebound · earthbound']],
 'homebound 可说归家途中，也可说难以外出；earthbound 可地面受限，也可朝地球前进；不能合成一条被绑所以回去的故事。',
 'The southbound train carried homebound passengers through the snowbound countryside.\n\n南行列车载着归家乘客，穿过被大雪围困的乡野。','southbound northbound eastbound westbound snowbound homebound earthbound')
R('B4343','活动状态被否定，再分闲置与使失活过程','INACTIVE：眼下没有活动、起作用，不必永远坏掉','inactive → inactivity；inactivate → inactivation，状态与造成状态的动作分开。',
 '账号、设备、物质、人物可以在各自语境中不活跃。词先说状态，原因与是否能恢复由上下文决定。',
 'in- 否定 + active；-ity 状态；-ate 使进入状态；-ation 动作、过程。',
 [['不活跃性质及状态','inactive · inactivity'],['使不活跃的动作和过程','inactivate · inactivation']],
 'inactive 不等于所有东西 permanently broken 永久损坏；inactivity 是状态，inactivation 强调使成该状态的过程。',
 'The account remained inactive after its inactivation.\n\n账号停用后一直处于不活跃状态。','inactive inactivity inactivate inactivation')
R('B4009','打破、断开动作形成的人或物，复合词限定对象','BREAKER：它打破什么，名字就从那里来','breaker → icebreaker、tiebreaker；heartbreaker、windbreaker、jawbreaker 各看不同画面。',
 '-er 不只造人。断路器断开电路，碎浪拍碎，破冰船破冰；社交破冰、打破平局再把动作借到抽象局面。',
 'break + -er；ice 冰；tie 平局；heart 心；wind 风；jaw 颌。这些复合词里破坏、阻断、打破的强弱各不同。',
 [['基本人或物与破局功能','breaker · icebreaker · tiebreaker'],['情感、衣物与夸张命名','heartbreaker · windbreaker · jawbreaker']],
 'windbreaker 是挡风外套，不是毁坏风；jawbreaker 可大硬糖或难念词，属于夸张命名，不能按字面断言一定断颌。',
 'The icebreaker question became a tiebreaker in the game.\n\n那个破冰问题在游戏里成了决胜题。','breaker icebreaker tiebreaker heartbreaker windbreaker jawbreaker')

Ne=[['二十世纪中叶美国学生俚语 nerd，确切来源未定','1950年书中已有同形虚构名，但传播关系不确定'],['nerd → 热衷专门领域的自称；+ -y → nerdy','旧贬称与新认同并存']]
W('nerd','英 /nɜːd/；美 /nɜːrd/','书呆子；对某领域很着迷的人、爱好者',
 '别人聊明星，他能聊一小时字体或火车时刻表，可能自称 a nerd。早期常笑人不合群，如今也常是带骄傲的深度爱好者自称。',
 '二十世纪中叶美国学生俚语，确切来源未定。1950年 Dr. Seuss 书里有 Nerd 虚构名称，但不能直接断定所有后来的俚语只由这本书造出。',Ne,
 'a computer nerd 电脑迷；a history nerd 历史迷；a self-confessed nerd 自称书呆子、专业爱好者的人。',
 'a history nerd；a computer nerd。',
 'nerd 可贬可亲昵自称，语气和关系决定；它不等于聪明或内向的科学分类，也不限男性、程序员。',
 ('She calls herself a history nerd.','她自称是个历史迷。'),('The club welcomes nerds who love maps, languages and unusual facts.','这个社团欢迎喜欢地图、语言和奇闻知识的深度爱好者。'),sources=['https://en.wiktionary.org/wiki/nerd#English','https://www.etymonline.com/word/nerd'])
W('nerdy','英 /ˈnɜːdi/；美 /ˈnɜːrdi/','书呆子气的；专门爱好浓厚的；极客风格的',
 '两个朋友兴奋地讨论字体间距，自己笑着说 this is nerdy，是承认话题有点专、迷得有点深。它不一定在说话题没用。',
 'nerd + -y → nerdy，保留 d。形容词可描写人物、兴趣、穿着风格或专门讨论。',Ne+[['nerd + -y → nerdy','像这类爱好者；有相应兴趣、风格']],
 'a nerdy hobby 很专的爱好；a nerdy discussion 极客式讨论；a nerdy joke 懂行的人才领会的玩笑。',
 'a nerdy hobby；a nerdy discussion。',
 'nerdy 可是自嘲或赞同兴趣，不必永远译成贬义呆板；technical 则更中性说技术、专业性质。',
 ('They had a delightfully nerdy discussion about old keyboards.','他们兴致勃勃地聊了一番很极客的老键盘话题。'),('His nerdy jokes made the whole programming club laugh.','他的极客笑话逗笑了整个编程社团。'))
R('B3483','学生俚语的旧标签，转为专门爱好和文化认同','NERD：对某件事研究很深、喜欢很浓','nerd → nerdy，人物标签与兴趣、风格性质。',
 '读出语气比只背书呆子更有用。嘲笑和自我认领都存在；历史来源未定，不编成某个缩写或唯一作者造词。',
 '二十世纪中叶美国俚语 nerd，早期词形有不同线索；+ -y → nerdy。',
 [['爱好者称呼与相关风格','nerd · nerdy']],
 'nerd 不保证内向、聪明或社交差；nerdy 的具体褒贬由说话者关系与情景决定。',
 'As a language nerd, she enjoys nerdy conversations about word origins.\n\n作为语言迷，她很喜欢钻研词源的极客式讨论。','nerd nerdy')

Cb=[['古英语 crabba → 中古英语 crabbe → crab 蟹','更早常联系抓挠、爬动材料'],['另有野酸苹果 crab 一支；crab、crabbed 等坏脾气材料交汇','动物好斗、果实酸涩等联想影响评价用法'],['crab + -y → crabby','像蟹的；常用为易烦躁、爱抱怨']]
W('crab','/kræb/','蟹、螃蟹；蟹肉；〔口语〕抱怨、发牢骚',
 '实物先看螃蟹和蟹肉；人在一旁不停 crab about the noise，则是发牢骚。另一个旧 crab 指野酸苹果，不是长在树上的螃蟹。',
 '动物名承古英语 crabba，更早常联系抓挠、爬动词族。野酸苹果义另有斯堪的纳维亚等来源解释；坏脾气、抱怨义与 crabbed 等及两支形象交汇，不归成唯一夹人故事。',Cb,
 'catch crabs 捉蟹；crab meat 蟹肉；crab about something 抱怨某事。horseshoe crab 鲎虽带 crab，通名不替代科学分类。',
 'crab meat；crab about。',
 '英语 crab 动物通名可宽于严格的真蟹类群；抱怨义是人物语气评价，不能由它断言所有蟹都情绪差。',
 ('A crab disappeared beneath the rock.','一只螃蟹钻到了石头下面。'),('He kept crabbing about the weather.','他不停抱怨天气。'),sources=['https://en.wiktionary.org/wiki/crab#English','https://www.etymonline.com/word/crab'])
W('crabby','/ˈkræbi/','易怒、脾气坏的；爱抱怨的；像蟹的',
 '累了、饿了，别人一搭话就不耐烦，可以说 feel crabby。常用义抓坏脾气，不是真的手长成了蟹钳。',
 'crab 双写 b + -y → crabby。常用易怒义承接 crab、crabbed 的评价词族，历史还带动物好斗、酸涩等交汇联想。',Cb+[['crab + -y → crabby','像蟹的性质，常用为烦躁爱抱怨']],
 'feel crabby 感觉烦躁；a crabby remark 不耐烦的牢骚话；较口语。',
 'feel crabby；a crabby mood。',
 'crabby 与 cranky 都可说烦躁，不必硬分哪一个一定更严重；前者也并非只用于老人。',
 ('I get crabby when I have not slept enough.','没睡够时，我容易烦躁。'),('She apologised for sounding crabby on the phone.','她为自己电话里显得不耐烦而道歉。'))
R('B3817','蟹名与酸苹果旧词分支，坏脾气评价有交汇','CRAB：动物名先认实物，crabby 再看语气','crab → crabby；动物、食物与抱怨分开使用。',
 '螃蟹、野酸苹果是不同历史线，人物坏脾气用法在相关评价词中交汇。抓“烦躁、爱挑毛病”的感觉即可，不硬编成蟹钳夹痛人的唯一词源。',
 'crabba → crab；另有野酸苹果 crab；双写 b 接 -y → crabby；crabbed 等影响人物评价。',
 [['动物、食物、抱怨与相应性质','crab · crabby']],
 'crabby 是口语心情评价，不是疾病名；crab 通名与严格动物分类范围也未必相同。',
 'He was crabby and kept crabbing about the delay.\n\n他心情烦躁，不停抱怨延误。','crab crabby')

Dw=[['古英语 dweorg → 中古英语 dwergh、dwerf 等 → dwarf','旧神话人物与身材矮小相关称呼'],['dwarf → 相对小型、使显小；+ -ism → dwarfism','神话、大小比较、医学语境分开']]
W('dwarf','英 /dwɔːf/；美 /dwɔːrf/','〔奇幻〕矮人；矮小型的；使相形见小；〔人物称呼〕身材矮小者',
 '童话里是矮人，园艺里 dwarf tree 是矮生树，旁边新楼 dwarfs the house 则让房子显得很小。三个场景不要只背成同一种人物。',
 '承古英语 dweorg，经中古英语多种词形延续。相对矮小的性质发展为植物、天体等修饰及使显小动词；普通复数常 dwarfs，奇幻语境常 dwarves。',Dw,
 'a dwarf tree 矮生树；a white dwarf 白矮星；dwarf nearby buildings 使附近建筑相形见小。称真人时可用 a person with dwarfism，具体个人称呼偏好不同。',
 'a dwarf tree；dwarf nearby buildings。',
 'dwarf 作动词多是比较效果，不是把实物真缩小；dwarf planet 是具体天文类别，不等于随便一颗小行星。',
 ('The new tower dwarfs the neighbouring houses.','新塔楼让附近房屋显得很小。'),('They planted a dwarf apple tree in the small garden.','他们在小花园里种了一棵矮生苹果树。'))
W('dwarfism','英 /ˈdwɔːfɪzəm/；美 /ˈdwɔːrfɪzəm/','生长受限、显著矮小的状况；侏儒症',
 '医学语境里它说生长受限、身高显著较矮的一类情况，原因可以不同。不是每个比同学矮一点的人都能凭外观贴上这个词。',
 'dwarf + -ism → dwarfism，这里 -ism 命名状况，不是矮人主义。现代说明需分不同原因及身体比例情况。',Dw+[['dwarf + -ism → dwarfism','命名生长受限、显著矮小相关状况']],
 'a person with dwarfism 有相关生长状况的人；different forms of dwarfism 不同类型；不一概等同某一种骨骼病。',
 'a person with dwarfism；forms of dwarfism。',
 'dwarfism 可以有比例协调或不协调的情况；神话矮人设定不能代替对现实身体状况的理解。',
 ('The article discusses different causes of dwarfism.','文章讨论了生长受限、显著矮小状况的不同原因。'),('The interview focuses on everyday life with dwarfism.','访谈关注有相关生长状况者的日常生活。'),sources=['https://en.wiktionary.org/wiki/dwarfism#English','https://www.nhs.uk/conditions/restricted-growth/'])
R('B3940','古老人名、相对矮小与比较效果，医学状况另分','DWARF：尺寸比旁边小，动词则让别人显小','dwarf → dwarfism；奇幻人物、矮生植物、天体名与真人状况按语境辨认。',
 '最有用的对照是小本身和使旁边显小。医学状况涉及具体原因，不从神话人物推定现实身体特点。',
 'dweorg → 中古英语相关形式 → dwarf；-ism 状况；dwarfs 常用普通复数，dwarves 常见奇幻。',
 [['小型、人物与比较动作','dwarf'],['生长相关状况名','dwarfism']],
 'dwarf 作比较动词不表示真的缩小；dwarfism 不是所有个子较矮的同义词，也不是思想主义。',
 'The tall building dwarfs the dwarf trees beside it.\n\n高楼衬得旁边的矮生树更小了。','dwarf dwarfism')

if __name__=='__main__':save('continuation_20261030_on',ROOTS,WORDS)
