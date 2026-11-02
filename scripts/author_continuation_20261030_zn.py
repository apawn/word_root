"""Common plural forms with distinct senses and stress patterns."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'C1346':dict(words=['single','singles'],label='single → singles：单个到单曲、单打',note='拉丁各自一个的词经法语借入，现代领域用途分别发展。'),
 'C0200':dict(words=['center','centers','centre'],label='center → centers；centre：中心与英美拼写',note='希腊尖点、拉丁中心词经法语借入，美式 er、英式 re 各有习惯。'),
 'A1760':dict(words=['title','titles'],label='title → titles：标识文字到标题、头衔',note='拉丁 titulus 经法语等路线，现代权利、比赛冠军等另看语境。'),
 'C1534':dict(words=['contract','contracts'],label='contract → contracts：拉拢、约定与收缩',note='拉丁 con 与 trahere，名词合同前重音，动词收缩、订约后重音。'),
 'C0503':dict(words=['congratulation','congratulations'],label='congratulation → congratulations：为别人一起高兴',note='拉丁祝贺名词独立借入，英语复数发展为祝贺感叹表达。'),
 'B3132':dict(words=['stop','stops'],label='stop → stops：堵住到停止、停靠处',note='本族及日耳曼堵塞词，名词停站、动词停下各有用途。'),
 'B2805':dict(words=['race','races'],label='race → races：竞速与族群分类另源',note='快跑支接本族、北欧词；血统分类支经法语借入。'),
 'B3296':dict(words=['rock','rocks'],label='rock → rocks：石头与摇动分支',note='岩石义与摇动动词有不同旧形式，音乐用法接摇动支。'),
 'B2924':dict(words=['boot','boots'],label='boot → boots：靴子、踢与启动',note='靴子接法语；电脑启动缩自 bootstrap 的技术用法。'),
 'C0560':dict(words=['period','periods'],label='period → periods：绕行到有边界的一段',note='希腊周围与路组成，时间、句段与句号等用途逐步发展。'),
 'B2962':dict(words=['ring','rings'],label='ring → rings：圆环与鸣响两支',note='古英语 hring、hringan 分别传下，过去式与分词变化不同。'),
 'B3955':dict(words=['master','masters'],label='master → masters：熟练者、负责人、母版',note='拉丁 magister 早借入英语并受法语影响，专业用途另看语境。'),
 'B3365':dict(words=['tie','ties'],label='tie → ties：系结、领带、联系和平局',note='古英语绳带、系结词后来汇入同形，现代名词与动词并学。'),
 'B2812':dict(words=['bear','bears'],label='bear → bears：熊与承载动词分支',note='古英语 bera 动物名和 beran 承载动词分开看。'),
 'B2565':dict(words=['blue','blues'],label='blue → blues：蓝色、低落与音乐名称',note='颜色词经法语接日耳曼来源，忧郁义与音乐义有各自后续历史。'),
}
W('singles','/ˈsɪŋɡəlz/','单曲、单打、单身人士等〔复数或集合用法〕',
 '把一个单位单独拿出来，是 singles 的共同线索：一首单独发行的歌、每边一位选手的单打、未有配偶或伴侣的人。具体对象随领域改变。',
 'single + -s，/l/ 后读 /z/。single 经古法语 sengle 等接拉丁 singulus 各自一个，英语形容词再有名词用途；领域中的 singles 不都按普通可数复数处理。',
 [['拉丁 singulus → 法语 → single','单独、一个 → 单个项目、单人角色'],['single + -s → singles；领域用途','多首单曲、单身群体；单打项目']],
 'release singles 发行单曲；play singles 打单打；events for singles 单身人士活动。',
 'her early singles 她早期的单曲；the singles final 单打决赛。','网球 singles 是项目名，末尾有 s 也可按一个项目说 Singles is...。音乐中的 singles 则常是一首首单曲；doubles 是双打。',
 ('The band released two singles before the album.','乐队在专辑发行前推出了两首单曲。'),('She prefers playing singles to doubles.','她更喜欢打单打而不是双打。'),sources=['https://en.wiktionary.org/wiki/singles#English','https://en.wiktionary.org/wiki/single#English'])
W('centers','英 /ˈsentəz/；美 /ˈsentərz/','中心、中央部分；中心机构〔复数，美式拼写〕；集中〔第三人称单数〕',
 '把注意或活动围绕一个中间点组织起来，是 centers 的线索。名词可以指几何中心，也可以指医疗、学习、社区活动集中发生的地方。',
 'center + -s，末尾读 /z/。center、centre 经法语接拉丁 centrum，较早希腊 kentron 尖点、中心点；center 常见美式拼写，centre 常见英式，动词后由名词等发展。',
 [['希腊 kentron → 拉丁 centrum → 法语、英语 center','尖点、定点 → 中心'],['center + -s → centers','多个中心；单数主语集中、围绕']],
 'community centers 社区中心；learning centers 学习中心；centers on a question 围绕一个问题展开。',
 'centers of activity 活动中心；centers the image 把图像居中。','英式常写 centres。centers on something 的主语可以是讨论、故事，意思是围绕它；center something 则把某物放在中间。',
 ('The city has several community centers.','这座城市有几个社区中心。'),('The discussion centers on how to improve the service.','讨论围绕如何改进服务展开。'),sources=['https://en.wiktionary.org/wiki/centers#English','https://en.wiktionary.org/wiki/center#English'])
W('titles','/ˈtaɪtəlz/','标题、书名、片名；头衔、冠军称号〔复数〕；命名〔第三人称单数〕',
 '给一个作品或身份挂上一块名字牌，就是 titles 的理解线索。书有书名，人有职务头衔，比赛胜者获得冠军称号。',
 'title + -s，/l/ 后读 /z/。title 接拉丁 titulus 铭文、标签、称号，经法语 title 等及较早英语借入路线延续；动词后来可说给作品定名。',
 [['拉丁 titulus → 法语等 → title','标示名称的文字 → 标题、身份或资格'],['title + -s → titles','多个名称、称号；单数主语给作品定名']],
 'book titles 书名；job titles 职务名称；win titles 赢得冠军；film titles 片名。',
 'titles of the chapters 各章标题；several national titles 几个全国冠军称号。','titles 可以按出版品说若干种书，也可以数名称本身。房产权利相关 title 是另一常用法律语境，不能每次都译作标题。',
 ('The list includes the titles of all her books.','清单列出了她所有作品的书名。'),('The team has won three national titles.','这支队伍赢得过三个全国冠军。'),sources=['https://en.wiktionary.org/wiki/titles#English','https://en.wiktionary.org/wiki/title#English'])
W('contracts','名词英 /ˈkɒntrækts/、美 /ˈkɑːntrækts/；动词 /kənˈtrækts/','合同、契约〔复数〕；收缩、订约、感染〔第三人称单数〕',
 '把双方拉到一项约定里，是合同的理解线索；把一个东西向内拉紧，是收缩。contracts 用不同重音区分这些名词、动词用途。',
 'contract + -s，/t/ 后读 /s/。拉丁 con- 一起 + trahere 拉 → contrahere，接 contractus 等形式；名词、动词各经法语、拉丁相关路线借入，现代重音分化。',
 [['拉丁 contrahere、contractus → 法语、英语 contract','拉到一起 → 订约、合同；缩紧'],['contract + -s → contracts','名词多份合同；动词单数主语收缩等']],
 'sign contracts 签合同；contracts with suppliers 与供应商的合同；the muscle contracts 肌肉收缩。',
 'employment contracts 雇用合同；contracts a disease 染上某种疾病。','合同名词前重音；收缩、感染等动词后重音。contract a disease 是染病，contract to do 是订约做某事，要按宾语和结构分别理解。',
 ('The two companies signed the contracts on Monday.','两家公司周一签了合同。'),('The muscle contracts when the signal reaches it.','信号到达时，肌肉便收缩。'),sources=['https://en.wiktionary.org/wiki/contracts#English','https://en.wiktionary.org/wiki/contract#English'])
W('congratulations','/kənˌɡrætʃəˈleɪʃənz/','祝贺、道贺；恭喜！',
 '别人有了值得高兴的收获，自己也走过去为他高兴、表达认可，就是 congratulations。它是把祝贺直接说给对方的常用词。',
 'congratulation + -s，/n/ 后读 /z/。名词独立借拉丁 congratulātiō，接 con- 一起与 grātulārī 表示喜悦、致意；英语祝贺感叹语由名词复数发展，不是英语先造 congratulate 才有全部名词。',
 [['拉丁 congratulātiō → congratulation','一起表达喜悦 → 祝贺'],['名词复数 congratulations → 感叹表达','祝贺的话；对别人说恭喜']],
 'Congratulations on your success! 恭喜你成功！；send congratulations 送上祝贺；congratulations to the winners 向获胜者祝贺。',
 'warm congratulations 热烈祝贺；Congratulations on finishing the course! 恭喜你完成课程！','常用复数 Congratulations!。对谁祝贺用 to，因什么祝贺用 on；on 后可接名词或 -ing。',
 ('Congratulations on your new job!','恭喜你找到新工作！'),('She sent her congratulations to the whole team.','她向整个团队送上祝贺。'),sources=['https://en.wiktionary.org/wiki/congratulations#English','https://www.etymonline.com/word/congratulation'])
W('stops','英 /stɒps/；美 /stɑːps/','停靠站、停顿；挡块等〔复数〕；停下、阻止〔第三人称单数〕',
 '把一条继续走的路堵住，事情就停下了。stops 可以说这个停止动作，也可以指车辆停靠、让人上下的一个个站点。',
 'stop + -s，/p/ 后读 /s/。stop 接古英语 stoppian、中古英语 stoppen 堵塞、封住，后来停止、阻止成为常见动词用途，再有停站等名词。',
 [['古英语 stoppian → stop','堵住通路 → 停止、使停止'],['stop + -s → stops；名词用途','单数主语停下；多处停靠点、停顿']],
 'bus stops 公交站；two stops away 隔两站；stops working 停止工作；stops to rest 停下来休息。',
 'stops at the station 在站上停靠；stops the noise 制止噪声。','stop doing 是停止正在做的事；stop to do 是停下原来的事去做另一件事。stops 是现在单数，过去式 stopped 双写 p。',
 ('The bus stops outside the library.','公交车在图书馆外停靠。'),('The museum is only two stops away.','博物馆只隔两站。'),sources=['https://en.wiktionary.org/wiki/stops#English','https://en.wiktionary.org/wiki/stop#English'])
W('races','/ˈreɪsɪz/','竞速比赛〔复数〕；疾跑、快速运转〔第三人称单数〕；种族等分类〔另一词源〕',
 '比谁先到终点，是 races 的竞赛画面；心跳飞快、思绪飞转，也可用动词 races。谈族群分类的 races 则另有词源，不能和快跑编成同一故事。',
 'race + -s，/s/ 后读 /ɪz/。快跑支接北欧 rás 及古英语同族词；血统、族群分类支经法语 race，可能联系意大利 razza，更远来源未定。',
 [['北欧、本族快跑词 → 竞速 race；法语分类词 → 另一 race','两支历史不同，今天同形同音'],['race + -s → races','多场比赛；单数主语快速移动；多种分类称呼']],
 'running races 跑步比赛；horse races 赛马；her heart races 她心跳很快。',
 'races against time 与时间赛跑；races across the field 飞快穿过场地。','race 的族群分类义要按社会、历史语境理解；竞速比赛义关注快慢、先后。人心里紧张时 heart races 并不要求真的在跑步。',
 ('The school held several races on sports day.','学校在运动日举行了几场赛跑。'),('Her heart races whenever she speaks in front of a large audience.','每当面对大批听众发言，她就心跳加快。'),sources=['https://en.wiktionary.org/wiki/races#English','https://www.etymonline.com/word/race'])
W('rocks','英 /rɒks/；美 /rɑːks/','岩石、石块〔复数〕；摇动、震动；很棒〔第三人称单数等〕',
 'rocks 可以是地上硬实的一块块石头，也可以说船、椅子来回摇。音乐与口语夸赞的 rocks 更接近让人随节奏摇动、兴奋的那条线。',
 'rock + -s，/k/ 后读 /s/。岩石词有古英语 rocc 和法语 roque、roche 等影响，更远未定；摇动动词接古英语 roccian，音乐 rock 后缩自 rock and roll 等用途。',
 [['岩石名词与摇动动词 → 现代 rock','石块；来回摇动，两支分开看'],['rock + -s → rocks；音乐、口语扩展','多个石块；单数主语摇动，或夸某事很棒']],
 'rocks by the river 河边的石头；rocks the cradle 摇摇篮；This song rocks! 这首歌真带劲！',
 'climb over the rocks 爬过岩石；the boat rocks 船摇晃。','rock 音乐义通常不数成 rocks；rocks 常是石头或动词形式。rock the boat 也可比喻打破现状、惹起波动。',
 ('We sat on the rocks beside the river.','我们坐在河边的岩石上。'),('The boat rocks gently in the water.','船在水中轻轻摇晃。'),sources=['https://en.wiktionary.org/wiki/rocks#English','https://www.etymonline.com/word/rock'])
W('boots','/buːts/','靴子〔复数〕；踢；启动〔第三人称单数〕',
 '脚上包得较高的靴子是 boots；用靴子踢，是动词的一条路。电脑 boots up 的启动义又经 bootstrap 这个较长技术词缩短而来。',
 'boot + -s，/t/ 后读 /s/。靴子 boot 经古法语 bote 借入，更远来源未定；动词踢接靴子动作，电脑 boot 缩自 bootstrap 的启动用途，不能只用踢解释电脑。',
 [['古法语 bote → boot 靴子；英语相关动词','靴子 → 穿靴踢等动作'],['bootstrap 技术用途缩短 → boot；加 -s → boots','电脑启动；多双或多只靴子、动词单数形式']],
 'walking boots 徒步靴；a pair of boots 一双靴子；boots up quickly 启动很快。',
 'muddy boots 沾泥的靴子；boots the ball downfield 把球踢向前场。','boots 作鞋类常按复数说，一双用 a pair of boots。to boot 此外、而且接另一古英语好处词的历史，不与电脑启动硬串。',
 ('Leave your muddy boots by the door.','把沾泥的靴子留在门边。'),('The new computer boots up in a few seconds.','新电脑几秒钟就能启动。'),sources=['https://en.wiktionary.org/wiki/boots#English','https://en.wiktionary.org/wiki/boot#English'])
W('periods','英 /ˈpɪəriədz/；美 /ˈpɪriədz/','时期、一段段时间；课时、局；句号；月经期〔复数〕',
 '把连续的时间或表达划出一段有边界的范围，就是 periods 的共同理解线索。历史时期、学校一节课、完整句段的结束，都能从一段来认识。',
 'period + -s，/d/ 后读 /z/。希腊 peri- 周围 + hodos 路 → periodos 绕行、一周，经拉丁、法语借入；时间段、完整句段和句号等分别发展。',
 [['希腊 periodos → 拉丁、法语 → period','绕行、完整一周 → 有界的一段、周期'],['period + -s → periods；领域用途','多段时间、课时；句号及生理周期用途']],
 'long periods 很长的几段时间；class periods 课时；periods in history 历史时期；periods at the ends of sentences 句末句号。',
 'periods of rest 休息时段；short periods of activity 短时活动。','句号义在美式英语常见，英式常叫 full stops。periods 也常指月经期，需按谈话内容判断，不把所有场景都译成时期。',
 ('The course compares two periods in history.','课程比较两个历史时期。'),('Avoid sitting still for long periods.','避免长时间坐着不动。'),sources=['https://en.wiktionary.org/wiki/periods#English','https://en.wiktionary.org/wiki/period#English'])
W('rings','/rɪŋz/','环、戒指、圈〔复数〕；响、打电话〔第三人称单数〕',
 '圆圆围成一圈的东西是 rings；铃、电话发出声音也写 rings。形状与声音是两条旧词支线，今天碰到了一样的拼写。',
 'ring + -s，/ŋ/ 后读 /z/。圆环名词接古英语 hring，鸣响动词接 hringan；环绕的动词后来接圆环用途。名词复数和动词三单同形。',
 [['古英语 hring 与 hringan → 两支 ring','环形物；发出响声'],['ring + -s → rings','多个圆环、戒指；单数主语鸣响或打电话']],
 'wedding rings 结婚戒指；rings of smoke 一圈圈烟；the phone rings 电话响。',
 'tree rings 树木年轮；rings her mother 给母亲打电话〔常见英式〕。','鸣响动词过去式 rang、过去分词 rung；围成圈的动词通常 ringed。ring somebody 在英式英语常指给人打电话。',
 ('The phone rings while she is making dinner.','她做饭时电话响了。'),('The children counted the rings in the tree stump.','孩子们数了树桩上的年轮。'),sources=['https://en.wiktionary.org/wiki/rings#English','https://en.wiktionary.org/wiki/ring#English'])
W('masters','英 /ˈmɑːstəz/；美 /ˈmæstərz/','大师、熟练者；主人、负责人；母版〔复数〕；掌握〔第三人称单数〕',
 '对某件事有很强掌握能力的人，是 masters 的大师、高手；动词 masters 则是把技能学到能熟练控制。另一些头衔、母版用途要结合领域理解。',
 'master + -s，末尾读 /z/。master 是古英语较早借入拉丁 magister 负责人、老师的词，中古英语又受法语 maistre 影响；英语动词掌握及多种专业名词后来发展。',
 [['拉丁 magister → 古英语，并受法语影响 → master','负责人、老师 → 熟练者、大师等'],['master + -s → masters','多位大师；单数主语熟练掌握；专业原版等']],
 'masters of the craft 这门手艺的大师；masters a skill 掌握一项技能；original masters 原始母版。',
 'learn from the masters 向大师学习；masters the basics 掌握基础。','硕士学位通常写 a master’s degree，注意所有格符号；masters 单独还可有专业比赛名称等用途。母版 master 是供复制的原始版本。',
 ('The exhibition brings together works by several masters.','展览汇集了几位大师的作品。'),('She masters new techniques through careful practice.','她通过认真练习掌握新技术。'),sources=['https://en.wiktionary.org/wiki/masters#English','https://en.wiktionary.org/wiki/master#English'])
W('ties','/taɪz/','领带、绳带；联系、关系；平局〔复数〕；系上、打平〔第三人称单数〕',
 '把两边接在一起，是 ties 的系结、联系画面；一条系在颈部的带子是领带。比赛双方停在同一个结果上，则是平局。',
 'tie + -s → ties，保留 ie，末尾读 /z/。名词绳带与动词系结各有古英语相关形式，后来合到现代 tie；领带、关系、比分持平等用途逐步发展。',
 [['古英语绳带、系结词 → tie','系在一起 → 带子、联结、领带'],['tie + -s → ties；比赛用途','多个带子、关系、平局；单数主语系结或打平']],
 'family ties 亲情纽带；ties with the community 与社区的联系；ties his shoes 系鞋带。',
 'wear ties 戴领带；ties for first 并列第一。','ties 可以说关系，不一定有实际绳子。比赛中的 ties 依规则可能是平局、并列名次；某些英式体育语境 a tie 还可指一场对阵。',
 ('She keeps close ties with her hometown.','她与家乡保持密切联系。'),('He ties his shoes before leaving the house.','他出门前系好鞋带。'),sources=['https://en.wiktionary.org/wiki/ties#English','https://en.wiktionary.org/wiki/tie#English'])
W('bears','英 /beəz/；美 /berz/','熊〔复数〕；承受、携带、具有、结果实〔第三人称单数〕',
 '山林里的 bears 是熊；一座桥 bears weight，是承住重量；树 bears fruit，是长出果实。动物名和承载动词有两条不同的旧词来路。',
 'bear + -s，结尾读 /z/。熊接古英语 bera，承载动词接 beran；熊名更远常联系棕色的称呼，但仍有讨论。动词现代过去式 bore，常用过去分词 borne。',
 [['古英语 bera → 熊 bear；beran → 承载 bear','动物名与携带、承受动词分别延续'],['bear + -s → bears','多只熊；单数主语承载、具有或生出果实']],
 'wild bears 野生熊；bears the weight 承重；bears her name 带有她的名字；bears fruit 结果实、见成效。',
 'bears responsibility 承担责任；bears a resemblance 有相似之处。','be born 出生用 born；普通承载、承受的过去分词多用 borne。bears fruit 可以是真结果，也可以说努力开始有成果。',
 ('The bridge bears the weight of heavy vehicles.','桥承受重型车辆的重量。'),('We saw bears near the edge of the forest.','我们在森林边缘看见了熊。'),sources=['https://en.wiktionary.org/wiki/bears#English','https://en.wiktionary.org/wiki/bear#English'])
W('blues','/bluːz/','蓝调、布鲁斯音乐；忧郁、低落；不同蓝色〔复数等〕',
 'blues 可以说心情低落，也可以是音乐类型蓝调。谈配色时，它又只是各种深浅的蓝色。先确定场景，再接相应意思。',
 'blue + -s，/uː/ 后读 /z/。颜色词经法语接日耳曼来源；blue 的低落义很早存在，blues 后指忧郁，音乐名称较晚发展，具体命名历史不简化成唯一传说。',
 [['blue 颜色、低落义 → blues','不同蓝色；忧郁、低落情绪'],['音乐领域的 blues → 类型名称','与低落表达等背景相关的蓝调音乐']],
 'listen to the blues 听蓝调；have the blues 心情低落；blues and greens 蓝色与绿色的各类色调。',
 'a blues singer 蓝调歌手；soft blues 柔和的各种蓝色。','音乐类型 blues 常按单数理解：Blues is...。说低落可用 the blues；说多种蓝色时则是普通复数。音乐名称不等于每首歌都只写伤心。',
 ('She enjoys listening to the blues in the evening.','她喜欢晚上听蓝调。'),('The room is decorated in soft blues and greens.','房间用柔和的蓝色和绿色装饰。'),sources=['https://en.wiktionary.org/wiki/blues#English','https://www.etymonline.com/word/blues'])
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_zn',ROOTS,WORDS)
 extend_lessons()
