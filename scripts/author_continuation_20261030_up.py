"""High-frequency missing bases, keeping borrowed history distinct from modern forms."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'B2669':dict(words=['car','carry','carrier'],label='车运的旧词族到今天的 carry、carrier',note='carry 经法语运输动词接 carrus 等车的旧词族；现代 carry 远不止用车搬运。carry 的 y 变 i 再加 -er 得 carrier。'),
 'B4162':dict(words=['enter','entry'],label='enter 与 entry：进入的动作和入口、记录',note='enter 与 entry 共同接法语、拉丁进入词族；现代读音、拼写不同，不能把 entry 画成 enter 随手加 y。'),
 'A1760':dict(words=['target','targeted','afraid'],label='targeted 的现代 -ed 与 afraid 的旧分词材料',note='targeted 是 target + -ed，末尾 /ɪd/；afraid 承接已不常用的旧 afray 动词分词，现代整体作害怕的形容词。'),
 'A1776':dict(words=['magazine','museum','valley'],label='借词单数认清后，再学英语复数',note='magazine、museum、valley 都已是英语可数单数，英语复数分别 magazines、museums、valleys。magazine 更早的阿拉伯来源本是复数，不能把来源语言的数直接当今天英语语法；valley 的复数保留元音字母 e 后的 y。'),
 'A1958':dict(words=['feast','festival','festive'],label='feast、festival、festive：庆典和宴饮的同源材料',note='三者接拉丁节庆词族而借入路径不同；feast 可说盛宴或节日，festival 是节庆活动，festive 是有节日气氛的。'),
 'B3939':dict(words=['prince','princess','principal','principality'],label='princeps 的领头者材料与 prince、principal',note='prince 和 principal 等共同接拉丁 princeps、princip- 的首位、领头词族；princess 为相应女性称号。具体称号不能在所有制度里只译王子、公主。'),
 'B3887':dict(words=['terror','terrible','terrify'],label='terrible、terrify：吓人词族与语义弱化',note='terrible 接拉丁 terribilis 吓人的，现代常弱化成很糟；terrify 接 terrificare，使人强烈害怕；不能把所有 terr- 字母串都拿来指土地。'),
 'C0743':dict(words=['minor','minimum','minimal'],label='minimum：从较小到最小的程度',note='minimum 接拉丁 minimus 最小的中性形式，与 minor 较小同族；现代是最小量名词，也限定最低要求。'),
}
W('carry','英 /ˈkæri/；美 /ˈkæri/','搬、携带；承载、传播；继续进行、执行；备有、销售等',
 '把东西托在身上或工具上带走，是 carry；一条电线、一个声音也能把东西或信息从一处带到另一处。',
 '经盎格鲁法语 carier、古北法语 carrier 等运输动词，接拉丁、古高卢车的词族。原有用车运的背景，进入英语后范围扩大到承载、携带、输送等。',
 [['车的拉丁、高卢材料 → 法语运输动词','用车辆运送、带走'],['英语 carry','携带、承载、传播；再有多种固定搭配']],
 'carry a bag 提包；carry a message 传递信息；carry on 继续；carry out a plan 执行计划；carry a product 店铺备售某产品。',
 'carry it upstairs；carry responsibility；carry on working。','carry 强调携带、承载的过程；bring、take 还涉及朝某参照点来或去。carry out 是执行，carry on 是继续，搭配中的小词改变动作方向。',
 ('Could you help me carry this box upstairs?','你能帮我把这个箱子搬上楼吗？'),('Sound carries well across the water.','声音在水面上传得很远。'),('We need more time to carry out the plan.','我们需要更多时间执行计划。'),sources=['https://www.etymonline.com/word/carry','https://en.wiktionary.org/wiki/carry#English'])
W('carrier','英 /ˈkæriə/；美 /ˈkæriər/','承运人、运输公司；运载工具；携带者；通信运营商等',
 '共同点是把东西承载、送到另一处：人送邮件，船载飞机，通信公司传送信号。carrier 不只是一种职业。',
 'carry 的 y 变 i 加 -er，较早泛指运输的人或物；后来按承载的对象，形成航运、通信、生物等专门用法。',
 [['carry + -er → carrier','携带、运送的人或东西'],['按运载对象与领域专门化','承运公司、运输装置、通信运营商、携带者等']],
 'a mail carrier 邮递员；a cargo carrier 货运公司或载货工具；an aircraft carrier 航空母舰；a mobile carrier 移动通信运营商；a pet carrier 宠物提箱。',
 'choose a carrier；a carrier of information。','carrier 的 -er 既可落到人，也可落到物或公司。判断时先看它携带、运送的是什么；手机语境 carrier 通常指网络运营商。',
 ('The carrier will deliver the package tomorrow.','承运公司明天会递送包裹。'),('She placed the kitten in a pet carrier.','她把小猫放进宠物提箱。'),sources=['https://www.etymonline.com/word/carrier','https://en.wiktionary.org/wiki/carrier#English'])
W('enter','英 /ˈentə/；美 /ˈentər/','进入；输入、录入；报名参加；开始进入某阶段',
 '跨过门槛进屋，或把名字填进系统，都有从外面进入一个范围的画面。',
 '经古法语 entrer，接拉丁 intrare 进入，来自 intra 在里面的词族。后来进入群体、记录、比赛、阶段等抽象范围的用法逐步扩展。',
 [['拉丁 intra → intrare → 法语 entrer','里面 → 走进去'],['英语 enter','进入场所；把信息录入；参加活动、进入阶段']],
 'enter the room 进入房间；enter a password 输入密码；enter a competition 报名比赛；enter a new phase 进入新阶段；enter into an agreement 达成协议。',
 'enter your name；enter the building。','普通进房间直接说 enter the room，不必加 into；enter into 常用于谈话、安排、协议等固定关系，不能所有场合机械省留介词。',
 ('Please enter your name in the box.','请在方框里输入你的名字。'),('She entered the room without making a sound.','她悄无声息地走进房间。'),sources=['https://www.etymonline.com/word/enter','https://en.wiktionary.org/wiki/enter#English'])
W('target','英 /ˈtɑːɡɪt/；美 /ˈtɑːrɡɪt/','目标、指标；靶子；针对、把某人某物定为目标',
 '把视线钉在一个想达到、想影响的点上，就是 target。它可以是销售数字，也可以是一群需要服务的人。',
 '较早 target 指小盾，接 targe 及法语 targete 等指小材料，来自日耳曼语盾框、边缘词族。后来用作瞄准物，可能与圆形、同心圈外观有关，再泛化为目标。',
 [['targe、法语 targete 等','较小、常为圆形的盾'],['瞄准物 → 现代 target','靶子；目标、指标；把某物当目标']],
 'meet a target 达到指标；set a target 设目标；target audience 目标受众；target a problem 针对问题；a target of criticism 批评对象。',
 'reach the target；target resources at something。','goal 常概括想实现的结果，target 常把可瞄准、可衡量或要影响的对象标出来；二者在目标义有重叠。',
 ('The team met its target ahead of schedule.','团队提前完成了目标。'),('The campaign targets young adults.','那项宣传活动面向年轻成年人。'),sources=['https://www.etymonline.com/word/target','https://en.wiktionary.org/wiki/target#English'])
W('targeted','英 /ˈtɑːɡɪtɪd/；美 /ˈtɑːrɡɪtɪd/','有针对性的；被选为目标的；target 的过去式、过去分词',
 '帮助不是平均撒出去，而是对准某一类具体需要；这种定向安排叫 targeted。也可说某人被选成攻击、批评对象。',
 'target + -ed，词干末尾 /t/ 后的 -ed 读 /ɪd/。旧 target 另有盾的历史，但现代常用 targeted 接选作目标、针对的动词分支。',
 [['target 的现代目标、针对分支','选定希望影响、达到的对象'],['target + -ed → targeted','有针对性的；被定为目标的']],
 'targeted support 有针对性的支持；targeted advertising 定向广告；targeted at students 面向学生；was targeted by criticism 被批评针对。',
 'carefully targeted；a targeted approach。','targeted 描写方向明确，不保证效果已经达到；effective 才直接评价有效。is targeted at 说面向谁，was targeted by 说被谁针对。',
 ('The programme offers targeted support to new students.','那项计划为新生提供有针对性的支持。'),('The messages were targeted at people learning to read.','那些信息面向正在学习阅读的人。'),sources=['https://www.etymonline.com/word/target','https://en.wiktionary.org/wiki/targeted#English'])
W('magazine','/ˌmæɡəˈziːn/','杂志；弹药库、弹匣等',
 '先想一座储藏东西的库：里面可以存弹药；后来一本刊物汇集多种文章，也像装满信息的仓库。',
 '经法语 magasin、意大利语 magazzino，接阿拉伯 makhazin，原是 makhzan 仓库的复数。英语把借入词作可数单数使用；出版物义从资料、信息的汇集发展。',
 [['阿拉伯 makhzan／makhazin → 欧洲语言相关形式','仓库、储藏处；来源形式为复数'],['英语 magazine','库藏、弹匣；汇集多种内容的杂志']],
 'a monthly magazine 月刊；a travel magazine 旅游杂志；an ammunition magazine 弹药库；a rifle magazine 步枪弹匣。不同义共用储放、汇集的线索。',
 'read a magazine；a magazine article；two magazines。','今天英语是 a magazine、two magazines，不能把阿拉伯来源是复数这一点直接套到英语。journal 常偏学术或专门记录，magazine 常是面向读者的综合、专题刊物。',
 ('She bought a magazine to read on the train.','她买了一本杂志，准备在火车上看。'),('The article was published in a science magazine.','那篇文章发表在一本科学杂志上。'),sources=['https://www.etymonline.com/word/magazine','https://en.wiktionary.org/wiki/magazine#English'])
W('feast','/fiːst/','盛宴、大餐；节日庆典；尽情享用',
 '桌上摆满好吃的，大家一起庆祝，是 a feast。也能把饱享搬到眼睛、耳朵上：a feast for the eyes 视觉盛宴。',
 '经古法语 feste 庆典、宗教节日等，接拉丁 festa 节庆、宴饮，属于 festus 欢乐、节日的词族。英语从庆祝活动发展出丰盛餐食与享受之义。',
 [['拉丁 festa、festus → 法语 feste','节庆、宴饮、欢乐'],['英语 feast','庆典、盛宴；尽情欣赏或享用']],
 'a wedding feast 婚宴；prepare a feast 准备盛宴；feast on something 大快朵颐、尽情享用；a feast for the eyes 视觉盛宴。',
 'a generous feast；feast one’s eyes on something。','meal 只是一次餐食，feast 常突出丰盛、庆祝或极大的享受。fast 作禁食时与 feast 的历史节日场景可形成对比，但拼写相近不能互换。',
 ('They prepared a feast for the whole family.','他们为全家准备了一桌盛宴。'),('The colourful garden was a feast for the eyes.','色彩丰富的花园让人饱享眼福。'),sources=['https://www.etymonline.com/word/feast','https://en.wiktionary.org/wiki/feast#English'])
W('festival','/ˈfestɪvəl/','节庆、节日；以某种活动为主题的盛会',
 '把吃喝、音乐、仪式或展演集中在一段时间，许多人一起参加，这种安排就是 festival 的常见样子。',
 '经法语 festival 或中世纪拉丁 festivalis 节日的，接拉丁 festum 节庆。英语名词由 festival day 等表达简化而来，后来扩展到电影节、音乐节等。',
 [['拉丁 festum → festivalis／法语 festival','节庆 → 节日的'],['festival day 等 → 名词 festival','节庆日；主题活动盛会']],
 'a music festival 音乐节；a film festival 电影节；a religious festival 宗教节日；a festival of local food 地方美食节。',
 'hold a festival；attend a festival。','feast 常把宴饮、享受突出出来；festival 更常说一整套庆典或主题活动，不要求每次都有盛大餐宴。',
 ('The town holds a music festival every summer.','小镇每年夏天都会举办音乐节。'),('We watched several films at the festival.','我们在电影节上看了几部电影。'),sources=['https://www.etymonline.com/word/festival','https://en.wiktionary.org/wiki/festival#English'])
W('prince','/prɪns/','王子、亲王等；君主、统治者〔依历史、制度而定〕',
 '今天常想到国王的儿子，但更老的核心是站在首位、领头的人。历史书里的 prince 也可能自己就是统治者。',
 '经古法语 prince，接拉丁 princeps、词干 princip- 首位者、领袖，由 primus 第一与 capere 取的材料构成。英语先有领袖、统治者等义，王室之子的专门义后来发展。',
 [['拉丁 primus 与 capere → princeps','取得首位、居首者 → 领袖'],['法语 prince → 英语 prince','统治者；后来各类王室、贵族称号']],
 'a young prince 年轻王子；a ruling prince 在位亲王、统治者；a prince of a man 比喻非常好的人；the prince in the story 故事中的王子。',
 'a royal prince；a prince’s title。','prince 不保证只是国王的儿子；具体中文可为王子、亲王、君主等，要看身份和历史背景。principal 也接首位、领头这一同源材料。',
 ('The story follows a prince who leaves the palace.','故事讲一位王子离开宫殿后的经历。'),('The prince ruled a small state.','那位亲王统治着一个小国。'),sources=['https://www.etymonline.com/word/prince','https://en.wiktionary.org/wiki/prince#English'])
W('princess','/prɪnˈses/，也有 /ˈprɪnses/ 等读法','公主、王妃等女性王室或贵族称号',
 '与 prince 对应的女性称号，可以由出生身份、婚姻或统治身份而来。具体故事里是谁的女儿、配偶，要靠上下文看。',
 '现代对应 prince + 女性称号后缀 -ess；英语早期已有形成，也有后来的法语 princesse 相关借入。更早接拉丁 princeps、princip- 领头词族。',
 [['prince 与相关女性称号材料、法语 princesse','女性王室、贵族或统治者称号'],['现代 princess','公主、王妃等；具体制度决定身份']],
 'a fairy-tale princess 童话公主；a royal princess 王室公主；a princess’s crown 公主的冠；treat someone like a princess 把某人宠爱得像公主。',
 'the princess in a play；a princess costume。','princess 不只按女儿关系解释，也可指某些 prince 的妻子或女性统治者。翻译具体人物时先确认身份。',
 ('She played a princess in the school play.','她在学校话剧里扮演公主。'),('The novel tells the story of a princess who becomes a ruler.','小说讲一位公主后来成为统治者的故事。'),sources=['https://www.etymonline.com/word/princess','https://en.wiktionary.org/wiki/princess#English'])
W('valley','/ˈvæli/','山谷、谷地',
 '两侧地势高，中间是一片低下去的地，常有河流穿过。valley 把视线放在高地之间的低处。',
 '经盎格鲁法语 valey、古法语 valee 等，上接拉丁 vallis 山谷，更远来源不明。现代作为完整可数名词，复数 valleys 保留 y。',
 [['拉丁 vallis → 法语 valee、valey 等','山谷、两侧高地间的低地'],['英语 valley','谷地；可数名词，复数 valleys']],
 'a river valley 河谷；a deep valley 深谷；the valley floor 谷底；a village in the valley 山谷中的村庄。',
 'across the valley；hills on either side of the valley。','valley 通常比一条狭窄冲沟更能让人想到两侧高地间的谷地；具体大小并无固定词长规则。复数 valleys 是元音 e 后保留 y 加 s。',
 ('A narrow river runs through the valley.','一条窄河穿过山谷。'),('The village lies at the bottom of a green valley.','村庄坐落在一片葱绿山谷的谷底。'),sources=['https://www.etymonline.com/word/valley','https://en.wiktionary.org/wiki/valley#English'])
W('museum','/mjuˈziːəm/','博物馆',
 '把值得研究、保存的东西收集起来，再展示给人看。museum 的老背景先是缪斯相关的学术、艺术场所，后来集中到收藏和展示。',
 '经拉丁 museum，接希腊 mouseion，原指缪斯女神的场所，也指学习、图书、艺术场所，接 Mousa 缪斯。英语后来形成现代收藏、展陈机构义。',
 [['希腊 Mousa → mouseion','缪斯 → 与艺术、学习相关的场所'],['拉丁 museum → 英语 museum','学术收藏场所 → 博物馆']],
 'a history museum 历史博物馆；an art museum 美术馆；museum collections 馆藏；a museum exhibit 博物馆展品或展览。',
 'visit a museum；a museum of natural history；two museums。','museum 不限于艺术，也可收藏历史、科技、自然标本等。现代复数通常 museums，借来的 -um 不要求一律改成拉丁式复数。',
 ('We spent the afternoon at the history museum.','我们在历史博物馆度过了下午。'),('The museum displays old tools and household objects.','博物馆展出旧工具和生活用品。'),sources=['https://www.etymonline.com/word/museum','https://en.wiktionary.org/wiki/museum#English'])
W('terrible','/ˈterəbəl/','很糟的、极坏的；可怕的、严重的',
 '老核心是让人害怕；今天说 a terrible meal，往往只是在说难吃得很。语气强，但不一定真有恐惧。',
 '经古法语 terrible 或直接借自拉丁 terribilis 吓人的，上接 terrere 使恐惧。后来从令人惊惧弱化到严重、很糟、极差。',
 [['拉丁 terrere → terribilis → 法语／英语 terrible','使害怕 → 可怕、难忍的'],['现代常见语义弱化','很糟、极差；也仍可说可怕、严重']],
 'terrible weather 糟糕天气；a terrible accident 严重事故；terrible at maths 数学很差；feel terrible 感觉难受，也可说心里愧疚。',
 'a terrible mistake；a terrible headache。','terrible 常负面，terrific 今天常可表示很棒；两者虽同属恐惧旧词族，现代评价方向已经分开。',
 ('The weather was terrible all weekend.','整个周末天气都很糟。'),('I felt terrible about forgetting her birthday.','忘了她的生日，我心里很过意不去。'),sources=['https://www.etymonline.com/word/terrible','https://en.wiktionary.org/wiki/terrible#English'])
W('terrify','/ˈterɪfaɪ/','使非常害怕、吓坏',
 '不是微微担心，而是恐惧一下涌上来。The noise terrified me 就是那声音把我吓坏了。',
 '接拉丁 terrificare 使害怕，来自 terrificus 引起恐惧的；terr- 属惊吓词族，-fic- 与 facere 做、使的材料相连，现代形式为 terrify。',
 [['拉丁 terrere、terrificus 等惊吓词族','使恐惧；引发恐惧的'],['拉丁 terrificare → 英语 terrify','使人强烈害怕']],
 'terrify someone 把某人吓坏；be terrified of something 非常怕某物；a terrifying experience 吓人的经历。terrify 的对象是感到害怕的人或动物。',
 'terrify the audience；terrify a child。','terrify 是使害怕，terrified 是感到害怕的，terrifying 是让人害怕的。主语和对象的角色分清，三个词就容易连起来。',
 ('The sudden noise terrified the dog.','突然的声响把狗吓坏了。'),('The thought of speaking in public terrifies him.','一想到当众讲话，他就非常害怕。'),sources=['https://www.etymonline.com/word/terrify','https://en.wiktionary.org/wiki/terrify#English'])
W('afraid','/əˈfreɪd/','害怕的；担心的；I’m afraid：恐怕、很遗憾地说',
 '危险还没发生，心里已经缩了一下，是 afraid；礼貌地传达不太好的消息，也常用 I’m afraid 来放软语气。',
 '接中古英语 afray 使惊恐的旧过去分词，源于盎格鲁法语 afrayer 等惊扰材料；更早接重构的通俗拉丁 *exfridare，混合了拉丁和日耳曼语出离平安的词材。现代整体作形容词。',
 [['法语惊扰、恐惧材料 → 中古英语 afray 的分词','使惊恐 → 感到害怕的'],['现代 afraid','害怕、担心；礼貌表示恐怕、遗憾']],
 'afraid of dogs 怕狗；afraid to ask 不敢问；afraid that something will happen 担心某事发生；I’m afraid not 恐怕不行、恐怕不是。',
 'Don’t be afraid；I’m afraid so。','afraid 通常在 be、feel 等后面，不常直接说 an afraid child；a frightened child 更自然。I’m afraid we’re closed 多是委婉说已关门。',
 ('She is afraid of the dark.','她怕黑。'),('I’m afraid we have no tickets left.','很遗憾，票已经卖完了。'),sources=['https://www.etymonline.com/word/afraid','https://en.wiktionary.org/wiki/afraid#English'])
W('minimum','/ˈmɪnɪməm/','最低量、最小值；最低的、最少的',
 '画一条底线：至少要有这么多，或尽量压到这么少。minimum 关注这个最小量，具体是要求下限还是最少程度，要看搭配。',
 '来自拉丁 minimum，minimus 最小的中性形式；minimus 是与 minor 较小相关的最高级材料。英语先作最小量名词，后也作限定最低的形容词。',
 [['拉丁 minor、minimus → minimum','较小 → 最小的事物或量'],['英语 minimum','最小量、最低值；最低的']],
 'a minimum of five 至少五个；the minimum age 最低年龄；keep noise to a minimum 把噪声压到最低；a bare minimum 最低限度。',
 'minimum requirements；at a minimum；the minimum amount。','minimum 是下限或最小量，maximum 是上限或最大量。a minimum of ten 是至少十个，不能看见最小就读成最多十个。',
 ('The course requires a minimum of ten students.','那门课至少需要十名学生。'),('Please keep noise to a minimum.','请尽量保持安静。'),sources=['https://www.etymonline.com/word/minimum','https://en.wiktionary.org/wiki/minimum#English'])
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_up',ROOTS,WORDS)
 extend_lessons()
