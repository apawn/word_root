"""High-frequency irregular forms, their pronunciation and real history."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'B3000':dict(words=['tell','told'],label='tell 的过去与过去分词：told',note='tell → told → told；told 接古英语 tealde、teald 的旧变位，不是现代常规拼写 telled。all told 还保留计数旧义。'),
 'B2498':dict(words=['take','took','taken'],label='take、took、taken 连着读',note='took 是过去式，taken 是过去分词；接较早北欧、英语强变位词族。'),
 'B2841':dict(words=['come','came'],label='come 的过去式：came',note='come → came → come；came 沿用中古英语过去形式，其路径还可能有北欧相关形式的影响。'),
 'B2871':dict(words=['go','went','gone'],label='go 的过去式为什么换了开头',note='went 原来是 wend 的过去形式，后来接替 go 的旧过去式；go → went → gone 是不同旧材料合在同一套现代变位里。'),
 'B2591':dict(words=['see','saw','seen'],label='see 的过去式 saw 与过去分词 seen',note='saw 的看见义接 see 的旧强变位；同形的锯工具名另接古英语 sagu，不能把两义编成一个来源。'),
 'B2740':dict(words=['hear','heard'],label='hear 与 heard 的读音、时间变化',note='hear → heard → heard；heard 接较早带 d 的过去形式，现代不读成 hear 原音直接加 d。'),
 'B2558':dict(words=['give','gave','given'],label='give、gave、given 的高频分工',note='gave 是 give 的过去式，given 是过去分词；由较早强变位词族延续并受北欧语音形式影响。'),
 'B2879':dict(words=['hold','held'],label='hold 与 held：拿着、保持与举办',note='hold → held → held；较早过去式 heold 与旧分词形式的历史不完全相同，现代过去分词后来也采用 held。'),
 'B2550':dict(words=['know','knew','known'],label='know、knew、known 的常用变位',note='knew 接较早过去式 cneow；know、knew、known 里的 k 在现代常见读音中不发音。'),
}
W('told','英 /təʊld/；美 /toʊld/','告诉了、讲述了；tell 的过去式、过去分词',
 'tell 的事发生在过去，或某人已经被告知，就常用 told。告诉的内容可以是消息、故事，也可以是要求别人做什么。',
 '接古英语 tellan 的过去式 tealde、分词 teald 等旧形式，经过中古英语语音、拼写变化形成 told。tell 还曾广泛表示计数。',
 [['古英语 tellan → tealde、teald 等','讲述、计数动词的旧过去形式'],['现代 tell → told → told','告诉、讲述的过去与过去分词；all told 总计']],
 'told me the news 告诉了我消息；was told 被告知；told someone to wait 叫某人等；all told 总共。',
 'I’ve told you；she told a story。','told someone something 常直接接人，said something to someone 则用另一种结构。told me 不能一律照中文改成 told to me。',
 ('She told me the news yesterday.','她昨天把消息告诉了我。'),('I was told to wait outside.','有人叫我在外面等。'),('There were twelve people, all told.','总共十二个人。'),sources=['https://www.etymonline.com/word/told','https://en.wiktionary.org/wiki/told#English'])
W('took','/tʊk/','拿了、带走了、采取了；take 的过去式',
 '把 take 的拿取、搭乘、花费、采取等意思放进过去。took 本身主要改变时间，不会把 take 变成另一个动作。',
 '延续较早 take 词族的变位；晚期古英语 tacan 有过去形式 toc，北欧语 taka 也有对应 tok。现代 took 保留不同元音的过去形式。',
 [['较早北欧、英语 take 词族与过去形式','taka、tacan 与 tok、toc 等对应'],['现代 take → took → taken','过去式 took；过去分词 taken']],
 'took the bus 搭了公共汽车；took a photo 拍了照；took a long time 花了很长时间；took advice 采纳了建议。',
 'took a break；took the bag home。','一般过去用 took，完成时用 have taken。took 的 oo 读 /ʊ/，不同于 food 的 /uː/。',
 ('We took the bus to the museum.','我们坐公共汽车去了博物馆。'),('The repair took longer than expected.','维修花的时间比预计更长。'),sources=['https://www.etymonline.com/word/took','https://en.wiktionary.org/wiki/took#English'])
W('came','/keɪm/','来了、到达了、出现了；come 的过去式',
 'come 的来到、出现放在过去：人来了，雨来了，办法也可能 came to mind 突然出现在脑中。',
 '接中古英语 cam、came 等过去形式；come 所属旧强变位词族有古英语 cuman 等，现代 came 的形成也常联系北欧语过去形式的影响。',
 [['较早 come 的强变位词族 → 中古英语 cam 等','来到、到达的过去形式'],['现代 come → came → come','过去用 came；过去分词仍用 come']],
 'came home 回家了；came to a stop 停了下来；came to mind 想到了；came across something 偶然遇见、发现。',
 'came back yesterday；an idea came to me。','一般过去是 came，have、has 后的过去分词是 come：She came yesterday；She has come back。',
 ('She came home before dinner.','她晚饭前回到了家。'),('A better idea came to mind later.','后来我想到了一个更好的办法。'),sources=['https://www.etymonline.com/word/came','https://en.wiktionary.org/wiki/came#English'])
W('went','/went/','去了、走了；进入某种状态；go 的过去式',
 'go 的过去形式长得很不一样，是因为它借用了另一个动词的旧过去式。意思仍接 go：去了某地，事情进行得怎样。',
 'went 原来是 wend 转向、行进的过去形式，经中古英语变化后逐渐接替 go 的旧过去式。是两条旧词史汇成一套变位，不是把 go 的元音改出来。',
 [['wend 的旧过去式 wende、wente → went','转向、行进的过去'],['went 成为 go 的标准过去式','现代 go → went → gone']],
 'went to school 去上学了；went wrong 出了问题；went well 进行得顺利；went quiet 安静下来了。',
 'went home；everything went well。','went 是过去式，gone 是过去分词：I went there；I have gone there。现代 wend 的常见过去式则是 wended。',
 ('We went to the park after lunch.','午饭后，我们去了公园。'),('The presentation went well.','展示进行得很顺利。'),sources=['https://www.etymonline.com/word/went','https://en.wiktionary.org/wiki/went#English'])
W('saw','英 /sɔː/；美 /sɔː/ 或 /sɑː/','看见了、见到了〔see 的过去式〕；锯〔另源名词、动词〕',
 'I saw 是我看见了；a saw 则是一把锯。相同读音和拼写装着两条常用历史，先看句子里的位置。',
 '看见义接 see 的旧强变位，古英语有 seah、sawon 等过去形式。锯的名词另接古英语 sagu 切割工具，后也发展出锯开的动词。',
 [['see 的旧过去形式 → saw','看见了、见到了'],['古英语工具名 sagu → saw','锯；再作动词表示用锯切割']],
 'saw a bird 看见了一只鸟；saw the doctor 看过医生、就诊过；a hand saw 手锯；saw a board 锯木板。',
 'see → saw → seen；saw → sawed → sawn 或 sawed。','看见的完成时是 have seen；锯开则用 have sawn、have sawed 等工具动词形式。saw 在两套变位中扮演的角色不同。',
 ('I saw a fox near the river.','我在河边看见了一只狐狸。'),('She used a small saw to cut the wood.','她用一把小锯切木头。'),sources=['https://www.etymonline.com/word/saw','https://www.etymonline.com/word/see','https://en.wiktionary.org/wiki/saw#English'])
W('heard','英 /hɜːd/；美 /hɜːrd/','听见了、听说了；hear 的过去式、过去分词',
 '耳朵听到了声音，或消息已经传到你这里，都可能用 heard。I’ve heard of it 是我听说过它，不一定亲耳听过某种声音。',
 '较早英语已有 herde 等过去形式，与 hear 的旧听觉动词相连。现代元音和拼写经历变化，不能按 hear 的读音直接加 d 来念。',
 [['旧英语 hear 词族与 herde 等过去形式','听见、获知的过去表达'],['现代 hear → heard → heard','过去式、过去分词相同']],
 'heard a noise 听到声响；heard the news 听说消息；heard of someone 听说过某人；heard from someone 收到某人的消息。',
 'I’ve heard about it；she heard him sing。','heard of 是听说过，heard from 是收到对方联系、消息。heard 和 herd 畜群在常见发音中同音。',
 ('I heard a strange noise outside.','我听到外面有奇怪的声响。'),('Have you heard from her recently?','你最近收到她的消息了吗？'),sources=['https://www.etymonline.com/word/heard','https://en.wiktionary.org/wiki/heard#English'])
W('gave','/ɡeɪv/','给了、带来了、作出了；give 的过去式',
 'give 放进过去就是 gave：给了一本书，作出一个回答，或者 gave up 放弃了。动作的具体意思由搭配决定。',
 'give 的旧强变位词族有古英语 giefan、过去式 geaf 等，英语词形后来也受北欧相关形式影响。现代过去式以 gave 延续。',
 [['古英语 giefan、geaf 等及北欧相关材料','给予与相应过去形式'],['现代 give → gave → given','过去 gave；过去分词 given']],
 'gave me a book 给了我一本书；gave an answer 作了回答；gave a speech 发表演讲；gave up 放弃了。',
 'gave permission；gave the child a hand。','gave 是过去式；given 是过去分词：She gave me a book；She has given me a book。不要把完成时直接换成 have gave。',
 ('He gave me a useful piece of advice.','他给了我一条有用的建议。'),('She gave up trying to open the jar.','她放弃了继续拧开罐子。'),sources=['https://www.etymonline.com/word/gave','https://en.wiktionary.org/wiki/gave#English'])
W('held','/held/','拿住了、保持了、举办了；hold 的过去式、过去分词',
 '拿在手里的东西没松开，会议被组织举行，某种看法被坚持着，都是 hold 的不同用法在过去或完成结构中出现。',
 '旧英语 hold 词族有过去式 heold 等；现代 held 接此发展。较早分词 healden、holden 等后来在普通变位中也由 held 取代。',
 [['旧英语 healdan、heold 等 → 后来 held','握持、保持的旧过去形式'],['现代 hold → held → held','过去与过去分词采用同形 held']],
 'held her hand 握着她的手；held a meeting 举行了会议；was held 被举行、被扣住等；held the view 持有某种看法。',
 'held in the hall；held the door open。','held 接的是 hold 的动词词族。was held 常是被动句，具体是举行还是扣留，必须看主语、地点和上下文。',
 ('She held the baby carefully.','她小心地抱着婴儿。'),('The meeting was held in the library.','会议在图书馆举行。'),sources=['https://www.etymonline.com/word/held','https://en.wiktionary.org/wiki/held#English'])
W('knew','英 /njuː/；美 /nuː/','知道、认识过、会〔过去时〕；know 的过去式',
 '在过去某个时间已经知道一件事、认识一个人、会做某事，就常用 knew。它不单独保证这份知识今天是否还在。',
 '接古英语 cnawan 的过去式 cneow 等旧强变位形式，经中古英语延续。现代开头 k 不发音，部分口音还省去 /j/。',
 [['古英语 cnawan、cneow 等','知道、认识与相应过去形式'],['现代 know → knew → known','过去 knew；过去分词 known']],
 'knew the answer 知道答案；knew her well 很了解她；knew how to do 会做某事；I knew it! 我就知道！',
 'already knew；knew what to say。','knew 是过去式，known 是过去分词。knew 与 new 新的在相同口音中常同音，但不是同一个词族。',
 ('I knew the answer but stayed quiet.','我知道答案，却没有出声。'),('She knew how to repair the bike.','她那时会修自行车。'),sources=['https://www.etymonline.com/word/knew','https://en.wiktionary.org/wiki/knew#English'])
def extend_lessons():
    extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
    save('continuation_20261030_tv',ROOTS,WORDS)
    extend_lessons()
