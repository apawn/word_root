"""High-frequency predicates and their common constructions."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'B3353':dict(words=['believe','believes'],label='believe → believes：把话当真、信任',note='本族信赖词，动词 v 与 belief 的 f 分开记。'),
 'C1057':dict(words=['explain','explains'],label='explain → explains：铺开讲清楚',note='拉丁使平、展开词经法语或拉丁路线借入。'),
 'C1288':dict(words=['describe','describes'],label='describe → describes：写出、描出样子',note='拉丁写下、描画词族经法语等借入。'),
 'C1353':dict(words=['consist','consists'],label='consist → consists：各部分共同组成',note='法语借入或直接拉丁来源均有分析，现代 consist of 不用被动。'),
 'C1657':dict(words=['involve','involves'],label='involve → involves：卷进去、包括在内',note='拉丁 in 与 volvere 的组合，现代包括和牵涉语境分别看。'),
 'C1325':dict(words=['deserve','deserves'],label='deserve → deserves：付出、行为配得上结果',note='拉丁尽力服务的词经法语发展，现代不限奖赏。'),
 'C1608':dict(words=['reveal','reveals'],label='reveal → reveals：移开遮盖、让人知道',note='拉丁遮盖词加 re，经法语借入；re 在此使状态转为相反。'),
 'C0847':dict(words=['occur','occurs'],label='occur → occurs：迎面遇到、发生、想到',note='拉丁朝向与跑组成，法语或直接拉丁借入两说保留。'),
 'B2502':dict(words=['add','adds'],label='add → adds：把另一份放上去',note='拉丁 addere 的后半是放置材料，不是 dare 给。'),
 'B3064':dict(words=['die','dies'],label='die → dies：死亡；模具另支',note='死亡动词可能北欧借入；die 骰子、模具的名词历史分开看。'),
 'B3843':dict(words=['hope','hopes'],label='hope → hopes：期待好结果',note='本族希望名词、动词均有旧形式，现代形态重合。'),
 'B3949':dict(words=['wish','wishes'],label='wish → wishes：愿望、祝愿与遗憾',note='古英语愿望动词延续，固定句型在英语中发展。'),
 'B2895':dict(words=['meet','meets'],label='meet → meets：相遇、接到与达到要求',note='古英语相遇动词，抽象满足标准按接上、达到理解。'),
 'B3029':dict(words=['care','cares'],label='care → cares：挂在心上的事',note='本族忧虑、关心名词及动词，复数与三单形态重合。'),
 'B3774':dict(words=['present','presents'],label='present → presents：礼物与呈现的不同重音',note='拉丁在场词族，不同名词、动词借入用途分别学习。'),
 'C1235':dict(words=['control','controls'],label='control → controls：核对卷册到控制',note='拉丁 contra、rotulus 经法语形成核查、掌控词族。'),
}
W('believes','/bɪˈliːvz/','相信、认为；信任〔第三人称单数〕',
 '把一句话接进自己的判断里，认为它是真的，是 believes；把一个人的可靠性接进心里，则是相信、信任。',
 'believe + -s，/v/ 后读 /z/。believe 继承古英语 belȳfan、gelȳfan 等信赖词，经中古英语延续；更早常联系珍视、信任的词族，但不把更远词义重建写死。',
 [['古英语信赖词 → 中古英语 → believe','信赖、信服 → 把某种说法当真'],['believe + -s → believes','单数主语相信、认为']],
 'believes the story 相信这个故事；believes that... 认为……；believes in her team 信任自己的团队。',
 'believes it is possible 相信这有可能；believes in fairness 相信公平的价值。','believes 是动词，beliefs 是信念的名词复数。前者 /v/，后者 /f/，拼写和读音一起记；believe somebody 与 believe in somebody 的侧重点也不同。',
 ('She believes that regular practice makes a difference.','她相信经常练习会带来改变。'),('The coach believes in the whole team.','教练信任整个团队。'),sources=['https://en.wiktionary.org/wiki/believes#English','https://www.etymonline.com/word/believe'])
W('explains','/ɪkˈspleɪnz/','解释、说明；说明原因〔第三人称单数〕',
 '原来皱在一起、不容易看清的事情，被铺展开，让人知道怎么回事，就是 explains 的讲清画面。',
 'explain + -s，/n/ 后读 /z/。拉丁 ex- 向外 + plānāre 使平 → explānāre 铺平、讲明，经法语及拉丁路线接英语 explain。',
 [['拉丁 explānāre → 法语、英语 explain','铺开、弄平 → 讲明白'],['explain + -s → explains','单数主语给出说明、解释原因']],
 'explains the problem 解释问题；explains how it works 说明工作原理；explains the delay 解释延误原因。',
 'explains it clearly 解释得清楚；explains the rule to us 向我们说明规则。','explain something to somebody：事情直接作宾语，人放在 to 后。The traffic explains the delay 中，主语是能说明原因的情况，不一定是会说话的人。',
 ('The diagram explains how the machine works.','图示说明了机器的工作原理。'),('She explains the rule to new players.','她向新玩家说明规则。'),sources=['https://en.wiktionary.org/wiki/explains#English','https://en.wiktionary.org/wiki/explain#English'])
W('describes','/dɪˈskraɪbz/','描述、描写；画出轮廓〔第三人称单数〕',
 '用话或文字，把一个人、一件事的样子勾出来，是 describes。重点是让别人能想见它有什么特点、怎样发生。',
 'describe + -s，/b/ 后读 /z/。拉丁 dē- 与 scrībere 写 → dēscrībere 写下、描画，经法语等借入英语；这里 de- 不按否定来译。',
 [['拉丁 dēscrībere → 法语等 → describe','写下、勾画 → 描述特征、经过'],['describe + -s → describes','单数主语作描述；事物画出轨迹']],
 'describes the scene 描述场景；describes how she felt 描写她的感受；describes him as patient 说他很有耐心。',
 'describes the process 描述过程；describes a circle 画出圆形轨迹。','describe something to somebody 是向某人描述某物。describe A as B 是把 A 描述为 B，可能含评价，不等于客观定义已经成立。',
 ('The book describes life in a small coastal town.','这本书描写一座海滨小镇的生活。'),('She describes her teacher as patient and encouraging.','她说自己的老师耐心又善于鼓励人。'),sources=['https://en.wiktionary.org/wiki/describes#English','https://en.wiktionary.org/wiki/describe#English'])
W('consists','/kənˈsɪsts/','由……组成；在于〔第三人称单数〕',
 '把各个部分一起摆定，看它们共同构成什么，就是 consists of；如果问关键究竟落在哪里，可以用 consists in。',
 'consist + -s，/t/ 后读 /s/。接法语 consister 或直接接拉丁 cōnsistere，con- 一起 + sistere 使站定；从一起处于某状态发展出由各部分组成。',
 [['拉丁 cōnsistere → 法语或直接借入 → consist','一起站定、存在 → 由部分构成'],['consist + -s → consists','单数主语由某些部分组成、实质在于']],
 'consists of three parts 由三部分组成；consists mainly of water 主要由水组成；consists in careful planning 在于周密计划。',
 'the team consists of... 团队由……组成；success consists in... 成功在于……。','consist of 直接说整体由什么组成，通常不用被动：The set consists of six pieces。consist in 说明本质、关键所在，不把两个介词混用。',
 ('The course consists of six short lessons.','课程由六节短课组成。'),('The mixture consists mainly of water.','这种混合物主要由水组成。'),sources=['https://en.wiktionary.org/wiki/consists#English','https://www.etymonline.com/word/consist'])
W('involves','/ɪnˈvɒlvz/；美亦 /ɪnˈvɑːlvz/','包括、涉及；需要；使参与〔第三人称单数〕',
 '把某人、某项行动或某种后果卷进一件事的范围里，是 involves。于是做某事时绕不开的步骤、牵涉的人和条件，都能成为宾语。',
 'involve + -s，/v/ 后读 /z/。拉丁 in- 在里面 + volvere 卷 → involvere 包住、卷入，经法语或直接拉丁借入的词族接英语 involve。',
 [['拉丁 involvere → involve','卷在里面 → 包括、牵涉、使参与'],['involve + -s → involves','单数主语涉及或需要某人、某行动']],
 'involves careful planning 需要细心规划；involves working late 包含工作到很晚；involves the whole team 涉及整个团队。',
 'involves several steps 包含几个步骤；involves everyone in the discussion 让所有人参与讨论。','involve doing 表示包含、需要做；involve somebody in something 表示使人参与。前者不加一个表示目的的 to。',
 ('The job involves talking to many different people.','这份工作需要与许多不同的人交谈。'),('The teacher involves every student in the discussion.','老师让每个学生都参与讨论。'),sources=['https://en.wiktionary.org/wiki/involves#English','https://en.wiktionary.org/wiki/involve#English'])
W('deserves','英 /dɪˈzɜːvz/；美 /dɪˈzɜːrvz/','值得、应得、应受〔第三人称单数〕',
 '一个人的行为、付出，或一件事本身的分量，配得上某种对待，是 deserves。可以配得上表扬，也可以应受批评。',
 'deserve + -s，/v/ 后读 /z/。拉丁 dēservīre 尽力服务，经法语 deservir 等发展为赢得、应得；dē- 在这里起加强作用，servīre 是服务。',
 [['拉丁 dēservīre → 法语 → deserve','尽力服务、挣得 → 应得某种结果'],['deserve + -s → deserves','单数主语值得得到、应受到']],
 'deserves praise 值得表扬；deserves attention 值得关注；deserves to be heard 应该得到倾听。',
 'deserves a rest 应该休息一下；deserves careful study 值得认真研究。','deserve 接名词或 to do；deserves to be considered 是值得被考虑。它并不只接好结果，deserves criticism 也很自然。',
 ('Her hard work deserves recognition.','她的努力值得认可。'),('This question deserves more careful study.','这个问题值得更认真研究。'),sources=['https://en.wiktionary.org/wiki/deserves#English','https://en.wiktionary.org/wiki/deserve#English'])
W('reveals','/rɪˈviːlz/','揭示、透露；显露〔第三人称单数〕',
 '把遮在上面的东西移开，让原来不知道、看不到的内容露出来，就是 reveals。可以真掀开遮挡，也可以让信息变得可知。',
 'reveal + -s，/l/ 后读 /z/。拉丁 re- 与 vēlāre 遮盖 → revēlāre 揭开，经古法语 reveler 借入；re- 在这里通常解释为撤回遮盖、转向相反状态。',
 [['拉丁 revēlāre → 法语 → reveal','去掉遮盖 → 使人看见、知道'],['reveal + -s → reveals','单数主语揭示某事、显露内容']],
 'reveals the answer 揭晓答案；reveals a problem 显示一个问题；reveals that... 揭示……。',
 'reveals hidden details 显露隐藏细节；reveals her plans 透露她的计划。','reveal 强调从未知、隐藏到可见或可知。不是每次 reveal 都有故意保密的背景，一张清晰照片也能显露此前难以看见的细节。',
 ('The photograph reveals details that are hard to see from the road.','照片显示了从路上很难看清的细节。'),('The report reveals a gap between the plan and the results.','报告揭示了计划与结果之间的差距。'),sources=['https://en.wiktionary.org/wiki/reveals#English','https://www.etymonline.com/word/reveal'])
W('occurs','英 /əˈkɜːz/；美 /əˈkɜːrz/','发生、出现；想到〔第三人称单数〕',
 '一件事来到现实或观察范围里，是 occurs；一个念头来到脑海里，则是 occurs to somebody。较早迎面遇上的画面能把它们连起来。',
 'occur + -s，这个 -s 读 /z/。拉丁 ob- 朝向在 c 前同化 + currere 跑 → occurrere 迎面来、遇到；英语可能经法语 occurrer，也可能直接借拉丁语。',
 [['拉丁 occurrere → 法语或直接 → occur','迎面跑来、遇到 → 出现、发生'],['occur + -s → occurs','单数事件发生；想法来到某人脑中']],
 'occurs every year 每年发生；occurs naturally 天然存在；it occurs to me that... 我想到……。',
 'occurs in several places 出现在几个地方；occurs during the test 测试时发生。','occur 通常不及物，事情发生不写被动。The idea occurs to her 的 to her 是念头来到谁脑中；不是某人主动安排某事。',
 ('The festival occurs every spring.','这个节庆每年春天举行。'),('The same pattern occurs in several examples.','同样的模式出现在几个例子中。'),sources=['https://en.wiktionary.org/wiki/occurs#English','https://en.wiktionary.org/wiki/occur#English'])
W('adds','/ædz/','加上、增加；补充说〔第三人称单数〕',
 '原来已有一份，再往上放另一份，就是 adds。数值、配料、信息和一句补充的话，都能加进去。',
 'add + -s，/d/ 后读 /z/。add 借拉丁 addere，较早 ad- 向 + -dere 放置；这里接放置词族，和 dare 给的拆法要分清。',
 [['拉丁 addere → add','朝某处放上去 → 加入、增加'],['add + -s → adds','单数主语把另一份加上、补充内容']],
 'adds water 加水；adds to the cost 增加成本；adds that... 补充说……。',
 'adds two numbers 把两个数相加；adds a new detail 补充一个新细节。','add A to B 是把 A 加入 B；add to something 是使它增加。adds up to 给出总数或合起来产生的结果。',
 ('She adds a little water to the mixture.','她往混合物里加一点水。'),('The extra stop adds ten minutes to the journey.','多停这一站让行程增加了十分钟。'),sources=['https://en.wiktionary.org/wiki/adds#English','https://en.wiktionary.org/wiki/add#English'])
W('dies','/daɪz/','死亡、枯死；熄灭、停止工作〔第三人称单数〕；模具〔复数〕',
 '生命走到终点是 dies；火、声音或机器停止活动，也能借这个不再继续的画面。工业名词 dies 模具则要另看来源和场景。',
 '死亡动词 die + -s → dies，读 /z/；加 s 时保留 ie。die 的死亡义见中古英语 deyen 等，可能接北欧 deyja；名词 die 经法语 de 的骰子、印模等词史进入，不能把两支合成一个。',
 [['中古英语及可能北欧死亡词 → die → dies','死亡 → 火熄灭、声音消失、机器停止'],['另支名词 die → dies','印模、模具的复数；与死亡动词分开']],
 'the plant dies 植物枯死；the sound dies away 声音渐渐消失；the engine dies 发动机熄火。',
 'dies of old age 寿终；dies down 渐渐减弱。','die 的死亡义变化是 die—died—dying；现在单数 dies 保留 ie。游戏骰子的常见复数是 dice，生产模具常用 dies。',
 ('The plant dies if its roots stay under water too long.','植物根部长时间泡在水里就会枯死。'),('The sound of the bells dies away in the distance.','远处钟声渐渐消失。'),sources=['https://en.wiktionary.org/wiki/dies#English','https://en.wiktionary.org/wiki/die#English'])
W('hopes','英 /həʊps/；美 /hoʊps/','希望、期望〔复数〕；希望、期盼〔第三人称单数〕',
 '朝一个想要的好结果看过去，心里觉得它有可能，是 hopes 的希望感。名词数愿望，动词说谁期待它发生。',
 'hope + -s，/p/ 后读 /s/。hope 的名词、动词接古英语 hopa、hopian 等旧形式，经中古英语延续，更远来源不确定；不凭形似连接跳跃 hop。',
 [['古英语希望名词、动词 → hope','期待想要的结果'],['hope + -s → hopes','若干希望；单数主语希望某事发生']],
 'high hopes 很高的期望；hopes to finish 希望完成；hopes that... 希望……。',
 'hopes for better weather 盼着天气好转；raise hopes 带来希望。','hope to do 与 hope that 都常见；不要把希望某人做什么硬套成 hope somebody to do，通常用 hope that somebody will do。',
 ('She hopes to finish the course before summer.','她希望夏天前完成课程。'),('The new library raised hopes of better access to books.','新图书馆让人对更方便地获取图书有了期待。'),sources=['https://en.wiktionary.org/wiki/hopes#English','https://en.wiktionary.org/wiki/hope#English'])
W('wishes','/ˈwɪʃɪz/','愿望、祝愿〔复数〕；希望、想要〔第三人称单数〕',
 '把心里想要的结果说出来，是 wishes。可以是给别人的祝愿，也可以是自己渴望却未必能实现的事情。',
 'wish + -es，/ʃ/ 后增加 /ɪz/。wish 继承古英语 wȳsċan 希望；愿望名词和祝愿、遗憾的句型在英语历史中发展，现代名词复数与动词三单同形。',
 [['古英语 wȳsċan → wish','想要、希望 → 愿望、祝愿'],['wish + -es → wishes','多项愿望、祝愿；单数主语希望']],
 'best wishes 诚挚祝愿；her wishes 她的意愿；wishes to speak 希望发言；wishes she had more time 希望自己有更多时间。',
 'respect their wishes 尊重他们的意愿；wishes him luck 祝他好运。','wishes to do 较正式，近想要；wishes somebody something 是祝愿。wishes + 过去式常说与现在现实不符的愿望，如 wishes she had more time。',
 ('She wishes her brother good luck before the exam.','考试前她祝弟弟好运。'),('He wishes he had more time to read.','他真希望自己有更多时间读书。'),sources=['https://en.wiktionary.org/wiki/wishes#English','https://en.wiktionary.org/wiki/wish#English'])
W('meets','/miːts/','见面、相遇；遇到；满足、达到〔第三人称单数〕',
 '人和人接上，是 meets 的相遇；河流接上另一条河，是汇合；事情做到要求所在的位置，则是 meets the requirements。',
 'meet + -s，/t/ 后读 /s/。meet 继承古英语 mētan 相遇，经中古英语延续；它的现代过去式是 met，meets 只表示现在单数主语。',
 [['古英语 mētan → meet','碰到、相遇 → 接到、达到要求'],['meet + -s → meets','单数主语见面、汇合或达到标准']],
 'meets her friends 与朋友见面；meets the river 与河汇合；meets the requirements 满足要求。',
 'meets every Tuesday 每周二碰面；meets a deadline 赶上截止日期。','meet somebody 通常直接接人；meet the standard 是达到标准。meets with somebody 常指为商谈而见面，meets with opposition 则是遇到反对。',
 ('The club meets every Tuesday evening.','俱乐部每周二晚碰面。'),('The design meets all the basic requirements.','设计满足所有基本要求。'),sources=['https://en.wiktionary.org/wiki/meets#English','https://en.wiktionary.org/wiki/meet#English'])
W('cares','英 /keəz/；美 /kerz/','关心、在意、照顾〔第三人称单数〕；忧虑、烦心事〔复数〕',
 '一件事挂在心上，就是 cares 的核心。向好的一面是关心、照顾；把压力挂住的一面，则是名词的烦心事。',
 'care + -s，结尾读 /z/。care 名词接古英语 caru、cearu 忧虑、挂心，动词有 carian 等旧形式；现代两种词性各自作规则变化。',
 [['古英语 caru、carian 等 → care','忧虑、挂心 → 在意、照顾'],['care + -s → cares','单数主语关心；一件件烦心事']],
 'cares about her friends 关心朋友；cares for her father 照料父亲；daily cares 日常烦恼。',
 'Who cares? 谁在乎呢？；cares deeply 非常在意。','care about 强调在意；care for 可以是照顾，也可在特定句式表示喜欢、想要。名词 care 泛指照料通常不数成 cares，cares 常是忧虑。',
 ('She cares about how the whole team is doing.','她关心整个团队的情况。'),('A quiet walk helped him forget his daily cares.','安静地走一走，让他暂时忘记日常烦恼。'),sources=['https://en.wiktionary.org/wiki/cares#English','https://en.wiktionary.org/wiki/care#English'])
W('presents','名词 /ˈprezənts/；动词 /prɪˈzents/','礼物〔复数〕；呈现、提交、介绍〔第三人称单数〕',
 '把东西送到面前，可以是一件礼物，也可以是一份方案、一段介绍。presents 的名词和动词有这种意义联系，但重音不同。',
 'present + -s，两种读法结尾都 /ts/。相关远源是拉丁 praesens 在场的、praesentāre 放到面前；动词经法语借入，礼物名词与呈送给人的表达相连。',
 [['拉丁在场、放到面前词族 → 法语、英语 present','呈送、展示；送给人的礼物'],['present + -s → presents；词性重音分化','名词多件礼物；动词单数主语呈现']],
 'birthday presents 生日礼物；presents the results 展示结果；presents a problem 带来一个问题。',
 'unwrap presents 拆礼物；presents her work to the class 向全班展示作品。','礼物名词前重音 /ˈprezənts/，呈现动词后重音 /prɪˈzents/。presents a challenge 常是造成、构成一个挑战，不是赠送礼品。',
 ('The children opened their presents after breakfast.','孩子们早餐后拆礼物。'),('She presents the results at the weekly meeting.','她在每周会议上展示结果。'),sources=['https://en.wiktionary.org/wiki/presents#English','https://en.wiktionary.org/wiki/present#English'])
W('controls','英 /kənˈtrəʊlz/；美 /kənˈtroʊlz/','控制、操纵〔第三人称单数〕；控制装置、管制措施、对照项〔复数〕',
 '让事情按一个可管理、可核对的范围运行，是 control 的共同线索。controls 可以是人按的按钮、调节器，也可以是机构设的限制。',
 'control + -s，/l/ 后读 /z/。经盎格鲁法语 contreroller，较早接 contra 对照 + rotulus 登记卷；与拿另一份记录核账的做法相关，后扩展为监督、掌控，名词再从动词形成。',
 [['登记卷核对词 → 法语 → control','核查、监督 → 掌控、调节'],['control + -s → controls','单数主语控制；多个装置、措施或对照项']],
 'controls the temperature 调节温度；the controls of a machine 机器操纵装置；safety controls 安全控制措施。',
 'price controls 价格管制措施；controls for the experiment 实验对照项。','controls 在实验里还可能是对照样本、对照条件，帮助比较观察结果；机器语境通常是操纵装置。都要看它在什么系统里起作用。',
 ('This switch controls the lights in the hall.','这个开关控制大厅的灯。'),('The engineer checked the machine’s controls.','工程师检查了机器的操纵装置。'),sources=['https://en.wiktionary.org/wiki/controls#English','https://www.etymonline.com/word/control'])
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_zk',ROOTS,WORDS)
 extend_lessons()
