"""Defensive reactions, immunity, logging, knives and ordinary things."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
W('defensiveness','/dɪˈfensɪvnəs/','防御性、戒备；受质疑时急于自我辩护的反应',
 '别人一提问题，先感觉自己被攻击，赶紧解释、反击或关上话头；日常心理、人际语境常说这种护住自己的反应。',
 'defensive + -ness，性质名词；defensive 远接 defend 防卫词族。不是 defense 再加一个表示人的 -iveness。',
 [['defend → defensive','防卫 → 防御的、戒备自卫的'],['defensive + -ness → defensiveness','这种防御态度、反应']],
 'respond with defensiveness 带防御心回应，reduce defensiveness 减少戒备，a tone of defensiveness 自我辩护的语气。',
 'respond with defensiveness；reduce defensiveness；a tone of defensiveness。',
 'defensiveness 常聚焦态度和反应，defence 是防守、辩护本身；合理说明理由不一定就是过度防御，要看具体互动。',
 ('His defensiveness made the discussion more difficult.','他的戒备、自我辩护让讨论更难进行。'),('She answered the criticism without anger or defensiveness.','她回应批评时，既不生气，也不急着自我辩护。'))
R('B4258','防守性质、行事方式与人际防御反应','DEFENSIVE：护住自己，可能是战术，也可能是态度','defensive → defensively/defensiveness；前者性质，后两者分别说方式和反应状态。',
 '防守在球场可完全中性；在交谈中则常指怕被批评、急着护自己。不能把所有 defensive 都只翻成防御工事。',
 'defend 及相应历史词干 → defensive；defensive + -ly/-ness。',
 [['性质、方式与防御态度','defensive · defensively · defensiveness']],
 'defensiveness 不等于 defence 的所有意思；defensive tactics 可中性，defensive tone 常指戒备。',
 'He spoke defensively, and his defensiveness distracted us from the facts.\n\n他说话很戒备，这种急于自辩的态度让我们偏离了事实。','defensive defensively defensiveness')
I=[['拉丁 immūnis / immūnitās → 法语、英语相应词','免除义务、负担 → 豁免及其状态'],['医学与一般引申','对疾病的免疫保护；不受某种影响'],['现代派生','immunize/immunization；immunology；-s- 拼写变体 immunisation']]
W('immunity','/ɪˈmjuːnəti/','免疫力、免疫保护；豁免权；免受某事影响的状态',
 '身体对某种威胁有保护，和法律上某种义务、程序被豁免，都保留免于某事的共同感觉；不是任意情况下无敌。',
 '经法语 immunité 接拉丁 immūnitās，法律豁免背景较早；现代对应 immune 去 e + -ity。医学保护义是后来的专门发展。',I[:2],
 'immunity to a disease 对某病的免疫保护，diplomatic immunity 外交豁免，immunity from prosecution 免受起诉的相关豁免，acquired immunity 获得性免疫。',
 'immunity to；immunity from；diplomatic immunity；acquired immunity。',
 '免疫保护常针对具体对象，程度也不同；法律 immunity 也有具体适用范围，不能仅凭词义认定一个人完全不受任何法律约束。',
 ('The chapter compares different forms of immunity.','这一章比较不同形式的免疫。'),('The article explains the scope of diplomatic immunity.','文章解释外交豁免的范围。'),sources=['https://en.wiktionary.org/wiki/immunity#English','https://www.cdc.gov/vaccines/basics/explaining-how-vaccines-work.html','https://www.law.cornell.edu/wex/immunity'])
W('immunology','英 /ˌɪmjʊˈnɒlədʒi/；美 /ˌɪmjəˈnɑːlədʒi/','免疫学',
 '研究身体怎样识别、应对不同对象，以及这种系统怎样工作；不是只研究疫苗，也不只是问抵抗力强不强。',
 'immune 的词干 immun- + -ology 研究、学科。去掉 immune 末尾 e 后连接；学科词重音落在后半 /nɒl/、/nɑːl/。',I[:2]+[['immun- + -ology → immunology','研究免疫系统及相关过程的学科']],
 'a course in immunology 免疫学课程，an immunology laboratory 免疫学实验室，basic immunology 基础免疫学。',
 'a course in immunology；an immunology laboratory；basic immunology。',
 'immunology 是学科，immunity 是免疫状态，immunization 是获得相应保护的过程。三个名词不能只按中文免疫互换。',
 ('She took an introductory course in immunology.','她上了一门免疫学入门课。'),('The laboratory studies a basic question in immunology.','实验室研究免疫学中的一个基础问题。'))
W('immunisation','/ˌɪmjʊnaɪˈzeɪʃən/','免疫、预防接种〔immunization 的常见英式拼写〕',
 '看到 s 不必再学一种接种方式，它和 immunization 在常见医学语境里是同一个过程名词。',
 '接法语 immunisation 等形式，现代对应 immunise + -ation；-ise/-ize 相关拼写使名词出现 -isation/-ization 两种形式。',I+[['immunise + -ation → immunisation','与 immunization 对应的常见英式名词拼写']],
 'an immunisation programme 免疫接种项目，immunisation records 接种记录，routine immunisation 常规免疫接种。',
 'an immunisation programme；immunisation records；routine immunisation。',
 'immunisation/immunization 不是两种不同疫苗；vaccination 与它们的区别仍是接种动作和形成免疫保护的概念侧重。',
 ('The leaflet explains the school immunisation programme.','传单介绍学校免疫接种项目。'),('Please bring the child’s immunisation records to the appointment.','预约时请带上孩子的接种记录。'),sources=['https://en.wiktionary.org/wiki/immunisation#English','https://www.england.nhs.uk/long-read/nhs-vaccination-strategy/'])
R('B4049','从免除义务到免疫保护，以及相关学科、过程','IMMUNE：免于某种影响，但要问免于什么','immune → immunity；immunize → immunization/immunisation；immunology 是研究学科；autoimmune 另指定自身免疫相关方向。',
 '免除、保护是连接线。医学不是笼统无敌，法律也不是无条件免责；把保护对象、制度范围补出来，含义才完整。',
 'in- 不 + mūnus 服务、义务 → immūnis；immūnitās → immunity；immune + -ize；immun- + -ology；auto- + immune。',
 [['豁免、保护与状态','immune · immunity'],['使免疫及过程、拼写变体','immunize · immunization · immunisation'],['研究学科与自身方向','immunology · autoimmune']],
 'immunity 状态、immunology 学科、immunization 过程；-s-/-z- 常是拼写差异；autoimmune 不是自动使一切都免疫。',
 'The immunology course explains immunity before discussing immunization.\n\n免疫学课程先解释免疫，再讨论免疫接种。','immune immunity immunize immunization immunisation immunology autoimmune')
L=[['中古英语 logge/logg → log','原木；更早可能有北欧来源，细节不定'],['航海测速用木质浮块 → logbook → log','测速装置 → 航海日志 → 各类记录'],['另线 logarithm → log','数学对数的缩称，不从木头变来']]
W('log','英 /lɒɡ/；美 /lɑːɡ/','原木；日志、记录；伐木；记录；对数〔另路缩称〕',
 '木柴堆里是原木；系统报错时看的 log 是事件记录。记录义能接回航海：测速用木块的 log，再到记录航行数据的 logbook。',
 '原木接中古英语 logge 等，远源不定，可能有北欧相关词。日志从 logbook 截短，和旧航海测速装置相连；数学 log 却是 logarithm 的截短，另一路。',L,
 'a log fire 木柴火，a system log 系统日志，log the results 记录结果，log in 登录，log out 退出登录，log 10 数学对数表达。',
 'a log fire；a system log；log the results；log in；log out。',
 'log in 动词短语，login 常作名词或定语；logs 可是木头也可是多条记录。记录在 log 里不保证记录内容完整或正确。',
 ('They stacked the logs beside the stove.','他们把原木柴块堆在炉子旁。'),('The system logs every failed connection attempt.','系统记录每次失败的连接尝试。'),sources=['https://en.wiktionary.org/wiki/log#English','https://www.etymonline.com/word/log'])
W('logger','英 /ˈlɒɡə/；美 /ˈlɑːɡər/','伐木工；记录器、日志记录程序',
 '在林场做 logging 的是伐木工；程序里做 logging 的，则是帮你把事件写下来的记录器。',
 'log + -er，双写 g。两种常见角色分别接原木、伐木义和日志、记录义；-er 可以是人，也可以是程序、装置。',L[:2]+[['log + -er → logger','伐木者；日志记录角色']],
 'a timber logger 伐木工，a data logger 数据记录器，a temperature logger 温度记录器，a software logger 软件日志记录器。',
 'a timber logger；a data logger；a temperature logger。',
 'logger 不等于 log 记录本身；data logger 可是器材，也可是软件功能。看到 -er 不要直接补成人。',
 ('The logger recorded the room temperature every hour.','记录器每小时记录一次室温。'),('The documentary follows a team of loggers.','纪录片跟拍了一队伐木工。'))
W('weblog','英 /ˈweblɒɡ/；美 /ˈweblɑːɡ/','网络日志、博客〔较完整的早期名称〕',
 '把持续更新的记录放到网上，web + log 形成网络日志；后来短到 blog 更普遍。',
 'Web 网络 + log 日志，取记录义，不是网上的一根木头。blog 是从 weblog 进一步截短、重新切分的形式。',L[1:2]+[['Web + log → weblog → blog','网上持续发布的日志式页面或网站']],
 'keep a weblog 写网络日志，a personal weblog 个人博客，a travel weblog 旅行博客；现代通常直接说 blog。',
 'keep a weblog；a personal weblog；a travel weblog。',
 'weblog 不是所有 website 网站的同义词，强调持续更新的日志式发布；今天博客也未必只写私人日记。',
 ('She kept a weblog during her journey.','旅行期间，她持续写网络日志。'),('The old website linked to several personal weblogs.','旧网站链接了几个个人博客。'))
W('logjam','英 /ˈlɒɡdʒæm/；美 /ˈlɑːɡdʒæm/','原木拥塞；僵局、积压堵塞',
 '一根根木头在河里挤成一堵，后面的都过不去；事情积压、各方卡住，也能叫 logjam。',
 'log 原木 + jam 挤塞。实物漂木拥塞是最直观入口，后来比喻工作、谈判、流程无法推进。',L[:1]+[['log + jam → logjam','漂运木材堵住 → 进程被积压、僵住']],
 'break the logjam 打破僵局，a legislative logjam 立法僵局，a logjam of applications 申请积压。',
 'break the logjam；a legislative logjam；a logjam of applications。',
 'logjam 的 jam 不是果酱；比喻里也不要求真的有木头。backlog 强调待处理积压，logjam 更突出积压使进展堵住。',
 ('The agreement finally broke the logjam.','协议终于打破了僵局。'),('The office faced a logjam of unprocessed applications.','办公室面对堵住流程的大量未处理申请。'))
R('B3443','原木、航海记录路线与堵塞比喻','LOG：一根木头能连到航海日志，数学缩称另分','log → logger；Web + log → weblog/blog；logjam 是原木拥塞比喻。backlog、changelog 又分别看积压和变更记录。',
 '从木块测速到记录航行，再到一般日志，这条历史比只背日志直观；对数 log 则缩自另一个长词。',
 'logge → 原木 log → 测速 log / logbook → 记录 log；log + -er/jam；Web + log；logarithm → log 另线。',
 [['原木、记录与记录角色','log · logger'],['网络、变更记录与积压','weblog · changelog · backlog · logjam']],
 'logger 可是程序或工人；weblog 不等于所有网站；logjam 的 jam 是塞住；log 对数不从木头义演化。',
 'The logger wrote the error to the log while a logjam delayed the remaining work.\n\n记录程序把错误写进日志，流程堵塞则拖延了其余工作。','log logger weblog changelog backlog logjam')
K=[['古英语 cnīf、中古英语 knif，联系北欧相关刀名','切割用刀具，早期借入、继承分析有不同看法'],['现代 knife 名词转动词','刀 → 用刀切、刺；比喻锋利穿过、背叛']]
W('knife','/naɪf/','刀；用刀切或刺；像刀一样穿过〔比喻〕',
 '有刀刃、用来切的工具；动词把工具名变成动作，既可真用刀，也可借说寒风像刀一样穿透。',
 '接较早英语 cnīf/knif，联系古诺尔斯语 knífr 等形式，具体早期借入分析有不同看法。开头 k 现代不发音；名词复数 knives /naɪvz/，动词形式另看。',K,
 'a kitchen knife 厨刀，a bread knife 面包刀，a knife blade 刀刃，the wind knifed through 寒风像刀一样穿过，knife someone in the back 也可比喻背叛。',
 'a kitchen knife；a bread knife；a knife blade；knife through。',
 '名词多把刀是 knives，动词第三人称却可写 knifes；过去式 knifed /naɪft/，没有 k 音，也不加 /ɪd/。',
 ('The bread knife is in the drawer.','面包刀在抽屉里。'),('A cold wind knifed through the thin coat.','冷风像刀一样穿透薄外套。'))
W('knifed','/naɪft/','被刀切、刺过的；knife 的过去式、分词',
 '可以说受过刀伤，也可以在文学描写里说寒风、光束锋利地穿过；先看主语和对象。',
 'knife + -ed，末尾 e 后加 d。/f/ 后词尾读 /t/，不同于名词复数 knives 的 /v/。',K+[['knife → knifed','用刀作用完成；或锋利穿过的比喻过去动作']],
 'had been knifed 曾被刀刺伤，knifed through the darkness 像刀一样划破黑暗；较少见组合还可说配某种刀片。',
 'had been knifed；knifed through；knifed apart。',
 'knifed 不发 /k/；knifed through 可以纯粹是比喻，不能看到这个词就认为每句都有真实袭击。',
 ('The report said that the man had been knifed.','报道说，那名男子被刀刺伤。'),('A beam of light knifed through the darkness.','一道光束利落地划破黑暗。'))
R('B3083','刀具、用刀动作和旧制笔工具','KNIFE：工具名可作动作，读音保留历史变化','knife → knifed；penknife 是旧时修整笔尖的小刀，后来成为随身小折刀名。',
 '掌握 k 不发音、复数 knives 和过去式 knifed，读写就不容易照字母机械拼。动作也可进入风、光的文学比喻。',
 'cnīf/knif 与北欧相关形式 → knife；knife → knives/knifed；pen + knife。',
 [['工具及其动作变化','knife · knifed'],['用途组合','penknife']],
 'knife 不读 k；knives 名词复数变 /v/，knifed 仍 /f/；penknife 不必外形像笔。',
 'The old penknife lay beside two larger knives.\n\n旧小折刀放在两把较大的刀旁。','knife knifed penknife')
W('unremarkable','英 /ˌʌnrɪˈmɑːkəbl/；美 /ˌʌnrɪˈmɑːrkəbl/','平常的、不显眼的、没有特别之处的',
 '没有什么值得停下来专门说一笔；可能平淡，也可能只是正常，不一定是批评。',
 'un- 不 + remarkable 值得注意、令人称奇的。remark 与注意、评论相关，-able 在这里保留值得注意的性质。',
 [['remarkable','值得注意、特别显著的'],['un- + remarkable → unremarkable','没有显著特别之处的']],
 'an unremarkable building 普通建筑，an unremarkable day 平常一天，a largely unremarkable career 大体平淡的经历。',
 'an unremarkable building；an unremarkable day；largely unremarkable。',
 'unremarkable 不等于无法评论，也不必等于 bad 很差；一段平静普通的日子完全可能令人满意。',
 ('The office was in an unremarkable building near the station.','办公室在车站附近一栋不起眼的楼里。'),('It was a quiet, unremarkable day.','那是安静、平常的一天。'))
R('B4458','值得注意，或没有特别之处','REMARKABLE：值得特意说一笔，反面便是普通','remarkable → remarkably；unremarkable 不显眼、平常，不自动是坏。',
 'remarkable 可以赞成就，也可说异常程度；unremarkable 则撤去特别显著的评价。语气和好坏由具体对象决定。',
 'remark 与 -able 相关 → remarkable；remarkable → remarkably；un- + remarkable。',
 [['显著性质、程度与反面','remarkable · remarkably · unremarkable']],
 'remarkably 可修饰程度；unremarkable 不是无话可评，也不自动很差。',
 'The building looked unremarkable outside but was remarkably bright inside.\n\n楼的外表不起眼，里面却格外明亮。','remarkable remarkably unremarkable')
if __name__=='__main__':save('continuation_20261030_if',ROOTS,WORDS)
