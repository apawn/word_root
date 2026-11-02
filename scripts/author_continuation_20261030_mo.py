"""Ling formations, cheeks, surgical and bolts."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
Li=[['古英语及其他日耳曼语言 -ling 形式','某类成员、与前项相关的人或物；也形成幼小个体名'],['现代 -ling 的不同分支','亲属称呼、幼兽幼树、地位评价等，不全表示小']]
Si=[['古英语 sibb 亲属关系 + -ling → sibling','原泛指亲属'],['二十世纪重新采用旧词','现代常用义收窄为兄弟姐妹，不指定性别和长幼']]
W('sibling','/ˈsɪblɪŋ/','兄弟姐妹中的一个；同胞',
 '不想逐个说 brother or sister，就用 sibling。它只说明兄弟姐妹关系，不告诉你男、女、哥哥还是妹妹。',
 '由古英语亲属词 sibb 与 -ling 构成旧词，原可泛说亲属；现代重新采用后，常用义专指兄弟姐妹。',Si,
 'an older sibling 年长的兄弟姐妹，younger siblings 年幼的兄弟姐妹，sibling rivalry 手足间竞争；问几个 siblings 通常不把本人算进去。',
 'an older sibling；sibling rivalry。',
 'sibling 不是 cousin 堂、表亲；-ling 也不让这个词只指小孩，成年兄弟姐妹仍是 siblings。',
 ('She has two younger siblings.','她有两个比她小的兄弟姐妹。'),('The siblings kept in touch after moving to different cities.','搬到不同城市后，兄弟姐妹仍保持联系。'),sources=['https://en.wiktionary.org/wiki/sibling#English','https://www.etymonline.com/word/sibling'])
F=[['fledge 长出飞羽、准备飞翔 + -ling','羽翼渐丰的幼鸟'],['新鸟 → 刚起步的人、组织','经验少、正在形成的比喻']]
W('fledgling','/ˈfledʒlɪŋ/','羽翼渐丰的幼鸟；新手；初创、刚起步的',
 '羽毛刚长好、开始学着离巢的鸟是 fledgling；新公司、新作家也像刚学飞，仍在起步阶段。',
 'fledge 去末尾 e 加 -ling；g 属于 fledge 词干，真正后缀是 -ling。由幼鸟扩展为经验不足、初步发展的性质和人物。',F,
 'a fledgling bird 羽翼渐丰的幼鸟，a fledgling business 初创企业，a fledgling writer 新手作家。',
 'a fledgling business；a fledgling writer。',
 'fledgling 强调刚起步，不自动表示终将失败；形容企业时也不是真的会飞。',
 ('A fledgling perched on a low branch.','一只羽翼渐丰的幼鸟栖在低枝上。'),('The grant helped a fledgling theatre company.','这笔资助帮助了一家刚起步的剧团。'))
Go=[['古诺斯 gás 鹅 + -lingr → gæsling 等','小鹅名称'],['借入英语，受 goose 词形影响','中古英语 gesling、goslyng → gosling']]
W('gosling','英 /ˈɡɒzlɪŋ/；美 /ˈɡɑːzlɪŋ/','小鹅、幼鹅',
 'goose 是鹅，旁边跟着那几只毛茸茸的幼鹅就是 goslings。词里少一个 o、s 读 /z/，都有历史变化，别按字母硬拼。',
 '旧北欧语言已有鹅 + 幼小后缀 -lingr 的形式，借入中古英语后受 goose 影响，发展成 gosling；不是现代规则规定所有 oo 都这样缩短。',Go,
 'a gosling 一只幼鹅，a brood of goslings 一窝幼鹅，follow the goose 跟随母鹅。',
 'a gosling；a brood of goslings。',
 'gosling 幼鹅与 duckling 小鸭区分；成年鹅的常见复数是 geese，幼鹅仍正常加 s。',
 ('The goslings followed the goose across the grass.','小鹅跟着母鹅穿过草地。'),('A yellow gosling paddled near the bank.','一只黄色幼鹅在岸边划水。'))
Du=[['早期英语方言 dumpling','煮熟的面团块、面皮包馅食物，来源未定'],['可能联系团块 dump 与 -ling','也有低地德语等分析，先不把前项定死']]
W('dumpling','/ˈdʌmplɪŋ/','饺子；团子、面团块等食物',
 '英语 dumpling 的范围比中国水饺大：可以面皮包馅，也可以不包馅的面团块，放汤、炖菜里煮。先抓一小团面食。',
 '早期见于英语方言，确切来源未定；常联系团块义 dump 与 -ling 指小形式，也有其他语言分析。不能把倒垃圾的 dump 当作确定词源。',Du,
 'steamed dumplings 蒸饺、蒸面食，boiled dumplings 水煮饺子、团子，dumplings in a stew 炖菜里的面团块。',
 'steamed dumplings；boiled dumplings。',
 'dumpling 不保证一定有馅，也不保证一定是中国食物；具体做法看菜名、地区。',
 ('She served steamed dumplings with a dipping sauce.','她端上蒸饺和蘸酱。'),('Soft dumplings cooked in the stew.','松软的面团块在炖菜里煮着。'),sources=['https://en.wiktionary.org/wiki/dumpling#English','https://www.etymonline.com/word/dumpling'])
Sa=[['sap 树液、鲜活木质部一族','与有生命、幼嫩树木相关'],['中古英语 saplyng → sapling','sap + -ling，年轻小树']]
W('sapling','/ˈsæplɪŋ/','树苗、幼树',
 '已经是一棵能看出树干的小树，但还没长成大树，就是 sapling。想象幼嫩、仍在往上长的树，而非刚冒头一点芽。',
 '承中古英语 saplyng 等，现代对应 sap 树液、鲜活木质部 + -ling 幼小个体后缀。',Sa,
 'plant a sapling 栽幼树，young saplings 年轻树苗，a row of saplings 一排幼树。',
 'plant a sapling；a row of saplings。',
 'seedling 更突出由种子萌发的幼苗，sapling 通常已是稍长大的幼树；具体尺寸不由单词硬性统一规定。',
 ('They planted a row of saplings beside the road.','他们在路旁种了一排树苗。'),('The sapling bent in the wind but did not break.','幼树被风吹弯了，却没有折断。'))
Fo=[['中古英语 fyndling、foundlyng 等','被发现的、遭遗弃的孩子'],['现代 found + -ling 对应','found 取 find 发现的过去、分词形式']]
W('foundling','/ˈfaʊndlɪŋ/','弃婴、被遗弃后发现的孩子',
 '人们发现一个被遗弃、需要照料的孩子，旧故事里常称 foundling。名字从被找到这一面说，不代表其父母一定已经去世。',
 '承中古英语相应形式，现代可对应 found 找到的 + -ling 人物后缀；found 在这里联系 find，不是建立机构的动词 found。',Fo,
 'a foundling 弃婴，a foundling home 弃婴收容机构，a foundling child 被发现的弃童；历史、文学语境较常见。',
 'a foundling；a foundling home。',
 'foundling 与 orphan 孤儿有重叠可能，却不是同义定义：前者强调被遗弃、被发现，后者强调父母去世等亲属状态。',
 ('The novel’s hero grows up as a foundling.','小说主人公作为弃童长大。'),('The old building once housed a home for foundlings.','这栋老建筑曾是一家弃婴收容机构。'))
U=[['古英语 underling → 中古英语 underling','处于别人之下的人'],['under + -ling 的现代对应','下级、手下，常有轻视态度']]
W('underling','英 /ˈʌndəlɪŋ/；美 /ˈʌndərlɪŋ/','〔常含贬意〕下属、手下、小人物',
 '说某人只是大人物底下跑腿的一个，underling 就把这种低一等的眼光带出来。它不是最中性的同事介绍。',
 '承古英语 underling，现代对应 under 下方 + -ling 人物后缀；由地位在下形成较低权力者称呼。',U,
 'treat someone as an underling 把人当低等手下，leave it to an underling 把事情丢给小手下。',
 'treat as an underling；an underling of。',
 'employee、colleague、subordinate 的语气不同；underling 通常多一层轻视，不宜当所有下属的中性替换。',
 ('The manager treated everyone else as underlings.','经理把其他人都当作低自己一等的手下。'),('He left the unpleasant task to an underling.','他把那件讨厌的活丢给了一个小手下。'))
Ha=[['hatch 孵化、出壳','幼体从卵中出来'],['hatch + -ling → hatchling','刚孵出的幼小动物']]
W('hatchling','/ˈhætʃlɪŋ/','刚孵出的幼鸟、幼龟等动物',
 '蛋壳刚打开，小生命爬出来，这个阶段就可以 hatchling；不只鸟，龟、鳄等卵生动物也能这样称。',
 'hatch 孵化 + -ling 幼小个体后缀，按刚出壳的生命阶段命名。',Ha,
 'turtle hatchlings 刚孵出的幼龟，bird hatchlings 初生幼鸟，new hatchlings 新孵出的幼体。',
 'turtle hatchlings；new hatchlings。',
 'hatchling 看刚出壳，fledgling 看羽翼长成、准备或开始飞翔；后者不适用于龟。',
 ('The turtle hatchlings crawled towards the sea.','刚孵出的小海龟爬向大海。'),('The hatchlings stayed close to the broken eggshells.','初生幼体待在破蛋壳附近。'))
R('A1905','幼小个体、某类成员与带评价的人物后缀','-LING：一类中的小个体，也能按关系、地位叫人','duckling、gosling、sapling；sibling、underling；同形 -ing 要另拆。',
 '动物、植物的幼小分支很直观，亲属、地位分支却未必说小。先认前项，再判断它是在命名年龄、关系还是态度。',
 '日耳曼旧 -ling 形式；goose 的 gosling 有借入与音形变化；fledgling 去 fledge 末 e；dumpling 前项来源未定。',
 [['亲属与地位评价','sibling · underling · weakling · earthling'],['动物生命阶段、年龄','hatchling · nestling · fledgling · duckling · gosling · suckling · yearling'],['幼植物','seedling · sapling'],['历史人物、变化与食物名称','foundling · changeling · dumpling']],
 'sibling 不只小孩；buckling 常用屈曲义是 buckle + -ing，cowling 罩壳是 cowl + -ing；nestling 也有 nestle + -ing 的同形分词。',
 'The hatchling grew into a nestling and later a fledgling.\n\n那只刚孵出的鸟长成巢中幼鸟，后来羽翼渐丰。','sibling underling weakling earthling hatchling nestling fledgling duckling gosling suckling yearling seedling sapling foundling changeling dumpling')
ROOTS[-1]['exclude']['buckling']='常用屈曲义为 buckle + -ing，不是幼小后缀 -ling。'
ROOTS[-1]['exclude']['cowling']='常用罩壳义为 cowl + -ing；罕见小牛同形义本轮暂缓。'
C=[['古英语 ċēce、ċēace 等 → cheek','面颊、颌部'],['面颊、脸面 → 厚脸皮的态度','cheek 无礼，cheeky 冒失、调皮放肆']]
W('cheek','/tʃiːk/','面颊；〔尤英式〕无礼、厚脸皮',
 '脸两侧柔软的面颊是 cheeks；说话一点不客气、居然敢这样，也能说 have the cheek to ...，像厚着脸皮。',
 '承古英语面颊、颌部词，经中古英语 cheke 等到 cheek；脸面的形象扩展出大胆无礼的态度。',C,
 'rosy cheeks 红润脸颊，kiss someone on the cheek 亲吻某人脸颊，have the cheek to do 居然有脸做，What a cheek! 真不客气。',
 'on the cheek；have the cheek to。',
 'cheek 的无礼义多带说话者不满，身体义则中性；两个语境不要混译。',
 ('Tears ran down her cheeks.','眼泪顺着她的脸颊流下来。'),('He had the cheek to ask me to finish his work.','他居然有脸让我替他把活做完。'))
W('cheeky','/ˈtʃiːki/','冒失、放肆的；调皮、俏皮的',
 '孩子笑嘻嘻顶一句嘴，可能 cheeky；大人讲话没分寸，也能 cheeky。轻重取决于关系、语气，有时觉得可爱，有时真被冒犯。',
 'cheek 无礼、大胆 + -y，形容带这种态度；不是单纯脸颊多的外形描述。',C+[['cheek + -y → cheeky','冒失大胆；可带调皮、可爱意味']],
 'a cheeky grin 调皮笑容，a cheeky reply 放肆、俏皮回答，Don’t be cheeky. 别没大没小。',
 'a cheeky grin；a cheeky reply。',
 'cheeky 不固定等于严重厚颜无耻；但也不是在所有场合都算可爱的玩笑。',
 ('The child gave her a cheeky grin.','孩子冲她调皮地一笑。'),('That was a cheeky reply to a serious question.','面对严肃问题，那回答未免太没分寸。'))
R('B3982','面颊、脸面引出无礼，轻重随语境','CHEEK：身体的脸颊，态度里也能借脸面说大胆','cheek → cheekbone、cheeky。',
 '骨头名是实体复合，cheeky 则走无礼、调皮的态度分支。别把身体含义或态度评价套到全部用法。',
 '旧英语面颊词 → cheek；bone 骨；-y 具有相应性质。',
 [['面颊与颧骨','cheek · cheekbone'],['态度性质','cheeky']],
 'cheeky 的玩笑或冒犯轻重取决于场合；cheekbone 是骨头名。',
 'Her cheeks lifted in a cheeky grin.\n\n她调皮一笑，脸颊也扬了起来。','cheek cheekbone cheeky')
S=[['希腊 kheir 手 + ergon 工作 → kheirourgia','用手实施的医疗工作'],['拉丁、法语相应形式 → surgery、surgeon 词族','长期音形缩短，形成现代 surg-'],['surgical、surgically','外科、手术相关性质与方式']]
W('surgical','英 /ˈsɜːdʒɪkəl/；美 /ˈsɜːrdʒɪkəl/','外科、手术的；精确细致的',
 '谈手术工具、外科团队，用 surgical；把一个复杂问题像手术一样精细处理，也能借它形容精准。',
 '与 surgery、surgeon 同族，现代可认 surg- + -ical；更早经法语、拉丁 chirurgical 一族，上接希腊手 + 工作。',S,
 'surgical instruments 手术器械，a surgical team 外科团队，surgical precision 手术般精确。',
 'surgical instruments；surgical precision。',
 'medical 医疗的范围更广，surgical 更具体关联外科、手术；精确义是比喻，不自动证明任何现实行动没有误差。',
 ('The surgical team prepared the operating room.','外科团队准备好了手术室。'),('She edited the text with surgical precision.','她像做精细手术一样准确地修改文字。'),sources=['https://en.wiktionary.org/wiki/surgical#English','https://www.etymonline.com/word/surgical'])
W('surgically','英 /ˈsɜːdʒɪkli/；美 /ˈsɜːrdʒɪkli/','以手术方式；精确细致地',
 '事情是通过手术完成，就 surgically；比喻性地把多余内容准确去掉，也能用这个副词表现操作精细。',
 'surgical + -ly，-ical + -ly 写成 -ically，常用读音中末部为 /ɪkli/。',S+[['surgical + -ly → surgically','以手术或手术般精确的方式']],
 'surgically treated 以手术处理的，surgically remove 通过手术去除；比喻语境也可说精确删除、调整。',
 'surgically treated；surgically remove。',
 'surgically 说明方式，surgical 说明性质；它不是某一种具体手术的名称。',
 ('The injury was treated surgically.','那处损伤采用了手术治疗。'),('The editor surgically removed the repeated passages.','编辑精准地删掉了重复段落。'))
W('neurosurgical','英 /ˌnjʊərəʊˈsɜːdʒɪkəl/；美 /ˌnʊroʊˈsɜːrdʒɪkəl/','神经外科的',
 '把外科范围进一步放到神经系统，就是 neurosurgical；不是只把神经一词当紧张情绪，而是在说医学专业。',
 'neuro- 神经 + surgical 外科的，与 neurosurgery 神经外科对应；后部保留手 + 工作的旧词源。',S+[['neuro- + surgical → neurosurgical','神经系统相关的外科专业性质']],
 'a neurosurgical team 神经外科团队，a neurosurgical ward 神经外科病区，neurosurgical training 神经外科培训。',
 'a neurosurgical team；neurosurgical training。',
 'neurosurgical 是专业形容词，neurosurgeon 是相应医生；neuro- 本身不表示心情焦虑。',
 ('She joined the hospital’s neurosurgical team.','她加入了医院的神经外科团队。'),('The course forms part of his neurosurgical training.','这门课是他神经外科培训的一部分。'))
R('B4479','手的工作形成外科词族，再限定方式与神经专业','SURGICAL：现代外科词里藏着手 + 工作的旧组合','surgery、surgeon → surgical、surgically；neurosurgical 再加神经专业。',
 '古词形经过多次缩短，今天不再完整保留手、工作的字母。用词族认形，再按 -ical、-ly、neuro- 区分专业、性质和方式。',
 'kheir + ergon → kheirourgia → 拉丁、法语缩短形式 → surg- 词族；-ical 性质，-ly 方式，neuro- 神经。',
 [['外科领域、人物与性质','surgery · surgeon · surgical'],['方式与专业限定','surgically · neurosurgical']],
 'medical 范围更广；neuro- 神经专业不等于普通紧张情绪。',
 'The neurosurgical team discussed the surgical plan with the surgeon.\n\n神经外科团队与外科医生讨论了手术方案。','surgery surgeon surgical surgically neurosurgical')
Bo=[['古英语 bolt','粗短箭、弩箭；更远来源未定'],['粗短杆的形状 → 螺栓、门闩','形状、固定用途扩展'],['箭疾射 → 突然冲出、雷电','快速动作也用于狼吞虎咽等']]
W('bolt','英 /bəʊlt/；美 /boʊlt/','螺栓、门闩；一束闪电；闩住；突然冲出、匆匆吞下',
 '把词的两幅画面分开：一根粗短杆可以固定门、零件；一支箭突然射出去，则像人猛地冲走、闪电划过。',
 '承古英语粗短箭名 bolt；短杆形状扩展到螺栓、锁闩，箭的疾射又帮助形成突然冲出、雷电等义。另有筛面粉的同形词，来源不同。',Bo,
 'nuts and bolts 螺母和螺栓，bolt the door 闩门，a bolt of lightning 一道闪电，bolt for the exit 冲向出口，bolt down food 狼吞虎咽。',
 'bolt the door；a bolt of lightning；bolt for。',
 'bolt 固定物和猛冲不是互相矛盾，而是形状、运动两条延伸；bolt down food 也不是给食物拧螺栓。',
 ('She bolted the door before going upstairs.','她上楼前闩好了门。'),('The horse bolted when the gate opened.','门一开，马就猛地冲了出去。'),('A bolt of lightning lit up the sky.','一道闪电照亮天空。'),sources=['https://en.wiktionary.org/wiki/bolt#English','https://www.etymonline.com/word/bolt'])
R('B3253','粗短箭的杆状形状与疾射动作，各走一支','BOLT：像杆就能固定，像箭就能突然飞出去','bolt → deadbolt；thunderbolt 雷电相关复合。',
 '形状解释门闩、螺栓；速度解释突然逃跑、雷电；把这两支并列看，日常多义就好记。',
 '古英语 bolt 粗短箭；短杆用途、疾射运动分别扩展；dead、thunder 限定复合词。',
 [['固定杆、门闩及动作','bolt · deadbolt'],['雷电的形象','thunderbolt']],
 '普通锁闩词与冷门筛粉同形词另源；bolt down food 是快速吞食。',
 'A thunderbolt startled the horse, and it bolted towards the gate.\n\n一声雷电惊到了马，它猛地冲向大门。','bolt deadbolt thunderbolt')
if __name__=='__main__':save('continuation_20261030_mo',ROOTS,WORDS)
