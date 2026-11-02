"""Communicate and ring: sharing, connection, circular objects and sound."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
C=[['拉丁语 commūnis → commūnicāre、commūnicāt-','共同的 → 使共享、告知、传递'],['借入英语 communicate','沟通、传达；使相通等']]
def CH(f,m):return C+[[f,m]]
W('communicate','/kəˈmjuːnɪkeɪt/','沟通、交流；传达；相通〔房间等〕',
 '把原来只有自己知道的内容送给别人，让它成为双方能共享的信息。也可以不用说话，靠表情、图像传达。',
 '借拉丁语 commūnicāt- 词干形成英语动词，背后是 commūnis 共同的。-ate 是英语动词词形材料；不要把 communicate 拆成英语 common 加一个不存在的独立词。',C,
 'communicate with someone 与某人交流，communicate an idea to someone 向某人传达想法；rooms communicate 房间相通，较书面。',
 'communicate with；communicate ideas；communicate clearly；communicate through。',
 'communicate 不只开口讲话，say 偏说出内容；communicate with 人与 communicate something to 人宾语位置不同。',
 ('We communicate mainly by email.','我们主要通过电子邮件交流。'),('The drawing communicates the idea more clearly than words.','这幅图比文字更清楚地传达了这个想法。'))
W('communicating','英 /kəˈmjuːnɪkeɪtɪŋ/；美 /kəˈmjuːnəkeɪtɪŋ/','正在交流、传递的；相通的〔房间〕',
 '普通句子里是交流这个动作在进行；酒店房型里则可能是两个房间中间有门相通。',
 'communicate 去末尾 e 加 -ing。形容词相通义接 communicate 的连接、通达支线，不是房间会说话。',CH('communicate + -ing → communicating','交流、传递；互相通连的'),
 'communicating with a client 与客户交流，communicating rooms 相通客房，a communicating door 连通门。',
 'communicating rooms；a communicating door；communicating with。',
 'communicating rooms 房间内部可互通，adjacent rooms 只说相邻，不保证中间有门。',
 ('The hotel gave us two communicating rooms.','酒店给我们安排了两间相通的客房。'),('She is communicating with the team through an interpreter.','她正通过口译员与团队交流。'))
W('communication','/kəˌmjuːnɪˈkeɪʃən/','交流、沟通；信息传递；通知、来函；通信〔按语境〕',
 '把内容从一方送到另一方的过程；也可以指送来的那一份正式消息。不可数过程和可数来函要分清。',
 '经法语 communicacion、拉丁语 commūnicātiōn- 进入中古英语，本身有独立名词借入链，在英语中早于 communicate。现代可对照 communicate 与 -ion，但不画成较晚英语动词生出较早名词。',
 [['拉丁语 commūnicāre → commūnicātiō、commūnicātiōnem','使共享 → 交流、传达的动作名词'],['法语 communicacion 等 → 中古英语 communicacioun → communication','沟通、交流；传达内容、通信方式']],
 'clear communication 清楚沟通，a breakdown in communication 沟通中断，an official communication 正式通知，communications equipment 通信设备。',
 'communication skills；clear communication；an official communication；a breakdown in communication。',
 'communication 过程或信息，conversation 对话是具体交流形式；网络通了不保证双方真正理解，但都可讨论 communication。',
 ('Good communication helped the teams avoid mistakes.','良好沟通帮助各团队避免出错。'),('We received an official communication from the museum.','我们收到博物馆的一份正式通知。'))
W('communicator','英 /kəˈmjuːnɪkeɪtə/；美 /kəˈmjuːnɪkeɪtər/','沟通者、善于传达的人；通信设备〔按语境〕',
 '不仅自己懂，还能把意思送进别人脑子里的人，常被夸为 a good communicator；科幻里也可以是通信小设备。',
 'communicate + -or，并有拉丁语 commūnicātor 等人物词作背景。词尾 -or 表参与、执行传达者，不限定职业。',CH('communicate + -or → communicator；参照拉丁语人物词','传达、沟通的人；也可命名设备'),
 'an effective communicator 善于沟通的人，a skilled communicator 很会传达的人，a handheld communicator 手持通信设备。',
 'a good communicator；an effective communicator；a handheld communicator。',
 'communicator 人或器具，communication 沟通过程、消息；a good communicator 不必话最多，能让人明白才是重点。',
 ('A good teacher needs to be an effective communicator.','好老师需要善于把意思讲明白。'),('The explorer spoke into a small communicator.','探险者对着一个小通信器说话。'))
R('B4245','使共享；交流、传递与连接','COMMUNICATE：把内容传给别人，使双方能共享','communicate → communicating、communicator；communication 现代放同组，历史保留独立且较早的名词借入。',
 '不把名词按表面后缀硬画成现代动词的后代。相通房间借连通义，正式来函是传达内容的可数用法。',
 '拉丁语 commūnis、commūnicāre、commūnicāt-；communicate 去 e 加 -ing/-or；communication 对应 -ion 但另有借入链。',
 [['传达、过程与参与者','communicate · communicating · communication · communicator']],
 'communicate with 人、communicate something to 人；communication 可过程也可来函；communicating rooms 相通不只相邻。',
 'Clear communication helped both teams understand the plan.\n\n清楚的沟通帮助两支团队都理解了计划。','communicate communicating communication communicator')
RC=[['古英语 hring → 中古英语 ryng → ring','圆环、圆圈；环形围合的区域'],['另一词：古英语 hringan → ring','发出铃声、使鸣响，通常认为有拟声背景'],['现代 ring 两条常用路径','戒指、圈、拳击台等；铃响、电话等']]
W('ring','/rɪŋ/','戒指、环、圈；拳击台；铃声；鸣响、打电话',
 '一条像手指上的圈，另一条像耳朵里的铃声。两条旧来源要分开，不能说因为铃铛是圆的，所以戒指就变成铃响。',
 '环来自古英语 hring；响来自动词 hringan。环义动词围成圈常用 ringed，鸣响义 ring—rang—rung。拳击台源于围出的比赛空间，现代不必是圆形。',RC,
 'a wedding ring 婚戒，a ring of trees 一圈树，a boxing ring 拳击台；ring the bell 按铃，give someone a ring 打电话〔尤其英式〕。',
 'a wedding ring；a boxing ring；ring the bell；give me a ring。',
 'ringed the tree 给树围圈或作环形标记，rang the bell 使铃响；两套过去式跟着词义走。',
 ('She wore a silver ring on her finger.','她手指上戴着一枚银戒指。'),('The bell rang just as we reached the door.','我们刚到门口，铃就响了。'),
 sources=['https://en.wiktionary.org/wiki/ring#English','https://www.etymonline.com/word/ring'])
W('ringer','英 /ˈrɪŋə/；美 /ˈrɪŋər/','敲铃者、铃响装置；冒名顶替的高手；极像的人〔dead ringer〕',
 '叫铃响的人或装置，构词最清楚；比赛里偷偷换上的强手和 a dead ringer 极像的人，常见但来源细节不能全靠敲铃故事解决。',
 '敲铃义可明确接 ring + -er，中古英语已有。替身、冒名者、极像者等支线的具体形成不完全确定，词典有不同解释，不统一编成赢了比赛敲铃。',
 [['ring〔鸣响〕+ -er → ringer','敲铃的人、铃声装置'],['其他 ringer 用法：冒名、替身、极像者','来源细节有不确定性，现代用法分别学习']],
 'the phone’s ringer 手机铃声装置，turn the ringer off 关铃声；a dead ringer for someone 与某人极像；bring in a ringer 暗中找高手顶替。',
 'turn off the ringer；a dead ringer for；bring in a ringer。',
 'dead ringer 的 dead 表程度强、完全，不是死去的敲钟人；ringer 与 ringtone 铃声曲调也不完全同义。',
 ('Turn the ringer off before the concert.','音乐会开始前把手机铃声关掉。'),('She is a dead ringer for her older sister.','她和姐姐长得简直一模一样。'))
W('ringside','/ˈrɪŋsaɪd/','拳击台边；紧邻比赛场地的；近距离观察位置',
 '坐在比赛围台的边上，看动作特别近；看一件事的第一现场，也能比喻有 ringside view。',
 'ring 比赛围台 + side 边，组成位置名词和修饰语。接圆圈、围合场地这条 ring，不接电话铃声。',RC[:1]+[['ring + side → ringside','比赛台旁；比喻近距离见证的位置']],
 'a ringside seat 拳击台边座位，a ringside view 近距离视角，sit at ringside 坐在拳击台旁。',
 'a ringside seat；a ringside view；at ringside。',
 'ringside 强调贴近比赛台或事件现场，不是坐在电话旁；现代拳击台通常是方形，名称保留旧围圈背景。',
 ('They paid extra for ringside seats.','他们加钱买了拳击台边的座位。'),('Her job gave her a ringside view of the negotiations.','她的工作让她能近距离见证谈判。'))
W('ringmaster','英 /ˈrɪŋmɑːstə/；美 /ˈrɪŋmæstər/','马戏团表演主持人；统筹全场的人〔比喻〕',
 '在马戏场中央介绍节目、衔接表演，把全场带着走的人。master 在这里指主持、掌控的人。',
 'ring 马戏表演场 + master 主持、掌管者，合成职业名；后来借指统筹复杂活动的人。',RC[:1]+[['ring + master → ringmaster','主持马戏表演的人；比喻统筹者']],
 'the circus ringmaster 马戏主持人，act as ringmaster 像主持全场一样统筹。',
 'a circus ringmaster；act as ringmaster；the ringmaster’s announcement。',
 'ringmaster 主持节目，ringleader 常指带头组织不良活动的人；两者都可领导协调，常见语气不同。',
 ('The ringmaster introduced the next act.','马戏主持人介绍了下一个节目。'),('She acted as ringmaster for the busy charity event.','她像掌控全场的主持人一样统筹了忙碌的慈善活动。'))
W('ringworm','英 /ˈrɪŋwɜːm/；美 /ˈrɪŋwɜːrm/','癣〔真菌感染的传统英语名称〕',
 '名字容易骗人：不是皮肤里有一条绕圈的虫。名称与环形皮疹等旧理解有关，现代指真菌感染。',
 '旧英语 rengwyrm、中古英语 ringworm 等形式延续，表面是 ring + worm。旧命名和现代病因认识分开：名字里的 worm 不等于病因是虫。',RC[:1]+[['旧英语 rengwyrm → 中古英语 ringworm → ringworm','环状皮肤表现相关的旧病名；现代指真菌感染']],
 'a ringworm infection 癣感染，a ringworm rash 癣的皮疹。这里只解释词义与命名，不凭词形辨认、诊断个人皮肤问题。',
 'a ringworm infection；a ringworm rash；the name ringworm。',
 'ringworm 名称含 worm 却由真菌造成；不能用中文环虫病机械理解。不同部位的名称和表现需按具体医学语境。',
 ('The leaflet explains that ringworm is caused by fungi.','宣传页解释说，癣是由真菌引起的。'),('The vet diagnosed the cat with ringworm.','兽医诊断这只猫患了癣。'),
 sources=['https://en.wiktionary.org/wiki/ringworm#English','https://www.cdc.gov/ringworm/about/index.html'])
R('B2962','环形、围合；铃响另源，人物与场所分别接支线','RING：眼睛看到的圈，耳朵听到的铃，要分两条线','ring → ringer；earring、keyring 环形物；ringtone 鸣响；ringside、ringmaster、ringleader 场地或群体；ringworm 旧名称另辨。',
 'ringed 与 rang/rung 随不同来源和意义变化。ringer 的相貌、替身支线不编确定起源；ringworm 的名称不当病因。',
 'ring〔环〕—ringed；ring〔响〕—rang—rung；ring + -er/side/master/worm/tone；ear/key + ring。',
 [['环与随身物品','ring · earring · keyring'],['声音、装置及人物用法','ringer · ringtone'],['比赛、表演和带头者','ringside · ringmaster · ringleader'],['旧病名辨析','ringworm']],
 '环与铃响另源；ringmaster/ringleader 常见语气不同；dead ringer 极像而非死人；ringworm 真菌感染。',
 'He took a ringside seat and waited for the bell to ring.\n\n他坐到拳击台边，等着铃声响起。','ring earring keyring ringer ringtone ringside ringmaster ringleader ringworm')
ROOTS[-1]['exclude']['coring']='常见 coring 为 core 去芯的 -ing 形式；另有罕见 co- + ring 数学词。本轮不把前者误作圆环 ring 的直接派生。'
if __name__=='__main__':save('continuation_20261030_cf',ROOTS,WORDS)
