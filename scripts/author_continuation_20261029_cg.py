"""Present, cover, further, town, speak: common words and etymological traps."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
def C(a,b,w,m):return [[a+'；'+b,'并列构词部分'],[w,m]]
P=[['拉丁语 praesens；相关 praesentāre','在眼前、在场；把东西放到眼前、呈上'],['经法语进入英语 present 词族','当前、在场；礼物；展示、提交']]
W('present','形容词、名词 /ˈprezənt/；动词 /prɪˈzent/','在场的；当前的；现在；礼物；展示、提交、颁给',
 '在眼前，可以是人正在这里、时间就是现在；把东西放到别人面前，又成了展示或送礼。',
 '形容词接拉丁语 praesens 在场的；动词经法语来自 praesentāre 放到面前。礼物名词与把东西呈送到人面前的表达有关。来路相关，但现代分两种重音。',P,
 'be present 在场；at present 目前；a birthday present 生日礼物；present a report 提交、展示报告。the present tense 是语法现在时，仍读 /ˈprezənt/。',
 'be present at；at present；a birthday present；present something to someone。',
 'present 在场、礼物的重音在前，present 提交、展示重音在后；currently 强调目前，present 动词强调呈给别人看。',
 ('All the students were present at the meeting.','所有学生都出席了会议。'),('She brought a small present for the host.','她给主人带了一份小礼物。'),('I’ll present the results tomorrow.','我明天展示结果。'),sources=['https://en.wiktionary.org/wiki/present#English','https://www.etymonline.com/word/present'])
W('presence','/ˈprezəns/','在场；存在；气场、风度',
 '某人或某物在那里；有些人一出现，就会让人明显感觉到他的存在感。',
 '经古法语 presence 来自拉丁语 praesentia 在场，与 present 的在场形容词分支相关。不是把现代 present 的 t 随便改成 ce。',P+[['拉丁语 praesentia → 法语 presence → 英语 presence','在场、存在；后也说显著存在感']],
 'in someone’s presence 当着某人的面；a strong presence 强烈存在感；the presence of water 有水存在。与礼物的 presents 同音时靠语境区分。',
 'in the presence of；make one’s presence felt；a calm presence；the presence of。',
 'presence 是在场、存在，presents 是 present 礼物的复数；presence of mind 是临危镇定、反应敏捷，不是礼物在脑中。',
 ('Her presence helped everyone feel calmer.','她在场让大家安心了些。'),('The test showed the presence of salt in the water.','检测表明水中有盐。'))
W('presently','/ˈprezəntli/','目前、现在；不久、稍后',
 '一个意思是眼下正在发生，另一个意思是过一小会儿；要靠上下文辨认。',
 'present + -ly，历史上有当下、立即、很快等相近时间用法，现代保留目前与不久两类常见意思。',P+[['present → presently','当下、随即等时间用法 → 目前；不久']],
 'is presently working 通常说目前正在工作；will join you presently 通常说过会儿就来。不是所有 presently 都能统一换成 now。',
 'presently working；presently available；will arrive presently。',
 'currently 一般明确是目前；soon 明确是不久。需要避免歧义时，直接选它们比依赖 presently 的双义更清楚。',
 ('She is presently working on a new book.','她目前正在写一本新书。'),('Please take a seat; the manager will join you presently.','请坐，经理稍后就来。'))
W('presentable','/prɪˈzentəbəl/','像样、整洁的；可以拿给人看的',
 '状态已经收拾到能见人、能摆到别人面前，不至于太乱或太粗糙。',
 'present 展示 + -able 可以……的，表示适合展示、见人的；重音随动词 present 一支。',P+[['present + -able → presentable','展示 → 能拿得出来、整洁像样的']],
 'make oneself presentable 收拾到能见人；a presentable draft 可以给人看的草稿。通常不要求极致漂亮，只要达到合适展示状态。',
 'look presentable；make the room presentable；a presentable draft。',
 'presentable 不等于 perfect 完美，也不等于 present 在场；可以是一份还可改进、但足以拿出来讨论的稿子。',
 ('Give me ten minutes to make the room presentable.','给我十分钟把房间收拾得像样些。'),('The draft is presentable, though it still needs editing.','草稿已经可以拿出来看，不过仍需编辑。'))
W('presenter','英 /prɪˈzentə/；美 /prɪˈzentər/','主持人；演示者、报告人',
 '把节目、内容或成果带到观众面前的人。',
 'present 展示、呈现 + -er，人名词；不从 present 礼物名词理解成送礼者这个通用称呼。',P+[['present + -er → presenter','呈现、展示 → 主持、报告的人']],
 'a television presenter 电视主持人，a conference presenter 会议报告人。具体是主持整场还是作一份报告，按场景看。',
 'a TV presenter；a radio presenter；a conference presenter。',
 'presenter 可以是主持人，也可以是报告人；audience 是受众，不能只看都在会议现场就混淆角色。',
 ('The presenter introduced the next guest.','主持人介绍了下一位嘉宾。'),('Each presenter has ten minutes to explain their research.','每位报告人有十分钟介绍研究。'))
W('presentation','/ˌprezənˈteɪʃən/','展示、报告；呈现方式；颁赠',
 '既可以是把成果讲给别人看的那一次活动，也可以是东西摆出来、表现出来的样子。',
 '经法语 presentation 接拉丁语 praesentātiō 展示、呈上，与 present 动词词族相关；现代可对应 present + -ation 的活动名词关系。',P+[['拉丁语 praesentātiō → 法语、英语 presentation','展示、呈上 → 报告、呈现方式、颁赠活动']],
 'give a presentation 作报告；food presentation 菜肴摆盘、呈现；the presentation of an award 颁奖。做 presentation 不一定使用幻灯片。',
 'give a presentation；a presentation on；visual presentation；the presentation of an award。',
 'presentation 是展示、报告及其呈现方式；slides 是幻灯片，二者不是同一范围的词。',
 ('She gave a short presentation on the new design.','她就新设计作了一个简短报告。'),('The restaurant pays attention to the presentation of each dish.','餐厅很注重每道菜的呈现。'))
W('represent','/ˌreprɪˈzent/','代表；描绘；象征；把……表现为',
 '让不在眼前的人、事或观点，通过一个人、图像或符号显现出来。这个画面可帮助记忆。',
 '经法语 représenter 来自拉丁语 repraesentāre 展现、使呈现等用法，与 present 词族相关。现代常用代表义，不等于每次都把东西再提交一次。',P+[['拉丁语 repraesentāre → 法语 représenter → 英语 represent','展现、表现 → 代表、描绘、象征']],
 'represent a company 代表公司；a symbol represents water 符号表示水；represent something as easy 把某事表现得很容易。表现方式未必客观准确。',
 'represent someone；represent a proportion；represent something as；a symbol represents。',
 'present 展示，represent 代表、描绘；re- 的历史作用不能强迫每个现代用法都译再次。',
 ('She will represent the school at the conference.','她将代表学校参加会议。'),('The blue line represents the river on the map.','地图上的蓝线表示河流。'))
R('B3774','在场、当前；呈上、展示；礼物与代表','PRESENT：在眼前，或把东西放到别人眼前','现代两种重音分别掌握；presence、presently 接在场分支，presentable、presenter、presentation 接展示分支，再对照 represent。',
 '拉丁语 praesens 在场与相关 praesentāre 呈上，经法语形成英语词族。礼物也有把东西呈送到别人面前的历史联系。',
 'present /ˈprezənt/ → presence、presently；present /prɪˈzent/ → presentable、presenter、presentation；represent 是代表、描绘；omnipresent 遍在另看。',
 [['当前、在场与存在','present · presence · presently · omnipresent'],['可展示状态、人物与活动','presentable · presenter · presentation'],['代表与描绘','represent']],
 'present 礼物与 presence 在场分清；presentation 不一定有幻灯片；presently 可是目前，也可是稍后。',
 'The presenter gave a presentation that represented the views of everyone present.\n\n报告人作了一份代表所有在场者观点的报告。',
 'present presence presently omnipresent presentable presenter presentation represent')
CV=[['拉丁语 cooperīre → 古法语 covrir / couvrir','覆盖、遮住'],['英语 cover 词族','覆盖；封面、掩护及其派生']]
W('softcover','英 /ˈsɒftkʌvə/；美 /ˈsɔːftkʌvər/','平装书；软封面的',
 '书的封面能弯，不像精装书那样有硬壳。',
 'soft 软 + cover 封面，形成按装订特征命名的复合词；cover 的封面义与覆盖书页的外层有关。',C('soft 软','cover 封面','softcover','软封面的；平装书'),
 'a softcover edition 平装版，a softcover book 平装书；也可作名词说一本平装书。纸张、售价不完全由这个词决定。',
 'a softcover edition；a softcover book；available in softcover。',
 'softcover 与 paperback 常有重叠；hardcover 是硬封面精装。不要把 softcover 理解成内容柔和、题材轻松。',
 ('I bought the cheaper softcover edition.','我买了较便宜的平装版。'),('The book is now available in softcover.','这本书现在有平装本了。'))
W('recover','英 /rɪˈkʌvə/；美 /rɪˈkʌvər/','恢复；取回、找回；另有重新覆盖义需分开',
 '常用意思是把失去的状态、东西或控制重新得到，不是往上盖一层。',
 '恢复、取回义经古法语 recovrer、盎格鲁法语相关形式来自拉丁语 recuperāre。它不能按现代 re- + cover 来解释。重新覆盖这一另一构词义可写 recover 或 re-cover，常与恢复义区分。',
 [['两条现代需分辨的来路：拉丁语 recuperāre 经法语；英语 re- + cover','前者为恢复、取回；后者为重新覆盖'],['英语 recover','常用恢复、找回；重新覆盖另义按语境区分']],
 'recover from a setback 从挫折中恢复；recover a lost file 找回丢失文件；recover one’s balance 恢复平衡。重新给沙发覆面这一义才真正按再覆盖理解。',
 'recover from；recover a file；recover one’s balance；recover the cost。',
 'recover 恢复义与 cover 覆盖只是形似陷阱；不能编成用被子盖住所以恢复健康的词源故事。',
 ('The team took several weeks to recover from the setback.','团队花了几周从挫折中恢复。'),('We managed to recover the missing document from a backup.','我们设法从备份中找回了丢失文档。'),sources=['https://en.wiktionary.org/wiki/recover#English','https://www.etymonline.com/word/recover'])
R('B3031','覆盖；外层、封面；附形似词 recover 辨析','COVER：盖住表面，封面保护里面','先学真正的 cover 词族；常用 recover 恢复放在最后作形似词辨析，不把它冒充覆盖的直接派生。',
 'cover 经法语来自拉丁语 cooperīre 覆盖。softcover、hardcover 说书封面；recover 恢复义另来自 recuperāre，经法语发展。',
 'cover → covering、coverage；uncover、undercover；hardcover ↔ softcover；最后单独分清 recover。',
 [['覆盖与范围','cover · covering · coverage'],['揭开、隐蔽与封面种类','uncover · undercover · hardcover · softcover'],['形似但常用恢复义另源','recover']],
 'softcover 平装，不说内容温柔；recover 恢复、取回不按再盖一次硬推。',
 'We uncovered a softcover copy and recovered the missing notes tucked inside.\n\n我们找到一本原先盖住的平装书，也找回了夹在里面的失踪笔记。',
 'cover covering coverage uncover undercover hardcover softcover recover')
FU=[['古英语 forþor / furþor → 中古英语 further','更向前、更远'],['英语 further','进一步；更远；额外的；促进']]
W('further','英 /ˈfɜːðə/；美 /ˈfɜːrðər/','更远；进一步；更多、额外的；促进',
 '沿着已经走的方向再往前，可以是距离、讨论深度，也可以是事情的发展。',
 '接古英语 forþor、furþor，属于向前、比较程度的旧形式，与 forth 等有历史关系。现代虽能作 far 的比较形式，却不能简单拆成 far + ther。',FU,
 'further away 更远；further discussion 进一步讨论；for further information 如需更多信息；further a cause 推动一项事业。',
 'further information；go further；further away；further one’s career；without further delay。',
 'further 可说实际距离和抽象进一步；farther 常突出距离，但实际用法有重叠。additional 可明确说额外的，却不能替代所有动词 further。',
 ('The report calls for further investigation.','报告呼吁进一步调查。'),('We walked further along the river.','我们沿河又往前走了一段。'),('The scholarship helped further her studies.','奖学金帮助她继续推进学业。'))
W('furthermore','英 /ˌfɜːðəˈmɔː/；美 /ˌfɜːrðərˈmɔːr/','而且；此外',
 '在已有理由上再加一条，把论证往前推一步。',
 'further 进一步 + more 更多，形成补充论点的连接副词。不是说物理距离又远了几米。',FU+[['further + more → furthermore','进一步 + 更多 → 此外、而且']],
 'Furthermore, ... 常在正式论述中引出同方向的补充信息。句首之后常有逗号，但它不像 and 那样在所有句式中都能直接顶替连词。',
 'Furthermore, ...；and furthermore；furthermore, it should be noted...。',
 'furthermore 补充支持点，however 则常转折；不要只因为都能放句首就忽略逻辑关系。',
 ('The room is too small. Furthermore, it has no windows.','房间太小，而且没有窗户。'),('The plan is affordable; furthermore, it can be completed quickly.','计划花费不高，而且能很快完成。'))
W('furtherance','英 /ˈfɜːðərəns/；美 /ˈfɜːrðərəns/','促进；推进',
 '把让一项事业、目标更向前这件事，作为一种正式的活动或目的来表达。',
 'further 促进 + -ance，形成活动、过程名词。现代多见正式固定短语，不是更远距离的普通计量。',FU+[['further + -ance → furtherance','促进 → 推进、促进这一过程']],
 'in furtherance of 为促进、为推进……；in furtherance of its aims 为实现、推进其目标。正式机构文件中常见。',
 'in furtherance of；the furtherance of education；in furtherance of a goal。',
 'furtherance 推进目标，不等于 further distance 更远距离；日常可按句子改用 to support、to advance 更直白。',
 ('The grant was awarded in furtherance of local education.','这笔资助用于促进当地教育。'),('The society organizes talks in furtherance of its cultural aims.','学会举办讲座，推进其文化目标。'))
R('B4136','更向前；进一步；促进','FURTHER：沿原方向再推进一点','可以在路上往前，也可以在知识、计划和论证上往前；further 还可直接当促进的动词。',
 'further 接古英语向前、比较程度形式，与 forth 等相关。它的现代比较功能不等于词源只是 far + ther。',
 'further → furthermore、furtherance；分别是补充论点与正式的促进名词。',
 [['距离、程度与推动','further'],['补充逻辑与促进过程','furthermore · furtherance']],
 'further information 更多信息；further a goal 推进目标；in furtherance of 为促进，偏正式。',
 'We need further information before taking the proposal any further.\n\n进一步推进提议前，我们需要更多信息。',
 'further furthermore furtherance')
TO=[['古英语 tūn → 中古英语 toun','围起来的地方、庄园、聚落等'],['英语 town','城镇；城区；当地居民整体']]
W('town','/taʊn/','城镇；城区；某地居民、当地生活',
 '从围起的一片生活空间，逐渐成为人们集中居住、来往的城镇。',
 '继承古英语 tūn，旧义包括围场、庄园、聚落，经中古英语发展为现代城镇义。地名里的 -ton 常与这个旧词有关，不能每次都当今天独立的 town 来随意拆。',TO,
 'a small town 小城镇；go into town 进城、去城里中心区域；out of town 不在城里、出城。town 与 city 的行政界线并非全世界同一标准。',
 'in town；out of town；go into town；the whole town；a small town。',
 'town 城镇，country 在对照里可指乡村；a county 是行政上的郡等单位，不是 town 的固定放大版。',
 ('She grew up in a small town by the river.','她在河边一座小城长大。'),('I’m going into town to collect a book.','我要进城取一本书。'))
W('township','/ˈtaʊnʃɪp/','镇区、乡镇等行政区域；南非历史中的特定居住区',
 '把一片地方组织成一个行政或社区单位；但这个名称在不同国家承载不同历史。',
 'town + -ship，旧后缀也能表示群体、区域等。现代不同地区把 township 用于不同形式的地区名称，不是镇上停着的一艘船。',TO+[['town + -ship → township','城镇区域、社区单位；地区制度中形成特定用法']],
 'an administrative township 行政镇区；南非语境中常涉及种族隔离历史所形成的城外居住区。不能只按一个国家的译名套所有材料。',
 'a rural township；township residents；a township boundary。',
 'township 的准确行政层级依国家、地区；不是所有地方都等于中文同一级的乡或镇。',
 ('The map shows the boundary of the township.','地图显示这个镇区的边界。'),('The documentary explores daily life in a South African township.','纪录片考察南非一处具有特定历史背景的城外居住区的日常生活。'))
W('midtown','/ˈmɪdtaʊn/','城市中部；城市中部的',
 '不从城边看，而是把位置放在城市中间这一带。',
 'mid- 中间 + town 城市，组成城市中部区域的名词、形容词。某些城市会把它作为具体街区名称。',C('mid- 中间','town 城市','midtown','城市中部地区'),
 'a midtown office 城中区办公室；a hotel in midtown 城市中部酒店。具体范围由城市惯例、地图划分决定，不是量出几何中点。',
 'a midtown hotel；a midtown office；live in midtown。',
 'midtown 城市中部，downtown 常指商业中心区，二者在不同城市可能重叠，也可能是不同街区。',
 ('Her office is in a busy midtown district.','她的办公室在繁忙的城市中部街区。'),('We stayed at a small hotel in midtown.','我们住在城市中部一家小酒店。'))
W('townsfolk','英 /ˈtaʊnzfəʊk/；美 /ˈtaʊnzfoʊk/','镇民；城里的居民们',
 '把这个地方的居民作为一群人来讲，有叙事、社区生活的感觉。',
 'town + 连接 -s- + folk 人们，形成复数、集合性的居民称呼。不是只指某一位居民。',C('town 城镇 + -s-','folk 人们','townsfolk','当地城镇居民这一群体'),
 'the local townsfolk 当地镇民；小说、地方报道中常见，通常与复数动词配合。',
 'the local townsfolk；among the townsfolk；townsfolk gathered。',
 'townsfolk 泛指居民，town council 是镇议会、地方管理机构；居民整体不等于管理者。',
 ('The townsfolk gathered to celebrate the restored bridge.','镇民们聚在一起庆祝桥梁修复。'),('Many townsfolk remembered the old railway station.','许多镇民还记得旧火车站。'))
W('townie','/ˈtaʊni/','城镇本地人；大学城中的当地居民，口语',
 '相对于外来的学生或游客，这个人是镇上生活的人。',
 'town + 非正式称人后缀 -ie，形成当地人、城里人的称呼；具体对比对象由环境决定。',TO+[['town + -ie → townie','城镇 → 本地居民、城里人这一口语称呼']],
 'students and townies 学生与当地居民；乡村语境也可能用 townie 说城里人。有时只是随便称呼，有时带轻蔑、对立感。',
 'students and townies；a local townie；describe oneself as a townie。',
 'townie 的语气不像 resident 那么中性；不要把大学城居民自动理解成没受教育或一定讨厌学生。',
 ('The café was popular with both students and townies.','咖啡馆既受学生欢迎，也受本地居民喜欢。'),('He jokingly called himself a townie who knew nothing about farming.','他开玩笑地说自己是个对农事一无所知的城里人。'))
R('B3266','城镇；城镇内部、居民与行政名称','TOWN：人们集中生活的一片地方','从围场、聚落的旧义到城镇，再分市内位置、居民称呼、行政和居住区名称。',
 'town 接古英语 tūn。township 的制度义与当地历史相关，midtown、downtown 的边界也不是全球统一。',
 'town → township；downtown ↔ midtown、hometown、townhouse、crosstown；居民 townsfolk、townie 相邻。',
 [['城镇、区域与市内位置','town · township · downtown · midtown · hometown · townhouse · crosstown'],['居民整体与口语称呼','townsfolk · townie']],
 'township 不同国家含义不同；townsfolk 是居民整体，townie 口语、有时带对立语气。',
 'The townsfolk planned a celebration in the old part of town.\n\n镇民们计划在老城区举行庆祝活动。',
 'town township downtown midtown hometown townhouse crosstown townsfolk townie')
SP=[['古英语 specan；更早相关形式常见 sprecan','说话；早期形式关系有不同分析'],['中古英语 speken → 英语 speak','说话、讲某语言、发言；过去 spoke，分词 spoken']]
W('speak','/spiːk/','说话；讲某语言；发言；表明',
 '把话说出来，可以是与人交谈、用某种语言，也可以代表一方正式表达。',
 '继承古英语 specan，经中古英语 speken 发展；更早与 sprecan 等形式的关系有不同历史分析，不硬编成固定去掉 r 规则。过去式 spoke，分词 spoken。',SP,
 'speak English 说英语；speak to someone 与某人讲话；speak for a group 代表群体发言。actions speak louder than words 行动比语言更有说服力。',
 'speak to；speak about；speak for；speak up；speak a language。',
 'speak a language 说某语言；say 侧重说出的内容，tell 常接告诉的对象。不能把三者所有宾语搭配直接互换。',
 ('Do you speak English?','你会说英语吗？'),('She spoke calmly about a difficult subject.','她平静地谈论了一个棘手话题。'),('I can’t speak for everyone in the group.','我不能代表组里每个人发言。'))
W('speaking','/ˈspiːkɪŋ/','口语、讲话；发言、说话相关的',
 '把说话能力或讲话过程拿出来谈；有时也是说明接下来从什么角度说。',
 'speak + -ing，可作分词、活动名词或形容词。speaking of...、generally speaking 等已经形成常见话语表达。',SP+[['speak → speaking','说话 → 口语、讲话活动及相关用法']],
 'public speaking 公众演讲，speaking skills 口语技能；generally speaking 一般说来；a speaking role 是有台词的角色，不是演技一定好的角色。',
 'speaking skills；public speaking；generally speaking；speaking of...。',
 'speaking 口语能力、过程，不等于 writing 书面写作；a speech 通常是一篇、一次具体演说或说话现象。',
 ('The course helps students improve their speaking skills.','课程帮助学生提升口语技能。'),('Generally speaking, the smaller classes allow more discussion.','一般来说，小班能进行更多讨论。'))
W('speaker','英 /ˈspiːkə/；美 /ˈspiːkər/','说话人；演讲者；扬声器；某些议会的议长',
 '人把话讲出来，设备把声音放出来，都可被叫 speaker；职务名又有固定历史用法。',
 'speak + -er，旧英语已有相应人名词。后来扩展到发声设备；首字母大写 Speaker 等可表示特定议会职务，不是所有讲话者都担任该职。',SP+[['speak → speaker','说话 → 说话、演讲的人；后也说发声设备、议会职务']],
 'a guest speaker 嘉宾演讲者，a native speaker 母语使用者，wireless speakers 无线音箱。根据句中人、设备或制度语境判断。',
 'a guest speaker；a native speaker；a keynote speaker；wireless speakers。',
 'speaker 母语使用者不自动是语言学专家；设备 speaker 是扬声器、音箱，不是 microphone 麦克风。',
 ('The guest speaker answered questions after the talk.','嘉宾演讲者在讲座后回答了问题。'),('The music was coming from a small speaker on the shelf.','音乐从架上一只小音箱里传出来。'))
SPEECH=[['古英语 spǣċ / sprǣċ → 中古英语 speche','话语、交谈、语言'],['英语 speech','讲话现象、说话能力；一篇演说；与 speak 是历史词族关系']]
W('speech','/spiːtʃ/','说话、言语；演说；一篇讲话',
 '既能说人发出、组织话语这件事，也能说面向听众的一次具体演讲。',
 '继承古英语 spǣċ、sprǣċ，经中古英语 speche 发展，与 speak 有历史词族关系。不是现代把 speak 的 k 随意改成 ch 就能造所有名词。',SPEECH,
 'freedom of speech 言论自由，give a speech 作演说；speech recognition 语音识别。能力、现象义常不可数，一篇演说可数。',
 'give a speech；a farewell speech；freedom of speech；speech recognition。',
 'speech 说出的语言、演说，language 还包括整个语言系统；a speech 不等于所有一段随口对话。',
 ('She gave a short speech at the opening ceremony.','她在开幕式上作了简短讲话。'),('The app uses speech recognition to turn spoken words into text.','应用使用语音识别把话语转换成文字。'))
W('speechless','/ˈspiːtʃləs/','说不出话的；惊讶、感动等导致无言的',
 '话到了嘴边却发不出来，可能是震惊、感动、气愤等情绪太强。',
 'speech + -less，没有话语、无法说话；旧英语已有对应 sprǣċlēas 等形式。现代常是暂时的情绪反应。',SPEECH+[['speech + -less → speechless','言语 → 无言、说不出话']],
 'leave someone speechless 让某人说不出话；speechless with surprise 惊得无言。并不每次都说明永久失去说话能力。',
 'leave me speechless；speechless with anger；stand speechless。',
 'speechless 是说不出话的状态，silent 是安静、不作声；一个人可以主动保持 silent，并没有 speechless。',
 ('The unexpected gift left her speechless.','意想不到的礼物让她感动得说不出话。'),('He stood speechless at the sight of the rebuilt house.','看见重建后的房子，他一时无言。'))
R('B2914','说话、讲语言；说话者、话语与演讲','SPEAK：把话说出来，角色与产物另看','speak 是动作，speaker 是说话者或发声设备；speech 是旧相关名词，不能当作一条现代万能拼写规则。',
 'speak 接古英语 specan，speech 接 spǣċ、sprǣċ 等旧形式，属于历史相关词族。过去 spoke、分词 spoken；更早形式关系不硬归成单一删音规则。',
 'speak → speaking、speaker；相关名词 speech → speechless；newspeak 看已经讲过的固定命名。',
 [['动作、活动与角色','speak · speaking · speaker'],['话语、演说与无言','speech · speechless · newspeak']],
 'speak English，give a speech；speaker 可是人也可是音箱；speechless 不一定是永久失语。',
 'The speaker’s speech left the audience speechless.\n\n演讲者的讲话让听众一时无言。',
 'speak speaking speaker speech speechless newspeak')
for item in WORDS:
 if item['word']=='presence':item['explanation']=item['explanation'].replace('与礼物的 presents 同音时靠语境区分。','与礼物的 presents 读音很近，靠语境区分。')
if __name__ == '__main__':save('continuation_20261029_cg',ROOTS,WORDS)
