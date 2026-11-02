"""Common roles: public affairs, representatives, organisers and audiences."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'C1090':dict(words=['politician','politicians'],label='politician → politicians：参与政治事务的人',note='politic、politics 词族加人物 ian，较早接公共事务、城邦材料。'),
 'C1297':dict(words=['president','presidents'],label='president → presidents：坐在前面主持的人',note='拉丁 prae 与 sedere 的现在分词，经法语等借入多种机构头衔。'),
 'C0507':dict(words=['governor','governors'],label='governor → governors：掌舵、治理者',note='拉丁 gubernator 经法语或直接借入，不把它只当现代 govern 加 or 的新造词。'),
 'C0661':dict(words=['delegate','delegates'],label='delegate → delegates：派出的代表与委派动作',note='拉丁 delegare、delegatus 的借入，名词弱尾、动词强尾分别标。'),
 'C0917':dict(words=['organizer','organizers','organiser','organisers'],label='organizer → organizers；organiser → organisers：组织者与整理工具',note='organize 加 er，ise、ize 两套拼写对应，后续 s 为复数。'),
 'C1007':dict(words=['competitor','competitors'],label='competitor → competitors：争取同一目标的人',note='拉丁 competitor 经法语或直接借入，英语名词早于常用 compete 的记录。'),
 'C1097':dict(words=['opponent','opponents'],label='opponent → opponents：对面竞争、反对的一方',note='拉丁 opponens 现在分词接 ob 与 ponere，英语借入人物名词。'),
 'B2741':dict(words=['listen','listener','listeners'],label='listen → listener → listeners：主动听的人',note='本族听取动词加人物 er，t 不发音。'),
 'C1635':dict(words=['view','viewer','viewers'],label='view → viewer → viewers：看的人与查看工具',note='看景象词族经法语进入，英语 er 命名观看者或工具。'),
}
W('politicians','/ˌpɒlɪˈtɪʃənz/；美 /ˌpɑːləˈtɪʃənz/','政治人物、从政者〔复数〕',
 '把公共事务、选举、政党或政府工作作为主要活动的人，是 politicians。它说角色，也可能随说话语气带有赞许或批评。',
 'politician + -s，/n/ 后读 /z/。politic、politics 词族与人物 -ian 结合，cian 一段读 /ʃən/；较早经法语、拉丁接希腊城邦、公共事务材料。',
 [['politic、politics 词族 + -ian → politician','政治、公共事务 → 从政的人'],['politician + -s → politicians','多位政治人物']],
 'local politicians 地方政治人物；politicians from different parties 不同政党的从政者；interview politicians 采访政治人物。',
 'politicians attending the debate 参加辩论的政治人物；former politicians 曾经从政的人。','politician 指从事政治活动的人，political scientist 指研究政治学的人；是否担任具体公职，还要看人物身份。词本身也不决定其能力、品德。',
 ('Local politicians answered questions at the public meeting.','地方政治人物在公开会议上回答问题。'),('The journalist interviewed politicians from several parties.','记者采访了几个政党的政治人物。'),sources=['https://en.wiktionary.org/wiki/politicians#English','https://www.etymonline.com/word/politician'])
W('presidents','/ˈprezɪdənts/','总统；校长、会长、机构负责人等〔复数〕',
 '坐在前面主持、负责一个组织的人，是 presidents 的历史画面。到了现代，国家、大学、协会、企业可以各有自己的 president 头衔。',
 'president + -s，/t/ 后读 /s/。拉丁 prae- 在前 + sedēre 坐 → praesidēns 主持的、主持者，经法语等借入；不是所有名词历史都由现代 preside 再加 ent 才出现。',
 [['拉丁 praesidēns → 法语等 → president','坐在前面主持 → 主持者、负责人'],['president + -s → presidents','多位总统或相应机构负责人']],
 'university presidents 大学校长；club presidents 俱乐部会长；former presidents 前任总统、前任负责人。',
 'presidents of several associations 几个协会的会长；a meeting of presidents 负责人会议。','president 的准确中文头衔看国家、机构：大学可译校长，协会可译会长。公司中的 president 与其他管理头衔如何分工，也不能只凭一个词定死。',
 ('The presidents of three universities met to discuss cooperation.','三所大学的校长开会讨论合作。'),('The club keeps photographs of its former presidents.','俱乐部保存着历任会长的照片。'),sources=['https://en.wiktionary.org/wiki/presidents#English','https://en.wiktionary.org/wiki/president#English'])
W('governors','英 /ˈɡʌvənəz/；美 /ˈɡʌvərnərz/','州长、省长；机构主管、理事等〔复数〕',
 '像掌舵一样，把一个地区或机构的事情引向可管理方向的人，是 governors。现代职务会因地方、组织而不同。',
 'governor + -s，末尾读 /z/。拉丁 gubernātor 掌舵者、治理者，经古法语 governeor 等或直接借入英语；较早 gubernāre 治理、掌舵与希腊航行指挥词相连。',
 [['拉丁 gubernātor → 法语或直接 → governor','掌舵、治理的人 → 地区、机构负责人'],['governor + -s → governors','多位州长、省长或机构治理人员']],
 'state governors 州长；school governors 学校理事；governors of the institution 机构治理人员。',
 'a meeting of governors 州长或机构理事会议；former governors 前任州长、前任主管。','governors 在地区治理中可能译州长、省长；学校等机构中又有理事、治理人员的用法。具体职权由制度决定，先认治理职责的共同点。',
 ('The school governors discussed plans for the new library.','学校理事讨论了新图书馆计划。'),('The exhibition includes portraits of former governors.','展览包括历任州长的画像。'),sources=['https://en.wiktionary.org/wiki/governors#English','https://en.wiktionary.org/wiki/governor#English'])
W('delegates','名词 /ˈdelɪɡəts/；动词 /ˈdelɪɡeɪts/','代表〔复数〕；委派、授权〔第三人称单数〕',
 '派出一个人，让他带着某个群体的意思去办事，这个人是 delegate；把任务、处理权交出去的动作，也用 delegate。',
 'delegate + -s，/t/ 后读 /s/。拉丁 dē- 离开 + lēgāre 带任务派出 → dēlēgāre，分词 dēlēgātus 经法语或直接借入相关英语名词、动词，词尾读法按词性区分。',
 [['拉丁 dēlēgāre、dēlēgātus → delegate','带职责派出去 → 代表；派作代表、授权'],['delegate + -s → delegates','名词多名代表；动词单数主语委派']],
 'conference delegates 会议代表；delegates from each school 各校代表；delegates tasks to the team 向团队委派任务。',
 'welcome the delegates 欢迎代表；delegates responsibility 委派职责。','名词尾 /ɡəts/，动词尾 /ɡeɪts/。delegate something to somebody 是把任务、权责委派给谁。',
 ('Delegates from several schools attended the conference.','几所学校的代表参加了会议。'),('She delegates routine tasks to the team.','她把常规任务委派给团队。'),sources=['https://en.wiktionary.org/wiki/delegates#English','https://www.etymonline.com/word/delegate'])
W('organizers','英 /ˈɔːɡənaɪzəz/；美 /ˈɔːrɡənaɪzərz/','组织者、筹办人员；整理用品〔复数〕',
 '把人、步骤或物品排得有条理的一方，是 organizers。活动里可以是筹办人员，桌面上也可以是把文具分类的小工具。',
 'organize 去 e + -er → organizer，再加 -s，末尾读 /z/。organize 的词族经法语、拉丁等接希腊 organon 工具、器官；现代人物、工具名词用 er 构成。',
 [['organize + -er → organizer','使有组织、有条理 → 组织者、整理工具'],['organizer + -s → organizers','多位筹办人员或多件整理用品']],
 'event organizers 活动组织者；the organizers of the meeting 会议筹办人；desk organizers 桌面收纳用品。',
 'thank the organizers 感谢组织者；organizers preparing the event 筹备活动的人员。','organizers 常用 z；organisers 是常见英式 s 拼写。er 可以命名人，也可命名帮助整理的工具，按宾语、修饰语看。',
 ('The organizers sent the programme to all participants.','组织者把日程发给所有参加者。'),('She uses small desk organizers for pens and notes.','她用小型桌面收纳用品放笔和便笺。'),sources=['https://en.wiktionary.org/wiki/organizers#English','https://en.wiktionary.org/wiki/organizer#English'])
W('organiser','英 /ˈɔːɡənaɪzə/；美同 organizer /ˈɔːrɡənaɪzər/','组织者、筹办人；整理工具〔常见英式拼写〕',
 '把分散的人、步骤或物品安排到一起，让事情有秩序地运行，就是 organiser 的作用。它可以是人，也可以是帮人整理物品的工具。',
 'organise 去 e + -er → organiser，与 organize → organizer 对应。s、z 是这套词族的拼写差异；构词核心都是组织、整理的动词与 er。',
 [['organise／organize + -er → organiser／organizer','安排有条理 → 组织者或整理工具'],['英语拼写变体沿用','organiser 常见于英式，读音与相应 z 形式一致']],
 'an event organiser 活动组织者；a personal organiser 个人日程簿、安排工具；a skilled organiser 善于组织的人。',
 'the organiser of the trip 旅行组织者；a desk organiser 桌面收纳用品。','英式英语也可用 organizer，不能把所有英式文本都限制为 s。学习时把 organiser、organizer 认成同一个词的两种常见写法。',
 ('She is the main organiser of the school festival.','她是学校节庆的主要组织者。'),('The desk organiser keeps her pens in one place.','桌面收纳用品让她的笔集中放在一处。'),sources=['https://en.wiktionary.org/wiki/organiser#English','https://en.wiktionary.org/wiki/organizer#English'])
W('organisers','英 /ˈɔːɡənaɪzəz/；美同 organizers /ˈɔːrɡənaɪzərz/','组织者、筹办人员；整理工具〔复数，常见英式拼写〕',
 '一场活动能顺利展开，背后安排场地、人员、步骤的人，就是 organisers。若说桌面用品，也可以是帮人把东西分门别类放好的工具。',
 'organiser + -s，末尾读 /z/；organiser 接 organise + -er。organise 与 organize 的拼写变体沿到人物词、复数，organisers 对应 organizers。',
 [['organise + -er → organiser','组织、整理的执行者或工具'],['organiser + -s → organisers','多个组织者或整理用品；与 z 形式同词']],
 'festival organisers 节庆组织者；the organisers of the conference 会议筹办人员；drawer organisers 抽屉收纳用品。',
 'contact the organisers 联系组织者；thank the organisers 感谢筹办人员。','s、z 的拼写差异不意味着另有一种工作。阅读 organisers、organizers 时认成同一词族，写作时在同一篇文字里保持习惯一致。',
 ('The organisers asked everyone to arrive before nine.','组织者请大家九点前到达。'),('We thanked the organisers for their careful planning.','我们感谢组织者的细心筹划。'),sources=['https://en.wiktionary.org/wiki/organisers#English','https://en.wiktionary.org/wiki/organiser#English'])
W('competitors','英 /kəmˈpetɪtəz/；美 /kəmˈpetɪtərz/','竞争者、对手；参赛者〔复数〕',
 '几个人、几家公司都在争取同一个目标，他们就是 competitors。比赛里数参赛者，商业里说提供相近东西、争取同一批顾客的企业。',
 'competitor + -s，末尾读 /z/。名词接法语 compétiteur 或直接借拉丁 competītor 对手，连到 competere 一起争取，com- 与 petere 寻求；英语整个人物名词有较早借入记录。',
 [['拉丁 competītor → 法语或直接 → competitor','争取同一目标的人 → 对手、参赛者'],['competitor + -s → competitors','多名选手、多家竞争企业']],
 'fellow competitors 其他参赛者；main competitors 主要竞争对手；competitors in the race 赛跑选手。',
 'keep up with competitors 跟上竞争对手；prices offered by competitors 竞争对手的报价。','competitors 可以包括整场比赛的选手，不限于正和自己直接交手的一位。人物名词在拉丁语已形成，不只按英语 compete 后临时加几个字母解释。',
 ('All competitors must register before the race.','所有参赛者必须在赛前登记。'),('The company compared its service with those of its competitors.','公司把自己的服务与竞争对手的服务进行比较。'),sources=['https://en.wiktionary.org/wiki/competitors#English','https://www.etymonline.com/word/competitor'])
W('opponents','英 /əˈpəʊnənts/；美 /əˈpoʊnənts/','对手、反对者〔复数〕',
 '摆在自己对面，争同一个比赛结果或坚持相反意见的人，是 opponents。可以是体育对手，也可以是某个方案的反对者。',
 'opponent + -s，/t/ 后读 /s/。拉丁 ob- 对面、在前与 pōnere 放置 → oppōnere，b 在 p 前同化；现在分词 oppōnēns、opponent- 名词化借入英语，现代再加复数 s。',
 [['拉丁 oppōnēns → opponent','摆在对面、反对的一方 → 辩论或竞争对手'],['opponent + -s → opponents','多位对手、反对者']],
 'political opponents 政治对手；opponents of the proposal 提案反对者；respect your opponents 尊重对手。',
 'opponents in the final 决赛对手；listen to opponents’ arguments 听取反对者的论点。','opponents 表示在这项竞争、争议中站在对面，不必等于私人仇敌。opponents of something 常是反对某事的一群人。',
 ('The players shook hands with their opponents after the match.','球员赛后与对手握手。'),('Opponents of the plan asked for a fuller explanation.','计划的反对者要求更充分的解释。'),sources=['https://en.wiktionary.org/wiki/opponents#English','https://www.etymonline.com/word/opponent'])
W('listeners','英 /ˈlɪsənəz/；美 /ˈlɪsənərz/','听众、收听者；倾听的人〔复数〕',
 '把注意力放到声音、话语上，认真接进来的人，是 listeners。广播的听众、朋友谈话时愿意倾听的人，都能这样叫。',
 'listen + -er → listener，再加 -s，末尾读 /z/，t 不发音。listen 接古英语 hlysnan 等本族听取词，现代 er 表执行倾听的人。',
 [['古英语听取词 → listen；加 -er → listener','主动听 → 听者、听众'],['listener + -s → listeners','多位收听者、倾听者']],
 'radio listeners 广播听众；good listeners 善于倾听的人；listeners to the programme 节目听众。',
 'regular listeners 经常收听的听众；questions from listeners 听众提问。','listen 强调把注意放在听上，hear 常可只是听见声音。a good listener 常是愿意专注理解别人话的人，并非仅说听力好。',
 ('The presenter answered questions from listeners.','主持人回答了听众的提问。'),('The teacher encouraged the students to become better listeners.','老师鼓励学生更善于倾听。'),sources=['https://en.wiktionary.org/wiki/listeners#English','https://en.wiktionary.org/wiki/listener#English'])
W('viewers','英 /ˈvjuːəz/；美 /ˈvjuːərz/','观众、观看者；查看器〔复数〕',
 '把画面、影像或展品放到眼前看的人，是 viewers。软件或设备若帮助人查看内容，也可以有 viewer 的工具名称。',
 'view + -er → viewer，再加 -s，末尾读 /z/。view 经法语 veue 看见的景象接拉丁 vidēre 词族，英语动词和 er 人物、工具名词后来发展。',
 [['view + -er → viewer','观看、查看 → 观看者或查看工具'],['viewer + -s → viewers','多位观众、多种查看器']],
 'television viewers 电视观众；viewers of the film 影片观众；image viewers 图像查看器。',
 'attract viewers 吸引观众；comments from viewers 观众评论。','viewers 常强调看，listeners 强调听，readers 强调读。一个节目可同时有看直播的 viewers 和只听声音的 listeners。',
 ('The programme invites viewers to send in questions.','节目邀请观众发来问题。'),('The exhibition gives viewers a close look at the sketches.','展览让观众近距离观看那些草图。'),sources=['https://en.wiktionary.org/wiki/viewers#English','https://en.wiktionary.org/wiki/viewer#English'])
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_zu',ROOTS,WORDS)
 extend_lessons()
