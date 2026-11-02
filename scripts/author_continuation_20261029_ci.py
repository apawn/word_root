"""Development, personal and month: useful everyday extensions."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
D=[['古法语 desveloper → 法语 développer','解开包裹、展开'],['英语 develop；对应名词 development','逐渐形成、发展；发展的过程和结果']]
W('development','/dɪˈveləpmənt/','发展；开发；成长；新进展',
 '一件事原来还没成形，后来一步步展开、变得完整；也可以指局面里新冒出的变化。',
 '现代可认作 develop + -ment，-ment 形成过程或结果名词；历史与法语 développement 对应。develop 接法语展开、解开包裹的词，包裹部分更远来源不确定，不硬拆成拉丁语的帆或面纱。',D,
 'child development 儿童发展，software development 软件开发；a new development 新情况，不一定是好消息；a housing development 也可指一片开发建成的住宅区。',
 'economic development；software development；a recent development；in development。',
 'development 是发展、变化或开发，improvement 明说改善。a worrying development 恰恰是令人担忧的新变化。',
 ('The team is working on the development of a new app.','团队正在开发一款新应用。'),('There has been an unexpected development in the story.','事情出现了一个意料之外的新变化。'),sources=['https://en.wiktionary.org/wiki/development#English','https://www.etymonline.com/word/develop'])
W('developmental','/dɪˌveləpˈmentəl/','与发展、发育过程有关的',
 '看一个人或事物怎样经过不同阶段长起来、形成起来，重点在变化的过程。',
 'development + -al，-al 表与……有关，重音落在 -mental 中的 men。不是单独把 mental 心理的加到 develop 后面。',D+[['development + -al → developmental','发展过程 → 与发展阶段有关的']],
 'developmental stages 发展阶段，developmental psychology 发展心理学；developmental work 也可说产品等处于探索、形成过程的工作。',
 'developmental stages；developmental psychology；developmental changes。',
 'developmental 不等于 developed 已发展成熟的，也不自动表示生病；它首先说明与成长、形成过程有关。',
 ('The book explains several developmental stages in early childhood.','这本书解释了幼儿时期的几个发展阶段。'),('The project is still in a developmental phase.','项目仍处于探索成形的阶段。'))
W('redevelopment','/ˌriːdɪˈveləpmənt/','重新开发；改建',
 '原来的地方已经用过，现在重新规划、改造，让它换一种用法或面貌。',
 're- 再、重新 + development 开发；对应动词 redevelop。前缀说明重复或重新处理，不保证恢复成原样。',D+[['re- + development → redevelopment','开发 → 对已有地区、设施重新开发']],
 'the redevelopment of a station 车站改建，an urban redevelopment project 城市片区改造项目；可能保留旧建筑，也可能改变布局，具体看方案。',
 'urban redevelopment；a redevelopment plan；redevelopment of the site。',
 'development 可以首次开发，redevelopment 特别强调已有基础上的重新开发；renovation 更常聚焦建筑整修。',
 ('The old factory is scheduled for redevelopment.','旧工厂已列入重新开发计划。'),('Residents asked to see the station redevelopment plans.','居民要求查看车站改建方案。'))
W('underdevelopment','英 /ˌʌndədɪˈveləpmənt/；美 /ˌʌndərdɪˈveləpmənt/','发展不足；欠发达状态',
 '本该形成的能力、设施或服务还没有充分发展出来。',
 'under- 不足、未达到充分程度 + development；这里 under- 不是空间上的在下面。',D+[['under- + development → underdevelopment','发展 → 发展程度不足']],
 'the underdevelopment of transport infrastructure 交通基础设施发展不足；可用于地区经济、服务或某方面能力，具体说明哪方面不足更清楚。',
 'economic underdevelopment；regional underdevelopment；the underdevelopment of infrastructure。',
 'underdevelopment 一个词说发展不足；under development 两个词说正在开发。The app is under development 不是这款应用处于欠发达状态。',
 ('The report examines the underdevelopment of rural transport networks.','报告考察了农村交通网络发展不足的问题。'),('The app is under development; the report is about regional underdevelopment.','应用正在开发中；报告讲的是区域发展不足。'))
R('B3553','发展、成长、开发与进展','DEVELOPMENT：从没展开到逐步成形','想象折着的东西慢慢展开；发展既可能是成长，也可能是局面冒出新变化。',
 'develop 经法语保留展开的历史画面，development 是相应过程、结果名词。现代很多用法已固定，不要把每一次发展都解释成进步。',
 'development → developmental；re- 重新开发 → redevelopment；under- 发展不足 → underdevelopment。',
 [['发展及阶段','development · developmental'],['重新开发与发展不足','redevelopment · underdevelopment']],
 'development 不总是 improvement；underdevelopment 与 under development 要分开认。',
 'The redevelopment plan is still under development.\n\n这份重新开发方案仍在制定中。',
 'development developmental redevelopment underdevelopment')
P=[['拉丁语 persōna → persōnālis → 法语 personal','人、角色 → 与个人有关的'],['中古英语 personal → 现代英语 personal','个人的、私人的；针对个人的']]
W('personally','英 /ˈpɜːsənəli/；美 /ˈpɜːrsənəli/','亲自；就我个人而言；针对个人地',
 '把范围落到某个具体的人：我自己去做、我自己的看法，或者觉得别人是在冲我来。',
 'personal + -ly 成副词；中古英语已有对应形式。personal 经法语接拉丁语 persōnālis 与个人有关的。',P+[['personal + -ly → personally','个人的 → 亲自、就个人而言']],
 'Personally, I disagree 是就我个人而言不同意；thank someone personally 亲自道谢；take criticism personally 把批评当成针对自己这个人。',
 'personally speaking；know someone personally；take it personally；personally responsible。',
 'personally 亲自或就个人而言；in person 强调本人到场。I personally checked it 不保证是在现场而非远程核查。',
 ('I will personally check every address.','我会亲自核对每个地址。'),('Please don’t take the comment personally.','请别把这句话当成针对你个人。'))
W('impersonal','英 /ɪmˈpɜːsənəl/；美 /ɪmˈpɜːrsənəl/','不针对个人的；缺乏人情味的',
 '看不到具体这个人的个性、关系或感受，像统一流程在处理每个人。',
 '现代可认作 im- 不 + personal；历史接法语 impersonnel、拉丁语 impersōnālis。im- 是否定 in- 在 p 前的形式，不是表示进入的 in-。',P[:1]+[['拉丁语 impersōnālis → 法语 impersonnel → impersonal','非个人的；现代也指缺乏个人温度']],
 'an impersonal email 像群发模板的邮件，an impersonal tone 不带私人感情的语气；写说明书时客观中性可能合适，服务场景里又可能显得冷。',
 'an impersonal service；an impersonal tone；impersonal language。',
 'impersonal 不针对具体的人，interpersonal 人与人之间的；impersonal 也不必然等于 rude 粗鲁。',
 ('The automatic reply felt cold and impersonal.','自动回复显得冷冰冰，毫无人情味。'),('The instructions use clear, impersonal language.','说明使用清晰、不带个人感情色彩的语言。'))
W('personality','英 /ˌpɜːsəˈnæləti/；美 /ˌpɜːrsəˈnæləti/','性格；个性；知名人物',
 '同一件事，有人热情外向，有人安静谨慎；一个人稳定而有辨识度的样子，就是他的 personality。',
 '认形可用 personal + -ity；历史由法语、中世纪拉丁语相应名词进入英语，较早说作为人的性质，后来发展为独特性格，再可指有名、有鲜明形象的人。',P[:1]+[['法语 personalité、拉丁语 persōnālitās → 英语 personality','作为人的性质 → 个性、性格；知名人物']],
 'a warm personality 热情的性格，a clash of personalities 性格不合；a television personality 电视界知名人物，不能直译成电视性格。',
 'a strong personality；personality traits；a clash of personalities；a TV personality。',
 'person 人，personal 个人的，personality 性格或知名人物。personality 不等于 character 的所有意思，小说中的一个人物一般是 a character。',
 ('She has a warm and outgoing personality.','她性格热情外向。'),('The show was hosted by a popular television personality.','节目由一位很受欢迎的电视界名人主持。'),sources=['https://en.wiktionary.org/wiki/personality#English','https://www.etymonline.com/word/personality'])
W('personalize','英 /ˈpɜːsənəlaɪz/；美 /ˈpɜːrsənəlaɪz/','按个人定制；使针对个人',
 '原来人人拿到一样的，现在加上你的名字、喜好或需要，变成适合你的那一份。',
 'personal + -ize 使成为，形成动词；英式也常写 personalise。它也可把一般问题变成针对个人的事情。',P+[['personal + -ize → personalize','个人的 → 使具有个人特点、适合个人']],
 'personalize a gift 在礼物上加名字等个性内容，personalize the settings 按自己需要调整设置；personalize a dispute 则是把争论变成针对个人。',
 'personalize a gift；personalize a message；personalize your settings。',
 'personalize 常强调面向具体个人，customize 可按个人或组织要求改动；两者实际范围有交叠。',
 ('You can personalize the notebook with a name on the cover.','你可以在封面加名字，把笔记本做成个人专属款。'),('Please discuss the decision without personalizing the disagreement.','请就决定本身讨论，别把分歧变成针对个人。'))
W('personalization','英 /ˌpɜːsənəlaɪˈzeɪʃən/；美 /ˌpɜːrsənəlaɪˈzeɪʃən/','个性化；面向个人的定制',
 '把给大家的一套内容，调整成更贴合某个人的一套；这是定制的过程或效果。',
 'personalize 去末尾 e + -ation 成名词；也可看 personal + -ization 的词族对应。重音移到 -zation 的 za。',P+[['personalize + -ation → personalization','按个人定制 → 个性化过程、结果']],
 'message personalization 信息个性化，product personalization 产品定制；可以是人工加名字，也可以根据偏好调整内容，不是只有算法推荐才叫这个词。',
 'content personalization；product personalization；personalization options。',
 'personalization 定制过程，personality 个性、性格。礼物加了名字是 personalization，不是礼物长出了人的 personality。',
 ('The website offers several personalization options.','网站提供多种个性化设置。'),('Simple personalization made each invitation feel more thoughtful.','简单的个人化处理，让每张请柬都显得更用心。'))
R('B3783','个人的、私人的；个性与定制','PERSONAL：落到具体这个人身上','从人人一样的一套，切换到这个人的意见、性格、需要与私人范围。',
 'personal 经法语接拉丁语 persōnālis，与 person 属同族。先分清个人的、性格、按个人定制，再看人与人之间的 interpersonal。不把 persona 更远来源的争议编成确定故事。',
 'personal → personally、impersonal、personality；personal → personalize → personalization；interpersonal 看人与人之间。',
 [['个人与非个人','personal · personally · impersonal'],['性格','personality'],['个性化定制','personalize · personalization'],['人与人之间','interpersonal · transpersonal']],
 'personal 不是 personnel 员工；personality 不是 personalization；impersonal 也不是 interpersonal。',
 'Personally, I prefer a personal message to an impersonal reply.\n\n就我个人而言，我更喜欢专门写给我的信息，而非没有人情味的回复。',
 'personal personally impersonal personality personalize personalization interpersonal transpersonal')
M=[['古英语 mōnaþ → 中古英语 moneth','月，与 moon 月亮属历史相关词族'],['英语 month','日历上的一个月；一段按月计算的时间']]
W('month','/mʌnθ/','月；一个月的时间',
 '把一年按月份切成一段段，January、February 各是一段；也可以从某一天起算一个月。',
 '接古英语 mōnaþ，经中古英语延续，与 moon 月亮历史同族，背景是用月亮周期计时。现代 month 不是把 moon 删掉一个 o 再加 th 的即时拼词规则。',M,
 'next month 下个月，a month later 一个月后；日历月份的天数不完全相同，现代日历里的月也不必与一次完整月相周期严格重合。',
 'this month；once a month；a month later；month after month。',
 'last month 上个月通常不加 in；in May 在五月。a month 可以是一段时间，不只指从每月一号开始的月份。',
 ('We moved here last month.','我们上个月搬到了这里。'),('The club meets once a month.','俱乐部每月聚会一次。'))
W('monthly','/ˈmʌnθli/','每月的；按月；月刊',
 '每跨过一个月就来一回，或者把费用、收入等按一个月来算。',
 'month + -ly；形容词、相应副词有中古英语乃至更早的对应形式。这里 -ly 不只构成副词，也能形容每月发生的事。',M+[['month + -ly → monthly','月 → 每月的、按月；月刊']],
 'a monthly payment 每月付款额，meet monthly 每月见面；a monthly 是月刊。twice monthly 一个月两次，every two months 两个月一次，说清楚比含糊缩写好。',
 'a monthly meeting；monthly rent；pay monthly；a literary monthly。',
 'a monthly report 通常是按月出的报告，a month’s work 是一个月的工作；monthly 本身不限定在每月哪一天。',
 ('We hold a monthly meeting to review progress.','我们每月开一次会，回顾进展。'),('The fee can be paid monthly.','费用可以按月支付。'))
R('B2421','月；每月的、按月','MONTH：用月划分时间','从月亮周期的古老计时背景，走到今天日历上一格格的月份。',
 'month 与 moon 历史相关，但现代日历月份不必严格等于月相周期。monthly 就把 month 变成每月发生、按月计算的表达。',
 'month → monthly；-ly 在这里可成形容词，也可成副词，monthly 还可作月刊名词。',
 [['月份与按月','month · monthly']],
 'monthly 每月；twice monthly 每月两次；every two months 每两个月一次。',
 'We pay monthly, on the first day of each month.\n\n我们按月付款，在每月第一天支付。',
 'month monthly')
if __name__=='__main__':save('continuation_20261029_ci',ROOTS,WORDS)
