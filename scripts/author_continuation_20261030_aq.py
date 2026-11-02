"""Shops and materials: familiar scenes, distinct abstractions and honest histories."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
SH=[['中古英语 shoppe；与古英语 sċoppa 等棚舍词相关','棚、摊位、做工或交易的地方；旧词细义有不确定处'],['现代 shop','商店、工场；由店铺名词发展购物动词']]
def S(f,m):return SH+[[f,m]]
W('shop','英 /ʃɒp/；美 /ʃɑːp/','商店；工场；购物',
 '先是能做工、卖东西的一处地方；再把去店里看、挑、买这个活动叫 shop。',
 '接中古英语 shoppe，与古英语及日耳曼同族的棚舍词相关；旧词具体含义有不确定处，本文不硬补远古建筑故事。动词由商店名词形成。',SH,
 'a small shop 小店，shop online 网购，shop around 多看几家比较。repair shop 修理铺，talk shop 大谈本行业工作。',
 'a small shop；shop online；shop around；talk shop。',
 'shop 浏览、挑选、购买的过程，不保证最后买到；buy 直接说买下。shop 也有工场义，不能每次都译零售商店。',
 ('We shopped around before choosing a new sofa.','我们比较了几家后才选定新沙发。'),('The bike is still at the repair shop.','自行车还在修理铺。'))
W('shopping','英 /ˈʃɒpɪŋ/；美 /ˈʃɑːpɪŋ/','购物；买来的东西',
 '逛、挑、买这一整段活动；回家说把 shopping 放下，也可指刚买的东西。',
 'shop 双写 p + -ing。既可活动名词，也可借指购得物，不能见 -ing 就只翻正在。',S('shop + -ing → shopping','购物活动；购得的物品'),
 'go shopping 去购物，do the shopping 采购，carry the shopping 提着买来的东西。',
 'go shopping；do the shopping；a shopping list；online shopping。',
 'shopping 通常不可数；a shop 是店，a shopper 是购物者。go shopping 不需要在 shopping 前另加 to。',
 ('I do the grocery shopping on Saturday mornings.','我在周六早上采购食品杂货。'),('He put the shopping on the kitchen table.','他把买来的东西放到厨房桌上。'))
W('shopper','英 /ˈʃɒpə/；美 /ˈʃɑːpər/','购物者；顾客',
 '站在买东西这一边的人，可以正在逛，也可以已经买了；不按开什么店来命名。',
 'shop + -er，词尾前双写 p。后缀称呼做购物活动的人。',S('shop + -er → shopper','购物活动的参与者'),
 'online shoppers 网购者，a regular shopper 常来的购物者，a mystery shopper 暗访购物者。',
 'online shoppers；a regular shopper；a mystery shopper。',
 'shopper 来挑买，shopkeeper 经营店铺；customer 顾客范围还包括各种服务，不只购物。',
 ('The website helps shoppers compare prices.','这个网站帮助购物者比价。'),('Early shoppers found the store unusually quiet.','早来的顾客发现店里格外安静。'))
W('shopkeeper','英 /ˈʃɒpkiːpə/；美 /ˈʃɑːpkiːpər/','店主；经营店铺的人',
 '负责把店经营起来的人，重点是守着、管着这门生意。',
 'shop + keeper，keeper 接 keep 管理、照料。不是单纯站在门口看守，也不保证每位临时店员都算店主。',S('shop + keeper → shopkeeper','经营、管理店铺的人'),
 'a local shopkeeper 当地店主，a small shopkeeper 小店经营者。常见于谈社区、零售生意。',
 'a local shopkeeper；a small shopkeeper；talk to the shopkeeper。',
 'shopkeeper 经营者，shop assistant 店员，shopper 顾客；把三者放进同一家店就容易分清。',
 ('The shopkeeper knew most of her customers by name.','店主叫得出大多数顾客的名字。'),('Local shopkeepers agreed to stay open later.','当地店主同意延长营业时间。'))
W('shoplift','英 /ˈʃɒplɪft/；美 /ˈʃɑːplɪft/','在商店行窃、偷拿商品',
 '假装正常购物，却把商品偷走；lift 在这里取偷的旧俚义。',
 '可认出 shop + lift 偷，但现代动词由较早 shoplifting、shoplifter 等词逆构。不能按现代短词更简单，就断言动词一定先出生。',S('较早 shoplifter、shoplifting 等 → shoplift〔动词〕','商店行窃者、行为 → 对应动词'),
 'be caught shoplifting 行窃时被发现，shoplift goods 偷拿商品；不要按抬高店铺逐字理解。',
 'be caught shoplifting；shoplift goods；attempt to shoplift。',
 'shoplift 在店内偷商品，rob 更常以被抢的人、地方作对象；不是把任何偷东西都机械叫 shoplift。',
 ('The character is caught trying to shoplift a watch.','故事中的人物试图偷拿手表时被发现。'),('The film shows why the teenager began to shoplift.','影片展现了这个少年为什么开始在商店行窃。'),sources=['https://www.etymonline.com/word/shoplift','https://en.wiktionary.org/wiki/shoplift#English'])
W('shoplifting','英 /ˈʃɒplɪftɪŋ/；美 /ˈʃɑːplɪftɪŋ/','商店行窃；偷拿店内商品的行为',
 '这次不说哪个人，而是把商店偷拿商品这种行为作为一件事来谈。',
 '现代对应 shoplift + -ing，但行为名词的记录早于现代动词；它和 shoplifter 等旧形式相关，动词后来逆构。',S('较早 shoplifting〔名词〕；后有动词 shoplift','店内行窃行为；现代可按动词加 -ing 认形'),
 'prevent shoplifting 防范店内行窃，an increase in shoplifting 店内行窃增多；通常不可数。',
 'prevent shoplifting；an increase in shoplifting；shoplifting incidents。',
 'shoplifting 是行为，shoplifter 是人；历史先后与现代最方便的拆分顺序不是一回事。',
 ('The store changed its layout to reduce shoplifting.','商店调整了布局，以减少店内行窃。'),('The report discusses the rise in shoplifting.','报告讨论了店内行窃增多的情况。'))
W('shoplifter','英 /ˈʃɒplɪftə/；美 /ˈʃɑːplɪftər/','在商店行窃的人',
 '把商品偷拿走的那个人；lifter 在这里接偷窃，不是帮店搬货的工人。',
 'shop + lifter 偷窃者；这个人物词比对应现代动词 shoplift 更早有记录。现代仍可方便地与 shoplift + -er 对应。',S('shop + lifter → shoplifter','店内偷拿商品的人；早于对应现代动词'),
 'a suspected shoplifter 涉嫌店内行窃的人，catch a shoplifter 抓到店内行窃者。',
 'a suspected shoplifter；catch a shoplifter；a shoplifter in the story。',
 'shoplifter 偷拿者，shopper 正常购物者；lifter 单独在其他场景也可指举重者或提升器，要看组合。',
 ('Security staff stopped a suspected shoplifter at the exit.','安保人员在出口拦下了一名涉嫌行窃的人。'),('The novel explains how the shoplifter escaped notice.','小说解释了那个店内行窃者如何没被注意到。'))
W('pawnshop','英 /ˈpɔːnʃɒp/；美 /ˈpɔːnʃɑːp/','当铺；典当行',
 '把东西交给店作抵押换一笔钱，以后按约定赎回；名字说明店的典当业务。',
 'pawn 典当、抵押物 + shop。这里 pawn 的典当义与国际象棋里的兵分源，不是卖棋子的店。',S('pawn〔典当〕+ shop → pawnshop','经营典当业务的店铺'),
 'a local pawnshop 当地当铺，take a watch to a pawnshop 把手表拿去典当。',
 'a local pawnshop；a pawnshop window；take to a pawnshop。',
 'pawnshop 提供典当业务，secondhand shop 二手店通常侧重买卖旧货；实际店铺业务可能兼有。',
 ('He took the old watch to a pawnshop.','他把旧手表拿到当铺。'),('The pawnshop displayed guitars in its window.','当铺橱窗里摆着几把吉他。'))
W('shopaholic','英 /ˌʃɒpəˈhɒlɪk/；美 /ˌʃɑːpəˈhɔːlɪk/','购物狂；特别爱购物的人〔口语〕',
 '一逛就停不下来，别人打趣说你是购物狂；这个词常带夸张、自嘲语气。',
 'shop + -aholic，后部从 alcoholic 等词类推，表示对某活动特别上瘾、沉迷。不是酒精这个意思直接装到店里。',S('shop + 类推后缀 -aholic → shopaholic','沉迷购物的人；常作口语夸张'),
 'a self-confessed shopaholic 自称购物狂的人。一般聊天里的称呼本身不构成医学诊断。',
 'a self-confessed shopaholic；call oneself a shopaholic；a former shopaholic。',
 'shopper 中性购物者，shopaholic 强调买得多、特别沉迷；不能把每个爱逛街的人都默认有临床问题。',
 ('She jokes that she is a shopaholic whenever there is a sale.','她开玩笑说，一打折自己就成了购物狂。'),('The story follows a shopaholic trying to change her habits.','故事讲一个购物狂尝试改变自己的习惯。'))
R('B3267','店铺、工场和购物；买者、经营者与行窃者','SHOP：做工或交易的地方，后来也说购物活动','shop → shopping、shopper；shopkeeper 经营者；shoplift、shoplifting、shoplifter 连读并注明逆构；共有 workshop、bookshop、sweatshop。',
 '旧棚舍词走到交易、做工场所；别只看现代商店义。人物和行为按角色讲，生僻 topshop 等先略。',
 'shop + -ing/-er/keeper；shop + lift 偷及相关旧形式；pawn + shop；shop + -aholic。',
 [['基本场所、活动和角色','shop · shopping · shopper · shopkeeper'],['店铺类型与工场','bookshop · pawnshop · workshop · sweatshop'],['行窃及过度购物称呼','shoplift · shoplifting · shoplifter · shopaholic']],
 'shop 挑买不保证买下；shopkeeper/assistant/shopper 分角色；shoplift 动词逆构；pawn 典当不是棋兵。',
 'The shopkeeper helped the shopper carry her shopping.\n\n店主帮顾客提起买来的东西。',
 'shop shopping shopper shopkeeper bookshop pawnshop workshop sweatshop shoplift shoplifting shoplifter shopaholic')
MA=[['拉丁 māteria → 晚期拉丁 māteriālis','木材、材料、物质 → 物质的、材料的'],['法语及中古英语 → material','物质的、重要的；材料、布料、资料等用法']]
def M(f,m):return MA+[[f,m]]
W('material','英 /məˈtɪəriəl/；美 /məˈtɪriəl/','材料、布料、资料；物质的；重要、实质性的',
 '做桌子需要木料，写文章需要资料；都把它们看成用来做出东西的材料。形容词还有真正影响事情的意思。',
 '接晚期拉丁 māteriālis，来自 māteria 木材、材料、物质，经法语等传入中古英语。māteria 更远常联系 māter 母亲、来源，但不要把现代每一义都硬译成妈妈。',MA,
 'building materials 建材，reading material 阅读资料，material possessions 物质财产，a material difference 实质差异。',
 'building materials；reading material；material possessions；a material difference。',
 'material 资料不一定实体材料；形容词重要的也不等于摸得着。a material change 强调足以影响事情的改变。',
 ('The chairs are made from recycled material.','这些椅子由再生材料制成。'),('The change made no material difference to the result.','这项变化没对结果造成实质影响。'),sources=['https://www.etymonline.com/word/material','https://en.wiktionary.org/wiki/material#English'])
W('materially','英 /məˈtɪəriəli/；美 /məˈtɪriəli/','实质上、显著地；在物质方面',
 '改变大到真正影响结果，是 materially；只比较物质生活条件，也可用这个副词。',
 'material + -ly，中古英语已有对应形式。随 material 的重要、物质两路分义，不统一翻成用材料地。',M('material + -ly → materially','实质、显著地；物质方面'),
 'materially affect 显著影响，materially different 实质不同，materially comfortable 物质生活舒适。',
 'materially affect；materially different；materially better off。',
 'materially 在影响语境常近 substantially；physically 说身体上、物理上，不等于每处 materially 都可替换。',
 ('The delay did not materially affect the schedule.','延误没有对日程产生实质影响。'),('The two proposals are materially different.','两项提议存在实质差异。'))
W('materiality','英 /məˌtɪəriˈæləti/；美 /məˌtɪriˈæləti/','物质性；重要性、实质影响程度',
 '一件事是否有实体存在，或一个变化是否重要到该被认真计入；按场景看两条意思。',
 'material + -ity，形成可能参照拉丁相应名词。接 material 的物质与重要两义，不能只认一个后缀就推成材料数量。',M('material + -ity → materiality','物质存在的性质；足以产生影响的重要性'),
 'the materiality of an object 物体的物质性；报告、审计等语境 materiality 常讨论信息对判断的重要程度。',
 'assess materiality；a question of materiality；the materiality of objects。',
 'materiality 重要程度或物质性，materialism 物质主义、唯物论等立场；不是同义抽象名词。',
 ('The team assessed the materiality of the error.','团队评估了这个错误的重要程度。'),('The essay explores the materiality of handwritten books.','文章探讨手写书籍作为实物的物质特性。'))
W('materialize','英 /məˈtɪəriəlaɪz/；美 /məˈtɪriəlaɪz/','实现；出现、显现',
 '原来只是一个计划、一种期待，后来真在眼前出现了；也可说人像突然冒出来。',
 'material + -ize，使成物质形态的构词联系，后来通用于实现、出现。现代不是只说把材料加工出来。',M('material + -ize → materialize','取得实际形态 → 实现、显现'),
 'plans materialize 计划实现，an opportunity materializes 机会出现，fail to materialize 没能出现、兑现。',
 'plans materialize；fail to materialize；materialize out of nowhere。',
 'materialize 常让计划、结果、人物作主语；realize a plan 常是人实现计划。The plan materialized 与 We realized the plan 结构不同。',
 ('The promised funding never materialized.','承诺的资金始终没有到位。'),('A waiter seemed to materialize beside our table.','一位服务员像突然冒出来似的来到桌边。'))
W('immaterial','英 /ˌɪməˈtɪəriəl/；美 /ˌɪməˈtɪriəl/','无关紧要的；非物质的',
 '判断这件事时，这个细节不影响结果；另一路是在讨论没有物质形态的东西。',
 '经法语及中世纪拉丁 immāteriālis 等借入；im- 是否定 in- 在 m 前的变体，现代可认 im- + material。两义分别否定重要、物质。',MA[:1]+[['中世纪拉丁 immāteriālis → 法语及英语 immaterial','非物质的；后有无关紧要、不影响判断义']],
 'be immaterial to the decision 对决定无关紧要，whether ... is immaterial 是否……并不重要。',
 'immaterial to；it is immaterial whether；immaterial differences。',
 'immaterial 常是无关紧要，immature 未成熟是另一词。immaterial 不只是材料缺货，也不等于 impossible。',
 ('The colour is immaterial to the experiment.','颜色对这项实验无关紧要。'),('Whether he arrived first or second is immaterial.','他是第一个还是第二个到，并不重要。'))
W('materialist','英 /məˈtɪəriəlɪst/；美 /məˈtɪriəlɪst/','唯物论者；看重物质享受的人',
 '一个语境在谈世界由什么构成，另一个语境在谈人重视钱和享受；同词两种关注点要分开。',
 'material + -ist，后缀称持某立场、倾向的人。接物质概念发展哲学用法，也有日常物质至上称呼。',M('material + -ist → materialist','物质立场的持有者；日常重物质的人'),
 'a philosophical materialist 哲学上的唯物论者；日常称人 a materialist 可能带重钱物的评价。',
 'a philosophical materialist；a committed materialist；call someone a materialist。',
 '哲学 materialist 不自动等于贪钱；materialistic 日常常带过分重物质意味。先看是否在讨论哲学。',
 ('The philosopher described herself as a materialist.','这位哲学家把自己称为唯物论者。'),('The story contrasts a materialist with a man who values simple pleasures.','故事把一个看重物质的人与一个珍视简单快乐的人作了对照。'))
W('materialistic','英 /məˌtɪəriəˈlɪstɪk/；美 /məˌtɪriəˈlɪstɪk/','过分看重金钱、财物的；唯物论的〔特定语境〕',
 '评判生活总盯着买了什么、挣了多少，日常就容易被说 materialistic。',
 'material + -istic，也可结合 materialist 和形容词 -ic 认形。日常评价与哲学含义并存，不靠词尾替人判断价值观。',M('material + -istic → materialistic','物质至上的；哲学语境亦可唯物论的'),
 'a materialistic attitude 重物质的态度，a materialistic society 物质至上的社会。常带批评意味。',
 'a materialistic attitude；materialistic values；a materialistic lifestyle。',
 'material 物质的往往中性，materialistic 日常多说过分重物质；material possessions 财物不必写成 materialistic possessions。',
 ('She worried that the children were becoming too materialistic.','她担心孩子们变得太看重物质。'),('The novel criticizes the materialistic values of the city.','小说批评了城市里物质至上的价值观。'))
R('B3894','做出事物的材料；物质与实质重要两路','MATERIAL：拿来做东西的材料；也说足以影响结果','material → materially、materiality；materialize 变成现实，immaterial 否定；materialist、materialistic 最后分哲学与日常评价。',
 '拉丁木材、材料走向一般物质、资料，也有重要的含义；不要用摸得着一招解释所有句子。',
 'material + -ly/-ity/-ize/-ist/-istic；im- + material 的借入对应。',
 [['材料、重要性与程度','material · materially · materiality'],['实际出现与否定','materialize · immaterial'],['立场和价值评价','materialist · materialistic']],
 'material difference 实质差异；immaterial 无关紧要；materialist 哲学不等于贪财；materialize 主语常是计划、结果。',
 'The material change mattered, but the promised improvement never materialized.\n\n这个实质变化值得注意，但承诺的改善始终没有出现。',
 'material materially materiality materialize immaterial materialist materialistic')
if __name__=='__main__':save('continuation_20261030_aq',ROOTS,WORDS)
