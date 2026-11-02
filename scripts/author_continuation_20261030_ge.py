"""Nose and pink: visible shapes, colour names and a misleading homograph."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
N=[['古英语 nosu → 中古英语 nose','鼻子，呼吸、嗅闻的器官'],['英语 nose','鼻子 → 像鼻子一样突出的前端；嗅探、打听']]
W('nose','英 /nəʊz/；美 /noʊz/','鼻子；前端、机头；嗅探、打听',
 '脸上伸出来、能闻味道的鼻子；飞机前端像它，所以也叫 nose。把鼻子探进别人的事，又能说打听、窥探。',
 '古英语 nosu 经中古英语到 nose，是本族旧词。现代当一个整体用，末尾 -se 不是有独立意义的后缀。',N,
 'blow your nose 擤鼻子，the nose of the plane 机头，a nose for news 对新闻的敏锐嗅觉，nose around 四处打探。',
 'blow your nose；the nose of；a nose for；nose around。',
 'nose 器官或突出前端，nostril 是鼻孔；a nose for something 常说善于发现，不是那东西真有气味。',
 ('The nose of the plane pointed toward the runway.','飞机机头朝着跑道。'),('She has a nose for a good story.','她很善于发现好故事。'),sources=['https://www.etymonline.com/word/nose'])
W('nozzle','英 /ˈnɒzəl/；美 /ˈnɑːzəl/','喷嘴、管嘴',
 '水管或机器前面伸出一个小嘴，液体、气体从那里出来；可以想成器具的小鼻子。',
 '中古英语 noselle，历史上相当于 nose + 表小形式 -le，拼写、读音后来变化为 nozzle；不是 no + zzle。',N[:1]+[['noselle → nozzle','器物伸出的小嘴 → 喷嘴、管嘴']],
 'a spray nozzle 喷雾嘴，a fuel nozzle 加油枪嘴，adjust the nozzle 调节喷嘴。喷嘴形状往往还决定喷出的方向、范围。',
 'a spray nozzle；a fuel nozzle；adjust the nozzle。',
 'nozzle 是出口处的嘴，hose 是软管，faucet/tap 是控制出水的龙头；几个部件可以连着，但不等同。',
 ('Turn the nozzle to change the spray pattern.','转动喷嘴，改变喷洒形状。'),('Water leaked from the joint behind the nozzle.','水从喷嘴后面的接头漏出来。'))
W('nosy','英 /ˈnəʊzi/；美 /ˈnoʊzi/','爱打听别人私事的、多管闲事的',
 '总把鼻子往别人的生活里伸：你没打算告诉他，他还想刨根问底。常带嫌人越界的语气。',
 'nose + -y，末尾 e 在这里不保留。nose 已有打探义，形容词 nosy 把这种习惯贴到人或问题上；也拼 nosey。',N+[['nose + -y → nosy','爱窥探、打听私事的']],
 'a nosy neighbor 爱管闲事的邻居，nosy questions 过分打探私事的问题，be nosy about 对某事瞎打听。',
 'a nosy neighbor；nosy questions；be nosy about。',
 'curious 泛指好奇，可以是学习动力；nosy 多说好奇伸进了别人的边界。不要把每个爱学习的人都叫 nosy。',
 ('I did not want to sound nosy, so I changed the subject.','我不想显得爱打听私事，就换了话题。'),('Our nosy neighbor asked who had visited us.','爱打听的邻居问谁来过我们家。'))
W('nostril','英 /ˈnɒstrəl/；美 /ˈnɑːstrəl/','鼻孔',
 '鼻子是整个器官，nostril 是其中一个进出空气的开口：通常左右各一个。',
 '古英语 nosþyrel，把鼻子材料和表示孔洞的 þyrel 接起来，后来缩变成 nostril。可借旧词 thirl 孔理解后半段，不能按现代 trill 颤音拆。',
 [['古英语 nosþyrel','鼻 + 孔'],['中古英语 nostrille → nostril','鼻孔，复数 nostrils']],
 'one nostril 一个鼻孔，both nostrils 两个鼻孔，flare your nostrils 鼻翼张开。鼻翼不是整个鼻孔的英语直译。',
 'one nostril；both nostrils；flare your nostrils。',
 'nose 整个鼻子，nostril 开口，nasal 形容鼻部的；拼写不同不代表器官不同。',
 ('The horse flared its nostrils.','马张开了鼻翼。'),('A drop of paint had landed beside his left nostril.','一滴油漆落在了他的左鼻孔旁。'))
W('nosebleed','英 /ˈnəʊzbliːd/；美 /ˈnoʊzbliːd/','流鼻血、鼻出血',
 'nose 指发生部位，bleed 指出血；连起来，出血这件事成了能说 a 的事件名。',
 'nose + bleed；动词 bleed 的材料进入复合名词。复数 nosebleeds 表示多次鼻出血，不把 nose 单独变复数。',N[:1]+[['nose + bleed → nosebleed','鼻部出血 → 一次鼻出血事件']],
 'have a nosebleed 流鼻血，get nosebleeds 会流鼻血；nosebleed seats 是俚语，夸张说体育场或剧院特别高、远的座位。',
 'have a nosebleed；frequent nosebleeds；nosebleed seats〔俚语〕。',
 'a nosebleed 是名词，my nose is bleeding 用动词描述正在出血。后一个句式不要再加 a。',
 ('He missed the start of the game because he had a nosebleed.','他因为流鼻血，错过了比赛开场。'),('We could only afford the nosebleed seats.','我们只买得起最高、最远处的座位。'))
W('nosedive','英 /ˈnəʊzdaɪv/；美 /ˈnoʊzdaɪv/','俯冲；急剧下跌',
 '机头朝下扎，整架飞机陡陡往下掉；价格、销量也能借这个动作说突然暴跌。',
 'nose 前端、机头 + dive 下潜、俯冲。整体可作名词和动词，财经用法沿用陡降的画面。',N+[['nose + dive → nosedive','机头向下俯冲 → 数值、状况急跌']],
 'go into a nosedive 进入俯冲、骤跌，take a nosedive 暴跌，sales nosedived 销量骤降。',
 'go into a nosedive；take a nosedive；prices nosedive。',
 'decline 可缓慢下降，nosedive 突出又快又陡；dive 更宽，nosedive 把朝下的前端也画出来。',
 ('The plane went into a nosedive before the pilot regained control.','飞行员重新控制住飞机前，飞机一度向下俯冲。'),('Ticket sales took a nosedive after the bad reviews.','差评出现后，票销量骤降。'))
R('B2766','鼻子、嗅觉与伸出的前端','NOSE：先看鼻子，再看像鼻子的前端','nose → nosy 打听；nozzle 小管嘴；nose + 孔 → nostril；nosebleed、nosedive 各选不同鼻子义。',
 '鼻子能闻、能往前伸，这两点足以解释很多扩展。先分清器官、嗅探、前端，再接后面的材料。',
 'nosu → nose；noselle → nozzle；nosþyrel → nostril；nose + -y/bleed/dive；bottle + nose。',
 [['基本词与爱打听','nose · nosy'],['形状与孔口','nozzle · nostril · bottlenose'],['部位和运动','nosebleed · nosedive']],
 'nose/nostril 整体与开口；nosy/curious 越界打听与一般好奇；nosedive 不只是轻微下降。',
 'The nosy neighbor watched as the plane’s nose dipped.\n\n爱打听的邻居看着飞机机头低了下去。','nose nosy nozzle nostril bottlenose nosebleed nosedive')
P=[['英语 pink 花名','石竹属花卉的名称；更早来源不确定'],['花名 → 颜色名 pink','其中常见的浅红、粉红色'],['颜色比喻','较浅的红色 → 某些政治语境里的温和左倾']]
W('pink','/pɪŋk/','粉红色、粉红的；石竹属花卉',
 '先有一类叫 pink 的花，再把它常见的浅红色借来给颜色命名；不是所有这种花都必须开粉红花。',
 '颜色名来自既有花名。花名更早来源不确定，有把花瓣锯齿边和 pink 剪出齿边联系的解释，也有其他说法；不能把其中一个猜想写成定论。',P,
 'a pink shirt 粉红衬衫，pale pink 浅粉色，turn pink 脸泛粉红；in the pink 常说身体状况很好。pinking shears 的 pink 是剪齿边动词支。',
 'pale pink；bright pink；turn pink；in the pink。',
 'pink 颜色义有花名来路；pinky 小指不能简单说因为小指粉红而得名。pink 的古老同形词也不必全部归成颜色。',
 ('The sky turned pink just before sunrise.','日出前，天空变成了粉红色。'),('She planted white and pink pinks along the path.','她沿小路种了白色和粉红色的石竹花。'),sources=['https://www.etymonline.com/word/pink'])
W('pinkish','/ˈpɪŋkɪʃ/','略带粉红色的、偏粉红的',
 '还不能干脆说是纯粉红，但看得出一点粉红调；-ish 把颜色判断放松一点。',
 'pink + -ish，颜色 + 有点、近似；这里的 -ish 不是民族名后缀的那一类用法。',P[:2]+[['pink + -ish → pinkish','有些粉红、偏粉红']],
 'a pinkish glow 淡粉光晕，pinkish skin 泛粉的皮肤，a pinkish tint 偏粉的色调。',
 'a pinkish glow；a pinkish tint；look pinkish。',
 'pinkish 说有粉红成分，pale pink 说粉红的颜色浅；一个偏判断，一个偏深浅，两者可以重叠。',
 ('The white walls looked pinkish in the evening light.','白墙在傍晚光线里显得有些粉红。'),('The stone has a pinkish tint.','这块石头略带粉红色。'))
W('pinko','英 /ˈpɪŋkəʊ/；美 /ˈpɪŋkoʊ/','左倾分子、亲社会主义者〔贬称〕',
 '说话人拿红色比共产主义，再把较浅的 pink 用来贬称左倾的人；这是带立场的标签，不是中性的政治测量。',
 'pink 政治比喻义 + -o 人物词尾。粉红比红浅，形成较温和、未必彻底共产主义的联想；实际使用常只是在骂对方左倾。',P+[['pink + -o → pinko','对左倾人物的贬称']],
 'call someone a pinko 给某人扣左倾帽子，a pinko intellectual 左倾知识分子〔说话人贬意〕。常见于特定时代的政治争论。',
 'call someone a pinko；a pinko intellectual〔贬称〕。',
 'leftist 范围宽、语气看上下文；pinko 明显带嘲讽、敌意，不宜当作对方自我认同的正式名称。',
 ('The columnist dismissed the professor as a pinko.','专栏作者把教授贬称为左倾分子。'),('In the film, the word pinko reveals the speaker’s political hostility.','片中的 pinko 暴露了说话人的政治敌意。'))
W('pinky','/ˈpɪŋki/','小指〔也拼 pinkie〕；带粉红色的〔另一构词义〕',
 '最常见名词是手上最小那根指头；另有 pink + -y 的颜色用法。两个读写相同，不等于小指是按颜色命名。',
 '小指名经苏格兰英语接荷兰语 pinkje，后者是 pink 小指的指小形式；颜色形容词则可拆 pink + -y。两条来路分开记。',
 [['荷兰语 pink → pinkje','小指 → 指小形式'],['苏格兰英语 pinkie → pinky','小指名'],['另一路：pink + -y','粉红、略粉红的颜色描述']],
 'my left pinky 我的左手小指，a pinky promise 勾小指的承诺；英式也常直接叫 little finger，pinkie 是常见拼写变体。',
 'my left pinky；a pinky promise；little finger。',
 'pinky 常用名词指小指，pinkish 才是很稳妥的“略粉红”；不能遇到 pinky 就译粉红色。',
 ('She raised her pinky while holding the tiny cup.','她握着小杯子时翘起了小指。'),('We made a pinky promise to keep the surprise secret.','我们拉钩答应对这个惊喜保密。'),sources=['https://www.etymonline.com/word/pinkie','https://en.wiktionary.org/wiki/pinky#English'])
R('B2569','花名借给颜色，颜色还能变成政治标签','PINK：花的名字变成粉红；小指另走一条路','pink → pinkish 稍粉红；pink → pinko 政治贬称；pinky 小指另接荷兰语指小形式。',
 '花名到颜色很直观，但花名最早从哪来仍有争议。小指的常用名也别被现代粉红色带偏。',
 '花名 pink → 颜色 pink → pinkish/pinko；荷兰语 pinkje → pinkie/pinky 小指。',
 [['颜色与程度','pink · pinkish'],['颜色的政治比喻','pinko'],['同形分路：小指','pinky']],
 'pink/pinky 颜色与常用小指名分路；pinkish/pale pink 有点粉红与浅粉；pinko 带贬意。',
 'She painted her pinky nail a pinkish colour.\n\n她把小指指甲涂成了略带粉红的颜色。','pink pinkish pinko pinky')
if __name__=='__main__':save('continuation_20261030_ge',ROOTS,WORDS)
