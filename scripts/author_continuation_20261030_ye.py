"""Everyday places and landscapes: farms, forests, rivers, islands and waves."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'B3410':dict(words=['farm','farms'],label='farm → farms：从租地背景到种养场所',note='早期固定租金、租地背景发展为农场；更早路线有争议，现代 farm 也可作经营种养的动词。'),
 'A1741':dict(words=['garden','gardens'],label='garden → gardens：围起、照料的园地',note='经法语借入的围地词族，与本族 yard 同源，路线不同。'),
 'B3298':dict(words=['forest','forests'],label='forest → forests：林地与旧狩猎保留地',note='经古法语接中世纪拉丁林地名称，更早来源有不同分析。'),
 'B3781':dict(words=['park','parks'],label='park → parks：围起的场区与停车',note='围地的名词发展为公园等，集中安放的动词发展为停车。'),
 'C0762':dict(words=['mountain','mountains'],label='mountain → mountains：高山与大量困难、工作',note='拉丁 mons／montis 词族经罗曼语、法语山地名词进入英语。'),
 'B3100':dict(words=['river','rivers'],label='river → rivers：从河岸名称到河流',note='接拉丁 ripa 河岸及 riparia 岸边地带，经法语进入英语。'),
 'B3037':dict(words=['lake','lakes'],label='lake → lakes：较早英语与法语水体词的影响',note='古英语 lacu 与法语 lac、拉丁 lacus 背景在中古英语中相互影响，现代湖泊义承接这些材料。'),
 'B3390':dict(words=['island','islands'],label='island → islands：岛与土地；后来添上的 s',note='本族岛加土地的复合词，后来受 isle 影响添写不发音 s。'),
 'A1776':dict(words=['valley','valleys'],label='valley → valleys：两侧高地之间的低地',note='拉丁 vallis 经法语借入；复数直接加 s，保留 y。'),
 'B3361':dict(words=['beach','beaches'],label='beach → beaches：水边的沙、砾岸滩',note='中古英语岸滩词，具体远源未定；es 在 ch 后增加 iz。'),
 'C0850':dict(words=['ocean','oceans'],label='ocean → oceans：古代大水体名称与现代大洋',note='希腊 Okeanos 经拉丁、法语借入，较早更远来源不定。'),
 'B3706':dict(words=['wave','waves'],label='wave → waves：水的起伏、手的摆动与一波波事件',note='水波名词和摆动动词的较早词形不同，现代拼写靠拢，保留两路背景。'),
}
W('farms','英 /fɑːmz/；美 /fɑːrmz/','农场；经营种植、养殖〔第三人称单数〕',
 '把土地、设施用于种庄稼、养动物的地方，是 farms；一个人经营这些种养活动，也可以说 farms。',
 'farm + -s，/m/ 后读 /z/。farm 有中古英语、法语及中世纪拉丁固定租金、租地的背景，后来从租地走向农业经营；更早来源细节有争议。',
 [['中古英语、法语及中世纪拉丁相关词形 → farm','固定租金、租地 → 农场、农业经营'],['farm + -s → farms','多家农场；单数主语经营种养']],
 'small farms 小农场；dairy farms 奶牛场；farms the land 耕种经营土地；fish farms 养鱼场。',
 'farms in the valley；farms run by families。','farms 不只种植物，也可以养牛、养鱼；farmland 侧重农用土地，farms 常把土地、设施和经营作为一个个整体。',
 ('The valley is dotted with small farms.','山谷里散布着小农场。'),('She farms the land with her brother.','她和哥哥一起耕种经营那片土地。'),sources=['https://en.wiktionary.org/wiki/farms#English','https://en.wiktionary.org/wiki/farm#English'])
W('gardens','英 /ˈɡɑːdənz/；美 /ˈɡɑːrdənz/','花园、菜园、园地〔复数〕；做园艺〔第三人称单数〕',
 '把一片地方围起、照料，让花草、蔬菜长起来，是 garden 的具体画面；多块园地是 gardens，动词则说种植、打理园子。',
 'garden + -s，/n/ 后读 /z/。garden 经盎格鲁诺曼语 gardin 等借入，较早是日耳曼围地词族；与英语本族词 yard 同源，但借入路线不同。',
 [['日耳曼围地词族 → 法语 gardin 等 → garden','围起、照料的园地'],['garden + -s → gardens','多个花园、菜园；单数主语做园艺']],
 'public gardens 公共花园；vegetable gardens 菜园；gardens behind the houses 屋后的花园；gardens every weekend 每周末打理园子。',
 'botanical gardens；gardens full of flowers。','garden 可以是花园，也可以是菜园，不只按种花理解。gardens 有时用于一个大型园区、正式名称，实际是否分成多个独立花园要看地点。',
 ('The houses have small gardens at the back.','这些房子后面都有小花园。'),('She gardens whenever she has a free afternoon.','只要有空闲的下午，她就会打理园子。'),sources=['https://en.wiktionary.org/wiki/gardens#English','https://en.wiktionary.org/wiki/garden#English'])
W('forests','英 /ˈfɒrɪsts/；美 /ˈfɔːrɪsts, ˈfɑːrɪsts/','森林；大片林地〔复数〕',
 '树木成片覆盖的一大块地方，日常可以叫 forest；不同地方、不同类型的森林合起来就是 forests。',
 'forest + -s，/t/ 后读 /s/。forest 经古法语接中世纪拉丁 forestis，历史上还涉及狩猎保留地，范围并不只由树木多少决定；更早来源有不同分析。',
 [['中世纪拉丁 forestis → 古法语 forest → 英语 forest','林地、狩猎保留地 → 森林'],['forest + -s → forests','多片或不同类型的森林']],
 'tropical forests 热带森林；pine forests 松林；forests in the mountains 山中森林。',
 'walk through forests；forests covering the hills。','forest 常比 wood、woods 带更大片林地的感觉，但实际分类、称谓因地区而异。历史文件里的 forest 还可能指受专门管理的狩猎区域，不能只按现代密林画面理解。',
 ('Pine forests cover the hills above the town.','镇子上方的山丘覆盖着松林。'),('The exhibition shows photographs of forests from different regions.','展览展示了不同地区森林的照片。'),sources=['https://en.wiktionary.org/wiki/forests#English','https://en.wiktionary.org/wiki/forest#English'])
W('parks','英 /pɑːks/；美 /pɑːrks/','公园；专门园区〔复数〕；停车、安放〔第三人称单数〕',
 '划出、围起一片地方，供某种用途使用，可以是 parks；把车辆安放在一个位置，则是动词 parks。',
 'park + -s，/k/ 后读 /s/。park 经法语 parc 的围地名称进入英语，更早联系围栏、围起土地的词族；动词经集中安放等用法发展为停车。',
 [['法语 parc → 中古英语、英语 park','围地、园地 → 公园、专门场区'],['park + -s → parks；动词安放分支','多个公园；单数主语停车']],
 'public parks 公共公园；national parks 国家公园；business parks 商业园区；parks the car 停车。',
 'parks near the river；parks outside the house。','parks in the city 可以说城里的公园；She parks in the city 则是她把车停在城里，主语和句法决定词性。park 的名词范围还包括专门用途园区。',
 ('The town has several small parks beside the river.','这个镇子沿河有几个小公园。'),('She parks her bicycle near the library entrance.','她把自行车停在图书馆入口附近。'),sources=['https://en.wiktionary.org/wiki/parks#English','https://en.wiktionary.org/wiki/park#English'])
W('mountains','/ˈmaʊntɪnz/','山、高山〔复数〕；大量事物〔mountains of〕',
 '一座座明显隆起的高地，就是 mountains；工作、纸张堆得像山一样多，也可以说 mountains of。',
 'mountain + -s，/n/ 后读 /z/。mountain 经法语 montaigne、muntaine 等接罗曼语山地名称，较早是拉丁 mōns、词干 mont-；现代作为完整词使用。',
 [['拉丁 mōns、mont- 及山地词 → 罗曼语、法语 → mountain','山、高地、山地'],['mountain + -s → mountains','多座山；比喻大量、堆积']],
 'snowy mountains 雪山；in the mountains 在山区；mountains of paperwork 大量文书工作；move mountains 克服巨大困难〔习语〕。',
 'mountains in the distance；a range of mountains。','mountain 通常给人比 hill 更高大、起伏更明显的感觉，具体命名会有地区习惯。mountains of 强调数量非常多，不要求真的堆出山形。',
 ('We could see snow on the distant mountains.','我们能看见远山上的积雪。'),('She had mountains of paperwork to finish.','她有一大堆文书工作要完成。'),sources=['https://en.wiktionary.org/wiki/mountains#English','https://en.wiktionary.org/wiki/mountain#English'])
W('rivers','英 /ˈrɪvəz/；美 /ˈrɪvərz/','河流〔river 的复数〕',
 '沿着河岸向前流动的一条条水道，就是 rivers。这个名字的历史从河岸、岸边地带走向了河流本身。',
 'river + -s，读 /z/。river 经法语 rivere、riviere 等接拉丁 rīpāria 岸边地带，较早 rīpa 表河岸；不要与另一个表示小溪的拉丁 rīvus 直接混为一条借词路线。',
 [['拉丁 rīpa、rīpāria → 法语 riviere 等 → river','河岸、岸边地带 → 河流'],['river + -s → rivers','多条河流']],
 'rivers and lakes 河流与湖泊；rivers flowing through the valley 流经山谷的河；the banks of rivers 河岸。',
 'rivers meeting near the town；bridges over rivers。','river 重点是有流向、沿水道流动的河；lake 是较集中的湖泊水体。a river of people 还可以比喻不断向前流动的人群，注意看是否在形容画面。',
 ('Two rivers meet just below the town.','两条河在镇子下方不远处交汇。'),('The map shows the rivers that flow into the lake.','地图上标出了流入这个湖的河流。'),sources=['https://en.wiktionary.org/wiki/rivers#English','https://en.wiktionary.org/wiki/river#English'])
W('lakes','/leɪks/','湖泊〔lake 的复数〕',
 '水聚在较集中的一片低地、盆地里，形成湖；不同的一片片湖泊合起来就是 lakes。',
 'lake + -s，/k/ 后读 /s/。水体名 lake 有古英语 lacu 与法语 lac 的背景，法语词接拉丁 lacus；这些形式在中古英语阶段相互影响、合流，现代常指湖。',
 [['古英语 lacu；法语 lac、拉丁 lacus → 中古英语 lake','较早溪流、水池、湖等水体名称的共同影响'],['lake + -s → lakes','多个湖泊']],
 'mountain lakes 山间湖泊；freshwater lakes 淡水湖；lakes and rivers 湖泊与河流。',
 'lakes surrounded by forests；lakes in the valley。','湖名常见 Lake 加名称，普通复数 lakes 则说几个湖。river 强调河道中的流动，lake 强调较集中、四周有陆地围住的水体。',
 ('Several small lakes lie between the mountains.','群山之间分布着几个小湖。'),('The route passes two lakes before reaching the village.','这条路线在到达村庄前会经过两个湖。'),sources=['https://en.wiktionary.org/wiki/lakes#English','https://en.wiktionary.org/wiki/lake#English'])
W('islands','/ˈaɪləndz/','岛屿〔island 的复数〕',
 '一块土地四周被水围住，是 island；一座座岛屿就是 islands。这个词里的 s 是后来添进拼写的，通常不发音。',
 'island + -s，末尾 /d/ 后读 /z/。早期英语是岛的旧词 ieg、ig 与 land 土地组成，经历 iland、yland 等形式；后来受 isle 拼写影响加入不发音的 s。',
 [['古英语岛的词 + land → igland 等 → 中古英语 iland、yland','本族复合词：岛、土地'],['受 isle 影响拼成 island；再加 -s → islands','添写不发音 s → 多座岛屿']],
 'small islands 小岛；tropical islands 热带岛屿；a group of islands 一组岛屿；islands off the coast 近海岛屿。',
 'travel between islands；islands in the lake。','island 开头读 /aɪ/，中间 s 不发音，复数末尾才有 /z/。英语 isle 是另一条借词路线，虽影响 island 拼写，却不把 island 本来的来源变成拉丁词。',
 ('A ferry connects the three islands.','一艘渡轮往返连接这三座岛。'),('The lake contains several small islands.','湖里有几座小岛。'),sources=['https://en.wiktionary.org/wiki/islands#English','https://en.wiktionary.org/wiki/island#English'])
W('valleys','/ˈvæliz/','山谷；谷地〔valley 的复数〕',
 '两侧有更高的山地，中间低下去、常有河流经过的地方，是 valley；多个山谷就是 valleys。',
 'valley + -s，y 前有元音 e，所以保留 y，直接加 s。valley 经盎格鲁法语 valey、古法语 valee 等接拉丁 vallis 山谷，更远来源不明。',
 [['拉丁 vallis → 法语 valee、valey → valley','山谷、谷地'],['valley + -s → valleys','多条山谷；保留 y 的复数']],
 'deep valleys 深谷；river valleys 河谷；valleys between mountains 山间谷地。',
 'villages in the valleys；valleys filled with mist。','valleys 和 keys 一样，y 前有元音，普通复数加 s。city 的 y 前是辅音，通常变 cities；先看 y 前面的字母，再选拼写。',
 ('Mist filled the valleys below us.','我们下方的山谷里弥漫着雾。'),('Small villages lie in the valleys between the hills.','小村庄坐落在丘陵之间的谷地里。'),sources=['https://en.wiktionary.org/wiki/valleys#English','https://en.wiktionary.org/wiki/valley#English'])
W('beaches','/ˈbiːtʃɪz/','海滩、湖滩、河岸滩地〔复数〕；使上滩、搁浅〔第三人称单数〕',
 '水边铺着沙、石子等的一片岸滩，就是 beach；多处滩地是 beaches。把船拖到滩上，动词也可以用 beach。',
 'beach + -es，/tʃ/ 后增加 /ɪz/。beach 接中古英语 bache 等相关岸滩形式，更早来源有不同分析；动词由上滩场景形成。',
 [['中古英语相关岸滩词 → beach','沙、砾石等组成的岸滩'],['beach + -es → beaches；相关动词','多处滩地；单数主语使上滩']],
 'sandy beaches 沙滩；pebble beaches 砾石滩；beaches along the coast 沿海滩地。',
 'walk along the beaches；quiet beaches near the village。','beach 不一定只在海边，湖边、河边也可有 beach；也不保证都是细沙，pebble beach 是石子、砾石滩。shore 更广地说水陆交界的岸边。',
 ('The island has several quiet beaches.','这座岛有几处安静的海滩。'),('We visited both sandy and pebble beaches along the coast.','我们沿海既去了沙滩，也去了砾石滩。'),sources=['https://en.wiktionary.org/wiki/beaches#English','https://en.wiktionary.org/wiki/beach#English'])
W('oceans','英 /ˈəʊʃənz/；美 /ˈoʊʃənz/','海洋、大洋〔复数〕；大量〔oceans of，较口语〕',
 '地球上相连的广大咸水区域，可以按不同大洋来称呼 oceans；像海一样多的时间、空间，也偶尔用 oceans of 来夸张表达。',
 'ocean + -s，/n/ 后读 /z/。ocean 经古法语 occean、拉丁 ōceanus 接希腊 Ōkeanós，古代是想象中环绕陆地的大水体名称，更远来源未明。',
 [['希腊 Ōkeanós → 拉丁 ōceanus → 法语、英语 ocean','古代大水体名称 → 大洋、海洋'],['ocean + -s → oceans','多个大洋；比喻大量']],
 'the world’s oceans 世界各大洋；oceans and seas 大洋与海；oceans of time 大把时间〔夸张说法〕。',
 'life in the oceans；oceans of space。','ocean 常说大洋，sea 可说海或海洋的一部分，日常也有重合。oceans of time 是数量夸张，理解为很多时间即可。',
 ('The exhibition explores life in the world’s oceans.','展览介绍了世界各大洋中的生命。'),('The map shows the continents and oceans.','地图标出了各大洲和各大洋。'),sources=['https://en.wiktionary.org/wiki/oceans#English','https://en.wiktionary.org/wiki/ocean#English'])
W('waves','/weɪvz/','水波、波浪；物理波；一波波事件；挥手、摆动〔第三人称单数〕',
 '水面一上一下起伏，是 waves；手来回摆动，就是动词 waves；声音、光的物理波或一批批涌来的事，也借波的概念表达。',
 'wave + -s，/v/ 后读 /z/。摆动动词接古英语 wafian；水波名词承中古英语 wawe 等旧形，现代拼写受动词影响靠拢。两路直接祖先不同，用起伏联系意思，不压成一条单线。',
 [['古英语 wafian → wave 动词；中古英语 wawe 等 → wave 名词','摆动；水波，后词形互相影响'],['wave + -s → waves','多道波浪、多种波；单数主语挥手']],
 'ocean waves 海浪；sound waves 声波；waves of visitors 一波波访客；waves goodbye 挥手告别。',
 'waves breaking on the beach；waves to a friend。','wave to someone 是朝某人挥手；wave something 是挥动某物。waves of something 常把一批批到来的感觉比作水浪，具体说访客、情绪还是热量要看对象。',
 ('Small waves broke against the beach.','小浪拍打着海滩。'),('She waves to the children from the window.','她从窗边向孩子们挥手。'),('Visitors arrived in waves throughout the afternoon.','整个下午，访客一拨接一拨地到来。'),sources=['https://en.wiktionary.org/wiki/waves#English','https://en.wiktionary.org/wiki/wave#English'])
def extend_lessons():
 extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_ye',ROOTS,WORDS)
 extend_lessons()
