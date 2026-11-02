"""Existence, gang and turkey: absence, groups and historical naming confusion."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
W('nonexistence','英 /ˌnɒnɪɡˈzɪstəns/；美 /ˌnɑːnɪɡˈzɪstəns/','不存在、没有存在这一状态',
 '不是东西躲起来没看见，而是在讨论它根本有没有；这个名词把“不存在”本身拿出来作话题。',
 'non- 不、无 + existence 存在，否定整个名词。existence 自己接拉丁 exsistere 等显现、存在词族，不从 non- 重新改造古拉丁。',
 [['exsistere 等词族 → existence','出现、存在这一状态'],['non- + existence → nonexistence','不存在的状态']],
 'the nonexistence of a record 记录不存在，prove nonexistence 证明不存在，claims of nonexistence 声称不存在。',
 'the nonexistence of；prove nonexistence；evidence of nonexistence。',
 'nonexistence 不存在，absence 不在场、缺少也可能只是没来；没有找到证据和已经证明 nonexistence 也不是同一句判断。',
 ('The report notes the nonexistence of a central register.','报告指出不存在中央登记册。'),('The story explores the idea of nonexistence.','故事探讨了不存在这一概念。'))
R('B2603','存在、共同存在与不存在','EXISTENCE：把存在这件事当名词','existence → coexistence 共同存在；nonexistence 否定存在。',
 'co-、non- 作用在同一个名词上，却改变关系不同：前者把多个存在者放一起，后者否定有没有。',
 'exist 词族 → existence；co- + existence → coexistence；non- + existence → nonexistence。',
 [['存在状态与关系','existence · coexistence · nonexistence']],
 'nonexistence/absence 根本不存在与不在场、缺少；coexistence 共同存在不自动保证完全和谐。',
 'The essay considers existence, coexistence and the possibility of nonexistence.\n\n文章讨论存在、共同存在，以及不存在的可能。','existence coexistence nonexistence')
G=[['古英语 gang、古北欧相关词 → 英语 gang','行进、通路、成套等旧材料'],['英语群体用法','一同工作、来往的人 → 一伙人，也可犯罪团伙'],['组合分选旧义','gangster 接犯罪团伙；gangplank、gangway 保留行走通路材料']]
W('gang','/ɡæŋ/','一群、一伙；团伙、帮派；结伙',
 '一群常一起走、一起干活的人；朋友口中的 the gang 可以亲近，新闻里的 a criminal gang 则是犯罪团伙。',
 '接古英语行进、通路名及北欧相关形式，成套、一起行动等用法再发展成人群。gang 的旧行进词虽和 go 意思接近，不能断言现代 gang 就是 go 加尾巴。',G,
 'a gang of thieves 一伙盗贼，a work gang 一班工人，the whole gang 全伙朋友，gang up on 联合起来欺负或对付。',
 'a gang of；a work gang；the whole gang；gang up on。',
 'gang 不总带犯罪评价，gangster 却明确偏犯罪人物；gangway 的 gang 又保留旧通路材料。',
 ('The whole gang came to the picnic.','一伙朋友全来野餐了。'),('They warned him not to gang up on the new student.','他们提醒他别结伙欺负新同学。'),
 sources=['https://www.etymonline.com/word/gang','https://en.wiktionary.org/wiki/gang#English'])
W('gangster','英 /ˈɡæŋstə/；美 /ˈɡæŋstər/','匪徒、黑帮成员、犯罪集团成员',
 '不是普通朋友群里的成员，而是接 gang 的犯罪团伙那支；电影里的 gangster 常靠组织性犯罪谋利。',
 'gang + -ster，人物后缀，选取犯罪团体语义。-ster 本身不是所有场合都带犯罪，关键还在词基和约定用法。',G[:2]+[['gang + -ster → gangster','犯罪团伙、黑帮中的人物']],
 'a gangster film 黑帮片，a notorious gangster 臭名昭著的匪徒，a former gangster 前黑帮成员。',
 'a gangster film；a notorious gangster；a former gangster。',
 'gangster 明确指犯罪人物，a member of the gang 可能只是朋友一群中的成员；不能省掉语境直接等同。',
 ('The actor became famous for playing a gangster.','演员因饰演黑帮成员而出名。'),('The book follows the rise and fall of a notorious gangster.','书追踪了一名臭名昭著匪徒的兴衰。'))
W('gangplank','/ˈɡæŋplæŋk/','跳板、上下船踏板',
 '船和码头之间搭一块能走的板，临时接成通路；gang 取旧行走通路义，不是黑帮专用木板。',
 'gang 行走的路、通道 + plank 木板，航海组合名称。gangway 范围可更广，gangplank 强调踏板、板桥。',G[:1]+[['gang + plank → gangplank','连接船岸供人行走的板']],
 'lower the gangplank 放下跳板，walk up the gangplank 沿跳板登船，a narrow gangplank 窄踏板。',
 'lower the gangplank；walk up the gangplank；a narrow gangplank。',
 'gangplank 是通行板，plank 一般木板；gangland 才接黑帮地域的那一支。',
 ('The crew lowered the gangplank.','船员放下了登船跳板。'),('Passengers walked up the gangplank one at a time.','乘客一个接一个沿跳板登船。'))
W('gangbang','/ˈɡæŋbæŋ/','群交、轮奸〔粗俗词，依语境〕；参与暴力帮派活动',
 'gang 抓多人一伙，bang 接粗俗性行为或暴力活动的用法；是否涉及自愿不能靠一个词的表面组合判断。',
 'gang + bang 的俚语组合，作名词、动词。现代可指群体性行为，也可指轮奸；动词还有参与暴力帮派活动这一支。',G[1:]+[['gang + bang → gangbang','多人性行为、轮奸等粗俗义；暴力帮派活动义']],
 'a report of a gangbang 关于轮奸等事件的报告〔按语境〕；gangbanging 在犯罪活动叙述里可说参与帮派暴力。',
 'gangbang〔粗俗、语境定具体义〕；gangbanging〔亦可帮派活动〕。',
 '群体性行为与性侵害不能混为同一件事；这个词在不同材料里覆盖不同义，正式叙述宜把具体行为说明白。',
 ('The novel describes the gangbang as an act of violence.','小说把该事件描述为一次轮奸暴力。'),('In the report, gangbanging refers to violent gang activity.','报告里 gangbanging 指参与暴力帮派活动。'),
 sources=['https://www.merriam-webster.com/dictionary/gangbang','https://en.wiktionary.org/wiki/gangbang#English'])
R('B4040','一起走、一起做，现代也可是一伙犯罪者','GANG：群体与旧通路分开选义','gang → gangster、gangland 接犯罪；gangplank、gangway 接旧通路；gangbang 俚语义按语境辨。',
 'the gang of friends 与 gangsters 语气不同。通路复合词不必拖入黑帮故事，俚语也不只按两个常用字面义猜。',
 'gang 行进通路旧材料 → 成套、群体；gang + -ster/land；gang + plank/way；gang + bang。',
 [['群体与犯罪人物','gang · gangster · gangland'],['行走通道','gangway · gangplank'],['特殊俚语组合','gangbang']],
 'gang/gangster 普通一群与犯罪人物；gangplank 不按帮派木板讲；gangbang 的不同语义不抹平同意与伤害。',
 'The whole gang walked up the gangplank together.\n\n一伙朋友一起沿跳板登船。','gang gangster gangland gangway gangplank gangbang')
W('turkey','英 /ˈtɜːki/；美 /ˈtɜːrki/','火鸡、火鸡肉；失败作品、笨家伙〔俚语〕',
 '扇形大尾、脖颈有肉垂的大鸟，以及餐桌上的肉；a turkey 说电影等也可能是在骂失败之作。',
 '鸟名与旧 Turkey 地域称呼相关，较早用在经相关贸易路线传入的珍珠鸡，后转到北美火鸡；具体传播解释有差异。不是说现代火鸡原产土耳其。',
 [['旧 Turkey 地域名关联的鸟类称呼','贸易、误认背景；早期曾指珍珠鸡'],['名称转用到北美火鸡 → turkey','鸟、肉料'],['俚语扩展','失败作品、无能人物等']],
 'roast turkey 烤火鸡，turkey sandwiches 火鸡肉三明治，a box-office turkey 票房失败影片，go cold turkey 突然完全停止某习惯。',
 'roast turkey；turkey meat；a box-office turkey；cold turkey。',
 'turkey 鸟与 Turkey 地名按大写、语境分；火鸡肉不可数用法常见，an entire turkey 可说一整只。',
 ('They served roast turkey with vegetables.','他们端上了烤火鸡和蔬菜。'),('The expensive film turned out to be a turkey.','这部耗资巨大的电影结果成了失败之作。'),
 sources=['https://www.etymonline.com/word/turkey','https://en.wiktionary.org/wiki/turkey#English'])
R('B2520','鸟名经过地域联想与误认，再固定下来','TURKEY：名字带旧地理印象，鸟却不因此原产那儿','turkey 鸟 → 肉料；俚语 turkey 可指失败作品。',
 '词名保存了贸易、地理认知的历史，不能只照名字给动物画原产地。失败作品的比喻则按现代上下文辨。',
 'Turkey 关联的早期鸟名 → 转用于北美火鸡 → turkey；再有肉料、失败之作等义。',
 [['鸟、食物与俚语','turkey']],
 'turkey/Turkey 普通鸟名与大写地域名；turkey 原产地不由英文名字推出；a turkey 还可失败之作。',
 'The documentary explains how the turkey got its misleading English name.\n\n纪录片解释了火鸡怎样得到这个容易误导人的英文名字。','turkey')
if __name__=='__main__':save('continuation_20261030_gd',ROOTS,WORDS)
