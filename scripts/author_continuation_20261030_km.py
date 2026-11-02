"""Pathy and addict: separate senses and grammatical roles."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
P=[['希腊 pathos、-patheia','经历、感受、遭受、病患等相关意义'],['现代医学 -pathy','某部位、系统的病变；与表示感受的旧词分支区别'],['retino-、nephro- + -pathy','视网膜病变；肾病、肾损害']]
W('retinopathy','英 /ˌretɪˈnɒpəθi/；美 /ˌretɪˈnɑːpəθi/','视网膜病变',
 '视网膜是眼内感光的组织。retinopathy 告诉你病变发生在视网膜，名字本身还没有交代是哪种原因、哪种程度。',
 'retino- 视网膜，来自 retina + -pathy 病变。连接元音 o 把部位名与病变后部接起来。',P,
 'diabetic retinopathy 糖尿病视网膜病变，retinopathy screening 视网膜病变筛查。加在前面的限定语可进一步说明类型或相关原因。',
 'diabetic retinopathy；retinopathy screening。',
 'retinopathy 是部位加病变的总称，retinitis 的 -itis 则突出炎症名称。不能仅凭后缀判断全部病理过程、病因。',
 ('The researcher studied images of retinopathy.','研究人员研究了视网膜病变的影像。'),('The clinic runs a screening program for diabetic retinopathy.','诊所开展糖尿病视网膜病变筛查项目。'),sources=['https://en.wiktionary.org/wiki/retinopathy#English','https://www.nei.nih.gov/eye-health-information/eye-conditions-and-diseases/diabetic-retinopathy'])
W('nephropathy','英 /nɪˈfrɒpəθi/；美 /nəˈfrɑːpəθi/','肾病、肾脏病变',
 'nephro- 把位置指向肾，-pathy 告诉你在谈病变。它像一个范围标签，具体什么病还要看后续说明。',
 'nephro-，联系希腊 nephros 肾 + -pathy 病变。组合成肾脏疾病、损伤等的名称。',P[:2]+[['nephro- + -pathy → nephropathy','肾的病变']],
 'diabetic nephropathy 糖尿病肾病，a form of nephropathy 一种肾脏病变。相关形容词 renal、nephric 都可涉及肾，但构词来源不同。',
 'diabetic nephropathy；a form of nephropathy。',
 'nephropathy 并不自动等于 nephritis 肾炎，也不自动表示肾衰竭；词本身只给出较宽的肾病范围。',
 ('No history of nephropathy was recorded.','病历中没有记录肾病史。'),('The study compared two forms of nephropathy.','研究比较了两种肾脏病变。'),sources=['https://en.wiktionary.org/wiki/nephropathy#English','https://goldbook.iupac.org/terms/view/15915'])
R('A2023','经历、感受与病患的不同历史分支','PATHY：旧核心是经历、感受、遭受，医学里常说病变','empathy、sympathy 看感受关系；retinopathy、nephropathy 等看部位病变；其他固定名称分别理解。',
 '后缀不是永远翻成同一个字。先判断整词在讲情感、病变还是某种理论、实践名称，再看前部。',
 'pathos、-patheia → -pathy；retino- 视网膜、nephro- 肾、neuro- 神经、myo- 肌肉等限定对象。',
 [['情感与感受关系','sympathy · empathy · telepathy'],['部位、系统的病变','retinopathy · nephropathy · neuropathy · encephalopathy · myopathy · psychopathy'],['已经固定的实践名称','homeopathy · osteopathy']],
 '词源解释名称，不证明某种理论有效；-pathy 不等于 -itis；不同整词可能已形成专门定义。',
 'Retinopathy names a retinal condition, while nephropathy names a kidney condition.\n\nretinopathy 命名视网膜病变，nephropathy 命名肾脏病变。','sympathy empathy telepathy retinopathy nephropathy neuropathy encephalopathy myopathy psychopathy homeopathy osteopathy')
A=[['拉丁 ad- 向、给予 + dīcere 宣告 → addīcere','宣告归属、判给；转为交付、献身'],['addictus → 英语 addict、addicted','交付、投身 → 对某事依赖、难以控制'],['addiction、addictive、addicting','成瘾状态；容易使人上瘾、停不下来的性质']]
W('addict','名词 /ˈædɪkt/；动词 /əˈdɪkt/','成瘾者；痴迷者〔口语〕；使上瘾',
 '历史起点像把人交付给某人、某件事，后来成为被某种东西强烈牵住。名词说人，动词说使进入这种状态，重音随之改变。',
 '借拉丁 addictus，addīcere 的过去分词；ad- + dīcere 宣告，形成判给、交付、献身等义。英语较早有投身、交付用法，现代成瘾者名词后来固定。',A[:2],
 'a drug addict 药物成瘾者，a coffee addict 咖啡迷〔常为夸张〕。谈健康状况时也常用 person with an addiction，把人和状况说开。动词多在 addicted 等形式中见到。',
 'a coffee addict；a person with an addiction。',
 '口语 shopping addict、coffee addict 常夸张说爱好，不等于已经作了临床判断；临床成瘾涉及控制困难、危害等，远不只喜欢。',
 ('He jokingly calls himself a coffee addict.','他开玩笑说自己是个咖啡迷。'),('He described himself as a recovering addict.','他称自己是一名正在康复中的成瘾者。'),sources=['https://en.wiktionary.org/wiki/addict#English','https://www.etymonline.com/word/addict','https://www.cdc.gov/overdose-prevention/hcp/training-modules/treatment/page33957.html'])
W('addicted','/əˈdɪktɪd/','上瘾、成瘾的；着迷的〔口语〕',
 '人已经被某种东西牢牢吸住、很难停下，是 addicted。日常说 addicted to a show，也常只是夸张地说追剧上头。',
 'addict 动词 + -ed，结尾 /ɪd/。历史由交付、投身某事的状态，走向依赖、成瘾等义。',A[:2]+[['addict + -ed → addicted','已处于依赖、着迷的状态']],
 'be addicted to something 对某物上瘾，become addicted 变得上瘾。to 是介词，接动词时用 -ing：addicted to playing。',
 'be addicted to；become addicted。',
 'addicted 多说受到影响的人，addictive 多说让人难停下的东西：an addictive game；a player addicted to it。',
 ('She says she is addicted to the detective series.','她说自己追这部侦探剧追上头了。'),('They asked him when he first became addicted.','他们问他是从什么时候开始成瘾的。'))
W('addiction','/əˈdɪkʃən/','成瘾、上瘾；难以割舍的痴迷〔口语〕',
 '重点不只是很喜欢，而是控制越来越困难，明知有损害也难停下。轻松聊天里也会夸张说某个爱好是 an addiction，要按语气分辨。',
 '拉丁 addictiō、addiction- 表判给、交付，英语也可联系 addict + -ion。早期有倾向、投身等义，后来成瘾状态义日益突出。',A[:2]+[['addictiō 等 → addiction','交付、投身的名词 → 成瘾状态']],
 'drug addiction 药物成瘾，addiction research 成瘾研究，an addiction to something 对某物的成瘾、痴迷。具体专业定义还依对象和领域区分。',
 'drug addiction；addiction research；an addiction to something。',
 'habit 是习惯，不必造成危害或失去控制；addiction 的专业用法不能仅凭频繁使用、喜爱就认定。',
 ('The book explains how addiction differs from an ordinary habit.','书中解释成瘾与普通习惯有何不同。'),('The course includes an introduction to addiction research.','课程包括成瘾研究入门。'),sources=['https://en.wiktionary.org/wiki/addiction#English','https://www.etymonline.com/word/addict','https://www.cdc.gov/overdose-prevention/hcp/training-modules/treatment/page33957.html'])
W('addictive','/əˈdɪktɪv/','容易使人上瘾的；让人停不下来的〔口语〕',
 '东西有一种让人反复回去、难以停下的吸引力，可以 addictive。专业语境说成瘾风险，游戏、食物等评论里也常是夸张。',
 '联系 addict 词干 + -ive，形成倾向、作用的形容词。要与 addicted 已经受到影响的状态分开。',A[:2]+[['addict + -ive → addictive','可能引起成瘾；口语难以停下']],
 'an addictive substance 可使人成瘾的物质，an addictive game 让人停不下来的游戏，highly addictive 很容易让人上瘾。',
 'an addictive game；highly addictive。',
 '评论中的 addictive 不一定是医学诊断，也不一定是单纯褒义；观察对象和说话目的。addicted 则多修饰人或相关状态。',
 ('The puzzle is simple but surprisingly addictive.','谜题很简单，却意外地让人停不下来。'),('Some substances are highly addictive.','有些物质很容易使人成瘾。'))
W('addicting','/əˈdɪktɪŋ/','让人上瘾、使人停不下来的',
 '和 addictive 一样，常用来评价某东西让人反复想用、想玩，尤其见于美式口语。',
 'addict + -ing，由分词形成表示引起上瘾作用的形容词。英语里确有这个词，不是见到 addictive 就要把另一形式一律判错。',A[:2]+[['addict + -ing → addicting','有使人上瘾作用的性质']],
 'an addicting game 让人停不下来的游戏，so addicting 太让人上头。正式、广泛表达时 addictive 更通行。',
 'an addicting game；so addicting。',
 'addicting 与 addictive 的常用意思重叠；addicted 才主要说人已经上瘾、着迷的状态。',
 ('He described the new game as addicting.','他形容新游戏让人玩得停不下来。'),('The review calls the series funny and addicting.','评论说这部剧有趣得让人一直想看。'))
R('B4127','从宣告归属、交付，到依赖和难以控制的状态','ADDICT：历史上是交付、投身，现代成瘾义更强','addict → addicted、addiction；addictive、addicting 看引起上瘾的性质。',
 '先分清人、状态和作用：addict 可以说人；addicted 是人的状态；addictive、addicting 常说东西的作用。口语夸张与专业成瘾语境要分别理解。',
 'ad- + dīcere → addīcere、addictus；-ed 状态，-ion 名词，-ive、-ing 作用性质。',
 [['人物、动作与状态','addict · addicted · addiction'],['引起反复使用、难以停下的性质','addictive · addicting']],
 'addicted to 后接名词或 ing；addictive 修饰东西很常见；普通爱好、习惯不自动等于临床成瘾。',
 'The learner compared an addictive game with a player who feels addicted to it.\n\n学习者比较“让人停不下来的游戏”与“觉得自己玩上瘾的玩家”两种说法。','addict addicted addiction addictive addicting')
if __name__=='__main__':save('continuation_20261030_km',ROOTS,WORDS)
