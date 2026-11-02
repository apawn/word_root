"""Familiar food borrowings, source-language structure and English usage."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
def S(word,base):
 a=['https://en.wiktionary.org/wiki/'+word+'#English','https://www.etymonline.com/word/'+base]
 if word=='sushi':a.append('https://www.japan.travel/en/guide/sushi-in-japan/')
 return a
EXISTING_ROOT_ADDITIONS={
 'C0923':dict(words='sushi'.split(),label='与 rice 对照：sushi 的醋饭与借词历史',note='这里按食物概念对照，sushi 不由 oryz- 派生。它借日语寿司名，旧食物史有米饭发酵等背景，现代常见形式以调味醋饭配食材；不能直接等同生鱼片。'),
 'B3810':dict(words='tofu soy soya'.split(),label='豆类食物名：tofu、soy、soya',note='tofu 经日语 tōfu 接汉语豆腐；soy、soya 经荷兰语接日语酱油名，后来也用于大豆及制品。这些是借词历史，与英语 bean 对照食材，不能都拆成 bean 派生。'),
 'C0965':dict(words='ramen spaghetti macaroni lasagna lasagne ravioli'.split(),label='面食名对照：拉面与几类意面',note='此处和 pasta、paste 的面食概念对照，不表示各名称同源。ramen 经日语接汉语面条名的分析；spaghetti 是意大利小绳名的复数；其他意面分别有自己的借入历史。'),
 'B3028':dict(words='tortilla tortillas'.split(),label='tortilla：西班牙语小饼名的借用',note='torta 饼 + 西班牙语小称 -illa → tortilla，经借入英语，复数 tortillas。墨西哥食物语境多是薄饼，西班牙食物语境可指蛋饼，不能由中文单一译名覆盖所有菜名。'),
 'A1969':dict(words='burrito burritos'.split(),label='与 donkey 对照：burrito 的西班牙语小驴名称',note='这里与 donkey 对照命名材料，不把 burrito 当 -ock 派生词。西班牙语 burro 驴 + 小称 -ito → burrito，食物为何如此命名没有定论；现代英语借来指卷饼等。'),
 'B2928':dict(words='nachos'.split(),label='与 cheese 对照：nachos 的食物与人名来源',note='这里只按常见配料对照，nachos 不由 cheese 派生。名称与 Ignacio Anaya 的昵称 Nacho 有关，现代英语常用复数指配奶酪等的玉米片食物。'),
 'B2489':dict(words='guacamole'.split(),label='avocado 对照：guacamole 牛油果酱',note='经美洲西班牙语接纳瓦特尔语的牛油果 + 酱材料；现代英语短称 guac 才由 guacamole 截短。'),
 'B3543':dict(words='hummus'.split(),label='chickpea 对照：hummus 鹰嘴豆泥',note='hummus 借阿拉伯语鹰嘴豆的名称材料，英语常特指做成的豆泥。与 chickpea 对照原料，不把阿拉伯语借词当英语 pea 派生。'),
 'B2415':dict(words='pesto'.split(),label='与 pound 动作对照：pesto 捣碎的酱',note='pesto 接意大利语 pestare 捣、碾的分词材料，远处与拉丁捣碎词族、pestle 名称相关。与英语 pound 只是动作意义对照，不表示由英语 pound 改音产生。'),
 'C0271':dict(words='croissant croissants'.split(),label='增长 → 渐盈月 → 月牙形点心：croissant',note='法语 croissant 新月、月牙的材料接拉丁 crescere 生长；由渐盈月到月牙形，再用于点心名。英语借 croissant，复数 croissants；crescent 与它有历史联系。'),
 'C0109':dict(words='baguette baguettes'.split(),label='小棍的名称材料 → baguette 法棍',note='法语 baguette 杖、小棍经意大利语 bacchetta 小棍，接拉丁 baculum 棍、杖。名称又用于长条面包及某些长方形切割宝石；英语复数按末尾 -s 变化。'),
 'B2946':dict(words='croissant croissants baguette baguettes'.split(),label='与 bread 对照：可颂与法棍的法语借名',note='按日常烘焙食物对照，两个法语词不由英语 bread 派生。croissant 接月牙与生长词线，baguette 接棍、杖词线，各自按食物形象命名。'),
}
SOY=[['日语 shōyu 酱油名 → 荷兰语 soya 等形式','贸易接触传播名称；更远有汉字酱油的材料背景'],['英语 soy、soya → 大豆、相关制品的现代用法','早期酱名与后来原料、制品用法要区分']]
LASAGNA=[['意大利语 lasagna、复数 lasagne → 英语借名','现代可说大片意面或层叠烘烤的菜肴'],['更远常追到拉丁 lasanum、希腊 lasanon 器皿名','从烹调容器等名称材料向食物名发展的常见分析']]
TORTILLA=[['西班牙语 torta 饼 + 小称 -illa → tortilla','直观是小饼，远接晚期拉丁饼名材料'],['英语 tortilla → tortillas','借词保留多种菜肴语境，现代英语复数加 -s']]
BURRITO=[['西班牙语 burro 驴 + 小称 -ito → burrito','字面小驴；食物为何这样得名没有定论'],['食物名称借入英语 burrito → burritos','现代常指薄饼包裹馅料的卷饼']]
CROISSANT=[['拉丁 crescere 生长、crescens 渐长 → 法语 croissant','由渐盈月的材料发展月牙、新月名称'],['月牙形点心名 croissant → 英语 croissant、croissants','英语借来作食物名称，复数加 -s']]
BAGUETTE=[['拉丁 baculum 棍、杖 → 意大利语 bacchio、bacchetta 小棍','意大利语小称材料参与构词'],['法语 baguette 棍、杖 → 长条面包等名称 → 英语借入','形状命名，现代复数 baguettes']]
W('sushi','英、美 /ˈsuːʃi/','寿司',
 '先想调味醋饭，配上海鲜、鸡蛋、蔬菜等食材。常见寿司的关键不只是鱼，更不是见到生鱼片就一律叫 sushi。',
 '整词借日语 sushi。名称与日本寿司的食物历史相接，旧形式有用米饭发酵、后来改用醋饭等变化；英语不按 su、shi 拆成自己的前后缀。',
 [['日语寿司名与旧发酵食物背景','食物形态经历变化，不能把古今做法一概等同'],['日语 sushi → 英语 sushi','现代英语通常作为食物名整体使用']],
 'some sushi 是一些寿司；a piece of sushi 是一块寿司；sushi rice 是调味寿司饭。常用不可数食物名来谈一份寿司。',
 'some sushi；a piece of sushi；sushi rice。',
 'sashimi 常指生鱼片等刺身，不一定配寿司饭；sushi 也可以配熟食、蔬菜。认食物结构比死记“生鱼”更准。',
 ('We ordered some sushi for lunch.','我们午餐点了些寿司。'),('This piece of sushi has cucumber inside.','这块寿司里面有黄瓜。'),sources=S('sushi','sushi'))
W('tofu','英 /ˈtəʊfuː/；美 /ˈtoʊfuː/','豆腐',
 '豆浆凝成柔软或较结实的块状食物，就是 tofu。英语把熟悉的豆腐名借过去，通常当食材整体来谈。',
 '借日语 tōfu，日语又接汉语豆腐。可追到原语言的豆、腐两个字的名称材料，但不把腐的字面义当作每块现代豆腐的制作说明。',
 [['汉语豆腐 → 日语 tōfu','食物名称借入，声音随语言改变'],['日语 tōfu → 英语 tofu','英语常用不可数食材名，分块用 a piece、a block']],
 'a block of tofu 是一块豆腐；firm tofu 是较结实的豆腐；soft tofu 是嫩豆腐。要按实际产品、做法理解。',
 'a block of tofu；firm tofu；tofu with vegetables。',
 '普通新鲜豆腐不等同发酵豆腐；不能因为腐字的旧字面解释，就说所有 tofu 都是腐败或发酵制品。',
 ('She added tofu and vegetables to the soup.','她往汤里加了豆腐和蔬菜。'),('We cut the tofu into small cubes.','我们把豆腐切成小方块。'),sources=S('tofu','tofu'))
W('ramen','英、美 /ˈrɑːmən/','日式拉面；拉面面条',
 '一碗面条配汤和浇头，菜单上常写 ramen。现代英语里通常想到日式拉面，未必是现场手拉的面。',
 '借日语 rāmen。常见分析追到汉语拉面一类面条名称，但确切借词细节有不同讨论；现代日语、英语的食物范围不能直接由拉字决定。',
 [['汉语面条名称材料 → 日语 rāmen 的常见来源分析','具体声音、传播细节保留不确定性'],['日语 rāmen → 英语 ramen','既说相应面条，也说做成的一碗面食']],
 'a bowl of ramen 是一碗拉面；instant ramen 是方便拉面；ramen noodles 具体说面条。',
 'a bowl of ramen；instant ramen；ramen noodles。',
 '词源可能与拉面相关，不表示现代所有 ramen 都用手拉制作；名字的历史与眼前的工艺要分开。',
 ('We shared a bowl of ramen after the walk.','散步后我们分着吃了一碗拉面。'),('I added an egg to my instant ramen.','我往方便拉面里加了一个鸡蛋。'),sources=S('ramen','ramen'))
W('soy','英、美 /sɔɪ/','大豆；大豆制品；酱油〔部分语境〕',
 'soy milk 是豆奶，soy sauce 是酱油。先抓“大豆及相关食物”的现代范围，不把每个 soy 都翻成同一件成品。',
 '经荷兰语 soya 接日语 shōyu 等酱油名的形式，早期英语多说酱；现代也广用于大豆及大豆制品。',SOY,
 'soy milk 是豆奶；soy sauce 是酱油；soy protein 是大豆蛋白。单独 soy 的具体意思由场景决定。',
 'soy milk；soy sauce；soy products。',
 '同一个借词从酱名扩展到相关原料、制品范围；soy sauce 不是把大豆和任意酱汁相加，而是固定名称酱油。',
 ('She added a little soy sauce to the rice.','她往米饭里加了一点酱油。'),('This drink is made from soy.','这种饮料是用大豆制成的。'),sources=S('soy','soy'))
W('soya','英 /ˈsɔɪə/；美 /ˈsɔɪə/','大豆；大豆制品〔英式等用法常见〕',
 '英国等地写 soya milk，常就是豆奶；美式常见 soy milk。多一个 a，不表示换成另一种豆子。',
 'soya 与 soy 都接荷兰语 soya、日语 shōyu 等酱油名的传播线。英语里的两种形式分布有差别，现代都能用于大豆及制品。',SOY,
 'soya milk 是豆奶；soya beans 是大豆；soya products 是大豆制品。按后接名词确定具体对象。',
 'soya milk；soya beans；soya products。',
 'soy、soya 在很多大豆搭配里可对应，但各地区固定搭配习惯不同；别为末尾 a 编一个单复数规则。',
 ('The shop sells soya milk.','这家店卖豆奶。'),('Soya beans are used to make several different foods.','大豆可用来制作多种不同食物。'),sources=S('soya','soya'))
W('spaghetti','英 /spəˈɡeti/；美 /spəˈɡɛti/','细长条意面；这类意面做成的菜',
 '像一根根小细绳的长意面，就是 spaghetti。原来的命名很直观：按长、细的形状叫它。',
 '意大利语 spago 绳 + 小称材料 → spaghetto 小绳；复数 spaghetti 借入英语。现代英语常把 spaghetti 当不可数食材名。',
 [['意大利语 spago 绳 → 小称 spaghetto','形状像小绳子，名称用于细长面条'],['意大利语复数 spaghetti → 英语 spaghetti','源语言复数进入英语后，常作不可数食物名']],
 'some spaghetti 是一些细长意面；a plate of spaghetti 是一盘意面；a strand of spaghetti 是一根面。',
 'a plate of spaghetti；spaghetti with tomato sauce；a strand of spaghetti。',
 '不需要按英语规则再给一盘面加 -s。意大利语的单复数历史帮助理解词形，英语实际用法则看英语句法。',
 ('We had spaghetti with tomato sauce.','我们吃了番茄酱细长意面。'),('A strand of spaghetti fell onto the table.','一根意面掉到了桌上。'),sources=S('spaghetti','spaghetti'))
W('macaroni','英 /ˌmækəˈrəʊni/；美 /ˌmækəˈroʊni/','通心粉；这类意面做成的食物',
 '常见小弯管、短管样的意面，可以叫 macaroni。现代日常先认这类食物，不必把每种意面都叫 macaroni。',
 '借意大利语方言 maccaroni 等复数形式，标准意大利语相关形式 maccheroni。更远有揉压、谷物食物等不同来源分析，不能选一个当定论。',
 [['意大利语地区食物名 maccarone 等 → 复数 maccaroni','较远来源有争议'],['意大利语复数形式 → 英语 macaroni','现代常作不可数意面、菜肴名称']],
 'macaroni and cheese 是奶酪通心粉；some macaroni 是一些通心粉；a bowl of macaroni 是一碗。',
 'macaroni and cheese；a bowl of macaroni；cooked macaroni。',
 '英语旧时 macaroni 的面食范围可能更宽；读现代菜单先按常见通心粉理解，别照旧用法把所有意面都归在一起。',
 ('The children asked for macaroni and cheese.','孩子们想吃奶酪通心粉。'),('We mixed the macaroni with the sauce.','我们把通心粉和酱拌在一起。'),sources=S('macaroni','macaroni'))
W('lasagna','英 /ləˈzænjə/；美 /ləˈzɑːnjə/','千层面；用来做千层面的大片意面',
 '大片面皮、酱和其他馅料一层叠一层烘烤，整道菜常叫 lasagna。它既能指面皮，也能指做好的千层面。',
 '借意大利语 lasagna，意大利语复数是 lasagne；更远常追到拉丁 lasanum、希腊 lasanon 等烹调器皿名。现代英语 lasagna 常作为整道菜的名称。',LASAGNA,
 'a slice of lasagna 是一块千层面；vegetable lasagna 是蔬菜千层面。食谱所用配料多样，不由名称保证一定有肉。',
 'a slice of lasagna；vegetable lasagna；make lasagna。',
 'lasagna 与英语里的 lasagne 常指同类食物，拼法习惯不同。别把意大利语单复数直接当成英语只能一份、多份的限制。',
 ('She made vegetable lasagna for dinner.','她晚餐做了蔬菜千层面。'),('I saved a slice of lasagna for tomorrow.','我留了一块千层面明天吃。'),sources=S('lasagna','lasagna'))
W('lasagne','英 /ləˈzænjə/；美 /ləˈzɑːnjə/','千层面；大片意面〔lasagna 的另一常见拼写〕',
 '菜单上 lasagne 和 lasagna 常说同类千层面。这不是英语里通过换 e 就指定一盘还是好几盘。',
 'lasagne 是意大利语 lasagna 的复数形式，借入英语后又常作整道食物的名称；英语中两种拼法均见，英式常见 lasagne。',LASAGNA+[['意大利语复数 lasagne → 英语常见食物名','进入英语后，按英语食物名使用']],
 'a portion of lasagne 是一份千层面；homemade lasagne 是自制千层面；lasagne sheets 指制作所用的大片面皮。',
 'a portion of lasagne；homemade lasagne；lasagne sheets。',
 '本词的 e 是源语言词形的一部分，不是英语复数 -s；谈几份时可直接用 portions、slices 来数。',
 ('The café serves homemade lasagne.','这家咖啡馆供应自制千层面。'),('I ordered a small portion of lasagne.','我点了一小份千层面。'),sources=S('lasagne','lasagna'))
W('ravioli','英 /ˌræviˈəʊli/；美 /ˌræviˈoʊli/','意式馅面；意大利饺',
 '两片或一片面皮把奶酪、蔬菜、肉等馅料包起来，形成一个个小面包裹，就是常见的 ravioli。',
 '借意大利语 ravioli，是 raviolo 的复数。更远来源有不同分析，虽有人联系包覆材料等，但不宜当成已定的英语构词拆分。',
 [['意大利语 raviolo → 复数 ravioli','各个包馅小面食的名称'],['意大利语 ravioli → 英语借词','现代菜单中也常整体说这一类食物']],
 'cheese ravioli 是奶酪馅面；a plate of ravioli 是一盘；a piece of ravioli 可明确说一个。',
 'cheese ravioli；a plate of ravioli；ravioli with tomato sauce。',
 'ravioli、dumplings 都能帮助你想到包馅面食，但具体食物、做法不同。英语常按整体食物名使用，不必再加英语 -s。',
 ('We ordered ravioli filled with cheese and spinach.','我们点了奶酪菠菜馅的意式馅面。'),('The ravioli came with tomato sauce.','意式馅面配的是番茄酱。'),sources=S('ravioli','ravioli'))
W('tortilla','英 /tɔːˈtiːə/；美 /tɔːrˈtiːə/','墨西哥薄饼；西班牙式蛋饼〔按菜肴语境〕',
 '墨西哥食物里，常是一张用来包馅或配菜的薄饼；西班牙食物里，又可能是一块厚蛋饼。先看是哪种菜系。',
 '西班牙语 torta 饼 + 小称 -illa → tortilla，字面小饼；远接晚期拉丁 torta 饼名。英语借来后，保留不止一种食物语境。',TORTILLA,
 'a flour tortilla 是面粉薄饼；a corn tortilla 是玉米薄饼；Spanish tortilla 常指西班牙式蛋饼，常见土豆等配料。',
 'a flour tortilla；a corn tortilla；Spanish tortilla。',
 '小称 -illa 属西班牙语原词构造；现代英语把 tortilla 当整词，不能把里面的 t、ill 分别套英语意思。',
 ('She wrapped the filling in a warm tortilla.','她把馅料包进一张温热的薄饼里。'),('We shared a slice of Spanish tortilla.','我们分着吃了一块西班牙式蛋饼。'),sources=S('tortilla','tortilla'))
W('tortillas','英 /tɔːˈtiːəz/；美 /tɔːrˈtiːəz/','墨西哥薄饼；西班牙式蛋饼〔复数，按语境〕',
 '桌上放几张用来包东西的薄饼，常说 tortillas。若在西班牙菜语境里，则可能是在说几份、几个蛋饼。',
 'tortilla + -s → tortillas，元音后读 /z/。torta + 西班牙语小称 -illa 是基础词的历史构造，末尾复数 -s 才是在整个名词外加的数量变化。',TORTILLA+[['tortilla + -s → tortillas','多张薄饼或相应蛋饼，词尾 /z/']],
 'warm tortillas 是温热的薄饼；corn tortillas 是玉米薄饼；a stack of tortillas 是一摞薄饼。',
 'warm tortillas；corn tortillas；a stack of tortillas。',
 'tortilla 与 tortillas 的区别是单复数；墨西哥薄饼、西班牙蛋饼的区别来自菜肴语境，不由是否加 s 决定。',
 ('He placed a stack of tortillas on the table.','他把一摞薄饼放在桌上。'),('We used corn tortillas for the tacos.','我们用玉米薄饼做了塔可。'),sources=S('tortillas','tortilla'))
W('burrito','英 /bəˈriːtəʊ/；美 /bəˈriːtoʊ/','墨西哥卷饼',
 '拿一张薄饼把豆、肉、蔬菜等馅料裹起来，常见这种卷饼就叫 burrito。今天先认完整食物。',
 '借西班牙语 burrito：burro 驴 + 小称 -ito，字面小驴。食物为什么用了这个名称没有定论，不能把某个商贩故事或外形猜想说成已证实来源。',BURRITO,
 'a bean burrito 是豆馅卷饼；a chicken burrito 是鸡肉卷饼；a breakfast burrito 常指早餐风格的卷饼。',
 'a bean burrito；a chicken burrito；a breakfast burrito。',
 'tortilla 是外面那张薄饼，burrito 是包好馅的食物；二者不是两个可任意互换的名字。',
 ('I ordered a bean burrito for lunch.','我午餐点了一个豆馅卷饼。'),('She cut the burrito in half.','她把卷饼切成两半。'),sources=S('burrito','burrito'))
W('burritos','英 /bəˈriːtəʊz/；美 /bəˈriːtoʊz/','墨西哥卷饼〔复数〕',
 '几个人各拿一个卷饼，合起来就是 burritos。外来食物名进入英语后，也可以很自然地按英语复数规则变化。',
 'burrito + -s → burritos；元音后读 /z/，末尾 o 保留，直接加 s，不写成 -oes。基础词里 -ito 则是西班牙语小称材料。',BURRITO+[['burrito + -s → burritos','多个卷饼，末尾 /z/']],
 'two burritos 是两个卷饼；vegetable burritos 是蔬菜卷饼；make burritos 是做卷饼。',
 'two burritos；vegetable burritos；make burritos。',
 '西班牙语小称 -ito 与英语复数 -s 分属两层：先有食物名 burrito，再谈一个还是多个。',
 ('We made burritos for everyone.','我们给每个人都做了卷饼。'),('The café sells both chicken and vegetable burritos.','这家咖啡馆卖鸡肉卷饼和蔬菜卷饼。'),sources=S('burritos','burrito'))
W('nachos','英 /ˈnætʃəʊz/；美 /ˈnɑːtʃoʊz/','配奶酪等浇头的玉米片；这类食物',
 '一盘脆玉米片，上面配奶酪、辣椒或其他浇头，常叫 nachos。菜单上通常用复数名说整份。',
 '食物名与 Ignacio Anaya 的昵称 Nacho 有关；名称进入英语后有单数 nacho、复数 nachos。这里不是把 na、cho 拼成普通英语词根。',
 [['人名 Ignacio 的昵称 Nacho → 食物名称','与 Ignacio Anaya 的命名背景相关'],['英语 nacho + -s → nachos','/əʊ/、/oʊ/ 后读 /z/，常用复数说整份食物']],
 'a plate of nachos 是一盘；share some nachos 是分着吃些玉米片食物；nachos with cheese 是配奶酪的版本。',
 'a plate of nachos；nachos with cheese；share some nachos。',
 'tortilla chips 是脆玉米薄饼片的名称；nachos 常说配好浇头的食物，日常范围会有交叉，要看菜单具体描述。',
 ('We shared a plate of nachos.','我们分着吃了一盘配浇头的玉米片。'),('The nachos came with melted cheese.','这份玉米片配了融化的奶酪。'),sources=S('nachos','nachos'))
W('guacamole','英 /ˌɡwækəˈməʊli/；美 /ˌɡwɑːkəˈmoʊli/','牛油果酱',
 '把牛油果压成泥，配其他调味材料，做成能蘸、能抹的酱，常叫 guacamole。名字本身就有牛油果与酱的材料。',
 '经美洲西班牙语 guacamole 接纳瓦特尔语 āhuacamōlli：牛油果的 āhuacatl 材料 + mōlli 酱。借词变形后，不能逐字按英语字母切义。',
 [['纳瓦特尔语牛油果材料 + 酱材料 → āhuacamōlli','原语言组合直观表示牛油果酱'],['美洲西班牙语 guacamole → 英语 guacamole','食物名整体借入，英语还可截短为 guac']],
 'some guacamole 是一些牛油果酱；a bowl of guacamole 是一碗；guacamole with chips 是酱配脆片。具体配方可以不同。',
 'a bowl of guacamole；chips with guacamole；spread guacamole on toast。',
 'avocado 是原料牛油果，guacamole 是做成的酱；英语短称 guac 从这个长词截来，词源分析要先看原语言材料。',
 ('We served guacamole with tortilla chips.','我们用牛油果酱配脆玉米片。'),('She spread guacamole on her toast.','她把牛油果酱抹在吐司上。'),sources=S('guacamole','guacamole'))
W('hummus','英 /ˈhʊməs/；美 /ˈhʌməs/，也读 /ˈhuːməs/','鹰嘴豆泥',
 '把鹰嘴豆打成泥，常配芝麻酱等调味材料，做成可以蘸、可以抹的食物，就是常见 hummus。',
 '借阿拉伯语 ḥummuṣ 等鹰嘴豆的名称。英语通常以这个名字指做成的豆泥，现代把原材料名借来称这道食物。',
 [['阿拉伯语鹰嘴豆名称 ḥummuṣ 等','原语言材料先是豆名'],['借入英语 hummus → 常指鹰嘴豆泥','原料名称用于相应菜肴，配方可有变化']],
 'some hummus 是一些鹰嘴豆泥；hummus with bread 是豆泥配面包；a bowl of hummus 是一碗。',
 'a bowl of hummus；bread with hummus；spread hummus on toast。',
 'chickpeas 是原料豆子，hummus 通常是处理、调味后的豆泥。两词相关，现代英语里却不能在所有句子中互换。',
 ('We ate hummus with warm bread.','我们用温热的面包配鹰嘴豆泥吃。'),('She put a bowl of hummus in the middle of the table.','她把一碗鹰嘴豆泥放在桌子中间。'),sources=S('hummus','hummus'))
W('pesto','英 /ˈpestəʊ/；美 /ˈpɛstoʊ/','意式青酱；一类捣碎、混合食材制成的酱',
 '先想把香草、蒜等材料捣碎，再与油等拌成酱。pesto 的名字就保留了“捣、碾”的动作背景。',
 '借意大利语 pesto，接 pestare 捣、碾的分词材料，常联系 pestato 的缩合；远接拉丁捣碎词族，与 pestle 杵有历史关系。',
 [['拉丁捣碎材料 → 意大利语 pestare 捣、碾','动作是压碎、捣碎材料'],['分词材料 pesto → 酱名 → 英语 pesto','由制作动作命名食物']],
 'pasta with pesto 是青酱意面；basil pesto 是罗勒青酱。日常常指罗勒等制成的绿酱，也有不同材料的变体。',
 'pasta with pesto；basil pesto；a spoonful of pesto。',
 '名字的捣碎动作帮助理解来源，不表示今天每份 pesto 都一定用手杵制作；也不保证所有配方都相同。',
 ('We mixed the pasta with pesto.','我们把意面和青酱拌在一起。'),('She added a spoonful of pesto to the soup.','她往汤里加了一勺青酱。'),sources=S('pesto','pesto'))
W('croissant','英 /ˈkwæsɒ̃/、/ˈkrwæsɒ̃/；美 /krəˈsɑːnt/〔常见读法〕','可颂，牛角面包',
 '一层层酥皮、常做成月牙或牛角形的点心，叫 croissant。词名原本指月牙，食物借了这个形状。',
 '借法语 croissant 新月、月牙；法语词有 croître 生长的分词背景，远接拉丁 crescere 生长。先是渐盈月，再由月牙形命名点心。',CROISSANT,
 'a butter croissant 是黄油可颂；a warm croissant 是温热的可颂。现代有直形等不同产品，不因外形变化就失去这个名称。',
 'a butter croissant；a warm croissant；coffee and a croissant。',
 'croissant 与 crescent 新月有历史联系，但英语 croissant 直接借法语食物名，并不是把英语 crescent 随意改拼。',
 ('I had coffee and a croissant for breakfast.','我早餐喝了咖啡，吃了一个可颂。'),('She bought a warm croissant from the bakery.','她在面包店买了一个温热的可颂。'),sources=S('croissant','croissant'))
W('croissants','英 /ˈkwæsɒ̃z/、/ˈkrwæsɒ̃z/；美 /krəˈsɑːnts/〔英语常见复数读法〕','可颂，牛角面包〔复数〕',
 '一篮子可颂，或买两个可颂，用 croissants。这个借词在英语里会按普通名词表示多个。',
 'croissant + -s → croissants。英语按不发末尾 t 的常见英式读法可加 /z/；按发 /t/ 的常见美式读法，末尾为 /ts/。',CROISSANT+[['croissant + -s → croissants','英语复数读音随基础词常见读法变化']],
 'two croissants 是两个可颂；fresh croissants 是新鲜出炉的可颂；a basket of croissants 是一篮子。',
 'two croissants；fresh croissants；a basket of croissants。',
 '来源是法语，不表示英语复数必须照法语不变地读。先用自己学的基础读法，再接相应英语复数音。',
 ('We bought two croissants for breakfast.','我们买了两个可颂当早餐。'),('The bakery had a basket of fresh croissants by the counter.','面包店柜台边有一篮新鲜可颂。'),sources=S('croissants','croissant'))
W('baguette','英 /bæˈɡet/；美 /bæˈɡɛt/','法式长棍面包；长方形切割宝石〔形状义〕',
 '细长的一根法棍，像根小棍子。baguette 的法语原义正有小棍、杖；相同的长条形象也用于某些宝石切割。',
 '借法语 baguette 小棍、杖，接意大利语 bacchetta 小棍，含 bacchio 棍与小称 -etta 的材料，远接拉丁 baculum 棍、杖。',BAGUETTE,
 'a fresh baguette 是新鲜法棍；a baguette sandwich 是用法棍做的三明治；a baguette diamond 是长方形切割钻石。',
 'a fresh baguette；a baguette sandwich；a baguette diamond。',
 '面包和宝石义共享长条、小棍的形状命名，不是说面包后来变成了钻石；先看所修饰的对象。',
 ('He carried a baguette home from the bakery.','他从面包店拿了一根法棍回家。'),('The ring has a small baguette diamond on each side.','戒指两侧各有一颗小长方形切割钻石。'),sources=S('baguette','baguette'))
W('baguettes','英 /bæˈɡets/；美 /bæˈɡɛts/','法式长棍面包〔复数〕；长方形切割宝石〔复数〕',
 '几根长法棍是 baguettes；珠宝介绍里的几个长方形切割宝石，也可能用这个复数。形状相近，具体对象由场景决定。',
 'baguette + -s → baguettes；基础词末尾发 /t/，复数 -s 读 /s/，合成 /ts/。法语拼写保留，英语按所读的尾音接复数。',BAGUETTE+[['baguette + -s → baguettes','多个面包或相应长方形切割宝石，词尾 /ts/']],
 'two baguettes 是两根法棍；fresh baguettes 是新鲜法棍；diamond baguettes 在珠宝语境里说长方形切割钻石。',
 'two baguettes；fresh baguettes；diamond baguettes。',
 '拼写末尾有 e，但常见英语读音的最后一个音是 /t/；复数按声音接 /s/，不另读一个 /ɪz/ 音节。',
 ('She bought two baguettes for the picnic.','她为野餐买了两根法棍。'),('The baker placed the fresh baguettes on a wooden shelf.','面包师把新鲜法棍放到木架上。'),sources=S('baguettes','baguette'))
def extend_lessons():
 extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_zjh',ROOTS,WORDS)
 extend_lessons()
