"""Useful informal words, common animals and selected science names."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
import json
from pathlib import Path
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={'B3198':['silica','silicate','borosilicate']}
W('newbie','英 /ˈnjuːbi/；美 /ˈnuːbi/','新手；刚加入的人〔口语〕',
 '刚进论坛、刚学游戏、刚开始一个爱好，还在摸索规则的人，可以自称 newbie，语气通常随意。',
 '确切形成有争议，可能是 newie 加入 b 的变化，也可能与 new boy、new beginner 等缩短有关。能认出 new 的新，但不把 -bie 强定为古代某个独立词根。',
 [['new 相关口语人物形式','newie 变形、较长称呼缩短等分析并存'],['固定名词 newbie','新手、新加入者']],
 'a complete newbie 完全的新手；a newbie to coding 编程新手；a newbie in the group 群里新来的人。也常用于自谦。',
 'a total newbie；help the newbies。','newcomer 较中性，重在刚来；newbie 更口语，也常暗示还不熟练。对别人用时要看说话关系、语气。',
 ('I’m a complete newbie to gardening.','我对园艺完全是个新手。'),('The forum has a guide for newbies.','这个论坛有一份新手指南。'),sources=['https://en.wiktionary.org/wiki/newbie#English','https://www.etymonline.com/word/newbie'])
W('mongrel','/ˈmʌŋɡrəl/','混种狗；混杂的；杂种〔对人使用时贬损〕',
 '一只狗的祖先来自不同品种，可以叫 mongrel；现代也有更中性的 mixed breed 说法。用来骂人时，语气会很恶劣。',
 '中古英语 mongrel，前部接混合、混杂的旧 mong、gemang 材料，后部 -rel 是小称、带评价的人物或事物词尾。',
 [['旧 mong、gemang 混合材料 + -rel','形成混种、混杂的名称'],['现代 mongrel 的动物及引申义','混种狗；混杂的；带贬损的称人用法']],
 'a friendly mongrel 一只友好的混种狗；a mongrel dog 混种狗。谈人或族群时可能成为侮辱，词义不能照动物语境当中性。',
 'adopt a mongrel；a mongrel dog。','mixed breed 是狗的较中性描述；mongrel 对狗可以是普通叫法，对人却可能带强烈贬意。',
 ('They adopted a friendly mongrel from the shelter.','他们从收容所领养了一只友好的混种狗。'),('The dog was a small mongrel with a curly tail.','那是一只尾巴卷卷的小混种狗。'))
W('cockerel','英 /ˈkɒkərəl/；美 /ˈkɑːkərəl/','小公鸡、年轻公鸡',
 'hen 是母鸡，cock、rooster 是公鸡；年纪还小的公鸡，就可以叫 cockerel。',
 '中古英语 kokerel 等形式延续；对应 cock 公鸡与 -erel、-rel 小称材料。它是年轻雄鸡的固定名称。',
 [['cock + 小称 -erel／-rel','公鸡名称加年轻、小称关系'],['中古英语 kokerel → cockerel','年轻公鸡']],
 'a young cockerel 一只小公鸡；a cockerel crowing 小公鸡啼叫。英式农场、儿童故事等场景里常见。',
 'a farmyard cockerel；hear a cockerel crow。','chick 是小鸡，未必指雄性；cockerel 明确是年轻公鸡。hen 则通常说母鸡。',
 ('The cockerel began to crow at dawn.','小公鸡天亮时开始啼叫。'),('The farmer kept the young cockerel with the hens.','农夫把那只小公鸡和母鸡养在一起。'))
W('borosilicate','英 /ˌbɔːrəʊˈsɪlɪkət/；美 /ˌbɔːroʊˈsɪlɪkət/','硼硅酸盐；硼硅的〔材料名中〕',
 '玻璃杯、实验室烧杯的标签上，borosilicate glass 就是硼硅玻璃；前半给硼，后半给硅酸盐的材料关系。',
 'boro- 硼相关 + silicate 硅酸盐。boro- 联系 boron、borax 的近代化学命名词族，完整复合用于矿物、玻璃等名称。',
 [['boro- + silicate','硼相关材料 + 硅酸盐'],['borosilicate 的材料用法','硼硅酸盐；硼硅玻璃等名称']],
 'borosilicate glass 硼硅玻璃；a borosilicate beaker 硼硅玻璃烧杯。作材料修饰语时，后面常省略或出现 glass。',
 'a borosilicate glass tube；borosilicate materials。','boron 是元素硼，silicate 是硅酸盐类，borosilicate 是二者结合的材料名称；先分清元素和材料。',
 ('The laboratory uses borosilicate glass beakers.','实验室使用硼硅玻璃烧杯。'),('The label identifies the cup as borosilicate glass.','标签注明这个杯子是硼硅玻璃制品。'))
W('glutamate','/ˈɡluːtəmeɪt/','谷氨酸盐、谷氨酸酯；谷氨酸〔生理语境常用译名〕',
 '化学里是谷氨酸对应的盐、酯等形式；读脑科学资料时，也常把 glutamate 当神经递质名称来谈。先看所处语境。',
 'glutamic acid 谷氨酸的词基 + 化学词尾 -ate。glutamic 词族更早与 gluten 面筋、黏性蛋白的名称有关，属于近代科学命名的词族。',
 [['glutamic acid 相关词基 + -ate','形成盐、酯等化学名'],['glutamate 的化学、生理语境','谷氨酸盐或酯；神经信号相关物质名称']],
 'glutamate signalling 谷氨酸信号传递；monosodium glutamate 谷氨酸钠；glutamate receptors 谷氨酸受体。',
 'a glutamate receptor；glutamate metabolism。','glutamine 是谷氨酰胺，glutamate 是谷氨酸盐等形式；末尾 amine、ate 反映不同结构、命名关系，不能互换。',
 ('The researchers studied glutamate signalling in the brain.','研究人员研究了脑内的谷氨酸信号传递。'),('The glossary gives MSG as the abbreviation for monosodium glutamate.','词汇表注明，MSG 是谷氨酸钠的缩写。'),sources=['https://en.wiktionary.org/wiki/glutamate#English','https://www.etymonline.com/word/glutamate','https://en.wiktionary.org/wiki/glutamic'])
W('ethylene','/ˈeθɪliːn/','乙烯',
 '塑料原料、植物成熟的科普里都可能遇到它：ethylene 是乙烯，一种简单气体，也是植物的信号物质。',
 '十九世纪以 ethyl 乙基相关名 + -ene 形成，受到 methylene 等已有名称类比影响；现代也可从 eth- 与 -ylene 这组词形来认。',
 [['ethyl + -ene 的近代命名','沿已有化学名称类比形成'],['ethylene','乙烯；在植物信号等领域又有重要作用']],
 'ethylene gas 乙烯气体；ethylene production 乙烯生产；ethylene and fruit ripening 乙烯与果实成熟。其分子式是 C2H4。',
 'an ethylene molecule；ethylene signalling。','polyethylene 是聚乙烯材料，ethylene 是乙烯单体；poly- 指许多单元接成聚合物，二者的物质形态不同。',
 ('The factory uses ethylene to make polyethylene.','工厂用乙烯制造聚乙烯。'),('The class discussed ethylene’s role in fruit ripening.','课堂上讨论了乙烯在果实成熟中的作用。'),sources=['https://www.etymonline.com/word/ethylene','https://en.wiktionary.org/wiki/ethylene#English','https://extension.psu.edu/keeping-produce-fresh-best-practices-for-producers'])
W('propylene','/ˈprəʊpɪliːn/；美 /ˈproʊpɪliːn/','丙烯',
 '先把它放到塑料原料这一场景：许多丙烯单元接起来，可以形成 polypropylene 聚丙烯。',
 '十九世纪名称由法语 propionique 丙酸相关材料与 -ylene 形成，后来进入英语。现代词形与 propyl、prop- 三碳命名词族对应，但实际名称有自己的历史。',
 [['propionique 相关材料 + -ylene','近代化学名称的类比形成'],['propylene','丙烯，现代也称 propene']],
 'propylene gas 丙烯气；propylene production 丙烯生产；polypropylene 聚丙烯。丙烯分子式 C3H6。',
 'a propylene molecule；propylene and polypropylene。','propylene 是丙烯，polypropylene 是聚丙烯；ethylene 又是另一个二碳物质名，不能因末尾相似而互换。',
 ('Polypropylene is made from propylene monomers.','聚丙烯由丙烯单体制成。'),('The textbook gives C3H6 as the formula for propylene.','课本给出了丙烯的分子式 C3H6。'))
W('phage','/feɪdʒ/','噬菌体',
 '一种感染细菌的病毒。长词 bacteriophage 日常在微生物学里常直接缩成 phage，意思仍是噬菌体。',
 'bacteriophage 的截短，保留后部 -phage。这个后部来自希腊吃、吞食材料，旧名称借吃细菌的画面，现代实际说感染关系。',
 [['bacterio- 细菌 + -phage 吃者','形成 bacteriophage 的命名画面'],['bacteriophage → phage','完整词缩短成常用科研名称']],
 'a phage that infects bacteria 感染细菌的噬菌体；phage research 噬菌体研究；different phages 不同噬菌体。',
 'a phage particle；phage infection。','macrophage 是巨噬细胞，phage 作为独立短词却通常指噬菌体；同一吃材料，不表示同一类生物。',
 ('The researchers identified a phage that infects the bacterium.','研究人员鉴定出一种感染该细菌的噬菌体。'),('The sample contained several types of phage.','样本中含有几种噬菌体。'))
W('silica','/ˈsɪlɪkə/','二氧化硅、硅石',
 '沙和石英中常见的硅氧化合物，也出现在 silica gel 硅胶这个名称中；它与元素 silicon 硅是不同层面的物质名称。',
 '十九世纪初采用拉丁 silex、词干 silic- 燧石材料，仿 alumina 等氧化物名称形成 silica。现代成为二氧化硅的常用名称。',
 [['拉丁 silex、silic- 燧石 + 近代物质名形式','沿氧化物名称模式命名'],['silica','二氧化硅，化学式 SiO2']],
 'silica sand 硅砂；silica gel 硅胶；silica in quartz 石英中的二氧化硅。通常作为不可数物质名。',
 'a silica structure；silica particles。','silicon 是元素硅，silica 是二氧化硅，silicate 是硅酸盐类名称；三个近形词分别记物质层次。',
 ('Quartz is composed of silica.','石英由二氧化硅组成。'),('The packet contains silica gel.','小包里装有硅胶。'),sources=['https://www.oxfordlearnersdictionaries.com/definition/english/silica','https://en.wiktionary.org/wiki/silica#English'])
W('silicate','/ˈsɪlɪkeɪt/ 或 /ˈsɪlɪkət/','硅酸盐；硅酸盐矿物',
 '硅、氧与其他成分结合形成的一大类矿物、化合物名称；岩石、玻璃、陶瓷资料里常见。',
 'silicic acid 硅酸相关词基 + -ate 盐等化学名后缀，远接拉丁 silex、silic- 燧石。现代类别范围需要按化学、矿物名称理解。',
 [['silicic acid 相关词基 + -ate','形成硅酸盐类名称'],['silicate 的物质、矿物用法','硅酸盐；含相应结构的矿物']],
 'silicate minerals 硅酸盐矿物；sodium silicate 硅酸钠；borosilicate glass 硼硅玻璃。这个名词有 /eɪt/、/ət/ 两类常见词尾读法。',
 'a silicate mineral；silicate structures。','silica 是二氧化硅，silicate 是更广的硅酸盐类；两词不能仅因都含 silic- 就随意互换。',
 ('Silicate minerals make up much of the earth’s crust.','硅酸盐矿物构成地壳的很大一部分。'),('The textbook compares silica with several silicates.','课本把二氧化硅与几种硅酸盐作了比较。'),sources=['https://en.wiktionary.org/wiki/silicate#English','https://www.oxfordlearnersdictionaries.com/definition/english/silicate'])
R('A1923','有关、具有某种性质；近代形容词命名材料','-ACEOUS：具体性质由前面的旧词干决定',
 'sebaceous 说皮脂相关，curvaceous 说曲线丰满；相近末尾形成形容词，但不能只背成同一种外观。',
 '多词联系拉丁 -aceus 等形容词材料及英语 -ous，也有近代类比造词和与 -acious 相互影响的形式。各词的构成不必完全一样。',
 'sebum 皮脂相关词干 → sebaceous；curve 相关词形 + 形容词模式 → curvaceous。',
 [['皮脂相关性质','sebaceous'],['曲线外形','curvaceous']],
 'sebaceous glands 是皮脂腺；curvaceous 可形容曲线形态。后部给形容词关系，具体对象仍由前部和搭配决定。',
 'The diagram labels the sebaceous glands in the skin.\n\n图示标出了皮肤中的皮脂腺。','sebaceous curvaceous')
R('A1806','织物；转用为生物组织','HISTO-：像织物那样组织在一起，后来成为组织学材料',
 '组织由细胞等结构构成，histo- 的旧织物画面帮助记住组织这一研究对象；histology 是组织学。',
 '来自希腊 histos 织物、织成物等，近代生物学转用为组织。相关组织材料也进入 histidine、histamine 等科学命名词族。',
 'histo- + -logy → histology；histamine 按 histidine 的部分词形 + amine 命名，是相邻词族的另一条组合。',
 [['组织研究','histology'],['相关物质名称对照','histamine']],
 'histology 的对象是生物组织，histamine 是具体信号物质；同族前部不把学科名和物质名变成同义词。',
 'The histology class examined the structure of tissue.\n\n组织学课观察了组织结构。','histology histamine')
R('A2102','谷氨酸相关的化学词族材料','GLUTA-：把盐类、酰胺等关系接到谷氨酸词族上',
 'glutamate 是谷氨酸盐等名称，glutamine 是谷氨酰胺；前部相近，后部对应的化学关系不同。',
 '与 glutamic acid 谷氨酸及 gluten 面筋、黏性蛋白名称相连；更早 gluten 接拉丁胶、黏性物质材料。现代名称按科学结构关系固定。',
 'glutamic acid 相关词基 + -ate → glutamate；gluta- 与相应酰胺命名材料 → glutamine。gluten 是相邻命名来源，不是这些物质的同义词。',
 [['相关蛋白名称来源','gluten'],['谷氨酸盐、谷氨酰胺对照','glutamate · glutamine']],
 'glutamate、glutamine、gluten 分别是不同物质或物质类，不能因都有 glut- 就混写成同一个成分。',
 'The glossary compares glutamate with glutamine.\n\n词汇表对照了谷氨酸盐与谷氨酰胺。','gluten glutamate glutamine')
R('A2058','承载、携带者','-FER：让前面的东西被承载、带着',
 'aquifer 最直观是承载水的地层：地下的水存储、流动在其中；不是表面随便一滩水。',
 '来自拉丁 -fer 承载者，联系 ferre 带、承载。aquifer 借法语 aquifere 含水的等相关形式，后用为地层名。',
 'aqui- 水 + -fer 承载者 → aquifer；这里字面线索是含水、承载水，现代完整名称进一步限定地质结构。',
 [['地下含水地层','aquifer']],
 'aquifer 是能储存、传输地下水的含水层，不等同于一条地下河；前部水、后部承载只是命名起点。',
 'The town draws water from an underground aquifer.\n\n镇上从地下含水层取水。','aquifer')
R('A2306','乳房','MAMMO-：前部给器官，后部区别成像方法和记录',
 'mammography 是乳腺 X 线成像的方法，mammogram 常是这项检查得到的影像，也可指一次检查。',
 '来自拉丁 mamma 乳房，经医学拉丁等作为 mammo- 组合材料；-graphy 与 -gram 分别给过程、记录结果。',
 'mammo- + -graphy → mammography；mammo- + -gram → mammogram。',
 [['成像方法、技术','mammography'],['影像或一次检查','mammogram']],
 'mammogram 里的 -gram 是记录，不是重量克；mammography 也不是所有乳房相关检查的通称。',
 'The radiologist reviewed the mammogram.\n\n放射科医生查看了乳腺 X 线影像。','mammography mammogram')
R('A1888','硼相关的科学材料','BORO-：硼与硅酸盐两部分，合成硼硅材料名称',
 'boron 是元素硼；silicon、silica、silicate 分别看硅、二氧化硅和硅酸盐，borosilicate 才把硼与硅酸盐关系接起来。',
 'boro- 与 borax 硼砂、boron 硼等近代命名词族相连；复合 borosilicate 的后半接硅酸盐，来源又联系拉丁燧石材料。',
 'boro- + silicate → borosilicate；silicon、silica、silicate 是理解组合词另一半的基础对照，不都由 boro- 派生。',
 [['硼的基础名称','boron'],['硅材料基础对照','silicon · silica · silicate'],['两部分相连的材料','borosilicate']],
 '元素名不等于材料名；硼硅玻璃、纯硅、二氧化硅不是同一种东西，词的每一半都有作用。',
 'The cup is made of borosilicate glass.\n\n这个杯子由硼硅玻璃制成。','boron silicon silica silicate borosilicate')
R('A2197','眼','OPHTHALMO-：把学科、医生的领域限定到眼',
 'ophthalmology 是眼科学、眼科，ophthalmologist 是眼科医生；先把长前部认成眼，再读后面的学科和人物。',
 '来自希腊 ophthalmos 眼，进入医学拉丁、近代学术词，形成 ophthalmo- 组合。ph、th 在词中有各自的历史拼写。',
 'ophthalmo- + -logy → ophthalmology；相应人物后部 -logist → ophthalmologist。',
 [['学科、科室与医生','ophthalmology · ophthalmologist']],
 'ophthalmologist 是眼科医生名称；配镜、验光等相关职业还有各自称呼，不能只因都与眼有关就互换。',
 'The ophthalmologist explained the eye examination.\n\n眼科医生解释了这次眼部检查。','ophthalmology ophthalmologist')
R('A2075','手','CHIRO-：用手操作的旧材料，进入整脊体系名称',
 'chiropractic 是以相应手法操作为特点的体系名称；chiropractor 是从业者。手的命名线索，并不把所有手工治疗都归成同一职业。',
 '接希腊 kheir 手，词干 chir-，与实践、操作的相关材料形成近代 chiropractic；人物名又在英语中形成。',
 'chiro- 手 + practic- 操作、实践 → chiropractic；再形成 chiropractor。',
 [['体系与人物','chiropractic · chiropractor']],
 '这是一组具体名称；理解词根里的手，不等于仅凭名称判断某种方法的疗效或职业范围。',
 'The article explains the term chiropractic and the title chiropractor.\n\n文章解释了 chiropractic 这个名称以及 chiropractor 这个职业称谓。','chiropractic chiropractor')
R('A2213','粥状、糊状的旧材料','ATHERO-：从粥样外观，理解动脉粥样硬化的命名',
 'atherosclerosis 的前部用了像粥、糊状物的旧名称，后部说硬化；现代术语关心动脉壁的粥样斑块与变化。',
 '来自希腊 athare 粥、糊状物，近代医学借其形象描述某类沉积；与 sclero- 硬、-osis 状态等材料合成疾病名称。',
 'athero- 粥样 + sclerosis 硬化 → atherosclerosis。旧食物画面是外观类比，不是说血管里真的有粥。',
 [['固定医学名称','atherosclerosis']],
 'athero- 给出粥样外观线索，sclero- 给出硬化关系；分开认这两部分，名称会更清楚。',
 'The diagram illustrates the changes associated with atherosclerosis.\n\n图示展示了与动脉粥样硬化相关的变化。','atherosclerosis')
R('A1852','冰冷、低温','CRYO-：把过程、设备与低温条件联系起来',
 'cryogenic 描述低温相关的性质、技术；cryopreservation 是低温保存，把保存对象放到这种条件下。',
 '来自希腊 kryos 冰冷、霜冻，进入近代低温科学、生物保存等名称。',
 'cryo- + genic 相关材料 → cryogenic；cryo- + preservation 保存 → cryopreservation。',
 [['低温相关性质','cryogenic'],['低温保存过程','cryopreservation']],
 'cryogenic 用于低温科学的特定范围，日常说冷更常用 cold；cryopreservation 则强调保存目的。',
 'The laboratory uses cryogenic storage for some samples.\n\n实验室对部分样本采用低温储存。','cryogenic cryopreservation')
R('A2113','长期、持续，来自 permanent 的截短','PERMA-：把长久保持的感觉放到名称前面',
 'permafrost 是多年冻土，permalink 是供长期引用的固定链接；持续、长久是两者命名的共同线索。',
 '由 permanent 长久的截短成近代构词材料 perma-，进入不同科学、网络等名称。',
 'perma- + frost → permafrost；perma- + link → permalink。现代词的技术定义各自固定，不只按永远两个字理解。',
 [['长期冻结状态','permafrost'],['网页引用名称','permalink']],
 'permafrost 的多年冻结有具体地学定义；permalink 的命名表达持续可引用的用途，不是网站绝不可能变化的保证。',
 'Use the permalink when citing the article.\n\n引用这篇文章时，请使用它的固定链接。','permafrost permalink')
R('A2219','小称、带评价的名词形式','-REL：同一类旧词尾，在不同词里有不同语气',
 'cockerel 说年轻公鸡，偏小称；mongrel 说混种等，历史上又带评价性质。不能把每个结尾都统一译成可爱的小。',
 '中古英语 -rel、-erel 等联系古法语 -erel、-erelle，小称、评价用途随具体完整词发展。',
 'cock + -erel → cockerel；旧 mong 混合材料 + -rel → mongrel。前者指年龄、类别，后者的现代语气还要看对象。',
 [['年轻动物名称','cockerel'],['混种及带评价用法','mongrel']],
 'mongrel 谈狗可作普通名称，谈人可能强烈贬损；cockerel 则是正常的年轻公鸡称呼，不自动带同样评价。',
 'The cockerel watched the friendly mongrel cross the yard.\n\n小公鸡看着那只友好的混种狗穿过院子。','cockerel mongrel')
R('B2604','公鸡、公鸟；相关动作及粗俗身体称呼','COCK：先认公鸡，再分清各词和各场景的用法',
 '公鸡昂首挺胸的画面能帮助记 cocky 自负；cockerel 是年轻公鸡，peacock 是孔雀的雄鸟名称。cock 本身另有动作、粗俗身体用法。',
 '公鸡义继承古英语 cocc 等，可能拟鸟叫，也受法语相关词影响；后续人物评价、动作和身体隐喻分别发展，另有同形词来自不同路线。',
 'cock → cockerel〔小称〕、cocky〔相应性质〕；旧 pea 孔雀材料 + cock 公鸟 → peacock。cocktail 的来源有争议，不定为公鸡的直接派生。',
 [['公鸡与年轻公鸡','cock · cockerel'],['相关鸟名、评价','peacock · cocky'],['同词的动作、粗俗身体分支','cock']],
 'peacock 的 pea 是旧孔雀名称材料；cock 的身体粗俗义、歪头等动作义都要按语境选。不要用一个公鸡中文义硬译所有例子。',
 'The cockerel stood beside the hens while the peacock crossed the garden.\n\n小公鸡站在母鸡旁边，那只雄孔雀穿过了花园。','cock cockerel cocky peacock')
ROOTS[-1]['exclude']['cocktail']='词源解释未定，不作为 cock 公鸡义直接派生的确定证据。'
ROOTS[-1]['exclude']['chicken']='基础鸡类名称已单独精讲；此处集中于 cock 的透明派生及复合。'
R('A2200','近代化学命名中抽出的词形材料','-YLENE：看完整化学名称，也看词尾怎样从旧名中被抽出',
 'ethylene 是乙烯，propylene 是丙烯；前面的材料与二碳、三碳命名词族有关，后部反映近代化学命名的类比。',
 '从 methylene、ethylene 等旧名称中抽出相似词形；其中 -yl 与 -ene 原本也有各自的命名历史。后来的 -ylene 不能简单当一个古代独立物质名。',
 'ethyl + -ene → ethylene；propionique 丙酸相关材料 + -ylene → propylene；再加 poly- 形成 polyethylene、polypropylene。',
 [['常见单体名称','ethylene · propylene'],['对应聚合材料','polyethylene · polypropylene']],
 '单体与聚合物不互换；-ylene 的历史类比也不替代现代完整结构名称，具体仍看 ethylene、propylene。',
 'The factory makes polyethylene from ethylene and polypropylene from propylene.\n\n工厂用乙烯制造聚乙烯，用丙烯制造聚丙烯。','ethylene polyethylene propylene polypropylene')
R('A1930','吃、吞食的命名材料','-PHAGE：借吃的画面，形成细胞或病毒名称',
 'macrophage 是巨噬细胞，能吞噬某些颗粒等；bacteriophage 的旧名像吃细菌，现代说感染细菌的病毒。',
 '经拉丁 -phagus 接希腊 phagein 吃及 phagos 等材料，现代生物学用于不同类别名称；独立 phage 再从 bacteriophage 缩短。',
 'macro- 大 + -phage → macrophage；bacterio- 细菌 + -phage → bacteriophage → phage。',
 [['吞噬细胞名称','macrophage'],['感染细菌的病毒及缩称','bacteriophage · phage']],
 'macrophage 是细胞，phage 作为独立短词通常是病毒；吃是历史命名画面，两者的实际生物过程不同。',
 'The diagram distinguishes a macrophage from a bacteriophage.\n\n图示区分了巨噬细胞与噬菌体。','macrophage bacteriophage phage')
R('A2260','少数口语名词中的类比、表达性结尾','-BIE：认固定口语词，不把末尾硬当一条万能规则',
 'newbie 是新手，freebie 是免费赠品；都短小随意，但各自的形成有不同分析，不必强画成一个先从另一个派生。',
 '现代英语从 newbie 等词可以辨认 -bie 一类形式；newbie 的更早构成未定，freebie 也可按 free 加口语过渡音、昵称式 -ie 来理解。',
 'newie 变形或较长人物称呼缩短等 → newbie〔来源有不同分析〕；free + 口语形式 → freebie。两词并列学习，不强定年代先后造成的派生关系。',
 [['新加入的人','newbie'],['免费得到的东西','freebie']],
 'newbie 有时可自谦，有时会带轻视；freebie 常是轻松的赠品叫法。这个后部不像 -er 那样能自由造一大批规则人物词。',
 'The event gave every newbie a small freebie.\n\n活动给每位新来者发了一份小赠品。','newbie freebie')
def extend_silicon_lesson():
    path=Path(__file__).resolve().parents[1]/'content/精讲/roots_continuation_20261030_mn.json'
    rows=json.loads(path.read_text())
    matches=[r for r in rows if r['id']=='B3198']
    assert len(matches)==1
    lesson=matches[0]
    for word in EXISTING_ROOT_ADDITIONS['B3198']:
        if word not in lesson['words']:lesson['words'].append(word)
        lesson.get('exclude',{}).pop(word,None)
    label='硅的氧化物、盐类与硼硅复合材料'
    if not any(row[0]==label for row in lesson['branches']):
        lesson['branches'].append([label,'silica · silicate · borosilicate'])
    note='silic- 燧石材料还形成 silica 二氧化硅、silicate 硅酸盐；borosilicate 包含另一半 boro- 硼。'
    if note not in lesson['forms']:lesson['forms']+='\n\n'+note
    path.write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
if __name__=='__main__':
    save('continuation_20261030_sr',ROOTS,WORDS)
    extend_silicon_lesson()
