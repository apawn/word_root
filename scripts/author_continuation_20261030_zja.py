"""Useful short forms in everyday reading, work, shopping and food."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
VEGAN='https://www.vegansociety.com/about-us/history'
def S(word,base):
 a=['https://en.wiktionary.org/wiki/'+word+'#English']
 if base=='merch':a+=['https://www.merriam-webster.com/dictionary/merch','https://www.etymonline.com/word/merchandise']
 else:a.append('https://www.etymonline.com/word/'+base)
 if base=='alum':a+=['https://www.merriam-webster.com/dictionary/alum','https://www.etymonline.com/word/alumnus']
 if base=='vegan':a.append(VEGAN)
 return a
EXISTING_ROOT_ADDITIONS={
 'C0720':dict(words='memo memos'.split(),label='memorandum → memo → memos：记下来别忘的事',note='memo 缩略 memorandum，远接拉丁 memorandum 要记住的事、memor 记得的词族；memos 是现代规则复数，直接加 s。'),
 'C0728':dict(words='merchandise merch'.split(),label='merchandise → merch：商品、周边的短称',note='merch 缩略 merchandise，现代常说音乐人、作品、品牌等周边商品。merchandise 经法语商业、货物词线，较远接拉丁交易、商品词族；缩略没有另造一个 -ch 后缀。'),
 'C0338':dict(words='condo condos'.split(),label='condominium → condo → condos：产权公寓的短称',note='condo 缩略 condominium 的公寓一义，长词最初有共同支配、共同所有的材料，接 com- 一起 + dominium 所有、支配；现代复数 condos 不照搬整个拉丁词尾。'),
 'C0761':dict(words='demo demos'.split(),label='demonstration → demo → demos：演示、样本的短称',note='demo 接 demonstration 展示、示范等的缩略，远处是拉丁 de- 加强与 monstrare 展示的词族；演示、样本义不直接按希腊 demos 人民拆。'),
 'C0769':dict(words='promo promos'.split(),label='promotion → promo → promos：促销宣传的短称',note='promo 缩略 promotion 宣传、推广一义；promotion 远接拉丁 promovere 向前推动。现代不能把 promotion 的职位晋升义全部自动搬给 promo。'),
 'C1485':dict(words='temp temps'.split(),label='temp、temps：临时工作与温度的两个缩略',note='临时人员、临时的 temp 缩 temporary，接时间词族；温度 temp 缩 temperature，后者有拉丁调和、比例的另一段历史。两种长词分别缩短，不由临时雇员演化出温度。'),
 'C1624':dict(words='varsity'.split(),label='university → versity → varsity：大学称呼到校队',note='varsity 是 university 的旧缩略、变体，经 versity 等形式；现代美国学校体育中常用于校队主力级别，中学也能用，不局限于大学。'),
 'C0039':dict(words='alum'.split(),label='alum：alumnus、alumna 的短称；明矾另源',note='校友 alum 缩略 alumnus、alumna，远接拉丁 alere 滋养、培养词族，读 /əˈlʌm/。明矾 alum 另接法语、拉丁 alumen，读 /ˈæləm/，不由校友义演变。'),
 'B3539':dict(words='deli'.split(),label='delicatessen → deli：精美食物到熟食店',note='deli 缩略 delicatessen；长词经德语美食的复数形式、法语精美词线接拉丁 delicatus，与 delicate 远同族。英语店铺名后来按一个店来数，不受德语原复数限制。'),
 'C0451':dict(words='fridge fridges'.split(),label='refrigerator → fridge → fridges：冰箱的短称',note='fridge 缩短、改写 refrigerator，拼写补 d；更远接 refrigerate 使冷却、拉丁冷的词族，品牌可能有影响但不是定论。fridges 直接加 s，/dʒ/ 后增 /ɪz/。'),
 'A1698':dict(words='veggie veggies'.split(),label='vegetable → veggie → veggies：蔬菜的口语称呼',note='veggie 缩短 vegetable 并采用 -ie 等口语名词形式；veggies 直接在已以 ie 结尾的词后加 s，不再多套一遍 y 变 i。这里先学常用的蔬菜义。'),
 'A1692':dict(words='vegan vegans'.split(),label='vegetarian → vegan → vegans：纯素称呼的形成',note='vegan 以 vegetarian 开头三字母、末尾两字母形成，1944 年纯素运动采用这一名称，接着有 veganism 行为理念称呼。vegans 是人群复数，不把植物、食品本身都叫人。'),
}
PROMO=[['拉丁 promovere 向前推动 → promotion 晋升、推进等','现代 promotion 又有宣传推广义'],['promotion 宣传义缩略 → promo → promos','广告、宣传片或促销等语境，不把所有长词意义完整搬来']]
TEMP=[['temporary 临时的、临时人员 → temp；远接时间词族','现代人事语境的简称'],['temperature 温度 → temp','另一个长词的缩略；字形相同，具体指称靠语境判断']]
W('memos','英 /ˈmeməʊz/；美 /ˈmɛmoʊz/','备忘录、简短通知〔复数〕',
 '把要记住、要通知大家的事简短写下来，是 memos。它可以是几份内部通知，也可以是留给自己看的备忘。',
 'memorandum 要记住的事 → 缩略 memo；memo + -s → memos，元音后读 /z/。短称用普通复数，不沿用长词的 memoranda。',
 [['拉丁 memor 记得等 → memorandum 要记住的事','英语借为备忘记录、备忘录'],['memorandum → memo → memos','缩短后给现代名词加规则复数 -s']],
 'office memos 是办公室通知；write memos 是写备忘录；memos to staff 是给员工的简短通知。',
 'office memos；write memos；memos to staff。',
 'memos 是 memo 的复数；memoranda、memorandums 属于完整长词 memorandum 的复数，别把词尾交叉拼接。',
 ('She left two memos on my desk.','她在我桌上留了两份备忘录。'),('The folder contains old memos to staff.','文件夹里存着以前发给员工的简短通知。'),sources=S('memos','memo'))
W('merch','英 /mɜːtʃ/；美 /mɝtʃ/','商品；周边商品〔非正式〕',
 '演出现场卖的乐队 T 恤、海报等，口语常叫 merch。它把长长的“商品”一词缩得很利落。',
 'merchandise 缩略 → merch；merchandise 经法语商业、商品词线，较远接拉丁交易相关材料。现代口语尤其常在品牌、音乐、作品周边语境中出现。',
 [['法语商业、货物词线 → 英语 merchandise','商品名词与 merchant 商人远同族'],['merchandise → merch','日常短称，周边商品是常见现代场景']],
 'band merch 是乐队周边；official merch 是官方周边；a merch stall 是周边商品摊位。',
 'band merch；official merch；a merch stall。',
 'merch 通常按不可数商品整体用，three items of merch 数三件商品；它的词义不限于衣服。',
 ('We bought some band merch after the concert.','演唱会后，我们买了些乐队周边。'),('The merch stall was next to the entrance.','周边商品摊位就在入口旁。'),sources=S('merch','merch'))
W('condos','英 /ˈkɒndəʊz/；美 /ˈkɑndoʊz/','产权公寓、公寓单元〔复数；北美常用短称〕',
 '北美住宅介绍里的 condos，常说一套套可分别拥有的公寓。名字来自长词 condominium，不是某种特殊建材名称。',
 'condominium 的公寓义缩略为 condo；condo + -s → condos，词尾 /z/。长词有一起拥有、支配的历史材料，现代按住房单元等使用。',
 [['近代拉丁 com- 一起 + dominium 所有、支配 → condominium','从共同支配等旧用法，后来用于特定公寓拥有形式'],['condominium → condo → condos','常见北美短称，现代规则复数']],
 'beachfront condos 是海滨公寓；a block of condos 是一栋公寓楼；condos for sale 是待售公寓。',
 'beachfront condos；a block of condos；condos near the station。',
 'apartment 常按住房形态说公寓，condo 往往还带分别拥有单元的含义；不能只凭楼高、装修判断两者。',
 ('Several new condos overlook the harbour.','几套新公寓俯瞰港口。'),('The street has shops below and condos above.','这条街的楼下是商店，楼上是公寓。'),sources=S('condos','condo'))
W('demos','英 /ˈdeməʊz/；美 /ˈdɛmoʊz/','演示；样本、试用版本；样带〔复数〕',
 '软件先给你试一小段，乐队先录几个样本，这些都可能叫 demos：先展示“做出来大概是什么样”。',
 'demonstration 的示范、展示等义缩略为 demo；demo + -s → demos，元音后 /z/。展示一义远接拉丁 demonstrare 指出、展示，不按希腊 demos 人民来拆。',
 [['拉丁展示词族 → demonstration 示范、展示','现代还可用于示威等含展示态度的用法'],['demonstration → demo → demos','样带、试用演示等，具体意思按场景判断']],
 'software demos 是软件演示、试用版本；music demos 是音乐样带；product demos 是产品演示。',
 'software demos；music demos；product demos。',
 'demos 在音乐中可能是录音样本，在软件中可能是可试用内容；不是每次都要译成现场表演。',
 ('The band recorded three demos in a small studio.','乐队在一个小录音室录了三首样带。'),('The website offers short demos of the software.','网站提供这款软件的简短演示。'),sources=S('demos','demo'))
W('promo','英 /ˈprəʊməʊ/；美 /ˈproʊmoʊ/','宣传片、推广广告；促销活动〔非正式短称〕',
 '节目开播前的一小段宣传视频，或商家的一次促销，常被叫 a promo。短词抓的是推广、吸引注意这一义。',
 'promotion 宣传、推广一义缩略 → promo；更远接拉丁 promovere 向前推动。长词也有职位晋升义，但不能因此把升职通知一概说成 a promo。',PROMO,
 'a TV promo 是电视宣传片；a promo video 是宣传视频；a promo code 是促销代码。',
 'a TV promo；a promo video；a promo code。',
 'promo 作前部修饰时常表示 promotional 宣传、促销的关系；a promo 单独作名词时则依场景指宣传片、推广活动等。',
 ('The channel released a short promo for the series.','频道发布了这部剧的一段简短宣传片。'),('The shop is running a weekend promo.','商店正在举办周末促销。'),sources=S('promo','promo'))
W('promos','英 /ˈprəʊməʊz/；美 /ˈproʊmoʊz/','宣传片、推广广告、促销活动〔复数〕',
 '几条宣传视频、几次促销，可以说 promos。短称变成完整名词以后，复数直接加 s。',
 'promo + -s → promos，元音后读 /z/；来自 promotion 的宣传推广义，不是把全部意义都收进同一个缩略词。',PROMO+[['promo + -s → promos','多条宣传片、多个促销等，词尾 /z/']],
 'TV promos 是电视宣传片；weekend promos 是周末促销活动；new promos 是新的宣传内容。',
 'TV promos；weekend promos；new promos。',
 'promos 与 demos 常同时出现：promos 主要用来宣传推广，demos 主要展示、供试听试用，功能可有重叠。',
 ('The station played promos for its new programmes.','电台播放了新节目的宣传片段。'),('The website lists the latest promos from local shops.','网站列出了本地商店最新的促销活动。'),sources=S('promos','promo'))
W('temp','英、美 /temp/','临时员工；临时的；温度〔不同长词的短称〕',
 '公司说 hire a temp，是找个临时员工；天气记录说 the temp，则可能是温度。相同短词，要先找回不同长词。',
 'temporary 临时的、临时人员 → temp；temperature 温度 → temp。前者有时间词族背景，后者有调和、冷热比例等历史，不能把两条现代缩略混成一个意义发展。',TEMP,
 'hire a temp 是雇临时员工；a temp job 是临时工作；the room temp 是室温的短写、短称。也可见 temp 作做临时工作的动词。',
 'hire a temp；a temp job；room temp。',
 '写正式技术数据时 temperature 更明确；人事语境里的 a temp 通常按一个员工来数，不能当温度读。',
 ('The office hired a temp for the summer.','办公室雇了一位暑期临时员工。'),('The room temp was higher than expected.','室温比预想的高。'),sources=S('temp','temp'))
W('temps','英、美 /temps/','临时员工〔复数〕；温度数值〔复数短称〕',
 '办公室新来几个临时员工，是 temps；天气预报里几天、几处的温度，也能缩写成 temps。',
 'temp + -s → temps，/p/ 后读 /s/；分别对应 temporary 人员名词和 temperature 温度名词的复数短称。',TEMP+[['temp + -s → temps','数人员或温度数值，按场景还原']],
 'office temps 是办公室临时员工；daytime temps 是白天温度；low temps 是低温。',
 'office temps；daytime temps；low temps。',
 'temps 不一定是几个人；看到 daytime、nighttime 等天气修饰，通常应还原 temperatures。',
 ('The company hired three temps during the busy season.','旺季时，公司雇了三位临时员工。'),('Daytime temps stayed low all week.','整周白天气温都很低。'),sources=S('temps','temp'))
W('varsity','英 /ˈvɑːsəti/；美 /ˈvɑrsəti/','校队、校队主力级别的；大学的〔旧短称等语境〕',
 '美国校园里 varsity team 通常是代表学校、较高竞赛级别的校队。这个体育词，远处其实缩自 university。',
 'university 大学 → 旧缩略 versity → 变体 varsity；后来学校体育中用于主力级别代表队，中学也能用。不是 varied 变化多的加 -ity 造出来。',
 [['university → 旧缩略 versity → varsity','英语长词缩短，并有元音、拼写的变化'],['大学相关称呼 → 学校体育中的校队级别用法','现代美国高中也可用 varsity，范围不限大学']],
 'a varsity team 是校队主力级别队伍；varsity basketball 是这一等级篮球；a varsity jacket 是常与校队文化相连的夹克。',
 'a varsity team；varsity basketball；a varsity jacket。',
 'junior varsity 通常是较低一级、培养性的队伍称呼；varsity 的核心是学校竞赛等级，不单纯等于年龄大。',
 ('She plays on the varsity basketball team.','她在学校篮球主力队打球。'),('He wore a varsity jacket to the reunion.','他穿着校队风格夹克参加聚会。'),sources=S('varsity','varsity'))
W('alum','校友：英、美 /əˈlʌm/；明矾：英、美 /ˈæləm/','校友〔非正式短称〕；明矾〔另源、读音不同〕',
 '介绍人说 an alum，是校友；化学瓶上标 alum，可能是明矾。两个词同拼写，重音却不在同一处。',
 '校友 alum 缩略 alumnus、alumna，远接拉丁 alere 滋养、培养词族；明矾 alum 则接古法语、拉丁 alumen。前者后重 /əˈlʌm/，后者前重 /ˈæləm/。',
 [['拉丁 alere 滋养 → alumnus 门生、受养者 → 英语校友称呼','alumnus、alumna 缩略为 alum，不限定男性或女性'],['另源：拉丁 alumen → 法语、英语 alum 明矾','同拼写但不同词源、重音，不是校友变成化学物质']],
 'a university alum 是大学校友；an alum of this school 是这所学校的校友；化学、染色等语境里的 alum 另看明矾义。',
 'a university alum；an alum of the school；a jar labelled alum。',
 '校友 alum 的普通复数是 alums；完整 alumnus、alumna 又分别有 alumni、alumnae 等传统形式。先看使用的是长词还是短词。',
 ('She is an alum of this university.','她是这所大学的校友。'),('The jar on the shelf was labelled “alum”.','架子上的罐子标着“明矾”。'),sources=S('alum','alum'))
W('deli','英、美 /ˈdeli/','熟食店；熟食柜台',
 '想买三明治、冷切肉、奶酪等现成食物，常会去 a deli。商场里一块专卖熟食的柜台也能这样叫。',
 'delicatessen 缩略 → deli；长词经德语精美食物的复数形式，向前接法语、拉丁的精美、可口词族。英语从食物转称售卖它们的店，再形成短称。',
 [['拉丁 delicatus 精美等 → 法语、德语美食称呼 → 英语 delicatessen','德语原形式有复数背景，英语后来也用作一个店的名称'],['delicatessen → deli','熟食店、熟食柜台的日常短称']],
 'a local deli 是附近熟食店；a deli counter 是熟食柜台；a deli sandwich 是熟食店式三明治。',
 'a local deli；a deli counter；a deli sandwich。',
 'deli 名称虽由旧复数形式缩来，现代英语仍可说 a deli；不用把词源中的德语复数硬套到每次点单。',
 ('I bought a sandwich at the deli on the corner.','我在街角的熟食店买了一个三明治。'),('There was a queue at the supermarket deli.','超市的熟食柜台前排着队。'),sources=S('deli','deli'))
W('fridges','英、美 /ˈfrɪdʒɪz/','冰箱〔复数〕',
 '两台冰箱，是 two fridges。短词看着比 refrigerator 多了一个 d，是缩短后调整过的拼写。',
 'refrigerator 缩短、改写 → fridge；fridge + -s → fridges。基础词已经以 e 结尾，直接加 s，/dʒ/ 后后缀读 /ɪz/。',
 [['refrigerator → fridge','短称拼写补 d；可用 bridge、ridge 的字母外观帮助记音'],['fridge + -s → fridges','多台冰箱，增加复数 /ɪz/ 音节']],
 'small fridges 是小冰箱；fridges and freezers 是冰箱与冷冻柜；fridges in hotel rooms 是酒店客房中的冰箱。',
 'small fridges；fridges and freezers；two fridges。',
 'fridge 通常说冷藏用途的冰箱，freezer 强调冷冻；家用一台设备可能两种功能都有，词的重点仍不同。',
 ('The shop sells fridges and washing machines.','这家商店卖冰箱和洗衣机。'),('The small fridges fit under the counters.','这些小冰箱能放在操作台下方。'),sources=S('fridges','fridge'))
W('veggies','英、美 /ˈvedʒiz/','蔬菜〔口语复数〕',
 '饭桌上说多来点菜，口语可以说 more veggies。比 vegetables 短，也更随意。',
 'vegetable 缩短后形成口语名词 veggie，采用 -ie 形式，另有 vegie 拼写；veggie + -s → veggies，原 /i/ 后接 /z/。',
 [['vegetable → veggie、vegie','截短并用口语名词形式表达蔬菜'],['veggie + -s → veggies','基础词以 ie 结尾，直接加 s，不再改一遍 y']],
 'fresh veggies 是新鲜蔬菜；roasted veggies 是烤蔬菜；fruit and veggies 是水果和蔬菜的口语说法。',
 'fresh veggies；roasted veggies；fruit and veggies。',
 '这里的 veggies 数蔬菜、谈菜肴；vegetarian、vegan 是人物、饮食方式相关称呼，不能看到同样 veg 开头就全部译成蔬菜。',
 ('The soup is full of fresh veggies.','汤里放了很多新鲜蔬菜。'),('We served roasted veggies with the rice.','我们用烤蔬菜配米饭。'),sources=S('veggies','veggie'))
W('vegans','英、美 /ˈviːɡənz/','纯素者〔复数〕',
 'vegans 在饮食上不只避开肉，也避开蛋、奶等动物来源食物；相关生活理念往往还涉及衣物等动物使用。',
 'vegan 在 1944 年形成，以 vegetarian 开头三字母 veg 与末尾两字母 an 组合；vegan + -s → vegans，/n/ 后读 /z/。这个现代造词也连接到后来的 veganism。',
 [['vegetarian 的开头 veg 与末尾 an → vegan','纯素运动采用的新名称，相关组织保存了命名史'],['vegan + -s → vegans','多名纯素者；veganism 另说理念、生活方式']],
 'food for vegans 是适合纯素者的食物；vegans and vegetarians 是纯素者与其他素食者的常见并称。',
 'food for vegans；suitable for vegans；vegans and vegetarians。',
 'vegetarians 通常不吃肉、鱼，部分仍吃奶蛋；vegans 的排除范围进一步包括这些动物来源食物。vegans 是人，vegan food 是纯素食物。',
 ('The café has several options for vegans.','这家咖啡馆为纯素者提供了几种选择。'),('Two of our guests are vegans.','我们的客人中有两位纯素者。'),sources=S('vegans','vegan'))
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_zja',ROOTS,WORDS)
 extend_lessons()
