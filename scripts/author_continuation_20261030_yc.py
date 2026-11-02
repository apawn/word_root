"""Useful number plurals, grouped quantities and fractions."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'A1781':dict(words=['hundred','hundreds','thousand','thousands','billion','billions','fifth','fifths','tenth','tenths'],label='数词词族补读：若干百、千、大数与分数',note='先接已有数词基本形式，再看 -s 数量表达；本组同时与原有序数词、分数词讲解相邻。'),
 'C0739':dict(words=['million','millions'],label='million → millions：一百万与数以百万计',note='mille 一千经意大利语加大形式、法语借入，现代以一百万为一个计数单位。'),
 'C0349':dict(words=['dozen','dozens'],label='dozen → dozens：十二一组与许多',note='duodecim 的二加十，经法语十二一组词进入英语。'),
 'B3367':dict(words=['score','scores'],label='score → scores：分数、总谱与若干个二十',note='刻记、计数词族还保留一组二十的数量用法；scores of 常泛指数十、许多。'),
 'C0957':dict(words=['pair','pairs'],label='pair → pairs：相称的一对',note='相等、相配的拉丁词族经法语进入英语；一对通常按两个成组。'),
 'C0253':dict(words=['couple','couples'],label='couple → couples：连成一对的人或物',note='纽带词族形成名词一对与动词连接，英语名词动词分别有法语借入历史。'),
 'B2576':dict(words=['third','thirds'],label='three／third → thirds：第三与三等份',note='third 的序数形式有古老历史，分数名词可数一份、两份。'),
}
W('hundreds','/ˈhʌndrədz/','数百；几百个；百位数量〔hundred 的复数名词用法〕',
 '把一百当成一组，再说有许多这样的组，就是 hundreds；hundreds of 常用来表达数百、成百上千的一大批。',
 'hundred + -s，/d/ 后读 /z/。hundred 继承古英语 hundred 的日耳曼语计数词族；这里把百当作一个可数数量单位。',
 [['古英语 hundred → 中古英语、英语 hundred','现代常用数量单位一百'],['hundred + -s → hundreds','若干个百；hundreds of 数百个']],
 'hundreds of people 数百人；in the hundreds 数量在几百；hundreds and thousands 成百上千〔按语境〕。',
 'hundreds of books；several hundred people〔数量词后用 hundred〕。','two hundred people、several hundred people 中 hundred 通常不加 s，也不加 of；hundreds of people 则用复数和 of 表概数。不是看到中文几百就总写 hundreds。',
 ('Hundreds of people came to the festival.','数百人来到节庆活动现场。'),('The number of old photographs is now in the hundreds.','老照片的数量如今已经有几百张了。'),sources=['https://en.wiktionary.org/wiki/hundreds#English','https://en.wiktionary.org/wiki/hundred#English'])
W('thousands','/ˈθaʊzəndz/','数千；千位数量〔thousand 的复数名词用法〕',
 '以一千为一组来数，有许多组，就是 thousands；thousands of 常说成千上万的一大批，不要求报出精确数量。',
 'thousand + -s，/d/ 后读 /z/。thousand 接古英语 þūsend 等形式，经中古英语延续，是古老日耳曼语数词；复数表达数量组。',
 [['古英语 þūsend → 中古英语 → thousand','一千这一数量单位'],['thousand + -s → thousands','若干个千；成千上万']],
 'thousands of trees 数千棵树；tens of thousands 数以万计；in the thousands 数量达几千。',
 'thousands of visitors；three thousand visitors〔确数结构〕。','three thousand visitors 用 thousand 单数形式；thousands of visitors 用复数和 of 说概数。tens of thousands 是许多个万，字面上是许多个十千。',
 ('Thousands of trees were planted along the river.','河边种下了数千棵树。'),('The archive contains tens of thousands of letters.','档案馆里收藏着数以万计的信件。'),sources=['https://en.wiktionary.org/wiki/thousands#English','https://en.wiktionary.org/wiki/thousand#English'])
W('millions','/ˈmɪljənz/','数百万；百万位数量〔million 的复数名词用法〕',
 '以一百万为一份大数量来数，是 millions；millions of 常强调非常多，也可以在报道、统计里表达数百万。',
 'million + -s，/n/ 后读 /z/。million 经法语接意大利语 milione，较早是 mille 一千的加大形式，英语常用值为一百万；复数不改变基本单位大小。',
 [['拉丁 mille → 意大利 milione → 法语、英语 million','一千 → 加大数量名称 → 一百万'],['million + -s → millions','若干个百万；millions of 数百万个']],
 'millions of people 数百万人；millions of years 数百万年；in the millions 数量达几百万。',
 'several million people〔数量词后用 million〕；millions of stars。','two million、several million 后接具体对象时通常不加 s；millions of 则常说概数。中文一百万与英语 one million 对应，不能看到 milli- 的另一个用法就解释成千分之一。',
 ('The museum’s collection tells a story spanning millions of years.','博物馆的藏品讲述了跨越数百万年的历史。'),('The night sky seemed to contain millions of stars.','夜空里仿佛有数百万颗星星。'),sources=['https://en.wiktionary.org/wiki/millions#English','https://en.wiktionary.org/wiki/million#English'])
W('billions','/ˈbɪljənz/','数十亿；以十亿为单位的数量〔现代常用值〕',
 '现代通常把十亿当作一组来数，许多这样的组就是 billions。按单位算，一个 billion 等于一千个 million；不能只凭开头 bi- 二来直接算数值。',
 'billion + -s，/n/ 后读 /z/。billion 借法语，以 million 的后部与 bi- 构成；历史长数制中曾表示一百万的平方，现代英语常用十亿值，旧资料需看所用计数体系。',
 [['法语以 million 形式构成 billion → 英语 billion','较早大数名称，数值随长、短数制而不同'],['现代常用 billion：十亿；再加 -s → billions','数十亿；以十亿为单位的概数']],
 'billions of stars 数十亿颗星；billions of dollars 数十亿美元；in the billions 数量以十亿计。',
 'several billion〔数量词结构〕；billions of possible combinations。','现代常用 one billion = one thousand million = 十亿；历史资料可能用 long scale，把 billion 当一万亿。two billion 常不加 s，billions of 则是复数概数表达。',
 ('The computer compared billions of possible combinations.','计算机比较了数十亿种可能的组合。'),('The estimated cost ran into billions of dollars.','估算费用高达数十亿美元。'),sources=['https://en.wiktionary.org/wiki/billions#English','https://en.wiktionary.org/wiki/billion#English','https://www.merriam-webster.com/dictionary/billion'])
W('dozens','/ˈdʌzənz/','数十；许多；若干打〔dozen 的复数〕',
 '一打是十二个，多打合起来就是 dozens；日常的 dozens of 常泛指数十、很多，不一定真按十二个一组去点数。',
 'dozen + -s，/n/ 后读 /z/。dozen 经法语 dozaine 一组十二，较早 doze 十二接拉丁 duodecim，由 duo 二与 decem 十组成。',
 [['拉丁 duodecim → 法语 doze、dozaine → dozen','二加十 → 十二一组'],['dozen + -s → dozens','多打；泛指数十、许多']],
 'dozens of questions 数十个问题；dozens of times 许多次；several dozen eggs 几打鸡蛋；by the dozen 按打。',
 'dozens of people；three dozen flowers。','three dozen flowers 用 dozen 的普通数量形式；dozens of flowers 用复数和 of 表概数。dozens of times 常强调次数很多，未必给出精确的十二倍数。',
 ('She had dozens of questions about the project.','她对这个项目有一大堆问题。'),('We bought three dozen flowers for the event.','我们为活动买了三打花。'),sources=['https://en.wiktionary.org/wiki/dozens#English','https://en.wiktionary.org/wiki/dozen#English'])
W('scores','英 /skɔːz/；美 /skɔːrz/','分数；乐谱、总谱；数十、许多〔scores of〕；得分〔第三人称单数〕',
 '刻记用来记数量，发展出分数；一组二十也叫 a score，scores of 就常说数十、许多。把音乐各部分写在一起的总谱，则是另一个常见名词用法。',
 'score + -s，词尾读 /z/。score 的早期英语、古诺尔斯语材料与刻痕、刻记及计数相连；分数、二十这一数量用法和乐谱等在不同分支发展。',
 [['较早刻痕、刻记词族 → score','记数 → 分数；一组二十等'],['score + -s → scores','多个分数、乐谱；scores of 数十个；单数主语得分']],
 'exam scores 考试分数；musical scores 乐谱、总谱；scores of visitors 数十位访客；scores a goal 进球得分。',
 'compare the scores；scores of examples。','scores of 用来泛指许多时，不用精确算成某个二十倍数。考试的 scores 是分数，音乐的 scores 是记录演奏内容的谱，靠修饰词、语境区别。',
 ('The teacher compared the scores from the two tests.','老师比较了两次测验的分数。'),('Scores of visitors arrived before the gates opened.','大门开放前就来了数十位访客。'),('The library keeps the musical scores in a separate room.','图书馆把乐谱单独放在一间房里。'),sources=['https://en.wiktionary.org/wiki/scores#English','https://en.wiktionary.org/wiki/score#English'])
W('pairs','英 /peəz/；美 /perz/','一对对；几双；把……配对〔第三人称单数〕',
 '两个东西相配、一起算一组，就是 a pair；多组是 pairs。两只鞋是一双，一把剪刀也常按 a pair of scissors 来说。',
 'pair + -s，词尾读 /z/。pair 经法语 paire 接拉丁 paria 相等、相配的东西，这是 par 相等的中性复数形式；英语形成一对及配对动词用法。',
 [['拉丁 par、paria → 法语 paire → pair','相等、相配的东西 → 一对'],['pair + -s → pairs','多对、多双；单数主语配对']],
 'pairs of shoes 几双鞋；work in pairs 两人一组；pairs of scissors 几把剪刀；pairs A with B 把 A 与 B 配成一组。',
 'two pairs of socks；matching pairs。','a pair of shoes 是两只鞋合成的一双，two pairs 是两双。a pair of scissors 通常是一把剪刀，名称把两个相配的部分作为一组看待。',
 ('The students worked in pairs to solve the problem.','学生们两人一组解决问题。'),('She packed two pairs of socks for the trip.','她为旅途装了两双袜子。'),sources=['https://en.wiktionary.org/wiki/pairs#English','https://en.wiktionary.org/wiki/pair#English'])
W('couples','/ˈkʌpəlz/','几对人或物；情侣、夫妻〔复数〕；把……结合〔第三人称单数〕',
 '两个对象连成一组，是 couple 的一对；两个人以伴侣关系相连，常叫 a couple。多对就说 couples，动词也可表示把两种东西连接起来。',
 'couple + -s，/l/ 后读 /z/。名词经古法语 couple 接拉丁 cōpula 纽带，动词另经古法语 copler；两者同族，但英语有分别借入的记录。',
 [['拉丁 cōpula → 法语 couple／copler → 英语 couple','纽带、连接 → 一对；把……连在一起'],['couple + -s → couples','多对伴侣、人或物；单数主语结合']],
 'married couples 已婚夫妇；young couples 年轻伴侣；couples creativity with discipline 把创造力与严谨结合。',
 'several couples dancing；couples the two systems。','a couple of things 常说两件或几件东西，要看语境；couples 本身常说几对伴侣。pairs 强调成组、相配，couples 在人物语境常带伴侣关系。',
 ('Several couples were dancing near the stage.','几对伴侣在舞台旁跳舞。'),('The design couples a simple shape with bright colours.','这个设计把简单形状与鲜亮色彩结合起来。'),sources=['https://en.wiktionary.org/wiki/couples#English','https://en.wiktionary.org/wiki/couple#English'])
W('thirds','英 /θɜːdz/；美 /θɜːrdz/','三分之一的若干份；三等份〔third 的分数复数〕',
 '把一个整体平均分成三份，一份是 a third，两份是 two thirds。这个词既说明分成几份，也能把其中的份数数出来。',
 'third 作分数名词，加 -s，/d/ 后读 /z/。third 继承古英语 þridda，经中古英语延续，与 three 有历史对应；第三的顺序词也用于三分之一。',
 [['古英语 þridda → 中古英语 → third','第三；英语另用为三分之一'],['third 分数名词 + -s → thirds','多个三分之一；按三等份分']],
 'two thirds 三分之二；divide into thirds 分成三等份；two thirds of the class 全班的三分之二。',
 'cut into thirds；nearly two thirds。','分子是一时常用单数，如 one third；分子大于一时常用复数，如 two thirds。two thirds of 后的实际对象决定句子谓语，如 people are、water is。',
 ('She folded the paper into thirds.','她把纸折成了三等份。'),('Two thirds of the students chose the morning class.','三分之二的学生选择了上午的课。'),sources=['https://en.wiktionary.org/wiki/thirds#English','https://en.wiktionary.org/wiki/third#English'])
W('fifths','/fɪfθs/','五分之一的若干份；五等份〔fifth 的分数复数〕',
 '把整体平均分成五份，一份叫 a fifth；拿其中两份，就是 two fifths，也就是五分之二。',
 'fifth 分数名词加 -s，常见读音末尾连成 /fθs/。fifth 接古英语 fīfta 等旧序数形式，现代与 five 对应；five 到 fifth 的变化有历史来源。',
 [['古英语第五的旧形式 → 中古英语 → fifth','第五；英语分数用法五分之一'],['fifth + -s → fifths','多个五分之一；五等份']],
 'two fifths 五分之二；three fifths 五分之三；divide into fifths 分成五等份。',
 'three fifths of the total；cut into fifths。','one fifth 用单数，two fifths、three fifths 用复数。fifths 中 th 通常仍读 /θ/，末尾辅音较密，慢读时先认清 fifth，再接 /s/。',
 ('Two fifths of the class chose the blue design.','全班有五分之二的人选择了蓝色设计。'),('Cut the chocolate into fifths.','把这块巧克力切成五等份。'),sources=['https://en.wiktionary.org/wiki/fifths#English','https://en.wiktionary.org/wiki/fifth#English'])
W('tenths','/tenθs/','十分之一的若干份；十等份〔tenth 的分数复数〕',
 '把一个整体平均分成十份，每一份是 a tenth；拿三份就是 three tenths，等于十分之三。小数点后一位就是按这种十分之一计数。',
 'tenth 分数名词加 -s，末尾 /nθs/ 连读。tenth 在中古英语中受 ten 类推形成；更早英语的第十有其他旧形式，现代清楚对应 ten 与 -th。',
 [['古英语、中古英语十的词族 → 中古英语 tenth','序数第十受 ten 影响重新形成'],['tenth 作分数名词 + -s → tenths','多个十分之一；十等份']],
 'three tenths 十分之三；tenths of a second 零点几秒、若干十分之一秒；the tenths place 小数点后第一位。',
 'measured in tenths；seven tenths of the total。','three tenths = 0.3；one tenth = 0.1。tenths place 是小数点后一位，tens place 则是整数十位，不能只看两者都含 ten。',
 ('The timer measures tenths of a second.','这个计时器能测到十分之一秒。'),('Three tenths of the total was left over.','总量还剩十分之三。'),sources=['https://en.wiktionary.org/wiki/tenths#English','https://en.wiktionary.org/wiki/tenth#English'])
def extend_lessons():
 extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_yc',ROOTS,WORDS)
 extend_lessons()
