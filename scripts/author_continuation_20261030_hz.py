"""Scholarship, suitability, strips and interpretation."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
S=[['scholar 学者、学习者 + -ship','学者的学问、研究活动与成果'],['资助学习的专门用法','奖学金、助学资助']]
W('scholarship','英 /ˈskɒləʃɪp/；美 /ˈskɑːlərʃɪp/','奖学金；学问、学术研究及成果',
 '学生说拿到一份 scholarship，通常是学习资助；书评夸 the scholarship，可能是在夸考证、研究有分量，和钱无关。',
 'scholar + -ship，-ship 表性质、活动、成就或身份等，不是船。学术性质、研究和资助学习的制度用法后来共存。',S,
 'win a scholarship 获得奖学金，a full scholarship 全额奖学金，historical scholarship 历史研究，sound scholarship 扎实学问。',
 'win a scholarship；a full scholarship；historical scholarship；sound scholarship。',
 'scholarship 不一律可数：a scholarship 常是一项资助，scholarship 学问常不可数。good scholarship 也不等于奖学金金额高。',
 ('She won a scholarship to study engineering.','她获得奖学金去学工程。'),('The book is admired for its careful scholarship.','这本书因研究严谨而受到赞赏。'))
W('scholarly','英 /ˈskɒləli/；美 /ˈskɑːlərli/','学术的、学者式的；有学问的',
 '像学者那样认真查证、讨论，也可指面向学术研究的著作、期刊；不是只把句子写得很难读。',
 'scholar + -ly，形容词词尾，表示与学者、学问有关。这里不是副词，a scholarly article 直接修饰文章。',S[:1]+[['scholar + -ly → scholarly','学者的、学术性的']],
 'a scholarly article 学术文章，a scholarly journal 学术期刊，scholarly research 学术研究，a scholarly manner 学者般的举止。',
 'a scholarly article；a scholarly journal；scholarly research。',
 'scholarly 强调学问、研究性质；scholarship 在资助义里说钱。scholarly book 不一定艰涩，也不因这个形容词就免于批评。',
 ('She published a scholarly article on medieval trade.','她发表了一篇关于中世纪贸易的学术文章。'),('The museum catalogue is scholarly but easy to read.','博物馆图录有学术深度，也容易读。'))
R('B4273','学习研究的人、学问与学习资助','SCHOLAR：研究者的学问，也能连到资助学习','scholar → scholarly 学术的；scholarship 既是学问研究，也可是一份奖学金。',
 '看名词对象最管用：拿到的常是资助，称赞一本书时则常是其研究。-ly 在这里形成形容词。',
 'scholar + -ly/-ship；scholar 自身远接学校、学习词族。',
 [['人物、学术性质与学问资助','scholar · scholarly · scholarship']],
 'scholarly 不是副词；scholarship 学问常不可数、奖学金可数；学术性不等于难读。',
 'The scholar used the scholarship to continue her scholarly research.\n\n那位学者用奖学金继续她的学术研究。','scholar scholarly scholarship')
U=[['suit 相合、适合 → suitable','与用途、对象合得上'],['suitable 的否定、副词','unsuitable 不适合；suitably 以合适方式、达到适当程度']]
W('unsuitable','/ʌnˈsuːtəbl/','不适合的、不合宜的',
 '东西未必坏，只是放在这件事、这个人或这个时机里不合适：礼服可能很好，却不适合爬山。',
 'un- 不 + suitable 适合的；suitable 对应 suit + -able。否定的是与当前用途相合的关系，不一定否定东西本身的价值。',U,
 'unsuitable for children 不适合儿童，unsuitable for the task 不适合任务，an unsuitable choice 不合适的选择。',
 'unsuitable for；unsuitable to do；an unsuitable choice。',
 'unsuitable 不等于 useless 完全无用，也不自动等于 dangerous 危险；要补明对谁、什么用途不适合。',
 ('These shoes are unsuitable for walking on rough ground.','这双鞋不适合在崎岖地面行走。'),('The room was unsuitable for a large meeting.','那个房间不适合开大型会议。'))
W('suitably','/ˈsuːtəbli/','合适地、适当地；达到应有程度地',
 '衣服与场合合上，反应与消息相称；有时是认真说适当，有时略带打趣说果然足够惊讶。',
 'suitable + -ly，-able 形容词的副词形式变为 -ably。不是 suit + ably 能干地两个词。',U+[['suitable → suitably','合适性质 → 以合适方式、适当程度']],
 'suitably dressed 穿着得体，suitably qualified 资格合适的，suitably impressed 受到应有程度的震撼，常带轻松语气。',
 'suitably dressed；suitably qualified；suitably impressed。',
 'suitably impressed 不能机械译适当地被印下；impressed 在这里是留下深刻印象。suitably 强调符合情境，不只是程度高。',
 ('Please arrive suitably dressed for the ceremony.','请穿着适合典礼的服装到场。'),('The children were suitably impressed by the enormous model.','孩子们看到巨大的模型，果然大受震撼。'))
R('B4259','与人、用途和场合相合','SUITABLE：不问东西绝对好坏，先问配不配','suitable → suitably；unsuitable 否定适合关系。',
 '同一双鞋适合室内，却不适合登山。把用途说清楚，适合、不适合就不会变成空泛的好、坏。',
 'suit + -able → suitable；suitable → suitably；un- + suitable。',
 [['相合、相应方式与不合','suitable · suitably · unsuitable']],
 'unsuitable 不等于无用；suitably 要看场合、程度；-able 到副词变 -ably。',
 'He was suitably dressed for dinner, but his shoes were unsuitable for the muddy path.\n\n他的晚餐穿着得体，但鞋子不适合走泥路。','suitable suitably unsuitable')
T=[['名词 strip 的路线','长条；联系 stripe 或中古低地德语相应形式，远源未定'],['动词 strip 的旧英语路线','剥夺、脱去 → 去覆盖层、取走'],['现代专门组合','stripper/striptease；outstrip 的快速前行路线另有争议']]
W('strip','/strɪp/','长条；地带；连环漫画；剥去、脱去；剥夺',
 '名词看形状，是窄长一条；动词看动作，把表面那层取掉，或把某人拥有的东西拿走。',
 '长条名词常联系 stripe 或中古低地德语 strippe；剥去动词接古英语剥夺、劫掠相关形式。两路可作形象联想，但不把全部历史压成先撕出一条布的故事。',T[:2],
 'a strip of paper 一条纸，a strip of land 一条地带，a comic strip 连环漫画，strip paint off 剥去油漆，strip someone of power 剥夺权力。',
 'a strip of paper；a comic strip；strip paint off；strip someone of。',
 'strip 长条与 stripe 条纹相关却不是同一个现代词；strip 除衣物外还可剥油漆、绝缘层、权利。stripped/stripping 双写 p。',
 ('Cut the paper into narrow strips.','把纸剪成细条。'),('The committee stripped him of his title.','委员会撤销了他的头衔。'))
W('stripper','英 /ˈstrɪpə/；美 /ˈstrɪpər/','剥除工具、脱漆剂等；脱衣舞表演者',
 '前面如果有 paint，通常是在去油漆；舞台人物语境则可能是脱衣舞表演者。都与去掉覆盖物有关，但对象不同。',
 'strip + -er，双写 p。-er 可指做动作的人、工具，也可指帮助去掉材料的药剂。',T[1:2]+[['strip + -er → stripper','去除覆盖物的人、工具、药剂；表演者']],
 'paint stripper 脱漆剂，a wire stripper 剥线钳，a stage stripper 脱衣舞表演者。',
 'paint stripper；a wire stripper；a stage stripper。',
 'stripper 不一律译脱衣舞者；电工工具语境的 stripper 不是人。striper 只有一个 p，可能说有条纹者，读音也不同。',
 ('The toolbox contained a wire stripper and a screwdriver.','工具箱里有剥线钳和螺丝刀。'),('The novel follows the life of a nightclub stripper.','小说讲述一位夜总会脱衣舞表演者的生活。'))
W('striptease','/ˈstrɪptiːz/','脱衣舞、逐渐脱衣的挑逗性表演',
 'strip 是脱去，tease 是逗引；合起来强调借逐步脱衣制造期待的舞台表演形式。',
 'strip + tease，两个动词材料合成表演名词，也能转作表演这种舞的动词。tease 最后读 /z/，不是 /s/。',T[1:2]+[['strip + tease → striptease','脱去 + 逗引 → 特定舞台表演形式']],
 'a striptease act 脱衣舞节目，a history of striptease 脱衣舞表演史，perform a striptease 表演脱衣舞。',
 'a striptease act；perform a striptease；the history of striptease。',
 'striptease 是一种表演名称，不等于所有脱衣动作；换衣服通常直接说 change clothes 或 get undressed。',
 ('The book includes a chapter on the history of striptease.','书中有一章介绍脱衣舞表演的历史。'),('The film follows a performer preparing a striptease act.','电影跟拍一位演员准备脱衣舞节目的过程。'))
W('outstrip','/ˌaʊtˈstrɪp/','超过、超越；把……甩在后面',
 '两边都在往前，一边快得把另一边留在后面；需求跑过供应、成绩超过预期，都可 outstrip。',
 'out- 胜过 + 旧的快速移动 strip 是一种解释，也有联系 outstrike 等形式的看法，来路不完全确定。不是比别人脱得更多；那只是后来可作的双关。',
 [['out- + 旧快速前行形式；具体分析有争议','跑得更快、越过'],['英语 outstrip','实际速度或数量、成就超过']],
 'demand outstrips supply 需求超过供给，outstrip expectations 超过预期，outstrip competitors 超越竞争者。',
 'outstrip supply；outstrip expectations；outstrip competitors。',
 'outstrip 不一定是竞争胜负：成本增长超过收入也可说 costs outstrip income。outstripped/outstripping 双写 p。',
 ('Demand for the tickets quickly outstripped supply.','门票需求很快超过了供应。'),('Her progress outstripped all our expectations.','她的进步超出了我们所有人的预期。'),sources=['https://en.wiktionary.org/wiki/outstrip#English','https://www.etymonline.com/word/outstrip'])
R('B4241','窄长形状、剥去动作与超越词的不同历史','STRIP：长条看形状，剥去看动作，outstrip 另辨','strip → stripper/striptease；airstrip 是窄长跑道；outstrip 超过，不靠脱衣义解释。',
 '形状和动作可以互相帮助记忆，但历史上名词、动词和快速前行组合不宜硬画为单线。',
 '长条名词的低地德语、stripe 相关路线；旧英语剥夺动词 → strip；-er、tease；outstrip 快速前行相关的多种解释。',
 [['长条与剥除动作','strip · airstrip'],['执行角色与表演','stripper · striptease'],['超越','outstrip']],
 'stripper 看上下文可为工具或人；striptease 不等于普通换衣；outstrip 不从比别人脱更多确定演化。',
 'The factory’s output outstripped demand for the metal strips.\n\n工厂金属条的产量超过了需求。','strip airstrip stripper striptease outstrip')
I=[['拉丁 interpres → interpretārī','中间人、传达者 → 解释、转达意思'],['法语相关形式 → 英语 interpret 等','解释、理解、口译；名词、人物词各有借入路线'],['现代专门用法','艺术演绎；计算机解释执行']]
W('interpret','英 /ɪnˈtɜːprɪt/；美 /ɪnˈtɜːrprɪt/','解释、解读、理解为；口译；演绎作品',
 '把不明白的信号、话、动作转成可理解的意思；口译是帮两边跨语言理解，艺术家也会用表演给作品一种理解。',
 '经法语接拉丁 interpretārī，来自 interpres 中间人、传达者。inter- 在中间较清楚，后半远源有贸易、引导等不同解释，不虚构现代英语 pret 小词。',I,
 'interpret the results 解读结果，interpret silence as agreement 把沉默理解为同意，interpret for someone 为人作口译，interpret a role 演绎角色。',
 'interpret the results；interpret A as B；interpret for；interpret a role。',
 'interpret 不保证理解正确；I interpreted it as approval 只是说我这样理解。translate 常用于书面翻译，interpret 常指现场口语或手语传达，也有更广解释义。',
 ('How do you interpret these results?','你怎样解读这些结果？'),('She interpreted for the visitors during the meeting.','开会时，她为来访者作口译。'),sources=['https://en.wiktionary.org/wiki/interpret#English','https://www.etymonline.com/word/interpret'])
W('interpretation','英 /ɪnˌtɜːprəˈteɪʃən/；美 /ɪnˌtɜːrprəˈteɪʃən/','解释、解读；口译；艺术演绎方式',
 '同一段沉默，有人当同意，有人当犹豫；每一种赋予的意思都是一种 interpretation。演奏同一首曲子也可有不同处理。',
 '经法语接拉丁 interpretātiō，动作名词。现代对应 interpret + -ation；历史有自己的借入路线，不必把所有义写成英语临时加尾巴。',I+[['interpretātiō → interpretacion → interpretation','解释过程、理解结果；现代对应 interpret + -ation']],
 'an interpretation of the data 数据解读，open to interpretation 可有不同解释，simultaneous interpretation 同声传译，her interpretation of the song 她对歌曲的演绎。',
 'an interpretation of；open to interpretation；simultaneous interpretation。',
 'interpretation 是对意思的理解、呈现，不等于 objective fact 客观事实；同声传译中的 interpretation 又是跨语言传达活动。',
 ('The evidence allows more than one interpretation.','证据可以有不止一种解读。'),('Her interpretation of the song was quiet and restrained.','她演绎这首歌时安静而克制。'))
W('interpreter','英 /ɪnˈtɜːprɪtə/；美 /ɪnˈtɜːrprɪtər/','口译员、手语传译员；解释者；计算机解释器',
 '在人之间传达话语或手语的是 interpreter；电脑中承担读取、执行程序指令这类工作的程序，也借用解释者这个角色名。',
 '接法语、晚期拉丁相应人物词，现代对应 interpret + -er。不是所有 -er 都说明只在英语里首次新造，计算机义是后来的角色转用。',I+[['法语、拉丁人物词 → interpreter','解释、传译的人；现代对照 interpret + -er'],['计算机角色用法','负责解释、执行指令的程序']],
 'a conference interpreter 会议口译员，a sign language interpreter 手语传译员，a language interpreter 程序语言解释器。',
 'a conference interpreter；a sign language interpreter；a language interpreter。',
 'interpreter 不只口头说话者，手语也在内；计算机解释器的内部可结合编译等步骤，不能把字面逐行解释当作所有实现的完整定义。',
 ('A sign language interpreter stood beside the speaker.','一位手语传译员站在发言人旁边。'),('The interpreter reported an error in the command.','解释器报告命令中有一个错误。'))
W('reinterpret','英 /ˌriːɪnˈtɜːprɪt/；美 /ˌriːɪnˈtɜːrprɪt/','重新解读、重新演绎',
 '材料可能没换，但换了背景、证据或表演角度，再把它读出另一层意思。',
 're- 再次 + interpret。可以重新研究同一批资料，也可以用新风格演旧作品，不等于把它错解。',I+[['re- + interpret → reinterpret','再次赋予解释、以新方式演绎']],
 'reinterpret the evidence 重新解读证据，reinterpret a classic 重新演绎经典，reinterpret the past 重新解释过去。',
 'reinterpret the evidence；reinterpret a classic；reinterpret the past。',
 'reinterpret 说再解释，misinterpret 说解释错；新解释不保证正确，也不必故意推翻原来的一切。',
 ('New evidence led historians to reinterpret the event.','新证据使历史学家重新解读那件事。'),('The director reinterpreted the classic play for a modern audience.','导演为现代观众重新演绎了那部经典戏剧。'))
R('B4467','在材料与理解之间传达、解释意思','INTERPRET：把话、信号、作品带到可理解的一边','interpret → interpretation/interpreter；reinterpret 重新解释，misinterpret 解释错。',
 '从中间传达者的角色看，口译、数据解读和演绎作品就能连起来。理解仍可能有不同版本或错误，词本身不保证解释为真。',
 'interpres → interpretārī → interpret；interpretātiō、人物词等各自借入；re-/mis- + interpret。',
 [['解释、结果与传达角色','interpret · interpretation · interpreter'],['重新解读与误解','reinterpret · misinterpret']],
 '后半远源有争议；interpreter 可是手语传译员或程序；interpretation 可能只是看法；reinterpret 不等于 misinterpret。',
 'The interpreter explained the first interpretation, then helped us reinterpret the evidence.\n\n传译员解释了最初的解读，又帮助我们重新理解证据。','interpret interpretation interpreter reinterpret misinterpret')
if __name__=='__main__':save('continuation_20261030_hz',ROOTS,WORDS)
