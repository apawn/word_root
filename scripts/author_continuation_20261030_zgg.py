"""Amusement, bemusement, reflection and different forms of confusion."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
def S(word,base):
 return ['https://en.wiktionary.org/wiki/'+word+'#English','https://www.etymonline.com/word/'+base]+(['https://www.merriam-webster.com/dictionary/bemused'] if word.startswith('bemuse') or word=='bemusing' else [])
EXISTING_ROOT_ADDITIONS={
 'A1760':dict(words='amuse amuses amused amusing amusingly amusements bemuse bemused bemusing bemusedly bemusement muse muses mused musing musings daze dazes dazed dazedly'.split(),label='amuse、bemuse、muse 的动作与过去状态',note='amuse 经法语 a- 加 muser 借入，早期分散注意、迷惑义后来转为逗乐；bemuse 是 be- 加沉思动词 muse。名词 Muse 的希腊来源另路，不能把逗乐当没有缪斯。'),
 'C0726':dict(words='muse muses mused musing musings'.split(),label='muse 的灵感名词与沉思动词分路',note='缪斯、灵感名词接希腊 Mousa，较远可联系思想词根；动词承法语 muser，远源未定，两支可能相互影响，但不统一成唯一来源。'),
 'A2238':dict(words='daze dazes dazed dazedly dazzle dazzling dazzlingly'.split(),label='daze、dazzle 的发懵与眩目',note='dazzle 接中古英语 dasen 等的反复动作材料；早期发懵义在英语记录早于强光使眩目义，学习画面不倒排实际演化。'),
 'B3953':dict(words='wild wilderness bewilder bewildered bewildering bewilderingly bewilderment'.split(),label='bewilder：像被带到陌生旷野般辨不清方向',note='be- 加旧动词 wilder 引入迷途等，wilder 可能从 wilderness 逆构；现代 bewilder 写情境、信息把人弄糊涂，不能把中间 er 当比较级简单直拆。'),
 'C1067':dict(words='perplex perplexes perplexed perplexing perplexingly perplexity perplexities'.split(),label='perplex 的纠结画面与逆构动词',note='拉丁 perplexus 的缠绕、错综材料先有英语形容词，后形成 perplexed，再逆构动词；perplexities 是多个难题、复杂之处，不虚构拉丁 perplectere 为实证。'),
}
AMUSE=[['法语 a- 加 muser 等沉思、停留注意材料 → amuser → amuse','早期吸住、分散注意，也可使迷惑，不只是现代逗人开心'],['分散严肃事务的注意 → 使愉快、消遣、觉得有趣','现代 amused 是人觉得有趣，amusing 是让人觉得有趣']]
W('amuses','/əˈmjuːzɪz/','逗乐、使觉得有趣；让自己消遣〔第三人称单数〕',
 '一件小事让人忍不住觉得好玩，是 amuses；孩子自己想点游戏打发时间，是 amuses herself。',
 'amuse + -s，/z/ 后词尾读 /ɪz/；基础借法语 a- 加 muser 一路，不把 a- 当否定。',AMUSE+[['amuse + -s → amuses','它使人觉得有趣；他、她让自己消遣']],
 'amuses the children 逗孩子开心；amuses herself with a game 自己玩游戏消遣。',
 'it amuses me that 让我觉得有趣的是；amuses everyone。',
 'amuses 使人觉得有趣，不要求一定笑出声；makes someone laugh 才直接把笑的反应说出。',
 ('The little dog’s expression amuses everyone.','小狗的表情让大家都觉得有趣。'),('She amuses herself by drawing tiny cartoons.','她画些小漫画，自己找乐子。'),sources=S('amuses','amuse'))
W('amusing','/əˈmjuːzɪŋ/','有趣、逗人发笑的；正在逗乐、使消遣',
 '故事里的小反转让人觉得好笑，这个故事是 amusing；人正在逗孩子开心，动作也用 amusing。',
 'amuse 去 e 加 -ing；既是动作形式，也形成常见形容词，指能让人觉得有趣的性质。',AMUSE+[['amuse → amusing','正在逗乐；也形容令人觉得有趣']],
 'an amusing story 有趣的故事；amusing the children 正在逗孩子；find something amusing 觉得某事好笑。',
 'an amusing detail；mildly amusing 有点好笑。',
 'amusing 是东西、行为让人觉得有趣，amused 是人的感受；an amusing guest 逗趣的客人，an amused guest 觉得有趣的客人。',
 ('She told us an amusing story about the journey.','她给我们讲了旅途中的一个趣事。'),('He was amusing the children with simple tricks.','他正用简单的小戏法逗孩子们。'),sources=S('amusing','amuse'))
W('amusingly','/əˈmjuːzɪŋli/','有趣、好笑地；令人发笑地',
 '两个人碰巧给猫取了同一个名字，这个巧合本身有趣；开头用 amusingly，就像提醒读者“说来也好笑”。',
 'amusing + 副词 -ly；内层 amuse 去 e 加 -ing 的形容词再扩展，主说事物有趣的呈现方式。',AMUSE+[['amusing + -ly → amusingly','以让人觉得有趣的方式；也评价整件事有趣']],
 'amusingly similar 相似得有趣；amusingly enough 说来也好笑；amusingly described 描述得很有趣。',
 'amusingly different；amusingly exaggerated 夸张得好玩。',
 'amusingly 评价内容有趣，amusedly 才偏本人觉得有趣地；一个是造成感受，一个是带着感受。',
 ('Amusingly, we had both chosen the same name for the cat.','说来也好笑，我们竟给猫选了同一个名字。'),('The scene is amusingly exaggerated.','这个场景夸张得很有趣。'),sources=S('amusingly','amuse'))
AMUSEMENT=AMUSE+[['法语 amusement → 英语 amusement，再作 amusements','消遣、乐趣；可数时指具体娱乐活动、设施']]
W('amusements','/əˈmjuːzmənts/','娱乐活动、消遣；游乐设施〔复数〕',
 '不是只说心里觉得好笑，而是把逛集市、玩游戏、坐游乐设施这些具体消遣一项项数出来，用 amusements。',
 'amusement + -s；amusement 经法语动作名词借入，现代可与 amuse 去 e 加 -ment 对照，复数再接 /s/。',AMUSEMENT,
 'seaside amusements 海滨娱乐活动、设施；fairground amusements 游乐场里的设施；simple amusements 简单消遣。',
 'a range of amusements；children’s amusements。',
 'amusement 单数常说有趣的感受、消遣这一过程，amusements 把具体娱乐项目数出来；并不只是好多次笑。',
 ('The seafront has cafés, shops and plenty of amusements.','海滨有咖啡馆、商店，还有不少娱乐设施。'),('Reading and gardening were her favourite amusements.','阅读和园艺是她最喜欢的消遣。'),sources=S('amusements','amuse'))
BEMUSE=[['be- 使、加强 + muse 沉入思绪 → bemuse','使人陷入出神、混乱，后来常写摸不着头脑'],['现代困惑、茫然，有时夹着觉得好笑','与 amuse 形似而侧重点不同；可以困惑中发笑，不当成普通逗乐的完全同义词']]
W('bemuse','/bɪˈmjuːz/','使困惑、茫然；使有点摸不着头脑',
 '对方做的事很古怪，你一下不知道该怎么理解，停在那里发懵，这件事会 bemuse you。',
 'be- 使、加强 + 动词 muse 沉入思绪；不从名词 Muse 缪斯直接推出把人变成缪斯崇拜者。',BEMUSE,
 'bemuse the visitors 让访客摸不着头脑；can bemuse beginners 会把初学者弄糊涂；常见被动、形容形式 bemused。',
 'seems to bemuse him；a rule that may bemuse people。',
 'amuse 更侧重让人觉得有趣；bemuse 常是看不懂、想不明白，特定场景也带一点好笑的反应。',
 ('The unusual rules may bemuse first-time visitors.','这些特别的规矩可能让第一次来的访客摸不着头脑。'),('His sudden change of subject seemed to bemuse everyone.','他突然换话题，似乎把大家都弄糊涂了。'),sources=S('bemuse','bemuse'))
W('bemused','/bɪˈmjuːzd/','困惑、茫然的；带点好笑地不解的',
 '不是直接被逗得开心，而是像在想“这到底怎么回事”，可能还忍不住笑一下，这种反应常叫 bemused。',
 'bemuse 去 e 加完整 -ed，/z/ 后词尾读 /d/；作过去形式，也常作描述人神态的形容词。',BEMUSE+[['bemuse → bemused','已经被弄困惑；也描述摸不着头脑的神态']],
 'a bemused expression 困惑的神情；looked bemused 显得茫然；a bemused smile 带点不解的笑。',
 'slightly bemused；bemused by the instructions。',
 'bemused smile 可以在不理解中觉得好笑，amused smile 更直接是觉得有趣；不要只因都能带笑就抹掉差别。',
 ('She gave me a bemused look when I explained the plan.','我解释方案时，她困惑地看了我一眼。'),('He watched the strange performance with a bemused smile.','他看着这场古怪的表演，笑里带着不解。'),sources=S('bemused','bemused'))
W('bemusing','/bɪˈmjuːzɪŋ/','令人困惑、摸不着头脑的；正在使人茫然',
 '眼前的事不按常理来，越看越不知道该怎么理解，就可以叫 bemusing；有时也会让人在困惑中发笑。',
 'bemuse 去 e 加 -ing；动作形式又可描述引起困惑的事物性质。',BEMUSE+[['bemuse → bemusing','使人困惑正在发生；也形容引发不解']],
 'a bemusing situation 让人摸不着头脑的情况；a bemusing mixture 令人不解的混搭。',
 'find it bemusing；a bemusing response。',
 'bemusing 说事情令人困惑，bemused 说人的反应；结构与 amusing、amused 的关系相似，具体感受不同。',
 ('The instructions were a bemusing mixture of words and symbols.','说明书把文字和符号混在一起，让人摸不着头脑。'),('I found his sudden politeness rather bemusing.','他突然这么客气，让我有点不解。'),sources=S('bemusing','bemuse'))
W('bemusedly','/bɪˈmjuːzədli/','困惑地；茫然、带不解地',
 '一个人不太明白发生了什么，停一下、笑一下或看着别人，这种反应方式可以用 bemusedly。',
 'bemused + -ly；bemused 作动词过去形式通常读 /bɪˈmjuːzd/，这个副词常保留 /əd/ 音节，按实际副词读音记。',BEMUSE+[['bemused → bemusedly','带着困惑、不解的感受做动作']],
 'looked bemusedly at someone 茫然不解地看某人；smiled bemusedly 带着不解笑了笑。',
 'shook his head bemusedly；watched bemusedly。',
 'bemusedly 重点是当事人不解的反应，amusingly 重点是内容好笑；修饰同一个笑脸时也不能随意调换。',
 ('She looked bemusedly at the pile of mismatched shoes.','她不解地看着那堆不成对的鞋。'),('He shook his head bemusedly and read the message again.','他茫然地摇摇头，又读了一遍消息。'),sources=S('bemusedly','bemused'))
W('bemusement','/bɪˈmjuːzmənt/','困惑、茫然；带点好笑的不解',
 '表演结束了，人却还在想“刚才那是什么意思”，脸上带着不解，这份感受就是 bemusement。',
 'bemuse 去 e 加 -ment；动作使人茫然，名词把这种反应、状态拿出来说。',BEMUSE+[['bemuse + -ment → bemusement','使人不解或当事人困惑的状态']],
 'in bemusement 困惑地；with bemusement 带着不解；to someone’s bemusement 让某人不解的是。',
 'a look of bemusement；watched with bemusement。',
 'amusement 是有趣、消遣的感受，bemusement 侧重摸不着头脑；有时两种感受能在同一场景并存。',
 ('She watched the ceremony with mild bemusement.','她带着些许不解，看着仪式进行。'),('To my bemusement, everyone applauded before I had spoken.','让我不解的是，我还没开口，大家就鼓起掌来。'),sources=S('bemusement','bemuse'))
MUSE=[['动词：古法语 muser 沉思、出神 → 英语 muse','较远可能有鼻子、吻部材料等分析，来源未定'],['名词：希腊 Mousa → 拉丁 Musa、法语 Muse → muse','缪斯女神；后说启发创作的人、物，与沉思动词分路，现代意思可能相互影响']]
W('muse','/mjuːz/','沉思；若有所思地说；缪斯；灵感来源',
 '眼睛看着窗外，心里慢慢转一个问题，是动词 muse；某个人让诗人总想写诗，则可以叫 the poet’s muse。两条画面不要硬并成一个来源。',
 '动词经法语 muser，远源未定；名词接希腊 Mousa 缪斯，经拉丁、法语借入，较远联系思想材料。现代可能相互影响。',MUSE,
 'muse about the future 沉思未来；muse on a question 琢磨问题；a writer’s muse 作家的灵感来源。',
 'muse aloud 若有所思地说出；find a muse 找到灵感来源。',
 'Muse 可专指神话缪斯，muse 小写也指创作启发者；动词并不要求主题一定是文学艺术。',
 ('She liked to muse about the future on long walks.','她喜欢在长时间散步时沉思未来。'),('The city became a muse for the young poet.','这座城市成了年轻诗人的灵感来源。'),sources=S('muse','muse'))
W('muses','/ˈmjuːzɪz/','沉思、若有所思地说〔第三人称单数〕；缪斯、灵感来源〔复数〕',
 '他坐着慢慢想，用 muses；几个启发创作的人、地方，也能称作 muses。动词与名词碰巧同形，来源仍分开。',
 'muse + -s，基础 /z/ 后词尾读 /ɪz/；两条来源分别有动词三单和名词复数。',MUSE+[['muse + -s → muses','他、她沉思；多个缪斯或灵感来源']],
 'muses on the past 沉思往事；the nine Muses 神话九位缪斯；artists and their muses 艺术家与他们的灵感来源。',
 'muses aloud；muses about what comes next。',
 'muses 的词性靠句子判：he muses 是他在想，his muses 是他的灵感来源，不要统一翻成沉思。',
 ('He often muses on how the town has changed.','他常沉思小镇这些年的变化。'),('The exhibition explores artists and their muses.','展览探讨艺术家与他们的灵感来源。'),sources=S('muses','muse'))
W('mused','/mjuːzd/','沉思了；若有所思地说了',
 '不是立刻下结论，而是把一个念头放在心里慢慢转；话说出来仍带琢磨的感觉，过去可以用 mused。',
 '沉思动词 muse 去 e 加完整 -ed，/z/ 后词尾读 /d/；这里不接名词缪斯那条借入来源。',MUSE+[['动词 muse → mused','过去沉思，或若有所思地说出']],
 'mused about the future 琢磨未来；mused aloud 若有所思地说出来；mused that 后接所想的内容。',
 'mused on the question；“Perhaps,” she mused。',
 'mused 标出思考式、沉吟式语气；announced 则是明确宣布，声音的确定感不同。',
 ('“Perhaps we should wait,” she mused.','“也许我们该等等。”她若有所思地说。'),('He mused about the possible reasons for the change.','他琢磨着这次变化可能有哪些原因。'),sources=S('mused','muse'))
W('musing','/ˈmjuːzɪŋ/','正在沉思；若有所思的；一段思绪',
 '心里慢慢想着，暂时没有急着下结论，叫 musing；也能把这样一段想法当成名词，复数 musings 更常见。',
 '动词 muse 去 e 加 -ing；形成动作形式、形容词和思绪名词，不直接从缪斯女神复数变化来解释。',MUSE+[['动词 muse → musing','沉思的过程；也形容若有所思，或指一段思绪']],
 'musing about the past 沉思往事；a musing expression 若有所思的神情；a quiet musing 一段安静的思索。',
 'musing aloud；lost in musing 陷入沉思。',
 'musing 常是散缓、反思式的想，calculating 更明确是计算、权衡；两者思考的节奏、目标感不同。',
 ('She sat by the window, musing about the journey.','她坐在窗边，回想着那趟旅程。'),('He gave me a musing look before replying.','他若有所思地看了我一眼，才回答。'),sources=S('musing','muse'))
W('musings','/ˈmjuːzɪŋz/','随想；沉思、感想〔复数〕',
 '不是一份条理紧密的论证，而是慢慢想出来、随手记下的感想，常叫 musings。读起来像跟着一个人的思绪走。',
 'muse 去 e 加 -ing → musing，再加复数 -s，词尾读 /z/；名词把思索片段一篇篇、一段段数出来。',MUSE+[['musing + -s → musings','多段沉思、随想或感想']],
 'musings on life 对生活的随想；personal musings 个人感想；a collection of musings 一本随想集。',
 'late-night musings 深夜随想；musings about the future。',
 'musings 通常比较反思、随笔式；findings 是调查研究得出的发现，不只是同一种想法换个词。',
 ('The notebook is full of her musings on everyday life.','笔记本里写满了她对日常生活的随想。'),('He published a collection of travel musings.','他出版了一本旅行随想集。'),sources=S('musings','muse'))
DAZE=[['中古英语 dasen：发懵、使茫然等 → daze','可能接北欧疲乏材料，也有荷兰语比较分析，较早词形关系有讨论'],['头脑一时不清楚 → 使发懵；名词 in a daze','现代可由惊讶、疲倦、强烈经历等引出，场景决定具体原因']]
W('dazes','/ˈdeɪzɪz/','使发懵、茫然〔第三人称单数〕；发懵状态〔复数〕',
 '消息太突然、声光一下太强，人脑子一时跟不上，脑子像一下卡住了；造成这种反应的东西 dazes someone。',
 'daze + -s，/z/ 后词尾读 /ɪz/；动词三单常见于使人发懵场景，名词复数较少用。',DAZE+[['daze + -s → dazes','它使人短暂茫然；多次发懵状态']],
 'dazes the audience 让观众一时发懵；a noise that dazes him 让他一时反应不过来的噪声。',
 'dazes for a moment；dazes with sudden news。',
 'dazes 强调一时难以清楚反应，不等于每次都失去意识；faints 才直接说昏厥。',
 ('The sudden burst of noise dazes the audience for a moment.','突然爆出的噪声让观众一时发懵。'),('In the story, the unexpected news dazes him.','故事里，突如其来的消息让他茫然了。'),sources=S('dazes','daze'))
W('dazed','/deɪzd/','发懵、茫然的；使一时反应不过来了',
 '话听见了，脑子却还没接上；人像在场又不完全在状态，这种发懵的样子叫 dazed。',
 '现代可按 daze 去 e 加完整 -ed 理解，词尾读 /d/；较早 dazed 与 daze 的词形先后有讨论，不能只凭长短决定全部历史。',DAZE+[['daze → dazed〔现代构词对应〕','被弄得一时不清楚；也形容茫然、发懵']],
 'a dazed expression 发懵的神情；looked dazed 显得茫然；dazed by the sudden noise 被突然的噪声弄得一时反应不过来。',
 'slightly dazed；dazed and confused。',
 'dazed 常像反应被冲击、疲倦等压慢，puzzled 更像有个问题想不通；原因和程度由上下文补足。',
 ('He looked dazed after the long overnight journey.','熬了一夜的长途旅行后，他显得有些发懵。'),('She stared at the unexpected message with a dazed expression.','她带着茫然的神情，盯着那条意外的消息。'),sources=S('dazed','daze'))
W('dazedly','/ˈdeɪzədli/','茫然地；发懵、反应迟钝地',
 '人还没完全弄明白，像脑子慢半拍地看看四周、点个头，这种动作方式叫 dazedly。',
 'dazed + -ly；副词常读 /ˈdeɪzədli/，ed 的音节与单独 dazed /deɪzd/ 不同，按整个副词记。',DAZE+[['dazed → dazedly','带着发懵、茫然的状态做动作']],
 'looked dazedly around 茫然四顾；nodded dazedly 发懵地点头；said dazedly 茫然地说。',
 'blinked dazedly；stared dazedly at the screen。',
 'dazedly 强调反应还没清楚，slowly 只说慢；慢慢做也可能是很清醒、很从容。',
 ('He looked dazedly around the unfamiliar room.','他茫然地打量着陌生房间。'),('She nodded dazedly, still trying to understand the news.','她茫然地点点头，还在努力理解那条消息。'),sources=S('dazedly','daze'))
DAZZLE=DAZE+[['dasen 等发懵材料的反复动作形式 → dazzle','早期迷糊义后来有强光晃眼、表现惊艳等用法']]
W('dazzlingly','/ˈdæzəlɪŋli/','耀眼地；灿烂、惊艳地',
 '亮得一下难直视，叫 dazzlingly bright；表现出色得让人目不暇接、惊叹，也能用 dazzlingly。',
 'dazzle 去 e 加 -ing → dazzling，再加 -ly；历史反复动作材料与 daze 相连，现代既写光也写惊艳。',DAZZLE+[['dazzling + -ly → dazzlingly','以眩目、令人惊叹的方式；也修饰这种程度']],
 'dazzlingly bright 亮得耀眼；dazzlingly beautiful 美得惊艳；dazzlingly skilful 技艺精湛得令人惊叹。',
 'dazzlingly white；a dazzlingly original performance。',
 'dazzlingly 不只是程度很高，还带像光彩夺目般吸住注意、令人惊叹的感觉；用于普通清楚明白未必合适。',
 ('The snow was dazzlingly bright in the sun.','雪在阳光下亮得耀眼。'),('She gave a dazzlingly skilful performance.','她的表演技艺精湛，令人惊叹。'),sources=S('dazzlingly','dazzle'))
BEWILDER=[['wild、wilderness 等旷野词族 → 旧动词 wilder','wilder 引入迷途，可能从 wilderness 逆构，不能只按现代比较级看 er'],['be- 加 wilder → bewilder','像被带入不熟悉的旷野，辨不清方向；现代也说信息、情境令人糊涂']]
W('bewilder','英 /bɪˈwɪldə/；美 /bɪˈwɪldər/','使困惑、摸不着头脑；使不知所措',
 '选择一大堆，标志又各指一边，人像被丢到陌生地方，连该从哪里开始都不知道，这些东西会 bewilder someone。',
 'be- 加旧动词 wilder 引入迷途等，后者可能从 wilderness 逆构；现代保留 wild 旷野的画面帮助理解，但中间历史另说明。',BEWILDER,
 'bewilder beginners 让初学者摸不着头脑；bewilder the audience 让观众不知所措。',
 'a system that can bewilder people；bewilder with too many choices。',
 'confuse 更一般，bewilder 更容易写不知该往哪里想、如何反应的迷茫；不只是一处数字算错。',
 ('The number of choices can bewilder a beginner.','选择太多，可能把初学者弄得不知从哪儿下手。'),('The contradictory signs seemed designed to bewilder visitors.','这些互相矛盾的标志简直像专门来让访客摸不着头脑的。'),sources=S('bewilder','bewilder'))
W('bewildered','英 /bɪˈwɪldəd/；美 /bɪˈwɪldərd/','困惑、茫然、不知所措的；使困惑了',
 '别人都开始行动了，自己却还不知道发生了什么、该跟哪边走，这个摸不清状况的样子叫 bewildered。',
 'bewilder + 完整 -ed，词尾读 /d/；动作过去形式又作形容词，描述当事人的困惑状态。',BEWILDER+[['bewilder + -ed → bewildered','已经被弄糊涂；也形容茫然不解的人']],
 'a bewildered look 茫然的目光；bewildered by the rules 被规矩弄糊涂；looked utterly bewildered 显得完全不知所措。',
 'a bewildered child；bewildered and unsure。',
 'bewildered 是人的反应，bewildering 是事物让人产生这种反应；a bewildered visitor、a bewildering map。',
 ('He gave me a bewildered look when I mentioned the meeting.','我提起会议时，他茫然地看了我一眼。'),('We were bewildered by the maze of corridors.','迷宫般的走廊把我们弄得摸不着方向。'),sources=S('bewildered','bewilder'))
W('bewildering','英 /bɪˈwɪldərɪŋ/；美 /bɪˈwɪldərɪŋ/','令人困惑、眼花缭乱的；正在使人不知所措',
 '菜单几十页，选项还互相套，人越看越不知道选哪一个；这种多、乱、复杂得让人难下手的东西常叫 bewildering。',
 'bewilder + -ing；动作形式又作形容词，描述造成迷茫的东西。',BEWILDER+[['bewilder + -ing → bewildering','正在使人困惑；也形容让人不知所措']],
 'a bewildering array of choices 多得让人眼花缭乱的选择；a bewildering system 复杂得令人糊涂的系统。',
 'bewildering variety；a bewildering explanation。',
 'bewildering variety 不只说种类多，还说多得让人不易理清；wide variety 可以更中性、正面地说丰富。',
 ('The shop offered a bewildering variety of cables.','店里的线缆种类多得让人不知道怎么选。'),('I found the system bewildering at first.','起初，我觉得这个系统让人摸不着头脑。'),sources=S('bewildering','bewilder'))
W('bewilderingly','英 /bɪˈwɪldərɪŋli/；美 /bɪˈwɪldərɪŋli/','令人困惑地；复杂、纷繁得让人无所适从地',
 '不是只说复杂，而是复杂到人理不清、选不定；用 bewilderingly complex 就把看的人那份迷茫也带上。',
 'bewildering + 副词 -ly；内层 be-、wilder、-ing 分层保留，外层描述造成困惑的方式、程度。',BEWILDER+[['bewildering + -ly → bewilderingly','把令人困惑的性质用于方式、程度']],
 'bewilderingly complex 复杂得令人糊涂；bewilderingly varied 变化多得让人无所适从。',
 'bewilderingly different；bewilderingly unfamiliar 陌生得令人不知所措。',
 'bewilderingly 把人的理解困难写进程度，extremely 只加强程度；extremely varied 未必让人觉得糊涂。',
 ('The instructions were bewilderingly complex.','说明复杂得让人理不出头绪。'),('The two versions were bewilderingly different.','两个版本差得让人摸不着头脑。'),sources=S('bewilderingly','bewilder'))
W('bewilderment','英 /bɪˈwɪldəmənt/；美 /bɪˈwɪldərmənt/','困惑、茫然；不知所措',
 '人停在那儿，想不通发生了什么，也不知道接下来做什么；把这种摸不清状况的感受当名词，就是 bewilderment。',
 'bewilder + 名词 -ment；动词使人不知所措，名词把这种结果、状态提出来说。',BEWILDER+[['bewilder + -ment → bewilderment','使困惑的结果或当事人的茫然']],
 'in bewilderment 茫然地；a look of bewilderment 不解的神情；to my bewilderment 让我不解的是。',
 'stared in bewilderment；complete bewilderment。',
 'bewilderment 写的是理不清状况的感受，indecision 着重难以决定；不知道发生什么和知道选项却拿不定主意有区别。',
 ('She stared at the unfamiliar machine in bewilderment.','她茫然地看着那台陌生机器。'),('His explanation only added to my bewilderment.','他的解释只让我更加摸不着头脑。'),sources=S('bewilderment','bewilder'))
PERPLEX=[['拉丁 per- 加 plexus 缠绕、错综 → perplexus','像线相互缠住，理不出清楚头绪'],['英语先有 perplex、perplexed 等形容形式，后逆构动词 perplex','现代词形能按动词加词尾学习，但历史上形容词出现更早']]
W('perplexes','/pəˈpleksɪz/〔英〕；/pərˈpleksɪz/〔美〕','使困惑、费解〔第三人称单数〕',
 '问题里几条线索互相打架，怎么想都接不顺，这件事 perplexes someone：让人理不出头绪。',
 'perplex + -s，基础 /s/ 后词尾读 /ɪz/；基础动词由较早形容形式逆构，远接拉丁缠绕、错综材料。',PERPLEX+[['perplex + -s → perplexes','它使人困惑、无法理顺']],
 'perplexes me 让我费解；a question that perplexes everyone 让所有人困惑的问题。',
 'what perplexes me is 让我想不通的是；still perplexes researchers。',
 'perplexes 常是某个问题使人思路打结；bewilders 更容易是整个情境让人不知所措，实际语境可以交叠。',
 ('What perplexes me is why nobody noticed the missing page.','让我想不通的是，为什么没人发现缺了一页。'),('The question still perplexes researchers.','这个问题仍让研究人员感到困惑。'),sources=S('perplexes','perplex'))
W('perplexingly','英 /pəˈpleksɪŋli/；美 /pərˈpleksɪŋli/','令人费解地；让人想不通地',
 '两个说明明明讲的是同一件事，却差得接不起来；说 perplexingly different，就像写“不同得让人想不通”。',
 'perplexing + 副词 -ly；内层 perplex + -ing 写引起困惑的性质，外层写方式、程度。',PERPLEX+[['perplexing + -ly → perplexingly','以让人费解的方式，或修饰难理解的程度']],
 'perplexingly vague 模糊得让人不解；perplexingly different 不同得令人费解。',
 'perplexingly silent 沉默得让人想不通；perplexingly brief 简短得叫人不解。',
 'perplexingly 不是指出字面事实错误，而是表达说话人理解不通；事实可能还需要更多信息才能解释。',
 ('The two reports gave perplexingly different totals.','两份报告的总数差得让人想不通。'),('His reply was perplexingly vague.','他的回答含糊得令人费解。'),sources=S('perplexingly','perplex'))
W('perplexities','英 /pəˈpleksətiz/；美 /pərˈpleksətiz/','难题；复杂之处；让人困惑的事情〔复数〕',
 '办一件事，条款一层套一层，每到一处都有个想不通、难处理的结，这些具体的复杂之处可以叫 perplexities。',
 'perplexity 改 y 为 ies；perplexity 的拉丁、法语名词词族背景单独保留，不能全当现代 perplex 加 -ity 当场造出。',PERPLEX+[['perplexity → perplexities','把复杂、困惑当成一项项具体难题']],
 'the perplexities of the system 系统的复杂之处；practical perplexities 实际难题；the perplexities of daily life 生活中的种种难题。',
 'deal with perplexities；explain the perplexities。',
 'perplexity 可指一般困惑状态，perplexities 更常把让人困惑的事情一项项列出；复数带来了可数视角。',
 ('The guide explains some of the perplexities of the old system.','指南解释了旧系统中一些让人费解的地方。'),('They discussed the practical perplexities of sharing a small office.','他们讨论了共用一间小办公室会遇到的种种实际难题。'),sources=S('perplexities','perplexity'))
def extend_lessons():
 extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_zgg',ROOTS,WORDS)
 extend_lessons()
