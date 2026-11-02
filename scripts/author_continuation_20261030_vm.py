"""Useful nouns and their ordinary plural and figurative extensions."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'A1776':dict(words=['dollar','dollars','potato','potatoes','tomato','tomatoes','lane','lanes','shoulder','shoulders'],label='常见单数 → 复数：货币、食物、通道与肩膀',note='本组按复数 s／es 组织阅读，不宣称各底词同源。potatoes、tomatoes 写 es，但结尾仍读 z；其余规则复数也分别说明。'),
}
W('dollar','英 /ˈdɒlə/；美 /ˈdɑːlər/','元〔若干国家和地区的货币单位〕；一元的硬币、纸币〔视语境〕',
 '看到价格 $5，通常会读 five dollars；是哪一种元，要看所在国家、币种标注和上下文。美国、加拿大、澳大利亚等都使用叫 dollar 的货币单位。',
 '较早借低地德语 daler，接德语 Taler／Thaler，是 Joachimstaler 的缩短，原指与 Joachimstal 地名有关的银币。地名里的 Tal 是山谷，与英语 dale 同源；不是现代英语 doll 加 -ar。',
 [['德语 Joachimstaler → Taler／Thaler','按地名命名的银币 → 名称缩短'],['低地德语 daler → 英语 dollar','银币名称 → 不同地区的货币单位']],
 'one dollar 一元；a dollar coin 一元硬币；the US dollar 美元；the Canadian dollar 加拿大元；cost a dollar 售价一元。',
 'a dollar bill；a dollar each。','dollar 不是任何场合都等于美元；US dollar 才明确币种。谈 dollar coin、dollar bill 时，前面的单位词作修饰语，用单数。',
 ('The postcards cost one dollar each.','这些明信片每张一元。'),('Is that price in US dollars or Canadian dollars?','那个价格是美元还是加拿大元？'),sources=['https://www.etymonline.com/word/dollar','https://en.wiktionary.org/wiki/dollar#English'])
W('dollars','英 /ˈdɒləz/；美 /ˈdɑːlərz/','元〔dollar 的复数〕；以元计的金钱',
 '一元是 a dollar，几元是 dollars。金额作一个整体讲时，即使单位写复数，后面的动词也可以用单数。',
 'dollar + -s，词尾读 /z/；继承德语银币名称经低地德语借入的历史。hundred、thousand 后的 dollars 仍须复数：two hundred dollars。',
 [['银币名 → dollar','借入并成为多个币种的单位名'],['dollar + -s → dollars','多个货币单位；具体币种看限定语']],
 'ten dollars 十元；hundreds of dollars 几百元；save a few dollars 省下几元；in dollars 以元为单位。',
 'five dollars each；several thousand dollars。','Five dollars is enough 把金额看作一个整体。a five-dollar ticket 中单位作复合修饰语通常用单数，这与 five dollars 是不同结构。',
 ('Five dollars is enough for the bus fare.','五元够付公交车费。'),('The two tickets cost thirty dollars in total.','两张票一共三十元。'),sources=['https://www.etymonline.com/word/dollar','https://en.wiktionary.org/wiki/dollars#English'])
W('potato','英 /pəˈteɪtəʊ/；美 /pəˈteɪtoʊ/','土豆、马铃薯',
 '挖出来的一颗土豆，可以煮、烤、切片。a potato 说一颗，mashed potato 则把它当做成泥的食物来讲。',
 '经西班牙语相关名称借入，更早联系美洲原住民语言 batata 甘薯名。英语较早也用它说甘薯，后来扩展、固定为常见马铃薯；现代 sweet potato 是甘薯这一不同植物。',
 [['美洲原住民语言 batata 等 → 西班牙语相关形式','甘薯的名称传播'],['英语 potato','较早说甘薯，后来常说马铃薯；两种植物名称发生过扩展']],
 'a baked potato 烤土豆；potato soup 土豆汤；potato salad 土豆沙拉；a hot potato 棘手问题〔比喻〕。复数 potatoes。',
 'peel a potato；mashed potato。','potato 与 tomato 虽然尾部拼写相似，来源词并不相同。a hot potato 像烫手的土豆一样让人难接手，因而比喻棘手、敏感的问题。',
 ('She cut a potato into thin slices.','她把一颗土豆切成薄片。'),('The issue became a political hot potato.','这个问题成了政治上烫手的山芋。'),sources=['https://www.etymonline.com/word/potato','https://www.merriam-webster.com/dictionary/potato','https://en.wiktionary.org/wiki/potato#English'])
W('potatoes','英 /pəˈteɪtəʊz/；美 /pəˈteɪtoʊz/','土豆、马铃薯〔复数〕',
 '一袋、一盘土豆通常不只一颗，所以常用 potatoes。即使做成一道菜，英语仍常沿用这个复数名称。',
 'potato 以 o 结尾，常规复数写 potatoes，加 -es；结尾的 es 在这里读 /z/，不会额外增加一个音节。',
 [['potato','马铃薯；词名有更早甘薯相关历史'],['potato + -es → potatoes','多个土豆；也用于相应菜肴名']],
 'boiled potatoes 煮土豆；roast potatoes 烤土豆；mashed potatoes 土豆泥〔美式尤其常见〕；a bag of potatoes 一袋土豆。',
 'new potatoes；peel the potatoes。','不能把所有 o 结尾名词都套成 es：potatoes、tomatoes 用 es，photos、pianos 通常只加 s。食物的可数、不可数用法还要看具体表达。',
 ('We need three large potatoes for the soup.','做这道汤需要三个大土豆。'),('They served fish with boiled potatoes.','他们端上鱼，配着煮土豆。'),sources=['https://www.merriam-webster.com/dictionary/potato','https://en.wiktionary.org/wiki/potatoes#English'])
W('tomato','英 /təˈmɑːtəʊ/；美 /təˈmeɪtoʊ/','番茄、西红柿',
 '切开多汁、做沙拉或酱汁的番茄，英语叫 tomato。这个常用词的一大特点是英美中间重读元音不同。',
 '经西班牙 tomate 接纳瓦特尔语 tomatl 等番茄名称；英语较早形式是 tomate，现代 o 结尾可能受 potato 拼写影响。拼写互相影响不等于词源相同。',
 [['纳瓦特尔语 tomatl → 西班牙 tomate','美洲植物名称传播'],['英语 tomate → tomato','借入后拼写变化；可能受 potato 影响']],
 'a ripe tomato 熟番茄；tomato sauce 番茄酱汁；tomato soup 番茄汤；a tomato plant 番茄植株。复数 tomatoes。',
 'slice a tomato；fresh tomato sauce。','英国常读 /mɑː/，美国常读 /meɪ/，都是常见标准读法。tomato sauce 常指烹饪用番茄酱汁，不能在所有场景都等同瓶装 ketchup。',
 ('She added a sliced tomato to the sandwich.','她往三明治里加了一颗切片的番茄。'),('We made a simple tomato sauce for the pasta.','我们为意面做了一份简单的番茄酱汁。'),sources=['https://www.etymonline.com/word/tomato','https://en.wiktionary.org/wiki/tomato#English'])
W('tomatoes','英 /təˈmɑːtəʊz/；美 /təˈmeɪtoʊz/','番茄、西红柿〔复数〕',
 '篮子里有几个番茄，就是 tomatoes。做菜时切碎的一堆番茄，也常按原来的可数食材说 chopped tomatoes。',
 'tomato + -es → tomatoes；结尾读 /z/，不增加音节。单数中的英美重读元音差异保留在复数里。',
 [['tomato','经西班牙语借入的番茄名称'],['tomato + -es → tomatoes','不止一个番茄；食材的常见复数表达']],
 'chopped tomatoes 切碎番茄；tinned tomatoes 罐装番茄〔英式〕；canned tomatoes 罐装番茄〔美式〕；a few tomatoes 几个番茄。',
 'grow tomatoes；ripe tomatoes。','tomato soup 中修饰语通常是单数；some tomatoes 作名词时是复数。不能因为它们在菜里已经切碎，就认定英语一定要改成不可数。',
 ('The tomatoes in our garden are finally ripe.','我们菜园里的番茄终于熟了。'),('Add the chopped tomatoes and stir gently.','加入切碎的番茄，轻轻搅拌。'),sources=['https://www.etymonline.com/word/tomato','https://en.wiktionary.org/wiki/tomatoes#English'])
W('lane','/leɪn/','小路、巷道；车道；泳道、跑道分道等',
 '两旁有边界，中间留出一条供通过的带状空间。乡间是小路，道路上是车道，泳池里则是泳道。',
 '承接古英语 lane、lanu 狭窄围路，经中古英语 lane 延续。更早日耳曼语来源不明；现代 lane 是完整词，不是 line 随便换一个元音。',
 [['古英语 lane、lanu → 中古英语 lane','两侧围起、较窄的通道'],['现代 lane 的不同场景','乡间路、车道、跑道分道、泳道']],
 'a country lane 乡间小路；a bus lane 公交专用道；a cycle lane 自行车道；a swimming lane 泳道；change lane 换车道。',
 'a narrow lane；stay in your lane。','road 是整条道路，lane 可是其中一个分道。line 通常是线本身，lane 是供通行的一条空间；这能帮助理解它们的区别。',
 ('A narrow lane leads from the village to the river.','一条窄路从村庄通向河边。'),('She was swimming in the next lane.','她在旁边的泳道游泳。'),sources=['https://www.etymonline.com/word/lane','https://en.wiktionary.org/wiki/lane#English'])
W('lanes','/leɪnz/','小路、车道、泳道、跑道分道等〔复数〕',
 '一条路可以分成几条车道，泳池也可以分成几条泳道。数这些并排或相连的通行带时，用 lanes。',
 'lane + -s，词尾 /n/ 后读 /z/；继承古英语狭窄、两侧有边界的通道词。现代复数适用于道路、游泳、田径等具体场景。',
 [['古英语通道词 → lane','一条有边界的通行空间'],['lane + -s → lanes','多条小路或分道']],
 'two lanes 两条车道、泳道等；change lanes 换车道；cycle lanes 自行车道；quiet country lanes 安静的乡间小路。',
 'separate lanes；the outside lanes。','The road has three lanes 是这条道路有三个车道，不是三条道路。换道常用 change lanes 这个复数搭配。',
 ('The pool has six lanes.','这个泳池有六条泳道。'),('We explored the quiet lanes behind the village.','我们逛了村后那些安静的小路。'),sources=['https://www.etymonline.com/word/lane','https://en.wiktionary.org/wiki/lanes#English'])
W('shoulder','英 /ˈʃəʊldə/；美 /ˈʃoʊldər/','肩、肩膀；肩部、路肩；承担；用肩挤、推',
 '手臂与躯干相接的肩膀能扛东西，因此英语也用 shoulder 说把责任、成本扛到自己身上。',
 '来自古英语 sculdor，经中古英语 shulder 等形式延续，更早来源不明。动词由身体部位名转用，先有用肩推、扛起的动作，再可说承担抽象负担。',
 [['古英语 sculdor → shoulder 名词','肩膀；较早也比喻支撑负担的能力'],['shoulder 名词 → 动词','用肩推、扛起 → 承担责任、成本']],
 'a shoulder bag 单肩包；tap someone on the shoulder 轻拍某人肩膀；shoulder responsibility 承担责任；the shoulder of a road 路肩。',
 'look over your shoulder；shoulder the burden。','shoulder 既能是部位，也能是动作。shoulder the cost 说承担费用；shoulder past someone 则是用肩挤着从旁边过去，靠宾语和搭配区分。',
 ('She tapped me on the shoulder to get my attention.','她轻拍我的肩膀，让我注意她。'),('The manager agreed to shoulder the responsibility.','经理同意承担责任。'),sources=['https://www.etymonline.com/word/shoulder','https://en.wiktionary.org/wiki/shoulder#English'])
W('shoulders','英 /ˈʃəʊldəz/；美 /ˈʃoʊldərz/','肩膀〔复数〕；承担、用肩推〔shoulder 的第三人称单数〕',
 '说双肩时是 shoulders；说某一个人现在扛起某种责任时，动词也会写成 shoulders。相同的字形，要靠句子里的位置判断。',
 '名词 shoulder + 复数 -s，或动词 shoulder + 第三人称单数 -s，两者都读 /z/。身体肩膀和承担负担的动词关系清楚，但两个 s 的语法作用不同。',
 [['shoulder 肩膀 → shoulder 动词','身体承重 → 扛起、承担'],['名词 + -s／动词 + -s → shoulders','多个肩膀；他、她、它承担']],
 'shrug your shoulders 耸肩；broad shoulders 宽阔的肩膀；on someone’s shoulders 由某人承担；She shoulders the cost 她承担费用。',
 'relax your shoulders；shoulders the responsibility。','shrugged his shoulders 中 shoulders 是名词宾语；He shoulders the burden 中 shoulders 是谓语动词。on her shoulders 说责任压在她身上，用复数。',
 ('He shrugged his shoulders and said nothing.','他耸了耸肩，什么也没说。'),('The responsibility rests on her shoulders.','这份责任落在她肩上。'),('She shoulders most of the work during the week.','平日里大部分工作由她承担。'),sources=['https://www.etymonline.com/word/shoulder','https://en.wiktionary.org/wiki/shoulders#English'])
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_vm',ROOTS,WORDS)
 extend_lessons()
