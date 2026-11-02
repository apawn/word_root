"""Common people and occupations, with the older noun-forming routes retained."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'B2478':dict(words=['musician','musicians'],label='musician → musicians：从事音乐的人',note='法语音乐人名词借入，与 music 形成可学习的词族对应。'),
 'C0023':dict(words=['actor','actors'],label='actor → actors：行动者与演员',note='拉丁行动者名词经法语等借入，现代演员义最常见。'),
 'B2914':dict(words=['speaker','speakers'],label='speaker → speakers：说话者与发声设备',note='英语旧来人名词继承，发声音箱是后来用途。'),
 'B3751':dict(words=['tourist','tourists'],label='tourist → tourists：以旅行游览为活动的人',note='tour 与活动者后缀 ist 组合，不限是否跟团。'),
 'B3422':dict(words=['guest','guests'],label='guest → guests：来访者与被招待者',note='古英语本族与古诺尔斯同族形式交汇，现代也可指酒店住客。'),
 'C1280':dict(words=['scientist','scientists'],label='scientist → scientists：为科学研究者造的名称',note='十九世纪仿 artist 创造的名称，词形有 scient- 与 ist。'),
 'C0399':dict(words=['professor','professors'],label='professor → professors：公开申明与教授',note='拉丁 profess- 词族名词借入，现代学术称谓按语境理解。'),
 'B3121':dict(words=['engineer','engineers'],label='engineer → engineers：巧妙装置的设计者',note='法语装置制造者名词较早借入，现代也可作设计、促成的动词。'),
 'B2797':dict(words=['lawyer','lawyers'],label='lawyer → lawyers：法律从业者',note='中古英语名词对应 law 与 yer 的从业者词尾。'),
 'C0844':dict(words=['nurse','nurses'],label='nurse → nurses：哺育、照护与护士',note='法语哺育名词与英语 nourish 旧形共同参与现代名动词发展。'),
 'B3525':dict(words=['neighbour','neighbours'],label='neighbour → neighbours：附近的居住者',note='古英语近与居住者组合，美式另拼 neighbor、neighbors。'),
 'C0397':dict(words=['stranger','strangers'],label='stranger → strangers：外来者与不认识的人',note='拉丁外来的词族经法语、英语不同分析形成名词，不是形容词比较级。'),
}
W('musicians','/mjuˈzɪʃənz/','音乐家、乐手〔musician 的复数〕',
 '唱、演奏、创作等音乐活动里有专业技能的人，是 musicians；可以是管弦乐团成员，也可以是独立创作者。',
 'musician + -s，/n/ 后读 /z/。musician 经古法语 musicien 到中古英语，现代对照 music 与 -ian、-ician；music 末尾的 /k/ 与 musician 中的 /ʃ/ 是词族语音对应。',
 [['古法语 musicien → 中古英语 → musician','从事音乐、具有音乐技艺的人'],['musician + -s → musicians','多位音乐家、乐手']],
 'local musicians 当地乐手；professional musicians 职业音乐家；musicians in the orchestra 乐团成员。',
 'musicians practising together；musicians invited to perform。','musicians 不只指作曲家，也可以是演奏、演唱等从事音乐的人。music 重音在前，musician 重音转到 /zɪʃ/ 这一段。',
 ('Local musicians performed in the square.','当地乐手在广场上演出。'),('The musicians rehearsed together before the concert.','音乐家们在音乐会前一起排练。'),sources=['https://en.wiktionary.org/wiki/musicians#English','https://en.wiktionary.org/wiki/musician#English'])
W('actors','英 /ˈæktəz/；美 /ˈæktərz/','演员；行动主体、参与者〔actor 的复数〕',
 '在舞台、镜头前扮演角色的人，是 actors；分析一件事由谁推动时，文章也会借这个行动者词说参与主体。',
 'actor + -s，词尾读 /z/。actor 经法语、拉丁 āctor 借入，接 agere 行动的 āct- 词干；现代可认 act + -or，但名词不是只在现代英语临时加尾造出。',
 [['拉丁 agere、āct- → āctor → 法语等 → actor','行动者 → 扮演角色的演员等'],['actor + -s → actors','多位演员；多个参与主体']],
 'film actors 电影演员；stage actors 舞台演员；key actors 关键行动方。',
 'actors preparing for a scene；actors involved in the process。','actors 常说演员，也可以不分性别地称演员。学术、政策分析中的 key actors 往往是重要参与者、机构，不一定是演戏的人。',
 ('The actors rehearsed the scene twice.','演员们把这场戏排练了两遍。'),('The report identifies the main actors in the project.','报告指出了项目的主要参与方。'),sources=['https://en.wiktionary.org/wiki/actors#English','https://en.wiktionary.org/wiki/actor#English'])
W('speakers','英 /ˈspiːkəz/；美 /ˈspiːkərz/','说话者、发言者；扬声器〔speaker 的复数〕',
 '人在把话说出来，是 speakers 的说话者义；设备把声音放出来，也沿发声这个功能叫 speakers。',
 'speak + -er → speaker，再加 -s，词尾 /z/。古英语已有相应说话者名称；后来发声设备借用人名词，特定大写 Speaker 还可作议会职务称呼。',
 [['古英语说话者名词、speak + -er → speaker','说话、发言的人'],['发声设备扩展；speaker + -s → speakers','多位说话者；多个扬声器']],
 'guest speakers 特邀演讲者；native speakers 母语者；computer speakers 电脑扬声器。',
 'speakers at the meeting；speakers connected to the laptop。','native speakers 指以某语言为母语的人，不等于每个人都研究该语言。设备语境 speakers 是音箱、扬声器，按声音输出功能理解。',
 ('The speakers answered questions after their talks.','演讲结束后，发言者们回答了问题。'),('The speakers are connected to the laptop.','扬声器连接着笔记本电脑。'),sources=['https://en.wiktionary.org/wiki/speakers#English','https://en.wiktionary.org/wiki/speaker#English'])
W('tourists','英 /ˈtʊərɪsts/；美 /ˈtʊrɪsts/','游客、观光者〔tourist 的复数〕',
 '为了游览、体验不同地方而出行的人，是 tourists；可自己走，也可跟团，重点是旅行游览的活动。',
 'tour + -ist → tourist，再加 -s，/t/ 后读 /s/。tour 是游览、环行相关借词，-ist 在英语里命名从事活动的人；tour 的法语、拉丁上游有转动材料。',
 [['tour + -ist → tourist','游览活动 → 游客'],['tourist + -s → tourists','多位观光者']],
 'foreign tourists 外国游客；tourists visiting the town 到镇上游览的游客；attract tourists 吸引游客。',
 'tourists taking photographs；tourists arriving by train。','tourists 与 travellers 会重叠：tourists 更突出游览目的，travellers 范围更广。词尾 /sts/ 连在一起，实际口语可能有弱化。',
 ('Tourists gathered near the old bridge.','游客们聚在老桥附近。'),('The museum attracts tourists from many countries.','这家博物馆吸引许多国家的游客。'),sources=['https://en.wiktionary.org/wiki/tourists#English','https://en.wiktionary.org/wiki/tourist#English'])
W('guests','/ɡests/','客人、来宾；酒店住客〔guest 的复数〕',
 '来到某人家里、某个活动里，受到招待的一方，是 guests；酒店里付费住宿的人也叫 guests。',
 'guest + -s，/t/ 后读 /s/。guest 延续古英语 gæst、ġiest 等，并受古诺尔斯语 gestr 同族形式影响；更早是陌生来者、主客互相招待的词族。',
 [['古英语与古诺尔斯同族形式 → guest','来者、陌生人 → 被招待的客人'],['guest + -s → guests；住宿、节目等用途','多位来宾、住客或受邀参与者']],
 'wedding guests 婚礼宾客；hotel guests 酒店住客；invited guests 受邀来宾。',
 'guests arriving for dinner；guests staying at the hotel。','host 是招待的一方，guest 是被招待的一方；更远同族背景不使现代角色互换。hotel guests 即使付费，也可以用 guest 强调接待关系。',
 ('The guests arrived just before dinner.','客人们在晚餐开始前不久到了。'),('Hotel guests can leave their bags at reception.','酒店住客可以把行李留在前台。'),sources=['https://en.wiktionary.org/wiki/guests#English','https://www.etymonline.com/word/guest'])
W('scientists','/ˈsaɪəntɪsts/','科学家、科学研究人员〔scientist 的复数〕',
 '以研究、观察、检验来增进科学知识的人，是 scientists。这个总称比许多具体学科名称出现得晚，是近代有记录的造词。',
 'scientist + -s，/t/ 后读 /s/。William Whewell 仿 artist，用拉丁 scientia 的 scient- 与 -ist 造出 scientist，1834 年已有出版记录；现代把它同 science 放在一族学习。',
 [['scient- 科学知识材料 + -ist；仿 artist → scientist','近代为科学研究者创造的总称'],['scientist + -s → scientists','多位科学研究人员']],
 'research scientists 科研人员；young scientists 青年科学家；scientists studying the climate 研究气候的科学家。',
 'scientists comparing results；scientists working together。','science 读 /ˈsaɪəns/，scientist 读 /ˈsaɪəntɪst/，词族形态里出现 scient-。科学总称与某个专业的研究者名称可以并用。',
 ('The scientists compared results from several experiments.','科学家们比较了几次实验的结果。'),('Young scientists presented their work at the meeting.','青年科学家在会上展示了自己的工作。'),sources=['https://en.wiktionary.org/wiki/scientists#English','https://www.etymonline.com/word/scientist'])
W('professors','英 /prəˈfesəz/；美 /prəˈfesərz/','教授、大学教师〔professor 的复数，称呼范围随地区〕',
 '在大学等场合公开讲授自己专门知识的人，是 professors；词族更早有公开申明、表明专门身份的背景。',
 'professor + -s，词尾读 /z/。拉丁 professor 接 profitērī 公开申明的 profess- 词干，经法语或直接拉丁借入；现代可对照 profess 与 -or，教学称谓逐渐固定。',
 [['拉丁 profitērī、profess- → professor → 英语','公开申明 → 以专门学识讲授者'],['professor + -s → professors','多位教授、大学教师']],
 'university professors 大学教授；visiting professors 访问教授；professors of history 历史学教授。',
 'professors attending the seminar；professors from different departments。','professor 在各地可以是特定职称，也可在某些语境泛称大学教师；读句子时结合大学、国家和称呼习惯。它与学生 student 的角色不同。',
 ('Professors from several departments attended the seminar.','几个院系的教授参加了研讨会。'),('The students interviewed two professors of history.','学生们采访了两位历史学教授。'),sources=['https://en.wiktionary.org/wiki/professors#English','https://en.wiktionary.org/wiki/professor#English'])
W('engineers','英 /ˌendʒɪˈnɪəz/；美 /ˌendʒɪˈnɪrz/','工程师〔复数〕；设计、促成〔第三人称单数〕',
 '把知识变成能运行的装置、系统或工程的人，是 engineers；把某种结果经过安排促成，也能用 engineer 作动词。',
 'engineer + -s，词尾读 /z/。名词较早经法语 engigneor 等借入，与 engin 巧妙装置、战械同族，较早接拉丁 ingenium 巧思；英语后来由名词形成设计、促成的动词。',
 [['拉丁 ingenium → 法语 engin、engigneor → engineer','巧思、机械装置 → 装置设计制造者'],['engineer + -s → engineers；职业、动作扩展','多位工程师；单数主语设计、促成']],
 'civil engineers 土木工程师；software engineers 软件工程师；engineers a solution 设计出解决方案。',
 'engineers inspecting the bridge；engineers a change in the process。','engineers 今天不限发动机制造者，软件、土木、电气等都有工程师。engineers a change 中是动词，常强调通过设计、安排使结果发生。',
 ('The engineers inspected the bridge before it reopened.','桥梁重新开放前，工程师们进行了检查。'),('The company employs engineers from several fields.','这家公司雇用了几个领域的工程师。'),sources=['https://en.wiktionary.org/wiki/engineers#English','https://en.wiktionary.org/wiki/engineer#English'])
W('lawyers','英 /ˈlɔɪəz/；美 /ˈlɔɪərz/、/ˈlɑːjərz/','律师、法律从业者〔lawyer 的复数〕',
 '专门研究、运用法律来处理事务的人，是 lawyers；先抓职业领域 law，再记 -yer 给从业者命名。',
 'law + -yer → lawyer，再加 -s，词尾读 /z/。中古英语已有 lawiere、lawier、lawer 等形式；law 自身经北欧相关法律词传入，-yer 是这里的从业者词尾。',
 [['law + -yer；中古英语 lawiere 等 → lawyer','法律 → 处理法律事务的人'],['lawyer + -s → lawyers','多位律师、法律从业者']],
 'lawyers at the firm 律所里的律师；lawyers specialising in... 专门从事某领域的律师。',
 'lawyers reviewing documents；lawyers speaking at the meeting。','lawyer 的常见发音有 /lɔɪ/ 和美式 /lɑːj/ 的地区差别。读这类职业词时，后面的修饰语常交代具体专长或工作单位。',
 ('The lawyers reviewed the documents before the meeting.','律师们在会前审阅了文件。'),('Several lawyers spoke at the university event.','几位律师在这场大学活动中发言。'),sources=['https://en.wiktionary.org/wiki/lawyers#English','https://en.wiktionary.org/wiki/lawyer#English'])
W('nurses','英 /ˈnɜːsɪz/；美 /ˈnɜːrsɪz/','护士〔复数〕；照护、哺育等〔第三人称单数〕',
 '照顾病人、帮助护理的人，是 nurses 的职业义；动词则把注意放在照料、使其恢复或成长的动作上。',
 'nurse + -s，/s/ 后增加 /ɪz/。名词经法语 norrice 接拉丁哺育词族，旧指哺育儿童者；动词还接中古英语 nourish 的旧形，并受名词影响，后来发展为护理等义。',
 [['拉丁哺育词族 → 法语 norrice → nurse 名词','哺育、照顾儿童者 → 护理职业'],['中古英语滋养动词旧形与名词影响 → nurse；加 -s','多位护士；单数主语照护、哺育']],
 'hospital nurses 医院护士；nurses caring for patients 照护病人的护士；nurses the injured animal 照料受伤动物。',
 'nurses on the morning shift；nurses a young animal。','nurses 既是职业复数，也是单数主语的动词。现代职业名称本身不限定性别；读动作句时，看它后面照料的对象。',
 ('The nurses prepared the room for the new patients.','护士们为新来的病人准备了房间。'),('She nurses injured animals at the rescue centre.','她在救助中心照料受伤动物。'),sources=['https://en.wiktionary.org/wiki/nurses#English','https://www.etymonline.com/word/nurse'])
W('neighbours','英 /ˈneɪbəz/；美 /ˈneɪbərz/','邻居；邻近的人或地方〔复数；美式 neighbors〕',
 '住在附近的人，就是 neighbours；把人换成相邻国家、建筑，也可以借用邻居这个关系。',
 'neighbour + -s，词尾 /z/。继承古英语 nēahġebūr，内部是 nēah 近与 ġebūr 居住者，经中古英语不同拼写发展；美式拼作 neighbor、neighbors。',
 [['古英语近 + 居住者 → nēahġebūr → neighbour','住得近的人 → 邻居'],['neighbour + -s → neighbours','多个邻居、邻近者；美式拼写少 u']],
 'next door neighbours 隔壁邻居；friendly neighbours 友好的邻居；neighbouring countries 邻国〔同族形容形式〕。',
 'neighbours living upstairs；neighbours helping each other。','neighbours 与 neighbors 是英美拼写差别。附近同住的人可叫 neighbours，国家之间的邻接关系也可这样描述。',
 ('Our neighbours helped us carry the table upstairs.','邻居们帮我们把桌子搬上了楼。'),('The two countries are close neighbours.','这两个国家彼此毗邻。'),sources=['https://en.wiktionary.org/wiki/neighbours#English','https://en.wiktionary.org/wiki/neighbour#English'])
W('strangers','英 /ˈstreɪndʒəz/；美 /ˈstreɪndʒərz/','陌生人；外来者、不熟悉某事的人〔stranger 的复数〕',
 '对你来说还不认识的人，是 strangers；来到不熟悉地方的人，也保留了外来者这层历史画面。',
 'stranger + -s，词尾读 /z/。名词有古法语 estrangier 外来者借入的分析，也有英语 strange + -er 的分析；都接拉丁 extrāneus 外来的词族。',
 [['拉丁 extrāneus → 法语相关形式、英语 strange 词族','外来的 → 不熟悉的；外来者'],['stranger + -s → strangers','多个陌生人、外来者']],
 'complete strangers 完全陌生的人；strangers to the town 初到这个镇的人；no strangers to hard work 很熟悉辛苦工作。',
 'strangers meeting for the first time；strangers to the area。','strangers 在这里是人名词；strange 的比较级也可写 stranger，表示更奇怪，但那是另一种句法用途。no stranger to something 是对某事不陌生。',
 ('The two travellers were complete strangers before the trip.','旅行前，这两名旅客彼此完全不认识。'),('The volunteers welcomed strangers to the town.','志愿者欢迎初到镇上的人。'),sources=['https://en.wiktionary.org/wiki/strangers#English','https://en.wiktionary.org/wiki/stranger#English'])
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_yu',ROOTS,WORDS)
 extend_lessons()
