"""Rough voices, piercing sounds and hard objects sounding together."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
def S(word,base):
 return ['https://en.wiktionary.org/wiki/'+word+'#English','https://www.etymonline.com/word/'+base]
EXISTING_ROOT_ADDITIONS={
 'A1740':dict(words=['hoarse','hoarsely','gruff','gruffly','shrill','shrilly'],label='嗓音、态度形容词加 -ly',note='hoarse、gruff、shrill 分别解释基础来源；-ly 使沙哑、粗声或尖声的特点修饰说话等动作。shrilly 的普通副词义来自 shrill + -ly。'),
 'A1839':dict(words=['hoarse','hoarseness','shrill','shrillness'],label='-ness 把沙哑、尖厉的特点整体提出来',note='hoarse、shrill 是基础形容词，hoarseness、shrillness 是相应性质名词，不从 horse 马或 thrill 兴奋推导。'),
 'A1699':dict(words=['rasp','raspy'],label='rasp 到 raspy：锉擦般粗哑的声音',note='rasp 原有刮、锉擦材料，raspy 用 -y 写有这种粗糙声音的特点；不是 raspberry 的确定反向构词。'),
 'A1697':dict(words=['clatter','clatters','clattered','clattering'],label='clatter 的旧反复动作形式',note='古英语 clatrung 动作名词提供较早证据，基础动词形式是据此推知；这里的 -er 是旧反复动作材料，不是指人的后缀。'),
 'A1760':dict(words='rasp rasps rasped rasping rattle rattles rattled rattling clatter clatters clattered clattering clang clangs clanged clanging clank clanks clanked clanking'.split(),label='刮擦、碰撞拟声动词的现代词尾',note='这些基础词各自解释来源，不因声音相似就归为同一古根。rattled、clattered、clanged 的 -ed 读 /d/，rasped、clanked 的 -ed 读 /t/。'),
}
HOARSE=[['古英语 has → 中古英语 hos、hors → hoarse','沙哑；后来 r 的出现有不同解释，不能编成已确定的一次规则变化'],['hoarse 的现代扩展','人嗓音粗哑；-ly 写说话方式，-ness 写沙哑状态']]
W('hoarse','英 /hɔːs/；美 /hɔːrs/','嗓音沙哑的、嘶哑的',
 '声音失去平滑清亮的感觉，像嗓子粗了、哑了，叫 hoarse。它描述听起来怎样，不指定是感冒、喊多了还是别的原因。',
 '承古英语 has，经中古英语 hos、hors 等到现代 hoarse；r 的历史出现不好完全解释，不能把它拆成 horse 马。',HOARSE,
 'a hoarse voice 是沙哑嗓音，go hoarse 是声音变哑，shout yourself hoarse 是喊到嗓子哑。',
 'sound hoarse 听起来嗓子哑；a hoarse whisper 沙哑的低语。',
 'hoarse 讲音色粗哑，quiet 讲音量小。人可以压低声音但仍沙哑；hoarse 和 horse 在许多口音中同音，意义分开。',
 ('Her voice was hoarse after the long rehearsal.','长时间排练后，她的声音哑了。'),('We shouted ourselves hoarse at the match.','比赛时，我们喊得嗓子都哑了。'),sources=S('hoarse','hoarse'))
W('hoarsely','英 /ˈhɔːsli/；美 /ˈhɔːrsli/','沙哑地、嘶哑地',
 '话是哑着嗓子说出来的，用 hoarsely。它不改变说了什么，只让你听到那种粗哑音色。',
 'hoarse + 副词后缀 -ly，保留 e → hoarsely；不是 hoarse 去 e 再造另一个词根。',HOARSE+[['hoarse + -ly → hoarsely','以沙哑的声音说、喊、低语']],
 'said hoarsely 是哑声说，whispered hoarsely 是用沙哑的声音低语；音量小仍可以音色粗哑。',
 'called hoarsely 嘶哑地喊；laughed hoarsely 沙哑地笑。',
 'hoarsely 侧重嗓音质感，angrily 侧重情绪。一个人可以沙哑地温柔说话，也可以沙哑地发怒。',
 ('“I need some water,” he said hoarsely.','“我需要点水。”他沙哑地说。'),('She called hoarsely from the back of the room.','她从房间后面嘶哑地喊。'),sources=S('hoarsely','hoarse'))
W('hoarseness','英 /ˈhɔːsnəs/；美 /ˈhɔːrsnəs/','嗓音沙哑、嘶哑的状态',
 '把“嗓音哑了”这件事整体提出来，就是 hoarseness。-ness 像把一个特点装进名词盒子，方便说它出现、消失或能被听出来。',
 'hoarse + 性质名词后缀 -ness，保留 e → hoarseness。基础词的 r、se 都属于既有拼写。',HOARSE+[['hoarse + -ness → hoarseness','嗓音沙哑这一状态']],
 'hoarseness in her voice 是她声音里的沙哑，the hoarseness faded 是沙哑逐渐消退；通常整体当不可数名词。',
 'slight hoarseness 轻微沙哑；notice the hoarseness 听出声音沙哑。',
 'hoarse 用来直接形容 voice、person；hoarseness 把这一特点当名词说，如 the hoarseness of his voice。',
 ('I could hear the hoarseness in his voice.','我听得出他声音里的沙哑。'),('The hoarseness faded after a quiet weekend.','安静休息了一个周末后，嗓音的沙哑减轻了。'),sources=S('hoarseness','hoarse'))
GRUFF=[['中古荷兰语或中古低地德语 grof → gruff','早期说东西粗糙、颗粒粗；更远来源有争议'],['物的粗糙 → 嗓音粗低、态度生硬','说话不柔和、短而硬；不必每次都代表恶意']]
W('gruff','/ɡrʌf/','嗓音粗低的；态度生硬的、不亲切的',
 '声音低低粗粗，回答又短又硬，像“嗯，进来”，可以叫 gruff。它既能说嗓音，也能说待人的生硬劲。',
 '来自中古荷兰语或低地德语 grof 一系“粗糙”材料，后来扩到声音、举止；不是 growl 的简写。',GRUFF,
 'a gruff voice 是粗低嗓音，a gruff reply 是生硬答复；gruff but kind 可以形容嘴上硬、心里好的样子。',
 'a gruff manner 生硬的态度；a gruff greeting 不大亲切的招呼。',
 'hoarse 常让人想到嗓音哑，gruff 还容易带粗低、生硬的态度。gruff 不必表示嗓子出了问题。',
 ('He answered in a gruff voice.','他用粗低的声音回答。'),('Despite his gruff manner, he was always willing to help.','尽管他态度生硬，却一直愿意帮忙。'),sources=S('gruff','gruff'))
W('gruffly','/ˈɡrʌfli/','粗声地、生硬地',
 '话说得短、粗、不柔和，用 gruffly。听起来有点硬，但人物心里是否友好，要看接下来的行动。',
 'gruff + 副词后缀 -ly，已有 ff 保留 → gruffly；不再额外双写 f。',GRUFF+[['gruff + -ly → gruffly','用粗低、生硬的方式说话、招呼']],
 'said gruffly 是粗声说，greeted us gruffly 是生硬地跟我们打招呼；常修饰回答、咕哝等动作。',
 'replied gruffly 生硬回答；muttered gruffly 粗声嘟囔。',
 'gruffly 不等于 loudly。一个人声音不大，也可以说得粗硬；loudly 则只把音量提出来。',
 ('“Come in,” he said gruffly.','“进来。”他粗声说。'),('She replied gruffly but held the door open for us.','她回答得生硬，却替我们扶着门。'),sources=S('gruffly','gruff'))
RASP=[['中古英语 raspen，借中古荷兰语、古法语刮擦材料 → rasp 动词','粗糙工具刮、擦、锉'],['法语 raspe → rasp 工具名；动词再有声音义','粗锉；刮擦般粗哑的响声、嗓音，名词动词借入路线要分清']]
W('rasp','英 /rɑːsp/；美 /ræsp/','锉、粗刮；发刺耳粗哑声、沙哑地说；粗锉、粗哑声',
 '想象粗锉在木头上“嚓嚓”刮，叫 rasp；把这种粗糙摩擦感借到声音里，就是粗哑、磨耳朵的声响。',
 '动词接中古英语 raspen，借中古荷兰语、古法语材料；工具名词另借法语 raspe。不能只写成现代英语动词直接造出所有名词义。',RASP,
 'rasp the wood 是粗锉木头，a rasp in his voice 是声音里的粗哑；rasp out a reply 是哑声挤出答复。',
 'a coarse rasp 一把粗锉；a harsh rasp 刺耳粗哑声。',
 'rasp、raspy 的刮擦画面有历史依据；raspberry 的更早来源有争议，不能只凭前半拼写断言树莓因像锉刀得名。',
 ('He used a rasp to smooth the wooden handle.','他用粗锉修整木柄。'),('There was a dry rasp in her voice.','她的声音里带着干涩的沙哑感。'),sources=S('rasp','rasp'))
W('rasps','英 /rɑːsps/；美 /ræsps/','粗锉、粗刮、哑声说〔第三人称单数〕；粗锉、粗哑声〔复数〕',
 '工具在表面粗粗磨过，或某个声音像刮擦一样粗哑，用 rasps；名词复数也能数几把粗锉。',
 'rasp + -s，/p/ 后读 /s/；末尾 /sps/ 连着发，不往中间插元音。',RASP+[['rasp + -s → rasps','它粗刮、粗哑响；多把粗锉、多声粗响']],
 'rasps against the frame 是擦着框发粗响，wood rasps 是木工粗锉；具体名词义要看工具还是声音。',
 'rasps out a reply 哑声挤出回答；a set of rasps 一套粗锉。',
 'rasps 突出粗糙摩擦感，rings 偏清亮、共鸣声；同为响声，听感很不同。',
 ('The loose bolt rasps against the metal frame.','松动的螺栓擦着金属框发出粗响。'),('The workshop has several rasps for shaping wood.','作坊里有几把用来修整木头的粗锉。'),sources=S('rasps','rasp'))
W('rasped','英 /rɑːspt/；美 /ræspt/','粗锉、粗刮了；粗哑地说了、响了',
 '刚才工具擦出粗声，或人哑着嗓子挤出几个字，用 rasped。粗糙、磨耳的感觉仍在。',
 'rasp + 完整 -ed，/p/ 后读 /t/，结尾 /spt/；不加成多一个音节。',RASP+[['rasp + -ed → rasped','过去粗刮、发粗声、哑声说']],
 'rasped out a warning 是沙哑地挤出警告，rasped against metal 是擦过金属、发出粗响。',
 'rasped a reply 哑声回答了；rasped against the stone 擦石头发粗响。',
 'rasped 比 said 多了刮擦般的音色；whispered 讲压低音量，两种特点可以同时出现。',
 ('“Stay back,” he rasped.','“退后。”他粗哑地说。'),('The blade rasped against the stone.','刀片擦过石头，发出粗涩的响声。'),sources=S('rasped','rasp'))
W('rasping','英 /ˈrɑːspɪŋ/；美 /ˈræspɪŋ/','正在粗刮、锉擦；声音粗哑刺耳的；粗涩响声',
 '声音像粗锉在磨东西，带沙沙、嚓嚓的粗涩感，叫 rasping。也能直接说工具正在锉擦。',
 'rasp + 完整 -ing；分词可写动作，也能作形容词写粗哑的声音，不改变基础词的拼写。',RASP+[['rasp + -ing → rasping','锉擦过程；粗涩、沙哑的声音状态']],
 'a rasping voice 是粗哑的声音，a rasping noise 是摩擦般刺耳的响声；rasping the wood 是正在粗锉木头。',
 'a dry, rasping cough 干而粗哑的咳声；rasping metal 金属的粗涩响声。',
 'rasping 与 raspy 都能形容声音；rasping 保留明显的摩擦、正在响的感觉，raspy 更直接说声音具有这种特点。',
 ('He spoke in a low, rasping voice.','他说话声音低低的，粗哑磨耳。'),('A rasping noise came from the old fan.','旧风扇里传来一阵粗涩的响声。'),sources=S('rasping','rasp'))
W('raspy','英 /ˈrɑːspi/；美 /ˈræspi/','嗓音粗哑的；刺耳粗涩的',
 '声音像表面不光滑，带粗粗、沙沙的摩擦感，叫 raspy。形容歌声时也可以是独特音色，不一定在批评。',
 'rasp + 形容词后缀 -y，直接相接；从刮擦、粗哑声材料变成“声音有这种特点”。',RASP+[['rasp + -y → raspy','带粗哑、摩擦声特点的']],
 'a raspy voice 是粗哑嗓音，raspy singing 是带沙哑摩擦感的歌声；可以是天生音色或一时声音状态。',
 'a deep, raspy voice 低沉粗哑的嗓音；sound raspy 听起来粗哑。',
 'raspy、hoarse 很接近；raspy 更容易让人想到刮擦的质感，hoarse 常说嗓音哑了，边界并不绝对。',
 ('The singer has a warm, raspy voice.','这位歌手的嗓音温暖，带一点沙哑摩擦感。'),('My voice sounded raspy after all that shouting.','喊了那么久，我的声音听着有些粗哑。'),sources=S('raspy','rasp'))
SHRILL=[['中古英语 schrylle 及相应旧叫喊材料 → shrill','尖高、穿耳；大概拟声，可能联系古英语 scralletan'],['现代声音形容词及比喻','尖厉；话语、批评有尖锐、激烈或刺耳的感觉']]
W('shrill','/ʃrɪl/','尖高刺耳的、尖厉的；尖锐激烈的',
 '声音高得像细针扎进耳朵，叫 shrill。它不只是“响”，而是又高又尖、容易让人觉得刺耳。',
 '接中古英语 schrylle，可能与古英语 scralletan 等叫喊材料相关，大概拟声；不是 thrill 兴奋去掉 t 的形式。',SHRILL,
 'a shrill whistle 是尖厉哨声，shrill criticism 是尖锐、激烈的批评；后者把听感借给说话态度。',
 'a shrill voice 尖厉嗓音；a shrill alarm 刺耳的警报。',
 'high 描述音调高，可以中性；shrill 常多了刺耳的评价。loud 讲音量，低沉的声响也能很 loud。',
 ('A shrill whistle cut through the noise.','一声尖厉的哨响穿过喧闹声。'),('The debate became increasingly shrill.','辩论的语气越来越尖锐刺耳。'),sources=S('shrill','shrill'))
W('shrilly','/ˈʃrɪli/','尖声地、尖厉刺耳地',
 '某句话、笑声或叫声是高高尖尖地发出来，用 shrilly。它在句子里主要修饰“怎么说、怎么叫”。',
 '普通副词由 shrill + 完整 -ly 构成，三枚 l 在常用拼写中简化为两枚 → shrilly。另有较少见形容词 shrill + -y，近源构词要分清。',SHRILL+[['shrill + -ly → shrilly〔常用副词拼写〕','以尖厉的声音说、笑、叫']],
 'laughed shrilly 是尖声笑，called shrilly 是尖声喊；多数普通场景解释这个副词义即可。',
 'cried shrilly 尖声叫；rang shrilly 刺耳地响。',
 'shrilly 描述声音的尖厉，cheerfully 描述心情轻快；尖声笑未必开心，也可能紧张，需看上下文。',
 ('She laughed shrilly at the sudden surprise.','突如其来的意外让她尖声笑了。'),('The alarm rang shrilly in the empty corridor.','警报在空走廊里尖厉地响。'),sources=S('shrilly','shrilly'))
W('shrillness','/ˈʃrɪlnəs/','声音尖厉刺耳的特点；语气尖锐激烈的程度',
 '把“声音尖得扎耳朵”这一特点整体提出来，叫 shrillness；也能说一场争论的语气越来越尖锐。',
 'shrill + 性质名词后缀 -ness，已有 ll 保留，不去 l、不双写 n。',SHRILL+[['shrill + -ness → shrillness','声音或语气尖厉这一性质']],
 'the shrillness of the whistle 是哨声的尖厉，the shrillness of the debate 是辩论语气的尖锐、激烈。',
 'shrillness in her voice 她声音里的尖厉感；reduce the shrillness 减轻刺耳程度。',
 'shrillness 与 loudness 不一样：前者关乎尖高刺耳的听感，后者关乎音量大小；调小音量也未必完全不尖。',
 ('The shrillness of the whistle made me cover my ears.','哨声尖厉刺耳，让我捂住耳朵。'),('I was surprised by the shrillness of the argument.','这场争论的语气如此尖锐，令我意外。'),sources=S('shrillness','shrill'))
RATTLE=[['中古英语 ratelen → rattle','连续碰撞的声音材料；可能借中古荷兰语，也有本土来源分析'],['声音 → 摇出响声、说得飞快 → 搅得人慌乱','名词还可指婴儿摇铃等发出哗啦声的器具']]
W('rattle','/ˈrætəl/','哗啦响、咯咯响；摇得响；使慌乱；摇铃、连续碰撞声',
 '摇一个装着硬币的盒子，里面一连串“哗啦、咯咯”响，叫 rattle；借来说人，就是把原本镇定的心搅乱。',
 '承中古英语 ratelen，可能借中古荷兰语同类形式，也有本土来源分析。古英语基础动词没有直接记录，不把推定形式写成确证。',RATTLE,
 'rattle the keys 是把钥匙摇得哗啦响；rattle off a list 是一口气飞快报出清单；rattle someone 是使人心慌、不镇定。',
 'a baby’s rattle 婴儿摇铃；rattle around 在里面晃得哗啦响。',
 'rattle 不一定代表东西破了：钥匙、玩具本来就能这样响。比喻人被 rattled 则是镇定被打乱。',
 ('Loose coins began to rattle inside the box.','松散的硬币开始在盒子里哗啦响。'),('The unexpected question did not rattle her.','突如其来的问题没有让她慌乱。'),sources=S('rattle','rattle'))
W('rattles','/ˈrætəlz/','连续碰响、摇得响、使慌乱〔第三人称单数〕；摇铃、连续响声〔复数〕',
 '硬物在盒子里晃来碰去，发一串细碎响声，用 rattles；婴儿的摇铃有几个，也用这个名词复数。',
 'rattle + -s，保留 e，/l/ 后读 /z/；已有 tt 属基础拼写，不再变化。',RATTLE+[['rattle + -s → rattles','它连续碰响；他、她摇得响；多个摇铃']],
 'rattles in the wind 是风一吹就咯咯响；nothing rattles her 是没有什么能使她慌乱，转到心理比喻。',
 'rattles the keys 摇得钥匙哗啦响；wooden rattles 木制摇铃。',
 'rattles 在 the window rattles 中是动词，在 two rattles 中可指数个摇铃；看句子位置，比只背一个中文义更清楚。',
 ('The loose window rattles in the wind.','松动的窗子被风吹得咯咯响。'),('The baby has two wooden rattles.','婴儿有两个木制摇铃。'),sources=S('rattles','rattle'))
W('rattled','/ˈrætəld/','连续碰响了、摇响了；慌乱的、心神不定的',
 '刚才硬物一连串响了，叫 rattled；一个人被意外打乱镇定，也说 looked rattled，像心里被摇乱了。',
 'rattle 去 e + 完整 -ed → rattled；/l/ 后读 /d/，基础词里的 tt 保留。',RATTLE+[['rattle 去 e + -ed → rattled','过去摇响、碰响；后来也形容慌乱状态']],
 'rattled the handle 是摇得把手响了；looked rattled 是看起来有些慌；rattled off the answers 是飞快报出答案。',
 'slightly rattled 有点慌；rattled by the news 被消息搅得心神不定。',
 'rattled 的心理义比 angry 更接近不镇定、受惊扰；人可能被弄慌，却没有生气。',
 ('The windows rattled as the train went past.','火车经过时，窗子咯咯作响。'),('She looked rattled by the sudden change of plan.','计划突然变动，让她显得有些慌乱。'),sources=S('rattled','rattle'))
W('rattling','/ˈrætlɪŋ/','正在连续碰响、摇响；哗啦声、咯咯声；使人慌乱的',
 '一串短促碰撞声正接连响着，是 rattling。也能写使人失去镇定，或飞快地念、说出内容。',
 'rattle 去 e + 完整 -ing → rattling；常读两音节 /ˈrætlɪŋ/，不是看见 -ing 就保留 e。',RATTLE+[['rattle 去 e + -ing → rattling','碰响、摇响过程；快速报说等扩展']],
 'a rattling window 是咯咯响的窗子，rattling off names 是一口气飞快报名字；听感与动作都由搭配提示。',
 'rattling around inside 在里面晃得响；the rattling of keys 钥匙哗啦声。',
 'rattling 多是接连的短响，ringing 更容易让人想到延续的共鸣；两种声音可以来自同一个物体的不同动作。',
 ('The rattling of the loose window kept me awake.','松动窗子的咯咯声让我睡不着。'),('He was rattling off names faster than I could write them down.','他报名字报得飞快，我都来不及记。'),sources=S('rattling','rattle'))
CLATTER=[['较晚古英语 clatrung 等动作名词证据 → 中古英语 clateren → clatter','碰撞、喧响；古英语基础动词形式据名词推知，带旧反复动作材料'],['动词 → 声音名词及移动描写','硬物接连碰响；带着这种声音哒哒、哗啦地移动']]
W('clatter','英 /ˈklætə/；美 /ˈklætər/','哗啦、哒哒地响；碰响着移动；一阵硬物碰撞声',
 '一摞盘子、几个锅盖碰来碰去“哗啦哗啦”，或马蹄在石路上“哒哒哒”，都像 clatter：硬物一连串碰响。',
 '接中古英语 clateren；较早证据有古英语动作名词 clatrung，基础动词形式是推知的。-er 含旧反复动作材料，不是“某种人”。',CLATTER,
 'the clatter of dishes 是餐具碰响，clatter down the stairs 是哒哒、咚咚地走下楼梯；声音也跟着移动。',
 'a loud clatter 哗啦一阵响；clatter onto the floor 哗啦掉到地上。',
 'clatter 常是响亮、连续的硬碰撞；rustle 偏轻薄材料的沙沙声，不能只按“有声音”混用。',
 ('The pans fell with a loud clatter.','平底锅掉下来，哗啦响成一片。'),('We heard horses clatter along the cobbled street.','我们听见马蹄在石板街上哒哒响。'),sources=S('clatter','clatter'))
W('clatters','英 /ˈklætəz/；美 /ˈklætərz/','哗啦、哒哒响〔第三人称单数〕；一阵阵碰响',
 '手推车走起来一路哐当响，或硬物落下接连碰响，用 clatters。复数名词也能指几阵碰撞声。',
 'clatter + -s，读 /z/；旧动作 -er 留在基础词中，现代词尾加在整个动词、名词后。',CLATTER+[['clatter + -s → clatters','它接连碰响；多阵碰响']],
 'clatters down the steps 是沿台阶哒哒、哐当而下，clatters onto the table 是碰得桌面一阵响。',
 'clatters noisily 哗啦作响；clatters along the road 一路哐当走。',
 'clatters 能把“移动加声音”一起写出来；moves 只说移动，不能让人听见轮子、马蹄或硬鞋底。',
 ('The old trolley clatters across the tiled floor.','旧手推车哐当哐当地驶过瓷砖地面。'),('The metal lid clatters onto the kitchen floor.','金属盖子掉到厨房地上，哗啦一响。'),sources=S('clatters','clatter'))
W('clattered','英 /ˈklætəd/；美 /ˈklætərd/','哗啦、哒哒地响了；碰响着移动了',
 '硬物刚才撞出一阵急促响声，或人、车带着哒哒、哐当声走过，用 clattered。',
 'clatter + 完整 -ed，读 /d/；词内虽有 tt，基础词末尾是轻元音或 r，不读 /ɪd/。',CLATTER+[['clatter + -ed → clattered','过去连续碰响、响着移动']],
 'clattered to the floor 是哗啦掉到地上；clattered down the stairs 是踩得楼梯咚咚、哒哒响着下楼。',
 'clattered past 哐当经过；clattered against the wall 碰墙发出一阵响。',
 'clattered 可以只有一个物件连续撞击，不一定需要一大堆东西；关键是接连的硬响。',
 ('The tray clattered to the floor.','托盘哗啦一声掉到地上。'),('She clattered down the stairs in heavy boots.','她穿着沉重的靴子，咚咚地走下楼梯。'),sources=S('clattered','clatter'))
W('clattering','英 /ˈklætərɪŋ/；美 /ˈklætərɪŋ/','正在哗啦、哒哒响；一阵接连碰撞声',
 '锅碗、车轮、马蹄的硬碰撞正一声接一声地响，叫 clattering。它也能写人在这种响声中移动。',
 'clatter + 完整 -ing；英式接元音时发 /r/。旧反复动作材料已在基础词里，现代直接变化。',CLATTER+[['clatter + -ing → clattering','连续碰响、响着移动的过程']],
 'clattering dishes 是碰得响的餐具，the clattering of hooves 是马蹄哒哒声；可以作背景声音名词。',
 'clattering down the stairs 咚咚下楼；a clattering cart 哐当响的车。',
 'clattering 比 tapping 通常更响、更杂乱；tapping 往往是一下一下较轻、较有控制的敲击。',
 ('The clattering of dishes came from the kitchen.','厨房里传来餐具哗啦碰响的声音。'),('A clattering cart passed beneath the window.','一辆哐当响的车从窗下经过。'),sources=S('clattering','clatter'))
CLANG=[['十六世纪英语 clang 动词 → 声音名词','响亮、有共鸣的尖声材料，大概拟声'],['可与拉丁 clangere、希腊 klangē 等比较','比较发声材料，不等于每个英语 clang 都直接借自拉丁语']]
W('clang','/klæŋ/','铿锵响、当啷响；使金属响；一声响亮的金属声',
 '敲到一块金属，声音“当——”地亮亮响开，叫 clang。抓住金属碰撞后响亮、有余响的感觉。',
 '英语里大概属拟声材料，可与拉丁 clangere、希腊 klangē 比较；不能据外形就写成确定的拉丁借词。',CLANG,
 'the clang of a bell 是钟的当当声，clang shut 是金属门当啷关上；也能主动敲得东西响。',
 'a loud clang 一声响亮的金属声；clang against metal 碰金属铿锵响。',
 'clang 常有响亮、回荡的金属声；clink 更轻更清脆，clank 往往让人想到沉重、机械的硬碰响。',
 ('The metal gate closed with a clang.','金属大门当啷一声关上了。'),('We heard the bells clang across the valley.','我们听见钟声铿锵，传过山谷。'),sources=S('clang','clang'))
W('clangs','/klæŋz/','铿锵、当啷响〔第三人称单数〕；一声声金属响',
 '门、钟或金属件每动一下就“当”地亮响，用 clangs；复数名词指一声声这种响。',
 'clang + -s，/ŋ/ 后读 /z/；ng 表示 /ŋ/，不另外加读一个 /ɡ/ 再接 s。',CLANG+[['clang + -s → clangs','它铿锵响；多声金属响']],
 'clangs shut 是当啷关上，clangs against the railing 是碰着栏杆铿锵响；几声金属响可以说 a few clangs。',
 'clangs loudly 大声铿锵响；distant clangs 远处的金属响。',
 'clangs 描写响声，closes 只说关上；the gate clangs shut 同时把动作和声音放进一句话。',
 ('The gate clangs shut behind the last visitor.','最后一位游客身后，大门当啷关上。'),('A few loud clangs came from the workshop.','作坊里传来几声响亮的金属撞击声。'),sources=S('clangs','clang'))
W('clanged','/klæŋd/','铿锵、当啷地响了；敲得金属响了',
 '金属物刚才“当——”响了，叫 clanged。它能同时写门怎样关、钟怎样响或物件怎样撞上去。',
 'clang + 完整 -ed，/ŋ/ 后读 /d/；不是 cling 的旧不规则过去式 clang 再接词尾来构成现代声音动词。',CLANG+[['clang + -ed → clanged','过去铿锵响、当啷碰响']],
 'clanged shut 是当啷关上，clanged against the bars 是碰到栏杆、金属条而响；常与方向、结果词一起用。',
 'clanged loudly 铿锵大响；clanged to the floor 当啷落地。',
 'clanged 常突出碰撞产生的响亮声，rang 还可以是规则敲钟、电话响等；两者能在钟声场景重合。',
 ('The bell clanged above the school entrance.','学校入口上方的钟铿锵响起。'),('The metal bucket clanged against the railing.','金属桶碰到栏杆，当啷作响。'),sources=S('clanged','clang'))
W('clanging','/ˈklæŋɪŋ/','正在铿锵、当啷响；响亮的金属碰撞声',
 '金属“当、当”地接连响，或一声声钟响回荡，是 clanging。它把整段响声拉出来作为背景。',
 'clang + 完整 -ing，/ŋ/ 后直接接 /ɪŋ/；保留 ng，不把它改成另一个动词。',CLANG+[['clang + -ing → clanging','金属响、钟响的过程与声音']],
 'clanging bells 是铿锵响的钟，the clanging of metal 是金属碰撞声；也能形容刺耳杂乱的金属响。',
 'loud clanging 响亮的当啷声；clanging against each other 相互碰得铿锵响。',
 'clanging 不一定杂乱：可以是规则钟响，也可以是乱碰金属声；规律性由场景另说。',
 ('The clanging of the bells filled the square.','广场上回荡着铿锵钟声。'),('Loose metal parts were clanging against one another.','松动的金属零件正相互撞得当啷响。'),sources=S('clanging','clang'))
CLANK=[['十七世纪 clank 动词 → 声音名词','金属短硬的碰撞声；可能拟声，也有低地德语来源或受 clang、clink 影响的分析'],['现代机械声、链条声及带声音的移动','像“哐当”一下下，常让人想到较沉的金属物件']]
W('clank','/klæŋk/','哐当响、金属硬碰响；哐当声',
 '铁链、机器或沉金属件“哐当”一碰，叫 clank。声音硬、机械，常给人比 clink 更沉的感觉。',
 '可能是拟声，或受 clang、clink 等形式影响，也有低地德语来源分析。不能说成现代 clang 按固定规则把 g 换成 k。',CLANK,
 'the clank of chains 是铁链的哐当声，clank along 是一路哐当响着移动；声音和移动可同时描述。',
 'a metallic clank 金属哐当声；clank shut 哐当关上。',
 'clank 常偏短、硬、沉，clang 常偏亮、有余响；它们有重合，不是两种严格分级的响度。',
 ('The machine stopped with a heavy clank.','机器哐当一声沉响，停了。'),('We could hear the chains clank in the wind.','我们听见铁链被风吹得哐当响。'),sources=S('clank','clank'))
W('clanks','/klæŋks/','哐当、金属硬碰响〔第三人称单数〕；一声声哐当响',
 '机器每转一下就硬硬碰响，或金属门每关一次就“哐当”，用 clanks；复数名词则指接连几声。',
 'clank + -s，/k/ 后读 /s/。nk 的 /ŋk/ 保留，与 clangs 的 /ŋz/ 有明显区别。',CLANK+[['clank + -s → clanks','它哐当响；多声硬金属碰响']],
 'clanks up the hill 是哐当响着上坡，clanks shut 是哐当关上；a series of clanks 是一连串机械碰响。',
 'clanks noisily 哐当作响；heavy clanks 沉重的哐当声。',
 'clanks 是声音词，不直接说明机器坏了；老车、链条或正常机械动作也可能发出这类响声。',
 ('The old lift clanks as it rises.','旧电梯上升时哐当作响。'),('A series of clanks came from the machinery.','机器里传出一连串哐当声。'),sources=S('clanks','clank'))
W('clanked','/klæŋkt/','哐当响了；哐当响着移动了',
 '刚才沉金属件硬碰了一下，或机器、车带着哐当声走过，用 clanked。画面里既有动作，也有声音。',
 'clank + 完整 -ed，/k/ 后读 /t/，结尾 /ŋkt/；不是 clanged 的另一种拼写。',CLANK+[['clank + -ed → clanked','过去哐当响、带响移动']],
 'clanked shut 是哐当关上，clanked past 是哐当响着经过；适合铁门、机器、较沉的金属物件。',
 'clanked against the wall 碰墙哐当响；clanked into place 哐当地落到位。',
 'clanked 把声响写进移动；went past 只说经过。读动作场景时，别把声音丢掉。',
 ('The iron door clanked shut behind us.','铁门在我们身后哐当关上。'),('An old tractor clanked past the house.','一辆旧拖拉机哐当响着从屋旁经过。'),sources=S('clanked','clank'))
W('clanking','/ˈklæŋkɪŋ/','正在哐当响；沉硬的金属碰撞声',
 '机器、铁链、沉金属件正一下下哐当作响，叫 clanking。声音往往带硬碰硬、机械移动的感觉。',
 'clank + 完整 -ing，/ŋk/ 保留，后接 /ɪŋ/；不双写 k。',CLANK+[['clank + -ing → clanking','金属硬碰响的过程、状态']],
 'clanking machinery 是哐当响的机器，the clanking of chains 是铁链碰撞声；可作为环境背景声。',
 'a clanking engine 哐当响的引擎；clanking along 一路哐当移动。',
 'clanking 偏沉硬，clinking 偏轻脆；钥匙、链条、杯子在不同力度下能发不同声音，要按听感选词。',
 ('The clanking of chains echoed through the yard.','铁链的哐当声在院子里回荡。'),('We passed a shed full of clanking machinery.','我们经过一间棚屋，里面机器哐当作响。'),sources=S('clanking','clank'))
def extend_lessons():
 extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_zfa',ROOTS,WORDS)
 extend_lessons()
