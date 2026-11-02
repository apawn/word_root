"""Aware and band: attention, strips, groups and modern capacity."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
AW=[['古英语 gewær → 中古英语 aware','留神、警觉；前部旧 ge- 后来弱化'],['现代 aware','意识到、知道；注意到情况']]
W('aware','英 /əˈweə/；美 /əˈwer/','知道的；意识到的；留神的',
 '某件事已进入你的注意范围，你知道它在那里、可能影响什么。',
 '继承古英语 gewær，wær 表警觉、谨慎，前部旧 ge- 经弱化形成今日 a-。这个 a- 不是希腊否定前缀。',AW,
 'be aware of a problem 知道某问题，be aware that 意识到某事实，make someone aware of 提醒某人知晓。',
 'aware of；aware that；make someone aware；as far as I am aware。',
 'aware 通常放 be 等之后说状态；an aware person 单独不如 a person aware of the risks 明确。aware 知道不等于已经采取行动。',
 ('Are you aware of the change in the schedule?','你知道日程改了吗？'),('She became aware that someone was standing behind her.','她意识到有人站在身后。'),sources=['https://www.etymonline.com/word/aware','https://en.wiktionary.org/wiki/aware#English'])
W('awareness','英 /əˈweənəs/；美 /əˈwernəs/','知晓；意识；认识程度',
 '不是一条知识本身，而是人有没有注意到、认识到这件事。',
 'aware + -ness，性质、状态名词。通常不可数，前面可以加 environmental、public 等说明认识什么。',AW+[['aware + -ness → awareness','意识到的状态、程度']],
 'raise awareness of 提高对某事的认识，public awareness 公众认知，environmental awareness 环保意识。',
 'raise awareness；public awareness；awareness of；self awareness。',
 'awareness 认识状态，knowledge 常更具体说掌握的知识；知道问题存在，不保证知道全部解决方法。',
 ('The campaign aims to raise awareness of food waste.','活动旨在提高人们对食物浪费的认识。'),('Public awareness of the issue has grown.','公众对这一问题的认识加深了。'))
W('unaware','英 /ˌʌnəˈweə/；美 /ˌʌnəˈwer/','不知道的；未意识到的',
 '事情已经发生或正在身边，你却还没注意到。',
 'un- 不 + aware，否定知晓状态。保留 aware 后接 of、that 的结构。',AW+[['un- + aware → unaware','没有意识到、不知情']],
 'unaware of the danger 未觉察危险，unaware that 不知道某事实，remain unaware 一直不知。',
 'unaware of；unaware that；remain unaware。',
 'unaware 没注意或不知情，不自动表示 careless 粗心；可能根本没有获得消息。',
 ('He was unaware of the change until Monday.','直到周一他才知道有了变动。'),('She walked past, unaware that her friend was waving.','她走了过去，没注意到朋友在招手。'))
W('beware','英 /bɪˈweə/；美 /bɪˈwer/','小心；提防',
 '从知道这里有东西，再向前一步提醒自己：留神，它可能带来麻烦。',
 '主要由中古英语 be ware 小心、警觉的短语连写收缩，ware 接古英语 wær。不是把现代 be aware 随便删去一个 a 就造出新词。',
 [['古英语 wær → 中古英语 ware〔警觉〕；be ware 短语','保持警惕'],['be ware → beware','小心、提防的动词']],
 'Beware of the dog! 小心犬只，beware of hidden charges 提防隐藏费用；也可直接接宾语，如 beware the consequences。',
 'beware of；Beware!；beware the consequences。',
 'be aware of 是知道，beware of 是留神提防。Beware 常用原形的警告、提醒结构，不按普通每个时态都随意变化。',
 ('Beware of ice on the steps.','小心台阶上的冰。'),('Travellers should beware of hidden charges.','旅客应留意隐藏费用。'),sources=['https://www.etymonline.com/word/beware','https://en.wiktionary.org/wiki/beware#English'])
R('B3791','觉察、知晓与警惕','AWARE：知道；BEWARE：留神提防','aware → awareness、unaware，再并列 be ware 短语形成的 beware。',
 'aware 的 a- 是旧前部弱化，beware 来自小心的短语收缩，两个词与警觉旧形有共同关系，不套成现代删字母规则。',
 'aware + -ness；un- + aware；be ware → beware。',
 [['知晓、状态与否定','aware · awareness · unaware'],['警惕提醒','beware']],
 'aware of 知道，beware of 提防；awareness 不是全部知识；unaware 不自动粗心。',
 'Be aware of the rules, and beware of misleading shortcuts.\n\n了解规则，并提防误导人的捷径。',
 'aware awareness unaware beware')
BA=[['古英语 bend 等、古诺尔斯语 band、法语 bande 的相关形式','束带、条带；多条传入形式汇合'],['法语 bande〔人群〕→ 英语 band；条带另发展频带义','群体 → 乐队；条状范围 → 频带']]
def BH(f,m):return BA+[[f,m]]
W('band','/bænd/','带、环；条纹；频带；乐队、群体；结成一伙',
 '可以是围着手腕的一条带，也可以是一群凑在一起的人；技术里某一段连续频率，又像一条带。',
 '条带义汇合本族、诺尔斯语、法语相关形式；群体义经法语进入，较深可能仍关乎绑在一起，但具体中间路线有不同解释。乐队是群体的一种。',BA,
 'a rubber band 橡皮筋，a band of colour 色带，a rock band 摇滚乐队，band together 团结起来。',
 'a rubber band；a rock band；a band of；band together。',
 'band 带、乐队与 ban 禁止不是同词；a band of volunteers 只是志愿者一群，不表示他们会演奏。',
 ('A band of volunteers cleared the path.','一群志愿者清理了小路。'),('The band played until midnight.','乐队一直演奏到午夜。'),sources=['https://www.etymonline.com/word/band','https://en.wiktionary.org/wiki/band#English'])
W('banding','/ˈbændɪŋ/','条带、带状纹；加环标记；分组、结队',
 '一层一层的色带是一种 banding；给鸟戴标记环，或人聚到一组，也走各自的 band 动词义。',
 'band + -ing，条带、套带、成群等义分别名词化或形成进行时。不能只根据 -ing 猜成乐队在演奏。',BH('band + -ing → banding','带状纹；加标记环；结组活动'),
 'colour banding 色带、色阶断层，bird banding 鸟类环志，banding together 团结起来。',
 'colour banding；bird banding；banding together。',
 'banding 带状纹与 bending 弯曲不同；colour banding 不必实际有布带，是视觉上分成条带。',
 ('The image shows visible banding in the sky.','图像里的天空出现了可见色带。'),('Local groups are banding together to save the library.','当地各团体正联合起来保住图书馆。'))
W('wristband','/ˈrɪstbænd/','腕带；腕部标识带、护腕',
 '绕手腕的一圈带，可能用来吸汗、装饰，也可能证明可以入场。',
 'wrist 手腕 + band，wrist 的 w 不发音。具体用途由附加词与场景说明。',BH('wrist + band → wristband','围在手腕上的带'),
 'a festival wristband 音乐节入场腕带，a sports wristband 运动护腕，a hospital wristband 医院身份腕带。',
 'a festival wristband；a sports wristband；wear a wristband。',
 'wristband 手腕上，armband 胳膊上，waistband 腰部；不要只记 band 而忽略身体部位。',
 ('Visitors must wear a wristband to enter the venue.','访客须佩戴腕带进入场馆。'),('He wore a cotton wristband while playing tennis.','他打网球时戴着棉质护腕。'))
W('waistband','/ˈweɪstbænd/','腰头；裤腰、裙腰上的带状部分',
 '衣服贴着腰围的那一圈布，可以有弹性，也可以带扣。',
 'waist 腰 + band 带，按服装部位命名。waist 与 waste 浪费常同音，但拼写、意思不同。',BH('waist + band → waistband','衣物围腰的一圈带状部分'),
 'an elastic waistband 松紧腰，a tight waistband 紧裤腰，adjust the waistband 调腰围部位。',
 'an elastic waistband；a tight waistband；adjust the waistband。',
 'waistband 通常衣服本身的一部分，belt 腰带常是独立配件；同样围腰但结构不必相同。',
 ('The trousers have an elastic waistband.','裤子是松紧腰。'),('The skirt’s waistband felt too tight.','裙腰感觉太紧了。'))
W('bandmate','/ˈbændmeɪt/','同一乐队的成员；乐队伙伴',
 '和你在同一支乐队演奏、排练的人，mate 说共同参与者。',
 'band 乐队 + mate 伙伴，与 roommate、classmate 等人物组合的逻辑相近，但不因此把这些都当同一职业。',BH('band + mate → bandmate','与自己同队的乐队成员'),
 'my former bandmate 我以前的乐队伙伴，reunite with bandmates 与乐队伙伴重聚。',
 'a former bandmate；reunite with bandmates；a fellow bandmate。',
 'bandmate 同一乐队，bandleader 领队；伙伴不一定就是负责人。',
 ('She wrote the song with a former bandmate.','她和以前的乐队伙伴合写了这首歌。'),('His bandmates helped him prepare for the concert.','乐队伙伴帮他准备音乐会。'))
W('bandwagon','/ˈbændwæɡən/','乐队彩车；热门潮流、看涨阵营〔比喻〕',
 '热闹乐队坐在车上，别人也想跟上；后来常比喻看见某事受欢迎、像要成功就跟风加入。',
 'band 乐队 + wagon 大车，原用于游行等载乐队的彩车。政治庆祝、竞选等场合又促成加入成功阵营的比喻。',BH('band + wagon → bandwagon','载乐队的彩车 → 受追捧潮流、看似会成功的阵营'),
 'jump on the bandwagon 跟风，join the bandwagon 加入热门潮流，the bandwagon effect 从众效应。',
 'jump on the bandwagon；join the bandwagon；the bandwagon effect。',
 'bandwagon 比喻常带跟风意味，不是所有加入一项活动都缺少判断；wagon 是载人的车，不是乐队成员。',
 ('Many companies jumped on the bandwagon after the product became popular.','产品走红后，许多公司跟风加入。'),('She bought it because she liked it, not just to join the bandwagon.','她买它是因为喜欢，并不只是为了跟风。'),sources=['https://www.etymonline.com/word/bandwagon','https://en.wiktionary.org/wiki/bandwagon#English'])
W('bandwidth','/ˈbændwɪdθ/；也读 /ˈbændwɪtθ/','带宽；可用处理能力、时间精力〔比喻〕',
 '技术里先看一段频带多宽，网络日常又谈能传多少数据；人说没 bandwidth，是说没余力再接任务。',
 'band 频带 + width 宽度。频率宽度和网络数据传输能力是相关但不同的技术用法，口语再借成注意力、精力容量。',BH('band + width → bandwidth','频带宽度 → 数据传输能力；比喻可用精力容量'),
 'network bandwidth 网络带宽，use more bandwidth 占更多带宽，I do not have the bandwidth 没余力。频率宽度常以赫兹描述，数据率常以每秒比特描述。',
 'network bandwidth；limited bandwidth；use bandwidth；have the bandwidth。',
 'bandwidth 容量与 latency 延迟不同；容量大不保证每次响应都快。口语 bandwidth 不是真的给人的脑袋测网络速率。',
 ('Video calls use more bandwidth than plain text messages.','视频通话比纯文本消息占用更多带宽。'),('I do not have the bandwidth to take on another project this week.','这周我没精力再接一个项目。'))
R('B3161','条带、群体、乐队与频带容量','BAND：一圈带、一群人或一段频率，后部说明是哪支','先 band、banding；腕、腰、臂带分位置；乐队伙伴和彩车走人群支，broadband、bandwidth 走频带支。',
 '条带义有多种相关形式汇合，群体义经法语进入，深层连接有不同解释。现代频带是条状范围比喻，乐队是群体专门化。',
 'band + -ing/mate/wagon/width；wrist/waist/arm/head + band；broad/wide + band；band + stand/leader。',
 [['基础与条带','band · banding'],['身体佩戴位置','wristband · waistband · armband · headband'],['音乐与跟风','bandmate · bandleader · bandstand · bandwagon'],['通信范围与容量','broadband · wideband · bandwidth']],
 'wrist 手腕、waist 腰；bandmate 伙伴与 bandleader 领队；bandwagon 跟风；bandwidth 与延迟不同。',
 'The bandmates wore wristbands as they climbed onto the bandwagon.\n\n乐队伙伴戴着腕带，登上了载乐队的彩车。',
 'band banding wristband waistband armband headband bandmate bandleader bandstand bandwagon broadband wideband bandwidth')
if __name__=='__main__':save('continuation_20261030_ai',ROOTS,WORDS)
