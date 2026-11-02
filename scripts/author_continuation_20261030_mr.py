"""Selected ite names, haul, reed and spoon."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
It=[['希腊 -itēs，经拉丁、法语 -ite','属于、来自、与……相关；用于人物、地方及矿物等名'],['现代科学与文化命名','矿石、化石、物质名及虚构材料，具体前项各有来历']]
W('bauxite','英 /ˈbɔːksaɪt/；美 /ˈbɔːksaɪt/','铝土矿',
 '看名字别先找一种叫 baux 的元素：baux 来自法国地名 Les Baux。它是按产地命名、富含铝的矿石材料。',
 'Les Baux 地名 + -ite 矿物、材料命名后缀；英语按拼写读出 /ks/。铝土矿是多种矿物组成的材料，不是一个纯净单一矿物种。',It+[['法国 Les Baux + -ite → bauxite','以产地命名的铝土矿']],
 'bauxite ore 铝土矿石，bauxite deposits 铝土矿矿床；是重要的铝矿石来源。',
 'bauxite ore；bauxite deposits。',
 'bauxite 是矿石，aluminium／aluminum 是元素铝；二者不在同一个物质类别层次。',
 ('The region has large deposits of bauxite.','这个地区有大规模铝土矿矿床。'),('Bauxite is an important ore used to produce aluminium.','铝土矿是生产铝的重要矿石。'),sources=['https://en.wiktionary.org/wiki/bauxite#English','https://www.usgs.gov/centers/national-minerals-information-center/bauxite-and-alumina-statistics-and-information'])
W('lignite','/ˈlɪɡnaɪt/','褐煤',
 'lign- 让你想到木、木质材料；lignite 是一种煤，名字借了这种联系。先把它认成煤的类别，不当作普通木柴。',
 '借法语 lignite，由拉丁 lignum 木材、木柴 + -ite 构成材料名称；现代指较低煤阶的褐煤。',It+[['拉丁 lignum + -ite，经法语 → lignite','以木质联系命名的褐煤']],
 'lignite deposits 褐煤矿藏，lignite mining 褐煤开采，brown coal 褐煤的另一常用称呼。',
 'lignite deposits；brown coal。',
 'lignite 与 lignin 木质素都含木词根，但不是同一物质；词根关联不等于化学、地质类别相同。',
 ('The mine produces lignite rather than hard coal.','这座矿生产褐煤，而不是硬煤。'),('The report describes the region’s lignite deposits.','报告介绍了这个地区的褐煤矿藏。'))
Am=[['Ammon／Amun 神名及羊角形象','旧名称把盘曲外壳比作阿蒙的羊角'],['法语 ammonite → ammonite','菊石及其化石，使用 -ite 名称形式']]
W('ammonite','/ˈæmənaɪt/','菊石；菊石化石',
 '常见菊石化石一圈圈盘起来，像卷曲羊角。名字里的 Ammon 联系带羊角形象的阿蒙神，因此不是按今天中文菊花来拆英文。',
 '经法语 ammonite 接旧的阿蒙之角命名传统，Ammon + -ite。现代指已灭绝的有壳头足类及其化石；常见盘卷外形有多种变化。',Am,
 'an ammonite fossil 一块菊石化石，an ammonite shell 菊石壳；化石记录的是曾经生活的海洋动物。',
 'an ammonite fossil；an ammonite shell。',
 'ammonite 不是普通蜗牛，属于已灭绝的头足类；外形相似不等于现代动物分类相同。',
 ('The museum displayed a large ammonite fossil.','博物馆展出了一块大型菊石化石。'),('The ammonite’s shell had a clear spiral pattern.','菊石壳有清晰的螺旋纹路。'),sources=['https://en.wiktionary.org/wiki/ammonite#English','https://www.nhm.ac.uk/discover/what-is-an-ammonite.html'])
K=[['超人故乡 Krypton + -ite','仿物质名称形成虚构氪石名'],['超人故事中的弱点 → 日常 kryptonite','让强者失去优势、抵抗力的弱点比喻']]
W('kryptonite','/ˈkrɪptənaɪt/','〔虚构〕氪石；致命弱点、难以抗拒的东西',
 '超人平时很强，碰到某些氪石就会受影响；日常说 chocolate is my kryptonite，是夸张说自己一遇巧克力就没了抵抗力。',
 'Krypton 虚构星球名 + -ite，仿矿物、材料命名。普通小写用法从故事弱点扩展为个人难以克服的诱惑、短板。',It[:1]+K,
 'someone’s kryptonite 某人的致命弱点、难抗拒之物，green kryptonite 绿色氪石；虚构故事不同种类的设定不完全相同。',
 'someone’s kryptonite；my kryptonite。',
 'kryptonite 是虚构材料、文化比喻，不是现实元素 krypton 氪的另一个科学名称；比喻也不必真有危险。',
 ('In the story, green kryptonite weakens Superman.','故事里，绿色氪石削弱了超人的力量。'),('Chocolate cake is my kryptonite.','巧克力蛋糕是我的软肋，我一见就没抵抗力。'),sources=['https://en.wiktionary.org/wiki/kryptonite#English','https://www.dc.com/blog/2025/05/29/crushed-by-color-a-kryptonite-catalogue'])
R('A1903','属于、来自某处的名称形式，扩展到矿物、化石和物质','-ITE：前项给来历，后缀给它一个成员、材料式名称','bauxite 地名、lignite 木、ammonite 羊角神名；kryptonite 仿材料命名。',
 '不要把所有 -ite 都当同一种矿物：有矿石、煤、化石，也有人物和生物化学类别。以具体前项和整词定义为准。',
 '希腊 -itēs 经拉丁、法语发展；另一化学盐后缀 -ite 与 -ate 的命名体系有关，逐词辨。',
 [['矿石、煤与矿物名称','bauxite · lignite · calcite · magnetite · pyrite · ferrite'],['天外来源与古生物名称','meteorite · ammonite'],['其他物质及虚构命名','dynamite · kryptonite'],['人物、生物化学与形状名称','socialite · metabolite · dendrite']],
 '相同词尾不等于相同分类；bauxite 不是单一纯矿物，ammonite 是动物、化石，kryptonite 是虚构材料。',
 'The display separated bauxite ore, an ammonite fossil and a fictional kryptonite prop.\n\n展台把铝土矿、菊石化石和虚构氪石道具分开放置。','bauxite lignite calcite magnetite pyrite ferrite meteorite ammonite dynamite kryptonite socialite metabolite dendrite')
H=[['法语 haler 与日耳曼相应拉、取词','拉、拖，进入中古英语 halen 等'],['英语 haul','费力拉、搬运；一趟路及取得的一批东西'],['后续构词','haulage 货运业务；hauler 承运者；overhaul 全面检修']]
W('haul','英 /hɔːl/；美 /hɔːl/','用力拖、搬运；运输；一批收获；一段路程',
 '箱子又重又笨，要费劲拉走，就是 haul。捕鱼、购物回来拿到的一大批东西，也能叫 a haul。',
 '经中古英语 halen 等，联系法语 haler 及日耳曼相应拉取词，可能还有本族旧形式合流。名词从搬运、拉取发展到路程和所得。',H[:2],
 'haul a heavy box 搬拖重箱，haul goods 运货，a shopping haul 购物收获，a long haul 长途、长期艰难过程。',
 'haul goods；a shopping haul；a long haul。',
 'haul 通常比普通 carry 多一点费劲、距离长或数量大的感觉；一大批收获不一定违法，需看对象。',
 ('They hauled the heavy table upstairs.','他们费劲把重桌子搬上楼。'),('The fishing boat returned with a good haul.','渔船带着不错的渔获回来了。'))
W('haulage','英 /ˈhɔːlɪdʒ/；美 /ˈhɔːlɪdʒ/','货物运输、货运业务；运输费',
 'haul 是拉、运，haulage 常把重货运输当一项业务来说。读 road haulage，就想到卡车等公路货运这一行。',
 'haul + -age，形成活动、业务及相关费用名词。英式商业用语里尤其常见。',H[:2]+[['haul + -age → haulage','运输活动、业务及其费用']],
 'road haulage 公路货运，a haulage company 货运公司，haulage costs 运输费用。',
 'road haulage；a haulage company。',
 'haulage 不表示乘客本人；通常看货物、重载运输业务，旅客运输用语需另看场景。',
 ('The company specialises in road haulage.','这家公司专做公路货运。'),('Higher haulage costs affected the delivery budget.','较高运输费用影响了交货预算。'))
W('hauler','英 /ˈhɔːlə/；美 /ˈhɔːlər/','运输者、承运公司；搬运车辆',
 '谁负责把那一车货运走，谁或什么车就可以 hauler。-er 可以人，也可以承担运输的公司、车辆。',
 'haul + -er，承中古英语相应人物形式；美式常见 hauler，英式也常用相关形式 haulier。',H[:2]+[['haul + -er → hauler','从事运输的人、公司或车辆']],
 'a freight hauler 货物承运者，a waste hauler 废物清运公司、车辆，a heavy hauler 重型运输车辆。',
 'a freight hauler；a waste hauler。',
 'hauler 强调实际运输角色，不等于货物买方、卖方；-er 也不保证对象一定是个人。',
 ('The hauler collected the goods early in the morning.','承运方一早来收了货。'),('A waste hauler removed the old furniture.','一家清运公司运走了旧家具。'))
W('overhaul','名词英 /ˈəʊvəhɔːl/、美 /ˈoʊvərhɔːl/；动词英 /ˌəʊvəˈhɔːl/、美 /ˌoʊvərˈhɔːl/','全面检修、翻修；彻底改革；大修',
 '不是拧紧一颗松螺丝就走，而是把整套系统检查、修整一遍；机器能 overhaul，过时的制度也能 overhaul。',
 'over- + haul，早期航海用法涉及反向拉绳、松开索具以检查，后来扩展为全面检修、改革。名词常重读前部，动词常重读后部。',H[:2]+[['航海 over- + haul → overhaul','检查、修整索具 → 全面检修、改革']],
 'overhaul an engine 全面检修发动机，overhaul a system 彻底改革系统，need an overhaul 需要大修、全面整改。',
 'overhaul a system；need an overhaul。',
 'overhaul 的 over- 不在此简单译运得过多；常用核心是全面检查、更新，也有追上、超过的其他用法。',
 ('The engine needs a complete overhaul.','发动机需要一次全面大修。'),('The school overhauled its admissions process.','学校彻底改革了招生程序。'),sources=['https://en.wiktionary.org/wiki/overhaul#English','https://www.etymonline.com/word/overhaul'])
R('B4282','用力拉、搬运，到货运业务、角色和全面检修','HAUL：费劲把东西拉过来、运过去','haul → haulage、hauler；overhaul 还要接航海检视的历史。',
 '动作、业务、承运者按后缀连着记。overhaul 从旧索具检查发展为整套检修，不能只按现代搬运逐字翻译。',
 'haler、halen 等旧拉取词 → haul；-age 活动、费用；-er 执行者；overhaul 有航海词史。',
 [['运输动作、业务及承运者','haul · haulage · hauler'],['全面检修、改革','overhaul']],
 'a haul 可一批收获；hauler 可以公司、车辆；overhaul 名词、动词常有重音差别。',
 'The hauler arranged an overhaul of the truck before the long haul.\n\n长途运输前，承运方安排给卡车大修。','haul haulage hauler overhaul')
Re=[['古英语 hrēod → 中古英语 red → reed','芦苇等高细草本植物，深源未定'],['植物材料 → 振动发声薄片','乐器中的簧片'],['reed + -y → reedy','多芦苇；声音高细、外形细长']]
W('reed','/riːd/','芦苇；苇秆；簧片',
 '水边一片高细植物可以 reeds；乐器里一片薄材料随气流振动发声，也叫 reed。它把植物材料名移到了相应发声部件。',
 '承古英语 hrēod，经中古英语 red 延续，日耳曼词族的更远来源未定；簧片义由相关材料、用途发展。',Re[:2],
 'a reed bed 芦苇丛，a reed stem 苇秆，a clarinet reed 单簧管簧片；现代簧片材料不必都是真芦苇。',
 'a reed bed；a clarinet reed。',
 'reed 的簧片义不是所有管乐器的共同部件；具体乐器怎样发声要另看结构。',
 ('Reeds grew along the edge of the lake.','湖边长着芦苇。'),('The musician replaced the clarinet’s reed.','乐手换了单簧管的簧片。'))
W('reedy','/ˈriːdi/','多芦苇的；细长的；声音高而细的',
 '岸边长满芦苇是 reedy bank；声音细细高高、带一点尖亮感，也能 reedy。前者看植物数量，后者借簧片声的联想。',
 'reed + -y，中古英语已有对应形式；形成有芦苇、像芦苇或簧片相关特征的形容词。',Re[:2]+[['reed + -y → reedy','多芦苇；细长、声调高细']],
 'a reedy bank 芦苇岸，a reedy voice 高细嗓音，a tall, reedy figure 高而瘦长的身影。',
 'a reedy voice；a reedy bank。',
 'reedy voice 不是喉咙里真的长芦苇，也不表示所有簧片乐器声音都很细弱；这是特征比喻。',
 ('A reedy voice called from behind the door.','门后传来一个高细的声音。'),('Ducks hid in the reedy shallows.','鸭子藏在长着芦苇的浅水处。'))
R('B3738','植物、材料与振动簧片，形容词再借细长和音色','REED：一根细长苇秆，也能成为发声材料的名字','reed → reedy。',
 '实体芦苇、簧片部件与声音性质连起来看。材料名转功能名后，即便换材料，名称也可能继续使用。',
 'hrēod → reed；-y 具有、类似相应特征。',
 [['植物、乐器部件及相关性质','reed · reedy']],
 'reed 不保证所有现代簧片都用真芦苇；reedy 声音是细高音色评价。',
 'The clarinet reed produced a thin, reedy note.\n\n单簧管簧片发出一个高细的音。','reed reedy')
Sp=[['古英语 spōn','木片、削下的薄片'],['中古英语 spon、spoon','木片名走向取食、盛食的勺；北欧相应词也有联系'],['spoon + -ful → spoonful','一勺能容下的量']]
W('spoon','/spuːn/','勺、匙；用勺舀、盛',
 '长柄前面有个凹进去的小碗，可以舀汤、搅拌，就是 spoon。旧名字先说木片，后来随材料用途发展成勺。',
 '承古英语 spōn 木片、削片，经中古英语 spoon 等形成器具义，也与北欧相关勺名有联系；现代勺不要求木制。',Sp[:2],
 'a soup spoon 汤匙，a wooden spoon 木勺，spoon sauce over something 用勺把酱汁舀上去；teaspoon、tablespoon 再限定勺类。',
 'a soup spoon；spoon over。',
 'spoon 器具名与动词舀、盛分清；born with a silver spoon in one’s mouth 是出身富裕的比喻。',
 ('She stirred the soup with a wooden spoon.','她用木勺搅汤。'),('He spooned the sauce over the vegetables.','他用勺把酱汁舀在蔬菜上。'),sources=['https://en.wiktionary.org/wiki/spoon#English','https://www.etymonline.com/word/spoon'])
W('spoonful','/ˈspuːnfəl/','一勺的量',
 '手里这把勺装一次能装多少，就是 a spoonful。重点不是又多了一把勺，而是勺里承载的那一份。',
 'spoon + -ful，-ful 在这里是容器所容纳量的名词后缀；中古英语已有相应形式。',Sp+[['spoon + -ful → spoonful','一勺所容纳的量']],
 'a spoonful of sugar 一勺糖，two spoonfuls 两勺量，a heaped spoonful 堆得冒尖的一勺，a level spoonful 平平一勺。',
 'a spoonful of；a heaped spoonful。',
 '复数通常 spoonfuls；只有 spoonful 没规定勺子大小和是否冒尖，精确配方需看其他限定。',
 ('She added a spoonful of sugar to the bowl.','她往碗里加了一勺糖。'),('He ate two spoonfuls and put the spoon down.','他吃了两勺，就把勺子放下了。'))
R('B3675','木片旧名变勺，再按容器量与勺类细分','SPOON：凹处能盛东西，一次盛多少就是 spoonful','spoon → spoonful；teaspoon、tablespoon 说明具体勺类。',
 '器具、动作、所盛的量分三层看。-ful 在本词是数量名词后缀，和有某性质的形容词用法不同。',
 'spōn 木片 → spoon 勺；-ful 所容纳量；tea、table 限定勺名。',
 [['器具、所盛量与具体勺类','spoon · spoonful · teaspoon · tablespoon']],
 'spoonfuls 常规复数；不说明勺子大小时，不自行当成一个固定毫升数。',
 'She measured one spoonful with the tablespoon.\n\n她用大汤匙量了一勺。','spoon spoonful teaspoon tablespoon')
if __name__=='__main__':save('continuation_20261030_mr',ROOTS,WORDS)
