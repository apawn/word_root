"""Bottom, parliament, bus and wealth: locations, institutions, transport, abundance."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
B=[['古英语 botm → 中古英语 botme、botom → bottom','底部、基础、地面'],['英语 bottom','最下部；最低位置；臀部；触底等']]
W('bottom','英 /ˈbɒtəm/；美 /ˈbɑːtəm/','底部、最下端；末位；臀部；触底〔动词〕',
 '杯子的下面、海的最深处、名单最后一行，都可以从最下面这一位置理解。人的 bottom 则是坐下时接触椅子的臀部。',
 '由古英语 botm 经中古英语延续，不是 bot + tom 的现代合成。动词触底、达到最低点接底部名词发展。',B,
 'at the bottom of 在……底部，the bottom of the page 页底，bottom out 触底、跌势见底。get to the bottom of 查清根本原因。',
 'at the bottom；the bottom drawer；bottom out；get to the bottom of。',
 'bottom 最下部，base 基础、底座常强调支撑功能；at the bottom of a list 表排名最后，不一定物理上离地最近。',
 ('Your keys are at the bottom of the bag.','钥匙在包的底部。'),('The answer is printed at the bottom of the page.','答案印在页底。'))
W('bottomless','英 /ˈbɒtəmləs/；美 /ˈbɑːtəmləs/','无底的；深不见底的；似乎无穷无尽的',
 '向下望，看不到尽头；借来形容精力、需求或续杯服务时，抓的是一直用不完的感觉。',
 'bottom + -less，中古英语已有相应形式。字面无底与夸张极深、无限供给分语境理解。',B+[['bottom + -less → bottomless','没有底；比喻深或多得仿佛没有尽头']],
 'a bottomless pit 无底洞，bottomless energy 用不完的精力，bottomless coffee 可续杯咖啡。服务用语仍由具体规则限定。',
 'a bottomless pit；bottomless energy；bottomless coffee。',
 'bottomless 仿佛没底，deep 深；深井有底仍可被夸张叫 bottomless，不把每处都当物理测量结论。',
 ('The old well looked like a bottomless pit.','那口老井看起来像个无底洞。'),('The café offers bottomless coffee with breakfast.','这家咖啡馆早餐提供可续杯咖啡。'))
W('bottomed','英 /ˈbɒtəmd/；美 /ˈbɑːtəmd/','达到底部的；有某种底部的〔通常与修饰成分连用〕',
 '当作 bottom 的过去式，是已经碰到底、降到底；描述器物时，则常是有怎样的底。',
 'bottom + -ed；一条是动词过去式、分词，一条是具有底部结构的形容词材料。带修饰成分的写法常见，但本条不另堆连字符词。',B+[['bottom + -ed → bottomed','已经触底；有某种底部结构的']],
 'prices bottomed out 价格触底，the boat bottomed on the mud 船底碰到泥底；具体含义靠动词结构判断。',
 'bottomed out；bottomed on the mud；has bottomed out。',
 'bottomed 过去形式，bottomless 无底；bottomed out 表达到低点，不由词本身保证之后一定大幅反弹。',
 ('Sales bottomed out in January.','销量在一月降到了最低点。'),('The boat bottomed on the mud at low tide.','退潮时船底碰到了淤泥。'))
R('B3669','最下面、基础、最低点；无底与触底','BOTTOM：向下直到尽头的位置','bottom → bottomless、bottomed，把无底性质与触底动作分开。',
 '物理位置、排名、最低点、臀部按具体场景认。价格例子只解释用语，不凭 bottomed 推断未来涨跌。',
 'bottom + -less/-ed；bottom out 达到最低点；at the bottom of。',
 [['底部、无底与触底','bottom · bottomless · bottomed']],
 'bottomless 常有夸张；bottomed out 不保证反弹；bottom/base 最下部与支撑基础侧重不同。',
 'We found the missing coin at the bottom of the box.\n\n我们在盒底找到了丢失的硬币。','bottom bottomless bottomed')
P=[['法语 parler 说话 + -ment → parlement','讨论、商谈、会议'],['盎格鲁法语 parlement 等 → 中古英语 parlement → parliament','议事集会 → 议会；拼写受中世纪拉丁语形式影响']]
def PH(f,m):return P+[[f,m]]
W('parliament','英 /ˈpɑːləmənt/；美 /ˈpɑːrləmənt/','议会、国会',
 '本来是一群人聚在一起商谈，后来专门叫议事、立法的机构。词的出发点是说话讨论，不是现代英语 part 加 lie。',
 '经法语 parlement，与 parler 说话和 -ment 动作名词材料有关。中古英语后来的 parliament 拼写受中世纪拉丁语相近形式影响；常用发音不逐字读出 ia。',P,
 'a member of parliament 议会议员，a parliamentary debate 的机构基础是 parliament。Parliament 大写时可指特定议会，制度和权限依国家而异。',
 'a member of parliament；address parliament；the parliament building。',
 'parliament 机构，government 政府，不能一律视作同一个组织；congress 也是某些制度下的议会名称，名称不能推出全部制度。',
 ('The proposal was debated in parliament.','这项提案在议会进行了辩论。'),('She was elected a member of parliament.','她被选为议会议员。'))
W('parliamentary','英 /ˌpɑːləˈmentəri/；美 /ˌpɑːrləˈmentəri/','议会的；符合议事规则的',
 '给辩论、选举、委员会加一个标签：它属于议会或按相应议事程序进行。',
 'parliament + -ary，形成关系形容词。重音转到 /men/ 附近，不能完全按基础词的重音照搬。',PH('parliament + -ary → parliamentary','与议会有关；按议事规则的'),
 'a parliamentary debate 议会辩论，a parliamentary committee 议会委员会，parliamentary procedure 议事程序。',
 'a parliamentary debate；a parliamentary committee；parliamentary procedure。',
 'parliamentary 议会相关，parliamentarian 人物或相关形容词；a parliamentary system 描写制度类型，不直接等于每一项具体政策。',
 ('The report was examined by a parliamentary committee.','报告由一个议会委员会审查。'),('The chair explained the parliamentary procedure before the vote.','主持人在投票前解释了议事程序。'))
W('parliamentarian','英 /ˌpɑːləmənˈteəriən/；美 /ˌpɑːrləmənˈteriən/','议会议员；熟悉议事程序的人',
 '一条是坐在议会里履职的人；另一条是懂开会、提案、表决规则，能指导程序的人。',
 'parliament + -arian，形成相关人物名称。议员与议事程序专家两种常见语境，不能只背其中一个。',PH('parliament + -arian → parliamentarian','议会成员；议事程序专家等'),
 'an experienced parliamentarian 资深议员，consult a parliamentarian 咨询议事程序专家；实际角色依机构和上下文。',
 'an experienced parliamentarian；a senior parliamentarian；consult a parliamentarian。',
 'parliamentarian 人物，parliamentary 多修饰事物；并非所有被叫 parliamentarian 的人都在当议员，也可能负责程序咨询。',
 ('Several parliamentarians spoke against the proposal.','几位议员发言反对这项提案。'),('The club consulted a parliamentarian about the voting rules.','俱乐部就投票规则咨询了一位议事程序专家。'))
R('B3211','商谈集会发展为议会；制度性质与人物','PARLIAMENT：聚到一起讨论，专门化为议事机构','parliament → parliamentary → parliamentarian，机构、性质和人物相邻。',
 '法语 parler 的说话背景保留为词源，不据此把现代议会简单解释为任何聊天聚会。不同国家制度不混为一谈。',
 '法语 parler + -ment；parliament + -ary/-arian，派生重音不同。',
 [['机构、相关性质与人物','parliament · parliamentary · parliamentarian']],
 'parliament/government 不等同；parliamentarian 可议员也可程序专家；基础词不按 ia 逐字硬读。',
 'The parliamentarian joined the parliamentary debate.\n\n那位议员参加了议会辩论。','parliament parliamentary parliamentarian')
BU=[['拉丁语 omnibus〔给所有人的〕 → 法语公共车名称 omnibus','面向众人的公共车辆'],['英语 omnibus 缩短 → bus','公共汽车；交通动词及技术总线等比喻']]
def BH(f,m):return BU+[[f,m]]
W('bus','/bʌs/','公共汽车；用巴士运送；总线〔技术〕',
 '很多人共乘的一辆公共车；这个名字实际上是较长的 omnibus 留下的尾巴。技术总线也借了共同输送通道的画面。',
 'omnibus 的截短，较长名称经法语交通用语接拉丁语 omnibus 给所有人。不是把 bus 三个字母各展开成一个英语词。',BU,
 'take a bus 坐公交，by bus 乘公交，bus children to school 用巴士接送孩子，a data bus 数据总线。餐馆里 bus tables 收桌是另一条相关职业用法。',
 'take the bus；a bus stop；by bus；a data bus。',
 'bus 车辆，coach 常指长途或旅游大巴但也有其他义；by bus 通常不加冠词，take the bus 则按具体搭配用冠词。',
 ('I usually go to work by bus.','我通常坐公交上班。'),('The school buses the children to the museum.','学校用巴士把孩子们送到博物馆。'))
W('minibus','/ˈmɪnibʌs/','小型公共汽车、小巴',
 '能载一组乘客，但比通常想象的大巴更小的车。mini- 先把尺寸、容量缩小。',
 'mini- 小型 + bus 巴士，合成车辆名。名称没有规定全球统一的精确座位数。',BH('mini- + bus → minibus','小型巴士'),
 'a school minibus 学校小巴，hire a minibus 租一辆小巴，a minibus service 小巴服务。',
 'hire a minibus；a school minibus；travel by minibus。',
 'minibus 载客小巴，van 厢式车更泛，可载货也可载人；不能只看外形像就认定用途相同。',
 ('We hired a minibus for the group trip.','我们为集体出游租了一辆小巴。'),('A school minibus picked up the children.','一辆学校小巴来接孩子们。'))
W('airbus','英 /ˈeəbʌs/；美 /ˈerbʌs/','大型客机、空中巴士；Airbus 为专名',
 '把飞机看成在空中载很多乘客的公共交通工具，是这个合成词的直观画面。现实阅读大写 Airbus 常是航空制造企业或其飞机的专名。',
 'air 空中 + bus 巴士，先有大型客机等通称背景；大写专名使用需与普通名词区分。具体品牌名称不按一架真正飞起来的公路巴士理解。',BH('air + bus → airbus','空中载客交通工具；亦用于专名 Airbus'),
 'an airbus 普通名词客机用法较少见，an Airbus aircraft 大写专名常见；a model of an Airbus 某型号空客飞机模型。',
 'an Airbus aircraft；an Airbus model；a large airbus。',
 'airbus 通称与 Airbus 专名大小写不同；不是所有客机都可在品牌意义上叫 Airbus。',
 ('The museum displayed an old advertisement for an airbus service.','博物馆展出了一则旧空中巴士服务广告。'),('He built a model of an Airbus aircraft.','他做了一架空客飞机模型。'))
R('B3248','公共车名称的截短；小巴和空中载客','BUS：面向众人共乘的交通工具','bus → minibus、airbus；尺寸和运输环境分支相邻。',
 '较长 omnibus 接拉丁语给所有人的形式。airbus 普通词与大写专名区分，冷门 bussy 同形和俚语暂不收。',
 'omnibus → bus〔截短〕；mini-/air + bus。',
 [['公共车、尺寸与空中运输','bus · minibus · airbus']],
 'by bus/take the bus 冠词搭配不同；minibus 不规定统一座位数；Airbus 专名不指所有飞机。',
 'The group took a minibus to the airport.\n\n大家乘小巴去了机场。','bus minibus airbus')
WE=[['古英语 wela〔繁荣、福祉〕等 → 中古英语 wele、welthe','安好、幸福、富足；-th 性质名词形成或类推有不同分析'],['英语 wealth','财富、富足；大量有用资源']]
W('wealth','/welθ/','财富；富足；大量、丰富的资源',
 '不只看每月流进来多少，还看积累、拥有多少有价值的东西。知识、经验很多，也能叫 a wealth of。',
 '接中古英语 welthe 等，与 weal 安好、福祉同族。可对照 weal + 旧抽象后缀 -th 认识；更早继承或类推形成有不同分析，不把重建旧形当成确实记录。',WE,
 'personal wealth 个人财富，a wealth of experience 丰富经验，create wealth 创造财富。通常不可数，不说几只 wealth。',
 'a wealth of information；personal wealth；create wealth。',
 'wealth 财富存量、富足，income 收入流入；一个时期收入高，不自动说明已积累很多财富。a wealth of details 不是给细节标价。',
 ('The library contains a wealth of information about local history.','图书馆里有丰富的地方史资料。'),('She used part of her wealth to support the arts.','她用一部分财富支持艺术事业。'))
W('wealthy','/ˈwelθi/','富有的、财富充足的',
 '说一个人或家庭拥有很多有价值的资源，日常主要指经济富裕。',
 'wealth + -y，形成具有财富、富足性质的形容词，中古英语已有 welthy 等形式。',WE+[['wealth + -y → wealthy','拥有丰富财富的、富有的']],
 'a wealthy family 富裕家庭，a wealthy country 富裕国家，the wealthy 富人群体。',
 'a wealthy family；a wealthy donor；the wealthy。',
 'wealthy 与 rich 在富有义常接近；rich 还常指味道浓郁、颜色深等，不能都换 wealthy。',
 ('He grew up in a wealthy family.','他在一个富裕家庭长大。'),('The project received help from several wealthy donors.','项目得到几位富有捐赠者的帮助。'))
R('B3175','安好、繁荣；财富及丰富资源','WEALTH：从福祉、富足说到拥有的有价值资源','wealth → wealthy；commonwealth 单列公共福祉、共同体的旧义背景，沿用共享精讲。',
 '不是现代 well 与 health 随便拼在一起。旧形成分析保留不确定性；财富、收入和丰富经验用实际场景分清。',
 'wealth 与 weal 同族，含 -th 旧抽象材料；wealth + -y；common + wealth 的旧福祉义。',
 [['财富、富有及公共福祉','wealth · wealthy · commonwealth']],
 'wealth 存量、income 流入；rich 更广，浓咖啡不能一律改 wealthy coffee；commonwealth 不逐字译为共同的钱。',
 'The wealthy collector had a wealth of knowledge about old maps.\n\n那位富有的收藏家对古地图有丰富的知识。','wealth wealthy commonwealth')
if __name__=='__main__':save('continuation_20261030_ce',ROOTS,WORDS)
