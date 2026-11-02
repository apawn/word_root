"""Hat, pilot, secondary and musical: jobs, guidance, order and sensitivity."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
H=[['古英语 hætt → 中古英语 hat → hat','帽子，遮盖头部的物品'],['英语比喻','所戴的帽子 → 所扮演的角色、职责']]
W('hat','/hæt/','帽子；身份、职责〔比喻〕',
 '头上一顶帽子能遮阳、挡冷，也可能标明职位；说 wear several hats，就把不同职责想成几顶轮着戴的帽子。',
 '接古英语 hætt，是本族旧词。更远来源有不确定性，现代 hat 不拆成 h + at；职业身份义是在帽子画面上发展。',H,
 'a straw hat 草帽，take off your hat 脱帽，wear several hats 身兼数职，take your hat off to someone 向某人表示佩服。',
 'a straw hat；take off your hat；wear several hats；take your hat off to。',
 'hat 是宽泛帽子名，cap 常是贴头、带帽舌等具体帽型；wear several hats 不必真把几顶帽子叠头上。',
 ('Take your hat off when you come inside.','进屋后把帽子摘下来。'),('In this small company, everyone wears several hats.','在这家小公司里，人人都身兼数职。'))
W('hatter','英 /ˈhætə/；美 /ˈhætər/','制帽、修帽或卖帽的人',
 '给帽子量尺寸、做帽、卖帽的从业者；末尾 -er 指做这行的人。',
 'hat 双写 t + -er，中古英语已有 hatter。不是 hater 讨厌者：一个双 t，一个单 t，元音也不同。',H[:1]+[['hat + -er → hatter','制帽或经营帽子的人']],
 'a master hatter 制帽大师，a hatter’s shop 帽店；the Mad Hatter 疯帽匠是文学中熟悉的名字。',
 'a master hatter；a hatter’s shop；the Mad Hatter。',
 'hatter /ˈhætər/ 制帽人，hater /ˈheɪtər/ 怀恨者；不要因为都是 -er 就忽略词基和双写。',
 ('The hatter measured his head before making the hat.','制帽人做帽子前量了他的头围。'),('Her grandfather worked as a hatter.','她祖父曾以制帽为业。'))
W('asshat','/ˈæshæt/','蠢货、讨厌的混蛋〔粗俗俚语〕',
 '把对方骂成既蠢又惹人烦的人，重点是冒犯语气，不是他真戴着某种帽子。',
 'ass + hat 的粗俗组合，常被联系到 head up one’s ass 这类骂人不明事理的说法；按夸张意象理解，不需要当成现实器物。',
 [['ass + hat → asshat','粗俗组合，借荒唐头部意象骂人'],['现代俚语','愚蠢、无知又讨厌的人']],
 'call someone an asshat 骂某人蠢货；常在网络争吵、随意口语中出现，语气比单说 foolish 很不客气。',
 'an asshat；call someone an asshat〔粗俗、冒犯〕。',
 'asshat 是骂人的人物名词，hatter 是正经职业。看懂前者的态度即可，不把它当帽子制造商。',
 ('He apologized for calling his friend an asshat.','他为骂朋友蠢货而道歉。'),('The reviewer uses asshat as a deliberately rude insult.','评论者用 asshat 故意粗鲁地骂人。'))
R('B3655','帽子、戴帽子的职责；制帽人和粗俗组合','HAT：头上戴的物品，也能标明一种角色','hat → hatter 制帽人；wear several hats 身兼数职；asshat 是粗俗骂人话。',
 '先抓住帽子，再看职业后缀。比喻职责很常用，粗俗组合只按实际语气解释，不给它假装中性的中文。',
 'hætt → hat；hat + -er 双写 t；ass + hat；hat 作动词的常规形式可为 hatted。',
 [['帽子与职业','hat · hatter'],['粗俗人物称呼','asshat']],
 'hatter/hater 制帽人和怀恨者读音拼写都不同；hat 的角色比喻不要求真有帽子。',
 'The hatter wears several hats: designer, maker and shopkeeper.\n\n这位制帽人身兼数职：设计师、制作人和店主。','hat hatter asshat')
P=[['意大利语 piloto 等 → 法语 pilote/pillot','航行、掌舵、引航的人'],['英语 pilot','引航员 → 飞行员；引导、试行、试播']]
W('pilot','/ˈpaɪlət/','飞行员；引航员；试点、试播；驾驶、试行',
 '最初先想带船安全走过水路的人，再把带路、掌舵搬到飞机；一个新方案先探路，也叫 pilot。',
 '经法语接意大利语 piloto 等，较早形式常联系到希腊舵桨、掌舵词；中间形式和变化有推测，不能拆成 pi + lot。英语的船舶用法早于飞机用法。',P,
 'an airline pilot 航空公司飞行员，a harbor pilot 港口引航员，a pilot project 试点项目，a pilot episode 试播集；pilot a scheme 试行方案。',
 'an airline pilot；a harbor pilot；a pilot project；a pilot episode。',
 'pilot 人员义不只飞机驾驶员，船上的引航员也常见；pilot project 是先小范围试验，不是飞行员专用项目。',
 ('A local pilot guided the ship into the harbor.','一名当地引航员引导船只进港。'),('The city will pilot the scheme in two neighborhoods.','该市将先在两个街区试行这个方案。'),sources=['https://www.etymonline.com/word/pilot'])
W('copilot','英 /ˈkəʊpaɪlət/；美 /ˈkoʊpaɪlət/','副驾驶员；共同驾驶、协助驾驶',
 '不是坐旁边看热闹的乘客，而是能协同完成驾驶任务的另一位飞行员。co- 抓一起协作。',
 'co- 共同、协同 + pilot 驾驶员，也常拼 co-pilot。较新的工具命名借它表示协助工作，但词的基本职业义先存在。',P+[['co- + pilot → copilot','协同驾驶的另一位驾驶员、助手']],
 'the pilot and copilot 机长与副驾驶员〔具体职位按语境〕，serve as copilot 担任副驾驶；a writing copilot 是借喻协作写作工具。',
 'the pilot and copilot；serve as copilot。',
 'copilot 是协同驾驶者，autopilot 是自动驾驶系统或机制；人和系统不能只凭中文都有驾驶就混。',
 ('The copilot read the checklist aloud.','副驾驶员大声读出了检查单。'),('She served as copilot on the return flight.','返程飞行中，她担任副驾驶员。'))
R('B3268','引航、驾驶与先行探路','PILOT：替船、飞机或新计划把方向','pilot 引航、驾驶 → pilot project 先试路；copilot 协同驾驶者；autopilot 自动系统。',
 '把方向掌住、先探一段路，能把引航员、试播集、试点项目连起来。它不是因为现代飞机而新造的词。',
 'piloto → pilote → pilot；co- + pilot；auto- + pilot。',
 [['引航、驾驶和试点','pilot'],['协同与自动','copilot · autopilot']],
 'pilot/captain 岗位不完全相同；copilot/autopilot 协同驾驶者与自动系统；pilot episode 试播集。',
 'The pilot and copilot tested the autopilot during the flight.\n\n飞行中，两位驾驶员测试了自动驾驶系统。','pilot copilot autopilot')
S=[['拉丁 secundus → secundārius','第二、随后 → 第二位或第二等的'],['中古英语 secundarie → secondary','次要、第二级、继发等关系']]
W('secondary','英 /ˈsekəndəri/；美 /ˈsekənderi/','次要的；第二级的；中等教育的；间接、继发的',
 '先排一个主次或先后：跟在第一项后面、由第一项引起，或者处在教育的第二阶段；各场景的第二关系不同。',
 '经中古英语接拉丁 secundārius，来自 secundus 第二 + 相应形容词后缀；现代可对应 second + -ary，不是 secretary 秘书。',S,
 'a secondary concern 次要顾虑，secondary education 中等教育，a secondary source 二手资料、间接来源。具体分级与制度要看上下文。',
 'a secondary concern；secondary education；a secondary source；be secondary to。',
 'secondary 次要不等于毫无价值；secondary source 不是“错误来源”，而是相对于原始材料的后续解释、整理等。',
 ('Cost is important, but it is secondary to safety.','费用很重要，但安全更优先。'),('The textbook is a secondary source for the historical event.','这本教科书是研究该历史事件的二手资料。'))
W('secondarily','英 /ˌsekənˈderəli/；美 /ˌsekənˈderəli/','其次；在第二位、次要地；间接地',
 '说明有两个考虑时，先把主要的摆前面，再说其次还考虑什么。也可说影响通过另一层关系间接传来。',
 'secondary 的副词对应 -ly，y 改 i；常见读音重音移到后面的 /der/。中古英语已有相应形式。',S+[['secondary → secondarily','在次要程度或第二层关系上']],
 'primarily ... and secondarily ... 主要……其次……；secondarily affected 间接受影响。实际句子选主次还是因果层级。',
 'primarily … secondarily …；secondarily affected。',
 'secondly 常是列点“第二”；secondarily 更强调次要程度、后续关系，不是每次列两条都必须换这个长词。',
 ('The course focuses primarily on writing and secondarily on presentation.','这门课主要练写作，其次练展示。'),('We considered speed and, secondarily, appearance.','我们考虑了速度，其次才是外观。'))
R('B4080','第二位、次级、随后；中等教育','SECONDARY：先确定按什么顺序或层级排','secondary → secondarily；postsecondary 接在中等教育之后。',
 '优先级的第二、教育层级的第二、材料来源的间接，都用到跟在主要或前一层之后的关系。不同关系不能混成差等。',
 'secundus → secundārius → secondary；secondary → secondarily；post- + secondary → postsecondary。',
 [['基本次级关系','secondary · secondarily'],['教育阶段扩展','postsecondary']],
 'secondary 不等于不重要；secondarily/secondly 次要程度与列点第二；postsecondary 不是小学之后的一切。',
 'The report examines secondary education and opportunities for postsecondary study.\n\n报告考察中等教育及中等教育后的升学机会。','secondary secondarily postsecondary')
W('musicality','/ˌmjuːzɪˈkæləti/','音乐性；乐感、音乐表现力',
 '音都弹对还不够：哪里该轻，哪句该呼吸，节奏怎样流动，这些听得出、表达得出的音乐感觉叫 musicality。',
 'musical + -ity，性质名词，重音后移到 /kæl/。不是 musical 音乐剧的复数，而是音乐性、乐感这类抽象性质。',
 [['希腊 mousikē 等 → music','与缪斯、艺术有关的历史材料 → 音乐'],['music → musical → musicality','音乐的 → 音乐性、音乐表现能力']],
 'natural musicality 天生乐感，develop musicality 培养乐感，the musicality of language 语言的音乐性、节奏音韵。',
 'natural musicality；develop musicality；the musicality of language。',
 'musicality 常说敏感、表现力，technical skill 技术能力；好技术能帮助表达，但音弹对不自动等于表现有乐感。',
 ('Her playing combines technical precision with remarkable musicality.','她的演奏把精准技巧和出色乐感结合起来。'),('The poet loved the musicality of everyday speech.','诗人喜爱日常言语里的音乐性。'))
R('B2577','音乐的；以音乐方式；乐感和音乐性','MUSICAL：从与音乐有关，走到听得出、表达得出音乐','musical → musically 以音乐方式、在音乐方面；musicality 音乐性、乐感。',
 'music 是音乐，musical 是相关形容词，也能作音乐剧名词；musicality 把音乐感受和表现的性质拿出来谈。',
 'music + -al → musical；musical + -ly/-ity → musically/musicality。',
 [['音乐相关及表达方式','musical · musically'],['音乐性与乐感','musicality']],
 'musical 名词音乐剧与 musicality 抽象乐感分清；musically/technically 音乐表达与技术角度可以对照。',
 'The musical is technically demanding and rewards performers with real musicality.\n\n这部音乐剧技术要求高，也很需要演员有真正的音乐表现力。','musical musically musicality')
if __name__=='__main__':save('continuation_20261030_gj',ROOTS,WORDS)
