"""Common animals, pets and countable food names."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'B2543':dict(words=['cow','cows'],label='cow → cows：母牛；威吓动词另源',note='动物 cow 延续古英语 cū，威吓动词通常接古诺尔斯语 kúga；现代第三人称和名词复数同写 cows。'),
 'B3044':dict(words=['goat','goats'],label='goat → goats：山羊的复数',note='goat 接古英语 gāt 等日耳曼旧名称；goats 在 /t/ 后加 /s/，不另加音节。'),
 'B3053':dict(words=['pig','pigs'],label='pig → pigs：猪；pigs out 的大吃',note='pig 接中古英语 pigge 等，远源未定；现代 pigs 可作复数，也可作动词第三人称。'),
 'A1783':dict(words=['chicken','chickens'],label='chicken → chickens：可数的鸡与食物鸡肉',note='chicken 接古英语 cicen 等；chickens 数鸡，鸡肉义通常用不可数 chicken。'),
 'B2628':dict(words=['fish','fishes'],label='fish → fish／fishes：名词复数与动词形式',note='普通复数常用 fish，fishes 也是复数，尤其常在不同种类等语境；动词第三人称则用 fishes。'),
 'B3154':dict(words=['pet','pets'],label='pet → pets：宠物；轻抚',note='pet 经苏格兰语相关称呼进入一般英语，可能联系盖尔语 peata；动词由宠爱、宠物关系发展。'),
 'A1776':dict(words=['rabbit','rabbits'],label='rabbit → rabbits：兔子的普通复数',note='rabbit 较早用于幼兔，后来成为兔的常用名；更早借入路线有讨论，不硬拆现代 rabbit 的末尾。'),
}
W('cows','/kaʊz/','母牛〔复数〕；威吓、使畏缩〔另源 cow 的第三人称单数〕',
 '农场里产奶的成年母牛，可以叫 cows。另一种动词用法说强势态度把人压得不敢反对，也写 cows，但它来自另一条路线。',
 'cow + -s，元音后读 /z/。动物名接古英语 cū；威吓动词通常联系古诺尔斯语 kúga 压迫，近源不同。',
 [['古英语 cū → 动物 cow；另路古诺尔斯语 kúga 等 → 威吓动词 cow','母牛；压迫、吓住，两路分开'],['各路 cow + -s → cows','多头母牛；单数主语使人畏缩']],
 'dairy cows 奶牛；milk the cows 给母牛挤奶；cows in a field 田野里的母牛；cows someone into silence 吓得某人不敢作声。',
 'a herd of cows；cows grazing nearby。','cows 通常是成年母牛，cattle 是较广的牛类集合称呼。cow 还可说其他大型动物的雌性，但不能据此把所有 cattle 都当成母牛。',
 ('The cows came back to the farm before sunset.','母牛在日落前回到了农场。'),('His loud voice cows the quieter members into silence.','他的大嗓门把较安静的成员吓得不敢说话。'),sources=['https://en.wiktionary.org/wiki/cows#English','https://en.wiktionary.org/wiki/cow#English'])
W('goats','英 /ɡəʊts/；美 /ɡoʊts/','山羊；goat 的复数',
 '多只山羊就是 goats。山羊与绵羊在英语里用不同常用词区分，读农场、食物或动物描写时很实用。',
 'goat + -s，/t/ 后读 /s/。goat 接古英语 gāt，经中古英语 goot、got 等发展，属于旧日耳曼动物名称，更远来源未定。',
 [['古英语 gāt → 中古英语 goot／got → goat','山羊'],['goat + -s → goats','多只山羊']],
 'wild goats 野山羊；a herd of goats 一群山羊；goats’ milk 山羊奶；goats on the hillside 山坡上的山羊。',
 'keep goats；feed the goats。','goats 是山羊，sheep 是绵羊。goat 的复数加 s，sheep 的单复数通常同形：two goats、two sheep。',
 ('The goats climbed onto the rocks beside the path.','山羊爬上了小路旁的岩石。'),('The farm keeps goats as well as sheep.','这家农场既养山羊，也养绵羊。'),sources=['https://en.wiktionary.org/wiki/goats#English','https://en.wiktionary.org/wiki/goat#English'])
W('pigs','/pɪɡz/','猪〔复数〕；pigs out 表大吃〔口语动词形式〕',
 '动物名是 pigs；口语 pig out 借用大口吃的画面说吃得很多，单数主语后写 pigs out。',
 'pig + -s，/ɡ/ 后读 /z/。pig 接中古英语 pigge 及更早相关动物词形，较远来源未定；现代动词用法从名词发展。',
 [['早期英语相关猪名 → 中古英语 pigge → pig','猪的名称'],['pig 名词、动词 + -s → pigs','多头猪；在 pig out 中说大吃']],
 'farm pigs 农场饲养的猪；feed the pigs 喂猪；pigs in the field 地里的猪；pigs out on snacks 口语说大吃零食。',
 'a group of pigs；pigs and chickens。','pig 是动物，pork 通常是食用猪肉。类似地，cow／cattle 是动物名称，beef 是牛肉；这些常用食物名称来自不同借入、传承路线。',
 ('The pigs ran towards the farmer at feeding time.','到了喂食时间，猪朝农场主跑去。'),('He sometimes pigs out on snacks while watching films.','他看电影时有时会猛吃零食。'),sources=['https://en.wiktionary.org/wiki/pigs#English','https://en.wiktionary.org/wiki/pig#English'])
W('chickens','/ˈtʃɪkɪnz/','鸡〔复数〕；chicken 的第三人称单数形式〔如 chickens out 临阵退缩〕',
 '数一只只鸡，用 chickens；把鸡当食材、不按整只来数时，常用 chicken。chicken out 又把胆怯的口语感觉发展为临阵退缩。',
 'chicken + -s，词尾 /z/。chicken 继承古英语 cicen 等，远源可能涉及鸟叫与指小材料；现代 chick 的常见鸟义后来从相关形式缩短，不把现代词长短当成唯一历史顺序。',
 [['古英语 cicen 等 → chicken','鸡、幼鸡等旧动物名称'],['chicken 名词、动词 + -s → chickens','多只鸡；在 chicken out 中说退缩']],
 'keep chickens 养鸡；feed the chickens 喂鸡；roast chickens 一只只烤鸡；chickens out at the last minute 最后关头打退堂鼓。',
 'chickens in the yard；two whole chickens。','two chickens 可说两只活鸡，也可以是两只整鸡；some chicken 常说一些鸡肉。可数与不可数的变化，关键是按动物、整只来数，还是按食材来谈。',
 ('We keep a few chickens behind the house.','我们在屋后养了几只鸡。'),('He agrees to perform, then chickens out at the last minute.','他答应上台表演，却在最后关头退缩了。'),sources=['https://en.wiktionary.org/wiki/chickens#English','https://en.wiktionary.org/wiki/chicken#English'])
W('fishes','/ˈfɪʃɪz/','鱼〔fish 的一种复数，常见于种类等语境〕；捕鱼、钓鱼〔动词形式〕',
 '说好几条鱼，最常用的复数仍是 fish；fishes 也存在，尤其常在谈不同种类时见到。若句子是 He fishes，则是在说他钓鱼。',
 'fish + -es；原词以 /ʃ/ 结尾，加 /ɪz/。名词接古英语 fisc，动词接 fiscian 等，现代复数形式与动词第三人称都可写 fishes。',
 [['古英语 fisc／fiscian → fish 名词、动词','鱼；捕鱼'],['fish + -es → fishes；另有常见同形复数 fish','若干鱼，尤其不同种类等语境；单数主语捕鱼']],
 'freshwater fishes 淡水鱼类；the fishes of a region 某地区的鱼类；fishes in the river 在河里捕鱼；fishes for compliments 设法让别人夸自己。',
 'different fishes；fishes on weekends。','two fish 是普通日常数鱼的说法。fishes 不只在一个绝对限定场景里才合法，但不同鱼类、较书面叙述中更常见；He fishes 则是规则动词形式。',
 ('The guide describes the freshwater fishes of the region.','指南介绍了该地区的淡水鱼类。'),('He fishes in the lake on quiet summer mornings.','夏天安静的早晨，他会在湖里钓鱼。'),sources=['https://en.wiktionary.org/wiki/fishes#English','https://en.wiktionary.org/wiki/fish#English'])
W('pets','/pets/','宠物〔复数〕；轻抚、抚摸〔pet 的第三人称单数〕',
 '养在身边、照料和亲近的动物是 pets；用手温柔地摸它们，pet 又可以作动词。',
 'pet + -s，/t/ 后读 /s/。pet 经苏格兰语相关称呼进入一般英语，可能接盖尔语 peata 被宠爱的动物、孩子，更远来源未定；抚摸等动词由名词发展。',
 [['苏格兰语相关 pet，可能联系盖尔语 peata → pet','受照料、宠爱的动物；后来有宠物义'],['pet 名词、动词 + -s → pets','多只宠物；单数主语抚摸']],
 'keep pets 养宠物；pets allowed 允许携带宠物；pets the dog 抚摸狗；household pets 家庭宠物。',
 'a home for pets；pets a cat gently。','pets 在 The pets are asleep 中是复数名词；在 She pets the dog 中是动词。pet 作形容词的 a pet project 则说特别钟爱的项目，要看整体搭配。',
 ('The hotel allows small pets in some rooms.','这家酒店允许部分客房携带小宠物入住。'),('She pets the cat while reading on the sofa.','她坐在沙发上读书时，轻轻抚摸着猫。'),sources=['https://en.wiktionary.org/wiki/pets#English','https://en.wiktionary.org/wiki/pet#English'])
W('rabbit','/ˈræbɪt/','兔、家兔等；兔肉〔食物语境〕',
 '最常见的画面是长耳朵、会跳、常见于宠物或洞穴生活描写的兔子。rabbit 可以数动物，菜单上也可以说兔肉。',
 '中古英语 rabet 较早指幼兔，后来扩大为常见兔名。可能经北法语方言的指小形式联系荷兰语等相关兔名 robbe，但具体借入路线、更远来源未定；不把现代 -it 当万能指小后缀。',
 [['中古英语 rabet；可能联系北法语方言及荷兰语相关兔名','较早指幼兔；更早路线有讨论'],['英语 rabbit','范围扩大为常用兔名；食物语境可指兔肉']],
 'a pet rabbit 宠物兔；a rabbit hole 兔子洞，也可比喻越钻越深的问题、话题；rabbit ears 兔耳朵，也可说外形相似的东西。',
 'a wild rabbit；a rabbit in the garden。','rabbit 是中性常用名称，bunny 更有亲昵、口语色彩，不必只指幼兔。谈食物时 some rabbit 可以是一些兔肉，而 two rabbits 通常按整只来数。',
 ('A rabbit disappeared into a hole beside the fence.','一只兔子钻进了篱笆旁的洞里。'),('Their pet rabbit likes to hide under the chair.','他们的宠物兔喜欢躲在椅子下面。'),sources=['https://en.wiktionary.org/wiki/rabbit#English','https://www.etymonline.com/word/rabbit'])
W('rabbits','/ˈræbɪts/','兔子〔复数〕；rabbit 的复数形式',
 '一只兔是 rabbit，多只兔就是 rabbits。数量变化很简单，词尾要把原来的 /t/ 和复数 /s/ 连起来。',
 'rabbit + -s，/t/ 后读 /s/。rabbit 接中古英语 rabet，较早指幼兔，后来成为常用兔名；北法语、荷兰语等较早关联路线仍有不确定性。',
 [['中古英语 rabet → rabbit','幼兔名逐渐扩大为常用兔名'],['rabbit + -s → rabbits','多只兔']],
 'wild rabbits 野兔；pet rabbits 宠物兔；rabbits in the garden 花园里的兔；pull rabbits out of a hat 字面指魔术中变出兔子，也可比喻拿出意外办法。',
 'two rabbits；rabbits hiding in the grass。','rabbits 是复数，rabbit’s 指一只兔的，rabbits’ 指多只兔的。hare 是另一常用兔类名称，具体动物描述中不要只因中文都能叫兔就随意替换。',
 ('We saw three rabbits at the edge of the field.','我们在田野边看见了三只兔子。'),('The rabbits’ enclosure has a shaded corner.','兔子的围栏里有一处阴凉角落。'),sources=['https://en.wiktionary.org/wiki/rabbits#English','https://en.wiktionary.org/wiki/rabbit#English'])
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_wl',ROOTS,WORDS)
 extend_lessons()
