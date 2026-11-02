"""Small and large, intensified praise, familiar names and everyday verb forms."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
def S(word,base):
 urls=['https://en.wiktionary.org/wiki/'+word+'#English']
 if base in ['micro','mega']:
  urls+=['https://www.etymonline.com/word/'+base+'-','https://www.merriam-webster.com/dictionary/'+base]
 else:urls.append('https://www.etymonline.com/word/'+base)
 return urls
EXISTING_ROOT_ADDITIONS={
 'C0736':dict(words='micro'.split(),label='micro：小的组合形式到独立形容词、短称',note='micro 接希腊 mikros、smikros 小，现代也能独立形容微小、微观。名词可能缩略 microcomputer、microprocessor 等；按场景还原，不只认同一长词。'),
 'C0714':dict(words='mega'.split(),label='mega：大的组合形式到巨大、很棒的口语',note='mega 接希腊 megas 大、重要；科学组合有百万倍的精确用法，现代口语独立形容巨大、很棒时不直接表示恰好一百万。'),
 'B3887':dict(words='terrific terrifically'.split(),label='terrific → terrifically：恐惧强烈到棒极了',note='拉丁 terrificus 接 terrere 使恐惧 + facere 使、做的材料；英语从令人害怕扩大为很强烈，再有棒极了的口语赞美。副词 -ic 后常以 -ically 形成，不漏掉中间字母与音节。'),
 'B3026':dict(words='coke cokes'.split(),label='coke：焦炭一支；饮料、药物名称缩略另支',note='与 coal 比较燃料，coke 焦炭来自英格兰北部词，可能接旧 colke 核心、木炭等材料，远源不定。饮料 Coke 缩略 Coca-Cola，可卡因俗称 coke 缩略 cocaine，各自有来源。'),
 'C1090':dict(words='bobby bobbies'.split(),label='bobby：Robert 的昵称借给英国警察',note='与 police 比较职业称呼，不由希腊 polis 派生。bobby 指警察的称呼接 Robert Peel 的昵称 Bobby，和其推动伦敦警察制度的历史有关；Bob 的昵称小称形式再成为普通名词。'),
 'C0287':dict(words='guinea guineas'.split(),label='guinea：另源的旧英国金币名',note='与 coin 比较货币，不由 coin 派生。guinea 金币名接西非 Guinea 地名，与历史上使用非洲黄金等背景有关；不是现代字面 guin 加货币后缀 ea。'),
 'B2656':dict(words='bastard bastards'.split(),label='bastard：带历史偏见的出身称呼到粗口',note='与 child 比较历史称谓，不由 child 派生。bastard 借古法语，远源有鞍具材料与婚姻相关日耳曼语词等不同分析，不能把鞍上出生故事当定论；现代常见粗口、带感情色彩称呼。'),
 'B3890':dict(words='butt butts butted butting'.split(),label='butt → butts、butted、butting：末端、顶撞与插话',note='butt 多支来源有交织：厚末端、烟头；法语 buter 推撞动词；靶子到笑柄；臀部义可能接末端或 buttock。不要全部由现代屁股名词造出，butt in 插话接顶入、闯入关系。'),
 'B3626':dict(words='skid skids skidded skidding'.split(),label='skid：垫木、制动块到轮子滑行',note='与 ski 较远北欧木片词族可能相关，不是现代英语 ski 加 d。skid 名词先见垫木、木梁；动词制动轮子到轮不转而滑、侧滑，现代名词滑行又随动词发展。'),
 'B4350':dict(words='cope copes'.split(),label='cope → copes：应付、处理眼前困难',note='现代 cope 接法语打击、交锋材料，交手到应对的关系；copes 是第三人称单数，通常接 with 表应付对象。宗教披风 cope 是另源名词。'),
}
TERRIFIC=[['拉丁 terrere 使恐惧 + facere 使、做的材料 → terrificus','令人害怕、带来恐惧的'],['英语 terrific：可怕 → 程度强烈 → 棒极了','terrific + 副词构词 -ally 等拼写关系 → terrifically，保留程度与赞美用法']]
COKE=[['焦炭 coke：英格兰北部旧词，可能接 colke 核心、木炭等','更远来源不明；不要由现代 coal 随意变形解释'],['饮料 Coke：Coca-Cola 缩略；药物俗称 coke：cocaine 缩略','同形不等于煤、饮料、药物都来自一条词源']]
BOBBY=[['Robert 的昵称 Bob、Bobby → Robert Peel 的称呼','其推动伦敦警察制度的历史，给职业昵称提供背景'],['bobby 成为英国警察的非正式称呼 → bobbies','昵称的人名材料借给普通职业名词']]
GUINEA=[['西非 Guinea 地名 → 英国 guinea 金币名','历史贸易与非洲黄金背景，不是英语 coin 的派生'],['旧币名继续用于历史价钱、记账单位等','复数 guineas；更远地名来源不完全确定']]
BASTARD=[['古法语 bastard → 英语 bastard，旧时用于非婚生者的带偏见称谓','远源有鞍具、婚姻词等不同分析，具体故事不确定'],['从出身、被视为不正统的旧标签 → 普通粗口及情绪化称呼','现代骂人或熟人玩笑时，通常不在陈述对方的出生事实']]
BUTT=[['末端、短粗部分名词与法语推撞动词等多线交织','烟头是留下的末端；臀部、笑柄等各有发展，不能强制一条时间链'],['butt 动词顶撞、接合 → butt in 插入谈话','现代 s、-ed、-ing 按相应名词或动词用法变化']]
SKID=[['skid 垫木、木梁，可能接北欧木片材料','和 ski 可能较远同族，不是现代 ski 加后缀 d'],['给轮子用制动块 → 轮子不转地滑行 → 侧滑','滑行名词用法随动词发展，现代常见车辆打滑']]
W('micro','英 /ˈmaɪkrəʊ/；美 /ˈmaɪkroʊ/','很小的、微观的；微型计算机等的短称',
 '把镜头拉近，看一个很小的层面，就是 micro。它能作组合形式，也能独立修饰 level、detail 等，表示微观、很细小。',
 'micro- 接希腊 mikros、smikros 小，经拉丁化形式用于现代构词；独立形容词保留小的意义，某些名词短称则来自 microcomputer、microprocessor 等具体长词。',
 [['希腊 mikros、smikros 小 → micro- 组合形式','现代可形成许多微型、微观相关词'],['micro 独立形容词；名词按场景缩略具体长词','微观层面不等于每次都是精确的百万分之一']],
 'at the micro level 是在微观层面；micro details 是细节层面；a micro 在特定计算机历史语境可指微型计算机。',
 'at the micro level；micro details；micro changes。',
 '科学计量组合 micro- 有精确数量含义；a micro-level view 的日常分析则说观察尺度，不能把每个 micro 都机械换成数字。',
 ('The study examines change at the micro level.','研究从微观层面考察变化。'),('We need to consider both macro and micro factors.','我们需要同时考虑宏观与微观因素。'),sources=S('micro','micro'))
W('mega','英、美 /ˈmeɡə/','巨大的、超级的；很棒的〔口语〕',
 '事情大到让人“哇”一声，或表现特别棒，随意口语里可以说 mega。它把“大、重要”的词根劲头直接拿来加强程度。',
 'mega- 接希腊 megas 大、强大、重要；现代独立形容词再表示巨大、极出色。科学单位中的百万倍含义，是另一种精确约定用法。',
 [['希腊 megas 大、重要 → mega- 组合形式','既有普通大的意义，也有科学数量约定'],['mega 独立作口语形容词','巨大、很棒，不要求恰好一百万个单位']],
 'a mega event 可说大型活动；that was mega 可以是那太棒了；具体口语接受度有地区、语体差异。',
 'a mega event；a mega success；that was mega。',
 'mega 的口语夸赞不需要出现可计数数量；megawatt 的科学前缀则不能任意当作很棒来换算。',
 ('The concert turned into a mega event.','这场音乐会办成了一场大型活动。'),('“That was mega!” she said after the show.','演出后她说：“太棒了！”'),sources=S('mega','mega'))
W('terrific','英、美 /təˈrɪfɪk/','极好的；很强烈、巨大的；〔旧义〕令人恐惧的',
 'A terrific performance 今天通常是“表演棒极了”，词源却真有恐惧：强烈到让人害怕，再泛成强烈得惊人，最后也能强烈得让人赞叹。',
 '拉丁 terrificus 接 terrere 使恐惧 + facere 使、做的构词材料；英语先有令人害怕，后来扩大为很强烈、过度，再有极好的口语义。',TERRIFIC,
 'a terrific job 是很棒的工作；a terrific noise 是巨响；terrific speed 是惊人的速度。所修饰的对象决定是夸赞还是单说强度。',
 'a terrific job；a terrific performance；a terrific noise。',
 'terrific 今天常是褒义，terrible 常是糟糕、可怕；远源同有恐惧，不保证现代褒贬相同。',
 ('You did a terrific job on the presentation.','这次演示你做得太棒了。'),('The door slammed with a terrific bang.','门砰的一声关上，响声巨大。'),sources=S('terrific','terrific'))
W('terrifically','英、美 /təˈrɪfɪkli/','极其、非常；非常出色地',
 'terrifically useful 是特别有用；played terrifically 是发挥得很棒。它把 terrific 的强烈程度、出色评价带到副词位置。',
 'terrific 的 -ic 结尾，常见副词拼写接 -ally → terrifically，即 -ically 的外观；常见发音 /fɪkli/，不把每个书写元音都读成独立音节。',TERRIFIC+[['terrific + -ally → terrifically','-ic 形容词常见副词构词；现代表示极其、很出色地']],
 'terrifically useful 是极有用；terrifically busy 是忙极了；performed terrifically 是表现得非常出色。',
 'terrifically useful；terrifically busy；played terrifically。',
 'terrific 是形容词，terrifically 是副词；a terrific result 与 performed terrifically，分别修饰结果和表现动作。',
 ('The notes were terrifically useful during revision.','复习时，这些笔记特别有用。'),('The team played terrifically in the second half.','球队下半场发挥得非常出色。'),sources=S('terrifically','terrific'))
W('coke','英 /kəʊk/；美 /koʊk/','焦炭；〔Coke〕可口可乐；〔俗语〕可卡因',
 '炼铁语境里的 coke 是焦炭；点饮料说 a Coke 常是可口可乐。这些词看起来一样，却不是把煤做成饮料那样的一条意思演化。',
 '焦炭一支来自英格兰北部词，可能接旧 colke 核心、木炭，远源不明；饮料 Coke 缩略 Coca-Cola；药物俗称 coke 则缩略 cocaine。',COKE,
 'coal and coke 是煤与焦炭；a Coke 是一份可口可乐；语境谈药物时，小写 coke 又可能是 cocaine 的俗称。数量、大小写与上下文一起看。',
 'coal and coke；a Coke；a glass of Coke。',
 'Coke 饮料通常保留大写品牌习惯，小写也可能出现在随意文字里；大小写有帮助，不能脱离上下文当作唯一判据。',
 ('The old works used coal and coke as fuel.','旧工厂用煤和焦炭作燃料。'),('She ordered a coke with her lunch.','她吃午饭时点了一份可乐。'),sources=S('coke','coke'))
W('cokes','英 /kəʊks/；美 /koʊks/','可乐饮料〔按杯、瓶、份计的复数〕',
 '桌上两杯可乐，口语可以说 two cokes。这里把本来可按液体说的饮料名，按一份份点单来数。',
 'coke + -s → cokes，/k/ 后后缀读 /s/。饮料份数用法属于 Coke、coke 的现代可数转换；焦炭材料通常不可数，专业比较种类时另可用复数。',COKE+[['coke + -s → cokes','本组先学饮料份数，后缀 /s/']],
 'two cokes 可说两份可乐；cans of coke 明说罐数；glasses of coke 明说杯数。品牌名规范书写也常用 Cokes。',
 'two cokes；cold cokes；a couple of cokes。',
 '点单的 cokes 往往省略一杯、一瓶等单位；需要确定容器时说 cans of coke、bottles of coke。',
 ('We ordered two cokes and a lemonade.','我们点了两份可乐和一份柠檬汽水。'),('The waiter brought the cokes to our table.','服务员把可乐端到我们桌上。'),sources=S('cokes','coke'))
W('bobby','英 /ˈbɒbi/；美 /ˈbɑbi/','英国警察〔非正式、常带传统色彩〕',
 '英国老照片、小说里戴着传统头盔的警察，常会被叫 a bobby。这个职业昵称借的是一个人的名字，不是警察工作的动作。',
 'Robert 的昵称 Bob、Bobby，与推动伦敦警察制度的 Robert Peel 相联系，成为普通警察称呼 bobby。名字的小称形式后来指一类职业。',BOBBY,
 'a bobby on the beat 是巡逻警察；a London bobby 是伦敦警察。现代普通、通用名称仍可用 police officer。',
 'a London bobby；a bobby on the beat；a local bobby。',
 'Bobby 大写可为人名，bobby 小写可为职业昵称；后者有英国、传统口语色彩，不是所有国家警察的中性名称。',
 ('A bobby stood at the corner of the street.','一名英国警察站在街角。'),('The old photograph shows a bobby in a tall helmet.','老照片中是一名戴高头盔的英国警察。'),sources=S('bobby','bobby'))
W('bobbies','英 /ˈbɒbiz/；美 /ˈbɑbiz/','英国警察们〔bobby 的复数〕',
 '几位英国警察，是 bobbies。原本是人物昵称衍生的普通名词，进入英语词汇后照常变化复数。',
 'bobby 词尾辅音字母 b + y，变 y 为 i + -es → bobbies；原 /i/ 保留，再接 /z/。',BOBBY+[['bobby 变 y 为 i + -es → bobbies','多名英国警察；词尾 /biz/']],
 'London bobbies 是伦敦警察们；two bobbies 数两位；bobbies on bicycles 是骑车的英国警察。',
 'London bobbies；two bobbies；bobbies on the beat。',
 'bobbies 不是给不同人名 Bobby 都自动用来作正式职业称呼；它作为普通警察词义，有特定地区、语体背景。',
 ('Two bobbies helped direct the traffic.','两位英国警察帮忙指挥交通。'),('The film recreates the world of bicycles, trams and bobbies on the beat.','电影重现了自行车、有轨电车和街头巡警的时代风貌。'),sources=S('bobbies','bobby'))
W('guinea','英、美 /ˈɡɪni/','基尼〔旧英国金币、计价单位〕',
 '旧小说、旧价目表里的 a guinea，是一种历史货币名称。名字借自西非 Guinea 地名，把当时贸易、黄金来源的背景留在钱币上。',
 'Guinea 地名 → guinea 金币名，与历史上对西非的贸易及非洲黄金有关。地名更远来路不完全确定，词尾 -ea 不是英语里通用的货币后缀。',GUINEA,
 'a gold guinea 是一枚基尼金币；a guinea fee 是以基尼计的费用；旧价格里的单位不应直接当成今天常见货币名称。',
 'a gold guinea；a fee of one guinea；an old guinea coin。',
 'guinea pig 是豚鼠，属于另一个完整动物名；它的命名路线有不同分析，不能只因含 Guinea 就判定动物原产西非。',
 ('The museum displays a gold guinea.','博物馆展出了一枚基尼金币。'),('The old receipt lists a fee of one guinea.','旧收据上列着一基尼的费用。'),sources=S('guinea','guinea'))
W('guineas','英、美 /ˈɡɪniz/','基尼金币；按基尼计的金额〔复数〕',
 '几枚旧金币，或旧书里几基尼的费用，是 guineas。即使实体钱币退出日常使用，名称还可能在历史计价习惯里留下。',
 'guinea + -s → guineas，基础词末尾 ea 在这里读 /i/，复数再加 /z/；直接加 s，不改成 -ies。',GUINEA+[['guinea + -s → guineas','旧币、历史计价单位的复数；读 /ˈɡɪniz/']],
 'five guineas 是五基尼；gold guineas 是基尼金币；priced in guineas 是以基尼计价，常见于旧资料、特定传统语境。',
 'five guineas；gold guineas；priced in guineas。',
 'guineas 与 pennies、pounds 是不同单位名称。看到旧金额，要先认单位，不仅把数字直接读成同样多的英镑。',
 ('The old catalogue priced the painting at ten guineas.','旧目录把这幅画标价为十基尼。'),('He kept two gold guineas in the collection.','他的收藏里有两枚基尼金币。'),sources=S('guineas','guinea'))
W('bastard','英 /ˈbɑːstəd/；美 /ˈbæstɚd/','混蛋〔粗口〕；家伙〔情绪化称呼〕；〔旧时带偏见称谓〕非婚生者',
 '现代对白里一句 bastard 常是在骂“混蛋”，并不是调查对方的家庭。它从旧时带出身偏见的称谓，发展成泛指人的粗口。',
 '借古法语 bastard。更远有联系鞍具材料、婚姻相关日耳曼词等不同分析；鞍具上的出生故事只是旧解释，不能当成确知来历。',BASTARD,
 'an arrogant bastard 是骂傲慢的人；a lucky bastard 可以在熟人间带又羡慕又调侃的语气；历史资料的出身称谓则要按旧语境理解。',
 'a lucky bastard；a poor bastard；an arrogant bastard。',
 '这个词通常粗俗；lucky、poor 等搭配又可减弱敌意、带羡慕或同情。不能仅凭一个中文“混蛋”判断每段对白的情绪。',
 ('“You lucky bastard,” he said with a laugh.','“你这走运的家伙。”他笑着说。'),('The old chronicle labels the prince a bastard.','这部旧编年史用当时的出身称谓把王子记作非婚生者。'),sources=S('bastard','bastard'))
W('bastards','英 /ˈbɑːstədz/；美 /ˈbæstɚdz/','混蛋们、家伙们〔粗口或情绪化复数〕；〔旧称〕非婚生者们',
 '几个人被愤怒地骂，或熟人被半开玩笑地羡慕，都可能听见 bastards。复数数人，具体敌意要看语气、修饰词。',
 'bastard + -s → bastards，/d/ 后复数后缀读 /z/；现代粗口和旧历史称谓都可形成复数，不代表说话者每次真在陈述出生情况。',BASTARD+[['bastard + -s → bastards','多人的称呼；词尾 /dz/']],
 'lucky bastards 常带羡慕、调侃；poor bastards 可带同情；angry insults 中则可能有很强敌意。读对白时一起看人物关系。',
 'lucky bastards；poor bastards；arrogant bastards。',
 'bastards 的旧出身用法反映历史偏见；现代泛骂用法也很粗俗，作为阅读识别词与中性 people 的语气差别明显。',
 ('“Lucky bastards—they got the last two tickets,” she joked.','“这两个走运的家伙，买到了最后两张票。”她开玩笑说。'),('He muttered “bastards” after finding his bicycle stolen.','发现自行车被偷后，他低声骂了句“混蛋”。'),sources=S('bastards','bastard'))
W('butts','英、美 /bʌts/','烟头、末端；屁股〔复数〕；用头顶、顶撞〔第三人称单数〕',
 '地上留下的烟头，是 cigarette butts；山羊用头顶门，是 it butts the gate。一个抓留下的末端，一个抓往前顶的动作，多支旧来源在同一个词形里碰面。',
 'butt + -s → butts，/t/ 后接 /s/。末端名词、顶撞动词有交织的日耳曼语及法语来源；臀部义又与厚末端、buttock 等有联系，不能全由现代屁股造出来。',BUTT+[['butt + -s → butts','名词复数；或顶撞动词第三人称单数']],
 'cigarette butts 是烟头；the goat butts 是山羊用头顶；work our butts off 是拼命干活的随意说法。',
 'cigarette butts；butts the gate；work our butts off。',
 'butts 与 buts 转折 but 的名词化复数可同音；no ifs or buts 是不许找借口，不是这里的烟头或顶撞。',
 ('Cigarette butts lay near the bench.','长椅旁落着烟头。'),('The goat butts the gate whenever someone approaches.','每当有人走近，山羊就用头顶门。'),sources=S('butts','butt'))
W('butted','英、美 /ˈbʌtɪd/','用头顶撞了；端头相接了；插话了〔过去式、过去分词〕',
 '羊把头往前一顶，是 butted；谈话里把自己的话突然顶进去，是 butted in。物理动作到对话动作很直观。',
 'butt + -ed → butted，词根原已有双 t，直接加后缀；/t/ 后 -ed 读 /ɪd/，增加音节。',BUTT+[['butt + -ed → butted','保留已有 tt，不再添第三个 t']],
 'butted the gate 是顶门；butted in 是插话；butted the boards together 是让木板端头相接，后一用法也有 abut 影响。',
 'butted the gate；butted in；butted the boards together。',
 'butted in 常带未经邀请、打断别人的意味；joined the conversation 可只是加入谈话，语气不一定冒失。',
 ('The ram butted the wooden gate.','公羊用头顶了木门。'),('He butted in before she had finished speaking.','她话还没说完，他就插了进来。'),sources=S('butted','butt'))
W('butting','英、美 /ˈbʌtɪŋ/','正在用头顶撞；插话；端头接合的过程',
 '一只头往前顶，或一句话往别人的话里顶，这个过程是 butting。butting in 一出现，常能听出说话者嫌对方打断。',
 'butt + -ing → butting，基础词已有 tt，直接接 -ing；不是以单 t 的 but 变出顶撞词。',BUTT+[['butt + -ing → butting','现在分词、动名词；保留基础双 t']],
 'butting against a gate 是顶着门；butting in 是插话；butting two boards together 是把两块板端头拼接。',
 'butting against the gate；butting in；butting boards together。',
 'butting in 说闯入谈话的方式；talking 只说正在讲话。上下文里，未经轮到就插进来才是重点。',
 ('The goat kept butting against the fence.','山羊不停用头顶围栏。'),('Sorry for butting in, but I think I can help.','抱歉打断一下，不过我觉得我能帮上忙。'),sources=S('butting','butt'))
W('skid','英、美 /skɪd/','打滑、侧滑；一次打滑；垫木、滑木',
 '车轮没能正常滚着抓住路面，车身滑出去，是 skid。这个现代画面背后还有木块、木梁的旧名称，并不从现代车祸才开始。',
 'skid 旧名词是垫木、木梁，可能接北欧木片词族；动词早有给车轮用制动块，后来指轮子不转而滑、再到侧滑。现代滑行名词又随动词发展。',SKID,
 'go into a skid 是进入打滑状态；skid on ice 是在冰上打滑；hit the skids 还可比喻陷入衰退，借向下滑的画面。',
 'go into a skid；skid on ice；hit the skids。',
 'slide 是较宽的滑动；skid 常用于轮胎失去正常滚动、抓地的车辆等。skid 往往强调非预期打滑，slide 还可用于有意、平稳的滑动。',
 ('The car began to skid on the icy road.','车在结冰路面上开始打滑。'),('A sudden skid left dark marks on the road.','一次突然打滑在路上留下了深色痕迹。'),sources=S('skid','skid'))
W('skids','英、美 /skɪdz/','打滑〔第三人称单数〕；滑木、垫木；打滑事件〔复数〕',
 'the car skids 是车打滑；一辆直升机下面的支撑滑架，也常叫 skids。它们共享旧木梁、滑动关系，但在句子里不是同一种词性。',
 'skid + -s → skids，/d/ 后后缀读 /z/。可数名词有复数，动词配单数主语也加 s。',SKID+[['skid + -s → skids','名词复数或动词第三人称单数；词尾 /dz/']],
 'helicopter skids 是直升机滑橇式起落架；the car skids 是车侧滑；hit the skids 比喻开始走下坡路。',
 'helicopter skids；the car skids；hit the skids。',
 'skids 可是支撑装置，也可是打滑动词；不要在每个有 skids 的句子里都自动找失控事故。',
 ('The helicopter rested on its skids.','直升机停在滑橇式起落架上。'),('The car skids whenever its wheels hit the icy patch.','车轮一碰到那块结冰处，车就打滑。'),sources=S('skids','skid'))
W('skidded','英、美 /ˈskɪdɪd/','打滑了、侧滑了〔过去式、过去分词〕',
 '车没沿着轮子原本的方向滚，而是突然滑开，是 skidded。过去形式把那次非预期滑动交代出来。',
 'skid 双写 d + -ed → skidded；短元音单音节词尾双写，/d/ 后 -ed 读 /ɪd/，增加一个音节。',SKID+[['skid 双写 d + -ed → skidded','规则过去式、过去分词；末尾 /dɪd/']],
 'skidded on ice 是在冰上打滑；skidded across the road 是滑过路面；skidded to a halt 是滑着停下，to 说明结果。',
 'skidded on ice；skidded across the road；skidded to a halt。',
 'skidded 不等于 crashed 撞上、坠毁；它只交代滑动，是否发生碰撞需看后续文字。',
 ('The car skidded on a patch of ice.','车在一块冰面上打了滑。'),('The bicycle skidded to a halt beside the gate.','自行车在门旁打滑着停了下来。'),sources=S('skidded','skid'))
W('skidding','英、美 /ˈskɪdɪŋ/','正在打滑、侧滑；打滑过程',
 '轮子抓不住地面，车辆正在横滑，这个持续过程是 skidding。它比单说 moving 把运动方式交代得更清楚。',
 'skid 双写 d + -ing → skidding；现在分词、动名词用同一形式，读 /ˈskɪdɪŋ/。',SKID+[['skid 双写 d + -ing → skidding','打滑的过程、行为；保留基础短元音']],
 'be skidding 是正在打滑；skidding on ice 是在冰上打滑；the sound of skidding tyres 是轮胎打滑声。',
 'skidding tyres；skidding on ice；skidding sideways。',
 'skidding 强调滑动，spinning 强调旋转；轮子可能空转，也可能锁住后滑行，两个词不能仅凭都与车辆有关就互换。',
 ('We heard the sound of skidding tyres outside.','我们听到外面轮胎打滑的声音。'),('The van was skidding sideways across the road.','货车正在路上横着滑动。'),sources=S('skidding','skid'))
W('copes','英 /kəʊps/；美 /koʊps/','应付、处理困难〔第三人称单数〕',
 '事情多、压力在眼前，她还能一项项处理，是 she copes。它常先说“能接住、应付下来”，不要求每件事都做到完美。',
 'cope + -s → copes，基础词已有 e，直接加 s；/p/ 后后缀读 /s/。现代应对动词较远接法语打击、交手材料，交手到应对，也可能受另一条旧交易动词影响。',
 [['法语 couper 等打击、交锋材料 → 英语 cope','从面对、应战到应付困难'],['cope + -s → copes','第三人称单数；常接 with 表对象']],
 'copes with pressure 是应对压力；copes well 是应付得好；copes on her own 是独自处理得来。',
 'copes with pressure；copes well；copes on her own。',
 '应付动词 cope 通常接 with；she copes with the workload，而非把所有情况都写成 copes the workload。宗教披风名词 cope 则是另一来源。',
 ('She copes well with a heavy workload.','她能很好地应付繁重工作。'),('He copes on his own when the rest of the team is away.','团队其他人不在时，他独自也能处理得来。'),sources=S('copes','cope'))
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_zit',ROOTS,WORDS)
 extend_lessons()
