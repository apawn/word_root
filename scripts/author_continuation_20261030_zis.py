"""Familiar plants, observable naming images and independent homograph histories."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
def S(word,base):return ['https://en.wiktionary.org/wiki/'+word+'#English','https://www.etymonline.com/word/'+base]
EXISTING_ROOT_ADDITIONS={
 'B2679':dict(words='lilac lilacs'.split(),label='lilac：另源的丁香花与浅紫色',note='与 flower 比较花卉，不从拉丁 flos 派生。lilac 经法语等接土耳其 leylak 植物名，较远来源有争论；植物名再借给花色、香气。'),
 'B4240':dict(words='lily lilies'.split(),label='lily → lilies：借来的百合名与英语复数',note='古英语 lilie 接拉丁 lilia、lilium 等植物名，较远可能是东地中海借词。拉丁 lilia 本为复数，也不决定现代英语 lily 必须复数；现代 lily 变 y 为 i 加 -es。'),
 'B2422':dict(words='daisy daisies'.split(),label='day 的旧组合：day’s eye → daisy',note='古英语 dæges eage 白天的眼睛，以随日光开合的花作眼睛命名，缩变为 daisy；现代复数 daisies。day、eye 的旧组合并不保留现代完整拼写。'),
 'C0912':dict(words='orchid orchids'.split(),label='orchid → orchids：形状命名的兰花名称',note='orchid 接近代拉丁兰科名，较远接希腊 orkhis 睾丸及兰花名，因为部分兰花地下块茎的形状。现代 d 和植物学词形处理有关，不是英语独立的花朵后缀。'),
 'B3620':dict(words='orchard orchards'.split(),label='orchard → orchards：旧园地词组合到果园',note='古英语 orceard、ortgeard 等，可能接 wyrt 植物 + geard 园地，词形也受拉丁 hortus 园影响的分析。现代不是 orchard 直接从 orchid 兰花派生。'),
 'B4209':dict(words='moss mosses'.split(),label='moss → mosses：苔藓植被与种类复数',note='古英语 meos 苔藓、mos 沼地及北欧等形式同接潮湿词族；植物、沼泽哪义最先不能确排。mosses 常数苔藓种类、不同植物，不要求普通一层苔藓每次都复数。'),
 'B2557':dict(words='fern ferns clover clovers ivy ivies'.split(),label='fern、clover、ivy：各自来源的常见植物名',note='与 plant 比较植物，不是 planta 派生。fern 接古英语 fearn，可能更远以羽状叶命名；clover 接古英语 clafre，黏稠材料分析仍有不确定；ivy 接古英语 ifig，远源不明。'),
 'B3333':dict(words='clove cloves'.split(),label='clove：香料像钉子；蒜瓣另源',note='香料 clove 经法语 clou de girofle 接拉丁 clavus 钉子，以花蕾像钉子的形状命名；蒜瓣 clove 则接古英语 clufu 裂开的块，与 cleave 分裂词族有关。不能让钉子一条线包办两种名词。'),
 'B3689':dict(words='oak oaks'.split(),label='oak → oaks：橡树个体与木材用法',note='oak 接古英语 ac，并有北欧对应词影响，较远日耳曼语以外的来源不确定。oaks 数多棵树；oak furniture 的单数材料修饰语不因来自多树就加复数。'),
 'B3284':dict(words='poppy poppies'.split(),label='poppy → poppies：花名与现代英语复数',note='古英语 popig 等接日耳曼语借入的拉丁 papaver 等罂粟花名；较远拟声或膨胀材料解释并不完全确定。poppy 变 y 为 i 加 -es，后缀读 /z/。'),
 'B2615':dict(words='willow willows'.split(),label='willow：另源的柳树与柔软枝条',note='与 tree 比较树木，不从 tree 派生。willow 接古英语 welig、日耳曼语柳树名，更远可能接弯转词族，和柔软可弯枝条的关系有助记忆，但远源分析仍保留可能。'),
}
LILAC=[['土耳其 leylak → 法语 lilac 等 → 英语 lilac','更远来源有争论，先认稳定的借入植物名'],['丁香花、灌木 → 浅紫花色、相应香气','植物名和颜色名用同一现代词']]
DAISY=[['古英语 dæges eage：白天的眼睛','day 的旧属格 + eye 的旧词形，借花随日光开合的形象'],['古英语组合缩变 → 中古英语 daiseie 等 → daisy','现代英语整体为花名，再形成 daisies']]
FERN=[['日耳曼语植物名 → 古英语 fearn → fern','更远可能联系羽毛、翅膀材料，以叶片形状命名，属于分析而非确证'],['英语 fern：蕨类植物','常见羽状叶帮助认植物；并不要求所有蕨叶形状完全相同']]
CLOVER=[['古英语 clafre、clæfre → 中古英语 claver → clover','较远来源不定，有联系黏稠材料的分析'],['三叶草植物 → 四叶草幸运意象、in clover 富足比喻','幸运是文化联想，名称本身不由现代 lucky 派生']]
CLOVE=[['香料：拉丁 clavus 钉子 → 法语 clou de girofle → clove','干花蕾的细杆加圆头，像小钉子'],['蒜瓣：古英语 clufu 裂开的块 → clove','与 cleave 分裂词族相连；两种名词来路不同']]
IVY=[['古英语 ifig → 英语 ivy','日耳曼语植物名，更远来源不明'],['攀附墙面、树木的常绿植物','现代还可在 Ivy League 名称中看到老校墙面常春藤的形象']]
WILLOW=[['古英语 welig → 中古英语 wilwe → willow','较远可能接弯转词族，具体分析保留可能'],['柳树、柔软枝条与木材名称','weeping willow 借下垂姿态指垂柳，像低垂着哭泣']]
W('lilac','英、美 /ˈlaɪlək/','丁香灌木、丁香花；浅紫色',
 '春天一串串有香味的浅紫色小花，可以叫 lilac；衣服是这种柔和紫色，也可直接说 lilac。植物把花色借给了颜色名。',
 '经法语 lilac 等接土耳其 leylak 植物名；更远来源仍有争论。英语先有植物名，再扩展颜色、香气用法。',LILAC,
 'a lilac bush 是一株丁香灌木；lilac flowers 是丁香花；a lilac scarf 是浅紫色围巾。',
 'a lilac bush；lilac flowers；a lilac scarf。',
 'lilac 是丁香花灌木名；香料丁香叫 clove，是不同植物、不同来源。中文都含丁香，不表示英语也要用一个词。',
 ('A lilac bush grows beside the gate.','门边长着一株丁香。'),('She wore a pale lilac scarf.','她围着一条浅丁香紫的围巾。'),sources=S('lilac','lilac'))
W('lilacs','英、美 /ˈlaɪləks/','丁香灌木、丁香花〔复数〕',
 '花园里几株丁香，或花瓶里几枝丁香花，可以说 lilacs。颜色名作为修饰语时，则通常保持 lilac。',
 'lilac + -s → lilacs，/k/ 后复数后缀读 /s/；数的是多株、多个花枝等植物个体。',LILAC+[['lilac + -s → lilacs','植物复数，词尾 /ks/']],
 'lilacs in bloom 是盛开的丁香；a vase of lilacs 是一瓶丁香花；lilac curtains 则说颜色，不需要因窗帘多个就把颜色加 s。',
 'lilacs in bloom；a vase of lilacs；fragrant lilacs。',
 'lilacs 通常不是把很多种紫色数出来；在普通花园、花束语境，先按丁香植物与花理解。',
 ('The lilacs are in bloom along the path.','小路边的丁香开花了。'),('She placed fresh lilacs in a vase.','她把新鲜丁香花放进花瓶。'),sources=S('lilacs','lilac'))
W('lilies','英、美 /ˈlɪliz/','百合、百合花〔复数〕',
 '一束百合，英语常见 lilies。单数 lily 的 y 改成 ies，读音仍保留原来的 /i/，再加复数 /z/。',
 'lily 词尾辅音字母 l + y，变 y 为 i + -es → lilies。植物名更早经古英语 lilie 接拉丁 lilia、lilium 等，较远可能是东地中海借词。',
 [['拉丁 lilium、lilia 等 → 古英语 lilie → 英语 lily','拉丁旧复数形式不决定现代英语单复数'],['lily 变 y 为 i + -es → lilies','现代英语复数，末尾 /liz/']],
 'white lilies 是白百合；a bouquet of lilies 是一束百合；many lilies 可以数花、植株，具体单位看场景。',
 'white lilies；a bouquet of lilies；lilies in a vase。',
 'water lilies 是睡莲相关通称，lily of the valley 是铃兰；含 lily 的常用名未必都指严格同属植物，完整名称要一起看。',
 ('White lilies stood in a tall vase.','白百合插在一个高花瓶里。'),('The garden was filled with lilies in early summer.','初夏，花园里开满了百合。'),sources=S('lilies','lily'))
W('daisy','英、美 /ˈdeɪzi/','雏菊；类似雏菊的花',
 '圆圆的花心，四周围一圈花瓣，随白天张开的雏菊，旧英语把它叫“白天的眼睛”。名字已经把一幅画装在里面。',
 '古英语 dæges eage，day 的旧属格“白天的” + eye“眼睛”，形成 dægesēage 等，经历缩变为 daisy。植物随光照开合，是传统命名解释。',DAISY,
 'a daisy 是一朵雏菊或一株相应植物；a daisy chain 可指串起来的雏菊花环。现代完整词名已经缩短，不能要求还看得出每个旧音节。',
 'a daisy；a daisy chain；a white daisy。',
 'daisy 里的现代 -y 不是在英语 dais 上新加一个可爱后缀；它来自整个“白天的眼睛”组合的长期变化。',
 ('A small daisy grew between the paving stones.','铺路石之间长出了一株小雏菊。'),('She tucked a daisy behind her ear.','她把一朵雏菊别在耳后。'),sources=S('daisy','daisy'))
W('daisies','英、美 /ˈdeɪziz/','雏菊、雏菊花〔复数〕',
 '草地上一片白花心黄的小雏菊，是 daisies。基础词本来是“白天的眼睛”，现代再把完整花名变成英语复数。',
 'daisy 的辅音字母 s + y 词尾，变 y 为 i + -es → daisies；基础末尾 /i/ 保留，再接 /z/，不多一个音节。',DAISY+[['daisy 变 y 为 i + -es → daisies','多个花、植株；读 /ˈdeɪziz/']],
 'a field of daisies 是一片雏菊；pick daisies 是摘雏菊；push up daisies 是死后被埋的口语比喻，沿墓上长花的画面理解。',
 'a field of daisies；pick daisies；a bunch of daisies。',
 'daisy chain 里的 daisy 作前置名词修饰语，通常用单数；a chain of daisies 的 of 后才按实际花朵用复数。',
 ('Daisies dotted the grass beside the path.','小路旁的草地上点缀着雏菊。'),('The child made a chain of daisies.','孩子把雏菊串成了花环。'),sources=S('daisies','daisy'))
W('orchids','英 /ˈɔːkɪdz/；美 /ˈɔrkɪdz/','兰花、兰科植物〔复数〕',
 '花店里一盆盆兰花，是 orchids。名字的较远形状联想来自某些兰花的地下块茎，不是今天所有兰花花瓣都必须像同一种东西。',
 'orchid + -s → orchids，/d/ 后后缀读 /z/。orchid 接近代拉丁植物学词形，较远希腊 orkhis 睾丸、兰花，联系部分地下块茎的形状；d 是植物学词形处理中的历史变化。',
 [['希腊 orkhis 睾丸及兰花名 → 拉丁、近代植物学形式 → orchid','部分块茎的形状命名，不能要求所有现代品种都显出同样特征'],['orchid + -s → orchids','多个兰花、兰科植物；末尾 /dz/']],
 'potted orchids 是盆栽兰花；wild orchids 是野生兰花；grow orchids 是栽兰花。ch 在常见读音里是 /k/。',
 'potted orchids；wild orchids；grow orchids。',
 'orchids 是兰花；orchards 是果园，虽然外形接近，来源和指的事物不同。orchids 的第二音节是 /kɪdz/。',
 ('The greenhouse contains several kinds of orchids.','温室里有几种兰花。'),('She grows orchids beside a bright window.','她在明亮的窗边栽兰花。'),sources=S('orchids','orchid'))
W('orchards','英 /ˈɔːtʃədz/；美 /ˈɔrtʃɚdz/','果园〔复数〕',
 '一处种苹果，另一处种梨，几处果树园就是 orchards。它数的是园地，不是里面的每棵树。',
 'orchard + -s → orchards，/d/ 后后缀读 /z/。古英语 orceard、ortgeard 等可能接植物 wyrt 与围园 geard 的组合，词形又有受拉丁 hortus 园影响的分析。',
 [['古英语 ortgeard、orceard 等 → orchard','可能联系植物 + 园地，另有拉丁 hortus 影响词形的分析'],['orchard + -s → orchards','多个果园；词尾 /dz/']],
 'apple orchards 是苹果园；fruit orchards 是果园；old orchards 是老果园。前置 apple 常用单数修饰，不写成必须 apples orchards。',
 'apple orchards；pear orchards；old orchards。',
 'orchards 的 ch 读 /tʃ/，orchids 的 ch 读 /k/；中文果园、兰花也正好提醒它们不是同一词族加两个不同后缀。',
 ('Apple orchards cover the lower hills.','低矮山坡上遍布苹果园。'),('The road runs between two old orchards.','公路从两处老果园之间穿过。'),sources=S('orchards','orchard'))
W('mosses','英 /ˈmɒsɪz/；美 /ˈmɔsɪz/','多种苔藓；苔藓植物〔复数〕',
 '墙上一层青苔可以整体叫 moss；比较不同种类、不同苔藓植物时，就会见到 mosses。不是每一小片绿都一定要数成复数。',
 'moss + -es → mosses，/s/ 后后缀读 /ɪz/，增加音节。moss 接古英语苔藓、沼地词及北欧影响，较远与潮湿材料有关，哪种旧义最先不确定。',
 [['古英语 meos 苔藓、mos 沼地等 → moss','同接潮湿、沼泽植物背景，不能强定哪义先后'],['moss + -es → mosses','不同种类、植物个体的可数复数']],
 'different mosses 是不同种苔藓；mosses on tree trunks 是树干上的各类苔藓；a layer of moss 仍可按植被材料不可数说。',
 'different mosses；woodland mosses；mosses on tree trunks。',
 'mosses 与 moss 的区别在计数方式；不是苔藓多一点就必须把所有普通植被描述都换成复数。',
 ('Several mosses grow on the damp wall.','湿墙上长着几种苔藓。'),('The guide helped us identify woodland mosses.','向导帮我们辨认林地里的苔藓。'),sources=S('mosses','moss'))
W('fern','英 /fɜːn/；美 /fɝn/','蕨；蕨类植物',
 '林下展开一大片像羽毛的绿叶，常见的是 fern。羽状叶是很好的识别画面，词源学里也有以羽毛、翅膀形状命名的分析。',
 '接古英语 fearn、日耳曼语蕨类植物名；较远可能联系羽毛、翅膀材料，但不能把这个分析当作已经完全确定的构词。',FERN,
 'a fern 是一株蕨；fern leaves、fern fronds 是蕨叶；a potted fern 是盆栽蕨。蕨类很多，不要求所有叶片都长成完全同一形状。',
 'a fern；fern fronds；a potted fern。',
 'fern 是一种植物类别，feather 是羽毛；可能的远源形状联系不意味着现代 fern 是 feather 的缩写。',
 ('A fern grew in the shade beside the wall.','墙旁阴凉处长着一株蕨。'),('She placed a potted fern near the window.','她把一盆蕨放在窗边。'),sources=S('fern','fern'))
W('ferns','英 /fɜːnz/；美 /fɝnz/','蕨、蕨类植物〔复数〕',
 '林下许多株蕨，或温室里不同种蕨，可以说 ferns。看的是成株植物或种类，不是数一片片叶子。',
 'fern + -s → ferns，/n/ 后后缀读 /z/；英语植物名的普通复数。',FERN+[['fern + -s → ferns','多株、不同种蕨；词尾 /nz/']],
 'woodland ferns 是林地蕨类；large ferns 是大型蕨；grow ferns 是栽培蕨。不同场景可以数个体，也可以讨论种类。',
 'woodland ferns；large ferns；grow ferns。',
 'ferns 是植物复数，fern fronds 里的 fronds 才数叶；单位层级不同。',
 ('Ferns covered the shaded bank.','阴凉的岸坡上长满了蕨。'),('The greenhouse displays ferns from several regions.','温室展出来自几个地区的蕨类植物。'),sources=S('ferns','fern'))
W('clover','英 /ˈkləʊvə/；美 /ˈkloʊvɚ/','三叶草、车轴草；〔in clover〕生活富足',
 '一根小叶柄上常见三片小叶，便于认 clover；偶尔找到四片小叶的四叶草，又成为幸运的文化象征。',
 '接古英语 clafre、clæfre，经中古英语 claver 成 clover；较远来源不定，有联系黏稠材料的分析。四叶草的幸运意象是文化发展，不是名字直接由幸运拼出。',CLOVER,
 'white clover 是白车轴草；a four-leaf clover 是四叶草；in clover 比喻日子宽裕、舒服，沿牛吃到丰美草料的形象理解。',
 'white clover；a four-leaf clover；in clover。',
 'clover 的 -er 不应按现代人物后缀拆；clove 香料丁香、蒜瓣则各有其他来源，与三叶草名不能只因前几字母相同就归并。',
 ('White clover grew among the grass.','草丛中长着白车轴草。'),('The child found a four-leaf clover.','孩子找到了一株四叶草。'),sources=S('clover','clover'))
W('clovers','英 /ˈkləʊvəz/；美 /ˈkloʊvɚz/','多株、多种三叶草〔复数〕',
 '比较几株不同的三叶草，或植物名录里的几个种类，可以用 clovers。铺在草地上的整片植被，则常整体说 clover。',
 'clover + -s → clovers，后缀读 /z/；数个体、种类时用复数，不可数植被用法仍保留。',CLOVER+[['clover + -s → clovers','多个个体、不同种类；词尾 /əz/、/ɚz/']],
 'different clovers 是不同种三叶草；red and white clovers 是红、白车轴草等不同种类；four-leaf clovers 可数找到的几株。',
 'different clovers；red and white clovers；four-leaf clovers。',
 'clovers 与 cloves 多了一个 r，但来源、读音、植物都不同；前者常有 /ə/ 或 /ɚ/ 音节，后者是 /kləʊvz/、/kloʊvz/。',
 ('The field guide describes several common clovers.','这本野外图鉴介绍了几种常见三叶草。'),('She pressed two four-leaf clovers between the pages.','她把两株四叶草夹进书页压平。'),sources=S('clovers','clover'))
W('clove','英 /kləʊv/；美 /kloʊv/','丁香〔香料〕；一瓣蒜',
 '一粒香料丁香像小钉子：细杆顶着圆头；一瓣蒜则像从大蒜球上分出的小块。两个 clove 同形，名字各抓住一种形状、结构。',
 '香料经法语 clou de girofle，较远拉丁 clavus 钉子；蒜瓣接古英语 clufu 裂开的块，与 cleave 分裂词族相连。不能用钉子来包办两种词源。',CLOVE,
 'a clove 是一粒香料丁香；a clove of garlic 是一瓣蒜；ground cloves 则常指磨成的丁香香料。完整搭配决定是哪种食材。',
 'a clove；a clove of garlic；clove oil。',
 'clove 不是 lilac 丁香花灌木名；中文同名不代表同一植物。蒜瓣 clove 也不是一整个 garlic bulb。',
 ('Add a clove to the simmering sauce.','往小火煮着的酱汁里加一粒丁香。'),('Crush one clove of garlic.','把一瓣蒜拍碎。'),sources=S('clove','clove'))
W('cloves','英 /kləʊvz/；美 /kloʊvz/','丁香香料；蒜瓣〔复数〕',
 '菜谱要 two cloves of garlic，是两瓣蒜；如果只写 whole cloves，常是整粒丁香香料。字形一样，搭配给出具体食材。',
 'clove + -s → cloves，/v/ 后后缀读 /z/。两种不同来源的名词都按同一英语规则形成复数。',CLOVE+[['clove + -s → cloves','丁香香料粒、蒜瓣的复数；词尾 /vz/']],
 'whole cloves 是整粒丁香；ground cloves 是丁香粉；two cloves of garlic 是两瓣蒜。ground 修饰已经磨碎的香料用法。',
 'whole cloves；ground cloves；two cloves of garlic。',
 'cloves of garlic 的 of 很关键；写 two garlics 可能数整颗蒜或另有语境，并不自动等于两瓣蒜。',
 ('The recipe needs two cloves of garlic.','这份食谱需要两瓣蒜。'),('She added cinnamon and whole cloves to the pot.','她往锅里加了肉桂和整粒丁香。'),sources=S('cloves','clove'))
W('oaks','英 /əʊks/；美 /oʊks/','橡树、栎树〔复数〕',
 '路边几棵高大的橡树，是 oaks；做成桌子后说 oak wood，则把树名当材料用。复数数树，单数材料名说木材。',
 'oak + -s → oaks，/k/ 后后缀读 /s/。oak 接古英语 ac，并有古诺尔斯 eik 等对应词影响，较远日耳曼语以外来源不确定。',
 [['古英语 ac、北欧 eik 等 → 中古英语 oke → oak','古老树名，更远来源未全确定'],['oak + -s → oaks','多棵橡树；词尾 /ks/']],
 'old oaks 是老橡树；a row of oaks 是一排；oak furniture 的 oak 作材料修饰语通常不加 s。',
 'old oaks；a row of oaks；oaks along the road。',
 'oaks 数个体，oak 数材料时往往不可数；不是木桌用到多棵树，就把 oak table 改成 oaks table。',
 ('Old oaks lined the entrance to the park.','公园入口旁排列着老橡树。'),('We rested in the shade of two large oaks.','我们在两棵大橡树的树荫下歇息。'),sources=S('oaks','oak'))
W('poppies','英 /ˈpɒpiz/；美 /ˈpɑpiz/','罂粟属花卉；虞美人等〔复数〕；罂粟花纪念饰物',
 '田里一片红色、花瓣轻薄的花，常可见 poppies。英语 poppy 是较宽的花名，具体说哪种植物还要看完整名称。',
 'poppy 词尾辅音字母 p + y，变 y 为 i + -es → poppies。较早接古英语 popig、日耳曼语借入的拉丁 papaver 等植物名，远源解释仍有不确定。',
 [['拉丁 papaver 等 → 日耳曼语、古英语 popig → poppy','旧植物名，不是现代 pop 爆开加 -y 就能概括来源'],['poppy 变 y 为 i + -es → poppies','花卉复数；纪念饰物也可借用这个花名']],
 'red poppies 是红花；a field of poppies 是一片花田；英国等纪念语境中 wear poppies 可指佩戴相应花形纪念饰物。',
 'red poppies；a field of poppies；paper poppies。',
 'poppy 的不同种类不宜一律按中文同一种具体植物翻译；词源与本页花名学习先抓植物、花及其纪念意象。',
 ('Red poppies grew along the edge of the field.','田边长着红色的虞美人一类花卉。'),('The children made paper poppies for the display.','孩子们做了纸制罂粟花，用于展陈。'),sources=S('poppies','poppy'))
W('ivy','英、美 /ˈaɪvi/','常春藤；常春藤类攀缘植物',
 '绿叶攀在老墙上，沿着墙面不断伸展，这种常见常绿攀缘植物是 ivy。先记附着、蔓延的植物画面，名字更远的来源反而不清楚。',
 '接古英语 ifig，属于西日耳曼语植物旧名，较远来源不明。现代 ivy 不能按英语 I 加某个后缀硬拆。',IVY,
 'ivy on a wall 是墙上的常春藤；ivy-covered walls 是长满常春藤的墙；Ivy League 名称也借老校常春藤墙面的形象。',
 'ivy on the wall；ivy leaves；ivy-covered walls。',
 'ivy 是植物名；Ivy 首字母大写也能是人名或专名部分。poison ivy 的完整名称又指另一类植物，不把带 ivy 的名称全等同。',
 ('Ivy covered the old stone wall.','常春藤爬满了旧石墙。'),('A trail of ivy hung from the pot.','一串常春藤枝蔓从盆里垂下来。'),sources=S('ivy','ivy'))
W('ivies','英、美 /ˈaɪviz/','多株、多种常春藤〔复数〕',
 '苗圃里比较几种叶形不同的常春藤，可以说 ivies。墙上一整片覆盖，则仍可按植被整体说 ivy。',
 'ivy 词尾辅音字母 v + y，变 y 为 i + -es → ivies；原词末尾 /i/ 保留，再加 /z/。',IVY+[['ivy 变 y 为 i + -es → ivies','多株、不同种常春藤；读 /ˈaɪviz/']],
 'variegated ivies 是斑叶常春藤；different ivies 是不同种类、品种；container-grown ivies 是盆栽个体。',
 'variegated ivies；different ivies；trailing ivies。',
 'Ivies 在特定上下文也可能缩指常春藤盟校；植物语境的小写 ivies，先按实际植物理解，不能都当学校。',
 ('The nursery sells several varieties of ivies.','苗圃出售几个品种的常春藤。'),('Trailing ivies hung from baskets by the window.','垂生常春藤从窗边的吊篮里垂下来。'),sources=S('ivies','ivy'))
W('willow','英 /ˈwɪləʊ/；美 /ˈwɪloʊ/','柳树；柳木',
 '河边垂着柔软枝条的柳树，是 willow。weeping willow 像低垂着头哭泣，用这个姿态给垂柳起了形象的名字。',
 '古英语 welig，经中古英语 wilwe 等成为 willow；较远可能联系弯转材料，和枝条柔韧可弯的形象相合，但远源分析仍带可能性。',WILLOW,
 'a willow tree 是一棵柳树；a weeping willow 是垂柳；willow branches 是柳枝；willow 作材料名可指柳木。',
 'a willow tree；a weeping willow；willow branches。',
 'willow 的 -ow 是词形历史变化的一部分，不按现代词尾添加一个独立意思。weeping willow 说下垂形象，不是树真的在哭。',
 ('A willow leaned over the stream.','一棵柳树斜伸在溪流上方。'),('We sat beneath a weeping willow.','我们坐在一棵垂柳下。'),sources=S('willow','willow'))
W('willows','英 /ˈwɪləʊz/；美 /ˈwɪloʊz/','柳树〔复数〕',
 '河岸边一排柳树，是 willows。它数不同树木；柳枝作篮子材料时，又常把 willow 按材料单数使用。',
 'willow + -s → willows，基础末音是元音 /əʊ/、/oʊ/，复数后缀读 /z/；不另加 /ɪz/ 音节。',WILLOW+[['willow + -s → willows','多棵柳树；末尾 /əʊz/、/oʊz/']],
 'weeping willows 是多棵垂柳；willows along a river 是河岸柳树；a row of willows 是一排。',
 'weeping willows；a row of willows；willows along the river。',
 'willows 的 s 数树；willow branches 里的 willow 用单数修饰枝条，和 oak furniture 一样，不因来源有多棵树就必须加 s。',
 ('Willows grew along both sides of the river.','河流两岸长着柳树。'),('The pond was shaded by three old willows.','池塘由三棵老柳树遮阴。'),sources=S('willows','willow'))
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_zis',ROOTS,WORDS)
 extend_lessons()
