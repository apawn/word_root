"""Everyday actions and lexicalized extensions in existing families."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'A1741':dict(words=['stalk','stalking','sew','sewing'],label='跟踪与缝纫：动作、活动名',note='stalk + -ing → stalking；sew + -ing → sewing。stalk 的植物茎名词与跟踪动词有不同来源分析。'),
 'A1697':dict(words=['coast','coaster','cruise','cruiser','wrestle','wrestler'],label='活动执行者、装置及固定器物名',note='coast + -er → coaster；cruise + -er → cruiser；wrestle + -er → wrestler。coaster 的杯垫义经过器物名称的历史变化。'),
 'A2238':dict(words=['wrestle','wrestler'],label='本族词中的反复、持续动作材料',note='wrestle 接旧英语扭转词族和反复动作形式；wrestler 是对应人物名。'),
 'A1699':dict(words=['nanny'],label='亲昵称呼进入照料者名称',note='nanny 联系 nan、nanna 等亲昵称呼及 -y；更远来源有不同分析，不只凭现代人名强定来源。'),
 'A1740':dict(words=['huge','hugely'],label='巨大程度与程度副词',note='huge + -ly → hugely；huge 的较早法语来源可识别，更远来源未定。'),
 'A1760':dict(words=['harass','harassed','overlooked'],label='骚扰、忙乱与被忽视的分词用法',note='harass + -ed → harassed；overlook + -ed → overlooked。作形容词时看语境判断被骚扰、忙乱或被忽视。'),
}
W('stalk','英 /stɔːk/；美 /stɔːk/ 或 /stɑːk/','茎、梗；悄悄接近；跟踪、纠缠；大步走',
 '植物上支撑叶、花的一根茎可叫 stalk；动词则常让人想到悄悄靠近或不断跟随。两类用法分别记来源。',
 '植物名词经中古英语 stalke 等，接日耳曼支撑、茎的词族；跟踪动词经中古英语 stalken 接旧英语悄悄移动材料，更远分析有分歧。不硬画成植物茎直接变成跟踪。',
 [['名词 stalk 的茎、支撑材料；动词 stalk 的移动材料','两条来源分析分别保留'],['现代不同词义并存','茎梗；悄悄接近、持续跟踪；大步走']],
 'a celery stalk 一根芹菜梗；a cat stalking a bird 悄悄靠近鸟的猫；stalk out of the room 大步走出房间。对人的持续跟踪、纠缠常带负面含义。',
 'flower stalks；stalk a target；stalk away。','植物 stem、stalk 有具体搭配习惯；动词 stalk 比普通 follow 更突出隐蔽、持续或令人不安的跟随。不同词义不能只靠一个动作画面全包。',
 ('She cut a stalk of celery into small pieces.','她把一根芹菜梗切成了小段。'),('The cat stalked a bird through the grass.','猫穿过草丛悄悄靠近一只鸟。'))
W('stalking','英 /ˈstɔːkɪŋ/；美 /ˈstɔːkɪŋ/ 或 /ˈstɑːkɪŋ/','跟踪、尾随、纠缠；潜行跟进；stalk 的 -ing 形式',
 '把持续跟随、反复纠缠这件事当作一个行为来谈。也可在狩猎、动物活动中说隐蔽地接近。',
 '动词 stalk + -ing；英语较早已有相应潜行动作名词。现代针对人的持续跟踪用法又发展出特定社会语境。',
 [['stalk 的潜行、跟进动词词族','悄悄移动、接近'],['stalk + -ing → stalking','潜行行为；持续跟踪、纠缠']],
 'report stalking 反映、举报跟踪纠缠；stalking behaviour 跟踪行为。也可说 a cat stalking prey 猫潜行接近猎物，此时是动词分词结构。',
 'persistent stalking；online stalking。','stalking 对人的用法常是持续、非自愿的纠缠，不等同于普通社交平台 follow 关注。动物狩猎语境的评价又不同。',
 ('The article discusses the impact of stalking on victims.','文章讨论了跟踪纠缠对受害者的影响。'),('We watched a cat stalking its prey.','我们看见一只猫正在悄悄接近猎物。'))
W('coaster','英 /ˈkəʊstə/；美 /ˈkoʊstər/','杯垫；沿海航行的船；滑行者、滑行装置等',
 '今天在桌边最常见的画面，是杯子下保护桌面的垫子。航运、滑行场景又会用到同词的其他分支。',
 'coast 沿边移动、滑行等 + -er。杯垫义经较早的酒瓶托盘名称发展；一种常见解释是托盘能沿桌边滑动、传给客人，后来转为杯垫。',
 [['coast + -er','沿海行进的人、船；滑行者、装置'],['酒瓶托盘名称 → 饮杯下的垫子','移动托盘的命名转到桌面保护用品']],
 'put a glass on a coaster 把玻璃杯放在杯垫上；a set of coasters 一套杯垫。海运资料里 a coastal coaster 可说沿海运输船。',
 'a cork coaster；a coaster under the mug。','-er 不只形成人物名，也能形成装置、器物名。coaster 的杯垫义经过历史转用，不能只靠今天 coast 滑行就完整猜出。',
 ('Please put your mug on a coaster.','请把马克杯放在杯垫上。'),('The shop sells a set of wooden coasters.','商店出售一套木制杯垫。'),sources=['https://www.etymonline.com/word/coaster','https://en.wiktionary.org/wiki/coaster#English'])
W('cruiser','英 /ˈkruːzə/；美 /ˈkruːzər/','巡洋舰；巡游船；巡逻车等',
 '先抓住 cruise 巡航、巡游这个动作，再看执行它的是军舰、休闲船，还是某些语境中的巡逻车辆。',
 'cruise + -er；cruise 的词族经荷兰语交叉航行、巡航等材料进入英语。后缀形成执行巡航任务或用于巡游的对象名。',
 [['cruise + -er','执行巡航、巡游的船或对象'],['cruiser 在不同领域固定用法','巡洋舰、巡游艇；部分语境的巡逻车等']],
 'a naval cruiser 海军巡洋舰；a cabin cruiser 有舱室的休闲游艇；a police cruiser 警用巡逻车〔美式常见〕。搭配决定具体类型。',
 'a cruiser in the harbour；a police cruiser。','cruiser 不是所有客轮的总称；cruise ship 常明确说邮轮。看修饰语，才能把军事、休闲和警用场景分开。',
 ('A naval cruiser entered the harbour at dawn.','一艘巡洋舰黎明时驶入港口。'),('A police cruiser was parked outside the station.','警察局外停着一辆巡逻警车。'))
W('wrestle','/ˈresəl/','摔跤；扭打；努力应对、苦苦思索',
 '两个人缠住对方、用力争夺位置，是摔跤；脑子里与难题反复较劲，也能说 wrestle with a problem。',
 '经中古英语 wrestlen 接古英语 wrǣstlian，联系 wræstan 扭转、用力扭的词族。-le 反映旧的反复动作材料；开头 w、词中 t 现代通常不发音。',
 [['旧英语扭转词族 + 反复动作形式','扭打、身体上的角力'],['现代 wrestle 的比喻发展','与困难、决定反复较劲']],
 'wrestle with an opponent 和对手摔跤；wrestle with a difficult decision 为艰难决定反复思量。比喻里 with 后面常接问题、抉择。',
 'wrestle with a problem；wrestle for control。','wrestle 强调纠缠、角力和费力应对；fight 范围更广，不一定是摔跤式身体接触。',
 ('The children wrestled on the grass.','孩子们在草地上摔跤玩。'),('She wrestled with the decision for several days.','她为这个决定反复思量了好几天。'))
W('wrestler','英 /ˈreslə/；美 /ˈreslər/','摔跤运动员、摔跤手',
 'wrestle 是做摔跤动作，wrestler 是参加这项运动的人。-er 把动作接成相应人物。',
 '经中古英语 wrastlere 等延续，现代对应 wrestle 去末尾 e 加 -er。旧词中已有人物名称，并非英语很晚才临时造出。',
 [['wrestle 的旧英语、中古英语词族','摔跤、角力'],['相应人物形式 wrestler','摔跤运动员、摔跤手']],
 'an Olympic wrestler 奥运摔跤运动员；a professional wrestler 职业摔跤手。具体运动、表演传统由语境说明。',
 'a skilled wrestler；train as a wrestler。','wrestler 是人，wrestling 常说这项运动、摔跤活动；不能把职业人物名与活动名随意互换。',
 ('The wrestler trained every morning.','那位摔跤运动员每天早晨训练。'),('She interviewed an Olympic wrestler after the match.','她在赛后采访了一位奥运摔跤运动员。'))
W('nanny','/ˈnæni/','育儿保姆；祖母〔某些家庭、地区的称呼〕；过度保护、管束',
 '受雇在家照顾孩子的人，常叫 nanny；孩子的日常起居、照料是这个职业称呼的重点。',
 '联系 nan、nanna 等亲昵称呼与 -y 形式；更远可有儿童称呼、女性人名昵称等不同分析，不能强定唯一来源。名词后又产生过度照管的动词比喻。',
 [['nan、nanna 等照料者、长辈称呼的相邻词族','亲昵称呼材料，来源解释不一'],['nanny 的固定用法','育儿保姆；部分家庭的祖母称呼；再有过度照管比喻']],
 'hire a nanny 雇育儿保姆；work as a nanny 当育儿保姆。作动词 nanny someone 有时批评对人管得太细、过度保护。',
 'a live-in nanny；a nanny for two children。','babysitter 常是临时看护孩子的人；nanny 往往有较固定、持续的照料安排。具体职责仍以实际安排为准。',
 ('The family hired a nanny to look after their two children.','这家人雇了一位保姆照顾两个孩子。'),('She worked as a nanny while studying at college.','她读大学时做过育儿保姆。'),sources=['https://www.etymonline.com/word/nanny','https://en.wiktionary.org/wiki/nanny#English'])
W('sew','英 /səʊ/；美 /soʊ/','缝、缝制、缝补',
 '针带着线反复穿过布，把两片接起来，或把破口补上。这个很具体的动作就是 sew。',
 '经中古英语 sewen、sowen 等接古英语 siwian、seowian，属于古老的缝合词族。与 seam 缝、接缝有历史联系。',
 [['古英语 siwian 等 → 中古英语 sewen','用线缝、接合'],['现代 sew','缝制、缝补；过去式 sewed，过去分词 sewn 或 sewed']],
 'sew a dress 缝一条裙子；sew on a button 缝上纽扣；sew up a tear 把破口缝好。拼写 sew 的发音像 sow 播种。',
 'sew by hand；sew two pieces together。','sew 缝制，sow 播种，常同音但意思不同。sewn 是 sew 的常用过去分词，不能只看到 w 就按 new 的读音类推。',
 ('Could you sew this button back on?','你能把这颗纽扣重新缝上吗？'),('She sewed the two pieces of fabric together.','她把两片布缝在了一起。'))
W('sewing','英 /ˈsəʊɪŋ/；美 /ˈsoʊɪŋ/','缝纫；针线活；正在缝的东西；sew 的 -ing 形式',
 '把一针一线这项活动当作一个技能、爱好，就是 sewing；篮子里没做完的针线活也能叫 her sewing。',
 'sew + -ing，较早中古英语已有相应动作名词。现代保留活动名、所做针线活和动词形式等用法。',
 [['sew 缝 + -ing','缝纫这个活动'],['sewing 的名词扩展','缝纫技能、针线活；待缝、正在缝的东西']],
 'a sewing machine 缝纫机；a sewing class 缝纫课；do some sewing 做些针线活。sewing 作活动名时通常不可数。',
 'sewing skills；a sewing needle。','sewing 可以是名词，不只表示正在。a sewing machine 是用于缝纫的机器，不必理解为这台机器此刻正在工作。',
 ('She learned sewing from her grandmother.','她跟祖母学会了缝纫。'),('I keep my sewing in this basket.','我把针线活放在这个篮子里。'))
W('huge','/hjuːdʒ/','巨大的；极大的',
 '体积大到很显眼，或影响、差距、变化大得惊人，都能用 huge。把普通 large 的程度再推高一截。',
 '经中古英语 huge 接古法语 ahuge 高大、巨大的等形式；更远来源未定。有不同推测，不把某一种山丘来源说成定论。',
 [['古法语 ahuge → 中古英语 huge','高大、巨大的'],['现代具体与抽象范围','巨大物体；极大影响、差距、成功等']],
 'a huge building 巨大的建筑；a huge difference 极大差别；a huge success 巨大成功。具体、抽象名词都常接。',
 'a huge amount；a huge impact。','large 可中性陈述尺寸、数量大；huge 通常把程度说得更强。它是形容词，不能直接按 very 的方式修饰另一个形容词。',
 ('A huge tree stood beside the house.','房子旁边立着一棵巨大的树。'),('The new bridge made a huge difference to the village.','新桥给村庄带来了极大的改变。'))
W('hugely','/ˈhjuːdʒli/','极其、非常；在很大程度上',
 '把 huge 的巨大程度用来加强一个评价：hugely successful 就是非常成功，不是在说成功有物理体积。',
 'huge + -ly，形成程度副词；中古英语已有 hugely、hugeliche 等同族形式。',
 [['huge 巨大的 + -ly','把很大的程度转成副词'],['hugely 的常见搭配','极其；在很大程度上']],
 'hugely popular 极受欢迎；hugely successful 极其成功；benefit hugely 获益很大。修饰形容词、动词时都表达程度。',
 'hugely important；hugely enjoyable。','huge 修饰名词，如 a huge success；hugely 修饰形容词，如 hugely successful。记住对应，句子就容易搭对。',
 ('The exhibition was hugely popular.','展览极受欢迎。'),('The students benefited hugely from the extra practice.','额外练习让学生受益很大。'))
W('harass','/həˈræs/，也读 /ˈhærəs/','不断烦扰、纠缠、骚扰',
 '一次次来打扰、施压，让人没法安宁。harass 的劲头在持续、反复，并且对方不欢迎这种行为。',
 '借自法语 harasser 使疲惫、烦扰，更远来源未定，可能联系旧法语驱赶、挑动等材料。不能把 ha-、rass 硬拆成现代英语词根。',
 [['法语 harasser → 英语 harass','使疲惫、反复烦扰'],['现代不同场景的 harass','持续纠缠、骚扰或反复施压']],
 'harass someone with calls 用不断来电骚扰某人；be harassed at work 在工作中遭骚扰；harass someone for payment 不断催某人付款。搭配说明行为方式。',
 'repeatedly harass；harass someone online。','annoy 可以是一次让人烦；harass 常有反复、持续施压的意味。具体行为性质由语境说明，不能只当普通打招呼。',
 ('She asked him to stop harassing her with repeated messages.','她要求他别再不断发消息骚扰她。'),('The reporters harassed the actor for a comment.','记者们不断纠缠那位演员，想让他表态。'),sources=['https://www.etymonline.com/word/harass','https://en.wiktionary.org/wiki/harass#English'])
W('harassed','/həˈræst/，也读 /ˈhærəst/','受到骚扰、烦扰的；忙乱疲惫的；harass 的过去式、过去分词',
 '一层是别人不停来烦你；另一层是事情接连压过来，让人显得忙乱、疲惫。看人的处境和后面搭配来选。',
 'harass + -ed。harass 的使疲惫、不断烦扰材料，进入分词后形成被烦扰的、忙乱的状态形容词；-ed 在这里常读 /t/。',
 [['harass + -ed','过去发生的烦扰；被烦扰'],['分词形容词 harassed','受骚扰的；被琐事折腾得忙乱的']],
 'feel harassed 感到被纠缠、受压力；look harassed 看起来忙乱疲惫；be harassed by someone 被某人骚扰。是否明确有骚扰者，要看句子。',
 'a harassed expression；a harassed parent。','harassed 有时是忙乱神情的形容，不必每次都译成遭到某项明确骚扰。being harassed by someone 则直接给了行为者。',
 ('The receptionist looked harassed as the phones kept ringing.','电话不停地响，接待员显得忙乱不堪。'),('She said she was being harassed by unwanted calls.','她说自己不断受到不请自来的电话骚扰。'))
W('overlooked','英 /ˌəʊvəˈlʊkt/；美 /ˌoʊvərˈlʊkt/','被忽视、漏看的；overlook 的过去式、过去分词',
 '一个细节明明在那里，目光却从它上面过去了，没注意到；overlooked 常把这种被漏掉的状态说出来。',
 'overlook + -ed；overlook 的 over- 越过、在上方与 look 看构成复合，分别发展俯瞰、漏看、宽容等义。分词形容词常取被忽视这一支。',
 [['over- + look → overlook','在上方看、越过而没注意等分支'],['overlook + -ed → overlooked','过去漏看；被漏掉、被忽视']],
 'an overlooked detail 被漏看的细节；an often overlooked problem 常被忽视的问题。We overlooked it 是过去漏看；It was overlooked 是它被漏看。',
 'a frequently overlooked factor；easily overlooked。','looked over 常是检查、浏览，overlooked 常是漏看，两者词序不同。overlook 作俯瞰义时，过去式仍写 overlooked，要按宾语判断。',
 ('One important detail had been overlooked.','一个重要细节被漏掉了。'),('The article highlights an often overlooked problem.','文章强调了一个常被忽视的问题。'))
def extend_lessons():
    extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
    save('continuation_20261030_tb',ROOTS,WORDS)
    extend_lessons()
