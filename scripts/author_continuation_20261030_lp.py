"""Oak, bee, helm and lace."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
O=[['古英语 āc → 中古英语 oke、ok 等 → oak','橡树、栎树类名称'],['树木 → 木材、颜色与气味','oak 可直接指橡木，oaky 说相应性质'],['oak + wood → oakwood','橡树林，或橡木材料；wood 的两种义都可能']]
W('oak','英 /əʊk/；美 /oʊk/','橡树、栎树；橡木',
 '活着是一棵 oak，砍作木料也叫 oak。an oak 看一棵树，made of oak 则看木材，数法和场景随之变化。',
 '承古英语 āc，经中古英语 oke、ok 等到现代 oak，属于古老的日耳曼语树名词族。不是从 okay 缩短来的。',O[:2],
 'an oak tree 橡树，an oak table 橡木桌，oak barrels 橡木桶。不同 oak 种类形态不全一样，不用一种叶片画法概括所有树。',
 'an oak tree；made of oak；oak barrels。',
 '树木义可数，材料义通常不可数；oak table 是材料前置修饰，不一定表示树形桌子。',
 ('An old oak stood in the centre of the field.','田地中央立着一棵老橡树。'),('The table is made of solid oak.','桌子用实心橡木制成。'))
W('oakwood','英 /ˈəʊkwʊd/；美 /ˈoʊkwʊd/','橡树林；橡木材料',
 'wood 可以是树林，也可以是木料，所以 oakwood 要先看是在林间走，还是用木材做东西。这一词能练会同一个后半的两种常见意思。',
 'oak + wood，古英语已有 āc wudu 相应组合。复合后保留树林、木料两类用法，不只一个中文名。',O[:1]+[['oak + wood → oakwood','橡树林；橡木材料']],
 'walk through an oakwood 穿过橡树林，oakwood furniture 橡木家具。现代材料描述里直接用 oak 也很常见。',
 'an oakwood；oakwood furniture。',
 'an oakwood 可是一片林地；木材义则通常作物质表达。wood 在这里不是树上某一根树枝。',
 ('A narrow path led through the oakwood.','一条窄路穿过橡树林。'),('The box was crafted from oakwood.','盒子用橡木制作。'))
W('oaky','英 /ˈəʊki/；美 /ˈoʊki/','像橡木的、有橡木气息的',
 '木桶会给所接触的酒带来橡木相关香气、味道，品评时 oaky 就在说这种木质气息。也可泛指像橡树、橡木的性质。',
 'oak + -y，性质后缀；在酒类品评中常说橡木接触、陈酿带来的风味。',O[:2]+[['oak + -y → oaky','橡木相关性质、气味或风味']],
 'an oaky aroma 橡木香气，an oaky flavour 橡木风味，an oaky wine 橡木气息明显的酒。',
 'an oaky aroma；an oaky flavour。',
 'oaky 不是一定有木屑，也不自动表示好喝或不好喝；它先描述风味特点和强弱。',
 ('The wine had a strong oaky aroma.','这款酒有明显橡木香气。'),('She preferred a less oaky flavour.','她更喜欢橡木风味轻一点的口感。'))
R('B3689','橡树名称，扩到木材与相应气息','OAK：树是 oak，做成桌子仍可说 oak','oak → oakwood、oaky。',
 '先分活树和木料，再看后缀：wood 可以树林或木材，-y 说相应性质、气息。',
 'āc、oke → oak；wood 树林、木材，-y 性质。',
 [['树木、林地与材料','oak · oakwood'],['相应性质与气息','oaky']],
 '树木与材料数法不同；oakwood 的 wood 有两条常见义；oaky 是风味描述，不是质量保证。',
 'The oak table stood beside a window overlooking the oakwood.\n\n橡木桌放在窗边，窗外望出去是一片橡树林。','oak oakwood oaky')
B=[['古英语 bēo、bīo → bee','蜂类名称'],['复合扩展','bumblebee 熊蜂；beehive 蜂巢；beekeeping 养蜂；beeline 直奔路线'],['另源比较：集会、比赛 bee','可能联系邻里帮助的旧词，不把拼字比赛直接编成蜜蜂比赛']]
W('bee','/biː/','蜂、蜜蜂等；〔另支〕共同活动、比赛',
 '花间采集花粉的蜂类叫 bee，日常常想到蜜蜂，但不是所有蜂都像蜜蜂一样群居产蜜。spelling bee 的 bee 却是比赛名称的另一用法。',
 '昆虫义承古英语 bēo、bīo，经中古英语到现代。集会、比赛义有邻里帮忙旧词的来源分析，不能仅因蜜蜂勤劳就把全部集会史认作昆虫比喻。',B[:1]+[B[2]],
 'a honey bee 蜜蜂，a bee on a flower 花上的蜂，a spelling bee 拼字比赛，a quilting bee 大家一起缝被子的活动。',
 'a honey bee；a spelling bee。',
 'bee 与 be 同音；常见 wasp 黄蜂等另有名称，日常混叫不代替生物分类。集会义按固定搭配认识。',
 ('A bee landed on the purple flower.','一只蜂落在紫色花上。'),('She won the school spelling bee.','她赢得了学校拼字比赛。'))
W('bumblebee','/ˈbʌmbəlbiː/','熊蜂',
 '体形较粗壮、身上常显毛茸茸，飞过时嗡嗡响的这类蜂叫 bumblebee。前半让名字带上嗡鸣的听觉印象。',
 'bumble 嗡鸣的旧动词 + bee；与较早 humbul-be 等形式相关。这里 bumble 取声音背景，不是说它飞得笨、必须靠犯错生存。',B[:1]+[['bumble + bee → bumblebee','带嗡鸣命名的蜂类']],
 'a bumblebee on a flower 花上的熊蜂，bumblebees pollinate flowers 熊蜂为花授粉。这里指动物，不展开冷门饮品同名词。',
 'a bumblebee；bumblebee pollination。',
 'bumblebee 不等于所有 honey bee；名字的声音联想也不说明它的全部飞行机制。',
 ('A bumblebee buzzed past my shoulder.','一只熊蜂嗡嗡飞过我的肩旁。'),('Bumblebees visited the flowers throughout the morning.','整个上午，熊蜂不断飞来访花。'))
W('beehive','/ˈbiːhaɪv/','蜂巢、蜂箱；忙碌场所；蜂窝式高耸发型',
 '蜂居住、繁殖的地方是 beehive，人工养蜂的箱体也这样叫。人多、活多、忙得热火朝天的地方，又像蜂巢一样。',
 'bee 蜂 + hive 蜂巢、蜂箱，中古英语已有相应复合。繁忙场所取活动形象，发型则借高耸蜂巢的外形。',B[:1]+[['bee + hive → beehive','蜂的居所 → 忙碌场所、相似外形发型']],
 'a wooden beehive 木蜂箱，a beehive of activity 一片忙碌的场所，a beehive hairstyle 蜂窝式高耸发型。',
 'a beehive of activity；a wooden beehive。',
 'beehive 通常围着蜜蜂等相应居所说，不能推成所有蜂类都住同样形状的巢；比喻里没有真实蜂也成立。',
 ('The beekeeper checked the wooden beehive.','养蜂人检查了木蜂箱。'),('The kitchen became a beehive of activity before the guests arrived.','客人到来前，厨房忙得热火朝天。'))
W('beekeeping','/ˈbiːkiːpɪŋ/','养蜂、养蜂业',
 '不是把一只蜂随手留下，而是持续照料、管理蜂群，这套活动、行业就是 beekeeping。',
 'bee + keeping，keep 在此是饲养、照料，-ing 形成活动名词；对应的执行者是 beekeeper。',B[:1]+[['bee + keeping → beekeeping','养护蜂群的活动、职业']],
 'take up beekeeping 开始养蜂，urban beekeeping 城市养蜂，a beekeeping course 养蜂课程。通常作不可数活动名词。',
 'take up beekeeping；a beekeeping course。',
 'beekeeping 是活动，beekeeper 是人，beehive 是居所、设施；三者用角色串起来。',
 ('He took up beekeeping after moving to the countryside.','搬到乡下后，他开始养蜂。'),('The community garden offers a beekeeping course.','社区花园开设养蜂课程。'))
W('beeline','/ˈbiːlaɪn/','直达路线；〔make a beeline for〕直奔',
 '一眼认准目标，几乎不绕路就过去，是 make a beeline for。比如一下车就直奔饮水处，不必真量一条笔直几何线。',
 'bee + line，命名联系蜜蜂直接返回蜂巢的传统印象。它说明词的形象来源，不是对所有蜂每次飞行路线的科学保证。',B[:1]+[['bee + line → beeline','直接回巢的形象 → 直达、直奔路线']],
 'make a beeline for the door 直奔门口，head in a beeline towards something 径直朝某物去。最常用整组 make a beeline for。',
 'make a beeline for。',
 'beeline 重在直接、迅速奔向目标；不要求地上真有画出的线，也不必在有蜜蜂的地方用。',
 ('The children made a beeline for the ice cream stand.','孩子们直奔冰淇淋摊。'),('After the meeting, she made a beeline for the exit.','会后，她径直走向出口。'))
R('B2667','蜂类及其声音、居所、养护活动与路线形象','BEE：从一只蜂，把家、养蜂人和养蜂活动串起来','bee → bumblebee、beehive、beeline；beekeeper、beekeeping、beeswax。',
 'bee 是动物，hive 是住处，keeper 是养护的人，keeping 是持续活动，wax 是相应蜡质产物。beeline 则借直接回巢的传统印象。',
 'bēo、bīo → bee；bumble 嗡鸣，hive 居所，keep 饲养，line 路线，wax 蜡。',
 [['动物与居所','bee · bumblebee · beehive'],['养护的人、活动与产物','beekeeper · beekeeping · beeswax'],['路线形象','beeline']],
 '不是所有蜂都群居产蜜；beeline 是直奔的表达；spelling bee 的集会义另有来源分析。',
 'The beekeeper studied beekeeping before buying the beehives.\n\n养蜂人在买蜂箱前先学习了养蜂。','bee bumblebee beehive beekeeper beekeeping beeswax beeline')
He=[['操舵：古英语 helma → helm','操舵装置、控制位置；更远词源有不同分析'],['护头：古英语 helm 及相应日耳曼语词','保护头部的覆盖物，与操舵同形词分开'],['helm 护头词 + 小称 -et → helmet','常见法语借入分析，也有英语内部扩展讨论']]
W('helm','/helm/','舵柄、舵轮、操舵装置；掌舵、领导；头盔〔旧义〕',
 '船上控制方向的装置是 helm，at the helm 就是掌着方向，后来也说领导组织。旧式头盔义另是一条保护覆盖的来源，不因船长戴帽子而产生。',
 '操舵义承古英语 helma；头盔义承古英语 helm 及相应日耳曼语护头词。更远来源各有分析，不把两种功能强接成一个故事。',He[:2],
 'at the helm 掌舵、领导，take the helm 接过指挥，helm a project 领导项目。旧文学、奇幻中 helm 仍可说头盔。',
 'at the helm；take the helm；helm a project。',
 'helm 可以泛指操舵装置，rudder 更具体是改变水流方向的舵面；不总是同一个实物部件。',
 ('She took the helm as the boat left the harbour.','船驶离港口时，她接过了操舵。'),('He spent ten years at the helm of the company.','他领导公司十年。'),sources=['https://en.wiktionary.org/wiki/helm#English','https://www.etymonline.com/word/helm'])
W('helmet','/ˈhelmɪt/，也读 /ˈhelmət/','头盔、保护头部的硬质帽具',
 '给头外面加一层保护壳，是 helmet 的直观画面。骑行、运动、工地、历史盔甲里都可见，具体结构随用途不同。',
 '中古英语已有 helmet 等，通常联系古法语 helmet、heaumet 等小称，源自日耳曼语护头词 helm；也有英语 helm + -et 的扩展分析。不是从船舵缩小变成头盔。',He[1:],
 'a cycling helmet 骑行头盔，a safety helmet 安全帽，a helmet visor 头盔面罩。-et 的历史小称不表示现代头盔都很小。',
 'a cycling helmet；a safety helmet。',
 'helmet 比普通 hat 更突出硬质保护；不同用途的具体要求不能仅凭词名判断。',
 ('She put on her cycling helmet before leaving.','出发前，她戴上骑行头盔。'),('The worker placed his safety helmet on the bench.','工人把安全帽放在长凳上。'),sources=['https://en.wiktionary.org/wiki/helmet#English','https://www.etymonline.com/word/helmet'])
R('B4183','操舵控制与护头覆盖，分清同形词的来源','HELM：一手掌方向，一层护住头','helm → helmsman；护头 helm → helmet，分别成组。',
 'at the helm 的领导画面是掌舵；helmet 的保护画面是护头。两者都容易想象，但不把同形字母当成唯一来源。',
 'helma 操舵 → helm、helmsman；护头 helm 词族 → 法语或英语小称 helmet。',
 [['掌舵装置与人物','helm · helmsman'],['护头词族','helmet']],
 'helm 与 rudder 不总是相同部件；helmet 的 -et 不规定现代大小；旧 helm 头盔义在部分作品中仍见。',
 'The helmsman wore a helmet while steering the fast boat.\n\n操舵者驾驶快艇时戴着头盔。','helm helmsman helmet')
La=[['拉丁 laqueus 绳圈、套索 → 法语 las、laz → lace','绳带、系带、网'],['绳带装饰 → 镂空花纹织物','花边、蕾丝；动词系带、交织、掺入'],['后缀与复合','lacy 花边的；shoelace 鞋带；necklace 项链']]
W('lace','/leɪs/','蕾丝、花边；系带、鞋带；系紧、交织、掺入',
 '一边是细绳穿孔系起来的带子，一边是细线交织成镂空花纹的蕾丝。两者都从线、绳、网的旧画面发展，动词也能说系紧、交织。',
 '借古法语 las、laz，来自拉丁 laqueus 绳圈、套索的相关形式。由绳带发展为装饰编带，再成为镂空花纹织物；动词借相应法语系带形式。',La[:2],
 'a lace collar 蕾丝领，tie your laces 系鞋带，lace up your boots 系紧靴带，a speech laced with humour 夹着幽默的演讲。',
 'lace up；tie your laces；be laced with。',
 '织物 lace 通常不可数，系带 a lace 可数；be laced with 根据所掺内容可说幽默、酒等，不都译成织布。',
 ('The dress had a delicate lace collar.','裙子有一圈精致蕾丝领。'),('He laced up his boots before the walk.','徒步前，他系紧靴子的带子。'),sources=['https://en.wiktionary.org/wiki/lace#English','https://www.etymonline.com/word/lace'])
W('lacy','/ˈleɪsi/','蕾丝制的、带花边的；像蕾丝般镂空细密的',
 '真蕾丝边可以 lacy；叶脉、霜花细细分叉、镂空得像蕾丝，也可以借它形容。它说性质，不要求材料真是布。',
 'lace + -y，去词尾 e。字母 c 在这个形式中仍读 /s/；由花边织物形成相应性质。',La[:2]+[['lace + -y → lacy','带蕾丝、像蕾丝般细密镂空']],
 'a lacy dress 蕾丝裙，lacy curtains 蕾丝窗帘，a lacy pattern 细密镂空花纹，lacy leaves 细裂如花边的叶子。',
 'lacy curtains；a lacy pattern。',
 'lacy 可以是真材料，也可以是视觉相似；lace 是名词或动词，lacy 是性质形容词。',
 ('Sunlight passed through the lacy curtains.','阳光透过蕾丝窗帘照进来。'),('Frost left a lacy pattern on the window.','霜在窗上留下蕾丝般细密的花纹。'))
R('B3830','绳圈、系带与线网，扩到花边、交织和相似花纹','LACE：一根线能系住东西，许多线能织出镂空花纹','lace → lacy；shoelace、necklace 各有固定物品义。',
 '鞋带看系紧，蕾丝看交织花纹，lacy 再把外观带到叶片、霜花等。necklace 的末尾发音已与单独 lace 不同，要按整词记。',
 'laqueus → 法语 las、laz → lace；-y 性质去 e；shoe 鞋、neck 颈 + lace 形成复合。',
 [['系带、花边与外观','lace · lacy'],['固定物品名称','shoelace · necklace']],
 '织物与带子数法不同；lace up 是系紧；necklace 不是现代把末尾照 /leɪs/ 生读。',
 'Her lacy collar framed a small necklace.\n\n她的蕾丝领衬着一条小项链。','lace lacy shoelace necklace')
if __name__=='__main__':save('continuation_20261030_lp',ROOTS,WORDS)
