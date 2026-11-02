"""Common spoken clippings and measurement words, with distinct routes kept clear."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
SI='https://www.bipm.org/documents/20126/41483022/SI-Brochure-9-EN.pdf/2d2b50bf-f2b4-9661-f402-5f9d66e4b507?download=true&t=1780410776583&version=7.0'
def S(word,base):
 a=['https://en.wiktionary.org/wiki/'+word+'#English']
 if base in ['semi','trans','cyber']:a.append('https://www.merriam-webster.com/dictionary/'+base)
 else:a.append('https://www.etymonline.com/word/'+base)
 if base=='cyber':a.append('https://www.etymonline.com/word/cybernetics')
 if base=='prof':a.append('https://www.etymonline.com/word/profess')
 if base=='stat':a+=['https://www.merriam-webster.com/dictionary/stat','https://www.etymonline.com/word/statistics']
 if base=='kilo':a.append('https://www.etymonline.com/word/kilogram')
 if base in ['kilo','litre','liter','tonne','milligram','megawatt','sec','minute']:a.append(SI)
 return a
EXISTING_ROOT_ADDITIONS={
 'C1304':dict(words='semi semis'.split(),label='semi：半的前缀材料，到几个常见长词的短称',note='semi 分别可缩 semifinal半决赛、semitrailer 半挂货车、semidetached house 半独立式住宅等；前缀 semi- 接拉丁半。现代独立名词按语境还原，不把三个具体事物当作彼此演化。'),
 'C1535':dict(words='trans'.split(),label='trans：对侧的科学用法与 transgender 的短称',note='化学形容词 trans 直接接拉丁 trans 对面、另一侧的材料；形容人的现代 trans 常缩 transgender。共享跨越、另一侧的词形背景，但现代各领域含义分别掌握。'),
 'A1731':dict(words='cyber'.split(),label='cyber：掌舵、控制词族到计算机网络相关',note='cyber 接 cybernetics、cybernetic 的构词材料，远处是希腊 kybernētēs 掌舵者、kybernan 掌舵、控制；现代组合形式又可独立作形容词，表示计算机、网络相关。'),
 'C0399':dict(words='prof profs'.split(),label='professor → prof → profs：教授的口语短称',note='professor 接拉丁 professor、profiteri 公开声明、宣称有专长，远处与说、承认词族有关；现代缩成 prof，再加复数 -s，/f/ 后读 /s/。'),
 'C0415':dict(words='ref refs'.split(),label='referee、reference → ref → refs：裁判与引用的短称',note='ref 可缩 referee 裁判，也可缩 reference 参考、引用；两个长词都接 refer 词族，不能把裁判的职业动作当作所有引用的起源。refs 兼名词复数与相关动词第三人称。'),
 'C1404':dict(words='stat stats'.split(),label='stat：statistic 的短称；statim 立即的缩略另支',note='统计数据名词 stat 缩 statistic，远接 statistics 的国家事务、拉丁 status 状态、stare 站立词线；立即副词 stat 缩拉丁 statim，两个现代短称分开解释。'),
 'C1317':dict(words='sec secs'.split(),label='second → sec → secs：秒到一会儿',note='second 秒源于第二次细分的小份，second 第二本来接跟随、下一位的词族；sec、secs 是口语短称，a sec 常只表示一会儿，不保证正好一秒。'),
 'C0743':dict(words='mins'.split(),label='minutes → mins：分钟的随意短写',note='mins 是 minutes 的常见非正式短写、短称，完整 minute 接拉丁 minuta 小份、minuere 减少。正式单位符号 min 不因复数而加 s，和随意文本 mins 分清。'),
 'C0633':dict(words='kilo kilos'.split(),label='kilogram → kilo → kilos：千克的短称',note='kilo 名词缩 kilogram 千克，长词前缀 kilo- 接希腊千的材料；现代 two kilos 通常说两千克，不能只把数量词前缀千当成单位。'),
 'C0725':dict(words='litre litres liter liters'.split(),label='litre、liter：和 measure 对照的容量单位名称',note='这里与 measure 对照计量，升的名称不由 mensur- 派生。litre、liter 是同一容量单位的英美常见拼写，借法语 litre、旧 litron，远接希腊 litra 旧重量、钱币名；不由拉丁 littera 字母词根派生。'),
 'B3474':dict(words='tonne tonnes'.split(),label='tonne → tonnes：桶的旧计量背景到公吨',note='tonne 以法语拼写进入英语，现代指公吨；远处与 ton、tun 桶的旧计量背景有关。复数 tonnes，1 tonne = 1000 kg，英语 ton 则需另辨计量体系。'),
 'A1688':dict(words='milligram milligrams'.split(),label='milli- + gram → milligram → milligrams：千分之一克',note='milli- 虽远接拉丁 mille 千，现代单位前缀约定为千分之一；milligram 是一克的千分之一，复数给整个单位名末尾加 s。'),
 'B3141':dict(words='milligram milligrams'.split(),label='milligram → milligrams：克词族的细分单位',note='milligram 经法语 milligramme，milli- 千分之一 + gram 克；gram 远接希腊小重量用法，与记录、字母的 gramma 有历史关系。'),
 'B3368':dict(words='megawatt megawatts'.split(),label='mega- + watt → megawatt → megawatts：百万瓦',note='mega- 在科学单位中表示一百万，watt 以 James Watt 姓名命名功率单位。megawatts 是功率，不是累计电量，词尾 /ts/。'),
 'C0714':dict(words='megawatt megawatts'.split(),label='mega- 的单位用法：megawatt、megawatts',note='希腊大、强的材料用于 mega-；科学计量中约定百万倍，megawatt = 1000000 watts。它的精确数值不能换成普通口语 mega 很大的模糊程度。'),
}
SEMI=[['拉丁 semi- 半 → 多个现代英语长词','semifinal 半决赛；semitrailer 半挂货车；semidetached house 半独立式住宅'],['各长词按场景缩成 semi → semis','短称相同，不表示三个具体词义一条接一条演化']]
PROF=[['拉丁 profiteri 公开宣称、professor 教习者 → 英语 professor','借法语等传播，人物名有公开宣称知识、专长的背景'],['professor → 口语短称 prof → profs','现代截短，再用英语规则复数']]
REF=[['refer 词族 → referee 受托裁定者、reference 参考引用','较远有拉丁 re- 回 + ferre 带、承载的材料'],['referee、reference 分别缩成 ref → refs','裁判和引用按场景还原，不把两种缩略当完全同义']]
SEC=[['拉丁 secundus 随后的、第二的 → 第二次细分的小份称呼','秒的名称与分钟之后再细分一层有关'],['英语 second → sec → secs','既说秒，也常用一秒、一会儿来表示很短时间']]
LITRE=[['法语 litre ← 旧法语容量名 litron ← 中世纪拉丁 litra','更远接希腊 litra 旧重量、钱币名；名称经历计量对象变化'],['英语 litre、liter → litres、liters','同一容量单位的常见英美拼写，现代 1 L = 1 dm³']]
W('semi','英 /ˈsemi/；美 /ˈsɛmi/、/ˈsɛmaɪ/','半决赛；半挂货车〔美〕；半独立式住宅〔英〕〔不同长词的短称〕',
 '赛场上的 a semi 是半决赛；公路上的 a semi 常是半挂货车；英国房屋介绍里的 a semi 又常说半独立式住宅。短词相同，要从场景找回长词。',
 'semi 分别缩略 semifinal、semitrailer、semidetached house 等。它们都有拉丁 semi- 半的材料，但并不是先从球赛演化成货车、再变成房子。',SEMI,
 'reach a semi 是打进一场半决赛；a semi on the highway 是公路上的半挂货车；live in a semi 是住半独立式住宅，后者常见于英式语境。',
 'a cup semi；a semi on the highway；live in a semi。',
 '独立名词 semi 要按语境还原完整名称；放在别的词前的 semi- 则仍可表达半、部分等构词意义。',
 ('She reached the semi of the cup competition.','她打进了杯赛半决赛。'),('A semi pulled into the warehouse yard.','一辆半挂货车驶进仓库院子。'),('They live in a three-bedroom semi.','他们住在一套有三间卧室的半独立式住宅里。'),sources=S('semi','semi'))
W('semis','英 /ˈsemiz/；美 /ˈsɛmiz/、/ˈsɛmaɪz/','半决赛；半挂货车；半独立式住宅〔semi 的复数〕',
 '比赛到了 the semis，是打到半决赛阶段；车场里几辆大半挂车，也可叫 semis。语境决定是哪一个长名称的短称。',
 'semi + -s → semis，元音后读 /z/；基础词中的 /i/ 或 /aɪ/ 随常见地区读法保留。',SEMI+[['semi + -s → semis','不同短称共享的现代复数，后缀 /z/']],
 'reach the semis 是打进半决赛；two semis 是两辆半挂货车或两套半独立式住宅，需由上下文确定。',
 'reach the semis；the semis and the final；two semis outside the warehouse。',
 'the semis 常整体说半决赛阶段，不需要每次严格数出几场；谈车辆、房屋时才按相应对象计数。',
 ('The team reached the semis for the first time.','这支队伍首次打进半决赛。'),('Two semis were parked outside the warehouse.','仓库外停着两辆半挂货车。'),sources=S('semis','semi'))
W('trans','英、美 /trænz/，也可 /træns/','跨性别的〔常为短称〕；反式的〔化学〕',
 'trans people 是跨性别者，即性别认同与出生时指定性别不一致的人；化学里 trans 又说特定基团分处对侧。两个语境分别理解。',
 '形容人的 trans 常缩 transgender；化学形容词 trans 直接接拉丁 trans 在另一侧的材料。两种现代用法有共同的跨越、另一侧词形背景，具体意义各自发展。',
 [['拉丁 trans 在另一侧 → 科学构词中的 trans','化学里用于双键、环等结构的特定对侧排列'],['transgender 等词的截短 → 现代形容词 trans','通常放在 people、person 等名词前使用']],
 'trans people 是跨性别者；a trans writer 是跨性别作家；the trans form of a molecule 是分子的反式形式。',
 'trans people；a trans writer；the trans form。',
 '修饰人的 trans 通常是形容词；科学文章中的 trans 可能是结构术语，应由所修饰对象和领域确定意思。',
 ('The book includes interviews with trans people.','这本书收录了对跨性别者的访谈。'),('The diagram shows the trans form of the molecule.','图中展示了该分子的反式形式。'),sources=S('trans','trans'))
W('cyber','英 /ˈsaɪbə/；美 /ˈsaɪbɚ/','计算机、网络相关的',
 'cyber risks 是网络风险，cyber skills 是网络、计算机方面的技能。现代先抓“计算机和网络这一边的”意思。',
 'cybernetics 通信与控制理论、cybernetic 的材料 → cyber- 组合形式，再独立作形容词 cyber；更远接希腊 kybernētēs 掌舵者、kybernan 掌舵、控制。',
 [['希腊掌舵、控制词族 → cybernetics 通信与控制理论','船舵保持航向的画面帮助理解控制、引导'],['cybernetic 等材料 → cyber- → cyber 形容词','现代大量用于计算机、网络领域']],
 'cyber security 是网络安全；cyber risks 是网络风险；cyber skills 是计算机、网络相关技能。',
 'cyber security；cyber risks；cyber skills。',
 'cyber 的现代用法重点在计算机、网络；掌舵是理解更远词源的画面，翻译具体搭配时按现代领域处理。',
 ('The course introduces basic cyber security concepts.','这门课介绍基础网络安全概念。'),('The report examines cyber risks faced by small businesses.','报告考察小企业面临的网络风险。'),sources=S('cyber','cyber'))
W('prof','英 /prɒf/；美 /prɑf/','教授〔非正式短称〕',
 '学生聊天说 the prof，通常就是“那位教授”。长长的 professor 缩成一个短音节，语气随意一些。',
 'professor 截短 → prof。长词接拉丁 profess- 公开宣称的词干 + -or 人，向前有 pro- 向外 + fateri 承认、宣称的材料；现代 prof 不是重新添加职业后缀的新词。',PROF,
 'a history prof 是历史教授；my maths prof 是我的数学教授；talk to the prof 是和教授谈谈。',
 'a history prof；my maths prof；talk to the prof。',
 'prof 适合随意聊天；正式称呼、文件里 professor 更稳妥。书写头衔 Prof. 常可展开读为 Professor，不必每次都读短称。',
 ('My history prof recommended this book.','我的历史教授推荐了这本书。'),('I spoke to the prof after class.','课后我和教授谈了谈。'),sources=S('prof','prof'))
W('profs','英 /prɒfs/；美 /prɑfs/','教授们〔口语复数〕',
 '几位教授，学生随意聊天时可以说 profs。截短以后，复数像普通名词一样加 s。',
 'prof + -s → profs，/f/ 后读 /s/，词尾 /fs/；既不改成 v，也不另添一个 /ɪz/ 音节。',PROF+[['prof + -s → profs','多位教授的口语短称，词尾 /fs/']],
 'two profs 是两位教授；visiting profs 是访问教授；the profs in our department 是我们系里的教授。',
 'two profs；visiting profs；the profs in our department。',
 'profs 与 professors 词义可对应，前者更随意；在正式介绍里用完整长词通常更清楚。',
 ('Two profs joined the discussion.','两位教授加入了讨论。'),('The students invited their profs to the exhibition.','学生们邀请教授们参观展览。'),sources=S('profs','prof'))
W('ref','英 /ref/；美 /rɛf/','裁判；参考、引用〔非正式短称〕；担任裁判',
 '球场上吹哨的 ref 是裁判；笔记里的 ref 可能是一条参考、引用。要从两个不同长词里找回它的完整身份。',
 '裁判 ref 缩 referee；引用 ref 缩 reference。两者都接 refer 词族，远有 re- 回 + ferre 带的材料；ref 也能缩 referee 的动词，表示执裁。',REF,
 'the ref blew the whistle 是裁判吹哨；a source ref 是出处引用；ref a match 是担任一场比赛的裁判。',
 'the ref；a source ref；ref a match。',
 'referees 是裁判们，references 是引用、参考资料；两者都缩成 refs 时，仍需从体育或文献语境判断。',
 ('The ref stopped play after the foul.','犯规后，裁判叫停了比赛。'),('I added the source ref to my notes.','我把出处引用加进了笔记。'),sources=S('ref','ref'))
W('refs','英 /refs/；美 /rɛfs/','裁判们；参考、引用〔复数短称〕；担任裁判',
 '场边几位裁判是 refs；文章末尾几条参考出处，也可能缩写成 refs。单数主语后还可能是执裁动词。',
 'ref + -s → refs，/f/ 后读 /s/。名词复数、动词第三人称单数同形；基础短词各自还原 referee 或 reference。',REF+[['ref + -s → refs','多位裁判、多条引用，或执裁动词，词尾 /fs/']],
 'the match refs 是比赛裁判；add refs 是加参考出处；refs local games 是为本地比赛执裁。',
 'the match refs；add refs；refs local games。',
 'refs 不是一个意思固定的独立古典词根；这里是两个同族长词的短称，现代句法再决定词性。',
 ('The refs checked the result before the restart.','重新开赛前，裁判们核对了结果。'),('Please add refs for the figures in the report.','请为报告中的数字加上参考出处。'),('He refs local games on Sundays.','他周日为本地比赛执裁。'),sources=S('refs','ref'))
W('stat','英、美 /stæt/','一项统计数据〔口语〕；立刻、马上〔另一路缩略〕',
 'a useful stat 是一条有用的数据；someone shouts “stat!” 时，可能是在催“立刻！”两个短称要分别还原。',
 '统计名词 stat 缩 statistic，远接 statistics、国家事务与拉丁 status 状态的词线；立即副词 stat 则缩拉丁 statim 立即。不能从看数据推演出催人快点的词义。',
 [['国家状态、事务等词线 → statistics、statistic → stat','现代缩略，一项统计数据，复数 stats'],['拉丁 statim 立即 → 缩略 stat','副词常见于医疗语境，也可在日常夸张催促中使用']],
 'a useful stat 是有用数据；player stats 是球员数据；I need it stat 是我马上就要。',
 'a useful stat；a surprising stat；need it stat。',
 'statistic 的复数 stats 很常见；stat 也能单说一项数据。表示立即时是副词，不是在数统计项目。',
 ('She quoted one stat from the report.','她引用了报告里的一项统计数据。'),('“I need that file, stat!” the editor said.','编辑说：“那个文件我马上就要！”'),sources=S('stat','stat'))
W('sec','英 /sek/；美 /sɛk/','秒；一会儿〔second 的口语短称〕',
 'Wait a sec 是“等一下”，通常不要求你真的计时一秒。短词背后，秒和第二其实有一段共同来历。',
 'second 秒缩成 sec。小时先分为六十分之一的小份，再对它作第二次六十等分，第二次的小份成为 second 秒；second 第二更远接拉丁随后的、跟随材料。',SEC,
 'a sec 是一秒、一会儿；just a sec 是稍等一下；in a sec 是马上、一会儿就好。',
 'just a sec；wait a sec；in a sec。',
 'sec 的时间义常是 second 的短称；口语 a sec 可表示很短时间，不是每次都作严格的一秒承诺。',
 ('Wait a sec while I find the key.','等一下，我找找钥匙。'),('I will be ready in a sec.','我马上就准备好。'),sources=S('sec','sec'))
W('secs','英 /seks/；美 /sɛks/','秒；几秒钟、一会儿〔复数短称〕',
 'a few secs 是几秒钟，也常随意说稍微等一会儿。它给 sec 这个短称加上普通英语复数。',
 'sec + -s → secs，/k/ 后读 /s/，词尾 /ks/。来自 second 的短称，不是另一个古典计时词根。',SEC+[['sec + -s → secs','多秒、几秒钟，词尾 /ks/']],
 'a few secs 是几秒钟；ten secs 是十秒；back in a few secs 是几秒钟后回来。',
 'a few secs；ten secs；back in a few secs。',
 '随意文本可写 secs；正式计量中秒的单位符号是 s，不随着复数再添 s。',
 ('The screen went dark for a few secs.','屏幕黑了几秒。'),('Give me ten secs to finish this.','给我十秒把这个做完。'),sources=S('secs','sec'))
W('mins','短称可读 /mɪnz/；展开为 minutes 时读 /ˈmɪnɪts/','分钟〔minutes 的非正式短写、短称〕',
 '消息里写 five mins，就是五分钟。它省掉长词的一部分，适合便条、聊天、简短界面文字。',
 'minutes 缩短写为 mins；完整 minute 接拉丁 minuta 小份、minuere 减少。短称以 /mɪn/ 的声音为基础接 /z/，朗读时也常直接展开说 minutes。',
 [['拉丁小份、减少词族 → minute 分钟 → minutes','第一次按六十细分得到的小份是其历史计时背景'],['minutes → mins','非正式短写、短称；读法可保留短称或展开长词']],
 'five mins 是五分钟；ten mins away 是还差、相距十分钟；5 mins remaining 是剩余五分钟。',
 'five mins；ten mins away；5 mins remaining。',
 '非正式短写 mins 与正式单位符号 min 分开：单位符号 min 本身不按复数加 s；minutes 另有会议记录义，要按语境看。',
 ('I will be back in five mins.','我五分钟后回来。'),('The message said, “See you in ten mins.”','消息写着：“十分钟后见。”'),sources=S('mins','minute'))
W('kilos','英 /ˈkiːləʊz/；美 /ˈkiloʊz/','千克、公斤〔kilo 的复数短称〕',
 '行李重十二公斤，可以说 twelve kilos。这里的 kilos 已经带着“千克”这个单位，不只是抽象的一千。',
 'kilogram 千克缩为 kilo，再加 -s → kilos，元音后读 /z/。长词里 kilo- 接希腊 khilioi 千，gram 克；这里 kilo- 表一千倍，所以 1 kilogram = 1000 grams。',
 [['希腊千的材料 → 法语、英语 kilo- + gram → kilogram','现代单位前缀 kilo- 表一千倍'],['kilogram → kilo → kilos','日常按千克计重的短称及复数']],
 'two kilos of rice 是两公斤米；weigh twelve kilos 是重十二公斤；a few kilos 是几公斤。',
 'two kilos of rice；weigh twelve kilos；a few kilos。',
 'kilos 是普通名词复数；单位符号 kg 保持同样写法，不能再写成 kgs 来作为规范单位符号。',
 ('The suitcase weighs twelve kilos.','行李箱重十二公斤。'),('She bought two kilos of rice.','她买了两公斤米。'),sources=S('kilos','kilo'))
W('litre','英 /ˈliːtə/；美 /ˈlitɚ/','升〔容量、体积单位；英式常用拼写〕',
 'litre 是升。想象一个边长十厘米的小立方体，它的容积就是一升；这里说能装多少，而不是重量。',
 '借法语 litre，向前有旧容量名 litron、中世纪拉丁 litra、希腊旧重量名 litra；现代容量意义已固定。litre 与美式常用 liter 指同一单位。',LITRE,
 'a litre of water 是一升水；a litre bottle 是一升装瓶子；hold one litre 是容纳一升。',
 'a litre of water；a litre bottle；hold one litre。',
 'litre 计体积，kilogram 计质量，不能只凭体积相同就认为不同物质一样重；liter 只是另一常见拼写。',
 ('The jug holds a litre.','这个壶能装一升。'),('She bought a litre of juice.','她买了一升果汁。'),sources=S('litre','litre'))
W('litres','英 /ˈliːtəz/；美 /ˈlitɚz/','升〔litre 的复数〕',
 '两升、五十升，用完整英式单位名称写，就是 litres。数的是容积，不是在数瓶子。',
 'litre + -s → litres，后缀读 /z/；词尾 re 不按书写顺序另念两个音，基础发音与单数相同再加 /z/。',LITRE+[['litre + -s → litres','英式常见拼写的复数，词尾 /z/']],
 'two litres of milk 是两升牛奶；capacity in litres 是以升计的容量；fifty litres 是五十升。',
 'two litres of milk；capacity in litres；fifty litres。',
 'litres 与 liters 表同一单位，不因英美拼写不同而改变容量；单位符号 L、l 则不加复数 s。',
 ('We bought two litres of milk.','我们买了两升牛奶。'),('The tank holds fifty litres.','这个箱体能装五十升。'),sources=S('litres','litre'))
W('liter','英 /ˈliːtə/；美 /ˈlitɚ/','升〔容量、体积单位；美式常用拼写〕',
 '美国商品、说明书里常写 liter，英国等语境常写 litre。两种写法都表示同一升，不是两套大小不同的单位。',
 'liter 接同一条法语 litre、旧容量名 litron、希腊 litra 的词线；英语的 -er、-re 拼写习惯逐渐分化，现代美式常写 liter。',LITRE,
 'a liter of water 是一升水；a liter of paint 是一升油漆；one liter 是一升。',
 'a liter of water；a liter of paint；one liter。',
 '升的 liter 不属于 literal、literature 那条拉丁字母词族；相同字母开头不能代替实际词源。',
 ('The bottle holds one liter of water.','这个瓶子能装一升水。'),('We used a liter of paint.','我们用了一升油漆。'),sources=S('liter','liter'))
W('liters','英 /ˈliːtəz/；美 /ˈlitɚz/','升〔liter 的复数；美式常用拼写〕',
 '美国文本里写 two liters，通常就是两升。它与 two litres 的容量相同，只是拼写习惯不同。',
 'liter + -s → liters，词尾读 /z/；保留美式常用 -er 排列，不能因为复数又改成另一种字母顺序。',LITRE+[['liter + -s → liters','美式常见拼写的复数，词尾 /z/']],
 'two liters of water 是两升水；capacity in liters 是以升计的容量；several liters 是几升。',
 'two liters of water；capacity in liters；several liters。',
 '单位符号 L 不按复数加 s；liters 是完整单位名，才按普通英语名词规则加 s。',
 ('The tank can hold five hundred liters.','这个箱体能装五百升。'),('The display shows the capacity in liters.','显示屏以升显示容量。'),sources=S('liters','liter'))
W('tonnes','英、美 /tʌnz/','公吨、吨〔tonne 的复数，每吨 1000 千克〕',
 '货物重几公吨，就可以说 tonnes。这个大重量单位，远处有“按大桶计量”的命名背景。',
 'tonne 是从法语拼写进入英语的公吨名，与 ton、tun 大桶旧计量词族有关；tonne + -s → tonnes，e 不发音，/n/ 后读 /z/。',
 [['桶、桶容量等旧计量词族 → ton、法语 tonne 等','名称后来用于重量，具体历史计量有不同体系'],['英语 tonne 公吨 → tonnes','现代 1 tonne = 1000 kg；保留法语式拼写，读 /tʌnz/']],
 'five tonnes of sand 是五吨沙；weight in tonnes 是以公吨计重；several tonnes 是几吨。',
 'five tonnes of sand；weight in tonnes；several tonnes。',
 'tonne 明确指公吨；ton 在不同语境可指不同体系的吨。现代数量换算先认完整单位名，不只看读音相同。',
 ('The truck carried five tonnes of sand.','卡车运载了五吨沙。'),('The report gives the amounts in tonnes.','报告以吨为单位给出数量。'),sources=S('tonnes','tonne'))
W('milligrams','英 /ˈmɪlɪɡræmz/；美 /ˈmɪləˌɡræmz/','毫克〔复数，一毫克为一克的千分之一〕',
 '把一克分成一千份，其中一份是一毫克。milligrams 就是在数这些小小的质量单位。',
 'milli- 接拉丁 mille 千的材料，现代单位前缀约定为千分之一；与 gram 克形成 milligram，整词也经法语 milligramme 传播，再加 -s → milligrams，末尾 /mz/。',
 [['milli- 千分之一 + gram 克 → 法语 milligramme、英语 milligram','古词根材料与现代科学约定要一起看'],['milligram + -s → milligrams','现代复数，1 milligram = 0.001 gram']],
 'five milligrams 是五毫克；mass in milligrams 是以毫克计的质量；a few milligrams 是几毫克。',
 'five milligrams；mass in milligrams；a few milligrams。',
 'milli- 在这里是千分之一，kilo- 是一千倍；单位符号 mg 不随复数再加 s，也不能随意改变大小写。',
 ('The sample weighed five milligrams.','样本重五毫克。'),('The table lists the amounts in milligrams.','表格以毫克为单位列出数量。'),sources=S('milligrams','milligram'))
W('megawatts','英 /ˈmeɡəwɒts/；美 /ˈmɛɡəˌwɑts/','兆瓦〔复数，每兆瓦为一百万瓦；功率单位〕',
 '把瓦这个功率单位放大一百万倍，就是 megawatt；几兆瓦是 megawatts。它说做事、输出能量的快慢，不直接说累计用了多少能量。',
 'mega- 接希腊 megas 大，科学单位中约定百万倍；watt 用 James Watt 的姓名命名。megawatt + -s → megawatts，/t/ 后读 /s/，末尾 /ts/。',
 [['希腊大的材料 → mega- 百万倍；Watt 姓名 → watt 瓦','前缀与功率单位组成 megawatt'],['megawatt + -s → megawatts','1 megawatt = 1000000 watts；现代复数，符号 MW 不另加 s']],
 'ten megawatts 是十兆瓦；capacity in megawatts 是以兆瓦计的功率规模；output in megawatts 是以兆瓦表示输出功率。',
 'ten megawatts；capacity in megawatts；output in megawatts。',
 'megawatts 是功率；要说累计发了多少电，还要考虑持续时间，不能把一天的电量直接当作同一个量。',
 ('The turbine has a capacity of ten megawatts.','这台涡轮机的额定功率为十兆瓦。'),('The chart reports output in megawatts.','图表以兆瓦表示输出功率。'),sources=S('megawatts','megawatt'))
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_zjd',ROOTS,WORDS)
 extend_lessons()
