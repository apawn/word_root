"""Everyday measurement families: decimal scales, data sizes and named units."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
SI='https://www.bipm.org/documents/20126/41483022/SI-Brochure-9-EN.pdf/2d2b50bf-f2b4-9661-f402-5f9d66e4b507?download=true&t=1780410776583&version=7.0'
PREFIX='https://www.nist.gov/pml/owm/metric-si-prefixes'
BINARY='https://physics.nist.gov/cuu/Units/binary.html'
IEC='https://styleguide.iec.ch/?docs=iec%2Ftypographic%2Funits-and-symbols'
def S(word,base,extra=None):
 return ['https://en.wiktionary.org/wiki/'+word+'#English','https://www.etymonline.com/word/'+base,PREFIX]+(extra or [])
EXISTING_ROOT_ADDITIONS={
 'C0733':dict(words='millimetres millimeters centimetres centimeters kilometres kilometers nanometers micrometers'.split(),label='米的单位家族：把一米分小，或按千倍放大',note='长度单位中的 metre、meter 接法语 mètre、希腊 metron 测量；英美拼写差别不改变大小。millimetres、centimetres、kilometres 与对应美式复数相邻。micrometers 另有测量仪复数，词义与重音分别说明。'),
 'A1688':dict(words='millimetres millimeters milliseconds'.split(),label='milli-：一千份里的一份',note='milli- 远接拉丁 mille 千；现代单位名前固定表示千分之一，毫米与毫秒分别把米、秒分成一千份。复数只给整个单位名加 -s。'),
 'A1684':dict(words='centimetres centimeters'.split(),label='centi-：一百份里的一份',note='centi- 接拉丁 centum 百，公制单位里约定为百分之一；英美厘米复数拼写相邻，两个名称表示相同长度。'),
 'C0633':dict(words='kilometres kilometers kilobytes kilowatts'.split(),label='kilo-：千米、千字节、千瓦',note='kilo- 远接希腊千，现代十进制单位固定为一千倍。计算机字节单位另讲历史二进制口径，不能把所有 kilo- 一概改成 1024。'),
 'C1317':dict(words='milliseconds microseconds nanoseconds'.split(),label='同一秒的不同细分：毫秒、微秒、纳秒',note='second 秒的名称有第二次细分小份的历史背景；milli-、micro-、nano- 分别把秒缩为千分之一、百万分之一、十亿分之一。学习时按尺度比较，不表示一个单词由另一个单词演化。'),
 'A1701':dict(words='microseconds micrograms micrometers'.split(),label='micro-：百万分之一的单位，与测微仪的另一构词线',note='micro- 远接希腊 mikros 小；现代微秒、微克、微米中约定百万分之一。micrometers 也可指多把测微仪，-meter 是仪器构词成分，另有重音。'),
 'A1689':dict(words='nanoseconds nanometers'.split(),label='nano-：十亿份里的一份',note='nano- 接希腊 nanos 小个子、侏儒的材料，现代单位前表示十亿分之一；纳秒和纳米分别是时间、长度，不因共用 nano- 而变成同一种量。'),
 'B3141':dict(words='micrograms'.split(),label='microgram → micrograms：微克',note='micro- 百万分之一 + gram 克；gram 经法语 gramme，远接希腊 gramma 小重量的用法。微克不是毫克，后者要大一千倍。'),
 'A1700':dict(words='megabytes'.split(),label='mega- + byte → megabyte → megabytes',note='mega- 远接希腊大，在十进制数据单位中表示百万；历史软件也可能采用二进制含义，精确时核对 MB、MiB。'),
 'C0714':dict(words='megabytes'.split(),label='大到百万倍：megabytes 的数据容量用法',note='希腊 megas 大的材料进入 mega-；现代十进制 MB 是百万字节。它与 megawatt 共享前缀，不共享字节和功率这两个单位。'),
 'A1687':dict(words='gigabytes'.split(),label='giga-：从巨人的词源材料到十亿倍',note='giga- 名称接希腊 gigas 巨人，在现代十进制 GB 中表示十亿倍。GiB 则明确表示二进制量，不能把二者拼写差别当装饰。'),
 'A1690':dict(words='terabytes'.split(),label='tera-：从巨物的名称材料到万亿倍',note='tera- 接希腊 teras 奇物、巨物、怪物等材料，现代十进制 TB 表示万亿字节；学习倍率按现代约定，旧词义只帮助记住大尺度。'),
 'B3368':dict(words='kilowatts joule joules'.split(),label='千瓦和焦耳：做功有多快，与总共多少能量',note='kilowatt 是功率单位，watt 以 James Watt 命名；joule、joules 是能量、功单位，以 James Prescott Joule 命名。两条人名来源不同，这里放在一起对照功率与能量，不把 joule 当 watt 的派生词。'),
 'A1685':dict(words='decibels'.split(),label='deci- + bel → decibel → decibels',note='deci- 表十分之一，接拉丁十的材料；bel 以 Alexander Graham Bell 命名。分贝是一种对数比值单位，不能把数字倍数直接当成声音强度倍数。'),
 'C0736':dict(words='micrometers'.split(),label='micrometer 的单位与仪器两条线',note='micro- 小的材料既进入百万分之一米的单位名，也进入测小距离的仪器名；美式 micrometers 可同形，重音与上下文区分。'),
 'A1974':dict(words='micrometers'.split(),label='-meter 测量仪：micrometers 的仪器义',note='仪器线的 micro- 小 + -meter 测量仪构成测微仪；同形的微米单位中 meter 是米。共享测量材料，不把单位与工具说成同一东西。'),
}
MM=[['拉丁 mille 千 → 法语公制 milli- 千分之一','单位前缀的现代约定，不把千直接译成一千米'],['法语 millimètre → 英语 millimetre／millimeter → 复数','milli- + metre／meter；米的千分之一']]
CM=[['拉丁 centum 百 → 法语公制 centi- 百分之一','一米等分一百份，每份一厘米'],['法语 centimètre → 英语 centimetre／centimeter → 复数','英美常见拼写不同，长度相同']]
KM=[['希腊 khilioi 千 → 法语公制 kilo-','现代单位前表示一千倍'],['法语 kilomètre → 英语 kilometre／kilometer → 复数','一千米组成一公里']]
W('millimetres','英 /ˈmɪlɪmiːtəz/','毫米〔英式复数〕',
 '尺子上相邻两条最细刻线常隔一毫米。把一米分成一千份，每份就是一个 millimetre；这里说若干份。',
 'milli- 千分之一 + metre 米 → millimetre，再加复数 -s → millimetres；词尾读 /z/。',MM,
 '量一块薄板的厚度、两处细小间距，常用 millimetres。10 millimetres 是一厘米，1000 millimetres 是一米。',
 'three millimetres thick；a gap of two millimetres；measure in millimetres。',
 'millimetres 与美式 millimeters 是同一单位；单位符号 mm 不因复数加 s。',
 ('The board is six millimetres thick.','这块板厚六毫米。'),('Leave a gap of two millimetres between the pieces.','两块材料之间留两毫米的缝。'),sources=S('millimetres','milligram',[SI]))
W('millimeters','美 /ˈmɪlɪˌmiːtɚz/','毫米〔美式复数〕',
 '螺丝直径、薄片厚度，往往小到需要用毫米数。millimeters 是这些小长度单位的美式写法。',
 'millimeter + -s → millimeters，词尾读 /z/；millimeter 是 millimetre 的美式拼写，milli- 表千分之一。',MM,
 'a few millimeters 是几毫米；in millimeters 说明读数用毫米标。小单位表示得细，不等于仪器本身就一定测得准。',
 'a few millimeters；five millimeters wide；measurements in millimeters。',
 '10 millimeters = 1 centimeter；改用 centimeters 后数字要随换算变化，不能只换词。',
 ('The hole is eight millimeters wide.','这个孔宽八毫米。'),('The drawing gives all measurements in millimeters.','图上的所有尺寸都用毫米表示。'),sources=S('millimeters','milligram',[SI]))
W('centimetres','英 /ˈsentɪmiːtəz/','厘米〔英式复数〕',
 '一把三十厘米长的直尺，就是 thirty centimetres。把一米分成一百份，厘米是其中一份。',
 'centi- 百分之一 + metre 米 → centimetre，再加复数 -s → centimetres；词尾读 /z/。',CM,
 '身高、书本宽度、小盒子尺寸都常用 centimetres。100 centimetres 是一米，1 centimetre 是10毫米。',
 'thirty centimetres long；a few centimetres；height in centimetres。',
 'centi- 的远源是百；在这个计量名里取百分之一，不能见到百就理解成一百米。',
 ('The shelf is eighty centimetres wide.','这个架子宽八十厘米。'),('Please write your height in centimetres.','请用厘米填写你的身高。'),sources=S('centimetres','centi-',[SI]))
W('centimeters','美 /ˈsentɪˌmiːtɚz/','厘米〔美式复数〕',
 '量一下照片宽多少、植物长高多少，用 centimeters 就很方便。它与英式 centimetres 没有大小差别。',
 'centimeter + -s → centimeters，词尾 /z/；centi- 百分之一 + meter 米，是同一单位的美式拼写。',CM,
 'ten centimeters 是十厘米；a few centimeters taller 是高几厘米；square centimeters 说面积，已经不是单纯长度。',
 'ten centimeters；a few centimeters taller；measure in centimeters。',
 'centimeters 表长度，square centimeters 表平方厘米。量的种类由完整搭配决定。',
 ('The plant grew three centimeters this week.','这株植物这周长高了三厘米。'),('Cut a strip twenty centimeters long.','剪一条二十厘米长的带子。'),sources=S('centimeters','centi-',[SI]))
W('kilometres','英 /kɪˈlɒmɪtəz/，也读 /ˈkɪləmiːtəz/','千米，公里〔英式复数〕',
 '城镇之间、跑步路线的距离，可以把一千米打成一个大单位来数：kilometres。五公里就是五个一千米。',
 'kilo- 一千倍 + metre 米 → kilometre；kilometre + -s → kilometres，词尾 /z/。',KM,
 'ten kilometres away 是十公里外；kilometres per hour 表速度；walk five kilometres 是走五公里。',
 'a few kilometres away；kilometres per hour；walk five kilometres。',
 'kilometres 是英式常见拼写。读音有两种常见重音，不能只照独立名词 kilo 的重音机械拼读。',
 ('The village is five kilometres from here.','那个村子离这里五公里。'),('We walked twelve kilometres along the coast.','我们沿着海岸走了十二公里。'),sources=S('kilometres','kilo',[SI]))
W('kilometers','美 /kɪˈlɑːmɪtɚz/，也读 /ˈkɪləˌmiːtɚz/','千米，公里〔美式复数〕',
 '地图上说 two kilometers，是两公里，也就是两千米。换成美式拼写后，距离没有变。',
 'kilometer + -s → kilometers，词尾 /z/；kilo- 千 + meter 米，基础单位名与英式 kilometre 对应。',KM,
 'several kilometers 是几公里；kilometers from the station 是离车站多少公里；kilometers per hour 说明每小时走多远。',
 'several kilometers；two kilometers from the station；kilometers per hour。',
 'kilometers 和 miles 都能计距离，但数值不能直接照搬；kilometres 与 kilometers 才是同一单位的不同拼写。',
 ('The hotel is two kilometers from the station.','旅馆离车站两公里。'),('The route covers thirty kilometers.','这条路线全长三十公里。'),sources=S('kilometers','kilo',[SI]))
W('milliseconds','英 /ˈmɪlɪˌsekəndz/；美 /ˈmɪlɪˌsɛkəndz/','毫秒',
 '把一秒分成一千格，一格就是一毫秒。屏幕响应、程序延迟，常用 milliseconds 来量这种很短的等待。',
 'milli- 千分之一 + second 秒 → millisecond，再加 -s → milliseconds；/d/ 后的 -s 读 /z/，词尾 /ndz/。',
 [['拉丁 mille 千 → 现代 milli- 千分之一','与 second 秒组合，得到更细的时间单位'],['millisecond + -s → milliseconds','1000 milliseconds = 1 second']],
 'a delay of twenty milliseconds 是二十毫秒延迟；in milliseconds 表示用毫秒计。重点是时间很短，不是“一千秒”。',
 'a few milliseconds；a delay of twenty milliseconds；measured in milliseconds。',
 '1 millisecond = 1000 microseconds。milli- 与 micro- 看着都很小，数量级却差一千倍。',
 ('The screen responded within twenty milliseconds.','屏幕在二十毫秒内作出了响应。'),('The delay is measured in milliseconds.','这段延迟以毫秒计。'),sources=S('milliseconds','milligram',[SI]))
W('microseconds','英 /ˈmaɪkrəʊˌsekəndz/；美 /ˈmaɪkroʊˌsɛkəndz/','微秒',
 '一秒切成一百万份，每一份才是一微秒。它适合描述电子信号、快速计算里非常短的时间。',
 'micro- 百万分之一 + second 秒 → microsecond；加复数 -s → microseconds，词尾 /ndz/。micro- 远接希腊 mikros 小。',
 [['希腊 mikros 小 → 计量 micro- 百万分之一','小的材料被赋予明确倍率'],['microsecond + -s → microseconds','1000000 microseconds = 1 second']],
 'a few microseconds 是几微秒；每一微秒都是一百万分之一秒。机器快的场景用它，普通约会时间不用这么细。',
 'a few microseconds；a delay of five microseconds；timing in microseconds。',
 '一毫秒包含一千微秒；一微秒又包含一千纳秒。按单位大小排是毫秒、微秒、纳秒。',
 ('The two signals arrived five microseconds apart.','两个信号到达的时间相差五微秒。'),('The table records each delay in microseconds.','表格用微秒记录每次延迟。'),sources=S('microseconds','micrometer',[SI]))
W('nanoseconds','英 /ˈnænəʊˌsekəndz/；美 /ˈnænoʊˌsɛkəndz/','纳秒；极短的一瞬间〔夸张〕',
 '一纳秒只有十亿分之一秒。技术文章真在计时；日常说 in nanoseconds，也可能只是在夸张“快得几乎没间隔”。',
 'nano- 十亿分之一 + second 秒 → nanosecond；加 -s → nanoseconds，词尾 /ndz/。nano- 名称远接希腊 nanos 小个子的材料。',
 [['希腊 nanos 小个子 → 科学 nano- 十亿分之一','旧词义帮助记住微小，精确倍率由现代约定'],['nanosecond + -s → nanoseconds','技术计时，也可夸张说极短时间']],
 'measured in nanoseconds 是以纳秒测量；felt like nanoseconds 是主观觉得一瞬间。写科学结果时按精确数值理解。',
 'a few nanoseconds；a delay of ten nanoseconds；in nanoseconds。',
 '这里 nano- 精确表示十亿分之一；宣传里泛泛说 nano 的“小”，不能直接充当一项测量结果。',
 ('The instrument measures delays in nanoseconds.','这台仪器用纳秒测量延迟。'),('The tickets seemed to disappear in nanoseconds.','那些票好像一瞬间就没了。'),sources=S('nanoseconds','nano-',[SI]))
W('micrograms','英 /ˈmaɪkrəʊɡræmz/；美 /ˈmaɪkroʊɡræmz/','微克',
 '把一克分成一百万份，每份是一微克。实验里极少量的物质，质量小到常需要用 micrograms 来数。',
 'micro- 百万分之一 + gram 克 → microgram；加复数 -s → micrograms，/m/ 后读 /z/。gram 经法语 gramme，远接希腊小重量的名称。',
 [['希腊 mikros 小、gramma 小重量的材料 → 现代单位组合','micro- 在单位前取百万分之一'],['microgram + -s → micrograms','1000000 micrograms = 1 gram']],
 'a few micrograms 是几微克；a mass of ten micrograms 是十微克的质量。这里在说物质量有多小，不是在说长度。',
 'a few micrograms；ten micrograms of material；mass in micrograms。',
 '1000 micrograms = 1 milligram。微克与毫克不是两种拼法，换算差一千倍。',
 ('The sample contained only a few micrograms of dust.','这个样品里只有几微克灰尘。'),('The table lists each mass in micrograms.','表格以微克列出每项质量。'),sources=S('micrograms','micrometer',[SI,'https://www.etymonline.com/word/gram']))
W('kilobytes','英 /ˈkɪləbaɪts/；美 /ˈkɪləˌbaɪts/','千字节；历史计算机用法也可按1024字节计',
 '短小的文字文件，大小可能只有几个 kilobytes。先抓住“一组组字节在计文件大小”，再看软件采用哪种换算。',
 'kilo- 千 + byte 字节 → kilobyte；kilobyte + -s → kilobytes，/t/ 后读 /s/，词尾 /ts/。这是现代计算机单位组合。',
 [['希腊千的材料 → kilo-；现代计算机单位 byte','单位名前缀与字节名相接'],['kilobyte + -s → kilobytes','十进制每单位1000字节；历史用法也有1024字节口径']],
 'a file of a few kilobytes 是几千字节的小文件。kB 按十进制，KiB 明确按1024字节；遇到旧资料写 KB，要看它的口径。',
 'a few kilobytes；file size in kilobytes；save several kilobytes。',
 'byte 字节与 bit 比特是不同单位；符号大小写和计数口径都要看清，不能只盯着 kilo-。',
 ('The text file is only a few kilobytes in size.','这个文本文件只有几千字节大。'),('The table lists file sizes in kilobytes.','表格用千字节列出文件大小。'),sources=S('kilobytes','kilo-',[BINARY,IEC,'https://www.etymonline.com/word/byte']))
W('megabytes','英 /ˈmeɡəbaɪts/；美 /ˈmɛɡəˌbaɪts/','兆字节；十进制每单位一百万字节',
 '一张照片、一份带图片的文档，大小常用 megabytes 来说。它把很多字节合成一个较大的计数单位。',
 'mega- 百万 + byte 字节 → megabyte；加复数 -s → megabytes，词尾 /ts/。mega- 远接希腊 megas 大。',
 [['希腊 megas 大 → 现代计量 mega- 百万倍','大是词源画面，百万是现代倍率'],['megabyte + -s → megabytes','十进制 MB；历史计算机用法有二进制口径']],
 'ten megabytes 是十兆字节。规范十进制 MB 每个一百万字节；明确二进制时用 MiB，旧软件的 MB 可能采用后者口径。',
 'a few megabytes；several megabytes of data；size in megabytes。',
 'megabytes 说数据量，megabytes per second 才说每秒传多少。别把文件多大和传得多快混在一起。',
 ('The photo takes up several megabytes.','这张照片占了几兆字节空间。'),('The app shows the download size in megabytes.','这个应用用兆字节显示下载大小。'),sources=S('megabytes','mega-',[BINARY,IEC,'https://www.etymonline.com/word/byte']))
W('gigabytes','英 /ˈɡɪɡəbaɪts/；美 /ˈɡɪɡəˌbaɪts/','吉字节；十进制每单位十亿字节〔日常常说G〕',
 '手机还剩多少空间、视频占了多少容量，常用 gigabytes。把字节成十亿地计，就能用较小数字说很大的数据量。',
 'giga- 十亿 + byte 字节 → gigabyte；加复数 -s → gigabytes，词尾 /ts/。giga- 的命名材料接希腊 gigas 巨人。',
 [['希腊 gigas 巨人 → 计量 giga- 十亿倍','现代倍率有严格约定'],['gigabyte + -s → gigabytes','十进制 GB；与明确二进制的 GiB 区分']],
 'several gigabytes of video 是几吉字节的视频；free gigabytes 是可用空间。十进制 GB 为十亿字节，GiB 为2的30次方字节，旧显示可能混称。',
 'several gigabytes of video；free space in gigabytes；a few gigabytes left。',
 '同一堆数据换用 GB、GiB 显示，数字可以不同；不能仅凭数字变小就判断数据丢失。',
 ('The videos take up several gigabytes.','这些视频占了几吉字节空间。'),('I still have twenty gigabytes of free space.','我还有二十吉字节的可用空间。'),sources=S('gigabytes','giga-',[BINARY,IEC,'https://www.etymonline.com/word/byte']))
W('terabytes','英 /ˈterəbaɪts/；美 /ˈterəˌbaɪts/','太字节；十进制每单位一万亿字节〔日常常说T〕',
 '大量视频、照片和备份堆在一起，容量可能要按 terabytes 来数。它比 gigabytes 又放大了一层。',
 'tera- 万亿 + byte 字节 → terabyte；加复数 -s → terabytes，词尾 /ts/。tera- 名称远接希腊 teras 奇物、巨物、怪物的材料。',
 [['希腊 teras 奇物、巨物等 → 现代 tera- 万亿倍','取大尺度的命名材料，不按旧词义计算容量'],['terabyte + -s → terabytes','十进制 TB；二进制可明确写 TiB']],
 '十进制下1000 gigabytes = 1 terabyte；TB 是10的12次方字节，TiB 是2的40次方字节，精确比较容量时先统一口径。',
 'several terabytes of data；capacity in terabytes；terabytes of backups。',
 '容量、已有数据量、剩余空间都能用 terabytes；名词前后的搭配告诉你到底在数哪一项。',
 ('The archive contains several terabytes of video.','这个档案库里有几太字节的视频。'),('The report lists storage capacity in terabytes.','报告用太字节列出存储容量。'),sources=S('terabytes','tera-',[BINARY,IEC,'https://www.etymonline.com/word/byte']))
W('kilowatts','英 /ˈkɪləwɒts/；美 /ˈkɪləˌwɑːts/','千瓦〔功率单位〕',
 '设备一秒能转化多少能量，可以用功率来描述。kilowatts 是把瓦放大一千倍来计的单位，像把做事速度调到更大的刻度。',
 'kilo- 千 + watt 瓦 → kilowatt；加复数 -s → kilowatts，词尾 /ts/。watt 是用 James Watt 的姓命名的单位。',
 [['希腊千的材料 → kilo-；James Watt 姓名 → watt','单位名由数量前缀和人名单位组合'],['kilowatt + -s → kilowatts','1 kilowatt = 1000 watts']],
 'a rated power of two kilowatts 是额定功率两千瓦；power in kilowatts 是用千瓦表示功率。',
 'two kilowatts；rated power in kilowatts；an output of five kilowatts。',
 'kilowatts 是功率，kilowatt-hours 是能量；持续多久会影响总能量，不能把千瓦数直接当作累计电量。',
 ('The heater is rated at two kilowatts.','这台加热器的额定功率是两千瓦。'),('The display shows the output in kilowatts.','显示屏用千瓦显示输出功率。'),sources=S('kilowatts','kilo-',[SI,'https://www.etymonline.com/word/megawatt']))
W('decibels','英 /ˈdesɪbelz/；美 /ˈdesəˌbɛlz/','分贝〔对数比值单位，常用于声级〕',
 '测声音大小时，仪表常显示多少分贝。这个刻度把很大的比值压到便于表示的数字上，所以它不是普通尺子那样的直线刻度。',
 'deci- 十分之一 + bel 贝 → decibel；加复数 -s → decibels，/l/ 后读 /z/。bel 以 Alexander Graham Bell 的姓命名。',
 [['拉丁 decimus 第十的材料 → deci- 十分之一；Bell 姓名 → bel','这里是单位名字的组合'],['decibel + -s → decibels','一个 decibel 为十分之一 bel，用于特定对数比值']],
 'a level in decibels 是用分贝表示的声级、信号电平等。读技术结果时，还要看在测什么、以什么为参考。',
 'a level in decibels；measured in decibels；a change of five decibels。',
 '分贝数字加倍，不表示声音强度或主观响度就简单加倍；具体比较取决于量和参考值。',
 ('The meter shows the sound level in decibels.','这台仪表用分贝显示声级。'),('The chart compares levels measured in decibels.','这张图比较了用分贝测得的级值。'),sources=S('decibels','decibel',[SI]))
JOULE=[['物理学家 James Prescott Joule 的姓 → 单位名 joule','以人名命名能量、功的单位'],['英语 joule → 复数 joules','符号 J；名称小写，通常读作与 jewel 同音']]
W('joule','英、美 /dʒuːl/，也读 /dʒaʊl/','焦耳〔能量、功的单位〕',
 '弹簧里储了多少能量，或推动物体做了多少功，可以用 joule 来计。先抓“总共多少能量”这个问题。',
 '以物理学家 James Prescott Joule 的姓命名；现代单位名 joule 作为整词借用人名，不需要硬拆英语前后缀。',JOULE,
 'one joule 是一焦耳；a unit of energy 是一种能量单位。名称通常小写 joule，符号写大写 J。',
 'one joule；a joule of energy；the joule as a unit。',
 'watt 问能量转化得多快，joule 问能量有多少。1 watt = 1 joule per second，二者由时间联系起来。',
 ('The joule is a unit of energy.','焦耳是一种能量单位。'),('In this example, the spring stores one joule of energy.','在这个例子中，弹簧储存了一焦耳能量。'),sources=S('joule','joule',[SI]))
W('joules','英、美 /dʒuːlz/，也读 /dʒaʊlz/','焦耳〔复数〕',
 '能量多于一个焦耳，或泛说用焦耳计，就用 joules。无论来自热、运动还是电，所计的都是相应能量、功的数量。',
 'joule + -s → joules；/l/ 后读 /z/，词尾 /lz/。基础词来自 James Prescott Joule 的姓，复数按现代英语规则变化。',JOULE+[['joule + -s → joules','多个焦耳，或泛指以焦耳计量']],
 'ten joules 是十焦耳；energy in joules 是以焦耳表示的能量。复数是单位名称的词尾变化，单位符号 J 保持原样。',
 'ten joules；energy in joules；measured in joules。',
 'joules 与 calories 都可计能量，但换算后数字不同；watts 则计功率，量的种类已经变了。',
 ('The calculation gives an answer of ten joules.','计算得出的答案是十焦耳。'),('The graph shows energy measured in joules.','图中展示了以焦耳计的能量。'),sources=S('joules','joule',[SI]))
W('nanometers','美 /ˈnænoʊˌmiːtɚz/','纳米〔美式复数〕',
 '把一米分成十亿份，每份是一纳米。讨论很薄的膜、光的波长时，nanometers 能把极小长度写成好读的数字。',
 'nano- 十亿分之一 + meter 米 → nanometer；加 -s → nanometers，词尾 /z/。nano- 的命名材料远接希腊 nanos 小个子。',
 [['希腊 nanos 小个子 → 科学 nano- 十亿分之一','与长度单位 meter 结合'],['nanometer + -s → nanometers','1000000000 nanometers = 1 meter']],
 'a thickness in nanometers 是以纳米表示的厚度；a wavelength of five hundred nanometers 是五百纳米的波长。',
 'a few nanometers thick；wavelengths in nanometers；hundreds of nanometers。',
 '1000 nanometers = 1 micrometer。nanometers 是美式拼写，英式常写 nanometres，长度相同。',
 ('The coating is only a few nanometers thick.','这层涂层只有几纳米厚。'),('The graph gives wavelengths in nanometers.','这张图用纳米标出波长。'),sources=S('nanometers','nano-',[SI]))
W('micrometers','单位〔美〕/ˈmaɪkroʊˌmiːtɚz/；仪器：英 /maɪˈkrɒmɪtəz/，美 /maɪˈkrɑːmɪtɚz/','微米〔美式复数〕；测微仪，千分尺〔复数〕',
 '写 five micrometers wide，是宽五微米；写 two micrometers on the bench，可能是工作台上两把千分尺。一个是长度单位，一个是测量工具。',
 '单位：micro- 百万分之一 + meter 米 → micrometer；仪器：micro- 小 + -meter 测量仪，经法语等形成 micrometer。两线各加 -s 成 micrometers，重音不同。',
 [['希腊 mikros 小、metron 测量的材料 → 两条现代构词线','仪器名说测微小距离的工具；单位名说米的百万分之一'],['两个 micrometer 各加复数 -s → micrometers','单位通常重读最前；仪器通常重读第二音节']],
 '单位1 micrometer = 1000 nanometers；英国常写 micrometre、micrometres。仪器千分尺则用来精密测量，不因名称相同就固定只能测一微米。',
 'five micrometers wide；dimensions in micrometers；two micrometers on the bench。',
 '分清“长度多少”与“有几把仪器”。meter 在两条线里分别是米和测量仪构词成分，不能把工具当单位来换算。',
 ('The fiber is ten micrometers wide.','这根纤维宽十微米。'),('The technician checked both micrometers before measuring the parts.','测量零件前，技术员检查了两把千分尺。'),sources=S('micrometers','micrometer',[SI,'https://www.merriam-webster.com/dictionary/micrometer']))
def extend_lessons():
 extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_zje',ROOTS,WORDS)
 extend_lessons()
