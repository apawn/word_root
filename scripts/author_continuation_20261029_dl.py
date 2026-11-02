"""Develop, hate and answer: common bases and close extensions."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
D=[['古法语 desveloper → 法语 développer','解开包裹、展开；更远的包裹词来源不确定'],['英语 develop','逐渐形成、把潜能展开 → 发展、开发、产生等']]
W('develop','/dɪˈveləp/','发展；开发；逐渐形成、产生；显影',
 '原来还没成形的东西，逐渐展开、变得明显；因此既能发展技能，也能养成习惯、出现问题。',
 '借法语 développer，旧有展开、解包的意义。前半有解除的历史成分，后半包裹词更远来源不定，不硬编拉丁 de + velum 面纱。抽象形成、发展等义逐渐成为现代重点。',D,
 'develop a skill 培养技能，develop software 开发软件，develop a habit 养成习惯；develop a problem 逐渐出现问题，develop film 冲洗显影胶片。',
 'develop a skill；develop a habit；develop software；develop a problem。',
 'develop 不总是 improve 改善：a problem developed 是问题出现，未必变好；grow 常强调生长、增大，develop 还强调成形、复杂化。',
 ('The team is developing a new booking system.','团队正在开发一套新预订系统。'),('A small problem developed during the test.','测试期间渐渐出现了一个小问题。'),sources=['https://en.wiktionary.org/wiki/develop#English','https://www.etymonline.com/word/develop'])
W('developer','英 /dɪˈveləpə/；美 /dɪˈveləpər/','开发者；地产开发商；显影剂',
 '把软件、地块等做成可用成果的人或公司；摄影里能让潜在影像显出来的药剂也叫 developer。',
 'develop + -er，按不同 develop 义形成执行者、作用物。-er 可以是机构或化学用品，不只一个人。',D+[['develop + -er → developer','开发、显影 → 开发者、开发商、显影剂']],
 'a software developer 软件开发者，a property developer 地产开发商，photographic developer 显影剂。',
 'a software developer；a property developer；a web developer。',
 'developer 具体职业由 software、property 等限定；不是每位开发者都写代码，也不是所有 developer 都是人物。',
 ('The developer fixed the bug before the release.','开发者在发布前修复了漏洞。'),('The property developer presented plans for the site.','地产开发商提交了这块地的开发方案。'))
W('developed','/dɪˈveləpt/','已开发的；发展成熟的；发达的',
 '已经经过形成、完善的过程，到达某种较充分状态；究竟哪方面充分，最好说清楚。',
 'develop + -ed，末尾 /t/，不是单独一个 /ɪd/ 音节。过去分词、形容词都可见，现代常取技能、系统、经济等发展程度。',D+[['develop + -ed → developed','发展、开发 → 已发展、较成熟的']],
 'well-developed skills 充分发展的技能，a developed economy 发达经济体；a developed photograph 是已显影的照片。',
 'a developed economy；fully developed；well-developed skills。',
 'developed 已发展、形成，developing 正在发展；a developed plan 成形方案不是说明一定已经执行。',
 ('She has highly developed observational skills.','她的观察能力已相当成熟。'),('The idea was not yet fully developed.','这个想法尚未完全成形。'))
W('developing','/dɪˈveləpɪŋ/','正在发展、形成的；发展中的',
 '过程还在展开，新的能力、情况或结构正在成形；重点是目前处在变化中。',
 'develop + -ing，现代动作形式与形容词；developing economies 是固定经济描述之一，其他语境还可说正在出现的趋势、技能。',D+[['develop + -ing → developing','发展、形成 → 正在发展、形成中的']],
 'a developing situation 正在变化的局势，developing skills 正在形成的技能，developing economies 发展中经济体。',
 'a developing situation；a developing trend；developing skills。',
 'developing 正在发展，不等于 developer 开发者；The developer is developing a tool 是开发者正在开发工具。',
 ('We are watching a rapidly developing situation.','我们正密切关注迅速变化的局势。'),('The programme supports children’s developing language skills.','项目帮助儿童发展中的语言能力。'))
W('undeveloped','/ˌʌndɪˈveləpt/','尚未开发的；未充分展开、形成的',
 '地块还没有建起来，想法也还没展开成细节；重点是这一步没有发生或完成。',
 'un- 未、不 + developed，否定已开发、已成形状态。与 under- 不充分不同，不把两个前缀看成同一个。',D+[['un- + developed → undeveloped','已开发、成形 → 尚未开发、未展开']],
 'undeveloped land 未开发土地，an undeveloped idea 未展开的想法；看具体对象，不一定是在说品质差。',
 'undeveloped land；an undeveloped idea；undeveloped potential。',
 'undeveloped 尚未开发，underdeveloped 发展不充分；同一片地可能完全未建，也可能已有部分建设但不充分，表达焦点不同。',
 ('The path led across undeveloped land.','小路穿过未开发的土地。'),('The proposal contains several interesting but undeveloped ideas.','提议中有几个有趣、但还未展开的想法。'))
W('underdeveloped','英 /ˌʌndədɪˈveləpt/；美 /ˌʌndərdɪˈveləpt/','发展不充分的；欠发达的；展开不足的',
 '已经形成或开始发展，但比所需、预期的程度还少一截。',
 'under- 不充分、低于所需程度 + developed。under- 在这里不是空间下面，也不是 un- 的另一种拼写。',D+[['under- + developed → underdeveloped','已发展 → 发展程度不足']],
 'an underdeveloped transport network 发展不足的交通网，an underdeveloped character 人物刻画不充分；小说里也可用，不只经济术语。',
 'an underdeveloped network；an underdeveloped character；an underdeveloped idea。',
 'underdeveloped 不充分，undeveloped 未开发；under development 两词是正在开发，不能混成一个形容词。',
 ('The story has an interesting plot but underdeveloped characters.','故事情节有趣，但人物刻画不足。'),('The report highlights the region’s underdeveloped transport network.','报告指出了该地区交通网络发展不足的问题。'))
W('redevelop','/ˌriːdɪˈveləp/','重新开发；改建',
 '已有的地块、建筑或区域，用新的规划再做一遍，让它能承担新用途。',
 're- 重新 + develop 开发，常用于旧开发区域改造；对应名词 redevelopment 已在同词族页精讲。',D+[['re- + develop → redevelop','开发 → 在已有基础上重新开发']],
 'redevelop a site 重新开发地块，redevelop the station 改建车站；具体是否拆建、保留依方案。',
 'redevelop a site；redevelop an area；plans to redevelop。',
 'redevelop 重开发，renovate 更常说翻修建筑；rebuild 重建强调建筑重新造，不完全相同。',
 ('The city plans to redevelop the old railway yard.','城市计划重新开发旧铁路货场。'),('The company will redevelop the site for housing.','公司将重新开发这块地，用于住宅建设。'))
R('B3554','发展、形成、开发；已形成、正形成与不足','DEVELOP：把未成形的东西逐步展开','先看 develop，再读开发者 developer；developed、developing、undeveloped、underdeveloped 按完成、进行和不足区分。',
 'develop 经法语接展开、解包的历史词，包裹部分更远来源不确定。development 已在前文精讲，此处共享完整词族，名词派生与动词一起看。',
 'develop → developer、developed、developing；un- 未开发、under- 不充分；re- 重新 → redevelop → redevelopment；development → developmental。',
 [['形成、开发与执行者','develop · developer · development · developmental'],['已形成与正在形成','developed · developing'],['未开发与发展不足','undeveloped · underdeveloped · underdevelopment'],['重新开发','redevelop · redevelopment']],
 'develop 问题出现不一定改善；developing 不是 developer；undeveloped、underdeveloped、under development 分开。',
 'The developer will redevelop the site, but the plan is still under development.\n\n开发商将重新开发这块地，但方案仍在制定中。',
 'develop developer development developmental developed developing undeveloped underdeveloped underdevelopment redevelop redevelopment')
HA=[['古英语 hatian、hete 等 → 中古英语 hate','强烈厌恶、敌意；相应名词词族'],['现代 hate 词族','仇恨、讨厌；人、话语、被讨厌状态分别派生']]
W('hate','/heɪt/','仇恨；非常讨厌；不愿、遗憾要做',
 '可以是很重的敌意，也能在日常夸张说讨厌等车、讨厌洗碗；别只按一个强度翻译所有句子。',
 '继承古英语 hatian 等厌恶词族。现代动词和名词都常用，hate doing、hate to do 有时按语气、习惯选择。',HA,
 'hate waiting 讨厌等待，hate lies 讨厌谎言；I hate to interrupt, but... 很不愿打断，不过……是礼貌铺垫之一。',
 'hate doing；hate to say；a hate campaign；love and hate。',
 'hate 通常比 dislike 更强，但 I hate Mondays 常有口语夸张；hate to bother you 不一定真在仇恨打扰这个动作。',
 ('I hate waiting in long queues.','我很讨厌排长队。'),('I hate to interrupt, but the meeting is starting.','很不愿打断，不过会议要开始了。'))
W('hated','/ˈheɪtɪd/','被讨厌、憎恨的；hate 的过去形式',
 '把视角放到被别人讨厌的对象，而不是它自己正在表现仇恨。',
 'hate 去 e + -ed，t 后 -ed 读 /ɪd/；是过去式、过去分词，也可在名词前修饰。',HA+[['hate + -ed → hated','讨厌 → 被讨厌、曾讨厌']],
 'a much-hated rule 备受厌恶的规则，a hated task 令人不愿做、被讨厌的任务；He hated it 是动词过去时。',
 'a hated task；a hated rule；widely hated。',
 'hated 被讨厌，hateful 可充满仇恨或令人厌恶；hated 不能自动说明对象自己也恨别人。',
 ('The manager removed a widely hated rule.','经理取消了一条大家都讨厌的规定。'),('She hated the early starts when she was younger.','她年轻时很讨厌一大早出发。'))
W('hatred','/ˈheɪtrɪd/，亦 /ˈheɪtrəd/','仇恨；强烈厌恶',
 '把很重、很持续的恨意作为一种情绪、态度来讲，比随口说不爱做某件小事更重。',
 'hate + 旧后缀 -red 表状态、性质，接中古英语 haterede 等。-red 与 kindred 的旧后缀对应，不是红色。',HA+[['hate + -red → hatred','仇恨 → 仇恨状态、强烈厌恶']],
 'hatred of violence 对暴力的憎恶，deep hatred 深仇大恨；hatred towards someone 对某人的恨意。',
 'hatred of；deep hatred；hatred towards；fuel hatred。',
 'hate 本身也可作仇恨名词，hatred 更明确是情绪、态度名词；不能说 I hatred it 来当动词。',
 ('The novel explores the damage caused by hatred.','小说探讨仇恨造成的伤害。'),('She spoke of her hatred of cruelty.','她谈到自己对残忍行为的憎恶。'),sources=['https://en.wiktionary.org/wiki/hatred#English','https://www.etymonline.com/word/hatred'])
W('hateful','/ˈheɪtfəl/','充满仇恨的；令人厌恶的',
 '一句话可以带着恨意；一种行为也能让人觉得非常可憎。两个方向都在这个词里。',
 'hate + -ful，历史有充满恨、值得恨等固定用法。-ful 不能机械只译装满，现代会评价内容、性质和给人感受。',HA+[['hate + -ful → hateful','仇恨 → 含仇恨或招人厌恶的']],
 'hateful comments 充满仇恨的评论，hateful behaviour 可憎行为；并不是 ordinary criticism 普通批评的统一名称。',
 'hateful comments；hateful language；hateful behaviour。',
 'hated 被人讨厌的，hateful 充满恨意或可憎；两个词末尾一换，施受关系和评价也会变。',
 ('The moderator removed the hateful comments.','版主删除了充满仇恨的评论。'),('The story condemns the character’s hateful behaviour.','故事谴责了这个角色可憎的行为。'))
W('hater','英 /ˈheɪtə/；美 /ˈheɪtər/','强烈厌恶某事者；恶意贬损、唱衰者〔口语〕',
 '不是提一个具体问题，而是总用敌意、酸话贬低别人；网络里常拿这个词称酸民、唱衰者。',
 'hate + -er，人物后缀；也能中性一点地说 someone is a hater of something，即强烈讨厌某事者。网络标签用法更带主观评价。',HA+[['hate + -er → hater','讨厌 → 厌恶者；口语恶意贬损者']],
 'online haters 网络恶意贬损者，ignore the haters 别理会唱衰者；不同意见、建设性批评不因此自动算恶意。',
 'online haters；ignore the haters；a hater of something。',
 'hater 是对人的称呼，hatred 是情绪；critic 批评者可以有依据、有善意，不与 hater 完全等同。',
 ('She refused to let online haters stop her from writing.','她不肯让网上恶意唱衰的人阻止自己写作。'),('The essay distinguishes a critic from a hater.','文章区分了批评者与恶意贬损者。'))
R('B3756','讨厌、仇恨；被恨、恨意和厌恶者','HATE：厌恶的强度，要结合对象和语气','hate waiting 可以日常夸张，hatred 常更重；hated 被讨厌，hateful 含恨、可憎，hater 是人物标签。',
 'hate 继承古英语厌恶词族，hatred 的 -red 是旧状态后缀，和颜色 red 无关。后缀改变动作、状态和施受焦点。',
 'hate → hated；hate → hatred、hateful、hater。',
 [['厌恶与被厌恶','hate · hated'],['情绪、性质和人物','hatred · hateful · hater']],
 'hated 不等于 hateful；hatred 名词不能作动词；critic 不必是 hater；hate to interrupt 可礼貌铺垫。',
 'The writer described hatred without using hateful language.\n\n作者描写仇恨，却没有采用充满仇恨的语言。',
 'hate hated hatred hateful hater')
AN=[['古英语 andswaru、andswarian → 中古英语 answere','回应；and- 对应、反向 + swaru 郑重表态词族'],['英语 answer','答复、答案；接听、应门；为行为作出解释、负责']]
W('answer','英 /ˈɑːnsə/；美 /ˈænsər/','回答；答案、解决办法；接电话、应门；负责',
 '对面来了问题、电话、敲门或需要，你给一个回应；问题解决办法也就是它的 answer。',
 '继承古英语 andswaru、andswarian，构词与针对性的郑重表态有关，曾被解释为对指控的宣誓答复背景；现代是普通回应。w 在常用读音中不发音。',AN,
 'answer a question 回答问题，answer the phone 接电话，answer the door 应门；an answer to the problem 问题解决办法，answer for your actions 为行为负责。',
 'answer a question；answer the phone；the answer to；answer for。',
 '动词 answer the question，名词 the answer to the question；reply to a question 通常要 to，别把两种结构混在一起。',
 ('Can you answer the phone while I’m cooking?','我做饭时，你能接一下电话吗？'),('We still need an answer to the problem.','我们仍需要找到解决这个问题的办法。'))
W('answering','英 /ˈɑːnsərɪŋ/；美 /ˈænsərɪŋ/','回答、应答的；应答活动、形式',
 '动作在进行，或一个设备、服务的功能就是替人接听、作出回复。',
 'answer + -ing，动词形式，也用于 answering machine 等功能修饰语；w 不发音，不按拼写增加 /w/。',AN+[['answer + -ing → answering','答复、接听 → 应答活动或相应功能']],
 'answering questions 回答问题，an answering machine 电话答录机，an answering service 代接、应答服务。',
 'answering questions；an answering machine；an answering service。',
 'answering 是活动、功能修饰，answerable 是应负责、可回答；an answering machine 不是一台须承担责任的机器。',
 ('She spent the morning answering emails.','她上午一直在回复邮件。'),('The message was recorded on the answering machine.','留言被录在电话答录机上。'))
W('answerable','英 /ˈɑːnsərəbəl/；美 /ˈænsərəbəl/','应负责的；须向……交代的；可回答的',
 '有人能追问你为什么这样做，你必须给出交代；另一个用法只是问题能否回答。',
 'answer + -able，先常接 answer 负责、作解释的分支，也有能被回答的字面能力义。不能只看 -able 就漏掉常用责任含义。',AN+[['answer + -able → answerable','负责、作解释 → 须交代；另有能回答义']],
 'answerable to the board 向董事会负责，answerable for a decision 为决定负责；an answerable question 一个可回答的问题。',
 'answerable to；answerable for；an answerable question。',
 'answerable to 谁来追问、监督，answerable for 为哪件事负责；两个介词的角色不同。',
 ('The manager is answerable to the board.','经理向董事会负责。'),('The research question needs to be clear and answerable.','研究问题需要明确且可以回答。'),sources=['https://en.wiktionary.org/wiki/answerable#English','https://www.etymonline.com/word/answer'])
R('B2632','回答、应答、解决办法；负责与可回答','ANSWER：对请求、问题、呼唤作回应','问题可回答，电话可接，门响可应；为行为 answer for，则要对别人解释清楚。answerable 接责任这支很常见。',
 'answer 继承古英语回应词，有针对性郑重表态的构词背景。不是现代 and 与 swear 直接拼起来；常用读音不发 w。',
 'answer → answering、answerable；动词接问题不必 to，名词答案后常用 to。',
 [['回应、应答与责任性质','answer · answering · answerable']],
 'answer the question；the answer to the question；answerable to 人或机构，answerable for 行为、决定。',
 'The manager answered the question and explained whom she was answerable to.\n\n经理回答了问题，并说明自己向谁负责。',
 'answer answering answerable')
if __name__=='__main__':save('continuation_20261029_dl',ROOTS,WORDS)
