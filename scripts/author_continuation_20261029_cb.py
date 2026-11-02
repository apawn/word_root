"""Ground: earth, support, evidence and conventional compounds."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
def C(a,b,w,m):return [[a+'；'+b,'并列构词部分'],[w,m]]
GR=[['古英语 grund → 中古英语 ground','底部、地面、基础'],['英语 ground','地面、场地；理由根据；动词可说奠基、停飞、禁足等']]
W('ground','/ɡraʊnd/','地面；场地；基础、根据；奠基、停飞、禁足',
 '地面托住脚，基础托住事情；一个判断也需要有根据托着，才站得住。',
 '继承古英语 grund，经中古英语 ground 发展。ground coffee 中 ground 却是 grind 研磨的过去分词；现代构词要另看，不能解释成地面咖啡。',GR,
 'on the ground 在地上；sports ground 运动场；grounds for concern 担忧的理由。ground aircraft 是让飞机停飞，ground a child 是罚孩子不许外出。common ground 是共同点、共识。',
 'on the ground；school grounds；grounds for；on the grounds that；common ground；ground a plane。',
 'ground 地面、基础，floor 常说建筑物内地板或楼层；coffee grounds 是咖啡渣，与 grind 的研磨分支相关。',
 ('The bag fell to the ground.','包掉在地上。'),('We have good grounds for questioning the result.','我们有充分理由质疑结果。'),('The two groups found some common ground.','两组人找到了一些共同点。'))
W('grounded','/ˈɡraʊndɪd/','有根据的；脚踏实地的；被禁足的、停飞的；接地的',
 '可以说观点落在事实基础上、人不飘；也可以说人或飞机被要求留在原处。',
 'ground + -ed，来自地面、奠基、限制离开等不同动词用法。现代形容词的具体意思不能只靠一个中文接地气涵盖。',GR+[['ground → grounded','奠基、留在地面等 → 有基础、务实、被禁足或停飞']],
 'grounded in evidence 以证据为基础；stay grounded 保持务实；be grounded for a week 被禁足一周。电气语境还可说已接地，尤其美式。',
 'grounded in reality；stay grounded；be grounded for a week；grounded aircraft。',
 'grounded 务实不等于 boring 无聊；grounded aircraft 是被停飞，不只是飞机眼下碰着地。',
 ('Her advice is grounded in years of practical experience.','她的建议建立在多年实践经验上。'),('Success has not stopped him from staying grounded.','成功没有让他失去脚踏实地的态度。'),('In the story, he is grounded for breaking the family rules.','故事里，他因违反家规被禁足。'))
W('grounding','/ˈɡraʊndɪŋ/','基础知识、基本训练；停飞；搁浅；接地',
 '学习上像先铺一层稳固地基；其他语境则跟随 ground 的停飞、搁浅或接地用法。',
 'ground + -ing，活动或结果名词。基本训练取基础义，飞机停飞取留在地面义，各自看语境。',GR+[['ground → grounding','基础、停飞等动词用法 → 基础训练、相应活动或事件']],
 'a good grounding in mathematics 扎实数学基础；the grounding of aircraft 飞机停飞。课程介绍里看到 grounding，多数是在谈基本知识训练。',
 'a solid grounding in；a basic grounding in；the grounding of a ship。',
 'a grounding in 是在某领域打下基础，不等于已经精通所有高级内容；grounding 也不只属于电气领域。',
 ('The course gives students a solid grounding in statistics.','课程为学生打下扎实的统计学基础。'),('The investigation examined the causes of the ship’s grounding.','调查分析了船舶搁浅的原因。'))
W('groundless','/ˈɡraʊndləs/','没有根据的；无理由的',
 '说法下面没有地基，撑不起这个结论。',
 'ground 根据、理由 + -less 没有，构成缺乏依据的形容词；不是说某地没有地面。',GR+[['ground + -less → groundless','根据 → 缺少根据的']],
 'groundless fears 无根据的担忧，a groundless accusation 无端指控。强调没有充分基础，不只是说别人不喜欢这句话。',
 'groundless rumours；a groundless claim；prove groundless。',
 'groundless 是缺乏根据，false 是不真实，两者常相关但观察角度不同；一个说法暂没根据，不代表仅凭该词就完成了事实证明。',
 ('The report found the accusation to be groundless.','报告认定那项指控没有根据。'),('Her fear that nobody would attend proved groundless.','她担心无人参加，后来证明是多虑了。'))
W('groundbreaking','/ˈɡraʊndbreɪkɪŋ/','开创性的；动工破土的',
 '把原来没开过的地面打破、开辟出来，再借说研究、设计打开新路。',
 'ground 地面 + breaking 破开；从建筑破土的组合意象发展为创新、开创的形容词，也保留动工活动用法。',C('ground 地面、未开辟领域的意象','breaking 破开','groundbreaking','破土 → 开创性的'),
 'groundbreaking research 开创性研究；a groundbreaking ceremony 破土动工仪式。不是所有新推出的产品都客观达到开创性的程度，这可能是评价或宣传。',
 'groundbreaking work；a groundbreaking discovery；a groundbreaking ceremony。',
 'groundbreaking 强调开创新路；new 只说明新，二者并不等强。建筑仪式里则可能是字面破土。',
 ('The exhibition celebrates her groundbreaking work in design.','展览纪念她在设计领域的开创性工作。'),('The town held a groundbreaking ceremony for the new library.','小城为新图书馆举行了破土动工仪式。'))
W('underground','形容词、副词 /ˌʌndəˈɡraʊnd/，美 /ˌʌndərˈɡraʊnd/；名词常 /ˈʌndəɡraʊnd/，美 /ˈʌndərɡraʊnd/','地下的、地；地铁；秘密的、非主流的',
 '字面是地表下面；看不见、公开渠道之外的活动，也会被借说成地下。',
 'under 在下面 + ground 地面，早期已有相关组合。后来用于地下交通、秘密组织、非主流文化等不同场景。',C('under 在下面','ground 地面','underground','地表之下 → 地下交通；秘密或非主流活动'),
 'an underground car park 地下停车场；travel by underground 坐地铁，英式常见。underground music 地下音乐通常指主流商业渠道之外，不自动表示违法。',
 'underground tunnels；go underground；underground music；the Underground。',
 'underground 秘密、地下与 illegal 违法不同；一条地下管线合法，一种非主流文化也可能完全公开。',
 ('The cables run underground beneath the road.','电缆埋在道路下方。'),('The club became known for its underground music scene.','这家俱乐部因其非主流音乐圈而闻名。'))
W('overground','英 /ˌəʊvəˈɡraʊnd/；美 /ˌoʊvərˈɡraʊnd/','地面上的；地上运行的',
 '与钻到地表下面相对，路线、活动在地表上方。',
 'over 在上方 + ground 地面，形成地上、地面上的形容词或副词；交通语境常与 underground 对比。',C('over 在上方','ground 地面','overground','地面上、地表以上'),
 'an overground railway 地面铁路；an overground section 地上路段。重点是与地下路段区分，不代表必须架在高架桥上。',
 'an overground railway；overground trains；an overground route。',
 'overground 不等于一定 elevated 高架的；一条贴近地表的铁路也可以与地下线路相对称为 overground。',
 ('The train moves from a tunnel onto an overground section.','列车从隧道开到地上路段。'),('The map shows both underground and overground routes.','地图同时标出了地下和地上线路。'))
W('foreground','英 /ˈfɔːɡraʊnd/；美 /ˈfɔːrɡraʊnd/','前景；显著、重要的位置；突出某事',
 '看一幅画，离观看者近、先抓住眼睛的那一层，是前景。',
 'fore 前方 + ground 场域、画面部分，形成前景名称；再引申为关注焦点，动词表示把某事突出。',C('fore 前面','ground 场域、画面部分','foreground','画面前景 → 关注焦点；突出'),
 'in the foreground 在前景中；foreground an issue 突出某个问题。可以说照片布局，也可以说文章、讨论把什么放到最显著的位置。',
 'in the foreground；bring something to the foreground；foreground a concern。',
 'foreground 靠前或受到突出关注，background 背景；靠近画面的人不一定就是故事最重要的人物。',
 ('A red bicycle stands in the foreground of the photograph.','照片前景中停着一辆红色自行车。'),('The article foregrounds the experiences of local workers.','文章突出呈现了当地工人的经历。'))
W('battleground','英 /ˈbætəlɡraʊnd/；美 /ˈbætəlɡraʊnd/','战场；争夺、冲突的领域',
 '双方在同一片地方较量；比喻时，这片地方可以是一项政策、一个市场。',
 'battle 战斗、争夺 + ground 场地，形成战斗地点名称，再借说激烈争夺的领域。',C('battle 战斗、争夺','ground 场地','battleground','战场 → 争夺领域'),
 'a political battleground 政治角力场，a battleground over policy 围绕政策的争夺领域。文章说学校成了 battleground，未必发生实战。',
 'a key battleground；a political battleground；become a battleground。',
 'battleground 与 battlefield 都可说战场；比喻用法不能仅凭一个词就判断发生了真实武装冲突。',
 ('The old fort overlooked a historic battleground.','古堡俯瞰着一处历史战场。'),('Online advertising has become a battleground for small businesses.','网络广告成了小企业争夺的领域。'))
W('campground','英 /ˈkæmpɡraʊnd/；美 /ˈkæmpɡraʊnd/','露营地',
 '一片允许、安排人扎营的场地，可能划分出多个营位。',
 'camp 露营 + ground 场地，按用途命名。美式英语中很常见，不是研磨营地。',C('camp 露营','ground 场地','campground','供露营的场地'),
 'a riverside campground 河边营地；a campground with showers 有淋浴设施的营地。具体设施要看说明，词本身不保证都有水电。',
 'a public campground；stay at a campground；a campground entrance。',
 'campground 常说整个营地；campsite 可指整个营地，也可指其中一个营位，具体按地区和语境。',
 ('We stayed at a small campground near the lake.','我们住在湖边一处小营地。'),('The campground has twenty marked pitches for tents.','营地划出了二十个帐篷营位。'))
W('fairground','英 /ˈfeəɡraʊnd/；美 /ˈferɡraʊnd/','游乐场；集市、游艺活动场地',
 '一片举行集市、游乐活动的场地，可能摆着游乐设施和摊位。',
 'fair 集市、游艺活动 + ground 场地。这里 fair 不是公平的，而是另一个名词用法。',C('fair 集市、游艺活动','ground 场地','fairground','举行集市、游乐活动的场地'),
 'fairground rides 游乐场设施，a fairground stall 集市摊位。常见复数 fairgrounds 也可以说展销、集市场地。',
 'fairground rides；a fairground stall；the county fairgrounds。',
 'fairground 不等于公平的土地；playground 主要是儿童等玩耍场地，fairground 常有游艺、集市活动背景。',
 ('The fairground was bright with lights and music.','游乐场灯火通明，音乐阵阵。'),('We bought roasted nuts from a fairground stall.','我们从游乐集市摊位买了烤坚果。'))
W('aground','/əˈɡraʊnd/','搁浅的、地；被困住的比喻',
 '船本应在水里浮着，却碰上水下地面，走不动了。',
 'a- 在……上 + ground 地面，中古英语 on grounde 等表达发展为 aground，常用于船舶搁浅。',GR+[['on grounde / a- + ground → aground','碰到水下地面 → 搁浅']],
 'run aground 搁浅；a plan runs aground 计划受阻，是借船停住的比喻。不是船每次正常停靠岸边都叫 aground。',
 'run aground；go aground；a ship aground。',
 'aground 是搁浅，ashore 是上岸、在岸上；船搁浅时，乘客不一定已经上岸。',
 ('The fishing boat ran aground near the harbour entrance.','渔船在港口入口附近搁浅了。'),('Their plans ran aground when the funding disappeared.','资金没了，他们的计划也搁浅了。'))
W('groundswell','/ˈɡraʊndswel/','海涌；不断增强的民意、支持或反对声浪',
 '一股宽阔的涌浪慢慢抬起来；公众情绪从许多地方汇聚，也能形成这样的势头。',
 'ground + swell 涌起的旧组合，原有海洋涌浪义；后来借波浪上升形容广泛民意增强。不要把名字硬说成海底真的整体抬升。',C('ground 旧组合中的成分','swell 涌浪、增强','groundswell','海涌 → 逐渐汇聚、增强的民意声浪'),
 'a groundswell of support 越来越广泛的支持；a groundswell of opposition 不断增强的反对。通常强调社会层面的广泛趋势，不是某个人突然一声喊。',
 'a groundswell of support；a groundswell of anger；a growing groundswell。',
 'groundswell 不自动代表全体人赞同，也不是一次精确统计；读报道时把声浪这个评价与实际数据区分。',
 ('There was a groundswell of support for saving the old cinema.','保留老电影院的呼声越来越广泛。'),('The proposal met a growing groundswell of opposition.','提议遭遇了不断增强的反对声浪。'))
W('groundhog','英 /ˈɡraʊndhɒɡ/；美 /ˈɡraʊndhɑːɡ/','美洲旱獭；一种俗称土拨鼠的啮齿动物',
 '名字像地里的猪，实际是一种掘洞生活的旱獭，和猪不是一类动物。',
 'ground 地面、地下生活场所 + hog 猪的动物比拟名称。英语普通动物名常借其他动物作形象比方，不等于科学分类。',C('ground 地面、地下','hog 猪的比拟名称','groundhog','美洲旱獭的普通名称'),
 'a groundhog burrow 美洲旱獭洞穴；也叫 woodchuck。现代文艺语境里 Groundhog Day 可借电影说仿佛不断重复的日子，不是在说每一天都有这种动物。',
 'a groundhog burrow；spot a groundhog；a groundhog near the field。',
 'groundhog 是啮齿动物、松鼠科中的一种旱獭，不是野猪；也不是把所有 marmots 旱獭都叫这个特定名称。',
 ('A groundhog disappeared into its burrow beside the field.','一只美洲旱獭钻进了田边的洞穴。'),('The sign explains that a groundhog is also called a woodchuck.','牌子说明，groundhog 也叫 woodchuck。'),sources=['https://en.wiktionary.org/wiki/groundhog#English','https://mdc.mo.gov/discover-nature/field-guide/woodchuck-groundhog'])
W('groundnut','/ˈɡraʊndnʌt/','花生，尤指作物或相关产品',
 '名称抓住果实在地下发育的特点；nut 是日常食物叫法，不等于严格植物分类里的坚果。',
 'ground 地下 + nut 坚果类食物称呼，常用来指 peanut 花生，尤其在作物、油等场景。不是把坚果磨碎的 ground nuts。',C('ground 地下','nut 日常坚果类食物名称','groundnut','花生等地下结果的作物名称'),
 'groundnut oil 花生油，groundnut production 花生产量。ground nuts 分写时，ground 可能是 grind 研磨的分词，表示磨碎的坚果。',
 'groundnut oil；groundnut farming；roasted groundnuts。',
 'groundnut 花生与 ground nuts 磨碎坚果词法不同；花生是豆科作物，不因名字有 nut 就成了树上结的所有坚果。',
 ('The recipe uses a little groundnut oil.','食谱用少许花生油。'),('The farmers grow groundnuts alongside other crops.','农民在种其他作物的同时，也种花生。'),sources=['https://en.wiktionary.org/wiki/groundnut#English','https://dictionary.cambridge.org/dictionary/english/groundnut'])
R('B2548','地面、底部；场地；基础、根据','GROUND：脚下能站稳，观点也需要站得住','地面支持身体，基础支持计划，根据支持结论。各种场地和位置复合词继续看另一部分说明了什么。',
 'ground 接古英语 grund。ground coffee、coffee grounds 的 ground 另按 grind 研磨的过去分词分支理解，不硬从土地来推。',
 'ground → grounded、grounding、groundless、groundbreaking；under/overground；background ↔ foreground；场地组 playground、battleground、campground、fairground、showground；aground、groundswell；groundhog、groundnut。',
 [['基础、根据与创新','ground · grounded · grounding · groundless · groundwork · groundbreaking'],['位置与画面','underground · overground · groundwater · background · foreground'],['各种场地','playground · battleground · campground · fairground · showground'],['搁浅、民意与名称','aground · groundswell · groundhog · groundnut']],
 'groundless 无根据，grounded in evidence 以证据为基础；groundnut 花生与 ground nuts 磨碎坚果分开；underground 不自动等于违法。',
 'A solid grounding in the subject helps us distinguish grounded arguments from groundless claims.\n\n扎实的学科基础，有助于我们分清有依据的论证和无根据的说法。',
 'ground grounded grounding groundless groundwork groundbreaking underground overground groundwater background foreground playground battleground campground fairground showground aground groundswell groundhog groundnut')
if __name__ == '__main__':save('continuation_20261029_cb',ROOTS,WORDS)
