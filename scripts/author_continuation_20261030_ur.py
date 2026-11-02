"""Common missing nouns: bounded space, acting, administration and plural domains."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'A1776':dict(words=['area'],label='area：可数范围与面积的普通复数',note='area 来自拉丁开阔、平坦场地词，现代 areas 是普通英语复数，可说多片地区或多个领域；面积作为数值性质另按搭配理解。'),
 'C0023':dict(words=['agent','agency'],label='agent 与 agency：做事的一方及行动能力',note='agency 接中世纪拉丁 agentia，源于 agere 行动的分词词干；机构义与能动性义分开用例，不只背成公司。'),
 'B3207':dict(words=['execute','execution','executive'],label='execute 与 executive：把事付诸实行',note='executive 接拉丁执行、完成的词干及 -ivus 形容词材料；行政、企业管理和管理者名词均接实际施行这一条支线。'),
 'C1526':dict(words=['turn','attorney'],label='attorney：由转向、指定词族形成的代理人名称',note='attorney 经法语 atorné 被指定的人，上接 atorner 指派、转向；更早接 tourner、拉丁 tornare 转动的词族，不能按现代英语几个任意音节硬拆。'),
 'A1705':dict(words=['cancer','cancerous'],label='cancer 与 cancerous：疾病名到性质形容词',note='cancer 医学词经拉丁螃蟹、肿瘤旧名称等历史进入英语；cancer + -ous → cancerous，现代义按细胞、组织的癌性理解。旧形状比喻不是病因解释。'),
 'C0898':dict(words=['operation','operations'],label='operations：运营、行动、手术与运算',note='operation 接拉丁 operari 工作、施行；复数 operations 在不同领域形成固定用法，不能都直译操作。'),
 'B2636':dict(words=['art','arts'],label='arts：技能、艺术与人文学科的范围',note='art 旧指学习实践所得技能；arts 可统称艺术门类，也保留人文学科和技艺的历史范围，具体学科边界依课程名称而定。'),
}
W('area','英 /ˈeəriə/；美 /ˈeriə/','地区、区域；面积；领域、方面',
 '在地图上圈一片地方，是 an area；问这一片有多大，是 area 面积；把知识也想成一片版图，就有研究领域的意思。',
 '来自拉丁 area 平坦地面、空场，可用于建筑地、活动场、打谷场等；更远来源不定。英语由空场发展为边界内的表面量、区域和抽象领域。',
 [['拉丁 area','平坦地面、开阔空场'],['英语 area','区域；范围内的表面量；抽象领域']],
 'a residential area 住宅区；the area of a circle 圆的面积；an area of study 研究领域；in this area 在这一带或这一方面。',
 'a large area；areas of concern；calculate the area。','area 是区域或面积，volume 是体积。词义随提问变化：Where? 常关心区域，How much surface? 关心面积；专业上下文也会把 area 用于方面。',
 ('The school is in a quiet residential area.','学校位于安静的住宅区。'),('We calculated the area of the rectangle.','我们算出了长方形的面积。'),('This is an area where we need more research.','这是我们需要进一步研究的领域。'),sources=['https://www.etymonline.com/word/area','https://en.wiktionary.org/wiki/area#English'])
W('agency','/ˈeɪdʒənsi/','机构、代理处；作用；自主行动、作出影响的能力〔能动性〕',
 '有人或某个单位能把事情办起来，是 agency 的老行动线索。a travel agency 是办理旅行事务的机构；a sense of agency 是感觉自己能作决定、让事情发生。',
 '接中世纪拉丁 agentia，来自拉丁 agens、agent- 行动、起作用者的分词材料，上接 agere 推动、做。英语先有作用、施加影响义，后来发展出替人办理业务的机构等。',
 [['拉丁 agere → agens／agent- → agentia','做、推动 → 起作用、采取行动'],['英语 agency','作用、能动性；代理业务单位、机构']],
 'a travel agency 旅行社；a government agency 政府机构；an advertising agency 广告代理公司；human agency 人的能动作用；a sense of agency 能自己作决定的感受。',
 'act through an agency；individual agency。','agency 不总是一个办公单位。talk about personal agency 在谈人的自主行动能力；an agency 通常是可数机构，定冠词和修饰语有助分义。',
 ('She found the job through an employment agency.','她通过职业介绍机构找到了工作。'),('The project gave students a stronger sense of agency.','那个项目让学生更感到自己能作决定并产生影响。'),sources=['https://www.etymonline.com/word/agency','https://www.merriam-webster.com/dictionary/agency','https://en.wiktionary.org/wiki/agency#English'])
W('executive','/ɪɡˈzekjətɪv/','行政的、执行管理的；管理人员、高管；行政部门',
 '计划写出来，还需要有人决定怎么落地、调动资源做成。executive 把重点放在实际执行、管理的一方。',
 '接拉丁 executivus，来自 exequi、exsequi 跟进完成、执行的分词词干；其 ex- 与 sequi 跟随材料相连。行政权用法后来形成企业管理人员、行政部门等名词义。',
 [['拉丁 exsequi／exequi → executivus','跟进、完成 → 执行相关的'],['英语 executive','行政、执行管理；相应人员或部门']],
 'an executive decision 管理者作出的决定；chief executive 首席执行官等；executive summary 给决策者看的概要；a company executive 企业管理人员。',
 'executive responsibility；the executive branch。','execute 是执行动作，executive 是相关性质或执行管理者。executive summary 不是计划下一步要去执行的摘要，而是供决策者快速掌握重点的概要。',
 ('She works as an executive at a publishing company.','她在一家出版公司担任管理职务。'),('The report begins with a short executive summary.','报告开头有一份简短的决策概要。'),sources=['https://www.etymonline.com/word/executive','https://en.wiktionary.org/wiki/executive#English'])
W('attorney','英 /əˈtɜːni/；美 /əˈtɝːni/','律师〔尤美式常见〕；被授权的代理人',
 '别人把某件事务交到你手里，让你代表他处理，老核心是被指定的代表。现代美式里 attorney 很常指律师。',
 '经古法语 atorné 被指派的人，原为 atorner 指定、安排、转向的分词；上接 a- 向与 tourner 转动，后者接拉丁 tornare。英语后来在法律代理、律师领域专门化。',
 [['法语 atorner → atorné','指定、派定 → 被指定的代表'],['英语 attorney','获授权代理者；现代常见律师义']],
 'an attorney for a client 客户的代理律师；hire an attorney 聘请律师；power of attorney 授权委托、代理权等文书用语，具体所指由文本决定。',
 'speak to an attorney；an attorney’s office。','lawyer 泛指律师；attorney 在美式常这样用，也保留授权代理人的用法。不能单凭这个英文称号推定所有地区完全同一种资格或职能。',
 ('The company’s attorney reviewed the draft.','公司的律师审阅了草稿。'),('She works as an attorney in a small law firm.','她在一家小型律师事务所做律师。'),sources=['https://www.etymonline.com/word/attorney','https://www.merriam-webster.com/dictionary/attorney','https://en.wiktionary.org/wiki/attorney#English'])
W('cancer','英 /ˈkænsə/；美 /ˈkænsər/','癌；癌症；Cancer：巨蟹座等专名用法',
 '现代医学里，它是一组异常细胞失控分裂、可能侵入或扩散到其他组织的疾病名称。老名字借螃蟹形状来联想部分肿瘤的外观。',
 '接拉丁 cancer 螃蟹、肿瘤等旧名，与希腊 karkinos 的螃蟹、肿瘤名称相关。英语古时已借入，后有受法语影响的 canker 等形式，近代医学中又固定 cancer；大写还用于巨蟹座。',
 [['希腊、拉丁螃蟹与肿瘤旧名称','部分肿瘤周围血管使古人联想到螃蟹'],['英语 cancer 的医学专门化','现代疾病类别名称；大写另有星座用法']],
 'cancer cells 癌细胞；cancer research 癌症研究；a type of cancer 一类癌症；Cancer as a zodiac sign 巨蟹座。命名史与现代疾病机制分开理解。',
 'study cancer；cancer biology；a cancer research centre。','cancer 通常指癌这一疾病类，cancerous 是癌性的形容词。canker 是同源分化后的另一个词，现代不能到处拿它替换 cancer。',
 ('The laboratory studies how cancer cells grow.','实验室研究癌细胞怎样生长。'),('The museum exhibition traced the history of cancer research.','博物馆展览回顾了癌症研究的历史。'),sources=['https://www.etymonline.com/word/cancer','https://www.cancer.gov/publications/dictionaries/cancer-terms/def/cancer','https://en.wiktionary.org/wiki/cancer#English'])
W('cancerous','英 /ˈkænsərəs/；美 /ˈkænsərəs/','癌性的、癌变的；比喻：像癌一样扩散、侵蚀的',
 'cancer 是病名，cancerous 把癌的性质接到细胞、组织、肿瘤上。这个词说明所指东西具有癌性。',
 'cancer + -ous，-ous 形成具有某种性质的形容词。医学词族沿旧 cancer 名称发展，后来也有恶性蔓延、侵蚀的比喻用法。',
 [['cancer','癌；疾病名称'],['cancer + -ous → cancerous','具有癌性的；后来可比喻侵蚀扩散']],
 'cancerous cells 癌细胞；cancerous tissue 癌组织；a cancerous tumour 癌性肿瘤。比喻用于抽象问题时有很强负面色彩。',
 'cancerous growth；cancerous changes。','cancerous 描写性质，cancer 是名词。不能仅由旧螃蟹字面判断今天的科学分类；读现代医学说明时按癌性的专业义理解。',
 ('The textbook includes images of cancerous cells.','教材中有癌细胞的图像。'),('The lecture explained how cancerous tissue can affect nearby structures.','讲座解释了癌组织怎样影响邻近结构。'),sources=['https://www.etymonline.com/word/cancer','https://www.cancer.gov/publications/dictionaries/cancer-terms/def/cancer','https://en.wiktionary.org/wiki/cancerous#English'])
W('operations','英 /ˌɒpəˈreɪʃənz/；美 /ˌɑːpəˈreɪʃənz/','运营、业务活动；行动；手术、运算等〔operation 复数〕',
 '不是纸上的想法，而是一整套实际做起来的工作。企业每天怎么运转、救援怎么组织，都能放进 operations。',
 'operation 经法语接拉丁 operatio 工作、施行，上接 operari 劳作及 opus、oper- 工作词族。复数 operations 在企业、军事、医疗、数学等领域各自固定下来。',
 [['拉丁 operari → operatio → operation','工作、施行、产生作用'],['operation + -s → operations','多次施行；领域中的整套活动或处理']],
 'daily operations 日常运营；rescue operations 救援行动；military operations 军事行动；surgical operations 手术；arithmetic operations 算术运算。',
 'manage operations；business operations。','operations 在企业里通常不是按钮操作的复数，而是实际业务运作。要先认领域，再决定译运营、行动、手术还是运算。',
 ('She manages the hotel’s daily operations.','她管理酒店的日常运营。'),('Rescue operations continued through the night.','救援行动持续了一整夜。'),sources=['https://www.etymonline.com/word/operation','https://en.wiktionary.org/wiki/operations#English'])
W('arts','英 /ɑːts/；美 /ɑːrts/','艺术门类；人文学科、技艺等〔art 复数〕',
 '绘画、音乐、戏剧等不同门类放在一起，是 the arts。大学里 arts 又常保留更广的人文、学习技艺的历史范围。',
 'art 经法语接拉丁 ars、art- 技能、手艺，旧时就可指学习实践得到的能力；arts 为复数，现代既统称艺术，也见于人文教育、学位名称。',
 [['拉丁 ars／art- → 法语／英语 art','学习、实践得到的技能、手艺'],['art + -s → arts','艺术门类；人文、技艺教育等历史分支']],
 'the arts 艺术各门类；performing arts 表演艺术；arts and crafts 艺术与手工；a Bachelor of Arts 文学学士等学位名称，实际课程范围依学校而定。',
 'support the arts；an arts festival。','art 在普通语境常让人想到美术或艺术统称；arts 在教育名称中不只指画画。读 arts degree 时不能只凭日常美术义猜专业。',
 ('The town opened a new centre for the performing arts.','小镇新建了一座表演艺术中心。'),('The festival brings together music, theatre and other arts.','那场艺术节汇集了音乐、戏剧等艺术门类。'),sources=['https://www.etymonline.com/word/art','https://en.wiktionary.org/wiki/arts#English'])
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_ur',ROOTS,WORDS)
 extend_lessons()
