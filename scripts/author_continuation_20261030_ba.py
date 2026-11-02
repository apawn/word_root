"""Drink and wear: old verb changes and ordinary extended meanings."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
DI=[['古英语 drincan、drynċ → 中古英语 drinken、drink → drink','喝；饮品，名动词都有旧形式'],['现代 drink—drank—drunk','喝饮料、喝酒；相关醉态形容词发展']]
def D(f,m):return DI+[[f,m]]
W('drink','/drɪŋk/','喝；饮料；喝酒〔依语境〕',
 '液体从杯子进嘴里是最基本动作；不说喝什么时，drink 也常专指喝酒。',
 '继承古英语 drincan，名词饮品也有旧 drynċ。现代变化 drink—drank—drunk，具体液体由宾语和语境决定，不把所有 a drink 都先当酒。',DI,
 'drink water 喝水，a hot drink 热饮，go for a drink 去喝一杯，I don’t drink. 常说我不喝酒。',
 'drink water；a hot drink；go for a drink；drink in the view。',
 'drink 喝液体，eat 吃固体；soup 常可 have/eat，也可按喝的方式用 drink。a drink 可能饮品或酒，不由冠词直接判定。',
 ('Would you like a hot drink?','你想喝点热饮吗？'),('She drank a glass of water after the walk.','散步后，她喝了一杯水。'))
W('drinking','/ˈdrɪŋkɪŋ/','喝、饮用；饮酒；供饮用的〔修饰用法〕',
 '说喝这件活动；drinking water 则常是供人喝的水，不是水自己正在喝。',
 'drink + -ing，活动名词承接较早形式。-ing 在组合里可说明用途，饮酒义仍靠具体语境。',D('drink + -ing → drinking','喝的活动；饮酒；组合中说明饮用用途'),
 'drinking water 饮用水，drinking habits 饮酒或饮用习惯，a drinking glass 饮水杯。',
 'drinking water；drinking habits；a drinking glass。',
 'drinking water 作名词组合通常是饮用水，He is drinking water 才是他正在喝水；同一串词位置决定结构。',
 ('The village has a new supply of clean drinking water.','村里有了新的清洁饮用水供应。'),('The survey asked about drinking habits.','调查询问了饮酒习惯。'))
W('drinker','英 /ˈdrɪŋkə/；美 /ˈdrɪŋkər/','喝某饮品的人；饮酒者',
 '按喝什么、喝多少来称呼人；tea drinker 只是喝茶的人，单说 heavy drinker 通常偏酒。',
 'drink + -er，古英语 drincere 等人物词已存在。后缀不是自动表示成瘾，是否饮酒和程度看修饰语。',D('古英语 drincere → drinker','喝饮品的人；现代常有饮酒者义'),
 'a tea drinker 喝茶的人，a coffee drinker 咖啡饮用者，a heavy drinker 喝酒多的人。',
 'a tea drinker；a coffee drinker；a heavy drinker。',
 'drinker 饮用者，drunk 可醉了的人且称呼可能贬；a coffee drinker 不意味着每次喝咖啡都会醉。',
 ('I’m more of a tea drinker than a coffee drinker.','比起咖啡，我更常喝茶。'),('The study compared drinkers and people who never drank alcohol.','研究比较了饮酒者和从不饮酒的人。'))
W('drinkable','/ˈdrɪŋkəbl/','可以饮用的；还算能喝的',
 '可能是在说水可供饮用，也可能只是评价一杯咖啡虽不出色但还能喝；语气要看场景。',
 'drink + -able，中古英语已有相应形式。可被喝的能力、适宜性延伸到口味勉强可接受。',D('drink + -able → drinkable','适合饮用；口味可接受'),
 'drinkable water 可饮用水，barely drinkable 勉强能喝，quite drinkable 还算不错、能喝。',
 'drinkable water；barely drinkable；quite drinkable。',
 'drinkable 可能说适宜饮用或味道过得去；delicious 明确好喝。便宜饮料 quite drinkable 不等于在作实验室检测结论。',
 ('The sign says the water is drinkable.','牌子上说这里的水可以饮用。'),('The coffee was weak but drinkable.','咖啡淡了些，但还算能喝。'))
W('drunk','/drʌŋk/','drink 的过去分词；醉的；醉汉〔名词带贬义〕',
 'has drunk 是已经喝了，is drunk 才通常是喝醉了；不能把分词每次都翻成醉。',
 '接 drink 的旧过去分词，古英语 druncen 等较完整形式后来出现 drunk；醉态形容词与喝酒联系。动词分词也可用于喝水，不要求酒精。',DI+[['旧 druncen 等 → drunk','过去分词；专门化的醉态形容词、人物名词']],
 'has drunk water 已经喝水，get drunk 喝醉，be drunk on power 比喻陶醉权力。',
 'has drunk；get drunk；be drunk；drunk on power。',
 'drank 过去式，drunk 分词；I have drunk water 不等于我喝水喝醉了。a drunk 称人常带贬义。',
 ('He has already drunk two glasses of water.','他已经喝了两杯水。'),('The character was too drunk to remember the conversation.','故事中的人物醉得不记得那段对话。'))
W('drunken','/ˈdrʌŋkən/','醉酒的；因醉酒发生的；像醉了般的',
 '修饰那个人、举动或声音都带酒醉状态；常放在名词前。',
 '保留古英语 druncen 等较完整分词形式，现代主要作形容词。不是今天 drunk 再加使成为的 -en 才诞生。',DI[:1]+[['古英语 druncen → drunken','保留较完整的旧分词；现代多作醉态形容词']],
 'a drunken argument 酒后争吵，a drunken passenger 醉酒乘客，drunken laughter 酒醉笑声。',
 'a drunken argument；a drunken passenger；drunken laughter。',
 'He is drunk 常用表语；a drunken argument 常用前置修饰。drunk 也能作前置形容词，不能把这种偏好写成绝无例外的禁令。',
 ('A drunken argument broke out outside the pub.','酒馆外爆发了一场酒后争吵。'),('The scene shows a drunken passenger missing his stop.','场景中，一个喝醉的乘客坐过了站。'),sources=['https://www.etymonline.com/word/drunken','https://en.wiktionary.org/wiki/drunken#English'])
R('B2542','喝、饮品与饮酒；不规则变化和醉态分清','DRINK：喝液体，是否喝酒、是否醉要看结构','drink → drinking、drinker、drinkable；drunk 与 drunken 一起读，说明前者分词和醉态不同；drinkwater 冷门形式先略。',
 '旧动词变化保留 dr-i/dr-a/dr-u，不是 drank、drunk 两个新词根。喝水的完成时与醉态形容词分开。',
 'drink—drank—drunk；drink + -ing/-er/-able；drunken 保留旧较完整分词形。',
 [['动作、活动、人物与可饮用','drink · drinking · drinker · drinkable'],['分词及醉态','drunk · drunken']],
 'drinking water 可能饮用水或正在喝水的结构；has drunk 不等于喝醉；drinker 不自动成瘾；drunken 多形容修饰。',
 'The tea drinker has drunk some water and found the tea quite drinkable.\n\n这位爱喝茶的人喝了些水，也觉得那茶还算能喝。',
 'drink drinking drinker drinkable drunk drunken')
WE=[['古英语 werian → 中古英语 weren → wear','穿、覆盖身体'],['穿用、使用造成损耗','衣物穿旧 → 磨损、使疲惫等引申'],['中古英语类推不规则变化','由旧规则过去形转向 wore、worn，受同韵动词影响']]
def WN(f,m):return WE+[[f,m]]
W('wear','英 /weə/；美 /wer/','穿戴；留着〔胡须等〕、带着〔表情〕；磨损；衣着、损耗〔名词〕',
 '衣服穿在身上是状态，反复穿用又会磨旧；人被事情反复消耗，也能 wear out。',
 '继承古英语 werian 穿、覆盖，耗损义从反复穿用等发展。原先规则变化，后来类推成 wear—wore—worn，不是自古就只能强变化。',WE,
 'wear a coat 穿着外套，wear glasses 戴眼镜，wear a smile 带着笑，wear out 穿坏、使精疲力竭，wear and tear 日常损耗。',
 'wear a coat；wear glasses；wear a smile；wear and tear。',
 'wear 穿戴着的状态，put on 穿上动作；dress 可给人穿衣。What are you wearing? 问穿什么，不是问正在做哪个穿衣动作。',
 ('She wears glasses for reading.','她读书时戴眼镜。'),('Constant use will wear the fabric thin.','反复使用会把面料磨薄。'),sources=['https://www.etymonline.com/word/wear','https://en.wiktionary.org/wiki/wear#English'])
W('worn','英 /wɔːn/；美 /wɔːrn/','wear 的过去分词；磨旧的；疲惫的',
 '可以只是曾穿过，也可以是用久了已经旧、薄；人的脸看着累也能 worn。',
 'wear 的不规则分词，类推 torn、sworn 等同韵词形形成。现代磨损形容词接使用造成消耗的支线，不是过去式 wore。',WE+[['wear → wore → worn','原形、过去式、过去分词；分词也可磨旧、疲惫']],
 'has worn 穿过，worn shoes 磨旧鞋，look worn 显得疲惫；worn out 可物品报废或人累坏。',
 'has worn；worn shoes；look worn；worn out。',
 'has worn the coat 只表穿过，未必外套破了；a worn coat 通常说磨旧外套。分词结构与性质形容词不要总当同义。',
 ('The steps were worn smooth by years of use.','台阶经过多年踩踏，被磨得光滑。'),('She has worn that jacket only once.','那件夹克她只穿过一次。'))
W('wearing','英 /ˈweərɪŋ/；美 /ˈwerɪŋ/','wear 的 -ing 形式；使人疲惫、烦累的',
 'wearing a coat 是穿着外套；a wearing day 则是一天把人的精力慢慢耗下去。',
 'wear + -ing。穿戴分词接基本义；令人疲惫的形容词接 wear 消耗、磨损这条支线。',WN('wear + -ing → wearing','穿戴、磨损的过程；形容使精力耗损的'),
 'be wearing a coat 穿着外套，a wearing journey 累人的旅途，find something wearing 觉得某事耗人。',
 'be wearing；a wearing journey；find it wearing。',
 'wearing 让人疲惫，worn 人已显疲惫或物已旧；The journey was wearing，the traveller looked worn。',
 ('He was wearing a blue shirt.','他穿着一件蓝衬衫。'),('Answering the same question all day was wearing.','一整天回答同样的问题很耗人。'))
W('wearer','英 /ˈweərə/；美 /ˈwerər/','穿戴者',
 '谁把这件衣服、眼镜或设备戴在身上，就从这个角度叫 wearer。',
 'wear + -er，中古英语已有 werer、werere 等人物形式。名字按穿戴角色，不说明是物品主人还是借用者。',WN('wear + -er → wearer','穿戴衣物、饰品或设备的人'),
 'the wearer of the coat 穿外套的人，glasses wearers 戴眼镜者，protect the wearer 保护穿戴者。',
 'the wearer of；glasses wearers；protect the wearer。',
 'wearer 穿戴者，owner 所有者；租来的礼服穿在你身上，你是 wearer，未必是 owner。',
 ('The coat is designed to keep the wearer warm.','这件外套设计来给穿着者保暖。'),('The glasses can be adjusted to fit the wearer.','眼镜可以调整，以适合佩戴者。'))
W('wearable','英 /ˈweərəbl/；美 /ˈwerəbl/','可穿戴的；适合日常穿着的；穿戴设备〔名词〕',
 '衣服做得再特别，能舒服、合适地穿出门才叫 wearable；科技里也指能戴在身上的设备。',
 'wear + -able，最基本是能穿戴。技术名词 wearables 借指手表、追踪器等穿戴设备；不是所有小电子产品都自动属此类。',WN('wear + -able → wearable','可穿戴、好穿；后作穿戴设备名词'),
 'wearable technology 穿戴技术，a wearable device 穿戴设备，a wearable design 适合实际穿着的设计。',
 'wearable technology；a wearable device；wearable designs。',
 'wearable 能戴、适合穿，portable 可携带；电脑能放包里 portable，不一定设计来穿在身上 wearable。',
 ('The collection combines unusual shapes with wearable designs.','这组服装把独特造型与适合实际穿着的设计结合起来。'),('The company makes wearable devices for tracking activity.','公司制造用于记录活动的穿戴设备。'))
R('B3008','穿戴状态与用久磨损；人也会被消耗','WEAR：穿在身上；反复使用会磨损、耗精力','wear → worn、wearing，再 wearer、wearable；变化 wore 直接在基础词说明，所有新增词逐词讲清。',
 '穿戴与损耗有历史联系；不把 wear 当只会穿衣。它还显示英语旧规则动词能后来类推成不规则。',
 'wear—wore—worn；wear + -ing/-er/-able；wear out/down/off 等接不同耗损方向。',
 [['基本状态、分词和耗人过程','wear · worn · wearing'],['穿戴者与适穿、设备','wearer · wearable']],
 'wear 状态、put on 动作；worn 穿过不一定磨坏；wearing 耗人、worn 已疲惫；wearable 可戴与 portable 可带不同。',
 'The wearer was wearing a new device, while the old strap looked worn.\n\n佩戴者戴着新设备，旧表带则显得磨损了。',
 'wear worn wearing wearer wearable')
if __name__=='__main__':save('continuation_20261030_ba',ROOTS,WORDS)
