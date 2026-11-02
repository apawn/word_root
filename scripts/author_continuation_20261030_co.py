"""Cloth, weak and replace: material/clothing distinctions, loss of strength, substitutability."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
C=[['古英语 clāþ → 中古英语 cloth → cloth','布、覆盖物、衣物；更远来源不定'],['英语 cloth 与衣物支线','布料、单块布；旧复数 clothes 专门化为衣服']]
def CH(f,m):return C+[[f,m]]
W('cloth','英 /klɒθ/；美 /klɔːθ/ 或 /klɑːθ/','布料；一块布、抹布',
 '还没做成衣服的一匹料子，是不可数材料；剪成一块用来擦桌，也可数成 a cloth。',
 '接古英语 clāþ，旧义还包括衣物、覆盖物。现代材料与单块布保留；较远来源未定。古复数另发展为 clothes，今天不把所有布块复数写成 clothes。',C,
 'cotton cloth 棉布，a damp cloth 湿布，two cleaning cloths 两块清洁布。复数 cloths 常读 /klɒθs/〔英〕，不是 clothes 的长元音。',
 'cotton cloth；a piece of cloth；a damp cloth；cleaning cloths。',
 'cloth 布料或一块布，clothes 衣服，clothing 衣物集合；三者同族，现代不能互换语法。',
 ('She bought some blue cloth for the curtains.','她买了些蓝布做窗帘。'),('Wipe the table with a damp cloth.','用湿布擦擦桌子。'))
W('clothes','英 /kləʊðz/ 或 /kləʊz/；美 /kloʊðz/ 或 /kloʊz/','衣服〔复数集合〕',
 '衬衫、裤子、外套都放在一起叫 clothes。现代说的是穿在身上的衣物，不是所有剪下的布片。',
 '来自古英语 clāþas、经中古英语 clothes，是 cloth 衣物旧义的历史复数，后来词义、元音专门化。今天 cloths 表多块布、clothes 表衣物，两者分工。',C[:1]+[['古英语 clāþas → 中古英语 clothes → clothes','旧衣物复数 → 现代衣服集合']],
 'warm clothes 保暖衣服，change your clothes 换衣服，a change of clothes 一套替换衣物。通常用复数搭配，单件说 an item of clothing 等。',
 'warm clothes；change your clothes；a change of clothes。',
 'clothes are，不说 clothes is；a clothes 不能表示一件衣服。close 动词常与它近同音，但来源和意思不同。',
 ('Your clean clothes are in the cupboard.','你的干净衣服在柜子里。'),('Bring a change of clothes for the trip.','出门旅行带一套替换衣服。'))
W('clothe','英 /kləʊð/；美 /kloʊð/','给穿衣、提供衣物；覆盖、赋予〔比喻〕',
 '把衣服穿到某人身上，或供给他衣物；也可说把思想包进某种语言、给某物加上外在形式。',
 '接中古英语 clothen，更早古英语 *clāþian 属词源重建。与 cloth 同族的动词不是今天任意加一个 e，元音和 th 的清浊也有历史差别。',C[:1]+[['中古英语 clothen → clothe；更早有重建形 *clāþian','给穿衣、提供衣物；比喻覆盖、赋予']],
 'feed and clothe children 给孩子吃穿，clothe someone in 给某人穿上……，clothe an idea in words 把思想用语言表达；日常直接说穿某件衣服常用 wear。',
 'feed and clothe；clothe someone in；clothe an idea in words。',
 'clothe 给穿衣，wear 穿着；She clothed the child 说明她给孩子穿，She wore a coat 说她自己穿着外套。',
 ('The charity helps feed and clothe families in need.','慈善机构帮助困难家庭解决吃穿。'),('The writer clothed a simple idea in elegant language.','作者用优雅语言表达了一个简单想法。'))
W('clothed','英 /kləʊðd/；美 /kloʊðd/','穿着衣服的；披着、被赋予的〔比喻〕',
 '人已经穿上衣服，是 clothed；山披上白雪、想法披上漂亮语言，也可借衣服覆盖来描述。',
 '常见用法是 clothe 给穿衣的过去式、分词，词尾加 -d，/ðd/ 连读。另有较少的 cloth 材料名接 -ed 的读法，本页不混成同一日常形。',C[:1]+[['中古英语 clothen → clothe；更早有重建形 *clāþian；clothe 去 e + -ed → clothed','给穿衣 → 已穿衣；被覆盖、赋予的']],
 'fully clothed 穿戴完整，clothed in black 穿一身黑，clothed in snow 覆雪；不是每个搭配都真有衣物。',
 'fully clothed；clothed in black；clothed in snow。',
 'clothed 已穿衣、clothes 衣服名词；clothed 的 /ðd/ 和 clothes 的 /ðz/ 词尾不同。',
 ('He fell asleep on the sofa fully clothed.','他衣服都没脱，就在沙发上睡着了。'),('The hills were clothed in snow.','山丘披着白雪。'))
W('washcloth','英 /ˈwɒʃklɒθ/；美 /ˈwɑːʃklɑːθ/，部分美式 /ˈwɔːʃklɔːθ/','洗脸巾、洗澡用小毛巾〔美式常见〕',
 '一小块布或毛巾拿来擦洗脸、身体；名字把用途 wash 放前面。',
 'wash 洗 + cloth 布，合成器物名。英国常见相近说法 flannel，具体材质、大小依实物。',CH('wash + cloth → washcloth','擦洗脸、身体的小巾'),
 'a clean washcloth 干净洗脸巾，a damp washcloth 湿小毛巾，a soft washcloth 柔软洗脸巾。',
 'a clean washcloth；a damp washcloth；a soft washcloth。',
 'washcloth 小擦洗巾，dishcloth 常洗碗、擦厨房用；按用途区分，不是所有 cloth 都能互叫。',
 ('She wet a washcloth with warm water.','她用温水打湿了一条洗脸巾。'),('A clean washcloth lay beside the towel.','大毛巾旁放着一条干净洗脸巾。'))
W('clothier','英 /ˈkləʊðiə/；美 /ˈkloʊðiər/','服装商、制衣售衣者〔较正式〕',
 '做衣服、卖衣服的商家；今天店名、商业介绍里还可能遇到。',
 '中古英语 clother 后来变成 clothyer、clothier，人物词形受相似职业词影响。可按 cloth 与职业后缀 -ier 认识，历史不只是现代衣服单词加比较级。',C[:1]+[['中古英语 clother → clothyer、clothier','制作、售卖布或衣服的人']],
 'a local clothier 本地服装商，a men’s clothier 男装商，an established clothier 老牌服装商。',
 'a men’s clothier；a local clothier；an established clothier。',
 'clothier 从制作、售卖范围称商家，tailor 裁缝更突出裁剪、缝制、改衣；两种角色可以重叠。',
 ('He bought the suit from a local clothier.','他从一家本地服装商那里买了这套西装。'),('The old clothier’s sign still hung above the door.','那家老服装店的招牌仍挂在门上。'))
W('loincloth','英 /ˈlɔɪnklɒθ/；美 /ˈlɔɪnklɔːθ/','缠腰布、遮裆布',
 '围在腰胯附近，遮住下身的一块布；按覆盖的身体部位命名。',
 'loin 腰、胯部相关部位 + cloth 布，合成衣物名称。',CH('loin + cloth → loincloth','围腰遮盖下身的一块布'),
 'wear a loincloth 穿围腰布，a simple loincloth 简单缠腰布；历史、民族服饰或影视服装语境较常见。',
 'wear a loincloth；a simple loincloth；a cloth loincloth。',
 'loincloth 是特定结构衣物，不等于所有 skirt 裙子或 underwear 内衣；描述文化服饰时依具体实物称呼。',
 ('The illustration shows a man wearing a loincloth.','插图上是一位围着缠腰布的男子。'),('The costume included a simple linen loincloth.','这套戏服包括一块简单的亚麻围腰布。'))
W('cheesecloth','英 /ˈtʃiːzklɒθ/；美 /ˈtʃiːzklɔːθ/','稀松棉纱布、滤布',
 '有细孔，液体能流过、较大固体被留下；名字来自制奶酪时包、滤凝乳的用途。',
 'cheese 奶酪 + cloth 布，按早期典型用途命名。后来也用于厨房过滤等，不说明布本身由奶酪制成。',CH('cheese + cloth → cheesecloth','原用于奶酪制作的稀松布；可过滤等'),
 'strain through cheesecloth 用纱布过滤，a layer of cheesecloth 一层纱布，line a sieve with cheesecloth 给筛子铺纱布。',
 'strain through cheesecloth；a layer of cheesecloth；line a sieve。',
 'cheesecloth 厨房用滤布，cheese 奶酪食品；具体食用接触用途按材料说明，不把任意布都当合适滤布。',
 ('She strained the liquid through cheesecloth.','她用纱布过滤了液体。'),('Line the sieve with a layer of cheesecloth.','在筛子里铺一层纱布。'))
R('B3019','布料、单块布与衣服旧复数；制品按用途','CLOTH：一块材料可以覆盖、擦洗，也能做成衣物','cloth → clothes；clothe → clothed；clothier 职业；tablecloth、washcloth、loincloth、cheesecloth 按用途。',
 'cloths 布块复数与 clothes 衣物分清，读音不一律按拼写直读。clothed 常接 clothe 动词的结果，不把它认成衣物名词复数。',
 'cloth—cloths；旧复数 clothes；clothe 去 e + -ed → clothed；clothier 旧职业派生；table/wash/loin/cheese + cloth。',
 [['材料、衣物和穿衣结果','cloth · clothes · clothe · clothed'],['相关职业','clothier'],['桌布、清洗、衣物和过滤','tablecloth · washcloth · loincloth · cheesecloth']],
 'cloth/clothes/clothing 语法不同；clothes are，无 a clothes；clothed /ðd/ 与 clothes /ðz/；clothier 与 tailor 工作范围不同。',
 'She used a clean cloth to wipe the cupboard before putting away her clothes.\n\n她先用干净布擦了柜子，再把衣服放好。',
 'cloth clothes clothe clothed clothier tablecloth washcloth loincloth cheesecloth')
WE=[['古诺尔斯语 veikr → 中古英语 weik、wayk → weak','缺乏力量；与古英语 wāc 等同族'],['英语 weak','力量不足；薄弱、淡、无力、不充分']]
def WH(f,m):return WE+[[f,m]]
W('weak','/wiːk/','虚弱、无力的；薄弱的；淡的；不充分的',
 '推不动、撑不住是力量弱；论据撑不起结论、茶浓度不够，也借支撑不足来理解。',
 '现代形接中古英语 weik 等，来自古诺尔斯语 veikr，与本族旧词 wāc 有同族关系。旧背景含容易弯、让步等，现代抽象义按对象区分。',WE,
 'weak muscles 力量弱的肌肉，a weak signal 弱信号，weak tea 淡茶，a weak argument 站不住脚的论证。',
 'a weak signal；weak tea；a weak argument；feel weak。',
 'weak 与 week 周同音异词；weak tea 浓度低，不是茶叶身体虚弱。弱点也不等于人完全无价值。',
 ('The radio signal is too weak here.','这里无线电信号太弱。'),('That is a weak argument for changing the plan.','拿这个理由来主张改计划，论据不够有力。'))
W('weakness','/ˈwiːknəs/','虚弱；弱点、不足；特别喜欢的东西〔a weakness for〕',
 '一方面是撑不住的地方，另一方面也可说某种诱惑面前自己抵挡不住，于是特别喜欢。',
 'weak + -ness，现代词形接中古英语 weyknesse，也替换了较早本族对应形式。性质名词又可数化为具体弱点。',WH('weak + -ness → weakness','虚弱状态；具体弱点；抵不住的偏爱'),
 'a weakness in the plan 计划弱点，muscle weakness 肌肉无力，have a weakness for chocolate 偏爱巧克力。',
 'a major weakness；a weakness in；have a weakness for。',
 'weakness 不可数状态与可数不足并存；a weakness for sweets 是偏爱，不是在给甜食做医学诊断。',
 ('The review identified a weakness in the design.','评审指出设计中的一个弱点。'),('I have a weakness for old bookshops.','我特别喜欢老书店。'))
W('weaken','/ˈwiːkən/','削弱；变弱',
 '原来还能支撑，后来力气、效力一点点减掉。可说某因素削弱它，也可说它自己逐渐变弱。',
 'weak + -en，形成状态变化动词。既及物使弱，也不及物变弱。',WH('weak + -en → weaken','使力量、作用减小；变弱'),
 'weaken the structure 削弱结构，weaken confidence 削弱信心，the wind weakens 风势减弱。',
 'weaken confidence；weaken the structure；gradually weaken。',
 'weak 状态，weaken 变化；weaken 不必完全 destroy 毁掉，只是程度下降。',
 ('The cracks weakened the wall.','裂缝削弱了墙的强度。'),('The wind weakened during the afternoon.','下午风势减弱了。'))
W('weakly','/ˈwiːkli/','无力地、微弱地；〔较旧形容词〕体弱的',
 '说话声音轻得像没有力气，或试着笑一下却没精神；日常主要修饰动作。',
 '副词可按 weak + -ly 认识，中古英语已有相应形式。另有较旧的体弱形容词，接本族旧派生背景；不把它们都当刚造出的同一副词。',WH('weak + -ly；另有旧本族形容词背景','无力地；较旧形容词体弱的'),
 'smile weakly 无力地笑，protest weakly 软弱地反对，glow weakly 发微弱光。',
 'smile weakly；protest weakly；glow weakly。',
 'weakly 无力地、weekly 每周地常同音；a weekly meeting 是每周会议，不是无力的会议。',
 ('She smiled weakly and sat down.','她无力地笑了笑，坐了下来。'),('The old lamp glowed weakly in the corner.','旧灯在角落里发着微弱的光。'))
W('weakling','/ˈwiːklɪŋ/','弱小、软弱的人〔常贬义〕',
 '把弱这个特点直接叫到人身上，常有轻视、欺负的语气；不是中性身体状况描述。',
 'weak + -ling，-ling 构成有某特点的人等名词，在此常有贬意；不是动词的 -ing。',WH('weak + -ling → weakling','被认为弱小、软弱的人物称呼'),
 'a weakling 一个软弱的人，call someone a weakling 嘲人软弱。文学角色可能用来自嘲或攻击他人。',
 'a weakling；call him a weakling；a timid weakling。',
 'weakling 人物贬称，weakness 特点或弱点；不能因为 someone has a weakness 就认定对方整个人是 weakling。',
 ('The bully called the younger boy a weakling.','欺凌者骂那个更小的男孩是软蛋。'),('She refused to see herself as a weakling.','她不肯把自己看作软弱的人。'))
R('B3393','力量、支撑或效力不足；弱点和减弱','WEAK：撑不够、力不够，换对象看哪里不足','weak → weakness、weaken、weakly；weakling 人物贬称放后面。',
 '信号、茶、论证、身体按对象具体讲。偏爱 a weakness for 从抵不住诱惑理解，不只背缺点一个中文义。',
 'weak + -ness/-en/-ly/-ling；-ling 人物词不是 -ing；weak/weakly 与 week/weekly 同音对照。',
 [['性质、弱点、变化和方式','weak · weakness · weaken · weakly'],['人物贬称','weakling']],
 'weak/week 同音，weakly/weekly 同音；weaken 变化非状态；weakness for 偏爱；weakling 语气不应抹平。',
 'The weak signal weakened further as we entered the tunnel.\n\n进入隧道后，本来就弱的信号变得更弱了。','weak weakness weaken weakly weakling')
RP=[['replace 的替换、更换等现代用法','换一个来接替；另有放回等用法背景'],['replace + -able → replaceable','可以换掉、可以找到替代的']]
W('replaceable','/rɪˈpleɪsəbəl/','可替换的、可更换的',
 '坏了可以换一个新的，或这个角色可以由别人接手。重点在有替代办法。',
 'replace + -able，保留 e，形成可被替换的形容词。这里接替换义，不把所有 replace 的历史和现代义都压成重新摆放。',RP,
 'a replaceable battery 可更换电池，replaceable parts 可换零件，easily replaceable 容易替代的。',
 'a replaceable battery；replaceable parts；easily replaceable。',
 'replaceable 可替换，repairable 可修理；可换不保证能修，能修也不保证有替代件。',
 ('The device has a replaceable battery.','这台设备的电池可以更换。'),('The damaged part is easily replaceable.','损坏的零件很容易更换。'))
R('B4159','换掉、接替；替代物与可替换性质','REPLACE：原来的位置由另一个来接上','replace → replacement → replaceable，复用已有前两词精讲。',
 '替换动作、替代物和是否能换分清。可替换不保证可修理，产品用途只用作词义例子。',
 'replace + -ment/-able；replacement 和 replaceable 不同词性。',
 [['动作、替代物和性质','replace · replacement · replaceable']],
 'replace 替换、replacement 替代物或更换、replaceable 可换；repairable 可修不是同义。',
 'The replacement battery is replaceable too.\n\n换上的新电池也可以再更换。','replace replacement replaceable')
if __name__=='__main__':save('continuation_20261030_co',ROOTS,WORDS)
