"""Kiss, schedule, combo, angry, cute and -ible: common practical extensions."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
K=[['古英语 cyssan、coss 等 → 中古英语 → kiss','亲吻动作及名词，日耳曼语继承词族'],['现代派生与比喻','kissing 动作；kisser 人物、嘴脸；轻触、告别等引申']]
W('kiss','/kɪs/','吻、亲吻；轻触',
 '嘴唇碰一下表示感情、问候，也可借来说东西轻轻碰到；kiss goodbye to a hope 则像跟希望告别，表示放弃。',
 '动词接古英语 cyssan，名词接 coss 等早期形式，历史上同族并行发展。更远常被解释为拟声，但不必假定一个确定最早亲吻声音。',K,
 'give someone a kiss 亲一下，kiss someone on the cheek 吻某人的面颊，blow a kiss 飞吻，kiss goodbye to 告别、放弃。',
 'give someone a kiss；kiss on the cheek；blow a kiss；kiss goodbye to。',
 'kiss 动词可直接接人，give a kiss 名词要配结构；kiss goodbye to 不只真的亲吻，也可表示某种希望没了。',
 ('She kissed the child on the forehead.','她亲了一下孩子的额头。'),('He blew a kiss from the train window.','他从火车窗口送来一个飞吻。'))
W('kissing','/ˈkɪsɪŋ/','亲吻的动作；正在亲吻的；刚好相接的',
 '把亲吻当一个过程；也可形容两物轻轻挨着，像只是碰了一下，没有大幅重叠。',
 'kiss + -ing，早期英语已有相应分词、名词形式。ss 已在基础词里，不需再添一个 s。',K[:1]+[['kiss + -ing → kissing','亲吻过程、正在亲吻；轻触相接的']],
 'kissing goodbye 吻别，a kissing scene 亲吻场景，just kissing 刚好相接〔描述物体时〕。',
 'kissing goodbye；a kissing scene；kissing on the cheek。',
 'kissing 的 -ing 可过程名词或分词，不能只按一种进行时处理；kissing scene 是场景类型。',
 ('The film includes a brief kissing scene.','影片有一小段亲吻场景。'),('The two circles were just kissing at one point.','两个圆刚好在一点相接。'))
W('kisser','英 /ˈkɪsə/；美 /ˈkɪsər/','亲吻的人；嘴、脸〔俚语〕',
 '人物义是亲吻者；俚语里把用来亲的嘴、脸也叫 kisser，所以 on the kisser 常是在说脸部。',
 'kiss + -er，人物后缀先构成亲吻者，再有口语部位代称，不把每个 -er 都只译成职业。',K[:1]+[['kiss + -er → kisser','亲吻的人'],['功能相关的俚语转称','嘴或脸']],
 'a good kisser 善于接吻的人，on the kisser 在脸上〔俚语〕，a hit on the kisser 打中脸。',
 'a good kisser；on the kisser；a hit on the kisser。',
 'kisser 的嘴脸义很口语，正式描述一般用 mouth、face；不是标准解剖部位名。',
 ('The novel describes him as a good kisser.','小说把他写成很会接吻的人。'),('In the cartoon, a pie lands on his kisser.','动画里，一个派砸在他脸上。'))
R('B3307','亲吻到轻触，再有口语部位名','KISS：轻轻一碰的动作，也可以说告别','kiss → kissing、kisser，基础动作、过程和人物部位用法相邻。',
 'kiss goodbye to a plan 不一定真的亲吻，kisser 的脸是俚语；kissing circles 则是轻触画面。',
 'cyssan、coss 等经中古英语 → kiss；kiss + -ing/-er。',
 [['动作、过程和口语人物部位','kiss · kissing · kisser']],
 'kiss 与 give a kiss 动词名词结构；kisser 正式部位仍用 face、mouth；kiss goodbye to 可比喻放弃。',
 'The film ended with the characters kissing goodbye.\n\n影片以人物吻别作结。','kiss kissing kisser')
S=[['希腊 skhédē 等 → 拉丁 scheda、schedula → 法语 cedule → 中古英语','纸片、字条、附表'],['schedule 的拼写与用途扩展','清单、附表 → 时间表、日程；后来作动词安排'],['前缀和工具名','reschedule 重新安排；scheduler 排程人、工具']]
W('schedule','英 /ˈʃedjuːl/ 或 /ˈʃedʒuːl/；美 /ˈskedʒuːl/','日程、时间表；附表、清单；安排',
 '把什么时候做什么写成安排，就是 schedule；某些文件里的 schedule 则是列明细的附表，不必带具体钟点。',
 '从纸片、字条的希腊拉丁词，经法语接入英语，后来清单扩到日程。拼写向古典形式靠拢，读音也有英美变化；不拆成 school + 某词。',S,
 'a tight schedule 紧日程，ahead of schedule 比计划提前，behind schedule 落后进度，schedule a meeting 安排会议。',
 'a tight schedule；ahead of schedule；behind schedule；schedule a meeting。',
 'schedule 名词、动词都前重音，英美开头有 /ʃ/、/sk/ 常见差别；schedule 附表不是所有情况都翻成时间表。',
 ('The project is ahead of schedule.','项目进度比计划提前。'),('We scheduled the meeting for Friday.','我们把会议安排在周五。'),
 sources=['https://en.wiktionary.org/wiki/schedule#English','https://www.etymonline.com/word/schedule'])
W('reschedule','英 /ˌriːˈʃedjuːl/；美 /ˌriːˈskedʒuːl/','重新安排、改期',
 '原来已有时间或顺序安排，现在换一个；改到更早、更晚都可以，不只延期。',
 're- 再 + schedule，形成重新安排动词。re- 管再次安排，不自动规定新日期一定在原日期之后。',S[:2]+[['re- + schedule → reschedule','再次排定、改变安排']],
 'reschedule a meeting 改会议时间，reschedule for Monday 改到周一，reschedule an appointment 改预约。',
 'reschedule a meeting；reschedule for；reschedule an appointment。',
 'reschedule 改期可提前或延后，postpone 专说推迟；cancel 取消则不保证另安排。',
 ('Can we reschedule the meeting for Monday?','我们能把会议改到周一吗？'),('The appointment was rescheduled to an earlier date.','预约改到了更早的日期。'))
W('scheduler','英 /ˈʃedjələ/；美 /ˈskedʒələr/，亦有保留 /uː/ 的读法','排程人员；调度器、计划任务工具',
 '决定任务先后、什么时间运行的人或程序；系统里 scheduler 常在分配运行机会，不是日程表那张纸本身。',
 'schedule + -er，表示安排者、执行排程的部件或程序。程序语境再有资源调度的具体用法。',S[:2]+[['schedule + -er → scheduler','排程者；执行排程、资源分配的工具']],
 'a task scheduler 任务计划工具，a job scheduler 作业调度器，the operating system scheduler 操作系统调度器。',
 'a task scheduler；a job scheduler；the operating system scheduler。',
 'schedule 是安排、时间表，scheduler 是安排者或工具；calendar 日历可能显示结果，但不必具有自动调度功能。',
 ('The scheduler runs the backup every night.','任务计划工具每晚运行备份。'),('The operating system scheduler decides which task runs next.','操作系统调度器决定下一个运行的任务。'),
 sources=['https://en.wiktionary.org/wiki/scheduler#English','https://www.merriam-webster.com/dictionary/scheduler'])
R('B4170','写在纸上的清单，到安排时间和任务','SCHEDULE：把事项放进可执行的次序、时间里','schedule → reschedule、scheduler，先安排，再改期和执行工具。',
 '英美读法不同不等于两个词；改期可提前，附表可没有钟点，排程器则是安排的人或程序。',
 '纸片、字条相关古典词经法语 → schedule 清单、日程 → 动词；re- + schedule；schedule + -er。',
 [['安排、改期与排程者','schedule · reschedule · scheduler']],
 'reschedule/postpone/cancel 改期、推迟、取消；schedule/scheduler 安排与执行者。',
 'The scheduler rescheduled the task without changing the other appointments.\n\n排程工具重新安排了这项任务，其他预约未变。','schedule reschedule scheduler')
W('combo','英 /ˈkɒmbəʊ/；美 /ˈkɑːmboʊ/','组合、小乐队；套餐；连招',
 '几样东西搭在一起：小乐队几个人一组，套餐几种食物一组，游戏几下有效衔接成连招。',
 'combination 截短并配 -o 口语结尾，常先见于小乐队等用法，再扩到组合套餐、动作连段。不是 com + bo 两个正式词根。',
 [['combination 的口语缩短 → combo','组合，常见小乐队称呼'],['现代场景扩展','食品组合、套餐；动作组合、游戏连招']],
 'a jazz combo 爵士小乐队，a combo meal 套餐，a winning combo 好用组合，perform a combo 打出连招。',
 'a jazz combo；a combo meal；a winning combo；perform a combo。',
 'combo 较口语，combination 更一般、正式；游戏连招通常强调有效衔接，不是随便按很多次键就一定算。',
 ('A jazz combo played in the café.','一支爵士小乐队在咖啡馆演奏。'),('She ordered a combo meal with a drink.','她点了一份配饮料的套餐。'))
R('B3673','组合成整体与口语缩短','COMBINATION：几个部分合在一起，日常也简称 combo','combination → combo；recombination 看已存在的材料重新组合。',
 'combo 套餐、小乐队、游戏连招，都是不同场景的一组；recombination 的科学义有更具体对象。',
 'combine 相关名词 combination 的借入历史；combination 缩短配 -o → combo；re- + combination。',
 [['组合及口语简称','combination · combo'],['重新组合','recombination']],
 'combo 口语与 combination 一般用法；recombination 重新组合非完全凭空新造。',
 'The small combo used an unusual combination of instruments.\n\n小乐队采用了一种不常见的乐器组合。','combination combo recombination')
A=[['古诺斯语 angr 等 → anger','痛苦、烦恼等 → 愤怒'],['中古英语 angry → 现代 angry','anger + -y 的性质关系：感到或表现愤怒'],['angry → angrily','以生气的方式说话、行动']]
W('angry','/ˈæŋɡri/','生气的、愤怒的；风暴般凶猛的〔比喻〕',
 '心里有火，对人或事情不满；也可借给乌云、海浪，写出凶猛、威胁的感觉。',
 '中古英语已有 angry，现代对应 anger + -y，词形压缩为 angr-。anger 更早接北欧痛苦、烦恼词族，不把 angry 拆成 ang + ry 两个新词根。',A,
 'angry with someone 生某人的气，angry about something 因某事生气，angry at the decision 对决定气愤，angry clouds 凶猛乌云。',
 'angry with；angry about；angry at；get angry。',
 'angry 情绪，hungry 饿只差部分字母却不同；with、at、about 有搭配重叠，不用僵硬认成某个介词只能接人或事。',
 ('She was angry about the delay.','她因延误而生气。'),('Angry clouds gathered above the hills.','山丘上空聚起了气势汹汹的乌云。'))
W('angrily','/ˈæŋɡrɪli/，美式也常弱读 /ˈæŋɡrəli/','生气地、愤怒地',
 '不是只说某人心里生气，而是他讲话、关门、回应时带着怒气；副词把情绪落在动作方式上。',
 'angry 末尾 y 变 i + -ly，成 angrily；中古英语已有相应形式，不写成 angryly。',A[:2]+[['angry → angrily〔y 变 i 再加 -ly〕','以愤怒方式说话、行动']],
 'reply angrily 生气回应，shout angrily 愤怒叫喊，look angrily at 怒视。',
 'reply angrily；shout angrily；look angrily at。',
 'be angry 说状态，reply angrily 说怎么回应；不要把副词直接放在 be 后替代所有 angry。',
 ('He replied angrily and left the room.','他生气地回应后离开房间。'),('She looked angrily at the broken window.','她气愤地看着破窗。'))
R('B2631','愤怒情绪和带着愤怒做事','ANGRY：心里生气，再看动作怎么表现','angry → angrily，把状态和动作方式放一起学。',
 'angry 的乌云、海浪义是气势比喻；angrily 则经 y 变 i 后接 -ly。',
 'angr → anger；anger + -y 对应 angry；angry + -ly → angrily。',
 [['情绪状态与动作方式','angry · angrily']],
 'angry/hungry 生气饥饿不同；be angry/reply angrily 状态方式；介词搭配看实际对象。',
 'He was angry and answered angrily.\n\n他心里生气，回答时也带着怒气。','angry angrily')
U=[['acute 的截短 cute','原有机灵、聪明等旧义 → 现代可爱、讨喜'],['cute + 人物、语气词尾','cutie 可爱的人或动物；cutesy 过度装可爱']]
W('cutie','/ˈkjuːti/','可爱的人、小可爱；可爱的动物〔口语〕',
 '把可爱的对象直接叫“小可爱”，可亲昵、调情，也可能让不熟的人不舒服，语气和关系很重要。',
 'cute + -ie，去末尾 e 接人物、亲昵词尾；cute 更早来自 acute 的缩短。并非正式性别或年龄类别。',U,
 'a little cutie 小可爱，what a cutie 真可爱，a cutie in the photo 照片中的可爱对象。',
 'a little cutie；what a cutie；a cutie in the photo。',
 'cutie 名词，cute 形容；Cuties 等也可商标名称，不用把果品品牌反推成 cutie 人物义的来源。',
 ('Your puppy is such a cutie.','你的小狗真是个小可爱。'),('Everyone called the smiling baby a cutie.','大家都说那个爱笑的宝宝很可爱。'))
W('cutesy','/ˈkjuːtsi/','故作可爱的、过分甜腻可爱的〔常贬义〕',
 '蝴蝶结、甜声音、卡通装饰堆得太满，让人觉得用力装可爱，就是 cutesy；不只是普通夸可爱。',
 'cute + 口语性质词尾 -sy，组成过度、做作可爱的形容词。',U[:1]+[['cute + -sy → cutesy','过度追求可爱、带做作感']],
 'a cutesy voice 故作可爱的声音，cutesy decorations 甜腻装饰，a cutesy design 过度可爱的设计。',
 'a cutesy voice；cutesy decorations；a cutesy design。',
 'cute 通常可正面，cutesy 常嫌过头；cutie 指对象，cuteness 是可爱这种性质。',
 ('The design was too cutesy for the formal event.','这个设计对正式活动来说过于甜腻可爱。'),('She disliked the narrator’s cutesy voice.','她不喜欢旁白故作可爱的声音。'))
R('B3123','可爱、讨喜与过度装可爱','CUTE：可爱是性质，小可爱是对象，cutesy 常嫌过头','cute → cuteness、cutie、cutesy，从性质、对象到带评价的过度可爱。',
 'cute 原与 acute 缩短、机灵义有关，现代可爱是常见意思；cutesy 不要当完全中性赞美。',
 'acute → cute；cute + -ness/-ie/-sy，去 e 的位置按具体拼法记。',
 [['可爱性质、对象与语气','cute · cuteness · cutie · cutesy']],
 'cute 形容；cutie 名词对象；cuteness 性质；cutesy 通常负面嫌做作。',
 'The puppy was cute, but the advertisement felt cutesy.\n\n小狗很可爱，不过广告显得过分装可爱。','cute cuteness cutie cutesy')
I=[['拉丁 -ibilis 等 → 法语 -ible → 英语 -ible','可……、能够被……；关系需结合词基'],['借入整词与后来的英语造词','有些已有拉丁法语历史，有些英语后来按模式构成'],['词形不能随意互换','-ible/-able 意思常近，拼写需随整词学；gullible 历史另有讨论']]
W('deductible','/dɪˈdʌktəbl/','可扣除的；免赔额、自负额〔名词，保险语境〕',
 '先有 deduct 从总数扣掉：deductible 说可以扣除；保险名词又指通常先由自己承担、未进入相应赔付的那部分金额。',
 'deduct 扣除的词基 + -ible，可扣除；较早词基接拉丁 dēdūcere 等。名词是形容词的专门化，不等于凡能扣除的金额都叫保险免赔额。',I[:2]+[['deduct + -ible → deductible','可以扣除'],['保险语境的名词化','相应条款中的免赔额、自负额']],
 'a deductible expense 可扣除费用，a deductible amount 可扣金额，an insurance deductible 保险免赔额。',
 'a deductible expense；a deductible amount；an insurance deductible。',
 'deductible 形容可扣、名词免赔额，deduction 是扣除行为、扣除额；具体金额与适用范围由实际条款确定。',
 ('The form asked whether the expense was deductible.','表格问这笔费用是否可以扣除。'),('The policy listed the deductible on the first page.','保单在第一页列明了免赔额。'))
W('gullible','/ˈɡʌləbl/，也有 /ˈɡʌlɪbl/','轻信的、容易受骗的',
 '别人说什么就容易信，很少先查证，骗子一牵就跟着走；并不是单纯善良、友好。',
 '常联系 gull 欺骗、受骗者与 -ible；也有从较早 gullibility 倒推形容词的分析，具体造词过程不定。不把它解释成海鸥 gull 天生好骗的确定故事。',I[:2]+[['gull 的欺骗、受骗者词族；gullibility 等较早形式','具体来源、造词顺序有不同分析'],['gullible','容易相信而被欺骗的']],
 'a gullible customer 轻信顾客，gullible enough to believe 容易轻信到相信，too gullible 太好骗。',
 'a gullible customer；too gullible；gullible enough to believe。',
 'gullible 容易被骗，trusting 愿意信任可较中性或正面；不轻信也不等于必须怀疑一切。',
 ('The scam targeted gullible customers.','骗局盯上了容易轻信的顾客。'),('He was gullible enough to believe the invented story.','他太轻信，竟相信了编造的故事。'),
 sources=['https://en.wiktionary.org/wiki/gullible#English','https://www.etymonline.com/word/gullible'])
W('reproducible','英 /ˌriːprəˈdjuːsəbl/；美 /ˌriːprəˈduːsəbl/','可重现的、可复现的；可复制的',
 '给出办法和条件，别人再照着做，也能得到相应结果；软件错误稳定再出现，也说 reproducible。',
 'reproduce 重新产生、复制，去 e + -ible。re- 再、produce 产生的现代层次清楚，较早词基有拉丁、法语历史。',I[:2]+[['re- + produce → reproduce；reproduce + -ible → reproducible','重新产生 → 能再次得到、复制的']],
 'reproducible results 可复现结果，a reproducible bug 可稳定复现的错误，a reproducible example 可复现示例。',
 'reproducible results；a reproducible bug；a reproducible example。',
 'reproducible 重点是再做能得到相应结果；repeatable 在不同领域有自己的约定，不用一句统一定义强分所有学科。',
 ('The team published code to make the results reproducible.','团队公开代码，让结果可以复现。'),('Please provide a reproducible example of the error.','请提供一个能够复现错误的示例。'))
W('invertible','英 /ɪnˈvɜːtəbl/；美 /ɪnˈvɜːrtəbl/','可倒转的；可逆的、有逆的〔数学等〕',
 '能把操作倒回来，或能找到相应的逆；数学里 invertible matrix 是有逆矩阵的矩阵，不只是能把纸翻个面。',
 'invert 倒转 + -ible；invert 较早接拉丁 in- 向内、进入与 vertere 转的组合，不把此处 in- 先认成否定。',I[:2]+[['invert + -ible → invertible','能够倒转、具有逆的']],
 'an invertible matrix 可逆矩阵，an invertible function 可逆函数，an invertible transformation 可逆变换。',
 'an invertible matrix；an invertible function；an invertible transformation。',
 'invertible 数学对象有相应逆，reversible 一般可逆、可反转范围更广；不是所有能旋转的矩阵图形就有逆矩阵。',
 ('The exercise asked whether the matrix was invertible.','练习要求判断矩阵是否可逆。'),('The transformation is invertible.','这个变换可逆。'))
R('A1765','能够、可以被……，随词基确定方向','-IBLE：别只背一个能，要看究竟能做什么、被怎样处理','从常见 accessible、flexible 到 deductible、reproducible、invertible，按具体词基理解；gullible 单列不确定历史。',
 '有的整词早从拉丁法语借来，有的英语后来接尾；-ible 与 -able 功能近，不能凭中文意思随意换拼法。',
 '拉丁 -ibilis、-bilis 等经法语及直接借词 → -ible；现代动词词基继续接尾形成性质形容词。',
 [['能力、接近与接受','accessible · admissible · inducible · digestible · gullible'],['变换与反向操作','convertible · reversible · reproducible · invertible · reducible'],['材料、器具与传递','flexible · compressible · collapsible · submersible · transmissible'],['评价、辩护和扣除','deductible · negligible · collectible · reprehensible · forcible · defensible · irascible · fungible']],
 'deductible/deduction 可扣与扣除额；reproducible 看重现条件；invertible 数学逆；gullible 非海鸥故事；-able/-ible 拼法随整词。',
 'A reproducible example made the problem easier to understand.\n\n可复现示例让问题更容易理解。','accessible admissible inducible digestible gullible convertible reversible reproducible invertible reducible flexible compressible collapsible submersible transmissible deductible negligible collectible reprehensible forcible defensible irascible fungible')
if __name__=='__main__':save('continuation_20261030_eo',ROOTS,WORDS)
