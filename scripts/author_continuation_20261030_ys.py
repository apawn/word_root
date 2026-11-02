"""Practical vocabulary for work, systems, records and public life."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'C0401':dict(words=['office','offices'],label='office → offices：职务、办公地点与办事机构',note='拉丁职务、工作材料借入，工作内容与开展工作的地方逐渐分化。'),
 'B2955':dict(words=['payment','payments'],label='payment → payments：付款与一笔笔款项',note='法语付款名词借入，现代对应 pay 与 ment。'),
 'C1297':dict(words=['session','sessions'],label='session → sessions：坐下来的一段活动与会话',note='拉丁坐的词族发展为一段会议、活动，计算机有特定会话义。'),
 'C1158':dict(words=['symptom','symptoms'],label='symptom → symptoms：伴随显出的迹象',note='希腊共同发生、碰到的词族，经拉丁借入，后有一般迹象义。'),
 'B3923':dict(words=['limit','limits'],label='limit → limits：边界与限制',note='拉丁边界名词与划界动词各有借入路径，现代形式重合。'),
 'C0706':dict(words=['manager','managers'],label='manager → managers：管理、负责的人',note='英语 manage 加 er 命名执行管理动作的人，manage 的较早词族有手的背景。'),
 'C0423':dict(words=['file','files'],label='file → files：文档、队列；锉刀另源',note='线与串联文书的借词背景形成存档等意义，锉刀支来自本族。'),
 'C0684':dict(words=['location','locations'],label='location → locations：放置与所在地点',note='拉丁放置词形成名词借入，现代也用于拍摄地点。'),
 'C0238':dict(words=['client','clients'],label='client → clients：受庇护者、客户与客户端',note='cliens 是可靠的拉丁近源；联系倾斜、依靠只是更早词源的一种分析，另有 cluens、clueo 路线。'),
 'C1209':dict(words=['director','directors'],label='director → directors：指引工作的人',note='直引、指挥的词族经法语、拉丁形成不同专业称谓。'),
 'C0507':dict(words=['government','governments'],label='government → governments：掌舵、治理与政府',note='法语治理名词借入，较早接拉丁、希腊掌舵词族。'),
 'B2778':dict(words=['loss','losses'],label='loss → losses：失去、损失与落败',note='本族失去词延续，可数事件与不可数总体分开。'),
 'C0271':dict(words=['increase','increases'],label='increase → increases：增长及名动词重音',note='拉丁生长词族经法语进入英语，名词与动词的重音帮助识别。'),
 'C1660':dict(words=['voter','voters'],label='voter → voters：投票的人',note='现代 vote 去 e 加 er，再用 s 形成复数。'),
}
W('offices','英 /ˈɒfɪsɪz/；美 /ˈɑːfɪsɪz/','办公室；办事处、部门；职务〔office 的复数〕',
 '人处理公务、业务的地方，是 offices 的办公室义；组织的办事机构也可以这样说。它的老名字先与职责、工作有关，再转向工作地点。',
 'office + -s，/s/ 后增加 /ɪz/。拉丁 officium 职责、服务是 opificium 的缩短形式，含 opus 工作与 facere 做的材料；经法语借入英语。',
 [['拉丁 opificium、officium → 法语 → office','工作、职务 → 公务、工作地点'],['office + -s → offices','多个办公室、办事处或职务']],
 'regional offices 地区办事处；head offices 总部；offices on the second floor 二层的办公室。',
 'offices open to visitors；offices held by different people。','offices 可以数房间，也能数机构、职务。hold office 常说担任公职；different offices 在某些组织说明里则是不同职位。',
 ('The company has offices in three cities.','这家公司在三个城市设有办事处。'),('The offices on this floor are shared by two teams.','这一层的办公室由两个团队共用。'),sources=['https://en.wiktionary.org/wiki/offices#English','https://en.wiktionary.org/wiki/office#English'])
W('payments','/ˈpeɪmənts/','付款；一笔笔支付的款项〔payment 的复数〕',
 '把该付的钱交出去，是 payment；分几次、付几笔，就能数成 payments，既可关注付款行为，也可关注金额项目。',
 'payment + -s，/t/ 后读 /s/。payment 经古法语 paiement 借入，现代对应 pay + -ment；pay 的较早背景经法语接拉丁 pacāre 使平静、满足。',
 [['拉丁 pacāre → 法语支付词及 paiement → payment','使满足 → 付钱、付款'],['payment + -s → payments','多次付款、多笔款项']],
 'monthly payments 每月付款；card payments 刷卡付款；make payments 付款；payments received 已收到款项。',
 'payments recorded in the system；payments made each month。','payment 泛说付款可不可数，payments 把几笔或几次分开。a payment of... 后面说明金额；payment for... 后面说明付的是什么。',
 ('The office records all payments in the same system.','办公室在同一个系统里记录全部款项。'),('The customer made three separate payments.','这位顾客分三笔付款。'),sources=['https://en.wiktionary.org/wiki/payments#English','https://en.wiktionary.org/wiki/payment#English','https://en.wiktionary.org/wiki/pay#English'])
W('sessions','/ˈseʃənz/','一段会议、活动、训练；会话〔session 的复数〕',
 '大家坐下来专门做一件事的一段时间，是 sessions；会议、练习、录音都可分成一场场，计算机也把一段持续交互称为会话。',
 'session + -s，/n/ 后读 /z/。拉丁 sessiō 坐下、就坐的集会，经法语、中古英语借入；sess- 与 sedēre 坐同族，后来按各类持续活动扩展。',
 [['拉丁 sedēre、sessiō → 法语 → session','坐下、集会 → 一段专门活动'],['session + -s → sessions；技术用法扩展','多场活动；多段计算机会话']],
 'training sessions 培训场次；recording sessions 录音场次；practice sessions 练习时段；user sessions 用户会话。',
 'sessions lasting an hour；sessions recorded by the system。','session 关注一次连续活动的时段。meeting 通常是人与人的会议；session 范围更广，一次练习或系统交互也可用。',
 ('The course includes six practice sessions.','这门课包含六次练习。'),('The system records how long user sessions last.','系统记录用户会话持续多久。'),sources=['https://en.wiktionary.org/wiki/sessions#English','https://en.wiktionary.org/wiki/session#English'])
W('symptoms','/ˈsɪmptəmz/','症状；显出的迹象〔symptom 的复数〕',
 '内部有某种情况，外面伴随显出一些表现，是 symptoms。身体语境说症状，系统、组织语境也能借指深层问题的迹象。',
 'symptom + -s，/m/ 后读 /z/。希腊 syn- 一起在 p 前成 sym-，与 piptein 落下形成 sympiptein 发生、碰到，再有 symptōma；经拉丁、中古英语借入，后重新调整拼写。',
 [['希腊 sympiptein、symptōma → 拉丁 → 较早英语','共同发生、碰到 → 事件、疾病表现'],['古典化拼写 symptom + -s → symptoms','多个症状；一般事物显出的迹象']],
 'main symptoms 主要症状；symptoms observed 观察到的症状；symptoms of a deeper problem 深层问题的迹象。',
 'symptoms listed in the report；symptoms of poor organisation。','symptoms of... 交代这些表现指向什么情况。一般比喻阅读中，它常是在说表面问题背后还有更深层原因。',
 ('The report lists the symptoms observed during the study.','报告列出了研究中观察到的症状。'),('The repeated delays are symptoms of a deeper problem.','反复延误是更深层问题显出的迹象。'),sources=['https://en.wiktionary.org/wiki/symptoms#English','https://www.etymonline.com/word/symptom'])
W('limits','/ˈlɪmɪts/','界限、限度〔复数〕；限制〔第三人称单数〕',
 '事情能到哪里、再往外就超出了范围，这条边是 limits；把范围压在边线以内，动词也用 limits。',
 'limit + -s，/t/ 后读 /s/。名词经法语接拉丁 līmes、līmit- 边界；动词也有拉丁 līmitāre、法语 limiter 的借入路线，现代两类形式合用。',
 [['拉丁边界名词及划界动词 → 法语 → limit','边界、范围 → 限度、划定范围'],['limit + -s → limits','多个界限；单数主语限制']],
 'time limits 时限；within the limits 在限度内；limits the number 限制数量；know your limits 了解自己的限度。',
 'limits set for the task；limits access to the room。','limits 可以是实际边界，也可说能力、数量等上限。The rule limits... 是规则在限制，The limits are... 则是名词界限。',
 ('The task has clear time limits.','这项任务有明确的时间限制。'),('The design limits the amount of water used.','这种设计限制了用水量。'),sources=['https://en.wiktionary.org/wiki/limits#English','https://en.wiktionary.org/wiki/limit#English'])
W('managers','英 /ˈmænɪdʒəz/；美 /ˈmænɪdʒərz/','经理、管理者；管理程序〔manager 的复数〕',
 '负责把人员、资源、事情安排好的人，是 managers；软件里负责管理文件、任务的组件，也借用管理者这个名称。',
 'manage 去末尾 e 加 -er → manager，再加 -s，词尾读 /z/。manage 经意大利语、法语相关驾驭处理词，较早接拉丁 manus 手的材料；现代 er 在英语命名执行动作的人。',
 [['手、驾驭处理词族 → manage + -er → manager','把事情安排运行的人'],['manager + -s → managers；软件用途扩展','多位管理者；管理某类资源的程序']],
 'project managers 项目经理；store managers 店长；file managers 文件管理程序。',
 'managers from different teams；managers responsible for the project。','manager 的范围由前面修饰词说明：店铺、项目、体育队伍都能有经理或管理者。file managers 的管理者是软件，按资源管理功能理解。',
 ('The project managers met to compare their plans.','项目经理们开会比较各自的计划。'),('Different file managers organise folders in different ways.','不同文件管理程序用不同方式组织文件夹。'),sources=['https://en.wiktionary.org/wiki/managers#English','https://en.wiktionary.org/wiki/manager#English','https://en.wiktionary.org/wiki/manage#English'])
W('files','/faɪlz/','文件、档案；队列；锉刀〔复数，分支不同〕；归档、提交等〔第三人称单数〕',
 '一份份整理好的记录，是 files；电脑把可保存、读取的一份数据也叫 file。排成一线的人、工具中的锉刀，也会出现同形 files，各走自己的分支。',
 'file + -s，/l/ 后读 /z/。文档与队列支经法语接拉丁 fīlum 线，旧时把文书穿在线上保存；锉刀名接古英语 fēol，锉磨动词接 fīlian。',
 [['拉丁 fīlum → 法语 → file 的记录、队列支','线、串联文书 → 档案与排列成线'],['另一支古英语锉刀、锉磨词 → file；加 -s → files','多份记录、多把锉刀；单数主语存档、锉磨等']],
 'open files 打开文件；paper files 纸质档案；files a report 提交报告；metal files 金属锉。',
 'files stored on the server；files arranged by date。','files 可以是实体文书，也可以是数字数据。filed 是过去形式，files 作动词则接单数主语，说当前习惯或行为。',
 ('The files are stored on the shared drive.','这些文件存放在共享驱动器上。'),('She files the reports by date.','她按日期把报告归档。'),sources=['https://en.wiktionary.org/wiki/files#English','https://www.etymonline.com/word/file'])
W('locations','/ləʊˈkeɪʃənz/；美式常 /loʊˈkeɪʃənz/','位置、地点；拍摄地点〔location 的复数〕',
 '把地图上的一个点、商店所在的位置或拍电影选中的地方标出来，就是 locations；重点是东西具体在哪里。',
 'location + -s，/n/ 后读 /z/。名词接拉丁 locātiō，由 locāre 放置、出租形成，联系 locus 地方；现代与 locate 对应，但名词有自己的借入历史。',
 [['拉丁 locus、locāre → locātiō → location','地方、放置 → 所在位置、地点'],['location + -s → locations','多个位置；特别用途的地点']],
 'store locations 门店地点；filming locations 拍摄地；locations marked on a map 地图上标出的位置。',
 'locations near the station；locations chosen for the film。','location 通常关注实际所在的地方；position 也能说位置，还常延伸到姿态、立场、职位。filming locations 是实地拍摄选用的场所。',
 ('The map shows all the store locations.','地图标出了所有门店的地点。'),('They visited several possible filming locations.','他们考察了几个可能的拍摄地。'),sources=['https://en.wiktionary.org/wiki/locations#English','https://en.wiktionary.org/wiki/location#English'])
W('clients','/ˈklaɪənts/','客户、委托人；客户端程序或设备〔client 的复数〕',
 '把某件专业事务委托给别人处理的一方，是 clients；计算机里，向服务器提出请求、接受服务的程序或设备，也用这个服务关系来命名。',
 'client + -s，/t/ 后读 /s/。经法语接拉丁 cliēns、client- 跟随者、受庇护者；更早有联系倾斜、依靠的分析，也有 cluēns、clueō 的分析，不能只认定一种。',
 [['拉丁 cliēns → 法语 → client','受庇护者 → 接受专业服务、委托事务的一方'],['client + -s → clients；计算机用途','多个客户；请求服务的程序或设备']],
 'meet clients 会见客户；clients of the firm 公司的客户；email clients 邮件客户端；clients connected to a server 连接服务器的客户端。',
 'clients waiting in reception；clients requesting information。','customer 与 client 的范围会重叠，client 常用于专业、持续服务关系。技术语境的 clients 可以全是程序，不能因为是客户词就只想成人。',
 ('The designer meets new clients on Mondays.','设计师每周一会见新客户。'),('Several clients connect to the same server.','几个客户端连接同一台服务器。'),sources=['https://en.wiktionary.org/wiki/clients#English','https://www.etymonline.com/word/client','https://en.wiktionary.org/wiki/cliens#Latin'])
W('directors','英 /dəˈrektəz/、/daɪˈrektəz/；美 /dəˈrektərz/、/daɪˈrektərz/','董事；主管；导演〔director 的复数〕',
 '决定事情往哪个方向走、带着工作运行的人，是 directors 的共同画面。公司里可说董事、主管，电影里则是导演。',
 'director + -s，词尾读 /z/。经法语 directeur、directour 及后期拉丁 director 等借入，接 dirigere 指引、拉直的 direct- 词干；现代可认 direct + -or。',
 [['拉丁 dirigere、direct- → director；法语相关形式','指引方向、指挥 → 负责引导工作的人'],['director + -s → directors','多位董事、主管或导演']],
 'film directors 电影导演；company directors 公司董事；a board of directors 董事会。',
 'directors meeting in the boardroom；directors discussing their films。','director 的具体头衔按行业判断。board of directors 是董事会，film directors 是拍摄电影时负责总体创作指挥的人。',
 ('The directors met to discuss the company’s plans.','董事们开会讨论公司的计划。'),('The festival invited directors from several countries.','电影节邀请了几国的导演。'),sources=['https://en.wiktionary.org/wiki/directors#English','https://en.wiktionary.org/wiki/director#English'])
W('governments','英 /ˈɡʌvənmənts/；美 /ˈɡʌvərnmənts/','政府；执政班子〔government 的复数〕',
 '负责治理一个国家或地区的组织，是 governments。更早的词族有掌舵、引导船前进的画面，后来用于管理公共事务。',
 'government + -s，/t/ 后读 /s/。government 借自古法语 governement，接 governer 治理；较早经拉丁 gubernāre 追到希腊 kybernân 掌舵。现代 govern + -ment 对应易记，但借词历史在前。',
 [['希腊掌舵词 → 拉丁 gubernāre → 法语 governer、governement','引导船 → 治理；治理的组织'],['government + -s → governments','不同国家、地区或时期的政府']],
 'local governments 地方政府；national governments 国家政府；governments working together 政府间合作。',
 'governments in different regions；governments sharing information。','government 可指治理组织，也可按具体时期说某届政府；state、country 则常指国家的其他层面，读文章时看是在说哪一个主体。',
 ('Local governments shared information after the storm.','暴风雨后，各地方政府共享了信息。'),('Several governments supported the cultural exchange.','几国政府支持了这次文化交流。'),sources=['https://en.wiktionary.org/wiki/governments#English','https://en.wiktionary.org/wiki/government#English'])
W('losses','英 /ˈlɒsɪz/；美 /ˈlɔːsɪz/、/ˈlɑːsɪz/','损失；失去的事物；落败次数〔loss 的复数〕',
 '钱、物品、机会或比赛结果比原来少了、失去了，就有 losses；它可以按具体损失项目，也可以按输掉几次来数。',
 'loss + -es，/s/ 后增加 /ɪz/。loss 接古英语 los 失去、损害，与 lose 的较早词族相连；现代不是直接给 lose 加一个 ss。',
 [['古英语 los、相关失去词族 → loss','失去、损害 → 损失、落败'],['loss + -es → losses','多项损失；多次败绩']],
 'heavy losses 严重损失；crop losses 作物损失；wins and losses 胜负记录。',
 'losses caused by the storm；losses during the season。','losses 不限金钱，农作物、物件、比赛都能用。the loss of something 还可以用单数把某一次失去整体框起来。',
 ('The storm caused serious crop losses.','暴风雨造成了严重的作物损失。'),('The table shows each team’s wins and losses.','表格展示了各队的胜负记录。'),sources=['https://en.wiktionary.org/wiki/losses#English','https://en.wiktionary.org/wiki/loss#English'])
W('increases','名词 /ˈɪnkriːsɪz/；动词 /ɪnˈkriːsɪz/','增长、增加量〔复数〕；增加、使增加〔第三人称单数〕',
 '数量、大小、程度比原来多了，就是 increases；数一笔笔增长量时是名词，说某样东西变多时是动词，两者重音常不同。',
 'increase + -s，/s/ 后增加 /ɪz/。拉丁 in- 与 crēscere 生长组成 incrēscere，经法语进入英语；现代名词常前重音、动词常后重音。',
 [['拉丁 incrēscere → 法语 → increase','生长、变多 → 增加'],['increase + -s → increases','多项增幅；单数主语增加，重音随词性']],
 'increases in demand 需求增长；increases the speed 提高速度；increases by... 增加了……；increases to... 增至……。',
 'increases recorded each year；the number increases slowly。','increases by 说明增加多少，increases to 说明最后达到多少。The report shows increases 是名词；The number increases 是动词。',
 ('The chart shows increases in demand over five years.','图表展示了五年间的需求增长。'),('The number of visitors increases in summer.','夏季游客人数增加。'),sources=['https://en.wiktionary.org/wiki/increases#English','https://en.wiktionary.org/wiki/increase#English'])
W('voters','英 /ˈvəʊtəz/；美 /ˈvoʊtərz/','投票者、选民〔voter 的复数〕',
 '参与投票、用一票表达选择的人，是 voters。这个词把注意放在投票者身上，和候选人 candidates 分清角色。',
 'vote 去不发音 e，加 -er → voter，再加 -s，词尾读 /z/。vote 的较早词族经拉丁 vōtum 誓愿与法语等发展；英语 er 命名投票的人。',
 [['vote + -er → voter','投票动作 → 投票的人'],['voter + -s → voters','多位投票者、选民']],
 'registered voters 登记选民；young voters 年轻选民；voters in the district 该地区选民。',
 'voters arriving at the hall；voters choosing a representative。','voters 是投票一方，candidates 是争取被选中的一方；一个人在不同情境也可同时具有两种身份。votes 数的是票或投票动作，voters 数的是人。',
 ('Voters arrived at the hall throughout the morning.','整个上午都有投票者来到大厅。'),('The survey asked voters about local issues.','这项调查询问选民对当地议题的看法。'),sources=['https://en.wiktionary.org/wiki/voters#English','https://en.wiktionary.org/wiki/voter#English','https://en.wiktionary.org/wiki/vote#English'])
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_ys',ROOTS,WORDS)
 extend_lessons()
