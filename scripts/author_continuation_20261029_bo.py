"""Food, level, history: useful base families and genuine historical links."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
def C(a,b,w,m):return [[a+'；'+b,'并列构词部分'],[w,m]]
F=[['古英语 fōda → 中古英语 fode / foode','食物'],['英语 food','供人或动物吃、维持生长的东西']]
W('food','/fuːd/','食物；食品',
 '让身体吃下去、从中获得养分的东西；也可借说给思想提供材料。',
 '继承古英语 fōda，经中古英语 fode 等形式发展。与 feed 有历史亲缘，但不能把现代 food 硬拆成 fo + od。',F,
 'buy food 买吃的；food for thought 是值得思考的材料。food 常统称食物，foods 则能强调不同种类的食品。',
 'fresh food；pet food；a variety of foods；food for thought。',
 'food 是吃的东西，meal 是一次用餐或一顿饭，dish 可以是一道菜。说三顿饭通常是 three meals。',
 ('We bought enough food for the whole weekend.','我们买了足够整个周末吃的食物。'),('Her question gave me plenty of food for thought.','她的问题给了我很多值得思考的东西。'))
W('foodie','/ˈfuːdi/','美食爱好者',
 '不只是饿了吃饭，还喜欢研究、品尝和谈论食物的人。',
 'food + 非正式称人后缀 -ie，形成现代称呼；20世纪后期在餐饮写作中流行。',F+[['food + -ie → foodie','食物 → 对食物有浓厚兴趣的人']],
 'a foodie destination 美食爱好者喜欢去的地方；a foodie friend 喜欢探店、研究吃喝的朋友。通常偏轻松口语。',
 'a keen foodie；a foodie destination；foodie culture。',
 'foodie 不自动等于专业厨师或美食评论家，也不只指饭量大的人。',
 ('My foodie friend always knows where to find good noodles.','我那位爱研究美食的朋友总知道哪家的面好吃。'),('The old market has become a popular destination for foodies.','老市场成了美食爱好者的热门去处。'))
W('seafood','/ˈsiːfuːd/','海鲜；食用鱼类、贝类等水产',
 '把从水里来的、供食用的鱼贝等看成一类食品。',
 'sea 海 + food 食物。词面是海里的食物，现代使用范围有时也包括食用淡水水产，不能只凭 sea 机械划边界。',C('sea 海','food 食物','seafood','供食用的鱼、贝类等水产'),
 'a seafood restaurant 海鲜餐厅，seafood pasta 海鲜意面。食材可以来自捕捞，也可以来自养殖；名称不自动说明来源方式。',
 'fresh seafood；a seafood restaurant；a seafood platter。',
 'seafood 强调食材、食品这个类别；sea animals 是海洋动物，并不是每种海洋动物都按食品来谈。',
 ('The restaurant serves rice with mixed seafood.','这家餐厅供应配多种海鲜的米饭。'),('We stopped at a small seafood restaurant near the harbour.','我们在港口附近一家小海鲜餐厅停下来吃饭。'))
W('foodservice','英 /ˈfuːdsɜːvɪs/；美 /ˈfuːdsɜːrvɪs/','餐饮服务；供餐行业',
 '把食物准备好、供应给别人吃的一整类服务和生意。',
 'food 食品 + service 服务，形成行业名称；也常分写 food service。',C('food 食物','service 服务','foodservice','准备、供应餐食的服务或行业'),
 'the foodservice industry 餐饮服务业，可包括餐厅、食堂、机构供餐等。foodservice equipment 是行业使用的厨房、供餐设备。',
 'the foodservice industry；a foodservice company；foodservice equipment。',
 'foodservice 不只指送外卖，food delivery 才特别强调配送；也不等于食品制造全部行业。',
 ('She designs kitchen equipment for the foodservice industry.','她为餐饮服务业设计厨房设备。'),('The college hired a new foodservice company for its dining hall.','学院为食堂聘用了一家新的供餐公司。'))
W('foodborne','英 /ˈfuːdbɔːn/；美 /ˈfuːdbɔːrn/','经食物传播的；食源性的',
 '食物像载体一样把致病因素带给吃的人。',
 'food 食物 + borne 携带、传播的；borne 是 bear 承载的过去分词形式，不是 born 出生。',C('food 食物','borne 被携带、传播','foodborne','通过食物传播的'),
 'foodborne illness 食源性疾病；foodborne pathogens 经食物传播的病原体。先理解传播途径，不要把它读成食物本身出生了。',
 'foodborne illness；foodborne disease；foodborne pathogens。',
 'foodborne 强调通过食物这一途径传播，不等于所有吃完饭后出现的不舒服；词源也不是 food + born。',
 ('The report discusses the causes of foodborne illness.','报告讨论食源性疾病的成因。'),('The course includes a section on foodborne pathogens.','这门课有一个部分介绍食源性病原体。'),sources=['https://en.wiktionary.org/wiki/foodborne#English','https://dictionary.cambridge.org/us/dictionary/english/foodborne'])
R('B2496','食物；食品；供餐及传播途径','FOOD：供身体吃，也可给思想提供材料','食物是核心；爱研究它的人是 foodie，提供餐食的行业是 foodservice。',
 'food 接古英语 fōda。复合词里先确定它与另一部分的关系：sea 说食品类别，service 说服务，borne 说传播途径。',
 'food → foodie；seafood、superfood 是食品类别名称；foodservice 是行业，foodborne 是经食物传播的。',
 [['基本词与美食爱好者','food · foodie'],['食品类别与服务','seafood · superfood · foodservice'],['作为传播载体','foodborne']],
 'food 与 meal 不同；foodservice 不只外卖；foodborne 中 borne 是承载，不是出生。',
 'The foodie chose a seafood restaurant for our evening meal.\n\n这位美食爱好者为我们的晚餐选了一家海鲜餐厅。',
 'food foodie seafood superfood foodservice foodborne')
L=[['拉丁语 libra → 指小型器具的 libella','天平 → 小天平、水准器'],['古法语 livel → 中古英语 level → 英语 level','水准器 → 水平、同一高度 → 程度、等级']]
W('level','/ˈlevəl/','水平的；程度、等级、层；使平整、使持平',
 '先想一条水平线：同这条线一样高，就是齐平；再把这条线当作衡量能力、数量的刻度。',
 '经古法语 livel 来自拉丁语 libella 小天平、水准器，后者由 libra 天平加指小形式形成。英语借入后发展出水平、层次、程度以及使平整等用法。',L,
 'a level floor 平的地面；water level 水位，skill level 技能水平。level the ground 平整地面；level with someone 是坦诚相告。',
 'at the same level；a high level of skill；sea level；level the score；level with someone。',
 'flat 强调表面平，没有明显凹凸；level 强调不倾斜、等高。一个平整的斜坡可以 flat，但不 level。',
 ('Use this tool to check that the shelf is level.','用这个工具检查架子是否水平。'),('The class includes students at different skill levels.','这个班有不同技能水平的学生。'),('I’ll level with you: the work will take longer than we expected.','我跟你说实话：这项工作会比预计花更长时间。'))
W('leveller','英 /ˈlevələ/；美 /ˈlevələr/','使差距缩小的因素；平整工具或平整者',
 '把原来有高低差的东西拉到差不多一条线上；也可让人的地位、机会差距缩小。',
 'level + -er，英式拼写常双写 l；美式常写 leveler。由使平整的动作发展出消除差别的事物或因素。',L+[['level → leveller','使齐平 → 使差距缩小的人、工具或因素']],
 'a great leveller 常比喻让不同地位的人面临相似处境的因素；不必真是一件刮平土地的工具。',
 'a great leveller；a social leveller；a ground leveller。',
 'leveller 是起拉平作用的人或因素，level 是水平或程度。历史上首字母大写的 Levellers 另可指特定政治群体。',
 ('In the competition, the unfamiliar rules were a great leveller.','比赛中，大家都不熟悉的规则大大缩小了彼此的优势差距。'),('The report describes education as a possible social leveller.','报告把教育描述为可能缩小社会差距的因素。'))
R('B3915','水平；程度、等级；拉平','LEVEL：用一条水平线看高低','水准器帮人看是否平；把同样的高低画面借给技能、数量和社会差距，就有多种抽象用法。',
 '从拉丁语 libra 天平到指小形式 libella 水准器，经古法语 livel 进入英语。现代不要硬拆 le + vel。',
 'level → leveller；multi- + level → multilevel。',
 [['水平、程度与使平整','level'],['拉平差距与多个层级','leveller · multilevel']],
 'flat 表面平整，level 不倾斜或同高；leveller 可比喻缩小差距的因素。',
 'The shelf is level, but the two shelves are at different levels.\n\n架子是水平的，但两个架子处在不同高度。',
 'level leveller multilevel')
H=[['古希腊语 historía','探究所得的知识；记述'],['拉丁语 historia → 古法语 estoire / estorie → 中古英语 historie','叙述、纪事'],['英语 history','过去发生的事；关于过去的记录与研究']]
W('history','/ˈhɪstəri/','历史；历史学；以往经历、记录',
 '把过去发生的事追查清楚、记下来，逐渐成为我们说的历史。',
 '经法语、拉丁语追到希腊语 historía 探究、探究所得的记述。不是英语 his 他的 + story 故事；story 与它有同源关系，但现代词义已有分工。',H,
 'study history 学历史；the history of a town 一座城的历史；a history of problems 过去反复出现问题的记录。make history 是创造历史，be history 口语可表示已成过去、不再重要。',
 'world history；a family history；make history；go down in history；a history of something。',
 'history 关注实际过去、相关记录或研究；story 是故事，可以真实，也可以虚构。两者同源不代表现代能随便互换。',
 ('She is researching the history of the old railway.','她正在研究这条老铁路的历史。'),('This building has a long history of use as a school.','这座建筑长期以来都被用作学校。'),('The victory made history for the club.','这场胜利为俱乐部创造了历史。'))
W('historian','英 /hɪˈstɔːriən/；美 /hɪˈstɔːriən/','历史学家；历史研究者、记述者',
 '不只是记住几个年代，而是研究、解释过去的人。',
 '中古英语 historian / historien 有法语、拉丁语历史词族背景；现代可按 histor(y) + -ian 理解这个从事历史研究的人名词。',H+[['historia 词族 → historian','历史、记述 → 历史研究或写作者']],
 'a local historian 地方史研究者，an art historian 艺术史研究者。专业方向可以是政治、城市、艺术等。',
 'a local historian；an economic historian；historians argue that...。',
 'historian 是研究历史的人，historical 是与历史有关的，historic 是具有历史重要性的。不要凭词长猜成三种职业。',
 ('A local historian showed us photographs of the old market.','一位地方史研究者给我们看了老市场的照片。'),('Historians disagree about why the settlement was abandoned.','历史学家对这处聚落为何被遗弃有不同看法。'))
W('historic','英 /hɪˈstɒrɪk/；美 /hɪˈstɔːrɪk/','具有历史意义的；历史上重要的',
 '这件事值得被历史记住，而不只是发生过。',
 '借自拉丁语 historicus，其上接希腊语 historikós；现代可以 history 词干 + -ic 帮助理解。现代常用义突出历史重要性。',H[:2]+[['希腊语 historikós → 拉丁语 historicus → 英语 historic','关于历史的 → 常强调历史上重要的']],
 'a historic decision 具有历史意义的决定；a historic building 有历史重要性的建筑。今天刚发生的事也可称 historic，只要认为其影响重大。',
 'a historic moment；a historic victory；a historic agreement。',
 'historic 常带重要、值得铭记的评价；historical 通常只说与过去或历史研究有关。不是所有历史资料中的小事都要称 historic。',
 ('The first successful flight was a historic achievement.','首次成功飞行是一项具有历史意义的成就。'),('Residents gathered to mark the town’s historic anniversary.','居民聚在一起纪念这座城具有历史意义的周年日。'),sources=['https://en.wiktionary.org/wiki/historic#English','https://dictionary.cambridge.org/grammar/british-grammar/historic-or-historical'])
W('historical','英 /hɪˈstɒrɪkəl/；美 /hɪˈstɔːrɪkəl/','历史的；与过去有关的',
 '把一件事放在过去的时间里考察；不必给它加上重大意义。',
 '在来自拉丁语 historicus 的词族基础上加 -al；现代可看成 historic + -al，或 history 对应的 -ical 形容词形式。',H+[['historicus 词族 + -al → historical','与历史、过去有关的']],
 'historical records 历史记录；a historical novel 历史小说，情节可以虚构，但设在历史背景中；historical data 过去的数据。',
 'historical evidence；a historical novel；historical context；historical data。',
 'historical 常说与历史有关；historic 常说历史上重要。历史小说不自动是重要到载入史册的小说。',
 ('The museum keeps historical records of the harbour.','博物馆保存着这个港口的历史记录。'),('The novel mixes fictional characters with historical events.','这部小说把虚构人物与历史事件结合起来。'),sources=['https://en.wiktionary.org/wiki/historical#English','https://dictionary.cambridge.org/grammar/british-grammar/historic-or-historical'])
W('historically','英 /hɪˈstɒrɪkli/；美 /hɪˈstɔːrɪkli/','历史上；从历史角度看',
 '暂时把镜头拉到过去，看长久以来或在某个历史时期是什么情况。',
 'historical + -ly，形成副词；-ically 的常见读音不必把每个字母各读成一拍。',H+[['historical → historically','与历史有关的 → 从历史来看、在过去']],
 'historically important 历史上重要的；historically accurate 符合史实的。句首 Historically, ... 常是在交代过去背景，不等于宣告一件新事物载入史册。',
 'historically speaking；historically accurate；historically important。',
 'historically 通常说明历史角度、过去情况；不等于 historic 所带的重大意义，也不是 hysterically 情绪失控地。',
 ('Historically, the town depended on river trade.','历史上，这座城依靠河运贸易。'),('The costumes are beautiful but not historically accurate.','这些服装很好看，却不符合史实。'))
R('B3416','历史；记录与研究过去','HISTORY：探究过去，形成记述','历史既是过去发生的事，也可以是人们对这些事的研究、解释和记录。',
 '希腊语 historía 有探究、探究所得记述义，经拉丁语和法语进入英语。history 与 story 同源，但不是 his + story。',
 'history → historian；historic、historical 并排比较，再接 historically；prehistory、prehistoric 看文字记载之前的时期。',
 [['过去与研究者','history · historian'],['重要性、关联与历史角度','historic · historical · historically'],['文字记载前的时期','prehistory · prehistoric']],
 'historic 重要到值得历史记住，historical 与过去或历史研究有关；history 不是 his story 的历史拼接。',
 'The historian checked historical records before describing the historic event.\n\n历史研究者先查阅历史记录，再描述那件具有历史意义的事件。',
 'history historian historic historical historically prehistory prehistoric')
if __name__ == '__main__':save('continuation_20261029_bo',ROOTS,WORDS)
