"""Common coarse language explained as vocabulary, with register and history."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
W('fuck','/fʌk/','性交〔极粗俗〕；他妈的、该死〔感叹、强调等〕',
 '它有粗俗性行为动词义，但电影里突然一句 Fuck! 往往只是愤怒、惊讶；What the fuck? 常是很重的怎么回事、搞什么。',
 '英语较早文献已见相应形式，可能接日耳曼语相关材料，具体经低地德语、北欧语或其他路线仍有争论。不是某个王室许可短语的首字母缩写。',
 [['较早英语相应形式；可能的日耳曼语关系','粗俗性行为词，最远路线不确定'],['广泛口语语用发展','感叹、加强语气、固定短语']],
 'What the fuck? 强烈惊讶、愤怒；fuck up 把事情搞砸、出错；not give a fuck 毫不在乎。语气很粗，完整短语的意思常与字面动作拉开。',
 'What the fuck?；fuck up；not give a fuck。','fuck 是单词，不是一个字母缩略词；它与 folk 民间、人民不同。固定语气表达不能每次硬译成性行为。',
 ('“Fuck, I missed the last train,” he said.','“该死，我错过末班车了。”他说。'),('“What the fuck happened to this file?” the character asks.','那个角色问：“这文件他妈的怎么回事？”'),sources=['https://www.etymonline.com/word/fuck'])
W('fucked','/fʌkt/','搞砸、完蛋的；严重损坏的；fuck 的过去式、分词〔粗俗〕',
 '文件没备份，唯一的硬盘又坏了，角色可能说 We’re fucked. 意思是这下我们完了，不是在叙述字面性行为。',
 'fuck + -ed，末尾 /k/ 后的 -ed 读 /t/。过去分词进一步形成严重受损、处境糟糕等口语形容词义。',
 [['fuck + -ed','动词过去、分词形式'],['fucked 的固定口语评价','东西坏透；处境糟糕、完蛋']],
 'The engine is fucked. 引擎彻底坏了；We’re fucked. 我们麻烦大了。语气粗俗、情绪重，普通场合可直接说 broken、in trouble。',
 'completely fucked；We’re fucked.。','fucked up 还可说混乱、不公、精神状态很糟等；单独 fucked 的具体意思仍看对象，不一定等于同一种故障。',
 ('“The engine’s fucked,” the mechanic muttered.','“引擎彻底坏了。”修理工嘟囔道。'),('“If the backup is gone too, we’re fucked,” she said.','“要是备份也没了，我们就完了。”她说。'))
W('fucking','/ˈfʌkɪŋ/','他妈的、极其〔粗俗加强语气〕；fuck 的 -ing 形式',
 'I’m fucking tired 主要把累的程度、说话人的情绪推得很高；不表示疲惫在进行什么性动作。',
 'fuck + -ing。动词形式之外，早已形成修饰名词、形容词等的加强语气用法，后缀并不让每一次出现都成进行时。',
 [['fuck + -ing','动作形式、动作名词'],['强调用法的 fucking','强烈修饰、表达怒气或兴奋等']],
 'a fucking mess 一团他妈的乱局；fucking amazing 好得惊人、太他妈棒了。可表达正面兴奋，也可表达负面情绪，语体始终粗。',
 'fucking tired；a fucking disaster。','very 强调程度却不带同样粗俗语气；fucking 并非每次都负面，但也不能因在夸人就当成礼貌表达。',
 ('“I’m fucking exhausted,” she said after the long walk.','走了很长一段路后，她说：“我他妈累坏了。”'),('“That was fucking amazing,” he whispered after the show.','演出后他小声说：“刚才真是太他妈棒了。”'))
W('fucker','英 /ˈfʌkə/；美 /ˈfʌkər/','混账、讨厌的家伙；难缠的人或东西〔粗俗〕',
 '骂人时可叫人 fucker；对着一个怎么也拧不动的零件，说话人也可能用它骂这个难缠东西。',
 'fuck + -er 的人物名词形式，后来在咒骂、评价中泛用于人或难处理的物件。不是每一次都在按字面描述某人的性行为。',
 [['fuck + -er','动作执行者形式，带粗俗材料'],['泛化的口语称呼','混账；烦人、难处理的家伙或物件']],
 'a nasty fucker 粗俗骂人的称呼；a tricky fucker 也可能粗俗说一个难处理的东西。少数熟人语境会半开玩笑使用，仍需理解其强烈语气。',
 'a tough fucker；this fucker。','-er 在这里造称呼，不能推成一个正式职业；fucker 也不是普通 friend 朋友的等价昵称。',
 ('“This fucker won’t move,” he muttered at the rusty bolt.','他对着生锈螺栓嘟囔：“这破玩意儿就是拧不动。”'),('“The fucker took my tools,” he said angrily.','他生气地说：“那个混账拿走了我的工具。”'))
W('clusterfuck','英 /ˈklʌstəˌfʌk/；美 /ˈklʌstərˌfʌk/','一团混乱；多人、多环节搞成的烂摊子〔粗俗〕',
 '时间撞车、设备没到、负责人互相推诿，一堆问题缠成团；口语可把整个局面骂作 clusterfuck。',
 'cluster 一团、一簇 + fuck 的粗俗加强材料，二十世纪中期已有记录。最初命名、传播的细节有不同说法。',
 [['cluster + fuck','一团聚集与粗俗负面加强'],['现代 clusterfuck','复杂失控、协调混乱的烂局面']],
 'a complete clusterfuck 彻底一团糟；turn into a clusterfuck 变成烂摊子。常用于多环节相互拖累的混乱，情绪很重。',
 'an organizational clusterfuck；a total clusterfuck。','mistake 可以只是一个错误，clusterfuck 通常评价整个混乱局面；不要求真有一群人在进行字面性行为。',
 ('“The whole launch was a clusterfuck,” he complained.','他抱怨：“整个发布搞得他妈一团糟。”'),('The overlapping schedules turned the event into a complete clusterfuck.','彼此冲突的安排把活动搞成了彻底的烂摊子。'))
W('mindfuck','/ˈmaɪndˌfʌk/','令人脑子转不过来的体验；扰乱心智、让人困惑〔粗俗〕',
 '电影最后一幕把前面两小时的理解全部推翻，你脑中一时接不上；口语可能说 That was a mindfuck.。',
 'mind 心智 + fuck 的粗俗扰乱、强烈影响材料。可作名词，也可作动词，重点在认知、心理受到冲击的比喻。',
 [['mind + fuck','对理解、思绪造成强烈扰动的比喻'],['mindfuck 名词、动词','令人困惑的体验；扰乱、操弄心理等']],
 'a complete mindfuck 彻底让人脑子转不过来的体验；a film that mindfucks the audience 粗俗说一部让观众认知混乱的影片。',
 'a surreal mindfuck；a psychological mindfuck。','confusing 只说难理解，mindfuck 情绪更强，也可能带对巧妙反转的惊叹；有时还涉及心理操弄，要看上下文。',
 ('“That ending was a mindfuck,” she said after the film.','看完电影，她说：“那结尾真把我脑子都搅乱了。”'),('The novel’s shifting realities make it a surreal mindfuck.','小说里现实不断切换，读起来像一场让人脑子转不过来的超现实体验。'))
W('cluster','英 /ˈklʌstə/；美 /ˈklʌstər/','一簇、一群；集群；聚集、聚类',
 '小房子挨在一起像一簇，几台机器合起来工作也像一组；核心是若干东西聚成较紧密的一团。',
 '接古英语 clyster 自然长在一起的一群东西，可能与 clot 块、团的词族有关。后由名词发展出聚集、把对象分组的动词。',
 [['古英语 clyster → cluster 名词','自然成簇；靠近的一组对象'],['名词 → 动词及技术用法','聚在一起；把数据分组、组成设备集群']],
 'a cluster of houses 一簇房屋；a star cluster 星团；a server cluster 服务器集群；cluster data 把数据聚类。共同点是成组，不要求每个成员真的黏在一起。',
 'a cluster of；cluster around；a server cluster。','group 群、组很通用，cluster 常强调靠得近、相似或联合成组；clutter 杂乱、杂物是另一个词，不是 cluster 漏一个 s。',
 ('A small cluster of houses stood near the river.','河边有一小簇房屋。'),('The researchers clustered the samples by similarity.','研究人员按相似性将样本分组。'),sources=['https://www.etymonline.com/word/cluster'])
R('B2546','粗俗性行为词；广泛的咒骂、强烈评价与语气表达','FUCK：历史身体词，现代也成为强烈情绪的工具',
 'fucking amazing 可以是极兴奋；the engine is fucked 是坏透了；clusterfuck 说多环节搞成的混乱局面。别把固定口语一律直译成同一个动作。',
 '英语较早时期已有相关形式，可能与日耳曼语材料有关，具体远源和传播路线仍有争论。任何王室许可长句的首字母故事都不是可靠词源。',
 'fuck + -ed → fucked；fuck + -ing → fucking；fuck + -er → fucker；mother + fucker → motherfucker；cluster + fuck → clusterfuck；mind + fuck → mindfuck。后面几词的日常比喻义要作为整词学。',
 [['基本词与语法、强调形式','fuck · fucked · fucking'],['人物、物件的粗俗称呼','fucker · motherfucker'],['一团混乱的局面','cluster · clusterfuck'],['认知、心理冲击的比喻','mindfuck']],
 'fucking 不是每次都进行时；fucked 不只说字面性行为；cluster 是中性群、簇，clusterfuck 则加上很强的混乱、搞砸评价。所有这些口语粗话都要保留语气信息。',
 'The files were fucked, and the whole handover had become a clusterfuck.\n\n文件坏透了，整个交接也搞成了一团烂摊子。','fuck fucked fucking fucker motherfucker cluster clusterfuck mindfuck')
if __name__=='__main__':save('continuation_20261030_rw',ROOTS,WORDS)
