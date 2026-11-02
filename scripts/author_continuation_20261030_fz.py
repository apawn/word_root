"""Butter, coal, kit and wet: textures, fuels, equipment and moisture."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
B=[['黄油词 butter → 英语性质和食物组合','油润味道、柔滑触感、浅黄色可借名'],['butter + -y/ball/scotch','buttery、butterball；butterscotch 后段有不同解释'],['另源旧 buttery〔贮藏室〕','经法语桶、酒具贮藏相关词，词形受 butter 影响']]
W('buttery','英 /ˈbʌtəri/；美 /ˈbʌtəri/','黄油味的、油润柔滑的；黄油色的；贮藏室〔旧名词，另源〕',
 '饼干有黄油香，布料摸着像黄油一样柔滑，纸张也可淡黄如黄油；性质相似不保证原料真加了黄油。',
 '常用形容词 butter + -y。旧名词贮藏室来自法语 boterie 等桶、酒具相关形式，拼写受 butter 影响，不是只存黄油的小房间。',B,
 'a buttery flavour 黄油风味，a buttery texture 油润柔滑质感，buttery yellow 浅黄；the buttery 在旧建筑语境可指贮藏处。',
 'a buttery flavour；a buttery texture；buttery yellow。',
 'buttery 是感觉、颜色描述时不等于成分说明；旧房间名和常用形容词同形，不直接合并来源。',
 ('The biscuits have a rich, buttery flavour.','饼干有浓郁的黄油风味。'),('The fabric feels soft and buttery.','面料摸着柔软细滑。'))
W('butterscotch','英 /ˈbʌtəskɒtʃ/；美 /ˈbʌtərskɑːtʃ/','黄油糖、奶油硬糖；相应糖浆、风味与浅棕色',
 '黄油和糖熬出的那种香甜味，可做硬糖，也可做浇在冰淇淋上的酱；不是看见 Scotch 就一定加苏格兰威士忌。',
 'butter + scotch，前半黄油清楚；后半有切划糖块、苏格兰等不同分析，资料并不一致，因此不把任何一种当定论。',B[:1]+[['butter + scotch → butterscotch','黄油糖制品；后部命名缘由有争议'],['食物名借用','相似糖浆、风味、颜色']],
 'butterscotch sauce 黄油糖浆酱，butterscotch sweets 黄油糖，butterscotch flavour 黄油糖风味。',
 'butterscotch sauce；butterscotch sweets；butterscotch flavour。',
 'butterscotch 和 caramel 都有糖的风味，名称、原料习惯却不完全相同；scotch 的未定来源也不能用一道现代配方倒推。',
 ('She poured butterscotch sauce over the ice cream.','她把黄油糖浆酱浇在冰淇淋上。'),('The shop sells small bags of butterscotch sweets.','店里卖小袋装黄油糖。'),
 sources=['https://www.etymonline.com/word/butterscotch','https://en.wiktionary.org/wiki/butterscotch#English'])
W('butterball','英 /ˈbʌtəbɔːl/；美 /ˈbʌtərbɔːl/','黄油球、圆团脂肪；胖乎乎的人〔戏谑或贬称〕',
 '黄油搓成一个圆团，是字面 butterball；说人时借圆滚滚形状，可带取笑色彩，不是在说人体由黄油做成。',
 'butter 黄油 + ball 圆球，从圆团食物到体形比喻。也有鸟名等较专门用途，常用先抓这两支。',B[:1]+[['butter + ball → butterball','黄油或类似脂肪小圆团'],['体形比喻','胖乎乎的人这一口语称呼']],
 'small butterballs 小黄油球，shape butter into balls 把黄油做成球；人物称呼看叙述者态度，不当中性体重数据。',
 'small butterballs；a plate of butterballs；call someone a butterball。',
 'butterball 可实物也可取笑人的比喻，ball 说形状；butterfly 的 fly 则另有命名史，不能所有 butter 组合都用这一圆球画面。',
 ('The restaurant served small butterballs with the bread.','餐厅给面包配了小黄油球。'),('In the story, the boy dislikes being called a butterball.','故事里的男孩不喜欢被人叫成胖球。'))
R('B2948','黄油材料、香味与触感各自进入组合','BUTTER：香、润、滑；组合不全是配方','butter → buttery；buttermilk、buttercream 接乳品；butterscotch 糖品；butterball 形状；butternut、buttercup、butterfly 各按名称历史。',
 'buttery texture 可只说手感；butternut squash 不是黄油拌坚果；旧 buttery 贮藏室另源。不要把一切组合都当成原料清单。',
 'butter + -y/ball/scotch；butter + milk/cream/nut/cup/fly；buttery 房间义另接法语贮藏词。',
 [['基础与黄油般性质','butter · buttery'],['食品和形状','buttermilk · buttercream · butterscotch · butterball · butternut'],['植物与昆虫名称','buttercup · butterfly']],
 'buttery 触感与配料；butterscotch 后段未定；butterball 形状比喻；buttermilk、buttercream 具体产品并非逐字配方。',
 'The buttery biscuits tasted of butterscotch.\n\n油润的饼干带着黄油糖的风味。','butter buttery buttermilk buttercream butterscotch butterball butternut buttercup butterfly')
C=[['古英语 col → 中古英语 col、cole → coal','炭、炭火等旧义，后来常指矿物煤'],['中古英语 charcole → charcoal','木材转成炭；前部具体历史有不同分析'],['旧 colier 等 → collier','烧炭卖炭者、煤矿工人；运煤船等']]
W('coal','英 /kəʊl/；美 /koʊl/','煤；炭火、燃着的炭块〔coals〕',
 '现代先想到地下开采、作为燃料的煤；旧词范围还包括炭与火里发红的炭块，所以 hot coals 不必全是矿坑挖出的煤。',
 '继承古英语 col，早期炭、燃烧块等义较宽，矿物煤义后来成为现代重要中心。不是 coal 和 cool 只差元音就构成冷热反义。',C,
 'a coal mine 煤矿，burn coal 烧煤，hot coals 炽热炭块，coal mining 煤矿开采。',
 'a coal mine；burn coal；hot coals；coal mining。',
 'coal 现代矿物煤，charcoal 通常木材等热处理得到的炭；日常 coals 又可说火中炭块，先看场景。',
 ('The train once carried coal from the mine.','这列火车以前从矿上运煤。'),('The food cooked slowly over the hot coals.','食物在热炭火上慢慢烤熟。'))
W('charcoal','英 /ˈtʃɑːkəʊl/；美 /ˈtʃɑːrkoʊl/','木炭；炭笔、炭画；炭灰黑色',
 '木材在受限氧气等条件下变成富碳材料，既可作燃料，也能拿来在纸上画黑线；名称后来还借作颜色。',
 '来自中古英语 charcole。前半有 charren 转变、或法语 charbon 影响等分析；现代 char 烧焦反可能由 charcoal 逆构，不能一律画成 char 先有、再加 coal。',C[:2]+[['英语 charcoal 的用途扩展','燃料木炭；绘画材料、作品和颜色']],
 'a charcoal grill 木炭烤炉，a charcoal sketch 炭笔速写，charcoal grey 炭灰色。',
 'a charcoal grill；a charcoal sketch；charcoal grey。',
 'charcoal 与 coal 都能黑、都能烧，但制造来源不同；画一幅 charcoal 作品也不是拿矿物煤随便代替专用画材。',
 ('The artist drew the portrait in charcoal.','画家用炭笔画了这幅肖像。'),('They cooked dinner on a charcoal grill.','他们用木炭烤炉做晚饭。'),
 sources=['https://www.etymonline.com/word/charcoal','https://en.wiktionary.org/wiki/charcoal#English'])
W('collier','英 /ˈkɒliə/；美 /ˈkɑːliər/','煤矿工人；煤商、炭商；运煤船',
 '职业名围绕煤、炭工作，但海运故事里 a collier 还可能整艘就是运煤船。',
 '中古英语 colier、coler 等，现代可对应 coal + -ier；词干拼写、读音历史变化，不保留完整 coal /koʊl/。后缀人物词也借指运输工具。',C[:1]+[['coler、colier 等 → collier','制作、贩卖煤炭者；煤矿工人'],['工作对象引申','运煤船']],
 'a retired collier 退休煤矿工人，a coal collier 运煤船〔海运语境〕，a collier’s cottage 矿工小屋。',
 'a retired collier；a collier’s cottage；a collier in the harbour。',
 'collier 不等于 collar 领子；港里 arriving collier 可能是船，不是一位工人自己驶进港。',
 ('The retired collier described life underground.','退休煤矿工人描述了井下生活。'),('A collier arrived in the harbour before dawn.','一艘运煤船天亮前抵达港口。'))
R('B3026','炭火旧义、矿物煤与木炭材料','COAL：先分矿物煤和旧炭块用法','coal → coalfield；charcoal 木炭及画材；collier 煤业人物、运煤船。',
 'charcoal 词史比“char 烧焦 + coal”表面拆分复杂，char 动词可能逆构。collier 的 -ier 和煤词干变化也一起交代。',
 'col → coal；charcole → charcoal；coler、colier → collier；coal + field → coalfield。',
 [['煤与煤田','coal · coalfield'],['木炭与煤业人物工具','charcoal · collier']],
 'coal/charcoal 矿物煤与木炭；collier/collar 煤业人物船与领子；char/charcoal 留意逆构方向。',
 'The collier carried coal, while the artist carried charcoal for drawing.\n\n运煤船载着煤，画家则带着绘画用的炭笔。','coal coalfield charcoal collier')
K=[['中古荷兰语 kitte 等 → 英语 kit〔容器、装备〕','装东西的器具 → 里面成套的用品、装备'],['另源动物幼崽 kit','由 kitten、kitling 等缩短，不是装备生出小猫'],['kitty 的两路','猫的昵称接 kitten 等；公共钱池近源未定，可能联系 kit 一套物品']]
W('kit','/kɪt/','成套用品、装备；组装套件；幼崽〔另一来源〕',
 '一套急救用品、修理用具放在一起，就是 kit；买来零件自己拼的模型也叫 kit。狐狸幼崽 kit 则另有猫幼崽词的缩短背景。',
 '装备义从可能接中古荷兰语 kitte 的容器名发展到所装整套用品；幼崽义由 kitten、kitling 缩短等路径而来，另有更冷门同形乐器词。',K,
 'a first aid kit 急救包，a repair kit 维修套件，a model kit 模型套件，a fox kit 狐狸幼崽，kit someone out 配齐装备。',
 'a first aid kit；a repair kit；a model kit；kit out。',
 'kit 说成套配置，不只外面的包；kit 幼崽与 kit 工具包同音同形却非同一路词义。',
 ('Keep a first aid kit in the car.','在车里放一个急救包。'),('She built the model from a kit.','她用套件拼出了模型。'))
W('kitty','/ˈkɪti/','小猫、猫咪；公用款、钱池',
 '招呼猫咪的 kitty 是亲昵口吻；旅行大家各出一点放进 the kitty，却是在攒公用钱，不是给猫投喂硬币。',
 '猫义与 kitten 变体、昵称材料有关，也可能受人名昵称 Kitty 影响；钱池义来源未定，有 kit 成套用品加小后缀的分析，也有其他旧俚语路径。',K[1:]+[['英语 kitty 的常用同形义','猫咪昵称；公共经费池']],
 'a little kitty 小猫咪，put money in the kitty 凑钱进公款，the holiday kitty 旅行公用款。',
 'a little kitty；put money in the kitty；a holiday kitty。',
 'kitty 钱池不等于 cat 猫的所有物；kitty 两支不能简单画成工具包里装猫、猫变钱的演化。',
 ('The little kitty slept beside the window.','小猫咪睡在窗边。'),('We each put ten pounds into the kitty for dinner.','我们各拿出十英镑，凑作晚饭公款。'),
 sources=['https://www.etymonline.com/word/kitty','https://en.wiktionary.org/wiki/kitty#English'])
W('rootkit','/ˈruːtkɪt/','隐蔽控制系统的一组恶意软件工具、根套件',
 '把控制计算机、隐藏痕迹等工具配成一套；root 在这里接系统高权限那条技术用法，不是植物根部修剪工具包。',
 'root 系统特权用户、根权限相关名称 + kit 工具套件，命名一类隐蔽控制系统的软件工具。现代用法不要求每个变种一定只在类 Unix 系统。',K[:1]+[['root〔系统权限名〕+ kit → rootkit','用于隐蔽控制系统的软件工具集合']],
 'detect a rootkit 检出根套件，a rootkit infection 根套件感染，rootkit detection 根套件检测。',
 'detect a rootkit；rootkit detection；a rootkit infection。',
 'rootkit 是安全语境的特定工具类，不是所有需要管理员权限的正常软件；toolkit 则只是广义工具包。',
 ('The security scan detected a rootkit.','安全扫描检测到了一组隐蔽控制软件。'),('The report explains why rootkit detection can be difficult.','报告解释了为什么根套件可能难以检测。'))
R('B3723','装在一起的一套，动物幼崽另源','KIT：容器到成套装备；KITTY 不全接这支','kit → toolkit、rootkit；kit 幼崽接 kitten 等缩短；kitty 猫称呼、钱池分别辨来源。',
 'kitty 公款的起源未定，不能因为可以放进包就当成确定的 kit + -y 历史。rootkit 则明确取技术权限与套件材料。',
 'kitte 等容器名 → kit 成套用品；tool/root + kit；kitten、kitling → kit 幼崽；kitty 两路另辨。',
 [['成套装备与同形基础','kit'],['猫昵称、公共款与软件套件','kitty · toolkit · rootkit']],
 'kit/toolkit 成套用品与特定工具包；kitty 猫与公款同形；rootkit 不泛指任何管理员软件。',
 'We used money from the kitty to buy a repair kit.\n\n我们用公用款买了一套维修工具。','kit kitty toolkit rootkit')
W('wet','/wet/','湿的、潮湿的；弄湿；雨水、雨天',
 '干东西吸了水、表面沾了液体，就是 wet；用作动词就是让它从干到湿。',
 '接古英语 wǣt、wǣtan 等湿、水相关词族，中古英语过去分词形态与旧形容词也发生合流。更远与 water 同族，不是现代 water 剪掉几字母就造出 wet。',
 [['古英语 wǣt、wǣtan 等 → 中古英语 wet、weten','湿的；使湿，相应形态交汇'],['英语 wet','湿、弄湿；湿天气等名词']],
 'wet clothes 湿衣服，wet paint 未干油漆，wet the cloth 把布弄湿，get wet 淋湿；比较级 wetter、最高级 wettest 双写 t。',
 'get wet；wet clothes；wet paint；wet the cloth。',
 'wet 较直接说沾水、液体多，damp 常只微潮；wetter 日常常是更湿的比较级，独立名词湿润剂等较专门。',
 ('My shoes got wet in the rain.','我的鞋被雨淋湿了。'),('Wet the cloth before wiping the table.','擦桌子前先把布弄湿。'))
R('B3010','东西沾了水，或把它弄出水分','WET：湿的，也能说弄湿','wet → wetter、wettest 规则比较；wetland、wetsuit 各有自然环境、服装功能专名。',
 'wet paint 说漆还没干，不要求正在下雨；wetsuit 湿式潜水服名称也有具体设计原理，不能只理解成任何湿衣服。',
 'wǣt、wǣtan 等 → wet；wet + -er/-est → wetter、wettest；wet + land/suit。',
 [['湿与弄湿基础','wet'],['湿地与服装组合','wetland · wetsuit']],
 'wet/damp 湿与微潮；wetter 比较级与专门名词看语境；wet paint 不等于雨水。',
 'The wetsuit was still wet when we left the wetland.\n\n我们离开湿地时，湿式潜水服仍是湿的。','wet wetland wetsuit')
ROOTS[-1]['exclude']['wetter']='日常比较级 wetter 已解释；湿润剂等独立名词较专门，暂不单列。'
if __name__=='__main__':save('continuation_20261030_fz',ROOTS,WORDS)
