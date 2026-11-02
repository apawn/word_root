"""Following, pursuit, persistent trouble and memorable impressions."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
def S(word,base):
 return ['https://en.wiktionary.org/wiki/'+word+'#English','https://www.etymonline.com/word/'+base]
EXISTING_ROOT_ADDITIONS={
 'A1697':dict(words='stalk stalks stalked stalking stalker stalkers'.split(),label='stalk 的茎与潜行分路，stalker 的角色扩展',note='stalk 植物茎名词与潜行动词分别保留来源分析；stalker 是跟踪行动者，不从植物茎直接推出。'),
 'C1317':dict(words='pursue pursues pursued pursuing pursuer pursuers'.split(),label='pursue：沿着目标一路跟进',note='经古法语 poursuir 等接拉丁 prosequi，pro- 向前加 sequi 跟随；现代 pursues、pursuers 分别是动词三单与人物词复数。'),
 'C0168':dict(words='catch chase chases chased chasing chaser chasers'.split(),label='chase 与 catch 的法语双式词联系',note='追逐义 chase、catch 经不同法语形式联系拉丁 capere、captare 一路；现代追赶不保证已经抓住。'),
 'B3088':dict(words='tail tails tailed tailing'.split(),label='tail 从尾巴到跟在尾后、逐渐减弱',note='动物尾巴承古英语 taegl 等材料；现代跟踪动词从在后跟随扩展。带尾形容 tailed 的记录早于现代跟随动词，不能全当动作过去式。'),
 'B3369':dict(words='shadow shadows shadowed shadowing'.split(),label='shadow：阴影笼罩与形影相随',note='shade、shadow 接古英语同一词的不同形态发展；shadowed 可说遮暗、情绪笼罩或跟着观察，按宾语辨义。'),
 'B4609':dict(words='dog dogs dogged dogging doggedly doggedness'.split(),label='dog 的追随纠缠与 dogged 顽强坚持',note='动词 dog 用紧跟不放的形象；形容词 dogged 的旧负面评价后来发展出顽强义，末尾 -ed 读 /ɪd/，和动词过去式 /dɒɡd/、/dɔːɡd/ 分清。'),
 'C0164':dict(words='hound hounds hounded hounding'.split(),label='hound：旧泛称狗到猎犬，再到追逼',note='hound 来自古英语 hund，较远与拉丁 canis 属同源材料，不是从 canis 直接借来；名词后来收窄为猎犬，动词再扩展为追逼不放。'),
 'A1740':dict(words='haunt haunting hauntingly'.split(),label='hauntingly：印象反复回来、久久不散',note='haunt 经法语常去、反复来访材料，远源未定；hauntingly 接 -ly，较早还用过经常地的意思，现代难忘义不是唯一原始义。'),
}
STALK=[['植物茎名词与悄悄移动动词的旧材料分别发展','潜行动词可接古英语 bestealcian 等，较远分析有分歧'],['现代 stalk：潜近、持续跟踪；另有昂首大步走','同形不同画面，不能从植物茎一路硬推所有动作义']]
W('stalks','英 /stɔːks/；美 /stɔːks/','茎梗〔复数〕；潜行跟踪、昂首大步走〔第三人称单数〕',
 '花下面直直支撑着的几根茎是 stalks；猫悄悄接近猎物，动词也写 stalks。词性、宾语一变，画面就不同。',
 'stalk + -s，词尾读 /s/；茎名词和移动动词保留不同来源分析，现代常见读音中 l 不单独发出。',STALK+[['stalk + -s → stalks','多个茎梗；它潜近目标，或某人昂首大步走']],
 'flower stalks 花茎；stalks its prey 潜近猎物；stalks out of the room 高傲或气冲冲地大步出屋。',
 'celery stalks 芹菜梗；stalks through the grass。',
 'stalks 作动词有悄悄接近和大步走两种近乎相反的样子；有无猎物宾语、out 等方向词能帮助判断。',
 ('Cut the flower stalks before putting them in water.','把花插进水里前，先剪一下花茎。'),('The cat stalks its prey through the grass.','猫穿过草丛，悄悄接近猎物。'),sources=S('stalks','stalk'))
W('stalked','英 /stɔːkt/；美 /stɔːkt/','潜近、跟踪了；昂首或气冲冲地大步走了；有茎的',
 '猫压低动作接近目标，可以说 stalked；一个人生气后挺着身子大步离开，也能说 stalked out。不能只记成慢慢走。',
 '动作词 stalk + -ed，/k/ 后读 /t/；形容植物有茎的 stalked 则可按茎名词加“具有”的 -ed 理解。',STALK+[['stalk + -ed → stalked','动作过去式；另有以茎名词构成的有茎形容词']],
 'stalked a deer 悄悄跟踪鹿；stalked out 大步离开；a long-stalked flower 是长茎花，常见复合修饰语另看整体。',
 'stalked through the grass；stalked away without a word。',
 'stalked someone 在现代人物场景可说持续跟踪、纠缠；动物捕猎场景则通常是在说潜近猎物。',
 ('The cat stalked the bird without making a sound.','猫不声不响地悄悄接近那只鸟。'),('He stalked out of the room without saying goodbye.','他没道别，就气冲冲地大步走出了房间。'),sources=S('stalked','stalk'))
W('stalkers','英 /ˈstɔːkəz/；美 /ˈstɔːkərz/','跟踪者；持续跟踪、纠缠他人的人〔复数〕',
 '一次巧合碰到不算这个画面；总跟着一个人、反复关注其去向，让对方摆脱不了的人，现代常叫 stalkers。',
 'stalk + -er → stalker，再加复数 -s；构词接潜行、跟踪动词，不接花茎名词。',STALK+[['stalk + -er + -s → stalkers','多个跟踪者；现代常指反复纠缠的人']],
 'online stalkers 在网上反复跟踪、纠缠别人的人；protect someone from stalkers 帮某人摆脱跟踪者。',
 'stalkers following a celebrity；unwanted contact from stalkers。',
 'followers 可以是普通关注者、追随者；stalkers 常带不受欢迎、持续纠缠的意味，不能只因关注账号就随意互换。',
 ('The actor spoke about unwanted messages from stalkers.','那位演员谈到了跟踪纠缠者发来的骚扰消息。'),('The novel follows two stalkers who keep appearing outside the same house.','小说写了两个跟踪者，他们总出现在同一栋房子外。'),sources=S('stalkers','stalk'))
PURSUE=[['拉丁 pro- 向前 + sequi 跟随 → prosequi','一路跟着、伴随、继续跟进'],['古法语 poursuir、porsivre 等 → 英语 pursue','追赶目标，也追求梦想、继续开展某项工作']]
W('pursues','英 /pəˈsjuːz/；美 /pərˈsuːz/','追赶、追求；继续进行〔第三人称单数〕',
 '目标在前面，自己一路跟上去，可以是追一个人，也可以是追一门学业、一个梦想；动词用 pursues。',
 'pursue + -s，词尾读 /z/；基础词经法语接拉丁 pro- + sequi，现代结尾 ue 的 e 不单独发音。',PURSUE+[['pursue + -s → pursues','他、她沿目标追赶、寻求或继续开展']],
 'pursues a career 追求某种职业；pursues a lead 跟进线索；pursues further study 继续深造。',
 'pursues his dream；pursues the suspect。',
 'pursues a goal 说持续朝目标行动，不保证目标已经达到；achieves the goal 才明确达到。',
 ('She pursues her dream of becoming an architect.','她努力追求成为建筑师的梦想。'),('The reporter pursues every promising lead.','这名记者会跟进每一条有希望的线索。'),sources=S('pursues','pursue'))
W('pursuers','英 /pəˈsjuːəz/；美 /pərˈsuːərz/','追赶者、追求者〔复数〕',
 '不是只说追的动作，而是点名后面追着的人：被追的人拐进小巷，想甩掉的就是 his pursuers。',
 'pursue 去不发音 e，加完整人物后缀 -er → pursuer，再加 -s；不是只加一个 -r。',PURSUE+[['pursue → pursuer → pursuers','把追赶、追求的动作变成行动者，再作复数']],
 'escape from pursuers 甩开追赶者；pursuers of knowledge 追求知识的人，较正式。',
 'stay ahead of the pursuers；lose his pursuers 甩掉追他的人。',
 'pursuers 是行动者复数；pursues 才是动词三单，多了 -er 就把视角转成谁在追。',
 ('He turned into a narrow lane to lose his pursuers.','他拐进一条窄巷，想甩掉追他的人。'),('The deer disappeared into the forest ahead of its pursuers.','鹿赶在追赶者前面，消失在森林里。'),sources=S('pursuers','pursue'))
CHASE=[['拉丁 capere 拿、抓 → captare 等追取材料','经重建通俗拉丁语 *captiare 及不同法语形式发展'],['古法语 chacier 等 → chase；另一路形成 catch','英语追赶动词与追逐名词都有法语背景，不把名词全当现代动词新造']]
W('chases','/ˈtʃeɪsɪz/','追赶、追逐、催办〔第三人称单数〕；追逐场面〔复数〕',
 '球滚到前面，狗跑着追；事情一直没回音，人去追问进度；chases 都有跟着目标往前赶的劲头。',
 'chase + -s，/s/ 后读 /ɪz/；名词复数也同形。基础词与 catch 经不同法语形式联系同一拉丁追取材料。',CHASE+[['chase + -s → chases','他、她追赶、追问；多次追逐']],
 'chases the ball 追球；chases up an order 跟催订单；car chases 汽车追逐场面。',
 'chases a dream 追梦；chases away the birds 赶走鸟。',
 'chases 描写追的过程；catches 明确抓到、赶上。追了很久，仍可能没抓到。',
 ('The dog chases the ball across the lawn.','狗追着球跑过草坪。'),('The film is full of dramatic car chases.','这部电影里有很多惊险的汽车追逐场面。'),sources=S('chases','chase'))
W('chased','/tʃeɪst/','追赶、追逐了；赶走了；催问了',
 '刚才目标在前面动，自己跟着追过去，叫 chased；chased away 则把重点放在追赶到对方离开。',
 'chase 去 e 加完整 -ed，/s/ 后词尾读 /t/，结尾 /st/；不要把它念成多一个 /ɪd/。',CHASE+[['chase → chased','过去追赶、驱赶或催问']],
 'chased the bus 追公交车；chased away the birds 赶走鸟；chased up the missing order 催问那笔没到的订单。',
 'chased after someone；chased a dream。',
 'chased someone 是追赶某人，chased someone away 是把某人赶开，away 把离开的结果写出来。',
 ('We chased the bus but failed to catch it.','我们追着公交车跑，却没赶上。'),('The dog chased the birds away from the garden.','狗把鸟从花园里赶走了。'),sources=S('chased','chase'))
W('chasers','英 /ˈtʃeɪsəz/；美 /ˈtʃeɪsərz/','追赶者、追逐某种目标的人；烈酒后的跟饮〔复数〕',
 '追着某个目标跑的人能叫 chasers；喝完烈酒再接一口别的饮料，后面这口像跟在后头，也叫 a chaser。',
 'chase 去 e 加完整 -er → chaser，再加 -s；旧人物词也有法语同类词的影响，饮料义后来形成。',CHASE+[['chase → chaser → chasers','追逐者；饮料中跟在烈酒后的一杯，再作复数']],
 'storm chasers 追逐观察风暴的人；fortune chasers 追逐财富的人；water chasers 烈酒后跟饮的水。',
 'ambulance chasers 是带贬义的固定说法；chasers following the leaders 追赶领先者的人。',
 'chasers 的饮料义不说明要把两杯混在一起，重点是后面接着喝；人物义则看前面修饰词写追什么。',
 ('The documentary follows storm chasers across the plains.','这部纪录片跟拍了在平原上追逐风暴的人。'),('The menu lists several drinks that can be served as chasers.','菜单列出了几种可作为烈酒后跟饮的饮料。'),sources=S('chasers','chase'))
TAIL=[['古英语 taegl、taegel 等 → tail','动物身体后面的尾部，后来扩展到物体末端、后部'],['跟在尾后 → 动词 tail；另有具有尾巴的形容构词','tailed 有尾的记录很早，不能把所有 tailed 都当现代跟踪动词的过去式']]
W('tails','/teɪlz/','尾巴〔复数〕；硬币反面；燕尾服；跟踪〔第三人称单数〕',
 '几条尾巴是 tails；硬币有头像那面之外的反面，投币时也叫 tails；人一直跟在后头，动词同样写 tails。',
 'tail + -s，词尾读 /z/；名词复数、动词三单同形。硬币反面和燕尾服义是各自固定发展出的用法。',TAIL+[['tail + -s → tails','多个尾部；特定名词用法；他、她跟踪']],
 'heads or tails 正面还是反面；wear tails 穿燕尾服；tails the suspect 跟踪嫌疑人。',
 'dogs wagging their tails；tails someone through the crowd。',
 'tales 是故事，tails 是尾巴等，两者常同音；写投币选反面时用 tails。',
 ('The dogs wagged their tails when we arrived.','我们一到，狗就摇起尾巴。'),('I called tails before the coin landed.','硬币落下前，我选了反面。'),sources=S('tails','tail'))
W('tailed','/teɪld/','跟踪了；逐渐减弱了；有尾巴或尾状部分的',
 '一辆车一路跟在后面，是 tailed us；声音越来越小，是 tailed off；描述某物有尾部，也能用 tailed 作修饰材料。',
 '动词 tail + -ed，词尾读 /d/；有尾的形容词则接尾巴名词加“具有”的 -ed，相关形容形式早于现代跟随动词。',TAIL+[['tail + -ed → tailed','跟随动作过去式；另路也可表示具有尾部']],
 'tailed someone home 一路跟踪某人到家；interest tailed off 兴趣逐渐消退；short-tailed 在复合形容词里说短尾的。',
 'tailed the car；the applause tailed off 掌声渐弱。',
 'tailed off 比 stopped 更容易让人看见一点点减少、弱下去；stopped 只说停止，未说明渐变过程。',
 ('A grey car tailed us all the way to the bridge.','一辆灰色汽车一路跟踪我们到了桥边。'),('The applause tailed off as the lights came on.','灯一亮，掌声便渐渐弱了下去。'),sources=S('tailed','tail'))
W('tailing','/ˈteɪlɪŋ/','正在跟踪、跟在后面；正在逐渐减弱',
 '目标车拐了个弯，后面的车也跟着拐，这个持续跟在后头的动作叫 tailing；tailing off 则像尾端一点点收小。',
 'tail + -ing；这里接跟随动词，工业语境 tailings 矿尾料是另一个常见名词形式，需按场景辨认。',TAIL+[['tail + -ing → tailing','正在跟在尾后；与 off 连用写逐渐减少']],
 'tailing someone 跟踪某人；tailing behind 跟在后面；sales tailing off 销量正在减少。',
 'a car tailing us；interest tailing off。',
 'following 可以普通跟随，tailing someone 通常更像盯着目标的行动；尾随的目的还要由上下文交代。',
 ('I think that car has been tailing us since the station.','我觉得那辆车从车站起就一直在跟踪我们。'),('Interest in the event was tailing off by the end of the week.','到周末时，人们对这次活动的兴趣正在逐渐减退。'),sources=S('tailing','tail'))
SHADOW=[['古英语 sceadu 及相关格变化形式 → shade、shadow','同一旧词不同形式后来发展为两个英语词'],['阴影笼罩；像影子随人 → 跟踪、跟班观察','遮光、情绪阴影与形影相随是不同现代场景']]
W('shadowed','英 /ˈʃædəʊd/；美 /ˈʃædoʊd/','被阴影遮暗的；笼罩了；跟踪、跟班观察了',
 '树把脸遮在阴影里，是 shadowed；人一路像影子跟着另一人，也是 shadowed；跟着同事看他怎么工作，可是学习式跟班。',
 'shadow + -ed，词尾读 /d/；基础词来自旧名词、动词材料，现代不能把 shadow 硬拆成 shade + ow。',SHADOW+[['shadow + -ed → shadowed','遮暗、笼罩或像影子一样跟随已经发生']],
 'a shadowed face 被阴影遮住的脸；shadowed a colleague 跟班观察同事；shadowed by worry 被忧虑笼罩。',
 'shadowed by tall trees；shadowed the manager for a day。',
 'shadowed someone 可以是秘密跟踪，也可以是获准跟班学习；看有没有工作、培训等场景，不统一翻成尾随。',
 ('Her face was shadowed by the wide brim of her hat.','宽大的帽檐把她的脸遮在阴影里。'),('I shadowed an experienced colleague on my first day.','第一天，我跟着一位有经验的同事观察学习。'),sources=S('shadowed','shadow'))
DOG=[['古英语 docga 等 → 中古英语 dogge → dog','狗；基础词更远来源仍未明'],['dog 动词：像狗追着一样紧跟、纠缠','dogged 形容词的旧负面犬性评价，后来也说顽强坚持；现代两支分开读、用']]
W('dogging','英 /ˈdɒɡɪŋ/；美 /ˈdɔːɡɪŋ/','正在紧追、纠缠；持续困扰',
 '一个问题像甩不掉的狗一样一直跟着，刚处理完又冒出来，用 dogging 很形象：它持续缠着人或事情。',
 'dog 双写末尾 g 加 -ing → dogging；这是动词动作形式，不是 dogged 顽强形容词再接词尾。',DOG+[['dog → dogging','双写 g，加 -ing，正在紧跟、持续困扰']],
 'problems dogging the project 持续困扰项目的问题；bad luck dogging someone 厄运总跟着某人。这里选日常动词义。',
 'rumours dogging a company；injuries dogging a season。',
 'dogging 侧重不肯离开、持续纠缠；bothering 更一般地说造成烦扰，未必有这种紧跟不放的时间感。',
 ('Technical problems have been dogging the project for months.','技术问题已持续困扰这个项目好几个月。'),('Rumours kept dogging the company after the announcement.','公告发布后，各种传闻仍一直缠着这家公司。'),sources=S('dogging','dogged'))
W('doggedly','英 /ˈdɒɡɪdli/；美 /ˈdɔːɡɪdli/','顽强地；执拗地；不肯放弃地',
 '一次没做成，再试；别人走了，自己还守着目标继续做，这种咬住不松口的坚持可以说 doggedly。',
 '形容词 dogged + -ly；dogged 的 ed 在这个词里读 /ɪd/，不是动词过去式 dogged 的单音节结尾。',DOG+[['dogged → doggedly','早期可带恶劣等评价，后来常写顽强坚持的做事方式']],
 'work doggedly 顽强地工作；doggedly pursue a goal 咬定目标追求；doggedly refuse 执拗地拒绝。',
 'doggedly continue；doggedly stick to the plan。',
 'doggedly 可夸不放弃，也可嫌过于执拗；看坚持的是值得做的目标，还是不肯改的立场。',
 ('She worked doggedly until the last piece of the puzzle fitted.','她一直不放弃地拼，直到最后一块拼图也对上。'),('He doggedly refused to change his answer.','他执拗地拒绝改答案。'),sources=S('doggedly','dogged'))
W('doggedness','英 /ˈdɒɡɪdnəs/；美 /ˈdɔːɡɪdnəs/','顽强；不屈不挠；执拗',
 '做不成还继续做、不轻易被困难赶走，把这种劲头当作一个品质，就叫 doggedness。',
 'dogged + 性质名词 -ness；保留形容词中 ed 的 /ɪd/，不是 dog 动词过去式再随便加名词尾。',DOG+[['dogged → doggedness','把顽强、执拗的性质拿出来讨论']],
 'sheer doggedness 单凭不放弃的劲；admire someone’s doggedness 佩服某人的顽强。',
 'patience and doggedness；succeed through doggedness。',
 'talent 是天赋，doggedness 是咬定不松口的坚持；句子可以用二者对照，解释成功靠的是什么。',
 ('She finished the task through sheer doggedness.','她全靠不放弃的劲头完成了任务。'),('I admire his doggedness, even when I disagree with his methods.','即使不认同他的办法，我也佩服他的顽强。'),sources=S('doggedness','dogged'))
HOUND=[['古英语 hund → hound','早先泛指狗，较远与拉丁 canis 属同源词，不是英语借自拉丁词'],['一般的狗 → 猎犬；由名词转为 hound 动词','用猎犬追猎，后来也说像追猎一样追逼、纠缠人不放']]
W('hound','/haʊnd/','猎犬；追逼、纠缠不放',
 '猎犬循着目标一路追，是名词 hound 的画面；人不停追问、烦扰另一个人，动词 hound 像追着不肯放。',
 '承古英语 hund，原来更广泛说狗，后来常收窄到猎犬。动词由名词发展；同源拉丁 canis 是亲属词，不是直接上一级借词。',HOUND,
 'a hunting hound 猎犬；hound someone for an answer 缠着某人要答案；hound someone out 追逼到某人不得不离开。',
 'a pack of hounds 一群猎犬；hound someone with questions。',
 'dog 是一般的狗，hound 常说猎犬；动词 hound 往往让被追逼者感到压力，不能当普通 ask 随意替换。',
 ('The hound followed the scent through the woods.','猎犬循着气味穿过树林。'),('Please do not hound me for an answer before I have read the report.','我还没读报告，请别不停追着我要答案。'),sources=S('hound','hound'))
W('hounds','/haʊndz/','猎犬〔复数〕；追逼、纠缠〔第三人称单数〕',
 '几只循迹追猎的狗是 hounds；一个人每天追问同一件事、不给别人喘口气，动词也用 hounds。',
 'hound + -s，词尾读 /z/，结尾 /ndz/；名词复数和动词三单同形。',HOUND+[['hound + -s → hounds','多只猎犬；他、她不停追逼、纠缠']],
 'a pack of hounds 一群猎犬；hounds someone about something 为某事一直缠着某人。',
 'hounds following a scent；hounds him for a reply。',
 'hounds 作动词重点是反复追逼的压力，reminds 只说提醒，语气通常轻得多。',
 ('We heard the hounds barking beyond the trees.','我们听见树林那边的猎犬在叫。'),('He hounds me about the deadline every morning.','他每天早上都缠着我追问截止日期的事。'),sources=S('hounds','hound'))
W('hounded','/ˈhaʊndɪd/','被追逼、纠缠了；不停追问了',
 '已经说想安静一下，对方却仍追着问、追着要，这种过去或被动承受的压力，可以用 hounded。',
 'hound + 完整 -ed，基础以 /d/ 结尾，所以词尾读 /ɪd/；不是所有 -ed 都只读 /d/。',HOUND+[['hound + -ed → hounded','过去持续追逼；也构成被追逼、被纠缠的状态']],
 'was hounded by reporters 被记者不断追问；hounded someone for money 缠着某人要钱。',
 'hounded out of a job 被追逼得离职；hounded by questions。',
 'hounded 是具体的持续追逼、烦扰；haunted 更常写记忆、担心挥之不去，两个词不是拼写小变体。',
 ('She was hounded by reporters after the announcement.','公告发布后，记者们一直追着她问。'),('They hounded him for a decision all week.','他们整整一周都追着他要决定。'),sources=S('hounded','hound'))
W('hounding','/ˈhaʊndɪŋ/','正在追逼、纠缠；持续烦扰的行为',
 '对方还在一遍遍追问，自己感觉被紧紧跟住、不让停，这段过程就叫 hounding。',
 'hound + -ing，直接接完整词尾；可作进行形式，也可把反复追逼当作一种行为名词。',HOUND+[['hound + -ing → hounding','追逼过程正在进行；也指这种持续烦扰']],
 'stop hounding someone 别再缠着某人；constant hounding 不停追逼；hounding someone for a reply 追着要回复。',
 'hounding him with questions；tired of the hounding 厌倦了持续纠缠。',
 'hounding 常带被迫应付的烦扰感，following up 可以中性说跟进；两者不能只按“追踪”二字混用。',
 ('Stop hounding me; I said I would call tomorrow.','别再缠着我了，我说过明天会打电话。'),('He was tired of the constant hounding about his private life.','别人不停追问私生活，让他厌倦了。'),sources=S('hounding','hound'))
HAUNT=[['古法语 hanter：常去、反复来访等 → haunt','较远来源未定，与北欧回家材料的联系是一种分析'],['反复回来 → 出没、萦绕心思 → haunting、hauntingly','旧 hauntingly 还曾表示经常地；现代常写令人难忘、久久不散的印象']]
W('hauntingly','英 /ˈhɔːntɪŋli/；美 /ˈhɔːntɪŋli/','令人难以忘怀地；萦绕心头地',
 '一段旋律已经停了，却还像在心里回响；一张脸看过之后久久忘不掉，修饰这种美、熟悉或忧伤，可以用 hauntingly。',
 '现代按 haunt + -ing → haunting，再加副词 -ly；较早相关副词还说经常地，现代难忘义是后来发展的。',HAUNT,
 'hauntingly beautiful 美得令人难忘；hauntingly familiar 熟悉得挥之不去；不要求场景里有鬼。',
 'a hauntingly sad melody；hauntingly clear memories。',
 'beautifully 可仅说优美，hauntingly beautiful 还说这份美会留在心里，常有幽远、忧伤的气氛，但不必是恐怖。',
 ('She sang a hauntingly beautiful melody.','她唱了一段美得令人难忘的旋律。'),('His voice sounded hauntingly familiar.','他的声音有一种挥之不去的熟悉感。'),sources=S('hauntingly','haunt'))
def extend_lessons():
 extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_zfx',ROOTS,WORDS)
 extend_lessons()
