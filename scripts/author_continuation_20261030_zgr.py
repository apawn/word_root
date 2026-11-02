"""Light movement, bumpy motion and small restless movements."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
def S(word,base):
 return ['https://en.wiktionary.org/wiki/'+word+'#English','https://www.etymonline.com/word/'+base]
EXISTING_ROOT_ADDITIONS={
 'B3106':dict(words='float flit flits flitted flitting'.split(),label='flit：古老搬移、浮动材料到轻快掠过',note='flit 接古诺斯 flytja 搬移，与 float 的更早日耳曼浮动材料同族；现代不只是飞行，想法、表情也可短暂掠过。'),
 'B2864':dict(words='dart darted darting'.split(),label='dart：像投出的尖物一样迅速窜过',note='动词由飞镖、投矛名词发展，近源法语更早接日耳曼材料；darting pain 也像尖痛突然射来。'),
 'A1697':dict(words='sprint sprinter sprinters'.split(),label='sprinters：短距离全速冲刺的人',note='sprinter 来自 sprint 加 -er，复数再加 -s；现代竞技用途接短距离高速跑，不把所有能跑的人都叫短跑选手。'),
 'B4418':dict(words='bump bumpy bumpier bumpiest bumpily bumpiness'.split(),label='bumpy：凸起让路不平、行程不顺',note='bump 加 -y，再有比较级、最高级、-ly、-ness；具体路面、飞行颠簸到过程不顺是语境扩展，不以中文一个颠字抹去方向。'),
 'B3903':dict(words='bounce bouncer bouncers'.split(),label='bouncers：把闹事者请出去的门卫等',note='bouncer 接 bounce 加 -er，旧 bounce 有捶击等义，后来可指场所维持秩序、驱走闹事者的人；不只按现代弹跳译成人在跳。'),
 'A1699':dict(words='twitch twitchy fidget fidgety wiggle wiggly wriggle wriggly squirm squirmy'.split(),label='几个 -y：抽动、坐不住、扭来扭去的不同画面',note='twitchy、fidgety、wiggly、wriggly、squirmy 各接自己的基底；共同 -y 写性质，不表示这些基础词全部同源。'),
 'B2811':dict(words='jerk jerky jerkily jerkiness'.split(),label='jerky：动作一顿一顿的；肉干另源',note='jerk 动作名词加 -y 的形容词再接副词、性质名词；肉干 jerky 接克丘亚语经西班牙语的另一条来源，不用于解释 jerkily。'),
}
FLIT=[['古诺斯 flytja 搬移 → 中古英语 flitten 等 → flit','更早与 float 的浮动材料同族，最初不限于小鸟飞动'],['搬移、离去 → 轻快短暂移动','现代可写鸟掠过、人穿梭、表情或想法一闪而过']]
DART=[['法语 dart、dard → 英语 dart 名词','投矛、飞镖，法语更早接日耳曼尖物名'],['名词 → dart 动词','刺、投掷，再有迅速突然移动；像飞镖一下射出的动作']]
SPRINT=[['早期 sprenten、sprint 的跳起、窜出材料','很可能与斯堪的纳维亚相关形式相连，路线细节有不确定性'],['sprint 短距离冲刺 + -er → sprinter','命名做这类跑动的人，再用 -s 表复数']]
BUMPY=[['bump 凸起、碰撞材料','远源未定，有拟声、北欧相关词等分析'],['bump + -y → bumpy','路面有凸起、行进颠簸，也比喻事情推进不顺']]
BOUNCER=[['bounce 的旧捶击、后来弹回与推赶等用法','远源未定，可能拟声或与邻近语言材料相连'],['bounce + -er → bouncer','早期实施者称呼，后来用于酒吧等维持秩序、驱走闹事者的人']]
JERKY=[['jerk 动作名词：急拉、突然一动','更早路线未完全确定；不接肉干那条克丘亚语来源'],['jerk + -y → jerky','动作一顿一顿，不平顺；再接 -ly、-ness 写方式与性质']]
W('flit','/flɪt/','轻快短暂地掠过、移动；穿梭；一闪而过',
 '小鸟一掠而过，想法在脑海闪一下就没了，都能 flit。它常是轻、快、停不久，不要求一直飞在空中。',
 '接古诺斯 flytja 搬移，经中古英语相应形式延续；与 float 的更早浮动材料同族，现代轻快移动义后来发展。',FLIT,
 'flit from flower to flower 在花间轻快穿梭；flit through the mind 在脑海一闪而过。',
 'flit across someone’s face 在脸上短暂掠过；flit between topics 在话题间跳来跳去。',
 'flit 多有轻快、短暂与位置变化，hover 是在一个地方盘旋、停留；小鸟不一定正在两者都做。',
 ('Butterflies flit from flower to flower.','蝴蝶在花间轻快穿梭。'),('Strange thoughts sometimes flit through my mind before sleep.','睡前，我脑海有时会闪过些奇怪的念头。'),sources=S('flit','flit'))
W('flits','/flɪts/','轻快掠过、穿梭；一闪而过〔第三人称单数〕',
 '她一会儿聊这个、一会儿聊那个，注意力停不住，叫 she flits between topics；笑容在脸上短暂出现，也能 flits across her face。',
 'flit + -s，/t/ 后读 /s/；继承搬移材料发展的现代轻快短暂动作义。',FLIT+[['flit + -s → flits','它、他或她轻快短暂地移动']],
 'flits from topic to topic 话题跳来跳去；flits across the face 在脸上一闪而过。',
 'flits through the branches；an idea flits through my mind。',
 'flits through my mind 通常只是短暂念头，stays on my mind 则更像一直盘桓；停留时间的画面不同。',
 ('A small bird flits between the branches.','一只小鸟在枝间轻快穿梭。'),('A smile flits across her face when she reads the note.','她读便条时，脸上掠过一丝笑意。'),sources=S('flits','flit'))
W('flitted','/ˈflɪtɪd/','轻快掠过、穿梭了；一闪而过了',
 '笑容在脸上闪了一下，或小鸟突然飞过，过去发生了就是 flitted。它很适合写短暂出现、没有停留的变化。',
 'flit 双写 t 加完整 -ed，/t/ 后读 /ɪd/；短元音后单个 t 按规则双写。',FLIT+[['flit + -ed → flitted','过去轻快短暂地移动、出现']],
 'flitted across the face 在脸上掠过；flitted through the room 在房间里轻快穿梭。',
 'flitted from one group to another；a thought flitted through his mind。',
 'flitted across her face 强调神情短暂掠过，remained on her face 是持续留着；不能都只译成脸上有。',
 ('A look of surprise flitted across his face.','他脸上掠过一丝惊讶。'),('The bird flitted out of sight.','小鸟轻快地飞走，不见了踪影。'),sources=S('flitted','flit'))
W('flitting','/ˈflɪtɪŋ/','正在轻快穿梭、掠过；短暂跳转',
 '晚会上她在人群间这里一句、那里一句，是 flitting from group to group；思绪不停跳转，也能用它写过程。',
 'flit 双写 t 加 -ing；规则动作形式，保留轻快、短暂停留的性质。',FLIT+[['flit + -ing → flitting','轻快短暂地移动、跳转正在发生']],
 'flitting between groups 在几群人间穿梭；flitting thoughts 闪来闪去的想法。',
 'flitting about the garden；flitting from one task to another。',
 'flitting from task to task 常突出停不住、浅尝辄止，working through tasks 可以是有次序做完；不是所有多任务都同一种画面。',
 ('She was flitting from one group of guests to another.','她正在几群客人之间轻快穿梭。'),('We watched butterflies flitting around the garden.','我们看着蝴蝶在花园里轻快飞来飞去。'),sources=S('flitting','flit'))
W('darted','英 /ˈdɑːtɪd/；美 /ˈdɑrtɪd/','突然窜过、冲过去了；迅速投去〔目光等〕',
 '老鼠一见人就像飞镖一样窜进洞，是 darted；眼睛迅速朝门口扫一下，也能 darted towards the door。',
 'dart + 完整 -ed，/t/ 后读 /ɪd/；动词由投矛、飞镖名词发展出迅速移动的用法。',DART+[['dart + -ed → darted','过去突然快速窜动，或投去目光']],
 'darted across the road 突然窜过马路；eyes darted towards the door 目光迅速投向门口。',
 'darted into a doorway；darted a glance 迅速瞥一眼。',
 'darted 比 walked 更有突然、方向明确的短促动作感，不一定持续远距离快速行进；a long sprint 是另一种持续冲刺。',
 ('A mouse darted under the cupboard.','一只老鼠突然窜到柜子下面。'),('Her eyes darted towards the door.','她的目光迅速投向门口。'),sources=S('darted','dart'))
W('darting','英 /ˈdɑːtɪŋ/；美 /ˈdɑrtɪŋ/','正在迅速窜动；短促射出的；突然刺来的',
 '鱼在水草间突然这里一下、那里一下，是 darting；darting pain 则把疼痛写成突然射来、短促的尖刺。',
 'dart + -ing；动作形式也形容快速、短促射出或袭来的性质。',DART+[['dart + -ing → darting','迅速窜动的过程；比喻像尖物突然射来']],
 'darting eyes 快速转动、扫视的眼睛；darting movements 突然快速的动作。',
 'fish darting between rocks；a darting pain 一阵短促尖痛。',
 'darting pain 强调突然、短促，dull ache 强调钝钝、隐隐地痛；词语写感受性质，不能仅凭名称判断具体原因。',
 ('We watched fish darting between the rocks.','我们看着鱼在石头间迅速穿梭。'),('His darting eyes kept returning to the clock.','他快速转动的目光总是又落回时钟上。'),sources=S('darting','dart'))
W('sprinters','英 /ˈsprɪntəz/；美 /ˈsprɪntərz/','短跑选手；全速短距离冲刺的人〔复数〕',
 '不是为了跑一整天，而是把速度在短距离里爆出来，这些人是 sprinters。运动项目里常就是短跑选手。',
 'sprint + -er → sprinter，再加复数 -s，读 /z/；旧跳起、窜出材料发展为短距离全速跑后，-er 命名做事的人。',SPRINT,
 'elite sprinters 顶尖短跑选手；the sprinters at the start 起跑线上的短跑选手。',
 'train sprinters；a race for sprinters。',
 'sprinters 着重短距离全速，distance runners 着重长距离跑；两者训练、项目侧重点不同，不是所有跑者都叫 sprinters。',
 ('The sprinters crouched at the starting line.','短跑选手蹲在起跑线上。'),('Elite sprinters practise their starts repeatedly.','顶尖短跑选手会反复练习起跑。'),sources=S('sprinters','sprint'))
W('bumpier','英 /ˈbʌmpiə/；美 /ˈbʌmpiər/','更颠簸、不平的；更不顺利的',
 '路上的凸起更多，车把人颠得更厉害，是 bumpier；计划一路遇到更多小阻碍，也像更难走的路。',
 'bumpy 的 y 变 i 加完整 -er；内层 bump + -y，外层比较颠簸、坎坷的程度。',BUMPY+[['bumpy → bumpier','更不平、更颠簸；比喻过程更不顺']],
 'a bumpier road 更颠簸的路；a bumpier ride 更颠簸的行程或更坎坷的经历。',
 'getting bumpier；bumpier than expected。',
 'bumpier road 讲不平带来的起伏，longer road 只讲长度；路颠不代表一定更长。',
 ('The road became bumpier after the village.','过了村庄，路变得更颠簸。'),('The project had a bumpier start than we expected.','项目开头比我们预想的更不顺。'),sources=S('bumpier','bumpy'))
W('bumpiest','/ˈbʌmpiɪst/','最颠簸、不平的；最坎坷的',
 '几条路线里，让人一路弹起来、坐不稳的那条最厉害，就是 the bumpiest；也能比喻一段推进最不顺的时期。',
 'bumpy 的 y 变 i 加完整 -est；所比范围内，凸起、颠簸、过程不顺的程度最高。',BUMPY+[['bumpy → bumpiest','最不平、最颠簸，或最不顺利']],
 'the bumpiest road 最颠簸的路；the bumpiest part of the trip 行程最颠簸的部分。',
 'our bumpiest flight；the bumpiest start。',
 'bumpiest 在经历中比喻不顺，不一定是最危险；危险程度是另一判断，不能从颠簸自动推出。',
 ('This was the bumpiest road we had travelled all week.','这是我们一周来走过最颠簸的路。'),('The first month was the bumpiest part of the transition.','第一个月是过渡过程中最不顺的阶段。'),sources=S('bumpiest','bumpy'))
W('bumpily','/ˈbʌmpɪli/','颠簸地；一颠一颠地',
 '车轮压过一处处不平，整辆车一颠一颠往前，是 bumpily。它把路面凸起变成乘坐时的运动感受。',
 'bumpy 的 y 变 i 加 -ly → bumpily；性质形容词变成动作方式副词。',BUMPY+[['bumpy + -ly → bumpily','以被凸起颠动、不平顺的方式前进']],
 'rode bumpily 颠簸着行驶；bumpily along the track 沿小路一颠一颠地走。',
 'moved bumpily；bumpily down the lane。',
 'bumpily 说路面、气流等造成的不平顺运动，quickly 只说快；颠簸也可能发生在慢速移动中。',
 ('The cart rolled bumpily along the track.','小车沿小路一颠一颠地前进。'),('We rode bumpily down the rough lane.','我们沿着崎岖的小路颠簸而下。'),sources=S('bumpily','bumpy'))
W('bumpiness','/ˈbʌmpinəs/','颠簸、不平；过程的坎坷不顺',
 '把不是平平顺顺、总一颠一颠的性质提出来，就是 bumpiness；可说路、旅途，也可比喻事情推进。',
 'bumpy 的 y 变 i 加 -ness → bumpiness；把性质、程度整体名词化。',BUMPY+[['bumpy + -ness → bumpiness','不平、颠簸或过程不顺的程度、状态']],
 'the bumpiness of the road 路面的颠簸；some initial bumpiness 初期一些不顺。',
 'reduce bumpiness；complained about the bumpiness。',
 'bumps 是一个个凸起，bumpiness 是整体不平、颠簸的性质；不能把 a few bumps 的可数结构随意搬给性质名词。',
 ('The suspension reduced the bumpiness of the ride.','悬挂系统减轻了行驶中的颠簸。'),('Some bumpiness was expected during the transition.','过渡过程中预计会有一些不顺。'),sources=S('bumpiness','bumpy'))
W('bouncers','英 /ˈbaʊnsəz/；美 /ˈbaʊnsərz/','酒吧、夜店等的门卫、秩序维护人员〔复数〕',
 '酒吧门口把关、闹事时把人请出去的工作人员，常叫 bouncers。-er 命名实施者，重点是维持秩序、把闹事者带出去的角色。',
 'bounce 去 e 加 -er → bouncer，再加复数 -s。实施者后缀可命名人、器具；门卫义接旧捶击、后来驱走等材料，不是人整晚在弹跳。',BOUNCER+[['bounce → bouncer → bouncers','多个维持秩序的人，或多个弹动设备等']],
 'club bouncers 夜店门卫；two bouncers at the entrance 门口两名秩序维护人员。',
 'bouncers at the door 门口的保安；bouncers checking tickets 正在查票的门卫。',
 'bouncers 常用于夜店、酒吧门口的角色，security guards 更宽泛；办公室、博物馆保安不必都叫 bouncers。',
 ('Two bouncers checked tickets at the club entrance.','两名门卫在夜店门口查票。'),('The bouncers calmly escorted the noisy group outside.','秩序维护人员平静地把那群吵闹的人带了出去。'),sources=S('bouncers','bouncer'))
W('twitchy','/ˈtwɪtʃi/','容易抽动的；紧张不安、反应敏感的',
 '神经绷着，听见一点动静就一激灵，显得 twitchy；字面上也能说肌肉、眼皮容易短促抽动。',
 'twitch + -y；基底承古英语 twiccian 拔、抓、急扯材料，后来有肌肉短促抽动，形容词再写这类反应、不安性质。',
 [['古英语 twiccian → twitch','拔、急扯到短促抽动'],['twitch + -y → twitchy','容易抽动；也形容紧张、反应过度敏感']],
 'feel twitchy 感到紧张不安；a twitchy eyelid 容易抽动的眼皮；twitchy about delays 对拖延特别敏感。',
 'a little twitchy；looked twitchy before the interview。',
 'twitchy 常突出小动静就激起反应，fidgety 更突出坐不住、手脚动来动去；日常可重叠，但画面不同。',
 ('He felt twitchy before the interview.','面试前，他紧张得有点一惊一乍。'),('The unexpected noises made the horse twitchy.','突如其来的声响让马变得很不安。'),sources=S('twitchy','twitch'))
W('fidgety','/ˈfɪdʒɪti/','坐立不安的；小动作不断的',
 '坐在椅子上，脚尖敲、手指搓，停不下来，是 fidgety。它比单说 nervous 更能让你看到小动作。',
 'fidget 名词 + -y；更早接 fidge 不安移动的材料，远源、连接路线有不确定性。形容词不必等现代完整 fidget 动词出现后才形成。',
 [['旧 fidge 不安移动材料 → fidget 名词','不安、坐不住，后来常有 the fidgets 用法'],['fidget + -y → fidgety','带坐不住、小动作多的性质']],
 'a fidgety child 坐不住的孩子；get fidgety 变得坐立不安。',
 'feel fidgety；fidgety during a long meeting。',
 'fidgety 可以因紧张，也可以因无聊、等待太久；不能只凭小动作就断言人一定害怕。',
 ('The children grew fidgety during the long speech.','演讲太长，孩子们渐渐坐不住了。'),('I feel fidgety when I have to wait without knowing why.','不知道原因地干等，会让我坐立不安。'),sources=S('fidgety','fidgety'))
W('wiggly','/ˈwɪɡəli/，也读 /ˈwɪɡli/','扭动不停的；弯弯曲曲的',
 '宝宝在怀里动来动去，可以叫 wiggly；随手画的一条左右弯曲线，也像停不住的扭动留下的痕迹，叫 a wiggly line。',
 'wiggle 去 e 加 -y；可按动作名词 wiggle + -y 理解。基础词可能借低地德语、荷兰语相关来回摇动材料，与摇篮旧词有关。',
 [['中古英语 wigelen 等 → wiggle','大概接邻近日耳曼语言摇动材料，英语已有来回小动'],['wiggle 名词 + -y → wiggly','动来动去；或线条多弯、像扭动']],
 'a wiggly baby 扭来扭去的宝宝；a wiggly line 弯弯曲曲的线。',
 'draw a wiggly line；keep the wiggly puppy still。',
 'wiggly 是小幅扭来扭去，wobbly 更像不稳、晃得要倒；线条 wiggly 不一定表示支撑不牢。',
 ('She drew a wiggly line across the page.','她在纸上画了一条弯弯曲曲的线。'),('The wiggly puppy would not stay still for a photograph.','小狗扭来扭去，不肯乖乖待着拍照。'),sources=S('wiggly','wiggly'))
W('wriggly','/ˈrɪɡəli/，也读 /ˈrɪɡli/','扭来扭去的；不断蜿蜒、挣动的',
 '一条虫、一只小动物在手里弯扭着想溜走，叫 wriggly。它常比普通摇晃更突出身体弯转、挣动。',
 'wriggle 去 e 加 -y；w 不发音。基础词接低地德语 wrigglen 等转动材料，与相关扭转词族相连。',
 [['低地德语 wrigglen 等 → wriggle','短促扭转、蜿蜒挣动'],['wriggle + -y → wriggly','有不断扭动、挣动的性质']],
 'a wriggly worm 扭动的虫子；a wriggly toddler 扭来扭去的幼儿。',
 'hold a wriggly puppy；a wriggly creature。',
 'wriggly 与 wiggly 用法可接近，但前者开头读 /r/，后者读 /w/；读音和拼写都要分清，不能当同一个词。',
 ('The wriggly worm slipped out of his hand.','那条扭来扭去的虫子从他手里滑了出去。'),('It was difficult to dress the wriggly toddler.','那个幼儿扭来扭去，很难给他穿衣服。'),sources=S('wriggly','wriggle'))
W('squirmy','英 /ˈskwɜːmi/；美 /ˈskwɝmi/','扭来扭去、难以安坐的',
 '孩子坐着不停扭身体，或小动物在手里挣来挣去，是 squirmy。它写身体不断扭动，不用先替人判断具体情绪原因。',
 'squirm + -y；基底更早来源未定，早期可说鳗鱼等扭动。形容词写容易、不断这样扭动的性质。',
 [['早期方言 squirm','鳗鱼等扭动，来源未定，有拟声等分析'],['squirm + -y → squirmy','扭来扭去、很难保持不动']],
 'a squirmy child 扭来扭去的孩子；a squirmy puppy 不停挣动的小狗。',
 'get squirmy；too squirmy to sit still。',
 'squirmy 与 wriggly 在身体扭动时可接近；squirm 动词还常写难堪得不自在，不能把所有身体动作都倒推成尴尬。',
 ('The squirmy child could not sit still through the story.','那个孩子听故事时扭来扭去，坐不住。'),('She struggled to hold the squirmy puppy.','小狗不断挣动，她很难抱稳。'),sources=S('squirmy','squirm'))
W('jerkily','英 /ˈdʒɜːkɪli/；美 /ˈdʒɝkɪli/','一顿一顿地；突然、断续地',
 '视频不是顺畅播放，而是动一下卡一下，叫 jerkily；车起步也可以一窜一顿地走。画面是不连贯的小猛动。',
 'jerky 形容词的 y 变 i 加 -ly；内层 jerk 动作名词 + -y。这里不接另源的 jerky 肉干。',JERKY+[['jerky + -ly → jerkily','以突然、断续、不平顺的方式运动']],
 'moved jerkily 动作一顿一顿；played jerkily 播放不连贯；nodded jerkily 突兀地连连点头。',
 'started jerkily；turned jerkily。',
 'jerkily 是运动方式不连贯，slowly 是速度慢；画面可以很慢却平顺，也可能快却一顿一顿。',
 ('The old car moved jerkily down the road.','旧车沿路一窜一顿地前进。'),('The video played jerkily on the weak connection.','网络连接不好，视频播放得一卡一卡。'),sources=S('jerkily','jerky'))
W('jerkiness','英 /ˈdʒɜːkinəs/；美 /ˈdʒɝkinəs/','动作断续、不平顺；一顿一顿的性质',
 '把运动里那些突然一窜、一卡的性质整体提出来，叫 jerkiness。常可说车辆动作、动画、视频播放。',
 'jerky 的 y 变 i 加 -ness；内层是动作 jerk + -y，不是肉干名词加性质后缀。',JERKY+[['jerky + -ness → jerkiness','突然断续、不平顺的运动性质']],
 'the jerkiness of the movement 动作的不连贯；reduce jerkiness 减少一顿一顿。',
 'noticeable jerkiness；jerkiness in the animation。',
 'jerkiness 常是动作变化突兀、断续，bumpiness 常是路面凸起等造成颠簸；二者都不平顺，原因、画面却不完全相同。',
 ('The new motor reduced the jerkiness of the movement.','新电机减少了动作一顿一顿的现象。'),('Viewers noticed some jerkiness in the animation.','观众注意到动画有些不连贯。'),sources=S('jerkiness','jerky'))
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_zgr',ROOTS,WORDS)
 extend_lessons()
