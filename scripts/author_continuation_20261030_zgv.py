"""Bobbing, wafting, drifting and eddying, with droopy extensions."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
def S(word,base):
 return ['https://en.wiktionary.org/wiki/'+word+'#English','https://www.etymonline.com/word/'+base]
EXISTING_ROOT_ADDITIONS={
 'B3296':dict(words='rock rocked rocking'.split(),label='rocked：摇动，或使局势受冲击',note='摇动动词承古英语 roccian，岩石名词另路；rocked 的震撼、使不稳常接摇动意象，不用岩石坚硬解释全部。'),
 'B3648':dict(words='bob bobs bobbed bobbing'.split(),label='bob：短促上下动；短发等名词各看旧材料',note='浮动动词接中古英语 bobben，远源未定；短发、短截、团簇等名称历史相互交织，不把所有名词都写成由水面漂浮直接派生。'),
 'A1760':dict(words='waft wafts wafted wafting'.split(),label='waft：由气流等轻轻带来、送走',note='通常联系荷兰语、低地德语守护、护航材料，并可能受摆动词影响；连接细节不是定论。现代先抓被空气、水轻带的动作，不把画面当全部词史。'),
 'B4023':dict(words='drift drifts drifted drifting drifter drifters'.split(),label='drift：顺着外力，逐渐移动、偏离',note='drift 与 drive 的更早日耳曼材料同族，名词的英语近源有继承构词或借入分析；动词由名词发展，漂移、疏远、主题转移各依语境。'),
 'A1741':dict(words='eddy eddies eddied eddying'.split(),label='eddy：流体绕回去打旋',note='eddy 可能联系北欧 iða 与古英语回转、再次的 ed- 等材料，词源分析有差别；不能把现代字尾 y 当作普通形容词后缀，更不能只凭 e、d 猜根。'),
 'A1699':dict(words='droop droopy droopier droopiest'.split(),label='droopy：耷拉、没精神，再比较程度',note='早期 drupie 形容材料可能很古老，有北欧相关分析；现代 droopy 和 droop 的关系透明，比较级、最高级明确按 y 变 i 接完整词尾。'),
 'B2793':dict(words='weather wither withering witheringly'.split(),label='witheringly：像把气势一下晒蔫的讥讽',note='wither 通常联系旧天气、经风吹日晒的词族；withering 的尖刻评价可像让人蔫掉。植物与人物的不同记录都很早，不硬排成现代才有抽象义。'),
}
ROCK=[['古英语 roccian → rock 摇动动词','来回晃动，与岩石名词的近源分开'],['摇动 → 使情绪、局势受强烈冲击','音乐 rock and roll 等又有其具体命名背景，不用石头比喻替代所有历史']]
BOB=[['中古英语 bobben → bob 短促上下动','远源未定；现代可说水面浮动、点头、身体上下移动'],['bobbe 等团簇、短截名词材料','短发、短尾、垂重等名称历史交织，不全从水中浮动义造来']]
WAFT=[['早期 waften 等 → waft','可能借荷兰语、低地德语守护、护航材料，经护航船带行等联系解释，细节不完全确定'],['轻轻带过水、空气 → 自己随气流等飘来、飘走','也可能受 wave 相关摆动形式影响；名词后来写一阵气味、气流']]
DRIFT=[['与 drive 同族的旧日耳曼被驱动材料 → drift 名词','英语近源有自身构词或北欧、荷兰语借入等分析，不能机械 drive 加 t'],['drift 名词 → 动词顺流漂移','可渐渐偏离、疏远、没目标地生活；名词还可写堆积与话的意图']]
EDDY=[['苏格兰 ydy 等 → eddy 名词','可能联系古诺斯 iða、古英语回转等材料，不同来源分析不宜硬定一个现代拆法'],['涡流名词 → eddy 动词','液体、空气局部绕回打旋，不是所有顺流移动都叫 eddy']]
DROOPY=[['早期 drupie 等低落材料；与 droop 同族的关系可比较','近源分析有差别，不能说形容词一定由现代动词才首次造出'],['现代 droopy：耷拉、蔫软 → 比较形式','学习可按 droop + -y 理解；比较时 y 变 i 接 -er、-est']]
WITHER=[['中古英语 widderen、wederen 等 → wither','通常联系经风吹日晒、干枯、失活材料，形式逐步分化'],['withering 的尖刻、使难堪义 → witheringly','像让人气势蔫掉；人物比喻很早，不写成现代才从植物发明']]
W('rocked','英 /rɒkt/；美 /rɑkt/','摇动、使震动了；震撼、使动荡了；表现出色了〔口语〕',
 '轻摇婴儿入睡，是 rocked；丑闻把机构原来的稳定摇得不稳，也是 rocked。口语里说 someone rocked a role，又可能夸表现很出色。',
 'rock + 完整 -ed，/k/ 后读 /t/；摇动动词承古英语 roccian，与岩石名词的近源分开。',ROCK+[['rock + -ed → rocked','过去来回摇动，或使某种稳定受强烈冲击']],
 'rocked the baby to sleep 摇着哄睡；rocked by scandal 被丑闻震动。',
 'rocked the boat 摇船，也可比喻搅乱局面；rocked the stage 口语夸舞台表现出色。',
 'rocked by the news 说明受到强烈冲击，不保证后来倒下；destroyed 才明确毁掉，程度结果不能自动补进去。',
 ('She gently rocked the baby to sleep.','她轻轻摇着婴儿，哄他入睡。'),('The company was rocked by the sudden resignation.','突如其来的辞职让公司受到很大震动。'),sources=S('rocked','rock'))
W('bobs','英 /bɒbz/；美 /bɑbz/','上下轻动、点头〔第三人称单数〕；短发、垂重等〔复数〕',
 '浮标在水面一上一下，是 bobs；理发店里几款齐短发也可叫 bobs。短促上下动作和短截名词不能只用一条来源解释。',
 'bob + -s，/b/ 后读 /z/；动词三单和名词复数同形。不同旧形的关系有交织，远源未定。',BOB+[['bob + -s → bobs','它上下轻动；多款短发、多个垂重等']],
 'bobs on the water 在水面上下浮动；bobs his head 轻点头；short bobs 齐短发。',
 'bobs up and down；models with bobs 留齐短发的模特。',
 'bobs 上下浮动，drifts 更侧重顺水、气流等平移；一个浮标可以一边上下动一边被带走，动作可同时发生。',
 ('The red float bobs on the water.','红浮标在水面一上一下。'),('Several models wore short bobs.','几位模特都留着齐短发。'),sources=S('bobs','bob'))
W('bobbed','英 /bɒbd/；美 /bɑbd/','上下轻动、点头了；剪成齐短发的',
 '小船一上一下，是 bobbed；a bobbed haircut 则是齐短发造型，形容头发剪短后的外观。两种用法不要只按浮动联想硬合。',
 'bob 双写 b 加完整 -ed，读 /d/；上下动动词与短截、剪短发支线共用现代变化。',BOB+[['bob + -ed → bobbed','过去上下动；也写短发经剪短后的样子']],
 'bobbed on the waves 在浪中起伏；bobbed his head 点了点头；bobbed hair 齐短发。',
 'a bobbed hairstyle；bobbed out of sight 上下起伏着消失。',
 'bobbed hair 是剪成某种短发型，bobbing hair 可以是在动；不要只见 bob 就忽略后面的状态、过程词尾。',
 ('The little boat bobbed on the waves.','小船在波浪中一上一下。'),('She wore her hair in a neat, bobbed style.','她留着整齐的齐短发。'),sources=S('bobbed','bob'))
W('bobbing','英 /ˈbɒbɪŋ/；美 /ˈbɑbɪŋ/','正在上下轻动、浮沉；点头',
 '水上漂着的东西不断一上一下，像有个小弹簧，是 bobbing。它常是短促、重复的上下移动。',
 'bob 双写 b 加 -ing；规则动作形式，不因原词短就省掉双写。',BOB+[['bob + -ing → bobbing','上下轻动、点头的过程正在发生']],
 'bobbing up and down 一上一下；heads bobbing 人头上下动；bobbing on the surface 在表面浮动。',
 'bobbing in the crowd 在人群中上下起伏；apple bobbing 捞苹果游戏。',
 'bobbing 通常上下动，swaying 多来回侧摆；两种都摇，方向和姿态却不同。',
 ('We could see heads bobbing above the crowd.','我们能看见人群上方一上一下的人头。'),('The bottle was bobbing on the surface of the river.','瓶子正在河面一上一下地浮动。'),sources=S('bobbing','bob'))
W('waft','英 /wɒft/、/wɑːft/；美 /wɑft/、/wæft/','轻轻飘送、飘来；一阵气味、气流',
 '厨房香味随风慢慢飘来，或音乐隔着窗轻轻传过来，都可以 waft。它有被空气、水等柔和带着走的感觉。',
 '早期 waften 等通常联系荷兰语、低地德语守护、护航材料，也可能受 wave 相关摆动形式影响；连接细节未全定。现代动词可及物飘送，也可不及物飘来，名词写一阵气味等。',WAFT,
 'waft through the window 飘过窗户；a waft of perfume 一阵香水味；waft smoke away 轻轻把烟扇走。',
 'waft on the breeze 随微风飘动；music wafts from a room 音乐从房间轻轻传来。',
 'waft 常像气味、烟、声音被柔和带来，blast 则可能是强烈冲击或轰响；两种传来方式的力度不同。',
 ('Warm smells of bread began to waft from the kitchen.','温热的面包香开始从厨房飘来。'),('A waft of perfume followed her into the room.','她走进房间时，身后带来一阵香水味。'),sources=S('waft','waft'))
W('wafts','英 /wɒfts/、/wɑːfts/；美 /wɑfts/、/wæfts/','轻轻飘送、飘来〔第三人称单数〕；阵阵气味、气流〔复数〕',
 '咖啡香从门缝飘过，是 the smell wafts through；一阵阵气味，则可用名词 wafts。两者都很适合写空气轻带过的东西。',
 'waft + -s，/t/ 后读 /s/，结尾为 /fts/；动词三单和名词复数同形。',WAFT+[['waft + -s → wafts','它轻轻飘来；一阵阵气味、气流']],
 'wafts of smoke 阵阵烟气；music wafts through the hall 音乐在大厅里轻轻传来。',
 'wafts from the bakery；faint wafts of perfume 淡淡的阵阵香水味。',
 'wafts of smoke 是断续飘来的烟气，a thick cloud of smoke 可以是一大片浓烟；都叫烟，却在形态、浓度上不同。',
 ('The smell of coffee wafts through the open door.','咖啡香从敞开的门里飘来。'),('Faint wafts of smoke rose from the dying fire.','渐熄的火堆升起淡淡的阵阵烟气。'),sources=S('wafts','waft'))
W('wafted','英 /ˈwɒftɪd/、/ˈwɑːftɪd/；美 /ˈwɑftɪd/、/ˈwæftɪd/','轻轻飘来了、飘送了',
 '气味、烟、音乐过去随风轻轻来到，是 wafted；也可说有人把香味、烟轻扇过去。不是所有飘动都大幅翻滚。',
 'waft + 完整 -ed，/t/ 后读 /ɪd/，多出一个音节；基础词的守护、护航材料联系仍保留不确定性。',WAFT+[['waft + -ed → wafted','过去轻轻被带来、带走或飘送']],
 'wafted through the room 飘过房间；wafted from the garden 从花园飘来。',
 'a smell wafted in 气味飘进来；wafted on the air 随空气飘动。',
 'wafted music 常像远处随风传来的轻柔声音，blared music 是高声响起；不要都只译成播放而丢掉距离、力度。',
 ('The scent of jasmine wafted through the window.','茉莉香从窗外飘了进来。'),('Music wafted across the courtyard.','音乐轻轻传过庭院。'),sources=S('wafted','waft'))
W('wafting','英 /ˈwɒftɪŋ/、/ˈwɑːftɪŋ/；美 /ˈwɑftɪŋ/、/ˈwæftɪŋ/','正在轻轻飘送、飘来',
 '烟一缕缕被风轻带着走，或面包香正在空气里散过来，是 wafting。常用来营造柔和的环境感受。',
 'waft + -ing；规则动作形式，写被空气、水等带动的过程，也可写轻轻扇送。',WAFT+[['waft + -ing → wafting','轻柔飘动、飘送正在发生']],
 'smoke wafting upwards 烟轻轻向上飘；smells wafting from the oven 从烤箱飘出的香味。',
 'wafting through the trees；music wafting from an open window。',
 'wafting 常突出柔和带过，swirling 更突出打旋；一缕烟可以同时轻飘又绕圈，但两词各强调一侧。',
 ('The smell of bread was wafting from the oven.','面包香正从烤箱飘出来。'),('Thin smoke was wafting through the trees.','薄烟正在树间轻轻飘动。'),sources=S('wafting','waft'))
W('drifts','/drɪfts/','漂移、渐渐转向〔第三人称单数〕；堆积、趋势等〔复数〕',
 '船没主动划，也被水慢慢带走，是 drifts；雪被风推到一起，堆成一处处，是 drifts of snow。都有被外力带动的旧核心。',
 'drift + -s，/t/ 后读 /s/；名词复数和动词三单同形。drift 与 drive 同族，英语名词的近源有构词或借入的不同分析。',DRIFT+[['drift + -s → drifts','它逐渐漂移；多堆被风等带拢的雪等']],
 'drifts out to sea 漂向海上；drifts away 渐渐远离；drifts of snow 风积雪堆。',
 'attention drifts 注意力渐渐飘走；snow drifts 积雪堆。',
 'drifts 写被带着逐渐移动，steers 写主动控制方向；船可以漂移，掌舵者也可以试着修正，动作主体别混。',
 ('The empty boat drifts towards the far bank.','空船正慢慢漂向对岸。'),('Deep drifts of snow blocked the lane.','厚厚的风积雪堆堵住了小路。'),sources=S('drifts','drift'))
W('drifted','/ˈdrɪftɪd/','漂移了；渐渐疏远、转向了；迷糊睡去了',
 '一段关系没有大吵，却不再那么近，是 drifted apart；人躺着，意识慢慢飘开、睡过去，是 drifted off。不同搭配都抓住渐渐、不由强力控制的变化。',
 'drift + 完整 -ed，/t/ 后读 /ɪd/；名词发展出的漂移动词，再有关系、注意力等比喻。',DRIFT+[['drift + -ed → drifted','过去顺外力移动，或状态渐渐转开']],
 'drifted apart 渐渐疏远；drifted off to sleep 迷迷糊糊睡去；drifted ashore 漂到岸边。',
 'conversation drifted to another topic 谈话渐渐转向另一话题；drifted away。',
 'drifted apart 常无一个明确决裂时刻，broke off the friendship 则更主动、明确地断交；结果都远离，过程不同。',
 ('We drifted apart after leaving university.','大学毕业后，我们渐渐疏远了。'),('She drifted off to sleep while listening to the rain.','听着雨声，她迷迷糊糊睡着了。'),sources=S('drifted','drift'))
W('drifting','/ˈdrɪftɪŋ/','正在漂移、渐渐转向；漂流；赛车漂移〔语境义〕',
 '没牢牢把住方向，就随外力慢慢偏开，是 drifting；人生、谈话、注意力也可以这样飘。赛车的 drifting 则是有意控制车辆侧滑，不能都说成毫无控制。',
 'drift + -ing；动作形式、行为名词。赛车义是后来特定运动用法，在本来被带动的词族上专业化。',DRIFT+[['drift + -ing → drifting','漂移、渐变的过程；具体领域可有控制侧滑的专义']],
 'drifting clouds 漂动的云；drifting apart 渐渐疏远；drifting off 渐渐睡去或走神。',
 'drifting through life 漫无目标地过日子；competitive drifting 赛车漂移比赛。',
 'drifting through life 往往评价缺少方向，drifting in motorsport 却可以很有技巧；领域搭配不能只按一个中文核心硬套。',
 ('We watched clouds drifting across the sky.','我们看着云慢慢漂过天空。'),('I noticed my attention drifting during the long meeting.','长会中，我发现自己的注意力正在飘走。'),sources=S('drifting','drift'))
W('drifters','英 /ˈdrɪftəz/；美 /ˈdrɪftərz/','漂泊、无固定方向的人〔复数〕；漂流物、漂移用具等〔依语境〕',
 '从一个地方、一份临时活转到下一处，很少定下来，这些人可能叫 drifters。人物描写里像顺着生活外力漂，不是计划清楚的旅行者。',
 'drift + -er → drifter，再加 -s，读 /z/；-er 命名漂泊的人，也能在专门语境里命名漂流、漂移对象或器具。',DRIFT+[['drift → drifter → drifters','多个随处漂泊、缺固定方向的人等']],
 'a group of drifters 一群漂泊者；drifters passing through town 经过镇子的漂泊者。',
 'young drifters；seasonal drifters 辗转做季节工的人。',
 'travellers 只说旅行者，drifters 更常带未安定、缺固定方向的描写；不是所有到处走的人都适合后者。',
 ('The town attracted drifters looking for temporary work.','镇子吸引了寻找临时工作的漂泊者。'),('The novel follows two young drifters crossing the country.','小说讲两个年轻漂泊者横穿全国的经历。'),sources=S('drifters','drift'))
W('eddy','/ˈedi/','涡流；打旋、回旋',
 '大股水往前，石头旁一小块水却绕回去兜圈，那就是 an eddy。空气也能局部回旋；动词 eddy 写这种绕圈过程。',
 '接苏格兰 ydy 等，可能与古诺斯 iða、古英语 ed- 再次、回转等旧材料有关；现代动词由涡流名词发展，不能从结尾 y 就当形容词。',EDDY,
 'an eddy in the river 河中涡流；leaves eddy in the wind 叶子随风打旋。',
 'a small eddy；eddy around a rock 绕石头回旋。',
 'eddy 着重局部绕回、旋转，drift 着重随外力逐渐移走；水里一片叶子可以被带进涡流，既漂又转。',
 ('A small eddy formed behind the rock.','石头后面形成了一小股涡流。'),('Dry leaves began to eddy around the doorway.','干叶开始在门口打旋。'),sources=S('eddy','eddy'))
W('eddies','/ˈediz/','涡流〔复数〕；打旋、回旋〔第三人称单数〕',
 '石头后有一处处小回旋水，是 eddies；烟在角落绕圈不散，动词也可说 eddies。',
 'eddy 的 y 变 i 加 -es；名词复数和动词三单同形，读 /z/ 结尾。',EDDY+[['eddy → eddies','多个局部回旋流；它打旋']],
 'small eddies 小涡流；eddies in the current 水流里的局部回旋。',
 'smoke eddies around the ceiling 烟在天花板附近打旋；eddies behind rocks 石后涡流。',
 'eddies 不一定巨大，whirlpool 常让人想到较明显、集中的水旋；不能所有小涡流都夸成吞船的大旋涡。',
 ('Foam collected in little eddies beside the bank.','泡沫聚在岸边一股股小涡流里。'),('Smoke eddies beneath the low ceiling.','烟在低矮的天花板下打旋。'),sources=S('eddies','eddy'))
W('eddied','/ˈedid/','打旋、回旋了',
 '风把落叶卷到门边，一阵阵绕圈，过去发生了就是 eddied。不是沿一条直线飘过，而是局部折回来转。',
 'eddy 的 y 变 i 加完整 -ed，词尾读 /d/；前面的 /i/ 来自基底末尾，不是额外插入的 /ɪd/。',EDDY+[['eddy → eddied','过去发生局部回旋、打旋']],
 'eddied around the corner 在角落打旋；eddied behind the rock 在石后回旋。',
 'leaves eddied in the wind；smoke eddied upwards 烟回旋而上。',
 'eddied 可以边回旋边往上、往前，并非绝对固定在一个点；关键是流动含局部绕回的旋转。',
 ('Leaves eddied around our feet.','落叶在我们脚边打旋。'),('The stream eddied behind the fallen branch.','溪水在倒下的树枝后回旋。'),sources=S('eddied','eddy'))
W('eddying','/ˈediɪŋ/','正在打旋、回旋的',
 '水、烟、叶子正在局部绕回兜圈，叫 eddying；写出它不只是移动，还带旋转的路径。',
 'eddy + -ing，保留 y → eddying；和 eddies、eddied 的变 y 为 i 分开。',EDDY+[['eddy + -ing → eddying','回旋流动的过程正在发生']],
 'eddying water 回旋的水；eddying leaves 打旋的叶子。',
 'smoke eddying above the fire；eddying around a pillar。',
 'eddying 写旋转路径，wafting 写轻柔地被气流等带动；同一缕烟可能两者兼有，词的关注点不同。',
 ('We watched smoke eddying above the fire.','我们看着烟在火堆上方回旋。'),('The boat turned slowly in the eddying water.','小船在回旋的水里缓缓转动。'),sources=S('eddying','eddy'))
W('droopier','英 /ˈdruːpiə/；美 /ˈdruːpiər/','更耷拉、蔫软的；更没精神的',
 '叶片比昨天更垂下来，小狗耳朵也耷得更低，都可以 droopier；人的表情更蔫，也能借这个外形说。',
 'droopy 的 y 变 i 加完整 -er；现代可按 droop + -y 理解，但早期 drupie 形容词很古老，不能把历史只写成现代动词现造。',DROOPY+[['droopy → droopier','更下垂、没精神；比较性质程度']],
 'droopier leaves 更耷拉的叶子；a droopier expression 更没精神的表情。',
 'ears looked droopier；droopier than before。',
 'droopier 讲向下垂、缺精神的姿态，smaller 只说大小；垂得更低不等于体积更小。',
 ('The plant looked droopier after a day in the hot sun.','在烈日下晒了一天，植物显得更蔫了。'),('The dog’s ears looked even droopier when he was tired.','那只狗累了时，耳朵显得耷拉得更低。'),sources=S('droopier','droopy'))
W('droopiest','/ˈdruːpiɪst/','最耷拉、蔫软的；最没精神的',
 '几株花里，垂得最低、最显得没精神的，是 the droopiest；比较人或动物的表情、耳朵，也用同样的性质。',
 'droopy 的 y 变 i 加完整 -est；形容词最高级，内层词源仍保留早期 drupie 等分析。',DROOPY+[['droopy → droopiest','所比范围内下垂、蔫软程度最高']],
 'the droopiest plant 最蔫的植物；the droopiest ears 最耷拉的耳朵。',
 'the droopiest flowers；the droopiest expression。',
 'droopiest flowers 是外形最蔫，不等于一定 dead 已死；外观姿态和生命状态不能自动画等号。',
 ('We moved the droopiest plant into the shade.','我们把最蔫的那株植物搬到阴凉处。'),('The puppy had the droopiest ears of the litter.','那只小狗的耳朵是同窝里最耷拉的。'),sources=S('droopiest','droopy'))
W('witheringly','/ˈwɪðərɪŋli/','尖刻地；带让人难堪、气势蔫掉的意味地',
 '一句讥讽轻轻扔来，却让对方像叶子一下蔫掉、接不上话，这种口气是 witheringly。核心是言语里的严厉轻蔑、杀伤力。',
 'withering + -ly；内层 wither + -ing。wither 通常联系经天气、干枯失活的旧材料，人物比喻很早；现代副词多写尖刻的方式。',WITHER+[['withering + -ly → witheringly','以让人难堪、气势受挫的尖刻方式']],
 'said witheringly 尖刻地说；looked witheringly at someone 用轻蔑、让人难堪的目光看某人。',
 'witheringly dismissive 轻蔑否定得让人下不来台；replied witheringly。',
 'witheringly 比 coldly 更明确带使人难堪的尖刻；coldly 可以只是冷淡、疏离，不一定有一句话把气势打蔫的效果。',
 ('“You call that a plan?” she asked witheringly.','“你管那叫计划？”她尖刻地问。'),('He was witheringly dismissive of their explanation.','他尖刻地把他们的解释一口否定，让人很难堪。'),sources=S('witheringly','wither'))
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_zgv',ROOTS,WORDS)
 extend_lessons()
