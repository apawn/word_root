"""Shore, victim, weekly and consumer: coastlines, suffering, frequency and consumption."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
S=[['中古英语 schore 等 → shore〔岸〕','水域边的陆地，深源有不同分析'],['方向与边界组合','a-/on-/off- + shore；shore + line'],['另一路低地德语、荷兰语支柱词 → shore〔支撑〕','支撑柱、支撑；shore up 是撑住，不是搬到岸上']]
W('shore','英 /ʃɔː/；美 /ʃɔːr/','岸、滨；支撑柱；撑住、加强〔shore up〕',
 '水和陆地接上的地方是 shore；句里 shore up a wall 却像用柱子撑墙，选的是另一条支撑词来源。',
 '岸义来自中古英语 schore 等，可能有更早英语形式；支柱义接中古低地德语、荷兰语相关支撑词。两支同形，不能所有现代用法都从海边硬推。',S,
 'on the shore 在岸上，reach the shore 到岸边，shore leave 船员上岸休假，shore up a wall 撑墙，shore up confidence 增强信心。',
 'on the shore；reach the shore；shore leave；shore up。',
 'shore 岸可接海湖等水域，beach 特别指沙、石等构成的滩面；shore up 的撑住另源，不是把信心搁到岸上。',
 ('We watched the boats from the shore.','我们从岸上看那些船。'),('Workers used wooden beams to shore up the wall.','工人用木梁撑住墙。'))
W('shoreline','英 /ˈʃɔːlaɪn/；美 /ˈʃɔːrlaɪn/','岸线、海岸线；水陆交界线',
 '沿着水碰到陆地的边缘描一条线，就是 shoreline；可以是实际边界，也可以是地图上的线。',
 'shore 岸 + line 线，不是说岸边必须修一条直线；岸线会弯曲，也随潮水、水位等变。',S[:1]+[['shore + line → shoreline','水陆边界及地图表示']],
 'a rocky shoreline 多岩岸线，the lake’s shoreline 湖岸线，follow the shoreline 沿岸线走。',
 'a rocky shoreline；the lake’s shoreline；follow the shoreline。',
 'shoreline 更聚焦交界边缘，coast 可说较广海岸地区；湖也有 shoreline，不必强改成海岸。',
 ('The path follows the lake’s shoreline.','小路沿着湖岸延伸。'),('The map shows changes in the shoreline.','地图显示了岸线的变化。'))
W('ashore','英 /əˈʃɔː/；美 /əˈʃɔːr/','在岸上；向岸上、上岸',
 '人在船上、水里，后来到了陆地那一边；它本身是位置、方向副词，不需要再照中文补一个 on。',
 'a-〔接在、向等旧位置材料〕+ shore，构成在岸上、到岸上的副词；不是 a 这个冠词加岸就表示一片海岸。',S[:1]+[['a- + shore → ashore','在岸上，或移向岸上']],
 'go ashore 上岸，come ashore 到岸上，wash ashore 被冲上岸，spend the night ashore 在岸上过夜。',
 'go ashore；come ashore；wash ashore；stay ashore。',
 'ashore 常修饰上岸、在岸动作，onshore 可作形容词修饰岸上设施等；通常不说 go to ashore。',
 ('The passengers went ashore after lunch.','乘客午饭后上了岸。'),('Pieces of wood washed ashore after the storm.','风暴后，一些木块被冲上岸。'))
W('onshore','英 /ˈɒnʃɔː/；美 /ˈɑːnʃɔːr/','岸上的、陆上的；向岸的；境内的',
 '设施放在陆上，或风从海朝岸吹；商业语境又可按相对 offshore 的关系说留在境内。',
 'on 在、向 + shore 岸，组合为形容词、副词，后有生产服务位置等引申。不是所有 onshore 都只在紧挨海边几米内。',S[:1]+[['on + shore → onshore','岸上、向岸；相对离岸的境内位置']],
 'onshore wind 向岸风，onshore wind farms 陆上风电场，onshore operations 陆上、境内业务。前两搭配中的 wind 分别是风向与能源设施对象。',
 'an onshore breeze；onshore operations；onshore wind farms。',
 'onshore breeze 吹向陆地，onshore wind farm 说设施位于陆地，不表示风机只在向岸风里转。',
 ('An onshore breeze cooled the beach.','一阵向岸微风让海滩凉快了些。'),('The company moved some operations onshore.','公司把一些业务转回了境内。'))
W('offshore','英 /ˌɒfˈʃɔː/；美 /ˌɔːfˈʃɔːr/，也见前重音','离岸的、海上的；向外海的；境外的',
 '离开岸边，在海里布置设施；业务也可移到本国之外，借离开本岸的关系称 offshore。',
 'off 离开 + shore 岸，形成方向、位置词，再接境外业务等用法。词本身不说明一种业务是否合法。',S[:1]+[['off + shore → offshore','离岸、海上、朝外海'],['经济位置引申','境外安排、在外国开展的业务']],
 'an offshore wind farm 海上风电场，offshore drilling 海上钻探，an offshore breeze 离岸风，offshore operations 境外业务等。',
 'offshore wind farms；offshore drilling；offshore operations。',
 'offshore wind 是离岸风向时要看搭配；offshore wind farm 则是风机在海上。offshore/onshore 常对照，但并不总是同一个领域。',
 ('The island has a large offshore wind farm.','岛外海上有一座大型风电场。'),('The boat waited a short distance offshore.','船在离岸不远处等候。'))
R('B4299','水陆边界与在岸、离岸方向；支撑义另源','SHORE：岸；SHORE UP：用支撑撑住','shore → shoreline；ashore 上岸；onshore 陆上向岸；offshore 海上离岸；foreshore 等按前滨分支。',
 '风向与风电设施位置要看完整搭配。shore up 的支撑不接海岸词源；shored 的少见带某种岸线性质先不单列。',
 'schore 等 → shore 岸；shore + line；a-/on-/off- + shore；sea/lake/fore + shore；另一支柱词 → shore up。',
 [['岸边基础与岸线','shore · shoreline · seashore · lakeshore · foreshore'],['位置与移动方向','ashore · onshore · offshore']],
 'shore/beach 岸与滩；onshore/offshore wind 的风向、设施位置按后文选；shore up 支撑另源。',
 'We came ashore and followed the shoreline while the boat waited offshore.\n\n我们上岸后沿岸线走，船则在离岸处等着。','shore shoreline seashore lakeshore foreshore ashore onshore offshore')
V=[['拉丁 victima → 法语 victime、英语 victim','祭献中的牺牲对象，深源不定'],['英语受害者义','遭人、事故、处境等伤害的人'],['英语派生','victimize 使受害；victimization 受害、欺凌过程；victimhood 身份处境；victimless 无受害者的']]
W('victim','/ˈvɪktɪm/','受害者、受骗者；牺牲品',
 '伤害落在谁身上，谁就是 victim；可能来自犯罪、事故，也可能来自一次骗局或不利处境，不要求一定已经死亡。',
 '来自拉丁 victima 的祭献对象，经法语等借入；后来扩成受伤害、被利用的人。更远来源未定，不能看见 vict- 就套成 victor 胜利者的反面。',V,
 'a victim of fraud 骗局受害者，an accident victim 事故伤者、死伤者等，fall victim to 成为……受害者。',
 'a victim of；fall victim to；an accident victim；a fraud victim。',
 'victim 受害者不必死亡，casualty 在事故战争中另有伤亡等范围；victor 胜者与 victim 不靠同拼写前三字母强拼一条直接词源。',
 ('The victim of the theft reported the missing bag.','失窃者报失了丢掉的包。'),('Several small shops fell victim to the scam.','几家小店成了骗局的受害者。'),
 sources=['https://www.etymonline.com/word/victim','https://en.wiktionary.org/wiki/victim#English'])
W('victimize','/ˈvɪktɪmaɪz/','欺凌、迫害；使受害、使上当',
 '有人把欺骗、不公、伤害加到别人身上；victimize 把受害者身份翻成使对方受害的动作。',
 'victim + -ize，使进入相应受害处境。另有 victimise 的常见英式拼法，不能把 -ize 当“本人自愿成为”。',V[:2]+[['victim + -ize → victimize','使别人遭受伤害、欺凌或诈骗']],
 'victimize vulnerable people 伤害、欺凌脆弱者，be victimized by a scam 被骗局坑害，victimize an employee 不公对待员工。',
 'victimize someone；be victimized by；repeatedly victimized。',
 'victimize 动作主体可为人或安排，victim 是承受者；criticize 批评本身不必等于不公欺凌。',
 ('The scheme was designed to victimize inexperienced buyers.','这个骗局专门坑害缺乏经验的买家。'),('The character is repeatedly victimized by his classmates.','这个人物反复受到同学欺凌。'))
W('victimization','英 /ˌvɪktɪmaɪˈzeɪʃən/；美也常 /ˌvɪktɪməˈzeɪʃən/','使受害、欺凌、迫害；受害经历',
 '把伤害、排挤某人的整件过程拿出来谈，也可谈承受它留下的处境；不只是一个人的称号。',
 'victimize + -ation，对应 victim + -ization；动词末尾 e 在后缀前不保留，重音移到后段。',V[:2]+[['victimize + -ation → victimization','使受害的行为、过程与经历']],
 'repeated victimization 反复受害，a fear of victimization 对遭报复迫害的担心，a victimization survey 受害经历调查。',
 'repeated victimization；a fear of victimization；a victimization survey。',
 'victimization 多说发生的伤害、欺凌过程，victimhood 多说受害者处境或自我认同；不能只因中文都能有受害就总互换。',
 ('The study examines repeated victimization at school.','研究考察了校园中的反复受害经历。'),('Workers described a fear of victimization after speaking out.','工人说，发声后他们担心遭到报复迫害。'))
W('victimhood','/ˈvɪktɪmhʊd/','受害者处境、受害身份或自我认同',
 '把“作为受害者”这一状态放到讨论中心；可以是客观处境，也可以是人怎样看待自己的身份。',
 'victim + -hood，状态、身份后缀，不是 hood 帽兜那种实物。',V[:2]+[['victim + -hood → victimhood','受害者状态、身份和相应感受']],
 'a sense of victimhood 受害者心态或自觉，shared victimhood 共同受害处境，move beyond victimhood 超越只以受害身份看待自己。',
 'a sense of victimhood；shared victimhood；the language of victimhood。',
 'victimhood 本身不自动断言受害是假的；有时中性分析处境，有时批评过度以受害定位自己，语气看上下文。',
 ('The essay explores the relationship between memory and victimhood.','文章探讨了记忆与受害身份之间的关系。'),('Shared victimhood brought the characters together.','共同的受害处境让这些人物走到了一起。'))
W('victimless','/ˈvɪktɪmləs/','无受害者的；被认为没有直接受害者的',
 '称某行为 victimless，是在说找不到直接承受伤害的那个人；这个说法也常正是争论的焦点。',
 'victim + -less 无……的，修饰行为等。victimless crime 是固定讨论表达，不能看到这个标签就替作者证实毫无伤害。',V[:2]+[['victim + -less → victimless','没有受害者、或被这样看待']],
 'a victimless crime 所谓无受害者犯罪，supposedly victimless 被认为无直接受害者的，a victimless act 无受害者的行为。',
 'a victimless crime；supposedly victimless；a victimless act。',
 'victimless 评价的是有没有受害对象，不等于 harmless 各种方面都无害，也不等于 legal 合法。',
 ('The article questions whether the offence is truly victimless.','文章质疑这种违法行为是否真的没有受害者。'),('They disagreed about the label “victimless crime”.','他们对“无受害者犯罪”这一标签有分歧。'))
R('B3799','伤害落在哪一方，再分动作、经历与身份','VICTIM：承受伤害的人，不一定已经死亡','victim → victimize → victimization；victimhood 处境身份；victimless 对直接受害者有无的判断。',
 '过程、身份与标签各自回答不同问题。说 victimhood 未必否认真实受害；称 victimless 也不等于已经证明没有任何伤害。',
 'victima → victime、victim；victim + -ize/-hood/-less；victimize + -ation → victimization。',
 [['受害者、使受害与过程','victim · victimize · victimization'],['身份与受害者有无','victimhood · victimless']],
 'victimization/victimhood 受害过程与身份；victimless/harmless 无直接受害者标签与无害；victim/victor 不按外形强串。',
 'The report describes the victims’ experiences without reducing their whole lives to victimhood.\n\n报告描述了受害者的经历，也呈现了他们人生中受害身份之外的部分。','victim victimize victimization victimhood victimless')
R('B2694','按周计频率，biweekly 要查清一次还是两次','WEEKLY：每周；BIWEEKLY：有两种常见频率','weekly → biweekly，bi- 在实际用法中可能每两周一次，也可能每周两次。',
 '具体安排里用 every two weeks、twice a week 最清楚；频率歧义不能只靠坚持一个前缀解释消除。',
 'week + -ly → weekly；bi- + weekly → biweekly。',
 [['每周与两种 biweekly 频率','weekly · biweekly']],
 'weekly 每周；biweekly 两周一次或一周两次，按明文日期判断。',
 'Our weekly meeting stays on Monday; the biweekly report is issued every two weeks.\n\n每周会议仍在周一；这里说的 biweekly 报告明确为每两周发布一次。','weekly biweekly')
C=[['consume → consumer','消费、使用的人或群体'],['consumer + -ism → consumerism','重消费、重购买的观念；另一支消费者权益主张'],['consumer + -ist → consumerist','相关主张者或相应性质，要选对 consumerism 的意思']]
W('consumerism','英 /kənˈsjuːmərɪzəm/；美 /kənˈsuːmərɪzəm/','消费主义、重购买的风气；消费者权益保护主张',
 '一边是把买更多、拥有更多看得很重；另一种用法却是维护消费者利益。不是每次见这个词都在赞买买买。',
 'consumer 消费者 + -ism，观念、主张名词；不同历史用法形成了重消费与消费者保护两支。',C[:2],
 'mass consumerism 大众消费主义，criticize consumerism 批评消费主义，consumerism and consumer protection 消费者运动与权益保护〔按所用义〕。',
 'mass consumerism；criticize consumerism；the rise of consumerism。',
 'consumption 消费行为、消耗量，consumerism 消费观念、风气或权益运动；后缀 -ism 不等于每次都同一政治立场。',
 ('The film criticizes the emptiness of consumerism.','影片批评了消费主义的空虚。'),('The chapter uses consumerism to mean the movement for consumer protection.','这一章用 consumerism 指维护消费者权益的运动。'),
 sources=['https://www.merriam-webster.com/dictionary/consumerism','https://en.wiktionary.org/wiki/consumerism#English'])
W('consumerist','英 /kənˈsjuːmərɪst/；美 /kənˈsuːmərɪst/','消费主义的、主张消费主义者；消费者权益倡导者〔依语境〕',
 '讲 consumerist culture 常说围绕购买、占有来组织的文化；旧运动语境也可能说站在消费者利益一方的人。',
 'consumer + -ist，与 consumerism 对应，能作人物名词，也能作相关性质形容词；不是词尾有 -ist 就永远只能作职业。',C,
 'a consumerist culture 消费主义文化，consumerist values 消费主义价值观，a consumerist campaign 消费者权益倡导活动〔相应语境〕。',
 'a consumerist culture；consumerist values；a consumerist campaign。',
 'consumer 购买、使用商品的人，consumerist 是观点或性质；普通消费者不一定热衷消费主义，也不一定从事权益倡导。',
 ('The novel portrays a deeply consumerist society.','小说描绘了一个深受消费主义影响的社会。'),('The historian describes the campaigners as early consumerists.','历史学家把这些倡导者称为早期消费者权益推动者。'),
 sources=['https://www.merriam-webster.com/dictionary/consumerism','https://en.wiktionary.org/wiki/consumerist#English'])
R('B3948','消费者到重消费观念，也可到权益主张','CONSUMER：使用、购买者；后缀再谈立场','consumer → consumerism、consumerist；把购买行为、消费观念与消费者保护分清。',
 'consumerism 两支意思可能给相反阅读印象，先看文章是在批评物质购买，还是讨论消费者利益。',
 'consume + -er → consumer；consumer + -ism/-ist → consumerism、consumerist。',
 [['消费者角色','consumer'],['观念与相关主体、性质','consumerism · consumerist']],
 'consumption/consumerism 行为量与观念运动；consumer/consumerist 身份与立场；-ist 名词形容词都可。',
 'A consumer can question consumerist values without giving up every purchase.\n\n消费者也可以质疑消费主义价值观，并不因此完全停止购买。','consumer consumerism consumerist')
if __name__=='__main__':save('continuation_20261030_fx',ROOTS,WORDS)
