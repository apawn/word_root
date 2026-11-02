"""Useful everyday nouns: creatures, buildings, coverings, stone and fragments."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
def S(word,base):
 return ['https://en.wiktionary.org/wiki/'+word+'#English','https://www.etymonline.com/word/'+base]
EXISTING_ROOT_ADDITIONS={
 'C0399':dict(words='fairy fairies'.split(),label='fairy：仙境到仙子',note='fairy 接古法语 faerie、fee 仙子与 -erie 材料，早有仙境、魔法义，再指其中的居民。较远连到拉丁 Fata 命运女神是常见分析，但也有其他来源分析，不能定为唯一答案。'),
 'B3082':dict(words='barn barns'.split(),label='barn：谷物的屋子',note='和 house 比较建筑用途，不表示由现代 house 派生。barn 承古英语 bere 大麦 + ærn 房屋、储存处的旧组合，后来缩合；今天不只存大麦。'),
 'B2557':dict(words='clan clans'.split(),label='clan：枝条到后代、宗族',note='clan 经盖尔语 clann 家族、后代，较远借拉丁 planta 新枝、萌芽材料；不是现代英语 plant 删字母形成。'),
 'B2877':dict(words='hut huts'.split(),label='hut：遮蔽人的小屋',note='hut 经法语 hutte、中高地德语 hütte 小屋材料借入，可能与 hide 的更远遮蔽词族相关；不是现代 hide 的直接派生。'),
 'B3904':dict(words='envelope envelopes'.split(),label='envelope：另源的包覆物、信封',note='与 wrap 比较包裹功能，不是 wrap 派生。envelope 借法语 enveloppe，法语名词由 envelopper 包裹形成；更远 voloper 来源未定。'),
 'C1105':dict(words='porch porches'.split(),label='porch：门前的有顶空间',note='porch 经古法语 porche 接拉丁 porticus 有顶廊道，再接 porta 门、入口；与 port 的入口、通过材料比较，不等于现代 port 直接加词尾。'),
 'B3112':dict(words='marble marbles'.split(),label='marble：石材到弹珠',note='与 stone 比较材料，不是 stone 的派生。marble 经法语 marbre 接拉丁 marmor、希腊 marmaros 等，较远闪亮分析未定。弹珠早与石料制作有关，现代可用玻璃。'),
 'B2763':dict(words='ivory'.split(),label='ivory：另源的象牙与象牙白',note='和 tooth 比较动物牙质材料，不是 tooth 的派生。ivory 经法语、拉丁 eborium、ebur，远源可能涉及非洲语言借入线，不硬造唯一完整路线。'),
 'B3808':dict(words='niche niches'.split(),label='niche：凹龛到适合自己的位置',note='和 nest 比较容身空间；niche 经法语，远源有意大利贝壳、小凹处与拉丁 nidus 巢等不同分析，不能把其中任一条定为已证实。'),
 'B2828':dict(words='debris'.split(),label='debris：另源的破碎残余物',note='和 break 比较打碎后的结果，不从英语 break 构词。debris 借法语 débris，接 debriser 打碎与 briser 破裂材料，更远有高卢来源分析。'),
 'B2627':dict(words='owl owls'.split(),label='owl：叫声命名的猫头鹰',note='与 bird 比较鸟类名称，不从 bird 构词。owl 承古英语 ule，接更早日耳曼材料，远源通常联系模仿呼叫、啼声的声音材料。'),
}
FAIRY=[['古法语 fee 等仙子名 + -erie → faerie','较远与拉丁命运女神的关系有不同分析'],['仙境、魔法 → 仙境居民 → 常见小仙子形象','不把所有早期传说人物都画成带小翅膀']]
BARN=[['古英语 bere 大麦 + ærn 房屋、储存处 → bereærn','储藏大麦的建筑'],['中古英语 bern 等 → barn','现代农用仓、牲畜棚等，不限大麦']]
CLAN=[['拉丁 planta 新枝、萌芽 → 盖尔语 clann 后代、家族','枝条的延续可用来理解后代这条比喻'],['盖尔语家族、宗族 → 英语 clan','先见传统宗族，再见口语一大家子、团体']]
HUT=[['中高地德语 hütte 小屋 → 法语 hutte','可能接更早遮蔽的日耳曼材料'],['英语 hut','简易小屋；现代不限定一种建材']]
ENVELOPE=[['法语 envelopper 包裹 → 名词 enveloppe 包覆物','更远 en- 向内与 voloper 包裹，后者来历未定'],['英语 envelope','信封；更广的外包层，名词重音在前']]
PORCH=[['拉丁 porta 门 → porticus 有顶廊道','古法语 porche → 英语 porch'],['门前有顶入口 → 门廊、建筑外侧有顶空间','现代布局、地区用法有差别']]
MARBLE=[['法语 marbre ← 拉丁 marmor、希腊 marmaros 等','较远闪亮的分析未定；英语词形有 r/l 历史变化'],['大理石 → 石制小球 → 弹珠','现代弹珠可由玻璃制作；理智的俚语另有分析']]
NICHE=[['法语 niche 小凹处、龛 → 英语 niche','远源有贝壳、巢等不同分析'],['容纳物件的位置 → 合适的角色、细分位置','生态、市场等语境各有引申用途']]
OWL=[['古英语 ule ← 更早日耳曼材料','通常联系模仿呼叫、猫头鹰啼声的材料'],['英语 owl 猫头鹰 → night owl 夜猫子','借夜间活动习惯说晚睡的人']]
W('fairy','英 /ˈfeəri/；美 /ˈferi/','仙子；小精灵；仙境般的〔修饰用法〕',
 '今天童话里挥魔杖、可能带小翅膀的角色，常叫 fairy。不过旧传说的 fairy 不一定都小，也不一定都有翅膀。',
 '经古法语 faerie，接 fee 仙子与 -erie 材料，英语较早有仙境、魔法义，再指其中居民。更远连到拉丁命运女神是常见分析，也有别的来源分析。',FAIRY,
 'a fairy godmother 是仙女教母；fairy tales 是童话，不要求每篇都出现一位 fairy。',
 'a little fairy；a fairy godmother；a fairy tale。',
 'fairy 不能简单拆成 fair 美丽加 -y；它有自己的法语借入史。童话 fairy 与传统故事中的 elf、spirit 形象有重叠，却不是严格一一对应。',
 ('A fairy appeared and offered to help her.','一位仙子出现了，说愿意帮助她。'),('The child dressed as a fairy for the party.','孩子扮成仙子去参加聚会。'),sources=S('fairy','fairy'))
W('fairies','英 /ˈfeəriz/；美 /ˈferiz/','仙子、小精灵〔复数〕',
 '故事里几位神奇角色一起出现，是 fairies。看古老传说时，别因为这个词就自动补上迷你身体和蝴蝶翅膀。',
 'fairy 的 y 改 i 加 -es → fairies，读 /z/；基础词本身是法语借入线，不按 fair 重新造一条词源。',FAIRY+[['fairy → fairies','y 改 i 加 -es，多个相应传说角色']],
 'stories about fairies 说仙子、精灵故事；believe in fairies 是相信有这类神奇存在。',
 'woodland fairies；stories about fairies；fairies in the garden。',
 'fairies 是虚构或民间信仰中的存在，fairy tales 是故事类别；关于神奇事物的故事未必以 fairies 为主角。',
 ('The book tells stories about fairies in the woods.','书里讲了树林中仙子的故事。'),('Several children came to the party dressed as fairies.','几个孩子打扮成仙子来参加聚会。'),sources=S('fairies','fairy'))
W('barn','英 /bɑːn/；美 /bɑrn/','农用仓房；谷仓；牲畜棚',
 '农场里一座大屋，用来放干草、谷物、农具，有时也安置牲畜，是 barn。旧名字像在说“大麦住的屋子”。',
 '承古英语 bere 大麦 + ærn 房屋、储存处 → bereærn，经过缩合、变音成为 barn。今天用途已经扩大，不是只能存大麦。',BARN,
 'store hay in the barn 是把干草存进仓房；an old barn converted into a house 是由旧农用仓改建的住宅。',
 'a wooden barn；a barn full of hay；the barn door。',
 'barn 常是农场的较大仓棚，shed 更广、常较小，stable 特别偏养马的厩；具体建筑功能可以重叠。',
 ('The farmer stored the hay in the barn.','农民把干草存进了仓房。'),('They converted an old barn into a home.','他们把一座旧农用仓改成了住宅。'),sources=S('barn','barn'))
W('barns','英 /bɑːnz/；美 /bɑrnz/','农用仓房、谷仓、牲畜棚〔复数〕',
 '农场上几座分开放草料、农具或牲畜的大仓棚，可以叫 barns。用途不同不妨碍都保留这个建筑名。',
 'barn + -s，/n/ 后读 /z/；旧大麦屋子的缩合已在基础词里，现代复数直接加后缀。',BARN+[['barn + -s → barns','多座农场仓棚']],
 'old barns、stone barns 说年代、材料；several barns 数独立建筑，不是数里面几堆干草。',
 'wooden barns；old farm barns；barns beside the fields。',
 'barns 是建筑，farms 是农场整个单位；一家 farm 可以有几座 barns，不应按一座建筑就数一家农场。',
 ('Two red barns stood beside the fields.','田边立着两座红色农用仓。'),('The village restored several old barns.','村里修复了几座旧仓房。'),sources=S('barns','barn'))
W('clan','/klæn/','宗族、氏族；一大家子；紧密团体',
 '许多代人像同一棵树不断长出枝条，连成一个大家族，这幅画面能帮助记 clan。口语也会把一大家子亲切地叫 the whole clan。',
 '经盖尔语 clann 后代、家族，较远借拉丁 planta 新枝、萌芽材料。借入盖尔语时词首发生变化，不是现代英语 plant 任意删字母。',CLAN,
 'a Scottish clan 常是历史宗族；the whole clan 可轻松说全家老小；游戏里的 clan 则是组织紧密的玩家团体。',
 'a Scottish clan；the whole clan；a gaming clan。',
 'clan 不必只指现代同住的小家庭，nuclear family 则有更具体家庭范围；玩家 clan 又未必有血缘。',
 ('The museum explains the history of a Scottish clan.','博物馆介绍了一个苏格兰宗族的历史。'),('The whole clan gathered for her birthday.','全家老小都聚来给她过生日。'),sources=S('clan','clan'))
W('clans','/klænz/','宗族、氏族、紧密团体〔复数〕',
 '不同宗族，或游戏里分头组织的几个团队，可以叫 clans。数的是一组组有共同身份、认同的人。',
 'clan + -s，/n/ 后读 /z/；盖尔语借词在现代英语里按普通名词成复数。',CLAN+[['clan + -s → clans','多个宗族或紧密团体']],
 'rival clans 是相互竞争的宗族、团体；several clans 可以是历史族群，也可以是游戏组织。',
 'Scottish clans；rival clans；members of different clans。',
 'clans 是多个团体，clan members 是成员；五个 clans 不表示总共只有五个人。',
 ('The book describes the traditions of several clans.','书里介绍了几个宗族的传统。'),('Players from different clans met in the tournament.','来自不同团队的玩家在比赛中碰面了。'),sources=S('clans','clan'))
W('hut','/hʌt/','简易小屋；棚屋',
 '能遮风避雨，结构却比较简单的小屋，常叫 hut。可以是木屋、石屋、草棚，不是只有茅草才配用这个词。',
 '经法语 hutte 借入，接中高地德语 hütte 小屋；可能与更早遮蔽、隐藏的日耳曼材料相关。不是从现代 house 或 hide 直接新造。',HUT,
 'a wooden hut 是简易木屋，a mountain hut 是山中可歇脚、住宿的小屋；具体舒适程度看实际设施。',
 'a fishing hut；a wooden hut；a mountain hut。',
 'hut 强调小、简易，cottage 常指小住宅，可能很舒适；两者形象重叠，但别把所有乡村小屋都说成破棚屋。',
 ('They took shelter in a small wooden hut.','他们躲进一间简易小木屋避雨。'),('The mountain hut had room for six walkers.','山间小屋能容纳六名徒步者。'),sources=S('hut','hut'))
W('huts','/hʌts/','简易小屋、棚屋〔复数〕',
 '海边几间渔棚，或山路沿线几个歇脚小屋，是 huts。它数一个个建筑，不一定在说有人长期居住。',
 'hut + -s，/t/ 后读 /s/；不增加音节。普通复数不改变基础借词的德语、法语路线。',HUT+[['hut + -s → huts','多间简易小屋']],
 'fishing huts、beach huts、mountain huts 都可用；材料与用途靠前面的修饰语交代。',
 'wooden huts；fishing huts；huts along the trail。',
 'huts 是建筑，tents 是搭起来的帐篷；两者都可临时避雨，却不是同一种结构。',
 ('Small fishing huts lined the shore.','岸边排列着几间小渔棚。'),('The map shows mountain huts along the route.','地图标出了路线沿途的山间小屋。'),sources=S('huts','hut'))
W('envelope','英 /ˈenvələʊp/、/ˈɒnvələʊp/；美 /ˈenvəloʊp/、/ˈɑnvəloʊp/','信封；外包层、包覆物',
 '一张信纸外面再包一层，那个包住内容的东西是 envelope。信封最常见，气球、器物等的外层也可借这个包覆画面。',
 '借法语 enveloppe 包覆物，法语名词由 envelopper 包裹形成；较远是 en- 向内与 voloper 包裹，后者来历未定。不是英语名词一律先于相关动词。',ENVELOPE,
 'put a letter in an envelope 是把信放进信封；push the envelope 是突破边界、探索极限的比喻，不能按字面推信封理解。',
 'a sealed envelope；an empty envelope；address an envelope；push the envelope。',
 'envelope 名词末尾有 e、重音在前；envelop 动词包住没有末尾 e、重音在后，通常读 /ɪnˈveləp/。',
 ('She sealed the letter in an envelope.','她把信装入信封并封好了。'),('The team likes to push the envelope with unusual designs.','团队喜欢用不寻常的设计探索新的边界。'),sources=S('envelope','envelope'))
W('envelopes','英 /ˈenvələʊps/ 等；美 /ˈenvəloʊps/ 等','信封、外包层〔复数〕',
 '桌上一叠空信封，是 envelopes；写邀请函时，信纸和信封是两种不同用品，不能混着数。',
 'envelope + -s，/p/ 后读 /s/；末尾 e 不发音，复数读音接在 /p/ 后，不另读一个音节。',ENVELOPE+[['envelope + -s → envelopes','多个包覆物；日常最常是信封']],
 'address the envelopes 是给信封写收件信息，seal the envelopes 是封口；paper envelopes 说纸信封。',
 'blank envelopes；sealed envelopes；a pack of envelopes。',
 'envelopes 是名词复数，envelops 没有词尾 e 是相关动词三单；Fog envelops the hill 说雾包住山，不是几个信封。',
 ('She wrote the addresses on the envelopes.','她把地址写在信封上。'),('The drawer contains a pack of empty envelopes.','抽屉里放着一包空信封。'),sources=S('envelopes','envelope'))
W('porch','英 /pɔːtʃ/；美 /pɔrtʃ/','门廊；入口前或建筑外侧的有顶空间',
 '还没进屋，门前有一块能站人、遮雨的有顶空间，就是 porch。美式房屋里，它也常大到可以摆椅子、坐着聊天。',
 '经古法语 porche，接拉丁 porticus 有顶廊道，再接 porta 门、入口。借词历史联系门口，不是每个现代 porch 都有古典柱廊。',PORCH,
 'the front porch 是前门廊，the back porch 是屋后门廊；a screened porch 用纱网围护，可减少虫子进入。',
 'sit on the porch；the front porch；a porch light。',
 'porch 常在地面入口附近，balcony 常是较高楼层伸出的阳台；都有外部空间，不等于位置相同。',
 ('We sat on the porch and watched the rain.','我们坐在门廊上看雨。'),('She left the parcel beside the porch light.','她把包裹放在门廊灯旁。'),sources=S('porch','porch'))
W('porches','英 /ˈpɔːtʃɪz/；美 /ˈpɔrtʃɪz/','门廊、建筑外侧有顶空间〔复数〕',
 '一排房子各有可以坐人的门廊，放在一起就是 porches。它们可能大小、围护方式都不同。',
 'porch + -es，/tʃ/ 后读 /ɪz/；多个入口有顶空间，词尾增加一个音节。',PORCH+[['porch + -es → porches','多个门廊，/tʃ/ 后 -es 读 /ɪz/']],
 'front porches 强调屋前，covered porches 强调有顶；建筑布局要看具体房子。',
 'front porches；wooden porches；houses with porches。',
 'porches 是门廊，entrances 是入口，更广；一个入口可以只有门，没有可停留、坐人的门廊。',
 ('Many houses on the street have wide porches.','街上许多房子都有宽门廊。'),('Neighbours sat on their porches in the evening.','傍晚，邻居们坐在各自的门廊上。'),sources=S('porches','porch'))
W('marble','英 /ˈmɑːbəl/；美 /ˈmɑrbəl/','大理石；弹珠；大理石制的、纹理状的',
 '雕像、地板上有纹路的石材，是 marble；孩子手里滚着的玻璃弹珠，也叫 a marble。弹珠名字保留了早年用石材做球的来历。',
 '经法语 marbre，接拉丁 marmor、希腊 marmaros 等材料，远源未定。英语有 r 变 l 等词形变化；大理石制小球再扩大到其他材料弹珠。',MARBLE,
 'made of marble 按材料不可数；a glass marble 可数一颗弹珠；marble cake 说两色面糊形成的大理石纹蛋糕。',
 'a marble statue；a marble floor；a glass marble；marble cake。',
 'marble 数材料时不可数，数玩具小球时可数；a piece of marble 是一块石料，a marble 常是一颗弹珠。',
 ('The statue is carved from white marble.','雕像由白色大理石雕成。'),('A glass marble rolled under the chair.','一颗玻璃弹珠滚到了椅子下面。'),sources=S('marble','marble'))
W('marbles','英 /ˈmɑːbəlz/；美 /ˈmɑrbəlz/','弹珠〔复数〕；弹珠游戏；理智、清醒判断〔口语〕',
 '一袋圆圆的小球是 marbles，拿来一起玩的游戏也叫 marbles。lose your marbles 又是口语“犯糊涂、失去理智”，不是一定真把玩具弄丢了。',
 'marble + -s，/l/ 后读 /z/；玩具、游戏名承接石制小球材料。理智的俚语来源有另与旧家当词相关的分析，不硬编成弹珠等于脑细胞。',MARBLE+[['marble + -s → marbles','多颗弹珠、游戏；另有理智的口语用法']],
 'play marbles 是玩弹珠；a bag of marbles 数玩具；lost his marbles 常是夸张说某人做事太离谱。',
 'glass marbles；play marbles；lose your marbles。',
 'marbles 可以是游戏名，也可以是玩具复数；Marbles is a game 以游戏看待，The marbles are in the bag 数实物。',
 ('The children were playing marbles in the yard.','孩子们正在院子里玩弹珠。'),('You want to walk there in this rain? Have you lost your marbles?','下这么大雨你还想走过去？你是不是糊涂了？'),sources=S('marbles','marble'))
W('ivory','英 /ˈaɪvəri/；美 /ˈaɪvəri/','象牙、牙质材料；象牙白、乳白色',
 'ivory 先是象牙等牙质材料名，后来借那种偏暖的白色说颜色。an ivory dress 通常在讲色调，不是整条裙子用象牙做的。',
 '经盎格鲁法语 ivorie 等，接中古拉丁 eborium、拉丁 ebur 象牙；更远可能经腓尼基语连到非洲来源，完整路线不完全确定。后来有制品、颜色等引申。',
 [['拉丁 ebur、eborium → 法语 ivorie 等 → ivory','较远非洲语言借入线有分析'],['牙质材料 → 相应制品；再借颜色说象牙白','现代颜色用法不保证实物含这种材料']],
 'an ivory carving 是象牙雕刻品；an ivory blouse 通常是象牙白上衣；ivory tower 象牙塔常比喻远离现实的学术、理想环境。',
 'ivory colour；an ivory dress；an ivory tower。',
 'ivory colour 命名色调，ivory material 命名材质；颜色相同不代表材料相同。',
 ('The museum displayed an old ivory carving.','博物馆展出了一件古老的象牙雕刻品。'),('She wore an ivory blouse with dark trousers.','她穿着一件象牙白上衣，配深色长裤。'),sources=S('ivory','ivory'))
W('niche','/niːʃ/ 或 /nɪtʃ/','壁龛、小凹处；适合自己的位置；细分领域；生态位',
 '墙里凹进去一小块，刚好放一尊小像，是 niche。一个人找到自己擅长、能发挥的位置，也像找到了刚好装得下自己的那一格。',
 '借法语 niche 凹处、龛，远源有意大利小凹处、贝壳，以及拉丁巢等不同分析，未统一。后来由实际小空间扩到适合的角色、细分领域与生态用途。',NICHE,
 'find your niche 是找到适合自己的位置；a niche market 是范围较小、需求专门的市场；生态 niche 不只等于地理住址。',
 'a niche in the wall；find a niche；a niche market；an ecological niche。',
 'niche 的生态义包括生物怎样利用资源、发挥作用，habitat 偏居住环境；在同一 habitat 中也可有不同 niches。',
 ('A small statue stood in a niche in the wall.','墙上的壁龛里放着一尊小像。'),('She found her niche in children’s publishing.','她在儿童出版领域找到了适合自己的位置。'),sources=S('niche','niche'))
W('niches','/ˈniːʃɪz/ 或 /ˈnɪtʃɪz/','壁龛、适合的位置、细分领域、生态位〔复数〕',
 '墙上几处小凹龛，或不同人各自擅长的位置，都可以说 niches。不是凡有 niches 就代表市场狭小，也可能在谈墙面或生态。',
 'niche + -s，末音 /ʃ/ 或 /tʃ/ 后后缀读 /ɪz/；保留末尾 e 的书写形式。两种基础读法都有对应复数。',NICHE+[['niche + -s → niches','多个凹龛、专门位置；后缀读 /ɪz/']],
 'market niches 是不同细分领域；ecological niches 是生态位；wall niches 是墙面凹龛。',
 'different niches；market niches；ecological niches。',
 'niches 的拼写没有再加第二个 e：基础 niche 加 -s 即可；不是照读音写成 nichees。',
 ('Small statues filled the niches along the wall.','墙边各个壁龛里摆着小雕像。'),('The company serves several specialised market niches.','公司服务于几个专门的细分市场。'),sources=S('niches','niche'))
W('debris','英 /ˈdebriː/；美 /dəˈbriː/','碎片、残骸、散落的残余物〔通常不可数〕',
 '东西被撞坏、拆掉后，地上散着木块、玻璃、碎石，这一片残余统称 debris。它像把“破碎后留下的一堆”整体拍进镜头。',
 '借法语 débris 残余物，接旧动词 debriser 打碎、压碎，其中 de- 与 briser 破裂结合；更远可能接高卢材料。末尾 s 是借词拼写，通常不发音。',
 [['法语 de- + briser → debriser 打碎','briser 更远有高卢来源分析'],['法语 débris → 英语 debris','破碎后残余物；英语通常不可数，末尾 s 不读']],
 'clear away debris 是清理残余物；pieces of debris 数碎片；space debris 是太空碎片，仍常按整体材料说。',
 'building debris；floating debris；clear debris；pieces of debris。',
 'debris 通常不是普通可数复数；说 The debris was removed，数一块用 a piece of debris，不因末尾 s 就配 are。',
 ('Workers cleared debris from the road.','工人们清走了路上的残骸。'),('A piece of debris was floating near the boat.','船边漂着一块碎片。'),sources=S('debris','debris'))
W('owl','/aʊl/','猫头鹰；晚睡的人〔常见于 night owl〕',
 '大眼睛、夜间活动，是猫头鹰最常见的印象。把总熬到很晚的人叫 a night owl，也就是中文很像的夜猫子。',
 '承古英语 ule，接更早日耳曼同族材料，远源通常联系模仿啼叫、呼声的声音。现代 owl 整体识别，不必拼成普通前后缀。',OWL,
 'a barn owl 是仓鸮；a night owl 是夜猫子。鸟名来源可能模仿声音，不表示所有猫头鹰都发完全一样的叫声。',
 'an owl in the tree；a barn owl；be a night owl。',
 'owl 的 ow 读 /aʊ/，像 how，不像 snow 的 /əʊ/、/oʊ/；night owl 比喻晚睡的人，不限定在夜间工作。',
 ('An owl called from the trees.','树林里传来一只猫头鹰的叫声。'),('I am a night owl and often read late into the night.','我是个夜猫子，经常读书读到很晚。'),sources=S('owl','owl'))
W('owls','/aʊlz/','猫头鹰〔复数〕；晚睡者〔依语境〕',
 '几只猫头鹰是 owls；一群喜欢晚睡的人可叫 night owls。夜间活动的画面相同，一个在谈鸟，一个在谈人。',
 'owl + -s，/l/ 后读 /z/；基础 /aʊ/ 保留，不因为复数变成另一个 ow 读音。',OWL+[['owl + -s → owls','多只猫头鹰；night owls 又可指多个晚睡者']],
 'barn owls、snowy owls 指不同鸟类；night owls 在谈生活习惯时通常说人。',
 'owls at dusk；barn owls；a family of night owls。',
 'night owls 与 early birds 可对照晚睡者、早起者；两者借鸟类形象形容作息，不一定在讨论真实鸟类。',
 ('We heard owls calling after sunset.','日落后，我们听到了猫头鹰的叫声。'),('Most of my friends are night owls.','我的朋友大多是夜猫子。'),sources=S('owls','owl'))
def extend_lessons():
 extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_zib',ROOTS,WORDS)
 extend_lessons()
