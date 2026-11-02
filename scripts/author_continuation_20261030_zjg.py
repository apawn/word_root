"""Common spoken reductions and exclamations, explained through situations."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
def S(word,base=None):
 a=['https://en.wiktionary.org/wiki/'+word+'#English']
 if word!='shh':a.append('https://www.etymonline.com/word/'+(base or word))
 if word in ['gonna','wanna','gotta']:a.append('https://www.merriam-webster.com/dictionary/'+word)
 return a
EXISTING_ROOT_ADDITIONS={
 'B2871':dict(words='gonna'.split(),label='going to → gonna：口语里的将要、打算',note='gonna 记录表示将来的 going to 的连读弱化，后接动词原形；不是把所有 going to 后接地点的句子都换成 gonna。'),
 'B4134':dict(words='gonna'.split(),label='going to 的口语连读：gonna',note='go 的 going 与 to 在表示将来、打算的结构中连读弱化，形成 gonna 这种非正式写法；保留主语对应的 be。'),
 'B3173':dict(words='wanna'.split(),label='want to → wanna：想要做某事的口语形式',note='wanna 记录 want to 的非正式连读；部分口语还可记录 want a。重点看后接动词还是名词，不另造一个 na 后缀。'),
 'B2869':dict(words='gotta'.split(),label='got to → gotta：必须、得做的口语形式',note='gotta 记录 got to 的连读，常见于 have got to 的必须义，随意口语也可省 have。与机会义 got to、地点义 got to 等完整用法分开看。'),
 'B2733':dict(words='kinda'.split(),label='kind of → kinda：有点、算是的口语弱化',note='kind 名词种类有同族、性质背景；kind of 的近似、稍微义在口语中连读成 kinda，a 记录弱元音，不是新后缀。'),
 'A2265':dict(words='okay'.split(),label='与 yes、yep 对照：okay 的同意、认可',note='这里只对照回应方式，不把 okay 当 -p 派生词。okay 是 OK 按字母读音写出的形式；OK 的有文献支持来源是 all correct 故意拼作 oll korrect 的缩写玩笑。'),
 'B3697':dict(words='hello haha whoa oops ouch phew whew yo ugh huh eh shh hooray'.split(),label='与 wonder、wow 对照：常见呼喊与情绪反应',note='这些词放在一起比较日常情绪、招呼、呼喊，不表示都由 wonder 或 wow 派生。hello 接旧呼喊变体；ouch 常联系德语疼痛呼声；其余多是声音写法、感叹变体，各条分别说明。'),
 'B3720':dict(words='jeez gosh darn'.split(),label='damn、darn 与其他较缓和的感叹用语',note='darn 感叹用法是 damn 的缓和改形；jeez 改自 Jesus，gosh 改自 God，三条来源分开。darn 织补动词另有历史，不能从骂人推成补袜子。'),
}
W('gonna','英、美 /ˈɡənə/，弱读也可 /ɡənə/','将要；打算〔going to 的口语写法〕',
 'I am gonna leave 就是“我打算走了”。把 going to 很快地连起来说，声音压缩了，写出来便成 gonna。',
 'going to 在表示将来、打算的结构中连读弱化 → gonna。这是语音的口语写法，不是 go 加一个表示将来的 -nna 后缀。',
 [['go → going，与 to 组成 going to','表示将来、打算的结构有 go 的动词背景'],['going to 连读弱化 → gonna','保留结构意义，用非正式拼写记录说话声']],
 'I am gonna call 是我要打电话；she is gonna help 是她打算帮忙；it is gonna rain 是要下雨了。gonna 后接动词原形。',
 'am gonna call；is gonna rain；are gonna need help。',
 'I am going to London 里的 to 接地点，不能写成 I am gonna London。若说 I am gonna go to London，gonna 后有动词 go，才是这类结构。',
 ('I am gonna call you after dinner.','我晚饭后打算给你打电话。'),('It is gonna rain, so take an umbrella.','要下雨了，带把伞吧。'),sources=S('gonna'))
W('wanna','英 /ˈwɒnə/；美 /ˈwɑːnə/、/ˈwɔːnə/','想要〔常记录 want to 的口语连读〕',
 'I wanna try 是“我想试试”。want to 连着说，末尾的辅音和弱音被压缩，听起来就成了 wanna。',
 'want to 的非正式连读 → wanna；一些口语写法也用它记录 want a。不是 want 后面加上新造的 -na 词缀。',
 [['want to 连读弱化 → wanna','常接动词原形，表示想做某事'],['口语书写有时也用 wanna 记录 want a','还原哪一个短语，要看后面的词']],
 'wanna try 是想试；wanna come 是想来。只记常用的 want to 对应关系，就足以听懂大量随意对话。',
 'wanna try；wanna come；do not wanna wait。',
 '正式写作用 want to 更合适；wanna 的连读也受句法限制，不能见到相邻的 want、to 就一概替换。',
 ('I wanna try the new game.','我想试试那个新游戏。'),('Do you wanna come with us?','你想和我们一起来吗？'),sources=S('wanna'))
W('gotta','英 /ˈɡɒtə/；美 /ˈɡɑːtə/，口语 t 常闪音','必须；得〔got to 的口语写法〕',
 'I gotta go 就是“我得走了”。说话人把 got to 挤着说，常用来表达眼下必须做的事。',
 'got to 连读 → gotta，常出现在 have got to 必须的结构里；很随意的口语可省 have。现代形式记录语音，不是 got 加特殊后缀。',
 [['have got to → 必须、得做的常见口语结构','got 是 get 的历史形式，但这里按整个结构理解'],['got to 连读弱化 → gotta','I have gotta go；随意说法 I gotta go']],
 'gotta leave 是得走；gotta finish this 是得完成这件事；you have gotta be kidding 表示你一定是在开玩笑。',
 'gotta go；gotta finish this；have gotta be kidding。',
 'I got to meet her 也可说有机会见到她，got to the station 是到车站；不要把所有 got to 都自动解释成必须。',
 ('I gotta leave in five minutes.','我五分钟后就得走了。'),('We have gotta finish this before lunch.','我们得在午饭前完成这件事。'),sources=S('gotta'))
W('kinda','英、美 /ˈkaɪndə/','有点；算是；某种程度上〔kind of 的口语写法〕',
 'I am kinda tired 是“我有点累”。说话人留一点余地，没有把程度说满。',
 'kind of 连读弱化 → kinda；kind 本是种类、性质的名词，kind of 的近似表达发展为口语的有点、算是。末尾 a 记录弱元音。',
 [['kind 种类 → a kind of 一种、类似某种东西','近似、归类的表达提供语义背景'],['kind of 的稍微、算是义 → 连读 kinda','语气较缓和，常放在形容词等前面']],
 'kinda tired 是有点累；kinda strange 是有点奇怪；kinda like it 是算喜欢、还挺喜欢，但说得留有余地。',
 'kinda tired；kinda strange；kinda like it。',
 '它来自 kind of 的非正式连读，不是形容词 kind 善良加词尾。写正式文章时通常用完整形式或更准确的程度词。',
 ('I am kinda tired after the trip.','旅行回来后我有点累。'),('The idea sounds kinda strange, but it might work.','这个想法听起来有点奇怪，但也许能行。'),sources=S('kinda'))
W('okay','英 /əʊˈkeɪ/；美 /oʊˈkeɪ/','好，行；没问题的；尚可；同意，批准',
 '别人提建议，你说 okay，是“行”；问某人是不是 okay，是问有没有事；评价东西 just okay，则只是还可以，没在大力夸。',
 'OK 按字母读音写成 okay。有文献支持的 OK 来源，是美国旧缩写玩笑：把 all correct 故意错拼为 oll korrect，再取首字母。不是从现代 okay 切出词根。',
 [['all correct → 玩笑错拼 oll korrect → OK','早期有文字记录的缩写背景'],['字母读音 → okay；认可、状态尚可等多种用法','又可名词化为许可、动词化为批准']],
 'Are you okay? 是你没事吧；That is okay 是没关系、可以；just okay 是一般般；okay a plan 是批准一个计划。',
 'Are you okay?；That is okay；just okay；okay the plan。',
 'okay 的力度随场景变化：接受提议可以很干脆，评价作品 just okay 则偏普通。别每次都译成非常好。',
 ('Are you okay after the long trip?','长途旅行后，你还好吗？'),('The film was okay, but I would not watch it again.','这部电影还行，但我不会再看一遍。'),('The manager needs to okay the final design.','经理需要批准最终设计。'),sources=S('okay'))
W('hello','英 /həˈləʊ/；美 /həˈloʊ/','你好；喂；用来引起注意或表示发现',
 '碰面先招呼 hello；接电话说 hello，是“喂”；发现一件意外的事，语气一转也可以是“咦，看看这个”。',
 'hello 是 hallo、hollo、holla 等旧呼喊形式的变体，早先有引起注意的作用，后来广用于招呼。电话传播推动它流行，但这个词早于电话。',
 [['旧的招呼、呼喊形式 hallo、hollo、holla 等','声音、拼写长期有多种变体'],['hello → 碰面招呼、电话开头等常用语','从引起注意发展为固定问候，不是由电话发明者造出的全新词']],
 'say hello to someone 是向某人问好；a quick hello 是简单打个招呼；Hello? 升调可能是接电话或确认有人在听。',
 'say hello；say hello to someone；a quick hello。',
 '同一个 hello，平常语气是问候，提高或拉长音可能是在招呼注意、催人回应；具体含义由语调和场景决定。',
 ('She smiled and said hello.','她笑着打了个招呼。'),('Please say hello to your sister for me.','请代我向你姐姐问好。'),sources=S('hello'))
W('haha','英、美 /ˌhɑːˈhɑː/，实际笑声和语调可变','哈哈〔笑声的书写〕',
 '聊天里写 haha，像把笑声放到文字里。可能真觉得好笑，也可能是客气缓和、化解尴尬，要看前后说了什么。',
 '反复写 ha 来模仿笑声，古英语已有相应写法；类似声音在多种语言出现，不能因此说现代英语从其中某一语言直接借来。',
 [['自然笑声 → ha 的文字记录','声音模拟不需要固定古典词根'],['ha 重复 → ha ha、haha 等写法','本条学连写 haha；现代聊天里表达笑声与语气']],
 'Haha, that was funny. 表示笑；Haha, I made the same mistake. 也能缓和承认自己的小失误。重复几个 ha 可改变文字中的笑意强度。',
 'Haha, that was funny.；Haha, me too.；Haha, good one.。',
 '文字 haha 不是精确的情绪测量；简短回应可能热情，也可能敷衍，单凭这个词不能判断对方真实态度。',
 ('Haha, I nearly sent that message to the wrong person.','哈哈，我差点把那条消息发错人。'),('Haha, that is exactly what my cat does.','哈哈，我家猫就是这样。'),sources=S('haha','ha-ha'))
W('whoa','英 /wəʊ/；美 /woʊ/','吁，停；等等；哇〔惊讶〕',
 '马跑着时喊 whoa，让它停；谈话节奏太快、事情发展太猛，也可喊“等等”；看到惊人景象又可以是“哇”。',
 '接旧的远处招呼、让人注意的呼喊变体，后来常作停马口令，也用于阻止、惊讶等。这里是呼声的历史，不按现代 who 谁来逐字翻译。',
 [['旧呼喊形式 → whoa 引起注意、停马等用法','与 ho 等呼声变体有关系'],['停、慢下来 → 谈话中打断；也表达惊讶','现代具体情绪由语调与后句决定']],
 'Whoa, slow down. 是等等、慢点；Whoa, look at that! 是哇，看那个。前者拦住节奏，后者表示震惊。',
 'Whoa, slow down.；Whoa, hold on.；Whoa, look at that!。',
 'whoa 可能是赞叹，也可能是在制止；不要把每次出现都译成赞美式的哇。',
 ('Whoa, slow down and tell me what happened.','等等，慢慢说，告诉我发生了什么。'),('Whoa, that waterfall is huge!','哇，那道瀑布真大！'),sources=S('whoa'))
W('oops','英、美 /uːps/、/ʊps/','哎呀〔发现小失误、意外时〕',
 '杯子碰倒了、消息发错了，你一发现，就可能说 oops。重点是“哎呀，刚才弄岔了”，语气通常较轻。',
 '记录失手、意外时的自然感叹声，英语也有 whoops 等相关形式。确切最早年代、形式先后有不同记录，不必编一个固定古典词根。',
 [['自然感叹声 → 英语 oops 的书写','把发现失误时的声音固定为文字'],['oops 用于小意外、出错与自我纠正','表达情绪，不在词尾 s 里数复数']],
 'Oops, wrong number. 是哎呀，拨错号了；Oops, I forgot. 是哎呀，我忘了。可以承认小疏忽，也可接着改正。',
 'Oops, sorry.；Oops, wrong number.；Oops, I forgot.。',
 'oops 的 s 是整词的一部分，不是复数后缀；它也不能替代所有严肃道歉，具体语气要和事情轻重相配。',
 ('Oops, I sent the message to the wrong group.','哎呀，我把消息发错群了。'),('Oops, I forgot to attach the file.','哎呀，我忘记附上文件了。'),sources=S('oops'))
W('ouch','英、美 /aʊtʃ/','哎哟〔疼痛〕；哎呀〔受打击、代感疼〕',
 '手被夹了一下喊 ouch，是哎哟；听到很扎心的评价或昂贵的报价，也能用它表示“这一下可真疼”。',
 '常见分析联系宾夕法尼亚德语 outch、德语 autsch 的疼痛呼声；更早来源和借用细节仍有争议。现代作为整声感叹使用。',
 [['疼痛呼声；常联系德语 autsch 等形式','借用细节并非完全确定'],['英语 ouch → 身体疼痛、受打击的感叹','把疼的反应用到花钱、被批评等场景']],
 'Ouch, that hurt. 是哎哟，真疼；看到修理账单说 Ouch，也是在表达心疼、吃不消。',
 'Ouch, that hurt.；Ouch, that is expensive.；say ouch。',
 '身体痛与比喻的心疼共享反应画面；它只表达当下感受，不直接说明受伤程度或实际费用。',
 ('Ouch, I hit my elbow on the table.','哎哟，我胳膊肘撞桌子上了。'),('Ouch, that repair costs more than I expected.','哎呀，那次修理比我预想的贵多了。'),sources=S('ouch'))
W('phew','英、美 /fjuː/〔呼气声与语调可变〕','呼，松了口气；唉，真累；呸，难闻〔按场景〕',
 '险些迟到却赶上了，长呼一口气说 phew；刚干完累活，也可用同一声呼气表示累。',
 '模仿迅速呼气、吹气的声音，旧记录有疲倦、厌恶等用法；现代也常说松一口气。没有可逐字翻译的词根与后缀。',
 [['呼气的声音 → phew 的文字写法','旧用法有疲倦、厌恶的反应'],['phew → 松口气、疲惫或对气味的反应','不同情绪由前后句和语调区分']],
 'Phew, we made it. 是呼，总算赶上了；Phew, that was hard work. 是呼，可真累。',
 'Phew, we made it.；Phew, that was close.；Phew, what a smell!。',
 '不必给 phew 固定配一个中文词；先想说话人正在呼气，是放松、疲惫还是嫌弃。',
 ('Phew, we caught the last train.','呼，我们赶上了末班车。'),('Phew, carrying those boxes was hard work.','呼，搬那些箱子可真累。'),sources=S('phew'))
W('whew','英、美 /hwjuː/、/fjuː/〔呼声读法可变〕','呼；哎呀〔松口气、吃惊、疲惫等〕',
 '考试结束、终于赶上车，长出一口气可以写 whew。面对很费劲、很惊人的事，也可用这一声表达反应。',
 '旧英语记录的 whew 是模仿吹口哨般的呼声；现代常与 phew 在松口气等场景交叉。是声音写法，不按 wh- 问句词根去拆。',
 [['旧形式 quhewe 等 → whew','记录类似吹气、口哨的感叹声'],['现代 whew → 松口气、惊讶、疲惫等反应','可与 phew 部分用法对应，语调决定具体情绪']],
 'Whew, that was close. 是呼，刚才好险；Whew, what a day. 是呼，今天可够累的。',
 'Whew, that was close.；Whew, what a day.；Whew, we are done.。',
 'phew、whew 都能记录呼气感叹；自然说话的气流、语调有变化，音标只是常见读法。',
 ('Whew, that was close—we nearly missed the bus.','呼，刚才好险，我们差点没赶上公交车。'),('Whew, we have finally finished packing.','呼，我们终于收拾完行李了。'),sources=S('whew'))
W('jeez','英、美 /dʒiːz/','天啊，哎呀〔惊讶、烦躁等，随意说法〕',
 '突然看到一堆麻烦事，说 jeez，可以是“天啊，怎么这么多”；对人不耐烦时又可能是“哎呀，别这样”。',
 'Jesus 作为感叹时的缓和改形 → jeez。改了声音、缩了形式，保留情绪反应；现代常不在字面讨论宗教人物。',
 [['Jesus 用作情绪感叹','人名在感叹中的用法背景'],['缓和改形、截短 → jeez','现代随意表达惊讶、烦躁、感叹']],
 'Jeez, that was loud. 是天啊，真响；Jeez, give me a minute. 是哎呀，给我一分钟。',
 'Jeez, that was close.；Jeez, give me a minute.；Oh, jeez.。',
 '来源缓和了原来的直接感叹，不等于语气总温柔；对人说时仍可能显得烦躁，要看语调和后句。',
 ('Jeez, that alarm was loud.','天啊，那个警报真响。'),('Jeez, give me a minute to find my keys.','哎呀，给我一分钟找钥匙。'),sources=S('jeez'))
W('gosh','英 /ɡɒʃ/；美 /ɡɑːʃ/','天哪〔惊讶、感动、强调等〕',
 '看见很美的风景、突然想起漏做的事，都可能说 gosh。它像中文随口的一声“天哪”。',
 'God 在感叹中的缓和改音 → gosh，可能经过较早的 by gosse 等形式。现代作为整声感叹使用，不另拆 sh 词根。',
 [['God 的感叹用法 → 较缓和的改音形式','旧记录有 by gosse 等相关写法'],['gosh → 日常惊讶、感动、强调','具体态度由语调与句子决定']],
 'Oh my gosh! 是天哪；Gosh, that is beautiful. 是天哪，真美；Gosh, I forgot. 则可能是突然想起失误。',
 'Oh my gosh!；Gosh, that is beautiful.；Gosh, I forgot.。',
 'gosh 常比直接说 God 显得缓和；它不自动表示赞叹，也可表达担忧、懊恼或出乎意料。',
 ('Gosh, the mountains look beautiful today.','天哪，今天的山景真美。'),('Oh gosh, I left my notebook at home.','哎呀，我把笔记本落家里了。'),sources=S('gosh'))
W('darn','英 /dɑːn/；美 /dɑːrn/','可恶，哎呀；该死的〔较缓和〕；真，很〔强调〕；织补〔另源动词〕',
 '钥匙又丢了说 Darn!，是较轻的懊恼；darn good 是真不错；darn a sock 则真是在用针线补袜子，属于另一条词史。',
 '感叹、强调的 darn 是 damn 的缓和改形。织补动词的远源有不同分析，可能联系旧 dern 隐藏、法语等，不能把补袜子说成骂人演化来。',
 [['damn 感叹用法 → 缓和改形 darn','又作修饰、强调成分，例如 darn good'],['织补动词 darn 的另一来源线','远源不确定，现代指交织针线填补破洞']],
 'Darn, I forgot. 是哎呀，我忘了；darn good 是真不错；darn these socks 是织补这些袜子。',
 'Darn it!；darn good；darn a sock。',
 '两个同形词必须分开：一句 Darn! 在表达情绪，I can darn socks 才在谈织补技能。',
 ('Darn, I left the tickets at home.','哎呀，我把票落在家里了。'),('That was a darn good meal.','那顿饭真不错。'),('I learned to darn a hole in a sock.','我学会了织补袜子上的破洞。'),sources=S('darn'))
W('yo','英 /jəʊ/；美 /joʊ/','嘿，喂〔随意招呼、引起注意〕',
 '朋友从门口喊 Yo!，像在说“嘿，我来了”；要引起熟人注意，也能先喊一声 yo。语气很随意。',
 '旧记录里已有水手、猎人等使用的呼喊声，后来用作招呼。现代 yo 不是把 you 简单删一个字母后形成的统一词源。',
 [['旧呼喊、使劲声等形式 yo','有水手、猎人呼声的早期记录'],['yo → 招呼、回应、引起注意','现代随意口语延续、发展呼喊用途']],
 'Yo, are you coming? 是嘿，你来吗；Yo, I am over here. 是嘿，我在这边。合不合适取决于熟悉程度和场景。',
 'Yo, what is up?；Yo, over here!；say yo。',
 '它的感觉接近很随意的 hey；陌生、正式场合用 hello 等通常更自然。别把所有地区、所有人的说话风格都套成同一种。',
 ('Yo, are you coming with us?','嘿，你和我们一起来吗？'),('Yo, I saved you a seat over here.','嘿，我在这边给你留了个座位。'),sources=S('yo'))
W('ugh','常见 /ʌɡ/、/ʌ/，也可带喉部摩擦音〔感叹声有变化〕','呃，真烦，恶心〔厌恶、烦躁、不愿意等〕',
 '闻到怪味、想到还要排很久队，喉咙里嫌弃地发出一声 ugh。它把“我不喜欢这个”的反应放在声音里。',
 '通常作为模仿咳声、喉部呼声的写法来分析；旧记录的 ough 等形式与后来厌恶感叹相联系，不需要给 gh 安排一个固定意思。',
 [['咳声、喉部呼声的模拟 → ough、ugh 等写法','自然声音变成文字'],['ugh → 厌恶、烦躁、不情愿等感叹','语调可短促，也可拖长']],
 'Ugh, what a smell. 是呃，什么怪味；Ugh, more paperwork. 是唉，又有一堆文书活。嫌弃对象由后句说明。',
 'Ugh, what a smell.；Ugh, not again.；Ugh, more work.。',
 'ugh 的读音不必像普通单词那样每次一样；它在模拟反应，气流、喉音、长短会随说话人变化。',
 ('Ugh, this bin smells awful.','呃，这个垃圾桶真难闻。'),('Ugh, I have to fill in the whole form again.','真烦，我又得把整张表填一遍。'),sources=S('ugh'))
W('huh','英、美 /hʌ/，也有 /hə/〔常伴鼻化、不同语调〕','啊，什么〔没听清〕；咦〔惊讶〕；是吧〔求回应〕',
 '没听清时升调 Huh?，像中文“啊？你说什么”；看到出乎意料的结果，低一点的 Huh. 又像“咦，原来如此”。',
 '记录喉音、鼻化等自然感叹声，约17世纪已有这种英语写法。语调承担很大部分意思，不从字母拆出普通前后缀。',
 [['自然的短促感叹、喉音 → huh 的文字记录','约17世纪的英语记录已有这种感叹写法'],['不同语调 → 疑问、惊讶、求回应等','同一文字并不固定等于同一种情绪']],
 'Huh? 单说可请求重复；Nice view, huh? 是风景不错，是吧；Huh, that is odd. 是咦，有点奇怪。',
 'Huh?；Nice view, huh?；Huh, that is odd.。',
 '没听清时直接 Huh? 很随意，有时显得生硬；Sorry?、Could you repeat that? 的语气不同。学会识别，不必所有场合照用。',
 ('Huh? I did not hear the last part.','啊？最后那部分我没听见。'),('That was a close game, huh?','那场比赛可真势均力敌，是吧？'),sources=S('huh'))
W('eh','常见 /eɪ/，也有 /e/、/ɛ/〔随地区和语气变化〕','嗯，啊〔疑问、求重复〕；是吧；一般般〔随意评价〕',
 '句尾一个 eh?，常像“是吧？”请对方回应；单独 Eh? 可能是“啊？再说一遍”；平平的一声 Eh. 又可能表示兴趣不大。',
 '旧记录里已有自然感叹 eh，后来见于疑问、惊讶等用法；不同地区还有自己的用法背景。本条学常见英语感叹，不把同形的所有地区语气词编成一条来源。',
 [['自然感叹写法 eh 的早期记录','没有必要硬拆古典词根'],['询问、疑问、确认等用法 → 多种现代口语功能','部分场景又表示无所谓、一般般']],
 'Nice day, eh? 是天气不错，是吧；Eh? 是没听清、疑问；The film was eh. 可随意评价电影一般般。',
 'Nice day, eh?；Eh? Say that again.；The film was eh.。',
 'eh 常让人想到加拿大英语，但其他地区也用；同形的地区语气词未必来源相同，不用一个标签概括所有说法。',
 ('Nice day for a walk, eh?','今天适合散步，是吧？'),('“Eh? Could you say that again?” she asked.','她问：“啊？你能再说一遍吗？”'),sources=S('eh'))
W('shh','英、美 /ʃː/〔嘘声，可拉长〕','嘘〔请人安静〕；发嘘声让人安静',
 '手指竖在嘴前，发出长长的“嘘”，文字里可以写 shh。它把请人安静的声音直接写下来。',
 '常联系 hush 安静、嘘的缩短形式，也是在模仿非语言的嘘声。两个 h 不分别代表词根，只帮助记录声音。',
 [['hush 等请人安静的呼声材料 → shh','常作缩短、声音模拟来理解'],['shh 的书写 → 感叹，也可转作动词','发嘘声、让别人安静']],
 'Shh, the baby is asleep. 是嘘，宝宝睡着了；Shh, listen. 是嘘，听。自然发音主要是一段持续的 /ʃ/。',
 'Shh, be quiet.；Shh, listen.；Shh, the baby is asleep.。',
 '它没有普通英语单词那样必须明显读出的元音；别为了拼字硬加一个“西”或“是”的音节。',
 ('Shh, the baby is asleep.','嘘，宝宝睡着了。'),('Shh, listen to the birds outside.','嘘，听听外面的鸟叫声。'),sources=S('shh'))
W('hooray','英、美 /hʊˈreɪ/、/həˈreɪ/','好耶，万岁〔欢呼〕；一声欢呼',
 '事情成功了、好消息到了，喊 hooray，就像“好耶！”不是只陈述开心，而是直接欢呼出来。',
 '与 hurrah、hurray 等欢呼形式相关；更远有人联系 huzzah 或其他欧洲语言的欢呼声，细节不确定，不必指定唯一原始词根。',
 [['hurrah、hurray 等相关欢呼形式','更远来源有不同分析'],['hooray → 表示高兴、赞同、成功的呼喊','也可作名词表示一声欢呼']],
 'Hooray, we did it! 是好耶，我们做到了；a hooray 是一声欢呼。文字里常配感叹号，也可带故意的反讽语气。',
 'Hooray, we did it!；Hooray for the team!；a loud hooray。',
 '欢呼原本是声音行为，音高和长短会变；句中是否真高兴还要看语气，反讽时可能恰好相反。',
 ('Hooray, we finished the puzzle!','好耶，我们把拼图拼完了！'),('Everyone gave a loud hooray when the results appeared.','结果一出来，大家都大声欢呼起来。'),sources=S('hooray'))
def extend_lessons():
 extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_zjg',ROOTS,WORDS)
 extend_lessons()
