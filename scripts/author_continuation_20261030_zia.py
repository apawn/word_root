"""Common lexical gaps: people, shelter, ballots, household objects and food."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
def S(word,base):
 return ['https://en.wiktionary.org/wiki/'+word+'#English','https://www.etymonline.com/word/'+base]
EXISTING_ROOT_ADDITIONS={
 'C0401':dict(words='sheriff sheriffs'.split(),label='sheriff：另源的地方长官、县警长',note='与 officer 比较职务称谓，不从拉丁 officium 派生。sheriff 承古英语 scirgerefa，即 shire 辖区与 gerefa 长官的旧组合，后经缩合。'),
 'B3913':dict(words='haven havens'.split(),label='haven：港口到避风港',note='与 shelter 比较庇护，不是现代 shelter 的派生。haven 承古英语 hæfen 与北欧港口材料，远源有抓住、海等不同分析，不定为 have 加 -n。'),
 'B2610':dict(words='darling darlings'.split(),label='darling：被珍爱的那个人',note='承古英语 deorling、dyrling，被珍爱的人，接 dear 的旧形式与小称材料；元音历史变化成 dar-，末尾不是现代动词的 -ing。'),
 'B2644':dict(words='ore ores'.split(),label='ore：矿石与金属旧词的汇合',note='与 earth 比较地下矿物材料。ore 包含古英语 ora 矿石与 ar 铜、青铜等旧词的汇合；不能直接写成现代 earth 截短。'),
 'C1660':dict(words='ballot ballots'.split(),label='ballot：投票小球到选票',note='与 vote 比较投票行为，不接拉丁 votum 发愿词根。ballot 经意大利小球名，接把小球用作秘密投票标记的习惯，后来扩到纸票。'),
 'B2954':dict(words='cemetery cemeteries'.split(),label='cemetery：另源的安睡之地',note='和 sleep 比较死亡如长眠的历史比喻；cemetery 经法语、拉丁接希腊 koimeterion 睡处、宿舍，不由英语 sleep 直接构词。'),
 'B4083':dict(words='hull hulls'.split(),label='hull：外壳、船体与去壳',note='和 shell 比较外层覆盖，不是现代 shell 的派生。种壳 hull 承古英语 hulu；船体一支有种荚形状比喻、与船舱词混合等不同分析。'),
 'B2739':dict(words='pillow pillows'.split(),label='pillow：枕头与枕靠',note='与 bed 比较寝具，不是 bed 的派生。pillow 承古英语 pyle，较早日耳曼形式借自拉丁 pulvinus 软垫，更远来历未定。'),
 'B3019':dict(words='towel towels'.split(),label='towel：洗后擦干的布',note='和 cloth 比较布的用途，不是 cloth 派生。towel 经古法语 toaille，接法兰克等日耳曼洗涤相关材料；后来名词又成用毛巾擦的动词。'),
 'C1580':dict(words='garlic'.split(),label='garlic：另源的蒜，与 onion 比较',note='这里与 onion 比较葱蒜类食物，不接拉丁 unus 一。garlic 承古英语 gar 矛 + leac 葱蒜类植物的旧组合，不能把 -lic 当现代通用后缀。'),
 'B3219':dict(words='spa spas'.split(),label='spa：地名到温泉、护理场所',note='和 bath 比较沐浴场所，不是 bath 派生。spa 接比利时温泉镇 Spa 的地名，再通称温泉地、护理机构；不是拉丁词组首字母缩写。'),
}
SHERIFF=[['古英语 scir 辖区 + gerefa 长官 → scirgerefa','辖区里的王权代表'],['中古英语 shir-reve 等 → sheriff','现代按地区制度指县警长、司法或礼仪官员等']]
HAVEN=[['古英语 hæfen 与北欧港口材料 → haven','更远抓住、海等分析未统一'],['港口 → 庇护所、避风港','从船能躲风浪，借说人能安稳待着的地方']]
DARLING=[['古英语 deor、dyre 亲爱的旧形式 + 小称材料','deorling、dyrling：被珍爱的人'],['中古英语 dereling 等 → darling','元音发生历史变化，名词再可作可爱的形容词']]
ORE=[['古英语 ora 矿石，与 ar 铜、青铜等材料汇合','不同旧词在形式、意义上逐渐混合'],['英语 ore：可从中提炼金属的矿石','通常按材料不可数，ores 可分别数矿石种类']]
BALLOT=[['意大利语小球名 → ballot','小球曾用作秘密投票的计数标记'],['投票小球、投票方式 → 纸选票等','现代保留名称，不要求投票真的用球']]
CEMETERY=[['希腊 koimeterion 睡处、宿舍 ← koiman 使睡下','死亡如安睡的旧比喻接入墓地称呼'],['拉丁 coemeterium 等 → 法语 cimetiere → cemetery','现代墓地、墓园，不能译成一般睡觉的旅馆']]
HULL=[['古英语 hulu 种壳、荚 → hull','接更早覆盖、隐藏材料'],['壳；去壳；另有船体义','船体有种荚比喻等分析，不能定成唯一证实路线']]
PILLOW=[['拉丁 pulvinus 软垫 → 较早日耳曼借词','古英语 pyle → 中古英语 pilwe'],['pillow 枕头 → 动词枕靠','器具名词再用来说把头搁在某物上']]
TOWEL=[['法兰克等日耳曼洗涤材料 → 古法语 toaille','英语经法语借入，不是现代 wash 的直接派生'],['英语 towel 毛巾 → 用毛巾擦干','名词再成为动作名称']]
SPA=[['比利时地名 Spa：以矿泉著名的地方','地名接瓦隆语泉、喷泉材料'],['地名 → 温泉、温泉疗养地 → 护理机构','现代 spa 不必都有天然温泉']]
W('sheriff','英 /ˈʃerɪf/；美 /ˈʃerɪf/','县警长〔美国等〕；地方行政、司法官员〔依地区制度〕',
 '西部片里带着警徽、负责县里治安的 sheriff，常译县警长。这个词本来是“某个辖区的长官”，不同地区后来保留了不同职责。',
 '古英语 scir 辖区 + gerefa 长官 → scirgerefa，经中古英语 shir-reve 等逐渐缩合成 sheriff。不是现代几个字母随意删出来的构词。',SHERIFF,
 '美国故事里常是县级执法负责人；英国等语境须看具体地区制度，不能把所有 sheriff 都理解成西部片里的同一岗位。',
 'the county sheriff；the sheriff’s office；a deputy sheriff。',
 'sheriff 是具体职务，police officer 是较广的警务人员称呼；deputy sheriff 则常是副警长、县警人员，不是每个人都担任 sheriff。',
 ('The sheriff spoke to the reporters outside the office.','警长在办公室外向记者们讲话。'),('In the film, the sheriff keeps watch over a small frontier town.','电影里，警长守护着一座边境小镇。'),sources=S('sheriff','sheriff'))
W('sheriffs','/ˈʃerɪfs/','县警长、相关地方官员〔复数〕',
 '几个县各有自己的负责人，放在一起就可说 sheriffs；不表示同一个县必然有几位同等职位的警长。',
 'sheriff + -s，/f/ 后读 /s/，保留 ff；不像 leaf → leaves 那样把 f 改 v。',SHERIFF+[['sheriff + -s → sheriffs','多位持有相应职务的人']],
 'county sheriffs 常用于多个县的负责人；具体职责仍随地区、制度不同。',
 'local sheriffs；county sheriffs；a meeting of sheriffs。',
 'sheriffs 是职务复数，sheriff’s 带撇号通常是单数所有格；the sheriffs’ meeting 才可表示多位警长的会议。',
 ('The county sheriffs attended a regional meeting.','各县警长参加了一场地区会议。'),('The museum displays portraits of former sheriffs.','博物馆陈列着几位前任地方长官的肖像。'),sources=S('sheriffs','sheriff'))
W('haven','/ˈheɪvən/','避风港；庇护所；令人安心、适宜的地方',
 '外面风浪大，船可以躲进港；生活里有个能让人安静下来、安全待着的地方，就像 a haven。它不必真在海边。',
 '承古英语 hæfen 港口，与北欧港口词相关；更远来源有不同分析。港口能庇护船只，词后来常用来指庇护、安全之所。',HAVEN,
 'a safe haven 是安全避难处；a haven for birds 是让鸟容易栖居的地方，也可把安静花园比成城市里的避风港。',
 'a safe haven；a haven for wildlife；a haven of peace。',
 'haven 读 /ˈheɪvən/，heaven 天堂读 /ˈhevən/；意思可以同样美好，但元音、拼写都不同。',
 ('The garden became a haven of peace in the busy city.','那座花园成了喧闹城市里一处宁静的避风港。'),('The wetlands provide a haven for birds.','湿地给鸟类提供了庇护之所。'),sources=S('haven','haven'))
W('havens','/ˈheɪvənz/','避风港、庇护所、安稳去处〔复数〕',
 '城市里几处安静公园，或候鸟沿途能歇脚的几块湿地，都可看作 havens。数的是让人或动物有保护、有喘息的地方。',
 'haven + -s，/n/ 后读 /z/；现代复数保留港口到庇护所的比喻，不另添一个词源分支。',HAVEN+[['haven + -s → havens','多处可庇护、令人安稳的地方']],
 'safe havens、wildlife havens 都可使用；具体是否足够安全，是情境事实，不是词尾本身保证。',
 'quiet havens；havens for wildlife；havens of calm。',
 'havens 是地点、环境，heavens 是天堂、天空的另一词复数；先听清 /eɪ/ 与 /e/。',
 ('Small parks can be havens of calm in crowded cities.','小公园可以成为拥挤城市里的宁静去处。'),('The islands are havens for nesting birds.','那些岛屿是鸟类筑巢的庇护地。'),sources=S('havens','haven'))
W('darling','英 /ˈdɑːlɪŋ/；美 /ˈdɑrlɪŋ/','亲爱的、宝贝；宠儿；可爱的',
 '把一个人看得珍贵，亲昵地叫一声 darling，就像中文的亲爱的、宝贝。the darling of the press 又是媒体特别宠爱、追捧的人。',
 '承古英语 deorling、dyrling 被珍爱的人，接 dear 的旧形式与小称材料。历史元音变成 dar-；最后的 -ing 不是现代动词正在做的后缀。',DARLING,
 'my darling 是亲密称呼；a media darling 是媒体宠儿；a darling little house 用作形容词，有可爱、讨人喜欢的语气。',
 'my darling；a media darling；a darling child。',
 'darling 是情感称呼、宠儿名词或可爱的形容词，dearly 常作副词；love someone dearly 不能直接换成 love someone darling。',
 ('Good morning, darling.','早上好，亲爱的。'),('The young actor quickly became a media darling.','那位年轻演员很快成了媒体宠儿。'),sources=S('darling','darling'))
W('darlings','英 /ˈdɑːlɪŋz/；美 /ˈdɑrlɪŋz/','宝贝们、亲爱的人们；宠儿〔复数〕',
 '父母亲昵地叫孩子们 darlings，是把每个人都当宝贝；某个行业眼下热捧的几家公司，也可能被写成行业的 darlings。',
 'darling + -s，/ŋ/ 后读 /z/；基础词本来是被珍爱的人，现代按普通名词成复数。',DARLING+[['darling + -s → darlings','多个被宠爱、追捧的人或事物']],
 'my darlings 多是亲密称呼；the darlings of 某群体 指该群体特别喜欢的对象。',
 'my darlings；the darlings of the press；everyone’s darlings。',
 'darlings 作公开称呼可能显得亲昵或戏剧化，语气取决于关系；不是所有正式场合都像 children、colleagues 那样中性。',
 ('Come inside, my darlings; dinner is ready.','进来吧，宝贝们，饭好了。'),('The two singers became the darlings of the music press.','那两位歌手成了音乐媒体热捧的宠儿。'),sources=S('darlings','darling'))
W('ore','英 /ɔː/；美 /ɔr/','矿石；可从中提炼金属的矿物材料',
 '从山里挖出来的还不是一块纯铁，而是含着铁的岩石材料，叫 iron ore。它是原料，需要再加工，才可能得到金属。',
 '由古英语 ora 矿石、未加工金属，与 ar 铜、青铜等旧词逐渐汇合。现代形与义承接不同旧材料，不把它简化成 earth 的缩短。',ORE,
 'iron ore、copper ore 指含相应金属的矿石；通常按材料不可数，a piece of ore 数一块。',
 'iron ore；copper ore；extract metal from ore。',
 'ore 是含有可提取成分的原料，metal 是金属；不是每块岩石都能叫 ore，也不是挖到 ore 就已经得到纯金属。',
 ('The mine produces iron ore.','那座矿山出产铁矿石。'),('Metal is extracted from the ore at the plant.','工厂从矿石中提取金属。'),sources=S('ore','ore'))
W('ores','英 /ɔːz/；美 /ɔrz/','矿石种类；不同矿石材料〔复数〕',
 '不是单纯数三块石头，而是在比较不同种类、不同成分的矿石时，常用 ores。材料名词在分种类时，也能有复数。',
 'ore + -s，读 /z/；不可数材料的分类用法，表示不同矿石类型。末尾 e 保留，不增加音节。',ORE+[['ore + -s → ores','按种类、性质分别看的矿石材料']],
 'metal ores、different ores 常用于讨论矿石类别；数小块时可用 pieces、samples。',
 'different metal ores；copper-bearing ores；samples of ores。',
 'three pieces of ore 是三块样品，可以同一种；three ores 常是在说三种不同矿石，计数对象不同。',
 ('The display includes several metal ores.','展柜中有几种金属矿石。'),('Different ores require different processing methods.','不同矿石需要不同的加工方法。'),sources=S('ores','ore'))
W('ballot','英 /ˈbælət/；美 /ˈbælət/','选票；无记名投票；投票表决',
 '把选择悄悄放进箱子，是 ballot 很直观的画面。早年放进去的真可以是小球，后来换成纸票，名称保留了下来。',
 '接意大利语小球名，小球用作秘密投票的计数标记；英语后来把名称扩到纸票、投票方式。不是现代 ball 随手加 -ot 就完成了全部历史。',BALLOT,
 'cast a ballot 是投票；a secret ballot 是无记名投票；ballot members 作动词可说让会员投票表决。',
 'a ballot paper；a ballot box；cast a ballot；a secret ballot。',
 'vote 是更广的投票、表态，ballot 强调选票或相应投票程序；举手表决可以叫 vote，不一定是 secret ballot。',
 ('She placed her ballot in the box.','她把选票投入了箱子。'),('The members chose a leader by secret ballot.','会员们通过无记名投票选出了一位负责人。'),sources=S('ballot','ballot'))
W('ballots','/ˈbæləts/','选票；多次投票表决〔复数〕；让人投票〔第三人称单数〕',
 '箱里一张张票是 ballots；第一轮没选出来，再进行几轮，也可以数 rounds、ballots。不要把一张选票和一场投票当成相同计数。',
 'ballot + -s，/t/ 后读 /s/；选票复数、表决轮次复数以及动词三单同形。',BALLOT+[['ballot + -s → ballots','多张选票、多轮表决；或某组织让人投票']],
 'count the ballots 是计票；several ballots may be needed 可以是需要几轮表决，意思随搭配改变。',
 'paper ballots；count the ballots；spoiled ballots。',
 'ballots 可按张数选票，voters 按人数数投票者；一场选举还可能给同一人多张不同议题的票。',
 ('The officials counted the ballots after the polls closed.','投票结束后，工作人员清点了选票。'),('The box contained hundreds of paper ballots.','箱子里有几百张纸选票。'),sources=S('ballots','ballot'))
W('cemetery','英 /ˈsemətri/；美 /ˈseməteri/','墓地；墓园',
 '一片专门安葬、纪念逝者的地方，是 cemetery。名字更早把死亡委婉地比作安睡，所以像在说安睡之地。',
 '希腊 koimeterion 原有睡处、宿舍义，接 koiman 使睡下；经拉丁 coemeterium 等、法语 cimetiere 借入。安睡的旧比喻走向墓地称呼，现代不指普通宿舍。',CEMETERY,
 'visit a cemetery 是去墓园；a cemetery gate 是墓园大门。拼写三处都是 e：cemetery，不写成 cemetary。',
 'an old cemetery；a military cemetery；the cemetery gates。',
 'grave 是一座具体坟墓，cemetery 是安葬的整片场地；graveyard 常让人联想到教堂附近墓地，但使用范围有重叠。',
 ('They walked quietly through the old cemetery.','他们静静地走过那座旧墓园。'),('The cemetery lies on a hill outside the town.','墓园位于镇外的一座小山上。'),sources=S('cemetery','cemetery'))
W('cemeteries','英 /ˈsemətriz/；美 /ˈseməteriz/','墓地、墓园〔复数〕',
 '城里的几处墓园，是 cemeteries；每处可能有很多坟墓。数的是整个场地，不是里面每一块墓碑。',
 'cemetery 的 y 改 i 加 -es → cemeteries，词尾读 /z/；词干仍保留 cemetery 那组 e 的拼写。',CEMETERY+[['cemetery → cemeteries','y 改 i 加 -es，多个安葬场地']],
 'historic cemeteries 说有历史的墓园；几座不同地点的墓园可用 several cemeteries。',
 'historic cemeteries；public cemeteries；maps of cemeteries。',
 'cemeteries 数墓园，graves 数坟墓，gravestones 数墓碑；一处 cemetery 内可以有许多 graves。',
 ('The guide describes several historic cemeteries.','指南介绍了几处历史悠久的墓园。'),('Volunteers recorded the inscriptions in two cemeteries.','志愿者记录了两处墓园里的碑文。'),sources=S('cemeteries','cemetery'))
W('hull','/hʌl/','谷物等的外壳；船体；去掉外壳、蒂等',
 '把东西外面的包覆层留下来看，是 hull 的好画面：粮食有壳，船有包围内部空间的主体。食谱 hull strawberries 则是去草莓顶部的蒂。',
 '种壳义承古英语 hulu，接日耳曼覆盖材料。船体义有种荚外形比喻、与旧船舱词混合等分析；去壳动词由外壳名词形成，不把所有义确定成一条单线。',HULL,
 'the hull of a ship 是船体，不含每个上层装置；hull grain 是去壳；hull strawberries 是去蒂，不是剥掉整层果皮。',
 'a wooden hull；the ship’s hull；hull the strawberries。',
 'hull 常说船的主要外部结构，deck 是甲板；船体与人在上面行走的平台不是同一个部位。',
 ('The boat has a wooden hull.','那艘船有木质船体。'),('Wash and hull the strawberries before slicing them.','把草莓洗净、去蒂，再切片。'),sources=S('hull','hull'))
W('hulls','/hʌlz/','外壳、船体〔复数〕；去壳、去蒂〔第三人称单数〕',
 '加工后剩下的一堆稻壳，是 rice hulls；船厂里几艘船的主体，是 hulls。共同的外层画面有帮助，但不能替代各支的历史核对。',
 'hull + -s，/l/ 后读 /z/；名词复数与动词三单同形。',HULL+[['hull + -s → hulls','多个外壳、船体；或某人去掉壳、蒂']],
 'rice hulls 数或统称稻壳材料；boat hulls 数船体，hulls strawberries 是给草莓去蒂的动作。',
 'rice hulls；damaged hulls；hulls the berries。',
 'hulls 与 whole ships 不等同：一艘船的 hull 是主要船体，不能把引擎、帆等都算作这个词直接命名的部件。',
 ('The yard repairs damaged boat hulls.','那家船厂修理受损船体。'),('Rice hulls were piled beside the mill.','碾米厂旁堆着稻壳。'),sources=S('hulls','hull'))
W('pillow','英 /ˈpɪləʊ/；美 /ˈpɪloʊ/','枕头；枕靠、搁在柔软支撑上',
 '躺下时让脑袋有个软软的支撑，是 pillow。作动词，pillow your head on something 就是把头枕在上面，那个东西未必真是枕头。',
 '承古英语 pyle，经更早日耳曼借词接拉丁 pulvinus 软垫，更远来历未定。英语后来由枕头名词发展出枕靠动词。',PILLOW,
 'a soft pillow 是软枕；pillow your head on your arm 是枕着手臂；pillow talk 常说床上的亲密闲谈。',
 'a feather pillow；a pillow on the bed；pillow your head on your arm。',
 'pillow 常给头部支撑，cushion 更广，可是坐垫、靠垫；用途重叠但不总是一件东西。',
 ('She put a fresh cover on the pillow.','她给枕头换上了干净枕套。'),('She used a folded coat as a pillow.','她把折好的外套当枕头。'),sources=S('pillow','pillow'))
W('pillows','英 /ˈpɪləʊz/；美 /ˈpɪloʊz/','枕头〔复数〕；把头枕靠〔第三人称单数〕',
 '床头叠着几只枕头，是 pillows。数的是有填充、能垫头的东西，外面套着的布套要另说 pillowcases。',
 'pillow + -s，读 /z/；名词复数与动词三单同形。末尾 ow 是基础词拼写，不因加 s 改变。',PILLOW+[['pillow + -s → pillows','多个枕头；或某人把头枕靠']],
 'extra pillows 是多备的枕头；a pile of pillows 是一堆枕头；不同软硬也可叫 firm、soft pillows。',
 'soft pillows；extra pillows；a pile of pillows。',
 'pillows 是枕头本体，pillowcases 是枕套；换洗布套不一定意味着换掉里面的枕芯。',
 ('There are extra pillows in the cupboard.','柜子里有备用枕头。'),('She stacked the pillows at the head of the bed.','她把枕头叠在床头。'),sources=S('pillows','pillow'))
W('towel','/ˈtaʊəl/','毛巾、浴巾；用毛巾擦干',
 '洗完后用一块吸水的布把水擦掉，这块布是 towel；动作也可直接叫 towel off，省得再说用什么擦。',
 '经古法语 toaille 借入，较远接法兰克等日耳曼洗涤相关词。名词毛巾较早，英语后来把它用作拿毛巾擦干的动词。',TOWEL,
 'a bath towel 是浴巾；a hand towel 是擦手巾；throw in the towel 借拳击中认输的动作表示放弃。',
 'a clean towel；a bath towel；towel yourself dry；throw in the towel。',
 'towel 按擦干用途命名，cloth 是更广的布、布块；纸质擦手用品可说 paper towel，不是每一条 towel 都必须是织布。',
 ('She dried her hands on a clean towel.','她用一条干净毛巾擦干双手。'),('After several failed attempts, he refused to throw in the towel.','失败几次后，他仍不肯放弃。'),sources=S('towel','towel'))
W('towels','/ˈtaʊəlz/','毛巾、浴巾、擦手巾〔复数〕；用毛巾擦干〔第三人称单数〕',
 '浴室里挂着几条毛巾，是 towels；厨房里的 paper towels 也用这个复数，数的是擦拭用品。',
 'towel + -s，/l/ 后读 /z/；基础词常读两个音节，复数只增加 /z/。',TOWEL+[['towel + -s → towels','多条、张擦干用品；或某人用毛巾擦']],
 'fresh towels 是干净新换的毛巾；paper towels 是擦手纸、厨房纸等；rolls of paper towels 数卷。',
 'clean towels；bath towels；paper towels。',
 'towels 是毛巾本身，towel rails 是挂毛巾的杆；一个在数擦拭用品，一个在数架子。',
 ('Fresh towels are on the bathroom shelf.','干净毛巾放在浴室架子上。'),('We used paper towels to wipe up the water.','我们用厨房纸把水擦干了。'),sources=S('towels','towel'))
W('garlic','英 /ˈɡɑːlɪk/；美 /ˈɡɑrlɪk/','大蒜；蒜',
 '一整头里分成好几瓣，拍碎后有明显蒜香，这就是 garlic。英语通常把它当食材整体说，要数一瓣就加 clove。',
 '承古英语 garlec、garleac，由 gar 矛 + leac 葱蒜类植物的旧组合形成。矛的形状联想藏在旧命名里，现代 -lic 不作为普通蒜类后缀自由使用。',
 [['古英语 gar 矛 + leac 葱蒜类植物 → garleac','旧名带尖、矛形的形状联想'],['中古英语 garlek 等 → garlic','现代食材名通常不可数，用 clove、head 数瓣、头']],
 'a clove of garlic 是一瓣，a head of garlic 是一头；minced garlic 是蒜末，garlic bread 是蒜香面包。',
 'fresh garlic；a clove of garlic；garlic bread；crushed garlic。',
 'garlic 常不可数，two cloves of garlic 才明确是两瓣；clove 单独还可指丁香这种香料，需看食谱对象。',
 ('Add two cloves of garlic to the pan.','往锅里放两瓣蒜。'),('The kitchen smelled of roasted garlic.','厨房里弥漫着烤蒜的香气。'),sources=S('garlic','garlic'))
W('spa','英 /spɑː/；美 /spɑ/','温泉、温泉疗养地；水疗、美容护理场所',
 '从有矿泉的度假小镇，到提供泡浴、按摩、护理的场所，spa 的名字跟着场景扩展了。今天一家 spa 未必坐落在天然温泉旁。',
 '来自比利时温泉镇 Spa 的地名，地名接瓦隆语泉、喷泉材料。地名先被通用为温泉地，再扩到现代护理机构；不是把一句拉丁语取三个首字母。',SPA,
 'a spa town 是温泉小镇，a hotel spa 是酒店里的护理设施；a spa day 通常是去享受护理、放松的一天。',
 'a spa town；a hotel spa；a day at the spa。',
 'spa 是场所或相应服务场景，massage 是按摩项目；一家 spa 可以提供 massage，但两个词不互为完整定义。',
 ('The old spa town is known for its mineral springs.','那座古老温泉小镇以矿泉著称。'),('They spent a relaxing afternoon at the hotel spa.','他们在酒店水疗中心度过了一个放松的下午。'),sources=S('spa','spa'))
W('spas','英 /spɑːz/；美 /spɑz/','温泉疗养地、水疗护理场所〔复数〕',
 '几处温泉度假地，或城里几家护理场所，是 spas。它数机构、地方，不规定每家都有一样的项目。',
 'spa + -s，元音后读 /z/；基础词尾 a 保留，不需要加 -es。',SPA+[['spa + -s → spas','多个温泉地、护理机构']],
 'hotel spas 是酒店里的水疗护理场所；historic spas 可说历史上的温泉地，具体时代和服务有差别。',
 'hotel spas；mineral spas；several local spas。',
 'spas 数场所，treatments 数护理项目；一家 spa 可以提供 many treatments，不是一个项目就一家机构。',
 ('Several hotels have their own spas.','几家酒店都有自己的水疗护理设施。'),('The guide lists historic spas across the region.','指南列出了该地区多处历史悠久的温泉疗养地。'),sources=S('spas','spa'))
def extend_lessons():
 extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_zia',ROOTS,WORDS)
 extend_lessons()
