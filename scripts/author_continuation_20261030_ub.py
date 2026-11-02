"""Everyday past forms: letting go, appearing, waking, freezing and tearing."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'B2558':dict(words=['forgive','forgave','forgiven'],label='forgive、forgave、forgiven：不再追究',note='forgive 历史上可说免去债务、宽恕过错；forgave 是过去式，forgiven 是过去分词。'),
 'B2963':dict(words=['arise','arose','arisen'],label='arise：事情冒出来',note='arise → arose → arisen，常说问题、机会、需要出现；保留 rise 词族的元音换形。'),
 'B3006':dict(words=['awake','awoke','awoken'],label='awake 的动词过去形式',note='awake 作动词常用 awoke、awoken；作形容词时说 be awake。历史上多个醒、唤醒动词材料合流，不能只用现代字母机械拆。'),
 'B2867':dict(words=['freeze','froze','frozen'],label='freeze、froze、frozen：冻住与停住',note='froze 是过去式；frozen 是过去分词。结冰的停固画面可帮助理解吓呆、设备卡住等比喻。'),
 'B2751':dict(words=['tear','tore','torn'],label='tear 的撕裂分支与过去形式',note='撕裂 tear → tore → torn；泪水 tear 另源且读音不同。tore 后来取用了旧分词的元音材料，词形也会在家族内部类推改换。'),
 'B2995':dict(words=['swear','swore','sworn'],label='swear 的过去式与承诺、粗话两支',note='swear → swore → sworn；认真发誓与说粗话是同一词的不同常用分支。'),
 'B2826':dict(words=['bleed','bled'],label='bleed 与 bled：流出、渗出',note='bleed → bled → bled；原形长元音与过去短元音对应，保留旧出血词族与过去词尾演变。'),
 'B2831':dict(words=['breed','bred'],label='breed 与 bred：繁育、养成、滋生',note='breed → bred → bred；繁育后代、人的成长环境和滋生某种情绪要按搭配理解。'),
}
W('forgave','英 /fəˈɡeɪv/；美 /fərˈɡeɪv/','原谅了；宽免了；forgive 的过去式',
 '别人做了错事，你决定放下追究和怨恨。forgave 说这份原谅发生在过去。',
 'forgive 接古英语 forgiefan，含旧 for- 与给予动词 giefan，已有给予、宽免债务、原谅等义；过去形式 forgeaf 等发展为 forgave。这里 for- 不等于今天介词 for 的逐字意思。',
 [['古英语 forgiefan、forgeaf 等','给予、宽免及其过去形式'],['现代 forgive → forgave → forgiven','原谅的原形、过去式、过去分词']],
 'forgave him 原谅了他；forgave her for being late 原谅她迟到；forgave the debt 免除了债务。日常重点常是决定不再为过错责怪对方。',
 'forgave someone for something；eventually forgave。','forgave 不等于忘记发生过什么。forgot 是忘记；forgave 是对过错或债务采取宽免的态度或行动。',
 ('She forgave him for breaking the cup.','她原谅了他打碎杯子的事。'),('He apologized, and I forgave him.','他道了歉，我原谅了他。'),sources=['https://www.etymonline.com/word/forgive','https://en.wiktionary.org/wiki/forgave#English'])
W('forgiven','英 /fəˈɡɪvən/；美 /fərˈɡɪvən/','被原谅的；已宽免；forgive 的过去分词',
 '原谅这件事已经发生，或一个人已经得到原谅。have forgiven 看作出的原谅，be forgiven 看得到原谅的人或事。',
 '继承 forgive 所接古英语 forgiefan 的分词 forgifen 等材料；现代 forgiven 保留分词 -en，与 gave、given 的换形相对应。',
 [['古英语 forgiefan、forgifen 等','宽免、原谅与相应分词'],['现代 forgiven','have forgiven 已原谅；be forgiven 被原谅']],
 'have forgiven someone 已经原谅某人；can be forgiven for something 因某事可以得到谅解；a debt was forgiven 一笔债被免除。',
 'forgiven and forgotten；never been forgiven。','forgave 可直接说过去：She forgave me。forgiven 通常需放进 have forgiven、was forgiven 等结构，不能直接写 She forgiven me。',
 ('I have forgiven him, but I still remember what happened.','我已经原谅了他，但仍记得发生的事。'),('The small mistake was quickly forgiven.','那个小失误很快就得到了谅解。'),sources=['https://www.etymonline.com/word/forgive','https://en.wiktionary.org/wiki/forgiven#English'])
W('arose','英 /əˈrəʊz/；美 /əˈroʊz/','出现了、产生了；arise 的过去式',
 '讨论本来进行得好好的，一个新问题冒了出来。这个从没有摆在面前到出现的变化，是 arose 最常见的用法。',
 'arise 接古英语 arisan，属于 rise 上升、起身词族。原形与过去形式承接旧强变化，现代为 arise、arose、arisen；出现、产生义在旧词中已有。',
 [['古英语 arisan；rise 词族','起身、上升；产生、出现'],['现代 arise → arose → arisen','出现、产生的常用过去表达']],
 'a problem arose 出了问题；an opportunity arose 出现机会；the dispute arose from a misunderstanding 争议源于误会。',
 'a need arose；when the question arose。','arose 通常由事情自己出现：A problem arose。不能用它直接表示某人提出了问题；raised a question 才把提出者放在主语位置。',
 ('A new problem arose during the test.','测试过程中出现了一个新问题。'),('The disagreement arose from a misunderstanding.','分歧源于一场误会。'),sources=['https://www.etymonline.com/word/arise','https://en.wiktionary.org/wiki/arose#English'])
W('arisen','英 /əˈrɪzən/；美 /əˈrɪzən/','已经出现、产生；arise 的过去分词',
 '事情已经冒出来，现在需要面对；has arisen 就把出现这件事接到眼下。',
 'arise 的旧强变化词族保留了分词材料，现代 arisen 与 risen 相对应。a- 是旧前缀材料，不把全词理解为现代冠词 a 加 rise。',
 [['古英语 arisan 词族','起身、出现、产生'],['现代 arisen','arise 的过去分词；常接 has、have、had']],
 'a difficulty has arisen 出现了困难；questions have arisen 出现了疑问；had arisen earlier 更早就已出现。',
 'problems arising from something；problems that have arisen。','arose 常直接放在一般过去句中；arisen 接完成结构。has arisen 表示出现，不自动表示问题已经解决。',
 ('Several questions have arisen since the meeting.','会议之后出现了几个疑问。'),('We discussed the difficulties that had arisen during the move.','我们讨论了搬迁过程中已经出现的困难。'),sources=['https://www.etymonline.com/word/arise','https://en.wiktionary.org/wiki/arisen#English'])
W('awoke','英 /əˈwəʊk/；美 /əˈwoʊk/','醒了；开始意识到；awake 的过去式',
 '原来睡着，后来睁开眼，awoke 说这个醒来的转折。awoke to a problem 又把清醒转到终于认识到问题。',
 'awake 合流了古英语 awæcnan、awacian 等醒来、清醒的动词材料；旧强变化过去 awoc 等与现代 awoke 相承。不能把它当作规则 awake + -ed。',
 [['古英语 awæcnan、awoc 等；与 awacian 合流','醒来、清醒及其旧变位'],['现代 awake → awoke → awoken','醒来；比喻开始认识到']],
 'awoke early 很早醒来；awoke to birdsong 在鸟鸣中醒来；awoke to the danger 开始意识到危险。',
 'awoke from a dream；awoke with a start。','awoke 是动词过去式；awake 也可作形容词：I was awake 我醒着。日常口语也很常说 woke up。',
 ('She awoke to the sound of rain.','她在雨声中醒来。'),('He awoke from a strange dream.','他从一个奇怪的梦中醒来。'),sources=['https://www.etymonline.com/word/awake','https://en.wiktionary.org/wiki/awoke#English'])
W('awoken','英 /əˈwəʊkən/；美 /əˈwoʊkən/','已醒来；被唤醒；awake 的过去分词',
 'have awoken 表示已经醒来；was awoken by a noise 把视线放在被声音叫醒的人身上。',
 '接 awake 的旧醒来词族和分词材料，现代强变化组常记 awake、awoke、awoken。awaken 则是另一个相关动词，现代常用 awakened。',
 [['古英语 awæcnan、awacen 等及后续合流','醒来及相应过去分词'],['现代 awoken','awake 的常用过去分词']],
 'had awoken early 当时很早就醒了；was awoken by the alarm 被闹钟叫醒。使用习惯会有差别，woken up、awakened 也常见。',
 'have just awoken；awoken from sleep。','awake → awoke → awoken；awaken → awakened → awakened。两个动词相关，但不能把 awoken 接成 awaken 的普通 -ed 形式。',
 ('I had awoken before the alarm rang.','闹钟响之前我已经醒了。'),('She was awoken by a loud noise outside.','她被外面一声巨响吵醒了。'),sources=['https://www.etymonline.com/word/awake','https://en.wiktionary.org/wiki/awoken#English'])
W('froze','英 /frəʊz/；美 /froʊz/','结了冰；冻住了；僵住、卡住了；freeze 的过去式',
 '水冷到不再流动，成了冰；人吓得一动不动、画面突然卡住，也借这幅停住的画面。',
 'freeze 接古英语 freosan，旧过去式 freas、分词 froren 等，经后续变化形成现代 freeze、froze、frozen；现代 z 拼写和分词也经过改换。',
 [['古英语 freosan 等结冰词族','结冰及旧过去形式'],['现代 freeze → froze → frozen','冻住；后来也说身体、设备等停住']],
 'the lake froze 湖结冰了；froze with fear 吓僵了；the screen froze 屏幕卡住了；froze the price 把价格固定住。',
 'froze overnight；froze for a moment。','froze 是发生动作或变化的过去式，frozen 是分词和状态形容词：The water froze；the water is frozen。',
 ('The lake froze overnight.','湖一夜之间结了冰。'),('She froze when she heard footsteps behind her.','听见身后的脚步声，她僵住了。'),sources=['https://www.etymonline.com/word/freeze','https://en.wiktionary.org/wiki/froze#English'])
W('tore','英 /tɔː/；美 /tɔːr/','撕破了、扯开了；tear〔撕裂〕的过去式',
 '把连在一起的东西硬拉开：纸裂了，布破了。tore away 还可说用力扯开、挣脱。',
 '撕裂 tear 接古英语 teran，旧过去式 tær、分词 toren。现代 tore 后来取用了旧分词的元音材料，替代较早 tare 等过去形式。',
 [['古英语 teran；旧分词 toren 等','用力撕开、扯裂'],['后来的 tore → 现代 tear、tore、torn','旧分词材料参与形成现代过去式']],
 'tore the paper 撕了纸；tore a hole 扯出一个洞；tore up the letter 把信撕碎；tore down the old shed 拆了旧棚屋。',
 'tore it in half；tore a page out。','撕裂的原形 tear 读英 /teə/、美 /ter/；眼泪 tear 读英 /tɪə/、美 /tɪr/。流泪的动词过去常写 teared，不能套成 tore。',
 ('He tore the paper in half.','他把纸撕成了两半。'),('She tore a hole in her sleeve on a nail.','她的袖子被钉子扯出了一个洞。'),sources=['https://www.etymonline.com/word/tear','https://en.wiktionary.org/wiki/tore#English'])
W('torn','英 /tɔːn/；美 /tɔːrn/','撕破的；难以取舍的；tear〔撕裂〕的过去分词',
 '一块布被往两边拉，留下裂口；一个人同时被两个选择拉扯，就会 feel torn。',
 '来自撕裂动词 tear 的旧分词材料，古英语有 toren。现代 torn 既作过去分词，也用作撕破的、内心受拉扯的形容词。',
 [['古英语 teran → 分词 toren 等','撕裂；被撕开'],['现代 torn','撕破的；比喻在选择间左右为难']],
 'a torn shirt 破了的衬衫；has torn the page 已撕破页面；be torn between two choices 在两个选择间左右为难。',
 'torn apart；torn between duty and desire。','torn between 强调两边都牵动自己；undecided 只直接说还没决定。torn 作形容词保留了被往两边扯的感觉。',
 ('He was wearing a torn shirt.','他穿着一件撕破的衬衫。'),('She was torn between staying home and joining her friends.','她在留在家里与去和朋友见面之间难以取舍。'),sources=['https://www.etymonline.com/word/tear','https://en.wiktionary.org/wiki/torn#English'])
W('swore','英 /swɔː/；美 /swɔːr/','发了誓、郑重保证；说了粗话；swear 的过去式',
 '说话时把保证的分量压得很重，是 swore；气恼时冒出粗话，也可能用同一个过去式。具体是哪种，要听后面的内容。',
 'swear 接古英语 swerian，旧过去式 swor、分词 sworen。原先郑重起誓，后来由不敬地援引神圣名字等用法发展出说粗话的分支。',
 [['古英语 swerian、swor 等','郑重起誓及其过去形式'],['现代 swore','发誓、保证；也可说骂了粗话']],
 'swore to help 发誓帮助；swore that it was true 坚称是真的；swore at the driver 对司机骂粗话；swore off sweets 发誓戒掉甜食。',
 'swear → swore → sworn；swore never to return。','swore that 常引出坚称的内容；swore at 指把粗话冲某人说。不能看到 swore 就都译成发誓。',
 ('He swore that he had locked the door.','他坚称自己锁了门。'),('She swore when she dropped the heavy box on her foot.','沉重的箱子砸到脚上时，她骂了一句。'),sources=['https://www.etymonline.com/word/swear','https://en.wiktionary.org/wiki/swore#English'])
W('bled','/bled/','流了血；渗了色；bleed 的过去式、过去分词',
 '血从小伤口里流出来，是 bled；洗衣时染料从布里渗出来、串到别处，也借这个流出的画面。',
 'bleed 接古英语 bledan 出血、使出血，与 blood 词族相连；bled 承接旧过去形式经后续缩短、词尾变化的发展。现代 bleed 长元音 /iː/ 对应 bled 短元音 /e/。',
 [['古英语 bledan 等血液、出血词族及过去材料','流血、使流血'],['现代 bleed → bled → bled','流血；后来也说染色渗出']],
 'his finger bled 他的手指出血了；the red dye bled 红染料渗出来了；bled money 持续大量耗钱。',
 'bled through the fabric；bled onto another shirt。','bled 是 bleed 的动词过去形式；blood /blʌd/ 通常是血这一名词。读音和词性一起记，别按拼写相似就读成一样。',
 ('His finger bled after he caught it on a thorn.','他的手指被刺挂破后出了血。'),('The red dye bled onto the white cloth.','红色染料渗到了白布上。'),sources=['https://www.etymonline.com/word/bleed','https://en.wiktionary.org/wiki/bled#English'])
W('bred','/bred/','繁育了；养成、长大的；滋生了；breed 的过去式、过去分词',
 '养出下一代，或让某种习惯、情绪慢慢长出来，都可用 breed。bred 把过程放到过去，或说已经形成的背景。',
 'breed 接古英语 bredan 繁殖、育幼、保暖等，同源材料有孵育的意思；bred 承接其过去变化。养育、生长、教育的分支也很早就存在。',
 [['古英语 bredan 等孵育、繁殖词族','育幼、保暖；繁殖'],['现代 breed → bred → bred','繁育、养成；比喻滋生']],
 'bred sheep 繁育绵羊；born and bred 出生并长大；bred resentment 滋生怨恨。a well-bred person 旧式说法可指有教养的人。',
 'born and bred in a place；bred for a purpose。','bred 与 bread 面包同音 /bred/。born 说出生，bred 在 born and bred 中说成长、养育背景，二者各添一层信息。',
 ('She was born and bred in a small coastal town.','她出生并成长在一座海边小镇。'),('The family bred horses for many years.','这家人繁育马匹已有多年。'),sources=['https://www.etymonline.com/word/breed','https://en.wiktionary.org/wiki/bred#English'])
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_ub',ROOTS,WORDS)
 extend_lessons()
