"""Frequent abstract nouns and people: concrete images without invented histories."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'C0769':dict(words=['moment','moments'],label='moment → moments：短时段与重要时刻',note='拉丁 momentum 已有运动、分量与短时段等义，不把英语各义硬编成单线。'),
 'C0222':dict(words=['circumstance','circumstances'],label='circumstance → circumstances：围在事情周围的条件',note='circum- 周围与站立词族组合，现代环境常由多项条件组成。'),
 'C0204':dict(words=['concern','concerns'],label='concern → concerns：涉及、在意与担忧',note='涉及义经拉丁、法语发展，英语名词由动词转用。'),
 'B2428':dict(words=['deal','deals'],label='deal → deals：分配、处理与交易',note='本族份额、分配词延续，交易义与处理往来发展相关。'),
 'B2850':dict(words=['dream','dreams'],label='dream → dreams：睡梦与梦想',note='中古英语睡梦词与北欧同族关系密切；和古英语快乐、音乐义的具体关系未定。'),
 'B2894':dict(words=['match','matches'],label='match → matches：配对、比赛；火柴另源',note='配对名词与火柴名词分开追溯，现代同形词尾发音相同。'),
 'B2480':dict(words=['war','wars'],label='war → wars：争斗与战争',note='日耳曼争斗词族经北部法语、盎格鲁诺曼语借入英语。'),
 'C0307':dict(words=['decade','decades'],label='decade → decades：十个一组与十年',note='希腊十的材料经拉丁、法语借入，常用十年义。'),
 'C1409':dict(words=['institution','institutions'],label='institution → institutions：建立与制度、机构',note='名词有独立拉丁、法语借入路线，不能只按现代英语 institute 加 ion 讲历史。'),
 'C1275':dict(words=['scene','scenes'],label='scene → scenes：舞台空间、场面与场景',note='希腊棚、帐篷词经戏剧用途发展，借入后再扩到现实场景。'),
 'B4130':dict(words=['tip','tips'],label='tip → tips：尖端、建议与小费',note='多个历史分支的关系不全确定，建议、小费义接给、递的用法，不编首字母故事。'),
 'B4137':dict(words=['partner','partners'],label='partner → partners：共同有份的人',note='中古英语形式受 part 影响定形，现代伙伴、合伙人等义按语境分。'),
 'B3799':dict(words=['victim','victims'],label='victim → victims：祭献对象与受害者',note='拉丁祭献对象词经借入后扩展为遭受伤害者，更远来源未定。'),
 'C0023':dict(words=['agent','agents'],label='agent → agents：行动、起作用的人或物',note='拉丁 agens 正在行动的分词材料形成名称，现代不同专业角色各有用途。'),
 'C0333':dict(words=['doctor','doctors'],label='doctor → doctors：教师、学者与医生',note='拉丁教导词的施事名词，经学者、专业人士义发展为医学称谓。'),
 'B2689':dict(words=['experience','experiences'],label='experience → experiences：试过、经历与经验',note='法语、拉丁经历词借入，经验总体与一次次经历的可数用法分开。'),
}
W('moments','英 /ˈməʊmənts/；美 /ˈmoʊmənts/','片刻；时刻〔moment 的复数〕',
 '把时间切成短短一小段，是 moments；回忆里特别值得记住的某一刻，也常用 moments 来数。',
 'moment + -s，/t/ 后读 /s/。moment 经法语接拉丁 mōmentum，旧词已有运动、推动力、分量和短时段等义；英语短时段义延续这条借词历史。',
 [['拉丁 mōmentum → 法语 → moment','运动、分量、短时段等旧义；英语常用片刻'],['moment + -s → moments','多个短时段、特别的时刻']],
 'a few moments 一会儿；moments later 片刻之后；special moments 特别时刻；in her quiet moments 在她安静的时候。',
 'moments before the train left；moments worth remembering。','moments 常让人感觉时间很短，但不是精确的秒数单位。important moments 还强调意义，未必只在数实际持续多久。',
 ('She returned a few moments later.','她过了一会儿就回来了。'),('The album records happy moments from their travels.','相册记录着他们旅行中的快乐时刻。'),sources=['https://en.wiktionary.org/wiki/moments#English','https://en.wiktionary.org/wiki/moment#English'])
W('circumstances','英 /ˈsɜːkəmstænsɪz/；美 /ˈsɜːrkəmstænsɪz/','情况、环境；条件；境遇〔circumstance 的复数〕',
 '一件事周围围着哪些条件：时间够不够、人手怎样、发生了什么，这一整圈背景就是 circumstances。词根的站在周围很适合记这个画面。',
 'circumstance + -s，/s/ 后增加 /ɪz/。拉丁 circum- 周围与 stāre 站形成 circumstantia，经法语借入英语；英语常用复数把多项周围条件合起来说。',
 [['拉丁 circum- + stāre → circumstantia → 法语 → circumstance','站在周围 → 周边条件、事情背景'],['circumstance + -s → circumstances','各种条件、整体情况或境遇']],
 'under the circumstances 在这种情况下；in difficult circumstances 处境困难；changing circumstances 变化中的情况。',
 'circumstances beyond our control；in similar circumstances。','under the circumstances 常是考虑眼前这些条件之后作判断；in similar circumstances 说处在相似情境。circumstances 不是单数 circumstance 随便可省的装饰性 s。',
 ('Under the circumstances, we decided to postpone the trip.','考虑到当时的情况，我们决定推迟旅行。'),('Her circumstances changed after she moved to the city.','搬到城里后，她的生活境况发生了变化。'),sources=['https://en.wiktionary.org/wiki/circumstances#English','https://en.wiktionary.org/wiki/circumstance#English'])
W('concerns','英 /kənˈsɜːnz/；美 /kənˈsɜːrnz/','担忧、关心的事〔复数〕；涉及、使担心〔第三人称单数〕',
 '某件事跟你有关，因而进入你在意的范围，是 concerns 的共同理解线索；它可以只是涉及，也可以让人担心。',
 'concern + -s，/n/ 后读 /z/。拉丁 concernere 的较早一起筛、混合义，经中古拉丁转到涉及，再经法语进入英语；英语名词由动词发展。',
 [['拉丁 concernere → 中古拉丁涉及义 → 法语 → concern','原有混合背景 → 与某事相关、涉及'],['concern + -s → concerns；英语名词用法','涉及、使担心；多项担忧或在意之事']],
 'raise concerns 提出担忧；concerns about the plan 对计划的顾虑；concerns everyone 涉及每个人。',
 'concerns about the delay；concerns the whole team。','concerns somebody 可说事情与某人有关，也可说让某人担心，靠语境区分。concerns about something 中 concerns 通常是名词，表示顾虑或担忧。',
 ('Several members raised concerns about the delay.','几位成员对延期提出了担忧。'),('This decision concerns everyone in the team.','这个决定涉及团队里的每个人。'),sources=['https://en.wiktionary.org/wiki/concerns#English','https://en.wiktionary.org/wiki/concern#English'])
W('deals','/diːlz/','交易、协议；优惠〔复数〕；处理、应对、分发〔第三人称单数〕',
 '把东西按份分出去，是 deal 的老画面；后来人与人处理往来、谈妥一笔交易，发展出 deals 的常见用法。今天不同搭配要作为整组理解。',
 'deal + -s，/l/ 后读 /z/。常用词族继承古英语 dǣl 一份与 dǣlan 分配，名动词各有旧形式；木板、松木材料的同形词另有借入背景。',
 [['古英语 dǣl、dǣlan → deal','份额、分配 → 往来、处理等发展'],['deal + -s → deals','多笔交易、优惠；单数主语处理、分发']],
 'make deals 达成交易；special deals 特别优惠；deals with problems 处理问题；deals the cards 发牌。',
 'deals offered by the shop；deals with customer questions。','deals with 可以说处理，也可说文章涉及某主题。special deals 常是优惠条件；cards 语境则回到把牌分给每个人的动作。',
 ('The shop offers special deals at the weekend.','这家店周末有特别优惠。'),('She deals with questions from new customers.','她处理新客户提出的问题。'),sources=['https://en.wiktionary.org/wiki/deals#English','https://en.wiktionary.org/wiki/deal#English'])
W('dreams','/driːmz/','梦；梦想〔复数〕；做梦、向往〔第三人称单数〕',
 '睡着时脑中出现的画面，是 dreams；清醒时想象未来希望过上的生活，也发展成梦想的用法。',
 'dream + -s，/m/ 后读 /z/。睡梦义见中古英语，与古诺尔斯语 draumr 等同族词关系密切；古英语同形 drēam 常是快乐、音乐义，两者具体关系未定。',
 [['中古英语睡梦义 dream；北欧同族联系','睡梦画面；不强定与古英语音乐义的语义过渡'],['dream + -s → dreams；想象与愿望扩展','多个梦、梦想；单数主语做梦、向往']],
 'strange dreams 怪梦；follow your dreams 追求梦想；dreams of travelling 梦想旅行。',
 'dreams remembered in the morning；dreams of opening a café。','dreams 作名词可以说睡梦，也可以说目标愿望。动词 dreams of 或 dreams about 后接名词、-ing，具体是睡梦内容还是向往之事看语境。',
 ('He remembers his dreams when he wakes up.','他醒来时还记得自己的梦。'),('She dreams of opening a small café by the sea.','她梦想在海边开一家小咖啡馆。'),sources=['https://en.wiktionary.org/wiki/dreams#English','https://www.etymonline.com/word/dream'])
W('matches','/ˈmætʃɪz/','比赛；相配的人或物；火柴〔复数，分支不同〕；匹配〔第三人称单数〕',
 '配得上的一对、实力能相对的一场比赛，是 matches 的配对分支；点火的火柴是同形的另一支，要单独记来源。',
 'match + -es，/tʃ/ 后增加 /ɪz/。配对 match 接古英语 mæcca、gemæcca 伙伴、一对中的一个；火柴 match 经古法语 meiche 灯芯等借入，更深传承有不确定处。',
 [['古英语配对词 → match；配对名词转动词','相配、对手 → 比赛、匹配'],['另一支：古法语 meiche 等 → match；各加 -es → matches','灯芯、引火物 → 火柴；现代复数或第三人称']],
 'football matches 足球比赛；a box of matches 一盒火柴；matches the description 符合描述；matches the curtains 与窗帘相配。',
 'matches played on Saturday；matches kept in a drawer。','The colour matches the curtains 中 matches 是相配动词；football matches 是比赛；a box of matches 是火柴。先用语境选分支，再接今天的意思。',
 ('Two matches will be played on Saturday.','周六将进行两场比赛。'),('She kept a box of matches beside the candles.','她在蜡烛旁放了一盒火柴。'),('The colour matches the curtains perfectly.','这个颜色与窗帘特别相配。'),sources=['https://en.wiktionary.org/wiki/matches#English','https://www.etymonline.com/word/match'])
W('wars','英 /wɔːz/；美 /wɔːrz/','战争；激烈竞争、冲突〔war 的复数〕',
 '不同群体之间持续的武装冲突，是 wars 的战争义；比喻里特别激烈的竞争，也借用交战的画面。',
 'war + -s，元音或 /r/ 后读 /z/。war 经盎格鲁诺曼、古北法语 werre、guerre 借入，较早是日耳曼语争斗、混乱词族；比喻竞争是后续用途。',
 [['日耳曼争斗词族 → 北部法语等 → war','冲突、争斗 → 战争'],['war + -s → wars；比喻扩展','多场战争；激烈竞争']],
 'civil wars 内战；world wars 世界大战；price wars 价格战；wars between kingdoms 王国间的战争。',
 'wars described in the book；price wars between shops。','price wars 在商业描述中借用双方不断竞争的画面，并非真的武装交战。world wars 的数量要随具体历史上下文判断，不凭词形猜。',
 ('The book describes several wars between neighbouring kingdoms.','这本书描写了邻近王国之间的几场战争。'),('Price wars changed the local market.','价格战改变了当地市场。'),sources=['https://en.wiktionary.org/wiki/wars#English','https://en.wiktionary.org/wiki/war#English'])
W('decades','/ˈdekeɪdz/','几十年、多个十年〔decade 的复数〕',
 '把时间十年十年地分成一组，是 decades；for decades 就是持续了几十年，通常并不精确指定有几组。',
 'decade 已有 e，复数直接加 -s，/d/ 后读 /z/。希腊 deka 十形成 dekas 十个一组，经拉丁、法语借入英语；现代常用于十年。',
 [['希腊 deka → dekas → 拉丁、法语 → decade','十 → 十个一组 → 常用十年义'],['decade + -s → decades','多个十年；泛说几十年']],
 'for decades 几十年来；over the past two decades 过去二十年间；in recent decades 近几十年来。',
 'decades of work；three decades later。','two decades 是二十年；decades 单独说常是几十年。说 a decade 可以是一段连续十年，不一定只能是日历上的某个整十年代。',
 ('She lived in the town for three decades.','她在这个镇上住了三十年。'),('The building changed little over the following decades.','此后几十年间，这座建筑变化很小。'),sources=['https://en.wiktionary.org/wiki/decades#English','https://en.wiktionary.org/wiki/decade#English'])
W('institutions','/ˌɪnstɪˈtjuːʃənz/；美式常 /ˌɪnstɪˈtuːʃənz/','机构；制度；长期确立的惯例〔institution 的复数〕',
 '人们建立起来、长期运作的组织或规则，是 institutions 的核心画面；大学、医院等是组织，某些社会规则、传统则是制度或惯例。',
 'institution + -s，/n/ 后读 /z/。拉丁 instituere 建立、安排形成 institūtiō，经古法语 institucion 等借入；现代与 institute 形成词族对应，但名词有独立借入链。',
 [['拉丁 instituere → institūtiō → 古法语 → institution','建立、安排 → 建立的制度、组织等'],['institution + -s → institutions','多个机构、制度或长期惯例']],
 'educational institutions 教育机构；public institutions 公共机构；social institutions 社会制度。',
 'institutions in the city；institutions that shape daily life。','institution 有具体组织和抽象制度两大常用方向。educational institutions 常说学校等机构；social institutions 则往往从社会运作规则来谈。',
 ('Several educational institutions share the library.','几家教育机构共用这座图书馆。'),('The course examines how social institutions change over time.','这门课探讨社会制度如何随时间变化。'),sources=['https://en.wiktionary.org/wiki/institutions#English','https://en.wiktionary.org/wiki/institution#English'])
W('scenes','/siːnz/','场面、景象；戏剧场、电影片段；现场〔scene 的复数〕',
 '眼前一整幅正在发生的画面，是 scenes；戏剧电影把故事分成一场场，也沿用 scene。追溯更早，源头与舞台后方的棚、帐篷有关。',
 'scene + -s，/n/ 后读 /z/。希腊 skēnē 棚、帐篷经戏剧用途发展，经过拉丁 scaena、法语 scène 等进入英语；现实场面等义再扩展。',
 [['希腊 skēnē → 拉丁 scaena → 法语 → scene','棚、帐篷 → 戏剧空间、场'],['scene + -s → scenes；现实画面扩展','多个场面、片段或现场']],
 'opening scenes 开场片段；street scenes 街景；behind the scenes 在幕后；scenes from daily life 日常生活场景。',
 'scenes filmed outdoors；scenes painted from memory。','behind the scenes 从舞台幕后借指看不见的工作过程。scene 中 c 不单独发 /k/；scenes 与 seen 后加 /z/ 的声音相近，但词义靠句子判断。',
 ('The opening scenes were filmed in a small village.','开场的几段戏是在一个小村庄拍的。'),('The paintings show scenes from daily life.','这些画展示了日常生活中的场景。'),sources=['https://en.wiktionary.org/wiki/scenes#English','https://en.wiktionary.org/wiki/scene#English'])
W('tips','/tɪps/','尖端；建议、窍门；小费〔复数，分支不同〕；倾倒、给小费等〔第三人称单数〕',
 'tip 最常见的几个画面分别记：细长物最前面的尖端、别人递来的一点窍门、服务后多给的一点钱。它们的远源关系并非都已确定。',
 'tip + -s，/p/ 后读 /s/。尖端 tip 通常联系低地日耳曼或北欧相关词；小费、私下信息的用法接旧动词 tip 给、递，确切远源不定；倾斜动词也有自己的旧分支。',
 [['尖端词与倾斜动词等旧支 → tip','末端、倾斜；具体来源有不确定处'],['旧 tip 给、递 → 小费及信息用法；加 -s → tips','递钱、递信息 → 小费、窍门；现代词形同形']],
 'tips of the fingers 指尖；useful tips 实用窍门；leave tips 留小费；tips the bottle 使瓶子倾斜。',
 'tips for beginners；tips left on the table。','tips for doing something 常是做事窍门。小费词不是由 To Insure Prompt Service 等首字母创造的；这种故事与实际较早记录不合。',
 ('The guide gives useful tips for travelling by train.','这本指南给出了坐火车旅行的实用窍门。'),('The waiter collected the tips from the table.','服务员收起了桌上的小费。'),('She touched the fabric with the tips of her fingers.','她用指尖摸了摸那块布。'),sources=['https://en.wiktionary.org/wiki/tips#English','https://www.etymonline.com/word/tip'])
W('partners','英 /ˈpɑːtnəz/；美 /ˈpɑːrtnərz/','伙伴、合伙人、搭档；伴侣〔复数〕；与……搭档〔第三人称单数〕',
 '一起参与、共同有份的人，是 partners；工作、比赛、舞蹈、生活里都能有这种共同参与的关系。',
 'partner + -s，词尾 /ə/ 或 /ər/ 后读 /z/。partner 接古法语共同有份的人相关词，经中古英语 parcener 等形式，受 part 的拼写、意义影响形成 partner；现代不拆成独立后缀 ner。',
 [['古法语共同有份者词 → 中古英语 parcener 等 → partner','共同参与、共有一份的人；受 part 影响定形'],['partner + -s → partners；名词转动词','多个伙伴；单数主语与人合作']],
 'business partners 商业伙伴、合伙人；dance partners 舞伴；project partners 项目合作方。',
 'partners in the project；partners with a local school。','partners 不必是亲密朋友，也可只是共同完成某件事的搭档。生活关系中可指伴侣；具体亲密程度、法律身份不由这个词单独决定。',
 ('The students worked with different partners each week.','学生们每周和不同的搭档合作。'),('The two companies became partners in the project.','这两家公司成为该项目的合作伙伴。'),sources=['https://en.wiktionary.org/wiki/partners#English','https://en.wiktionary.org/wiki/partner#English'])
W('victims','/ˈvɪktɪmz/','受害者；遭受不利影响的人或物〔victim 的复数〕',
 '因为事故、灾难、欺骗等遭受伤害的一方，是 victims。今天的受害者义已经从较早祭献对象的名称扩大出来。',
 'victim + -s，/m/ 后读 /z/。victim 接拉丁 victima 祭献对象，经法语等借入英语；后来扩成被伤害、被利用者，更远来源不定。',
 [['拉丁 victima → 法语等 → victim','祭献对象 → 遭受伤害或被利用的一方'],['victim + -s → victims','多个受害者或受不利影响者']],
 'flood victims 洪灾受害者；victims of fraud 欺诈受害者；help the victims 帮助受害者。',
 'victims of the accident；victims waiting for assistance。','victim 常用 of 引出造成损害的事件、行为。拼写中的 vict- 不能直接按 victory 胜利拆成相反的故事，较远词源并未这样确定。',
 ('Volunteers brought blankets to the flood victims.','志愿者把毯子送给洪灾受害者。'),('The report includes interviews with victims of fraud.','报告包含对欺诈受害者的访谈。'),sources=['https://en.wiktionary.org/wiki/victims#English','https://en.wiktionary.org/wiki/victim#English'])
W('agents','/ˈeɪdʒənts/','代理人、经纪人；行动人员；起作用的物质等〔agent 的复数〕',
 '代表别人办事、实际去行动的人，是 agents；能让某种变化发生的物质，也可以叫 agents。底层画面是行动、发挥作用。',
 'agent + -s，/t/ 后读 /s/。拉丁 agere 做、行动的现在分词 agēns，词干 agent-，经法语、拉丁借入英语，形成行动者、代理者等用法。',
 [['拉丁 agere → agēns、agent- → agent','行动 → 行动或发挥作用的人、物'],['agent + -s → agents','多个代理人、行动者或作用物']],
 'travel agents 旅行代理商；estate agents 房地产经纪人；cleaning agents 清洁剂；literary agents 文学经纪人。',
 'agents representing the writer；agents used for cleaning。','agents 不自动等于间谍；旅行、房产、出版都有代理角色。cleaning agents 说起清洁作用的物质，仍接发挥作用这条线索。',
 ('Several agents offered to represent the writer.','几位经纪人提出愿意代理这位作家。'),('Different cleaning agents were stored on separate shelves.','不同清洁剂放在不同架子上。'),sources=['https://en.wiktionary.org/wiki/agents#English','https://en.wiktionary.org/wiki/agent#English'])
W('doctors','英 /ˈdɒktəz/；美 /ˈdɑːktərz/','医生；博士〔复数〕；篡改等〔第三人称单数〕',
 '日常医院里的 doctors 常是医生；大学学位语境也可以说博士。老词本来是教导者、学者，医学称谓后来沿专业人士的方向发展。',
 'doctor + -s，词尾 /ə/ 或 /ər/ 后读 /z/。拉丁 docēre 教导形成 doctor 教师，经法语、拉丁借入；学术、医学等称谓逐渐分化，英语另形成处理、篡改等动词义。',
 [['拉丁 docēre → doctor → 英语 doctor','教导 → 教师、学者；专业和医学称谓'],['doctor + -s → doctors；现代词性扩展','多位医生或博士；单数主语篡改等']],
 'hospital doctors 医院医生；doctors of philosophy 哲学博士学位获得者；doctors the figures 篡改数字。',
 'doctors at the hospital；doctors in different subjects。','Doctor 的博士称谓不只指医学。PhD 是学位名称，doctors of philosophy 的研究领域也不必是哲学这一个学科；医院语境则通常是医生。',
 ('The hospital invited doctors from several departments.','医院邀请了几个科室的医生。'),('The ceremony honoured new doctors from several fields.','典礼表彰了几个领域新获得博士学位的人。'),sources=['https://en.wiktionary.org/wiki/doctors#English','https://en.wiktionary.org/wiki/doctor#English'])
W('experiences','英 /ɪkˈspɪəriənsɪz/；美 /ɪkˈspɪriənsɪz/','经历、体验〔复数〕；经历、体验到〔第三人称单数〕',
 '亲自遇过、走过的一次次事情，是 experiences；把这些事情积累成能力时，英语常用不可数的 experience 说经验。',
 'experience + -s，/s/ 后增加 /ɪz/。名词经古法语接拉丁 experientia，与 experīrī 尝试、经历相连；英语动词又形成经历、感受到的用法。',
 [['拉丁 experīrī、experientia → 古法语 → experience','试过、经历 → 经验、经历'],['experience + -s → experiences','多次经历；单数主语经历、感受']],
 'childhood experiences 童年经历；share experiences 分享经历；experiences difficulties 遇到困难。',
 'experiences described in the book；experiences something for the first time。','much experience 说经验丰富；many experiences 说经历过许多事情。The system experiences delays 的 experiences 是动词，说明系统遇到延迟。',
 ('They shared their experiences of living abroad.','他们分享了在国外生活的经历。'),('The system experiences delays during busy periods.','系统在繁忙时段会出现延迟。'),sources=['https://en.wiktionary.org/wiki/experiences#English','https://en.wiktionary.org/wiki/experience#English'])
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_ym',ROOTS,WORDS)
 extend_lessons()
