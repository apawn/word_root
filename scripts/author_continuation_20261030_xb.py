"""Common past forms in narrative, reports and everyday conversation."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'C0229':dict(words=['claim','claims'],label='clamare → claim → claims：宣称、提出主张',note='claim 经法语接拉丁 clamare；补上现代 claims 的主张、要求和第三人称用法，实际路线按逐词说明读。'),
 'B3642':dict(words=['appear','appeared'],label='appear → appeared：进入视线、显得如此',note='appear 经法语接拉丁 apparere，历史 ad- 加 parere 显露；appeared 的 -ed 读 /d/。'),
 'C0899':dict(words=['cover','covered'],label='cover → covered：盖住、包含到、走过范围',note='cover 经法语接拉丁 cooperire，co- 加强、operire 遮盖；covered 词尾读 /d/。'),
 'C0446':dict(words=['force','forced'],label='force → forced：用力促成、被迫',note='forced 的 /s/ 后过去词尾读 /t/；a forced smile 常说勉强挤出的笑容。'),
 'C0726':dict(words=['mention','mentioned'],label='mention → mentioned：提到、顺带说起',note='mention 接拉丁 mentio 使想起、说到，经法语等进入；mentioned 词尾读 /d/。'),
 'B4236':dict(words=['miss','missed'],label='miss → missed：没赶上、没碰中；想念',note='动作 miss 接古英语 missan；missed 的 /s/ 后加 /t/，与大写称谓 Miss 的缩短来源分开。'),
 'C1526':dict(words=['turn','return','returned'],label='turn → return → returned：转回、返回、归还',note='return 经法语、拉丁相关回转词族借入；现代可用 re- 加 turn 认形，不把全部词史压成新拼词。'),
 'C1325':dict(words=['serve','served'],label='serve → served：服务、端上、担任、发球',note='serve 接拉丁 servīre，经法语借入；served 在 /v/ 后加 /d/，不同服务、任职等搭配看对象。'),
 'B3727':dict(words=['rise','raise','raised'],label='rise／raise → raised：自己升起与使升高',note='raise 接北欧 reisa，与 rise 历史使动同族形式相连；raised 是 raise 的过去形式，rise 的过去式是 rose。'),
 'C1105':dict(words=['support','supported'],label='support → supported：从下面托住、帮助维持',note='support 接拉丁 sub- 加 portare，b 在 p 前同化；supported 在 /t/ 后加 /ɪd/。'),
}
W('appeared','英 /əˈpɪəd/；美 /əˈpɪrd/','出现了；显得、似乎；出版、登载、演出了；appear 的过去式和过去分词',
 '原来看不见，现在进了视线，是 appeared；某种样子呈现在别人面前，又能说显得。文章、演员出现在公众面前，也用这个词。',
 'appear + -ed，词尾读 /d/。经古法语 aparoir 接拉丁 apparere，历史 ad- 加 parere 显露；英语现代把 appear 当完整词基。',
 [['拉丁 ad- + parere → apparere → 古法语 aparoir → appear','显露、出现'],['appear + -ed → appeared','过去出现；显得；公开登载、演出等']],
 'appeared suddenly 突然出现；appeared tired 显得累；appeared to know 似乎知道；appeared in a magazine 登载于杂志；appeared on stage 上台演出。',
 'first appeared；appeared at the door。','appeared tired 是当时看起来累，不直接确认内在感受；appeared in a play 是在剧中演出。句法和介词能帮你分开显得、出现、演出等用法。',
 ('A small boat appeared from behind the rocks.','一条小船从岩石后面出现了。'),('The story first appeared in a local magazine.','这个故事最早发表于当地一本杂志。'),sources=['https://en.wiktionary.org/wiki/appeared#English','https://en.wiktionary.org/wiki/appear#English'])
W('covered','英 /ˈkʌvəd/；美 /ˈkʌvərd/','盖住了；覆盖、包含了；走过了；报道、承担了；cover 的过去式和过去分词',
 '把一层东西铺到表面，是 covered；把话题纳入范围、把一段路程走完、把费用包进去，也能借覆盖范围来理解。',
 'cover + -ed，词尾读 /d/。经古法语 covrir 接拉丁 cooperire，co- 加强语气与 operire 遮盖相关，不是英语 co- 加一个现代 ver。',
 [['拉丁 cooperire → 古法语 covrir → cover','遮盖、盖住；后来有范围、包含等用法'],['cover + -ed → covered','过去盖住、涵盖、走过、承担等']],
 'covered in snow 被雪覆盖；covered the topic 涵盖了话题；covered ten miles 走了十英里；covered the costs 承担了费用；covered the event 报道活动。',
 'covered with a cloth；covered by the report。','covered in／with 常接表面覆盖物，covered by 可接实际覆盖物，也可接报道、规则等覆盖范围。covered the costs 说费用得到承担，paid the bill 更直接说付账。',
 ('The table was covered with old maps.','桌上铺满了旧地图。'),('The short guide covered everything we needed for the visit.','这份简短指南涵盖了我们参观所需的全部内容。'),sources=['https://en.wiktionary.org/wiki/covered#English','https://en.wiktionary.org/wiki/cover#English'])
W('forced','英 /fɔːst/；美 /fɔːrst/','迫使了；被迫的；强行的、勉强挤出的；force 的过去式和过去分词',
 '事情没法顺着来，就用力量、压力或条件把结果推出来，是 forced。被迫离开、强行开门、勉强挤出笑容，都有这种不自然地推动的感觉。',
 'force 去末尾 e，加完整 -ed，/s/ 后读 /t/。force 动词经法语 forcer／forcier 等接拉丁 fortis 强壮的相关词族，和力量名词同源相连。',
 [['拉丁 fortis 相关词族 → 法语 forcer／forcier → force','用力量、压力促成'],['force 去 e + -ed → forced','过去迫使；被迫的、勉强的']],
 'was forced to leave 被迫离开；forced the door open 强行打开门；a forced smile 勉强的笑容；forced a change 迫使作出改变。',
 'forced to wait；a forced laugh。','forced to do 说没有太多选择而做了某事，chose to do 说主动选择。a forced smile 常不是真心自然流露，而是有意挤出来的笑。',
 ('The heavy rain forced us to move the event indoors.','大雨迫使我们把活动搬到室内。'),('He gave a forced smile and changed the subject.','他勉强笑了笑，换了个话题。'),sources=['https://en.wiktionary.org/wiki/forced#English','https://en.wiktionary.org/wiki/force#English'])
W('mentioned','/ˈmenʃənd/','提到了；说起了；mention 的过去式和过去分词',
 '让一件事短暂进入谈话或文字里，是 mentioned。它常只说明说到了，不保证展开解释了。',
 'mention + -ed，/n/ 后读 /d/。名词经法语 mencion 接拉丁 mentio 使想起、说到；英语动词有名词转用及法语 mentionner 影响等相关路线。',
 [['拉丁 mentio → 古法语 mencion → mention；另有相关动词影响','使想起、提及'],['mention + -ed → mentioned','过去提到、说起']],
 'mentioned the problem 提到了问题；mentioned that ... 提到……；mentioned earlier 前面提过；as mentioned above 如上所述。',
 'briefly mentioned；mentioned in the letter。','mentioned 是提到，explained 是作解释。mentioned the issue 不自动说已经查明或解决问题；mentioned doing something 后面可接做过、打算做等由语境决定的内容。',
 ('She mentioned the new timetable during lunch.','午饭时，她提到了新的时间表。'),('The address was mentioned in the last paragraph.','地址在最后一段里提到了。'),sources=['https://en.wiktionary.org/wiki/mentioned#English','https://en.wiktionary.org/wiki/mention#English'])
W('missed','/mɪst/','错过了；没看见、没听到；没击中；想念了；miss 的过去式和过去分词',
 '本来要碰上、赶上或注意到，却没接上，是 missed。想念某人，也可以用少了对方的感觉来理解。',
 'miss 原有 ss，直接加 -ed；/s/ 后读 /t/，读 /mɪst/，一个音节。动作词接古英语 missan 等缺失、未中材料；大写 Miss 称谓来自 mistress 的截短，另源。',
 [['古英语 missan 等 → miss','未中、缺失；现代错过、想念等分支'],['miss + -ed → missed','过去没赶上、没注意到、未击中；想念']],
 'missed the bus 没赶上公交；missed the point 没领会要点；missed a call 漏接电话；missed someone 想念某人；a missed opportunity 错失的机会。',
 'nearly missed；was missed by everyone。','missed 与 mist 雾在常见口音里同音，拼写、词性不同。I missed the message 常说没看到消息，I missed you 则常说想念你，意思由对象和场景决定。',
 ('We missed the first five minutes of the film.','我们错过了电影开头五分钟。'),('I missed our conversations while you were away.','你不在的时候，我很想念我们聊天的时光。'),sources=['https://en.wiktionary.org/wiki/missed#English','https://en.wiktionary.org/wiki/miss#English'])
W('returned','英 /rɪˈtɜːnd/；美 /rɪˈtɜːrnd/','回来了、返回了；归还了；回应、回报了；return 的过去式和过去分词',
 '从出去的方向转回来，是 returned；物品回到原主手里，是归还；微笑、帮助等还回对方，又可以说回应、回报。',
 'return + -ed，/n/ 后读 /d/。动词经法语 retorner／retourner，并受中世纪拉丁 retornare 等影响；现代 re- + turn 有助认形，名词另有相连借入路线。',
 [['法语 retorner／retourner 与中世纪拉丁相关形式 → return','转回、返回；归还'],['return + -ed → returned','过去回来、归还、回应']],
 'returned home 回家了；returned to work 回去工作了；returned the book 还书了；returned a smile 回以微笑；returned a call 回电话。',
 'has returned；returned to the topic。','returned the book 直接接归还的物品，returned to the library 是回到图书馆。returned home 通常不加 to，home 在这里作方向表达。',
 ('We returned the keys before leaving the guesthouse.','离开旅馆前，我们归还了钥匙。'),('She returned to the question after a short break.','稍作休息后，她又回到这个问题上。'),sources=['https://en.wiktionary.org/wiki/returned#English','https://en.wiktionary.org/wiki/return#English'])
W('served','英 /sɜːvd/；美 /sɜːrvd/','服务、接待了；端上了；担任、服役了；发球了；serve 的过去式和过去分词',
 '把需要的东西送到人面前、为某个角色或目标出力，是 served。餐馆端菜、在组织里担任职务、球场发球，都是不同搭配。',
 'serve 去末尾 e，加完整 -ed，/v/ 后读 /d/。经法语 servir 接拉丁 servīre 服侍、效力，与 servus 奴仆一系相连；现代服务用法范围很广。',
 [['拉丁 servīre → 古法语 servir → serve','服侍、效力 → 端上、任职等现代分支'],['serve 去 e + -ed → served','过去服务、端上、担任、发球等']],
 'served lunch 端上午餐；served as chair 担任主席；served in the army 在军队服役过；served a purpose 起到了作用；served first 先发球。',
 'was served with tea；served as an example。','served as ... 是担任、起到……作用，served someone 是服务、接待某人。served food 说端菜，prepared food 说备餐、做菜，过程重点不同。',
 ('Lunch was served in the garden.','午餐在花园里供应。'),('The old school served as a meeting place for the village.','那所旧学校曾是村里的聚会场所。'),sources=['https://en.wiktionary.org/wiki/served#English','https://en.wiktionary.org/wiki/serve#English'])
W('raised','/reɪzd/','举起、提高了；提出了；筹集、养育了；raise 的过去式和过去分词',
 '把手、数值或一个问题抬到大家面前，是 raised；把孩子养大、把资金聚起来，也可用 raise。不同对象让向上、使成长的感觉具体化。',
 'raise 去末尾 e，加完整 -ed；/z/ 后读 /d/。raise 经中古英语借北欧 reisa，与 rise 的旧使动同族形式相关；现代 raised 是规则过去形式。',
 [['北欧 reisa → 中古英语 reisen 等 → raise','使升起、竖起；与 rise 的使动关系相连'],['raise 去 e + -ed → raised','过去举起、提高、提出、筹集、养育等']],
 'raised a hand 举手了；raised a question 提出了问题；raised money 筹集资金；raised children 养育孩子；raised the price 提高价格。',
 'was raised in ...；raised concerns。','raised 是 raise 的过去形式，通常带被提高、养育等对象；rose 是 rise 的过去式，常说某物自己上升。The price rose 与 They raised the price 叙述角度不同。',
 ('She raised a useful question at the end of the meeting.','会议快结束时，她提出了一个有用的问题。'),('He was raised in a small town near the coast.','他在海岸附近的一个小镇长大。'),sources=['https://en.wiktionary.org/wiki/raised#English','https://en.wiktionary.org/wiki/raise#English'])
W('supported','英 /səˈpɔːtɪd/；美 /səˈpɔːrtɪd/','支撑了；支持、帮助了；为……提供依据；support 的过去式和过去分词',
 '从下面托住，让东西不倒，是 supported；给人帮助、给观点证据，也都是让它站得住的支持。',
 'support + -ed，/t/ 后读 /ɪd/。拉丁 sub- 在下 + portāre 携带、承载形成 supportare，b 在 p 前同化，前面呈 supp-。',
 [['拉丁 sub- + portare → supportare → 法语等 → support','从下面承载 → 托住、维持、帮助'],['support + -ed → supported','过去支撑、支持；由依据支撑']],
 'supported the roof 支撑屋顶；supported a friend 支持朋友；supported the proposal 支持提议；supported by evidence 有证据支持；supported formats 支持的文件格式等。',
 'fully supported；supported by several sources。','supported by evidence 说有证据支撑，supported by the committee 说得到委员会支持。两种支持的依据不同，不能仅凭 supported 判断它是事实还是态度。',
 ('Two wooden posts supported the small roof.','两根木柱支撑着小屋顶。'),('The explanation was supported by several independent sources.','这个解释得到了几份独立来源资料的支持。'),sources=['https://en.wiktionary.org/wiki/supported#English','https://en.wiktionary.org/wiki/support#English'])
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_xb',ROOTS,WORDS)
 extend_lessons()
