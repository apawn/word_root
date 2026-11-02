"""Corn and rich: grains, food names and richness beyond money."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
CO=[['古英语 corn → 中古英语 corn → corn','谷物、谷粒；地区上常指当地主要谷物'],['现代地区用法','美式多指玉米；旧谷粒、颗粒义仍留在一些组合里']]
def C(f,m):return CO+[[f,m]]
W('kernel','英 /ˈkɜːnl/；美 /ˈkɜːrnl/','谷粒；果仁；核心；计算机内核',
 '壳或外层去掉，里面那一点实在的仁；一段话最有价值的那一点，也能叫 kernel。',
 '古英语 cyrnel 等旧形式来自 corn 谷粒的同族词干加小称 -el；经历旧元音、拼写变化，不是今天临时把 corn 改成 kern 再拼。核心比喻后来用于计算机等。',CO[:1]+[['旧谷粒词干 + 小称 -el → 古英语 cyrnel → kernel','种子、仁 → 中心、核心']],
 'corn kernels 玉米粒，a walnut kernel 核桃仁，a kernel of truth 一点真实核心，the operating system kernel 操作系统内核。',
 'corn kernels；a walnut kernel；a kernel of truth；the system kernel。',
 'kernel 果仁、内核，shell 外壳；kernel 与 colonel 上校常同音，拼写、来源都不同。',
 ('Remove the kernels from the corn cob.','把玉米粒从玉米芯上剥下来。'),('There is a kernel of truth in what he says.','他的话里有一点真实的东西。'),sources=['https://www.etymonline.com/word/kernel','https://en.wiktionary.org/wiki/kernel#English'])
W('corny','英 /ˈkɔːni/；美 /ˈkɔːrni/','老套、俗气的；过分煽情的〔口语〕',
 '笑话太老、情话太套路，听了想翻白眼又可能忍不住笑，就是常见 corny。',
 'corn + -y，旧有与谷物有关的字面义；现代老套、煽情俚义可能联系乡土趣味等评价，具体动机不完全确定，种子目录笑话故事不当定论。',C('corn + -y → corny','旧谷物相关；后有老套、过分煽情的口语评价'),
 'a corny joke 老套笑话，a corny line 俗套台词，a corny love song 煽情老套的情歌。',
 'a corny joke；a corny line；a corny love song。',
 'corny 多贬套路、煽情，old 古老只说时间；老歌可以很好听，不必都 corny。另源鸡眼义的 corny 不是本页重点。',
 ('He told a corny joke that still made us laugh.','他讲了个老套笑话，还是逗笑了我们。'),('The ending is sweet but a little corny.','结局很甜，但有点俗套煽情。'),sources=['https://www.etymonline.com/word/corny','https://en.wiktionary.org/wiki/corny#English'])
W('corned','英 /kɔːnd/；美 /kɔːrnd/','盐腌的〔尤见 corned beef〕',
 '牛肉被盐粒腌过，不是在牛肉上裹了玉米；corn 在这里保留颗粒的旧义。',
 'corn 的用盐粒腌制动词 + -ed。盐粒曾称 corns，corned beef 由此得名，不是 corn 玉米这一个现代地区义就能解释。',CO[:1]+[['corn〔颗粒；用盐粒腌〕+ -ed → corned','盐粒处理过 → 盐腌的']],
 'corned beef 盐腌牛肉，a corned beef sandwich 盐腌牛肉三明治。先掌握这个固定食品搭配。',
 'corned beef；corned beef sandwiches；sliced corned beef。',
 'corned beef 盐腌牛肉，beef with corn 才明确牛肉配玉米；cornstarch 玉米淀粉又接现代玉米义。',
 ('The café serves corned beef sandwiches.','咖啡馆供应盐腌牛肉三明治。'),('She sliced the corned beef for lunch.','她把盐腌牛肉切片准备午饭。'),sources=['https://www.etymonline.com/word/corn','https://en.wiktionary.org/wiki/corned#English'])
W('cornstarch','英 /ˈkɔːnstɑːtʃ/；美 /ˈkɔːrnstɑːrtʃ/','玉米淀粉',
 '从玉米里取得的淀粉，常用来让酱汁变稠；不是磨完整玉米粒得到的所有粉。',
 'corn 玉米 + starch 淀粉，接玉米义。名称说明来源和材料类别，不表示每种 corn flour 在所有地区都同一种粉。',C('corn + starch → cornstarch','来自玉米的淀粉'),
 'thicken with cornstarch 用玉米淀粉勾芡，a cornstarch mixture 玉米淀粉混合物。英式 cornflour 常对应这个材料。',
 'thicken with cornstarch；a cornstarch mixture；cornstarch slurry。',
 'cornstarch 淀粉，cornmeal 通常玉米磨成的粉粒；英美 cornflour/corn flour 的常用所指有差异，食谱先看地区和材料说明。',
 ('Mix the cornstarch with a little cold water.','把玉米淀粉与一点冷水混合。'),('The sauce thickened after she added the cornstarch mixture.','她加了玉米淀粉混合物后，酱汁变稠了。'))
W('cornmeal','英 /ˈkɔːnmiːl/；美 /ˈkɔːrnmiːl/','玉米粉；磨碎的玉米颗粒',
 '把玉米磨成粉粒，用来做粥、面包等；粗细可不同，不等于纯淀粉。',
 'corn 玉米 + meal 磨碎谷物的粉。meal 在这里不是一次早饭、午饭的餐义。',C('corn + meal〔谷物粉〕→ cornmeal','磨成粉粒的玉米'),
 'coarse cornmeal 粗玉米粉，fine cornmeal 细玉米粉，cornmeal bread 玉米粉面包。',
 'coarse cornmeal；fine cornmeal；cornmeal bread。',
 'cornmeal 粉粒取全粒等加工材料背景，cornstarch 主要淀粉；不能只看中文都带粉就任意互换食谱材料。',
 ('The recipe calls for fine cornmeal.','食谱要求用细玉米粉。'),('She dusted the tray with cornmeal.','她在烤盘上撒了一层玉米粉。'))
W('cornflower','英 /ˈkɔːnflaʊə/；美 /ˈkɔːrnflaʊər/','矢车菊；矢车菊蓝〔修饰用法〕',
 '常见蓝花、过去可长在谷物田里的植物；不是玉米穗顶上开的那种花。',
 'corn 谷物 + flower 花，接旧谷物田背景。颜色名称 cornflower blue 借这种花的蓝色，不从玉米黄色推。',CO[:1]+[['corn〔谷物〕+ flower → cornflower','谷物田相关花名 → 矢车菊；颜色比喻']],
 'blue cornflowers 蓝色矢车菊，cornflower blue 矢车菊蓝。',
 'blue cornflowers；cornflower blue；a field of cornflowers。',
 'cornflower 花与 cornflour 玉米淀粉在不少口音同音，拼写和物品不同；一个 flower 花，一个 flour 粉。',
 ('Blue cornflowers grew at the edge of the field.','田边长着蓝色矢车菊。'),('She chose a cornflower blue dress.','她选了一条矢车菊蓝连衣裙。'))
R('B3694','谷粒、谷物与地区玉米义；盐粒和小称保留','CORN：先是谷粒，现代美式常指玉米','已有 corn 先读，kernel 旧小称，corny 俚义、corned 盐粒义分开；cornstarch/cornmeal/cornflower 比材料与花。cornfield、peppercorn 共享。',
 '常用 corner 角落来自角、突出点词系，不是这一组谷物加 -er；不沿用自动归族。cornish、cornhole 等本轮略。',
 '旧 corn 同族词干 + -el → kernel；corn + -y/-ed/starch/meal/flower/field；pepper + corn。',
 [['谷粒、颗粒和旧义','corn · kernel · peppercorn · corned'],['玉米材料与谷物田','cornstarch · cornmeal · cornflower · cornfield'],['口语评价','corny']],
 'corn 地区所指不同；corned 盐粒不等于玉米；cornstarch/cornmeal 不是一种粉；cornflower/cornflour 常同音。',
 'The recipe uses cornmeal, while the sauce needs cornstarch.\n\n食谱用玉米粉，酱汁则需要玉米淀粉。',
 'corn kernel peppercorn corned cornstarch cornmeal cornflower cornfield corny')
ROOTS[-1]['exclude']['corner']='常用角落、拐角义接法语角、拉丁 cornu 角，不是谷物 corn + -er；另有罕见谷物工人同形词，本页暂略。'
RI=[['古英语 rīċe → 中古英语 riche → rich','有权势、强大、地位高、富有；又受法语同族形式影响'],['现代 rich','有钱；资源、味道、颜色、内容丰厚；反讽真好意思等用法']]
W('rich','/rɪtʃ/','富有的；丰富、富含的；浓郁、浓厚的',
 '不只是钱多：食物味厚、颜色深、文化内容多，都像里面装着充足的东西。',
 '继承古英语 rīċe 权势大、富有等，远接日耳曼王权、强大词系，法语同族词也有影响。后发展为内容、味道等丰厚，不把所有 rich 都译成昂贵。',RI,
 'a rich family 富裕家庭，rich in history 历史丰富，a rich sauce 浓郁酱汁，rich colours 浓厚鲜明的色彩。That’s rich! 可反讽你还真好意思说。',
 'a rich family；rich in；a rich sauce；rich colours。',
 'rich 丰厚，expensive 昂贵；便宜食材也可做 rich sauce。rich in 后说明富含什么，不是 fixed richer than 的同一结构。',
 ('The region is rich in history.','这个地区历史底蕴丰富。'),('The cake has a rich chocolate flavour.','蛋糕有浓郁巧克力味。'))
W('richness','/ˈrɪtʃnəs/','丰富；浓郁、浓厚；富足',
 '把 rich 里面那种充足、层次多、味道厚的感觉提出来说，不只统计银行余额。',
 'rich + -ness，中古英语 richenesse 等旧形式延续。随对象可文化丰富、滋味浓厚或物质富足。',RI+[['中古英语 richenesse → richness','丰厚、富足的性质；现代 rich + -ness 对应']],
 'the richness of the culture 文化丰富性，the richness of the sauce 酱汁浓郁度，a richness of detail 丰富细节。',
 'the richness of；a richness of detail；cultural richness。',
 'richness 性质、丰富程度，riches 多指财富、珍贵资源；The richness of a story 不只是作者赚了多少钱。',
 ('The novel is admired for its richness of detail.','小说因细节丰富而受到赞赏。'),('A little cream adds richness to the sauce.','加一点奶油会让酱汁更浓郁。'))
W('richly','/ˈrɪtʃli/','丰富、华丽地；浓郁地；充分、非常〔某些搭配〕',
 '装饰堆出丰富层次，味道做得浓厚；richly deserved 则是强调确实很应得。',
 'rich + -ly，古英语 rīċlīce 等副词已有。现代随 rich 的丰富、富厚支线分义，不能只按有钱地翻译。',RI+[['古英语 rīċlīce → richly','富厚、充足地；后有程度加强用法']],
 'richly decorated 装饰华丽，richly detailed 细节丰富，richly deserved 完全应得、实至名归。',
 'richly decorated；richly detailed；richly deserved。',
 'richly deserved 夸奖励应得，不表示奖金金额大；richly 描述程度，wealthily 更直观关联财富却不常用于这些搭配。',
 ('The ceiling was richly decorated.','天花板装饰得十分华丽。'),('The award was richly deserved.','这个奖项实至名归。'))
R('B3917','权势、富有背景到内容丰厚、味浓色深','RICH：里面很丰厚，不只钱包丰厚','rich → richness、richly；每个词用钱之外的例子说明，减少只会背富有一个义。',
 '旧权势和财富关联发展到丰富程度。食物 rich 不一定价格贵，文化 richness 也不是文化机构有钱。',
 'rich + -ness/-ly；rich in + 所富含的东西；比较 richer、richest。',
 [['丰厚性质、名词和方式程度','rich · richness · richly']],
 'rich 不等于 expensive；richness 丰富特质、riches 财富；richly deserved 是实至名归。',
 'The richly detailed story reveals the richness of local life.\n\n这个细节丰富的故事展现了当地生活的多彩。',
 'rich richness richly')
if __name__=='__main__':save('continuation_20261030_bq',ROOTS,WORDS)
