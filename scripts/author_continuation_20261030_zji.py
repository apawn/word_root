"""Common clothing and fabric names with cautious naming histories."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
def S(word,base):
 a=['https://en.wiktionary.org/wiki/'+word+'#English']
 if base=='spandex':a.append('https://www.merriam-webster.com/dictionary/spandex')
 else:a.append('https://www.etymonline.com/word/'+base)
 if base in ['satin','tweed']:a.append('https://www.merriam-webster.com/dictionary/'+base)
 if word=='leggings':a.append('https://www.merriam-webster.com/dictionary/leggings')
 return a
EXISTING_ROOT_ADDITIONS={
 'B3722':dict(words='cardigan cardigans tuxedo'.split(),label='与 jacket 对照：开衫与晚礼服的命名',note='这里按服装用途对照，不表示各词都由 jacket 派生。cardigan 以 Cardigan 伯爵头衔命名，tuxedo 接 Tuxedo Park 地名；词名来源与现代实际产地、设计者身份分开。'),
 'B3737':dict(words='blazers'.split(),label='blaze → blazer → blazers：亮眼到夹克名',note='blaze 发光、燃烧 + -er 的名物用法，衣服义有鲜艳划艇夹克背景；blazers 是复数。现代 blazer 也能颜色素净，不由旧命名限制。'),
 'B2769':dict(words='leggings'.split(),label='leg → legging → leggings：腿部覆盖物到紧身裤',note='leg + 名词构词 -ing → legging，双写 g；现代 leggings 常说紧身长裤，通常用复数，数一条用 a pair。不是腿这个名词直接变成动作进行时。'),
 'A1776':dict(words='leggings pajamas pyjamas'.split(),label='常用复数衣物名：leggings、pajamas、pyjamas',note='这些衣物常以复数形式说一条裤子或一套睡衣，数件数常用 a pair of。pajamas、pyjamas 是同一睡衣名的常见美英拼写，远接波斯腿 + 衣物。'),
 'C1534':dict(words='trainers'.split(),label='train → trainer → trainers：训练者与运动鞋',note='训练词族有拉、引导成形的远处背景，train + -er 可说教练、训练设备，trainers 也常在英式英语里说运动鞋。用法并列，不能把教练变成鞋当唯一演化线。'),
 'B2801':dict(words='trainers'.split(),label='trainers：教练们；英式运动鞋',note='trainer 的复数，train 训练 + -er + -s。鞋义接运动、训练的用途，两个现代名词用法按上下文分辨。'),
 'B3019':dict(words='denim satin tweed khaki'.split(),label='cloth 对照：几种常见布料与颜色名称',note='此处比较材料和外观，不表示借词都由 cloth 派生。denim 接法语地名短语；satin 更远来源有争议；tweed 的命名有不同分析；khaki 接乌尔都语、波斯语尘土色材料。'),
 'B2904':dict(words='cashmere fleece'.split(),label='wool 对照：羊绒与整片羊毛、绒面材料',note='cashmere 接 Kashmir 的旧拼写，是地名用于纤维、织物；fleece 承古英语羊毛名，又发展绒面衣料与骗取钱财等用法。羊绒和普通羊毛的材料名不能随意互换。'),
 'B3015':dict(words='nylon spandex'.split(),label='与 cotton 对照：nylon、spandex 的现代造名',note='这里只比较纤维材料，合成纤维名不由英语 cotton 派生。nylon 是人为造出的名称；spandex 是 expands 的字母重排，表达弹性伸展的联想。'),
 'B3899':dict(words='spandex'.split(),label='stretch 对照：spandex 弹性纤维的造名',note='spandex 名称是 expands 的字母重排，不是现代词根 span + dex。伸展的图景帮助理解用途，与英语 stretch 只作意义对照。'),
 'C0287':dict(words='sequin sequins'.split(),label='金币名 → 装饰亮片：sequin、sequins',note='经法语 sequin、意大利语 zecchino 金币名，接 zecca 铸币厂与阿拉伯语铸币模材料；后来用于亮片。与 coin 对照，不能从英语 sequence 取词根解释。'),
 'C0955':dict(words=['spandex'],label='expands 字母重排 → spandex',note='expand 的伸展词族有拉丁 ex- 向外 + pandere 展开的材料；现代 expands 的字母重排得到 spandex，是造名游戏，不是普通加前后缀。'),
 'B3110':dict(words=['khaki'],label='dust 对照：khaki 的尘土色名称',note='波斯语 khāk 尘土的材料经乌尔都语进入 khaki，英语与 dust 只作词义对照，不表示来自英语 dust。'),
 'B2624':dict(words=['suede'],label='leather 对照：suede 绒面革',note='名称截自法语 gants de Suède 瑞典手套，材料义为绒面革；与英语 leather 比较类别，不由英语 leather 派生。'),
 'B3468':dict(words='kimono sari'.split(),label='dress 对照：和服与纱丽的借词名称',note='此处按服饰对照，不表示两词由 dress 派生。kimono 是日语穿 + 东西的组合；sari 经印地语等接更早南亚语言的衣物名。'),
}
CARDIGAN=[['第七代 Cardigan 伯爵的头衔 → 相关针织衣物名','与人物穿着风格、流行背景相连；不必声称由他发明'],['英语 cardigan → cardigans','开衫成为普通服装名，复数加 -s']]
PAJAMAS=[['波斯语腿、脚的材料 + 衣物材料 → 印地语、乌尔都语相关名称','原有宽松裤装的名称背景'],['借入英语 → pajamas／pyjamas','发展、固定为睡衣名，常指上衣与裤子的一套']]
SEQUIN=[['阿拉伯语铸币模材料 → 意大利语 zecca 铸币厂、zecchino 金币','经法语 sequin 借入英语金币名'],['金币、穿孔装饰物的形象 → 装饰亮片 sequin','再加英语复数 -s → sequins']]
W('cardigan','英 /ˈkɑːdɪɡən/；美 /ˈkɑːrdɪɡən/','针织开衫',
 '前襟能打开，常用纽扣等扣起来的针织上衣，就是 cardigan。先和需要从头套进去的普通套头毛衣区分。',
 '以第七代 Cardigan 伯爵的头衔命名，接其穿衣风格、流行背景。更远头衔接威尔士地名；现代不按 card、-igan 拆成英语意思。',CARDIGAN,
 'a wool cardigan 是羊毛开衫；button up a cardigan 是把开衫扣好；wear a cardigan over a shirt 是衬衫外穿开衫。',
 'a wool cardigan；a cardigan over a shirt；button up a cardigan。',
 'sweater 是较宽泛的针织上衣名，cardigan 重点在前襟可开合。以人物命名，也不能据此证明那个人亲自发明了衣服。',
 ('She wore a cardigan over her shirt.','她在衬衫外穿了一件针织开衫。'),('I left my cardigan on the back of the chair.','我把开衫落在椅背上了。'),sources=S('cardigan','cardigan'))
W('cardigans','英 /ˈkɑːdɪɡənz/；美 /ˈkɑːrdɪɡənz/','针织开衫〔复数〕',
 '衣柜里几件前襟能打开的针织上衣，可以说 cardigans。原本来自头衔的名字，现在照普通衣物名变复数。',
 'cardigan + -s → cardigans；/n/ 后读 /z/，词尾 /nz/。词内的原头衔名称保留，不在里面继续拆分。',CARDIGAN+[['cardigan + -s → cardigans','多件开衫，词尾 /nz/']],
 'two cardigans 是两件开衫；wool cardigans 是羊毛开衫；light cardigans 是轻薄开衫。',
 'two cardigans；wool cardigans；light cardigans。',
 '来源中的衣料、旧样式帮助理解命名背景，现代 cardigan 可以用不同材料制作；不能只凭名称断定一定纯羊毛。',
 ('The shop sells light cardigans for spring.','这家店卖春季穿的轻薄开衫。'),('She packed two cardigans for the trip.','她为旅行带了两件开衫。'),sources=S('cardigans','cardigan'))
W('blazers','英 /ˈbleɪzəz/；美 /ˈbleɪzɚz/','西装式夹克，休闲西装上衣〔复数〕',
 '衣架上一排能配不同裤子的西装式上衣，常叫 blazers。如今很多是深蓝、黑色，但名字的早期衣物背景很亮眼。',
 'blaze 发光、燃烧去末尾不发音 e，再加完整后缀 -er → blazer；衣服义与鲜艳、显眼的划艇俱乐部夹克背景有关。blazer + -s → blazers，词尾 /z/。',
 [['blaze → blazer 发亮、引人注意的东西','-er 在这里可构名物，不只表示人'],['鲜艳夹克名 → 现代 blazer → blazers','衣服用途扩大，复数按末尾读音变化']],
 'school blazers 是校服夹克；navy blazers 是海军蓝西装式上衣；wear blazers 是穿这类上衣。',
 'school blazers；navy blazers；blazers and trousers。',
 '现代 blazer 不一定鲜艳，也不一定配同料裤子；词源里的发亮帮助记名称，不是购物时判断款式的唯一标准。',
 ('The students wore navy blazers.','学生们穿着海军蓝西装式校服上衣。'),('The shop has blazers in several different fabrics.','这家店有几种不同面料的西装式夹克。'),sources=S('blazers','blazer'))
W('tuxedo','英 /tʌkˈsiːdəʊ/；美 /tʌkˈsiːdoʊ/','男式无尾晚礼服〔常见美式名称〕',
 '电影里正式晚宴上常见、配领结的那种晚礼服，可以叫 tuxedo。它有自己的礼服样式背景，不是所有深色西装的统称。',
 '接美国纽约 Tuxedo Park 的地名，相关社交场所与衣着风格推动名称使用。地名更远来源有不同解释，不硬拆英语 tux、-edo。',
 [['Tuxedo Park 地名与相关社交服装背景','衣服以场所名称命名，不等于在那里首次发明'],['英语 tuxedo → 这类晚礼服的通用名称','现代口语还可截短为 tux']],
 'wear a tuxedo 是穿晚礼服；rent a tuxedo 是租礼服；a tuxedo jacket 指其中的上衣。英式常见 dinner jacket、dinner suit 等对应说法。',
 'wear a tuxedo；rent a tuxedo；a tuxedo jacket。',
 'tuxedo 与 business suit 商务西装的具体用途、式样有区别；看到黑色外套，不能只凭颜色就都叫 tuxedo。',
 ('He rented a tuxedo for the evening reception.','他为晚间招待会租了一套晚礼服。'),('The tuxedo jacket was hanging beside his shirt.','晚礼服上衣挂在他的衬衫旁边。'),sources=S('tuxedo','tuxedo'))
W('leggings','英、美 /ˈleɡɪŋz/','紧身长裤，打底裤；护腿〔按场景〕',
 '今天服装店里的 leggings，常是贴腿的弹性长裤；旧用法和一些专门场景里，则是覆盖、保护腿部的护腿。核心画面都在腿上。',
 'leg 腿 + 名词构词 -ing → legging，双写 g；再加 -s → leggings。名词 legging 原有腿部覆盖物义，不等于动词正在抬腿。',
 [['leg + 名词 -ing → legging','双写 g，腿部覆盖物、护腿的名称'],['leggings → 现代常见紧身长裤用法','复数形式说一条裤子，常用 a pair 来计数']],
 'a pair of leggings 是一条紧身长裤；black leggings 是黑色打底裤；protective leggings 在专门场景中可能指护腿。',
 'a pair of leggings；black leggings；wear leggings。',
 '一条也常说 leggings，配 are；a pair of leggings 的中心是单数 pair，配 is。先看主语中心词。',
 ('She wore black leggings and a long sweater.','她穿着黑色打底裤和一件长毛衣。'),('This pair of leggings is very comfortable.','这条紧身长裤很舒服。'),sources=S('leggings','legging'))
W('pajamas','美 /pəˈdʒɑːməz/；英也见 /pəˈdʒɑːməz/','睡衣，睡衣裤〔常见美式拼写〕',
 '睡觉前换上的上衣、裤子，一套可以叫 pajamas。这个名字的老底子先指穿在腿上的宽松衣物。',
 '经印地语、乌尔都语相关形式，接波斯语腿、脚的 pāy 等材料 + jāma 衣物；英语加、固定复数词尾，后来广用于睡衣套装。',PAJAMAS,
 'wear pajamas 是穿睡衣；a pair of pajamas 是一套睡衣；pajama pants 指睡裤，修饰 pants 时常用单数形式。',
 'wear pajamas；a pair of pajamas；pajama pants。',
 'pajamas 与 pyjamas 是同一服装名的常见美英拼写。词源先说腿部衣物，不限制现代整套睡衣只能有裤子。',
 ('He changed into his pajamas after dinner.','晚饭后他换上了睡衣。'),('I packed an extra pair of pajamas.','我多带了一套睡衣。'),sources=S('pajamas','pajamas'))
W('pyjamas','英 /pɪˈdʒɑːməz/','睡衣，睡衣裤〔常见英式拼写〕',
 '英国等地常写 pyjamas，美国常写 pajamas；说的通常是同一类睡衣，不是两种不同衣料。',
 '同源于经南亚语言借入的腿、脚 + 衣物名称，英语有 pyjamas、pajamas 两种常见拼写。末尾 -s 属常用复数形式。',PAJAMAS+[['英语常见拼写分化：pyjamas、pajamas','拼写差别不改变服装类别']],
 'a pair of pyjamas 是一套睡衣；cotton pyjamas 是棉睡衣；pyjama top 指睡衣上装，修饰 top 时常用单数形式。',
 'a pair of pyjamas；cotton pyjamas；a pyjama top。',
 'My pyjamas are... 用复数；This pair of pyjamas is... 由单数 pair 决定动词。拼写 y 不负责这个单复数区别。',
 ('Her pyjamas are in the top drawer.','她的睡衣在最上面的抽屉里。'),('He bought a pair of cotton pyjamas.','他买了一套棉睡衣。'),sources=S('pyjamas','pajamas'))
W('trainers','英 /ˈtreɪnəz/；美 /ˈtreɪnɚz/','教练，培训师〔复数〕；运动鞋〔常见英式用法〕；训练设备〔复数〕',
 '健身房里的 trainers 可以是教练；脚上 a pair of trainers 则是运动鞋。共享训练这个用途，具体是人还是鞋，要看搭配。',
 'train 训练 + -er → trainer；加 -s → trainers。人的用法是训练者，鞋、设备的用法接训练用途，不必讲成教练后来变成鞋。',
 [['train + -er → trainer','训练的人，也可用于训练的设备'],['训练用鞋的命名 → trainer、trainers','鞋义在英式日常常见'],['trainer + -s → trainers','教练等的复数；一双鞋常用 a pair 来数']],
 'fitness trainers 是健身教练；a pair of trainers 是一双运动鞋；flight trainers 可能指飞行训练设备，需看上下文。',
 'fitness trainers；a pair of trainers；experienced trainers。',
 '运动鞋义常对应美式 sneakers；职业人物义与地区鞋名要分开，不把所有 trainers 都译成培训师。',
 ('The new staff met their trainers on Monday.','新员工周一见了培训师。'),('I put on my trainers before going for a walk.','出门散步前，我穿上了运动鞋。'),sources=S('trainers','trainer'))
W('denim','英、美 /ˈdenɪm/','牛仔布',
 '牛仔裤、牛仔夹克常见的那种较结实、有斜纹的布，叫 denim。它说材料，jeans 通常说裤子。',
 '通常接法语 serge de Nîmes 来自尼姆的斜纹织物短语，名称压缩、改形为 denim；后来英语所指织物范围也有变化。',
 [['法语地名短语 serge de Nîmes','Nîmes 是法国地名，de 表来自'],['借词改形 denim → 现代牛仔布名','旧名称传下，现代材料、产品不由地名限定产地']],
 'a denim jacket 是牛仔夹克；dark denim 是深色牛仔布；made of denim 是用牛仔布制成。',
 'a denim jacket；dark denim；made of denim。',
 'denim 是布名，jeans 是常见裤装名；denim jacket 不是牛仔裤外套的逐字拼凑，而是牛仔布制的夹克。',
 ('She wore a denim jacket over her dress.','她在裙子外穿了一件牛仔夹克。'),('The bag is made of thick denim.','这个包用厚牛仔布制成。'),sources=S('denim','denim'))
W('satin','英、美 /ˈsætɪn/','缎子，缎面；光滑有光泽的',
 '表面平滑、有光泽，光照上去像顺着布面滑过去，这种缎面感觉就是 satin。现代先认表面和织物类型。',
 '英语借古法语 satin。更远有拉丁 seta 丝的分析，也有阿拉伯语与中国港口名相关的假说，来源有争议，不能把某一条说成定论。',
 [['古法语 satin → 英语 satin','较远来源有丝名分析、地名假说等分歧'],['布料名称 → 缎面、光滑有光泽的形容用法','现代形容表面时，也能用在其他材料、涂层等上']],
 'a satin ribbon 是缎带；a satin dress 是缎面连衣裙；a satin finish 是柔和光滑的缎面效果，具体指什么要看对象。',
 'a satin ribbon；a satin dress；a satin finish。',
 'satin 不直接等于 silk 真丝：缎面织物可用不同纤维制作。若要判断成分，要看实际说明，不能仅凭布面光泽。',
 ('She tied the box with a satin ribbon.','她用一条缎带把盒子系好。'),('The fabric has a smooth satin surface.','这种织物有光滑的缎面。'),sources=S('satin','satin'))
W('tweed','英、美 /twiːd/','粗花呢',
 '常见于外套、夹克，纹理比较明显，颜色像多种线交织在一起的那类粗花呢，叫 tweed。先抓有质感的毛织物画面。',
 '近代英语布料名。较远有接苏格兰语 tweedling、twidling 斜纹织物的缩短分析，也有接 Tweed 河名与相关服装贸易的分析；具体命名存在分歧。',
 [['近代布料、服装贸易中的 tweed 名称','词典对更远命名有不同分析'],['英语 tweed → 粗花呢及相关衣物搭配','现代按布料名称使用，不把流行误读故事当定论']],
 'a tweed jacket 是粗花呢夹克；a tweed coat 是粗花呢外套；made of tweed 是用粗花呢制成。',
 'a tweed jacket；a tweed coat；made of tweed。',
 'tweed 与 wool 关系在于常见材料和织物类别；wool 是纤维、材料的宽泛名称，tweed 指更具体的织物类型。',
 ('He wore a tweed jacket to the lecture.','他穿着粗花呢夹克去听讲座。'),('The coat is made of thick tweed.','这件外套用厚粗花呢制成。'),sources=S('tweed','tweed'))
W('suede','英、美 /sweɪd/','绒面革；绒面革制的',
 '摸上去有一层细细绒感、表面偏哑光的皮革，常叫 suede。先把它和光滑亮面的皮革区分。',
 '借法语 gants de Suède 瑞典手套这个名称中的 Suède，后来用于相应皮革。名称截取地名材料，不表示今天所有 suede 都产自瑞典。',
 [['法语 gants de Suède 瑞典手套','Suède 是法语瑞典的名称'],['名称截短、用途转移 → 英语 suede 绒面革','由相关手套名称转到材料名及材料修饰用法']],
 'suede shoes 是绒面鞋；a suede jacket 是绒面革夹克；made of suede 是用绒面革制成。',
 'suede shoes；a suede jacket；made of suede。',
 'suede 是皮革表面、类型相关的名称，velvet 是天鹅绒织物；二者都可能摸着有绒感，但不是同一种材料。',
 ('She wore a brown suede jacket.','她穿着一件棕色绒面革夹克。'),('The shoes are made of soft suede.','这双鞋用柔软的绒面革制成。'),sources=S('suede','suede'))
W('cashmere','英 /ˈkæʃmɪə/；美 /ˈkæʃmɪr/','山羊绒；羊绒织物',
 '细软的山羊绒，以及用它做的围巾、毛衣，常用 cashmere。它说的是纤维、材料，不只是“很柔软”的泛泛赞美。',
 '接 Cashmere 这个 Kashmir 克什米尔的旧拼写，原有 Cashmere wool 等名称，地名转为纤维、织物名。现代把这个历史地名形式作为普通材料名使用。',
 [['Kashmir 的旧拼写 Cashmere → 相关羊绒、织物名称','地名参与材料命名'],['Cashmere wool 等名称 → cashmere','普通材料名通常小写，现代产地不由旧地名限定']],
 'a cashmere sweater 是羊绒毛衣；a cashmere scarf 是羊绒围巾；cashmere blend 是含羊绒的混纺，具体比例看说明。',
 'a cashmere sweater；a cashmere scarf；cashmere blend。',
 'wool 常说羊毛等宽泛毛纤维，cashmere 特指山羊绒这类材料。柔软的衣服不一定就是 cashmere。',
 ('She wrapped a cashmere scarf around her neck.','她把一条羊绒围巾围在脖子上。'),('The sweater is made from a cashmere blend.','这件毛衣用羊绒混纺材料制成。'),sources=S('cashmere','cashmere'))
W('nylon','英 /ˈnaɪlɒn/；美 /ˈnaɪlɑːn/','尼龙；尼龙制品、面料',
 '背包、绳子、衣物里常见的尼龙，是一类合成材料。nylon 这个名字是人为造出的材料名。',
 '由杜邦为材料造名；常见说明是任意造出的 nyl- + 纤维名常见词尾 -on。不能把 NY、LON 的纽约、伦敦拆法当成有根据的来源。',
 [['新材料命名 → 人为造词 nylon','不是从古典词根逐段正常派生'],['nylon → 合成材料、纤维及材料搭配','又可修饰袋、绳、衣物等制品']],
 'a nylon bag 是尼龙包；nylon rope 是尼龙绳；made of nylon 是用尼龙制成。',
 'a nylon bag；nylon rope；made of nylon。',
 'nylon 是材料名，denim、satin 等更偏具体织物名称；看标签时先分清在说纤维成分还是织物表面、结构。',
 ('The bag is made of lightweight nylon.','这个包用轻质尼龙制成。'),('They used nylon rope to tie the bundle.','他们用尼龙绳把那捆东西扎好。'),sources=S('nylon','nylon'))
W('spandex','英、美 /ˈspændeks/','氨纶，弹性纤维',
 '运动衣、紧身裤拉开后还能收回，常借助 spandex 这类弹性纤维。名字本身就是从“伸展”这个英文动作玩出来的。',
 '把 expands 伸展的字母重新排列，造出 spandex。是字母重排，不按 span、dex 切成两个有固定词义的部分。',
 [['expand → expands 伸展','动作画面是拉长、变大'],['expands 的字母重排 → spandex','用人为造名给弹性纤维命名']],
 'fabric with spandex 是含氨纶的面料；a spandex blend 是氨纶混纺；spandex leggings 是使用这类弹性纤维的紧身裤。',
 'fabric with spandex；a spandex blend；spandex leggings。',
 'spandex 是通用材料名，Lycra 是相关弹性纤维的品牌名；elastane 也是常见对应材料名称，不能把品牌与全部材料一概等同。',
 ('The fabric contains a small amount of spandex.','这种面料含有少量氨纶。'),('She wore leggings made from a spandex blend.','她穿着一条氨纶混纺紧身裤。'),sources=S('spandex','spandex'))
W('khaki','英 /ˈkɑːki/；美 /ˈkæki/','卡其色；卡其布；卡其色的',
 '先想尘土、沙地那种偏黄褐的颜色，再想到同色布料。现代 khaki 可以说颜色，也可以说布，不限定只有军服。',
 '经乌尔都语 khākī 尘土色的材料，接波斯语 khāk 尘土 + 表相关、性质的 -ī。早期衣料、制服背景推动英语用名。',
 [['波斯语 khāk 尘土 + -ī → 尘土色的名称材料','经乌尔都语相关形式传播'],['英语 khaki → 布料名、颜色名及修饰用法','旧制服语境扩展为普通服饰、颜色用语']],
 'a khaki jacket 是卡其色夹克；khaki trousers 是卡其色裤子；made of khaki 可说用卡其布制成。',
 'a khaki jacket；khaki trousers；khaki fabric。',
 '颜色名与布料名要按句子区分；描述一件衣服 khaki，并不能单凭这个词确定纤维成分。',
 ('He wore khaki trousers and a white shirt.','他穿着卡其色裤子和白衬衫。'),('The bag comes in black and khaki.','这个包有黑色和卡其色两种。'),sources=S('khaki','khaki'))
W('fleece','英、美 /fliːs/','羊毛，整片羊毛；绒面织物，抓绒衣；骗取钱财',
 '羊身上一整层毛是 fleece；衣服里常指毛茸茸的绒面材料或抓绒衣；动词则像把人的钱“薅走”，表示骗钱、敲竹杠。',
 '承古英语 flēos 等羊毛、毛皮名，更远来源有不确定处。名词羊毛 → 去毛、剪取羊毛的动作，再比喻剥走钱财；绒面衣料是外观、触感等的现代扩展。',
 [['古英语羊毛名 → fleece','整片羊毛、动物毛层的画面'],['去除羊毛的动作 → fleece 骗钱、敲竹杠','从剥走毛比喻剥走钱'],['绒面、羊毛般触感 → 现代织物、抓绒衣名','不表示每种现代 fleece 面料都由羊毛制成']],
 'a sheep’s fleece 是一只羊的毛；a fleece jacket 是抓绒夹克；fleece someone 是骗走某人的钱。',
 'a sheep’s fleece；a fleece jacket；fleece customers。',
 '现代衣料 fleece 常可用合成纤维制作，来源的羊毛画面不等于眼前材料一定含羊毛；动词的骗钱义则借剥取形象。',
 ('The sheep had a thick fleece.','那只羊有厚厚的一层毛。'),('I put on a fleece before going outside.','出门前我穿上了一件抓绒衣。'),('The dishonest seller tried to fleece his customers.','那个不诚实的卖家想敲顾客的竹杠。'),sources=S('fleece','fleece'))
W('sequin','英 /ˈsiːkwɪn/；美 /ˈsiːkwɪn/','装饰亮片；旧金币名〔历史〕',
 '衣服上缝的一片片会反光的小圆片，单个叫 a sequin。它的名字先和金币有关，后来用来叫像小钱片的装饰物。',
 '经法语 sequin 接意大利语 zecchino 金币名；向前有 zecca 铸币厂、阿拉伯语 sikka 铸币模的材料。由币名转到装饰亮片。',SEQUIN,
 'a silver sequin 是一片银色亮片，不保证材质是真银；a sequin on the dress 是裙子上的一片亮片。',
 'a silver sequin；a loose sequin；a sequin on the dress。',
 '颜色像银币、金币的亮片不一定是金属，更不一定是真金银；旧币名是理解命名的背景。',
 ('A silver sequin fell from the costume.','一片银色亮片从演出服上掉了下来。'),('She sewed a loose sequin back onto the dress.','她把一片松脱的亮片重新缝回裙子上。'),sources=S('sequin','sequin'))
W('sequins','英 /ˈsiːkwɪnz/；美 /ˈsiːkwɪnz/','装饰亮片〔复数〕',
 '舞台衣服上一片片反光的装饰，合起来就是 sequins。光线一动，许多小片就跟着闪。',
 'sequin + -s → sequins，/n/ 后读 /z/，词尾 /nz/。基础词经法语接意大利金币名、铸币材料，后来转为装饰亮片。',SEQUIN+[['sequin + -s → sequins','多片亮片，词尾 /nz/']],
 'covered in sequins 是缀满亮片；gold sequins 是金色亮片；sew on sequins 是缝上亮片。',
 'covered in sequins；gold sequins；sew on sequins。',
 'sequin、sequins 与 sequence 顺序虽然字母相近，来源、意思不同。亮片的词线接旧币名，别套跟随、顺序词根。',
 ('The jacket was covered in sequins.','那件夹克上缀满了亮片。'),('The sequins glittered under the stage lights.','亮片在舞台灯光下闪闪发光。'),sources=S('sequins','sequin'))
W('kimono','英 /kɪˈməʊnəʊ/；美 /kəˈmoʊnoʊ/','和服；和服式衣袍〔按语境〕',
 '想到日式交叠前襟、宽袖、常配腰带的衣袍，英语常叫 kimono。原语言构词很朴素：穿在身上的东西。',
 '借日语 kimono：ki 是 kiru 穿的词干材料，mono 是东西；日语写作着物。英语把整个服饰名借入。',
 [['日语 ki 穿的材料 + mono 东西 → kimono','原构词直观是穿的东西'],['日语服饰名 kimono → 英语 kimono','现代英语可说传统和服，也有和服式款式用法']],
 'a silk kimono 是丝绸和服；wear a kimono 是穿和服；a kimono-style robe 是和服式衣袍，具体设计要看对象。',
 'a silk kimono；wear a kimono；a kimono-style robe。',
 '原构词范围广，现代英语具体服饰名的范围较窄；不能因为字面是穿的东西，就把所有衣服都叫 kimono。',
 ('She wore a silk kimono for the ceremony.','她在仪式上穿了一件丝绸和服。'),('The museum displayed a kimono with a floral pattern.','博物馆展出了一件花卉图案和服。'),sources=S('kimono','kimono'))
W('sari','英、美 /ˈsɑːri/','纱丽，莎丽〔南亚常见缠绕式衣服〕',
 '用一长幅布料在身上围裹、垂搭成衣服，常叫 sari。重点是长布的穿着方式，不是某一种固定纤维。',
 '借印地语 sāṛī，向前通常接中古印度语言的衣物名、梵语 śāṭī 等形式。英语也常拼 saree，整词作为服饰名使用。',
 [['梵语等较早衣物名 → 中古印度语言相关形式','长布、衣物名称在语言中演变'],['印地语 sāṛī → 英语 sari、saree','两种常见拼写，现代说相应缠绕式服饰']],
 'a silk sari 是丝绸纱丽；a cotton sari 是棉纱丽；wear a sari 是穿纱丽。颜色、花纹、材料有多种。',
 'a silk sari；a cotton sari；wear a sari。',
 'sari 是衣服名称，silk、cotton 是材料名；不能只见到长布或某种材质，就忽略实际穿法和服饰类别。',
 ('She chose a blue sari for the celebration.','她为庆祝活动选了一件蓝色纱丽。'),('The sari had a narrow gold border.','那件纱丽有一圈窄窄的金色镶边。'),sources=S('sari','sari'))
def extend_lessons():
 extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_zji',ROOTS,WORDS)
 extend_lessons()
