"""Trained, guest and breathe: preparation, hospitality and room for air."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
W('untrained','/ˌʌnˈtreɪnd/','未经训练的、不熟练的',
 '别人练过、受过专门指导，这个人还没有；to the untrained eye 是“在外行看来”，不是说眼球也去上过课。',
 'un- 未、不 + trained 受过训练的，否定训练状态；train 训练义有自己的旧牵引、引导发展，不由火车开过去推断。',
 [['train 的训练用法 → trained','接受过培养、训练'],['un- + trained → untrained','没有接受相应训练']],
 'untrained staff 未受训员工，an untrained dog 未训练过的狗，to the untrained eye 外行看来。是否在某方面受训，要看修饰范围。',
 'untrained staff；an untrained dog；to the untrained eye。',
 'untrained 未练过，unskilled 技能不足，可能重叠但不等同；有经验的人也可能没接受某一项专门训练。',
 ('The untrained dog ignored the command.','未经训练的狗没理会指令。'),('To the untrained eye, the two paintings look identical.','在外行看来，这两幅画一模一样。'))
R('B4557','练过与没练过某项技能','TRAINED：有训练积累；UNTRAINED：未受相应训练','trained → untrained，否定的是特定训练状态，而不是人的全部能力。',
 'to the untrained eye 是从外行观察角度说话，不必真把眼睛单独看成受训者。',
 'train 训练动词 → trained；un- + trained → untrained。',
 [['训练状态与否定','trained · untrained']],
 'untrained/unskilled 未受训练与缺技能；未受某项训练不等于毫无经验。',
 'A trained observer may notice details that an untrained visitor misses.\n\n受过训练的观察者可能注意到未经训练的访客漏掉的细节。','trained untrained')
G=[['古英语 ġiest 与古诺尔斯语 gestr 等近亲形式 → 中古英语 gest → guest','被接待、来访的人；旧形式在英语中合流'],['接待关系扩展','家中客人、旅馆住客、节目嘉宾、系统访客'],['组合','guesthouse 接待住宿的房子；houseguest 住在别人家里的客人']]
W('guest','/ɡest/','客人、旅客、嘉宾；访客；做嘉宾',
 '来到别人的地盘，受到主人接待；旅馆住客付了钱，节目嘉宾带着专门身份，也仍站在“来访这一方”。',
 '中古英语 gest 等接古诺尔斯语 gestr，并与古英语 ġiest 近亲形式合流。更远与 hospitality 的主客互惠词族相关，不等于现代 host 主人和 guest 客人可以随便互换。',G,
 'a dinner guest 晚餐客人，hotel guests 旅馆住客，a guest speaker 特邀演讲者，a guest account 访客账户，guest on a show 做节目嘉宾。',
 'a dinner guest；a guest speaker；hotel guests；a guest account。',
 'guest 被接待或特邀，visitor 泛说访客；customer 顾客说交易角色，同一个人可同时是旅馆 guest 与付费 customer。',
 ('We have three guests staying this weekend.','这个周末有三位客人来住。'),('The professor appeared as a guest on the programme.','教授作为嘉宾参加了节目。'))
R('B3422','站在受接待、来访的一方','GUEST：来到主人或机构这里的人','guest → guesthouse 接待场所；houseguest 在别人家中住宿的客人。旅馆、节目和账户也能用访客身份。',
 'host 与 guest 更远同属主客接待词族，不代表现代角色相同。guest account 的权限也不能只由词名推出。',
 'ġiest、gestr 等 → gest → guest；guest + house → guesthouse；house + guest → houseguest。',
 [['来访与嘉宾基础','guest'],['住宿场所与住家客人','guesthouse · houseguest']],
 'guest/host 受接待与主人；guesthouse/houseguest 前者房、后者人；guest/customer 接待身份与交易身份。',
 'The guesthouse welcomed a guest who had previously been our houseguest.\n\n旅馆迎来了一位客人，他以前也曾在我们家住过。','guest guesthouse houseguest')
B=[['古英语 breath 词族 → 中古英语 brethen → breathe','气息名词基础上形成呼吸动词'],['英语动作、人物工具和能力派生','breathing 呼吸；breather 呼吸者、喘息间歇；breathable 可呼吸、透气']]
W('breathing','/ˈbriːðɪŋ/','呼吸；呼吸着的；呼吸过程、方式',
 '把吸气、呼气这套持续动作当一件事说；也能修饰生物活着在呼吸，不是把 breath 名词复数化。',
 'breathe + -ing，去掉末尾不发音 e，保留动词长元音 /iː/ 和浊 /ð/。',B[:1]+[['breathe + -ing → breathing','正在呼吸；呼吸这一过程']],
 'steady breathing 平稳呼吸，breathing space 缓冲空间、喘息机会，a living, breathing person 活生生的人。',
 'steady breathing；normal breathing；breathing space；living and breathing。',
 'breathing 是过程，breath 是一口气；a breathing space 常比喻留一点处理事情的余地，不只物理上能吸气的房间。',
 ('Her breathing became slower and steadier.','她的呼吸变得更慢、更平稳。'),('The delay gave us some breathing space.','延后给了我们一点喘息、调整的余地。'))
W('breather','英 /ˈbriːðə/；美 /ˈbriːðər/','呼吸者；通气装置；短暂休息、喘口气',
 '原本可以是呼吸的东西；日常 take a breather 常说先歇一小会儿，恢复节奏再继续。',
 'breathe + -er，去末尾 e；人物、装置义之外，又发展出喘息恢复的一段休息。不要把所有 -er 名词都锁死成人。',B[:1]+[['breathe + -er → breather','呼吸者、通气装置'],['英语休息义','短暂喘息、暂停']],
 'take a breather 歇口气，need a breather 需要短暂停一下，a breather pipe 通气管。',
 'take a breather；need a breather；a brief breather。',
 'breather 休息可短，holiday 通常较长假期；breather 也可技术装置，读维修材料时不总是让人休假。',
 ('Let us take a breather before the next section.','下一部分开始前，我们先歇一会儿。'),('The short break gave the team a welcome breather.','短暂休息让团队有了难得的喘息机会。'))
W('breathable','/ˈbriːðəbəl/','可供呼吸的；透气的',
 '空气让人能吸，是 breathable air；布料让湿气、空气适当通过，也说 breathable，但不是衣服自己长肺在呼吸。',
 'breathe + -able，去掉末尾 e，接能呼吸、允许气体通过的能力。词干沿 breathe /briːð/，不是 breath /breθ/。',B[:1]+[['breathe + -able → breathable','可呼吸；可让气体、水汽通过']],
 'breathable air 可呼吸空气，breathable fabric 透气面料，a breathable jacket 透气外套。',
 'breathable air；breathable fabric；a breathable jacket。',
 'breathable 透气性不等于 waterproof 防水性，两种性质可按材料结构组合；不能只凭透气一词推定所有天气用途。',
 ('The jacket is made from a lightweight, breathable fabric.','外套采用轻薄透气的面料。'),('The astronauts checked the supply of breathable air.','宇航员检查了可供呼吸的空气储备。'))
R('B2753','呼吸动作再分过程、喘息和透气能力','BREATHE：动词 /briːð/ 这一条派生保留读音','breathe → breathing、breather、breathable。breather 可休息或装置，breathable 可空气或衣料。',
 '三个常用扩展都沿长元音、浊 th。与 breathless、breathy 的短元音、清 th 放在一起读，词形和发音就容易对上。',
 'breath 词族 → breathe；去末尾 e + -ing/-er/-able → breathing、breather、breathable。',
 [['动作与过程','breathe · breathing'],['主体、间歇和能力','breather · breathable']],
 'breathing/breath 过程与一口气；breather 休息或通气装置；breathable air/fabric 可呼吸与透气。',
 'After a short breather, her breathing settled into a steady rhythm.\n\n歇了一小会儿后，她的呼吸恢复了平稳节奏。','breathe breathing breather breathable')
if __name__=='__main__':save('continuation_20261030_fp',ROOTS,WORDS)
