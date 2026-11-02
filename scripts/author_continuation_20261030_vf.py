"""Documents, growing together, keeping, public places and optical forms."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'B3732':dict(words=['chart','charter'],label='纸张材料的不同借词：chart 与 charter',note='charter 经法语接拉丁 chartula 小文书，与 chart 追到 charta 纸、文书同族；正式文书、特许与包租用途逐步发展。'),
 'C0247':dict(words=['coalesce','coalition'],label='co-：长在一起与联合行动',note='coalesce 接拉丁 coalescere，co- 一起与 alescere 生长结合；coalition 经法语接同一词族的不同名词形式。'),
 'C0039':dict(words=['coalesce','coalition'],label='更早 alere 的生长材料：长到一起',note='alescere 接 alere 滋养、成长，和 altus 长高材料同族；coalesce 与 coalition 共享更早生长材料，不能从现代 altitude 直接推成联盟。'),
 'A1771':dict(words=['custody','custodial'],label='custody 到 custodial：看管、照护的性质',note='custody 接拉丁 custodia 看管、保护，custodial 对应 custod- 与性质形容词材料；监护、拘押、楼宇照管的语境分别理解。'),
 'A1770':dict(words=['custody','custodian'],label='custodian：负责照管、保管的人',note='custodian 接 custody 与拉丁 custod- 看管材料及相应人物名词词尾；保管人、校舍管理人员等随对象分化。'),
 'B3599':dict(words=['public','pub'],label='pub：public house 的缩短',note='pub 缩短 public house，较早指向公众开放的场所，后固定为酒馆；不是一切 public building 都叫 pub。'),
 'B3502':dict(words=['arch','arc'],label='arc 与 arch：弓形的两种借入形式',note='arc、建筑 arch 接拉丁 arcus 弓、弧的不同词形路径；表示首要的希腊 arch- 另源，现代读音也不同。'),
 'C1004':dict(words=['paradise'],label='远层同源比较：围园里的伊朗语 pairi-',note='paradise 更早接伊朗语支围起来的园子名称，pairi- 周围与希腊 peri- 有同源关系；这个词经希腊、拉丁、法语进入英语，不是英语直接把 peri- 拼出天堂。'),
 'B3335':dict(words=['bar','barrier'],label='barrier：拦在面前的杆到障碍',note='barrier 经法语 barriere 接 barre 杆、栅栏，与 bar 的门栓、阻隔线同族；不接压力单位 bar 的另一来源。'),
 'A1776':dict(words=['lens','lenses','stair','stairs','staircase','upstairs','downstairs'],label='lens 本身单数；stairs 与 staircase 的区别',note='lens 末尾 s 属于单词本身，复数 lenses 读 /ɪz/；stair 常指一阶，stairs 常指一段楼梯，staircase 再加入围框结构的 case。'),
 'C0168':dict(words=['case','stair','staircase'],label='case 围框容纳的复合词：staircase',note='staircase 是 stair 与 case 围框、容纳结构的英语复合，case 的容器线接拉丁 capsa；stair 本身另来自日耳曼登升词族，不能归为拉丁 capere 的直接借词。'),
}
W('charter','英 /ˈtʃɑːtə/；美 /ˈtʃɑːrtər/','宪章、章程、特许状；特许；包租船、飞机等',
 '先把权利、目标或安排写成正式文书，charter 就有了章程、特许状的意思。专门签约租下一条船、一架飞机，又形成包租的动词用法。',
 '经法语 chartre 接拉丁 chartula 小文书、小纸张，为 charta 纸、文书的小称，与 chart 同族。英语先有正式授权文书，再有授予特许、按专门合约包租等动词义。',
 [['拉丁 charta → chartula → 法语 chartre','纸、文书 → 小文书、正式凭据'],['英语 charter','章程、特许状；授予特许；专约包租']],
 'a charter of rights 权利宪章；an organization’s charter 组织章程；charter a boat 包租一条船；a charter flight 包机航班。',
 'a founding charter；charter a bus。','chart 常是图表、地图，charter 常是正式文书或包租动作。chartered flight 指包机航班，不能只按图表的 chart 来猜。',
 ('The organization’s charter sets out its main aims.','组织章程列出了主要目标。'),('They chartered a boat for the day.','他们包租了一条船，使用一天。'),sources=['https://www.etymonline.com/word/charter','https://en.wiktionary.org/wiki/charter#English'])
W('coalesce','/ˌkəʊəˈles/；美 /ˌkoʊəˈles/','合并、融合；逐渐形成一个整体',
 '几滴水碰到一起，渐渐成一大滴；零散想法凑在一起，渐渐成一个方案。coalesce 看的是几个部分聚成整体。',
 '接拉丁 coalescere，co- 一起与 alescere 生长结合，后者接 alere 滋养、成长。英语继承长在一起、联合成整体的图景。',
 [['拉丁 co- + alescere → coalescere','一起 + 生长 → 长到一起'],['英语 coalesce','部分合为一体；想法、群体渐成整体']],
 'coalesce into a plan 聚成一个方案；coalesce around an idea 围绕一个想法凝聚；droplets coalesce 水滴合并；coalesce with another group 与另一群体融合。',
 'ideas coalesce；coalesce into a single whole。','coalesce 常把多项看成逐渐合成一体，collect 只说收集到一起，不保证各部分已经融合。',
 ('The droplets coalesced into a larger drop.','小水滴合并成了一大滴。'),('Their separate ideas slowly coalesced into a clear plan.','他们各自的想法慢慢融合成一份清楚的方案。'),sources=['https://www.etymonline.com/word/coalition','https://en.wiktionary.org/wiki/coalesce#English'])
W('coalition','英 /ˌkəʊəˈlɪʃən/；美 /ˌkoʊəˈlɪʃən/','联盟、联合；联合行动的团体',
 '原本分开的几方，为一个共同目标站到一起，组成 coalition。它们可以保留各自身份，同时合作做某件事。',
 '经法语 coalition 接拉丁 coalescere 长到一起的相关分词、名词材料，与 coalesce 同族。英语先有部分长合，后常说政党、组织或国家为了目标形成的联盟。',
 [['拉丁 coalescere 与 coalit- 材料','长到一起、联合'],['法语 coalition → 英语 coalition','联合、联盟；为目标合作的群体']],
 'form a coalition 组成联盟；a coalition government 联合政府；a coalition of local groups 当地团体组成的联盟；a broad coalition 广泛联盟。',
 'join a coalition；build a coalition。','coalition 不要求成员完全融成同一个组织，常仍保留各自身份。核心历史材料是一起生长，现代强调为共同目标联合。',
 ('A coalition of local groups organized the cleanup.','当地几个团体组成的联盟组织了清洁活动。'),('The parties agreed to form a coalition government.','各党同意组建联合政府。'),sources=['https://www.etymonline.com/word/coalition','https://en.wiktionary.org/wiki/coalition#English'])
W('custody','英 /ˈkʌstədi/；美 /ˈkʌstədi/','保管、看护；监护；拘押、羁押',
 '某个人或东西交到一方手里，由这一方看管、负责。对象是文物，可以是保管；对象是孩子，常谈监护照护；警方控制住人，则有拘押义。',
 '接拉丁 custodia 看管、保护，也可指监禁，来自 custos、词干 custod- 看管者、保护者。英语沿看守、保管线发展，具体自由程度由场景决定。',
 [['拉丁 custos／custod- → custodia','看管者 → 看守、保护、拘押'],['英语 custody','保管、照护；监护；警方等的拘押']],
 'in the custody of a museum 由博物馆保管；custody of the children 对孩子的监护、照护安排；in police custody 被警方拘押；take someone into custody 将某人拘押。',
 'safe custody；have custody of something。','custody 的统一线索是由谁看管、负责，不能看到就一律译入狱。manuscripts in the library’s custody 是图书馆保管的手稿。',
 ('The manuscript remains in the custody of the library.','手稿仍由图书馆保管。'),('He was taken into custody after the incident.','事件发生后，他被拘押了。'),sources=['https://www.etymonline.com/word/custody','https://en.wiktionary.org/wiki/custody#English'])
W('custodian','/kʌˈstəʊdiən/；美 /kʌˈstoʊdiən/','保管人、照管者；楼宇、校舍管理员等〔美式常见〕',
 '东西交给某个人照看、维护，这个人是 custodian。照看珍贵文物可以这样称，负责校舍清洁维护的人也可以这样称。',
 '接 custody 及拉丁 custod- 看管者材料与相应人物词尾，发展为承担照管职责的人。美式校舍管理员义由看管建筑、维持日常使用的职责专门化。',
 [['拉丁看管材料；英语 custody','看守、保管、照护'],['人物名词 custodian','负责照管的人；特定场景中楼宇管理员']],
 'the custodian of a collection 藏品保管人；a school custodian 校舍管理员；a custodian of tradition 传统的守护者。',
 'a museum custodian；the building custodian。','custodian 通常强调保管、照护责任，不自动等于拥有者。物品属于谁，用 owner；谁负责照管，用 custodian 等，实际称呼依场景。',
 ('The custodian unlocked the school early in the morning.','校舍管理员清早打开了学校的门。'),('The museum sees itself as a custodian of local history.','博物馆把自己看作当地历史的守护者。'),sources=['https://www.etymonline.com/word/custody','https://en.wiktionary.org/wiki/custodian#English'])
W('custodial','英 /kʌˈstəʊdiəl/；美 /kʌˈstoʊdiəl/','看管、监护的；拘押、监禁的；楼宇照管维护的',
 'custody 是看管这件事，custodial 把看管的性质放到职责、照护安排、刑罚或校舍工作上。',
 '对应 custody 的词干 custod-、custodi- 与形容词 -al，英语、法语已有相应形式。具体义由看管对象展开：人、场所或被拘押者。',
 [['custody／custod- 看管词族','保管、照护、监护、拘押'],['custod-／custodi- + 形容词材料 → custodial','与相应看管职责或状态有关的']],
 'custodial care 看护、照护；custodial duties 管护职责；custodial staff 校舍、楼宇维护清洁人员等；a custodial sentence 监禁刑。',
 'custodial work；custodial responsibility。','custodial staff 在学校语境常是清洁、维护、管理楼宇的人员；不能只因 custody 有拘押义就把所有 custodial 译成监狱的。',
 ('The custodial staff cleaned the classrooms after the event.','活动后，校舍管理清洁人员打扫了教室。'),('The training covers custodial duties in public buildings.','培训涵盖公共建筑的管护职责。'),sources=['https://www.etymonline.com/word/custody','https://en.wiktionary.org/wiki/custodial#English'])
W('pub','/pʌb/','酒馆、英式酒吧',
 '街区里可以坐下来吃点东西、喝饮品、和熟人见面的酒馆，是 pub 的常见生活画面。',
 '由 public house 缩短，public 指向公众开放。这个短语较早可泛指开放的建筑，后来用于提供食宿、酒食的场所，再固定到酒馆；pub 是较后的口语缩短。',
 [['public house','向公众开放的场所 → 旅店、酒馆等'],['缩短 pub','日常常用的酒馆名称']],
 'meet at the pub 在酒馆见面；a local pub 社区酒馆；pub food 酒馆餐食；a pub garden 酒馆花园。',
 'a village pub；a traditional pub。','pub 与 bar 有重叠，pub 在英式生活中常带社区酒馆的感觉；bar 也可指店里的吧台。pub 这个词本身不保证建筑一定古老。',
 ('We met for lunch at the village pub.','我们在村里的酒馆碰面吃午饭。'),('The pub has a small garden at the back.','酒馆后面有一个小花园。'),sources=['https://www.etymonline.com/word/pub','https://en.wiktionary.org/wiki/pub#English'])
W('arc','英 /ɑːk/；美 /ɑːrk/','弧、弧线；电弧；故事发展线；沿弧线移动',
 '把弓的弯曲形状想出来：球划过天空的路线、圆周上的一段，都可以看成 arc；故事从起点走向变化、收束，也有 story arc。',
 '经法语 arc 接拉丁 arcus 弓、弧。几何、天体路径、电弧和叙事发展等后来借用了弯曲路径的画面；与建筑 arch 的弓形来源同族。',
 [['拉丁 arcus → 法语 arc','弓；弯曲形状'],['英语 arc','弧线、圆弧；电弧；比喻的发展轨迹']],
 'an arc of a circle 一段圆弧；move in an arc 沿弧线移动；an electric arc 电弧；a story arc 故事发展线；a character arc 人物变化轨迹。',
 'a wide arc；arc across the sky。','arc 常以 /k/ 收尾，arch 建筑拱常以 /tʃ/ 收尾。几何圆弧与日常弧形路径的精确范围不同，读专业定义时按该语境看。',
 ('The ball travelled in a high arc.','球沿着一条高高的弧线飞了出去。'),('The final episode completes the character’s story arc.','最后一集完成了这个人物的故事发展线。'),sources=['https://www.etymonline.com/word/arc','https://en.wiktionary.org/wiki/arc#English'])
W('paradise','/ˈpærədaɪs/','天堂、乐园；极其美好舒适的地方或状态',
 '老画面是一座围起来、精心照料的园子。后来它成为宗教中的乐园名称，也可把现实中舒服、美好的地方比作 paradise。',
 '经古法语 paradis、拉丁 paradisus、希腊 paradeisos，较早借伊朗语支围园名称，可与阿维斯陀语 pairidaeza 比较。pairi- 周围与建墙、围合材料结合，前部与希腊 peri- 同源。',
 [['较早伊朗语支围园词 → 希腊 paradeisos','围起来的园子、园林'],['拉丁 paradisus → 古法语 paradis → 英语 paradise','宗教乐园名称；美好地方、幸福状态的比喻']],
 'a tropical paradise 热带乐园；a paradise for walkers 徒步者的乐园；the Garden of Paradise 宗教乐园语境；feel like paradise 感到像在乐园。',
 'a birdwatcher’s paradise；a little paradise。','paradise 既有宗教义，也广泛作日常比喻。a paradise for readers 表示对读者特别理想，不要求说话者作宗教主张。',
 ('The quiet valley was a paradise for walkers.','宁静的山谷是徒步者的乐园。'),('After weeks of noise, the garden felt like paradise.','经历几周的嘈杂后，那座花园让人觉得像乐园一样。'),sources=['https://www.etymonline.com/word/paradise','https://en.wiktionary.org/wiki/paradise#English'])
W('barrier','英 /ˈbæriə/；美 /ˈbæriər/','障碍物、屏障；阻碍、隔阂',
 '前面横着一根栏杆，过不去，是 barrier；语言、费用、信任问题也能横在两方之间，形成看不见的障碍。',
 '经法语 barriere 接 barre 杆、栅栏、门栓，与 bar 的阻隔线同族。更远来源不定，英语由入口障碍扩展到各种阻碍与保护性屏障。',
 [['法语 barre → barriere','杆、栅栏 → 阻拦入口的设施'],['英语 barrier','障碍物、屏障；抽象阻碍、隔阂']],
 'a safety barrier 防护栏；a language barrier 语言障碍；a barrier to entry 进入障碍；remove barriers 消除障碍；a barrier against noise 隔音屏障。',
 'break down barriers；a physical barrier。','barrier 可以挡住坏东西而起保护作用，也可阻碍想完成的事。barrier to communication 是沟通障碍，barrier against the wind 则是挡风屏障。',
 ('The barrier at the car park entrance lifted slowly.','停车场入口的栏杆慢慢抬起。'),('Language can be a barrier to finding work.','语言可能成为求职的障碍。'),sources=['https://www.etymonline.com/word/barrier','https://en.wiktionary.org/wiki/barrier#English'])
W('lens','/lenz/','透镜、镜片；镜头；晶状体；观察视角〔比喻〕',
 '一片能改变光线路径的透明材料，帮助聚焦、看清或成像，是 lens。把同一件事换个观察角度，也能说换了一副 lens。',
 '借拉丁 lens、词干 lent-，原义扁豆，以早期双凸透镜像扁豆的形状命名。后来有眼睛晶状体、相机镜头与抽象观察视角等义；名称的老形状不限制所有现代镜片形状。',
 [['拉丁 lens 扁豆 → 光学 lens','由双凸形状联想命名透镜'],['英语用途与比喻扩展','镜片、镜头、晶状体；观察角度']],
 'a camera lens 相机镜头；a contact lens 隐形眼镜镜片；the lens of the eye 眼睛晶状体；through the lens of history 从历史视角看。',
 'a wide-angle lens；a lens cap。','lens 的 s 是单词本身的一部分，一枚用 a lens；多枚用 lenses。len 不是这个词的普通单数形式。',
 ('She cleaned the camera lens with a soft cloth.','她用软布擦拭了相机镜头。'),('The diagram shows how a lens focuses light.','示意图展示了透镜怎样聚焦光线。'),('She examines the story through the lens of family history.','她从家族历史的视角审视这个故事。'),sources=['https://www.etymonline.com/word/lens','https://en.wiktionary.org/wiki/lens#English'])
W('lenses','/ˈlenzɪz/','透镜、镜片、镜头等〔lens 复数〕；也可为动词形式',
 '不止一枚 lens，就有 lenses。相机包里几支不同镜头，或一副眼镜里的两片镜片，都能这样数。',
 'lens 加 -es，词干末音 /z/ 后复数词尾读 /ɪz/。借词 lens 原本就以 s 结尾，英语复数是在完整单词上再加相应词尾。',
 [['lens','一枚透镜、镜片或一支镜头等'],['lens + -es → lenses','完整单词后加复数；末尾 /zɪz/']],
 'camera lenses 相机镜头；contact lenses 隐形眼镜；two lenses 两枚镜片或两支镜头；different lenses 不同镜头或不同观察视角。',
 'change lenses；a pair of lenses。','a pair of lenses 通常数两片；a pair of glasses 数一副眼镜。两者都能说眼镜相关东西，但所数单位不同。',
 ('The photographer carried three lenses.','摄影师带了三支镜头。'),('The glasses need new lenses.','这副眼镜需要换新镜片。'),sources=['https://en.wiktionary.org/wiki/lenses#English','https://www.etymonline.com/word/lens'])
W('stair','英 /steə/；美 /ster/','一阶楼梯、一级台阶；较早也可统称楼梯',
 '脚往上抬，踏到一级新的高度，那一级可以叫 a stair。说整段楼梯，日常更常用 stairs。',
 '接古英语 stæger 楼梯名称，较早属于向上走、攀升的日耳曼语材料。旧词也可指一组楼梯，后来普通复数 stairs 与单阶 stair 的分工逐渐形成。',
 [['古英语 stæger → 中古英语 steir','登升结构、楼梯等'],['现代 stair 与 stairs 的分工','一阶；多阶、整段楼梯']],
 'the bottom stair 最下面一级；the top stair 最上面一级；sit on a stair 坐在一级台阶上；a broken stair 损坏的一级台阶。',
 'one stair at a time；the first stair。','a stair 通常在数一级，不是一整层楼。普通说从楼梯上去，用 go up the stairs；说第几层用 floor 等另外的单位词。',
 ('She sat on the bottom stair to tie her shoes.','她坐在最下面一级台阶上系鞋带。'),('One of the wooden stairs creaked under his foot.','一阶木台阶在他脚下吱呀作响。'),sources=['https://www.etymonline.com/word/stair','https://en.wiktionary.org/wiki/stair#English'])
W('stairs','英 /steəz/；美 /sterz/','楼梯、阶梯；stair 的复数',
 '一阶接一阶，连成让人上下楼的路，普通说 the stairs。这里多数时候在看整段台阶。',
 'stair + -s，尾音读 /z/。旧词已有集合结构的用法，英语后来让 stairs 成为说一组楼梯的常见复数；upstairs、downstairs 又把方向与这组材料结合。',
 [['stair 的台阶、楼梯材料','一阶及较早集合用法'],['stair + -s → stairs','普通复数；常说整段楼梯']],
 'go up the stairs 上楼梯；take the stairs 走楼梯；a flight of stairs 一段楼梯；at the top of the stairs 楼梯顶部。',
 'walk down the stairs；the stairs are steep。','stairs 通常接复数动词：The stairs are steep。a flight of stairs 数一段；the staircase 更常把楼梯连同结构看作一个整体。',
 ('We took the stairs instead of the lift.','我们走了楼梯，没有坐电梯。'),('The stairs are narrow and steep.','楼梯又窄又陡。'),sources=['https://www.etymonline.com/word/stair','https://en.wiktionary.org/wiki/stairs#English'])
W('staircase','英 /ˈsteəkeɪs/；美 /ˈsterkeɪs/','楼梯、楼梯结构整体',
 '不只数脚下几阶，还看整套台阶、支撑和围合安排。把它当建筑里的一个整体构造，就是 a staircase。',
 'stair 台阶 + case 围框、容纳结构，英语复合词；这里 case 的容器线更早经法语接拉丁 capsa 箱、容器。stair 自身来自日耳曼语，两个部分各有来源。',
 [['stair + case','台阶 + 围框、容纳的结构'],['英语 staircase','由台阶等组成的一套楼梯结构']],
 'a spiral staircase 螺旋楼梯；a wooden staircase 木楼梯；a narrow staircase 狭窄楼梯；the main staircase 主楼梯。',
 'a winding staircase；a grand staircase。','stairs 常把一组台阶作为复数说，staircase 可数一套整体：The stairs are steep；The staircase is steep。case 在这里是围框结构，不是事件、病例的另一源词义。',
 ('A spiral staircase leads to the roof.','一道螺旋楼梯通向屋顶。'),('The house has a broad wooden staircase.','房子里有一道宽木楼梯。'),sources=['https://en.wiktionary.org/wiki/staircase#English','https://www.etymonline.com/word/stair'])
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_vf',ROOTS,WORDS)
 extend_lessons()
