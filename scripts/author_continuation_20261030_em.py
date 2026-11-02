"""-ine: distinguish a relational suffix, substance names and misleading spellings."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
I=[['拉丁 -īnus、-īna 等，经法语 -in、-ine 或直接借入英语','属于……、像……；形容词也可转成事物名'],['现代科学命名中的 -ine','沿法语物质名称传统扩用；并非所有词指同一化学类别'],['拼写相同不等于每个词同一种拆法','tangerine 接地名；labyrinthine 接迷宫；opine 常用动词另源']]
W('caffeine','/ˈkæfiːn/','咖啡因',
 '名字抓住最初研究所联系的咖啡，不等于只有咖啡才含有它；茶等也有咖啡因。',
 '借法语 caféine、德语相应咖啡物质名称等，词基是 coffee 对应的 café、Kaffee 一类词，接物质命名词尾。不是英语 calf 小牛的一段。',I[:2]+[['café、Kaffee 等咖啡词 + 物质名称词尾 → caffeine','与咖啡研究相连的物质名']],
 'caffeine content 咖啡因含量，caffeine free 不含咖啡因〔搭配〕，a source of caffeine 咖啡因来源。',
 'caffeine content；a source of caffeine；contain caffeine。',
 'caffeine 是具体物质，coffee 是饮品、咖啡原料；名称来源不代表只存在于这一种来源物。',
 ('The label lists the caffeine content.','标签列出了咖啡因含量。'),('Tea can also contain caffeine.','茶也可能含有咖啡因。'))
W('nicotine','/ˈnɪkətiːn/','尼古丁、烟碱',
 '名字不是“有毒”的直接词根，而与人名 Nicot 及烟草名称历史有关；现代指具体物质。',
 '借法语 nicotine，接与烟草传播史相连的 Jean Nicot 姓名、相关烟草名称词基和 -ine。不可按 nice 好 + tine 拆，也不是因为味道好而得名。',I[:2]+[['Nicot 人名、相关烟草名称 + -ine → nicotine','与烟草历史相连的物质名称']],
 'nicotine content 尼古丁含量，nicotine exposure 尼古丁接触，nicotine dependence 尼古丁依赖。',
 'nicotine content；nicotine exposure；nicotine dependence。',
 'nicotine 具体物质，tobacco 烟草；词源中的人名帮助记词，不把人名本身解释成现代化学性质。',
 ('The report compared nicotine levels in the samples.','报告比较了样本中的尼古丁水平。'),('The exhibit explained the history of nicotine research.','展览介绍了尼古丁研究史。'))
W('cocaine','英 /kəʊˈkeɪn/；美 /koʊˈkeɪn/','可卡因、古柯碱',
 '从古柯 coca 的名称接出的物质名；与 cocoa 可可字母近，却不是巧克力里那种原料的名字。',
 'coca 古柯 + 物质词尾 -ine，coca 更早接南美克丘亚语 kuka。词尾实际读 /eɪn/，不能看到 -ine 一律读 /iːn/。',I[:2]+[['克丘亚语 kuka → coca；coca + -ine → cocaine','植物名 → 与它相关的物质名']],
 'cocaine use 可卡因使用，cocaine trafficking 可卡因贩运，cocaine research 可卡因研究。',
 'cocaine use；cocaine trafficking；cocaine research。',
 'coca 古柯与 cocoa 可可不同；cocaine 不是 caffeine 咖啡因，不能因都带类似物质词尾就认为同一东西。',
 ('The documentary examined the history of cocaine trafficking.','纪录片考察了可卡因贩运史。'),('The article distinguished coca from cocaine.','文章区分了古柯植物与可卡因。'))
W('codeine','英 /ˈkəʊdiːn/；美 /ˈkoʊdiːn/','可待因',
 '它的 code- 不是电脑代码 code；名称往前追，抓住的是罂粟果实这个旧希腊语画面。',
 '借法语 codéine，接希腊 kṓdeia 罂粟蒴果、果头 + -ine 物质词尾；声音到英语后成为 codeine。',I[:2]+[['希腊 kṓdeia → 法语 codéine → codeine','罂粟果实名称 → 相关物质名称']],
 'codeine content 可待因含量，contain codeine 含可待因，codeine listed as an ingredient 成分表中列有可待因。',
 'contain codeine；codeine content；a medicine containing codeine。',
 'codeine 物质名与 code 编码不同；本词学习关注识别药名，不凭词尾推断与其他药物可互换。',
 ('The ingredient list included codeine.','成分表中列有可待因。'),('The researcher identified codeine in the sample.','研究者在样本中识别出可待因。'))
W('iodine','/ˈaɪədaɪn/，也有词尾 /-diːn/、/-dɪn/ 的读法','碘',
 '名字抓住碘蒸气的紫色，不是说每种含碘产品都长得紫；它是元素名，不等于一种固定配方的消毒水。',
 '接法语 iode 与 -ine，iode 更早联系希腊 ioeidḗs 紫罗兰色的。外观观察进入元素命名，英语词尾有多种读法。',I[:2]+[['希腊 ioeidḗs〔紫罗兰色〕→ 法语 iode → iodine','按蒸气颜色形成的元素名称']],
 'iodine content 碘含量，iodine in a sample 样本中的碘，an iodine solution 碘溶液。',
 'iodine content；an iodine solution；contain iodine。',
 'iodine 元素名，iodide 碘化物、碘离子相关名称；不同词形对应不同化学对象，不能只当同词拼写变化。',
 ('The textbook described the violet vapour of iodine.','课本描述了碘的紫色蒸气。'),('The analysis measured the iodine content.','分析测定了碘含量。'))
W('fluorine','英 /ˈflʊəriːn/；美 /ˈflʊriːn/，也有词尾 /-ɪn/ 等读法','氟',
 '元素名称的前半与“流”有关，经过矿物作助熔剂帮助熔炼流动的历史背景；不是英语 floor 地板。',
 '拉丁 fluor 流动等词，经萤石、助熔相关命名传统，接 -ine 形成 fluorine。不要把现代氟元素和含氟化合物当同一种东西。',I[:2]+[['拉丁 fluor 与助熔矿物名称背景 → fluorine','流动、帮助熔融的历史命名 → 元素氟']],
 'the element fluorine 元素氟，fluorine compounds 氟化合物，fluorine chemistry 氟化学。',
 'the element fluorine；fluorine compounds；fluorine chemistry。',
 'fluorine 氟元素，fluoride 氟化物或氟离子相关名称；含有相同元素不代表物质性质完全一样。',
 ('The class studied fluorine and chlorine.','班里学习了氟和氯。'),('The diagram showed a fluorine atom.','图中画了一个氟原子。'))
W('alkaline','/ˈælkəlaɪn/','碱性的、与碱有关的',
 '这里先看 alkali 碱，-ine 把它接成“碱性的”；它不是遇到 -ine 就又造出一种叫 alkaline 的药物。',
 'alkali + 形容词 -ine；alkali 较早经阿拉伯语 al-qily 等草木灰名称，因为灰与制碱历史相连。',I[:1]+[['阿拉伯草木灰相关名称 → alkali；alkali + -ine → alkaline','碱 → 碱性的']],
 'an alkaline solution 碱性溶液，alkaline soil 碱性土壤，an alkaline battery 碱性电池。',
 'an alkaline solution；alkaline soil；an alkaline battery。',
 'alkali 名词、alkaline 形容词；碱性电池说一种电池体系，不能只凭 alkaline 把任何物品推断成同等碱度。',
 ('The test showed that the solution was alkaline.','检测表明溶液呈碱性。'),('Some plants grow well in alkaline soil.','有些植物在碱性土壤中长得好。'))
W('amine','/əˈmiːn/，另有 /ˈæmiːn/ 等读法','胺；胺类化合物',
 '想氨的结构里，氮旁的氢被别的基团换掉，形成胺类的基本理解；它是一类名称，不是一瓶固定产品。',
 '由 ammonia 氨的词基接 -ine 形成 amine。现代化学中它已有明确类别意义，不能只靠音节推断所有带 -ine 的东西都是胺。',I[:2]+[['ammonia 的词基 + -ine → amine','由氨的结构关系命名的一类化合物']],
 'a primary amine 伯胺，an amine group 胺基，amine chemistry 胺化学。',
 'a primary amine；an amine group；amine chemistry。',
 'amine 胺，amide 酰胺是不同类别；amino 常见于 amino acid 氨基酸，不是三个词随意换后缀的同义词。',
 ('The diagram highlighted the amine group.','图中突出了胺基。'),('The students compared an amine with an amide.','学生们比较了胺与酰胺。'))
W('creatine','/ˈkriːətiːn/','肌酸',
 '与肌肉能量供给相关的含氮物质；名字来自“肉”，不是 create 创造加一个尾巴。',
 '接希腊 kréas 肉、属格词干 kreat-，配物质词尾 -ine，经欧洲科学命名形成 creatine。',I[:2]+[['希腊 kréas、kreat-〔肉〕+ -ine → creatine','从肉的研究背景得来的物质名']],
 'creatine in muscle 肌肉中的肌酸，creatine metabolism 肌酸代谢，creatine research 肌酸研究。',
 'creatine in muscle；creatine metabolism；creatine research。',
 'creatine 肌酸与 creatinine 肌酐名字相关而不是同一物；create 创造是另一条词源。',
 ('The chapter explains creatine metabolism.','这一章解释肌酸代谢。'),('The researchers measured creatine in the samples.','研究者测量了样本中的肌酸。'))
W('creatinine','/kriˈætəniːn/，也见末尾弱读等变体','肌酐',
 '名字比 creatine 多一段，实际指肌酸代谢有关的另一种物质；读报告时不能把这两个中文名看成同一个。',
 '经德语 Kreatinin 借入，名称由 creatine 相应词基再接物质词尾形成；命名把关系留下，但不等于化学性质、数值意义完全相同。',I[:2]+[['Kreatin → Kreatinin → creatinine','与肌酸代谢相关的另一物质名称']],
 'creatinine level 肌酐水平，a creatinine measurement 肌酐测定，creatinine in a sample 样本中的肌酐。',
 'creatinine level；a creatinine measurement；measure creatinine。',
 'creatine 肌酸，creatinine 肌酐；多出来的字母不是可忽略的拼写变体，二者要分读、分认。',
 ('The table listed the creatinine measurements.','表格列出了肌酐测定值。'),('The student confused creatine with creatinine.','学生把肌酸和肌酐混淆了。'))
W('glycine','/ˈɡlaɪsiːn/','甘氨酸',
 '名字抓住“甜”，中文的甘也帮助联想；但它是氨基酸，不是把蔗糖换了一个英文名。',
 '希腊 glykýs 甜的词基 + -ine 物质词尾。先按命名特点记住，再与物质类别分开。',I[:2]+[['希腊 glykýs〔甜〕+ -ine → glycine','以甜味特征命名的氨基酸']],
 'glycine in proteins 蛋白质中的甘氨酸，a glycine molecule 甘氨酸分子，glycine research 甘氨酸研究。',
 'a glycine molecule；glycine in proteins；glycine research。',
 'glycine 甘氨酸，不是 glucose 葡萄糖；词源都可联系甜，不代表化学上是同一类糖。',
 ('The model showed a glycine molecule.','模型展示了一个甘氨酸分子。'),('The lesson introduced glycine as an amino acid.','课程把甘氨酸作为一种氨基酸来介绍。'))
W('tyrosine','英 /ˈtaɪrəsiːn/；美 /ˈtaɪrəˌsiːn/','酪氨酸',
 'tyro- 的历史画面是奶酪，名称来自早期研究来源；不是一个新手 tyro 变成的化学物。',
 '希腊 tūrós 奶酪 + -ine，经科学命名形成 tyrosine；名称与奶酪蛋白的研究有关，不表示只存在于奶酪。',I[:2]+[['希腊 tūrós〔奶酪〕+ -ine → tyrosine','从奶酪相关研究背景命名的氨基酸']],
 'a tyrosine residue 酪氨酸残基，tyrosine in proteins 蛋白质中的酪氨酸，tyrosine metabolism 酪氨酸代谢。',
 'tyrosine in proteins；a tyrosine residue；tyrosine metabolism。',
 'tyrosine 的 tyro- 奶酪与 tyro 新手不要按拼写硬并；来源名字也不限制现代发现它的全部位置。',
 ('The diagram marked a tyrosine residue in the protein.','图中标出蛋白质中的一个酪氨酸残基。'),('The chapter compares tyrosine with other amino acids.','这一章比较酪氨酸与其他氨基酸。'))
W('epinephrine','/ˌepɪˈnefrɪn/','肾上腺素〔与 adrenaline 同一物质名〕',
 '把 epi- 上面和 nephr- 肾脏合起来，就是肾上方的命名画面；并不是“肾素”那个不同名称。',
 '希腊 epi- 在上 + nephrós 肾 + -ine 物质词尾。adrenaline 采用拉丁来源的肾上方命名，两套语言材料指向同一物质。',I[:2]+[['epi-〔上〕+ nephr-〔肾〕+ -ine → epinephrine','按肾上方器官背景命名'],['与 adrenaline 的命名对应','希腊语材料与拉丁语材料的同物异名']],
 'epinephrine and adrenaline 肾上腺素的两种英文名，epinephrine release 肾上腺素释放，epinephrine research 肾上腺素研究。',
 'epinephrine release；epinephrine research；epinephrine and adrenaline。',
 'epinephrine 与 adrenaline 是同一物质名称；相似名称 norepinephrine 则不是可以直接删几个字母就当同物。',
 ('The textbook used epinephrine, while the lecture used adrenaline.','课本用 epinephrine，讲座则用 adrenaline。'),('The diagram showed epinephrine release.','图中展示了肾上腺素释放。'))
W('adenosine','英 /əˈdenəʊsiːn/；美 /əˈdenəsiːn/','腺苷',
 '它是核苷名称；名字把腺嘌呤、核糖的命名材料压缩组合起来，不是一个人把 aden 这个动作做了。',
 '借德语 Adenosin，造词对应 adenine 的 aden-、ribose 的 -os- 和 -ine 等材料；不是只截取开头就等于独立器官腺体。',I[:2]+[['adenine、ribose 的命名片段 + 词尾 → 德语 Adenosin → adenosine','腺嘌呤与核糖组成的核苷名称']],
 'an adenosine molecule 腺苷分子，adenosine triphosphate 三磷酸腺苷〔ATP〕，adenosine signalling 腺苷信号传递。',
 'adenosine triphosphate；an adenosine molecule；adenosine signalling。',
 'adenosine 腺苷，adenine 腺嘌呤，不因开头相同就可互换；ATP 的全称还有 triphosphate 三磷酸部分。',
 ('The lesson introduced adenosine triphosphate as ATP.','课上介绍了三磷酸腺苷的简称 ATP。'),('The diagram showed an adenosine molecule.','图中展示了一个腺苷分子。'))
W('vaseline','/ˈvæsəliːn/','凡士林、矿脂〔源于 Vaseline 商标名〕',
 '原是产品商标名称，后来常被泛用来指矿脂；它不是自然界本来就有的一种叫 vase 的花瓶油。',
 'Vaseline 的造名通常解释为德语 Wasser 水的片段、希腊 élaion 油的片段和 -ine，属于混合来源商标造词。小写泛指用法与正式品牌名需分。',I[:2]+[['Wasser、élaion 等造名材料 + -ine → Vaseline','混合来源的产品商标'],['商标名的泛用','vaseline 指矿脂类物质']],
 'a jar of Vaseline 一罐凡士林品牌产品，petroleum jelly 矿脂、凡士林的通称，vaseline in a text 文本中的泛称用法。',
 'a jar of Vaseline；petroleum jelly；Vaseline as a brand name。',
 'Vaseline 商标，petroleum jelly 通称；并非所有同类产品都来自同一品牌，词源中的水不代表它就是水。',
 ('The label used the brand name Vaseline.','标签使用了 Vaseline 这个品牌名。'),('The glossary explained vaseline as petroleum jelly.','词汇表把 vaseline 解释为矿脂。'))
W('tangerine','/ˌtændʒəˈriːn/，也有前重音读法','橘、橘子的一类；橘红色',
 '名字里藏着摩洛哥港口 Tangier：过去经那边输入的橘子，名称从产运地点关系留下来；不是所有橘子都必须今天从那里发货。',
 '早有表示来自 Tangier 的 Tangerine，相应西班牙语等形式也有关；tangerine orange 后简称 tangerine。不是从 tang 酸味加一段随意音节造来。',I[:1]+[['Tangier 相关地名形容词 → tangerine orange → tangerine','丹吉尔相关的橘 → 橘子名称'],['果实颜色 → 色名','橘红色']],
 'peel a tangerine 剥橘子，tangerine peel 橘皮，a tangerine scarf 橘红围巾。',
 'peel a tangerine；tangerine peel；a tangerine scarf。',
 'tangerine 是柑橘类常用名，不是全部 citrus 的无差别名称；名称与地名相关，不是化学物质 -ine 的用法。',
 ('She peeled a tangerine for the child.','她给孩子剥了一个橘子。'),('He wore a bright tangerine scarf.','他戴着一条鲜艳的橘红围巾。'),
 sources=['https://en.wiktionary.org/wiki/tangerine#English','https://www.etymonline.com/word/tangerine'])
W('nectarine','/ˈnektəriːn/，也见末尾重音读法','油桃',
 '外皮光滑的桃类果实，名称借 nectar 甘甜饮料、神饮的甜美联想；不是橘子和桃子按字母混出来。',
 'nectar + -ine，早期相应词形有如 nectar 甘美的性质用法，再用于果实名。是甜美联想，不是把花蜜灌进桃子。',I[:1]+[['nectar + -ine → nectarine 的甘美性质名称','如 nectar 般甜美'],['性质名称 → 油桃果实名','光滑果皮的桃类']],
 'a ripe nectarine 熟油桃，nectarine slices 油桃片，nectarine skin 油桃皮。',
 'a ripe nectarine；nectarine slices；nectarine skin。',
 'nectarine 油桃，tangerine 橘的一类；两者同尾音不代表同种果实，油桃也不是普遍由桃李杂交的定义。',
 ('She sliced a ripe nectarine into the bowl.','她把一只熟油桃切进碗里。'),('The nectarine had smooth skin.','油桃表皮光滑。'))
W('turpentine','英 /ˈtɜːpəntaɪn/；美 /ˈtɜːrpəntaɪn/','松节油；某些树脂类物质〔历史、技术语境〕',
 '绘画里常见的松节油名称，往前追原与树脂有关；不是 turn 转动加 paint 油漆拼成的词。',
 '经中古英语、古法语接拉丁、希腊 terebinth 树相关树脂名称。后用于松类等树脂及其挥发油，属于整词借入、变形，不是英语刚造的药物词尾。',I[:1]+[['希腊 terebinth 树相关树脂名 → 拉丁、法语 → 中古英语 → turpentine','树脂名称沿借词演变'],['名称适用范围扩展','松类等树脂及由其得到的挥发油']],
 'a bottle of turpentine 一瓶松节油，turpentine used as a solvent 用作溶剂的松节油，the smell of turpentine 松节油气味。',
 'a bottle of turpentine；the smell of turpentine；turpentine as a solvent。',
 'turpentine 松节油，turpentine 的现代拼写不能机械等于一个常用 turpent 词根；名称历史比现代化学词尾更早。',
 ('The studio smelled of paint and turpentine.','画室里有油漆和松节油的气味。'),('The museum displayed old bottles of turpentine.','博物馆展出了旧松节油瓶。'),
 sources=['https://en.wiktionary.org/wiki/turpentine#English','https://www.etymonline.com/word/turpentine'])
W('labyrinthine','英 /ˌlæbəˈrɪnθaɪn/；美 /ˌlæbəˈrɪnθɪn/，也有 /-θaɪn/','迷宫般曲折的；错综复杂的',
 '小巷转来转去像迷宫，规章流程层层绕弯，也能说 labyrinthine；不是单纯很长，而是复杂得难找到路。',
 'labyrinth 迷宫 + 关系形容词 -ine，labyrinth 更早接希腊迷宫名。先说像迷宫的结构，再借给制度、手续等。',I[:1]+[['labyrinth + -ine → labyrinthine','与迷宫相似、有关'],['实际曲折 → 抽象复杂','通道、街区；制度、流程难理清']],
 'labyrinthine streets 迷宫般街道，labyrinthine rules 错综复杂的规则，a labyrinthine system 复杂难解的体系。',
 'labyrinthine streets；labyrinthine rules；a labyrinthine system。',
 'labyrinthine 不只 long 长，更有难以理清路线的弯绕；医学语境可指内耳迷路相关，按具体对象理解。',
 ('We wandered through the old town’s labyrinthine streets.','我们在老城迷宫般的街道间穿行。'),('The application involved labyrinthine rules.','申请涉及错综复杂的规则。'))
for word in WORDS:
    if word['word'] in {'nectarine','fluorine'}:
        word['sources'].append('https://www.etymonline.com/word/'+word['word'])
    if word['word'] in {'tyrosine','creatinine'}:
        word['sources'].append('https://www.merriam-webster.com/dictionary/'+word['word'])
R('A1982','属于、像……的形容词传统，及其物质名称扩展','-INE：先看词基和历史，不能只靠尾巴猜化学性质','关系形容词与科学物质名的历史有关，但现代用途已不同；果名、品牌名、旧借词各自追到实际来源。',
 'caffeine 咖啡、nicotine 人名、iodine 紫色、creatine 肉，各自抓住不同命名线索。-ine 可读 /iːn/、/aɪn/、/ɪn/ 等，不一刀切。',
 '拉丁 -īnus、-īna 经法语等 → 英语 -ine；关系形容词与事物名 → 化学命名扩展；有些整词在英语形成以前就带相应词尾。',
 [['关系性质与旧借词','alkaline · labyrinthine · serpentine · riverine · turpentine'],['果名与商品名','tangerine · nectarine · vaseline'],['常见物质名','caffeine · nicotine · cocaine · codeine · iodine · fluorine · chlorine · bromine · gasoline'],['生化名称与近形辨析','amine · glycine · tyrosine · creatine · creatinine · epinephrine · adrenaline · adenosine · lysine · taurine · thyroxine'],['人物等其他派生','heroine · figurine · argentine · saccharine']],
 'creatine/creatinine 肌酸肌酐；epinephrine/adrenaline 同物两名；tangerine/nectarine 不同果；opine 常用动词不按 op+-ine 拆。',
 'The labels distinguished caffeine from nicotine and creatine from creatinine.\n\n标签分别区分了咖啡因与尼古丁、肌酸与肌酐。','alkaline labyrinthine serpentine riverine turpentine tangerine nectarine vaseline caffeine nicotine cocaine codeine iodine fluorine chlorine bromine gasoline amine glycine tyrosine creatine creatinine epinephrine adrenaline adenosine lysine taurine thyroxine heroine figurine argentine saccharine')
ROOTS[-1]['exclude']['opine']='常用动词来自法语 opiner、拉丁 opīnor 表意见，不是 op 加本页词尾；同形化学名词较冷门暂略。'
if __name__=='__main__':save('continuation_20261030_em',ROOTS,WORDS)
