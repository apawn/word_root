"""Short, frequent words whose meanings depend strongly on the surrounding nouns."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'B4199':dict(words=['post','posts'],label='post → posts：柱、岗位与发布内容',note='柱与驿站、岗位等分支分别追溯，张贴内容后有网络发布义。'),
 'B2968':dict(words=['set','sets'],label='set → sets：使就位、固定与一套',note='动词继承本族使坐定材料，集合名词有旧名词及可能法语背景，不硬画单线。'),
 'B2878':dict(words=['hit','hits'],label='hit → hits：击中、成功作品与命中结果',note='北欧相遇、击中词族经借入发展，现代名词也数成功或检索命中。'),
 'B2976':dict(words=['shot','shots'],label='shot → shots：射击、镜头与一次尝试',note='名词有古英语射出词形，短饮等量词用法经过各自历史发展。'),
 'B3861':dict(words=['store','stores'],label='store → stores：储备、存放与商店',note='法语供应、储备词族借入，商品储放地点后来有商店义。'),
 'C0728':dict(words=['market','markets'],label='market → markets：交易场所与买卖范围',note='拉丁交易名词经法语等进入，现代动词表示面向买家推广。'),
 'B2609':dict(words=['fall','falls'],label='fall → falls：落下、瀑布与秋季',note='本族落下词延续，名词按具体落下、季节等用途发展。'),
 'C1526':dict(words=['turn','turns'],label='turn → turns：转向、弯道与轮次',note='拉丁车旋词族经本族早借与法语路线交汇，动作次序也用轮转画面。'),
 'B3625':dict(words=['step','steps'],label='step → steps：步伐、台阶与步骤',note='古英语迈步词族延续，现代抽象步骤由动作分段理解。'),
 'B3311':dict(words=['side','sides'],label='side → sides：侧边与不同立场',note='本族侧面词扩展到队伍、立场，站在哪边的画面直观。'),
 'B3202':dict(words=['link','links'],label='link → links：链环、联系与网页链接',note='中古英语链环词通常联系北欧，现代网络沿连接功能命名。'),
 'C1340':dict(words=['sign','signs'],label='sign → signs：标志、迹象与签名',note='拉丁 signum 经古英语、法语等路径进入，名动词各有历史。'),
 'C1108':dict(words=['power','powers'],label='power → powers：能力、权限与提供动力',note='能够的拉丁词族经法语发展，英语动词由名词转用。'),
 'B2923':dict(words=['attack','attacks'],label='attack → attacks：攻击与抨击',note='接合、接战词族经法语借入，名动词都有常用同形变化。'),
 'B2711':dict(words=['gun','guns'],label='gun → guns：枪、火炮及枪形工具',note='中古英语战械名称，更早可能人名等来源，保留不确定性。'),
 'A1697':dict(words=['troop','troops'],label='troop → troops：队伍、部队与成群行进',note='法语队伍词借入，是 trooper 等名词的基础材料，现代 troops 常合称军人。'),
}
W('posts','英 /pəʊsts/；美 /poʊsts/','柱、桩；岗位；帖文〔复数〕；张贴、发布、邮寄等〔第三人称单数〕',
 '立着支撑的柱、人在组织中的岗位、网上发布的一条条内容，都能写 posts；先把柱与驻点两条历史分开，再看发布、邮递用途。',
 'post + -s，/t/ 后读 /s/。柱名经古英语、法语接拉丁 postis；岗位、驿站支经法语 poste 接意大利语 posto 等放置词。张贴义接在柱面公布，邮递义接沿途驿站。',
 [['拉丁 postis → 柱 post → 张贴、公开发布','实物柱 → 在显眼处公布内容'],['意大利驻点词、法语 poste → 岗位、邮递 post；加 -s','驻留位置、驿站 → 岗位、邮件；现代形式 posts']],
 'wooden posts 木柱；teaching posts 教职岗位；blog posts 博客文章；posts a message 发布消息。',
 'posts along the fence；posts appearing on the website。','posts a letter 在英式常是寄信；posts a message 常是发布消息。所有这些 post 都不能只按 post- 在后这个前缀解释。',
 ('The fence is supported by wooden posts.','围栏由木柱支撑。'),('Several teaching posts are advertised on the website.','网站上刊登着几个教职岗位。'),('She posts a short update every Friday.','她每周五发布一则简短进展。'),sources=['https://en.wiktionary.org/wiki/posts#English','https://www.etymonline.com/word/post'])
W('sets','/sets/','套、组；集合〔复数〕；放置、设定、落下等〔第三人称单数〕',
 '把东西安排到一个确定位置或状态，是 sets 的动作线索；搭配好的几件东西是一套，名词便有 sets。太阳落下、把时间定下，也都有固定用法。',
 'set + -s，/t/ 后读 /s/。动词继承古英语 settan，使坐定、使就位，与 sit 是较早使动关系；集合名词有旧英语名词及可能法语影响等不同分析，不把所有名词义都强归为现代动词新派生。',
 [['古英语 settan → 动词 set；集合名词另有历史分析','使就位、安排；一套一组的名词义'],['set + -s → sets','多套、多组；单数主语设定、放置或落下']],
 'sets of tools 几套工具；sets the time 设定时间；sets the table 摆餐具；the sun sets 太阳落下。',
 'two sets of keys；sets a date for the visit。','set 的过去式、过去分词仍是 set。sets 可以是一套套名词，也可是他、她、它进行设定的动词，先找主语和后面的对象。',
 ('The room has two sets of keys.','这个房间有两套钥匙。'),('She sets the table before dinner.','她晚饭前摆好餐具。'),('The sun sets behind the hills.','太阳在山丘后落下。'),sources=['https://en.wiktionary.org/wiki/sets#English','https://www.etymonline.com/word/set'])
W('hits','/hɪts/','击打、命中；成功作品；检索命中等〔复数〕；击中、达到〔第三人称单数〕',
 '东西准确碰到目标，是 hits；作品获得成功、搜索找到结果，也借用命中目标的画面。',
 'hit + -s，/t/ 后读 /s/。hit 有古诺尔斯语 hitta 相遇、找到、击中背景；英语名词从击中、一次击打发展出成功作品等用法。',
 [['古诺尔斯语 hitta 等 → hit','相遇、击中 → 达到目标'],['hit + -s → hits；命中比喻和技术用途','多次命中、成功作品或检索结果；单数主语击中']],
 'greatest hits 最受欢迎作品集；search hits 搜索命中结果；hits the target 击中目标。',
 'hits returned by the search；hits reaching the top of the chart。','web hits 有时统计的是对资源的请求次数，不必等于访客人数。歌曲、电影的 hits 则是受欢迎、成功的作品。',
 ('The album contains the band’s biggest hits.','这张专辑收录了乐队最受欢迎的作品。'),('The search returned hundreds of hits.','搜索返回了数百条命中结果。'),sources=['https://en.wiktionary.org/wiki/hits#English','https://en.wiktionary.org/wiki/hit#English'])
W('shots','英 /ʃɒts/；美 /ʃɑːts/','射击、投射；照片、镜头；尝试；小杯烈酒等〔复数〕',
 '一次朝目标发出的动作，是 shots 的射击、投射画面；相机的一次拍摄、做事的一次尝试也沿用它。小杯饮酒等量词义还有自己的历史。',
 'shot + -s，/t/ 后读 /s/。名词接古英语 sceot、scot 等，与 shoot 的旧词族相关；射击动作扩到体育、拍摄和尝试。饮酒用法可能联系旧投下、付款等意义，具体连接不宜硬定。',
 [['古英语射出名词 → shot','一次射出、投射 → 体育、拍摄、尝试'],['不同量词义发展；shot + -s → shots','多次射击、镜头、尝试或小杯饮酒等']],
 'take shots 拍照、投射等〔看对象〕；close up shots 特写镜头；shots of espresso 份装浓缩咖啡；call the shots 作主、决定安排。',
 'shots taken from the bridge；shots at the goal。','shot 也是 shoot 的过去式、过去分词；shots 在本页主要是名词复数。call the shots 是决定事情怎样进行的固定短语。',
 ('She took several shots of the harbour at sunset.','她在日落时拍了几张港口照片。'),('The player had three shots at the goal.','这名球员向球门尝试射门三次。'),('In this small team, the project leader calls the shots.','在这个小团队里，项目负责人作主。'),sources=['https://en.wiktionary.org/wiki/shots#English','https://www.etymonline.com/word/shot'])
W('stores','英 /stɔːz/；美 /stɔːrz/','商店；储备、储藏物〔复数〕；存放、存储〔第三人称单数〕',
 '把供应品留着以后用，是 stores 的储备画面；存放商品、供人挑选购买的地方又发展成商店。动词则说把东西存起来。',
 'store + -s，元音或 /r/ 后读 /z/。经法语相关储备、供应词接拉丁 instaurāre 建立、配备等材料；英语名词与动词逐步形成库存、商店、存储等用途。',
 [['拉丁 instaurāre 词族 → 法语 → store','配备、供应 → 储备、存放'],['store + -s → stores；地点和数字存储用途','多家商店、多项储备；单数主语存储']],
 'department stores 百货商店；food stores 食物储备或食品店〔视语境〕；stores information 存储信息。',
 'stores along the street；stores water for later use。','stores 在街道、购物语境通常是商店，在供应、远行语境可以是储备。stores data 中是动词，用存放的共同画面理解数字信息。',
 ('Several stores stayed open late on Friday.','周五几家商店营业到很晚。'),('The device stores information on a small card.','这个设备把信息存储在一张小卡上。'),sources=['https://en.wiktionary.org/wiki/stores#English','https://en.wiktionary.org/wiki/store#English'])
W('markets','英 /ˈmɑːkɪts/；美 /ˈmɑːrkɪts/','市场、集市；买卖范围〔复数〕；推销、营销〔第三人称单数〕',
 '买卖双方汇到一起，是 markets 的市场画面；它可以是实际摊位，也可以是某类产品面向的买卖范围。把产品推向这些买家，动词也用 market。',
 'market + -s，/t/ 后读 /s/。拉丁 mercārī 交易形成 mercātus，经古法语与晚期古英语等形式进入英语；现代动词由名词发展。',
 [['拉丁 mercārī、mercātus → 法语、英语 market','交易 → 买卖的场所、范围'],['market + -s → markets；名词转动词','多个市场；单数主语面向买家推广']],
 'local markets 当地集市；overseas markets 海外市场；markets the product 推销产品。',
 'markets selling fresh food；markets for different services。','markets 不一定都有实际摊位：the market for software 说软件买卖的需求、客户范围。markets software 作动词则说把软件介绍、销售给买家。',
 ('Local markets sell fresh vegetables and fruit.','当地集市出售新鲜蔬菜和水果。'),('The company markets its products overseas.','这家公司向海外推销产品。'),sources=['https://en.wiktionary.org/wiki/markets#English','https://en.wiktionary.org/wiki/market#English'])
W('falls','英 /fɔːlz/；美 /fɔːlz/、/fɑːlz/','跌落、降幅；瀑布〔复数〕；落下、降低〔第三人称单数〕',
 '东西朝下走，是 falls 最稳的画面；人摔倒、数字下降、水从高处落成瀑布，都沿这个方向理解。',
 'fall + -s，/l/ 后读 /z/。fall 继承古英语 feallan；名词的跌落、降低和瀑布等义有各自发展，现代动词变化是 fall—fell—fallen。',
 [['古英语 feallan → fall 的名动词词族','落下 → 跌落、降低等用途'],['fall + -s → falls；水流名称','多次跌落、多项降幅；单数主语落下；瀑布']],
 'falls in temperature 温度下降；the snow falls 雪落下；the falls at the end of the valley 山谷尽头的瀑布；falls asleep 入睡。',
 'falls from the roof；falls below the line。','动词 falls 后的短语决定落到什么状态：falls asleep 是进入睡眠，falls below 是降到某条线以下。地名中的 Falls 常是瀑布的名称。',
 ('Snow falls on the higher hills in winter.','冬季较高的山丘上会下雪。'),('The path leads to the falls at the head of the valley.','这条小路通向山谷尽头的瀑布。'),sources=['https://en.wiktionary.org/wiki/falls#English','https://en.wiktionary.org/wiki/fall#English'])
W('turns','英 /tɜːnz/；美 /tɜːrnz/','转动、拐弯；轮次、机会〔复数〕；转向、变成〔第三人称单数〕',
 '朝另一个方向转，是 turns；机会在人之间轮着转，就有轮次。颜色、状态转到另一种样子，也能说 turns。',
 'turn + -s，/n/ 后读 /z/。中古英语 turnen 汇合晚期古英语 turnian 与古法语 torner 等路线，接拉丁 tornāre 车旋；名词还受法语 torn、tourn 等影响。',
 [['拉丁 tornāre → 早期英语、法语相关形式 → turn','旋转加工 → 转动、转向；名动词各路交汇'],['turn + -s → turns；次序和状态扩展','多个弯、轮次；单数主语转向或改变状态']],
 'take turns 轮流；sharp turns 急转弯；turns left 向左转；turns red 变红。',
 'turns along the road；takes turns reading。','take turns doing something 是轮流做某事。turns red 后直接接形容词，表示状态转变；turns into something 后接变成的对象。',
 ('The children take turns reading aloud.','孩子们轮流大声朗读。'),('The road turns left after the bridge.','这条路过桥后向左转。'),sources=['https://en.wiktionary.org/wiki/turns#English','https://en.wiktionary.org/wiki/turn#English'])
W('steps','/steps/','脚步；台阶；步骤、措施〔复数〕；迈步〔第三人称单数〕',
 '脚往前迈一次，就是一步；台阶让人一步步上去，步骤让事情一步步做完。steps 把身体动作和抽象流程接在同一个分段画面里。',
 'step + -s，/p/ 后读 /s/。step 延续古英语迈步、步伐词族，台阶与抽象行动阶段等义逐渐扩展；继亲前缀 step- 是另一古词来源。',
 [['古英语步伐、迈步词族 → step','迈一步 → 步子、台阶'],['step + -s → steps；抽象行动扩展','多步、多级台阶、多项措施；单数主语迈步']],
 'follow the steps 按步骤做；take steps 采取措施；stone steps 石阶；steps aside 迈到一旁。',
 'steps leading to the door；steps needed to complete the task。','steps in a process 说流程步骤，take steps to do 常说为实现目标采取措施。walk a few steps 则回到具体迈几步。',
 ('The instructions explain the steps in the process.','说明讲清了这个流程的各个步骤。'),('She steps aside to let the visitors pass.','她迈到一旁，让访客通过。'),sources=['https://en.wiktionary.org/wiki/steps#English','https://en.wiktionary.org/wiki/step#English'])
W('sides','/saɪdz/','侧面、边；各方、立场〔复数〕；站在某一方〔第三人称单数〕',
 '一个物体有不同的边，人们也可能站在事情的不同边上；sides 于是能说实物侧边，也能说不同立场、阵营。',
 'side + -s，/d/ 后读 /z/。side 继承古英语 sīde 的侧面词；队伍、立场、观点等由不同边的空间画面扩展，英语还有站队的动词。',
 [['古英语 sīde → side','身体或物体的一侧 → 边、观察方向'],['side + -s → sides；立场及动词扩展','多条边、多方；单数主语支持某一方']],
 'both sides 两边、双方；sides of the road 路两侧；sides of the argument 争论各方；sides with somebody 支持某人一方。',
 'trees on both sides；sides with the smaller team。','both sides of an argument 可以是两方观点，未必在说几何侧面。sides with someone 中 sides 是动词，表示选择支持哪一方。',
 ('Trees grow on both sides of the road.','路的两侧都长着树。'),('The chair listened to both sides of the argument.','主持人听取了争论双方的意见。'),sources=['https://en.wiktionary.org/wiki/sides#English','https://en.wiktionary.org/wiki/side#English'])
W('links','/lɪŋks/','链环、联系；网页链接〔复数〕；连接〔第三人称单数〕',
 '一环扣着一环，把两处接起来，是 links；人与事的关联、网页之间能跳转的链接，都沿连接功能理解。',
 'link + -s，/k/ 后读 /s/。中古英语的链环 link 通常联系北欧相关词，细节有讨论；英语名动词关系紧密，现代网络借用连接义。',
 [['中古英语链环词、可能北欧来源 → link','链上的环 → 连接、关联'],['link + -s → links；网络用途扩展','多个联系、链接；单数主语连接']],
 'links between... ……之间的联系；transport links 交通联系；click the links 点击链接；links the towns 连接城镇。',
 'links to related pages；links between the two events。','link to 常说明指向哪里，link between 常说明联系两边的对象。一个网页 link 指向资源，现代用途已不限实体链环。',
 ('The page contains links to related articles.','这个页面包含相关文章的链接。'),('The bridge links the two villages.','这座桥连接两个村庄。'),sources=['https://en.wiktionary.org/wiki/links#English','https://en.wiktionary.org/wiki/link#English'])
W('signs','/saɪnz/','标志、标牌；迹象、手势〔复数〕；签名、签署〔第三人称单数〕',
 '让人看见后知道某件事的信息标记，是 signs；路牌直接指路，迹象提示内部情况，签名则用个人的标记表示确认。',
 'sign + -s，/n/ 后读 /z/，g 不发音。名词经古英语 segn、古法语 signe 等接拉丁 signum；动词也有旧英语、法语等来源，现代不同用途逐渐分开。',
 [['拉丁 signum → 古英语、古法语相关形式 → sign','标记 → 标牌、迹象、个人确认标记'],['sign + -s → signs','多个标记、迹象；单数主语签署']],
 'road signs 路标；signs of change 变化迹象；signs the form 在表格上签名；makes signs 做手势。',
 'signs pointing to the station；signs of improvement。','sign 的 g 不发音，signature 等同族词里又会出现 /ɡ/，这是词族读音对应。signs of something 引出迹象所指向的情况。',
 ('The signs point visitors towards the main entrance.','标牌指引访客前往正门。'),('She signs the form at the bottom.','她在表格底部签名。'),sources=['https://en.wiktionary.org/wiki/signs#English','https://en.wiktionary.org/wiki/sign#English'])
W('powers','英 /ˈpaʊəz/；美 /ˈpaʊərz/','能力；权限；强国；幂〔复数〕；提供动力〔第三人称单数〕',
 '有能力让事情发生，是 powers 的共同线索；人能做什么是能力，机构获准能做什么是权限。数学里的幂和机器供能则有专门用法。',
 'power + -s，词尾读 /z/。power 经法语接通俗拉丁重建形式 *potēre 能够，联系拉丁 potis、posse；英语再从名词发展出供能动词。',
 [['拉丁能够词族 → 法语 → power','能够做到 → 能力、权力、动力'],['power + -s → powers；不同领域扩展','多项能力、权限；幂等专门义；单数主语供能']],
 'powers of observation 观察力；limited powers 有限权限；powers of ten 十的幂；powers the pump 为泵供能。',
 'powers granted to the committee；powers used in the calculation。','power 作能源总体时常不可数；powers 常分说不同能力、权限等。The engine powers the pump 中 powers 是动词，说明动力来自哪里。',
 ('The committee has limited powers.','这个委员会的权限有限。'),('The engine powers the pump.','发动机为水泵提供动力。'),('The lesson explains how to write numbers as powers of ten.','这节课讲解怎样把数写成十的幂。'),sources=['https://en.wiktionary.org/wiki/powers#English','https://en.wiktionary.org/wiki/power#English'])
W('attacks','/əˈtæks/','攻击、袭击；抨击〔复数〕；攻击、抨击〔第三人称单数〕',
 '冲着一个目标发力，可能造成损害或提出强烈批评，是 attacks；名词数一次次攻击，动词说谁在攻击什么。',
 'attack + -s，/k/ 后读 /s/。经法语 attaquer 接意大利语 attaccare 等接合、接战材料，名词与动词逐渐形成现代攻击义；与 attach 有历史联系。',
 [['意大利语、法语接合与接战用法 → attack','接战 → 攻击、袭击'],['attack + -s → attacks','多次攻击、批评；单数主语攻击']],
 'verbal attacks 言语攻击；attacks on the proposal 对提案的抨击；attacks the argument 攻击论证。',
 'attacks described in the report；attacks a weak point。','attacks 在计算机、体育、身体等领域还有专门用法，先看目标是什么。普通评论中 attacks a view 常是猛烈批评某种观点。',
 ('The article contains several attacks on the proposal.','这篇文章多次猛烈批评这项提案。'),('She attacks the weakest part of the argument.','她针对论证中最薄弱的部分提出强烈批评。'),sources=['https://en.wiktionary.org/wiki/attacks#English','https://en.wiktionary.org/wiki/attack#English'])
W('guns','/ɡʌnz/','枪、火炮；枪形工具〔gun 的复数〕',
 '能发射的枪、炮是 guns 的常用义；一些握持方式或外形类似的工具，也沿器具形状叫 gun，如喷漆枪、胶枪。',
 'gun + -s，/n/ 后读 /z/。gun 接中古英语 gunne、gonne 等战械名称；更早有从器械昵称、人名而来的分析，也有其他解释，来源未定。',
 [['中古英语 gunne、gonne → gun','战械、火炮 → 枪炮；更早来源未定'],['gun + -s → guns；形状用途扩展','多件枪炮；喷涂、打胶等枪形器具']],
 'historic guns 历史枪炮；paint guns 喷漆枪；glue guns 胶枪。',
 'guns displayed in the museum；guns used for painting furniture。','gun 的具体对象由前面修饰词说明。glue gun 是打胶工具，paint gun 是喷漆工具，不能见到 guns 就把工具句子都译成武器。',
 ('The museum displays guns from several historical periods.','博物馆展出了几个历史时期的枪炮。'),('The workshop stores its paint guns in a locked cabinet.','车间把喷漆枪存放在上锁的柜子里。'),sources=['https://en.wiktionary.org/wiki/guns#English','https://en.wiktionary.org/wiki/gun#English'])
W('troops','/truːps/','部队；军人、士兵〔集合复数〕；成群行进〔第三人称单数〕',
 '聚成队伍的一群人，是 troop 的老画面；troops 在新闻里常合称军人、部队，不一定逐个数有多少支小队。',
 'troop + -s，/p/ 后读 /s/。troop 借自法语 troupe 人群、队伍，更早来源有不同分析；英语又发展出成群行进的动词，troops 还有军人集合用法。',
 [['法语 troupe → 英语 troop','人群、队伍 → 一支队伍；成群走'],['troop + -s → troops；集合用途','多支队伍或军人总称；单数主语成群行进']],
 'troops arriving at the base 到达基地的部队；send troops 派出军人；troops of visitors 一群群访客。',
 'troops returning home；troops helping after the flood。','two troops 可按具体编制数两队；two hundred troops 在常见新闻用法里通常是两百名军人。计数对象要结合句子，不能一律把 troops 当成小队数量。',
 ('The troops returned to the base before nightfall.','部队天黑前返回了基地。'),('Troops helped clear the roads after the flood.','军人在洪水后协助清理道路。'),sources=['https://en.wiktionary.org/wiki/troops#English','https://en.wiktionary.org/wiki/troop#English'])
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_yv',ROOTS,WORDS)
 extend_lessons()
