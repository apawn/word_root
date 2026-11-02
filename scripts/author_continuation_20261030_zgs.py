"""Trembling, quivering, shivering and shuddering."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
def S(word,base):
 return ['https://en.wiktionary.org/wiki/'+word+'#English','https://www.etymonline.com/word/'+base]
EXISTING_ROOT_ADDITIONS={
 'C1542':dict(words='tremble trembles trembled trembling trembly'.split(),label='tremble：细小颤抖与发颤的性质',note='经法语 trembler 接拉丁 tremere、tremulus 等材料；trembly 则是英语 tremble 加 -y，不把整个 tremble 拆成英语 -able。'),
 'A1699':dict(words='quiver quivers quivered quivering quivery shiver shivers shivered shivering shivery'.split(),label='quivery、shivery：微颤与寒颤的两种性质',note='quiver 颤动动词远源未定，箭袋名词经法语来自容器材料，二者分路；shiver 颤抖承旧 chiveren 等不确定来源，碎片、击碎的旧同形词也分路。形容词 -y 写各自颤动性质。'),
 'A1760':dict(words='shudder shudders shuddered shuddering shudderingly'.split(),label='shudder：猛打一个寒战；机械也可震动',note='可能借荷兰语、低地德语相关摇动材料；不能把 shudder 的 -er 直接当成实施者人物后缀。现代过去式、-ing 和 -ly 再按英语分析。'),
}
TREM=[['拉丁 tremere、tremulus → 中世纪拉丁 tremulare 等','颤抖、发颤的材料'],['法语 trembler → 英语 tremble','由冷、害怕、情绪等造成细小抖动；现代再接规则词尾、形容词 -y']]
QUIVER=[['颤动 quiver 动词：更早来源未定','有拟声、quaver 变形或更早活泼形容词材料等不同分析，不能任选一条当定论'],['箭袋 quiver 名词：经法语接更早容器材料','与颤动动词分开；动作名词 a quiver 微颤则由颤动动词发展']]
SHIVER=[['中古英语 chiveren 等 → shiver 颤抖','远源未定，有下颌材料、寒冷与颤动词混合等不同分析；ch- 到 sh- 可能受 shake 影响'],['颤抖动词 → 寒颤名词；shiver + -y → shivery','现代常写冷、怕或其他强烈反应；旧碎片、击碎同形词另源，不合成一条']]
SHUDDER=[['中古英语 shoderen 等 → shudder','可能接荷兰语、低地德语反复摇动材料，不能写成已记录的古英语形式'],['动词 → 名词突然一颤；再接现代词尾','可由冷、恐惧、厌恶触发，机械也可震颤；不要求每次都是害怕']]
W('trembles','/ˈtrembəlz/','颤抖、发颤〔第三人称单数〕',
 '手拿着纸，纸边也跟着细细抖；声音说到一半不稳，都可以说 trembles。重点是连续的小幅颤动，不必大幅摇晃。',
 'tremble + -s，读 /z/；基础词经法语接拉丁 tremere 颤抖材料，不是英语 trem 加 -able。',TREM+[['tremble + -s → trembles','他、她或它发生细小颤动']],
 'trembles with fear 因害怕颤抖；his voice trembles 他的声音发颤。',
 'a hand trembles；trembles with excitement。',
 'trembles 可以是冷、紧张、兴奋，shakes 还可写幅度更大的摇动；不能从单个颤抖词就确定唯一原因。',
 ('Her voice trembles when she talks about the rescue.','她谈到那次营救时，声音会发颤。'),('The leaf trembles in the slightest breeze.','哪怕最轻的风也会让那片叶子微微颤动。'),sources=S('trembles','tremble'))
W('trembled','/ˈtrembəld/','颤抖、发颤了',
 '当时手不稳、声音打颤，过去发生了就是 trembled；可以是怕，也可以是激动到难以平稳。',
 'tremble 去 e 加完整 -ed，读 /d/；连着基础词末尾 /l/ 形成 /ld/，不额外加 /ɪd/。',TREM+[['tremble → trembled','过去发生细小颤动']],
 'trembled with cold 冷得发抖；trembled as she spoke 说话时声音、身体发颤。',
 'his hands trembled；trembled with relief。',
 'trembled 写反应，不自动表示一个人胆小；激动、释然、寒冷也能造成颤抖。',
 ('His hands trembled as he opened the envelope.','他拆信封时，双手微微颤抖。'),('She trembled with relief when she heard he was safe.','听说他安全后，她激动得浑身发颤。'),sources=S('trembled','tremble'))
W('trembly','/ˈtrembli/','发颤的；颤巍巍、不太稳的',
 '话已经说出来，声音却有点抖、撑不稳，可以叫 a trembly voice。比笼统说情绪激动，更能让人听见那份颤。',
 'tremble 去 e 加 -y → trembly；英语用 -y 把颤动变成性质，不把 -bly 当一个独立词根。',TREM+[['tremble + -y → trembly','有发颤、不稳的性质']],
 'a trembly voice 发颤的声音；trembly hands 颤抖的手。',
 'feel a little trembly；a trembly smile 伴着颤抖的微笑。',
 'trembly 描述发颤，tearful 描述含泪；两种情绪表现可能一起出现，但不是每次都相同。',
 ('She answered in a small, trembly voice.','她用微弱、发颤的声音回答。'),('His hands felt trembly after the excitement.','兴奋过后，他觉得双手还有些发颤。'),sources=S('trembly','tremble'))
W('quiver','英 /ˈkwɪvə/；美 /ˈkwɪvər/','微微颤动；一颤；箭袋、箭筒',
 '嘴唇轻轻抖、水面一圈微颤，都可以 quiver；弓箭手背的 quiver 箭筒却是另源名词，不是箭因为会颤才叫箭袋。',
 '颤动动词更早来源未定，有拟声、quaver 变形等分析；箭袋名词经法语 quivre 等接更早容器材料。动作名词一颤则从动词来。',QUIVER,
 'quiver with emotion 激动得微颤；a quiver in the voice 声音里一丝颤；an arrow in a quiver 箭筒里的箭。',
 'lips quiver 嘴唇发颤；a quiver of excitement 一阵兴奋的颤动。',
 'quiver 常写细微、快速的颤动，shudder 更容易是一阵猛打寒战；箭袋 quiver 与这两种动作都不能按字面混成同源。',
 ('Her lips began to quiver as she tried to speak.','她想开口时，嘴唇开始微微发颤。'),('He took an arrow from his quiver.','他从箭筒里取出一支箭。'),sources=S('quiver','quiver'))
W('quivers','英 /ˈkwɪvəz/；美 /ˈkwɪvərz/','微微颤动〔第三人称单数〕；微颤、箭袋〔复数〕',
 '嘴唇控制不住地细细抖，是 it quivers；几只箭筒是 quivers。复数和三单同形，但箭筒、颤动历史分开。',
 'quiver + -s，读 /z/；颤动动词三单与名词复数同形。装箭名词接容器材料，不能从微颤动作推出来。',QUIVER+[['quiver + -s → quivers','它细微颤动；多阵微颤或多只箭筒']],
 'her voice quivers 她声音发颤；quivers with excitement 激动得微颤。',
 'a leaf quivers；leather quivers 皮制箭筒。',
 'quivers with excitement 可是高兴，quivers with fear 则是害怕；同一个颤动词不决定情绪正负。',
 ('Her voice quivers whenever she mentions that day.','她每次提到那一天，声音都会发颤。'),('The archers placed their quivers beside the targets.','弓箭手把箭筒放在靶子旁边。'),sources=S('quivers','quiver'))
W('quivered','英 /ˈkwɪvəd/；美 /ˈkwɪvərd/','微微颤动了；声音发颤了',
 '话到嘴边，嘴唇细细一抖，或声音压不住情绪，过去发生了就是 quivered。常能让人看见、听见小幅变化。',
 'quiver + 完整 -ed，读 /d/；这里接颤动动词，不由箭袋名词推出。',QUIVER+[['quiver + -ed → quivered','过去细微颤动']],
 'lips quivered 嘴唇发颤；voice quivered with anger 声音气得发颤。',
 'quivered in the breeze；quivered with excitement。',
 'quivered with anger 可写努力压住但漏出的反应，shouted angrily 才明确大声喊；发颤不必然出声很大。',
 ('Her lower lip quivered, but she said nothing.','她的下唇微微发颤，却没有说话。'),('The reflection quivered on the water.','倒影在水面微微颤动。'),sources=S('quivered','quiver'))
W('quivering','英 /ˈkwɪvərɪŋ/；美 /ˈkwɪvərɪŋ/','微微颤动的；正在发颤',
 '薄叶、嘴唇、嗓音正细细抖，是 quivering。它既可以写动作过程，也能写物体、人当下发颤的样子。',
 'quiver + -ing；基础词末尾 r 前有弱读元音，直接接 -ing，不另双写 r。',QUIVER+[['quiver + -ing → quivering','细小快速颤动的过程或性质']],
 'quivering lips 发颤的嘴唇；a quivering voice 发颤的声音。',
 'quivering with excitement；a quivering leaf。',
 'quivering 常写很小、连续的颤动，swaying 常写幅度较大、来回慢摆；都是动，运动姿态不同。',
 ('He answered in a quivering voice.','他用发颤的声音回答。'),('The little dog stood quivering with excitement.','小狗站在那里，兴奋得微微发抖。'),sources=S('quivering','quiver'))
W('quivery','英 /ˈkwɪvəri/；美 /ˈkwɪvəri/','发颤、不稳的；带微颤的',
 '声音还撑着正常说话，尾音却轻轻抖，叫 a quivery voice。形容词把那种细微不稳提出来。',
 'quiver + -y；写微颤性质，不把 quiver 里的 -er 当作人名后缀。',QUIVER+[['颤动 quiver + -y → quivery','容易、正在呈现细微颤动的性质']],
 'a quivery voice 微颤的声音；quivery hands 发颤的手。',
 'a little quivery；a quivery note in her voice。',
 'quivery 常描述发颤的质感，quiet 只说明音量小；声音可以小而稳，也可以小且发颤。',
 ('There was a quivery note in her voice.','她的声音里带着一丝颤音。'),('His hands were still a little quivery after the excitement.','兴奋过后，他的手还有一点发颤。'),sources=S('quivery','quiver'))
W('shiver','英 /ˈʃɪvə/；美 /ˈʃɪvər/','发抖、打寒颤；一阵寒颤',
 '冷风一吹，身体不由自主地细细抖，是 shiver；害怕、反感或想到某件事，也可能让人打一个寒颤。',
 '承中古英语 chiveren 等形式，远源未定；ch- 到 sh- 可能受 shake 影响。寒颤名词由动词发展，旧碎片、击碎同形词另源。',SHIVER,
 'shiver with cold 冷得发抖；a shiver down the spine 脊背一阵发凉；give someone the shivers 让人不寒而栗。',
 'a little shiver；shiver at the thought 一想到就打寒颤。',
 'shiver 常让人联想到冷，但也能来自怕、兴奋等反应；quake、shudder 各有常见倾向，不能替所有句子指定唯一原因。',
 ('I began to shiver in the cold wind.','冷风里，我开始发抖。'),('A shiver ran down her spine when she heard the noise.','听见那个声音，她脊背一阵发凉。'),sources=S('shiver','shiver'))
W('shivers','英 /ˈʃɪvəz/；美 /ˈʃɪvərz/','发抖〔第三人称单数〕；阵阵寒颤、不寒而栗的感觉〔复数〕',
 '他冷得身体细细抖，是 he shivers；一个地方让人莫名脊背发凉，可以说 it gives me the shivers。',
 'shiver + -s，读 /z/；动词三单和寒颤名词复数同形，the shivers 是常见整块表达。',SHIVER+[['shiver + -s → shivers','他发抖；一阵阵寒颤或恐惧反应']],
 'shivers with cold 冷得发抖；gives me the shivers 让我不寒而栗。',
 'shivers in the doorway；a story that sends shivers down your spine。',
 'the shivers 在故事里可写害怕，不一定是实际温度低；chills 也可类似，要靠场景看是寒冷还是强烈感受。',
 ('He shivers whenever the wind blows through the doorway.','风一从门口吹过，他就冷得发抖。'),('That abandoned house gives me the shivers.','那栋废弃房子让我不寒而栗。'),sources=S('shivers','shiver'))
W('shivered','英 /ˈʃɪvəd/；美 /ˈʃɪvərd/','发抖、打寒颤了',
 '当时一阵冷、一阵怕，身体不由自主地抖起来，是 shivered。也可写只是想到某件事就打个寒战。',
 'shiver + 完整 -ed，读 /d/；这里讲颤抖支线，旧击碎支线也同形，但来源分开。',SHIVER+[['shiver + -ed → shivered','过去出现一阵或持续寒颤']],
 'shivered with cold 冷得发抖；shivered at the thought 想到就打寒颤。',
 'shivered in the rain；shivered despite the warm room。',
 'shivered 是身体反应，was cold 才直接说感觉冷；暖房里也可能因恐惧、强烈反应而 shivered。',
 ('We shivered while waiting in the rain.','我们在雨里等候，冷得发抖。'),('She shivered at the thought of going back.','一想到要回去，她就打了个寒颤。'),sources=S('shivered','shiver'))
W('shivering','英 /ˈʃɪvərɪŋ/；美 /ˈʃɪvərɪŋ/','正在发抖、打寒颤；发抖的状态',
 '外套湿透，人还在一阵阵发抖，是 shivering；也能把这份不由自主的颤抖当名词讲。',
 'shiver + -ing；既作动作形式，也可作行为、状态名词，或描述发抖的人。',SHIVER+[['shiver + -ing → shivering','颤抖正在发生；或命名发抖状态']],
 'shivering with cold 冷得发抖；a shivering child 发抖的孩子。',
 'stop shivering；stand shivering by the door。',
 'shivering 是发抖，shimmering 是闪烁、微光摇动；拼写接近，但在描写人、水面时画面不同。',
 ('The child stood shivering in the wet coat.','孩子穿着湿外套站着，浑身发抖。'),('We found him shivering beside the open window.','我们发现他在开着的窗旁冷得发抖。'),sources=S('shivering','shiver'))
W('shivery','英 /ˈʃɪvəri/；美 /ˈʃɪvəri/','冷得发抖的；令人打寒颤的；发颤的',
 '人觉得冷得身上发抖，是 shivery；故事读得背后发凉，也能形容为 shivery，重点在寒颤的感觉。',
 '颤动名词 shiver + -y；写带寒颤、发颤的性质，或会引起这类感觉。不是旧碎片词义的直接延伸。',SHIVER+[['shiver + -y → shivery','带寒颤、发抖的性质，也可写令人寒颤']],
 'feel shivery 感到冷得发抖；a shivery story 令人背脊发凉的故事。',
 'cold and shivery；a shivery sensation 一阵寒颤感。',
 'shivery 可以写人有寒颤，也可写事物引起寒颤；和 boring／bored 不同，不能把所有 -y 都只锁定反应中的一方。',
 ('I felt cold and shivery after the walk.','走完那段路，我觉得冷得身上发抖。'),('It was a shivery story about footsteps in an empty house.','那是个让人背脊发凉的故事，讲空屋里的脚步声。'),sources=S('shivery','shivery'))
W('shudder','英 /ˈʃʌdə/；美 /ˈʃʌdər/','猛地颤一下、打寒战；震颤；一阵寒战',
 '想到可怕或恶心的事，身体一下缩紧、颤过一阵，是 shudder；机器一阵沉重震动，也能用这个词。',
 '中古英语 shoderen 等，可能借荷兰语、低地德语相关反复摇动材料；名词一阵颤动由动词发展。',SHUDDER,
 'shudder with horror 吓得打寒战；shudder at the thought 想到就犯怵；with a shudder 打着寒战。',
 'I shudder to think 一想到就后怕；a shudder through the train 列车一阵震动。',
 'shiver 常写细细发抖，shudder 常更像突然一阵、身体较强的反应；实际可交叠，不把原因锁死为冷或恐惧。',
 ('I shudder to think what might have happened.','一想到当时可能发生什么，我就后怕。'),('A shudder ran through the train as it stopped.','列车停车时，车身一阵震动。'),sources=S('shudder','shudder'))
W('shudders','英 /ˈʃʌdəz/；美 /ˈʃʌdərz/','打寒战、震颤〔第三人称单数〕；阵阵寒战〔复数〕',
 '每次听到那段声音，她身体就一缩、一颤，是 she shudders；让人发怵的感觉也可说 gives me the shudders。',
 'shudder + -s，读 /z/；动词三单和动作名词复数同形，the shudders 可整体写强烈不适、寒战。',SHUDDER+[['shudder + -s → shudders','她突然颤动；一阵阵寒战、震颤']],
 'shudders at the memory 想起就打寒战；gives me the shudders 让我发怵。',
 'shudders to a halt 震颤着停下；the shudders of the machine 机器阵阵震动。',
 'shudders to a halt 可以是机器震动，不是机器害怕；动词的身体意象也能用于机械运动。',
 ('She shudders whenever she remembers the accident.','她每次想起那次事故都会打个寒战。'),('That scraping sound gives me the shudders.','那种刮擦声让我浑身不舒服。'),sources=S('shudders','shudder'))
W('shuddered','英 /ˈʃʌdəd/；美 /ˈʃʌdərd/','打寒战、猛颤了；震颤了',
 '身体突然不由自主地一颤，是 shuddered；老机器停下时震一阵，也一样能写，不要求有人的情绪。',
 'shudder + 完整 -ed，词尾读 /d/；末尾 er 属于基底，整体再接过去词尾。',SHUDDER+[['shudder + -ed → shuddered','过去突然、较强地颤动或震动']],
 'shuddered at the sight 看到就打寒战；shuddered to a halt 震颤着停下。',
 'shuddered with disgust 厌恶得打寒战；the engine shuddered 发动机一阵震动。',
 'shuddered to a halt 着重停下时不平稳的震动，glided to a halt 则是平滑地滑停；结果同为停下，过程画面相反。',
 ('He shuddered at the memory of the freezing water.','一想起那冰冷的水，他就打了个寒战。'),('The old bus shuddered to a halt.','旧巴士震颤着停了下来。'),sources=S('shuddered','shudder'))
W('shuddering','英 /ˈʃʌdərɪŋ/；美 /ˈʃʌdərɪŋ/','正在打寒战、震颤；一阵阵强烈颤动的',
 '身体一阵缩紧、抖过，或机器沉重地震动着，是 shuddering。可以写动作过程，也可形容一次呼吸、声音里的震颤。',
 'shudder + -ing；规则动作形式，末尾 r 保留，直接接词尾。',SHUDDER+[['shudder + -ing → shuddering','强烈颤动的过程；或带这种颤动的性质']],
 'a shuddering breath 发颤的一口气；shuddering to a halt 震颤着停下。',
 'shuddering with cold；a shuddering engine 震颤的发动机。',
 'a shuddering breath 常能让人听见断续、不稳，a sigh 只是叹气；一口气可以兼有两种表现，词关注点不同。',
 ('She took a deep, shuddering breath before speaking.','开口前，她深深吸了一口发颤的气。'),('The engine was shuddering as the bus climbed the hill.','巴士爬坡时，发动机正一阵阵震动。'),sources=S('shuddering','shudder'))
W('shudderingly','英 /ˈʃʌdərɪŋli/；美 /ˈʃʌdərɪŋli/','打着寒战地；带震颤地',
 '不是平稳呼吸，而是带着一阵阵颤，一口气不稳地出来，可以写 breathed shudderingly。常见于叙事中描写身体反应。',
 'shuddering + -ly；内层 shudder + -ing，外层把颤动性质用于呼吸、动作等方式。',SHUDDER+[['shudder → shuddering → shudderingly','强烈颤动的性质，转成做动作时的方式']],
 'breathed shudderingly 带颤地呼吸；sighed shudderingly 颤着叹气。',
 'shudderingly drew breath；shudderingly turned away。',
 'shudderingly 写动作里带一阵颤，fearfully 写害怕的态度；两者可能相关，但不能把身体反应的原因永远锁定一种情绪。',
 ('He breathed shudderingly after climbing out of the cold water.','从冷水里爬出来后，他带着寒战呼吸。'),('She sighed shudderingly and covered her face.','她颤着叹了口气，捂住脸。'),sources=S('shudderingly','shudder'))
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_zgs',ROOTS,WORDS)
 extend_lessons()
