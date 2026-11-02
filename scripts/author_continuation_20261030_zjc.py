"""Common animal words, native compounds, clipped names and distinct borrowing routes."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
def S(word,base):
 a=['https://en.wiktionary.org/wiki/'+word+'#English','https://www.etymonline.com/word/'+base]
 if word in ['dino','dinos']:a.append('https://www.merriam-webster.com/dictionary/dino')
 return a
EXISTING_ROOT_ADDITIONS={
 'C0055':dict(words='raccoon raccoons weasel weasels hamster hamsters crocodile crocodiles alligator alligators camels'.split(),label='动物名对照：当地语言、古英语与欧洲借词',note='本支按 animal 动物对照名称，分别有来源：raccoon 接波瓦坦语，weasel 接古英语，hamster 借德语，crocodile 经法语、拉丁语接更早希腊名称，alligator 由西班牙语 el lagarto 借来，camel 更远接闪米特语名称。各词不从拉丁 anim- 派生。'),
 'B3050':dict(words='buffalo buffaloes bison'.split(),label='buffaloes 与 bison：水牛、野牛名称的交叉',note='buffalo 经葡萄牙语、拉丁语接古希腊动物名称；bison 经法语、拉丁语接日耳曼语等另一条词线。北美日常 buffalo 可称美洲野牛 bison，两种名称有用法交叉而不因此同源。'),
 'C0460':dict(words='ferret ferrets'.split(),label='ferret → ferrets：小贼的命名到雪貂、搜寻',note='ferret 经法语 furet 小称等向前接拉丁 fur 贼，名字借人对其灵巧的看法；不是现代英语 fur 毛皮加动物后缀。ferrets 兼动物复数、动词第三人称，ferret out 用来表示搜寻查出。'),
 'B4047':dict(words='hedgehog hedgehogs'.split(),label='hedge + hog → hedgehog → hedgehogs：篱边的小猪',note='hedge 篱笆、树篱 + hog 猪 → hedgehog 刺猬，前者接活动环境，后者借像猪的口鼻形状命名。'),
 'C1263':dict(words='dinosaur dinosaurs dino dinos'.split(),label='dinosaur → dinosaurs；短称 dino → dinos',note='dinosaur 接近代拉丁 Dinosauria 与希腊 deinos 令人畏惧、强大 + sauros 蜥蜴材料；现代 dino 是完整名词缩短，dinos 再加复数 s，不把短称当一个英语可怕前缀。'),
 'B3115':dict(words='flamingo flamingos'.split(),label='flamingo：火焰色材料中的鸟名',note='flamingo 经西班牙语、葡萄牙语等形式，通常联系更早火焰、火焰色的材料，可能又与弗兰德人的名称形式相互影响；不是现代 flaming 随便添 o。复数 flamingos 直接加 s。'),
 'B2627':dict(words='pelican pelicans ostrich'.split(),label='pelican、ostrich：两条古老鸟名传播路线',note='与 bird 比较鸟名，不由 bird 派生。pelican 接古英语与拉丁、希腊鸟名，远处可能有斧、啄木鸟名称关系；ostrich 经法语、中世纪拉丁语接通俗拉丁 avis struthio 鸟加鸵鸟名等材料，不能按英语 os 骨来拆。'),
}
RACCOON=[['波瓦坦语的当地动物名 → 英语早期 arocoun 等形式','通常联系用手抓挠的原语言材料，历史记录的拼写多样'],['英语 raccoon → raccoons','现代名称整体使用；黑眼罩、环纹尾帮助辨认']]
WEASEL=[['古英语 weosule、wesle → 中古英语 wesel → weasel','更远来路不定，与其他动物名称的关系只是部分学者的提议'],['动物名 → 人的狡猾、逃避等比喻；weasel out 设法脱身、推诿','现代 weasels 可作动物复数，也可作第三人称单数动词']]
HAMSTER=[['德语 Hamster ← 中高地德语 hamastra 等','更远可能接斯拉夫语言名称，细节不确定'],['借入英语 hamster → hamsters','整词动物名进入英语，复数按现代规则变化']]
CROCODILE=[['希腊 krokodilos → 拉丁 crocodilus → 中世纪拉丁语、古法语形式','更远起源不明，石子加虫的拆分受到质疑'],['中古英语 cocodril、cokedrille 等 → 现代 crocodile','拼写后来向拉丁、法语形式靠拢；复数 crocodiles']]
ALLIGATOR=[['西班牙语 el 那个 + lagarto 蜥蜴','lagarto 更远接拉丁 lacertus、lacerta 动物名'],['整个词组被英语借入、改写 → alligator → alligators','原来独立的冠词 el 并入新词，不是现代英语 all 加 gator 的最初构词']]
FLAMINGO=[['西葡语 flamengo 等鸟名，通常联系普罗旺斯语火焰色材料','与弗兰德人名称形式之间可能有相互影响'],['英语 flamingo → flamingos','以暖红、粉红色羽毛帮助记；现代复数直接加 s']]
PELICAN=[['希腊 pelekan → 拉丁 pelecanus → 古英语 pellicane 等','更远可能与斧、啄木鸟名相关，或有鸟喙形状背景'],['中古英语拼写又受法语 pelican 影响 → pelican、pelicans','不能把可能的旧形状命名当作英语逐字直拼']]
W('raccoon','英、美 /rəˈkuːn/','浣熊',
 '黑色眼罩、蓬松的环纹尾巴，前爪常灵巧摆弄东西的动物，是 raccoon。名字的旧线索也常联系用手抓挠。',
 '借波瓦坦语等记录中的动物名称，英语早期有 arocoun 等多种拼写；原语言材料通常解释为用手抓挠，更远不按现代英语字母另拆。',RACCOON,
 'a raccoon’s tail 是浣熊尾巴；a raccoon near the bin 是垃圾桶旁的浣熊；a young raccoon 是幼年浣熊。',
 'a young raccoon；a raccoon’s tail；a raccoon near the bin。',
 'raccoon 是浣熊，red panda 是小熊猫；面部花纹可能让人觉得相似，但名称、动物不同。',
 ('A raccoon climbed onto the fence.','一只浣熊爬上了栅栏。'),('The raccoon searched around the empty bin.','浣熊在空垃圾桶周围翻找。'),sources=S('raccoon','raccoon'))
W('raccoons','英、美 /rəˈkuːnz/','浣熊〔复数〕',
 '几只戴着黑眼罩似的浣熊，就是 raccoons。注意重音仍在后面长长的 /kuːn/。',
 'raccoon + -s → raccoons，/n/ 后读 /z/；基础词保留两个 c、两个 o，复数只在末尾添 s。',RACCOON+[['raccoon + -s → raccoons','多只浣熊，词尾 /nz/']],
 'young raccoons 是幼年浣熊；raccoons in the garden 是花园里的浣熊；photographs of raccoons 是浣熊照片。',
 'young raccoons；raccoons in the garden；photographs of raccoons。',
 'raccoons 直接数动物；raccoon tracks 的前部通常用单数作修饰，表示浣熊的足迹。',
 ('Two raccoons were exploring the garden.','两只浣熊正在花园里探来探去。'),('The camera recorded raccoons beside the fence.','摄像机拍到了栅栏旁的浣熊。'),sources=S('raccoons','raccoon'))
W('buffaloes','英 /ˈbʌfələʊz/；美 /ˈbʌfəloʊz/','水牛、非洲水牛等；〔北美日常用法〕美洲野牛〔复数〕',
 '田间水牛、草原上的非洲水牛，可以叫 buffaloes；北美故事里的 buffalo 又常在说美洲野牛。要看地域和完整名称。',
 'buffalo 经葡萄牙语、拉丁语向前接希腊动物名称；更远来路不定。buffalo + -es → buffaloes，后缀读 /z/，也见 buffalos 或不变复数 buffalo。',
 [['希腊 boubalos 动物名 → 拉丁 bubalus、bufalus → 葡萄牙语、英语 buffalo','古今所指动物有过转用，更远起源不定'],['buffalo + -es → buffaloes','现代复数；北美口语名称也用于 bison']],
 'water buffaloes 是水牛；African buffaloes 是非洲水牛；a herd of buffaloes 是一群水牛或语境中的野牛。',
 'water buffaloes；African buffaloes；a herd of buffaloes。',
 'bison 是美洲、欧洲野牛的名称；日常 American buffalo 会和它交叉，但不能把亚洲水牛也当同一个物种。',
 ('Water buffaloes stood in the muddy field.','水牛站在泥泞的田里。'),('A herd of buffaloes moved across the plain.','一群水牛穿过平原。'),sources=S('buffaloes','buffalo'))
W('bison','英、美 /ˈbaɪsən/','野牛〔常指美洲野牛、欧洲野牛；单复数常同形〕',
 '肩部高耸、前半身厚重的野牛，可以用 bison。这个词不用每次靠加 s 来表示多只。',
 '经法语 bison、拉丁 bison 接日耳曼语等旧动物名称；更远可能涉及波罗的、斯拉夫语材料，但具体来路不完全确定。',
 [['日耳曼语等旧动物名 → 拉丁 bison → 法语、英语 bison','原先用于欧洲野牛，后来也用于北美野牛'],['英语 bison 的现代用法','常见单复数同形：one bison、several bison']],
 'an American bison 是美洲野牛；European bison 是欧洲野牛；a herd of bison 是一群野牛。',
 'American bison；European bison；a herd of bison。',
 '北美日常 buffalo 常指 bison；名称交叉是历史习惯，两词的借入路线、严格指称并不因此完全相同。',
 ('A bison stood beside the track.','一头野牛站在小路旁。'),('Several bison grazed in the distance.','几头野牛在远处吃草。'),sources=S('bison','bison'))
W('weasel','英、美 /ˈwiːzəl/','鼬；狡猾的人〔贬义〕；推诿、设法逃脱〔常接 out〕',
 '细长身体能钻来钻去的鼬，是 weasel；说人 weasel out of something，就像滑溜溜地钻出难题，不肯承担。',
 '古英语 weosule、wesle 经中古英语传为 weasel；更远词源不定。现代动物形象又借给人的狡猾、设法脱身、含糊推诿等用法。',WEASEL,
 'a weasel in the grass 是草里的鼬；weasel out of a promise 是设法逃避承诺；calling someone a weasel 是贬损地说对方狡猾。',
 'a small weasel；weasel out of a promise；weasel out of doing something。',
 'weasel out 常含不诚实地逃避的批评；普通 get out of 可以较中性地说脱身、免去某事。',
 ('A weasel disappeared into the long grass.','一只鼬钻进了高草丛。'),('Do not try to weasel out of your promise.','别想耍滑头逃避承诺。'),sources=S('weasel','weasel'))
W('weasels','英、美 /ˈwiːzəlz/','鼬〔复数〕；耍滑头逃避〔第三人称单数〕',
 '几只鼬是 weasels；he weasels out of work 则是他耍滑头躲活。看句子里是动物还是逃避的动作。',
 'weasel + -s → weasels，/l/ 后读 /z/；名词复数、动词第三人称单数同形。',WEASEL+[['weasel + -s → weasels','动物复数或人耍滑头逃避，词尾 /əlz/']],
 'small weasels 是小鼬；weasels out of a task 是耍滑头逃掉任务；weasels out of answering 是避而不答。',
 'small weasels；weasels out of work；weasels out of answering。',
 'he weasels out 表主语自己逃避；若说 weasels 在林中活动，通常就是复数动物，别把比喻套到所有句子。',
 ('We saw two weasels near the old wall.','我们在旧墙边看到了两只鼬。'),('He always weasels out of doing the washing-up.','他总是耍滑头躲掉洗碗的活。'),sources=S('weasels','weasel'))
W('ferrets','英 /ˈferɪts/；美 /ˈfɛrɪts/','雪貂〔复数〕；搜寻、查出〔动词，常接 out〕',
 '雪貂爱钻探的形象，也能帮你记 ferrets out the truth：把藏着的信息一点点找出来。',
 'ferret 经法语 furet 等小称接拉丁 fur 贼的词族；动词与借动物搜寻、驱出藏物的关系相连。ferret + -s → ferrets，/t/ 后读 /s/。',
 [['拉丁 fur 贼的词族 → 法语 furet 等小称 → 英语 ferret','动物名借人的拟人化看法，不从现代 fur 毛皮另造'],['相关动词搜寻、驱出 → ferret out 查出；ferret + -s → ferrets','名词复数与第三人称单数动词同形']],
 'pet ferrets 是宠物雪貂；ferrets out information 是搜出信息；ferrets out the cause 是追查出原因。',
 'pet ferrets；ferrets out information；ferrets out the truth。',
 'ferrets out 强调耐心翻找、查出藏着的东西；finds 只说找到，不一定带同样的搜寻过程。',
 ('The ferrets explored every corner of the room.','雪貂们把房间的每个角落都探了一遍。'),('The reporter ferrets out details that others miss.','这位记者会挖出别人漏掉的细节。'),sources=S('ferrets','ferret'))
W('hamster','英 /ˈhæmstə/；美 /ˈhæmstɚ/','仓鼠',
 '小小一团、会把食物塞进颊囊的仓鼠，是 hamster。宠物仓鼠跑轮的画面也很常见。',
 '整词借自德语 Hamster，向前有中古高地德语 hamastra 等形式；更远可能接斯拉夫语言名称，具体分析不确定。',HAMSTER,
 'a pet hamster 是宠物仓鼠；a hamster wheel 是仓鼠跑轮；a hamster cage 是仓鼠笼。',
 'a pet hamster；a hamster wheel；a hamster cage。',
 'hamster 是整词动物名；这里的 -ster 不需要按现代英语职业后缀重新拼成做某事的人。',
 ('The hamster stored seeds in its cheeks.','仓鼠把种子塞在颊囊里。'),('Her pet hamster ran on its wheel.','她的宠物仓鼠在跑轮上跑动。'),sources=S('hamster','hamster'))
W('hamsters','英 /ˈhæmstəz/；美 /ˈhæmstɚz/','仓鼠〔复数〕',
 '几只小仓鼠，就是 hamsters。德语动物名称借进英语后，用英语规则变化复数。',
 'hamster + -s → hamsters，词尾后缀读 /z/；英式常见 /stəz/，美式常见 /stɚz/。',HAMSTER+[['hamster + -s → hamsters','多只仓鼠，词尾 /z/']],
 'pet hamsters 是宠物仓鼠；young hamsters 是幼年仓鼠；pictures of hamsters 是仓鼠图片。',
 'pet hamsters；young hamsters；pictures of hamsters。',
 'hamsters 数动物；hamster wheels 的 hamster 作前部修饰，通常不先加复数 s。',
 ('The children drew pictures of hamsters.','孩子们画了仓鼠的图画。'),('The poster shows several kinds of hamsters.','海报上展示了几种仓鼠。'),sources=S('hamsters','hamster'))
W('hedgehogs','英 /ˈhedʒhɒɡz/；美 /ˈhɛdʒhɑɡz/','刺猬〔复数〕',
 '背上有刺、鼻子尖尖的小动物，是 hedgehogs。英文可直观看成“树篱边的小猪”，借的是活动环境和口鼻形状。',
 'hedge 树篱 + hog 猪 → hedgehog 刺猬；再加 -s → hedgehogs，/ɡ/ 后读 /z/。这是真正的英语复合构词。',
 [['hedge 树篱 + hog 猪 → hedgehog','树篱接常见活动环境，猪接像猪的口鼻'],['hedgehog + -s → hedgehogs','整个复合名词末尾加 s，词尾 /ɡz/']],
 'hedgehogs in the garden 是花园里的刺猬；young hedgehogs 是幼年刺猬；photographs of hedgehogs 是刺猬照片。',
 'hedgehogs in the garden；young hedgehogs；photographs of hedgehogs。',
 'hedgehogs 是刺猬，porcupines 是豪猪；都有刺，不表示两个名称和动物可以直接互换。',
 ('Hedgehogs sometimes visit the garden at night.','夜里有时会有刺猬来到花园。'),('The book has a chapter about hedgehogs.','这本书有一章介绍刺猬。'),sources=S('hedgehogs','hedgehog'))
W('dinosaurs','英 /ˈdaɪnəsɔːz/；美 /ˈdaɪnəˌsɔrz/','恐龙〔复数，日常常指史前非鸟类恐龙〕；过时的人、机构〔比喻〕',
 '博物馆里一排排史前恐龙骨架，是 dinosaurs。借来说人、机构，也能表示固守老办法、跟不上变化。',
 'dinosaur 接近代拉丁 Dinosauria，向前有希腊 deinos 令人畏惧、强大 + sauros 蜥蜴材料；加 -s → dinosaurs，后缀 /z/。这是历史命名，不是说它们都只是放大的现代蜥蜴。',
 [['希腊 deinos 令人畏惧、强大 + sauros 蜥蜴 → 近代拉丁名称','现代英语 dinosaur 的命名材料'],['dinosaur + -s → dinosaurs','既数恐龙，也能比喻不肯适应变化的人或机构']],
 'dinosaur fossils 是恐龙化石；models of dinosaurs 是恐龙模型；corporate dinosaurs 可比喻守旧、反应迟缓的企业。',
 'models of dinosaurs；books about dinosaurs；corporate dinosaurs。',
 '日常 dinosaurs 常说史前非鸟类恐龙；名称里的蜥蜴是命名材料，现代分类不靠字面大小决定。',
 ('The museum has a gallery of dinosaurs.','博物馆里有一个恐龙展厅。'),('Some firms behave like dinosaurs when technology changes.','技术变化时，有些公司像老古董一样固守旧法。'),sources=S('dinosaurs','dinosaur'))
W('dino','英 /ˈdaɪnəʊ/；美 /ˈdaɪnoʊ/','恐龙〔非正式短称〕',
 '小朋友抱着恐龙玩具，说 a dino，就是一只“恐龙”。长词 dinosaur 缩短后，语气更轻松。',
 'dinosaur 截去后部，保留 dino- → dino；现代短称仍指整只恐龙，不只保留希腊词根“可怕”的意思。',
 [['dinosaur 恐龙 → 截短 dino','完整动物名的缩略，而不是把古希腊材料单独借来作同义词'],['英语 dino 作为日常短称','可数名词，也常用于玩具、儿童用品等搭配']],
 'a toy dino 是玩具恐龙；a dino model 是恐龙模型；a dino book 是恐龙主题的书。',
 'a toy dino；a dino model；a dino book。',
 'dino 更随意，dinosaur 适用范围更广；前者的 o 留自原词，不是再新加一个动物后缀。',
 ('The child carried a toy dino everywhere.','孩子走到哪儿都带着一只玩具恐龙。'),('He drew a green dino with a long tail.','他画了一只长尾巴的绿色恐龙。'),sources=S('dino','dinosaur'))
W('dinos','英 /ˈdaɪnəʊz/；美 /ˈdaɪnoʊz/','恐龙〔dino 的复数短称〕',
 '一盒小恐龙玩具，随意口语可以说 a box of dinos。短称也能直接数复数。',
 'dino + -s → dinos，元音后读 /z/；长词 dinosaur、短词 dino 分别有 dinosaurs、dinos 两种形式，意义可对应但语体不同。',
 [['dinosaur → dino','保留原名开头材料的口语截短'],['dino + -s → dinos','多只恐龙、恐龙形象，词尾 /oʊz/']],
 'toy dinos 是玩具恐龙；plastic dinos 是塑料恐龙玩具；pictures of dinos 是恐龙图片。',
 'toy dinos；plastic dinos；pictures of dinos。',
 'dinos 对应短称 dino；dinosaurs 对应完整 dinosaur，不用把两种结尾叠起来。',
 ('The box was full of plastic dinos.','盒子里装满了塑料恐龙玩具。'),('She loves drawing colourful dinos.','她喜欢画五颜六色的恐龙。'),sources=S('dinos','dinosaur'))
W('crocodile','英 /ˈkrɒkədaɪl/；美 /ˈkrɑkəˌdaɪl/','鳄鱼〔常指鳄科类〕',
 '长身体贴着水面、只露出眼鼻的鳄鱼，可以叫 crocodile。词名经过希腊、拉丁、法语，英语拼写也曾多次变化。',
 '希腊 krokodilos 经拉丁 crocodilus、中世纪拉丁与古法语相关形式借入英语；中古英语有 cocodril 等，后来向古典形式靠拢。更远来路不定，不宜硬拆成石子加虫。',CROCODILE,
 'a crocodile in the river 是河里的鳄鱼；a crocodile’s tail 是鳄鱼尾巴；crocodile tears 借传说形象说假哭、假惺惺的眼泪。',
 'a crocodile’s tail；a crocodile in the river；crocodile tears。',
 'alligator 常译短吻鳄，crocodile 是另一常见名称；中文都可能泛译鳄鱼，英语里仍有名称区分。',
 ('A crocodile lay almost hidden in the water.','一条鳄鱼几乎完全隐在水里。'),('He shed crocodile tears over the broken vase.','他对着碎花瓶假惺惺地掉眼泪。'),sources=S('crocodile','crocodile'))
W('crocodiles','英 /ˈkrɒkədaɪlz/；美 /ˈkrɑkəˌdaɪlz/','鳄鱼〔复数〕',
 '河边几条大鳄鱼，是 crocodiles。现代名称虽然来自多次借入、改写，复数只在整词末尾加 s。',
 'crocodile + -s → crocodiles，基础词 e 不发音，/l/ 后加 /z/；读音末尾 /aɪlz/。',CROCODILE+[['crocodile + -s → crocodiles','多条鳄鱼，词尾 /lz/']],
 'crocodiles in the river 是河里的鳄鱼；young crocodiles 是幼年鳄鱼；pictures of crocodiles 是鳄鱼图片。',
 'young crocodiles；crocodiles in the river；pictures of crocodiles。',
 'crocodiles 直接是动物复数；crocodile tears 的前部通常仍用单数词形，整个搭配才是鳄鱼的眼泪这个比喻。',
 ('Several crocodiles rested along the riverbank.','几条鳄鱼伏在河岸边休息。'),('The documentary shows crocodiles moving through shallow water.','纪录片展示了鳄鱼穿行浅水的情景。'),sources=S('crocodiles','crocodile'))
W('alligator','英 /ˈælɪɡeɪtə/；美 /ˈæləˌɡeɪtɚ/','短吻鳄',
 '名字像一个长英语词，最初却含着西班牙语的“那个蜥蜴”：el lagarto。一整个称呼被听进英语，逐渐粘成了 alligator。',
 '西班牙语 el 定冠词 + lagarto 蜥蜴，整体借入英语，出现 lagarto、aligarto 等形式，再变成 alligator；lagarto 更远接拉丁 lacertus、lacerta。',ALLIGATOR,
 'an alligator in the water 是水里的短吻鳄；a young alligator 是幼年短吻鳄；an alligator’s tail 是短吻鳄尾巴。',
 'a young alligator；an alligator’s tail；an alligator in the water。',
 'alligator 与 crocodile 都常在中文里被说成鳄鱼；英语区分名称时，alligator 通常对应短吻鳄类。',
 ('An alligator rested beside the pond.','一条短吻鳄伏在池塘边休息。'),('The picture shows an alligator with its mouth open.','图中是一条张着嘴的短吻鳄。'),sources=S('alligator','alligator'))
W('alligators','英 /ˈælɪɡeɪtəz/；美 /ˈæləˌɡeɪtɚz/','短吻鳄〔复数〕',
 '几条短吻鳄，是 alligators。原先的西班牙语词组借成完整名词后，英语直接给整词加 s。',
 'alligator + -s → alligators，后缀读 /z/；原来的 el、lagarto 不再各自按西班牙语规则形成复数。',ALLIGATOR+[['alligator + -s → alligators','英语整体词的规则复数，词尾 /z/']],
 'young alligators 是幼年短吻鳄；alligators in the pond 是池塘里的短吻鳄；pictures of alligators 是短吻鳄图片。',
 'young alligators；alligators in the pond；pictures of alligators。',
 'alligators 的复数 s 属于现代英语；词源里旧冠词的一部分已并进词中，不再单独当作一个英语词。',
 ('The documentary follows several young alligators.','纪录片跟拍了几条幼年短吻鳄。'),('The sign compares alligators with crocodiles.','说明牌比较了短吻鳄与鳄鱼。'),sources=S('alligators','alligator'))
W('camels','英 /ˈkæməlz/；美 /ˈkæməlz/','骆驼〔复数〕',
 '背上有驼峰、常见于沙漠旅行画面的骆驼，是 camels。名称本身没有限定只能是一峰或两峰。',
 'camel 在古英语已有形式，远处接拉丁 camelus、希腊 kamēlos，再接希伯来语、腓尼基语等闪米特语名称；法语形式也在其传播史中。camel + -s → camels，/l/ 后 /z/。',
 [['闪米特语 gamal 等 → 希腊 kamēlos → 拉丁 camelus','英语有古英语 camel 及法语相关传播形式'],['英语 camel + -s → camels','现代复数，词尾 /əlz/']],
 'a caravan of camels 是一队骆驼；camels carrying goods 是驮货的骆驼；two camels 是两头骆驼。',
 'a caravan of camels；camels carrying goods；two camels。',
 'camels 可以包括单峰、双峰等骆驼；camel hair 的 camel 作前部修饰时，通常仍保持单数。',
 ('A line of camels crossed the desert.','一队骆驼穿过沙漠。'),('The camels carried bags and blankets.','骆驼驮着袋子和毯子。'),sources=S('camels','camel'))
W('flamingo','英 /fləˈmɪŋɡəʊ/；美 /fləˈmɪŋɡoʊ/','火烈鸟',
 '长腿、长脖子，羽毛带粉红或暖红色的火烈鸟，是 flamingo。用“像火焰的颜色”来记，和常见词源分析也能相接。',
 '英语经西葡语 flamengo 等鸟名，通常联系更早普罗旺斯语火焰色材料；其中也可能与弗兰德人的名称形式发生影响，传播细节不能只凭现代英语 flame 的拼写反推。',FLAMINGO,
 'a pink flamingo 是粉红色火烈鸟；a flamingo standing on one leg 是单腿站立的火烈鸟；a flamingo’s feathers 是它的羽毛。',
 'a pink flamingo；a flamingo on one leg；a flamingo’s feathers。',
 'flamingo 是完整鸟名；flaming 是燃烧、火焰般的相关英语词形，不能把它们当作现代同一个词随意互换。',
 ('A flamingo stood on one leg in the shallow water.','一只火烈鸟在浅水里单腿站着。'),('The child painted a bright pink flamingo.','孩子画了一只鲜粉色火烈鸟。'),sources=S('flamingo','flamingo'))
W('flamingos','英 /fləˈmɪŋɡəʊz/；美 /fləˈmɪŋɡoʊz/','火烈鸟〔复数〕',
 '一片粉红色的长腿鸟，是 flamingos。这个常见复数直接加 s。',
 'flamingo + -s → flamingos，元音后读 /z/；这里采用常见 -s 复数，不把所有 -o 词都机械改成 -oes。',FLAMINGO+[['flamingo + -s → flamingos','多只火烈鸟，词尾 /oʊz/']],
 'pink flamingos 是粉红色火烈鸟；a flock of flamingos 是一群火烈鸟；flamingos in shallow water 是浅水里的火烈鸟。',
 'pink flamingos；a flock of flamingos；flamingos in shallow water。',
 'flamingos 的 s 不另添一个 /ɪz/ 音节；与前面的 /oʊ/ 接成 /oʊz/。',
 ('A flock of flamingos gathered in the shallow water.','一群火烈鸟聚在浅水中。'),('The photograph shows flamingos taking flight.','照片里是正在起飞的火烈鸟。'),sources=S('flamingos','flamingo'))
W('pelican','英 /ˈpelɪkən/；美 /ˈpɛlɪkən/','鹈鹕',
 '长嘴下面挂着能伸展的大喉囊，常在水面捕鱼的鸟，是 pelican。先抓住这副长嘴、大袋子的样子。',
 '古英语 pellicane 等接晚期拉丁 pelecanus、希腊 pelekan；中古英语拼写又受法语影响。更远可能与斧、啄木鸟名称相关，鸟喙形状是可能背景。',PELICAN,
 'a pelican’s pouch 是鹈鹕喉囊；a pelican on the water 是水面上的鹈鹕；a brown pelican 是褐鹈鹕。',
 'a pelican’s pouch；a brown pelican；a pelican on the water。',
 '喉囊是记住现代动物的画面；可能的斧形命名分析则属于更远词源，两种线索不必硬说成同一个字面解释。',
 ('A pelican landed on the water.','一只鹈鹕落到了水面上。'),('The pelican scooped a fish into its pouch.','鹈鹕把一条鱼兜进了喉囊。'),sources=S('pelican','pelican'))
W('pelicans','英 /ˈpelɪkənz/；美 /ˈpɛlɪkənz/','鹈鹕〔复数〕',
 '几只长嘴大喉囊的水鸟，是 pelicans。名称传承很老，现代复数却很规则。',
 'pelican + -s → pelicans，/n/ 后读 /z/；基础词常见三音节，复数不另添一个音节。',PELICAN+[['pelican + -s → pelicans','多只鹈鹕，词尾 /nz/']],
 'pelicans by the harbour 是港口边的鹈鹕；a group of pelicans 是一群鹈鹕；pelicans fishing 是捕鱼的鹈鹕。',
 'a group of pelicans；pelicans by the harbour；pelicans fishing。',
 'pelicans 直接数鸟；pelican feathers 的 pelican 作前部修饰，通常不用复数。',
 ('Pelicans floated beside the fishing boats.','鹈鹕漂在渔船旁边。'),('The children counted the pelicans along the harbour wall.','孩子们数着港口堤墙边的鹈鹕。'),sources=S('pelicans','pelican'))
W('ostrich','英 /ˈɒstrɪtʃ/；美 /ˈɑstrɪtʃ/','鸵鸟',
 '身高很显眼、腿长、不会飞却擅长跑的鸵鸟，是 ostrich。它的旧名称甚至有“大麻雀”的命名关系。',
 '经古法语、中世纪拉丁语形式，接通俗拉丁 avis struthio，其中 avis 是鸟，struthio 接希腊鸵鸟名，更早有 strouthos megale 大麻雀的名称关系。',
 [['希腊 strouthos megale 大麻雀等 → strouthion 鸵鸟名','古人借熟悉的鸟名去称另一种大鸟'],['通俗拉丁 avis 鸟 + struthio → 法语、中世纪拉丁语形式 → ostrich','整个名称经多次语音、拼写变化进入现代英语']],
 'an ostrich egg 是鸵鸟蛋；an ostrich feather 是鸵鸟羽毛；an ostrich running 是奔跑的鸵鸟。',
 'an ostrich egg；an ostrich feather；an ostrich running。',
 'ostrich 首音是元音，前面用 an；词尾 /tʃ/，不是只读 /ʃ/。',
 ('An ostrich ran across the open ground.','一只鸵鸟跑过开阔地。'),('The display included a large ostrich egg.','展品中有一枚大鸵鸟蛋。'),sources=S('ostrich','ostrich'))
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_zjc',ROOTS,WORDS)
 extend_lessons()
