"""Productive, tool, branch and enforce: results, means, divisions and execution."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
P=[['拉丁 prōdūcere、product- → productīvus、法语 productif 等 → productive','带出来、产生 → 能产出、能带来结果的'],['英语前后缀派生','productively 有成果地；unproductive 无成果；counterproductive 适得其反；reproductive 生殖、复制相关']]
W('productively','/prəˈdʌktɪvli/','有成果地、有成效地',
 '时间花了，事情也真往前推进了；不是只看人忙不忙，而是有没有有用结果。',
 'productive 有成果的 + -ly，副词修饰使用时间、工作、讨论等动作。',P[:1]+[['productive + -ly → productively','以能带来成果的方式']],
 'use time productively 有效利用时间，work productively 有成效地工作，discuss productively 有建设性地讨论。',
 'use time productively；work productively；spend the morning productively。',
 'productively 不等于 constantly 不停地；休整后更有成果也可以叫 working productively。',
 ('We used the waiting time productively.','我们有效利用了等待时间。'),('The two teams worked productively together.','两个团队合作得很有成效。'))
W('unproductive','/ˌʌnprəˈdʌktɪv/','无成果的、成效低的；不再能产新词的〔语言学〕',
 '忙了半天，没产生想要的进展；像对着空地撒力气，却没收成。',
 'un- 不 + productive，否定产出、成效；语言学也用来形容不再活跃产生新形式的构词模式。',P[:1]+[['un- + productive → unproductive','缺少有用产出；不活跃产新形式']],
 'an unproductive meeting 没成果的会议，unproductive work 成效低的工作，an unproductive argument 无益争论。',
 'an unproductive meeting；an unproductive argument；unproductive work。',
 'unproductive 没推进，counterproductive 反把事情往坏处推；一下午没完成任务与越催越乱，程度和方向不同。',
 ('The meeting was long and unproductive.','会议又长又没成果。'),('They spent hours in an unproductive argument.','他们在无益争论中耗了几个小时。'))
W('counterproductive','英 /ˌkaʊntəprəˈdʌktɪv/；美 /ˌkaʊntərprəˈdʌktɪv/','适得其反的、产生反效果的',
 '本想催快，结果把人催乱、做得更慢；不只是没帮上忙，而是把目标往反方向推。',
 'counter- 对抗、相反 + productive，整体表示产生与所希望相反的效果。不是 counter 柜台产出的东西。',P[:1]+[['counter- + productive → counterproductive','效果与目标相反']],
 'a counterproductive policy 适得其反的政策，counterproductive pressure 反起坏作用的压力，prove counterproductive 结果适得其反。',
 'prove counterproductive；counterproductive pressure；a counterproductive approach。',
 'unproductive 可以只是没有成果，counterproductive 更突出坏了原本想办好的事；是否反效果要结合目标看。',
 ('Constant criticism can be counterproductive.','不断批评可能适得其反。'),('Rushing the repair proved counterproductive.','抢着赶工修理，结果反而坏了事。'),
 sources=['https://www.etymonline.com/word/counterproductive','https://en.wiktionary.org/wiki/counterproductive#English'])
W('reproductive','/ˌriːprəˈdʌktɪv/','生殖的、繁殖的；复制、再现相关的',
 '产生下一代，是生命意义的再产生；艺术、复制语境里也可说把原物再现出来的能力。',
 're- 再 + productive，与 reproduce、reproduction 词族对应。生物生殖义已经固定，不能每次只按再次高效工作来译。',P[:1]+[['re- + productive → reproductive','再产生、复制；生殖繁殖相关']],
 'reproductive behaviour 繁殖行为，reproductive cycle 生殖周期，reproductive art 复制、再现性艺术〔特定语境〕。',
 'reproductive behaviour；reproductive cycle；reproductive success。',
 'reproductive 生殖、复制相关，productive 高产或有成果；reproductive success 说繁殖成功，不是办公室业绩。',
 ('The documentary explains the birds’ reproductive behaviour.','纪录片解释了这些鸟的繁殖行为。'),('The species has a short reproductive cycle.','这个物种的繁殖周期很短。'))
R('B4516','产生结果，再问结果多少、方向对不对','PRODUCTIVE：做出来有用结果','productive → productively、productivity；unproductive 无成果；counterproductive 反效果；reproductive 接再产生、繁殖。',
 '一忙到底不等于有成效；没有帮助和帮倒忙也不同。reproductive 则转到复制、繁殖的固定语义分支。',
 'prōdūcere、product- → productive；+ -ly、-ity；un-/counter-/re- + productive。',
 [['产出性质、方式与效率','productive · productively · productivity'],['没成果与反效果','unproductive · counterproductive'],['再产生与繁殖','reproductive']],
 'unproductive/counterproductive 没推进与倒退；productive/reproductive 有成果与生殖复制相关。',
 'Pressure that makes a productive team less effective is counterproductive.\n\n如果压力让一个有成效的团队效率下降，它就起了反作用。','productive productively productivity unproductive counterproductive reproductive')
T=[['古英语 tōl → 中古英语 tool、tol → tool','帮人完成事情的器具；与制作、准备词族有关'],['实物到抽象手段','锤子、软件、思考方法，甚至被人利用的人'],['组合与再装备','toolkit；tooled 用工具加工的；retool 重新配置工具、调整方案']]
W('tool','/tuːl/','工具、手段；被利用的人；用工具加工、配置工具',
 '手直接做不方便，就借一样东西把事做成；电脑程序、分析方法也可充当这种“帮手”。',
 '继承古英语 tōl，与古老制作、准备词族有关。现代不拆成 too 太 + l；名词后来可转成加工、配置工具等动词。',T,
 'a useful tool 有用工具，the tools of the trade 行业工具，a learning tool 学习工具，a tool of powerful interests 被强势利益方利用的人。口语叫人 a tool 还可能是骂人蠢、讨厌。',
 'a useful tool；the tools of the trade；a learning tool；tool up。',
 'tool 不限手持铁器；instrument 也可工具、仪器，但特定固定名称不能随意互换。称人为 a tool 常有贬意。',
 ('A dictionary is a useful learning tool.','词典是一种有用的学习工具。'),('He chose the right tool for the job.','他为这项工作选对了工具。'),
 sources=['https://www.etymonline.com/word/tool','https://en.wiktionary.org/wiki/tool#English'])
W('toolkit','/ˈtuːlkɪt/','工具包、成套工具；一套方法或软件工具',
 '把做某类事情要用的几样东西配成一套；不只指外面的包，还常指里面整套装备或方法。',
 'tool 工具 + kit 成套用品，两个名词并列组合；可以是修车包，也可以是写程序、解决问题的一套资源。',T[:1]+[['tool + kit → toolkit','为任务配齐的一套工具、方法']],
 'a repair toolkit 维修工具包，a software toolkit 软件工具包，a teaching toolkit 教学资源与方法包。',
 'a repair toolkit；a software toolkit；a teaching toolkit。',
 'toolkit 侧重成套、为任务配置，toolbox 字面侧重装工具的箱子，但抽象用法会重叠；不能说所有 toolkit 都必须有实物袋。',
 ('She keeps a small toolkit in the car.','她在车里放着一套小工具。'),('The workshop gave teachers a practical toolkit for group activities.','工作坊给老师提供了一套组织小组活动的实用方法。'))
W('tooled','/tuːld/','用工具加工的；压制、刻制装饰纹样的',
 '皮面上的纹样不是画笔随便涂上去，而是借工具压、刻加工；词选中的是加工方式。',
 'tool 动词 + -ed 的分词、形容词，接工具加工一支；不是 too 很 + led 引导。',T[:2]+[['tool + -ed → tooled','经工具加工、带压刻纹样']],
 'tooled leather 压花、雕花皮革，a tooled cover 压纹封面，finely tooled decoration 精细工具加工的装饰。',
 'tooled leather；a tooled cover；finely tooled decoration。',
 'tooled 接工艺，不等于 printed 印刷；tooled up 则可说配齐工具等，需看有无 up 与具体语境。',
 ('The book has a tooled leather cover.','这本书有一个压纹皮封面。'),('The belt is decorated with finely tooled patterns.','皮带饰有精细加工出的纹样。'))
W('retool','/ˌriːˈtuːl/','重新配置工具、改装生产设备；调整改造',
 '工厂换做另一种产品，先得换一套工装；借到方案、团队，就是把做事的配置重新调一遍。',
 're- 再 + tool 动词，早期可重新用工具加工，后常说工厂重新装备，再引申调整组织、计划。',T[:2]+[['re- + tool → retool','重新加工、配工具；调整配置']],
 'retool a factory 改装工厂设备，retool a strategy 调整策略，retool for a new product 为新产品重配设备。',
 'retool a factory；retool a strategy；retool for。',
 'retool 重新改造做事的装备、配置，repair 可只修坏的东西；改装不必原设备已经损坏。',
 ('The factory retooled to make smaller engines.','工厂改装设备，转而生产较小的发动机。'),('The team retooled its strategy after the trial.','试行后，团队调整了策略。'))
R('B3260','借一样东西，把手头的事做成','TOOL：实物器具，也可是一套方法','tool → tooled、retool；toolkit、toolbox、toolset 成套配置；toolbar、tooltip 接软件工具界面。',
 '工具可以有形，也可以是程序、方法；说某个人是别人的 tool，往往是说他被利用，而非夸他有用。',
 'tōl → tool；tool + kit/box/set/bar/tip；tool + -ed；re- + tool。',
 [['基础、加工与重配','tool · tooled · retool'],['成套装备与界面','toolkit · toolbox · toolset · toolbar · tooltip']],
 'toolkit/toolbox 成套工具与箱体、抽象用法交叉；retool/repair 改装重配与维修。',
 'The toolkit contains the tools needed to retool the small workshop.\n\n工具包里配有改装这间小作坊所需的工具。','tool tooled retool toolkit toolbox toolset toolbar tooltip')
B=[['晚期拉丁 branca 等 → 古法语 branche → 英语 branch','足印、爪等旧材料到枝条名称；更早来源未定'],['树枝状关系引申','主体分出的支路、分支、分店、学科'],['branch + -ed → branched','有分支、分叉的']]
W('branch','英 /brɑːntʃ/；美 /bræntʃ/','树枝；支路、分支、分店；分叉、拓展',
 '一根主干旁边分出一条，分出的那条还可再分；公司分店、知识分科也借这张树形图。',
 '经古法语 branche 接晚期拉丁 branca 的爪、足印等材料，具体更远来源未定；爪形到枝形是解释线索，不臆造第一个命名者的故事。',B,
 'a tree branch 树枝，a bank branch 银行分行，a branch of science 科学分支，branch off 分岔出去，branch out 拓展新领域。',
 'a branch of；a local branch；branch off；branch out。',
 'branch 强调从主体分出，root 是根；计算机 branch 也借分支意象，不一定真复制出一个完整独立系统。',
 ('A bird landed on a low branch.','一只鸟落在低处的树枝上。'),('The company opened a new branch in the city.','公司在城里开了一家新分店。'),
 sources=['https://www.etymonline.com/word/branch','https://en.wiktionary.org/wiki/branch#English'])
W('branched','英 /brɑːntʃt/；美 /bræntʃt/','有分支的、分叉的；已经分岔的',
 '一条线走着走着分成两条、多条，或一个结构长出侧枝；形容的是枝状结构。',
 'branch + -ed，可作过去式，也可作有分支的形容词；末尾 /t/ 接在 /tʃ/ 后面，不读额外 /ɪd/。',B[:2]+[['branch + -ed → branched','有分支；已经分岔']],
 'a branched structure 分支结构，branched roots 分叉的根，a highly branched network 高度分支的网络。',
 'a branched structure；branched roots；a highly branched network。',
 'branched 有分叉，broken 是断了；branching 也可描述正在分叉、分叉式结构，不保证枝条已断离主体。',
 ('The plant has a highly branched root system.','这种植物的根系分支很多。'),('The path branched near the old bridge.','小路在旧桥附近分岔了。'))
R('B2950','从主体分出去的一支','BRANCH：先画主干，再画侧支','branch 树枝 → 分店、学科、路线分支；branched 有分叉的结构。',
 '树根也可以是 branched，因为这里说形状，不是把根叫树枝。分支关系也不要求从主体彻底分离。',
 'branca → branche → branch；branch + -ed → branched；branch off/out 固定组合。',
 [['树枝与各种分支','branch'],['分支结构','branched']],
 'branched/broken 分叉与断裂；branch/root 分支与根，根本身也能分支。',
 'The main path branched into two smaller paths.\n\n主路分成了两条较小的路。','branch branched')
E=[['法语 enforcier 等 → 英语 enforce','强化、用力等旧义 → 使规定真正执行'],['英语常见派生','enforceable 可执行；enforceability 可执行性；enforcer 执行者']]
W('enforceable','英 /ɪnˈfɔːsəbəl/；美 /ɪnˈfɔːrsəbəl/','可强制执行的、能够落实执行的',
 '不是只把规定写在纸上，还能要求遵守、真正落实；可执行说的是约束能不能落地。',
 'enforce 使执行 + -able，表示能被执行。enforce 的 force 材料联系力量，但现代不必字字翻成动用武力。',E[:1]+[['enforce + -able → enforceable','能够落实、强制执行']],
 'an enforceable rule 可执行的规则，an enforceable agreement 有执行约束力的协议，legally enforceable 可依法执行的。',
 'an enforceable rule；an enforceable agreement；legally enforceable。',
 'enforceable 能执行，enforced 已在执行或被执行；写得清楚也不自动保证实际上能执行。',
 ('The team wanted a clear and enforceable rule.','团队想要一条清楚且能落实的规则。'),('The textbook asks whether the promise is legally enforceable.','教材提出一个问题：这项承诺是否可以依法强制执行。'))
W('enforceability','英 /ɪnˌfɔːsəˈbɪləti/；美 /ɪnˌfɔːrsəˈbɪləti/','可执行性、执行约束力',
 '把“这条规定到底能不能管用、要求遵守”当成一个性质来讨论；不等于执行人员有多强壮。',
 'enforceable 的相应 -ability 名词，对应 enforce + -ability。-able 的可行性质变成 ability 形式的抽象名词。',E[:1]+[['enforceable → enforceability','能够执行这一性质']],
 'the enforceability of a rule 规则的可执行性，question enforceability 质疑执行约束力，practical enforceability 实际可执行性。',
 'the enforceability of；question enforceability；practical enforceability。',
 'enforceability 是否具有可执行性质，enforcement 是实施执行过程；规则能执行与目前有没有被执行，是两个问题。',
 ('The report questions the rule’s practical enforceability.','报告质疑这条规则在实际中的可执行性。'),('The chapter discusses the enforceability of written promises.','这一章讨论书面承诺的执行约束力。'))
W('enforcer','英 /ɪnˈfɔːsə/；美 /ɪnˈfɔːrsər/','执行者、执法者；强硬执行人物、打手',
 '让别人照规矩办的人；在帮派故事里也可指靠威吓让人服从的打手，角色不能只看后缀就判断正邪。',
 'enforce + -er，做执行、强制遵守工作的人；体育等场景还可用来指承担强硬对抗角色的队员。',E[:1]+[['enforce + -er → enforcer','让要求得到执行的主体；特定强硬人物']],
 'a rule enforcer 规则执行者，a law enforcer 执法者，a gang’s enforcer 帮派打手。',
 'a rule enforcer；a law enforcer；a gang’s enforcer。',
 'enforcer 人物，enforcement 执行行为；enforcer 可以中性职业，也可带强硬威吓色彩，依修饰词判断。',
 ('The referee acts as the rule enforcer during the match.','裁判在比赛中负责执行规则。'),('The novel introduces him as the gang’s enforcer.','小说介绍他是帮派里负责威吓执行的打手。'))
R('B3049','让纸面要求真正得到遵守','ENFORCE：不只宣布，还要执行','enforce → enforcement；enforceable → enforceability；enforcer 执行者。',
 '把动作、过程、可执行性质和执行人物排开学。force 的力量材料不意味着每个执行行为都在使用武器。',
 'enforcier 等 → enforce；enforce + -ment/-able/-er；enforceable → enforceability。',
 [['执行动作与过程','enforce · enforcement'],['能否执行与相应性质','enforceable · enforceability'],['负责执行的人','enforcer']],
 'enforceability/enforcement 可执行性与实施过程；enforceable/enforced 能执行与已执行；enforcer 语气由角色语境定。',
 'The enforcer can apply the rule only if there is a clear way to enforce it.\n\n只有执行办法清楚，执行者才能落实这条规则。','enforce enforcement enforceable enforceability enforcer')
if __name__=='__main__':save('continuation_20261030_fm',ROOTS,WORDS)
