"""Ton, brick, candy, curse and bloodied."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
T=[['tun 大桶；古法语 tonne 等相关形式','从装货、装酒的桶，到桶所容纳的量'],['ton 与 tonne 的计量分工','ton 有多种吨制；tonne 明确说公吨'],['数额、规模与单位扩展','tonnage 吨位、吨数；megaton 百万吨、百万吨当量']]
W('ton','/tʌn/','吨〔不同吨制〕；大量〔口语〕',
 '历史先有大桶，再拿装一桶的量计东西，后来形成吨的单位。今天 a ton 有多大，必须看它用哪种吨制。',
 '与 tun 大桶同源的词形，受法语 tonne 等影响，重量、容量义逐渐固定为 ton。时髦社会的旧同形词借法语 ton，是另一来源。',T[:2],
 '美制 short ton 为 2000 磅，约907千克；英制 long ton 为2240磅，约1016千克；metric ton 为1000千克。tons of work 口语说大量工作。',
 'a metric ton；a short ton；tons of work。',
 'ton 不总等于1000千克；tonne 明确指1000千克。tons of homework 是夸张数量，不是在给作业称重。',
 ('The shipment weighs two metric tons.','这批货重两公吨。'),('I still have tons of work to do.','我还有一大堆工作要做。'),sources=['https://en.wiktionary.org/wiki/ton#English','https://www.etymonline.com/word/ton'])
W('tonne','/tʌn/','公吨，1000千克',
 '需要避开英吨、美吨的歧义时，tonne 清楚指1000千克。虽然多了 ne，常用读音仍和 ton 一样。',
 '借法语 tonne，与 ton、tun 有共同历史。在现代英语计量中固定用于公吨。',T[:2]+[['法语 tonne → 英语 tonne','明确表示公吨']],
 'one tonne of grain 一公吨谷物，tonnes of cargo 若干公吨货物。美式也常写 metric ton。',
 'one tonne；tonnes of grain。',
 'tonne 与 ton 的常用发音相同，含义精度不同；写技术数据时要看原文单位。',
 ('The machine weighs just over a tonne.','机器重一公吨多一点。'),('The report gives all masses in tonnes.','报告所有质量都以公吨表示。'))
W('tonnage','/ˈtʌnɪdʒ/','吨数、吨位；货运量等按吨衡量的数量',
 '把某种总量按相应规则计算，可以谈 tonnage。船舶语境尤其要先看指标：有的谈载重，有的由空间容积计算，不能都当船重。',
 '借法语 tonnage，现代可联系 tonne／ton + -age。相关名词用于吨数、船舶容量和其他按吨计量的总量。',T[:2]+[['tonnage','吨数、船舶吨位、货运等总量名称']],
 'cargo tonnage 货运吨数，gross tonnage 总吨位，deadweight tonnage 载重吨位。不同限定词决定衡量对象。',
 'cargo tonnage；gross tonnage；deadweight tonnage。',
 'gross tonnage 按船舶封闭空间容积等计算，不等于以千克直接量出的质量。不能只看中文都有吨位就当同一个数。',
 ('The port recorded a rise in cargo tonnage.','港口记录的货运吨数有所上升。'),('The chart lists the gross tonnage of each ship.','图表列出每艘船的总吨位。'),sources=['https://en.wiktionary.org/wiki/tonnage#English','https://www.imo.org/en/About/Conventions/Pages/International-Convention-on-Tonnage-Measurement-of-Ships.aspx'])
W('megaton','/ˈmeɡətʌn/','百万吨；百万吨TNT当量〔能量单位〕',
 'mega- 作数量前缀说百万，因此质量语境是百万吨。爆炸能量语境则用相当于百万吨TNT释放的能量来作比较。',
 'mega- 百万 + ton。由吨数的数量组合，形成质量单位及TNT当量的能量计量用法。',T[:2]+[['mega- + ton → megaton','百万吨；TNT当量语境的能量单位']],
 'emissions in megatons 以百万吨计的排放量，a megaton of TNT equivalent 百万吨TNT当量。质量语境仍需确认吨制。',
 'megatons of material；TNT equivalent in megatons。',
 '百万吨当量是能量的比较，不表示物体本身重百万吨。megaton 与 megawatt 衡量的物理量也不同。',
 ('The table reports annual emissions in megatons.','表格以百万吨报告年度排放量。'),('The energy was expressed in megatons of TNT equivalent.','能量以百万吨TNT当量表示。'))
R('B3474','从大桶、装载量走向不同吨制与总量、当量','TON：单位有历史，也有必须区分的吨制','ton、tonne → tonnage；mega- + ton → megaton。',
 '最有用的不是背一个吨字，而是确认单位和对象：公吨、长吨、短吨；质量、船舶容量、能量又不同。',
 'tun 大桶与 tonne 等相关 → ton；tonne 公吨；-age 总量等名词；mega- 百万。',
 [['吨与公吨','ton · tonne'],['总量与百万单位','tonnage · megaton']],
 'ton 不保证1000千克；船舶总吨位不等于船重；百万吨当量是能量比较。',
 'The cargo weighs one tonne, but the ship’s tonnage is measured separately.\n\n货物重一公吨，但船的吨位另行计量。','ton tonne tonnage megaton')
B=[['中古荷兰语、低地德语 bricke 等 → 中古英语 brik → brick','砖、瓦等，通常联系破裂、碎块的旧词族'],['建筑物件与工程','brickwork、bricklaying、brickworks'],['像无功能砖块的比喻','brick a device → bricked 设备变砖']]
W('brick','/brɪk/','砖、砖块；用砖砌；使电子设备变砖〔口语〕',
 '一块块砖能砌墙；电子设备若无法正常启动、使用，像只剩一块硬块，口语就说被 bricked、变砖。',
 '经中古英语 brik 等，借中古荷兰语、低地德语 bricke 相关形式，通常联系 break 的旧词族。现代变砖义来自砖块物件的比喻。',B,
 'a brick wall 砖墙，build in brick 用砖建造，brick up a doorway 用砖封门，brick a phone 使手机变砖。',
 'a brick wall；brick up a doorway；brick a device。',
 'a brick 是一块砖，brick 作材料名词可不数。设备变砖表示严重失去功能，通常比普通软件卡一下更重。',
 ('The house was built of red brick.','房子用红砖建成。'),('The failed update bricked the old device.','更新失败使旧设备变砖。'))
W('bricked','/brɪkt/','变砖、严重无法使用的〔电子设备〕',
 '屏幕不亮、正常功能起不来，设备仿佛只剩一个硬块；bricked 是技术口语里描述这种严重故障状态的词。',
 'brick 使设备变砖 + -ed，尾音 /t/，不另加一个音节。由过去分词作状态形容词。',B[:1]+B[2:]+[['brick + -ed → bricked','已经严重失去功能的设备状态']],
 'a bricked phone 变砖手机，a bricked router 变砖路由器。具体能否恢复还取决于故障，不宜把口语一律当永久报废判定。',
 'a bricked phone；a bricked router。',
 'bricked 比 frozen 卡住通常更严重；关掉某个应用不一定足以恢复。这里只描述状态，不预设故障原因。',
 ('The technician examined the bricked router.','技术人员检查了变砖的路由器。'),('The forum post describes how the phone became bricked.','论坛帖子描述了手机如何变砖。'))
W('brickwork','英 /ˈbrɪkwɜːk/；美 /ˈbrɪkwɜːrk/','砖砌结构、砖工；砌砖工艺',
 '看墙上一层层砖的排列、接缝、结构，可以说 brickwork。它说砌出来的部分，也可评价砌得好不好。',
 'brick + work。work 取做出的工程、结构与工艺义，不只是一份工作。',B[:2]+[['brick + work → brickwork','砖砌结构、相应工艺']],
 'exposed brickwork 外露砖结构，damaged brickwork 受损砖砌部分，fine brickwork 精细砖工。通常不可数。',
 'exposed brickwork；repair the brickwork。',
 'brickwork 是砌成的结构或工艺，bricklaying 强调砌砖活动，brickworks 则是制砖厂。',
 ('The renovation revealed the original brickwork.','翻修露出了原来的砖砌结构。'),('The wall has beautifully detailed brickwork.','这面墙的砖工细节很精美。'))
W('bricklaying','/ˈbrɪkleɪɪŋ/','砌砖、砌砖手艺',
 '砖一块块放好，按结构砌起来，这个活动、手艺是 bricklaying。lay 在这里是铺放。',
 'brick + laying，lay 的 -ing 形式保留 y。对应从事者 bricklayer。',B[:2]+[['brick + laying → bricklaying','把砖按结构铺砌的工作、手艺']],
 'learn bricklaying 学砌砖，a bricklaying course 砌砖课程，bricklaying skills 砌砖技术。',
 'learn bricklaying；a bricklaying course。',
 'bricklaying 是手艺、活动；bricklayer 是工人；laying 与 lying 躺着、说谎的形式不要混。',
 ('She learned bricklaying at a vocational college.','她在职业院校学了砌砖。'),('The course combines drawing with practical bricklaying.','课程结合绘图与砌砖实践。'))
W('brickworks','英 /ˈbrɪkwɜːks/；美 /ˈbrɪkwɜːrks/','制砖厂、砖场',
 '砖要先生产出来，再运去建筑现场；生产砖的工厂叫 brickworks。这里 works 是工厂、制造场所。',
 'brick + works，后半用工业生产场所义。形式带 s，仍可以说 a brickworks。',B[:2]+[['brick + works → brickworks','制造砖的工厂']],
 'an old brickworks 旧砖厂，a former brickworks 原制砖厂。',
 'an old brickworks；a former brickworks。',
 'brickworks 有 s，说制砖厂；brickwork 通常不可数，说砖砌结构、工艺。少一个 s，所指就不同。',
 ('The old brickworks closed many years ago.','旧砖厂多年前就关闭了。'),('The park occupies the site of a former brickworks.','公园建在原来一座砖厂的旧址上。'))
R('B2952','砖块、砖工与生产，另有设备变砖的比喻','BRICK：建筑中的硬块，也可比喻只剩硬件外壳的设备','brick → bricked；bricklaying、bricklayer 看工作与人；brickwork、brickworks、brickyard 分清结构和场所。',
 '砖词组最容易混的是 work、works：前者常说砌好的砖工，后者是生产砖的工厂。',
 'bricke 等 → brick；-ed 状态；lay 铺放，layer 砌的人，work 工程，works 工厂，yard 场地。',
 [['材料与设备状态','brick · bricked'],['施工、工人和结构','bricklaying · bricklayer · brickwork'],['生产场地','brickworks · brickyard']],
 'brickwork 与 brickworks 所指不同；设备 bricked 不必一律永久不可恢复。',
 'The bricklayer studied the old brickwork before beginning the repair.\n\n泥瓦工开始修补前，先查看了旧砖砌结构。','brick bricked bricklaying bricklayer brickwork brickworks brickyard')
C=[['波斯语 qand 等糖词；更早来源有讨论','与南亚的糖块、结晶糖词可能有关'],['阿拉伯 qandī → 法语 sucre candi → 中古英语 sugre candy','结晶糖、糖块'],['candy 的范围扩大与动词用法','糖果；用糖处理、形成糖衣 → candied']]
W('candy','/ˈkændi/','糖果；用糖腌制、裹糖',
 '先是糖块、结晶糖，后来尤其在美式英语里扩大成糖果统称。作动词则是在食物上用糖、糖浆处理。',
 '中古英语 sugre candy，经法语 sucre candi，上接阿拉伯语、波斯语糖词。更早与梵语 khaṇḍa 糖块等或达罗毗荼语言的联系有讨论，不把远源定成唯一结论。',C,
 'a piece of candy 一颗糖，a candy store 糖果店，hard candy 硬糖。美式常用 candy 统称，英式常说 sweets。',
 'a piece of candy；a candy store；hard candy。',
 'candy 作泛称时常不可数，也可在一些语境数 candies、不同糖果。不能因为末尾 -y 就说这里是英语性质后缀。',
 ('She put a piece of candy in the gift bag.','她在礼袋里放了一颗糖。'),('The shop sells fruit candy and chocolate.','店里卖水果糖和巧克力。'),sources=['https://en.wiktionary.org/wiki/candy#English','https://www.etymonline.com/word/candy'])
W('candied','/ˈkændid/','糖渍的、裹糖的',
 '橙皮、姜等用糖浆处理，保留下糖分或包上糖衣，做成 candied peel、candied ginger。',
 'candy 作动词 + -ed，y 变 i。过去分词再形容经过糖处理的食物。',C+[ ['candy + -ed → candied','经过糖渍、裹糖处理的状态']],
 'candied fruit 糖渍水果，candied orange peel 糖渍橙皮，candied nuts 裹糖坚果。',
 'candied fruit；candied ginger；candied nuts。',
 'candied 说明用糖处理过，sweet 只说甜等性质。水果天然很甜，不因此自动叫 candied。',
 ('The cake contains candied orange peel.','蛋糕里有糖渍橙皮。'),('She decorated the dessert with candied nuts.','她用裹糖坚果装饰甜点。'))
R('B4108','从结晶糖到糖果，再到糖渍、裹糖的处理','CANDY：糖块、糖果，也可把食物用糖处理','candy → candied。',
 '这组把借词路径和现代动词分开：末尾 y 原来就是借入词的一部分，变成 candied 才涉及英语词尾变化。',
 'qand 等糖词 → qandī → sucre candi → candy；动词 + -ed，y 变 i。',
 [['糖果与糖处理的状态','candy · candied']],
 'candy 与 sweets 有地区用法差别；candied 不等于天然有甜味。',
 'The candy shop sells candied fruit as well as chocolate.\n\n糖果店除了巧克力，也卖糖渍水果。','candy candied')
U=[['古英语 curs、cors；远源不明','诅咒、咒骂'],['curse 的比喻和日常表达','带来苦难之物；说脏话、咒骂'],['cursed、cursing','被诅咒、可恶或怪异的；咒骂这一活动']]
W('curse','英 /kɜːs/；美 /kɜːrs/','诅咒；咒骂、说脏话；祸害、灾祸之源',
 '故事里希望坏事降到别人身上的话是 curse；日常里骂一句脏话也可用 curse。某种长期折磨人的问题，又可比作祸害。',
 '承古英语 curs、cors 及相应动词，中古英语继续使用；更早来源不明。超自然叙事、咒骂和苦难比喻逐渐形成常见用法。',U[:2],
 'put a curse on 对……下诅咒，lift a curse 解除诅咒，curse under your breath 低声咒骂，a blessing and a curse 既是福也是祸。',
 'put a curse on；curse under your breath；a blessing and a curse。',
 'curse 可涉及故事里的诅咒，也可只是说脏话。swear 还另有发誓的常用义，不能每次与 curse 对换。',
 ('In the story, the village lives under a curse.','故事里，村庄笼罩在诅咒下。'),('He cursed under his breath when the key broke.','钥匙断了，他低声骂了一句。'))
W('cursed','英 /kɜːst/ 或 /ˈkɜːsɪd/；美 /kɜːrst/ 或 /ˈkɜːrsɪd/','被诅咒的；可恶的；怪异、令人不安的〔网络等语境〕',
 '故事里的宝物受了诅咒，是 cursed；抱怨某个破机器可说 this cursed machine。网络里 cursed image 则常说怪得让人不舒服、又有点好笑的图。',
 'curse + -ed，中古英语已有相应形式。过去分词常读单音节 /kɜːst/ 等，形容词也有两音节读法；具体语气随语境变化。',U+[ ['curse + -ed → cursed','被诅咒；可恶、怪异等状态评价']],
 'a cursed object 被诅咒的物件，a cursed image 怪异图像，this cursed machine 这该死的机器〔抱怨语气〕。',
 'a cursed object；a cursed image。',
 '两个读法不是绝对按一个词义切开；文学、语气和说话习惯会影响读法。网络 cursed 也不等于真在声称存在诅咒。',
 ('The tale begins with a cursed ring.','故事从一枚被诅咒的戒指开始。'),('I cannot get this cursed printer to work.','这该死的打印机，我怎么都弄不动。'),sources=['https://en.wiktionary.org/wiki/cursed#English','https://www.merriam-webster.com/dictionary/cursed'])
W('cursing','英 /ˈkɜːsɪŋ/；美 /ˈkɜːrsɪŋ/','咒骂、说脏话；诅咒的行为',
 'curse 是动作，cursing 可以把咒骂这件事整体拿出来说，或表示动作正在发生。',
 '现代对应 curse + -ing，去 e；古英语已有 cursung、中古英语已有 cursing 等行为名词。不是直到现代才第一次产生这个名词。',U[:1]+[['cursung → cursing；现代对应 curse + -ing','咒骂、诅咒的活动']],
 'no cursing 禁止骂脏话，a burst of cursing 一阵咒骂，stop cursing 停止咒骂。',
 'no cursing；a burst of cursing；stop cursing。',
 'cursing 说行为，curse 既能说一次骂话，也能说诅咒、祸害。需要看句中词性。',
 ('The coach told the players to stop cursing.','教练叫球员停止骂脏话。'),('A burst of cursing came from the locked room.','锁着的房间里传来一阵咒骂。'))
R('B3292','诅咒、咒骂与祸害比喻，再有抱怨和怪异评价','CURSE：说出恶意、坏话，或比喻长期折磨','curse → cursed、cursing。',
 '现实咒骂、故事里的诅咒、网上怪图是不同使用场景。按场景理解，比把每句都当魔法更实用。',
 'curs／cors → curse；-ed 状态或分词，-ing 行为、分词；远源不明。',
 [['基础与状态、行为','curse · cursed · cursing']],
 'cursed 常有两种读法；curse 与 swear 只在部分用法重叠；网络 cursed 常是语气。',
 'He stopped cursing and began reading the tale of the cursed ring.\n\n他停止咒骂，开始读那枚受诅咒戒指的故事。','curse cursed cursing')
V=[['blood 血 → bloody 的动词用法','使沾血、使受伤出血'],['bloody + -ed → bloodied','沾了血；比喻受挫、受到打击']]
W('bloodied','/ˈblʌdid/','沾血、染血的；受挫、受到打击的',
 '脸、衣服等沾了血，可以 bloodied；比喻里经历冲突、失败而受损，也能用这个带有战斗痕迹的形象。',
 'bloody 作动词使沾血、使出血 + -ed，y 变 i。bloodied 是分词及状态形容词，不是 bloody 作强调词时再加一个程度后缀。',V,
 'a bloodied face 沾血的脸，bloodied but unbowed 受挫却不屈服。后一搭配常用于坚强回应失败的描述。',
 'a bloodied face；bloodied but unbowed。',
 'bloody 可以是带血的，也可作英式口语强调词；bloodied 常保留染血、受创这一动作后的状态。',
 ('The boxer wiped his bloodied face with a towel.','拳击手用毛巾擦了擦沾血的脸。'),('The team left bloodied but unbowed after the defeat.','败局后，球队受了挫折，却没有低头。'))
R('B3650','带血、使沾血，与强调语气分清','BLOODY：血的性质、动作和口语强调各有用法','bloody → 动词分词 bloodied。',
 '带血的外观、使出血的动作、英式口语强调，不能用同一个中文词替换。bloodied 主要看动作之后的受创状态。',
 'blood + -y → bloody；动词 + -ed，y 变 i → bloodied。',
 [['性质与动作后的状态','bloody · bloodied']],
 'bloodied 不是 bloody 强调语气的过去时；bloodied but unbowed 可比喻受挫却不屈。',
 'His shirt was bloody, and his face was bloodied by the fall.\n\n他的衬衫沾着血，脸也在摔倒时受伤染血。','bloody bloodied')
if __name__=='__main__':save('continuation_20261030_kj',ROOTS,WORDS)
