"""Dry, wake and coffee: material states, separate wake sources, borrowed drink."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
D=[['古英语 drȳġe〔形容词〕、drȳġan〔动词〕→ 中古英语 drye、drien','干的；使干、变干'],['英语 dry','干燥；使干；扩展到不甜、枯燥、冷面幽默等']]
def DH(f,m):return D+[[f,m]]
W('dry','/draɪ/','干的；使干、变干；〔酒〕不甜的；枯燥的；冷面幽默的',
 '毛巾没水是干，话语没什么热闹情绪也可叫 dry。先抓没有湿润感，再把不甜、乏味、冷幽默分场景记，别强求都译成干。',
 '形容词、动词各有古英语旧形。现代 dried、drying 等接这条本族词路径；酒、文章、幽默是后来各自形成的常用用法。',D,
 'dry clothes 干衣服，dry your hair 把头发弄干，dry wine 不甜的酒，dry humour 不动声色的幽默。a dry subject 可指枯燥题目，dry humour 却可能很好笑。',
 'dry your hands；dry weather；dry wine；a dry sense of humour。',
 'dry wine 仍是液体，dry humour 不一定枯燥；dried fruit 是经过脱水的水果。dry run 是演练、预演，不是人在干地上跑步。',
 ('Dry your hands before touching the paper.','碰纸之前先把手擦干。'),('Her dry sense of humour made the meeting more enjoyable.','她那不动声色的幽默让会议轻松了些。'))
W('drying','/ˈdraɪɪŋ/','干燥、脱水过程；使干的、正在变干的',
 '水分还在离开物体，是一个进行中的过程；也可说某种东西让皮肤变干。',
 'dry + -ing，保留 y，不改成 dr i ing。名词指干燥过程，分词、形容词按动作和作用理解。',DH('dry + -ing → drying','干燥过程；正在干、使变干'),
 'drying time 干燥时间，a drying rack 晾衣架，a drying effect 使干燥的作用。',
 'drying time；a drying rack；the drying process。',
 'drying 过程或作用，dried 常是已经干燥的结果；drying fruit 正在脱水的水果、dried fruit 果干。',
 ('The paint needs more drying time.','油漆还需要更长的干燥时间。'),('She hung the shirts on a drying rack.','她把衬衫挂到晾衣架上。'))
W('dryer','英 /ˈdraɪə/；美 /ˈdraɪər/','烘干机、干燥器；吹风机〔按搭配〕',
 '把湿东西变干的设备。放衣服进去烘的是 clothes dryer，拿来吹头发的是 hair dryer。',
 'dry + 器具后缀 -er，旧时已有相应人物、器具派生。dryer 常用于设备；drier 也有干燥器拼写，drier 还常是 dry 的比较级。',DH('dry + -er → dryer','使东西变干的人或设备；常用设备义'),
 'a tumble dryer 滚筒烘干机，a hair dryer 吹风机，put clothes in the dryer 把衣服放进烘干机。',
 'a clothes dryer；a hair dryer；use the dryer。',
 'dryer 设备，dryness 干燥状态；天气更干常写 drier weather，不把 dryer 当作所有比较级的首选。',
 ('The towels are still in the dryer.','毛巾还在烘干机里。'),('I used a hair dryer to dry my hair.','我用吹风机吹干了头发。'))
W('dryness','/ˈdraɪnəs/','干燥；干的程度；枯燥、冷淡等特征〔按对象〕',
 '把干这个特点拿出来说：皮肤有多干、空气有多干；谈文章时也可能说它有多枯燥。',
 'dry + -ness，形成性质名词，中古英语已有相应形式。词尾 y 保留。',DH('dry + -ness → dryness','干燥的状态、程度；引申相应的干淡特点'),
 'skin dryness 皮肤干燥，the dryness of the air 空气的干燥程度，dryness of tone 冷淡、平直的语调。',
 'skin dryness；the dryness of；a feeling of dryness。',
 'dryness 状态，drying 使干、变干的过程；dryness 本身不是某一疾病的确诊名称。',
 ('The dryness of the air made the paper curl.','空气干燥，使纸张卷了起来。'),('He commented on the dryness of the textbook’s style.','他评论说，这本教科书的文风很枯燥。'))
W('dryly','/ˈdraɪli/','冷冷地、淡淡地〔说笑等〕；以干的方式',
 '话里带着笑点，脸上却没有大笑，像平平淡淡说一句事实；这是日常很值得记的 dryly。',
 'dry + -ly，形成方式副词，保留 y。d r y 这部分不因接 -ly 就自动换成 dri。',DH('dry + -ly → dryly','以干淡的方式；不动声色地'),
 'say dryly 淡淡地说，remark dryly 冷冷评论，smile dryly 淡淡一笑。常由上下文判断是否讽刺。',
 'say dryly；remark dryly；reply dryly。',
 'dryly 不动声色，loudly 大声，二者观察维度不同。dryly 不能按天气干燥一律译成干巴巴地。',
 ('“That went well,” she said dryly as the cake collapsed.','蛋糕塌下去时，她淡淡地说：“这可真成功。”'),('He dryly remarked that the shortcut had taken an extra hour.','他不动声色地评论说，这条捷径让他们多走了一个小时。'))
W('drought','/draʊt/','干旱；长期无成果、未得分等的低潮期〔比喻〕',
 '雨迟迟不来，地越来越干；球队迟迟进不了球，也会借雨一直不来的画面说进球荒。',
 '接古英语 drūgaþ、drugoþ 等，经中古英语 droughte 延续，与 dry 同族，含旧抽象名词后缀。不是今天把 dry 拼写随手换成 drought；gh 在常用读音中不发音。',
 [['古英语 drūgaþ、drugoþ → 中古英语 droughte → drought','持续干燥天气；与 dry 同族的旧抽象名词'],['现代 drought','干旱；比喻长期没有想要的成果']],
 'a severe drought 严重干旱，a prolonged drought 持续干旱，end a goal drought 结束进球荒。',
 'a severe drought；a prolonged drought；a goal drought。',
 'dry weather 干燥天气不一定达到 drought 干旱程度；drought 比喻低潮时也不是指球场上真的缺水。',
 ('The region suffered a prolonged drought.','这个地区遭遇了持续干旱。'),('Her late goal ended a six-game scoring drought.','她临近终场的进球结束了连续六场的得分荒。'),
 sources=['https://en.wiktionary.org/wiki/drought#English','https://www.etymonline.com/word/drought'])
W('drydock','英 /ˈdraɪdɒk/；美 /ˈdraɪdɑːk/','干船坞；使船进入干船坞',
 '先把船开进船坞，再排掉里面的水，让船底露出来方便修理。dry 说工作时船体周围没有水。',
 'dry 干 + dock 船坞，合成名词，也可转作动词；分开写 dry dock 也常见。',DH('dry + dock → drydock','能排水以建造、维修船舶的船坞；使进坞'),
 'in drydock 在干船坞维修，enter drydock 进入干船坞，drydock a ship 使船进坞。',
 'in drydock；enter drydock；drydock the vessel。',
 'drydock 干船坞，普通 dock 可指码头、船坞等；这里的 dry 是排水维修条件，非形容港口没有生意。',
 ('The ship spent two weeks in drydock for repairs.','船在干船坞里修了两周。'),('The company drydocked the vessel to inspect its hull.','公司让船进干船坞检查船体。'))
R('B3042','没有水分；干燥过程；不甜、干淡等比喻','DRY：少了水分，也可借干淡感说味道和表达','dry → drying、dryer、dryness、dryly；drought 另接旧同族名词；drydock、drywall、dryland 按设施、材料、地理用途。',
 '不甜的酒仍是液体；冷幽默也不等于无趣。drought 保留古英语支线，不画成现代 dry 直接变几个字母。',
 'dry—dried—dried；dry + -ing/-er/-ness/-ly；drought 旧同族抽象名词；dry + dock/wall/land。',
 [['状态、过程和器具','dry · drying · dryer · dryness · dryly'],['干旱旧同族','drought'],['设施、材料和地区','drydock · drywall · dryland']],
 'drying 过程、dryness 状态；dryer 设备、drier 常比较级；dry wine 不甜、dry humour 不动声色；dry weather 不自动等于旱灾。',
 'The towels felt dry after an hour in the dryer.\n\n毛巾在烘干机里烘了一小时后，摸着已经干了。',
 'dry drying dryer dryness dryly drought drydock drywall dryland')
WA=[['古英语 wacan、wacian 等 → 中古英语 waken、wakien → wake','醒来；保持清醒；后来相关动词形式合流'],['英语 wake','醒来、叫醒；名词守灵与清醒守夜相关']]
W('wake','/weɪk/','醒来、叫醒；守灵；〔另源〕航迹、尾波',
 '睡着的人睁开眼睛，是醒来；整夜守着逝者的旧习俗也跟清醒守夜相连。船后面的尾波则走另一条来源，别编成海水醒了。',
 '醒义来自古英语相关动词的合流，守灵名词接清醒守夜。船尾航迹义大概经荷兰语、低地德语或北欧相关词进入，和冰上开口等旧义相连，具体路线未全确定。',WA+[['另一来源：低地德语、荷兰语或北欧语相关词 → wake','冰面开口等 → 船后留下的水迹；借入路线有不确定性']],
 'wake up 醒来，wake someone up 叫醒；常用过去 woke、分词 woken。in the wake of 表在……之后、随之而来，由船尾踪迹比喻发展。',
 'wake up；wake someone up；a funeral wake；in the wake of。',
 'wake 醒来、awake 清醒的；awake 也可动词。wake 的尾波义另源，in the wake of 不理解成在谁醒来里面。',
 ('Please wake me up at seven.','请七点叫醒我。'),('The boat left a wide wake behind it.','小船身后留下了一道宽宽的尾波。'),
 sources=['https://en.wiktionary.org/wiki/wake#English','https://www.etymonline.com/word/wake'])
W('awake','/əˈweɪk/','醒着的；醒来、唤醒〔动词〕',
 'wake 强调醒过来的动作，be awake 把镜头停在已经醒着的状态。',
 '动词接古英语 āwacan、āwacian，经中古英语延续，表面可认 a- + wake。形容词历史还涉及旧分词的缩短，不只是今天随意给 wake 加 a。',
 [['古英语 āwacan、āwacian → 中古英语 awaken、awakien','醒来、唤醒'],['英语 awake；形容词亦经旧分词缩短发展','醒着的；动词醒来、唤醒']],
 'be awake 醒着，stay awake 保持清醒，wide awake 完全清醒，awake to the danger 意识到危险。普通形容词主要在系动词后，名词前常用 waking 等其他表达。',
 'stay awake；wide awake；lie awake；awake to。',
 'asleep 睡着，awake 醒着；wake up 动作与 stay awake 保持状态不同。动词还可见 awoke、awoken，不要拿醒着的形容词强套时态。',
 ('I was still awake when you called.','你打电话时我还醒着。'),('The sudden noise awoke the whole family.','突如其来的响声把全家人都惊醒了。'))
R('B3006','醒来、保持清醒；尾波另源','WAKE：从睡眠转入清醒；航迹须另分来源','wake 与 awake 放一起，wake 内部另外说明守灵和船尾航迹。',
 '不是所有同形 wake 都从叫醒推出；船后水迹的来源有不确定性，保持分支说明，不编成海水苏醒。',
 'wake—woke—woken；awake—awoke—awoken〔动词〕；a- 是旧前缀材料。',
 [['醒来与清醒','wake · awake']],
 'wake up 动作、be awake 状态；守灵与守夜相关；wake 尾波另源，in the wake of 从航迹发展比喻。',
 'I woke early but stayed awake instead of going back to sleep.\n\n我很早醒来，却一直醒着，没有再睡。','wake awake')
C=[['阿拉伯语 qahwa → 奥斯曼土耳其语 kahve 等 → 欧洲语言相关形式','咖啡饮料名称的跨语言传播'],['荷兰语 koffie 等 → 英语 coffee','咖啡；一份咖啡、咖啡色等用途']]
W('coffee','英 /ˈkɒfi/；美 /ˈkɔːfi/ 或 /ˈkɑːfi/','咖啡；一杯咖啡；咖啡豆、粉〔按语境〕',
 '杯里的饮料、磨来冲泡的原料都可叫 coffee。点单说 two coffees，就是两份咖啡，不是两种化学物质。',
 '借入词，通常经荷兰语 koffie 追到土耳其语 kahve、阿拉伯语 qahwa；传播也涉及意大利语等欧洲形式。更远命名动机有不同说法，不把埃塞俄比亚 Kaffa 地名说成已经确定的唯一答案。',C,
 'a cup of coffee 一杯咖啡，black coffee 黑咖啡，ground coffee 咖啡粉，two coffees 两份咖啡。美式元音因口音有差异。',
 'a cup of coffee；black coffee；ground coffee；coffee beans。',
 'coffee 饮料、原料，café 咖啡馆等是相关借词；coffee table 是矮茶几，不必专门只摆咖啡。',
 ('Would you like a cup of coffee?','你想喝杯咖啡吗？'),('She bought a bag of freshly ground coffee.','她买了一袋刚磨好的咖啡粉。'))
W('coffeemaker','英 /ˈkɒfimeɪkə/；美 /ˈkɔːfimeɪkər/ 或 /ˈkɑːfimeɪkər/','咖啡机、煮咖啡的器具',
 '负责把水和咖啡原料做成饮料的设备。maker 在这里叫机器，不一定叫一个人。',
 'coffee + maker〔make + -er〕，合成器具名词。coffee maker 分开写也很常见。',C+[['coffee + maker → coffeemaker','制作咖啡饮料的器具']],
 'a drip coffeemaker 滴滤咖啡机，clean the coffeemaker 清洗咖啡机；具体机器类型依上下文。',
 'a drip coffeemaker；clean the coffeemaker；an electric coffeemaker。',
 'coffeemaker 制作设备，coffee grinder 磨豆机；磨豆和冲泡是不同步骤，有的机器可把功能合在一起。',
 ('The coffeemaker is on the kitchen counter.','咖啡机放在厨房台面上。'),('He cleaned the coffeemaker after breakfast.','他吃完早饭后清洗了咖啡机。'))
R('B3177','咖啡饮料及原料；设备和店铺','COFFEE：随饮料传播而借入的名称','coffee → coffeemaker、coffeehouse，按原料饮料、设备、场所排序。',
 '这类词讲借入和传播，不硬拆英语前后缀。更远的命名争议简短交代，重点仍是日常用法。',
 'coffee + maker〔make + -er〕；coffee + house；coffee maker 分写亦常见。',
 [['饮料、设备与场所','coffee · coffeemaker · coffeehouse']],
 'coffee 可不可数饮料，也可可数一份；coffeemaker 制作设备、grinder 磨豆设备；-maker 不总指人物。',
 'The coffeehouse bought a new coffeemaker for its morning customers.\n\n咖啡馆为早晨的顾客添置了一台新咖啡机。','coffee coffeemaker coffeehouse')
if __name__=='__main__':save('continuation_20261030_by',ROOTS,WORDS)
