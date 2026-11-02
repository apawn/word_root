"""Dead and die: state, change and transparent compounds."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
D=[['古英语 dēad → 中古英语 ded','死的；不活跃的'],['现代英语 dead','死亡状态 → 不运作、完全没有反应；也可加强语气']]
W('dead','/ded/','死的；不工作的；完全、十足地',
 '抓住没有生命、没有反应的状态：动物可以死去，电池也可以一点电都没了；后者是比喻。',
 '继承古英语 dēad，属于死亡词族。现代 dead 是形容词，也可作加强语气的副词，不要把它当 die 的过去式。',D,
 'a dead battery 没电的电池，a dead tree 枯树；dead quiet 一片寂静，dead serious 十分认真，dead centre 正中心。语境决定是失去生命、失去功能，还是完全达到某种程度。',
 'a dead battery；dead quiet；dead serious；the dead 死者。',
 'die 说死去这个变化，dead 说死了的状态，death 是死亡这件事。He died yesterday；He is dead，不能说 He is die。',
 ('The remote is not working because the batteries are dead.','遥控器不工作了，因为电池没电了。'),('I am dead serious about changing jobs.','我对换工作这件事是十分认真的。'))
W('undead','/ʌnˈded/','不死的；亡灵、活死人一类的',
 '故事里明明与死亡有关，却还能活动的存在，比如吸血鬼和僵尸。',
 'un- + dead。旧英语阶段已有相应组合，现代超自然用法因吸血鬼文学等变得熟悉；不能把整个词的首次出现归给《德古拉》。',D+[['un- + dead → undead','否定死亡状态；现代奇幻中特指死而仍能活动']],
 'the undead 可统称这类生物；an undead army 是亡灵军队。日常活着的人通常叫 alive，不叫 undead。',
 'the undead；an undead creature；an undead army。',
 'alive 正常活着，undead 带着奇幻中的死亡与复活设定；immortal 不会死，概念也不同。',
 ('The castle is guarded by an army of the undead.','城堡由一支亡灵军队守卫。'),('In the game, undead creatures emerge after sunset.','游戏中，不死生物在日落后出现。'))
W('deadlock','英 /ˈdedlɒk/；美 /ˈdedlɑːk/','僵局；死锁',
 '几方互相卡住，谁也推进不了：谈判中没人让步，程序中也可能各自等着对方释放资源。',
 'dead 无法活动 + lock 锁住，组合出卡死的画面。现代谈判、政治和计算机语境都常用，门锁领域也有相应名词。',D+[['dead + lock → deadlock','动不了地锁住 → 僵局；程序相互等待的死锁']],
 'break the deadlock 打破僵局；reach a deadlock 陷入僵局。程序死锁有特定的互相等待关系，并非所有卡顿都叫 deadlock。',
 'break a deadlock；a political deadlock；a database deadlock。',
 'delay 只是延迟，deadlock 强调各方互相堵住；stalemate 也指无法进展的僵局，本有棋局背景。',
 ('A compromise finally broke the deadlock.','一项折中方案终于打破了僵局。'),('The two processes entered a deadlock while waiting for each other.','两个进程在互相等待时陷入了死锁。'))
W('deadbeat','/ˈdedbiːt/','赖账、逃避责任的人；筋疲力尽的',
 '常用名词带着责备：该付的钱、该担的责任都躲开；较旧的形容词用法还能说累瘫了。',
 'dead 表完全 + beat 被打垮、累坏；精疲力竭的用法较早，后来名词用于游手好闲、逃避付款或责任的人。现代要按词性和语境理解。',D+[['dead + beat → deadbeat','完全累垮；后来也作贬义人物称呼']],
 'a deadbeat tenant 常说赖租的房客，a deadbeat dad 指逃避抚养责任的父亲。这个词是口语贬称，语气比 late payer 重。',
 'a deadbeat tenant；a deadbeat dad；deadbeat customers。',
 'broke 没钱，deadbeat 指被说成逃避责任；一次付晚了不自动等于长期赖账。',
 ('The landlord complained that the tenant was a deadbeat.','房东抱怨那个房客是个赖账的人。'),('She refused to lend more money to her deadbeat brother.','她不肯再借钱给那个总逃避责任的哥哥。'))
W('deadwood','/ˈdedwʊd/','枯木；无用、拖累整体的部分',
 '先想一棵树上已经枯死的枝木，再想一份文稿里占地方、却不起作用的内容。',
 'dead 枯死的 + wood 木材、树木。由真实枯木扩展为组织、计划或作品中不再发挥作用的部分。',D+[['dead + wood → deadwood','枯死木材 → 被认为无用的部分']],
 'remove deadwood 可以是清理枯枝，也可以是删掉无效内容。用于人时是很不客气的评价。',
 'clear away deadwood；remove the deadwood；deadwood in a draft。',
 'deadwood 说失去作用，dead forest 是整片死去的森林；别把 wood 在这里只理解成一块板。',
 ('The gardener cleared deadwood from the path.','园丁清走了小路上的枯木。'),('The editor cut the deadwood from the first draft.','编辑删掉了初稿中无用的内容。'))
W('deadpan','/ˈdedpæn/','面无表情的；不动声色地讲笑话',
 '嘴里说着很好笑的事，脸上却像什么都没发生：笑点就在这种反差里。',
 'dead 无表情、无反应 + pan 旧俚语脸。pan 在这个组合里不是平底锅；组合早期用于没有表情的脸，后来用于这种幽默的表达方式。',D+[['dead + pan（脸）→ deadpan','脸无反应 → 不动声色的表达']],
 'deadpan humour 冷面幽默，a deadpan delivery 一本正经的讲述方式；还可作副词或动词，表示面不改色地说。',
 'deadpan humour；a deadpan expression；deadpan delivery。',
 'serious 真认真，deadpan 只说表面不露情绪；内容可能非常荒诞。',
 ('Her deadpan delivery made the joke even funnier.','她一本正经地讲出来，让笑话更好笑了。'),('He gave a deadpan reply, and nobody knew whether he was joking.','他面无表情地回答，谁也不知道他是不是在开玩笑。'),sources=['https://www.etymonline.com/word/deadpan','https://en.wiktionary.org/wiki/deadpan#English'])
W('deadlift','/ˈdedlɪft/','硬拉',
 '健身中，把原本静止在地面的重量拉起来；名称抓住从静止状态起重这个特点。',
 'dead 静止、不活动 + lift 举起，组合成为运动名词，也可作动词。这里不是抬死人，dead 对应静止的负重。',D+[['dead + lift → deadlift','从静止状态提起重量 → 硬拉']],
 'a deadlift 是一次硬拉动作，也可泛指该项目；a deadlift competition 是硬拉比赛。',
 'do a deadlift；a deadlift record；a deadlift competition。',
 'lift 是广义举起，deadlift 是具体力量训练项目；weightlifting 在不同语境可泛称举重，也可指竞技举重项目。',
 ('The competition ended with the deadlift event.','比赛以硬拉项目结束。'),('She set a personal record in the deadlift.','她在硬拉项目中创造了个人纪录。'))
W('deadbolt','英 /ˈdedbəʊlt/；美 /ˈdedboʊlt/','呆锁锁舌；带这种锁舌的门锁',
 '门上那种需要用钥匙或旋钮移进移出的锁舌，不靠关门时弹回的弹簧动作工作。',
 'dead 在这里表示不靠弹簧自行活动 + bolt 门闩、锁舌。bolt 还有闪电等意思，但这个组合接的是门闩义。',D+[['dead + bolt → deadbolt','非弹簧自行动作的锁舌 → 相应门锁']],
 'a deadbolt lock 是这类门锁；lock the deadbolt 是把这种锁锁好。中文可按物件说锁舌或门锁。',
 'a deadbolt lock；lock the deadbolt；install a deadbolt。',
 'latch 常指能弹回、扣住门的门闩或锁舌；deadbolt 着重其需要主动移入移出的结构。',
 ('The apartment has a deadbolt on the front door.','公寓前门装有一把呆锁。'),('She turned the key to lock the deadbolt.','她转动钥匙，把门锁锁好。'))
W('deadhead','/ˈdedhed/','摘去残花；空驶、空驶行程',
 '园艺里是去掉已经谢掉的花头；交通里是车辆在移动，却没有载着付费乘客或货物。',
 'dead + head。花头义可直观看出 dead flower head；交通、免费入场等用法有各自的使用史，不把空驶硬说成从剪花发展而来。',D+[['dead + head → deadhead','枯萎花头等组合义；另有非营运运输用法'],['现代动词用法','摘去残花；车辆空驶']],
 'deadhead the roses 给玫瑰摘残花；a bus deadheads back to the depot 是公交车空驶返回车场。大写 Deadhead 还可指某乐队歌迷，是另一具体语境。',
 'deadhead the flowers；deadhead back to the depot；a deadhead trip。',
 'deadhead 空驶不等于车辆没油坏掉；在园艺中只去掉残花头，也不同于砍掉整棵植物。',
 ('She deadheaded the roses after the flowers faded.','花谢后，她摘掉了玫瑰的残花。'),('The bus deadheaded back to the depot after its final service.','最后一班营运结束后，公交车空驶返回车场。'))
R('B3064','死亡状态；失去活动与反应','DEAD：已经不活、不动，或完全没有反应','从 dead 的状态出发，读 undead 的奇幻设定，再把卡住、枯木和无表情这些扩展分别理解。',
 'dead 继承古英语 dēad。复合词多利用失去生命、不活动或完全的含义；每个组合接的第二部分也要选对意思。',
 'dead → undead；dead + lock、wood、pan、lift、bolt、head；deadbeat 的人物贬称单独辨析。',
 [['状态与变化','die · dying · dead · death · undead'],['卡住与不起作用','deadlock · deadbeat · deadwood'],['具体复合词','deadpan · deadlift · deadbolt · deadhead']],
 'dead 形容状态，die 表变化；pan 是旧俚语脸，bolt 是门闩。不要只看到 dead 就把每个组合都解释成死人。',
 'The battery is dead, but the phone itself is fine.\n\n电池没电了，但手机本身没问题。',
 'die dying dead death undead deadlock deadbeat deadwood deadpan deadlift deadbolt deadhead')
DI=[['中古英语 deyen 等，可能借自古诺尔斯语 deyja 等北欧形式','死去；具体借入关系保留不确定性'],['现代英语 die → dying','生命结束 → 声音、风俗等逐渐消失；夸张表示渴望']]
W('die','/daɪ/','死去；消失、停止运作；另有骰子、模具名词',
 '动词抓住从活着到不再活着这个变化。声音可以渐渐消失，机器也可以突然不工作，都是扩展用法。',
 '死亡动词见中古英语 deyen 等，可能来自古诺尔斯语 deyja 等北欧形式。名词 die 骰子借古法语 de，与死亡动词来源不同；再往前联系拉丁 datum 是一种解释，不作定论。模具义也属另一名词使用史。',DI+[['另一路古法语 de → 英语名词 die','骰子；与死亡动词分开理解']],
 'die down 逐渐平息，die out 逐渐消失，die away 声音等渐弱。骰子通常单数 a die、复数 dice；工业中 a die 也可指成形、压印工具。',
 'die down；die out；die away；roll a die。',
 'die—died—died；dead 是死的状态，不能拿来代替过去式。die 骰子与 die 死去是同形词，别编成掷骰子导致死亡的故事。',
 ('The wind died down after midnight.','午夜过后，风渐渐小了。'),('Roll a die and move your piece that many spaces.','掷一枚骰子，然后把棋子移动相应的格数。'),sources=['https://www.etymonline.com/word/die','https://en.wiktionary.org/wiki/die#English'])
W('dying','/ˈdaɪɪŋ/','快死的；逐渐消失的；极想做某事的',
 '生命或事物快到尽头，还没彻底结束；口语也可以夸张说想得不得了。',
 'die 加 -ing 时 ie 改 y，成为 dying。字母变化是拼写规则，不是加了另一个词根。渴望用法是死亡动词的夸张扩展。',DI+[['die + -ing → dying','正在死去、消退 → 夸张说极其渴望']],
 'a dying tradition 正在消失的传统，the dying minutes 最后几分钟；be dying to do 极想做，be dying for something 极想要。',
 'a dying tradition；be dying to see；be dying for a drink；the dying minutes。',
 'dying 源自 die，dyeing 源自 dye 染色：加 -ing 时 dye 保留 e。I am dying to see it 通常是在表达迫切期待。',
 ('The museum documents a dying craft.','博物馆记录了一门正在消失的手艺。'),('I am dying to hear what happened next.','我特别想知道接下来发生了什么。'))
R('B2450','死去、消退；死亡过程与状态','DIE：从有生命、有活动走向结束','先把 die、dying、dead、death 连起来，再分开处理同形的骰子名词。',
 '死亡动词可能经北欧语言进入中古英语；dead 与 death 属相关古老词族，但现代形式不能机械地把 death 说成 die 加一个随意拼出的后缀。',
 'die → died、dying；dead 形容状态，death 表死亡；骰子 die 走法语名词路线。',
 [['变化、进行、状态与事件','die · dying · dead · death']],
 'dying 不是 dyeing；a die 的骰子义与死去动词来源分开。',
 'The noise slowly died away.\n\n声音慢慢消失了。',
 'die dying dead death')
if __name__=='__main__':save('continuation_20261029_dm',ROOTS,WORDS)
