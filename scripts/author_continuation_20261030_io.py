"""Selected useful colloquial -o words, with clipping and homographs separated."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
O=[['现代英语的口语 -o 构词模式','把词变成昵称、人物称呼或随意表达；不只有一个固定感情色彩'],['可接完整词，也可配合截短','kid → kiddo；conversation → convo 等'],['同样结尾未必同一构造','servo 的技术义是长词截短，另有 service station 的口语缩称']]
W('servo','英 /ˈsɜːvəʊ/；美 /ˈsɜːrvoʊ/','伺服机构、伺服电机；加油站〔澳大利亚口语，另线〕',
 '模型或机器里的 servo 常负责按控制要求转动、定位。澳大利亚口语说去 the servo，则通常是去加油站。',
 '技术义截短 servomotor、servomechanism 等，不能直接说 serv + 口语 -o。澳大利亚加油站义则由 service station 截取词干配 -o，恰好同形。',
 [['servomotor / servomechanism → servo','长技术词截短：伺服电机、机构'],['service station 截短配 -o → servo','澳大利亚口语的加油站']],
 'a small servo 小型伺服电机，servo control 伺服控制，stop at the servo 在加油站停一下〔澳口语〕。',
 'a small servo；servo control；stop at the servo。',
 'servo 不是任何电机的随意同义词；去加油站的地域口语与技术缩称分开。servomotor 中的 servo- 也不是服务员的昵称。',
 ('The model uses a small servo to move the arm.','模型用一个小型伺服电机带动机械臂。'),('“We’ll stop at the servo,” our Australian host said.','“我们在加油站停一下。”我们的澳大利亚东道主说。'),sources=['https://en.wiktionary.org/wiki/servo#English','https://www.merriam-webster.com/dictionary/servo'])
W('doggo','英 /ˈdɒɡəʊ/；美 /ˈdɔːɡoʊ/，也读 /ˈdɑːɡoʊ/','狗狗〔亲昵、网络口语〕；lie doggo 隐伏不动',
 '在宠物照片下叫一声 doggo，像说可爱的狗狗。旧搭配 lie doggo 却是躲着不动、别引人注意，不必真的在谈一只狗。',
 '名词 dog + -o，双写 g，带昵称语气。旧副词 doggo 见于 lie/play doggo，可能同源，但新旧用法的先后联系不硬说成唯一确定路线。',O[:1]+[['dog + -o → doggo 名词','亲昵、网络语中的狗'],['旧搭配 lie doggo','隐伏不动、不引人注意的另一用法']],
 'a sleepy doggo 困困的狗狗，a photo of a doggo 狗狗照片；lie doggo 暂时躲着不动。',
 'a sleepy doggo；a photo of a doggo；lie doggo。',
 'doggo 适合随意、可爱化语气，不是更正式的狗种名称。lie doggo 不能一字一字译成躺一只狗。',
 ('She posted a photo of a sleepy doggo.','她发了一张困困狗狗的照片。'),('The characters decide to lie doggo until the search is over.','故事人物决定隐伏不动，等搜寻结束。'))
W('dumbo','英 /ˈdʌmbəʊ/；美 /ˈdʌmboʊ/','笨蛋、傻瓜〔贬义口语〕',
 '把 dumb 的愚蠢评价变成一个人的称呼。它可以出现在玩笑里，也能伤人，不能当正式描述能力的中性词。',
 'dumb 愚蠢的 + -o 人物称呼。dumb 单独的 b 不发音，dumbo 通行读音里却有 /b/，别把原词的静音机械照搬。',O[:1]+[['dumb + -o → dumbo','带愚蠢评价的人物称呼']],
 'call someone a dumbo 叫某人笨蛋，feel like a dumbo 觉得自己像个傻瓜。Dumbo 首字母大写还可作虚构角色名，具体专名另看语境。',
 'call someone a dumbo；feel like a dumbo。',
 'dumbo 是说话人的贬低评价，不是智力或疾病分类。玩笑能否接受取决于关系和语境，正式表达可直接指出哪一步出了错。',
 ('He felt like a dumbo after finding the key in his pocket.','他在自己口袋里找到钥匙后，觉得自己像个傻瓜。'),('The teacher explained that calling a classmate a dumbo was hurtful.','老师解释说，叫同学笨蛋会伤人。'))
W('aggro','英 /ˈæɡrəʊ/；美 /ˈæɡroʊ/','麻烦、烦扰；挑衅、攻击性行为；强攻的〔口语、游戏〕',
 '现实里 aggro 可能是让人头疼的折腾，也可能是挑衅找事；游戏里拉到 aggro，则常说敌人的攻击注意转到了你身上。',
 'aggr- 截短词干配 -o，与 aggravation 烦扰、aggression/aggressive 攻击性都有联系；资料对最初截自哪一个分析不同，不强定唯一原词。',
 [['aggravation 与 aggression/aggressive 等相互影响','烦扰、攻击性这一组相关语义'],['截取 aggr- + -o → aggro','口语烦扰、挑衅；再形成游戏中的仇恨、强攻等用法']],
 'avoid the aggro 避免麻烦，get aggro 变得咄咄逼人，draw aggro 吸引敌方攻击注意，an aggro deck 强攻型卡组。',
 'avoid the aggro；get aggro；draw aggro；an aggro deck。',
 'aggro 的游戏仇恨值不是现实里某人一定恨你；口语麻烦也不必发展成暴力。先看人物冲突、办事折腾还是游戏机制。',
 ('We took the train to avoid the aggro of parking.','我们坐了火车，省去停车的麻烦。'),('In the game, the defender drew aggro away from the other players.','游戏里，防御角色把敌方攻击注意从其他玩家身上引开了。'),sources=['https://en.wiktionary.org/wiki/aggro#English','https://www.merriam-webster.com/dictionary/aggro'])
W('distro','英 /ˈdɪstrəʊ/；美 /ˈdɪstroʊ/','软件发行版〔尤指 Linux〕；分发或分销组织〔依语境〕',
 '同样围绕 Linux，一个发行版把系统组件、工具、安装方式等打包整理成可交给用户的一套，技术口语叫 distro。',
 'distribution 截短配 -o；另有 distributor 分销者截短的同形词。不是英语正式词根 dis + tro，后半也不表示三。',
 [['distribution 发行、分发','整理成可交付的一套；也指分发行为'],['截短配 -o → distro','技术口语发行版；另由 distributor 截短可指分销者']],
 'a Linux distro 一个 Linux 发行版，try a different distro 换一个发行版，a lightweight distro 轻量发行版。',
 'a Linux distro；a lightweight distro；try a different distro。',
 'distro 不等于 Linux 内核本身，通常是一套发行组合。技术版号、软件包与独立发行版也不是同一个层级的词。',
 ('This Linux distro includes a simple installation tool.','这个 Linux 发行版附带一个简便的安装工具。'),('The article compares three lightweight distros.','文章比较了三个轻量发行版。'))
W('wacko','英 /ˈwækəʊ/；美 /ˈwækoʊ/','古怪的、荒唐的；怪人〔带揶揄或贬义〕',
 '像在说这个点子怪得离谱，或给人贴一个怪人的标签。语气可能玩笑，也可能明显不尊重。',
 'wacky 古怪、滑稽的，截取 wack- 配 -o。词尾可造人物称呼，整个词也可作形容词，并非每个 -o 都只能是名词。',O[:1]+[['wacky 的 wack- + -o → wacko','古怪、荒唐的；带这种评价的人']],
 'a wacko idea 荒唐点子，a wacko character 古怪角色，describe someone as a wacko 把某人称作怪人。',
 'a wacko idea；a wacko character；a wacko。',
 'wacko 不是精神健康诊断，形容一个方案离谱与给人贬低标签也有语气差别；正式讨论可直接说具体哪里不合理。',
 ('The comedy is full of wacko ideas.','这部喜剧里尽是稀奇古怪的点子。'),('The review describes the character as a lovable wacko.','评论把这个角色形容为一个可爱的怪人。'))
W('cheerio','英 /ˈtʃɪəriəʊ/；美 /ˈtʃɪrioʊ/，也有末尾重读的形式','再见〔主要英式口语，略带旧式或轻快语气〕',
 '挥挥手、轻快地道别，像说好啦，回头见。熟悉它是为了听懂语气，不是每次正式告别都要换成长一点的 goodbye。',
 'cheer 或 cheery 愉快的 + -o，形成感叹式表达。多用于告别，也可能在旧式、特定场景作问候或祝酒。',O[:1]+[['cheer / cheery + -o → cheerio','轻快的口头表达，通常用于告别']],
 'say cheerio 说再见，a cheerful cheerio 轻快的一声再见。早餐麦圈品牌 Cheerios 是专名，不把商标复数直接当再见。',
 'say cheerio；Cheerio, see you tomorrow!。',
 'cheerio 是告别表达，cheers 还常用于感谢、祝酒等，不能在所有句子里直接互换。cheerio 的香肠等地域同形义不用于一般告别。',
 ('“Cheerio, see you tomorrow!” he called.','“再见，明天见！”他喊道。'),('She waved and said cheerio before getting on the bus.','她挥手说了声再见，然后上了公交车。'),sources=['https://en.wiktionary.org/wiki/cheerio#English','https://www.merriam-webster.com/dictionary/cheerio'])
W('cheapo','英 /ˈtʃiːpəʊ/；美 /ˈtʃiːpoʊ/','便宜货、廉价的；小气鬼〔名词，口语〕',
 '说物品时可指便宜、简陋的那款，说人时可能嫌对方太抠。共同用 cheap 的低价或吝啬分支，但评价对象不同。',
 'cheap + -o，口语词尾；作形容词、物品名词或人物贬称。价格低的基础义不必自动包含质量坏透了。',O[:1]+[['cheap + -o → cheapo','口语低价、廉价品；另一评价是小气的人']],
 'a cheapo camera 廉价相机，a cheapo version 便宜版本，call someone a cheapo 说某人小气。',
 'a cheapo camera；a cheapo version；a cheapo。',
 'cheapo 比 inexpensive 随意，有时嫌简陋，有时只是自嘲预算低。称人 cheapo 带贬义，不是节俭者的中性职业名。',
 ('I used a cheapo camera for the experiment.','我用一台便宜相机做了这个实验。'),('The shop sells a cheapo version without the extra accessories.','店里卖一个不带额外配件的便宜版本。'),sources=['https://en.wiktionary.org/wiki/cheapo#English','https://www.merriam-webster.com/dictionary/cheapo'])
W('neato','英 /ˈniːtəʊ/；美 /ˈniːtoʊ/','真棒、挺酷〔玩笑式、略旧的口语〕',
 '看到一个小巧有趣的东西，随口感叹挺棒啊。用的是 neat 很棒的口语义，不是在检查桌面有没有擦干净。',
 'neat 的口语很棒义 + -o，形成感叹表达。美式连读的 /t/ 可听成较轻的闪音，但拼写仍是 t。',O[:1]+[['neat + -o → neato','表示赞赏的玩笑式感叹']],
 'a neato little gadget 挺酷的小玩意，Neato! 真棒！常带随意、俏皮或略旧的语感。',
 'Neato!；a neato little gadget。',
 'neato 不是整洁程度的正式等级，也不适合拿来替换所有正式评价。neat 的纯饮酒等其他义不能一股脑套入此词。',
 ('“Neato!” she said when the model lit up.','模型亮起来时，她说：“真棒！”'),('He showed us a neato little folding lamp.','他给我们看了一盏挺酷的小折叠灯。'))
W('preggo','英 /ˈpreɡəʊ/；美 /ˈpreɡoʊ/','怀孕的〔非常随意的口语〕',
 '朋友聊天或社交媒体可能用来轻松地说怀孕了。词义不难，关键是语体：它比 pregnant 随意得多。',
 'pregnant 截取 preg- 配 -o，双写 g。不是把 pregnant 完整词尾换成一个表示怀孕的新词根。',O[:1]+[['pregnant 截短 + -o → preggo','非常随意的怀孕表达']],
 'say someone is preggo 用很随意的方式说某人怀孕；正式说明通常用 pregnant。',
 'I’m preggo〔极随意〕；pregnant〔普通、正式均常见〕。',
 'preggo 不说明孕期、健康状况或个人态度；意大利语 prego 的拼写、来源和用法又不同，不是英语怀孕一词的来源。',
 ('The character texts her friend, “I’m preggo!”','角色给朋友发消息：“我怀孕啦！”'),('The editor replaced preggo with pregnant in the formal announcement.','编辑把正式公告里的随意表达 preggo 改成了 pregnant。'))
R('A1786','口语昵称、人物称呼与截短模式','-O：把语气拉到随意一边，褒贬还要看基础词','kiddo、doggo 亲昵；cheapo、wacko 可贬；convo、distro 配合截短；servo 的技术义另看。',
 '这里没有一个统一的圆形、零、小东西义。-o 能让表达随意，感情色彩由词基和场景决定；长词截短也未必每次都真的新加一个 -o。',
 '完整词或截短词干 + 口语 -o；有时双写末尾辅音，有时保留截短后已有结尾。具体词逐个分辨。',
 [['亲昵与口语人物称呼','kiddo · doggo · rando · weirdo · dumbo · sicko · wacko · wino · pinko · psycho'],['截短、事物与风格','combo · convo · journo · distro · servo · aggro · cheapo · preggo'],['感叹和道别','cheerio · neato']],
 '-o 不总表可爱；servo 技术义是长词截短；lingo 远源和借入路线不完全确定；campo 常见草原义属于借词，不由英语这个词尾制造。',
 'The kiddo posted a photo of a doggo, then said cheerio.\n\n那个孩子发了一张狗狗照片，然后说了声再见。','kiddo doggo rando weirdo dumbo sicko wacko wino pinko psycho combo convo journo distro servo aggro cheapo preggo cheerio neato')
ROOTS[-1]['exclude']['lingo']='远接 lingua，直接形成路线有不同解释，不作为确定的英语口语 -o 派生。'
ROOTS[-1]['exclude']['campo']='常用草原、原野义借自西班牙语、葡萄牙语，不是英语词基加口语 -o；校园缩称另看。'
if __name__=='__main__':save('continuation_20261030_io',ROOTS,WORDS)
