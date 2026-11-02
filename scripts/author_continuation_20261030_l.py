"""Ride and table: ordinary words before their common extensions."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
RI=[['古英语 rīdan → 中古英语 riden','骑乘、乘坐着移动'],['英语 ride','骑马、骑车、乘车；一段乘坐经历']]
W('ride','/raɪd/','骑；乘坐；骑乘、搭车经历',
 '人坐在马、车或其他载体上，让它带着自己走；自己骑车和搭别人的车都可以用。',
 '继承古英语 rīdan，经中古英语延续。不规则变化 ride—rode—ridden。现代 ride 也作名词，指一趟乘坐或游乐设施。',RI,
 'ride a bike 骑自行车，ride a horse 骑马，ride on a bus 乘公交。give someone a ride 捎某人一程，go for a ride 出去骑一圈或兜风。',
 'ride a bike；give someone a ride；go for a ride；a fairground ride。',
 'drive 常说驾驶汽车、控制车辆，ride in a car 常说坐车；骑自行车用 ride。give me a ride 口语求搭车，英式还常说 give me a lift。',
 ('She rides her bike to work every day.','她每天骑自行车上班。'),('Could you give me a ride to the station?','你能捎我去车站吗？'))
W('ridden','/ˈrɪdən/','ride 的过去分词；受某事困扰的〔常用于组合〕',
 '说“已经骑过”时用 ridden；描述被麻烦缠住时，像那件事压在身上。',
 'ride 的不规则过去分词，保留旧分词 -en 与元音变化。困扰、支配义常用于组合形式，不把所有 -en 都当使成为的动词后缀。',RI+[['ride → rode → ridden','现在、过去与过去分词的不规则词形'],['ridden 的组合用法','受某种问题支配、困扰']],
 'have ridden 已经骑过，be ridden by 可说由谁骑乘。debt-ridden 负债累累等组合帮助理解延伸，但本页不新增连字符词条。',
 'have ridden；had ridden；a horse ridden by a beginner。',
 'I rode yesterday 是过去式；I have ridden before 用过去分词。written 写过与 ridden 骑过拼写不同，重在辨清原动词。',
 ('I have never ridden a motorcycle.','我从未骑过摩托车。'),('The horse had been ridden by several beginners that morning.','那天上午，好几名初学者骑过这匹马。'))
W('rider','英 /ˈraɪdə/；美 /ˈraɪdər/','骑手；乘客；附加条款、附件',
 '先是骑在马或车上的人；条款义可想成附在主文件上的补充部分，跟着正文走。',
 '古英语 rīdere 已有骑乘者义，现代可对应 ride + -er。附加条款义后来出现，不是把合同内容真的拿去骑马。',RI+[['古英语 rīdere → rider','骑乘者 → 乘客；另发展出文件附加条款义']],
 'a bicycle rider 骑车者，bus riders 公交乘客，美式常用。a rider to an agreement 协议附加条款；演出合同中的 rider 可列场地、设备等额外要求。',
 'a skilled rider；bus riders；a rider to an agreement。',
 'rider 不限骑马的人；driver 明确是驾驶者。附加条款义属于文件用法，具体效力由文本及适用规则决定。',
 ('The rider slowed down as she approached the bend.','骑手接近弯道时放慢了速度。'),('The band sent the venue a rider listing its equipment needs.','乐队给场地方发了列明设备需求的合同附件。'),sources=['https://www.etymonline.com/word/rider','https://en.wiktionary.org/wiki/rider#English'])
W('override','英 /ˌəʊvəˈraɪd/；美 /ˌoʊvərˈraɪd/〔动词〕','压过；推翻；越过默认设置而接管',
 '两条指令相冲突，较强、较高优先级的那条占上风；机器本来自动做，人也可以接管。',
 '古英语 oferrīdan，经中古英语 overriden；对应 over- 越过、压过 + ride。由骑过、压过发展到压倒原有决定。变化 override—overrode—overridden。',RI+[['古英语 ofer- + rīdan → override','骑过、压过 → 使另一决定或控制失效']],
 'override a decision 推翻决定，override the automatic settings 越过自动设置。a manual override 是人工接管功能，名词通常重音靠前。',
 'override a decision；override the default；a manual override。',
 'override 是较高优先级取代当前行为；overload 是负载过大。override 某设置不表示把设备负荷加大。',
 ('An administrator can override the default settings.','管理员可以更改并取代默认设置。'),('Safety concerns overrode the desire to finish quickly.','安全方面的顾虑压过了尽快完成的愿望。'))
W('hayride','/ˈheɪraɪd/','乘干草车游玩；干草车游乐活动',
 '坐上铺着干草、干草包的车，在农场一带慢慢兜一圈，是一种乡村游乐。',
 'hay 干草 + ride 一趟乘坐，按车上的铺垫物和活动方式命名。',RI+[['hay + ride → hayride','坐在铺着干草的车上兜游']],
 'go on a hayride 参加干草车游乐，a farm hayride 农场干草车活动；北美秋季农场活动里常见。',
 'go on a hayride；a farm hayride；an evening hayride。',
 'hayride 是游乐乘坐，hay 是晒干的草；普通运草作业不能不看语境就译成游乐。',
 ('The farm offers a hayride every autumn weekend.','农场每逢秋季周末都提供干草车游乐。'),('The children climbed onto the wagon for the hayride.','孩子们爬上车，准备乘干草车兜游。'))
R('B2960','骑乘、搭乘与压过原决定','RIDE：坐在载体上随它移动','先 ride、ridden、riding，再 rider；override 走压过分支，joyride、hayride、rideshare 各看活动。',
 '古英语骑乘词保留 ride—rode—ridden 的变化。现代载体扩展到车与游乐设施，override 又有优先级压过的抽象义。',
 'ride → rode → ridden；ride → riding、rider；over- + ride；joy/hay + ride；ride + share。',
 [['动作、词形与人物','ride · ridden · riding · rider'],['压过与不同乘坐活动','override · joyride · hayride · rideshare']],
 'drive 驾驶与 ride 搭乘有侧重；rode 是过去式，ridden 是过去分词；override 压过不同于 overload 超载。',
 'The experienced rider had never ridden that horse before.\n\n那位经验丰富的骑手以前从未骑过那匹马。',
 'ride ridden riding rider override joyride hayride rideshare')
TA=[['拉丁 tabula','板、写字板、列表'],['古英语 tabele 与古法语 table → 英语 table','早期借词与法语借词汇合；桌子、表格']]
def TH(f,m):return TA+[[f,m]]
W('table','/ˈteɪbl/','桌子；表格；提出或搁置议题〔地区用法不同〕',
 '一块平面既能摆饭菜，也能把文字、数字排得整整齐齐；于是有桌子和表格两种常用义。',
 '最终接拉丁 tabula 板、列表；英语既有古英语阶段的早期借词，也有后来法语 table 的影响。家具义和表格义都围绕平面展开。',TA,
 'a dining table 餐桌，a table of results 结果表，table of contents 目录。作动词 table a proposal，英式常指提交讨论，美式常指暂搁。',
 'set the table；a table of results；table of contents；table a proposal。',
 'table a proposal 的地区意义可能相反，跨地区沟通用 submit for discussion 或 postpone 更明确。table 表格与 chart 图表也要按呈现方式选择。',
 ('The table shows the results for each month.','表格列出了每个月的结果。'),('We booked a table for four near the window.','我们订了一张靠窗的四人桌。'),sources=['https://en.wiktionary.org/wiki/table#English','https://dictionary.cambridge.org/dictionary/english/table'])
W('tablespoon','/ˈteɪblspuːn/','大汤匙；一大匙〔烹饪量〕',
 '餐桌上的大勺子；食谱里更常指用量勺量出的一大匙。',
 'table 餐桌 + spoon 勺子，合成后也用作烹饪容量名称。它是固定词，不按两部分各自翻译成桌子勺。',TH('table + spoon → tablespoon','餐桌用大勺 → 烹饪一大匙'),
 'a tablespoon of oil 一大匙油，常缩写 tbsp。食谱量有地区差异；不少标准用约15毫升，澳式常用20毫升，应按食谱和量勺标注。',
 'a tablespoon of oil；two tablespoons of sugar；tbsp。',
 'tablespoon 大匙通常大于 teaspoon 茶匙；普通家用餐勺大小不统一，精确烘焙宜用标有容量的量勺。',
 ('Add two tablespoons of olive oil to the pan.','往锅里加入两大匙橄榄油。'),('She measured the sugar with a tablespoon.','她用一大匙量勺量糖。'))
W('tablecloth','英 /ˈteɪblklɒθ/；美 /ˈteɪblklɔːθ/','桌布',
 '铺在桌面上的一层布，让桌面整洁，也能保护它。',
 'table + cloth 布；中古英语已有对应形式，前部用 table 替换了更早同义组合里的 bord。',TH('table + cloth → tablecloth','铺在桌面上的布'),
 'a clean tablecloth 干净桌布，a linen tablecloth 亚麻桌布，spread a tablecloth 铺桌布。',
 'a linen tablecloth；spread a tablecloth；wash the tablecloth。',
 'cloth 是布，clothes 是衣服；桌布不是 tableclothes。复数 tablecloths 保留完整词基。',
 ('She spread a white tablecloth over the table.','她在桌上铺了一块白桌布。'),('We washed the tablecloth after dinner.','晚饭后我们洗了桌布。'))
W('tableware','英 /ˈteɪblweə/；美 /ˈteɪblwer/','餐具〔总称〕',
 '摆一桌饭要用的盘、碗、杯、刀叉等，统起来叫餐具。',
 'table 餐桌 + ware 制品、用具，按使用场景形成集合名称。',TH('table + ware → tableware','餐桌上使用的器具总称'),
 'ceramic tableware 陶瓷餐具，a set of tableware 一套餐具。通常作不可数总称，具体几件可说 pieces of tableware。',
 'ceramic tableware；a set of tableware；disposable tableware。',
 'tableware 是大范围总称；cutlery 侧重刀叉勺等，glassware 侧重玻璃器皿，范围并不完全相同。',
 ('The shop sells simple ceramic tableware.','店里出售简洁的陶瓷餐具。'),('They chose reusable tableware for the party.','他们为聚会选了可重复使用的餐具。'))
W('turntable','英 /ˈtɜːnteɪbl/；美 /ˈtɜːrnteɪbl/','转盘；唱机转盘、唱盘机',
 '平台围着中心转：可以带唱片转，也可以让整辆机车转个方向。',
 'turn 转动 + table 平台；早期用例包括铁路机车转向平台，后来用于唱片播放设备。',TH('turn + table → turntable','能转动的平台 → 铁路转车盘、唱片转盘'),
 'a record on the turntable 唱盘上的唱片，a railway turntable 铁路转车盘；日常音乐语境也可指整台唱盘机。',
 'a record turntable；a railway turntable；a rotating turntable。',
 'turntable 是能旋转的实体平台；turn the tables 是扭转局面的固定表达，来自棋盘游戏背景，别按唱机解释。',
 ('He placed a record on the turntable.','他把唱片放到唱盘上。'),('The museum demonstrated how the turntable turned a locomotive.','博物馆演示了转车盘怎样使机车转向。'),sources=['https://www.etymonline.com/word/turntable','https://en.wiktionary.org/wiki/turntable#English'])
R('B3461','桌面、表格与餐桌用具','TABLE：一块能摆东西、排信息的平面','先桌子和表格，再大匙、桌布、餐具；最后转盘与已有时间表、桌面词。',
 '最终来自拉丁 tabula 板、列表；早期日耳曼借词和法语词在英语中汇合。table 的动词义需要留意英美差异。',
 'table + spoon/cloth/ware；turn + table；time + table → timetable；table + top → tabletop。',
 [['基本平面与安排','table · timetable · tabletop'],['餐桌相关','tablespoon · tablecloth · tableware'],['旋转平台','turntable']],
 'table 议题动词有地区差异；tablespoon 的容量看地区；tableware 总称与 cutlery 不完全同范围。',
 'The tablecloth and tableware were ready before the guests arrived.\n\n客人到来前，桌布和餐具都准备好了。',
 'table timetable tabletop tablespoon tablecloth tableware turntable')
if __name__=='__main__':save('continuation_20261030_l',ROOTS,WORDS)
