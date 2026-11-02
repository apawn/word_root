"""Familiar animal names: attested borrowing routes and useful everyday uses."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
def S(word,base):
 a=['https://en.wiktionary.org/wiki/'+word+'#English','https://www.etymonline.com/word/'+base]
 if base in ['prawn','shrimp']:a.append('https://www.merriam-webster.com/dictionary/'+base)
 if base=='microgram':a=['https://en.wiktionary.org/wiki/'+word+'#English','https://www.etymonline.com/word/gram','https://www.etymonline.com/word/micrometer','https://www.nist.gov/pml/owm/metric-si-prefixes']
 return a
EXISTING_ROOT_ADDITIONS={
 'A1701':dict(words='microgram micrograms'.split(),label='micro- + gram：微克单数到复数',note='micro- 百万分之一，gram 克；microgram 是一克的百万分之一，micrograms 给整个单位名加复数 -s。'),
 'B3141':dict(words='microgram micrograms'.split(),label='microgram → micrograms：克的细分单位',note='gram 经法语 gramme，远接希腊 gramma 小重量用法；micro- 在计量名中规定为百万分之一。'),
 'C1214':dict(words='lizard lizards chameleon'.split(),label='与 reptile 对照：蜥蜴、变色龙的名称',note='这里按动物概念对照，不把这些动物名都说成 rept- 的派生词。lizard 经法语接拉丁 lacerta；chameleon 经法语、拉丁接希腊地上、小的材料与 leon 狮子。'),
 'C0665':dict(words='chameleon'.split(),label='chameleon：地上、小的材料与狮子名组成的旧动物称呼',note='希腊 khamai 在地上、低的材料 + leon 狮子 → khamaileon；经拉丁、法语进入英语。命名中的狮子是形象比较，不能据此推成现代动物亲缘。'),
 'B2508':dict(words='shrimp shrimps'.split(),label='shrimp 的细小、缩小词源联想',note='shrimp 承中古英语 shrimpe，更远常联系日耳曼细小、缩小词族，细节用可能表述。现代 shrimp 既指虾，也可贬称小个子；不是把英语 shrink 直接剪掉末尾造出。'),
 'A1918':dict(words='lobsters'.split(),label='lobster → lobsters：动物名词尾与复数',note='lobster 接古英语 loppestre，常联系拉丁 locusta 动物名，借入改形过程和 -estre 影响仍有不明确处。现代只在整个词尾加 -s，不能按人物职业后缀理解。'),
 'B3817':dict(words='crabs'.split(),label='crab → crabs：蟹的复数；抱怨动词的第三人称',note='蟹名接古英语 crabba，常联系抓挠、爬动词族；crab 抱怨的评价用法与 crabbed 等有历史关系，酸苹果另支也有影响。新词条分开例示蟹名复数与抱怨动词。'),
 'B4083':dict(words='squid prawn prawns clam clams mussel mussels scallop scallops'.split(),label='水生动物名称对照：乌贼、虾、几类贝',note='这是与 shell、shellfish 对照认识动物与食材，不表示这些词同源。squid、prawn 更远来源不明确；clam 常联系夹紧的旧词；mussel 接拉丁小鼠的名称材料；scallop 经古法语壳名。'),
 'C0931':dict(words='oysters'.split(),label='oyster → oysters：牡蛎、蚝',note='oyster 经古法语、拉丁接希腊 ostreon 牡蛎，与硬壳、骨的古老词族有关；复数 -s 在 /ə/、/ɚ/ 后读 /z/。'),
 'C0777':dict(words='mussel mussels'.split(),label='mussel 与 muscle：小鼠名称材料的两条用法',note='mussel 接古英语 muscle 等和晚期拉丁 muscula、musculus，远有 mus 鼠 + 拉丁小称材料。它与 muscle 肌肉有历史关系，现代是同音的不同词，不把贻贝说成由英语 muscle 改义产生。'),
 'B2628':dict(words='tuna trout mackerel eel eels'.split(),label='fish 对照下的常见鱼名',note='这里按鱼类概念聚合，不把各名称都说成英语 fish 的派生词。tuna 经西班牙语、阿拉伯语接拉丁希腊鱼名；trout 有古英语与法语传播线；mackerel 经古法语，远源不明；eel 承古英语 æl。'),
}
LIZARD=[['拉丁 lacerta／lacertus 蜥蜴 → 古法语 laisarde 等形式','较远来源不明确'],['古法语、盎格鲁法语 → 中古英语 → lizard','借入时词形改变；末尾可能受 -ard 类形式影响']]
SHRIMP=[['中古英语 shrimpe → 现代 shrimp','更远可能与日耳曼细小、缩小词族相关'],['动物名称与小个子用法 → 现代语境分别使用','古老材料和词义先后细节不宜说死']]
PRAWN=[['中古英语 prayne 等旧形式 → prawn','更远来源不明确，整词记这个虾名'],['英语 prawn → prawns','个体名复数，日常食材用法常见']]
CLAM=[['古英语 clamm 夹、束缚 → 中古英语 clam 夹钳等','常见词源分析把合拢的壳与夹紧动作联系起来'],['clam 贝名 → clam up 闭口不说','壳合上帮助理解闭口的现代比喻']]
MUSSEL=[['拉丁 mus 鼠 + 小称材料 → musculus、muscula 等','小鼠的形象用于若干身体、动物名称'],['晚期拉丁 → 古英语 muscle／musscel → mussel','现代拼写与 muscle 肌肉分开，通常仍同音']]
SCALLOP=[['古法语 escalope 壳、甲壳 → 英语 scallop','更远通常联系日耳曼壳、鞘的材料，细节有不确定处'],['扇贝、扇贝壳 → 壳状圆弧花边、烹调动词等','由壳形向相似边缘、盛放烹调的用法扩展']]
EEL=[['古日耳曼鳗鱼名 → 古英语 æl → eel','日耳曼语以外的更远来源没有定论'],['eel → eels；也有滑溜、难捉摸的比喻','现代复数规则变化，比喻借动物形象']]
W('microgram','英 /ˈmaɪkrəʊɡræm/；美 /ˈmaɪkroʊɡræm/','微克',
 '一克若切成一百万个同样重的小份，其中一份的质量就是一微克。它是极小质量的计数单位。',
 'micro- 百万分之一 + gram 克 → microgram；micro- 接希腊小的材料，gram 经法语接希腊小重量的名称。',
 [['希腊小的材料 → micro- 百万分之一','现代单位前缀的精确约定'],['micro- + gram → microgram → micrograms','一微克，再按英语规则变复数']],
 'one microgram 是一微克；less than a microgram 是不到一微克；复数见 micrograms。',
 'one microgram；less than a microgram；a microgram of material。',
 '毫克 milligram 是千分之一克，微克 microgram 是百万分之一克。数值相同时，毫克对应的质量大一千倍。',
 ('The sample weighed less than a microgram.','这个样品的质量不到一微克。'),('One microgram is a millionth of a gram.','一微克是一克的百万分之一。'),sources=S('microgram','microgram'))
W('lizard','英 /ˈlɪzəd/；美 /ˈlɪzɚd/','蜥蜴',
 '细长的身子、尾巴，许多种有四条腿；墙面或石头上见到的那类小爬行动物，常叫 lizard。',
 '整词经盎格鲁法语、古法语的蜥蜴名，接拉丁 lacerta／lacertus。现代英语里没有必要再硬切出可用的前后缀。',LIZARD,
 'a lizard on a wall 是墙上一只蜥蜴；a small lizard 是一只小蜥蜴。名称范围较广，具体种类再由修饰词说明。',
 'a small lizard；a lizard on the wall；a lizard in the garden。',
 'alligator 的西班牙语来源 el lagarto 也能向远处接到这条拉丁动物名；英语两个词指的动物范围已经不同。',
 ('A small lizard ran across the wall.','一只小蜥蜴跑过墙面。'),('We saw a lizard resting on a warm rock.','我们看见一只蜥蜴趴在温热的石头上。'),sources=S('lizard','lizard'))
W('lizards','英 /ˈlɪzədz/；美 /ˈlɪzɚdz/','蜥蜴〔复数〕',
 '不是一只，而是几只蜥蜴，便用 lizards。先认整词，再给动物名加常规复数。',
 'lizard + -s → lizards；/d/ 后读 /z/，词尾 /dz/。借入的动物名已经按英语名词规则变化。',LIZARD+[['lizard + -s → lizards','多只蜥蜴，词尾 /dz/']],
 'small lizards 是小蜥蜴们；several lizards 是几只蜥蜴；不同种类也可统称 lizards。',
 'small lizards；several lizards；lizards on the rocks。',
 'lizards 是现代动物名复数；dinosaurs 的 -saur- 接希腊蜥蜴材料，是另一条语言来源，别只按中文同为蜥蜴就混成同一个词根。',
 ('Several lizards were resting on the rocks.','几只蜥蜴趴在石头上。'),('The guide showed us pictures of local lizards.','向导给我们看了当地蜥蜴的照片。'),sources=S('lizards','lizard'))
W('chameleon','英 /kəˈmiːliən/；美 /kəˈmiːliən/','变色龙；善于改变外表、立场或风格的人',
 '动物是变色龙；形容人时，借它会变色的画面，说这个人换个环境就换一种样子。可以夸适应力，也可能批评见风转舵。',
 '希腊 khamai 在地上、低的材料 + leon 狮子 → khamaileon；经拉丁 chamaeleon、古法语进入英语。英语 h 后来按古典拼写恢复。',
 [['希腊 khamai + leon → khamaileon','旧动物名可直观记成地上的小狮子；具体命名缘由不能说死'],['拉丁、古法语 → chameleon → 善变者的比喻','由动物变色形象延伸到人的风格、立场变化']],
 'a political chameleon 常批评政治立场多变；a stylistic chameleon 可说创作者能驾驭多种风格。评价取决于搭配。',
 'a chameleon on a branch；a political chameleon；a stylistic chameleon。',
 '词源里的 lion 是旧命名形象，不表示它和狮子是近亲；动物变色的具体原因也不能一概解释成模仿背景。',
 ('The chameleon gripped the branch with its feet.','那只变色龙用脚抓着树枝。'),('As an actor, she is a chameleon who can disappear into any role.','作为演员，她很善于变换面貌，能完全融入各种角色。'),sources=S('chameleon','chameleon'))
W('squid','英、美 /skwɪd/','鱿鱼；鱿鱼肉',
 '身体细长，带腕和较长的触手；水族馆里的动物、餐盘里的鱿鱼，都可以叫 squid。先把这个整词和形象接起来。',
 '英语旧记录已有 squid 这个动物名，远源不明确。有分析把它和 squirt 喷射联系起来，但只能作可能的解释。',
 [['早期现代英语 squid 动物名','更远来源没有定论'],['动物 squid → 食材 squid','既可数动物，也可把肉当作不可数食材']],
 'a squid 是一只鱿鱼；grilled squid 是烤鱿鱼。作动物复数时 squid 很常见，squids 也存在，按语境和文体使用。',
 'a squid；grilled squid；squid swimming in the tank。',
 'squid 属软体动物，不能因为常和 seafood 一起出现就把它当鱼；喷墨是理解可能词源的联想，不是已证实的造词步骤。',
 ('A squid moved through the water with a sudden burst of speed.','一只鱿鱼突然加速穿过水中。'),('We ordered grilled squid for lunch.','我们午餐点了烤鱿鱼。'),sources=S('squid','squid'))
W('shrimp','英、美 /ʃrɪmp/','虾；虾肉；小个子〔常有贬意〕',
 '先认弯着身子、长须的虾。说 a little shrimp 形容人时，则把细小的形象转成“小个子”，语气可能不友好。',
 '承中古英语 shrimpe，更远可能联系日耳曼细小、缩小的材料。现代作为虾名整词使用，人物义的具体早期关系不宜强说成单一路线。',SHRIMP,
 'a shrimp 是一只虾；shrimp in the bowl 可以是多只虾；shrimp with rice 常把虾当食材。',
 'a shrimp；shrimp with rice；a bowl of shrimp。',
 '复数 shrimp、shrimps 都存在；美式菜单常见 shrimp，英式也常说 prawns。大小、物种和地区用名会交叉，不是一条全球统一的大小分界。',
 ('A shrimp moved between the plants in the tank.','一只虾在水缸里的水草间移动。'),('We had shrimp with rice for dinner.','我们晚餐吃了虾配米饭。'),sources=S('shrimp','shrimp'))
W('shrimps','英、美 /ʃrɪmps/','虾〔复数〕；捕虾〔动词第三人称〕',
 '几只虾可以写 shrimps，也常直接写 shrimp。若前面是 he、she 等单数主语，shrimps 还可能表示那个人捕虾。',
 'shrimp + -s → shrimps，/p/ 后读 /s/，词尾 /mps/。名词复数与捕虾动词的第三人称同形。',SHRIMP+[['shrimp + -s → shrimps','虾的复数，或捕虾动词的第三人称']],
 'several shrimps 指几只虾；shrimps in the tank 是缸里的虾。作食材整体时，shrimp 的不变复数、不可数用法也很常见。',
 'several shrimps；small shrimps；shrimps in the tank。',
 '不要见到没加 s 的 shrimp 就认定只有一只；数词、限定词和句子场景一起决定单复数。',
 ('Several shrimps were hiding under the rock.','几只虾躲在石头下面。'),('The child counted the shrimps in the tank.','孩子数了数缸里的虾。'),sources=S('shrimps','shrimp'))
W('prawn','英 /prɔːn/；美 /prɔːn/、/prɑːn/','虾，对虾；虾肉',
 '在很多英式菜单里，看见 prawn 就想到虾。它常让人想到较大的食用虾，但日常命名并不总按一套严格的大小规则。',
 '中古英语 prayne 等旧形式演变为 prawn，更远来源不明确。把它作为动物名整词学，不硬拆出英语前后缀。',PRAWN,
 'a prawn 是一只虾；a prawn sandwich 是虾肉三明治；prawn 放在食物名前可用单数形式作修饰。',
 'a prawn；a prawn sandwich；prawn curry。',
 'shrimp 与 prawn 在地区、菜单和分类语境中可能交叉。具体餐盘是什么，还要看当地用法，不能只凭这个词推断准确物种。',
 ('A large prawn lay on top of the noodles.','面条上放着一只大虾。'),('She chose a prawn sandwich for lunch.','她午餐选了虾肉三明治。'),sources=S('prawn','prawn'))
W('prawns','英 /prɔːnz/；美 /prɔːnz/、/prɑːnz/','虾，对虾〔复数〕',
 '盘里一只只的虾，常直接说 prawns。它是英国等地菜单和买菜场景里很常见的复数。',
 'prawn + -s → prawns；/n/ 后读 /z/，词尾 /nz/。基础动物名的远源仍不明确，复数变化则很规则。',PRAWN+[['prawn + -s → prawns','多只虾，词尾 /nz/']],
 'grilled prawns 是烤虾；a plate of prawns 是一盘虾；peel the prawns 是给虾剥壳。',
 'grilled prawns；a plate of prawns；peel the prawns。',
 'prawn sandwich 用单数名词修饰 sandwich，a plate of prawns 则在数、指盘里的虾，句法位置不同。',
 ('We shared a plate of grilled prawns.','我们分着吃了一盘烤虾。'),('She added the prawns to the noodles.','她把虾加进了面条里。'),sources=S('prawns','prawn'))
W('lobsters','英 /ˈlɒbstəz/；美 /ˈlɑːbstɚz/','龙虾〔复数〕',
 '几只长身、硬壳的龙虾，用 lobsters。餐桌上也可这样数整只龙虾，若只谈肉则常用 lobster。',
 'lobster + -s → lobsters，词尾 /z/。lobster 承古英语 loppestre，常联系拉丁 locusta 动物名；借入改形和词尾受影响的细节仍有不明确处。',
 [['拉丁 locusta 动物名 → 古英语 loppestre 等形式','通常作为借词改形来分析，不是现代职业名'],['中古英语 lopster 等 → lobster → lobsters','整词后加复数 -s']],
 'two lobsters 是两只龙虾；live lobsters 是活龙虾；lobster meat 则把肉作为食材来谈。',
 'two lobsters；live lobsters；lobsters in a tank。',
 '这里的 -ster 是历史词形的一部分，不能按现代“做某事的人”去拆；今天数多只时只添加末尾 -s。',
 ('Two lobsters were moving around the tank.','两只龙虾在水缸里移动。'),('The drawing shows the claws of several lobsters.','图中画了几只龙虾的螯。'),sources=S('lobsters','lobster'))
W('crabs','英、美 /kræbz/','螃蟹〔复数〕；抱怨，挑毛病〔动词第三人称〕',
 '石头下几只横着走的蟹，是 crabs；若说 he crabs about something，则是在说他为某事抱怨。词性要看整个句子。',
 'crab + -s → crabs，/b/ 后读 /z/。蟹名接古英语 crabba，较远常联系抓挠词族；抱怨的动词与 crabbed 等坏脾气用法有关，别强编成蟹一直在抱怨。',
 [['古英语 crabba → crab 蟹','更远常联系抓挠、爬动材料'],['crabbed、crab 等评价用法 → crab 抱怨','动物、酸苹果等分支的形象有交汇'],['crab + -s → crabs','蟹名复数或动词第三人称，词尾 /bz/']],
 'small crabs 是小螃蟹；crabs about the weather 是抱怨天气。动物作食材时还可用不可数 crab。',
 'small crabs；crabs under the rocks；crabs about the weather。',
 'crab 的野酸苹果是另有来源解释的一支；多义词不能因为拼写相同，就把每个意思都编成同一动物故事。',
 ('Small crabs hid under the rocks.','小螃蟹躲在石头下面。'),('He crabs about the weather whenever we plan a walk.','我们每次计划散步，他就抱怨天气。'),sources=S('crabs','crab'))
W('clam','英、美 /klæm/','蛤蜊；闭口不说〔常见于 clam up〕',
 '先看两片壳合紧的贝。英语里 clam up 就借这个画面，说人突然把嘴闭紧，不愿再说。',
 '贝名常分析为中古英语 clam 夹钳、夹具的特殊用法，向前接古英语 clamm 夹、束缚等；具体命名联系用可能表述。现代 clam up 是闭口的动词短语。',CLAM,
 'a clam 是一只蛤蜊；clam chowder 是蛤蜊浓汤；clam up 是不肯说话，不是单独把 up 译成向上。',
 'a clam；clam chowder；clam up when asked。',
 'clam 是具体贝类名，shellfish 是更宽的日常类别名。词源里的夹紧画面有助理解，不能替代具体动物辨认。',
 ('A clam was partly buried in the sand.','一只蛤蜊半埋在沙里。'),('I tend to clam up when strangers ask personal questions.','陌生人问私人问题时，我往往就不肯说话了。'),sources=S('clam','clam'))
W('clams','英、美 /klæmz/','蛤蜊〔复数〕；闭口不说〔clam up 的第三人称〕',
 '盘里几只、沙里几只蛤蜊，可以说 clams；someone clams up 则是在说某人闭口不言。',
 'clam + -s → clams；/m/ 后读 /z/，词尾 /mz/。名词复数与动词第三人称同形，后面有 up 时常是闭口用法。',CLAM+[['clam + -s → clams','多只蛤蜊，或单数主语后的动词形式']],
 'a bowl of clams 是一碗蛤蜊；clams in the sand 是沙里的蛤蜊；clams up when questioned 是一问就不说了。',
 'a bowl of clams；clams in the sand；clams up when questioned。',
 'clam up 描述不愿或突然停止说话，不必是真的发不出声音；按人的反应理解这幅闭壳画面。',
 ('We ordered a bowl of clams.','我们点了一碗蛤蜊。'),('She clams up whenever anyone mentions the old argument.','只要有人提起那次旧争吵，她就闭口不言。'),sources=S('clams','clam'))
W('oysters','英 /ˈɔɪstəz/；美 /ˈɔɪstɚz/','牡蛎，蚝〔复数〕',
 '两片不规则的硬壳里包着软肉，餐桌上常叫蚝，英语是 oysters。它与蛤蜊、贻贝等名称要分别认。',
 'oyster + -s → oysters，词尾 /z/。oyster 经古法语 oistre、拉丁 ostrea 等接希腊 ostreon 牡蛎，与硬壳、骨的古老词族有关。',
 [['希腊 ostreon 牡蛎 → 拉丁 ostrea → 古法语 oistre','旧动物名在借入中改形'],['英语 oyster + -s → oysters','多只牡蛎、蚝，词尾 /z/']],
 'oysters on a plate 是盘里的牡蛎；oyster shells 是蚝壳。修饰 shell 时常用单数 oyster，不需要把每个位置都变复数。',
 'a plate of oysters；oysters on the menu；oyster shells。',
 'oysters 与 clams 都有两片壳，但现代名称对应不同动物；同属宽泛的贝类食材，不等于两个词可随便替换。',
 ('The menu lists oysters as a starter.','菜单把牡蛎列为前菜。'),('The display showed several oysters beside their shells.','展台展示了几只牡蛎和它们的壳。'),sources=S('oysters','oyster'))
W('mussel','英、美 /ˈmʌsəl/','贻贝，淡菜；贻贝肉',
 '两片常呈细长形的壳，成群附着在石头上；餐桌上的贻贝、淡菜，英语常叫 mussel。',
 '经古英语 muscle、musscel 等接晚期拉丁 muscula、拉丁 musculus，远有 mus 鼠 + 拉丁小称材料，即小鼠的名称形象。现代拼写与 muscle 肌肉分开。',MUSSEL,
 'a mussel 是一只贻贝；a mussel shell 是一片贻贝壳；谈肉时也可把 mussel 作食材名。',
 'a mussel；a mussel shell；mussel beds。',
 'mussel 与 muscle 同音，又有历史联系；现在一个是贻贝，一个是肌肉，写字时靠语境选词。',
 ('A mussel was attached to the rock.','一只贻贝附着在石头上。'),('She picked up an empty mussel shell.','她捡起一片空贻贝壳。'),sources=S('mussel','mussel'))
W('mussels','英、美 /ˈmʌsəlz/','贻贝，淡菜〔复数〕',
 '石头上一群贻贝，或碗里一份贻贝，都常说 mussels。单只动物的名字后，加上复数即可。',
 'mussel + -s → mussels，/l/ 后读 /z/，词尾 /lz/。基础词接拉丁小鼠名称材料，但复数不用拉丁词尾，按英语规则变化。',MUSSEL+[['mussel + -s → mussels','多只贻贝；与 muscles 肌肉们仍同音']],
 'a bowl of mussels 是一碗贻贝；mussels on the rocks 是石头上的贻贝；名称也常整体指作为食材的一份。',
 'a bowl of mussels；mussels on the rocks；mussels on the menu。',
 'mussels 与 muscles 都读 /ˈmʌsəlz/。看餐盘、水域还是身体运动场景，才能把拼写和意义分开。',
 ('Mussels covered the rocks near the water.','水边的石头上布满了贻贝。'),('We shared a bowl of mussels at lunch.','午餐时我们分着吃了一碗贻贝。'),sources=S('mussels','mussel'))
W('scallop','英 /ˈskɒləp/；美 /ˈskɑːləp/，也读 /ˈskæləp/','扇贝；扇贝壳状的圆弧花边；做成圆弧边；用酱汁等焗烤',
 '先看扇贝壳：像一把小扇子，边缘带弧形。边缘装饰的一串小圆弧，也能借它的壳形来叫 scallop。',
 '经古法语 escalope 壳、甲壳进入英语，更远通常联系日耳曼壳、鞘的材料。由动物与壳形再扩展出装饰、烹调动词，不能把每个义项都理解成吃扇贝。',SCALLOP,
 'a scallop 是一只扇贝；scallop the edge 是把边缘做成一连串圆弧；烹调里的 scallop 还可指将食物加酱汁等焗烤。',
 'a scallop shell；scallop the edge；scallop the potatoes。',
 'scalloped potatoes 是一种烹调名称，不表示土豆里一定放了扇贝；这个动词有盛放、烹调用法的历史。',
 ('The child found a scallop shell on the beach.','孩子在沙滩上找到一枚扇贝壳。'),('Use the template to scallop the edge of the card.','用模板把卡片边缘裁成圆弧花边。'),sources=S('scallop','scallop'))
W('scallops','英 /ˈskɒləps/；美 /ˈskɑːləps/，也读 /ˈskæləps/','扇贝〔复数〕；圆弧花边〔复数〕；做成圆弧边或焗烤〔第三人称〕',
 '餐盘里的 scallops 是扇贝食材；衣料、纸边的一连串 scallops，则是像扇贝壳边缘的小圆弧。',
 'scallop + -s → scallops；/p/ 后读 /s/，词尾 /ps/。名词复数与动词第三人称同形，由句法区分。',SCALLOP+[['scallop + -s → scallops','多只扇贝、多个圆弧，或相关动词形式']],
 'grilled scallops 是烤扇贝；a border of scallops 是一圈圆弧花边。菜单上也常用 scallops 指取出的可食部分。',
 'grilled scallops；a plate of scallops；a border of scallops。',
 '扇贝和圆弧花边之间有壳形联想，具体见到哪个意思，要看它是在餐盘里还是边缘设计上。',
 ('The menu includes grilled scallops.','菜单上有烤扇贝。'),('The card has a border of small scallops.','这张卡片的边缘是一圈小圆弧花边。'),sources=S('scallops','scallop'))
W('tuna','英 /ˈtjuːnə/、/ˈtʃuːnə/；美 /ˈtuːnə/','金枪鱼；金枪鱼肉',
 '罐头、三明治里的金枪鱼，以及海里的金枪鱼，都可以叫 tuna。整条动物和作为食材的肉，语法用法会不同。',
 '英语鱼名借美洲西班牙语 tuna，接西班牙语 atún、阿拉伯语 tūn，向前接拉丁 thunnus、希腊 thynnos 等鱼名。更远是否有飞快游动的含义，不宜当定论。',
 [['希腊、拉丁鱼名 → 阿拉伯语 tūn → 西班牙语 atún','鱼名随借用在语言间传播'],['美洲西班牙语 tuna → 英语 tuna','动物名也指食材；同名的仙人掌果是另一来源的较少见词']],
 'a tuna 是一条金枪鱼；canned tuna 是罐装金枪鱼肉；a tuna sandwich 是金枪鱼三明治。作动物复数时 tuna 很常见，tunas 也存在。',
 'a tuna；canned tuna；a tuna sandwich。',
 '谈食材时 some tuna 不需要加 s；谈几条动物时看数词与上下文。不要为了复数一律写 tunas。',
 ('A tuna swam past the boat.','一条金枪鱼从船边游过。'),('I made a tuna sandwich for lunch.','我午餐做了金枪鱼三明治。'),sources=S('tuna','tuna'))
W('trout','英、美 /traʊt/','鳟鱼；鳟鱼肉',
 '河流、湖泊里常谈到的一类鱼，叫 trout。餐馆菜单里也可用这个词说鳟鱼这道食材。',
 '中古英语形式一部分承古英语 truht，一部分受古法语 truite 影响，都接晚期拉丁 tructa；更远可能联系希腊意为啃咬者的鱼名，但有不确定处。',
 [['晚期拉丁 tructa → 古英语 truht、古法语 truite','两条传播线共同影响中古英语词形'],['中古英语 → trout','保留动物名，也用作食材名称']],
 'a trout 是一条鳟鱼；several trout 是几条鳟鱼；grilled trout 是烤鳟鱼。普通复数常不变，也有 trouts。',
 'a trout；several trout；grilled trout。',
 'trout 的复数没有必须加 s 的要求。先认这是鱼名，再用数词、限定词判断句子在说多少。',
 ('A trout rested in the clear water below the bridge.','一条鳟鱼停在桥下清澈的水里。'),('The restaurant serves grilled trout with vegetables.','这家餐馆供应烤鳟鱼配蔬菜。'),sources=S('trout','trout'))
W('mackerel','英 /ˈmækərəl/；美 /ˈmækərəl/，也可压缩中间弱元音','鲭鱼；鲭鱼肉',
 '海里成群游动、背部常有条纹的鲭鱼，叫 mackerel。菜单上也可用它直接说鱼肉。',
 '英语借古法语 maquerel 鱼名，较远来源不明确。联系拉丁 macula 斑点等的说法只能作假说，不按拼写硬切成确定词根。',
 [['古法语 maquerel 鲭鱼 → 中古英语形式','远源有不同解释，没有定论'],['中古英语 → mackerel','现代鱼名与食材名；惊叹表达另按整体使用']],
 'a mackerel 是一条鲭鱼；smoked mackerel 是熏鲭鱼；Holy mackerel! 是表示惊讶的口语感叹。复数通常 mackerel，也有 mackerels。',
 'a mackerel；smoked mackerel；Holy mackerel!。',
 '感叹句不需要字面翻成神圣的鲭鱼。它是一整句随意的惊叹，和菜单中的具体鱼名用法分开。',
 ('We had smoked mackerel with bread.','我们吃了熏鲭鱼配面包。'),('“Holy mackerel! That box is heavy,” he said.','他说：“哇，这箱子真重！”'),sources=S('mackerel','mackerel'))
W('eel','英、美 /iːl/','鳗鱼；滑溜、难捉摸的人〔比喻〕',
 '长长的身子像蛇，却是一种鱼。英语还借它滑溜、不好抓住的形象，形容某人难以抓住话柄或看透。',
 '承古英语 æl，再向前接日耳曼鳗鱼名称；日耳曼语以外的远源没有定论。比喻义借动物形象延伸。',EEL,
 'an eel 是一条鳗鱼；slippery as an eel 是像鳗鱼一样滑溜，形容人时常说难捉摸、不肯让人抓住。',
 'an eel；an eel in the water；slippery as an eel。',
 'eel 的长形不改变它是鱼的身份；与 snake 蛇作形状比较，不表示这两个词同源或动物相同。',
 ('An eel slipped between the rocks.','一条鳗鱼滑进石缝里。'),('The witness was as slippery as an eel when asked for details.','一问到细节，那位证人就躲躲闪闪，很难问出实话。'),sources=S('eel','eel'))
W('eels','英、美 /iːlz/','鳗鱼〔复数〕',
 '几条细长、滑溜的鳗鱼，就是 eels。整个短词加复数 -s，读起来仍只有一个音节。',
 'eel + -s → eels；/l/ 后读 /z/，词尾 /lz/。基础动物名承古英语 æl，现代复数按规则变化。',EEL+[['eel + -s → eels','多条鳗鱼，词尾 /lz/']],
 'several eels 是几条鳗鱼；eels in the tank 是缸里的鳗鱼；baby eels 可说幼小的鳗鱼。',
 'several eels；eels in the tank；baby eels。',
 '长元音 /iː/ 后接 /lz/，词尾不另添 /ɪz/ 音节。它和 seals 海豹在发音、动物名称上都要分开。',
 ('Several eels were hiding among the stones.','几条鳗鱼躲在石头间。'),('The children watched the eels in the aquarium.','孩子们看着水族馆里的鳗鱼。'),sources=S('eels','eel'))
def extend_lessons():
 extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_zjf',ROOTS,WORDS)
 extend_lessons()
