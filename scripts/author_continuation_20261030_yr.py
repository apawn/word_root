"""Frequent nouns with time, measurement, people and practical uses."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'C0301':dict(words=['date','dates'],label='date → dates：日期、约会；椰枣另源',note='果实名接手指相关的希腊词，日期名接拉丁给予词，明确分开两支。'),
 'C0498':dict(words=['degree','degrees'],label='degree → degrees：一步步的程度与等级',note='拉丁台阶材料经法语借入，现代温度、角度、学位各有单位或等级用法。'),
 'C0022':dict(words=['age','ages'],label='age → ages：年龄、时代与漫长时间',note='拉丁生命时间词族经法语借入；ages 可口语夸张地说很久。'),
 'B3065':dict(words=['death','deaths'],label='death → deaths：死亡与一例例死亡事件',note='本族死亡词延续，抽象状态与可数事件分开。'),
 'C0979':dict(words=['fee','fees'],label='fee → fees：牲畜财产旧词与服务费用',note='日耳曼财产词本族与法语支线合流；与拉丁 pecu 更远同源。'),
 'B2415':dict(words=['pound','pounds'],label='pound → pounds：重量、钱币；敲打另源',note='重量和货币义有历史联系，动词敲打与围栏等另有词支。'),
 'C1209':dict(words=['region','regions'],label='region → regions：方向、划界与地区',note='拉丁方向、界线与地区名词经法语等借入。'),
 'C0415':dict(words=['difference','differences'],label='difference → differences：不同之处与分歧',note='拉丁 differentia 名词借入，与 different 平行，不是后者现代临时变形。'),
 'B2689':dict(words=['expert','experts'],label='expert → experts：经试验、经历而熟悉的人',note='拉丁 experiri 的分词 expertus 经法语借入，英语形容词可转为专家名词。'),
 'B3774':dict(words=['representative','representatives'],label='representative → representatives：使他人呈现、在场的人',note='代表性形容词和代表名词的历史含法语、拉丁借入线。'),
 'C1319':dict(words=['season','seasons'],label='season → seasons：播种时节、季节与调味',note='时节和使适宜的词族经法语发展，调味义经使达到适宜状态的路线形成。'),
 'B3381':dict(words=['club','clubs'],label='club → clubs：棍棒、社团与梅花牌组',note='古诺尔斯棍棒词借入，社团与牌组名称各有后续发展。'),
 'B3031':dict(words=['cover','covers'],label='cover → covers：遮盖、封面与涉及',note='拉丁遮盖词经法语借入，现代按覆盖对象发展多种常用义。'),
 'B3159':dict(words=['loan','loans'],label='loan → loans：暂借之物与借出',note='北欧借词与 lend 同族，钱、书、设备等都能借出。'),
}
W('dates','/deɪts/','日期、约会；椰枣〔复数〕；标日期、交往〔第三人称单数〕',
 '日历上的一天、约好见面的那次安排，是 dates 的时间分支；棕榈果实椰枣也写 dates，来源要另分。',
 'date + -s，/t/ 后读 /s/。日期义经法语接拉丁 data 已给出的，日期来自文书写明交付时间的习惯，后有约会；椰枣义经法语、拉丁 dactylus 接希腊 daktylos，较早果名关系有争议。',
 [['拉丁 data → 法语 → 日期 date','文书给出时间 → 日期；约定见面'],['另支：希腊、拉丁果名 → 法语 → 椰枣 date；各加 -s','多个日期、约会或椰枣；动词形式']],
 'available dates 可选日期；go on dates 去约会；dried dates 椰枣干；dates from... 始于……。',
 'dates marked on the calendar；dates served with tea。','dates from the nineteenth century 是追溯到十九世纪，dates 是动词。果实 dates 与时间 date 近代字形重合，不从日历故事解释果名。',
 ('Please check the dates before booking the tickets.','订票前请核对日期。'),('She put a bowl of dates on the table.','她把一碗椰枣放在桌上。'),('The house dates from the nineteenth century.','这栋房子建于十九世纪。'),sources=['https://en.wiktionary.org/wiki/dates#English','https://www.etymonline.com/word/date'])
W('degrees','/dɪˈɡriːz/','度；程度、等级；学位〔degree 的复数〕',
 '沿着台阶一步步往上，便有不同层次、程度的画面；degrees 今天既可数温度、角度的度，也可说学位、不同程度。',
 'degree + -s，元音 /iː/ 后读 /z/。经古法语 degré 接拉丁 gradus 台阶、步，后来等级与测量刻度等用途各自固定。',
 [['拉丁 gradus → 古法语 degré → degree','台阶、一步 → 程度、等级、刻度'],['degree + -s → degrees','多个度数、等级或学位']],
 'twenty degrees 二十度；ninety degrees 九十度角；university degrees 大学学位；to varying degrees 在不同程度上。',
 'degrees shown on the thermometer；degrees of confidence。','degrees 只说度数时，要靠温度、角度等语境知道单位体系。学位 degrees 数资格等级；varying degrees 则用程度高低的抽象台阶。',
 ('The temperature rose by five degrees.','温度上升了五度。'),('The two roads meet at ninety degrees.','这两条路以九十度角相交。'),sources=['https://en.wiktionary.org/wiki/degrees#English','https://en.wiktionary.org/wiki/degree#English'])
W('ages','/ˈeɪdʒɪz/','年龄；时代；很久〔复数用法〕；变老〔第三人称单数〕',
 '每个人走过多少生命时间，是 ages 的年龄义；把历史按阶段分开，也有时代义。口语等了 ages，是夸张地说等了很久。',
 'age + -s，/dʒ/ 后增加 /ɪz/。age 经古法语接拉丁 aetās、aevum 一族的生命时间词；英语名词又形成变老等动词。',
 [['拉丁生命时间词族 → 古法语 → age','一生的时间、年龄 → 年龄、时代'],['age + -s → ages；动词与夸张用法','多个年龄、时期；变老；很长时间']],
 'people of all ages 各年龄的人；for ages 很久；through the ages 历经各时代；ages well 经年仍好、老得有风采。',
 'children of different ages；waited for ages。','for ages 往往是感受上的很久，未必真的过了几个历史时代。children of different ages 说不同年龄段的孩子。',
 ('The activity is suitable for people of all ages.','这项活动适合各年龄的人。'),('We waited for ages before the bus arrived.','我们等了好久，公共汽车才来。'),sources=['https://en.wiktionary.org/wiki/ages#English','https://en.wiktionary.org/wiki/age#English'])
W('deaths','/deθs/','死亡事件、死亡人数〔death 的复数〕',
 'death 可说死亡这种状态；把一次次死亡按事件或人数记录，就用 deaths。登记、统计语境里常见这个可数用法。',
 'death + -s，/θ/ 后读 /s/，词尾 /θs/ 连在一起。death 继承古英语 dēaþ，经中古英语发展，与 die、dead 同属旧词族。',
 [['古英语 dēaþ → 中古英语 → death','死亡；与 die、dead 的历史亲缘'],['death 的可数事件义 + -s → deaths','多例死亡、死亡人数']],
 'recorded deaths 有记录的死亡；births and deaths 出生与死亡；the number of deaths 死亡人数。',
 'deaths recorded in the register；deaths over the same period。','deaths 的 th 通常保留清音 /θ/，后面接 /s/。the number of deaths 的语法核心是 number，谓语通常按单数处理。',
 ('The old register records births and deaths in the village.','旧登记册记录着村里的出生和死亡情况。'),('The report compares the number of deaths over two periods.','报告比较了两个时期的死亡人数。'),sources=['https://en.wiktionary.org/wiki/deaths#English','https://en.wiktionary.org/wiki/death#English'])
W('fees','/fiːz/','费用、服务费、学费等〔fee 的复数〕',
 '为了某项服务、资格或参与机会付的钱，是 fees；不同项目的一笔笔收费，常合起来用复数说。',
 'fee + -s，元音后读 /z/。fee 是古英语 feoh 牲畜、财产、钱财与盎格鲁法语相关封地、支付词的合流；更早牲畜曾代表财富，与拉丁 pecu 远同源，非直接从拉丁借来。',
 [['本族 feoh 与法语相关支线 → fee','牲畜、财产、支付 → 工作服务报酬与收费'],['fee + -s → fees','多项费用、若干笔服务费']],
 'tuition fees 学费；membership fees 会费；entry fees 参赛、入场费；service fees 服务费。',
 'fees listed on the form；fees for the course。','fee 通常与具体服务、资格相连。fees 只说明有若干项或总体收费，实际包括哪些项目仍要看紧邻说明。',
 ('The course fees include all printed materials.','课程费用包含全部印刷材料。'),('Membership fees are listed on the application form.','会费列在申请表上。'),sources=['https://en.wiktionary.org/wiki/fees#English','https://www.etymonline.com/word/fee'])
W('pounds','/paʊndz/','磅；英镑等货币单位〔复数〕；猛敲、捣碎〔第三人称单数，另一支〕',
 '称重量的磅和英国货币的镑，是 pounds 的计量分支；连续用力敲打，也写 pounds，却来自另一条动词历史。',
 'pound + -s，/d/ 后读 /z/。重量、钱币义接古英语 pund，较早借自拉丁 pondō 按重量，货币与按银重量计价有关；敲打义接古英语 pūnian，后来的 d 不是重量词造出的。',
 [['拉丁 pondō → 古英语 pund → pound','重量单位；也用于计钱'],['古英语 pūnian → pounen → 敲打 pound；各加 -s','敲、捣 → 单数主语敲打；或多磅、多镑']],
 'weighs ten pounds 重十磅；costs ten pounds 售价十镑；pounds on the door 猛敲门；pounds the spices 捣香料。',
 'pounds shown on the scale；pounds spent on books。','weighs、costs 常能区分在说重量还是钱。pounds on the door 的 pounds 是动词，要读出敲打动作；围栏等同形旧词另有来源。',
 ('The parcel weighs three pounds.','这个包裹重三磅。'),('She spent twenty pounds on the books.','她买这些书花了二十英镑。'),('He pounds the spices in a small bowl.','他在一个小碗里捣香料。'),sources=['https://en.wiktionary.org/wiki/pounds#English','https://www.etymonline.com/word/pound'])
W('regions','/ˈriːdʒənz/','地区、区域；身体等的部位〔region 的复数〕',
 '把较大的范围按方向、边界或特点划开，一块块区域就是 regions；地理、图像、身体描述都能各自划区域。',
 'region + -s，/n/ 后读 /z/。拉丁 regiō、regiōn- 有方向、界线、地区等义，与 regere 指引词族相连，经法语、拉丁借入英语。',
 [['拉丁 regere、regiōn- → 法语、英语 region','方向、划界 → 地区、区域'],['region + -s → regions','多个区域、部位']],
 'coastal regions 沿海地区；mountain regions 山区；different regions of the image 图像的不同区域。',
 'regions with similar weather；regions marked in red。','region 的范围由所讨论的对象决定，不一定是正式行政区。regions of an image 是图像里划出的区域，沿用空间划分的共同画面。',
 ('The survey includes several coastal regions.','这项调查涵盖几个沿海地区。'),('The software compares different regions of the image.','软件比较图像中的不同区域。'),sources=['https://en.wiktionary.org/wiki/regions#English','https://en.wiktionary.org/wiki/region#English'])
W('differences','/ˈdɪfərənsɪz/','差别、不同之处；分歧〔difference 的复数〕',
 '把两样东西放在一起看，哪些地方不一样，就是 differences；人们在看法上不一样，也能说 differences。',
 'difference + -s，/s/ 后增加 /ɪz/。名词经法语 difference 或直接拉丁 differentia 借入，接 differēns 不同的词干，与拉丁 differre 分开带、不同相连；和 different 有平行借入历史。',
 [['拉丁 differre、differēns → differentia → difference','分开、不同 → 不同之处'],['difference + -s → differences','多个差别；不同意见、分歧']],
 'differences between... ……之间的差别；cultural differences 文化差异；resolve differences 解决分歧。',
 'differences in size；differences of opinion。','differences between A and B 说明比较对象，differences in colour 说明在哪一方面不同。differences of opinion 是观点分歧，不能只理解成外形差别。',
 ('The diagrams show differences in size and shape.','图示展示了大小和形状上的差别。'),('They discussed their differences before making a decision.','作决定前，他们讨论了彼此的分歧。'),sources=['https://en.wiktionary.org/wiki/differences#English','https://en.wiktionary.org/wiki/difference#English'])
W('experts','/ˈekspɜːts/；美式常 /ˈekspɜːrts/','专家、行家〔expert 的复数〕',
 '在某个领域经过学习、实践，真的试过、熟悉怎样做的人，是 experts。它和 experience 的较早词族，都接到尝试、经历这条线上。',
 'expert + -s，/t/ 后读 /s/。拉丁 experīrī 尝试、检验的分词 expertus，表示经过试验、凭经历知道的，经法语 expert、espert 借入，英语又把形容词用作人名词。',
 [['拉丁 experīrī → expertus → 法语 → expert','经过尝试、经历而熟悉 → 专门熟练的'],['expert 名词 + -s → experts','有专门知识、技能的人']],
 'language experts 语言专家；experts in the field 该领域专家；ask the experts 请教行家。',
 'experts invited to the workshop；experts on local history。','experts in 或 on 后面交代领域。一个领域的专家身份不自动扩展到所有领域，读文章时看清在说什么专长。',
 ('The museum invited experts on local history.','博物馆邀请了研究当地历史的专家。'),('Several experts helped examine the old documents.','几位专家协助检视了这些旧文献。'),sources=['https://en.wiktionary.org/wiki/experts#English','https://en.wiktionary.org/wiki/expert#English'])
W('representatives','/ˌreprɪˈzentətɪvz/','代表、代理人、业务代表〔representative 的复数〕',
 '一个人到场，却替一个群体把意见带来、把事情办好，就是 representative；多个这样的人便是 representatives。',
 'representative + -s，/v/ 后读 /z/。representative 经法语 representatif 或中世纪拉丁 repraesentativus 借入，接 repraesentāre 使呈现词族；现代可对照 represent + -ative，名词代表用法另有发展。',
 [['拉丁、法语代表性的材料 → representative','使他人呈现、代表性的 → 代表者'],['representative 名词 + -s → representatives','多个代表、代理人']],
 'student representatives 学生代表；sales representatives 销售代表；representatives from each team 各团队代表。',
 'representatives attending the meeting；elected representatives。','representative 作形容词可说有代表性的；representatives 在这里是人。来自某团体常用 from，代表某群体也常见 of。',
 ('Representatives from each team attended the meeting.','每个团队的代表都出席了会议。'),('The students elected two representatives.','学生们选出了两名代表。'),sources=['https://en.wiktionary.org/wiki/representatives#English','https://en.wiktionary.org/wiki/representative#English'])
W('seasons','/ˈsiːzənz/','季节；赛季、某项活动的时期〔复数〕；调味〔第三人称单数〕',
 '一年里适合某件事的那段时间，是 seasons 的时节画面；体育比赛、旅游、剧集也会按自己的周期分季。调味动词则接使味道达到适宜状态的历史用法。',
 'season + -s，/n/ 后读 /z/。拉丁 satiō 播种经法语 seison、saison 发展到播种时节、适宜时间；调味动词还接法语 saisonner、assaisonner 使成熟、使适宜等形式。',
 [['拉丁播种名词 → 法语时节词 → season','播种 → 合宜时段、季节'],['相关法语使适宜、调味动词 → season；加 -s → seasons','多个季节或周期；单数主语调味']],
 'the four seasons 四季；rainy seasons 雨季；football seasons 足球赛季；seasons the soup 给汤调味。',
 'seasons of the year；seasons the vegetables with herbs。','seasons 作名词按自然或活动周期分段；作动词直接接要调味的食物，with 引出材料。可从合宜时间、达到合适状态理解两条后续用法。',
 ('The photographs show the garden in all four seasons.','这些照片展示了花园四季的样子。'),('She seasons the soup with fresh herbs.','她用新鲜香草给汤调味。'),sources=['https://en.wiktionary.org/wiki/seasons#English','https://www.etymonline.com/word/season'])
W('clubs','/klʌbz/','俱乐部、社团；球杆、棍棒；梅花牌组〔复数〕',
 '一群人为了共同爱好聚在一起，是 clubs 的社团义；球杆、棍棒是更早的器物义。扑克牌 clubs 今天用三叶形图案，中文通常叫梅花。',
 'club + -s，/b/ 后读 /z/。古诺尔斯语 klubba 等棍棒词借入；社团义一般联系较晚聚成一团、联合的用法。牌组名保留棒的名称背景，英语牌面采用法式三叶图案。',
 [['古诺尔斯语 klubba 等 → club','棍棒 → 运动用杆；牌组名称保留棒的历史'],['聚成团的用法 → 社团 club；加 -s → clubs','多个社团、球杆；梅花牌组']],
 'sports clubs 体育俱乐部；school clubs 学校社团；golf clubs 高尔夫球杆；the ace of clubs 梅花 A。',
 'clubs meeting after school；clubs stored in a bag。','school clubs 数社团，golf clubs 数球杆。牌名中的 clubs 是固定牌组名；a club 在相应牌局中还可说一张梅花牌。',
 ('The school offers several clubs after class.','学校课后开设了几个社团。'),('He put the golf clubs in the car.','他把高尔夫球杆放进了车里。'),('She placed the ace of clubs on the table.','她把梅花 A 放在了桌上。'),sources=['https://en.wiktionary.org/wiki/clubs#English','https://www.etymonline.com/word/club'])
W('covers','英 /ˈkʌvəz/；美 /ˈkʌvərz/','封面、外罩；被褥〔复数〕；覆盖、涉及、支付〔第三人称单数〕',
 '盖在外面的那一层，是 covers 的封面、外罩义；动词把范围罩住后，可以说内容涉及多少，费用够付多少。',
 'cover + -s，词尾 /ə/ 或 /ər/ 后读 /z/。古法语 covrir 接拉丁 cooperīre，co- 加强，operīre 遮盖；英语名词、动词发展出不同覆盖用途。',
 [['拉丁 cooperīre → 古法语 covrir → cover','遮盖 → 覆盖、外罩等'],['cover + -s → covers；范围、费用扩展','多个封面或罩；单数主语涉及、足以支付']],
 'book covers 书封面；pull up the covers 拉起被子；covers the cost 支付、足够覆盖费用；covers the topic 涉及主题。',
 'covers on the chairs；the fee covers materials。','covers 作动词时，看宾语：the bed 是盖住，the topic 是内容涵盖，the cost 是费用得到支付或补足。作被褥名词常用复数 the covers。',
 ('The book covers were designed by local artists.','这些书的封面由当地艺术家设计。'),('The course fee covers all materials.','课程费用包含全部材料。'),sources=['https://en.wiktionary.org/wiki/covers#English','https://en.wiktionary.org/wiki/cover#English'])
W('loans','英 /ləʊnz/；美 /loʊnz/','借款；借出物、借用安排〔复数〕；借出〔第三人称单数〕',
 '把钱、书或设备暂时交给别人、以后需要归还，就是 loan 的借用画面；loans 可以数这些借款、借出项目。',
 'loan + -s，/n/ 后读 /z/。loan 经中古英语接古诺尔斯语 lán，与 lend 同族；英语名词又发展为借出动词，动词用法在美式英语尤其常见。',
 [['古诺尔斯语 lán → 中古英语 → loan','暂时借用、借出安排'],['loan + -s → loans；名词转动词','多笔借款或借出物；单数主语借出']],
 'book loans 图书借阅；equipment loans 设备借用；loans from a bank 银行借款；loans equipment to schools 向学校借出设备。',
 'loans recorded by the library；loans a camera to a visitor。','loan、lend 的动词方向通常是借出去；borrow 是借进来。loan 不只说钱，图书馆和设备中心也可有 loans。',
 ('The library records all book loans electronically.','图书馆用电子方式记录全部图书借阅。'),('The centre loans cameras to local schools.','这个中心向当地学校借出相机。'),sources=['https://en.wiktionary.org/wiki/loans#English','https://en.wiktionary.org/wiki/loan#English'])
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_yr',ROOTS,WORDS)
 extend_lessons()
