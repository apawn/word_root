"""Pawn and hock, stakes and bets: keep unrelated sources separate."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
def S(word,base):
 return ['https://en.wiktionary.org/wiki/'+word+'#English','https://www.etymonline.com/word/'+base]
EXISTING_ROOT_ADDITIONS={
 'A1760':dict(words='hock hocks hocked hocking pawn pawns pawned pawning'.split(),label='hock 与 pawn 的典当线：同义不等于同源',note='hock 债务、典当线接荷兰 hok 围栏、监禁等材料；动物后腿关节、葡萄酒同形名各另源。典当 pawn 接法语押物词，不能拿棋兵的拉丁 ped- 脚解释。'),
 'B4515':dict(words='pawnbroker pawnbrokers'.split(),label='pawnbrokers：收押物借款的经营者',note='pawn 押物 + broker，复数加 -s；这是 pawn 的押物线，与棋兵线不同。'),
 'B3267':dict(words='pawnshop pawnshops'.split(),label='pawnshops：典当业务的店',note='pawn 押物 + shop 构成店名，复数加 -s；不把 shop 的商店义又推成棋盘。'),
 'B3009':dict(words='wager wagered wagering'.split(),label='wager：拿价值押结果',note='wager 名词经法语质押、保证材料进入英语，动词由名词转用；不是现代 wage 工资加人物 -er。'),
 'B3824':dict(words='stake staked'.split(),label='staked：用桩固定与拿价值押结果',note='木桩 stake 接古英语 staca；赌注、利益 stake 的更早联系未定，不能把赌注挂桩上的故事当证据。现代 staked 可写支撑、标定，也可写押上名声等。'),
 'B3309':dict(words='gamble gambles gambled gambling gambler gamblers'.split(),label='gamble：由玩乐材料到押上价值冒险',note='gamble 接 game 旧玩乐词族的相应动词，具体近路有分析差别；b 的进入可能受 gambol 影响，但两者来源不同。现代加词尾认形，不用 game 加 -ble 硬拼。'),
 'B2823':dict(words='bet bets bettor bettors'.split(),label='bets 与 bettors：赌注、下注者及确信口语',note='bet 远源未定；bets 为复数或动词三单，bettors 是 bet 双写 t 加 -or 人物词的复数。I bet 表确信时未必真拿钱下注。'),
 'A1698':dict(words='bookie bookies'.split(),label='bookies：bookmaker 的口语短称',note='bookie 是 bookmaker 博彩用法的缩短形式并带 -ie，bookie 以 -ie 结尾，直接加 -s 写 bookies。'),
 'B2414':dict(words='bookmaker bookmakers'.split(),label='bookmakers：制书旧义与经营投注的常见义',note='book + maker；制作书籍义较早，投注业务义较晚，联系记录赌注的 book。现代 bookmakers 常指经营接收投注的一方，不是普通下注者的总称。'),
}
HOCK=[['荷兰 hok 围栏、监禁等材料 → in hock','相关俚语发展到欠债、典当状态'],['hock 名词 → 典当动词','动物后腿关节接古英语材料；葡萄酒名接德语地名，均另源']]
PAWN=[['典当线：法语 pan、pant 押物，可能接日耳曼材料','更远来源未定，不能硬定来自布料'],['押物名词 → pawn 典当动词','另源棋兵线接法语步兵、拉丁 ped- 脚，不解释典当']]
WAGER=[['法语 wageure、wagiere 等 → wager 名词','质押、保证，也用于赌注'],['wager 名词 → wager 动词','拿钱、物押一个不确定结果']]
STAKE=[['古英语 staca → stake 木桩 → 固定、支撑、标定','用桩钉住、圈出某处'],['stake 赌注、利益的具体远源联系未定','拿价值押结果，不能把赌注挂桩的传说当确定事实']]
GAMBLE=[['古英语 gamen 玩乐与相关动词 → 较早 gammlen、gamel 等材料','与 game 家族相关，具体近路不止一种分析'],['gamble → 拿价值冒险；现代屈折、人物词','字母 b 可能受 gambol 影响，但不能把两词认作同源']]
BET=[['十六世纪 bet 名词、动词等俚语材料','押上价值赌结果，远源未定'],['现代赌注、下注与 I bet 等口语','确信、猜测的语气未必对应真实下注']]
BOOK=[['book + maker → bookmaker','较早可说制作书籍的人'],['记录投注的 book、make a book 等 → 博彩经营者；bookie 短称','bookmakers、bookies 是各自人物名词的复数']]
W('hock','英 /hɒk/；美 /hɑk/','典当〔口语〕；〔in hock〕欠债、处于典当状态；后腿关节〔另源〕',
 '把手表押在店里，先借一笔钱，口语可说 hock the watch；in hock 则像被债务拴住。菜谱里的 ham hock 却是猪肘、腿节，另走一条词源。',
 '债务、典当线由 in hock 等用法接荷兰 hok 围栏、监禁材料，再形成典当动词。动物后腿关节接古英语脚跟筋材料；酒名还另接德国地名，不能合讲。',HOCK,
 'hock a watch 典当手表；be in hock 欠债、抵押着；a ham hock 猪肘、猪腿节。',
 'deep in hock 欠债很深；get something out of hock 把典当物赎回。',
 'hock 典当较口语，pawn 同样常见且更中性；ham hock 不拿债务解释，先看食物语境。',
 ('In the story, he has to hock his watch to pay the rent.','故事里，他不得不典当手表来付房租。'),('The soup was made with beans and a ham hock.','汤是用豆子和猪肘做的。'),sources=S('hock','hock'))
W('hocks','英 /hɒks/；美 /hɑks/','典当〔第三人称单数〕；动物后腿关节、猪肘等〔复数〕',
 '小说人物一缺钱就把旧物拿去典当，动词可用 hocks；菜谱里几块猪腿节，也写 hocks，但属于另一来源的名词复数。',
 'hock + -s，/k/ 后读 /s/；同形词尾既可接典当动词，也可接后腿关节、食材名词，两条来源分开。',HOCK+[['hock + -s → hocks','他典当；或多个后腿关节、腿节食材']],
 'hocks his belongings 典当财物；ham hocks 猪肘、猪腿节。',
 'smoked hocks 烟熏猪肘；hocks a watch。',
 'hocks 是食物还是动作，靠句子中的 ham、smoked 或动作宾语判断；不是同一个古词从身体部位变成借钱。',
 ('The character hocks his belongings whenever money runs short.','那个角色一缺钱，就典当自己的东西。'),('Smoked ham hocks gave the soup a rich flavour.','烟熏猪肘给汤添了浓郁风味。'),sources=S('hocks','hock'))
W('hocked','英 /hɒkt/；美 /hɑkt/','典当了；被押在典当店了',
 '东西先交给店里作押物，再拿到钱，过去的这个动作口语可写 hocked。物品仍可能日后赎回，不等于普通卖断。',
 'hock 典当动词 + 完整 -ed，/k/ 后读 /t/；当前取荷兰 hok 相关债务材料这一支。',HOCK+[['hock + -ed → hocked','过去把东西典当，或已被典当']],
 'hocked his guitar 典当吉他；hocked jewellery 典当珠宝。',
 'had hocked the watch；was hocked for cash。',
 'hocked 典当与 sold 卖出不同：前者以押物借钱，可能通过还款赎回；具体故事有没有赎回，要看后文。',
 ('He hocked his guitar to cover the urgent expense.','他典当了吉他，应付那笔急需支出。'),('She later bought back the watch she had hocked.','她后来赎回了自己典当过的手表。'),sources=S('hocked','hock'))
W('hocking','英 /ˈhɒkɪŋ/；美 /ˈhɑkɪŋ/','正在典当；典当物品的活动',
 '把旧物送去作押物换取借款，这个过程口语可叫 hocking。放回故事里看，它写人物眼前的筹钱动作。',
 'hock + -ing；这里接典当动词，而非动物关节名词。现代过程形式清楚，基础词的同形来源仍应区分。',HOCK+[['hock + -ing → hocking','典当的过程、活动']],
 'hocking jewellery 典当珠宝；hocking a watch 典当手表。',
 'hocking possessions 典当财物；consider hocking something。',
 'hocking 与 pawning 可指同一类典当动作；两词是同义关系，不表示必然同源。',
 ('The novel describes him hocking his last valuable possession.','小说描写他典当最后一件值钱物品。'),('She considered hocking the necklace but decided to keep it.','她考虑过典当项链，最后决定留下。'),sources=S('hocking','hock'))
W('pawns','英 /pɔːnz/；美 /pɔnz/','棋兵、被利用的人〔复数〕；典当〔第三人称单数，另源〕',
 '棋盘前排的一排小兵是 pawns；人被大人物当工具摆布，也可叫 pawns。小说里有人 pawns a watch，则是典当手表，另一个词源。',
 'pawn + -s，/n/ 后读 /z/。棋兵线来自法语步兵词、拉丁 ped- 脚；典当线接法语押物词，不能把两种意思都用脚解释。',PAWN+[['另一棋兵线：拉丁步行者、步兵材料 → pawn → pawns','多个兵、被摆布者；典当三单同形但另源']],
 'chess pawns 棋兵；political pawns 被当作政治棋子的人；pawns his watch 典当手表。',
 'use people as pawns 把人当棋子利用；a row of pawns。',
 'pawns 作被利用者时是棋兵比喻；pawns valuables 是典当动作，不能把押物也说成在下棋。',
 ('The pawns stood in a row at the start of the game.','开局时，兵排成一行。'),('The workers did not want to be used as pawns in the dispute.','工人们不想在争端中被当作棋子利用。'),sources=S('pawns','pawn'))
W('pawned','英 /pɔːnd/；美 /pɔnd/','典当了；被用作押物了',
 '把戒指留在店里作押物，拿一笔借款，过去做了这件事，就是 pawned。它对应押物这一支，不是棋兵的动作。',
 'pawn 典当动词 + 完整 -ed，/n/ 后读 /d/；动词由押物名词转来，经法语押物词接更早日耳曼材料，远源未定。',PAWN+[['pawn + -ed → pawned','过去典当或已被典当']],
 'pawned a watch 典当手表；pawned jewellery 典当珠宝。',
 'had pawned the ring；pawned for a loan。',
 'pawned 是交物作押借钱，sold 是卖出；典当物有赎回这一可能，不能把两种交易一概混译。',
 ('The musician pawned his guitar to pay the rent.','那位音乐家典当吉他来付房租。'),('She returned to reclaim the ring she had pawned.','她回去赎回了自己典当过的戒指。'),sources=S('pawned','pawn'))
W('pawning','英 /ˈpɔːnɪŋ/；美 /ˈpɔnɪŋ/','正在典当；典当活动',
 '先留下值钱物，拿到暂时用的钱，这种把物品作为借款押物的活动，就是 pawning。它不是简单把所有权直接卖给下一位买家。',
 'pawn + -ing，当前用典当动词一支；棋兵名词虽同形，并非这项借款活动的来历。',PAWN+[['pawn + -ing → pawning','以物作押借款的过程、活动']],
 'pawning possessions 典当财物；pawning jewellery 典当珠宝。',
 'consider pawning something；a story about pawning a watch。',
 'pawning 和 hocking 在典当语境可相近，hocking 较口语；共同意思不要求历史来源相同。',
 ('The film shows him pawning his watch before leaving town.','电影里，他离开小镇前典当了手表。'),('She thought about pawning the camera but changed her mind.','她想过典当相机，后来改了主意。'),sources=S('pawning','pawn'))
W('pawnbrokers','英 /ˈpɔːnˌbrəʊkəz/；美 /ˈpɔnˌbroʊkɚz/','典当商〔复数〕',
 '收下手表、首饰等押物，按押物借出钱的经营者，叫 pawnbrokers。这里的 pawn 是押物，broker 是经营、经手这一类事务的人。',
 'pawnbroker + -s，读 /z/；内层 pawn 押物 + broker。pawn 的棋兵来源不参与这个复合词。',PAWN+[['pawn + broker → pawnbroker → pawnbrokers','经手押物借贷业务者及其复数']],
 'local pawnbrokers 当地典当商；licensed pawnbrokers 有许可的典当商。',
 'pawnbrokers and jewellers；visit pawnbrokers。',
 'pawnbrokers 是经营者，pawnshops 是经营场所；一个说人或机构，一个说店。',
 ('The street had several pawnbrokers and jewellery shops.','那条街上有几家典当商和珠宝店。'),('The documentary interviewed local pawnbrokers.','纪录片采访了当地典当商。'),sources=S('pawnbrokers','pawnbroker'))
W('pawnshops','英 /ˈpɔːnʃɒps/；美 /ˈpɔnʃɑps/','典当店、当铺〔复数〕',
 '街上几家店收押物、办理典当，人们也可能在里面买到未被赎回的物品，这些店叫 pawnshops。',
 'pawnshop + -s，/p/ 后读 /s/；内层 pawn 押物 + shop 店，与棋兵的 pawn 不同源。',PAWN+[['pawn + shop → pawnshop → pawnshops','办理典当业务的场所及其复数']],
 'local pawnshops 当地当铺；pawnshops selling used instruments 卖二手乐器的当铺。',
 'visit pawnshops；a row of pawnshops。',
 'pawnshops 的主要词义联系押物借款业务，second-hand shops 是二手商店；两者可能都卖旧货，但经营模式不必一样。',
 ('He searched local pawnshops for a second-hand guitar.','他在当地当铺找二手吉他。'),('Two pawnshops stood near the old railway station.','旧火车站附近有两家当铺。'),sources=S('pawnshops','pawnshop'))
W('wagered','英 /ˈweɪdʒəd/；美 /ˈweɪdʒɚd/','押了赌注；拿某物押某个结果了',
 '双方说好，猜错的人请咖啡，就可以说 wagered a cup of coffee。押的可以是钱，也可以是别的有价值的东西。',
 'wager + 完整 -ed，读 /d/；wager 动词来自较早的赌注、质押名词，名词经法语保证、押物材料而来。',WAGER+[['wager + -ed → wagered','过去拿价值押某结果']],
 'wagered money on a race 把钱押在比赛上；wagered that 打赌认为。',
 'wagered a small sum；wagered a cup of coffee。',
 'wagered 与 bet 过去式可近义，wagered 语气通常更正式；不是 wage 工资的过去式 waged。',
 ('They wagered a cup of coffee on who would arrive first.','他们打赌谁先到，输的人请一杯咖啡。'),('He wagered that the old car would start on the first try.','他打赌那辆旧车一次就能发动。'),sources=S('wagered','wager'))
W('wagering','英 /ˈweɪdʒərɪŋ/；美 /ˈweɪdʒərɪŋ/','正在打赌；下注、投注活动',
 '把有价值的东西押在尚未确定的结果上，这项活动叫 wagering。新闻或正式文章里，这个词比随口说 betting 更常显得书面。',
 'wager + -ing；动词由名词转用后加现代过程尾，英式在元音开头后缀前读出 r。',WAGER+[['wager + -ing → wagering','拿价值押结果的过程、活动']],
 'sports wagering 体育投注；wagering money 押钱打赌。',
 'a history of wagering；wagering on the outcome 押某结果。',
 'wagering 一般比 betting 正式；I bet 在日常还可纯表确信，wagering 更常把注意力放在真实押注活动。',
 ('The museum display described the history of wagering on horse races.','博物馆展板介绍了赛马投注的历史。'),('The article examined changes in online wagering.','文章考察了网上投注的变化。'),sources=S('wagering','wager'))
W('staked','/steɪkt/','用桩固定、支撑了；标定、主张了；押上、拿来冒险了',
 '给番茄苗插支撑桩，是 staked the plants；拿自己的名声去保证一件事，是 staked his reputation。两种现代画面好记，但更远历史不全连得上。',
 'stake 去 e 加完整 -ed，/k/ 后读 /t/。木桩线接古英语 staca；赌注、拿利益冒险这一线与木桩怎么相接未定，不把挂赌注在桩上的故事当事实。',STAKE+[['stake + -ed → staked','过去支撑、标定、主张，或押上某种价值']],
 'staked the plants 用桩撑苗；staked a claim 主张权利、划定位置；staked his reputation 押上声誉。',
 'staked out the area 标定区域，也可写监视地点；staked everything on 把一切押在。',
 'staked his reputation on 说拿声誉作保证，guessed 只是猜；前者多了自己会承担名誉损失的意味。',
 ('We staked the young trees to keep them upright.','我们用桩把幼树撑直。'),('She staked her reputation on the accuracy of the report.','她以自己的声誉保证报告准确。'),sources=S('staked','stake'))
W('gambles','/ˈɡæmbəlz/','赌博、冒险押结果〔第三人称单数〕；冒险举动〔复数〕',
 '他用不确定的结果作赌注，是 he gambles；一次可能成、也可能损失很大的决定，则是 a gamble，多个就是 gambles。',
 'gamble + -s，/l/ 后读 /z/；动词三单与名词复数同形，基础词接 game 的旧玩乐材料，具体近路有分析差别。',GAMBLE+[['gamble + -s → gambles','他或它拿价值冒险；多次冒险举动']],
 'gambles on the outcome 押结果；risky gambles 风险大的冒险举动。',
 'gambles with his reputation 拿声誉冒险；take gambles。',
 'gambles 不必都发生在赌场；a risky career move 也可能被说成 a gamble，重点是押上重要东西、结果不确定。',
 ('The character gambles away his savings in the novel.','小说里，那个角色把积蓄都赌光了。'),('The film explores the gambles people take when changing careers.','电影探讨了人们转行时做出的冒险决定。'),sources=S('gambles','gamble'))
W('gambled','/ˈɡæmbəld/','赌博、冒险押结果了',
 '没预订住宿，赌到时候会有空房，就是 gambled on finding a room。它说过去把希望押在一个不保证会发生的结果上。',
 'gamble 去 e 加完整 -ed，/l/ 后读 /d/；原词干有 /əl/，-ed 不另加 /ɪd/ 音节。',GAMBLE+[['gamble + -ed → gambled','过去赌博，或押某不确定结果作决定']],
 'gambled on 依赖、押某不确定情况；gambled away 赌掉。',
 'gambled that 打赌、冒险认为；gambled with his future 拿未来冒险。',
 'gambled on 说明知道结果没保证却押上去，counted on 常是指望、依靠；风险感和确信程度不同。',
 ('We gambled on finding a room without booking ahead.','我们没提前订房，赌到时能找到住处。'),('He gambled that the weather would stay dry.','他冒险认定天气会一直干爽。'),sources=S('gambled','gamble'))
W('gambling','/ˈɡæmblɪŋ/','赌博活动；正在赌博、拿重要东西冒险',
 '拿钱或其他价值押输赢，这项活动叫 gambling；gambling with someone’s future 则把别人的未来放在风险里，是比喻用法。',
 'gamble 去 e 加 -ing，常读 /ˈɡæmblɪŋ/。gamble 由 game 旧玩乐词族相应动词发展，不能按现代 game 加一个 -ble 简单拼出。',GAMBLE+[['gamble + -ing → gambling','赌博活动，或拿某种价值冒险的过程']],
 'gambling losses 赌博损失；gambling on the result 押结果；gambling with lives 拿生命冒险。',
 'a history of gambling；gambling away money 赌掉钱。',
 'gambling 是押价值赌输赢，gaming 可泛说玩电子游戏等；语境不同，不能把所有 gaming 都译成赌博。',
 ('The novel describes the effect of gambling on the family.','小说描写赌博对这个家庭的影响。'),('Critics said the decision was gambling with the town’s future.','批评者说，这个决定是在拿小镇的未来冒险。'),sources=S('gambling','gamble'))
W('gamblers','英 /ˈɡæmbləz/；美 /ˈɡæmblɚz/','赌博者；爱拿重要东西冒险的人〔复数〕',
 '有人把钱押在牌、赛果上，是 gamblers；文章也能这样形容赌上一切求成功的冒险者，未必真在牌桌边。',
 'gambler + -s，读 /z/；内层 gamble 去 e 加 -er 人物尾。现代角色名既可取具体赌博，也可取冒险比喻。',GAMBLE+[['gamble + -er → gambler → gamblers','进行赌博、冒险押结果的人及其复数']],
 'professional gamblers 职业赌博者；compulsive gamblers 有强迫性赌博行为的人。',
 'a group of gamblers；gamblers in the story。',
 'gamblers 是押风险的一方，bookmakers 常是经营接收投注的一方；不同角色不应只用一个赌徒混过。',
 ('The film follows three gamblers over one weekend.','电影跟随三位赌客，讲述一个周末的经历。'),('The novel portrays the founders as bold gamblers.','小说把创办者描绘成大胆的冒险者。'),sources=S('gamblers','gamble'))
W('bets','/bets/','赌注、打赌〔复数〕；下注、确信〔第三人称单数〕',
 '一笔笔押下的钱、作出的打赌，是 bets；说 someone bets that… 也可能只是他确信某件事，不一定真拿钱。',
 'bet + -s，/t/ 后读 /s/；名词复数、动词三单同形。bet 远源未定，口语确信用法后来发展，不硬指定来自 better。',BET+[['bet + -s → bets','多笔赌注；他下注或表示确信']],
 'place bets 下注；small bets 小额赌注；hedge your bets 留多手准备。',
 'bets on the result 押赛果；all bets are off 一切都说不准了。',
 'bets 是押注或确信，bids 是报价；竞拍里举牌叫价，不因为有输赢就改用 bets。',
 ('The story follows a man who keeps making reckless bets.','故事讲一个不断鲁莽下注的男人。'),('She bets that we will arrive before sunset.','她确信我们会在日落前赶到。'),sources=S('bets','bet'))
W('bettors','英 /ˈbetəz/；美 /ˈbetɚz/','下注者、打赌的人〔复数〕',
 '一边有人接收投注，另一边把钱押在某个赛果上的那些人，就是 bettors。词写参与下注的一方。',
 'bettor + -s，读 /z/；内层 bet 双写 t 加完整 -or，尤其常见于美式；不是 better 更好的加复数。',BET+[['bet + -or → bettor → bettors','下注者及其复数，保留完整人物后缀 -or']],
 'sports bettors 体育投注者；bettors at the racecourse 赛马场的下注者。',
 'a group of bettors；experienced bettors。',
 'bettors 下注，bookmakers 经营接收投注；同一事件中的两边角色要区分。',
 ('The documentary interviewed bettors at the racecourse.','纪录片采访了赛马场的下注者。'),('The article compared how bettors and bookmakers viewed the result.','文章比较了下注者和博彩经营者如何看待结果。'),sources=S('bettors','bet'))
W('bookies','/ˈbʊkiz/','接收投注、经营赌注业务的人或机构〔口语复数〕',
 '顾客把赌注交给他们，他们按约定接注、支付输赢，这些人或机构口语叫 bookies。book 在这里连着投注记录，不是书店售货。',
 'bookie + -s → bookies；bookie 是 bookmaker 博彩义的口语缩短形式，带 -ie。复数直接在 -ie 后加 -s。',BOOK+[['bookmaker → bookie → bookies','博彩经营者的口语短称及其复数']],
 'local bookies 当地接注者；bookies at the racecourse 赛马场的接注商。',
 'bets placed with bookies；bookies and bettors。',
 'bookies 接收投注，booksellers 卖书；词里都有 book，却选了记录册、书籍的不同具体用法。',
 ('The novel describes several bookies working near the racecourse.','小说描写了几位在赛马场附近经营接注的人。'),('The report examined how bookies kept records of bets.','报告考察了接注商如何记录赌注。'),sources=S('bookies','bookie'))
W('bookmakers','英 /ˈbʊkˌmeɪkəz/；美 /ˈbʊkˌmeɪkɚz/','经营接收投注的人或机构；制书者〔较早义〕',
 '现代体育新闻里的 bookmakers 多半在接收投注、定赔率；不是在写书、装订书。后者却是这个组合更早真实存在的用途。',
 'bookmaker + -s，读 /z/；内层 book + maker。较早制书者义，后来博彩义联系记录投注的 book、make a book 等表达，不是从作家职业直接变赌客。',BOOK+[['bookmaker + -s → bookmakers','多个经营接收投注者，也可按较早义指制书者']],
 'bookmakers and bettors 博彩经营者与下注者；online bookmakers 网上接注机构。',
 'odds offered by bookmakers；records kept by bookmakers。',
 'bookmakers 通常经营接注业务，gamblers、bettors 是下注者；不是每个下注的人都在当 bookmaker。',
 ('The documentary explained how bookmakers recorded bets.','纪录片解释了博彩经营者如何记录投注。'),('The article compared the odds offered by different bookmakers.','文章比较了不同接注机构给出的赔率。'),sources=S('bookmakers','bookmaker'))
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_zhf',ROOTS,WORDS)
 extend_lessons()
