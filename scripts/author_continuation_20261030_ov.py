"""Usability, direction, intuition, exclusion, cuffs, theatre, cyber and sleepiness."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()

Us=[['英语 use + -able → usable','可以使用、适于使用的'],['un- + usable → unusable','不能用；不适合使用']]
W('unusable','/ʌnˈjuːzəbəl/','不能使用的；不适用的',
 '文件打不开、椅子断了腿、数据乱到无法利用，都可能是 unusable：拿到了也没法按需要用起来。',
 'un- 否定 + usable 可使用的；usable 对应 use 去末尾 e 加 -able。un- 否定整个性质，不是动作“把使用撤销”。',Us,
 'an unusable file 无法使用的文件；an unusable room 无法正常使用的房间；render something unusable 使某物无法使用。',
 'an unusable file；render something unusable。',
 'unusable 不能用，unused 没被用；全新的备用文件可能 unused，却完全 usable。',
 ('The damaged file was unusable.','损坏的文件无法使用了。'),('Heavy rain left the outdoor stage unusable.','大雨使室外舞台无法使用。'))
R('B4408','能否用起来，与使用起来是否顺手','USABLE：拿到手，能不能真正用上','usable → usability；unusable 否定可用性。',
 'usable 先过能用这一关，usability 再谈使用的方便程度。不能用与还没用，是两个问题。',
 'use + -able 去末尾 e → usable；usable + -ity 对应 usability，-able 改为 -ability；un- 否定。',
 [['可用、好用与不能用','usable · usability · unusable']],
 'usable 不保证使用体验出色；unusable 不是 unused；usability 也不是系统运行时间指标 availability 的通用替代。',
 'The old file is usable, but the interface has poor usability.\n\n旧文件还能用，但界面使用起来不方便。','usable usability unusable')
R('B4370','朝外方向与外在表现，由空间走向观察层面','OUTWARD：往外看，或只看外表那一层','outward → outwardly；outwards 是朝外的副词形式。',
 '门向外开是空间方向，一个人外表冷静是观察层面。外表没有露出来，并不等于心里完全没有变化。',
 'out + -ward 方向材料，接古英语相关形式；outward + -ly 成副词，outwards 接副词 -s。',
 [['朝外、外在表现','outward · outwardly · outwards']],
 'outwardly calm 只说表面冷静；outwards 是朝外，不能替换成 outwardly calm 的那个方式副词。',
 'Outwardly calm, she pushed the door outwards.\n\n她表面镇定，把门向外推开。','outward outwardly outwards')

In=[['拉丁 in- 朝向 + tueri 看 → intueri','注视、考虑'],['中世纪拉丁 intuitivus；法语 intuitif 等 → intuitive','直观把握的；凭直觉的'],['intuitive + -ly → intuitively','凭直觉、直观地']]
W('intuitive','英 /ɪnˈtjuːɪtɪv/；美 /ɪnˈtuːɪtɪv/','凭直觉的；直观易懂的',
 '还没把推理一步步说出来，已经大致抓到了答案；界面一看就知道怎么操作，也可以说 intuitive。',
 '借法语 intuitif 等，上接中世纪拉丁 intuitivus、拉丁 intueri 注视、考虑；in- 在这里是朝向，tueri 是看，不是否定前缀。',In,
 'an intuitive understanding 直觉式理解；an intuitive interface 易懂易用的界面；an intuitive sense 直觉判断。感觉可来自经验，也可能判断错误。',
 'intuitive understanding；an intuitive interface；an intuitive sense of。',
 'intuitive 容易凭直觉把握，counterintuitive 与直觉预期相反；后者不自动等于错误，前者也不保证正确。',
 ('The app has an intuitive interface that new users can understand quickly.','这个应用的界面直观，新用户很快就能看懂。'),('Years of practice gave her an intuitive sense of timing.','多年练习让她对时机形成了直觉。'),sources=['https://en.wiktionary.org/wiki/intuitive#English','https://www.oxfordlearnersdictionaries.com/definition/english/intuitive'])
W('intuitively','英 /ɪnˈtjuːɪtɪvli/；美 /ɪnˈtuːɪtɪvli/','凭直觉地；直观上',
 '你可能还没写出证明，但心里先觉得应该这样。intuitively 交代的是判断方式，不给结论盖正确印章。',
 'intuitive + -ly → intuitively，保留末尾 e 再接 -ly；副词用于理解、感觉、使用等动作或整句判断。',In,
 'intuitively understand 凭直觉理解；intuitively obvious 直观上显而易见；Intuitively, ... 从直觉上说……。',
 'intuitively understand；intuitively obvious；intuitively appealing。',
 'intuitively 并不必然是天生就会；长期训练形成的熟练模式也能让判断看起来不经刻意思考。',
 ('She intuitively understood what the child was trying to say.','她凭直觉明白了孩子想表达什么。'),('The result seems intuitively obvious, but it still needs a proof.','结果直观上似乎显然，但仍需要证明。'))
R('B3193','不经逐步刻意思考就抓到，或设计得容易直接理解','INTUITIVE：还没讲完步骤，脑中已经抓到意思','intuitive → intuitively；counterintuitive 是与这种直接预期相反。',
 '经验可以把复杂判断练成直觉，清楚的界面也可让操作顺着人的预期走。词源的看，帮助连接直接把握，不能据此把直觉当眼见事实。',
 'in- 朝向 + tueri 看 → intueri、intuitivus → intuitive；-ly 方式；counter- 相反。',
 [['直观性质与判断方式','intuitive · intuitively'],['违背直觉预期','counterintuitive']],
 'intuitive 不保证正确，counterintuitive 不表示必然错误；直观易用也不是无需任何学习。',
 'The counterintuitive result challenged what we intuitively expected.\n\n这个违反直觉的结果，挑战了我们直觉上的预期。','intuitive intuitively counterintuitive')

Ex=[['拉丁 excludere、exclusio → exclusion','把……关在外面；排除'],['exclusion + -ary → exclusionary','具有排除作用、性质的']]
W('exclusionary','英 /ɪkˈskluːʒənri/；美 /ɪkˈskluːʒəneri/','排斥性的；把某些人、事物排除在外的',
 '规则表面开着门，条件却让某群人进不来，便可以说是 exclusionary。重点在产生排除的机制、性质。',
 'exclusion + -ary → exclusionary；exclusion 追到拉丁 ex- 在外 + claudere 关闭的排除材料，不拆成现代 exclude 直接加 -ary。',Ex,
 'exclusionary rules 排除性规则；exclusionary practices 排斥性做法；正式语境常用于参与资格、群体边界等。专门法律词组另按所处体系理解。',
 'exclusionary practices；exclusionary rules；an exclusionary policy。',
 'exclusion 是排除这个行为、结果，exclusionary 修饰造成排除的性质；exclusive 还可指独家、高档专属，不能处处替换。',
 ('The club changed rules that had been criticised as exclusionary.','俱乐部修改了被批评具有排斥性的规则。'),('The study examines exclusionary practices in recruitment.','研究考察招聘中的排斥性做法。'),sources=['https://en.wiktionary.org/wiki/exclusionary#English','https://www.oxfordlearnersdictionaries.com/definition/english/exclusionary'])
R('B4388','关在外面，从排除行为到排除性质','EXCLUSION：把某人、某物挡在范围之外','exclusion → exclusionary。',
 '一个是排除这件事，一个是规则、做法具有这种效果。学习时用资格门槛的画面理解，再按语境判断具体对象。',
 '拉丁 excludere、exclusio 等 → exclusion；exclusion + -ary 成形容词。',
 [['排除及其性质','exclusion · exclusionary']],
 'exclusion 与 exclusionary 词性不同；exclusive 的独家、高档义不随意套进 exclusionary。',
 'The report links social exclusion to exclusionary practices.\n\n报告把社会排斥与具有排斥性的做法联系起来。','exclusion exclusionary')

Cu=[['中古英语 cuffe、coffe','手套、连指手套；远源未定'],['英语 cuff 袖口 → handcuff、缩短 cuff','袖口、腕部圈套；给人戴手铐'],['另源 cuff 打、拍','可能接北欧语推、打材料，不与袖口强并']]
W('cuff','/kʌf/','袖口；裤脚翻边；手铐、铐住〔缩略〕；拍打',
 '衬衫包住手腕的那一圈是 cuff；衣物词走向腕部圈套，再能与手铐联系。拍打一巴掌的 cuff 则是另一条来源。',
 '衣物义接中古英语 cuffe 手套等，远源未定。手铐义可由 handcuff 缩短；打、拍义可能接北欧语言的推击材料，不能硬讲成拿袖口打人。',Cu,
 'shirt cuffs 衬衫袖口；trouser cuffs 裤脚翻边；off the cuff 即兴地、未准备地；cuff someone 铐住或拍打，要看语境。',
 'shirt cuffs；off the cuff；a cuff on the ear。',
 'off the cuff 的即兴表达常联系袖口便记的画面，但不要把这种解释升级成所有场合都真正写了袖口小抄。',
 ('He rolled back the cuffs of his shirt.','他把衬衫袖口翻了上去。'),('She answered the question off the cuff.','她即兴回答了这个问题。'),sources=['https://en.wiktionary.org/wiki/cuff#English','https://www.etymonline.com/word/cuff'])
R('B4202','袖口与腕部约束，和同形拍打词分开理解','CUFF：围住手腕的一圈；拍打另有来源','cuff → handcuff、handcuffs；词形缩短后 cuff 也可说铐住。',
 '袖口与手铐都围着腕部，构词关系可以直观理解；但同形的打击义不能靠这个画面编成历史。',
 '中古英语 cuffe 等衣物名 → cuff；hand + cuff → handcuff；常用复数 handcuffs。拍打 cuff 有不同的可能北欧来源。',
 [['袖口、腕部圈套与手铐','cuff · handcuff · handcuffs']],
 'off the cuff 是即兴，不是脱下手铐；cuff 的拍打义与衣物义不强并同源。',
 'The dictionary distinguishes shirt cuffs from handcuffs.\n\n词典把衬衫袖口与手铐区分开。','cuff handcuff handcuffs')
R('B4133','舞台相关，或像表演一样夸张外露','THEATRICAL：像站在台上，把动作和情绪放大','theatrical → theatrically、theatricality。',
 '舞台需要让后排也看清、听清；日常用 theatrical，可能就说动作像在演一场戏。要从语境分中性舞台关联与夸张评价。',
 'theatre 的戏剧材料接 -ical 等历史形式 → theatrical；-ly 方式；-ity 性质。',
 [['舞台性质、方式与表现感','theatrical · theatrically · theatricality']],
 'theatrical equipment 是戏剧设备，不是在批评设备做作；theatrical gesture 才常有夸张表现的意味。',
 'Her theatrical gesture was delivered theatrically, adding to the scene’s theatricality.\n\n她用舞台化的方式做出夸张动作，增强了场面的戏剧感。','theatrical theatrically theatricality')

Cy=[['希腊 kybernetes 舵手、掌舵者 → cybernetics','控制、通信相关学科名称'],['cybernetics 等缩取 cyber-','逐渐广用于计算机、网络、虚拟空间'],['cyber- + punk／crime','赛博朋克；网络犯罪']]
W('cyberpunk','英 /ˈsaɪbəpʌŋk/；美 /ˈsaɪbɚˌpʌŋk/','赛博朋克；相关创作、人物',
 '技术已经非常发达，城市生活却可能混乱、贫富悬殊，人物在系统夹缝里生存，这类科幻常有 cyberpunk 的气质。不是加上霓虹灯就够了。',
 'cyber- 计算机、控制技术相关 + punk 反叛人物、文化材料。Bruce Bethke 于 1983 年发表同名短篇，此名后来成为流派称呼。',Cy,
 'cyberpunk fiction 赛博朋克小说；a cyberpunk setting 赛博朋克背景；cyberpunk aesthetics 赛博朋克美学。常结合高科技与社会失序、权力压迫等主题。',
 'cyberpunk fiction；a cyberpunk setting；cyberpunk aesthetics。',
 'cyberpunk 是流派、风格相关名，cybercrime 是借网络实施犯罪；喜欢此类小说不等于参与犯罪。',
 ('The novel combines cyberpunk themes with a detective story.','这部小说把赛博朋克主题与侦探故事结合起来。'),('The game is set in a crowded cyberpunk city.','游戏背景是一座拥挤的赛博朋克城市。'))
W('cybercrime','英 /ˈsaɪbəkraɪm/；美 /ˈsaɪbɚkraɪm/','网络犯罪',
 '电脑、网络成为作案工具或攻击目标，像窃取账户资料这类行为，常落在 cybercrime 的讨论范围。',
 'cyber- 网络、计算机相关 + crime 犯罪 → cybercrime。cyber- 从控制、通信词族缩取后扩展，不是原始希腊语就表示互联网。',Cy,
 'combat cybercrime 打击网络犯罪；cybercrime investigations 网络犯罪调查；可说整体类型，也可数某次此类犯罪。',
 'combat cybercrime；cybercrime investigations；a rise in cybercrime。',
 'cybercrime 涉及犯罪，不是所有网络争吵、系统故障都自动算；具体法律分类随适用制度判断。',
 ('The report describes a rise in cybercrime targeting small businesses.','报告描述了针对小企业的网络犯罪增多。'),('The course introduces basic terms used in cybercrime investigations.','课程介绍网络犯罪调查中的基本术语。'))
R('A1731','从掌舵、控制材料走向计算机和网络领域','CYBER-：今天多指网络，远源却是掌舵','cyberpunk、cyberspace 看技术文化与空间；cybersecurity、cybercrime 等看风险与活动。',
 '掌舵画面帮助理解控制、通信学科名 cybernetics 的远源。现代 cyber- 已扩为网络相关，不能逐词死译成船舵。',
 '希腊 kybernetes 舵手等 → cybernetics；缩取 cyber- 再构词。后半决定空间、安全、犯罪、文化、活动等类别。',
 [['技术空间与文化','cyberspace · cyberpunk'],['安全、攻击与犯罪','cybersecurity · cyberattack · cybercrime · cyberbullying'],['其他网络活动语境','cyberwarfare · cybersex']],
 'cyber- 不等于每个词都涉及违法；cyberpunk 流派也不是单纯一切霓虹灯装饰。',
 'The article contrasts cyberpunk fiction with real issues of cybersecurity and cybercrime.\n\n文章把赛博朋克小说与现实中的网络安全、网络犯罪问题作了对照。','cyberspace cyberpunk cybersecurity cyberattack cybercrime cyberbullying cyberwarfare cybersex')

Sl=[['sleep + -y；历史相应 sleepy 形式','带睡意的；令人觉得安静无活力的'],['sleepy 改 y 为 i 接 -ly／-ness','困倦地；困倦这种状态']]
W('sleepily','/ˈsliːpɪli/','困倦地；带着睡意地',
 '眼睛还没睁开就含糊应一声，声音和动作都带睡意，就是 sleepily。',
 'sleepy + -ly，y 改 i → sleepily；不是 sleep + ily 的独立新后缀。',Sl,
 'murmur sleepily 困倦地低声说；blink sleepily 睡眼惺忪地眨眼；answer sleepily 带睡意地回答。',
 'blink sleepily；answer sleepily；yawn sleepily。',
 'sleepily 困得想睡，sleeping 是正在睡；人能 sleepily answer，通常还没完全睡着。',
 ('He blinked sleepily at the bright window.','他睡眼惺忪地望着明亮的窗户。'),('She answered sleepily and pulled the blanket closer.','她带着睡意应了一声，把毯子拉近了些。'))
W('sleepiness','/ˈsliːpinəs/','困倦；睡意',
 '不是睡了多少小时，而是现在有多想睡。sleepiness 把这种眼皮发沉的感觉当作一个状态来谈。',
 'sleepy + -ness，y 改 i → sleepiness；-ness 构成性质、状态名词。',Sl,
 'daytime sleepiness 白天困倦；a wave of sleepiness 一阵睡意；sleepiness after lunch 午饭后的困意。',
 'daytime sleepiness；a wave of sleepiness。',
 'sleepiness 是想睡的感觉，sleeplessness 是睡不着或缺少睡眠的状态；拼写只差一点，方向不同。',
 ('A wave of sleepiness came over him after lunch.','午饭后，他涌上一阵睡意。'),('The diary records periods of daytime sleepiness.','日记记录了白天出现困意的时段。'))
R('B3536','想睡的性质、带睡意的方式与困倦状态','SLEEPY：眼皮开始沉，动作也慢下来','sleepy → sleepily、sleepiness。',
 'sleepy 形容人困，sleepily 形容怎样说、怎样动，sleepiness 是睡意本身。安静小镇的 sleepy 比喻也由缺少活力、节奏缓慢理解。',
 'sleep + -y；sleepy 改 y 为 i 接 -ly、-ness。',
 [['困倦性质、方式与状态','sleepy · sleepily · sleepiness']],
 'sleepiness 不是睡眠时长；sleepiness 与 sleeplessness 分别是困意、缺少睡眠或失眠状态。',
 'Feeling sleepy, she answered sleepily and wrote down her level of sleepiness.\n\n她感到困倦，带着睡意应答，并记下困意的程度。','sleepy sleepily sleepiness')

if __name__=='__main__':save('continuation_20261030_ov',ROOTS,WORDS)
