"""Service, connections, arrival, proportion and first steps."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'C0238':dict(words=['incline','client'],label='client：受庇护者到客户；更早词源有分歧',note='client 接拉丁 cliens 受庇护者；更早联系倾斜、依靠只是一种分析，另有 cluens、clueo 的路线。这里把依靠画面作为一种传统解释，现代客户、客户端义按场景说明。'),
 'C0168':dict(words=['cable'],label='cable：抓住、套住的绳到传输线路',note='cable 经法语接拉丁 capulum 绳套，连接 capere 抓住；现代线缆义随材料和通信用途扩展。'),
 'B3100':dict(words=['river','arrive','arrival'],label='ripa 岸的历史分支：river 与 arrive',note='river 经法语接拉丁河岸相关材料，arrive 经法语接到岸、上岸；两词共享更早的岸词，不是把英语 river 在今天任意拆改。arrival 历史另经法语名词借入。'),
 'B2597':dict(words=['rational','ratio'],label='ratio：计算、推理材料中的数量比',note='ratio 直接接拉丁 ratio 计算、推理，与 rational 同族；现代英语常用比例义，不将全部拉丁多义照搬成英语基本释义。'),
 'B3838':dict(words=['frequent','frequency'],label='frequent 与 frequency：出现得密与出现的频率',note='frequency 接拉丁 frequentia 众多、聚集等名词，现代可对照 frequent 与 -cy；物理频率是反复次数的专门化。'),
 'A1958':dict(words=['initiate','initiative'],label='initiative：把开头做起来的主动性',note='initiative 经法语借入，连接拉丁 initiare 开始、initium 开端及相应 -ivus 材料；主动性与发起的一项行动分别举例。'),
 'B3939':dict(words=['prince','principal','principle'],label='princeps 居首的分支：principle 基础原则',note='principle 经法语接拉丁 principium 开始、基础，与 principal、prince 共享 princeps 等更早材料，现代词义不同。'),
}
W('client','/ˈklaɪənt/','客户、委托人；客户端〔计算机〕',
 '有件事需要专业帮忙，你把它交给设计师、会计师等处理，在这个服务关系里你是 client。计算机里的 client 则是向服务端提出请求的一方。',
 '经法语接拉丁 cliens、client- 跟随者、受庇护者，后来指委托事务、接受专业服务的人。更早有接 clinare 倾斜、依靠的分析，也有接 cluens、clueo 的分析，不能把依靠来源当作定论。',
 [['拉丁 cliens → 法语 → 英语 client','依靠保护者的一方 → 委托专业事务的人'],['现代 client 的业务、计算机专门义','客户；向服务端请求服务的程序或设备']],
 'a client meeting 客户会议；a client of the firm 这家公司的客户；an email client 邮件客户端；client software 客户端软件。',
 'meet a client；a client request。','customer 常是购买商品或服务的人，client 更容易让人想到持续的专业服务关系，但实际行业用词有重叠。计算机 client 也可以是软件，不一定是一个人。',
 ('The designer met the client to discuss the first sketches.','设计师与客户会面，讨论第一批草图。'),('The email client downloaded the new messages.','邮件客户端下载了新邮件。'),sources=['https://www.etymonline.com/word/client','https://en.wiktionary.org/wiki/client#English','https://en.wiktionary.org/wiki/cliens#Latin'])
W('cable','/ˈkeɪbəl/','粗缆绳、钢索；电缆、线缆；有线电视；用线缆连接',
 '一条结实的长线，原先能拉住船，后来能带着电力、信号从一头到另一头。形状相近，用途随着材料和技术变化。',
 '经北部古法语 cable 接拉丁 capulum 绳套、缰索，连接 capere 抓住、套住。英语由粗绳、缆索扩展到金属钢索及电力、通信线缆。',
 [['拉丁 capulum → 法语 cable','抓牢东西的绳套、缆绳'],['英语 cable','粗绳、钢索 → 电力与通信线路；有线电视等']],
 'a power cable 电源线、电力电缆；a charging cable 充电线；an undersea cable 海底电缆；cable television 有线电视；a suspension cable 悬索。',
 'connect the cable；a damaged cable。','cable 旧绳索义仍常见，不能看见就只译电线。a cable holding a bridge 是承力索；a cable connected to a screen 通常是传输线。',
 ('I need a longer cable to connect the screen.','我需要更长的线来连接屏幕。'),('Steel cables support the bridge.','钢索支撑着桥。'),sources=['https://www.etymonline.com/word/cable','https://en.wiktionary.org/wiki/cable#English'])
W('arrive','/əˈraɪv/','到达、抵达；到来；达到〔某种结论、状态〕',
 '坐船终于靠岸，这是它很直观的老画面。后来不坐船也能 arrive：到车站、到家，甚至经过思考到达一个结论。',
 '经法语 ariver 到岸，接较早拉丁到岸相关动词，常重建为 *arripare，来自 ad 向与 ripa 岸。英语从海上行程扩到一般行程及抽象状态。',
 [['拉丁 ad ripam；较早到岸动词 → 法语 ariver','朝向岸边 → 靠岸、上岸'],['英语 arrive','抵达目的地；事物到来；得到结论']],
 'arrive at a station 到车站；arrive in a city 到某城；arrive home 到家；arrive at a decision 作出决定；The day has arrived 那一天终于到了。',
 'arrive on time；arrive safely。','arrive 通常不直接接地点作宾语：arrive at the hotel、arrive in London；home、here、there 作地点副词时不加 at 或 in：arrive home。',
 ('We arrived at the station just before noon.','我们在快中午时到了车站。'),('The team arrived at a decision after a long discussion.','团队长时间讨论后作出了决定。'),sources=['https://www.etymonline.com/word/arrive','https://en.wiktionary.org/wiki/arrive#English'])
W('arrival','/əˈraɪvəl/','到达；到来；新到的人、物',
 'arrive 是到的动作，arrival 把这一次抵达拿出来说；也能把刚到的那个成员叫 a new arrival。',
 '经法语 arrivaille 等到岸、到达名词借入，与 arriver 同族。现代可对应 arrive 去 e 加名词 -al，但英语形式不只是今天新拼的规则词。',
 [['法语 arriver → arrivaille 等','到达 → 到达这件事'],['英语 arrival','抵达；后来也指到达的人、物']],
 'on arrival 一到达；the arrival of spring 春天到来；a new arrival 新来者、新生儿等；arrivals hall 机场到达大厅。',
 'arrival time；an early arrival。','arrival 可说过程，也可数新到的人或一班到达航班。on arrival at the hotel 一到酒店；departure 则是离开、出发。',
 ('Please call us on arrival at the hotel.','到酒店后请给我们打电话。'),('The new arrival was welcomed by the whole class.','新来的同学受到了全班欢迎。'),sources=['https://www.etymonline.com/word/arrive','https://en.wiktionary.org/wiki/arrival#English'])
W('ratio','英 /ˈreɪʃiəʊ/；美 /ˈreɪʃioʊ/','比、比率、比例关系',
 '把两种数量并排比较：每两杯米配三杯水，米与水的 ratio 是 2 比 3。重点是 A 相对 B 有多少。',
 '直接借拉丁 ratio 计算、账目、推理，来自 reri 计算、认为的词干 rat-。与 rational、reason、ration 同族但借入路径和现代分工不同；英语常见数学比例义。',
 [['拉丁 reri → ratio','计算、推想 → 计算、数量关系、道理等'],['英语 ratio 的常用数学义','两个数量之间的比']],
 'the ratio of A to B：A 与 B 的比；a ratio of two to three 二比三；aspect ratio 画面宽高比；a high ratio 较高的比值。',
 'a one-to-one ratio；the ratio between two quantities。','A to B 的先后决定比值：2 比 3 与 3 比 2 不同。ratio 比较两个量，percentage 则常把相对某个整体的量折成每百份表达。',
 ('Mix flour and water in a ratio of two to one.','把面粉和水按二比一混合。'),('The screen has a different aspect ratio from the old one.','这块屏幕的宽高比与旧屏幕不同。'),sources=['https://www.etymonline.com/word/ratio','https://en.wiktionary.org/wiki/ratio#English'])
W('frequency','/ˈfriːkwənsi/','频率、发生次数；频数；频率值〔物理、通信〕',
 '一分钟响几次、一周来几趟，都可以看 frequency。把反复发生的事情放到一段时间里，问它出现得多密。',
 '接拉丁 frequentia 聚集、众多，来自 frequens 众多、频繁。现代可对照 frequent 与名词 -cy；早期聚集义到经常发生，再有物理中单位时间反复次数的专门义。',
 [['拉丁 frequens → frequentia','众多、聚集、频繁 → 相应状态'],['英语 frequency','发生得多常；物理频率等']],
 'the frequency of visits 探访频率；a high frequency 高频率；word frequency 词频；radio frequency 无线电频率；a frequency of 50 hertz 五十赫兹的频率。',
 'increase the frequency；frequency of occurrence。','frequency 日常回答多常、多少次；duration 回答每次持续多久。词频可以是某语料中的出现次数或相对频度，要看统计口径。',
 ('The buses run with greater frequency during rush hour.','高峰期公交班次更密。'),('The table shows the frequency of each word in the text.','表格显示了每个词在文本中的出现频数。'),sources=['https://www.etymonline.com/word/frequency','https://en.wiktionary.org/wiki/frequency#English'])
W('initiative','/ɪˈnɪʃətɪv/','主动性；率先采取的行动；倡议、措施',
 '大家都等别人开头，你先把第一步做起来，这是 initiative。把一个新目标启动起来的一整项行动，也可以叫 an initiative。',
 '借法语 initiative，连接拉丁 initiare 开始、initium 开端及相应形容词材料。更早 initium 接进入、开始的 inire；主动发起的能力再扩成具体倡议。',
 [['拉丁 initium → initiare → 法语 initiative','开端 → 发起；有发起作用的性质'],['英语 initiative','主动开始的能力；一项发起的行动']],
 'take the initiative 主动迈出第一步；show initiative 表现主动性；on one’s own initiative 自发地；launch an initiative 发起一项行动。',
 'a local education initiative；use your initiative。','initiative 说主动性时通常不可数，a new initiative 则是可数的一项新行动、倡议。initiative 不只是心里有想法，还含着着手推动的意思。',
 ('She took the initiative and arranged the first meeting.','她主动安排了第一次会议。'),('The town launched an initiative to repair old bicycles.','小镇发起了一项维修旧自行车的活动。'),sources=['https://www.etymonline.com/word/initiative','https://en.wiktionary.org/wiki/initiative#English'])
W('principle','/ˈprɪnsəpəl/','原则、准则；原理；基本规律',
 '盖房先有地基，做事、解释问题也会有几条最底下支撑它的规则。principle 是这种基础性的准则或原理。',
 '经法语接拉丁 principium 开始、基础，来自 princeps 居首的、领头者；更早含 primus 第一与 capere 取得的材料。英语拼写的 l 受到相近词形等影响，不来自现代把 principal 随意改字母。',
 [['拉丁 princeps → principium','居首、领先 → 开始、基础'],['法语 → 英语 principle','基础规则；行为准则、事物原理']],
 'a basic principle 基本原则；in principle 原则上、从基本道理上；on principle 出于原则；the principle behind a device 装置背后的原理。',
 'a matter of principle；put a principle into practice。','principle 与 principal 常同音。principle 是原则、原理；principal 可说主要的、校长、本金。in principle 同意，仍可能有细节没定。',
 ('She refused the gift on principle.','她出于原则拒收了礼物。'),('The teacher explained the principle behind the experiment.','老师解释了实验背后的原理。'),sources=['https://www.etymonline.com/word/principle','https://en.wiktionary.org/wiki/principle#English'])
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_uv',ROOTS,WORDS)
 extend_lessons()
