"""Observation instruments, acoustics, affection and several homographs."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
Sc=[['拉丁 oscillare 摆动 → oscillo-','振荡、来回变化'],['oscillo- + 希腊来源 -scope 观察仪器 → oscilloscope','把电信号随时间等的变化显示为图形']]
W('oscilloscope','英 /əˈsɪləskəʊp/；美 /əˈsɪləskoʊp/','示波器',
 '电压在变，肉眼看不见；示波器把变化画成屏幕上的线，让你看见信号怎样起伏。oscillo- 是摆动、变化，-scope 是观察工具。',
 'oscillo- 接拉丁 oscillare 摆动，-scope 接希腊 skopein 观察；近代混合构词，用于显示电信号的仪器。',Sc,
 'an oscilloscope trace 示波器轨迹，an oscilloscope screen 示波器屏幕；常见显示电压随时间变化，也有其他显示模式。',
 'an oscilloscope trace；connect a signal to an oscilloscope。',
 '示波器把信号变为可见图形，不表示一定在看声音；声音经转换成电信号后也能研究。',
 ('The oscilloscope displayed a repeating waveform.','示波器显示出重复的波形。'),('She adjusted the time scale on the oscilloscope.','她调整了示波器的时间刻度。'),sources=['https://en.wiktionary.org/wiki/oscilloscope#English','https://www.etymonline.com/word/oscilloscope'])
R('A1828','观察仪器的成分，把看不清、看不见的东西呈现出来','-SCOPE：帮你观察，前面说明看什么、怎样看','telescope 看远处，microscope 看微小物，oscilloscope 看变化的电信号。',
 '观察不一定是眼睛直接望进去：听诊器把声音传来，示波器把信号画出。先问仪器让哪种信息可被察觉。',
 '希腊 skopein 观察 → -skopion → 拉丁化 -scopium → 英语 -scope。',
 [['远近、方向与光学图形','telescope · microscope · periscope · kaleidoscope'],['身体、转动与电信号','stethoscope · endoscope · gyroscope · oscilloscope']],
 '带 -scope 的仪器作用各异；不能一律翻成普通放大镜。',
 'A microscope reveals tiny structures, while an oscilloscope reveals changing electrical signals.\n\n显微镜显出微小结构，示波器显出变化的电信号。','telescope microscope periscope kaleidoscope stethoscope endoscope gyroscope oscilloscope')
A=[['希腊 akouein／akouo 听 → akoustikos','听觉、声音相关的'],['中世纪拉丁 acousticus → acoustic','听觉、声学的；音乐中指原声形式'],['-s、-al、-ally 扩展','学科或空间声音特性；形容词、副词']]
W('acoustic','/əˈkuːstɪk/','声音的、声学的；原声的、不靠电扩音产生本体声音的',
 'acoustic 先锁定声音如何产生、传递、被听到。acoustic guitar 的弦与琴体自己发声；音乐现场即使用麦克风扩音，也仍可称原声吉他。',
 '经中世纪拉丁 acousticus 借自希腊 akoustikos，与 akouo 听相关。由听觉、声学性质扩展到音乐中的原声器乐形式。',A[:2],
 'acoustic properties 声学性质，acoustic panels 吸声、声学处理板，an acoustic guitar 原声吉他，an acoustic version 原声版。',
 'an acoustic guitar；acoustic treatment；acoustic properties。',
 '音乐中的 acoustic 看发声方式、编配，不保证现场完全没有电子设备。声学处理也不全等同于彻底隔音。',
 ('He played the song on an acoustic guitar.','他用原声吉他弹了这首歌。'),('The panels improved the room’s acoustic properties.','这些板材改善了房间的声学特性。'))
W('acoustics','/əˈkuːstɪks/','声学；空间的声音传播、回响效果',
 '研究声音怎样振动、传播，是学科 acoustics；走进大厅说“这里听起来真好”，评价的是这地方的 acoustics。',
 'acoustic + -s；学科名的 -s 类似 physics 等。空间声音特性义通常按复数性质使用。',A[:2]+[['acoustic + -s → acoustics','声音研究学科；场所的声音传播特性']],
 'study acoustics 学习声学，the acoustics of a hall 大厅音响效果，good acoustics 良好音响条件。',
 'acoustics is ...〔学科〕；the acoustics are ...〔场所效果〕。',
 '学科通常单数谓语 Acoustics is；房间的声学特性常用复数谓语 The acoustics are。',
 ('Acoustics is part of the engineering course.','声学是工程课程的一部分。'),('The acoustics in the concert hall are excellent.','音乐厅的音响效果非常好。'))
W('acoustical','/əˈkuːstɪkəl/','声学的、与声音或听觉有关的',
 '和 acoustic 的声学义大体重叠，多在工程、设计里说声音怎样在空间里表现。多一个 -al，并没有把声音变成另一种物理现象。',
 'acoustic + -al，形成扩展形容词；与 acoustic 在听觉、声学性质上常同义。',A[:2]+[['acoustic + -al → acoustical','与声学、声音特性有关的']],
 'acoustical engineering 声学工程，acoustical design 声学设计，acoustical treatment 声学处理。',
 'acoustical design；acoustical engineering。',
 '原声吉他习惯叫 acoustic guitar；谈工程 acoustical 与 acoustic 常有重叠，搭配习惯比硬分高低更有用。',
 ('The architect consulted an acoustical engineer.','建筑师咨询了一位声学工程师。'),('The room needs better acoustical treatment.','房间需要更好的声学处理。'))
W('acoustically','/əˈkuːstɪkli/','从声学角度；以声音方式；以原声方式',
 '看房间声音表现，是 acoustically；把歌改用原声乐器演出，也能说 play it acoustically。前者看考察角度，后者看演出方式。',
 'acoustic + -ally，或 acoustical + -ly；-ically 通常读 /ɪkli/，形成角度、方式副词。',A[:2]+[['acoustic + -ally → acoustically','声学方面；以原声等方式']],
 'acoustically treated room 做过声学处理的房间，perform acoustically 以原声方式演出。',
 'acoustically treated；play acoustically。',
 'acoustically treated 可能处理混响、反射等；不必然表示对外完全隔音。',
 ('The band performed acoustically for the small audience.','乐队为小群观众作了原声演出。'),('The studio was acoustically treated to reduce reflections.','录音室做了声学处理，以减少声音反射。'))
R('B3039','听觉来源的词族，连接声学研究、场所效果与原声音乐','ACOUST-：先想声音怎样被听见','acoustic → acoustics、acoustical → acoustically。',
 '声学研究是学科，大厅声音条件是特性，原声演奏是音乐方式。词形相近，先靠名词、形容词、副词和搭配分工。',
 'akouo 听 → akoustikos → acousticus → acoustic；-s 学科、特性，-al 形容词扩展，-ally 副词。',
 [['声音性质、学科与方式','acoustic · acoustics · acoustical · acoustically']],
 'acoustics 的学科义与场所效果义谓语习惯不同；acoustic guitar 也可通过麦克风扩音。',
 'The acoustical engineer checked the hall’s acoustics before the band played acoustically.\n\n乐队作原声演出前，声学工程师检查了大厅的音响效果。','acoustic acoustics acoustical acoustically')
Fo=[['中古英语 fonnen、fonned → fond','旧义愚傻；经过分疼爱走向喜爱、深情'],['fond + -ly、-ness；fond 一族 + -le → fondle','深情方式、喜爱之情；反复轻抚'],['fondle + -ing → fondling','抚摸动作；另有旧 fond + -ling 人物名']]
W('fond','英 /fɒnd/；美 /fɑːnd/','喜爱的、深情的；〔旧或固定用法〕天真的、空想的',
 '想到某人、某物心里就柔软，是 fond 的常用感觉。be fond of cats 喜欢猫，fond memories 带感情的回忆；它早年却曾说人愚傻。',
 '中古英语 fonned 是 fonnen 愚傻的分词形式，后来变 fond。词义经“疼爱得过分”转到深情、喜爱，现代常用义已不必带愚傻判断。',Fo[:1]+[['过分疼爱 → fond 喜爱、深情','现代常见于 fond of、fond memories 等']],
 'be fond of 喜欢，fond memories 美好而深情的回忆，a fond farewell 深情告别；a fond hope 有时指不切实际的希望。',
 'be fond of；fond memories；a fond farewell。',
 'fond of 后接名词或 -ing；fond hope 的旧有天真义与 fond memories 的深情义要按搭配读。',
 ('She is fond of old detective stories.','她喜欢老派侦探故事。'),('He has fond memories of their summers by the sea.','他深情怀念他们在海边度过的那些夏天。'),sources=['https://en.wiktionary.org/wiki/fond#English','https://www.etymonline.com/word/fond'])
W('fondly','英 /ˈfɒndli/；美 /ˈfɑːndli/','深情地、亲切地；〔旧或特定语境〕天真地',
 'fond 是心里带着喜爱，fondly 就说回忆、注视、称呼时带着这份感情。remember fondly 是回想起来仍觉得亲切。',
 'fond + -ly，中古英语已有相应形式；常用承深情义，也保留较旧的愚傻、天真用法。',Fo[:1]+[['fond + -ly → fondly','带喜爱、柔情的方式；旧义天真地']],
 'remember someone fondly 深情怀念某人，look fondly at 亲切注视，fondly known as 被亲切称作。',
 'remember fondly；look fondly at。',
 'fondly remembered 常带正面感情；fondly imagine 在某些文体中却可能讽刺想得过于天真。',
 ('They remembered their first teacher fondly.','他们深情怀念第一位老师。'),('She looked fondly at the old photograph.','她深情地望着那张老照片。'))
W('fondness','英 /ˈfɒndnəs/；美 /ˈfɑːndnəs/','喜爱、钟爱；深情',
 '把 fond 那种心里亲近、喜欢的感觉当成一份感情来说，就是 fondness。a fondness for something 是对它有偏爱。',
 'fond + -ness，性质、情感名词，中古英语已有相应形式。现代多承喜爱义。',Fo[:1]+[['fond + -ness → fondness','喜爱这一情感、偏好']],
 'a fondness for music 对音乐的喜爱，speak with fondness 带着深情谈起。',
 'a fondness for；with great fondness。',
 'fondness 通常是温和亲近、偏爱，不必达到强烈迷恋。',
 ('He developed a fondness for gardening.','他渐渐喜欢上园艺。'),('She spoke of the town with great fondness.','她满怀深情地谈起那座小镇。'))
W('fondle','英 /ˈfɒndəl/；美 /ˈfɑːndəl/','爱抚、轻抚；抚弄',
 '手反复温柔地摸、轻轻摩挲，就是 fondle 的动作。可写抚摸动物，也能指亲密或性的抚弄，含义要看接触部位、关系和语境。',
 '联系 fond 喜爱，加古老反复动作后缀 -le，或接同族旧动词；由疼爱走到爱抚、轻触。',Fo[:1]+[['fond 一族 + -le → fondle','疼爱、反复轻抚']],
 'fondle a pet 轻抚宠物，fondle someone’s hand 轻抚某人的手。',
 'fondle a cat；fondle someone’s hand。',
 'fondle 比普通 touch 更强调抚摸、亲密性质；报道里也可能描述不受欢迎的性接触，不能只凭词源认定双方愿意。',
 ('She fondled the cat as it lay in her lap.','猫趴在她腿上，她轻轻抚摸着它。'),('He fondled the smooth pebble in his pocket.','他在口袋里轻轻摩挲那块光滑卵石。'))
W('fondling','英 /ˈfɒndlɪŋ/；美 /ˈfɑːndlɪŋ/','抚摸、爱抚；fondle 的现在分词',
 'fondle 是轻抚，fondling 可以把正在抚摸的动作带进句子，也可把这种接触当作活动来谈。',
 '常见形式为 fondle 去 e + -ing。另有旧名词 fond + -ling，指受宠爱的人或宠物；这两种边界不同，不能一概把末尾看成 -ling。',Fo[:2]+[['fondle + -ing → fondling','正在轻抚；抚摸活动']],
 'be fondling a pet 正在轻抚宠物，gentle fondling 轻柔爱抚；涉及人的身体接触时须结合场景读。',
 'fondling a pet；gentle fondling。',
 '现代常见动作义按 fondle + -ing 拆；旧人物名才按 fond + -ling 拆。',
 ('She sat by the window, fondling the dog’s ears.','她坐在窗边，轻抚狗的耳朵。'),('The cat settled down under his gentle fondling.','在他轻柔的抚摸下，猫安静下来。'))
R('B4264','由旧日愚傻、溺爱，转到温柔喜爱与轻抚','FOND：心里喜欢，眼神、回忆、手势都能带着感情','fond → fondly、fondness；fondle → fondling。',
 '深情回忆是态度，喜爱是感情，爱抚是动作。旧词义提醒演变路径，现代例句则按实际搭配理解。',
 'fonnen、fonned → fond；-ly 方式，-ness 情感、性质；-le 动作，fondle 去 e + -ing。',
 [['喜爱及其方式、情感','fond · fondly · fondness'],['轻抚动作及进行形式','fondle · fondling']],
 'fondling 的动作义按 fondle + -ing；fond hope 有时仍带天真、不切实际的旧义。',
 'Remembering the dog fondly, she recalled its fondness for gentle fondling.\n\n她深情想起那只狗，也想起它多爱被人温柔抚摸。','fond fondly fondness fondle fondling')
J=[['jerk 急拉、突然动作','早期 yerk 等形式的联系有讨论，来源未完全确定'],['jerk + -y → jerky','一顿一顿、不平稳的'],['克丘亚语 ch’arki → 西班牙语 charqui → jerky','干肉名称；与动作形容词另一路']]
W('jerk','英 /dʒɜːk/；美 /dʒɝːk/','猛拉、突然一动；急促动作；讨厌鬼、混蛋',
 '车突然一顿、手猛地一拉，就是 jerk 的动作画面。骂人 a jerk 则说对方讨厌、自私或没礼貌，已经是人物评价。',
 '动作词的早期来源未定，可比较 yerk 等急拉词形。猛拉、一顿名词接动作材料；讨厌者的人物义来路另有争议，不能直接画成由突动义顺推。干肉、牙买加风味的同形词另分食物来源。',J[:1]+[['急促动作的名词；另有来路有争议的人物贬称','猛拉、一顿；讨厌者人物义不作确定的单线派生']],
 'jerk the door open 猛拉开门，with a jerk 猛地一动，Don’t be a jerk. 别那么混蛋、别惹人讨厌。',
 'with a jerk；jerk backwards；a rude jerk。',
 '人物义带冒犯色彩；jerk a rope 描述动作，并不在评价绳子讨厌。',
 ('The bus stopped with a jerk.','公交车猛地一顿停住了。'),('Being tired is no excuse to act like a jerk.','累了也不是待人粗鲁、惹人讨厌的理由。'))
W('jerky','英 /ˈdʒɜːki/；美 /ˈdʒɝːki/','动作不平稳、一顿一顿的；肉干',
 '画面一跳一跳、手臂一顿一顿，是 jerky 的形容词。零食袋上的 beef jerky 是牛肉干，来自另一种语言的干肉名称。',
 '形容词 jerk 急动 + -y；名词经西班牙语 charqui 借自克丘亚语 ch’arki 干肉。两路同形，不按猛拉肉条来编词源。',J,
 'jerky movements 不连贯的动作，jerky video 卡顿跳动的视频，beef jerky 牛肉干。',
 'jerky movement；jerky footage；beef jerky。',
 'smooth movement 平滑连续，jerky movement 突然停动、衔接不顺；肉干名词不评价食物会不会抖。',
 ('The old camera produced jerky footage.','旧摄像机拍出的画面一顿一顿。'),('He packed some beef jerky for the journey.','他带了些牛肉干路上吃。'),sources=['https://en.wiktionary.org/wiki/jerky#English','https://www.etymonline.com/word/jerky'])
R('B2811','突然而急促的动作，与干肉借名分两路','JERK：猛地一拉，动作就不连贯；肉干另有来源','jerk → jerky〔动作性质〕；charqui → jerky〔肉干〕。',
 '用动作画面记猛拉、顿挫，再把零食袋的肉干单独接回美洲原住民语言。相同拼写不必分享一个故事。',
 'jerk 来源未定；jerk + -y → jerky；ch’arki → charqui → jerky 为食物名支线。',
 [['急促动作及性质','jerk · jerky']],
 'jerky 形容词与肉干名词不同源；a jerk 人物名带贬义。',
 'The jerky ride ended with a sudden jerk.\n\n颠顿不稳的行程以猛地一顿结束了。','jerk jerky')
M=[['拉丁 mobile vulgus 易变的人群 → 英语 mobile → mob','近代英语的缩短人物集合名'],['人群 → 拥挤围上、犯罪集团等','mobster 组织犯罪成员；游戏 mob 另由 mobile 缩短']]
W('mob','英 /mɒb/；美 /mɑːb/','喧闹或失控的人群；犯罪集团；蜂拥围住；〔游戏〕怪物、非玩家角色',
 '一群人挤作一团、情绪上来，不再只是安静的人数总和，常叫 mob。动词 mob 是一窝蜂围上去；the mob 在一些语境中指有组织犯罪集团。',
 '近代英语把 mobile 缩短为 mob，后者接拉丁 mobile vulgus 易变的人群。游戏用法则由早期 mobile 活动角色等名称缩短，不按 man or beast 的倒造缩写解释。',M,
 'an angry mob 愤怒人群，be mobbed by fans 被粉丝蜂拥围住，the mob 犯罪集团；澳新等语境还可中性指一群人、动物。',
 'an angry mob；mob the entrance；be mobbed by fans。',
 '普通英语 mob 常比 crowd 带更强的混乱、威胁感；地区用法与游戏义不必有相同贬义。',
 ('An angry mob gathered outside the building.','愤怒的人群聚集在楼外。'),('Fans mobbed the singer as she left the theatre.','歌手离开剧院时，粉丝蜂拥围住她。'),sources=['https://en.wiktionary.org/wiki/mob#English','https://www.etymonline.com/word/mob'])
R('B4376','近代缩短的人群词，再到围聚与犯罪集团人物','MOB：人挤成一团，群体行动与普通人数不同','mob → mobster；游戏 mob 也有 mobile 缩短的独立背景。',
 '人群可能喧闹失控，粉丝也能因蜂拥而上作动词 mob。mobster 特别联系有组织犯罪，不能泛指所有围观者。',
 'mobile vulgus → mobile → mob；-ster 人物名；游戏 mob 另接 mobile 活动角色名称。',
 [['人群、行为与犯罪集团成员','mob · mobster']],
 'mobster 不是所有人群成员；游戏 mob 不按现代倒造的英文首字母故事解释。',
 'The article distinguishes an angry mob from an organised group of mobsters.\n\n文章区分了愤怒人群与有组织犯罪成员组成的集团。','mob mobster')
G=[['古英语 goma 腭、口腔部分 → gum','牙龈；常用复数 gums'],['另一支：埃及、希腊 kommi → 拉丁 gummi → 法语 gome → gum','植物胶、黏性物 → 胶、口香糖'],['gum + -y、ball 等','gummy 黏胶般的；gumball 球形口香糖；牙龈义也可加 -y']]
W('gum','/ɡʌm/','牙龈；树胶、胶；口香糖；用胶粘住',
 '牙齿周围那圈肉是 gums；嘴里嚼的 chewing gum 则接黏性树胶、胶状物的另一来源。刚好都在嘴里常见，也不能把两条历史合成一条。',
 '牙龈义承古英语 goma；胶义经法语 gome、拉丁 gummi，联系希腊 kommi 与更早埃及胶名。动词用胶粘、使堵塞接胶这一支。',G[:2],
 'the teeth and gums 牙齿与牙龈，chewing gum 口香糖，gum up a mechanism 黏住、卡住机构。',
 'chewing gum；healthy gums；gum up。',
 '牙龈常用复数 gums；口香糖常不可数，按片说 a piece of gum。',
 ('The diagram labels the teeth and gums.','图上标出了牙齿和牙龈。'),('He offered her a piece of chewing gum.','他递给她一片口香糖。'))
W('gummy','/ˈɡʌmi/','黏胶状的、黏的；软糖；露出牙龈的',
 '糖浆干成黏糊糊一层，是 gummy 的胶状义；gummy smile 却要回牙龈那一支，描述笑时露出的牙龈。',
 'gum + -y，双写 m。胶与牙龈两种 gum 都能各自产生形容词；软糖名词还受德语 Gummi 胶、橡胶这一名称影响。',G[:2]+[['gum + -y → gummy；软糖名词受德语名称影响','黏胶般的；露牙龈的；软糖']],
 'a gummy residue 黏胶残留物，gummy sweets 软糖，a gummy smile 露牙龈的笑。',
 'gummy sweets；a gummy residue；a gummy smile。',
 'gummy smile 与 gummy sweets 的 gum 来源分支不同，读句子时让后面的名词帮你选义。',
 ('The label left a gummy residue on the jar.','标签在罐子上留下黏胶残渣。'),('She bought a packet of gummy sweets.','她买了一包软糖。'))
W('gumball','英 /ˈɡʌmbɔːl/；美 /ˈɡʌmbɔːl/','球形口香糖；〔植物〕某些胶树的球形果实',
 '把 chewing gum 做成圆球，再包一层硬糖衣，就是常见 gumball。名字直接给出内容物与外形。',
 'gum 口香糖 + ball 球。另有指某些胶树球形果实的用法，前项接树名分支。',G[1:2]+[['gum + ball → gumball','球形口香糖；另可依树名指球果']],
 'a gumball machine 球形口香糖售卖机，a colourful gumball 彩色口香糖球。',
 'a gumball machine；a round gumball。',
 'gumball 常见糖果是可咀嚼的口香糖球，gummy candy 通常是软糖，两种食品不能只按都圆都甜来混同。',
 ('A gumball machine stood near the shop entrance.','商店门口附近放着一台球形口香糖售卖机。'),('He put a bright red gumball in his pocket.','他把一颗鲜红的口香糖球放进口袋。'))
R('B3645','牙龈与植物胶两条来源，现代词形交叉出现','GUM：嘴里的牙龈、嚼的胶，名称来自不同历史','gum → gummy；胶、口香糖支 → gumball、bubblegum；gumshoe 接胶底鞋。',
 '牙龈是身体部位，植物胶是材料。gummy 两支都能派生，读笑容、糖果、残渣这些搭配就能知道是哪一路。',
 'goma → gum 牙龈；kommi → gummi → gome → gum 胶；-y 双写 m，ball 球。',
 [['两支原词与性质','gum · gummy'],['口香糖、胶底相关复合','gumball · bubblegum · gumshoe']],
 '常见 Begum 女性尊称来自波斯语、突厥语头衔，不由胶义派生；另有罕见 be- + gum 动词同形。',
 'The gumball machine stood beside shelves of gummy sweets and bubblegum.\n\n球形口香糖售卖机放在货架旁，架上有软糖和泡泡糖。','gum gummy gumball bubblegum gumshoe')
ROOTS[-1]['exclude']['begum']='常见女性尊称接波斯、突厥语头衔；另有罕见 be- + gum 涂胶动词同形，分开看。'
Wi=[['古英语 wrist → 中古英语 wrist → wrist','手腕；联系日耳曼转动词族'],['身体部位名 + 物品名','wristband 腕带；wristwatch 腕表']]
W('wrist','/rɪst/','手腕、腕部',
 '手和前臂接起来、手表常戴着的地方，是 wrist。它的远亲词族与转动有关，用手掌活动的画面帮助记，但别把身体动作硬说成无限旋转。',
 '承古英语 wrist，经中古英语延续；联系日耳曼扭、转词族。现代开头 w 不发音，读 /rɪst/。',Wi,
 'on the wrist 在手腕上，a flick of the wrist 手腕轻轻一甩，a slap on the wrist 轻微惩戒。',
 'a wristwatch；a wristband；a flick of the wrist。',
 'wrist 是腕，ankle 是踝；a slap on the wrist 常比喻处罚很轻，不必真的拍手腕。',
 ('She wore a silver watch on her wrist.','她手腕上戴着一块银色手表。'),('He opened the fan with a flick of his wrist.','他手腕一甩，打开了扇子。'))
R('B3860','腕部名称，放在复合词前限定佩戴位置','WRIST：手表、腕带戴在哪里，就看这个部位','wrist → wristband、wristwatch。',
 '先认手与前臂之间的腕，再把腕带、腕表按部位与物品组合。开头 w 保留在拼写里，不另发音。',
 '古英语 wrist → wrist；wrist + band，wrist + watch。',
 [['身体部位及所戴物品','wrist · wristband · wristwatch']],
 'a slap on the wrist 通常比喻轻微处罚；wrist 开头 w 不发音。',
 'The wristband sat just above her wristwatch.\n\n腕带戴在腕表上方一点。','wrist wristband wristwatch')
if __name__=='__main__':save('continuation_20261030_mx',ROOTS,WORDS)
