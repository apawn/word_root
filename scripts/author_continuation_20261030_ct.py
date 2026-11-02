"""Mail and balance: bag/post vs armor; two pans and equilibrium expansions."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
MA=[['法语 male 袋 → 中古英语 male → mail','装物袋 → 邮袋、袋中信件 → 邮件、邮政'],['另一来源：法语 maille → 中古英语 mayle → mail','小环、网眼 → 环环相扣的锁子甲'],['现代 mail 动词','由邮政名词转为寄送；盔甲相关用法另接锁甲来源']]
def MH(f,m):return MA[:1]+[[f,m]]
W('mail','/meɪl/','邮件、邮政；邮寄；〔另源〕锁子甲',
 '常用邮寄义的旧画面是一只装信的袋子，后来用袋叫里面的信；骑士身上的 mail 却是小金属环连成的甲，来源不同。',
 '邮件义经法语 male 袋；锁甲义经 maille 小环、网眼，接拉丁语 macula 等。动词寄送从邮件名词发展。blackmail 勒索里的 mail 又接旧付款、租税等词，不是三种都来自一袋信。',MA,
 'check the mail 查看邮件，send by mail 邮寄，mail a letter 寄信，a coat of mail 锁子甲。邮件名词通常不可数；单封可说 a letter、a piece of mail。',
 'check the mail；send by mail；mail a letter；a coat of mail。',
 'mail/male 男性同音异词；mail 邮件不通常说 a mail 来数一封，电子语境 an email 更常见。post 在英式邮寄场景也很常用。',
 ('The mail arrived earlier than usual today.','今天邮件比平时到得早。'),('The knight wore a coat of mail beneath his tunic.','骑士在外袍下穿着锁子甲。'),
 sources=['https://en.wiktionary.org/wiki/mail#English','https://www.etymonline.com/word/mail'])
W('mailed','/meɪld/','已邮寄的；穿锁子甲的〔另来源〕',
 'mailed letter 是寄出的信；mailed knight 则是披锁甲的骑士。看后面对象才能确定到底走哪条 mail。',
 '邮寄义是 mail 动词 + -ed；锁甲形容词是 mail 锁甲 + -ed，旧时已有 mayled 等。两者同音、同形，不能统一理解成把骑士塞进邮袋。',
 [['mail〔邮寄〕+ -ed → mailed','已寄出的'],['mail〔锁子甲〕+ -ed → mailed','披锁子甲的；有中古英语旧形背景']],
 'a mailed letter 寄出的信，mailed copies 邮寄的副本，a mailed knight 锁甲骑士。被寄出不保证对方已经收到。',
 'a mailed letter；mailed copies；a mailed knight。',
 'mailed 已寄出、delivered 已投递，步骤不同；mailed armour 语境接锁甲来源，不接邮政。',
 ('The mailed copies should arrive next week.','邮寄出去的副本预计下周送到。'),('The illustration shows a mailed knight on horseback.','插图画着一位骑马的锁甲骑士。'))
W('mailer','英 /ˈmeɪlə/；美 /ˈmeɪlər/','寄件人；邮寄广告、邮寄包装；邮件程序〔按语境〕',
 '可以指把邮件送出去的一方，也可以是供邮寄的包装、寄到手里的宣传单；具体角色看物品和场景。',
 'mail 邮寄 + -er，人、器具或相关物名称。寄件人和包装、广告、程序是不同专门化用法，不全翻成邮递员。',MH('mail + -er → mailer','寄件方；邮寄包装、广告或邮件程序等'),
 'a padded mailer 气泡衬垫信封，a promotional mailer 邮寄宣传材料，a bulk mailer 批量寄件者或程序。',
 'a padded mailer；a promotional mailer；a bulk mailer。',
 'mailer 寄件方、包装等，mail carrier 投递邮件的人；两者都跟邮件有关，但工作环节不同。',
 ('She packed the booklet in a padded mailer.','她把小册子装进气泡衬垫信封。'),('We received a promotional mailer from the museum.','我们收到了博物馆寄来的宣传材料。'))
W('voicemail','/ˈvɔɪsmeɪl/','语音信箱；语音留言',
 '对方没接电话，声音先被存下来，等对方有空再听；像给声音留一个信箱。',
 'voice 声音 + mail 邮件，合成按声音存储、传递的通信名称。可指系统、功能，也可指里面的一条留言。',MH('voice + mail → voicemail','存储语音消息的系统；语音留言'),
 'leave a voicemail 留语音消息，check voicemail 听语音留言，go to voicemail 转入语音信箱。',
 'leave a voicemail；check voicemail；go to voicemail。',
 'voicemail 留下后再听，a live call 实时通话；voice message 更泛，可在不同通信服务发送。',
 ('I left her a voicemail about the meeting.','我给她留了条语音，告诉她会议的事。'),('The call went straight to voicemail.','电话直接转进了语音信箱。'))
R('B3331','袋到邮袋、邮件；锁子甲另源；语音也借信箱','MAIL：袋里的信成为邮件；小环连成的甲走另一来源','mail → mailed、mailer；voicemail 声音消息；mailbox、mailbag、mailman、mailroom、airmail 按对象、场所、方式复用。',
 '邮件与锁甲明确分源；mailed 两种用法随对象分辨。blackmail 旧付款来源只作辨析，不让邮件词族解释所有同形字串。',
 'mail + -ed/-er/box/bag/man/room；voice/air + mail；mail 锁甲 + -ed 另支。',
 [['邮件、寄件与结果','mail · mailed · mailer'],['语音与发送方式','voicemail · airmail'],['存放、人物和场所','mailbox · mailbag · mailman · mailroom']],
 'mail/male 同音；邮件通常不可数；mailed 已寄不等于 delivered 已投递；mailer 非一律投递员；锁甲另源。',
 'The mailer included instructions for checking voicemail.\n\n那份邮寄材料里附有查看语音留言的说明。','mail mailed mailer voicemail airmail mailbox mailbag mailman mailroom')
BA=[['拉丁语 bilanx〔双盘的〕、相关 bilancia → 法语 balance → 中古英语 balaunce','bi- 两 + lanx 盘，双盘秤'],['英语 balance','称量、平衡；协调、收支差额、余额等']]
def BH(f,m):return BA+[[f,m]]
W('balance','/ˈbæləns/','平衡、均衡；天平；余额；保持平衡、权衡',
 '天平两边放东西，别让一边把另一边完全压下去；身体、时间、观点也可用这个协调画面。账目里则看两边算过之后剩多少。',
 '经法语 balance 接拉丁语双盘秤相关形式，旧成分 bi- 两、lanx 盘。动词由名词发展，数学相等、身体平衡和日常兼顾各按对象理解。',BA,
 'keep your balance 保持平衡，a balance between work and rest 工作休息平衡，a bank balance 账户余额，balance A against B 权衡两者。',
 'keep your balance；strike a balance；on balance；a bank balance。',
 'balance 平衡不要求所有东西各占同样数量；balanced schedule 可以按需要安排不同时间。on balance 总的权衡来看，并不是站在天平上。',
 ('She lost her balance on the uneven ground.','她在不平地面上失去了平衡。'),('We need to balance speed against accuracy.','我们需要在速度和准确性之间作权衡。'))
W('balanced','/ˈbælənst/','平衡、均衡的；公允、全面的',
 '不让某一边压倒一切；描述报道时，就是给不同相关方面适当位置，别只剩一面。',
 'balance 去 e 加 -ed，过去分词形成形容词。/s/ 后 -ed 常读 /t/，不是单独再读一节 /ɪd/。',BH('balance + -ed → balanced','平衡的；各方面考虑得当的'),
 'a balanced view 公允看法，a balanced account 全面叙述，a balanced schedule 均衡日程。',
 'a balanced view；a balanced account；a balanced schedule。',
 'balanced 不等于每边严格一半；报道 balanced 也不意味着证据强弱不同的说法必须得到完全相同权重。',
 ('The article gives a balanced account of the debate.','文章较全面公允地叙述了那场争论。'),('She tries to keep a balanced schedule of work and rest.','她尽量把工作与休息安排得均衡。'))
W('imbalance','/ɪmˈbæləns/','不平衡、失衡',
 '该协调的两边差得太多，一边过重或过少；先说这种状态，而不直接说谁把它弄偏了。',
 '否定前缀 im- + balance；im- 是 in- 在 b 前的相应形式。这里构成状态名词，不是动词移除平衡的动作。',BH('im- + balance → imbalance','缺少应有协调、平衡的状态'),
 'an imbalance between A and B 两者间失衡，a power imbalance 权力不对等，correct an imbalance 纠正失衡。',
 'an imbalance between；a power imbalance；correct an imbalance。',
 'imbalance 状态，unbalance 常动词使失衡；不对等不一定只指物理重量，也可资源、权力、供需。',
 ('The report highlights an imbalance between supply and demand.','报告指出供需之间存在失衡。'),('They changed the schedule to correct the imbalance.','他们调整日程来纠正不均衡。'))
W('unbalance','/ʌnˈbæləns/','使失去平衡；打乱均衡',
 '原来还能站住、配合得当，某股力量把它推歪、弄乱。',
 'un- 移除、逆转 + balance 保持平衡，形成动词。不是把名词简单放在前面作一个没有平衡的标签。',BH('un- + balance → unbalance','破坏平衡、使失衡'),
 'unbalance the load 使负载失衡，unbalance the system 打乱系统均衡，unbalance someone 使人失去稳定。',
 'unbalance the load；unbalance the system；unbalance the team。',
 'unbalance 动作，imbalance 状态；The change unbalanced the system 是变化造成失衡。',
 ('Putting all the boxes on one side unbalanced the cart.','把所有箱子放在一边，使小推车失去了平衡。'),('The sudden departure unbalanced the team.','那个人突然离开，打乱了团队的协调。'))
W('unbalanced','/ʌnˈbælənst/','不平衡、失衡的；偏颇的',
 '力气、重量、资源没配好，或一份说明只顾一边；重点在已经呈现的不均衡。',
 'un- + balanced 可表示不平衡的性质；也可是 unbalance + -ed 的结果。两种结构在现代形式上重合，依句法判断。',BH('un- + balanced / unbalance + -ed → unbalanced','处于不平衡状态；被打乱均衡的'),
 'an unbalanced load 失衡负载，an unbalanced account 偏颇叙述，an unbalanced design 比例不协调设计。旧人物精神状态用法不作中性医学名称。',
 'an unbalanced load；an unbalanced account；an unbalanced design。',
 'unbalanced 不平衡，imbalanced 也有相近性质用法；不是所有不平衡都涉及人的精神问题。',
 ('An unbalanced load made the machine shake.','负载失衡使机器抖动起来。'),('The reviewer criticized the book’s unbalanced account of events.','评论者批评书中对事件的叙述偏颇。'))
W('counterbalance','英 /ˌkaʊntəˈbæləns/；美 /ˌkaʊntərˈbæləns/','抵消、制衡；平衡重、抗衡力量',
 '一边太重，就在另一边放一个相应力量。也可一项好处抵消某项坏处，不必真搬砝码。',
 'counter- 相对、抵消 + balance，构成名词和动词。counter 在这里不是柜台，也不是数东西的计数器。',BH('counter- + balance → counterbalance','相对力量、平衡重；用它抵消、制衡'),
 'counterbalance a risk 抵消风险，a counterbalance to something 对某物的制衡，a counterbalance weight 平衡重。',
 'counterbalance the effect；a counterbalance to；a counterbalance weight。',
 'counterbalance 强调相对力量抵消或制衡，rebalance 调整整体分配使重新协调；不保证一定完全消掉另一项影响。',
 ('The lower price counterbalanced the longer journey.','较低价格抵消了路程更长的不利之处。'),('The heavy base acts as a counterbalance to the long arm.','沉重底座给长臂提供平衡重量。'))
W('rebalance','/ˌriːˈbæləns/','重新平衡、调整比例',
 '原来配好的比重不再合适，就把任务、资源、重量重新分配一下。',
 're- 重新 + balance，组成恢复或调整均衡的动词。没有由词本身规定必须恢复到最初的相同比例。',BH('re- + balance → rebalance','再次调整，使比例或作用协调'),
 'rebalance the workload 调整工作量分配，rebalance the system 重新平衡系统，rebalance priorities 调整重点。',
 'rebalance the workload；rebalance priorities；rebalance the system。',
 'rebalance 重新协调，unbalance 打乱协调；重新分配可因目标改变，不必原样倒回。',
 ('The manager rebalanced the workload across the team.','经理重新调整了团队各人的工作量。'),('They moved several boxes to rebalance the cart.','他们挪动几个箱子，让小推车重新平衡。'))
W('balancer','英 /ˈbælənsə/；美 /ˈbælənsər/','平衡装置、使平衡者',
 '负责把不均匀的负载、力量分配稳的人或设备；实际指什么得看前面的修饰词。',
 'balance + -er，词尾 e 与 -er 衔接。器具、人物和系统功能都能借使平衡这个动作命名。',BH('balance + -er → balancer','提供、调整平衡的装置或执行者'),
 'a wheel balancer 车轮平衡设备，a load balancer 负载均衡器，a mechanical balancer 机械平衡装置。',
 'a wheel balancer；a load balancer；a mechanical balancer。',
 'balancer 实现平衡的角色或设备，balance 状态、动作、秤等；不把所有 balancer 都认成测体重的秤。',
 ('The mechanic checked the wheel on a balancer.','机械师用平衡设备检查了车轮。'),('A load balancer distributes requests among several servers.','负载均衡器把请求分配给几台服务器。'))
R('B3025','双盘秤、协调平衡；状态、破坏、抵消与重调','BALANCE：两边不互相压垮，再借来讲资源、观点和账目','balance → balanced；unbalance → unbalanced；imbalance 状态；counterbalance 抵消、rebalance 重调、balancer 器具角色。',
 '不把平衡机械认成每边一半。新增 balanced、unbalanced 是常见实际用法；双盘秤词源帮助串起来，不要求所有比喻真有秤。',
 '拉丁 bi- 两 + lanx 盘；balance + -ed/-er；im-/un-/counter-/re- + balance；un- + balanced。',
 [['平衡与性质','balance · balanced'],['失衡动作、结果和状态','unbalance · unbalanced · imbalance'],['抵消、重调与器具','counterbalance · rebalance · balancer']],
 'balanced 不必一半一半；imbalance 状态、unbalance 动作；counterbalance 抵消制衡、rebalance 重调；balancer 不只体重秤。',
 'They rebalanced the unbalanced load before moving the cart.\n\n他们先重新调整失衡的负载，再推小车。','balance balanced unbalance unbalanced imbalance counterbalance rebalance balancer')
if __name__=='__main__':save('continuation_20261030_ct',ROOTS,WORDS)
