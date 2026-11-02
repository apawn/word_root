"""Air: atmosphere, flight, pneumatic tools, and their figurative uses."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
def C(a,b,name,meaning):return [[f'英语 {a}；{b}','并列组合的两部分'],[f'{a} + {b} → {name}',meaning]]
AIR=[['希腊 āēr → 拉丁 āēr → 法语 air','空气'],['英语 air','空气、空中；通风、公开、播出等动词义']]
W('airing','英 /ˈeərɪŋ/；美 /ˈerɪŋ/','通风、晾晒；公开讨论；播出',
 '衣物拿出来接触空气，问题也拿出来给大家听；节目则被播给观众。',
 'air + -ing，从名词空气与动词通风、公开、广播的不同用法名词化。不是每次都在说飞行。',AIR+[['air + -ing → airing','让空气接触；让公众听到、看到']],
 'give the room an airing 是给房间通风，give an issue an airing 是让问题公开讨论；the first airing of a show 是节目首次播出。',
 'give something an airing；a public airing；a television airing。',
 'airing 是通风、公开讨论等活动，airfare 是机票价；air 前半不总意味着航空运输。',
 ('The blankets needed a good airing.','毯子需要好好晾一晾。'),('The proposal received a public airing at the meeting.','提议在会上得到公开讨论。'))
W('airstrike','英 /ˈeəstraɪk/；美 /ˈerstraɪk/','空袭；空中打击',
 '打击从空中到来，新闻里用一个复合词概括这类攻击。',
 'air（空中）+ strike（打击），可作名词，也见动词用法。strike 不是罢工这一义，因此不是航空员工停工。',C('air','strike〔打击〕','airstrike','来自空中的军事打击'),
 'an airstrike on a target 是对某目标的空袭，reports of airstrikes 是空袭报道；具体战况要看报道，词本身不提供详情。',
 'an airstrike on；reports of airstrikes；carry out an airstrike。',
 'airstrike 是攻击，airline strike 常可能是航空业罢工；strike 的义项由整体组合和上下文决定。',
 ('The newspaper reported an airstrike near the border.','报纸报道了边境附近的一次空袭。'),('The documentary examines the effects of airstrikes on the town.','纪录片考察了空袭对小镇的影响。'))
W('airbag','英 /ˈeəbæɡ/；美 /ˈerbæɡ/','安全气囊；充气缓冲袋',
 '平时收着的袋状装置，碰撞时迅速鼓起，在人和车内硬物之间提供缓冲。',
 'air + bag，按充气袋结构命名；车辆义最常见，也有其他场景的充气缓冲装置。不是旅客带上飞机的行李。',C('air','bag','airbag','充气形成缓冲的袋状装置'),
 'a driver airbag 是驾驶员安全气囊，a side airbag 是侧气囊。名称不保证所有碰撞都会触发，核心词义是辅助缓冲保护装置。',
 'a driver airbag；a side airbag；an airbag system。',
 'airbag 安全气囊，air baggage、hand baggage 等才与航空行李相关；air 选空气、充气这一支。',
 ('The car is equipped with front and side airbags.','汽车配有前部和侧面安全气囊。'),('The mechanic inspected the airbag system.','技师检查了安全气囊系统。'),sources=['https://en.wiktionary.org/wiki/airbag','https://www.nhtsa.gov/vehicle-safety/air-bags'])
W('airman','英 /ˈeəmən/；美 /ˈermən/','航空人员；空军人员；飞行员〔按语境〕',
 '工作与航空、空军联系起来，但不只坐在驾驶舱的人。',
 'air + man，man 在职业词中有各自历史沿用；airman 可泛指航空相关人员，部分军事体系还有特定身份、等级用法。',C('air','man〔从业者〕','airman','航空、空军相关人员'),
 'a young airman 是年轻航空或空军人员；具体是飞行员、维修或其他岗位，需要上下文。不能仅从词尾 man 决定每个制度中的性别范围。',
 'an experienced airman；a retired airman；an airman’s account。',
 'pilot 明确驾驶航空器，airman 范围可能更宽。airman 与 airline employee 又不是所有语境都同义。',
 ('The memoir was written by a former airman.','回忆录由一位前航空人员撰写。'),('The exhibition records the experiences of wartime airmen.','展览记录了战时航空人员的经历。'))
W('airstrip','英 /ˈeəstrɪp/；美 /ˈerstrɪp/','简易跑道；小型起降场',
 '地上留一条够飞机起降的带状区域，设施比完整机场简单。',
 'air（航空）+ strip（狭长带），不是 strip“脱衣”这一动词。',C('air','strip〔狭长带〕','airstrip','供航空器起降的简易带状场地'),
 'a remote airstrip 是偏远简易机场跑道，a grass airstrip 是草地跑道。名称通常强调简易，不保证每处都未铺装。',
 'a remote airstrip；a grass airstrip；land at an airstrip。',
 'runway 是起降跑道更泛，airstrip 常连同简易小场地一起说；大型 airport 可有多条 runway，不通常整体叫 airstrip。',
 ('The small plane landed on a remote airstrip.','小飞机降落在一处偏远简易起降场。'),('The island’s airstrip lies beside the coast.','岛上的简易跑道位于海岸旁。'))
W('midair','英 /ˌmɪdˈeə/；美 /ˌmɪdˈer/','在空中；半空',
 '还没落到地面，也不搁在支撑面上，东西正处在空中。',
 'mid（中间）+ air，形成空中、半空的整体表达；不是必须位于大气层高度的精确中点。',C('mid','air','midair','处在空中、离地状态'),
 'in midair 是在半空，a midair collision 是空中相撞，catch a ball in midair 是球落地前接住。也有 mid-air 拼法。',
 'in midair；a midair collision；suspended in midair。',
 'midair 关注离地、在空中，midday 是一天中午；mid- 给出中间感觉，但整体对象不同。',
 ('The dancer seemed to pause in midair.','舞者仿佛在半空停了一瞬。'),('She caught the falling leaf in midair.','她在半空接住了飘落的叶子。'))
W('airframe','英 /ˈeəfreɪm/；美 /ˈerfreɪm/','机体；航空器主要结构',
 '先把飞机的机身、机翼等结构看成一个承载整体，再与发动机等装置区分。',
 'air（航空）+ frame（主体框架），不只指框架上几根梁，也常包括整体机体结构。',C('air','frame','airframe','航空器的主要结构整体'),
 'airframe inspection 是机体检查，airframe design 是机体结构设计。具体工程边界依材料、体系定义，核心区别是结构体与动力装置等。',
 'airframe design；an airframe inspection；airframe components。',
 'airframe 机体结构，aircraft 航空器整体；机体没有发动机也可被讨论，但不是完整可飞飞机的同义词。',
 ('Engineers inspected the airframe for damage.','工程师检查了机体是否受损。'),('The museum displays an unfinished airframe.','博物馆陈列着一副尚未完工的机体。'))
W('airbrush','英 /ˈeəbrʌʃ/；美 /ˈerbrʌʃ/','喷笔；喷绘；修饰、抹去〔照片或叙述〕',
 '用气流把细小颜料喷出去，之后也借来形容把照片、历史叙述修得看不见原样。',
 'air + brush，工具虽名 brush，实际以气体喷涂而非普通刷毛涂抹；修图、改写叙述义从这种加工意象延伸。',C('air','brush','airbrush','气体喷涂工具 → 修图、修饰叙述'),
 'airbrush a model 是喷绘模型，airbrush a photo 是修饰照片；airbrush someone out of history 是在历史叙述里抹去某人。数字修图也可能沿用动词。',
 'an airbrush artist；airbrush a photo；airbrush out of。',
 'airbrush 是特定喷绘工具与相应比喻，paint 是上色更泛；不需要真的拿喷笔，仍可说某段历史被 airbrushed。',
 ('The artist used an airbrush to paint the model.','艺术家用喷笔给模型上色。'),('The article argues that their contribution was airbrushed out of history.','文章认为他们的贡献在历史叙述中被抹去了。'))
W('airlock','英 /ˈeəlɒk/；美 /ˈerlɑːk/','气闸；隔气过渡室；气塞〔另义〕',
 '两个空气环境之间先设一间过渡空间，让一边的门不会直接把内外全接通。',
 'air + lock，lock 在这里有隔断通道、闸的意义，不只是金属门锁。流体管道中的 airlock 又可指空气堵塞。',C('air','lock〔闸、隔断〕','airlock','隔开不同环境的过渡室；空气造成的堵塞'),
 'a spacecraft airlock 是航天器气闸，a cleanroom airlock 是洁净室过渡间；a pipe airlock 则可能是管中气塞，物件类型不同。',
 'a spacecraft airlock；enter an airlock；an airlock in a pipe。',
 'airlock 是隔气过渡结构或气塞，airtight 是不透气的性质；一个房间气密良好，不代表它本身就是气闸。',
 ('The astronauts entered through the airlock.','宇航员经气闸进入。'),('An airlock separates the cleanroom from the corridor.','气闸过渡间把洁净室与走廊隔开。'))
W('airspeed','英 /ˈeəspiːd/；美 /ˈerspiːd/','空速；相对周围空气的速度',
 '人在跑步机上走，脚下地面也在动；飞机的空气环境也能流动，所以要区分对空气和对地面。',
 'air + speed，测的是相对空气的速度，不只是任何在空中发生的速度数值。',C('air','speed','airspeed','飞行器相对周围空气的运动速度'),
 'an airspeed indicator 是空速表，maintain airspeed 是保持相对空气速度。航空还分不同空速表达，普通阅读先分清参照物。',
 'an airspeed indicator；indicated airspeed；true airspeed。',
 'airspeed 对空气，ground speed 对地面；逆风、顺风会让两者不同，不拿一个表名就当飞行操作说明。',
 ('The diagram distinguishes airspeed from ground speed.','图中区分了空速与地速。'),('The pilot checked the airspeed indicator.','飞行员看了一眼空速表。'),sources=['https://en.wiktionary.org/wiki/airspeed','https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/relative-velocity/'])
W('airdrop','英 /ˈeədrɒp/；美 /ˈerdrɑːp/','空投；从空中投送',
 '地面道路到不了，物资从飞行器上送下来，到需要的地区。',
 'air（空中）+ drop（投下、落下），名词和动词都常见。不是每一件从手里掉落的东西都叫空投。',C('air','drop','airdrop','从空中投送物品、人员等'),
 'an airdrop of supplies 是物资空投，airdrop food 是空投食品。其他行业会借用分发的比喻；手机功能 AirDrop 又是具体产品名称，别当这个普通词的词源。',
 'an airdrop of supplies；airdrop food；an emergency airdrop。',
 'airdrop 强调从空中投送，airlift 强调用航空器运送；运到机场再卸下的物资不必叫 airdrop。',
 ('An airdrop brought supplies to the isolated village.','一次空投把物资送到了与外界隔绝的村庄。'),('The aircraft airdropped food after the roads were blocked.','道路受阻后，飞机空投了食物。'))
W('airmail','英 /ˈeəmeɪl/；美 /ˈermeɪl/','航空邮件；航空邮寄',
 '信件、包裹的运输段走飞机，而不是海运、陆路慢慢送。',
 'air + mail（邮政邮件），这里 mail 不是 male“男性”；可作名词、动词，也常见 air mail 分写。',C('air','mail','airmail','经航空运输的邮政邮件、寄送方式'),
 'send by airmail 是用航空邮件寄，an airmail letter 是航空信。区别的是运输方式，不等于发邮件这一数字通信行为。',
 'by airmail；an airmail letter；airmail postage。',
 'airmail 是实体邮政航空运输，email 是电子邮件；mail 的历史与现代通信分支不能只按有没有空中无线信号来分。',
 ('She sent the documents by airmail.','她用航空邮件寄出文件。'),('The old envelope still had an airmail label.','旧信封上还贴着航空邮件标签。'))
W('airfoil','英 /ˈeəfɔɪl/；美 /ˈerfɔɪl/','翼型；能与气流作用产生升力的翼形结构',
 '机翼不是随便一块板，它的截面形状会影响空气怎样流过、产生怎样的力。',
 'air + foil，foil 在此接翼面、薄片结构相关用法，不是 foil“挫败”这个动词。英式也常写 aerofoil。',C('air','foil〔翼面、薄片结构〕','airfoil','与气流相互作用的翼形结构、剖面形状'),
 'an airfoil section 是翼型剖面，airfoil design 是翼型设计。普通阅读先知道它在谈空气动力外形，不靠一个词包办全部升力原理。',
 'airfoil design；an airfoil section；airfoil shape。',
 'airfoil 强调翼形结构、截面外形，airframe 是机体主体结构；研究翼型不等于已经描述整架飞机。',
 ('The model uses a different airfoil shape.','模型采用了不同翼型。'),('Students compared two airfoil sections in the diagram.','学生比较图中的两种翼型剖面。'),sources=['https://en.wiktionary.org/wiki/airfoil','https://www.grc.nasa.gov/WWW/k-12/FoilSim/Manual/fsim0003.htm'])
W('airstream','/ˈeəstriːm/（英）；/ˈerstriːm/（美）','气流',
 '空气不是只静静占着地方，也能像水流一样沿某个方向连续移动。',
 'air + stream（流），用水流意象形容空气的连续运动。小写普通词与品牌、专有名称需分开。',C('air','stream','airstream','连续流动的一股空气'),
 'the airstream around a wing 是机翼周围气流；语音学也可谈说话所需气流。方向、速度仍由具体描述给出。',
 'an airstream around；in the airstream；the direction of the airstream。',
 'airstream 常突出一股流动空气，airspace 是一片空域；流动的东西和划出的空间不是同一类对象。',
 ('The smoke made the airstream visible.','烟让气流变得可见。'),('The diagram shows the airstream around the wing.','图中画出了机翼周围的气流。'))
R('B2629','空气；空中；航空；公开播出','AIR：先分清空气物质、飞行空间和公开传播','气囊用充气，航邮走空中，节目 airing 是播出；同一个 air 在不同组合里选不同义。',
 '空气义 air 经法语、拉丁语接古希腊 āēr。现代作为自由词基能组成空气、航空、广播等多支词；音乐曲调等同形用法另按词条辨认。',
 'air → airing、airy、airless 先看基本状态；airflow、airstream、airspeed、airfoil 抓空气运动。airbag、airbrush、airlock 看空气装置，airstrip、airframe、airman 等看航空，airdrop、airmail、airlift 看运输，airplay、airtime 看播出。airbus 小写旧类名与品牌、airsoft 专门运动本页暂不展开。',
 [['基本空气与流动','air · airing · airy · airless · airflow · airstream · airspeed · airfoil'],['充气、喷绘与隔气','airbag · airbrush · airlock · airtight'],['飞行场所、结构及人员','airport · airfield · airstrip · airspace · airway · aircraft · airplane · airframe · airship · airborne · midair · airman · aircrew'],['航空运输和服务','airline · airliner · airfare · airlift · airdrop · airmail'],['传播、行动与其他组合','airplay · airtime · airstrike · airpower · airhead']],
 'airspeed 对空气、ground speed 对地面；airdrop 空投、airlift 空运。airbrush 既可喷绘也可把内容修饰抹去；airing 不一定是航空。',
 'The airdrop reached the village near the airstrip, while a radio airing reported the delivery.\n\n空投物资送到简易跑道附近的村庄，广播节目报道了这次投送。',
 'air airing airy airless airflow airstream airspeed airfoil airbag airbrush airlock airtight airport airfield airstrip airspace airway aircraft airplane airframe airship airborne midair airman aircrew airline airliner airfare airlift airdrop airmail airplay airtime airstrike airpower airhead')
if __name__=='__main__':save('continuation_20261028_ak',ROOTS,WORDS)
