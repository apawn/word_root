"""Wing and experiment: shape/function branches and the practice of trying things."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
G=[['古诺斯语 vængr → 中古英语 wenge、winge → wing','动物翼；侧边伸出部分等'],['两侧伸展的形状、位置引申','机翼、建筑侧翼、舞台侧幕；群体一派'],['现代常用派生与组合','人物位置、翼展、翼尖、翼装、带翼形凸起的器件']]
W('wing','/wɪŋ/','翼、翅膀、机翼；侧翼、派别；临场发挥〔wing it〕',
 '先想身体两边伸出去的部分；飞机、楼的一侧、队伍两翼都可借这幅形状。政治 wing 说阵营一派，不是真的长出翅膀。',
 '借古诺斯语 vængr 经中古英语传下。更远联系风、吹的词源有可能但不确定。wing it 临场应付有舞台侧幕等旧解释，不把一种故事当定论。',G,
 'spread your wings 展翅、施展能力，under someone’s wing 受某人保护，the east wing 东侧楼翼，wing it 临场应付。',
 'spread your wings；under someone’s wing；the east wing；wing it。',
 'wing 翼，feather 羽毛不是同一部位；蝙蝠有翼却没有鸟类那种羽毛，wing 不只鸟能用。',
 ('The museum opened a new east wing.','博物馆开放了新东翼。'),('I had no notes, so I had to wing it.','我没有笔记，只好临场发挥。'),
 sources=['https://en.wiktionary.org/wiki/wing#English','https://www.etymonline.com/word/wing'])
W('wingless','/ˈwɪŋləs/','无翼的；翅膀退化的',
 '没有发达的翼，先描述身体结构；它不自动等于所有不会飞的动物，因为有翼也可能不会飞。',
 'wing + -less 没有，组成结构性质形容词。科学语境可涵盖翼很退化的情况，按具体描述理解。',G[:1]+[['wing + -less → wingless','没有翼、缺少发达翼']],
 'wingless insects 无翼昆虫，a wingless form 无翼形态，a wingless creature 无翼动物。',
 'wingless insects；a wingless form；a wingless creature。',
 'wingless 无翼，flightless 不能飞；企鹅有翼但不能飞，所以不能仅凭 flightless 就换成 wingless。',
 ('The textbook showed wingless insects.','课本展示了无翼昆虫。'),('The species has both winged and wingless forms.','这一物种有有翼和无翼两种形态。'))
W('wingspan','/ˈwɪŋspæn/','翼展；臂展〔引申〕',
 '把两翼展开，从一边翼尖量到另一边翼尖；不是把左右单片翼长随便取一片来叫总翼展。',
 'wing 翼 + span 跨距，组成横跨两端的长度名。也可借给人伸开双臂的距离。',G[:1]+[['wing + span → wingspan','左右翼尖之间的整体跨度']],
 'a wide wingspan 宽大翼展，measure the wingspan 测量翼展，an aircraft’s wingspan 飞机翼展。',
 'measure the wingspan；an aircraft’s wingspan；a wide wingspan。',
 'wingspan 两端总跨距，wingtip 是某一端翼尖；span 不是翅膀活了多少年的 lifespan。',
 ('The eagle has an impressive wingspan.','这只鹰翼展很大。'),('The label lists the aircraft’s wingspan.','标签列出了飞机翼展。'))
W('wingtip','/ˈwɪŋtɪp/','翼尖；翼纹鞋头、翼纹皮鞋〔鞋类语境〕',
 '鸟翼、机翼最外端就是 wingtip；皮鞋上沿鞋头向两侧延伸的翼形装饰，也借这个形状命名。',
 'wing 翼 + tip 尖端，先是翼末端；鞋类义接类似翅翼的鞋头拼接、装饰形状，复数 wingtips 常指整双鞋。',G[:1]+[['wing + tip → wingtip','翼的最外端'],['翼形外观 → 鞋类用法','翼纹鞋头；相应皮鞋']],
 'the aircraft’s wingtip 飞机翼尖，wingtip lights 翼尖灯，a pair of wingtips 一双翼纹皮鞋。',
 'the aircraft’s wingtip；wingtip lights；a pair of wingtips。',
 'wingtip 是尖端，wingspan 两端距离；鞋义说形状、装饰，不是鞋子具有飞行功能。',
 ('A small light flashed near the wingtip.','翼尖附近一盏小灯闪烁着。'),('He wore polished wingtips to the ceremony.','他穿着擦亮的翼纹皮鞋参加典礼。'))
W('wingsuit','/ˈwɪŋsuːt/','翼装',
 '手臂与躯干、双腿之间增加大片布面，展开后像多了翼面；是一种特殊服装，不是任何画了翅膀的上衣。',
 'wing 翼 + suit 成套服装，按展开后增加翼面、用于滑翔的功能命名。词形里的 suit 是服装，不是诉讼。',G[:1]+[['wing + suit → wingsuit','增加翼状表面的特殊服装']],
 'a wingsuit flyer 翼装飞行者，wingsuit flying 翼装飞行，a wingsuit design 翼装设计。',
 'wingsuit flying；a wingsuit flyer；a wingsuit design。',
 'wingsuit 服装，parachute 降落伞是另一设备；两者不能因为都出现在空中便当同一物。',
 ('The documentary followed a wingsuit flyer.','纪录片跟拍了一位翼装飞行者。'),('The exhibit showed how a wingsuit changes the body’s surface area.','展览展示了翼装如何改变身体展开的表面积。'))
W('winger','英 /ˈwɪŋə/；美 /ˈwɪŋər/','边锋、侧翼球员；某一派的人〔组合中〕',
 '场地或阵型的边上有 wing，在那里活动的球员就可叫 winger；政治组合里也可说某一翼的人。',
 'wing 侧翼 + -er 人物后缀。具体站位、任务随运动不同，不用同一个边锋定义盖住全部项目。',G[:1]+[['wing + -er → winger','在侧翼位置活动的人；所属一派的人']],
 'a left winger 左侧边锋，a fast winger 速度快的边锋，a right winger 右翼人物〔政治语境〕。',
 'a fast winger；a left winger；a right winger。',
 'winger 运动边路或政治派别看上下文；wingman 支援搭档不必在球场边路。',
 ('The winger sent a cross into the penalty area.','边锋向禁区传中。'),('The coach praised the young winger’s speed.','教练表扬了年轻边锋的速度。'))
W('wingback','/ˈwɪŋbæk/','翼卫、边翼卫；带翼靠背的椅子或其侧部〔家具语境〕',
 '足球里常是边路攻守都参与的位置；家具里高靠背两边伸出“耳朵”的椅子也可叫 wingback。',
 'wing 侧翼 + back 后部、后卫，体育组合按位置功能命名；家具义取靠背两侧的翼形部分。两种场景分开理解。',G[:1]+[['wing + back → wingback〔体育〕','边路与后卫角色相连'],['wing + back〔家具形状〕','靠背两侧的翼状部分、相应椅子']],
 'an attacking wingback 攻击型翼卫，a wingback chair 翼形靠背椅，play as a wingback 出任翼卫。',
 'an attacking wingback；play as a wingback；a wingback chair。',
 'wingback 不同运动的角色有差异；足球 winger 与 wingback 不必承担相同防守任务，家具语境更不能硬译球员。',
 ('She played as a wingback for the team.','她在队里出任翼卫。'),('A wingback chair stood beside the fireplace.','壁炉旁放着一把翼形靠背椅。'))
W('wingman','/ˈwɪŋmən/，也读 /ˈwɪŋmæn/','僚机飞行员；支援搭档、帮忙打圆场的朋友',
 '飞行中有人在旁配合支援；日常借来指陪你、帮你搭话打圆场的朋友，不一定真的会开飞机。',
 'wing 侧翼 + man 人物，先是航空配合角色，再引申社交支援伙伴。传统名称并不要求所有现代使用对象都按字面男性来解释。',G[:1]+[['wing + man → wingman','侧翼配合的飞行伙伴'],['航空支援关系 → 日常搭档比喻','陪同支援、帮忙打圆场的人']],
 'a reliable wingman 可靠僚机伙伴、搭档，act as someone’s wingman 当某人的助攻搭档，a pilot and a wingman 飞行员与僚机伙伴。',
 'a reliable wingman；act as someone’s wingman；a pilot and a wingman。',
 'wingman 支援搭档，winger 边路球员；社交语境的 wingman 常帮建立联系，不等于正式工作上的所有 assistant。',
 ('The pilot stayed close to her wingman.','飞行员与她的僚机伙伴保持接近。'),('He asked a friend to be his wingman at the party.','他请一位朋友在聚会上帮忙打圆场。'))
W('wingnut','/ˈwɪŋnʌt/','蝶形螺母；翼果树类；古怪者、极端派〔贬义俚语〕',
 '螺母两侧伸出像小翅膀的凸片，手指好拧；植物名则借带翼果实。骂人义的 nut 是“怪人”，不是一颗真的螺母变成人。',
 'wing + nut：器件里 nut 是螺母，植物里是果实命名；政治骂语常联系 right-wing nut 等缩短。不能把这三路全排成螺母导致极端观点。',G[:1]+[['wing + nut〔螺母〕→ wing nut、wingnut','带翼形手拧凸片的螺母'],['wing + nut〔果实〕；政治俚语另有缩短背景','翼果树类；贬称古怪、极端人物']],
 'tighten a wingnut 拧紧蝶形螺母，loosen the wingnut 松蝶形螺母，call someone a wingnut 骂人古怪极端〔俚语〕。',
 'tighten a wingnut；loosen the wingnut；a wingnut on the frame。',
 'wingnut 器件义也常分写 wing nut；人物义带贬意，不是中性的政治分类或正式心理诊断。',
 ('She tightened the wingnut by hand.','她用手拧紧了蝶形螺母。'),('The columnist used wingnut as an insult.','专栏作者把 wingnut 当骂语使用。'),
 sources=['https://en.wiktionary.org/wiki/wingnut#English','https://en.wiktionary.org/wiki/wing_nut#English','https://www.merriam-webster.com/dictionary/wingnut'])
R('B2670','翅翼的形状、侧边位置与支援功能','WING：向两边伸出去，后来借给楼、阵型、器件','wing → wingless；wingspan、wingtip、wingsuit 描部位、尺寸、衣物；winger、wingback、wingman 按人物位置；wingnut 分器件植物俚语，batwing 看外形。',
 '翼不等于羽毛，无翼不等于不能飞；翼展量两端，翼尖说一端。形状、位置、作用不同，组合义也各有方向。',
 'vængr 经中古英语 → wing；wing + -less/span/tip/suit/-er/back/man/nut；bat + wing。',
 [['基础与无翼状态','wing · wingless'],['尺寸、尖端与服装','wingspan · wingtip · wingsuit · batwing'],['侧翼人物、角色','winger · wingback · wingman'],['翼状器件、植物与口语人物','wingnut']],
 'wingless/flightless 结构能力不同；wingspan/wingtip 总跨距与尖端；winger/wingman 位置与支援；wingnut 人物义不从机械硬接。',
 'The diagram marked the wingtips and measured the wingspan.\n\n示意图标出了翼尖，并量出翼展。','wing wingless wingspan wingtip wingsuit batwing winger wingback wingman wingnut')
E=[['拉丁 experīrī → experimentum → 法语 esperiment → experiment','尝试、检验 → 一次试验、证明'],['英语名词再作动词','做实验；试着改变方法、材料'],['常用派生','experimental 试验性、基于实验；experimentation 实践过程；experimenter 实验者']]
W('experiment','名词 /ɪkˈsperɪmənt/；动词 /ɪkˈsperɪment/，弱读有变体','实验、试验；做实验、尝试不同方法',
 '不是只猜会怎样，而是安排一次尝试、观察会发生什么；科学实验追问结果，生活中 experiment with colours 则是试不同配色。',
 '经法语接拉丁 experimentum，源自 experīrī 尝试、检验。名词后形成英语动词，不把它现代拆成 experience + moment。',E,
 'conduct an experiment 做实验，an experiment on plants 关于植物的实验，experiment with colours 尝试不同颜色，a controlled experiment 对照条件下的实验。',
 'conduct an experiment；experiment with；a controlled experiment；an experiment on。',
 'experiment 实验，experience 经历、经验同族但不同词；experiment with 尝试材料、做法，experiment on 常针对研究对象。',
 ('The class conducted a simple experiment with light.','班里做了一个简单的光学实验。'),('She likes to experiment with different colours.','她喜欢尝试不同配色。'),
 sources=['https://en.wiktionary.org/wiki/experiment#English','https://www.etymonline.com/word/experiment'])
W('experimental','/ɪkˌsperɪˈmentəl/','实验的、基于实验的；试验性的；创新探索的',
 '可以说数据来自实验，也可以说新方法仍在试验；艺术里的 experimental 则常说在探索新形式，不按老套路来。',
 'experiment + -al，形成关系性质形容词，历史已有经验、实验等用法。不是所有 experimental 都表示失败、不靠谱。',E[:1]+[['experiment + -al → experimental','与实验有关、基于实验；作为尝试的']],
 'experimental results 实验结果，an experimental design 实验设计、试验性设计，experimental music 实验音乐。',
 'experimental results；an experimental design；experimental music。',
 'experimental 可以实验所得或试验性的；experienced 是有经验的，不要因开头相似把 experimental researcher 翻成资深研究员。',
 ('The paper presented the experimental results.','论文展示了实验结果。'),('The festival included experimental music.','音乐节包含实验音乐。'))
W('experimentation','/ɪkˌsperɪmenˈteɪʃən/','实验活动、试验探索；反复尝试的过程',
 '把一次次尝试不同办法、观察结果看成一段实践；不是只数某一次实验，而是强调试着摸索的过程。',
 'experiment 作动词接 -ation 的过程名词，词基较早有拉丁法语背景；历史不必重新解释成拉丁 ex- 加一串现代字母。',E[:1]+[['experiment〔动词〕+ -ation → experimentation','做实验、试验探索的活动过程']],
 'experimentation with materials 材料探索，through experimentation 通过试验，artistic experimentation 艺术探索。',
 'experimentation with；through experimentation；artistic experimentation。',
 'an experiment 可一次实验，experimentation 常不可数说实践过程；更多试验不自动保证结论正确，还需看设计和观察。',
 ('The design emerged through experimentation with paper.','设计是在反复尝试纸材时形成的。'),('The course encourages artistic experimentation.','课程鼓励艺术探索。'))
W('experimenter','英 /ɪkˈsperɪmentə/；美 /ɪkˈsperəmentər/','实验者、试验者；爱尝试的人',
 '负责安排、实施实验的人，也可宽泛说不断试新办法的人；与接受测试的参加者不是同一角色。',
 'experiment + -er，形成执行试验的人物名词。-er 的角色在这里是做实验，不是一定作为实验对象。',E[:1]+[['experiment + -er → experimenter','做实验、尝试新方法的人']],
 'the experimenter’s instructions 实验者指示，an experienced experimenter 有经验的实验者，a musical experimenter 音乐探索者。',
 'the experimenter’s instructions；an experienced experimenter；a musical experimenter。',
 'experimenter 实施者，participant 参加者；同一个人在某实验可兼角色，但词义本身要分开。',
 ('The experimenter explained the task to the participants.','实验者向参加者解释了任务。'),('She was an inventive experimenter with sound.','她是个在声音上很有创意的探索者。'))
R('B2689','试着做、观察发生什么，而非只凭想象','EXPERIMENT：让想法接受一次实际尝试','experiment → experimental、experimentation、experimenter，按一次试验、性质、过程和人物排在一起。',
 'experiment with colours 日常尝试，experimental results 实验所得；experimental music 探索形式，不必都按实验室解释。',
 'experīrī → experimentum 经法语 → experiment；experiment + -al/-ation/-er。',
 [['试验、性质、过程与人物','experiment · experimental · experimentation · experimenter']],
 'experiment/experience 实验经验；experimental/experienced 实验性与有经验；experimenter/participant 实施者参加者。',
 'The experimenter encouraged experimentation and recorded the experimental results.\n\n实验者鼓励尝试，并记录实验结果。','experiment experimental experimentation experimenter')
if __name__=='__main__':save('continuation_20261030_er',ROOTS,WORDS)
