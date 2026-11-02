"""Hair: texture, professions, tools and shape metaphors."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
H=[['古英语 hǣr → 中古英语 her、heer → hair','头发、毛发'],['现代 hair 词族','毛发集合与单根；护理、造型、发际线和细如发丝的比喻']]
def E(f,m):return H+[[f,m]]
W('hair','英 /heə/；美 /her/','头发；毛发；一根头发',
 '说整头头发时通常当一片整体，说掉下来的一根时才可以数一根、两根。',
 '继承古英语 hǣr，日耳曼语中的古老毛发词。现代不可数与可数用法并存，取决于整体还是单根。',H,
 'long hair 长发，a hair 一根头发，wash your hair 洗头；split hairs 是在细枝末节上较真。',
 'long hair；wash your hair；a strand of hair；split hairs。',
 'She has long hair 不把整体长发说成 long hairs；I found a hair in the soup 是一根。hair 与 hare 野兔同音不同词。',
 ('She has thick, curly hair.','她头发浓密卷曲。'),('I found a grey hair on my jacket.','我在夹克上发现一根灰白头发。'))
W('hairy','英 /ˈheəri/；美 /ˈheri/','多毛的；危险、棘手的',
 '字面是毛多；口语里 a hairy moment 是让人紧张、险些出事的一刻，不是那一刻长出毛。',
 'hair + -y，现代有多毛和非正式险要、令人紧张的形容词义。后者的确切演化不强编成某个确定故事。',E('hair + -y → hairy','有毛、多毛；另有险要口语义'),
 'hairy arms 毛多的手臂，a hairy situation 险要局面，a hairy moment 惊险一刻。',
 'hairy arms；a hairy situation；a hairy moment。',
 'hairy 指多毛，haired 常由前面说明发色、长度；口语 hairy situation 要从整体搭配理解。',
 ('The small caterpillar had a hairy body.','小毛毛虫的身体长满细毛。'),('We had a hairy moment when the boat hit a rock.','船撞上石头时，我们经历了惊险一刻。'))
W('haired','英 /heəd/；美 /herd/','有某种头发的',
 '通常前面要告诉你头发什么样，比如短发、红发；单独说有头发往往信息不够。',
 'hair + -ed，形成具有毛发特征的形容词，相应形式中古英语已有。读 /d/ 结尾，不另添 /ɪd/ 音节。',E('hair + -ed → haired','具有某种毛发的'),
 'a red-haired child 红发孩子，a short-haired cat 短毛猫；复合修饰语中的连字符照常保留，不另建连字符词条。',
 'red-haired；short-haired；dark-haired。',
 'haired 描述特征，haired 不等于 hired 被雇用；hairy 则直接说毛多。',
 ('A red-haired child opened the door.','一个红发孩子打开了门。'),('The short-haired cat was sleeping on the sofa.','短毛猫正在沙发上睡觉。'))
W('hairless','英 /ˈheələs/；美 /ˈherləs/','无毛的；没有毛发的',
 '某个身体部位或动物表面没有明显毛发，重点是缺少这一层毛。',
 'hair + -less 没有，构成无毛形容词。范围看对象，不一定整只动物、整个人完全没有任何毛。',E('hair + -less → hairless','没有毛发的'),
 'hairless skin 无毛皮肤，a hairless cat 无毛猫；相对描述不等于所有物种都真的零根毛。',
 'hairless skin；a hairless cat；a hairless patch。',
 'bald 常说头顶秃或局部不长毛，hairless 更直接泛说缺毛；两者在部分语境重合。',
 ('The cat has nearly hairless skin.','这只猫的皮肤几乎没有毛。'),('A small hairless patch appeared on the dog’s leg.','狗腿上出现了一小块无毛区域。'))
W('hairline','英 /ˈheəlaɪn/；美 /ˈherlaɪn/','发际线；极细的线、裂纹',
 '头发从额头附近开始生长的边界是一条线；像一根发丝那么细的裂纹也叫 hairline。',
 'hair + line 线、边界，形成发际线和发丝般细线两条用法。不是所有 line 都在额头上。',E('hair + line → hairline','头发边界；细如发丝的线'),
 'a receding hairline 后移的发际线，a hairline crack 细微裂纹；后者用 hairline 作修饰成分。',
 'a receding hairline；a hairline crack；a hairline fracture。',
 'hairline crack 通常形容细，不一定浅到完全无关紧要；看到裂纹是否影响结构要看专业检查，不从名字猜。',
 ('His hairline has changed over the years.','这些年他的发际线发生了变化。'),('A hairline crack ran across the cup.','一道细微裂纹横过杯身。'))
W('hairdresser','英 /ˈheədresə/；美 /ˈherdresər/','理发师；美发师',
 '替人剪、整理、烫染或造型头发的人，工作不只把头发剪短。',
 'hair + dresser 整理、装饰者，dress 这里取整理装扮义，不是给头发穿连衣裙。',E('hair + dresser → hairdresser','整理、造型头发的人 → 美发师'),
 'go to the hairdresser’s 去美发店，a professional hairdresser 专业美发师；所有格常省略 salon。',
 'a professional hairdresser；the hairdresser’s；book a hairdresser。',
 'barber 常侧重短发、男士修面等服务，hairdresser 服务范围常更广；实际服务有重叠，不硬按从业者性别区分。',
 ('The hairdresser suggested a shorter style.','美发师建议换个短一点的发型。'),('I have an appointment at the hairdresser’s tomorrow.','我明天预约了去美发店。'))
W('hairdressing','英 /ˈheədresɪŋ/；美 /ˈherdresɪŋ/','美发；理发、造型行业',
 '把整理、剪染、造型头发这一整套工作作为技能和行业来讲。',
 'hair + dressing 整理装扮，活动名词，与 hairdresser 执行者对应。dressing 这里不是沙拉酱。',E('hair + dressing → hairdressing','整理头发的活动 → 美发'),
 'a hairdressing course 美发课程，hairdressing skills 美发技能；通常不可数地说行业。',
 'a hairdressing course；hairdressing skills；the hairdressing industry。',
 'hairdresser 是人，hairdressing 是活动、行业；a hairdressing student 是学美发的学生。',
 ('She is taking a hairdressing course.','她正在上美发课。'),('The college teaches practical hairdressing skills.','学院教授实用美发技能。'))
W('hairstylist','英 /ˈheəstaɪlɪst/；美 /ˈherstaɪlɪst/','发型师',
 '重点在设计、制作发型，让头发的形状和整体造型适合人或场景。',
 'hair + stylist 造型师；stylist 又与 style、人物后缀 -ist 对应。不是 hair + style + list 名单。',E('hair + stylist → hairstylist','头发造型的专业人员 → 发型师'),
 'a professional hairstylist 专业发型师，a film hairstylist 影视发型师；也可用于普通美发店人员。',
 'a professional hairstylist；a film hairstylist；work as a hairstylist。',
 'hairstylist 与 hairdresser 大幅重叠，前者称呼更突出造型；别编成一个只能剪、另一个绝不剪的硬界限。',
 ('The hairstylist created a new look for the actor.','发型师为演员设计了一个新造型。'),('She asked her hairstylist for advice about the fringe.','她向发型师咨询刘海的建议。'))
W('hairstyling','英 /ˈheəstaɪlɪŋ/；美 /ˈherstaɪlɪŋ/','发型设计、造型；头发造型活动',
 '用梳理、修剪、卷烫或造型产品等方法，把头发做成想要的样子。',
 'hair + styling，styling 是 style 去 e + -ing；这里整体是头发造型活动，不是造型师人物。',E('hair + styling → hairstyling','为头发做造型的活动'),
 'hairstyling products 头发造型产品，hairstyling tools 造型工具；与 hairstyle 已完成的发型对照。',
 'hairstyling products；hairstyling tools；hairstyling techniques。',
 'hairstyle 发型结果，hairstyling 造型活动，hairstylist 做造型的人。',
 ('The shop sells hairstyling products and brushes.','商店销售头发造型产品和梳子。'),('Hairstyling is part of her work in the theatre.','头发造型是她在剧院工作的一部分。'))
W('hairdryer','英 /ˈheədraɪə/；美 /ˈherdraɪər/','吹风机',
 '用气流把头发吹干的设备；dryer 是让东西变干的器具。',
 'hair + dryer，dryer 来自 dry + -er。也常写 hair dryer、hair drier；拼写变体不必重复建词条。',E('hair + dryer → hairdryer','让头发变干的设备 → 吹风机'),
 'use a hairdryer 用吹风机，a travel hairdryer 旅行吹风机；名称强调用途，不指定每款机器的技术结构。',
 'use a hairdryer；a travel hairdryer；a handheld hairdryer。',
 'hairdryer 吹干头发，hairbrush 梳理头发；dryer 不是 driver 驾驶者。',
 ('The hotel room has a hairdryer.','酒店房间有吹风机。'),('She packed a small travel hairdryer.','她装好了一台小旅行吹风机。'))
W('hairbrush','/ˈheəbrʌʃ/；美 /ˈherbrʌʃ/','发刷；梳头刷',
 '一面有一排排刷齿、刷毛，用来梳理头发的工具。',
 'hair + brush 刷子，按用途直接组合。brush 名词是工具，动词 brush your hair 则是梳理头发。',E('hair + brush → hairbrush','梳头发的刷子 → 发刷'),
 'a round hairbrush 圆筒发刷，clean a hairbrush 清理发刷；形状、刷毛材料可以不同。',
 'a round hairbrush；a wooden hairbrush；clean a hairbrush。',
 'comb 常是单排齿的梳子，hairbrush 是刷式梳具；中文都能说梳子，英语结构名有所不同。',
 ('She keeps a hairbrush in her bag.','她在包里放着一把发刷。'),('He removed the loose hairs from the hairbrush.','他把发刷上掉落的头发清理掉了。'))
W('hairpin','英 /ˈheəpɪn/；美 /ˈherpɪn/','发夹、发簪；发夹状的急弯',
 '先想一根弯成窄 U 形、固定头发的小夹子；道路猛地折回，形状也像它。',
 'hair + pin 别针、簪，先有发夹器物义，再按形状形成 hairpin bend、hairpin turn 急转弯。',E('hair + pin → hairpin','固定头发的小簪 → 发夹状急弯'),
 'secure hair with a hairpin 用发夹固定头发，a hairpin bend 发夹弯；后者不是路上落了一枚夹子。',
 'a metal hairpin；a hairpin bend；a hairpin turn。',
 'hairpin bend 强调急折回的形状，winding road 可泛说一路弯曲；不一定每个弯都尖得像发夹。',
 ('She secured the bun with two hairpins.','她用两枚发夹固定发髻。'),('The mountain road has several sharp hairpin bends.','这条山路有几个急剧回折的发夹弯。'))
W('hairpiece','/ˈheəpiːs/；美 /ˈherpiːs/','假发片；补发片',
 '不是一定换掉整头头发，而是用一片假发补充部分发量或造型。',
 'hair + piece 一片、一个部件，组合成局部假发用品。piece 选部分义，不能译成一根头发。',E('hair + piece → hairpiece','一片头发用品 → 假发片'),
 'wear a hairpiece 戴假发片，a removable hairpiece 可拆卸发片；影视造型、日常补发都可能使用。',
 'wear a hairpiece；a removable hairpiece；fit a hairpiece。',
 'wig 常指整体假发，hairpiece 更常指局部补发件；实际商品称呼可有重叠。',
 ('The actor wore a hairpiece for the role.','演员为这个角色戴了假发片。'),('The stylist fitted a small hairpiece to add volume.','造型师装上一小片假发来增加发量。'))
W('hairball','英 /ˈheəbɔːl/；美 /ˈherbɔːl/','毛球；毛发结成的团',
 '一根根毛聚在一起缠成一团；猫舔毛后形成的毛团是常见使用场景。',
 'hair + ball 球、团，不要求像标准球一样圆，也不表示给猫玩的毛线球。',E('hair + ball → hairball','毛发聚成一团 → 毛球'),
 'a cat hairball 猫毛球，a clump of hair 也可描述毛团；医疗情况要看具体动物，不从词义判断问题轻重。',
 'a cat hairball；a small hairball；cough up a hairball。',
 'hairball 真实毛发形成，a ball of yarn 是毛线球；hairball 也可比喻混乱复杂的一团。',
 ('The cat coughed up a small hairball.','猫咳出了一小团毛球。'),('A hairball blocked the shower drain.','一团毛发堵住了淋浴排水口。'))
W('shorthair','英 /ˈʃɔːtheə/；美 /ˈʃɔːrther/','短毛猫；短毛动物类称呼',
 '用毛短这个外观特点给一类猫命名；British Shorthair 就是英国短毛猫。',
 'short + hair，形容毛短的特征转为动物名词。具体犬猫品种常在前面另加名称。',E('short + hair → shorthair','短毛特征 → 短毛动物名'),
 'a British Shorthair 英国短毛猫，a domestic shorthair 家养短毛猫；品种名常大写。',
 'a British Shorthair；a domestic shorthair；a shorthair cat。',
 'shorthair 名词称动物，short-haired 形容毛短；人剪短发通常说 has short hair，不把人叫 a shorthair。',
 ('They adopted a domestic shorthair from the shelter.','他们从收容所领养了一只家养短毛猫。'),('The British Shorthair sat beside the window.','英国短毛猫坐在窗边。'))
R('B2764','毛发、造型、护理工具与细线比喻','HAIR：整片头发与单根发丝，再看工具和造型','按状态、职业活动、工具用品来读；hairline、hairpin 的比喻接细线与发夹形状。',
 'hair 继承古英语毛发词。现代复合词大多清楚，但整体 hair 不可数、单根 a hair 可数的区别很实用。',
 'hair → hairy、haired、hairless；hair + line、dresser、dressing、stylist、styling、dryer、brush、pin、piece、ball；short + hair。',
 [['核心与毛发状态','hair · hairy · haired · hairless · hairline'],['职业、活动与造型','hairdresser · hairdressing · hairstylist · hairstyling · hairstyle · haircut · hairdo · haircare'],['工具与用品','hairdryer · hairbrush · hairpin · hairpiece'],['毛团与动物名称','hairball · shorthair']],
 'hairstyle 结果，hairstyling 活动，hairstylist 人；hair 整体不可数，a hair 单根可数；hairpin bend 是形状比喻。',
 'The hairstylist used a hairbrush and hairpins to create the hairstyle.\n\n发型师用发刷和发夹做出了这个发型。',
 'hair hairy haired hairless hairline hairdresser hairdressing hairstylist hairstyling hairstyle haircut hairdo haircare hairdryer hairbrush hairpin hairpiece hairball shorthair')
if __name__=='__main__':save('continuation_20261029_ee',ROOTS,WORDS)
