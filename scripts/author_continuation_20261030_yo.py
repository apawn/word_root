"""Fill useful family gaps: suppose, squad, and healthcare."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'C1097':dict(words=['suppose','supposes','supposed','supposing','supposedly','supposition','presuppose','presupposition'],label='suppose 词族：把一个想法先垫在底下',note='拉丁放在下面的历史材料，经法语 poser 影响形成现代词形；先假定、再推论是理解线索，名词各有独立借入历史。'),
 'C1182':dict(words=['squad','squads','squadron'],label='squad → squads；squadron：方阵到行动小组',note='四、方形的材料经欧洲语言里的队伍名称借入，现代人数不由方形词源决定。'),
 'B3667':dict(words=['health','healthcare'],label='health → healthcare：健康与医疗照护服务',note='现代 health + care 复合，整体通常不可数；这里解释词义与用法。'),
}
W('suppose','英 /səˈpəʊz/；美 /səˈpoʊz/','认为、猜想；假设',
 '先把一个想法放在底下当作前提，再看看会怎样，就是 suppose 很好记的画面。日常 I suppose 也常是“我想大概是这样”。',
 '拉丁 sub- 下面在 p 前同化为 sup-，与 pōnere 放形成 suppōnere。法语 suposer 等在传承中受 poser 放置影响，英语借入为 suppose；不能把 pose 简单当成 ponere 原样保留。',
 [['拉丁 sub- + pōnere → suppōnere','放在下面；作为假定、基础的历史背景'],['受 poser 影响的古法语 suposer → suppose','假定、认为；直接法语词形经过替换、重塑']],
 'I suppose so 我想是这样；suppose that... 假设……；suppose we leave now 假设我们现在出发。',
 'suppose it is true；suppose we miss the train。','I suppose 常带不十分肯定、接受眼前判断的语气；Suppose... 可以开启一个假设。词源画面帮助记忆，实际使用仍要看是在猜想还是设定前提。',
 ('I suppose the shop is still open.','我想那家店大概还开着。'),('Suppose we miss the last train. What could we do?','假如我们错过末班火车，可以怎么办？'),sources=['https://www.etymonline.com/word/suppose','https://en.wiktionary.org/wiki/suppose#English'])
W('supposes','英 /səˈpəʊzɪz/；美 /səˈpoʊzɪz/','认为、假设〔suppose 的第三人称单数〕',
 '他、她或一个论证先接受某个想法作前提，就可以说 supposes；动作本身不说明这个想法最后一定是真的。',
 'suppose + -s，/z/ 后增加 /ɪz/。底词经古法语 suposer 等接拉丁 suppōnere 放在下面，并受法语 poser 的形式影响；现代词尾表示第三人称单数。',
 [['拉丁 suppōnere → 受 poser 影响的古法语 → suppose','放在下面 → 假定、认为'],['suppose + -s → supposes','单数主语认为或预先假定']],
 'supposes that... 认为、假设……；the argument supposes... 论证以……为假定。',
 'supposes it will work；supposes everyone agrees。','supposes 是现在时单数主语形式；I、you、we、they 常接 suppose。结尾虽然只加一个 s，读音却增加 /ɪz/ 音节。',
 ('She supposes that the meeting will finish before lunch.','她想会议大概午饭前会结束。'),('The argument supposes that everyone has the same information.','这个论证假定每个人掌握的信息相同。'),sources=['https://en.wiktionary.org/wiki/supposes#English','https://www.etymonline.com/word/suppose'])
W('supposing','英 /səˈpəʊzɪŋ/；美 /səˈpoʊzɪŋ/','假定、认为〔现在分词〕；假如〔引出假设〕',
 '把一个可能情况暂时摆出来，可以用 supposing；像讨论前先摆一张条件卡：要是条件这样，会有什么结果？',
 'suppose 去不发音 e，加 -ing → supposing。suppose 经古法语接拉丁 suppōnere，并受 poser 影响；英语分词形式又发展成引出假设的连接用法。',
 [['拉丁 suppōnere → 古法语重塑词形 → suppose','假定、作为前提'],['suppose → supposing；分词的连接用法','正在假定；假如某个条件成立']],
 'supposing that... 假如……；supposing we leave early 假如我们早走；keep supposing 不断作假设。',
 'supposing the weather changes；supposing that he agrees。','Supposing... 在讨论假设时常接一个完整小句，也可不加 that。它往往提出条件，后面再问或说明结果。',
 ('Supposing the weather changes, where could we meet?','假如天气变了，我们可以在哪里见面？'),('Supposing we leave now, can we catch the earlier train?','假如现在走，我们能赶上早一班火车吗？'),sources=['https://en.wiktionary.org/wiki/supposing#English','https://www.etymonline.com/word/suppose'])
W('supposition','英 /ˌsʌpəˈzɪʃən/；美 /ˌsʌpəˈzɪʃən/','假定、推测；作为依据的设想',
 '证据还没把事情完全坐实，先拿来当判断基础的想法，是 supposition。它把 suppose 的假定动作框成一个可以讨论的设想。',
 '名词借自中世纪拉丁 suppositio、suppositionem 等，接 suppōnere 的分词词干 supposit-；历史已有放在下面、假设等义。现代与 suppose、-ition 对照认形，不能把英语动词词尾简单原样相加。',
 [['拉丁 suppōnere → supposit-、suppositio → 中世纪拉丁假设义','放在下面、替置等背景 → 作为论证基础的假定'],['英语 supposition','未经充分证实的设想、推测；与 suppose 同族']],
 'on the supposition that... 根据……的假定；mere supposition 仅仅是推测；a reasonable supposition 合理的假定。',
 'based on supposition；question the supposition。','supposition 不自动等于胡猜，可以是合理但待核实的前提。与 fact 的区别在于是否已得到确认；表达时要交代支撑它的资料。',
 ('We planned the visit on the supposition that the museum would be open.','我们按博物馆会开门这个假定安排了参观。'),('That conclusion rests on supposition rather than direct evidence.','那个结论依据的是推测，还没有直接证据。'),sources=['https://www.etymonline.com/word/supposition','https://en.wiktionary.org/wiki/supposition#English'])
W('presuppose','英 /ˌpriːsəˈpəʊz/；美 /ˌpriːsəˈpoʊz/','预先假定；以……为前提',
 '还没开始往下说，已经默认某件事成立，是 presuppose。它比 suppose 更突出这个想法已经先放在讨论底下。',
 '现代可认 pre- 预先 + suppose。历史英语早有 presupponen，后来词形改变，联系古法语 presupposer 或中世纪拉丁 praesuppōnere；不是只有一条现代英语临时拼接的历史。',
 [['古法语 presupposer／中世纪拉丁 praesuppōnere → 较早英语形式','预先放入假定、当作前提'],['词形调整 → presuppose','预设某事成立；要求先有某个条件']],
 'presuppose that... 预先假定……；presuppose knowledge 以具备知识为前提。',
 'presuppose equal access；presuppose that help is available。','suppose 可是当下提出一个假设，presuppose 则强调说法或安排本身已把某条件当作成立。分析论证、计划或教材要求时很有用。',
 ('The plan presupposes that everyone has internet access.','这个计划预先假定每个人都能上网。'),('We should not presuppose knowledge that beginners may not have.','我们不该预先认定初学者掌握了他们可能还没有的知识。'),sources=['https://www.etymonline.com/word/suppose','https://en.wiktionary.org/wiki/presuppose#English'])
W('presupposition','/ˌpriːsʌpəˈzɪʃən/','预先的假定；预设、前提',
 '一句话、一个计划已经悄悄当真的那张条件卡，就是 presupposition。把这张卡找出来，才能看清后面的推论靠什么站住。',
 '现代认形可用 pre- 预先与 supposition 对照；历史经法语 présupposition、或直接中世纪拉丁 praesuppositio 等借入，接 praesuppōnere 的名词材料。',
 [['中世纪拉丁 praesuppōnere → praesuppositio；法语相应形式','预先假定 → 先在的假设、前提'],['英语 presupposition','某个判断、表达背后已默认的条件']],
 'a hidden presupposition 隐含预设；question a presupposition 质疑前提；the presupposition that... ……这一预设。',
 'presupposition behind the question；built on a presupposition。','presupposition 常指已经埋在表达里的前提；supposition 可以只是你现在提出的假定。语言学还有更专门的预设概念，这里先掌握一般阅读义。',
 ('The question contains a hidden presupposition about who made the decision.','这个问题对谁作了决定含有一个隐藏预设。'),('The discussion began by examining its central presupposition.','讨论从审视其核心前提开始。'),sources=['https://www.etymonline.com/word/presupposition','https://en.wiktionary.org/wiki/presupposition#English'])
W('squad','英 /skwɒd/；美 /skwɑːd/','小队、行动组；运动队的队员班底',
 '为了一个共同任务聚在一起的一小组人，是 squad；体育里也常指一支队伍可用的整批队员。较早的词源画面与方形队列有关。',
 '经法语 esquade、escadre，接西班牙语 escuadra 或意大利语 squadra 的队伍词，较早联系方形与拉丁 quadrāre 使成方形等材料。词源四方形不规定现代小队必须几个人。',
 [['拉丁方形词族 → 西班牙语／意大利语队伍名称','方形、方阵 → 一组军人'],['法语相关形式 → 英语 squad','任务小队；后来扩至体育队伍等']],
 'a rescue squad 救援小队；a police squad 警方行动组；the national squad 国家队班底。',
 'a squad sent to help；selected for the squad。','体育报道里的 squad 常是整批入选队员，不一定都是当场首发。小队人数和编制按具体组织决定，不能从 quad- 四推出恰好四人。',
 ('A rescue squad reached the village before dark.','一支救援小队天黑前到达了村庄。'),('She was selected for the national squad.','她入选了国家队。'),sources=['https://www.etymonline.com/word/squad','https://en.wiktionary.org/wiki/squad#English'])
W('squads','英 /skwɒdz/；美 /skwɑːdz/','小队、行动组；运动队班底〔squad 的复数〕',
 '几组人分头承担任务，可以说 squads；体育语境则可以数不同队伍、年龄组的队员班底。',
 'squad + -s，/d/ 后读 /z/。squad 的队伍名称经法语与意大利语、西班牙语相关形式，较早接拉丁方形词族；现代按普通名词形成复数。',
 [['方形、队列词族 → 欧洲语言相关形式 → squad','方阵背景 → 小队、队伍'],['squad + -s → squads','多个小队或队伍班底']],
 'rescue squads 救援小队；training squads 集训队；squads from different regions 不同地区的队伍。',
 'squads working in different areas；squads named for the tournament。','squads 数不同团队，players 数其中队员。两个 squads 不意味着只有两个运动员；要分清队与人的计数单位。',
 ('The squads worked in different parts of the town.','各小队在镇上的不同区域工作。'),('The coaches announced their squads for the tournament.','教练们公布了各自参加锦标赛的队员名单。'),sources=['https://en.wiktionary.org/wiki/squads#English','https://www.etymonline.com/word/squad'])
W('squadron','英 /ˈskwɒdrən/；美 /ˈskwɑːdrən/','中队；舰艇、飞机等的编队单位',
 '在较大的军队、航空或舰队组织里，一个按编制组成的单位，可以叫 squadron。它和 squad 有同族历史，但现代具体等级、人数由组织规定。',
 '来自意大利语 squadrone，是 squadra 队伍、方阵的增大形式，英语借入后先用于军人队列，后来用于骑兵、舰队、航空等单位；不是现代英语 squad 随意加一个 ron 后缀。',
 [['意大利语 squadra → squadrone','队伍、方阵 → 较大的队列名称'],['英语 squadron；不同军种专门化','骑兵、舰队、航空等编制单位']],
 'an air squadron 航空中队；a squadron of aircraft 一支飞机中队；a squadron based nearby 驻扎在附近的中队。',
 'a squadron arriving at the base；members of the squadron。','squadron 与 squad 词源相关，现代不总能按小队扩大一次来换算编制。阅读新闻时，把它先理解为所在军种的一支单位，再看上下文给出的规模。',
 ('The squadron moved to a new base in spring.','这个中队春季转移到了一个新基地。'),('The exhibition tells the history of a local air squadron.','展览讲述了当地一支航空中队的历史。'),sources=['https://www.etymonline.com/word/squad','https://en.wiktionary.org/wiki/squadron#English'])
W('healthcare','英 /ˈhelθkeə/；美 /ˈhelθker/','医疗、卫生保健；医疗照护服务',
 '为了维护、恢复人的健康而提供的照护服务，就是 healthcare。把 health 健康与 care 照顾放在一起，现代组合的意思就很直观。',
 'health + care → healthcare。health 继承古英语 hǣlþ 的健康词，care 接古英语 caru 等关切、照料词；两个本族词组成现代服务名称，也常分写为 health care。',
 [['health 健康 + care 照护','两条本族词的现代组合'],['healthcare／health care','与健康有关的医疗、照护服务及其领域']],
 'healthcare workers 医疗卫生人员；healthcare services 医疗服务；access to healthcare 获得医疗服务的机会。',
 'work in healthcare；healthcare provided in the region。','healthcare 通常不可数，泛指服务或领域；具体一家医院、诊所要用相应机构名称。分写 health care 与连写 healthcare 都常见，本文收连写形式。',
 ('She has worked in healthcare for ten years.','她在医疗卫生领域工作了十年。'),('The report compares healthcare services in several regions.','报告比较了几个地区的医疗服务。'),sources=['https://en.wiktionary.org/wiki/healthcare#English','https://en.wiktionary.org/wiki/health#English','https://en.wiktionary.org/wiki/care#English'])
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_yo',ROOTS,WORDS)
 extend_lessons()
