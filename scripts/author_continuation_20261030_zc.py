"""Frequent gaps: sites, lies, votes, networks, roles and strong-verb forms."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'B4085':dict(words=['site','sites'],label='site → sites：所在地点与网站',note='拉丁位置词经法语等借入，现代互联网沿地点功能命名。'),
 'B2890':dict(words=['lie','lies'],label='lie → lies：躺、位于；说谎另源',note='古英语躺卧词与说谎词不同，现代同形而过去变化各异。'),
 'C1660':dict(words=['vote','votes','voter','voters'],label='vote → votes；voter → voters：选择、票与投票人',note='拉丁誓愿词经法语等发展为正式选择；词与人分开计数。'),
 'B2896':dict(words=['mistake','mistakes'],label='mistake → mistakes：错拿、误认与错误',note='英语 mis 与 take 对应，并有古诺尔斯同族来源的可能影响。'),
 'B3310':dict(words=['network','networks'],label='network → networks：网状结构与相连系统',note='net 与 work 的较早复合，现代可为人际、交通或计算机网络。'),
 'C0955':dict(words=['pass','passes'],label='pass → passes：迈过、通过与通行凭证',note='一步的拉丁材料经法语形成动词，名词还有平行来源。'),
 'B3138':dict(words=['rate','rating'],label='rate → rating：评定与评分结果',note='拉丁核定数值词族经法语等借入，ing 可命名评估过程或结果。'),
 'B4098':dict(words=['track','tracks'],label='track → tracks：足迹、路径与曲目',note='法语足迹词借入，更早可能日耳曼来源，避免直接硬接拉丁 trahere。'),
 'B4610':dict(words=['water','waters'],label='water → waters：水体、水域与浇水',note='本族名词、动词各有古英语旧形式，复数与第三人称形态重合。'),
 'C0168':dict(words=['capture','captured'],label='capture → captured：抓到、留住与捕捉影像',note='拉丁抓取词的名词经法语借入，英语再发展出动词。'),
 'C0627':dict(words=['injury','injuries','injure','injured'],label='injury → injuries；injure → injured：损伤与受伤',note='名词与动词的进入历史分别看，injure 的反构及法语借入两种分析已保留。'),
 'C1235':dict(words=['role','roles'],label='role → roles：卷轴、演员台词与职责',note='法语角色词以写台词的卷纸为背景，和英语 roll 是不同借入线。'),
 'C0990':dict(words=['depend','depends','depending'],label='depend → depends → depending：依靠与条件',note='拉丁从上悬挂的词族形成抽象依赖，谓语与补充条件表达相邻学习。'),
 'A1741':dict(words=['draw','drew','drawn'],label='draw → drew → drawn：拉、画与强变化',note='本族不规则变化，过去式与过去分词的元音、结尾分别记。'),
 'B2957':dict(words=['put','puts'],label='put → puts：放到位置、状态与安排',note='中古英语放、推动词延续，更远来源未定，过去形式仍是 put。'),
}
W('sites','/saɪts/','地点、场地、遗址；网站〔复数〕；选址〔第三人称单数〕',
 '一件事或一个东西具体落在的地方，是 sites；建筑工地、历史遗址、网站，都能按所在的地点理解。',
 'site + -s，/t/ 后读 /s/。site 经盎格鲁诺曼、中古英语接拉丁 situs 位置、地点，与 sinere 放置等旧义有关；网站义是现代功能借用。',
 [['拉丁 situs → 法语相关形式、中古英语 → site','所在位置 → 场地、遗址'],['site + -s → sites；网络与选址用途','多个地点、网站；单数主语给某物选址']],
 'building sites 建筑工地；historic sites 历史遗址；web sites 网站；sites chosen for the project 项目选用的场地。',
 'sites near the river；sites listed in the guide。','sites、sights 景象常同音，但词义不同。sites 强调地点，sights 常是可看的景物；网站也可连写 website，sites 仍能独立作简短称呼。',
 ('The guide lists several historic sites near the town.','指南列出了镇子附近几处历史遗址。'),('The article links to useful sites for language learners.','文章链接到一些对语言学习者有用的网站。'),sources=['https://en.wiktionary.org/wiki/sites#English','https://en.wiktionary.org/wiki/site#English'])
W('lies','/laɪz/','谎言〔复数〕；说谎；躺、位于〔第三人称单数〕',
 '不真实的话是 lies；一个人躺着、一座村庄位于某处，也写 lies。今天同形同音，历史却是两组不同旧词。',
 'lie + -s，/aɪ/ 后读 /z/。躺卧支接古英语 licgan，现代 lie—lay—lain；说谎支接 lēogan，谎言名词有 lyge 等，现代动词 lie—lied—lied。',
 [['古英语 licgan → 躺卧 lie → lies','躺着 → 物体处于某位置、事情在于某处'],['古英语 lēogan、lyge → 说谎、谎言 lie → lies','不实言语；与躺卧支另源']],
 'tell lies 说谎；lies on the sofa 躺在沙发上；lies near the river 位于河边；the problem lies in... 问题在于……。',
 'lies about the event；lies beneath the surface。','tell lies 中 lies 是名词；He lies on the sofa 是躺的动词。The answer lies in... 是答案存在于某处的抽象位置用法。',
 ('The village lies near the river.','村庄位于河边。'),('She asked him not to tell lies.','她请他不要说谎。'),sources=['https://en.wiktionary.org/wiki/lies#English','https://en.wiktionary.org/wiki/lie#English'])
W('votes','英 /vəʊts/；美 /voʊts/','票、投票〔复数〕；投票、表决〔第三人称单数〕',
 '把自己的选择正式表示出来，是 votes 的投票动作；把每个人表达的那一票收起来计数，就是名词 votes。',
 'vote + -s，/t/ 后读 /s/。拉丁 vōtum 誓愿、愿望，接 vovēre 郑重许诺，经法语等发展为英语正式选择的名词、动词。',
 [['拉丁 vōtum、法语等 → vote','誓愿、正式表示意愿 → 投票选择'],['vote + -s → votes','若干票、表决；单数主语投票']],
 'count votes 计票；votes for and against 赞成票与反对票；votes in the election 在选举中投票。',
 'votes recorded by the committee；votes for a new leader。','votes 数票或表决动作，voters 数人。votes for somebody 可以是支持某人的票，也可是单数主语投票支持某人，按句法判断。',
 ('The committee counted the votes after the meeting.','委员会在会后计票。'),('Each member votes for one candidate.','每位成员投票选择一名候选人。'),sources=['https://en.wiktionary.org/wiki/votes#English','https://en.wiktionary.org/wiki/vote#English'])
W('mistakes','/mɪˈsteɪks/','错误、失误〔复数〕；误认、误解〔第三人称单数〕',
 '拿错、理解错、选择错，都能落到 mistakes 的核心：把事情当成了不该当成的样子。名词再把做错的那一处数出来。',
 'mistake + -s，/k/ 后读 /s/。现代可认 mis- 错与 take 拿；历史可能是英语组合、古诺尔斯 mistaka 借入或两者交汇，名词错误义从动词发展。',
 [['mis- + take／古诺尔斯 mistaka 等 → mistake 动词','拿错、误解 → 发生错误'],['名词 mistake + -s → mistakes；动词同形变化','多个失误；单数主语把 A 误当 B']],
 'make mistakes 犯错；correct mistakes 改错；mistakes A for B 把 A 误认成 B。',
 'mistakes in the text；mistakes a shadow for a person。','名词常说 make a mistake；动词 mistake something for something 说明把什么认成什么。它的过去式 mistook，过去分词 mistaken。',
 ('She corrected the mistakes in the first draft.','她改正了初稿中的错误。'),('He often mistakes the two brothers for each other.','他经常把这兄弟俩认混。'),sources=['https://en.wiktionary.org/wiki/mistakes#English','https://www.etymonline.com/word/mistake'])
W('networks','英 /ˈnetwɜːks/；美 /ˈnetwɜːrks/','网络、相连系统；关系网〔复数〕；建立联系〔第三人称单数〕',
 '许多点和线像网一样接起来，是 networks；交通线路、电脑、人际联系都能组成这样的相连系统。',
 'net 网 + work 制成物、结构 → network，再加 -s，/k/ 后读 /s/。先有网状实体结构，后来扩展到不同连接系统和建立联系的动词。',
 [['net + work → network','网状制成物、结构 → 互相连接的系统'],['network + -s → networks；现代领域扩展','多个网络；单数主语主动建立联系']],
 'transport networks 交通网络；computer networks 计算机网络；social networks 社交网络。',
 'networks linking towns；networks of local volunteers。','network 关注多个节点怎样相连，不只互联网。links 可以数其中的连接，networks 则把整套系统框起来。',
 ('The map shows the region’s transport networks.','地图展示了这个地区的交通网络。'),('The project connects networks of local volunteers.','这个项目把当地志愿者的联系网络连接起来。'),sources=['https://en.wiktionary.org/wiki/networks#English','https://en.wiktionary.org/wiki/network#English'])
W('passes','英 /ˈpɑːsɪz/；美 /ˈpæsɪz/','经过、通过；递交、传递〔第三人称单数〕；通行证等〔复数〕',
 '从这边跨到那边，是 passes 的通过画面；时间过去、东西递给别人，也能用 pass。允许通过的证件再叫 passes。',
 'pass + -es，/s/ 后增加 /ɪz/。拉丁 passus 一步，经重建通俗拉丁 *passāre 与法语 passer 进入英语；名词还有法语 pas 等及英语动词转用路径。',
 [['拉丁 passus、*passāre → 法语 → pass','一步、迈过 → 经过、通过'],['pass + -es → passes；凭证名词等用途','单数主语经过、递给；多个通行凭证']],
 'passes the test 通过测试；passes the ball 传球；time passes 时间过去；visitor passes 访客通行证。',
 'passes through the village；passes the book to her friend。','passes 可以说人经过，也可说主语把东西传给谁。a pass 作证件时数一张，passes 是多张；和过去 past 的拼写区分。',
 ('The bus passes through the village every morning.','公共汽车每天早晨经过这个村庄。'),('Visitors collect their passes at reception.','访客在前台领取通行证。'),sources=['https://en.wiktionary.org/wiki/passes#English','https://en.wiktionary.org/wiki/pass#English'])
W('rating','/ˈreɪtɪŋ/','评价、评级〔现在分词、动名词〕；评分、等级',
 '把表现、质量等按某个尺度评出位置，就是 rating；评出来的分数、等级，也可直接称为 a rating。',
 'rate 去 e 加 -ing → rating。rate 的数值、评定支经法语等接拉丁 rāta 核定份额，联系 rērī 计算、判断；英语 ing 形成评估过程与结果名词。',
 [['拉丁 rāta 等 → 法语、英语 rate','核定份额、数值 → 评价、定等级'],['rate → rating','去 e 加 ing；正在评估或评定结果']],
 'a high rating 高评分；rating the entries 给参赛作品评分；a star rating 星级评分。',
 'ratings based on visitor reviews；rating each item separately。','a rating 是一次结果或一项等级；rating something 可以是正在评价。ratings 作为复数还常用于节目收视等领域，具体按上下文看尺度。',
 ('The visitors gave the exhibition a high rating.','访客给这个展览很高的评分。'),('The judges are rating each entry separately.','评委正在逐件给参赛作品评分。'),sources=['https://en.wiktionary.org/wiki/rating#English','https://en.wiktionary.org/wiki/rate#English'])
W('tracks','/træks/','足迹、踪迹；轨道、路径；曲目〔复数〕；跟踪〔第三人称单数〕',
 '走过留下痕迹，顺着痕迹就能找到路线，是 tracks；铁路规定行进路线，唱片、录音也形成记录、播放的通路，后来有曲目义。',
 'track + -s，/k/ 后读 /s/。中古英语借古法语 trac 足迹、马的踪迹，更早可能日耳曼来源，具体未定；动词由名词发展出循迹跟随。',
 [['古法语 trac → 中古英语 → track','足迹、痕迹 → 路线、轨道'],['track + -s → tracks；录音用途、动词扩展','多个痕迹、轨道、曲目；单数主语跟踪']],
 'animal tracks 动物足迹；railway tracks 铁轨；album tracks 专辑曲目；tracks progress 追踪进度。',
 'tracks in the mud；tracks on the recording。','tracks 在音乐场景可说独立曲目，在制作里还可说音轨。keep track of something 是持续掌握情况的固定短语。',
 ('We found animal tracks in the mud.','我们在泥地里发现了动物足迹。'),('The album contains twelve tracks.','这张专辑包含十二首曲目。'),sources=['https://en.wiktionary.org/wiki/tracks#English','https://www.etymonline.com/word/track'])
W('waters','英 /ˈwɔːtəz/；美 /ˈwɔːtərz/、/ˈwɑːtərz/','水域、大片水体〔复数用法〕；浇水〔第三人称单数〕',
 'water 把水当作总体；waters 常把某片海、湖的水域作为场景来谈。把水给到植物等对象，动词也写 waters。',
 'water + -s，词尾读 /z/。名词继承古英语 wæter，动词有 wæterian 的旧形；现代水域复数和给水动作按各自名动词用途解释。',
 [['古英语 wæter、wæterian → water 名动词','水；给水、浇水'],['water + -s → waters','水域、大片水体；单数主语浇水']],
 'coastal waters 沿海水域；calm waters 平静水面；waters the plants 给植物浇水。',
 'waters around the island；waters the garden each morning。','一般喝水说 water，通常不可数；waters 多用于地理、景色中的水域。She waters the plants 中则是动词，让植物得到水。',
 ('The boat moved into calmer waters near the island.','船驶入岛旁较平静的水域。'),('She waters the plants every morning.','她每天早晨给植物浇水。'),sources=['https://en.wiktionary.org/wiki/waters#English','https://en.wiktionary.org/wiki/water#English'])
W('captured','英 /ˈkæptʃəd/；美 /ˈkæptʃərd/','捕获、抓住；捕捉影像、吸引〔capture 的过去式、过去分词〕',
 '把原来可能溜走的东西抓住、留住，是 captured；镜头留住瞬间，故事抓住注意力，都是这个画面的现代扩展。',
 'capture 已有 e，加 -d，词尾读 /d/。拉丁 capere 抓的 capt- 形成 captūra，经法语进入英语名词，英语再发展为捕获动词。',
 [['拉丁 capere、capt- → captūra → 法语、英语 capture','抓取 → 捕获这一行为或结果'],['capture 去 e + -ed → captured；记录、注意力用途','抓住了、留下影像；吸引了']],
 'captured the moment 捕捉瞬间；captured attention 吸引注意；captured in a photograph 留在照片中。',
 'captured by the camera；captured the audience’s interest。','capture 常让人想到把目标抓住、留住，record 更常强调把内容保存下来。摄像机 captured a movement，可以突出瞬间没有漏掉。',
 ('The camera captured the movement clearly.','相机清楚捕捉到了这个动作。'),('The opening story captured everyone’s attention.','开场的故事吸引了所有人的注意。'),sources=['https://en.wiktionary.org/wiki/captured#English','https://en.wiktionary.org/wiki/capture#English'])
W('injuries','/ˈɪndʒəriz/','伤、损伤〔injury 的复数〕',
 '身体某个部分受了损害，把一次次或不同部位的伤分开数，就是 injuries；和痛的感觉相比，它更关注损伤本身。',
 'injury 的 y 前是辅音 r，变 y 为 i 加 -es，词尾读 /z/。经法语 injurie 接拉丁 iniūria 不公、侵害，较早为 in- 不与 iūs 权利、公道的组合。',
 [['拉丁 iniūria → 法语 injurie → injury','不公、侵害 → 损害、身体损伤'],['injury → injuries','y 变 i 加 es；多处、多次损伤']],
 'minor injuries 轻伤；sports injuries 运动损伤；injuries to the hand 手部损伤。',
 'injuries recorded after the accident；injuries affecting different parts of the body。','injuries 可数具体伤，injury 也可不可数地说伤害总体。wounds 常突出破口、创口；injuries 的范围更宽。',
 ('The report records injuries from the accident.','报告记录了事故中的伤情。'),('Several players missed the match because of injuries.','几名队员因伤缺席比赛。'),sources=['https://en.wiktionary.org/wiki/injuries#English','https://en.wiktionary.org/wiki/injury#English'])
W('roles','英 /rəʊlz/；美 /roʊlz/','角色；职责、作用〔role 的复数〕',
 '一个人在一出戏、一个团队里分到什么部分，就是 roles；较早演员的台词写在一卷纸上，纸卷的名字后来用来称那份角色。',
 'role + -s，元音后读 /z/。法语 rôle 角色，较早接 rolle、拉丁 rotulus 卷轴，联系 rotula 小轮、rota 轮；英语 role 与更早借入的 roll 是不同路线。',
 [['拉丁轮、卷轴材料 → 法语 rolle、rôle','卷起的纸；写演员台词的卷纸 → 角色'],['英语 role + -s → roles','多个戏剧角色；团队、生活中的职责作用']],
 'leading roles 主角；different roles 不同职责；roles in the project 项目里的分工。',
 'roles played by the actors；roles assigned to team members。','play a role 可说扮演角色，也可说发挥作用。roles 与 rolls 常同音，前者是角色、职责，后者可能是卷、面包卷等同族另一路词。',
 ('The actors changed roles during the rehearsal.','演员们排练时交换了角色。'),('Each team member has several roles in the project.','每位团队成员在项目中承担几项职责。'),sources=['https://en.wiktionary.org/wiki/roles#English','https://www.etymonline.com/word/role'])
W('depends','/dɪˈpendz/','取决于；依赖〔depend 的第三人称单数〕',
 '结果靠某个条件支撑，条件变了结果也会变，就是 depends；像挂着的东西要靠上面的支点。',
 'depend + -s，/d/ 后读 /z/。拉丁 dē- 从、向下与 pendēre 悬挂形成 dēpendēre，经法语或直接拉丁进入英语，较早已有条件、依赖的抽象用途。',
 [['拉丁 dēpendēre → 法语、英语 depend','从上悬挂 → 由条件支撑、依赖'],['depend + -s → depends','单数主语取决于、依赖']],
 'depends on the weather 取决于天气；depends on help 依赖帮助；It depends 要看情况。',
 'depends on what you choose；depends on the route。','depends 常接 on、upon 引出支撑条件。It depends 单独说时，通常是在表示还要看条件，后面可以继续说明是哪一项。',
 ('The journey time depends on the route.','路程所需时间取决于走哪条路线。'),('The garden depends on regular rainfall.','这个花园依赖规律的降雨。'),sources=['https://en.wiktionary.org/wiki/depends#English','https://www.etymonline.com/word/depend'])
W('drawn','英 /drɔːn/；美 /drɔːn/、/drɑːn/','拉、画；吸引、得出〔draw 的过去分词〕',
 '东西被拉到某处、线条被画出来、注意力被引过去，都可用 drawn。它是过去分词，常出现在 has drawn、was drawn 等结构里。',
 'draw—drew—drawn 是本族不规则变化，drawn 的结尾保留旧分词形式痕迹。较早接古英语 dragan、后来的 drawen 等，不把现代 awn 看作画画专用后缀。',
 [['古英语 dragan 等 → draw','拉 → 画线、吸引、推进到结论等'],['draw—drew—drawn','过去式 drew；过去分词 drawn，元音分别记']],
 'has drawn a map 已画地图；was drawn by 由……画出；drawn to music 被音乐吸引；conclusions drawn 得出的结论。',
 'a map drawn by a child；visitors drawn to the exhibition。','drew 是不带 have 的一般过去式；drawn 常与 have、be 等组成完成、被动结构。被吸引也可说 be drawn to something。',
 ('The map was drawn by a local artist.','这张地图由当地一位画家绘制。'),('The exhibition has drawn visitors from several nearby towns.','这个展览吸引了附近几个镇的访客。'),sources=['https://en.wiktionary.org/wiki/drawn#English','https://en.wiktionary.org/wiki/draw#English'])
W('puts','/pʊts/','放、置；使处于某状态〔put 的第三人称单数〕',
 '把东西安到一个位置，或者让事情进入一种状态，就是 puts；具体地方、状态常在后面补出来。',
 'put + -s，/t/ 后读 /s/，u 读 /ʊ/。put 经中古英语 putten 等延续，较早有推动、放置用法，更远来源未定；过去式、过去分词仍是 put。',
 [['中古英语 putten 等 → put','推、安放 → 放置、使处于状态'],['put + -s → puts','单数主语放、使进入某位置或状态']],
 'puts the book on the shelf 把书放上架；puts quality first 把质量放第一；puts an end to... 结束……。',
 'puts the keys in a drawer；puts the plan into action。','put 常需要补足放在哪里、放成怎样，puts the book 后还要看 on the shelf 等。puts somebody at ease 是让某人放松的状态表达。',
 ('She puts her keys in the same drawer each evening.','她每天晚上把钥匙放进同一个抽屉。'),('The team puts clear communication first.','这个团队把沟通清楚放在第一位。'),sources=['https://en.wiktionary.org/wiki/puts#English','https://en.wiktionary.org/wiki/put#English'])
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_zc',ROOTS,WORDS)
 extend_lessons()
