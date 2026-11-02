"""Frequent actions: making, arranging, selecting and handling things."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'C0351':dict(words=['produce','producing'],label='produce → producing：把成果带出来',note='拉丁向前带领的词族，扩展到生产、创作与拿出。'),
 'B4170':dict(words=['schedule','scheduled'],label='schedule → scheduled：清单到排定日程',note='纸片、清单发展为日程，名词再转动词。'),
 'B3757':dict(words=['pick','picking'],label='pick → picking：挑出、摘取',note='本族挑、啄、刺相关旧词，不把远源猜测写成定论。'),
 'C0986':dict(words=['push','pushed','pushing'],label='push → pushed → pushing：向前施力',note='拉丁击打、推动词经法语借入，现代常说推、催促、推进。'),
 'B2738':dict(words=['beat','beating'],label='beat → beating：击打、打败与节拍',note='本族强变化动词；beating 还可作动作或节律名词。'),
 'C1072':dict(words=['employ','employed'],label='employ → employed：投入使用到雇用',note='拉丁卷入词经法语形成使用、雇用义。'),
 'B3465':dict(words=['enjoy','enjoying'],label='enjoy → enjoying：感到愉快；享有好处',note='法语快乐词族借入，享有权利等用法另结合搭配理解。'),
 'B4162':dict(words=['enter','entering'],label='enter → entering：进到某个范围',note='拉丁里面词族经法语借入，可进入地点、阶段、比赛或记录。'),
 'B3390':dict(words=['land','landing'],label='land → landing：陆地、落地与着陆点',note='本族陆地词与动词用途相连，楼梯平台按落脚处理解。'),
 'C0706':dict(words=['manage','managing'],label='manage → managing：操持、办成',note='手、操控马匹的意象扩展到处理事务和设法完成。'),
 'B3030':dict(words=['clean','cleaning'],label='clean → cleaning：让脏东西离开',note='本族干净词，动词表达使干净。'),
 'B3002':dict(words=['throw','throwing'],label='throw → throwing：扭转旧义到投掷',note='古英语转、扭的动词延续，投掷成为现代中心用途。'),
 'B4205':dict(words=['improve','improving'],label='improve → improving：从收益到变好',note='盎格鲁法语产生收益的词发展成改善，并受 prove 类拼写影响。'),
 'C1488':dict(words=['attempt','attempted'],label='attempt → attempted：着手试着做',note='拉丁尝试词经法语借入，尝试不承诺成功。'),
}
W('producing','英 /prəˈdjuːsɪŋ/；美 /prəˈduːsɪŋ/','生产、创作、产生；拿出〔现在分词、动名词〕',
 '把原先没有摆在面前的东西带出来：工厂做出产品，作家写出作品，措施带来结果，都可以是 producing。',
 'produce 去词尾不发音的 e，加 -ing。底词接拉丁 prō- 向前、向外 + dūcere 带领 → prōdūcere 带出来，经法语等进入英语。',
 [['拉丁 prōdūcere → 英语 produce','带出、呈现 → 生产、产生、拿出'],['produce 去 e + -ing → producing','正在生产；把生产这件事作一个过程谈']],
 '生产不限于工厂制造：producing a report 是写出报告，producing results 是产生效果；producing a ticket 是把票拿出来。',
 'producing electricity 发电；producing clear results 产生明确效果。','这里用动词 produce 的后重音；名词 produce 农产品常是前重音。producing something 强调做出或拿出什么。',
 ('The farm is producing more food with less water.','这个农场正在用更少的水生产更多食物。'),('The new approach is producing better results.','新方法正在带来更好的结果。'),sources=['https://en.wiktionary.org/wiki/producing#English','https://en.wiktionary.org/wiki/produce#English'])
W('scheduled','英 /ˈʃedjuːld/；美 /ˈskedʒuːld/','已安排的、预定的；安排了〔过去式、过去分词〕',
 '一件事已经被放进时间表，在某个时间格子里有了位置，就是 scheduled。',
 'schedule + -d，结尾 /l/ 后读 /d/。schedule 经法语接晚期拉丁 schedula 小纸片，较早接希腊撕开、碎片词族；纸上的清单发展为日程，再有安排的动词。',
 [['希腊、拉丁纸片词 → 法语 → schedule','写字的纸片 → 清单、时间表'],['名词 schedule → 动词；加 -d → scheduled','把事情排入表中 → 已排定']],
 'scheduled for Friday 是定在周五；scheduled to begin 是预定开始。它说明安排，事情是否实际发生还要看后文。',
 'a scheduled meeting 预定的会议；arrive as scheduled 按预定时间到达。','schedule 的英式 /ʃ/ 与美式 /sk/ 都常见。scheduled 后的 -d 不另读一整个 /ɪd/ 音节。',
 ('The meeting is scheduled for Friday morning.','会议定在周五上午。'),('They scheduled the repairs for next week.','他们把维修安排在下周。'),sources=['https://en.wiktionary.org/wiki/scheduled#English','https://www.etymonline.com/word/schedule'])
W('picking','/ˈpɪkɪŋ/','挑选、采摘、捡取；拨奏〔现在分词、动名词〕',
 '从一堆或一片东西里，把某一个挑出来、摘下来，是 picking 的共同画面。手指拨动琴弦时，也在做细小、分开的动作。',
 'pick + -ing → picking，末尾已有 ck，不再补一个 k。pick 接中古英语挑、啄、刺等相关旧形式，与日耳曼邻近词有联系，更远来源不强作定论。',
 [['中古英语 pick 等旧形式 → pick','细小的挑、啄、刺动作 → 挑选、摘取等'],['pick + -ing → picking','正在挑、摘；挑选或采摘的过程']],
 'picking apples 摘苹果；picking a team 挑选队伍成员。picking up 可以捡起，也可接人，要把 up 一起读。',
 'picking a suitable date 选合适的日子；picking up a parcel 取包裹。','pick 强调从中选出；choose 更通用。picking on somebody 是挑某人的毛病、欺负某人，不能只按采摘理解。',
 ('We spent the morning picking apples.','我们整个上午都在摘苹果。'),('She is picking a book for her younger brother.','她正在为弟弟挑一本书。'),sources=['https://en.wiktionary.org/wiki/picking#English','https://en.wiktionary.org/wiki/pick#English'])
W('pushed','/pʊʃt/','推了、推动了；催促了〔过去式、过去分词〕',
 '手向前施力，让东西离开原来的位置，就是 pushed；把计划往前推进、催一个人行动，也借这个画面。',
 'push + -ed，/ʃ/ 是清辅音，因此 -ed 读 /t/。push 经古法语 poulser 接拉丁 pulsāre 反复击打、推动，与 pellere 推动的词族相连。',
 [['拉丁 pulsāre → 古法语 poulser → push','施力推动 → 推、催促、推进'],['push + -ed → pushed','过去推了；被推动、受到催促']],
 'pushed the door open 推开门；pushed for change 力争改变；pushed back the date 把日期推迟。',
 'pushed the chair closer 把椅子推近些；pushed the project forward 推进项目。','push 表示施力的方向和动作，东西不一定真的移动成功。was pushed 可以是被动，has pushed 则是完成式。',
 ('He pushed the heavy door open.','他推开了那扇沉重的门。'),('The team pushed the project forward.','团队推动了项目进展。'),sources=['https://en.wiktionary.org/wiki/pushed#English','https://en.wiktionary.org/wiki/push#English'])
W('pushing','/ˈpʊʃɪŋ/','推、推动、催促；力争〔现在分词、动名词〕',
 '持续把力量加到某处，让东西或事情往前走，是 pushing。抽象地用时，往前走的是计划、要求或一个人的行动。',
 'push + -ing → pushing。底词沿古法语 poulser 接拉丁 pulsāre，较早与 pellere 推动相连；现代英语在 push 上添加过程形式。',
 [['拉丁推动词族 → 法语 → push','物理施力 → 促使事情前进'],['push + -ing → pushing','正在推；推动、争取的过程']],
 'pushing a trolley 推手推车；pushing for an answer 力争得到答复。push somebody to do 表示催、促使某人做。',
 'keep pushing 继续努力推进；pushing the deadline back 把截止日期往后推。','pushing for 强调争取某个结果；pushing against 可以是向某物施力。具体往哪里推，要看宾语和介词。',
 ('She is pushing the trolley toward the exit.','她正把手推车推向出口。'),('Local residents are pushing for a safer crossing.','当地居民正争取设置更安全的过街设施。'),sources=['https://en.wiktionary.org/wiki/pushing#English','https://en.wiktionary.org/wiki/push#English'])
W('beating','/ˈbiːtɪŋ/','敲打、跳动、打败〔现在分词〕；殴打；节律性拍打',
 '一下接一下地打，是 beating 的基本画面。心脏一下一下跳、雨拍在窗上，也能用这个词；比赛中把对手压过去，则是打败。',
 'beat + -ing → beating。beat 继承古英语 bēatan 击打，是强变化动词；现在的 -ing 形式不改变词干元音，过去分词另作 beaten。',
 [['古英语 bēatan → beat','击打 → 节律性运动；击败'],['beat + -ing → beating；名词用途','正在打、跳动；一次殴打或持续拍打']],
 'a beating heart 跳动的心脏；beating the record 打破纪录；take a beating 遭到殴打，也可比喻受到重创。',
 'rain beating against the window 雨拍打窗户；beating the other team 击败对方球队。','beat 常接对手或纪录，win 常接比赛、奖项。beating 作名词时可能指暴力殴打，语气比普通 beat 节拍重得多。',
 ('I could hear the rain beating against the window.','我能听到雨拍打窗户的声音。'),('Her heart was beating fast before the race.','比赛前她的心跳得很快。'),sources=['https://en.wiktionary.org/wiki/beating#English','https://en.wiktionary.org/wiki/beat#English'])
W('employed','/ɪmˈplɔɪd/','雇用的、有工作的；使用了〔过去式、过去分词〕',
 '让一个人或一种办法投入工作，是 employed。说人，常是被雇用；说工具、方法，常是被拿来使用。',
 'employ + -ed → employed，元音后的 y 保留，-ed 读 /d/。employ 经法语 employer 等接拉丁 implicāre 卷入、牵连，后来发展出使用、雇用义。',
 [['拉丁 implicāre → 法语 → employ','使卷入、投入某项事务 → 使用、雇用'],['employ + -ed → employed','雇用了、使用了；处于受雇状态']],
 'employed by a company 受雇于某公司；employed as a teacher 被聘为教师；the method employed 所采用的方法。',
 'fully employed 有充分工作；techniques employed in the study 研究中采用的技术。','employed 和 employee 角色不同：an employed person 是有工作的人，an employee 是雇员。employed 作过去分词也常直接修饰方法。',
 ('She is employed as a designer at a small company.','她在一家小公司担任设计师。'),('The researchers employed two different methods.','研究人员采用了两种不同的方法。'),sources=['https://en.wiktionary.org/wiki/employed#English','https://en.wiktionary.org/wiki/employ#English'])
W('enjoying','/ɪnˈdʒɔɪɪŋ/','享受、喜欢；享有〔现在分词、动名词〕',
 '人在某件事里感到愉快，或正在得到某种好处，是 enjoying。前者是感受，后者是拥有并受益。',
 'enjoy + -ing → enjoying，y 保留。底词经古法语 enjoir 等，较早 en- 使 + joir 感到快乐，最终接拉丁 gaudēre 高兴；享有利益也是很早的英语用途。',
 [['拉丁 gaudēre → 法语快乐词族 → enjoy','愉快、取乐；享有使用或收益'],['enjoy + -ing → enjoying','正在享受；正在享有某种条件']],
 'enjoying the view 欣赏景色；enjoying good health 身体状况良好；enjoying reading 享受阅读。',
 'enjoying a quiet afternoon 享受安静的下午；enjoying greater freedom 享有更多自由。','enjoy 后接动词时用 -ing：enjoy reading。enjoying 本身已是 -ing，后面仍可接 reading；两个形式各有自己的语法位置。',
 ('We are enjoying the view from the balcony.','我们正欣赏阳台外的景色。'),('The students are enjoying greater freedom in choosing projects.','学生在选择项目方面正享有更大的自由。'),sources=['https://en.wiktionary.org/wiki/enjoying#English','https://www.etymonline.com/word/enjoy'])
W('entering','英 /ˈentərɪŋ/；美 /ˈentərɪŋ/','进入、加入、报名参加；输入〔现在分词、动名词〕',
 '从外边跨进一个范围，是 entering。门内、某个行业、比赛名单、电脑表格，都能成为这个范围。',
 'enter + -ing → entering，末尾 r 不双写，重音不在最后一音节。enter 经古法语 entrer 接拉丁 intrāre 进入，与 intrā 在里面相连。',
 [['拉丁 intrāre → 法语 entrer → enter','到里面去 → 进入地点或活动范围'],['enter + -ing → entering','正在进入；加入、登记或输入的过程']],
 'entering the room 进入房间；entering a competition 报名参赛；entering data 输入数据。',
 'entering a new phase 进入新阶段；entering the job market 进入就业市场。','enter 常直接接地点：enter the room。enter into an agreement 是订立协议，不能把所有 enter 都随手加 into。',
 ('Please check the address before entering it in the form.','把地址填入表格前，请先核对。'),('The project is entering a new phase.','项目正在进入一个新阶段。'),sources=['https://en.wiktionary.org/wiki/entering#English','https://en.wiktionary.org/wiki/enter#English'])
W('landing','/ˈlændɪŋ/','着陆、上岸〔现在分词、动名词〕；着陆、登陆；楼梯平台',
 '从空中或水上来到一个可以落脚的地方，是 landing。楼梯中途让人停步转身的平面，也叫 landing。',
 'land + -ing → landing。land 接古英语 land 陆地，动词的到岸、登岸用途已有较早历史；现代 -ing 可表示过程，也可给着陆或落脚处命名。',
 [['古英语 land 等 → land 名词、动词','陆地 → 来到陆地、使落地'],['land + -ing → landing；名词扩展','着陆过程；楼梯间可落脚的平台']],
 'a safe landing 安全着陆；a landing on the island 在岛上登陆；the upstairs landing 楼上的楼梯平台。',
 'landing at the airport 在机场着陆；a narrow landing 狭窄的楼梯平台。','landing a job 是成功找到工作，像把目标稳稳拿到手。楼梯平台义按实际位置理解，通常不是建筑顶上的屋顶。',
 ('The plane made a smooth landing.','飞机平稳着陆。'),('There is a small window on the upstairs landing.','楼上的楼梯平台有一扇小窗。'),sources=['https://en.wiktionary.org/wiki/landing#English','https://en.wiktionary.org/wiki/land#English'])
W('managing','/ˈmænɪdʒɪŋ/','管理、处理；设法做到、应付〔现在分词、动名词〕',
 '把事情握在手里，让它照着需要运行，是 managing。事情难办时，仍能把它办下来、撑过去，也用 manage。',
 'manage 去末尾 e + -ing → managing。较早经法语 manège、意大利 maneggio、maneggiare 的操控马匹、用手处理用途，最终接拉丁 manus 手。',
 [['拉丁 manus → 意大利、法语操持词 → manage','用手控制 → 处理、管理事务'],['manage 去 e + -ing → managing','正在操持；设法完成、应付']],
 'managing a team 管理团队；managing time 安排时间；managing to finish 设法完成。',
 'managing several tasks 处理几项任务；How are you managing? 你应付得怎么样？','manage a task 强调处理任务；manage to do 强调克服困难做成。managing director 是固定职位名，通常指董事总经理等，具体职权看机构。',
 ('She is managing a team of six people.','她正管理一个六人团队。'),('He is managing to study while working full time.','他在全职工作的同时，仍设法坚持学习。'),sources=['https://en.wiktionary.org/wiki/managing#English','https://www.etymonline.com/word/manage'])
W('cleaning','/ˈkliːnɪŋ/','清洁、打扫〔现在分词、动名词〕；清扫工作',
 '让脏污从东西上离开，使它重新干净，是 cleaning。对象也可以是数据：把错误、重复或不合要求的内容清理掉。',
 'clean + -ing → cleaning。clean 继承古英语 clǣne 干净、纯净等义；英语动词表达使干净，-ing 再表示正在做或这项工作。',
 [['古英语 clǣne → clean；动词用途','干净 → 使某物干净'],['clean + -ing → cleaning','正在清理；清洁这件工作']],
 'cleaning the kitchen 打扫厨房；cleaning products 清洁用品；data cleaning 数据清理。',
 'do some cleaning 做些清洁；cleaning up after dinner 饭后收拾。','cleaning products 是用来清洁的产品；clean products 则是干净的产品。cleaning 作工作名词常不可数：some cleaning。',
 ('I spent an hour cleaning the kitchen.','我花了一小时打扫厨房。'),('The team is cleaning the data before the analysis.','团队正在分析前清理数据。'),sources=['https://en.wiktionary.org/wiki/cleaning#English','https://en.wiktionary.org/wiki/clean#English'])
W('throwing','英 /ˈθrəʊɪŋ/；美 /ˈθroʊɪŋ/','扔、投、抛；使突然处于〔现在分词、动名词〕',
 '用一个动作把东西从手边送出去，是 throwing。把自己一下投入某事、把问题抛给别人，也借这个突然投入或送出的画面。',
 'throw + -ing → throwing，保留 ow。throw 继承古英语 þrāwan 转、扭；投掷义后来居于中心，转动后抛出的动作可能有助于理解联系，但历史动机不写死。',
 [['古英语 þrāwan → throw','转、扭的旧义 → 投掷成为中心用途'],['throw + -ing → throwing','正在投、抛；投掷的过程']],
 'throwing a ball 投球；throwing away rubbish 扔掉垃圾；throwing yourself into work 全身心投入工作。',
 'throwing stones into the water 往水里扔石头；throwing a party 举办聚会。','throwing a party 是举办聚会的固定用法，不能按扔一个聚会逐字译。throw 的过去式 threw，过去分词 thrown，-ing 形式用原词干。',
 ('The children were throwing a ball to each other.','孩子们正在互相抛球。'),('They are throwing a party for their parents.','他们正在为父母举办聚会。'),sources=['https://en.wiktionary.org/wiki/throwing#English','https://en.wiktionary.org/wiki/throw#English'])
W('improving','/ɪmˈpruːvɪŋ/','改善、提高；好转〔现在分词、动名词〕',
 '同一件事比原来更好，是 improving：既可以主动把它改好，也可以说它自己在好转。',
 'improve 去 e + -ing → improving。底词接盎格鲁法语 emprouwer 使产生收益，含 en- 与 prou 利益；收益增加的意思后来扩展为品质、状况变好。拼写曾受 -prove 类词影响。',
 [['盎格鲁法语 emprouwer → improve','产生收益、利用 → 改善、变好'],['improve 去 e + -ing → improving','正在改进某物；某种情况正在好转']],
 'improving skills 提高技能；improving the service 改进服务；the weather is improving 天气在好转。',
 'improving steadily 稳步提高；ways of improving sleep 改善睡眠的办法。','improve 可以有宾语，也可没有：improving the system 是改进系统，the system is improving 是系统正在变好。两种句子中的行动者不同。',
 ('Her writing is improving with regular practice.','随着经常练习，她的写作正在进步。'),('We are improving the instructions for new users.','我们正在改进给新用户的说明。'),sources=['https://en.wiktionary.org/wiki/improving#English','https://www.etymonline.com/word/improve'])
W('attempted','/əˈtemptɪd/','尝试了、企图了〔过去式、过去分词〕；未遂的',
 '已经朝目标动手试过，是 attempted；它只说迈出了尝试这一步，成功与否要另看结果。',
 'attempt + -ed，/t/ 后读 /ɪd/。底词经古法语 atempter 接拉丁 attemptāre，含 ad- 朝向与 temptāre 尝试、试探；英语形式受拉丁拼写影响。',
 [['拉丁 attemptāre → 古法语 → attempt','朝目标尝试、试探 → 着手试做'],['attempt + -ed → attempted','过去尝试；描述已着手但未完成的行为']],
 'attempted to open 试图打开；an attempted theft 一次未遂盗窃。修饰某些违法行为时，attempted 常说明未遂。',
 'attempted a repair 尝试修理；attempted to explain 试着解释。','attempted to do 可能成功，也可能失败；只有结合结果或未遂的固定语境，才能确定。tried to do 在日常交流里通常更口语。',
 ('She attempted to repair the old clock.','她试着修理那座旧钟。'),('They attempted the climb but turned back before dark.','他们尝试攀登，但在天黑前折返了。'),sources=['https://en.wiktionary.org/wiki/attempted#English','https://en.wiktionary.org/wiki/attempt#English'])
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_ze',ROOTS,WORDS)
 extend_lessons()
