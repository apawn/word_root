"""Sulky, glum, grumpy and grouchy: different shades of bad temper."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
def S(word,base):
 return ['https://en.wiktionary.org/wiki/'+word+'#English','https://www.etymonline.com/word/'+base]
EXISTING_ROOT_ADDITIONS={
 'A1697':dict(words='glum glummer glummest grumpy grumpier grumpiest sulky sulkier sulkiest'.split(),label='glum、grumpy、sulky 的比较程度',note='glummer、glummest 双写 m 加 -er、-est；grumpier、sulkier 一路改 y 为 i 加完整词尾。这里是后缀与近义情绪比较，不作全组同源归并。'),
 'A1699':dict(words='grumpy grumpier grumpiest grumpily grumpiness grouch grouches grouched grouching grouchy grouchiness'.split(),label='grumpy、grouchy 的坏脾气性质',note='grumpy 接 grump 加 -y，grouchy 接 grouch 加 -y；两组更早来源都有讨论，不因为像 gr- 开头就说一个由另一个派生。grouch 的不快状态名词先有，现代人物义稍后。'),
 'A1740':dict(words='sulky sulkier sulkiest sulkily glum glumly grumpy grumpily'.split(),label='生闷气、低落、易烦躁的方式副词',note='sulkily、grumpily 改 y 为 i 加 -ly；glumly 是 glum 加 -ly。sulky 的记录早于动词 sulk，不画成先有短动词再加 y 的确定历史。'),
 'A1839':dict(words='glum glumness grumpy grumpiness grouchy grouchiness'.split(),label='glumness、grumpiness、grouchiness 的性质名词',note='glum 接 -ness，两个 -y 形容词改 y 为 i 加 -ness。glum 与中古英语 gloumen、gloom 的材料相关，古英语 glom 暮色不是已证实祖先。'),
}
SULKY=[['英语 sulky 的较早记录：沉默、带怨气','具体更早来源未定，有迟缓、倦怠材料等分析'],['sulky → 后来逆构 sulk；现代比较、方式扩展','学习时可从短词到长词排，历史上却不是短的动词一定先出现']]
W('sulkier','英 /ˈsʌlkiə/；美 /ˈsʌlkiər/','更闷闷不乐的；更爱生闷气的',
 '本来还会回话，后来脸一沉、嘴一闭，更不愿理人，这种生闷气的样子变重了，就是 sulkier。',
 'sulky 改 y 为 i，加完整比较级 -er；基础 sulky 来源未定，记录早于从中逆构的 sulk。',SULKY+[['sulky → sulkier','比较沉默带怨气、生闷气的程度']],
 'get sulkier 变得更爱生闷气；a sulkier expression 更闷闷不乐的表情。',
 'sulkier than before；even sulkier 更加闷闷不乐。',
 'sulkier 比 sadder 更突出带怨气、以沉默拒人；伤心不一定会不理别人。',
 ('He grew sulkier when nobody agreed with him.','没人赞同时，他越发沉着脸生闷气。'),('She looked even sulkier after we changed the plan.','我们改了计划后，她看起来更闷闷不乐了。'),sources=S('sulkier','sulky'))
W('sulkiest','/ˈsʌlkiɪst/','最爱生闷气的；最闷闷不乐的',
 '几种表情里，这一张最沉、最不想搭理别人，可以叫 the sulkiest；它把无声怨气的程度推到最高。',
 'sulky 改 y 为 i，加完整最高级 -est；不是仅加 -st。',SULKY+[['sulky → sulkiest','在范围内沉默怨气最明显']],
 'the sulkiest expression 最闷闷不乐的表情；one of the sulkiest characters 最爱生闷气的角色之一。',
 'the sulkiest face；the sulkiest person in the room。',
 'sulkiest 比较的是这种神态、脾气，不等于人生最痛苦；情绪种类与程度要分开。',
 ('He put on his sulkiest face when told to tidy the room.','一听要收拾房间，他就摆出最不高兴的脸。'),('She was the sulkiest character in the story.','她是故事里最爱生闷气的角色。'),sources=S('sulkiest','sulky'))
W('sulkily','/ˈsʌlkɪli/','闷闷不乐地；赌气、带怨气地',
 '嘴上只回一个字，脸转到一边，不高兴却不明说，这种做事、回答的方式叫 sulkily。',
 'sulky 改 y 为 i，加副词 -ly → sulkily；修饰 replied、walked 等动作，说明带着无声怨气。',SULKY+[['sulky → sulkily','把沉默生闷气的性质变成行动方式']],
 'replied sulkily 赌气地回答；walked away sulkily 闷闷不乐地走开；sat sulkily 赌气地坐着。',
 'muttered sulkily；turned away sulkily。',
 'quietly 只说安静，sulkily 还写不高兴、怨气；不说话可以很平静，不一定是在赌气。',
 ('“Fine,” he replied sulkily.','“行吧。”他赌气地答道。'),('She sat sulkily in the corner while the others played.','别人玩耍时，她赌气地坐在角落里。'),sources=S('sulkily','sulky'))
GLUM=[['中古英语 gloumen 等暗下、阴沉地看材料 → glum','也有低地德语 glum 等影响分析；与 gloom 的旧材料相关，较远来源未定'],['不快、阴沉的表情 → 现代沮丧、闷闷不乐','不接成已证实的古英语 glom 暮色路线，也不必把现代 gloom 名词排在所有形式之前']]
W('glum','/ɡlʌm/','沮丧的；闷闷不乐的；神情阴沉的',
 '好消息没等来，脸上的光像暗下去，人不太说话、提不起劲，这种样子叫 glum。常从脸和气氛看出来。',
 '接中古英语 gloumen 等材料，或受低地德语相关形式影响；较远来源未定，glum 与 gloom 的现代形式差异不能代替历史依据。',GLUM,
 'look glum 显得沮丧；a glum face 闷闷不乐的脸；glum silence 低落沉闷的安静。',
 'feel glum；a glum expression。',
 'glum 常写低落、不快的神态，sulky 更常带怨气、不愿理人的行为；人可以 glum 却仍愿意好好说话。',
 ('He looked glum after hearing the result.','听见结果后，他显得很沮丧。'),('Do not be so glum; we can try again tomorrow.','别这么闷闷不乐，明天我们还能再试。'),sources=S('glum','glum'))
W('glummer','英 /ˈɡlʌmə/；美 /ˈɡlʌmər/','更沮丧的；神情更阴沉的',
 '原来还有点笑意，消息一来，脸又沉下去一截，叫 glummer。比较的是低落、不快的程度。',
 'glum 双写末尾 m，加完整比较级 -er → glummer；基础不是 glummy，所以不改 y。',GLUM+[['glum → glummer','双写 m，加 -er，比较阴沉低落程度']],
 'look glummer 显得更沮丧；grow glummer 情绪、神情更加低落。',
 'glummer than before；a glummer expression。',
 'glummer 描写情绪、表情更低落，darker 也可写光线更暗；二者不能只按阴暗一词随意替换。',
 ('He looked even glummer when the rain began.','一下起雨，他显得更加沮丧了。'),('The news left us glummer than before.','这消息让我们比先前更低落。'),sources=S('glummer','glum'))
W('glummest','/ˈɡlʌmɪst/','最沮丧、最闷闷不乐的',
 '同样听到坏消息，这一张脸最沉、最没有精神，可以说 the glummest face。',
 'glum 双写 m，加完整最高级 -est → glummest；词尾读 /ɪst/。',GLUM+[['glum → glummest','在比较范围内神情或情绪最低落']],
 'the glummest face 最沮丧的脸；at his glummest 他最闷闷不乐的时候。',
 'the glummest person in the room；the glummest expression。',
 'glummest 常描述场景中的暂时状态；at her glummest 不自动说她平时一直如此。',
 ('He wore the glummest expression I had seen all week.','他脸上那副表情，是我这一周见过最沮丧的。'),('Even at her glummest, she could still make us laugh.','即使最闷闷不乐的时候，她也还能逗我们笑。'),sources=S('glummest','glum'))
W('glumly','/ˈɡlʌmli/','沮丧地；闷闷不乐地',
 '话说得没精神，脸也没亮起来；坐着、看着、点头都带低落气氛，就可以用 glumly。',
 'glum + 副词 -ly，直接相接；不是比较级 glummer 再接词尾。',GLUM+[['glum + -ly → glumly','以低落、闷闷不乐的方式做事']],
 'said glumly 沮丧地说；sat glumly 闷闷不乐地坐着；looked glumly at something 沮丧地看某物。',
 'nodded glumly；waited glumly。',
 'glum 是形容词，looked glum 是看起来沮丧；glumly 修饰看、说等动作，写做事时的低落气氛。',
 ('“We missed the last bus,” she said glumly.','“我们错过末班车了。”她沮丧地说。'),('He sat glumly by the window while the rain continued.','雨一直下，他闷闷不乐地坐在窗边。'),sources=S('glumly','glum'))
W('glumness','/ˈɡlʌmnəs/','沮丧；闷闷不乐；阴沉的神情、气氛',
 '人坐在那里没有笑意，大家也不太说话，把这种低落、阴沉的感觉当成一件东西讨论，就用 glumness。',
 'glum + 性质名词 -ness；不双写 m，双写出现在 glummer、glummest，后缀规则不同。',GLUM+[['glum + -ness → glumness','把低落、不快的性质或气氛名词化']],
 'shake off the glumness 摆脱低落；an air of glumness 一种闷闷不乐的气氛。',
 'the glumness in his voice；a moment of glumness。',
 'glumness 是 glum 的性质名词，gloom 有阴暗、忧郁等独立用法；二者相关但不是所有搭配都一一替换。',
 ('The good news lifted the glumness in the room.','好消息一扫房间里的低落气氛。'),('There was a note of glumness in his voice.','他的声音里带着一点沮丧。'),sources=S('glumness','glum'))
GRUMPY=[['grump：不快、抱怨材料 → grumpy','grump 更早来源未定，可能联系 grum，或受 grumble、grunt 等影响'],['grump + -y → grumpy，再加程度、方式、性质词尾','早期不快状态名词先有，现代爱抱怨的人义是较晚发展，不倒排全部记录']]
W('grumpier','英 /ˈɡrʌmpiə/；美 /ˈɡrʌmpiər/','更烦躁、脾气更不好的',
 '原来还耐着性子，后来一点小事就不高兴，说话也更冲，叫 grumpier。',
 'grumpy 改 y 为 i，加完整比较级 -er；内层是 grump + -y，把不快、爱抱怨当作性质。',GRUMPY+[['grumpy → grumpier','比较易烦躁、脾气不好的程度']],
 'get grumpier 变得更烦躁；grumpier than usual 比平常更没好气。',
 'feel grumpier；a grumpier reply。',
 'glummer 偏更低落，grumpier 偏更容易对事、对人不耐烦；两种不快的外在表现不一样。',
 ('I get grumpier when I skip breakfast.','不吃早饭时，我会更容易烦躁。'),('He sounded grumpier than usual on the phone.','电话里，他听起来比平常更没好气。'),sources=S('grumpier','grumpy'))
W('grumpiest','/ˈɡrʌmpiɪst/','脾气最不好的；最爱抱怨、最烦躁的',
 '这一天里，刚睡醒那会儿最容易嫌烦，叫 at his grumpiest；几个角色里最爱发脾气的，也可叫 the grumpiest。',
 'grumpy 改 y 为 i，加完整最高级 -est；这里 -est 比较的是坏脾气、烦躁程度。',GRUMPY+[['grumpy → grumpiest','把易烦躁的程度放到比较范围内最高']],
 'at her grumpiest 她脾气最不好的时候；the grumpiest customer 最爱抱怨的顾客。',
 'the grumpiest person in the room；his grumpiest voice。',
 'grumpiest 可以写一个时段的状态，不必等于这个人永远难相处；at his grumpiest 就常是暂时一面。',
 ('He is at his grumpiest before his first cup of tea.','喝第一杯茶之前，他脾气最不好。'),('Even our grumpiest neighbour smiled at the puppies.','连我们那位最爱抱怨的邻居，看见小狗也笑了。'),sources=S('grumpiest','grumpy'))
W('grumpily','/ˈɡrʌmpɪli/','没好气地；烦躁地；不耐烦地',
 '别人问一句，自己带着嫌烦的口气回一句，这种做事、说话的方式叫 grumpily。',
 'grumpy 改 y 为 i，加副词 -ly → grumpily；不快的性质被用来描述动作方式。',GRUMPY+[['grumpy → grumpily','以没好气、不耐烦的方式做事']],
 'replied grumpily 没好气地回答；muttered grumpily 烦躁地嘟囔；walked off grumpily 不高兴地走开。',
 'said grumpily；grumpily agreed。',
 'grumpily agreed 是答应了，但态度不高兴；态度副词不能把 agreed 的同意改成拒绝。',
 ('“Not now,” he replied grumpily.','“现在不行。”他没好气地答道。'),('She grumpily agreed to move her bag.','她不高兴地答应把包挪开。'),sources=S('grumpily','grumpy'))
W('grumpiness','/ˈɡrʌmpinəs/','坏脾气；烦躁、不耐烦的状态',
 '不是某一次顶嘴，而是把一段时间里容易嫌烦、没好气的状态拿出来说，这叫 grumpiness。',
 'grumpy 改 y 为 i，加性质名词 -ness；前面的 grump + -y 已经形成形容词。',GRUMPY+[['grumpy → grumpiness','把烦躁、不耐烦的性质作为名词']],
 'morning grumpiness 早晨的坏脾气；a bout of grumpiness 一阵烦躁；forgive someone’s grumpiness 原谅某人一时没好气。',
 'his usual grumpiness；grumpiness after a poor night’s sleep。',
 'grumpiness 常适合轻一些的日常烦躁；rage 是强烈愤怒，不只是同一词的随意替换。',
 ('A bad night’s sleep explained his morning grumpiness.','昨晚没睡好，难怪他早上没好气。'),('She laughed at her own grumpiness after finding the lost keys.','找到丢失的钥匙后，她笑自己刚才那副烦躁样。'),sources=S('grumpiness','grumpy'))
GROUCH=[['十九世纪末英语 grouch：不快状态，后指坏脾气的人','来源未定，可能接 grutching 抱怨等较早材料'],['grouch 名词 → grouch 动词；grouch + -y → grouchy','不快状态名词、人物义、动词和形容词记录不完全按现代长短排序']]
W('grouch','/ɡraʊtʃ/','爱抱怨、脾气坏的人；闹情绪；抱怨',
 '别人提什么都能挑出一点不满，整个人像带着不高兴的刺，口语就能叫 a grouch；动词则是絮絮抱怨。',
 '来源未定，可能接较早 grutching 抱怨材料；不快状态名词先有，人物名词、动词后来各自发展。',GROUCH,
 'an old grouch 老爱抱怨的人；do not be a grouch 别闹情绪了；grouch about the weather 抱怨天气。',
 'a lovable grouch 虽爱抱怨却可爱的人；have a grouch on 闹情绪，较旧口语。',
 'grouch 名词可评价一个人当时的态度，也可写惯常脾气；grump 很接近，都是较口语的坏脾气角色词。',
 ('Do not be such a grouch; come and join us.','别这么闹情绪了，过来和我们一起吧。'),('He likes to grouch about the weather.','他爱抱怨天气。'),sources=S('grouch','grouch'))
W('grouches','/ˈɡraʊtʃɪz/','爱抱怨的人〔复数〕；抱怨、发牢骚〔第三人称单数〕',
 '几个人总没好气、爱挑不满，可以叫 grouches；他一遇到排队就发牢骚，动词也用 grouches。',
 'grouch + -s，/tʃ/ 后词尾读 /ɪz/；名词复数和动词三单同形。',GROUCH+[['grouch + -s → grouches','多个坏脾气的人；他、她发牢骚']],
 'grouches about delays 抱怨耽搁；a pair of old grouches 两个老爱抱怨的人。',
 'grouches all morning；grouches about everything。',
 'grouches 作为人物名词是带评价的称呼，complaints 才是抱怨内容；几个爱抱怨的人并不等于几条意见。',
 ('He grouches about the traffic every morning.','他每天早晨都抱怨交通。'),('The two old grouches were secretly delighted by the party.','那两个老爱抱怨的人，其实心里都为聚会高兴。'),sources=S('grouches','grouch'))
W('grouched','/ɡraʊtʃt/','抱怨、发牢骚了',
 '刚才一路嫌这儿不行、那儿不对，边走边嘟囔不满，就可以用 grouched。',
 'grouch + 完整 -ed，/tʃ/ 后词尾读 /t/；结尾 /tʃt/，不多出 /ɪd/。',GROUCH+[['grouch + -ed → grouched','过去发牢骚、絮絮抱怨']],
 'grouched about the delay 抱怨耽搁；grouched all the way home 一路发牢骚到家。',
 'grouched that the room was cold；grouched under his breath 小声嘀咕抱怨。',
 'grouched 常把小事上的不满、坏脾气写出来；reported a problem 可以中性而有建设性。',
 ('He grouched about the long queue.','他抱怨队伍太长。'),('She grouched all the way home about the rain.','她回家一路都在抱怨下雨。'),sources=S('grouched','grouch'))
W('grouching','/ˈɡraʊtʃɪŋ/','正在抱怨、发牢骚；发牢骚的行为',
 '人还在嘟囔哪里不满意，听的人觉得这种抱怨没完没了，叫 grouching。也能把这类行为当作一件事说。',
 'grouch + -ing；基础 /tʃ/ 保留，现代动词来自名词，再接动作词尾。',GROUCH+[['grouch + -ing → grouching','发牢骚的过程；也可作为行为名词']],
 'grouching about the noise 抱怨噪声；stop grouching 别发牢骚了；constant grouching 不停抱怨。',
 'grouching all day；tired of the grouching。',
 'grouching 更容易带不赞成的语气，discussing a problem 可以中性说讨论问题；态度与内容要分清。',
 ('Stop grouching and tell me what you want to change.','别只顾发牢骚了，告诉我你想改什么。'),('He was grouching about the cold weather.','他正在抱怨天冷。'),sources=S('grouching','grouch'))
W('grouchy','/ˈɡraʊtʃi/','脾气不好的；爱抱怨、易烦躁的',
 '别人正常问一句，自己也容易嫌烦，脸上、语气里都带着不高兴，这样可以说 grouchy。',
 'grouch 的不快名词 + 形容词 -y；形容词的早期记录稍早于人物名词记录，不必因此倒说人物义是唯一基础。',GROUCH+[['grouch + -y → grouchy','从不快状态材料形成易烦躁、坏脾气性质']],
 'feel grouchy 感到烦躁；a grouchy reply 没好气的回答；grouchy in the morning 早上脾气不好。',
 'a grouchy neighbour；get grouchy when tired。',
 'grouchy 与 grumpy 很接近，日常多能互通；都比 sad 更容易写对外表现的不耐烦。',
 ('I get grouchy when I have not slept enough.','睡不够时，我会变得没好气。'),('The supposedly grouchy neighbour was kind to the children.','那位据说脾气不好的邻居，对孩子们却很和善。'),sources=S('grouchy','grouchy'))
W('grouchiness','/ˈɡraʊtʃinəs/','坏脾气；爱抱怨、易烦躁的状态',
 '把今天总嫌这嫌那、容易没好气的状态拎出来说，就用 grouchiness。可以是一阵，也可以是较常见的脾气特点。',
 'grouchy 改 y 为 i，加性质名词 -ness；内层 grouch + -y 先形成形容词。',GROUCH+[['grouchy → grouchiness','把烦躁、爱抱怨的性质名词化']],
 'morning grouchiness 早晨的坏脾气；a spell of grouchiness 一阵烦躁；forgive the grouchiness 包容一时没好气。',
 'tiredness and grouchiness 疲倦和烦躁；usual grouchiness。',
 'grouchiness 指状态、性质，a grouch 才能直接指那个人；不要把性质名词当人物称呼。',
 ('Her grouchiness disappeared after breakfast.','吃过早饭，她那阵坏脾气就消散了。'),('He blamed his grouchiness on the long wait.','他把自己没好气归因于等了太久。'),sources=S('grouchiness','grouchy'))
def extend_lessons():
 extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_zge',ROOTS,WORDS)
 extend_lessons()
