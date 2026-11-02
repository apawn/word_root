"""Skill, draft, presentation and don: reasoning, drawing and parallel histories."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
S=[['古诺斯语 skil、skilja → 中古英语 skill 等','区分、辨别、理解'],['从判断到做得好','实践知识、方法、熟练能力'],['派生及需另辨的币名','skilled、skillful；shilling 旧钱币名，远源有争议，非现代 skill+-ing']]
W('skill','/skɪl/','技能、本领；熟练能力',
 '能看出细微差别，知道该怎么做，最后把事情做好；词的老底子是辨别、理解，不只一套手部动作。',
 '接古诺斯语 skil 辨别、理解，相关 skilja 分开、辨认，经中古英语到 skill。判断力逐步发展出实践能力义。',S,
 'communication skills 沟通技能，a practical skill 实用技能，skill in drawing 绘画技能，develop a skill 培养技能。',
 'communication skills；a practical skill；skill in；develop a skill。',
 'skill 可以具体一种技能而可数，也可泛说熟练能力；ability 能力更广，不一定已训练到熟练。',
 ('Cooking is a practical skill.','烹饪是一项实用技能。'),('The job requires patience and skill.','这份工作需要耐心和熟练本领。'))
W('skilled','/skɪld/','熟练的、有技能的；需要技能的',
 '人经过学习、经验能做得熟，是 skilled；工作本身要求专门能力，也可说 skilled work。',
 '现代可对应 skill + -ed 表有技能；更早 skill 也有懂得、熟知的动词，历史分词用法与熟练义相连。末尾 -ed 不多读一个音节。',S[:2]+[['skill 的名词、旧熟知动词与 -ed → skilled','有实践知识、熟练；工作要求专门技能']],
 'a skilled worker 熟练工，skilled at something 擅长某事，skilled in design 在设计方面熟练，skilled work 技能型工作。',
 'a skilled worker；skilled at；skilled in；skilled work。',
 'skilled worker 人有技能，skilled work 工作要求技能；用同一形容词，承载技能要求的对象位置不同。',
 ('She is skilled at repairing old radios.','她很擅长修理老收音机。'),('The project needs skilled workers.','项目需要熟练工人。'))
W('skillful','/ˈskɪlfəl/','有技巧的、巧妙熟练的',
 '不只具备资格，而是这次做得很有章法、技巧；常夸处理、表演、运用材料的熟练。',
 'skill + -ful，中古英语已有相应形式；英式常拼 skilful，读音、核心意思相同。-ful 不拼成末尾双 l 的 full。',S[:2]+[['skill + -ful → skillful；也拼 skilful','充满技巧、表现熟练']],
 'skillful handling 巧妙处理，skillful use of colour 巧妙运用颜色，a skillful performance 技巧娴熟的演出。',
 'skillful handling；skillful use of；a skillful performance。',
 'skilled 常描述人已具某领域本领，skillful 常夸具体做法有技巧；两者有重叠，别把侧重点当绝对禁用规则。',
 ('Her skillful handling prevented an argument.','她巧妙处理，避免了一场争执。'),('The painting shows skillful use of colour.','这幅画表现出娴熟的色彩运用。'))
W('shilling','/ˈʃɪlɪŋ/','先令〔货币单位名称，常见旧币史与文学〕',
 '读旧英国小说、看旧硬币会遇到的货币名；不是 someone is shilling 就在表演某项 skill。',
 '继承古英语 scilling 的日耳曼钱币名。更远有切分金属、盾形、声响等不同分析，后缀也有争议，不能确定成现代 skill + 进行时 -ing。',
 [['日耳曼旧钱币名 → 古英语 scilling → shilling','先令币名、计价单位'],['更远来源有不同解释','切分、声响等分析尚非唯一确定路线']],
 'a silver shilling 一枚银先令，two shillings 两先令，an old shilling coin 旧先令硬币。',
 'a silver shilling；two shillings；an old shilling coin。',
 'shilling /ʃ/，skill /sk/，都不要按现代同字母词根直接互换；各地各时期币值不同，本页只认名称。',
 ('The museum displayed an old shilling coin.','博物馆展出了一枚旧先令硬币。'),('The novel says the meal cost two shillings.','小说说那顿饭花了两先令。'),
 sources=['https://en.wiktionary.org/wiki/shilling#English','https://www.etymonline.com/word/shilling'])
R('B2521','分辨得出、理解得清，到实践做得好','SKILL：懂得怎么区分，才能知道怎么做好','skill → skilled、skillful；shilling 作为旧币名和不确定远源对照，不能按现代能力加 -ing。',
 'skillful/skilful 为常见英美拼法差异；skilled 人有技能，skilled work 工作需要技能。',
 'skil、skilja → skill；skill 相关旧动词、名词 + -ed → skilled；skill + -ful；shilling 另经 scilling 传下，远源有争议。',
 [['技能、熟练与技巧','skill · skilled · skillful'],['旧币名与远源对照','shilling']],
 'skill/ability 范围；skilled/skillful 侧重但可重叠；skilful 拼写；shilling 不作现代 skill 的进行时。',
 'The skilled artist showed skillful use of colour.\n\n熟练的艺术家展现了娴熟的色彩运用。','skill skilled skillful shilling')
D=[['古英语拉、拖词族 → 中古英语 draught、draght → draft','拉取、抽取；画出、写下的东西'],['不同对象的抽取、拉动','初稿、制图；空气流；抽选；从桶取酒、支取款项'],['拼写与派生','draft 与 draught 同源；drafty、draftsman、drafter；overdraft、updraft、downdraft']]
W('draft','英 /drɑːft/；美 /dræft/','草稿、初稿；起草；穿堂风、气流；抽选、征召；汇票等支取凭证',
 '把思路画、写出来是 draft 初稿；空气被引着流是 draft 气流；从人群抽出一些人，又可说 draft。先抓拉出、抽取的旧背景，再按对象选。',
 '与 draught 同源，接中古英语 draught、draght，较早联系 draw、drag 拉。draft 是随读音简化的拼法；英国一些气流、啤酒场景仍常 draught。',D,
 'a first draft 初稿，draft a letter 起草信，a cold draft 冷穿堂风，draft beer 生啤〔美式常写〕，a bank draft 银行汇票。',
 'a first draft；draft a letter；a cold draft；draft beer；a bank draft。',
 'draft/draught 同源拼法用途有地区差别；draft 初稿不等于已批准的 final version，技术、金融、体育词义都看对象。',
 ('She saved the first draft of the report.','她保存了报告初稿。'),('A cold draft came through the window.','一股冷风从窗户钻了进来。'),
 sources=['https://en.wiktionary.org/wiki/draft#English','https://www.etymonline.com/word/draft'])
W('draftsman','英 /ˈdrɑːftsmən/；美 /ˈdræftsmən/','制图员；文件起草人',
 '把设计变成准确图纸，或把条文、文件草拟出来的人。不是所有画画的人都一定担任这项工作。',
 'draft 图稿、草拟 + 连接成分 -s- + man 人；英式也见 draughtsman。drafter 是常见不带 man 的对应人物名。',D[:2]+[['draft + -s- + man → draftsman','制图、起草的人；也拼 draughtsman']],
 'an architectural draftsman 建筑制图员，a legal draftsman 法律文件起草人，a skilled draftsman 熟练制图员。',
 'an architectural draftsman；a legal draftsman；a skilled draftsman。',
 'draftsman 可制图、起草不同专业工作，drafts 的 s 不是说很多男人；现代职位也常用 drafter。',
 ('The draftsman prepared detailed plans of the building.','制图员绘制了建筑详细图纸。'),('The document was revised by an experienced legal draftsman.','文件由有经验的法律文件起草人修改。'))
W('drafter','英 /ˈdrɑːftə/；美 /ˈdræftər/','制图员；草稿、文件起草者',
 '负责把计划、条文、想法起成图稿或文字稿的人；-er 在这里是执行 draft 的人物。',
 'draft + -er，形成不带 man 的人物称呼，职业制图和一般起草场景都可用。',D[:2]+[['draft + -er → drafter','画图稿、起草文件的人']],
 'a technical drafter 技术制图员，the drafter of the proposal 提案起草者，a skilled drafter 熟练起草人。',
 'a technical drafter；the drafter of；a skilled drafter。',
 'drafter 是起草人，draft 是草稿、起草动作；某份草稿的 drafter 不一定就是最终批准人。',
 ('The drafter checked the measurements on the plan.','制图员检查了图纸尺寸。'),('She was the main drafter of the proposal.','她是提案的主要起草者。'))
W('drafty','英 /ˈdrɑːfti/；美 /ˈdræfti/','漏风的、穿堂风大的',
 '门窗关了还嗖嗖进冷风，房间就 drafty；不是书房里草稿太多。',
 'draft 气流 + -y，来自较早 draughty 拼法；英式常仍用 draughty，意思相同。',D[:2]+[['draft〔气流〕+ -y → drafty；也拼 draughty','有冷风穿过、漏风的']],
 'a drafty room 漏风房间，a drafty window 漏风窗户，a drafty old house 漏风老屋。',
 'a drafty room；a drafty window；a drafty old house。',
 'drafty 说空气流动、漏风，windy 泛说风大；a drafty room 可以屋外风并不很大却门窗密封差。',
 ('The old cottage was cold and drafty.','旧小屋又冷又漏风。'),('She moved her desk away from the drafty window.','她把书桌移离漏风的窗户。'))
W('updraft','英 /ˈʌpdrɑːft/；美 /ˈʌpdræft/','上升气流',
 '一股空气往上走，不是文章上面的那份草稿；鸟、滑翔等语境常讨论利用它获得升力。',
 'up- 向上 + draft 气流；英式也见 updraught。前半给方向，后半选气流义。',D[:2]+[['up- + draft → updraft','向上的气流']],
 'a strong updraft 强上升气流，warm updrafts 暖上升气流，ride an updraft 乘上升气流。',
 'a strong updraft；warm updrafts；ride an updraft。',
 'updraft 运动方向向上，warm 说温度；暖空气常与上升联系，但这个词本身先标方向。',
 ('The bird circled in an updraft.','鸟在一股上升气流中盘旋。'),('The diagram showed an updraft above the warm ground.','图中展示了暖地面上方的上升气流。'))
W('downdraft','英 /ˈdaʊndrɑːft/；美 /ˈdaʊndræft/','下降气流',
 '空气整体往下冲、下沉，方向与 updraft 相反；不是把草稿删掉往下移动。',
 'down- 向下 + draft 气流，英式也见 downdraught。',D[:2]+[['down- + draft → downdraft','向下流动、下沉的气流']],
 'a strong downdraft 强下降气流，a downdraft in a storm 风暴中的下降气流，rising air and downdrafts 上升空气与下降气流。',
 'a strong downdraft；a downdraft in a storm；warm updrafts and cold downdrafts。',
 'downdraft 说局部向下空气运动，不等于所有天气整体转冷；draft 在这里不是文稿。',
 ('The weather diagram marked a downdraft beneath the cloud.','天气示意图标出了云下的下降气流。'),('The lesson compared updrafts with downdrafts.','课程比较了上升气流与下降气流。'))
W('overdraft','英 /ˈəʊvədrɑːft/；美 /ˈoʊvərdræft/','账户透支；透支金额、透支额度〔按语境〕',
 '从账户支取的金额超过原有余额，是 overdraft；词里的 draft 沿支取分支，不是写了一份过长草稿。',
 'over- 超过 + draft 支取、支款相关用法。现代名词可指透支行为、已透支金额，也可指约定额度，按具体文件辨认。',D[:2]+[['over- + draft → overdraft','超过余额的支取 → 透支及相关金额、额度']],
 'an overdraft facility 透支服务安排，an overdraft limit 透支额度，an overdraft fee 透支费用。',
 'an overdraft limit；an overdraft fee；an overdraft facility。',
 'overdraft 不是账户里多出来的自有存款；limit、balance、fee 分别上限、余额、费用，不把同词所有金融用法当同一个数。',
 ('The statement showed an overdraft.','账单显示账户透支了。'),('The letter explained the overdraft limit.','信中解释了透支额度。'))
R('B3484','拉、抽、画出的旧动作，按对象形成不同现代义','DRAFT：画出初稿、抽取款项、引来气流，各有对象','draft → draftsman、drafter；drafty、updraft、downdraft 气流分支；overdraft 支取分支。',
 'draft/draught 同源不同地区拼写习惯，不把草稿、冷风、支取凭证都译成一个草稿；同源动作可分出多种结果。',
 '拉取旧词族 → draught、draght → draft；draft + -s-man/-er/-y；up-/down-/over- + draft。',
 [['草稿与起草制图人物','draft · draftsman · drafter'],['漏风与上下气流','drafty · updraft · downdraft'],['支取超过余额','overdraft']],
 'drafty/windy 室内漏风与风大；updraft/downdraft 方向；overdraft 非多存的钱；draft 初稿非定稿。',
 'The drafter worked on the draft in a drafty room.\n\n起草者在一间漏风的房间里修改草稿。','draft draftsman drafter drafty updraft downdraft overdraft')
P=[['拉丁 praesentāre、praesentātiō 等 → presentation','呈到面前、展示'],['英语现代性质派生','presentation + -al → presentational'],['拉丁 repraesentāre、repraesentātiō 经法语 → representation','展示、让对象在眼前或心中出现 → 表现、代表等；非单一再次演示']]
W('presentational','/ˌprezənˈteɪʃənəl/','展示方式的、表达呈现方面的',
 '内容同样，如何排、如何说、如何给人看，属于 presentational 问题；不自动是内容事实本身的问题。',
 'presentation + -al，关系形容词。presentation 先有拉丁、法语名词历史，现代在英语里继续接性质词尾。',P[:2],
 'presentational skills 展示表达技能，presentational choices 呈现方式选择，a presentational issue 展示层面问题。',
 'presentational skills；presentational choices；a presentational issue。',
 'presentational 呈现方式，representational 具象表现、表征等是另一词；多一个 re- 不总是再讲一次幻灯片。',
 ('The course improves students’ presentational skills.','课程提高学生的展示表达技能。'),('The difference was presentational rather than a change in the data.','差别在呈现方式，数据本身没有改变。'))
W('representation','/ˌreprɪzenˈteɪʃən/，中间弱读有变体','表现、描绘、表征；代表、代表权；正式陈述〔按语境〕',
 '地图用图形把城市放到眼前，代表替一群人到场发声：一个让对象出现，一个让对象的利益被代为表达，都可 representation。',
 '经法语 representacion 接拉丁 repraesentātiō，源自 repraesentāre 使出现、展示等。现代可对应 represent + -ation，常用义不是简单英语 re- 再 + presentation 又演示一次。',P[2:]+[['从展示到描绘、代表','现实对象由图像、符号呈现；群体由代表表达']],
 'a visual representation 图形呈现，accurate representation 准确描绘，political representation 政治代表，data representation 数据表示。',
 'a visual representation；accurate representation；political representation；data representation。',
 'representation 可画面、符号或代表关系，presentation 可一次展示；常用前部 /reprɪ-/，另有较少见再展示义可读 /riː-/，不要混为唯一路径。',
 ('The diagram is a simplified representation of the system.','示意图是系统的简化表示。'),('The group asked for better representation on the committee.','团体要求在委员会中获得更充分的代表。'),
 sources=['https://en.wiktionary.org/wiki/representation#English','https://www.etymonline.com/word/representation'])
R('B3943','呈现方式与另一路描绘、代表的拉丁名词','PRESENTATION：把东西呈到别人面前；旁支 representation 按独立历史理解','presentation → presentational；representation 接拉丁 repraesentātiō，经法语到英语，常用义非重新做一次展示。',
 '展示讲法、图形表征、群体代表是不同范围；现代可拆的词形不代替实际借词先后。',
 'praesentātiō 等 → presentation；presentation + -al；repraesentātiō 经法语 → representation，现代对应 represent + -ation。',
 [['展示与展示方式','presentation · presentational'],['描绘、表征及代表','representation']],
 'presentational/representational 呈现与表征性质；representation/presentation 常用义不同；re- 此处不强定再次。',
 'The presentation used a visual representation of the network.\n\n展示使用了一张网络图来表示结构。','presentation presentational representation')
R('B3419','尊称与穿衣动词分来源','DON：名词尊称接 dominus，穿上是 do on 缩合','don 的名词、动词两支用法，保留在一个基础词里辨清。',
 '大学学者、黑帮首领、男性尊称为名词背景；don a coat 的穿衣动作不从掌权者派生。',
 'dominus 经西班牙、意大利等 → don 名词；英语 do on → don 动词。',
 [['名词尊称与另源穿衣动词','don']],
 'don/doff 穿上脱下；donned、donning 双写 n；donner 的南非用法另接 thunder 同族材料，不视为同族。',
 'The don donned his coat before the lecture.\n\n那位大学教师在讲课前穿上了外套。','don')
ROOTS[-1]['exclude']['donner']='常见于特定地区的动词来源接 Afrikaans donder、Dutch donder 雷，与穿衣 don 分源；极少见 don+-er 人物义暂略。'
if __name__=='__main__':save('continuation_20261030_fc',ROOTS,WORDS)
