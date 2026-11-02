"""Everyday gaps: bunches, galleries, pizza, waste, creeks and arsenals."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
def S(word,base):
 return ['https://en.wiktionary.org/wiki/'+word+'#English','https://www.etymonline.com/word/'+base]
EXISTING_ROOT_ADDITIONS={
 'B2825':dict(words='bunch bunches bunched bunching'.split(),label='bunch：一束、一串，到挤成一团',note='与 bundle 比较聚在一起的画面；bunch 有经法语方言、佛兰德语一捆材料传入的分析，不是现代 bind 或 bundle 自由换字母的派生。'),
 'B2636':dict(words='gallery galleries'.split(),label='gallery：从长廊到画廊、图片集',note='本组与 art 作艺术展览场景比较，gallery 不从拉丁 ars 派生；它经古法语 galerie、中古拉丁 galeria，远源未定。'),
 'B2946':dict(words='pizza pizzas pizzeria pizzerias'.split(),label='pizza：面饼，到卖披萨的店',note='与 bread 比较面食场景，不是由现代 bread 派生。pizza 借意大利语，远源未定；pizzeria 接 pizza 与表示店铺、场所的意大利语后缀材料。'),
 'B3418':dict(words='trash trashes trashed trashing trashy rubbish rubbishes rubbished rubbishing'.split(),label='trash、rubbish：垃圾，到把东西说得一文不值',note='与 waste 作近义比较，不是同一个词根的直接派生。trash 或接北欧落叶、废料材料，rubbish 经盎格鲁法语 rubouses，二者远源都不能硬造确定拆分。'),
 'B3100':dict(words='creek creeks'.split(),label='creek：狭窄水湾，到小溪',note='与 river 作水域词比较，不是 river 的后代。creek 可能接古诺尔斯 kriki 角落、弯处等材料，早有狭窄水湾义，后来在美式等英语中常指小溪、支流。'),
 'C0081':dict(words='arsenal arsenals'.split(),label='arsenal：另源的兵工厂、武器库',note='与 armory、arms 作武器储备词比较；arsenal 经意大利语接阿拉伯语 dar as-sina‘ah 制作的房屋、工场，不是从拉丁 arma 构词。'),
}
BUNCH=[['bunch 较早有捆、凸块等材料','可能经法语方言 bonge、佛兰德语 bondje 等一捆材料传入'],['一团、一束 → 一群、一大堆；名词再成动词','bunch up 表聚拢、布料挤皱，现代不再自由拆词干']]
GALLERY=[['古法语 galerie 长廊 ← 中古拉丁 galeria','更远来源未定，不把相关地名猜测写成确定史'],['长廊、通道 → 展画空间；剧院高层座席等','现代图片集合、缩略图页也沿用展示空间的画面']]
PIZZA=[['意大利语 pizza 原有饼、馅饼等材料 → 英语 pizza','更远来源未定，不把某一压面、夹折猜测当成唯一来源'],['pizza → pizzas；pizzeria → pizzerias','食品、食品复数，与制作销售它的店铺及复数']]
TRASH=[['trash 较早有落叶、细枝、废物、无用物等材料','可能接北欧语言，但更远来历不完全确定'],['废物 → 无价值内容；现代动词有扔掉、损坏、猛烈批评','trashy 用 -y 评价低劣、俗气，不都指真的有垃圾']]
RUBBISH=[['盎格鲁法语 rubouses 废料 → 英语 rubbish','远源未定，与 rubble 碎石有关系分析'],['废料、垃圾 → 无价值内容、胡说；后来动词说贬低','现代末尾 -ish 不能当成 rub 擦加有点的后缀来理解']]
CREEK=[['早期 kryk、creke 等：狭窄水湾','可能接古诺尔斯 kriki 角落，或受法语 crique 影响'],['水湾、河汊 → 美式等英语里的小溪、支流','读到海边或内陆，要靠具体地理场景定意思']]
ARSENAL=[['阿拉伯语 dar 房屋 + as-sina‘ah 制作、工艺 → 工场','经意大利 arzenale 等接入英语'],['较早船坞、海军物资基地 → 兵工厂、武器库','再用作某人、机构掌握的一套手段、资源']]
W('bunch','/bʌntʃ/','一束、一串、一群；很多；聚拢、挤成团',
 '葡萄一颗颗连成一串，花扎成一束，都能叫 a bunch。后来也能轻松说 a bunch of people 一群人；bunch up 则是挤到一起。',
 '基础词较早有捆、凸块等材料，可能经法语方言、佛兰德语一捆词传入；不从现代 bind 随意换字母。名词再发展出聚拢、挤皱的动作义。',BUNCH,
 'a bunch of grapes 一串葡萄；a bunch of flowers；bunch up 挤成一团。',
 'a bunch of friends 一群朋友；a whole bunch 一大堆。',
 'bunch 常用来把相近、相连或随意归拢的东西当成一组，pair 精确是两个；一束花不规定只有两支。',
 ('She put a bunch of flowers on the table.','她把一束花放在桌上。'),('The fabric tends to bunch up at the waist.','那块布料在腰部容易挤皱成团。'),sources=S('bunch','bunch'))
W('bunches','/ˈbʌntʃɪz/','几束、几串、几群；聚拢、挤成团〔第三人称单数〕',
 '花店几束花，是 bunches；衣服穿着穿着在肘部堆皱，是 bunches up。一个在数团，一个在说成团的动作。',
 'bunch + -es，/tʃ/ 后读 /ɪz/；名词复数和动词三单同形。',BUNCH+[['bunch + -es → bunches','多束、多串；或它聚拢、堆皱']],
 'bunches of flowers；bunches of grapes；bunches up at the elbow。',
 'sold in bunches 成束销售；the cloth bunches up。',
 'bunches of grapes 是几串葡萄，bunches of grape juice 不按同一普通方式数；可数一团要看名词的实际形态。',
 ('The stall sells grapes in large bunches.','摊位上的葡萄都是大串卖的。'),('The sleeve bunches up at the elbow.','袖子在肘部堆起了褶皱。'),sources=S('bunches','bunch'))
W('bunched','/bʌntʃt/','聚拢、挤成团、堆皱了的',
 '人挤在门边，布料堆在腰上，或手指收拢成拳头，都能用 bunched。重点是分开的东西收成了密密的一团。',
 'bunch + 完整 -ed，/tʃ/ 后读 /t/；过去式、过去分词。',BUNCH+[['bunch + -ed → bunched','过去聚拢，或现在呈现挤团、堆皱的状态']],
 'bunched up by the door；bunched fabric；bunched his fists。',
 'bunched together；the skirt bunched at the waist。',
 'bunched together 强调挤在一起，lined up 强调整齐排成线；一群人聚拢不保证有队形。',
 ('The passengers bunched together near the door.','乘客们挤在门边。'),('The skirt bunched up around her waist.','裙子在她腰部堆皱起来。'),sources=S('bunched','bunch'))
W('bunching','/ˈbʌntʃɪŋ/','正在聚拢、挤成团；堆皱',
 '队伍走到窄处，人开始往一起挤；衣服在活动中一层层堆皱，都是 bunching。它写逐渐聚成一团的过程。',
 'bunch + -ing；保留 ch，读 /tʃ/，不另外重复字母。',BUNCH+[['bunch + -ing → bunching','聚拢、挤团、堆皱的过程']],
 'bunching up near the gate；fabric bunching at the knees。',
 'stop the cloth from bunching；bunching together。',
 'bunching 写形成团、褶的过程，stretching 写拉长、撑开；衣服一处可能拉紧，另一处却堆皱。',
 ('People were bunching up near the narrow entrance.','人们正在狭窄入口附近越挤越密。'),('The lining kept bunching behind my knees.','里衬总在我膝盖后面堆皱。'),sources=S('bunching','bunch'))
W('gallery','英 /ˈɡæləri/；美 /ˈɡæləri/','画廊、展厅；图片集；楼座、旁听席；长廊',
 '走进一条长长的空间，沿路看画，是 gallery 的好画面。后来屏幕上一格格展示照片，也叫 gallery；剧院、议会里的高处看台又是另一常见用法。',
 '经古法语 galerie 长廊，接中古拉丁 galeria，远源未定。先有长廊、通道材料，再有展画空间；不把词尾 -ery 当作现代 gallery 的全部构词答案。',GALLERY,
 'an art gallery；a photo gallery；the public gallery 公众旁听席。',
 'a gallery of portraits；play to the gallery 哗众取宠、讨好观众。',
 'museum 范围更广，可展历史、自然等藏品；gallery 常偏艺术展览空间，也可指一个展室。',
 ('We visited a small gallery near the station.','我们参观了车站附近一家小画廊。'),('The website has a gallery of old photographs.','网站有一组展示老照片的图片集。'),sources=S('gallery','gallery'))
W('galleries','英 /ˈɡæləriz/；美 /ˈɡæləriz/','画廊、展厅、图片集、楼座等〔复数〕',
 '几家画廊，或一个网站上按主题分开的几组图片，都是 galleries。数的是空间、集合，不是把每张画都叫一间 gallery。',
 'gallery 的 y 改 i 加 -es → galleries，结尾读 /z/；现代复数规则不改变古法语、拉丁的借入路线。',GALLERY+[['gallery → galleries','y 改 i 加 -es，多个展示空间、图片集合等']],
 'local art galleries；online photo galleries；museum galleries。',
 'public galleries；galleries showing contemporary art。',
 'galleries 可以是多个展室，不一定是多个独立机构；同一家博物馆内部也可能有多间。',
 ('Several local galleries stayed open late for the event.','为配合活动，当地几家画廊都延长了开放时间。'),('The archive contains separate galleries for each decade.','档案馆把每个年代的照片分成了不同图片集。'),sources=S('galleries','gallery'))
W('pizza','/ˈpiːtsə/','披萨；披萨饼',
 '面饼上铺奶酪、番茄等配料烤出来，就是 pizza。吃这种食物时可不数整张；要一整张时也能说 a pizza。',
 '借自意大利语 pizza，较早有饼、馅饼等意思；更远来源未定。有关压面、夹折等解释只是分析，不当成确定历史。',PIZZA,
 'a slice of pizza 一片披萨；order a pizza 点一张披萨；have pizza。',
 'cheese pizza；a large pizza；pizza dough。',
 'pizza 可作食物不可数，也可数一张张；two pizzas 是两张，不是两片，two slices 才是两片。',
 ('We shared a pizza after the film.','电影结束后，我们分吃了一张披萨。'),('Would you like a slice of pizza?','你想吃一片披萨吗？'),sources=S('pizza','pizza'))
W('pizzas','/ˈpiːtsəz/','披萨饼〔复数，通常数整张〕',
 '给一群人订餐，两张、三张披萨，就说 pizzas。大小、切多少片可以不同，复数主要在数一张张成品。',
 'pizza + -s，读 /z/；末尾 a 是基础词的一部分，现代英语复数直接加 -s。',PIZZA+[['pizza + -s → pizzas','多张披萨，不规定每张切几片']],
 'two large pizzas；cheese pizzas；freshly baked pizzas。',
 'order pizzas；share three pizzas。',
 'pizzas 数整张，slices of pizza 数片；买了三片不应自动说买了 three pizzas。',
 ('We ordered two large pizzas for the group.','我们给大家点了两张大披萨。'),('The oven can bake several pizzas at once.','那个烤炉一次能烤好几张披萨。'),sources=S('pizzas','pizza'))
W('pizzeria','英 /ˌpiːtsəˈrɪə/；美 /ˌpitsəˈriə/','披萨店、披萨餐馆',
 '专门做、卖披萨的店，是 a pizzeria。把食物和店铺配起来记：pizza 是吃的，pizzeria 是去买、去吃的地方。',
 '意大利语 pizza 的构词词干 pizz- + -eria 店铺、场所的后缀材料；不是 pizza 原封不动再拼上 eria。英语借入或仿这种形式使用。',PIZZA+[['pizza 的词干 pizz- + -eria → pizzeria','制作、销售披萨的店铺']],
 'a local pizzeria；a family-run pizzeria；work at a pizzeria。',
 'a pizzeria near the station；open a pizzeria。',
 'pizzeria 说主要卖披萨的店，不保证是自助式；不能因为词尾像 cafeteria 就把它一律理解成自助餐厅。',
 ('There is a small pizzeria beside the cinema.','电影院旁边有一家小披萨店。'),('She works at a family-run pizzeria.','她在一家家庭经营的披萨店工作。'),sources=S('pizzeria','pizzeria'))
W('pizzerias','英 /ˌpiːtsəˈrɪəz/；美 /ˌpitsəˈriəz/','披萨店、披萨餐馆〔复数〕',
 '一条街上有几家披萨店，就是 several pizzerias。它数店，不数披萨，也不数做披萨的人。',
 'pizzeria + -s，读 /z/；英语复数按普通名词处理，词尾 a 保留。',PIZZA+[['pizzeria + -s → pizzerias','多家制作、销售披萨的店']],
 'local pizzerias；three pizzerias；independent pizzerias。',
 'pizzerias along the main street；reviews of pizzerias。',
 'pizzerias 是店，pizzas 是食品；order from three pizzerias 和 order three pizzas 说的是不同数量。',
 ('Three pizzerias opened on the same street.','同一条街上开了三家披萨店。'),('The guide lists several independent pizzerias.','指南列出了几家独立经营的披萨店。'),sources=S('pizzerias','pizzeria'))
W('trash','/træʃ/','垃圾；低劣、无价值的内容；扔掉、毁坏、猛烈批评',
 '要扔掉的东西是 trash；嫌一部电影一文不值，也可说 trash。作动词时，像把它当垃圾处理，发展成扔掉、砸坏、骂得很差。',
 '较早有落叶、细枝、废料等材料，可能接北欧语言，远源未定。现代扔弃、损坏、批评的动词义分期发展，不简单等同于 thrash。',TRASH,
 'take out the trash 倒垃圾；trash a room 把房间糟蹋得乱七八糟；trash an idea。',
 'a trash can；talk trash 说垃圾话、贬损话；trash the draft。',
 'trash 在美式常说生活垃圾，rubbish 在英式更常见；评价作品时都可表示无价值、很差，语气很强。',
 ('Please take out the trash before you leave.','走之前请把垃圾倒掉。'),('The reviewer did not simply criticise the film; she seemed determined to trash it.','评论者不只是指出电影的问题，看起来简直要把它批得一无是处。'),sources=S('trash','trash'))
W('trashes','/ˈtræʃɪz/','扔掉、毁坏、猛烈批评〔第三人称单数〕',
 '每出一部续集，他都把它骂得一文不值，是 trashes it。也可说把没用的文件扔掉、把地方糟蹋坏。',
 'trash + -es，/ʃ/ 后读 /ɪz/；这里是动词三单。普通垃圾名词通常不可数，不靠加 -es 来数几袋垃圾。',TRASH+[['trash + -es → trashes','他或她把东西当废物扔掉、糟蹋或贬低']],
 'trashes an idea；trashes the room；trashes old drafts。',
 'trashes every sequel；trashes the proposal in public。',
 'trashes a film 的批评通常很狠，reviews a film 只说做评论；评论可以喜欢，也可以不喜欢。',
 ('He trashes every sequel before giving it a fair chance.','他还没认真看待每部续集，就先把它骂得一文不值。'),('She trashes the rough drafts once the final version is saved.','保存最终版后，她就把草稿丢掉。'),sources=S('trashes','trash'))
W('trashed','/træʃt/','扔掉、毁坏、猛烈批评了；喝醉得厉害的〔口语〕',
 '房间被糟蹋得没法看，是 trashed；作品被狠批也能用。口语 get trashed 还可说喝得烂醉，不是人真的变成垃圾。',
 'trash + 完整 -ed，/ʃ/ 后读 /t/；既可作过去式、过去分词，也有喝得很醉等口语形容词义。',TRASH+[['trash + -ed → trashed','被扔弃、糟蹋、狠批；另有醉得厉害的口语用法']],
 'a trashed room；trashed the proposal；get trashed〔很口语〕。',
 'trashed the old files；the film was trashed by critics。',
 'trashed 作醉义语气口语而强，drunk 更一般；在房间、文件场景则不能按醉了来理解。',
 ('The party left the room completely trashed.','聚会过后，房间被糟蹋得一塌糊涂。'),('The film was trashed by several reviewers.','几位评论者把那部电影批得一无是处。'),('The character got trashed at the party.','那个角色在聚会上喝得烂醉。'),sources=S('trashed','trash'))
W('trashing','/ˈtræʃɪŋ/','正在扔弃、糟蹋、猛烈批评；一顿狠批',
 '把一个方案从头骂到尾、说得一文不值，是 trashing。也能指实际破坏房间、丢掉资料的过程，不能只看成普通整理。',
 'trash + -ing；过程形式也可名词化，如 give something a trashing 表示一顿狠批。',TRASH+[['trash + -ing → trashing','扔弃、毁坏、贬低的过程，或一顿狠批']],
 'trashing the proposal；a public trashing；trashing a hotel room。',
 'trashing old files；trashing someone’s work。',
 'constructive criticism 是有助于改进的批评，trashing 常像一味贬低；指出问题与说得一无是处程度不同。',
 ('He was accused of trashing other people’s work without reading it.','他被指没读别人的作品就大加贬低。'),('The proposal received a public trashing at the meeting.','那项提案在会上被当众狠批了一顿。'),sources=S('trashing','trash'))
W('trashy','/ˈtræʃi/','低劣、俗气、没什么品位的；像垃圾的',
 '情节夸张、八卦刺激，却没多少质量，可能被嫌 trashy。也有人自嘲爱看 trashy novels，明知不高雅，仍觉得好玩。',
 'trash + -y；名词加性质后缀，早有无价值、像废物的意思。现代常用来评价内容、审美，而不是说实物上粘了垃圾。',TRASH+[['trash + -y → trashy','带低劣、无价值、俗气等评价']],
 'a trashy novel；trashy television；a trashy magazine。',
 'cheap and trashy；trashy entertainment。',
 'trashy 是对质量、品味的主观贬评，popular 只说受欢迎；流行作品不自动低劣。',
 ('She enjoys reading trashy novels on holiday.','度假时，她爱看些通俗刺激、没那么高雅的小说。'),('The magazine was full of trashy celebrity gossip.','那本杂志全是低俗的名人八卦。'),sources=S('trashy','trash'))
W('creek','/kriːk/〔部分美式方言 /krɪk/〕','小溪、支流〔尤美式等〕；狭窄水湾、河汊',
 '美式故事里，孩子到 creek 边玩，常是一条小溪。海岸、河口场景里，它也可能是狭窄水湾；同一个词不能不看地点就一律画成山间溪流。',
 '早有 kryk、creke 等狭窄水湾材料，可能接古诺尔斯 kriki 角落，或受法语 crique 影响。后来发展为河汊，再在美式等英语中常指小溪、支流。',CREEK,
 'a shallow creek 浅溪；cross the creek；a tidal creek 潮汐水道。',
 'up the creek 陷入困境〔口语〕；a creek beside the campsite。',
 'creek 在美式常比 river 小，但地名、地区用法并无统一尺寸界线；不拿一个词就精确判断河道宽度。',
 ('We crossed the creek on stepping stones.','我们踩着踏脚石过了小溪。'),('The boat entered a narrow tidal creek.','船驶入一条狭窄的潮汐水道。'),sources=S('creek','creek'))
W('creeks','/kriːks/〔部分美式方言 /krɪks/〕','小溪、支流、水湾、河汊〔复数〕',
 '山谷里几条小溪，或海湾边几条窄窄的水道，都是 creeks。读到海水、潮汐时，要把水湾、河汊那条意思也留在脑中。',
 'creek + -s，/k/ 后读 /s/；复数规则相同，地区和地理场景决定具体水域。',CREEK+[['creek + -s → creeks','多条小溪、支流或狭窄水道']],
 'small creeks；tidal creeks；creeks feeding into the river。',
 'cross several creeks；a network of creeks。',
 'creeks 可能汇入更大的 river，也可能是沿海水道；不能见复数就认成同一种内陆小河。',
 ('Several small creeks flow into the lake.','几条小溪流入那个湖。'),('The coast is cut by narrow tidal creeks.','海岸被狭窄的潮汐水道分割开来。'),sources=S('creeks','creek'))
W('arsenal','英 /ˈɑːsənəl/；美 /ˈɑrsənəl/','兵工厂、武器库；储备的一整套武器、手段、资源',
 '存放、制造武器的地方可以叫 arsenal；一个人准备了很多解决问题的办法，也像有一座手段库。重点是储备齐，遇事能拿出来用。',
 '经意大利 arzenale 等接阿拉伯语 dar as-sina‘ah，字面为制作、工艺的房屋，即工场。英语早有船坞、海军物资基地义，后来发展为武器库、兵工厂。',ARSENAL,
 'a military arsenal；an arsenal of weapons；an arsenal of techniques。',
 'a vast arsenal；add something to your arsenal 充实你的手段库。',
 'arsenal 常突出武器、手段储备，warehouse 只是仓储建筑；比喻中的 teaching arsenal 也不是真的存武器。',
 ('The old arsenal was converted into a museum.','旧兵工厂改成了博物馆。'),('She has an arsenal of techniques for engaging a class.','她掌握了一整套调动课堂兴趣的方法。'),sources=S('arsenal','arsenal'))
W('arsenals','英 /ˈɑːsənəlz/；美 /ˈɑrsənəlz/','兵工厂、武器库〔复数〕；多方储备的武器、手段',
 '几座武器库、兵工厂，是 arsenals；不同人、团队各自掌握的一套套手段，也能这样数。它既可说地点，也可说储备。',
 'arsenal + -s，读 /z/；末尾 -al 在这个借词里不是现代现场加的英语形容词后缀。',ARSENAL+[['arsenal + -s → arsenals','多个兵工厂、武器库，或各方储备']],
 'military arsenals；nuclear arsenals；their arsenals of techniques。',
 'old arsenals；reduce arsenals；add tools to their arsenals。',
 'arsenals 可以侧重武器总量而非建筑数量，warehouses 更直接指仓库；看后面谈地点还是储备。',
 ('Several old arsenals now house cultural institutions.','几座旧兵工厂如今成了文化机构的所在地。'),('The workshop added new techniques to the teachers’ arsenals.','工作坊给教师们的方法库增加了新招。'),sources=S('arsenals','arsenal'))
W('rubbish','/ˈrʌbɪʃ/','垃圾、废物；胡说、低劣的东西；贬得一文不值',
 '要倒掉的废物是 rubbish；一句话没根据，也能说 That is rubbish。英式等英语中作动词，还能把一个方案狠狠贬低。',
 '经盎格鲁法语 rubouses 废料，远源未定，和 rubble 碎石有关系分析。末尾后来写成 -ish，不是现代 rub 擦加有点的后缀。',RUBBISH,
 'take out the rubbish；a load of rubbish 一派胡言；rubbish an idea。',
 'a rubbish bin；talk rubbish；the film was rubbish 电影很差〔口语〕。',
 'rubbish 在英式常见，trash 在美式常见；说看法是 rubbish 语气很不客气，不是普通的我不同意。',
 ('Please put the rubbish in the bin.','请把垃圾放进垃圾桶。'),('I do not want to rubbish the idea before hearing the details.','没听细节前，我不想先把那个想法贬得一文不值。'),sources=S('rubbish','rubbish'))
W('rubbishes','/ˈrʌbɪʃɪz/','贬得一文不值、猛烈否定〔第三人称单数，尤英式等〕',
 '别人还没说完，他就断言整个方案都不值一提，是 rubbishes the proposal。动词把被批评的东西当垃圾看待，评价很强。',
 'rubbish + -es，/ʃ/ 后读 /ɪz/；这里是动词三单。普通垃圾名词 rubbish 通常不可数，几袋垃圾不这样数。',RUBBISH+[['rubbish + -es → rubbishes','他或她猛烈贬低、否定']],
 'rubbishes a proposal；rubbishes the claim；rubbishes other people’s work。',
 'rubbishes every suggestion；rubbishes the report。',
 'rubbishes 强调贬低、说不值一提，questions 可以只是提出疑问；质疑证据不一定全盘否定。',
 ('He rubbishes every suggestion without offering an alternative.','他把每个建议都批得一文不值，却不提出别的办法。'),('The spokesperson rubbishes the claim in the interview.','发言人在采访中把那个说法驳得一文不值。'),sources=S('rubbishes','rubbish'))
W('rubbished','/ˈrʌbɪʃt/','贬低、猛烈否定了',
 '计划刚提出，就被人当成毫无价值的东西批了一通，是 rubbished。它描述强烈否定的态度，不表示批评必定有理。',
 'rubbish + 完整 -ed，/ʃ/ 后读 /t/；过去式、过去分词。',RUBBISH+[['rubbish + -ed → rubbished','过去把某事贬得很低、说不值一提']],
 'rubbished the proposal；the claim was rubbished；rubbished his work。',
 'publicly rubbished；rubbished the suggestion。',
 'rubbished 不等于 disproved；前者是强烈否定、贬低，后者是以证据证伪；态度强不自动代表证据足。',
 ('The proposal was rubbished before anyone examined the evidence.','还没人查看证据，提案就被贬得一文不值。'),('She rubbished the suggestion that the team had given up.','她强烈否定了团队已经放弃的说法。'),sources=S('rubbished','rubbish'))
W('rubbishing','/ˈrʌbɪʃɪŋ/','正在贬低、猛烈否定；一顿狠批',
 '不提具体改法，只把对方的工作说得什么都不值，是 rubbishing。它常强调批评方式粗暴、轻蔑，不只是正常审查。',
 'rubbish + -ing；过程形式也能作动作名词，表示贬低、狠批这件事。',RUBBISH+[['rubbish + -ing → rubbishing','把某事当作无价值而贬低的过程']],
 'rubbishing an idea；rubbishing the report；a public rubbishing。',
 'stop rubbishing every suggestion；rubbishing someone’s efforts。',
 'rubbishing 是贬低，不是普通的 revising 修改；指出具体问题、帮助改进时通常不用这么强的词。',
 ('He spent the meeting rubbishing other people’s ideas.','整个会议上，他都在贬低别人的想法。'),('She objected to the constant rubbishing of the team’s efforts.','她反对别人不断把团队的努力说得一文不值。'),sources=S('rubbishing','rubbish'))
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_zhv',ROOTS,WORDS)
 extend_lessons()
