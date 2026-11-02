"""Learned plurals encountered in ordinary reading, with homographs separated."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'C1015':dict(words=['phenomenon','phenomena'],label='phenomenon 与 phenomena：显现出来的现象',note='一个现象 a phenomenon；多个现象 phenomena。保留借词的 -on／-a 形式，不用看到 -a 就猜成一个独立新后缀义。'),
 'C0694':dict(words=['analysis','analyses','analyse','analyze'],label='analysis 与 analyses：拆开来看',note='名词 analysis 的复数 analyses 读 /əˈnæləsiːz/；英式动词 analyse 的第三人称形式也写 analyses，读 /ˈænəlaɪzɪz/。同形要按词性分读。'),
 'C0276':dict(words=['crisis','crises'],label='crisis 与 crises：几个危急关头',note='crisis 的复数 crises 结尾 /siːz/；希腊语判断、决定的旧词族，曾用于病程转折，后来泛说危急局面。'),
 'C0108':dict(words=['base','basis','bases'],label='bases 的两种读音和原形',note='base 的复数、第三人称动词形式 bases /ˈbeɪsɪz/；basis 的复数 bases /ˈbeɪsiːz/。同族分途借入，又在复数拼写上重合。'),
 'C0106':dict(words=['axis','axes','axe'],label='axis 的复数 axes 与斧头 axes',note='axis → axes /ˈæksiːz/；ax／axe → axes /ˈæksɪz/。轴与斧头属于不同来源，不能用同一个字面拆法串起来。'),
 'B2535':dict(words=['index','indices'],label='index 与 indices：指路的目录和指标',note='indices 保留拉丁 index／indic- 的复数材料；英语规则形式 indexes 也用，领域有偏好，分工不是绝对禁令。'),
 'C0443':dict(words=['formula','formulas','formulae'],label='formula 的两种常用复数',note='formulas 是英语规则复数，formulae 是保留拉丁形式的复数。公式、配方、固定办法等按上下文取义。'),
 'C0990':dict(words=['append','appendix','appendices'],label='appendix 与 appendices：附在后面的材料',note='appendix 从挂附的词族发展为书后附录，也作身体附属结构名称；appendices、appendixes 都可作复数。'),
 'C0289':dict(words=['curriculum','curricula'],label='curriculum 与 curricula：学习的路线',note='curriculum 接拉丁奔跑、进程材料，现代指课程体系、学习内容安排；复数 curricula，也可见 curriculums。'),
}
W('phenomena','英 /fəˈnɒmɪnə/；美 /fəˈnɑːmənə/','现象〔复数〕；phenomenon 的复数',
 '一场极光是一个 phenomenon；极光、彩虹等几类可观察到的现象合起来，是 phenomena。重点是显现出来、能被察觉的事情。',
 'phenomenon 经晚期拉丁借自希腊 phainomenon 显现之物，接 phainesthai 出现。phenomena 保留这一借词的 -on／-a 单复数对应。',
 [['希腊 phainomenon → 拉丁／英语 phenomenon','显现、被观察到的事物'],['phenomenon → phenomena','一个现象 → 多个现象']],
 'natural phenomena 自然现象；social phenomena 社会现象；these phenomena are 这些现象是。phenomenon 也可指非同寻常的人或事物。',
 'explain these phenomena；observe unusual phenomena。','标准学习先记 a phenomenon、several phenomena。词尾 -a 是保留下来的复数形式，不能再把 phenomena 当成普通单数加 s。',
 ('The book explains natural phenomena such as rainbows and lightning.','那本书解释彩虹、闪电等自然现象。'),('These phenomena are difficult to observe directly.','这些现象很难直接观察到。'),sources=['https://www.etymonline.com/word/phenomenon','https://en.wiktionary.org/wiki/phenomena#English'])
W('analyses','名词 /əˈnæləsiːz/；英式动词 /ˈænəlaɪzɪz/','分析〔名词复数〕；另为英式 analyse 的第三人称单数',
 '把问题拆成几部分，分别看它们怎么起作用，是 analysis。比较几份这样的分析，就用名词 analyses。',
 'analysis 经拉丁接希腊 analysis，字面有解开、拆开之意，接 ana- 与 lysis 松开。名词复数 analyses 沿借词模式；动词 analyses 则是 analyse + -s，两条现代语法路径同形而读音不同。',
 [['希腊 analysis → 拉丁／英语 analysis','解开、拆分来研究；分析结果'],['名词 analysis → analyses；动词 analyse + -s','多份分析；另一个读音表示某人作分析']],
 'two analyses 两份分析；statistical analyses 统计分析；she analyses the data 她分析数据，动词英式常用 analyse，美式常用 analyze。',
 'compare the analyses；the report analyses the causes。','名词重读第二音节 /ˈnæl/，末尾 /siːz/；动词重读第一音节 /ˈæn/，含 /laɪz/。看前面的 two 或主语 the report 能帮助分辨。',
 ('The two analyses reached different conclusions.','两份分析得出了不同结论。'),('We compared the statistical analyses in the report.','我们比较了报告中的各项统计分析。'),('The chapter analyses the causes of the conflict.','这一章分析冲突的原因。'),sources=['https://www.etymonline.com/word/analysis','https://en.wiktionary.org/wiki/analyses#English'])
W('crises','/ˈkraɪsiːz/','危机、危急局面〔复数〕；crisis 的复数',
 '一件大事到了必须作决定、局面可能急转的关口，是 a crisis。接连遇到几个这样的局面，就是 crises。',
 'crisis 借自希腊 krisis 判断、决定及关键转折点，进入英语时有病程关键点等义，后来泛化。复数 crises 保留这一借词的 -is／-es 形式。',
 [['希腊 krisis → 英语 crisis','判断、决定；关键转折、危急关头'],['crisis → crises','一场危机 → 多场危机']],
 'financial crises 金融危机〔复数〕；several crises 几场危机；a series of crises 一连串危机；deal with crises 应对多个危急局面。',
 'during times of crises；successive crises。','crisis 末尾 /sɪs/，crises 末尾 /siːz/。写法只变 i 为 e，读音的长短和最后 /z/ 也跟着变化。',
 ('The organization faced several crises in its first year.','该组织第一年就面对了几场危机。'),('The book compares how different communities respond to crises.','那本书比较不同社区如何应对危机。'),sources=['https://www.etymonline.com/word/crisis','https://en.wiktionary.org/wiki/crises#English'])
W('bases','base 的形式 /ˈbeɪsɪz/；basis 的复数 /ˈbeɪsiːz/','底座、基地等〔base 复数〕；依据、基础〔basis 复数〕；base 的第三人称形式',
 '几座能托住物体的底座可以是 bases；几套支撑判断的依据也写 bases。先找它的单数原形，才能把读音和意思对上。',
 '名词 base 与 basis 都接拉丁、希腊 basis 的站立处、基础材料，但经不同路径借入。base + -s 读 /ˈbeɪsɪz/；basis 沿借词复数模式成 bases /ˈbeɪsiːz/。动词 base + -s 与前一种同音。',
 [['希腊、拉丁 basis → 英语 base／basis','站立处、底座 → 基础、依据'],['base + -s；basis → bases','两条复数路径在拼写上重合，读音有别']],
 'lamp bases 灯座；military bases 军事基地；the theoretical bases 理论依据；she bases her view on evidence 她依据证据形成看法。',
 'different bases for comparison；bases an argument on facts。','basis 表依据时单数末尾 /sɪs/，复数末尾 /siːz/；base 的规则复数则是 /sɪz/。听结尾长元音能帮助辨认。',
 ('The lamps have heavy wooden bases.','那些灯配有沉重的木底座。'),('The chapter explains the theoretical bases of the method.','这一章解释该方法的理论基础。'),('She bases her decisions on careful observation.','她根据仔细观察作决定。'),sources=['https://www.etymonline.com/word/base','https://www.etymonline.com/word/basis','https://en.wiktionary.org/wiki/bases#English'])
W('axes','axis 的复数 /ˈæksiːz/；ax／axe 的形式 /ˈæksɪz/','轴、坐标轴〔复数〕；另源斧头〔复数〕或砍掉的动词形式',
 '图上横竖两条参照线叫 axes，读末尾长 /iː/；工具架上的几把斧头也写 axes，末尾短 /ɪ/。',
 '轴 axis 来自拉丁 axis，复数 axes 保留借词形式；斧头 ax／axe 接古英语 æces、æx 等，复数按英语规则加 -es。两条词源不同。',
 [['拉丁 axis → axis／axes /ˈæksiːz/','转轴、参照轴；单复数'],['古英语 æces 等 → ax／axe + -es','斧头的规则复数；也有动词第三人称形式']],
 'the horizontal and vertical axes 横轴和纵轴；label the axes 标注坐标轴；two sharp axes 两把锋利的斧头；axes a plan 砍掉计划。',
 'the axes of a graph；tools such as axes and saws。','axes 同形不同音：看 graph、rotation 常取 axis 分支；看 tools、chop 常取 ax／axe 分支。实际读音同时提示所属来源。',
 ('Label both axes before drawing the graph.','画图之前先标注两条坐标轴。'),('The old shed contained two axes and a saw.','旧棚屋里有两把斧头和一把锯子。'),sources=['https://www.etymonline.com/word/axis','https://www.etymonline.com/word/ax','https://en.wiktionary.org/wiki/axes#English'])
W('indices','/ˈɪndɪsiːz/','指数、指标；索引〔复数之一〕；index 的复数',
 '一根手指能指出东西在哪里；目录把人指到书页，指标把人指向某种变化。indices 是 index 的多个版本。',
 'index 来自拉丁 index，词干 indic-，表示指出者、指示物等；indices 保留拉丁复数材料，字母 c 在现代英语这里读 /s/。规则复数 indexes 也广泛使用。',
 [['拉丁 index、indic- → 英语 index','指出东西的人或物；索引、指标'],['拉丁复数形式 → indices；并存 indexes','多个索引、指标或指数']],
 'price indices 价格指数；refractive indices 折射率〔复数〕；stock indices 股票指数；book indices 书籍索引。现代不同领域对 indices、indexes 有习惯偏好。',
 'compare the indices；several performance indices。','不能规定 indices 只能数学、indexes 只能书籍。二者的使用确有领域倾向，具体还要看该领域惯用名称和编辑习惯。',
 ('The chart compares price indices from several years.','图表比较了几年的价格指数。'),('The report uses three indices to describe the changes.','报告用三个指标描述这些变化。'),sources=['https://www.etymonline.com/word/index','https://en.wiktionary.org/wiki/indices#English'])
W('formulas','英 /ˈfɔːmjələz/；美 /ˈfɔːrmjələz/','公式、配方、固定办法〔复数〕；formula 的规则复数',
 '一套能反复使用的表达或做法，像可套用的小模版。多套数学表达、食品配方、成功套路，都可能是 formulas。',
 'formula 来自拉丁 formula，原是 forma 形式的指小词，已有规则、草案等义。现代 formulas 是 formula + -s 的英语规则复数，与 formulae 并存。',
 [['拉丁 forma → formula → 英语 formula','小形式、规则、固定表达；后来公式等'],['formula + -s → formulas','英语规则复数']],
 'mathematical formulas 数学公式；chemical formulas 化学式；different formulas 不同配方、办法；simple formulas 简单公式或套路。',
 'memorize the formulas；compare two formulas。','formulas 与 formulae 都是合法复数；不能把 formulas 限制为只有配方、把 formulae 限制为只有数学。语境决定具体意思。',
 ('The students wrote the formulas on the board.','学生们把公式写在黑板上。'),('The company tested several formulas for the new paint.','公司测试了几种新油漆配方。'),sources=['https://www.etymonline.com/word/formula','https://en.wiktionary.org/wiki/formulas#English'])
W('formulae','英 /ˈfɔːmjəliː/；美 /ˈfɔːrmjəliː/','公式、配方等〔复数之一〕；formula 的拉丁式复数',
 '看到末尾 ae，先认成 formula 的另一种复数，不必猜成全新的公式种类。',
 'formula 借自拉丁 forma 的指小词，formulae 保留拉丁复数写法；在现代英语中末尾常读 /liː/。与规则复数 formulas 并存。',
 [['拉丁 formula → formulae','拉丁语单复数对应'],['英语采用 formulae，同时也用 formulas','公式、配方等的两种复数形式']],
 'algebraic formulae 代数公式；a list of formulae 公式表；derive the formulae 推导公式。英式、学术写作较容易遇到这一形式，但不是只能出现在这些场景。',
 'standard formulae；use these formulae。','formulae 末尾通常 /liː/，formulas 通常 /ləz/。选用形式受语言变体和编辑习惯影响，阅读时把注意力放在所指公式或配方即可。',
 ('The appendix lists the formulae used in the chapter.','附录列出了本章使用的公式。'),('These formulae can be rearranged to find the unknown value.','这些公式可以变形，以求出未知值。'),sources=['https://www.etymonline.com/word/formula','https://en.wiktionary.org/wiki/formulae#English'])
W('appendices','/əˈpendɪsiːz/','附录〔复数〕；阑尾等附属结构〔复数〕；appendix 的复数之一',
 '正文说完了，把细表、问卷、额外说明附在后面。一本书有几份这样的附加材料，就是 several appendices。',
 'appendix 接拉丁 appendix 附加物，源自 appendere 挂附：ad- 向、附着 + pendere 悬挂。appendices 保留拉丁复数材料，appendixes 也是英语中使用的复数。',
 [['拉丁 appendere → appendix','挂附 → 附在主体上的东西'],['appendix → appendices；也用 appendixes','多份附录；身体附属结构的复数']],
 'the book’s appendices 该书的附录；in the appendices 在附录中；appendices A and B 附录 A 和 B。身体器官义也可以用这个复数形式。',
 'consult the appendices；additional appendices。','appendices 是名词复数；append 是附加的动词，过去式 appended。不能把 appendices 直接当成 append 的某种过去形式。',
 ('The report has three appendices.','报告有三个附录。'),('The survey questions are included in the appendices.','调查问题收在附录中。'),sources=['https://www.etymonline.com/word/appendix','https://en.wiktionary.org/wiki/appendices#English'])
W('curricula','英 /kəˈrɪkjələ/；美 /kəˈrɪkjələ/','课程体系、课程安排〔复数〕；curriculum 的复数之一',
 '一个学校安排学生一路学什么、怎样往下走，是 curriculum；比较几所学校的整套课程，就用 curricula。',
 'curriculum 接拉丁 curriculum 奔跑、进程等，属于 currere 跑的词族；近代拉丁把它用于学习进程。curricula 保留拉丁 -um／-a 复数，英语也用 curriculums。',
 [['拉丁 currere → curriculum','跑 → 进程、走过的路线'],['近代学习进程用法 → curriculum／curricula','课程体系及其复数']],
 'school curricula 学校课程体系；different curricula 不同课程安排；compare curricula 比较课程；develop curricula 设计课程体系。',
 'national curricula；revised curricula。','a course 可以是一门课；a curriculum 通常是整体学习安排、内容体系。curricula 的复数范围是多套体系，不自动等于同一套中的几门课。',
 ('The study compared the curricula of three schools.','研究比较了三所学校的课程体系。'),('Teachers helped develop the new curricula.','教师们参与制定了新的课程体系。'),sources=['https://www.etymonline.com/word/curriculum','https://en.wiktionary.org/wiki/curricula#English'])
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_ug',ROOTS,WORDS)
 extend_lessons()
