"""Dabbing, blotting, scuffing, staining and sprawling outward."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
def S(word,base):
 return ['https://en.wiktionary.org/wiki/'+word+'#English','https://www.etymonline.com/word/'+base]
EXISTING_ROOT_ADDITIONS={
 'C0030':dict(words='daub daubs daubed daubing'.split(),label='daub 经法语灰泥、粉刷材料的可能远源',note='daub 借古法语 dauber，或上溯拉丁语 dealbare 涂白、albus 白；远源有不确定性，不把今天所有涂抹都解释成白色。'),
 'A2238':dict(words='dab dabble dabbles dabbled dabbling'.split(),label='dabble：反复轻触到浅浅涉入',note='dabble 可能是 dab 的旧反复形式，也有相关语言影响分析；小量、多次接触的画面扩到业余涉猎。'),
 'B3516':dict(words='rub rubs rubbed'.split(),label='rub：来回摩擦、擦掉与影响',note='rub 的更远来源未定，现代 rubbed 双写 b 加完整 -ed；rub off、rub it in、rub someone the wrong way 等按完整搭配理解。'),
 'B4358':dict(words='shove scuff scuffs scuffed scuffing'.split(),label='scuff 与推移材料的可能历史联系',note='scuff 最初见于苏格兰拖脚走，来源可能混合，或借北欧推移材料，与 shove 可比较；磨蹭表面义后来发展，不是现代 shove 的规则改写。'),
 'A1782':dict(words='stain stains stained staining'.split(),label='stainless 周围的 stain 基础动作',note='stains、stained、staining 在此给既有 stainless 词族补基础语境，自身不含 -less；染色、弄脏有多条材料合流。'),
 'A1699':dict(words='splotch splotches splotchy'.split(),label='splotchy：一块块斑痕的外观',note='splotch 的更早形成未定，可能受 spot、blot、botch 等影响；现代 splotch + 完整 -y 描写一块块不均匀斑色。'),
 'A1760':dict(words='daub daubs daubed daubing blot blots blotted blotting dabble dabbles dabbled dabbling rub rubs rubbed scuff scuffs scuffed scuffing stain stains stained staining sprawl sprawls sprawled sprawling'.split(),label='抹、吸干、浅涉、磨蹭、染色和摊开的变化',note='blotted 的 -ed 读 /ɪd/；scuffed 读 /t/；daubed、dabbled、rubbed、stained、sprawled 读 /d/。blot、rub 的相应形式双写末辅音。'),
}
DAUB=[['古法语 dauber 粉刷、抹灰泥 → 英语 daub','更远或接拉丁语 dealbare 涂白，具体远源未定'],['抹软黏物 → 粗略涂色；乱涂画作','现代可中性说抹上，也可评价涂得厚、随意或不高明']]
W('daub','英 /dɔːb/；美 /dɔːb/','涂抹、抹上；乱涂；一块涂抹物、拙劣画作',
 '泥灰、厚颜料一块块抹到表面，是 daub。说一幅画 a daub，则像嫌它只把颜色糊上去，是对画作的贬评。',
 '借古法语 dauber 的粉刷、抹灰泥义，更远可能接拉丁语 dealbare 涂白；现代可抹各种颜色，不限定白色。',DAUB,
 'daub paint on a wall 是把颜料抹上墙，a daub of colour 是一抹颜色；call a painting a daub 是嫌画得差。',
 'daub with mud 抹上泥；daubed lettering 涂写的字迹。',
 'daub 常有厚、粗略、随手涂的感觉，dab 更像轻点一下；涂一大块泥与点一点颜色，动作范围不同。',
 ('He used a brush to daub blue paint onto the board.','他用刷子往木板上抹蓝漆。'),('She added a daub of red in the corner of the picture.','她在画角添了一抹红色。'),sources=S('daub','daub'))
W('daubs','英 /dɔːbz/；美 /dɔːbz/','涂抹、乱涂〔第三人称单数〕；几块涂抹物、拙劣画作〔复数〕',
 '一个人把颜色一块块抹上去，动词用 daubs；画上几块厚颜料，又可用名词复数来数。',
 'daub + -s，/b/ 后读 /z/；动词三单与涂抹块、乱涂画作名词复数同形。',DAUB+[['daub + -s → daubs','他、她抹涂；几块颜色或几幅拙画']],
 'daubs paint onto canvas 是在画布上抹色，daubs of colour 是一块块颜色；画作名词通常带嫌画得差的语气。',
 'thick daubs of paint 厚厚几块颜料；daubs the wall with colour 往墙上抹色。',
 'daubs 作为几块颜色可以只描述笔触，作为整幅画的称呼则常是贬评；不能每次看到复数就译成烂画。',
 ('She daubs paint onto the canvas with a broad brush.','她用宽刷子往画布上抹颜料。'),('Thick daubs of yellow covered part of the board.','厚厚几块黄色颜料盖住了木板的一部分。'),sources=S('daubs','daub'))
W('daubed','英 /dɔːbd/；美 /dɔːbd/','涂抹、乱涂了；抹着厚色、泥等的',
 '刚才在表面抹了一片泥或厚颜色，是 daubed；大字粗粗涂在墙上，也可用这种写法。',
 'daub + 完整 -ed，/b/ 后读 /d/；au 是长元音拼写，直接加，不双写 b。',DAUB+[['daub + -ed → daubed','过去抹上软黏材料或粗略涂色']],
 'daubed with paint 是抹着漆，daubed on the wall 是涂写在墙上；with 后说材料，on 后说落在哪里。',
 'daubed in red 用红色涂写；daubed with mud 抹着泥。',
 'daubed 的长元音和单 b，与 dabbed 的短元音、双 b 分开；dabbed 更像轻点，daubed 更像涂抹。',
 ('The wall was daubed with bright colours.','墙上被抹上鲜亮颜色。'),('Someone had daubed large letters on the fence.','有人在围栏上粗粗涂了几个大字。'),sources=S('daubed','daub'))
W('daubing','英 /ˈdɔːbɪŋ/；美 /ˈdɔːbɪŋ/','正在涂抹、粗略涂色、乱画；涂抹活动',
 '刷子或手正把颜料、泥灰摊到表面，是 daubing；更像一块一块糊上去，不太强调精细勾线。',
 'daub + 完整 -ing，直接加；基础 au、单 b 保留，分词和动作名词同形。',DAUB+[['daub + -ing → daubing','厚色、软黏物涂抹的过程']],
 'daubing paint on a board 是往板上抹漆，daubing the wall with colour 是往墙上抹色；也能评价业余乱涂。',
 'daubing with a brush 用刷子抹；messy daubing 乱糊色块。',
 'daubing 着重涂色的块、抹，sketching 着重少量线条的轮廓；同一次画画可以先勾线，再厚涂颜色。',
 ('The children were daubing paint onto large sheets of paper.','孩子们正往大纸上涂抹颜料。'),('He spent the afternoon daubing colour over the old board.','他整个下午都在旧木板上涂抹颜色。'),sources=S('daubing','daub'))
BLOT=[['中古英语 blot 墨斑、污点名词','可能接北欧污斑材料，也有法语等分析，来源未定；道德污点义较早已见'],['污斑名词 → 弄花、涂掉；后有吸干、遮住等用法','blot out 像盖上一片让原物看不见，blot up 则用吸水材料取走湿迹']]
W('blot','英 /blɒt/；美 /blɑːt/','墨斑、污点；吸干、吸去；涂掉；〔blot out〕遮住、抹掉',
 '纸上落了一团墨，是 a blot；纸巾按上水迹吸走，是 blot it up。blot out 又像用黑块盖住，让字、景物或记忆看不见。',
 '较早名词说墨斑、污点，远源未定，北欧、法语等有不同分析；相应动词后来发展，吸干、涂掉等按搭配分别理解。',BLOT,
 'an ink blot 是墨斑，blot the paper dry 是把纸吸干；clouds blot out the sun 是云遮住太阳，a blot on a record 是记录中的污点。',
 'blot up a spill 吸去洒出的液体；blot out a memory 抹去一段记忆。',
 'blot 吸水时多像按上材料让水进入，wipe 常是横着擦；同样让表面干，动作轨迹不同。',
 ('An ink blot spread across the corner of the page.','一团墨斑在页角洇开。'),('Use the paper towel to blot up the water.','用厨房纸把水吸起来。'),sources=S('blot','blot'))
W('blots','英 /blɒts/；美 /blɑːts/','墨斑、污点〔复数〕；吸干、涂掉、遮住〔第三人称单数〕',
 '纸上几团墨，是 blots；一个人拿纸轻按湿处，或一大片影子遮住景物，动词三单也叫 blots。',
 'blot + -s，/t/ 后读 /s/，结尾 /ts/；名词复数与动词三单同形，基本拼写不双写 t。',BLOT+[['blot + -s → blots','几团污痕；它吸去、遮掉']],
 'ink blots 是墨斑，blots the surface dry 是把表面吸干；blots out the view 是挡住视野，out 一起带遮盖义。',
 'blots on the page 纸上污点；blots out the sun 遮住太阳。',
 'blots out 常像一大片盖住、抹掉，covers 更宽；一张透明膜 covers 也可以仍看得清，未必 blot out。',
 ('The old page was covered with ink blots.','旧书页上满是墨斑。'),('The huge sign blots out the view from the window.','巨大的招牌挡住了窗外景色。'),sources=S('blots','blot'))
W('blotted','英 /ˈblɒtɪd/；美 /ˈblɑːtɪd/','吸干、吸去、涂掉、遮住了；带墨斑的',
 '刚才纸巾按上去，水被吸走，是 blotted；名字被黑线涂掉、太阳被云遮住，也能用 blotted out。',
 'blot 双写 t + 完整 -ed → blotted，/t/ 后读 /ɪd/，多一个音节。',BLOT+[['blot 双写 t + -ed → blotted','过去吸去、弄花或盖掉']],
 'blotted the spill 是吸掉洒出的水，blotted out the name 是涂掉名字；was blotted with ink 又可说留下墨点。',
 'blotted dry 轻按吸干了；blotted out the light 遮住光线了。',
 'blotted out a word 常是把它盖到看不见，crossed out 则可能划一条线、原字仍可辨；删改痕迹不同。',
 ('She blotted the wet page with a clean cloth.','她用干净布轻按湿书页，吸去水分。'),('Dark clouds blotted out the sun.','乌云遮住了太阳。'),sources=S('blotted','blot'))
W('blotting','英 /ˈblɒtɪŋ/；美 /ˈblɑːtɪŋ/','正在吸干、吸去、遮住、涂掉；吸水动作',
 '吸水纸正按着湿墨、水迹，是 blotting；一片云正把光吞掉，也像在把原来可见的东西盖过去。',
 'blot 双写 t + 完整 -ing → blotting；分词、动作名词同形，双写不增加一个 /t/ 音。',BLOT+[['blot 双写 t + -ing → blotting','吸水或遮去的过程']],
 'blotting paper 是吸墨纸，blotting up the liquid 是正吸走液体；blotting out the light 是遮光。',
 'blotting gently 轻按吸干；blotting the page dry 吸干纸面。',
 'blotting paper 的名字说用途，不表示那张纸本来就是污点；它通过吸收把未干墨迹取走。',
 ('He used blotting paper to absorb the excess ink.','他用吸墨纸吸掉多余墨水。'),('A cloud was blotting out the moon.','一片云正遮住月亮。'),sources=S('blotting','blot'))
DABBLE=[['dab 一系的轻触 + 旧反复动作形式 → dabble','可能从小量、多次浸碰、拨水材料形成，也有邻近语言影响分析'],['反复浅浅碰水 → 业余试着做、涉猎','像把脚尖探进水里玩一点，还没把整个学习、职业投入进去']]
W('dabbles','/ˈdæbəlz/','浅涉、业余玩一点；拨水〔第三人称单数〕',
 '一个人平时画一点、偶尔写一点，没把它当主要工作，是 dabbles in it。像手只在浅水里拨一拨，接触了一点。',
 'dabble + -s，/l/ 后读 /z/；基础可能接 dab 的旧反复形式，现代三单直接加 s。',DABBLE+[['dabble + -s → dabbles','他、她业余涉猎、浅浅接触']],
 'dabbles in painting 是业余画一点，dabbles in photography 是玩一点摄影；水的用法可接 in、with，具体看对象。',
 'dabbles in several hobbies 业余试几种爱好；dabbles her fingers in the water 用手指拨水。',
 'dabbles in 不保证做得差，只说投入较随意、不是专业主业；studies 可以更系统，也可以只说学习。',
 ('She dabbles in photography at weekends.','她周末业余玩一点摄影。'),('He dabbles in several hobbies without choosing just one.','他试着玩几种爱好，没有只选定一种。'),sources=S('dabbles','dabble'))
W('dabbled','/ˈdæbəld/','业余试过、浅涉过；拨弄水了',
 '以前偶尔画过、试过一点某个领域，是 dabbled in；它不像多年主修，更像一度把脚尖探进水里。',
 'dabble 去末尾 e + 完整 -ed → dabbled，/l/ 后读 /d/；基础双 b 保留。',DABBLE+[['dabble 去 e + -ed → dabbled','过去小量接触、业余试做']],
 'dabbled in pottery 是玩过一点陶艺，dabbled in poetry 是业余写过诗；dabbled her fingers in the pool 是用手指拨过池水。',
 'briefly dabbled 短暂涉猎过；dabbled in music 业余玩过音乐。',
 'dabbled in 常适合轻描淡写地说试过，不等于完全学会；mastered 则明确达到熟练掌握。',
 ('I dabbled in pottery for a while.','我曾有一阵子业余玩过陶艺。'),('She dabbled her fingers in the cool water.','她用手指拨了拨凉水。'),sources=S('dabbled','dabble'))
W('dabbling','/ˈdæbəlɪŋ/','正在浅涉、业余试做、拨水；浅浅接触',
 '闲时试试陶艺、画画，像在水边浅浅玩一下，是 dabbling。这里强调投入方式轻、范围浅，并不自动贬低兴趣。',
 'dabble 去末尾 e + 完整 -ing → dabbling；双 b 保留，分词和动作名词同形。',DABBLE+[['dabble 去 e + -ing → dabbling','随意、小量试做的过程']],
 'dabbling in photography 是正业余玩摄影，dabbling in the water 是拨水、浅玩水；后面的领域或对象决定场景。',
 'start dabbling in something 开始业余试做某事；a bit of dabbling 一点浅尝。',
 'dabbling 常说没有全面投入，experimenting 更强调试验、探索结果；两者可重叠，但后者也可以很系统。',
 ('He has been dabbling in watercolour painting.','他最近一直在业余试着画水彩。'),('She relaxed by dabbling her fingers in the stream.','她把手指伸进溪水里拨了拨，放松下来。'),sources=S('dabbling','dabble'))
RUB=[['中古英语 rubben → rub','与德荷、北欧擦刮词形可比较，更远来源未定'],['表面摩擦 → 擦去、抹进；影响、惹恼等搭配','现代看 off、in、against 等小词，摩擦的画面会带到不同结果']]
W('rubs','/rʌbz/','擦、搓、摩擦〔第三人称单数〕；摩擦、揉擦〔复数〕',
 '一个人来回搓手取暖，或鞋不停磨到脚，用 rubs。rub off on someone 又像一种颜色擦到别人身上，表示习惯、情绪影响对方。',
 'rub + -s，/b/ 后读 /z/；三单与揉擦名词复数同形，基础单 b 保留。',RUB+[['rub + -s → rubs','他、她摩擦；几下揉擦']],
 'rubs his hands together 是搓双手，rubs against the skin 是磨皮肤；enthusiasm rubs off on others 是热情感染别人。',
 'rubs it clean 擦干净；rubs me the wrong way 让我不舒服、惹我不快。',
 'rubs 往往来回接触，dabs 是轻点后抬开；rub off on 的影响义又要把 off on 一起记。',
 ('He rubs his hands together to warm them.','他搓着双手取暖。'),('Her enthusiasm rubs off on everyone around her.','她的热情感染了周围每个人。'),sources=S('rubs','rub'))
W('rubbed','/rʌbd/','擦、搓、摩擦了；擦掉、抹入了',
 '刚才手在表面来回擦、把双手搓热，是 rubbed；某句话让人不快，也像不合适地磨到了人。',
 'rub 双写 b + 完整 -ed → rubbed，/b/ 后读 /d/；短元音重读单音节按规则双写。',RUB+[['rub 双写 b + -ed → rubbed','过去摩擦、搓动及相关搭配']],
 'rubbed his hands together 是搓了搓手，rubbed the mark off 是擦掉痕；rubbed me the wrong way 是惹得我不舒服。',
 'rubbed dry 擦干了；rubbed it in 反复提人难处、让人更难受。',
 'rubbed off 常是被擦掉，rubbed off on someone 则是影响别人；多了 on 和人物对象，搭配方向就变了。',
 ('She rubbed the mark off the desk.','她把桌上的痕迹擦掉了。'),('His dismissive tone rubbed me the wrong way.','他那轻慢的语气让我很不舒服。'),sources=S('rubbed','rub'))
SCUFF=[['较早苏格兰 scuff 的拖脚走法 → scuff','来源可能混合，或接北欧推移材料，更远可与 shove 比较'],['鞋底磨过地面 → 表面磨损、蹭出痕','现代鞋面、地板都能因擦碰留下不深但显眼的痕']]
W('scuff','/skʌf/','磨蹭、蹭坏表面；拖脚走；磨痕、蹭痕',
 '鞋尖蹭上台阶，皮面留下一块灰白痕，是 scuff；脚不抬高、鞋底擦着地走，也保留拖脚的动作。',
 '较早见于苏格兰拖脚走的用法，来源未定，可能有北欧与推移材料。表面被擦坏、留痕义后来发展。',SCUFF,
 'scuff your shoes 是把鞋面蹭出痕，a scuff on the floor 是地板蹭痕；scuff along 是拖着脚走。',
 'scuff marks 磨蹭痕；scuff easily 容易蹭坏。',
 'scuff 常是表面磨蹭、不很深的痕，scratch 可是尖物划出的线；走过粗地面与被钥匙划过，痕迹感觉不同。',
 ('There was a pale scuff on the toe of the shoe.','鞋尖有一块浅色蹭痕。'),('Try not to scuff the polished floor with the chair legs.','挪椅子时尽量别让椅腿把抛光地板蹭花。'),sources=S('scuff','scuff'))
W('scuffs','/skʌfs/','磨蹭、蹭出痕、拖脚走〔第三人称单数〕；蹭痕〔复数〕',
 '一双鞋老是被蹭花，或一个人鞋底贴地磨着走，动词可用 scuffs；鞋面几个灰白磨痕则是名词复数。',
 'scuff + -s，/f/ 后读 /s/；名词复数通常直接 scuffs，f 不变为 ves。',SCUFF+[['scuff + -s → scuffs','它磨蹭、留痕；几块蹭痕']],
 'scuffs the floor 是把地板蹭出痕，scuffs his feet 是拖着脚擦地；scuffs on the leather 是皮面蹭痕。',
 'minor scuffs 小蹭痕；scuffs easily 容易被蹭花。',
 'scuffs 是一种表面痕迹，dirt 可以是附在表面的灰；擦掉灰不一定能把磨损的 scuffs 也还原。',
 ('This soft leather scuffs easily.','这种软皮很容易被蹭花。'),('The old suitcase had scuffs around the corners.','旧行李箱的几个角上有蹭痕。'),sources=S('scuffs','scuff'))
W('scuffed','/skʌft/','磨蹭、蹭坏了；表面磨花的；拖着脚走了',
 '鞋尖、箱角已被粗糙表面蹭掉一点光泽，叫 scuffed；看起来旧，却不一定破出一个洞。',
 'scuff + 完整 -ed，/f/ 后读 /t/；原有双 f 保留，直接加词尾。',SCUFF+[['scuff + -ed → scuffed','过去磨蹭；表面已留磨痕']],
 'scuffed shoes 是鞋面磨花的鞋，scuffed the floor 是蹭花地板；scuffed along the pavement 是拖脚沿人行道走。',
 'scuffed at the toes 鞋尖磨花；slightly scuffed 略有蹭痕。',
 'scuffed 常只说表面外观受磨，torn 是撕裂、破开；一只旧包可以 scuffed 而布料仍完整。',
 ('His shoes were scuffed at the toes.','他的鞋尖已经磨花了。'),('The chair legs scuffed the wooden floor.','椅腿把木地板蹭出了痕。'),sources=S('scuffed','scuff'))
W('scuffing','/ˈskʌfɪŋ/','正在磨蹭、蹭坏表面、拖脚走；表面磨损',
 '鞋底正擦着地面走，或椅腿正把地板磨出浅痕，是 scuffing；可以描述动作，也可把一片表面磨损当整体。',
 'scuff + 完整 -ing，直接加；原有 ff 保留，分词和动作名词同形。',SCUFF+[['scuff + -ing → scuffing','磨蹭过程；留下的表面磨损']],
 'scuffing the floor 是正蹭花地板，scuffing along 是拖脚走；some scuffing 是一些磨蹭损伤。',
 'scuffing at the corners 角落磨损；scuffing his feet 拖脚擦地。',
 'scuffing 关注擦碰、留痕，polishing 关注擦亮、使表面光洁；两者都有摩擦，却给表面不同结果。',
 ('He walked away, scuffing his feet along the path.','他拖着脚沿小路走开了。'),('There was some scuffing around the corners of the case.','箱角周围有些磨蹭损伤。'),sources=S('scuffing','scuff'))
STAIN=[['北欧 steina 染色材料与经法语来的 disteynen 等合流 → stain','染色、失色、弄脏的不同旧用法汇入同一现代词'],['改变颜色 → 污渍；有意染木、彩色玻璃；名声污点','现代看颜色是不是有意加上，不把所有 stain 都看成失败、脏']]
W('stains','/steɪnz/','污渍、染色剂、名誉污点〔复数〕；染色、留下污渍〔第三人称单数〕',
 '衣服上几块洗不掉的颜色，是 stains；一种果汁染到桌布，也可 it stains。木工染色剂同样改变颜色，却是有意求效果。',
 'stain + -s，/n/ 后读 /z/；动词三单与污渍、染料等名词复数同形，基础涉及北欧与法语材料合流。',STAIN+[['stain + -s → stains','它染色；几块污渍或几种染色剂']],
 'coffee stains 是咖啡渍，stains the fabric 是把布染色；wood stains 是木材染色剂，未必指木头脏了。',
 'stains easily 容易留下污渍；stains on a reputation 名誉污点。',
 'stains 常像颜色留在材料里，smears 常像软物在表面拖开成痕；有些污渍要洗，有些油痕一擦就掉，形状和附着方式不同。',
 ('The tablecloth had several coffee stains.','桌布上有几块咖啡渍。'),('Beetroot juice stains the fabric a deep red.','甜菜汁把布染成深红色。'),sources=S('stains','stain'))
W('stained','/steɪnd/','染色、沾污了；带污渍的；有色彩的',
 '衬衫染上咖啡色，是 stained；窗上的 stained glass 却是有意做出的彩色玻璃。关键看颜色被当作污渍还是设计。',
 'stain + 完整 -ed，/n/ 后读 /d/；过去式、过去分词和染色状态形容词同形。',STAIN+[['stain + -ed → stained','颜色已改变；可以污损，也可以有意染色']],
 'stained with ink 是沾上墨，stained glass 是彩色玻璃；stained the wood dark brown 是把木头染成深棕色。',
 'a stained shirt 有污渍的衬衫；reputation stained by lies 被谎言弄脏的名声。',
 'stained glass 里的 stained 是有色、染色，不等于 dirty glass 脏玻璃；一个固定搭配就能显示这个词不只负面。',
 ('Her sleeve was stained with coffee.','她的袖子沾上了咖啡渍。'),('Sunlight shone through the stained glass.','阳光透过彩色玻璃照进来。'),sources=S('stained','stain'))
W('staining','/ˈsteɪnɪŋ/','正在染色、留下污渍；染色处理、污渍形成',
 '木头正在吸进染色剂，或饮料正把布变色，是 staining。动作都是颜色进入、留住，效果好坏要看是不是有意。',
 'stain + 完整 -ing，直接加；分词、动作名词同形，基础 ai 长元音不改。',STAIN+[['stain + -ing → staining','使材料变色、留色的过程']],
 'staining wood 是给木材染色，prevent staining 是防止留污渍；staining the cloth 是把布染上颜色。',
 'wood staining 木材染色；staining around the edge 边缘的色渍。',
 'staining 与 painting 都能加颜色，staining 常让木纹等基底仍透出，painting 更常覆盖表面；具体材料、效果仍看场景。',
 ('They spent the afternoon staining the wooden shelves.','他们整个下午都在给木架染色。'),('The dark liquid was staining the white cloth.','深色液体正把白布染上颜色。'),sources=S('staining','stain'))
SPLOTCH=[['近代 splotch 的大片不规则斑痕名词','可能受 spot、blot、botch 等影响，旧 splott 也可比较，形成未定'],['不规则色块 → splotchy 的斑驳外观','现代按形状看：颜色不均、成片分布，不是整面一致']]
W('splotch','英 /splɒtʃ/；美 /splɑːtʃ/','一大片不规则斑痕、色块；使留下斑块',
 '颜料啪地落下，不是一个整齐小圆点，而是一块边缘歪歪的颜色，是 splotch。大小没有固定尺度，重点是块状、不规则。',
 '近代英语已有斑块名词，可能混合或受 spot、blot、botch 等影响，确切形成未定；相应动词较晚出现。',SPLOTCH,
 'a splotch of paint 是一块不规则颜料痕，a dark splotch 是一片暗斑；可说污痕，也可说画面中的色块。',
 'a green splotch 一块绿色；leave a splotch 留下一块不规则痕。',
 'splotch 通常比 dot 更像边缘不规整的块，dot 常是小点；spot 范围更宽，不保证一定圆或一定小。',
 ('A large splotch of blue paint marked the floor.','地板上留着一大块不规则蓝漆痕。'),('She added a green splotch to the abstract picture.','她在抽象画里添了一块不规则绿色。'),sources=S('splotch','splotch'))
W('splotches','英 /ˈsplɒtʃɪz/；美 /ˈsplɑːtʃɪz/','一块块斑痕、色块〔复数〕；留下斑块〔第三人称单数〕',
 '布上、纸上这儿一块那儿一块不均匀的颜色，是 splotches；像颜色没铺平，被分成许多不规则小区域。',
 'splotch + -es，/tʃ/ 后读 /ɪz/；常见名词复数，相应动词三单也同形。',SPLOTCH+[['splotch + -es → splotches','多块不规则斑痕；它留下斑块']],
 'splotches of colour 是一块块颜色，paint splotches 是颜料斑痕；covered in splotches 是布着这些斑块。',
 'dark splotches 一片片暗斑；splotches on the canvas 画布上的块状颜色。',
 'splotches 强调不规则块状，stripes 则像长条；点、条、块都能装饰画面，名称帮你看清外形。',
 ('The cloth was covered with splotches of paint.','布上沾满了一块块不规则颜料痕。'),('Dark splotches appeared as the paper soaked up the water.','纸吸进水后，出现了一片片暗色斑块。'),sources=S('splotches','splotch'))
W('splotchy','英 /ˈsplɒtʃi/；美 /ˈsplɑːtʃi/','斑驳的、颜色一块块不均匀的',
 '涂色没铺匀，有的地方深、有的地方浅，像散着一块块色斑，是 splotchy。说的是外观，不自动说明原因。',
 'splotch + 完整 -y → splotchy，表示带有这种不规则斑块的性质；ch 保留 /tʃ/。',SPLOTCH+[['splotch + -y → splotchy','颜色、痕迹呈不规则块状分布']],
 'splotchy paint 是斑驳不匀的漆，a splotchy surface 是色块不均的表面；衣物、纸面、肤色都可作对象。',
 'a splotchy finish 不均匀的涂装；look splotchy 看起来一块块斑驳。',
 'splotchy 强调斑块分布，faded 强调颜色变淡；褪色可以整片均匀，也可以出现斑块，两种描述不互相代替。',
 ('The paint dried with a splotchy finish.','漆干后呈现斑驳不匀的表面。'),('The old photograph looked faded and splotchy.','旧照片看起来褪色了，还一块块斑驳不均。'),sources=S('splotchy','splotch'))
SPRAWL=[['古英语 spreawlian → 中古英语 spraulen → sprawl','较早是手脚剧烈活动，后有四散伸开的义；更远同源分析仍有推测'],['四肢伸开 → 建筑、城市等向外铺展','现代身体可松散摊开，城市也像没收紧边界而向周围摊开']]
W('sprawl','英 /sprɔːl/；美 /sprɔːl/','摊开四肢坐卧；向外铺展、蔓延；摊开姿态、城市蔓延',
 '回家一累，胳膊腿伸开占满沙发，是 sprawl。城市不紧凑，一片片往郊外铺过去，也像摊开的身体。',
 '承古英语 spreawlian 的手脚活动材料，经中古英语延续；伸展开来的义较早发展，城市蔓延名词义则是较晚的现代用法。',SPRAWL,
 'sprawl on the sofa 是摊在沙发上，sprawl across the valley 是铺展整个山谷；urban sprawl 是城市向周边蔓延。',
 'sprawl out 伸展开来；a sprawl of suburbs 一大片向外铺开的郊区。',
 'sprawl 比 lie 更强调四肢散开、占空间，城市用法也常带松散外扩；一块紧凑街区不必有 sprawl 的外观。',
 ('He liked to sprawl on the sofa after work.','他喜欢下班后摊在沙发上。'),('The town was struggling with urban sprawl.','小镇正为不断向外蔓延的城区发愁。'),sources=S('sprawl','sprawl'))
W('sprawls','英 /sprɔːlz/；美 /sprɔːlz/','摊开坐卧；向外铺展〔第三人称单数〕；摊开物、蔓延区域〔复数〕',
 '一个人手脚伸开占了大半张床，用 sprawls；城市、建筑散着铺过一片地，也能这样写。',
 'sprawl + -s，/l/ 后读 /z/；三单与少见一些的蔓延区域名词复数同形，常用优先记动词。',SPRAWL+[['sprawl + -s → sprawls','他、她摊开；它四散铺展']],
 'sprawls across the bed 是摊满床面，sprawls over the hillside 是沿山坡铺开；主语可以人，也可以城镇建筑。',
 'sprawls on the carpet 摊在地毯上；the city sprawls 城市向外散开。',
 'sprawls 常有占地宽、边界松散的画面，extends 只说延伸；一条笔直整齐的走廊也可 extends，却不一定 sprawls。',
 ('He sprawls across the sofa with a book.','他拿着书，四肢摊在沙发上。'),('The city sprawls over the low hills.','城市沿着低矮山丘向外铺展。'),sources=S('sprawls','sprawl'))
W('sprawled','英 /sprɔːld/；美 /sprɔːld/','摊开四肢坐卧了；散着铺展了；摊着的',
 '刚才人整个伸开躺到草地上，或地图上建筑铺成松散一大片，是 sprawled。它不只说在哪里，还说占空间的姿态。',
 'sprawl + 完整 -ed，/l/ 后读 /d/；基础 aw、l 保留，过去式、分词同形。',SPRAWL+[['sprawl + -ed → sprawled','过去摊开；已松散铺展']],
 'sprawled on the bed 是摊在床上，sprawled out on the grass 是手脚伸开躺在草地；sprawled across the plain 是铺过平原。',
 'sat sprawled 坐得手脚散开；sprawled in a chair 伸着手脚摊在椅里。',
 'sprawled 只保证姿态散开，不自动说明睡着；asleep 才说睡眠，人在看书也可以 sprawled on the sofa。',
 ('She lay sprawled on the grass, watching the clouds.','她四肢摊开躺在草地上，看着云。'),('Low houses sprawled across the plain.','低矮房屋松散地铺过平原。'),sources=S('sprawled','sprawl'))
W('sprawling','英 /ˈsprɔːlɪŋ/；美 /ˈsprɔːlɪŋ/','正在摊开、铺展；面积大而松散的、蔓延的',
 '城区一片接一片往外铺，庄园大得翼楼、庭院散开，是 sprawling；也能形容故事线多、铺陈很广的长篇作品。',
 'sprawl + 完整 -ing，直接加；动作分词还常作形容词，突出占地、范围广而不紧凑。',SPRAWL+[['sprawl + -ing → sprawling','散开过程；大范围铺展的性质']],
 'a sprawling city 是铺得很开的城市，a sprawling house 是规模大、布局松散的房子；a sprawling novel 是铺陈广的长篇小说。',
 'sprawling suburbs 不断外扩的郊区；sprawling on the floor 摊在地板上。',
 'sprawling 不只是 large，还带范围散开、分支多的感觉；大而紧凑的一座塔楼也 large，却未必 sprawling。',
 ('They lived in a sprawling old house with many wings.','他们住在一座翼楼很多、铺得很开的旧房子里。'),('The map showed a sprawling network of suburbs.','地图上是一大片向外铺展的郊区网络。'),sources=S('sprawling','sprawl'))

def extend_lessons():
 extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_zft',ROOTS,WORDS)
 extend_lessons()
