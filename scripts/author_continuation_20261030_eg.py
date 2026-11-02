"""Leg, parent and tight: common extensions kept beside their base."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
L=[['古诺斯语 leggr → 中古英语 leg、legge → leg','腿、肢骨、杆状部位 → 腿'],['现代形状与功能引申','桌腿；分段旅程的一段；腿部衣物和形容词']]
W('leg','/leɡ/','腿；桌椅等的腿；行程的一段',
 '身体靠腿支撑、移动，桌子下面支撑它的细长部分也叫腿；旅程从一个点走到下一个点，则可算一段 leg。',
 '经中古英语接古诺斯语 leggr，旧义包括腿、肢骨等。现代不拆成 le + g，桌腿、行程段是词义扩展。',L,
 'a table leg 桌腿，the last leg of the trip 旅程最后一段，stretch your legs 活动一下腿，on its last legs 快撑不住了。',
 'a table leg；the last leg of the journey；stretch your legs；on its last legs。',
 'leg 腿，foot 脚，limb 肢体范围更广；a leg of a trip 是行程一段，不一定真的步行。',
 ('We flew to Rome on the final leg of our trip.','旅程最后一段，我们飞往罗马。'),('One leg of the old table was loose.','旧桌子有一条腿松了。'))
W('bootleg','/ˈbuːtleɡ/','未经授权制作或流通的录音、翻版；私酒；非法制作或贩卖',
 '先想靴筒：旧时把东西藏在靴筒里偷运，后来 bootleg 就常指绕开许可做出来、卖出去的酒或录音。',
 'boot 靴 + leg 腿部、靴筒。原可直接指靴筒，私酒、走私义与藏酒的旧背景相连，后来扩到未经授权的录音等。',L[:1]+[['boot + leg → bootleg〔靴筒〕','靴筒可用于藏物'],['私酒、非法流通 → 未经授权的录音等','从藏运场景扩到许可之外的制作、传播']],
 'a bootleg recording 未经授权的录音，a bootleg copy 翻版，bootleg liquor 私酒；bootleg jeans 又可按靴筒形状说裤脚较宽的裤型。',
 'a bootleg recording；a bootleg copy；bootleg liquor。',
 'bootleg recording 不等于正式发行的 live recording 现场录音；是否现场与是否授权是两回事。',
 ('The shop sold bootleg recordings of old concerts.','那家店出售旧演唱会未经授权的录音。'),('He found a bootleg copy with poor sound quality.','他找到一份音质很差的翻版。'),
 sources=['https://en.wiktionary.org/wiki/bootleg#English','https://www.etymonline.com/word/bootleg'])
W('leggy','/ˈleɡi/','腿长的；植物茎长而细弱的',
 '人显得腿很长，或植物为了找光向上窜、茎拉得细长，都可以用 leggy；不只是在夸身材。',
 'leg + -y，双写 g。由腿部突出、细长的形状扩到植物的细长茎，不是说植物长出人的腿。',L[:1]+[['leg + -y → leggy〔双写 g〕','腿长；借形状说植物茎细长']],
 'a leggy teenager 长腿少年，leggy seedlings 茎细长的幼苗，become leggy 长得细高。',
 'leggy seedlings；a leggy plant；become leggy。',
 'leggy 是外观形容，legged 常在 four-legged 一类组合里表示有几条腿；植物 leggy 往往不是健壮的意思。',
 ('The seedlings became leggy in the dark room.','幼苗在昏暗房间里长得细高。'),('The leggy teenager struggled to fit into the small seat.','那个长腿少年坐进小座位时很局促。'))
W('legless','/ˈleɡləs/','没有腿的；喝得烂醉的〔英式口语〕',
 '字面是没有腿；英式口语里也可夸张说醉得站不稳，像腿不听使唤。两个场景要分开。',
 'leg + -less 没有，早期英语已有相应形式。烂醉义是后来的口语引申，不把饮酒义套回所有动物或人的描述。',L[:1]+[['leg + -less → legless','没有腿'],['后来的英式口语引申','醉得站不稳、烂醉']],
 'a legless lizard 无腿蜥蜴，get legless 喝得烂醉，absolutely legless 烂醉如泥〔口语〕。',
 'a legless lizard；get legless；absolutely legless。',
 'legless lizard 仍是蜥蜴，不因没腿便自动等于 snake；醉酒用法很口语，正式说明可说 very drunk。',
 ('The guide showed us a legless lizard.','向导给我们看了一只无腿蜥蜴。'),('In the comedy, he gets legless at the party.','喜剧里，他在聚会上喝得烂醉。'))
W('legging','/ˈleɡɪŋ/；常见复数 leggings /ˈleɡɪŋz/','护腿、腿套；leggings 紧身裤',
 '给腿套上的衣物。现在买衣服常见复数 leggings，通常指贴身、有弹性的裤装，不是在说某个人正在踢腿。',
 'leg + 名词后缀 -ing，双写 g，形成腿部覆盖物名称；现代服饰多用复数 leggings。这个 -ing 不是每次都表示进行时。',L[:1]+[['leg + 名词 -ing → legging','腿部覆盖物'],['复数 leggings 的现代服饰用法','贴腿裤装、紧身裤']],
 'a pair of leggings 一条紧身裤，wear leggings 穿紧身裤，thermal leggings 保暖紧身裤。',
 'a pair of leggings；wear leggings；thermal leggings。',
 'leggings 和 tights 都可贴身，具体剪裁、厚薄、是否包脚因服装而异；不要仅用一个固定外观给所有款式下定义。',
 ('She wore leggings and a long sweater.','她穿了紧身裤和一件长毛衣。'),('I packed a pair of thermal leggings for the trip.','我为旅行装了一条保暖紧身裤。'))
R('B2769','腿的支撑、细长形状与分段延伸','LEG：身体的一条支撑，也能借给桌子和分段旅程','leg → leggy、legless、legging；bootleg 从靴筒进入私酒、翻版；legroom、legwork 放在实用组合里理解。',
 '同一个腿字可借形状、支撑作用和路程分段产生不同引申，不能一见 leg 就硬译成人的腿。',
 '古诺斯 leggr 经中古英语 → leg；leg + -y/-less/-ing；boot + leg；leg + room/work。',
 [['基础与腿部形容、衣物','leg · leggy · legless · legging'],['空间、跑腿与靴筒分支','legroom · legwork · bootleg']],
 'leg/foot 腿脚不同；leggy 植物可细弱；leggings 服装常复数；bootleg 许可问题与现场录音不是一回事。',
 'The final leg of the trip involved a lot of legwork.\n\n旅程最后一段需要做不少实地跑动的工作。','leg leggy legless legging legroom legwork bootleg')
P=[['拉丁 pariō、parere → parēns、parentem','生出、带来 → 生育者、父母'],['古法语、盎格鲁法语 parent → 中古英语 parent','父母、亲属等 → 现代父母与照顾孩子的人'],['英语动词与派生','parent 抚养 → parenting；parenthood 为人父母的身份、经历']]
W('parent','英 /ˈpeərənt/；美 /ˈperənt/','父亲或母亲；家长；母体、上一级；抚养、教养',
 '一个 parent 是父母中的一位，也可按实际关系指承担养育责任的人。公司、文件夹有 parent，则是在说它是上一级或来源。',
 '经法语接拉丁 parēns、parentem，原是表示生育的动词分词。现代人物关系不限于生物生育，名词再可作动词表示养育。',P,
 'a single parent 单亲家长，a parent company 母公司，the parent folder 上级文件夹，parent a child 抚养孩子。',
 'a single parent；a parent company；the parent folder；both parents。',
 'parent 一位父母，parents 通常复数说父母；transparent 透明的有另一条显现词源，不能按字母 parent 把它编成育儿词。',
 ('A parent came to collect the child after school.','放学后，一位家长来接孩子。'),('The files are stored in the parent folder.','文件存放在上级文件夹里。'),
 sources=['https://en.wiktionary.org/wiki/parent#English','https://www.etymonline.com/word/parent'])
W('parenthood','英 /ˈpeərənthʊd/；美 /ˈperənthʊd/','为人父母的身份、经历',
 '不是一次喂饭或一次辅导，而是进入当父母这种人生角色，以及随之而来的生活经历。',
 'parent + -hood 状态、身份，与 childhood 的词尾同类；hood 在这里不是连帽衫的帽子。',P[:2]+[['parent + -hood → parenthood','为人父母的身份、阶段和体验']],
 'the joys of parenthood 为人父母的喜悦，adjust to parenthood 适应父母身份，early parenthood 初为父母阶段。',
 'adjust to parenthood；the joys of parenthood；early parenthood。',
 'parenthood 侧重角色和经历，parenting 侧重具体养育过程、做法；两者关系密切，镜头位置不同。',
 ('They were still adjusting to parenthood.','他们还在适应初为父母的生活。'),('The book describes the challenges and joys of parenthood.','这本书描写了为人父母的挑战与喜悦。'))
W('parenting','英 /ˈpeərəntɪŋ/；美 /ˈperəntɪŋ/','养育、育儿；养育方式',
 '每天怎么照顾、引导、回应孩子，这些实际做法和过程合起来就是 parenting。',
 'parent 由人物名词作动词，抚养、教养；加 -ing 形成过程名词 parenting。现代常说不同的育儿方式。',P[:2]+[['parent〔名词〕→ parent〔抚养动词〕→ parenting','父母角色 → 实际养育过程、方法']],
 'parenting skills 育儿技能，parenting styles 养育方式，shared parenting 共同养育，a parenting class 育儿课程。',
 'parenting skills；parenting styles；shared parenting；a parenting class。',
 'parenting 不是只指母亲的工作，也不只限于婴儿护理；parenthood 是身份经历，parenting 是如何养育。',
 ('They attended a class on parenting skills.','他们参加了一堂育儿技能课。'),('The article compares different parenting styles.','文章比较了不同养育方式。'))
R('B2650','生育者到现代养育角色，再借作上一级关系','PARENT：人物是父母，动作是养育，结构里是上一级','parent → parenthood、parenting；grandparent 往上一代。',
 '词源的生育画面帮助记忆，现代 parent 还包括实际养育关系；透明 transparent 不属于这个父母分支。',
 'parere → parēns、parentem，经法语 → parent；parent + -hood；parent 作动词 + -ing；grand- + parent。',
 [['角色、经历与日常养育','parent · parenthood · parenting'],['上一代','grandparent']],
 'parent 单数与 parents 复数；parenthood 身份经历与 parenting 过程；transparent 不按现代字母切进本族。',
 'Parenting skills helped them adjust to parenthood.\n\n育儿技能帮助他们适应为人父母的生活。','parent parenthood parenting grandparent')
ROOTS[-1]['exclude']['transparent']='透明一词接显现、看见的另一条词源，不是现代 parent 父母的派生。'
T=[['北欧语、古英语表示密实的相关词 → 中古英语 thight、tight 等','密、实、贴合'],['tight 的现代扩展','绷紧、衣物紧；时间资金紧；比赛接近'],['常用派生与组合','tightly、tightness；tighten；tights 衣物；tightrope 绷紧的绳']]
W('tight','/taɪt/','紧的、绷紧的；严密的；时间、钱等紧张的；势均力敌的',
 '先抓住空隙很少：绳子不松、衣服贴身、安排没空档、预算没余地，都能用 tight。比赛双方差距很小，也说 tight。',
 '中古英语 thight、tight 等接北欧语、古英语密实词族，后来词形和旧动词互有影响。gh 不发音，不按 sight 的意思拆。',T,
 'a tight knot 紧结，a tight budget 紧预算，a tight schedule 紧安排，a tight race 竞争接近，sit tight 留在原处等待。',
 'a tight knot；a tight budget；a tight schedule；a tight race；sit tight。',
 'tight 核心是紧、余地小，close 另有近等范围；tight budget 不是钱很多，而是可调配的钱不宽裕。',
 ('The lid was too tight to open easily.','盖子拧得太紧，不容易打开。'),('We are working to a tight schedule.','我们的工作安排很紧。'),
 sources=['https://en.wiktionary.org/wiki/tight#English','https://www.etymonline.com/word/tight'])
W('tightly','/ˈtaɪtli/','紧紧地、紧密地、严密地',
 '把紧这个状态放到动作上：握得紧、包得紧、排得密，都是动作进行的方式。',
 'tight + -ly 形成副词；不是把 ly 当作一个新的紧词根。',T[:2]+[['tight + -ly → tightly','以紧、密、牢的方式']],
 'hold tightly 紧握，tightly packed 挤得密实，tightly controlled 严格控制，tightly sealed 密封严实。',
 'hold tightly；tightly packed；tightly controlled；tightly sealed。',
 'tight 作形容词，tightly 常修饰动作；某些固定表达 hold tight、sit tight 也保留 tight 的副词用法。',
 ('She held the rope tightly.','她紧紧抓着绳子。'),('The books were tightly packed in the box.','书在箱子里塞得很密实。'))
W('tighten','/ˈtaɪtən/','拧紧、拉紧；收紧、加强限制；变紧',
 '原来有松动、余地，现在把它收小：拧螺丝、拉绳子、收紧规则，都可用 tighten。',
 '现代可清楚按 tight + 动词 -en 理解。更早还有接古英语 tyhtan 的动词，旧形式与现代 tight、tighten 的历史互相交织，不能把全部年代都简化成刚加一个后缀。',
 T[:1]+[['旧动词 tight、tighten 等与现代形容词相互影响','较早动词另有古英语 tyhtan 背景'],['现代 tight + -en 的透明构词关系','使变紧、变紧；用于实物或限制']],
 'tighten a screw 拧紧螺丝，tighten a rope 拉紧绳子，tighten security 加强安保，tighten the rules 收紧规则。',
 'tighten a screw；tighten a rope；tighten security；tighten the rules。',
 'tighten 可及物也可不及物：tighten the rope / the rope tightens；loosen 松开与之相对。',
 ('Tighten the screw with a screwdriver.','用螺丝刀把螺丝拧紧。'),('The school tightened its rules on late arrivals.','学校收紧了迟到规定。'),
 sources=['https://en.wiktionary.org/wiki/tighten#English','https://www.etymonline.com/word/tighten'])
W('tightness','/ˈtaɪtnəs/','紧度、紧绷感；紧张、余地少的状态',
 '不说具体去拉、去拧，而是把有多紧、处于紧状态这件事当名词。绳子、衣服、预算都可能有自己的紧。',
 'tight + -ness 状态名词。抽象场景沿 tight 的时间、资金余地小等用法延伸。',T[:2]+[['tight + -ness → tightness','紧的性质、程度或感受']],
 'check the tightness 检查松紧，the tightness of the knot 结的紧度，budget tightness 预算紧张。',
 'check the tightness；the tightness of the knot；budget tightness。',
 'tightness 状态名词，tighten 动作；tightness 不自动说明为什么紧，原因需要看后文。',
 ('Check the tightness of the knot before lifting the box.','提箱子前，检查绳结是否够紧。'),('The tightness of the budget left little room for changes.','预算紧张，几乎没有调整余地。'))
W('tights','/taɪts/','紧身裤、连裤袜〔具体款式依语境〕',
 '贴腿穿的衣物，用复数形式说整件，一件常说 a pair of tights；不是很多个紧的状态。',
 'tight 紧、贴身 + -s，衣物名称沿紧贴外观形成。现代英美、运动与日常服装的具体指向有差异。',T[:2]+[['tight + -s → tights〔服装复数名词〕','贴身的腿部衣物']],
 'a pair of tights 一条紧身裤或连裤袜，running tights 跑步紧身裤，opaque tights 不透明连裤袜。',
 'a pair of tights；running tights；opaque tights。',
 'tights 常按复数搭配 these tights are；leggings 也贴身，需看实际款式，不能只凭是否包脚给全部产品一刀切。',
 ('She wore black tights with the dress.','她穿着黑色连裤袜配那条连衣裙。'),('These running tights are comfortable in cold weather.','天冷时穿这条跑步紧身裤很舒服。'))
W('tightrope','英 /ˈtaɪtrəʊp/；美 /ˈtaɪtroʊp/','绷紧的表演绳索；必须谨慎维持的平衡',
 '人踩在拉直绷紧的绳上，一边偏多就可能失衡；所以 walk a tightrope 可说在两种压力之间小心拿捏。',
 'tight 绷紧 + rope 绳，先是走绳表演的实际绳索，再借危险平衡的画面说处理复杂局面。',T[:1]+[['tight + rope → tightrope','绷紧的绳索'],['walk a tightrope 的比喻','两边都不能偏过头，谨慎维持平衡']],
 'walk a tightrope 走钢丝、谨慎平衡，a tightrope walker 走绳表演者，a political tightrope 政治上的艰难平衡。',
 'walk a tightrope；a tightrope walker；a political tightrope。',
 'tightrope 中 rope 本义是绳索，中文常译走钢丝；比喻的重点是平衡困难，不是任何困难都必须翻成一根钢丝。',
 ('The performer walked slowly across the tightrope.','表演者慢慢走过绷紧的绳索。'),('The manager walked a tightrope between saving money and keeping staff.','经理在节省开支与留住员工之间小心维持平衡。'))
R('B3912','空隙小、绷得紧，再说余地少','TIGHT：实物不松，安排、资金也没多少松动空间','tight → tightly、tightness、tighten；tights 是衣物，tightrope 是绷紧的绳，再分 airt​ight、watertight、skintight。'.replace('air\u200btight','airtight'),
 '紧预算不等于有钱，紧比赛是双方差距小；tighten 的现代拆分清楚，更早动词背景另外交代。',
 '密实词族 → 中古英语 tight；tight + -ly/-ness/-en；tight + -s/rope；air/water/skin + tight。',
 [['基础状态、方式和变化','tight · tightly · tightness · tighten'],['服装与绳索','tights · tightrope'],['紧密的具体范围','airtight · watertight · skintight']],
 'tighten/loosen 收紧松开；tightness 状态非动作；tights 复数衣物；tightrope 比喻两难平衡。',
 'Tighten the rope and check that the knot is tight.\n\n拉紧绳子，再检查绳结是否牢靠。','tight tightly tightness tighten tights tightrope airtight watertight skintight')
if __name__=='__main__':save('continuation_20261030_eg',ROOTS,WORDS)
