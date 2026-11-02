"""Groups, announcement, stern degrees and visible gestures."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
def S(word,base):return ['https://en.wiktionary.org/wiki/'+word+'#English','https://www.etymonline.com/word/'+base]
EXISTING_ROOT_ADDITIONS={
 'B2901':dict(words='flock flocks flocked flocking'.split(),label='flock：另源的群体、成群聚集',note='与 sheep 比较羊群，不由 sheep 派生。flock 接古英语 flocc 人群、队伍，后来扩大到动物群；是否较远与 folk 同源不确定。群体动词由名词转来；绒毛 flock 另有拉丁 floccus 词线。'),
 'B3820':dict(words='herd herds herded herding'.split(),label='herd → herds、herded、herding：成群与赶成一群',note='古英语 heord 动物群与牧人词族形成关系；动词用于照看、驱赶牲畜，也用于引导人群。现代 herd animals、herd people 的语气须看场景，不等于所有人群都应叫牲畜群。'),
 'C0541':dict(words='herald heralds heralded heralding'.split(),label='herald → heralds、heralded、heralding：传令者到预示',note='herald 经法语接日耳曼语军队 + 管理、统领一类材料，但职务到传令者的具体历史桥梁有难点。英语名词转作宣布、称赞、预示等动词，不能按现代 her + ald 拆。'),
 'B3700':dict(words='stern sterner sternest'.split(),label='stern → sterner → sternest：更严厉、最严厉',note='形容词 stern 接古英语 styrne 等严厉、强硬材料，较远与僵硬词族有关；船尾名词另有掌舵词线。比较级、最高级只接形容词一支。'),
 'C0478':dict(words='shrug shrugs shrugged shrugging'.split(),label='shrug：另源的耸肩；shrug off 不放在心上',note='与 gesture 比较身体动作，不从拉丁 gestus 派生。shrug 接中古英语 shruggen 突然提肩，远源不确定，可能与北欧弯身材料有关；不在乎、疑惑等表达义逐渐固定。'),
 'A1713':dict(words='peck pecks pecked pecking'.split(),label='peck → pecks、pecked、pecking：啄的动作',note='在已有 peck 同族旁补常用动词形式；peck 可能接 pick 的早期变体或低地德语材料。pecking order 从鸡群啄击关系借给人的地位次序，不把计量单位 peck 硬并为鸟啄起源。'),
}
FLOCK=[['古英语 flocc：人群、队伍 → 英语 flock','较远来源不明，与 folk 的联系只是可能'],['扩大到动物群；名词 → flock 成群聚集','现代常见羊群、鸟群、蜂拥的人；绒毛 flock 是另条来源']]
HERD=[['古英语 heord：家畜群，与牧人词形同族','群体、照看、驱赶在同族中形成关系'],['英语 herd 动词：看管、驱赶牲畜 → 集合、引导人群','人群用法可能带拥挤、被赶着走的语气']]
HERALD=[['日耳曼语军队 + 管理、统领材料 → 古法语 heraut 等','到传令、使者职责的具体义桥存在疑点'],['英语 herald 名词：传令者、先兆 → 动词','宣布、赞誉；像先行传令者一样预示接下来的事']]
STERN=[['古英语 stirne、styrne：严厉、强硬 → stern 形容词','较远联系僵硬、不易弯折的词族'],['stern + -er、-est → sterner、sternest','比较严厉程度；船尾 stern 的掌舵词线分开看']]
SHRUG=[['中古英语 shruggen：突然抬肩、缩肩','远源不定，可能接北欧弯身、蹲伏等材料'],['耸肩逐渐固定为疑惑、不在意等表达 → shrug off','像肩膀一抖摆脱负担 → 不放在心上']]
PECK=[['中古英语 pekken：鸟用喙啄','可能联系 pick 的旧变体或低地德语 pekken 等'],['啄食、轻啄 → 轻触式小口动作等现代用法','pecking order 由鸡群啄击的次序借给人的地位次序']]
W('flock','英 /flɒk/；美 /flɑk/','一群〔羊、鸟等〕；成群聚集、蜂拥而至',
 '一群鸟一起飞、一群羊一起走，是 a flock。人一下子往同一个地方涌，也能用动词 flock。共同点是成群行动。',
 '接古英语 flocc 人群、队伍，后来扩大到动物群；较远来源不明。群体名词转成成群聚集的动词，不能把 flock 的所有来历都倒写成最初只指鸟。',FLOCK,
 'a flock of sheep 是一群羊；a flock of birds 是一群鸟；flock to a place 是成群前往某地。',
 'a flock of birds；a flock of sheep；flock to the beach。',
 'flock 群体一支与绒毛、短纤维 flock 的来源不同。现代说动物群时，搭配习惯比“凡是群都用 flock”更重要。',
 ('A flock of birds rose from the field.','一群鸟从田野里飞起。'),('Visitors flock to the coast in summer.','夏天游客成群涌向海边。'),sources=S('flock','flock'))
W('flocks','英 /flɒks/；美 /flɑks/','多群羊、鸟等〔复数〕；蜂拥而至〔第三人称单数〕',
 '一群接一群鸟，是 flocks；一大群人作为单数主语时，the crowd flocks 也能表示人群涌去。先看它数群体还是作动作。',
 'flock + -s → flocks，/k/ 后接 /s/；名词复数与动词第三人称单数同形。',FLOCK+[['flock + -s → flocks','多个群体；或单数主体成群行动']],
 'flocks of birds 是一群群鸟；flocks of sheep 是多群羊；flocks to a venue 是蜂拥前往场地。',
 'flocks of birds；flocks of sheep；flocks to the festival。',
 'birds 数单只鸟，flocks 数由鸟组成的群。three flocks 不是只有三只鸟。',
 ('Flocks of birds gathered on the shore.','一群群鸟聚在岸边。'),('The crowd flocks to the main stage when the band appears.','乐队一出现，人群就涌向主舞台。'),sources=S('flocks','flock'))
W('flocked','英 /flɒkt/；美 /flɑkt/','成群聚集了；蜂拥而至了〔过去式、过去分词〕',
 '消息一出，很多人一起赶到现场，是 flocked to the scene。不是一个一个孤立地来，而是突出了成群涌来的规模。',
 'flock + -ed → flocked，/k/ 后 -ed 读 /t/；不额外增加 /ɪd/ 音节。',FLOCK+[['flock + -ed → flocked','成群聚集动词的过去式、过去分词']],
 'flocked to 是涌向；flocked around 是聚到周围。服装材料语境里 flocked 还可属植绒那条不同来源的词线。',
 'flocked to the beach；flocked around the stage；flocked to see。',
 'flocked 常不及物，说 visitors flocked to the shop；不是普通地用 the shop flocked visitors 表示店聚来游客。',
 ('People flocked to the park for the concert.','人们涌向公园听音乐会。'),('Fans flocked around the entrance.','粉丝们聚在入口周围。'),sources=S('flocked','flock'))
W('flocking','英 /ˈflɒkɪŋ/；美 /ˈflɑkɪŋ/','正在成群聚集；蜂拥而至',
 '一波波游客仍在往小镇来，是 flocking。-ing 把“成群前往”的趋势展开，常见于描述一阵人气。',
 'flock + -ing → flocking，基础词末尾 ck 保留，直接接 -ing；不再额外双写 k。',FLOCK+[['flock + -ing → flocking','现在分词、动名词，表现成群移动的过程']],
 'be flocking to 是正蜂拥前往；flocking around 是正聚在周围。鸟群移动的研究语境也会使用 flocking。',
 'flocking to the town；flocking around the stage；birds flocking together。',
 '群体移动 flocking 与材料植绒 flocking 同形；后者接绒毛那条来源，别因为词形相同就都译成蜂拥。',
 ('Tourists are flocking to the town for the festival.','游客正为节日活动成群赶往小镇。'),('We watched birds flocking together above the marsh.','我们看着鸟儿在湿地上空聚成群。'),sources=S('flocking','flock'))
W('herds','英 /hɜːdz/；美 /hɝdz/','兽群、牧群〔复数〕；驱赶、集合〔第三人称单数〕',
 '几群牛、象，是 herds；牧人把动物赶在一起，是 he herds them。一个数群体，一个说把它们带成群的动作。',
 'herd + -s → herds，/d/ 后接 /z/。herd 接古英语 heord 动物群，名词和看管、驱赶等动词关系相连。',HERD+[['herd + -s → herds','名词复数；或动词第三人称单数']],
 'herds of cattle 是几群牛；herds of elephants 是几群象；herds animals into a field 是把动物赶进田地。',
 'herds of cattle；herds of elephants；herds animals into a pen。',
 'cattle 本身通常配复数动词；a herd of cattle 把一群牛作为集合来看。herds 数的是好几群。',
 ('Herds of elephants moved across the plain.','几群象走过平原。'),('The farmer herds the cattle into the next field.','农场主把牛群赶进旁边的田地。'),sources=S('herds','herd'))
W('herded','英 /ˈhɜːdɪd/；美 /ˈhɝdɪd/','赶到一起了；被引导成群了〔过去式、过去分词〕',
 '把分散的动物赶进围栏，或把乘客一拨拨带进等候室，是 herded。用于人时，可能带“大家被赶着一起走”的感受。',
 'herd + -ed → herded，/d/ 后的 -ed 读 /ɪd/，增加音节；规则过去式、过去分词。',HERD+[['herd + -ed → herded','末音 /d/ 后加 /ɪd/；驱赶、引导的过去形式']],
 'herded into 是被赶进、被集中带进；herded together 是聚拢在一起。宾语可为动物，也可为人。',
 'herded cattle；herded into a room；herded together。',
 'guided 可能是从容地引导；herded 往往更强调成群、统一驱动，可能让人感到拥挤或被催促。',
 ('They herded the sheep into a pen.','他们把羊赶进了围栏。'),('Passengers were herded into a crowded waiting room.','乘客被集中带进一间拥挤的等候室。'),sources=S('herded','herd'))
W('herding','英 /ˈhɜːdɪŋ/；美 /ˈhɝdɪŋ/','驱赶、看管牲畜；集合引导的过程',
 '狗绕着羊群跑，把散开的羊重新聚拢，这样的工作是 herding。它不仅是跟着动物走，还在维持群体的方向和聚合。',
 'herd + -ing → herding；基础词直接接 -ing。牧群名词转作看管、驱赶动词，再形成过程和活动名。',HERD+[['herd + -ing → herding','现在分词、动名词；也作 herding dog 的用途修饰语']],
 'a herding dog 是牧羊、牧畜犬；herding cattle 是赶牛；like herding cats 比喻把一群各行其是的人组织起来很难。',
 'a herding dog；herding cattle；like herding cats。',
 'herding cats 是常见比喻，通常不是建议真的把猫像牲畜一样驱赶；重点是对象各走各的，难以组织。',
 ('The dog was herding sheep towards the gate.','狗正把羊群赶向大门。'),('Organising the volunteers felt like herding cats.','组织这群志愿者，感觉像赶猫一样难。'),sources=S('herding','herd'))
W('heralds','英 /ˈherəldz/；美 /ˈhɛrəldz/','预示、宣告〔第三人称单数〕；传令者、先兆〔复数〕',
 '第一阵暖风像在提前宣布春天来了，可以说 it heralds spring。herald 是先来传消息的人，事物也能借他的角色给下一步报信。',
 'herald + -s → heralds，/d/ 后接 /z/；名词复数与动词第三人称单数同形。动词由传令者名词转来。',HERALD+[['herald + -s → heralds','预示的动词单数；或多个传令者、先兆']],
 'heralds the start of 是预示开始；heralds a new era 是宣告新时代；early heralds of spring 是春天早来的信号。',
 'heralds spring；heralds a new era；heralds a change。',
 'heralds 预示某事，并不要求有一个人在正式宣布；自然迹象也能像传令者一样“报信”。',
 ('The first blossom heralds the arrival of spring.','最早绽放的花预示春天来临。'),('The agreement heralds a new phase of cooperation.','这份协议宣告合作进入新阶段。'),sources=S('heralds','herald'))
W('heralded','英 /ˈherəldɪd/；美 /ˈhɛrəldɪd/','预示了、宣告了；被誉为〔过去式、过去分词〕',
 '新事物被宣传成一个突破，是 was heralded as a breakthrough；一个变化带来下一阶段，则是 heralded the start。都借了向前传消息的角色。',
 'herald + -ed → heralded，基础末音 /d/ 后的后缀读 /ɪd/，增加一个音节。',HERALD+[['herald + -ed → heralded','过去式、过去分词；末尾 /ldɪd/']],
 'was heralded as 是被誉为、被宣传为；heralded a change 是预示了变化；两种搭配关注的不是同一件事。',
 'heralded as a breakthrough；heralded a new era；widely heralded。',
 'heralded as 说明有人这样称赞、宣传，不等于结果一定兑现；理解报道时应分清评价与后来实际表现。',
 ('The product was heralded as a major breakthrough.','这款产品被誉为一项重大突破。'),('The announcement heralded the start of a new partnership.','这项宣布标志着新合作关系的开始。'),sources=S('heralded','herald'))
W('heralding','英 /ˈherəldɪŋ/；美 /ˈhɛrəldɪŋ/','预示着；宣告、称赞的过程',
 '一个迹象已经出现，像传令者走在队伍前面，提示后面的变化快到了，就是 heralding。',
 'herald + -ing → heralding，直接接后缀；不删字母、不双写 d。',HERALD+[['herald + -ing → heralding','现在分词、动名词；预示或宣布过程']],
 'heralding a new phase 是预示新阶段；heralding the arrival of 是宣告、提示某物到来。分词常解释前一件事带来的意义。',
 'heralding a new phase；heralding the arrival of spring；heralding a change。',
 'heralding 指先兆、宣告关系；causing 强调直接造成。一个信号提示变化，不一定就是变化的原因。',
 ('The bells rang, heralding the start of the festival.','钟声响起，宣告节日开始。'),('New buds appeared, heralding the arrival of spring.','新芽冒出，预示春天到来。'),sources=S('heralding','herald'))
W('sterner','英 /ˈstɜːnə/；美 /ˈstɝnɚ/','更严厉、更强硬的；更艰巨的',
 '刚才还温和，换上更严肃的表情，是 a sterner look；接下来的考验更不容易，也能说 a sterner test。像东西更硬、更不让步。',
 'stern + -er → sterner，比较级后缀 -er；形容词接古英语 styrne 等严厉、强硬材料，较远与僵硬词族相关。',STERN+[['stern + -er → sterner','形容词比较级；不用于另源的船尾名词']],
 'a sterner warning 是更严厉的警告；a sterner test 是更艰巨的考验；made of sterner stuff 是更坚强、没那么容易屈服。',
 'a sterner look；a sterner warning；a sterner test。',
 'stern 的船尾义是另一来源，不用 sterner 表示更靠船尾；这里比较的是严厉、强硬或困难程度。',
 ('The teacher gave him a sterner warning.','老师给了他更严厉的警告。'),('The next round will be a sterner test of our skills.','下一轮将更严峻地考验我们的技能。'),sources=S('sterner','stern'))
W('sternest','英 /ˈstɜːnɪst/；美 /ˈstɝnɪst/','最严厉、最强硬的；最艰巨的',
 '一连串考验里，最难让你轻松过关的，是 the sternest test。人的表情、要求也能比出最严厉的一个。',
 'stern + -est → sternest，后缀 -est 表最高级，读 /ɪst/；基础词不改字母。',STERN+[['stern + -est → sternest','一定范围内最严厉、最艰巨']],
 'the sternest warning 是最严厉的警告；the sternest test 是最严峻考验；her sternest voice 是她最严厉的声音。',
 'the sternest warning；the sternest test；her sternest voice。',
 'sternest 常含严肃、不轻易让步；rudest 则侧重失礼。一个人语气 stern，不必然就是 rude。',
 ('She used her sternest voice to quiet the room.','她用最严厉的声音让屋里安静下来。'),('This was the sternest test the team had faced all season.','这是球队整个赛季遇到的最严峻考验。'),sources=S('sternest','stern'))
W('shrug','英、美 /ʃrʌɡ/','耸肩；耸肩动作；不在意地摆脱〔常与 off 连用〕',
 '肩膀往上一提又放下，像在说“不知道”“随你”或“无所谓”，就是 shrug。动作本身不说话，却能表达态度。',
 '接中古英语 shruggen 突然抬肩、缩肩，远源不定，可能联系北欧弯身材料。表达疑惑、不在意等意义逐渐固定；名词耸肩动作由动词形成。',SHRUG,
 'give a shrug 是耸一下肩；shrug your shoulders 是耸肩；shrug off criticism 是把批评甩在一边、不放在心上。',
 'give a shrug；shrug your shoulders；shrug off criticism。',
 '耸肩不只一种意思：可能不知道、无奈，也可能不在乎。解释人物动作时要看对话，不能一律翻成冷漠。',
 ('He answered with a shrug.','他耸了耸肩，算是回答。'),('She tried to shrug off the criticism and keep working.','她努力不把批评放在心上，继续工作。'),sources=S('shrug','shrug'))
W('shrugs','英、美 /ʃrʌɡz/','耸肩〔第三人称单数〕；耸肩动作〔复数〕',
 '他每次被问都耸肩，是 he shrugs；几个人只给几个耸肩回应，也能说 shrugs。动作和态度一起由语境说明。',
 'shrug + -s → shrugs，/ɡ/ 后后缀读 /z/；名词复数和动词第三人称单数同形。',SHRUG+[['shrug + -s → shrugs','多个耸肩动作；或单数主语耸肩']],
 'he shrugs 是他耸肩；shrugs off a setback 是不把挫折放在心上；a series of shrugs 是一连串耸肩回应。',
 'shrugs his shoulders；shrugs off criticism；a series of shrugs。',
 'shrugs his shoulders 与 simply shrugs 都能表达耸肩，不必每次把肩膀宾语补出来才完整。',
 ('She shrugs whenever I ask about the schedule.','每次我问日程，她都耸耸肩。'),('The proposal was met with a few indifferent shrugs.','提议得到的只是几次无所谓的耸肩回应。'),sources=S('shrugs','shrug'))
W('shrugged','英、美 /ʃrʌɡd/','耸肩了；未放在心上〔过去式、过去分词〕',
 '问完之后，他肩膀一提就过去了，是 shrugged；困难来了也没有一直纠缠在心上，可说 shrugged it off。',
 'shrug 双写 g + -ed → shrugged；单音节短元音后一个辅音字母，接后缀时双写。/ɡ/ 后 -ed 读 /d/。',SHRUG+[['shrug 双写 g + -ed → shrugged','过去式、过去分词；后缀 /d/']],
 'shrugged his shoulders 是耸了耸肩；shrugged off the problem 是没把问题放在心上；是否适当由上下文判断。',
 'shrugged his shoulders；shrugged off criticism；shrugged it off。',
 'shrugged off 可能是积极地走出挫折，也可能是草率忽视问题；词本身不保证这种态度值得赞同。',
 ('He shrugged and said he did not know.','他耸耸肩，说自己不知道。'),('She shrugged off the minor setback and tried again.','她没把这点挫折放在心上，又试了一次。'),sources=S('shrugged','shrug'))
W('shrugging','英、美 /ˈʃrʌɡɪŋ/','正在耸肩；耸肩回应；不在意地摆脱',
 '一边说“不确定”，一边耸肩，是 shrugging。动作和说的话并列，能让小说、对话里的态度一下子看得见。',
 'shrug 双写 g + -ing → shrugging；-ing 表动作过程或行为，保留短元音基础的拼写规律。',SHRUG+[['shrug 双写 g + -ing → shrugging','现在分词、动名词；不是 shrugged 的过去时间']],
 'shrugging her shoulders 是她正耸肩；keep shrugging 是一直耸肩回应；shrugging off criticism 是不把批评放在心上。',
 'shrugging her shoulders；shrugging off criticism；keep shrugging。',
 'shrugging 是人物动作，不直接等于一句完整的“不知道”；可以搭配不知道、无奈、不在意等不同台词。',
 ('“Maybe,” she said, shrugging her shoulders.','“也许吧。”她耸着肩说。'),('He kept shrugging off our questions.','他一直对我们的问题不当回事。'),sources=S('shrugging','shrug'))
W('pecks','英、美 /peks/','啄〔第三人称单数〕；轻啄、轻吻〔复数〕',
 '鸟用尖喙一下下点着食物，是 pecks；像这样轻轻点一下的动作，也能借来说轻吻。共同画面是短促接触。',
 'peck + -s → pecks，/k/ 后接 /s/。peck 可能接 pick 的旧变体或低地德语啄的词，名词动作义来自动词。',PECK+[['peck + -s → pecks','动词第三人称单数；轻啄动作的名词复数']],
 'pecks at seeds 是啄种子；pecks at food 也可形容只小口吃一点；quick pecks 可说快速轻啄、轻吻。',
 'pecks at seeds；pecks at the ground；quick pecks。',
 '计量单位 peck 也能有复数 pecks，但较远来源不明；本组先学啄、轻触这一常见动作线，不强并所有同形词。',
 ('The pigeon pecks at seeds on the ground.','鸽子啄着地上的种子。'),('She only pecks at her breakfast before leaving.','她出门前只小口吃一点早餐。'),sources=S('pecks','peck'))
W('pecked','英、美 /pekt/','啄过；轻吻了；只小口吃了〔过去式、过去分词〕',
 '鸟刚在手边点了一下，或人对食物只轻轻吃了几口，都可以用 pecked。动作小而短，不是大口吞下。',
 'peck + -ed → pecked，基础末音 /k/ 后 -ed 读 /t/；拼写 ck 保留，不额外双写 k。',PECK+[['peck + -ed → pecked','过去式、过去分词；读 /pekt/']],
 'pecked at seeds 是啄种子；pecked at lunch 是午饭只吃一点；pecked someone on the cheek 是轻吻面颊。',
 'pecked at seeds；pecked at lunch；pecked her on the cheek。',
 'pecked at food 常突出吃得零零星星、很少；ate the meal 只是吃饭，不包含这种动作与量的感觉。',
 ('The hen pecked at a few grains of corn.','母鸡啄了几粒玉米。'),('He pecked her on the cheek before leaving.','出门前，他轻吻了一下她的面颊。'),sources=S('pecked','peck'))
W('pecking','英、美 /ˈpekɪŋ/','正在啄；啄食；〔pecking order〕地位次序',
 '鸡群里谁能啄谁，反映相对地位；pecking order 后来借给人的等级次序。先看到真实啄击动作，再理解社会里的上下位置。',
 'peck + -ing → pecking，ck 保留直接接 -ing；pecking order 的动物行为用语借入后，再扩展到人的地位秩序。',PECK+[['peck + -ing → pecking','现在分词、动名词；在 pecking order 中作修饰语']],
 'birds pecking at seeds 是鸟正啄种子；the office pecking order 是办公室里的地位次序；low in the pecking order 是地位较低。',
 'pecking at seeds；the pecking order；low in the pecking order。',
 'pecking order 不要求人真的互相啄；比喻的是谁比谁地位高、谁先获得资源或发言机会。',
 ('Several hens were pecking at the ground.','几只母鸡正在地上啄食。'),('It took her a while to understand the office pecking order.','她过了一阵才弄清办公室里的地位次序。'),sources=S('pecking','peck'))
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_zio',ROOTS,WORDS)
 extend_lessons()
