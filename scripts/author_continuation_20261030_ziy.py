"""Common digital words: blends, borrowed names and transparent extensions."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
BT='https://www.bluetooth.com/about-us/bluetooth-origin/'
def S(word,base):
 a=['https://en.wiktionary.org/wiki/'+word+'#English']
 if base in ['hashtag','webinar']:a.append('https://www.merriam-webster.com/dictionary/'+base)
 elif base=='bluetooth':a.append(BT)
 elif base=='spam':a+=['https://www.merriam-webster.com/dictionary/spam','https://www.etymonline.com/word/Spam']
 else:a.append('https://www.etymonline.com/word/'+base)
 if base=='webinar':a.append('https://www.etymonline.com/word/seminar')
 return a
EXISTING_ROOT_ADDITIONS={
 'C0755':dict(words='modem modems'.split(),label='modem：调制器与解调器的缩合名称',note='modem 缩合 modulator、demodulator 两个长词，保留调制、解调的功能关系；modulator 远接拉丁调节、度量词族，不是现代 mod 这个游戏短词加后缀 -em。'),
 'C1535':dict(words='avatar avatars'.split(),label='avatar：从神祇降世到虚拟形象',note='avatar 经印度斯坦语借入，向前接梵语降下、降世相关名词，ava- 向下 + 横渡、越过的词根材料，远处与 trans- 跨越同族；现代可指代表用户的虚拟形象，不是现代英语 trans 派生。'),
 'C1045':dict(words='pixel pixels emoji emojis'.split(),label='pixel 与 emoji：图像单位和图画字符的不同来路',note='pixel 接 pix 图片短称 + element 前部缩合，pix 是 pics 的变体，远接 picture。emoji 与图画比较，不由拉丁 pict 派生：它借日语 e 画 + moji 文字，和 emotion、emoticon 的相似拼写不等于同源。'),
 'A1698':dict(words='selfie selfies'.split(),label='self + -ie → selfie → selfies：自拍及复数',note='self 自己 + 口语名词后缀 -ie → selfie 自拍；现代 selfies 直接在已经写成 -ie 的词后加 s，不是把一个不存在的 selfy 当作实际来源。'),
 'B3864':dict(words='hashtag hashtags'.split(),label='hashtag → hashtags：用 # 标出的标签',note='hash 在这里指 # 符号，加 tag 标签 → hashtag；整体复数 hashtags。标签可帮助聚合内容，也能补充态度、评论，不仅有分类一种用途。'),
 'C1305':dict(words='webinar webinars'.split(),label='web + seminar → webinar：搬到网上的研讨活动',note='web 网络 + seminar 研讨活动缩合 → webinar，不把 -inar 拆成独立通用后缀。seminar 更远经德语接拉丁苗圃、培育场的比喻，后来有小组研习、讨论活动。'),
 'B4524':dict(words='upload uploads'.split(),label='upload → uploads：向服务器上传及上传项目',note='up 向上 + load 装载 → upload，网络里说把本地内容送往远端服务的方向；uploads 兼名词复数与第三人称单数动词，重音常有差别。'),
 'B2763':dict(words='Bluetooth'.split(),label='Bluetooth：蓝牙王的绰号借给连接技术',note='与 tooth 比较名字材料：Bluetooth 技术名借 Harald Bluetooth 的历史绰号，用统一、连接的形象命名。不是按牙齿颜色判断现代设备功能；正式品牌通常写 Bluetooth。'),
 'B2628':dict(words='phishing'.split(),label='fishing → phishing：用钓鱼画面说信息诱骗',note='phishing 是 fishing 的变形拼写，用诱饵引人上钩的画面说电子通信中的信息诱骗；ph 的选择常联系黑客词语习惯，但具体影响不能全当作定论。'),
 'B3374':dict(words='spam spammed spamming spammer spammers'.split(),label='spam → spammed、spamming；spammer → spammers',note='网络 spam 名称与 Monty Python 短剧中反复喊 Spam 淹没对话的形象有关，再用于垃圾消息、刷屏。spammed、spamming 双写 m 接完整后缀，spammer 加 -er 指发送者，再加 s。'),
}
MODEM=[['modulator 调制器 + demodulator 解调器 → modem','缩合两个长名称，概括双向信号转换功能'],['modem → modems','现代英语直接加复数 s；更远 modulate 接调节、度量词族']]
PIXEL=[['picture → pics、pix 图片短称；element 元素、构成单位','两块材料缩合为 pixel'],['pixel 像素 → pixels','图像可分解为许多小单位，不是把每个像素都当作一张完整照片']]
AVATAR=[['梵语向下、横渡词根材料 → 降下、神祇降世的名词','英语借为 avatar 神祇化身、具体体现'],['化身、具体体现 → 代表用户的虚拟形象','avatar + -s → avatars；网络用法借了代表、化身的关系']]
EMOJI=[['日语 e 画 + moji 文字 → emoji','原本就有图画字符的构词关系'],['英语借入 emoji → emojis','与 emoticon 的 emotion + icon 构词不同；复数也常见不变形式 emoji']]
WEBINAR=[['seminar 研讨活动，远接德语、拉丁苗圃与培育的词线','小组研究、讨论的场所与活动'],['web 网络 + seminar 缩合 → webinar → webinars','把研讨、讲座搬到网络上，现代复数加 s']]
SPAM=[['Spam 肉类罐头品牌 → 短剧中反复出现、淹没对话的词','网络用法借这种不请自来、铺天盖地的形象'],['spam 垃圾消息 → spam 动词大量发送、刷屏','动词变化、行为名词和发送者称呼继续形成']]
W('modem','英 /ˈməʊdem/；美 /ˈmoʊdəm/','调制解调器',
 'modem 像通信链路两端的“信号翻译员”：把数据变成适于传输的信号，再把收到的信号还原。名字把这两个功能缩在一起。',
 'modulator 调制器 + demodulator 解调器缩合为 modem；不是把所有长词完整相加。modulator 更远与调节、度量的词族相连。',MODEM,
 'a cable modem 是有线宽带调制解调器；an external modem 是外置调制解调器；a modem connection 是经调制解调器的连接。',
 'a cable modem；an external modem；a modem connection。',
 'modem 处理通信信号转换，router 路由器负责网络数据的转发；家用设备可把功能合在一个盒子里，两个词的核心仍不同。',
 ('The modem sits beside the router.','调制解调器放在路由器旁边。'),('The old computer used an external modem.','那台老电脑使用外置调制解调器。'),sources=S('modem','modem'))
W('modems','英 /ˈməʊdemz/；美 /ˈmoʊdəmz/','调制解调器〔复数〕',
 '不同型号、不同年代的几个调制解调器，就是 modems。名称缩合好之后，复数照英语规则变化。',
 'modem + -s → modems，/m/ 后读 /z/；不再把它展开成两个长词各自加复数。',MODEM+[['modem + -s → modems','多个调制解调器，词尾 /mz/']],
 'cable modems 是有线宽带调制解调器；old modems 是老式调制解调器；several modems 是几台设备。',
 'cable modems；old modems；several modems。',
 'modem 已经是一个完整英语名词；数几台时，给整词加 s，不把内部缩略块分别处理。',
 ('The shop sells routers and modems.','这家商店出售路由器和调制解调器。'),('Several old modems were on display.','展台上陈列着几台老式调制解调器。'),sources=S('modems','modem'))
W('pixels','英、美 /ˈpɪksəlz/','像素〔复数〕',
 '把一张小图片放大，看到一格格颜色单位，可以用 pixels 来理解。许多小单位一起组成图像。',
 'pixel 接 pix 图片短称 + element 前部缩合；pix 是 pics 的变体。pixel + -s → pixels，/l/ 后读 /z/。',PIXEL,
 'millions of pixels 是数百万像素；individual pixels 是单个像素；a width of 800 pixels 是宽 800 像素。',
 'individual pixels；millions of pixels；800 pixels wide。',
 '像素数是图像、显示的一个维度；这个词本身不等于所有画质指标，也不是屏幕上的物理毫米单位。',
 ('The image is 800 pixels wide.','这张图宽 800 像素。'),('At this magnification, you can see individual pixels.','放大到这个程度，你能看到单个像素。'),sources=S('pixels','pixel'))
W('avatar','英 /ˈævətɑː/；美 /ˈævəˌtɑr/','化身；虚拟形象、用户头像',
 '现实中的你在游戏、论坛里用一个形象出现，那个“代表你出场的身体”就是 avatar。更早的意义是神祇降世的化身。',
 '经印度斯坦语借入，向前接梵语降下、降世相关名词，ava- 向下 + 横渡、越过词根材料；英语从神祇化身、具体体现，继续用于代表用户的数字形象。',AVATAR,
 'a digital avatar 是数字化身；a game avatar 是游戏角色形象；choose an avatar 是选择头像、虚拟形象。',
 'a digital avatar；a game avatar；choose an avatar。',
 'avatar 可以是静态头像，也可以是可活动角色；profile 则常指个人资料整体，范围不同。',
 ('She chose a fox as her avatar.','她选了一只狐狸作为自己的头像。'),('His avatar wears a bright green coat in the game.','他在游戏里的虚拟形象穿着鲜绿色外套。'),sources=S('avatar','avatar'))
W('avatars','英 /ˈævətɑːz/；美 /ˈævəˌtɑrz/','化身；虚拟形象、用户头像〔复数〕',
 '屏幕上每个人各有一个代表自己的小形象，这些形象就是 avatars。它们把“化身”这个旧词带进了数字世界。',
 'avatar + -s → avatars，基础词接梵语降世、化身词线；现代复数直接加 s，后缀 /z/。',AVATAR+[['avatar + -s → avatars','多个化身或数字形象，词尾 /z/']],
 'custom avatars 是自定义头像、虚拟形象；player avatars 是玩家化身；animated avatars 是会动的虚拟形象。',
 'custom avatars；player avatars；animated avatars。',
 'avatars 数的是代表人物的形象；同一个用户也可能有多个 avatars，不一定等于用户人数。',
 ('Players can design their own avatars.','玩家可以设计自己的虚拟形象。'),('The meeting screen showed a row of colourful avatars.','会议屏幕上显示了一排彩色头像。'),sources=S('avatars','avatar'))
W('emoji','英 /ɪˈməʊdʒi/；美 /ɪˈmoʊdʒi/','表情符号、绘文字',
 '消息里一个笑脸、一颗心、一辆小汽车，都可能是 emoji。它是用图画样式写出来的字符，不只用来表达情绪。',
 '借日语 e 画 + moji 文字 → emoji；不是 emotion 情绪的 e 加上一个后缀。和 emoticon 的相似拼写，是不同构词路线的巧合。',EMOJI,
 'a smiley emoji 是笑脸表情符号；a heart emoji 是爱心符号；send an emoji 是发送一个表情符号。',
 'a heart emoji；a smiley emoji；send an emoji。',
 'emoji 是图画字符；emoticon 常说由标点、字母拼成的表情，如 :-)；也别把任意整张贴纸都当作同一种字符。',
 ('She replied with a heart emoji.','她回复了一个爱心表情。'),('I added an emoji to make the message friendlier.','我加了一个表情符号，让消息显得更友好。'),sources=S('emoji','emoji'))
W('emojis','英 /ɪˈməʊdʒiz/；美 /ɪˈmoʊdʒiz/','表情符号〔复数〕',
 '一条消息里好几个笑脸、爱心，是 emojis。图画有多少个，就可以按字符一个个来数。',
 'emoji + -s → emojis，原 /i/ 后接 /z/。英语也常见单复数不变的 emoji；emojis 是使用广泛的规则复数。',EMOJI+[['emoji + -s → emojis','规则复数；另有不变复数 emoji']],
 'smiling emojis 是笑脸符号；a string of emojis 是一串表情符号；messages with emojis 是带表情的消息。',
 'a string of emojis；smiling emojis；messages with emojis。',
 'emojis 与不变复数 emoji 都能见到；这里的复数 -s 是英语借入后的变化，不是日语 moji 的一个新组成部分。',
 ('The message ended with three laughing emojis.','消息最后带着三个大笑表情。'),('She uses emojis in chats with her friends.','她和朋友聊天时会用表情符号。'),sources=S('emojis','emoji'))
W('selfies','英、美 /ˈselfiz/','自拍照〔复数〕',
 '把镜头对向自己拍出的照片，是 selfies。几个人一起自拍也可以叫 selfies，并不要求每张只能出现一个人。',
 'self 自己 + -ie 口语名词后缀 → selfie；selfie + -s → selfies，基础词已以 ie 结尾，直接加 s，词尾 /iz/。',
 [['self 自己 + -ie → selfie 自拍','口语名词构词，拍摄者也在照片中'],['selfie + -s → selfies','复数直接加 s；不漏 -ie，也不误用 y 变 i 的规则']],
 'take selfies 是自拍；group selfies 是多人自拍照；holiday selfies 是旅行自拍照。',
 'take selfies；group selfies；holiday selfies。',
 'photos 泛指照片，selfies 则说明拍摄者把自己也拍了进去；别人替你拍的普通人像不因只有你一人就自动是自拍。',
 ('We took selfies by the lake.','我们在湖边拍了自拍照。'),('Her phone is full of holiday selfies.','她的手机里全是旅行自拍照。'),sources=S('selfies','selfie'))
W('hashtags','英、美 /ˈhæʃtæɡz/','话题标签〔复数〕',
 '帖子后面带 # 的词组，像 #CityWalk，可以是 hashtags：把内容挂上一个能被找到的话题牌。',
 'hash 这里指 # 符号 + tag 标签 → hashtag；再加 -s → hashtags，/ɡ/ 后读 /z/。不是 hash 食物或杂烩义直接组成的话题名。',
 [['hash mark 的 hash：# 符号 + tag 标签 → hashtag','用带 # 的词语标出、聚合话题，也能补充评论'],['hashtag + -s → hashtags','多个话题标签，词尾 /ɡz/']],
 'add hashtags 是添加话题标签；search hashtags 是搜索标签；popular hashtags 是热门话题标签。',
 'add hashtags；popular hashtags；search by hashtags。',
 'tag 范围更广，可以是各种标签；hashtags 特别强调 # 形式及其话题用法。',
 ('She added two hashtags to the post.','她给帖子加了两个话题标签。'),('We used the same hashtags to find photos from the event.','我们用相同的话题标签查找活动照片。'),sources=S('hashtags','hashtag'))
W('webinar','英 /ˈwebənɑː/；美 /ˈwɛbəˌnɑr/','网络研讨会、在线讲座',
 '不用走进教室，在网上听讲、参与提问讨论的研讨活动，可以叫 a webinar。名字就是把网络和研讨会揉到一起。',
 'web 网络 + seminar 研讨活动缩合 → webinar；seminar 更远经德语接拉丁 seminarium 苗圃、培育场的比喻。这里不是 web 后面接一个通用后缀 -inar。',WEBINAR,
 'attend a webinar 是参加网络研讨会；host a webinar 是主持、举办；a webinar on design 是关于设计的在线讲座。',
 'attend a webinar；host a webinar；a webinar on design。',
 'webinar 强调网上讲解、研讨活动；普通远程开会更常用 online meeting，不必把每次线上闲聊都叫 webinar。',
 ('I attended a webinar on design yesterday.','昨天我参加了一场关于设计的网络讲座。'),('The webinar ended with a short question session.','网络研讨会以一段简短问答结束。'),sources=S('webinar','webinar'))
W('webinars','英 /ˈwebənɑːz/；美 /ˈwɛbəˌnɑrz/','网络研讨会、在线讲座〔复数〕',
 '一系列在网上举行的讲座、研讨会，是 webinars。缩合词形成后，照常加英语复数。',
 'webinar + -s → webinars，后缀读 /z/；原来 web + seminar 的缩合部分保留。',WEBINAR+[['webinar + -s → webinars','多场在线讲座、研讨活动，词尾 /z/']],
 'free webinars 是免费网络讲座；a series of webinars 是系列网络研讨会；recorded webinars 是录下来的网络讲座。',
 'free webinars；a series of webinars；recorded webinars。',
 'webinars 通常按场次、活动来数；几个人看同一场讲座，不会因此自动变成几场 webinars。',
 ('The library offers free webinars every month.','图书馆每月提供免费网络讲座。'),('Recordings of the webinars are available online.','这些网络研讨会的录像可以在线查看。'),sources=S('webinars','webinar'))
W('uploads','名词：英 /ˈʌpləʊdz/、美 /ˈʌploʊdz/；动词：英 /ʌpˈləʊdz/、美 /ʌpˈloʊdz/','上传的文件、上传操作〔复数〕；上传',
 '本地照片送到网站，是上传；网站里列出来的一份份上传内容，也可叫 uploads。它既能说动作，也能数动作、文件。',
 'up + load → upload；加 -s → uploads，/d/ 后读 /z/。常见名词前重、动词后重；网络中的 up 标示传送方向，不是文件在物理空间里向天上飞。',
 [['up 向上 + load 装载 → upload 上传','将装载动作借给向远端系统送入数据'],['upload + -s → uploads','名词复数、第三人称单数动词；常有重音差别']],
 'recent uploads 是最近上传的内容；failed uploads 是失败的上传操作；uploads a photo 是上传一张照片。',
 'recent uploads；failed uploads；uploads a photo。',
 'uploads 强调送到远端、服务一侧；downloads 则常从远端取回。方向按当前设备、系统语境判断。',
 ('Recent uploads appear at the top of the page.','最近上传的内容显示在页面顶部。'),('She uploads a new drawing every Friday.','她每周五上传一幅新画。'),sources=S('uploads','upload'))
W('Bluetooth','英 /ˈbluːtuːθ/；美 /ˈbluˌtuθ/','蓝牙〔短距离无线连接技术；通常写 Bluetooth〕',
 '耳机、键盘和手机不用线也能连接，常用到 Bluetooth。名字借“把不同东西联合起来”的历史人物形象。',
 '技术名借 Harald Bluetooth 的历史绰号；最初作临时代号，后来沿用为名称。Bluetooth 不是一串技术术语首字母缩写，正式书写通常保留大写 B。',
 [['Harald Bluetooth 的历史绰号 → 无线技术的临时代号','命名借联合不同产品、行业的关系'],['代号沿用为 Bluetooth 技术名称','技术官网解释名称与标志背景；现代不是描述设备有一颗蓝牙齿']],
 'Bluetooth headphones 是蓝牙耳机；a Bluetooth connection 是蓝牙连接；connect via Bluetooth 是通过蓝牙连接。',
 'Bluetooth headphones；a Bluetooth keyboard；a Bluetooth connection。',
 'Bluetooth、Wi-Fi 都用于无线通信，但名称不互相替换；这里学的是蓝牙这一技术名称及常见搭配。',
 ('These headphones connect to my phone via Bluetooth.','这副耳机通过蓝牙连接我的手机。'),('The laptop has a Bluetooth keyboard.','这台笔记本配了一把蓝牙键盘。'),sources=S('Bluetooth','bluetooth'))
W('phishing','英、美 /ˈfɪʃɪŋ/','网络钓鱼、电子通信中的信息诱骗',
 '把假消息伪装成可信来源，诱人交出敏感信息，这种骗取信息的做法叫 phishing。像下诱饵等人上钩，所以借“钓鱼”来命名。',
 'fishing 钓鱼的变形拼写 → phishing；ph 仍读 /f/，不表示这里用了一个古希腊学术前缀。拼写可能受黑客词语习惯等影响，具体不能只认一条已定故事。',
 [['fishing 钓鱼 → 变形拼写 phishing','诱饵、上钩的比喻用于信息诱骗'],['phishing 作为现代网络词使用','ph 读 /f/，与普通 fishing 发音相同']],
 'a phishing email 是钓鱼邮件；a phishing attempt 是一次信息诱骗尝试；phishing messages 是钓鱼消息。',
 'a phishing email；a phishing attempt；phishing messages。',
 'spam 侧重不请自来的大量消息，phishing 侧重骗取信息；一封消息可能同时符合两种描述。',
 ('The email turned out to be a phishing attempt.','那封邮件原来是一次网络钓鱼尝试。'),('The training explains how to recognise phishing messages.','培训讲解如何识别钓鱼消息。'),sources=S('phishing','phishing'))
W('spammed','英、美 /spæmd/','群发了垃圾消息；被垃圾消息、刷屏内容淹没了',
 '同样的广告一遍遍塞进邮箱、讨论区，可以说被 spammed 了。重点是别人没要求，却被大量重复内容打扰。',
 'spam 双写 m + -ed → spammed，/m/ 后后缀读 /d/；动词接网络垃圾消息名词，名字背后有短剧反复喊 Spam 淹没对话的形象。',SPAM+[['spam 双写 m + -ed → spammed','规则过去式、过去分词；词尾 /md/']],
 'spammed with adverts 是被广告刷屏；spammed the forum 是给论坛发垃圾内容；users were spammed 是用户收到大量垃圾消息。',
 'spammed with adverts；spammed the forum；spammed with links。',
 'emailed 只说发了邮件；spammed 还表明内容不请自来、数量多或重复，常带批评。',
 ('The forum was spammed with identical adverts.','论坛被一模一样的广告刷屏了。'),('My inbox was spammed with unwanted offers.','我的收件箱被不想要的促销消息塞满了。'),sources=S('spammed','spam'))
W('spamming','英、美 /ˈspæmɪŋ/','发送垃圾消息；刷屏',
 '不断重复发消息，把别人的正常讨论顶走，是 spamming。它把垃圾消息的名词变成正在发生的动作。',
 'spam 双写 m + -ing → spamming；可作现在分词、动名词。这个 m 是按现代拼写规则双写，不是原品牌名里藏着两个 m。',SPAM+[['spam 双写 m + -ing → spamming','发垃圾消息、刷屏的动作形式']],
 'stop spamming 是停止刷屏；spamming the chat 是往聊天里刷消息；spamming links 是反复发链接。',
 'stop spamming；spamming the chat；spamming links。',
 '发很多有必要、被期待的消息不自动都叫 spamming；这个词通常包含不受欢迎、重复干扰的判断。',
 ('The moderator asked him to stop spamming the chat.','管理员让他停止在聊天里刷屏。'),('The rules prohibit spamming links in the comments.','规则禁止在评论区刷链接。'),sources=S('spamming','spam'))
W('spammers','英 /ˈspæməz/；美 /ˈspæmɚz/','垃圾消息发送者；刷屏者〔复数〕',
 '不是一条条垃圾消息本身，而是发这些东西的人、账号，就是 spammers。后缀把动作变成“做这事的人”。',
 'spam 双写 m + -er → spammer，再加 -s → spammers；名词复数词尾 /z/。发送账号也能被这样称呼，不一定强调屏幕后某个人的身份。',SPAM+[['spam 双写 m + -er → spammer → spammers','-er 发送者，再以 -s 形成复数']],
 'block spammers 是屏蔽垃圾消息发送者；spammers in the comments 是评论区刷屏者；accounts used by spammers 是被其使用的账号。',
 'block spammers；persistent spammers；spammers in the comments。',
 'spam 是垃圾内容或刷屏动作，spammers 是发送者；不要把几条垃圾消息数成 three spammers。',
 ('The forum blocks persistent spammers.','论坛会屏蔽反复刷屏的人。'),('Spammers had filled the comments with adverts.','垃圾消息发送者把评论区塞满了广告。'),sources=S('spammers','spam'))
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_ziy',ROOTS,WORDS)
 extend_lessons()
