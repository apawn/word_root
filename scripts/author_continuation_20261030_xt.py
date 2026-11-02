"""People and roles: citizens, residents, participants and audiences."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'C0227':dict(words=['citizen','citizens'],label='citizen → citizens：共同体中的成员',note='从城镇居民到国家公民，借词中间有法语城市词族；现代没有自由造词的 -zen 人后缀。'),
 'C1297':dict(words=['resident','residents'],label='reside／resident → residents：留下居住的人',note='坐下、停留的词族发展到在某处居住的身份。'),
 'C0401':dict(words=['official','officials'],label='official → officials：担任正式职务的人',note='official 名词、形容词接拉丁 officialis；officials 常说官员或执行职务的人员。'),
 'B3077':dict(words=['soldier','soldiers'],label='soldier → soldiers：领军饷的军人与坚持前行',note='金币、军饷到服役者的历史，和现代士兵、军人相关；soldier on 是继续坚持。'),
 'B3925':dict(words=['owner','owners'],label='own／owner → owners：拥有者',note='现代 own + er 的对应帮助记忆；owner 本身也有较早英语词形，历史比现代组合更长。'),
 'C0961':dict(words=['participant','participants'],label='participate／participant → participants：拿到一份、参与其中',note='部分与拿取的拉丁构词材料形成参与词族，participant 的人物词尾来自分词历史。'),
 'C0167':dict(words=['candidate','candidates'],label='candidus／candidate → candidates：亮白袍与候选身份',note='古代亮白竞选服的名称发展为候选人；更早是发亮、白的词族。'),
 'C0096':dict(words=['audience','audiences'],label='audience → audiences：一群群接收内容的人',note='听的词族发展到听众、观众、读者群体；一群很多人可用单数 audience。'),
 'C1105':dict(words=['supporter','supporters'],label='support → supporter → supporters：托住、支持的一方',note='从下面承载的画面引申为支持人、事业、球队。'),
}
W('citizens','/ˈsɪtɪzənz/','公民；市民〔特定地方语境，复数〕',
 '作为一个国家共同体的正式成员，是 citizen；有些语境也沿用城镇居民的意思。citizens 合起来说这些成员。',
 'citizen + -s，/n/ 后读 /z/。citizen 经盎格鲁法语 citesein、citezein，接法语 cité 城市及更早拉丁 cīvitās、cīvis 公民词族；早期城镇居民义发展到国家公民。',
 [['拉丁 cīvis、cīvitās → 法语 cité 及相关人物词 → citizen','公民共同体、城市 → 城镇成员、国家公民'],['citizen + -s → citizens','多位公民、市民']],
 'citizens of a country 某国公民；senior citizens 老年人；local citizens 当地市民；responsible citizens 有责任感的公民。',
 'rights of citizens；citizens living abroad。','citizens 侧重共同体成员身份，residents 侧重住在某处；两种身份不完全重合。senior citizens 是称呼老年人的常见表达，不一定在强调某人的国籍。',
 ('The museum invited local citizens to share old photographs.','博物馆邀请当地市民分享老照片。'),('The survey included citizens living abroad.','调查包括了居住在国外的公民。'),sources=['https://en.wiktionary.org/wiki/citizens#English','https://en.wiktionary.org/wiki/citizen#English'])
W('residents','/ˈrezɪdənts/','居民；住户；住院医师〔特定职业语境，复数〕',
 '在某个地方持续住下来的人，就是 residents；可以是一座城市的居民，也可以是一栋楼的住户。',
 'resident + -s，/t/ 后读 /s/。resident 经盎格鲁法语等接拉丁 residēns，来自 residēre 留下居住，较早含 re- 与 sedēre 坐、停留。英语现代能与 reside 对应认读。',
 [['拉丁 sedēre、residēre、residēns → 法语等 → resident','坐下停留 → 留居的人'],['resident + -s → residents','一群居民、住户；特定语境的住院医师']],
 'local residents 当地居民；permanent residents 永久居民；residents of the building 楼内住户；medical residents 住院医师。',
 'ask the residents；residents in the area。','residents 强调实际或持续居住的联系，visitors 是来访者。医疗培训语境的 residents 是住院医师，不能只因 resident 有住的历史，就理解为住在医院里的所有人。',
 ('Local residents helped clean the park after the storm.','暴风雨后，当地居民协助清理了公园。'),('The notice asks residents to keep the entrance clear.','通知请住户保持入口畅通。'),sources=['https://en.wiktionary.org/wiki/residents#English','https://en.wiktionary.org/wiki/resident#English'])
W('officials','英 /əˈfɪʃəlz/；美 /əˈfɪʃəlz/','官员；负责人；正式执行职务的人员〔复数〕',
 '在某个组织、机构里承担正式职务、负责处理事情的人，就是 officials；比赛里的执裁、管理人员也可以这样说。',
 'official + -s，/l/ 后读 /z/。official 经法语接拉丁 officiālis，来自 officium 职务、职责；形容词表示职务上的、官方的，名词表示担任职务的人。',
 [['拉丁 officium、officiālis → 法语、英语 official','职责 → 职务上的；履职人员'],['official 名词 + -s → officials','多名官员、负责人或赛事执职人员']],
 'government officials 政府官员；local officials 当地官员；match officials 比赛裁判、执职人员；club officials 俱乐部负责人。',
 'senior officials；officials responsible for transport。','officials 是人；official documents 是正式文件，official 在这里是形容词。officers 也可指正式履职人员，但在军队、警察及具体机构中有自己的称谓习惯。',
 ('Local officials met residents to discuss the new park.','当地官员与居民会面，讨论新公园的事。'),('The match officials inspected the pitch before the game.','比赛执职人员赛前检查了场地。'),sources=['https://en.wiktionary.org/wiki/officials#English','https://en.wiktionary.org/wiki/official#English'])
W('soldiers','英 /ˈsəʊldʒəz/；美 /ˈsoʊldʒərz/','士兵；陆军军人〔复数〕；坚持往前〔soldiers on〕',
 '在军队中服役的人可以叫 soldiers，尤其常说陆军人员；soldiers on 则把继续坚持比作军人接着向前走。',
 'soldier + -s，读 /z/。soldier 经法语 soudier、soudeour 等接中世纪拉丁 soldārius 领军饷的军人，较早联系 soldum、solidus 金币；solidus 又有坚实的性质义。',
 [['拉丁 solidus、soldum → soldārius → 法语 → soldier','金币、军饷 → 领饷服役的人'],['soldier + -s → soldiers；动词 soldier on','多名军人；比喻继续坚持']],
 'young soldiers 年轻士兵；toy soldiers 玩具兵；soldiers on after a setback 遇到挫折仍继续坚持。',
 'soldiers returning home；soldiers on with the task。','soldiers 常说陆军服役者，sailors、airmen 等有各自称呼。soldier on 是动词短语；She soldiers on 中 -s 是第三人称，不是多位士兵。',
 ('The children arranged their toy soldiers in a line.','孩子们把玩具兵排成了一列。'),('Despite the setbacks, she soldiers on with the project.','尽管遇到挫折，她仍坚持推进项目。'),sources=['https://en.wiktionary.org/wiki/soldiers#English','https://en.wiktionary.org/wiki/soldier#English'])
W('owners','英 /ˈəʊnəz/；美 /ˈoʊnərz/','所有者；物主；业主〔owner 的复数〕',
 '一样东西真正归谁拥有，谁就是它的 owner；把多个拥有者合起来说，就是 owners。',
 'owner + -s，读 /z/。owner 有古英语 āgnere、中古英语 ouner 等较早形式；现代能对应 own + -er，但 own 动词和旧词形还涉及派生、逆构等历史，不能把现代拆分当成唯一来源。',
 [['古英语 āgnere → 中古英语 ouner → owner','拥有者'],['现代 own／owner；owner + -s → owners','拥有与拥有者的对应 → 多个物主、业主']],
 'pet owners 宠物主人；home owners 房主；business owners 企业主；the rightful owners 正当所有者。',
 'return items to their owners；owners of the building。','owner 强调拥有，user 强调使用；租住一间房的人可能是住户，拥有房产的人是 owner。一个人可以同时有多种角色，具体由句子说清。',
 ('The lost bags were returned to their owners.','遗失的包已归还给各自的主人。'),('The café owners greeted the regular customers by name.','咖啡馆的店主们叫着名字招呼熟客。'),sources=['https://en.wiktionary.org/wiki/owners#English','https://en.wiktionary.org/wiki/owner#English'])
W('participants','英 /pɑːˈtɪsɪpənts/；美 /pɑːrˈtɪsəpənts/','参与者；参加活动的人〔复数〕',
 '在一件事里拿出自己的一份行动、实际加入其中的人，就是 participants；比赛、课程、调查都可以有参与者。',
 'participant + -s，/t/ 后读 /s/。participant 经法语接拉丁 participāns 正在参与的，较早 participāre、particeps 联系 pars 一份与 capere 拿取。现代可与 participate 的词干、-ant 对应认读。',
 [['拉丁一份、拿取的词族 → participāre、participāns → 法语 → participant','有份参与 → 正在参与的人'],['participant + -s → participants','多个参与活动的人']],
 'course participants 课程学员；study participants 研究参与者；active participants 积极参与者；participants in the discussion 讨论参与者。',
 'all participants；participants from different schools。','participants 强调加入、参与活动；spectators 通常是观看者。study participants 指参与研究的人；participants in 后可接讨论、课程等活动。',
 ('Participants from six schools joined the workshop.','来自六所学校的参与者参加了研习活动。'),('All participants received a copy of the notes.','所有参与者都收到了一份笔记。'),sources=['https://en.wiktionary.org/wiki/participants#English','https://en.wiktionary.org/wiki/participant#English'])
W('candidates','/ˈkændɪdəts/，也常见 /ˈkændɪdeɪts/','候选人；应试者；候选对象〔复数〕',
 '还没有最终定下来，正在被考虑、挑选的人或对象，就是 candidates。这个名字背后有古代竞选者穿亮白袍的具体画面。',
 'candidate + -s，/t/ 后读 /s/。candidate 借拉丁 candidātus，原指穿亮白袍竞选公职的人，接 candidus 亮白的与 candēre 发亮、发白；现代再广用于候选人、考生、可能被选择的对象。',
 [['拉丁 candēre、candidus → candidātus → 英语 candidate','发亮、亮白 → 穿白袍竞选者'],['candidate + -s → candidates','多位候选人、应试者；可选对象']],
 'job candidates 求职候选人；election candidates 参选人；exam candidates 考生；candidates for replacement 可能需要更换的对象。',
 'interview the candidates；shortlist several candidates。','candidates 往往是仍在被考虑的人，applicants 强调递交了申请的人。考试语境的 candidates 通常是考生，不必存在竞选职位。',
 ('The panel interviewed three candidates for the position.','评审小组面试了三位职位候选人。'),('Candidates should write their number at the top of the paper.','考生应在试卷上方写下考号。'),sources=['https://en.wiktionary.org/wiki/candidates#English','https://en.wiktionary.org/wiki/candidate#English'])
W('audiences','/ˈɔːdiənsɪz/〔美音也常见 /ˈɑːdiənsɪz/〕','听众群体；观众群体；读者群体〔复数〕',
 '一场演出、一份内容面对的那一群人，就是一个 audience；不同场次、不同内容或不同人群，可以合起来说 audiences。',
 'audience + -s，/s/ 后增加 /ɪz/。audience 经法语接拉丁 audientia，来自 audīre 听及 audiēns 听着的；由听取、听众发展到观看、阅读内容的群体。',
 [['拉丁 audīre、audiēns、audientia → 法语 → audience','听、听取 → 听众及接收内容的人群'],['audience + -s → audiences','多个观众、听众或读者群体']],
 'young audiences 年轻观众；international audiences 国际观众群体；reach new audiences 接触新的受众；audiences at different performances 不同场次的观众。',
 'appeal to wider audiences；audiences around the world。','一个 audience 可以包含成千上万人；audiences 常在比较不同场次、地区或类型的群体。readers 特指读者，audience 则概括内容所面对的人群。',
 ('The theatre hopes to attract younger audiences.','剧院希望吸引更年轻的观众群体。'),('The book introduced the subject to audiences around the world.','这本书向世界各地的读者群体介绍了这个主题。'),sources=['https://en.wiktionary.org/wiki/audiences#English','https://en.wiktionary.org/wiki/audience#English'])
W('supporters','英 /səˈpɔːtəz/；美 /səˈpɔːrtərz/','支持者；拥护者；球队球迷〔复数〕',
 '用行动、资源、赞同或鼓励帮一方站住的人，就是 supporters；支持球队的一群球迷也常这样称呼。',
 'support + -er → supporter，再加 -s。support 经法语接拉丁 supportāre，历史有 sub- 从下与 portāre 携带、承载，形成从下面托住的画面。人物词在较早英语已有相关形式。',
 [['拉丁 supportāre → 法语、英语 support','从下面承载 → 支撑、支持'],['support → supporter → supporters','提供支持的人 → 多位支持者']],
 'loyal supporters 忠实支持者；football supporters 足球球迷；supporters of the plan 计划支持者；financial supporters 提供资金支持的人。',
 'thank the supporters；supporters from the local community。','supporters 强调支持哪一方；participants 强调参与某活动，两个身份可同时存在。fans 常带喜爱、热情关注的感觉，supporters 也适合事业、主张、团队。',
 ('The players thanked their supporters after the match.','比赛结束后，球员们感谢了支持他们的球迷。'),('Local supporters helped keep the small library open.','当地支持者帮助这家小图书馆继续开放。'),sources=['https://en.wiktionary.org/wiki/supporters#English','https://en.wiktionary.org/wiki/supporter#English'])
def extend_lessons():
 extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_xt',ROOTS,WORDS)
 extend_lessons()
