"""Horse and yard: physical names, coarse-size prefix; enclosure vs measurement."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
HO=[['古英语 hors → 中古英语 hors、horse → horse','马；更远来源有不同分析'],['英语 horse 及比喻、合成','骑乘、牵引动物；强壮、粗大；按用途叫工具、人物等']]
def HH(f,m):return HO+[[f,m]]
W('horse','英 /hɔːs/；美 /hɔːrs/','马；与马有关的；〔比喻〕强壮、粗大等',
 '能骑、能拉车的马，是日常画面。合成词有的真说马背、马毛，有的借马的力量、体量，不要求所指都是动物。',
 '本族词，接古英语 hors。更远有人联系跑的旧词根，也有借入等不同解释，从可靠旧形讲起。工具、力气和粗大等比喻在具体组合中认。',HO,
 'ride a horse 骑马，a horse race 赛马，hold your horses 别急，a dark horse 黑马、实力未明者。horsepower、workhorse 已有精讲，可一起复习。',
 'ride a horse；a horse race；hold your horses；a dark horse。',
 'horse 马、pony 小型马，不完全按幼年成年区分；foal 驹才直接说幼马。horse 的合成比喻不套用所有动物事实。',
 ('She learned to ride a horse as a child.','她小时候学会了骑马。'),('Hold your horses—we have not checked the date yet.','别急，我们还没核对日期呢。'))
W('horsehair','英 /ˈhɔːsheə/；美 /ˈhɔːrsher/','马毛〔尤鬃、尾长毛〕',
 '按材料来源叫名字：从马身上取得、常用于刷子、弓毛或填充等用途的毛。',
 'horse + hair，旧时已有相应组合。常作为材料不可数，也可作定语说明相关制品。',HH('horse + hair → horsehair','马的毛；相应用途材料'),
 'a horsehair brush 马毛刷，horsehair stuffing 马毛填充料，horsehair for violin bows 小提琴弓用马尾毛等。',
 'a horsehair brush；horsehair stuffing；natural horsehair。',
 'horsehair 材料来源，hairstyle 发型；horsehair brush 不是给马梳毛的所有刷子的总称，而常指刷毛材料是马毛。',
 ('He cleaned the shoes with a soft horsehair brush.','他用软马毛刷清理鞋子。'),('The restorer found horsehair stuffing inside the old chair.','修复师在旧椅子里发现了马毛填充料。'))
W('horseradish','英 /ˈhɔːsrædɪʃ/；美 /ˈhɔːrsrædɪʃ/','辣根；辣根酱〔按语境〕',
 '一种味道冲、常用根制成调味品的植物。名字里的 horse 常解释为粗大、强劲这类旧加强义，不是马爱吃的萝卜。',
 'horse + radish，horse 在这类旧植物名中可表强、粗大。不要把德语 Meerrettich 被误听成马的流行故事当作可靠唯一词源。',HH('horse〔粗大、强劲的旧用法〕+ radish → horseradish','辣根植物及相应调味品'),
 'horseradish sauce 辣根酱，grated horseradish 磨碎辣根，a little horseradish 少许辣根调味品。',
 'horseradish sauce；grated horseradish；a horseradish root。',
 'horseradish 辣根与 wasabi 山葵是不同植物名；有些调味品的实际配料会混合、替代，不能靠颜色直接判来源。',
 ('She added a little grated horseradish to the sauce.','她往酱汁里加了一点磨碎的辣根。'),('The jar contains horseradish sauce.','罐子里装的是辣根酱。'),
 sources=['https://en.wiktionary.org/wiki/horseradish#English','https://www.etymonline.com/word/horseradish'])
R('B4597','马及部位、用途；力量、体量与工具比喻','HORSE：真实的马，也借力量、体量给别物命名','horse → horsehair、horseback、horseman；horsepower 力量、racehorse 竞赛、workhorse/warhorse 比喻，horseradish 单讲旧加强义。',
 '已有多数常见合成精讲复用。horseradish 不解释成给马吃的萝卜，冷门与粗俗变体本轮略。',
 'horse + hair/back/man/power/radish；race/work/war + horse。',
 [['基本动物与相关部位、人物','horse · horsehair · horseback · horseman'],['力量、用途和比喻','horsepower · racehorse · workhorse · warhorse'],['旧加强义植物名','horseradish']],
 'pony 小型马不等于所有幼马；horsehair 按材料命名；horseradish 非马食萝卜，wasabi 另种植物。',
 'The horseman brushed the horse before the ride.\n\n骑手出发骑行前给马刷了刷毛。','horse horsehair horseback horseman horsepower racehorse workhorse warhorse horseradish')
YE=[['古英语 ġeard → 中古英语 yerd → yard','围起的地块、院子'],['另一词：古英语 ġierd → 中古英语 yerd → yard','杆、杖、量杆 → 码；船帆横桁也接杆义'],['现代 yard 两条常用线','院落、作业场地；长度单位']]
def EH(f,m):return YE[:1]+[[f,m]]
W('yard','英 /jɑːd/；美 /jɑːrd/','院子、场地；〔另源〕码、帆桁',
 '一条是房子外的一块地、工厂的一片作业场；另一条来自量杆，是长度单位码。院子并不是因为长一码才叫 yard。',
 '院子接古英语 ġeard，码接另一词 ġierd 杆、杖。两词后来同形同音。常用一码等于三英尺；帆船横桁保留杆的旧支线。',YE,
 'in the yard 在院子里，a railway yard 铁路调车场，three yards of cloth 三码布。yardstick 接量杆，backyard 接院子，复习时按来源分。',
 'in the yard；a railway yard；a yard of cloth；three feet。',
 'yard 院子与码不是同一个直接来源；garden 园子常突出栽种，英美院落称法有习惯差异。',
 ('The children are playing in the yard.','孩子们在院子里玩。'),('We need three yards of fabric for the curtains.','做窗帘需要三码布。'),
 sources=['https://en.wiktionary.org/wiki/yard#English','https://www.etymonline.com/word/yard'])
W('yardage','英 /ˈjɑːdɪdʒ/；美 /ˈjɑːrdɪdʒ/','以码计的长度、用量；码数',
 '不是问有没有院子，而是问这段距离、这块布一共有多少码。',
 'yard 码 + -age，总量、用量相关名词；日常布料、体育场景可见。',YE[1:2]+[['yard + -age → yardage','按码计量的距离、布料数量等']],
 'fabric yardage 布料码数，total yardage 总码数，gain yardage 在场上推进取得码数。',
 'fabric yardage；total yardage；gain yardage。',
 'yardage 接长度单位支线，不是院子总面积的唯一叫法；yardstick 标尺与它同接测量义。',
 ('Check the required yardage before buying the fabric.','买布之前先核对所需码数。'),('The team gained yardage on the next play.','下一次进攻中，球队向前推进了一段距离。'))
W('orchard','英 /ˈɔːtʃəd/；美 /ˈɔːrtʃərd/','果园',
 '一片地专门栽果树，而不是零星摆几个果盘。名字后半旧时就是园地、院地的词。',
 '接古英语 orċeard、ortġeard，末部 ġeard 与 yard 院地同族。首部常联系旧草木词 wort 一类，也涉及拉丁语 hortus 等影响的分析；细节不强定为唯一拼法。',
 [['古英语 ortġeard、orċeard → 中古英语 orchard → orchard','果树园地；末部接 ġeard 院地'],['现代 orchard','种植果树的园地']],
 'an apple orchard 苹果园，a cherry orchard 樱桃园，an orchard in blossom 花开满园的果园。',
 'an apple orchard；a cherry orchard；walk through the orchard。',
 'orchard 果树园，vineyard 葡萄园；葡萄藤不是普通树形，英语用不同固定名词。orchard 不拆成 or 或者 + chard 叶甜菜。',
 ('The apple orchard was full of blossom.','苹果园里开满了花。'),('We walked through the orchard after lunch.','午饭后我们在果园里走了走。'),
 sources=['https://en.wiktionary.org/wiki/orchard#English','https://www.etymonline.com/word/orchard'])
W('graveyard','英 /ˈɡreɪvjɑːd/；美 /ˈɡreɪvjɑːrd/','墓地；废弃物集中处〔比喻〕',
 '给坟墓留出的一片地；废船、废车集中停放，看起来像它们最后的归宿，也可借称 graveyard。',
 'grave 坟墓 + yard 场地。grave 这里是坟墓名词，不是严肃的形容词；具体合成直接按用途形成。',EH('grave + yard → graveyard','埋葬场所；废弃物最后集中处'),
 'an old graveyard 旧墓地，a ship graveyard 废船集中地，the graveyard shift 夜班、深夜班。后者指时段，不要求在墓地工作。',
 'an old graveyard；a ship graveyard；the graveyard shift。',
 'graveyard、cemetery 都可墓地，前者传统常联系教堂院地，现代用法也有重叠，不能硬说所有 graveyard 一定紧挨教堂。',
 ('An old graveyard lies behind the church.','教堂后面有一片旧墓地。'),('He works the graveyard shift at the factory.','他在工厂上深夜班。'))
W('barnyard','英 /ˈbɑːnjɑːd/；美 /ˈbɑːrnjɑːrd/','谷仓、牲畜棚附近的场院',
 '走到 barn 旁边，鸡、鸭、牲畜可能在院地上活动。强调农场这块院地和相关场景。',
 'barn 仓棚 + yard 院地，形成场所名，也可修饰 barnyard animals 等。',EH('barn + yard → barnyard','仓棚附近的场院'),
 'barnyard animals 场院家畜、家禽，a muddy barnyard 泥泞农家院地，barnyard sounds 农家动物声。',
 'barnyard animals；a muddy barnyard；in the barnyard。',
 'barnyard 场院，barn 建筑，farm 整个农场；不要把所有层级都译成同一栋谷仓。',
 ('Chickens wandered around the barnyard.','鸡在农家场院里四处走动。'),('The children listened to the sounds of the barnyard.','孩子们听着农家院地里的动物叫声。'))
W('junkyard','英 /ˈdʒʌŋkjɑːd/；美 /ˈdʒʌŋkjɑːrd/','废品场、旧汽车拆解场等',
 '废机器、旧车、零件集中放的一块地，有些东西还能拆下来用。不是所有东西都已毫无价值。',
 'junk 废旧物 + yard 场地，按存放、处理对象命名，尤美式常见。',EH('junk + yard → junkyard','存放、处理废旧物品的场地'),
 'a car junkyard 旧车废品场，junkyard parts 废品场拆下的零件，search a junkyard 逛废品场找物。',
 'a car junkyard；junkyard parts；in a junkyard。',
 'junkyard 侧重废旧物堆存、拆用，landfill 填埋场侧重处置方式；不能把两者完全互换。',
 ('He found a replacement door at a junkyard.','他在废品场找到了一扇可替换的车门。'),('The old van was taken to the junkyard.','那辆旧货车被送去了废品场。'))
W('scrapyard','英 /ˈskræpjɑːd/；美 /ˈskræpjɑːrd/','废料场、废金属处理场',
 '不用的金属、机器被集中拆解、分类，等着再利用；场地里的重点是可作废料处理的东西。',
 'scrap 废料 + yard 场地，形成处理废料场所的名词。',EH('scrap + yard → scrapyard','收集、拆解或处理废料的场地'),
 'a metal scrapyard 废金属场，send a car to the scrapyard 把车送去拆解，scrapyard workers 废料场工人。',
 'a metal scrapyard；send it to the scrapyard；scrapyard workers。',
 'scrapyard 和 junkyard 用法重叠；前者常更突出废料、金属回收，后者也常旧物、零件，地区习惯有差异。',
 ('The damaged cars were sent to a scrapyard.','损坏的汽车被送去废料拆解场。'),('Workers sorted the metal at the scrapyard.','工人在废料场分拣金属。'))
W('dockyard','英 /ˈdɒkjɑːd/；美 /ˈdɑːkjɑːrd/','船坞场、船舶建造修理场',
 '围着船坞安排起工棚、工具、工作区，专门造船、修船；不是普通买船票的码头。',
 'dock 船坞 + yard 作业场，合成与建造、修理船舶有关的设施名。',EH('dock + yard → dockyard','围绕船坞的造修船场所'),
 'a naval dockyard 海军船坞场，dockyard workers 船坞工人，repairs at the dockyard 在船坞场维修。',
 'a naval dockyard；dockyard workers；at the dockyard。',
 'dockyard 较完整造修船场，drydock 是可排水露出船体的干船坞；场地与其中设施不要混作完全同义。',
 ('The vessel was repaired at the dockyard.','船在船坞场修好了。'),('Several dockyard workers inspected the hull.','几位船坞工人检查了船体。'))
W('boatyard','英 /ˈbəʊtjɑːd/；美 /ˈboʊtjɑːrd/','小船建造、修理或存放场',
 '小船、帆船停上岸后检查、修理、存放的一片作业场。名字按服务对象 boat 来叫。',
 'boat 船 + yard 场地，合成船只建造、维修、存储设施名。',EH('boat + yard → boatyard','小船造修或存放的场地'),
 'a local boatyard 当地船修存放场，boatyard repairs 船场维修，store a boat at a boatyard 把船存放在船场。',
 'a local boatyard；at the boatyard；boatyard repairs。',
 'boatyard 偏小船相关作业，shipyard 较常说大型造船、修船设施；用词范围有重叠，不凭词强定船长界线。',
 ('We left the sailing boat at the boatyard for repairs.','我们把帆船留在船场维修。'),('The boatyard stores small boats over the winter.','这家船场在冬季存放小船。'))
W('lumberyard','英 /ˈlʌmbəjɑːd/；美 /ˈlʌmbərjɑːrd/','木材场、木材堆售场〔美式常见〕',
 '一叠叠锯好的木料按规格堆着，等着售卖或取用；不是树还在原地生长的森林。',
 'lumber 木材〔美式〕+ yard 堆存、交易场，按材料命名。',EH('lumber + yard → lumberyard','堆存、出售木材的场所'),
 'buy wood at a lumberyard 在木材场买木料，a local lumberyard 本地木材场。英式相关表达常用 timber yard。',
 'a local lumberyard；at the lumberyard；lumberyard stock。',
 'lumberyard 木料场，forest 森林；yard 在这里是场地，不是说木料长一码。',
 ('We bought the boards at a local lumberyard.','我们在本地木材场买了木板。'),('Stacks of timber filled the lumberyard.','一垛垛木料堆满了木材场。'))
W('brickyard','英 /ˈbrɪkjɑːd/；美 /ˈbrɪkjɑːrd/','砖场、制砖场',
 '不是铺了砖的普通小院，而是生产、堆放砖的作业场。',
 'brick 砖 + yard 场地，按制品与作业用途命名。',EH('brick + yard → brickyard','制砖、堆砖的场地'),
 'an old brickyard 旧砖场，brickyard workers 砖场工人，brickyard kilns 砖场窑炉。',
 'an old brickyard；brickyard workers；at the brickyard。',
 'brickyard 工作场所，a brick courtyard 是铺砖庭院；词序、合成约定不同。',
 ('The old brickyard supplied bricks for many local houses.','旧砖场曾为当地许多房屋供应砖。'),('Workers stacked the finished bricks in the brickyard.','工人在砖场码放烧好的砖。'))
W('boneyard','英 /ˈbəʊnjɑːd/；美 /ˈboʊnjɑːrd/','墓地〔口语〕；废弃飞机、机器等集中存放处',
 '骨头最后归处的画面，被借给老飞机、旧设备退役后的存放地。',
 'bone 骨 + yard 场地，形成墓地等口语称呼，继而比喻退役设备集中地；不保证现场有真的骨头。',EH('bone + yard → boneyard','墓地；比喻退役设备的最后存放场'),
 'an aircraft boneyard 退役飞机存放场，an old boneyard 旧墓地或废弃设备场，依对象分辨。',
 'an aircraft boneyard；a desert boneyard；an old boneyard。',
 'boneyard 带终点、退役比喻；存放的设备有时仍可拆件或恢复，不保证全被毁坏。graveyard 也有相近比喻。',
 ('Rows of retired aircraft stood in the desert boneyard.','一排排退役飞机停在沙漠存放场里。'),('The documentary explores an old aircraft boneyard.','纪录片探访了一处旧退役飞机存放场。'))
R('B3620','围合院地与作业场；码、量杆另源','YARD：一块围地；另一条是量长度的杆','yard → yardage、yardstick 接测量；orchard 接旧院园词；庭院、墓地、造修船与废料材料场按用途分组。',
 '院子与长度单位码必须分源；大部分场所合成接院地，而 yardage、yardstick 接量杆。旧 orchard 末部与 yard 同族，首部细节保留不同分析。',
 'yardage：yard + -age；yardstick：yard + stick；场地：back/court/grave/vine/ship/church/school/barn/farm/junk/scrap/dock/boat/lumber/brick/bone + yard。',
 [['两条基本义与测量','yard · yardage · yardstick'],['旧果园与日常院地','orchard · backyard · courtyard · schoolyard · barnyard · farmyard'],['墓地和种植地','graveyard · churchyard · vineyard'],['船只作业','shipyard · dockyard · boatyard'],['废料与材料场','junkyard · scrapyard · lumberyard · brickyard · boneyard']],
 'yard 院地与码分源；orchard 非 or+chard；dockyard 场地、drydock 设施；junkyard/scrapyard 常重叠；graveyard shift 深夜班非墓地工作。',
 'We bought three yards of cloth and carried it across the yard.\n\n我们买了三码布，提着它穿过院子。',
 'yard yardage yardstick orchard backyard courtyard schoolyard barnyard farmyard graveyard churchyard vineyard shipyard dockyard boatyard junkyard scrapyard lumberyard brickyard boneyard')
if __name__=='__main__':save('continuation_20261030_cn',ROOTS,WORDS)
