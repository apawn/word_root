"""Gawking, squinting, winking and peeking: four different eye actions."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
def S(word,base):
 return ['https://en.wiktionary.org/wiki/'+word+'#English','https://www.etymonline.com/word/'+base]
EXISTING_ROOT_ADDITIONS={
 'B2761':dict(words='look gawk gawks gawked gawking peek peeks peeked peeking'.split(),label='gawk、peek 与 look 的近义动作比较',note='本支是看法、姿态对照，不是把三个基础词认作同源。gawk 来源有多种争论；peek 可能接中古荷兰语等看词，与 peep 关系也有讨论，均不硬连成单一路线。'),
 'B2752':dict(words='eye squint squints squinted squinting'.split(),label='squint：眼睛眯起来和眼位斜向的不同用法',note='这里以眼部动作作场景扩展，不将 squint 说成 eye 的同源派生。squint 从旧 asquint 缩短、转成形容词再作动词，远源未定；现代眯眼动作不自动等于名词的斜视状态。'),
 'B4361':dict(words='blink wink winks winked winking'.split(),label='wink 与 blink：有信号的眨眼和一般眨眼',note='两词在同页按眼睑动作对照，不作彼此直接派生。wink 承古英语 wincian，眨眼示意的记录很早，不能说现代才从普通眨眼发明。'),
}
GAWK=[['十八世纪英语 gawk：呆呆盯着看','来源未定，联系旧 gaw、北欧注意词、拟声构词等分析互有争议'],['呆看 → 好奇地直盯，常带不赞成评价','不因拼写相似就认定从 gaze、gape 或 gawky 单线派生']]
W('gawk','英 /ɡɔːk/；美 /ɡɔːk/','呆呆地盯着看；直勾勾地看热闹',
 '见到新奇东西，人停下来，嘴也顾不上收，直盯着看；旁人觉得这副样子傻、没礼貌，就容易用 gawk。',
 '十八世纪有记录的呆看动词，更早来源有争议。现代整体理解，别把几种相似词的不同推测拼成确定历史。',GAWK,
 'gawk at the display 呆看展品；stop and gawk 停下来直盯着看；常带说话人的不赞成。',
 'gawk at a celebrity；do not gawk。',
 'stare 更一般地说固定注视，gawk 往往额外评价盯得呆、像看热闹；gaze 则较容易写入神。',
 ('People stopped to gawk at the enormous sculpture.','人们停下来，呆呆地看那座巨大的雕塑。'),('Do not gawk at the actors while they are eating.','演员吃饭时，别直勾勾地盯着看。'),sources=S('gawk','gawk'))
W('gawks','英 /ɡɔːks/；美 /ɡɔːks/','呆看、直盯着看热闹〔第三人称单数〕',
 '每次看见奇特的车，他都停下脚步、盯着不动，动词可以用 gawks。它不只是看，还带看呆了的评价。',
 'gawk + -s，/k/ 后词尾读 /s/，结尾 /ks/；基础词来源未定，现代三单按规则加词尾。',GAWK+[['gawk + -s → gawks','他、她呆呆直盯着看']],
 'gawks at the costume 呆看那套服装；gawks through the window 隔窗直盯着看。',
 'stands and gawks；gawks at anything unusual。',
 'gawks 通常不是赞美观察细致；observes carefully 才偏向认真观察的中性、正面描述。',
 ('He gawks at every unusual car that passes.','每有一辆特别的车经过，他都呆呆地盯着看。'),('The child gawks at the giant puppet in the square.','孩子呆看着广场上那个巨大的木偶。'),sources=S('gawks','gawk'))
W('gawked','英 /ɡɔːkt/；美 /ɡɔːkt/','呆呆地盯着看了；直勾勾地看热闹了',
 '刚才看到一个夸张的新造型，大家一下停住、直盯着不放，过去这个动作叫 gawked。',
 'gawk + 完整 -ed，/k/ 后词尾读 /t/，结尾 /kt/；拼写仍保留 ed。',GAWK+[['gawk + -ed → gawked','过去呆看、直盯着看']],
 'gawked at the sight 呆看眼前景象；gawked in amazement 惊奇得直盯着看。',
 'stood and gawked；gawked at us。',
 'gawked 常把看人的姿态评得有些傻或冒犯，admired 则说欣赏；写人物被围观时语气尤其不同。',
 ('We gawked at the enormous cake before anyone cut it.','蛋糕还没切，我们就呆看着它，惊讶于它那么大。'),('Tourists gawked at the unusual building.','游客们直盯着那座奇特建筑看。'),sources=S('gawked','gawk'))
W('gawking','英 /ˈɡɔːkɪŋ/；美 /ˈɡɔːkɪŋ/','正在呆看、直盯着看热闹',
 '人堵在前面，不做别的，就呆呆看着；别人催一句 stop gawking，就是别再看呆着不动了。',
 'gawk + -ing，基础 k 保留；既可作进行形式，也可把呆看这种行为提出来说。',GAWK+[['gawk + -ing → gawking','呆看、围观的过程']],
 'gawking at the scene 呆看现场；a crowd gawking through the window 一群隔窗看热闹的人。',
 'stop gawking；gawking tourists。',
 'gawking 不是一般所有观看行为的名称；它带的呆看、看热闹语气，需要场景支持。',
 ('Stop gawking and help me carry the box.','别看呆着了，来帮我搬箱子。'),('A small crowd was gawking through the shop window.','一小群人正隔着商店橱窗直勾勾地看。'),sources=S('gawking','gawk'))
SQUINT=[['旧副词 asquint 斜向地 → 缩短 squint 形容词','更早来源未定，有荷兰语斜坡、倾斜材料等比较分析'],['形容眼位斜向 → 动词、名词用法','现代动词常说为了看清或避强光而眯眼；名词也可指斜视，不能一概而论']]
W('squint','/skwɪnt/','眯着眼看；斜视；斜视状态；瞥一眼',
 '太阳太亮，或远处字太小，眼睛收成一条缝去看，这叫 squint。名词 a squint 在另一常见场景里则说眼位斜向的状态。',
 '从 asquint 缩短的形容词再发展出动词、名词；更早来路未定。现代先按句子判断眯眼动作、眼位状态还是一瞥。',SQUINT,
 'squint at the small print 眯眼看小字；squint in the sun 在阳光下眯眼；have a squint 名词常说斜视状态。',
 'take a squint at something 口语里瞧一眼；squint through the glare。',
 'squint 让人看到眼睛收窄或斜向的样子；peer 更强调努力看清，未必明确写眯眼。',
 ('I had to squint to read the distant sign.','我得眯起眼，才能看清远处的牌子。'),('She raised a hand to block the sun and began to squint.','她抬手挡太阳，开始眯起眼看。'),sources=S('squint','squint'))
W('squints','/skwɪnts/','眯眼看、斜视〔第三人称单数〕；斜视、一瞥〔复数〕',
 '一走到太阳下，她眼睛就收小；看远处的小字，也眯着看，动词用 squints。名词复数则需另按眼位或一瞥场景理解。',
 'squint + -s，/t/ 后词尾读 /s/，结尾 /nts/；动词三单和名词复数同形。',SQUINT+[['squint + -s → squints','他、她眯眼或斜向看；名词的多个状态、几瞥']],
 'squints at the screen 眯眼看屏幕；squints into the sunlight 朝着阳光眯眼。',
 'squints through the glass；squints to make out the letters。',
 'squints at a screen 可以只是当时为了看清而眯眼，不能直接当成名词 a squint 所说的持续眼位状态。',
 ('He squints at the tiny numbers on the display.','他眯起眼，看显示屏上那些小数字。'),('She always squints when she steps into bright sunlight.','她一走到强烈阳光下，总会眯起眼睛。'),sources=S('squints','squint'))
W('squinted','/ˈskwɪntɪd/','眯眼看了；斜眼看了',
 '刚才为了辨出远处的人影，眼睛收小一点、努力往前看，可以说 squinted。',
 'squint + 完整 -ed，基础 /t/ 后词尾读 /ɪd/；不是所有含 nt 的过去式都能省掉这个音节。',SQUINT+[['squint + -ed → squinted','过去把眼睛收窄、斜向地看']],
 'squinted at the label 眯眼看标签；squinted into the distance 眯眼望远处。',
 'squinted through the glare；squinted to read。',
 'squinted 写眼睛的动作，glanced 写看得短；一个人可以眯眼看很久，不一定是一瞥。',
 ('She squinted at the label, trying to read the faded date.','她眯眼看标签，想辨出褪色的日期。'),('We squinted into the bright light.','我们迎着强光眯起眼看。'),sources=S('squinted','squint'))
W('squinting','/ˈskwɪntɪŋ/','正在眯眼、斜眼看；眯着眼的',
 '眼睛还收着，头朝前，人在努力辨认一个不容易看清的东西，叫 squinting。',
 'squint + -ing；动作形式也能直接修饰人、眼睛，眼位状态义仍按名词、语境另辨。',SQUINT+[['squint + -ing → squinting','眯眼、斜向看的过程或姿态']],
 'squinting at a map 眯眼看地图；squinting in the glare 在强光里眯眼；squinting to see better 为看清而眯眼。',
 'without squinting 不用眯眼；stood squinting into the distance。',
 'squinting 更明确写眼部动作；looking carefully 只说看得仔细，未必需要眯起眼睛。',
 ('He stood squinting at the distant boat.','他站着眯眼看远处的船。'),('The print was large enough to read without squinting.','字足够大，不用眯眼也能读。'),sources=S('squinting','squint'))
WINK=[['古英语 wincian → 中古英语 winken → wink','闭眼、眨眼材料；眨一眼示意的用法也已有很早记录'],['眼睑一开一合 → 示意；灯光闪动；闭眼又联系短睡','现代单眼示意很常见，sleep a wink、forty winks 则保留短睡的固定说法']]
W('wink','/wɪŋk/','眨一只眼示意；闪烁；一次眨眼；片刻睡眠',
 '有句话不方便当面说，就对同伴眨一只眼，让他心领神会，这叫 wink。小灯一闪一灭也像在眨眼。',
 '承古英语 wincian，眨眼示意的记录很早；现代名词一次眨眼、短睡和动词闪动按各自场景理解。',WINK,
 'wink at someone 向某人眨眼示意；give someone a wink 给某人一个眼色；not sleep a wink 一点也没睡。',
 'forty winks 打个盹；a light winks 一盏灯在闪。',
 'blink 常是普通、不自觉的眨眼，wink 多为单眼传信号；wink at a fault 又能比喻对过错睁一只眼闭一只眼。',
 ('She gave me a wink to show that she was joking.','她向我眨了下眼，表示自己在开玩笑。'),('I did not sleep a wink last night.','我昨晚一点也没睡。'),sources=S('wink','wink'))
W('winks','/wɪŋks/','眨眼示意、闪烁〔第三人称单数〕；眨眼〔复数〕；短睡',
 '他讲完玩笑，朝你眨一下眼，动词用 winks；forty winks 则是闭会儿眼、打个盹，不是要数四十下。',
 'wink + -s，/k/ 后词尾读 /s/，结尾 /ŋks/；名词复数和动词三单同形。',WINK+[['wink + -s → winks','他、她眨眼示意；几次眨眼，或固定说法里的短睡']],
 'winks at me 向我眨眼；forty winks 小睡一会；exchanges winks 互相递眼色。',
 'the indicator winks 指示灯闪动；a few knowing winks 几个心照不宣的眼色。',
 'forty winks 是固定的短睡表达，不能按字面理解成必须眨四十次眼；winks 的普通动作义仍是一次次眨眼。',
 ('He winks whenever he is about to tell a joke.','他每次准备讲笑话时，都会眨一下眼。'),('I might catch forty winks before dinner.','晚饭前，我可能打个盹。'),sources=S('winks','wink'))
W('winked','/wɪŋkt/','眨眼示意了；闪动了；对过错睁一只眼闭一只眼了',
 '刚才对方看你一眼、闭一下单眼，像在传一个小暗号，就用 winked；灯也可以一闪作为提示。',
 'wink + 完整 -ed，/k/ 后词尾读 /t/，结尾 /ŋkt/；/k/ 不省掉。',WINK+[['wink + -ed → winked','过去眨眼、闪动；也有对过错故意不追究的用法']],
 'winked at me 向我眨眼；winked out 闪了闪熄灭；winked at the mistake 对错误睁一只眼闭一只眼。',
 'winked and smiled；a light winked in the distance。',
 'winked at someone 多是向人递眼色；winked at a fault 则是故意不追究，宾语从人变成过错，义项随之改变。',
 ('She winked at me across the table.','她隔着桌子向我眨了下眼。'),('A tiny red light winked in the dark.','一盏小红灯在黑暗中闪动。'),sources=S('winked','wink'))
W('winking','/ˈwɪŋkɪŋ/','正在眨眼示意、闪烁；眨眼的',
 '眼睛正一闭一开，像在递个暗号；远处的灯忽明忽暗，像眼睛眨着，这些过程都能叫 winking。',
 'wink + -ing，保留基础 /ŋk/；可作进行形式，也能直接形容眼睛、灯光等。',WINK+[['wink + -ing → winking','眨眼或一明一暗闪动正在进行']],
 'winking at someone 正向某人眨眼；winking lights 闪烁的灯；a winking face emoji 眨眼表情。',
 'keep winking；stars winking in the sky 闪动的星光。',
 'winking emoji 常传玩笑、默契等信号，具体意思仍看对话；不会只因一个眨眼就固定表示某一种关系。',
 ('He kept winking at me, but I did not understand the joke.','他不停向我眨眼，可我没听懂那个笑话。'),('We watched the winking lights of boats in the harbour.','我们望着港口里船上忽明忽暗的灯光。'),sources=S('winking','wink'))
PEEK=[['中古英语 piken：快速、偷偷地看 → peek','具体远源未定；与 keek、peep 等旧看词关系有不同分析'],['短暂、从遮挡处看 → peek 动词；后形成名词一瞥','现代常见于门缝、指缝、惊喜礼物等场景；也可说东西从遮挡处露出一点']]
W('peek','/piːk/','偷看；探头看；一瞥',
 '礼物还不让拆，人从包装缝里看一下；门只开一点，脑袋凑过去瞧瞧，这种带遮挡、短暂感的看叫 peek。',
 '承中古英语 piken 等看词，来源未定；名词后来由动词形成。现代整体保留，和 peak 山峰、pique 激起等同音词分别记。',PEEK,
 'peek through the door 从门缝偷看；have a peek 看一眼；a sneak peek 提前悄悄一看、先睹为快。',
 'peek inside 探头往里看；peek out from behind the curtain 从窗帘后露出、探看。',
 'peek 常有短暂、遮遮掩掩的看；peer 常有努力看清的感觉。同从门缝看，意图和姿态可不同。',
 ('Do not peek at the presents before your birthday.','生日之前，别偷看礼物。'),('Can I have a quick peek inside?','我能往里快速看一眼吗？'),sources=S('peek','peek'))
W('peeks','/piːks/','偷看、探头看〔第三人称单数〕；短暂的一瞥〔复数〕',
 '她从窗帘后偷偷看是谁来了，动词用 peeks；几次短短的偷看，名词也写 peeks。',
 'peek + -s，/k/ 后词尾读 /s/；名词复数与动词三单同形，ee 保留 /iː/。',PEEK+[['peek + -s → peeks','他、她短暂探看；几次一瞥']],
 'peeks through the curtains 从窗帘后偷看；peeks around the corner 从拐角探头看；quick peeks 快速的几瞥。',
 'peeks inside the box；peeks out of a pocket 从口袋里露出一点。',
 'peeks 作动作，peaks 是峰顶或达到顶点，二者常同音；a face peeks out 是脸探出来，不是脸达到高峰。',
 ('She peeks through the curtains to see who is outside.','她从窗帘后偷看，想知道谁在外面。'),('He keeps taking quick peeks at the surprise gift.','他总忍不住偷偷瞄几眼那份惊喜礼物。'),sources=S('peeks','peek'))
W('peeked','/piːkt/','偷看、探头看了一眼；露出了一点',
 '刚才从门边探头瞧了一下，就用 peeked；阳光、花朵从遮挡后露出一点，也能借用这种探头的样子。',
 'peek + 完整 -ed，/k/ 后词尾读 /t/，结尾 /kt/；保持 ee 的 /iː/，不和 pecked 啄了混读。',PEEK+[['peek + -ed → peeked','过去短暂探看；或从遮挡处露出一点']],
 'peeked into the room 探头往屋里看；peeked around the door 从门边探看；the sun peeked out 太阳露了出来。',
 'peeked through his fingers；peeked inside the box。',
 'peeked out 可写人向外看，也可写东西露出一点；太阳的例句就是拟人画面，不是太阳真的长眼睛。',
 ('He peeked around the door to see whether the meeting had ended.','他从门边探头看了一眼，想知道会议结束没有。'),('The sun peeked out from behind the clouds.','太阳从云后露出了一点。'),sources=S('peeked','peek'))
W('peeking','/ˈpiːkɪŋ/','正在偷看、探看；从遮挡后露出一点的',
 '手指挡着脸，眼睛却从缝里往外看，就是 peeking；小花从叶子后露出一点，也像在探头。',
 'peek + -ing，保留基础 k；进行形式也可直接修饰正露出来、探看的对象。',PEEK+[['peek + -ing → peeking','短暂探看正在进行；也写从遮挡后探出的样子']],
 'peeking through the curtains 从窗帘后偷看；flowers peeking through leaves 从叶间露出的小花。',
 'caught someone peeking 撞见某人偷看；no peeking 不许偷看。',
 'peeking 与 peaking 同音，前者看或露出来，后者达到峰值；看惊喜礼物的场景写 peeking。',
 ('I caught her peeking at the birthday cake.','我撞见她在偷看生日蛋糕。'),('Tiny flowers were peeking out between the stones.','小花从石缝间露出头来。'),sources=S('peeking','peek'))
def extend_lessons():
 extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_zgb',ROOTS,WORDS)
 extend_lessons()
