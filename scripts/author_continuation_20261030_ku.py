"""Ock: clear old diminutives and words whose remoter analysis is disputed."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
O=[['古英语 -uc、-oc 等 → -ock','小称后缀，许多词后来成为固定名称'],['bulluc → bullock 等较清楚的例子','小公牛等旧称；现代意义不总保留小'],['词形变化与不确定分析','maggot、paddock 等看各自历史；donkey、hulk、husk、tussock 的远源不都能定为同一路']]
W('bullock','/ˈbʊlək/','小公牛；阉公牛〔不同地区、用途有差别〕',
 '历史像在 bull 后加小称，说小公牛；现代有些地区主要指阉公牛，尤其见于农事、役畜语境。不能每次只凭小后缀判断年龄。',
 '古英语 bulluc 经中古英语 bullok 传下，现代对应 bull + -ock。小称已凝固，实际所指由地区、时代确定。',O[:2],
 'a bullock cart 牛车，a team of bullocks 一队役牛，a young bullock 一头小公牛等。bullock 的特定义与 bull、ox、steer 的使用范围有重叠。',
 'a bullock cart；a team of bullocks。',
 'bullock 不保证总是幼小；也不要和 bollocks 的拼写、元音及粗俗用法混淆。',
 ('A bullock cart moved slowly along the road.','一辆牛车沿路缓缓前行。'),('The farmer led the bullocks into the field.','农夫把那几头牛牵进田里。'),sources=['https://en.wiktionary.org/wiki/bullock#English','https://www.merriam-webster.com/dictionary/bullock'])
W('paddock','/ˈpædək/','围栏牧地、马围场；赛马、赛车的围场区域',
 '有边界的一块地，让马等动物活动、放牧，常叫 paddock；比赛里又固定为马匹、车辆集结、准备的区域。',
 '围场义来自 parrock 等变形，上接古英语 pearroc 围起来的地方，与 park 有历史联系。另有 pad 蛙、蟾蜍 + 小称的古同形词，不能拿它解释现代马围场。',
 [['古英语 pearroc → 中古英语 parrock → paddock','围起来的场地；与 park 相关'],['场地用途扩展','动物活动、赛前准备；澳新等还可泛说较大牧场地块']],
 'a horse paddock 马围场，the racing paddock 赛事围场，in the paddock 在围场里。澳新等用法不要求都很小。',
 'a horse paddock；in the paddock。',
 'paddock 围场义不来自现代 pad 垫子加 -ock；赛车 paddock 与比赛跑道、维修通道也不是完全同一区域。',
 ('The horses grazed in the paddock behind the stable.','马在马厩后面的围场里吃草。'),('The mechanics returned to the paddock after the race.','比赛后，机械师回到围场。'),sources=['https://en.wiktionary.org/wiki/paddock#English','https://www.etymonline.com/word/paddock'])
W('maggot','/ˈmæɡət/','蛆、蝇类的无足幼虫',
 '苍蝇等双翅目昆虫的幼虫阶段，常见软软、没有足的形态，叫 maggot。它不是所有小虫的通称。',
 '中古英语 magot 等通常联系更早 maddock、maðek 等幼虫词，基础可追到古英语 maþa，涉及旧小称及词形变化。不能按现代 made 做的过去式 + -ock 望文生义。',O[:1]+[['maþa 等幼虫词 → maddock、maðek → maggot','旧小称形式及词形变化，现代已不透明']],
 'fly maggots 蝇蛆，maggots in decaying matter 腐败物中的蛆。普通生物名称要与 caterpillar 蝶蛾幼虫等区分。',
 'fly maggots；maggots in decaying matter。',
 'maggot 不是蚯蚓 earthworm；名字和腐败物常有联系，不表示蛆是由腐烂物自己生成。',
 ('The students observed fly maggots under a magnifying glass.','学生用放大镜观察蝇蛆。'),('Maggots moved beneath the discarded food.','被丢弃的食物下面有蛆在动。'),sources=['https://en.wiktionary.org/wiki/maggot#English','https://www.etymonline.com/word/maggot'])
W('husk','/hʌsk/','谷物、果实等的壳皮；空壳；去壳',
 '米、玉米等外面包着壳皮，husk 抓住的是外部包覆层；内容已经不在、只剩外壳，也可借来形容建筑、物件。',
 '中古英语 huske 已指果实、种子外皮，远源不明。有旧覆盖物加小称、荷兰语小房子等分析，但不能认定唯一是现代 hose + -ock。动词再从名词发展去壳。',O[:1]+[['中古英语 huske → husk','外皮、壳；远源有不同小称、覆盖物解释'],['名词 → 动词和空壳比喻','去壳；只剩外部的结构']],
 'corn husks 玉米苞叶，rice husks 稻壳，husk corn 给玉米去苞叶，a burnt husk 烧后残存的外壳。',
 'corn husks；rice husks；husk corn。',
 'husk 常说较干、包覆的外层，skin、peel 的搭配各有惯例。壳皮也可能有其他用途，词义不等于完全无用。',
 ('She removed the husks from the corn.','她把玉米的苞叶剥掉。'),('Only a blackened husk remained of the barn.','谷仓只剩一副烧黑的空壳。'),sources=['https://en.wiktionary.org/wiki/husk#English','https://www.etymonline.com/word/husk'])
W('hulk','/hʌlk/','废弃、失去原功能的船体；庞大躯壳、大块头',
 '一艘船设备拆去、只剩大船壳，可是 a hulk；一座巨大废楼、一辆报废大车，也能借这个庞大躯壳的形象。',
 '古英语 hulc 已是船名，中古英语又受大陆日耳曼船词影响。更早有希腊语船名与空穴、小称等不同分析；不能把现代 hole + -ock 当作确定历史。',O[:1]+[['古英语 hulc 等船名 → hulk','船名 → 残存船体、庞大躯壳'],['体积形象的扩展','大块头、巨大结构等']],
 'a rusting hulk 生锈的大型残骸，the hulk of a ship 船壳，a hulk of a man 大块头男人〔口语〕。大写 Hulk 也可作虚构人物名称。',
 'a rusting hulk；the hulk of a ship。',
 'hulk 不是 hull 的普通拼写变体：hull 船体本身，hulk 常突出旧船、躯壳或巨大笨重的存在。',
 ('The old ship remained as a rusting hulk in the harbor.','旧船成了一副生锈的船壳，留在港里。'),('The factory’s empty hulk dominated the skyline.','工厂庞大的空壳占据着天际线。'),sources=['https://en.wiktionary.org/wiki/hulk#English','https://www.etymonline.com/word/hulk'])
W('donkey','英 /ˈdɒŋki/；美 /ˈdɑːŋki/','驴；顽固或愚笨的人〔贬义比喻〕',
 '常见长耳、像马而通常较小的家畜是 donkey。拿来形容人时，多半借顽固、笨等文化印象，是评价，不是动物学结论。',
 '18世纪末已有，原为口语、方言词，远源不确定。可能联系 dun 灰褐色动物名加小称，也有人联系名字 Duncan；不能断言 dun + -ock + -ie 是唯一证实拆法。',O[:1]+[['口语、方言 donkey','驴；颜色、小称或人名来源有不同分析']],
 'a donkey carrying bags 驮包的驴，a donkey ride 骑驴；donkey’s years 是很久的口语搭配。',
 'a donkey ride；donkey’s years。',
 'donkey 与 monkey 不因尾部相像就属同一构词家族；词源中谈可能影响，不等于能把动物随便互推。',
 ('The donkey carried bags along the narrow path.','驴沿窄路驮着包。'),('I have not seen him for donkey’s years.','我很久很久没见过他了。'),sources=['https://en.wiktionary.org/wiki/donkey#English','https://www.etymonline.com/word/donkey'])
W('tussock','/ˈtʌsək/','草丛、草墩',
 '草不是平平铺着，而是从一处密密长成一簇、顶起小墩，可以叫 tussock。',
 '较早有一束毛发的用法，后来用于成簇的草。可能是旧 tusk 束、簇义的小称，远源不定；不是用现代 tusk 长牙义硬推草是小象牙。',O[:1]+[['较早的毛发束义 → tussock','成束、成簇 → 草丛、草墩']],
 'a tussock of grass 一簇草，tussock grass 丛生草类，between the tussocks 在草墩间。具体植物可有多个种类。',
 'a tussock of grass；between the tussocks。',
 'tussock 重点是聚成簇、成墩的生长形态，不是所有草地的通称；lawn 则是草坪。',
 ('A small bird disappeared behind a tussock of grass.','一只小鸟躲到草墩后面，不见了。'),('The path wound between the tussocks.','小路在草丛墩间蜿蜒。'),sources=['https://en.wiktionary.org/wiki/tussock#English','https://www.etymonline.com/word/tussock'])
R('A1969','旧小称后缀及词形变化，按证据分开确定与不确定来源','OCK：小称常藏在旧词里，现代不必仍表示小','bullock、hillock 等看小称；maggot 看旧虫名变化；paddock 分围场与古蛙名；其他词的远源分析另列。',
 '这一组不能整齐地画成同一种公式。小称可能凝固、变音，也可能只是某种尚未确定的分析；先学真实常用意思，再看来源的确定程度。',
 '古英语 -uc、-oc 等 → -ock；现代各词看历史词干、变体，不照字母机械拆分。',
 [['较清楚的小称及固定身体词','bullock · hillock · buttock'],['旧名、同形与词形变化','maggot · paddock'],['远源分析有讨论的物件、动物名','husk · hulk · donkey · tussock · shuck'],['常用形容词与同形鱼名分开','bleak']],
 '现代 bullock 不一定小；paddock 围场不能按蛙解释；hulk、husk、donkey 不定作唯一小称来源；bleak 的常用形容词另源。',
 'A donkey waited in the paddock beside a tussock of grass.\n\n一头驴在围场里的一簇草旁等着。','bullock hillock buttock maggot paddock husk hulk donkey tussock shuck bleak')
if __name__=='__main__':save('continuation_20261030_ku',ROOTS,WORDS)
