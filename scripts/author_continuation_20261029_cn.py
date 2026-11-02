"""Break: interruptions, openings and fixed compounds."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
def C(a,b,w,m):return [[a+'；'+b,'并列构词部分'],[w,m]]
BR=[['古英语 brecan → 中古英语 breken','打破、折断'],['英语 break','破坏完整或连续状态；中断、休息、突破等引申']]
W('break','/breɪk/','打破；断裂；中断；休息；机会',
 '原来完整、连着或一直不变的状态，突然开了口、断了一下。杯子破、工作停一会儿、纪录被刷新，都可用这个核心理解。',
 '由古英语 brecan 延续，经中古英语 breken；不是按现代 br- 加 eak 拆。变化为 break—broke—broken，是历史元音交替形式。',BR,
 'break a cup 打破杯子，break a rule 违反规则，break the silence 打破沉默；take a break 休息一下，a big break 重要机遇。具体义要配合对象。',
 'take a break；break a record；break the news；a lucky break。',
 'break 打破、休息，brake 刹车，读音相同而来源、拼写不同。break the news 是告知消息，不是损坏报纸。',
 ('Let’s take a short break before the next task.','下一项任务前，我们休息一小会儿吧。'),('Her performance broke the school record.','她的表现打破了学校纪录。'))
W('breakable','/ˈbreɪkəbəl/','易碎的；可被打破的',
 '碰一下、摔一下可能会坏，或者某种记录、约束并非永远不能打破。',
 'break + -able 可……的；-able 表可能性、可承受动作，不说明一定已经破了。',BR+[['break + -able → breakable','能被打破 → 易碎或可打破的']],
 'breakable glassware 易碎玻璃器皿，breakable items 易碎物品；breakables 作复数名词可指这些易碎品。',
 'breakable items；breakable glass；pack breakables carefully。',
 'breakable 可能破，broken 已经破；fragile 易碎、脆弱与前者有交叠，但语境和搭配不全相同。',
 ('Wrap the breakable items in soft cloth.','用软布包好易碎物品。'),('These cups are breakable, so please handle them carefully.','这些杯子易碎，请小心拿放。'))
W('unbreakable','/ʌnˈbreɪkəbəl/','不易打破的；坚不可摧的；坚定的',
 '经得住冲击、压力或考验，难被破坏；讲友情、意志时常带夸张和赞美。',
 'un- 不 + breakable 可打破的，否定整个形容词，不是 unbreak + -able 这一普通现代动词派生。',BR+[['breakable → unbreakable','可打破 → 难以或不能打破']],
 'an unbreakable bond 牢固的关系，an unbreakable rule 不可破的规矩；产品宣传说 unbreakable 不等于任何条件下都绝对不会损坏。',
 'an unbreakable bond；unbreakable glass；unbreakable resolve。',
 'unbreakable 强调难破或不可破，unbroken 强调目前没有断、未被打破；an unbroken record 不说明未来也破不了。',
 ('They formed an unbreakable bond during the expedition.','他们在探险中结下了牢固的情谊。'),('Her unbreakable resolve impressed the team.','她坚定不移的决心给团队留下了深刻印象。'))
W('breakage','/ˈbreɪkɪdʒ/','破损；破损物；破损损耗',
 '不只说某样东西破了，还把搬运、生产中破坏掉的这一部分算成一类损耗。',
 'break + -age，形成破损过程、结果或破损数量等名词。-age 在这里不表示人的年龄。',BR+[['break + -age → breakage','打破 → 破损、破损损耗']],
 'damage and breakage 损坏与破损，reduce breakage 减少破损；hair breakage 则是发丝断裂，不等于头发从根部脱落。',
 'reduce breakage；allow for breakage；hair breakage。',
 'breakage 常看破损现象或损耗，break 可以是一个断口、休息等；a coffee break 不能写 coffee breakage。',
 ('Better packaging reduced breakage during transport.','改进包装减少了运输中的破损。'),('The salon recommended gentler brushing to reduce hair breakage.','美发店建议梳头轻柔一些，以减少发丝断裂。'))
W('breaker','英 /ˈbreɪkə/；美 /ˈbreɪkər/','破坏、打破者；断路器；拍岸碎浪',
 '能把连续状态打断的人或东西：规则被破、电流被切断，海浪到岸边也会翻碎。',
 'break + -er，在中古英语已有相应形式。人、装置、波浪由不同 break 用法形成固定名词；另有少见同形词不在此串成一支。',BR+[['break + -er → breaker','打破者；断开装置；翻碎的浪']],
 'a rule breaker 违规者，a circuit breaker 断路器；breakers 复数常说翻卷拍碎的浪。单独 breaker 具体是哪种，靠环境判断。',
 'a circuit breaker；a rule breaker；waves breaking into breakers。',
 'breaker 是执行或产生作用的对象，breakage 是破损；海浪 breakers 不等于海里有什么人把东西砸坏。',
 ('The electrician inspected the circuit breaker.','电工检查了断路器。'),('White breakers rolled towards the beach.','白色碎浪朝海滩涌来。'))
W('breakthrough','/ˈbreɪkθruː/','突破；重大进展',
 '前面一直像有一堵墙挡着，终于穿过去，事情进入了一个新阶段。',
 'break through 突破、穿过转成单词名词；through 是穿过，不是 throw 扔。具体突破可以是技术、谈判、调查等。',BR+[['break through → breakthrough','穿过阻碍 → 关键突破、进展']],
 'a major breakthrough 重大突破，a breakthrough in research 研究突破；研究里的突破不自动等于已经能广泛实际应用。',
 'make a breakthrough；a scientific breakthrough；a breakthrough in negotiations。',
 'progress 可以是一点点进步，breakthrough 强调打通关键障碍的明显变化；不必每次小更新都叫 breakthrough。',
 ('The team made a breakthrough after months of failed tests.','经过几个月失败的测试，团队终于取得突破。'),('The agreement marked a breakthrough in the talks.','这份协议标志着谈判取得关键进展。'))
W('breakaway','/ˈbreɪkəweɪ/','脱离的；分裂出去的；突围、甩开对手的行动',
 '原来属于一个整体，后来从里面脱出来，成为单独的一股。',
 '由 break away 脱离形成名词、形容词；不是两词短语在所有句法位置都能直接连写。',BR+[['break away → breakaway','脱离原整体 → 脱离者、分离的分支或突围行动']],
 'a breakaway group 分离出去的团体；a breakaway in cycling 自行车赛甩开大部队的突围；a breakaway clasp 则是受拉力时可分开的扣件。',
 'a breakaway group；a breakaway movement；a breakaway attempt。',
 'break away 两词是动词短语，breakaway 单词常是名词、形容词：The group broke away，a breakaway group。',
 ('A breakaway group formed its own organisation.','一支脱离原团体的分支成立了自己的组织。'),('The rider launched a breakaway near the end of the race.','那位车手在比赛接近结束时发起突围。'))
W('breakneck','/ˈbreɪknek/','快得危险的；极其迅速的',
 '快到像可能摔断脖子的程度；现代大多是在夸张地强调速度和风险。',
 'break 折断 + neck 脖子，形成危险、猛烈的形容词，现代常紧接 speed、pace。不是每次使用都真的发生颈部受伤。',C('break 折断','neck 脖子','breakneck','危险到可能摔伤的 → 极快、猛烈的'),
 'at breakneck speed 以极快速度，a breakneck pace 极快节奏；可以说车辆，也可以说组织、技术变化的速度。',
 'at breakneck speed；a breakneck pace；breakneck growth。',
 'fast 快可中性，breakneck 强调惊人、可能不安全或难以跟上的程度；不要把普通准时完成都写成 breakneck。',
 ('The story moves at a breakneck pace.','故事推进得飞快。'),('The industry expanded at breakneck speed.','这个行业以令人咋舌的速度扩张。'))
W('jailbreak','/ˈdʒeɪlbreɪk/','越狱；解除设备或系统限制的行为',
 '原来被关在一个有边界的空间里，现在突破边界出去；技术领域借用这幅图景。',
 'jail 监狱 + break 突破，复合成越狱名词并可作动词。计算机、设备以及 AI 语境里，借指突破原有软件限制或约束，具体对象不同。',C('jail 监狱','break 突破','jailbreak','逃出监狱 → 技术语境中的限制突破'),
 'a jailbreak in a film 电影中的越狱；a device jailbreak 设备越狱。软件里看到这个词，先确认是在讨论哪一种限制，而不把所有修改都叫它。',
 'a jailbreak attempt；a fictional jailbreak；a device jailbreak。',
 'jailbreak 固定强调突破禁闭、限制；breakaway 只说从某整体脱离，不一定有监狱或技术限制背景。',
 ('The film begins with a dramatic jailbreak.','电影以一场戏剧性的越狱开场。'),('The article explains what a device jailbreak means.','文章解释了设备越狱这个词的含义。'))
W('tiebreak','/ˈtaɪbreɪk/','平局决胜局、决胜程序',
 '双方打成平手，得再用一套规定把这个平局打破，分出结果。',
 'tie 平局 + break 打破；也常写 tie-break，另有 tiebreaker 决胜者、决胜办法等相关词。不是拿剪刀剪断领带。',C('tie 平局','break 打破','tiebreak','用于打破平局的决胜局、程序'),
 'a tennis tiebreak 网球抢七或其他规定形式的决胜局；具体分数、赛制依比赛规则，词本身只交代用于打破平局。',
 'win a tiebreak；play a tiebreak；a final-set tiebreak。',
 'tie 平局，tiebreak 打破平局的办法或局；不能把所有正常最后一局都叫 tiebreak。',
 ('The players reached a tiebreak in the first set.','双方在第一盘进入了平局决胜局。'),('She won the match after a tense tiebreak.','经过紧张的平局决胜局，她赢下了比赛。'))
W('breakdancing','英 /ˈbreɪkdɑːnsɪŋ/；美 /ˈbreɪkdænsɪŋ/','霹雳舞；breaking 舞蹈',
 '常见地板动作、定格和旋转的一类舞蹈；名字里的 break 抓的是音乐的间奏、节奏段落，不是把身体摔坏。',
 'break + dancing，背景联系嘻哈音乐中强调打击乐的 break 段落及其舞蹈。舞者和比赛语境也常用 breaking 这一名称。',C('break 音乐中的间奏、节奏段落','dancing 跳舞','breakdancing','围绕这种节奏文化发展的一类舞蹈'),
 'a breakdancing class 霹雳舞课，a breakdancing performance 霹雳舞表演；具体动作并不只剩旋转，也有站立步法等。',
 'a breakdancing class；a breakdancing crew；a breakdancing performance。',
 'breakdancing 不是 break + dancing 表示跳舞中途休息；take a break from dancing 才是跳累了休息一会儿。',
 ('The festival included a breakdancing performance.','节庆活动包含一场霹雳舞表演。'),('She joined a beginner’s breakdancing class.','她参加了霹雳舞入门班。'))
W('breakfast','/ˈbrekfəst/','早餐；吃早餐',
 '夜里一段时间没有进食，早上这顿饭把这段空腹结束掉。',
 '中古英语 brekefast，break 结束、打破 + fast 禁食；fast 在这里不是快。所以早餐也不必吃得特别快。常用读音已弱化，不按 break 与 fast 分别完整拼读。',
 [['break 结束；fast 禁食','结束夜间不进食的时段'],['中古英语 brekefast → breakfast','早餐；吃早餐']],
 'have breakfast 吃早餐，a big breakfast 丰盛早餐；breakfast 作动词也可说早餐吃什么、在哪里吃，日常用 have breakfast 更普遍。',
 'have breakfast；a breakfast menu；breakfast cereal；bed and breakfast。',
 'breakfast 不是 fast food 快餐；eat breakfast quickly 才说早餐吃得快。一般 have breakfast 不必加 a，描述一顿丰盛早餐可说 have a big breakfast。',
 ('We had breakfast before leaving the hotel.','我们离开酒店前吃了早餐。'),('The price includes a simple breakfast.','价格包含一份简单早餐。'))
R('B2828','打破、断裂；休息、突破及脱离','BREAK：完整或连续的状态被打开','杯子裂开、工作暂停、障碍被突破，都能从原来完整或连续的状态被打断理解。固定复合词再各看对象。',
 'break 继承古英语 brecan。先读基础和可破性，再看打破者、突破、脱离；breakfast 的 fast 是禁食，breakdancing 的 break 联系音乐段落。',
 'break → breakable → unbreakable；breakage 说破损，breaker 说作用者；through 穿过、away 脱离；fast 禁食加 break 得早餐。',
 [['基础及可破性','break · breakable · unbreakable · breakage · breaker'],['突破与脱离','breakthrough · breakaway · jailbreak · tiebreak'],['速度与节奏','breakneck · breakdancing'],['固定生活词','breakfast'],['已学的其他复合词','heartbreak · daybreak · outbreak · breakwater · breakpoint']],
 'break 不等于 brake；breakfast 不是快餐；breakdancing 不是跳舞休息，breakthrough 不是普通小改动。',
 'After a short break and some breakfast, the team finally made a breakthrough.\n\n短暂休息、吃过早餐后，团队终于取得了突破。',
 'break breakable unbreakable breakage breaker breakthrough breakaway jailbreak tiebreak breakneck breakdancing breakfast heartbreak daybreak outbreak breakwater breakpoint')
if __name__=='__main__':save('continuation_20261029_cn',ROOTS,WORDS)
