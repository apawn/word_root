"""Tax, mom and quality with the qualify family kept adjacent."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
T=[['拉丁 taxāre → 法语 taxer、taxe → 英语 tax','评定、估量、征收'],['现代 tax','税；征税 → 增加负担、耗费能力']]
W('tax','/tæks/','税；征税；使承受重负',
 '先算该缴多少，再向对象征收；比喻中，一项任务也能像收税一样耗用你的耐心、精力。',
 '经法语接拉丁 taxāre 评定、估量等义。联系 tangere 触碰的更远解释常被提出，但不把推测当成现代拆词规则。',T,
 'pay tax 缴税，income tax 所得税，tax a product 对商品征税；tax someone’s patience 使耐心受到很大考验。',
 'pay tax；income tax；tax revenue；tax someone’s patience。',
 'tax 通常是政府征收，fee 常是某项服务或手续的费用；tax 的动词比喻并不表示真的向人收钱。',
 ('The price does not include tax.','价格不含税。'),('The long delay taxed everyone’s patience.','长时间的延误让所有人的耐心受到考验。'))
W('taxpayer','英 /ˈtækspeɪə/；美 /ˈtækspeɪər/','纳税人',
 '从缴税这一关系来看个人或机构，payer 是付款的一方。',
 'tax 税 + payer 支付者，payer 由 pay + -er。并非 tax + player，不多出玩耍的 l。',T+[['tax + payer → taxpayer','缴纳税款的主体 → 纳税人']],
 'individual taxpayers 个人纳税人，taxpayers’ money 纳税人的钱；可以包括公司等机构，不限定受雇员工。',
 'individual taxpayers；taxpayers’ money；the cost to taxpayers。',
 'taxpayer 纳税人，tax collector 征税人员；payer 和 collector 是支付与收取的两端。',
 ('The project will be funded with taxpayers’ money.','项目将由纳税人的钱资助。'),('The report estimates the cost to taxpayers.','报告估算了纳税人承担的成本。'))
W('taxable','/ˈtæksəbəl/','应纳税的；可征税的',
 '这部分收入、交易或财产属于计算税款的范围；具体哪些算，要按适用规则判断。',
 'tax + -able，可被征税。形容词说明纳税属性，不表示税已经付完。',T+[['tax + -able → taxable','可被征税 → 应纳税的']],
 'taxable income 应纳税收入，a taxable benefit 应税福利；词义学习不等于给出某一地区的具体征税结论。',
 'taxable income；a taxable benefit；taxable earnings。',
 'taxable 应纳税，taxed 已被征税；pretax 税前是计算阶段，不是免税。',
 ('The form asks for the amount of taxable income.','表格要求填写应纳税收入金额。'),('The guide explains which benefits are taxable.','指南说明哪些福利应纳税。'))
R('B2485','税、纳税人与应税范围','TAX：评定税款并征收，也比喻消耗精力','先学 tax 的税与负担，再接 taxpayer 支付者、taxable 可征税；已有 pretax、taxman 一起看。',
 '经法语接拉丁评定、估量词。现代 tax someone’s patience 是使耐心承受重负，并非真的征税。',
 'tax + payer → taxpayer；tax + -able → taxable；pre- → pretax；tax + man → taxman。',
 [['核心与缴纳、征收角色','tax · taxpayer · taxman'],['征税属性与计算阶段','taxable · pretax']],
 'taxable 应税不等于已付税；pretax 税前不等于免税；taxpayer 是缴税方。',
 'The taxpayer checked the taxable income on the form.\n\n纳税人核对了表上的应纳税收入。',
 'tax taxpayer taxman taxable pretax')
M=[['儿童称呼 momma 等 → mom','妈妈的亲昵称呼；儿童发音形式不能硬拆拉丁根'],['现代 mom 词族','妈妈、妈咪；step- 接继亲关系']]
W('mom','英 /mɒm/；美 /mɑːm/','妈妈',
 '日常亲近地叫母亲，尤其在美式英语常见；语气比正式 mother 更像家里的称呼。',
 '通常看作 momma 等儿童、家庭称呼的缩短形式。妈妈类称呼跨语言相似，也不能因此断定英语直接借某个现代外语词。',M,
 'my mom 我妈妈；Mom 直接当称呼或人名用时常大写，不加 my。英式很多地区更常说 mum。',
 'my mom；ask Mom；a working mom。',
 'mom、mum 地区拼写习惯不同，mother 更正式；中文不必为了形式不同硬译成三种不同亲属。',
 ('My mom taught me how to cook.','我妈妈教会了我做饭。'),('Mom, have you seen my keys?','妈，你看见我的钥匙了吗？'))
W('mommy','英 /ˈmɒmi/；美 /ˈmɑːmi/','妈咪；妈妈的儿童称呼',
 '小孩叫妈妈时更亲昵、带儿童口吻的说法。',
 'mom + 昵称式 -y，写 mommy 时双写 m；对应家庭称呼的亲昵扩展，不是改变亲属关系。',M+[['mom + -y → mommy','妈妈 → 儿童亲昵称呼']],
 'Where is Mommy? 妈妈在哪儿？my mommy 我妈咪；美式常见，英式也常写 mummy。',
 'my mommy；ask Mommy；Mommy and Daddy。',
 'mommy 是称呼语气，stepmom 是关系类型；同一位继母也可以被孩子亲昵叫 Mommy。',
 ('The little girl ran to her mommy.','小女孩跑向妈妈。'),('Mommy, can you read this story again?','妈咪，你能再读一遍这个故事吗？'))
W('stepmom','英 /ˈstepmɒm/；美 /ˈstepmɑːm/','继母的口语称呼',
 '父亲后来结婚的妻子，且她不是自己的生母；mom 让称呼更日常。',
 'step- 继亲关系 + mom。step- 的历史接失去亲属、孤儿等旧词族，与迈步 step 不是同一条来源。',M+[['step- + mom → stepmom','继亲关系 + 妈妈 → 继母口语称呼']],
 'my stepmom 我的继母；正式或中性完整形式是 stepmother。关系名本身不说明相处亲疏。',
 'my stepmom；a caring stepmom；live with a stepmom。',
 'stepmom 继母，不是 mother-in-law 岳母、婆婆，也不是 godmother 教母。',
 ('My stepmom helped me prepare for the interview.','我的继母帮我准备了面试。'),('She gets along well with her stepmom.','她和继母相处得很好。'))
R('B4438','妈妈的日常称呼与继母','MOM：家庭里的亲近称呼','mom、mommy 按口吻亲昵程度相邻；stepmom 另外说明继亲关系。',
 'mom 是儿童、家庭称呼形式的缩短用法，mommy 再加亲昵称呼后缀。step- 接继亲旧词族，不是走路一步。',
 'mom → mommy；step- + mom → stepmom。',
 [['称呼与亲昵扩展','mom · mommy'],['继亲关系','stepmom']],
 'mom 多见美式，mum 多见英式；mommy 变语气，stepmom 变关系类型。',
 'She calls her stepmom Mom.\n\n她把继母叫作妈妈。',
 'mom mommy stepmom')
Q=[['拉丁 quālis 什么样 → quālitās → 法语 qualité → quality','某物是什么性质 → 特点、质量'],['中世纪拉丁 qualificāre → 法语 qualifier → qualify','赋予、说明性质 → 使具资格；限定说法']]
W('quality','/ˈkwɒləti/；美 /ˈkwɑːləti/','质量；品质；特征、优点',
 '先问它是什么样，再问做得好不好。单数常说质量，复数 qualities 经常说一个人的特点、优点。',
 '经法语来自拉丁 quālitās，接 quālis 什么样。历史是性质名词，不是把 quantity 数量改几个字母变成质量。',Q[:1]+[['现代英语 quality','性质、质量；人物特点与优点']],
 'high quality 高质量，leadership qualities 领导品质，quality of life 生活质量；quality time 指专心陪伴的相处时间。',
 'high quality；quality of life；leadership qualities；quality time。',
 'quality 质量、性质，quantity 数量；a quality product 常有品质好的评价，不只是说东西有某种性质。',
 ('The company focuses on quality rather than quantity.','公司注重质量，而非数量。'),('Patience is one of her best qualities.','耐心是她最好的品质之一。'))
W('qualitative','英 /ˈkwɒlɪtətɪv/；美 /ˈkwɑːləteɪtɪv/','性质上的；定性的',
 '问发生了什么、是什么体验、有哪些特点，而不只是问有几个、多少分。',
 '经拉丁性质词的对应形容词形式与法语等进入英语，现代与 quality 相联系。不能把整个词简单译成质量好的。',Q[:1]+[['拉丁性质词的形容词分支 → qualitative','关于性质、特点 → 定性的']],
 'qualitative research 定性研究，qualitative data 定性资料，a qualitative difference 性质上的差别；方法名不自动评价研究好坏。',
 'qualitative research；qualitative data；a qualitative difference。',
 'qualitative 关注性质，quantitative 关注数量；实际研究可以把两类方法结合，并非互相排斥。',
 ('The study uses qualitative interviews to explore people’s experiences.','研究用定性访谈探索人们的经历。'),('There is a qualitative difference between the two approaches.','这两种方法存在性质上的差别。'))
W('qualify','英 /ˈkwɒlɪfaɪ/；美 /ˈkwɑːləfaɪ/','具备资格；使符合条件；限定、修正说法',
 '一条常用路是条件够了、可以参加；另一条是给话加条件，让它别说得太满。',
 '经法语 qualifier 及中世纪拉丁 qualificāre，历史接 quālis 什么样 + facere 使、做的组合成分。不是现代英语直接把 quality 尾巴改成 fy 才第一次造出来。',Q,
 'qualify for the final 获得决赛资格，qualify as a teacher 取得教师资格；qualify a statement 为说法加限制。',
 'qualify for；qualify as；qualify someone to do；qualify a statement。',
 'qualify for 针对准入对象，qualify as 针对身份；qualify my support 可能是给支持加保留，绝非让支持拿证。',
 ('The team qualified for the final.','球队获得了决赛资格。'),('She qualified her earlier statement by adding a condition.','她补充一个条件，对先前的说法作了限定。'),sources=['https://www.etymonline.com/word/qualify','https://en.wiktionary.org/wiki/qualify#English'])
W('qualified','英 /ˈkwɒlɪfaɪd/；美 /ˈkwɑːləfaɪd/','合格、有资质的；有限度、带保留的',
 '说人时常是条件、训练达标；说支持或赞同时，反而可能是有条件地支持。',
 'qualify 以辅音字母 f 加 y 结尾，加 -ed 时 y 改 i，成为 qualified。两种主要形容词义接 qualify 的资格、限定两分支。',Q+[['qualify + -ed → qualified','具资格 → 合格；被限定 → 有保留']],
 'a qualified teacher 合格教师，qualified support 有保留的支持；well qualified for 很适合、很有资质担任。',
 'a qualified teacher；qualified support；qualified approval。',
 'qualified support 不是完全支持；unqualified support 无保留支持。别把形容词只记成合格。',
 ('A qualified electrician checked the wiring.','一位合格电工检查了线路。'),('The proposal received only qualified support.','提议只获得了有保留的支持。'))
W('unqualified','英 /ʌnˈkwɒlɪfaɪd/；美 /ʌnˈkwɑːləfaɪd/','不合格、无资质的；无保留的、十足的',
 '否定的是哪个意思很关键：人没资格是不合格，支持没有限制则是全力支持。',
 'un- 不、没有 + qualified，同时可否定具资格与被限定两种状态，形成看似相反的现代语气。',Q+[['un- + qualified → unqualified','无资格；另一路无任何限定']],
 'unqualified staff 无资质人员，unqualified support 无保留支持，an unqualified success 十足的成功。',
 'unqualified staff；unqualified support；an unqualified success。',
 'unqualified success 是毫无疑问的成功，不是不合格的成功；先判 qualified 资格还是限定这条义。',
 ('The event was an unqualified success.','活动取得了十足的成功。'),('He was unqualified for the technical role.','他不具备担任该技术岗位的资格。'))
W('disqualify','英 /dɪsˈkwɒlɪfaɪ/；美 /dɪsˈkwɑːləfaɪ/','取消资格；使不具备资格',
 '原本想参加、被选中，某项规则或情况让它失去准入资格。',
 'dis- 取消、相反 + qualify，形成取消资格动词。disqualify someone from doing 是常用结构。',Q+[['dis- + qualify → disqualify','资格被取消、受阻 → 取消资格']],
 'disqualify a competitor 取消选手资格，be disqualified from the race 被取消比赛资格；原因可能是违规或资格条件不符。',
 'disqualify someone from；be disqualified for；disqualify a competitor。',
 'disqualify 资格被取消，lose 比赛落败；输了比赛不自动等于被取消资格。',
 ('The runner was disqualified for a false start.','跑者因抢跑被取消资格。'),('The rule disqualifies employees from entering the competition.','规则规定员工没有资格参加这项比赛。'))
W('qualifier','英 /ˈkwɒlɪfaɪə/；美 /ˈkwɑːləfaɪər/','资格赛；入围者；限定词语',
 '可以是一场决定谁能参加的比赛、一个已取得资格的人，也可以是给说法加条件的词。',
 'qualify + -er，词尾 y 改 i，成为 qualifier。不同义分别接资格与限定两分支。',Q+[['qualify + -er → qualifier','决定、获得资格者或事项；限定成分']],
 'a World Cup qualifier 世界杯预选赛，a surprise qualifier 意外入围者；a qualifier such as usually 是诸如通常这样的限定成分。',
 'a World Cup qualifier；a final qualifier；add a qualifier。',
 'qualifier 可以是比赛、参赛者或语言成分；不是永远指资格证书，证书要看 certificate 等具体词。',
 ('The team won its first qualifier.','球队赢得了首场资格赛。'),('Adding the qualifier usually made the claim more accurate.','加上通常这个限定词，让说法更准确了。'))
R('B2470','性质、质量；资格与限定','QUALITY：是什么样；QUALIFY：条件与范围如何界定','先从 quality 性质进入，再看 qualify 的资格与限定两分支。qualified、unqualified 用支持和成功的搭配对照。',
 'quality 借法语上接拉丁 quālitās；qualify 另经法语接中世纪拉丁性质 + 使的组合。它们是历史词族关系，不能把所有变化都伪装成现代英语临时加后缀。',
 'quality → qualitative；qualify → qualification、qualified、qualifier；un- → unqualified；dis- → disqualify。',
 [['性质、质量与定性','quality · qualitative'],['资格、条件与限定','qualify · qualification · qualified · qualifier'],['否定的不同方向','unqualified · disqualify']],
 'qualified support 有保留，unqualified support 无保留；qualitative 定性不等于质量好；qualification 可有资格与保留条件义，已有精讲可连读。',
 'The qualified coach gave the team unqualified support.\n\n那位有资质的教练给予球队毫无保留的支持。',
 'quality qualitative qualify qualification qualified qualifier unqualified disqualify')
if __name__=='__main__':save('continuation_20261029_eb',ROOTS,WORDS)
