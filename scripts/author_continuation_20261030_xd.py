"""Learning, meetings, users, computers and messages."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'C0289':dict(words=['course','courses'],label='course → courses：跑过的路线、学习路径与菜序',note='course 接拉丁 currere 跑的 cursus 路程、路线，经法语 cours 借入；courses 也可作流过等动词形式。'),
 'C0659':dict(words=['lesson','lessons'],label='lesson → lessons：阅读到教学内容、经验教训',note='lesson 经法语 leçon 接拉丁 lēctiō 阅读，与学习和教授的内容相连；现代复数直接加 s。'),
 'B2895':dict(words=['meet','meeting','meetings'],label='meet → meeting → meetings：相遇到聚会、会议',note='meeting 的名词已有古英语相应形式，不只是在现代把 meet 加 -ing 临时造出，meetings 数不同聚会、会议。'),
 'C1594':dict(words=['use','user','users'],label='use → user → users：谁在使用',note='use 的动词 /z/ 保留到 user、users，人物后缀 -er；英语自身派生与现代复数分别看。'),
 'C1174':dict(words=['compute','computer','computers'],label='compute → computer → computers：计算的人到机器',note='computer 原来可指从事计算的人，后来电子计算设备义常用，-er 不只表示人。'),
 'C0751':dict(words=['message','messages'],label='message → messages：送出去的信息',note='message 经法语接中古拉丁 missaticum，远接 mittere 送；messages 在 /dʒ/ 后加 /ɪz/。'),
}
W('courses','英 /ˈkɔːsɪz/；美 /ˈkɔːrsɪz/','课程；路线、进程；一道道菜；疗程等；流过、奔流〔动词形式〕',
 '按一条安排往前走，是 course 的好记画面：学习走一门课程，行动走一条路线，用餐按顺序上一道道菜。',
 'course 已有 e，加 s，/s/ 后增加 /ɪz/。拉丁 currere 跑形成 cursus 跑程、路线，经古法语 cours 传入英语；多种现代义有各自使用史。',
 [['拉丁 currere → cursus → 古法语 cours → course','跑、跑程、路线 → 进程等'],['course 名词、动词 + -s → courses','多门课程、多道菜等；单数主语流过']],
 'language courses 语言课程；main courses 主菜；three courses 三道菜；courses of action 行动方案；water courses through ... 水流经……。',
 'attend courses；courses offered by the college。','courses 常数系统安排的课程，lessons 常数其中的一次教学或一课。three courses 在餐厅通常是三道菜，具体是哪种进程由场景决定。',
 ('The college offers evening courses in several languages.','这所学院提供几种语言的夜间课程。'),('Dinner consisted of three courses.','晚餐分三道菜。'),sources=['https://en.wiktionary.org/wiki/courses#English','https://en.wiktionary.org/wiki/course#English'])
W('lessons','/ˈlesənz/','课、课程中的单元；经验教训；lesson 的复数',
 '一次要教、要学的内容是 lesson；经历过一件事以后学到的东西，也叫 lesson。lessons 可以发生在教室，也可以来自生活。',
 'lesson + -s，/n/ 后读 /z/。经古法语 leçon 接拉丁 lēctiō 阅读，和 legere 阅读的 lect- 形式相连；和 lection 是不同借入路线的同源词。',
 [['拉丁 legere／lectio → 古法语 leçon → lesson','阅读、诵读 → 教授、学习的内容'],['lesson + -s → lessons','多次课、学习单元；多项经验教训']],
 'piano lessons 钢琴课；driving lessons 驾驶课；lessons from experience 经验教训；learn lessons 吸取教训。',
 'weekly lessons；lessons we learned。','a course 常是一门系统课程，其中可有 many lessons。lessons learned 可以概括从项目、经历里得到的经验，并不一定指受到了惩罚。',
 ('She takes piano lessons on Saturday mornings.','她周六上午上钢琴课。'),('We wrote down the lessons we learned from the first event.','我们记下了从第一次活动中得到的经验教训。'),sources=['https://en.wiktionary.org/wiki/lessons#English','https://en.wiktionary.org/wiki/lesson#English'])
W('meetings','/ˈmiːtɪŋz/','会议、会面；聚会；meeting 的复数',
 '人们在同一处或同一通话里聚到一起，是 meetings。可以是正式讨论，也可以是约好见面，具体形式靠修饰语说明。',
 'meeting + -s，/ŋ/ 后读 /z/，不加 /ɡ/。meeting 对应 meet + -ing 的相遇名词，古英语已有 meting、gemeting 等相应形式，经中古英语延续。',
 [['古英语 mēting／ġemēting 等 → 中古英语 meeting → meeting','会面、聚集；与 meet 相连'],['meeting + -s → meetings','多场会议、会面、聚会']],
 'team meetings 团队会议；online meetings 线上会议；regular meetings 定期会议；meetings with clients 与客户的会面。',
 'attend meetings；several short meetings。','meetings 可以线上举行，不限定必须身体到同一间屋。meeting 作为一次安排可数；meeting people 在动作结构里则可能是在见人、结识人。',
 ('We keep the weekly meetings short and focused.','我们让每周会议尽量简短、集中。'),('The project began with several meetings between the two teams.','项目从两个团队之间的几次会面开始。'),sources=['https://en.wiktionary.org/wiki/meetings#English','https://en.wiktionary.org/wiki/meeting#English'])
W('users','英 /ˈjuːzəz/；美 /ˈjuːzərz/','使用者、用户；user 的复数',
 '谁在实际使用工具、道路、服务或系统，谁就是 users。它不只说付钱的人，也不只说电脑用户。',
 'user + -s，词尾 /z/。user 是英语动词 use /juːz/ 加 -er 的人物名词，动词的 /z/ 保留到 user 和 users。',
 [['英语 use 动词 + -er → user','使用 → 使用者'],['user + -s → users','多位用户、使用者']],
 'computer users 电脑用户；road users 道路使用者；new users 新用户；users of the service 服务使用者。',
 'users with different needs；regular users。','users 强调使用，customers 强调购买、消费的关系。一个人可以同时是两者，也可能只使用别人购买的服务。名词 use /juːs/ 与 users 里的 /z/ 要分开。',
 ('The guide is written for users with no previous experience.','这份指南是为没有使用经验的用户编写的。'),('The new path is shared by cyclists and other road users.','这条新路由骑车人和其他道路使用者共同使用。'),sources=['https://en.wiktionary.org/wiki/users#English','https://en.wiktionary.org/wiki/user#English'])
W('computers','英 /kəmˈpjuːtəz/；美 /kəmˈpjuːtərz/','计算机、电脑；历史上也指从事计算的人；computer 的复数',
 'compute 是算，computer 最初能说负责算数的人，后来最常用来指按程序处理信息的机器。computers 就数这些机器。',
 'computer + -s，词尾 /z/。computer 是英语 compute 加 -er 的施事、工具名词；compute 更早经法语、拉丁 computare 计算词族，-er 的机器义后来常见。',
 [['英语 compute + -er → computer','计算的人；后来指执行计算、处理信息的机器'],['computer + -s → computers','多台计算机；历史语境也可指多位计算者']],
 'desktop computers 台式电脑；laptop computers 笔记本电脑；school computers 学校电脑；computers on the network 网络里的计算机。',
 'use computers；two older computers。','computer 的 -er 可表工具，不只表人；现代说 users 常是使用计算机的人，computers 通常是被使用的设备。历史文献中的人物义要另看年代、背景。',
 ('The library has several computers for visitors to use.','图书馆有几台供访客使用的电脑。'),('The two computers share a printer.','这两台电脑共用一台打印机。'),sources=['https://en.wiktionary.org/wiki/computers#English','https://en.wiktionary.org/wiki/computer#English'])
W('messages','/ˈmesɪdʒɪz/','消息、口信；信息、主旨；发消息〔message 的第三人称单数〕',
 '把要告诉别人的内容送过去，是 messages。手机里是一条条消息，文章、作品里又可以说它想传达的核心意思。',
 'message 已有 e，加 s；原词 /dʒ/ 后增加 /ɪz/。经古法语 message 接中古拉丁 missaticum，远源关联 mittere 送出；英语动词由名词发展。',
 [['拉丁 mittere 词族 → 中古拉丁 missaticum → 古法语 message → 英语 message','送出、传达 → 送出去的内容'],['message 名词、动词 + -s → messages','多条消息、传达的意思；单数主语发消息']],
 'text messages 短信、文字消息；leave messages 留言；messages of support 支持的话语；messages someone 给某人发消息。',
 'read the messages；messages from a friend。','messages 是传达的内容，notifications 常是提醒有新情况的通知；一条通知可以提醒有一条新消息，但两者不必是同一个东西。',
 ('I read your messages after the meeting ended.','会议结束后，我看了你的消息。'),('She messages the group whenever the timetable changes.','时间表一变，她就给群里发消息。'),sources=['https://en.wiktionary.org/wiki/messages#English','https://en.wiktionary.org/wiki/message#English'])
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_xd',ROOTS,WORDS)
 extend_lessons()
