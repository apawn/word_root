"""Cheering, brightening, merrier moods and expressions of delight."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
def S(word,base):
 return ['https://en.wiktionary.org/wiki/'+word+'#English','https://www.etymonline.com/word/'+base]
EXISTING_ROOT_ADDITIONS={
 'B3666':dict(words='cheer cheered cheering cheery cheerier cheeriest cheerily'.split(),label='cheer 从表情、心情到鼓励喝彩',note='cheer 经法语接脸、表情材料，积极心情义逐渐占主流；cheery 加 -y，其比较级和副词改 y 为 i。'),
 'B2929':dict(words='bright brighten brightens brightened brightening'.split(),label='brighten：光线与表情、心情亮起来',note='bright 加动词 -en；相关变亮动词历史很早，现代 brightens、brightened、brightening 按规则扩展。'),
 'B4320':dict(words='merry merrier merriest merrily merriment'.split(),label='merry 的欢乐程度与 merriment 的旧动词背景',note='merry 承古英语 myrge；更远联系短暂、令人忘记时间是一种分析。merriment 的 -ment 接旧动词 merry 欢乐、使欢乐，不把它简化成所有形容词都能直接加 -ment。'),
 'A1697':dict(words='jolly jollier jolliest jollity jollies'.split(),label='jolly 的比较、欢闹与口语乐趣',note='jolly 经法语 jolif，远源未定；不能把北欧节日 jol 当确定起点。jollity 经法语名词 jolivete 一路，现代不是单靠替换 -y 说明全部借入过程。'),
 'B3465':dict(words='joy joyous joyously joyousness joyful joyfully joyfulness'.split(),label='joy 的 -ous、-ful 与副词、性质名词',note='joy 经法语接拉丁喜悦材料；joyous、joyful 平行发展，副词、性质名词分别接 -ly、-ness，不能把所有 -ous 和 -ful 都说成固定完全同义。'),
 'A1740':dict(words='delight delights delighted delighting delightful delightfully delightedly'.split(),label='delight 的喜悦、令人愉快与高兴地',note='delight 接法语、拉丁 delectare 使愉快，gh 不发音；delightfully 接 delightful，delightedly 接 delighted，分别强调令人愉快的方式与当事人的喜悦。'),
}
CHEER=[['晚期拉丁 cara 脸 → 古法语 chiere、chere → cheer','从面容、表情说到它表现出的心情，英语积极心情义逐渐占主流'],['cheer 动词：鼓舞、使振奋、喝彩','给好心情与喊出支持可在现代不同句式里呈现；不只一种动作']]
W('cheered','英 /tʃɪəd/；美 /tʃɪrd/','欢呼、喝彩了；使高兴、振奋了',
 '球进了，全场喊出来，是 cheered；坏心情被一个好消息托起来，也可以说 the news cheered me。',
 'cheer + -ed，词尾读 /d/；基础词从脸、表情发展到心情，再有鼓舞、喝彩的动词用法。',CHEER+[['cheer + -ed → cheered','过去喊出支持，或让人心情好起来']],
 'cheered the team 为球队喝彩；cheered me up 让我振作；was cheered by the news 因消息而振奋。',
 'cheered loudly；cheered him on 给他加油。',
 'cheered 不一定有喊声，the message cheered me 就是消息让我高兴；主语和宾语决定场景。',
 ('The crowd cheered when the final goal went in.','最后一球进了，全场欢呼。'),('Her kind message cheered me up.','她亲切的消息让我振作起来。'),sources=S('cheered','cheer'))
W('cheering','英 /ˈtʃɪərɪŋ/；美 /ˈtʃɪrɪŋ/','正在欢呼、喝彩；欢呼声；令人振奋的',
 '看台上还在喊、还在鼓劲，是 cheering；一个消息让人心里提起精神，也叫 cheering news。',
 'cheer + -ing；既可作进行形式、活动名词，也可作令人振奋的形容词。',CHEER+[['cheer + -ing → cheering','鼓励、喝彩过程；也写带来好心情的性质']],
 'cheering fans 欢呼的球迷；loud cheering 响亮的欢呼；cheering news 令人振奋的消息。',
 'cheering someone on；a cheering thought 让人振奋的念头。',
 'cheering fans 多是球迷正在欢呼，cheering news 则是消息让人振奋；-ing 修饰语的关系要看被修饰对象。',
 ('We could hear cheering from the stadium.','我们能听见体育场传来的欢呼声。'),('It was cheering to know that everyone had arrived safely.','知道大家都已安全到达，让人振奋。'),sources=S('cheering','cheer'))
CHEERY=CHEER+[['cheer + -y → cheery','愉快、开朗；与 cheerful 是平行形容词']]
W('cheerier','英 /ˈtʃɪəriə/；美 /ˈtʃɪriər/','更愉快、开朗的；更令人心情好的',
 '屋里多了一点亮色，人说话也多一点笑意，比先前更有精神、让人更愉快，叫 cheerier。',
 'cheery 改 y 为 i，加完整比较级 -er；内层 cheer + -y，不是把 cheerful 截短出来。',CHEERY+[['cheery → cheerier','比较开心、明快的程度']],
 'a cheerier voice 更愉快的声音；look cheerier 显得更开朗；a cheerier room 更明快的房间。',
 'feel cheerier；sound cheerier。',
 'cheerier 可以形容人心情，也能说环境让人感觉明快；不是每次都要求有人在笑。',
 ('She sounded cheerier after hearing from her sister.','收到姐姐的消息后，她声音听起来更愉快了。'),('The yellow curtains made the room feel cheerier.','黄色窗帘让房间显得更明快。'),sources=S('cheerier','cheery'))
W('cheeriest','英 /ˈtʃɪəriɪst/；美 /ˈtʃɪriɪst/','最愉快、最开朗的；最明快的',
 '一群人里，这个人最有笑意、最能让气氛轻松，可以叫 the cheeriest；环境也能因颜色、光线而显得最明快。',
 'cheery 改 y 为 i，加完整最高级 -est；基础 cheer + -y 的结构仍保留。',CHEERY+[['cheery → cheeriest','比较范围内愉快、明快程度最高']],
 'the cheeriest voice 最愉快的声音；the cheeriest person 最开朗的人；the cheeriest room 最明快的房间。',
 'her cheeriest smile；at his cheeriest。',
 'cheeriest 描写表现出的心情或气氛；心里是否完全无忧，并不能只凭一个开朗表情判断。',
 ('She greeted us in her cheeriest voice.','她用最愉快的声音向我们问好。'),('We chose the cheeriest room for the celebration.','我们挑了气氛最明快的房间来庆祝。'),sources=S('cheeriest','cheery'))
W('cheerily','英 /ˈtʃɪərɪli/；美 /ˈtʃɪrɪli/','愉快地；开朗地',
 '一句早安说得带笑、轻快，让听的人也精神一点，这种方式叫 cheerily。',
 'cheery 改 y 为 i，加副词 -ly；不是 cheerful 直接加 -ly 那条，虽然两者意思常接近。',CHEERY+[['cheery → cheerily','以愉快、开朗的方式做事']],
 'said cheerily 愉快地说；waved cheerily 高兴地挥手；greeted us cheerily 开朗地招呼我们。',
 'smiled cheerily；called out cheerily。',
 'cheerily、cheerfully 都常说愉快地，cheerfully 还常见于乐意、不抱怨地做事；实际搭配比硬分两种心情更有用。',
 ('“Morning!” she called cheerily from the doorway.','“早！”她从门口愉快地喊道。'),('He waved cheerily as the train pulled away.','火车开走时，他高兴地挥着手。'),sources=S('cheerily','cheery'))
BRIGHTEN=[['古英语 beorht、bryht 等 → bright','发亮、明亮；历史上也有较早变亮动词'],['bright + 动词 -en → brighten 等形式','使变亮、变得更亮，后来也写表情、心情明朗起来']]
W('brightens','/ˈbraɪtənz/','变亮、使变亮；使人高兴、面露喜色〔第三人称单数〕',
 '灯一开，屋里亮了；听到熟悉的名字，人眼神亮起来、脸上有了笑意，都可以用 brightens。',
 'bright + 动词 -en → brighten，再加 -s，词尾读 /z/；整个词既能带宾语，也能不带宾语。',BRIGHTEN+[['brighten + -s → brightens','它使环境、心情变亮；表情自己亮起来']],
 'brightens the room 使房间明亮；brightens my day 让我一天心情变好；her face brightens 她面露喜色。',
 'brightens up the kitchen；the sky brightens。',
 'her face brightens 没有宾语，是脸上显出喜色；the news brightens her day 有宾语，是消息带来好心情。',
 ('Her face brightens whenever the dog runs to greet her.','每次狗跑来迎接，她脸上就亮起笑意。'),('A vase of flowers brightens the room.','一瓶花让房间显得明快。'),sources=S('brightens','brighten'))
W('brightened','/ˈbraɪtənd/','变亮、使变亮了；心情好转、面露喜色了',
 '原来有点沉的脸，一听好消息就活泛起来，叫 brightened；房间、天空亮起来，也可这样说。',
 'brighten + -ed，词尾读 /d/；bright + -en 的动词层在里面，-ed 只负责现代过去形式。',BRIGHTEN+[['brighten + -ed → brightened','过去环境更亮，或心情、表情好转']],
 'brightened up 高兴、明朗起来；brightened the day 让一天变愉快；the sky brightened 天空亮起来了。',
 'her expression brightened；brightened the walls with paint。',
 'brightened 可说一点好转，不保证整个问题解决；一个电话让人开心些，也可以说 brightened her day。',
 ('He brightened when I mentioned the weekend trip.','我一提周末出游，他就高兴起来。'),('The sky brightened after the clouds moved away.','云散开后，天空亮了起来。'),sources=S('brightened','brighten'))
W('brightening','/ˈbraɪtənɪŋ/','正在变亮、使变亮；心情好转、面露喜色',
 '天色还在一点点亮起来，或人的表情正从低沉转到有笑意，这段变化过程叫 brightening。',
 'brighten + -ing，基础 en 保留；现在分词可接正在发生的光线变化，也可写心理、表情变化。',BRIGHTEN+[['brighten + -ing → brightening','环境或情绪正在明亮、明快起来']],
 'the sky brightening 天空渐亮；brightening the room 让屋里明快；a brightening expression 渐有喜色的神情。',
 'brightening up the day；brightening at the news。',
 'brightening 是变化过程，bright 是已经明亮的性质；描写日出时二者能给出不同时间画面。',
 ('We watched the sky brightening beyond the hills.','我们看着山那边的天空渐渐亮起来。'),('She looked up, her expression brightening.','她抬起头，脸上渐渐露出喜色。'),sources=S('brightening','brighten'))
MERRY=[['古英语 myrge → 中古英语 mirie 等 → merry','令人愉快、悦耳等较广性质，后来常写兴高采烈'],['较远有短暂、令人觉得时间飞快的分析','这层联系保留可能性；现代 merry、merrier、merriest 不需要每次绕回古代假说']]
W('merrier','英 /ˈmeriə/；美 /ˈmeriər/','更欢乐、兴高采烈的',
 '人多一点，笑声多一点，气氛更热闹快乐，就可以说 merrier。谚语 the more, the merrier 就像“人越多越热闹”。',
 'merry 改 y 为 i，加完整比较级 -er；基础双 r 保留，不需要再加第三个 r。',MERRY+[['merry → merrier','比较欢乐、兴高采烈的程度']],
 'the more, the merrier 人越多越热闹；a merrier mood 更欢乐的心情。',
 'look merrier；a merrier gathering。',
 'merrier 比 happier 更容易让人想到有笑声、聚会的欢乐气氛；安静的满足也可 happy，未必很 merry。',
 ('Bring your friends; the more, the merrier.','把朋友们也带来，人越多越热闹。'),('The room grew merrier as more guests arrived.','客人陆续到来，屋里越来越欢乐。'),sources=S('merrier','merry'))
W('merriest','/ˈmeriɪst/','最欢乐、最兴高采烈的',
 '整个聚会里，这一刻笑声最多、大家最放松开心，就可以说 the merriest moment。',
 'merry 改 y 为 i，加完整最高级 -est；保留原有双 r。',MERRY+[['merry → merriest','在范围内把欢快程度推到最高']],
 'the merriest evening 最欢乐的一晚；the merriest laughter 最欢快的笑声。',
 'her merriest smile；at their merriest。',
 'merriest 常适合欢笑、庆祝场景，most satisfied 更偏最满意；愉快可以有不同样子。',
 ('It was the merriest evening we had spent together in years.','那是多年来我们一起度过的最欢乐的一晚。'),('She greeted us with her merriest smile.','她带着最欢快的笑容迎接我们。'),sources=S('merriest','merry'))
JOLLY=[['古法语 jolif、joli → 英语 jolly','欢快、节庆等义，远源未定；北欧 jol 节日来源说存在明显争议'],['现代 jolly：乐呵呵；程度副词很、相当','jollity 经法语名词一路借入；jollies 另有口语乐趣用法']]
W('jollier','英 /ˈdʒɒliə/；美 /ˈdʒɑːliər/','更欢快、乐呵呵的',
 '同样一次聚餐，这次大家更爱笑、更放松，气氛更乐呵，可以说 jollier。',
 'jolly 改 y 为 i，加完整比较级 -er；jolly 的 ly 是基础借词的一部分，不能当普通副词 -ly。',JOLLY+[['jolly → jollier','比较欢快、愉悦的程度']],
 'a jollier atmosphere 更欢快的气氛；look jollier 显得更乐呵；a jollier group 更爱说笑的一群人。',
 'jollier than before；a much jollier evening。',
 'jollier 是形容词比较；jolly good 里的 jolly 是程度用法。两种语法关系要看所修饰的成分。',
 ('The music made the whole occasion feel jollier.','音乐让整个场合显得更欢快。'),('He seemed much jollier after lunch.','午饭后，他看起来乐呵多了。'),sources=S('jollier','jolly'))
W('jolliest','英 /ˈdʒɒliɪst/；美 /ˈdʒɑːliɪst/','最欢快、最乐呵呵的',
 '这群人里，他最爱笑、最能把大家带得开开心心，叫 the jolliest；一场活动也可以欢快到最突出。',
 'jolly 改 y 为 i，加完整最高级 -est；这里比较 jolly 的欢快性质，不是副词 very 的某种最高级。',JOLLY+[['jolly → jolliest','在范围内最欢快、最有愉悦气氛']],
 'the jolliest person 最乐呵的人；the jolliest party 最欢快的聚会。',
 'his jolliest laugh；the jolliest group。',
 'jolliest 常带外露、热闹的欢快感；calmest 是最平静，不是同一种正面状态的程度差。',
 ('He was the jolliest person at the table.','他是桌边最乐呵呵的那个人。'),('It turned out to be the jolliest party of the summer.','结果，那成了这个夏天最欢快的一场聚会。'),sources=S('jolliest','jolly'))
W('jollity','英 /ˈdʒɒləti/；美 /ˈdʒɑːləti/','欢乐、欢闹；愉快热闹的气氛',
 '房间里笑声、玩笑、聊天声交织，大家都很放松，这种外露、热闹的欢乐气氛叫 jollity，较书面。',
 '经古法语 jolivete 等名词借入，接 jolif 欢快词族；现代可与 jolly 对照，但不能只说英语当场把 y 换成 ity。',JOLLY+[['古法语 jolivete 等 → jollity','欢闹、愉快的状态与活动；相关形式经历史借入']],
 'an air of jollity 欢乐的气氛；Christmas jollity 圣诞欢闹；forced jollity 勉强装出的欢乐。',
 'laughter and jollity；the general jollity。',
 'jollity 比 happiness 更容易写大家一起说笑的气氛；内心安静、持久的幸福不必带热闹。',
 ('The room was full of laughter and jollity.','房间里满是笑声和欢乐气氛。'),('There was a hint of forced jollity in his voice.','他的声音里有一点强装欢乐的味道。'),sources=S('jollity','jollity'))
W('jollies','英 /ˈdʒɒliz/；美 /ˈdʒɑːliz/','乐趣、快感〔口语复数〕；逗乐、哄劝〔第三人称单数〕',
 '一个人觉得什么好玩、拿什么取乐，口语常说 get his jollies from it；动词 jollies 则是逗别人开心、哄着往前走。',
 'jolly 的名词复数或动词三单都把 y 改为 ies；名词乐趣与动词逗乐分别看语法，基础仍是欢快词族。',JOLLY+[['jolly → jollies','口语复数乐趣；或逗乐动词三单，改 y 为 ies']],
 'get your jollies from something 从某事取乐；jollies someone along 逗着、哄着某人继续。这个口语名词可带讽刺。',
 'gets his jollies from teasing；jollies the children along。',
 'jollies 不是正式的 joy 同义替换，常含某人图个什么乐的口语评价；有时语境带性意味，也不固定只有那一种。',
 ('He gets his jollies from teasing his friends.','他拿逗朋友取乐。'),('She jollies the children along when they get tired on walks.','散步时孩子们累了，她就逗着他们继续走。'),sources=S('jollies','jolly'))
JOYOUS=[['拉丁 gaudium、gaudia → 法语 joie → joy','喜悦与带来喜悦的事物'],['法语 joios 等 → 英语 joyous；英语 joyful 为平行表达','现代可对应 joy + -ous、joy + -ful，但 joyous 有自己的法语借入史'],['joyous + -ly、-ness；joyful + -ness','把喜悦性质变成方式或性质名词']]
W('joyously','/ˈdʒɔɪəsli/','欢欣地；满心喜悦地',
 '好事一来，笑声、拥抱都盛着喜悦，这种表达方式叫 joyously，常比简单地高兴更有感染力。',
 'joyous + 副词 -ly；joyous 经法语同族形容词借入，不能把整个历史都缩成现代英语 joy 直接加 -ous。',JOYOUS+[['joyous + -ly → joyously','以满心欢喜的方式行动']],
 'laughed joyously 欢欣地笑；celebrated joyously 喜悦地庆祝；greeted someone joyously 满心欢喜地迎接某人。',
 'sang joyously；shouted joyously。',
 'joyously 写喜悦的方式；loudly 只说声音大。声音可以轻，却满是喜悦。',
 ('The children laughed joyously as the dog chased its ball.','狗追着球跑，孩子们欢欣地笑着。'),('They greeted the returning team joyously.','他们满心喜悦地迎接归来的队伍。'),sources=S('joyously','joyous'))
W('joyousness','/ˈdʒɔɪəsnəs/','欢欣、喜悦；充满喜悦的气氛或性质',
 '不再只说某个人很开心，而是把歌声、场面里那股洋溢的喜悦拎出来说，这就是 joyousness。',
 'joyous + 性质名词 -ness；基础形容词有法语借入史，外层后缀把喜悦性质名词化。',JOYOUS+[['joyous + -ness → joyousness','把欢欣的性质或表现作为讨论对象']],
 'the joyousness of the occasion 场合中的欢欣；a sense of joyousness 喜悦感。',
 'music full of joyousness；unrestrained joyousness 无拘束的欢欣。',
 'joy 本身最简洁常见，joyousness 更像专门讨论某种欢欣性质、气氛；具体表达可按句子选。',
 ('The music captured the joyousness of the celebration.','音乐表现出了庆典中的欢欣。'),('There was a sense of joyousness in the room.','房间里洋溢着一股喜悦。'),sources=S('joyousness','joyous'))
W('joyfulness','/ˈdʒɔɪfəlnəs/','喜悦；充满欢乐的性质、状态',
 '一个笑容、一段歌声，能让人感到里面装满快乐；把这份喜悦的状态当名词，就叫 joyfulness。',
 'joy + -ful → joyful，再加 -ness；ful 只有一个 l，后面接 ness，不改成 full。',JOYOUS+[['joyful + -ness → joyfulness','把充满喜悦的性质名词化']],
 'the joyfulness of her smile 她笑容里的喜悦；a feeling of joyfulness 一种满心欢喜的感觉。',
 'express joyfulness；a song full of joyfulness。',
 'joyfulness 与 joyousness 很接近，日常若只是说喜悦，用 joy 通常更简洁；这里保留派生关系帮助阅读长词。',
 ('The joyfulness of her smile made everyone relax.','她笑容里的喜悦让大家都放松了。'),('The song expresses a simple joyfulness.','这首歌表达了一种单纯的喜悦。'),sources=S('joyfulness','joyous'))
DELIGHT=[['拉丁 delectare 使愉快 → 古法语 delit、delitier 等 → delight','英语早期写 delit、delite；gh 后来受 light 等拼写影响出现，不发音'],['delight 名词喜悦、乐趣；动词使喜悦、从中取乐','现代 delightful 令人愉快，delighted 感到高兴，再分别形成副词']]
W('delights','/dɪˈlaɪts/','乐趣、令人高兴的事物〔复数〕；使高兴、喜爱〔第三人称单数〕',
 '旅途中那些小吃、美景、小惊喜，合起来是 delights；某件事总让她高兴，动词也写 delights。',
 'delight + -s，/t/ 后词尾读 /s/；名词复数和动词三单同形，gh 不发音。',DELIGHT+[['delight + -s → delights','多种乐趣；它使人欢喜，或某人喜爱某事']],
 'the delights of travel 旅行的种种乐趣；delights the children 使孩子们高兴；delights in storytelling 喜欢讲故事。',
 'simple delights 朴素的小乐趣；delights everyone。',
 'delights someone 是使某人高兴，delights in something 是某人从中取乐；宾语结构改变观察方向。',
 ('The little dog delights everyone it meets.','这只小狗让遇见它的人都高兴。'),('We enjoyed the simple delights of walking and good food.','我们享受散步和美食带来的朴素乐趣。'),sources=S('delights','delight'))
W('delighting','/dɪˈlaɪtɪŋ/','正在使人高兴；从中取乐、喜爱',
 '歌手一唱，孩子们就笑起来，是 delighting the children；自己沉浸在小乐趣里，是 delighting in it。',
 'delight + -ing，基础 gh 不发音，/t/ 保留；这里是整个动词的动作形式。',DELIGHT+[['delight + -ing → delighting','使别人愉快或自己从中取乐的过程']],
 'delighting the audience 让观众欢喜；delighting in small things 从小事中取乐。',
 'a performer delighting children；delighting in the attention 因受关注而高兴。',
 'delighting 是动作形式，delightful 是令人愉快的性质；an act is delighting the crowd 与 a delightful act 句法不同。',
 ('The magician was delighting the children with simple tricks.','魔术师用简单的戏法逗得孩子们很开心。'),('She walked slowly, delighting in every new flower she saw.','她慢慢走着，每看到一朵新开的花都很欢喜。'),sources=S('delighting','delight'))
W('delightfully','/dɪˈlaɪtfəli/','令人愉快地；惬意地；可爱、讨喜地',
 '屋里凉得正好、点心酥得可口、表演妙得让人开心，描述这种让人喜欢的样子，可以用 delightfully。',
 'delight + -ful → delightful，再加副词 -ly；ful 保留一个 l，与 ly 相接成为 fully。',DELIGHT+[['delightful + -ly → delightfully','以令人愉快、讨喜的方式，或修饰这种性质的程度']],
 'delightfully cool 凉爽得很惬意；delightfully simple 简单得讨喜；delightfully funny 有趣得让人开心。',
 'delightfully fresh；a delightfully quiet place。',
 'delightfully 常评价事物给人的愉快感；delightedly 则常写人带着喜悦行动。',
 ('The room was delightfully cool after the heat outside.','从外面的炎热进来，房间里凉爽得很惬意。'),('The story is delightfully funny without being cruel.','这个故事有趣得让人开心，又不刻薄。'),sources=S('delightfully','delight'))
W('delightedly','/dɪˈlaɪtɪdli/','高兴地；满心喜悦地',
 '人真的觉得惊喜，笑着、拍手、答应，动作里满是开心，用 delightedly 就把当事人的喜悦写出来。',
 'delight + -ed → delighted，再加 -ly；基础 /t/ 使 -ed 读 /ɪd/，这个音节在副词里保留。',DELIGHT+[['delighted + -ly → delightedly','以感到喜悦的心情行动']],
 'laughed delightedly 高兴地笑；clapped delightedly 高兴地鼓掌；agreed delightedly 欣然答应。',
 'smiled delightedly；exclaimed delightedly 高兴地叫道。',
 'smiled delightedly 写本人高兴地笑；delightfully funny 则说事物令人愉快，不混成一个万能的愉快副词。',
 ('The child clapped delightedly when the puppet appeared.','木偶一出现，孩子就高兴地拍起手。'),('She laughed delightedly at the surprise.','面对这份惊喜，她开心地笑了。'),sources=S('delightedly','delight'))
def extend_lessons():
 extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_zgf',ROOTS,WORDS)
 extend_lessons()
