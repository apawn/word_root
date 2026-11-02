"""Useful furniture and clothing words, with genuine derivation and everyday scenes."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
def S(word,base):
 a=['https://en.wiktionary.org/wiki/'+word+'#English','https://www.etymonline.com/word/'+('Ottoman' if base=='ottoman' else base)]
 if base in ['futon','chaise']:a.append('https://www.merriam-webster.com/dictionary/'+base)
 return a
EXISTING_ROOT_ADDITIONS={
 'B2739':dict(words='mattress mattresses quilt quilts cushion cushions futon cot cots crib cribs bunks'.split(),label='bed 对照：床垫、被子、坐垫与几类床',note='按坐卧用品对照，不表示各词都由 bed 派生。mattress 远接阿拉伯铺垫名；quilt 接拉丁床垫名；cushion 经法语，远源有分歧；futon 借日语；cot 床义经南亚语言；crib 承古英语饲槽名。'),
 'C0524':dict(words='chaise armchairs'.split(),label='chaise 与 armchairs：椅子名称及组合',note='chaise 与 chair 是共同法语、拉丁椅子材料的不同形式，英语借 chaise 后有车、躺椅等用法；armchairs 则是 arm 扶手材料 + chair + 复数 -s。'),
 'C0684':dict(words='ottomans sofas'.split(),label='ottoman → ottomans；sofa → sofas',note='两个家具借名分别按英语规则加 -s，元音或 /n/ 后读 /z/。与 couch 对照家具类别，不把借词当 loc- 的派生词。'),
 'B2635':dict(words='armchairs'.split(),label='arm + chair → armchair → armchairs',note='椅子两侧像手臂般托住胳膊的部分叫 arm，armchair 是扶手椅；复数只加在整个复合词末尾。'),
 'B3468':dict(words='dressers'.split(),label='dress → dresser → dressers：人、备餐家具与抽屉柜',note='人的 dresser 接 dress + -er；家具名另有法语准备食物的桌、柜名称背景，后来也用于梳妆、收衣抽屉柜。不能把所有家具义当穿衣者变成柜子的故事。'),
 'C1209':dict(words='dressers'.split(),label='整理、准备的 dress 词线与 dressers',note='dress 远接拉丁使直、整理材料，后有准备食物、穿戴等义；dressers 可指穿着者、服装助理或相应柜桌，具体来源、用法分别解释。'),
 'A1697':dict(words='bunks'.split(),label='bunk → bunks：铺位、睡铺动作等',note='床铺名 bunk 常联系 bunker 座位义的缩短，现代复数 bunks；动词有在铺位睡、随意住宿或英式 bunk off 逃课逃工等用法。胡说 bunk 是 bunkum 缩略的另一支，不能归成床铺故事。'),
 'B4104':dict(words='hijab'.split(),label='veil 对照：hijab 的遮盖与头巾用法',note='借阿拉伯语 ḥijāb，根材料 h-j-b 遮挡、遮盖；旧有隔屏、遮挡等义，现代英语常说部分穆斯林女性所戴头巾，也可能说相关衣着观念。与英语 veil 只作意义对照。'),
 'B2430':dict(words='turban'.split(),label='head 对照：turban 缠绕式包头巾',note='名称经法语、意大利语等接土耳其语 tülbent，远接波斯语相关头巾名称；现代不同文化、款式均可使用这个服饰名，不把词当某单一人群的专属标签。'),
 'B2951':dict(words='poncho parka'.split(),label='coat 对照：斗篷式衣物与防寒外套',note='poncho 经美洲西语，远源有原住民织物名称分析；parka 经阿留申语、俄语等，远接西伯利亚相关皮制衣物名称。按外套用途对照，不把它们当英语 coat 的派生词。'),
 'B3015':dict(words='calico'.split(),label='Calicut 地名 → calico 棉布 → 花色用法',note='calico 接印度港口 Calicut 的名称变体，现代英国常说本色平纹棉布，美国也常说印花棉布；花杂色联想又进入 calico cat 三花猫等。'),
 'B2912':dict(words='moccasins'.split(),label='moccasin → moccasins：软皮鞋的借名',note='经北美阿尔冈昆语族语言的鞋名进入英语，常联系波瓦坦语 makasin；复数 -s 读 /z/。现代鞋款可受传统结构启发，不把所有软皮鞋的具体做法都说成一样。'),
}
MATTRESS=[['阿拉伯语 maṭraḥ 铺垫等名称，含投下、铺下的词根材料','经中世纪拉丁、意大利语等进入欧洲相关名称'],['古法语 materas 等 → 英语 mattress → mattresses','旧铺垫名发展为现代床垫；复数末尾 /ɪz/']]
QUILT=[['拉丁 culcita 床垫、靠垫 → 古法语 cuilte、quilte 等','旧义偏填充物做的床垫、垫层'],['英语 quilt → 缝合夹层的床被；又转作绗缝动词','重点是布层、填充物与缝线结合']]
CUSHION=[['古法语 coissin 等坐垫名 → 英语 cushion','更远常联系拉丁 coxa 髋、大腿等材料，也有不同分析'],['软垫吸收冲击的画面 → cushion 缓冲','名词也能指缓冲物，动词说减轻冲击']]
COT=[['印地语 khāṭ 等床名，接梵语相关名称材料','更远有南亚其他语言来源的分析'],['英语 cot → 轻便床、折叠床；英式常说婴儿床','与小屋义 cot 的日耳曼词线分开']]
CRIB=[['古英语 cribbe 饲槽、饲料箱 → crib','封围的小空间、容器的旧图景'],['crib → 有栏杆的婴儿床；又有住处、抄用等用法','具体后续命名不都确定，现代按语境分辨']]
W('mattress','英、美 /ˈmætrəs/','床垫',
 '床架上那块让人躺着承托身体的大垫子，就是 mattress。它在身子下面，和盖在身上的被子分开。',
 '经古法语 materas 等，向前接意大利语、中世纪拉丁与阿拉伯语 maṭraḥ 铺垫名；阿拉伯语材料含投下、铺下的词根和 ma- 名词构形。',MATTRESS,
 'a firm mattress 是较硬实的床垫；a soft mattress 是软床垫；put a sheet on the mattress 是在床垫上铺床单。',
 'a firm mattress；a soft mattress；a mattress on the floor。',
 'bed 可指整张床，mattress 特指承托身体的床垫；duvet、quilt 等通常是床上盖、铺的另一类用品。',
 ('The mattress rests on a wooden frame.','床垫放在木床架上。'),('She put a clean sheet on the mattress.','她在床垫上铺了一张干净床单。'),sources=S('mattress','mattress'))
W('mattresses','英、美 /ˈmætrəsɪz/','床垫〔复数〕',
 '仓库里几张床垫、客房需要换几张床垫，就用 mattresses。加复数后，比 mattress 多出一个弱读音节。',
 'mattress + -es → mattresses；基础词末尾是 /s/，复数读 /ɪz/。双 s 属原词拼写，后面加完整复数词尾 -es。',MATTRESS+[['mattress + -es → mattresses','/s/ 后加 /ɪz/，多一个音节']],
 'two mattresses 是两张床垫；spare mattresses 是备用床垫；replace the mattresses 是更换床垫。',
 'two mattresses；spare mattresses；replace the mattresses。',
 'mattress、mattresses 是单复数，不因 -es 变成床单或被子；同一类物品改变数量。',
 ('The room has two mattresses on the floor.','房间地上有两张床垫。'),('The staff moved the spare mattresses into storage.','工作人员把备用床垫搬进了储藏室。'),sources=S('mattresses','mattress'))
W('quilt','英、美 /kwɪlt/','绗缝被，夹层被；绗缝',
 '两层布中间夹填充物，再用一条条缝线把各层固定，这种被子常叫 quilt。缝线既固定夹层，也能做出图案。',
 '经法语接拉丁 culcita 床垫、靠垫名；英语由旧填充垫层义发展出缝合夹层的床被，再用名词作动词说绗缝。',QUILT,
 'a patchwork quilt 是拼布被；a quilt on the bed 是床上的夹层被；quilt the layers together 是把几层绗缝在一起。',
 'a patchwork quilt；a quilt on the bed；quilt the layers together。',
 'duvet 常是内有填充物、外配被套的被芯类用品；quilt 常强调缝合的层与表面，地区叫法也有交叉。',
 ('A patchwork quilt covered the bed.','床上盖着一床拼布被。'),('We learned to quilt the fabric layers together.','我们学会了把几层布绗缝在一起。'),sources=S('quilt','quilt'))
W('quilts','英、美 /kwɪlts/','绗缝被，夹层被〔复数〕；绗缝〔动词第三人称〕',
 '几床拼布、绗缝的夹层被是 quilts；she quilts 则是在说她做绗缝。数量和动作由前后词确定。',
 'quilt + -s → quilts；/t/ 后读 /s/，词尾 /lts/。既可名词复数，也可动词第三人称，不另加一个音节。',QUILT+[['quilt + -s → quilts','多床被子，或单数主语后的绗缝动作']],
 'handmade quilts 是手工绗缝被；patchwork quilts 是拼布被；quilts by hand 是用手绗缝。',
 'handmade quilts；patchwork quilts；quilts by hand。',
 '名词 quilts 可以是成品，动词 quilts 说制作动作；两者有明确名词转动词关系，不是仅凭拼写碰巧一样。',
 ('The exhibition displayed handmade quilts.','展览展示了手工绗缝被。'),('She quilts by hand in the evenings.','她晚上用手做绗缝。'),sources=S('quilts','quilt'))
W('cushion','英、美 /ˈkʊʃən/','坐垫，靠垫；缓冲物；缓冲、减轻冲击',
 '坐下时垫一块软的 cushion，让身体别直接撞上硬面。再把这幅画面扩大，就能理解减轻一次冲击、损失或打击。',
 '经古法语 coissin 等坐垫名进入英语。更远常联系拉丁髋、大腿的 coxa 材料，也有床垫名等分析；名词软垫后来转作缓冲动词。',CUSHION,
 'a sofa cushion 是沙发靠垫；cushion the impact 是缓冲冲击；a cushion against a shock 是应付冲击的缓冲。',
 'a sofa cushion；a soft cushion；cushion the impact。',
 'pillow 常说睡觉用枕头，cushion 常说座位上的坐垫、靠垫；抽象缓冲义不必真有一块布垫。',
 ('She put a cushion behind her back.','她在背后放了一个靠垫。'),('The foam helps cushion the impact.','泡沫有助于缓冲冲击。'),sources=S('cushion','cushion'))
W('cushions','英、美 /ˈkʊʃənz/','坐垫，靠垫〔复数〕；缓冲〔动词第三人称〕',
 '沙发上几个软垫是 cushions；the foam cushions the impact 则是在说泡沫缓冲冲击。软垫和减轻碰撞的画面相通。',
 'cushion + -s → cushions，/n/ 后读 /z/，词尾 /nz/。名词复数与动词第三人称同形。',CUSHION+[['cushion + -s → cushions','多个垫子，或单数主语后的缓冲动作']],
 'soft cushions 是软垫；sofa cushions 是沙发靠垫、坐垫；cushions the landing 是缓冲落地时的冲击。',
 'soft cushions；sofa cushions；cushions the impact。',
 '不是每个 cushions 都要数出几块垫子；动词后接 impact 等对象时，要按减轻冲击理解。',
 ('The sofa has three blue cushions.','沙发上有三个蓝色靠垫。'),('The thick layer cushions the impact when the box is moved.','移动箱子时，那层厚垫料能缓冲冲击。'),sources=S('cushions','cushion'))
W('futon','英 /ˈfuːtɒn/；美 /ˈfuːtɑːn/','日式床垫；使用这类床垫的坐卧家具',
 '可铺在地上睡的日式软床垫，常叫 futon；英语也常把配这种床垫、能坐能躺的家具叫 futon。',
 '借日语 futon，现代写作布団，较远常追到汉语蒲团：蒲草等编成的圆坐垫。名称在日语中用于寝具，再借入英语说床垫及相应坐卧家具。',
 [['汉语蒲团的名称材料 → 日语 futon','有蒲草、圆坐垫的命名背景，后来日语常写布団'],['日语寝具名 futon → 英语 futon','整词借入，现代常说相应床垫'],['床垫名 → 配有这类床垫的坐卧家具','英语常说可转换坐卧用途的家具']],
 'sleep on a futon 是睡这种床垫；fold up the futon 是把它折收；a futon frame 是相应家具框架。',
 'sleep on a futon；fold up the futon；a futon frame。',
 '日语寝具与现代英语家具的范围不完全重合；看到照片、房间介绍时，先判断是地铺床垫还是框架家具。',
 ('We laid a futon on the floor for the guest.','我们给客人在地上铺了一张日式床垫。'),('The futon opens into a bed at night.','那张坐卧家具晚上可以展开成床。'),sources=S('futon','futon'))
W('chaise','英、美 /ʃeɪz/，也读 /ʃez/','躺椅〔常缩 chaise longue〕；旧式轻便马车〔历史〕',
 '家具介绍里的 chaise 常说能伸腿倚躺的长椅；旧小说里的 chaise 则可能是一种轻便马车。时代、场景决定对象。',
 '借法语 chaise 椅子，与英语 chair 接同一较远的法语、拉丁座椅材料。英语先有轻便马车等用法，现代家具义常缩自 chaise longue 长椅。',
 [['法语 chaise 椅子，与 chaire 等形式相关','远接拉丁 cathedra 座椅材料，与 chair 有历史关系'],['英语 chaise 的马车用法；chaise longue → 短称 chaise','多个现代、历史用法，不能把马车与躺椅简单当同一物品']],
 'a chaise by the window 是窗边躺椅；a chaise longue 是躺椅的完整常见名称；小说的 a chaise and horses 可能说车马。',
 'a chaise by the window；a chaise longue；a chaise and horses。',
 '法语 longue 是长的；美式常见 chaise lounge 是受熟悉的 lounge 联想影响的形式。两种英语写法看语境识别。',
 ('She read on the chaise beside the window.','她躺在窗边的长椅上读书。'),('In the novel, a chaise carried the visitors to the estate.','小说里，一辆轻便马车把来客送到了庄园。'),sources=S('chaise','chaise'))
W('ottomans','英 /ˈɒtəmənz/；美 /ˈɑːtəmənz/','软垫脚凳；无靠背软垫座椅〔复数〕',
 '客厅里几张能坐、能搁脚的小软垫凳，叫 ottomans。来自历史风格名称的词，如今按普通家具名计数。',
 'ottoman + -s → ottomans，/n/ 后读 /z/，词尾 /nz/。家具名单数有 Ottoman 风格名称到软垫座椅、脚凳的历史。',
 [['Ottoman 风格名称 → ottoman 软垫家具名','旧命名接相关坐卧风格联想'],['ottoman + -s → ottomans','多个软垫座椅、脚凳；普通名词通常小写']],
 'two ottomans 是两张软垫凳；storage ottomans 是有收纳功能的软垫凳；ottomans beside the sofa 是沙发旁的几张。',
 'two ottomans；storage ottomans；small ottomans。',
 '家具名 ottomans 与历史族群、朝代名的大写 Ottomans 要看场景分辨；本条先掌握现代客厅用法。',
 ('Two small ottomans stood in front of the sofa.','沙发前放着两张小软垫凳。'),('The room uses ottomans as extra seats.','这个房间用软垫凳作额外座位。'),sources=S('ottomans','ottoman'))
W('sofas','英 /ˈsəʊfəz/；美 /ˈsoʊfəz/','沙发〔复数〕',
 '客厅或展厅里有两张、几张沙发，便用 sofas。名字本来是借来的坐台、长座名，现代按英语规则变化。',
 'sofa + -s → sofas；元音后读 /z/。末尾 a 保留，直接加 s，不需要另添一个 /ɪz/ 音节。',
 [['阿拉伯语坐台名，经土耳其语等 → sofa','旧坐卧空间名称发展为现代软垫长座'],['sofa + -s → sofas','多张沙发，词尾 /z/']],
 'two sofas 是两张沙发；leather sofas 是皮沙发；sofas facing each other 是面对面摆的沙发。',
 'two sofas；leather sofas；sofas facing each other。',
 '沙发上放的 cushions 是靠垫、坐垫；sofas 是整张家具。复数词尾相近，物品层级却不同。',
 ('The living room has two sofas facing each other.','客厅里有两张面对面摆的沙发。'),('The showroom displays sofas in several sizes.','展厅里陈列着几种尺寸的沙发。'),sources=S('sofas','sofa'))
W('armchairs','英 /ˈɑːmtʃeəz/；美 /ˈɑːrmtʃerz/','扶手椅〔复数〕',
 '两边有地方托住胳膊、一般一人一座的椅子，叫 armchair；几张便是 armchairs。扶手像椅子伸出的手臂。',
 'arm 手臂、扶手 + chair 椅子 → armchair；整个复合名词加 -s → armchairs，词尾 /z/。chair 经法语接拉丁座椅名，arm 的手臂词史另讲。',
 [['arm 扶手 + chair 椅子 → armchair','用结构直接命名扶手椅'],['armchair + -s → armchairs','复数加在整个复合词末尾']],
 'two armchairs 是两张扶手椅；comfortable armchairs 是舒适扶手椅；armchairs beside the fire 是壁炉边的扶手椅。',
 'two armchairs；comfortable armchairs；armchairs by the window。',
 'armchair 的单数还可修饰 critic 等，表示只坐着评论、缺少亲身实践；本条复数 armchairs 通常直接数家具。',
 ('Two armchairs stood by the window.','窗边放着两张扶手椅。'),('We moved the armchairs closer to the fireplace.','我们把扶手椅往壁炉边挪近了些。'),sources=S('armchairs','armchair'))
W('dressers','英 /ˈdresəz/；美 /ˈdrɛsɚz/','抽屉衣柜、梳妆柜〔常见美式等〕；餐具柜〔英式等〕；穿着者、服装助理〔复数〕',
 '家具店里的 dressers 可能是放衣物的抽屉柜；英国厨房里的也可能是放餐具的柜架。说 smart dressers 则在形容穿着讲究的人。',
 'dresser + -s → dressers。人物线可拆 dress 穿戴 + -er 人；家具线有法语准备、陈列食物的桌柜名称背景，后来扩展到收衣、梳妆家具，不都由穿衣者义直接来。',
 [['dress 整理、准备、穿戴等 → dresser 人物名','-er 可以表示相应做事的人'],['法语备餐桌柜名等 → dresser 家具义','与准备、陈列的旧 dress 材料相接'],['dresser + -s → dressers','不同名词义按语境变复数，词尾 /z/']],
 'bedroom dressers 是卧室抽屉柜；kitchen dressers 在英式等语境说餐具柜架；smart dressers 是穿着讲究的人。',
 'bedroom dressers；kitchen dressers；smart dressers。',
 '不要因为 dress 现在很熟悉穿衣义，就把所有 dresser 都想成给人穿衣的人；家具义也保留准备、陈列的旧用法背景。',
 ('The shop sells wooden dressers for bedrooms.','这家店卖卧室用的木制抽屉柜。'),('Both of them are smart dressers.','他们两个人都穿得很讲究。'),sources=S('dressers','dresser'))
W('cot','英 /kɒt/；美 /kɑːt/','婴儿床〔英式常见〕；轻便折叠床〔美式等常见〕',
 '英国家长说 a cot，常是有栏杆的婴儿床；美国旅行、临时住宿说 a cot，常是轻便折叠床。先看地区和场景。',
 '床义经印地语 khāṭ 等接南亚床名，向前有梵语、其他南亚语言来源的分析。英语从轻便床发展出折叠床、婴儿床等用法；小屋 cot 是另一条词源。',COT,
 'a baby cot 是婴儿床；a folding cot 是折叠床；a camp cot 是露营等使用的轻便床。',
 'a baby cot；a folding cot；a camp cot。',
 '英式 cot 与美式 crib 常可对应婴儿床；美式 cot 则不能每次都译成婴儿床，要看是否在临时睡铺场景。',
 ('The baby was asleep in the cot.','宝宝在婴儿床里睡着了。'),('The shelter provided a folding cot for each guest.','临时住宿处给每位住客配了一张折叠床。'),sources=S('cot','cot'))
W('cots','英 /kɒts/；美 /kɑːts/','婴儿床；轻便折叠床〔复数，按地区和场景〕',
 '几张婴儿床，或一排临时折叠床，都可能叫 cots。加复数只改变数量，哪种床仍靠场景判断。',
 'cot + -s → cots；/t/ 后读 /s/，词尾 /ts/。床义词从南亚相关名称借入，再按英语规则变复数。',COT+[['cot + -s → cots','多张相应床具，词尾 /ts/']],
 'two cots 是两张相应小床；baby cots 是婴儿床；folding cots 是折叠床。',
 'baby cots；folding cots；a row of cots。',
 'cots 没有固定只能说婴儿床的跨地区意义；baby、folding、camp 等词能帮你迅速认准对象。',
 ('The nursery has two baby cots.','婴儿房里有两张婴儿床。'),('A row of folding cots lined the hall.','大厅里沿边摆了一排折叠床。'),sources=S('cots','cot'))
W('crib','英、美 /krɪb/','婴儿床〔常见美式〕；住处〔俚语〕；抄用，抄袭；辅助答案、笔记〔按语境〕',
 'a crib 常是四周有栏杆的婴儿床；welcome to my crib 的随意说法是在欢迎你来我住处；crib from a book 则是从书里抄用。几个现代用法分别掌握。',
 '承古英语 cribbe 饲槽、饲料箱等名称，封围容器的图景延伸到婴儿床。抄用的动词常联系较早偷取用法，具体早期细节有不确定处，住处俚语也不必全归成同一故事。',CRIB+[['较早 crib 动词偷取 → 学生口语抄用等','借用、抄取的语义延伸，精确起点不完全确定']],
 'a baby crib 是婴儿床；crib from a book 是从书里抄用；a crib sheet 常说提示、速查或辅助答案，是否作弊要看实际场景。',
 'a baby crib；crib from a book；a crib sheet。',
 '英语常见美式 crib 与英式 cot 可对应婴儿床；住处、笔记、抄用义要看上下文，不能全译成小床。',
 ('The baby was asleep in the crib.','宝宝在婴儿床里睡着了。'),('He tried to crib a paragraph from an old report.','他试图从一份旧报告里抄用一段话。'),('“Welcome to my crib,” she joked as she opened the door.','她开门时开玩笑说：“欢迎来我这儿。”'),sources=S('crib','crib'))
W('cribs','英、美 /krɪbz/','婴儿床〔复数〕；抄用〔动词第三人称〕；住处、辅助笔记等〔按语境〕',
 '婴儿房里几张小床是 cribs；someone cribs from a report 则是在说某人从报告里抄用。末尾 s 同时可服务名词和动词。',
 'crib + -s → cribs；/b/ 后读 /z/，词尾 /bz/。基础词的饲槽、婴儿床历史与抄用等后续词义，不能只靠 s 来辨认。',CRIB+[['crib + -s → cribs','名词复数或动词第三人称，词尾 /bz/']],
 'baby cribs 是婴儿床；two cribs 是两张小床；cribs from another source 是从另一来源抄用。',
 'baby cribs；two cribs；cribs from another source。',
 'cribs 在家具、育儿场景先认小床；在主语后接 from 等时可能是抄用动词。数量和词性都由句法确定。',
 ('The nursery has three baby cribs.','婴儿房里有三张婴儿床。'),('The article cribs several lines from an earlier essay.','这篇文章从一篇早先的短文里抄了几行。'),sources=S('cribs','crib'))
W('bunks','英、美 /bʌŋks/','铺位〔复数〕；睡、住宿〔第三人称〕；逃课、逃工〔常见英式 bunk off〕',
 '船舱、宿舍里一层层或紧凑布置的铺位，叫 bunks；he bunks with a friend 是和朋友同住、借住；bunks off 则可能是逃课逃工。',
 'bunk + -s → bunks，/k/ 后读 /s/，词尾 /ŋks/。床铺名可能缩自 bunker 的座位义；睡铺动词接名词，逃课逃工用法另按短语历史理解。',
 [['bunker 座位义可能缩成 bunk 铺位','现代床铺名称及相关睡、住宿动词'],['bunk + -s → bunks；bunk off 为逃课逃工的短语','不同现代用法按搭配识别']],
 'upper bunks 是上铺；bunks with a friend 是和朋友同住；bunks off school 是逃课。',
 'upper bunks；bunks with a friend；bunks off school。',
 '胡说的 bunk 缩 bunkum，是另一来源支线；这里的复数床铺、睡铺动词不能从胡说义硬推。',
 ('The cabin has four bunks.','船舱里有四个铺位。'),('He bunks with a friend when he visits the city.','他来城里时借住在朋友那里。'),('The character often bunks off school in the story.','故事里那个角色经常逃课。'),sources=S('bunks','bunk'))
W('hijab','英 /hɪˈdʒɑːb/；美 /hɪˈdʒɑːb/','希贾布，头巾；相关遮盖、衣着观念〔按语境〕',
 '现代英语常用 hijab 指部分穆斯林女性戴的头巾；较宽语境里，也可能在谈有关遮盖、衣着的观念。先分具体衣物和较宽概念。',
 '借阿拉伯语 ḥijāb，接 h-j-b 遮挡、遮盖的根材料，原有隔屏、帘幕等含义。现代英语在头巾、衣着语境中使用这个名称。',
 [['阿拉伯语 h-j-b 遮挡材料 → ḥijāb','有隔屏、遮盖等名称义'],['ḥijāb → 英语 hijab','常具体说头巾，也可谈相关衣着观念']],
 'wear a hijab 是戴头巾；a blue hijab 是蓝色头巾；the history of hijab 可能在谈衣着观念、习俗的历史。',
 'wear a hijab；a blue hijab；a silk hijab。',
 'hijab、turban、burqa 等名称对应不同服饰、覆盖方式，不能把所有头巾、罩衣一律当成同一个词。',
 ('She chose a blue hijab to match her coat.','她选了一条蓝色头巾来配外套。'),('The portrait shows a woman wearing a hijab.','那幅肖像画着一位戴头巾的女性。'),sources=S('hijab','hijab'))
W('turban','英 /ˈtɜːbən/；美 /ˈtɜːrbən/','包头巾，缠绕式头巾',
 '把一长条布缠绕在头上形成头饰，常叫 turban。不同地区、文化和时装中的具体包法会有差别，先认缠绕的结构。',
 '经法语 turbant、意大利语 turbante 等形式，接土耳其语 tülbent 纱布、头巾等材料，远接波斯语 dulband 的相关头巾名。',
 [['波斯语相关头巾名 → 土耳其语 tülbent 等','头巾、纱布类名称材料传播'],['意大利语、法语等形式 → 英语 turban','借入改形，现代泛用于相应缠绕式头饰']],
 'a blue turban 是蓝色包头巾；wear a turban 是戴包头巾；tie a turban 是缠、系头巾。',
 'a blue turban；wear a turban；tie a turban。',
 'turban 和 tulip 郁金香有较远名称联系，后者有花形像包头巾的命名解释；现代两个词分别说头饰和花。',
 ('He wore a blue turban in the portrait.','肖像里他戴着蓝色包头巾。'),('The costume included a brightly coloured turban.','那套演出服配了一顶色彩鲜艳的包头巾。'),sources=S('turban','turban'))
W('poncho','英 /ˈpɒntʃəʊ/；美 /ˈpɑːntʃoʊ/','斗篷式套头衣；斗篷式雨衣',
 '像一大片布，中间开口套过头，布料向身体四周垂下，便是典型 poncho 的结构。既有保暖服装，也有雨衣版本。',
 '借美洲西班牙语 poncho。更远有克丘亚语 punchu、马普切语相关毛织物名等不同分析，不把其中一条当唯一已定路线。',
 [['美洲原住民相关衣物、织物名称的不同来源分析','较远细节有分歧'],['美洲西班牙语 poncho → 英语 poncho','斗篷式服装，后来也广用于相应结构雨衣']],
 'a wool poncho 是羊毛斗篷式衣；a rain poncho 是斗篷式雨衣；put on a poncho 是穿上这类衣物。',
 'a wool poncho；a rain poncho；put on a poncho。',
 'poncho 主要帮助你想到套头、披垂的结构，不能仅凭名称断定是羊毛、防水材料或某一固定产地。',
 ('She put on a rain poncho before leaving the tent.','离开帐篷前，她穿上了一件斗篷式雨衣。'),('The poncho hung loosely over his shoulders.','那件斗篷式衣物松松地垂在他肩上。'),sources=S('poncho','poncho'))
W('parka','英 /ˈpɑːkə/；美 /ˈpɑːrkə/','派克式防寒外套，常带兜帽',
 '长一些、常带兜帽的防寒外套，叫 parka。今天有各种面料、填充物，旧名称则接北方皮制服装的背景。',
 '经阿留申语、俄语 parka 等传播，远处常追到西伯利亚涅涅茨语等相关皮制衣物名。现代英语将名称用于类似防寒外套。',
 [['西伯利亚相关皮制衣物名 → 俄语、阿留申语等 parka','借名在多种语言间传播'],['英语 parka → 现代带帽防寒外套等','旧名称保留，材料、设计可变化']],
 'a winter parka 是冬季防寒外套；a hooded parka 是带帽款；zip up a parka 是拉好外套拉链。',
 'a winter parka；a hooded parka；zip up a parka。',
 'parka 与 anorak 在日常叫法中可能交叉，但名称和具体款式不总完全重合；旧皮衣词源也不保证现代衣物使用皮毛。',
 ('He zipped up his parka before stepping outside.','出门前，他拉好了防寒外套的拉链。'),('She hung her winter parka beside the door.','她把冬季防寒外套挂在门边。'),sources=S('parka','parka'))
W('calico','英 /ˈkælɪkəʊ/；美 /ˈkælɪkoʊ/','本色棉布〔英式等〕；印花棉布〔美式等〕；花杂色的，三花猫',
 '英国缝纫语境里的 calico 常是本色平纹棉布；美国旧布料用法常指印花棉布。由花色布的画面，又能说 calico cat 三花猫。',
 '来自印度港口 Calicut 的名称变体，旧贸易中的棉布名。英语在不同地区所指布料范围分化，再借花杂颜色形容动物等。',
 [['Calicut 地名 → kalyko cloth 等贸易布名','地名用于相关棉布名称'],['英语 calico 的地区布料义 → 花杂颜色用法','印花布的联想进入 calico cat 等搭配']],
 'a piece of calico 是一块这种棉布；a calico dress 在相应语境说印花棉布裙；a calico cat 是三花猫。',
 'a piece of calico；a calico dress；a calico cat。',
 '地名参与命名不表示现代 calico 必须产自那座港口；说猫时是花色名称，不能按布料字面翻译。',
 ('She used calico to make a trial version of the dress.','她用本色棉布做了一件裙子的试样。'),('A calico cat was sleeping on the windowsill.','一只三花猫在窗台上睡觉。'),sources=S('calico','calico'))
W('moccasins','英 /ˈmɒkəsɪnz/；美 /ˈmɑːkəsɪnz/','莫卡辛软皮鞋〔复数〕',
 '柔软皮革包住脚、常能看见鞋面缝合结构的那类软皮鞋，叫 moccasins。现代也有受传统样式启发的不同鞋款。',
 'moccasin 借北美阿尔冈昆语族语言的鞋名，常联系波瓦坦语 makasin；现代加 -s → moccasins，/n/ 后读 /z/。',
 [['北美阿尔冈昆语族相关鞋名 → 英语 moccasin','早期借词常联系弗吉尼亚地区波瓦坦语材料'],['moccasin + -s → moccasins','多只软皮鞋，或通常按一双来谈']],
 'a pair of moccasins 是一双软皮鞋；leather moccasins 是皮制软鞋；wear moccasins 是穿这类鞋。',
 'a pair of moccasins；leather moccasins；soft moccasins。',
 '来源接具体原住民语言的鞋名，进入英语后按常规变复数；现代款式不一定完整复制传统鞋底、材料结构。',
 ('He wore soft leather moccasins indoors.','他在室内穿着柔软的皮制莫卡辛鞋。'),('She packed a pair of moccasins for the trip.','她为旅行带了一双莫卡辛软皮鞋。'),sources=S('moccasins','moccasin'))
def extend_lessons():
 extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_zjk',ROOTS,WORDS)
 extend_lessons()
