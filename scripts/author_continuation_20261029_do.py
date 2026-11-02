"""Wonder and door families."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
WO=[['古英语 wundor、wundrian → 中古英语 wonder、wondren','令人惊奇的事；感到惊奇'],['现代 wonder','惊叹 → 好奇、心里想知道']]
W('wonder','英 /ˈwʌndə/；美 /ˈwʌndər/','想知道；感到惊奇；奇观、惊叹',
 '一件事让你停下来：有时是太神奇，有时是还不明白，想知道怎么回事。',
 '继承古英语 wundor 名词和相关动词 wundrian。现代动词把惊奇与好奇连接起来，I wonder 常说心中疑问。',WO,
 'I wonder why... 我想知道为什么；wonder at something 对某事惊奇；a wonder 可以是奇观或令人惊叹的人事。no wonder 难怪。',
 'wonder why；wonder whether；no wonder；the wonders of nature。',
 'wonder 想知道，wander 漫步、走神，拼写和发音都不同；I wonder where he is 采用陈述语序，不说 where is he。',
 ('I wonder why the shop is closed today.','我想知道这家店今天为什么没开。'),('It is no wonder she is tired after such a long journey.','走了这么长的路，难怪她累了。'))
W('wonderful','英 /ˈwʌndəfəl/；美 /ˈwʌndərfəl/','非常好的；令人赞叹的',
 '最初是让人惊叹，如今日常经常只是很棒、非常令人愉快。',
 'wonder + -ful，相应组合古英语已有。由充满惊奇、令人惊叹，扩展成常用赞美形容词。',WO+[['wonder + -ful → wonderful','令人惊叹的 → 很棒的']],
 'a wonderful idea 很棒的主意，have a wonderful time 玩得很开心；不要求事情超自然或史无前例。',
 'a wonderful idea；wonderful news；have a wonderful time。',
 'wonderful 常正面赞美；wonder 本身可以只是好奇，不能把 I wonder 译成我觉得很棒。',
 ('Thank you for a wonderful evening.','谢谢你让我度过一个美好的夜晚。'),('That is a wonderful idea for the school project.','那是一个很棒的学校项目点子。'))
W('wonderment','英 /ˈwʌndəmənt/；美 /ˈwʌndərmənt/','惊奇；惊叹',
 '看到让人赞叹的东西，一时看呆了的那种感觉。比普通说想知道更聚焦惊奇的心情。',
 'wonder + -ment，后缀将感受、状态名词化。相较日常 wonder，wonderment 语气更有描写感。',WO+[['wonder + -ment → wonderment','惊奇 → 惊叹的心情']],
 'in wonderment 惊叹地，a sense of wonderment 一种惊奇感；适合描写初见新世界、自然景观时的感受。',
 'in wonderment；a sense of wonderment；look on in wonderment。',
 'wonderment 惊叹，bewilderment 困惑不知所措；新奇有时令人惊叹，有时令人迷糊，焦点不同。',
 ('The children watched the night sky in wonderment.','孩子们惊叹地望着夜空。'),('The exhibition filled her with wonderment.','展览让她充满惊奇。'))
R('B3697','惊叹、好奇与很棒','WONDER：一件事让你停下来，觉得神奇或想弄明白','先学 wonder 想知道、惊叹，再读 wonderful 的日常赞美和 wonderment 的惊奇感。',
 '继承古英语惊奇词族。wonderful 的现代赞美已经非常日常，不必每次译得神乎其神。',
 'wonder → wonderful、wonderment；wonder + land、boy → wonderland、wonderboy。',
 [['核心与状态派生','wonder · wonderful · wonderment'],['奇妙世界与出众人物','wonderland · wonderboy']],
 'wonder 与 wander 区分；wonderful 常是很棒，wonderment 更具体是惊奇的感觉。',
 'I wonder who designed this wonderful garden.\n\n我想知道是谁设计了这座美妙的花园。',
 'wonder wonderful wonderment wonderland wonderboy')
DO=[['古英语 duru、dor → 中古英语 dore → door','门、门户'],['现代 door 词族','出入口 → 相关部件、人员；也比喻机会']]
W('door','英 /dɔː/；美 /dɔːr/','门；出入口；机会之门',
 '分隔里外又让人通过的那道门；由能不能进来，很自然地用来比喻机会。',
 '继承古英语 duru、dor 等，属于很古老的门词族。现代复合词常用它作可辨认的完整基本词。',DO,
 'open the door 开门；open doors for someone 给某人创造机会；next door 是隔壁，the people next door 是隔壁的人。',
 'open the door；at the door；next door；open doors for。',
 'door 可指活动门扇或门口，doorway 更明确说门的开口；gate 常指围墙、院子等的门或出入口。',
 ('Someone is waiting at the door.','有人正在门口等。'),('Learning another language can open doors for you.','学习另一门语言可以为你打开机会之门。'))
W('indoor','英 /ˈɪndɔː/；美 /ˈɪndɔːr/','室内的',
 '把活动、场所放到门以内，也就是屋里；这个词主要拿来修饰名词。',
 'in 或 within + door 的组合发展而来，历史有门内的空间画面。现代 indoor 是常用形容词，与 indoors 副词有分工。',DO+[['in + door → indoor','门内 → 室内的']],
 'indoor activities 室内活动，an indoor pool 室内泳池，indoor plants 室内植物。',
 'indoor activities；indoor sports；an indoor pool。',
 'indoor 修饰名词，indoors 表在室内：indoor games；play indoors。不要说 We stayed indoor。',
 ('The hotel has an indoor swimming pool.','这家酒店有一个室内游泳池。'),('We planned some indoor activities because of the rain.','因为下雨，我们安排了一些室内活动。'))
W('doorstep','英 /ˈdɔːstep/；美 /ˈdɔːrstep/','门前台阶；门口、近在眼前',
 '人还没进门，先踩到或站在那一块门前台阶；再由门口扩展为就在身边。',
 'door + step 台阶。现代既可指实际台阶，也可泛指门前区域或极近的位置。',DO+[['door + step → doorstep','门前台阶 → 门口、近旁']],
 'on the doorstep 在门口；on your doorstep 就在你家附近。英国媒体里 doorstep 作动词还可指堵在门口采访。',
 'on the doorstep；leave something on the doorstep；right on your doorstep。',
 'doorstep 通常在门前，threshold 更聚焦门槛、入口边界；生活中的位置可能很近，不能把所有 doorstep 都画成门槛。',
 ('A parcel was waiting on the doorstep.','门口放着一个包裹。'),('We have a beautiful park right on our doorstep.','我们家附近就有一座美丽的公园。'))
W('doorbell','英 /ˈdɔːbel/；美 /ˈdɔːrbel/','门铃',
 '门外的人按一下，让屋里的人知道有人来了。',
 'door + bell 铃，按门口通知来人的用途组合；现代电子门铃未必真的含有传统金属铃。',DO+[['door + bell → doorbell','门口的铃 → 门铃']],
 'ring the doorbell 按门铃，answer the doorbell 听到门铃后去应门；不要因为 ring 也有打电话义就译成打门电话。',
 'ring the doorbell；hear the doorbell；a video doorbell。',
 'doorbell 发声或发送通知，doorknob 是开门用的圆把手，功能不同。',
 ('Please ring the doorbell and wait.','请按门铃后稍等。'),('The dog barked when the doorbell rang.','门铃一响，狗就叫了起来。'))
W('doorknob','英 /ˈdɔːnɒb/；美 /ˈdɔːrnɑːb/','圆形门把手',
 '门上凸出来、让你用手握住转动的圆把手。',
 'door + knob 圆形凸起、旋钮。knob 的 k 不发音；组合中也不读成带 /k/ 的音。',DO+[['door + knob → doorknob','门 + 圆形把手 → 圆形门把手']],
 'turn the doorknob 转动圆把手，a brass doorknob 黄铜门把手；日常也可泛称门把。',
 'turn the doorknob；a loose doorknob；a brass doorknob。',
 'door handle 范围更宽，包括长柄把手；doorknob 更突出圆形旋钮形状。',
 ('She turned the doorknob and pushed the door open.','她转动门把手，把门推开。'),('The old brass doorknob was loose.','那个旧黄铜门把手松了。'))
W('doorframe','英 /ˈdɔːfreɪm/；美 /ˈdɔːrfreɪm/','门框',
 '围住门洞、让门能够装上去的框架；门开了，这个框还留在墙上。',
 'door + frame 框架，按结构直接组合。frame 不只是照片框，在建筑里也是承托、围合的框架。',DO+[['door + frame → doorframe','门 + 框架 → 门框']],
 'a wooden doorframe 木门框，lean against the doorframe 倚着门框。door frame 分写也常见。',
 'a wooden doorframe；paint the doorframe；lean against the doorframe。',
 'door 门扇可开合，doorframe 是四周的框；doorway 是供人通过的门口空间。',
 ('He leaned against the doorframe while they talked.','他们交谈时，他倚着门框。'),('The painter applied a fresh coat of paint to the doorframe.','油漆工给门框刷了一层新漆。'))
W('doormat','英 /ˈdɔːmæt/；美 /ˈdɔːrmæt/','门垫；任人欺负、摆布的人',
 '本来是进门前供人擦鞋、踩在脚下的垫子；拿来说人，就是总被别人踩着、从不坚持自己。',
 'door + mat 垫子，由门前擦鞋垫扩展为对任人摆布者的比喻。人物义带贬意，常出现在劝人别一味退让的表达里。',DO+[['door + mat → doormat','门口脚垫 → 被人随意对待的人']],
 'wipe your feet on the doormat 在门垫上擦鞋；treat someone like a doormat 把某人当成好欺负的人。',
 'a welcome doormat；wipe your feet on the doormat；treat someone like a doormat。',
 'polite 礼貌，a doormat 强调缺少界限、任人利用；礼貌不自动等于任人摆布。',
 ('Please wipe your feet on the doormat.','请在门垫上擦擦鞋。'),('She decided she would no longer let people treat her like a doormat.','她决定不再让别人随意欺负、摆布自己。'))
W('doorman','英 /ˈdɔːmən/；美 /ˈdɔːrmən/','门童；门卫、门口接待人员',
 '在建筑入口迎接来客、帮忙开门或管理出入的人，具体职责看场所。',
 'door + man，人、男子的组合成分。词形保留历史上以男子命名职业的方式；现代常见于酒店、公寓等场所。复数 doormen。',DO+[['door + man → doorman','门口工作的人 → 门童、门卫']],
 'a hotel doorman 酒店门童，the apartment doorman 公寓门卫；不一定只是全天替人拉门，也可能负责接待、协助叫车等。',
 'a hotel doorman；an apartment doorman；ask the doorman。',
 'doorman 与 receptionist 接待员工作可能有交集，但 receptionist 通常在接待台，doorman 聚焦入口。',
 ('The doorman helped us carry the bags inside.','门童帮我们把包提进了里面。'),('Ask the doorman which entrance to use.','问问门卫该走哪个入口。'))
W('trapdoor','英 /ˈtræpdɔː/；美 /ˈtræpdɔːr/','活板门；地板、天花板上的翻板门',
 '看起来是地板或天花板的一块，掀开后才发现可以通往上面或下面。',
 'trap + door。历史 trap 有捕捉装置等相关意思，现代 trapdoor 专指常在地板、天花板上的活板门；实际不一定是为了陷害谁。',DO+[['trap + door → trapdoor','特殊开合的门 → 活板门']],
 'a trapdoor in the floor 地板上的活板门，open the trapdoor 掀开活板门；舞台、阁楼入口都可能出现。',
 'a trapdoor in the floor；open a trapdoor；a hidden trapdoor。',
 'trap 陷阱可用来捕捉，trapdoor 是门的类型；安全通往阁楼的活板门也叫 trapdoor。',
 ('A trapdoor in the ceiling led to the attic.','天花板上的一扇活板门通往阁楼。'),('The actor disappeared through a trapdoor in the stage.','演员从舞台上的活板门消失了。'))
R('B3040','门、门口与相关部件','DOOR：分隔里外，也提供进出的通道','从 door 出发，先分清门、门洞、门框，再把台阶、铃、把手和门垫放到门口这个场景里。',
 'door 是古英语继承词。现代复合词通常清楚保留 door；有的再发展出比喻，比如 doormat 的任人摆布义。',
 'door → doorway、doorframe；door + step、bell、knob、mat、man、stop；indoor、outdoor 表里外；trapdoor 是活板门。',
 [['核心、门洞与门框','door · doorway · doorframe'],['门口与门上的物件','doorstep · doorbell · doorknob · doormat · doorstop'],['工作人员与特殊门','doorman · trapdoor'],['室内与室外','indoor · outdoor']],
 'indoor 形容词、indoors 副词；doormat 的人喻义是任人摆布，不等于礼貌。trapdoor 不一定是陷阱。',
 'The doorman opened the door while a parcel sat on the doorstep.\n\n门童打开门，门口台阶上放着一个包裹。',
 'door doorway doorframe doorstep doorbell doorknob doormat doorstop doorman trapdoor indoor outdoor')
if __name__=='__main__':save('continuation_20261029_do',ROOTS,WORDS)
