"""Winning, holding ground, productive work and accumulating supplies."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
def S(word,base):
 return ['https://en.wiktionary.org/wiki/'+word+'#English','https://www.etymonline.com/word/'+base]
EXISTING_ROOT_ADDITIONS={
 'B2541':dict(words='prizewinner prizewinners'.split(),label='prizewinner：赢得奖项的人',note='prize 奖项 + winner 获胜者，winner 内部为 win 双写 n 加 -er；完整复合词再加 -s 成复数，不把 prize 的撬动同形动词套进来。'),
 'B2996':dict(words='sweepstakes'.split(),label='sweepstakes：把赌注一扫而得的旧画面',note='旧 sweep stake 表赢走所有赌注，后来成竞赛、抽奖等名称；stakes 取赌注一线。现代尤其美式也可用 a sweepstakes，不机械由结尾 s 判为多个活动。'),
 'B3824':dict(words='stakeout stakeouts'.split(),label='stakeout：由 stake out 相关短语形成的监视名词',note='stake out 较早用桩标出边界，后来有对地点守候监视的用法，名词 stakeout 连写；不是把赌注 stake 与 out 直接相加就能逐字翻成下注出门。'),
 'B3157':dict(words='gainful gainfully'.split(),label='gainfully：能取得收入、回报的方式',note='现代对应 gainful 加 -ly，gainful 内层 gain 加 -ful；gainfully employed 常说有收入地就业，不保证工资高或工作令人满足。'),
 'A1741':dict(words='yield yielded yielding unyielding unyieldingly'.split(),label='yield：给出结果、让步与不屈服',note='yield 接古英语支付、交出材料，后来发展产出、给出、屈服。unyielding 为 un- 加 yielding，人的不让步记录早于某些物质不易变形义；现代用物理画面串联不等于年代顺序。'),
 'B2475':dict(words='stockpile stockpiles stockpiled'.split(),label='stockpile：为后来留一批储备',note='stock 储备 + pile 堆，先有矿业名词，再有动词，后扩到一般储备。stock 这一义与树干等旧义的具体语义桥有多种分析，不一概只讲树上长股票。'),
 'B2796':dict(words='amass amasses amassed amassing'.split(),label='amass：把东西聚成很大数量',note='amass 经法语 amasser，联系 à 朝向、masser 聚成一团与 masse 堆、团。现代 a- 不是不的否定前缀，也不是英文一堆的冠词 a。'),
 'A1904':dict(words='accumulate accumulates accumulated accumulating'.split(),label='accumulate：一点点累成一堆',note='accumulate 接拉丁 accumulatus、accumulare，内层 ad- 与 cumulare 堆起、cumulus 堆；ad- 在 c 前同化为 ac-。现代去 e 加词尾，不把 acc- 当独立无来源词根。'),
}
PRIZE=[['prize 奖项 + winner 获胜者 → prizewinner','奖项义与 price 等价值材料相关，winner 接 win'],['prizewinner + -s → prizewinners','一个、多个获奖者']]
SWEEP=[['旧 sweep stake：赢走全部赌注','sweep 扫 + stake 赌注'],['sweepstakes → 竞赛、抽奖等名称','现代词尾 s 也可出现在单项活动名称中']]
STAKEOUT=[['stake out 较早用桩标界，后来守候监视地点','同一短语具体用途发展'],['监视短语 → stakeout 名词 → stakeouts','守候监视活动及复数']]
YIELD=[['古英语 gieldan、geldan 支付、交出 → yield','英语后来有产出、给出与屈服等用途'],['un- + yielding → unyielding；再加 -ly','不让步、不易压弯的性质，及相应方式']]
STOCK=[['stock 储备 + pile 堆 → stockpile 名词','较早矿业堆存物'],['名词 → stockpile 动词及词尾','为将来积存物资；后有一般用途']]
AMASS=[['法语 à + masser，接 masse 团、堆 → amasser','聚到一起、聚成堆'],['法语动词 → 英语 amass','聚集大量财物、信息等']]
ACC=[['拉丁 ad- + cumulare 堆起 → accumulare、accumulatus','ad- 在 c 前同化，cumulus 为堆'],['英语 accumulate → 现代词尾','逐步增加、累积，既可主动积累也可自行堆起来']]
W('prizewinner','英 /ˈpraɪzˌwɪnə/；美 /ˈpraɪzˌwɪnɚ/','获奖者',
 '某项比赛、评选把奖颁给一个人，那个人就是 prizewinner。重在确实赢到一个奖，不只是表现不错。',
 'prize 奖项 + winner 获胜者；winner 内部 win 双写 n 加 -er。prize 在这里不是撬开的同形动词。',PRIZE,
 'a literary prizewinner 文学奖获奖者；the first prizewinner 首位获奖者。',
 'a former prizewinner 曾经的获奖者；interview a prizewinner。',
 'prizewinner 已经获奖，nominee 是被提名者；进入候选名单不等于最终拿奖。',
 ('The prizewinner thanked her teachers during the ceremony.','获奖者在颁奖礼上感谢了老师。'),('The festival invited a former literary prizewinner to speak.','艺术节邀请了一位曾获文学奖的人发言。'),sources=S('prizewinner','prize'))
W('prizewinners','英 /ˈpraɪzˌwɪnəz/；美 /ˈpraɪzˌwɪnɚz/','获奖者〔复数〕',
 '一场评选有几位获奖者，把他们一起说就是 prizewinners。最后的 -s 加在整个奖项获胜者这个组合后面。',
 'prizewinner + -s，读 /z/；内层 prize + winner，winner 又接 win + -er。层层都保留，不把人物尾漏掉。',PRIZE,
 'this year’s prizewinners 今年获奖者；previous prizewinners 往届获奖者。',
 'announce the prizewinners 宣布获奖者；a list of prizewinners。',
 'prizewinners 是拿到奖的人，prizes 是奖项、奖品；复合词末尾 winner 决定这里指向人。',
 ('The judges announced the prizewinners at the end of the evening.','评委在晚会结束时宣布了获奖者。'),('Previous prizewinners returned to meet this year’s finalists.','往届获奖者回来，与今年的决赛入围者见面。'),sources=S('prizewinners','prize'))
W('sweepstakes','/ˈswiːpsteɪks/','抽奖、有奖竞赛；旧式合赌注竞赛',
 '广告里报名后等抽取大奖，常能看到 sweepstakes。旧名字的画面是把大家押上的赌注一扫而得，现代抽奖不要求仍照旧式赌局组织。',
 'sweep 扫 + stake 赌注，接旧 sweep stake 赢走所有赌注的表达；后发展竞赛、抽奖名称。尤其美式 a sweepstakes 可说一项活动，不能只凭结尾 s 就数成多项。',SWEEP,
 'enter a sweepstakes 参加抽奖；a sweepstakes winner 抽奖获奖者。',
 'a promotional sweepstakes 促销抽奖；win a sweepstakes。',
 'sweepstakes 常见于抽奖，competition 可以按表现、技巧评选；具体规则仍由活动说明决定，词本身不写出全部要求。',
 ('The magazine announced the winner of its annual sweepstakes.','杂志宣布了年度抽奖的获奖者。'),('The advertisement invited readers to enter a sweepstakes.','广告邀请读者参加抽奖。'),sources=S('sweepstakes','sweepstakes'))
W('stakeout','/ˈsteɪkaʊt/','守候监视；蹲守',
 '侦探小说里，人守在一个地点等目标出现，整段守候监视叫 stakeout。它把注意力放在持续观察，不一定已有逮捕。',
 '由 stake out 相关动词短语形成名词；短语较早用桩标界，后来有守候监视地点义。现代名词常连写，动词短语分写。',STAKEOUT,
 'on a stakeout 在蹲守；a long stakeout 长时间守候监视。',
 'conduct a stakeout 进行守候监视；after a stakeout 蹲守之后。',
 'stakeout 是监视、等待，raid 是突袭行动；影视里可能先有蹲守再突袭，但两个词不是同一阶段。',
 ('The detective spent the night on a stakeout in the novel.','小说里，侦探整夜都在蹲守。'),('The film opens with a stakeout that lasts for hours.','电影以一场持续数小时的蹲守开场。'),sources=S('stakeout','stake-out'))
W('stakeouts','/ˈsteɪkaʊts/','守候监视、蹲守活动〔复数〕',
 '不是一次长等，而是多次安排守候监视，便可叫 stakeouts。最后 -s 只数活动，不改变 stakeout 的角色、用途。',
 'stakeout + -s，/t/ 后读 /s/；内层对应 stake out 相关短语，现成名词再加复数。',STAKEOUT,
 'long stakeouts 长时间蹲守；several stakeouts 几次蹲守。',
 'stories about stakeouts；stakeouts in detective films。',
 'stakeouts 是守候监视的活动，lookouts 可以指放哨、观察的人或观察点；一个说活动，一个还可能说角色、位置。',
 ('The novel describes several unsuccessful stakeouts.','小说描写了几次无果的蹲守。'),('He said detective work involved more paperwork than exciting stakeouts.','他说侦探工作里的文书事务，比刺激的蹲守更多。'),sources=S('stakeouts','stake-out'))
W('gainfully','/ˈɡeɪnfəli/','有收入、能取得经济回报地',
 'gainfully employed 常见于较正式文字：人有一份能带来收入的工作。它不负责夸这份工作有多幸福、薪水有多高。',
 '现代对应 gainful + -ly，内层 gain + -ful；较早形式、记录的先后不必和现代学习拆分完全同序，常用搭配整体记。',
 [['gain 收益 + -ful → gainful','能带来收益的性质材料'],['现代对应 gainful + -ly → gainfully','有经济回报地；不据短词先学断定所有记录先后']],
 'gainfully employed 有收入地就业；gainfully occupied 从事有报酬的活动。',
 'remain gainfully employed；become gainfully employed。',
 'gainfully employed 强调有收入的工作，happily employed 强调工作满意；报酬与感受是不同信息。',
 ('She remained gainfully employed while finishing her degree.','她完成学位期间，一直有一份有收入的工作。'),('The report asked how many graduates were gainfully employed.','报告问有多少毕业生已从事有报酬的工作。'),sources=S('gainfully','gainful'))
W('yielded','/ˈjiːldɪd/','产出、给出了；让步、屈服了',
 '实验给出有用结果，是 yielded useful results；压力太大，最后让了一步，也用 yielded。现代几条义都能借“给出来、让出去”串联。',
 'yield + 完整 -ed，/d/ 后读 /ɪd/；基础词接古英语支付、交出等材料，后来有产出、屈服等用途，不全从庄稼收成这一义派生。',YIELD+[['yield + -ed → yielded','过去给出、产出，或屈服、让步']],
 'yielded results 得到结果；yielded to pressure 向压力让步。',
 'yielded a crop 产出庄稼；yielded under the weight 被重量压得弯、塌。',
 'yielded useful results 是产出，yielded to a demand 是让步；是否有 to、后面是什么对象，决定怎么理解。',
 ('The experiment yielded useful results.','实验得到了有用结果。'),('He eventually yielded to their request.','他最终答应了他们的要求。'),sources=S('yielded','yield'))
W('unyielding','/ʌnˈjiːldɪŋ/','不让步的、坚定不移的；坚硬不易变形的',
 '手压一块硬木，压不下去，是 unyielding；人面对压力也不肯松口、改立场，同样像压不动。这个画面可以记义，不等于物质用法在英语里先出现。',
 'un- 不 + yielding 会让、会弯的；人的不让步义记录早于部分物质不易变形义。yield 的较早历史接支付、交出材料。',YIELD,
 'an unyielding attitude 不肯让步的态度；an unyielding surface 坚硬不让的表面。',
 'unyielding opposition 坚决反对；an unyielding demand 不肯松口的要求。',
 'unyielding 可以夸坚定，也可以批评固执，取决于立场；firm 也能说坚定，通常少一点硬顶不动的强度。',
 ('She remained unyielding in her opposition to the plan.','她对那项计划的反对立场始终坚定。'),('The mattress felt hard and unyielding.','床垫又硬又不下陷。'),sources=S('unyielding','unyielding'))
W('unyieldingly','/ʌnˈjiːldɪŋli/','不肯让步地；坚定不移地',
 '对方一再要求变更，他仍然守着原来的立场，unyieldingly 写这种压不动、不松口的方式。褒贬由说话人怎么评价决定。',
 'unyielding + -ly；内层 un- 不 + yielding 让步、变形。副词这一层修饰坚持、拒绝、反对等，不是直接把产量 yield 否定掉。',YIELD+[['unyielding + -ly → unyieldingly','以不松动、不让步的方式']],
 'unyieldingly opposed 坚决反对；stand unyieldingly 坚定站住立场。',
 'unyieldingly firm 坚定不移；refused unyieldingly 不肯松口地拒绝。',
 'unyieldingly 描述不让步，patiently 描述耐心；一个人可能很耐心地解释，却仍坚定不肯改变条件。',
 ('She stood unyieldingly by her decision.','她坚定不移地坚持自己的决定。'),('He remained unyieldingly opposed to the proposal.','他始终坚决反对那项提议。'),sources=S('unyieldingly','unyielding'))
W('stockpiles','英 /ˈstɒkpaɪlz/；美 /ˈstɑkpaɪlz/','储备物资〔复数〕；积存、储备〔第三人称单数〕',
 '仓库里为以后留的一批批物资，是 stockpiles；机构每年往里增加一批，动词也用 stockpiles。它让人看到有计划留出的储备。',
 'stockpile + -s，/l/ 后读 /z/；内层 stock 储备 + pile 堆，先有堆存物名词，后有动词。',STOCK+[['stockpile + -s → stockpiles','多批储备，或它积存物资']],
 'food stockpiles 食物储备；stockpiles of materials 材料储备。',
 'stockpiles supplies 储备物资；large stockpiles。',
 'stockpiles 常像为将来需要而集中保存，piles 只说一堆堆；一堆杂物不一定是有意留用的储备。',
 ('The warehouse held large stockpiles of building materials.','仓库里存着大批建筑材料储备。'),('The organisation stockpiles supplies before the rainy season.','机构在雨季前储备物资。'),sources=S('stockpiles','stockpile'))
W('stockpiled','英 /ˈstɒkpaɪld/；美 /ˈstɑkpaɪld/','积存、储备了；被留作储备的',
 '入冬前，把燃料、食物等一批批留下，过去做过这件事，就是 stockpiled。它说留作后用，不保证东西最后一定派上用场。',
 'stockpile 去 e 加完整 -ed，/l/ 后读 /d/；内层 stock + pile，动词由较早名词转用。',STOCK+[['stockpile + -ed → stockpiled','过去集中积存物资，或已被留作储备']],
 'stockpiled food 储备的食品；stockpiled materials 积存的材料。',
 'stockpiled for winter 为冬天储备；supplies were stockpiled。',
 'stockpiled 强调集中留用，distributed 强调分发出去；物资可以先储备，再按需要发出。',
 ('The village stockpiled firewood before winter.','村里在入冬前储备了柴火。'),('The company had stockpiled spare parts for future repairs.','公司已为将来维修储备了零件。'),sources=S('stockpiled','stockpile'))
W('amass','/əˈmæs/','聚集、积累大量',
 '一件件添，最后成了一大堆；钱、证据、粉丝都能 amass。这个词比普通拿到更突出最后聚出来的量。',
 '经法语 amasser，内层 à 朝向 + masser 聚成团，接 masse 团、堆。可以对应 a- 与 mass 认材料，但不是现代英语冠词 a 加 mass 临时拼成动词。',AMASS,
 'amass a fortune 积累大笔财富；amass evidence 收集大量证据。',
 'amass a collection 积成大批收藏；amass information 汇集大量信息。',
 'amass 突出聚到很多，hoard 常突出存着不放；收集大量证据可说 amass，不一定有不肯分享的意味。',
 ('The researcher managed to amass a large collection of letters.','研究者设法收集了一大批信件。'),('It took years to amass enough evidence for the book.','为写这本书收集足够证据，花了好几年。'),sources=S('amass','amass'))
W('amasses','/əˈmæsɪz/','聚集、积累大量〔第三人称单数〕',
 '一个人不断找资料，手里的记录越攒越多，是 amasses records。它让人看到从小份到大批的聚集。',
 'amass + -es，/s/ 后读 /ɪz/，多一个音节；基础词借法语聚成一堆的动词材料。',AMASS+[['amass + -es → amasses','他或它聚集大量某物']],
 'amasses evidence 收集大量证据；amasses wealth 积累财富。',
 'amasses data 积累大量数据；amasses a following 聚集大批追随者。',
 'amasses evidence 只是证据数量增多，proves a claim 才是论证说法；数量多不自动决定结论。',
 ('The historian amasses evidence from many different archives.','历史学家从许多不同档案馆收集大量证据。'),('The character amasses a fortune but loses his closest friends.','那个角色积累了大笔财富，却失去最亲近的朋友。'),sources=S('amasses','amass'))
W('amassed','/əˈmæst/','聚集、积累了大量',
 '多年买书、查档案，最后手里已是一大批资料，可以说 amassed a collection。它强调一段过程后的大量所得。',
 'amass + 完整 -ed，/s/ 后读 /t/；拼写保留词干 ss，不因为看见 -ed 就添一个 /ɪd/ 音节。',AMASS+[['amass + -ed → amassed','过去聚成了大量物品、信息等']],
 'amassed a fortune 积起大笔财富；amassed a collection 积成大批收藏。',
 'amassed over decades 几十年积累的；amassed enough evidence。',
 'amassed 常突出聚成很大数量，earned 强调挣得；财富可以来自不同渠道，amassed 本身不说明全部来源。',
 ('She amassed a remarkable collection of old maps.','她收集了一批很可观的旧地图。'),('The team amassed enough data to test the idea.','团队积累了足够数据来检验那个想法。'),sources=S('amassed','amass'))
W('amassing','/əˈmæsɪŋ/','正在聚集、积累大量',
 '证据、资料一份份进入手里，已经形成越积越多的势头，叫 amassing。通常比随手拿几件东西更有积成大批的感觉。',
 'amass + -ing；词基原有 ss 保留，现代过程形式对应聚集大量这一动作。',AMASS+[['amass + -ing → amassing','不断聚集、积成大量的过程']],
 'amassing evidence 收集大量证据；amassing wealth 积累财富。',
 'amassing a collection；amassing information from many sources。',
 'amassing 关注量的聚集，organising 关注整理结构；资料攒得多，不等于已经分门别类整理好。',
 ('The journalist spent months amassing evidence.','记者花了几个月收集大量证据。'),('He was more interested in amassing books than in reading them.','比起读书，他更热衷于把书越攒越多。'),sources=S('amassing','amass'))
W('accumulates','/əˈkjuːmjəleɪts/','逐渐积聚、积累〔第三人称单数〕',
 '灰尘没人管，天天添一点，最后盖满桌面，是 accumulates；知识、经验也能随着时间慢慢加起来。',
 'accumulate + -s，/t/ 后读 /s/；上接拉丁 ad- 与 cumulare 堆起，ad- 在 c 前同化，英语词尾这一层另按现代规则。',ACC+[['accumulate + -s → accumulates','它逐渐增加成一堆、更多数量']],
 'dust accumulates 灰尘积聚；knowledge accumulates 知识积累。',
 'accumulates over time 随时间积起来；accumulates on the surface。',
 'accumulates 可以是灰尘自己越积越多，amasses 常更像某主体主动聚起大量东西；主语、动作关系不同。',
 ('Dust accumulates quickly on the shelves.','架子上很快就会积灰。'),('Experience accumulates over years of practice.','经验随着多年实践慢慢积累。'),sources=S('accumulates','accumulate'))
W('accumulated','/əˈkjuːmjəleɪtɪd/','逐渐积累、积聚了；积存的',
 '平时每次省一点，后来攒出一笔钱，是 accumulated savings；灰尘、工作任务也能越积越多。它不要求这些东西受人欢迎。',
 'accumulate 去 e 加完整 -ed，/t/ 后读 /ɪd/。可作过去式、过去分词，也可形容已经积起来的一批东西。',ACC+[['accumulate + -ed → accumulated','过去逐渐增加，或已积存下来的性质']],
 'accumulated knowledge 积累的知识；accumulated dust 积灰。',
 'accumulated over the years 多年积累；accumulated savings 积蓄。',
 'accumulated 表逐步累加，inherited 表继承而来；一笔钱可以两种来源都有，词各自说明不同过程。',
 ('We cleared away the dust that had accumulated over the winter.','我们清掉了整个冬天积下的灰尘。'),('She used her accumulated savings to buy the equipment.','她用积蓄买了那套设备。'),sources=S('accumulated','accumulate'))
W('accumulating','/əˈkjuːmjəleɪtɪŋ/','正在积累、积聚；不断增加的',
 '不是一下出现一大堆，而是每天添一点，积得越来越多，就是 accumulating。它既能写人主动积累，也能写物体自然堆起。',
 'accumulate 去 e 加 -ing；内层拉丁 cumulus 堆的画面帮助理解，现代动作形式说明累加过程。',ACC+[['accumulate + -ing → accumulating','一点点聚多的过程或性质']],
 'accumulating evidence 不断增加的证据；accumulating knowledge 积累知识。',
 'snow accumulating outside 外面不断积雪；accumulating experience。',
 'accumulating 通常突出不断增加，gathering 还可说把原本分散的东西一次聚到一起；时间、过程感不同。',
 ('Snow was accumulating on the roof.','屋顶上的雪越积越多。'),('The course focuses on using knowledge, not merely accumulating facts.','课程注重运用知识，而不只是积攒事实。'),sources=S('accumulating','accumulate'))
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_zhi',ROOTS,WORDS)
 extend_lessons()
