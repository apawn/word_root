"""Scuttling, hurtling, ruffling and rushing, with homonyms separated."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
def S(word,base):
 return ['https://en.wiktionary.org/wiki/'+word+'#English','https://www.etymonline.com/word/'+base]
EXISTING_ROOT_ADDITIONS={
 'A2238':dict(words='scuttle scuttles scuttled scuttling ruffle ruffles ruffled ruffling unruffled'.split(),label='scuttle、ruffle：同形词与去 e 接词尾',note='scuttle 的小步快跑、船体开孔沉没、煤斗分不同来源；ruffle 则是扰乱平整、秩序到惹不快。共同 -le 外形不能证明两词同族，也不能替代各自词史。'),
 'B2880':dict(words='hurt hurtle hurtles hurtled hurtling'.split(),label='hurtle：保留 hurt 旧碰撞义的猛冲',note='hurtle 大概是中古英语 hurten 碰撞材料的反复动作形式，现代高速运动不一定真的撞上；hurl 更侧重猛力投掷，不当成同一个词。'),
 'A1741':dict(words='rush rushes rushed rushing'.split(),label='rush：猛冲、赶快与高峰；植物名另源',note='动作一支通常经法语 russher、ruser 接更早拉丁材料；rush 灯心草名词承古英语，不能把植物生长画面当成匆忙的唯一来源。'),
 'A1783':dict(words='haste hasten hastens hastened hastening'.split(),label='hasten：在更早 haste 动词上扩展 -en',note='hasten 接 haste 与 -en，但英语更早就有 haste 动词，不说所有动词功能都是加 -en 后才产生。'),
 'A1697':dict(words='rattle rattler rattlers'.split(),label='rattler：发出连续响声的人物、动物称呼',note='rattler 由 rattle 加 -er，较早有人喋喋不休的用法；响尾蛇口语义是 rattlesnake 的缩称，不能按一个现代后缀故事替代两种近源。'),
}
SCUTTLE=[['小步快跑一支 scuttle','可能接 scud 相关或反复动作材料，确切远源未定'],['船体开孔一支：法语、可能的西班牙语舱口材料 → scuttle','给船体开孔使其沉没；再比喻使计划告吹'],['煤斗一支：拉丁 scutella 盘 → 古英语等器皿名','器皿、篮子到盛煤容器，不能从跑动或凿沉词义推出全部来源']]
HURTLE=[['中古英语 hurten 的旧撞击义 → hurtelen、hurtle','可能为反复动作形式，与 hurt 同族，更早词源仍有争议'],['碰撞、冲撞 → 高速猛冲、飞驰','现代说 hurtle past 可以只是迅猛经过，不要求已经撞上']]
RUFFLE=[['中古英语 ruffelen：扰乱平整、秩序','有北欧、低地德语相似词比较，关系、远源未定'],['弄乱头发、羽毛；后来惹恼、扰乱镇定','褶边名词由动词发展；unruffled 的镇定义记录早于部分字面平整义']]
RUSH=[['动作一支：法语 russher、ruser 等 → 英语 rush','更早通常接拉丁 recusare 等材料；从抵退、猛冲到赶快等用法'],['rush 动词 → 名词涌动、高峰、强烈感觉','突然集中的画面可用于客流、需求、兴奋等'],['另源 rush 植物名：古英语 rysc 等 → rush','灯心草等植物名，不接赶快动词的同一来源']]
HASTEN=[['法语 haste、haster 等 → 英语 haste 名词、动词','英语在 hasten 之前已有赶快的 haste 动词'],['haste 动词 + -en → hasten','扩展形式写赶紧行动，也可及物地使事件更早发生']]
RATTLER=[['rattle 连续碰撞声 → rattler','rattle 去 e 加 -er，较早可命名说得又快又多的人'],['rattlesnake → 口语 rattler','响尾蛇的缩称；这一路近源不必讲成重新从蛇尾造了一次词']]
W('scuttle','/ˈskʌtəl/','小步快跑；凿沉船只；使计划告吹；煤斗',
 '螃蟹一串小步快跑可以 scuttle；scuttle a plan 却是把计划弄沉、使其告吹。这两条动词来源不同，煤斗名词又是另一支。',
 '跑动义可能接 scud 的相关、反复动作材料；凿沉义从舱口、开孔材料转动词；煤斗名词经古英语器皿名接拉丁 scutella 盘。分别看，不拼成一个万能词根。',SCUTTLE,
 'scuttle across the floor 小步快跑过地板；scuttle a ship 凿沉船；scuttle the deal 使交易告吹。',
 'scuttle away 迅速跑开；a coal scuttle 煤斗。',
 'scuttle the deal 的画面是让事情沉掉，不是交易跑得快；scurry away 则可近义说迅速小步跑开。',
 ('We watched the crabs scuttle across the sand.','我们看着螃蟹在沙地上小步快跑。'),('The new disagreement could scuttle the deal.','新的分歧可能让这笔交易告吹。'),sources=S('scuttle','scuttle'))
W('scuttles','/ˈskʌtəlz/','小步快跑、凿沉、使告吹〔第三人称单数〕；煤斗等〔复数〕',
 '小动物一溜烟钻进角落，是 scuttles away；一个问题把计划弄泡汤，是 scuttles the plan。动作方向靠搭配分，不靠同形词尾猜。',
 'scuttle + -s，读 /z/；不同来源的动词三单，以及器皿名词复数，共有同一词形。',SCUTTLE+[['scuttle + -s → scuttles','它急跑、使告吹；多只煤斗等']],
 'scuttles under a rock 快跑到石头下；scuttles negotiations 使谈判告吹。',
 'scuttles away；scuttles the proposal。',
 'scuttles the plan 强调计划被破坏，delays the plan 只说明推迟；推迟后仍可能继续，告吹则更严重。',
 ('The crab scuttles under a rock when we approach.','我们靠近时，螃蟹便小步快跑到石头下面。'),('One unresolved issue scuttles the whole proposal.','一个未解决的问题让整个提案告吹。'),sources=S('scuttles','scuttle'))
W('scuttled','/ˈskʌtəld/','小步快跑了；凿沉了；使计划告吹了',
 '一串急促小步跑远是 scuttled away；谈判被一个分歧弄泡汤是 the disagreement scuttled the talks。同形过去式分别承两条历史。',
 'scuttle 去 e 加完整 -ed，读 /d/；凿沉、使告吹接舱口开孔一支，急跑一支另源。',SCUTTLE+[['scuttle → scuttled','各自动词的过去形式，不能混合来源']],
 'scuttled into a corner 急跑进角落；scuttled the plan 使计划告吹；scuttled the vessel 凿沉船只。',
 'the deal was scuttled；scuttled away。',
 'scuttled the vessel 通常是有意让船进水沉没，the ship sank 只说船沉了；不是所有沉船都由人主动凿沉。',
 ('The mouse scuttled behind the cupboard.','老鼠一串小步快跑到柜子后面。'),('The funding dispute scuttled the project.','资金争执让项目告吹。'),sources=S('scuttled','scuttle'))
W('scuttling','/ˈskʌtlɪŋ/','正在小步快跑；凿沉；使计划告吹',
 '地板边一阵急促小脚步，是 scuttling；说一次行动正在毁掉协议，则是另一支 scuttling the agreement。',
 'scuttle 去 e 加 -ing；跑动、凿沉等各自来源不同，共用现代变化形式，常见读音中间收成 /tl/。',SCUTTLE+[['scuttle → scuttling','急跑、凿沉或使告吹的动作过程']],
 'scuttling across the floor 在地板上小步快跑；scuttling the talks 使谈判告吹。',
 'scuttling away；the scuttling of a ship 凿沉船只的行为。',
 'scuttling 的小步快跑常带急促、贴地的画面，hurtling 则更强调带大冲力的高速移动；两种快的姿态不同。',
 ('We heard something scuttling behind the wall.','我们听见墙后有什么在小步急跑。'),('They were accused of scuttling the talks at the last moment.','他们被指责在最后一刻破坏了谈判。'),sources=S('scuttling','scuttle'))
W('hurtles','英 /ˈhɜːtəlz/；美 /ˈhɝtəlz/','猛冲、飞驰〔第三人称单数〕',
 '列车带着一股挡不住的速度呼啸经过，叫 hurtles past；不仅快，还让人感觉有冲力。',
 'hurtle + -s，读 /z/；hurtle 大概承中古英语 hurten 旧碰撞义的反复动作形式，与 hurt 同族。',HURTLE+[['hurtle + -s → hurtles','它带着强大冲力高速移动']],
 'hurtles past 飞驰而过；hurtles towards 朝……猛冲。',
 'hurtles through space 在太空中疾驰；hurtles down the hill 冲下山坡。',
 'hurtles past 不表示已经撞上，crashes into 才明确碰撞；旧碰撞词源不能替现代每句补上不存在的事故。',
 ('The express train hurtles past the small station.','特快列车从小站旁飞驰而过。'),('A huge rock hurtles down the hillside.','一块巨石沿山坡猛冲下来。'),sources=S('hurtles','hurtle'))
W('hurtled','英 /ˈhɜːtəld/；美 /ˈhɝtəld/','猛冲、飞驰了',
 '车、石块或人带着冲力高速越过去，过去发生了就用 hurtled。它常让动作显得急、猛、难停。',
 'hurtle 去 e 加完整 -ed，读 /d/；内层可能接 hurt 的旧碰撞材料，不是把现代 hurl 投掷机械加 t。',HURTLE+[['hurtle → hurtled','过去迅猛地冲、飞驰']],
 'hurtled past 飞驰经过；hurtled down the road 沿路猛冲；hurtled towards 朝……冲去。',
 'hurtled through the air；hurtled into view 猛地冲入视野。',
 'hurled 是猛力扔出了什么，hurtled 常是对象自己飞驰、猛冲；一个写投掷动作，一个常写高速运动，别看漏 t。',
 ('The car hurtled past before we could read the number plate.','我们还没看清车牌，车就飞驰而过。'),('A loose wheel hurtled across the road.','一只脱落的车轮猛地滚冲过马路。'),sources=S('hurtled','hurtle'))
W('hurtling','英 /ˈhɜːtlɪŋ/；美 /ˈhɝtlɪŋ/','正在猛冲、飞驰',
 '物体带着很大冲力正快速移动，是 hurtling；比平平的 moving 更能让你看见速度、势头。',
 'hurtle 去 e 加 -ing；动作形式，常见读音中间收成 /tl/。旧碰撞材料发展成现代迅猛运动，不保证最终一定撞击。',HURTLE+[['hurtle → hurtling','带冲力高速移动的过程']],
 'hurtling towards the ground 朝地面急冲；hurtling through space 在太空中飞驰。',
 'a hurtling train；sent the object hurtling away 使物体猛地飞走。',
 'hurtling 是猛冲，hurting 是疼痛、伤害；二者有词史联系，现代多一个 l 就变成不同的常用动作。',
 ('The asteroid was hurtling through space.','小行星正在太空中疾驰。'),('The collision sent his bag hurtling across the carriage.','碰撞使他的包猛地飞向车厢另一边。'),sources=S('hurtling','hurtle'))
W('ruffle','/ˈrʌfəl/','弄乱头发、羽毛等；使不快、扰乱镇定；褶边',
 '平顺的头发被手一揉，乱起来，是 ruffle；一句话把平静心情拨乱，也可以 ruffle someone。衣服上拢成波浪状的褶边，则是 a ruffle。',
 '中古英语已有扰乱平整、秩序的 ruffelen；远源未定，有北欧、低地德语相似材料。褶边名词由动词发展，不硬定成现代 rough 加某个尾巴。',RUFFLE,
 'ruffle someone’s hair 揉乱头发；ruffle feathers 弄乱羽毛，也比喻惹恼人；a ruffle at the collar 领口褶边。',
 'nothing can ruffle her 很难让她失去镇定；ruffle the surface of the water 吹皱水面。',
 'ruffle someone’s feathers 常是碰触自尊、让人不高兴，不要求真的有鸟羽；但揉乱头发可很亲昵，不能所有 ruffle 都译成冒犯。',
 ('He reached over to ruffle the child’s hair.','他伸手揉了揉孩子的头发。'),('She wore a blouse with a ruffle at the collar.','她穿了一件领口有褶边的衬衫。'),sources=S('ruffle','ruffle'))
W('ruffles','/ˈrʌfəlz/','弄乱、惹不快〔第三人称单数〕；褶边〔复数〕',
 '衣服上几道波浪褶边是 ruffles；风把头发吹乱，是 ruffles her hair。平整变起伏的画面把现代两种用法串得起来。',
 'ruffle + -s，读 /z/；名词复数和动词三单同形。基底远源未定，褶边名词由扰乱平整的动词发展。',RUFFLE+[['ruffle + -s → ruffles','它弄乱、惹恼；多道波浪褶边']],
 'ruffles along the sleeves 袖子上的褶边；ruffles his feathers 惹他不快。',
 'ruffles her hair；a dress covered in ruffles。',
 'ruffles 是褶边，wrinkles 是不平整的皱褶；前者常是特意装饰，后者可能是衣物被压皱，不一律当同一种缺陷。',
 ('The dress had soft ruffles along the sleeves.','裙子的袖子上有柔软的褶边。'),('The breeze ruffles her hair as she walks.','她走路时，微风把头发吹乱。'),sources=S('ruffles','ruffle'))
W('ruffled','/ˈrʌfəld/','凌乱、被拨乱的；不快、失去镇定的；有褶边的',
 '羽毛、头发被弄乱是 ruffled；人被一句话搅得不高兴，也像心绪不再平顺，是 ruffled。衣服还可因带褶边而叫 ruffled。',
 'ruffle 去 e 加完整 -ed，读 /d/；既可作过去分词，也可形容凌乱、受扰或带褶边的性质。',RUFFLE+[['ruffle → ruffled','平整或镇定被扰乱；也可写服饰带褶边']],
 'ruffled feathers 凌乱羽毛或受冒犯的情绪；a ruffled blouse 有褶边的衬衫。',
 'looked ruffled；slightly ruffled by the remark。',
 'ruffled blouse 可能是设计好的褶边，不是没熨平；creased blouse 才更直接说衬衫有压皱。',
 ('The bird shook out its ruffled feathers.','鸟抖开了凌乱的羽毛。'),('He looked slightly ruffled by the criticism.','那些批评让他显得有些不快。'),sources=S('ruffled','ruffle'))
W('ruffling','/ˈrʌflɪŋ/','正在弄乱；惹人不快；褶边装饰等',
 '风正把平静的水面吹出起伏，是 ruffling；改革碰到旧习惯，让人不爽，也可借 ruffling feathers 来说。',
 'ruffle 去 e 加 -ing；可作动作形式，服饰语境也可把加褶边、褶边装饰当作行为或材料来讲。',RUFFLE+[['ruffle → ruffling','扰乱平整、镇定的过程；装饰义按语境另看']],
 'ruffling the water 使水面起伏；ruffling feathers 惹恼、触动某些人。',
 'ruffling his hair；without ruffling feathers 不惹人不快。',
 'ruffling feathers 常是意见、做法触动情绪，smoothing things over 则是缓和不快；都是意象搭配，不能逐字只讲羽毛或表面。',
 ('A light breeze was ruffling the surface of the pond.','一阵微风正吹皱池塘水面。'),('The changes are ruffling a few feathers in the office.','这些变化让办公室里一些人不太高兴。'),sources=S('ruffling','ruffle'))
W('unruffled','/ʌnˈrʌfəld/','镇定、未受扰乱的；平整未乱的',
 '别人话里带刺，他仍平静回答，心里好像没有被拨乱，就是 unruffled。也能用于没被吹乱、搅动的头发、水面等。',
 '否定 un- + ruffled。值得分清，unruffled 的镇定比喻记录很早，早于它某些字面未乱用法的记录；不能把记忆画面强排成历史。',RUFFLE+[['un- + ruffled → unruffled','不受情绪扰动；也描述字面未被弄乱']],
 'remain unruffled 保持镇定；calm and unruffled 冷静从容。',
 'an unruffled reply；an unruffled surface。',
 'unruffled 可以是有压力但应对从容，unaware 是根本没察觉；镇定不等于不了解发生了什么。',
 ('She remained unruffled by the hostile questions.','面对带敌意的问题，她仍保持镇定。'),('He gave an unruffled reply and continued the demonstration.','他平静地回答，然后继续演示。'),sources=S('unruffled','ruffle'))
W('rush','/rʌʃ/','猛冲；赶快、催赶；高峰、涌动；一阵强烈感觉；灯心草等植物',
 '人或水一股脑儿冲来，叫 rush；忙碌高峰、突然上头的一阵兴奋，也像一股涌上来的力量。植物 rush 则是另源词。',
 '动作一支通常经法语 russher、ruser，接更早拉丁材料；从抵退、猛冲到现代赶快、催赶。植物名承古英语 rysc 等，不与动作一支硬合。',RUSH,
 'rush to the station 冲去车站；rush someone 催某人；the morning rush 早高峰；a rush of excitement 一阵兴奋。',
 'rush hour 高峰时间；no rush 不着急；rush into a decision 仓促作决定。',
 'rush 强调来得急、做得急，有时带没准备好；move quickly 只说明速度。a rush of relief 是一阵释然，也不需要有人真的跑动。',
 ('Don’t rush into a decision before reading the details.','看清细节前，别仓促作决定。'),('She felt a rush of excitement when her name was announced.','听到自己的名字被宣布时，她感到一阵兴奋。'),sources=S('rush','rush'))
W('rushes','/ˈrʌʃɪz/','猛冲、赶快、催赶〔第三人称单数〕；涌动、高峰、灯心草等〔复数〕',
 '他早上总急匆匆冲出门，是 he rushes out；河边成片的 rushes 却可能是灯心草。两个来源要靠场景辨认。',
 'rush + -es，/ʃ/ 后读 /ɪz/；动作三单和不同来源名词的复数同形。',RUSH+[['rush + -es → rushes','他急冲、催赶；多阵涌动或多株植物等']],
 'rushes out of the door 冲出门；rushes to help 急忙帮忙；rushes by the water 水边灯心草。',
 'rushes through the work 匆匆做完工作；rushes of excitement 阵阵兴奋。',
 'rushes through a report 常有赶着做、可能没细看的意味，carefully reviews a report 则明确认真审阅；完成得快不表示读得细。',
 ('He rushes out of the house without breakfast.','他没吃早餐就匆匆冲出家门。'),('Tall rushes grew along the edge of the pond.','池塘边长着高高的灯心草。'),sources=S('rushes','rush'))
W('rushed','/rʌʃt/','冲、赶快、催促了；仓促的',
 '把本该慢慢想的事赶着做完，常叫 rushed；人过去急冲进来，也用同形过去式。',
 'rush + 完整 -ed，/ʃ/ 后读 /t/；过去分词形容词常写事情做得仓促、时间不够。',RUSH+[['rush + -ed → rushed','过去猛冲、催赶；或做得匆忙']],
 'a rushed decision 仓促决定；feel rushed 感到被时间追着；rushed to hospital 被急送医院。',
 'rushed through the meal；rushed into the room。',
 'rushed decision 常含时间不足、欠考虑，rapid decision 可以只是决定得快；是否草率仍要看语境、评价。',
 ('It was a rushed decision that we later regretted.','那是个仓促决定，我们后来后悔了。'),('She rushed into the room with the news.','她带着消息急冲进房间。'),sources=S('rushed','rush'))
W('rushing','/ˈrʌʃɪŋ/','正在猛冲、赶忙、催赶；急流的',
 '人忙着赶时间，是 rushing；溪水飞快冲过去，是 rushing water。都能抓住快速、带势头的过程。',
 'rush + -ing；规则动作形式，也可形容快速流动的水等。现代英语最早相关 rushing 记录很早，不把教学顺序当全部年代。',RUSH+[['rush → rushing〔现代构词对照〕','猛冲、匆忙动作的过程；也形容急速水流']],
 'rushing to work 正赶去上班；rushing water 急流；stop rushing 别再这么赶。',
 'rushing through the task；rushing past。',
 'rushing water 写水流急，running water 范围更广，包括流动水、自来水；不能每个 running 都译成汹涌。',
 ('Everyone was rushing to catch the last bus.','大家都正赶着去乘末班公交。'),('We could hear rushing water below the bridge.','我们能听见桥下急流的声音。'),sources=S('rushing','rush'))
W('hastens','/ˈheɪsənz/','赶快；使更早发生、加速〔第三人称单数〕',
 '一个变化让结果更早到来，是 hastens the process；某人赶紧澄清一句，则是 hastens to explain。既能自己赶快，也能让事情加快。',
 'hasten + -s，读 /z/；hasten 承更早 haste 动词接 -en，t 不发音。',HASTEN+[['hasten + -s → hastens','他赶快；它加速某个过程']],
 'hastens the process 加快过程；hastens to add 赶紧补充一句。',
 'hastens the decline 加速衰退；hastens to explain。',
 'hastens the decline 可能是坏结果更早，hastens recovery 可以是好结果加快；动词只写加速，不自带好坏。',
 ('Warm weather hastens the ripening of the fruit.','温暖天气使果实更早成熟。'),('He hastens to add that no final decision has been made.','他赶紧补充说，最终决定还没作出。'),sources=S('hastens','hasten'))
W('hastened','/ˈheɪsənd/','赶快行动了；使加速、提前了',
 '听到消息就赶紧过去，是 hastened to help；一项改变让事情更早发生，是 hastened the process。',
 'hasten + 完整 -ed，读 /d/；t 在 hasten 基底中不发音，不因加词尾重新读出来。',HASTEN+[['hasten + -ed → hastened','过去赶快行动；或使某事更早发生']],
 'hastened to help 赶紧帮忙；hastened the departure 使离开更早发生。',
 'hastened home 赶回家；hastened the decline 加速衰退。',
 'hastened to apologize 常是赶紧道歉，was hurried into apologizing 更像被别人催逼去道歉；主动与受压不同。',
 ('She hastened to reassure the visitors.','她赶紧让来访者放心。'),('The storm hastened our departure.','暴风雨让我们提前动身了。'),sources=S('hastened','hasten'))
W('hastening','/ˈheɪsənɪŋ/','正在赶快行动；正在使加速、提前',
 '一边行动，一边让结果更快到来，就是 hastening；常在较书面的描述里说明什么因素使变化加快。',
 'hasten + -ing；直接接完整词尾，t 继续不发音。内层 -en 扩展更早 haste 动词。',HASTEN+[['hasten + -ing → hastening','赶快行动或加快过程正在发生']],
 'hastening home 正赶回家；hastening the end 正使结束来得更早。',
 'hastening the process；without hastening the decision 不仓促催快决定。',
 'hastening 表示加速过程，happening 表示发生；某件事在 happening，不一定有人在 hastening it。',
 ('The children were hastening home before dark.','孩子们正赶在天黑前回家。'),('The extra workers were hastening the completion of the repairs.','增派的工人正加快维修完工。'),sources=S('hastening','hasten'))
W('rattler','英 /ˈrætlə/；美 /ˈrætlər/','响尾蛇〔口语〕；喋喋不休者等',
 '北美故事里 a rattler 常是响尾蛇，尾巴会发连续响声；旧时也可指说话又快又多、像哗啦声不停的人。',
 '说话者等用法可按 rattle 去 e 加 -er；响尾蛇义则常是 rattlesnake 的口语缩称。两条近源都和 rattle 发响材料有关，但形成方式要分清。',RATTLER,
 'a rattler on the path 小路上的响尾蛇；hear a rattler 听到响尾蛇的尾响。',
 'a young rattler；the rattler’s tail。',
 'rattler 动物义通常口语，rattlesnake 是完整称呼；不要因为 -er 常命名人，就在荒野场景里只找一个爱说话的人。',
 ('A rattler lay beside the path.','一条响尾蛇伏在小路旁。'),('We heard the dry sound of a rattler’s tail.','我们听见响尾蛇尾巴发出的干涩响声。'),sources=S('rattler','rattler'))
W('rattlers','英 /ˈrætləz/；美 /ˈrætlərz/','响尾蛇〔复数，口语〕；喋喋不休者等〔复数〕',
 '在北美荒野叙述里，几条 rattlers 通常就是几条响尾蛇；词尾只把单个称呼变成复数，具体是哪类角色仍看场景。',
 'rattler + -s，读 /z/；响尾蛇义的单数常缩自 rattlesnake，旧人物称呼则由 rattle + -er。',RATTLER+[['rattler + -s → rattlers','多个响尾蛇等被命名对象']],
 'rattlers in the desert 沙漠中的响尾蛇；watch for rattlers 留意响尾蛇。',
 'two rattlers；the sound of rattlers。',
 'rattlers 动物义不是 rattles 摇铃的复数；人或动物名字中的 -er 不能在变复数时省掉。',
 ('The guide pointed out places where rattlers sometimes rested.','向导指出了响尾蛇有时停留的地方。'),('The book describes several kinds of rattlers found in the region.','书里描述了这个地区的几种响尾蛇。'),sources=S('rattlers','rattler'))
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_zgq',ROOTS,WORDS)
 extend_lessons()
