"""Contemptuous smiles, frowns, radiant smiles and blushing."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
def S(word,base):
 return ['https://en.wiktionary.org/wiki/'+word+'#English','https://www.etymonline.com/word/'+base]
EXISTING_ROOT_ADDITIONS={
 'B2744':dict(words='smile sneer sneers sneered sneering sneeringly frown frowns frowned frowning'.split(),label='笑容、轻蔑与皱眉的表情对照',note='本支比较不同表情，不把 sneer、frown 归为 smile 的同源派生。sneer 有喷鼻息、拟声等可能材料；frown 经法语 frognier，较远鼻孔来源是一种分析。'),
 'B4007':dict(words='beam beams beamed beaming'.split(),label='beam 的发光、灿烂笑与传送',note='树、柱梁的旧名词早已发展出光柱、光束义；动词从发光扩到灿烂笑容、定向传播，beamed 按场景选择。'),
 'A1760':dict(words='blush blushes blushed blushing'.split(),label='blush 的脸红与现代 -ed 词尾',note='blush 可能承古英语 blyscan，较远联系发亮、燃烧材料，现代脸红义单独解释。blushed 的 -ed 在 /ʃ/ 后读 /t/，名词看一眼的旧义保存在 at first blush。'),
}
SNEER=[['早期 sneer 可说马喷鼻息','可能联系北弗里斯兰语轻蔑等材料，较远有拟声联系，具体路线未定'],['后形成轻蔑地笑、说话 → 名词一声冷笑或轻蔑表达','现代可用鼻子哼、嘴角动的形象理解，但不把每个表情细节都当确定历史顺序']]
W('sneer','英 /snɪə/；美 /snɪr/','讥笑；冷笑；轻蔑地说；轻蔑的表情或话',
 '嘴角一动，像在说“这也配？”；或者声音里明摆着瞧不起人，这叫 sneer。它能是表情，也能是语气。',
 '早期有喷鼻息义，更早可能接北弗里斯兰语轻蔑词及相关拟声材料；现代动词又形成名词。',SNEER,
 'sneer at someone 讥笑、轻视某人；with a sneer 带着冷笑；sneer a reply 轻蔑地回话。',
 'a contemptuous sneer；sneer at an idea。',
 'smirk 常像自鸣得意地笑，sneer 更明确把轻蔑朝别人、某事投过去；两种表情可能同时出现。',
 ('There is no need to sneer at someone who is still learning.','没必要讥笑还在学习的人。'),('He answered with a sneer.','他带着轻蔑的冷笑回答。'),sources=S('sneer','sneer'))
W('sneers','英 /snɪəz/；美 /snɪrz/','讥笑、轻蔑地说〔第三人称单数〕；冷笑、轻蔑话〔复数〕',
 '他总把别人的尝试看得不值一提，讲话带着“不过如此”的感觉，动词用 sneers；一连串冷嘲也能叫 sneers。',
 'sneer + -s，词尾读 /z/；动词三单、名词复数同形，基础词有喷鼻息与轻蔑材料的历史。',SNEER+[['sneer + -s → sneers','他、她轻蔑地笑、说；多个冷笑或讥讽']],
 'sneers at the suggestion 轻蔑地讥笑建议；cruel sneers 刻薄的冷嘲；sneers that 后接轻蔑话的内容。',
 'sneers at beginners；comments and sneers。',
 'criticizes 可以有理有据地批评，sneers 着重轻蔑态度，不保证提出了任何有用理由。',
 ('He sneers at any idea that is not his own.','只要不是他自己的想法，他都轻蔑地讥笑。'),('She ignored their sneers and continued practising.','她没理会他们的冷嘲，继续练习。'),sources=S('sneers','sneer'))
W('sneered','英 /snɪəd/；美 /snɪrd/','冷笑、讥笑了；轻蔑地说了',
 '刚才那句话的字面也许普通，语气却像在贬低人，就能用 sneered 标出说话的态度。',
 'sneer + 完整 -ed，词尾读 /d/；既可接 at 说讥笑对象，也可接引语呈现轻蔑话语。',SNEER+[['sneer + -ed → sneered','过去轻蔑地笑或说']],
 'sneered at the attempt 讥笑那次尝试；sneered in reply 冷笑着回应。',
 'sneered that it was easy；sneered at the result。',
 'said 中性标明说了，sneered 同时告诉读者话里的轻蔑；写对话时一个动词就能改变声音。',
 ('“Is that your best idea?” he sneered.','“这就是你最好的主意？”他轻蔑地说。'),('They sneered at our first attempt, but we tried again.','他们讥笑我们第一次的尝试，但我们又试了一次。'),sources=S('sneered','sneer'))
W('sneering','英 /ˈsnɪərɪŋ/；美 /ˈsnɪrɪŋ/','正在冷笑、讥讽；轻蔑嘲讽的',
 '话里一直带着瞧不起人的劲，或者脸上挂着冷笑，叫 sneering。形容声音、评论时，就不只是一瞬嘴角动作。',
 'sneer + -ing；动作形式也作形容词，描述语气、表情、评论里轻蔑的性质。',SNEER+[['sneer + -ing → sneering','轻蔑表达正在进行；也作为语气、表情的性质']],
 'a sneering tone 轻蔑的语气；sneering comments 讥讽的评论；sneering at someone 正在讥笑某人。',
 'a sneering smile；stop sneering。',
 'joking 可以友好，sneering 强调轻蔑；把它用来形容玩笑，会让读者感觉有人被看低。',
 ('I did not like the sneering tone of his reply.','我不喜欢他回答时那种轻蔑的语气。'),('She was tired of people sneering at her accent.','别人总讥笑她的口音，让她很厌烦。'),sources=S('sneering','sneer'))
W('sneeringly','英 /ˈsnɪərɪŋli/；美 /ˈsnɪrɪŋli/','轻蔑嘲讽地；冷笑着',
 '同样一句“你真聪明”，真心说是夸奖，带着瞧不起人的冷笑说，就可以用 sneeringly 写明这个方式。',
 '形容词 sneering + 副词 -ly；内层 sneer + -ing 保留，把轻蔑的性质再变成说、笑等动作的方式。',SNEER+[['sneering + -ly → sneeringly','以轻蔑、讥讽的方式表达']],
 'said sneeringly 轻蔑地说；smiled sneeringly 轻蔑地笑；referred to something sneeringly 带着嘲讽提到某物。',
 'replied sneeringly；asked sneeringly。',
 'sneering 是形容词可修饰 tone，sneeringly 修饰 said、asked 等动作；一个写什么样的语气，一个写怎样说。',
 ('“You call that a plan?” he asked sneeringly.','“你把那也叫方案？”他轻蔑地问。'),('She spoke sneeringly about people who had less experience.','她说起经验较少的人时，语气充满轻蔑。'),sources=S('sneeringly','sneer'))
FROWN=[['古法语 frognier 等皱眉、喷鼻息、翘鼻材料 → frown','更远可能联系高卢语鼻孔材料，但具体路线未定'],['眉头收紧、显不快 → 对某事不赞同；名词皱眉','现代也会因疑惑、专心或担忧而皱眉，不只表示愤怒']]
W('frown','/fraʊn/','皱眉；表示不赞同；皱眉的表情',
 '眉头往中间收，额头紧起来，就是 frown。可能不高兴，也可能在费劲想、没听懂，别急着一律理解成生气。',
 '经古法语 frognier 等借入，更早鼻孔、喷鼻息的来源联系保留可能性；名词由动词形成。',FROWN,
 'frown at the screen 皱眉看屏幕；with a frown 皱着眉；frown on cheating 不赞同作弊。',
 'a puzzled frown 疑惑的皱眉；frown in concentration 专注地皱眉。',
 'frown on 是对某事不赞同的固定搭配，不要求真有一张正在皱眉的脸；scowl 更常把怒气、不快写得更强。',
 ('I tend to frown when I am trying to solve a difficult problem.','我努力解难题时，往往会皱起眉头。'),('The school does frown on cheating.','学校确实不赞同作弊行为。'),sources=S('frown','frown'))
W('frowns','/fraʊnz/','皱眉、不赞同〔第三人称单数〕；皱眉的表情〔复数〕',
 '她看不懂一条信息，眉头收起来，动词用 frowns；周围几张脸都带疑惑，名词也可用 puzzled frowns。',
 'frown + -s，词尾读 /z/；名词复数与动词三单同形，ow 在这里读 /aʊ/。',FROWN+[['frown + -s → frowns','他、她皱眉或不赞同；几次皱眉表情']],
 'frowns at the message 皱眉看消息；frowns on waste 不赞同浪费；worried frowns 担忧的皱眉。',
 'frowns in confusion；draws frowns 引来不赞同的皱眉。',
 'frowns at 往往是朝某人、某物皱眉，frowns on 常直接表达不赞同某种做法；介词帮助分义。',
 ('She frowns whenever the instructions are unclear.','说明一不清楚，她就皱眉。'),('His rude remark drew frowns around the table.','他那句无礼的话让桌边的人都皱起眉。'),sources=S('frowns','frown'))
W('frowned','/fraʊnd/','皱眉了；对某事表示不赞同了',
 '刚才听到一句话，眉头一下收紧，叫 frowned；过去某种做法一直不被赞同，也常写 was frowned on。',
 'frown + -ed，词尾读 /d/，结尾 /nd/；基本元音 /aʊ/ 保留。',FROWN+[['frown + -ed → frowned','过去皱眉；也用于不被赞同的被动表达']],
 'frowned at the result 皱眉看结果；frowned in confusion 疑惑地皱眉；was frowned upon 不被赞同。',
 'frowned over the figures 皱眉思考数字；frowned slightly。',
 'frowned 需要上下文解释态度；a worried frown 可以担心，an angry frown 才明确生气。',
 ('He frowned at the unexpected result.','看着出乎意料的结果，他皱起了眉。'),('Taking calls during dinner was frowned upon in their family.','他们家不赞成吃晚饭时接电话。'),sources=S('frowned','frown'))
W('frowning','/ˈfraʊnɪŋ/','正在皱眉；眉头紧锁的',
 '眉头还收着，人正对问题费神或感到不快，这种正在发生的表情叫 frowning。',
 'frown + -ing；可作进行形式，也作修饰语，描述某人的皱眉神态。',FROWN+[['frown + -ing → frowning','眉头收紧正在发生；也描述这种表情']],
 'frowning at the figures 皱眉看数字；a frowning face 皱着眉的脸；frowning in concentration 专心地皱眉。',
 'stood frowning；stop frowning。',
 'frowning 常把眉部表情写清楚，worrying 是担心的心理或让人担心的性质；有时同现，但不是同一个观察角度。',
 ('She stood frowning at the confusing diagram.','她站着皱眉看那张难懂的示意图。'),('He was frowning in concentration as he read.','他读着读着，专注地皱起了眉。'),sources=S('frowning','frown'))
BEAM=[['古英语 beam：树、柱梁，也有光柱、光束义','光束义很早，常联系光柱形象，不把所有词义都从现代木梁临时造出'],['beam 发光 → 灿烂地笑；定向发送','现代 beamed 可把笑容明亮、传输信号分别放进场景']]
W('beamed','/biːmd/','喜笑颜开了；发出光芒了；定向传送了',
 '孩子看见礼物，脸上的笑像灯亮起来，这叫 beamed；信号像一束东西被送到远处，也能用 beamed。',
 'beam + -ed，词尾读 /d/；动词接光束名词发展，笑容明亮、信号发送是不同的后来用法。',BEAM+[['beam + -ed → beamed','过去发光、灿烂笑或定向传送']],
 'beamed at me 向我灿烂地笑；beamed with pride 满脸骄傲喜悦；beamed images back 把图像传回。',
 'beamed across the room 隔着房间喜笑颜开地看；beamed by satellite 由卫星传送。',
 'smiled 是一般微笑，beamed 更像整张脸都亮了起来；信号场景则按发送理解，不是设备在笑。',
 ('She beamed with pride when her name was called.','名字被叫到时，她满脸骄傲，笑得灿烂。'),('The spacecraft beamed images back to Earth.','航天器把图像传回了地球。'),sources=S('beamed','beam'))
BLUSH=[['中古英语 bluschen 等发亮、看材料 → blush','可能接古英语 blyscan，较远有发亮、燃烧词族联系'],['现代脸红义；名词也说红晕、腮红','旧看一眼的名词义保存在 at first blush，不能把该短语一律直译为第一次脸红']]
W('blush','/blʌʃ/','脸红；红晕、淡红色；腮红；初看〔固定搭配〕',
 '别人一夸，脸颊就红起来，是 blush；化妆时把脸颊添一点红润的产品，也叫 blush。at first blush 则是初看、乍看。',
 '可能承古英语 blyscan 与较早发亮、看材料，现代脸红义后来很常见；旧 look、glance 的名词用法保存在固定短语。',BLUSH,
 'blush with embarrassment 尴尬得脸红；a faint blush 一点红晕；apply blush 上腮红；at first blush 初看。',
 'make someone blush 让某人脸红；a blush of pink 一抹淡粉红。',
 'blush 常有害羞、尴尬或被赞美触动的场景；turn red 更一般，未必说明什么情绪。',
 ('You are making me blush with all those compliments.','你夸这么多，都让我脸红了。'),('At first blush, the two plans seem almost identical.','乍一看，这两个方案似乎几乎一样。'),sources=S('blush','blush'))
W('blushes','/ˈblʌʃɪz/','脸红〔第三人称单数〕；红晕、害羞脸红〔复数〕',
 '她一被夸奖，脸就红，动词用 blushes；save someone’s blushes 像替人把脸红的尴尬遮过去，意思是帮人解围。',
 'blush + -s，/ʃ/ 后词尾读 /ɪz/；动词三单与名词复数同形。',BLUSH+[['blush + -s → blushes','他、她脸红；几次红晕、羞赧的固定表达']],
 'blushes easily 容易脸红；save someone’s blushes 帮人解围、免其尴尬；spare someone’s blushes 同样可说替人避免尴尬。',
 'blushes at a compliment；spare my blushes。',
 'save her blushes 不一定真的看见她脸红，而是帮她避免难堪；不能只按挽救红色理解。',
 ('She blushes whenever someone praises her work.','每次有人夸她的作品，她都会脸红。'),('He changed the subject to spare my blushes.','他换了话题，替我解了围。'),sources=S('blushes','blush'))
W('blushed','/blʌʃt/','脸红了；泛起红晕了',
 '话刚听完，脸颊红起来，像颜色一下浮上皮肤，过去这个变化叫 blushed。',
 'blush + 完整 -ed，/ʃ/ 后词尾读 /t/，结尾 /ʃt/；拼写不是按听感只写一个 t。',BLUSH+[['blush + -ed → blushed','过去因情绪等脸红，或泛起红色']],
 'blushed with embarrassment 尴尬得脸红；blushed at the compliment 听到夸奖脸红了。',
 'blushed deeply 脸涨得很红；blushed and looked away。',
 'blushed 说明脸红的反应，不保证是撒谎；害羞、被夸、尴尬都可能让人物在故事里 blush。',
 ('She blushed when everyone began to applaud.','大家开始鼓掌时，她脸红了。'),('He blushed and looked down at his shoes.','他脸红了，低头看着自己的鞋。'),sources=S('blushed','blush'))
W('blushing','/ˈblʌʃɪŋ/','正在脸红；泛着红晕的；羞赧的',
 '脸上的红色还没退，人还在害羞或尴尬，这个正在发生的反应叫 blushing；也能直接描述红着脸的人。',
 'blush + -ing；可作进行形式，也作形容词，红润色彩还可用于花朵等描写。',BLUSH+[['blush + -ing → blushing','正在脸红；也描述羞赧、带红晕的样子']],
 'a blushing face 红着的脸；the blushing bride 羞赧的新娘，带传统描写色彩；blushing at the praise 因赞美而脸红。',
 'blushing cheeks；stop blushing。',
 'blushing 写颜色反应及常见情绪气氛；embarrassed 直接写尴尬心理，不要求一定看得出脸红。',
 ('I could feel myself blushing as I accepted the gift.','接过礼物时，我能感觉到自己脸红了。'),('She stood smiling and blushing while we sang.','我们唱歌时，她站在那里，一边笑一边脸红。'),sources=S('blushing','blush'))
def extend_lessons():
 extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_zgd',ROOTS,WORDS)
 extend_lessons()
