"""Plainness, spam, doping, predictions, wrecks and zips."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
U=[['sophisticate → sophisticated','从使不再单纯，到精密复杂、老练的'],['un- + sophisticated → unsophisticated','不精密复杂；不老练；也可说质朴简单']]
W('unsophisticated','/ˌʌnsəˈfɪstɪkeɪtɪd/','简单的、不精密的；不老练的；质朴的',
 '没有那么多复杂技巧和精细加工，便是 unsophisticated。说装置可能只是简单，说人可能是不老练；谈食物、生活也能欣赏那份质朴。',
 'un- 否定 + sophisticated 精密复杂、老练的。前缀否定其相应性质，具体褒贬随对象变化。',U,
 'unsophisticated equipment 简单设备，an unsophisticated audience 鉴赏经验较少的观众，simple, unsophisticated food 朴实的食物。',
 'unsophisticated equipment；unsophisticated tastes。',
 'unsophisticated 不必翻成愚蠢；缺少某种复杂性、经验与缺少智力不是一回事。',
 ('The device is unsophisticated but easy to repair.','这个装置很简单，不过容易修。'),('They enjoyed the restaurant’s fresh, unsophisticated food.','他们喜欢餐馆里新鲜朴实的食物。'))
R('B4560','精密老练与简单质朴，否定前缀按对象理解','SOPHISTICATED：细节和技巧发展得多，un- 则把这层性质撤去','sophisticated → unsophisticated。',
 '技术可以复杂精密，人可以见识老练；反过来的简单、不老练，有时是限制，有时也是质朴、容易使用。',
 'sophisticate → sophisticated；un- + sophisticated → unsophisticated。',
 [['精密老练及相反性质','sophisticated · unsophisticated']],
 'unsophisticated 的褒贬看对象，不能统一理解成笨。',
 'Sophisticated machinery may need an unsophisticated backup that is easy to repair.\n\n精密机器也可能需要一个容易维修的简单备用装置。','sophisticated unsophisticated')
Sp=[['SPAM 罐装肉品牌名','品牌名称的确切含义未公开确定，spiced ham 等是常见解释'],['喜剧中反复喊 SPAM → 网络反复塞入内容的比喻','spam 垃圾信息、刷屏；再生 spammer、spammy']]
W('spam','/spæm/','垃圾信息、垃圾邮件；刷屏、滥发消息；罐装午餐肉品牌相关称呼',
 '你没要求，对方却把同样内容一遍遍塞进来，就是 spam 的网络画面。它从罐装肉品牌，经过喜剧里反复唱喊同一词的场景，变成信息泛滥的比喻。',
 '原为 SPAM 品牌名，确切命名含义未公开确定；spiced ham 的拆法只是常见说法。网络义联系 Monty Python 喜剧中不断重复品牌名的桥段。',Sp,
 'a spam filter 垃圾信息过滤器，the spam folder 垃圾邮件文件夹，spam a chat 在聊天里刷屏；名词垃圾邮件通常不可数。',
 'a spam filter；spam messages；stop spamming。',
 'spam 不限电子邮件，也包括评论、即时消息等；收到的普通广告是否构成 spam，要看未经请求、大量或重复等语境。',
 ('The filter moved the message to the spam folder.','过滤器把消息移进了垃圾邮件文件夹。'),('Please stop spamming the chat with the same link.','请别再在聊天里反复刷同一个链接。'),sources=['https://en.wiktionary.org/wiki/spam#English','https://www.spam.com/faq','https://www.etymonline.com/word/Spam'])
W('spammer','英 /ˈspæmə/；美 /ˈspæmər/','垃圾信息发送者、刷屏者',
 'spam 是滥发内容，spammer 就是做这件事的人或账号。-er 从动作推出执行者，未必是对方真实姓名。',
 'spam + -er，双写 m。这里接网络滥发义，不接肉制品名。',Sp[:1]+[['spam 滥发信息 + -er → spammer','发送垃圾信息、反复刷屏者']],
 'block a spammer 屏蔽垃圾信息发送者，identify spammers 识别刷屏者。',
 'block a spammer；a persistent spammer。',
 'spammer 描述发送行为、账号角色；bot 强调自动程序，两者能重叠，但不能互相完全代替。',
 ('The moderator blocked the spammer.','管理员屏蔽了那个刷屏者。'),('Several spammers posted identical comments below the article.','几名垃圾信息发送者在文章下发了相同评论。'))
W('spammy','/ˈspæmi/','像垃圾信息的；广告过多、充斥刷屏内容的',
 '一个页面满眼弹窗、重复推销，读着像被广告围住，可以说 spammy。它评价的是带有垃圾信息那种烦扰特征。',
 'spam + -y，双写 m；由垃圾信息名词形成带该特征的口语形容词，也有较少见的肉制品相关用法。',Sp[:1]+[['spam 垃圾信息 + -y → spammy','像垃圾信息、广告重复过多的']],
 'spammy emails 像垃圾信息的邮件，a spammy website 充斥垃圾推广的网站。',
 'spammy comments；a spammy message。',
 'spammy 常是印象或评价，不能单凭这个形容词断定内容全部虚假；真正有用的内容也可能被反复推广得很烦。',
 ('The repeated sales links made the message look spammy.','反复出现的推销链接让消息看起来像垃圾信息。'),('She left the site because it felt too spammy.','她觉得网站垃圾推广太多，就离开了。'))
R('B3374','反复塞进来的内容，连接刷屏行为与执行者','SPAM：你没想看，它却一遍遍占住位置','spam → spammer、spammy。',
 '品牌名经过喜剧中的重复唱喊，进入网络信息泛滥的比喻。-er 指发送者，-y 形容带着这种令人烦扰的特征。',
 'SPAM 品牌 → 喜剧重复场景 → spam 网络义；双写 m + -er、-y。',
 [['内容、行为、人物及性质','spam · spammer · spammy']],
 '品牌名的拆法未定；网络 spam 不只电子邮件。',
 'The spammer filled the page with spammy links, most of which the spam filter removed.\n\n刷屏者把页面塞满垃圾推广式链接，大部分被过滤器清除了。','spam spammer spammy')
Do=[['荷兰 doop 蘸酱、浓稠液体 → 英语 dope','浓稠配制物、涂料等'],['后续分支','药物及使用；掺入材料；傻人、内幕消息等词义各有发展，具体桥梁有讨论']]
W('dope','英 /dəʊp/；美 /doʊp/','黏稠配制物、涂料；毒品；给……用药、掺杂；傻瓜；〔俚语〕很棒的',
 '最早先想一份浓稠的配制物，像蘸酱、涂料。后来分成药物、材料处理等用途；俚语又有傻瓜、内幕消息和很酷的意思，必须看句子。',
 '借自荷兰 doop 蘸酱，与 dopen 蘸相关。由浓稠物、配制物发展药物及处理用料；傻人义的具体语义桥梁不定，不编成一条已证实的药物故事。',Do,
 'get the dope on something 得到某事内幕，dope a material 给材料掺杂，That’s dope. 俚语很酷；a dope 骂人傻瓜，语气不客气。',
 'the dope on；dope a material；That’s dope.。',
 'dope 很棒的属于口语俚语；a dope 却可能是贬义人物名。dopamine 多巴胺的名称另有构成，不由这个词直接派生。',
 ('“That new track is dope,” he said.','他说：“那首新歌真酷。”'),('The conservator described the dope once used on the aircraft’s fabric covering.','修复师介绍了这种飞机蒙布上过去使用的涂料。'),sources=['https://en.wiktionary.org/wiki/dope#English','https://www.etymonline.com/word/dope'])
W('doping','英 /ˈdəʊpɪŋ/；美 /ˈdoʊpɪŋ/','〔体育〕使用兴奋剂；〔材料〕掺杂；涂布处理',
 '在比赛报道里，doping 常说违规借药物提高表现；在芯片课里，则是加入少量物质改变材料性质。同形词跨了两个领域。',
 'dope 去末尾 e 加 -ing，形成活动名词、分词。各义承 dope 的药物、材料处理等不同动词分支。',Do[:1]+[['dope + -ing → doping','用药、掺杂、涂布等过程']],
 'a doping investigation 兴奋剂调查，semiconductor doping 半导体掺杂，doping levels 掺杂水平。',
 'semiconductor doping；a doping investigation。',
 '材料里的 doping 是技术过程名，不能自动翻成体育作弊；体育报道则需按竞赛及规则语境读。',
 ('The athlete denied involvement in doping.','这名运动员否认参与使用兴奋剂。'),('The chapter explains semiconductor doping.','这一章解释半导体掺杂。'))
W('dopant','英 /ˈdəʊpənt/；美 /ˈdoʊpənt/','掺杂剂、掺杂物',
 '少量加进材料，用来改变电学、光学等性质的那份物质，是 dopant。它按“起掺杂作用的东西”命名。',
 'dope 掺杂去末尾 e + -ant，表示起作用的物质；与 doping 掺杂过程相配。',Do[:1]+[['dope + -ant → dopant','加入材料、改变其性质的掺杂物']],
 'a dopant in a semiconductor 半导体中的掺杂物，dopant concentration 掺杂物浓度。',
 'dopant concentration；a semiconductor dopant。',
 'dopant 指加入的物质，doping 指加入、处理过程；这里的 -ant 不限人，也能指物质。',
 ('The diagram shows dopant atoms in the material.','图示展示了材料中的掺杂原子。'),('The researchers compared samples with different dopant concentrations.','研究人员比较了掺杂物浓度不同的样品。'))
W('dopey','英 /ˈdəʊpi/；美 /ˈdoʊpi/','迷迷糊糊的、反应迟钝的；傻气的',
 '人像没完全醒来，反应慢半拍，可以说 dopey。也能批评一个主意傻乎乎；它是口语评价，要顾及语气。',
 'dope + -y，常见拼写保留 e 成 dopey，也见 dopy。承 dope 的呆傻、迟钝人物或状态分支。',Do[:1]+[['dope + -y → dopey','迟钝迷糊；傻气的']],
 'feel dopey 感到迷糊，a dopey grin 傻乎乎的笑，a dopey idea 傻主意。',
 'feel dopey；a dopey grin。',
 'dopey 描述外在反应、主观感觉或评价；并不必然说明用了药，也不是正式诊断。',
 ('He still felt dopey after waking from a long nap.','睡了很长一觉起来，他还觉得迷迷糊糊。'),('She gave him a dopey grin.','她朝他傻乎乎地笑了笑。'),sources=['https://en.wiktionary.org/wiki/dopey#English','https://www.etymonline.com/word/dopey'])
R('B3776','浓稠配制物的旧名，分成药物、材料与口语评价','DOPE：先有配制物，后面各个领域各走一支','dope → doping、dopant；dopey 接迟钝、傻气义。',
 '不要把材料掺杂和体育兴奋剂硬讲成同一个现代意思。doping 是过程，dopant 是加入的物质；口语 dope 很棒与 dopey 傻气又要看实际词形。',
 'doop 蘸酱 → dope 配制物；去 e + -ing、-ant；dopey 常保留 e + -y。',
 [['原词与材料、体育过程','dope · doping · dopant'],['迟钝、傻气的性质','dopey']],
 'doping 跨领域多义；dope 很棒的与 a dope 傻瓜的词性、语气不同。',
 'In materials science, doping is the process and a dopant is the substance added.\n\n在材料科学里，doping 是掺杂过程，dopant 是加入的物质。','dope doping dopant dopey')
Pr=[['praedicere 预先说 → predict → predictable','预测 → 可以预测的'],['predictable + -ly → predictably','按可预料的方式；果然、不出所料']]
W('predictably','/prɪˈdɪktəbli/','可预见地；果然、不出所料',
 '事情沿着你大概猜到的方向发生，就是 predictably。用在句首，常像中文“果然”：说话人觉得结果并不意外。',
 'predictable + -ly；-able 变 -ably，结尾通常 /əbli/。从可预测的性质变为方式副词或整句评注。',Pr,
 'behave predictably 表现得有规律，Predictably, ... 果然……；设备行为可预测通常是优点，故事套路可预测可能被嫌乏味。',
 'behave predictably；respond predictably；Predictably, ...。',
 'predictably 不保证说话人事先实际做过预测；有时是事后表达“这结果很容易想到”。',
 ('The system behaves predictably under normal conditions.','系统在正常条件下表现稳定、可预料。'),('Predictably, the free tickets were gone within minutes.','不出所料，免费票几分钟就领光了。'))
R('B4473','能否预先看出结果，副词再评论实际发生方式','PREDICTABLE：规律足够清楚，结果就容易想到','predictable → predictably；unpredictable 难以预料。',
 '设备可靠可预期常是好事，情节毫无意外则可能乏味。predictably 可以说明动作方式，也能在句首评论整个结果。',
 'predict + -able → predictable；-able → -ably；un- 否定。',
 [['性质、方式与相反性质','predictable · predictably · unpredictable']],
 'predictable 的好坏看场合；predictably 不一定意味着实际早已写下预测。',
 'A predictable system responds predictably, while an unpredictable one surprises its users.\n\n行为可预测的系统反应可预料；难以预料的系统则让用户意外。','predictable predictably unpredictable')
R('B4448','暖起来的过程，房屋落成习俗形成复合名称','WARMING：让东西暖起来，也能把新家变得有人气','warming → housewarming。',
 '温度上升、汤给人暖意，是 warming 的通常用法。housewarming 作为乔迁聚会名称，还保留把新屋暖起来的文化背景。',
 'warm + -ing → warming；house + warming → housewarming。',
 [['暖意过程与乔迁聚会','warming · housewarming']],
 'housewarming 通常是乔迁聚会，具体活动不要求真的给房子升温。',
 'They served warming soup at the housewarming.\n\n他们在乔迁聚会上端出了暖身的汤。','warming housewarming')
Wr=[['古诺尔斯相关漂流、抛上岸词，经盎格鲁诺曼语 → 中古英语 wrek','海难、被冲上岸的船货等'],['wreck → 严重毁坏及毁坏的东西、人的崩溃状态','-age 集合残骸；-er 拆解者、拖车等']]
W('wreck','/rek/','严重毁坏；失事、残骸；破败物；身心崩溃的人',
 '船、车坏到面目全非，是 wreck；被毁掉的计划也能这样说。a nervous wreck 则像人被焦虑折腾得快散架了。',
 '中古英语 wrek 经盎格鲁诺曼语，联系北欧漂流物、海难词族。由失事、被冲上岸的船货扩展到严重毁坏与相关状态；开头 w 不发音。',Wr[:1]+[['wreck 失事物、残骸 → 动词及比喻','严重破坏；人被折腾得筋疲力尽']],
 'a shipwreck 船难、沉船，wreck a plan 毁掉计划，a nervous wreck 极度焦虑、身心疲惫的人。',
 'wreck a car；wreck a plan；a nervous wreck。',
 'wreck /rek/ 与 wreak /riːk/ 读音、常见搭配不同；wreak havoc 是造成严重破坏的固定表达。',
 ('The storm wrecked several boats.','风暴毁坏了几条船。'),('I was a nervous wreck before the interview.','面试前，我紧张得快崩溃了。'))
W('wreckage','/ˈrekɪdʒ/','残骸、毁坏后留下的碎片',
 '东西已严重损坏，现场剩下一堆破片、扭曲结构，就是 wreckage。-age 在这里把残余部分作为一整体来谈。',
 'wreck + -age，构成集合性名词。由毁坏的东西走到事故、破坏后的残存部分，通常不可数。',Wr[:1]+[['wreck + -age → wreckage','毁坏后留下的残存物集合']],
 'the wreckage of a plane 飞机残骸，clear the wreckage 清理残骸，pieces of wreckage 几块残骸。',
 'aircraft wreckage；clear the wreckage；pieces of wreckage。',
 'a wreck 可指一艘毁船、一辆报废车；wreckage 看留下的残片整体，通常不说 several wreckages。',
 ('Rescuers searched the wreckage.','救援人员搜查了残骸。'),('Pieces of wreckage washed up on the beach.','几块残骸被冲上了海滩。'))
W('wrecker','英 /ˈrekə/；美 /ˈrekər/','破坏者；废车拆解者；拖车',
 'wreck 严重损坏，-er 可以指造成破坏的人；行业里也指拆解废车、回收零件的人或企业，美式还常指处理故障车的拖车。',
 'wreck + -er，执行者、工具名。拖车义来自处理失事、故障车辆的用途，不意味着拖车故意把汽车弄坏。',Wr[:1]+[['wreck + -er → wrecker','破坏者、拆解者；处理故障车的拖车']],
 'call a wrecker 叫拖车，an auto wrecker 废车拆解者、企业，a wrecker of plans 破坏计划者。',
 'a tow truck／wrecker；an auto wrecker。',
 'wrecker 的角色看语境；拆车行业与故意破坏不是同一评价。',
 ('They called a wrecker to remove the damaged car.','他们叫来拖车移走受损汽车。'),('The auto wrecker salvaged usable parts.','废车拆解商回收了可用零件。'))
R('B3951','从海难到严重毁坏，再看残骸与处理者','WRECK：东西毁得厉害，剩下什么、由谁处理','wreck → wreckage、wrecker。',
 'wreck 说毁坏及毁掉的物体；wreckage 集合地说残存碎片；wrecker 可造成破坏，也可负责拆解、拖走受损车辆。',
 '北欧相关词经盎格鲁诺曼语 → wrek → wreck；-age 集合，-er 人、工具；w 不发音。',
 [['毁坏、残存物与处理者','wreck · wreckage · wrecker']],
 'wreckage 通常不可数；wrecker 按对象可能是拖车或拆解者。',
 'The wrecker removed the wreck while workers cleared the wreckage.\n\n拖车拖走了受损汽车，工人清理了残骸。','wreck wreckage wrecker')
Z=[['拟声 zip，模仿轻小物体嗖地掠过','快速运动的声音、动作'],['zipper 商品命名 → 拉链通名；zip 拉上、合拢','后来计算机沿打包压缩的概念用 zip'],['un- 反向；-ed 状态；-y 性质','unzip 打开、解压；zipped、unzipped；zippy 轻快']]
W('zip','/zɪp/','嗖地移动；拉上拉链；压缩文件；拉链；活力；零',
 '嗖地一过去，是 zip；拉链一拉合拢，也带着这股轻快感。文件 zip 起来则是打包压缩；口语 zip 还可说活力，或一点也没有。',
 '起于模仿快速掠过声音的拟声词。拉链动词可接 zipper、zip 拉链名词；计算机压缩义为后来的技术用法。零的俚语义另有发展，不强接成确定故事。',Z[:2],
 'zip up a jacket 拉上夹克拉链，zip past 飞快掠过，zip the files 压缩文件；zip code 美国邮政编码里的 ZIP 另为 Zone Improvement Plan 缩写。',
 'zip up；zip past；zip a file。',
 'zip a file 是压缩，不等于加密；有无加密要看实际设置。美国邮编缩写 ZIP 的来源也不能只按拟声词理解。',
 ('She zipped past us on her bicycle.','她骑自行车嗖地从我们身边过去。'),('He zipped the files into a single archive.','他把这些文件压缩进一个归档文件。'))
W('zipper','英 /ˈzɪpə/；美 /ˈzɪpər/','拉链',
 '两排齿牙一拉就合在一起，像嗖地闭合，zipper 把快速动作变成了工具名。这个名称还经历过商品命名再成为通名的过程。',
 'zip + -er，双写 p。早期 Zipper 商品名用于配这种扣合装置的靴子，后来用于装置本身，成为普通拉链名。',Z[:1]+[['zip + -er → zipper；商品名进入通用名称','拉链、拉链式扣合装置']],
 'a broken zipper 坏拉链，the zipper on a bag 包上的拉链；英式常也直接叫 zip。',
 'a zipper on a jacket；a broken zipper。',
 'zipper 是扣合装置，zip 作动词才说明拉动、合上；button 是另一类纽扣结构。',
 ('The zipper on my bag is stuck.','我的包拉链卡住了。'),('She checked that the zipper was fully closed.','她检查了拉链是否完全拉好。'),sources=['https://en.wiktionary.org/wiki/zipper#English','https://www.etymonline.com/word/zipper'])
W('zipped','/zɪpt/','拉上拉链的；压缩了的；zip 的过去式、过去分词',
 '袋口的拉链已经合好，是 zipped；文件已经装进压缩包，也能说 zipped。两个都是 zip 动作完成的状态。',
 'zip + -ed，短元音后双写 p；/p/ 后 -ed 读 /t/。还有与美国 ZIP 邮编相关的较少见同形用法，来源另看缩写。',Z[:2]+[['zip + -ed → zipped','拉链合拢、文件压缩完成的状态']],
 'a zipped pocket 拉好拉链的口袋，a zipped file 压缩文件，keep the bag zipped 保持包口拉好。',
 'a zipped pocket；a zipped archive。',
 'zipped file 描述打包压缩状态，并不自动说明内容安全或有密码。',
 ('Keep the pocket zipped while you travel.','出行时把口袋拉链拉好。'),('The zipped archive contains three documents.','压缩归档里有三份文档。'))
W('unzip','/ʌnˈzɪp/','拉开拉链；解压缩',
 'zip 把两排拉链合上，unzip 沿反向把它打开。文件已经打成压缩包，再取出恢复，就是计算机里的 unzip。',
 'un- 撤去、反向 + zip。先承拉链动作，技术领域也承 zip 压缩的反向过程。',Z[:2]+[['un- + zip → unzip','打开拉链；还原压缩文件']],
 'unzip a jacket 拉开夹克拉链，unzip an archive 解压归档文件。',
 'unzip a bag；unzip the files。',
 'unzip 是解压，decrypt 是解密；有些文件兼有压缩与加密，两种过程仍有不同含义。',
 ('She unzipped her jacket when she came inside.','进屋后，她拉开夹克拉链。'),('Unzip the archive to view its contents.','解压归档即可查看里面的文件。'))
W('unzipped','/ʌnˈzɪpt/','拉链敞开的；已经解压的；unzip 的过去式、过去分词',
 '先合拢，再打开，留下 unzipped 的状态。衣袋看开口，文件看从压缩包里取出后的状态。',
 'unzip + -ed，双写 p，末尾 -ed 读 /t/；形容词还可按 un- + zipped 理解。',Z[:2]+[['unzip + -ed → unzipped','已经拉开或解压的状态']],
 'an unzipped bag 拉链敞开的包，unzipped files 解压后的文件。',
 'leave a bag unzipped；unzipped files。',
 'unzipped 的具体意思由包、衣物还是文件决定；解压后文件仍可能需要专门软件才能阅读。',
 ('He noticed that his backpack was unzipped.','他发现背包拉链敞着。'),('The unzipped files appeared in a new folder.','解压后的文件出现在新文件夹里。'))
W('zippy','/ˈzɪpi/','轻快的、敏捷的；充满活力的',
 '像 zip 嗖地走起来，zippy 就有轻快、利落的感觉。可以说小车反应快，也可以说曲调活泼。',
 'zip 快速动作、活力 + -y，双写 p，形成口语形容词。',Z[:1]+[['zip + -y → zippy','快速、轻快、充满活力的']],
 'a zippy little car 轻快灵活的小车，a zippy tune 活泼曲调。',
 'a zippy car；a zippy tune。',
 'zippy 带活泼轻快的口语色彩，通常比普通 fast 更有感觉描述。',
 ('The band opened with a zippy tune.','乐队用一支轻快曲子开场。'),('The little car felt zippy in city traffic.','这辆小车在城市车流里显得很轻快灵活。'))
W('zipline','/ˈzɪplaɪn/','滑索、飞索；乘滑索滑行',
 '人悬在索道的滑轮下，沿钢索嗖地滑向另一端，zip 的速度感加 line 索线，就形成 zipline。',
 'zip 快速移动 + line 索线，现代复合词，也常见 zip line、zip-line 写法；这里统一讲连写词。',Z[:1]+[['zip + line → zipline','沿高架索线滑行的装置、活动']],
 'ride a zipline 乘滑索，a zipline across the valley 横跨山谷的滑索。',
 'a zipline ride；ride a zipline。',
 'zipline 指这种索道滑行装置或活动；普通缆车 cabin、cable car 是不同具体设备。',
 ('The zipline stretched across the valley.','滑索横跨山谷。'),('They watched visitors ride the zipline.','他们看游客乘滑索滑行。'))
R('B4346','嗖地移动的拟声形象，连接拉链、开合与文件压缩','ZIP：一拉合上，反向打开；再借到文件打包','zip → zipper、zipped；unzip → unzipped；zippy 轻快，zipline 滑索。',
 '快速动作提供听觉记忆，拉链合拢提供开合画面；文件压缩、解压沿技术领域理解。相同拼写的美国 ZIP 邮编缩写另有来源。',
 '拟声 zip；zip + -er、-ed、-y 时双写 p；un- 反向；line 索线形成 zipline。',
 [['动作、工具与合拢状态','zip · zipper · zipped'],['反向打开与状态','unzip · unzipped'],['速度感与滑索复合','zippy · zipline']],
 '压缩、解压与加密、解密是不同操作；ZIP 邮编缩写另指 Zone Improvement Plan。',
 'She unzipped the bag, found the drive, and copied the zipped archive.\n\n她拉开包，找到存储盘，复制了压缩归档。','zip zipper zipped unzip unzipped zippy zipline')
if __name__=='__main__':save('continuation_20261030_mw',ROOTS,WORDS)
