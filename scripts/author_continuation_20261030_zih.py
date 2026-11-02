"""Common food, culture and household vocabulary from several borrowing routes."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
def S(word,base):
 urls=['https://en.wiktionary.org/wiki/'+word+'#English']
 urls.append('https://www.merriam-webster.com/dictionary/ninja' if base=='ninja' else 'https://www.etymonline.com/word/'+base)
 return urls
EXISTING_ROOT_ADDITIONS={
 'B3136':dict(words='coconut coconuts'.split(),label='coconut → coconuts：像一张脸的果壳',note='coco 借西班牙、葡萄牙语鬼脸等称呼，果壳三处凹点像面孔；再接 nut。复数加在整个 coconut 末尾，不把 cocoa 可可混进同一水果来源。'),
 'B2489':dict(words='mango mangoes avocado avocados'.split(),label='mango、avocado：不同语言传来的水果名',note='与 fruit 比较水果，不是拉丁 fructus 派生。mango 经葡萄牙语，较远接马来语、泰米尔语等材料；avocado 经西班牙语接纳瓦特尔语水果名，不能按现代英语前缀自由拼。'),
 'C1379':dict(words='cinnamon basil oregano'.split(),label='常见香味植物：cinnamon、basil、oregano',note='与 spice 作烹饪比较，不都从拉丁 species 派生。cinnamon 经法语、拉丁、希腊接闪米特语材料；basil 接希腊王者的；oregano 经西班牙、拉丁接希腊山与光彩、装饰材料。'),
 'C1008':dict(words='parsley'.split(),label='parsley：岩石 + 芹类植物的旧组合',note='parsley 经古英语、法语形式汇合，接拉丁、希腊 petroselinon，petros 石 + selinon 芹类植物；现代外形缩变很大，不能只看 par- 或 -ley 猜英语词缀。'),
 'B4579':dict(words='ninja ninjas'.split(),label='ninja：另源的忍者名称',note='与 stealth 比较隐秘行事，不是 steal 派生。ninja 借日语忍者，nin 接忍的隐忍、隐蔽义，ja 是者、人，属于日语汉字词读法。'),
 'B3064':dict(words='zombie zombies'.split(),label='zombie：另源的僵尸与没精神的人',note='和 dead 比较传说、影视中的死而复动，不由英语 dead 构词。zombie、zombi 的来路通常接西非、海地等语境，具体可能有不止一条旧词线，不能硬定一个非洲词包办所有意思。'),
 'B4294':dict(words='manga'.split(),label='manga：日语漫画名称进入英语',note='和 comic 比较漫画，不从希腊喜剧词根派生。manga 借日语漫画，man 漫、自由不拘一类材料 + ga 画；日语内部的旧用法不等于英语里才新造。'),
 'C0110':dict(words='volleyball'.split(),label='volleyball：球不落地地击来击去',note='volley 运动里指球未落地时回击 + ball，组成排球名；volley 经法语飞行词，接拉丁 volare 飞，和本页 ball 的来路分别看。'),
 'B2711':dict(words='pistol pistols'.split(),label='pistol：另源的手枪名称',note='和 gun 比较武器类型，不是 gun 的派生。pistol 经法语 pistole 等，远源有捷克管子与意大利地名等不同分析，不能定成唯一已知的地点命名。'),
 'B2701':dict(words='salon salons'.split(),label='salon：大房间到聚会、美发店',note='与 room 比较空间，不是 room 派生。salon 经法语接意大利 salone 大厅，sala 厅 + 增大材料 -one；大房间再借给社交聚会、展览与美容美发场所。'),
 'B2460':dict(words='bamboo'.split(),label='bamboo：另源的竹子、竹材',note='与 grass 比较植物类别，不由 grass 派生。bamboo 经荷兰 bamboe 或葡萄牙 bambu，较远可能接马来 samambu 等，后面是否还有借入线不确定。'),
}
MANGO=[['葡萄牙 manga 等 → 英语 mango','较远联系马来 mangga、泰米尔 mankay 等'],['泰米尔对应材料可拆树名 man + 果 kay','现代英语整体为芒果名']]
AVOCADO=[['纳瓦特尔语 ahuacatl 水果名 → 西班牙 aguacate 等','西班牙 avocado 词形受同形律师词影响的分析'],['英语 avocado：牛油果','水果来源不是直接从拉丁律师、呼叫词根派生']]
NINJA=[['日语 忍 nin：隐忍、隐蔽 + 者 ja：人','日语汉字词的读法，不是英语词缀'],['英语 ninja：忍者','现代影视、游戏角色名，也可口语夸某种高手']]
ZOMBIE=[['西非等语言材料，经海地等文化语境进入英语','zombi、zombie 旧义不完全统一，可能不止一条词线'],['亡灵、复动尸体的传说角色 → 影视僵尸；再喻没精神的人','不把传说角色当作真实生物类别']]
SALON=[['意大利 sala 厅 + -one 增大材料 → salone 大厅','法语 salon 接待室 → 英语 salon'],['房间 → 在其中举行的社交、艺术活动；再到美容美发场所','现代 hair salon 很常见，不保证仍是贵族大客厅']]
W('coconuts','英 /ˈkəʊkənʌts/；美 /ˈkoʊkənʌts/','椰子〔复数〕',
 '一颗颗硬壳椰子是 coconuts。看果壳那几个凹点，像一张小脸，这正好能帮助记住名字里 coco 的旧联想。',
 'coco 借西班牙、葡萄牙语鬼脸、怪脸等称呼，接果壳三处凹点像面孔的形状；coco + nut → coconut，整体加 -s → coconuts，读 /s/。',
 [['西班牙、葡萄牙 coco：鬼脸、怪脸 → 椰子相关称呼','果壳三处凹点像人脸或猴脸'],['coco + nut → coconut + -s → coconuts','果实复数，后缀只加在整体末尾']],
 'fresh coconuts 数完整果实；coconut milk、coconut flesh 把名称作材料修饰语，不跟后面的数量任意加复数。',
 'fresh coconuts；a pile of coconuts；coconuts on a palm。',
 'coconuts 椰子与 cocoa 可可不是同一种食物；coconut milk 是椰浆、椰奶，cocoa 是可可材料或相应饮品。',
 ('The stall sold fresh coconuts.','摊位上卖新鲜椰子。'),('Several coconuts lay beneath the palm.','棕榈树下躺着几个椰子。'),sources=S('coconuts','coconut'))
W('mango','英 /ˈmæŋɡəʊ/；美 /ˈmæŋɡoʊ/','芒果；芒果树',
 '熟了后果肉柔软、常见黄橙色的芒果，就是 mango。切一颗可以数 a mango，做成果昔时又按食材说 mango。',
 '经葡萄牙 manga 等借入，较远联系马来 mangga、泰米尔 mankay 等；泰米尔材料里 man 是树名、kay 是果。它在英语中是整体借词。',MANGO,
 'a ripe mango 是熟芒果；mango juice 是芒果汁；树本身也能称 mango 或 mango tree。',
 'a ripe mango；slices of mango；mango juice。',
 'mango 是芒果，manga 在英语常是日本漫画，两者现代词形接近，语言来源、所指不同。',
 ('She sliced a ripe mango for dessert.','她切了一颗熟芒果当甜点。'),('The smoothie contains mango and yoghurt.','果昔里有芒果和酸奶。'),sources=S('mango','mango'))
W('mangoes','英 /ˈmæŋɡəʊz/；美 /ˈmæŋɡoʊz/','芒果〔复数〕',
 '果摊上几颗芒果，是 mangoes。数的是果实，和一杯果昔里有多少芒果果肉不是同一种计数。',
 'mango + -es → mangoes，读 /z/，e 不单独增加音节；mangos 也是可见复数写法，不因此产生水果品种区别。',MANGO+[['mango + -es → mangoes','多个芒果；也有 mangos 变体']],
 'ripe mangoes 是熟芒果；green mangoes 可以指青的、未熟的芒果，具体食用方式看菜谱。',
 'ripe mangoes；a box of mangoes；slice the mangoes。',
 'mangoes 的复数没有额外 /ɪz/ 音节；基础末音是元音 /əʊ/、/oʊ/，再接 /z/。',
 ('We bought three mangoes at the market.','我们在市场买了三个芒果。'),('The mangoes on the windowsill are beginning to soften.','窗台上的芒果开始变软了。'),sources=S('mangoes','mango'))
W('avocado','英 /ˌævəˈkɑːdəʊ/；美 /ˌævəˈkɑdoʊ/','牛油果、鳄梨；牛油果树',
 '切开有一颗大核，果肉细软，常被压成泥抹面包，是 avocado。名字是一条跨语言借入线，不靠现代英语前后缀就能猜出水果。',
 '经西班牙 avocado、aguacate 等，接纳瓦特尔语 ahuacatl 水果名。西班牙词形受旧同形律师词影响的分析，不代表水果本来从拉丁 advocate 词族直接派生。',AVOCADO,
 'a ripe avocado 是熟牛油果；mashed avocado 是牛油果泥；avocado toast 是加牛油果的吐司。',
 'slice an avocado；mashed avocado；avocado toast。',
 'avocado 的颜色名称也可说牛油果绿；绿色食物、衣物未必因此都是这种果实或由它制成。',
 ('She mashed an avocado with a fork.','她用叉子把一个牛油果压成泥。'),('The sandwich contains sliced avocado.','三明治里夹着牛油果片。'),sources=S('avocado','avocado'))
W('avocados','英 /ˌævəˈkɑːdəʊz/；美 /ˌævəˈkɑdoʊz/','牛油果、鳄梨〔复数〕',
 '篮子里放着几个牛油果，是 avocados。词尾直接加 s，发 /z/，不用因为前一个字母是 o 就一律加 es。',
 'avocado + -s → avocados；水果名先整体借入英语，再按英语方式形成复数。',AVOCADO+[['avocado + -s → avocados','多个牛油果，末尾读 /z/']],
 'ripe avocados 是成熟的牛油果；firm avocados 摸着还硬。数量说 two avocados，食材说 mashed avocado。',
 'ripe avocados；two avocados；a bag of avocados。',
 'mango 常写 mangoes，avocado 的常规复数写 avocados。借词末尾同样是 o，复数拼法也要跟着具体词记。',
 ('These avocados are still too firm to mash.','这些牛油果还太硬，压不成泥。'),('We bought two avocados for the salad.','我们买了两个牛油果做沙拉。'),sources=S('avocados','avocado'))
W('cinnamon','英 /ˈsɪnəmən/；美 /ˈsɪnəmən/','肉桂；肉桂粉；肉桂色',
 '想一想热饮上撒的棕色香粉，或卷起来的一小段香树皮。cinnamon 是肉桂，常用的是它的内层树皮，不是一粒种子。',
 '经古法语 cinnamone，接拉丁 cinnamum、cinnamomum 和希腊 kinnamomon；更早与腓尼基语等闪米特语材料相连，希伯来语 qinnamon 是相应旧词。',
 [['闪米特语香料名称 → 希腊 kinnamomon','名称随香料跨语言传播'],['拉丁 cinnamomum 等 → 古法语 cinnamone → 英语 cinnamon','香料名；后来也借指类似的棕红色']],
 'ground cinnamon 是磨成的肉桂粉；a cinnamon stick 是卷状肉桂条。香料按材料用时通常不可数，数的是 spoonfuls、sticks 等。',
 'ground cinnamon；a cinnamon stick；sprinkle cinnamon on porridge。',
 'cinnamon 是具体香料；spice 是香料大类。cinnamon-coloured 描述颜色，不说明东西真的含肉桂。',
 ('She sprinkled cinnamon over the warm porridge.','她在热粥上撒了些肉桂粉。'),('Add a cinnamon stick to the pot.','往锅里放一根肉桂条。'),sources=S('cinnamon','cinnamon'))
W('basil','英 /ˈbæzəl/；美 /ˈbeɪzəl/','罗勒',
 '番茄旁放几片有香气的绿叶，或把绿叶打成青酱，常会用到 basil。先把它看成厨房里一种具体的香草。',
 '经法语 basile、中世纪拉丁 basilicum，接希腊 basilikon，原为“王者的植物”一类说法；basilikos 王者的接 basileus 王。为什么这样命名，并无唯一确定解释。',
 [['希腊 basileus 王 → basilikos 王者的','basilikon 用于这种香草的名称'],['中世纪拉丁 basilicum → 法语 basile → 英语 basil','现代厨房里的罗勒']],
 'fresh basil 是新鲜罗勒；basil leaves 是罗勒叶。词名里的王者背景帮助认亲，不表示现代每次说 basil 都有高贵的语气。',
 'fresh basil；basil leaves；tomato and basil soup。',
 'basil 是一种 herb；herb 是香草、草本植物的大类。读音英美常见差别在第一音节 /bæ/ 与 /beɪ/。',
 ('Tear a few basil leaves over the tomatoes.','撕几片罗勒叶撒在番茄上。'),('The sauce is made with fresh basil and olive oil.','这酱用新鲜罗勒和橄榄油做成。'),sources=S('basil','basil'))
W('oregano','英 /ˌɒrɪˈɡɑːnəʊ/；美 /əˈreɡənoʊ/','牛至；牛至叶香料',
 '披萨、番茄酱里那种干燥小绿叶香料，常是 oregano。它和 basil 都能给菜添香，但各是不同植物的名字。',
 '经西班牙 oregano，接拉丁 origanum 等，再接希腊 oreiganon；传统分析联系 oros 山 + ganos 光彩、装饰，像“山上的光彩”这样一幅命名画面。',
 [['希腊 oreiganon：传统上联系山 + 光彩、装饰','香味植物的旧名，不是现代英语再拼成'],['拉丁 origanum → 西班牙 oregano → 英语 oregano','食谱中的牛至、牛至香料']],
 'dried oregano 是干牛至叶香料；a pinch of oregano 是一小撮牛至。菜单里把它当食材名，通常不加复数。',
 'dried oregano；a pinch of oregano；season with oregano。',
 'oregano 与 basil 可以出现在同一道菜里，名称并不互换。这里的希腊山字材料也不是表示嘴的拉丁 or-。',
 ('Stir a pinch of oregano into the tomato sauce.','往番茄酱里拌入一小撮牛至。'),('The recipe uses dried oregano rather than fresh leaves.','这份食谱用干牛至，而不是鲜叶。'),sources=S('oregano','oregano'))
W('parsley','英 /ˈpɑːsli/；美 /ˈpɑrsli/','欧芹',
 '菜上撒的一点碎绿叶，或汤里加的清香叶子，可以是 parsley。它是欧芹；把中文里不同的“芹、香菜”名称先分开，读食谱就更清楚。',
 '古英语 petersilie 与古法语 peresil 等形式汇合，较远接拉丁 petroselinum、希腊 petroselinon。希腊 petros 石头 + selinon 芹类植物，旧组合大意是“石间的芹”。',
 [['希腊 petros 石 + selinon 芹类植物 → petroselinon','一种带生长环境画面的植物旧名'],['拉丁 petroselinum 等 → 古英语、古法语相应形式 → parsley','长期借用、缩变后，现代外形已很难直接认出 petros']],
 'chopped parsley 是切碎的欧芹；a sprig of parsley 是一小枝欧芹。petros 这条石头词线也能帮助连接本页的 petr- 材料。',
 'chopped parsley；a sprig of parsley；garnish with parsley。',
 'parsley 是欧芹，coriander、cilantro 通常指芫荽、香菜相关材料；外形相似，具体食材不同。',
 ('Sprinkle chopped parsley over the soup.','在汤上撒些切碎的欧芹。'),('She added a sprig of parsley to each plate.','她在每个盘子上放了一小枝欧芹。'),sources=S('parsley','parsley'))
W('ninja','英、美 /ˈnɪndʒə/','忍者；〔口语〕某方面的高手',
 '影视里悄悄潜入、行动隐秘的忍者，是 ninja。口语里还会借这个形象夸人做某件事很熟练，例如 a spreadsheet ninja 表格高手。',
 '借日语 忍者 ninja：nin 对应忍的隐忍、隐藏等义，ja 对应者、人。这里看的是日语汉字词读法，整个名称再借进英语。',NINJA,
 'a ninja 是一名忍者。高手的比喻常带轻松、宣传的口吻，普通工作介绍未必需要这么夸张。',
 'a ninja costume；a ninja character；a spreadsheet ninja。',
 'ninja 的人物形象突出隐秘行动；samurai 指日本武士，两个名称的身份背景不同，不能只因都出现在日本题材里就互换。',
 ('The child wore a ninja costume to the party.','孩子穿着忍者服装参加聚会。'),('Ask Maya for help—she is a spreadsheet ninja.','找玛雅帮忙吧，她可是表格高手。'),sources=S('ninja','ninja'))
W('ninjas','英、美 /ˈnɪndʒəz/','忍者〔复数〕；〔口语〕高手们',
 '游戏里几名忍者一起出现，可以说 ninjas。日语借词到了英语里，也常接英语复数后缀。',
 'ninja + -s → ninjas，词尾元音后接 /z/。ninja 也有单复数同形用法；ninjas 是清楚、常见的英语复数形式。',NINJA+[['ninja + -s → ninjas','多名忍者；也可见同形复数 ninja']],
 'two ninjas 直接数人物；a team of ninjas 是一队忍者。复数后面用 are、were 等相应形式。',
 'two ninjas；a team of ninjas；ninjas in a game。',
 'ninjas 的 s 不另成一个 /ɪz/ 音节；基础词尾是元音 /ə/，再接 /z/。',
 ('Two ninjas appear in the opening scene.','开场镜头里出现了两名忍者。'),('The game lets players choose from several ninjas.','游戏让玩家从几名忍者角色中挑选。'),sources=S('ninjas','ninja'))
W('zombie','英 /ˈzɒmbi/；美 /ˈzɑmbi/','僵尸；〔比喻〕没精打采、反应迟钝的人',
 '影视里身体还在动、却没有正常意识的僵尸，是 zombie。说自己累得像个 zombie，是把“人在动，脑子却没跟上”的画面借来。',
 '英语 zombi、zombie 的记录涉及西非语言及海地等文化语境。Kikongo zumbi、djumbi 一类鬼魂或灵物名称，以及其他神灵名称，都进入过远源讨论，未必是一条旧词线包办全部义项。',ZOMBIE,
 'a zombie film 是僵尸片；feel like a zombie 是觉得自己迷迷糊糊、毫无精神。后者通常是日常夸张。',
 'a zombie film；a zombie character；feel like a zombie。',
 'ghost 常突出没有实体的鬼魂；zombie 在现代影视里通常突出复动的身体。两种角色在具体作品中也可能被重新设定。',
 ('I felt like a zombie after the overnight flight.','坐了一夜飞机后，我整个人都迷迷糊糊的。'),('The film follows a group of survivors during a zombie outbreak.','电影讲一群人在僵尸出没时求生的故事。'),sources=S('zombie','zombie'))
W('zombies','英 /ˈzɒmbiz/；美 /ˈzɑmbiz/','僵尸〔复数〕；〔比喻〕没精神的人们',
 '一群僵尸是 zombies；一群熬夜后目光呆滞的人，也可能被打趣为 zombies。把角色形象搬到日常状态，就懂了比喻。',
 'zombie 已经以 -ie 结尾，直接加 -s → zombies，读 /z/，保留原来的 ie。',ZOMBIE+[['zombie + -s → zombies','基础拼写 -ie 保留；最后的 s 读 /z/']],
 'a crowd of zombies 是一群僵尸；look like zombies 是看起来都没精神。复数不改变这些意思之间的关系。',
 'a crowd of zombies；zombies in a film；look like zombies。',
 'zombie → zombies 是加 -s；party → parties 才是辅音字母 + y 改 -ies。两种拼写不能混套。',
 ('The zombies moved slowly through the empty street.','僵尸们慢慢穿过空荡荡的街道。'),('After the long shift, we all looked like zombies.','上完长班，我们个个看着都没了精神。'),sources=S('zombies','zombie'))
W('manga','英 /ˈmæŋɡə/；美 /ˈmɑŋɡə/','日本漫画；日本漫画作品',
 '翻开一本日本漫画，英语常说 manga。它首先是漫画作品的名称，故事可以搞笑、悬疑、日常，并不限某一种题材。',
 '借日语 漫画 manga：man 对应漫，含自由、不拘一类旧义；ga 对应画。漫画这一名称在日语里已有自己的历史，英语再把整个词借来。',
 [['日语 漫 man + 画 ga → manga','漫与画的汉字词组合，经历日语内部的用法发展'],['日语 manga → 英语 manga','英语中通常指日本漫画，或相应漫画风格']],
 'read manga 把它当一类读物；a manga series 是一套漫画系列。说某一部时 a manga、a manga title 都可按语境使用。',
 'read manga；a manga series；a manga artist。',
 'manga 是漫画；anime 通常是日本动画。一本书被改成动画，可以同时谈它的 manga 原作和 anime 改编。',
 ('She reads manga on the train.','她在火车上看日本漫画。'),('The anime is based on a popular manga series.','这部动画改编自一套受欢迎的日本漫画。'),sources=S('manga','manga'))
W('volleyball','英 /ˈvɒlibɔːl/；美 /ˈvɑlibɔl/','排球运动；排球',
 '把球隔着网击过去，接球时尽量不让它落地。volleyball 的名字就抓住了这种“球在空中，直接回击”的画面。',
 'volley + ball。volley 在球类运动里指球未落地时直接击球；它经法语 volée 飞行等义，接拉丁 volare 飞。ball 是另外一条球的词线。',
 [['拉丁 volare 飞 → 法语 volée 飞行等 → 英语 volley','球类运动中引申为球未落地时回击'],['volley + ball → volleyball','用这种击球画面给排球运动命名，再指所用的球']],
 'play volleyball 是打排球，不加 a；a volleyball 可以是一只排球。beach volleyball 是沙滩排球。',
 'play volleyball；a volleyball team；beach volleyball。',
 'volley 是一种空中直接击球的动作，在其他球类也能出现；volleyball 才是完整的运动名。',
 ('We play volleyball on the beach after work.','下班后我们在沙滩上打排球。'),('A volleyball rolled out of the sports bag.','一个排球从运动包里滚了出来。'),sources=S('volleyball','volleyball'))
PISTOL=[['法语 pistole 等 → 英语 pistol','较远来源有不同分析'],['捷克 pištala 管子等，或意大利 Pistoia 地名等解释','这些是有争议的远源路线，不能选一条写成定论']]
W('pistol','英、美 /ˈpɪstəl/','手枪',
 '电影里人物单手拿着的一把短枪，通常可以称 pistol。先抓“小型手持枪械”这个轮廓，再和范围更宽的 gun 对比。',
 '经法语 pistole 等进入英语。较远来路有日耳曼语形式接捷克 pištala 管子、哨管的分析，也有联系意大利 Pistoia 地名的分析；远源并无唯一确定说法。',PISTOL,
 'a pistol 是一把手枪；a pistol in a film 指作品中出现的手枪。具体机械类型并不是这个词最适合初学时硬拆的内容。',
 'a pistol；carry a pistol；a pistol in a film。',
 'gun 范围较宽，可以指多种枪；pistol 更具体。不能把所有 gun 都翻成手枪。',
 ('The detective found a pistol in the drawer.','侦探在抽屉里发现了一把手枪。'),('The museum displays a pistol from the nineteenth century.','博物馆展出了一把十九世纪的手枪。'),sources=S('pistol','pistol'))
W('pistols','英、美 /ˈpɪstəlz/','手枪〔复数〕',
 '展柜里不止一把手枪，是 pistols。这里把具体器物一把把数出来。',
 'pistol + -s → pistols，词尾 /l/ 后加 /z/；法语借入的枪械名称先成为英语名词，再加英语复数。',PISTOL+[['pistol + -s → pistols','多把手枪；复数后缀读 /z/']],
 'two pistols 是两把手枪；a collection of pistols 是一批手枪收藏。复数不改变它比 gun 更具体的范围。',
 'two pistols；antique pistols；a collection of pistols。',
 'pistols 是手枪复数，rifles 是步枪复数；不能因为两者都是 guns 就忽略名词指的类别。',
 ('The display contains several antique pistols.','展柜里陈列着几把古董手枪。'),('Two pistols lay beside the detective’s notebook.','两把手枪放在侦探的笔记本旁。'),sources=S('pistols','pistol'))
W('salon','英 /ˈsælɒn/；美 /səˈlɑn/','美发店、美容院；沙龙聚会；艺术展览',
 '在日常街景里，salon 往往是做头发、美容的店。它更早的画面却是一间接待客人的大房间：房间里的聚会，又把名称借给了活动。',
 '意大利 sala 厅 + 增大材料 -one → salone 大厅，经法语 salon 进入英语。这里 -one 把空间放大，不是“小房间”后缀。',SALON,
 'hair salon 是美发店；beauty salon 是美容院。literary salon 是文学沙龙，沿着房间内聚会那条线理解。',
 'a hair salon；a beauty salon；a literary salon。',
 'salon 与 saloon 有较远的同源背景，但今天 salon 常见美发美容或文化活动，saloon 则常指酒馆，英式英语中也指一种轿车。',
 ('She booked an appointment at the hair salon.','她在美发店预约了时间。'),('The writer hosted a small literary salon at home.','这位作家在家办了一场小型文学沙龙。'),sources=S('salon','salon'))
W('salons','英 /ˈsælɒnz/；美 /səˈlɑnz/','美发店、美容院〔复数〕；沙龙聚会〔复数〕',
 '一条街上几家美发店，或历史上多处文化聚会，都能用 salons。先看 hair、beauty、literary 等周围词，确定数的是什么。',
 'salon + -s → salons，末尾 /n/ 后加 /z/；基本名词的场所、活动两类用法都能形成复数。',SALON+[['salon + -s → salons','多家店、多个聚会；依修饰语和语境区分']],
 'hair salons 数美发店；literary salons 数文学沙龙。不能见到复数就把较早的聚会义自动换成现代店铺义。',
 'hair salons；beauty salons；literary salons。',
 'salons 与 saloons 只差一个 o，现代常见意思不同；复数后缀并没有把两词变成同一个词。',
 ('Several hair salons have opened near the station.','车站附近新开了几家美发店。'),('The chapter describes the literary salons of nineteenth-century Paris.','这一章描写十九世纪巴黎的文学沙龙。'),sources=S('salons','salon'))
W('bamboo','英、美 /bæmˈbuː/','竹子；竹材',
 '一节一节往上长、茎中空的竹子，是 bamboo。做成椅子、地板后，名称又指竹材：从植物到材料，是很自然的一步。',
 '经荷兰 bamboe 或葡萄牙 bambu 等形式进入英语，较远通常联系马来 samambu 等。是否还接更早的南亚语言借入线，并不完全确定。',
 [['马来 samambu 等材料 → 荷兰 bamboe、葡萄牙 bambu 等','跨语言借入路线的细节仍有不确定处'],['英语 bamboo：竹子 → 竹材','植物名转用于制作物品的材料']],
 'bamboo grows fast 说植物；made of bamboo 说材料。竹子在植物分类上属于禾本科，即使长得高，也不是因为像树就变成英语 tree 的派生。',
 'bamboo shoots；a bamboo chair；made of bamboo。',
 'bamboo shoots 是竹笋，shoots 在这里是新生嫩茎；a bamboo chair 是竹椅，材料名称通常用单数形式修饰。',
 ('Bamboo grows along the edge of the garden.','花园边上长着竹子。'),('The chair is made of bamboo.','这把椅子是竹子做的。'),sources=S('bamboo','bamboo'))
def extend_lessons():
 extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_zih',ROOTS,WORDS)
 extend_lessons()
