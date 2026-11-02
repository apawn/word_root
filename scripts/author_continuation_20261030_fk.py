"""Breath, chat, noise, conduct and tank: air, talk, signals and containers."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
B=[['古英语 brǣþ → 中古英语 breth、breeth → breath','气味、呼出气等旧义 → 呼吸、气息'],['中古英语 brethen → breathe','以 breath 为基础形成相应呼吸动词'],['直接性质派生','breathless 缺气、屏息般；breathy 带气息声的']]
W('breath','/breθ/','呼吸、气息；一口气；微风、细微气息',
 '一吸一呼里那口气；说 hold your breath，是把气憋住。这里是名词，末尾 /θ/ 不振动声带，元音也短。',
 '继承古英语 brǣþ，早期含气味、呼气、蒸气等义。名词 breath 与后来形成的 breathe 动词同族，却不只是随手多写一个 e 还同音。',B[:2],
 'take a deep breath 深吸一口气，hold your breath 屏住呼吸，out of breath 上气不接下气，a breath of fresh air 一口新鲜空气、令人耳目一新的事物。',
 'take a breath；hold your breath；out of breath；under your breath。',
 'breath /breθ/ 名词，breathe /briːð/ 动词；breath 不等于 breadth 宽度，后者多一个 /d/。',
 ('She took a deep breath before speaking.','她开口前深吸了一口气。'),('He was out of breath after climbing the stairs.','他爬完楼梯后上气不接下气。'))
W('breathe','/briːð/','呼吸；呼出；轻声说；让空气通过',
 '名词 breath 是一口气，动词 breathe 是把气吸进、呼出的动作。说话轻得像一口气，也能说 breathe the words。',
 '来自中古英语 brethen，以相应 breath 名词为基础形成动词。长元音 /iː/ 与末尾浊辅音 /ð/ 都不同于 breath；过去式 breathed 通常 /briːðd/。',B[:2]+[['英语 breathe 的用法扩展','呼吸、轻轻吐字；织物透气等']],
 'breathe deeply 深呼吸，breathe in/out 吸气、呼气，let the fabric breathe 让面料透气，breathe a sigh of relief 松一口气。',
 'breathe in/out；breathe deeply；breathe a sigh of relief；barely breathe。',
 'breathe 动作，breath 一口气；breathes /briːðz/ 是第三人称，breaths /breθs/ 是名词复数，不只字母位置不同。',
 ('We stopped to breathe the fresh mountain air.','我们停下来呼吸山里的新鲜空气。'),('She breathed a sigh of relief when the lights came back on.','灯重新亮起时，她松了一口气。'),
 sources=['https://www.etymonline.com/word/breathe','https://en.wiktionary.org/wiki/breathe#English'])
W('breathless','/ˈbreθləs/','气喘吁吁的；屏息般激动的；急促兴奋的',
 '跑完楼梯气接不上，或激动得仿佛忘了呼吸；-less 给出缺气的感觉，但日常不每次都表示完全停止呼吸。',
 'breath 气息 + -less 缺少，先抓缺气、喘不过气的性质，再看兴奋、叙述语气等比喻。',B[:1]+[['breath + -less → breathless','喘不过气；像屏息般急切、激动']],
 'leave someone breathless 让人喘不过气、惊叹，breathless excitement 屏息般兴奋，a breathless account 急促激动的叙述。',
 'leave someone breathless；breathless excitement；a breathless account。',
 'breathless 可说人的状态或叙述语气，breathtaking 常评价景色等令人惊叹；两者都借气息，却不互换所有搭配。',
 ('The climb left us breathless.','爬坡让我们气喘吁吁。'),('She gave a breathless account of the match.','她急促兴奋地讲了比赛经过。'))
W('breathy','/ˈbreθi/','带气息声的、气声的',
 '说话或唱歌时，声音里能听出呼出的气，好像字音旁边还裹着一层轻轻的哈气声。',
 'breath + -y，形成带气息特点的形容词。不是 breathe 动词直接照读，所以这里仍是短元音和 /θ/。',B[:1]+[['breath + -y → breathy','声音带可听见的气息']],
 'a breathy voice 带气声的嗓音，breathy singing 气声演唱，a breathy whisper 带气息的低语。',
 'a breathy voice；breathy singing；a breathy whisper。',
 'breathy 描述音质，breathless 描述缺气或急切状态；一个人能有 breathy voice，却并没有刚跑完步。',
 ('The singer has a soft, breathy voice.','这位歌手的嗓音柔和，带着气声。'),('She answered in a breathy whisper.','她用带气息声的低语回答。'),
 sources=['https://www.merriam-webster.com/dictionary/breathy','https://en.wiktionary.org/wiki/breathy#English'])
R('B2747','一口气、呼吸动作和气息声分清','BREATH /breθ/：气；BREATHE /briːð/：呼吸','breath → breathe；breathless 缺气、急切；breathy 带气声；breathtaking 令人惊叹。',
 'breathed 作 breathe 过去式通常 /briːðd/；较冷门的旧语音形容词另有 /breθt/，不拿后者去教普通“呼吸过了”的读音。',
 'brǣþ → breath；中古英语 brethen → breathe；breath + -less/-y；breath + taking 组成惊叹比喻。',
 [['气息与呼吸动作','breath · breathe'],['状态、声音与引起感受','breathless · breathy · breathtaking']],
 'breath/breathe 元音与清浊都变；breaths/breathes 名词复数和动词三单；breathy/breathless 音质与缺气状态。',
 'After the climb, she paused to catch her breath and breathe more slowly.\n\n爬完坡后，她停下来喘口气，慢慢恢复呼吸。','breath breathe breathless breathy breathtaking')
ROOTS[-1]['exclude']['breathed']='普通 breathe 过去式及其 /briːðd/ 已在正文解释；独立 breath + -ed 的旧形容词 /breθt/ 较冷门，暂不单列。'
C=[['中古英语 chateren 等拟声词 → chatter','叽叽喳喳、快速细碎发声'],['chatter 缩短 → chat','较轻松、随意地聊'],['现代派生、组合','chatty 爱聊天；chatbot 自动对话程序']]
W('chatter','英 /ˈtʃætə/；美 /ˈtʃætər/','喋喋不休、叽喳声；牙齿打战；快速碎响',
 '一小串声音接着一小串，不停往外冒；可以是人说个不停、鸟叽喳，也可以是冷得牙齿咯咯响。',
 '来自中古英语 chateren、chiteren 等带拟声性质的形式。历史上 chatter 比缩短后的 chat 早，不是现代 chat + -er 表示聊天的人。',C[:2],
 'chatter away 聊个不停，teeth chatter 牙齿打战，background chatter 背景里的人声，the chatter of birds 鸟的叽喳声。',
 'chatter away；teeth chatter；background chatter；the chatter of birds。',
 'chatter 侧重连续细碎、可能烦人的声音，chat 通常只是随便聊聊；聊天的人通常说 someone chatting、a talker 等，不直接按 chat+-er 猜 chatter。',
 ('The children chattered all the way home.','孩子们一路叽叽喳喳地聊回家。'),('His teeth began to chatter in the cold.','天一冷，他的牙齿开始打战。'))
W('chat','/tʃæt/','聊天、闲谈；一次聊天；在线聊天',
 '不端起讲台架子，就和人轻松说几句；可以当面，也可以隔着屏幕打字、说话。',
 '由较长的 chatter 缩短而来，后来稳定为熟人式轻松交谈。字短不代表历史一定比长词早；电脑聊天只是后来使用的媒介。',C[:2],
 'have a chat 聊一会儿，chat with someone 和某人聊，chat about work 聊工作，a group chat 群聊。',
 'have a chat；chat with；chat about；a group chat。',
 'chat 通常轻松随意，discuss 常带围绕问题认真讨论的感觉；a chat 也可为了谈一件正事，不保证完全没目的。',
 ('We had a quick chat over coffee.','我们喝咖啡时简短聊了几句。'),('I chatted with my sister online.','我和姐姐在网上聊了天。'),
 sources=['https://www.etymonline.com/word/chat','https://en.wiktionary.org/wiki/chat#English'])
W('chatty','/ˈtʃæti/','爱聊天的、健谈的；像聊天一样随意的',
 '人很容易打开话匣子，文章也能像朋友坐在旁边聊天；不一定是正式发表长篇演说。',
 'chat + -y，拼写把 t 双写为 chatty。-y 表有聊天这种特点；不是另有一个词根 chatt。',C[:2]+[['chat + -y → chatty','爱聊天；聊天式的语气']],
 'a chatty child 健谈的孩子，a chatty style 聊天式文风，feel chatty 想多聊几句。',
 'a chatty child；a chatty style；feel chatty。',
 'chatty 可以亲切，也可能嫌太爱说；talkative 较直接说话多，chatty 常带随意交谈的气氛。',
 ('She was unusually chatty this morning.','她今天早晨格外健谈。'),('The guide uses a warm, chatty style.','指南采用了亲切、像聊天一样的文风。'))
W('chatbot','英 /ˈtʃætbɒt/；美 /ˈtʃætbɑːt/','聊天机器人、自动对话程序',
 '用户发一句，它回一句，界面像聊天；bot 说软件代理，不要求背后站着一个金属身体的机器人。',
 'chat 聊天 + bot〔robot 的缩短形式〕，与较早 chatterbot 名称相关。不是 chat 先变出 robot，两个成分并列组成名称。',C[:2]+[['chat + bot → chatbot；另有较早 chatterbot','通过对话交互的软件程序']],
 'a customer service chatbot 客服聊天机器人，talk to a chatbot 与聊天机器人对话，a chatbot response 对话程序的回复。',
 'a customer service chatbot；talk to a chatbot；a chatbot response。',
 'chatbot 说交互形式和程序角色，不保证一定用现代大模型；bot 的范围也比聊天程序大。',
 ('The website uses a chatbot to answer common questions.','网站用聊天机器人回答常见问题。'),('The chatbot asked which product I needed help with.','聊天机器人问我需要哪个产品的帮助。'))
R('B2788','细碎发声的旧词缩短成轻松聊天','CHATTER → CHAT：长词先来，短词后缩','chatter 叽喳、牙齿打战 → chat 闲聊 → chatty；chat + bot → chatbot。',
 '不要因为 chatter 较长就把它写成 chat 加人物后缀。现代聊天可线上线下；chatbot 的 bot 也可以纯软件。',
 'chateren 等拟声形式 → chatter → 缩短 chat；chat + -y → chatty；chat + bot → chatbot。',
 [['声音旧词与聊天短词','chatter · chat'],['聊天性质与程序','chatty · chatbot']],
 'chatter/chat 连续碎响与轻松交谈；chatty/talkative 氛围和话多的侧重；bot 不一定实体机器人。',
 'The chatty visitor began to chatter while we waited for the chatbot’s reply.\n\n我们等聊天机器人回复时，那位健谈的访客开始聊个不停。','chatter chat chatty chatbot')
N=[['古法语 noise → 中古英语 noise、noyse → noise','喧闹、争吵、声响等；更早来源未定'],['英语声音与信号引申','声音、噪声；干扰有用信号的信息'],['英语派生','noisy 吵闹、噪点多；noiseless 无声、低声']]
W('noise','/nɔɪz/','声音、噪声；干扰、噪点',
 '想听清一个声音，却有别的声音挤进来；借到照片、数据里，不想要的杂点和干扰也叫 noise。',
 '由古法语 noise 的喧闹、争吵等用法传入，更远来源有不同说法未定。不直接断言它就是拉丁 nausea 恶心变来的。',N,
 'make a noise 发出声音，background noise 背景噪声，reduce image noise 降低图像噪点，signal and noise 信号与噪声。',
 'make a noise；background noise；reduce noise；signal and noise。',
 'noise 常是不希望有的声音，但 a noise 也可中性说听见一声；数字照片里的 noise 不会真的从照片里吵出来。',
 ('I heard a strange noise outside.','我听见外面有个奇怪的声音。'),('The software reduces noise in dark photographs.','软件能减少暗光照片里的噪点。'),
 sources=['https://www.etymonline.com/word/noise','https://en.wiktionary.org/wiki/noise#English'])
W('noisy','/ˈnɔɪzi/','吵闹的；含噪声、噪点多的',
 '耳朵里杂声多，或数据、图像里杂点多；重点是干扰多，不一定每次都在说音量特别大。',
 'noise + -y，去掉末尾 e 为 noisy；仍读 /z/。',N[:2]+[['noise + -y → noisy','带很多声响、干扰的性质']],
 'a noisy street 吵闹街道，noisy neighbours 吵闹邻居，a noisy image 噪点多的图像，noisy data 含较多干扰的数据。',
 'a noisy street；noisy neighbours；a noisy image；noisy data。',
 'loud 通常说声音大，noisy 常说杂声多、让人烦或信号脏；小音量持续嗡嗡声也可能讨厌。',
 ('The restaurant was too noisy for a quiet conversation.','餐馆太吵，没法安静交谈。'),('The camera produced a noisy image in low light.','相机在低光下拍出了噪点很多的照片。'))
W('noiseless','/ˈnɔɪzləs/','无声的、几乎不出声的',
 '动作做了，却没有让你听见明显声音；日常说法也可能只是很安静，未必实验测得绝对零声音。',
 'noise + -less，缺少噪声；这里保留 e 的拼写，不能按 noisy 的去 e 规则一律照搬。',N[:2]+[['noise + -less → noiseless','无声、低噪声的']],
 'a noiseless movement 无声动作，noiseless operation 安静运行，a noiseless door 安静开合的门。',
 'a noiseless movement；noiseless operation；almost noiseless。',
 'noiseless 偏没有可闻噪声，quiet 范围较宽；silent 还可以说人不说话，而 noiseless person 并不是沉默寡言的最普通说法。',
 ('The door opened with an almost noiseless movement.','门几乎无声地打开了。'),('The brochure promises noiseless operation.','宣传册承诺机器运行安静。'))
R('B3351','声响到干扰，不一定每个 noise 都很大声','NOISE：想要的信息之外，混进来的杂声杂点','noise → noisy；noiseless 说缺少可闻噪声。照片和数据也用噪声比喻。',
 'a noise 有时只是某个声响；noisy image 是图像有噪点，不是图像自己在叫。更远词源未定，不编晕船演化故事。',
 '古法语 noise → noise；noise + -y → noisy；noise + -less → noiseless。',
 [['声响与干扰基础','noise'],['噪声多少的性质','noisy · noiseless']],
 'noisy/loud 杂声与音量；noiseless/quiet/silent 具体搭配、侧重点不同。',
 'The noisy fan added background noise to the recording.\n\n吵闹的风扇给录音添了背景噪声。','noise noisy noiseless')
W('conductance','/kənˈdʌktəns/','电导；传导能力',
 '电阻像给电流设阻碍，电导从另一面问：这段路径让电流通过有多容易。是一个量，不是泛指“导电这件事”。',
 'conduct 传导 + -ance，形成量、性质名词，十九世纪出现。接 conduct 的物理传导一支，不接人的品行一支。',
 [['拉丁 condūcere、conductus 词族 → conduct','带领、引导；英语中发展传导等用法'],['conduct + -ance → conductance','传导能力、电导这一量']],
 'electrical conductance 电导，measure conductance 测电导。通常电导 G = 1/R，对应电阻倒数；常用单位 siemens，符号 S。',
 'electrical conductance；measure conductance；high conductance。',
 'conductance 指具体对象的电导，conductivity 常说材料电导率；对象长度、粗细改变时，两者不能直接视为同一个量。',
 ('The experiment measured the conductance of the wire.','实验测量了这段导线的电导。'),('A lower resistance means a higher conductance.','电阻越低，电导越高。'),
 sources=['https://www.merriam-webster.com/dictionary/conductance','https://en.wiktionary.org/wiki/conductance#English'])
R('B4234','引导、做事与让热电通过各有搭配','CONDUCT：带着走，导过去，或一个人的行为','conduct、misconduct 接行为等；conductive、conduction、conductance 接传导。',
 '名词 conduct 品行常前重音，动词 conduct 引导、进行、传导常后重音。conductance 后重音，专门量义别和 conduction 过程混用。',
 '拉丁 condūcere、conductus 等 → conduct；mis- + conduct；相关传导形容词、过程名词；conduct + -ance → conductance。',
 [['行为、进行与不当行为','conduct · misconduct'],['传导性质、过程与量','conductive · conduction · conductance']],
 'conduct 名词动词重音；conduction/conductance 传导过程与量；conductance/conductivity 对象电导与材料电导率。',
 'The material conducts electricity, but this experiment measures the conductance of one specific sample.\n\n这种材料能导电，而这次实验测的是某个具体样品的电导。','conduct misconduct conductive conduction conductance')
T=[['葡萄牙语 tanque 与南亚相关水池词的传播背景 → tank','水池、储水容器；更远路径有不同分析'],['英语储罐用法 → 军用履带车辆 tank','一战保密命名借用了容器名称，后来固定为坦克'],['英语派生与口语引申','tanker 罐装运输工具；antitank 反坦克；tank 暴跌、失败等']]
W('tank','/tæŋk/','箱、罐、槽；坦克；暴跌、惨败；故意输掉',
 '一支是装水、燃油等的容器；坦克车名借这类容器名称作早期保密称呼。口语说 sales tanked 则是销量猛跌，不是销量被塞进油箱。',
 '容器名涉及葡萄牙语 tanque 与南亚词传播背景，具体远源有不同分析。履带战车名是一次特殊历史借名；失败动词义的确切比喻来源未定。',T,
 'a water tank 水箱，a fuel tank 油箱，a battle tank 坦克，sales tanked 销量暴跌，tank a match 故意输比赛。',
 'a water tank；a fuel tank；an empty tank；sales tanked。',
 'tank 罐与坦克有关历史借名，但 tanker 通常是罐运工具；口语 tanked 也可说醉了，要看句子。',
 ('The water tank was nearly empty.','水箱快空了。'),('Ticket sales tanked after the bad reviews.','差评出来后，票房销量大跌。'),
 sources=['https://www.etymonline.com/word/tank','https://www.merriam-webster.com/dictionary/tank','https://en.wiktionary.org/wiki/tank#English'])
W('tanker','英 /ˈtæŋkə/；美 /ˈtæŋkər/','油轮、罐车；罐装运输船或飞机等',
 '带着大罐去运液体、气体，交通工具的名字抓住 tank 储罐；并不是单看 -er 就变成开坦克的士兵。',
 'tank 储罐 + -er，命名装罐运输的船、卡车，也用于空中加油机等。取容器、运输装备一支。',T[:1]+[['tank + -er → tanker','带储罐运输的工具；相关供油飞机']],
 'an oil tanker 油轮，a road tanker 公路罐车，a tanker aircraft 空中加油机。',
 'an oil tanker；a road tanker；a tanker aircraft。',
 'tanker 多运液体、气体，不只石油；tank crew 才通常说坦克乘员，不能按词尾把每辆 tanker 译成坦克兵。',
 ('The tanker carried fuel to the island.','运输船把燃油运到岛上。'),('A road tanker delivered milk to the factory.','一辆公路罐车把牛奶送到工厂。'))
W('antitank','英 /ˌæntiˈtæŋk/；美 /ˌæntiˈtæŋk/','反坦克的',
 '用途是对付坦克车辆；anti- 指对抗对象，不是反对储水罐，也不自动说明具体用什么技术。',
 'anti- 对抗 + tank 坦克，组合形容词；也常写成 anti-tank，这里合写与分连字符写法指同一构词。',T[1:2]+[['anti- + tank → antitank','用于对抗坦克的性质']],
 'antitank weapons 反坦克武器，antitank defences 反坦克防御，an antitank obstacle 反坦克障碍。',
 'antitank weapons；antitank defences；an antitank obstacle。',
 'antitank 接 tank 车辆义；tanker 接容器运输义。同一个字根在不同组合里要选对分支。',
 ('The museum has a section on antitank defences.','博物馆有一个展区介绍反坦克防御。'),('The old map marks an antitank obstacle beside the road.','旧地图在路旁标出了一处反坦克障碍。'))
R('B3230','储罐名称被历史借给战车，再有口语义','TANK：容器、坦克和暴跌要看场景','tank 容器 → tanker 运输；tank 战车 → antitank；口语 tank 失败、猛跌另辨。',
 '一战借容器名作保密称呼，是能讲清的历史；tank 失败义却不宜编成战车必定冲下坡。词义关联的确定程度不同。',
 'tanque 等水池、容器传播背景 → tank；储罐名历史借给履带战车；tank + -er；anti- + tank。',
 [['基础同形用法','tank'],['罐装运输工具','tanker'],['对抗坦克的性质','antitank']],
 'tank/tanker 坦克与罐运工具别误译；tank 比赛故意输和销量暴跌要辨主语；tank 远源分析存在分歧。',
 'The tanker filled the fuel tank before leaving the depot.\n\n罐车离开车库前加满了油箱。','tank tanker antitank')
if __name__=='__main__':save('continuation_20261030_fk',ROOTS,WORDS)
