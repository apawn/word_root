"""Education, activity, woman and beauty: useful related common words."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
def C(a,b,w,m):return [[a+'；'+b,'并列构词部分'],[w,m]]
ED=[['拉丁语 ēducāre → ēducātus、ēducātiō 词族','养育、训练、教育；相应分词和活动名词'],['英语 educate、education 及其派生','教育、培养；教育活动、过程']]
W('reeducation','英 /ˌriːedʒʊˈkeɪʃən/；美 /ˌriːedʒəˈkeɪʃən/','再教育；重新训练；某些语境中的思想改造',
 '把已经学过、形成习惯的人，再放进一轮学习或训练；语气可中性，也可能带强制色彩。',
 're- 再、重新 + education 教育。education 来自拉丁语养育、训练词族，不能仅凭带出这个更远构词关系就宣称教育最初一定等于释放潜能。',ED+[['re- + education → reeducation','再一次教育、训练；具体语境也可指强制思想改造']],
 'a reeducation programme 再教育、再训练项目。政治历史中也会指强迫改变观念的安排，不能只看 re- 就当成普通自愿进修。',
 'a reeducation programme；political reeducation；a process of reeducation。',
 'reeducation 重新训练、教育；retraining 在职业技能更新中往往更直接。它们是否自愿、具体教什么，要看上下文。',
 ('The new system required a period of reeducation for experienced staff.','新系统要求有经验的员工也重新接受一段培训。'),('The historian examines the political language of reeducation.','历史研究者考察再教育这一说法的政治语言背景。'),sources=['https://en.wiktionary.org/wiki/reeducation#English','https://www.etymonline.com/word/educate'])
R('B3273','教育；教育相关；再教育','EDUCATION：学习、培养的过程，再看用途与重复','education 是过程、体系或培养经验；educational 说教育相关或能让人学到东西，reeducation 则再来一轮。',
 'education 接拉丁语 ēducātiō，来自 ēducāre 养育、训练。更远与引导词族相关，不等于所有现代含义都能逐字从带出来推导。',
 'education → educational；re- + education → reeducation。',
 [['过程与教育作用','education · educational'],['再次教育、训练','reeducation']],
 '教育词族的更远来源不能替代现代具体用法；reeducation 可能中性再训练，也可能带强制改造语境。',
 'The book discusses education as an ongoing process rather than a single event.\n\n书中把教育视为持续过程，而不是一次性事件。',
 'education educational reeducation')
W('educated','/ˈedʒəkeɪtɪd/；英式也 /ˈedjʊkeɪtɪd/','受过教育的；有知识根据的',
 '一个人接受过学习培养；一个猜测也可不是瞎蒙，而是有已有知识托着。',
 'educate + -ed，过去分词形容词化。an educated guess 进一步借受过训练、有知识的背景，表示有根据的推测。',ED+[['educate → educated','教育、培养 → 受过教育；有知识根据的']],
 'an educated reader 有一定知识背景的读者；an educated guess 有依据推测。受过教育不自动等于精通所有领域。',
 'highly educated；an educated guess；an educated opinion。',
 'educated guess 仍是推测，不是已证实事实；education 名词、educated 形容词不要混用。',
 ('She made an educated guess based on the earlier figures.','她根据先前数字作了一个有依据的推测。'),('The article is written for educated readers without specialist training.','文章面向有一定知识背景、但未受专业训练的读者。'))
W('educative','英 /ˈedʒʊkətɪv/；美 /ˈedʒəkeɪtɪv/','有教育作用的；能让人学到东西的',
 '一次经历、一种活动，不只是发生了，还让人从中明白点什么。',
 'educate 去 e + -ive，形成表示具有教育作用的形容词。与 educational 用法有重合，但常更强调活动本身能教给人东西。',ED+[['educate + -ive → educative','教育 → 有教育、启发作用的']],
 'an educative experience 有教育意义的经历；the educative role of museums 博物馆的教育作用，偏正式表达。',
 'an educative experience；an educative function；an educative role。',
 'educative 有教育作用，educated 已受教育；前者说能教什么，后者说学过或有知识根据。',
 ('The exhibition was entertaining as well as educative.','展览既有趣，也让人学到东西。'),('The report emphasizes the educative role of public libraries.','报告强调公共图书馆的教育作用。'))
R('B4472','教育、培养；受教育与教育作用','EDUCATE：使人学习、成长，结果与作用分开说','educate 说行动，education 说过程；educated 说受过培养，educative 说能起教育作用。',
 'educate 来自拉丁语 ēducātus，背后是 ēducāre 养育、训练；与更远的引导词族有关，但不能硬把每个音节当成现代英语独立词。',
 'educate → education、educated、educative；educational 与 educative 对照。',
 [['动作与过程','educate · education'],['学习结果与教育作用','educated · educative · educational']],
 'educated guess 是有依据推测，不是已证事实；educative experience 是让人学到东西的经历。',
 'An educative experience can help us make a more educated guess next time.\n\n一次让人学到东西的经历，可以帮助我们下次作出更有依据的推测。',
 'educate education educated educative educational')
AC=[['拉丁语 agere → āctus、āctīvus → 法语 actif','做、行动 → 行动、积极活动的'],['英语 active 及其后续构词','活跃、起作用；使启动；相应方式、人物与活动']]
W('actively','/ˈæktɪvli/','积极地；主动地；正在活跃地',
 '不是只挂着名字，而是实际投入、主动做。',
 'active + -ly，修饰参与、寻找、鼓励等动作；具体是积极主动还是持续进行，由动词决定。',AC+[['active → actively','活跃的 → 积极、主动地']],
 'actively participate 积极参与，actively seek a job 主动找工作；actively discourage 明确、主动地劝阻，动作本身未必是支持。',
 'actively involved；actively seek；actively encourage；actively discourage。',
 'actively 强调投入或主动，不保证结果一定成功；active 也不是所有地方都只译道德上的积极。',
 ('She actively participated in the workshop.','她积极参加了工作坊。'),('The museum is actively seeking old photographs of the town.','博物馆正积极寻找这座城的旧照片。'))
W('activate','/ˈæktɪveɪt/','激活；启动；使起作用',
 '东西已经在那里，现在让它从待着、未启用变成能工作。',
 'active 的词干 activ- + 动词后缀 -ate，表示使变得活跃、起作用。不是再往 act 后随意加一个 vate 词根。',AC+[['active + -ate → activate','活跃、起作用 → 使启动、使起作用']],
 'activate a device 启动设备，activate an account 激活账号。具体方式与条件看对象，单词本身只说明从未启用转到起作用。',
 'activate a device；activate a feature；activate an account。',
 'activate 让功能起作用，create 创建出东西；账号可能先被创建，之后才激活。',
 ('Pressing the button activates the recorder.','按下按钮会启动录音机。'),('She received an email asking her to activate the new account.','她收到一封要求激活新账号的邮件。'))
W('inactive','/ɪnˈæktɪv/','不活跃的；未启用的；不起作用的',
 '没有在行动、没有正在发挥作用，可能只是暂时停着。',
 'in- 不 + active 活跃、起作用的；否定的是活动状态，不自动等于永远损坏。',AC+[['in- + active → inactive','不活跃、未起作用的']],
 'an inactive account 不活跃或未启用的账号，an inactive member 不活跃成员；inactive ingredients 非活性成分是特定产品语境。',
 'remain inactive；an inactive account；an inactive member。',
 'inactive 不自动等于 broken 损坏；系统、协会怎样定义不活跃，要看具体规则。',
 ('The club reviewed its list of inactive members.','俱乐部核对了不活跃会员名单。'),('The old account has been inactive for several years.','旧账号已多年没有活动。'))
W('reactivate','/ˌriːˈæktɪveɪt/','重新激活；恢复启用',
 '以前动过、后来停了，现在再让它起作用。',
 're- 再、重新 + activate 启动；不是所有修理都叫 reactivate，核心是恢复活动或启用状态。',AC+[['activate → re- + activate → reactivate','启动 → 再次使起作用']],
 'reactivate an account 重新启用账号，reactivate a plan 重新启动计划；具体恢复了什么，要看对象。',
 'reactivate an account；reactivate a project；reactivate an old network。',
 'reactivate 重新启用，repair 修理；没有坏只是停用的东西，也能被 reactivate。',
 ('The library reactivated my old membership.','图书馆重新启用了我的旧会员资格。'),('The group plans to reactivate a project that was paused last year.','团队打算重新启动去年暂停的项目。'))
W('overactive','英 /ˌəʊvərˈæktɪv/；美 /ˌoʊvərˈæktɪv/','过分活跃的；活动过度的',
 '不是没动力，而是活动、反应多过了当前合适的程度。',
 'over- 过度 + active 活跃的；over 在这里说程度超出，不是空间在上面。',AC+[['over- + active → overactive','活跃 → 过于活跃的']],
 'an overactive imagination 过度活跃的想象，常说想得太多、把小事脑补成大问题。某些医学搭配也用它描述活动过度，但需要具体看对象。',
 'an overactive imagination；an overactive mind；an overactive system。',
 'overactive 不只是 very active 很活跃，over- 常包含过头、不合适的评价。',
 ('My overactive imagination turned every small noise into a mystery.','我过分活跃的想象把每个小声响都脑补成了谜团。'),('The editor said the story suffered from an overactive plot with too many twists.','编辑说故事情节翻转太多，显得过分忙乱。'))
W('activewear','英 /ˈæktɪvweə/；美 /ˈæktɪvwer/','运动休闲服装；适合运动的服装类别',
 '为活动、锻炼而设计，也常被穿进日常生活的那类衣服。',
 'active 活动、运动相关 + wear 穿戴物，形成服装类别名词，通常不可数。',C('active 运动、活动相关','wear 穿戴物','activewear','运动、活动用途的服装类别'),
 'an activewear brand 运动休闲服品牌，an activewear collection 运动服装系列。不等于穿上就自动具有某种专业防护能力。',
 'an activewear collection；an activewear retailer；comfortable activewear。',
 'activewear 是衣物类别，activity 是活动；sporting equipment 是运动器材，范围又不同。',
 ('The shop added a range of comfortable activewear.','商店新增了一系列舒适运动休闲服。'),('She designs activewear that people can also wear on ordinary days.','她设计也适合日常穿着的运动休闲服。'))
W('activist','/ˈæktɪvɪst/','行动倡议者；积极推动社会等议题的人',
 '不只持有一个看法，还通过组织、倡议等行动试着推动改变。',
 'active 的词干 activ- + -ist 人物、主张者后缀，形成积极行动倡议者的称呼。',AC+[['active + -ist → activist','积极行动 → 推动议题、改变的人']],
 'an environmental activist 环保行动者，a community activist 社区活动人士。立场、目标和方法要另看具体人，词本身不保证全都激进或相同。',
 'a community activist；a human rights activist；an environmental activist。',
 'activist 是采取行动推动议题的人，active member 只是活跃成员；participant 参与者不一定有倡议、改变的角色。',
 ('Local activists campaigned to save the public library.','当地行动倡议者发起了保留公共图书馆的活动。'),('The documentary follows a community activist working on housing issues.','纪录片跟拍了一位推动住房议题的社区活动人士。'))
W('activism','/ˈæktɪvɪzəm/','行动主义；社会议题中的积极行动、倡议',
 '把推动改变从想法变成持续的行动，这是一个活动或方式的名称。',
 'active 的词干 activ- + -ism，形成行动方式、主张的抽象名词；与 activist 是同一现代词族的不同名词。',AC+[['active + -ism → activism','积极行动 → 以行动推动改变的活动、方式']],
 'student activism 学生社会行动，community activism 社区倡议行动。可能包括组织、宣传、抗议等多种活动，不能只等同某一种方法。',
 'community activism；political activism；environmental activism。',
 'activism 是活动、方式，activist 是人；表达反对意见不自动说明采取了哪一种 activism。',
 ('The exhibition traces a century of community activism.','展览追溯了一个世纪的社区行动历史。'),('She studies how online communication has changed environmental activism.','她研究网络通信如何改变环保倡议行动。'))
R('B3573','活跃；起作用；启动；采取行动','ACTIVE：真的在行动，或者让东西开始起作用','先区别状态 active、方式 actively、启动 activate，再看否定、再次启用与社会倡议这几支。',
 'active 经法语来自拉丁语 āctīvus，与 agere 做、行动的词族有关。英语后续用 -ate、-ist、-ism 等继续构词。',
 'active → actively、activity；activate → activation；inactive → inactivity；reactivate → reactivation；overactive、hyperactive；activist ↔ activism；activewear 另看衣物类别。',
 [['状态、方式与活动','active · actively · activity'],['启动、停用、恢复与程度','activate · activation · inactive · inactivity · reactivate · reactivation · overactive · hyperactive'],['倡议行动与服装名称','activist · activism · activewear'],['其他常用历史词族组合','interactive · proactive · retroactive · radioactive · psychoactive · bioactive']],
 'inactive 未活动不一定损坏；activist 人，activism 行动方式；activewear 是服装类别。',
 'The active members decided to reactivate the project and participate more actively.\n\n活跃成员决定重新启动项目，更积极地参与。',
 'active actively activity activate activation inactive inactivity reactivate reactivation overactive hyperactive activist activism activewear interactive proactive retroactive radioactive psychoactive bioactive')
WO=[['古英语 wīfmann：wīf + mann','女性 + 人；这里的 wīf 不只等于现代妻子'],['中古英语 wifman / wimman / womman → woman','女性；现代通常指成年女性']]
W('woman','/ˈwʊmən/；复数 women /ˈwɪmɪn/','成年女性；女人',
 '这个老复合词原来是女性的人，不是把女性定义成某人的妻子。',
 '古英语 wīfmann 由 wīf 女性与 mann 人组成，后来经过语音、拼写变化形成 woman。不是 womb 子宫 + man；woman、women 首个元音也不同。',WO,
 'a woman doctor 一位女医生；women’s voices 女性的声音。作职业前置修饰语时，woman doctor 的复数常为 women doctors；一般直接用职业名词即可，不必处处加性别。',
 'a young woman；women’s history；women and men；women’s voices。',
 'woman 单数 /ʊ/，women 复数 /ɪ/；girl 通常说女孩，adult woman 是成年女性，不把所有女性都称 girl。',
 ('A woman at the desk helped us find the room.','服务台的一位女士帮我们找到了房间。'),('The exhibition explores women’s lives in the nineteenth century.','展览考察19世纪女性的生活。'),sources=['https://en.wiktionary.org/wiki/woman#English','https://www.etymonline.com/word/woman'])
W('womanhood','/ˈwʊmənhʊd/','成年女性阶段；女性身份、共同经历',
 '把作为成年女性的阶段、身份或相关生活经验放在一起谈。',
 'woman + -hood，后缀表示阶段、身份、状态；不是头发 hood，也不与衣帽的 hood 义直接相加。',WO+[['woman + -hood → womanhood','女性 → 成年女性阶段、女性身份']],
 'enter womanhood 进入成年女性阶段；experiences of womanhood 女性身份相关经历。文学、社会讨论中会按具体观点使用，不能假设所有人的经历一样。',
 'enter womanhood；the experience of womanhood；ideas about womanhood。',
 'girlhood 女孩童年，womanhood 成年女性阶段或身份，motherhood 母亲身份；三者不能当成完全相同的词。',
 ('The memoir follows her journey from girlhood into womanhood.','回忆录讲述她从女孩成长为成年女性的历程。'),('The essay explores changing ideas about womanhood.','文章探讨女性身份观念的变化。'))
W('womanly','/ˈwʊmənli/','有成年女性气质的；传统描述中的女性化的',
 '说话人觉得某种外貌、气度或品质带成年女性的气质；这包含文化评价。',
 'woman + -ly，在这里构成形容词，不是所有 -ly 都是副词。现代意义与相应文化对女性气质的理解有关。',WO+[['woman + -ly → womanly','女性 → 被认为有成年女性气质的']],
 'a womanly presence 有成年女性气质的仪态；文学中常见。不同作者、时代想强调的品质不同，不能把它当成所有女性的生物学标准。',
 'a womanly figure；womanly grace；a womanly presence。',
 'womanly 常带传统气质评价，female 在许多分类描述中更中性；womanhood 是身份、阶段名词。',
 ('The novel gives her a confident, womanly presence.','小说赋予她一种自信、富有成年女性气质的仪态。'),('She disliked the advertisement’s narrow idea of what counted as womanly.','她不喜欢广告对女性气质的狭窄定义。'))
W('spokeswoman','英 /ˈspəʊkswʊmən/；美 /ˈspoʊkswʊmən/','女发言人',
 '代表某个组织说话的人，词尾 woman 明确说她是女性。',
 '与 spokesman 的构形对应，把 man 换成 woman；spokes- 属于 speak 的旧分词、连接成分构形背景，不是车轮辐条 spoke 的现代拼接。',WO+[['spokesman 的构形对应 spokes- + woman → spokeswoman','代表发言的角色名称，词尾标出女性']],
 'a company spokeswoman 公司女发言人；若性别无关，也常用 spokesperson 发言人。复数 spokeswomen，词尾 women 仍读 /ˈwɪmɪn/。',
 'a company spokeswoman；a government spokeswoman；a spokeswoman said...。',
 'spokeswoman 代表组织或团体发言，不等于所有在公开场合讲话的女性；speaker 范围更广。',
 ('A spokeswoman for the museum confirmed the opening date.','博物馆一位女发言人确认了开放日期。'),('The company’s spokeswoman answered questions after the announcement.','公司女发言人在消息宣布后回答了问题。'))
R('B2585','女性；成年阶段、气质与代表角色','WOMAN：旧女性 + 人，现代义与气质评价分开','先掌握 woman、women 的读音，再看 -hood 阶段身份、-ly 气质描述、spokes- 代表发言的关系。',
 'woman 来自古英语 wīfmann，wīf 的旧义是女性，mann 是人；不是 womb + man，也不把现代 wife 妻子义直接套回去。',
 'woman → women；womanhood、womanly；spokes- + woman → spokeswoman；superwoman 看已经讲过的比喻和专名用法。',
 [['女性与成年身份、气质','woman · womanhood · womanly'],['代表角色与固定称呼','spokeswoman · superwoman']],
 'woman /ˈwʊmən/，women /ˈwɪmɪn/；spokeswoman 是代表角色；womanly 带文化上的气质评价。',
 'The spokeswoman introduced an exhibition about women’s lives and ideas of womanhood.\n\n女发言人介绍了一场有关女性生活与女性身份观念的展览。',
 'woman womanhood womanly spokeswoman superwoman')
BE=[['拉丁语 bellus → 通俗拉丁语 *bellitās、古法语 beauté 等形式','好看、悦目 → 美这一性质'],['中古英语 bewte / beaute → 英语 beauty','美；美的事物、人；还有优点的比喻用法']]
W('beauty','/ˈbjuːti/','美；美感；美的人或事物；妙处',
 '看、听、理解时觉得有吸引力、协调或动人；不只用于人的外貌。',
 '经古法语 beauté 等形式来自拉丁语 bellus 好看的词族，中古英语有 bewte 等拼写。现代 beauty 不能拆成 beau + ty 当两个独立英语词。',BE,
 'natural beauty 自然之美，the beauty of music 音乐之美；the beauty of the plan 方案的妙处。a beauty 可称一个美人或漂亮、出色的物件。',
 'natural beauty；the beauty of；beauty products；a thing of beauty。',
 'beauty 常是性质、不可数；a beauty 则指具体漂亮的人或东西。并不是所有 beauty 都只等于化妆、美容。',
 ('The path gives visitors a chance to enjoy the beauty of the forest.','小路让游客有机会欣赏森林之美。'),('The beauty of this plan is that it needs no extra equipment.','这个方案的妙处在于不需要额外设备。'),sources=['https://en.wiktionary.org/wiki/beauty#English','https://www.etymonline.com/word/beauty'])
W('beautiful','/ˈbjuːtɪfəl/','美丽的；优美的；出色、令人愉悦的',
 '事物有美感，或完成得很出色、让人满意，不只指外表漂亮。',
 'beauty + -ful，y 变 i；-ful 形成具有美这种性质的形容词，现代拼写只有一个结尾 l。',BE+[['beauty + -ful → beautiful','美 → 具有美感、出色的']],
 'a beautiful landscape 美丽风景，a beautiful voice 优美嗓音，a beautiful solution 漂亮、巧妙的解决办法。',
 'a beautiful view；a beautiful voice；a beautiful performance；a beautiful solution。',
 'beautiful 比 pretty 更容易涵盖广阔、壮丽、深层美感，但两者范围可重叠；不是靠词长评定美的客观等级。',
 ('The room has a beautiful view of the mountains.','房间能看到美丽山景。'),('She found a beautiful solution to a difficult design problem.','她为棘手的设计问题找到了一个漂亮的解决办法。'))
W('beautifully','/ˈbjuːtɪfəli/，也常 /ˈbjuːtɪfli/','优美地；漂亮地；出色地',
 '做这件事的方式、最终呈现的状态很美，或配合得恰到好处。',
 'beautiful + -ly，形容词变副词；实际口语中中间弱音节常简化。',BE+[['beautiful → beautifully','优美、出色 → 优美地、出色地']],
 'sing beautifully 唱得优美，beautifully designed 设计精美；work beautifully 运作得极好，也可能没有视觉美。',
 'beautifully written；beautifully designed；sing beautifully；work beautifully。',
 'looks beautiful 看起来美，works beautifully 运作出色；修饰动词方式用副词，不必都按外观解释。',
 ('The old table has been beautifully restored.','旧桌子修复得很漂亮。'),('The two parts fit together beautifully.','这两个部件配合得非常好。'))
W('beautify','/ˈbjuːtɪfaɪ/','美化；使变美',
 '采取行动改变外观，让一个地方或物件看起来更好。',
 'beauty 的词干 beaut- + -ify 使变得，构成美化动词；不是 beautiful 的过去式。',BE+[['beauty + -ify → beautify','美 → 使变美']],
 'beautify a neighbourhood 美化街区；beautify the garden 美化花园。说改变的目标，不自动证明改造真的改善了所有人的生活。',
 'beautify the town；beautify a public space；a plan to beautify。',
 'beautify 强调使外观更美；repair 修好、clean 清洁可以是其中手段，却不与它完全同义。',
 ('Residents planted flowers to beautify the street.','居民种花美化街道。'),('The project aims to beautify the square without changing its historic character.','项目旨在美化广场，同时保留它的历史风貌。'))
W('beautification','/ˌbjuːtɪfɪˈkeɪʃən/','美化；美化工程、过程',
 '把美化这个动作当成一项计划、过程或工作来谈。',
 'beautify 对应的 -ification 名词形式；-ify → -ification 是常见动词转活动名词关系，不要把 fication 单独硬记成万能词根。',BE+[['beautify → beautification','使变美 → 美化过程、项目']],
 'a city beautification project 城市美化项目；street beautification 街道美化。通常在规划、公共空间或外观改造讨论中出现。',
 'a beautification project；urban beautification；a beautification programme。',
 'beautification 是过程、项目，beauty 是美这种性质或具体美的事物；实施项目不代表每项变化都获得一致好评。',
 ('The council announced a beautification project for the old square.','地方议会宣布了一项老广场美化工程。'),('The report weighs the costs and benefits of urban beautification.','报告权衡城市美化的成本与收益。'))
R('B3526','美；优美；使变美与美化过程','BEAUTY：先有美感，再分性质、方式和改变','beauty 是美，beautiful 形容事物，beautifully 说方式；beautify 主动改变，beautification 说过程。',
 'beauty 经法语来自拉丁语 bellus 好看词族。后续 -ful、-ly、-ify、-ification 把词性与表达重点分别改变。',
 'beauty → beautiful → beautifully；beauty → beautify → beautification。',
 [['美感、性质与方式','beauty · beautiful · beautifully'],['美化动作与过程','beautify · beautification']],
 'beauty of the plan 可说方案的妙处；beautiful solution 巧妙方案；beautification 是美化过程。',
 'The beautification project made the square more beautiful, but its real beauty lay in its welcoming atmosphere.\n\n美化工程让广场更漂亮，而它真正的魅力在于亲切宜人的氛围。',
 'beauty beautiful beautifully beautify beautification')
for item in WORDS:
 if item['word']=='educative':
  item['ipa']='英 /ˈedʒukətɪv/；美 /ˈedʒəkeɪtɪv/'
  item['sources'].append('https://dictionary.cambridge.org/pronunciation/english/educative')
 if item['word']=='educated':item['ipa']='常见 /ˈedʒəkeɪtɪd/；英式也 /ˈedjuːkeɪtɪd/'
 if item['word']=='overactive':
  revised_examples=list(item['examples'])
  revised_examples[1]=('His overactive mind kept inventing problems that never happened.','他过分活跃的头脑总在设想那些从未发生的问题。')
  item['examples']=revised_examples
if __name__ == '__main__':save('continuation_20261029_cf',ROOTS,WORDS)
