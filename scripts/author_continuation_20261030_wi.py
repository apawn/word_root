"""Common finite verbs and past forms with useful everyday distinctions."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'B2558':dict(words=['give','gives'],label='give → gives：给、产生与表达',note='gives 的词尾读 /z/；give 的硬 g 有古诺尔斯语同源形式的历史影响。'),
 'B2498':dict(words=['take','takes'],label='take → takes：拿、带；需要、花费',note='takes 是单数主语后的现在式，也可作录制次数、看法等名词复数；take 借北欧词族进入晚期古英语。'),
 'C0232':dict(words=['include','includes'],label='include → includes：把内容算在里面',note='includes 的词尾 /dz/ 不添音节；include 接拉丁 in- 加 claudere 围在内的词源。'),
 'A1741':dict(words=['happen','happens','find','finds'],label='happen／find 的常用第三人称形式',note='happens 说发生、碰巧，finds 说找到或发现，也可数发现物；各词历史分别看，不能因同页就当同源。'),
 'B2431':dict(words=['name','named'],label='name → named：命名、点名、任命',note='name 去末尾 e，加完整 -ed，named 词尾读 /d/；named after 是以……命名。'),
 'B4199':dict(words=['post','posted'],label='post → posted：发布、寄出与派驻',note='post 的柱、邮递、岗位等材料有不同历史路线；posted 不一律按前缀 post- 在后解释。'),
 'B3718':dict(words=['like','likes'],label='like → likes：喜欢；喜好、点赞',note='likes 的动词与喜好名词用法联系喜欢；the likes of 等相似类别表达还需看 like 的相像词族。'),
 'A1740':dict(words=['seem','seemed'],label='seem → seems／seemed：看起来如此',note='seemed 的 -ed 读 /d/；was 的判断与 seemed 的印象不同，后者保留外观、推断角度。'),
 'B3201':dict(words=['help','helped'],label='help → helped：帮忙；使改善',note='helped 的 -ed 读 /t/；现代规则过去式由早期本族动词的发展形成，不能反推古英语始终也是规则变化。'),
 'B2487':dict(words=['open','opened'],label='open → opened：打开了；开放、开始营业了',note='opened 的词尾读 /d/；open 是形容词，opened 是动词过去式或分词，状态和动作结构不同。'),
 'B3101':dict(words=['live','lived'],label='live → lived：住过、生活过',note='lived 作为生活动词的过去形式读 /lɪvd/；与 live 直播、活的形容词读音另分。'),
 'C0769':dict(words=['move','moves'],label='move → moves：移动、调动；举动、招数',note='move 接法语、拉丁 movere 的移动词族；moves 的名词、动词都常见，词尾读 /z/。'),
}
W('gives','/ɡɪvz/','给、给予；产生、表达；give 的第三人称单数',
 '把东西交到别人那里，是 gives；给出建议、带来机会、让人有某种感觉，也可以沿着给予的画面理解。',
 'give 已有 e，直接加 s；/v/ 后读 /z/。give 继承古英语 giefan 等词族，现代硬 g 受到古诺尔斯语 gefa 等同源形式影响。',
 [['古英语 giefan 及北欧同源形式的影响 → give','给予、交出'],['give + -s → gives','单数主语现在给予、产生某效果']],
 'gives advice 给建议；gives a smile 露出微笑；gives someone a chance 给某人机会；gives up 放弃；gives off a smell 散发气味。',
 'gives me time；gives a clear answer。','She gives me a book 与 She gives a book to me 都能交代人和物。gives up 与 gives off 是整组搭配，意思要连后面的小词一起看。',
 ('This window gives the room plenty of light.','这扇窗让房间光线充足。'),('He gives clear instructions before each task.','每项任务开始前，他都会作出清楚的说明。'),sources=['https://en.wiktionary.org/wiki/gives#English','https://en.wiktionary.org/wiki/give#English'])
W('takes','/teɪks/','拿、带、采取；花费、需要；拍摄遍次、看法等名词复数',
 '把东西拿到手、把人带走是 take；做事要占用多少时间、需要什么条件，也常用 takes 来说。',
 'take 已有 e，加 s；/k/ 后读 /s/。take 借古诺尔斯语 taka 等北欧形式进入晚期古英语 tacan；名词 take 的录制、看法等用法由相关动作发展。',
 [['古诺尔斯语 taka 等 → 晚期古英语 tacan → take','抓住、取得 → 拿、带、采取等'],['take 名词、动词 + -s → takes','单数主语拿、需要；多次录制、多种看法']],
 'takes time 需要时间；takes the bus 坐公交；takes a photo 拍照；takes care of ... 照顾……；several takes 拍摄了几遍；different takes on ... 对……的不同看法。',
 'takes ten minutes；takes a different approach。','It takes me an hour to walk there 是走去那里要花我一小时；I spend an hour walking 是我花一小时走路。两者主语和后面的结构不同。',
 ('It takes about ten minutes to walk to the station.','步行到车站大约需要十分钟。'),('We recorded three takes before choosing the best one.','我们录了三遍，才选出最好的一遍。'),sources=['https://en.wiktionary.org/wiki/takes#English','https://en.wiktionary.org/wiki/take#English'])
W('includes','/ɪnˈkluːdz/','包括、包含；把……算在内；include 的第三人称单数',
 '画一个范围，把某些东西圈在里面，就是 includes。它指出哪些项目已算进去，名单也可能还有其他项目。',
 'include 已有 e，加 s；/d/ 后读 /z/，结尾 /dz/。拉丁 in- 在内 + claudere 关、围形成 includere，英语借入相关整词。',
 [['拉丁 in- + claudere → includere → include','围在里面 → 包括、算入'],['include + -s → includes','单数主语现在包含、包括']],
 'the price includes breakfast 价格含早餐；includes everyone 包括每个人；includes the cost of ... 包含……的费用。',
 'includes several examples；includes tax。','A includes B 是 B 算在 A 里面；不自动说 A 只有 B。The bag contains books 更直接说包里装着书，The course includes reading 说课程内容包括阅读。',
 ('The price includes breakfast and a bus ticket.','价格包含早餐和一张公交票。'),('The guide includes examples from everyday conversations.','指南包含日常对话中的例子。'),sources=['https://en.wiktionary.org/wiki/includes#English','https://en.wiktionary.org/wiki/include#English'])
W('happens','/ˈhæpənz/','发生；碰巧；happen 的第三人称单数',
 '事情出现、发生了，用 happens；一个人恰好在某处或做了某事，也能说 happens to。事情本身可以好，也可以坏。',
 'happen + -s，/n/ 后读 /z/。happen 接中古英语 happenen 等，通常联系 hap 机缘、偶然事件与动词材料 -en；更早形成细节有不同解释。',
 [['中古英语 hap 等相关材料 → happen','机缘、事件 → 发生、碰巧'],['happen + -s → happens','单数事件发生；某人碰巧做']],
 'What happens next? 接下来会怎样？；happens every day 每天发生；happens to be ... 碰巧是、在……；as it happens 碰巧、说来也巧。',
 'it happens often；happens to know。','happens to someone 是事情发生在某人身上，happens to do 是碰巧做某事。Something happens 是主动结构，不加 is 来造被动。',
 ('What happens if we miss the last bus?','如果错过末班车，会怎么样？'),('She happens to know the owner of the shop.','她恰好认识店主。'),sources=['https://en.wiktionary.org/wiki/happens#English','https://en.wiktionary.org/wiki/happen#English'])
W('named','/neɪmd/','命名了；点名、列举、任命了；名叫……的；name 的过去式和过去分词',
 '把一个名字明确安到人、物或职位上，是 named。它能说起名字，也能说公告指出谁，或宣布由谁担任。',
 'name 去末尾 e，加完整 -ed；/m/ 后读 /d/。名词接古英语 nama、noma，动词有 namian 等相关形式；现代按规则产生 named。',
 [['古英语名称、命名词族 → name','名字；命名、说出名称'],['name 去 e + -ed → named','过去命名、点名、任命；名叫……的']],
 'a boy named Tom 名叫汤姆的男孩；named after ... 以……命名；named the winner 宣布获胜者；named someone as ... 指出某人是……；named captain 任命为队长。',
 'was named after her grandmother；named in the report。','was named after someone 是名字取自某人；was named in a report 是报告里提到了名字。after 与 in 交代的关系不同。',
 ('The boat was named after the owner’s daughter.','这条船以船主女儿的名字命名。'),('Three people were named in the announcement.','公告里点到了三个人的名字。'),sources=['https://en.wiktionary.org/wiki/named#English','https://en.wiktionary.org/wiki/name#English'])
W('posted','英 /ˈpəʊstɪd/；美 /ˈpoʊstɪd/','张贴、发布了；寄出了；派驻了；post 的过去式和过去分词',
 '信息贴出去、信寄出去、人派到岗位上，都能说 posted。共同的现代感觉是把内容或人员安排到某个位置，但几个 post 的历史路线要分别看。',
 'post + -ed，/t/ 后读 /ɪd/。柱义接拉丁 postis；邮递义经法语 poste、意大利 posta 驿站；岗位、派驻也与法语 poste 相关，不都归在英语 post- 在后。',
 [['不同借入路线的 post：柱、驿站与岗位等','张贴告示；递送邮件；派到岗位'],['post + -ed → posted','过去发布、寄出、派驻']],
 'posted a notice 张贴告示；posted a photo online 网上发照片；posted a letter 寄信〔常见英式〕；was posted abroad 被派驻国外；keep someone posted 随时告知进展。',
 'posted on the website；keep me posted。','posted online 说明放到网上了，posted a letter 是寄了信。keep me posted 是让我随时知道进展，不是让我一直去发帖。',
 ('The timetable was posted beside the entrance.','时间表贴在入口旁。'),('Please keep me posted if the delivery time changes.','如果送达时间有变，请及时告诉我。'),sources=['https://en.wiktionary.org/wiki/posted#English','https://en.wiktionary.org/wiki/post#English'])
W('likes','/laɪks/','喜欢；喜好；点赞；像……这类的人或物〔部分固定搭配〕',
 'She likes music 是她喜欢音乐；her likes 是她喜欢的东西；网页上的 likes 是别人点的赞。现代使用里，喜欢的态度变成了可数的反馈。',
 'like + -s，/k/ 后读 /s/。喜欢动词接古英语 līcian 合意、使愉快；相像等用法接古英语 ġelīc 等另一支，远源相关但具体语义过程未完全确定。',
 [['古英语 līcian → 喜欢义 like；另看 gelic 等相像词材料','合意、喜欢；相像、同类等路线'],['like 名词、动词 + -s → likes','单数主语喜欢；喜好、点赞；同类的固定表达']],
 'likes and dislikes 好恶；likes reading 喜欢阅读；received many likes 收到很多点赞；the likes of ... 像……这样的一类人、事物。',
 'likes to cook；her likes and dislikes。','She likes ... 中 likes 是动词；her likes and dislikes 中是名词。the likes of ... 说类似的一类，语气可能中性，也可能带不屑，要看整句话。',
 ('He likes reading on the train.','他喜欢在火车上看书。'),('The photo received more likes than I expected.','这张照片收到的点赞比我预想的多。'),sources=['https://en.wiktionary.org/wiki/likes#English','https://en.wiktionary.org/wiki/like#English'])
W('seemed','/siːmd/','似乎、看起来当时是；seem 的过去式和过去分词',
 '根据当时的外表、表现或线索，你觉得事情像是某种样子，就用 seemed。它保留你是在作判断的感觉。',
 'seem + -ed，/m/ 后读 /d/。seem 借古诺尔斯语 sœma 适合、相称一系，经中古英语发展为显得、似乎。',
 [['古诺尔斯语 sœma 等 → 中古英语 → seem','适合、相称 → 显得如此'],['seem + -ed → seemed','过去看起来、似乎']],
 'seemed tired 当时显得累；seemed to know 似乎知道；it seemed that ... 当时似乎……；seemed like a good idea 当时像个好主意。',
 'seemed reasonable；seemed to be working。','She was calm 直接说她平静；She seemed calm 是她看起来平静，留有内心可能不同的余地。seemed 是过去的印象，不自动评价现在怎样。',
 ('The room seemed larger in the photograph.','照片里这个房间显得更大。'),('He seemed to know exactly where to go.','他似乎很清楚该往哪里走。'),sources=['https://en.wiktionary.org/wiki/seemed#English','https://en.wiktionary.org/wiki/seem#English'])
W('helped','/helpt/','帮了；促成、改善了；help 的过去式和过去分词',
 '你添了一把力，让事情更容易完成，或让情况好一点，就是 helped。帮忙的人、工具、安排都能作主语。',
 'help + -ed；/p/ 后读 /t/，不另加 /ɪd/。help 名词、动词接古英语 help、helpan 等；早期动词还有其他变化，现代常规过去形式是 helped。',
 [['古英语 help／helpan → help','帮助、使得到支持'],['help + -ed → helped','过去帮忙、起了改善作用']],
 'helped me carry ... 帮我搬……；helped me to carry ... 也可；helped with the work 帮着做工作；helped improve ... 有助改善……。',
 'helped a lot；helped make it possible。','helped someone do 与 helped someone to do 都可用。It helped 说它起了作用；It was helped by ... 说它受到了……的帮助，主语角色不同。',
 ('The diagram helped me understand the instructions.','这张图帮助我看懂了说明。'),('Everyone helped with the cleaning after the event.','活动结束后，大家都帮着打扫。'),sources=['https://en.wiktionary.org/wiki/helped#English','https://en.wiktionary.org/wiki/help#English'])
W('finds','/faɪndz/','找到、发现、认为〔find 的第三人称单数〕；发现物〔复数〕',
 '终于找到一个东西，或看清一个以前没注意的情况，是 finds。名词 a find 是一个值得注意的发现，复数便是 finds。',
 'find + -s，/d/ 后读 /z/。find 继承古英语 findan；动词过去式、过去分词是 found，现在第三人称才用 finds。发现物名词由相应动词用法发展。',
 [['古英语 findan → find','找到、发现；认识到'],['find 名词、动词 + -s → finds','单数主语发现、觉得；多个发现物']],
 'finds a key 找到钥匙；finds it useful 觉得有用；finds out ... 查明……；archaeological finds 考古发现物；finds from a market 市场淘来的好东西。',
 'finds a solution；finds it hard to ...。','She finds it difficult to ... 是她觉得做……困难，it 先占着位置，真正要说的动作在后面。finds 是现在形式，found 才表示过去找到。',
 ('She often finds useful books in second-hand shops.','她常在二手店淘到实用的书。'),('The museum displays finds from the old settlement.','博物馆展出那处旧聚落的出土发现物。'),sources=['https://en.wiktionary.org/wiki/finds#English','https://en.wiktionary.org/wiki/find#English'])
W('opened','英 /ˈəʊpənd/；美 /ˈoʊpənd/','打开了；开放、开始营业了；open 的过去式和过去分词',
 '原来合着的门被打开，店开始接客，新的机会被打开，都可以说 opened。句子要看是谁打开，还是事物自己开放。',
 'open + -ed，/n/ 后读 /d/，不添 /ɪd/ 音节。open 形容词接古英语 open，动词也有早期相应形式；这里末尾 en 不拆成新加的使动后缀。',
 [['古英语 open 及相关动词形式 → open','敞开的；使打开'],['open + -ed → opened','过去打开、开始开放或营业']],
 'opened the door 打开了门；the shop opened 店开门了；opened an account 开了账户；opened up new possibilities 带来新的可能。',
 'opened at nine；opened to the public。','The door is open 说门现在开着；The door was opened 说门被打开了。The shop opened at nine 说开门动作发生在九点，不能把形容词 open 和动词 opened 的结构混用。',
 ('She opened the envelope carefully.','她小心地拆开信封。'),('The new library opened to the public last week.','新图书馆上周向公众开放了。'),sources=['https://en.wiktionary.org/wiki/opened#English','https://en.wiktionary.org/wiki/open#English'])
W('lived','/lɪvd/','住过；生活过；活过；live 的过去式和过去分词',
 '人在什么地方住，怎样过日子，生命延续了多久，都能用 lived。具体重点由地点、时间和方式补出来。',
 '生活动词 live 去末尾 e，加完整 -ed，读 /lɪvd/。动词接古英语 libban、lifian；live 直播、活的形容词读 /laɪv/，现代同形但读音和形成路线不同。',
 [['古英语 libban／lifian → live 动词','生活、居住、活着'],['live 去 e + -ed → lived','过去生活、住过；完成形式中的生活经历']],
 'lived in the city 在城里住过；lived alone 独居过；lived to be ninety 活到了九十岁；lived through ... 经历过……；lived up to expectations 达到了期望。',
 'has lived here for years；lived nearby。','He lived here 可说过去住这里；He has lived here for years 常把居住经历接到现在。单凭 lived 的拼写不能判断是否已去世，仍要看句子的时间和内容。',
 ('We lived above a small bakery for two years.','我们在一家小面包店楼上住过两年。'),('The exhibition lived up to our expectations.','这次展览没有辜负我们的期待。'),sources=['https://en.wiktionary.org/wiki/lived#English','https://en.wiktionary.org/wiki/live#English'])
W('moves','/muːvz/','移动、搬动；打动〔动词形式〕；举动、步骤、棋步、舞步等〔复数〕',
 '物体换个位置，是 moves；为达到目标走出一步，也叫 a move。棋盘上的一步、舞蹈里的一个动作，都能数成 moves。',
 'move 已有 e，加 s，/v/ 后读 /z/。move 经古法语相关形式接拉丁 movere 移动；名词步骤、举动等沿相应动作发展。',
 [['拉丁 movere → 古法语 → move','移动；使情绪受到触动等引申'],['move 名词、动词 + -s → moves','单数主语移动、打动；多个步骤或动作']],
 'moves slowly 缓慢移动；moves house 搬家〔常见英式〕；moves me 打动我；dance moves 舞步；next moves 下一步行动；chess moves 棋步。',
 'makes several moves；moves to another city。','The piece moves forward 中是动词，three moves ahead 中是名词。moving 也能作动人的形容词，moves someone 则是使某人感动的动作。',
 ('The boat moves slowly through the narrow channel.','船缓缓穿过狭窄水道。'),('She taught us three simple dance moves.','她教了我们三个简单的舞蹈动作。'),sources=['https://en.wiktionary.org/wiki/moves#English','https://en.wiktionary.org/wiki/move#English'])
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_wi',ROOTS,WORDS)
 extend_lessons()
