"""Multiples, pints, borne forms, caps, -itude, geometry, phobias and spurs."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()

Fo=[['古英语 -feald 等 → -fold','几重、几倍的数量材料，与折叠词族相关'],['数词或 many 的旧形式 + -fold','两倍、三倍、多样等；具体数字看前半']]
W('twofold','英 /ˈtuːfəʊld/；美 /ˈtuːfoʊld/','两倍的；双重的；成两倍地',
 '一份变两份，是倍数；一个目的分成两个方面，是双重。twofold 不要求真把纸折两次。',
 '古英语 tweofeald 等经中古英语延续，现代对应 two + -fold；不是 two 次折纸就固定等于两层。',Fo,
 'a twofold purpose 双重目的；a twofold increase 常说变为两倍；increase twofold 成两倍增长。用明确数字避免汉语“增加两倍”的歧义。',
 'a twofold purpose；a twofold increase。',
 '从 10 到 20 是变为原来的两倍，不是增加到 30；涉及 increase by 等写法时最好核对作者具体数字。',
 ('The project has a twofold purpose: education and conservation.','项目有双重目的：教育与保护。'),('The count rose twofold, from ten to twenty.','数量从十增到二十，变为两倍。'))
W('threefold','英 /ˈθriːfəʊld/；美 /ˈθriːfoʊld/','三倍的；三重的；成三倍地',
 '原来一份，现在同样大小的三份；或者一个结构有三个方面，都是 threefold 的常见用法。',
 '接古英语 thrifeald 等，现代对应 three + -fold。th 是 /θ/，不要把 three 的开头读成 tree。',Fo+[['three + -fold → threefold','三倍，或三个方面、部分']],
 'a threefold increase 变为三倍的增长；a threefold division 三分结构；grow threefold 变为三倍。',
 'a threefold increase；a threefold division。',
 'threefold 不等于 three times more 在所有文本中的唯一计算约定；具体倍数最好用前后数量说明。',
 ('The sample count increased threefold, from one hundred to three hundred.','样本数量从一百增至三百，变为三倍。'),('The chapter presents a threefold division of the topic.','这一章把主题分成三个部分。'))
W('fourfold','英 /ˈfɔːfəʊld/；美 /ˈfɔːrfoʊld/','四倍的；四重的；成四倍地',
 '把原来的量当一份，最后有四份一样多，就是 fourfold 的倍数义。也能说四个组成方面。',
 '接古英语 feowerfeald 等；现代可对应 four + -fold。这里 fold 表倍数、重数，不是反复折纸次数。',Fo+[['four + -fold → fourfold','四倍，或四个方面、部分']],
 'a fourfold increase 变为四倍的增长；a fourfold classification 四分法；expand fourfold 扩为四倍。',
 'a fourfold increase；a fourfold classification。',
 'fourfold 是四倍，four folds 常指四道折痕或四次折叠；后者的最终层数取决于怎么折。',
 ('The count rose fourfold, from four to sixteen.','数量从四增至十六，变为四倍。'),('The author proposes a fourfold classification.','作者提出了一种四分法。'))
W('tenfold','英 /ˈtenfəʊld/；美 /ˈtenfoʊld/','十倍的；成十倍地',
 '从十个变成一百个：原来的一份，现在有十份那么多。tenfold 的数字很明确，不是随口说非常多。',
 '接古英语 tienfeald 等，现代对应 ten + -fold；既可作倍数性质的修饰语，也可直接修饰增长动作。',Fo+[['ten + -fold → tenfold','达到原量的十倍；十重']],
 'a tenfold increase 变为十倍的增长；increase tenfold 变为十倍；tenfold capacity 十倍容量。',
 'a tenfold increase；increase tenfold。',
 'tenfold 是倍数，ten percent 是百分之十；不能把十倍增长读成只多一成。',
 ('The number of records grew tenfold, from ten to one hundred.','记录数从十条变成一百条，变为十倍。'),('The new storage system offers tenfold capacity.','新的存储系统提供十倍容量。'))
Mf=[['古英语 manigfeald → 中古英语 manifold','many 的旧材料 + -fold：多重、众多、多样'],['英语 manifold 在工程、数学中专门化','多支接口、歧管；流形等固定名词']]
W('manifold','英 /ˈmænɪfəʊld/；美 /ˈmænɪfoʊld/','多种多样的；歧管；流形〔数学〕',
 '先抓许多种、许多方面。工程里一处接出多路管道叫 manifold；数学流形则是局部可像普通空间那样描述的对象，不要求真的折叠。',
 '接古英语 manigfeald，对应 many 的旧形式 + -fold。不是 mani 手的拉丁词根加 fold；现代歧管、流形都是专门化用法。',Mf,
 'manifold causes 多种原因；an intake manifold 进气歧管；a two dimensional manifold 二维流形。流形可借球面局部像平面理解，但不只球面一种。',
 'manifold causes；an intake manifold；a mathematical manifold。',
 'manifold 不表示一个确定倍数；数学流形也不一律是三维空间里折弯的纸，直观例子不能代替一般定义。',
 ('The report examines the manifold causes of the problem.','报告考察了问题的多种原因。'),('The mechanic inspected the intake manifold.','机械师检查了进气歧管。'),('A sphere provides a familiar example of a manifold.','球面是一个熟悉的流形例子。'),sources=['https://en.wiktionary.org/wiki/manifold#English','https://www.merriam-webster.com/dictionary/manifold'])
R('A1753','倍数、重数或方面数量，和实际折纸次数区分','-FOLD：几份那么多，或分成几个方面','twofold → threefold → fourfold → tenfold；manifold 从许多重走向多样及专门名。',
 '先拿具体数字算倍数，再看双重目的这类方面数量。实际把纸折几次是另一种表达，不能拿折纸层数替代倍数词义。',
 '古英语 -feald 等 → -fold；数词 + -fold；many 的旧材料 → manifold。相关复合词不少由古英语延续，不是今天全部新造。',
 [['明确倍数与方面数量','twofold · threefold · fourfold · tenfold'],['多样及专业名词','manifold']],
 '10 到 20 是变成两倍；fourfold 不等于 four folds；manifold 也不是 mani 手加折叠。',
 'The count rose twofold, then later reached tenfold its original size.\n\n数量先变成两倍，后来达到最初的十倍。','twofold threefold fourfold tenfold manifold')

Pi=[['古法语 pinte → 中古英语 pinte → pint','容量单位名称'],['更早可能联系标记容量的拉丁画、涂记材料','来源解释有重构成分，现代单位值须看制式']]
W('pint','/paɪnt/','品脱〔容量单位〕；一品脱啤酒〔英式常用〕',
 '一瓶牛奶、一杯啤酒可以按 pint 计量。名字一样，英制与美制容量不同，所以先看配方、容器采用哪套单位。',
 '借古法语 pinte，远源可能接拉丁 picta 画、标记的材料，联系容器容量刻记的解释含重构。现代读 /paɪnt/，不按 mint 的短元音读。',Pi,
 '英制一品脱约 568 毫升，美制液量一品脱约 473 毫升；另有美制干量品脱，不能把所有 pint 都换成同一个毫升数。a pint 也常特指一品脱啤酒。',
 'a pint of milk；a pint of beer；an imperial pint；a US liquid pint。',
 'pint 是容量，不是重量；一品脱不同物质不保证同样重。读音也不是 /pɪnt/。',
 ('The recipe uses a pint of milk.','配方用一品脱牛奶。'),('An imperial pint is larger than a US liquid pint.','英制一品脱大于美制液量一品脱。'),sources=['https://en.wiktionary.org/wiki/pint#English','https://www.oxfordlearnersdictionaries.com/definition/english/pint','https://www.nist.gov/pml/owm/si-units-volume'])
R('B3255','容量单位及相应容器、饮品数量','PINT：先问哪套品脱，再谈是多少','pint 的日常搭配从牛奶、啤酒进入。',
 '单位名称一眼认识还不够，英制、美制液量和干量有区别。学习例句时把量与被量的东西分开。',
 '古法语 pinte → pint；更早可能接画记、容量标记材料；读 /paɪnt/。',
 [['容量与一份饮品','pint']],
 '容量不等于重量；英制品脱与美制液量品脱数值不同。',
 'The bottle is marked in litres and pints.\n\n瓶子上标有升和品脱两种容量。','pint')
R('A2386','被某介质承载、传播，或由它带来','-BORNE：搭着什么过来，就由什么携带','airborne、waterborne 分别看空气、水的承载传播。',
 'borne 接 bear 的承受、携带材料。感染传播是一种场景，空中尘粒、水中物质也能谈相应承载关系。',
 'bear 的过去分词 borne；air、water 等 + borne 构成性质词。与 born 出生的拼法对照。',
 [['承载、传播介质','airborne · waterborne']],
 '-borne 的 e 保留；airborne 不只等于飞行中的飞机，waterborne 也不只等于一种疾病。',
 'The glossary contrasts airborne particles with waterborne contaminants.\n\n词汇表对照空气携带的颗粒与水传播的污染物。','airborne waterborne')

Uc=[['cap 盖、上限或授帽材料 → capped','加盖、受上限约束；体育代表队出场等固定义'],['un- + capped → uncapped；uncap 的分词也同形','无盖、无上限；未获出场记录；已取下盖子']]
W('uncapped','/ʌnˈkæpt/','无盖的；不设上限的；尚无代表队出场记录的',
 '瓶子没盖、费用没有最高限额、球员还没代表队出场，都可能是 uncapped。cap 在不同领域里圈定的东西不一样。',
 'un- + capped 可否定有盖、受限、获出场记录的状态；uncap 去盖动词的过去分词也写 uncapped。双写 p，-ed 在 /p/ 后读 /t/。',Uc,
 'an uncapped bottle 无盖的瓶子；uncapped costs 无上限费用；an uncapped player 无相关代表队出场记录的球员。体育须看 national、international 等具体范围。',
 'an uncapped bottle；uncapped costs；an uncapped player。',
 'uncapped 不等于经济上免费：费用不设上限，与不收取费用恰是不同概念。球员 uncapped 也不表示从未打过任何比赛。',
 ('The pen had been left uncapped on the desk.','钢笔被敞着笔尖留在桌上。'),('The squad includes three uncapped players.','名单里有三名尚无相关代表队出场记录的球员。'))
R('B4604','盖住、设限或授帽记录，否定时分清场景','CAPPED：盖、上限、代表队出场，不只一顶帽子','capped → uncapped。',
 '盖子限制开口，数量上限限制额度，体育 cap 则取代表队授帽传统。uncapped 的否定跟着整词义项走。',
 'cap + -ed 双写 p → capped；un- 否定或 uncap 的分词 → uncapped；末尾 -ed 读 /t/。',
 [['加盖、限制与否定状态','capped · uncapped']],
 'uncapped player 不是完全没参加比赛；uncapped costs 也不是免费。',
 'The article explains capped and uncapped in both pricing and sport.\n\n文章解释了 capped 和 uncapped 在定价与体育中的不同用法。','capped uncapped')
R('A1822','拉丁性质、状态名词材料，随整词固定下来','-ITUDE：把一种性质或关系，当成状态来谈','multitude 看数量众多；servitude 看受支配、奴役状态。',
 '两词不靠中文统一成一个模糊的度。前半指出多或受役关系，词尾帮助形成状态、集合等名词。',
 '拉丁 -tudo、-itudo 等名词材料，经法语等进入英语 -itude 形式；不少是整体借入，不是现代英语任意加尾。',
 [['众多与受役状态','multitude · servitude']],
 'multitude 常可指一大群、许多，servitude 指受役状态；不是所有 -itude 都能按同一种可测量尺度理解。',
 'The reading moves from a multitude of examples to a discussion of servitude.\n\n阅读从大量例子延伸到对受役状态的讨论。','multitude servitude')
R('B4324','几何相关的性质与表达方式','GEOMETRIC：按形状、空间关系与几何结构来读','geometric、geometrical → geometrically。',
 '图案由规则形状组成，可以说 geometric；数学里也有专门的几何、等比等固定搭配。后缀长短不自动产生截然不同的两门知识。',
 '希腊 geo- 地 + metron 度量等 → geometry 词族；geometric、geometrical 为相应形容词；-ly 成方式副词。',
 [['几何性质、形式与方式','geometric · geometrical · geometrically']],
 'geometric 和 geometrical 常有重叠，但固定搭配如 geometric mean、geometric progression 按整词组学习。',
 'The geometric pattern is described geometrically using circles and lines.\n\n这个几何图案用圆和直线作几何描述。','geometric geometrical geometrically')

Ag=[['希腊 agora 集会、市集场所 + 恐惧材料','agoraphobia 的历史命名'],['agora- + -phobic → agoraphobic','现代涉及难以离开、难获帮助情境的恐惧相关性质']]
W('agoraphobic','英 /ˌæɡərəˈfəʊbɪk/；美 /ˌæɡərəˈfoʊbɪk/','广场恐惧相关的；患广场恐惧症的',
 '名字里有市集、广场，现代重点却不只是空间空旷，而是身处某些情境时害怕难以离开、出了事得不到帮助。',
 'agora- 集会、市集等 + -phobic 恐惧相关；对应 agoraphobia。历史名称不能代替现代范围，所以商场、公共交通等也可能进入讨论。',Ag,
 'agoraphobic symptoms 广场恐惧相关症状；agoraphobic avoidance 相应回避行为；形容人时也可用，清楚表述可说 a person with agoraphobia。',
 'agoraphobic symptoms；agoraphobic avoidance。',
 'agoraphobic 不等于只是不爱热闹、性格内向；introverted 说性格取向，不自动有这种恐惧。',
 ('The article explains agoraphobic avoidance in everyday situations.','文章解释了日常情境中的广场恐惧相关回避行为。'),('The course distinguishes agoraphobic fear from a simple dislike of crowds.','课程把广场恐惧相关的害怕与单纯不喜欢人群区分开。'),sources=['https://en.wiktionary.org/wiki/agoraphobic#English','https://www.nhs.uk/mental-health/conditions/agoraphobia/overview/'])
R('A1724','恐惧、厌恶或排斥相关，整词决定临床与社会含义','-PHOBIC：可能说恐惧，也可能说偏见、排斥','agoraphobic 与 homophobic、xenophobic、transphobic 的性质不能一概而论。',
 '词尾有恐惧的历史材料，现代社会词常说敌意、偏见，不要求当事人身体上真的害怕。临床恐惧词则另按具体症状范围理解。',
 '希腊 phobos 恐惧等 → -phobic；与 -phobia 名词形式对照；前半材料和整词固定语境决定对象。',
 [['临床恐惧相关','agoraphobic'],['社会偏见、排斥语境','homophobic · xenophobic · transphobic']],
 '不能只因词尾相同，就把社会偏见都当同一种医学诊断；agoraphobic 也不只表示不喜欢广场。',
 'The glossary explains why agoraphobic and xenophobic require different contexts.\n\n词汇表解释了为什么 agoraphobic 与 xenophobic 需要按不同语境理解。','agoraphobic homophobic xenophobic transphobic')

Sr=[['古英语 spora、spura → 中古英语 → spur','马刺；脚跟上用来催马的器具'],['英语 spur 名词、动词及形状比喻','促进、激励；支线、突出部等']]
W('spur','英 /spɜː/；美 /spɜːr/','马刺；促使、激励；刺激因素；支线、突出部',
 '马刺的旧用途是催动，从这个画面转到“给行动一个推动”。山脊、铁路线伸出的支部，又可以按突出形状叫 spur。',
 '古英语 spora、spura 等延续到现代，属日耳曼语马刺词族。催动比喻与突出部形状的发展分开理解，不把铁路说成真的在催马。',Sr,
 'spur someone on 鼓励某人继续；spur growth 促进增长；a spur to action 行动的推动因素；a rail spur 铁路支线；on the spur of the moment 一时冲动、临时起意。',
 'spur someone on；a spur to action；on the spur of the moment。',
 'spur 与 spear 长矛不同；spur someone on 主要说推动，不保证是责备或伤害。',
 ('The encouraging message spurred her on.','鼓励的信息推动她继续努力。'),('We decided to visit the museum on the spur of the moment.','我们临时起意，决定去博物馆。'))
R('B3871','催马器具进入推动比喻，突出形状进入支部名','SPUR：给行动一点推动，或从主体伸出一支','spur 的动作、刺激因素、支线依不同画面理解。',
 '催动和形状是两条现代义的联想路径。把普通搭配 spur on、on the spur of the moment 先抓住，读文章最实用。',
 '古英语 spora、spura 等 → spur；名词转动词，另有突出部、支线等形状发展。',
 [['马刺、推动与突出支部','spur']],
 'spur 不是 spear；on the spur of the moment 说临时起意，不是在某个马刺旁边。',
 'A sudden idea spurred us to act on the spur of the moment.\n\n突然的想法推动我们临时行动起来。','spur')

if __name__=='__main__':save('continuation_20261030_oz',ROOTS,WORDS)
