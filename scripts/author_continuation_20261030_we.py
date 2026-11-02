"""Everyday reading vocabulary: levels, sounds, costs and systems."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'B3915':dict(words=['level','levels'],label='level → levels：水平、层级；使平整',note='level 经法语接拉丁 libella 小天平、水准器，现代多种高低程度沿这一测平画面理解。'),
 'C1368':dict(words=['sound','sounds'],label='sound → sounds：声音；听起来',note='声音、发声路线接拉丁 sonus、sonare；健康、海峡、测深等同形词另有来源，不强归为 son-。'),
 'B2842':dict(words=['cost','costs'],label='cost → costs：费用；使付出代价',note='cost 经法语接拉丁 constare 一系，现代 -s 可标名词复数或单数主语花费。'),
 'C0675':dict(words=['line','lines'],label='line → lines：线条、行列、线路；加衬里',note='线条义融合早期英语、法语相关形式，法语 ligne 接拉丁 linea 麻线；衬里义另接早期亚麻布材料。'),
 'C0401':dict(words=['feature','features'],label='feature → features：特征、五官；以……为特色',note='feature 经法语接拉丁 factura 制作、形成；features 既可说多个特征，也可作特色呈现的动词。'),
 'B2597':dict(words=['reason','reasons'],label='reason → reasons：理由；推理、劝说',note='reason 经法语接拉丁 ratio 计算、理解、理由的词族，现代复数与动词第三人称同形。'),
 'B3366':dict(words=['goal','goals'],label='goal → goals：目标、球门与进球',note='goal 较早有边界、界限义，后用于终点、球门与目的，远源细节仍有讨论。'),
 'B3962':dict(words=['team','teams'],label='team → teams：队伍；合作与搭配',note='team 继承古英语团队、成组挽畜等材料；现代 teams 可作队伍复数，也可用于 teams up 等动词。'),
 'B3250':dict(words=['school','schools'],label='school → schools：学校、流派；鱼群另源',note='学习场所 school 接希腊 schole 闲暇、学习活动的路线；鱼群 school 接荷兰语相关词，是另一来源。'),
 'C1462':dict(words=['system','systems'],label='system → systems：各部分组成的整体',note='system 接希腊 systema 组织成的整体，与 syn- 一起和使站立词族有关；systems 是现代复数。'),
 'C0023':dict(words=['activity','activities'],label='activity → activities：活动、行动、活跃状态',note='activity 与 active 对应，历史经法语接拉丁 activitas；现代复数把 y 变成 ies。'),
}
W('levels','/ˈlevəlz/','水平、程度；层、级别、液位等；使平整等〔level 的第三人称单数〕',
 '把东西放到一把量高低的尺旁边：水有水位，人有技能水平，建筑有楼层，组织有层级。levels 把不同高低或程度数出来。',
 'level + -s，词尾 /z/。level 经古法语 livel 接拉丁 libella 小天平、水准器，后扩展到程度、层次及使平整的动作。',
 [['拉丁 libella → 法语 livel → level','小天平、水准器 → 水平、层次、程度'],['level 名词、动词 + -s → levels','多个层次、数值；单数主语使平整等']],
 'water levels 水位；noise levels 噪声水平；skill levels 技能等级；on several levels 在几个层面上；levels the ground 把地面整平。',
 'different levels of experience；high levels of noise。','levels of water 常强调水位或量的水平，levels of a building 是楼层。a level surface 说平整，level 作形容词本身不靠加 -s 表复数。',
 ('The course has exercises for several skill levels.','这门课为几个技能等级准备了练习。'),('Water levels rose after the heavy rain.','大雨过后，水位上升了。'),sources=['https://en.wiktionary.org/wiki/levels#English','https://en.wiktionary.org/wiki/level#English'])
W('sounds','/saʊndz/','声音〔复数〕；发声、听起来等〔sound 的第三人称单数〕；海峡等另源用法',
 '听到一阵阵声响，是 sounds；听完一个提议觉得不错，说 That sounds good。后一句是对听起来的印象作判断。',
 'sound + -s，/d/ 后读 /z/。声音名词接拉丁 sonus 经法语，发声动词接 sonare 的相关借入线；英语末尾 d 后加。另有海峡、健康可靠、测深等不同来源的同形词。',
 [['拉丁 sonus／sonare → 法语 → 声音义 sound','声音、发声；再有听起来等用法'],['sound + -s → sounds；另看同形词各自来源','多个声音；单数主语发声、听起来等']],
 'strange sounds 奇怪的声音；sounds like ... 听起来像……；sounds good 听着不错；sounds the alarm 发出警报。地理语境的 sounds 也可能是若干海峡或水道。',
 'the sounds of birds；sounds interesting。','sounds good 中 good 描述听起来的整体效果，不改成 sounds well 来表达同一个意思。sound advice 中 sound 是可靠的形容词，不能按拉丁声音词根硬猜。',
 ('We could hear the sounds of traffic through the window.','我们能从窗户听见车流声。'),('Your plan sounds practical.','你的计划听起来可行。'),sources=['https://en.wiktionary.org/wiki/sounds#English','https://en.wiktionary.org/wiki/sound#English'])
W('costs','英 /kɒsts/；美 /kɔːsts, kɑːsts/','费用、成本、代价〔复数〕；花费、使付出〔cost 的第三人称单数〕',
 '得到某个东西，需要付出什么，是 cost；分成交通、材料等几项来算，可以说 costs。代价也能是时间、机会或信任。',
 'cost + -s，/t/ 后读 /s/，结尾 /sts/ 不另加音节。cost 经法语 coster 等接拉丁 constare 一系，英语花费、代价义已经固定。',
 [['拉丁 constare → 法语 cost／coster 等 → cost','历史价格、花费词族'],['cost 名词、动词 + -s → costs','多项成本；单数主语花费、使失去']],
 'travel costs 出行费用；running costs 运营成本；cut costs 降低成本；costs ten pounds 花十英镑；costs time 耗费时间；at all costs 不惜一切代价。',
 'cover the costs；costs more than expected。','The costs are high 中 costs 是复数名词；It costs a lot 中是动词。一般花费义过去式仍是 cost，costs 不能靠 -s 来表示过去。',
 ('The ticket costs less if you book early.','提前订票，票价会更低。'),('We shared the travel costs equally.','我们平摊了出行费用。'),sources=['https://en.wiktionary.org/wiki/costs#English','https://en.wiktionary.org/wiki/cost#English'])
W('lines','/laɪnz/','线、线条；行、队列、线路；台词；给……画线、加衬里等动词形式',
 '一条细长的痕迹是 line，排成一线的人、文字、交通线路也能这样想。演员按顺序说的一句句话，则叫 lines 台词。',
 'line + -s，/n/ 后读 /z/。线条义融合古英语 line 与法语 ligne，法语线接拉丁 linea 麻线；加衬里另接早期英语 lin 亚麻布材料，不由画线动作直接解释。',
 [['拉丁 linea 及相关早期英语形式 → 线条义 line；另路 lin 布料 → 衬里动词','线、行列；以布衬里，分清近源用法'],['line 名词、动词 + -s → lines','多个线条、行、线路等；单数主语画线、衬里等']],
 'straight lines 直线；railway lines 铁路线；lines of text 一行行文字；learn your lines 记台词；along these lines 大致按这个思路；read between the lines 读出言外之意。',
 'draw two lines；the opening lines of a poem。','lines of a poem 是诗行，lines for a play 常是台词。the lines on a map 可能是线路或边界线，具体由图例说明，不能只认一种线。',
 ('The actor spent the afternoon learning her lines.','这位演员花了一下午背台词。'),('Draw two parallel lines across the page.','在纸上横着画两条平行线。'),sources=['https://en.wiktionary.org/wiki/lines#English','https://en.wiktionary.org/wiki/line#English'])
W('features','英 /ˈfiːtʃəz/；美 /ˈfiːtʃərz/','特征、特色、功能；面貌、五官；特写报道；以……为特色、包含〔动词形式〕',
 '让你认出一个人或产品的那些显著部分，是 features：人的眉眼轮廓，软件的功能，房子的特色，都可以从这个画面理解。',
 'feature 已有 e，加 s，词尾 /z/。feature 经古法语 faiture 形状、制作接拉丁 factura 形成、制作；动词由名词发展出突出呈现、包含等义。',
 [['拉丁 factura → 古法语 faiture → feature','形成、样貌 → 显著特点；面貌等'],['feature 名词、动词 + -s → features','多个特征、功能；单数主语以……为特色']],
 'facial features 面部特征、五官；safety features 安全功能；key features 主要特点；a magazine’s features 杂志的特写文章；features a large garden 以大花园为特色。',
 'new features；features local artists。','The app has new features 中是功能名词；The app features a new editor 中是动词。features 说提供了什么特点，benefits 更常说这些特点给人带来什么好处。',
 ('The update adds two useful features.','这次更新增加了两个实用功能。'),('The exhibition features work by local artists.','这次展览展出当地艺术家的作品。'),sources=['https://en.wiktionary.org/wiki/features#English','https://en.wiktionary.org/wiki/feature#English'])
W('reasons','/ˈriːzənz/','理由、原因〔复数〕；推理、讲道理〔reason 的第三人称单数〕',
 '把为什么说清楚，是给出 reasons；把想法一步步推过去，是作动词的 reasons。',
 'reason + -s，词尾 /z/。名词、动词沿相关法语路线接拉丁 ratio 计算、理解、理由，与 reri 思考、核算同族；现代两种词性同形。',
 [['拉丁 ratio／reri 词族 → 法语相关形式 → reason','计算、思考 → 理由、推理'],['reason + -s → reasons','多个理由；单数主语推理、讲道理']],
 'reasons for leaving 离开的理由；for several reasons 出于几个原因；gives reasons 给出理由；reasons that ... 推断……；reasons with someone 跟某人讲道理。',
 'good reasons；for personal reasons。','reasons for a decision 说明为何作此决定；causes of an event 更常追实际导致事件的因素。两者有重叠，但人的解释和客观成因不总是一回事。',
 ('There are several reasons for choosing the smaller room.','选择小房间有几个理由。'),('She reasons that an early start will save time later.','她推断，早点开始能为后面节省时间。'),sources=['https://en.wiktionary.org/wiki/reasons#English','https://en.wiktionary.org/wiki/reason#English'])
W('goals','英 /ɡəʊlz/；美 /ɡoʊlz/','目标；球门；进球、得分；goal 的复数',
 '球要送进哪儿，事情想做到哪一步，都有一个瞄准点。goals 可以是球门、进球，也可以是你希望实现的目标。',
 'goal + -s，/l/ 后读 /z/。goal 接中古英语 gol 边界、界限一系，后用于终点和目标；更远的障碍、标记词关系仍有讨论。',
 [['中古英语 gol → goal','边界、终点 → 球门、目标'],['goal + -s → goals','多个目标、球门或进球']],
 'set goals 设定目标；achieve goals 实现目标；long-term goals 长期目标；scored two goals 进了两球；the goals at either end 两端的球门。',
 'personal goals；goals for the season。','goals 指球门还是进球，要看 build、move、score 等搭配。score two goals 说进了两个球，move two goals 则可能是在搬动两个球门。',
 ('We set three small goals for the first month.','我们为第一个月定了三个小目标。'),('The team scored two goals in the final ten minutes.','球队在最后十分钟进了两个球。'),sources=['https://en.wiktionary.org/wiki/goals#English','https://en.wiktionary.org/wiki/goal#English'])
W('teams','/tiːmz/','队、团队〔复数〕；合作、使搭配〔team 的第三人称单数〕',
 '一组人朝共同目标一起做事，是 teams。team 作动词时，就是让原来分开的人或东西配成一组。',
 'team + -s，/m/ 后读 /z/。team 继承古英语 team，早有后代、成组挽畜等义，逐渐发展为共同活动的队伍；现代动词与成组、配合相连。',
 [['古英语 team → team','后代、成组挽畜等 → 共同活动的队伍'],['team 名词、动词 + -s → teams','多支队伍；单数主语合作、搭配']],
 'sports teams 运动队；project teams 项目团队；teams up with ... 与……联手；teams a jacket with jeans 把外套与牛仔裤搭配。',
 'teams from different cities；teams up for a project。','team 强调作为整体共同做事，group 只说明成一组，未必有共同任务。teams up 中 teams 是动词，要把 up 和 with 的搭配一起读。',
 ('Two teams worked together to finish the project.','两个团队合作完成了这个项目。'),('She often teams up with her neighbour to organise local events.','她常和邻居联手组织社区活动。'),sources=['https://en.wiktionary.org/wiki/teams#English','https://en.wiktionary.org/wiki/team#English'])
W('schools','/skuːlz/','学校；学派、流派；鱼群；训练、教导〔动词形式〕',
 '一所所学习机构是 schools；一群人采用相近思想和方法，又成为学派。鱼群也写 schools，但那是一条独立词源，不能把鱼想成真的去上学。',
 'school + -s，/l/ 后读 /z/。学习场所经早期英语接拉丁 schola、希腊 schole，早有闲暇、讨论、学习义；鱼群 school 则沿荷兰语相关群体词路线借入。',
 [['希腊 schole → 拉丁 schola → 学习场所 school；再有学派等义','闲暇、学习活动 → 学校'],['另路荷兰语相关群体词 → 鱼群 school；各加 -s → schools','多个学校、学派或鱼群；同形不同源']],
 'primary schools 小学；schools of thought 思想流派；schools of fish 一群群鱼；schools someone in ... 训练某人掌握……。',
 'local schools；different schools of thought。','schools of thought 指不同思想体系，未必是几所校舍；schools of fish 指鱼群。动词 school 常带有训练、使熟练或让人得到教训的意思。',
 ('The town has two primary schools.','镇上有两所小学。'),('Large schools of fish moved beneath the boat.','大群大群的鱼在船下游动。'),sources=['https://en.wiktionary.org/wiki/schools#English','https://en.wiktionary.org/wiki/school#English'])
W('systems','/ˈsɪstəmz/','系统；体系、制度；成套方法；system 的复数',
 '几个部分彼此配合，合起来能办成一件事，就是 system。systems 可说多套设备，也可说多种组织规则、运作方式。',
 'system + -s，/m/ 后读 /z/。经后期拉丁 systema 接希腊 systema 组织成的整体，与 syn- 一起、histanai 使站立相关的历史动词构成相连。',
 [['希腊 systema → 后期拉丁 systema → system','放在一起而成的整体 → 系统、体系'],['system + -s → systems','多个系统、体系或成套方法']],
 'computer systems 计算机系统；transport systems 交通系统；education systems 教育制度；heating systems 供暖系统。系统里的部分要按关系一起运作，未必都是机器。',
 'different systems；systems that work together。','systems 强调整体和内部关系，devices 常是一件件设备。several systems 可能各自又包含许多 devices，不能把二者按一对一理解。',
 ('The two booking systems do not share information automatically.','这两套预订系统不会自动共享信息。'),('The guide compares education systems in several countries.','指南比较了几个国家的教育制度。'),sources=['https://en.wiktionary.org/wiki/systems#English','https://en.wiktionary.org/wiki/system#English'])
W('activities','/ækˈtɪvətiz/','活动、行动；各项工作、业务；activity 的复数',
 '把人具体在做的事情一项项数出来，就是 activities：读书、徒步、做实验或公司的日常业务，都能按场景这么说。',
 'activity 的 y 前是辅音字母 t，加复数时变 -ies；末尾读 /tiz/。activity 与 active + -ity 对应，历史经法语 activite 接拉丁 activitas，不只是一条现代英语现场拼词的路线。',
 [['拉丁 activitas → 法语 activite → activity','行动、活跃的状态；具体活动'],['activity 变 y 为 i + -es → activities','多项活动、行动或业务']],
 'outdoor activities 户外活动；classroom activities 课堂活动；daily activities 日常活动；business activities 业务活动；a range of activities 一系列活动。',
 'activities for children；take part in activities。','activity 不可数时可强调活动量、活跃状态，如 little activity；activities 可数时数具体做的事。an event 常是一个有时间安排的活动，其中可以包含多项 activities。',
 ('The centre offers activities for people of all ages.','中心为各年龄段的人提供活动。'),('Reading and drawing were among the afternoon’s activities.','下午的活动包括阅读和画画。'),sources=['https://en.wiktionary.org/wiki/activities#English','https://en.wiktionary.org/wiki/activity#English'])
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_we',ROOTS,WORDS)
 extend_lessons()
