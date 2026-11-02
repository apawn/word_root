"""Wave paths, adjective/verb frequent, ban and an explicitly unrelated banner."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
A=[['古英语 wafian → 中古英语 waven → wave〔动词〕','来回、上下摆动'],['中古英语 wawe 等旧水波名词，受动词形式影响 → wave〔名词〕','水浪；现代词形与摆动动词靠拢'],['现代 wave 的形象扩展','手势、水波、物理波；一波接一波的事情']]
def AH(f,m):return A[:2]+[[f,m]]
W('wave','/weɪv/','波浪、波；挥手；摆动；一波、一阵',
 '水面一高一低地起伏，手也能来回摆；热、情绪、事件一阵阵袭来，可以借说一波。形象相通，但历史形式不是全由同一个现代词临时变出来。',
 '动词接古英语 wafian；水波名词有中古英语 wawe 等旧形式，现代拼写受到动词影响。两路的直接祖先、远源分析不完全相同，学习时用起伏连义，不伪造一条单线。',A,
 'waves on the sea 海浪，wave goodbye 挥手告别，wave someone over 招手叫人过来，a wave of relief 一阵宽慰，sound waves 声波。',
 'wave goodbye；wave someone over；a wave of；sound waves。',
 'wave 挥、波，waive 放弃某项权利等同音异词；wave of relief 是一阵感受，不等于微波炉。',
 ('She waved goodbye from the train.','她在火车上挥手告别。'),('A wave of relief passed through the crowd.','人群中涌过一阵如释重负的感觉。'),
 sources=['https://en.wiktionary.org/wiki/wave#English','https://www.etymonline.com/word/wave'])
W('wavy','/ˈweɪvi/','波浪形的、起伏的、卷曲的',
 '不是完全直，也不是紧紧的小圈，而是像水波那样一弯一弯地延伸。',
 'wave 去不发音 e 加 -y，形成带波浪形特点的形容词。',AH('wave + -y → wavy〔去 e〕','像波浪般弯曲、起伏的'),
 'wavy hair 波浪卷发，a wavy line 波浪线，wavy edges 起伏边缘。',
 'wavy hair；a wavy line；wavy edges。',
 'wavy 强调波形，curly 常更明显卷圈，二者范围可重叠；wavy 形状不一定正在 waving 摆动。',
 ('She has long wavy hair.','她有一头波浪长发。'),('Draw a wavy line across the page.','在纸上画一条波浪线。'))
W('waver','英 /ˈweɪvə/；美 /ˈweɪvər/','摇摆、动摇、犹豫；声音、光等颤动',
 '原来指向一边，下一刻又摆回另一边；拿不定主意、信心不稳，也像在两边来回摇。',
 '动词接中古英语 waveren，可能有北欧语及相关古英语词的背景，与 wave 摆动词族相关。末尾 -er 在这里有旧反复动作构词背景，不是现代人物后缀，不能译成挥手的人。',
 [['中古英语 waveren、wayveren → waver','犹豫、信念动摇的记录很早，之后有物体、声音等不稳的明确用法'],['与 wave、古英语 wæfre 等相关；更早路径有分析差别','重复摆动的学习画面可以串联意义，不代表所有物理记录早于抽象义']],
 'waver between two options 在两选项间犹豫，confidence wavers 信心动摇，her voice wavered 她声音发颤。',
 'waver between；confidence wavers；her voice wavered。',
 'wave 常单纯挥动，waver 常不稳定、犹豫；waiver 放弃权利的名词与 waver 发音近，拼写、来源不同。',
 ('He tends to waver between accepting the offer and staying where he is.','他总在接受邀请与留在原处之间犹豫。'),('Her voice began to waver as she read the letter.','读信时，她的声音开始发颤。'),
 sources=['https://en.wiktionary.org/wiki/waver#English','https://www.etymonline.com/word/waver'])
W('waveguide','/ˈweɪvɡaɪd/','波导〔引导波传播的结构〕',
 '让波沿指定的路走，像给它安排通道；不是给看海浪的游客带路的人。',
 'wave 波 + guide 引导物，合成技术名词。不同波、装置有不同具体结构，名称先说明引导传播的作用。',AH('wave + guide → waveguide','约束、引导波沿一定路径传播的结构'),
 'an optical waveguide 光波导，a metal waveguide 金属波导，a waveguide structure 波导结构。',
 'an optical waveguide；a metal waveguide；a waveguide structure。',
 'waveguide 是结构或通道，wavelength 是波长这个量；guide 末尾虽像动词，在复合词中可指起引导作用的物体。',
 ('The diagram shows light travelling through an optical waveguide.','图示展示光在光波导中传播。'),('The engineer inspected the metal waveguide.','工程师检查了金属波导。'))
W('wavelet','/ˈweɪvlət/','小波、小浪；小波〔数学、信号分析〕',
 '日常可说小小的波纹；技术上用集中在一小段范围的波形来分析变化，名称保留“小波”的形象。',
 'wave + 小称后缀 -let，英语构词也与法语 ondelette 的对应翻译有关。-let 是后缀，不是动词 let 让。',AH('wave + -let → wavelet；对应法语 ondelette','小波；再作数学分析名称'),
 'wavelets on the water 水面小波，wavelet analysis 小波分析，a wavelet transform 小波变换。',
 'wavelets on the water；wavelet analysis；a wavelet transform。',
 'wavelet 技术含义不能只理解为体积小的海浪；wavelength 测波长，wavelet 命名波形或分析材料。',
 ('Small wavelets moved across the pond.','池面泛过一道道小波纹。'),('The paper uses wavelet analysis to study the signal.','论文用小波分析研究该信号。'))
R('B3706','波形、摆动、信心动摇与传播分析','WAVE：来回起伏的画面，进入手势、感受和物理量','wave → wavy、waver；wavelength、waveform、wavefront、wavefunction 按波的描述分；waveguide、wavelet 按引导与分析分；其他复合词另组。',
 '水波名词与摆动动词的历史路线汇合，不是一条字母链包办所有。waver 动摇不是人物后缀 -er；wavy 去 e 加 y。',
 'wafian、waven → 动词 wave；旧 wawe 等 → 名词 wave；wave + -y/-let；wave + guide；waver 保留旧反复动作词史。',
 [['基础、形状与动摇','wave · wavy · waver'],['波的描述和引导分析','wavelength · waveform · wavefront · wavefunction · waveguide · wavelet'],['其他领域复合词','microwave · shortwave · heatwave · brainwave']],
 'wave/waive 同音异词；waver/waiver 易混；wavy 形状与 waving 动作不同；wavelet 不等于 wavelength。',
 'She drew a wavy line to represent a wave.\n\n她画了一条波浪线来表示一个波。','wave wavy waver wavelength waveform wavefront wavefunction waveguide wavelet microwave shortwave heatwave brainwave')
F=[['拉丁 frequēns → 法语 frequent → frequent〔形容词〕','拥挤、密集 → 经常、频繁'],['拉丁 frequentāre → 法语 frequenter → frequent〔动词〕','聚集、常去某地；与形容词同词族但独立路径']]
W('frequent','形容词 /ˈfriːkwənt/；动词 /frɪˈkwent/','频繁的、经常的；常去、常光顾〔动词〕',
 '事情隔不久又来一次，次数密，叫 frequent；人经常出现在同一咖啡馆，也可用动词 frequent，说他常去那里。',
 '形容词经法语接拉丁 frequēns 拥挤、密集、反复等；动词有 frequentāre、frequenter 的借入路线。两者现代拼写一样，重音却不同。',F,
 'frequent visits 频繁来访，frequent delays 经常延误，frequent a café 常去一家咖啡馆。动词较正式。',
 'frequent visits；frequent delays；a frequent visitor；frequent a café。',
 '形容词前重音 /ˈfriːkwənt/，动词后重音 /frɪˈkwent/；frequent 次数多不等于 always 每一次都发生。',
 ('Frequent delays made the service unpopular.','经常延误让这项服务不受欢迎。'),('The café is frequented by local artists.','当地艺术家常光顾这家咖啡馆。'))
W('frequently','/ˈfriːkwəntli/','频繁地、经常',
 '做这件事不是偶尔一次，而是隔些时候就会再发生；把 frequent 次数密的特点放到动作上。',
 '形容词 frequent + -ly，副词重音保持在前；不是从后重音动词再表示常去的某个人。',F[:1]+[['frequent + -ly → frequently','以很高频率发生地']],
 'frequently asked questions 常见问题，travel frequently 经常出行，check frequently 经常检查。缩写 FAQ 的 F 来自 frequently。',
 'frequently asked questions；travel frequently；check frequently。',
 'frequently 与 often 常近义，前者稍正式；frequently 是副词，不能在 a frequent visitor 中直接替形容词。',
 ('She travels frequently for work.','她因工作经常出差。'),('The answer appears in the frequently asked questions.','答案就在常见问题里。'))
W('infrequent','/ɪnˈfriːkwənt/','不频繁的、少有的',
 '不是从来没有，而是隔很久才碰到一次；in- 否定的是频繁，不是否定事件存在。',
 'in- 不 + 形容词 frequent，形成次数少、罕有的形容词。这里 in- 不表示在里面。',F[:1]+[['in- + frequent → infrequent','出现次数不多的']],
 'infrequent visits 少有的来访，an infrequent occurrence 不常发生的事，infrequent service 班次稀少的服务。',
 'infrequent visits；an infrequent occurrence；infrequent service。',
 'infrequent 不常见，impossible 不可能；infrequent buses 是班次少，不一定每辆车都迟到。',
 ('His visits became increasingly infrequent.','他来访得越来越少。'),('Snow is an infrequent occurrence in this town.','这个小镇不常下雪。'))
R('B3838','次数密、常去与次数稀少','FREQUENT：像人挤在一起那样，事情也能在时间上密集','frequent → frequently；infrequent 加否定。基础词的形容词、动词读音先分开。',
 '频繁不等于永远，少见不等于绝无。frequent 作动词是常去某地，不只是形容事情次数多。',
 'frequēns → frequent 形容词；frequentāre 经法语 → frequent 动词；frequent + -ly；in- + frequent。',
 [['频率与常去','frequent · frequently'],['次数少','infrequent']],
 '形容词前重音、动词后重音；frequently 副词；infrequent 非不可能。',
 'A frequent visitor comes here frequently.\n\n一位常客经常来这里。','frequent frequently infrequent')
BAN=[['古英语 bannan 与古诺尔斯语 banna 等 → 中古英语 bannen → ban','宣告、命令、禁止等旧义互相影响'],['现代 ban','禁止的决定；不准进行某事']]
W('ban','/bæn/','禁止、禁令',
 '有权作决定的一方明确说这事不准再做；作名词是禁令，作动词是实施禁止。',
 '古英语 bannan 宣告、命令与北欧同源词 banna 禁止、诅咒等影响中古英语，接到现代禁止义。不是天生只含互联网封号。',BAN,
 'ban smoking 禁止吸烟，a ban on smoking 禁烟令，ban someone from a place 不准某人进入某地，lift a ban 解除禁令。过去式 banned、分词 banning 双写 n。',
 'ban doing；a ban on；ban someone from；lift a ban。',
 '动词 ban 后直接接对象，名词 a ban on 接对象；ban 禁止、banned 已被禁，band 乐队同音近形却不是禁令过去式。',
 ('The library bans food and drink near the computers.','图书馆禁止在电脑旁饮食。'),('The school lifted the ban on mobile phones during breaks.','学校取消了课间使用手机的禁令。'))
W('banal','/bəˈnɑːl/ 或 /ˈbeɪnəl/','陈腐的、平庸乏味的',
 '听来听去都是人人说过的套话，没有新意；不是平常就一定不好，而是普通到让人觉得无聊。',
 '借法语 banal，接旧法语 banel 与封建命令、管辖下的公用设施等背景；从大家通用、普通发展到陈腐。与 ban 的宣告词族历史有关，但不是现代禁止 + -al 就能直接算出无聊。',
 [['旧法语 banel、法语 banal','管辖、公用背景 → 通用、普通'],['法语 banal → 英语 banal','平庸、陈腐、无新意']],
 'a banal remark 陈词滥调，banal conversation 乏味谈话，a banal observation 毫无新意的评论。',
 'a banal remark；banal conversation；a banal observation。',
 'banal 通常贬义，ordinary 普通可中性；与 ban 的联系经过法语旧社会用法，不能直接说被禁止的就是 banal。',
 ('The dialogue was full of banal remarks.','对话里满是陈词滥调。'),('The reviewer found the ending banal and predictable.','评论者觉得结尾平庸，而且一猜就中。'),
 sources=['https://en.wiktionary.org/wiki/banal#English','https://www.etymonline.com/word/banal'])
W('banner','英 /ˈbænə/；美 /ˈbænər/','横幅、旗帜；网页横幅；杰出的〔修饰语〕',
 '展开给大家看的大块标识，原来常是布旗，后来也可以是网页顶端显眼的一条图文。a banner year 则说特别出色的一年。',
 '经中古英语 baner、古法语 baniere，上接晚期拉丁 bandum 与日耳曼标识、旗帜词。这里不是 ban 禁止 + 人物 -er，不能译成禁令执行者。',
 [['日耳曼旗帜、标识词 → 晚期拉丁 bandum → 古法语 baniere','旗、标识'],['中古英语 baner → banner','旗帜、横幅 → 显眼广告、标题及杰出等比喻']],
 'hang a banner 挂横幅，a banner ad 横幅广告，under the banner of 打着某旗号，a banner year 出色的一年。',
 'hang a banner；a banner ad；under the banner of；a banner year。',
 'banner 与 ban 近形但来源另看；banner ad 是一类展示广告，adblock 可拦广告，两词不因此共享根。',
 ('They hung a welcome banner across the entrance.','他们在入口横挂了一条欢迎横幅。'),('The company had a banner year for sales.','公司这一年的销售成绩格外出色。'),
 sources=['https://en.wiktionary.org/wiki/banner#English','https://www.etymonline.com/word/banner'])
R('B2735','宣告、禁止与 banal 的历史；banner 另源对照','BAN：公开作出命令，现代常落到“不准”；相似拼写须另辨','ban 的 banned、banning 在本条说明；banal 是经法语绕到平庸的历史旁支；banner 是形近异源对照，不列作 ban 的后代。',
 'banal 不能直接按现代禁止拼出陈腐，banner 更不是禁止者。把真正词族与形近词分清，才有用。',
 '旧日耳曼宣告词 → ban；法语管辖、公用背景 → banal；日耳曼旗帜词经法语 → banner〔另源〕。',
 [['命令、禁止','ban'],['法语历史旁支','banal'],['形近异源对照，不属 ban 派生','banner']],
 'a ban on 与 ban something 句法不同；banal 陈腐非所有普通；banner 不从 ban + -er。',
 'The banner announced a ban on smoking.\n\n横幅上宣布禁止吸烟。','ban banal banner')
ROOTS[-1]['exclude']['banning']='ban 的规则 -ing 形式，双写 n 已在 ban 条内说明，不另立重复词头。'
if __name__=='__main__':save('continuation_20261030_dl',ROOTS,WORDS)
