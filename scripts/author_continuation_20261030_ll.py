"""Punk, taxi, ability nouns, entrepreneur and nightmare."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
P=[['punk 的较早多条用法','朽木、劣质、对人的贬称等，来源和彼此关系有争论'],['社会贬称 → punk rock','年轻人、反叛形象被借为音乐及文化名称'],['punk + -y → punky','朋克风格；另一支可说朽软木质']]
W('punk','/pʌŋk/','朋克音乐、朋克文化；朋克；〔贬义〕小混混；〔另支〕朽木',
 '音乐语境里是朋克及其文化形象；电影里叫 someone a punk，则可能是在骂小混混、没用的家伙。别让同一个中文音译遮住语气变化。',
 '这个词早有劣质、对人的贬称及朽木等用法，来源、相互关系并未全定。音乐名 punk rock 借用了反叛年轻人等贬称形象，后来形成文化自称。',P[:2],
 'a punk band 朋克乐队，punk rock 朋克摇滚，punk fashion 朋克服饰。骂人用法带贬损；朽木义多见木材描述。',
 'punk rock；a punk band；punk fashion。',
 '朋克乐迷不等于小混混；音乐文化名称与辱称的当代用法要按场景分开。',
 ('She plays guitar in a punk band.','她在一支朋克乐队里弹吉他。'),('The exhibition traces the influence of punk on fashion.','展览追溯朋克文化对时装的影响。'),sources=['https://en.wiktionary.org/wiki/punk#English','https://www.etymonline.com/word/punk'])
W('punky','/ˈpʌŋki/','有朋克风格的；朽软的〔木材义〕',
 '衣服、发型带着朋克的反叛风格，可说 punky；木头一戳发软、腐朽了，也可能 punky。这是 punk 的不同分支带出的性质。',
 'punk + -y，性质后缀。文化义基于朋克，木质义基于朽木，不能拿发型风格反推木头也在玩音乐。',P,
 'a punky haircut 朋克风发型，a punky look 朋克造型，punky wood 腐朽发软的木头。',
 'a punky haircut；punky wood。',
 '同形词的后缀规则可以相同，前面的具体含义却要看对象。木材义能识别即可，日常先掌握风格表达。',
 ('Her short, punky haircut suited the jacket.','她那短短的朋克风发型和夹克很搭。'),('The old fence had become soft and punky.','旧篱笆已经腐朽发软。'))
R('B4068','多条旧义汇入现代朋克文化名称与性质','PUNK：先看是在谈音乐文化，还是贬称、木材','punk → punky。',
 '词的历史不总是一根直线。文化名称可从旧贬称借来，但今天谈朋克音乐，并不是在给所有乐迷下人格判断。',
 'punk 的更早来源、关系有争论；punk rock 形成音乐文化分支，-y 再形成性质词。',
 [['文化、旧义与相应性质','punk · punky']],
 'punky wood 说朽木；punky haircut 说风格；同形不等于一个中文译义覆盖全部。',
 'The band’s punky style attracted new listeners.\n\n乐队的朋克风格吸引了新听众。','punk punky')
T=[['德语 Taxameter → 法语 taximètre','计费表；前项联系收费，后项是测量仪器'],['taximeter cab → taxicab、taxi','带计费表的出租车，后经缩短'],['车辆意象 → 飞机地面移动','taxi 作动词滑行，taxiway 是相应通道']]
W('taxi','/ˈtæksi/','出租车；乘出租车；〔飞机〕滑行',
 '城市里载你去某一程的是 taxi；机场里 The plane is taxiing 则是飞机还在地面滑行，像车辆在场内移动。',
 '由 taximeter cab 缩短，taximeter 联系德语 Taxameter、法语 taximètre 的计费表。飞机动词用法从车辆、地面移动意象发展，不是说飞机被出租车拖着走。',T,
 'take a taxi 乘出租车，hail a taxi 招出租车，taxi to the runway 滑行到跑道。-ing 形式常写 taxiing，保留 i。',
 'take a taxi；hail a taxi；taxi to the runway。',
 'taxiway 是滑行道，runway 是起降跑道；taxiing 不是已经起飞。taxi 的计费史也不等于每次出行都必须按同一种表收费。',
 ('We took a taxi to the station.','我们乘出租车去了车站。'),('The plane taxied slowly towards the runway.','飞机缓缓滑向跑道。'),sources=['https://en.wiktionary.org/wiki/taxi#English','https://www.etymonline.com/word/taxi'])
W('taxicab','/ˈtæksikæb/','出租车、计程车',
 'taxi 和 cab 都能说出租车，taxicab 是把历史名称保留得更完整的说法，不是出租车里面另一种完全不同的车。',
 '由 taximeter cab 缩短，现代外形对应 taxi + cab。cab 本身又从 cabriolet 一类马车名称缩短，后来转到机动车。',T[:2]+[['taximeter cab → taxicab','计费出租车的缩短名称']],
 'a yellow taxicab 黄色出租车，a taxicab driver 出租车司机，a taxicab company 出租车公司。',
 'a taxicab driver；a yellow taxicab。',
 'taxicab、taxi、cab 在常见出租车场景可重合；完整形式不自动表示豪华、多人或更便宜。',
 ('A yellow taxicab stopped outside the hotel.','一辆黄色出租车停在酒店外。'),('The taxicab driver helped us with the luggage.','出租车司机帮我们拿行李。'))
R('B3785','计费出租车的缩略名称，扩成飞机地面滑行','TAXI：先是按程载客的车，后来也说飞机在地面移动','taxicab、taxi；taxi → taxiway。',
 '词的短长不等于年龄顺序：taxi、taxicab 都从较长的计费出租车名称缩来。飞机滑行义再从车辆意象接出去。',
 'Taxameter → taximètre → taximeter cab → taxicab、taxi；way 通道。',
 [['出租车名称与滑行通道','taxi · taxicab · taxiway']],
 'taxiing 仍在地面；taxiway 与 runway 分工不同；taxicab 不代表另一等级服务。',
 'From the taxi, we could see planes moving along the taxiway.\n\n从出租车里，我们能看到飞机沿滑行道移动。','taxi taxicab taxiway')
Ab=[['动词、名词词干 + -able','能够、适合、可接受等性质，不只一种被动意思'],['-able → -ability','把这种性质变成可讨论、比较的状态或能力'],['具体用途决定中文','reusability 可复用性；serviceability 可用、可检修性；favorability 好感、有利程度']]
W('favorability','英 /ˌfeɪvərəˈbɪləti/；美 /ˌfeɪvərəˈbɪləti/','好感度、受认可程度；有利程度',
 '问大家对某人有没有好感，或条件对一件事有多有利，可以用 favorability。它把 favorable 的正面、有利变成可讨论的程度。',
 'favorable + -ity，-able 对应变为 -ability；也可按 favor + -ability 看表层结构。英式对应常拼 favourability，此处保留美式词头。',Ab[:2]+[['favorable → favorability','正面、有利的性质与程度']],
 'a favorability rating 好感度评分，public favorability 公众好感，the favorability of conditions 条件有利程度。',
 'a favorability rating；the favorability of。',
 '好感不等于实际投票、购买或赞成每项政策；rating 测什么要看题目，而不是只看词尾。',
 ('The survey measured public favorability towards the proposal.','调查衡量公众对提案的好感程度。'),('The report considered the favorability of local conditions.','报告考察当地条件的有利程度。'))
W('manoeuvrability','英 /məˌnuːvərəˈbɪləti/；美常拼 maneuverability /məˌnuːvərəˈbɪləti/','机动性、易操纵程度',
 '车能不能在窄路转弯，船能不能灵活变向，讲的是 manoeuvrability。不是只问开得多快，而是能否方便、灵活地调整运动。',
 'manoeuvre 操纵、机动 + -ability；对应 manoeuvrable + -ity。英式 manoeuvre 与美式 maneuver 拼法不同，形成的能力名词同理。',Ab[:2]+[['manoeuvre → manoeuvrable → manoeuvrability','能机动、好操纵 → 这种能力程度']],
 'improve manoeuvrability 提高机动性，excellent manoeuvrability 出色操纵性，manoeuvrability in tight spaces 狭小空间中的机动性。',
 'improve manoeuvrability；excellent manoeuvrability。',
 'manoeuvrability 不等于速度、动力或可靠性；各指标可以互相影响，但不是同一个意思。',
 ('The small boat offers good manoeuvrability in narrow channels.','这艘小船在狭窄水道里机动性很好。'),('The new wheels improved the cart’s manoeuvrability.','新轮子让手推车更容易操纵转向。'))
W('serviceability','英 /ˌsɜːvɪsəˈbɪləti/；美 /ˌsɜːrvɪsəˈbɪləti/','可用性、适用性；可检修性',
 '设备还能不能好好服役，是 serviceability 的可用义；坏了后能不能方便地检修，也会用这个词讨论。两者都围着 service 的服务、使用或保养。',
 'serviceable + -ity，对应 service + -ability；由可供使用、可服务或检修的性质形成名词。',Ab[:2]+[['service → serviceable → serviceability','能用、能检修 → 相应性质']],
 'check serviceability 检查能否使用，improve serviceability 改善可用或检修性质，easy access improves serviceability 便于接近部件可改善检修。',
 'equipment serviceability；improve serviceability。',
 '可用和易检修不是同一指标，读报告先看它的定义；serviceability 也不等于单次服务的礼貌程度。',
 ('The technician checked the serviceability of the equipment.','技术人员检查设备能否正常使用。'),('Removable panels improve the machine’s serviceability.','可拆面板提高了机器的检修便利性。'))
W('reusability','/ˌriːjuːzəˈbɪləti/','可重复使用性、可复用程度',
 '一次用完以后，还能不能在下一次、别的地方继续用？这种能力就是 reusability，杯子、软件模块、材料都可讨论。',
 'reuse 再使用 + -ability，对应 reusable + -ity。reuse 动词的 /z/ 保留，和单独名词 use 的 /s/ 不同。',Ab[:2]+[['reuse → reusable → reusability','可再用 → 这种能力、程度']],
 'code reusability 代码复用性，improve reusability 提高可复用性，the reusability of materials 材料重复利用的能力。',
 'code reusability；improve reusability。',
 'reusability 是能再用，recyclability 是能回收加工再利用；原物直接再用与材料重新加工不是同一步。',
 ('The design improves the reusability of the containers.','这个设计提高了容器的重复使用能力。'),('Clear interfaces can improve code reusability.','清晰的接口有助于提高代码复用性。'))
W('tolerability','英 /ˌtɒlərəˈbɪləti/；美 /ˌtɑːlərəˈbɪləti/','可忍受、可耐受程度',
 '可能不舒服，但在多大程度上还能承受，这是 tolerability。它问能否忍受，而不直接评价效果多好、你多喜欢。',
 'tolerate 容忍、承受 + -ability，去词尾 e；也可从 tolerable 可忍受的对应变成 -ability 名词。',Ab[:2]+[['tolerate → tolerable → tolerability','可承受 → 可承受的程度']],
 'the tolerability of a treatment 治疗的耐受性，assess tolerability 评估可耐受程度，poor tolerability 难以耐受。专业报告里通常与效果等指标分开。',
 'assess tolerability；poor tolerability。',
 'tolerability 不等于 effectiveness 效果，也不等于没有任何不适；这是词义上的指标区别。',
 ('The study assessed both effectiveness and tolerability.','研究同时评估效果与耐受性。'),('The questionnaire asked about the tolerability of the noise.','问卷询问人们对噪声的可忍受程度。'))
R('A1815','把能否、适合与可接受的性质名词化','-ABILITY：把能不能、好不好用变成可讨论的性质','从 -able 到 -ability：可读、可再用、可维护、可承受等各有具体对象。',
 '同一个词尾只帮你认出名词这一层，真正的理解还在前半：reusability 问能否再用，serviceability 问能否使用或检修，favorability 说好感或有利程度。',
 '-able 相应变 -ability，通常可理解为性质形容词 + -ity；并非每个词都能机械译成被……的能力。',
 [['使用、适配与长期运作','usability · reusability · serviceability · suitability · adaptability · workability · sustainability · maintainability · scalability'],['预测、识别与追踪','predictability · readability · traceability · repeatability · believability · deniability'],['接受、评价与可负担','favorability · tolerability · affordability · desirability · respectability · notability'],['其他具体能力','manoeuvrability · survivability · dependability · marketability · playability · excitability · enforceability · livability']],
 '同后缀不表示同一种能力；reusability 与回收加工不同；tolerability 与效果不同。',
 'The design balances affordability, serviceability and reusability.\n\n设计兼顾可负担性、检修便利性和重复使用能力。','usability reusability serviceability suitability adaptability workability sustainability maintainability scalability predictability readability traceability repeatability believability deniability favorability tolerability affordability desirability respectability notability manoeuvrability survivability dependability marketability playability excitability enforceability livability')
E=[['古法语 entreprendre 承担、着手','entre- + prendre 拿取；词整体已有承担事业义'],['entrepreneur 承担、经营者 → 英语','历史借入、再借入，发展为创业经营者'],['英语后缀扩展','entrepreneurship 创业活动、精神；entrepreneurial 创业相关性质']]
W('entrepreneur','英 /ˌɒntrəprəˈnɜː/；美 /ˌɑːntrəprəˈnɜːr/','创业者、企业经营者',
 '有一个想法，还得把人、资金、产品组织起来，并承担经营结果，这样创办、经营业务的人是 entrepreneur。核心像把事业拿到自己手上做。',
 '借法语 entrepreneur，来自 entreprendre 承担、着手 + 人物形式 -eur；prendre 联系拿取。英语中曾借入又再借入，后来商业经营义突出。',E[:2],
 'a young entrepreneur 年轻创业者，a social entrepreneur 社会创业者，an entrepreneur who founded a company 创办公司的人。',
 'a young entrepreneur；a social entrepreneur。',
 'entrepreneur 不自动等于亿万富翁，也不只限科技公司；重点是创办、组织、经营业务及相应风险。',
 ('The entrepreneur started a small repair business.','这位创业者开办了一家小维修店。'),('Local entrepreneurs turned the empty building into a market.','当地创业者把空楼改成了市场。'),sources=['https://en.wiktionary.org/wiki/entrepreneur#English','https://www.etymonline.com/word/entrepreneur'])
W('entrepreneurship','英 /ˌɒntrəprəˈnɜːʃɪp/；美 /ˌɑːntrəprəˈnɜːrʃɪp/','创业活动、创业精神与能力',
 'entrepreneur 是创业的人，entrepreneurship 把创办经营、寻找机会、承担不确定性的活动和精神合起来说。',
 'entrepreneur + -ship，形成身份、实践及相应品质的抽象名词。这里不是一艘船。',E,
 'encourage entrepreneurship 鼓励创业，a course in entrepreneurship 创业课程，entrepreneurship education 创业教育。',
 'encourage entrepreneurship；entrepreneurship education。',
 'entrepreneurship 不作一个创业者的人物名词；学创业课程也不自动保证一定创业成功。',
 ('The college offers a course in entrepreneurship.','学院开设创业课程。'),('The programme encourages entrepreneurship in rural communities.','这个项目鼓励乡村社区开展创业活动。'))
W('entrepreneurial','英 /ˌɒntrəprəˈnɜːriəl/；美 /ˌɑːntrəprəˈnɜːriəl/','创业的、有创业精神的、善于开创的',
 '看到机会就主动组织资源、想办法做出新业务，这种劲头可叫 entrepreneurial。它也能描述已有组织中的开创能力，不只给公司创始人用。',
 'entrepreneur + -ial，形成相关性质形容词，增加 -ial 后尾部读出 /riəl/。',E,
 'entrepreneurial skills 创业能力，an entrepreneurial spirit 创业、开拓精神，an entrepreneurial approach 主动开创新机会的做法。',
 'an entrepreneurial spirit；entrepreneurial skills。',
 'entrepreneurial 是性质，entrepreneur 是人，entrepreneurship 是活动或精神；不是用长短程度区分职位高低。',
 ('She brought an entrepreneurial spirit to the community project.','她为社区项目带来了主动开创的精神。'),('The workshop helps students develop entrepreneurial skills.','工作坊帮助学生发展创业能力。'))
R('B3704','把事业承担起来的人，及其活动、精神与性质','ENTREPRENEUR：把一个想法接到手里，组织起来做','entrepreneur → entrepreneurship、entrepreneurial。',
 '人、活动、性质分开：创业者是 entrepreneur，创业这件事和精神是 entrepreneurship，相关能力和态度是 entrepreneurial。',
 'entreprendre 承担 + -eur 人物 → entrepreneur；-ship 活动、品质，-ial 性质。',
 [['创业者、活动与性质','entrepreneur · entrepreneurship · entrepreneurial']],
 '创业者不必已经富有；entrepreneurial 也可说组织内部的开创精神；词尾各有语法角色。',
 'The entrepreneur teaches entrepreneurial skills in an entrepreneurship course.\n\n这位创业者在创业课程里教授创业能力。','entrepreneur entrepreneurship entrepreneurial')
Ni=[['night + 旧词 mare 夜间扰人的精怪','中古英语 nightmare 的旧超自然观念'],['精怪 → 睡眠中的压迫、噩梦 → 糟糕经历','旧观念的对象逐渐转为体验本身'],['nightmare + -ish → nightmarish','像噩梦一样可怕、难熬']]
W('nightmarish','英 /ˈnaɪtmeərɪʃ/；美 /ˈnaɪtmerɪʃ/','噩梦般的、可怕难熬的',
 '经历糟到像掉进噩梦，醒着也想赶紧结束，就是 nightmarish。比如混乱旅程、恐怖场景，不要求真在睡觉。',
 'nightmare + -ish，去词尾 e。nightmare 里的 mare 历史上指夜间扰人的精怪，不是母马；现代 nightmare 已常指噩梦、极糟经历。',Ni,
 'a nightmarish journey 噩梦般的旅程，a nightmarish scene 可怕场景，nightmarish traffic 糟糕得令人难熬的交通。',
 'a nightmarish experience；a nightmarish journey。',
 '-ish 在这里是像……的，不必减弱成只有一点点可怕；a nightmarish experience 可以非常严重，也可以口语夸张。',
 ('The journey became nightmarish after three missed connections.','三次没赶上接驳后，旅程变得噩梦般难熬。'),('The film creates a nightmarish city of endless corridors.','电影营造了一座走廊无尽、噩梦般的城市。'),sources=['https://en.wiktionary.org/wiki/nightmarish#English','https://www.etymonline.com/word/nightmare'])
R('B4417','夜间精怪的旧观念，转成噩梦与可怕经历','NIGHTMARE：从传说里的压迫者，转向人的可怕体验','nightmare → nightmarish。',
 '今天先用噩梦、糟糕经历理解；历史 mare 是旧精怪名称，所以夜里的母马不是可靠词源。',
 'night 夜 + mare 旧精怪词 → nightmare；-ish 像……的 → nightmarish。',
 [['噩梦体验与相应性质','nightmare · nightmarish']],
 'nightmarish 不必实际睡着；-ish 在这里不等于程度必然很轻；mare 不取现代母马义。',
 'What began as a small delay became a nightmarish journey.\n\n最初的一点延误，后来变成了一趟噩梦般的旅程。','nightmare nightmarish')
if __name__=='__main__':save('continuation_20261030_ll',ROOTS,WORDS)
