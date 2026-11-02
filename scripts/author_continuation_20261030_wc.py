"""Useful everyday loans and transparent family links."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'B3177':dict(words=['coffee','cafe'],label='coffee／cafe：同一饮料名称的不同借入路线',note='cafe 经法语 café 接意大利语 caffè，再接土耳其、阿拉伯咖啡词族；coffee 的近源借入路线另看本词。'),
 'A1768':dict(words=['soda','sodium'],label='soda → sodium：材料名称进入元素命名',note='sodium 的名称取 soda 词基加 -ium；soda 的化学物质义与现代汽水义分开，钠与这些化合物不是同一物质。'),
 'C0609':dict(words=['interim'],label='interim：两阶段之间的过渡时段',note='完整借入拉丁 interim 其间；其中 inter 表在……之间，末尾 im 是古代代词相关材料，不是现代英语后缀。'),
 'B4353':dict(words=['pose','pause','paused','pausing'],label='pause／pose：停下与放下的同源分路',note='pause 与 pose 接希腊、拉丁停止词族，pose 经法语发展出放置并受拉丁 ponere 影响；不能把它们当作现代英语互换元音。'),
 'B3437':dict(words=['raw','crude'],label='raw／crude：生、未加工的远源对应',note='raw 继承日耳曼语路线，crude 借拉丁 crudus；二者通常联系更早的生肉、鲜血词族，不是 crude 从英语 raw 派生。'),
 'C0660':dict(words=['legitimate','legit'],label='legitimate → legit：合法、正当到口语靠谱',note='legit 是 legitimate 的口语截短，后来常说真的、可信的；源头接拉丁 lex／legis 法律。'),
 'B3686':dict(words=['fry','fried','frying'],label='fry → fried／frying：煎炸动作的两种形式',note='烹饪动词 fry 经法语接拉丁 frigere；辅音字母加 y 在 fried 里变 i，frying 则保留 y。'),
}
W('cafe','英 /ˈkæfeɪ/；美 /kæˈfeɪ/','咖啡馆；供应饮料和简餐的小餐馆；也写 café',
 '从咖啡这杯饮料，想到人们坐下来喝它的地方。英语 cafe 通常指店，店里也可以卖茶、甜点或简餐。',
 '借法语 café，法语经意大利语 caffè 接土耳其语 kahve、阿拉伯语 qahwa 咖啡词族。coffee 与它有共同远源，近源借入路径不同；英语 cafe 不是把 coffee 临时改拼。',
 [['阿拉伯 qahwa → 土耳其 kahve → 意大利 caffè → 法语 café','咖啡；法语又指喝咖啡的场所'],['法语 café → 英语 cafe／café','咖啡馆、简餐店']],
 'a small cafe 小咖啡馆；a pavement cafe 英式说有人行道露天座位的咖啡馆；a cafe near the station 车站附近的咖啡馆。英语可保留法语重音符号，也常省略。',
 'meet at a cafe；sit outside the cafe。','英语 coffee 通常是饮料，cafe 通常是店；法语 café 则两种意思都常见。a cafe 可以供应很多饮料，不凭店名推断它只卖咖啡。',
 ('We found a quiet cafe beside the river.','我们在河边找到了一家安静的咖啡馆。'),('The cafe serves soup and sandwiches at lunchtime.','这家咖啡馆午间供应汤和三明治。'),sources=['https://en.wiktionary.org/wiki/cafe#English','https://www.etymonline.com/word/cafe'])
W('soda','英 /ˈsəʊdə/；美 /ˈsoʊdə/','苏打；苏打水；汽水〔尤其美式用法〕',
 '这个名字先与碱性物质相连，后来经过 soda water 用来叫有气泡的水和饮料。所以厨房里的 soda 与菜单上的 soda，要分场景理解。',
 '经意大利语或中世纪拉丁 soda 等形式传入，早期指碳酸钠及提取相关碱性物质的材料，更远来源未定。饮料义由 soda water 等缩短发展，不能反推每杯汽水都含碳酸钠。',
 [['意大利语／中世纪拉丁 soda 等 → 英语 soda','碳酸钠等碱性物质名称，远源未定'],['soda water 等 → 饮料义 soda','苏打水；尤其美式语境中的汽水']],
 'baking soda 小苏打，即碳酸氢钠；washing soda 洗涤用苏打，通常指碳酸钠；a can of soda 一罐汽水；soda water 苏打水、气泡水。',
 'a glass of soda；soda and juice。','sodium 是钠元素，soda 的常见化学义说的是相关化合物；名称有联系，物质不能混为一谈。不同地区把汽水叫 soda、pop 或 soft drink，使用习惯不完全相同。',
 ('Would you like water, juice, or a soda?','你想喝水、果汁，还是汽水？'),('The recipe calls for a small amount of baking soda.','这个食谱需要少量小苏打。'),sources=['https://en.wiktionary.org/wiki/soda#English','https://www.etymonline.com/word/soda'])
W('interim','/ˈɪntərɪm/','临时的、过渡期间的；过渡时段',
 '正式安排还没接上，先用一项安排把中间这段空档撑住。interim 关注的是两个阶段之间的过渡。',
 '完整借入拉丁 interim 其间、与此同时，历史材料为 inter 在……之间加代词相关的 im；不是英语 inter- 再接一个能自由使用的 -im 后缀。',
 [['拉丁 inter + 古代代词相关材料 → interim','在其间、与此同时'],['英语 interim 名词、形容词','中间的时段；过渡期间使用的']],
 'an interim report 阶段性报告；an interim manager 临时负责人；an interim solution 过渡方案；in the interim 在此期间。',
 'an interim arrangement；in the interim。','temporary 只说暂时，interim 常暗示在等待后续正式安排。interim report 通常是过程中的报告，final report 才是最终报告。',
 ('They appointed an interim manager while searching for a permanent replacement.','他们寻找长期接任者期间，任命了一位临时负责人。'),('The repairs will take a week; in the interim, we will use another room.','维修需要一周；在此期间，我们会用另一间屋子。'),sources=['https://en.wiktionary.org/wiki/interim#English','https://www.etymonline.com/word/interim'])
W('pause','英 /pɔːz/；美 /pɔːz, pɑːz/','暂停；停顿；犹豫片刻',
 '动作或话语先停一停，留出一点空白，往往还可以接着来。播放器上的暂停键，就是最直观的 pause。',
 '名词经古法语及拉丁 pausa 接希腊 pausis 停止；动词有名词转用及法语 pauser、晚期拉丁 pausare 的相关路线。与 pose 有共同历史材料，现代用法各自固定。',
 [['希腊 pausis → 拉丁 pausa → 古法语相关形式 → pause 名词','停止、停顿'],['相关法语、拉丁动词及英语名词转用 → pause 动词','暂时停下']],
 'pause for a moment 暂停片刻；pause to think 停下来想想；pause the video 暂停视频；a long pause 很长的停顿；give someone pause 让某人犹豫、重新考虑。',
 'after a short pause；pause before replying。','pause 通常强调停顿，stop 的范围更广，也可能是彻底停止。pause 和 paws 爪子的复数在常见口音中同音，拼写和语境不同。',
 ('Pause the video when the map appears.','地图出现时把视频暂停。'),('After a brief pause, she continued her story.','稍微停顿后，她接着讲故事。'),sources=['https://en.wiktionary.org/wiki/pause#English','https://www.etymonline.com/word/pause'])
W('paused','英 /pɔːzd/；美 /pɔːzd, pɑːzd/','暂停了、停顿了；pause 的过去式和过去分词',
 '话讲到一半先停了，视频暂时停在一帧上，都可以说 paused。这个停顿常给接下来的动作留着位置。',
 'pause 去末尾 e，加完整 -ed；/z/ 后读 /d/，不增加音节。词基接希腊 pausis、拉丁 pausa／pausare 的停止词族。',
 [['希腊、拉丁停止词族 → pause','停顿、暂时停止'],['pause 去 e + -ed → paused','过去停顿；已经暂停的状态']],
 'paused for breath 停下来喘口气；paused before answering 回答前停顿；paused the recording 暂停录音；the game is paused 游戏处于暂停状态。',
 'paused briefly；paused to listen。','She paused to read 是她停下原来的动作，去读；She stopped reading 是她停止阅读。to read 常交代停下来的目的，不能只看都有停就译成同一句话。',
 ('He paused to check the address on his phone.','他停下来，用手机核对地址。'),('The recording was paused while we moved the chairs.','我们搬椅子时暂停了录音。'),sources=['https://en.wiktionary.org/wiki/paused#English','https://en.wiktionary.org/wiki/pause#English'])
W('pausing','英 /ˈpɔːzɪŋ/；美 /ˈpɔːzɪŋ, ˈpɑːzɪŋ/','正在停顿、暂停；pause 的 -ing 形式；停顿这一动作',
 '把一连串动作之间的小空白拿出来看：pausing 可以说正在停一停，也能把停顿本身作为一个动作来讨论。',
 'pause 去掉末尾不发音的 e，再加 -ing，写 pausing；/z/ 保留。pause 接希腊、拉丁停止词族，英语这个形式按规则产生。',
 [['希腊、拉丁停止词族 → pause','暂时停下'],['pause 去 e + -ing → pausing','进行中的暂停；停顿这一动作']],
 'without pausing 毫不停顿地；pausing for thought 停下来思考；pausing between sentences 在句子之间停顿。',
 'pausing briefly；pausing to look around。','pausing to do 说停一下去做另一件事。pausing 本身不等于犹豫不决，也可能是刻意留时间让听者消化信息。',
 ('She read the list without pausing.','她一口气读完了清单。'),('Pausing between sentences gives listeners time to follow your ideas.','句子之间稍作停顿，能给听众时间跟上你的思路。'),sources=['https://en.wiktionary.org/wiki/pausing#English','https://en.wiktionary.org/wiki/pause#English'])
W('crude','/kruːd/','未加工的；粗略的、粗糙的；粗俗的；原油〔名词〕',
 '先想还没精加工的原料。做出来的模型不细致，可以叫 crude；话说得缺乏分寸，也可以沿着未加修饰、粗糙的感觉理解。',
 '借拉丁 crudus 生的、未煮熟的、粗糙的。与本族词 raw 通常联系更早的生肉、鲜血词族，但英语走两条独立传承路线；crude 不是 cr- + rude。',
 [['早期生肉、鲜血词族 → 拉丁 crudus；另路日耳曼语 → raw','共同远源比较，非英语 raw 派生 crude'],['拉丁 crudus → 英语 crude','生、未加工 → 粗略、粗俗；原油']],
 'crude oil 原油；a crude model 粗略模型；a crude estimate 粗略估算；crude language 粗俗言语。名词 crude 常在石油语境中缩指原油。',
 'a crude sketch；a barrel of crude。','crude estimate 强调估得粗略，crude joke 常批评内容粗俗；同一个形容词跟不同名词，评价方向不同。raw data 与 crude data 也不应一律互换，raw 常说尚未处理的原始数据。',
 ('He made a crude model from cardboard.','他用纸板做了一个粗略模型。'),('The diagram gives only a crude estimate of the building’s size.','这张图只能让人大致估计建筑的大小。'),sources=['https://en.wiktionary.org/wiki/crude#English','https://www.etymonline.com/word/crude'])
W('legit','/lɪˈdʒɪt/','合法、正当的；真的、可信的、靠谱的〔口语〕',
 '先问是不是来路正当，再扩展为是不是货真价实、值得相信。That looks legit 常是在说看着像真的、像靠谱的。',
 'legitimate 的口语截短，不另拆一个 leg 词根。更早接中世纪拉丁 legitimatus、legitimus，关联 lex、legis 法律；较早的截短用法见于戏剧行业语境。',
 [['拉丁 lex／legis → legitimus／legitimatus → legitimate','符合法律 → 合法、正当、真正的'],['legitimate 截短 → legit','口语说正当、真实、可信；也有强调真不错的用法']],
 'a legit business 正规经营的企业；a legit reason 站得住脚的理由；looks legit 看着靠谱；a legit musician 真有本事的音乐人。',
 'seems legit；a legit copy。','legit 是口语，legitimate 更适合正式表述。looks legit 只说看起来可信，不等于已经查证；某些口语还把 legit 当强调语，近似 really。',
 ('Is this the official page? It looks legit, but the address is unfamiliar.','这是官方页面吗？看着像真的，但网址很陌生。'),('She has a legit reason for arriving late.','她迟到有个说得通的理由。'),sources=['https://en.wiktionary.org/wiki/legit#English','https://www.etymonline.com/word/legit'])
W('fried','/fraɪd/','煎、炸、炒过的；累瘫了、脑子转不动了〔口语〕；fry 的过去式和过去分词',
 '食物放进油和热锅里做熟，是 fried；口语里说脑子 fried，则把耗得发烫、运转不动的感觉借过来。',
 'fry 的 y 前是辅音字母 r，加 -ed 时 y 变 i，写 fried；读音仍保留 /aɪ/，词尾读 /d/。烹饪动词经古法语 frire 接拉丁 frigere 煎、烤。',
 [['拉丁 frigere → 古法语 frire → fry','煎、炸等烹饪动作'],['fry 变 y 为 i + -ed → fried','煎炸过的；后有耗尽精力等口语引申']],
 'fried rice 炒饭；fried eggs 煎蛋；fried chicken 炸鸡；My brain is fried 口语说脑子累得转不动了。fry 在不同菜里可对应煎、炒、炸，不能只认一种中文做法。',
 'freshly fried；fried onions。','fried 描述已经煎炸过，frying 常说正在做或用于煎炸。幼鱼义 fry 有另一条词源路线，不把它解释成已经炸好的鱼。',
 ('We had fried rice and vegetables for lunch.','我们午饭吃了炒饭和蔬菜。'),('After three hours of editing, my brain was fried.','连续修改三个小时后，我脑子都转不动了。'),sources=['https://en.wiktionary.org/wiki/fried#English','https://www.etymonline.com/word/fry'])
W('frying','/ˈfraɪɪŋ/','正在煎、炒、炸；煎炸这一动作；fry 的 -ing 形式',
 '听到食物在热油里滋滋响，就是 frying 最直接的画面。它可以描述正在做菜，也可以给锅和油标明用途。',
 'fry + -ing，直接保留 y，不写 friing。/aɪ/ 后再接 /ɪŋ/，常标两个音节。词基经法语 frire 接拉丁 frigere 的烹饪义。',
 [['拉丁 frigere → 法语 frire → fry','用热油、热锅煎炸'],['fry + -ing → frying','正在煎炸；煎炸活动或用途']],
 'a frying pan 平底煎锅；frying oil 煎炸用油；frying an egg 正在煎蛋；out of the frying pan into the fire 从糟糕处境脱身却进入更糟的处境。',
 'frying onions；a large frying pan。','fried food 是煎炸过的食物，frying food 在动作语境中是正在煎炸食物。fry 加 -ed 时变 y 为 i，加 -ing 时保留 y，两种变化要分别记。',
 ('She was frying onions when I arrived.','我到的时候，她正在炒洋葱。'),('Use the smaller frying pan for the eggs.','煎蛋用那口小一点的平底锅。'),sources=['https://en.wiktionary.org/wiki/frying#English','https://www.etymonline.com/word/fry'])
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_wc',ROOTS,WORDS)
 extend_lessons()
