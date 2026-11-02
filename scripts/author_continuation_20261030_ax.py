"""Handle, hurt and pull: concrete actions and their everyday extensions."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
HA=[['古英语 handlian、handle 等 → handle','用手接触、操弄；把手等相关形式'],['现代 handle','操作、处理；把手；昵称等支线']]
W('handling','/ˈhændlɪŋ/','处理、搬运；操控性能；handle 的 -ing 形式',
 '手上怎样拿、事情怎样处理、车怎样操控，重点都在实际操作这一面。',
 '现代对应 handle 去 e + -ing；活动名词也有古英语 handlung、中古英语 handlinge 等旧形，不是刚由现代 handle 造出。',HA+[['古英语 handlung → handling','操作、处理的活动；现代对应 handle + -ing']],
 'careful handling 小心搬运，handling complaints 处理投诉，a car’s handling 汽车操控性能，shipping and handling 运费及处理费用。',
 'careful handling；handling complaints；shipping and handling；a car’s handling。',
 'handling 操作、处理，handle 可把手或处理动词；handling fee 是处理费用，不是买门把手的价格。',
 ('The glass requires careful handling.','这块玻璃需要小心搬运。'),('The review praised the car’s handling.','评测称赞了这辆车的操控表现。'))
W('handler','英 /ˈhændlə/；美 /ˈhændlər/','处理者；动物训练、控制人员；处理程序',
 '负责接住、控制某个对象的人或程序：牵犬的人，响应事件的软件代码都可以。',
 'handle + -er，中古英语已有对应人物词。计算机处理程序是后来按执行处理的角色命名。',HA+[['handle + -er → handler','处理、控制者；后有程序处理器用法']],
 'a dog handler 训犬、带犬人员，a baggage handler 行李搬运员，an event handler 事件处理程序。',
 'a dog handler；a baggage handler；an event handler。',
 'handler 执行处理的人、代码，handling 过程或性能；event handler 不是举办活动的主持人这个固定译法。',
 ('The dog waited for a signal from its handler.','狗等着带犬人员发出信号。'),('The event handler saves the user’s changes.','事件处理程序保存用户的更改。'))
W('panhandle','/ˈpænhændl/','锅柄；狭长突出地带〔美式〕；街头乞讨〔动词〕',
 '地图上一块土地细长地伸出去，像锅伸出一个柄；街头讨钱则是这个词另一个常见用法。',
 '地形名词由 pan 锅 + handle 柄，形象很清楚。乞讨义的具体动机有不同解释，可能联系伸出的手臂或讨钱器皿；动词有从相关名词形成、由 panhandler 逆构等分析，不强行定一说。',
 HA[:1]+[['pan + handle → panhandle〔名词〕','锅柄；像柄一样突出的狭长土地'],['另有乞讨名词、人物词及 panhandle 动词','具体动机、形成先后有不同分析']],
 'the Florida Panhandle 佛罗里达州狭长突出地区；panhandle on the street 在街头乞讨。',
 'the Florida Panhandle；a narrow panhandle；panhandle on the street。',
 'panhandle 地形义不是 pan 全部 + handle 处理；乞讨义也别编成必须真举着平底锅才成立。',
 ('They drove west through the Florida Panhandle.','他们向西开车穿过佛罗里达州的狭长突出地区。'),('The novel describes a man who panhandles near the station.','小说描写一个在车站附近乞讨的人。'),sources=['https://www.etymonline.com/word/panhandle','https://en.wiktionary.org/wiki/panhandle#English'])
R('B3129','用手操作到处理；执行者与外形组合','HANDLE：能用手抓的把手，也能把事情接住处理','既有 handle 先读，再 handling、handler；handlebar、manhandle 共享；panhandle 地形与乞讨两路分讲。',
 'handle 不是每个句子都用手触摸。软件 handler 按处理角色命名；地图 panhandle 按锅柄形状。',
 'handle + -ing/-er；pan + handle；handle + bar；man + handle。',
 [['基本词、活动与执行者','handle · handling · handler'],['身体操控及外形','handlebar · manhandle · panhandle']],
 'handling fee 处理费，event handler 事件处理代码；panhandle 不是泛欧洲 pan-；乞讨来源保留不确定。',
 'The handler checked the equipment before handling the dog.\n\n带犬人员控制犬只前检查了装备。',
 'handle handling handler handlebar manhandle panhandle')
HU=[['古北部法语 hurter 等 → 中古英语 hurten → hurt','撞击、碰撞；伤害；直接来源、远源仍有争议'],['现代 hurt','伤害、受伤；疼；感情受伤']]
def H(f,m):return HU+[[f,m]]
W('hurt','英 /hɜːt/；美 /hɜːrt/','使受伤、伤害；疼；受伤、难过的',
 '身体碰伤会疼，一句话也能让心里疼；对人是伤害，对部位可说它在痛。',
 '中古英语 hurten 与古法语 hurter 撞击等相关，是否还有本族来源影响有不同看法。过去式、分词都是 hurt，不加 hurted。',HU,
 'hurt your ankle 伤到脚踝，My back hurts. 我背疼，hurt someone’s feelings 伤感情，feel hurt 心里受伤。',
 'hurt your ankle；my back hurts；hurt someone’s feelings；feel hurt。',
 'hurt 可感到疼或造成伤害；injure 常强调造成身体损伤，ache 常是持续隐痛。hurt—hurt—hurt 词形不变。',
 ('My shoulder hurts when I lift my arm.','我抬胳膊时肩膀会疼。'),('I did not mean to hurt your feelings.','我不是有意伤害你的感情。'))
W('hurtful','英 /ˈhɜːtfəl/；美 /ˈhɜːrtfəl/','伤人的；让人难受的',
 '一句话戳中别人痛处，或一个举动让人心里受伤；强调造成伤害的效果。',
 'hurt + -ful，含造成伤害的性质。不是受伤的人已经充满疼痛这个分词状态。',H('hurt + -ful → hurtful','容易造成伤害，尤其言语、行为伤人'),
 'hurtful comments 伤人评论，hurtful words 伤人的话，find something hurtful 觉得某事很伤人。',
 'hurtful comments；hurtful words；find it hurtful。',
 'hurtful 常说言语、态度伤人，harmful 范围更广，可损害健康、环境等。两者有重合，不能所有伤害都只选一词。',
 ('The comment was unnecessary and hurtful.','那句话既没必要，又伤人。'),('She found his silence more hurtful than an argument.','她觉得他的沉默比争吵更伤人。'))
W('unhurt','英 /ʌnˈhɜːt/；美 /ʌnˈhɜːrt/','未受伤的；安然无恙的',
 '事情发生了，但人没受伤；不等于整个事件没有造成任何损失。',
 'un- 否定 + hurt 受伤的，中古英语已有 unhert 等形式。',H('un- + hurt → unhurt','没有受伤的'),
 'escape unhurt 没受伤地脱身，remain unhurt 仍然安然无恙。',
 'escape unhurt；remain unhurt；fortunately unhurt。',
 'unhurt 无伤，safe 安全或已脱险；身处安全处的人可能此前受过伤，两个描述着眼不同。',
 ('All the passengers escaped unhurt.','所有乘客都安然无恙地脱身。'),('The driver was shaken but unhurt.','司机受了惊吓，但没有受伤。'))
W('hurtle','英 /ˈhɜːtl/；美 /ˈhɜːrtl/','飞驰、猛冲；猛烈碰撞〔旧义或特定用法〕',
 '速度快得像刹不住，一下冲过去；今天不必真撞上，也可以说 hurtle。',
 '中古英语 hurtelen，通常分析为 hurt 的旧撞击义 + 反复、强化动作后缀 -le。不是 hurt + little，也不是先受伤才会跑得快。',HU[:1]+[['中古英语 hurtelen → hurtle','猛烈碰撞、冲撞 → 高速猛冲、飞驰']],
 'hurtle down the road 沿路飞驰，hurtle towards 冲向，hurtle through space 在太空飞驰。',
 'hurtle down；hurtle towards；hurtle through space。',
 'hurtle 常说主体高速冲行，hurl 常说把东西用力扔出去；二者历史上有接近、混淆，但现代句式不能随意互换。',
 ('A truck hurtled past us on the narrow road.','一辆卡车在窄路上从我们身边飞驰而过。'),('The spacecraft hurtled through space.','航天器在太空中飞驰。'),sources=['https://www.etymonline.com/word/hurtle','https://en.wiktionary.org/wiki/hurtle#English'])
W('butthurt','英 /ˈbʌthɜːt/；美 /ˈbʌthɜːrt/','因受冒犯而恼羞、耿耿于怀的〔粗俗、嘲讽〕',
 '网络争吵里嘲笑别人被戳痛了、太玻璃心；通常是在贬低对方反应，不是体贴表达他的难过。',
 'butt 臀部 + hurt 受伤，粗俗比喻转为因冒犯而恼怒、不满的网络俚语。不要根据字面编出某种唯一具体性行为来源。',H('butt + hurt → butthurt','粗俗的受伤形象 → 嘲讽对冒犯反应强烈'),
 'get butthurt 因受冒犯而恼火，butthurt about a comment 对评论耿耿于怀。工作、礼貌交流中通常不合适。',
 'get butthurt；butthurt about；sound butthurt。',
 'hurt 可以真诚说受伤难过，butthurt 通常带嘲讽、粗俗评价；两者语气远不一样。',
 ('The post used the word butthurt to mock angry replies.','帖子用 butthurt 这个词嘲讽愤怒的回复。'),('Calling someone butthurt can make the argument worse.','说别人 butthurt 可能让争吵更严重。'))
R('B2880','撞击、伤害与疼；伤人、无伤和高速冲行','HURT：身体疼、心里疼；hurtle 留着旧碰撞支线','hurt → hurtful、unhurt；hurtle 从旧撞击义讲高速冲行，butthurt 最后注明粗俗网络语气。',
 '现代 hurt 的身体和感情两路都常用。hurtle 不是无关拼写巧合，但要接旧义，不能从今天疼的感觉硬推高速。',
 'hurt—hurt—hurt；hurt + -ful；un- + hurt；旧 hurt + -le；butt + hurt。',
 [['疼痛、伤害与无伤','hurt · hurtful · unhurt'],['旧动作与俚语','hurtle · butthurt']],
 'hurtful 伤人、hurt 受伤；unhurt 未受伤不等于无事故；hurtle 猛冲、hurl 扔；butthurt 语气粗俗嘲讽。',
 'The truck hurtled past, but fortunately everyone remained unhurt.\n\n卡车飞驰而过，所幸大家都没受伤。',
 'hurt hurtful unhurt hurtle butthurt')
PU=[['古英语 pullian → 中古英语 pullen → pull','拉、拔、扯；更远来源不明'],['现代 pull','拉、拖；拉力；吸引、影响等引申']]
def P(f,m):return PU+[[f,m]]
W('pull','/pʊl/','拉、拖、拔；拉力；吸引力、影响力',
 '抓住一端往自己或指定方向带；抽象里也可说某种魅力把你吸过去。',
 '继承古英语 pullian，更远来源不确定。名词拉、牵引力由相关动词发展，吸引、影响等借拉动的形象延伸。',PU,
 'pull the door 拉门，pull a muscle 拉伤肌肉，pull out 拔出、退出，the pull of home 家的吸引力，pull it off 成功做到。',
 'pull the door；pull a muscle；pull out；pull it off。',
 'pull 拉向某处，push 向外或另一方向推；pull the door 与 push the door 操作相反。pull it off 是成功完成的固定说法。',
 ('Pull the handle towards you.','把把手朝你这边拉。'),('Nobody thought we could finish, but we pulled it off.','没人觉得我们能完成，但我们做到了。'))
W('pulling','/ˈpʊlɪŋ/','拉、拖、牵引；pull 的 -ing 形式',
 '把拉的动作当作一段活动或持续过程；不是看到 -ing 就一定另有一个陌生词根。',
 'pull + -ing，中古英语已有 pulling、pullyng 等活动名词。pull 为双 l 结尾，直接接 -ing，不再多加一个 l。',P('pull + -ing → pulling','拉、拖的动作；相关分词用法'),
 'pulling power 拉力，也可吸引人的能力；keep pulling 继续拉。',
 'pulling power；keep pulling；pulling the rope。',
 'pulling 活动或分词，puller 执行者、拉具；pulling power 有时说吸引力，要看是发动机还是明星。',
 ('Keep pulling until the rope is tight.','继续拉，直到绳子绷紧。'),('The engine has enough pulling power for the trailer.','发动机有足够牵引力拖动挂车。'))
W('puller','英 /ˈpʊlə/；美 /ˈpʊlər/','拉的人；拉拔器、牵引工具',
 '负责把东西拉动的人或工具；技术场景里往往是帮助拔出紧配零件的器具。',
 'pull + -er，中古英语已有人物形式。现代工具名按执行拉拔动作命名，常由前置名词说明拔什么。',P('pull + -er → puller','执行拉、拔的人或器具'),
 'a gear puller 齿轮拉拔器，a nail puller 拔钉器。',
 'a gear puller；a nail puller；a cable puller。',
 'puller 拉拔工具或人，pulley 滑轮是另一词；滑轮可帮拉动，但不是 pull + -ey 形成。',
 ('The mechanic used a gear puller to remove the part.','机械师用齿轮拉拔器拆下零件。'),('A nail puller made the job easier.','拔钉器让工作轻松了些。'))
R('B3105','拉、拔、牵引与吸引；活动和工具分清','PULL：抓住往一个方向拉，也借指吸引和影响','pull → pulling → puller；固定 pull it off、pull out 直接放常见场景解释。',
 '本族旧拉动词延续，远源不强定；工具、运动和魅力比喻靠对象辨认。',
 'pull + -ing/-er；pull it off、pull out 等为常用短语。',
 [['动作、活动和器具','pull · pulling · puller']],
 'pull 拉与 push 推相反；pulling power 可拉力或吸引力；puller 不是 pulley 的简单派生。',
 'The puller has enough pulling power to remove the part.\n\n拉拔器有足够的拉力把零件拆下来。',
 'pull pulling puller')
if __name__=='__main__':save('continuation_20261030_ax',ROOTS,WORDS)
