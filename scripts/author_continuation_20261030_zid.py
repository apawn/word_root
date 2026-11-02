"""Useful action families: toss, rack, slope, trim and snack."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
def S(word,base):
 return ['https://en.wiktionary.org/wiki/'+word+'#English','https://www.etymonline.com/word/'+base]
EXISTING_ROOT_ADDITIONS={
 'B3002':dict(words='toss tosses tossed tossing'.split(),label='toss：一甩，到抛、颠动、拌匀',note='和 throw 比较抛掷，不是现代 throw 的派生。toss 来历未定，可能接北欧散布、撒开材料；现代抛掷、翻动、拌沙拉按动作理解。'),
 'B3899':dict(words='rack racks racked racking'.split(),label='rack：伸展开的架子，到折磨、绞尽脑汁',note='rack 的架子支可能接中古荷兰 rec 框架、伸展词，动词又有拉伸、折磨；和 stretch 比较更远材料，不是现代 stretch 派生。肉排、流云等同形支各有分析，本组不硬串。'),
 'B2886':dict(words='slope slopes sloped sloping'.split(),label='slope：另源的倾斜、斜坡',note='和 lean 比较倾斜，不是 lean 派生。slope 可能接中古英语 aslope、古英语滑开材料；旧形容、副词到英语动词、名词的形成，不能反画成只有现代斜坡名词先存在。'),
 'B2844':dict(words='trim trims trimmed trimming'.split(),label='trim：整理到合适状态，剪掉多余或加饰边',note='和 cut 比较修剪，不是 cut 派生。trim 可能接古英语 trymman 加强、整理与 trum 稳固，但中古记录有断档，联系需保留不确定；现代剪齐、装饰、调整各支分开学。'),
 'B2743':dict(words='snack snacks snacked snacking'.split(),label='snack：咬、抢取，到一小份吃的',note='和 bite 比较小口，不是 bite 派生。旧 snack 有咬、猛咬材料，可能接北欧、荷兰语等；现代小食名词较早于常用的吃点心动词义，不能单凭短动词先有所有意思。'),
}
TOSS=[['toss 较早有突然抛起、上下翻动的动作','远源未定，可能接北欧散布等材料'],['抛、翻动 → 拌食物；不安地翻身；名词一次抛掷','对象不同，动作图景也随之变化']]
RACK=[['中古荷兰 rec 框架等或相关英语旧伸展材料 → rack','伸展的架子、拉伸装置'],['拉伸、折磨 → 痛苦折磨与绞尽脑汁','rack up 积累有台球等计分来源分析，不定为唯一证实']]
SLOPE=[['可能中古英语 aslope 倾斜地，接古英语滑开材料','先有相关副词、形容词，远源分析保留可能'],['动词倾斜、斜向行进 → 名词斜度、斜坡','现代再用于图线的斜率']]
TRIM=[['可能接古英语 trymman 加强、整理与 trum 稳固','中古记录有间断，不能抹掉不确定性'],['使适合、整齐 → 修剪多余、加饰边、调整状态','现代名词可说修剪一次、饰边，形容词说整洁利落']]
SNACK=[['旧 snack 咬、猛咬 → 名词一口、份额等','远源有北欧、荷兰语等材料分析'],['小食、轻餐 → 现代动词少量吃、吃点心','旧咬的动词早，不等于现代吃零食义先于小食名词']]
W('toss','英 /tɒs/；美 /tɔs/、/tɑs/','抛、甩；颠动、拌匀；辗转；一次抛掷',
 '手腕轻轻一甩，把钥匙抛给对方，是 toss。把沙拉从下面翻起来拌匀，或睡不着反复翻身，也都保留了“来回抛动”的感觉。',
 '较早有突然抛起、上下移动义，远源未定，可能接北欧散布材料。动词又扩到翻动食物、翻身，名词承接一次抛掷。',TOSS,
 'toss someone the keys 是抛钥匙给某人；toss a salad 是拌沙拉；toss and turn 是辗转反侧；a coin toss 是掷硬币。',
 'toss a coin；toss the salad；toss and turn；toss it aside。',
 'toss 通常比 throw 更有轻快、随手或颠动的感觉，但也能写浪把船颠来颠去；别把动作永远限定成很轻。',
 ('Could you toss me the keys?','能把钥匙抛给我吗？'),('Toss the salad gently before serving.','端上桌前，把沙拉轻轻拌匀。'),sources=S('toss','toss'))
W('tosses','英 /ˈtɒsɪz/；美 /ˈtɔsɪz/、/ˈtɑsɪz/','抛掷〔复数〕；抛、翻动、辗转〔第三人称单数〕',
 '连续几次掷硬币，是 coin tosses；他睡不着反复翻身，则是 he tosses and turns。',
 'toss + -es，/s/ 后读 /ɪz/；名词复数、动词三单同形，基础 ss 保留。',TOSS+[['toss + -es → tosses','多次抛掷；或某人抛、翻动、辗转']],
 'coin tosses 数抛掷次数；tosses the ball 是一个人的动作，不是好几个球自动变成复数。',
 'coin tosses；tosses a ball；tosses and turns。',
 'tosses 既可名词又可动词，coin tosses 看次数，she tosses 看动作；判断角色比只认中文抛更有用。',
 ('He tosses the ball from one hand to the other.','他把球从一只手抛到另一只手。'),('The experiment records the results of fifty coin tosses.','实验记录了五十次掷硬币的结果。'),sources=S('tosses','toss'))
W('tossed','英 /tɒst/；美 /tɔst/、/tɑst/','抛了、甩开了；拌匀了；被颠动的',
 '钥匙已经随手抛到桌上，或沙拉已经上下翻拌过，都是 tossed 可以描述的结果。',
 'toss + 完整 -ed，/s/ 后读 /t/；书面 ss 不变，不额外双写。',TOSS+[['toss + -ed → tossed','过去抛、拌；或被上下颠动']],
 'tossed his coat aside 是随手甩开外套；a tossed salad 是拌好的沙拉；was tossed by the waves 写被浪颠动。',
 'tossed the keys；a tossed salad；tossed aside。',
 'tossed aside 可能是随手一扔，也可比喻不重视而搁置；placed aside 更中性地说放在一边。',
 ('She tossed her coat onto the chair.','她随手把外套甩到椅子上。'),('The small boat was tossed about by the waves.','小船被海浪颠来颠去。'),sources=S('tossed','toss'))
W('tossing','英 /ˈtɒsɪŋ/；美 /ˈtɔsɪŋ/、/ˈtɑsɪŋ/','正在抛、甩、翻拌、辗转；抛动过程',
 '边聊天边把球轻抛，或躺在床上一直翻来翻去，都是动作还在进行的 tossing。',
 'toss + -ing；基础末尾已有 ss，直接接后缀，/s/ 接 /ɪŋ/。',TOSS+[['toss + -ing → tossing','抛、拌、翻身等动作的进行形式']],
 'tossing a ball、tossing the salad 按对象区分；tossing and turning 常写睡不安稳。',
 'tossing a coin；tossing the salad；tossing and turning。',
 'tossing a salad 是上下翻拌，stirring 常以勺等在容器里搅动；两者都混合食物，手法不同。',
 ('He stood by the gate, tossing a ball into the air.','他站在门边，把球往空中轻抛。'),('I spent half the night tossing and turning.','我辗转反侧了半个晚上。'),sources=S('tossing','toss'))
W('rack','/ræk/','架子；绞尽脑汁、使痛苦；积累〔rack up〕',
 '把东西展开、挂起的框架，是 rack。旧时也用架子拉伸人体施刑，于是 rack your brains 像把脑力拉到极限：绞尽脑汁想。',
 '架子义可能接中古荷兰 rec、英语旧伸展材料；动词有拉伸、折磨，再扩到心理痛苦、费尽脑力。rack up 积累有台球计分来源分析，不把所有 rack 同形支硬串。',RACK,
 'a drying rack 是晾衣架；rack your brains 是苦思；rack up points 是不断累积分数。a rack of lamb 是一排羊肋排，肉类名词的远源有不同分析。',
 'a luggage rack；a drying rack；rack your brains；rack up wins。',
 'rack 与 wrack 在部分痛苦、毁坏表达里有混用历史，常用 rack your brains 可先整体掌握；普通鞋架写 shoe rack。',
 ('Put the wet clothes on the drying rack.','把湿衣服放到晾衣架上。'),('I had to rack my brains to remember his name.','我绞尽脑汁才想起他的名字。'),sources=S('rack','rack'))
W('racks','/ræks/','架子〔复数〕；使痛苦、绞尽脑汁、积累〔第三人称单数〕',
 '衣服分挂在几排架子上，是 racks；球队一场场拿分，是 racks up points。一个数框架，一个说成绩不断堆高。',
 'rack + -s，/k/ 后读 /s/；名词复数、动词三单同形，基础词末尾 ck 原样保留。',RACK+[['rack + -s → racks','多个架子；或它折磨、某人积累成绩']],
 'clothes racks 是衣架、服装展示架；racks his brains 写他苦思；racks up points 写积累成绩。',
 'luggage racks；clothes racks；racks up points。',
 'racks 常是条杆、框架式支撑，shelves 是一层层搁板；两者都能放东西，但构造画面不同。',
 ('The shop displays coats on wooden racks.','店里把外套挂在木架上展示。'),('The team racks up points with quick passing.','球队靠快速传球不断拿分。'),sources=S('racks','rack'))
W('racked','/rækt/','使痛苦、苦思过；累积了〔racked up〕',
 '事情让人痛苦得像被拉扯，可说 was racked with guilt；一次次成功攒在一起，则是 racked up wins。',
 'rack + 完整 -ed，/k/ 后读 /t/；已有 ck，不再额外添 k。',RACK+[['rack + -ed → racked','过去折磨、费尽脑力；或累积成绩']],
 'racked my brains 是过去苦思；racked with guilt 是内疚折磨着；racked up a record 是积累了某种纪录。',
 'racked his brains；racked with guilt；racked up wins。',
 'racked 与 rocked 拼写、元音不同：rocked 常是摇动、震撼，racked 的痛苦支偏受折磨；不要只按中文难受互换。',
 ('I racked my brains but could not remember the title.','我绞尽脑汁，还是想不起标题。'),('The team racked up six wins in a row.','球队连拿了六场胜利。'),sources=S('racked','rack'))
W('racking','/ˈrækɪŋ/','正在折磨、绞尽脑汁；累积中；使人难受的',
 '为了一个名字反复想，脑子像拉到极限，是 racking your brains；痛苦不断折磨人，也能用这个形式。',
 'rack + -ing，保留已有 ck；过程形式也可形容带来强烈痛苦、紧张的事物。',RACK+[['rack + -ing → racking','折磨、苦思或累积的过程']],
 'racking my brains 是我正在苦思；racking up victories 是成绩一场场增加；a racking cough 是令人痛苦的剧咳。',
 'racking your brains；racking up points；a racking cough。',
 'racking up 不是只把物品放到架子上，常是抽象数量增长；racking your brains 也不描写真实身体受拉伸。',
 ('I was racking my brains for a way to solve the problem.','我正绞尽脑汁想办法解决问题。'),('She kept racking up points in the final round.','最后一轮她不断拿分。'),sources=S('racking','rack'))
W('slope','英 /sləʊp/；美 /sloʊp/','斜坡；斜度、斜率；倾斜、斜向延伸',
 '地面不是平着铺开，而是一边高一边低，就是 a slope；一条路渐渐往河边低下去，作动词可说 slopes down。',
 '可能接中古英语 aslope 倾斜地、古英语滑开材料，先有相关副词、形容词，再有现代动词，名词斜度、斜坡随后发展。不是所有形式都由现代名词后造。',SLOPE,
 'a steep slope 是陡坡，a gentle slope 是缓坡；the slope of a line 是图线斜率，借其倾斜程度命名。',
 'a grassy slope；a steep slope；slope down towards the river。',
 'slope 可往上或往下，方向要看 up、down、视角；downhill 明确往下，不能把所有 slope 都译成下坡。',
 ('The house stands on a gentle slope.','房子建在一处缓坡上。'),('The ground begins to slope down towards the stream.','地面开始向溪流方向逐渐倾斜下去。'),sources=S('slope','slope'))
W('slopes','英 /sləʊps/；美 /sloʊps/','斜坡、山坡；滑雪坡道〔复数〕；倾斜〔第三人称单数〕',
 '山的一面面坡地，是 slopes；the roof slopes down 则是屋顶往下斜。滑雪语境 hit the slopes 是去雪道上滑雪。',
 'slope + -s，/p/ 后读 /s/；名词复数与动词三单同形，末尾不发音 e 保留。',SLOPE+[['slope + -s → slopes','多个坡面；或它倾斜']],
 'grassy slopes 是草坡；ski slopes 是滑雪坡道；slopes gently 说倾斜不陡。',
 'mountain slopes；ski slopes；the road slopes down。',
 'slopes 可是天然山坡或人工雪道，hills 是山丘；同一座 hill 可以有不同方向的 slopes。',
 ('Snow covered the upper slopes of the mountain.','雪覆盖了山上较高处的坡面。'),('The garden slopes gently towards the lake.','花园朝湖边缓缓倾斜下去。'),sources=S('slopes','slope'))
W('sloped','英 /sləʊpt/；美 /sloʊpt/','倾斜了；斜面的、有坡度的',
 '屋顶本来就斜着、让水往下流，可以说 a sloped roof；描述过去地形往某边低，也能用 sloped。',
 'slope 去末尾 e，加完整 -ed → sloped，/p/ 后读 /t/；过去式、过去分词常作形容词。',SLOPE+[['slope 去 e + -ed → sloped','过去倾斜；或呈斜面状态']],
 'a sloped roof、a sloped path 都说不是水平的；具体倾斜角度不由 -ed 表达。',
 'a sloped roof；a gently sloped path；sloped towards the water。',
 'sloped 是有坡度，不等于 slippery 打滑；一个坡可以干燥粗糙，平地也可以很滑。',
 ('The cabin had a sharply sloped roof.','小屋的屋顶坡度很大。'),('The path sloped down to the water.','小路向水边倾斜下去。'),sources=S('sloped','slope'))
W('sloping','英 /ˈsləʊpɪŋ/；美 /ˈsloʊpɪŋ/','倾斜的；正在斜向延伸的',
 '地面渐渐从一边高到另一边低，是 sloping ground。它像用一条斜线把地势连起来，不是在说地面一定正在移动。',
 'slope 去末尾 e，加完整 -ing → sloping；可说动作过程，也常作状态形容词。',SLOPE+[['slope 去 e + -ing → sloping','倾斜的状态，或斜向延伸的过程']],
 'a sloping ceiling 是斜顶，gently sloping land 是缓坡地；-ing 不必一律翻成正在。',
 'sloping ground；a sloping ceiling；gently sloping land。',
 'sloping 与 sloped 都可描述斜面，前者常突出延展形态，后者常突出有此结构；不能硬分成前者在动、后者静止。',
 ('We found a campsite on gently sloping ground.','我们在一片缓坡地上找到了营地。'),('The attic has a low, sloping ceiling.','阁楼有一个低矮的斜顶。'),sources=S('sloping','slope'))
W('trim','/trɪm/','修剪、削减；装饰；整理调整；修剪一次、饰边；整洁利落的',
 '先把东西整理到合适状态：头发太长就剪齐，衣服边太素就加饰边。所以 trim 既能剪掉多余，也能加装饰，不能死记成一律减少。',
 '可能接古英语 trymman 加强、整理与 trum 稳固，但中古记录有断档。现代整理、装饰、剪齐等义早已并行发展，名词、形容词各接相应状态。',TRIM,
 'trim your hair 是修剪头发；trim costs 是削减成本；trim a hat with ribbon 是用丝带装饰帽子；a quick trim 是简单修剪。',
 'trim the hedge；trim costs；a neat trim；a trim figure。',
 'trim 常有去掉多余、整理合适的意味，cut 更广，可能大幅切断；要小修头发，可说 Just a trim。',
 ('Could you trim the ends of my hair?','能把我的发梢稍微修一下吗？'),('The jacket has a narrow strip of gold trim.','夹克边上有一道窄窄的金色饰边。'),sources=S('trim','trim'))
W('trims','/trɪmz/','修剪、削减、装饰〔第三人称单数〕；饰边、修剪次数〔复数〕',
 '园丁定期把树篱剪齐，是 trims the hedge；衣服上不同的装饰边，也可统称 trims。前者去掉一点，后者可能加上一点。',
 'trim + -s，/m/ 后读 /z/；动词三单和可数名词复数同形。',TRIM+[['trim + -s → trims','某人修剪、装饰；或多种饰边、多次修剪']],
 'trims her hair 说动作；decorative trims 说装饰材料、样式；trim 的不同分支须看宾语。',
 'trims the hedge；trims the budget；decorative trims。',
 'trims 不总等于 cuts：trims the dress with lace 是加蕾丝装饰，不是把裙子全部剪成蕾丝。',
 ('He trims the hedge every month.','他每月修剪一次树篱。'),('The shop sells ribbons and decorative trims.','那家店卖丝带和装饰花边。'),sources=S('trims','trim'))
W('trimmed','/trɪmd/','修剪过的；削减了；加了饰边的',
 '树篱边剪得整整齐齐，是 neatly trimmed；裙边加了蕾丝，也是 trimmed with lace。一个减少，一个添加，都在让东西合适、好看。',
 'trim 双写 m，加完整 -ed → trimmed，/m/ 后读 /d/；过去式、过去分词，常作形容词。',TRIM+[['trim → trimmed','双写 m 加 -ed，已经修整、削减或装饰']],
 'neatly trimmed hair 是剪齐的头发，a lace-trimmed collar 是加蕾丝边的领子；不能不看 with 或修饰对象就定方向。',
 'a trimmed hedge；trimmed the costs；trimmed with ribbon。',
 'trimmed with ribbon 表丝带装饰，trimmed off the edge 表剪掉边缘；介词、粒子帮助判断加还是减。',
 ('She trimmed the dead leaves from the plant.','她剪掉了植物上的枯叶。'),('The collar was trimmed with white lace.','领口加饰了白色蕾丝。'),sources=S('trimmed','trim'))
W('trimming','/ˈtrɪmɪŋ/','修剪、削减、调整；饰边、装饰材料',
 '把树篱多出来的枝叶剪掉，是 trimming；衣服上加的一道花边，也能叫 trimming。词一样，动作和装饰物要看句子。',
 'trim 双写 m 加 -ing → trimming；既是过程形式，也发展成修剪活动、装饰材料名词。',TRIM+[['trim → trimming','双写 m 加 -ing，过程或相应装饰名词']],
 'need trimming 是需要修剪；gold trimming 是金色装饰边；the trimmings 另可说剪下的碎料或额外配套，按搭配理解。',
 'hedge trimming；trimming costs；lace trimming。',
 'trimming 作名词可能是加上的饰边，不一定是剪下来的垃圾；trimmings 的复数又有自己的常用搭配。',
 ('The hedge needs trimming before summer.','夏天前需要把树篱修剪一下。'),('She chose a ribbon for trimming the hat.','她选了一条丝带来装饰帽子。'),sources=S('trimming','trim'))
W('snack','/snæk/','小吃、点心、零食；少量地吃、吃点东西',
 '没正式坐下来吃一顿，只拿点食物垫垫肚子，是 a snack。它可以是水果、面包、坚果，不等于词义里已经规定必须不健康。',
 '旧 snack 有咬、猛咬义，远源有北欧、荷兰语等分析；名词经历一口、份额等用法，再指小食。现代吃点心动词义接小食名词发展，和更早咬的动词义分开。',SNACK,
 'have a snack 是吃点东西，snack on nuts 是拿坚果当零嘴吃；a snack 比完整一餐通常轻便、量少。',
 'a quick snack；an afternoon snack；snack on fruit。',
 'snack 描述进食形式、分量，junk food 描述通常被评价为营养较差的一类食物；不是每份 snack 都是 junk food。',
 ('I had a small snack before the journey.','出发前我吃了点东西垫肚子。'),('We like to snack on fruit while working.','我们工作时喜欢拿水果当零嘴吃。'),sources=S('snack','snack'))
W('snacks','/snæks/','小吃、点心、零食〔复数〕；吃点东西〔第三人称单数〕',
 '给大家带几份路上吃的东西，是 snacks；他下午常吃些坚果，则是 he snacks on nuts。',
 'snack + -s，/k/ 后读 /s/；名词复数与动词三单同形。',SNACK+[['snack + -s → snacks','多份点心；或某人吃点东西']],
 'pack some snacks 是备些零食；snacks on fruit 是拿水果当零嘴；不要把带 s 的词一律只认成复数食品。',
 'light snacks；pack snacks；snacks between meals。',
 'snacks 可以是几种或几份食物，meals 是一顿顿正餐；数量、场景不同，一包 snacks 不必构成一顿完整饭。',
 ('We packed snacks for the train ride.','我们为火车旅程带了些零食。'),('She snacks on nuts in the afternoon.','她下午会拿坚果当零嘴吃。'),sources=S('snacks','snack'))
W('snacked','/snækt/','吃了点东西；吃过零食',
 '路上断断续续拿点坚果、水果吃，并没坐下来正式用餐，可以说 snacked on nuts and fruit。',
 'snack + 完整 -ed，/k/ 后读 /t/；已有 ck，不再添 k，也不加一个 /ɪd/ 音节。',SNACK+[['snack + -ed → snacked','过去少量吃东西、吃点心']],
 'snacked on something 明确拿什么当零嘴；snacked throughout the afternoon 写整个下午零零散散吃。',
 'snacked on fruit；snacked between meals；snacked during the trip。',
 'snacked 不等于 ate dinner，只说吃了点东西；动作发生在晚饭时间，也不自动变成正式用餐。',
 ('We snacked on fruit during the journey.','旅途中，我们拿水果当零食吃。'),('He snacked while waiting for the train.','等火车时，他吃了点东西。'),sources=S('snacked','snack'))
W('snacking','/ˈsnækɪŋ/','正在吃点东西；吃零食、点心的活动',
 '手边放一小碗东西，边做别的事边吃几口，这种进行中的轻量进食是 snacking。它说活动，不先替你判断食物好坏。',
 'snack + -ing，保留已有 ck；现代吃小食的过程形式，也可作活动名词。',SNACK+[['snack + -ing → snacking','少量进食、吃点心的过程或习惯']],
 'snacking on grapes 是吃些葡萄；snacking between meals 是两餐之间吃点东西；具体频率与分量由句子补充。',
 'snacking on nuts；snacking between meals；late-night snacking。',
 'snacking 侧重零散、轻量进食，grazing 比喻性地说断断续续吃少量东西；两者接近，但不必每次完全互换。',
 ('She was snacking on grapes while reading.','她一边看书，一边拿葡萄当零食吃。'),('The survey asked people about their snacking habits.','调查询问了人们吃零食的习惯。'),sources=S('snacking','snack'))
def extend_lessons():
 extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_zid',ROOTS,WORDS)
 extend_lessons()
