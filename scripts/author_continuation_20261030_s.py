"""Ice, speed and dad: useful everyday families."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
IC=[['古英语 īs → 中古英语 is、ice','冰'],['现代 ice','冰；使结冰、加冰；另有裱糖霜等用法']]
def IH(f,m):return IC+[[f,m]]
W('ice','/aɪs/','冰；加冰、使结冰；给糕点裱糖霜',
 '水冻成硬块是冰；给饮料加冰、给表面覆一层东西，又形成动词用法。',
 '继承古英语 īs，现代 ice 的 c 读 /s/。糕点糖霜的 ice 动词是表面覆盖用法，不表示蛋糕一定冷冻了。',IC,
 'ice cubes 冰块，on ice 加冰、冰镇，也可暂搁，break the ice 打破僵局，ice a cake 给蛋糕裱糖霜。',
 'ice cubes；on ice；break the ice；ice a cake。',
 'ice 冰不同于 ice cream 冰淇淋；thin ice 薄冰可比喻危险处境，具体危险由语境说明。',
 ('She put a few ice cubes in the glass.','她往杯里放了几块冰。'),('His joke helped break the ice at the meeting.','他的笑话帮助打破了会议上的拘谨气氛。'))
W('icy','/ˈaɪsi/','结冰的；冰冷的；态度冷冰冰的',
 '路面上一层冰，空气冻人，或者某人的眼神像冰一样没有温度。',
 'ice + -y，去末尾 e；古英语已有相关形式。由冰的状态延伸到温度和人际冷淡。',IH('ice + -y → icy','有冰、冰冷 → 冷淡的'),
 'an icy road 结冰道路，icy water 冰冷的水，an icy stare 冷冰冰的注视。',
 'icy roads；icy water；an icy stare；an icy silence。',
 'icy road 常真的有冰；icy tone 描写态度，不是在报告嗓音温度。iced 常说明加冰、被冰镇或裱糖霜。',
 ('The road became icy after sunset.','日落后路面结了冰。'),('She greeted him with an icy smile.','她用冷冰冰的微笑迎接他。'))
W('iced','/aɪst/','加冰、冰镇的；裱糖霜的',
 '饮料被冰镇，糕点被覆上糖霜；看后面的名词，就知道是哪一种处理。',
 'ice + -ed，/s/ 后的 -ed 读 /t/，整个词仍一音节。饮料义与糕点义来自 ice 不同动词用法。',IH('ice + -ed → iced','被冰镇、加冰；被覆糖霜'),
 'iced tea 冰茶，iced coffee 冰咖啡，an iced cake 裱糖霜蛋糕。iced drink 不保证喝到时仍有完整冰块。',
 'iced tea；iced coffee；an iced cake。',
 'iced cake 不是 ice-cream cake 冰淇淋蛋糕的必然同义词；iced 可能只说糖霜装饰。',
 ('She ordered an iced coffee.','她点了一杯冰咖啡。'),('The display was full of brightly iced cakes.','陈列柜里摆满了裱着鲜艳糖霜的蛋糕。'))
W('icebreaker','英 /ˈaɪsbreɪkə/；美 /ˈaɪsbreɪkər/','破冰船；打破拘谨的活动、话题',
 '船把冰层撞开，后面才有路走；陌生人做个小游戏，僵硬气氛松开，也叫破冰。',
 'ice + breaker，breaker 是 break + -er。社交用法连着 break the ice 打破僵局这个比喻。',IH('ice + break + -er → icebreaker','打破冰层的船 → 打破社交僵局的活动'),
 'an icebreaker in polar waters 极地水域破冰船，an icebreaker game 破冰游戏，a good icebreaker 容易打开话题的东西。',
 'an icebreaker ship；an icebreaker game；a good icebreaker。',
 'icebreaker 在培训里常指活动，并非参与者都要说心里话；物理破冰和社交破冰由语境区分。',
 ('An icebreaker opened a path through the frozen sea.','破冰船在结冰海面开出通路。'),('We began the workshop with a simple icebreaker.','工坊开始时，我们先做了一个简单的破冰活动。'))
W('icicle','/ˈaɪsɪkl/','冰柱；冰凌',
 '屋檐滴下的水一点点冻住，最后垂成尖尖的一条冰。',
 '中古英语 is〔冰〕+ ikel〔冰柱〕，后部接古英语 gicel。拼写后来像拉丁小称后缀 -icle，但真实后部是本族旧冰柱词，不与 particle 的 -icle 当同源后缀。',
 [['中古英语 is〔冰〕；ikel〔冰柱〕，后者接古英语 gicel','两个本族冰相关成分'],['is + ikel → isykle → icicle','屋檐等处下垂的尖冰柱；拼写受相似词形影响']],
 'icicles hanging from the roof 屋檐垂下的冰柱，a row of icicles 一排冰凌。构词里保留了今天不再独立常用的旧词。',
 'icicles on the roof；a row of icicles；a melting icicle。',
 'icicle 的 -icle 看起来像 particle 的后缀，历史却不同；icycle 不是这个词的标准拼写，也别与 bicycle 自行车混淆。',
 ('Long icicles hung from the roof.','屋檐垂下长长的冰柱。'),('The icicles began to melt in the afternoon sun.','冰柱在午后的阳光下开始融化。'),sources=['https://www.etymonline.com/word/icicle','https://en.wiktionary.org/wiki/icicle#English'])
R('B3036','冰、冰冷、破冰与冰柱','ICE：实物冰层，也能比喻冷淡和僵局','ice → icy、iced 先讲状态与处理，再看 icebreaker、icicle；现有 icebox、icehouse 共享。',
 '古英语冰词延续至今。icicle 后部是旧本族冰柱词，不把相似结尾一律当拉丁小称；冷门人名式、地名式扩展暂略。',
 'ice + -y → icy；ice + -ed → iced；ice + breaker；旧 is + ikel → icicle；ice + box/house。',
 [['基本状态与处理','ice · icy · iced'],['破冰与冰柱','icebreaker · icicle'],['储冰设施','icebox · icehouse']],
 'icy 冰冷与 iced 被处理有别；iced cake 常说糖霜；icicle 不是 ice 加拉丁 -icle。',
 'We drank iced tea while the last icicles melted outside.\n\n我们喝着冰茶，窗外最后几根冰柱正在融化。',
 'ice icy iced icebreaker icicle icebox icehouse')
SP=[['古英语 spēd、spēdan','成功、顺利进展；使成功、前进'],['中古英语 sped → speed','较早出现快速义 → 速度、加快、超速']]
def SH(f,m):return SP+[[f,m]]
W('speed','/spiːd/','速度；快速；加快；超速行驶',
 '今天常问一段时间走多远、做多快；历史上的老义却是事情有进展、能成功。',
 '名词、动词接古英语 spēd、spēdan，早有成功、进展义，快速与速率义后来成为中心。过去式、分词有 sped 和 speeded，不同搭配有偏好。',SP,
 'at a speed of 以某速度，speed up 加快，speed limit 限速；speed 也可以是很低的速率，并非每次都说快。',
 'at high speed；speed up；a speed limit；a slow speed。',
 'speed 作名词一般说速率，不含方向；velocity 科学语境包含方向。Godspeed 等祝愿用法保留旧成功义，不是催人开快车。',
 ('The train reached a speed of two hundred kilometres an hour.','火车时速达到两百公里。'),('A clearer process could speed up the work.','更清楚的流程能加快工作。'),sources=['https://www.etymonline.com/word/speed','https://en.wiktionary.org/wiki/speed#English'])
W('speedy','/ˈspiːdi/','迅速的；快速完成的',
 '回复很快来到、事情很快办妥，不一定是某辆车正在飞驰。',
 '接古英语 spēdiġ 等形式，现代可对应 speed + -y；旧义也有成功、富足，今天常用迅速义。',SH('古英语 spēdiġ → speedy','有成功进展 → 迅速的'),
 'a speedy reply 迅速答复，a speedy resolution 很快解决，a speedy recovery 早日康复这一祝愿。',
 'a speedy reply；a speedy resolution；a speedy recovery。',
 'speedy 常强调过程耗时短或处理及时，fast 适用范围更宽；a speedy recovery 是祝愿，不是对恢复速度作保证。',
 ('Thank you for your speedy reply.','谢谢你迅速回复。'),('We hope for a speedy resolution to the problem.','我们希望问题能尽快解决。'))
W('speeding','/ˈspiːdɪŋ/','快速行进；超速驾驶',
 '作为描述可以是车飞快掠过；作为交通名词，通常就是超过规定速度开车。',
 'speed + -ing，动词活动名词化，也可作进行时或修饰语。交通违法义是现代车辆语境里的固定用法。',SH('speed + -ing → speeding','快速移动；特指超速驾驶行为'),
 'a speeding car 疾驰的车，a speeding ticket 超速罚单，be stopped for speeding 因超速被拦下。',
 'a speeding car；a speeding ticket；be caught speeding。',
 'speeding ticket 指超速相关处罚文书，不是快递车票；speeding up 加快与超速驾驶要按完整搭配分。',
 ('The police stopped the driver for speeding.','警方因超速拦下了司机。'),('A speeding train passed the platform.','一列疾驰的火车经过站台。'))
W('speeder','英 /ˈspiːdə/；美 /ˈspiːdər/','超速驾驶者',
 '把车开得超过限速的人，按这种行为称呼。',
 'speed 动词超速 + -er，表示做这件事的人。另有专用设备义较冷门，本页聚焦交通用法。',SH('speed + -er → speeder','超速行驶的人'),
 'catch speeders 查获超速者，a warning to speeders 对超速者的警示。新闻里常用，日常也可说 speeding drivers。',
 'catch speeders；warn speeders；a repeat speeder。',
 'speeder 是人，不是 speedometer 速度表；speedster 更宽泛地夸快人、快车，不一定构成超速。',
 ('The camera records speeders on this road.','摄像头记录这条路上的超速驾驶者。'),('The signs warn speeders to slow down.','标牌警告超速者减速。'))
W('speedway','/ˈspiːdweɪ/','赛车场、赛道；摩托车场地竞速',
 '为高速比赛准备的赛道；有时不只说场地，也说在这种场地上的竞速项目。',
 'speed + way 通道、道路，固定用于赛车相关场地；特定摩托车竞速项目也叫 speedway。',SH('speed + way → speedway','高速比赛场地 → 相应竞速项目'),
 'a motor speedway 赛车道，racing at the speedway 在赛车场比赛，speedway racing 场地竞速。',
 'a motor speedway；speedway racing；at the speedway。',
 'speedway 通常赛车语境，motorway、freeway 常是公共高速公路；不能把所有高速公路都叫赛车场。',
 ('Thousands of fans gathered at the speedway.','成千上万名车迷聚集在赛车场。'),('The town hosts speedway racing during the summer.','镇上夏季举办摩托车场地竞速。'))
W('speedboat','英 /ˈspiːdbəʊt/；美 /ˈspiːdboʊt/','快艇',
 '为了跑得快设计的小型动力船，名字强调速度性能。',
 'speed + boat 船，合成快艇名称；现代还可转为乘快艇行进的动词，但名词最实用。',SH('speed + boat → speedboat','快速动力船 → 快艇'),
 'a speedboat ride 乘快艇游玩，a speedboat race 快艇赛，a small speedboat 小快艇。',
 'a speedboat ride；a speedboat race；a small speedboat。',
 'boat 船的总称，speedboat 特指以高速为特点的船型；不等于所有 motorboats 动力船。',
 ('A speedboat crossed the bay in a few minutes.','快艇几分钟就穿过了海湾。'),('They watched a speedboat race from the shore.','他们在岸上观看快艇比赛。'))
R('B2983','成功进展的旧义；现代速度与加快','SPEED：今天看多快，历史也曾说进展顺利','speed → speedy；speeding、speeder 放一起，再按赛道、快艇和测量复合词扩展。',
 '古英语已有成功、进展词族，快速义在早期英语中出现，现代 speed 还泛指速率，快慢都能有。过冷俚语和专名先略。',
 'speed → speedy、speeding、speeder；speed + way/boat；air/light + speed；speed + -o- + meter。',
 [['基础、性质、行为与人物','speed · speedy · speeding · speeder'],['交通与测量','speedway · speedboat · airspeed · lightspeed · speedometer'],['已有数字场景','speedrun']],
 'speed 不必快；speeding 常超速；speedway 多赛道；speedometer 是速度表。',
 'The speedboat maintained a steady speed as it crossed the bay.\n\n快艇以稳定速度穿过海湾。',
 'speed speedy speeding speeder speedway speedboat airspeed lightspeed speedometer speedrun')
DA=[['早期现代英语 dad、dadd、dadde','爸爸；更早口语历史缺少直接记录'],['dad → daddy；step- + dad','亲昵称呼；继父的口语名称']]
W('dad','/dæd/','爸爸；父亲〔口语〕',
 '日常叫父亲“爸”，通常比 father 更亲近、随意。',
 '早期现代英语已有 dad 等拼写，可能来自儿童易发的 da 音；更早具体来源未定。不是把 father 按字母规则缩出来。',DA,
 'my dad 我爸，Dad 作直接称呼常大写；a new dad 新当爸爸的人。正式关系说明可用 father。',
 'my dad；Dad, can you help?；a new dad。',
 'dad 亲近口语，father 中性或较正式。My dad 与 Dad 的大写取决于是否当作称呼，而不是随时都要大写。',
 ('My dad taught me how to ride a bike.','我爸教我骑自行车。'),('Dad, could you help me move this box?','爸，你能帮我搬这个箱子吗？'),sources=['https://www.etymonline.com/word/dad','https://en.wiktionary.org/wiki/dad#English'])
W('daddy','/ˈdædi/','爸爸、爹地〔亲昵称呼〕',
 '小孩子叫爸爸，或家庭里习惯的一种撒娇、亲昵称呼。',
 'dad + -y，双写 d；-y 在这里形成亲昵称呼，而不是说明材质或性质的形容词 -y。',DA+[['dad + 亲昵 -y → daddy','亲昵、儿语色彩的爸爸称呼']],
 'Daddy 作称呼常大写，my daddy 我爸爸。成年人是否这样叫父亲，要看家庭和文化习惯；别的口语义另看上下文。',
 'my daddy；Daddy, look!；a daddy’s girl。',
 'daddy 的亲昵程度通常比 dad 强；不因语境里出现 daddy 就一律当小孩真在叫生父。',
 ('“Daddy, look at my drawing!” the child said.','孩子说：“爸爸，看我画的画！”'),('She made a card for her daddy.','她为爸爸做了一张卡片。'))
W('stepdad','/ˈstepdæd/','继父〔口语〕',
 '父母再组成家庭后，家里称作爸爸的继亲父亲；词本身只说明亲属关系。',
 'step- 继亲 + dad；step- 源于旧亲属词材料，与走一步的 step 不是这里的现代构词关系。正式常用 stepfather。',DA+[['step-〔继亲〕+ dad → stepdad','继父的口语名称']],
 'my stepdad 我的继父，a supportive stepdad 很支持孩子的继父。与亲生父亲、养父的称呼要分别理解。',
 'my stepdad；a supportive stepdad；live with a stepdad。',
 'stepdad 不自动等于 adoptive father 养父，继亲关系与收养关系是不同概念；感情亲疏也不能仅凭词判断。',
 ('My stepdad helped me build the bookshelf.','继父帮我做了书架。'),('She introduced him as her stepdad.','她介绍他说，这是她的继父。'))
R('B3721','父亲的亲昵称呼与继亲','DAD：亲近口语；DADDY：更亲昵；STEPDAD：继父','dad 后接 daddy，再看 stepdad 与已有 granddad，分清亲昵后缀和亲属前部。',
 'dad 可能与儿童发音有关，具体早源未定。step- 是旧继亲材料，grand- 则接上一代。',
 'dad + -y → daddy；step- + dad；grand- + dad → granddad。',
 [['基本称呼与亲昵','dad · daddy'],['家庭关系','stepdad · granddad']],
 'dad 与 father 的语体；daddy 的 -y 是亲昵；stepdad 继父不必等于收养父亲。',
 'Dad and Granddad helped the child make a card for his stepdad.\n\n爸爸和爷爷帮孩子给继父做了一张卡片。',
 'dad daddy stepdad granddad')
if __name__=='__main__':save('continuation_20261030_s',ROOTS,WORDS)
