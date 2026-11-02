"""Frequent degree and time forms, with practical contrasts."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'B2731':dict(words=['bad','worse','worst'],label='bad 的不规则比较：worse 与 worst',note='现代 bad—worse—worst 配成一组，但 worse、worst 继承不同于 bad 的更早词干；不是给 bad 普通加后缀得到。'),
 'B3442':dict(words=['great','greater','greatest','greatly'],label='great：大小、程度、成就的比较和方式',note='great + -er／-est 形成比较、最高程度，great + -ly 形成副词；greatly 常修饰受影响、改变、感激等动词或分词，不能四处替换 very。'),
 'B3097':dict(words=['old','older','oldest','elder','eldest'],label='old 的两套保留形式',note='older、oldest 是普通比较词形，elder、eldest 保留更早变元音的历史，现代常用于家庭年龄关系等特定范围。'),
 'A1740':dict(words=['early','earlier','earliest'],label='early：带有旧 -ly 材料的形容词、副词及其比较',note='early 本身有较早英语早、早早地的历史，现代表比较时 y 换 i 接 -er／-est；不能把所有 -ly 形式都当只能作副词。'),
 'B3907':dict(words=['late','later','latest','last'],label='latest：时间上最靠后与最新',note='latest 对应 late 的最高级，the latest news 为最近传来的消息；at the latest 则说最晚限度，last 通常突出末尾、最后或上一个。'),
}
W('worst','英 /wɜːst/；美 /wɝːst/','最坏的、最差的；最糟地；最坏情况',
 '把几种情况从好到坏排开，worst 在最坏那头。the worst part 是最糟的一部分；at worst 是把可能的最坏边界拿出来说。',
 '继承古英语 wierrest、wyrst 等最高级词形，经中古英语发展。现代与 bad、ill 的比较系统配合，和 worse 同族，不来自给 bad 直接加 -est。',
 [['古英语 wierrest／wyrst → 中古英语相应形式','最坏、程度最不利的'],['现代 bad／ill—worse—worst 的配合','不规则比较系统中的最高程度']],
 'the worst day 最糟的一天；at worst 最坏情况下；the worst is over 最困难的阶段过去了；worst of all 最糟的是。',
 'my worst fear；the worst possible outcome。','worse 是更差，worst 是最差：This is worse than before；This is the worst so far。不要把两词都只背成糟糕。',
 ('This is the worst storm we have had this year.','这是今年我们遇到的最严重的一场暴风雨。'),('At worst, we will have to wait until Monday.','最坏也就是我们得等到星期一。'),sources=['https://www.etymonline.com/word/worst','https://en.wiktionary.org/wiki/worst#English'])
W('greater','英 /ˈɡreɪtə/；美 /ˈɡreɪtər/','更大的；程度更高的；Greater：大都市及周边范围的',
 '原来投入一份注意，现在投入更多，叫 greater attention；把一座城市与周边一起看，地名里也可加 Greater。',
 'great + 比较级 -er，承接 great 从大、粗壮到重要、程度高的历史。这里 -er 比较性质，不表示做某事的人。',
 [['great','大的；程度、重要性或成就显著的'],['great + -er → greater','相对更大、更显著；地名中的较大范围']],
 'greater care 更多照料、更谨慎；greater confidence 更强信心；greater than 大于；Greater London 大伦敦。',
 'a greater risk；a greater number of people。','greater 常比较程度、数量、重要性，不总评价更好。a greater problem 是更大的问题，通常不是更好的问题；物理大与程度大要按名词理解。',
 ('The new role gives her greater responsibility.','新职位让她承担了更大的责任。'),('We need greater care when handling these objects.','处理这些物品时，我们需要更加小心。'))
W('greatest','/ˈɡreɪtɪst/','最大的；程度最高的；最伟大的',
 '把某一范围里所有对象摆开，程度、影响或成就最突出的那个，就是 greatest。量的是哪一项，要看后面的名词。',
 'great + -est，形成最高级。great 的大小、重要性、成就等不同分支都能进入比较，并非所有 greatest 都只是在赞美。',
 [['great','大的、显著的、伟大的等'],['great + -est → greatest','在某一范围达到最高程度']],
 'the greatest difficulty 最大困难；the greatest number 最多数量；her greatest achievement 她最大的成就；one of the greatest ... 最……之一。',
 'the greatest challenge；the greatest possible care。','greatest 说最大程度或最突出，best 说最好。greatest risk 是最大的风险，不是最好的风险；greatest writer 才通常含成就评价。',
 ('Time is our greatest challenge on this project.','时间是这个项目最大的难题。'),('She regards the book as her greatest achievement.','她把这本书视为自己最大的成就。'))
W('greatly','/ˈɡreɪtli/','大大地、极大地；很、非常〔特定搭配〕',
 '不是只变了一点点，而是程度明显提高、减少或受到影响。greatly improved 就是大有改善。',
 'great + -ly，性质词形成副词；从程度大的这一支发展为在很大程度上。它有自己的搭配范围，不是所有中文很都能用 greatly。',
 [['great 的程度义','大、显著'],['great + -ly → greatly','在很大程度上；强烈、显著地']],
 'greatly improve 大有改善；greatly reduce 大幅降低；greatly appreciate 非常感激、重视；be greatly affected 受到很大影响。',
 'greatly increased；greatly admired。','常说 greatly improved、greatly appreciated；普通说很好用 very good，不说 greatly good。greatly 的搭配比 very 窄，不能逐字替换。',
 ('The new lighting greatly improved visibility.','新照明大大改善了能见度。'),('Your help is greatly appreciated.','非常感谢你的帮助。'))
W('older','英 /ˈəʊldə/；美 /ˈoʊldər/','年纪更大的；更旧的、年代更早的',
 '两个人比较谁出生得早，两件东西比较谁存在得久，都可以用 older。比较的重点是年龄或年代，不是先评价好坏。',
 'old + -er，现代普通比较级。较早英语还保留 elder 那套变元音形式，但 older 的现代适用范围更广，可说人、建筑、机器等。',
 [['old','存在已久；年老、旧的'],['old + -er → older','相对年龄更大、存在更久']],
 'an older brother 哥哥；an older building 更老的建筑；older than someone 比某人年长；as you get older 随着年龄增长。',
 'older people；an older version。','older 可用于人和物，也可接 than。elder 常限于家庭年长关系等用法；my older sister、my elder sister 都可说姐姐，而 older than me 是普通比较结构。',
 ('My sister is three years older than I am.','我姐姐比我大三岁。'),('The older version still works on this computer.','旧版本在这台电脑上仍能运行。'))
W('oldest','英 /ˈəʊldɪst/；美 /ˈoʊldɪst/','最年长的；最古老的、存在最久的',
 '在这一组里谁出生最早、哪栋建筑存在最久，就用 oldest。比较范围决定它具体有多老。',
 'old + -est，形成普通最高级。和较早变元音形式 eldest 相比，oldest 现代适用范围更广，既可说家庭成员，也可说物品、建筑或记录。',
 [['old → older','存在已久 → 相对更久'],['old + -est → oldest','在指定范围内年龄、年代最早']],
 'the oldest child 年龄最大的孩子；the oldest building 最古老的建筑；one of the oldest ... 最古老的……之一；the oldest known example 目前已知最早的实例。',
 'the oldest member；the oldest surviving copy。','oldest 不要求对象已经非常老：三个两三岁的孩子里也有 the oldest。eldest 更常用于同一家庭的孩子等关系，不能随意说 the eldest building。',
 ('This is the oldest building in the village.','这是村里年代最久的建筑。'),('The oldest of the three children is only six.','三个孩子中最大的才六岁。'))
W('eldest','/ˈeldɪst/','最年长的；多指同一家庭中年龄最大的孩子',
 '几个兄弟姐妹中，排年龄第一、出生最早的那个，是 the eldest。它突出家庭里的年长次序。',
 '保留 old 较早的最高级材料与变元音历史，经中古英语 eldeste 等形式发展。与 elder 同套，不是 elder 这个长者名词再任意去 r 加 st。',
 [['旧英语 old 的变元音比较、最高级材料','年长、最年长'],['中古英语 eldeste → eldest','现代多用于家庭成员的年龄次序']],
 'the eldest son 长子；the eldest daughter 长女；her eldest child 她年龄最大的孩子；the eldest of three 三人中最年长的。',
 'my eldest brother；the eldest in the family。','eldest 的范围通常比 oldest 窄，尤其常说家庭成员。eldest son 是儿子中最年长者，不一定是所有孩子中最年长者；最年长的孩子才是 eldest child。',
 ('Her eldest daughter lives abroad.','她的长女住在国外。'),('He is the eldest of four children.','他是四个孩子中年龄最大的。'),sources=['https://www.etymonline.com/word/elder','https://en.wiktionary.org/wiki/eldest#English'])
W('earlier','英 /ˈɜːliə/；美 /ˈɝːliər/','更早的；更早地；先前、早些时候',
 '时间线上的位置往前移，是 earlier；与眼下这个时刻比，刚才或此前某时也可以只说 earlier。',
 'early 词末 y 换 i 加 -er。early 本身继承较早英语早、早早地的词形，现代既作形容词也作副词，所以 earlier 也有两种功能。',
 [['early','早的；早地'],['early → earlier','相对更早；从眼下回看先前']],
 'an earlier train 更早一班火车；earlier than expected 比预期早；earlier today 今天早些时候；as mentioned earlier 如前所述。',
 'a little earlier；an earlier version。','earlier today 不一定是昨天，而是今天此前某时。earlier 修饰名词是形容词：an earlier meeting；修饰 arrived 则是副词：arrived earlier。',
 ('Could we take an earlier train?','我们能不能坐更早一班火车？'),('I spoke to her earlier today.','我今天早些时候和她说过话。'))
W('earliest','英 /ˈɜːliɪst/；美 /ˈɝːliɪst/','最早的；最早地；最早限度',
 '几个可能时间摆开，落在最前面的那个是 earliest。at the earliest 则把边界说清：再早也早不过它。',
 'early 词末 y 换 i 加 -est，形成形容词、副词的最高程度。at the earliest 是固定时间边界表达，承接最早的性质。',
 [['early → earlier','早 → 更早'],['early → earliest','最早；at the earliest 最早限度']],
 'the earliest train 最早一班火车；my earliest memories 最早的记忆；Monday at the earliest 最早也要星期一；at your earliest convenience 在你方便时尽早，较正式。',
 'the earliest possible date；the earliest known record。','at the earliest 给出最早边界，事情可能更晚；at the latest 给最晚边界，事情应在那之前。两者方向相反。',
 ('The repairs will be finished on Friday at the earliest.','维修最早也要星期五才能完成。'),('We booked the earliest train of the day.','我们订了当天最早的一班火车。'))
W('latest','/ˈleɪtɪst/','最新的、最近的；最晚的；最新消息',
 '时间线上最靠近现在的新消息，是 latest news；安排未来时间时，允许最晚到几点，又是 at the latest。',
 'late 去词末 e 加 -est，最高级形态保留时间上最靠后的意思。随比较范围不同，可说最近出现、最新，或最晚限度；the latest 还可名词化指最新情况。',
 [['late → latest','时间靠后 → 最靠后'],['不同参照范围的现代用法','最近出现的；未来的最晚界限']],
 'the latest news 最新消息；the latest version 最新版本；by Friday at the latest 最晚星期五前；What’s the latest? 最新情况怎样？',
 'her latest book；the latest developments。','latest 通常说目前最新，last 常说最后一个、上一个。her latest book 仍可能有下一本；her last book 可能是她最后一本，也可能按语境指上一本。',
 ('Have you read her latest book?','你读过她最新那本书吗？'),('Please reply by Monday at the latest.','请最晚在星期一回复。'))
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_vb',ROOTS,WORDS)
 extend_lessons()
