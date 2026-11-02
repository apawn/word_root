"""Alcohol's powder-to-spirit history; evil and the practical adverb usefully."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
A=[['阿拉伯语 al-kuḥl → 中世纪拉丁 alcohol → 欧洲相关形式','用于眼部化妆的细粉；al- 是定冠词'],['早期英语 alcohol 的炼金、化学用语','细粉、精制物 → 酒的精馏成分'],['现代 alcohol','日常常酒精、酒；化学也指醇类']]
def AH(f,m):return A+[[f,m]]
W('alcohol','英 /ˈælkəhɒl/；美 /ˈælkəhɔːl/ 或 /ˈælkəhɑːl/','酒精、酒；醇〔化学类别〕',
 '日常说不喝 alcohol，多半是在说不喝含酒精的饮品；实验室里 an alcohol 却可能说醇类中的一种，不能全当能喝的酒。',
 '经中世纪拉丁及欧洲传播，接阿拉伯语 al-kuḥl 细粉、眼部化妆粉。炼金化学用语把精细、精制物的称呼扩展到酒的精馏成分，后来形成现代酒精、醇义；不是阿拉伯语本来就专指啤酒。',A,
 'drink alcohol 喝酒，alcohol content 酒精含量，ethyl alcohol 乙醇，alcohol in the sample 样本中的酒精或醇，按分析对象。',
 'drink alcohol；alcohol content；ethyl alcohol；a type of alcohol。',
 '日常 alcohol 常指乙醇或酒，化学 alcohol 范围更广；类别名称不能用来判断是否可饮用。al- 这里来自阿拉伯定冠词，不是现代英语 all。',
 ('He does not drink alcohol.','他不喝酒。'),('The label states the drink’s alcohol content.','标签注明了饮品的酒精含量。'),
 sources=['https://en.wiktionary.org/wiki/alcohol#English','https://www.etymonline.com/word/alcohol'])
W('alcoholic','英 /ˌælkəˈhɒlɪk/；美 /ˌælkəˈhɔːlɪk/ 或 /ˌælkəˈhɑːlɪk/','含酒精的；与酒精有关的；酒精依赖者〔人物名词〕',
 '放在 drink 前，说饮料含酒精；a person is an alcoholic 则在说依赖问题，不是只说他偶尔喝酒。',
 'alcohol + -ic 相关的形容词；后来也有指人的名词用法。形容词、人物名词形成时间和语境有别，不把 drink 的含酒精义直接等同人的诊断。',AH('alcohol + -ic → alcoholic','含酒精、与酒精有关；再有人物名词'),
 'alcoholic drinks 含酒精饮品，alcoholic fermentation 酒精发酵；人物名词常见于旧叙述、自我认同或具体群体名称，称人时注意语境。',
 'alcoholic drinks；an alcoholic beverage；alcoholic fermentation。',
 'alcoholic drink 是饮料性质，alcoholic 人物名词涉及依赖；不能说凡 drink alcohol 者都是 alcoholic。',
 ('The café serves both alcoholic and soft drinks.','这家咖啡馆既卖含酒精饮品，也卖软饮料。'),('The lesson explains the role of yeast in alcoholic fermentation.','这节课解释酵母在酒精发酵中的作用。'))
W('alcoholism','英 /ˈælkəhɒlɪzəm/；美 /ˈælkəhɔːlɪzəm/ 或 /ˈælkəhɑːlɪzəm/','酒精依赖、酒瘾〔常见称呼〕',
 '不是一次喝醉，而是饮酒与控制、生活持续发生问题的概念。今天医学材料更常用 alcohol use disorder，阅读旧书还会遇到 alcoholism。',
 '现代对应 alcohol + -ism，与十九世纪医学拉丁语 alcoholismus 等名称相关。-ism 在此命名一种状态、问题，不是支持喝酒的主义。',
 AH('医学拉丁语 alcoholismus 等 → alcoholism；对应 alcohol + -ism','酒精相关长期问题的名称'),
 'the history of alcoholism 酒精依赖的历史，a memoir about alcoholism 关于酒瘾的回忆录，alcoholism research 酒精相关依赖研究。',
 'the history of alcoholism；a memoir about alcoholism；alcoholism research。',
 'alcoholism 不等于任意 drinking，也不同于一次 alcohol poisoning 酒精中毒；现代 AUD 与旧称的使用背景不完全相同，不能只凭一个词给人作判断。',
 ('The memoir describes a family affected by alcoholism.','回忆录描述了一个受到酒精依赖影响的家庭。'),('The article discusses changing language around alcoholism.','文章讨论了人们谈论酒精依赖时用语的变化。'),
 sources=['https://en.wiktionary.org/wiki/alcoholism#English','https://www.niaaa.nih.gov/publications/brochures-and-fact-sheets/understanding-alcohol-use-disorder'])
W('ethanol','英 /ˈeθənɒl/；美 /ˈeθənɑːl/','乙醇、乙基醇',
 '把日常酒精进一步说成确切化学物质名，常指乙醇；它只是醇类中的一种，不是所有 alcohols 的总称。',
 '化学命名对应 ethane 乙烷去 e 加 -ol 醇。前项保留两碳骨架的命名，后项标明醇，不是 ethan 某人名字 + ol。',
 [['ethane〔乙烷〕+ -ol〔醇〕→ ethanol〔去 e〕','对应两碳骨架的一种醇'],['现代 ethanol','乙醇的化学名称']],
 'ethanol content 乙醇含量，an ethanol sample 乙醇样本，ethanol production 乙醇生产。',
 'ethanol content；an ethanol sample；ethanol production。',
 'ethanol 是具体物质，alcohol 可是类别或日常简称；ethane 乙烷与 ethanol 乙醇后缀不同，对应物质也不同。',
 ('The report gives the ethanol content of the sample.','报告列出了样本的乙醇含量。'),('The textbook compares ethanol with other alcohols.','教材把乙醇与其他醇作了比较。'),
 sources=['https://en.wiktionary.org/wiki/ethanol#English','https://www.etymonline.com/word/ethanol'])
W('alkyl','/ˈælkaɪl/，也见 /ˈælkɪl/','烷基〔化学〕；烷基的',
 '把烷烃少一个氢的位置看成能接到别处的碳氢片段，例如 methyl 甲基。不是一种叫作 alkyl 的单独饮料。',
 '历史名称由 alcohol 的缩短材料与 -yl 基团命名后缀组成；现代化学义固定为烷基，不能按旧材料就认定每个 alkyl 都含酒精。',
 [['alcohol 的缩短材料 + -yl → alkyl','化学基团名称'],['现代 alkyl','由烷烃相应得到的碳氢基团名']],
 'an alkyl group 烷基，an alkyl chain 烷基链，methyl and other alkyl groups 甲基及其他烷基。',
 'an alkyl group；an alkyl chain；alkyl groups。',
 'alkyl 是基团类别，alcohol 是醇类；名称的历史联系不等于两种化学类别现代完全相同。',
 ('Methyl is an example of an alkyl group.','甲基是烷基的一个例子。'),('The diagram labels the alkyl chain in blue.','图中用蓝色标出了烷基链。'),
 sources=['https://en.wiktionary.org/wiki/alkyl#English','https://goldbook.iupac.org/terms/view/A00228'])
R('B3671','从细粉到酒精；生活用语与化学名称','ALCOHOL：旧时精制物的名字，后来专指酒的成分，再扩到醇类','alcohol → alcoholic、alcoholism；ethanol 是乙醇，alkyl 是历史关联的化学基团命名，不把它们都译成酒。',
 '先看日常酒、酒精，再看化学醇类。形容饮料含酒精和人物名词说人的依赖，是不同用法。',
 '阿拉伯 al-kuḥl 经中世纪拉丁等 → alcohol；alcohol + -ic/-ism；ethane + -ol → ethanol；alcohol 缩短材料 + -yl → alkyl。',
 [['日常、人物与状态','alcohol · alcoholic · alcoholism'],['化学物质与基团','ethanol · alkyl']],
 'alcohol 类别不全是可饮用酒；alcoholic drink 非人的依赖；ethanol 是特定醇，alkyl 是基团；-ism 不只主义。',
 'The label gives the alcohol content, while the lab report names ethanol.\n\n标签写酒精含量，实验报告则明确写乙醇。','alcohol alcoholic alcoholism ethanol alkyl')
E=[['古英语 yfel → 中古英语 yvel、evel → evil','坏、恶、有害；本族继承词'],['现代 evil 的常用重心','道德邪恶、严重有害；也可故事里的邪恶力量']]
W('evil','/ˈiːvəl/','邪恶的、恶毒的；恶、邪恶；严重有害的事物',
 '不仅做得差，还常指道德上很坏、存心伤害人的那种坏。故事里 evil 又能当一股与善对抗的力量。',
 '继承古英语 yfel，经中古英语多个拼写接现代 evil。旧时坏、有害的范围更宽；远源有不同分析，不拆成 e + vil 来编意义。',E,
 'an evil act 邪恶行为，good and evil 善与恶，an evil grin 恶意狞笑，the lesser of two evils 两害相权取其轻。',
 'an evil act；good and evil；an evil grin；the lesser of two evils。',
 'bad 范围很宽，evil 常道德评价更重；a bad meal 难吃的一餐通常不能因此叫邪恶一餐。',
 ('The story explores the struggle between good and evil.','故事探讨善与恶的斗争。'),('The villain gave an evil grin.','反派露出恶意的狞笑。'))
W('evilly','/ˈiːvəli/，也见 /ˈiːvli/','邪恶地、恶毒地',
 '不是普通笑一笑，而是带着伤害别人、让人发寒的恶意去笑、盯视。',
 'evil + -ly，拼写相接形成 ll，副词替代更早 evil 直接作副词的旧用法。',E[:1]+[['evil + -ly → evilly','带邪恶、恶意地']],
 'grin evilly 狞笑，smile evilly 恶意地笑，glitter evilly 透出凶恶闪光〔文学〕。',
 'grin evilly；smile evilly；glitter evilly。',
 'evilly 修饰动作，evil 形容性质；evilly 常在故事、强烈评价中，不是每个 mischievously 淘气地都上升为邪恶。',
 ('The villain smiled evilly at the frightened hero.','反派对着受惊的主角恶毒地笑。'),('The creature’s eyes glittered evilly in the dark.','那生物的眼睛在黑暗中闪着凶恶的光。'))
W('evilness','/ˈiːvəlnəs/','邪恶、邪恶的性质',
 '把某个人、行为所带的恶当作一个性质讨论；不是再增加一个更邪恶的人物。',
 '对应 evil + -ness；古英语 yfelnyss 经中古英语 yvelnesse 已有相应抽象词，不是全新现拼。',E[:1]+[['古英语 yfelnyss → 中古英语 yvelnesse → evilness','邪恶、恶的性质']],
 'the evilness of an act 某行为的邪恶，portray evilness 描绘邪恶性质。evil 本身也可名词，evilness 更直接把性质单独拎出来。',
 'the evilness of；portray evilness；a sense of evilness。',
 'evil 名词可说恶、恶的事物，evilness 强调邪恶性质；表达中 evil 通常更简洁常见，不必每句都加 -ness。',
 ('The critic discussed the evilness of the character’s actions.','评论者讨论了这个角色所作所为的邪恶。'),('The actor conveyed evilness without raising his voice.','演员没有提高音量，就表现出了邪恶感。'))
R('B3179','严重道德之恶与恶意表达','EVIL：比一般“不好”更重，常涉及蓄意伤害和道德判断','evil → evilly、evilness，分别看性质、动作方式与抽象性质。',
 '形容饭菜不好不必叫邪恶，故事里的反派才常用 evil 的强烈评价。evilness 可读懂，日常很多地方用 evil 已足够。',
 '古英语 yfel → evil；evil + -ly → evilly；yfelnyss 经中古英语 → evilness。',
 [['性质、动作方式与性质名词','evil · evilly · evilness']],
 'bad 范围宽，evil 道德评价重；mischievous 淘气不自动邪恶；evil 本身也可名词。',
 'The evil character grinned evilly.\n\n邪恶的角色露出恶毒的狞笑。','evil evilly evilness')
W('usefully','/ˈjuːsfəli/','有用地、有效益地；派得上用场地',
 '时间、信息没有白白放着，而是真帮上了忙。usefully occupied 就是忙的事情有价值。',
 'useful + -ly，useful 末尾一个 l，与后缀相接成为 usefully 的 ll。副词强调行动、安排有用。',
 [['use + -ful → useful','能派上用场的'],['useful + -ly → usefully','以有用、有帮助的方式']],
 'usefully employed 有效利用，usefully occupied 忙于有益事情，usefully compare 作有帮助的比较。',
 'usefully employed；usefully occupied；usefully compare。',
 'useful 形容词、usefully 副词、usefulness 有用性名词；busy 忙不保证 usefully occupied 忙得有价值。',
 ('The waiting time was usefully spent reviewing notes.','等待时间被有效利用来复习笔记。'),('The report usefully compares the two methods.','报告对两种方法作了很有帮助的比较。'))
R('B4218','派上用场与有益的行动','USEFUL：能帮你把事情往前推，时间也可以用得有价值','useful → usefully、usefulness，分别说性质、方式和性质名词。',
 '不只是放在一边也不坏，而是实际能帮忙。忙着做事和忙得有益要分清。',
 'use + -ful → useful；useful + -ly/-ness；usefully 接成 ll。',
 [['性质、方式与有用性','useful · usefully · usefulness']],
 'useful 形容物、usefully 修饰做法、usefulness 讨论有用程度；useful 一个 l、usefully 接后缀后两个。',
 'The useful notes helped us spend the time usefully.\n\n这些有用的笔记帮助我们把时间用得有价值。','useful usefully usefulness')
if __name__=='__main__':save('continuation_20261030_do',ROOTS,WORDS)
