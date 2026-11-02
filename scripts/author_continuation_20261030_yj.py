"""Everyday food: portions, kinds, meals, and the sandwich name."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'B3304':dict(words=['meal','meals'],label='meal → meals：一顿顿饭',note='用餐词与谷粉词有不同来源，本组复数主要说用餐。'),
 'B2828':dict(words=['breakfast','breakfasts'],label='breakfast → breakfasts：结束禁食的一餐',note='break 结束与 fast 禁食组合，复数可数不同份或不同天的早餐。'),
 'B3305':dict(words=['lunch','lunches'],label='lunch → lunches：午餐与吃午餐',note='便餐、午餐相关旧词发展，较早来源保留不确定性。'),
 'B3306':dict(words=['dinner','dinners'],label='dinner → dinners：主餐与宴会',note='借入后用餐时间变化，dinner 并非在所有语境都只能指晚餐。'),
 'B2542':dict(words=['drink','drinks'],label='drink → drinks：饮品与喝',note='本族名动词都有旧形式，第三人称单数与名词复数同形。'),
 'B2496':dict(words=['food','foods'],label='food → foods：食物总体与食物种类',note='通常不可数的 food 在区分种类、食品品项时可用 foods。'),
 'B2946':dict(words=['bread','breads'],label='bread → breads：面包总体与不同种类',note='bread 通常不可数，breads 用于种类、产品等语境。'),
 'B3028':dict(words=['cake','cakes'],label='cake → cakes：蛋糕与结块',note='北欧糕饼名称借入，又有团块及附着的动词发展。'),
 'B2486':dict(words=['apple','apples'],label='apple → apples：苹果与复数',note='本族果实名称延续，现代常用义已集中到苹果。'),
 'B2465':dict(words=['meat','meats'],label='meat → meats：肉类与品种',note='旧食物义缩窄到常见的动物肉义，meats 常区分肉类品种。'),
 'B3177':dict(words=['coffee','coffees'],label='coffee → coffees：咖啡、杯份与种类',note='借词随贸易传播，现代复数常按份或种类数。'),
 'B3404':dict(words=['tea','teas'],label='tea → teas：茶、份数与茶餐',note='闽南语茶的名称经贸易语言传播，英语有饮品、种类、茶餐等用法。'),
 'A1776':dict(words=['sandwich','sandwiches'],label='sandwich → sandwiches：人名转食物名与 -es',note='名称联系 Sandwich 伯爵头衔，相关用餐故事属传统说法；现代复数在 ch 后加 es。'),
 'B3786':dict(words=['kitchen','kitchens'],label='kitchen → kitchens：烹调空间',note='拉丁烹调处词较早借入日耳曼语，经古英语延续。'),
}
W('meals','/miːlz/','一顿顿饭；餐食〔meal 的复数〕',
 '把吃饭看成一次完整的用餐，就是 a meal；早餐、午餐、晚餐都属于一顿顿 meals。这个一餐义原来就与固定时刻有关。',
 'meal + -s，/l/ 后读 /z/。一餐 meal 接古英语 mǣl 时刻、场合、用餐；谷物粉的同形 meal 接 melu，是磨碎词族的另一来源。',
 [['古英语 mǣl → 中古英语 → meal','时刻、用餐场合 → 一顿饭'],['meal + -s → meals','多次用餐、多份餐食；与谷粉支分开']],
 'regular meals 规律的三餐；cook meals 做饭；meals included 包餐；between meals 两餐之间。',
 'three meals a day；prepare meals for the family。','food 说吃的东西总体，meals 把一次次用餐当作单位。The price includes meals 常说价格包含餐食，具体几餐要看说明。',
 ('The children eat their meals together.','孩子们一起吃饭。'),('The room price includes two meals a day.','房价包含每天两餐。'),sources=['https://en.wiktionary.org/wiki/meals#English','https://www.etymonline.com/word/meal'])
W('breakfasts','/ˈbrekfəsts/','多份早餐、多次早餐；吃早餐〔第三人称单数〕',
 '把早餐按每天一次、每人一份来数，就能说 breakfasts；酒店说供应多少份早餐，用的是这个可数画面。',
 'breakfast + -s，/t/ 后读 /s/，末尾为 /sts/。中古英语 brekefast 由 break 结束与 fast 禁食组合，指结束夜间不进食的时段；现代常用读音已经弱化。',
 [['break 结束 + fast 禁食 → breakfast','结束空腹 → 早餐'],['breakfast + -s → breakfasts','多份、多次早餐；单数主语吃早餐']],
 'cooked breakfasts 热早餐；hotel breakfasts 酒店早餐；breakfasts at seven 七点吃早餐〔动词用法〕。',
 'breakfasts served downstairs；two breakfasts and a pot of tea。','平时说吃早餐用 have breakfast，不必加 a；强调一份、一次或某种早餐时可用 a breakfast、breakfasts。动词 breakfast 较正式或带叙述色彩。',
 ('The café serves hot breakfasts until eleven.','这家咖啡馆供应热早餐到十一点。'),('Our breakfasts arrived with a large pot of tea.','我们的早餐送来时，还配了一大壶茶。'),sources=['https://en.wiktionary.org/wiki/breakfasts#English','https://en.wiktionary.org/wiki/breakfast#English'])
W('lunches','/ˈlʌntʃɪz/','午餐〔复数〕；吃午餐〔第三人称单数〕',
 '每天中午吃的那一顿，按不同天、不同份来数，就是 lunches；和同事中午一起吃饭，也可用 lunch 作动词。',
 'lunch + -es，/tʃ/ 后增加 /ɪz/。现代 lunch 的午餐义通常联系 luncheon 的缩短，较早两词还有一块食物、便餐等用法，具体远源不定。',
 [['早期 lunch、luncheon 等 → 午餐义 lunch','食物块、便餐相关旧义；近代午餐名称'],['lunch + -es → lunches','多份、多次午餐；单数主语吃午餐']],
 'packed lunches 自带午餐；school lunches 学校午餐；lunches with colleagues 和同事吃午餐。',
 'lunches in paper bags；lunches at a nearby café。','have lunch 很普通；lunches with somebody 作动词较偏叙述。packed lunches 指提前准备好带着吃的午餐，未必都装在专门餐盒里。',
 ('We packed our lunches before leaving home.','出门前，我们准备好了要带的午餐。'),('She often lunches with colleagues on Fridays.','她周五经常和同事一起吃午餐。'),sources=['https://en.wiktionary.org/wiki/lunches#English','https://en.wiktionary.org/wiki/lunch#English'])
W('dinners','/ˈdɪnəz/；美式常 /ˈdɪnərz/','多次主餐、晚餐；宴会〔dinner 的复数〕',
 '一天比较正式、丰盛的主餐，是 dinner；按一场场家庭晚餐、宴会来数，就是 dinners。一天中吃主餐的时间会随习惯变化。',
 'dinner + -s，词尾 /ə/ 或 /ər/ 后读 /z/。dinner 经古法语 disner 等借入，较早有结束空腹、进食的背景；英语主餐时间后来常移到晚上。',
 [['古法语 disner 等 → dinner','进食、主餐；时间随时代与习惯变化'],['dinner + -s → dinners','多顿主餐、多场宴会']],
 'family dinners 家庭晚餐；formal dinners 正式晚宴；school dinners 学校午餐〔英式常见〕。',
 'dinners with friends；dinners served in the hall。','现代 dinner 常是晚餐，但 school dinners 等英式搭配可指中午的主餐。具体时间由生活习惯与语境决定，别只记一个钟点。',
 ('Family dinners give them time to talk.','家庭晚餐让他们有时间聊聊天。'),('The hall is used for meetings and formal dinners.','这个大厅用来开会和举办正式宴会。'),sources=['https://en.wiktionary.org/wiki/dinners#English','https://en.wiktionary.org/wiki/dinner#English'])
W('drinks','/drɪŋks/','饮品〔复数〕；喝、饮酒〔第三人称单数〕',
 '一杯杯供人喝的东西，是 drinks；一个人把液体喝进去，动词的第三人称也是 drinks。是否含酒精，要看上下文。',
 'drink + -s，/k/ 后读 /s/。动词 drink 继承古英语 drincan，名词也有古英语 drynċ 等旧形式；现代名动词共享写法，过去变化为 drank、drunk。',
 [['古英语 drincan、drynċ → drink','喝；供喝的液体'],['drink + -s → drinks','多份饮品；单数主语喝']],
 'hot drinks 热饮；soft drinks 软饮料；drinks water 喝水；go out for drinks 出去喝几杯〔常指酒〕。',
 'drinks on the table；drinks tea with breakfast。','drinks 作名词可含无酒精饮料。He drinks 单独出现时常暗示饮酒；He drinks water 有明确宾语，直接按喝水理解。',
 ('Hot drinks are available near the entrance.','入口附近有热饮供应。'),('She drinks tea with breakfast every morning.','她每天早餐都喝茶。'),sources=['https://en.wiktionary.org/wiki/drinks#English','https://en.wiktionary.org/wiki/drink#English'])
W('foods','/fuːdz/','各种食物、食品种类〔food 的复数用法〕',
 'food 通常把吃的东西当作总体；换成 foods，画面往往是一种种不同的食品，如面包、蔬菜、奶酪这些类别。',
 'food + -s，/d/ 后读 /z/。food 延续古英语 fōda；不可数名词在区分种类、食品品项时发展出可数用法，与 feed 有历史联系。',
 [['古英语 fōda → food','供人或动物吃的东西'],['按种类、品项使用 food → foods','多种食物、多类食品']],
 'local foods 当地食品；frozen foods 冷冻食品；different foods 不同食物。',
 'foods from different regions；foods sold in the market。','some food 可以是一些吃的；some foods 通常是某些种类的食物。foods 的 s 并不意味着每一口或每一块都单独数出来。',
 ('The market sells foods from many regions.','这个市场出售许多地区的食品。'),('Frozen foods are kept in the large freezer.','冷冻食品存放在那个大冷柜里。'),sources=['https://en.wiktionary.org/wiki/foods#English','https://en.wiktionary.org/wiki/food#English'])
W('breads','/bredz/','不同种类、款式的面包〔bread 的复数用法〕',
 'bread 通常是笼统的面包；面包店摆出酸面包、黑麦面包等不同款式，谈这些种类就能用 breads。',
 'bread + -s，/d/ 后读 /z/。bread 继承古英语 brēad，经中古英语 bred 等发展；更早究竟偏向发酵还是碎块的联系有不同解释。现代种类复数不改变这条近源。',
 [['古英语 brēad → 中古英语 bred → bread','碎块、食物相关旧义 → 面包'],['bread 按种类可数 → breads','多种面包、不同面包产品']],
 'traditional breads 传统面包种类；freshly baked breads 新烤的各式面包；rye breads 黑麦面包品种。',
 'breads on display；breads made with different grains。','普通说两片面包用 two slices of bread；两个整条可说 two loaves of bread。breads 更常用于品种、产品介绍，不能到处替代 slices 或 loaves。',
 ('The bakery makes several traditional breads.','这家面包店制作几种传统面包。'),('The guide explains how breads differ across regions.','这本指南讲解不同地区的面包有何差异。'),sources=['https://en.wiktionary.org/wiki/breads#English','https://en.wiktionary.org/wiki/bread#English'])
W('cakes','/keɪks/','蛋糕、饼；块状物〔复数〕；结成硬块〔第三人称单数〕',
 '一块块做好的糕饼，是 cakes；有些东西黏在表面、干成厚厚一块，也沿这个团块形象用 cake 作动词。',
 'cake + -s，/k/ 后读 /s/。cake 借自古诺尔斯语 kaka，经中古英语延续；更早来源不定。英语由食物名称扩展到团块、结块和厚厚附着。',
 [['古诺尔斯语 kaka → 中古英语 → cake','糕饼类食物'],['cake + -s → cakes；形状和动词扩展','多个糕饼；单数主语结块、结成厚层']],
 'birthday cakes 生日蛋糕；fish cakes 鱼饼；cakes of soap 一块块肥皂；mud cakes on boots 泥在靴子上结块。',
 'cakes in the shop window；cakes baked for the party。','cakes 常数整个蛋糕或独立小糕点；几片蛋糕通常用 slices of cake。fish cakes 按饼状食物理解，具体做法与甜蛋糕不同。',
 ('She baked two cakes for the party.','她为聚会烤了两个蛋糕。'),('The café serves small cakes with afternoon tea.','这家咖啡馆在下午茶时供应小蛋糕。'),sources=['https://en.wiktionary.org/wiki/cakes#English','https://en.wiktionary.org/wiki/cake#English'])
W('apples','/ˈæpəlz/','苹果〔apple 的复数〕',
 '枝头、果篮里一个个苹果，就是 apples。这个很老的果实名字早期范围更宽，今天单独使用通常就说苹果。',
 'apple + -s，/l/ 后读 /z/。apple 继承古英语 æppel，经中古英语 appel 发展；较早还可较广地称果实，更远来源有争议。',
 [['古英语 æppel → 中古英语 appel → apple','较宽的果实名称 → 常用苹果义'],['apple + -s → apples','多个苹果']],
 'pick apples 摘苹果；slice the apples 把苹果切片；cooking apples 适合烹调的苹果。',
 'apples in a basket；apples growing on the tree。','apple 开头是元音音素，单数用 an apple。apples 数一个个果实；apple juice 中 apple 修饰 juice，通常保留单数形式。',
 ('The children picked apples from the tree.','孩子们从树上摘苹果。'),('She sliced the apples for the pie.','她把苹果切片，用来做派。'),sources=['https://en.wiktionary.org/wiki/apples#English','https://en.wiktionary.org/wiki/apple#English'])
W('meats','/miːts/','各种肉、肉类品种〔meat 的复数用法〕',
 'meat 通常把肉当作食材总体；meats 常把牛肉、鸡肉、不同加工肉等按类别或产品分开来说。',
 'meat + -s，/t/ 后读 /s/。meat 继承古英语 mete，旧义泛指食物，后来常用义缩窄到动物肉；现代区分种类时可以用复数。',
 [['古英语 mete → meat；意义逐渐缩窄','食物 → 常用的动物肉义'],['meat 按种类、品项可数 → meats','不同肉类、肉制品']],
 'cooked meats 熟肉制品；cold meats 冷肉；different meats 不同肉类。',
 'meats displayed at the counter；meats used in the recipe。','a piece of meat 是一块肉，meats 通常数品类，二者关注点不同。某些旧组合仍保留更宽的可食部分义，不能都按现代动物肉解释。',
 ('The counter sells cheeses and cooked meats.','这个柜台出售奶酪和熟肉制品。'),('The recipe can be made with several different meats.','这道食谱可以选用几种不同的肉来做。'),sources=['https://en.wiktionary.org/wiki/meats#English','https://en.wiktionary.org/wiki/meat#English'])
W('coffees','英 /ˈkɒfiz/；美 /ˈkɔːfiz/、/ˈkɑːfiz/','几份咖啡；咖啡品种〔coffee 的复数用法〕',
 '把咖啡按点单的一杯杯来数，可以说 coffees；品鉴或产品介绍里，一种种咖啡也能用这个复数。',
 'coffee + -s，/i/ 后读 /z/。coffee 的名称经荷兰语 koffie 等欧洲形式接土耳其语 kahve、阿拉伯语 qahwa；现代再按份数、种类作可数使用。',
 [['阿拉伯语 qahwa → 土耳其语 kahve → 欧洲语言 → coffee','咖啡名称随贸易传播'],['coffee 按份、品种使用 → coffees','几杯咖啡；多种咖啡']],
 'two coffees 两杯咖啡；coffees from different regions 不同产区的咖啡；order coffees 点咖啡。',
 'coffees for the table；a selection of coffees。','some coffee 是一些咖啡饮料或咖啡材料；two coffees 在点单时通常省去了 cups of。究竟是份数还是品种，靠点单或产品语境区分。',
 ('We ordered two coffees and a slice of cake.','我们点了两杯咖啡和一片蛋糕。'),('The shop sells coffees from several regions.','这家店出售几个产区的咖啡。'),sources=['https://en.wiktionary.org/wiki/coffees#English','https://en.wiktionary.org/wiki/coffee#English'])
W('teas','/tiːz/','茶的品种；几份茶；茶点餐〔tea 的复数用法〕',
 '把茶按品种或点单的一份份来数，就能用 teas；英式某些用法里，还可以数一次次喝茶配餐的活动。',
 'tea + -s，元音 /iː/ 后读 /z/。tea 的现代名称主要经荷兰语 thee 等贸易路径接闽南语 茶 tê；英语又形成饮品、份数、种类及茶餐等用法。',
 [['闽南语 tê → 荷兰语 thee 等 → tea','茶的名称随商品传播'],['tea 按份、种类、茶餐可数 → teas','多份茶、多种茶或多次茶点餐']],
 'green teas 绿茶品种；two teas 两份茶；afternoon teas 下午茶餐；a selection of teas 各种茶。',
 'teas from different regions；teas served in small pots。','two teas 在咖啡馆可以是两份茶，不必都是一杯的大小。tea 通常仍可不可数地说茶叶、茶水；teas 则把份数或种类单独拎出来。',
 ('The menu lists teas from different regions.','菜单列着不同产区的茶。'),('We ordered two teas and some biscuits.','我们点了两份茶和一些饼干。'),sources=['https://en.wiktionary.org/wiki/teas#English','https://en.wiktionary.org/wiki/tea#English'])
W('sandwich','/ˈsænwɪtʃ/、/ˈsændwɪtʃ/','三明治；把……夹在中间',
 '两片面包中间夹着馅，是 sandwich 最容易记住的画面；把别的东西夹在两者之间，也可以直接用它作动词。',
 '食物名称联系第四代 Sandwich 伯爵 John Montagu 的头衔，传统故事说他为方便持续活动而这样进食，故事细节不当作确定史实。Sandwich 头衔又来自地名；现代食物词整体学习，动词由名词发展。',
 [['Sandwich 伯爵头衔 → 食物名 sandwich','名称与人物联系；用餐轶事细节有传说成分'],['sandwich 名词 → 动词','面包夹馅的食物 → 把东西夹在两者之间']],
 'a cheese sandwich 奶酪三明治；make a sandwich 做三明治；sandwich something between two layers 把东西夹在两层之间。',
 'a sandwich for lunch；sandwich the filling between slices。','常见发音会弱化或省去 /d/。动词核心是夹在中间，可用于食物，也可用于位置、时间安排；现代 wich 不是可独立拆出的夹心后缀。',
 ('I made a cheese sandwich for lunch.','我做了一个奶酪三明治当午餐。'),('Sandwich the filling between two slices of bread.','把馅料夹在两片面包之间。'),sources=['https://www.etymonline.com/word/sandwich','https://en.wiktionary.org/wiki/sandwich#English'])
W('sandwiches','/ˈsænwɪtʃɪz/、/ˈsændwɪtʃɪz/','三明治〔复数〕；把……夹在中间〔第三人称单数〕',
 '一份份面包夹馅的食物，是 sandwiches；单数主语把东西夹到两层之间，动词也写 sandwiches。',
 'sandwich + -es，/tʃ/ 后增加 /ɪz/。sandwich 的食物名称联系 Sandwich 伯爵头衔，英语由食物名发展出夹在中间的动词，再按普通词形变化。',
 [['Sandwich 头衔 → sandwich；名词转动词','食物名称 → 夹在中间的动作'],['sandwich + -es → sandwiches','多份三明治；单数主语把东西夹在中间']],
 'make sandwiches 做三明治；sandwiches for a picnic 野餐用的三明治；sandwiches the filling between bread 把馅夹在面包之间。',
 'sandwiches in a lunch box；sandwiches cut into triangles。','sandwiches 的 ch 增加一个 /ɪz/ 音节，与 lunches 的词尾发音规则相同。点餐数 sandwiches，强调切下来的小块时也可用 pieces。',
 ('She packed the sandwiches in a lunch box.','她把三明治装进了午餐盒。'),('We cut the sandwiches into small triangles.','我们把三明治切成小三角块。'),sources=['https://en.wiktionary.org/wiki/sandwiches#English','https://www.etymonline.com/word/sandwich'])
W('kitchens','/ˈkɪtʃɪnz/','厨房〔kitchen 的复数〕',
 '专门准备、烹调食物的空间，是 kitchens；家庭厨房、餐馆后厨、共用厨房，都是这个烹调地点的现代画面。',
 'kitchen + -s，/n/ 后读 /z/。拉丁 coquina、cocina 等烹调处名称较早借入日耳曼语，古英语有 cycene 等形式，经中古英语发展成 kitchen。',
 [['拉丁 coquina、cocina → 早期日耳曼借词、古英语 cycene','烹调食物的地点'],['中古英语 → kitchen → kitchens','厨房 → 多个厨房']],
 'restaurant kitchens 餐馆后厨；shared kitchens 共用厨房；commercial kitchens 商用厨房。',
 'kitchens in the student residence；kitchens fitted with large ovens。','kitchen 主要指烹调空间；同族但另一条借入路线的 cuisine 常指菜系、烹饪风格。两个词现代的使用范围已经不同。',
 ('The student residence has two shared kitchens.','这栋学生宿舍有两个共用厨房。'),('The restaurant kitchens are on the ground floor.','餐馆的后厨设在底层。'),sources=['https://en.wiktionary.org/wiki/kitchens#English','https://en.wiktionary.org/wiki/kitchen#English'])
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_yj',ROOTS,WORDS)
 extend_lessons()
