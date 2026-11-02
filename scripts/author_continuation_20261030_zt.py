"""Common activities and everyday digital vocabulary."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'A2238':dict(words=['struggle','struggling'],label='struggle → struggling：费力地与阻力相持',note='中古英语奋力动作词，远源及 le 的具体基础材料未定。'),
 'B2877':dict(words=['hide','hiding'],label='hide → hiding：把东西放到看不见处',note='藏的动词继承古英语 hydan，与皮的名词路径分开看。'),
 'B3067':dict(words=['list','listing'],label='list → listing：把项目列出；倾斜另支',note='清单的条带背景与船体倾斜不同，现代 ing 可命名条目、刊登信息。'),
 'C0425':dict(words=['finish','finishing'],label='finish → finishing：做到终点',note='法语 finiss 形态接拉丁 finis 终点，ish 不同于性质后缀。'),
 'C1480':dict(words=['protect','protecting'],label='protect → protecting：在前面盖住、挡住',note='拉丁 pro 与 tegere，英语接 protectus 分词材料。'),
 'B3679':dict(words=['coach','coaching'],label='coach → coaching：载人前进到辅导',note='车辆词经法语、德语接匈牙利地名相关称呼，辅导比喻后来发展。'),
 'B3132':dict(words=['stop','stops','stopping'],label='stop → stops → stopping：阻住继续的动作',note='本族堵塞词，ing 前双写 p。'),
 'C0196':dict(words=['cent','cents'],label='cent → cents：一百到货币的百分之一',note='法语及拉丁百的词族，在货币单位中形成较小份额。'),
 'B2512':dict(words=['disease','diseases'],label='disease → diseases：失去安适到疾病',note='法语 desaise 的不舒适旧义，后来专门化为疾病。'),
 'C1072':dict(words=['application','applications','app','apps'],label='application → applications；app → apps：应用程序与缩短词',note='应用名词历史较早，计算机应用义与 app 的现代缩短后发展。'),
 'B3267':dict(words=['shop','shops'],label='shop → shops：店铺与购物',note='本族及日耳曼棚舍相关词发展为商店，动词后表购物。'),
 'B4085':dict(words=['website','websites','site','sites'],label='website → websites；site → sites：网络站点',note='web 与 site 的现代组合，整个站点和其中网页区分。'),
 'C0015':dict(words=['address','addresses'],label='address → addresses：朝向、目的地与处理',note='法语指向、使直词接通俗拉丁重构形式，名词动词后续发展。'),
}
W('struggling','/ˈstrʌɡəlɪŋ/','奋力、挣扎；做起来很吃力〔现在分词、动名词〕',
 '前面有阻力，自己还在使力，进得不轻松，就是 struggling。可以是搬动重物，也可以是读不懂、忙不过来或难以维持。',
 'struggle 去 e + -ing → struggling。底词接中古英语 strogelen、struglen 等奋力、扭打词，较早可能有反复动作 le 的构成，但基础词与远源未定。',
 [['中古英语 strogelen 等 → struggle','身体相持、费力 → 与各种困难相持'],['struggle 去 e + -ing → struggling','正在奋力；处于进展困难的状态']],
 'struggling to understand 努力却难以理解；struggling with the task 做任务很吃力；a struggling business 经营困难的企业。',
 'struggling for balance 奋力保持平衡；struggling to keep up 跟得很吃力。','struggling 不只是努力，也把困难、阻力带出来。struggle with 给难对付的对象，struggle to do 给很难做到的动作。',
 ('She is struggling to understand the instructions.','她正在费力理解说明。'),('The small shop is struggling to stay open.','小店正在艰难维持营业。'),sources=['https://en.wiktionary.org/wiki/struggling#English','https://www.etymonline.com/word/struggle'])
W('hiding','/ˈhaɪdɪŋ/','隐藏、躲藏〔现在分词、动名词〕；藏身状态',
 '把自己或东西移到别人看不见、找不到的位置，是 hiding。信息也能被藏起来，让外人暂时不知道。',
 'hide 去 e + -ing → hiding。藏的动词继承古英语 hȳdan，经中古英语延续；皮的名词 hide 有另一古英语 hȳd 路径，这里的 ing 接隐藏动词。',
 [['古英语 hȳdan → hide 动词','盖住、藏起 → 让人看不见、暂时不让人知道'],['hide 去 e + -ing → hiding','躲藏过程；in hiding 的藏身状态']],
 'hiding behind the door 躲在门后；hiding the keys 藏钥匙；in hiding 躲藏着。',
 'hiding a surprise 暂藏一个惊喜；hiding from the visitors 躲着来访的人。','hide something 是把东西藏起，hide 是自己躲。hiding from somebody 说明躲谁；常用过去式 hid，过去分词 hidden。',
 ('The cat is hiding under the bed.','猫躲在床底下。'),('She was hiding the present until his birthday.','她把礼物藏到他生日时才拿出来。'),sources=['https://en.wiktionary.org/wiki/hiding#English','https://en.wiktionary.org/wiki/hide#English'])
W('listing','/ˈlɪstɪŋ/','列出、刊登〔现在分词〕；清单、登记条目、刊登信息；倾斜〔另一动词用途〕',
 '把内容一项项放到别人能查看的名单上，是 listing。一次房源、职位刊登的信息，也常叫 a listing。',
 'list + -ing → listing。清单词较早有条带、边条及条状记录背景；名词 listing 后给列举过程、条目、公开信息命名。船体倾斜的 list 则另源不明。',
 [['清单 list → listing','列举 → 一份清单、一个登记或刊登条目'],['另支 list 倾斜 + -ing → listing','同形的过程词，按船体场景区分']],
 'listing the names 列出姓名；a job listing 招聘信息；a property listing 房源信息。',
 'a listing of local services 当地服务清单；listing to one side 向一边倾斜。','a listing 可以是一份目录，也可以是目录中的一条信息。listing the options 则是动词直接带宾语，表示正在列选项。',
 ('She is listing the tools needed for the repair.','她正在列维修所需的工具。'),('The website has a new job listing from a local company.','网站上有一家本地公司的新招聘信息。'),sources=['https://en.wiktionary.org/wiki/listing#English','https://en.wiktionary.org/wiki/list#English'])
W('finishing','/ˈfɪnɪʃɪŋ/','完成、结束；收尾、表面加工〔现在分词、动名词〕',
 '已经向终点推进，正把最后的部分做好，是 finishing。做完任务、跑到终点、给家具补上最后的表面处理，都在收尾。',
 'finish + -ing → finishing。finish 经古法语 finiss- 动词形式接拉丁 fīnīre 结束，较早 fīnis 边界、终点；这里 ish 来自法语词形，与 childish 的性质后缀不同。',
 [['拉丁 fīnis、fīnīre → 法语 finiss- → finish','终点、设限 → 做完、结束'],['finish + -ing → finishing','正在完成；把成品最后处理好的工序']],
 'finishing the report 完成报告；finishing touches 最后的修饰；finishing line 终点线〔常见英式〕。',
 'finishing work on the model 完成模型收尾；finishing a meal 吃完饭。','finish doing 表示把某事做完；finishing touches 是让东西更完整的最后几处细节。finish 的 -ish 不能按稍微、像某种性质来译。',
 ('She is finishing the last section of the report.','她正在完成报告的最后一部分。'),('The team is adding the finishing touches to the display.','团队正在给展陈补上最后的细节。'),sources=['https://en.wiktionary.org/wiki/finishing#English','https://www.etymonline.com/word/finish'])
W('protecting','/prəˈtektɪŋ/','保护、防护〔现在分词、动名词〕',
 '把一层能挡住伤害的东西放在前面，是 protecting 的保护画面。可以真用罩子挡，也可以用规则、行动照料容易受损的人或物。',
 'protect + -ing → protecting。拉丁 prō- 在前面 + tegere 盖住 → prōtegere，分词 prōtectus 的词干进入英语 protect；现代 ing 表过程。',
 [['拉丁 prōtegere、prōtectus → protect','在前盖住 → 使免受伤害'],['protect + -ing → protecting','正在保护；采取防护的过程']],
 'protecting the environment 保护环境；protecting the surface 保护表面；protecting people from harm 保护人免受伤害。',
 'protecting data 保护数据；protecting the wood from rain 保护木材免受雨淋。','protect something from/against something 说明保护对象和防范来源。protecting 不一定要求完全隔绝，重点是降低损害、保住对象。',
 ('The cover is protecting the wood from the rain.','罩子正保护木材免受雨淋。'),('The project focuses on protecting local wildlife.','项目重点保护当地野生动物。'),sources=['https://en.wiktionary.org/wiki/protecting#English','https://en.wiktionary.org/wiki/protect#English'])
W('coaching','英 /ˈkəʊtʃɪŋ/；美 /ˈkoʊtʃɪŋ/','辅导、训练；教练指导〔现在分词、动名词〕',
 '有人在旁边看你怎么做，指出需要调整的地方，帮助你向目标走，是 coaching。它可以是运动训练，也可以是考试、技能辅导。',
 'coach + -ing → coaching。coach 车辆词经法语、德语接匈牙利 Kocs 地名相关称呼；英语学生俚语把辅导人过考的教师比作载人前进的车，后来扩展到体育训练。',
 [['车辆 coach → 辅导者 coach、动词','载人前进的比喻 → 帮助学习者通过考试、比赛'],['coach + -ing → coaching','辅导、训练的过程']],
 'football coaching 足球训练指导；coaching for an exam 考试辅导；coaching a team 指导球队。',
 'individual coaching 个别辅导；coaching new staff 辅导新员工。','coaching 常有针对目标、观察表现并反馈的感觉；teaching 范围更广。车辆 coach 的历史仍在，但这类 coaching 句子通常是辅导。',
 ('She spends Saturday mornings coaching a youth team.','她周六上午指导一支青年队训练。'),('The course includes individual coaching on presentation skills.','课程包含演讲表达技巧的个别辅导。'),sources=['https://en.wiktionary.org/wiki/coaching#English','https://www.etymonline.com/word/coach'])
W('stopping','英 /ˈstɒpɪŋ/；美 /ˈstɑːpɪŋ/','停止、阻止；停靠〔现在分词、动名词〕',
 '原来还在继续的动作，现在被截住或自己停下，是 stopping。它也可以是途中停一站、暂歇一下。',
 'stop 双写 p + -ing → stopping，重读短元音后单辅音结尾影响拼写。stop 接古英语 stoppian、中古英语 stoppen 堵塞、封住，后发展出停止、使停止。',
 [['古英语 stoppian → stop','堵住 → 阻止继续、停下'],['stop 双写 p + -ing → stopping','正在停止；停靠、阻止的过程']],
 'stopping the machine 停下机器；stopping for lunch 停下来吃午饭；stopping at the station 在站上停靠。',
 'without stopping 不停地；stopping people from entering 阻止人进入。','stop somebody from doing 是阻止某人做。stopping to rest 是停下原动作去休息，stopping work 是停止工作，to 与 -ing 的关系分别看。',
 ('The bus is stopping outside the museum.','公交车正在博物馆外停靠。'),('We walked for an hour without stopping.','我们不停地走了一小时。'),sources=['https://en.wiktionary.org/wiki/stopping#English','https://en.wiktionary.org/wiki/stop#English'])
W('cents','/sents/','分〔货币小单位，复数〕',
 '把一种本位货币分成一百份，其中一份可以叫 cent。cents 是几份这样的零钱单位，远处的词根线索正是一百。',
 'cent + -s，/t/ 后读 /s/。cent 经法语 cent 一百接拉丁 centum，在多种货币中转指本位货币的百分之一；具体是哪种货币，要看语境。',
 [['拉丁 centum → 法语 cent → cent','一百 → 一百份中的一份货币单位'],['cent + -s → cents','几分、若干分的金额']],
 'fifty cents 五十分；a few cents 几分钱；dollars and cents 元与分。',
 'costs ten cents 价格十分；save a few cents 省下几分。','cents 是金额单位，具体属于美元、欧元或其他货币，需看前后说明；不同货币中同名单位不能直接当成相同价值。',
 ('The price rose by twenty cents.','价格涨了二十分。'),('She found a few cents in her coat pocket.','她在外套口袋里找到几分钱。'),sources=['https://en.wiktionary.org/wiki/cents#English','https://en.wiktionary.org/wiki/cent#English'])
W('diseases','/dɪˈziːzɪz/','疾病、各种病〔复数〕',
 '身体原来的正常状态受了某种疾病影响，谈不同种类时就说 diseases。这个词也可以用于动物、植物，不只谈人。',
 'disease + -s，底词末 /z/ 后增加 /ɪz/。disease 经法语 desaise 不安适借入，des- 缺少、离开 + aise 舒适，现代可认 dis- 与 ease 的对应；后来医学疾病义专门化。',
 [['法语 desaise → disease','失去安适 → 疾病的专门用途'],['disease + -s → diseases','不同病种或多种疾病']],
 'plant diseases 植物病害；infectious diseases 传染病；study diseases 研究疾病。',
 'diseases affecting trees 影响树木的病害；different diseases 不同疾病。','某一种病可说 a disease，多种病用 diseases；泛谈疾病现象也可用 disease。末尾是 /zɪz/，读音里保留底词的 /z/。',
 ('The researchers study diseases that affect fruit trees.','研究人员研究影响果树的病害。'),('The book explains how different diseases were understood in the past.','这本书介绍过去人们如何理解不同疾病。'),sources=['https://en.wiktionary.org/wiki/diseases#English','https://en.wiktionary.org/wiki/disease#English'])
W('apps','/æps/','应用程序〔复数〕',
 '为了完成某类具体任务而打开使用的程序，就是 apps。可以用它记笔记、看地图、编辑照片，核心是拿软件来做一件事。',
 'app + -s，/p/ 后读 /s/。app 是 application 的现代缩短；application 较早经法语、拉丁 applicātiō 接 applicāre 应用、附到，计算机应用义与缩短词后来发展。',
 [['application 应用 → 软件 application → app','应用到某种任务的程序 → 常用短称'],['app + -s → apps','多个应用程序']],
 'mobile apps 手机应用；note-taking apps 笔记应用；install apps 安装应用。',
 'apps for editing photos 照片编辑应用；apps on a computer 电脑应用程序。','apps 不限于手机，电脑上为具体任务使用的软件也能这样叫。application 还可以是申请、应用等普通名词，app 通常按计算机程序的语境理解。',
 ('She uses two apps to organise her notes.','她用两个应用程序整理笔记。'),('The tablet comes with several useful apps.','平板电脑预装了几个有用的应用。'),sources=['https://en.wiktionary.org/wiki/apps#English','https://en.wiktionary.org/wiki/app#English'])
W('shops','英 /ʃɒps/；美 /ʃɑːps/','商店、店铺〔复数〕；购物〔第三人称单数〕',
 '把商品摆在一个地方让人挑选、购买，就是 shops 的店铺画面；一个人去挑选、购买，则是动词 shops。',
 'shop + -s，/p/ 后读 /s/。shop 接中古英语 shoppe，与古英语及日耳曼棚舍相关材料相连，较远路线有不确定处；购物动词从商店名词发展。',
 [['中古英语及棚舍相关词 → shop','店铺、营业空间 → 购物动作'],['shop + -s → shops','多家商店；单数主语购买、挑选商品']],
 'local shops 当地商店；coffee shops 咖啡店；shops for vegetables 买菜。',
 'shops near the station 车站附近店铺；shops online 网上购物。','shops for something 作动词说明要买什么；shops 作名词则可接 selling... 说明卖什么。shop around 是比较不同商家的价格、条件。',
 ('The street has several small shops and cafés.','这条街有几家小店和咖啡馆。'),('She shops for vegetables at the local market.','她在当地市场买菜。'),sources=['https://en.wiktionary.org/wiki/shops#English','https://en.wiktionary.org/wiki/shop#English'])
W('websites','/ˈwebsaɪts/','网站〔复数〕',
 '在万维网上，把相关页面和功能放到一个可访问的站点里，就是 websites。一个学校、商店或项目可以有自己的网站。',
 'web 万维网 + site 站点 → website，再加 -s，/t/ 后读 /s/。两个旧词组成现代数字领域名词；web 的网状连接、site 的所在位置共同提供命名线索。',
 [['web + site → website','网络 + 站点 → 一组相关网页、功能所在处'],['website + -s → websites','多个网站']],
 'educational websites 教育网站；official websites 官方网站；visit websites 访问网站。',
 'websites for language learners 面向语言学习者的网站；links to websites 网站链接。','website 是整个站点，web page 常是其中一页；site 在网络语境也可直接简称网站。一个网站可以包含很多页面。',
 ('The teacher recommended several websites for reading practice.','老师推荐了几个练习阅读的网站。'),('The guide includes links to the museums’ websites.','指南包含博物馆网站的链接。'),sources=['https://en.wiktionary.org/wiki/websites#English','https://en.wiktionary.org/wiki/website#English'])
W('addresses','英 /əˈdresɪz/；美名词 /ˈædresɪz/ 或 /əˈdresɪz/，动词 /əˈdresɪz/','地址、致辞〔复数〕；处理、探讨；向……讲话〔第三人称单数〕',
 '把信件、话语或行动指向一个地方、一个对象，是 addresses 的共同线索。地址给投递方向，address a problem 则把注意和处理动作朝向问题。',
 'address + -es，/s/ 后增加 /ɪz/。经古法语 adrecier 指向、使直，接重构通俗拉丁 *addirectiare，ad- 向 + *directiare 使直，较早 directus 直的；英语先有动词，名词后发展。',
 [['通俗拉丁重构形式 → 法语 → address','指向、使直 → 投递目的地；对人讲话、处理事情'],['address + -es → addresses','多个地址、致辞；单数主语处理或讲话']],
 'email addresses 电子邮件地址；addresses the audience 向听众讲话；addresses the problem 处理问题。',
 'home addresses 家庭住址；addresses two questions 探讨两个问题。','address a problem 表示正面处理、讨论这个问题，不保证它已完全解决。名词 address 在美式英语中常可前重音，动词通常后重音。',
 ('The form asks for the addresses of all participants.','表格要求填写所有参加者的地址。'),('The report addresses two important questions.','报告探讨两个重要问题。'),sources=['https://en.wiktionary.org/wiki/addresses#English','https://www.etymonline.com/word/address'])
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_zt',ROOTS,WORDS)
 extend_lessons()
