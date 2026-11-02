"""Pressure, fine spray, sudden bursts, drops, drool and slow oozing."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
def S(word,base):
 return ['https://en.wiktionary.org/wiki/'+word+'#English','https://www.etymonline.com/word/'+base]
EXISTING_ROOT_ADDITIONS={
 'B4603':dict(words=['spray','sprays','sprayed','spraying'],label='spray 喷滴、小枝分源及现代变化',note='喷洒动词接中古荷兰语 sprayen 一系；花枝、小枝 spray 在中古英语另有记录，不从喷雾形状硬推来。'),
 'B4553':dict(words=['drip','drips','dripped','dripping','dribble','dribbles','dribbled','dribbling'],label='drip 与 dribble：滴落材料到连续小动作',note='drip 承古英语 drypan、dryppan；dribble 接旧 drib 的反复动作形式，体育控球再借连续轻触的动作，不能把运动义译成流口水。'),
 'A2238':dict(words=['drip','dribble','dribbles','dribbled','dribbling'],label='drib、drip 材料与 dribble 的旧反复尾',note='较早 drib 是滴、少量流一系的旧动词，dribble 带反复动作形式；现代 dribbled、dribbling 去 e 后加完整词尾。'),
 'A1760':dict(words='squeeze squeezes squeezed squeezing squash squashes squashing spray sprays sprayed spurt spurts spurted spurting gush gushes gushed gushing dribble dribbles dribbled dribbling drip drips dripped dripping drool drools drooled drooling ooze oozes oozed oozing'.split(),label='挤压、喷滴、涌出与缓流动词的变化',note='液体动作、挤压动作不因意义相近就合成一个古根。ooze 的软泥名词和汁液、渗流动词分别说近源，spurt 的液体喷出与短期活动名词历史关系保留不确定性。'),
}
SQUEEZE=[['较早 quease、quisen 等挤压材料可能参与 → squeeze','具体变化、近音词影响有不同分析，不给 squ-、ee 逐段编义'],['挤压 → 榨出、挤入、挤出时间资源','压力使空间变小，也让里面东西出来，形成常用搭配']]
W('squeezes','/ˈskwiːzɪz/','挤压、榨出、挤入〔第三人称单数〕；一挤、拥挤局面〔复数〕',
 '手把柠檬往里压、让汁出来，或人从窄处挤进去，用 squeezes。抓住两边收紧、空间变小的感觉。',
 'squeeze + -s，保留 e，/z/ 后读 /ɪz/；名词复数、动词三单同形。基础词更早来源有分歧。',SQUEEZE+[['squeeze + -s → squeezes','他、她挤压；它挤入；几次一挤']],
 'squeezes a lemon 是挤柠檬，squeezes into the seat 是挤进座位，squeezes in a visit 是挤出时间拜访。',
 'squeezes her hand 握紧她的手；squeezes out the juice 挤出汁。',
 'squeezes 强调压力、空间收紧，不一定把东西压坏；squashes 更容易让人想到压扁、变形。',
 ('She squeezes lemon juice over the salad.','她往沙拉上挤柠檬汁。'),('He squeezes into the last empty seat.','他挤进最后一个空座位。'),sources=S('squeezes','squeeze'))
W('squeezed','/skwiːzd/','挤压、榨出、挤入了；被挤紧、受压的',
 '刚才用力挤、榨出一点东西，或从窄缝里挤过去，用 squeezed。比喻安排时，也可说挤出一点时间。',
 'squeeze 去 e + 完整 -ed，/z/ 后读 /d/；已有 ee 保留长元音，不多读 /ɪd/。',SQUEEZE+[['squeeze 去 e + -ed → squeezed','过去挤压、挤入、腾挤时间']],
 'squeezed her hand 是握紧她的手，squeezed through the gap 是挤过缝，squeezed in a meeting 是挤出时间开会。',
 'freshly squeezed juice 鲜榨果汁；squeezed between two people 被挤在两人之间。',
 'squeezed 不必真有液体：人挤地铁、日程挤出空档，都保留有限空间被收紧的画面。',
 ('She squeezed my hand before the interview.','面试前，她握紧了一下我的手。'),('We squeezed through the narrow gap.','我们从狭窄的缝隙挤过去。'),sources=S('squeezed','squeeze'))
W('squeezing','/ˈskwiːzɪŋ/','正在挤压、榨出、挤入；挤出资源、时间',
 '空间正被两边往里收紧，或人正一点点挤过窄处，是 squeezing；挤时间、挤资源也能借这个动作。',
 'squeeze 去 e + 完整 -ing；ee 保留长元音 /iː/，z 仍读 /z/，整个动词再接表示过程的词尾。',SQUEEZE+[['squeeze 去 e + -ing → squeezing','挤压、榨出、挤入的过程']],
 'squeezing oranges 是正榨橙汁，squeezing past someone 是正从某人身边挤过；squeezing in time 是腾出一点时间。',
 'squeezing out toothpaste 挤牙膏；squeezing into a small space 挤进小空间。',
 'squeezing 与 pressing 都可压，squeezing 更常有包住、夹紧、让空间变小的感觉；pressing 可只从一侧按。',
 ('He was squeezing toothpaste onto his brush.','他正往牙刷上挤牙膏。'),('People were squeezing past us in the crowded corridor.','拥挤走廊里，人们正从我们身边挤过。'),sources=S('squeezing','squeeze'))
SQUASH=[['挤压支线：古法语 esquacher 等 → squash','更近拉丁来源有不同分析，亦可能受拟声、近形词影响；压扁、压碎'],['瓜类支线：纳拉甘西特语 askutasquash 的缩借 → squash','植物名称另借；运动、饮料等名词另联系挤压、软物材料']]
W('squashes','英 /ˈskwɒʃɪz/；美 /ˈskwɑːʃɪz/','挤扁、压碎、压制〔第三人称单数〕；瓜类果实、品种〔复数〕',
 '把软东西往下压扁，用 squashes；在菜市场或种植语境，squashes 又可以是各种南瓜、西葫芦等瓜类，来源另分。',
 '动词 squash + -es，/ʃ/ 后读 /ɪz/；瓜类名词可复数为 squashes，也可用不变复数 squash，名称不来自把瓜压扁。',SQUASH+[['squash + -es → squashes','他、她挤扁；多种或多个瓜类果实']],
 'squashes the box flat 是把盒子压扁，grows squashes 是种瓜类；语境决定是动作还是植物。',
 'winter squashes 冬南瓜类；squashes a hope 压灭希望。',
 'squashes 作植物名时不从英语压碎动词来；两词同形，不能用“瓜软所以一压就扁”替代借词历史。',
 ('The heavy bag squashes the soft bread underneath.','重袋子压扁了下面的软面包。'),('The stall sells several varieties of squashes.','摊位卖好几种瓜类。'),sources=S('squashes','squash'))
W('squashing','英 /ˈskwɒʃɪŋ/；美 /ˈskwɑːʃɪŋ/','正在挤扁、压碎、压制；挤压动作',
 '软物正被压扁、人正把东西硬挤进有限空间，叫 squashing。比喻希望、提议被压下，也能保留这种受压感。',
 '挤压动词 squash + 完整 -ing；植物名 squash 不因结尾相同，就把 squashing 当作种瓜的规则动词。',SQUASH+[['挤压动词 squash + -ing → squashing','压扁、硬挤或压制的过程']],
 'squashing a can 是正在压扁罐子，squashing clothes into a bag 是往包里硬塞衣服；squashing hopes 是压灭希望。',
 'squashing the bread 压扁面包；squashing everything together 把一切挤成一团。',
 'squashing 常比 squeezing 更突出压扁、变形或硬塞的结果；挤柠檬汁更常说 squeezing。',
 ('You are squashing the bread under that bag.','你那个袋子把面包压扁了。'),('She was squashing the last few clothes into the suitcase.','她正把最后几件衣服硬塞进箱子。'),sources=S('squashing','squash'))
SPRAY=[['喷滴支线：中古荷兰语 sprayen → spray 动词、相关名词','把液体撒成细滴，喷雾、喷剂等由此发展'],['小枝支线：中古英语 sprai 等 → spray','细枝、花枝；更远来源未定，不从喷雾外形确定推导']]
W('sprays','/spreɪz/','喷洒、喷雾〔第三人称单数〕；喷雾、喷剂、喷流〔复数〕；花枝〔复数〕',
 '把水分成细细的散滴喷出去，用 sprays；桌上的 sprays of flowers 则是几枝带花的枝条，属于另一条来源。',
 '喷洒动词、喷雾名词 spray + -s，读 /z/；小枝名词也有同形复数，近源需按场景分开。',SPRAY+[['spray + -s → sprays','他、她喷洒；多种喷雾或多枝花枝']],
 'sprays water on the leaves 是给叶片喷细水滴，cleaning sprays 是清洁喷剂，sprays of blossom 是几枝花枝。',
 'fine sprays 细喷雾；sprays the surface 喷洒表面。',
 'sprays 的植物枝条义不是“花朵被喷出来”；它有较早小枝材料，和喷液体支线分别记。',
 ('She sprays the leaves with a little water.','她给叶片喷一点水。'),('Two sprays of white flowers lay on the table.','桌上放着两枝白花。'),sources=S('sprays','spray'))
W('sprayed','/spreɪd/','喷洒了、喷雾了；被喷上细滴的',
 '刚才把水、清洁液等分成许多细滴撒开，用 sprayed。它常同时交代喷的液体和被喷的表面。',
 '喷洒动词 spray + 完整 -ed，/eɪ/ 后读 /d/；元音字母加 y 的结尾保留 y，不变成 i。',SPRAY+[['spray + -ed → sprayed','过去把液体喷成细滴']],
 'sprayed water on the plants 是往植物喷水，sprayed the plants with water 则把植物放宾语；两句对应同一个喷洒场景。',
 'sprayed the glass 喷了玻璃；sprayed into the air 喷向空中。',
 'sprayed 常把液体分散成滴，poured 常一股倒出；squirted 又常是一小股细流，不要都译成随意泼。',
 ('He sprayed water over the dusty path.','他往积灰的小路上喷水。'),('She sprayed the glass with a little cleaning fluid.','她往玻璃上喷了一点清洁液。'),sources=S('sprayed','spray'))
SPURT=[['十六世纪 spurt，与较早 spirt 形式相连','喷出材料来源未定，可能日耳曼语、拟声等参与'],['液体短喷与短时活动名词','活动 spurt 另联系表示短时间的 spirt；与液体动词的历史关系可能有关，不简单一线定论']]
W('spurt','英 /spɜːt/；美 /spɜːrt/','突然喷出；一股短喷；一阵猛增、发力',
 '水忽然冲出一小股，是 spurt；速度、增长、精力突然猛来一阵，也可叫 a spurt。抓住短、猛、突然冒出。',
 '接较早 spirt 一系，来源未定；液体喷出与表示短期活动的名词或有关，但不能把记录顺序都写成水流先造全部抽象义。',SPURT,
 'a spurt of water 是一股短促水流，a growth spurt 是一阵快速增长，a final spurt 是最后猛发一把力。',
 'spurt out 突然喷出；a spurt of energy 一阵精力爆发。',
 'spurt 常强调短促一阵，steady growth 则是持续平稳增长；a growth spurt 不等于一直保持同一快速度。',
 ('A spurt of water shot from the pipe.','管子里突然冲出一股水。'),('She put on a final spurt and reached the finish first.','她最后猛地加速，率先冲线。'),sources=S('spurt','spurt'))
W('spurts','英 /spɜːts/；美 /spɜːrts/','突然喷出、猛增〔第三人称单数〕；一阵阵短喷、发力、猛增',
 '水一小股一小股冲出，或活动一阵猛、一阵停，可用 spurts。名词复数常把一次次短爆发并列起来。',
 'spurt + -s，/t/ 后读 /s/；动词三单、短爆发名词复数同形。',SPURT+[['spurt + -s → spurts','它短促喷出；多阵喷流、活动爆发']],
 'water spurts out 是水突然喷出，work in spurts 是一阵一阵地干活，growth spurts 是几个快速增长期。',
 'short spurts 短短几阵；spurts from a hole 从孔里短促喷出。',
 'in spurts 强调不是均匀持续；regularly 只说规律，工作可能规律分段，也可能突然一阵，侧面不同。',
 ('Water spurts from the damaged pipe.','水从破损管道里一股股喷出。'),('I tend to work in short spurts.','我习惯集中干一小阵，再歇一下。'),sources=S('spurts','spurt'))
W('spurted','英 /ˈspɜːtɪd/；美 /ˈspɜːrtɪd/','突然喷出了；猛冲、猛增了一阵',
 '水、气或火花刚才突然冲出一阵，用 spurted；跑步者最后一下突然提速，也能借这个猛冲感。',
 'spurt + 完整 -ed；/t/ 后读 /ɪd/，多一个音节，基础元音不变。',SPURT+[['spurt + -ed → spurted','过去突然喷出、猛冲']],
 'spurted out 是突然喷出，spurted ahead 是猛地向前冲；后面的方向词把短爆发的路径说明白。',
 'spurted from the pipe 从管子里短喷；spurted towards the line 猛冲终点线。',
 'spurted ahead 不只是 went ahead 前进，还多了突然一把劲、短时加速的感觉。',
 ('Water spurted from the hose when he turned the tap.','他一拧水龙头，水就从软管里突然喷出。'),('She spurted ahead in the final few metres.','最后几米，她猛地冲到前面。'),sources=S('spurted','spurt'))
W('spurting','英 /ˈspɜːtɪŋ/；美 /ˈspɜːrtɪŋ/','正在突然喷出、猛冲；短促喷流的',
 '一股股液体、气体正突然冲出，是 spurting；也可描述人、事物一阵猛进的动作。',
 'spurt + 完整 -ing，直接加；末尾 rt 保留，不双写 t。',SPURT+[['spurt + -ing → spurting','短促喷出、猛冲的过程']],
 'water spurting from a pipe 是管口一股股喷水，spurting ahead 是猛冲上前；液体多少不是唯一重点，突然、短促更关键。',
 'spurting out 突然向外喷；a spurting fountain 短促喷涌的喷泉。',
 'spurting 与 squirting 很近；spurting 常突出突然一阵，squirting 常突出从小口挤出细流，实际使用能重合。',
 ('We saw water spurting from the cracked pipe.','我们看见水正从裂开的管子里一股股喷出。'),('She crossed the line after spurting ahead of the others.','她猛冲超过其他人，随后越过终点线。'),sources=S('spurting','spurt'))
GUSH=[['中古英语 gushen → gush','可能英语拟声、低地德语或北欧 gusa 一系影响，具体路径有不同分析'],['液体猛涌 → 话语、赞美感情倾泻','形容过分热情时可能略带评价，不能总当作中性称赞']]
W('gush','/ɡʌʃ/','涌出、奔涌；滔滔不绝地热情说；一股涌流、热情话语',
 '水像闸门打开一样一股涌出，叫 gush；夸赞、感情一股脑往外倒，也能用这个画面。',
 '接中古英语 gushen，具体或拟声、或有低地德语、北欧来源参与；与更远倒、流材料的联系依具体来源分析，不当确定唯一链。',GUSH,
 'water gushes out 是水涌出来，gush about a film 是热情不住地夸电影；a gush of praise 是一大串热烈赞美。',
 'a gush of water 一股涌水；gush over someone 热情过度地夸某人。',
 'gush 写话语时常有热情太满、滔滔不绝的感觉；praise 较中性地说赞扬，不一定带这种评价。',
 ('We heard a gush of water as the gate opened.','闸门打开时，我们听见一股水涌出来。'),('She began to gush about her new camera.','她开始滔滔不绝地夸新相机。'),sources=S('gush','gush'))
W('gushes','/ˈɡʌʃɪz/','涌出、热情地滔滔说〔第三人称单数〕；一股股涌流',
 '水一下涌出许多，或一个人一开口就热情地夸个不停，用 gushes；名词复数是几股涌流或热烈话语。',
 'gush + -es，/ʃ/ 后读 /ɪz/；三单、名词复数同形，两个音节。',GUSH+[['gush + -es → gushes','它涌出；他、她热情滔滔说；多股涌流']],
 'gushes from the pipe 是从管口奔涌，gushes about her trip 是不停热情夸旅行；about 提示话题，不是液体。',
 'gushes out 向外涌；gushes of enthusiasm 一股股热情。',
 'gushes 常比 drips 更有大量、冲出的感觉；一个是涌，一滴一滴落又是另一画面。',
 ('Water gushes from the pipe when the valve opens.','阀门一开，水就从管子里涌出来。'),('He gushes about the hotel whenever anyone mentions the trip.','只要有人提起旅行，他就滔滔不绝地夸那家酒店。'),sources=S('gushes','gush'))
W('gushed','/ɡʌʃt/','涌出了；热情洋溢地说了、夸个不停了',
 '液体刚才猛地涌出来，或人把喜爱、赞美一股脑说出来，用 gushed。后者可热情，也可显得过头。',
 'gush + 完整 -ed，/ʃ/ 后读 /t/；仍是一个音节。',GUSH+[['gush + -ed → gushed','过去奔涌；感情、话语热烈倾泻']],
 'gushed out of the pipe 是从管子里涌出，gushed about the meal 是热情地夸饭菜；可以接具体赞叹。',
 'gushed with enthusiasm 热情地滔滔说；gushed into the channel 涌入水渠。',
 'gushed 作为说话标签比 said 更带感情、热度和一泻而出的感觉；不一定代表叙述者完全赞同这种热情。',
 ('Water gushed out when we opened the valve.','我们打开阀门，水就涌出来。'),('“It was absolutely wonderful,” she gushed.','“真是太棒了。”她热情洋溢地说。'),sources=S('gushed','gush'))
W('gushing','/ˈɡʌʃɪŋ/','正在涌出的；热情洋溢、赞美过头的；奔涌',
 '水正猛烈流出，是 gushing；形容推荐、赞美时，像感情倒得满满的，可能让人觉得太热情。',
 'gush + 完整 -ing，直接加；分词可写流动，形容词可评价话语、举止的热情程度。',GUSH+[['gush + -ing → gushing','涌流过程；情感过满、赞美热烈的状态']],
 'gushing water 是涌水，a gushing review 是热烈得甚至有点过头的好评；两者抓的都是一股脑倾泻。',
 'a gushing stream 奔涌的小溪；gushing praise 热情过满的赞美。',
 'gushing praise 不必译成虚假赞美；它先说热情的程度，真不真诚仍需别的证据。',
 ('Water was gushing into the empty channel.','水正奔涌着流进空水渠。'),('The film received a gushing review in the magazine.','杂志给了这部电影一篇热情洋溢、甚至有点过头的好评。'),sources=S('gushing','gush'))
DRIBBLE=[['旧动词 drib，属 drip 一系 → dribble','加旧反复动作材料，少量一点点流、落'],['少量连续动作 → 运动控球','足球连续轻触推进；篮球连续拍弹控球，技术动作不同但都非一次大力击出']]
W('dribbles','/ˈdrɪbəlz/','少量流滴、流口水、运球〔第三人称单数〕；细流、运球动作〔复数〕',
 '水一点点沿边流，或口水慢慢流，用 dribbles；球不是一下踢飞，而是靠连续小动作带着走，也叫 dribbles。',
 'dribble + -s，保留 e，/l/ 后读 /z/。基础 dribble 联系旧 drib、drip 的少量流滴材料与反复动作尾。',DRIBBLE+[['dribble + -s → dribbles','它少量流；他、她控球；多段细流、运球']],
 'water dribbles down 是水一点点流下，dribbles the ball 是控球、运球；篮球与足球由运动背景区分具体动作。',
 'dribbles past a defender 带球过防守者；small dribbles of water 几小股缓流水。',
 'dribbles 在球场不是球漏水，借的是连续、小幅控制的动作；kick the ball 可以是一脚把球送远。',
 ('Water dribbles from the loose tap.','松动的水龙头里一点点流着水。'),('She dribbles past the defender and passes the ball.','她带球过了防守者，把球传出去。'),sources=S('dribbles','dribble'))
W('dribbled','/ˈdrɪbəld/','一点点流、滴了；流口水了；运球、带球了',
 '液体刚才细细沿边流下，或球员靠连续小动作把球带过一段，用 dribbled。不要在运动句子里仍只想口水。',
 'dribble 去 e + 完整 -ed，/l/ 后读 /d/；基础词已有 bb 保留，不再多添 b。',DRIBBLE+[['dribble 去 e + -ed → dribbled','过去少量流滴、流口水或运球']],
 'dribbled down his chin 是沿下巴流下来，dribbled across the court 是运球穿过球场；同形动词借动作扩义。',
 'dribbled oil into the pan 往锅里慢慢滴油；dribbled past two players 带球过两人。',
 'dribbled 常是连续小动作控着球走，shot 常是把球射、投向得分目标；别只译成笼统的打球。',
 ('A little sauce dribbled down the side of the bottle.','一点酱汁沿瓶身慢慢流下来。'),('She dribbled the ball across the court.','她运球穿过球场。'),sources=S('dribbled','dribble'))
W('dribbling','/ˈdrɪblɪŋ/','正在少量流、滴、流口水；运球、带球及其技术',
 '液体正一点点流，是 dribbling；运动里是不断轻触、拍弹，边控球边推进，像把大动作分成连续小动作。',
 'dribble 去 e + 完整 -ing，常读 /ˈdrɪblɪŋ/；可以是进行分词，也可以把运球当一项技术来谈。',DRIBBLE+[['dribble 去 e + -ing → dribbling','少量流滴过程；运球活动、技术']],
 'dribbling skills 是运球技术，practise dribbling 是练运球；water dribbling down a wall 则仍是细水往下流。',
 'dribbling past opponents 带球过人；keep dribbling 保持运球。',
 'dribbling 是控制球，不等于 scoring 得分；运球可以为传球、摆脱防守做准备，未必马上射、投。',
 ('The coach made us practise dribbling with both hands.','教练让我们练习左右手运球。'),('Water was dribbling down the tiled wall.','水正沿瓷砖墙一点点流下来。'),sources=S('dribbling','dribble'))
DRIP=[['古英语 drypan、dryppan → 中古英语 drippen → drip','让液体一滴一滴落下，与 drop、droop 等词族可比较'],['动词 → 液滴、滴注名词及比喻','dripping 可说滴湿；还可指烤肉滴出的脂油，按用途分支']]
W('drips','/drɪps/','一滴滴落、漏滴〔第三人称单数〕；液滴、漏滴声；输液滴注〔复数〕',
 '水龙头“滴、滴”地掉水，叫 drips；名词可以把几滴水、几声滴落说出来，设备场景还有滴注用法。',
 'drip + -s，/p/ 后读 /s/；动词三单、名词复数同形，基础承古英语滴落材料。',DRIP+[['drip + -s → drips','它一滴滴落；多滴液体或相关装置']],
 'the tap drips 是水龙头漏滴，drips of water 是水滴；medical drips 的装置命名联系一滴滴输入，不是新古根。',
 'drips onto the floor 滴到地上；steady drips 稳稳的一滴滴落。',
 'drips 更突出一滴一滴分开，dribbles 更容易是少量细细流；实际少量出水时两个画面可能重合。',
 ('The tap drips all night.','水龙头整夜滴水。'),('Cold drips of water fell from the cave roof.','冰凉的水滴从洞顶落下。'),sources=S('drips','drip'))
W('dripped','/drɪpt/','一滴滴落下了、滴出了；充满某种意味',
 '水刚才一滴滴落下，用 dripped；声音“滴着讽刺”则像某种态度浓得都往外落，是比喻。',
 'drip 双写 p + 完整 -ed → dripped；/p/ 后读 /t/，短元音重读单音节按规则双写。',DRIP+[['drip 双写 p + -ed → dripped','过去滴落；态度浓得外露的比喻']],
 'dripped from the roof 是从屋顶滴下，dripped onto the floor 是滴到地上；dripped with sarcasm 是充满讽刺。',
 'dripped slowly 慢慢滴；dripped off his coat 从外套上滴下。',
 'dripped with sarcasm 不是讽刺真的液化，是把很浓、很明显的态度写成往外滴；与普通 said 多了一层评价。',
 ('Water dripped from the edge of his coat.','水从他的衣服边一滴滴落下。'),('Her voice dripped with sarcasm.','她说话的声音满是讽刺。'),sources=S('dripped','drip'))
W('dripping','/ˈdrɪpɪŋ/','正在滴落；湿得滴水的；满是某种意味的；烤肉滴出的脂油',
 '衣服湿到往下掉水，是 dripping；dripping with sarcasm 是讽刺浓得藏不住。烹饪里 dripping 还指烤肉滴下的脂油。',
 'drip 双写 p + 完整 -ing；活动、状态分词之外，烹饪名词保留“滴出来的东西”这一发展，不是所有 dripping 都是进行时。',DRIP+[['drip 双写 p + -ing → dripping','滴落过程、滴湿状态；滴出的脂油名词']],
 'dripping wet 是湿得直滴水，dripping with confidence 可夸张说满满自信，beef dripping 是牛肉烤出的脂油。',
 'a dripping coat 滴水的外套；dripping with sarcasm 满是讽刺。',
 'dripping 比 damp 的湿更强，常已湿得滴水；菜谱里的 dripping 则要认成油脂名词。',
 ('We came home dripping wet from the rain.','我们淋雨回家，浑身湿得直滴水。'),('The potatoes were roasted in beef dripping.','土豆用烤牛肉滴出的脂油烤熟。'),sources=S('dripping','drip'))
DROOL=[['较早 drivel 一系 → 方言 drule、drool','drool 大概是 drivel 的方言变体或缩合，流唾液'],['动词 → 唾液名词；对想要之物的比喻','drool over 像馋得流口水，表示非常喜欢、眼馋，不要求真的流唾液']]
W('drool','/druːl/','流口水；口水；〔drool over〕眼馋、垂涎、十分喜欢',
 '口水慢慢从嘴里流出来，叫 drool；看见好吃的、新车或漂亮设计眼馋，也可说 drool over，像想要得流口水。',
 '大概由 drivel 的方言变体、缩合形式发展，早期拼 drule；名词后来可说唾液，现代比喻延伸到特别想要的东西。',DROOL,
 'drool on the pillow 是睡得口水流到枕头上，drool over a cake 是馋蛋糕；名词 dog drool 是狗的口水。',
 'a little drool 一点口水；drool over the photos 看照片眼馋。',
 'drool over 不等于每次真的流口水；对旅行照片、设备、衣服也能用，是随意、形象的说法。',
 ('The dog left a little drool on the floor.','狗在地板上留下了一点口水。'),('Try not to drool over the cake before the guests arrive.','客人来之前，尽量别对着蛋糕馋得直流口水。'),sources=S('drool','drool'))
W('drools','/druːlz/','流口水〔第三人称单数〕；〔drools over〕眼馋、十分喜欢',
 '说狗看见食物就口水往下流，用 drools；人对想要的东西赞叹、眼馋，也可以借这个动作。',
 'drool + -s，/l/ 后读 /z/；oo 保留 /uː/，现代三单不改元音。',DROOL+[['drool + -s → drools','他、她或它流口水；眼馋某物']],
 'drools over the food 是馋食物，drools over new gadgets 是特别眼馋新设备；后者通常是比喻。',
 'drools on the blanket 口水流到毯子上；drools over the catalogue 看目录眼馋。',
 'drools 描写流口水，droops 则是垂下、无精打采；外形只差一个辅音，动作不是同一回事。',
 ('The dog drools whenever it smells roast chicken.','狗每次闻到烤鸡味就流口水。'),('He drools over the latest camera models.','他对最新款相机特别眼馋。'),sources=S('drools','drool'))
W('drooled','/druːld/','流口水了；眼馋、垂涎了',
 '刚才口水流出来，或看着特别想要的东西心痒痒，用 drooled。后面的 over 常提示对什么眼馋。',
 'drool + 完整 -ed，/l/ 后读 /d/；oo 是长元音，直接加，不双写 l。',DROOL+[['drool + -ed → drooled','过去流唾液；对某物十分想要']],
 'drooled on the pillow 是口水流在枕头上，drooled over the menu 是看菜单馋得不行；比喻也能用在物品、景色上。',
 'drooled in his sleep 睡觉流口水；drooled over the display 看展示品眼馋。',
 'drooled over 比 liked 更外露、强烈，还带一点玩笑、自嘲；不是正式报告里中性的喜欢。',
 ('He had drooled on the pillow while sleeping.','他睡觉时把口水流到了枕头上。'),('We drooled over the pastries in the bakery window.','我们看着面包店橱窗里的糕点，馋得不行。'),sources=S('drooled','drool'))
W('drooling','/ˈdruːlɪŋ/','正在流口水；对某物眼馋、垂涎',
 '口水正往外流，是 drooling；人盯着好吃的、好看的、很想买的东西，也能借来写眼馋得不行。',
 'drool + 完整 -ing，直接加；oo 长元音保留，不双写 l。',DROOL+[['drool + -ing → drooling','流口水过程；强烈想要的比喻']],
 'a drooling dog 是流口水的狗，drooling over a dessert 是对甜点垂涎；看到照片也可以比喻这么说。',
 'drooling over the menu 看菜单馋；drooling over a sports car 对跑车眼馋。',
 'drooling 常比 admiring 更随意、更强调想要；欣赏一件作品不一定想占有它，drool over 常带这层欲望感。',
 ('The dog was drooling as we prepared its dinner.','我们给狗准备晚饭时，它正在流口水。'),('We were drooling over the desserts on the menu.','我们看着菜单上的甜点，馋得不行。'),sources=S('drooling','drool'))
OOZE=[['动词支线：古英语 wos 汁液及相关发流材料 → 中古英语 wosen → ooze','水分、汁液慢慢渗出；现代拼写后来固定'],['软泥名词支线：古英语 wase → ooze','软湿泥、淤泥；与动词有更远湿润材料可比较，近源分别说明']]
W('ooze','/uːz/','慢慢渗出、流出；满满显出某种特点；软泥、淤泥',
 '融化的奶酪、蜂蜜或泥浆慢慢往外挤流，叫 ooze。感觉黏、慢，不像水突然喷一大股；也能说人举手投足满是自信。',
 '渗流动词接中古英语 wosen，联系古英语 wos 汁液材料；软泥名词承古英语 wase。别把所有名词都写成现代动词直接转来。',OOZE,
 'cheese oozes out 是奶酪缓缓流出来，ooze confidence 是处处显出自信；thick ooze 是稠软淤泥。',
 'ooze from a crack 从缝里渗出；ooze charm 满是魅力。',
 'ooze 常比 gush 慢、黏、持续；比喻 ooze charm 时并不嫌人黏糊，而是特征浓得自然流露。',
 ('Warm cheese began to ooze from the sandwich.','温热的奶酪开始从三明治里慢慢流出来。'),('Our boots sank into the black ooze.','我们的靴子陷进了黑色淤泥。'),('The small hotel seems to ooze charm.','这家小酒店似乎处处散发着魅力。'),sources=S('ooze','ooze'))
W('oozes','/ˈuːzɪz/','缓缓渗出、流出〔第三人称单数〕；满满显出某种特点',
 '蜂蜜、奶酪沿缝慢慢出来，用 oozes；某个人一举一动都显出自信、魅力，也能这样写。',
 'ooze + -s，保留 e，/z/ 后读 /ɪz/，多一个音节；不是所有加 s 的词都只在末尾添 /s/。',OOZE+[['ooze + -s → oozes','它缓慢渗流；他、她处处显出特质']],
 'oozes from the filling 是从馅里慢慢流出，oozes confidence 是满是自信；物理、比喻两义可由对象分清。',
 'oozes out 慢慢流出；oozes warmth 自然透着温暖。',
 'oozes confidence 强调特质外露、明显，has confidence 只是说有自信；前者更形象。',
 ('Honey oozes slowly from the spoon.','蜂蜜从勺上慢慢流下。'),('She oozes confidence when she speaks on stage.','她站在台上说话时，满满都是自信。'),sources=S('oozes','ooze'))
W('oozed','/uːzd/','缓缓渗出、流出了；满满流露了某种特点',
 '稠稠的东西刚才从缝隙慢慢出来，叫 oozed；叙述人、地方自然散发气质，也可以借这种浓浓流露的感觉。',
 'ooze 去 e + 完整 -ed，/z/ 后读 /d/；仍是一个音节，不因字母 e 而读 /ɪd/。',OOZE+[['ooze 去 e + -ed → oozed','过去慢慢渗流；明显流露特质']],
 'oozed from the pie 是从馅饼里慢慢流出，oozed charm 是散发魅力；不是一定有看得见的液体。',
 'oozed through a gap 从缝中渗出；oozed confidence 处处显自信。',
 'oozed 的比喻用法可以形容吸引人的特点，也可以形容傲慢等负面特点；褒贬由后面词决定。',
 ('Melted cheese oozed from the edge of the toast.','融化的奶酪从吐司边缓缓流出。'),('The old café oozed charm.','那家老咖啡馆处处散发魅力。'),sources=S('oozed','ooze'))
W('oozing','/ˈuːzɪŋ/','正在缓缓渗出、流出；满满流露某种特点的',
 '黏稠汁液正慢慢从里面出来，是 oozing；形容人自信、魅力外露，也可以像特质正不断往外流。',
 'ooze 去 e + 完整 -ing，oo 的 /uː/ 与 z 的 /z/ 保留；词尾附在完整的渗流动词后。',OOZE+[['ooze 去 e + -ing → oozing','缓慢流出过程；特质自然外露']],
 'oozing cheese 是缓缓流出的奶酪，oozing confidence 是满满自信；可作进行动作，也可修饰一种状态。',
 'oozing from the filling 从馅里渗出；oozing with charm 魅力满溢。',
 'oozing 常有缓慢、浓稠感；spurting 常更突然、短促。形容性格、气质时，只借其不断外露的画面。',
 ('The pastry was warm, with chocolate oozing from the centre.','酥点热乎乎的，巧克力从中间慢慢流出。'),('He walked onto the stage, oozing confidence.','他走上舞台，满满都是自信。'),sources=S('oozing','ooze'))
def extend_lessons():
 extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_zff',ROOTS,WORDS)
 extend_lessons()
