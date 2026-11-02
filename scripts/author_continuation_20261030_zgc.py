"""Glaring obviousness, unwanted looks, peeping and chirping homonyms."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
def S(word,base):
 return ['https://en.wiktionary.org/wiki/'+word+'#English','https://www.etymonline.com/word/'+base]
EXISTING_ROOT_ADDITIONS={
 'A1740':dict(words='glare glaring glaringly'.split(),label='glaringly：像强光一样显眼、扎眼',note='glare 的亮光、怒视与 glaring 的明显扎眼分场景解释；glaringly 为形容词 glaring 加 -ly，常修饰 obvious、wrong、absent 等。'),
 'B2752':dict(words='eye ogle ogles ogled ogling'.split(),label='ogle 与 eye 的远亲联系：带欲望地看',note='ogle 可能借低地德语 oeglen，其基础 oege 为眼，与英语 eye 有同源关系；不是现代英语 eye 加一个词尾直接变成 ogle。'),
 'B2761':dict(words='look leer leers leered leering peek peep peeps peeped peeping peeper peepers'.split(),label='leer、peep 与一般看：神态、遮挡和同形分支',note='本支按近义动作对照，不作全组同源声明。leer 可能从旧面颊、脸词发展，路线保留可能性；peep 看与 peep 啾叫另分来源，不能把声音说成由偷看产生。'),
 'A1697':dict(words='peep peeper peepers'.split(),label='peeper、peepers 的行动者与眼睛口语用法',note='看这一支 peep 加 -er 可指偷看者，peepers 也口语说眼睛；另有出声、啾叫的一支，动物义需按那一路区分。'),
}
GLARING=[['glare 的强光、怒视 → glaring','形容词后来也说颜色耀眼、问题显眼得无法忽略'],['glaring + -ly → glaringly','把扎眼、明摆着的程度用作副词，现代常有批评语气']]
W('glaringly','英 /ˈɡleərɪŋli/；美 /ˈɡlerɪŋli/','极其明显地；扎眼地；显而易见地',
 '一个错误摆在最显眼的地方，像强光照在眼前，想忽略都难，就可以说 glaringly obvious。常带“这么明显竟然还……”的评价。',
 'glaring + 副词 -ly；更前面 glare + -ing 的形容词从强光、显眼画面发展，不是今天每次都真有刺眼亮光。',GLARING,
 'glaringly obvious 极其明显；glaringly wrong 错得明显；glaringly absent 明显缺席、缺失。',
 'glaringly inconsistent 明显不一致；glaringly unfair 明显不公平。',
 'clearly 较中性，glaringly 常把明显程度和批评感一起加强；描述普通清楚事实时不必随便加这份扎眼感。',
 ('The mistake was glaringly obvious once we checked the total.','一核对总数，那个错误就明显得不能再明显了。'),('Her name was glaringly absent from the list.','名单上明显缺了她的名字。'),sources=S('glaringly','glare'))
OGLE=[['低地德语 oeglen 等可能来源 → 英语 ogle','其基础 oege 眼睛，与英语 eye 属同源材料；具体借入保留可能性'],['带爱慕、欲望的目光 → 直盯着打量人或想要的东西','现代常有不礼貌的意味，也可夸张写盯着喜欢的物品']]
W('ogles','英 /ˈəʊɡəlz/；美 /ˈoʊɡəlz/','色眯眯地打量；眼馋地盯着看〔第三人称单数〕',
 '不是单纯看到，而是目光黏在人或想要的东西上，带着欲望、眼馋的感觉，动词用 ogles。',
 'ogle + -s，词尾读 /z/；ogle 可能借低地德语眼、看的材料，和 eye 有较远同源联系。',OGLE+[['ogle + -s → ogles','他、她带欲望或眼馋地盯着看']],
 'ogles someone 直勾勾、色眯眯地打量某人；ogles the sports cars 眼馋地看跑车。',
 'ogles the display；ogles strangers。',
 'admires 可说欣赏，ogles 常带欲望、目光不加掩饰的意味；用于陌生人时尤其容易显得冒犯。',
 ('In the comedy, he ogles every expensive car that passes.','喜剧里，每有一辆昂贵汽车经过，他都眼馋地盯着看。'),('She dislikes the way he ogles strangers.','她不喜欢他那样色眯眯地打量陌生人。'),sources=S('ogles','ogle'))
W('ogled','英 /ˈəʊɡəld/；美 /ˈoʊɡəld/','色眯眯地打量了；眼馋地盯着看了',
 '刚才那道目光不是中性观察，而是把喜欢、欲望都写在眼里地盯着，可以说 ogled。',
 'ogle 去 e 加完整 -ed，词尾读 /d/；基础 /ɡəl/ 保留。',OGLE+[['ogle → ogled','过去带欲望、眼馋地盯着打量']],
 'ogled the cars 眼馋地看汽车；was ogled by strangers 被陌生人色眯眯地打量。',
 'ogled the window display；ogled someone openly。',
 'ogled 写看的方式和态度，不等于 bought；眼馋地盯着橱窗看，并没有说明买下来了。',
 ('We ogled the shiny motorbikes in the showroom.','我们眼馋地盯着展厅里亮闪闪的摩托车看。'),('She felt uncomfortable when the man ogled her.','那个男人色眯眯地打量她，让她很不舒服。'),sources=S('ogled','ogle'))
W('ogling','英 /ˈəʊɡəlɪŋ/；美 /ˈoʊɡəlɪŋ/','正在色眯眯地打量；眼馋地盯看',
 '人还在直直地看，眼神里带着想要、欲望，叫 ogling；也可把这种让人不舒服的盯看当作一种行为。',
 'ogle 去 e 加 -ing；现代动作形式，也可用作行为名词。',OGLE+[['ogle → ogling','带欲望地盯看正在进行或作为一种行为']],
 'ogling strangers 色眯眯打量陌生人；ogling expensive watches 眼馋地盯着名表看。',
 'caught someone ogling；unwanted ogling 让人不愿承受的盯视。',
 'ogling 比 looking 更明确写出目光中的欲望；写普通观察、研究物件时通常无需这层态度。',
 ('They stood ogling the expensive watches in the window.','他们站着，眼馋地盯着橱窗里的名表。'),('He was asked to stop ogling people in the café.','有人请他别再色眯眯地打量咖啡馆里的人。'),sources=S('ogling','ogle'))
LEER=[['旧英语 hleor、中古英语 ler 等脸、面颊材料 → leer 的一种可能解释','可能经斜着脸、斜看发展，具体路线保留可能性'],['斜看 → 现代带欲望、恶意地看或笑','现代人物描写常含让人不舒服的暗示；不是所有斜眼一瞥都称 leer']]
W('leer','英 /lɪə/；美 /lɪr/','色眯眯、恶意地看；邪笑；不怀好意的一眼或笑',
 '眼神斜斜地黏着人，嘴边还挂着让人不舒服的笑，可以叫 a leer。这个词把不怀好意的态度写进目光里。',
 '一种常见分析联系旧脸、面颊名词，再到斜看；具体历史保留可能性。现代名词由这种看的动作形成。',LEER,
 'leer at someone 色眯眯、不怀好意地看某人；an unpleasant leer 令人不舒服的邪笑。',
 'give someone a leer；a knowing leer 带暗示的邪笑。',
 'a smile 可以友善，a leer 通常有令人反感的欲望、恶意或暗示；不用于普通礼貌微笑。',
 ('The villain gave a nasty leer.','反派露出一个恶心的邪笑。'),('He began to leer at the woman across the room.','他开始色眯眯地盯着房间另一头的女人。'),sources=S('leer','leer'))
W('leers','英 /lɪəz/；美 /lɪrz/','色眯眯、恶意地看〔第三人称单数〕；邪笑、恶意目光〔复数〕',
 '他看人的样子让人想避开，像笑里藏着别的心思，动词用 leers；几次这样的邪笑，名词也同形。',
 'leer + -s，词尾读 /z/；动词三单和名词复数同形，基础来源有脸、斜看等不同历史分析。',LEER+[['leer + -s → leers','他、她不怀好意地看；几道恶意目光或邪笑']],
 'leers at passersby 色眯眯地看路人；unpleasant leers 令人不舒服的邪笑。',
 'leers from the doorway；exchanges leers 互相露出带暗示的坏笑。',
 'leers 是说话人对目光的负面描写；gazes 可以只是凝望，不必带这种恶意、欲望评价。',
 ('In the film, the villain leers from the doorway.','电影里，反派站在门口，露着不怀好意的笑。'),('She was tired of their comments and leers.','他们的言语和色眯眯的目光让她厌烦。'),sources=S('leers','leer'))
W('leered','英 /lɪəd/；美 /lɪrd/','色眯眯、恶意地看了；露出邪笑了',
 '刚才对方不怀好意地打量过来，或者笑得让人不舒服，过去这种看、笑的动作叫 leered。',
 'leer + -ed，词尾读 /d/；英式在此通常不单独发 r，美式保留 /r/。',LEER+[['leer + -ed → leered','过去带欲望、恶意或暗示地看、笑']],
 'leered at someone 色眯眯盯着某人；leered from the doorway 在门口不怀好意地看。',
 'leered and laughed；leered across the table。',
 'leered at 不是中性地 looked at；把这个词换进句子，会明显改变人物给人的印象。',
 ('The man leered at her as she walked past.','她走过时，那个男人色眯眯地盯着她。'),('The villain leered before revealing his plan.','反派露出邪笑，接着说出了自己的计划。'),sources=S('leered','leer'))
W('leering','英 /ˈlɪərɪŋ/；美 /ˈlɪrɪŋ/','正在色眯眯、恶意地看；带邪笑的',
 '那种让人反感的目光、笑还挂在脸上，叫 leering；直接形容人时，也把这份不怀好意带上。',
 'leer + -ing；既作进行形式，也作形容词。英式接后面元音时发 /r/。',LEER+[['leer + -ing → leering','不怀好意地看正在进行；也修饰笑、脸等']],
 'a leering smile 邪笑；leering at someone 色眯眯地看某人；a leering face 一张带着邪笑的脸。',
 'leering from the shadows；a leering expression。',
 'leering smile 与 warm smile 的态度不同；两者都牵动嘴角，但一个让人戒备，一个常让人亲近。',
 ('The drawing showed a villain with a leering smile.','画上是一个带着邪笑的反派。'),('She moved away from the man who was leering at her.','那个男人正色眯眯地看着她，她走远避开了。'),sources=S('leering','leer'))
PEEP=[['看这一支：中古英语 pepen，可能联系 peek 的旧看词','从遮挡处探看、短暂看；后来也说东西刚露出一点'],['声音这一支：旧啾叫材料，可能与 pipen 等有关','拟声的短叫形成轻声、最小声响的名词；不是从眼睛偷看派生出来']]
W('peep','/piːp/','偷看、探看；一瞥；啾叫；一点声响',
 '从门缝看一眼，可以是 peep；小鸡啾一下，也叫 peep。这是两条来源的同形词，要分别记画面。',
 '看的一支可能联系旧 peek 材料；出声的一支最终有拟声背景。现代名词、动词都用，不把看和叫编成同一演化链。',PEEP,
 'peep through the curtains 从窗帘后偷看；have a peep 看一眼；not hear a peep 一点声音都没听见；chicks peep 小鸡啾叫。',
 'a peep at the garden；the first peep of daylight 刚露出的晨光。',
 'peek 与 peep 在偷看场景很接近；peep 还可以是轻叫、声响，这一支不能用 peek 替换。',
 ('I had a peep through the curtains.','我从窗帘后偷看了一眼。'),('We did not hear a peep from the children.','我们一点也没听到孩子们出声。'),sources=S('peep','peep'))
W('peeps','/piːps/','探看、啾叫〔第三人称单数〕；几瞥、短叫〔复数〕；朋友、伙伴〔口语〕',
 '小鸡轻轻叫，是 peeps；脸从门边探出来看，也能写 peeps。口语里 my peeps 又能指我的伙伴，需另看缩短来源。',
 'peep + -s，/p/ 后读 /s/；看、叫两支同形。称人的 peeps 通常解释为 people 的口语缩短，不从小鸡叫推出。',PEEP+[['peep + -s → peeps；另有 people 缩短的口语 peeps','看、叫的词形；人物称呼另外分路']],
 'peeps through the door 从门口探看；soft peeps 轻轻啾叫；my peeps 我的伙伴们。',
 'a chick that peeps；a few quick peeps 几次快速偷看。',
 'peeps 的人物口语用法需要轻松语体；正式写 colleagues、friends 等，表达对象更明确。',
 ('The chick peeps whenever it wants food.','那只小鸡一想吃东西就啾啾叫。'),('She peeps around the door to see who has arrived.','她从门边探头看，想知道谁到了。'),sources=S('peeps','peep'))
W('peeped','/piːpt/','偷看、探看了；露出来了；啾叫了',
 '花从叶间露了个头，是 peeped out；小鸡叫了一声，也是 peeped。虽然拼写一样，两个动作要分路理解。',
 'peep + 完整 -ed，/p/ 后词尾读 /t/，结尾 /pt/；看、声音两支都按这个规则变形。',PEEP+[['peep + -ed → peeped','过去从遮挡处看、露出；另一路是过去轻叫']],
 'peeped into the room 偷偷往屋里看；peeped out of the soil 从土里露出；a chick peeped 小鸡叫了。',
 'peeped through a gap；peeped softly。',
 'peeped out 可以写东西出现，不一定是在看；主语是花、光时，常是从遮挡处露出一点。',
 ('A few flowers peeped out between the stones.','几朵花从石缝间露出头来。'),('The chick peeped softly in the box.','小鸡在盒子里轻轻啾叫。'),sources=S('peeped','peep'))
W('peeping','/ˈpiːpɪŋ/','正在偷看、探看；露头；轻轻啾叫',
 '眼睛还在从缝里往外看，或者小花从土里刚冒出一点，可以写 peeping；小鸟啾叫则走声音的另一支。',
 'peep + -ing；两个同形动词都能加这个词尾，不能因为拼写一致就取消来源区别。',PEEP+[['peep + -ing → peeping','探看、露头正在进行；另一路是正在轻叫']],
 'peeping through the window 隔窗偷看；flowers peeping through the snow 从雪间露出的小花；chicks peeping 小鸡啾叫。',
 'no peeping 不许偷看；heard birds peeping 听见鸟啾叫。',
 'peeping 的普通看一眼与冒犯性窥探，要结合对象、场景；Peeping Tom 则是带负面意味的窥视者固定称呼。',
 ('No peeping until I finish wrapping the present.','我把礼物包好之前，不许偷看。'),('We could hear chicks peeping inside the barn.','我们能听见谷仓里小鸡啾啾叫。'),sources=S('peeping','peep'))
PEEPER=PEEP+[['peep + -er → peeper','看的一支可指偷看者，复数也口语说眼睛；出声的一支可命名啾叫动物']]
W('peeper','英 /ˈpiːpə/；美 /ˈpiːpər/','偷看者；啾叫的小鸟、蛙等；眼睛〔较口语，常用复数〕',
 '谁在从遮挡后偷偷看，-er 就能给这个行动者命名为 peeper。也有按声音给小动物命名的一支，口语 peepers 又能直接说眼睛。',
 'peep + -er；看与啾叫各自都能造行动者词，具体所指看上下文，不把所有动物都从窥看者演化出来。',PEEPER,
 'a peeper at the window 在窗边偷看的人；spring peeper 是一种按叫声命名的小蛙；eyes 的口语用法常用 peepers。',
 'an unwelcome peeper；a tiny peeper calling。',
 'peeper 带偷看的感觉时不同于普通 viewer 观众；动物名称则依叫声理解，角色不同。',
 ('The story begins when a peeper is spotted at the window.','故事从有人发现窗边有个偷看者开始。'),('A tiny peeper called from the reeds.','一只小小的啾叫蛙从芦苇里发出叫声。'),sources=S('peeper','peep'))
W('peepers','英 /ˈpiːpəz/；美 /ˈpiːpərz/','眼睛〔口语〕；偷看者；啾叫的小动物〔复数〕',
 'keep your peepers open 像说“眼睛睁大点，多留心”；放到池塘、夜声场景里，peepers 也能是啾叫的小蛙等动物。',
 'peeper + -s，词尾读 /z/；内层 peep + -er 的看、出声两支分别保留，眼睛口语通常用这个复数。',PEEPER+[['peeper + -s → peepers','多个看或叫的对象；口语直接说眼睛']],
 'keep your peepers open 留心看；shut your peepers 闭眼，语气随意；peepers calling by the pond 池边啾叫的小蛙。',
 'sleepy peepers 困倦的眼睛；a chorus of peepers 一片小蛙叫声。',
 'peepers 说眼睛很口语、常带玩笑，不适合代替所有正式 eye 用法；叫声场景则通常是动物名词。',
 ('Keep your peepers open for a red sign.','眼睛留神点，找一块红牌子。'),('We heard peepers calling near the pond.','我们听见池塘附近小蛙在啾啾叫。'),sources=S('peepers','peep'))
def extend_lessons():
 extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_zgc',ROOTS,WORDS)
 extend_lessons()
