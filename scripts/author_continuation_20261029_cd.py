"""Working and making: understand the relationship between compound parts."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
def C(a,b,w,m):return [[a+'；'+b,'并列构词部分'],[w,m]]
W('woodworking','英 /ˈwʊdwɜːkɪŋ/；美 /ˈwʊdwɜːrkɪŋ/','木工；木材加工、制作',
 '把木材当作工作对象，做成家具、构件或其他成品。',
 'wood 木材 + working 加工、制作；也可联系 woodwork 木工 + -ing 的词族关系。两部分共同构成木工活动名称，不是木材先变成工作。',C('wood 木材','working 加工、制作','woodworking','加工木材、制作木制品的活动'),
 'woodworking tools 木工工具，a woodworking class 木工课。可说爱好、手艺或行业活动，不限于木匠的一份正式工作。',
 'woodworking tools；woodworking skills；a woodworking workshop。',
 'woodworking 是以木材为对象的制作活动；woodwork 还可指建筑中已经做好的木制部件等，用法有交叠但不处处相同。',
 ('He took a woodworking class at the community centre.','他在社区中心上木工课。'),('The shed is full of old woodworking tools.','棚屋里放满旧木工工具。'))
W('coworking','英 /ˌkəʊˈwɜːkɪŋ/；美 /ˌkoʊˈwɜːrkɪŋ/','共享办公；一起工作',
 '不同的人使用同一办公空间，各做各的工作，也可能交流合作。',
 'co- 共同 + working 工作。现代共享办公义常用于自由职业者、小团队等共用场地，不要求大家同属一家公司。',C('co- 共同','working 工作','coworking','共同工作；现代常指共享办公'),
 'a coworking space 共享办公空间，a coworking membership 共享办公会员。可共享办公室设施，却不等于所有人都在同一个项目上协作。',
 'a coworking space；a coworking hub；coworking facilities。',
 'coworking 共享空间或一起工作的安排，coworker 同事是人；共用办公空间的人未必就是同一雇主的同事。',
 ('She rented a desk in a coworking space near the station.','她在车站附近的共享办公空间租了一个工位。'),('The coworking hub brings together freelancers from different fields.','共享办公中心聚集了不同领域的自由职业者。'),sources=['https://en.wiktionary.org/wiki/coworking#English','https://dictionary.cambridge.org/dictionary/english/co-working'])
R('B4186','工作；运作；加工；共同工作','WORKING：在做事，也可说明怎样做、做什么','working 既是 work 的形式，也已形成多种形容和活动名词。复合词先看前面说材料、共同关系，还是勤奋程度。',
 'working 由 work + -ing 形成。woodworking、metalworking 说加工对象，coworking 的 co- 说共同，hardworking 说工作态度。',
 'working → hardworking；wood + working、metal + working；co- + working。',
 [['基本用法与勤奋','working · hardworking'],['加工材料与共享办公','woodworking · metalworking · coworking']],
 'woodworking 木工，coworking 共享办公；共用办公空间不保证同属一个公司。',
 'The hardworking designer uses a coworking space for office tasks and a workshop for woodworking.\n\n这位勤奋的设计师在共享办公空间处理文书，在工作坊做木工。',
 'working hardworking woodworking metalworking coworking')
W('filmmaking','/ˈfɪlmmeɪkɪŋ/','电影制作；影视创作过程',
 '把故事、拍摄、声音、剪辑等工作组织起来，做出影片。',
 'film 影片 + making 制作，组成活动名词。现代影片可以数字拍摄，film 在这里不要求一定用胶片。',C('film 影片','making 制作','filmmaking','制作影片的活动、过程'),
 'digital filmmaking 数字电影制作，a filmmaking course 电影制作课程。比只按下相机录制更广，可包括整个创作流程。',
 'independent filmmaking；digital filmmaking；filmmaking techniques。',
 'filmmaking 是活动，filmmaker 是创作者；cinematography 更着重电影摄影，不等于制作全过程。',
 ('She discovered filmmaking through a school project.','她通过学校项目接触到电影制作。'),('The course covers both storytelling and practical filmmaking.','课程既讲故事创作，也讲实际电影制作。'))
W('winemaking','/ˈwaɪnmeɪkɪŋ/','葡萄酒酿造；酿酒',
 '把葡萄等原料转成酒、再形成成品的制作活动。',
 'wine 葡萄酒 + making 制作，复合为酿酒活动名词。不是 winning 赢的拼写变体。',C('wine 葡萄酒','making 制作','winemaking','葡萄酒的酿造活动'),
 'the history of winemaking 酿酒史，winemaking traditions 酿酒传统。学习词义先认出制作什么，不必把 wine 的全部来源重新当作 making 的历史。',
 'traditional winemaking；a winemaking region；winemaking methods。',
 'winemaking 是酿造活动，winemaker 是酿酒师；wine tasting 品酒是另一种活动，不是同一流程名称。',
 ('The museum explores the region’s long history of winemaking.','博物馆介绍这个地区悠久的酿酒历史。'),('She wrote a book about family winemaking traditions.','她写了一本关于家族酿酒传统的书。'))
W('steelmaking','/ˈstiːlmeɪkɪŋ/','炼钢；钢的制造',
 '重点是把原料制成钢这个材料，而不是把一块现成金属敲成形状。',
 'steel 钢 + making 制造，形成工业活动名词。对象决定是炼钢，不是所有金属制造的通名。',C('steel 钢','making 制造','steelmaking','制造钢的工业过程'),
 'the steelmaking industry 炼钢行业，steelmaking technology 炼钢技术。行业报道中常见，不能把 steel 与 steal 偷窃混为一谈。',
 'steelmaking technology；a steelmaking plant；the history of steelmaking。',
 'steelmaking 是制造钢，metalworking 通常说加工金属；making objects from steel 则可能用已制成的钢制作物件。',
 ('The exhibition explains how steelmaking changed the town.','展览介绍炼钢业如何改变了这座城。'),('The company develops equipment for the steelmaking industry.','公司为炼钢行业开发设备。'))
W('dressmaking','/ˈdresmeɪkɪŋ/','服装裁制；尤指女装制作',
 '根据设计、尺寸把布料做成衣服，着重这门裁制服装的手艺或活动。',
 'dress 服装、裙装 + making 制作，形成服装裁制名词；具体传统用法常偏女装，并非只是买裙子、穿裙子。',C('dress 服装、裙装','making 制作','dressmaking','服装尤其女装的裁制'),
 'dressmaking skills 服装裁制技巧，a dressmaking course 服装制作课。活动可包含量体、裁剪、缝制等，不把其中某一步当成全部。',
 'dressmaking patterns；dressmaking skills；a dressmaking course。',
 'dressmaking 比 sewing 缝纫更指向制作衣服；sewing 也可以修补布料、缝其他物品。',
 ('She learned dressmaking from her grandmother.','她跟祖母学会了服装裁制。'),('The shop sells fabric and dressmaking patterns.','这家店出售布料和服装裁制纸样。'))
W('papermaking','英 /ˈpeɪpəmeɪkɪŋ/；美 /ˈpeɪpərmeɪkɪŋ/','造纸',
 '做出来的材料本身是纸，而不是在纸上写字、折纸或填表。',
 'paper 纸 + making 制造，复合为造纸活动名称。',C('paper 纸','making 制造','papermaking','把原料制成纸的活动'),
 'traditional papermaking 传统造纸，the papermaking industry 造纸业。可以说手工工艺，也可以说工业生产。',
 'handmade papermaking；traditional papermaking；papermaking techniques。',
 'papermaking 制造纸；paperwork 是文书、书面手续，paper folding 是折纸。材料相同不代表活动相同。',
 ('The museum demonstrates traditional papermaking.','博物馆展示传统造纸工艺。'),('She studied the history of papermaking in the region.','她研究了该地区的造纸史。'))
W('rulemaking','/ˈruːlmeɪkɪŋ/','规则制定；规章制定',
 '先把该按什么办法做写成规则，让后面的行动有章可循。',
 'rule 规则 + making 制定。making 不只制造看得见的物品，也可说形成规范、决定等抽象成果。',C('rule 规则','making 制定','rulemaking','形成、制定规则的过程'),
 'the rulemaking process 规则制定过程；参与者可以是机构、组织等。监管、行政语境常有专门程序，但词本身不等于一套全球统一的法律流程。',
 'a rulemaking process；participate in rulemaking；a rulemaking body。',
 'rulemaking 制定规则，rule enforcement 执行规则；制定完成不等于规则已经得到遵守。',
 ('The report calls for a more transparent rulemaking process.','报告呼吁规则制定过程更加透明。'),('Several groups submitted comments during the rulemaking process.','几个团体在规则制定过程中提交了意见。'))
W('peacemaking','/ˈpiːsmeɪkɪŋ/','调解；促成和平、和解',
 '双方还在冲突，想办法让他们停下来、达成和解。',
 'peace 和平、和解 + making 促成。整体说努力建立和平、调解冲突，不是把和平当实体物品造出来。',C('peace 和平、和解','making 促成','peacemaking','调解冲突、促成和平'),
 'peacemaking efforts 促和努力；日常可说劝和，国际关系中也可说谈判、调解等促和活动。用这个词不保证行动最后成功。',
 'peacemaking efforts；a peacemaking role；the work of peacemaking。',
 'peacemaking 重在促成和解，peacekeeping 常说维持和平的安排、行动；现实活动可相关，但不是完全相同名称。',
 ('She often took a peacemaking role when the neighbours argued.','邻居争吵时，她常出来调解。'),('The book describes years of patient peacemaking efforts.','书中描述了多年耐心的促和努力。'))
R('B4253','making：制作、形成、促成','MAKING：前面是什么，就看在形成什么','物品可以被制造，规则、和平、配对关系等也可以被形成或促成。部分复合词还有固定专门义。',
 'making 是 make 去 e 加 -ing 的形式。不同复合词的前部分可说产物、活动目标或固定领域，不是所有 making 都限于手工造物。',
 'making → filmmaking、winemaking、steelmaking、dressmaking、papermaking；抽象成果看 rulemaking、policymaking、peacemaking；matchmaking、bookmaking、playmaking 等固定用法各自看。',
 [['基本形成与制作活动','making · filmmaking · winemaking · steelmaking · dressmaking · papermaking'],['规范、和平与家庭相关活动','rulemaking · policymaking · peacemaking · homemaking · lovemaking'],['已形成固定用法的组合','matchmaking · printmaking · playmaking · bookmaking · watchmaking']],
 'papermaking 造纸，不是 paperwork 文书；rulemaking 制定，enforcement 执行；bookmaking 等固定用法不要只逐字猜。',
 'The centre offers practical courses in filmmaking, dressmaking and papermaking.\n\n中心开设电影制作、服装裁制和造纸实践课程。',
 'making filmmaking winemaking steelmaking dressmaking papermaking rulemaking policymaking peacemaking homemaking lovemaking matchmaking printmaking playmaking bookmaking watchmaking')
if __name__ == '__main__':save('continuation_20261029_cd',ROOTS,WORDS)
