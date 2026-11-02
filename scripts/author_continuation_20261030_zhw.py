"""Common nouns and everyday speech: era, jersey, nick, ford, pie, china, dude, wow."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
def S(word,base):
 urls=['https://en.wiktionary.org/wiki/'+word+'#English']
 if base=='nick':urls.append('https://www.merriam-webster.com/dictionary/nick')
 elif base!='china':urls.append('https://www.etymonline.com/word/'+base)
 return urls
EXISTING_ROOT_ADDITIONS={
 'C0022':dict(words='era eras'.split(),label='era：另源的时代、阶段',note='与 age 作时间概念比较，不是拉丁 aevum 直接派生。era 经晚期拉丁 aera、era 纪年起点，可能接计算筹码 aera、铜钱 aes 等材料；现代常指有特色的一段历史。'),
 'B2883':dict(words='jersey jerseys'.split(),label='jersey：从岛名到针织料、球衣',note='和 knit 比较织物，不表示 jersey 从 knit 派生。jersey 的布料、上衣、牛种名称接泽西岛 Jersey，岛名更远来源有不同分析。'),
 'B2844':dict(words='nick nicks nicked nicking'.split(),label='nick：小缺口、轻划，到英式口语的偷、逮捕',note='和 cut 比较切口大小，不是 cut 的派生词。nick 承中古英语 nik、nyke 等刻痕材料，远源未定；与 nock 的关系在不同来源中有可能、未证实等表述，不能定为唯一已知来源。'),
 'B3398':dict(words='ford fords forded fording'.split(),label='ford：能涉过的浅滩，到涉水而过',note='ford 承古英语 ford，和 fare 可追到更远的通过、行进同源材料；不是由现代 fare 直接派生。名词浅滩较早，再有动词涉过水体。'),
 'B2946':dict(words='pie pies'.split(),label='pie：馅包在饼皮里',note='与 bread、pizza 作食物比较，不是 bread 的后代。pie 食物名称远源未定，有中古拉丁与喜鹊名 pica 的联系分析，不把喜鹊爱杂物的故事定为唯一来历。'),
 'B3418':dict(words='rubble'.split(),label='rubble：成堆的碎砖、碎石',note='与 rubbish、waste 比较废料，不是现代 waste 的后代。rubble 经盎格鲁法语碎石材料，远源未定，与 rubbish 的关系有分析，但不能定成一个从另一个截短。'),
 'C0202':dict(words='china'.split(),label='china：由产地代指瓷器',note='和 ceramic 作材料、器物比较，不表示来自希腊 keramos。小写 china 是 china ware 的省略，借中国这个来源地名称指瓷器、瓷餐具。'),
 'B2468':dict(words='dude dudes'.split(),label='dude：从讲究穿着的男子，到哥们、家伙',note='与 man 比较称呼、语气，不是现代 man 的派生。dude 早为纽约俚语，来历未定；Yankee Doodle 的缩变是研究分析，不当成无争议结论。'),
 'B3697':dict(words='wow wows wowed wowing'.split(),label='wow：哇，到让人惊叹',note='与 wonder 比较惊奇反应，不是 wonder 的缩写。wow 早为苏格兰惊叹声，后来名词、动词可表示大获成功、使人惊艳；本组优先学日常感叹、动词。'),
}
ERA=[['晚期拉丁 aera、era：用来计算年代的起点','可能接计算筹码 aera 与铜、钱 aes 的材料'],['英语 aera、era：纪年起点、体系 → 一段历史时期','现代强调某段时间有共同特色，不是限定多少年']]
JERSEY=[['Jersey 泽西岛 → jersey 针织布料、Jersey 牛种名','共同以岛为名，岛名更远来源有不同分析'],['针织布料 → 针织上衣、运动球衣','现代球衣的材料不必仍限于羊毛']]
NICK=[['中古英语 nik、nyke 刻口、刻痕 → nick','远源未定；与 nock 等词的关系不能写成定论'],['小刻口、划伤 → 关键点等用法；另有英式俚语偷、逮捕','各支不能硬编成一件从割伤到进监狱的必然故事']]
FORD=[['古英语 ford：水浅、能从底部通过的地方','接更早日耳曼通过、渡越材料'],['名词浅滩 → 动词 ford 涉水而过','不是见字母 for 就拆成现代英语前缀']]
PIE=[['中古英语、相关中古拉丁 pie 等馅饼材料','远源未定，喜鹊词的联系是分析而非确定单线'],['饼皮包多种馅料 → 现代甜、咸 pie','后来有 easy as pie、a slice of the pie 等比喻']]
WOW=[['wow：较早苏格兰材料里的自然惊叹声','不是普通词根加前后缀的结构'],['感叹 → 动词 wow 使人惊艳、惊叹','像让观众不由得发出一声哇']]
W('era','英 /ˈɪərə/；美 /ˈɪrə/','时代；有鲜明特色的时期、阶段',
 '一段历史被某种技术、风格或人物深深影响，就能叫 an era。日常说个人的新阶段，也可借这种开了新篇章的感觉。',
 '经晚期拉丁 aera、era 纪年起点进入英语，可能接计算筹码、铜钱等材料。英语从计时起点、体系发展到一段历史时期，不从现代 age 改字母。',ERA,
 'a new era；the digital era；the end of an era。',
 'an era of change；a bygone era 过去的时代。',
 'era 强调阶段特征，year 是日历单位；一个 era 没有固定必须多少年的长度。',
 ('The invention marked the beginning of a new era.','那项发明标志着一个新时代的开始。'),('The photographs capture an era before mass air travel.','那些照片记录了大众航空旅行普及前的一个时代。'),sources=S('era','era'))
W('eras','英 /ˈɪərəz/；美 /ˈɪrəz/','时代、时期、阶段〔复数〕',
 '不同年代有不同衣服、建筑、音乐风格，这些有特色的阶段可叫 eras。它在分段看历史，不是精确数几年。',
 'era + -s，读 /z/；不加额外音节，两个或更多有特征的时期。',ERA+[['era + -s → eras','多个有共同特色的时间阶段']],
 'different historical eras；music from several eras；past eras。',
 'eras of political change；compare eras。',
 'eras 可以跨越不同长度，decades 每段是十年；比较时代不等于总在比较十年一段。',
 ('The exhibition brings together clothing from several eras.','展览把几个时代的服装放在了一起。'),('The book compares attitudes from different historical eras.','那本书比较了不同时代的观念。'),sources=S('eras','era'))
W('jersey','英 /ˈdʒɜːzi/；美 /ˈdʒɝzi/','针织面料；针织上衣、运动球衣',
 '球员身上印着号码的上衣，常叫 a jersey。它也能说柔软的针织面料：cotton jersey 是棉针织布，不是一位穿棉衣的球员。',
 '从泽西岛 Jersey 的地名取名，先用于针织布料，后来有针织上衣、球衣等用法。岛名更远来历有不同分析，不把地点故事继续编成确定词根。',JERSEY,
 'a football jersey；a team jersey；cotton jersey。',
 'wear a numbered jersey；a dress made of jersey。',
 'jersey 可说料子，也可数一件球衣；a piece of jersey 数布料，a jersey 通常是一件衣服。',
 ('He wore a jersey with the number seven on the back.','他穿着一件背后印着七号的球衣。'),('The dress is made of soft cotton jersey.','那条连衣裙用柔软的棉针织布做成。'),sources=S('jersey','jersey'))
W('jerseys','英 /ˈdʒɜːziz/；美 /ˈdʒɝziz/','针织上衣、运动球衣〔复数〕',
 '球队一整排号码上衣，是 jerseys。这里数成衣；针织布料作为材料时，通常不靠这个普通复数来数几块。',
 'jersey 的 y 前是元音 e，直接加 -s → jerseys；不改成 jersies，读 /z/，基础词末尾已有 /i/。',JERSEY+[['jersey + -s → jerseys','保留 y，数多件球衣、针织上衣']],
 'team jerseys；numbered jerseys；signed jerseys 签名球衣。',
 'red and blue jerseys；players exchanging jerseys。',
 'jerseys 是上衣，uniforms 可以包括整套制服、队服；换球衣不一定包括裤子、鞋。',
 ('The players exchanged jerseys after the match.','比赛后，球员们交换了球衣。'),('The shop sells jerseys from several local teams.','那家店卖几支本地球队的球衣。'),sources=S('jerseys','jersey'))
W('nick','/nɪk/','小刻口、轻划伤；轻轻划破；偷、逮捕〔英式口语〕',
 '刀口碰了一下皮肤，留下很小的伤，是 a nick。in the nick of time 是恰在最后关头；英式口语里 nick 还可说偷、逮捕，不能只靠割伤画面硬推。',
 '承中古英语 nik、nyke 刻口等材料，远源未定。与 nock 的关系有不同表述；小刻痕可对应准确标记点，后来有关键时刻等用法。俚语各支的细桥不硬编。',NICK,
 'a nick in the blade；nick a finger；in the nick of time；get nicked〔英式口语〕。',
 'in good nick 状态良好〔英式口语〕；nick a biscuit 偷拿一块饼干。',
 'nick 常是小缺口、轻划，不等于深深切开；steal、arrest 则是英式俚语分支，要看对象和情境。',
 ('There is a small nick in the edge of the blade.','刀刃边上有一个小缺口。'),('We arrived in the nick of time.','我们恰在最后关头赶到。'),sources=S('nick','nick'))
W('nicks','/nɪks/','小刻口、轻伤〔复数〕；轻划、偷拿、逮捕〔第三人称单数〕',
 '剃完胡子有几个小划口，是 nicks；每次都偷拿块饼干，也可在英式口语里说 nicks a biscuit。同形词靠上下文认分支。',
 'nick + -s，/k/ 后读 /s/；名词复数、动词三单同形。基础词远源未定，不给不同俚语义编一个必然的割伤故事。',NICK+[['nick + -s → nicks','多个小口子；或他、她轻划、偷拿、逮捕']],
 'small nicks in the paint；nicks his finger；nicks a snack。',
 'shaving nicks；nicks on a wooden table。',
 'nicks 作伤口常小，scars 是愈合后留下的疤；刚划的小口子不等于已经有永久痕迹。',
 ('The old table has a few nicks around the edges.','那张旧桌子边缘有几个小缺口。'),('In the story, he nicks a biscuit whenever the cook turns away.','故事里，厨师一转身，他就偷拿一块饼干。'),sources=S('nicks','nick'))
W('nicked','/nɪkt/','轻划破、碰出缺口了；被偷、被逮捕了〔英式口语〕',
 '刚剃胡子不小心划到下巴，是 nicked my chin；英式口语 my bike was nicked 是自行车被偷。词一样，事件完全不同。',
 'nick + 完整 -ed，/k/ 后读 /t/；词尾已是 ck，不再添 k。',NICK+[['nick + -ed → nicked','过去轻划、偷拿或逮捕；也可表示被动']],
 'nicked himself shaving；the bike was nicked；got nicked〔英式口语〕。',
 'a nicked blade 有缺口的刀刃；nicked the paint。',
 'was nicked 在英式口语要看主语：bike 常是被偷，suspect 常是被捕；不是所有被动都译成划伤。',
 ('I nicked my chin while shaving.','我剃胡子时把下巴轻轻划破了。'),('His bicycle was nicked outside the library.','他的自行车在图书馆外被偷了。'),sources=S('nicked','nick'))
W('nicking','/ˈnɪkɪŋ/','正在轻划、碰出小缺口；偷拿、逮捕〔英式口语〕',
 '削东西时怕刀口轻碰手指，就是怕 nicking a finger。英式口语谈偷拿小东西时，也能用这个过程形式。',
 'nick + -ing；已有 ck 保留，不再双写 k。现代过程形式横跨轻划与俚语分支。',NICK+[['nick + -ing → nicking','轻划、偷拿或逮捕的过程']],
 'avoid nicking the surface；nicking biscuits；nicking a suspect〔英式口语〕。',
 'nicking the paint；nicking himself while shaving。',
 'nicking 不总是伤害动作；口语中说偷东西、警方逮捕时，应按对象认义，不套入切割。',
 ('Take care to avoid nicking the painted surface.','小心别把漆面碰出小缺口。'),('The child admitted nicking a few biscuits.','孩子承认偷拿了几块饼干。'),sources=S('nicking','nick'))
W('ford','英 /fɔːd/；美 /fɔrd/','可涉过河流的浅滩；涉水而过',
 '河里有一段浅到能踩着底部过，是 a ford；从这里蹚过去，就是 ford the river。它既能命名地点，也能说过水的动作。',
 '名词承古英语 ford 浅处、可过水处，接更早日耳曼通过材料；后来由名词成动词。与 fare 可比较更远同源，现代把 ford 当作完整基础词。',FORD,
 'cross at the ford；ford a river；a shallow ford。',
 'an old ford；ford the stream。',
 'ford 是踩着底部涉过水，swim 是游过去；桥上跨河则不叫涉水。',
 ('The old road crosses the river at a ford.','旧路从一处浅滩过河。'),('The travellers had to ford a shallow stream.','旅人们得涉过一条浅溪。'),sources=S('ford','ford'))
W('fords','英 /fɔːdz/；美 /fɔrdz/','浅滩〔复数〕；涉水过河〔第三人称单数〕',
 '旧地图标着好几处能蹚水过河的地点，是 fords；人物每天涉过溪流，也可说 he fords the stream。',
 'ford + -s，读 /z/；名词复数与动词三单同形，古英语浅滩名词早于英语动词。',FORD+[['ford + -s → fords','多个可过河浅处；或他、她涉水而过']],
 'several river fords；fords the stream；old fords marked on a map。',
 'shallow fords；fords a river on horseback。',
 'fords 是地点或涉水动作，bridges 是桥；两者都能帮助过河，但结构和过法不同。',
 ('The map marks several old fords.','地图标出了几处旧时的过河浅滩。'),('In the novel, the messenger fords the stream on horseback.','小说里，信使骑着马涉过溪流。'),sources=S('fords','ford'))
W('forded','英 /ˈfɔːdɪd/；美 /ˈfɔrdɪd/','涉水过河、过溪了',
 '已经踩着浅水底部过到另一边，过去这件事叫 forded。它比 crossed 更具体，交代了不是过桥、乘船。',
 'ford + 完整 -ed，基础末音 /d/ 后读 /ɪd/；新增一个音节。',FORD+[['ford + -ed → forded','过去踩着水底通过水体']],
 'forded the river；forded a stream；had forded the shallow water。',
 'forded on horseback；forded at the narrow crossing。',
 'crossed 只说从一边到另一边，forded 说明涉水过；没写交通方式时不能随意替换。',
 ('They forded the stream near the old mill.','他们在旧磨坊附近涉过溪流。'),('The riders forded the river before dawn.','骑手们黎明前涉过了河。'),sources=S('forded','ford'))
W('fording','英 /ˈfɔːdɪŋ/；美 /ˈfɔrdɪŋ/','正在涉水过河；涉水通行',
 '脚、马蹄或车辆在浅水底部往前走，过到另一岸的过程，是 fording。它是具体的过水方式，不是只在河边走。',
 'ford + -ing；保留 d，不因过去式有 /ɪd/ 就在这里也多添 /d/ 音节。',FORD+[['ford + -ing → fording','踩着水底过河、过溪的过程']],
 'fording a river；a fording place 涉水通行处；fording the stream。',
 'riders fording shallow water；a scene of fording。',
 'wading 可以只是在水里走，fording 更明确在过一条水体；沿着水边踩水不一定到了另一岸。',
 ('The painting shows riders fording a shallow river.','画里是骑手们涉过一条浅河的场景。'),('The story describes the difficulty of fording the stream after rain.','故事写了雨后涉过溪流的艰难。'),sources=S('fording','ford'))
W('pie','/paɪ/','馅饼、派；可分配的总量〔比喻〕',
 '把肉、蔬菜或水果馅放进饼皮里烤，是 pie。a slice of the pie 又可说从共同利益里分到一块，像一张饼切着分。',
 '有中古英语、相关中古拉丁 pie、pia 等材料，远源未定。与喜鹊 pica 杂收东西的联系是一种分析，不能直接讲成确定的命名故事。',PIE,
 'apple pie；a meat pie；a slice of the pie；easy as pie 很容易。',
 'pie in the sky 不切实际的美好愿望；a pie chart 饼图。',
 'pie 不必甜，meat pie 是咸馅；cake 更常说蛋糕，不能把所有烘焙甜点都叫 pie。',
 ('She baked an apple pie for the family.','她给家里人烤了一个苹果派。'),('Small businesses want a bigger slice of the pie.','小企业希望在总收益里分到更大一块。'),sources=S('pie','pie'))
W('pies','/paɪz/','馅饼、派〔复数〕',
 '柜台上几只肉馅饼、几只苹果派，都是 pies。它数整只成品，切出来的片再用 slices 数。',
 'pie + -s，读 /z/；末尾 ie 不改 y，直接加复数后缀。',PIE+[['pie + -s → pies','多个甜、咸馅饼']],
 'apple pies；meat pies；freshly baked pies。',
 'two small pies；pies cooling on the shelf。',
 'pies 与 peas 豌豆读音不同：/paɪz/ 对 /piːz/；菜单里也分别是成品食物与蔬菜。',
 ('The bakery sells both sweet and savoury pies.','那家面包店既卖甜馅饼，也卖咸馅饼。'),('Two small pies were cooling on the shelf.','架子上有两个小馅饼正在放凉。'),sources=S('pies','pie'))
W('rubble','/ˈrʌbəl/','碎砖、碎石；倒塌建筑留下的瓦砾',
 '墙倒了，不再是一块完整的墙，而是一地碎砖碎石，就是 rubble。重点是硬质东西碎成不规则的一堆，不是泛指所有生活垃圾。',
 '经盎格鲁法语碎石材料，远源未定；与 rubbish 的联系有分析，不强定一个从另一个截短。末尾 -le 不能在现代随意切出一个有固定义的 rub。',
 [['盎格鲁法语 *robel 等碎石材料 → 英语 rubble','远源未定，与 rubbish 废料词有关系分析'],['碎裂的石块 → 建筑倒塌、拆除留下的瓦砾','现代通常作不可数名词谈整堆物料']],
 'a pile of rubble；clear the rubble；reduce a building to rubble。',
 'rubble from the old wall；bricks and rubble。',
 'rubble 多指碎砖碎石，rubbish 是更宽的废物、垃圾；纸屑、剩饭通常不叫 rubble。',
 ('The old wall collapsed into a pile of rubble.','旧墙塌成了一堆瓦砾。'),('Workers cleared the rubble from the path.','工人们清走了小路上的碎砖碎石。'),sources=S('rubble','rubble'))
W('china','/ˈtʃaɪnə/','瓷器、瓷餐具；瓷制的〔作定语〕',
 '把精致的茶杯、盘子摆出来，是 bring out the china。小写时说器物、材料；大写 China 才通常是国家名称，两者的历史通过产地连在一起。',
 '由 China 作产地定语的 china ware、chinaware 等称呼省略而来，用来源地代称瓷器。瓷器名称的传播也有波斯语、印度等中间使用背景，不把现代小写词按字母拆。',
 [['China 作为瓷器来源地称呼 → china ware、chinaware','产地名称进入材料、器物名称'],['省略 ware 等 → china','现代多指瓷器、瓷餐具，不要求每件都产于中国']],
 'fine china；a china cup；a set of china 一套餐具。',
 'a china doll；the best china；bone china 骨瓷。',
 'china 作餐具通常不可数，two china cups 是两个瓷杯；不把普通数量写成 two chinas。',
 ('She brought out the best china for the celebration.','为了庆祝，她拿出了家里最好的瓷餐具。'),('The little cup is made of fine china.','那个小杯子由精细瓷料制成。'),sources=S('china','china'))
W('dude','/duːd/','家伙、哥们；嘿、老兄〔口语称呼〕',
 'a nice dude 就是一个不错的家伙；朋友间开口 Dude! 可以像“哥们！”具体是亲切、惊讶还是不满，要听语气。',
 '较早为纽约俚语，说穿着、举止很讲究的男子，远源未定。后来用于城市游客等，再广泛说男人、哥们；Yankee Doodle 缩变是分析，不当成定论。',
 [['早期 dude：讲究打扮的男子、城里来的人','来源未定，有词曲名缩变等分析'],['现代泛指男人、家伙 → 口语称呼','语气依关系、场景，不必真的在评价衣着']],
 'a nice dude；Hey, dude!；some dude I met。',
 'that dude over there；Dude, look at this!。',
 'dude 很随意，sir 更正式；对陌生人、正式场景直接叫哥们不一定合适，语体是词义的一部分。',
 ('That dude at the counter helped me find the book.','柜台旁那个哥们帮我找到了书。'),('Dude, you have to see this view!','哥们，你一定得看看这景色！'),sources=S('dude','dude'))
W('dudes','/duːdz/','家伙们、哥们儿〔复数，口语〕',
 '几个很随和的家伙，可以说 a few friendly dudes。也可向一群朋友招呼 Hey, dudes!，语气比正式称呼松得多。',
 'dude + -s，/d/ 后读 /z/；末尾 e 保留，复数不增加音节。',
 [['dude 从讲究衣着者，到泛指男子、哥们','现代常用随意、口语语气'],['dude + -s → dudes','多个家伙，或招呼一群朋友']],
 'a couple of dudes；friendly dudes；Hey, dudes!。',
 'those dudes over there；a group of young dudes。',
 'dudes 常让人想到男性朋友、家伙，某些群体中称呼范围可更宽；正式介绍一群人时不必一律用它。',
 ('A couple of dudes were playing guitar outside the café.','几个哥们在咖啡馆外弹吉他。'),('Those dudes helped us carry the boxes upstairs.','那几个哥们帮我们把箱子搬上楼。'),sources=S('dudes','dude'))
W('wow','/waʊ/','哇〔惊叹〕；使人惊艳、赞叹',
 '看见好景色，不由得“哇！”一声，就是 wow。作动词时，是表演、设计等好到让人发出这声惊叹。',
 '较早苏格兰材料中的自然惊叹声，后来发展出成功、惊艳等名词、动词义。不是缩写，也没有需要硬切的古典前后缀。',WOW,
 'Wow, that is beautiful!；wow the audience；the wow factor 惊艳效果。',
 'a performance that can wow people；a real wow 大获成功的东西〔口语〕。',
 'wow 常带赞叹，也可只是惊讶，语气决定情绪；动词 wow an audience 通常偏正面的震撼。',
 ('Wow, the stars are so clear tonight!','哇，今晚的星星看得真清楚！'),('The performance is designed to wow the audience.','那场表演就是要让观众惊艳赞叹。'),sources=S('wow','wow'))
W('wows','/waʊz/','使人惊艳、赞叹〔第三人称单数〕；几声惊叹',
 '歌手一开口就让全场惊艳，可以说 wows the audience。场中传来几声哇的赞叹，也可把声音数作 wows。',
 'wow + -s，读 /z/；w 是基础拼写的一部分，不重复。动词三单和可数惊叹声复数同形。',WOW+[['wow + -s → wows','他、她或它让人惊艳；多声惊叹']],
 'wows the crowd；wows the judges；oohs and wows。',
 'wows visitors；draws wows from the audience。',
 'wows 偏赞叹，shocks 可以是惊吓、震惊；让人吃惊并不一定讨人喜欢。',
 ('Her powerful voice wows the audience.','她有力量的嗓音让观众惊艳。'),('The view drew several wows from the group.','那片景色引得大家发出几声赞叹。'),sources=S('wows','wow'))
W('wowed','/waʊd/','让人惊艳、赞叹了；被惊艳了',
 '刚看完一场精彩演出，觉得真让人惊艳，可以说 I was wowed。表演作主语，则是 it wowed us，主动、被动换的是观察角度。',
 'wow + 完整 -ed，读 /d/；不增加 /ɪd/ 音节，也不重复 w。',WOW+[['wow + -ed → wowed','过去使人赞叹，或被精彩之处打动']],
 'wowed the audience；was wowed by the view；wowed the judges。',
 'wowed everyone；not easily wowed 不容易被惊艳。',
 'was wowed 是受惊艳的感受，was bored 才是觉得无聊；wow 的动词通常不用于普通负面惊吓。',
 ('The young pianist wowed the judges.','那位年轻钢琴家让评委们惊艳赞叹。'),('We were wowed by the view from the summit.','山顶的景色让我们惊叹不已。'),sources=S('wowed','wow'))
W('wowing','/ˈwaʊɪŋ/','正在使人惊艳、赞叹',
 '一场表演不断让人叫好，一项设计持续吸引大家赞叹，是 wowing。重点是对观众的效果，而不只是自己做得很卖力。',
 'wow + -ing，直接保留 w；不写 wowwing。由惊叹声发展来的动词，再加过程后缀。',WOW+[['wow + -ing → wowing','使观众发出惊叹的过程']],
 'wowing the crowd；wowing audiences；wowing visitors。',
 'a talent for wowing people；wowing the judges。',
 'wowing audiences 说效果惊艳，performing 只说演出；不是所有完成的表演都获得强烈赞叹。',
 ('The magician has been wowing audiences all week.','那位魔术师这一周的演出都让观众惊叹。'),('The new display is wowing visitors with its scale.','新展陈以宏大的规模，让参观者赞叹不已。'),sources=S('wowing','wow'))
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_zhw',ROOTS,WORDS)
 extend_lessons()
