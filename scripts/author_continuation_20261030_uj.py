"""Specialized senses of otherwise productive endings, with accurate older history."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'A1771':dict(words=['vagina','vaginal','evangelical'],label='-al：身体部位与福音相关形容词',note='vaginal 历史借自新拉丁 vaginalis，现代对应 vagin- + -al；evangelical 接较早 evangelic + -al，具体宗教派别义需超出字面构词来学。'),
 'A1699':dict(words=['kink','kinky'],label='kink 与 kinky：扭折、紧卷与语义引申',note='kink 接荷兰语绳索扭折材料；kinky 加 -y，先有卷曲义，后来又有性偏好、行为不循常规等义，按语境取义。'),
 'A1697':dict(words=['undertake','undertaker'],label='undertaker：承办业务的人如何专指殡葬业者',note='undertaker 较早泛指承揽事务的人；funeral undertaker 的专门用法后来让现代 undertaker 多指承办葬礼、安葬事务的人。'),
 'A1904':dict(words=['caliph','caliphate'],label='caliph 与 caliphate：职位、统治和领地',note='caliph 是经欧洲语言借入的阿拉伯 khalifa 继承者称号；-ate 在 caliphate 中形成职位、统治体系或领地名词，不把它当普通英语过去式 ate。'),
 'A1741':dict(words=['spank','spanking'],label='spanking 的动作义与加强语气义',note='spank + -ing 的拍打名词和 brand spanking new 的加强用法分开学；后者历史较早、来源未全确定，不能用一个拍打故事包办。'),
}
W('vagina','/vəˈdʒaɪnə/','阴道',
 '先明确它指一个具体内部通道：从外部阴道口通向宫颈的肌性管道。名称借了拉丁语鞘、套状覆盖物的旧词。',
 '作为解剖学名称借自医学拉丁语，对拉丁 vagina 鞘、剑鞘、覆盖物作专门使用。古典拉丁该词并非已经以这个解剖义使用；更远词源不定。',
 [['古典拉丁 vagina','鞘、套、覆盖物等'],['医学拉丁专门化 → 英语 vagina','解剖学中的阴道名称']],
 'the wall of the vagina 阴道壁；the opening of the vagina 阴道口；an anatomy diagram of the vagina 阴道解剖示意图。作为名词指部位本身。',
 'vagina → vaginal；the vagina and cervix。','vagina 指内部管道，vulva 指外阴，cervix 指宫颈。学部位名时把位置分清，比笼统都译成生殖器更容易读懂说明。',
 ('The textbook includes a diagram of the vagina and cervix.','教材中有阴道和宫颈的示意图。'),('The anatomy lesson explained the structure of the vagina.','解剖课讲解了阴道的结构。'),sources=['https://www.etymonline.com/word/vagina','https://www.cancer.gov/publications/dictionaries/cancer-terms/def/vagina','https://en.wiktionary.org/wiki/vagina#English'])
W('vaginal','英常 /vəˈdʒaɪnəl/；美也常 /ˈvædʒənəl/','阴道的；经阴道的',
 'vagina 是部位本身；vaginal 把这个部位接到后面的名词上，说明组织、通道或过程与它有关。',
 '历史借自新拉丁 vaginalis，源于 vagina 鞘、阴道 + 形容词 -alis；现代构词对应 vagin- + -al。较早可说鞘状结构相关，后来有现代常见解剖专门义。',
 [['拉丁 vagina → 新拉丁 vaginalis','鞘、阴道及相应形容词'],['英语 vaginal','与阴道有关、通过阴道的']],
 'vaginal tissue 阴道组织；the vaginal wall 阴道壁；vaginal birth 经阴道分娩。-al 在这里表示与某部位相关，具体关系由后面的名词决定。',
 'vaginal anatomy；vaginal delivery。','英美常见读音的重音、元音有差别；看到 vaginal 仍按同一个关系形容词理解。vagina 是名词，vaginal 用来限定后面的名词。',
 ('The diagram labels the vaginal wall.','示意图标出了阴道壁。'),('The chapter explains the term vaginal birth.','这一章解释经阴道分娩这个术语。'),sources=['https://www.etymonline.com/word/vaginal','https://en.wiktionary.org/wiki/vaginal#English'])
W('evangelical','/ˌiːvænˈdʒelɪkəl/','福音的；福音派的；热衷宣扬某种主张的；福音派基督徒',
 '最早的字面线索是好消息、福音。现代谈宗教时常是特定信仰传统的名称；谈别的事时，也可比喻像传福音一样热心劝人接受。',
 '较早 evangelic + -al，经法语、晚期拉丁福音相关材料，上接希腊 eu- 好与 angellein 宣告、angelos 使者词族。现代福音派的具体宗教含义在后来的历史中形成，不能只靠好消息三个字概括。',
 [['希腊 eu- 与宣告、使者词族 → 拉丁／法语相关词','好消息；基督教福音'],['evangelic + -al → evangelical','福音相关；后有福音派和热心宣扬的用法']],
 'an evangelical church 福音派教会；evangelical Christians 福音派基督徒，通常在新教传统中理解；evangelical about an idea 对某想法热心宣扬。',
 'evangelical beliefs；almost evangelical enthusiasm。','evangelical 与 evangelistic 都可能涉及传教，但 evangelical 也作信仰传统标签。比喻说对某事热心宣扬时，不自动表示那个人有该宗教身份。',
 ('She grew up in an evangelical church.','她在福音派教会的环境中长大。'),('He is almost evangelical about the benefits of cycling.','他对骑自行车的好处热衷宣扬，几乎逢人就讲。'),sources=['https://www.etymonline.com/word/evangelical','https://en.wiktionary.org/wiki/evangelical#English'])
W('kink','/kɪŋk/','扭结、急弯；小问题；特殊性偏好等',
 '水管突然折了一下，水流不顺，这一处折弯是 a kink。流程里还有几个卡点，也能说 a few kinks。',
 '借自荷兰语 kink 绳索扭折，早期英语见于航海等用法。由线、绳上的扭结发展出古怪想法、小毛病及特定性偏好等分支，更远来源存在推测。',
 [['荷兰语 kink → 英语 kink','绳索上的扭折、结状收缩'],['现代具体和比喻分支','急弯、流程小问题；特殊偏好']],
 'a kink in the hose 水管上的折弯；work out the kinks 排除小问题、磨合顺；a kink in the plan 计划中的小卡点。性语境中可指较不循常规的偏好。',
 'straighten out a kink；iron out the kinks。','kink 常是局部扭折或小毛病；knot 更直接说绳等打成结。流程中的 kinks 不一定意味着整个计划失败，常是还需磨合的小问题。',
 ('A kink in the hose was blocking the water.','水管上一处折弯阻住了水流。'),('We need a little time to work out the kinks in the new system.','我们需要一点时间磨合新系统、排除小问题。'),sources=['https://www.etymonline.com/word/kink','https://en.wiktionary.org/wiki/kink#English'])
W('kinky','/ˈkɪŋki/','紧密卷曲的；性偏好或行为不循常规的',
 '头发卷得紧、线缆容易形成短小扭折，是外形上的 kinky。另一个常见分支用于性偏好，意思要从场景判断。',
 'kink 扭折、急弯 + -y，早期为多扭折、卷曲的；后来出现古怪、不循常规的评价，再形成现代性语境用法。旧文献的评价色彩与现代自我描述可能不同。',
 [['kink + -y → kinky','多扭折、紧卷的'],['后来的行为、偏好引申','不循常规；性语境中特殊偏好相关']],
 'kinky hair 紧密卷曲的头发；a kinky cable 容易扭折的线缆；kinky interests 在成人性语境中指较不循常规的兴趣。',
 'naturally kinky hair；kinky preferences。','curly 泛说卷曲，kinky 常突出紧密、短小的卷；谈偏好时又是另一条现代分支。用词的评价色彩要看具体语境。',
 ('The artist carefully painted her naturally kinky hair.','画家仔细画出了她天生紧卷的头发。'),('The old cable was stiff and kinky.','旧线缆又硬又容易扭折。'),sources=['https://www.etymonline.com/word/kinky','https://en.wiktionary.org/wiki/kinky#English'])
W('undertaker','英 /ˈʌndəteɪkə/；美 /ˈʌndərteɪkər/','殡葬业者；承办葬礼、安葬事务的人',
 '家属需要有人把葬礼、运送、安葬等事务承办起来。现代 undertaker 主要就是负责这类安排的职业人员。',
 'undertake 承担、承揽，去末尾 e 加 -er。较早 undertaker 泛指承办某事、承揽生意的人；从 funeral undertaker 的专门称呼发展，现代殡葬义占主导。',
 [['undertake + -er → undertaker','承揽事务、经营业务的人'],['funeral undertaker 的专门化','承办葬礼与安葬事务的职业人员']],
 'contact the undertaker 联系殡葬业者；work as an undertaker 从事殡葬工作；the undertaker’s office 殡葬服务办公室。funeral director 也是常见职业名称。',
 'arrangements made by the undertaker；a local undertaker。','undertake 今天仍泛指承担任务；undertaker 却已主要专指一个职业。不能把 undertaker 用作所有接任务的人或一般项目承包商。',
 ('The family contacted a local undertaker to arrange the funeral.','家属联系当地殡葬业者安排葬礼。'),('He has worked as an undertaker for many years.','他从事殡葬工作已有多年。'),sources=['https://www.etymonline.com/word/undertaker','https://en.wiktionary.org/wiki/undertaker#English'])
W('caliph','/ˈkeɪlɪf/，也有 /ˈkælɪf/ 等读法','哈里发〔历史上穆斯林社群首领的称号〕',
 '称号背后的关键词是继承者：继承先知去世后社群领导职责的人。具体权力、承认范围和继承争议要放到各个时期看。',
 '经古法语 caliphe、中世纪拉丁 califa 等借入，上接阿拉伯 khalifa 继承者，来自 khalafa 接续、继承。ph 在英语里常读 /f/。',
 [['阿拉伯 khalifa','继承者；用于社群领导者的历史称号'],['拉丁、法语等形式 → 英语 caliph','英语中的哈里发称号']],
 'the title of caliph 哈里发称号；an Abbasid caliph 阿拔斯王朝的一位哈里发；the reign of a caliph 某位哈里发的统治时期。',
 'caliph → caliphate；the office of caliph。','caliph 是特定历史、宗教政治称号；不能泛指所有穆斯林国家的现代国家元首，也不等同于 imam 的所有用法。',
 ('The chapter explains how a new caliph was chosen.','这一章解释了新哈里发如何被选出。'),('The museum displayed coins issued during the caliph’s reign.','博物馆展出那位哈里发统治时期发行的钱币。'),sources=['https://www.etymonline.com/word/caliph','https://en.wiktionary.org/wiki/caliph#English'])
W('caliphate','/ˈkeɪlɪfeɪt/，也有 /ˈkælɪfeɪt/ 等读法','哈里发国、哈里发统治体系；哈里发职位',
 'caliph 是领袖称号；caliphate 把视线拉到这个职位、围绕它的统治体系或所辖领地。究竟指哪一层，由上下文决定。',
 'caliph + 名词后缀 -ate，形成统治领地、职位等名词。caliph 自阿拉伯继承者称号经欧洲语言借入；-ate 是英语接入的后缀材料。',
 [['阿拉伯继承者称号 → caliph','哈里发这一历史称号'],['caliph + -ate → caliphate','职位、统治或所辖领地']],
 'the Abbasid Caliphate 阿拔斯哈里发国；the history of the caliphate 哈里发制度或国家的历史；the end of a caliphate 某一哈里发统治体系的结束。',
 'the territory of a caliphate；different caliphates。','caliph 指称号持有者，caliphate 指职位、制度或领地。一个后缀把人名词转成相应政治单位，但各时期具体结构不能只按词尾猜。',
 ('The map shows the extent of the Abbasid Caliphate.','地图显示阿拔斯哈里发国的疆域范围。'),('The course compares several historical caliphates.','这门课比较了历史上的几个哈里发国。'),sources=['https://www.etymonline.com/word/caliphate','https://en.wiktionary.org/wiki/caliphate#English'])
W('spanking','/ˈspæŋkɪŋ/','拍打、打屁股；固定表达中加强语气：崭新的、很快的等',
 'a spanking 可以说一次拍打臀部的惩罚；brand spanking new 却只是在用力强调全新。这两组常见用法要分开记。',
 '拍打名词对应 spank + -ing，spank 更远可能有拟声背景。另一个很大、出色、迅速的形容词 spanking 较早已有，来源不全确定；不能把所有加强语气义都编成由打屁股逐步演变。',
 [['spank + -ing','拍打的动作名词、分词'],['另见较早 spanking 的加强形容词材料','很出色、很快；固定加强表达，来源未全确定']],
 'a spanking 打屁股的惩罚；brand spanking new 崭新的；at a spanking pace 以很快的速度，稍带旧式或生动表达色彩。',
 'a brand spanking new bicycle；spanking along。','brand spanking new 作为整体表示全新，spanking 不必按拍打翻译。读到 a spanking 则通常是动作名词，冠词与后面的搭配帮助分义。',
 ('She arrived on a brand spanking new bicycle.','她骑着一辆崭新的自行车来了。'),('The novel describes a child’s fear of getting a spanking.','小说描写一个孩子害怕挨打屁股的心情。'),sources=['https://www.etymonline.com/word/spanking','https://en.wiktionary.org/wiki/spanking#English'])
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_uj',ROOTS,WORDS)
 extend_lessons()
