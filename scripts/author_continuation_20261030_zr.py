"""Places, reports, conversations and people across generations."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'B3576':dict(words=['spot','spots'],label='spot → spots：小点、地方与发现',note='中古英语斑点词有本族、低地日耳曼相关来源，地点和发现义后发展。'),
 'C1404':dict(words=['statistics','stats'],label='statistics → stats：统计信息的常用缩短',note='统计学科接国家事务的学术词史，stat 的数据义再加复数 s。'),
 'B4460':dict(words=['temperature','temperatures'],label='temperature → temperatures：调配到冷热程度',note='拉丁适当比例、调和词族，现代温度义后来专门化。'),
 'B3112':dict(words=['stone','stones'],label='stone → stones：石块、果核与重量',note='本族石词，不同物品中的硬核、材料和动作用途分开。'),
 'A2077':dict(words=['update','updates'],label='update → updates：把信息推进到当前',note='up 与 date 的现代组合，动词后重音、名词前重音。'),
 'A1862':dict(words=['conversation','conversations'],label='conversation → conversations：相处、交往到谈话',note='法语及拉丁 conversationem 借入，英语现代口头交流义后发展。'),
 'B3971':dict(words=['estimate','estimates'],label='estimate → estimates：估出的数与估算动作',note='拉丁估价词族，名词尾 /mət/、动词尾 /meɪt/ 分别标出。'),
 'B3754':dict(words=['gate','gates'],label='gate → gates：入口、门与登机口',note='古英语门词，北欧道路词和现代丑闻后缀另有支线。'),
 'B3136':dict(words=['nut','nuts'],label='nut → nuts：坚果、螺母与口语',note='本族坚果词，机械形状及人物口语用途后扩展。'),
 'C1235':dict(words=['round','rounds'],label='round → rounds：一圈、一轮与巡回',note='法语圆的词接拉丁 rotundus，名词及动词在现代各有用途。'),
 'C1635':dict(words=['visit','visits','visited','visiting'],label='visit → visits → visited → visiting：拜访、访问与参观',note='拉丁看的加强形式经法语进入，名词动作及动词形式相邻。'),
 'B2480':dict(words=['warrior','warriors'],label='warrior → warriors：作战者',note='法语 war 词族人物名词借入，不把 rior 当现代通用后缀。'),
 'C0659':dict(words=['colleague','colleagues'],label='colleague → colleagues：共同任职的人',note='拉丁共同与委任组成，经法语借入。'),
 'B3634':dict(words=['follow','follower','followers'],label='follow → follower → followers：跟随、关注的人',note='本族跟随动词加人物 er，现代社交平台义后扩展。'),
 'C0475':dict(words=['generation','generations'],label='generation → generations：一代代人与技术',note='拉丁生出、产生的名词借入，年龄阶段和产品代次均由分代理解。'),
 'B4280':dict(words=['journalist','journalists'],label='journalist → journalists：面向公共报道的人',note='法语 journaliste 与 journal 加人物 ist 的构成，现代新闻职业用途。'),
}
W('spots','英 /spɒts/；美 /spɑːts/','斑点、污点；地点、空位〔复数〕；发现、认出〔第三人称单数〕',
 '在一大片东西里单独显出的一小点，是 spots；把地图上的一个点当作地点，或从背景里看见一个目标，也能沿这条线理解。',
 'spot + -s，/t/ 后读 /s/。中古英语 spot、spotte 联系低地日耳曼词及本族 splott 等形式，词形关系多路；地点、位置和发现的动词用途后来发展。',
 [['中古英语及相关斑点词 → spot','显出的小点 → 某个地点、位置'],['spot + -s → spots；动词扩展','多个斑点、地点；单数主语看见、发现']],
 'spots on the shirt 衬衫上的污点；quiet spots 安静的地方；spots a mistake 发现错误。',
 'parking spots 停车位；spots of colour 色点。','spot 强调具体一处、一个小点，和整个 area 区域相比更聚焦。spots 还可指皮肤斑点、痘点，按具体上下文判断。',
 ('The guide lists quiet spots for a picnic.','指南列出几处适合野餐的安静地方。'),('She usually spots mistakes in the first draft.','她通常能发现初稿里的错误。'),sources=['https://en.wiktionary.org/wiki/spots#English','https://en.wiktionary.org/wiki/spot#English'])
W('stats','/stæts/','统计数据、统计信息〔口语缩短形式〕',
 '把表现、数量或变化浓缩成几项数字，日常随口叫 stats。比赛成绩、网站访问量、调查结果，都能有各自的 stats。',
 'statistic 缩成 stat，再加 -s → stats，也常整体对应 statistics 的缩短表达。statistics 较早经德语等学术词接国家事务与拉丁 status，数据缩写是更晚的英语用法。',
 [['statistics、statistic → stat 数据义','长的统计词缩成口语短形式'],['stat + -s → stats','多项统计数字、概括的统计信息']],
 'player stats 球员数据；website stats 网站统计；check the stats 查看数据。',
 'stats for the season 本赛季数据；basic stats 基本统计信息。','stats 是较随意的统计简称；正式写作可按具体内容用 statistics、data。体育、网站分析中的 stats 通常是多个指标或数字的汇总。',
 ('The coach checked the players’ stats after the match.','教练在赛后查看了球员数据。'),('The website shows basic stats for each article.','网站展示每篇文章的基本统计信息。'),sources=['https://en.wiktionary.org/wiki/stats#English','https://www.etymonline.com/word/stat'])
W('temperatures','英 /ˈtemprətʃəz/；美 /ˈtemprətʃərz/','温度、不同测得的冷热程度〔复数〕',
 '不同地方、时刻或物体各有自己的冷热程度，把这些温度分别比较，就是 temperatures。可以是室内外、白天夜晚或几份样本的数值。',
 'temperature + -s，末尾读 /z/。temperature 接拉丁 temperātūra 调和、适当比例，联系 temperāre 调到适度；英语较早说性质、配比，科学冷热程度义后来发展。',
 [['拉丁 temperātūra → temperature','调配、适当比例 → 性质；后为冷热程度'],['temperature + -s → temperatures','多个时刻、对象或地点的温度']],
 'high temperatures 高温；temperatures at night 夜间温度；different temperatures 不同温度。',
 'record temperatures 记录温度；temperatures below zero 零度以下的温度。','temperature 本身是冷热程度，不直接规定摄氏或华氏。比较具体数值时要看单位；temperatures 可以把不同对象、时点的测量分开说。',
 ('Temperatures fall quickly after sunset in the desert.','沙漠中日落后温度下降很快。'),('The students compared the temperatures in three rooms.','学生比较了三个房间的温度。'),sources=['https://en.wiktionary.org/wiki/temperatures#English','https://www.etymonline.com/word/temperature'])
W('stones','英 /stəʊnz/；美 /stoʊnz/','石头、石块；果核；英石〔复数等〕；去果核、投石〔第三人称单数〕',
 '一块块硬实的石头是 stones；桃、李子里硬的果核也可这样叫。作动词时可说去掉果核，或向某物投石，动作方向要看宾语。',
 'stone + -s，/n/ 后读 /z/。stone 继承古英语 stān 石，材料、石块、果核、重量等用途逐步形成，动词可以表示加、去或用石类物体作动作。',
 [['古英语 stān → stone','石、石质材料 → 石块、硬果核等'],['stone + -s → stones；动词用途','多块石头、多枚果核；单数主语去核、投石']],
 'small stones 小石子；stones in the path 路上石块；plum stones 李子核；stones the fruit 给水果去核。',
 'smooth stones 光滑石子；remove the stones 去掉果核。','果核的 stone 在英式英语常见，美式常说 pit。英石是重量单位，数值后常保持 stone，如 ten stone；其他语境也能见复数 stones。',
 ('The children collected smooth stones by the river.','孩子们在河边收集光滑的石子。'),('Remove the stones from the plums before cooking them.','煮李子前先去核。'),sources=['https://en.wiktionary.org/wiki/stones#English','https://en.wiktionary.org/wiki/stone#English'])
W('updates','名词 /ˈʌpdeɪts/；动词 /ʌpˈdeɪts/','最新消息、更新〔复数〕；更新〔第三人称单数〕',
 '原来的内容停在昨天，把今天新知道的部分补上，就是 updates。名词可以是一条条新进展，也可以是软件的新版本内容。',
 'up- + date 日期、使标上日期 → update，再加 -s，/t/ 后读 /s/。这是现代英语更新到当前的组合，先有动词用途，再发展名词，重音有分化。',
 [['up + date → update 动词','推进到当前日期 → 使信息保持最新'],['名词 update 与 update + -s → updates','多条新进展；单数主语进行更新']],
 'regular updates 定期进展消息；software updates 软件更新；updates the list 更新名单。',
 'updates on the project 项目最新进展；updates the page daily 每天更新网页。','名词最新消息前重音，动词更新后重音。updates on something 给某事进展，updates something 作动词则直接更新某物。',
 ('The team sends weekly updates on the project.','团队每周发送项目进展消息。'),('She updates the list whenever a new member joins.','每有新成员加入，她就更新名单。'),sources=['https://en.wiktionary.org/wiki/updates#English','https://en.wiktionary.org/wiki/update#English'])
W('conversations','英 /ˌkɒnvəˈseɪʃənz/；美 /ˌkɑːnvərˈseɪʃənz/','谈话、交谈〔复数〕',
 '几个人把想法来回说给彼此听，一次次这样的交流就是 conversations。可以轻松闲聊，也可以认真谈某个问题。',
 'conversation + -s，/n/ 后读 /z/。名词经法语 conversacion 及拉丁 conversātiō 借入，连到 conversārī 与人相处、交往，较早 con- 与 versāre 转动的材料；英语口头交流义后来居于中心。',
 [['拉丁 conversātiō → 法语及英语 conversation','相处、交往、生活方式 → 口头思想交流'],['conversation + -s → conversations','几次谈话、不同主题的交谈']],
 'have conversations 进行交谈；conversations with friends 与朋友谈话；conversations about work 关于工作的谈话。',
 'everyday conversations 日常会话；private conversations 私人交谈。','conversation 常强调双方或多方交流，speech 常是一人向听众讲话。with 给交谈对象，about 给话题；不是现代 converse 临时加 ation 才有全部词史。',
 ('She practised English through everyday conversations.','她通过日常会话练习英语。'),('Our conversations often return to the books we are reading.','我们的谈话常又回到正在读的书上。'),sources=['https://en.wiktionary.org/wiki/conversations#English','https://www.etymonline.com/word/conversation'])
W('estimates','名词 /ˈestɪməts/；动词 /ˈestɪmeɪts/','估计数、估算、报价〔复数〕；估计〔第三人称单数〕',
 '资料还不够逐项精确算定，就先给一个有依据的大致数值，是 estimates。名词数的是估出的结果，动词说谁在进行估算。',
 'estimate + -s，/t/ 后读 /s/。底词接拉丁 aestimāre 估价、评价及 aestimātus 分词材料；英语名词、动词有各自发展，名词尾 /mət/，动词尾 /meɪt/。',
 [['拉丁 aestimāre、aestimātus → estimate','评价、估价 → 估算数值'],['estimate + -s → estimates；词性读法区分','多个估计、报价；单数主语估计']],
 'rough estimates 粗略估计；cost estimates 成本估算；estimates the time 估计耗时。',
 'compare estimates 比较估算；estimates that... 估计……。','estimates 是估算，精确程度依方法、资料而定，不等于随口猜。维修或施工语境 an estimate 常是预计报价，与确定最终账单要分清。',
 ('The two estimates of the cost were quite different.','两份成本估算差别很大。'),('She estimates that the walk will take two hours.','她估计这段路要走两个小时。'),sources=['https://en.wiktionary.org/wiki/estimates#English','https://en.wiktionary.org/wiki/estimate#English'])
W('gates','/ɡeɪts/','大门、栅栏门；入口、登机口〔复数〕',
 '在边界上留出一个可以开关、让人通过的口，是 gates。机场也把旅客进入某个登机通路的入口叫 gate。',
 'gate + -s，/t/ 后读 /s/。门义接古英语 geat、gatu 等，经中古英语延续；街名中表路的 gate 有北欧 gata 的另一来源，现代丑闻词尾 gate 又来自 Watergate 名称。',
 [['古英语门的旧形式 → gate','可通行的边界入口 → 大门、特定通道口'],['gate + -s → gates；机场用途扩展','多个门、入口或登机口']],
 'the school gates 学校大门；airport gates 机场登机口；open the gates 开门。',
 'gates to the garden 花园入口；departure gates 出发登机口。','gates 的门义和街名、丑闻后缀同形，不必合成一条意义线。机场 gate 是分配的登机口，和 terminal 航站楼不是同一层级。',
 ('The park gates close at sunset.','公园大门在日落时关闭。'),('The screen shows the departure gates for all flights.','屏幕显示所有航班的出发登机口。'),sources=['https://en.wiktionary.org/wiki/gates#English','https://en.wiktionary.org/wiki/gate#English'])
W('nuts','/nʌts/','坚果、螺母〔复数〕；发疯似的、痴迷的〔口语〕',
 '壳里有硬实果仁的食物常叫 nuts；拧在螺栓上固定东西的小零件也叫 nuts。口语的 go nuts、nuts about 则按情绪强烈、特别痴迷的固定用法学。',
 'nut + -s，/t/ 后读 /s/。nut 继承古英语 hnutu 坚果，螺母是后来按形状等扩展的机械名词；人物口语用途另有引申史，不把所有义项都从硬壳直接推出。',
 [['古英语 hnutu → nut','坚果 → 后有螺母等形状借义'],['nut + -s → nuts；口语性质用途','多个坚果、螺母；情绪或喜爱很强烈']],
 'a bowl of nuts 一碗坚果；nuts and bolts 螺母和螺栓；nuts about music 痴迷音乐。',
 'tighten the nuts 拧紧螺母；go nuts 兴奋、气恼到失控似的。','食物 nut 的日常范围和植物学严格分类并不完全一致。the nuts and bolts of a task 也可比喻一件事最基本、实际的细节。',
 ('She put a bowl of nuts on the table.','她在桌上放了一碗坚果。'),('Check that all the nuts and bolts are tight.','检查所有螺母和螺栓都已拧紧。'),sources=['https://en.wiktionary.org/wiki/nuts#English','https://en.wiktionary.org/wiki/nut#English'])
W('rounds','/raʊndz/','一轮轮、一圈圈；巡诊、巡查；回合〔复数〕；绕过、使成圆形〔第三人称单数〕',
 '沿着一圈依次走过，就有 rounds 的巡回画面；把同一套活动再完成一遍，也是一轮。比赛、讨论、分发物品都可以按轮次进行。',
 'round + -s，/d/ 后读 /z/。round 经法语 ront、rount 接拉丁 rotundus 圆的，名词一圈、一轮及动词绕行、使圆等用途后来发展；低声说话的旧同形词另源。',
 [['拉丁 rotundus → 法语 → round','圆的 → 一圈、一次完整巡回'],['round + -s → rounds','多轮、多个回合；单数主语绕过或使圆']],
 'rounds of talks 几轮会谈；make the rounds 巡回走访、广为流传；hospital rounds 医院巡诊。',
 'several rounds of discussion 几轮讨论；rounds the corner 转过街角。','a round of drinks 是给一组人买的一轮饮品；rounds 可按同一套动作完成几次来数。医疗、警卫等的 rounds 常是依次巡视相关地点。',
 ('The plan went through three rounds of discussion.','计划经过了三轮讨论。'),('The doctor makes the rounds each morning.','医生每天早晨巡诊。'),sources=['https://en.wiktionary.org/wiki/rounds#English','https://en.wiktionary.org/wiki/round#English'])
W('visits','/ˈvɪzɪts/','拜访、到访、参观〔复数〕；前去看、访问〔第三人称单数〕',
 '为见某个人、看看某个地方而专门去一趟，就是 visits。名词数去过几趟，动词说某个人会去哪里、看谁。',
 'visit + -s，/t/ 后读 /s/。visit 经法语 visiter 接拉丁 vīsitāre，是 vidēre 看的加强、反复词族；英语名词到访后从相关动词用途发展。',
 [['拉丁 vīsitāre → 法语 → visit','前去看看、探访 → 拜访、参观'],['visit + -s → visits','多次到访；单数主语去拜访、参观']],
 'visits to the museum 去博物馆的参观；visits her parents 看望父母；regular visits 定期到访。',
 'visits the website 浏览网站；home visits 上门访问。','visit somebody 或 visit a place 作动词通常直接接对象；a visit to somebody、a visit to a place 作名词常接 to。',
 ('She visits her grandparents every Sunday.','她每周日看望祖父母。'),('The school arranges regular visits to local museums.','学校定期安排参观当地博物馆。'),sources=['https://en.wiktionary.org/wiki/visits#English','https://en.wiktionary.org/wiki/visit#English'])
W('warriors','英 /ˈwɒriəz/；美 /ˈwɔːriərz/','战士、武士；斗士〔复数〕',
 '以作战身份参与战斗的人，是 warriors。描写古代武士、神话战士很常见，现代也可比喻为某个目标奋力争取的人。',
 'warrior + -s，末尾读 /z/。warrior 经中古英语 werreour 接盎格鲁法语 werreur、古法语相关人物词，与 war 的法语词族相连，更早有日耳曼来源。',
 [['法语战争词族人物名词 → warrior','参与作战的人 → 战士、武士'],['warrior + -s → warriors','多位战士；比喻为目标战斗的人']],
 'ancient warriors 古代战士；warriors in the story 故事中的武士；a group of warriors 一队战士。',
 'portraits of warriors 战士画像；warriors defending the city 保卫城市的战士。','warrior 偏作战者的身份形象，soldier 常指军队编制中的士兵；在文学、神话中两者范围不必相同。现代比喻义要看修饰内容。',
 ('The story follows a group of warriors on a long journey.','故事讲述一群战士的漫长旅程。'),('The museum displays armour worn by ancient warriors.','博物馆展出古代战士穿过的盔甲。'),sources=['https://en.wiktionary.org/wiki/warriors#English','https://en.wiktionary.org/wiki/warrior#English'])
W('colleagues','英 /ˈkɒliːɡz/；美 /ˈkɑːliːɡz/','同事、同僚〔复数〕',
 '同在一个组织、工作领域里一起任职做事的人，是 colleagues。可以在同一个办公室，也可以是同一专业、机构里需要合作的人。',
 'colleague + -s，/ɡ/ 后读 /z/。经法语 collègue 接拉丁 collēga 同僚，较早 com- 共同与 lēgāre 委任的词族相连，g 前的 ue 不另发音。',
 [['拉丁 collēga → 法语 collègue → colleague','共同任职的人 → 同事、同僚'],['colleague + -s → colleagues','多位工作中的同事、专业同僚']],
 'work with colleagues 与同事合作；former colleagues 以前的同事；colleagues in another department 别的部门同事。',
 'discuss it with colleagues 与同事讨论；supportive colleagues 愿意支持人的同事。','colleague 强调工作或专业关系，classmate 强调同班，friend 强调朋友关系。几种身份可以重合，但这个词本身不保证关系亲密。',
 ('She discussed the idea with her colleagues.','她与同事讨论了这个想法。'),('My colleagues helped me learn the new system.','同事帮助我学会使用新系统。'),sources=['https://en.wiktionary.org/wiki/colleagues#English','https://en.wiktionary.org/wiki/colleague#English'])
W('followers','英 /ˈfɒləʊəz/；美 /ˈfɑːloʊərz/','跟随者、支持者；关注者〔复数〕',
 '沿着某个人的路走，是 followers 的跟随者画面。可以追随一种思想，也可以在社交平台持续看某人的内容。',
 'follow + -er → follower，再加 -s，末尾读 /z/。follow 接古英语 folgian、fylgan 等本族跟随词；er 命名跟随主体，社交平台关注义是现代功能扩展。',
 [['古英语跟随词 → follow；加 -er → follower','跟在后面、追随 → 跟随者、支持者'],['follower + -s → followers；平台用途','多位追随者；订阅、关注某账号的人']],
 'followers of a movement 某运动的追随者；social media followers 社交平台关注者；gain followers 获得关注者。',
 'a group of followers 一群追随者；share news with followers 向关注者分享消息。','平台 follower 说明关注关系，不自动表示赞成每条内容。fans 更突出喜爱、支持，followers 范围常更宽。',
 ('The artist shared sketches with her followers.','这位艺术家向关注者分享了草图。'),('The writer gained followers through regular short essays.','这位作者通过定期发布短文获得了关注者。'),sources=['https://en.wiktionary.org/wiki/followers#English','https://en.wiktionary.org/wiki/follower#English'])
W('generations','/ˌdʒenəˈreɪʃənz/','几代人；世代、代次〔复数〕',
 '人一代代生长，产品也一代代更新，generations 把前后相接的群体或阶段分开看。它可以谈家族、社会，也可以谈技术。',
 'generation + -s，/n/ 后读 /z/。generation 经法语及拉丁 generātiō 生出、产生借入，与 generāre 生出相连；英语名词有独立而较早的历史。',
 [['拉丁 generātiō → 法语、英语 generation','产生、后代 → 一代人、一代产品'],['generation + -s → generations','多代人、多个技术代次']],
 'three generations 三代人；future generations 后代；generations of computers 几代计算机。',
 'passed down through generations 代代相传；differences between generations 代际差异。','generation 不等于固定多少年，家族、社会划代和产品升级的标准不同。几代人也可以在同一时期共同生活。',
 ('Three generations of the family live in the same town.','这个家庭三代人住在同一个城镇。'),('The stories have been passed down through generations.','这些故事代代相传。'),sources=['https://en.wiktionary.org/wiki/generations#English','https://en.wiktionary.org/wiki/generation#English'])
W('journalists','英 /ˈdʒɜːnəlɪsts/；美 /ˈdʒɜːrnəlɪsts/','记者、新闻工作者〔复数〕',
 '把事情查清、整理成可公开报道的内容，是 journalists 的工作线索。可以采写文字，也可以做影像、声音等新闻报道。',
 'journalist + -s，/t/ 后读 /s/。journalist 接法语 journaliste，可认 journal 刊物 + -ist 从事者；journal 较早接表示日、每日的法语及拉丁词族，职业报道义很早已出现。',
 [['法语 journaliste → journalist','从事公共刊物、新闻写作编辑的人'],['journalist + -s → journalists','多位记者、新闻工作者']],
 'local journalists 当地记者；journalists covering the event 报道活动的记者；talk to journalists 与记者交谈。',
 'journalists from different newspapers 不同报纸的记者；train journalists 培训新闻工作者。','journalist 比单纯私人记日记者的范围和职业用途不同；reporter 常偏具体采访报道，journalist 可以覆盖更多新闻采编角色。',
 ('Journalists from several newspapers attended the event.','几家报纸的记者参加了活动。'),('The journalists checked the facts before publishing the story.','记者在发表报道前核对了事实。'),sources=['https://en.wiktionary.org/wiki/journalists#English','https://www.etymonline.com/word/journalist'])
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_zr',ROOTS,WORDS)
 extend_lessons()
