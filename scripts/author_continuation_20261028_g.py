"""Common bases with several easily confused forms, explained individually."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
def C(a,b,name,meaning):return [[f'英语 {a}；{b}','组合使用的两个材料'],[f'{a} + {b} → {name}',meaning]]
OTHER=[['古英语 ōþer → 中古英语 other','另一个；也有第二的旧义'],['英语 other','别的、另外的']]
W('other','英 /ˈʌðə/；美 /ˈʌðər/','别的；其他的；另一个',
 '手里已经有这一件，把目光转向它之外的那一件或那些。',
 '来自古英语 ōþer，经中古英语延续；旧时也能表示第二。现代词不能按 o + ther 硬拆。',OTHER,
 'other people 是其他人，the other side 是另一边。两个对象中已说一个，the other 常指剩下的另一个；others 可独立代替复数名词。',
 'other people；the other day；each other；one or the other。',
 'another 通常是另外一个、不特指；the other 常是特定范围里另一个。other books 是其他书，others 后不再直接接 books。',
 ('Do you have any other questions?','你还有其他问题吗？'),('One shoe was under the bed, and the other was by the door.','一只鞋在床下，另一只在门边。'))
W('otherwise','英 /ˈʌðəwaɪz/；美 /ˈʌðərwaɪz/','否则；以别的方式；在其他方面',
 '沿着刚才的条件走会有一个结果，换一种情况就会走到另一个结果。',
 '接古英语 on ōþre wīsan“以别的方式”等表达，经中古英语延续；现代对应 other + -wise，-wise 在这里指方式。',OTHER[:1]+[['古英语 on ōþre wīsan → 英语 otherwise','以别的方式；在别的条件下']],
 'Hurry, otherwise we’ll be late 是快点，否则会迟到。I thought otherwise 是我看法不同。The room is small but otherwise fine 是房间小，其他方面很好。',
 'unless told otherwise；think otherwise；otherwise fine。',
 'otherwise 不只有否则。若句中只是补充其他方面的评价，就不必强行译成因果条件句。',
 ('Save the file now; otherwise, you may lose your changes.','现在保存文件，否则可能丢失修改。'),('The flat is noisy but otherwise very comfortable.','这套公寓有点吵，其他方面很舒服。'))
W('otherness','英 /ˈʌðənəs/；美 /ˈʌðərnəs/','异质性；不同感；他者性',
 '站在熟悉的人群中，忽然发现某人或自己被看成“不属于这里的那一种”。',
 'other + -ness；-ness 把别的、不同这种性质转为抽象名词，不表示具体另一个人。',OTHER+[['other + -ness → otherness','与通常或自我不同的性质、感受']],
 '文学和社会讨论常见，既可说陌生感，也可讨论人怎样被划成“他者”。具体是否带排斥、不安或好奇，要看叙述立场。',
 'a sense of otherness；the otherness of a place；cultural otherness。',
 'otherness 说不同或被当作他者的感觉，difference 更宽泛地说差别。otherness 不自动断言差别有高下。',
 ('The story explores the child’s sense of otherness.','故事探讨了孩子觉得自己格格不入的感受。'),('The landscape had an otherness that made familiar words seem inadequate.','这片景色有种陌生独特的气质，让熟悉的词都显得不够用。'))
W('otherworld','英 /ˈʌðəwɜːld/；美 /ˈʌðərwɜːrld/','异界；另一个世界〔神话、文学〕',
 '故事把日常世界之外另留一处：那里可能住着精灵、亡灵或其他存在。',
 'other（另一个）+ world（世界），古英语及中古英语已有相应表达；具体神话中的世界设定各不相同。',C('other','world','otherworld','日常世界以外的另一世界'),
 '多见神话、幻想文学或宗教研究，不是已经证实的物理地点名称。通常由故事背景定义它是什么。',
 'the otherworld；a journey to the otherworld；the realm of the otherworld。',
 'otherworld 偏神话中的异界；another world 是更普通短语，可以只是一个差异很大的生活环境。',
 ('The hero enters the otherworld through a hidden cave.','主人公通过隐秘洞穴进入异界。'),('The tale places the otherworld beyond the western sea.','传说把异界设在西海之外。'))
R('B2676','其他；别的','OTHER：把视线移到当前对象之外','已经拿起一只鞋，再找剩下的那一只。',
 'other 是古英语本族词，核心是别的、另外的。otherwise 转到其他方式或条件，otherness 说不同感，otherworld 则在故事中指另一个世界。',
 'the other／others／another 的选择受特指、数量影响；-wise 在 otherwise 中表示方式，-ness 说性质。otherworld 是复合名词，不从 otherness 的抽象义硬派生。',
 [['不同对象','other'],['换一种情况','otherwise'],['不同感与异界','otherness · otherworld']],
 'other 后可接复数名词，others 通常独立使用；another 是另外一个，the other 是特定范围里的另一个。',
 'Try the other door; otherwise, we may have to turn back.\n\n试试另一扇门，否则我们可能得返回。','other otherwise otherness otherworld')

MOST=[['古英语 mǣst → 中古英语 most','数量、程度最高的'],['英语 most','最多；大多数；最']]
W('most','/məʊst/〔英〕；/moʊst/〔美〕','最多；大多数；最；非常〔正式〕',
 '把一组数量或程度放在一起比较，走到上端；谈一群人时，也可以说其中的大部分。',
 '接古英语 mǣst，经中古英语 most 延续，是 many、much 的最高级配套形式之一，不是简单在 more 后加 -st。',MOST,
 'most people 是大多数人，the most useful tool 是最有用的工具。a most interesting idea 是很有趣的想法，较正式，不一定在所有想法中排第一。',
 'most people；most of the time；the most important；make the most of。',
 'most people 是泛指大多数人，most of the people 指一群特定人中的大多数。almost 是差一点，不能直接代替 most。',
 ('Most people arrived before nine.','大多数人九点前到了。'),('This is the most useful chapter in the book.','这是书里最有用的一章。'))
W('almost','/ˈɔːlməʊst/〔英〕；/ˈɔːlmoʊst/〔美〕','几乎；差一点',
 '离那条线只差一点，还没有完全到达。',
 '接古英语 eallmǣst，经中古英语 almost 延续；材料与 all、most 有关，现代已是固定副词，不按“所有最多”直译。',
 [['古英语 eallmǣst → 中古英语 almost','几乎全部、差不多'],['英语 almost','接近但没有完全达到']],
 'almost finished 是快做完；almost everyone 是几乎每个人。I almost fell 是差点摔倒，通常表示没真正摔下去。',
 'almost all；almost never；almost finished；almost certainly。',
 'almost 不直接修饰普通 people 来表示大多数：可用 almost all people、almost everyone，或用 most people。',
 ('The bottle is almost empty.','瓶子快空了。'),('I almost missed the train.','我差点没赶上火车。'))
W('mostly','/ˈməʊstli/〔英〕；/ˈmoʊstli/〔美〕','主要地；大部分；多半',
 '把一堆情况分开看，其中占大头的那一部分是这样。',
 'most + -ly，-ly 构成副词，常说明组成、情况或时间上的主要部分。',MOST+[['most + -ly → mostly','大部分如此；主要地']],
 'mostly students 是多数是学生；mostly dry 是大部分干燥、总体少雨。通常不表示每一处、每一次都一样。',
 'mostly made of；mostly because；mostly dry；mostly harmless。',
 'mostly 说占大部分，almost 说接近某个界线。mostly empty 表大部分是空的，almost empty 表几乎全空，侧重点不同。',
 ('The audience was mostly made up of students.','观众大多数是学生。'),('I work from home mostly, but I visit the office once a week.','我主要居家办公，不过每周去办公室一次。'))
R('B2479','最多；大多数','MOST：数量或程度的大头、上端','一群对象中占大部分，或比较时走到最高的一端。',
 'most 接古英语最高级形式；almost 早已有固定的接近、差不多用法，mostly 则表示大部分如此。三者不要都压缩成“大多数”。',
 'most people、most of the people 和 the most useful 的结构不同；almost 通常放在 all、everyone 或形容词动词前表达接近；mostly 是副词，描述主要情况。',
 [['最多与大多数','most'],['差一点','almost'],['主要如此','mostly']],
 'most people：大多数人；almost everyone：几乎每个人；mostly students：主要是学生。',
 'Most of the work is done, so the project is almost finished.\n\n大部分工作已完成，项目因此快结束了。','most almost mostly')

FIRST=[['古英语 fyrest → 中古英语 first','最在前的'],['英语 first','第一；首先、最初']]
W('first','英 /fɜːst/；美 /fɜːrst/','第一；首先；最初',
 '把人、事或步骤排成一列，站在队伍最前面的那一个。',
 '接古英语 fyrest 一系，更早与在前的日耳曼语材料和最高级形式有关；现代 first 不是 one 加一个常规词尾。',FIRST,
 'the first day 是第一天，First, check the name 是先检查姓名，at first 是起初。for the first time 是第一次，不能少掉 for 后直接逐字拼。',
 'at first；first of all；for the first time；first aid。',
 'at first 说最初状态，常暗含后来有变化；first 说顺序在前。At first I disagreed 不只是列举第一点。',
 ('Read the instructions first.','先读说明。'),('At first, I thought the shop was closed.','起初我以为商店关门了。'))
W('firstly','英 /ˈfɜːstli/；美 /ˈfɜːrstli/','首先；第一点',
 '开始列一串理由，先把第一项摆到桌面上。',
 'first + -ly，形成表示列举顺序的副词；中古英语后期已有对应构词形式。',FIRST+[['first + -ly → firstly','列举中的第一点']],
 '常搭 secondly、finally 用于条理清晰的论述。first 也能直接作这种顺序副词，因此不必为了语法正确总添 -ly。',
 'firstly, …；firstly and most importantly；firstly … secondly …。',
 'firstly 主要列举；at first 是起初。描述“起初我不喜欢”通常用 At first I didn’t like it，而非 Firstly。',
 ('Firstly, we need to agree on the goal.','首先，我们需要就目标达成一致。'),('Firstly, the plan is affordable; secondly, it is easy to test.','第一，计划费用可承担；第二，容易验证。'))
W('firsthand','英 /ˌfɜːstˈhænd/；美 /ˌfɜːrstˈhænd/','亲身的；直接地',
 '消息没有经过一层层转述，是自己亲眼看、亲手做、亲自经历的。',
 'first + hand，hand 借来表示接触、经手。连写形式可作形容词或副词；还常见带连字符的拼写。',C('first','hand','firsthand','直接接触、亲身经历的'),
 'firsthand experience 是亲身经验，see firsthand 是亲眼见到。直接经历可减少转述环节，但不保证观察者绝无偏差。',
 'firsthand experience；firsthand knowledge；see firsthand。',
 'firsthand 与 secondhand 亲历、转述相对；不是说第一只手与第二只手。',
 ('She has firsthand experience of running a small business.','她有亲自经营小企业的经验。'),('We saw firsthand how the new system worked.','我们亲眼看到了新系统如何运作。'))
W('firstborn','英 /ˈfɜːstbɔːn/；美 /ˈfɜːrstbɔːrn/','头生的；长子或长女；第一个孩子',
 '把同一家孩子按出生顺序排，第一个来到的就是 firstborn。',
 'first（最先）+ born（出生的），中古英语已有 first borne 等对应短语。born 是 bear 在出生义中的分词形式。',C('first','born','firstborn','最先出生的孩子或最先出生的'),
 'my firstborn 可以是长子也可以是长女；firstborn child 只说明出生顺序，不表示性别，也不自动说明继承安排。',
 'a firstborn child；their firstborn；firstborn son。',
 'firstborn 是出生顺序，eldest 是一组同辈中年龄最大，only child 是独生子女；语境有交叉但并不等同。',
 ('Their firstborn started school this year.','他们的第一个孩子今年上学了。'),('The portrait shows the couple with their firstborn daughter.','肖像画里是这对夫妇和他们的长女。'))
W('headfirst','/ˌhedˈfɜːst/〔英〕；/ˌhedˈfɜːrst/〔美〕','头朝前地；贸然地',
 '身体往前走时，头先进去；做决定时也可能还没看清就一头扎进去。',
 'head（头）+ first（先），把身体朝向与顺序组合成副词。比喻义关注没有足够准备就投入。',C('head','first','headfirst','头先进入；比喻贸然投入'),
 'fall headfirst 是头朝下摔，rush headfirst into a project 是贸然投入项目。词常提示姿势或冲动，但不保证每次都在批评。',
 'fall headfirst；dive headfirst；rush headfirst into。',
 'headfirst 说明哪一部分在前，firsthand 说明知识是否亲自取得；两个 first 组合不能互换。',
 ('The child slid headfirst down the slide.','孩子头朝前滑下了滑梯。'),('Do not rush headfirst into a project without checking the costs.','没查清费用前，不要贸然投入项目。'))
R('B2505','第一；最先','FIRST：排在时间或顺序的前面','先到的是第一名，先做的是第一步，先出生的是第一个孩子。',
 'first 来自古英语在前、最高级一系。firstly 用于列举；firsthand 是直接经手、亲历；firstborn 和 headfirst 则各自让后面的材料说明什么在先。',
 'first 可作形容词、副词及名词，不能只当序数词表格中的一项。firsthand 与 headfirst 虽共享 first，却不属于同一个意思：前者亲历，后者头在前。',
 [['顺序','first · firstly'],['经验与出生','firsthand · firstborn'],['姿势与投入','headfirst']],
 'at first：起初；firstly：第一点。firsthand：亲身；headfirst：头朝前或贸然。',
 'First, listen to someone with firsthand experience rather than rushing headfirst into action.\n\n首先，听听有亲身经验的人怎么说，再行动，别一头扎进去。','first firstly firsthand firstborn headfirst')

WELL=[['古英语 wel → 中古英语 wel','好地、顺利地'],['英语 well 的副词、形容词等','好地；健康；用来转接话语']]
W('well','/wel/','好地；健康的；井；涌出；嗯、好吧',
 '一条线问事情做得好不好；另一条线看水从井泉里涌出来。相同拼写有不同来源。',
 '“好地”接古英语 wel；“井”接古英语 wielle；“涌出”关联古英语 weallan／wiellan。不能用“做得好就有井水”把它们串成一条来历。',
 [['并行来源：古英语 wel；wielle；weallan／wiellan','好地；井泉；沸腾、涌出'],['现代 well','好地、健康；井；涌出；话语连接用法']],
 'She sings well 是唱得好，I am well 可说身体好；a well 是水井，tears welled up 是泪水涌上来。Well, … 可给回答留一点停顿，不一定有实义“好”。',
 'do well；as well；as well as；a water well；well up。',
 'good 通常修饰名词，well 通常修饰动作，但 well 表身体健康时是形容词。The soup smells good 也不因有动词就机械改成 well。',
 ('She speaks English very well.','她英语说得很好。'),('The village gets water from a deep well.','村子从一口深井取水。'),('Tears welled up in his eyes.','他眼里涌出了泪水。'))
W('unwell','/ʌnˈwel/','身体不适的',
 '没有到平常舒服的状态，可能只是觉得不舒服，未必已说明什么病。',
 'un-（不）+ well（健康的），否定的是形容词健康义，不是否定名词水井。',WELL+[['un- + well → unwell','身体不适']],
 'feel unwell 常是较温和、礼貌的身体不适说法。程度和原因需由上下文给出，词本身不作诊断。',
 'feel unwell；look unwell；be unwell。',
 'unwell 常描述人的身体状态；badly 可说动作做得不好。He feels unwell 与 He did badly 表达不同。',
 ('She went home early because she felt unwell.','她觉得身体不适，提前回家了。'),('I am sorry to hear that you have been unwell.','听说你近来身体不好，我很遗憾。'))
W('welfare','英 /ˈwelfeə/；美 /ˈwelfer/','福祉；安康；福利救助',
 '不只问一个人活着没有，还问他过得稳不稳、安不安全、有没有基本保障。',
 '中古英语 welefare，联系较早 wel faran“过得好、顺利”等表达；对应 well + fare。fare 在这里与生活、行进状况有关，不是车票钱。',WELL[:1]+[['wel faran 等表达 → 中古英语 welefare','过得好、生活顺遂'],['英语 welfare','安康、福祉；社会福利救助']],
 'child welfare 是儿童福祉或福利工作；animal welfare 关注动物生活处境。部分语境 welfare 专说公共救助，不能把所有出现都窄化为救济金。',
 'the welfare of children；animal welfare；welfare support。',
 'welfare 范围包括安康、安全、生活条件；wealth 是财富。有钱与福祉相关，却不是同一个词义。',
 ('The organisation works to improve animal welfare.','这个组织致力于改善动物福利。'),('The children’s welfare must come first.','孩子们的福祉必须放在首位。'))
W('farewell','英 /ˌfeəˈwel/；美 /ˌferˈwel/','告别；再见；告别的',
 '送人上路时，祝他一路好、往后也好，后来就成了告别词。',
 '由 fare well!“一路好、过得好”的祝愿表达固定成词；fare 是行进、生活的旧动词，well 是好地。不是 fare“票价”很便宜。',
 [['中古英语 fare wel!','祝一路顺利、过得好'],['英语 farewell','再见；告别或送别的']],
 '比 bye 更庄重或带离情，常说 a farewell party、bid farewell to。Farewell! 可单独作告别感叹词。',
 'a farewell party；a farewell speech；bid farewell to。',
 'farewell 不一定表示永别，但比日常 see you 常更正式、有结束一个阶段的意味。',
 ('They held a farewell party for their departing colleague.','他们为即将离开的同事办了送别会。'),('We said farewell to the village where we had spent the summer.','我们告别了度过夏天的村庄。'))
W('stairwell','英 /ˈsteəwel/；美 /ˈsterwel/','楼梯间',
 '站在楼下抬头看，楼梯在一个竖向空间里盘旋或逐层连接。',
 'stair（楼梯）+ well（井状竖向空间），取 well 的空间义，不是“楼梯很好”。',C('stair','well〔井状空间〕','stairwell','容纳楼梯的竖向建筑空间'),
 '常用于多层建筑的楼梯间，可能封闭或部分开放。stairwell 强调空间，楼梯本身可说 stairs、staircase。',
 'in the stairwell；a dark stairwell；an enclosed stairwell。',
 'stairway 是上下通行的楼梯路线，stairwell 是容纳它的空间；两者在描述时可能相关，但焦点不同。',
 ('Voices echoed in the stairwell.','说话声在楼梯间回响。'),('A window lights the top of the stairwell.','一扇窗照亮了楼梯间顶部。'))
W('wellspring','/ˈwelsprɪŋ/','泉源；源泉',
 '不是从远处运来的水，而是不断从这里冒出，补给其他地方。',
 '接古英语 wiellspring／wiellġespring 等形式；对应 well（井泉）+ spring（泉）。两个材料共同指向水的源头，后来抽象为持续来源。',
 [['古英语 wiellspring 等形式','水的泉源'],['英语 wellspring','泉源；思想、力量等的持续来源']],
 'a wellspring of creativity 常说不断提供创意的源头，较书面。不是单个偶然想法，而是反复能产生东西的来源。',
 'a wellspring of ideas；a wellspring of hope；a source and wellspring。',
 'wellspring 是源头，reservoir 是积存、储备的地方；泉不断供给与水库储存是两幅不同画面。',
 ('Local history became a wellspring of ideas for her novels.','当地历史成了她小说创意的源泉。'),('The community found a wellspring of hope in the new school.','社区从新学校获得了不断涌出的希望。'))
R('B3259','好地；健康；井泉与涌出〔分源〕','WELL：一边是过得好，一边是水的源头','用两幅图分开记：事情顺利；井泉涌水。',
 'well 至少要分“好地”的古英语 wel 与“井泉”的 wielle 等来源。welfare、farewell、unwell 接前一侧；stairwell、wellspring 接井泉空间与水源一侧。拼写一样不表示必须有一条共同的英语词义链。',
 'well 可作副词、健康形容词、井名词、涌出动词及话语词。farewell 的 fare 是行进、过日子的旧动词；stairwell 的 well 是井状空间。',
 [['状态与安康','well · unwell · welfare'],['告别祝愿','farewell'],['井状空间与源头','stairwell · wellspring']],
 'good／well 先看修饰对象；well 表健康时也可作形容词。welfare 不是 wealth；stairwell 不是 stairway 的完全同义词。',
 'She wished us farewell, and the memory remained a wellspring of comfort.\n\n她与我们道别，这段回忆始终带来安慰。','well unwell welfare farewell stairwell wellspring')

EVEN=[['古英语 efn → 中古英语 even','平整、相等、齐平'],['英语 even','平的、均匀的、相等的；甚至等副词用法']]
W('even','/ˈiːvən/','平整的；均匀的；偶数的；甚至；更',
 '形容词先想一条平线，两边齐平；副词则常把连最意外的情况也拉进来比较。',
 '常用平整、相等一系接古英语 efn。even 的强调副词用法经过长期发展，学习时可联系比较焦点，但不能编成一次简单的“平地→甚至”直线故事。',EVEN,
 'an even surface 是平面，even numbers 是偶数，an even chance 是机会相当。Even a child can see it 是连孩子都看得出；even better 是更好。',
 'even numbers；an even surface；even if；even better。',
 'evening 的晚上来自另一古英语“傍晚”词，不是这个“均匀”的 even 做了 -ing。强调词 even 放哪，哪一部分更受关注。',
 ('Spread the mixture in an even layer.','把混合物铺成均匀的一层。'),('Even the teacher found the question difficult.','连老师都觉得这道题难。'),('The second attempt was even better.','第二次尝试更好了。'))
W('evenly','/ˈiːvənli/','均匀地；平均地；平稳地',
 '每一块分到的差不多，每一处涂到的也差不多，没有一头厚一头薄。',
 'even + -ly，接古英语 efenlīċe 等副词形式；-ly 表副词，这里主要接均匀、平等一侧。',EVEN+[['even + -ly → evenly','均匀、平均或平稳地']],
 'divide evenly 是平均分，cook evenly 是受热均匀，speak evenly 是语气平稳。不是 even 所有强调义都能接成 evenly。',
 'spread evenly；divide evenly；evenly matched；evenly distributed。',
 'evenly 描述分布、动作或状态均匀；even 单独强调“甚至”的用法，不能直接变成 evenly a child。',
 ('Divide the money evenly between the two groups.','把钱平均分给两组。'),('The oven cooks the food evenly.','这个烤箱能让食物均匀受热。'))
W('uneven','/ʌnˈiːvən/','不平整的；不均匀的；水平不一的',
 '一条路高低不平，一篇文章也可能有些段落精彩、有些松散。',
 'un-（不）+ even（平整、均匀），接中古英语及更早 unefen 等否定形式。',EVEN[:1]+[['古英语 unefen → 英语 uneven','不平等、不相称；不平、不均匀']],
 'uneven ground 是高低不平地面；uneven performance 是表现有好有坏。un- 否定齐平，不自动把所有义项都变成“奇数”。',
 'uneven ground；an uneven surface；uneven quality。',
 '日常数学中偶数 even 的相对词通常是 odd，不用 uneven 当首选。uneven 常说高低不平、分布或水平不一致。',
 ('Be careful on the uneven path.','小心这条高低不平的小路。'),('The book is interesting but uneven in quality.','这本书有趣，但质量参差不齐。'))
W('evening','/ˈiːvnɪŋ/','傍晚；晚上',
 '白天的亮光慢慢退去，一天从白日过渡到夜晚的那一段。',
 '接古英语 ǣfnung、ǣfnian“进入傍晚”，根本材料是 ǣfen“傍晚”。虽然可见旧 even + -ing 的分析，这个 even 是“傍晚”的旧词，不是“平整、甚至”的 even。',
 [['古英语 ǣfen → ǣfnian／ǣfnung','傍晚 → 入晚、晚间'],['中古英语 evening → 英语 evening','傍晚、晚上']],
 'in the evening 是一般晚间，this evening 是今晚，不再加 in。Good evening 用于傍晚或晚间见面，good night 多用于道别、睡前。',
 'this evening；in the evening；an evening class；Good evening。',
 'evening 和 night 边界随作息与语境变化，不能背成全英语统一的某个钟点。evening 也不能靠“天变平了”解释。',
 ('We went for a walk in the evening.','我们傍晚出去散步。'),('Are you free this evening?','你今晚有空吗？'))
W('evensong','英 /ˈiːvənˌsɒŋ/；美 /ˈiːvənˌsɔːŋ/','晚祷；晚祷仪式',
 '一天渐晚，在教堂里以祈祷、诵读或歌唱结束日间活动。',
 '古英语 ǣfensang，even 是“傍晚”的旧形式，song 是歌唱。现代特指某些基督教传统的晚间礼拜，并非“平均唱歌”。',
 [['古英语 ǣfen + sang → ǣfensang','傍晚；歌唱'],['英语 evensong','晚间祈祷、礼拜仪式']],
 '常见于英国教堂与圣公会背景，可特别指有唱诗的晚祷。具体仪式内容随传统，不凭词名推断任何晚间音乐会都属于 evensong。',
 'attend evensong；choral evensong；Sunday evensong。',
 'evensong 是宗教仪式，evening concert 是晚间音乐会；有歌唱不等于同一活动。',
 ('Visitors are welcome to attend evensong.','欢迎访客参加晚祷。'),('The choir sang at choral evensong.','唱诗班在唱诗晚祷中献唱。'))
R('B3637','平整、相等；傍晚一支另源','EVEN：均匀一侧，与傍晚一侧分开记','先铺平一层材料，再另看黄昏的天色，不把两幅画硬串。',
 'even 的平整、相等来自古英语 efn；evening 和 evensong 接 ǣfen“傍晚”。两条近源不同，即使都能在现代看到 even 字母，也不能解释成同一个基础意思。',
 'evenly、uneven 对应平整均匀这支；evening 的 -ing 接较早“入晚”形式。even 作强调副词时要看它强调的是谁、什么情况。数学“奇数”通常用 odd。',
 [['齐平、分配与强调','even · evenly · uneven'],['傍晚与晚间仪式','evening · evensong']],
 'even numbers 的反面 odd numbers；uneven road 说路不平。Good evening 多在见面时说，Good night 多在道别或睡前说。',
 'One evening, we noticed that the light was not spread evenly across the room.\n\n一天晚上，我们发现房间里的光照分布不均。','even evenly uneven evening evensong')

TRY=[['古法语／盎格鲁诺曼语 trier → 中古英语 trien','挑选、筛分、检验，也有审理案件义'],['英语 try','试；尝试；检验；审理']]
W('try','/traɪ/','尝试；试用；审理；考验',
 '还不知道行不行，先做一次、检查一次，让结果告诉你。',
 '来自法语 trier 一系，经中古英语 trien，早期有挑选、检验、审理义；更远词源未完全确定，不强接某个看起来相似的拉丁词。',TRY,
 'try to do 是努力去做；try doing 常说试试某种办法看效果。try a case 是审理案件。try on clothes 是试穿，而不是把每种 try 都译成努力。',
 'try to do；try doing；try on；give it a try。',
 'try to open the door 侧重努力开门；try opening the window 侧重把开窗当成解决办法试试。两种结构可能重叠，但关注点不同。',
 ('I tried to call you, but the line was busy.','我试着给你打电话，但占线。'),('Try adding a little lemon juice.','试着加一点柠檬汁看看。'))
W('trying','/ˈtraɪɪŋ/','令人难受的；难熬的；try 的 -ing 形式',
 '一件事不断消耗耐心，让人忍着、撑着，感觉正在接受考验。',
 'try + -ing；除了普通分词，还由 try“考验、使受苦”形成形容词，表示令人疲惫或心烦。',TRY+[['try + -ing → trying','尝试着；考验耐心、难熬的']],
 'a trying day 是令人难熬的一天，trying circumstances 是艰难处境；I am trying 仍可只是我正在努力。形容词义不能由进行时机械推出。',
 'a trying time；a trying experience；trying circumstances。',
 'trying 修饰经历通常说它考验人；tried 形容办法则常说经过验证。一个词尾变化就改变了观察方向。',
 ('It has been a trying week for everyone.','对大家来说，这一周都很难熬。'),('Her calm manner helped us through a trying situation.','她镇定的态度帮我们度过了困难处境。'))
W('tried','/traɪd/','经过试验的；可靠的；try 的过去式、过去分词',
 '办法不是第一次听说，而是实际拿去用过，已经知道它行不行。',
 'try 的 y 变 i 加 -ed；中古英语已有相应形式。分词作形容词可强调经过检验。',TRY+[['try + -ed → tried','试过；经过验证的']],
 'a tried method 是试过、可靠的方法；tried and tested／tried and true 都强调经验证可信。She tried 是她试过，不自动等于成功。',
 'a tried method；tried and tested；tried and true。',
 'tried 只由动词作过去式时，不保证尝试成功；作为固定修饰语 tried and tested 才突出可靠。',
 ('We used a tried and tested approach.','我们用了经过验证的办法。'),('I tried the new app yesterday.','我昨天试用了这个新应用。'))
W('trier','英 /ˈtraɪə/；美 /ˈtraɪər/','肯努力的人；尝试者；事实裁断者〔法律〕',
 '也许还不是最强的，但一次不行还会继续试，是个肯下工夫的人。',
 '联系中古英语 triour、盎格鲁诺曼语相应人物名词及 try 动词；现代可对应 try + -er。法律义保留检验、审理这一支。',TRY+[['try／法语相关人物形式 → trier','尝试者；审查、裁断的人']],
 '英式 He’s a trier 常夸肯努力。法律 trier of fact 指判断事实的裁断者，这个角色不是只按字面“试一下的人”来理解。',
 'a real trier；a willing trier；a trier of fact。',
 'trier 不等于 winner：愿意努力与是否获胜是两个评价。法律用法也与日常努力者不同。',
 ('She may be inexperienced, but she is a real trier.','她或许经验不足，但确实肯努力。'),('The textbook explains the role of the trier of fact.','教材解释了事实裁断者的角色。'))
W('retry','/ˌriːˈtraɪ/','重试；重新审理',
 '第一次没完成、没成功或需要重来，就再按一次“试”。',
 're-（再次）+ try（尝试、审理），前缀对不同动词义都可起作用。',TRY+[['re- + try → retry','再尝试；再审理']],
 '网络操作 click Retry 是重试；retry a case 是重新审理案件。重试是否安全或会不会重复提交，取决于具体系统，不由词名保证。',
 'retry the connection；click Retry；retry a case。',
 'retry 是再次尝试，undo 是撤销已做动作，restart 是重新启动；三个动作可能配合，但不是一个按钮意思。',
 ('Please retry the connection in a few minutes.','请几分钟后重新尝试连接。'),('The exercise lets students retry any question they answered incorrectly.','练习允许学生重做答错的题。'))
R('B3724','试；检验；审理','TRY：先做一次，让结果接受检验','未知能否打开的门，先推一推；方案也先试一轮。',
 'try 从法语挑选、检验一系进入英语，同时保留审理案件等用法。trying 可以说难熬，tried 可以说经验证，不能只把后缀当时态标签。',
 'try → trying 保留 y，try → tried 则 y 变 i；trier 是人，retry 是再做。历史的检验、审理义也参与这些词，不统一压成“尝试”。',
 [['动作与再试','try · retry'],['考验与经验证','trying · tried'],['尝试、裁断的人','trier']],
 'try to do 偏努力达成；try doing 偏试试这个办法。trying day：难熬的一天；tried method：经验证的办法。',
 'If the first attempt fails, retry using a tried and tested method.\n\n第一次失败后，用经过验证的方法再试一次。','try trying tried trier retry')

FEEL=[['古英语 fēlan → 中古英语 felen','触觉感知、察觉'],['英语 feel','感到；触摸；给人某种感觉']]
W('feel','/fiːl/','感觉；觉得；触摸；摸起来',
 '手指摸到表面，也把心里的冷暖、情绪和判断感知出来。',
 '接古英语 fēlan，经中古英语 felen 延续。现代过去式和过去分词 felt，不用 feeld。',FEEL,
 'feel cold 是觉得冷；feel the fabric 是摸布料；The fabric feels soft 是布料摸起来柔软。I feel that… 还能提出主观判断，不必真有身体触觉。',
 'feel tired；feel like doing；feel that；get a feel for。',
 'feel 是自身感知或触觉，look 是外观，sound 是听感。feel + 形容词常作连系结构，不机械补成 feel softly。',
 ('The blanket feels soft and warm.','这条毯子摸起来柔软暖和。'),('I feel that we should discuss this together.','我觉得我们应该一起讨论这件事。'))
W('feeling','/ˈfiːlɪŋ/','感觉；感情；直觉；感受的',
 '身体传回一个信号，心里也留下喜悦、委屈或一种说不清的预感。',
 'feel + -ing；接中古英语相应形式，既可为动词形式，也可作独立名词。',FEEL+[['feel + -ing → feeling','感知这一过程；感觉、情绪或直觉']],
 'a strange feeling 是一种奇怪感觉，hurt someone’s feelings 是伤害感情，have a feeling that 是隐约觉得。feeling 的单复数随所指变化，不能只背成一个固定的“感情”。',
 'a feeling of；hurt someone’s feelings；have a feeling that；with feeling。',
 'feeling 可能是主观感受，evidence 是支持判断的证据。have a feeling 不等于已证明某事。',
 ('I had a feeling that we had met before.','我隐约觉得我们以前见过。'),('She did not mean to hurt his feelings.','她不是故意伤害他的感情。'))
W('felt','/felt/','感到过；feel 的分词；毛毡〔另源〕',
 '一条线把感觉放到过去；另一条线是一层纤维压缠成的布状材料。',
 '感到义是 feel 的不规则过去式、过去分词，历史关联古英语 fēled 等形式；毛毡名词另接古英语 felt。两个近源不同，不能用“摸起来有感觉”解释毛毡的来历。',
 [['并行来源：feel 的旧过去形式；古英语 felt','感到过；毛毡材料'],['英语 felt','feel 的过去式、分词；另有毡名词及毡化动词']],
 'I felt relieved 是我当时松了口气；a felt hat 是毡帽。felt material 通常不靠织经纬线形成，具体生产方式另有技术细节。',
 'felt better；felt that；a felt hat；a piece of felt。',
 'fell 是 fall 的过去式；felt 是 feel 的过去式。材料 felt 不是感觉动词一条顺畅派生出来的名词。',
 ('I felt much better after a short rest.','短暂休息后，我感觉好多了。'),('She cut a small circle from the blue felt.','她从蓝色毛毡上剪下一小块圆形。'))
W('feeler','英 /ˈfiːlə/；美 /ˈfiːlər/','触角；试探；探询意向的动作',
 '先伸出一根触角碰碰周围，再决定往哪里走；谈合作时也可以先探口风。',
 'feel + -er，-er 表执行或起作用的东西。人物义较早，动物感知器官义与后来的试探性提议都利用 feel 的感知方向。',FEEL+[['feel + -er → feeler','感知者或器官；试探性接触']],
 '昆虫 feelers 是触角；put out feelers 是先向相关人探询是否有意愿，不是已经正式下结论或达成协议。',
 'an insect’s feelers；put out feelers；send out feelers。',
 'feeler 是试探性接触，offer 是提出可接受或拒绝的方案；探口风通常比正式报价更早、更不确定。',
 ('The insect moved its feelers across the leaf.','昆虫让触角扫过叶片。'),('We put out feelers to see whether anyone wanted to join.','我们先探了探口风，看有没有人想加入。'))
W('mouthfeel','/ˈmaʊθfiːl/','口感',
 '食物进嘴后，除了甜酸咸，还能感觉到顺滑、粗糙、酥脆或稠厚。',
 'mouth（嘴）+ feel（触感），组成描述饮食在口中物理感受的名词。',C('mouth','feel','mouthfeel','饮食在口中产生的质地、触觉感受'),
 '饮品、巧克力等品评常见。creamy mouthfeel 强调口中顺滑浓厚的感觉，不直接证明用了奶油。',
 'a smooth mouthfeel；a creamy mouthfeel；improve mouthfeel。',
 'taste 侧重味觉，mouthfeel 侧重触感、质地；日常中文“口感”可能包得更宽，翻译时看作者具体说什么。',
 ('The soup has a rich, creamy mouthfeel.','这道汤入口浓厚顺滑。'),('The two chocolates taste similar but have different mouthfeels.','这两种巧克力味道相近，但口中质地不同。'))
R('B2857','感觉；触摸；察觉','FEEL：身体碰到，心里也感到','摸毯子觉出柔软，收到好消息感到轻松，两种感受都可用 feel。',
 'feel 接古英语 fēlan，延伸到情绪和主观判断。feeling 是感觉、情感或直觉；feeler 是触角，也能比喻探口风；mouthfeel 单说食物在口中的触感。',
 'feel／felt／felt 不规则变化。felt 的毛毡名词另源，不能因同形就反推来源。feely 在原词典里有不同、较少用分析，本页先略；常见的口语表达也不应靠这一个片段包办。',
 [['感知与过去形式','feel · felt'],['感受与试探','feeling · feeler'],['饮食触感','mouthfeel']],
 'felt 是 feel 的过去式；fell 是 fall 的过去式。feeling 可能主观，不能直接当证据；mouthfeel 也不等于所有味觉。',
 'I felt the cloth and had a feeling that it would make a comfortable blanket.\n\n我摸了摸布料，觉得它做成毯子会很舒服。','feel feeling felt feeler mouthfeel')

if __name__=='__main__':save('continuation_20261028_g',ROOTS,WORDS)
