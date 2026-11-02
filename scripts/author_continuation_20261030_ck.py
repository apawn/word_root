"""Cat and mad: animals, naming by likeness, emotional and figurative uses."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
C=[['古英语 catt、catte → 中古英语 cat、catte → cat','猫；日耳曼语与晚期拉丁语 cattus 等名称有联系，远源未定'],['英语 cat 与合成、比喻','猫类、像猫的外形或被比作猫的行为；技术同形可另源']]
def CH(f,m):return C+[[f,m]]
W('cat','/kæt/','猫；猫科动物〔较宽用法〕',
 '日常先想家里的猫；big cats 则能说狮、虎等大型猫科动物。合成词有时借胡须、短尾、步态或拟人评价，不要求真是一只猫。',
 '接古英语 catt、catte 等，近代欧洲猫名与晚期拉丁语 cattus 等相关，具体较远来源不定。计算机命令 cat 来自 concatenate 的缩短，不能拿动物词源解释。',C,
 'a pet cat 宠物猫，a stray cat 流浪猫，big cats 大型猫科动物；let the cat out of the bag 泄露秘密是习语，不必真的有猫和袋子。',
 'a pet cat；a stray cat；big cats；let the cat out of the bag。',
 'cat 不自动指母猫或某一品种；kitten 小猫。技术 cat 同形缩短另讲，不把所有 CAT 字母组合都当动物。',
 ('The cat slept on the warm windowsill.','猫睡在暖和的窗台上。'),('The documentary follows several big cats in the wild.','纪录片追踪了几种野外的大型猫科动物。'))
W('bobcat','英 /ˈbɒbkæt/；美 /ˈbɑːbkæt/','短尾猫、赤猞猁；Bobcat 亦见工程机械专名',
 '看尾巴：它短短的，像被截短了一截，所以 bob 说的是短尾，不是一个叫 Bob 的人养的猫。',
 'bob 短尾、截短的部分 + cat 猫，合成北美猫科动物名。大写专名用于机械时，另按品牌语境理解。',CH('bob + cat → bobcat','因短尾得名的北美猫科动物'),
 'a wild bobcat 野生短尾猫，bobcat tracks 短尾猫足迹；工程语境的 Bobcat 需看是品牌或被泛称的设备。',
 'a wild bobcat；bobcat tracks；a bobcat’s short tail。',
 'bobcat 特定动物名，wildcat 更泛并有商业冒险等比喻；不是每只野外的猫都叫 bobcat。',
 ('The bobcat disappeared into the trees.','那只短尾猫消失在树林里。'),('We saw bobcat tracks near the stream.','我们在溪边看见了短尾猫的足迹。'))
W('catnip','/ˈkætnɪp/','猫薄荷',
 '一种常见的猫用植物名称；名字后面的 nip 接旧植物名，不是在说小猫咬你一口。',
 'cat + nep、nip，后一部分来自古英语 nepte，接拉丁语 nepeta 的植物名。与现代 nip 轻咬的动词同形但不是这里的拆法。',C[:1]+[['cat + 旧植物名 nep、nip → catnip','猫薄荷；nip 接拉丁语 nepeta 的借词路径']],
 'dried catnip 干猫薄荷，a catnip toy 装猫薄荷的玩具，catnip leaves 猫薄荷叶。也可比喻对某人特别有吸引力的东西。',
 'dried catnip；a catnip toy；catnip leaves。',
 'catnip 不是 cat + nip 轻咬，也不是所有薄荷植物的统称；对猫反应的具体差异不由词名保证。',
 ('She put dried catnip inside the toy.','她把干猫薄荷放进了玩具。'),('The new puzzle was catnip to the enthusiastic mathematician.','那个新谜题对热衷数学的人极有吸引力。'))
W('catty','/ˈkæti/','尖酸刻薄、暗中挖苦的〔口语〕',
 '话不一定大声，却带着小刺，故意让别人难受。这里是人把猫的形象拿来评价说话，不是对猫的科学性格结论。',
 'cat + -y，双写 t，形容词由像猫的旧评价发展为尖酸、挖苦。另有重量单位 catty〔斤等语境〕来自马来语等，是不同来源。',CH('cat + -y → catty','旧拟人评价 → 尖酸、带刺的'),
 'a catty remark 尖酸的话，catty comments 挖苦评论，be catty about someone 挖苦某人。',
 'a catty remark；catty comments；be catty about。',
 'catty 尖酸评价，不等于 witty 机智；机智玩笑不一定刻薄。重量单位同形名词不要归入猫。',
 ('She regretted making a catty remark about his clothes.','她后悔挖苦了他的穿着。'),('The review was full of catty comments.','那篇评论充满了尖酸刻薄的话。'))
W('catsuit','/ˈkætsuːt/','紧身连体衣',
 '身体和腿部包在一件贴身衣服里，整体线条让人联想到猫般的流畅姿态；不是给宠物穿的衣服。',
 'cat + suit 衣服、套装，合成贴身连体服名称。这里 cat 是形象借用，穿的人并不需要扮演某个特定角色。',CH('cat + suit → catsuit','贴身连体服'),
 'a black catsuit 黑色紧身连体衣，wear a catsuit 穿连体衣，a stage catsuit 舞台紧身连体服。',
 'a black catsuit；wear a catsuit；a stage catsuit。',
 'catsuit 紧身连体衣，a suit for a cat 给猫穿的衣服；普通 jumpsuit 连体衣更宽泛，不保证紧身。',
 ('The dancer wore a silver catsuit on stage.','舞者在台上穿了一件银色紧身连体衣。'),('The costume designer adjusted the sleeves of the catsuit.','服装设计师调整了紧身连体衣的袖子。'))
R('B2412','猫类动物；外形、植物名和拟人评价','CAT：动物名向胡须、短尾、步态或人物评价扩展','cat → catty；bobcat 动物，catnip 植物；catfish、wildcat、catwalk、copycat、catsuit、catfight 按外形和行为分支复用。',
 '不是每个合成词真是猫：catfish 是鱼、catwalk 是通道；技术 cat 来自 concatenate。catnip 的 nip 是植物名旧形。',
 'cat + -y 双写 t；bob + cat；cat + nip/suit/fish/walk/fight；copy/wild + cat。',
 [['基本动物与野生类','cat · bobcat · wildcat'],['植物、外形命名与衣服','catnip · catfish · catwalk · catsuit'],['行为和人物评价','copycat · catty · catfight']],
 'catnip 非轻咬；catty 形容词与重量单位名词另源；catsuit 非猫衣；bobcat 非所有野猫的总称。',
 'The cat ignored the toy until she added some catnip.\n\n她加了些猫薄荷后，猫才开始理那个玩具。','cat bobcat wildcat catnip catfish catwalk catsuit copycat catty catfight')
M=[['古英语 ġemǣd、ġemǣded 等 → 中古英语 mad、madde → mad','愤怒、失去理智等旧用法'],['英语 mad','生气、狂热喜爱；荒唐、不理智等评价']]
def MH(f,m):return M+[[f,m]]
W('mad','/mæd/','生气的；狂热喜爱的；荒唐、不理智的〔口语〕',
 '情绪冲得很强：可以气得不行，也可以喜欢得不得了；哪条意思要看后面跟 at、about、with 等什么搭配。',
 '接古英语相关旧形，经中古英语 mad 延续。它有旧时描述精神失常的用法，现代学习优先掌握愤怒、狂热、荒唐等常用场景；不是医学诊断词。',M,
 'mad at someone 生某人的气〔尤美式〕，mad about music 迷恋音乐，a mad idea 荒唐主意，drive someone mad 把某人逼得受不了。',
 'mad at；mad about；drive me mad；a mad rush。',
 'mad about 可狂热喜爱，也可因某事愤怒，得看上下文；mad 与 made /meɪd/ 词形读音都不同。',
 ('Are you mad at me for being late?','你在为我迟到而生气吗？'),('She is mad about old films.','她特别迷老电影。'))
W('madly','/ˈmædli/','疯狂地、拼命地；极其、热烈地',
 '动作、情绪开到很大，不留什么余地；爱得热烈，或忙乱地到处寻找，都可用 madly。',
 'mad + -ly，中古英语已有相关副词形式。现代常作夸张方式或程度，不是每次都指精神疾病。',MH('mad + -ly → madly','以失去节制、强烈的方式；非常'),
 'madly in love 深深热恋，search madly 拼命寻找，wave madly 拼命挥手。',
 'madly in love；search madly；wave madly。',
 'madly 程度强、忙乱，angrily 愤怒地；madly in love 不能译成生气地恋爱。',
 ('They were madly in love.','他们热烈地相爱着。'),('He searched madly for the missing ticket.','他慌忙拼命地寻找丢失的票。'))
W('madness','/ˈmædnəs/','疯狂、荒唐；狂乱局面；旧精神失常称谓',
 '事情乱成一团，或决定冒险得让人难以理解，说话人会称它 madness。常是强烈评价，不是客观诊断。',
 'mad + -ness，中古英语 madnesse 等旧形延续。抽象名词接疯狂、失去理智等意义，现代很多用法是夸张。',MH('mad + -ness → madness','疯狂状态；荒唐行为或狂乱局面'),
 'sheer madness 简直荒唐，the madness of the rush hour 高峰时段的混乱，a moment of madness 一时冲动。',
 'sheer madness；a moment of madness；the madness of。',
 'madness 情绪化评价或旧称谓，chaos 强调秩序混乱；不能据有人说 madness 就判断精神状况。',
 ('Driving through that storm would be sheer madness.','开车穿过那场暴风雨简直太冒险了。'),('We escaped the madness of the city for a quiet weekend.','我们离开城市的喧闹混乱，过了一个安静周末。'))
W('madcap','/ˈmædkæp/','疯狂搞怪、冒失大胆的；冒失鬼',
 '一个念头接一个念头，做出离谱、搞笑或冒险的事。喜剧里常带热闹、荒诞感，不一定是在严肃责骂。',
 'mad + cap，cap 在旧口语可借指头、脑袋；先有指冒失人物的名词，再有修饰 madcap adventure 的形容词用法。不是现代帽子会生气。',MH('mad + cap〔头的借称〕→ madcap','冒失鬼；由人物名词转为疯狂搞怪的'),
 'a madcap adventure 疯狂冒险，a madcap comedy 荒诞喜剧，a madcap scheme 异想天开的计划。',
 'a madcap adventure；a madcap comedy；a madcap scheme。',
 'madcap 常有荒诞、冒失又有趣的色彩，dangerous 只说危险；并非所有危险行动都有喜剧感。',
 ('The film follows a group on a madcap adventure.','电影讲一群人展开荒诞冒险的故事。'),('His madcap scheme somehow worked.','他那异想天开的计划居然成功了。'))
W('madwoman','英 /ˈmædwʊmən/；美 /ˈmædwʊmən/','疯女人〔旧称、贬称或夸张〕',
 '文学或台词里可能这样叫行为被认为失控的女人；很多时候反映说话人的敌意、时代偏见，不能当中性身份。',
 'mad + woman，复数 madwomen。现代常见文学旧称、骂称或 like a madwoman 等夸张比较，不是规范医学名称。',MH('mad + woman → madwoman','被叫作疯狂女性的人物称呼；语气需看时代和场景'),
 'like a madwoman 像疯了似的，the madwoman in the story 故事里被这样称呼的女子。',
 'like a madwoman；the madwoman in the story；portray a madwoman。',
 'madwoman 人物旧称、贬称，madness 抽象状态；用词不能据其标签认定人物真正患有什么疾病。',
 ('She ran down the platform like a madwoman, trying to catch the train.','她像疯了似的沿站台奔跑，想赶上火车。'),('The essay questions why the narrator calls her a madwoman.','文章质疑叙述者为什么称她为疯女人。'))
R('B3787','强烈情绪、狂热喜爱；荒唐与混乱评价','MAD：情绪或行动超出平常控制，按搭配分愤怒、喜爱、荒唐','mad → madly、madness；madcap 冒失搞怪、madhouse 混乱场所、madwoman 人物旧称分支相邻。',
 '保留旧称的历史语境，现代常用场景优先。情绪夸张和对人的标签不冒充医学判断。',
 'mad + -ly/-ness；mad + cap/house/woman；madwoman—madwomen。',
 [['基本词、方式与状态','mad · madly · madness'],['搞怪、场所和人物','madcap · madhouse · madwoman']],
 'mad at 常愤怒、mad about 看语境；madly in love 热恋；madness 常评价荒唐；madwoman 非中性医学称呼。',
 'The madcap comedy made us laugh despite the madness of the day.\n\n尽管那天忙乱不堪，荒诞喜剧还是让我们笑了起来。','mad madly madness madcap madhouse madwoman')
if __name__=='__main__':save('continuation_20261030_ck',ROOTS,WORDS)
