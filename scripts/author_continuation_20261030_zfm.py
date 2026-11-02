"""Wobbling, twisting, changing course and tipping over."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
def S(word,base):
 return ['https://en.wiktionary.org/wiki/'+word+'#English','https://www.etymonline.com/word/'+base]
EXISTING_ROOT_ADDITIONS={
 'A2238':dict(words='wobble wobbles wobbled wobbling wiggle wiggles wiggled wiggling topple topples toppled toppling'.split(),label='wobble、wiggle、topple 的旧动作材料与现代变化',note='wobble、wiggle 各接日耳曼反复摆动材料；topple 联系 top 的倾倒旧动词和 -le。现代 -ed、-ing 接已固定整词，不能对所有 ble、gle 都找一个现成英语基词。'),
 'A1699':dict(words=['wobble','wobbly'],label='wobbly：从摇晃到不稳的性质',note='wobble 去末尾 e + 完整 -y → wobbly，形容物体松晃、腿脚不稳，也可形容信心动摇。'),
 'B2584':dict(words='weave wobble wobbles wobbled wobbling wobbly'.split(),label='wobble 与 weave 的可能远源联系',note='wobble 可能由低地德语 wabbeln 等借入，更远有与 weave 的来回动作材料联系的分析，保留不确定性，不当作现代 weave 直接构词。'),
 'B4505':dict(words='tilt tilts tilted tilting'.split(),label='tilt：从不稳到倾斜、偏向',note='tilt 较早接中古英语倒下、使倒下材料，可能上溯古英语不稳词族；现代 tilts、tilted、tilting 把倾斜、偏向分开讲。'),
 'B3469':dict(words='top topple topples toppled toppling'.split(),label='topple：顶端失衡而倾倒',note='top 的旧倾倒动作加 -le 一系形成 topple，现代整词可说物体倒下、使倒下，也可说推翻权力。此 top 不是希腊 top- 地点。'),
 'A1760':dict(words='totter totters tottered tottering wobble wobbles wobbled wobbling wiggle wiggles wiggled wiggling writhe writhes writhed writhing swerve swerves swerved swerving veer veers veered veering tilt tilts tilted tilting topple topples toppled toppling'.split(),label='摇摆、扭转、偏转与倾倒的词形',note='writhed 的 -ed 读 /d/，结尾为 /ðd/；tilted 读 /ɪd/。writhe、swerve 等去不发音 e 后再接完整 -ed、-ing。'),
}
TOTTER=[['中古英语 toteren → totter','较早说来回摆动；可能接北欧不稳材料，最远来源未定'],['基座上摇晃 → 站走不稳；制度等摇摇欲坠','现代常把立不稳的画面借给支撑薄弱的抽象事物']]
W('totter','英 /ˈtɒtə/；美 /ˈtɑːtər/','摇摇晃晃地站、走；摇摇欲坠',
 '刚学走路的小孩，两步就要找平衡；一张松了腿的桌子，碰一下就晃，都像 totter。一个快撑不住的组织也可这样说。',
 '承中古英语 toteren 的来回摆动义，可能有北欧来源；旧形式像反复动作词，但更早基础未定，不把现代 tot 小孩硬当它的来源。',TOTTER,
 'totter across the room 是晃晃悠悠走过房间，totter on the brink 是在边缘摇摇欲坠；可以写人、物体或局面。',
 'totter on weak legs 腿无力地晃着走；a regime begins to totter 一个政权开始摇摇欲坠。',
 'totter 重点是支撑不足、摇晃不稳，stroll 是从容散步；描述小孩时，totter 并不自动说明出了什么问题。',
 ('The toddler began to totter towards her father.','小宝宝开始摇摇晃晃地朝爸爸走去。'),('The old tower seemed ready to totter in the wind.','旧塔在风里看起来摇摇欲坠。'),sources=S('totter','totter'))
W('totters','英 /ˈtɒtəz/；美 /ˈtɑːtərz/','摇晃着站走、摇摇欲坠〔第三人称单数〕；摇晃动作〔复数〕',
 '一个人腿脚还没稳住，走起来东摇西晃，是 totters；一座塔或一套制度也可能像站不稳的人一样晃。',
 'totter + -s，读 /z/；常用作动词三单，动作名词复数也同形。原来的双 t 属于基础词。',TOTTER+[['totter + -s → totters','他、她摇晃着走；它立不稳']],
 'totters towards someone 是摇晃着走向某人，totters on its base 是在基座上晃；常接方向或支撑处。',
 'totters across the floor 晃晃悠悠走过地板；totters on the edge 在边缘摇晃。',
 'totters 更强调身体或支撑的摇晃，trips 是被绊、失脚；不稳走路未必已经绊到了东西。',
 ('He totters across the rug with his arms held out.','他伸着胳膊，摇摇晃晃走过地毯。'),('The old garden ornament totters on its narrow base.','那件旧花园摆饰在窄底座上晃晃悠悠。'),sources=S('totters','totter'))
W('tottered','英 /ˈtɒtəd/；美 /ˈtɑːtərd/','摇晃着站走了；摇摇欲坠了',
 '刚才一边挪步一边找平衡，或重重一摞东西晃了几下，是 tottered。说的是摇晃过程，不强迫最后倒下。',
 'totter + 完整 -ed，读 /d/；词尾接在 /tə/ 或 /tər/ 后，整词通常仍是两个音节。',TOTTER+[['totter + -ed → tottered','过去晃着走、立不稳']],
 'tottered to the chair 是晃着挪到椅旁，tottered and fell 是先晃再倒；是否跌落由后半句补清。',
 'tottered backwards 晃着往后退；tottered for a moment 摇晃了一会儿。',
 'tottered 与 teetered 都可不稳，tottered 更常见于摇晃步态或支撑虚弱，teetered 常突出在边缘将倒未倒。',
 ('He tottered to the chair after standing up too quickly.','他起身太快，摇摇晃晃挪到椅子旁。'),('The stack tottered, but she caught it in time.','那摞东西晃了晃，但她及时扶住了。'),sources=S('tottered','totter'))
W('tottering','英 /ˈtɒtərɪŋ/；美 /ˈtɑːtərɪŋ/','正在摇晃着站走；摇摇欲坠的、岌岌可危的',
 '小孩正晃着脚步走，或一座高书堆失去稳定，是 tottering；抽象局面也能像那堆书一样快撑不住。',
 'totter + 完整 -ing，直接加；分词可描写移动过程，也可前置修饰支撑不稳的东西。',TOTTER+[['totter + -ing → tottering','摇晃过程；失去稳定的状态']],
 'a tottering pile 是摇摇欲坠的一堆，tottering towards the door 是晃着走向门；a tottering empire 是岌岌可危的帝国。',
 'tottering steps 摇晃的脚步；tottering on the brink 在边缘摇摇欲坠。',
 'tottering 可把物体、组织都画成立不住的形状；old 只说年代久，老东西不一定处在摇摇欲坠的状态。',
 ('We watched the child tottering across the lawn.','我们看着孩子摇摇晃晃走过草坪。'),('A tottering pile of books filled the corner of the desk.','桌角堆着一摞摇摇欲坠的书。'),sources=S('tottering','totter'))
WOBBLE=[['较早 wabble → 现代 wobble','可能借低地德语 wabbeln；更远来回摆材料或与 weave 有关'],['不稳定地来回晃 → 信心、决定不稳','现代常从桌腿、车轮的松晃，借到人心里没那么笃定']]
W('wobble','英 /ˈwɒbəl/；美 /ˈwɑːbəl/','摇晃、晃动；动摇；摇晃、不稳的一下',
 '桌腿长短不齐，手一压，桌面就来回晃，是 wobble。骑车还找不准平衡，或原来很有信心却开始犹豫，也像这样不稳。',
 '较早写作 wabble，可能借低地德语 wabbeln；更远有与 weave 来回动作材料相关的分析，仍不确定。现代是完整基础词。',WOBBLE,
 'the wheel wobbles 是车轮晃动，confidence begins to wobble 是信心开始动摇；a slight wobble 是轻轻一晃或短暂不稳。',
 'wobble from side to side 左右晃；have a wobble 一度有点不稳、动摇。',
 'wobble 常是支撑、转动不均造成的晃，sway 可是平顺有节奏的摆；桌子 wobble 时往往让人想把它垫稳。',
 ('The table began to wobble when I leaned on it.','我往桌上一靠，桌子就开始晃。'),('Her confidence started to wobble after the first setback.','第一次受挫后，她的信心开始动摇。'),sources=S('wobble','wobble'))
W('wobbles','英 /ˈwɒbəlz/；美 /ˈwɑːbəlz/','摇晃、动摇〔第三人称单数〕；晃动、不稳时刻〔复数〕',
 '一张桌子压上去会晃，叫 wobbles；几次差点失去平衡或信心不稳，也可当作一下一下的 wobbles。',
 'wobble + -s，/l/ 后读 /z/；动词三单和摇晃名词复数同形，末尾 e 保留。',WOBBLE+[['wobble + -s → wobbles','它晃动；几次不稳、动摇']],
 'the chair wobbles 是椅子晃，a few wobbles 是几下不稳；也可在表现、决定等语境里作比喻。',
 'wobbles on uneven ground 在不平地面上晃；early wobbles 初期几次不稳。',
 'wobbles 往往是小幅、反复地不稳，topples 则是失衡倒下；晃动与倒下可以前后发生，却不是同一结果。',
 ('The front wheel wobbles when the bicycle speeds up.','自行车加速时，前轮会晃。'),('After a few wobbles, she managed to ride in a straight line.','晃了几下之后，她终于能骑成直线了。'),sources=S('wobbles','wobble'))
W('wobbled','英 /ˈwɒbəld/；美 /ˈwɑːbəld/','摇晃了；一度不稳、动摇了',
 '刚才人、物体左右晃了几下，或下定的决心一时没那么稳，是 wobbled。它能写一次具体晃动，也能写状态短暂松动。',
 'wobble 去末尾 e + 完整 -ed → wobbled，/l/ 后读 /d/；原有双 b 保留。',WOBBLE+[['wobble 去 e + -ed → wobbled','过去晃动；信心等出现不稳']],
 'wobbled on the stool 是在凳上晃，her voice wobbled 是声音不稳、颤了一下；decisions wobbled 则沿犹豫分支理解。',
 'wobbled slightly 轻轻晃动；wobbled but stayed upright 晃了却没倒。',
 'wobbled 并不保证散架、跌落，collapsed 才把塌下的结果说出来；这个词常留着重新稳住的余地。',
 ('The stool wobbled as he climbed onto it.','他爬上凳子时，凳子晃了晃。'),('Her voice wobbled as she thanked the team.','她向团队致谢时，声音有些发颤。'),sources=S('wobbled','wobble'))
W('wobbling','英 /ˈwɒbəlɪŋ/；美 /ˈwɑːbəlɪŋ/','正在摇晃、晃动、动摇；不稳定地晃着的',
 '车轮不是稳稳转，而是边转边偏晃，是 wobbling；腿一时不稳、晃着找平衡，也能这样说。',
 'wobble 去末尾 e + 完整 -ing → wobbling；动词过程和前置分词都保留来回不稳的感觉。',WOBBLE+[['wobble 去 e + -ing → wobbling','不稳定地晃动的过程']],
 'a wobbling wheel 是晃动的车轮，wobbling on one leg 是单腿站得晃；也能描述信心、决心逐渐不稳。',
 'wobbling from side to side 左右晃动；keep it from wobbling 扶住不让它晃。',
 'wobbling 是过程，wobbly 是性质、状态；a wobbling table 正在晃，a wobbly table 可能此刻没动，但一碰就晃。',
 ('The wheel was wobbling as it turned.','轮子转动时正在晃。'),('He stood wobbling on one leg while he put on his shoe.','他单腿晃着站，想把鞋穿上。'),sources=S('wobbling','wobble'))
W('wobbly','英 /ˈwɒbli/；美 /ˈwɑːbli/','摇晃不稳的；腿软的；不坚定、动摇的',
 '一把椅子坐上去就晃，一双腿累得站不稳，都是 wobbly。计划、信心不够牢，也像底座没垫稳。',
 'wobble 去末尾 e + 完整 -y → wobbly，形容有晃动、不稳的性质；不是 wobble 再加表示方式的 -ly。',WOBBLE+[['wobble 去 e + -y → wobbly','容易晃、不够稳的性质']],
 'a wobbly chair 是松晃的椅子，wobbly legs 是发软不稳的腿，feel wobbly 可说身体虚晃，也可说情绪、决心没底。',
 'a wobbly table leg 松晃的桌腿；a bit wobbly 有点不稳。',
 'wobbly 的结尾像 -ly，却是 wobble 变化后的形容词；要说“摇晃着走”，常直接用 wobble 或 walk unsteadily。',
 ('We put folded paper under the wobbly table leg.','我们把折好的纸垫在松晃的桌腿下面。'),('My legs felt wobbly after the long climb.','爬了很久之后，我觉得双腿发软、站不太稳。'),sources=S('wobbly','wobble'))
WIGGLE=[['中古英语 wigelen，可能借德荷相关摇摆形式 → wiggle','相关旧词与摇篮、来回摇动材料相连'],['小幅来回晃动 → 活动空间、变通余地','wiggle room 像身体在狭窄处还能挪动一点的空间']]
W('wiggle','/ˈwɪɡəl/','扭动、摆动、轻轻摇动；小幅扭摆',
 '脚趾活动几下、耳朵动几下、卡住的钥匙来回晃一晃，都可 wiggle。画面通常是幅度不大的来回动。',
 '中古英语 wigelen 可能借自荷兰语、低地德语一类反复摇动形式，关联旧摇篮、摇摆材料；现代变化接已经固定的 wiggle。',WIGGLE,
 'wiggle your toes 是动动脚趾，wiggle the key 是晃晃钥匙；wiggle room 是尚有变通、调整余地。',
 'give it a wiggle 把它晃一晃；room to wiggle 能挪动的小空间。',
 'wiggle 常是小幅来回晃，wriggle 更像身体扭着挤动；两词有重叠，不能一律按有无字母 r 判动作大小。',
 ('Try to wiggle the key gently in the lock.','试着在锁里轻轻晃动钥匙。'),('The schedule still gives us a little wiggle room.','这份时间表还给我们留了一点调整余地。'),sources=S('wiggle','wiggle'))
W('wiggles','/ˈwɪɡəlz/','扭摆、晃动〔第三人称单数〕；小幅扭摆动作〔复数〕',
 '人把手指、耳朵或脚趾来回动几下，动词三单用 wiggles；几下小扭摆也能叫 a few wiggles。',
 'wiggle + -s，/l/ 后读 /z/；整个基础词直接接三单或名词复数，双 g 原本就有。',WIGGLE+[['wiggle + -s → wiggles','他、她轻轻晃动；几下小摆动']],
 'wiggles his toes 是动脚趾，wiggles the handle 是轻晃把手；the wiggles of a worm 是虫子的扭动。',
 'wiggles free 扭摆着脱身；a few wiggles 几下轻晃。',
 'wiggles 可带被晃动的小东西作宾语，也可由身体本身作主语；小动作不一定是在挣扎、难受。',
 ('He wiggles his ears to make the children laugh.','他动耳朵逗孩子们笑。'),('The puppy wiggles with excitement when we come home.','我们回家时，小狗兴奋得扭来扭去。'),sources=S('wiggles','wiggle'))
W('wiggled','/ˈwɪɡəld/','扭摆、晃动了；晃着挪动、脱开了',
 '刚才把把手轻轻摇了几下，或让脚趾动起来，是 wiggled。东西卡住时，往往通过这种小幅来回动来松开。',
 'wiggle 去末尾 e + 完整 -ed → wiggled，/l/ 后读 /d/；双 g 保留，读音不额外延长。',WIGGLE+[['wiggle 去 e + -ed → wiggled','过去作小幅扭摆、晃动']],
 'wiggled her fingers 是晃动手指，wiggled it loose 是把它来回晃松；结果 loose、free 可接在后面补出。',
 'wiggled the handle 晃了晃把手；wiggled out of the narrow space 扭摆着挤出窄处。',
 'wiggled 的小幅晃动常用于试着松开，pulled 则是朝一个方向拉；两种动作可先后连用，却关注不同。',
 ('She wiggled the handle until the drawer opened.','她来回晃了晃把手，直到抽屉打开。'),('He wiggled his toes inside his new shoes.','他在新鞋里动了动脚趾。'),sources=S('wiggled','wiggle'))
W('wiggling','/ˈwɪɡəlɪŋ/','正在扭摆、轻晃；小幅来回动的',
 '脚趾、手指或身体正轻轻来回动，是 wiggling。像把卡住的小东西一点点晃松，而不是整个人大幅翻滚。',
 'wiggle 去末尾 e + 完整 -ing → wiggling；分词描写小幅、反复动作，也可作动作名词。',WIGGLE+[['wiggle 去 e + -ing → wiggling','轻晃、小幅扭摆的过程']],
 'wiggling her toes 是动着脚趾，wiggling the plug loose 是来回晃着把插头弄松；常用于局部、小幅动作。',
 'a wiggling puppy 扭来扭去的小狗；stop wiggling 别动来动去。',
 'wiggling 可以是轻松、好玩的晃动，writhing 常带强烈不适、痛苦或挣扎；两者动作感觉、语气轻重不同。',
 ('The baby lay on the mat, wiggling her toes.','宝宝躺在垫子上，动着脚趾。'),('He freed the stuck peg by wiggling it from side to side.','他左右晃动，把卡住的木钉弄松取出。'),sources=S('wiggling','wiggle'))
WRITHE=[['古英语 writhan 的捆缠、扭转材料 → 中古英语 writhen → writhe','较远属于转、弯词族；早期也能说把东西扭弯'],['身体、四肢扭曲 → 因痛苦、难堪等而翻扭','现代常见身体不舒服的动作，也用来描写内心难受']]
W('writhe','/raɪð/','扭动、翻扭、挣扎；因痛苦或难堪而不自在',
 '身体难受得在原地拧、翻，或一条蛇缠着扭动，是 writhe。比 squirm 更容易让人感到强烈的不适、痛苦或挣扎。',
 '承古英语 wriðan 的捆缠、扭转义，经中古英语 writhen 延续；现代 w 不发音，th 读浊音 /ð/。',WRITHE,
 'writhe in pain 是痛得翻扭，writhe with embarrassment 是难堪得浑身不自在；后者不必真的在地上翻滚。',
 'writhe on the ground 在地上扭动；make someone writhe 使人痛苦或难堪不安。',
 'writhe 比 wiggle 更强烈、更有难受或扭曲感；写轻松动脚趾，用 wiggle 往往更自然。',
 ('The snake began to writhe in the grass.','蛇开始在草里扭动。'),('The memory still made him writhe with embarrassment.','那段回忆仍让他难堪得浑身不自在。'),sources=S('writhe','writhe'))
W('writhes','/raɪðz/','翻扭、挣扎；因痛苦或难堪而不自在〔第三人称单数〕',
 '一个人身体难受得扭曲，或一条蛇全身拧动，叫 writhes；心里难堪得受不了，也可借这种扭动描写。',
 'writhe + -s，基础 e 保留；/ð/ 后读 /z/，结尾 /ðz/，不是 /sɪz/。',WRITHE+[['writhe + -s → writhes','他、她或它扭曲、翻动']],
 'writhes in pain 是痛得翻扭，writhes around the branch 是缠着树枝扭动；常见于叙述身体动作。',
 'writhes on the floor 在地上扭动；writhes with embarrassment 难堪不安。',
 'writhes 强调动作或内心的折磨，hurts 只说疼；疼的人可能安静不动，不一定 writhes。',
 ('In the scene, the injured character writhes on the floor.','在那场戏里，受伤的角色在地上翻扭。'),('He writhes with embarrassment whenever he recalls the speech.','每次想起那次演讲，他都难堪得浑身不自在。'),sources=S('writhes','writhe'))
W('writhed','/raɪðd/','扭动、翻扭、挣扎了；难堪得不自在了',
 '刚才身体因难受而拧来翻去，或回想当时心里难堪得受不了，是 writhed。动作可以很明显，也可以借来写内心反应。',
 'writhe 去末尾 e + 完整 -ed → writhed；/ð/ 后读 /d/，结尾 /ðd/，e 不表示多一个音节。',WRITHE+[['writhe 去 e + -ed → writhed','过去身体翻扭；内心难堪、受煎熬']],
 'writhed in pain 是痛得翻扭，writhed at the memory 是想起那件事就难堪；语境区分肉体与心理。',
 'writhed on the ground 在地上扭动了；writhed in embarrassment 难堪不安了。',
 'writhed 的基础元音 /aɪ/ 不变，writhe → writhed 是规则 -ed；不要因为旧英语动词很古老，就认为现代过去式一定变元音。',
 ('The fish writhed in the wet net.','鱼在湿网里扭动。'),('She writhed with embarrassment when she heard her old recording.','听到自己以前的录音，她难堪得浑身不自在。'),sources=S('writhed','writhe'))
W('writhing','/ˈraɪðɪŋ/','正在扭曲、翻扭、挣扎；扭动着的',
 '身体正一阵阵拧、翻，像要逃出不舒服的状态，是 writhing；一团蛇、虫交织着扭动也能这样描述。',
 'writhe 去末尾 e + 完整 -ing → writhing；th 仍读浊音 /ð/，与 writhe 的读音基础相接。',WRITHE+[['writhe 去 e + -ing → writhing','扭曲、翻扭的过程']],
 'writhing in pain 是正痛得翻扭，a writhing mass 是一团交织扭动的东西；心理用法仍可接 with embarrassment。',
 'writhing on the ground 在地上翻扭；a writhing snake 扭动的蛇。',
 'writhing 关注身体怎样拧动，shaking 只说抖、摇；发抖可以几乎没有身体扭曲的动作。',
 ('The actor lay writhing on the stage.','演员躺在舞台上，扭动着身体。'),('We saw a writhing mass of worms in the soil.','我们在土里看见一团交织扭动的蚯蚓。'),sources=S('writhing','writhe'))
SWERVE=[['中古英语 swerven 的离开、偏转 → swerve','形式与古英语 sweorfan 的磨擦材料相接，但意义路线有疑问'],['偏离直路 → 偏离原则、原定路线等','现代把直行路线借成既定方向；不把磨擦到转向的候选步骤当事实']]
W('swerve','英 /swɜːv/；美 /swɜːrv/','突然转向、偏转；偏离；偏转动作',
 '正沿路走，眼前来了障碍，方向一下往旁边偏，是 swerve。讲原则、计划时，它像从原来那条线偏出去了。',
 '中古英语 swerven 已有离开、转到一旁义；形式似承古英语 sweorfan，但从磨擦到偏转的意义连接未定，也可能牵涉不同旧词。',SWERVE,
 'swerve to avoid something 是突然转向避开，swerve from the path 是偏离道路；never swerve from a principle 是始终不偏离原则。',
 'a sudden swerve 突然偏转；swerve sharply 急转方向。',
 'swerve 常带突然、向旁边偏离的感觉，turn 更宽；正常转弯也叫 turn，未必需要 swerve。',
 ('The driver had to swerve to avoid a fallen branch.','司机不得不突然转向，避开掉落的树枝。'),('She refused to swerve from her original plan.','她不肯偏离原来的计划。'),sources=S('swerve','swerve'))
W('swerves','英 /swɜːvz/；美 /swɜːrvz/','突然转向、偏离〔第三人称单数〕；偏转动作〔复数〕',
 '一辆车或一颗球突然偏到另一边，是 swerves；几下急转，也能当作一个个可数的偏转动作。',
 'swerve + -s，/v/ 后读 /z/，结尾 /vz/；保留基础末尾 e，三单与名词复数同形。',SWERVE+[['swerve + -s → swerves','它突然偏转；几次偏转']],
 'swerves across the road 是突然横偏过道路，swerves away from an obstacle 是偏开障碍；也可写叙述偏离原话题。',
 'swerves to the left 突然左偏；sharp swerves 急剧的偏转。',
 'swerves 的偏转不保证失控，但会让人看到方向明显改变；drifts 更容易是渐渐、不知不觉偏过去。',
 ('The ball swerves to the left as it approaches the goal.','球接近球门时向左偏转。'),('The car made several sharp swerves on the uneven road.','汽车在坑洼道路上几次猛然偏转。'),sources=S('swerves','swerve'))
W('swerved','英 /swɜːvd/；美 /swɜːrvd/','突然转向、偏离了',
 '刚才方向猛地往旁边变，用 swerved；也可回头说谈话、思路从原来的路线转开了。',
 'swerve 去末尾 e + 完整 -ed → swerved，/v/ 后读 /d/，结尾 /vd/。',SWERVE+[['swerve 去 e + -ed → swerved','过去方向突然偏开']],
 'swerved to the right 是突然右转，swerved off the road 是偏出道路；swerved away from the topic 是从话题转开。',
 'swerved around the obstacle 转向绕过障碍；swerved sharply 猛然偏转。',
 'swerved 强调转向的过程，crashed 强调撞上的结果；车 swerved 后可以成功避开，也可能另有后果。',
 ('The cyclist swerved around the pothole.','骑车人突然转向，绕开坑洞。'),('The conversation swerved away from the awkward question.','谈话一下从那个尴尬的问题转开了。'),sources=S('swerved','swerve'))
W('swerving','英 /ˈswɜːvɪŋ/；美 /ˈswɜːrvɪŋ/','正在突然转向、偏转；急转的',
 '行进路线正一下偏到旁边，是 swerving。可以是一回避让，也可以几次左右急转；它把方向变化画出来。',
 'swerve 去末尾 e + 完整 -ing → swerving；v 留着，分词描写路线偏转的过程。',SWERVE+[['swerve 去 e + -ing → swerving','突然转向、偏离的过程']],
 'swerving from side to side 是左右急转，swerving to avoid a cyclist 是急转避开骑车人；也能比喻偏离既定立场。',
 'a swerving vehicle 突然偏转的车；swerving off course 偏离路线。',
 'swerving 强调向旁偏开，braking 强调减速；避开同一障碍，可能用其中一种，也可能两者同时发生。',
 ('The van was swerving from side to side.','那辆货车正左右急转。'),('She avoided the fallen box by swerving to the left.','她向左急转，避开了掉下的箱子。'),sources=S('swerving','swerve'))
VEER=[['法语 virer 转动 → 英语 veer','较早用于风、船改变方向，更远来源不确定'],['改变行进方向 → 话题、态度走向别处','现代核心是从原来的路线偏向另一边，不限定道路']]
W('veer','英 /vɪə/；美 /vɪr/','改变方向、偏转；转向另一种话题、态度',
 '走着的路线开始偏向左边，风向换了，话题也突然拐进旧事，都可 veer。抓住一条线转向别处的画面就好。',
 '借法语 virer 转动，英语早期多见于风、船转向；法语词的更远来源未定，不把与拉丁语手镯或振动材料的猜测写成定论。',VEER,
 'veer left 是向左偏转，veer off the path 是偏离小路，veer towards a topic 是话题转向某处；方向可快可慢。',
 'veer away from something 转离、避开；veer between extremes 在极端之间变来变去。',
 'veer 只要求方向、倾向改变，swerve 常更有突然急偏的感觉；但 veer sharply 也能写急转，不能绝对按快慢分词。',
 ('The path begins to veer left beyond the bridge.','过桥后，小路开始向左偏。'),('The discussion could easily veer into unrelated issues.','讨论很容易转到不相干的问题上。'),sources=S('veer','veer'))
W('veers','英 /vɪəz/；美 /vɪrz/','改变方向、偏转、转向〔第三人称单数〕；方向变化〔复数〕',
 '一条路往旁边转，一段话转向另一类事情，动词都可用 veers；中心是原来的走向变了。',
 'veer + -s，读 /z/；ee 和 r 保留，常见作动词三单，方向变化名词也可用同形复数。',VEER+[['veer + -s → veers','它改变方向、偏向另一边']],
 'veers towards the coast 是偏向海岸，veers off topic 是偏离主题；地图、谈话等都能成为主语。',
 'veers sharply 急剧偏转；veers between styles 在不同风格之间转来转去。',
 'veers off topic 说话题离开原线，disagrees 说意见不同；讨论可以仍围绕主题却有分歧，也可以没争论却跑题。',
 ('The road veers towards the coast after the village.','过了村子，道路转向海岸。'),('His story veers into fantasy near the end.','他的故事接近结尾时转入了幻想。'),sources=S('veers','veer'))
W('veered','英 /vɪəd/；美 /vɪrd/','改变方向、偏转了；话题、态度转向了',
 '刚才行进方向拐向另一边，或谈话偏进另一类事情，是 veered。它把路线的转变记在过去。',
 'veer + 完整 -ed，读 /d/；不是去 e 再加词尾，因为基础末尾是发音材料的一部分 ee 加 r，并无单独不发音尾 e。',VEER+[['veer + -ed → veered','过去路线、话题、倾向发生转变']],
 'veered off the road 是偏离道路，veered towards a new subject 是转向新话题；常用 away、off、towards 指出方向。',
 'veered to the right 向右偏了；veered away from the subject 转离话题。',
 'veered 与 turned 可都表示转向，veered 常让人看到偏出原本走向；turned 则能很中性地说按预定路线转弯。',
 ('The boat veered away from the rocks.','船转向，避开了礁石。'),('Our conversation veered towards childhood memories.','我们的谈话转到了童年回忆上。'),sources=S('veered','veer'))
W('veering','英 /ˈvɪərɪŋ/；美 /ˈvɪrɪŋ/','正在改变方向、偏转；话题或倾向正在转移',
 '路线正从原方向转开，是 veering；讨论的重心不断滑向另一件事，也能这样描写。',
 'veer + 完整 -ing，直接加；英式在元音开头词尾前发 r，动词过程仍是改变走向。',VEER+[['veer + -ing → veering','方向、倾向变化的过程']],
 'veering off course 是正偏离航线、路线，veering into politics 是谈话转入政治；veering between extremes 是在极端间变来变去。',
 'veering sharply to one side 急剧转向一边；veering away 转离。',
 'veering 说走向改变，wandering 常说漫无目的地移动、走神；一次明确改向也可 veering，并不总是乱转。',
 ('We noticed the boat veering towards the shore.','我们注意到船正偏向岸边。'),('The discussion was veering into subjects we had not planned to cover.','讨论正转入我们原本没打算涉及的话题。'),sources=S('veering','veer'))
TILT=[['中古英语 tilten 的倒下、推倒材料 → tilt','可能接古英语不稳词族；未记录的重建形式保留为推测'],['倾倒的旧义 → 现代倾斜、使倾斜 → 偏向','一端高、一端低；机会、判断像被压向某一边']]
W('tilts','/tɪlts/','倾斜、使倾斜；使偏向〔第三人称单数〕；倾角、倾斜动作〔复数〕',
 '一个人把头歪一点，瓶口抬高或压低，用 tilts；一个因素把局势推向某边，也像把平衡面倾过去。',
 'tilt + -s，/t/ 后读 /s/，结尾 /lts/；动词三单和倾斜名词复数同形。',TILT+[['tilt + -s → tilts','它倾斜；他、她使物体倾斜；多次倾斜']],
 'tilts her head 是歪头，tilts the balance 是使天平、局势偏向某边；物体也可自己 tilts backwards。',
 'tilts slightly 稍稍倾斜；tilts the screen 调斜屏幕。',
 'tilts 可以只是改变角度、还站得稳，topples 则通常失衡倒下；倾斜不是倾覆的必然结果。',
 ('She tilts her head when she listens carefully.','她认真听时会把头歪一点。'),('The extra space tilts the balance in favour of the larger room.','多出来的空间让选择偏向了更大的房间。'),sources=S('tilts','tilt'))
W('tilted','/ˈtɪltɪd/','倾斜、使倾斜了；斜着的；偏向的',
 '相框一边高一边低，或人把头稍歪，是 tilted；规则、条件偏向一方，也像把原本平的面斜了过去。',
 'tilt + 完整 -ed，/t/ 后读 /ɪd/，多一个音节；lt 两个辅音字母后直接加词尾。',TILT+[['tilt + -ed → tilted','已经倾斜；已被带向某边']],
 'tilted her head 是歪了歪头，a tilted screen 是倾斜屏幕；tilted in favour of someone 是偏向某人、有利于某人。',
 'tilted backwards 向后倾；slightly tilted 稍稍斜着。',
 'tilted 描写相对于正直位置的角度，crooked 还可泛说不直、不正；一块整体平直的板也能 tilted。',
 ('He tilted the lamp towards the page.','他把灯斜向书页。'),('The picture frame was slightly tilted.','相框有点歪。'),sources=S('tilted','tilt'))
W('tilting','/ˈtɪltɪŋ/','正在倾斜、使倾斜、偏向；倾斜动作',
 '把瓶子一点点斜过去倒水，或把屏幕调成斜角，是 tilting；局面向一边偏，也能借同一个动作说。',
 'tilt + 完整 -ing，直接加，lt 保留。tilting at windmills 的骑枪比喻另有旧比武材料背景，不能从倒水动作直接推出词史。',TILT+[['tilt + -ing → tilting','改变角度、使局势偏向的过程']],
 'tilting the screen 是调屏幕角度，tilting towards one side 是正在向一边倾；tilting at windmills 比喻攻击想象中的敌人或无谓争斗。',
 'tilting her head 歪着头；a tilting platform 可倾斜平台。',
 'tilting 常可以是受控调角度，tipping over、toppling 更突出倒下；读倒水场景时不用一见倾斜就想成事故。',
 ('She adjusted the view by tilting the screen.','她把屏幕调斜，改变观看角度。'),('The boat was tilting to one side under the uneven load.','货物装得不均，船正向一侧倾斜。'),sources=S('tilting','tilt'))
TOPPLE=[['top 的旧倾倒动作材料 + -le → topple','旧式反复动作形式，较早说翻滚、头向下倒'],['失衡倒下、使倒下 → 推翻权力、地位','现代词形接完整 topple；比喻像把原本站在高处的一方推倒']]
W('topples','英 /ˈtɒpəlz/；美 /ˈtɑːpəlz/','倒下、倾覆、推倒、推翻〔第三人称单数〕',
 '积木塔重心一偏，整个倒下来，是 topples；一场冲击让强势的人或权力垮下，也像推倒那座塔。',
 'topple + -s，/l/ 后读 /z/。基础 topple 接 top 的旧动作材料与 -le，不从希腊表示地点的 top- 解释。',TOPPLE+[['topple + -s → topples','它失衡倒下；它使人、物或权力倒下']],
 'topples over 是倒下来，topples the tower 是把塔弄倒；topples a leader 是使领导者失去地位。',
 'topples off the shelf 从架上倒下；topples the stack 弄倒堆叠物。',
 'topples 把失衡倒下的结果说出来，wobbles 只说晃；塔可以先晃一阵后稳住，也可以接着倒下。',
 ('The tower topples if the bottom block is pulled away.','底部那块积木一抽走，塔就会倒。'),('A strong gust sometimes topples the light garden chairs.','一阵强风有时会吹倒轻便的花园椅。'),sources=S('topples','topple'))
W('toppled','英 /ˈtɒpəld/；美 /ˈtɑːpəld/','倒下、倾覆了；被推倒、被推翻了',
 '刚才花瓶、树或一堆积木从直立变成倒下，是 toppled；一个掌权者失势，也可以像站不住的塔被推翻。',
 'topple 去末尾 e + 完整 -ed → toppled，/l/ 后读 /d/；原有双 p 保留。',TOPPLE+[['topple 去 e + -ed → toppled','过去倒下；已被推倒、失去地位']],
 'toppled over 是倒了，toppled the statue 是推倒雕像；was toppled 是被推翻，主动、被动都常见。',
 'toppled by the storm 被风暴吹倒；toppled from power 被赶下台。',
 'toppled 通常已有倒下、失势结果，teetered 更常是将倒未倒；两个词可组成先摇摇欲坠、后倒下的过程。',
 ('The wind toppled a tree beside the road.','风吹倒了路边一棵树。'),('The vase toppled from the narrow shelf.','花瓶从窄架子上倒落下来。'),sources=S('toppled','topple'))
W('toppling','英 /ˈtɒpəlɪŋ/；美 /ˈtɑːpəlɪŋ/','正在倒下、倾覆、推倒、推翻；倾覆过程',
 '一座塔正歪过去倒落，或手推的积木开始一块接一块倒，是 toppling；政权、优势地位也能进入被推倒的过程。',
 'topple 去末尾 e + 完整 -ing → toppling；把倾倒、使倾倒的完整动词变成过程或动作名词。',TOPPLE+[['topple 去 e + -ing → toppling','倒下、推倒或推翻的过程']],
 'toppling over 是正在倒，toppling a stack 是正在弄倒一摞；the toppling of a statue 是推倒雕像这件事。',
 'stop it from toppling 扶住不让它倒；toppling dominoes 倒落的多米诺骨牌。',
 'toppling 是从直立失衡倒下，dropping 只需从高处落；东西可以平平地掉下，不一定有先歪倒的画面。',
 ('She caught the toppling box before it hit the floor.','箱子正倒下时，她在它落地前接住了。'),('The children watched the toppling dominoes in silence.','孩子们安静地看着多米诺骨牌接连倒下。'),sources=S('toppling','topple'))

def extend_lessons():
 extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_zfm',ROOTS,WORDS)
 extend_lessons()
