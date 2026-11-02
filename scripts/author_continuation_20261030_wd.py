"""High-frequency reading forms: books, questions and studies."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'B2414':dict(words=['book','books'],label='book → books：书、账簿与预订',note='books 既可作书的复数，也可作预订的动词形式；账簿义保留书面记录的历史联系。'),
 'C1189':dict(words=['question','questions'],label='question → questions：问题与质疑',note='question 经法语及拉丁 quaestio 词族传入；questions 说问题，也可说单数主语询问、质疑。'),
 'B3190':dict(words=['group','groups'],label='group → groups：成组的整体；把东西归类',note='group 经法语接意大利语 gruppo／groppo 结、团块；groups 可作复数，也可作分组的动词。'),
 'A1776':dict(words=['area','areas'],label='area → areas：区域、面积与领域',note='area 来自拉丁空地、平地名称；areas 是现代复数，词尾读 /z/。'),
 'C1614':dict(words=['event','events'],label='event → events：发生的事与安排的活动',note='event 接拉丁 evenire 出来、发生的 eventus 形式；events 可以是意外发生的事，也可以是筹办的活动。'),
 'C0172':dict(words=['case','cases'],label='case → cases：情况、实例、案件',note='case 的情况、案件线接拉丁 casus 发生的事，与 cadere 落下、发生相关；容器义另源。'),
 'C0168':dict(words=['case','cases'],label='case → cases：盒、箱的复数另看容器来源',note='容器 case 经法语接拉丁 capsa 盒，不与情况义 casus 合并；cases 两义在英语中同形。'),
 'C0351':dict(words=['product','products'],label='product → products：产物、产品和乘积',note='product 接拉丁 producere 带出、产生的分词；products 是现代复数，数学语境另看乘法。'),
 'C1060':dict(words=['place','places'],label='place → places：地点、位置；放置',note='place 经法语、拉丁接希腊宽阔道路一系；places 可作多个位置，也可作单数主语放置。'),
 'C1057':dict(words=['plan','plans'],label='plan → plans：图纸、安排；打算',note='plan 从平面图扩展到行动安排，plans 可作名词复数或单数主语的计划动作。'),
 'C1440':dict(words=['study','studies'],label='study → studies：学习、研究与研究成果',note='study 名词、动词经法语分别接拉丁 studium、studere；studies 两种词性都把末尾 y 变 ies。'),
}
W('books','/bʊks/','书籍；账簿、账目；预订〔book 的第三人称单数〕',
 '一本本装着文字的书是 books；账目原来常记在簿子里，books 又能说账簿。把名字登记进去，book 作动词便能说预订。',
 'book + -s，/k/ 后读 /s/。book 接古英语 boc 书、文书，动词登记、预订与书面记录的发展相连。',
 [['古英语 boc → book','书、文书；书面记录'],['book 名词、动词 + -s → books','多本书、账簿；单数主语预订']],
 'read books 读书；keep the books 记账；balance the books 使收支账目平衡；on the books 在册、列入记录；books a room 预订房间。',
 'a stack of books；books a table。','The books are here 中 books 是复数名词；She books the tickets 中是动词。book 作预订时可以接房间、票、座位等对象，并不限于书。',
 ('The books on the top shelf belong to my sister.','最上层架子上的书是我姐姐的。'),('He books the same room whenever he visits the city.','每次来这座城市，他都预订同一个房间。'),sources=['https://en.wiktionary.org/wiki/books#English','https://en.wiktionary.org/wiki/book#English'])
W('questions','/ˈkwestʃənz/','问题、疑问；询问、质疑〔question 的第三人称单数〕',
 '有不清楚的地方，把它提出来，是 questions；作动词时也可以把原本被接受的说法拿出来重新问：真的如此吗？',
 'question + -s，词尾 /z/。question 经法语及直接拉丁借入接 quaestio 询问、探究，属于 quaerere 寻求、询问词族；不把全词历史缩成英语 quest 临时加 -ion。',
 [['拉丁 quaerere／quaestio → 法语及英语 question','寻求、探究 → 问题、询问'],['question + -s → questions','多个疑问；单数主语询问、质疑']],
 'ask questions 提问；answer questions 回答问题；questions about ... 关于……的问题；questions the decision 质疑决定；raises questions 引发疑问。',
 'a list of questions；questions the need for ...。','a question 常需要回答，a problem 常需要解决。question the result 不只是问比分是多少，也可能是在质疑结果是否可靠。',
 ('Please write down any questions you want to ask.','请把你想问的问题记下来。'),('The article questions whether the change is necessary.','文章质疑这项改变是否有必要。'),sources=['https://en.wiktionary.org/wiki/questions#English','https://en.wiktionary.org/wiki/question#English'])
W('groups','/ɡruːps/','组、群、团体〔复数〕；把……分组、归类〔group 的第三人称单数〕',
 '原本分散的人或物凑成几团，就是 groups。作动词时，是按某种规则把这些东西放到同一组。',
 'group + -s，/p/ 后读 /s/。group 借法语 groupe，上接意大利语 gruppo、groppo 结、团块等形式，更深来源有讨论。',
 [['意大利 gruppo／groppo → 法语 groupe → group','结、团块 → 聚在一起的群体'],['group 名词、动词 + -s → groups','多组、多群；单数主语分组']],
 'in groups 分组、成群；age groups 年龄组；small groups 小组；groups items by size 按大小把物品归类。',
 'groups of four；groups the files by date。','in groups of four 是每组四人或四个；four groups 是一共四组。先看数字在 groups 前还是在 of 后，才能读清组数和每组数量。',
 ('The students worked in groups of four.','学生们四人一组做任务。'),('The app groups the photos by date.','这个应用按日期把照片分组。'),sources=['https://en.wiktionary.org/wiki/groups#English','https://en.wiktionary.org/wiki/group#English'])
W('areas','英 /ˈeəriəz/；美 /ˈeriəz/','区域、地区；领域；面积〔复数〕',
 '在地图、地面或话题里圈出几块范围，都是 areas。说它们有多大时，则是在比较面积。',
 'area + -s，词尾 /z/。area 借拉丁 area 平地、空场等名称，后来扩展为区域、表面量和抽象领域；不是英语 air 再接后缀。',
 [['拉丁 area → 英语 area','平地、空场 → 区域、面积、领域'],['area + -s → areas','多个区域、领域或面积值']],
 'rural areas 乡村地区；residential areas 居住区；areas of interest 感兴趣的领域；areas for improvement 可改进的方面。',
 'different areas；the areas of two shapes。','compare the areas of two rooms 是比较两间房的面积；compare two areas of the city 是比较城里的两个区域。复数形式相同，要看被比较的是范围还是大小。',
 ('The map marks the areas where cycling is allowed.','地图标出了允许骑车的区域。'),('The feedback identified three areas for improvement.','反馈指出了三个可以改进的方面。'),sources=['https://en.wiktionary.org/wiki/areas#English','https://en.wiktionary.org/wiki/area#English'])
W('events','/ɪˈvents/','事件；活动；比赛项目；event 的复数',
 '发生的一件件事是 events，专门安排给人参加的活动也叫 events。它既能说意外，也能说有计划的聚会、赛事。',
 'event + -s，/t/ 后读 /s/。经法语 event 接拉丁 eventus，源于 e-／ex- 出来 + venire 来形成的 evenire 发生；不是 even 偶数的加 t。',
 [['拉丁 evenire → eventus → 法语、英语 event','出来、发生 → 发生的事'],['event + -s → events','多件事件、活动或竞赛项目']],
 'recent events 近期事件；a series of events 一连串事件；social events 社交活动；sporting events 体育赛事；field events 田赛项目。',
 'upcoming events；the order of events。','events 可以是筹办的活动，也可以是没有人筹办的事件；activities 更常强调人在做什么。a running event 是一个比赛项目，不自动等于一次大事故。',
 ('The museum lists next month’s events on its website.','博物馆在网站上列出了下个月的活动。'),('She described the events in the order they happened.','她按发生的先后顺序讲述了这些事。'),sources=['https://en.wiktionary.org/wiki/events#English','https://en.wiktionary.org/wiki/event#English'])
W('cases','/ˈkeɪsɪz/','情况、实例、案件、病例、语法格；盒、箱；case 的复数等',
 '这个拼写住着两大家：一边是发生的情况和拿来处理的实例，另一边是装东西的盒、箱。先分这两路，再看句子属于哪个场景。',
 'case + -s；/s/ 后加 /ɪz/。情况、案件一支经法语 cas 接拉丁 casus 发生的事；容器一支经法语接拉丁 capsa 盒，不能把两个祖先合成一个。',
 [['拉丁 casus → 法语 cas → case','发生的事 → 情况、案件、实例等'],['另路拉丁 capsa → 法语相关形式 → case；两路各加 -s → cases','盒、箱；英语两词族的复数同形']],
 'in most cases 在大多数情况下；similar cases 类似实例；court cases 诉讼案件；cases of illness 疾病病例；camera cases 相机套；grammatical cases 语法中的格。',
 'in some cases；cases containing tools。','in these cases 常是在这些情况下；these cases on the shelf 则可指架子上的这些箱子。复数都是 cases，词源和含义仍要分开。',
 ('In most cases, you can solve the problem by restarting the device.','大多数情况下，重启设备就能解决问题。'),('The instruments travel in strong wooden cases.','这些仪器装在结实的木箱里运输。'),sources=['https://en.wiktionary.org/wiki/cases#English','https://en.wiktionary.org/wiki/case#English'])
W('products','/ˈprɒdʌkts/〔英〕；/ˈprɑːdʌkts/〔美〕','产品、产物；乘积；product 的复数',
 '经过某个过程，最后产出了什么，就是 products。工厂产出商品，化学反应生成物质，乘法运算得到乘积。',
 'product + -s，/t/ 后读 /s/。拉丁 producere 带出、产生的分词 productus 提供历史材料；product 不是把英语 produce 任意截短再拼一个 t。',
 [['拉丁 pro- + ducere → producere／productus → product','带出来、产生 → 产出的东西'],['product + -s → products','多个产品、产物或乘积']],
 'dairy products 乳制品；household products 家用品；finished products 成品；reaction products 反应产物；products of two numbers 两个数的乘积等数学表达。',
 'new products；products made locally。','produce 作农产品集合名词时通常不可数，products 可数，指一件件或一类类产品。product 在数学里是乘积，sum 才是加法所得的和。',
 ('The shop sells products made by local artists.','这家店出售当地艺术家制作的产品。'),('The students compared the products of several pairs of numbers.','学生们比较了几组数相乘得到的乘积。'),sources=['https://en.wiktionary.org/wiki/products#English','https://en.wiktionary.org/wiki/product#English'])
W('places','/ˈpleɪsɪz/','地方、位置、名额、名次；放置、把……列入〔place 的第三人称单数〕',
 '现实里能站、能坐的一处位置，名单里留给某人的位置，比赛里排到的位置，都可以叫 places。作动词时，是把东西放到某处。',
 'place + -s，/s/ 后加 /ɪz/。经法语 place 接拉丁 platea，远源是希腊宽阔道路的名称；英语常用词的主要借入路线经过法语。',
 [['希腊宽阔道路词 → 拉丁 platea → 法语 place → 英语 place','街道、场所 → 地点、位置'],['place 名词、动词 + -s → places','多个位置、名额；单数主语放置']],
 'public places 公共场所；places to visit 值得去的地方；change places 交换位置；decimal places 小数位；places the cup on the table 把杯子放桌上。',
 'two empty places；places an order。','places in a course 可说课程名额，places in a race 可说比赛名次。She places an order 中是下订单的动词结构，不能把 places 当复数地点。',
 ('There are only two places left on the course.','这门课只剩两个名额了。'),('She always places the keys in the same bowl.','她总把钥匙放在同一个碗里。'),sources=['https://en.wiktionary.org/wiki/places#English','https://en.wiktionary.org/wiki/place#English'])
W('plans','/plænz/','计划、打算；平面图、设计图；计划、打算〔plan 的第三人称单数〕',
 '先把要做的事画出来或安排出来，就是 plans：房子的图纸是一种，周末怎么过的安排也是一种。',
 'plan + -s，/n/ 后读 /z/。plan 借法语 plan 平面图，接拉丁 planum 平面；英语由图示扩展到行动方案，动词由名词发展。',
 [['拉丁 planum → 法语 plan → 英语 plan','平面 → 平面图、设计安排 → 行动计划'],['plan 名词、动词 + -s → plans','多个安排、图纸；单数主语打算']],
 'travel plans 出行计划；building plans 建筑图纸；make plans 制定计划；plans to leave 打算离开；plans for the weekend 周末安排。',
 'change our plans；plans to study abroad。','She has plans 是她有安排，She plans to go 是她打算去。plans to do 的 to 接动词；plans for the trip 的 for 接名词，结构不同。',
 ('Have you made any plans for the weekend?','你周末有什么安排吗？'),('The architect showed us the plans for the new kitchen.','建筑师给我们看了新厨房的设计图。'),sources=['https://en.wiktionary.org/wiki/plans#English','https://en.wiktionary.org/wiki/plan#English'])
W('studies','/ˈstʌdiz/','学习、课业；研究〔复数〕；学习、研究〔study 的第三人称单数〕',
 '把注意力持续放进一个问题里，是 study。studies 可说一个人的学习，也能数不同研究；单数主语后又可以是他在学、在研究。',
 'study 的 y 前是辅音字母 d，加复数或第三人称 -s 时变为 -ies；读 /iz/，不是另外加 /ɪz/ 后缀。名词、动词经相关法语形式分别接拉丁 studium、studere。',
 [['拉丁 studium／studere → 法语相关形式 → study','专注、用心投入 → 学习、研究'],['study 变 y 为 i + -es → studies','多项研究、课业；单数主语学习、研究']],
 'continue your studies 继续学业；research studies 研究；case studies 案例研究；studies music 学习音乐；studies the map 仔细查看地图。',
 'recent studies；studies at a local college。','Recent studies show ... 中 studies 是复数研究；She studies ... 中是动词。study 不只说上课，也能说认真看、仔细研究某个具体东西。',
 ('Several studies reached similar conclusions.','几项研究得出了相似的结论。'),('He studies the map before choosing a route.','他选路线前会仔细看地图。'),sources=['https://en.wiktionary.org/wiki/studies#English','https://en.wiktionary.org/wiki/study#English'])
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_wd',ROOTS,WORDS)
 extend_lessons()
