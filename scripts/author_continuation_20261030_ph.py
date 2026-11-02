"""High-priority -al: related adjectives, action nouns and their common bases."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()

Pr=[['古法语 pro- + poser → proposer → 英语 propose', '向前放出、供考虑；法语 poser 在语义上替代了较早 ponere 相关词形'],['英语 propose → proposal','提出建议、求婚；所提出的计划、请求']]
W('propose','英 /prəˈpəʊz/；美 /prəˈpoʊz/','提议、提出；求婚；打算〔较正式〕',
 '把一个办法摆到大家面前，说“这样做怎么样”，就是 propose。向某人提出结婚请求，是它另一种常见场景。',
 '借古法语 proposer，含 pro- 向前与 poser 放。poser 接较早 pausare 停下、使安放，并在法语中替代了拉丁 ponere 放的相关复合词形，因此与拉丁 proponere 意义相接，不能画成词形未经改变的直接继承。',Pr,
 'propose a plan 提出计划；propose doing 建议做；propose to someone 向某人求婚；propose to do 较正式说打算做。',
 'propose a plan；propose doing；propose to someone。',
 'propose doing 常是建议，propose to do 常是打算；propose to a person 则可能是求婚，要看后接成分。',
 ('She proposed a simpler solution.','她提出了一个更简单的办法。'),('He proposed to her during their holiday.','度假时他向她求婚。'))
W('proposal','英 /prəˈpəʊzəl/；美 /prəˈpoʊzəl/','提案、建议；求婚',
 'propose 是把想法提出去，proposal 是被摆出来供考虑的那份内容，或求婚这个请求。它仍在等待评估、回应。',
 'propose 去末尾 e 加名词尾 -al → proposal。这里 -al 形成动作、结果名词，不是所有结尾 -al 都是形容词。',Pr+[['propose + -al → proposal','提出的计划、建议，或求婚请求']],
 'a research proposal 研究计划书；submit a proposal 提交提案；a marriage proposal 求婚。',
 'submit a proposal；a research proposal；a marriage proposal。',
 'proposal 是提议，不等于已批准的 agreement 协议；被提出与获同意是不同阶段。',
 ('The committee discussed the proposal.','委员会讨论了这份提案。'),('She accepted his marriage proposal.','她答应了他的求婚。'))
Oc=[['拉丁 occupare 占据、抓住 → occupatio → 法语 occupation','占用、从事的活动与控制关系'],['英语 occupation → occupational','职业、占用等；相关性质']]
W('occupation','英 /ˌɒkjəˈpeɪʃən/；美 /ˌɑːkjəˈpeɪʃən/','职业；占用、居住；占领',
 '平常用什么工作占据时间，是职业；房屋被使用、地区被控制，则是占用、占领。共同材料是某处或某事被占据。',
 '经法语接拉丁 occupatio、occupare 等占据材料；现代与 occupy 对应，不能把 occupation 每次都只译职业。',Oc,
 'state your occupation 填写职业；military occupation 军事占领；a building in occupation 有人使用、居住的建筑，后者较正式。',
 'state your occupation；military occupation。',
 'occupation 通常职业，具体职位可说 job；occupation 的占领义不是在问从事哪个行业。',
 ('The form asks for your name and occupation.','表格要求填写姓名和职业。'),('The book examines life during the occupation.','书中研究了占领时期的生活。'))
W('occupational','英 /ˌɒkjəˈpeɪʃənəl/；美 /ˌɑːkjəˈpeɪʃənəl/','职业的；与工作有关的',
 '工作带来的风险、按职业划分的群体，都是 occupational 的常见对象。它说相关领域，不直接评价专业能力高低。',
 'occupation + -al → occupational；形容词尾把职业、从业活动等名词变成相关性质。其他占用等义须看具体文本。',Oc+[['occupation + -al → occupational','与职业、从业活动等相关的']],
 'occupational health 职业健康；an occupational hazard 职业风险；occupational groups 职业群体。',
 'occupational health；an occupational hazard；occupational groups。',
 'occupational 说与职业有关，professional 还可评价专业、职业化；occupational 不等于做得很专业。',
 ('The survey compares several occupational groups.','调查比较了几个职业群体。'),('The report discusses occupational hazards in the industry.','报告讨论了行业中的职业风险。'))
Bt=[['中古英语 be- + tray 等出卖材料 → betray','旧 tray 接法语 trahir 等，再接拉丁交付材料'],['现代 betray 的信任与显露用法','背叛、泄密；显露义还受近形 bewray 影响']]
W('betray','/bɪˈtreɪ/','背叛、出卖；泄露；无意显露',
 '别人信你会守住，你却把秘密、利益交出去，是 betray；声音藏不住紧张，也能 betray your fear，不一定真在背叛谁。',
 'be- 加旧 tray 出卖材料，后者接法语、拉丁交付的词族。现代显露、泄露义还受近形旧词 bewray 影响，不由一个现代托盘 tray 推出。',Bt,
 'betray a friend 背叛朋友；betray trust 辜负信任；betray a secret 泄密；betray fear 无意露出害怕。',
 'betray trust；betray a secret；betray fear。',
 'betray a feeling 可只是显露情绪；不能每个 betray 都译成政治叛变或有意恶行。',
 ('He refused to betray his friend’s trust.','他不愿辜负朋友的信任。'),('Her voice betrayed her nervousness.','她的声音露出了紧张。'))
W('betrayal','/bɪˈtreɪəl/','背叛、出卖；辜负信任的行为',
 '原本托付给你的东西，被你反着对待，别人感到的不只是失败，而是信任被伤害，这就是 betrayal 的重心。',
 'betray + -al → betrayal，保留 y。-al 在这里把行为、结果命名成名词，不形成与托盘有关的性质。',Bt+[['betray + -al → betrayal','背叛行为；信任被辜负的结果']],
 'a betrayal of trust 辜负信任；a sense of betrayal 被背叛的感觉；an act of betrayal 一次背叛行为。',
 'a betrayal of trust；a sense of betrayal。',
 'betrayal 比普通 disappointment 失望多信任、忠诚遭破坏的成分；不只是任何没达到预期。',
 ('Publishing the private letter felt like a betrayal.','公开私人信件让人感到像是背叛。'),('The novel centres on a betrayal of trust.','小说围绕一次信任被辜负的事件展开。'))
Tr=[['拉丁 transitio，接 transire 走过 → 法语 transition','从一边、一种状态走到另一边'],['英语 transition → transitional','转变、过渡；过渡相关性质']]
W('transition','/trænˈzɪʃən/','过渡、转变；转入、过渡到',
 '不是只看旧状态、新状态两个点，还看中间怎么换过去。学生走入职场、新系统替换旧系统，都有 transition。',
 '借法语 transition，上接拉丁 transitio、transire 走过；trans- 越过与 ire 走的材料，后来用于状态变化。',Tr,
 'a transition from A to B 从 A 到 B 的转变；a smooth transition 平稳过渡；transition to a new system 过渡到新系统。',
 'a smooth transition；transition from ... to ...。',
 'transition 重阶段之间的转换，translation 是翻译，transaction 是交易；相似开头不能混成同一个名词。',
 ('The transition from school to work can take time.','从学校到职场的转变可能需要时间。'),('The team planned a smooth transition to the new system.','团队计划平稳过渡到新系统。'))
W('transitional','/trænˈzɪʃənəl/','过渡的；转变时期的',
 '还不是最终稳定形态，而是在从旧走到新，便是 transitional。可以修饰时期、安排、风格。',
 'transition + -al → transitional；-al 把过渡过程名词变成相关性质。',Tr+[['transition + -al → transitional','处于或服务于过渡的性质']],
 'a transitional period 过渡期；transitional arrangements 过渡安排；a transitional stage 过渡阶段。',
 'a transitional period；transitional arrangements。',
 'transitional 过渡的，traditional 传统的；一个在描述改变阶段，一个在描述传统关系。',
 ('The organisation is in a transitional period.','机构正处于过渡期。'),('These are transitional arrangements rather than the final design.','这些是过渡安排，还不是最终设计。'))
W('empirical','/ɪmˈpɪrɪkəl/','经验性的；以观察、实验为依据的',
 '先实际看、测、试，再用观察结果支持判断，是 empirical。不是只在脑中推，也不是随便一句“我凭感觉觉得”。',
 '希腊 empeirikos 有经验的，接 en- 在其中 + peira 试验、经历，经拉丁 empiricus 等材料再形成 empirical，带 -al 性质尾。',
 [['希腊 en- + peira → empeiria、empeirikos','在实际尝试中获得经验；有经验的'],['拉丁 empiricus 等 + -al → empirical','源于经验、可由观察试验检验的']],
 'empirical evidence 实证证据；an empirical study 实证研究；empirical data 实测、观察数据。研究也可把理论与实证结合。',
 'empirical evidence；an empirical study；empirical data。',
 'empirical 与 theoretical 区分证据、方法侧重，不是宣布理论没用；一次主观印象也不自动代表充分实证。',
 ('The theory needs empirical support.','理论需要实证支持。'),('The study combines a model with empirical data.','研究把模型与实测数据结合起来。'),sources=['https://en.wiktionary.org/wiki/empirical#English','https://www.etymonline.com/word/empirical','https://www.oxfordlearnersdictionaries.com/definition/english/empirical'])
W('cerebral','/səˈriːbrəl/〔亦 /ˈserəbrəl/〕','脑的、大脑的；偏理智、费思考的',
 '医学里说脑相关；艺术评论里还可说作品偏思考、理智，得动脑去理解，而不是主要靠直接情感冲击。',
 '接拉丁 cerebrum 脑的材料与 -al，历史也见法语 cérébral 对应。不是 cereal 谷物随便多加一个 b。',
 [['拉丁 cerebrum 脑 → 相应性质形式','脑相关的命名材料'],['英语 cerebral','脑的；比喻偏思维、理智的']],
 'cerebral blood flow 脑血流；the cerebral cortex 大脑皮层；a cerebral novel 偏理智、费思考的小说。',
 'the cerebral cortex；cerebral blood flow；a cerebral novel。',
 'cerebral 比喻义不单纯等于智商高；cereal 是谷物、早餐谷物食品，两词来源不同。',
 ('The diagram labels the cerebral cortex.','图中标出了大脑皮层。'),('The review describes the film as cerebral and demanding.','评论说电影偏理智，也很考验理解力。'),sources=['https://en.wiktionary.org/wiki/cerebral#English','https://www.oxfordlearnersdictionaries.com/definition/english/cerebral'])
Ab=[['拉丁 abdomen → 法语、英语 abdomen','腹部名，更早具体来源未定'],['拉丁词干 abdomin- + -alis → abdominal','采用腹部词干的相关形容词']]
W('abdomen','/ˈæbdəmən/','腹部；腹腔〔依语境〕',
 '胸部下面、骨盆上面这一片身体区域，是常见人体语境里的 abdomen。不是胃这个器官单独改了一个名字。',
 '借法语、拉丁 abdomen；拉丁格变化给出 abdomin- 词干，供 abdominal 等派生。更早可能与隐藏等词有关，但不当作确定拆分。',Ab,
 'the lower abdomen 下腹部；the upper abdomen 上腹部；the abdomen of an insect 昆虫腹部，动物学范围另按结构。',
 'the lower abdomen；the upper abdomen。',
 'abdomen 是区域、腔体名称，stomach 主要是胃，也会口语泛说肚子；正式解剖语境不可随意合并。',
 ('The illustration shows the organs in the abdomen.','插图展示了腹部里的器官。'),('The insect has a long abdomen.','这只昆虫的腹部很长。'))
W('abdominal','英 /æbˈdɒmɪnəl/；美 /æbˈdɑːmənəl/','腹部的；腹腔相关的',
 'abdomen 是腹部，abdominal 把肌肉、疼痛、腔体等与腹部联系起来。形容词本身不说明某种疼痛的具体原因。',
 '接新拉丁 abdominalis：abdomin- 是 abdomen 的历史词干，接 -al 相应性质尾；不凭空插一个 n 当记忆口诀。',Ab,
 'abdominal muscles 腹肌；the abdominal cavity 腹腔；abdominal pain 腹痛；abdominals 也可简称腹肌。',
 'abdominal muscles；the abdominal cavity；abdominal pain。',
 'abdominal 指腹部相关，cerebral 指脑相关；词尾相同只交代性质，不把身体部位合并。',
 ('The chart labels the abdominal muscles.','图表标出了腹肌。'),('The article explains the structure of the abdominal cavity.','文章解释了腹腔结构。'),sources=['https://en.wiktionary.org/wiki/abdominal#English','https://www.cancer.gov/publications/dictionaries/cancer-terms/def/abdominal'])
W('cereal','英 /ˈsɪəriəl/；美 /ˈsɪriəl/','谷类作物、谷物；早餐谷物食品',
 '麦、稻、燕麦等为人提供可食谷粒，属于 cereal crops；早餐碗里的加工谷物食品也常直接叫 cereal。',
 '借法语 céréale，上接拉丁 Cerealis 与农业女神 Ceres 有关的，再用于谷物。不是 cerebral 脑的缩略，也不从英语 serial 连续的借义。',
 [['罗马农业女神 Ceres → 拉丁 Cerealis','与农业、谷物有关的性质'],['法语 céréale → cereal','谷类作物、谷粒；后来早餐谷物食品']],
 'cereal crops 谷类作物；breakfast cereal 早餐谷物食品；a bowl of cereal 一碗早餐麦片等。',
 'cereal crops；breakfast cereal；a bowl of cereal。',
 'cereal 谷物与 serial 连续的常同音；cerebral 脑的又是近形异源词，不能用一种词根讲三者。',
 ('She had a bowl of cereal for breakfast.','她早餐吃了一碗谷物食品。'),('Wheat is an important cereal crop.','小麦是一种重要谷类作物。'))
W('portrayal','英 /pɔːˈtreɪəl/；美 /pɔːrˈtreɪəl/','描绘；塑造、演绎；所呈现的形象',
 '演员怎么把角色演出来，文章怎么把某群人写出来，这种呈现和呈现出来的形象，都可叫 portrayal。',
 'portray + -al → portrayal，保留 y；这里名词尾形成描绘行为、结果，不是与某种 tray 托盘有关的形容词。',
 [['法语 portraire 等描绘材料 → portray','描绘、表现，现代也用于表演'],['portray + -al → portrayal','描绘过程、塑造出的形象']],
 'a portrayal of a character 角色演绎；an accurate portrayal 准确描绘；media portrayal 媒体呈现。',
 'a portrayal of；an accurate portrayal。',
 'portrayal 侧重如何呈现，reality 是实际情况；生动形象的 portrayal 仍可能不准确。',
 ('Her portrayal of the character won praise.','她对角色的演绎赢得了称赞。'),('The article challenges the usual portrayal of the town.','文章挑战了对这座小镇惯常的描绘。'))
Pi=[['古法语 pivot → 英语 pivot','转轴、铰链轴等，更早来源有争论'],['pivot + -al → pivotal','枢轴相关；转为关键作用的比喻']]
W('pivot','/ˈpɪvət/','支点、枢轴；转动、转向；关键点',
 '门绕着轴转，计划也能围绕一个关键点改变方向。pivot 既可指支点，也能作转动、转向的动作。',
 '借古法语 pivot 等枢轴名，远源未定；现代商业 pivot 改变方向，是转轴动作的比喻。',Pi,
 'turn on a pivot 围绕支点转；pivot towards a new approach 转向新做法；a central pivot 核心支点。',
 'turn on a pivot；pivot towards。',
 'pivot 转向，不保证完全抛弃原有一切；也不等于任何细微调整都构成战略转型。',
 ('The frame turns on a central pivot.','框架绕中心支点转动。'),('The team pivoted towards a simpler approach.','团队转向了更简单的做法。'))
W('pivotal','/ˈpɪvətəl/','关键的、起枢纽作用的',
 '像一个轴影响整个东西往哪转，pivotal 就是能左右局面、结果的关键作用。不是普通“有一点帮助”。',
 'pivot + -al → pivotal，性质尾；先有枢轴关联，再有至关重要的比喻用法。',Pi+[['pivot + -al → pivotal','像枢轴一样影响整体方向、结果']],
 'a pivotal role 关键作用；a pivotal moment 关键时刻；a pivotal decision 关键决定。',
 'a pivotal role；a pivotal moment。',
 'pivotal 比普通 relevant 相关更强：相关未必关键；它也不自动等于事件唯一原因。',
 ('Her advice played a pivotal role in the project.','她的建议在项目中发挥了关键作用。'),('The discovery marked a pivotal moment in the investigation.','这项发现成为调查中的关键转折点。'))
Ce=[['拉丁 caerimonia、caeremonia 等 → ceremony','神圣礼仪、敬意等名称；更早来源未定'],['拉丁 caerimonialis 等 → ceremonial','仪式相关；用于礼仪、象征的性质']]
W('ceremony','英 /ˈserəməni/；美 /ˈserəmoʊni/','仪式、典礼；礼节',
 '通过一套安排好的动作、话语，郑重标记毕业、结婚、纪念等事情，是 ceremony。它不只限宗教场合。',
 '接拉丁 caerimonia 等礼仪、敬意材料，经中古英语等延续；更早来源不确定，不硬编一个地方名起源。',Ce,
 'a graduation ceremony 毕业典礼；a wedding ceremony 婚礼仪式；without ceremony 不拘礼节地。',
 'a graduation ceremony；a wedding ceremony；without ceremony。',
 'ceremony 是仪式，celebration 是庆祝；哀悼、纪念仪式也可 ceremony，不必都是欢庆。',
 ('The graduation ceremony began at ten.','毕业典礼十点开始。'),('The town held a ceremony to remember the event.','镇上举行仪式，纪念那件事。'))
W('ceremonial','英 /ˌserəˈməʊniəl/；美 /ˌserəˈmoʊniəl/','仪式的；礼仪性、象征性的',
 '服装是典礼穿的，职责主要用于礼仪、象征，都可以说 ceremonial。它并不自动意味着毫无价值。',
 '接拉丁 caerimonialis 等相应形容词，现代与 ceremony + -al／-ial 材料对应；不是把 ceremony 的 y 原样后面直接拼 al。',Ce,
 'ceremonial dress 礼服；a ceremonial role 礼仪性职务；ceremonial duties 礼仪职责。',
 'ceremonial dress；a ceremonial role。',
 'ceremonial 强调仪式关联，ceremonious 常强调举止拘礼、郑重；固定搭配仍看实际用法。',
 ('The mayor has several ceremonial duties.','市长承担几项礼仪职责。'),('The display includes ceremonial clothing from different periods.','展品包括不同时期的礼仪服装。'))

W('correctional','/kəˈrekʃənəl/','矫正的；与刑罚矫正、监禁或改造有关的',
 'correction 本有纠正的意思；correctional 在机构、人员名称里，常进入关押、改造违法者的固定用法。不是每一处拼写纠错都这么叫。',
 'correction + -al → correctional；性质尾接在纠正、矫正名词上，现代刑罚机构等语境很常见。',
 [['correct 纠正 → correction','纠正的行为、结果'],['correction + -al → correctional','矫正相关；刑罚矫正机构等固定性质']],
 'a correctional facility 矫正机构、监狱等；a correctional officer 惩教、矫正人员；correctional services 矫正相关服务。',
 'a correctional facility；a correctional officer。',
 'corrective 通常更宽地说纠正问题的；correctional 在现代常有刑罚矫正领域的固定搭配，不能随意互换全部。',
 ('The report examines education in correctional facilities.','报告考察矫正机构里的教育。'),('The course introduces the work of correctional officers.','课程介绍矫正人员的工作。'))
W('incremental','/ˌɪŋkrəˈmentəl/','逐步增加的；增量的',
 '不一次全换完，而是一小步一小步添、改，就是 incremental 的典型感觉。数据处理里也可只处理新增、变化的部分。',
 'increment 增量 + -al → incremental；increment 接拉丁增加、生长的材料。不是 increase 的拼写随意截短再接 mental 心理的。',
 [['拉丁 incrementum 等 → increment','增加量、一步增量'],['increment + -al → incremental','按增量、分步骤推进的性质']],
 'incremental change 渐进变化；incremental improvements 逐步改进；an incremental update 增量更新。',
 'incremental change；incremental improvements；an incremental update。',
 'incremental 说明按增量、步骤推进，不保证每次变化都微不足道，也不等于所有渐进方案都慢。',
 ('The team made incremental improvements each week.','团队每周都作出逐步改进。'),('The system processes an incremental update instead of rebuilding every record.','系统处理增量更新，无需重建每条记录。'))
Fu=[['拉丁 fungus 蘑菇 → 英语 fungus','菌类名称，现代扩大为真菌类群成员'],['fungus 的 fung- 词干 + -al → fungal','真菌相关的性质形容词']]
W('fungus','/ˈfʌŋɡəs/','真菌；霉菌、蘑菇等真菌类群成员',
 '蘑菇、酵母、霉菌看着差别大，都有成员属于真菌。fungus 不是所有微小生物或所有污斑的统称。',
 '借拉丁 fungus 蘑菇；现代科学概念扩展到真菌类群。复数常用 fungi，也有 funguses；派生形容词用 fung- 词干。',Fu,
 'a fungus growing on wood 木头上生长的真菌；fungi in the soil 土壤真菌；a type of fungus 一种真菌。',
 'a type of fungus；fungi in the soil。',
 'fungi 是现代独立类群，不能把所有真菌都定义成植物；bacteria 细菌也是另一类生物。',
 ('A fungus was growing on the fallen branch.','倒下的树枝上长着一种真菌。'),('The book describes several fungi found in woodland.','书中描述了几种林地里的真菌。'),sources=['https://en.wiktionary.org/wiki/fungus#English','https://www.merriam-webster.com/dictionary/fungus'])
W('fungal','/ˈfʌŋɡəl/','真菌的；由真菌引起或与之有关的',
 'fungus 是真菌，fungal 把生长、孢子、感染等与真菌相连。它是性质词，不是复数菌名。',
 'fungus 去拉丁词尾 -us，采用 fung- + -al → fungal；不是整个 fungus 原样直接拼上 al。',Fu+[['fung- + -al → fungal','与真菌有关的性质']],
 'fungal growth 真菌生长；fungal spores 真菌孢子；a fungal infection 真菌感染。',
 'fungal growth；fungal spores。',
 'fungal 不是所有 microbial 微生物相关的通用替代；微生物还包括别的类群。',
 ('The study tracks fungal growth on different materials.','研究追踪不同材料上的真菌生长。'),('The diagram shows how fungal spores spread.','图解展示真菌孢子如何传播。'))
W('feral','/ˈferəl/〔亦有 /ˈfɪərəl/〕','野化的；野性的、未驯服的',
 '家养动物的后代在野外自行生活，是 feral 的典型场景。也可能是在野外出生，重点是这条谱系、生活状态，不要求每只都曾进过家门。',
 '接拉丁 fera 野兽、ferus 野的等材料与 -al，相应形式也可经法语、拉丁借入。不是 fear 害怕加 l。',
 [['拉丁 fera、ferus 的野兽、野性材料','未驯、野生的性质'],['feral 的现代使用','野化动物、未驯服状态，也有较宽野性义']],
 'a feral cat 野化、野生化猫；feral populations 野化种群；feral animals 野化动物。',
 'a feral cat；feral populations。',
 'feral 与 wild 有重叠，前者常强调家养、圈养祖先后的野化；并非所有野生动物都需要叫 feral。',
 ('The researchers counted feral cats near the old farm.','研究者统计了旧农场附近的野化猫。'),('The article examines how feral populations become established.','文章考察野化种群如何形成。'))
Ar=[['希腊 arkheion 公共政务建筑、档案 → 拉丁 archivum','政府文书及其存放处'],['法语等 → archive、archives','档案、保存处；归档'],['archive + -al → archival','档案相关或适合长期保存的性质']]
W('archive','英 /ˈɑːkaɪv/；美 /ˈɑːrkaɪv/','档案、档案库；归档、存档；归档文件',
 '把不常用但值得保留的材料整理存好，方便以后查，就是 archive。档案可以是纸张，也可以是数字记录。',
 '接法语等档案词，上接拉丁 archivum、希腊 arkheion 公共政务建筑和文书材料；名词常见复数 archives，后来作归档动词。',Ar,
 'the city archives 城市档案；archive old emails 归档旧邮件；an archive file 归档文件；a digital archive 数字档案库。',
 'a digital archive；archive old emails；the city archives。',
 'archive 归档通常保留内容，delete 删除则移除；归档文件也不保证一定经过压缩。',
 ('The letters are kept in the city archive.','信件保存在城市档案库里。'),('She archived the old project files.','她把旧项目文件归档了。'),sources=['https://en.wiktionary.org/wiki/archive#English','https://www.etymonline.com/word/archive'])
W('archival','英 /ɑːˈkaɪvəl/；美 /ɑːrˈkaɪvəl/','档案的；适合档案保存的',
 '档案里的资料是 archival material；适合保存材料的纸盒、纸张也会称 archival。前者说来源、用途，后者说保存品质。',
 'archive 去末尾 e 加 -al → archival，常见读音重音后移。不是 arch 建筑拱门加一个不相关的 ival。',Ar,
 'archival material 档案材料；archival research 档案研究；archival paper 适合保存用途的纸。',
 'archival material；archival research；archival paper。',
 'archival paper 表适合保存的品质、用途，不保证永远不变；archival material 也不要求每件都印在特制纸上。',
 ('The historian worked with archival material.','历史学家研究档案材料。'),('The photographs are stored in archival boxes.','照片存放在档案保存盒里。'))
Ao=[['a- 加强 + rouse 唤起 → arouse','唤醒、使活跃的动作材料'],['arouse + -al → arousal','唤醒、激起的过程和状态']]
W('arouse','/əˈraʊz/','激起、唤起；使醒来；引起性兴奋',
 '原来没起反应，后来好奇、怀疑、兴趣被叫醒，是 arouse 的常见画面。也能直说把人从睡眠中唤醒。',
 'a- 加强 + rouse 唤起、使起来 → arouse；与 arise 出现、起身不同，不能随意互换两个动作的方向。',Ao,
 'arouse curiosity 激起好奇；arouse suspicion 引起怀疑；arouse interest 激发兴趣；arouse someone from sleep 唤醒某人。',
 'arouse curiosity；arouse suspicion；arouse interest。',
 'arouse 常是使别人、某种反应被唤起；arise 常是事情自己出现。Problems arise 不等于 problems arouse。',
 ('The unusual sound aroused her curiosity.','不寻常的声音激起了她的好奇。'),('His vague answer aroused suspicion.','他含糊的回答引起了怀疑。'))
W('arousal','/əˈraʊzəl/','唤醒、唤起；身心激活状态；性唤起',
 '从低反应到警觉、情绪活跃，是较宽的 arousal；某些语境专指性唤起，要看 emotional、physiological、sexual 等限定。',
 'arouse 去末尾 e 加名词尾 -al → arousal；不是形容词有唤醒性质的某某物，而是过程、状态名。',Ao+[['arouse + -al → arousal','被唤醒、激起的过程和状态']],
 'emotional arousal 情绪唤起；physiological arousal 生理激活；arousal from sleep 从睡眠中醒来。',
 'emotional arousal；physiological arousal；arousal from sleep。',
 'arousal 不只性语境，研究注意、情绪、睡眠时也常见；与 arrival 到达的拼写、意思不同。',
 ('The study measured changes in physiological arousal.','研究测量了生理激活状态的变化。'),('The textbook discusses arousal from sleep.','教材讨论从睡眠中醒来的过程。'),sources=['https://en.wiktionary.org/wiki/arousal#English','https://www.merriam-webster.com/dictionary/arousal'])
Rb=[['古法语 re- + bouter 推、顶 → rebut','推回、驳回的动作材料'],['rebut + -al → rebuttal','提出相反论证、证据的反驳行为或内容']]
W('rebut','/rɪˈbʌt/','反驳；用相反理由、证据回应',
 '别人把一个说法推过来，你拿理由、证据推回去，是理解 rebut 的画面。重点不只是大声说不。',
 '借古法语 rebuter、rebouter 等，re- 回 + bouter 推、顶。后来的论证反驳义保留推回的方向。',Rb,
 'rebut an argument 反驳论证；rebut a claim 反驳主张；rebut an allegation 反驳指控。',
 'rebut an argument；rebut a claim。',
 'deny 可以只说不承认，rebut 通常更强调拿相反理由、证据回应；是否说服人仍看论证本身。',
 ('She rebutted the claim with records from the archive.','她用档案记录反驳了那个说法。'),('The article rebuts the main argument point by point.','文章逐点反驳了主要论证。'))
W('rebuttal','/rɪˈbʌtəl/','反驳；反驳陈述、回应',
 'rebut 是动作，rebuttal 可以是这一轮反驳，也可以是你写出来、说出来的回应内容。',
 'rebut + -al，末音节重读、短元音后双写 t → rebuttal。名词尾不把它变成与反驳有关的形容词。',Rb+[['rebut + -al → rebuttal','反驳行为、陈述或论证内容']],
 'a detailed rebuttal 详细反驳；a rebuttal to the claim 对说法的反驳；publish a rebuttal 发表反驳回应。',
 'a rebuttal to；a detailed rebuttal。',
 'rebuttal 不等于任何 reply 回复；它通常有回应、反对某个具体论点的方向。',
 ('The journal published her rebuttal.','期刊发表了她的反驳回应。'),('He prepared a detailed rebuttal to the criticism.','他对批评准备了详细反驳。'))
W('upheaval','/ʌpˈhiːvəl/','剧变、动荡；隆起〔地质等〕',
 '像把原来稳定的地面从下面掀起来，原有秩序一下被打乱，就是社会、生活里 upheaval 的感觉。',
 'upheave 向上抬、掀起 + -al，去末尾 e → upheaval。upheave 又由 up + heave 举、抬组成；不从 heaven 天空变形解释。',
 [['up + heave → upheave','从下面向上抬、掀起'],['upheave + -al → upheaval','地质隆起；比喻强烈动荡、剧变']],
 'social upheaval 社会剧变；political upheaval 政治动荡；a period of upheaval 动荡时期。',
 'social upheaval；a period of upheaval。',
 'upheaval 比普通 change 变化强，常带结构被打乱、需要重新适应的感觉，不只例行小调整。',
 ('Moving countries caused a major upheaval in their lives.','迁居国外使他们的生活发生重大变化。'),('The book describes a period of social upheaval.','书中描写了一段社会剧变时期。'))
Si=[['拉丁 situs 位置 → situare、situatio → 法语 situation','放置、所处位置'],['英语 situation → situational','处境、情况；特定情境相关性质']]
W('situation','/ˌsɪtʃuˈeɪʃən/〔亦 /ˌsɪtjuˈeɪʃən/〕','情况、局面；处境；位置〔较正式〕',
 '不是一件孤立东西，而是此刻各种条件凑成的局面。人像站在这个局面里，所以也译处境。',
 '经法语接拉丁 situatio、situare、situs 等位置材料；现代与 situate 使处于的词族对应，不拆成 sit 坐 + 任意 uation。',Si,
 'the current situation 当前情况；a difficult situation 困难处境；deal with the situation 应对局面。',
 'the current situation；a difficult situation。',
 'situation 是当下条件、处境，location 更直接说地理位置；两个词的具体义有重叠，却不总能互换。',
 ('We need to understand the situation before deciding.','作决定前，我们需要了解情况。'),('She handled the difficult situation calmly.','她冷静处理了困难局面。'))
W('situational','/ˌsɪtʃuˈeɪʃənəl/','情境的；由具体处境、情况决定的',
 '不是说一个人永远如此，而是当前环境、条件让反应变成这样，可以用 situational。',
 'situation + -al → situational；性质尾保留整词的情境、处境材料，不加一个独立词 national。',Si+[['situation + -al → situational','特定情境相关、依情况而变的']],
 'situational factors 情境因素；situational awareness 情境感知；situational constraints 具体环境的限制。',
 'situational factors；situational awareness。',
 'situational 强调环境条件，dispositional 常强调较稳定倾向；不同解释角度，不一定二选一。',
 ('The study considers several situational factors.','研究考虑了几种情境因素。'),('Good situational awareness helps the team notice changes.','良好的情境感知帮助团队察觉变化。'))
W('perceptual','/pəˈseptʃuəl/；美 /pərˈseptʃuəl/','知觉的；与感知有关的',
 '眼睛、耳朵等接收信息，脑中组织成形状、声音、距离的感受，这一层面可叫 perceptual。',
 '接拉丁 perceptus 等感知、领会材料 + -al；现代可与 perception 知觉对照。并非每个 -ual 都是把现代名词随意删尾后新造。',
 [['拉丁 percipere、perceptus 等','接收、抓住，走向领会、感知'],['相关词干 + -al → perceptual','与知觉、感知过程有关的性质']],
 'perceptual skills 感知能力；perceptual differences 知觉差异；a perceptual illusion 知觉错觉。',
 'perceptual skills；perceptual differences。',
 'perceptual 不等于 perceptive 敏锐、有洞察力；一个说明领域，一个评价察觉能力。',
 ('The task tests perceptual skills using shapes and colours.','任务用形状、颜色测试感知能力。'),('The article describes a perceptual illusion.','文章描述了一种知觉错觉。'))
Ca=[['希腊 kategoria、kategorein 等说出、指控材料','进入逻辑陈述、范畴命名'],['法语、拉丁相应形式 → category；categoricus + -al 等 → categorical','类别；分类性质或明确断言性质']]
W('category','英 /ˈkætəɡəri/；美 /ˈkætəɡɔːri/','类别、种类；范畴',
 '按一个规则把相近东西放在同一个格子里，这个格子就是 category。规则变了，同一件东西也可能换分类。',
 '经法语 catégorie、拉丁 categoria 接希腊 kategoria，远源是公开说出、断言、指控的材料，后来进入逻辑范畴和一般分类。不是 cat 猫加一个动物分类后缀。',Ca,
 'a category of books 一类书；fall into a category 属于一类；a broad category 大类；different categories 不同类别。',
 'fall into a category；a broad category。',
 'category 是类别，criterion 是分类标准；先有标准，再据此决定把东西放到哪类。',
 ('The books are divided into three categories.','这些书分为三类。'),('This example does not fit neatly into any single category.','这个例子不能很整齐地归入单一类别。'),sources=['https://en.wiktionary.org/wiki/category#English','https://www.etymonline.com/word/category'])
W('categorical','英 /ˌkætəˈɡɒrɪkəl/；美 /ˌkætəˈɡɔːrɪkəl/','明确断然的；类别的、分类的',
 'a categorical denial 是直接、明确、没有保留地否认；categorical data 则是按类别表示的数据。相同词有断言和分类两种常见领域。',
 '接晚期拉丁 categoricus 等 + -al；现代对应 category、categoric、categorical 的词族。-ic、-al 性质材料可叠加，不按英文 category 原样加 al。',Ca,
 'a categorical denial 断然否认；a categorical statement 明确断言；categorical data 类别数据。',
 'a categorical denial；categorical data。',
 'categorical 断然不等于说法已被证明正确；categorical data 也不是语气很强硬的数据。',
 ('She gave a categorical denial.','她作出了断然否认。'),('The table contains categorical data such as colour and type.','表格含有颜色、类型等类别数据。'))
W('methodical','英 /məˈθɒdɪkəl/；美 /məˈθɑːdɪkəl/','有条理、有步骤的；细致系统的',
 '不是想到哪做到哪，而是有顺序地一项项核对、推进，就是 methodical。可以仔细而快，不必磨蹭。',
 '希腊 methodikos 按方法办事，经拉丁等材料接 -al；与 method 方法对应。method 的重音在前，methodical 的常用重音移到中间。',
 [['希腊 methodos 方法、探求路径 → methodikos','按规则、方法进行的性质'],['相应拉丁、英语形式 + -al → methodical','有条理、细致系统的']],
 'a methodical approach 有条理的方法；a methodical search 有步骤的搜查；a methodical worker 做事细致有条理的人。',
 'a methodical approach；a methodical search。',
 'methodical 与 methodological 方法论相关的不同；前者评价做事方式，后者常说研究方法、方法论这一领域。',
 ('Her methodical notes made the problem easier to solve.','她有条理的笔记让问题更容易解决。'),('The team carried out a methodical check of every file.','团队按步骤细查了每个文件。'),sources=['https://en.wiktionary.org/wiki/methodical#English','https://www.oxfordlearnersdictionaries.com/definition/english/methodical'])
W('adversarial','英 /ˌædvəˈseəriəl/；美 /ˌædvərˈseriəl/','对抗性的；对手式相互挑战的',
 '双方像站在对面，各自提出主张、找对方的问题，是 adversarial 的关系。可以是一种制度、测试安排，不一定私人相互仇恨。',
 '通常由 adversary 对手 + -al，y 改 i → adversarial；adversary 上接拉丁转向相反一边的 adversus 等材料。',
 [['拉丁 adversus、adversarius 等 → adversary','相向、对立 → 对手'],['adversary + -al → adversarial','按对手关系展开的性质']],
 'an adversarial relationship 对抗关系；an adversarial approach 对抗式做法；adversarial testing 对抗式测试。',
 'an adversarial relationship；an adversarial approach。',
 'adversarial 描述对抗、挑战结构，不等于每个参与者都很 hostile 怀有敌意；也不等于 adverse 不利的所有用法。',
 ('The meeting became unnecessarily adversarial.','会议变得不必要地充满对抗。'),('The exercise uses an adversarial approach to test the argument.','练习用对手式挑战来检验论证。'))

R('A1771','相关性质形容词与动作、结果名词等多条历史','-AL：可能是与它有关，也可能是这件事及其结果','occupation → occupational；propose → proposal；betray → betrayal；archive → archival。先看词性，再看词尾。',
 '形容词把人、物放进某个领域：abdominal 腹部相关，fungal 真菌相关。名词则把动作、内容单独拿来谈：proposal 提案，rebuttal 反驳。结尾相同，句子里担当的工作不同。',
 '性质尾主要经法语、拉丁 -alis 等进入英语；动作名词尾有法语 -aille、拉丁相关形式及英语类推的发展。propose → proposal 去 e，betray → betrayal 留 y，rebut → rebuttal 双写 t；abdomen → abdominal 用 abdomin- 词干，fungus → fungal 用 fung-。categorical、methodical 还叠有 -ic 材料，不能每词只按最后两字母硬切。化学等专门命名另按领域，不混成统一性质义。',
 [['动作、内容与结果名词','propose · proposal · betray · betrayal · portray · portrayal · arouse · arousal · rebut · rebuttal · upheaval'],['工作、过渡、处境与关键作用','occupation · occupational · transition · transitional · situation · situational · pivot · pivotal · correctional · incremental'],['实证、思维、知觉与分类','empirical · cerebral · perceptual · category · categorical · methodical · adversarial'],['身体、真菌与野化性质','abdomen · abdominal · fungus · fungal · feral'],['仪式、谷物与档案','ceremony · ceremonial · cereal · archive · archival']],
 '-al 不保证形容词；proposal、betrayal 都是常见名词。cereal 谷物与 cerebral 脑的分源；methodical 有条理与 methodological 方法论相关分用；archival 不等于删除。',
 'The researcher used archival material to prepare a proposal and a methodical rebuttal.\n\n研究者用档案材料准备提案，并作出有条理的反驳。',
 'propose proposal occupation occupational betray betrayal transition transitional empirical cerebral abdomen abdominal cereal portray portrayal pivot pivotal ceremony ceremonial correction correctional increment incremental fungus fungal feral archive archival arouse arousal rebut rebuttal upheaval situation situational perception perceptual category categorical method methodical adversary adversarial national political personal original natural professional normal global traditional critical digital mental cultural technical environmental historical emotional internal educational typical chemical clinical musical approval universal formal electrical survival removal agricultural constitutional mechanical experimental classical conventional functional naval serial magical identical operational coastal congressional structural tropical colonial logical statistical electoral minimal rental viral ethical optical exceptional withdrawal dimensional continental disposal institutional denial instrumental seasonal tactical architectural optimal postal revival biblical aerial optional recreational territorial verbal confidential promotional behavioral fictional geographical governmental renewal organizational accidental developmental neural phenomenal spatial inspirational bacterial dismissal marginal tidal skeptical theatrical peripheral provisional numerical vocational nutritional computational nominal referral conditional cynical economical orbital societal doctoral mystical physiological sentimental bilingual sensational instructional procedural bridal monumental gravitational nautical supplemental frontal motivational existential graphical spectral topical mythical sectional ancestral appraisal contractual lyrical natal multicultural skeletal spherical directional longitudinal dysfunctional continual cylindrical ornamental causal hormonal primal incidental congenital sequential disapproval generational recital divisional orchestral relational rotational alphabetical pictorial anatomical preferential')
for k in ROOTS[-1]['exclude']:
    ROOTS[-1]['exclude'][k]='本页优先常用且性质、名词关系清楚的形式；其余词在基础词族继续整理，近形不凭结尾强并。'

if __name__=='__main__':save('continuation_20261030_ph',ROOTS,WORDS)
