"""The two historically different -ty endings, including the common tens."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
Tw=[['古英语 twa、twegen 等 → 中古英语 two 等','二；早期有不同语法形式'],['现代 two；古英语 twentig → twenty','二；二个十 → 二十']]
W('two','/tuː/','二；两个',
 '一个再加一个就是 two；它可以直接限定后面的东西，也可以自己指数字二。看数字不用把 w 也读出来。',
 '延续古英语 twa、twegen 等数词形式，经中古英语成为 two；w 保留在拼写里，现代常用发音不发 /w/。twenty 保留同族数词材料。',Tw,
 'two books 两本书；in two days 两天后、两天内等，随句意；in two 分成两半；the two of us 我们俩。',
 'two people；the two of us；in two。',
 'two、to、too 在常见强读里可同音，但 two 说数量，to 常是介词或不定式标记，too 常说也、太；不是一个词的三种随意拼法。',
 ('The two of us carried the table upstairs.','我们俩把桌子搬上楼。'),('She cut the apple in two.','她把苹果切成两半。'))
W('twenty','/ˈtwenti/','二十；二十岁的；二十元等〔看上下文〕',
 '想成两组十：十个再来十个，就是 twenty。in your twenties 则把二十到二十九岁这一段当成一个阶段。',
 '延续古英语 twentig，历史是二的材料与 -tig 十、十的一组相合；现代对应 two 与 -ty 的数词关系，拼写已不是原样 twoty。',Tw,
 'twenty students 二十名学生；in her twenties 在她二十多岁时；a twenty 可按货币语境指面额二十的纸币。',
 'twenty minutes；in your twenties。',
 'twenty 是二十，twentieth 是第二十；数量与序数分开。twenties 的年龄段通常是二十至二十九岁。',
 ('The walk takes about twenty minutes.','步行大约需要二十分钟。'),('She started the business in her twenties.','她二十多岁时创办了这家公司。'),sources=['https://en.wiktionary.org/wiki/twenty#English','https://www.etymonline.com/word/twenty'])
Th=[['古英语 thri、threo 等 → 中古英语 thre','三的数词形式'],['古英语 thritig → 中古英语 thritty、thirty 等','三个十；后来音位次序调整，形成 thirty']]
W('three','/θriː/','三；三个',
 '一、二之后再多一个，就是 three。最容易绊住的是开头 /θr/：不是 free，也不是 tree。',
 '延续古英语 thri、threo 等形式；th 对应旧字母 þ 的声音，现代一般读 /θ/。thirty 与 third 是同族的十位数、序数形式。',Th,
 'three people 三个人；in groups of three 三人一组；all three 三个全都。',
 'all three；three times；groups of three。',
 'three 是三个，third 是第三；three times 是三次、三倍，third time 是第三次。',
 ('All three answers were correct.','三个答案全都正确。'),('The students worked in groups of three.','学生三人一组活动。'))
W('thirty','英 /ˈθɜːti/；美 /ˈθɜːrti/','三十；三十岁的',
 '三组十就是 thirty；现代看起来与 three 不完全一样，是旧词音形变化留下的痕迹。',
 '古英语 thritig 等来自三与十组的材料；中古英语较早有 thritty 一类，随后相邻音的次序调整，形成 thirty。不是英语常用词 thir 加数字三的意义。',Th,
 'thirty days 三十天；in his thirties 他三十多岁时；thirty percent 百分之三十。',
 'thirty minutes；in your thirties。',
 'thirty 三十与 thirteen 十三分开。常见单独说时 thirty 重音在前、thirteen 常在后，但比较或句中重音会变，也要听元音、末音。',
 ('The museum is thirty kilometres from the city.','博物馆离城里三十公里。'),('He learned to swim in his thirties.','他三十多岁时学会游泳。'),sources=['https://en.wiktionary.org/wiki/thirty#English','https://www.etymonline.com/word/thirty'])
Fr=[['古英语 feower → 中古英语 four','四'],['古英语 feowertig → forty','四个十 → 四十；现代拼写不保留 four 的 u']]
W('four','英 /fɔː/；美 /fɔːr/','四；四个',
 '四条腿、四个方向，数到四就是 four。它与 forty 的数词关系清楚，但拼写不能逐个字母搬过去。',
 '延续古英语 feower，经中古英语成为 four；与日耳曼语其他四的形式同源。现代 four 中的 our 不能按 our 我们的去解释。',Fr,
 'four corners 四个角；all four 四个全都；four times 四次、四倍。',
 'four people；all four；four times。',
 'four 与 for 的强读在常见口音里可同音；数字四写 four，介词 for 不因此变成数词。',
 ('The table has four legs.','桌子有四条腿。'),('All four windows face the garden.','四扇窗都朝着花园。'))
W('forty','英 /ˈfɔːti/；美 /ˈfɔːrti/','四十；四十岁的',
 '四组十就是 forty；记拼写时抓住一点：four 有 u，forty 没有 u。',
 '由古英语 feowertig 经中古英语 fourty、forty 等形式延续；现代通用拼写定为 forty，不因为基础数词 four 就改成 fourty。',Fr,
 'forty pages 四十页；in her forties 她四十多岁时；forty percent 百分之四十。',
 'forty minutes；in your forties。',
 'forty 四十，fourteen 十四，fourth 第四，fortieth 第四十；同族词在数量、序数上不同。',
 ('The report is forty pages long.','报告有四十页。'),('She changed careers in her forties.','她四十多岁时换了职业。'))
W('fifty','/ˈfɪfti/','五十；五十岁的',
 '五组十就是 fifty。five 的 /v/ 到这里成为 /f/，不要只按 five 原音再接 ty。',
 '延续古英语 fiftig，上接五与十组的日耳曼语数词材料；现代对应 five、fifty，词干与语音已有变化。',
 [['古英语 fiftig 等','五个十'],['现代 fifty；对应 five','五十；与五保持词族关系']],
 'fifty people 五十人；fifty percent 百分之五十；in his fifties 他五十多岁时。',
 'fifty percent；in your fifties。',
 'fifty 五十与 fifteen 十五分开；两个词的 f 都要看清，数字后缀不能只凭一个末尾 t 猜。',
 ('Fifty people attended the workshop.','五十人参加了工作坊。'),('The battery was at fifty percent.','电池电量为百分之五十。'))
W('sixty','/ˈsɪksti/','六十；六十岁的',
 '六组十就是 sixty。six 的 /ks/ 仍在，与后面的 /t/ 连起来，别把六十听成十六。',
 '延续古英语 sixtig，中古英语 sixty、sexty 等形式；现代很直观地对应 six + -ty。',
 [['古英语 sixtig → 中古英语相应形式','六个十'],['现代 six + -ty 的对应 → sixty','六十']],
 'sixty seconds 六十秒；in her sixties 她六十多岁时；sixty percent 百分之六十。',
 'sixty seconds；in your sixties。',
 'sixty 六十通常前重音，sixteen 十六常末重音；句中仍要结合末尾是否有 /n/ 等线索辨认。',
 ('There are sixty seconds in a minute.','一分钟有六十秒。'),('She began painting in her sixties.','她六十多岁时开始画画。'))
W('seventy','/ˈsevənti/','七十；七十岁的',
 '七组十就是 seventy，现代 seven 的大部分外形、声音还很清楚。in your seventies 指七十到七十九岁。',
 '延续古英语 hundseofontig 等相应形式；旧形式含现今已不用的数词组合材料，现代可按 seven 与 -ty 对应来认，不把旧 hund- 机械算成一百再相加。',
 [['古英语 hundseofontig → 中古英语 seventy 等','七十的旧数词形式'],['现代 seven、seventy','七；七十']],
 'seventy years 七十年；seventy percent 百分之七十；in his seventies 他七十多岁。',
 'seventy people；in your seventies。',
 'seventy 七十、seventeen 十七；末尾 /ti/ 与 /tiːn/ 以及重音一起帮助辨认。',
 ('The hall can hold seventy people.','大厅可容纳七十人。'),('He remained active well into his seventies.','他到了七十多岁仍然很活跃。'))
W('eighty','/ˈeɪti/','八十；八十岁的',
 '八组十就是 eighty。eight 本来结尾已经有 t 的拼写，现代 eighty 不额外叠出两个 t。',
 '从古英语 hundeahtatig、中古英语 eightety 等相应形式发展而来，现代对应 eight 与 -ty；一些旧形式后来缩短、调整。',
 [['古英语 hundeahtatig 等 → 中古英语相应形式','八十的旧数词形式'],['现代 eight、eighty','八；八十']],
 'eighty kilometres 八十公里；in her eighties 她八十多岁；the eighties 也可按语境指某世纪八十年代。',
 'eighty percent；in your eighties。',
 'eighty 八十，eighteen 十八，eighth 第八，eightieth 第八十。数词材料相近，具体数量、顺序不同。',
 ('The battery charges to eighty percent in an hour.','电池一小时充到百分之八十。'),('She began writing poetry in her eighties.','她八十多岁时开始写诗。'))
W('ninety','/ˈnaɪnti/','九十；九十岁的',
 '九组十就是 ninety；nine 的末尾 e 在这个数词外形里不保留，但 /naɪn/ 还在。',
 '延续古英语 hundnigontig、中古英语 nynty、nynety 等形式，现代对应 nine 与 -ty，末尾直接用 -ty。',
 [['古英语 hundnigontig 等 → 中古英语相应形式','九十的旧数词形式'],['现代 nine、ninety','九；九十']],
 'ninety minutes 九十分钟；ninety percent 百分之九十；in his nineties 他九十多岁。',
 'ninety minutes；in your nineties。',
 'ninety 九十与 nineteen 十九区分；nineteen 保留 nine 的 e，ninety 的拼写不保留。',
 ('The journey took ninety minutes.','路程花了九十分钟。'),('He was still gardening in his nineties.','他九十多岁时还在打理花园。'))
W('eightieth','/ˈeɪtiəθ/','第八十；八十分之一',
 'eighty 说有八十个，eightieth 说排到第八十；作分母时 one eightieth 则是把整体分成八十份的一份。',
 'eighty 的 y 改 i，再加 -eth → eightieth；是十位数基数转序数的常见形式，不写成 eightyth。',
 [['eight → eighty','八 → 八十'],['eighty → eightieth','第八十；分母用法八十分之一']],
 'her eightieth birthday 她的八十岁生日；one eightieth of the total 总数的八十分之一。',
 'the eightieth anniversary；an eightieth。',
 'eighth 是第八，eightieth 是第八十；中间的 /ti/ 会影响数值，不能为了省音把两词都读成 eighth。',
 ('The town celebrated the library’s eightieth anniversary.','小镇庆祝图书馆成立八十周年。'),('Each part represents one eightieth of the total.','每部分占总数的八十分之一。'))
W('ninetieth','/ˈnaɪntiəθ/','第九十；九十分之一',
 '排第九十是 ninetieth；如果在说分数，one ninetieth 是九十份中的一份。和数量 ninety 分开。',
 'ninety 的 y 改 i，再加 -eth → ninetieth。nine 的 e 不在 ninety 中保留，序数也沿用这个词干。',
 [['nine → ninety','九 → 九十'],['ninety → ninetieth','第九十；分母用法九十分之一']],
 'a ninetieth birthday 九十岁生日；the ninetieth minute 第九十分钟。',
 'the ninetieth anniversary；one ninetieth。',
 'ninth 是第九，nineteenth 第十九，ninetieth 第九十；中间是不是 -teen- 很关键。',
 ('The family gathered for her ninetieth birthday.','家人为她的九十岁生日聚在一起。'),('The winning goal came in the ninetieth minute.','制胜球在第九十分钟出现。'))
R('A2095','数词中表示若干个十；另一来源构成性质、状态名词','-TY：同一外形，两条不同词源','twenty 是两个十，sixty 是六个十；loyalty 忠诚、difficulty 困难里的 -ty 则不是十。先分清词源线，再看实际用法。',
 '数词最直观：three 三，thirty 三十；four 四，forty 四十。再接序数变化就有 thirtieth 第三十、fortieth 第四十。另一方面，loyalty、royalty、subtlety 等是在谈状态、性质或固定发展出的事物，这一组与 -ity 相联。',
 '数词 -ty 延续古英语 -tig，日耳曼语中十、十的一组的材料；twenty、thirty 等有古老音形变化，不是现代数字词原封不动加 ty。另一条 -ty 经法语 -té、-te 接拉丁 -tas、-tat- 等性质名词材料，和 -ity 同族，来源与数词后缀不同。property、sovereignty 等可能整体借入，不强行按一个现代短词再加尾。现代十位数序数常 y → i 再接 -eth，如 twenty → twentieth；forty 的 u 不保留。',
 [['二、三、四个十','two · twenty · twentieth · three · thirty · thirtieth · four · forty · fortieth'],['五、六、七个十','five · fifty · fiftieth · six · sixty · sixtieth · seven · seventy · seventieth'],['八、九个十','eight · eighty · eightieth · nine · ninety · ninetieth'],['年龄段、年代和数量','twenty · thirty · forty · fifty · sixty · seventy · eighty · ninety'],['另一词源：性质与状态','loyalty · difficulty · uncertainty · sovereignty · royalty · subtlety · property']],
 'forty 四十不写 fourty；-teen 与 -ty 用末尾 /n/、元音及重音共同辨认；twenty 数量与 twentieth 顺序分开；in your twenties 通常二十到二十九岁；性质名词的 -ty 不表示十。',
 'Twenty people attended the first session, and thirty came to the second.\n\n二十人参加了第一场，三十人来了第二场。',
 'two twenty twentieth three thirty thirtieth four forty fortieth five fifty fiftieth six sixty sixtieth seven seventy seventieth eight eighty eightieth nine ninety ninetieth ten property difficulty loyalty uncertainty sovereignty royalty parity subtlety surety admiralty')
for x in WORDS:
 if x['word']=='twenty':x['sources'].append('https://www.etymonline.com/word/-ty')
if __name__=='__main__':save('continuation_20261030_qc',ROOTS,WORDS)
