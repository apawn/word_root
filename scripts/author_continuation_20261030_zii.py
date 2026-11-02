"""Kitchen vocabulary: distinguish borrowed plant names from actual derivation."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
def S(word,base):
 urls=['https://en.wiktionary.org/wiki/'+word+'#English']
 if base!='courgette':urls.append('https://www.etymonline.com/word/'+base)
 return urls
EXISTING_ROOT_ADDITIONS={
 'B2557':dict(words='cucumber cucumbers celery leek leeks broccoli spinach zucchini courgette'.split(),label='常见食用植物：逐条看借入来源',note='与 plant 比较食用植物，不是拉丁 planta 派生。cucumber 接拉丁 cucumis；celery 接希腊 selinon；leek 是古英语葱蒜植物旧名；broccoli 接意大利嫩芽的小称复数；spinach 较远来源有争论；zucchini、courgette 分别借意大利语、法语的小瓜称呼。'),
 'C1526':dict(words='turnip turnips'.split(),label='turnip：可能像车削成圆形的芜菁',note='turnip 通常分析为 turn 的转、车削形状联想 + 古英语 næp 等芜菁名，上接拉丁 napus。前半形状动机是可能的解释，不把它讲成确知的造词故事。'),
 'B3512':dict(words='beet beetroot'.split(),label='beet → beetroot：甜菜到甜菜根',note='beet 经古英语 bete 借拉丁 beta；beet + root 是甜菜的根。不是英语 beat 打击改一个字母形成。'),
 'A2167':dict(words='mushroom mushrooms'.split(),label='mushroom：另源的蘑菇名与快速增长比喻',note='与 fungus 比较真菌，并非拉丁 fungus 派生。mushroom 经古法语 meisseron 等借来，更远是否接 moss 对应词有争论；英语整体也转作动词，表示像蘑菇冒出来一样快速增加。'),
 'C1379':dict(words='turmeric cumin mustard'.split(),label='厨房里的香料和调味料：来源各自看',note='与 spice 作用途比较，不都由拉丁 species 派生。turmeric 的 terra merita、阿拉伯语等远源分析并不确定；cumin 经古英语接拉丁、希腊香料名；mustard 经古法语 mostarde 接新葡萄汁、酒液相关的 mustum，是旧制酱材料的命名背景。'),
 'B3511':dict(words='lentil lentils sesame'.split(),label='lentil、sesame：另源的食用籽实名称',note='与 seed 比较食用籽实，不从英语 seed 派生。lentil 经法语接拉丁 lenticula，lens 扁豆的小称；光学 lens 因扁豆形状得名。sesame 经拉丁、希腊接更早的近东油籽名称。'),
}
CUCUMBER=[['拉丁 cucumis、cucumer- → 古法语 cocombre','更早可能来自地中海地区的其他语言，尚不确定'],['中古英语 cucomer 等 → 现代 cucumber','拼写又向拉丁形式靠拢；现代指黄瓜与黄瓜植株']]
TURNIP=[['古英语 næp 芜菁，接拉丁 napus','中古英语 nepe 延续植物名'],['turn + nepe → turnip','通常解释为像车削成圆形的根；这个命名动机仍带推测']]
LEEK=[['原始日耳曼语 *lauka- 等 → 古英语 leac、læc','早期范围可含葱、蒜等相关植物'],['古英语形式 → 英语 leek','现代常指韭葱；garlic 的后半也保留这条旧植物名']]
LENTIL=[['拉丁 lens、lent- 扁豆 + 小称材料 → lenticula','小而扁圆的食用豆粒'],['古法语 lentille → 英语 lentil','光学 lens 又借扁豆的双凸形状命名，不是豆名来自镜片']]
MUSHROOM=[['古法语 meisseron 等 → 中古英语 musherun 等','更远来源不确定，与法语 moss 对应词的联系存在争论'],['英语 mushroom：蘑菇；整体转作动词','像蘑菇迅速冒出来一样 → 数量、规模快速增长']]
W('cucumber','英 /ˈkjuːkʌmbə/；美 /ˈkjuˌkʌmbɚ/','黄瓜；黄瓜植株',
 '切开一根清脆多水的黄瓜，就是 cucumber。词名整体借来；现代英语里不用强行把前后几段拼成一套黄瓜故事。',
 '古法语 cocombre 接拉丁 cucumis、cucumer-；中古英语曾有 cucomer 等形式，现代拼写部分向拉丁形式靠拢。',CUCUMBER,
 'a cucumber 数完整黄瓜；sliced cucumber 说切好的食材。as cool as a cucumber 借清凉形象说人很镇定。',
 'sliced cucumber；a cucumber salad；as cool as a cucumber。',
 'cucumber 是黄瓜；zucchini、courgette 常指西葫芦。形状都可能细长，食谱里的食材仍不同。',
 ('She sliced a cucumber for the salad.','她切了一根黄瓜做沙拉。'),('He stayed as cool as a cucumber during the interview.','面试时他一直十分镇定。'),sources=S('cucumber','cucumber'))
W('cucumbers','英 /ˈkjuːkʌmbəz/；美 /ˈkjuˌkʌmbɚz/','黄瓜〔复数〕',
 '菜篮里几根黄瓜，是 cucumbers。数整根果实时用复数；切成片混入菜里，则常按食材说 cucumber。',
 'cucumber + -s → cucumbers，复数后缀读 /z/；加在整个借入植物名末尾。',CUCUMBER+[['cucumber + -s → cucumbers','多个黄瓜，末尾加 /z/']],
 'two cucumbers 是两根黄瓜；fresh cucumbers 是新鲜黄瓜。英美对末尾 r 的处理不同，不改变复数后缀的浊音。',
 'fresh cucumbers；two cucumbers；grow cucumbers。',
 'a slice of cucumber 数一片；two cucumbers 数两根。单位与名词可数用法一起看。',
 ('We picked three cucumbers from the garden.','我们从菜园摘了三根黄瓜。'),('The stall sells cucumbers and tomatoes.','摊位卖黄瓜和番茄。'),sources=S('cucumbers','cucumber'))
W('turnip','英 /ˈtɜːnɪp/；美 /ˈtɝnɪp/','芜菁',
 '圆鼓鼓、可当根菜煮或烤的芜菁，是 turnip。名称的一个常见解释，恰好抓住了这个圆形：像在车床上旋出来的。',
 '通常分析为 turn 转、车削 + 中古英语 nepe 芜菁；nepe 接古英语 næp、拉丁 napus。形状为什么与 turn 相连，是推测性命名解释。',TURNIP,
 'a turnip 是一颗芜菁；roasted turnip 是烤芜菁。名称不意味着它真被人工车削过，只是可能的形状联想。',
 'a turnip；roasted turnip；turnip soup。',
 'turnip 是芜菁；radish 是萝卜相关名称。中文菜名有地方差异，英语食谱里应按具体植物辨认。',
 ('She peeled a turnip and cut it into cubes.','她给一颗芜菁削皮，再切成小块。'),('The soup contains carrot and turnip.','汤里有胡萝卜和芜菁。'),sources=S('turnip','turnip'))
W('turnips','英 /ˈtɜːnɪps/；美 /ˈtɝnɪps/','芜菁〔复数〕',
 '几颗圆圆的芜菁，是 turnips。词尾 p 是清音，复数 s 跟着读清音 /s/。',
 'turnip + -s → turnips；旧植物名形成英语名词后，再按英语规律数多个。',TURNIP+[['turnip + -s → turnips','多个芜菁，末尾 /ps/']],
 'roast turnips 是烤芜菁；grow turnips 是种芜菁。与复数数量搭配时，菜名的具体植物含义不变。',
 'roast turnips；grow turnips；a basket of turnips。',
 'turnips 的词尾没有额外 /ɪz/ 音节；/p/ 后直接接 /s/。',
 ('The basket was full of turnips.','篮子里装满了芜菁。'),('We roasted the turnips with a little oil.','我们用少量油烤了这些芜菁。'),sources=S('turnips','turnip'))
W('celery','英 /ˈseləri/；美 /ˈsɛləri/','芹菜；西芹',
 '拿起一根有长槽、咬起来清脆的芹菜茎，就是厨房里常见的 celery。按食材说时通常不可数；一根叫 a stalk of celery。',
 '法语 céleri 接意大利方言 seleri、selero，经晚期拉丁 selinon 接希腊 selinon 芹类植物名。希腊词的更远来源不确定。',
 [['希腊 selinon 芹类植物 → 晚期拉丁 selinon','parsley 的旧组合里也有这部分材料'],['意大利方言 → 法语 céleri → 英语 celery','现代食谱中的芹菜名']],
 'chopped celery 是切碎的芹菜；celery sticks 是切成条的芹菜。和 parsley 能在较远的词源里认亲，但现代不是同一种食材名。',
 'a stalk of celery；chopped celery；celery sticks。',
 'celery 常吃茎；parsley 常作为欧芹叶香草使用。词源有联系，不等于名称可以随意替换。',
 ('Add chopped celery to the soup.','往汤里加些切碎的芹菜。'),('She packed celery sticks for lunch.','她带了些芹菜条当午餐的一部分。'),sources=S('celery','celery'))
W('leek','英、美 /liːk/','韭葱；大葱形蔬菜',
 '白色长茎接着宽绿叶，切开能看见一层层，英语常见的 leek 指韭葱。先记这种食材的样子，不把所有细长葱蒜都叫同一个词。',
 '接古英语 leac、læc，属于日耳曼语 *lauka- 一族；旧名称范围曾包含葱、蒜等相关植物，现代英语 leek 更具体。',LEEK,
 'a leek 是一根韭葱；leek soup 是韭葱汤。garlic 的后半来自同一条葱蒜植物旧名，但整个词已指大蒜。',
 'a leek；leek soup；potato and leek soup。',
 'leek 与 leak 漏、泄漏同音 /liːk/，拼写和来源不同；食谱里应写 leek。',
 ('She sliced a leek into thin rings.','她把一根韭葱切成薄圈。'),('This leek soup is rich and creamy.','这碗韭葱汤浓郁顺滑。'),sources=S('leek','leek'))
W('leeks','英、美 /liːks/','韭葱〔复数〕',
 '菜摊上一把韭葱，是 leeks。长茎是一根根可数的，切成汤料后也能按食材说 leek。',
 'leek + -s → leeks，/k/ 后的复数 s 读 /s/。',LEEK+[['leek + -s → leeks','多根韭葱；词尾 /ks/']],
 'wash the leeks 是把这些韭葱洗净；sliced leeks 是切好的韭葱。几个可数食材合在一起时，用复数很自然。',
 'wash the leeks；sliced leeks；two leeks。',
 'leeks 是食材复数，leaks 是泄漏事件或 leak 的动词形式；两者也同音，要靠语境与拼写分开。',
 ('Wash the leeks before slicing them.','把韭葱洗净后再切。'),('The recipe calls for two leeks.','这份食谱需要两根韭葱。'),sources=S('leeks','leek'))
W('broccoli','英 /ˈbrɒkəli/；美 /ˈbrɑkəli/','西兰花；绿花椰菜',
 '一大团绿色小花蕾，分开像一棵棵小树，是 broccoli。名字更早抓住的是“冒出来的小芽”。',
 '借意大利 broccoli，它是 broccolo 的复数；broccolo 又是 brocco 芽、突出的尖端等的小称形式，较远接拉丁 broccus 突出的。',
 [['拉丁 broccus 突出的 → 意大利 brocco 芽等 → broccolo 小芽','意大利语内部用小称材料形成植物名称'],['意大利复数 broccoli → 英语 broccoli','英语中通常按一类蔬菜、食材使用，并不因此必须当复数主语']],
 'steamed broccoli 是蒸西兰花；a head of broccoli 是一整颗；broccoli florets 是分开的小花球。整体食材常不可数。',
 'steamed broccoli；a head of broccoli；broccoli florets。',
 'broccoli 常指绿色西兰花；cauliflower 常指白色花椰菜。Broccoli is ready 用 is，不能照搬意大利词尾去判断英语单复数。',
 ('The broccoli is ready to serve.','西兰花可以上桌了。'),('She added broccoli florets to the pasta.','她往意面里加了西兰花小花球。'),sources=S('broccoli','broccoli'))
W('spinach','英、美 /ˈspɪnɪtʃ/','菠菜',
 '一把柔软绿叶，炒过后体积明显缩下去，是 spinach。先把它和日常食材画面对应上，词尾拼写不用逐段猜意思。',
 '经盎格鲁法语 spinache、古法语 espinache 等形式借入；通常还联系阿拉伯语、波斯语的菠菜名称，但罗曼语形式的更远来源存在争论。',
 [['古法语 espinache 等 → 英语 spinach','跨语言借入的蔬菜名'],['较远常接阿拉伯语、波斯语材料，但有争论','旧时联系拉丁 spina 刺的解释不宜当作定论']],
 'fresh spinach 是鲜菠菜；baby spinach 是嫩菠菜叶。作为食材通常不可数，a bag of spinach 数的是一袋。',
 'fresh spinach；baby spinach；a bag of spinach。',
 'spinach 的常见词尾读 /ɪtʃ/；也存在 /ɪdʒ/ 变体。名称的远源不宜只因拼写像 spine 就断定由脊柱、刺派生。',
 ('Stir the spinach into the hot soup.','把菠菜拌进热汤里。'),('We used baby spinach in the salad.','我们用嫩菠菜叶做了沙拉。'),sources=S('spinach','spinach'))
W('beet','英、美 /biːt/','甜菜；〔尤美〕甜菜根',
 '切开会留下深红汁液的圆根，英语里常叫 beet 或 beetroot。甜菜也包括不同栽培类型，不是每次说 beet 都只指同一种红根。',
 '经古英语 bete 借拉丁 beta 植物名；更远有凯尔特语来源的说法，但并不完全确定。beet + root 才是把“根”明说出来的复合词。',
 [['拉丁 beta 甜菜 → 古英语 bete → 英语 beet','早期借入的植物名'],['beet + root → beetroot','把植物名与根组合，明确所吃的部位']],
 'a beet 数一个根菜；beet salad 是甜菜沙拉；sugar beet 是制糖用的甜菜。美式日常食物语境也常见复数 beets。',
 'a roasted beet；beet salad；sugar beet。',
 'beet 与 beat 击打同音，来源不同。beetroot 的 root 才是根的意思，不能漏掉这层组合关系。',
 ('She sliced a roasted beet into the salad.','她把一颗烤甜菜切片加进沙拉。'),('The farm grows sugar beet.','农场种植糖用甜菜。'),sources=S('beet','beet'))
W('zucchini','英 /zʊˈkiːni/；美 /zuˈkiːni/','西葫芦〔常见于美式等英语〕',
 '细长的嫩瓜，外皮常见绿色，切片煎或烤，常叫 zucchini。它是西葫芦；英国菜谱里常换用 courgette 这个名称。',
 '借意大利 zucchini，原为 zucchino 的复数；zucchino 是 zucca 瓜的小称形式。zucca 更远可能接晚期拉丁 cucutia，但后面的来源不确定。',
 [['意大利 zucca 瓜 → zucchino 小瓜 → 复数 zucchini','小称 + 意大利复数的旧构词'],['意大利 zucchini → 英语 zucchini','英语中既能按食材使用，也能说 a zucchini 一根西葫芦']],
 'grilled zucchini 是烤西葫芦；a zucchini 可数一根。借进英语后，不必每次都把意大利复数形式当成只能表示多个。',
 'grilled zucchini；sliced zucchini；a zucchini。',
 'zucchini 和 courgette 的常见差别主要是地区用词；cucumber 黄瓜则是另一种食材。',
 ('She cut a zucchini into thick slices.','她把一根西葫芦切成厚片。'),('The pasta comes with grilled zucchini.','这份意面配有烤西葫芦。'),sources=S('zucchini','zucchini'))
W('courgette','英 /kʊəˈʒet/；美 /kʊɚˈʒɛt/','西葫芦〔常见于英式英语〕',
 '英国超市里的一根西葫芦，标签可能写 courgette。到了美国菜谱，同类食材常写 zucchini，先建立这组对应就很好用。',
 '借法语 courgette：courge 瓜 + 小称材料 -ette，像“小瓜”。构词发生在法语中，整个名称进入英语；g 在这里读 /ʒ/。',
 [['法语 courge 瓜 + -ette 小称 → courgette','法语内部的小瓜名称'],['法语 courgette → 英语 courgette','英国、爱尔兰等地常用的西葫芦名']],
 'a courgette 数一根；courgette soup 是西葫芦汤。重音落在最后一节，不按常见英语 get 读中间字母。',
 'a courgette；courgette soup；sliced courgette。',
 'courgette 通常对应 zucchini；两者分别借法语、意大利语。现代两词不是互相缩写或英语里替换一个后缀形成的。',
 ('Grate a courgette into the mixture.','把一根西葫芦擦成丝，加进混合物。'),('The cafe serves courgette soup with bread.','这家咖啡馆供应配面包的西葫芦汤。'),sources=S('courgette','courgette'))
W('mushroom','英 /ˈmʌʃruːm/；美 /ˈmʌʃrum/','蘑菇；迅速增长、迅速扩大',
 '一朵蘑菇像突然从地上冒出来。mushroom 作动词时，就把这个画面借给数量和规模：很快长出一大片。',
 '经古法语 meisseron、盎格鲁法语 musherun 等借入；更远是否与法语 mousse 苔藓一族有关，有不同意见。现代整体名词后来转作动词。',MUSHROOM,
 'a mushroom 是一朵蘑菇；mushroom soup 是蘑菇汤；costs can mushroom 表示费用能迅速膨胀。名称不是现代英语 mush + room 的房间组合。',
 'a mushroom；mushroom soup；costs mushroom。',
 'mushroom 是常见菌类形态和名称；fungus 的范围更广，还包含霉菌、酵母等。动词 mushroom 强调快速增长，不只是普通 grow。',
 ('A mushroom grew beside the old stump.','老树桩旁长出了一朵蘑菇。'),('Without clear limits, small costs can mushroom.','没有明确限制，小额费用也可能迅速膨胀。'),sources=S('mushroom','mushroom'))
W('mushrooms','英 /ˈmʌʃruːmz/；美 /ˈmʌʃrumz/','蘑菇〔复数〕；迅速增长〔第三人称单数〕',
 '盘子里几朵蘑菇，是 mushrooms；说 a problem mushrooms，则是一个问题迅速扩大。看前面的主语和句子位置，就能分清。',
 'mushroom + -s → mushrooms，名词复数或动词第三人称单数，词尾均读 /z/。动词来自整个蘑菇名的快速冒出联想。',MUSHROOM+[['mushroom + -s → mushrooms','名词数多个；动词搭配单数主语']],
 'fried mushrooms 是炒蘑菇；the workload mushrooms 是工作量迅速增加。两个用法共享外形，但句法位置不同。',
 'fresh mushrooms；fried mushrooms；the workload mushrooms。',
 'mushrooms are 用复数主语；the workload mushrooms 中，mushrooms 本身就是谓语，后面不再加 are。',
 ('She fried the mushrooms with garlic.','她用大蒜炒了这些蘑菇。'),('The workload mushrooms whenever we add another project.','每增加一个项目，工作量就会迅速上升。'),sources=S('mushrooms','mushroom'))
W('turmeric','英 /ˈtɜːmərɪk/；美 /ˈtɝmərɪk/','姜黄；姜黄粉',
 '能把饭菜染成亮黄色的那种香料，常是 turmeric。它来自姜科植物的地下茎；先抓住“黄色香料”这个厨房画面。',
 '现代形式由中古英语 turmeryte 等演变；更远来源不确定。有资料比较拉丁 terra merita 字面“值得的土”等形式，也有联系阿拉伯 kurkum 的分析，不能当作已证实的单一路线。',
 [['中古英语 turmeryte 等 → 英语 turmeric','更早来自哪里仍有争论'],['terra merita、kurkum 等是远源讨论中的材料','现代常指姜黄及磨成的黄色香料']],
 'ground turmeric 是姜黄粉；a pinch of turmeric 是一小撮。词源的不确定不妨碍先用常见食谱搭配掌握它。',
 'ground turmeric；a pinch of turmeric；turmeric rice。',
 'turmeric 是姜黄；ginger 是姜；cumin 是孜然。它们都能是香料，具体风味与食材不同。',
 ('Add a pinch of turmeric to the rice.','往米饭里加一小撮姜黄粉。'),('The turmeric gave the sauce a bright yellow colour.','姜黄让酱汁呈现鲜黄色。'),sources=S('turmeric','turmeric'))
W('cumin','英 /ˈkjuːmɪn/；美 /ˈkʌmɪn/','孜然；孜然籽、孜然粉',
 '烤肉上那股熟悉的孜然香，对应 cumin。整粒时说 cumin seeds，磨成粉时说 ground cumin，名字跟着食材形态一起用。',
 '古英语 cymen 借拉丁 cuminum，接希腊 kyminon；希伯来 kammon、阿拉伯 kammun 等也有对应香料名称。',
 [['希腊 kyminon 等近东香料名称 → 拉丁 cuminum','存在希伯来、阿拉伯语对应词'],['拉丁 cuminum → 古英语 cymen → 英语 cumin','现代食谱中指孜然及相关香料']],
 'cumin seeds 是通常当籽粒使用的香料；ground cumin 是磨粉后的形式。cumin 自身作食材名通常不可数。',
 'cumin seeds；ground cumin；a teaspoon of cumin。',
 'cumin 的常见读音有 /ˈkjuːmɪn/、/ˈkʌmɪn/ 等变体；不是看到 cu 就只能读一种。菜单里别和 cinnamon 肉桂混淆。',
 ('Toast the cumin seeds in a dry pan.','把孜然籽放进干锅里烘香。'),('The recipe calls for a teaspoon of ground cumin.','这份食谱需要一茶匙孜然粉。'),sources=S('cumin','cumin'))
W('lentil','英 /ˈlentəl/；美 /ˈlɛntəl/','小扁豆；兵豆；小扁豆植株',
 '小小一粒，圆而扁，中间略鼓，这种 lentil 的形状后来还帮光学镜片起了名字：两面鼓起的透镜很像它。',
 '经古法语 lentille 借拉丁 lenticula，它是 lens、lent- 小扁豆的小称形式；现代英语 lens 透镜则借同一拉丁植物名的形状。',LENTIL,
 'a lentil 数一粒；lentil soup 把豆名当汤的食材修饰语。中文“小扁豆、兵豆”比笼统扁豆更能避免和其他豆种混淆。',
 'a lentil；lentil soup；a lentil dish。',
 '词源上先有扁豆名，透镜名称借的是形状；学习时把 lentil 放在 lens 前面，更容易看清命名画面。',
 ('A single lentil rolled across the table.','一粒小扁豆从桌上滚了过去。'),('She made a thick lentil soup for lunch.','她做了一锅浓稠的小扁豆汤当午餐。'),sources=S('lentil','lentil'))
W('lentils','英 /ˈlentəlz/；美 /ˈlɛntəlz/','小扁豆、兵豆〔复数〕',
 '一袋红色或绿色的小扁豆，通常说 lentils。做一锅汤会用很多粒，日常食谱因此常用复数。',
 'lentil + -s → lentils，词尾读 /z/。拉丁 lens 的小称经法语变成英语 lentil，现代再加英语复数。',LENTIL+[['lentil + -s → lentils','一粒到多粒，复数后缀读 /z/']],
 'red lentils 是红小扁豆；green lentils 是绿小扁豆。rinse the lentils 是把这些豆子冲洗一下。',
 'red lentils；green lentils；a bag of lentils。',
 'lentils 是豆粒；lenses 是 lens 的复数，指镜片、镜头等。两者较远同源，现代复数却分别接在不同基础词后。',
 ('Rinse the lentils before adding them to the pot.','把小扁豆冲洗后再放进锅里。'),('The cupboard contains rice, lentils and flour.','橱柜里有米、小扁豆和面粉。'),sources=S('lentils','lentil'))
W('sesame','英、美 /ˈsesəmi/','芝麻；芝麻植物',
 '面包上那一粒粒芝麻，或拌菜用的芝麻油，都对应 sesame。籽粒能榨油，名字的更早背景也和油籽有关。',
 '经拉丁 sesamum、希腊 sēsamon，较远通常接腓尼基语等近东语言的名称；与古代两河地区“油籽”一类词形相联系。',
 [['古代近东油籽名称 → 希腊 sēsamon → 拉丁 sesamum','香料、油料名称随语言接触传播'],['英语 sesame：芝麻、芝麻植物','Open Sesame 又通过阿里巴巴故事成为开门咒语及比喻']],
 'sesame seeds 是芝麻粒；sesame oil 是芝麻油。Open Sesame 是“芝麻开门”，后来也能比喻打开机会的诀窍、通行口令。',
 'sesame seeds；sesame oil；Open Sesame。',
 'sesame 的最后 e 在常见发音里读 /i/，不是不发音的 e。sesame oil 名称修饰的是油，通常不把 sesame 写成复数。',
 ('Sprinkle sesame seeds over the noodles.','在面条上撒些芝麻。'),('A few drops of sesame oil gave the dish a nutty aroma.','几滴芝麻油给这道菜添了坚果般的香气。'),sources=S('sesame','sesame'))
W('mustard','英 /ˈmʌstəd/；美 /ˈmʌstɚd/','芥末；芥末酱；芥菜类植物；芥末黄',
 '热狗上挤的一条黄色、带辛味的酱，常是 mustard。名称更早来自做酱时加入的葡萄汁、酒液材料，后来又指植物和颜色。',
 '古法语 mostarde 接 moust 新葡萄汁、未充分发酵酒液，再接拉丁 mustum 新酒；旧时把这类液体与磨碎的籽混成酱，是命名背景。法语 -arde 是旧名中的构词材料。',
 [['拉丁 mustum 新酒 → 古法语 moust → mostarde','以旧制酱所加的液体命名'],['英语 mustard：调味酱、籽 → 植物；再借指芥末黄色','这里的 must 酒液与 must 必须是不同来源的词']],
 'mustard seeds 是芥末籽；a spoonful of mustard 是一勺芥末酱；a mustard jacket 可指芥末黄色夹克。具体含义看搭配。',
 'mustard seeds；a spoonful of mustard；mustard yellow。',
 'mustard 通常是芥末类调味料；wasabi 是山葵相关名称，不宜把所有绿色辛辣酱都当成同一种原料。cut the mustard 是够格、达到要求。',
 ('He added mustard to the sandwich.','他在三明治里加了芥末酱。'),('The new printer does not quite cut the mustard.','这台新打印机还不太能满足要求。'),sources=S('mustard','mustard'))
def extend_lessons():
 extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_zii',ROOTS,WORDS)
 extend_lessons()
