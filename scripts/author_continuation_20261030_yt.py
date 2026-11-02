"""Everyday periods, occasions, traditions and repeated actions."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'B2494':dict(words=['morning','mornings'],label='morning → mornings：一次次清晨',note='本族清晨词的旧派生延续，现代复数常说每逢早晨。'),
 'C0823':dict(words=['afternoon','afternoons'],label='afternoon → afternoons：正午之后',note='after 与 noon 的本族复合，按每天的时间段形成复数。'),
 'B2437':dict(words=['weekend','weekends'],label='weekend → weekends：一周尾段与休息时段',note='week 与 end 的现代组合，具体所指依作息习惯判断。'),
 'B2422':dict(words=['holiday','holidays','birthday','birthdays'],label='holiday／birthday：神圣的日子与出生纪念日',note='日子词分别与 holy、birth 组合，现代意义各自发展。'),
 'C0196':dict(words=['century','centuries'],label='century → centuries：一百为组与百年',note='拉丁百的分组名借入后，现代常用作一百年。'),
 'C0056':dict(words=['anniversary','anniversaries'],label='anniversary → anniversaries：每年转回的纪念日期',note='拉丁年与转回的材料组合，现代可纪念多种事情。'),
 'A1771':dict(words=['ceremony','ceremonies'],label='ceremony → ceremonies：礼仪与仪式',note='拉丁礼仪词整体借入，更早来源未定，不按现代字母硬拆。'),
 'B4012':dict(words=['celebration','celebrations'],label='celebration → celebrations：庆祝与庆祝活动',note='法语、拉丁名词独立借入，英语现代与 celebrate 对照认形。'),
 'A1958':dict(words=['festival','festivals'],label='festival → festivals：节日与文化节庆',note='节日的形容词经名词化形成活动名称，现代音乐、电影等也可办节。'),
 'C1535':dict(words=['tradition','traditions'],label='tradition → traditions：传交下来的习俗与观念',note='越过、给的拉丁材料形成交付、传承词，名词经法语等借入。'),
 'C0515':dict(words=['habit','habits'],label='habit → habits：保持的状态与惯常做法',note='拉丁拥有、保持词族经法语形成衣着、状态、习惯等意义。'),
 'C1240':dict(words=['routine','routines'],label='routine → routines：走惯的路与固定程序',note='法语 route 道路加词尾形成惯常做法，英语借入后扩至表演和软件程序。'),
}
W('mornings','英 /ˈmɔːnɪŋz/；美 /ˈmɔːrnɪŋz/','早晨、上午〔复数〕；每逢早晨、上午〔时间用法〕',
 '每天从夜晚转入白天的那一段，可以一次次说成 mornings；说工作日早晨常做什么，复数也能表示重复的时间习惯。',
 'morning + -s，/ŋ/ 后读 /z/。morning 接中古英语 morwenynge 等清晨词的旧派生，与较旧 morn、morwen 相连；不是现代一个普通动词正在做的 ing 形式。',
 [['较旧清晨词 morwen、morn → morning','早晨名称的旧派生'],['morning + -s → mornings','多个早晨；惯常在早晨的时间表达']],
 'cold mornings 寒冷的早晨；on Monday mornings 每周一早晨；in the mornings 在早晨、上午。',
 'mornings spent reading；works mornings。','on Monday mornings 常说明每周反复发生。morning 与 mourning 哀悼常同音，写法和历史不同；具体时间还要按生活场景理解。',
 ('She walks to work on Monday mornings.','她每周一早晨步行上班。'),('The mornings were cold, but the afternoons were warm.','早晨很冷，下午却很暖和。'),sources=['https://en.wiktionary.org/wiki/mornings#English','https://en.wiktionary.org/wiki/morning#English'])
W('afternoons','英 /ˌɑːftəˈnuːnz/；美 /ˌæftərˈnuːnz/','下午〔复数〕；每逢下午〔时间用法〕',
 'noon 是正午，after noon 就是正午之后；把一天天下午的时段分开看，就得到 afternoons。',
 'after + noon → afternoon，末尾加 -s，/n/ 后读 /z/。这个组合在中古英语已有相应形式，今天已经是一个完整时间名词。',
 [['after 在之后 + noon 正午 → afternoon','正午之后的时间段'],['afternoon + -s → afternoons','多个下午；反复在下午的时间用法']],
 'on Sunday afternoons 每周日下午；in the afternoons 在下午；spend afternoons reading 下午读书。',
 'quiet afternoons at home；works afternoons。','in the afternoon 泛说下午，on Sunday afternoons 说明每逢周日下午。名词前的时间介词由具体表达决定，不能只按一个固定中文词选。',
 ('We meet on Sunday afternoons to practise music.','我们每周日下午见面练音乐。'),('She spent the afternoons reading in the garden.','那些下午，她都在花园里读书。'),sources=['https://en.wiktionary.org/wiki/afternoons#English','https://en.wiktionary.org/wiki/afternoon#English'])
W('weekends','/ˌwiːkˈendz/、/ˈwiːkendz/','周末〔复数〕；在周末〔时间用法〕',
 '一周走到尾段、常安排休息和外出的日子，是 weekends；复数常说每逢周末的习惯。',
 'week 周 + end 末端 → weekend，再加 -s，/d/ 后读 /z/。组合从一周尾段的表达形成现代名称，休息安排影响了它的常用范围。',
 [['week + end → weekend','一周的末段 → 周末名称'],['weekend + -s → weekends','多个周末；周末反复做某事']],
 'at weekends 周末〔英式常见〕；on weekends 周末〔美式常见〕；long weekends 连休的长周末。',
 'weekends spent outdoors；works weekends。','at weekends、on weekends 都能表达惯常周末，各地区偏好不同。this weekend 说这次周末，常不加介词。',
 ('They often visit the lake at weekends.','他们周末常去湖边。'),('She works weekends and takes Mondays off.','她周末工作，周一休息。'),sources=['https://en.wiktionary.org/wiki/weekends#English','https://en.wiktionary.org/wiki/weekend#English'])
W('holidays','英 /ˈhɒlədeɪz/；美 /ˈhɑːlədeɪz/','假日、节日；假期〔复数〕；度假〔第三人称单数〕',
 '从平常劳作中留出来庆祝、休息的日子，是 holidays。更早是神圣的节日，后来范围扩大到休假、旅行等。',
 'holiday + -s，元音后读 /z/。古英语 hāliġ 神圣与 dæġ 日组成 hāliġdæġ，经中古英语发展为 holiday；后来读音、用法与逐词 holy day 有所分化。',
 [['古英语 holy 与 day 的旧组合 → holiday','宗教节日 → 休息、娱乐的假日'],['holiday + -s → holidays；名词转动词','多个假日、一段假期；单数主语度假']],
 'school holidays 学校假期；public holidays 公共假日；summer holidays 暑假；on holiday 在度假〔英式常见〕。',
 'holidays spent with family；holidays marked on the calendar。','英式 holidays 常说假期、度假，美式日常也常用 vacation 表示休假；the holidays 在美式特定语境常指年末节日期间。具体仍看上下文。',
 ('The children visit their grandparents during the school holidays.','孩子们在学校假期去看望祖父母。'),('The calendar marks public holidays in red.','日历用红色标出公共假日。'),sources=['https://en.wiktionary.org/wiki/holidays#English','https://www.etymonline.com/word/holiday'])
W('birthdays','英 /ˈbɜːθdeɪz/；美 /ˈbɜːrθdeɪz/','生日〔birthday 的复数〕',
 '出生那天在每一年重新到来，就有生日；同一年不同人的、同一个人不同年的纪念日，都可以用 birthdays。',
 'birth 出生 + day 日 → birthday，再加 -s，/eɪ/ 后读 /z/。英语较早已有相应出生之日组合，后来用于周年生日。',
 [['birth + day → birthday','出生之日及每年的纪念日'],['birthday + -s → birthdays','多个生日、不同年的生日']],
 'celebrate birthdays 庆祝生日；remember birthdays 记住生日；birthday cards 生日卡片〔修饰语用单数〕。',
 'birthdays in the same month；birthdays celebrated at home。','birthdays 数生日，birthday cards 中 birthday 说明卡片用途，通常不加 s。生日一般是一年一次，出生日期本身则是特定年月日。',
 ('Their birthdays are in the same month.','他们的生日在同一个月。'),('She keeps a list of family birthdays.','她保留着一份家人生日清单。'),sources=['https://en.wiktionary.org/wiki/birthdays#English','https://en.wiktionary.org/wiki/birthday#English'])
W('centuries','/ˈsentʃəriz/','多个世纪；几百年〔century 的复数〕',
 '一百年合成一个大时间格，是 a century；把这样的时间格接起来，就是 centuries，日常也可泛说几百年。',
 'century 的 y 前是辅音 r，变 y 为 i 加 -es，词尾读 /z/。拉丁 centuria 原指一百组成的单位，经法语、中古英语进入，百年义成为日常核心。',
 [['拉丁 centuria → 法语、中古英语 → century','一百为组 → 一百年的时段'],['century → centuries','y 变 i 加 es；多个百年时段']],
 'for centuries 几百年来；over the centuries 历经数百年；two centuries 两个世纪、两百年。',
 'centuries of history；centuries after the event。','two centuries 可是一段连续两百年，不必只说两个日历世纪。for centuries 不给确切起止时点，主要突出时间久远。',
 ('The bridge has stood for centuries.','这座桥屹立了几百年。'),('The town changed greatly over the following two centuries.','接下来的两百年里，这个镇变化很大。'),sources=['https://en.wiktionary.org/wiki/centuries#English','https://en.wiktionary.org/wiki/century#English'])
W('anniversaries','英 /ˌænɪˈvɜːsəriz/；美 /ˌænɪˈvɜːrsəriz/','周年纪念日〔anniversary 的复数〕',
 '日历绕了一年，同一个日期又转回来，是 anniversaries 的核心画面。结婚、创立、事件发生，都可以有周年纪念日。',
 'anniversary 的 y 前是辅音 r，变 y 为 i 加 -es，词尾 /z/。拉丁 annus 年与 vertere 的 versus 转回材料组成 anniversārius 每年返回的，中世纪拉丁名词形式进入英语。',
 [['拉丁 annus + versus → anniversārius、anniversarium','年 + 转回 → 每年回来的纪念日期'],['anniversary → anniversaries','多个周年纪念日']],
 'wedding anniversaries 结婚纪念日；important anniversaries 重要周年纪念日；mark anniversaries 纪念周年。',
 'anniversaries remembered by the family；anniversaries of major events。','anniversary 不限结婚，也可用于组织成立、历史事件等。birthdays 通常专说生日；anniversaries 的范围更广。',
 ('The family keeps photographs from important anniversaries.','家人保存着重要周年纪念日的照片。'),('The museum marks anniversaries of major local events.','博物馆纪念当地重大事件的周年。'),sources=['https://en.wiktionary.org/wiki/anniversaries#English','https://www.etymonline.com/word/anniversary'])
W('ceremonies','英 /ˈserəməniz/；美 /ˈserəmoʊniz/','仪式、典礼〔ceremony 的复数〕',
 '为了标记一件重要的事，按一定次序和礼节进行的一场场活动，是 ceremonies；毕业、开幕、颁奖都可以有典礼。',
 'ceremony 的 y 前是辅音 n，变 y 为 i 加 -es，词尾 /z/。ceremony 经法语、中古英语接拉丁 caerimōnia 等礼仪、敬意词，更早来源不确定。',
 [['拉丁 caerimōnia 等 → 法语、中古英语 → ceremony','礼仪、敬意 → 一场正式仪式'],['ceremony → ceremonies','y 变 i 加 es；多场仪式、典礼']],
 'graduation ceremonies 毕业典礼；opening ceremonies 开幕式；award ceremonies 颁奖典礼。',
 'ceremonies held in the hall；ceremonies marking a new beginning。','ceremony 强调仪式、礼节上的次序和意义；celebration 强调庆祝。一次活动可以同时具有这两个性质。',
 ('The hall is used for graduation ceremonies.','这个大厅用来举办毕业典礼。'),('The exhibition shows photographs of local ceremonies.','展览展示了当地仪式活动的照片。'),sources=['https://en.wiktionary.org/wiki/ceremonies#English','https://en.wiktionary.org/wiki/ceremony#English'])
W('celebrations','/ˌseləˈbreɪʃənz/','庆祝活动；庆典〔celebration 的复数〕',
 '值得高兴或纪念的事情发生了，人们把这种喜悦变成聚会、表演等活动，就是 celebrations；复数常把一系列庆祝一起说。',
 'celebration + -s，/n/ 后读 /z/。celebration 经法语或拉丁 celebrātiō 借入，与 celebrāre 庆祝、赞颂词族相连；现代可对照 celebrate 与 -ion，但名词有独立来路。',
 [['拉丁 celebrāre、celebrātiō → 法语、英语 celebration','庆贺、赞颂 → 庆祝行为或活动'],['celebration + -s → celebrations','多场或一系列庆祝活动']],
 'birthday celebrations 生日庆祝；anniversary celebrations 周年庆祝；join the celebrations 参加庆祝。',
 'celebrations lasting all day；celebrations in the town square。','celebration 可泛说庆祝，celebrations 常把多项安排或整个庆祝场面合起来。celebrity 名人与它较早同族，现代却不是同一个意思。',
 ('The celebrations continued in the square after sunset.','日落后，广场上的庆祝活动仍在继续。'),('The school planned several celebrations for its anniversary.','学校为周年纪念安排了几场庆祝活动。'),sources=['https://en.wiktionary.org/wiki/celebrations#English','https://en.wiktionary.org/wiki/celebration#English'])
W('festivals','/ˈfestɪvəlz/','节日；音乐节、电影节等集中活动〔festival 的复数〕',
 '把大家聚起来，集中庆祝、欣赏表演或作品的一段活动，是 festivals；既可以是传统节庆，也可以围绕音乐、电影来办节。',
 'festival + -s，/l/ 后读 /z/。festival 先经法语或中世纪拉丁 festīvālis 作节日的形容词，较早接拉丁 festum 节庆；英语从 festival day 等表达发展出活动名词。',
 [['拉丁 festum、festīvālis → festival 形容词','节庆 → 节日的'],['英语活动名词 festival + -s → festivals','多个节庆；不同主题的文化节']],
 'music festivals 音乐节；film festivals 电影节；local festivals 当地节庆。',
 'festivals held each summer；festivals celebrating local food。','festival 不一定是法定放假日，也可是一组专门活动。holiday 更常关注假日、休息安排，festival 更常关注节庆内容。',
 ('The town hosts music festivals every summer.','这个镇每年夏天举办音乐节。'),('The museum collects stories about local festivals.','博物馆收集当地节庆的故事。'),sources=['https://en.wiktionary.org/wiki/festivals#English','https://en.wiktionary.org/wiki/festival#English'])
W('traditions','/trəˈdɪʃənz/','传统、传承下来的做法或观念〔tradition 的复数〕',
 '上一代把做法、故事、观念交给下一代，东西就沿着人群传下来了，这些是 traditions。词根的交付、递过去很适合记传承。',
 'tradition + -s，/n/ 后读 /z/。拉丁 trans- 越过与 dare 给形成 trādere 交付，其名词 trāditiō 经古法语等借入，现代的 tra- 是历史压缩形式。',
 [['拉丁 trans- + dare → trādere、trāditiō → tradition','给过去、交付 → 传承'],['tradition + -s → traditions','多种流传下来的观念、做法']],
 'family traditions 家庭传统；local traditions 当地传统；oral traditions 口头传承；keep traditions alive 让传统延续。',
 'traditions passed down through generations；traditions around the festival。','traditions 可以是仪式，也可以是饮食、讲故事、节日习惯。一次个人偶然行为未必成传统，重点在持续传承、共同延续。',
 ('The festival keeps several local traditions alive.','这个节庆让几项当地传统延续下来。'),('The children learned about family traditions from their grandparents.','孩子们从祖父母那里了解了家庭传统。'),sources=['https://en.wiktionary.org/wiki/traditions#English','https://en.wiktionary.org/wiki/tradition#English'])
W('habits','/ˈhæbɪts/','习惯、惯常做法〔habit 的复数〕',
 '一件事反复做，后来做起来很自然，就成了 habits；它常贴着一个人或群体稳定的行为方式来理解。',
 'habit + -s，/t/ 后读 /s/。拉丁 habēre 拥有、保持的 habitus 表示状态、姿态、衣着和习性，经古法语 habit、abit 进入英语，现代常用行为习惯义。',
 [['拉丁 habēre、habitus → 古法语 → habit','保持的状态、样态等 → 惯常行为'],['habit + -s → habits','多个习惯、惯常做法']],
 'reading habits 阅读习惯；daily habits 日常习惯；form habits 养成习惯；change old habits 改变旧习惯。',
 'habits learned at home；habits that develop over time。','habit 常说反复形成的具体做法；routine 常把一串固定步骤、日程框起来。每天先读书再散步可是一套 routine，其中的读书也可以是一项 habit。',
 ('The survey asks students about their reading habits.','这项调查向学生询问阅读习惯。'),('Some habits develop slowly over many years.','有些习惯是在多年里慢慢形成的。'),sources=['https://en.wiktionary.org/wiki/habits#English','https://en.wiktionary.org/wiki/habit#English'])
W('routines','/ruːˈtiːnz/','固定流程、日常安排；表演成套动作；程序例程〔复数〕',
 '一条走惯的路，每次差不多照着走，是 routines 最容易记的画面；工作步骤、舞蹈动作、软件操作都能形成固定的一套。',
 'routine + -s，/n/ 后读 /z/。法语 routine 由 route 道路、惯常路径加 -ine 形成，英语借入后有惯常流程、排练动作及软件程序用法；route 的拉丁更早背景接 rupta 被开辟的路。',
 [['法语 route + -ine → routine → 英语 routine','走惯的路 → 惯常做事流程'],['routine + -s → routines；专业用途扩展','多套日常安排、表演动作或程序例程']],
 'daily routines 日常流程；dance routines 成套舞蹈动作；software routines 软件例程。',
 'routines followed each morning；routines practised for the show。','routine 作形容词时也可说例行的；routines 在这里是名词，数一套套固定步骤。舞台上的 routine 强调排练好的一串动作。',
 ('The children soon became familiar with the classroom routines.','孩子们很快熟悉了课堂里的固定流程。'),('The dancers practised their routines before the show.','舞者在演出前练习各自的成套动作。'),sources=['https://en.wiktionary.org/wiki/routines#English','https://www.etymonline.com/word/routine'])
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_yt',ROOTS,WORDS)
 extend_lessons()
