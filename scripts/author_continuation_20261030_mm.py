"""Buff, frost, riots and ticking."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
B=[['法语 buffle 水牛 → buff 软皮革','皮革可用于抛光；又给出浅黄褐色'],['材料、用途和人物称呼','buff 抛光；制服相关火灾爱好者称呼扩展为迷、爱好者'],['另一击打词 buff','与缓冲器 buffer 的词源相连；抛光器 buffer 则接皮革用途']]
W('buff','/bʌf/','抛光；爱好者、迷；浅黄褐色；肌肉发达的；增益',
 '一块软皮把表面磨亮，是 buff 的抛光画面；a history buff 则是历史迷。它的常用义很多，先按人物、动作、颜色分开认。',
 '皮革名经法语 buffle 水牛发展，皮革用于抛光、颜色成为色名。爱好者义常追溯到纽约穿相应色制服的消防人员及其爱好者称呼；肌肉、游戏增强是后续不同语境。',B[:2],
 'buff a surface 抛光表面，a film buff 影迷，buff paper 浅黄褐色纸，look buff 看起来肌肉发达；游戏中的 buff 指增强、增益。in the buff 则是裸体的口语表达。',
 'a history buff；buff a surface；look buff。',
 'a buff 是人物爱好者，buff 作动词多为抛光或增强；不能用同一种中文塞进所有句子。',
 ('She is a history buff and loves visiting museums.','她是历史迷，很喜欢参观博物馆。'),('He buffed the table until it shone.','他把桌子抛光，直到表面发亮。'),('The file was stored in a buff envelope.','文件装在一个浅黄褐色信封里。'),sources=['https://en.wiktionary.org/wiki/buff#English','https://www.etymonline.com/word/buff'])
W('buffer','英 /ˈbʌfə/；美 /ˈbʌfər/','缓冲物、缓冲区；缓冲；抛光工具',
 '两件东西别直接硬碰硬，中间垫一层，就是 buffer 的缓冲画面。数据来得快、处理得慢，先暂存一下，也像给速度差留个中间层。',
 '缓冲义的 buffer 接旧 buff 受击发闷声、打击词 + -er；抛光器义则接 buff 抛光 + -er。两种近形构词有不同词义来源。',B[-1:]+[['缓冲名词 → buffer 动词','减少冲击；暂存以协调处理速度'],['抛光 buff + -er','抛光的人或工具']],
 'a buffer zone 缓冲地带，a financial buffer 财务缓冲余地，a data buffer 数据缓冲区，a floor buffer 地板抛光机；化学中 buffer 也指抵抗酸碱度变化的缓冲体系。',
 'a buffer zone；a data buffer；a floor buffer。',
 'buffer 数据常为处理、传输之间暂存，cache 常突出方便重复访问；具体实现可交叠，名称侧重点不同。抛光器要看 floor 等背景。',
 ('The trees form a buffer between the road and the houses.','树木在道路与住宅之间形成缓冲带。'),('The program stores incoming data in a buffer.','程序把传入数据暂存在缓冲区。'),sources=['https://en.wiktionary.org/wiki/buffer#English','https://www.etymonline.com/word/buffer'])
Rb=[['意大利 ribuffare → 法语 rebuffer','驳回、粗暴回应等旧用法'],['英语 rebuff','冷淡、断然拒绝；拒绝的遭遇']]
W('rebuff','/rɪˈbʌf/','断然拒绝、冷淡回绝；碰壁、拒绝',
 '你伸出合作的手，对方直接挡回来，态度冷淡；rebuff 不只是说不，还让人感到被拒在门外。',
 '常用拒绝义借旧法语 rebuffer，接意大利 ribuffare。另有 re- + buff 再次抛光的同形动词，通常读 /ˌriːˈbʌf/，不是本词最常见用法。',Rb,
 'rebuff an offer 回绝提议，rebuff someone’s advances 拒绝某人示好，meet with a rebuff 遭到拒绝。',
 'rebuff an offer；meet with a rebuff。',
 'rebuff 通常比中性 decline 更突出拒绝的生硬、冷淡；不必每次有当面争吵。',
 ('She rebuffed his offer of help.','她冷淡地回绝了他提供帮助的提议。'),('Their request met with a firm rebuff.','他们的请求遭到断然拒绝。'))
R('B2720','软皮抛光、爱好者称呼与缓冲击打词分支','BUFF：先分皮革用途与旧击打词，现代义就不乱','buff → 抛光器 buffer；击打词 buff → 缓冲器 buffer；rebuff 拒绝另看借词。',
 '同形词在词表里常被挤在一起，学习时用来源和场景拆开。buffer 的中间缓冲层能帮助理解软件暂存，不能拿抛光解释全部。',
 'buffle 水牛 → buff 软皮、抛光等；另有旧打击 buff；-er 工具；rebuff 借法语、意大利相应词。',
 [['皮革、抛光及现代扩展','buff'],['缓冲与抛光的同形工具名','buffer'],['断然拒绝','rebuff']],
 'buffer 两条来源分开；rebuff 常用回绝义不按再次抛光来理解。',
 'The film buff’s proposal met with a rebuff.\n\n那位影迷的提议遭到了冷淡回绝。','buff buffer rebuff')
F=[['古英语 forst、frost 等 → frost','霜、严寒，与 freeze 词族相关'],['覆盖一层细冰晶的外观','扩展到糖霜、磨砂似的半透明表面'],['复合、前缀扩展','frostbite 冻伤；permafrost 多年冻土；defrost 除霜、解冻']]
W('frost','英 /frɒst/；美 /frɔːst/','霜；霜冻；结霜、覆上霜状层',
 '早晨玻璃、草叶上那层细小冰晶，是 frost；一夜气温使地面结霜，也可说 a frost。',
 '承古英语 forst、frost 相应形式，经中古英语延续，与 freeze 的旧词族相关。动词说结霜、覆盖霜状表层。',F[:2],
 'a layer of frost 一层霜，a hard frost 严重霜冻，frost on the window 窗上霜，frost a cake 给蛋糕抹糖霜。',
 'a layer of frost；a hard frost。',
 'frost 是表面细冰晶及相应寒冷现象，snow 是雪；糖霜义借外观，不是把真正冰霜放到蛋糕上。',
 ('Frost covered the grass in the morning.','早晨，霜覆盖了草地。'),('There was a hard frost overnight.','夜里出现了严重霜冻。'))
W('frosting','英 /ˈfrɒstɪŋ/；美 /ˈfrɔːstɪŋ/','糖霜、蛋糕甜涂层；一层霜；frost 的 -ing 形式',
 '蛋糕外面盖一层甜甜的涂层，视觉上像覆上霜，便叫 frosting。它可以柔滑厚实，不必是硬结晶。',
 'frost + -ing，由覆霜、覆上霜状层的动作命名表层；甜涂层义借外观延伸。',F[:2]+[['frost + -ing → frosting','覆盖层 → 糖霜、甜涂层']],
 'chocolate frosting 巧克力糖霜，spread frosting on a cake 在蛋糕上抹糖霜；与 icing 在不同地区、做法中用法可交叠。',
 'chocolate frosting；spread frosting。',
 'frosting 与 icing 的细分常因地区、配方而异，不强定一个永远稠、一个永远稀。',
 ('She spread vanilla frosting over the cake.','她在蛋糕上抹了一层香草糖霜。'),('The cupcakes had thick chocolate frosting.','纸杯蛋糕上有厚厚的巧克力糖霜。'))
W('frosted','英 /ˈfrɒstɪd/；美 /ˈfrɔːstɪd/','覆霜的；磨砂似半透明的；覆糖霜的',
 '玻璃看上去像罩着一层霜，能透光却看不清后面，就 frosted glass；蛋糕覆了糖霜也能 frosted。',
 'frost + -ed；词末 /t/ 后 -ed 读 /ɪd/。分词形容词由真实结霜扩展到相似表面和甜涂层。',F[:2]+[['frost + -ed → frosted','覆霜、霜状表面或覆甜涂层']],
 'frosted glass 磨砂玻璃，a frosted window 结霜或经磨砂处理的窗，frosted cupcakes 覆糖霜的纸杯蛋糕。',
 'frosted glass；frosted cupcakes。',
 'frosted glass 可以是加工的纹理效果，不表示玻璃一直处在结冰温度；具体工艺不由这个词确定。',
 ('The bathroom door had frosted glass.','浴室门装着磨砂玻璃。'),('They placed the frosted cupcakes on a tray.','他们把覆好糖霜的纸杯蛋糕放到托盘上。'))
W('defrost','英 /diːˈfrɒst/；美 /diːˈfrɔːst/','除霜；解冻',
 '冰箱壁上结了一层霜，把它去掉是 defrost；食物冻成硬块，让它解冻，也常用同一个词。',
 'de- 去除 + frost 霜，先说除去霜，再扩展为解除冷冻状态。',F[:1]+[['de- + frost → defrost','去霜 → 使解冻']],
 'defrost the freezer 给冷冻柜除霜，defrost food 使食物解冻，a defrost setting 除霜、解冻设置。',
 'defrost the freezer；defrost food。',
 'defrost 是去掉霜、冰冻状态；不等于把食物做熟。烹调动作要另用 cook 等词。',
 ('The freezer needs to be defrosted.','冷冻柜需要除霜了。'),('The appliance has a separate defrost setting.','这台设备有单独的解冻设置。'))
W('frostbite','英 /ˈfrɒstbaɪt/；美 /ˈfrɔːstbaɪt/','冻伤〔低温使皮肤、组织冻结造成的损伤〕',
 '寒冷像咬了身体一口，frost + bite 把冻伤说得很形象；它是实际组织损伤，不只是感觉凉或不舒服。',
 'frost 霜、严寒 + bite 咬，复合名称用寒冷咬伤的画面指冻结性损伤。',F[:1]+[['frost + bite → frostbite','严寒像咬伤一样损害组织']],
 'suffer frostbite 遭受冻伤，frostbite in the fingers 手指冻伤，severe frostbite 严重冻伤。',
 'suffer frostbite；severe frostbite。',
 'frostbite 是损伤名，不要求皮肤表面真看见一层霜；bite 也是命名比喻。',
 ('The climber suffered frostbite during the expedition.','登山者在远征中遭受了冻伤。'),('The report described frostbite injuries to the fingers.','报告描述了手指冻伤。'),sources=['https://en.wiktionary.org/wiki/frostbite#English','https://www.nhs.uk/conditions/frostbite/'])
W('permafrost','英 /ˈpɜːməfrɒst/；美 /ˈpɜːrməfrɔːst/','多年冻土、永久冻土',
 '地面下面的一层，连续多年都保持在冰点或以下，就是 permafrost。它是土、砂、沉积物或岩石的温度状态，不是地面上一层白霜。',
 'perma- 从 permanent 长期、永久的截成构词形式 + frost。科学定义看连续至少两年保持在 0°C 或以下，而不是承诺以后永远不会融。',F[:1]+[['perma- + frost → permafrost','长期冰点以下的地层']],
 'permafrost thaw 多年冻土融化，a permafrost layer 多年冻土层；定义依据温度、持续时间，不要求土里全部是冰。',
 'a permafrost layer；permafrost thaw。',
 'permanent 的字面不能机械理解为永不改变；permafrost 也不等于只冻了一个冬天的季节冻土。',
 ('The researchers measured temperatures in the permafrost.','研究人员测量了多年冻土中的温度。'),('The village was built on ground underlain by permafrost.','村庄建在下伏多年冻土的地面上。'),sources=['https://en.wiktionary.org/wiki/permafrost#English','https://nsidc.org/learn/parts-cryosphere/frozen-ground-permafrost'])
R('B3552','表面细冰晶、霜状覆盖及严寒复合名词','FROST：细冰晶覆上一层，外观可以借，温度概念另要看定义','frost → frosting、frosted、defrost；frostbite、permafrost。',
 '糖霜、磨砂借外观；除霜说去除；冻伤说组织损害；多年冻土则有持续温度定义。每一支保留最关键的区别。',
 '旧 frost、forst 形式与 freeze 词族相连；-ing、-ed 覆盖层及状态；de- 去除，bite 咬，perma- 长期。',
 [['霜与相似覆盖','frost · frosting · frosted'],['去除霜、冷冻状态','defrost'],['严寒相关专名','frostbite · permafrost']],
 'frosted glass 不必真结冰；frosting 不等于冰霜；permafrost 至少连续两年处于冰点或以下。',
 'Frost covered the frosted glass, so the window was difficult to see through.\n\n霜覆在磨砂玻璃上，更难透过窗看清外面。','frost frosting frosted defrost frostbite permafrost')
Ri=[['古法语 riote、rioter','争吵、纷乱；深源有不同解释'],['中古英语 riot → riot','放纵、喧闹 → 骚乱、暴动；也可比喻繁盛、热闹'],['人物与性质','rioter 参与者；riotous 纷乱、喧闹或放纵的']]
W('riot','/ˈraɪət/','骚乱、暴动；闹腾、放纵；纷繁热闹的景象',
 '人群失去秩序、发生暴力冲突，可以 riot；花园颜色多得奔涌出来，也可 a riot of colour。第二种是借热闹、无拘束的比喻。',
 '经中古英语 riot 接古法语 riote、rioter 争吵、纷乱等，更远未定。由喧闹、放纵发展骚乱，也保留丰富热闹的比喻。',Ri[:2],
 'a riot broke out 发生骚乱，riot police 防暴警察，a riot of colour 色彩纷呈；He’s a riot. 口语可夸某人特别逗。',
 'a riot broke out；a riot of colour。',
 'riot 的公共暴力义不等于所有 protest 抗议；描述具体事件要看实际情况，不能只按人多就叫暴动。',
 ('A riot broke out after the match.','比赛后发生了骚乱。'),('The garden was a riot of colour in spring.','春天，花园里色彩缤纷。'))
W('rioter','英 /ˈraɪətə/；美 /ˈraɪətər/','骚乱、暴动参与者',
 'riot 是一场骚乱，rioter 是其中参与骚乱行为的人。-er 把事件、动作转向具体参与者。',
 '经中古英语 riotour、古法语 rioteor 等人物形式，现代对应 riot + -er。',Ri[:2]+[['rioteor、riotour → rioter','参与骚乱的人']],
 'rioters in the street 街上的骚乱者，a group of rioters 一群骚乱参与者；名词有具体行为背景。',
 'a group of rioters；rioters in the street。',
 '旁观者 bystander 与 rioter 不同；人在现场不自动表示参与骚乱。',
 ('The rioters damaged several parked cars.','骚乱者损坏了几辆停着的汽车。'),('The report distinguished rioters from people watching nearby.','报告区分了骚乱参与者和附近围观的人。'))
W('riotous','/ˈraɪətəs/','骚乱的；喧闹、放纵的；热闹纷繁的',
 '声音、活动像一大群人闹开了，就是 riotous 的画面。可以指真正骚乱，也可说大笑、花园生长得热热闹闹。',
 '承中古英语、盎格鲁诺曼语 riotous，现代对应 riot + -ous，形容具有相应纷乱、无拘束特征。',Ri[:2]+[['riot + -ous 的历史形式 → riotous','骚乱、喧闹、放纵的性质']],
 'riotous laughter 哄堂大笑，riotous behaviour 骚乱、放纵举动，riotous colours 热烈纷繁的颜色。',
 'riotous laughter；riotous behaviour。',
 'riotous laughter 常只是笑得热烈，不是说笑的人正在犯罪骚乱；宾语、修饰对象决定分支。',
 ('The joke was followed by riotous laughter.','笑话说完，大家哄堂大笑。'),('The room was decorated in riotous colours.','房间装饰得色彩热烈纷繁。'))
R('B4075','喧闹、失序与热烈纷繁的比喻','RIOT：动静大得收不住，具体场景决定是否骚乱','riot → rioter、riotous。',
 '人群暴力、热闹大笑、色彩繁盛不是同一件事。人物后缀和性质后缀帮你认结构，语境再帮你选中文。',
 '古法语 riote、rioter → riot；-er 人物，-ous 性质。',
 [['事件、参与者与性质','riot · rioter · riotous']],
 'riot 不等于所有 protest；riotous laughter 可以是正常哄堂大笑。',
 'The story contrasted a street riot with a garden’s riotous colour.\n\n故事把街头骚乱与花园热烈纷繁的色彩作了对照。','riot rioter riotous')
T=[['轻碰、敲击的旧 tick 词族','小而短促的触碰、声响 → 滴答、刻度、勾号'],['另源古英语 ticia → tick','蜱的动物名称'],['另源覆盖物 tick','经荷兰、低地德语等接拉丁 theca 覆盖物；ticking 的织物义']]
W('tick','/tɪk/','滴答声、发滴答声；对勾、勾选；蜱',
 '钟表一声一声 tick，清单上一笔勾 tick；动物 tick 则是蜱。短促声响、轻点记号可以联系，动物名要另记来源。',
 '声响、勾号联系中古英语轻碰、轻敲词族，可能拟声；蜱义承古英语 ticia。旧覆盖物 tick 又是另一借词，保留在织物 ticking 中。',T,
 'the tick of a clock 钟的滴答声，tick the box 勾选方框，a tick on the dog 狗身上的蜱；英式 tick mark 常对应美式 check mark。',
 'tick the box；the tick of a clock。',
 'tick 蜱不是英语 insect 昆虫分类名称，蜱属于蛛形动物；勾选和滴答义不因此与动物习性同源。',
 ('Tick the boxes that apply to you.','勾选适合你的方框。'),('We could hear the clock tick in the quiet room.','安静房间里能听见钟的滴答声。'),('They noticed a tick on the dog’s ear.','他们发现狗耳朵上有一只蜱。'))
W('ticking','/ˈtɪkɪŋ/','滴答声、滴答作响；〔另源〕枕套、床垫罩用结实织物',
 'the ticking of a clock 是钟持续滴答；ticking fabric 则可能是结实的外罩布。一个听声音，一个看覆盖材料。',
 '声响义是 tick + -ing；织物义接旧覆盖物名 tick + 材料名词后缀 -ing，底层借词通向拉丁 theca 覆盖物。',T[:1]+T[-1:]+[['不同 tick + -ing → ticking','滴答过程；另一来源的织物名']],
 'the ticking of the clock 钟的滴答声，a ticking clock 滴答的钟，也可比喻时间紧迫；cotton ticking 棉质结实外罩布。',
 'a ticking clock；cotton ticking。',
 '织物 ticking 不是因为布会滴答作响；-ing 也不都表示正在做。',
 ('The ticking of the clock kept him awake.','钟的滴答声让他睡不着。'),('The mattress was covered with strong cotton ticking.','床垫外包着结实的棉质罩布。'))
W('ticker','英 /ˈtɪkə/；美 /ˈtɪkər/','滴答式记录、报价装置；滚动信息条；〔口语〕心脏',
 '早期记录装置边工作边发短促声响，就叫 ticker；后来屏幕上滚动的新闻、报价也借这个名字。心脏持续跳动，口语里也能叫 ticker。',
 'tick + -er，形成会滴答、记录的人或装置名。记录纸带的名称迁移到显示内容；心脏义借持续跳动。',T[:1]+[['tick + -er → ticker','滴答记录器 → 信息显示；心脏比喻']],
 'a stock ticker 股票报价装置、信息条，a news ticker 新闻滚动条，ticker tape 自动收报、报价纸带；my ticker 是很口语的心脏称呼。',
 'a news ticker；a stock ticker。',
 'ticker 显示信息不一定真发声；stock ticker 的具体价格内容与系统由上下文决定。',
 ('A news ticker ran along the bottom of the screen.','屏幕底部滚动着新闻信息条。'),('The museum displayed an old stock ticker and its paper tape.','博物馆展出了一台旧股票报价机和纸带。'))
W('uptick','/ˈʌptɪk/','小幅上升、回升；价格向上一格的变化',
 '刻度、报价比上一格高了一点，就 uptick。后来不只价格，报名人数、活动数量的小幅增加也能这样说。',
 'up 向上 + tick 刻度、报价变动，先认向上一小格，再理解一般小幅增长。',T[:1]+[['up + tick → uptick','报价、指标向上变化 → 小幅增加']],
 'an uptick in demand 需求小幅上升，an uptick in sales 销售回升，a slight uptick 一点上扬。',
 'an uptick in；a slight uptick。',
 'uptick 常强调相对小的向上变化，不自动说明长期趋势，也不保证之后继续增长。',
 ('There was a slight uptick in attendance.','出席人数略有增加。'),('The survey recorded an uptick in interest in local history.','调查记录到，人们对地方历史的兴趣略有上升。'))
Tl=[['中古英语 tiklen、tikelen → tickle','轻触、挠痒；确切来源未定'],['可能联系 tick 轻碰 + 旧反复 -le','也有其他旧词、音形变化解释'],['由感官刺激到兴趣、喜悦','tickle someone’s fancy 合某人兴趣、使人喜欢']]
W('tickle','/ˈtɪkəl/','挠痒、使发痒；逗乐、激起兴趣',
 '手轻轻反复碰敏感处，让人忍不住笑，是 tickle；有个想法轻轻拨动兴趣，也像挠到心里有趣的地方。',
 '中古英语 tiklen 等确切来源未定，常分析为旧 tick 轻碰的反复形式 + -le，也有其他日耳曼词解释。它不是从蜱咬人的动物名必然派生。',Tl,
 'tickle someone 挠某人痒痒，a tickle in the throat 喉咙发痒，tickle someone’s fancy 引起某人兴趣、合其心意，be tickled 很高兴。',
 'tickle someone’s fancy；a tickle in the throat。',
 'tickle 的轻触反复画面能辅助记忆，但词源分析保留不确定；be tickled 可纯说高兴。',
 ('The feather tickled her nose.','羽毛弄得她鼻子发痒。'),('The idea of a seaside holiday tickled his fancy.','去海边度假的想法很合他的心意。'),sources=['https://en.wiktionary.org/wiki/tickle#English','https://www.etymonline.com/word/tickle'])
R('B2605','短促轻碰、声音与刻度，蜱和织物另源','TICK：一小下、一小格；同形动物与覆盖物别混','tick → ticking、ticker、uptick；tickle 可能接轻碰旧词。',
 '滴答、勾号、刻度都是短促一点的好画面。动物名、床垫罩布各有旧来源，不能全用钟表解释。',
 '轻触 tick 词族；ticia → 蜱 tick；theca 覆盖物经借入 → 织物 tick；-ing、-er、up；tickle 的 -le 分析有讨论。',
 [['短促动作、持续声与显示','tick · ticking · ticker'],['小幅向上变化','uptick'],['轻触、逗乐的近形词','tickle']],
 '蜱属于蛛形动物；织物 ticking 不从滴答声得名；uptick 不保证长期上涨。',
 'The ticking clock sat above a screen showing a small uptick in visitor numbers.\n\n滴答作响的钟下面，屏幕显示访客人数略有增加。','tick ticking ticker uptick tickle')
if __name__=='__main__':save('continuation_20261030_mm',ROOTS,WORDS)
