"""Weight and birth: concrete pictures, real histories and grouped extensions."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
WE=[['古英语 wiht、gewiht → 中古英语 weight → weight','重量；与 weigh 称重同族'],['现代 weight','重的量 → 影响力、重要性；也指训练负重']]
def H(f,m):return WE+[[f,m]]
W('weight','/weɪt/','重量、体重；重物；分量、重要性',
 '放上秤看多重，是实际重量；一个人的话能影响决定，就像在天平上很有分量。',
 '继承古英语 wiht、gewiht 等，与 weigh 同族，现代可对应 weigh + 旧名词成分 -t。不是 wait 等待，也不把 gh 当一个有意义的新词根。',WE,
 'the weight of a bag 包的重量，lift weights 举重物训练，carry weight 有影响力，give weight to 重视。',
 'body weight；lift weights；carry weight；give weight to。',
 '日常公斤数常叫 weight；物理中 mass 质量与 weight 重力不同。weight 作动词也可指加权、加重，不等于 weigh 称重。',
 ('What is the maximum weight for this suitcase?','这只行李箱的重量上限是多少？'),('Her opinion carries a lot of weight with the committee.','委员会很重视她的意见。'))
W('weighty','/ˈweɪti/','沉重的；重要、需认真考虑的',
 '一块东西重得压手，一项决定也可能重得不能随便处理。',
 'weight + -y，现代性质形容词，中古英语已有相应形式。抽象重要义利用有分量的共同画面。',H('weight + -y → weighty','有重量 → 沉重；重大'),
 'a weighty volume 厚重书册，weighty matters 重大事情，a weighty decision 重大决定。',
 'a weighty decision；weighty matters；a weighty volume。',
 'weighty 常强调分量与重要性，heavy 搭配更广；heavy rain 大雨通常不说 weighty rain。',
 ('The meeting dealt with several weighty matters.','会议处理了几件重大事项。'),('He lifted a weighty volume from the shelf.','他从书架上拿下一册厚重的书。'))
W('overweight','英 /ˌəʊvəˈweɪt/；美 /ˌoʊvərˈweɪt/','超过规定重量的；体重超标的',
 '重过了眼前采用的上限或参照标准；可以是包裹，也可以是身体状况描述。',
 'over- 超出 + weight，形容词按重量过高理解。说人体时常译超重，具体判定不由这个词单独给出。',H('over- + weight → overweight','超过参考重量 → 超重'),
 'overweight baggage 超重行李，an overweight parcel 超重包裹；词义是比较关系，先看标准。',
 'overweight baggage；an overweight parcel；slightly overweight。',
 'overweight 重量超，oversize 尺寸超；小箱子也可能很重，大箱子也可能很轻。',
 ('The airline charged extra because the bag was overweight.','航空公司因行李超重加收费用。'),('The parcel was overweight for the selected service.','包裹超过了所选服务的重量上限。'))
W('underweight','英 /ˌʌndəˈweɪt/；美 /ˌʌndərˈweɪt/','低于应有、规定重量的；体重不足的',
 '不是普通地轻，而是比某个应有或标明的重量少。',
 'under- 不足 + weight，与 overweight 构成方向对照。对象可以是人、动物或商品。',H('under- + weight → underweight','低于参考重量 → 重量不足'),
 'an underweight package 重量不足的包装商品，an underweight animal 体重不足的动物。',
 'slightly underweight；an underweight package；underweight for its age。',
 'underweight 比标准不足，light 只是轻；小巧物件很轻，不一定包装缺斤少两。',
 ('The inspection found several underweight packages.','检查发现几包商品重量不足。'),('The rescued animal was underweight when it arrived.','获救动物刚送来时体重不足。'))
W('counterweight','英 /ˈkaʊntəweɪt/；美 /ˈkaʊntərweɪt/','配重；平衡、制衡因素',
 '天平另一端加一块重物，使两边平衡；组织或观点也能成为彼此的制衡。',
 'counter- 相对、抵消 + weight，先是平衡另一负荷的重量，再作抽象制衡比喻。',H('counter- + weight → counterweight','抵消一侧重量的配重 → 制衡因素'),
 'a crane counterweight 起重机配重，a counterweight to power 权力的制衡因素。',
 'a counterweight to；a crane counterweight；act as a counterweight。',
 'counterweight 不只是额外增加重量，关键是平衡另一侧；counterargument 则是回应、反对的论点。',
 ('The crane uses a counterweight for balance.','起重机用配重保持平衡。'),('The committee acts as a counterweight to the director’s power.','委员会起到制衡主管权力的作用。'))
W('weightless','/ˈweɪtləs/','失重的；轻若无物的',
 '像宇航员一样没有平时脚下承托的重量感，但身体、器材仍有质量。',
 'weight + -less 没有，物理用法指失重状态；在轨道中常来自持续自由落体，并非地球引力完全消失。',H('weight + -less → weightless','没有通常承重感觉 → 失重'),
 'a weightless environment 失重环境，feel weightless 感到轻若无物；广告描写面料也可能是轻盈比喻。',
 'a weightless environment；feel weightless；weightless conditions。',
 'weightless 失重，massless 无质量；轨道宇航员不是 massless。NASA 说明微重力环境中的表观失重。',
 ('The astronauts practised moving in a weightless environment.','宇航员练习在失重环境中移动。'),('In the pool, she felt almost weightless.','在泳池里，她几乎感觉不到身体的重量。'),sources=['https://www.nasa.gov/learning-resources/for-kids-and-students/what-is-microgravity-grades-5-8/','https://en.wiktionary.org/wiki/weightless#English'])
W('weightlifting','/ˈweɪtlɪftɪŋ/','举重；负重训练',
 '把重物举起来进行训练或比赛；不同场合可能泛指训练，也可能特指竞技举重项目。',
 'weight 重物、负重 + lifting 举起，形成活动名词。lifting 来自 lift + -ing，不是 life 生命的变形。',H('weight + lifting → weightlifting','举起负重的活动 → 举重'),
 'a weightlifting competition 举重比赛，weightlifting training 举重训练；竞技项目的具体动作按运动规则分，不把所有举铁都当同一比赛。',
 'a weightlifting competition；weightlifting training；take up weightlifting。',
 'weightlifting 举重，powerlifting 力量举是另一竞技项目；普通口语健身中两类名称也有各自用法。',
 ('She took up weightlifting at university.','她在大学开始练举重。'),('The hall hosted a weightlifting competition.','大厅举办了一场举重比赛。'))
W('weightlifter','英 /ˈweɪtlɪftə/；美 /ˈweɪtlɪftər/','举重运动员；练举重的人',
 '做 weightlifting 的人，从活动换成执行者。',
 'weight + lifter，lifter 是 lift + -er；与 weightlifting 活动名词相邻记。',H('weight + lifter → weightlifter','举重物的人 → 举重运动员'),
 'a competitive weightlifter 竞技举重运动员，an experienced weightlifter 有经验的举重者。',
 'a competitive weightlifter；a young weightlifter；an experienced weightlifter。',
 'weightlifter 是人，weightlifting 是活动；-er 这里指执行者，并不是更重的比较级。',
 ('The weightlifter prepared for her next competition.','举重运动员为下一场比赛作准备。'),('He interviewed three experienced weightlifters.','他采访了三名有经验的举重运动员。'))
W('featherweight','英 /ˈfeðəweɪt/；美 /ˈfeðərweɪt/','羽量级；羽量级选手；极轻的',
 '像羽毛一样轻的命名画面，用在比赛里却是具体体重级别，不是选手真的只重一根羽毛。',
 'feather 羽毛 + weight 重量，形成轻体重级别名称，再可作轻便的修饰语。具体限重依运动与组织而异。',H('feather + weight → featherweight','羽毛般轻 → 羽量级；轻便'),
 'a featherweight boxer 羽量级拳击手，the featherweight title 羽量级冠军头衔；a featherweight jacket 极轻外套。',
 'a featherweight boxer；the featherweight title；a featherweight jacket。',
 'featherweight 具体级别，不等于所有 lightweight 轻量事物；比赛名称别按字面随意换。',
 ('She won the featherweight title.','她赢得了羽量级冠军。'),('The featherweight jacket folds into a small pouch.','这件极轻外套能折进一个小袋。'))
R('B2937','重量与分量；负重活动及轻重级别','WEIGHT：称得出重，也能衡量影响力','先读 weight、weighty，再对比 over-/under-/counter-；weightless 单列物理状态，weightlifting 与 weightlifter 相邻。',
 '与 weigh 同族的古英语继承名词。体重级别已有 lightweight、heavyweight、middleweight、flyweight，本页共享，不重复写定义。',
 'weight → weighty、weightless；over-/under-/counter- + weight；weight + lifting/lifter；feather + weight。',
 [['重量、分量与比较','weight · weighty · overweight · underweight'],['平衡与失重','counterweight · weightless'],['训练活动与人物','weightlifting · weightlifter · bodyweight'],['级别与日常复合','lightweight · featherweight · flyweight · middleweight · heavyweight · paperweight']],
 'weightless 不等于 massless；weighty matters 重大事项；overweight 重量超与 oversize 尺寸超不同。',
 'Her weighty opinion carried more weight than the figures alone.\n\n她有分量的意见比单看数字更具影响力。',
 'weight weighty overweight underweight counterweight weightless weightlifting weightlifter bodyweight lightweight featherweight flyweight middleweight heavyweight paperweight')
BI=[['古英语 gebyrd 与北欧 burðr、byrd 等同族形式 → 中古英语 birthe','生育、出生；与 bear 生育、承载同族'],['现代 birth','出生、诞生 → 新阶段的开始；相关日期与习俗']]
def BH(f,m):return BI+[[f,m]]
W('rebirth','英 /ˌriːˈbɜːθ/；美 /ˌriːˈbɜːrθ/','重生；复兴；宗教转生',
 '像重新出生一样，原来衰落、停滞的东西又获得新的生命；宗教语境也可说转生。',
 're- 再次 + birth 出生。复兴是出生画面的比喻，宗教转生则依具体信仰背景理解。',BH('re- + birth → rebirth','再次诞生 → 重生、复兴'),
 'the rebirth of a city 城市复兴，a cultural rebirth 文化复兴，belief in rebirth 相信转生。',
 'the rebirth of；a cultural rebirth；a spiritual rebirth。',
 'rebirth 强调像获得新生命，repair 只说修复；重修一座楼不一定要夸大成整座城市重生。',
 ('The new theatre helped bring about a cultural rebirth in the town.','新剧院帮助小镇迎来文化复兴。'),('The novel ends with a sense of hope and rebirth.','小说以希望与新生的感觉收尾。'))
W('birthing','英 /ˈbɜːθɪŋ/；美 /ˈbɜːrθɪŋ/','生育、分娩；与分娩有关的',
 '把出生这件事看成正在进行的过程，常用来修饰场所、设施等。',
 'birth 用作生育动词 + -ing，形成过程名词、修饰形式。不是 birth 名词只能加一个固定后缀变成生物学新概念。',BH('birth + -ing → birthing','生育动作、过程 → 分娩相关的'),
 'a birthing centre 分娩中心，a birthing pool 分娩池；具体机构服务由其实际安排决定。',
 'a birthing centre；a birthing room；a birthing pool。',
 'birth 出生事件，birthing 常聚焦分娩过程；childbirth 是已有的常用生育、分娩名词。',
 ('The hospital opened a new birthing centre.','医院新开了一处分娩中心。'),('The brochure describes the facilities in the birthing rooms.','宣传册介绍了分娩室的设施。'))
W('birthdate','英 /ˈbɜːθdeɪt/；美 /ˈbɜːrθdeɪt/','出生日期',
 '问你是哪一年、哪一月、哪一天出生，常见于登记资料，而不是问今年什么时候办生日会。',
 'birth + date 日期，组成记录出生日期的名词，也常写 date of birth。',BH('birth + date → birthdate','出生的日期 → 出生日期'),
 'enter your birthdate 填出生日期，verify a birthdate 核对出生日期；月日年顺序按表格要求。',
 'enter your birthdate；verify a birthdate；date of birth。',
 'birthdate 通常包括出生年份，birthday 日常常说每年纪念的月日；有些系统字段也用 birthday 存完整日期，仍看提示。',
 ('Please enter your full birthdate on the form.','请在表格上填写完整出生日期。'),('The records list different birthdates for the same person.','档案给同一个人列出了不同出生日期。'))
W('birthstone','英 /ˈbɜːθstəʊn/；美 /ˈbɜːrθstoʊn/','诞生石；生日石',
 '习俗或珠宝列表里，与某个出生月份相关联的宝石；不是婴儿出生时身体里的一块石头。',
 'birth 出生 + stone 宝石，按出生月份与石头的文化联想命名。不同传统、列表可能不一致，不写一张表当全球唯一标准。',BH('birth + stone → birthstone','与出生月份关联的宝石 → 诞生石'),
 'a birthstone ring 诞生石戒指，her birthstone 她出生月份对应的宝石；名称表达习俗关系，不表示医疗作用。',
 'a birthstone ring；a birthstone necklace；a traditional birthstone。',
 'birthstone 是习俗、饰品分类，birthmark 是胎记；两个词后部完全不同，不能只按 birth 猜身体器官。',
 ('She received a ring set with her birthstone.','她收到了一枚镶着自己诞生石的戒指。'),('The jeweller showed us several birthstone necklaces.','珠宝商给我们看了几条诞生石项链。'))
R('B2453','出生、复兴、日期与诞生石习俗','BIRTH：生命开始，也能借来形容新事物开始','从已有 birth、childbirth 接过程 birthing，再把 birthdate、birthday 放在一起；rebirth 复兴，birthstone 属文化习俗。',
 'birth 与 bear 生育、承载同族，现代词形受北欧相关形式影响，不能把词尾随意说成今天可造任何名词的 -th。',
 'birth → birthing、rebirth；birth + date/day/place/right/mark/rate/stone；child、still + birth。',
 [['基本出生与过程','birth · childbirth · birthing · stillbirth'],['日期、地点与身份','birthdate · birthday · birthplace · birthright'],['身体、统计与习俗','birthmark · birthrate · birthstone'],['再次开始','rebirth']],
 'birthdate 通常含出生年份，birthday 常说每年生日；birthstone 文化习俗不等于 birthmark 胎记；rebirth 可比喻复兴。',
 'The old theatre’s rebirth became part of the city’s story.\n\n老剧院的复兴成为城市故事的一部分。',
 'birth childbirth birthing stillbirth birthdate birthday birthplace birthright birthmark birthrate birthstone rebirth')
if __name__=='__main__':save('continuation_20261030_a',ROOTS,WORDS)
