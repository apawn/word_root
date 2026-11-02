"""Mud, spray and bulk."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
M=[['中古荷兰语、低地德语 modde 等可能借词 → 中古英语 mudde → mud','水和土等混成的泥'],['泥的颜色、混浊、难辨形象','muddy 泥泞、浑浊；把事情搅浑'],['mud + stone → mudstone','泥质沉积物成岩 → 泥岩']]
W('mud','/mʌd/','泥、泥浆；抹黑言辞〔比喻〕',
 '土、细颗粒沉积物混了水，黏黏湿湿的是 mud。拿泥往别人身上抹的形象，再变成以恶意话语损害名声。',
 '中古英语 mudde、mud 等，通常认为可能借自低地德语、荷兰语相关泥词，更早来源有不同分析。现代湿泥、建筑材料和抹黑比喻分别发展。',M[:2],
 'boots covered in mud 沾满泥的靴子，thick mud 厚泥，throw mud at someone 抹黑某人，drag someone’s name through the mud 糟蹋某人的名声。',
 'covered in mud；thick mud；drag a name through the mud。',
 'mud 是湿泥，dust 常说干尘；soil 更广泛地说土壤。比喻里的 mud 不是在交代对方真沾了泥。',
 ('The boots were covered in mud.','靴子上沾满了泥。'),('The wheels sank into the soft mud.','车轮陷进软泥里。'))
W('muddy','/ˈmʌdi/','泥泞、沾泥的；浑浊、混杂不清的；使浑浊、搅乱',
 '路混着泥，水里搅起泥，都 muddy；颜色、声音、解释失去清楚边界，也可借浑浊的画面形容。',
 'mud + -y，双写 d；中古英语已有相应性质词，动词再由形容词发展。',M[:2]+[['mud + -y → muddy','有泥、浑浊 → 不清楚；使变得混浊']],
 'muddy boots 沾泥靴子，muddy water 浑水，muddy colors 发浑颜色，muddy the waters 把问题搅浑、弄复杂。',
 'muddy boots；muddy water；muddy the waters。',
 'muddy water 重点是浑浊含泥，muddy explanation 比喻解释不清。作动词时可以不涉及真的加泥。',
 ('The path was muddy after the rain.','雨后小路泥泞。'),('His extra comments only muddied the waters.','他多加的评论只把事情搅得更乱。'))
W('mudstone','英 /ˈmʌdstəʊn/；美 /ˈmʌdstoʊn/','泥岩',
 '细小泥质沉积物经过成岩，变成了岩石，就可以叫 mudstone。名字把原来的泥和已经成岩这两层连起来。',
 'mud 泥质沉积物 + stone 岩石，按主要沉积物及成岩后的物质状态组成名称。',M[:1]+[M[2]],
 'a layer of mudstone 一层泥岩，mudstone samples 泥岩样本，a mudstone cliff 泥岩崖。颜色、硬度等随具体岩石变化。',
 'a layer of mudstone；mudstone samples。',
 'mudstone 已是岩石，mud 是松散湿泥。不能因为名称含 mud，就以为碰到水会立即成为泥浆。',
 ('A thin layer of mudstone lies above the sandstone.','砂岩上方有一薄层泥岩。'),('The geologist collected mudstone samples from the cliff.','地质学家从崖壁采集泥岩样本。'))
R('B4154','湿泥与混浊的形象，再到由泥质沉积成岩的名称','MUD：泥混在水里，既能看质地也能看清晰程度','mud → muddy；mudstone 是泥质沉积成岩；mudslide 接泥土滑动。',
 '湿泥、浑浊、把问题搅浑，联想很直观。泥岩则要多看一步，已经从沉积物变成岩石。',
 'mudde 等 → mud；-y 性质，双写 d；stone 岩石，slide 滑动。',
 [['湿泥与浑浊性质','mud · muddy'],['地质物质与事件','mudstone · mudslide']],
 'mud 与 dust、soil 不完全相同；mudstone 不是松散泥；muddy the waters 是固定比喻。',
 'The muddy path ran beneath a mudstone cliff.\n\n泥泞小路经过一面泥岩崖壁下方。','mud muddy mudstone mudslide')
S=[['中古荷兰语 sprayen 等 → spray 动词','撒散、喷洒液滴'],['动词 → 液滴、喷雾产品等名词','分散的细水滴；喷雾、喷剂'],['另源同形词 spray','小枝、带花小枝；与喷雾线分开']]
W('spray','/spreɪ/','喷、喷洒；飞沫、喷雾、喷剂；带花小枝〔另源〕',
 '液体分成许多细滴向外散开，是 spray；浪打在石头上扬起飞沫，也可叫 spray。a spray of flowers 却是带花枝条，来自另一条词线。',
 '喷洒动词通常借中古荷兰语 sprayen 等，联系散播、撒散词族；液滴名词相关。小枝义在中古英语已有，远源未明，可能联系古英语枝条形式。',S,
 'sea spray 海浪飞沫，a fine spray of water 细水雾，spray water on leaves 往叶子上喷水，spray the leaves with water 用水喷叶子，a spray of flowers 带花的小枝。',
 'sea spray；a fine spray；spray something with water。',
 'spray 液滴分散，pour 倒水更像液流；花枝义不能只按现代喷雾比喻倒推词源。',
 ('Sea spray reached the windows of the boat.','海浪飞沫溅到船窗上。'),('She added a spray of small flowers to the arrangement.','她往插花中添了一小枝花。'),sources=['https://en.wiktionary.org/wiki/spray#English','https://www.etymonline.com/word/spray'])
W('spraying','/ˈspreɪɪŋ/','喷洒、喷涂等活动',
 '液体、涂料等分成细滴施到表面，这个动作过程可以 spraying。对象不同，可译喷洒、喷涂等。',
 'spray + -ing，保留 y。这里的 y 是元音组合 ay 的一部分，不像 tidy 那样在相应派生中换 i。',S[:2]+[['spray + -ing → spraying','喷洒、喷涂的过程']],
 'water spraying 喷水，paint spraying 喷涂，a spraying system 喷洒系统。',
 'paint spraying；a spraying system。',
 'spraying 是活动，sprayer 是执行喷洒的人、设备；spray 可是动作，也可是喷雾物。',
 ('The system provides even spraying across the surface.','系统让液体均匀喷洒在表面。'),('The film shows the spraying of water over the young plants.','影片展示给幼苗喷水的过程。'))
W('sprayer','英 /ˈspreɪə/；美 /ˈspreɪər/','喷雾器、喷洒设备；喷洒者',
 '把水、涂料等喷成细滴的器具，可以叫 sprayer。小喷瓶、大型喷洒设备都能按功能这样命名。',
 'spray + -er，保留 y；-er 指执行喷洒功能的人或设备。',S[:2]+[['spray + -er → sprayer','喷洒的人、器具或设备']],
 'a hand sprayer 手持喷雾器，a garden sprayer 园艺喷雾器，a paint sprayer 喷涂设备。',
 'a hand sprayer；a garden sprayer。',
 'sprayer 是较宽的功能名称，spray bottle 明确是喷瓶；不是所有喷洒设备都做成瓶子。',
 ('She filled the hand sprayer with water.','她给手持喷雾器装了水。'),('The gardener adjusted the sprayer before watering the plants.','园丁给植物喷水前，调整了喷雾器。'))
R('B4603','细滴撒散的动作、喷雾及设备，与花枝同形词分清','SPRAY：把液体分成许多细滴散开','spray → spraying、sprayer；花枝 spray 是另一来源的固定名词。',
 '喷雾从动作到液滴、产品、器具，关系清楚；花枝义只要另记一条，不必编成花是喷出来的。',
 'sprayen 等 → spray；-ing 过程，-er 执行者和器具，均保留 y；小枝义另有中古英语来源。',
 [['动作、细滴与另源花枝','spray'],['过程与设备','spraying · sprayer']],
 'spray 不等于 pour；sprayer 不只喷瓶；a spray of flowers 是花枝。',
 'The sprayer produces a fine spray for gentle watering.\n\n喷雾器产生细水雾，用于轻柔浇水。','spray spraying sprayer')
B=[['古诺尔斯语 búlki 等 → 中古英语 bulk、bolke','船货、堆、体积；与其他躯体词形有交汇'],['bulk 的现代扩展','体积、大部分；成批、散装'],['bulkhead 的前部另看隔断词','通常联系 bálkr 等梁、隔板形式，中间构词有讨论']]
W('bulk','/bʌlk/','体积、大块；大部分；大批量、散装',
 '一堆货看起来占多大地方，是 bulk 的体积感；一件事的大部分是 the bulk of；货物大批、散装处理，则说 in bulk。',
 '中古英语 bulk、bolke 借古诺尔斯语 búlki 船货等，且与其他躯体、隆起词形有交汇。现代规模、主要部分和批量用法分别固定。',B[:2],
 'the bulk of the work 大部分工作，buy in bulk 大批购买，bulk cargo 散货，without adding bulk 不增加厚重体积，bulk up 增大体量、增肌等。',
 'the bulk of；buy in bulk；bulk cargo。',
 'bulk 重点可在体积，不等于 weight 重量。in bulk 随语境可大批量或散装，不能一律当同一种包装方式。',
 ('The bulk of the work is already finished.','大部分工作已经完成。'),('The thick lining adds bulk to the coat.','厚里衬增加了外套的厚重感。'))
W('bulky','/ˈbʌlki/','体积大、占地方的；笨重难搬的',
 '东西很占空间，搬、装、穿时显得不利落，是 bulky。它可以很轻，只是太占地方。',
 'bulk + -y，中古英语已有相应形式。由体积、块头形象形成性质词。',B[:2]+[['bulk + -y → bulky','体积大、占空间，因而难搬或不利落']],
 'a bulky coat 厚重外套，bulky luggage 大件行李，a bulky package 体积大的包裹。',
 'bulky luggage；a bulky coat；a bulky package。',
 'bulky 不保证很重；heavy 强调重量。空纸箱可以 bulky，金属小块却可能 heavy。',
 ('The bulky suitcase would not fit under the seat.','大行李箱塞不进座位下面。'),('The coat is warm without being bulky.','外套很暖，却不显臃肿。'))
W('bulkhead','/ˈbʌlkhed/','舱壁、隔舱板；飞机、车辆等内部隔板',
 '大空间里竖起一面隔板，把船体内部、机舱等分成区域，就是 bulkhead。先抓隔开，而不是大头。',
 'head 与前部隔断、梁类旧词组合，前部通常联系古诺尔斯语 bálkr 等；具体中间形式有讨论。不能简单拿现代 bulk 体积大 + head 头来解释全部历史。',B[2:]+[['隔断相关旧词 + head → bulkhead','船内竖直隔板 → 其他交通工具等内部隔板']],
 'a watertight bulkhead 水密舱壁，a cabin bulkhead 客舱隔板，a bulkhead seat 隔板前的座位。具体隔板不一定都水密。',
 'a watertight bulkhead；a cabin bulkhead。',
 'bulkhead 侧重内部隔断，hull 是船体外壳等。只有加 watertight 等明确说明，才是在说相应水密结构。',
 ('A watertight bulkhead separated the two compartments.','一道水密舱壁把两个舱室隔开。'),('The seat is directly behind the cabin bulkhead.','座位就在客舱隔板后面。'),sources=['https://en.wiktionary.org/wiki/bulkhead#English','https://www.etymonline.com/word/bulkhead'])
R('B3482','体积、货堆与主要部分，再分清隔断来源的 bulkhead','BULK：体量大、主要部分或批量；BULKHEAD 单看隔断历史','bulk → bulky；bulkhead 前部与隔断、梁类旧词相连。',
 '大行李看空间，工作大部分看比例，散货看运输方式。隔板词则不能只套现代大块意思。',
 'búlki 船货等 → bulk；-y 性质；bálkr 等隔断相关形式 + head → bulkhead。',
 [['体积、主要部分与性质','bulk · bulky'],['隔板的相关但不同历史','bulkhead']],
 'bulky 不保证重；in bulk 依语境区分批量、散装；bulkhead 不等于船的整个外壳。',
 'The bulky bags occupied the bulk of the storage space.\n\n这些大包占了储物空间的大部分。','bulk bulky bulkhead')
if __name__=='__main__':save('continuation_20261030_kx',ROOTS,WORDS)
