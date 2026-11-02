"""Bashing, punching, splashes, scattered drops and interrupted bursts."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
def S(word,base):
 return ['https://en.wiktionary.org/wiki/'+word+'#English','https://www.etymonline.com/word/'+base]
EXISTING_ROOT_ADDITIONS={
 'B3299':dict(words=['bash','bashes','bashed','bashing'],label='bash 的重击、抨击与尝试等口语',note='bash 可能北欧来源或拟声，古诺尔斯 *basca 是推定形式；抨击、尝试、派对各自发展，不能把每义都写成真实打斗。'),
 'B3878':dict(words=['smash','smashes','smashed','smashing'],label='smash 的碎裂、扣杀与巨大成功',note='smashes 的 -es 读 /ɪz/；动词三单、名词复数同形，可以写打碎、体育扣杀或大获成功的作品。'),
 'B3218':dict(words=['splash','splashes','splashed','splashing','splatter','splatters','splattered','splattering'],label='splash 与 splatter：水花、飞溅与形象比较',note='splash 可能接 plash 加强化材料；splatter 有受 splash、spatter 影响的分析，保留可能性，不把教学联想写成确定混成史。'),
 'A1697':dict(words=['spatter','spatters','spattered','spattering'],label='spatter 的喷、溅材料与旧反复动作形式',note='spatter 可能联系荷兰语或低地德语 spatten 一系，再有反复动作形式；这里的 -er 属旧反复动作材料，现代直接以整个 spatter 为基础变化。'),
 'A1760':dict(words='bash bashes bashed bashing punch punches punched smash smashes splash splashes splashed splashing splatter splatters splattered splattering spatter spatters spattered spattering sputter sputters sputtered sputtering splutter splutters spluttered spluttering squirt squirts squirted squirting'.split(),label='重击、溅点、噗噗声与细流喷射的变化',note='punch 的戳、打孔、拳击与饮料分近源；sputter、splutter 可比较但不能直接从现代 spit 硬变。squirted 因 /t/ 后接 -ed 读 /ɪd/。'),
}
BASH=[['十七世纪 bash 重击动词 → 名词','或北欧来源，或拟声；不能把推定古诺尔斯形式当作直接记录'],['重击 → 猛批、尝试、派对等口语分支','have a bash 是试一下或办场聚会，按具体搭配分别理解']]
W('bashes','/ˈbæʃɪz/','猛击、猛批〔第三人称单数〕；重击、尝试、聚会〔复数〕',
 '用力敲、打一个东西，用 bashes；狠狠批评一个做法也能用。名词 bashes 还可以说几场热闹聚会。',
 'bash + -es，/ʃ/ 后读 /ɪz/。动词三单、名词复数同形，基础词来源可能北欧、也可能拟声。',BASH+[['bash + -es → bashes','他、她猛击、猛批；多记重击、聚会等']],
 'bashes the door 是猛敲门，bashes the government 是猛批政府；birthday bashes 是生日派对，属口语。',
 'bashes away at the keyboard 使劲敲键盘；big bashes 热闹的大聚会。',
 'bashes 作派对名词时不要求真打架；这个口语分支和动词重击画面有关联，但不是每场聚会都有击打。',
 ('He bashes the stuck door with his shoulder.','他用肩膀猛撞卡住的门。'),('They are known for throwing huge birthday bashes.','他们以办热闹的大型生日派对出名。'),sources=S('bashes','bash'))
W('bashed','/bæʃt/','猛击、撞击了；猛批了；〔bashed out〕草草写出、弹出',
 '刚才重重撞、敲了一下，叫 bashed；批评说得很重，也可这样写。bashed out a draft 则像猛敲键盘，赶快弄出一稿。',
 'bash + 完整 -ed，/ʃ/ 后读 /t/；只有一个音节，不读 /ɪd/。',BASH+[['bash + -ed → bashed','过去猛击、猛批；快速弄出内容等搭配']],
 'bashed his knee 是撞了膝盖，bashed the plan 是猛批计划；bashed out an email 是很快草草写出邮件。',
 'bashed against a wall 撞到墙；bashed out a tune 使劲、随意弹出曲子。',
 'bashed out 常带赶快、不精细的感觉；carefully drafted 则强调仔细起草，速度、态度都不同。',
 ('I bashed my knee on the low table.','我的膝盖重重撞到了矮桌。'),('She bashed out a first draft in an hour.','她一小时里赶出了一份初稿。'),sources=S('bashed','bash'))
W('bashing','/ˈbæʃɪŋ/','正在猛击、猛批；一顿重打、猛烈抨击',
 '工具、身体正重重敲撞，是 bashing；评论中对某人、某事集中猛批，也可叫 a bashing。',
 'bash + 完整 -ing，直接加；可写进行动作，也可作活动名词，再用于抨击的比喻。',BASH+[['bash + -ing → bashing','猛击过程；猛烈批评活动']],
 'bashing on the door 是猛敲门，give the proposal a bashing 是猛烈抨击提案；宾语帮助区分实体还是观点。',
 'constant bashing 没完没了的猛批；bashing away at a keyboard 使劲敲键盘。',
 'bashing 语气比 discussion、criticism 更猛烈，通常带痛打或集中攻击的感觉；并不是普通中性讨论。',
 ('Someone was bashing on the door downstairs.','有人在楼下猛敲门。'),('The proposal took a bashing in the press.','这项提案遭到媒体猛烈抨击。'),sources=S('bashing','bash'))
PUNCH=[['古法语 ponchonner、ponchon → 中古英语 punchen → punch','戳、冲打、尖工具；后来常用于打孔、拳击'],['工具、击打与其他同形词','punch 工具名还联系 puncheon 的缩短；饮料 punch 另有来源争论，不从打孔推来']]
W('punches','/ˈpʌntʃɪz/','拳击、打孔、输入〔第三人称单数〕；拳击、冲孔工具〔复数〕',
 '拳头一记记打出，或冲孔器把纸打穿，用 punches。输入数字时 punch in 也保留一下下按键的动作感。',
 'punch + -es，/tʃ/ 后读 /ɪz/；动词三单、工具或击打名词复数同形。饮料同形词的来源另分。',PUNCH+[['punch + -es → punches','他、她拳击、打孔；多记拳击、冲孔工具']],
 'punches holes 是打孔，throws punches 是挥拳，punches in a number 是按键输入号码；不是每义都在打人。',
 'powerful punches 有力拳击；punches a ticket 给票打孔。',
 'punches 常指拳头或冲孔动作，slaps 更常是张开的手掌拍；动作形状不同。',
 ('The machine punches two holes in each sheet.','机器在每张纸上打两个孔。'),('The boxer threw several quick punches.','拳击手快速打出几拳。'),sources=S('punches','punch'))
W('punched','/pʌntʃt/','用拳打了；打孔了；按键输入了',
 '刚才出拳、给纸打孔、把号码一个个按进去，都能用 punched；共同动作是一下下冲、戳、按进去。',
 'punch + 完整 -ed，/tʃ/ 后读 /t/，结尾 /tʃt/；不另加 /ɪd/。',PUNCH+[['punch + -ed → punched','过去拳击、冲孔或按键输入']],
 'punched a hole 是冲出一个孔，punched in the code 是输入密码、代码；punch the clock 还可指打卡。',
 'punched the bag 打了沙袋；punched in the number 按入号码。',
 'punched 不能一律译成揍：punched holes、punched in a code 都是工具或按键动作，宾语决定中文。',
 ('She punched two holes in the paper.','她在纸上打了两个孔。'),('He punched in the code and opened the door.','他按键输入密码，打开了门。'),sources=S('punched','punch'))
W('smashes','/ˈsmæʃɪz/','砸碎、猛击、打破纪录〔第三人称单数〕；扣杀、巨大成功作品〔复数〕',
 '猛地一击、东西碎了，用 smashes；体育里可说扣杀、打破纪录，演艺里 smashes 又可指大获成功的作品。',
 'smash + -es，/ʃ/ 后读 /ɪz/；基础词可能拟声，不能硬拆成 s + mash 再声称这就是确定形成史。',
 [['近代英语 smash','强烈撞击、碎裂材料，具体来源未定，大概拟声'],['smash + -es → smashes','三单、名词复数；体育与巨大成功等分支']],
 'smashes a record 是打破纪录，smashes the ball 是猛击球，box-office smashes 是票房大热作品；不全是真砸碎。',
 'powerful smashes 强力扣杀；smashes into a wall 猛撞墙。',
 'smashes 强调击碎、压倒性效果，scratches 只是刮、划，cracks 还可只裂开；动作结果有轻重差别。',
 ('The tennis player wins points with powerful smashes.','网球选手靠强力扣杀得分。'),('Her new film smashes the opening-week record.','她的新电影打破首周纪录。'),sources=S('smashes','smash'))
SPLASH=[['较早 plash 等溅水材料 → splash','可能加了强化的 s-；不是每一步都能从现代字母独立推出来'],['溅水 → 飞溅液体、色块、醒目宣传等','make a splash 是引人注意；splash out 是痛快花钱，按搭配另记']]
W('splashes','/ˈsplæʃɪz/','溅水、泼溅、醒目刊登〔第三人称单数〕；水花、溅点、色块〔复数〕',
 '水“哗”地一溅，形成一团水花，用 splashes；墙上、画上的鲜明色块也可这样说，像颜色泼上去。',
 'splash + -es，/ʃ/ 后读 /ɪz/；声音动词、飞溅物名词同形变化，基础可能联系 plash 的强化形式。',SPLASH+[['splash + -es → splashes','它泼、溅；多团水花、液点或色块']],
 'splashes through puddles 是踩得水坑飞溅，splashes of colour 是鲜明色块；news splashed across a page 是醒目刊登。',
 'splashes of water 水花；splashes of red 一块块醒目的红色。',
 'splashes 可以是声音、动作、留下的色点；不是只表示泼的水量大。add a splash of milk 里甚至只是一点奶。',
 ('The child splashes through every puddle.','孩子踩过每个水坑，溅起水花。'),('Bright splashes of colour cover the canvas.','画布上是一块块鲜亮色彩。'),sources=S('splashes','splash'))
W('splashed','/splæʃt/','泼溅了、溅湿了；醒目刊登了；〔splashed out〕痛快花钱了',
 '水或别的液体刚才哗地溅出去、溅到人身上，用 splashed；splashed out on a holiday 又可说花一笔钱好好度假。',
 'splash + 完整 -ed，/ʃ/ 后读 /t/；不另加 /ɪd/。固定搭配的现代意义也跟着同一动词变化。',SPLASH+[['splash + -ed → splashed','过去泼溅、醒目展示；splashed out 的花钱义']],
 'splashed water on his face 是往脸上泼水，splashed the story across the front page 是把报道醒目放上头版。',
 'splashed through the stream 踩得小溪水花四溅；splashed out on dinner 花钱好好吃一顿。',
 'splashed out 常有舍得多花、享受一下的感觉；spent money 只说花钱，不一定有这层态度。',
 ('A passing car splashed mud onto my shoes.','经过的汽车把泥水溅到我的鞋上。'),('We splashed out on a special dinner for her birthday.','她生日那天，我们花钱好好吃了一顿特别的晚餐。'),sources=S('splashed','splash'))
W('splashing','/ˈsplæʃɪŋ/','正在泼溅、溅水；水花声、泼水活动；醒目刊登',
 '脚、手或船桨把水一阵阵扬起，叫 splashing。既能说动作，也能把水花四溅的声音作为背景。',
 'splash + 完整 -ing，直接加；sh 保留，不需要双写末尾 h。',SPLASH+[['splash + -ing → splashing','泼溅过程、声音；相应展示等引申用法']],
 'splashing in the pool 是在泳池里玩得水花四溅；the splashing of oars 是船桨激起水花的声音。',
 'splashing water around 四处泼水；splashing through puddles 踩过水坑飞溅。',
 'splashing 更侧重液体被打起、散开，swimming 是游泳；人在水里 splashing 不保证真会游。',
 ('The children were splashing in the shallow pool.','孩子们在浅水池里玩得水花四溅。'),('We heard splashing near the riverbank.','我们听见河岸附近有水花声。'),sources=S('splashing','splash'))
SPLATTER=[['十八世纪 splatter 及更早相关形式','可能受 splash、spatter 共同影响，具体形成不作唯一确定分析'],['液体、泥、漆飞散 → 落成一片片斑点、溅痕','既可写被溅到的表面，也可写液体飞出去']]
W('splatter','英 /ˈsplætə/；美 /ˈsplætər/','飞溅、泼溅；溅满；一片飞溅物、溅痕',
 '番茄酱、泥水、油漆“啪啦”散开，点点洒到四处，叫 splatter。常让人看见落在表面的一片乱点。',
 '可能受 splash、spatter 的声音、形式共同影响；可以用二者联想，却不把混成分析说成已确定的唯一历史。',SPLATTER,
 'splatter paint on the wall 是把漆泼溅到墙上，a splatter of mud 是一片泥点；物可飞溅，表面也可被溅满。',
 'splatter everywhere 四处飞溅；splatter the floor 溅得满地都是。',
 'splatter、spatter 在飞溅、溅点义大量重合；splatter 往往给人更散、更乱的画面，但不是液滴大小的严格分类。',
 ('The sauce began to splatter over the cooker.','酱汁开始往炉子上四处溅。'),('A splatter of paint marked the floor.','地上留下了一片飞溅的漆点。'),sources=S('splatter','splatter'))
W('splatters','英 /ˈsplætəz/；美 /ˈsplætərz/','飞溅、溅满〔第三人称单数〕；一片片溅点、飞溅物',
 '酱汁、泥水每次一动就往四处飞，用 splatters；地面、衣服上留下的一片片溅痕，也可用复数名词。',
 'splatter + -s，读 /z/；动词三单、飞溅物名词复数同形，词内 tt 保留。',SPLATTER+[['splatter + -s → splatters','它飞溅；多片飞溅物、溅痕']],
 'splatters onto the tiles 是溅到瓷砖上，paint splatters 是漆的溅点；名词不一定还在飞，可能已干。',
 'splatters everywhere 到处飞溅；mud splatters 泥水溅痕。',
 'splatters 在 paint splatters 中指留下的东西，在 sauce splatters 中通常写动作；句子结构帮助辨别。',
 ('The sauce splatters whenever it boils too hard.','酱汁煮得太猛就四处溅。'),('Paint splatters covered his old shoes.','他的旧鞋上满是漆点。'),sources=S('splatters','splatter'))
W('splattered','英 /ˈsplætəd/；美 /ˈsplætərd/','飞溅了、溅满了；沾满溅点的',
 '液体刚才啪啦溅开，或衣服、墙面被溅了一片乱点，叫 splattered。结果往往仍能看见。',
 'splatter + 完整 -ed，词尾读 /d/；词内虽然有 tt，最后的基础音不是 /t/，不读 /ɪd/。',SPLATTER+[['splatter + -ed → splattered','过去飞溅；已沾满溅点']],
 'splattered with mud 是沾满溅起的泥，splattered paint across the wall 是把漆四处泼到墙上；主动、被动都能用。',
 'mud-splattered boots 沾满泥点的靴子；splattered onto the floor 溅到地上。',
 'splattered 不等于整块浸湿：它常留下点状、不规则飞溅痕；soaked 则强调液体浸透、湿透。',
 ('Mud splattered across the side of the car.','泥水飞溅到车身侧面。'),('His jacket was splattered with paint.','他的外套上满是飞溅的漆点。'),sources=S('splattered','splatter'))
W('splattering','英 /ˈsplætərɪŋ/；美 /ˈsplætərɪŋ/','正在飞溅、溅满；一阵飞溅、溅点',
 '雨水、酱汁或油漆正乱点般飞出去，叫 splattering。它既能表现动作，也能说留下的一阵、一片溅痕。',
 'splatter + 完整 -ing；英式在后接元音时发 /r/，已有 tt 保留。',SPLATTER+[['splatter + -ing → splattering','散乱飞溅的过程、飞溅物']],
 'splattering against the window 是飞点打到窗上，a splattering of mud 是一片溅起的泥点；具体看介词、对象。',
 'splattering paint 泼溅的漆；splattering everywhere 四处乱溅。',
 'splattering 可强调分散的点、斑痕；pouring 更常是一股连续倒出，动作形态不同。',
 ('Rain was splattering against the window.','雨点正噼啪溅打在窗上。'),('The artist was splattering paint across the canvas.','画家正把油漆泼溅到画布上。'),sources=S('splattering','splatter'))
SPATTER=[['十六世纪 spattering 等材料 → spatter','可能是荷兰语、低地德语 spatten 喷、迸裂一系的反复动作形式'],['水、泥、漆点飞散 → 溅点、斑痕名词','后来名词也指已落下的零星液点，不限于飞的瞬间']]
W('spatter','英 /ˈspætə/；美 /ˈspætər/','飞溅、溅上；一片溅点、溅痕',
 '泥、雨、漆变成一粒粒点飞出去、落在表面，叫 spatter。重点常是散开的滴点、斑痕。',
 '可能接荷兰语或低地德语 spatten 喷、迸裂材料的反复动作形式；-er 不指人，不能把 spat 当此处必有的现代基础词。',SPATTER,
 'spatter mud on the wall 是把泥点溅上墙，a spatter of paint 是一片漆点；主动溅、被溅都能说。',
 'spatter the pavement 溅得人行道上都是点；spatter with mud 溅上泥。',
 'spatter、splatter 在普通飞溅场景常可互换；spatter 容易突出滴点，splatter 常更显四散、凌乱，不要当作绝对规则。',
 ('We heard the rain spatter against the glass.','我们听见雨点溅打玻璃。'),('A spatter of paint covered the edge of the table.','桌沿上留着一片漆点。'),sources=S('spatter','spatter'))
W('spatters','英 /ˈspætəz/；美 /ˈspætərz/','飞溅、溅上〔第三人称单数〕；一片片溅点',
 '雨、泥或漆一粒粒溅开，用 spatters；桌面、纸上的零星液点也能用复数名词。',
 'spatter + -s，读 /z/；三单、飞溅物名词复数同形，旧反复动作材料留在基础词中。',SPATTER+[['spatter + -s → spatters','它滴点飞溅；多片溅点、斑痕']],
 'spatters onto the ground 是飞点溅到地上，ink spatters 是墨汁溅点；名词不要求液体还在移动。',
 'spatters against the roof 溅打屋顶；small spatters of mud 小片泥点。',
 'spatters 与 spots 可都指斑点；spatters 常额外交代或让人想到液体飞溅留下的过程。',
 ('Rain spatters against the kitchen window.','雨点溅打着厨房窗户。'),('There were ink spatters on his sleeve.','他的袖子上有墨汁溅点。'),sources=S('spatters','spatter'))
W('spattered','英 /ˈspætəd/；美 /ˈspætərd/','飞溅了、溅上了；沾满溅点的',
 '泥水、油漆刚才散成滴点落下来，用 spattered；说衣服 spattered with mud，则是上面留了一片片泥点。',
 'spatter + 完整 -ed，读 /d/；基础词末尾不是 /t/，不能被词内 tt 误导成 /ɪd/。',SPATTER+[['spatter + -ed → spattered','过去飞溅；已溅上滴点']],
 'spattered with paint 是沾满漆点，rain spattered the steps 是雨点溅打台阶；可用液体或被溅表面作主语。',
 'spattered across the wall 溅到墙上各处；mud-spattered shoes 沾泥点的鞋。',
 'spattered 与 painted 不同：前者说散点飞溅，后者泛指涂画；一面墙可以被有意画上去，也可被意外溅脏。',
 ('Mud spattered the lower part of his trousers.','泥水溅上了他的裤腿。'),('The floor was spattered with blue paint.','地板上满是蓝色漆点。'),sources=S('spattered','spatter'))
W('spattering','英 /ˈspætərɪŋ/；美 /ˈspætərɪŋ/','正在飞溅、溅打；零星的溅点、一阵溅雨',
 '滴点正一个个散开、打到表面，叫 spattering；a spattering of rain 也可以把零星小阵雨整体说出来。',
 'spatter + 完整 -ing；英式接元音时发 /r/。可作分词或活动、少量飞溅物名词，具体看句子位置。',SPATTER+[['spatter + -ing → spattering','点状飞溅过程；一阵、一片飞溅物']],
 'spattering against the window 是飞点溅打窗户，a spattering of mud 是一片泥点；不限于水。',
 'a light spattering of rain 零星一阵雨；spattering paint 泼溅漆点。',
 'spattering 的零星、分散感与 a steady stream 的连续细流不同；不是看见液体都用同一个喷、流词。',
 ('We felt a light spattering of rain.','我们感到零星雨点落下来。'),('Paint was spattering onto the floor as he worked.','他干活时，漆点正溅到地板上。'),sources=S('spattering','spatter'))
SPUTTER=[['十六世纪 sputter，联系日耳曼 *sput- 喷、吐材料','与荷兰语 sputteren 等可比较，有反复、小量迸出和声音感'],['噗噗迸出 → 引擎断续响、人急促说话','话像一下下喷出来，也可比喻进展一顿一顿、难以持续']]
W('sputter','英 /ˈspʌtə/；美 /ˈspʌtər/','噗噗响、断续喷出；急促含混地说；断断续续运转',
 '旧引擎“噗、噗”几下、火苗一点点迸出来，像 sputter；人气急、惊讶得话一下下喷出来，也能这样写。',
 '联系日耳曼喷、吐材料，可与荷兰语 sputteren 等比较；不是按现代 spit → spat 的变元音规则再造一个词。',SPUTTER,
 'the engine sputters 是引擎断续噗响，sputter an objection 是急急喷出反对意见；sputter out 可说断续响后熄掉。',
 'sputter into life 噗噗响着启动；sputter in surprise 惊得急促说话。',
 'sputter 常把细小爆发、断续声写出来；hum 更平稳、连续。人 sputters 也不一定真在有意吐口水。',
 ('The old engine began to sputter.','旧引擎开始断续噗响。'),('He could only sputter in surprise at the announcement.','听到宣布，他惊得只能断断续续说几句。'),sources=S('sputter','sputter'))
W('sputters','英 /ˈspʌtəz/；美 /ˈspʌtərz/','噗噗断续响、急促说〔第三人称单数〕；一阵阵噗响',
 '引擎一阵一阵噗响、运转不连贯，或人急得话说不顺，用 sputters。复数名词也能把几阵小爆发声数出来。',
 'sputter + -s，读 /z/；基础词里的旧喷吐、反复声材料不拆成指人后缀。',SPUTTER+[['sputter + -s → sputters','它噗噗响；他、她急促说；多阵噗响']],
 'sputters and stops 是断续响后停了，sputters in disbelief 是不敢相信、急急说不顺；原因由后面词交代。',
 'sputters into life 噗响着启动；brief sputters 几阵短促噗响。',
 'sputters 描写断续的小爆发，roars 往往更饱满连续；它们能写同一引擎不同的运转状态。',
 ('The engine sputters whenever the fuel runs low.','燃料快用完时，引擎就断续噗响。'),('He sputters in disbelief when he hears the price.','他听到价格，不敢相信，话说得急急断断续续。'),sources=S('sputters','sputter'))
W('sputtered','英 /ˈspʌtəd/；美 /ˈspʌtərd/','噗噗断续响了；急促说了；断断续续地运转了',
 '机器刚才噗噗响了几下，或人气急、惊讶得话一下下冒出来，用 sputtered。',
 'sputter + 完整 -ed，读 /d/；基础词末尾是轻元音或 r，不因词内 tt 就读 /ɪd/。',SPUTTER+[['sputter + -ed → sputtered','过去断续噗响、急促说']],
 'sputtered into life 是噗噗响着启动了，sputtered an objection 是急急说出反对；常可接具体喊话。',
 'sputtered and died 噗响几下熄了；sputtered in surprise 惊得急急说。',
 'sputtered 不等于机器一定彻底坏了：它可启动后运转顺，也可噗响后停，结果由后续动作交代。',
 ('The engine sputtered and then died.','引擎噗噗响了几下，随后熄火。'),('“That cannot be right!” he sputtered.','“那不可能对！”他急急、断续地说。'),sources=S('sputtered','sputter'))
W('sputtering','英 /ˈspʌtərɪŋ/；美 /ˈspʌtərɪŋ/','正在噗噗断续响、急促说；断断续续、难以持续的',
 '一阵阵小爆发正冒出来，是 sputtering；写项目、进展时，也可借引擎点着又不顺的感觉说推进断续。',
 'sputter + 完整 -ing；英式接元音时发 /r/，不从一个指人名词去倒推动作。',SPUTTER+[['sputter + -ing → sputtering','噗响、急说过程；比喻进展断续']],
 'a sputtering engine 是断续噗响的引擎，sputtering with rage 是气得话急而断续；不是单纯提高音量。',
 'sputtering into life 断续启动；a sputtering start 断断续续、不顺利的开头。',
 'sputtering 与 stuttering 在机器、过程语境可接近；sputtering 常多细小喷发、噗声感，stuttering 更重卡顿。',
 ('A sputtering engine disturbed the quiet morning.','一台断续噗响的引擎打破早晨的安静。'),('He was sputtering with rage as he read the letter.','他读信时气得话说得又急又断续。'),sources=S('sputtering','sputter'))
SPLUTTER=[['十七世纪 splutter 喧闹、混乱名词 → 后来的动词','可能是 sputter 的变体，受 splash、splatter 等辅音组合强化'],['急促混乱地说 → 断续喷、噗响等现代场景','与 sputter 大量重合；不把每个 l 都当可独立解释的后缀']]
W('splutter','英 /ˈsplʌtə/；美 /ˈsplʌtər/','急促含混地说；噗噗响、断续喷出；一阵噗响、急语',
 '人惊得、气得话一下下挤出来，甚至带喷吐声，像 splutter；引擎、蜡烛断续噗响也可以用。',
 '可能是 sputter 的强化变体，受 splash、splatter 等形式影响。较早名词说喧闹、混乱，后来有相应动词，不硬画成每义都先有动词。',SPLUTTER,
 'splutter an objection 是急急断续地反对，splutter with laughter 是笑得话、气息一阵阵喷出来；具体情绪由搭配给。',
 'a splutter of protest 一阵急促反对声；splutter into life 噗响着启动。',
 'splutter 与 sputter 常可重合，不能硬分一个只写人、一个只写机器；两者都可表现断续、小爆发的声音。',
 ('He could only splutter in protest at the suggestion.','听到那个提议，他只能急急、断续地表示反对。'),('The engine started with a splutter.','引擎噗噗响着启动了。'),sources=S('splutter','splutter'))
W('splutters','英 /ˈsplʌtəz/；美 /ˈsplʌtərz/','急促含混说、噗噗响〔第三人称单数〕；一阵阵噗响、急语',
 '一个人话急得不顺、一下下冒出来，或机器断续噗响，用 splutters。名词复数也能说几阵这种声音。',
 'splutter + -s，读 /z/；已有 tt 保留，现代变化接整个基础词。',SPLUTTER+[['splutter + -s → splutters','他、她急促说；它噗响；几阵噗声']],
 'splutters in disbelief 是惊得不敢相信、话说不顺，splutters into life 是断续噗响着启动。',
 'splutters with laughter 笑得断续喷声；splutters and stops 噗响后停。',
 'splutters 描写发声、运转的方式，不规定一定是生气；笑、惊讶或机器启动都可能出现。',
 ('He splutters with laughter whenever he tries to tell the story.','他每次想讲那个故事，都笑得断断续续说不顺。'),('The old engine splutters before it starts properly.','旧引擎先噗噗断续响，随后才运转起来。'),sources=S('splutters','splutter'))
W('spluttered','英 /ˈsplʌtəd/；美 /ˈsplʌtərd/','急促含混地说了；断续噗响、喷出了',
 '刚才话又急又断续地冲出来，或机器噗噗响了一阵，用 spluttered。常接惊讶、反对或着急说出的内容。',
 'splutter + 完整 -ed，读 /d/；不是看词中 tt 就把词尾读成 /ɪd/。',SPLUTTER+[['splutter + -ed → spluttered','过去急促说、断续噗响']],
 'spluttered an objection 是急急挤出反对意见，spluttered into life 是噗响着启动；可以接引号中的话。',
 'spluttered in shock 惊得急促说；spluttered and died 噗响后熄了。',
 'spluttered 与 stammered 都能写话不顺，前者常更有急促、喷吐的听感；不能据此把所有说话停顿都归同一原因。',
 ('“You must be joking!” she spluttered.','“你一定在开玩笑！”她急急、断续地说。'),('The motor spluttered for a moment and then stopped.','马达噗噗响了一会儿，随后停了。'),sources=S('spluttered','splutter'))
W('spluttering','英 /ˈsplʌtərɪŋ/；美 /ˈsplʌtərɪŋ/','正在急促含混地说、断续噗响；噗噗声、急语',
 '人正急急冒话、笑得气息一阵阵断开，或引擎正噗噗不稳地响，叫 spluttering。',
 'splutter + 完整 -ing；英式后接元音时发 /r/。-er 留在完整动词里，不作一个人来分析。',SPLUTTER+[['splutter + -ing → spluttering','急语、断续噗响的过程与状态']],
 'spluttering with indignation 是气愤得话说不顺，a spluttering engine 是断续噗响的引擎；也有笑、受惊等原因。',
 'spluttering with laughter 笑得喷声、话不顺；spluttering protests 急促断续的反对声。',
 'spluttering 重动作、声音的急促不连贯，mumbling 重字句含糊；一个人可以说得快而清楚，也可以含糊却不急。',
 ('He was spluttering with indignation at the accusation.','面对指责，他气得话说得又急又断续。'),('We listened to the spluttering engine in the yard.','我们听着院子里引擎断续噗响。'),sources=S('spluttering','splutter'))
SQUIRT=[['中古英语 squirten、squyrten 等 → squirt','喷、吐水材料，可能经荷兰语或低地德语，最终大概拟声；具体来源未定'],['突然喷出细流 → 一次喷量、喷射动作','名词与动词的早期记录不宜硬排成现代动词先造全部名词的单线']]
W('squirt','英 /skwɜːt/；美 /skwɜːrt/','挤、喷出细流；一股短促细流、一挤的量',
 '捏一下水枪、番茄酱瓶，细细一股液体突然挤出去，叫 squirt。抓住短促、成细流、受挤压的画面。',
 '接中古英语 squirten 等喷、吐水材料，或经荷兰语、低地德语，最终大概拟声；不是现代 squeeze 的规则缩写。',SQUIRT,
 'squirt water at someone 是朝某人喷水，a squirt of ketchup 是挤一点番茄酱；名词能表示一次喷射或那点量。',
 'squirt out 喷挤出来；a quick squirt 快速一喷、一挤。',
 'squirt 常是短促细流，spray 常把液体散成许多细滴；同一瓶子用不同喷头，动作也能不同。',
 ('She added a squirt of ketchup to the plate.','她往盘里挤了一点番茄酱。'),('The children tried to squirt water at one another.','孩子们试着互相喷水。'),sources=S('squirt','squirt'))
W('squirts','英 /skwɜːts/；美 /skwɜːrts/','挤、喷出细流〔第三人称单数〕；一次次喷射、一挤的量〔复数〕',
 '瓶子一捏就喷出细流，用 squirts；挤两次、喷几小股，也可用名词复数数出来。',
 'squirt + -s，/t/ 后读 /s/；动词三单、喷量名词复数同形。',SQUIRT+[['squirt + -s → squirts','它喷细流；他、她挤喷；几小股、几挤']],
 'squirts water 是喷细流的水，two squirts of sauce 是挤两下酱；常把一次动作当小量单位。',
 'squirts out 一挤就喷出；small squirts 几小股短喷。',
 'squirts 这里的量不固定，不像 millilitres 有标准大小；a squirt 说按、挤一次得到的一点量。',
 ('This bottle squirts water in a thin stream.','这个瓶子会喷出一股细水流。'),('Add two small squirts of sauce.','挤两小下酱进去。'),sources=S('squirts','squirt'))
W('squirted','英 /ˈskwɜːtɪd/；美 /ˈskwɜːrtɪd/','挤、喷出细流了；短促喷射了',
 '刚才捏、按一下，把水或酱细细喷出去，用 squirted；也可说液体自己突然成细流喷出。',
 'squirt + 完整 -ed；基础词以 /t/ 结尾，词尾读 /ɪd/，多一个音节。',SQUIRT+[['squirt + -ed → squirted','过去挤喷出短促细流']],
 'squirted water into a cup 是往杯里喷水，squirted out of the bottle 是从瓶中喷出来；方向由 into、out of 等说明。',
 'squirted sauce onto the plate 往盘里挤酱；squirted through the gap 从缝里喷出。',
 'squirted 常一小股、一小次，poured 往往是把液体连续倒出；不只是速度快慢不同。',
 ('He squirted water into the empty cup.','他把水细细喷进空杯子。'),('Tomato sauce squirted out of the bottle.','番茄酱从瓶子里挤喷出来。'),sources=S('squirted','squirt'))
W('squirting','英 /ˈskwɜːtɪŋ/；美 /ˈskwɜːrtɪŋ/','正在挤、喷出细流；短促喷射的过程',
 '液体正一小股、一小股被挤出去，叫 squirting；水枪、挤压瓶、管口都能形成这个动作。',
 'squirt + 完整 -ing，直接加；末尾 rt 已有两个辅音字母，不双写 t。',SQUIRT+[['squirt + -ing → squirting','挤喷短促细流的过程']],
 'squirting water at each other 是互相喷水，squirting sauce onto food 是把酱挤到食物上；不是都成细雾。',
 'water squirting from a pipe 管口喷出的细水流；keep squirting 不停挤喷。',
 'squirting 与 splashing 都能让人湿，但前者常是细流从口喷出，后者常是已有液体被拍起、散开。',
 ('The children were squirting water at each other in the garden.','孩子们在花园里互相喷水。'),('We could see water squirting from a small hole in the hose.','我们看见水从软管的一个小孔里喷出细流。'),sources=S('squirting','squirt'))
def extend_lessons():
 extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_zfe',ROOTS,WORDS)
 extend_lessons()
