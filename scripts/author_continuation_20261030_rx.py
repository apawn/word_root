"""Everyday coarse vocabulary: literal sense, metaphor, and tone."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
W('shit','/ʃɪt/','屎；排便；该死；东西、事情或麻烦〔粗俗〕',
 '字面是排泄物；Shit! 可以只是一声恼火；get your shit together 则是叫人把自己的事理顺、振作起来。很多用法已经是情绪、泛称。',
 '动词接古英语 scitan 一类形式，名词有 scitte 等历史材料，属于古老日耳曼语词族；更早常联系分开、排出的一类重建材料。它不是现代货船警告语的首字母缩略词。',
 [['古英语相应排泄动作、物质名称 → 中古英语形式','排便、排泄物等'],['后续粗俗泛化与情绪用法','糟糕事情、麻烦、泛指东西；感叹']],
 'Shit! 该死！；a lot of shit 可能是很多麻烦或东西；good shit 则可粗俗夸好东西。完整短语、语气决定具体褒贬。',
 'get your shit together；not give a shit；good shit。','sheet /ʃiːt/ 床单、纸张与 shit /ʃɪt/ 元音不同；shit 是粗俗词，feces 是排泄物的较正式名称。',
 ('“Shit, I forgot the tickets,” she said.','“该死，我忘带票了。”她说。'),('“I need to get my shit together before Monday,” he admitted.','他承认：“周一之前，我得把自己的事理顺、振作起来。”'),sources=['https://www.etymonline.com/word/shit'])
W('shitty','/ˈʃɪti/','糟糕、差劲的；恶劣的〔粗俗〕',
 '手机画面糊得不行，说 a shitty camera 是把相机质量狠狠贬低；重点是差，不必真沾着什么脏物。',
 'shit + -y，双写 t。由排泄物相关的负面评价材料，固定成形容质量、感受、待遇等很差的口语词。',
 [['shit + -y','带有粗俗负面评价的性质'],['shitty 的广泛口语义','差劲、糟糕、待遇恶劣等']],
 'shitty weather 糟糕天气；a shitty day 糟糕的一天；a shitty thing to do 很恶劣的一件做法。常在抱怨、批评中使用。',
 'a shitty camera；feel shitty。','dirty 可以客观说脏，shitty 常是情绪化说糟；feel shitty 可能是身体不舒服，也可能是心情很差。',
 ('“This phone has a shitty camera,” he complained.','他抱怨：“这手机的相机真烂。”'),('She had a shitty day and wanted to go home.','她这一天过得很糟，只想回家。'))
W('shitload','英 /ˈʃɪtləʊd/；美 /ˈʃɪtloʊd/','一大堆；非常多〔粗俗〕',
 '不是细数几个，而是把数量夸张成满满一大载；a shitload of emails 就是多得要命的邮件。',
 'shit 的粗俗加强材料 + load 一载、一大批。现代 a shitload of 用来加强很多这个数量判断，不要求对象和粪便有关。',
 [['shit + load','粗俗加强 + 一大载的数量画面'],['a shitload of ...','多得要命的一大批']],
 'a shitload of work 一大堆工作；a shitload of money 很多钱。是夸张数量说法，不给出固定单位或精确数值。',
 'a shitload of emails；a whole shitload。','a lot of 中性，a shitload of 粗俗而有情绪；shitload 形容量大，不直接说明这批东西质量一定差。',
 ('“I have a shitload of emails to answer,” she said.','她说：“我有一大堆邮件要回。”'),('They spent a shitload of time fixing the old machine.','他们花了多得要命的时间修那台旧机器。'))
W('shitshow','英 /ˈʃɪtʃəʊ/；美 /ˈʃɪtʃoʊ/','糟糕混乱、难堪的局面；烂摊子〔粗俗〕',
 '活动现场话筒坏了，流程全乱，台上台下都尴尬；可以把整个过程骂成 a shitshow。',
 'shit 的粗俗负面材料 + show 场面、表演。由表演、场面差劲的画面，泛用于失控、组织混乱、让人难堪的事。',
 [['shit + show','糟糕到像一场难堪表演的场面'],['现代 shitshow','混乱、失败、让人难堪的局面']],
 'turn into a shitshow 变成烂摊子；a complete shitshow 彻底一团糟。可指会议、活动或一连串处理失误，不必是真演出。',
 'an absolute shitshow；a public shitshow。','clusterfuck 常强调多问题缠成复杂混乱；shitshow 更容易突出整个场面糟糕、难堪，两者有重叠。',
 ('“The meeting turned into a shitshow,” he said afterwards.','会后他说：“那场会搞成了一团烂摊子。”'),('The delayed equipment and missing speakers made the event a complete shitshow.','设备迟到、发言人缺席，把活动搞得一塌糊涂。'))
W('shitpost','英 /ˈʃɪtpəʊst/；美 /ˈʃɪtpoʊst/','低质、荒诞、恶搞或挑衅性的帖子；发这类帖子〔网络俚语〕',
 '群里不打算认真论证，故意发个荒诞段子、无关紧要的烂梗，常被叫 shitpost；有时是玩笑，有时会把讨论搅乱。',
 'shit 的低质、无意义评价材料 + post 帖子、发帖。形成网络名词，也直接作动词，按整个词的网络用法理解。',
 [['shit + post','对帖子内容、认真程度的粗俗评价'],['网络名词、动词 shitpost','恶搞、低质等帖子；发此类内容']],
 'a silly shitpost 一个荒诞恶搞帖；shitpost in a group chat 在群里发烂梗、瞎玩。对它的评价可能嫌弃，也可能是发帖者自嘲。',
 'a harmless shitpost；spend time shitposting。','shitpost 不自动等于 false information 假信息；有些本来就是明显笑话、荒诞内容。serious post 则以认真表达、讨论为目的。',
 ('The thread began with a harmless shitpost about office coffee.','帖子串以一个拿办公室咖啡开玩笑的无伤大雅恶搞帖开始。'),('They were shitposting in the group chat instead of discussing the film.','他们在群里发烂梗，没有认真讨论电影。'))
W('bitch','/bɪtʃ/','母狗；讨厌、刻薄的人〔粗鲁辱骂〕；发牢骚',
 '动物语境是母狗；人物语境常是很冒犯的贬称，尤其带有针对女性的侮辱色彩。作动词时又常只是粗鲁地说抱怨、发牢骚。',
 '接古英语 bicce 母狗，更远来源有争论。中古英语时期已用于人物贬称；现代抱怨动词的形成，又可能与 bitchy 及旧的使坏、弄糟义交织。',
 [['古英语 bicce → 中古英语 biche 等','母狗名称'],['人物贬称及后来的口语动词','辱骂人；发牢骚、抱怨']],
 'a bitch with puppies 是动物语境；bitch about the weather 抱怨天气。某事 is a bitch to do 也可粗俗说特别难做、让人烦。',
 'bitch about；a bitch to fix。','bitch /bɪtʃ/ 与 beach /biːtʃ/ 海滩元音不同；动物称呼与人物辱骂的语气也完全不同，不能只按一个中文义套。',
 ('The vet examined the bitch and her puppies.','兽医检查了那只母狗和它的幼崽。'),('He kept bitching about the weather.','他一直在抱怨天气。'),sources=['https://www.etymonline.com/word/bitch'])
W('bitchy','/ˈbɪtʃi/','刻薄、恶意挖苦的；爱挑刺、发脾气的〔非正式、贬义〕',
 '不是认真指出哪里错，而是话里总带刺，专挑让人难堪的地方说。',
 'bitch + -y，取人物贬称词族里的刻薄、恶意等评价，形成形容词。现代常见义不必按母狗的生理特征逐字推。',
 [['bitch + -y','与相应人物评价有关的性质'],['现代常见 bitchy','话语、态度刻薄，恶意挑刺']],
 'a bitchy comment 刻薄评论；a bitchy tone 挖苦人的语气。可形容不同性别的人的说话方式，不只在给某种动物分类。',
 'bitchy remarks；sound bitchy。','critical 批评的可基于事实、帮助改进；bitchy 更突出带恶意、使人难堪的语气。blunt 直率也不必恶毒。',
 ('He made a bitchy comment about her presentation.','他对她的演示作了一句刻薄评论。'),('The review was witty without becoming bitchy.','那篇评论很机智，却没有变得刻薄。'),sources=['https://www.etymonline.com/word/bitch'])
R('B2606','排泄物、排便；粗俗泛指、抱怨与评价','SHIT：从身体词，扩成强烈情绪和东西、事情的泛称',
 'shitty camera 说相机烂；shitload of work 说工作多；shitshow 说场面糟；shitpost 则是网络中的特定帖子或发帖行为。',
 'shit 接古英语排泄动作、物质名称的相应材料，属于古老词族。现代很多固定口语已经主要传递情绪、评价，不能全部按粪便字面翻。',
 'shit + -y → shitty，双写 t；shit + load → shitload；shit + show → shitshow；shit + post → shitpost；bullshit 取胡扯、废话等固定发展。',
 [['基本词与质量评价','shit · shitty'],['数量与混乱局面','shitload · shitshow'],['废话、帖子及网络用法','bullshit · shitpost']],
 'shitload 指数量很多，不说明东西一定差；good shit 可能是粗俗夸奖；shitpost 也不必每次是试图让人信以为真的假信息。',
 'The team had a shitload of work after the meeting turned into a shitshow.\n\n那场会搞成烂摊子后，团队多了一大堆工作。','shit shitty shitload shitshow bullshit shitpost')
R('B3325','母狗；粗鲁人物贬称；刻薄和抱怨的词族','BITCH：动物名称与人物评价分开读',
 'bitch 在动物场景可指母狗，bitchy remark 常是刻薄话；bitch about 又是抱怨某事，不能都按动物来理解。',
 '英语从古英语 bicce 延续动物名词，后来出现人物贬称；抱怨动词与刻薄形容词等又有后续交织。更远词源、个别扩义细节存在争论。',
 'bitch + -y → bitchy。动物名词、人物辱骂、发牢骚动词与刻薄性质，分别按具体句子取义。',
 [['动物称呼与人物贬称','bitch'],['说话态度和抱怨','bitch〔动词〕· bitchy']],
 'bitch 与 beach 发音、含义不同；bitchy 是带恶意的刻薄，不等于所有有根据的批评。',
 'He stopped bitching and replaced the bitchy comment with a useful suggestion.\n\n他不再发牢骚，把那句刻薄话改成了有用的建议。','bitch bitchy')
if __name__=='__main__':save('continuation_20261030_rx',ROOTS,WORDS)
