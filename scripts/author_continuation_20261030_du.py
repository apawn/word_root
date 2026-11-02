"""Environment advocates, crowd participation, discovery and distant presence."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
E=[['法语 environ、environner 等 → environ → environment','周围、围绕 → 所处环境'],['environment + -al → environmental','与环境有关的']]
W('environmentally','/ɪnˌvaɪrənˈmentəli/','从环境角度、在环境方面；对环境地〔与形容词连用〕',
 '把评判的镜头放到环境影响上：environmentally friendly 说对环境较友好，不是这个产品对人态度热情。',
 'environmental + -ly，副词修饰友好、可持续、有害等性质，说明从环境影响方面看。',E+[['environmental + -ly → environmentally','在环境方面、从环境影响看']],
 'environmentally friendly 对环境友好的，environmentally damaging 损害环境的，environmentally sustainable 环境上可持续的。',
 'environmentally friendly；environmentally damaging；environmentally sustainable。',
 'environmentally 限定环境维度，不自动保证所有方面都更好；friendly 的这种搭配是兼容、影响较小的引申，不是物品有情绪。',
 ('The team looked for more environmentally friendly packaging.','团队寻找对环境更友好的包装。'),('The report called the project environmentally damaging.','报告认为项目会损害环境。'))
W('environmentalist','/ɪnˌvaɪrənˈmentəlɪst/','环保人士、环境保护主义者；相关的',
 '把保护环境当作关心、倡导的目标的人。可以从事不同职业，不必都在实验室研究环境。',
 'environmental + -ist，人物后缀命名关心、倡导环境保护的人；也可作修饰立场的词。',E+[['environmental + -ist → environmentalist','倡导环境保护的人或相关立场']],
 'an environmentalist 环保人士，local environmentalists 当地环保人士，an environmentalist group 环保团体。',
 'an environmentalist；local environmentalists；an environmentalist group。',
 'environmentalist 侧重倡导、关心环境，environmental scientist 环境科学家是研究职业；一个人可兼任，但不能自动互换。',
 ('Local environmentalists opposed the plan.','当地环保人士反对该计划。'),('The documentary interviews several environmentalists.','纪录片采访了几位环保人士。'))
W('environmentalism','/ɪnˌvaɪrənˈmentəlɪzəm/','环保理念、环境保护主义及其运动',
 '不再指某一个人，而是保护环境这一套关心、主张和推动社会行动的观念。',
 'environmental + -ism，-ism 命名理念、取向或运动。不是环境本身的另一个长名字。',E+[['environmental + -ism → environmentalism','保护环境的理念、主张或运动']],
 'the history of environmentalism 环保运动史，modern environmentalism 现代环保理念，debates about environmentalism 关于环保主义的讨论。',
 'the history of environmentalism；modern environmentalism；debates about environmentalism。',
 'environment 环境，environmentalism 保护环境的理念；environmentalist 人物，不是把 -ism 和 -ist 都译成同一种环境。',
 ('The course traces the history of environmentalism.','课程追溯环保运动的历史。'),('The essay compares different forms of environmentalism.','文章比较了不同形式的环保理念。'))
R('B4437','环境维度与保护环境的人、理念','ENVIRONMENTAL：与周围环境有关，再分评价角度和倡导立场','environmental → environmentally；environmentalist、environmentalism 放在一起分人物与理念。',
 'environmentally friendly 评环境影响，environmentalist 侧重倡导；不与环境科学家或环境本身简单互换。',
 'environment + -al；environmental + -ly/-ist/-ism。',
 [['环境性质与评价角度','environmental · environmentally'],['人物与理念','environmentalist · environmentalism']],
 'environmentalist/environmental scientist 倡导角色与研究职业；-ist 人、-ism 理念；friendly 非物品性格。',
 'The environmentalist explained why the packaging was environmentally harmful.\n\n环保人士解释了包装为什么对环境有害。','environmental environmentally environmentalist environmentalism')
C=[['古英语 crūdan → 中古英语 crouden → crowd〔动词〕','推挤、挤压'],['英语 crowd〔名词〕及后来的参与比喻','挤在一起的人 → 人群；也可说共同参与的大众']]
def CH(f,m):return C[:1]+[[f,m]]
W('crowd','/kraʊd/','人群、一群人；挤满、挤入；围拢',
 '许多人挤在一处，是 a crowd；动词说人或东西把空间塞紧。网络复合词里的 crowd 则能是分散各地、一起参与的大众。',
 '动词继承古英语 crūdan 推、挤，经中古英语到现代；名词人群由聚挤动作发展。不能只靠拼写把 crow 乌鸦和某个 d 后缀合起来。',C,
 'a crowd of people 一群人，crowd into a room 挤进房间，crowd around 围拢，crowd out 挤走、排挤，stand out from the crowd 脱颖而出。',
 'a crowd of；crowd into；crowd around；crowd out；stand out from the crowd。',
 'crowd 不保证愤怒、暴力，mob 常更带失控、威胁色彩；crowdfunding 的人不一定身体站在同一屋里。',
 ('A crowd gathered outside the theatre.','剧院外聚起一群人。'),('People crowded around the tiny stage.','人们围拢在小舞台周围。'),
 sources=['https://en.wiktionary.org/wiki/crowd#English','https://www.etymonline.com/word/crowd'])
W('crowded','/ˈkraʊdɪd/','拥挤的、挤满的',
 '人或物很多，空间显得不够，想转身、放东西都有点难；不是只说现场有人。',
 'crowd + -ed，过去分词发展为形容词。d 后的 -ed 读 /ɪd/，把两节读清楚。',CH('crowd + -ed → crowded','被挤满、空间紧张的'),
 'a crowded bus 拥挤公交车，crowded streets 拥挤街道，crowded with people 挤满人，a crowded schedule 排得很满的日程。',
 'a crowded bus；crowded streets；crowded with；a crowded schedule。',
 'crowded 人或事塞得多，popular 受欢迎可能导致拥挤，却不保证时刻都挤；empty 与 crowded 对看空间占用。',
 ('The bus was too crowded to sit down.','公交车太挤，没地方坐。'),('She has a crowded schedule this week.','她本周日程排得很满。'))
W('crowdfunding','/ˈkraʊdfʌndɪŋ/','众筹、大众筹资',
 '钱不是只向一个大出资人要，而是让很多参与者各出一点，共同凑起一个项目的资金。',
 'crowd 大众 + funding 筹资，现代复合词，也与动词 crowdfund 的 -ing 形式对应；构词材料并列，不画成人群先演变成基金。',CH('crowd + funding → crowdfunding','由大众共同提供资金的筹资方式'),
 'a crowdfunding campaign 众筹活动，a crowdfunding platform 众筹平台，raise money through crowdfunding 通过众筹筹钱。',
 'a crowdfunding campaign；a crowdfunding platform；through crowdfunding。',
 'crowdfunding 重点钱，crowdsourcing 重点让大众提供点子、数据、工作等；不同众筹可涉及捐赠、回报等方式，不只一种投资机制。',
 ('The film raised money through crowdfunding.','电影通过众筹筹集了资金。'),('They launched a crowdfunding campaign to restore the hall.','他们发起众筹，想修复那座大厅。'))
R('B3133','挤在一起的人与分散参与的大众','CROWD：从空间里的推挤，到许多人共同参与','crowd → crowded；crowdfund、crowdfunding 一组；crowdsource、crowdsourcing 一组，分钱与贡献内容、工作。',
 'crowd 不自带暴力，crowded 说空间或日程被填满；大众参与的网络词可以人人相隔很远。',
 'crūdan → crowd；crowd + -ed；crowd + fund/funding；crowd + source、sourcing 等现代组合。',
 [['人群、动作与拥挤','crowd · crowded'],['大众出资','crowdfund · crowdfunding'],['大众提供内容、工作','crowdsource · crowdsourcing']],
 'crowd/mob 聚集与可能失控色彩；crowdfunding 钱，crowdsourcing 范围更广；crowded 不等于单纯 popular。',
 'Crowdfunding let a widely scattered crowd support the project.\n\n众筹让分散各地的大众共同支持了项目。','crowd crowded crowdfund crowdfunding crowdsource crowdsourcing')
ROOTS[-1]['exclude']['crowdsourced']='crowdsource 的规则过去分词，可说通过众包取得；与 crowdsource 同条理解，不另立重复词头。'
D=[['法语 descovrir、相关旧形式 → discover','揭去覆盖、显露 → 发现'],['现代发现词族','再次发现、发现者、能够被找到的性质']]
W('rediscover','英 /ˌriːdɪˈskʌvə/；美 /ˌriːdɪˈskʌvər/','重新发现、重新认识到价值',
 '曾经知道、后来忘了或忽略的东西，重新进入眼前；重听一首旧歌、找回兴趣，也可叫 rediscover。',
 're- 再 + discover。discover 的揭开、发现是已有整体，前缀接在整体前，不把 re- 当其中某个远古字母变化。',D[:1]+[['re- + discover → rediscover','再次发现；找回原先忽略的价值']],
 'rediscover an old book 重新发现一本旧书，rediscover a love of painting 找回对绘画的热爱，rediscover the city 重新认识城市。',
 'rediscover an old book；rediscover a love of；rediscover the city。',
 'rediscover 不保证此前全人类都不知道，也不等于从零 invent 发明；个人重新欣赏旧物也很自然。',
 ('I rediscovered an old favourite while sorting my books.','整理书时，我重新翻到一本从前很喜欢的书。'),('The trip helped her rediscover her love of nature.','旅行让她重新找回了对自然的热爱。'))
W('discoverer','英 /dɪˈskʌvərə/；美 /dɪˈskʌvərər/','发现者',
 '把原来未被相关人群知道、确认的东西找出来的人；某地的发现者这个称呼还要留意是谁的叙述视角。',
 '现代对应 discover + -er；中古英语 discoverour 等既有法语 descouvreur 的借入，也有英语派生因素，不能只画成现代新加一个后缀。',D[:1]+[['法语 descouvreur、英语 discover + -er 等 → discoverer','揭示、发现某物的人']],
 'the discoverer of a comet 彗星发现者，one of the discoverers 发现者之一，credit the discoverer 给发现者应有认可。',
 'the discoverer of；one of the discoverers；credit the discoverer。',
 'discoverer 发现已有事物，inventor 发明新装置、方法等；谁算最早发现者需要证据，不能由词形证明。',
 ('The museum honours the discoverer of the comet.','博物馆纪念那颗彗星的发现者。'),('The article names several independent discoverers.','文章列出了几位各自独立作出发现的人。'))
W('discoverable','英 /dɪˈskʌvərəbəl/；美 /dɪˈskʌvərəbəl/','可发现的、能被找到的',
 '东西在那里，别人有办法搜到、察觉到它；不是它一定会主动出现，而是能被发现。',
 'discover + -able，形成可被发现的形容词。词基结尾 r 直接接后缀，不需要删一个并不存在的 e。',D[:1]+[['discover + -able → discoverable','能够被发现、找到的']],
 'easily discoverable 容易找到的，make content discoverable 让内容可被检索发现，a discoverable device 可被发现的设备。',
 'easily discoverable；make discoverable；a discoverable device。',
 'discoverable 能找到，discovered 已找到；可被发现的设备也可能尚未被任何人连接。',
 ('The new index makes the articles more discoverable.','新索引让这些文章更容易找到。'),('The device remained discoverable during the test.','测试期间，这个设备一直能被发现。'))
R('B3565','揭开、发现与再次找到、能够找到','DISCOVER：原来遮着、没察觉，后来进入认识范围','discover → discovery、discoverer、discoverable；rediscover 重新进入视野、找回价值。',
 '发现与发明不同；重新发现可以是个人重拾爱好，不必整个人类再来一次首次科学发现。discoverer 的法语人物名路径保留。',
 '法语 descovrir 等 → discover；discovery 有名词历史；discoverer 借入与派生；discover + -able；re- + discover。',
 [['发现与结果、人物、可能性','discover · discovery · discoverer · discoverable'],['重新认识','rediscover']],
 'discover/invent 发现与发明；discoverable/discovered 能找到与已找到；rediscover 不必须全球未知。',
 'The new catalogue helped readers rediscover forgotten books.\n\n新目录帮助读者重新发现被遗忘的书。','discover discovery discoverer discoverable rediscover')
W('telepresence','/ˌteləˈprezəns/','远程临场、遥在；远程在场技术及体验',
 '人还在这边，却能通过画面、声音、机器人等在远处观察、交流、行动，获得仿佛在那里的一种在场感。',
 'tele- 远距离 + presence 在场，现代技术复合词。presence 接法语 présence、拉丁 praesentia 的在场词族；不是把身体真的瞬间传送过去。',
 [['presence〔在场〕+ tele-〔远〕→ telepresence','远距离而有在场感'],['现代 telepresence','实现远程行动、交流的技术及体验']],
 'a telepresence robot 远程临场机器人，telepresence technology 远程在场技术，a sense of telepresence 远程临场感。',
 'a telepresence robot；telepresence technology；a sense of telepresence。',
 'telepresence 强调远程在场、行动或体验，teleportation 瞬间传送是另一概念；不必所有方案都戴 VR 头显。',
 ('A telepresence robot allowed the student to join the class remotely.','远程临场机器人让学生得以远程参与课堂。'),('The exhibition explored the experience of telepresence.','展览探讨了远程在场的体验。'),
 sources=['https://en.wiktionary.org/wiki/telepresence#English','https://www.merriam-webster.com/dictionary/telepresence'])
R('B4468','在场、无处不在与远程在场','PRESENCE：虽不只是身体站在那里，也强调让人感到你在','presence → omnipresence、telepresence，分处处在场与远程在场。',
 'remote 不等于不存在。telepresence 借技术让远处的行动、交流有临场感，不是把人真的搬到另一个坐标。',
 '法语 présence、拉丁 praesentia → presence；omni- + presence；tele- + presence。',
 [['在场与范围扩展','presence · omnipresence · telepresence']],
 'presence 在场，telepresence 远程临场；teleportation 瞬移是另一个概念；omnipresence 处处在场非只开一次远程会议。',
 'Telepresence helped him maintain a presence in the classroom.\n\n远程临场技术让他能继续参与课堂、保持在场感。','presence omnipresence telepresence')
if __name__=='__main__':save('continuation_20261030_du',ROOTS,WORDS)
