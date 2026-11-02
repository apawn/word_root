"""Useful base additions and ordinary forms: laser, yoga, yoke and related actions."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'B2891':dict(words=['light','laser','lasers'],label='light 参与的缩略词 laser → lasers',note='laser 取 Light Amplification by Stimulated Emission of Radiation 中的主要词首字母；本页按 light 参与构词收录，不把它拆成古典 las- 加 er。'),
 'C0624':dict(words=['yoke','yoga','conjugal','subjugate'],label='跨语言同源：yoke、yoga 与拉丁 iugum',note='yoke 承古英语 geoc，yoga 经印度语言接梵语 yoga；与拉丁 iugum 共享更远的连接词源，不是由英语互相派生，也不是都直接借拉丁。'),
 'B3958':dict(words=['arrange','arranged','arranging','arrangement'],label='arrange → arranging：把零散部分排出秩序',note='古法语排成行的词接行列材料，更早与日耳曼环相关，英语去 e 加 ing。'),
 'C1534':dict(words=['attract','attracts','attracted','attracting'],label='attract → attracting：朝自己这边拉来',note='拉丁 ad- 与 trahere 到 attrahere，现代英语加 ing。'),
 'C1064':dict(words=['supply','supplied'],label='supply → supplied：把所缺的补上',note='拉丁 sub- 与 plere，经法语等到英语；辅音字母加 y，过去式改为 ied。'),
 'C0351':dict(words=['introduce','introduced','introducing','introduction'],label='introduce → introducing：带进来、第一次让人认识',note='拉丁 intro- 与 ducere；英语动词有拉丁借入或较早 introduction 逆构分析，ing 形式去 e。'),
 'C1628':dict(words=['investigate','investigated','investigating','investigation'],label='investigate → investigating：沿着痕迹查清',note='拉丁 in- 与 vestigare，动词有从 investigation 逆构或接拉丁词干的分析；不与 invest 投资混同。'),
}
W('laser','英 /ˈleɪzə/；美 /ˈleɪzər/','激光；激光器',
 '它的名称不是一块古老的词根，而是把“用受激辐射来放大光”这条技术说明，压缩成一个能直接读出来的短词。现代可指产生激光的装置，也可指这种光。',
 'Light Amplification by Stimulated Emission of Radiation → L-A-S-E-R → laser。主要实词取首字母，by、of 不取；二十世纪仿 maser 等名称构造，后来作为普通单词使用。',
 [['英语技术短语 Light Amplification by Stimulated Emission of Radiation','受激辐射的光放大'],['取主要词首字母 → laser','首字母缩略词 → 激光、激光器']],
 'a laser beam 激光束；a laser printer 激光打印机；a laser scanner 激光扫描器。',
 'use a laser 使用激光器；laser light 激光。可先用常能集中成细光束的装置来理解日常设备里的 laser。',
 'laser 按整个单词读 /ˈleɪzə(r)/。名称里的字母来自技术短语，词尾 er 属于缩略名称整体，与 writer 那类人物后缀的形成方式不同。',
 ('The scanner uses a laser to read the code.','扫描器用激光读取代码。'),('The technician adjusted the laser before the demonstration.','演示前，技术员调整了激光器。'),sources=['https://en.wiktionary.org/wiki/laser#English','https://www.etymonline.com/word/laser'])
W('lasers','英 /ˈleɪzəz/；美 /ˈleɪzərz/','激光器；多种或多束激光〔复数〕',
 '实验室或工厂里不止一台激光器，就可以数成 lasers。谈不同类型、来源的激光时，也可能用这个复数。',
 'laser + -s，末尾读 /z/。laser 原是 Light Amplification by Stimulated Emission of Radiation 的主要词首字母缩略词，进入普通词汇后用英语复数规则。',
 [['英语技术短语的主要词首字母 → laser','名称说明受激辐射的光放大'],['laser + -s → lasers','多台装置；不同类型、来源的激光']],
 'industrial lasers 工业激光器；different types of lasers 不同类型的激光器；lasers used in scanners 扫描器所用的激光装置。',
 'two lasers 两台激光器；precision lasers 用于精密操作的激光器。',
 'laser 既能说光也能说装置；具体数两台还是谈两种光源，要看上下文。结尾 s 是普通英语复数，不属于原缩略短语。',
 ('The laboratory has two lasers for the experiment.','实验室有两台供这项实验使用的激光器。'),('The factory uses lasers to cut thin sheets of metal.','工厂用激光切割金属薄片。'),sources=['https://en.wiktionary.org/wiki/lasers#English','https://www.etymonline.com/word/laser'])
W('yoga','英 /ˈjəʊɡə/；美 /ˈjoʊɡə/','瑜伽',
 '今天常见的是结合体式、呼吸和专注的练习；它更早属于印度思想与修习传统。词的老画面是连接、结合，不能只缩成拉伸身体。',
 '英语经印地语等印度语言接梵语 yoga，含结合、套轭等历史意思，与 yuj 连接词根相关。它与拉丁 iugum、英语 yoke 有更远同源关系，但不是直接从拉丁 jug- 造出的英语词。',
 [['梵语 yuj 连接、yoga 结合及修习名称 → 印地语等','连接、结合的材料进入印度修习传统'],['印度语言名称 → 英语 yoga','保留传统名称；现代也广指相应身体与专注练习']],
 'do yoga 做瑜伽；a yoga class 瑜伽课；a yoga mat 瑜伽垫。',
 'a yoga teacher 瑜伽老师；yoga practice 瑜伽练习。一般作不可数名称。',
 'yoga 与 yoke 可以拿来比较远源的连接意象，不是现代英语一个词变出另一个词。日常课程只是 yoga 广阔传统中的一种现代呈现。',
 ('She takes a yoga class on Tuesday evenings.','她每周二晚上上瑜伽课。'),('I left my yoga mat beside the door.','我把瑜伽垫放在门边了。'),sources=['https://en.wiktionary.org/wiki/yoga#English','https://www.etymonline.com/word/yoga'])
W('yoke','英 /jəʊk/；美 /joʊk/','轭；束缚、压迫；用轭连接、使受束缚',
 '把一根横木搭在两头牲畜的颈肩上，让它们一起拉车、拉犁，这根连接装置就是 yoke。连在一起也可能变成无法摆脱，所以又有束缚、压迫义。',
 '名词继承古英语 geoc、geoht 等，动词有 geocian 连接等旧形式。经日耳曼传承，与拉丁 iugum、梵语 yoga 的连接材料有更远同源关系。',
 [['古英语 geoc 等 → yoke；geocian 等 → yoke 动词','把牵引牲畜套在一起的轭；用轭连接'],['物理套住的画面 → 抽象 yoke','负担、受制与压迫的束缚']],
 'a wooden yoke 木轭；under the yoke of 受……压迫；yoke two animals together 把两头牲畜套在一起。',
 'throw off the yoke 摆脱束缚；a pair of oxen in a yoke 套着轭的一对牛。',
 'yoke 与 yolk 蛋黄常同音，拼写、来源不同。yoke 的两头连在一起，可以帮助理解 conjugal、subjugate 等连接、受制意象，但各词有自己的语言路线。',
 ('A wooden yoke joined the two oxen.','一根木轭把两头牛连在一起。'),('The story describes a village throwing off the yoke of an unjust ruler.','故事写了一个村庄摆脱不公统治者束缚的过程。'),sources=['https://en.wiktionary.org/wiki/yoke#English','https://www.etymonline.com/word/yoke'])
W('arranging','/əˈreɪndʒɪŋ/','安排、排列、整理；改编音乐〔现在分词、动名词〕',
 '把零散的东西放到合适位置，把零散的事情定出先后，就是 arranging。音乐里重新分配给乐器、调整呈现，也叫编配、改编。',
 'arrange 去 e 加 -ing，ge 保留在词干发 /dʒ/。arrange 借古法语 arengier、arangier 排成行，含 reng、rang 行列材料，远接日耳曼环词。',
 [['古法语排成行的词 → arrange','排出秩序 → 安排、整理；也有音乐编配'],['arrange 去 e 加 -ing → arranging','正在安排、排列或改编']],
 'arranging flowers 插花；arranging a meeting 安排会议；arranging music for a small band 为小乐队编配音乐。',
 'arranging the chairs in a circle 把椅子围成一圈；arranging for someone to visit 安排某人来访。',
 'arranging something 常直接接要安排的事情；arranging for someone to do 常说明安排由某人来做。不是每个 arrange 都只说整理实体。',
 ('She is arranging the chairs in a circle.','她正在把椅子围成一圈。'),('We are arranging for a guide to meet the group.','我们正在安排一位导游与团队会合。'),sources=['https://en.wiktionary.org/wiki/arranging#English','https://en.wiktionary.org/wiki/arrange#English'])
W('attracting','/əˈtræktɪŋ/','吸引、引来〔现在分词、动名词〕',
 '目标原来在别处，现在有一股力量把它朝这里拉过来。可以是磁力，也可以是景色、作品让人的注意力过来。',
 'attract + -ing，直接加 ing。拉丁 ad- 朝向 + trahere 拉形成 attrahere，d 在 t 前同化；英语采用相关 attract- 词干。',
 [['拉丁 attrahere、attract- → attract','朝自己这边拉 → 吸引人、物或注意'],['attract + -ing → attracting','正在吸引、引来']],
 'attracting visitors 吸引游客；attracting attention 引起注意；attracting support 赢得支持。',
 'attracting more readers 吸引更多读者；a magnet attracting iron 磁铁吸引铁。',
 'attracting 讲把注意或目标拉过来；attractive 形容有吸引力。吸引不只指外貌，也可指内容、机会或物理力。',
 ('The exhibition is attracting visitors from nearby towns.','展览正吸引附近城镇的游客。'),('The unusual design is attracting a lot of attention.','这个不同寻常的设计正引起大量关注。'),sources=['https://en.wiktionary.org/wiki/attracting#English','https://en.wiktionary.org/wiki/attract#English'])
W('supplied','/səˈplaɪd/','供应、提供了〔过去式、过去分词〕',
 '缺什么，就把那一份补到需要的位置。supplied 说明材料、信息、用品等已经提供了。',
 'supply 改 y 为 i 加 -ed → supplied，结尾读 /d/。supply 接拉丁 sub- 与 plere 所成 supplere，经法语及拉丁借入；b 在 p 前同化。',
 [['拉丁 supplere → 法语、拉丁借入 → supply','补足、填满 → 供应、提供'],['supply → supplied','改 y 为 i 加 ed；供应已发生']],
 'supplied with tools 配给了工具；supplied the information 提供了信息；supplied by the school 由学校提供。',
 'supplied materials 已提供的材料；supplied water to the village 向村庄供水。',
 'supplied someone with something 与 supplied something to someone 可表达相近关系，先认谁得到东西、提供的是什么。supplier 是提供方，不是时态形式。',
 ('The school supplied the students with notebooks.','学校给学生提供了笔记本。'),('The missing information was supplied the next day.','缺少的信息在第二天补上了。'),sources=['https://en.wiktionary.org/wiki/supplied#English','https://en.wiktionary.org/wiki/supply#English'])
W('introducing','英 /ˌɪntrəˈdjuːsɪŋ/；美 /ˌɪntrəˈduːsɪŋ/','介绍、引入；首次推出〔现在分词、动名词〕',
 '原来在这个圈子外面，把人、想法或新方法带进来，是 introducing。第一次让别人认识，也就成了介绍、推出。',
 'introduce 去 e 加 -ing。较早拉丁 intro- 向内与 ducere 带领形成 introducere；英语动词有接拉丁动词或从较早 introduction 逆构的分析。',
 [['拉丁 introducere；introduction 等 → 英语 introduce','带进来 → 介绍、引进；英语来源有不同分析'],['introduce 去 e 加 -ing → introducing','正在介绍、推出或引入']],
 'introducing a new product 推出新产品；introducing someone to a friend 把某人介绍给朋友；introducing a new method 引入新方法。',
 'introducing the topic 引入话题；a book introducing basic ideas 一本介绍基础概念的书。',
 'introducing 可以是让双方认识，也可以是第一次把某事加入已有环境。introduced to 可介绍人或初次接触领域，具体宾语决定关系。',
 ('The teacher is introducing a new topic today.','老师今天正在引入一个新话题。'),('The library is introducing a simpler borrowing system.','图书馆正在引入更简单的借阅系统。'),sources=['https://en.wiktionary.org/wiki/introducing#English','https://en.wiktionary.org/wiki/introduce#English'])
W('investigating','/ɪnˈvestɪɡeɪtɪŋ/','调查、查明〔现在分词、动名词〕',
 '看到一点痕迹，沿着它继续找，弄清事情到底怎么发生，就是 investigating 的核心画面。现代痕迹可以是证据、记录、数据。',
 'investigate 去 e 加 -ing。较早 in- 进入与拉丁 vestigare 追踪足迹相连；英语动词有从 investigation 逆构或接拉丁 investigatus 的分析。',
 [['拉丁 vestigare、investigatus；investigation 等 → investigate','沿迹追踪 → 查明、调查；英语构形有不同分析'],['investigate 去 e 加 -ing → investigating','正在追查原因、事实或问题']],
 'investigating a problem 调查问题；investigating the cause 查原因；investigating how something happened 调查事情如何发生。',
 'a team investigating the incident 调查事件的团队；investigating possible explanations 研究可能的解释。',
 'investigating 是为了弄清事实，并不表示已经找出结论。invest 是投资，investigate 的 vestig- 接足迹，不按同样的几个字母混讲。',
 ('The team is investigating the cause of the power failure.','团队正在调查停电的原因。'),('Researchers are investigating how the material changes over time.','研究人员正在调查这种材料随时间怎样变化。'),sources=['https://en.wiktionary.org/wiki/investigating#English','https://en.wiktionary.org/wiki/investigate#English'])
W('attracts','/əˈtrækts/','吸引、招来〔第三人称单数〕',
 '一处花园把蝴蝶引来，一块招牌把目光引来：attracts 说目标被朝这边拉近，力量可能是物理的，也可能是兴趣。',
 'attract + -s，/t/ 后读 /s/。拉丁 ad- 与 trahere 拉形成 attrahere，辅音同化为 att-，英语接相关 attract- 词干。',
 [['拉丁 attrahere、attract- → attract','朝某处拉 → 吸引注意、人或物'],['attract + -s → attracts','第三人称主语吸引、引来']],
 'attracts attention 引起注意；attracts visitors 吸引游客；attracts iron 吸引铁。',
 'attracts interest 引起兴趣；attracts a wide audience 吸引广泛观众。',
 'attracts 是动作，attractive 是有吸引力的性质。attracts 不只说外貌，也可以讲磁力、内容或机会。',
 ('The bright sign attracts attention.','明亮的招牌吸引目光。'),('The garden attracts butterflies in summer.','花园在夏天会吸引蝴蝶。'),sources=['https://en.wiktionary.org/wiki/attracts#English','https://en.wiktionary.org/wiki/attract#English'])
W('investigated','/ɪnˈvestɪɡeɪtɪd/','调查、查明过〔过去式、过去分词〕',
 '看到了问题或线索，沿着它查过原因、经过，便能说 investigated。它说明做过调查，是否已有明确结论仍要继续看。',
 'investigate + -d，/t/ 后读 /ɪd/。investigate 的英语来源有从 investigation 逆构或接拉丁 investigatus 的分析，较早 in- 与 vestigare 追踪足迹相连。',
 [['拉丁足迹、追踪材料；investigation 等 → investigate','沿迹找 → 调查、查清'],['investigate 去 e + -ed → investigated','调查发生了；be investigated 表示接受调查']],
 'investigated the cause 调查原因；investigated by a team 由团队调查；thoroughly investigated 经过充分调查。',
 'investigated a complaint 调查投诉；investigated how something works 查明某物如何工作。',
 'investigated 不表示已证明某人有错；可能只是检查问题、寻找原因。invested 是 invest 投入的形式，不能因字母相似就混成同一动作。',
 ('The team investigated the cause of the delay.','团队调查了延误的原因。'),('The researchers investigated how the material responded to heat.','研究人员调查了这种材料受热后如何变化。'),sources=['https://en.wiktionary.org/wiki/investigated#English','https://en.wiktionary.org/wiki/investigate#English'])
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_zaf',ROOTS,WORDS)
 extend_lessons()
