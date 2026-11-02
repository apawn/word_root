"""Awkward motion: stumble, fumble, flounder and blunder."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
def S(word,base):
 return ['https://en.wiktionary.org/wiki/'+word+'#English','https://www.etymonline.com/word/'+base]
EXISTING_ROOT_ADDITIONS={
 'A1760':dict(words='flounder flounders floundered floundering'.split(),label='flounder：动作费劲，难以前进',note='动词来源未定，可能受 founder 沉、倒下与荷兰语等笨拙动作材料影响；鱼名 flounder 另经法语、古诺尔斯语接平展材料，不把动词定成因鱼扑腾而得名。'),
 'A2238':dict(words='stumble stumbles stumbled stumbling fumble fumbles fumbled fumbling'.split(),label='stumble 与 fumble：脚下卡住、手上不顺',note='两个词都有北欧日耳曼来源等分析，但近源并非同一条确定链。stumble 的 b 或为发音中增入、或受别词影响；fumble 可能接 falma 等摸索材料，也有拟声、拟态分析。'),
 'B3748':dict(words='blunder blunders blundered blundering'.split(),label='blunder：乱闯，到犯下大错',note='blunder 接北欧闭眼、乱撞等来源线索，或有混乱词族影响；与本页 blend 作辨析，不能把现代 blend 加 -er 当成确定来历。'),
 'C0238':dict(words='recline reclines reclined reclining recliner recliners'.split(),label='recline：往后靠，到可调躺椅',note='拉丁 re- 向后 + clinare 倾斜，经法语、拉丁路线成英语 recline。recliner 早可说人、物，后来特指可把靠背放倒的椅子。'),
 'B3446':dict(words='lounger loungers'.split(),label='loungers：闲躺的人，或休闲躺椅',note='lounge 去 e 加完整 -er，再加复数 -s；词尾 e 的拼写调整不改变完整后缀。lounge 更远来源有法语伸长、旧懒散者称呼等不同分析。'),
 'A1740':dict(words='limp limply'.split(),label='limply：软塌塌、没力地',note='limply 用形容词 limp 松软、无力的义加 -ly；跛行的 limp 动词另看基础词。二者更远联系有分析，不能把每句 limply 都译成跛着脚。'),
}
FLOUNDER=[['flounder 动词来源未定','可能受 founder 与荷兰语等笨拙动作词影响，不定为鱼名派生'],['笨拙、费力地挣扎 → 做事没有头绪、难以前进','鱼名另经法语、古诺尔斯语接平展的材料']]
STUMBLE=[['中古英语 stomblen；可能来自北欧日耳曼材料','b 可能为发音增入或受 stumpen 影响，近源仍有不确定性'],['绊脚、失足与早期比喻 → 说话卡壳、做事不顺','后来 stumble on/upon 也能说偶然发现']]
FUMBLE=[['中古英语 fumble 笨拙地拿弄','可能接古诺尔斯 falma 等材料，也有拟声、拟态分析'],['手上拿不顺 → 笨拙摸索、处理不好','后来还有球类运动中持球失误的用法']]
BLUNDER=[['中古英语 blundren；北欧闭眼、乱撞等来源线索','较早动词已有盲目跌撞的画面'],['犯大错、乱闯等现代义发展','现代名词大错的记录略早于相应动词义，不能把学习次序当年表']]
RECLINE=[['拉丁 re- 向后 + clinare 倾斜 → reclinare','经法语或拉丁材料进入英语'],['使向后靠 → 自己半躺、椅背后仰','recliner 后来可指靠背可放倒的椅子']]
W('flounder','英 /ˈflaʊndə/；美 /ˈflaʊndɚ/','费力、笨拙地挣扎；做事没有头绪；比目鱼类',
 '深雪里腿抬不出来，越挣扎越乱，是 flounder；回答问题时没头绪、越说越乱也能用。食物、鱼类里的 flounder 是另一条来源。',
 '动词来源未定，可能受 founder 沉、倒下与笨拙动作词影响。鱼名经法语 floundre、古诺尔斯 flydhra 等，接平展的旧材料，不能定成动词从鱼扑腾来。',FLOUNDER,
 'flounder in deep snow 在深雪里艰难挣扎；flounder for an answer 回答时没头绪。',
 'flounder under pressure；grilled flounder 烤比目鱼。',
 'flounder 强调挣扎得笨拙、难有进展，founder 常说沉没、计划失败；二者不能只按近音当成一个词。',
 ('Without clear instructions, new staff may flounder.','没有清楚的指引，新员工可能会忙乱得不知从何下手。'),('The restaurant serves grilled flounder with lemon.','那家餐馆供应配柠檬的烤比目鱼。'),sources=S('flounder','flounder'))
W('flounders','英 /ˈflaʊndəz/；美 /ˈflaʊndɚz/','费力挣扎、手足无措〔第三人称单数〕；比目鱼类〔复数之一〕',
 '一遇开放问题，他就没头绪、答得东一榔头西一棒，可以说 flounders。鱼类名词也可用 flounders 作复数，或用同形 flounder。',
 'flounder + -s，读 /z/；动词三单与鱼名一种复数同形，但两条来源分开。',FLOUNDER+[['flounder + -s → flounders','他或它笨拙挣扎；也可说多条比目鱼']],
 'flounders under pressure 压力下手忙脚乱；flounders without guidance。',
 'flounders for an answer；flat flounders on the seabed。',
 'flounders 写难以应付的过程，fails 直接说失败；挣扎时可能最后仍找到办法。',
 ('He flounders when a question has no obvious answer.','问题没有明显答案时，他就答得没了头绪。'),('Flounders lie flat on the sandy seabed.','比目鱼平贴在沙质海底上。'),sources=S('flounders','flounder'))
W('floundered','英 /ˈflaʊndəd/；美 /ˈflaʊndɚd/','费力挣扎了；曾手足无措、无从推进',
 '刚才在泥里挪不动，或解释计划时没准备好、说得乱七八糟，可以说 floundered。重点是过程中费劲又不顺。',
 'flounder + 完整 -ed，读 /d/；不另增 /ɪd/。动词近源仍保留不确定性。',FLOUNDER+[['flounder + -ed → floundered','过去曾笨拙、费力地挣扎']],
 'floundered in the mud 在泥里挣扎；floundered during the interview。',
 'floundered for several minutes；floundered without a plan。',
 'struggled 可说努力应对，floundered 更让人看见笨拙、没头绪；努力并不都等于乱了阵脚。',
 ('We floundered through the deep snow.','我们在深雪里费力地挣扎前行。'),('She floundered when asked to explain the unexpected results.','被问到如何解释意外结果时，她答得没了头绪。'),sources=S('floundered','flounder'))
W('floundering','英 /ˈflaʊndərɪŋ/；美 /ˈflaʊndərɪŋ/','正在笨拙挣扎、难以前进；陷入困境的',
 '动了不少，却没抓住方向，项目、人或生意都可能 floundering。它让人感觉需要支撑、指引，才能重新往前走。',
 'flounder + -ing；英式在元音后缀前读出 r。分词可写过程，也可形容处于困境的事物。',FLOUNDER+[['flounder + -ing → floundering','费力、无从着手的过程或状态']],
 'a floundering business 陷入困境的生意；floundering for an answer。',
 'left floundering 被弄得不知所措；floundering in deep water。',
 'floundering 是应付不来、进展困难，floating 只是漂浮；在水里漂着不一定在挣扎。',
 ('The new manager took over a floundering business.','新经理接手了一门陷入困境的生意。'),('I was floundering until someone showed me the first step.','直到有人示范第一步前，我一直手忙脚乱，不知从何下手。'),sources=S('floundering','flounder'))
W('stumble','/ˈstʌmbəl/','绊一下、踉跄；讲话卡壳；偶然发现',
 '脚被路边东西带住，身体猛地向前一晃，是 stumble。讲话时被某个词卡住，也像嘴上绊了一下；stumble upon 则是偶然碰见、发现。',
 '可能来自北欧日耳曼材料；中古英语有 stomblen，b 或是发音增入、或受别词影响。脚下失足与比喻用法都很早，不能把抽象义一概说成现代才有。',STUMBLE,
 'stumble over a stone 被石头绊一下；stumble over a word 读一个词卡壳。',
 'stumble upon a discovery 偶然有发现；stumble through a speech 磕磕绊绊讲完。',
 'stumble 可以晃一下后站稳，fall 是摔倒；绊到并不一定已经倒地。',
 ('Be careful not to stumble over the cable.','小心别被那根电线绊到。'),('You may stumble upon a useful detail while reading.','阅读时，你可能会偶然发现一个有用的细节。'),sources=S('stumble','stumble'))
W('stumbles','/ˈstʌmbəlz/','绊一下；讲话卡壳；偶然发现〔第三人称单数〕；失误〔复数〕',
 '他总在某个名字前读得不顺，是 stumbles over it；公司前进中的几个失误，也可叫 stumbles。看句子就能把动作与可数失误分开。',
 'stumble + -s，读 /z/；动词三单与名词复数同形。',STUMBLE+[['stumble + -s → stumbles','他或它绊住、卡住；也可说多次失误']],
 'stumbles over a name；early stumbles 初期的失误。',
 'stumbles upon a clue 偶然发现线索；stumbles through an explanation。',
 'stumbles over a word 是说词时卡壳，does not know a word 是不认识；认识的词也会因紧张念不顺。',
 ('He always stumbles over the same difficult name.','那个难读的名字，他每次都会念得磕绊。'),('The company recovered from its early stumbles.','公司从初期的几次失误中恢复过来了。'),sources=S('stumbles','stumble'))
W('stumbled','/ˈstʌmbəld/','绊到、踉跄了；讲话卡壳了；偶然发现了',
 '刚才脚下一绊，可以说 stumbled；无意翻到一本好书，是 stumbled upon a book。偶然发现不是因为真摔进了书里。',
 'stumble 去 e 加完整 -ed，读 /d/；过去式、过去分词。',STUMBLE+[['stumble + -ed → stumbled','过去绊到、卡壳，或偶然遇见']],
 'stumbled over a root 被树根绊一下；stumbled upon an old photograph。',
 'stumbled into the room 踉跄着进屋；stumbled through the answer。',
 'stumbled upon 常是偶然发现，searched for 是主动寻找；寻找过程中也可能意外碰到另一件东西。',
 ('I stumbled over a tree root but kept my balance.','我被树根绊了一下，但稳住了身子。'),('She stumbled upon an old photograph in the drawer.','她在抽屉里偶然翻到一张老照片。'),sources=S('stumbled','stumble'))
W('stumbling','/ˈstʌmbəlɪŋ/','正在踉跄、磕绊；不顺畅的',
 '脚步一会儿卡一下，话也说得断断续续，可以写 stumbling。stumbling block 把绊脚的东西借来指障碍，是常见搭配。',
 'stumble 去 e 加 -ing；不重复 l。分词可写动作，也可在 stumbling block 中描写造成阻碍的性质。',STUMBLE+[['stumble + -ing → stumbling','绊住、磕绊的过程；常见搭配中表示造成困难']],
 'a stumbling block 障碍；a stumbling explanation 磕磕绊绊的解释。',
 'stumbling over words；stumbling along the path。',
 'stumbling block 不是只能指真的路障；语言、费用、分歧都可能是让事情推进不下去的障碍。',
 ('She was stumbling over her words with excitement.','她激动得说话都有些磕绊。'),('Cost remains the main stumbling block.','费用仍是主要障碍。'),sources=S('stumbling','stumble'))
W('fumble','/ˈfʌmbəl/','笨拙地摸索、拿弄；没处理好；持球失误',
 '钥匙明明在手里，却怎么也对不准锁孔，是 fumble。话、机会也可能被笨拙地处理坏；球没拿稳掉下去也是常见场景。',
 '可能接古诺尔斯 falma 等摸索材料；北欧、北海日耳曼语中有相似词，也有拟声、拟态分析。不是按现代英语字母能确定拆出的组合。',FUMBLE,
 'fumble for the keys 笨拙地摸找钥匙；fumble with the lock 摆弄锁却不顺。',
 'fumble a catch 没接稳球；fumble for words 找不到顺口的话。',
 'stumble 常像脚下、话上绊住，fumble 更像手上或处理事情时不利索；二者有相近画面，但重点不同。',
 ('I began to fumble for my keys in the dark.','黑暗中，我开始笨手笨脚地摸找钥匙。'),('Do not fumble the chance to explain your idea clearly.','别笨拙应付，把清楚解释想法的机会弄丢。'),sources=S('fumble','fumble'))
W('fumbles','/ˈfʌmbəlz/','笨拙地摸索、拿弄〔第三人称单数〕；失误、掉球〔复数〕',
 '一紧张，他就拿不稳杯子、找不到要说的话，可以说 fumbles。球赛统计里的 fumbles 往往指持球失误的次数。',
 'fumble + -s，读 /z/；动词三单与名词复数同形。名词由既有动词发展，球类专用义较晚。',FUMBLE+[['fumble + -s → fumbles','他或她拿弄不顺；多次失误、掉球']],
 'fumbles with the buttons 笨拙地摆弄纽扣；several fumbles 几次持球失误。',
 'fumbles for an answer；fumbles in a game。',
 'fumbles with a button 说动作不利索，cannot find a button 是找不着纽扣；目标在手边也可能笨拙地弄不好。',
 ('He fumbles with the tiny buttons when he is nervous.','一紧张，他就扣不好那些小纽扣。'),('Two costly fumbles changed the course of the game.','两次代价很大的持球失误改变了比赛走势。'),sources=S('fumbles','fumble'))
W('fumbled','/ˈfʌmbəld/','笨拙地摸索、拿弄了；没处理好、掉球了',
 '刚才找手机时手忙脚乱，或者球到手又没拿稳，是 fumbled。它不一定说有意犯错，常是紧张、匆忙下不利索。',
 'fumble 去 e 加完整 -ed，读 /d/；不是 /ɪd/。',FUMBLE+[['fumble + -ed → fumbled','过去摸索不顺、拿弄失误']],
 'fumbled for the switch 摸索开关；fumbled the ball 没拿稳球。',
 'fumbled with a zip；fumbled an explanation 解释得不顺。',
 'dropped 只说掉下，fumbled the ball 通常说明处理、控制球出了失误；掉落也可能是主动放下。',
 ('She fumbled for the light switch.','她手忙脚乱地摸找电灯开关。'),('He fumbled the ball just before reaching the line.','他眼看就到线前，却没拿稳球。'),sources=S('fumbled','fumble'))
W('fumbling','/ˈfʌmbəlɪŋ/','正在笨拙摸索；不利索、磕绊的',
 '手在包里乱摸，话到嘴边也组织不好，是 fumbling。用作形容词时，常写一段动作、解释不够熟练。',
 'fumble 去 e 加 -ing；过程分词也能形容笨拙、不熟练的表现。',FUMBLE+[['fumble + -ing → fumbling','摸索的过程，或处理不顺的性质']],
 'fumbling with a lock 笨拙地摆弄锁；a fumbling apology 支支吾吾、不顺畅的道歉。',
 'fumbling for words；fumbling in a bag。',
 'fumbling 强调不利索，deliberate 强调有意、从容；动作慢可能因为认真，也可能因为手忙脚乱。',
 ('He was fumbling in his bag for a pen.','他正手忙脚乱地在包里摸找笔。'),('She offered a fumbling apology.','她道歉道得不太利索，有点支支吾吾。'),sources=S('fumbling','fumble'))
W('blunders','英 /ˈblʌndəz/；美 /ˈblʌndɚz/','犯大错、冒失乱闯〔第三人称单数〕；大错〔复数〕',
 '明明应该核对却连连弄错，是 makes blunders；不看情况就闯进来，也是 blunders in。比普通 mistake 更有笨拙、严重失误的评价。',
 'blunder + -s，读 /z/；动词三单、名词复数同形。基础词有北欧闭眼、乱撞来源线索，不是现代 blend 加人称 -er。',BLUNDER+[['blunder + -s → blunders','他或她犯错、乱闯；多次大失误']],
 'serious blunders 严重错误；blunders into trouble 冒失地陷入麻烦。',
 'administrative blunders；blunders through an explanation。',
 'blunders 往往比 errors 更带明显、笨拙或不该犯的评价；测量中很小的误差通常不叫大错。',
 ('The report exposed several serious blunders.','报告揭出了几次严重失误。'),('He blunders into the room without noticing the meeting.','他没注意到正在开会，冒冒失失闯进房间。'),sources=S('blunders','blunder'))
W('blundered','英 /ˈblʌndəd/；美 /ˈblʌndɚd/','犯下大错了；冒失、跌撞着闯入了',
 '在没看清情况时做错选择，或者误闯一场正在进行的会议，可以说 blundered。像闭着眼往前闯的画面在历史中有来路。',
 'blunder + 完整 -ed，读 /d/；过去式、过去分词，不增加 /ɪd/。',BLUNDER+[['blunder + -ed → blundered','过去犯错、冒失乱闯']],
 'blundered into a meeting 误闯会议；blundered badly 犯下大错。',
 'blundered through the dark；had blundered in choosing。',
 'blundered into 常带无准备、没看清的冒失，entered 只是进入；进门这个动作未必是失误。',
 ('I blundered into the wrong meeting room.','我冒冒失失进错了会议室。'),('They blundered by announcing the result before checking it.','他们没核对就宣布结果，犯了个大错。'),sources=S('blundered','blunder'))
W('blundering','英 /ˈblʌndərɪŋ/；美 /ˈblʌndərɪŋ/','正在冒失乱闯、犯错；笨拙、频频出错的',
 '一路没看情况就闯，做事接连出明显错误，是 blundering。作形容词时常有强烈批评，如 a blundering attempt。',
 'blunder + -ing；英式在元音后缀前读出 r。可写动作过程，也可表示冒失、处理笨拙的性质。',BLUNDER+[['blunder + -ing → blundering','乱闯、犯错的过程，或笨拙失误的性质']],
 'a blundering attempt 笨拙、弄巧成拙的尝试；blundering into danger。',
 'blundering through an explanation；a blundering official。',
 'fumbling 常写不利索、摸索，blundering 常批评大错、冒失；紧张而讲得不顺不一定犯了大错。',
 ('His blundering attempt to help made the situation worse.','他冒失地想帮忙，反倒把情况弄得更糟。'),('We were blundering through the dark without a map.','我们没带地图，在黑暗里跌跌撞撞地乱走。'),sources=S('blundering','blunder'))
W('limply','/ˈlɪmpli/','软塌塌、松垂地；无力地',
 '旗子没风就软软垂着，手臂没使劲地搭在一边，都能说 limply。它说失去挺度、支撑的样子，不只是运动慢。',
 'limp 形容词松软、无力 + -ly；limp 更远来源不完全确定，另有跛行的动词，不把这种副词每次都当作跛着脚。',
 [['limp 形容词：松软、下垂、缺乏挺度','来源未定，有古英语及日耳曼松垂材料等分析'],['limp + -ly → limply','以没支撑、软软垂着或无力的方式']],
 'hang limply 软软地垂着；shake hands limply 无力地握手。',
 'arms hanging limply；a flag hanging limply。',
 'limply 描写松软、没力，limping 描写跛着走；一面软垂的旗子不会是在跛行。',
 ('The flag hung limply in the still air.','空气静止，旗子软软地垂着。'),('He shook my hand limply.','他有气无力地和我握了握手。'),sources=S('limply','limp'))
W('reclines','/rɪˈklaɪnz/','向后靠、半躺；使椅背后仰〔第三人称单数〕',
 '椅子靠背能向后放倒，可以说 it reclines；一个人靠到半躺的位置，也能用。重点是向后倾，不一定完全平躺。',
 'recline + -s，读 /z/；拉丁内部 re- 向后与 clinare 倾斜相接，现代这里是三单形式。',RECLINE+[['recline + -s → reclines','人向后靠，或椅背能够后仰']],
 'the seat reclines 座椅可后仰；reclines in a chair。',
 'reclines almost flat 几乎能放平；reclines on the sofa。',
 'reclines 是向后靠、后仰，declines 在常见句中可能是下降、拒绝；同一倾斜材料在不同前缀中分出不同意思。',
 ('The seat reclines almost flat.','这个座椅几乎能放平。'),('He reclines on the sofa with a book.','他拿着书，半躺在沙发上。'),sources=S('reclines','recline'))
W('reclined','/rɪˈklaɪnd/','向后靠、半躺了；把椅背放倒了',
 '坐累了把身体向后靠，或把座椅调得更平，过去做了这一下，可以说 reclined。句子有宾语时常是放倒椅背。',
 'recline 去 e 加完整 -ed，读 /d/；不另加 /ɪd/。',RECLINE+[['recline + -ed → reclined','过去向后靠，或把座椅调后仰']],
 'reclined her seat 把座椅往后放；reclined on cushions。',
 'reclined in an armchair；the seat was fully reclined。',
 'reclined 可以是有支撑地后靠，collapsed 常是失去支撑突然倒下；舒服调整姿势不等于倒塌、昏倒。',
 ('She reclined her seat after the meal.','饭后，她把座椅靠背往后放了放。'),('He reclined on the cushions and closed his eyes.','他半躺在靠垫上，闭上了眼睛。'),sources=S('reclined','recline'))
W('recliners','英 /rɪˈklaɪnəz/；美 /rɪˈklaɪnɚz/','靠背可放倒的躺椅、休闲椅〔复数〕',
 '客厅里那几把能把靠背放下、常还能抬脚的椅子，是 recliners。学习先抓椅背能后仰，不是所有软椅都具备这个结构。',
 'recliner + -s，读 /z/；recline 去 e 加完整 -er 成名词，再说多把椅子。基础名词历史上也可泛指后靠的人或物，椅子专用义较晚。',RECLINE+[['recline → recliner → recliners','后靠动作，到可后仰的椅子，再到多把']],
 'leather recliners 皮质可调躺椅；cinema recliners 电影院可后仰座椅。',
 'comfortable recliners；a pair of recliners。',
 'recliners 通常强调可后仰的结构，armchairs 只说有扶手的单人椅；有扶手不保证能调靠背。',
 ('The cinema replaced its old seats with recliners.','电影院把旧座椅换成了可后仰座椅。'),('Two leather recliners stood beside the window.','窗边放着两把皮质可调躺椅。'),sources=S('recliners','recline'))
W('loungers','英 /ˈlaʊndʒəz/；美 /ˈlaʊndʒɚz/','闲躺、闲散的人〔复数〕；休闲躺椅〔复数〕',
 '泳池边晒太阳的躺椅是 loungers；闲靠着没做事的人，也可叫 loungers。人和椅子，都从 lounge 闲躺这个动作来理解。',
 'lounger + -s，读 /z/；lounge 去 e 加完整 -er，再加复数。lounge 本身更远来历有不同分析，不能把法语伸长的猜测写成唯一确定链。',
 [['lounge 闲躺、懒洋洋地靠着 → lounger','做这种动作的人；也可指供人闲躺的椅子'],['lounger + -s → loungers','多个闲躺者，或多把休闲躺椅']],
 'sun loungers 日光躺椅；loungers beside the pool。',
 'a row of loungers；idle loungers 闲散者。',
 'loungers 是椅子或闲散的人，lounges 常是休息室、客厅等；同族词不能只看前面相同就互换。',
 ('There were several empty loungers beside the pool.','泳池边有几把空着的躺椅。'),('The novel describes wealthy loungers filling the hotel terrace.','小说写到酒店露台上坐满了富有的闲散客。'),sources=S('loungers','lounge'))
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_zho',ROOTS,WORDS)
 extend_lessons()
