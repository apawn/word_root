"""Pedo- sources, penta-, boilers, deployment, outdoors, scotch, satisfactory and -ier."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()

R('A2138','儿童与脚是两条同形构词材料，须看具体词源','PEDO：先分儿童 paid-，还是脚 ped-','pediatric、pedophile 属儿童材料；pedometer 属脚的计步材料，不是儿童计量器。',
 '同样 pedo- 拼法，希腊儿童与拉丁脚并非一个根。连同儿科词的 paediatric 拼写对照，就不容易把计步器读成给儿童用的仪器。',
 '希腊 pais、paid- 儿童 → pedo-，接医疗或偏好等后半材料；拉丁 pes、ped- 脚 → pedometer，且有法语借入历史。',
 [['希腊儿童材料','pediatric · pedophile'],['拉丁脚材料','pedometer']],
 '不能把这页所有 ped- 都合成脚或儿童一个意思；后半 -iatric、-phile、-meter 各有专门范围。',
 'The pedometer counts steps; pediatric care concerns children.\n\n计步器数步数，儿科医疗关注儿童。','pediatric pedophile pedometer')
R('A1725','希腊五的数量材料，后半决定五个什么','PENTA：先数到五，再看边、角、音','pentagon 五边形，pentagram 五角星形，pentatonic 五声音阶相关。',
 '五这个核心清楚，不能因都五个就把图形与音乐当同一事物。前缀认数量，后半认对象，是这组最省力的学习法。',
 '希腊 pente 五 → penta-；gon 角、边形材料；gram 写画图形；tonic 音调材料。',
 [['五的图形与声音名称','pentagon · pentagram · pentatonic']],
 'pentagon 的五边形与 pentagram 五角星不同；pentatonic 不是五个音符随便摆在一起的唯一指定旋律。',
 'The lesson moves from a pentagon to a pentatonic melody.\n\n课程从五边形讲到五声音阶旋律。','pentagon pentagram pentatonic')
R('B3896','按 boil 功能命名的设备，再形成板材和职业名','BOILER：先是加热设备，再看它的板材和制作者','boiler → boilerplate、boilermaker；实物名称可再发展成模板、饮品俗称等固定义。',
 'boiler 的 -er 是设备，不是每次都指煮东西的人。boilerplate 从锅炉板材、印刷预制片到重复模板内容，boilermaker 从职业又转出饮品俚语。',
 'boil + -er；boiler + plate；boiler + maker。现代设备不保证每一种都把水煮成蒸汽，旧功能名可扩大范围。',
 [['设备与板材、模板','boiler · boilerplate'],['制作者及固定俗称','boilermaker']],
 'boilerplate 代码不是锅炉程序专名；boilermaker 的饮品义不能硬定一个未经证实的工人故事。',
 'The boilermaker examined the boilerplate before repairing the boiler.\n\n锅炉工修锅炉前，先检查了锅炉板材。','boiler boilerplate boilermaker')

Dp=[['拉丁 dis- 分开 + plicare 折叠 → 法语 desploiier、déployer','把折拢的东西展开'],['英语 deploy → 部署兵力、资源、系统；+ -able、re-','展开到可用位置；可部署；再次、重新部署']]
W('deploy','/dɪˈplɔɪ/','部署、调配；展开；使系统投入使用',
 '折拢的东西展开到能用的位置，是旧画面。后来队伍放到需要的位置、人员资源安排上场、软件投入运行，都能叫 deploy。',
 '借法语 déployer 等展开词，接拉丁 dis- 分开 + plicare 折叠。与 display 有共同历史材料；不是现代 de- 加 ploy 策略临时拼成。',Dp,
 'deploy resources 调配资源；deploy a team 部署团队；deploy an application 部署应用；deploy a parachute 展开降落伞。',
 'deploy resources；deploy an application。',
 'develop 是开发，deploy 是放到可用环境、位置；软件写好未必已部署，部署也未必等于向所有人公开发布。',
 ('The organiser deployed volunteers at each entrance.','组织者在各入口安排了志愿者。'),('The team deployed the application to a test environment.','团队把应用部署到测试环境。'),sources=['https://en.wiktionary.org/wiki/deploy#English','https://www.etymonline.com/word/deploy'])
W('deployable','/dɪˈplɔɪəbəl/','可部署的、可展开使用的',
 '东西已经能被放到需要的位置展开、投入用，就是 deployable。它说可用来部署，不是保证任何地方都能立刻用。',
 'deploy + -able，并有法语 déployable 对应形式；保留 y。形容词接可被部署，也可在专门语境中作可部署资源的名词。',Dp+[['deploy + -able／法语对应形式 → deployable','能展开、部署使用的性质']],
 'deployable equipment 可部署设备；a deployable package 可部署软件包；deployable resources 可调配资源。',
 'deployable equipment；a deployable package。',
 'deployable 不是已经 deployed；前者讲可部署性，后者讲动作已经发生或相应状态。',
 ('The exercise used lightweight, deployable equipment.','演练使用了轻便、可部署的设备。'),('The build produces a deployable software package.','构建过程生成可部署的软件包。'))
W('redeploy','/ˌriːdɪˈplɔɪ/','重新部署；调配到其他岗位、位置',
 '原来放在一处的人员、资源，改放到新的需要处，是 redeploy。re- 不只可能重复原动作，也可意味着重新安排。',
 're- 再次、重新 + deploy → redeploy，现代军事、组织、技术场景均可使用。不是把部署完全撤销后的唯一表达。',Dp+[['re- + deploy → redeploy','再次部署，或改变部署位置、用途']],
 'redeploy staff 重新调配员工；redeploy resources 重新分配资源；redeploy an application 重新部署应用。',
 'redeploy staff；redeploy resources。',
 'redeploy 是重新安排用途、位置，dismiss 是解雇，withdraw 是撤回；具体动作可能有关，却不是同义词。',
 ('The organisation redeployed staff to the busiest office.','机构把员工重新调配到最忙的办公室。'),('The team redeployed the application after correcting the configuration.','团队改正配置后重新部署了应用。'))
R('B4593','把折拢的东西展开，走向可用位置与资源调配','DEPLOY：摆开到需要的位置，让它能用上','deploy → deployable；redeploy 再次或重新安排。',
 '从展开画面进入，理解军事、人员、软件几个场景。开发、可部署、已经部署、重新调配是不同阶段和动作。',
 'dis- + plicare → 法语 déployer 等 → deploy；-able 可能性；re- 再次、重新。',
 [['部署动作与可部署性质','deploy · deployable'],['重新安排、部署','redeploy']],
 'deploy 不同于 develop；deployable 不同于 deployed；redeploy 员工也不自动是解雇。',
 'The deployable system was deployed once, then redeployed after an update.\n\n这套可部署系统先投入使用，更新后又重新部署了一次。','deploy deployable redeploy')

Od=[['outdoor、out of doors 等旧表达 → outdoors','在户外，-s 带旧副词材料'],['outdoors + -y、-man','喜欢、适合户外生活；户外活动爱好者']]
W('outdoorsy','英 /aʊtˈdɔːzi/；美 /aʊtˈdɔːrzi/','喜欢户外活动的；适合、有户外风格的',
 '周末更想徒步、露营而不是一直待屋里，可以说 outdoorsy。衣物、活动也能说有户外生活风格，不只描写一个人。',
 'outdoors + -y → outdoorsy，保留 s 并读 /z/。outdoors 的 s 有旧副词词尾、短语发展背景，不当成门 doors 的普通复数来解释整词。',Od,
 'an outdoorsy person 喜欢户外的人；an outdoorsy family 爱户外活动的家庭；an outdoorsy style 户外风格。',
 'an outdoorsy person；an outdoorsy style。',
 'outdoor 常是户外场所、用途的修饰语，outdoorsy 更常说爱好、风格；不是任何 outdoor lamp 都天然适合改叫 outdoorsy lamp。',
 ('She is outdoorsy and spends most weekends hiking.','她喜欢户外活动，大多数周末都去徒步。'),('The shop sells casual clothes with an outdoorsy style.','店里卖带户外风格的休闲衣服。'))
W('outdoorsman','英 /aʊtˈdɔːzmən/；美 /aʊtˈdɔːrzmən/','户外活动爱好者〔传统上指男子〕',
 '常去徒步、钓鱼、野外活动的人，传统称呼中可叫 outdoorsman。它不表示这个人没有房屋、只能睡外面。',
 'outdoors + -man → outdoorsman，复数 outdoorsmen。词形保留男性人物材料，泛指不限定性别的人也常用 outdoor enthusiast。',Od+[['outdoors + -man → outdoorsman','经常参与户外活动的男子称呼']],
 'a keen outdoorsman 热衷户外活动的人；an experienced outdoorsman 经验丰富的户外活动者。',
 'a keen outdoorsman；an experienced outdoorsman。',
 'outdoorsman 不等于 homeless person 无家可归者，也不保证每个人有专业野外技能；它先说活动偏好、生活方式。',
 ('Her father is a keen outdoorsman who enjoys fishing and walking.','她父亲热衷户外活动，喜欢钓鱼和步行。'),('The biography describes him as an experienced outdoorsman.','传记把他描述为经验丰富的户外活动者。'))
R('B2551','户外位置表达，进入爱好、风格与人物称呼','OUTDOORS：人走到屋外，活动也围绕屋外','outdoors → outdoorsy、outdoorsman，地点副词、风格性质、人物名。',
 'outdoors 说在哪里，outdoorsy 说爱不爱、像不像户外风格，outdoorsman 说相关活动人物。词形层次清楚，就不会把三个词都译成在外面。',
 'outdoor 加旧副词 -s，或联系 out of doors 短语发展 → outdoors；再接 -y、-man。',
 [['位置、偏好与人物','outdoors · outdoorsy · outdoorsman']],
 'outdoors 的 s 不按一般复数解释；outdoorsman 也不是无家可归的同义词。',
 'The outdoorsy family spends much of its free time outdoors.\n\n这家人喜欢户外活动，很多闲暇时间都在户外度过。','outdoors outdoorsy outdoorsman')

Sc=[['中古英语 scocchen 接法语 escocher 等切划材料','切口、划线；后有阻止、扑灭等动词义'],['另有垫块 scotch，来源未定；Scottish 缩短成 Scotch','阻止义有近形材料交汇；苏格兰称呼另源']]
W('scotch','英 /skɒtʃ/；美 /skɑːtʃ/','制止、打消；划痕、划线〔旧〕；Scotch 苏格兰威士忌',
 'scotch a rumour 是把传言压下、打消；hopscotch 里的旧 scotch 是地上划的线。酒名 Scotch 却是苏格兰相关称呼，不是传言被砍成酒。',
 '切划义由中古英语 scocchen 等接盎格鲁法语 escocher；垫住防滚动的 scotch 又有未定来源材料，参与阻止等义。大写 Scotch 则由 Scottish 缩短，不能全归入切划根。',Sc,
 'scotch a rumour 打消传言；scotch a plan 阻止计划；Scotch whisky 苏格兰威士忌；旧划线义见 hopscotch。',
 'scotch a rumour；scotch a plan；Scotch whisky。',
 'hopscotch 不是跳苏格兰；butterscotch 后半来源有不同解释，不靠糖果名字反推所有 scotch 都同源。',
 ('The clear statement scotched the rumour.','明确声明打消了传言。'),('The glossary distinguishes the verb scotch from Scotch whisky.','术语表把动词 scotch 与 Scotch whisky 的酒名区分开。'),sources=['https://en.wiktionary.org/wiki/scotch#English','https://www.merriam-webster.com/dictionary/scotch'])
R('B3755','切划、阻止与苏格兰同形词分源，复合词不必都统一','SCOTCH：划线和打消一支，苏格兰称呼另读','scotch → hopscotch 取划线旧义；butterscotch 的后半仍保留来源争论。',
 '不要用一个苏格兰故事解释整页。跳房子按地上划线理解，打消传言按现代阻止义理解，糖名与酒名各有历史问题。',
 'scocchen、escocher 等 → scotch 切划；垫块近形词来源未定；Scottish → Scotch；hop + scotch，butter + scotch 的后半有争论。',
 [['切划、制止与游戏名','scotch · hopscotch'],['来源有争论的糖名','butterscotch']],
 'butterscotch 的 scotch 不硬定苏格兰或切糖一条；Scotch 酒名与切划旧词不同源。',
 'The teacher scotched the idea that hopscotch means hopping around Scotland.\n\n老师打消了 hopscotch 意为在苏格兰跳来跳去的误解。','scotch hopscotch butterscotch')
R('B4478','达到满意要求的性质，否定与副词再调整表达','SATISFACTORY：够达到要求，让人可以接受','satisfactory → satisfactorily；unsatisfactory 加上否定，表示没有达到要求。',
 '先抓达标、令人满意，不必把它夸成完美、卓越。副词说办得是否令人满意，否定词说结果未达要求。',
 '法语 satisfactoire、拉丁 satisfactorius 等 → satisfactory；y 改 i 接 -ly → satisfactorily；un- 否定。',
 [['满意性质与方式','satisfactory · satisfactorily'],['未达满意要求','unsatisfactory']],
 'satisfactory 通常不等于 excellent；satisfactorily 与 satisfyingly 在达标和主观满足感上常有不同搭配重心。',
 'The satisfactory explanation resolved the issue satisfactorily.\n\n令人满意的解释妥善解决了问题。','satisfactory satisfactorily unsatisfactory')

Br=[['法语 brigade 部队 + -ier 人物材料 → brigadier','旅级指挥者称呼，后进入军衔名称'],['英语借入 brigadier','具体军衔制度因体系而异，不按词尾推所有等级']]
W('brigadier','英 /ˌbrɪɡəˈdɪə/；美 /ˌbrɪɡəˈdɪr/','准将；旅级军官称呼',
 'brigade 是旅级部队，brigadier 历史上接带领这类部队的人。现代常作为军衔、头衔读，不能只把它当“任何带着一群士兵的人”。',
 '借法语 brigadier，由 brigade + -ier 形成人物词。英语所指头衔要结合国家、年代，不能从同一个汉语准将推所有军制完全一致。',Br,
 'Brigadier + 姓名 准将头衔；a retired brigadier 一位退役准将；也可和 brigade 旅配对记。',
 'a retired brigadier；Brigadier + name。',
 'brigadier 与 brigade 部队名不同；brigadier、brigadier general 在各体系的用法不能仅凭英文多一个词就机械排等级。',
 ('The biography follows the career of a retired brigadier.','传记追踪了一位退役准将的经历。'),('The brigadier addressed the assembled officers.','准将向集合的军官讲话。'),sources=['https://en.wiktionary.org/wiki/brigadier#English','https://www.oxfordlearnersdictionaries.com/definition/english/brigadier'])
R('A1816','法语人物、职业词尾及其英语类推，读音与整词历史不同','-IER：常在说从事相关工作的人，别当比较级','collier、clothier 看职业，grenadier、brigadier 看军事人物；brazier 取铜匠一支。',
 '不是每个词都由现代英语现场把 -ier 粘上去，很多整词借入或受职业词类推。brazier 火盆还另有法语余烬词来源，不能全部变成黄铜匠。',
 '法语 -ier 接更早人物关系材料；brigade → 法语 brigadier；grenade → grenadier；coal 的旧词形 → collier；cloth 等职业形式类推。',
 [['职业人物','collier · clothier · brazier'],['军事人物与军衔','grenadier · brigadier']],
 'brazier 铜匠与火盆分源；collier 的煤船名是人物词再转用途；-ier 在这些词里不是 funny → funnier 的比较级尾。',
 'The museum labels identify a clothier, a collier and a brigadier in the old portraits.\n\n博物馆说明牌标出了旧肖像中的制衣业者、煤业从业者和准将。','collier clothier brazier grenadier brigadier')

if __name__=='__main__':save('continuation_20261030_ot',ROOTS,WORDS)
