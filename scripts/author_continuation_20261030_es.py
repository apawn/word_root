"""Smile, shirt, historic, max and meat: clear everyday images and useful cautions."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
S=[['中古英语 smilen → smile','微笑；可能来自低地德语或北欧相关词'],['动词 → 名词及性质、图形名','smile 微笑动作与一个微笑；smiley 爱笑、笑脸图形']]
W('smile','/smaɪl/','微笑、笑容；微笑着表示',
 '嘴角轻轻扬起，露出笑意，不一定发出笑声；人可能高兴、客气、紧张地微笑，笑容不自动证明心情。',
 '中古英语已有 smilen，来源可能接低地德语或北欧相关笑词；名词后来从动词发展。不要按 small 小硬改字母来编词源。',S,
 'smile at someone 向某人微笑，give a smile 露出微笑，a warm smile 温暖笑容，smile with relief 如释重负地笑。',
 'smile at；give a smile；a warm smile；smile with relief。',
 'smile 通常无声笑意，laugh 常有笑声；smirk 常带得意、轻蔑意味，不是所有 smile 都是 smirk。',
 ('She smiled at the child.','她向孩子微笑。'),('A nervous smile crossed his face.','他脸上掠过一丝紧张的笑。'),
 sources=['https://en.wiktionary.org/wiki/smile#English','https://www.etymonline.com/word/smile'])
W('smiley','/ˈsmaɪli/','爱笑的、笑眯眯的；笑脸图案、笑脸表情',
 '人物经常笑，可说 smiley；画一个眼睛加上扬嘴角的小脸，也可叫 a smiley。一个是性质，一个是图形名词。',
 'smile + -y，去末尾 e 加 y；形容词再经 smiley face 等用法产生笑脸图案名词。也见笑脸名词拼作 smilie，作为变体理解。',S[:1]+[['smile + -y → smiley','笑眯眯、爱笑的'],['smiley face → 名词 smiley','笑脸图形、表情']],
 'a smiley baby 爱笑宝宝，a smiley face 笑脸，add a smiley 加一个笑脸表情。',
 'a smiley baby；a smiley face；add a smiley。',
 'smiley 既形容词也名词；emoji 包括各种图案，不是每个 emoji 都是笑脸 smiley。',
 ('She was a cheerful, smiley child.','她是个开朗爱笑的孩子。'),('He added a smiley to the message.','他在消息里加了个笑脸表情。'))
R('B2744','嘴角笑意到爱笑的人、笑脸图形','SMILE：微笑的动作，也能成为纸面、屏幕上的小脸','smile → smiley，把动作、性质与图形接在一起。',
 '微笑可以高兴也可紧张，不必把所有 smile 翻成开心；smiley 图形不等于全部 emoji。',
 'smilen → smile；smile + -y → smiley；smiley face → 笑脸名词。',
 [['微笑与笑脸','smile · smiley']],
 'smile/laugh 无声笑意与常见笑声；smirk 多有得意意味；smiley/emoji 范围不同。',
 'She smiled and added a smiley to her reply.\n\n她微笑着，在回复里加了个笑脸。','smile smiley')
H=[['古英语 scyrte → 中古英语 shirte 等 → shirt','短衣、贴身上衣等旧服装名称'],['与 skirt 同族但走不同历史路径','现代 shirt 上身衣物，skirt 通常裙子，不是刚换读音的同词'],['现代组合与状态','shirtless 没穿上衣；undershirt 内穿；sweatshirt、redshirt 看用途']]
W('shirt','英 /ʃɜːt/；美 /ʃɜːrt/','衬衫、上衣、球衣等',
 '穿在上半身的一类衣物；日常可狭指有领扣衬衫，也可在球衣、运动上衣组合里更宽泛，不必每次都西装配白衬衫。',
 '继承古英语 scyrte 等，经中古英语到 shirt；与 skirt 同族而历史借入、语音路径不同。更早短衣、切短联系是历史背景，不是现代 short + 某尾。',H,
 'a cotton shirt 棉衬衫，a football shirt 球衣，button up your shirt 扣好上衣，keep your shirt on 别急〔口语〕。',
 'a cotton shirt；a football shirt；button up your shirt；keep your shirt on。',
 'shirt 与 skirt 现代不是同种衣物；keep your shirt on 固定口语可劝别急，并非每次命令对方穿衣。',
 ('He wore a clean cotton shirt.','他穿着干净的棉衬衫。'),('The players exchanged shirts after the match.','比赛后，球员互换球衣。'))
W('shirtless','英 /ˈʃɜːtləs/；美 /ˈʃɜːrtləs/','没穿上衣的、赤裸上身的',
 '上半身没有穿 shirt 一类上衣；并不自动说整个人一件衣服也没穿。',
 'shirt + -less 没有，组成缺少上衣的状态形容词。',H[:1]+[['shirt + -less → shirtless','没有穿上衣的状态']],
 'a shirtless runner 赤裸上身的跑者，go shirtless 不穿上衣，a shirtless man 没穿上衣的男子。',
 'a shirtless runner；go shirtless；a shirtless man。',
 'shirtless 只明确上身无衣，naked 常指更广泛的赤裸；不要把一个局部 -less 过度扩成全身。',
 ('A shirtless runner passed us on the beach.','一位赤裸上身的跑者从我们身边跑过沙滩。'),('The painting shows a shirtless worker beside the river.','画中是一位在河边赤裸上身的工人。'))
W('undershirt','英 /ˈʌndəʃɜːt/；美 /ˈʌndərʃɜːrt/','汗衫、内穿上衣',
 '穿在外层上衣里面的一件内衣，用 under 表层次在下、在里；它可以有袖，也可无袖。',
 'under- 在下面、里面 + shirt，上衣底下再穿的内衣。不是低级、较差的一件 shirt。',H[:1]+[['under- + shirt → undershirt','穿在外层上衣里面的衣物']],
 'a cotton undershirt 棉汗衫，wear an undershirt 穿汗衫，a sleeveless undershirt 无袖汗衫。',
 'a cotton undershirt；wear an undershirt；a sleeveless undershirt。',
 'undershirt 内穿上衣，underwear 内衣总类更广；英式 vest 在相应语境可指汗衫，美式 vest 又常背心外衣。',
 ('He wore a cotton undershirt beneath his uniform.','他在制服里穿了件棉汗衫。'),('The drawer held socks and undershirts.','抽屉里放着袜子和汗衫。'))
R('B2910','上半身衣物，再按内外、功能拆组合','SHIRT：基础上衣，前后材料告诉你穿在哪、用来做什么','shirt → shirtless、undershirt；sweatshirt 运动休闲上衣，redshirt 在不同历史场景有专门意义。',
 'shirtless 只明确无上衣，undershirt 不一定无袖；shirt/skirt 同族历史不能抹掉现代词义差别。',
 'scyrte 经中古英语 → shirt；shirt + -less；under-/sweat/red + shirt。',
 [['基础、无上衣与内穿','shirt · shirtless · undershirt'],['具体款式、用途和名称','sweatshirt · redshirt']],
 'shirt/skirt 上衣裙子；shirtless/naked 局部与更广赤裸；undershirt/underwear 具体与总类。',
 'He changed his shirt but kept the same undershirt on.\n\n他换了外面的衬衫，里面仍穿着同一件汗衫。','shirt shirtless undershirt sweatshirt redshirt')
W('historicity','/ˌhɪstəˈrɪsəti/','历史真实性；具有具体历史条件的性质〔学术语境〕',
 '问故事里的人物、事件到底有没有发生过，是在问 historicity；另一些学术讨论则问某观念如何受具体历史塑造。',
 '可能经法语 historicité，或由拉丁 historicus 接 -ity 等形成；现代可对照 historic + -ity。不是 historic 意义重大这一义机械变成重大程度。',
 [['希腊、拉丁历史词族 → historic 等相关形容词','历史的、有关历史的'],['historicité 等 → historicity；对应 historic + -ity','历史真实性；受历史形成的性质']],
 'the historicity of a story 故事的历史真实性，question the historicity 质疑是否确有其事，debate historicity 讨论历史真实性。',
 'the historicity of；question the historicity；debate historicity。',
 'historicity 常问是否有史实依据，不等于 historical importance 历史重要性；重要故事也可能含虚构。',
 ('The historian questioned the historicity of the account.','历史学者质疑这段记述的历史真实性。'),('The chapter separates the legend’s meaning from its historicity.','这一章把传说的意义与它是否确有史实依据分开。'))
R('B3417','历史关联、历史意义与史实真实性','HISTORIC：意义重大、属于历史、是否确有其事，别混成一件事','historic → historically、prehistoric；historicity 问真实性及历史形成性质。',
 'historic 常强调历史意义，historically 说从历史看，prehistoric 说史前；historicity 不自动夸一个事件很重要。',
 '希腊、拉丁历史词族经法语英语 → historic；historic + -ally；pre- + historic；historicité 等 → historicity。',
 [['历史意义、视角与时期','historic · historically · prehistoric'],['是否确有史实','historicity']],
 'historic/historical 常见侧重有差别；historicity/historical importance 真实性与重要性；prehistoric 非只指很旧。',
 'The account is historically important, even though its historicity is debated.\n\n这段记述很有历史意义，尽管其史实真实性仍有争论。','historic historically prehistoric historicity')
ROOTS[-1]['exclude']['historicism']='涉及多种学术理论与艺术史用法，现阶段先掌握 historic、historically、prehistoric 和 historicity。'
W('max','/mæks/','最大值、最高限度；最大的；达到上限〔max out〕',
 '把 maximum 这个长词缩成日常的 max：音量、容量或可做程度到顶，就是到上限。',
 'maximum 的截短，max 字母不再拆小词根；动词 max out 按到达、用尽上限理解。人名 Max 则另看专名历史。',
 [['拉丁 maximus 等 → maximum','最大的、最大量'],['maximum 截短 → max；max out','最大值、上限；达到或用尽上限']],
 'at the max 在最大限度，turn it up to the max 调到最大，max out the settings 把设置调满，ten minutes max 最多十分钟。',
 'to the max；ten minutes max；max out the settings。',
 'max 口语简称，maximum 较完整；max 与 min 最小值对比，Max 大写人名不必是最大值。',
 ('The walk takes ten minutes max.','走过去最多十分钟。'),('The volume was turned up to the max.','音量调到了最大。'))
R('B4390','最大值的口语简称与上限','MAX：maximum 缩短，日常拿来讲到顶','max → supermax，把最大上限及特定超级最高戒备名称分开。',
 'max out 可达到、用尽上限；supermax 的监狱专门义不能靠 super 直接推断所有制度细节。',
 'maximum → max；super- + max → supermax。',
 [['最大值与加强组合','max · supermax']],
 'max/min 最大最小；Max 专名与数值简称分开；supermax 专门场景看实际用法。',
 'The display was set to the max.\n\n显示设置调到了最大。','max supermax')
M=[['古英语 mete → 中古英语 mete → meat','原泛指食物、营养'],['语义逐渐缩窄','常指供食用的动物肉；旧宽义在部分组合中保留'],['食物形态与比喻','meatball、meatloaf；meaty 内容充实；mincemeat 有现代水果馅义']]
W('meat','/miːt/','肉、肉类；主要内容、实质；果仁等可食部分〔特定语境〕',
 '现代常说餐盘里的肉；the meat of the discussion 把真正有料的核心比作肉，不是讨论中突然端出一盘菜。',
 '古英语 mete 原泛指食物，后来常用义缩窄到肉类。旧的可食部分意义仍能帮助理解 coconut meat 等；不能拿现代狭义覆盖所有旧组合。',M,
 'raw meat 生肉，cooked meat 熟肉，a cut of meat 一块某部位的肉，the meat of the issue 问题实质，coconut meat 椰肉。',
 'raw meat；cooked meat；a cut of meat；the meat of the issue。',
 'meat 食物肉，flesh 身体组织范围更广；meat 和 meet 同音，meet 见面不是肉的动词形式。',
 ('They bought fresh meat for dinner.','他们买了新鲜肉类准备晚饭。'),('Let us get to the meat of the issue.','我们进入问题的实质吧。'),
 sources=['https://en.wiktionary.org/wiki/meat#English','https://www.etymonline.com/word/meat'])
W('meaty','/ˈmiːti/','肉多的、含肉的；肉味浓的；内容充实的',
 '菜里肉很足，或文章、角色有很多值得细看的内容，都可以说 meaty；不是所有用法都在量体重。',
 'meat + -y，性质形容词。从肉的量、口感引申到内容有料、可供深入处理。',M[:2]+[['meat + -y → meaty','肉多、肉感浓；再引申充实有料']],
 'a meaty stew 肉足的炖菜，a meaty role 有发挥空间的角色，a meaty discussion 内容充实的讨论。',
 'a meaty stew；a meaty role；a meaty discussion。',
 'meaty 可说口感、内容，不保证所有 meaty flavour 都来自动物肉；meatless 无肉与 meaty 肉感并非绝不可能同现。',
 ('The actor wanted a meaty role.','演员想要一个有发挥空间的角色。'),('The article offers a meaty discussion of the problem.','文章对问题作了内容充实的讨论。'))
W('meatless','/ˈmiːtləs/','无肉的、不含肉的',
 '这顿饭、这道菜没有肉；它说少了 meat，并没有顺便把鸡蛋、奶制品等都排除。',
 '古英语 metelēas 原可说没有食物，随着 meat 词义缩窄，现代 meat + -less 通常理解无肉。旧义和现代义的范围不同。',M[:1]+[['古英语 metelēas → 中古英语 meteles → meatless','早期无食物'],['meat 义缩窄后的现代用法','没有肉、不含肉']],
 'a meatless meal 无肉餐，meatless dishes 无肉菜肴，a meatless sauce 不含肉的酱。',
 'a meatless meal；meatless dishes；a meatless sauce。',
 'meatless 不必等于 vegan 纯素；是否含奶、蛋等要看食物成分，单词本身只否定肉。',
 ('The restaurant offers several meatless dishes.','餐厅提供几道无肉菜肴。'),('We made a meatless sauce with tomatoes and mushrooms.','我们用番茄和蘑菇做了一份无肉酱。'))
W('meatball','英 /ˈmiːtbɔːl/；美 /ˈmiːtbɔːl/','肉丸；好打的球〔棒球口语〕',
 '把碎肉拌好搓成球，就是 meatball；棒球里有时借说一个投得很容易被打的球，不是球真用肉做成。',
 'meat 肉 + ball 球，先按食物形状组合；其他口语义沿人物、易击球等场景发展，不能只按菜名翻每句话。',M[:2]+[['meat + ball → meatball','球形肉食'],['体育等口语引申','容易击打的来球等']],
 'meatballs in sauce 酱汁肉丸，a plate of meatballs 一盘肉丸，serve meatballs 上肉丸。',
 'meatballs in sauce；a plate of meatballs；serve meatballs。',
 'meatball 是团成球形，meatloaf 是整块条状再切片的菜；plant based meatballs 可按替代原料、外形借名。',
 ('She served meatballs with tomato sauce.','她端上了配番茄酱的肉丸。'),('The café added mushroom meatballs to the menu.','咖啡馆把蘑菇肉丸加入了菜单。'))
W('meatloaf','英 /ˈmiːtləʊf/；美 /ˈmiːtloʊf/','肉糜烤饼、烤肉卷〔整块条状肉菜〕',
 '把调好的肉糜等压成类似一条面包的形状烤熟，常切片吃；loaf 在这里借外形，不说里面一定全是面包。',
 'meat 肉 + loaf 一条、整条面包形，组合为特定肉菜名称。配方可含面包屑等，但名称重点是肉与成条形态。',M[:2]+[['meat + loaf → meatloaf','肉糜做成面包般整条形状的菜']],
 'a slice of meatloaf 一片烤肉卷，homemade meatloaf 自制肉糜烤饼，serve meatloaf 上整条烤肉菜。',
 'a slice of meatloaf；homemade meatloaf；serve meatloaf。',
 'meatloaf 不是 meatball 多搓大一点就随意换名，菜式通常有自己的形状、烹调习惯；loaf 多指整条。',
 ('She served slices of meatloaf with vegetables.','她端上切片肉糜烤饼和蔬菜。'),('The leftover meatloaf went into sandwiches.','剩下的烤肉卷用来夹三明治。'))
W('meatpacking','/ˈmiːtpækɪŋ/','肉类屠宰加工、肉品加工包装业',
 '行业里从处理肉到加工、包装的一整段业务，不只是最后拿塑料袋装一块肉。',
 'meat 肉 + packing 加工、装包相关活动名。行业名的实际范围比字面一次打包更大。',M[:2]+[['meat + packing → meatpacking','肉类处理、加工与包装的业务、行业']],
 'a meatpacking plant 肉类加工厂，the meatpacking industry 肉类加工包装业，meatpacking workers 肉类加工工人。',
 'a meatpacking plant；the meatpacking industry；meatpacking workers。',
 'meatpacking 是行业活动，a meat pack 一包肉是具体包装单位；plant 这里工厂不是植物。',
 ('The town grew around a meatpacking plant.','小镇围绕一家肉类加工厂发展起来。'),('The report described working conditions in meatpacking.','报告描述了肉类加工行业的工作条件。'))
W('meathead','/ˈmiːthed/','笨蛋；空有肌肉的人〔贬义口语〕',
 '骂人像脑袋里只有肉、没动脑子，有时也把魁梧却不聪明的刻板印象压在对方身上；不是正式能力判断。',
 'meat 肉 + head 头，组成贬低人物的比喻称呼。这个词早于后来使它流行的电视角色，并非某部电视剧才首次创造。',M[:2]+[['meat + head → meathead','把头脑比作一团肉的贬称']],
 'call someone a meathead 骂某人笨蛋，a complete meathead 十足笨蛋，the stereotype of a meathead 空有肌肉者的刻板印象。',
 'call someone a meathead；a complete meathead；a rude nickname。',
 'meathead 是侮辱、刻板印象，不证明肌肉发达的人更笨；meaty discussion 则可正面夸内容有料。',
 ('The comedian played a lovable meathead.','喜剧演员扮演了一个傻得可爱的角色。'),('The reviewer criticized the character as a meathead stereotype.','评论者批评这个角色落入空有肌肉的刻板印象。'))
W('mincemeat','/ˈmɪnsmiːt/','甜馅〔常为干果、香料、油脂混合，用于 mince pies〕；绞肉〔部分用法〕',
 '看英国 mince pie 的 mincemeat，现代常是甜的干果馅，未必有绞肉，也可能有动物脂；别只凭 meat 就期待一口肉饼。',
 '由较早 minced meat 等形式变化，现代可拆 mince 切碎 + meat。历史配方与现代果馅发展让名称留下旧材料痕迹；make mincemeat of 又借切碎说彻底击败。',M[:2]+[['minced meat → mincemeat；对应 mince + meat','切碎的食材、肉'],['配方、固定说法的后续变化','现代常见水果甜馅；make mincemeat of 彻底击败']],
 'mincemeat filling 甜果馅，a jar of mincemeat 一罐甜馅，make mincemeat of an opponent 彻底击败对手。',
 'mincemeat filling；a jar of mincemeat；make mincemeat of。',
 'minced meat 通常直说绞肉，mincemeat 连写在英式糕点里常甜果馅；无绞肉也不自动等于不含任何动物来源成分。',
 ('She filled the small pies with mincemeat.','她往小馅饼里填入甜果馅。'),('Their team made mincemeat of the opposition.','他们队把对手打得毫无招架之力。'),
 sources=['https://en.wiktionary.org/wiki/mincemeat#English','https://www.etymonline.com/word/mincemeat'])
R('B2465','原来泛说食物，现代常指肉；再借给实质内容','MEAT：肉是现代常义，旧食物义和食谱名称会留痕','meat → meaty、meatless；meatball、meatloaf、meatpacking 看形状与行业；meathead 贬称，mincemeat 看甜馅和绞肉语境。',
 'meaty role 有发挥空间，meatless 未排除奶蛋，mincemeat 现代甜馅未必含肉。每个组合的实际用法比机械逐字译更关键。',
 'mete 食物 → meat 常用义缩窄；meat + -y/-less/ball/loaf/packing/head；minced meat → mincemeat。',
 [['物质、性质与无肉','meat · meaty · meatless'],['菜式、加工与旧名称','meatball · meatloaf · meatpacking · mincemeat'],['人物比喻','meathead']],
 'meat/meet 同音；meaty 内容充实；meatless/vegan 不同范围；mincemeat/minced meat 糕点甜馅与绞肉；meathead 贬义刻板印象。',
 'The meatless menu still offered a meaty discussion topic for the food club.\n\n无肉菜单仍给美食小组提供了一个很有料的话题。','meat meaty meatless meatball meatloaf meatpacking meathead mincemeat')
if __name__=='__main__':save('continuation_20261030_es',ROOTS,WORDS)
