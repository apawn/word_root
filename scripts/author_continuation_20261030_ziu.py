"""Water animals, bird calls, movement and the separate histories of perch."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
def S(word,base):
 return ['https://en.wiktionary.org/wiki/'+word+'#English','https://www.etymonline.com/word/'+base]
EXISTING_ROOT_ADDITIONS={
 'B2684':dict(words='duck ducked ducking'.split(),label='duck → ducked、ducking：身子往下一闪',note='duck 动词从潜入水下扩大为低头闪避，再有避谈问题。鸭子名与潜水动作有古老关系，但不能把所有动词义都说成从现代鸭子名词新造出来。'),
 'B2417':dict(words='crow crows crowed crowing'.split(),label='crow → crows、crowed、crowing：鸟名、啼叫与得意',note='古英语 crow 鸟名和啼叫动词有拟声背景。现代 crow 动词常说公鸡啼叫，也比喻得意吹嘘；不是只有乌鸦能作它的主语。'),
 'B3504':dict(words='hen hens'.split(),label='hen → hens：母鸡及复数',note='hen 接古英语 henn，历史上是雄鸡称呼的阴性形式；现代先学母鸡，也可依鸟类名称指雌鸟。'),
 'B4610':dict(words='otter otters'.split(),label='otter：远处同族的水中动物名',note='otter 接古英语 otr、otor，上溯重建的日耳曼、印欧语形式，有水中动物的命名背景，与 water 远同族；不是现代英语 water 改几个字母产生。'),
 'B2812':dict(words='beaver beavers'.split(),label='beaver：与熊的动物名比较远古颜色命名',note='beaver 接古英语 beofor、befer，远源通常联系重叠构形的棕褐色、明亮颜色材料。与 bear 的动物名有远处颜色命名关系；不是 bear 承担动词的派生，也没有现代后缀 -ver。'),
 'B3151':dict(words='stir stirs stirring'.split(),label='stir → stirs、stirring：让东西动起来，也让心动起来',note='古英语 styrian、stirian 已兼有移动、搅动、激起等义。stirring 从正在搅动，还能形容激动人心；不必编造所有抽象义都先经过现代厨房。'),
 'B3871':dict(words='spur spurred spurring'.split(),label='spur → spurred、spurring：马刺推动到促进行动',note='spur 原有靴跟上的马刺名，动词借刺马催动的动作说激励、促使；spurred、spurring 双写末尾 r 后接 -ed、-ing。'),
 'B3938':dict(words='cannabis marijuana'.split(),label='marijuana：另一路进入英语的大麻称呼',note='与 cannabis 对照名称，marijuana 直接接墨西哥西班牙语 marihuana，远源不确定；不由 cannabis 拆字派生。'),
 'B2902':dict(words='perch perches perched perching'.split(),label='perch：杆到栖木、栖息；鱼名另源',note='栖木名接古法语 perche、拉丁 pertica 杆，动词经法语 perchier 栖息进入英语。鲈鱼名另接拉丁 perca、希腊 perkē，与斑点的古老材料有关；与 rod 在这里主要比较实物、用途，不宣称直接同源。'),
}
DUCK=[['古英语 duce 鸭，与古老潜水动作词有关','英语 duck 动词先有扎入水中、潜下去等义'],['潜下、俯低 → 迅速低头闪避 → 避开问题、责任','ducked、ducking 是现代动词变化，不把现代名词当全部起点']]
CROW=[['古英语 crawe 鸟名、crawan 啼叫','通常联系拟声背景；两种用法都很古老'],['英语 crow 动词常指公鸡啼叫，也有得意欢叫、吹嘘','现代 crows、crowed、crowing 按相应用法变化']]
HEN=[['古英语 henn ← 古日耳曼语雄鸡名称的阴性形式','更远通常接唱、鸣叫的古老词族'],['hen 母鸡，也可按语境指别的雌鸟 → hens','母鸡的名称继承历史关系，不是在说母鸡必定早晨打鸣']]
OTTER=[['古英语 otr、otor ← 重建日耳曼语 *otraz','重建的印欧语 *udros 有水中动物的背景'],['水的古老材料 → otter 水獭 → otters','water 和 otter 是远处同族，各自经历语音演变']]
BEAVER=[['古英语 beofor、befer ← 重建日耳曼语 *bebruz','更远常解释为颜色材料的重叠构形，有棕褐色动物的命名背景'],['beaver 河狸 → beavers','英语沿用动物名，现代不宜再硬切成英语零件']]
STIR=[['古英语 styrian、stirian：动起来、搅动、激起','更远接重建的日耳曼语材料与转动的古老词族'],['英语 stir：搅动食物、身体动一动、激起感情','stirs、stirring 是现代变化；搅动与心动帮助理解共同的动感']]
SPUR=[['古英语 spura、spora：靴跟上催马的尖器','远处与脚踝、踢的古老材料有关'],['spur 名词马刺 → 动词催动、激励','spurred、spurring 双写 r，再接相应完整后缀']]
PERCH=[['栖木名：拉丁 pertica 杆 → 古法语 perche → 英语 perch','栖息动词经古法语 perchier 进入英语，背后也是栖木、杆的名词'],['perch 鱼名：希腊 perkē → 拉丁 perca → 古法语 perche','这条线常联系斑点、深色的古老材料；和栖木名不是同一词源']]
W('ducked','英、美 /dʌkt/','迅速低头、弯身闪开了；避开了',
 '球飞过来，人把头往下一收，就是 ducked。谈话里也能把难题“闪过去”。',
 'duck + -ed → ducked；原来已有 ck，直接加 -ed，/k/ 后读 /t/。',DUCK+[['duck + -ed → ducked','过去式、过去分词；末尾 /kt/']],
 'ducked under 是低身钻过；ducked out of the way 是闪到旁边；ducked a question 是避而不答。',
 'ducked under a branch；ducked a question；ducked out of the way。',
 'ducked 强调把身体压低或闪避；普通 bent down 只说弯下身，不一定为躲开什么。',
 ('He ducked as the ball flew past.','球飞过时，他迅速低下了头。'),('She ducked the question and changed the subject.','她避开了问题，转移了话题。'),sources=S('ducked','duck'))
W('ducking','英、美 /ˈdʌkɪŋ/','正在低头闪避；回避',
 '人一路低头避开树枝，或不断绕开关键问题，动作进行中就可以用 ducking。',
 'duck + -ing → ducking，保留原 ck，接 /ɪŋ/。可作进行式中的分词，也可用作动作名称。',DUCK+[['duck + -ing → ducking','低头闪避、回避的进行或动作形式']],
 'ducking under branches 是低头钻过树枝；ducking the issue 是回避这个问题。',
 'ducking under；ducking the issue；keep ducking questions。',
 'ducking the issue 往往含有有意不正面处理的意思，不只是暂时没听见。',
 ('We kept ducking under low branches.','我们不断低头钻过低矮的树枝。'),('You are ducking the issue again.','你又在回避这个问题了。'),sources=S('ducking','duck'))
W('crows','英 /krəʊz/；美 /kroʊz/','乌鸦〔复数〕；啼叫；得意吹嘘',
 '树上几只黑色乌鸦，是 crows；a rooster crows 则是公鸡打鸣。先看它是名词还是动词。',
 'crow + -s → crows，元音后读 /z/。名词是多只乌鸦；动词是第三人称单数，常说公鸡啼叫，也可说人得意吹嘘。',CROW+[['crow + -s → crows','复数名词或第三人称单数动词；词尾 /z/']],
 'a flock of crows 是一群乌鸦；the rooster crows 是公鸡打鸣；crows about his victory 是得意地夸耀胜利。',
 'black crows；the rooster crows；crows about winning。',
 'crow 作啼叫动词，不等于叫声的主人必须是 crow 乌鸦；公鸡才是这种动词的常见主语。',
 ('Three crows landed in the field.','三只乌鸦落在田里。'),('The rooster crows before sunrise.','这只公鸡在日出前打鸣。'),sources=S('crows','crow'))
W('crowed','英 /krəʊd/；美 /kroʊd/','啼叫了；得意地说、吹嘘了',
 '赢了一场就昂着头得意宣布，crowed 会让人想到公鸡扬头啼叫的劲头。',
 'crow + -ed → crowed，元音后后缀读 /d/，不另加一个 /ɪd/ 音节。是常用的规则过去式、过去分词。',CROW+[['crow + -ed → crowed','从啼叫到人得意欢叫的比喻，继续保留在过去形式中']],
 'the rooster crowed 是公鸡叫了；crowed about his success 是得意夸耀成功；用来引出人说的话时往往带得意语气。',
 'crowed loudly；crowed about success；crowed with delight。',
 'said 只报说话；crowed 连说话时那股得意劲也带出来，可能含旁观者的调侃。',
 ('The rooster crowed just as the sky began to brighten.','天空刚开始亮，那只公鸡就叫了。'),('“I told you I would win,” he crowed.','“我就说过我会赢的。”他得意地说。'),sources=S('crowed','crow'))
W('crowing','英 /ˈkrəʊɪŋ/；美 /ˈkroʊɪŋ/','啼叫；正在得意吹嘘',
 '一边走一边反复夸自己赢了，就是 crowing about it：像扬着头不停报喜。',
 'crow + -ing → crowing，保留 w，直接加 -ing；既可表示啼叫动作，也能表示夸耀。',CROW+[['crow + -ing → crowing','现代进行形式、动作名称，核心仍是啼叫及得意表达']],
 'a rooster crowing 是公鸡在打鸣；stop crowing about it 是别再得意吹嘘这事了。',
 'a rooster crowing；crowing about a win；crowing with delight。',
 'crowing 多用于响亮啼叫、得意表达；普通 singing 不会自动带这种自得的语气。',
 ('I woke to the sound of a rooster crowing.','我被公鸡的啼叫声叫醒了。'),('He is still crowing about his victory.','他还在得意地夸耀自己的胜利。'),sources=S('crowing','crow'))
W('hens','英、美 /henz/','母鸡〔复数〕；雌鸟〔依语境〕',
 '几只母鸡在院子里刨地、下蛋，就是 hens。这个词把性别也说清楚了。',
 'hen + -s → hens；/n/ 后读 /z/。hen 本来继承古老的雌性鸟名，现代复数规则加 s。',HEN+[['hen + -s → hens','多只母鸡，也可依上下文说多只雌鸟']],
 'laying hens 是产蛋母鸡；brown hens 是棕色母鸡；hens and chicks 是母鸡和小鸡。',
 'laying hens；brown hens；hens and chicks。',
 'chickens 泛指鸡，hens 明确为母鸡，roosters 则是公鸡。',
 ('The hens were scratching in the yard.','母鸡们正在院子里刨地。'),('The farm keeps a small flock of laying hens.','这家农场养了一小群产蛋母鸡。'),sources=S('hens','hen'))
W('otter','英 /ˈɒtə/；美 /ˈɑtɚ/','水獭',
 '身体细长、擅长在水里游动找食物的水獭，是 otter。词源里也藏着“水中动物”的老画面。',
 '古英语 otr、otor，经古日耳曼语材料，上溯重建的印欧语 *udros 水中动物；与 water 的水词族有远处关系，现代英语不再拆成 water 加动物后缀。',OTTER,
 'a river otter 是河獭；a sea otter 是海獭；an otter swimming 是一只正在游泳的水獭。',
 'a river otter；a sea otter；an otter swimming。',
 'otter 是水獭；beaver 是河狸，常见辨认画面是河狸宽扁的尾巴和筑坝行为。',
 ('An otter slipped into the river.','一只水獭滑进了河里。'),('We watched a sea otter floating on its back.','我们看着一只海獭仰面浮在水上。'),sources=S('otter','otter'))
W('otters','英 /ˈɒtəz/；美 /ˈɑtɚz/','水獭〔复数〕',
 '河边不止一只水獭，便用 otters。记住它仍是那个与水有古老联系的动物名。',
 'otter + -s → otters，词尾按读音加 /z/。英国常见非卷舌读法 /təz/，美国常见卷舌 /tɚz/。',OTTER+[['otter + -s → otters','多只水獭的规则复数']],
 'river otters 是河獭；sea otters 是海獭；a pair of otters 是两只水獭。',
 'river otters；sea otters；a pair of otters。',
 'sea otters 和 river otters 都属于 otter 的名称范围，具体说哪类时保留前面的修饰词。',
 ('Two otters played beside the bank.','两只水獭在河岸旁玩耍。'),('The children looked for otters along the river.','孩子们沿着河寻找水獭。'),sources=S('otters','otter'))
W('beaver','英 /ˈbiːvə/；美 /ˈbivɚ/','河狸',
 '宽扁尾巴、啃树木、会筑坝的河狸，是 beaver。这个动物名有很古老的棕褐色命名背景。',
 '古英语 beofor、befer，接重建日耳曼语 *bebruz；更远通常联系重叠构形的颜色材料。与 bear 的动物名有远处关系，不是现代英语 bear 加 -ver。',BEAVER,
 'a beaver dam 是河狸筑的坝；a beaver lodge 是河狸的巢；beaver fur 是河狸毛皮。',
 'a beaver dam；a beaver lodge；beaver fur。',
 'beaver 动物名与旧头盔护面罩的同形词来自不同路线；护面罩义不需要拿河狸的样子硬解释。',
 ('A beaver dragged a branch into the water.','一只河狸把树枝拖进水中。'),('We found a beaver dam farther upstream.','我们在更上游发现了一道河狸坝。'),sources=S('beaver','beaver'))
W('beavers','英 /ˈbiːvəz/；美 /ˈbivɚz/','河狸〔复数〕',
 '几只河狸一起活动，就说 beavers。它们的名字仍是整块继承的老动物名。',
 'beaver + -s → beavers，词尾读 /z/；不把 beaver 中的 -er 当作现代英语表示职业、做事者的后缀。',BEAVER+[['beaver + -s → beavers','多只河狸的规则复数']],
 'a pair of beavers 是两只河狸；beavers building a dam 是正在筑坝的河狸。',
 'a pair of beavers；beavers building a dam；signs of beavers。',
 '宽扁尾巴、筑坝的辨认画面常用来记 beavers；otters 则是水獭，两个名称不能互换。',
 ('Beavers had built a dam across the stream.','河狸已经在小溪上筑起了一道坝。'),('We saw signs of beavers near the pond.','我们在池塘附近看到了河狸活动的痕迹。'),sources=S('beavers','beaver'))
W('stirs','英 /stɜːz/；美 /stɝz/','搅拌；动了动；激起；骚动〔复数〕',
 '勺子让汤动起来，回忆让心里动起来，都能用 stirs。先抓住“原来静着，现在被拨动了”。',
 'stir + -s → stirs，词尾读 /z/。动词是第三人称单数；名词也可表示不止一次、几处的骚动。',STIR+[['stir + -s → stirs','现代单数主语的动词形式，也可为骚动名词复数']],
 'stirs the soup 是搅汤；stirs memories 是唤起回忆；nobody stirs 是没人动弹。',
 'stirs the soup；stirs memories；stirs up debate。',
 'stirs memories 常是情绪、记忆被唤起；stirs the soup 则是实际搅拌，动作的共同点是从静到动。',
 ('She stirs the soup with a wooden spoon.','她用木勺搅汤。'),('That song still stirs memories of home.','那首歌至今仍会唤起对家的回忆。'),sources=S('stirs','stir'))
W('stirring','英 /ˈstɜːrɪŋ/；美 /ˈstɝɪŋ/','正在搅拌、活动；激动人心的；初现的感觉',
 'stirring soup 是搅汤；a stirring speech 是把人心里的劲头搅起来的演讲。这个画面能把动作与情绪连起来。',
 'stir 双写末尾 r + -ing → stirring。既作动词分词、动作名称，也发展出激动人心的形容词和内心初动的名词用法。',STIR+[['stir 双写 r + -ing → stirring','动的过程、心里的初动，以及激动人心的形容词']],
 'keep stirring 是继续搅拌；a stirring speech 是鼓舞人心的演讲；a stirring of hope 是一丝希望开始萌动。',
 'keep stirring；a stirring speech；a stirring of hope。',
 'stirring 形容演讲、音乐时多有振奋、打动人的效果；stirred 则常描述东西已被搅过，或人受到触动。',
 ('Keep stirring until the sauce is smooth.','继续搅拌，直到酱汁变得顺滑。'),('She gave a stirring speech about courage.','她发表了一番关于勇气的振奋人心的演讲。'),sources=S('stirring','stir'))
W('spurred','英 /spɜːd/；美 /spɝd/','促使了、激励了；用马刺催动了',
 '一个结果、一次鼓励，像从背后给行动加了把劲，就是 spurred。画面来自马刺催马。',
 'spur 双写 r + -ed → spurred；后缀读 /d/。现代常说某事促使人行动，或某种力量促进变化。',SPUR+[['spur 双写 r + -ed → spurred','过去式、过去分词，常接行动或变化']],
 'spurred someone to act 是促使某人行动；spurred growth 是促进增长；spurred on by 是受到……激励。',
 'spurred growth；spurred her to try again；spurred on by encouragement。',
 'spurred on by encouragement 把鼓励当推动力；spurred by fear 也能用，推动人行动的未必是愉快感觉。',
 ('Her encouragement spurred me to try again.','她的鼓励促使我再试一次。'),('The success of the first event spurred further plans.','首场活动的成功推动了后续计划。'),sources=S('spurred','spur'))
W('spurring','英 /ˈspɜːrɪŋ/；美 /ˈspɝɪŋ/','正在促使、促进；催动',
 '一股力量持续推着事情往前走，就是 spurring。它保留了马刺“催动一下”的感觉。',
 'spur 双写 r + -ing → spurring；现代常见于进行式，也可把促进这件事本身当作动作来谈。',SPUR+[['spur 双写 r + -ing → spurring','促进、激励正在发生，或作为动作名称']],
 'spurring growth 是促进增长；spurring change 是推动变化；spurring people on 是鼓励人继续努力。',
 'spurring growth；spurring change；spurring the team on。',
 'spurring 说推动的力量，具体结果仍要看句子；它本身不等于事情已经完成。',
 ('The new bus route is spurring interest in the area.','新公交线路正在带动人们对这个地区的关注。'),('The fans kept spurring the team on.','球迷们不断为球队鼓劲。'),sources=S('spurring','spur'))
W('marijuana','英 /ˌmærɪˈwɑːnə/；美 /ˌmærəˈwɑnə/','大麻；大麻制品〔常见于新闻、公共讨论〕',
 '新闻里的 marijuana，通常说大麻或相关制品。和 cannabis 指称有重合，但这两个英语名称走了不同的借词路线。',
 '借墨西哥西班牙语 marihuana 等形式进入英语，英文又出现 marijuana 拼写；更远来源不确定。不能把它拆成人名 Maria + Juana，当作已经证实的最初起源。',
 [['墨西哥西班牙语 marihuana 等形式 → 英语借词','更远的词源有争议'],['英语 marijuana 拼写及现代用法','与 cannabis 比较名称，不是 cannabis 的英语派生']],
 'marijuana use 是大麻使用；a debate about marijuana 是有关大麻的讨论；通常作不可数名词。',
 'marijuana use；marijuana policy；a debate about marijuana。',
 'cannabis 在植物、科学等语境很常见，marijuana 在媒体、社会讨论中也常出现；具体范围仍随上下文变化。',
 ('The documentary examines public attitudes toward marijuana.','这部纪录片考察公众对大麻的态度。'),('The article uses the word marijuana throughout.','这篇文章通篇都使用 marijuana 这个词。'),sources=S('marijuana','marijuana'))
W('perch','英 /pɜːtʃ/；美 /pɝtʃ/','栖木、歇脚的高处；栖息；鲈鱼〔鱼名另源〕',
 '鸟落在一根横杆上，那根杆是 a perch；鸟停在上面，也可以说 perch。鱼名 perch 则另记一条来源。',
 '栖木名来自古法语 perche、拉丁 pertica 杆；动词经古法语 perchier 栖息借入。鱼名另接希腊 perkē、拉丁 perca，通常联系有斑点、深色的古老材料。',PERCH,
 'a bird perch 是鸟栖木；perch on a branch 是停在树枝上；from a high perch 是从高处；鱼名通常可用 perch 作单复数。',
 'perch on a branch；a high perch；freshwater perch。',
 'sit 只说坐着，perch 常让人想到落在高处、小边缘或窄支点上；鲈鱼义和这幅图不是一条词源。',
 ('The parrot stepped onto its perch.','鹦鹉踏上了它的栖木。'),('Small birds often perch on the fence.','小鸟常停在栅栏上。'),('The lake is home to several kinds of perch.','这片湖里有好几种鲈鱼。'),sources=S('perch','perch'))
W('perches','英 /ˈpɜːtʃɪz/；美 /ˈpɝtʃɪz/','栖木〔复数〕；停歇、栖息；鲈鱼〔某些复数用法〕',
 '几根鸟能站的横杆是 perches；a bird perches on the roof 则说鸟停在屋顶。名词、动词要分清。',
 'perch + -es → perches，/tʃ/ 后增加 /ɪz/ 音节。鱼名多数时候复数仍用 perch，perches 也见于多类、多个体等语境。',PERCH+[['perch + -es → perches','名词复数或第三人称单数；词尾 /tʃɪz/']],
 'wooden perches 是木栖杆；perches on the railing 是停在栏杆上。鱼名的复数形式按上下文、用法选择。',
 'wooden perches；perches on a roof；perches on a railing。',
 '栖木复数通常用 perches；不能因为鱼名常用零复数，就把栖木也一概写成 two perch。',
 ('The cage has two wooden perches.','笼子里有两根木栖杆。'),('A robin perches on the railing every morning.','每天早晨都有一只知更鸟停在栏杆上。'),sources=S('perches','perch'))
W('perched','英 /pɜːtʃt/；美 /pɝtʃt/','停在、栖息在；坐落在高处或边缘的',
 '小鸟落定在枝头，或房子架在山坡高处，都有 perched 那种“在上面稳住”的画面。',
 'perch + -ed → perched，/tʃ/ 后后缀读 /t/。可作过去式、过去分词，也常描述停在某处的状态。',PERCH+[['perch + -ed → perched','栖息动词的过去、状态形式；不从鱼名派生']],
 'perched on a branch 是停在树枝上；perched on the edge of a chair 是坐在椅子边缘；a village perched on a hill 是坐落在山上的村子。',
 'perched on a branch；perched on the edge；perched above the valley。',
 'a village perched on a hill 借高处支点的画面，不是房子真的像鸟一样有翅膀。',
 ('A sparrow perched on the windowsill.','一只麻雀落在窗台上。'),('The little house was perched above the valley.','小房子坐落在山谷上方的高处。'),sources=S('perched','perch'))
W('perching','英 /ˈpɜːtʃɪŋ/；美 /ˈpɝtʃɪŋ/','停歇、栖息；适于停在枝上的',
 '鸟站在窄窄的树枝上，是 perching。人只坐在椅边那一点地方，也能借这个词来形容。',
 'perch + -ing → perching；直接接 -ing，ch 保留。来自动词栖息这一线，与鱼名是不同来源。',PERCH+[['perch + -ing → perching','栖息动作的进行形式、动作名称，也可作修饰']],
 'birds perching on wires 是停在电线上的鸟；perching on a stool 是坐在凳子上；perching birds 可描述能在枝上栖止的鸟。',
 'birds perching on wires；perching on a branch；perching on a stool。',
 'perching on the edge 强调支点、边缘的姿态；sitting 是范围更广的坐、停留。',
 ('We watched the birds perching on the wires.','我们看着停在电线上的鸟。'),('She was perching on the edge of a high stool.','她当时坐在一张高凳的边缘。'),sources=S('perching','perch'))
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_ziu',ROOTS,WORDS)
 extend_lessons()
