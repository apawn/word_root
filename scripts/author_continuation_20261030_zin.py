"""Common organizational, descriptive and landscape vocabulary."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
def S(word,base):return ['https://en.wiktionary.org/wiki/'+word+'#English','https://www.etymonline.com/word/'+base]
EXISTING_ROOT_ADDITIONS={
 'B4597':dict(words='marshal marshals marshaled marshalled marshaling marshalling'.split(),label='marshal：管马的职务 → 维持秩序者 → 调配组织',note='较远日耳曼语马 + 仆从组成职务名，经法语 mareschal 进入英语，职务地位与功能扩大；动词由职务名转来，表示排列、组织、调配。美式常见单 l，英式常见双 l 分词。'),
 'B2480':dict(words='martial'.split(),label='martial：战神名到军事、武艺',note='与 war 比较战争，不由 war 派生。martial 接拉丁 martialis，Mars、Mart- 战神名 + 关系形容词材料；与日耳曼管马职务名 marshal 来路不同。'),
 'B2886':dict(words='prone'.split(),label='prone：向前俯 → 易于、倾向于',note='与 lean 比较倾斜，不由英语 lean 派生。prone 借拉丁 pronus，兼有俯身与倾向义，可能接 pro 向前材料；英语倾向义的记录比俯卧义早，学习画面不等于英语先后顺序。'),
 'C0622':dict(words='gem gems'.split(),label='gem：另源的宝石、珍品',note='与 jewel 比较珍宝，不从拉丁 jocus 玩笑词根派生。gem 经法语 gemme、拉丁 gemma 宝石及芽的旧义，古英语也有直接借入形式；现代比喻珍贵、出色的人或物。'),
 'B4303':dict(words='midst'.split(),label='mid → middes → midst：中间、正当其中',note='mid 接旧副词性 -s 成 middes，后来出现 t，原因有最高级类比等解释。末尾 -st 不是现代最高级后缀；in the midst of 可用于空间和事件过程。'),
 'B2615':dict(words='cedar cedars'.split(),label='cedar：另源的雪松等树名',note='与 tree 比较树木，不由 tree 派生。古英语 ceder 与法语 cedre 等形式汇合，较远接拉丁 cedrus、希腊 kedros，远源不确定；俗名 cedar 也用于其他外形相近的树。'),
 'C0989':dict(words='pine pines'.split(),label='pine → pines：松树一支；思念消瘦另支',note='松树名接拉丁 pinus 经法语等；动词 pine 接古英语 pinian 折磨、使受苦，可能较远接拉丁 poena 惩罚，是不同来源。pines 可为树名复数，也可为思念动词单数。'),
 'B4463':dict(words='heather'.split(),label='heather：石南植物名，词形受 heath 影响',note='heather 接北部、苏格兰等植物名称，较远可能有凯尔特语来路；heath 荒原可能影响拼写，但不宜当成已证实的 heath + -er 派生。'),
 'A1776':dict(words='glen glens'.split(),label='glen → glens：盖尔语借来的山谷名',note='和 valley 比较地貌并展示复数，不由 valley 派生。glen 经苏格兰语接盖尔 gleann 山谷，复数在现代英语末尾加 s。'),
 'B2628':dict(words='cod'.split(),label='cod：另源的鳕鱼名',note='和 fish 比较鱼类，不是 fish 派生。cod 作为鱼名更远来源不明，与古英语 codd 袋子的关系没有确证；常见鱼名复数仍可用 cod。'),
 'C0436':dict(words='influenza flu'.split(),label='influence → influenza → flu：旧影响观念到疾病名、缩略名',note='influenza 借意大利语，上接中古拉丁 influentia 影响，历史与星体、气候影响的旧观念有关；flu 再截取词中间音节。历史命名观念不是现代病因说明。'),
}
MARSHAL=[['日耳曼语马 + 仆从 → 法语 mareschal 管马职务、家内及军中官职','职务的地位、职责随历史扩大'],['英语 marshal：维持秩序者、某些官衔；动词排列、组织','把人员、资源或论据有条理地集合到位']]
GEM=[['拉丁 gemma：芽，也用于宝石 → 法语 gemme、英语 gem','古英语 gimm 也曾直接借拉丁词，后续词形有汇合讨论'],['宝石的珍贵 → 出色的人、值得珍惜的东西','更远与牙、挤压等材料的联系有争论，不强作定论']]
CEDAR=[['希腊 kedros 雪松、杜松类旧名 → 拉丁 cedrus','更远来源不明'],['古英语 ceder 与法语 cedre 等 → 英语 cedar','树木名称也借给木材，俗名范围未必等于严格属名']]
GLEN=[['盖尔语 gleann 山谷 → 苏格兰语 → 英语 glen','常见于苏格兰风景与地名'],['glen：通常狭长的山谷 → glens','英语复数加 -s，名称不等于所有地貌词都同源']]
INFLUENZA=[['中古拉丁 influentia 影响 → 意大利 influenza','旧观念用星体、气候等影响解释某些疾病'],['意大利疾病名 influenza → 英语 influenza → 中间音节缩为 flu','现代疾病名；旧命名思想不充当现代病因']]
W('marshal','英 /ˈmɑːʃəl/；美 /ˈmɑrʃəl/','组织、调配、整理；维持秩序的工作人员；元帅等官衔',
 '把分散的人、资源、论据集合起来，排好、用上，就是 marshal。这个组织动作来自一种负责管理、维持秩序的职务名。',
 '日耳曼语马 + 仆从组成旧职务名，经法语 mareschal 进入英语；从管马、家内管理到更高官职。英语名词再转作排列、组织的动词。',MARSHAL,
 'marshal resources 是调集资源；marshal evidence 是整理证据；an event marshal 是活动现场维持秩序的工作人员；field marshal 是一种元帅官衔。',
 'marshal resources；marshal evidence；an event marshal。',
 'marshal 与 martial 常见读音很接近或相同，但 martial 是接战神名的军事形容词；marshal 是管马职务线及其组织动词。',
 ('We need to marshal our resources before the next stage.','进入下一阶段前，我们得把资源组织调配好。'),('A marshal directed runners towards the starting line.','一名现场工作人员引导跑者走向起跑线。'),sources=S('marshal','marshal'))
W('marshals','英 /ˈmɑːʃəlz/；美 /ˈmɑrʃəlz/','组织、调配〔第三人称单数〕；现场管理人员、元帅等〔复数〕',
 '她把论据一条条排好，是 she marshals the evidence；赛道旁几名工作人员，则是 marshals。行动与职务共享一个名字。',
 'marshal + -s → marshals，末尾 /l/ 后接 /z/；动词第三人称单数和职务名复数同形。',MARSHAL+[['marshal + -s → marshals','组织动作的单数形式；或多名现场管理人员等']],
 'race marshals 是赛事工作人员；marshals the team 是组织团队；marshals the evidence 是把证据组织起来。',
 'race marshals；marshals the evidence；marshals the team。',
 'marshals 只说明某些职务名称的复数，具体职责依场合而不同；赛事工作人员和历史元帅不能只靠中文一词包办。',
 ('Race marshals stood at each junction.','每个路口都站着赛事工作人员。'),('She marshals the evidence into a clear argument.','她把证据组织成清晰的论证。'),sources=S('marshals','marshal'))
W('marshaled','英 /ˈmɑːʃəld/；美 /ˈmɑrʃəld/','组织、调配、整理了〔过去式、过去分词；常见美式拼写〕',
 '原来散着的队伍或论据，已经被组织到位，就是 marshaled。美式常见单个 l 的过去形式。',
 'marshal + -ed → marshaled，后缀读 /d/；美式通常保留单 l，英式常见 marshalled，含义没有因此分成两套。',MARSHAL+[['marshal + -ed → marshaled','规则过去式、过去分词；常见美式单 l']],
 'marshaled the volunteers 是组织了志愿者；carefully marshaled evidence 是仔细整理的证据。',
 'marshaled resources；marshaled the volunteers；carefully marshaled evidence。',
 'marshaled 与 marshalled 是拼写变体，过去时间与完成意义相同；不是一个指人、另一个指资源。',
 ('The coordinator marshaled the volunteers into small teams.','协调员把志愿者组织成几个小组。'),('She marshaled her arguments before the debate.','辩论前，她整理好了论据。'),sources=S('marshaled','marshal'))
W('marshalled','英 /ˈmɑːʃəld/；美 /ˈmɑrʃəld/','组织、调配、整理了〔过去式、过去分词；常见英式拼写〕',
 '同样是把人力或思路组织起来，英式常写 marshalled，双写 l。读音和 marshaled 没有因为多一个字母就多一节。',
 'marshal 双写末尾 l + -ed → marshalled；英式在这类词尾常双写 l，-ed 仍读 /d/。',MARSHAL+[['marshal 双写 l + -ed → marshalled','常见英式过去式、过去分词；与单 l 形式同义']],
 'marshalled the crowd 是有秩序地引导人群；well-marshalled evidence 是组织得很好的证据。',
 'marshalled resources；marshalled the crowd；marshalled the evidence。',
 '双写 l 不代表末尾重读；marshal 的重音仍在第一音节。英式词尾 l 双写不能机械套成只能重读末节才双写。',
 ('The organisers marshalled the crowd into separate lines.','组织者把人群引导成几条队伍。'),('He marshalled all the available information before making a decision.','决定之前，他把现有信息全都整理了一遍。'),sources=S('marshalled','marshal'))
W('marshaling','英 /ˈmɑːʃəlɪŋ/；美 /ˈmɑrʃəlɪŋ/','正在组织、调配、整理〔常见美式拼写〕',
 '把志愿者分组，把资料排成论证，这些组织过程是 marshaling。不是只把东西堆到一起，还让它们有次序、能发挥作用。',
 'marshal + -ing → marshaling，美式常见单 l；英式常写 marshalling，读音和主要用法相同。',MARSHAL+[['marshal + -ing → marshaling','常见美式现在分词、动名词']],
 'marshaling resources 是调集资源；marshaling support 是组织、争取支持；marshaling evidence 是整理证据。',
 'marshaling resources；marshaling support；marshaling evidence。',
 'gathering 侧重收拢；marshaling 常进一步强调有条理地组织、安排，以便用来完成目标。',
 ('The team is marshaling its resources for the final stage.','团队正在为最后阶段组织调配资源。'),('Marshaling the evidence took longer than writing the summary.','整理证据花的时间比写摘要还长。'),sources=S('marshaling','marshal'))
W('marshalling','英 /ˈmɑːʃəlɪŋ/；美 /ˈmɑrʃəlɪŋ/','正在组织、调配、整理〔常见英式拼写〕',
 '英式常见 marshalling，仍是把人、资源或信息组织到位的过程。双 l 属拼写习惯，不另添一层调配含义。',
 'marshal 双写 l + -ing → marshalling，英式常见；与美式常见 marshaling 相对应。',MARSHAL+[['marshal 双写 l + -ing → marshalling','常见英式现在分词、动名词']],
 'marshalling the crowd 是组织引导人群；marshalling arguments 是组织论据。一个现实队伍，一个思路队伍，都能排出次序。',
 'marshalling the crowd；marshalling resources；marshalling arguments。',
 'marshalling 与 marshaling 不需要按不同动作背两份词义；记住同一动词和地区拼写习惯即可。',
 ('Staff were marshalling the crowd outside the venue.','工作人员正在场馆外组织引导人群。'),('She spent the morning marshalling arguments for her proposal.','她整个上午都在为提案组织论据。'),sources=S('marshalling','marshal'))
W('martial','英 /ˈmɑːʃəl/；美 /ˈmɑrʃəl/','军事的；战争的；与武艺有关的',
 'martial arts 是武术：先把 martial 看成“战斗、军事这一类的”。它不表示一种具体动作，而是给 arts 等名词划出领域。',
 '中世纪拉丁 martialis 接 Mars、Mart- 罗马战神名 + 关系形容词材料 -ialis，借入英语为 martial。名字先指神，形容词再用于战争、军中事务。',
 [['拉丁 Mars、Mart- 战神名 + -ialis → martialis','与战神、战争有关的'],['英语 martial：战争的、军事的','martial arts 用于武艺、武术等战斗技艺']],
 'martial arts 是武术；martial music 是军乐一类具有军事色彩的音乐；martial law 是军事管制、戒严相关名称。',
 'martial arts；martial music；martial law。',
 'martial 与 marshal 常见读音相同，来源和词性不同：martial arts 用形容词，marshal resources 用动词。',
 ('She has practised martial arts for several years.','她练武术已经好几年了。'),('The band played martial music during the parade.','游行时，乐队演奏了军乐。'),sources=S('martial','martial'))
W('prone','英 /prəʊn/；美 /proʊn/','易于……的、倾向于……的；俯卧的',
 '身体往前俯是一种倾斜；性格、设备总容易往某种结果“偏过去”，也是倾向。prone 把这两种关系连在一起。',
 '借拉丁 pronus 向前弯、俯下，也有倾向义；可能接 pro 向前的材料。英语“容易、倾向”义的记录比俯卧义早，不要把记忆画面当英语历史顺序。',
 [['拉丁 pronus：向前俯、倾向于','可能接向前的 pro 等材料，细分并非全确定'],['英语 prone：容易出现某种结果；也指脸朝下俯卧','两义借倾斜、偏向这一关系相通']],
 'prone to errors 是容易出错；prone to doing something 是容易做某事；lie prone 是脸朝下趴着。to 在前两种常见结构里是介词。',
 'prone to errors；prone to forgetting；lie prone。',
 'prone to 后常接名词或 -ing；与 likely to do 的不定式结构分开记。俯卧 prone 是脸朝下，supine 常是脸朝上。',
 ('The old system is prone to errors.','旧系统容易出错。'),('He lay prone on the floor to look under the cabinet.','他趴在地上往柜子底下看。'),sources=S('prone','prone'))
W('gem','英、美 /dʒem/','宝石；珍品；出色、难得的人或事物',
 '一小块珍贵宝石是 a gem；偶然发现的一家好书店、一个特别可靠的人，也能被夸为 a gem。重点从“石头”移到了“难得、珍贵”。',
 '通常经法语 gemme 接拉丁 gemma 宝石，也有芽的旧义；古英语 gimm 曾直接借拉丁词，后续形式有汇合讨论。较远究竟怎样连接芽、牙等材料，并无全无争议的解释。',GEM,
 'a precious gem 是宝石；a hidden gem 是不太出名但很出色的人、地方、作品；you are a gem 是亲切地夸人真好。',
 'a precious gem；a hidden gem；a gem of a book。',
 'gem 和 jewel 都可比喻珍品；gem 不必表示东西价格真的很高，一家便宜小店也能是 a hidden gem。',
 ('A small blue gem was set in the ring.','戒指上镶着一小颗蓝色宝石。'),('This little bookshop is a hidden gem.','这家小书店是个不太为人所知的宝藏。'),sources=S('gem','gem'))
W('gems','英、美 /dʒemz/','宝石；珍品、精彩之处〔复数〕',
 '几颗宝石是 gems；一本书里几段特别精彩的文字，也可以当成几颗“珍珠宝石”来夸。这里比喻的是出色、值得留下。',
 'gem + -s → gems，/m/ 后后缀读 /z/；多个实物或多个值得珍视的内容都能数。',GEM+[['gem + -s → gems','宝石与比喻珍品的复数，后缀 /z/']],
 'precious gems 是宝石；hidden gems 是尚未广为人知的好地方、好作品等；gems of advice 是几条精彩建议。',
 'precious gems；hidden gems；literary gems。',
 'gems 指宝石或珍品；germs 是细菌、萌芽等另一词，常见读音 /dʒɜːmz/ 与 /dʒemz/ 的元音不同。',
 ('The museum displays gems from several regions.','博物馆展出来自几个地区的宝石。'),('The collection contains a few forgotten literary gems.','这套选集收录了几篇被遗忘的文学佳作。'),sources=S('gems','gem'))
W('midst','英、美 /mɪdst/','中间、当中；事情进行之中',
 '站在人群当中，或正忙在一场变化里，常用 in the midst of。它把“周围都是这件事、自己处在其中”的感觉说出来。',
 '中古英语 mid 中间 + 旧副词性属格 -s → middes，后来出现 t，可能受最高级等形式影响。末尾 st 不是现代把 mid 变成最高级。',
 [['mid 中间 + 旧副词性 -s → middes','中古英语的历史构词，不是现代复数'],['middes → midst','t 的增加有类比解释；名词用于中间、过程中']],
 'in the midst of a crowd 是在人群中；in the midst of a move 是正忙着搬家；in our midst 是在我们当中。',
 'in the midst of；in our midst；in the midst of change。',
 'midst 常在固定结构里用；普通说房间正中，也常直接用 in the middle of the room。midst 不能自动表示精确几何中心。',
 ('We arrived in the midst of a lively discussion.','我们到时，一场热烈讨论正进行着。'),('She remained calm in the midst of the confusion.','混乱之中，她仍保持镇定。'),sources=S('midst','midst'))
W('cedar','英 /ˈsiːdə/；美 /ˈsidɚ/','雪松等树木；相应木材',
 '看到枝叶常绿的树，或闻到木柜里有香气的木材，标签可能写 cedar。它是树名，也能借给木材；具体种类要看名称语境。',
 '古英语 ceder 与法语 cedre 等形式汇合，接拉丁 cedrus、希腊 kedros 雪松、杜松类旧名；更远来源不确定。',CEDAR,
 'a cedar tree 是一棵 cedar 类树木；cedar wood 是相应木材；a cedar chest 是这种木材做的箱柜。',
 'a cedar tree；cedar wood；a cedar chest。',
 '日常 cedar 也用于一些不属于严格雪松属的树；认词时知道俗名可能宽于植物属名，便不会把所有 cedar 标签机械当同一种树。',
 ('A tall cedar shaded the corner of the garden.','一棵高大的雪松为花园一角遮阴。'),('The chest was made of cedar.','箱柜由雪松类木材制成。'),sources=S('cedar','cedar'))
W('cedars','英 /ˈsiːdəz/；美 /ˈsidɚz/','雪松等树木〔复数〕',
 '路旁一排 cedar 类树木，是 cedars。树按棵数，砍下加工成木材后，cedar 又常按材料不可数使用。',
 'cedar + -s → cedars，后缀读 /z/；英美对末尾 r 的处理不同，复数后缀仍为浊音。',CEDAR+[['cedar + -s → cedars','多棵树；材料用法通常不按这个复数数木料']],
 'tall cedars 是高大的树；a row of cedars 是一排；cedar furniture 则以单数材料名修饰家具。',
 'tall cedars；a row of cedars；cedars along the path。',
 'cedars 常按树木个体计数；cedar wood 通常说木材，不能只因木料来自多棵树就必须用 cedars wood。',
 ('A row of cedars screened the house from the road.','一排雪松挡住了从路上望向房子的视线。'),('The old cedars cast long shadows across the lawn.','那些老雪松在草坪上投下长长的影子。'),sources=S('cedars','cedar'))
W('pines','英、美 /paɪnz/','松树〔复数〕；因思念而憔悴、渴望〔第三人称单数〕',
 '山坡几棵松树，是 pines；he pines for home 是他思乡心切。拼写一样，历史上是两条来源，不能编成松树会思念的故事。',
 '松树 pine 接拉丁 pinus，经法语及早期借入形式；思念动词 pine 接古英语 pinian 使受苦、折磨，较远可能接拉丁 poena 惩罚。两者分别加 -s → pines，读 /z/。',
 [['树名：拉丁 pinus → pine；动词：古英语 pinian 使受苦 → pine','不同来源，现代形同'],['pine + -s → pines','树名复数；或思念动词第三人称单数']],
 'tall pines 是高松；pines for home 是渴望回家、思乡；pines away 是因忧伤、思念而日渐憔悴。',
 'tall pines；a row of pines；pines for home。',
 'pine for 不只是随口想要，通常更深、更带失落；名词 pines 才能直接数成 three pines。',
 ('Tall pines lined the mountain road.','高大的松树排列在山路旁。'),('The character pines for the home she left behind.','这个角色深深思念自己离开的故乡。'),sources=S('pines','pine'))
W('heather','英 /ˈheðə/；美 /ˈhɛðɚ/','石南类植物；石南花',
 '荒原坡地上一片低矮灌木，开着紫粉色小花，常见的名字是 heather。先用这种风景画面记植物，不把名字当成人物职业。',
 '接苏格兰、英格兰北部等地区的旧植物名 hathir 等，较远可能有凯尔特语背景但不确定；词形受 heath 荒原影响的解释，不等于确定由 heath + -er 派生。',
 [['北部、苏格兰等旧植物名称 → heather','更远来源不确定，heath 可能影响了外形'],['heather：常见石南类灌木、花','整体植物名；不是“在荒原做事的人”']],
 'purple heather 是紫花石南；heather-covered hills 是长满石南的山坡。按植被、材料说时通常不可数。',
 'purple heather；heather on the hillside；a patch of heather。',
 'Heather 首字母大写也能是人名；阅读风景描写时，小写 heather 常是植物，不能因为认识某个人名就漏掉普通词义。',
 ('Purple heather covered the hillside.','山坡上长满了开紫花的石南。'),('We rested beside a patch of heather.','我们在一片石南旁歇了一会儿。'),sources=S('heather','heather'))
W('glen','英、美 /ɡlen/','狭长山谷〔尤用于苏格兰语境〕',
 '两边山坡夹着一条狭长谷地，在苏格兰风景、地名里常叫 glen。它给 valley 加了一层地区用词和典型地貌的色彩。',
 '经苏格兰语接盖尔语 gleann 山谷，同族还有其他凯尔特语山谷词。整个地貌名称借入英语。',GLEN,
 'a wooded glen 是长着树木的山谷；a narrow glen 是狭谷。Glen 开头的地名常能借这层山谷意思理解，但具体名称仍有自身历史。',
 'a narrow glen；a wooded glen；a quiet glen。',
 'valley 是更普通、范围更广的谷地词；glen 常突出苏格兰等语境下的狭长山谷。',
 ('A stream ran through the quiet glen.','一条溪流穿过宁静的山谷。'),('We followed the path into a wooded glen.','我们沿小路走进一处林木覆盖的山谷。'),sources=S('glen','glen'))
W('glens','英、美 /ɡlenz/','狭长山谷〔复数〕',
 '穿过一处山谷，又走进另一处，这些谷地可以统称 glens。复数数不同的山谷，而不是山谷里有几条溪流。',
 'glen + -s → glens，/n/ 后复数后缀读 /z/；盖尔语借来的单词再按英语方式形成复数。',GLEN+[['glen + -s → glens','多个山谷；末尾 /nz/']],
 'wooded glens 是长着树木的山谷；remote glens 是偏远山谷；hills and glens 是山坡与谷地。',
 'wooded glens；remote glens；hills and glens。',
 'glens 是谷地复数，Glenn 等可能是人名拼写；风景描述和专名要看大小写、上下文，不只看字母近似。',
 ('The trail crosses several wooded glens.','这条步道穿过几处林木覆盖的山谷。'),('Mist filled the glens at sunrise.','日出时，雾气弥漫在各处山谷里。'),sources=S('glens','glen'))
W('cod','英 /kɒd/；美 /kɑd/','鳕鱼；鳕鱼肉',
 '菜单里的 fish and chips 如果写 cod，是说选用鳕鱼。整条鱼可以数；切成鱼肉做菜时，又按食材来理解。',
 '中古英语已有 cod 鱼名，更远来源不明。它与古英语 codd 袋子虽相似，但缺少确定联系，不宜按鱼像袋子编成唯一来源。',
 [['中古英语 cod：鳕鱼名','更远来源不明，与袋子旧词的联系未确证'],['英语 cod：鱼种、个体 → 食用鱼肉','常见单复数同形，可说 one cod、several cod']],
 'baked cod 是烤鳕鱼；a cod fillet 是一片鳕鱼片；several cod 可以数多条鱼，普通复数不一定加 s。',
 'baked cod；a cod fillet；cod and chips。',
 'cod 是具体鱼名；fish 是鱼的大类。商品名可能含其他修饰语，不能只因白色鱼肉就把所有鱼都叫 cod。',
 ('I ordered baked cod with vegetables.','我点了烤鳕鱼配蔬菜。'),('The boat returned with several large cod.','渔船带着几条大鳕鱼回来了。'),sources=S('cod','cod'))
W('influenza','英 /ˌɪnfluˈenzə/；美 /ˌɪnfluˈɛnzə/','流行性感冒；流感',
 '正式一点写 influenza，日常常缩成 flu。这个长词有一段旧观念背景：人们曾把疾病归于星体、天气等带来的影响。',
 '借意大利 influenza，接中古拉丁 influentia 影响，与 influence 同族；in- 向内 + fluere 流，较远是流入、影响材料。疾病名沿旧影响观念形成，再进入英语。',INFLUENZA,
 'influenza outbreak 是流感暴发；an influenza report 是流感报告。这里学习疾病名称与缩略关系，不把历史命名里的星体观念当现代解释。',
 'influenza outbreak；influenza cases；a report on influenza。',
 'influenza、flu 对应流感；a cold 是普通感冒的名称，词义不等于把 cold 加重语气就变成 influenza。',
 ('The report discusses the history of influenza.','报告讨论了流感的历史。'),('Several performances were cancelled because of influenza.','几场演出因为流感取消了。'),sources=S('influenza','influenza'))
W('flu','英、美 /fluː/','流感〔influenza 的常用缩略词〕',
 '把 influenza 中间最醒目的 flu 音节留下，就得到日常短词 flu。它省掉长词两端，不是只从开头截一截。',
 'influenza → flu，中间音节截取式缩略；英语早期也见 flue 拼写，后来 flu 固定下来。更远接意大利疾病名与拉丁影响词族。',INFLUENZA+[['influenza 截取中间 flu → flu','英语常见的疾病短称；末尾没有 e']],
 'have flu、have the flu 都可见，地区习惯有差异；flu season 是流感季。通常按疾病名不可数使用。',
 'have the flu；flu season；a flu outbreak。',
 'flu、flew 飞的过去式、flue 烟道通常同音 /fluː/，现代意思不同。flu 虽有早期 flue 写法，今天普通疾病名用 flu。',
 ('She missed the rehearsal because she had the flu.','她因为得了流感，没参加排练。'),('The school sent parents a note about flu season.','学校给家长发了一份关于流感季的通知。'),sources=S('flu','flu'))
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_zin',ROOTS,WORDS)
 extend_lessons()
