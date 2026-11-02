"""Growing, hiding, riding, singing, shaking, sleeping and swimming."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'B2873':dict(words=['grow','grew','grown'],label='grow、grew、grown：生长与逐渐变化',note='grew /ɡruː/ 是过去式，grown 是过去分词；植物长大和人、情绪逐渐变化共用该变位。'),
 'B2877':dict(words=['hide','hid','hidden'],label='hide、hid、hidden：藏起与看不见的状态',note='hide 较早属于带过去词尾的动词，不能把现代 hid、hidden 一律说成未变过的原始强变位；标准常用三式是 hide → hid → hidden。'),
 'B2960':dict(words=['ride','rode','ridden'],label='ride、rode、ridden：骑乘的三种形式',note='rode 是过去式；ridden 是过去分词。'),
 'B2750':dict(words=['sing','sang','sung'],label='sing、sang、sung 连着读',note='sing /sɪŋ/ → sang /sæŋ/ → sung /sʌŋ/，过去、分词的元音不同，常见读音词尾不额外加 /ɡ/。'),
 'B2969':dict(words=['shake','shook','shaken'],label='shake、shook、shaken：摇动与内心震动',note='shook 是过去式，shaken 是过去分词；shaken 作状态形容词时还常指受到惊吓、心绪不宁。'),
 'B2954':dict(words=['sleep','slept'],label='sleep 与 slept：过去、完成的睡眠',note='sleep → slept → slept，现代过去与分词同形；不能只凭词尾 t 把 sleep 的全部旧变位历史说成和 keep 完全相同。'),
 'B2997':dict(words=['swim','swam','swum'],label='swim、swam、swum 连着读',note='swam /swæm/ 是过去式，swum /swʌm/ 是过去分词；与 sing、sang、sung 对照记，但不把相似读音当所有动词的通用造词规则。'),
}
W('grew','/ɡruː/','长大了、增长了、逐渐变得；grow 的过去式',
 '植物往上长，人逐渐成熟，声音、担忧慢慢增强，都可以用 grew。它常比突然 changed 更有逐渐发展的感觉。',
 '接古英语 growan 的过去式 greow，经中古英语 grew 等延续。由植物生长的旧词族，扩展到人、数量和状态变化。',
 [['古英语 growan、greow → 中古英语相关形式','生长、增大及相应过去形式'],['现代 grow → grew → grown','过去 grew；过去分词 grown']],
 'grew taller 长高了；grew up 长大；grew quiet 逐渐安静；grew more confident 越来越自信。',
 'grew rapidly；grew tired of something。','grew 是过去式，grown 是过去分词。grew 加形容词常强调逐渐进入某状态，不必真涉及身体长高。',
 ('The little tree grew quickly that summer.','那棵小树那年夏天长得很快。'),('She grew more confident with practice.','随着练习，她越来越自信。'),sources=['https://www.etymonline.com/word/grow','https://en.wiktionary.org/wiki/grew#English'])
W('hid','/hɪd/','藏了、躲起来了；hide 的过去式',
 '把东西放到不容易被发现的地方，或让自己不被看见。过去发生的藏、躲，用 hid。',
 'hide 接古英语 hydan 等遮藏词族，较早是带过去词尾的动词；hid 由旧过去形式经历缩短、语音变化而来，现代常见分词则是 hidden。',
 [['较早 hide 的遮藏动词与过去形式','使某物、自己不被发现'],['现代 hide → hid → hidden','过去 hid；常见过去分词 hidden']],
 'hid the key 藏起钥匙；hid behind the door 躲到门后；hid her disappointment 掩饰失望。',
 'hid from view；hid a smile。','hid 可以及物也可以不及物：She hid the box 藏箱子；She hid behind it 躲到它后面。现代常见完成表达用 has hidden。',
 ('He hid the key under a flowerpot.','他把钥匙藏在花盆下面。'),('The children hid behind the sofa.','孩子们躲在沙发后面。'),sources=['https://www.etymonline.com/word/hide','https://en.wiktionary.org/wiki/hid#English'])
W('rode','英 /rəʊd/；美 /roʊd/','骑了、乘坐了；ride 的过去式',
 '人坐在马上、自行车上或某种交通工具里移动，这次骑乘发生在过去，就用 rode。',
 '接古英语 ridan 的过去式 rad 等旧强变位形式，经中古英语与后续元音变化成为 rode。',
 [['古英语 ridan、rad 等','骑乘、被载着移动及相应过去'],['现代 ride → rode → ridden','过去 rode；过去分词 ridden']],
 'rode a bike 骑了自行车；rode a horse 骑马了；rode on the bus 乘公共汽车了；rode through the village 骑行穿村。',
 'rode home；rode along the river。','rode 与 road 道路在常见口音中同音，但拼写、语法角色不同。一般过去 rode，完成结构常用 have ridden。',
 ('We rode our bikes along the river.','我们沿河骑自行车。'),('She rode a horse for the first time yesterday.','她昨天第一次骑了马。'),sources=['https://www.etymonline.com/word/ride','https://en.wiktionary.org/wiki/rode#English'])
W('sang','/sæŋ/','唱了、鸣唱了；sing 的过去式',
 '人的歌声、鸟的鸣唱在过去响起，用 sang。它只改变时间，唱的对象和方式继续由搭配说明。',
 '接古英语 singan 的过去式 sang 等旧形式，强变位词干的元音变化延续为现代 sing、sang、sung。',
 [['古英语 singan、sang、sungen 等','唱及相应过去、分词形式'],['现代 sing → sang → sung','一般过去 sang；过去分词 sung']],
 'sang a song 唱了首歌；sang softly 轻声唱；birds sang 鸟儿鸣唱；sang together 一起唱了歌。',
 'sang in the choir；sang along。','sang 是一般过去，sung 是过去分词：She sang yesterday；She has sung here before。注意 /æ/ 与 /ʌ/ 的区别。',
 ('She sang a quiet song to the baby.','她给婴儿轻声唱了一首歌。'),('The birds sang outside our window.','鸟儿在窗外鸣唱。'),sources=['https://www.etymonline.com/word/sing','https://en.wiktionary.org/wiki/sang#English'])
W('sung','/sʌŋ/','唱过、被演唱的；sing 的过去分词',
 'has sung 是已经唱过，was sung 是被演唱。sung 把唱的动作放进完成或被动结构。',
 '接 sing 的旧分词材料，古英语有 sungen 等，现代缩短为 sung。与过去式 sang 的元音不同。',
 [['古英语 sing 词族的分词 sungen 等','已进行、被进行的歌唱'],['现代 sing → sang → sung','sung 用在完成、被动等结构中']],
 'has sung before 以前唱过；a song sung by children 孩子们演唱的歌；beautifully sung 唱得很美的。',
 'sung in English；have never sung on stage。','sang 可以独立作一般过去谓语，sung 通常配合 have、be 等，或作分词修饰语；不是只看意思都叫唱了就能互换。',
 ('The song was sung by a children’s choir.','这首歌由一个儿童合唱团演唱。'),('I have never sung on stage before.','我以前从未在舞台上唱过歌。'),sources=['https://www.etymonline.com/word/sing','https://en.wiktionary.org/wiki/sung#English'])
W('shook','/ʃʊk/','摇了、抖了、震动了；shake 的过去式',
 '把瓶子晃一晃，头左右摇一下，或消息让人的信心动摇，都能接到 shake 的过去形式 shook。',
 'shake 接古英语 sceacan 来回移动、颤动，其过去式有 scoc 等；经过中古英语形式和元音变化延续为 shook。',
 [['古英语 sceacan、scoc 等','摇动、颤抖及相应过去形式'],['现代 shake → shook → shaken','过去 shook；过去分词 shaken']],
 'shook the bottle 摇了瓶子；shook his head 摇了摇头；shook hands 握了手；shook their confidence 动摇了他们的信心。',
 'shook with laughter；shook the dust off。','shook 的 oo 读 /ʊ/；shake 的过去分词是 shaken。过去 shook hands 说握手，shook his head 常说否定、惊讶等摇头动作。',
 ('She shook her head and smiled.','她摇摇头，笑了。'),('The loud noise shook the windows.','巨大的声响震得窗户晃动。'),sources=['https://www.etymonline.com/word/shake','https://en.wiktionary.org/wiki/shook#English'])
W('shaken','/ˈʃeɪkən/','被摇动的；受惊、心绪不宁的；shake 的过去分词',
 '东西被摇过，人的心也可能被一件事震得不稳。He looked shaken 常说他受到冲击，还没缓过来。',
 '接 shake 的旧分词材料，古英语有 scacen 等；现代 shaken 保留 -en。物理上的摇动、不稳又用于心理状态。',
 [['shake 词族的旧分词 → shaken','已经被摇动、使不稳定'],['shaken 的心理状态义','受到惊吓、打击后心绪不宁']],
 'a shaken bottle 摇过的瓶子；visibly shaken 明显受惊的；deeply shaken 深受震动；shaken confidence 动摇的信心。',
 'shaken by the news；shaken but unhurt。','shaken 可说受到一次事件的冲击；shaky 更常说发抖、不稳或缺乏把握的状态。两者相近，但不是同一个词形。',
 ('The dressing should be shaken before serving.','这份沙拉酱上桌前应摇匀。'),('He looked shaken after hearing the news.','听到消息后，他显得深受震动。'),sources=['https://www.etymonline.com/word/shake','https://en.wiktionary.org/wiki/shaken#English'])
W('slept','/slept/','睡了、睡过；sleep 的过去式、过去分词',
 '睡眠发生在过去，或说已经睡过，用 slept。它还能与搭配一起说睡过头、睡得好不好。',
 'sleep 接古英语 slæpan 等睡眠词族，较早过去、分词形式与现代不同；后续元音和过去尾变化形成 slept，现代过去与分词采用同形。',
 [['古英语 slæpan 及较早变位形式','睡、入睡、休眠'],['现代 sleep → slept → slept','过去与过去分词同形，长元音变短']],
 'slept well 睡得好；slept badly 睡得差；slept through the alarm 闹钟响了也没醒；slept in 睡懒觉。',
 'have slept enough；slept until noon。','slept 说睡觉这个过程，asleep 说睡着的状态：He slept；He was asleep。slept 不能直接当作普通形容词代替 asleep。',
 ('I slept well last night.','我昨晚睡得很好。'),('She slept through the noise.','她在那阵噪声中仍睡着，没有醒来。'),sources=['https://www.etymonline.com/word/slept','https://en.wiktionary.org/wiki/slept#English'])
W('swam','/swæm/','游泳了、游过了；swim 的过去式',
 '过去在水里游动，或游过一段距离，用 swam。人、鱼等都可以作主语。',
 '接古英语 swimman 的过去式 swamm 等，沿用旧强变位中以元音变化区分过去的形式。',
 [['古英语 swimman、swamm、swummen 等','水中移动及其过去、分词形式'],['现代 swim → swam → swum','过去 swam；过去分词 swum']],
 'swam across the river 游过河；swam in the pool 在池里游泳了；swam towards the boat 向船游去。',
 'swam for an hour；swam back to shore。','一般过去 swam，完成结构通常用 have swum。与 sing、sang、sung 一起读，容易听清 /ɪ/、/æ/、/ʌ/ 的分工。',
 ('We swam in the lake that afternoon.','那天下午，我们在湖里游了泳。'),('The fish swam under the bridge.','鱼游到了桥下。'),sources=['https://www.etymonline.com/word/swim','https://en.wiktionary.org/wiki/swam#English'])
W('swum','/swʌm/','游过、已经游泳；swim 的过去分词',
 '跟 have、has、had 连着，用来讲已经游过的距离、经历。swum 不是普通的一般过去拼写。',
 '接 swim 旧分词 swummen 等材料，现代词尾缩短为 swum；与过去式 swam 仍保留元音区别。',
 [['古英语 swim 词族的旧分词材料','已完成的游动、游泳'],['现代 swim → swam → swum','swum 主要进入完成结构等']],
 'has swum a long way 已游了很远；have swum here before 以前在这里游过；had never swum 从未游过〔过去参照〕。',
 'swum across the bay；have just swum a kilometre。','swam /swæm/ 与 swum /swʌm/ 不只是拼写差一点。I swam yesterday；I have swum here before，两句使用的语法形式不同。',
 ('She has swum across this bay before.','她以前游过这个海湾。'),('I had never swum in the sea before that holiday.','那次假期之前，我从未在海里游过泳。'),sources=['https://www.etymonline.com/word/swim','https://en.wiktionary.org/wiki/swum#English'])
def extend_lessons():
    extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
    save('continuation_20261030_ty',ROOTS,WORDS)
    extend_lessons()
