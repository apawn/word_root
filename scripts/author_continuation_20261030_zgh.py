"""Puzzles, riddles, bafflement, befuddlement and muddled order."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
def S(word,base):
 return ['https://en.wiktionary.org/wiki/'+word+'#English','https://www.etymonline.com/word/'+base]
EXISTING_ROOT_ADDITIONS={
 'A2238':dict(words='puzzle puzzles puzzling puzzlingly puzzler puzzlers muddle muddles muddled muddling'.split(),label='puzzle、muddle 的不同反复动作材料',note='puzzle 可能联系 pose 的旧困惑义，另有其他分析；muddle 可能接 mud 的反复动作形式，也可能借荷兰语同族材料。不能因都写 -le 就确定唯一现代拆法。'),
 'B2760':dict(words='read riddle riddles riddled riddling'.split(),label='riddle 的猜解词族与另源筛孔词分路',note='谜语 riddle 接古英语 raedels，与 read 的解释、猜解旧义相关；筛子 riddle 承 hriddel，筛、打孔和布满用法另路。这里不把两种 riddle 合成一个来源。'),
 'A1760':dict(words='baffle baffles baffled baffling bafflingly bafflement befuddle befuddles befuddled befuddling befuddlement bemuse bemuses'.split(),label='baffle、befuddle 的难住、迷糊与规则词尾',note='baffle 来源未定，早期羞辱义后有挫败、使困惑；befuddle 为 be- 加 fuddle，早期有醉后迷糊材料。现代各自去 e 加完整 -ed、-ing，不造一个确定的 baff 词根。'),
 'B4154':dict(words='mud muddle muddles muddled muddling'.split(),label='muddle：像水变浑一样，次序和想法乱了',note='muddle 可能接 mud 或荷兰语同族材料；英语早期抽象失去清楚的记录早于部分具体泥水义，形象有助理解，但不能倒排实际年代。'),
 'C0457':dict(words='confound confounds confounded confounding'.split(),label='confound：倒到一起，混杂难分',note='con- 加拉丁 fundere 倾倒，经法语进入英语；抽象使人困惑、把不同事物混为一谈，不能全当现代从具体倒水新造的比喻。'),
}
PUZZLE=[['早期英语 pusle → puzzle','更早来源未定，可能联系 pose 的旧困惑义，也有其他日耳曼比较材料'],['使困惑、费力琢磨 → 名词难题、益智玩具','现代 puzzled 是人的困惑，puzzling 是事物令人费解；puzzler 加 -er 可命名难题或解题者']]
W('puzzles','/ˈpʌzəlz/','谜题、益智游戏〔复数〕；使困惑、费力琢磨〔第三人称单数〕',
 '填字、拼图这些要动脑解开的东西是 puzzles；一件事总想不通，动词也用 puzzles。',
 'puzzle + -s，词尾读 /z/；名词复数与动词三单同形。基础词更早来路未定，名词由动词发展。',PUZZLE+[['puzzle + -s → puzzles','多个难题、益智游戏；它使人困惑']],
 'crossword puzzles 填字游戏；jigsaw puzzles 拼图；what puzzles me is 让我想不通的是。',
 'solves puzzles 解谜；puzzles over a question 费力琢磨问题。',
 'puzzles 作为游戏名词通常有设计好的问题、解法；mysteries 更广，可是现实中尚未解释的事。',
 ('She enjoys solving crossword puzzles on the train.','她喜欢坐火车时做填字游戏。'),('What puzzles me is how the keys ended up in the fridge.','让我想不通的是，钥匙怎么跑进冰箱了。'),sources=S('puzzles','puzzle'))
W('puzzlingly','/ˈpʌzəlɪŋli/','令人费解地；让人想不通地',
 '说明本该帮人弄明白，却偏偏模糊、缺一块，这种让人想不通的样子可以说 puzzlingly。',
 'puzzling + -ly；内层 puzzle 去 e 加 -ing，外层把令人费解的性质用于方式或程度。',PUZZLE+[['puzzling + -ly → puzzlingly','以引起不解的方式，或修饰这种程度']],
 'puzzlingly absent 缺席、缺失得令人不解；puzzlingly vague 含糊得让人想不通。',
 'puzzlingly different；puzzlingly quiet。',
 'puzzlingly absent 不只是没出现，还把说话人的不解放进去；absent 可以只是中性陈述。',
 ('Her name was puzzlingly absent from the guest list.','宾客名单里没有她的名字，这让人不解。'),('The two copies were puzzlingly different.','两份副本差得让人想不通。'),sources=S('puzzlingly','puzzle'))
W('puzzlers','英 /ˈpʌzələz/；美 /ˈpʌzələrz/','难题、谜题；解谜爱好者〔复数〕',
 '一道题把人难住，可以叫 a puzzler；爱解这类题的人也能叫 puzzlers。-er 有时命名造成作用的东西，有时命名做事的人。',
 'puzzle 去 e 加完整 -er → puzzler，再加 -s；难题与解题者按句子对象分开。',PUZZLE+[['puzzle → puzzler → puzzlers','多个让人琢磨的题目；或多个解谜者']],
 'logic puzzlers 逻辑谜题；keen puzzlers 热心解谜者；a book of puzzlers 一本谜题集。',
 'experienced puzzlers；tricky puzzlers 棘手的谜题。',
 'puzzles 常指题目、游戏，puzzlers 还可指人；不能看到 -er 就强行只译成解题者。',
 ('The magazine includes several tricky puzzlers.','这本杂志里有几道棘手的谜题。'),('Experienced puzzlers finished the challenge in minutes.','有经验的解谜爱好者几分钟就完成了挑战。'),sources=S('puzzlers','puzzle'))
RIDDLE=[['谜语一支：古英语 raedels 等猜解材料 → riddle','旧词尾 s 被当成复数后去掉，与 read 的解释、猜解材料同族'],['筛具一支：古英语 hriddel → riddle 筛子','由筛、像筛子一样多孔，形成打得满是孔及 riddled with 布满的用法；不是由谜语推出漏洞']]
W('riddles','/ˈrɪdəlz/','谜语、谜团〔复数〕；出谜、打得多孔、筛〔第三人称单数〕',
 '需要猜的几道谜语是 riddles；另一支动词可让东西变得像筛子一样满是孔。谜语和筛具虽然同形，来源不同。',
 'riddle + -s，词尾读 /z/；名词复数与动词三单同形，先判断是在说谜题还是筛、打孔。',RIDDLE+[['riddle + -s → riddles','多个谜语、谜团；另源动词的现代三单']],
 'tell riddles 说谜语；solve riddles 解谜；riddles something with holes 把某物打得多孔。',
 'children’s riddles；unanswered riddles 未解谜团。',
 'riddles 的谜语义与 riddled with errors 的满是错误不是一条从谜面变错误的历史，后者接筛孔那一路。',
 ('The children took turns telling riddles.','孩子们轮流说谜语。'),('Heavy hail riddles the soft leaves with holes.','强烈的冰雹把柔软的叶片打得到处是孔。'),sources=S('riddles','riddle'))
W('riddled','/ˈrɪdəld/','满是孔的；充斥、布满问题等的；出谜、解谜了',
 '一张板上到处是孔，像筛子，叫 riddled with holes；文章处处是错，也像坏点散得到处都是，叫 riddled with errors。',
 'riddle 去 e 加完整 -ed，词尾读 /d/；满布用法接筛具一支，谜语动词也有同形过去式。',RIDDLE+[['riddle → riddled','筛孔一支形成满布；另源出谜、解谜动词也同形']],
 'riddled with holes 满是孔；riddled with errors 错误百出；riddled with problems 问题重重。',
 'a report riddled with mistakes；a wall riddled with holes。',
 'riddled with 常带不良内容到处都是的评价；filled with flowers 只是装满花，通常不带这种坏点遍布的感觉。',
 ('The draft was riddled with spelling mistakes.','草稿里到处是拼写错误。'),('The old wooden panel was riddled with tiny holes.','那块旧木板上满是小孔。'),sources=S('riddled','riddle'))
W('riddling','/ˈrɪdlɪŋ/','谜语般含混的；正在出谜、解谜；筛、打孔',
 '话故意说得弯弯绕绕，让人猜里面什么意思，可以叫 riddling words；筛东西、打出孔的动作则属于同形的另一支。',
 'riddle 去 e 加 -ing；谜语名词转用的动词与筛具转用的动词都能有这个形式，具体来源分开。',RIDDLE+[['riddle → riddling','出谜、猜解过程与含谜语的性质；另一路是筛、打孔过程']],
 'a riddling answer 谜语般的回答；riddling language 隐晦让人猜的话；riddling sand 筛沙，较专门的器具义。',
 'riddling remarks；speak in a riddling way。',
 'riddling answer 常像故意留谜面，confusing answer 也可能只是说得差、无意让人糊涂；意图的感觉不同。',
 ('She answered in a playful, riddling way.','她用一种俏皮、像说谜语的方式回答。'),('His riddling remarks left us guessing.','他那些谜语般的话，让我们猜个不停。'),sources=S('riddling','riddle'))
BAFFLE=[['早期英语 baffle：羞辱、使丢脸','更早来源未定，可能联系苏格兰语、法语羞辱等材料'],['挫败努力、使行不通 → 难住、使困惑','后来还以 baffle 命名阻挡、改变气流水流声音的挡板']]
W('baffle','/ˈbæfəl/','使困惑、难住；挫败；挡板',
 '几种办法都试了，仍想不明白，问题把人卡住了，叫 baffle；工程里把流动挡一下、改个方向的板，也叫 a baffle。',
 '基础词来源未定，早期有羞辱义，后有挫败、造成困难；挡板名词后来由阻挡动作发展。现代不强造一个确定 baff 词根。',BAFFLE,
 'baffle the experts 把专家难住；a baffle in a tank 水箱里的挡板；baffle attempts 使尝试受挫。',
 'continue to baffle 继续令人费解；an acoustic baffle 声学挡板。',
 'puzzle 可让人琢磨，baffle 更常给人思路受阻、尝试也没解开的感觉；不代表这个问题永远无解。',
 ('The strange result continues to baffle the experts.','这个奇怪的结果仍把专家们难住了。'),('A baffle inside the tank slows the flow of water.','水箱内的一块挡板减缓了水流。'),sources=S('baffle','baffle'))
W('baffles','/ˈbæfəlz/','使困惑、难住、挫败〔第三人称单数〕；挡板〔复数〕',
 '一个问题让人试来试去都解不开，动词用 baffles；几块挡住、改变流向的板，则是名词 baffles。',
 'baffle + -s，词尾读 /z/；名词复数和动词三单同形，基础来源未定。',BAFFLE+[['baffle + -s → baffles','它难住人；多个改变流动的挡板']],
 'baffles me 让我想不通；internal baffles 内部挡板；sound baffles 声学挡板。',
 'baffles attempts to explain；a series of baffles。',
 'baffles 说挡板时是可见的器件，说问题时则是动作；看 two、internal 等修饰与主谓关系。',
 ('What baffles me is why the error appears only at night.','让我想不通的是，这个错误为什么只在夜里出现。'),('Several baffles divide the airflow inside the chamber.','几块挡板把腔体内的气流分开。'),sources=S('baffles','baffle'))
W('baffled','/ˈbæfəld/','困惑、被难住的；挫败、使困惑了',
 '线索都摆在面前，自己却接不起来，只能停着想“怎么会这样”，就是 baffled。',
 'baffle 去 e 加完整 -ed，词尾读 /d/；常作人的困惑状态形容词，也可作动作过去形式。',BAFFLE+[['baffle → baffled','过去难住；也形容被问题卡住的人']],
 'a baffled look 困惑的目光；baffled by the result 被结果难住；left everyone baffled 让大家都想不通。',
 'completely baffled；baffled but curious。',
 'baffled 说人的感受，baffling 说事情令人费解；the baffled engineer、the baffling fault。',
 ('The engineer looked baffled by the strange noise.','那阵奇怪的噪声让工程师显得很困惑。'),('I was completely baffled by the final question.','最后一道题把我彻底难住了。'),sources=S('baffled','baffle'))
W('baffling','/ˈbæflɪŋ/','令人困惑、难以理解的；正在难住人',
 '事物不按能理解的规律来，试着解释也接不上，叫 baffling。重点不是单纯信息多，而是让理解卡住。',
 'baffle 去 e 加 -ing；动作形式也形容造成困惑的性质，常见读音可收成 /ˈbæflɪŋ/。',BAFFLE+[['baffle → baffling','使人困惑正在发生；也描述令人难解']],
 'a baffling mystery 令人费解的谜团；a baffling result 难以理解的结果；baffling the experts 正在把专家难住。',
 'a baffling decision；a baffling explanation。',
 'complex 只说结构复杂，有时仍然很清楚；baffling 额外说人无法顺利理解。',
 ('The machine produced a baffling series of errors.','机器接连出现一串让人摸不着头脑的错误。'),('It was a baffling decision that nobody could explain.','那是个令人费解、谁也解释不清的决定。'),sources=S('baffling','baffle'))
W('bafflingly','/ˈbæflɪŋli/','令人费解地；难以理解地',
 '该回应的人一直不说话，偏偏你想不通原因，就可以写 bafflingly silent；副词把不解一并放进描述里。',
 'baffling + 副词 -ly；内层 baffle 去 e 加 -ing，外层修饰事物令人困惑的程度、方式。',BAFFLE+[['baffling + -ly → bafflingly','以让理解受阻的方式；或修饰难解程度']],
 'bafflingly vague 模糊得令人费解；bafflingly inconsistent 不一致得让人想不通。',
 'bafflingly silent；bafflingly complicated。',
 'bafflingly 是说理解上受阻，deliberately 才明确故意；一个回答让人费解，并不能只凭副词断言对方有意为之。',
 ('His answer was bafflingly vague.','他的回答含糊得让人想不通。'),('The figures were bafflingly inconsistent across the two pages.','两页上的数字不一致，令人费解。'),sources=S('bafflingly','baffle'))
W('bafflement','/ˈbæfəlmənt/','困惑；被难住、理不出头绪的状态',
 '想了半天仍然接不上，脸上挂着“这怎么解释”的样子；把这份困惑当名词，就是 bafflement。',
 'baffle 去 e 加 -ment；动词使人难住，名词命名相应状态、反应。',BAFFLE+[['baffle + -ment → bafflement','被问题卡住、无法理解的状态']],
 'in bafflement 困惑地；a look of bafflement 不解的神情；to my bafflement 让我不解的是。',
 'complete bafflement；a mixture of curiosity and bafflement。',
 'bafflement 侧重想不明白，frustration 侧重受阻后的烦躁、挫败；两种感受可以同时存在。',
 ('She shook her head in bafflement.','她困惑地摇了摇头。'),('The explanation only increased our bafflement.','这番解释只让我们更摸不着头脑。'),sources=S('bafflement','baffle'))
BEFUDDLE=[['fuddle 的醉、仿佛醉后迷糊材料','更早来源未定，可能接低地德语相关形式'],['be- 加 fuddle → befuddle','早期可说饮酒等使头脑迷糊，后来也写复杂信息把人弄糊涂；现代不要求涉及酒']]
W('befuddle','/bɪˈfʌdəl/','使迷糊、糊涂；把头脑搅乱',
 '原本还勉强理得清，说明越听越多、数字越摆越乱，脑子像一团雾，这些东西会 befuddle someone。',
 'be- 加 fuddle；后者有醉、像醉了一样迷糊的旧用法，远源未定。现代是使头脑不清楚，不要求真喝了酒。',BEFUDDLE,
 'befuddle the audience 把观众弄糊涂；befuddle beginners 使初学者迷糊。',
 'details that befuddle me；a rule that may befuddle readers。',
 'baffle 更像一个问题把理解卡住，befuddle 更容易写头脑被搅得不清楚；日常也有交叠。',
 ('Too many technical terms can befuddle a new reader.','技术术语太多，会把新读者弄糊涂。'),('His explanation seemed to befuddle rather than help us.','他的解释似乎只把我们越说越糊涂，没帮上忙。'),sources=S('befuddle','befuddle'))
W('befuddles','/bɪˈfʌdəlz/','使迷糊、搅乱头脑〔第三人称单数〕',
 '一套规矩刚说明白，又添一层例外，人脑子转不过来；造成这种混乱的东西 befuddles someone。',
 'befuddle + -s，词尾读 /z/；内层 be- + fuddle 的动词整体再加三单词尾。',BEFUDDLE+[['befuddle + -s → befuddles','它把人的思路弄得不清楚']],
 'befuddles me 把我弄糊涂；befuddles beginners 使初学者迷糊。',
 'a system that befuddles users；befuddles even experienced readers。',
 'befuddles 是造成反应，is befuddled 才是承受反应；换主语时把动作方向也看清楚。',
 ('The changing timetable befuddles even regular passengers.','时刻表变来变去，连常坐的乘客也被弄糊涂。'),('This explanation befuddles me more than the original question.','这个解释比原问题更让我糊涂。'),sources=S('befuddles','befuddle'))
W('befuddled','/bɪˈfʌdəld/','迷糊、糊涂的；使人糊涂了',
 '眼前一堆事情，人却还没理清，回话有点慢、方向也拿不准，叫 befuddled。像头脑里没完全透亮。',
 'befuddle 去 e 加完整 -ed，词尾读 /d/；过去形式又常作描述人状态的形容词。',BEFUDDLE+[['befuddle → befuddled','已经被弄迷糊；也形容思路不清楚']],
 'a befuddled look 迷糊的神情；befuddled by the instructions 被说明弄糊涂。',
 'slightly befuddled；looked tired and befuddled。',
 'befuddled 不要求原因一定是酒，繁杂说明、疲倦、陌生情境都可在叙述中造成这种迷糊感。',
 ('He looked befuddled by the complicated directions.','复杂的指路说明把他弄得有些迷糊。'),('I was still befuddled after the long overnight journey.','熬夜长途旅行后，我仍有些迷迷糊糊。'),sources=S('befuddled','befuddle'))
W('befuddling','/bɪˈfʌdlɪŋ/','令人迷糊的；正在把人弄糊涂',
 '说明本来是带路的，听完却更找不着方向；这种把思路越搅越乱的说明是 befuddling。',
 'befuddle 去 e 加完整 -ing；既作动作形式，也形容让头脑不清楚的事物。',BEFUDDLE+[['befuddle → befuddling','使人迷糊的过程与性质']],
 'befuddling instructions 令人糊涂的说明；a befuddling array of choices 多得让人不知怎么选的选项。',
 'a befuddling explanation；find the process befuddling。',
 'befuddling 描述事物带来的反应，befuddled 描述人的状态：befuddling rules 让读者成为 befuddled readers。',
 ('The form came with a befuddling set of instructions.','表格附带的填写说明让人越看越糊涂。'),('I found the constant changes befuddling.','不断的变动让我理不清头绪。'),sources=S('befuddling','befuddle'))
W('befuddlement','/bɪˈfʌdəlmənt/','迷糊；头脑混乱、理不清的状态',
 '听完一大段，人还没接上，望着纸发愣；把这种迷糊状态叫作 befuddlement。',
 'befuddle 去 e 加 -ment；把使人迷糊的动词变成相应状态的名词。',BEFUDDLE+[['befuddle + -ment → befuddlement','头脑被搅乱、暂时理不清的状态']],
 'in befuddlement 一头雾水地；a look of befuddlement 迷糊的表情。',
 'complete befuddlement；a moment of befuddlement。',
 'befuddlement 偏向脑子里乱、跟不上，bafflement 偏向某个问题想不通；实际语境可相近，不必硬划绝对界线。',
 ('She stared at the timetable in befuddlement.','她望着时刻表，一头雾水。'),('His expression changed from confidence to befuddlement.','他的表情从自信变成了迷糊。'),sources=S('befuddlement','befuddle'))
MUDDLE=[['早期英语 muddle：使清楚的状态遭到破坏','可能是 mud 的反复动作形式，也可能借荷兰语 moddelen 一类同族词'],['使浑浊、使混乱等意义并行发展','不能按现代联想把泥水义一律排在最早；后来还有弄错、笨拙应付和名词混乱局面']]
W('muddle','/ˈmʌdəl/','弄混、搞乱；混乱局面；勉强应付',
 '清水搅浑后看不清底，事情搅乱后也找不清头绪：把姓名、时间混在一起，可以用 muddle。这个画面帮助理解，具体历史并非所有抽象义都晚于泥水义。',
 '可能接 mud 的旧反复动作形式，也可能借荷兰语同族词；现代不能只凭字母就确定是英语 mud + -le。名词混乱局面由动词发展。',MUDDLE,
 'muddle the names up 把名字弄混；in a muddle 一团乱；muddle through 没有好计划也勉强撑过去。',
 'get into a muddle；muddle through a difficult week。',
 'muddle through 有磕磕绊绊仍设法完成的意思；fail 则明确没有成功。不要只看到 muddle 就译成彻底搞砸。',
 ('I always muddle the twins’ names up.','我老把这对双胞胎的名字弄混。'),('We had no clear plan, but we managed to muddle through.','我们没有清楚的计划，不过还是磕磕绊绊地应付过去了。'),sources=S('muddle','muddle'))
W('muddles','/ˈmʌdəlz/','弄混、搞乱〔第三人称单数〕；混乱局面〔复数〕',
 '他每次都把两个日期对不上，叫 he muddles them up；好几处乱套的安排，也能叫 muddles。',
 'muddle + -s，读 /z/；动词三单和名词复数同形。mud 相关的更早构词、借入路径存在不同分析。',MUDDLE+[['muddle + -s → muddles','它把事情弄混；多处混乱局面']],
 'muddles things up 把事情搅乱；administrative muddles 行政安排上的混乱。',
 'muddles the dates；a series of muddles。',
 'mistakes 是具体错误，muddles 可以指安排、关系纠缠成一团的局面；一场 muddle 里可能包含多个 mistakes。',
 ('He often muddles the departure date with the return date.','他常把出发日期和返程日期弄混。'),('Several booking muddles delayed the trip.','预订上几处乱套的安排耽误了行程。'),sources=S('muddles','muddle'))
W('muddled','/ˈmʌdəld/','混乱、含混不清的；弄混了',
 '纸上有想法，但前后打架，自己也说不明白，叫 muddled thinking；日期记反了，也能说 got the dates muddled。',
 'muddle 去 e 加完整 -ed，词尾读 /d/；过去形式也描述已经混乱、不清楚的状态。',MUDDLE+[['muddle → muddled','把事情弄混；或描述混乱后的状态']],
 'muddled thinking 混乱的思路；a muddled explanation 条理不清的解释；get the names muddled 把名字弄混。',
 'feel muddled；a muddled account of events。',
 'muddled explanation 可以是说话者自己也没理顺，misleading explanation 则说会把听者引向错误理解；后者也未必故意。',
 ('The report gives a muddled account of what happened.','报告把事情经过讲得乱七八糟。'),('I got the dates muddled and arrived a day early.','我把日期弄混了，早到了一天。'),sources=S('muddled','muddle'))
W('muddling','/ˈmʌdlɪŋ/','正在弄混、搞乱；勉强应付着',
 '东西还在被越弄越乱，是 muddling；但 muddling through 这个搭配往往说办法不漂亮，人仍在设法往前走。',
 'muddle 去 e 加 -ing；表示过程。through 带来穿过难关、应付到底的方向感，是搭配意义的重要部分。',MUDDLE+[['muddle → muddling','正在混淆；与 through 连用可写勉强应付的过程']],
 'muddling the names up 正把名字弄混；muddling through 勉强应付着。',
 'keep muddling things up；muddling through without much help。',
 'muddling through 不一定过程很顺，但通常仍在设法继续；struggling 只强调吃力，不保证已经撑过去。',
 ('You are muddling the two stories together.','你正在把那两件事混到一起。'),('We are muddling through while the manager is away.','经理不在时，我们正磕磕绊绊地应付着。'),sources=S('muddling','muddle'))
W('bemuses','/bɪˈmjuːzɪz/','使困惑、出神；使带着不解而觉得好笑〔第三人称单数〕',
 '一件事让人停下来发愣，觉得“这是什么情况”，可以说 it bemuses me；有时还带着无奈、诧异而觉得好笑的反应。',
 'bemuse + -s，/z/ 后的词尾加出 /ɪz/。内层是 be- + muse 动词；muse 接法语 muser，不能只因同形就改接希腊神话的 Muse。',
 [['法语 muser → 英语 muse 动词','沉思、出神等意义，远源存在不同解释'],['英语 be- + muse → bemuse → bemuses','使出神、使困惑；现代也可含困惑与微妙好笑并存']],
 'bemuses me 让我不解；bemuses outsiders 让局外人看不懂。',
 'a custom that bemuses visitors；the attention bemuses him。',
 'amuses 主要是使人觉得有趣、开心；bemuses 通常保留想不通、发愣的成分，部分语境里两种反应会交叠。',
 ('The complicated ticket system bemuses many visitors.','复杂的售票系统让许多游客摸不着头脑。'),('It bemuses her that a tiny joke has attracted so much attention.','那么小的一个玩笑竟引来这么多关注，让她又不解又觉得有点好笑。'),sources=S('bemuses','bemuse')+['https://www.merriam-webster.com/dictionary/bemused'])
W('confounds','/kənˈfaʊndz/','使困惑；混淆；使预期落空〔第三人称单数〕',
 '不同东西倒在一起，就难分彼此；confound 保留了混在一起的核心。结果与预测完全对不上，也会让原来的判断站不住脚，叫 confounds expectations。',
 'confound + -s，读 /z/。基础词经法语 confondre、confoundre 接拉丁 confundere：con- 一起 + fundere 倾倒。抽象混淆、使困惑在拉丁语里就已有。',
 [['拉丁 con- + fundere → confundere','倒在一起、混合，并已有混淆、使困惑的抽象用法'],['法语 confondre 等 → 英语 confound → confounds','使困惑、把不同事物混为一谈；结果使预期落空']],
 'confounds expectations 出乎预期、使预期落空；confounds the experts 让专家也想不通。',
 'confounds two different issues 把两个不同问题混为一谈；confounds predictions 与预测相悖。',
 'confirms expectations 是印证预期，confounds expectations 是结果让原来的预期落空；不要把两个近形动词看反。',
 ('The team’s success confounds all the early predictions.','这支球队的成功让早先的所有预测都落了空。'),('His argument confounds personal preference with objective evidence.','他的论证把个人喜好与客观证据混为一谈。'),sources=S('confounds','confound'))
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_zgh',ROOTS,WORDS)
 extend_lessons()
