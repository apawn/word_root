"""Common -ation nouns with bases; spelling variants and senses stay together."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
Cp=[['拉丁 compilare 搜掠、汇集 → 法语 compiler','把来自各处的材料聚拢'],['英语 compile → compilation','汇编、编译；汇集过程与汇编作品']]
W('compile','/kəmˈpaɪl/','汇编、编制；编译〔程序〕',
 '散落的资料先收起来，再按目的排成一份清单、书籍，是 compile。编程里则把源代码按语言规则翻译成另一种代码、中间形式。',
 '经法语 compiler 接拉丁 compilare，早有搜掠、汇集材料的意思。现代汇编通常是中性整理；计算机编译是后来的技术用法。',Cp,
 'compile a list 编制清单；compile a report 汇编报告；compile code 编译代码。',
 'compile a list；compile code。',
 'compile 比单纯 collect 收集常多整理成品的步骤；程序 compile 则按特定语言、工具规则转换，不只是把文本拼在一起。',
 ('She compiled a list of useful references.','她编了一份有用的参考资料清单。'),('The tool compiles the code into a different format.','工具把代码编译成另一种格式。'))
W('compilation','英 /ˌkɒmpɪˈleɪʃən/；美 /ˌkɑːmpɪˈleɪʃən/','汇编、编纂；汇编作品、精选集；编译',
 'compile 是把材料整理成一份，compilation 既能说这个过程，也能说最终那本合集、那张精选唱片。编程中则是编译过程。',
 '经法语接拉丁 compilatio；现代对应 compile 去 e 加 -ation，保留材料聚拢的词族关系。',Cp+[['compilatio → compilation','汇集过程；汇集成的作品；后有编译用法']],
 'a compilation of essays 文章合集；a compilation album 精选专辑；compilation errors 编译错误。',
 'a compilation of；compilation errors。',
 'compilation 可以是许多来源作品的集合，composition 常是创作、组成；汇编与原创写作的角度不同。',
 ('The book is a compilation of travel essays.','这本书是旅行随笔合集。'),('Compilation failed because of a syntax error.','由于语法错误，编译失败了。'))
If=[['拉丁 in- 进入 + flamma 火焰 → inflammare','点燃；引申为激起强烈反应'],['法语、英语 inflame；拉丁 inflammatio → inflammation','使激化、使发炎；炎症']]
W('inflame','/ɪnˈfleɪm/','激化、激起；使发炎',
 '原本已有火星，又给它添了火，情绪、冲突更强了，是 inflame 的比喻。身体组织发炎的红热感也保留了火的旧画面。',
 '经法语接拉丁 inflammare，in- 进入与 flamma 火焰的材料；点燃义走向激起情绪、使发炎等用法。',If,
 'inflame tensions 加剧紧张；inflame public opinion 激起舆情；inflamed skin 发炎的皮肤。',
 'inflame tensions；inflamed skin。',
 'inflame 常使反应更强，soothe 是缓和、安抚；这两个词可沿加火与降温的画面对照。',
 ('The remarks inflamed tensions between the groups.','这些话加剧了群体间的紧张。'),('The skin around the cut became inflamed.','伤口周围的皮肤发炎了。'))
W('inflammation','/ˌɪnfləˈmeɪʃən/','炎症；发炎',
 '组织受到刺激、损伤或感染等影响后，出现一套反应，常见红、肿、热、痛，这就是 inflammation。火只是帮助理解旧命名，不是真在身体里燃烧。',
 '经法语接拉丁 inflammatio，来自 inflammare 点燃、激起；现代对应 inflame 去 e 加 -ation。',If+[['inflammatio → inflammation','发炎这一反应、状态']],
 'inflammation of the skin 皮肤炎症；signs of inflammation 炎症表现；reduce inflammation 减轻炎症。',
 'signs of inflammation；inflammation of。',
 'inflammation 是炎症，infection 是感染；损伤等也可引起炎症，不能把两个词一律当同义词。',
 ('The report describes inflammation around the joint.','报告描述了关节周围的炎症。'),('The study examines how inflammation develops.','研究考察炎症如何形成。'),sources=['https://en.wiktionary.org/wiki/inflammation#English','https://www.oxfordlearnersdictionaries.com/definition/english/inflammation'])
W('realization','/ˌrɪəlaɪˈzeɪʃən/','意识到；实现；变现〔特定语境〕',
 '“啊，原来如此”是在头脑里终于看清；多年计划真正落地，则是现实中的实现。realization 把 realize 的这些过程拿来谈。',
 '接法语 réalisation 等，与 realize + -ation 对应；real 真实的、实际的经使成实际、看清实际发展出不同分支。',
 [['real → realize','实际的 → 实现、清楚认识'],['realize + -ation → realization','意识到的过程；成为现实的结果']],
 'the realization that ... 意识到……；the realization of a dream 梦想的实现；asset realization 可指资产变现。',
 'the realization that；the realization of。',
 'realization 是看清、实现的过程或结果，reality 是现实本身；脑中意识到与外界做成，还要看具体搭配。',
 ('The realization that she was safe brought relief.','意识到自己安全后，她松了口气。'),('The project is the realization of a long-standing dream.','项目实现了一个长久以来的梦想。'))
Ch=[['希腊 charakter 标记等 → charakterizein → 拉丁相关形式','用特征标明、描述'],['英语 characterize → characterization','刻画、构成特征；特征描述、人物塑造']]
W('characterize','/ˈkærəktəraɪz/','描写、刻画；构成……的特征',
 '说某人最突出的特点是什么，是 characterize；某个特点反过来成为一个地方、时代的代表，也能作主语 characterize it。',
 '接希腊、拉丁按特征标明的动词材料，现代对应 character 特征、人物 + -ize，形成描述、赋予特征的动词。',Ch,
 'characterize someone as 把某人描述为；be characterized by 以……为特征；characterize a material 表征材料。',
 'characterize as；be characterized by。',
 'characterize as 是作一种描述，不保证描述公正；be characterized by 则指出对象的主要特点。',
 ('The region is characterized by dry summers.','这个地区以干燥的夏季为特征。'),('She characterized the plan as overly ambitious.','她把计划描述为过于雄心勃勃。'))
W('characterization','英 /ˌkærəktəraɪˈzeɪʃən/；美 /ˌkærəktərəˈzeɪʃən/','特征描述；人物塑造；表征〔专业〕',
 '小说怎样让一个人显出性格，是 characterization；研究怎样说明一种材料的性质，也是 characterization。共同点是把它是什么样说清楚。',
 'characterize 去 e 加 -ation，把刻画、标明特征的过程名词化；人物与材料只是不同对象。',Ch+[['characterize + -ation → characterization','对特征的描述；通过细节塑造人物']],
 'the characterization of a person 对人的描述；strong characterization 鲜明人物塑造；material characterization 材料表征。',
 'strong characterization；material characterization。',
 'characterization 不只文学，技术研究也常用；classification 是分类，不必已经详细描述每个对象。',
 ('The novel is praised for its vivid characterization.','小说以生动的人物塑造受到称赞。'),('The report includes the characterization of the new material.','报告包括新材料的表征。'))
St=[['古英语 steorfan → 中古英语 sterven','原来泛指死亡、死去'],['现代 starve → starvation','意义集中到挨饿、饿死；严重缺食状态']]
W('starve','英 /stɑːv/；美 /stɑːrv/','挨饿、饿死；使挨饿；极度缺乏',
 '身体得不到足够食物，是 starve 的核心。口语 I’m starving 常夸张说饿极了；be starved of information 则像一直没有得到所需的信息。',
 '接古英语 steorfan，早期只是死去，后来英语意义收窄到饥饿导致的衰弱、死亡等；与德语 sterben 死同源。',St,
 'starve to death 饿死；be starving 饿极了、正挨饿；be starved of something 严重缺少某物。',
 'be starving；starve to death；be starved of。',
 '口语 starving 可以夸张饥饿，正式 starvation 常是严重缺食；看语境决定实际强度。',
 ('I skipped lunch, and now I am starving.','我没吃午饭，现在饿极了。'),('The team was starved of reliable information.','团队极度缺乏可靠信息。'))
W('starvation','英 /stɑːˈveɪʃən/；美 /stɑːrˈveɪʃən/','严重饥饿；挨饿、饥饿致死',
 '不只是饭晚了一个小时，而是持续得不到足够食物，身体受到严重影响的处境，是 starvation。它把 starve 的状态整体命名。',
 'starve 去 e 加 -ation；从英语动词构成名词，词干与后缀相接后 /v/ 和重音位置发生对应变化。',St+[['starve + -ation → starvation','严重缺食的状态、过程及后果']],
 'face starvation 面临严重饥饿；die of starvation 饿死；prevent starvation 防止严重饥饿。',
 'face starvation；die of starvation。',
 'starvation 通常比 hunger 饥饿强；I’m hungry 日常想吃饭，不必译成自己正处在饥荒、饥饿致死状态。',
 ('The aid was intended to prevent starvation.','援助旨在防止人们遭受严重饥饿。'),('The report describes families facing starvation.','报告描述了面临严重饥饿的家庭。'))
Lg=[['legal 合法的 + -ize／-ise → legalize、legalise','使法律上得到允许'],['相应动词 + -ation → legalization、legalisation','合法化的过程、政策变化']]
W('legalise','/ˈliːɡəlaɪz/','使合法化〔legalize 的常见英式拼写〕',
 '原先法律不允许，后来改变规则，使某种行为得到法律允许，就是 legalise。s 与 z 是这一词族的拼写习惯差别。',
 'legal 合法的 + -ise；与 legalize 同词的拼写变体，legal 的远源接拉丁 lex 法律词族。',Lg,
 'legalise an activity 使某种活动合法化；legalise gambling 使赌博合法化；a proposal to legalise something 提议使某事合法化。',
 'legalise an activity；legalise gambling。',
 'legalise 与 decriminalise 的关注点不同：前者说合法化，后者说去除刑事罪名；具体制度变化仍看文本。',
 ('The article debates whether to legalise gambling.','文章讨论是否应让赌博合法化。'),('The proposal would legalise the activity under new rules.','提案将按新规则使这项活动合法化。'),sources=['https://en.wiktionary.org/wiki/legalise#English','https://kaikki.org/dictionary/English/meaning/l/le/legalise.html','https://www.oxfordlearnersdictionaries.com/definition/english/legalize'])
W('legalization','/ˌliːɡəlaɪˈzeɪʃən/','合法化',
 'legalize 是把某事变成法律允许的活动，legalization 把这个变化、相关政策过程作为讨论对象。',
 'legalize 去 e 加 -ation；legal 的合法材料加使成为的动词尾，再形成过程名词。',Lg+[['legalize + -ation → legalization','合法化的过程、制度改变']],
 'the legalization of an activity 某活动的合法化；debate legalization 讨论合法化；support or oppose legalization 支持或反对合法化。',
 'the legalization of；debate legalization。',
 'legalization 是变为合法的过程，legality 是目前是否合法这一性质；变化与状态角度不同。',
 ('The report examines the effects of legalization.','报告考察合法化的影响。'),('The debate concerns the legalization of the activity.','争论涉及这项活动的合法化。'),sources=['https://en.wiktionary.org/wiki/legalization#English','https://www.oxfordlearnersdictionaries.com/definition/english/legalize'])
W('legalisation','/ˌliːɡəlaɪˈzeɪʃən/','合法化〔legalization 的常见英式拼写〕',
 '看到 -sation，不必另背一种法律变化。它与 legalization 说的是同一个词义，只沿 legalise 的拼写习惯。',
 'legalise 去 e 加 -ation → legalisation；-ise、-ize 系列常相应出现 -isation、-ization。',Lg+[['legalise + -ation → legalisation','合法化，同词的拼写变体']],
 'the legalisation of something 某物合法化；legalisation debate 合法化争论。一般在同一篇文本里保持所选拼写一致。',
 'the legalisation of；a legalisation debate。',
 'legalisation 与 legalization 不分法律效果强弱；拼写不能告诉你某项政策具体取消了哪些限制。',
 ('The essay reviews arguments for legalisation.','文章回顾支持合法化的理由。'),('Legalisation became the central topic of the debate.','合法化成为辩论的中心话题。'))
W('modernization','英 /ˌmɒdənaɪˈzeɪʃən/；美 /ˌmɑːdərnəˈzeɪʃən/','现代化；更新改造',
 '旧设备、旧流程换成更符合当代需要的方式，是 modernization。它可以涉及技术，也可以涉及组织、制度。',
 '接法语 modernisation 或 modernize + -ation；modern 当代的，先形成使现代化的动词，再有过程名词的对应。',
 [['modern → modernize','当代的 → 使采用现代方式'],['modernize + -ation → modernization','现代化、更新改造的过程']],
 'the modernization of a railway 铁路现代化；industrial modernization 工业现代化；modernization plans 更新改造计划。',
 'the modernization of；modernization plans。',
 'modernization 强调转向当代方式，maintenance 是维护现有状态；修好旧设施未必就是现代化改造。',
 ('The railway is undergoing modernization.','铁路正在进行现代化改造。'),('The plan includes modernization of the hospital’s equipment.','计划包括医院设备的更新改造。'))
W('specialization','英 /ˌspeʃəlaɪˈzeɪʃən/；美 /ˌspeʃələˈzeɪʃən/','专门化、专业化；专业方向',
 '不再什么都平均做，而是把知识、技能集中到一个领域，是 specialization。也能把那个重点领域本身叫 a specialization。',
 'specialize 去 e 加 -ation；special 专门的、特殊的经 -ize 动词形式，再形成过程、领域名词。',
 [['special → specialize','专门的 → 专攻、专门从事'],['specialize + -ation → specialization','专业化过程；专门领域']],
 'a specialization in history 历史专业方向；professional specialization 职业专业化；division of labour and specialization 分工与专业化。',
 'a specialization in；professional specialization。',
 'specialization 是集中某一方向，expertise 是已经具备的专业知识、能力；选定方向不自动表示已成专家。',
 ('Her specialization is medieval history.','她的专业方向是中世纪历史。'),('The company encouraged greater specialization within the team.','公司鼓励团队内部进一步专业分工。'))
W('localization','英 /ˌləʊkəlaɪˈzeɪʃən/；美 /ˌloʊkələˈzeɪʃən/','本地化；定位；局部化',
 '把产品改得适合当地语言、习惯，是 localization；确定声音、物体在哪里，则是定位。共同材料是 local 某个地方、局部。',
 'localize 去 e 加 -ation，接 local 地方的、局部的。不同领域把使与某地相联系具体化为适配、定位、局限。',
 [['local → localize','地方、局部相关 → 使适应当地、确定位置等'],['localize + -ation → localization','本地化过程；定位或局部化']],
 'software localization 软件本地化；sound localization 声源定位；the localization of production 生产本地化。',
 'software localization；sound localization。',
 'localization 常比 translation 翻译范围宽，还可涉及格式、文化习惯；声源定位义又是另一具体分支。',
 ('The company invested in software localization.','公司投入资源做软件本地化。'),('The experiment tests sound localization.','实验测试声源定位能力。'))
Mb=[['法语 mobile 可移动的 → mobiliser、mobilisation','把人员、资源组织得可以行动'],['英语 mobilize／mobilise 与相应名词','调动、动员；可用于军队及普通社会行动']]
W('mobilize','英 /ˈməʊbəlaɪz/；美 /ˈmoʊbəlaɪz/','动员、调集；组织起来行动',
 '人力、钱、支持原来各在一处，你把它们组织起来投入某项行动，就是 mobilize。军队动员是其中一类，社区清理街道也能用。',
 '借法语 mobiliser，与 mobile 可移动的及 -ize 对应；从使可动走向把资源实际调动起来。',Mb,
 'mobilize support 动员支持；mobilize resources 调集资源；mobilize volunteers 动员志愿者。',
 'mobilize support；mobilize resources。',
 'mobilize 强调组织行动，motivate 强调激发意愿；有意愿的人仍可能需要被组织、调集。',
 ('The group mobilized volunteers to clean the beach.','团体动员志愿者清理海滩。'),('The team quickly mobilized the necessary resources.','团队迅速调集了必要资源。'))
W('mobilise','/ˈməʊbəlaɪz/','动员、调集〔mobilize 的常见英式拼写〕',
 '把支持者、资源组织起来行动，仍是同一个动词。mobilise 的 s 主要反映拼写习惯，不改变动员这个画面。',
 '法语 mobiliser 的相关借词形式，英语常写 mobilise 或 mobilize；-ise 与 -ize 是这一词族的对应拼写。',Mb,
 'mobilise resources 调动资源；mobilise support 动员支持；mobilise a team 组织团队行动。',
 'mobilise resources；mobilise support。',
 'mobilise 不只出现在战争新闻里；社会组织、企业、社区也常调动资源。',
 ('The campaign mobilised support across the region.','活动在整个地区动员起了支持。'),('Local groups mobilised to help the residents.','当地团体组织起来帮助居民。'))
W('mobilization','英 /ˌməʊbəlaɪˈzeɪʃən/；美 /ˌmoʊbələˈzeɪʃən/','动员；资源调集、组织行动',
 'mobilize 是让人、资源动起来，mobilization 则把这一整套准备、组织、投入行动的过程拿来讨论。',
 '接法语 mobilisation，或由 mobilize 去 e 加 -ation；保留 mobile 可动的词族材料。',Mb+[['mobilize + -ation → mobilization','人员、资源被组织并调动的过程']],
 'the mobilization of resources 资源调集；military mobilization 军事动员；community mobilization 社区动员。',
 'the mobilization of；community mobilization。',
 'mobilization 是组织和调动，movement 可以泛说运动、移动；一次物体位移未必涉及动员。',
 ('The response required rapid mobilization of resources.','应对工作需要迅速调集资源。'),('The study examines community mobilization after the flood.','研究考察洪水过后的社区动员。'))
W('mobilisation','/ˌməʊbəlaɪˈzeɪʃən/','动员、调集〔mobilization 的常见英式拼写〕',
 '沿 mobilise 的拼写把动作变成名词，就是 mobilisation。可谈人，也可谈物资、社会支持。',
 '接法语 mobilisation，现代对应 mobilise 去 e 加 -ation；与 mobilization 是同词的拼写变体。',Mb+[['mobilise + -ation → mobilisation','动员与资源调集的过程']],
 'resource mobilisation 资源调集；the mobilisation of volunteers 志愿者动员；social mobilisation 社会动员。',
 'resource mobilisation；the mobilisation of。',
 'mobilisation 的 s 不表示规模更小，也不表示只限民用；含义仍由修饰语和上下文决定。',
 ('The plan depends on the mobilisation of local volunteers.','计划依靠动员当地志愿者。'),('Resource mobilisation took longer than expected.','资源调集比预期花了更长时间。'))
Is=[['拉丁 infestus 敌对的 → infestare → 法语 infester','攻击、侵扰'],['英语 infest → infestation','害虫等大量侵扰、寄生；侵扰状态']]
W('infest','/ɪnˈfest/','大量侵扰、寄生〔害虫、鼠类等〕',
 '不是偶然飞进一只虫，而是某种不受欢迎的生物大量盘踞、侵扰一个地方，是 infest。',
 '经法语接拉丁 infestare 侵扰，基础 infestus 敌对的；更远来源未定。现代尤其用来描述害虫等大量存在。',Is,
 'rats infest a building 鼠类盘踞建筑；a house infested with insects 虫害严重的房屋；常见被动 be infested with。',
 'be infested with；infest a building。',
 'infest 常说害虫等侵扰场所、宿主，infect 是感染；食品厂有鼠患与人体遭感染，英语用词角度不同。',
 ('Mice had infested the old warehouse.','旧仓库里鼠患严重。'),('The cupboard was infested with moths.','柜子里蛾患严重。'))
W('infestation','/ˌɪnfesˈteɪʃən/','虫害、鼠患等；大量寄生、侵扰',
 'infest 是大量盘踞、侵扰，infestation 是已经形成的这种问题、状态。具体是什么侵扰，要看 of 或修饰语。',
 '经法语接晚期拉丁 infestatio，现代对应 infest + -ation；不是 inflammation 炎症的另一种拼写。',Is+[['infestatio → infestation','大量侵扰、寄生的状态或事件']],
 'an infestation of mice 鼠患；an insect infestation 虫害；signs of infestation 大量侵扰的迹象。',
 'an infestation of；signs of infestation。',
 'infestation 与 infection、inflammation 是三件不同的事：大量侵扰、感染、炎症，要按对象和上下文区分。',
 ('The house had an infestation of mice.','房子里有鼠患。'),('The inspection found signs of insect infestation.','检查发现了虫害迹象。'))
Hs=[['hospital 医院 + -ize → hospitalize','使进入医院接受住院诊疗'],['hospitalize + -ation → hospitalization','住院过程、经历或次数']]
W('hospitalize','英 /ˈhɒspɪtəlaɪz/；美 /ˈhɑːspɪtəlaɪz/','使住院、送入医院治疗',
 '不是到医院问完问题就走，而是被收治、留在医院接受诊疗，这时常说 be hospitalized。',
 'hospital 医院 + -ize，使进入相应状态、场所；词族与接待来客的拉丁医院、旅舍材料相连。',Hs,
 'be hospitalized 住院；be hospitalized with an illness 因病住院；hospitalize a patient 收治病人。',
 'be hospitalized；hospitalize a patient。',
 'hospitalize 常着眼住院收治，visit a hospital 可能只是看门诊、探视；到过医院不一定住了院。',
 ('She was hospitalized after the accident.','事故后她住进了医院。'),('The report states that three people were hospitalized.','报告说有三个人住院。'),sources=['https://en.wiktionary.org/wiki/hospitalize#English','https://kaikki.org/dictionary/English/meaning/h/ho/hospitalize.html'])
W('hospitalization','英 /ˌhɒspɪtəlaɪˈzeɪʃən/；美 /ˌhɑːspɪtələˈzeɪʃən/','住院；住院治疗、经历',
 'hospitalize 是收治住院，hospitalization 把这段住院过程或这次经历作为名词。统计里复数还可数住院事件。',
 'hospitalize 去 e 加 -ation，形成过程、事件名词；保留 hospital 医院这一完整基础。',Hs+[['hospitalize + -ation → hospitalization','住院收治的过程；一次住院经历']],
 'require hospitalization 需要住院；a period of hospitalization 一段住院时间；hospitalization rates 住院率。',
 'require hospitalization；hospitalization rates。',
 'hospitalization 是住院经历、收治，hospital 是机构或场所；报告多少次住院与统计多少家医院不同。',
 ('The injury required hospitalization.','伤势需要住院治疗。'),('The study recorded several hospitalizations during the year.','研究记录了这一年间的几次住院。'))
W('standardization','英 /ˌstændədaɪˈzeɪʃən/；美 /ˌstændərdəˈzeɪʃən/','标准化；统一规范',
 '原来各做各的，尺寸、格式、做法不一致，后来按共同标准对齐，是 standardization。关键是有一个大家能对照的规范。',
 'standardize 去 e 加 -ation；standard 标准经 -ize 形成使标准化的动词，再以名词谈过程。',
 [['standard → standardize','标准 → 使符合共同标准'],['standardize + -ation → standardization','统一标准、规范的过程']],
 'the standardization of procedures 流程标准化；data standardization 数据标准化；standardization efforts 标准化工作。',
 'the standardization of；data standardization。',
 'standardization 不必把所有内容做得一模一样，可以只统一单位、接口、格式；individual content 仍能不同。',
 ('Standardization made the parts easier to replace.','标准化让零件更容易替换。'),('The team worked on the standardization of reporting formats.','团队着手统一报告格式。'))
Po=[['拉丁 prae- 在先 + occupare 占据 → praeoccupare、praeoccupatio','先占住某处、某种注意力'],['英语 preoccupied、preoccupation','心思被占着；反复挂念的状态、事情']]
W('preoccupied','英 /priˈɒkjupaɪd/；美 /priˈɑːkjupaɪd/','心事重重的；心不在焉的；一心想着的',
 '别人正在说话，你脑子却早被另一件事占满，注意力接不进来，就是 preoccupied。可能是担忧，也可能只是太专注别的事。',
 'preoccupy 占据心思的过去分词、形容词，接 pre- 在先与 occupy 占据的材料；现代重心是注意力已被别的事情占着。',Po,
 'be preoccupied with work 一心想着工作；look preoccupied 显得有心事；too preoccupied to notice 忙着想别的而没注意到。',
 'be preoccupied with；look preoccupied。',
 'an occupied room 是房间被占用，a preoccupied person 是人的心思被别事占着；前者还可说空间，后者常说注意力。',
 ('She seemed preoccupied during the meeting.','开会时她似乎心事重重。'),('He was preoccupied with the coming examination.','他心里一直想着即将到来的考试。'),sources=['https://en.wiktionary.org/wiki/preoccupied#English','https://www.oxfordlearnersdictionaries.com/definition/english/preoccupied'])
W('preoccupation','英 /priˌɒkjuˈpeɪʃən/；美 /priˌɑːkjuˈpeɪʃən/','一心想着；反复挂念的事；心神不属',
 '一件事一直占着脑子，是 preoccupation 的状态；那件占住心思的事情本身，也能叫 a preoccupation。',
 '经法语接拉丁 praeoccupatio，来自事先占据的材料；现代与 preoccupy、preoccupied 对应，不能只按 occupation 职业义来译。',Po+[['praeoccupatio → preoccupation','先占据 → 心思被占住、常想的事']],
 'a preoccupation with money 一心想着钱；a major preoccupation 主要挂心的事；in a state of preoccupation 心神不属。',
 'a preoccupation with；a major preoccupation。',
 'preoccupation 可以是正常关心的重要事，也可带过度专注的评价；不必每次都译成病态迷恋。',
 ('Her main preoccupation was finding a safe place to live.','她最挂心的是找到安全住处。'),('His preoccupation with detail slowed the discussion.','他过度纠结细节，让讨论慢了下来。'),sources=['https://en.wiktionary.org/wiki/preoccupation#English','https://www.oxfordlearnersdictionaries.com/definition/english/preoccupation'])
W('dispensation','/ˌdɪspenˈseɪʃən/','特许、豁免；施予、分配；制度、秩序〔正式〕',
 '一般规则要求大家都做到，有权决定的人却给某个情况开了特许口子，是 dispensation。另一条用法是把某种资源、正义等施予出去。',
 '经法语接拉丁 dispensatio，来自 dispensare 分配、管理，远接 dis- 分开与 pendere 称量。现代分支包含分配、管理安排、特许等。',
 [['拉丁 dis- + pendere 等 → dispensare、dispensatio','称量分派、管理安排'],['英语 dispensation','施予、分配；特许豁免；特定制度']],
 'a special dispensation 特别许可；dispensation from a requirement 免于某要求的特许；the dispensation of justice 司法公正的施行。',
 'a special dispensation；dispensation from。',
 'dispensation 的豁免来自有权作出的特别安排，disobedience 是不服从；一个是特许，一个是违反要求。',
 ('The student received dispensation from the attendance requirement.','学生获得了免于出勤要求的特许。'),('The essay discusses the dispensation of justice.','文章讨论司法公正的施行。'),sources=['https://en.wiktionary.org/wiki/dispensation#English','https://www.oxfordlearnersdictionaries.com/definition/english/dispensation'])
Ca=[['category 类别 + -ize → categorize','按类别把对象分组'],['categorize + -ation → categorization','分类的过程、方法、结果']]
W('categorize','/ˈkætəɡəraɪz/','分类；把……归为某类',
 '面前一堆东西，你决定哪些放同一格、分别叫什么类，是 categorize。把人归成一种类型，也是在做这种分类。',
 'category 类别去 y 接 -ize → categorize；category 远接希腊断言、范畴的材料，现代动词强调归类动作。',Ca,
 'categorize by size 按大小分类；categorize something as something 将某物归为某类；categorize into groups 分组。',
 'categorize by；categorize as。',
 'categorize 是归类，characterize 是描述特征；描述可以帮助分类，但不等于已经选定类别。',
 ('The files are categorized by topic.','文件按主题分类。'),('She categorized the problem as a design issue.','她把问题归为设计问题。'))
W('categorization','英 /ˌkætəɡəraɪˈzeɪʃən/；美 /ˌkætəɡərəˈzeɪʃən/','分类、归类；分类方式',
 'categorize 是放入类别，categorization 是这套归类过程或安排。类别怎样划分，会影响我们怎样看待对象。',
 'categorize 去 e 加 -ation，把分类动作名词化；与 category 类别、categorical 类别的等同族相照。',Ca+[['categorize + -ation → categorization','分类行为、方法或结果']],
 'the categorization of data 数据分类；automatic categorization 自动归类；a simple categorization 简单分类方式。',
 'the categorization of；automatic categorization。',
 'categorization 的类别是一种整理方式，不必穷尽对象的所有特征；无法整齐归类不等于对象本身有错。',
 ('The system supports automatic categorization of messages.','系统支持自动分类消息。'),('The book questions this simple categorization.','书中对这种简单分类提出质疑。'))
Ut=[['拉丁 utilis 有用的、uti 使用 → 法语 utiliser','把事物用于某目的'],['英语 utilise → utilisation','利用；使用、发挥用途的过程']]
W('utilise','/ˈjuːtɪlaɪz/','利用、使用〔utilize 的常见英式拼写〕',
 '把手头资源用起来，让它在某个目的上发挥作用，是 utilise。它比 use 正式，但并不另指一种神秘的使用动作。',
 '借法语 utiliser，接意大利语、拉丁有用、使用的词族材料；现代与 utilize 对应，-ise 是相应拼写。',Ut,
 'utilise resources 利用资源；utilise space 利用空间；utilise information 利用信息。',
 'utilise resources；utilise space。',
 'utilise 与 utilize 同义；use 是更普通的常用动词，不必所有简单使用都换成长词。',
 ('The design utilises the available space efficiently.','设计高效利用了现有空间。'),('The team utilised data from earlier studies.','团队利用了先前研究的数据。'))
W('utilisation','/ˌjuːtɪlaɪˈzeɪʃən/','利用、使用；利用程度〔搭配〕',
 '资源怎样被用上、用到了多少，是 utilisation 讨论的事情。机器闲着还是忙着，报告里也常用这个名词。',
 '接法语 utilisation，现代对应 utilise 去 e 加 -ation；与 utilization 是同词的拼写变体。',Ut+[['utilise + -ation → utilisation','使用过程；所能发挥的使用程度']],
 'resource utilisation 资源利用；capacity utilisation 产能利用；utilisation rate 利用率，具体计算按指标定义。',
 'resource utilisation；capacity utilisation。',
 'utilisation 是使用的过程、程度，utility 可指用途、效用或公用事业；名词不能只看共同的 util- 就互换。',
 ('The report examines resource utilisation.','报告考察资源利用情况。'),('Better scheduling improved the utilisation of the equipment.','改进排程提高了设备利用率。'))
Fl=[['早期英语 flirt、flurt 等词形交汇','轻弹、嘲弄等旧材料；确切远源未定'],['现代 flirt → flirty、flirtation','调情；短暂玩味某种想法、活动及其相应状态']]
W('flirt','英 /flɜːt/；美 /flɜːrt/','调情；短暂考虑、涉足〔搭配〕；爱调情的人',
 '说话、微笑带着暧昧、逗趣的吸引，是 flirt with someone。对一个想法有点心动，却还没认真投入，也能 flirt with the idea。',
 '早期英语 flirt、flurt 等轻弹、嘲弄的词形和人物称呼发生交汇，较远来历未定；现代集中在轻巧、试探性的亲近与尝试。',Fl,
 'flirt with someone 与某人调情；flirt with the idea of doing 短暂考虑做；a flirt 爱调情的人。',
 'flirt with someone；flirt with the idea。',
 'flirt with an idea 说想法上的试探，未必涉及恋爱；和人调情也不保证存在认真、持久的恋爱意图。',
 ('He flirted with her at the party.','他在聚会上和她调情。'),('She flirted with the idea of moving abroad.','她曾短暂考虑过搬到国外。'))
W('flirty','英 /ˈflɜːti/；美 /ˈflɜːrti/','爱调情的；带暧昧意味的',
 '一句话、一个笑容让人觉得带着试探性的吸引，是 flirty。它描述氛围、表达方式，也能描述人的倾向。',
 'flirt + -y，形成带有调情性质的形容词；同一基础词在日常口语里的短扩展。',Fl+[['flirt + -y → flirty','爱调情、表现暧昧的性质']],
 'a flirty smile 暧昧笑容；a flirty message 带调情意味的信息；a flirty tone 轻佻、暧昧的语气。',
 'a flirty smile；a flirty tone。',
 'flirty 比 friendly 友好更可能带吸引、暧昧意味；判断具体交流时，仍要看言语、情境。',
 ('She sent him a flirty message.','她给他发了一条带调情意味的信息。'),('The dialogue has a light, flirty tone.','对话带着轻松暧昧的语气。'))
W('flirtation','英 /flɜːˈteɪʃən/；美 /flɜːrˈteɪʃən/','调情；短暂暧昧关系；短暂涉足',
 'flirt 是试探性地亲近，flirtation 是这段调情、暧昧；对艺术流派、职业方向试了一阵又离开，也能叫 a flirtation with it。',
 'flirt + -ation，英语把外来的名词尾用到这个本族发展词上；不需要假设整词先存在于拉丁语。',Fl+[['flirt + -ation → flirtation','轻巧、短暂的亲近或尝试']],
 'a brief flirtation 短暂调情、暧昧；a flirtation with politics 短暂涉足政治；a harmless flirtation 无伤大雅的调情，含说话者评价。',
 'a brief flirtation；a flirtation with。',
 'flirtation 通常比 commitment 投入、承诺轻；短暂试水不表示决定长期走这条路。',
 ('Their flirtation lasted only a few weeks.','他们的暧昧只持续了几周。'),('Her flirtation with abstract art was brief.','她只短暂涉足过抽象艺术。'))
Mn=[['拉丁 moneta 钱币等 → 法语 monétiser','把事物与货币、收益相联系'],['英语 monetize → monetization','变现、货币化；相应收益机制与过程']]
W('monetize','/ˈmʌnətaɪz/，亦有 /ˈmɒnətaɪz/','使变现；从……获取收益；货币化',
 '有人看你的内容，是关注；把这些关注接成广告、订阅等收入，才是常见互联网语境的 monetize。它说怎么变成收入。',
 '借法语 monétiser，关联拉丁 moneta 钱币与使成为的动词尾；现代内容、平台的变现义是货币材料的扩展。',Mn,
 'monetize content 内容变现；monetize an audience 将受众注意力转为收益；monetize a service 从服务获取收入。',
 'monetize content；monetize a service。',
 'monetize 说获得收入的机制，不保证已经 profitable 盈利；有收入仍可能覆盖不了成本。',
 ('The company monetizes the service through subscriptions.','公司通过订阅从这项服务获得收入。'),('The creators are exploring ways to monetize their content.','创作者在探索内容变现方式。'))
W('monetization','/ˌmʌnətaɪˈzeɪʃən/，亦有 /ˌmɒnətaɪˈzeɪʃən/','变现；货币化；收益获取机制',
 'monetize 是把某种价值接成收入，monetization 是这个过程、策略或机制。金融等领域还有更具体的货币化用法。',
 'monetize 去 e 加 -ation，形成过程名词；接前面钱币、货币的词族材料。',Mn+[['monetize + -ation → monetization','转为货币收益的过程、机制']],
 'a monetization strategy 变现策略；content monetization 内容变现；monetization through advertising 通过广告获收入。',
 'a monetization strategy；content monetization。',
 'monetization 是变成收入的方式，valuation 是价值评估；估值很高与已经能赚钱是两回事。',
 ('The app’s monetization relies on subscriptions.','应用的变现依赖订阅。'),('The team tested several monetization strategies.','团队测试了几种变现策略。'))
Dc=[['de- 去除 + criminalization 定为犯罪的过程','取消某行为的刑事犯罪地位'],['decriminalization → decriminalize 的逆构对应','较长名词提供短动词的形成材料']]
W('decriminalize','/diːˈkrɪmɪnəlaɪz/','使非刑罪化；不再按刑事犯罪处理',
 '一项行为原先按刑事犯罪处理，后来撤去这种定性，就是 decriminalize。它关注刑事处罚这一层，其他规则可能仍存在。',
 '词史有从 decriminalization 去掉名词尾逆构的解释；现代对应 de- 去除 + criminalize 定为犯罪，不必把短动词画成历史上必然先有。',Dc,
 'decriminalize an activity 使某行为非刑罪化；a proposal to decriminalize 提议取消某刑事罪名。',
 'decriminalize an activity；a proposal to decriminalize。',
 'decriminalize 与 legalize 常在同一议题出现；去掉刑事罪名，不自动表示一切许可、行政规则也已取消。',
 ('The proposal would decriminalize the activity.','提案将不再把这项行为按刑事犯罪处理。'),('The article explains what it means to decriminalize an offence.','文章解释取消某项刑事罪名意味着什么。'),sources=['https://en.wiktionary.org/wiki/decriminalize#English','https://www.oxfordlearnersdictionaries.com/definition/english/decriminalize'])
W('decriminalization','/diːˌkrɪmɪnəlaɪˈzeɪʃən/','非刑罪化；取消刑事犯罪地位',
 '把刑事罪名这一层移开，这个过程叫 decriminalization。它把制度变化作为名词，便于讨论范围、效果和争议。',
 'de- 去除 + criminalization 刑罪化；现代也可与 decriminalize + -ation 对应。短动词有从这个长名词逆构的词史。',Dc,
 'the decriminalization of an activity 某行为非刑罪化；debate decriminalization 讨论非刑罪化。',
 'the decriminalization of；debate decriminalization。',
 'decriminalization 与 legalization 的具体边界要看制度文本；常见学习重点是取消刑罪与法律许可这两个不同焦点。',
 ('The paper distinguishes decriminalization from legalization.','论文区分非刑罪化与合法化。'),('Decriminalization became a major topic in the discussion.','非刑罪化成为讨论中的重要议题。'),sources=['https://en.wiktionary.org/wiki/decriminalization#English','https://www.oxfordlearnersdictionaries.com/definition/english/decriminalize'])
Mi=[['拉丁 minimus 最小的 + -ize → minimize','把量或作用降到尽量小'],['minimize + -ation → minimization','最小化；淡化严重程度的做法']]
W('minimize','/ˈmɪnɪmaɪz/','尽量减少；淡化；最小化〔界面、数学〕',
 '把损失、浪费压低，是 minimize；把严重问题说得很轻，也是 minimize。电脑把窗口收起，则取最小化显示的技术义。',
 '拉丁 minimus 最小的 + -ize 形成使尽量小的动词；英语再把数量、影响、界面操作等具体化。',Mi,
 'minimize waste 减少浪费；minimize the risk 尽量降低风险；minimize a problem 淡化问题；minimize a window 最小化窗口。',
 'minimize waste；minimize a window。',
 'minimize 常是尽量降低，不必降为零；eliminate 才常说消除。淡化问题的用法还可能带负面评价。',
 ('The design aims to minimize waste.','设计旨在尽量减少浪费。'),('He tried to minimize the seriousness of the mistake.','他试图淡化错误的严重性。'))
W('minimization','/ˌmɪnɪmaɪˈzeɪʃən/','最小化；尽量减少；淡化',
 'minimize 是把量压低，minimization 是这套减少过程；数学里可寻找目标函数的最小值，交流里也可说淡化问题。',
 'minimize 去 e 加 -ation，把使尽量小的动作名词化。不同对象让它成为优化、节约或话语评价。',Mi+[['minimize + -ation → minimization','减到尽量小的过程；弱化问题的表述']],
 'waste minimization 减少废弃物；cost minimization 成本最小化；the minimization of a problem 淡化问题。',
 'waste minimization；cost minimization。',
 'minimization 讨论怎样减少某量，minimum 是得到的最小值、下限；过程名词与数值名词分开。',
 ('The project focuses on waste minimization.','项目着重减少废弃物。'),('The report criticises the minimization of the problem.','报告批评了淡化问题的做法。'))
W('initialization','英 /ɪˌnɪʃəlaɪˈzeɪʃən/；美 /ɪˌnɪʃələˈzeɪʃən/','初始化；初始设置',
 '一件新东西要开始工作，先把数值、资源、状态设到起点，这个准备过程是 initialization。它不必等于重置所有旧数据。',
 'initialize 去 e 加 -ation；initial 最初的、开始的经 -ize 形成置于初始状态的动词，再名词化。',
 [['initial → initialize','初始的 → 设置初始值、状态'],['initialize + -ation → initialization','初始化、开始前的状态准备']],
 'system initialization 系统初始化；variable initialization 变量初始化；during initialization 初始化期间。',
 'system initialization；variable initialization。',
 'initialization 是设初始状态，installation 是安装；程序已安装好，仍可能每次启动时初始化某些资源。',
 ('The initialization takes only a few seconds.','初始化只需几秒。'),('The program failed during initialization.','程序在初始化时失败了。'))
W('capitalisation','/ˌkæpɪtəlaɪˈzeɪʃən/','使用大写；资本化；市值〔搭配〕',
 '文字里问首字母该不该大写，是 capitalisation；企业语境还可涉及资本化，market capitalisation 则是市值。先看对象是字母还是资金、企业。',
 'capitalise 去 e 加 -ation，与 capitalization 为同词变体；capital 的大写字母和资本分支分别进入这个名词。',
 [['capital → capitalise／capitalize','大写字母、资本等 → 相应处理动作'],['capitalise + -ation → capitalisation','使用大写；资本化；特定搭配中的市值']],
 'capitalisation rules 大写规则；market capitalisation 市值；the capitalisation of costs 成本资本化，属会计专门用法。',
 'capitalisation rules；market capitalisation。',
 '大写与资本两条现义不要只背成一种；market capitalisation 不是公司的名字写了多少个大写字母。',
 ('Check the capitalisation of every title.','检查每个标题的大小写。'),('The chart compares the companies by market capitalisation.','图表按市值比较这些公司。'))
Se=[['serial 成序列的、连载的 + -ize → serialize','使内容成为一系列、按一定顺序表示'],['serialize + -ation → serialization','分期连载；数据序列化']]
W('serialize','英 /ˈsɪəriəlaɪz/；美 /ˈsɪriəlaɪz/','分期连载；序列化〔数据〕',
 '小说拆成一期一期发表，是 serialize；程序把结构化数据转成可存储、传送的顺序表示，也是 serialize。两者都把内容安排成一串。',
 'serial 序列的、连载的 + -ize；计算机用法发展为把数据转成约定的顺序表示，以便保存、传输、恢复相应数据。',Se,
 'serialize a novel 连载小说；serialize data 序列化数据；serialize an object 序列化对象的相关数据表示。',
 'serialize a novel；serialize data。',
 'serialize 不等于 encrypt 加密；数据排成可保存的形式，并不自动变成别人无法读取的密文。',
 ('The magazine serialized her first novel.','杂志分期刊登了她的第一部小说。'),('The program serializes the data before sending it.','程序在发送前把数据序列化。'),sources=['https://en.wiktionary.org/wiki/serialize#English','https://kaikki.org/dictionary/English/meaning/s/se/serialize.html'])
W('serialization','英 /ˌsɪəriəlaɪˈzeɪʃən/；美 /ˌsɪriələˈzeɪʃən/','连载；序列化',
 'serialize 是把内容按期、按序排出来，serialization 是这个过程或安排。程序里重在有约定的数据表示，之后能据此恢复相应内容。',
 'serialize 去 e 加 -ation，接 serial 序列的词族；小说分期发布与数据转换在不同领域具体化。',Se+[['serialize + -ation → serialization','连载过程；数据转为顺序表示的过程']],
 'the serialization of a novel 小说连载；data serialization 数据序列化；a serialization format 序列化格式。',
 'data serialization；a serialization format。',
 'serialization 不保证压缩数据，compression 才说压缩；某些格式甚至会增加可读标签和额外信息。',
 ('The serialization of the novel attracted new readers.','小说连载吸引了新读者。'),('The error occurred during data serialization.','错误发生在数据序列化期间。'))
Ne=[['neutral 中性的、不偏向的 + -ize → neutralize','使某种作用被抵消、不再占优势'],['法语 neutralisation 等 → neutralization','中和；使失去作用的过程']]
W('neutralize','英 /ˈnjuːtrəlaɪz/；美 /ˈnuːtrəlaɪz/','中和；抵消、使失去作用',
 '一种作用被另一种作用抵住，不再像原先那样起效，是 neutralize。可以谈酸碱，也可以谈对手优势、某项因素的影响。',
 '接法语 neutraliser，现代对应 neutral 中性的 + -ize；把不偏一方、中性的材料具体化为抵消效力。',Ne,
 'neutralize an acid 中和酸；neutralize an advantage 抵消优势；neutralize a threat 消除威胁。',
 'neutralize an acid；neutralize an advantage。',
 'neutralize 侧重使作用不起效，remove 可能是把对象搬走；抵消效果不必让原有物质、对象完全消失。',
 ('The experiment shows how the base neutralizes the acid.','实验展示碱如何中和酸。'),('Their advantage was neutralized by the new rule.','新规则抵消了他们的优势。'))
W('neutralization','英 /ˌnjuːtrəlaɪˈzeɪʃən/；美 /ˌnuːtrələˈzeɪʃən/','中和；抵消、使失去作用',
 'neutralize 是抵消作用，neutralization 是中和、消除效力的过程。化学、免疫、策略等领域各有自己的具体对象。',
 '借法语 neutralisation，也对应 neutralize 去 e 加 -ation；名词化后可讨论反应、过程及其效果。',Ne+[['neutralize + -ation → neutralization','中和、抵消效力的过程']],
 'acid–base neutralization 酸碱中和；the neutralization of a threat 威胁的消除；a neutralization reaction 中和反应。',
 'a neutralization reaction；the neutralization of。',
 'neutralization 不等于所有对象都恢复成原样；它聚焦作用被抵消，reversal 才更突出过程、状态反转。',
 ('Neutralization is one type of chemical reaction.','中和是一类化学反应。'),('The report describes the neutralization of the threat.','报告描述了威胁如何被消除。'))
W('immobilization','英 /ɪˌməʊbɪlaɪˈzeɪʃən/；美 /ɪˌmoʊbələˈzeɪʃən/','固定；使不能移动；限制活动',
 '把原本能动的部分固定住，或让车辆无法移动，这种使不动的过程、状态是 immobilization。',
 'immobilize 去 e 加 -ation；im- 不与 mobil- 可移动的材料，再接动词、名词尾。也与法语 immobilisation 相应。',
 [['im- + mobile 等 → immobilize','使不能移动、固定'],['immobilize + -ation → immobilization','固定过程；活动受到限制的状态']],
 'temporary immobilization 暂时固定；vehicle immobilization 车辆锁止；prolonged immobilization 长时间固定、活动受限。',
 'temporary immobilization；prolonged immobilization。',
 'immobilization 是使不动，mobilization 是动员、使动起来；im- 在这里起否定作用，关注点相反。',
 ('The device allows temporary immobilization of the vehicle.','装置可暂时使车辆无法移动。'),('The report discusses prolonged immobilization after injury.','报告讨论受伤后的长时间固定。'))
Oc=[['拉丁 ob- + capere 拿住的材料 → occupare','占住、抓住；组合后词干发生变化'],['法语 occuper → 英语 occupy → occupied 等','占空间、时间、注意力；处于被占用的状态']]
W('occupy','英 /ˈɒkjʊpaɪ/；美 /ˈɑːkjəpaɪ/','占用、占据；居住、使用；使忙于',
 '椅子上有人，空间被占；一天全在开会，时间被占；一件事让你不停地想，注意力也被占。这个占住就是 occupy 的核心。',
 '经法语 occuper 接拉丁 occupare，关联 ob- 与 capere 拿、抓的材料，拉丁词干在组合中改变。过去式 occupied 把 y 改 i 再加 -ed。',Oc,
 'occupy a room 占用、使用房间；occupy time 占时间；occupy someone’s thoughts 占据某人心思；occupy territory 占领地区。',
 'occupy a room；occupy someone’s thoughts。',
 'occupy 是占着、使用的状态或动作，own 是拥有产权；租客可以 occupy 一间房而不 own 它。',
 ('The desk occupies most of the room.','桌子占了房间的大部分空间。'),('The question occupied her thoughts all afternoon.','整个下午，她脑子里都在想那个问题。'),sources=['https://en.wiktionary.org/wiki/occupy#English','https://kaikki.org/dictionary/English/meaning/o/oc/occupy.html'])
W('occupied','英 /ˈɒkjʊpaɪd/；美 /ˈɑːkjəpaɪd/','被占用的；忙着的；被占领的',
 '洗手间门上写 Occupied，表示里面有人。用在人身上，心力、时间被事情占着，就可以说忙着。',
 'occupy 的 y 改 i，加 -ed → occupied，既是过去式、过去分词，也作形容词。一个占据核心，按对象分成空间、忙碌、占领等场景。',Oc+[['occupy + -ed → occupied','被占用、正忙、处于占领状态']],
 'an occupied seat 有人的座位；keep someone occupied 让某人有事做；occupied territory 被占领地区。',
 'an occupied seat；keep someone occupied。',
 'occupied 常说空间、时间被占用；preoccupied 常说心思被某事占住而顾不上别的；occupied 的 -ed 不自动表示整句过去。',
 ('Every seat was occupied.','每个座位都有人。'),('The puzzle kept the children occupied.','拼图让孩子们一直有事做。'),sources=['https://en.wiktionary.org/wiki/occupied#English','https://kaikki.org/dictionary/English/meaning/o/oc/occupied.html'])

R('A1862','动作、过程、状态及相应结果；也可指具体对象','-ATION：把动词所做的事，或形成的结果，作为名词来谈','compile 汇编 → compilation 汇编作品；starve 挨饿 → starvation 严重饥饿；mobilize 动员 → mobilization 动员过程。',
 '不要只把它译成某某化。compilation 可以是一本合集，realization 可以是突然意识到，dispensation 可以是特许。名词尾告诉你能把事情整体拿来谈，具体谈什么，仍由基础词和用法决定。',
 '主要接法语、拉丁 -atio、-ation- 等动作名词材料，也广用于英语类推构词。compile、starve 等常去末尾 e 加 -ation；realize、mobilize 等相应形成 -ization。-ate 结尾的 vibrate 等通常去 e 加 -ion，外观也成为 -ation。借入历史不总按英语短词先、长词后：decriminalize 有从 decriminalization 逆构的解释。-ise、-ize 系列常相应出现 -isation、-ization。',
 [['汇编、理解、描写与严重缺食','compile · compilation · realize · realization · characterize · characterization · starve · starvation'],['炎症、大量侵扰与住院','inflame · inflammation · infest · infestation · hospitalize · hospitalization'],['合法化与刑事罪名变化','legalize · legalise · legalization · legalisation · decriminalize · decriminalization'],['时代、专业、地方与标准','modernize · modernization · specialize · specialization · localize · localization · standardize · standardization'],['动员与固定','mobilize · mobilization · mobilise · mobilisation · immobilize · immobilization'],['占据、挂念、分配与分类','occupy · occupied · occupation · preoccupied · preoccupation · dispense · dispensation · category · categorize · categorization'],['利用、变现、减少与抵消','utilize · utilization · utilise · utilisation · monetize · monetization · minimize · minimization · neutralize · neutralization'],['计算机、字母与资本的专门用法','initialize · initialization · capitalize · capitalization · capitalisation · serialize · serialization'],['轻巧亲近与短暂尝试','flirt · flirty · flirtation']],
 'inflammation 炎症、infection 感染、infestation 大量侵扰分用；localization 本地化可超出翻译；capitalisation 按字母、资本语境分义；序列化不等于加密或压缩；英美拼写变体放在相应词族一起看。',
 'The compilation combines observations from several studies and explains the categorization of the data.\n\n这份汇编结合了几项研究的观察，并解释数据如何分类。',
 'compile compilation inflame inflammation realize realise realization characterize characterization starve starvation legalize legalise legalization legalisation modernize modernization specialize specialization localize localization mobilize mobilization mobilise mobilisation infest infestation hospital hospitalize hospitalization standardize standardization occupy occupied occupation preoccupied preoccupation dispense dispensation category categorize categorization utilize utilization utilise utilisation flirt flirty flirtation monetize monetization decriminalize decriminalization minimize minimization initialize initialization capital capitalize capitalization capitalisation serialize serialization neutralize neutralization immobilize immobilization information conversation combination transportation formation explanation organisation preparation registration implementation presentation examination imagination interpretation motivation transformation exploration determination observation confirmation variation consultation resignation adaptation civilization preservation expectation configuration documentation reservation activation designation authorization confrontation temptation continuation limitation relaxation optimization accusation degradation deportation sanitation accreditation consolation quotation experimentation notation globalization instrumentation manifestation oxidation civilisation inclination colonization authentication computation alteration visualization aspiration stabilization misinformation privatization fragmentation segmentation deforestation stagnation deformation reclamation flotation condensation inhalation adoration synchronization causation improvisation sterilization industrialization fertilization importation derivation urbanization ionization excitation socialization immunization electrification normalization commercialization misrepresentation globalisation supplementation connotation revocation summation invocation menstruation recitation revitalization decentralization pigmentation polymerization liberalization victimization discoloration germination democratization ornamentation rationalization centralization disorientation equalization misinterpretation perspiration sedimentation reconsideration indentation permutation encapsulation memorization prioritization militarization personalization criminalization digitization reforestation oxygenation harmonization immunisation magnetization dramatization maximization mechanization exportation exhalation politicization sensitization dehumanization stigmatization vocalization homogenization sexualization idealization digitalization summarization familiarization computerization')
for k in ROOTS[-1]['exclude']:
    ROOTS[-1]['exclude'][k]='先保留常用动作、过程名词及基础词；较少用的学科专门名词保留原资料，不为填满词表硬列。'
R('B4036','调情；轻巧、短暂地涉足或考虑','FLIRT：先试探地靠近，未必认真投入','flirt with someone 和人调情；flirt with an idea 对一个想法有点心动；flirty 是这种语气，flirtation 是这段短暂亲近。',
 '早期 flirt、flurt 的轻弹、嘲弄等词形发生交汇，确切远源未定。现代最好从轻巧、带试探的亲近记：对人可带暧昧，对想法、活动则是短暂尝试。',
 'flirt + -y → flirty 带调情性质的；flirt + -ation → flirtation 调情、短暂涉足的过程或经历。-ation 在这里是英语使用外来名词尾，不要求整个词先在拉丁语存在。',
 [['人际间的试探性亲近','flirt · flirty'],['过程、关系与短暂涉足','flirtation']],
 'friendly 友好与 flirty 暧昧有侧重；flirtation 是轻巧、短暂的接触，commitment 才着眼认真投入和承诺。',
 'His flirtation with painting lasted only one summer.\n\n他只在一个夏天里短暂尝试过绘画。','flirt flirty flirtation')
for x in WORDS:
    if x['word']=='capitalisation':x['sources'].append('https://www.oxfordlearnersdictionaries.com/definition/english/capitalization')

if __name__=='__main__':save('continuation_20261030_pp',ROOTS,WORDS)
