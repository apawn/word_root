"""Common completed actions and the result states they describe."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'B2735':dict(words=['ban','banned'],label='ban → banned：命令、禁止',note='本族宣告词与北欧同族词交汇，现代禁止义结合语境。'),
 'B3944':dict(words=['hire','hired'],label='hire → hired：付钱取得人的服务或物的使用',note='古英语雇用、租用词延续，人和器物搭配各有习惯。'),
 'B4378':dict(words=['install','installed'],label='install → installed：放到位到安装',note='中世纪拉丁席位词经法语进入英语，就任义和安装义分别发展。'),
 'C1119':dict(words=['print','printed'],label='print → printed：压出印记到印刷',note='拉丁压词经法语，动词有名词转用和较长形式缩短等联系。'),
 'C1454':dict(words=['assume','assumed'],label='assume → assumed：拿到自己这里、先当成真',note='拉丁 ad 与 sumere 结合，承担、采用和假定分支分别理解。'),
 'C1325':dict(words=['observe','observed'],label='observe → observed：留意、守住',note='拉丁看守词经法语借入，遵守和观察均保留。'),
 'C0303':dict(words=['damage','damaged'],label='damage → damaged：损失到损坏',note='法语名词、动词分别借入，共同接拉丁 damnum 损失。'),
 'C0620':dict(words=['reject','rejected'],label='reject → rejected：往回扔到拒收',note='拉丁 re 与 iacere 的组合，英语借入分词词干。'),
 'B4528':dict(words=['threaten','threatened'],label='threaten → threatened：威胁、可能危及',note='本族 threat、动词 en 的关系与古英语旧动词历史并看。'),
 'C1455':dict(words=['surround','surrounded'],label='surround → surrounded：漫过到围住',note='词源接波浪与漫溢，后来受 round 的音义影响。'),
 'C0415':dict(words=['transfer','transferred'],label='transfer → transferred：带到另一处',note='拉丁 trans 与 ferre 结合，动词后重音影响双写 r。'),
 'C0232':dict(words=['conclude','concluded'],label='conclude → concluded：收拢、结束与下结论',note='拉丁关闭词组合，英语结束和判断用途分别看。'),
 'C0278':dict(words=['cross','crossed'],label='cross → crossed：十字交叉到横过',note='十字词经早期借入路线传下，英语后来发展动词。'),
 'B3790':dict(words=['award','awarded'],label='award → awarded：裁定后授予',note='盎格鲁法语考虑、裁定词进入英语，再有奖项名词。'),
 'C0898':dict(words=['operate','operated'],label='operate → operated：工作、运转与操作',note='从 operation 逆构或接拉丁 operatus 的分析均保留。'),
 'C0706':dict(words=['maintain','maintained'],label='maintain → maintained：用手握住到维持',note='拉丁 manu 与 tenere 的组合经法语借入，保持和坚持主张各有用法。'),
}
W('banned','/bænd/','禁止了；被禁的〔过去式、过去分词〕',
 '有人用规则把一道门关上，说这件事不许做、这个东西不许进，就是 banned。范围可以是一场比赛、一个场所或某项活动。',
 'ban 双写 n + -ed → banned，末尾读 /d/。ban 的历史接古英语 bannan 宣告、命令，并有北欧同族 banna 禁止等影响；现代规则禁止义沿这条线理解。',
 [['古英语与北欧宣告、禁止词 → ban','发布命令 → 不许某事发生'],['ban 双写 n + -ed → banned','过去禁止；处于被禁止状态']],
 'banned from entering 被禁止进入；a banned substance 禁用物质；banned the use of... 禁止使用……。',
 'banned in the building 在楼内禁止；banned from the competition 被禁止参赛。','ban somebody from doing 是禁止某人做；banned 不一定永久，时长和范围要看限制本身。它比普通建议不要做更明确。',
 ('The school banned cars from the playground.','学校禁止汽车进入操场。'),('The substance is banned in the competition.','这种物质在该项比赛中禁用。'),sources=['https://en.wiktionary.org/wiki/banned#English','https://en.wiktionary.org/wiki/ban#English'])
W('hired','英 /ˈhaɪəd/；美 /ˈhaɪrd/','雇用了；租用了〔过去式、过去分词〕',
 '付钱，让某个人提供服务，或让自己在一段时间里使用某样东西，是 hired。买下东西和租用东西的关系不同。',
 'hire 去 e + -ed → hired，末尾读 /d/。hire 接古英语 hȳr 工钱、雇用关系与 hȳrian 雇用，名词、动词已有早期形式；现代 hire 再作规则过去变化。',
 [['古英语 hȳr、hȳrian → hire','付费使用服务或物品'],['hire 去 e + -ed → hired','已经雇用、租用；被雇或租来的']],
 'hired a driver 雇了一位司机；hired a car 租了一辆车；newly hired staff 新聘员工。',
 'hired for the summer 暑期雇用；a hired van 租来的小货车。','租器物时 hire 在英式英语很常见，美式常用 rent。hire a person 是雇人，未必是长期全职雇用。',
 ('They hired a guide for the walking tour.','他们为这次徒步游雇了一位向导。'),('We hired a van to move the furniture.','我们租了一辆小货车搬家具。'),sources=['https://en.wiktionary.org/wiki/hired#English','https://en.wiktionary.org/wiki/hire#English'])
W('installed','英 /ɪnˈstɔːld/；美 /ɪnˈstɔːld/','安装了、安置了；使就任〔过去式、过去分词〕',
 '把东西放到需要的位置，并让它能够使用，是 installed 的常见画面。给某人正式安排一个职位，也保留就位的意思。',
 'install + -ed，/l/ 后读 /d/。底词经法语 installer 接中世纪拉丁 installāre，in- 在内 + stallum 席位，后者是日耳曼来源。任职就位义较早，设备和软件义后扩展。',
 [['中世纪拉丁 installāre → 法语 → install','放入席位、使就任 → 安置、安装'],['install + -ed → installed','安装了；已经放置到位或就任']],
 'installed the software 安装了软件；newly installed equipment 新安装的设备；installed as chair 正式就任主席。',
 'installed on a computer 安装在电脑上；installed in the office 安装在办公室。','软件 downloaded 是下载到本机，installed 是完成安装；两个步骤常相连，含义不同。具体介词按设备、位置、职位选。',
 ('She installed the new software on her laptop.','她在笔记本电脑上安装了新软件。'),('The lights were installed above the desks.','灯安装在书桌上方。'),sources=['https://en.wiktionary.org/wiki/installed#English','https://en.wiktionary.org/wiki/install#English'])
W('printed','/ˈprɪntɪd/','印刷了、打印了；印刷的〔过去式、过去分词〕',
 '把字或图像留成看得见的一份，是 printed。传统印刷靠压出印记，现代打印设备换了技术，表达保留下来。',
 'print + -ed，/t/ 后读 /ɪd/。print 名词经古法语 preinte 印记接拉丁 premere 压；动词与名词及较长 emprinten 的缩短相关，不只一条后缀派生线。',
 [['拉丁 premere → 法语印记词 → print','压出的痕迹 → 印刷、打印'],['print + -ed → printed','已经印出；以印刷形式存在']],
 'printed copies 印刷件；printed on paper 印在纸上；printed the tickets 打印了票。',
 'a printed book 纸质印刷书；printed in large letters 以大号字印出。','printed 可以是动作过去形式，也可描述成品状态。the printed word 是印刷文字、出版文字这一类内容的统称。',
 ('I printed two copies of the form.','我打印了两份表格。'),('The instructions are printed on the back of the box.','说明印在盒子背面。'),sources=['https://en.wiktionary.org/wiki/printed#English','https://en.wiktionary.org/wiki/print#English'])
W('assumed','英 /əˈsjuːmd/；美 /əˈsuːmd/','假定了；承担了、采用了〔过去式、过去分词〕；假定的、化用的',
 '把某种东西拿到自己这里，是 assume 的线索：拿来当作事实，是假定；拿来成为自己的任务，是承担；拿来作身份，是采用。',
 'assume 去 e + -ed → assumed，/m/ 后读 /d/。拉丁 ad- 朝向 + sūmere 拿取 → assūmere，d 在 s 前同化；英语较早有承担、揽到自己身上的意思，假定义后来发展。',
 [['拉丁 assūmere → assume','拿到自己这里 → 承担、采用；先当成真'],['assume 去 e + -ed → assumed','过去假定或承担；假定的、采用的']],
 'assumed that... 以为、假定……；assumed responsibility 承担了责任；an assumed name 化名。',
 'assumed to be correct 被假定为正确；assumed control 接管。','assumed 并不表示已经证实。an assumed name 是采用的名字，常是化名；具体是哪一义，看后面接事实、职责还是名字。',
 ('I assumed that the shop was open on Sundays.','我原以为这家商店星期天也开门。'),('She assumed responsibility for the project.','她承担了项目的责任。'),sources=['https://en.wiktionary.org/wiki/assumed#English','https://www.etymonline.com/word/assume'])
W('observed','英 /əbˈzɜːvd/；美 /əbˈzɜːrvd/','观察到、注意到；遵守了；评论道〔过去式、过去分词〕',
 '把一件事认真放在眼前留意，是 observed 的观察义；把规则认真放在行动中守住，则是遵守义。两种用法都带着留意、照看的线索。',
 'observe 去 e + -ed → observed，/v/ 后读 /d/。经古法语 observer 等接拉丁 observāre，ob- 在面前 + servāre 看守；英语早期遵行、守住用途较突出，观察和评论义后来发展。',
 [['拉丁 observāre → 法语 → observe','留意、守住 → 遵守；观察、注意'],['observe 去 e + -ed → observed','已观察到、遵行；发言时指出']],
 'observed the birds 观察了鸟；observed a change 注意到变化；observed the rules 遵守了规则。',
 'observed during the study 研究中观察到的；as she observed 正如她所指出的。','observed a rule 不能译成看着规则；这里是遵守。observed that... 可表示观察发现，也可能是评论指出，按叙述场景判断。',
 ('The students observed the birds from a distance.','学生从远处观察那些鸟。'),('The safety rules were carefully observed.','安全规定得到了认真遵守。'),sources=['https://en.wiktionary.org/wiki/observed#English','https://www.etymonline.com/word/observe'])
W('damaged','/ˈdæmɪdʒd/','损坏了、受损的；损害了〔过去式、过去分词〕',
 '东西还可能在，但原来的完整、功能或价值被伤了一块，就是 damaged。名声、关系和信心也能按这种受损来理解。',
 'damage 去 e + -ed → damaged，/dʒ/ 后接 /d/，不另加 /ɪd/。名词 damage、动词 damagier 等经法语各自影响英语，共同接拉丁 damnum 损失；中间构成有不同分析。',
 [['拉丁 damnum → 法语损失、损害词 → damage','损失 → 使完整性、价值或功能受损'],['damage 去 e + -ed → damaged','过去损害；处于受损状态']],
 'damaged goods 受损货物；damaged the roof 损坏屋顶；damaged trust 损害了信任。',
 'badly damaged 严重受损；damaged during transport 运输中受损。','damaged 是受损，不自动等于完全毁掉、不能修复。damage 作一般损害名词常不可数；赔偿金 damages 是另一常见法律用途。',
 ('Several books were damaged by the water.','几本书被水弄坏了。'),('The argument damaged their friendship.','这场争吵损害了他们的友谊。'),sources=['https://en.wiktionary.org/wiki/damaged#English','https://en.wiktionary.org/wiki/damage#English'])
W('rejected','/rɪˈdʒektɪd/','拒绝了、驳回了；被淘汰的〔过去式、过去分词〕',
 '东西已经送到面前，却被挡回去、不接受，是 rejected。申请、方案、说法、产品，都能成为被拒收或不采纳的对象。',
 'reject + -ed，/t/ 后读 /ɪd/。拉丁 re- 回 + iacere 扔 → reicere，分词 reiectus 的词干进入英语 reject；现代过去变化再加 -ed。',
 [['拉丁 reicere、reiectus → reject','往回扔 → 拒收、不采纳'],['reject + -ed → rejected','已拒绝；被淘汰、未获接纳']],
 'rejected the offer 拒绝提议；rejected an application 驳回申请；rejected goods 不合格退货。',
 'rejected by the committee 被委员会否决；felt rejected 感到不被接纳。','rejected 表示没有被接受，不必附带对象毫无价值的判断。a rejected proposal 是未获采纳的提案，原因还要看具体说明。',
 ('The committee rejected the proposal after a long discussion.','委员会长时间讨论后否决了提案。'),('The factory repaired the rejected items.','工厂修理了被判为不合格的物品。'),sources=['https://en.wiktionary.org/wiki/rejected#English','https://en.wiktionary.org/wiki/reject#English'])
W('threatened','/ˈθretənd/','威胁了；受到威胁的；有发生的危险〔过去式、过去分词〕',
 '坏事还没真的落下来，但已经逼到眼前，是 threatened 的危险感。人可以出言威胁，天气、环境变化也能使某事面临危险。',
 'threaten + -ed，结尾读 /d/。threaten 与 threat 威胁 + 动词 -en 对应，也承接中古英语 thretenen、古英语 þrēatnian 的旧动词，不能全当现代才新造。',
 [['古英语 þrēatnian → 中古英语 → threaten','威胁、使人面临危险'],['threaten + -ed → threatened','过去威胁；处于可能受害的状态']],
 'threatened to leave 威胁说要离开；threatened species 受威胁物种；rain threatened the event 雨使活动有受影响的危险。',
 'felt threatened 感到受威胁；threatened with closure 面临关闭威胁。','threatened 不等于损害已经发生。be threatened with something 说明可能遭遇什么，threatened to do 则常是主语扬言要做什么。',
 ('The storm threatened to delay the flight.','暴风雨可能使航班延误。'),('Several local species are threatened by the loss of habitat.','栖息地丧失正威胁当地几种生物。'),sources=['https://en.wiktionary.org/wiki/threatened#English','https://en.wiktionary.org/wiki/threaten#English'])
W('surrounded','/səˈraʊndɪd/','围住了、被包围的；四周都是〔过去式、过去分词〕',
 '四面都被某种东西占住，就是 surrounded：树围着房子，人围着表演者，也能说身边都是关心自己的人。',
 'surround + -ed，/d/ 后读 /ɪd/。词源接晚期拉丁 superundāre 漫过，super 越过 + undāre 起浪，经法语借入；后来围住义及拼写受到 round 的音义影响。',
 [['晚期拉丁 superundāre → 法语 → surround','漫过、溢出 → 后来四面围住'],['surround + -ed → surrounded','已经围住；处于被四面围绕的状态']],
 'surrounded by trees 四周有树；surrounded by friends 身边围着朋友；surrounded the building 围住建筑。',
 'surrounded on all sides 四面被围；surrounded by hills 四周群山环抱。','现代认形时 round 能帮助记住围一圈，但真实来源接 unda 波浪。surrounded by 通常说明周围是什么；不必一定是敌意包围。',
 ('The house is surrounded by trees.','房子四周都是树。'),('Children surrounded the table to watch the experiment.','孩子们围在桌旁看实验。'),sources=['https://en.wiktionary.org/wiki/surrounded#English','https://www.etymonline.com/word/surround'])
W('transferred','英 /trænsˈfɜːd/；美 /trænsˈfɜːrd/','转移了、转入了；调动了〔过去式、过去分词〕',
 '东西、人或信息从一个位置到了另一个位置，是 transferred。重点是换了所在处，具体可以换账户、单位、设备或交通工具。',
 'transfer 双写 r + -ed → transferred；动词末音节重读，结尾读 /d/。拉丁 trans- 越过、到另一边 + ferre 带 → transferre，英语借入后作规则过去变化。',
 [['拉丁 transferre → transfer 动词','带到另一边 → 转移、调动'],['transfer 双写 r + -ed → transferred','已转移；已换到另一个位置或机构']],
 'transferred the files 转移了文件；transferred to another school 转学了；transferred money 转了钱。',
 'transferred from A to B 从 A 转到 B；transferred to another department 调到另一个部门。','transferred 用动词的后重音。a transfer 作名词常前重音；是否还保留原处那一份，要看是移动、复制还是业务转交的具体过程。',
 ('She transferred the files to a new computer.','她把文件转移到一台新电脑上。'),('He was transferred to another department.','他被调到了另一个部门。'),sources=['https://en.wiktionary.org/wiki/transferred#English','https://en.wiktionary.org/wiki/transfer#English'])
W('concluded','/kənˈkluːdɪd/','结束了；得出结论；缔结了〔过去式、过去分词〕',
 '把一段事情收住，是 concluded 的结束义；把前面考虑过的线索收拢，落到一个判断上，则是得出结论。',
 'conclude + -d，/d/ 后读 /ɪd/。拉丁 con- 一起、加强 + claudere 关 → conclūdere，英语借入这个关闭、收束词族；现代去看它接的是活动、判断还是协议。',
 [['拉丁 conclūdere → conclude','关拢、收住 → 结束；下结论'],['conclude 去 e + -ed → concluded','已经结束、判断出；正式达成协议']],
 'concluded the meeting 结束会议；concluded that... 得出……的结论；concluded an agreement 达成协议。',
 'concluded with a song 以一首歌结束；concluded from the evidence 根据证据判断。','concluded that 引出判断的内容；concluded with 引出结尾用什么。下了结论不代表结论永远正确，依据仍可进一步核对。',
 ('The meeting concluded with a short discussion.','会议以一段简短讨论结束。'),('They concluded that the plan needed more work.','他们得出结论：计划还需要进一步完善。'),sources=['https://en.wiktionary.org/wiki/concluded#English','https://en.wiktionary.org/wiki/conclude#English'])
W('crossed','英 /krɒst/；美 /krɔːst/','穿过了、交叉了；杂交了〔过去式、过去分词〕',
 '一条线从另一条线这边走到那边，会交出一个叉；crossed 的横过、交叉都能抓这个画面。双臂叠在身前，也是 crossed。',
 'cross + -ed，/s/ 后读 /t/。cross 十字词通常追溯拉丁 crux，经古爱尔兰语、古诺尔斯语等早期借入路线进入古英语；英语后来发展横过、交叉的动词。',
 [['拉丁 crux 经早期借入路线 → cross','十字形 → 交叉、从一边到另一边'],['cross + -ed → crossed','已横过、交叉；交叠状态']],
 'crossed the road 过了马路；crossed arms 交叠的双臂；crossed paths 路线相交、偶然相遇。',
 'crossed the bridge 过桥；with her fingers crossed 交叉手指盼好运。','crossed 作动作形式不同于 cross 单独作形容词时的生气。keep your fingers crossed 是祝愿顺利的习惯表达。',
 ('We crossed the bridge before sunset.','我们在日落前过了桥。'),('She stood with her arms crossed.','她双臂交叠站着。'),sources=['https://en.wiktionary.org/wiki/crossed#English','https://en.wiktionary.org/wiki/cross#English'])
W('awarded','英 /əˈwɔːdɪd/；美 /əˈwɔːrdɪd/','授予了、判给了〔过去式、过去分词〕',
 '经过评选或裁定，把奖、合同或款项给到某人，是 awarded。重点在正式决定给谁，而非简单把物品递过去。',
 'award + -ed，/d/ 后读 /ɪd/。award 接盎格鲁法语 awarder 等考虑、裁定词，较早与 warder 看守、观察相关；英语后来发展正式授予和奖项义。',
 [['盎格鲁法语 awarder → award','考虑后裁定 → 决定授予'],['award + -ed → awarded','已授予；经裁定给到某人']],
 'awarded a prize 授予奖项；awarded the contract 授予合同；awarded to the winner 颁给获胜者。',
 'was awarded a medal 被授予奖章；awarded for outstanding work 因出色工作而获颁。','award somebody something 与 award something to somebody 都可以。got an award 更日常，was awarded a prize 更突出正式授予。',
 ('She was awarded a prize for her research.','她因自己的研究获得了一个奖项。'),('The contract was awarded to a local company.','合同授予了当地一家公司。'),sources=['https://en.wiktionary.org/wiki/awarded#English','https://en.wiktionary.org/wiki/award#English'])
W('operated','英 /ˈɒpəreɪtɪd/；美 /ˈɑːpəreɪtɪd/','操作了、运转了；经营了；做了手术〔过去式、过去分词〕',
 '让一套东西工作起来，是 operated 的共同线索：人操作机器，机构经营服务；医生做手术，则是专门的医疗用法。',
 'operate + -d，/t/ 后读 /ɪd/。operate 有从较早 operation 逆构，或接拉丁 operātus 分词词干的分析，共同远接 operārī 工作、做事；过去变化在英语中形成。',
 [['operation 逆构／拉丁 operātus → operate','工作、发挥作用 → 操作、经营等'],['operate 去 e + -ed → operated','过去操作、运转；已施行手术']],
 'operated the machine 操作过机器；operated by the council 由地方议会经营；operated on a patient 为病人做了手术。',
 'operated safely 安全运转；operated in several cities 在几个城市经营。','手术义常用 operate on somebody；operate a machine 是直接操作机器。was operated on 的 on 要跟着手术结构保留。',
 ('The machine operated smoothly throughout the test.','机器在整个测试过程中运转顺畅。'),('The museum was operated by a local charity.','这家博物馆由当地一家慈善机构运营。'),sources=['https://en.wiktionary.org/wiki/operated#English','https://www.etymonline.com/word/operate'])
W('maintained','/meɪnˈteɪnd/','维持了、保养了；坚持声称〔过去式、过去分词〕',
 '把某个状态稳稳握住，让它继续保持，是 maintained。机器要靠保养维持，速度要靠持续行动维持，一种说法也可以被坚持下去。',
 'maintain + -ed，/n/ 后读 /d/。古法语 maintenir、盎格鲁法语 meintenir 接拉丁 manū tenēre 用手握住，manū 用手 + tenēre 握；后来扩展到支持、保存、坚持。',
 [['拉丁 manū tenēre → 法语 → maintain','用手握住 → 支持、维持、保养'],['maintain + -ed → maintained','已经维持、维护；继续坚持某种说法']],
 'maintained the speed 保持速度；well maintained 保养良好；maintained that... 坚持声称……。',
 'maintained contact 保持联系；maintained a steady pace 保持稳定步速。','maintained that 引出的是某人一直坚持的说法，是否属实还需证据。a well maintained building 强调有持续维护，不能只理解成新建。',
 ('She maintained a steady pace throughout the walk.','她在整个步行过程中保持稳定步速。'),('The old building has been carefully maintained.','这栋老建筑一直得到细心维护。'),sources=['https://en.wiktionary.org/wiki/maintained#English','https://en.wiktionary.org/wiki/maintain#English'])
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_zg',ROOTS,WORDS)
 extend_lessons()
