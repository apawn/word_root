"""Further common irregular verbs, including changes by analogy."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'B2999':dict(words=['teach','taught'],label='teach 与 taught：指给人看、教会的过去',note='teach → taught → taught；taught 承接古英语 tæhte、tæht 等旧过去材料。'),
 'B3002':dict(words=['throw','threw','thrown'],label='throw、threw、thrown：甩出与举办',note='threw /θruː/ 是过去式；thrown 是过去分词。旧词有扭转义，后有投掷、举办等现代分支。'),
 'B3008':dict(words=['wear','wore','worn'],label='wear 的过去形式如何改换模式',note='wear 较早有 wered 等带词尾形式，后来受 bear、tear 等相近读音词的变位模式影响，形成现代 wore、worn。'),
 'B2840':dict(words=['choose','chose','chosen'],label='choose、chose、chosen 的常见分工',note='choose /tʃuːz/ → chose /tʃəʊz/ 或 /tʃoʊz/ → chosen；过去式与原形元音不同。'),
 'B2827':dict(words=['blow','blew','blown'],label='吹动的三种形式 blow、blew、blown',note='blew /bluː/ 是过去式；blown 是过去分词，保留旧分词材料。'),
 'B2856':dict(words=['feed','fed'],label='feed 与 fed：喂给、持续供给与够了',note='feed → fed → fed；fed up 从给得太满、已经够了的感觉转到厌烦、受够。'),
 'B2859':dict(words=['fight','fought'],label='fight 与 fought：打斗、抵抗、争取',note='fight → fought → fought；gh 在现代常见读音里不单独发音，保留较早拼写历史。'),
 'B2966':dict(words=['seek','sought'],label='seek 与 sought：主动寻求的过去',note='seek → sought → sought；sought 接古英语 sohte 等旧过去形式，与现代原形有较大字面差别。'),
 'B2428':dict(words=['deal','dealt'],label='deal 与 dealt：分发和应对',note='deal → dealt → dealt；长元音 /iː/ 与短元音 /e/ 连着记，dealt with 是处理、应对了。'),
 'B2845':dict(words=['dig','dug'],label='dig 与 dug：后起的元音换形',note='dug 在英语中是后来形成的强变位式形式，不能把它说成从古英语原封不动留下；现代 dig → dug → dug 已成为标准常用变位。'),
}
W('taught','英 /tɔːt/；美 /tɔːt/ 或 /tɑːt/','教过、教会了、被教；teach 的过去式、过去分词',
 '把做法展示、讲给别人，让别人学会。过去发生的教导用 taught；一次经历也可能 taught me a lesson 让我得到教训。',
 'teach 接古英语 tæcan 展示、指出、教导，过去式有 tæhte、分词 tæht 等；经后续音变、拼写变化发展成 taught。',
 [['古英语 tæcan → tæhte、tæht 等','指出、教导及相应旧过去形式'],['现代 teach → taught → taught','教过、教会；被教导']],
 'taught me English 教过我英语；taught her to cook 教会她做饭；was taught 被教导；taught me a lesson 让我得到教训。',
 'taught at a school；taught by experience。','teach 是教，learn 是学：She taught me；I learned from her。过去 taught 不是 learned 的另一种拼写，两边参与者视角不同。',
 ('My grandfather taught me to ride a bike.','我爷爷教会了我骑自行车。'),('The mistake taught her to check her work carefully.','那次失误让她学会仔细检查自己的工作。'),sources=['https://www.etymonline.com/word/taught','https://en.wiktionary.org/wiki/taught#English'])
W('threw','/θruː/','扔了、抛出了；举办了等；throw 的过去式',
 '把球甩出去是 threw；threw a party 则是办了场聚会。过去形式不变，具体动作跟着搭配走。',
 'throw 接古英语 þrawan 扭、转等，过去式有 þreow；现代 threw 承接旧过去材料。投掷义后来发展，甩动的画面可帮助理解。',
 [['古英语 þrawan、þreow 等','扭转及相应过去形式；后来有投掷义'],['现代 throw → threw → thrown','过去 threw；过去分词 thrown']],
 'threw the ball 扔了球；threw away the box 扔掉箱子；threw a party 举办聚会；threw up 呕吐了。',
 'threw it into the bin；threw the door open。','threw 与 through 常同音，前者是动作过去式，后者常作介词、副词。threw the ball through the window 中二者各有作用。',
 ('He threw the ball to his sister.','他把球扔给了妹妹。'),('They threw a small party for her birthday.','他们为她的生日办了个小聚会。'),sources=['https://www.etymonline.com/word/throw','https://en.wiktionary.org/wiki/threw#English'])
W('wore','英 /wɔː/；美 /wɔːr/','穿着、戴着；消耗、磨损了；wear 的过去式',
 '过去身上穿着什么、戴着什么，用 wore；一段消耗人的经历 wore someone out，则说把人累坏了。',
 'wear 接古英语 werian 穿、覆盖等。较早 wered 等过去形式，后来逐渐被按 bear、tear 等模式形成的 wore、worn 替代，是类推改变变位的例子。',
 [['较早 wear 的 wered 等形式','穿戴、使用的旧过去表达'],['受相似词变位模式影响 → wore、worn','形成现代 wear → wore → worn']],
 'wore a coat 穿着外套；wore glasses 戴着眼镜；wore a smile 面带微笑；wore me out 把我累坏了。',
 'wore it every day；wore down the surface。','wore 描写过去穿戴着的状态，put on 描写穿上的动作；worn 是过去分词，也常指用旧、磨损的状态。',
 ('She wore a blue coat to the meeting.','她穿着蓝色外套去参加会议。'),('The long journey wore us out.','长途旅行把我们累坏了。'),sources=['https://www.etymonline.com/word/wear','https://en.wiktionary.org/wiki/wore#English'])
W('chose','英 /tʃəʊz/；美 /tʃoʊz/','选择了、决定了；choose 的过去式',
 '几个可能摆在面前，过去选中了其中一个，或者决定去做一件事，就是 chose。',
 'choose 接古英语 ceosan 选择、尝试等，过去式有 ceas；经中古英语和后续音变成为 chose，分词则是 chosen。',
 [['古英语 ceosan、ceas 等','选择、试取及对应过去形式'],['现代 choose → chose → chosen','一般过去 chose；过去分词 chosen']],
 'chose a book 选了本书；chose to stay 决定留下；chose between two options 在两个选项间作了选择。',
 'chose carefully；chose the shorter route。','choose 的元音是 /uː/，chose 是 /əʊ/ 或 /oʊ/。chose 不是名词 choice 的拼写变体，choice 是选择行为、选项等名词。',
 ('She chose the seat by the window.','她选了靠窗的座位。'),('He chose to stay and help.','他决定留下来帮忙。'),sources=['https://www.etymonline.com/word/choose','https://en.wiktionary.org/wiki/chose#English'])
W('blew','/bluː/','吹了、刮了、吹动了；blow 的过去式',
 '风把东西吹起来，人吹灭蜡烛，都可用 blew。口语 blew a chance 又说把机会搞砸、浪费掉。',
 '接古英语 blawan 的过去式 bleow 等旧强变位形式，经中古英语延续为 blew。取吹气、气流移动这一动词分支。',
 [['古英语 blawan、bleow 等','吹、使气流移动及其过去形式'],['现代 blow → blew → blown','一般过去 blew；过去分词 blown']],
 'blew away the leaves 把叶子吹走；blew out a candle 吹灭蜡烛；blew his chance 搞砸机会；blew my mind 让我大为震撼。',
 'the wind blew；blew a whistle。','blew 与 blue 蓝色常同音；blew 是过去式，blue 是颜色词。吹动的完成表达用 have blown。',
 ('The wind blew the door shut.','风把门吹得关上了。'),('She blew out the candles.','她吹灭了蜡烛。'),sources=['https://www.etymonline.com/word/blow','https://en.wiktionary.org/wiki/blew#English'])
W('fed','/fed/','喂了、供给了；feed 的过去式、过去分词',
 '把食物送给动物、把材料持续送进系统，都是 feed 的画面。fed up 则像已经被塞够了，转成受够了、很烦。',
 'feed 接古英语 fedan 等滋养、供食词族，fed 承接其过去形式变化。fed up 较早可说喂足，后来比喻已经受够、厌烦。',
 [['较早 feed 的滋养、供给词族及过去形式','喂食；持续供给'],['现代 fed 与 fed up','过去、过去分词；已经受够的口语表达']],
 'fed the cat 喂了猫；fed data into a system 把数据送入系统；be fed up with something 受够某事。',
 'feed → fed → fed；fed up with waiting。','fed 是喂、供给的动词形式，fed up 是厌烦的固定表达。单说被喂 fed 不自动表示受够。',
 ('She fed the cat before leaving.','离开前，她喂了猫。'),('I’m fed up with waiting for the bus.','我等公共汽车已经等烦了。'),sources=['https://www.etymonline.com/word/feed','https://www.etymonline.com/word/fed','https://en.wiktionary.org/wiki/fed#English'])
W('fought','英 /fɔːt/；美 /fɔːt/ 或 /fɑːt/','打过、战斗过、抗争过；fight 的过去式、过去分词',
 '动手打斗、抵抗困难，或努力为某个目标争取，放在过去都可能是 fought。关键是存在阻力，需要与之较劲。',
 'fight 接古英语 feohtan，过去式有 feaht、分词 fohten。现代 fought 保留旧变位材料，gh 记录较早辅音的拼写，常见读音中已不发。',
 [['古英语 feohtan、feaht、fohten 等','打斗、抗争及其旧变位'],['现代 fight → fought → fought','过去与分词同形']],
 'fought a battle 打过一场仗；fought against the plan 反对过计划；fought for better conditions 为改善条件而争取。',
 'fought back；fought hard for something。','fought 不必是身体打架，fight for 可说争取目标，fight against 可说抵抗对象。for 和 against 常帮助判断方向。',
 ('They fought hard for better working conditions.','他们为改善工作条件努力争取。'),('The firefighters fought the fire through the night.','消防员们整夜扑救大火。'),sources=['https://www.etymonline.com/word/fight','https://en.wiktionary.org/wiki/fought#English'])
W('sought','英 /sɔːt/；美 /sɔːt/ 或 /sɑːt/','寻找了、寻求了、设法争取；seek 的过去式、过去分词',
 '目标还没到手，人主动去找、去争取。sought help 就是寻求帮助，不表示一定已经获得帮助。',
 '接古英语 secan 等寻找词族的过去式 sohte；原形与过去形式都经历了语音、方言等变化，现代 seek 与 sought 字面差别较大。',
 [['旧寻找动词 secan、sohte 等','寻找及对应过去形式'],['现代 seek → sought → sought','寻找、寻求的过去与过去分词']],
 'sought help 寻求帮助；sought advice 征求建议；sought to improve 设法改善；was sought 被寻找、被寻求。',
 'sought an explanation；sought permission。','seek、sought 常比 look for 稍正式；sought 指努力寻求，found 才明确表示找到了。不要把寻求自动译成获得。',
 ('She sought advice from a trusted friend.','她向一位信任的朋友征求建议。'),('The team sought to improve the design.','团队设法改进设计。'),sources=['https://www.etymonline.com/word/sought','https://en.wiktionary.org/wiki/sought#English'])
W('dealt','/delt/','分发了；处理了、应对了；deal 的过去式、过去分词',
 '牌一张张分出去是 dealt；事情摆到面前，一件件去处理，是 dealt with。要连着后面的介词看。',
 'deal 接古英语 dælan 分开、分配等，现代 dealt 承接旧过去形式与后续语音变化。应对义接 deal with 的交涉、处理分支。',
 [['古英语 dælan 等分配词族及过去形式','分发、与人打交道'],['现代 deal → dealt → dealt','分发；dealt with 处理、应对']],
 'dealt the cards 发了牌；dealt with the problem 处理了问题；dealt a blow 给予一击。',
 'have dealt with this before；dealt fairly with someone。','deal /diːl/ 与 dealt /delt/ 的元音不同。dealt with 是应对某事，dealt something out 常说把某物分发出去。',
 ('He dealt the cards to the players.','他把牌发给了玩家。'),('We dealt with the problem immediately.','我们立即处理了那个问题。'),sources=['https://www.etymonline.com/word/deal','https://en.wiktionary.org/wiki/dealt#English'])
W('dug','/dʌɡ/','挖了、挖出；深入查找过；dig 的过去式、过去分词',
 '先把表层刨开，向下找，是真挖土；翻资料、追细节，也可以借这个深入挖掘的画面。',
 'dig 的更远来源未定，较早英语有 diggen 等。dug 是后来按元音换形模式发展出来的形式，逐渐成为现代标准的过去式、过去分词。',
 [['中古英语 diggen 等挖掘词及较早变位','挖开、挖出'],['后起 dug 形式 → 现代 dig → dug → dug','类推形成并固定的过去与分词']],
 'dug a hole 挖了洞；dug up an old letter 翻出了旧信；dug through the files 深入翻找文件；dug into the details 深查细节。',
 'dug in the garden；dug up useful information。','dug 的历史展示词形会类推改变，不能把所有不规则形式都当上古同一规则的遗迹。现代常用 dug，无须另造 digged 来套普通 -ed。',
 ('The dog dug a hole under the fence.','狗在围栏下面挖了一个洞。'),('She dug through the old files to find the receipt.','她翻遍旧文件，寻找那张收据。'),sources=['https://www.etymonline.com/word/dig','https://en.wiktionary.org/wiki/dug#English'])
def extend_lessons():
    extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
    save('continuation_20261030_tz',ROOTS,WORDS)
    extend_lessons()
