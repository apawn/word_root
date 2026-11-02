"""Wed, tree, app, feed: compact everyday families with shared expansions."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
WD=[['古英语 weddian → 中古英语 wedden → wed','作出承诺、订婚、结婚'],['英语 wed','结婚；把事物结合起来〔比喻〕']]
def WH(f,m):return WD+[[f,m]]
W('wed','/wed/','结婚；使结合〔较正式〕',
 '词的旧背景是作承诺，后来集中到婚姻承诺。今天新闻标题常用简短的 wed 表示结婚。',
 '接古英语 weddian，原有立约、作保证、订婚等义，后来专门化为结婚。现代 wed 是完整词，不把它拆成 w 与 ed。',WD,
 'wed someone 与某人结婚，be wedded to an idea 死守、深信某个想法；后者用紧密结合的比喻。过去式、分词可见 wed、wedded。',
 'wed in June；wed someone；be wedded to an idea。',
 'wed 比 get married 常显书面、新闻标题风格；be wedded to a method 可说认定某种方法，不表示与方法举行婚礼。',
 ('The couple plan to wed in June.','这对伴侣打算六月结婚。'),('He is not wedded to any particular method.','他没有认定非用某一种方法不可。'))
W('wedding','/ˈwedɪŋ/','婚礼；结婚仪式',
 '结婚这件事办成的一场仪式：邀请宾客、交换誓言、庆祝。重点是那次活动。',
 '古英语 weddung 是 weddian 的动作名词，经中古英语 wedding 延续。现代对应 wed + -ing，双写 d；常见婚礼义由结婚、订婚活动发展。',WD[:1]+[['古英语 weddung → 中古英语 wedding → wedding','结婚、订婚活动 → 婚礼；现代对应 wed + -ing']],
 'a wedding ceremony 婚礼仪式，a wedding dress 婚纱，a wedding reception 婚宴、婚礼后的招待会。',
 'a wedding dress；a wedding ceremony；attend a wedding。',
 'wedding 那场婚礼，marriage 婚姻关系；a happy marriage 说长期关系，a beautiful wedding 常说仪式办得美。',
 ('We attended her wedding last Saturday.','上周六我们参加了她的婚礼。'),('They want a small wedding with close friends.','他们想办一场只请好友的小婚礼。'))
W('newlywed','英 /ˈnjuːliwed/；美 /ˈnuːliwed/','新婚者；新婚的',
 '刚刚结婚、仍处在新婚阶段的人。常用复数 the newlyweds 指那对新人。',
 'newly 刚刚、新近 + wed 已结婚的，合成名词或形容词。newly 是方式、时间副词，不拆成新加一根无义字母链。',WH('newly + wed → newlywed','刚结婚的人；新婚的'),
 'the newlyweds 那对新人，a newlywed couple 新婚夫妇、新婚伴侣；没有固定由词本身规定的新婚天数。',
 'the newlyweds；a newlywed couple；congratulate the newlyweds。',
 'newlywed 刚结婚的人，newcomer 新来者；新人中文能指不同身份，英文要按情境选。',
 ('The newlyweds thanked everyone for coming.','那对新人感谢大家到场。'),('A newlywed couple moved into the flat next door.','一对新婚伴侣搬进了隔壁公寓。'))
W('unwed','/ˌʌnˈwed/','未婚的〔较正式〕',
 '婚姻状态上没有结婚。un- 否定已婚状态，不是在说举行过婚礼又把仪式撤销。',
 'un- 不 + wed 已婚的，常用形容词。虽有较少用的逆向动词等历史用法，日常阅读先掌握未婚义。',WH('un- + wed → unwed','没有结婚的'),
 'unwed parents 未婚父母，an unwed couple 未婚伴侣。常见于较正式文本；日常描述也常用 unmarried。',
 'unwed parents；an unwed couple；remain unwed。',
 'unwed 未婚，不自动表示 divorced 离异或 widowed 丧偶；也不等于 single 在所有社交语境的无伴侣。',
 ('The article discusses the experiences of unwed parents.','文章讨论未婚父母的经历。'),('The two remained unwed for many years.','两人多年一直没有结婚。'))
R('B3009','承诺背景发展为结婚；婚礼和婚姻状态','WED：以承诺结合，专门化为结婚','wed → wedding；newlywed、unwed 放相邻作状态对照。',
 '古英语承诺背景有据，现代不靠词形编出婚姻买卖故事。重心是实际常用的婚礼、结婚和状态表达。',
 'wed—wed/wedded；wed + -ing，双写 d；newly/un- + wed。',
 [['动作与仪式','wed · wedding'],['新婚和未婚状态','newlywed · unwed']],
 'wedding 仪式、marriage 关系；newlywed 新婚者、newcomer 新来者；unwed 不自动等于无伴侣。',
 'The newlyweds shared photographs from their wedding.\n\n那对新人分享了婚礼照片。','wed wedding newlywed unwed')
TR=[['古英语 trēow、trēo → 中古英语 tre → tree','树；木材、木梁等'],['英语 tree','树木；以分枝结构比喻家谱、分类和数据关系']]
W('tree','/triː/','树；树形结构；〔动词〕把动物赶上树',
 '一根主干向上，分成大枝、小枝；家谱、分类图、文件目录借它的分支结构叫 tree。',
 '本族词，接古英语 trēow、trēo 等。旧义也包括木料和木制结构；现代树形图抓的是分支关系，不必每个分支都真长叶子。',TR,
 'a family tree 家谱，a tree diagram 树形图，plant a tree 种树；The dog treed the cat 表狗把猫追到树上。',
 'plant a tree；a family tree；a tree diagram；a directory tree。',
 'tree 树，wood 可木材、林地；tree 动词赶上树属于名词转动作，不是 tree 的过去式。',
 ('We planted a tree near the gate.','我们在门边种了一棵树。'),('The diagram shows the family tree.','这张图展示了家谱。'))
W('treeless','/ˈtriːləs/','没有树的',
 '放眼看去看不到树，可能是草原、山地或其他景观。它只否定树，不否定一切植物。',
 'tree + -less，没有树木。保留 tree 的完整词形。',TR+[['tree + -less → treeless','没有树木的']],
 'a treeless plain 无树平原，treeless hills 没有树的丘陵，a treeless landscape 无树景观。',
 'a treeless plain；treeless hills；a treeless landscape。',
 'treeless 没树，barren 贫瘠、少植被或不结果等；一大片青草地可以 treeless，却不必 barren。',
 ('We crossed a wide treeless plain.','我们穿过一片辽阔的无树平原。'),('Grass covered the treeless hills.','没有树的丘陵上长满了草。'))
R('B2615','树木、木制结构；分枝关系','TREE：从主干伸出枝条，也借来画关系','tree → treeless；treehouse、treetop、doubletree 等按部位、场所、木制器具相邻。',
 'gantry 的旧拼写和来源有不同分析，本轮不把它硬画成确定的 tree 直接派生。原有 doubletree 木制横杆用法复用旧精讲。',
 'tree + -less；tree + house/top；double + tree 的 tree 有旧木制杆架义。',
 [['树与没有树','tree · treeless'],['部位、场所和木杆器具','treetop · treehouse · doubletree']],
 'treeless 不等于无植物；family tree 借分支关系；tree 木材旧义解释部分器具名，不把它都译成活树。',
 'We could see the treetop from the treehouse.\n\n我们从树屋里能看见树梢。','tree treeless treetop treehouse doubletree')
ROOTS[-1]['exclude']['gantry']='旧形 gauntree 及更早来源有不同分析；本轮暂略，不把 tree 的参与方式断言为确定事实。'
AP=[['application program 等 → application','为具体任务服务的应用程序'],['application 缩短 → app','应用程序，常用于手机、电脑软件']]
W('app','/æp/','应用程序、App',
 '手机里点一下就能记账、导航、聊天的那一个程序。app 是长词 application 剪短后的常用叫法。',
 'application 的截短，不是三个字母各代表一个词的首字母缩写。这里研究软件义；菜单、体育统计里的同形缩略可另有来源。',AP,
 'download an app 下载应用，a messaging app 聊天应用，an app developer 应用开发者。首音是元音，单数说 an app。',
 'download an app；open the app；a mobile app；an app developer。',
 'app 应用，application 还可申请、应用、涂敷等；不能把 application form 申请表理解为手机软件表格。',
 ('I use an app to track my spending.','我用一个应用记录开销。'),('Open the app and choose a language.','打开应用，然后选择一种语言。'))
W('applet','/ˈæplət/','小应用程序；嵌在较大环境中执行的小程序',
 '不是完整的大套软件，而是负责一小件事的程序单元；常在某个宿主环境中运行。',
 'app〔application 缩短〕+ 小称后缀 -let。名称的具体早期背景还有其他影响说法，但基本构词可以这样理解；不拆成 apple 苹果加 t。',AP+[['app + -let → applet','小型应用程序；依附特定环境运行的程序单元']],
 'a Java applet 常见于旧技术文献，a small applet 小程序。这个英语词泛指的类别不必等同某个平台特定产品名里的小程序。',
 'a Java applet；run an applet；a small applet。',
 'app 常泛称应用，applet 突出小型、宿主环境等背景；不是所有体积小的手机 app 都惯常叫 applet。',
 ('The old manual describes a Java applet for drawing graphs.','旧手册介绍了一个绘图用的 Java 小程序。'),('The applet performs a single calculation.','这个小程序完成一项计算。'),
 sources=['https://en.wiktionary.org/wiki/applet#English','https://www.etymonline.com/word/applet'])
R('B4498','application 的截短；小型应用程序','APP：把 application 程序义缩短成口语常用名','app → applet，只保留常用基础软件称呼。',
 '这组要学截短和小称后缀，而不是把字母都当古典词根。Java applet 的历史例子只用于认识词义。',
 'application → app〔截短〕；app + -let → applet。',
 [['应用与小型程序','app · applet']],
 'app 不是逐字母首字母缩写；applet 不等于 apple+t；英语泛称不等于某一平台专有产品。',
 'The app contains a small applet for converting units.\n\n这个应用内含一个换算单位的小程序。','app applet')
F=[['古英语 fēdan → 中古英语 feden → feed','喂养、供给食物；与 food 同族'],['英语 feed','喂养；供应材料、数据、信息等；饲料、信息流']]
def FH(f,m):return F+[[f,m]]
W('feed','/fiːd/','喂养、进食；供应、输入；饲料；信息流',
 '把食物不断送进嘴里，再把这个供给画面借给机器、数据和手机更新。feed 不一定有真正的嘴。',
 '动词接古英语 fēdan，与 food 有旧同族联系；不是现代英语随意把 food 两个 o 改成 e。名词有饲料、供料等发展，信息流接持续提供内容的比喻。',F,
 'feed the cat 喂猫，feed data into a system 把数据输入系统，a live feed 实时传输，a news feed 信息流。过去式、分词 fed。',
 'feed the birds；feed on；feed data into；a live feed。',
 'feed 给食物、供给，eat 自己吃；feed on 可动物以……为食，也可比喻靠某事滋长。a social media feed 不是给手机吃的饲料。',
 ('Please feed the cat while I am away.','我不在时，请帮忙喂猫。'),('The camera sends a live feed to the control room.','摄像机把实时画面传送到控制室。'))
W('feeder','英 /ˈfiːdə/；美 /ˈfiːdər/','喂食器、供料器；进食者；支线的〔修饰语〕',
 '给鸟不断供谷粒的装置，是 feeder；把人、货或水流送到主干线的支线，也借供应关系来理解。',
 'feed + -er，旧英语阶段后的派生已有中古英语形式。可表人物、动物、器具；修饰语里的 feeder 说为较大系统供给。',FH('feed + -er → feeder','进食、喂养者；供给器；向主系统输送的'),
 'a bird feeder 鸟食器，a paper feeder 送纸器，a feeder road 支路，a bottom feeder 底部觅食动物等。',
 'a bird feeder；a paper feeder；a feeder road。',
 'feeder 不只指喂食的人；feeder road 为主路送入车流，不是路边有餐馆的路。',
 ('We hung a bird feeder outside the window.','我们在窗外挂了一个鸟食器。'),('A feeder road connects the village to the highway.','一条支路把村子连接到公路干线。'))
W('breastfeed','/ˈbrestfiːd/','用母乳喂养；吃母乳',
 '让婴儿从乳房获得乳汁，或泛说母乳喂养这种方式。按句子可以说喂养的人，也可以说吃奶的婴儿。',
 'breast 乳房 + feed 喂养、进食，合成动词。过去式、分词 breastfed，沿用 feed—fed 的词形变化。',FH('breast + feed → breastfeed','以母乳喂养；吃母乳'),
 'breastfeed a baby 给宝宝喂母乳，a breastfed baby 母乳喂养的宝宝。这里只解释语言，不推导个人喂养选择。',
 'breastfeed a baby；be breastfed；breastfeeding。',
 'breastfeed 母乳喂养，bottle-feed 用奶瓶喂；奶瓶中也可能是挤出的母乳，二者谈的维度有差别。',
 ('She found a quiet place to breastfeed her baby.','她找了个安静的地方给宝宝喂母乳。'),('The baby was breastfed for several months.','这个宝宝吃了几个月母乳。'))
R('B2856','喂养；向系统持续供给食物、材料或信息','FEED：让所需东西不断送进去','feed → feeder、breastfeed；feedback 回传、feedstock 原料、newsfeed 信息、feedlot 饲养场按供给对象分组。',
 '食物与信息的供给用实际场景接起来。feed 与 food 的旧同族不是现代字母替换规则；共享词沿用已有完整精讲。',
 'feed—fed—fed；feed + -er；breast + feed；feed + back/stock/lot；news + feed。',
 [['供给、器具与喂养','feed · feeder · breastfeed'],['反馈、内容和材料','feedback · newsfeed · feedstock'],['饲养场所','feedlot']],
 'feed 喂、eat 吃；feeder 不只人物；breastfeed 与用奶瓶描述维度不同；newsfeed 是信息供给。',
 'The feeder supplies material to the machine at a steady rate.\n\n供料器以稳定速度给机器供应材料。','feed feeder breastfeed feedback newsfeed feedstock feedlot')
if __name__=='__main__':save('continuation_20261030_bz',ROOTS,WORDS)
