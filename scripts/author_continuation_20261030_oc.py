"""Scum, algebra, conditions, hawks, repayment, loaded historical terms, correlation and coupons."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()

Sc=[['中古荷兰、低地德语 schume 等泡沫词 → 中古英语 scum 等','浮在液面上的泡沫、浮渣'],['scum → 脏污浮层；用来骂人的强贬称；+ -y','有浮渣的；卑劣、不体面的评价']]
W('scum','/skʌm/','浮渣、污膜；〔辱骂〕人渣；撇去浮渣',
 '汤、水、液体表面漂着一层要撇掉的东西，是 scum 的实物画面。用来骂人则把这种污渣的厌恶感转给人，语气很强。',
 '借中古荷兰、低地德语等 schume 泡沫材料，经中古英语 scum、skum 等延续。浮层、杂质义又带出低劣人物的侮辱比喻，名词也可作撇渣动词。',Sc,
 'a layer of scum 一层浮渣；skim off the scum 撇去浮渣；soap scum 皂垢。',
 'a layer of scum；soap scum。',
 'foam 中性说泡沫，scum 常突出不想要的浮层、残留；称人为 scum 带强烈贬斥。',
 ('A thin layer of scum floated on the pond.','池塘上漂着一层薄薄的浮膜。'),('She wiped the soap scum from the basin.','她把洗脸盆上的皂垢擦掉。'))
W('scummy','/ˈskʌmi/','有浮渣、污膜的；〔口语〕卑劣、龌龊的',
 'scummy water 是浮着污膜的水；a scummy trick 则是让人觉得卑劣的伎俩。一个看液面，一个借脏污厌恶感评价做法。',
 'scum + -y，双写 m → scummy。由有浮渣、污膜的性质扩展到卑劣、令人厌恶的道德评价。',Sc[:1]+[['scum + -y → scummy','浮渣覆盖 → 低劣、不体面的']],
 'scummy water 有浮膜的水；a scummy trick 卑劣伎俩。语气通常随意且负面。',
 'scummy water；a scummy trick。',
 'scummy 的人物、行为评价很主观；它不是一般 untidy 不整齐的中性同义词。',
 ('The old bucket held scummy water.','旧桶里盛着浮有污膜的水。'),('He thought it was a scummy way to win.','他觉得用这种方式获胜很卑劣。'))
R('B3548','液面浮层、残留物与厌恶评价，派生词各有强度','SCUM：浮在上面的杂质，再借去骂低劣的人或做法','scum → scummy、scumbag，后两者的人物、行为用法常带明显贬斥。',
 '先看池面浮层、皂垢的实物，再看厌恶感怎样进入评价。不是每一团泡沫都要用 scum，中性泡沫常用 foam。',
 'schume 等 → scum；双写 m + -y → scummy；scumbag 的人物骂法另见基础词条。',
 [['浮渣、污膜与强贬评价','scum · scummy · scumbag']],
 'foam 可中性，scum 常嫌杂质；scumbag 是强贬人物称呼，不能当普通人称。',
 'Scum floated on the scummy water.\n\n浮有污膜的水面上漂着浮渣。','scum scummy scumbag')

Al=[['阿拉伯语 al-jabr 补全、恢复，进入早期算书名','al- 是定冠词，jabr 接恢复、使完整的词根'],['中世纪拉丁语 algebra → 英语 algebra','方程操作名称走向代数学科名；+ -ic → algebraic']]
W('algebra','/ˈældʒɪbrə/','代数、代数学',
 '先把不知道的数留成 x，用已知关系把它解出来，是学校代数最容易抓的入口。更高层的 algebra 还研究运算结构，不能只缩成做含 x 的题。',
 '借中世纪拉丁语 algebra，上接阿拉伯语 al-jabr 补全、恢复，出现在花拉子米有关补全、平衡计算的算书名中。名称由整理方程的方法走向学科。',Al,
 'elementary algebra 初等代数；linear algebra 线性代数；abstract algebra 抽象代数。',
 'elementary algebra；linear algebra。',
 'algebra 与 algorithm 算法历史上同联系花拉子米相关著作传播，但前者来自术语，后者来自人名形式，不能说是同一词的后缀变化。',
 ('In algebra, x can stand for an unknown quantity.','在代数中，x 可以代表未知量。'),('She is taking a course in linear algebra.','她在上线性代数课。'),sources=['https://en.wiktionary.org/wiki/algebra#English','https://www.etymonline.com/word/algebra'])
W('algebraic','/ˌældʒɪˈbreɪɪk/','代数的；代数形式的',
 '把文字关系写成符号与运算的式子，是 algebraic expression 的典型场景。algebra 是学科，algebraic 则说方法、表达式具有代数性质。',
 '部分由 algebra + -ic，部分经法语 algebrique 等相应形式。现代词形去末尾 a 接 -ic → algebraic，重音转到 /breɪ/。',Al+[['algebra 的词干 + -ic／法语对应形式 → algebraic','代数相关性质，重音随派生变化']],
 'an algebraic expression 代数式；an algebraic equation 代数方程；an algebraic method 代数方法。',
 'an algebraic expression；an algebraic method。',
 'algebraic 在高等数学里还有专门意义，不能把每个场景都简化为有字母的算式。',
 ('Write the relationship as an algebraic expression.','把这个关系写成代数式。'),('The teacher explained an algebraic method for solving the problem.','老师解释了一个解决问题的代数方法。'))
R('B3330','补全、恢复的算书术语走向代数学科，形容词再派生','ALGEBRA：把已知关系写清楚，让未知量有办法求','algebra → algebraic，学科名与相关方法、表达式的性质分开。',
 '初等学习可以从 x 与方程进入，历史名称则来自阿拉伯补全、恢复术语。现代抽象代数范围更广，不把一个入门画面当作全部定义。',
 'al-jabr → 拉丁 algebra → 英语 algebra；去 a 的词干接 -ic，亦有法语对应影响。',
 [['代数学科与相应性质','algebra · algebraic']],
 'algebra 术语与 algorithm 人名借词不同；algebraic 的重音与 algebra 不同。',
 'The algebra lesson begins with a simple algebraic expression.\n\n代数课从一个简单代数式开始。','algebra algebraic')

Cn=[['condition 条件 → conditional','以相应条件为前提的性质'],['conditional + -ly → conditionally','在满足所列条件时，带条件地']]
W('conditionally','/kənˈdɪʃənəli/','有条件地；在某些条件下',
 '先给一个可以，但前面还有“只要……”，就是 conditionally。条件满足才继续成立，所以不是一句不附带要求的 yes。',
 'conditional + -ly → conditionally，原词末 l 再接 -ly，拼写 ll。副词把以条件为前提的性质放进批准、接受、成立等动作。',Cn,
 'conditionally accepted 有条件接收；conditionally approved 有条件批准；conditionally true 在特定条件下成立。',
 'conditionally accepted；conditionally approved。',
 'conditionally 与 unconditionally 相反；前者需看附带条件，而不是程度上有一点批准。',
 ('The proposal was conditionally accepted.','提案被有条件接收。'),('The result is conditionally true under the stated assumptions.','在列明假设下，这个结论有条件地成立。'))
R('B2621','条件作为前提，副词与否定说明是否附带要求','CONDITIONAL：这件事成立，但先得满足那件事','conditional → conditionally、unconditional、conditionality，性质、方式、否定与抽象名词分开。',
 '批准、数学结论、关系表达都可能有条件。词先说明依赖结构，具体门槛再由 if、under、provided 等上下文交代。',
 'condition + -al → conditional；-ly 方式；un- 否定条件性；-ity 抽象性质。',
 [['条件性质、方式与抽象名词','conditional · conditionally · conditionality'],['不附条件','unconditional']],
 'conditionally 不是批准程度低一点，而是附有前提；unconditional 则否定这层条件限制。',
 'The conditional offer was accepted conditionally, after the details were clarified.\n\n细节澄清后，那份附带条件的提议被有条件地接受。','conditional conditionally conditionality unconditional')

Ha=[['古英语 hafoc → 中古英语 hauk、hawke 等 → hawk 鹰','猛禽名，后来借作强硬立场人物'],['叫卖 hawk 由 hawker 回构，接低地德语贩售词；night、-ish 限定','同形动词分源；夜鹰名、夜猫子、鹰派性质']]
W('hawk','英 /hɔːk/；美 /hɔːk/','鹰；鹰派人物；叫卖、兜售',
 '天空里盘旋抓猎物的鹰，是 hawk。立场强硬、倾向对抗的人又借名为 hawk；街上 hawk goods 却是叫卖商品，来源另有商贩词族。',
 '鸟名承古英语 hafoc，经中古英语相关形式延续；强硬人物义借猛禽形象，与 dove 鸽派对照。叫卖动词由 hawker 回构，接低地德语贩售材料，不来自鹰卖东西的故事。',Ha,
 'watch like a hawk 紧盯；a political hawk 政治鹰派；hawk goods in the street 沿街叫卖商品。',
 'watch like a hawk；hawk goods。',
 'hawk 的叫卖义与鸟名近源不同；政治 hawk 是立场比喻，不按外貌认人。',
 ('A hawk circled above the field.','一只鹰在田野上方盘旋。'),('Vendors hawked their goods near the station.','小贩在车站附近叫卖商品。'),sources=['https://en.wiktionary.org/wiki/hawk#English','https://www.etymonline.com/word/hawk'])
W('nighthawk','英 /ˈnaɪthɔːk/；美 /ˈnaɪthɔːk/','夜鹰；〔口语〕夜猫子',
 'night 把画面移到夜间，nighthawk 是夜鹰等鸟的名称，也借指晚上、凌晨还精神十足的人。夜猫子义不是真的长出鹰的眼睛。',
 'night + hawk，形成鸟类通名，再用于夜间活动者。典型夜鹰属于夜鹰科等相应鸟类，并不是白天 hawk 类猛禽简单换了作息。',Ha[:1]+[['night + hawk → nighthawk','夜间活动鸟名 → 夜里常醒着活动的人']],
 'a common nighthawk 北美常见夜鹰的名称；a natural nighthawk 天生夜猫子。',
 'a nighthawk；a natural nighthawk。',
 'night owl、nighthawk 都可口语说夜猫子；鸟的具体分类不能由复合字面代替。',
 ('A nighthawk flew over the rooftops at dusk.','黄昏时，一只夜鹰飞过屋顶。'),('As a nighthawk, she preferred writing after midnight.','她是个夜猫子，喜欢午夜以后写作。'))
W('hawkish','英 /ˈhɔːkɪʃ/；美 /ˈhɔːkɪʃ/','像鹰的；鹰派的、强硬的',
 'hawk 是强硬派人物，hawkish 说言论、立场表现出这种强硬倾向。新闻里可以谈外交，也可谈偏向抑制通胀、收紧货币条件的态度，具体看议题。',
 'hawk + -ish → hawkish，性质形容词从鹰般外形、行为扩展到政治及其他政策立场。-ish 在这里说像、具有倾向，不只是稍微一点。',Ha[:1]+[['hawk + -ish → hawkish','鹰般的 → 政策立场强硬、偏收紧的']],
 'a hawkish stance 鹰派立场；a hawkish speech 强硬讲话；hawkish rhetoric 鹰派言论。',
 'a hawkish stance；hawkish rhetoric。',
 'hawkish 必须看议题；货币政策的鹰派不表示实际军事行动，反义常见 dovish。',
 ('The editorial criticised the minister’s hawkish rhetoric.','社论批评那位部长的鹰派言论。'),('The report described the speech as hawkish.','报告把讲话描述为立场偏鹰派。'))
R('B3430','猛禽名走向强硬立场，叫卖动词另有商贩来源','HAWK：鸟在空中盯猎物，政策比喻借强硬形象','hawk → hawkish、nighthawk；叫卖 hawk 保留独立的词源说明。',
 '立场人物与性质通过鸟的形象连接，夜猫子通过夜间活动连接；街头叫卖则是商贩动词，不编成鸟的拟人动作。',
 'hafoc → hauk、hawke → hawk；-ish 性质；night + hawk；hawk 叫卖由 hawker 回构。',
 [['鹰名与强硬立场','hawk · hawkish'],['夜鹰与夜猫子','nighthawk']],
 'nighthawk 的鸟类身份不由字面决定；hawkish 货币立场与军事立场按议题分开。',
 'The nighthawk read a hawkish editorial late at night.\n\n那位夜猫子深夜读着一篇鹰派社论。','hawk hawkish nighthawk')

Rp=[['re- 回、再 + pay → repay；repayment','还回钱、报偿；相应动作名词'],['repay + -able → repayable','可以偿还，或约定应偿还']]
W('repayable','/rɪˈpeɪəbəl/','可偿还的；须偿还的',
 'repayable 不只有“有能力还”，还常说一笔款按安排需要还。a repayable grant 就把通常像资助的钱，限定成要归还的形式。',
 'repay + -able，保留 y → repayable。-able 既可表达可被偿还的可能，也能在款项描述中表达须按约偿还的性质。',Rp,
 'a repayable amount 可偿还、须还款项；repayable over five years 在五年内分期偿还；repayable on demand 应要求偿还。',
 'repayable over；repayable on demand。',
 '-able 不在每个固定财务描述中只表示能够；repayable 可含须偿还的约定含义，具体看句子。',
 ('The loan is repayable over five years.','这笔贷款须在五年内偿还。'),('The document states which amounts are repayable.','文件列明哪些款项须归还。'))
R('B2959','还回、报偿的动作，名词与可还、须还性质','REPAY：收到的款、恩情等，以相应方式还回去','repay → repayment、repayable，动作、还款事件与性质按顺序读。',
 '钱可还回，帮助可报答；repayment 常用于款项，repayable 再看是否须还、可还。前缀在这里有回返意义，不只是再付一次。',
 're- 回、再 + pay；-ment 动作、结果；-able 相应可还、须还性质。',
 [['偿还动作、还款与应还性质','repay · repayment · repayable']],
 'repay 的 re- 可说还回；repayable 不总只是能力，也可能说明约定须还。',
 'The agreement explains when repayment is due and how much is repayable.\n\n协议说明何时还款，以及须还多少。','repay repayment repayable')

Wh=[['古英语 hore → 中古英语 hore → whore','性服务、性道德评价中的旧人物称呼'],['wh- 拼写后来形成；whore + house → whorehouse','w 现代不发音；场所名接人物活动']]
W('whore','英 /hɔː/；美 /hɔːr/','妓女〔粗俗、贬称〕；淫荡者〔辱骂〕；出卖原则的人〔贬〕',
 '这是带强烈贬意的旧称，也常被用来羞辱女性的性行为。阅读小说、争吵、历史材料时要认出它的攻击性，不能当作中性的职业称呼。',
 '承古英语 hore、中古英语 hore，上接日耳曼同族词，更远与欲求、喜爱材料相联系。后来的 wh- 拼写并不表示现代要读 /w/；人物贬称又扩展到为利益出卖原则的人。',Wh,
 'call someone a whore 用这个词辱骂某人；the insult whore 这个辱称。较中性的职业描述会依语境用 sex worker 等表达。',
 'the insult whore；call someone a whore。',
 'whore 的 w 不读，不与 who /huː/ 同音；它的侮辱力度也是词义的一部分。',
 ('The novel shows how the insult “whore” was used to shame women.','小说写出人们怎样用 whore 这个辱称羞辱女性。'),('The glossary marks whore as an offensive term.','词汇表把 whore 标为冒犯性用语。'))
W('whorehouse','英 /ˈhɔːhaʊs/；美 /ˈhɔːrhaʊs/','妓院〔粗俗或贬称〕',
 '人物称呼 whore 加 house，按活动、人员命名场所。这个词仍带前半的粗俗色彩，历史、小说叙述中常见。',
 '承中古英语 horehous，对应 whore + house。复合结构透明，但使用语气不因此变成中性。',Wh[:1]+[['whore + house → whorehouse','以相关人物、活动命名场所']],
 'an old whorehouse 旧妓院；a former whorehouse 曾作妓院的房子，常出现在历史描述。',
 'a former whorehouse；an old whorehouse。',
 'brothel 也指妓院，通常比 whorehouse 更中性、正式；两词所指相近，语气不同。',
 ('The historian identified the building as a former whorehouse.','历史学者指出，这栋建筑过去是一家妓院。'),('The novel uses whorehouse as a deliberately coarse word.','小说故意用 whorehouse 这个粗俗场所称呼。'))
R('B3445','人物旧称与粗俗贬称，复合场所名保留语气','WHORE：认出所指，也认出它带来的侮辱语气','whore → whorehouse，人物称呼与场所名分别识别。',
 '学习阅读需要明白粗俗、贬义本身就是词义信息。现代拼写还有不发音的 w，不能照 who 的字形猜读。',
 'hore → whore，现代 w 不发音；whore + house → whorehouse。',
 [['人物贬称与场所名','whore · whorehouse']],
 'whore 不是中性职业词；whorehouse 与 brothel 所指相近，语体力度不同。',
 'The dictionary distinguishes the neutral description from the insult whore.\n\n词典区分中性描述与 whore 这个辱称。','whore whorehouse')

Cr=[['法语 correlation，接共同关联的拉丁材料 → correlation','相互关系；现代可对应 correlate + -ion'],['auto- 自己 + correlation → autocorrelation','把一条序列与自己的滞后版本比较']]
W('correlation','英 /ˌkɒrəˈleɪʃən/；美 /ˌkɔːrəˈleɪʃən/','相关、关联；相关程度',
 '一组数据变大时，另一组也常跟着变，或常朝相反方向变，可能有 correlation。它说变化模式联系，并不直接告诉你是谁让谁变。',
 '借法语 correlation，上接共同关联的词族，现代与 correlate + -ion 对应。一般相互关系义在统计中发展为衡量关联方向、强弱的用法。',Cr,
 'a correlation between A and B 两者之间的相关；a positive correlation 正相关；a negative correlation 负相关；correlation does not establish causation 相关本身不能确立因果。',
 'a correlation between；a positive correlation。',
 '负相关仍是相关；常见 Pearson 指标偏线性关联，接近零不自动排除其他关系。',
 ('The study found a correlation between the two measurements.','研究发现两项测量之间存在相关。'),('The chart shows a negative correlation between the variables.','图表显示变量之间存在负相关。'),sources=['https://en.wiktionary.org/wiki/correlation#English','https://mathworld.wolfram.com/CorrelationAnalysis.html'])
W('autocorrelation','英 /ˌɔːtəʊkɒrəˈleɪʃən/；美 /ˌɔːtoʊkɔːrəˈleɪʃən/','自相关',
 '把同一段记录复制一份，向后错开一点，再看两份是否仍有相似起伏，就是 autocorrelation 的直观入口。不是两种不同变量，而是同一变量跨时间等间隔的联系。',
 'auto- 自己 + correlation 相关。信号、时间序列分析按与自身滞后版本的关联命名，错开的间隔称 lag。',Cr[:1]+[['auto- + correlation → autocorrelation','同一记录与自身滞后版本的相关']],
 'serial autocorrelation 序列自相关；autocorrelation at a lag 某滞后间隔的自相关；an autocorrelation plot 自相关图。',
 'an autocorrelation plot；autocorrelation at a lag。',
 'auto- 在这里是自己，不是自动完成；自相关也不是随便把一组数与完全同位置的自己比较。',
 ('The analyst checked the series for autocorrelation.','分析人员检查了序列是否存在自相关。'),('The autocorrelation plot revealed a repeating pattern.','自相关图显示出一种重复模式。'),sources=['https://en.wiktionary.org/wiki/autocorrelation#English','https://www.itl.nist.gov/div898/handbook/eda/section3/eda35c.htm'])
R('B3922','一同或反向变动的关联，自相关把比较对象转回自己','CORRELATION：先看一起怎么变，再问是不同记录还是自己','correlation → autocorrelation，后者用 auto- 限定为与自身不同位置、时间的关联。',
 '同时起伏不自动说明因果，反向起伏也可有强相关。自相关把同一条记录错开来比较，帮助看重复与持续性。',
 'correlation 经法语、拉丁相关材料；现代 correlate 的名词对应；auto- 自己。',
 [['关联与自身滞后关联','correlation · autocorrelation']],
 '相关不直接确立因果；auto- 自己不等于自动。',
 'The report first measured correlation between two series, then autocorrelation within each series.\n\n报告先测两条序列之间的相关，再测各自内部的自相关。','correlation autocorrelation')

Cp=[['法语 couper 切 → coupon 切下的一段、票券','票据的一部分可剪下去兑换相应权利'],['coupon → 优惠券、票息；+ -ing','从纸券延伸数字券；使用、收集优惠券的活动']]
W('coupon','英 /ˈkuːpɒn/；美 /ˈkuːpɑːn/，美式也常读 /ˈkjuːpɑːn/','优惠券、兑换券；债券票息',
 '从报纸剪下一小块，凭它换折扣，是 coupon 的老画面。今天手机里的券也沿用名称；债券票息则保留了早期剪息票领取利息的历史。',
 '借法语 coupon，上接 couper 切。切下的一段票据发展为可兑换优惠、服务的凭证；金融票息名称从纸质息票延续，现代不必真的剪纸。',Cp,
 'a discount coupon 优惠券；redeem a coupon 兑用券；a coupon code 优惠码；a bond coupon 债券票息。',
 'a discount coupon；redeem a coupon；a coupon code。',
 'coupon 的券面资格、金额、条件要看具体文本；票息义不是商店打折，不能只按优惠一词翻。',
 ('She used a coupon to get a discount.','她用优惠券获得折扣。'),('The checkout page has a box for a coupon code.','结账页有一个输入优惠码的框。'))
W('couponing','英 /ˈkuːpɒnɪŋ/；美 /ˈkuːpɑːnɪŋ/','收集、使用优惠券；优惠券活动',
 '有意识地找券、整理券，再购物时用上，不是偶然见到一张券，这类活动常叫 couponing。也可在商业语境说发券、优惠券促销。',
 'coupon + -ing → couponing，coupon 名词可转作使用优惠券的动词，-ing 再形成活动名。',Cp[:1]+[['coupon + -ing → couponing','使用、收集或发放优惠券的活动']],
 'digital couponing 数字优惠券活动；couponing habits 用券习惯；a couponing app 用券应用。',
 'digital couponing；couponing habits。',
 'couponing 是活动，coupon 是券本身；有券不代表每次购买都一定省到钱，实际效果看条件。',
 ('The article discusses digital couponing.','文章讨论数字优惠券的使用。'),('She keeps a folder for her couponing activities.','她专门用一个文件夹整理用券资料。'))
R('B3825','切下的票券换权益，数字券与票息继续沿用旧名','COUPON：剪下一段作凭证，今天也可以只是手机里的代码','coupon → couponing，从物件、权益凭证到用券活动。',
 '纸券的切割形象提供起点，数字形式保留功能而不保留剪刀。票息也从可剪下兑领的息票转为利息支付名称。',
 'couper 切 → coupon；coupon + -ing → couponing。',
 [['优惠券、票息与用券活动','coupon · couponing']],
 'coupon 可是票息，不只购物折扣；couponing 是使用、收集等活动。',
 'Her digital couponing began with a single coupon code.\n\n她从一个优惠码开始学着使用数字优惠券。','coupon couponing')

if __name__=='__main__':save('continuation_20261030_oc',ROOTS,WORDS)
