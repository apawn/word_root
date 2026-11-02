"""Regard, employable, behaviorism and violence: common abstract extensions."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
G=[['古法语 regarder、reguarder → 中古英语 regarden → regard〔动词〕','留意看、看待；后有尊重、认为'],['法语 regard → 中古英语 regard、regarde → regard〔名词〕','注意、看待 → 关心、敬重；方面、问候等']]
def GH(f,m):return G+[[f,m]]
W('regard','英 /rɪˈɡɑːd/；美 /rɪˈɡɑːrd/','看待、认为；注视；关心、敬重；方面；问候〔复数〕',
 '先把目光、心思放到某处，再看“你把它当什么”。放在心上可变成关心、敬重；in this regard 则把讨论目光限定到这一方面。',
 '经古法语 regarder、reguarder 与名词 regard 的相应路径；更早的 garder 有看守、留意的日耳曼语背景。re- 在旧词中带加强等作用，不机械译成再次守卫。',G,
 'regard A as B 把 A 看作 B，have regard for 顾及，hold someone in high regard 敬重某人，in this regard 在这方面，Best regards 信末问候。',
 'regard A as B；have regard for；in this regard；with regard to；Best regards。',
 'regard as 后不再套一个多余的 as；regard 可作动词，regarding 常是关于。regards 复数可问候，但单数 regard 不一般独立说一声问候。',
 ('They regard her as a reliable colleague.','他们认为她是一位可靠的同事。'),('The report says little in this regard.','报告在这方面没说多少。'))
W('regarding','英 /rɪˈɡɑːdɪŋ/；美 /rɪˈɡɑːrdɪŋ/','关于、就……而言；正在看待、注视〔分词〕',
 '把目光转到某个话题：regarding your question，就是下面说的话针对你的问题。',
 'regard + -ing 的分词形式发展出介词用法，表示在考虑、涉及某事方面。现代句中常已是介词，不必每次译成正在注视。',GH('regard + -ing → regarding','看待、考虑 → 引出相关话题的介词'),
 'regarding your request 关于你的请求，information regarding the project 项目相关信息。正式邮件常见。',
 'regarding your request；information regarding；questions regarding。',
 'regarding 后直接接对象，with regard to 才接 to；不要混成 regarding to。regarding 与 about 常可替换，但语气更正式。',
 ('I am writing regarding your application.','我写信是想谈谈你的申请。'),('Please contact us with any questions regarding the schedule.','关于日程有任何问题，请联系我们。'))
W('regardless','英 /rɪˈɡɑːdləs/；美 /rɪˈɡɑːrdləs/','不顾、不受影响地；不管怎样',
 '知道有某个条件、阻力，却不让它改变接下来的决定；有时也批评根本不顾后果。',
 'regard 关注、顾及 + -less 没有。现代常作副词；regardless of 后接那个不影响结果的条件。',GH('regard + -less → regardless','不予顾及 → 不管怎样、不受其影响'),
 'regardless of age 不论年龄，regardless of cost 不计成本，carry on regardless 不管怎样继续。',
 'regardless of；regardless of age；carry on regardless。',
 'regardless of 后接名词或名词性结构，although 常引句子；不顾成本与不受年龄影响，褒贬由具体场景决定。',
 ('Everyone is welcome, regardless of age.','不论年龄，所有人都欢迎来。'),('The rain was heavy, but they carried on regardless.','雨很大，但他们还是照常继续。'))
W('disregard','英 /ˌdɪsrɪˈɡɑːd/；美 /ˌdɪsrɪˈɡɑːrd/','不理会、忽视；不顾',
 '信息、规则就在眼前，却不把它算进自己的行动里；可以故意不理，也可在要求对方别把旧消息当回事。',
 'dis- 否定、逆转 + regard 顾及，形成不理会的动词，也可作不顾的名词。',GH('dis- + regard → disregard','不予考虑、不顾及'),
 'disregard a warning 不理警告，disregard the previous email 忽略上一封邮件，a disregard for safety 不顾安全。',
 'disregard a warning；disregard the previous email；a disregard for。',
 'disregard 常比 overlook 更有不把它当回事的感觉；overlook 还可是不小心漏看。disregard 具体动作、态度，regardless 常修饰不受某条件影响。',
 ('Please disregard the date in my previous message.','请忽略我上一条消息中的日期。'),('The review criticized the company’s disregard for safety.','评论批评了公司不顾安全的态度。'))
R('B3717','把某事放进目光、考虑与关心的范围','REGARD：看向它、怎样看它、是否把它放在心上','regard → regarding；regardless、disregard 接不顾及这一支，区别句法与语气。',
 '注视、看待、顾及、敬重可以从注意放在哪里串起；in this regard 是在这一方面，不用把每个义项都硬翻成再次守护。',
 '法语 regarder、regard 分别接入英语动词、名词；regard + -ing/-less；dis- + regard。',
 [['注意、看待与引话题','regard · regarding'],['不顾及、不受影响','regardless · disregard']],
 'regarding 后无 to，with regard to 有 to；regardless of 后接对象；disregard/overlook 故意不顾与漏看可不同。',
 'Regarding the schedule, please disregard my earlier message.\n\n关于日程，请忽略我之前那条消息。','regard regarding regardless disregard')
W('employable','/ɪmˈplɔɪəbəl/','具备就业条件的、能被雇用的',
 '拥有让雇主愿意考虑聘用的技能、条件。说具备机会和能力，不是已经拿到工作。',
 'employ + -able；employ 经法语 employer 接拉丁 implicāre 等旧路径，现代 employable 说可被雇用，不要硬译成可被缠绕。',
 [['法语 employer → employ','使用、雇用'],['employ + -able → employable','具备被雇用的条件']],
 'become more employable 提升就业能力，employable skills 有助就业的技能，highly employable 很有就业竞争力。',
 'become more employable；highly employable；employable skills。',
 'employable 能被雇用，employed 已受雇，unemployed 未就业；一个人可以暂未就业却具备很强的就业能力。',
 ('The course aims to make graduates more employable.','这门课旨在提高毕业生的就业能力。'),('Her language skills make her highly employable.','她的语言能力使她很有就业竞争力。'))
R('B4148','雇用双方与可就业条件','EMPLOY：把人的工作能力用到岗位上','employ → employer、employee；employable 再看能否被聘用。',
 'employer 提供岗位、雇人，employee 被雇。employable 是能力、条件，并不等于已经在职。',
 '法语 employer → employ；employ + -er/-ee/-able，人物和被动可能性分开。',
 [['雇用动作与双方','employ · employer · employee'],['就业条件','employable']],
 'employer 雇主、employee 雇员；employable 不保证 employed；-able 不等于过去分词。',
 'The employer values skills that make people more employable.\n\n这位雇主看重能提高就业能力的技能。','employ employer employee employable')
BE=[['behave → behavior','举止、行事 → 行为、表现'],['behavior + -ism/-ist','以行为研究为核心的理论名称及其研究者称呼']]
W('behaviorism','英 /bɪˈheɪvjərɪzəm/；美 /bɪˈheɪvjərɪzəm/','行为主义〔心理学理论取向〕',
 '研究心理时，先盯住能观察、记录的行为，以及行为怎样受环境和学习影响；不是在赞美某个人表现乖。',
 'behavior + -ism，-ism 命名理论取向。英式常拼 behaviourism；不同流派对内部过程的看法不全相同，不缩成所有行为主义都否认人有想法。',BE,
 'the history of behaviorism 行为主义史，the rise of behaviorism 行为主义的兴起，an introduction to behaviorism 行为主义入门。',
 'the history of behaviorism；the rise of behaviorism；an introduction to behaviorism。',
 'behavior 行为，behavioral 与行为有关，behaviorism 特定理论取向；不是所有观察行为的研究都自动属于行为主义。',
 ('The chapter introduces the main ideas of behaviorism.','这一章介绍行为主义的主要思想。'),('We compared behaviorism with other approaches to learning.','我们比较了行为主义与其他学习研究取向。'))
W('behaviorist','英 /bɪˈheɪvjərɪst/；美 /bɪˈheɪvjərɪst/','行为主义者；行为主义的',
 '人物名词指采取行为主义取向的人；修饰观点时，就是从这种理论出发看问题。',
 'behavior + -ist，和 behaviorism 构成理论、人物的对应。英式也见 behaviourist。',BE[:1]+[['behavior + -ist → behaviorist','采用行为主义取向的人；相关的']],
 'a behaviorist psychologist 行为主义心理学家，a behaviorist approach 行为主义取向，behaviorist theories 行为主义理论。',
 'a behaviorist psychologist；a behaviorist approach；behaviorist theories。',
 'behaviorist 接特定理论，behavioral 范围更宽；behavioral research 研究行为，不一定宣称采用行为主义。',
 ('The lecturer described herself as a behaviorist.','讲师说自己是一位行为主义者。'),('The essay examines a behaviorist approach to language learning.','文章考察了一种研究语言学习的行为主义取向。'))
R('B3017','行为、相关性质与行为主义理论','BEHAVIOR：做出来的表现；-ism 再命名一种研究取向','behavior → behavioral、misbehavior；behaviorism、behaviorist 放在一起分理论、人物。',
 '日常表现好坏与心理学行为主义是不同层面。不是看到 behavioral 就自动判为行为主义。',
 'behave → behavior；behavior + -al/-ism/-ist；mis- + behavior；英式 behaviour 保留 u。',
 [['行为与评价','behavior · behavioral · misbehavior'],['理论与人物','behaviorism · behaviorist']],
 'behavioral 涉及行为较广，behaviorist 指向理论取向；behaviorism 不等于行为乖巧。',
 'The behaviorist studied how behavior changed during learning.\n\n这位行为主义者研究行为在学习过程中怎样变化。','behavior behavioral misbehavior behaviorism behaviorist')
W('violence','/ˈvaɪələns/','暴力、强力侵害；猛烈、剧烈',
 '人与人之间以力量伤害、压制，叫 violence；风暴、爆炸等猛烈到让人感到冲击，也可借用同一词。',
 '中古英语 violence 借古法语 violence，上接拉丁 violentia，由 violēns、violentus 的猛烈、强力含义接抽象名词。不是 violin 小提琴或 violet 紫罗兰的随意缩写。',
 [['拉丁 violentia → 古法语 violence → 中古英语 violence','强力、猛烈、暴力'],['英语 violence','暴力侵害；自然力量的猛烈']],
 'domestic violence 家庭暴力，an act of violence 暴力行为，the violence of the storm 风暴的猛烈，nonviolence 非暴力立场、方式。',
 'an act of violence；domestic violence；the violence of the storm。',
 'violent 强烈、暴力的形容词，violence 名词；不同专业文本对暴力的范围可能不同，读搭配确认是人际侵害还是自然力量。',
 ('The novel explores the effects of violence on a family.','小说探讨暴力对一个家庭的影响。'),('We were surprised by the violence of the storm.','风暴的猛烈程度让我们吃惊。'))
R('B3370','暴力与猛烈力量、非暴力','VIOLENCE：力量强烈到造成伤害、压制或巨大冲击','violence 与 nonviolence 对看；前者是暴力、猛烈，后者是否定暴力的方式、立场。',
 '不是所有强烈感情都自然叫 violence；风暴义与人际侵害义靠搭配区分。',
 '拉丁 violentia → 法语 violence → 英语 violence；non- + violence → nonviolence。',
 [['力量与侵害','violence'],['否定暴力的方式','nonviolence']],
 'violence 名词、violent 形容词；nonviolence 并不等于不采取任何行动。',
 'The book compares violence and nonviolence as responses to conflict.\n\n这本书比较了面对冲突时的暴力与非暴力方式。','violence nonviolence')
if __name__=='__main__':save('continuation_20261030_dg',ROOTS,WORDS)
