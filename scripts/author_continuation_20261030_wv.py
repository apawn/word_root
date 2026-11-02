"""Everyday comparison of feelings, temperature, distance and cleanliness."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'B3186':dict(words=['happy','happier','happiest'],label='happy → happier → happiest：更开心、最开心',note='happy 与 hap 运气词族相连，较早有幸运义；现代比较形式把 y 变 i，不能把所有派生都硬译成幸运。'),
 'B3656':dict(words=['sad','sadder','saddest'],label='sad → sadder → saddest：更难过、最难过',note='sad 接古英语 sæd 饱足、厌倦等旧材料，后来有沉实、严肃、悲伤等用法，中间过渡有不同解释。'),
 'B2671':dict(words=['cold','colder','coldest'],label='cold → colder → coldest：温度低与态度冷淡',note='cold 继承古英语 cald、ċeald 等；现代比较形式可比温度，也可比态度是否冷淡。'),
 'B2673':dict(words=['warm','warmer','warmest'],label='warm → warmer → warmest：最暖和、最热情',note='warm 的本族温度义与亲切、友好等比喻相连；warmest 可用于问候等礼貌表达。'),
 'B2675':dict(words=['cool','cooler','coolest'],label='cool → cooler → coolest：最凉、最冷静、最酷',note='cool 的温度、情绪用法较早已有，赞许义后来广泛传播；cooler 的容器名词与比较级不能混作一个意思。'),
 'C0232':dict(words=['close','closer','closest'],label='close → closer → closest：距离、关系与接近程度',note='接近的 close 读 /s/，closest 保留 /s/；关上动词 close 读 /z/，不是最高级的基词义。'),
 'B3030':dict(words=['clean','cleaner','cleanest'],label='clean → cleaner → cleanest：最干净、最利落',note='clean 接古英语 clǣne，最高级按洁净、整齐、无杂乱等具体语境使用。'),
}
W('happier','英 /ˈhæpiə/；美 /ˈhæpiər/','更开心、满意、安心的；happy 的比较级',
 '心里比刚才更舒展、更满意，就是 happier。它可以比较情绪，也可以表示对某个安排更放心、更愿意接受。',
 'happy 变 y 为 i 加 -er。happy 较早有幸运义，联系 hap 运气和相关北欧材料，后来开心、满意的用法常见；具体更早形成有不同分析。',
 [['中古英语 happy 及 hap 等相关材料','幸运、顺遂 → 开心、满意等'],['happy 变 y 为 i + -er → happier','更开心、更满意等']],
 'feel happier 更开心；happier with the result 对结果更满意；happier about ... 对……更放心；much happier 开心多了。',
 'a happier time；happier than before。','happier 不一定是更兴奋，可能是更满意、更安心。I’d be happier if ... 常委婉说怎样做会让我更放心、满意。',
 ('She felt happier after talking to her friend.','和朋友聊过后，她心情好一些了。'),('I would be happier if we checked the address before leaving.','出发前核对一下地址，我会更放心。'),sources=['https://en.wiktionary.org/wiki/happier#English','https://en.wiktionary.org/wiki/happy#English'])
W('happiest','/ˈhæpiɪst/','最开心的；最满意、最舒心的；happy 的最高级',
 '在几段时光、几种处境里，心里最满足、最舒展的一种，是 happiest。它也能用来强调某个时刻特别快乐。',
 'happy 变 y 为 i 加 -est，常读三个音节。词基 happy 与中古英语幸运、顺遂词族相关，现代最高级主要按开心、满意等常用义理解。',
 [['中古英语 happy 及相关运气词族 → happy','幸运、顺遂；后来开心、满意'],['happy 变 y 为 i + -est → happiest','最开心；最满意等']],
 'the happiest day 最开心的一天；at her happiest 她最舒心的时候；the happiest memories 最美好的快乐回忆。',
 'one of my happiest days；happiest when ...。','She is happiest when gardening 说她做园艺时最舒心，不一定是在把她和所有人排名。最高级的比较范围可以是同一个人的不同处境。',
 ('He is happiest when working in the garden.','在花园里干活时，他最开心。'),('That afternoon became one of our happiest memories.','那个下午成了我们最快乐的回忆之一。'),sources=['https://en.wiktionary.org/wiki/happiest#English','https://en.wiktionary.org/wiki/happy#English'])
W('sadder','英 /ˈsædə/；美 /ˈsædər/','更难过的；更令人伤感的；sad 的比较级',
 '人心里更难受，或一个故事比另一个更让人伤感，都可以说 sadder。先看形容的是人的感受，还是引起感受的内容。',
 'sad 双写末尾 d，加 -er。sad 继承古英语 sæd，早有饱足、厌倦等义，后来出现沉实、严肃、悲伤等用法，具体语义过渡有不同解释。',
 [['古英语 sæd → 中古英语 sad → sad','饱足、沉实等旧义；后来有悲伤义'],['sad 双写 d + -er → sadder','更难过；内容更令人伤感']],
 'feel sadder 更难过；a sadder story 更令人伤感的故事；sadder than before 比以前更难过。',
 'a sadder ending；sadder after the news。','sadder 不只形容人，a sadder ending 可以说更令人伤感的结局。sad 侧重难过，worried 更侧重担心某事；感受的重点不同。',
 ('The ending was sadder than I expected.','这个结局比我预想的更令人伤感。'),('He felt sadder when he saw the empty room.','看见空荡荡的房间时，他更难过了。'),sources=['https://en.wiktionary.org/wiki/sadder#English','https://en.wiktionary.org/wiki/sad#English'])
W('saddest','/ˈsædɪst/','最难过的；最令人伤感、遗憾的；sad 的最高级',
 '在一组经历、故事或细节里，让人最难过的一项，是 saddest。说 the saddest part，常是在点出最令人遗憾的一环。',
 'sad 双写 d 加 -est，词尾 /ɪst/。sad 从古英语 sæd 等形式延续，其现代悲伤义成为最高级主要使用的一支。',
 [['古英语 sæd → sad','饱足、沉实等旧义与后来的悲伤义'],['sad 双写 d + -est → saddest','最难过；最令人伤感、遗憾']],
 'the saddest moment 最难过的时刻；the saddest part 最令人遗憾的部分；the saddest story 最伤感的故事。',
 'one of the saddest days；the saddest thing about ...。','the saddest part 常指出整件事中最令人遗憾的细节。人、故事、情境都可以成为 sad 的描述对象，具体是谁感到难过，靠语境判断。',
 ('The saddest part was that they never had a chance to say goodbye.','最令人难过的是，他们始终没机会道别。'),('It was the saddest story in the collection.','这是那本故事集里最伤感的故事。'),sources=['https://en.wiktionary.org/wiki/saddest#English','https://en.wiktionary.org/wiki/sad#English'])
W('colder','英 /ˈkəʊldə/；美 /ˈkoʊldər/','更冷的；态度更冷淡的；cold 的比较级',
 '温度再低一些，是 colder；人对你的反应更疏远，也可以借冷的感觉来描述。',
 'cold + -er，直接加，不双写 d。cold 继承古英语 cald、ċeald 等，经中古英语延续；现代比较形式主要按温度、态度等形容词义使用。',
 [['古英语 cald／ċeald → cold','冷；态度疏远等引申'],['cold + -er → colder','温度更低；态度更冷淡']],
 'colder weather 更冷的天气；colder water 更冷的水；a colder reply 更冷淡的答复；getting colder 越来越冷。',
 'much colder；colder than yesterday。','colder 说冷的程度，a worse cold 常是在说感冒更严重。形容词 cold 与疾病名词 a cold 在句中功能不同，不能把 colder 一律当病情比较。',
 ('The room became colder after the sun went down.','太阳下山后，房间更冷了。'),('Her reply was colder than I had expected.','她的答复比我预想的冷淡。'),sources=['https://en.wiktionary.org/wiki/colder#English','https://en.wiktionary.org/wiki/cold#English'])
W('coldest','英 /ˈkəʊldɪst/；美 /ˈkoʊldɪst/','最冷的；态度最冷淡的；cold 的最高级',
 '温度最低的一段时间、一个地方，是 coldest；人的答复最缺乏热情，也可以用它表达冷淡。',
 'cold + -est，/d/ 后接 /ɪst/。cold 延续古英语 cald、ċeald 等形式，现代最高级沿温度与相应比喻义使用。',
 [['古英语 cald／ċeald → cold','冷；疏远、不热情等引申'],['cold + -est → coldest','所比范围里最冷、最冷淡']],
 'the coldest day 最冷的一天；the coldest room 最冷的房间；the coldest reply 最冷淡的答复；at its coldest 在最冷时。',
 'the coldest part of winter；the coldest of the rooms。','coldest month 比较月里的温度情况，coldest reply 比较答复的情感温度。知道对象后，才好把冷译成低温还是冷淡。',
 ('The kitchen was the coldest room in the house.','厨房是整栋房子里最冷的房间。'),('We stayed indoors during the coldest part of the week.','一周里最冷的那段时间，我们待在室内。'),sources=['https://en.wiktionary.org/wiki/coldest#English','https://en.wiktionary.org/wiki/cold#English'])
W('warmest','英 /ˈwɔːmɪst/；美 /ˈwɔːrmɪst/','最暖和的；最热情、最亲切的；warm 的最高级',
 '温度最让人感觉暖，是 warmest；接待、问候让人最感到亲近，也能借温暖来表达。',
 'warm + -est，词尾 /ɪst/。warm 继承古英语 warm 等本族形式，温度与友好情感的关联在现代最高级中并用。',
 [['古英语 warm 及相关本族形式 → warm','温暖；亲切、友好等引申'],['warm + -est → warmest','所比范围里最暖；问候等极热情、亲切']],
 'the warmest room 最暖的房间；the warmest welcome 最热情的欢迎；warmest wishes 最诚挚的祝愿；warmest regards 最亲切的问候。',
 'the warmest part of the day；our warmest thanks。','warmest regards、warmest wishes 常是礼貌表达里的加强语气，不一定是在把几份问候作精确排名。warmest room 则通常是在比较实际温度。',
 ('We put the chairs in the warmest part of the room.','我们把椅子放在房间最暖和的地方。'),('They gave us the warmest welcome we could have hoped for.','他们给予了我们所能期待的最热情的欢迎。'),sources=['https://en.wiktionary.org/wiki/warmest#English','https://en.wiktionary.org/wiki/warm#English'])
W('coolest','/ˈkuːlɪst/','最凉爽的；最冷静的；最酷、最棒的〔口语〕；cool 的最高级',
 '温度最清凉，或人在压力下最镇定，是 coolest；口语里赞东西最酷、最棒，又是后来常见的赞许用法。',
 'cool + -est，词尾 /ɪst/。cool 继承古英语 cōl 等温度词，情绪平静用法也较早；赞许义后来广泛传播，分别按场景理解。',
 [['古英语 cōl 等 → cool','凉；情绪冷静等较早用法'],['cool + -est → coolest','最凉、最冷静；另按口语赞许义说最酷']],
 'the coolest room 最凉爽的房间；the coolest person under pressure 压力下最镇定的人；the coolest idea 最酷的点子。',
 'the coolest part of the house；one of the coolest things。','coolest 不总比温度。That is the coolest thing! 常是在赞叹太酷、太棒；The coolest room is downstairs 则通常是在说房间凉爽。',
 ('The shaded terrace is the coolest place to sit in the afternoon.','下午坐着休息，阴凉露台最凉爽。'),('That is one of the coolest ideas I have heard all week.','这是我这周听过最棒的点子之一。'),sources=['https://en.wiktionary.org/wiki/coolest#English','https://en.wiktionary.org/wiki/cool#English'])
W('closest','英 /ˈkləʊsɪst/；美 /ˈkloʊsɪst/','最近的；关系最亲近的；最接近的；close 的最高级',
 '两者之间的空隙最小，是 closest：可以是实际距离，也可以是关系、结果与目标之间的差距。',
 '接近的形容词 close 去末尾 e，加完整最高级 -est；这里 s 读 /s/，和关上动词 close 的 /z/ 分开。历史经法语 clos 接拉丁 clausus 关着、围住的材料，发展出紧贴、接近等义。',
 [['拉丁 clausus → 法语 clos → 形容词 close','关着、紧密 → 接近、亲密等'],['close 去 e + -est → closest','距离、关系、接近程度的最高级']],
 'the closest station 最近的车站；my closest friend 我最亲近的朋友；the closest match 最接近的匹配；closest to ... 最接近……。',
 'the closest of the options；our closest neighbour。','closest 的 close 读 /s/，closed 的关上动词词干读 /z/。closest friend 比关系亲近，closest house 比空间距离；最近和最亲密各看场景。',
 ('Which station is closest to the museum?','哪个车站离博物馆最近？'),('She asked her closest friend to read the first draft.','她请最亲近的朋友读了初稿。'),sources=['https://en.wiktionary.org/wiki/closest#English','https://en.wiktionary.org/wiki/close#English'])
W('cleanest','/ˈkliːnɪst/','最干净的；最整洁、最利落的；clean 的最高级',
 '污物最少，是 cleanest；设计、线条没有多余杂乱，做事干脆利落，也可以用 clean 的延伸义来理解。',
 'clean + -est，词尾 /ɪst/。clean 继承古英语 clǣne 的洁净、纯净等材料，现代最高级按清洁、整齐、利落等具体语境使用。',
 [['古英语 clǣne → clean','洁净、纯净 → 整齐、利落等'],['clean + -est → cleanest','所比范围里最干净、最整洁等']],
 'the cleanest room 最干净的房间；the cleanest lines 最简洁利落的线条；the cleanest finish 最干净利落的收尾。',
 'the cleanest of the three；our cleanest design。','cleanest design 可以说视觉最简洁、无杂乱；cleanest kitchen 通常说卫生、整洁。cleaner 还可能是清洁人员或清洁用品的名词，识别词性后再理解。',
 ('This was the cleanest room we saw during the visit.','参观时我们看到的房间里，这间最干净。'),('The second design has the cleanest lines.','第二个设计的线条最简洁利落。'),sources=['https://en.wiktionary.org/wiki/cleanest#English','https://en.wiktionary.org/wiki/clean#English'])
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_wv',ROOTS,WORDS)
 extend_lessons()
