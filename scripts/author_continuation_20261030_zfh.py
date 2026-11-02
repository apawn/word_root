"""Soaking, drenching, scouring, wetting and becoming dry."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
def S(word,base):
 return ['https://en.wiktionary.org/wiki/'+word+'#English','https://www.etymonline.com/word/'+base]
EXISTING_ROOT_ADDITIONS={
 'B3103':dict(words=['suck','soak','soaks','soaked','soaking'],label='suck 与 soak 的旧吸液材料',note='soak 承古英语 socian，是 sucan 吸一系的旧次生形式；联系在古代词族层面，不是现代英语把 suck 按规则改拼成 soak。'),
 'B2542':dict(words=['drink','drench','drenches','drenched','drenching'],label='drink 与 drench 的旧使动关系',note='drench 承古英语 drencan，是 drincan 喝的旧使动形式，早有使饮、浸透等义；现代 drench 常说浇透、弄湿透。'),
 'C1262':dict(words=['saturate','saturates','saturated','saturating'],label='satur：填满到浸透、饱和',note='拉丁 satur 满、saturare 填满、saturatus 已填满接英语 saturate；与 satis 足够相关，不从水这个现代意思推造同源。'),
 'B4610':dict(words=['water','waterlogged'],label='waterlogged 的进水、浸水画面',note='较早形容词 waterlogged 出现在船只进水、沉重难行的语境，waterlog 动词较晚，可能由它逆构；现代规则拆分与记录先后分清。'),
 'B3443':dict(words=['log','waterlogged'],label='waterlogged 的 log：原木般沉重难动',note='这里联系原木名词 log，早期像把船变成水里沉重木块；不是程序日志 log。更远 log 的来源有争论，不硬排北欧直接借入链。'),
 'B3010':dict(words=['wet','wets','wetted','wetting'],label='wet 的动词变化：使湿、变湿',note='动词和形容词各有古英语相关材料；过去式 wet、wetted 均用，wetted 双写 t 加完整 -ed，不能把 wets 只当形容词的错误复数。'),
 'B3042':dict(words=['dry','dries','dried','drying','drier','dryer'],label='dry 的三单、比较级与器具名词',note='dries 是 dry 变 y 为 i 加 -es；drier 可是形容词比较级，也可是干燥器名词的拼写，名词常另拼 dryer，-er 功能分开。'),
 'A1697':dict(words=['dry','drier','dryer'],label='drier 的比较级与器具 -er',note='drier 作比较级表示更干，作名词可表示使干燥的设备；同形的 -er 功能不同，不能把更干的天气解释成一台干燥机。'),
 'A1839':dict(words=['soggy','sogginess'],label='soggy 到 sogginess：湿软这一状态',note='soggy 变 y 为 i，再接完整 -ness；基础 sog 一系更早来源未定，不强连成现代 soak 的直接派生。'),
 'A1741':dict(words=['sopping'],label='sopping wet 的浸透状态',note='sopping 来自 sop 双写 p 再加完整 -ing；sop 的旧浸泡、泡软材料写在单词里，现代 sopping wet 常直接强调湿透。'),
 'A1760':dict(words='soak soaks soaked soaking drench drenches drenched drenching saturate saturates saturating wring wrings scour scours scoured scouring swab swabs swabbed swabbing wet wets wetted wetting'.split(),label='浸湿、拧挤、擦洗与使湿动词的变化',note='scour 的擦洗与四处搜寻分近源；swab 的工具名、动作有缩短、逆构等分析，不把现代 swab + -er 当所有历史形式的唯一起点。'),
}
SOAK=[['古英语 socian → 中古英语 soken → soak','浸在液体中；与 sucan 吸一系的旧次生形式有关'],['浸泡、吸满 → 充分吸收等比喻','soak up 阳光、气氛、知识，不要求把对象当水喝下']]
W('soak','/səʊk/〔英〕；/soʊk/〔美〕','浸泡、浸透；吸收；一次浸泡',
 '把东西放在水里，让水慢慢进到里面，是 soak；海绵吸满水，也能用它。重点不是表面沾一点，而是让液体进入、停留。',
 '承古英语 socian，经中古英语 soken；与旧 sucan 吸的词族有关。不是现代 suck 按规则变元音后就能随意构造出的新词。',SOAK,
 'soak beans 是泡豆子，soak up water 是吸水；soak up the atmosphere 是充分感受气氛，a long soak 是好好泡一会儿。',
 'soak overnight 泡一夜；soak through 浸透。',
 'soak 常重浸泡、吸进去，rinse 更重用水冲掉表面东西；泡豆子和冲一下豆子不是同一个动作。',
 ('Leave the beans to soak overnight.','把豆子留着泡一夜。'),('The sponge can soak up a lot of water.','这块海绵能吸进很多水。'),sources=S('soak','soak'))
W('soaks','英 /səʊks/；美 /soʊks/','浸泡、浸透、吸收〔第三人称单数〕；浸泡〔复数〕',
 '东西在水里慢慢吸进去，或布、海绵把水吸住，用 soaks。作名词复数还可说几次好好浸泡、泡澡。',
 'soak + -s，/k/ 后读 /s/；oa 仍读英 /əʊ/、美 /oʊ/，不因加词尾变元音。',SOAK+[['soak + -s → soaks','它浸泡、吸收；多次浸泡']],
 'soaks in the sink 是在水槽里泡着，soaks up the water 是吸进水；soaks up the sun 是舒服地晒太阳。',
 'soaks through the cloth 浸透布；long soaks 长时间浸泡。',
 'soaks up 把液体、光或体验吸进去；gives off 则向外发出，方向感相反。',
 ('The cloth soaks up the spilled water.','布把洒出的水吸进去。'),('She soaks the dried mushrooms before cooking them.','她做干蘑菇前先把它们泡一泡。'),sources=S('soaks','soak'))
W('soaked','英 /səʊkt/；美 /soʊkt/','浸泡了、浸透了；湿透的；吸收了',
 '水已经进到东西里面、把它弄得湿透，叫 soaked；大雨把人从头淋湿，也说 got soaked。',
 'soak + 完整 -ed，/k/ 后读 /t/；词尾不另添一个音节。',SOAK+[['soak + -ed → soaked','过去浸泡；已经浸湿透的状态']],
 'soaked in water 是泡在水里，soaked to the skin 是浑身湿透；soaked up the atmosphere 是充分感受了气氛。',
 'completely soaked 完全湿透；soaked clothes 湿透的衣服。',
 'soaked 比 damp 强得多，后者只是微湿；to the skin 是湿透的强调，不是一定在讨论皮肤状况。',
 ('We were soaked by the time we reached home.','我们到家时已经湿透了。'),('She soaked the bowl before washing it.','她洗碗前先把碗泡了一会儿。'),sources=S('soaked','soak'))
W('soaking','英 /ˈsəʊkɪŋ/；美 /ˈsoʊkɪŋ/','正在浸泡、吸收；浸泡；〔soaking wet〕湿透的',
 '东西正放在水里让液体进去，是 soaking；soaking wet 直接说湿得很透，像刚从水里捞出来。',
 'soak + 完整 -ing，直接加；活动名词与状态形容用法都来自浸泡动作，不双写 k。',SOAK+[['soak + -ing → soaking','浸泡过程；湿透的强调状态']],
 'soaking the beans 是正在泡豆子，give it a soaking 是让它泡透；soaking up the view 是尽情欣赏景色。',
 'soaking wet 湿透了；soaking in warm water 泡在温水里。',
 'soaking 可写正在做的事，也可在 soaking wet 中加强湿的程度；I am soaking wet 不等于我现在正在泡澡。',
 ('The beans are soaking in a bowl of water.','豆子正泡在一碗水里。'),('My coat was soaking wet after the storm.','风暴过后，我的外套湿透了。'),sources=S('soaking','soak'))
DRENCH=[['古英语 drincan 喝的使动形式 drencan → drench','使饮、浸透、淹没等；古代使动关系，不是现代可自由替换的拼写规则'],['现代常用浇透、淋透','让物体吸进大量液体；也可说阳光、颜色等铺满']]
W('drench','/drentʃ/','使湿透、淋透、浇透',
 '一盆水、大雨或浪一下把人和衣服弄得透湿，叫 drench。重点是湿得彻底，液体从外面大量上来。',
 '承古英语 drencan，它是 drincan 喝的旧使动形式，早有使饮、浸透等义；现代词义以把东西弄湿透最常见。',DRENCH,
 'drench someone 是把人淋透，drench the ground 是把地浇透；be drenched in sunlight 又可说满满沐在阳光里。',
 'drench with water 用水浇透；drench the clothes 淋透衣服。',
 'soak 常能说放在水里慢慢泡，drench 常更让人想到大量水从外面淋上；两者在湿透结果上会重合。',
 ('The sudden shower was enough to drench us.','突来的一阵雨足以把我们淋透。'),('Use enough water to drench the dry soil.','用足够的水把干土浇透。'),sources=S('drench','drench'))
W('drenches','/ˈdrentʃɪz/','使湿透、淋透、浇透〔第三人称单数〕',
 '雨、大浪或喷水装置把东西一下弄透湿，用 drenches。雨量、泼水量给人很足的感觉。',
 'drench + -es，/tʃ/ 后读 /ɪz/，多一个音节；旧使动词已成完整基础，再接现代三单。',DRENCH+[['drench + -es → drenches','它把人或物淋透、浇透']],
 'drenches the crowd 是把人群淋透，drenches the field 是把田地浇透；还可比喻颜色、光线铺满。',
 'drenches everything 把一切淋透；drenches the leaves with water 用水把叶片淋透。',
 'drenches 比 dampens 强，后者可只是让一点点湿；同样说给地浇水，强调的湿度、液量不同。',
 ('A passing wave drenches everyone near the rail.','一阵浪打过，把栏杆边的人全淋透。'),('The sprinkler drenches the dry patch of ground.','洒水器把那片干地浇透。'),sources=S('drenches','drench'))
W('drenched','/drentʃt/','淋透、浇透了；湿透的；充满某种光色的',
 '衣服吸满水、人从头湿透，是 drenched；drenched in sunlight 则像阳光从四面铺满，借彻底覆盖的感觉。',
 'drench + 完整 -ed，/tʃ/ 后读 /t/，结尾 /tʃt/；不是 /tʃɪd/。',DRENCH+[['drench + -ed → drenched','已淋透、湿透；光色铺满的比喻']],
 'drenched by the rain 是被雨淋透，drenched in sweat 是汗湿透；a sun-drenched terrace 是阳光洒满的露台。',
 'completely drenched 完全湿透；drenched clothes 淋透的衣服。',
 'drenched 和 soaked 都能形容湿透；drenched 更容易保留被雨、水从外面淋上来的画面，不是绝对区别。',
 ('We arrived home drenched by the rain.','我们被雨淋透，回到了家。'),('The terrace was drenched in afternoon sunlight.','午后的阳光洒满了露台。'),sources=S('drenched','drench'))
W('drenching','/ˈdrentʃɪŋ/','正在淋透、浇透；使人湿透的；一次浇淋',
 '雨或一大股水正把东西淋得透湿，是 drenching；a drenching rain 可直接把雨描述成会把人淋透的雨。',
 'drench + 完整 -ing，直接加；分词、形容词和活动名词都保留大量湿透的动作感。',DRENCH+[['drench + -ing → drenching','淋透过程；会把人湿透的雨或水']],
 'drenching rain 是淋透人的大雨，get a drenching 是挨了一场浇淋；drenching the soil 是正把土浇透。',
 'a sudden drenching 突然一场浇淋；drenching the garden 把花园浇透。',
 'drenching rain 与 drizzle 雨势差别很直观：前者能把人湿透，后者细密轻小，不能都只译下雨。',
 ('We walked through a drenching rain.','我们走在足以把人淋透的大雨里。'),('The hose was drenching the flower bed.','软管里的水正把花坛浇透。'),sources=S('drenching','drench'))
SATURATE=[['拉丁 satur 满的 → saturare 填满 → saturatus 已填满','英语 saturate 从填得够满的材料发展'],['填满 → 液体吸满、饱和；市场充斥','核心是容纳、接受能力接近被占满，不只说表面湿']]
W('saturates','/ˈsætʃəreɪts/','浸透、使饱和、使充斥〔第三人称单数〕',
 '水把海绵孔隙填得满满，或产品、广告把市场塞得到处都是，用 saturates。抓住吸满、占满的程度。',
 'saturate + -s，保留 e，/t/ 后读 /s/；基础来自拉丁 saturatus、saturare、satur 满一系，不是一个水专用根。',SATURATE+[['saturate + -s → saturates','它使浸透、饱和或充斥']],
 'saturates the soil 是把土浸透，saturates the market 是产品充斥市场；后者可含供应过多的感觉。',
 'saturates the sponge 浸满海绵；saturates the air with sound 让声音充满空气。',
 'saturates 比 wets 更强调填满、达到很高含量；wets 只说弄湿，未必接近再也吸不进。',
 ('Heavy rain saturates the soil.','大雨把土壤浸透。'),('The company saturates the market with cheap products.','公司用廉价产品充斥市场。'),sources=S('saturates','saturate'))
W('saturating','/ˈsætʃəreɪtɪŋ/','正在浸透、使饱和、使充斥',
 '液体或某种东西正一层层填满容纳空间，是 saturating。也可写把广告、产品铺得满满，尽量占住注意力或市场。',
 'saturate 去 e + 完整 -ing；基础里的 -ate 留在动词干里，不把 -ating 整体当不可拆的后缀。',SATURATE+[['saturate 去 e + -ing → saturating','使含量、覆盖达到很满的过程']],
 'saturating the cloth 是把布浸满，saturating the market 是让市场到处都是产品；作用对象不同，填满感相同。',
 'saturating the ground 浸透地面；saturating the media with adverts 用广告铺满媒体。',
 'saturating 讲使之变满的过程，saturated 常说已经饱和、浸透的状态；阶段不同。',
 ('Water was saturating the thin cloth.','水正把薄布浸透。'),('The campaign is saturating social media with adverts.','这场宣传正用广告铺满社交媒体。'),sources=S('saturating','saturate'))
W('wrings','/rɪŋz/','拧、绞、拧挤出；费力获取〔第三人称单数〕',
 '两手朝不同方向拧毛巾，让水挤出来，用 wrings；wrings her hands 则像绞扭手指，表现焦急、痛苦。',
 'wring + -s，/ŋ/ 后读 /z/，w 不发音。基础承古英语 wringan，现代过去式、过去分词另用 wrung。',
 [['古英语 wringan → 中古英语 wringen → wring','扭转、绞挤柔软物'],['wring + -s → wrings','他、她拧绞；比喻费力取得、使人难受']],
 'wrings out a towel 是把毛巾拧干，wrings a promise out of someone 是费力逼得一句承诺；out of 突出从里面挤出来。',
 'wrings her hands 焦急地绞着双手；wrings water from the cloth 从布里拧出水。',
 'wrings 和 rings 常同音，前者扭拧，后者可说响铃；拧毛巾时写 wring，w 虽不读却属于拼写。',
 ('She wrings the water out of the towel.','她把毛巾里的水拧出来。'),('He wrings his hands while waiting for the news.','等消息时，他焦急地绞着双手。'),sources=S('wrings','wring'))
SCOUR=[['擦洗支线：拉丁 excurare → 法语、荷兰语相关形式 → scour','彻底照管、擦净；具体借入路径有讨论'],['搜寻支线：中古英语 scouren，或有北欧、法语移动材料','四处奔走搜查；后来与擦洗义互相影响，不把两条近源硬缩为一条']]
W('scours','英 /skaʊəz/；美 /skaʊrz/','用力擦洗、冲刷；四处仔细搜寻〔第三人称单数〕',
 '把锅底用力擦到干净，是 scours；把网页、书架一处处仔细找过去，也是 scours，但近源历史另有一条线。',
 'scour + -s，读 /z/。擦洗义可能经法语、荷兰语接拉丁 excurare；搜寻义另有北欧、法语移动材料分析，后来彼此影响。',SCOUR+[['scour + -s → scours','他、她擦洗或四处搜寻；水冲刷']],
 'scours the pan 是擦洗锅，scours the internet 是把网络翻个遍；对象帮你确定是实物清洗还是搜寻。',
 'scours the shops for bargains 四处逛店找便宜货；scours the rocks 冲刷岩石。',
 'scours for something 通常比 looks for 更彻底、范围更广；也不等于已经找到了，结果要另说。',
 ('She scours the pan until it shines.','她把锅用力擦到发亮。'),('He scours second-hand shops for old records.','他把二手店一家家找过去，寻旧唱片。'),sources=S('scours','scour'))
W('scoured','英 /skaʊəd/；美 /skaʊrd/','用力擦净了、冲刷了；四处搜寻了',
 '锅被磨擦到污垢掉了，或一个人把能找的地方翻了一圈，用 scoured。两个现代常用义要根据宾语理解。',
 'scour + 完整 -ed，读 /d/；英式基础末尾是元音，接 /d/，美式保留相应 r 音。',SCOUR+[['scour + -ed → scoured','过去擦洗、冲刷或搜寻']],
 'scoured the sink 是擦洗水槽，scoured the city for a room 是找遍城市寻住处；搜索义不必真擦过任何东西。',
 'scoured the shelves 找遍书架；scoured clean 擦得干净。',
 'scoured 与 cleaned 在擦洗场景可接近，前者通常更突出用力磨擦；搜寻场景则和 cleaned 无关。',
 ('I scoured the sink with a stiff brush.','我用硬刷子用力擦洗水槽。'),('We scoured the internet for a copy of the book.','我们把网络找了个遍，想找到这本书。'),sources=S('scoured','scour'))
W('scouring','英 /ˈskaʊərɪŋ/；美 /ˈskaʊrɪŋ/','正在用力擦洗、冲刷；四处仔细搜寻；擦洗用的',
 '刷子正把硬污垢磨掉，或人正一处处找线索，是 scouring。scouring pad 则是用来这样擦洗的清洁垫。',
 'scour + 完整 -ing；英式后接元音时 r 发出来，现代词尾用于擦洗、搜寻两个动词支线。',SCOUR+[['scour + -ing → scouring','擦洗、搜寻的过程；供擦洗的工具用途']],
 'scouring the pan 是正在擦锅，scouring the area 是正仔细搜查区域；a scouring pad 是百洁布、擦洗垫。',
 'scouring powder 去污粉；scouring the archives 翻查档案。',
 'scouring 常有彻底、仔细、用力的感觉；rinsing 通常是用水冲洗，未必把黏住的污垢磨掉。',
 ('She was scouring the burnt pan.','她正用力擦洗烧焦的锅。'),('The researchers were scouring the archives for letters.','研究者们正翻查档案，寻找书信。'),sources=S('scouring','scour'))
SWAB=[['荷兰语 zwabber 等 → 英语 swabber → 缩短工具名 swab','较早指清理甲板的绳纱拖把'],['工具名、动作词的进一步发展','swab 动词或由 swabber 逆构；后来也用于吸水棉、拭子及取样，现代拆分不等于最早记录顺序']]
W('swab','英 /swɒb/；美 /swɑːb/','拭子、吸水棉棒；用来擦拭或采样的棉团；擦、拭取样本',
 '拿一小团吸水的棉、布擦过表面，叫 swab；这团东西本身也叫 a swab，采样时则把表面一点材料带走。',
 '较早清甲板工具名 swab 缩自 swabber，联系荷兰语 zwabber。动作词还可能由 swabber 逆构，不把历史全部写成先 swab 动词再加 -er。',SWAB,
 'a cotton swab 是棉棒，a throat swab 是咽拭子样本或取样用具，swab the deck 是擦洗甲板；语境决定大小与用途。',
 'take a swab 取一份拭子样本；swab a surface 擦拭表面、拭取样本。',
 'swab 常明确用吸水材料擦、取样，wipe 泛指擦过；sample 是样本总称，不限定由拭子采得。',
 ('The artist used a cotton swab to soften the edge of the paint.','画家用棉棒把颜料边缘晕柔。'),('The nurse took a swab from his throat.','护士从他的咽部取了一份拭子样本。'),sources=S('swab','swab'))
W('swabs','英 /swɒbz/；美 /swɑːbz/','拭子、棉棒、拭子样本〔复数〕；擦拭、拭取样本〔第三人称单数〕',
 '几根棉棒、几份拭子样本，叫 swabs；一个人拿吸水材料擦表面，也可以用动词三单 swabs。',
 'swab + -s，/b/ 后读 /z/；名词复数、动词三单同形。工具名的较早缩短路线另见基础词。',SWAB+[['swab + -s → swabs','多根棉棒、多个样本；他、她擦拭']],
 'cotton swabs 是棉棒，collect swabs 是收集拭子样本；swabs the deck 是擦洗甲板，属于动词第三人称单数。',
 'clean swabs 干净棉棒；swabs a surface 擦拭、取样表面。',
 'swabs 不等于所有 tests 检测：拭子是工具、采样方式或样本，检测还可能用血液等其他材料。',
 ('She used cotton swabs to blend the colours.','她用棉棒把颜色晕开。'),('The technician swabs each handle in turn.','技术人员按顺序擦拭每只把手。'),sources=S('swabs','swab'))
W('swabbed','英 /swɒbd/；美 /swɑːbd/','擦拭了、擦洗了；用拭子取样了',
 '刚才用棉团、布或拖把擦过一处，叫 swabbed；检查、采样场景里，可以是用拭子擦取了材料。',
 'swab 双写 b + 完整 -ed → swabbed，/b/ 后读 /d/；重读短元音单音节后一个辅音字母，按规则双写。',SWAB+[['swab 双写 b + -ed → swabbed','过去擦拭、擦洗或拭取样本']],
 'swabbed the deck 是擦洗了甲板，swabbed the surface 是擦拭或采样表面；具体功能由工具、后续动作说明。',
 'swabbed down a counter 擦过台面；swabbed for traces 拭取微量材料。',
 'swabbed 说采用了吸水材料接触表面的动作；scrubbed 更常强调来回用力擦，力度、目的可能不同。',
 ('The crew swabbed the deck before breakfast.','船员早饭前擦洗了甲板。'),('The technician swabbed the handle to collect a sample.','技术人员用拭子擦取把手上的材料，采集样本。'),sources=S('swabbed','swab'))
W('swabbing','英 /ˈswɒbɪŋ/；美 /ˈswɑːbɪŋ/','正在擦拭、擦洗；拭子采样及其过程',
 '吸水材料正擦过甲板、皮肤或物品表面，是 swabbing。语境可以是清洁，也可以是把少量材料收集起来。',
 'swab 双写 b + 完整 -ing → swabbing；双写保留短元音基础词的拼写，不代表多一次擦拭。',SWAB+[['swab 双写 b + -ing → swabbing','擦拭、采样的过程']],
 'swabbing the deck 是正擦洗甲板，surface swabbing 是表面拭子采样；名词活动不一定只指眼前进行的动作。',
 'swabbing down the table 擦拭桌面；swabbing for a sample 拭取样本。',
 'swabbing、sampling 可重合，但 sampling 更广；swabbing 具体说明通过擦过表面来采材料。',
 ('The sailors were swabbing the deck.','水手们正擦洗甲板。'),('The technician spent the morning swabbing several surfaces.','技术人员上午在几处表面做拭子采样。'),sources=S('swabbing','swab'))
W('sopping','英 /ˈsɒpɪŋ/；美 /ˈsɑːpɪŋ/','湿透的；浸湿、吸取液体的过程',
 '衣服、鞋湿得透透、像吸满水的海绵，可以说 sopping wet。日常先把它当很湿、湿透的强烈表达来用。',
 'sop 双写 p + 完整 -ing；旧 sop、soppian 有浸泡、泡软材料，现代分词、形容词保留被水浸透的状态。',
 [['古英语 sop、soppian 等 → 中古英语 soppen → sop','浸泡、使液体吸进去；浸软的东西'],['sop 双写 p + -ing → sopping','浸湿动作；sopping wet 中强调湿透']],
 'sopping wet 是湿透，sopping up spilled water 是吸起洒出的水；后一种仍是 sop up 的动作。',
 'sopping clothes 湿透的衣服；sopping wet shoes 湿透的鞋。',
 'sopping wet 与 soaking wet 意思很近，都比 a little damp 强得多；区别通常是习惯表达，而非精确含水比例。',
 ('My shoes were sopping wet after the walk.','走完那段路，我的鞋湿透了。'),('She took off her sopping coat at the door.','她在门口脱下湿透的外套。'),sources=S('sopping','sop'))
W('sogginess','英 /ˈsɒɡinəs/；美 /ˈsɑːɡinəs/','湿软、湿塌的状态',
 '炸物吸了水不脆、面包被汤汁泡软，那种湿塌塌的状态就是 sogginess。说的不只是有水，还常嫌原来的挺、脆没了。',
 'soggy 变 y 为 i，再接完整 -ness → sogginess；基础 sog 一系来源未定，不把现代 soak 当它确定的直接父词。',
 [['旧 sog 湿地、浸透等材料 → soggy','湿软、湿重；更远联系未定'],['soggy 变 y 为 i + -ness → sogginess','湿软这一性质、状态']],
 'the sogginess of the pastry 是酥皮的湿软，avoid sogginess 是避免变得湿塌；通常作为不可数性质名词。',
 'unpleasant sogginess 让人不喜欢的湿软；sogginess at the bottom 底部湿塌。',
 'sogginess 与 dampness 都可有湿，但前者还常突出软、失去脆挺；轻微潮气不一定使东西 soggy。',
 ('The sogginess of the pastry spoiled the pie.','酥皮湿塌塌的，影响了馅饼口感。'),('Too much sauce can add to the sogginess of the bread.','酱汁太多，会让面包更湿软。'),sources=S('sogginess','soggy'))
W('waterlogged','英 /ˈwɔːtəlɒɡd/；美 /ˈwɔːtərlɑːɡd/','浸透水的、积水严重的；进水后沉重难动的',
 '土、木头或物体吸进太多水，湿得沉沉、排不出去，叫 waterlogged。球场因积水不能比赛，是很常见的场景。',
 'water + log 的原木画面，较早形容词 waterlogged 像说船进水后变成沉重、难动的木块。现代可按 waterlog 双写 g + 完整 -ed 理解，但 waterlog 动词的记录较晚，可能是逆构。',
 [['十八世纪先有 waterlogged 形容词','船进水，像原木般沉重、失去灵活性'],['较晚 waterlog 动词；现代 waterlogged 的扩展','土壤、场地、木头等被水浸透、积水']],
 'waterlogged soil 是积水浸透的土，a waterlogged pitch 是积水严重的球场；现代不要求东西真是一块原木。',
 'waterlogged ground 浸水地面；waterlogged timber 吸满水的木料。',
 'waterlogged 常比 wet 更强调水过量、渗透或排不掉；不是只说表面刚沾了一点水。',
 ('The match was postponed because the pitch was waterlogged.','球场积水严重，比赛延期了。'),('The waterlogged wood was heavy to carry.','吸满水的木头搬起来很沉。'),sources=S('waterlogged','waterlogged'))
W('wets','/wets/','弄湿、使湿；尿湿〔第三人称单数〕',
 '一个人把海绵、手、嘴唇润湿，用 wets；wets the bed 则是尿湿床铺，具体液体和动作靠对象分清。',
 '动词 wet + -s，/t/ 后读 /s/；这是“使湿”的三单，形容词 wet 本身不靠 -s 变化数。',
 [['古英语 wætan 等 → wet 动词','使湿、变湿，与湿的形容词有旧词族联系'],['wet + -s → wets','他、她使湿；尿湿某物的现代用法']],
 'wets the sponge 是弄湿海绵，wets her lips 是润湿嘴唇；wets the bed 在日常语境指尿床。',
 'wets a cloth 把布润湿；wets the surface 使表面变湿。',
 'wets 只说有了湿的变化，不必浸透；drenches、saturates 常把充分、彻底湿透说得更明显。',
 ('She wets the sponge before cleaning the board.','她擦板子前先把海绵弄湿。'),('He wets his lips before beginning the speech.','开始讲话前，他润了润嘴唇。'),sources=S('wets','wet'))
W('wetted','/ˈwetɪd/','弄湿了、使湿了；尿湿了',
 '布、手指或表面刚才被润上水，用 wetted。wet 也可作过去式，这个有词尾的形式同样存在。',
 'wet 双写 t + 完整 -ed → wetted；/t/ 后读 /ɪd/，多一个音节。现代过去式、过去分词也用 wet，按地区、语境有偏好。',
 [['古英语 wætan 等 → wet 动词','使湿、变湿的旧材料'],['wet 双写 t + -ed → wetted；另有 wet','现代两种过去式、过去分词形式']],
 'wetted the cloth 是把布润湿，wetted her finger 是润湿手指；不必一律改成过去式 wet，wetted 也是正确形式。',
 'slightly wetted 稍微润湿；wetted with water 用水弄湿。',
 'wetted 强调发生了使湿的动作，was wet 可以只说处于湿的状态；同样有湿，叙述重点不同。',
 ('She wetted the cloth and wiped the table.','她把布润湿，擦了桌子。'),('He wetted his finger to turn the page.','他润湿手指，翻过书页。'),sources=S('wetted','wet'))
W('wetting','/ˈwetɪŋ/','正在弄湿、变湿；润湿过程；尿湿',
 '液体正让表面变湿，是 wetting；wetting the bed 则是尿床这一用法，常可把整件事当活动名词说。',
 'wet 双写 t + 完整 -ing → wetting；短元音重读单音节末尾的 t 双写，词尾表示过程。',
 [['古英语 wet 的相关动词材料 → wet','使湿、变湿'],['wet 双写 t + -ing → wetting','润湿过程；相应尿湿用法也能变化']],
 'wetting the paper 是把纸润湿，surface wetting 是表面润湿；wetting the bed 在生活语境是尿床。',
 'wetting a sponge 弄湿海绵；wetting the cloth 润湿布。',
 'wetting 可写主动弄湿，也可在日常搭配里说尿湿；具体含义由宾语与场景决定，不一律译成浇水。',
 ('She was wetting the paper before folding it.','她正把纸润湿，再折叠。'),('The child had been wetting the bed.','那个孩子有一阵子一直尿床。'),sources=S('wetting','wet'))
W('dries','/draɪz/','使干、擦干、变干〔第三人称单数〕',
 '水分正散掉、布把表面擦干，用 dries。它可以说东西自己变干，也可以说某人、设备让它干。',
 'dry 的 y 前是辅音字母，变 y 为 i，再加 -es → dries，读 /draɪz/；基础词不是 drie。',
 [['古英语 drygan → 中古英语 drien → dry 动词','使干、失去水分；与 dry 形容词同族'],['dry 变 y 为 i + -es → dries','它变干；他、她把东西弄干']],
 'paint dries 是油漆变干，dries the dishes 是擦干餐具；dries up 还能比喻供应、想法等枯竭。',
 'dries quickly 很快变干；dries her hair 弄干头发。',
 'dries 可以不靠热：风吹、自然放着、用布擦都能干；heats 只说明加热，不保证已经干。',
 ('This paint dries quickly.','这种油漆干得快。'),('He dries the dishes while I wash them.','我洗餐具，他负责擦干。'),sources=S('dries','dry'))
W('drier','英 /ˈdraɪə/；美 /ˈdraɪər/','更干的、较少水分的；干燥器〔也拼 dryer〕',
 '两处相比，水分少一点、天气没那么湿，叫 drier；作为名词又能指把东西弄干的器具，和 dryer 是同类拼法。',
 '比较级：dry 变 y 为 i + 比较级 -er → drier。器具名词则是 dry 动词 + 执行者 -er 的另一层，名词 drier、dryer 均有，现代设备名常拼 dryer。',
 [['dry 形容词 + 比较级 -er → drier','更干、较少水分'],['dry 动词 + 器具 -er → drier、dryer','使东西变干的人或设备；不是把比较级直接变设备']],
 'drier weather 是较干的天气，a hair drier 是吹风机；an air dryer 也可说烘干、干燥设备，拼法和词性分别看。',
 'a little drier 稍干一点；a tumble drier 滚筒烘干机。',
 'drier 作比较级时回答干的程度，作器具名词时回答用什么干燥；同一 -er 外形有不同工作。',
 ('The weather should be drier tomorrow.','明天的天气应该会干燥些。'),('The hotel room had a hair drier.','酒店房间里有一台吹风机。'),sources=S('drier','drier'))
def extend_lessons():
 extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_zfh',ROOTS,WORDS)
 extend_lessons()
