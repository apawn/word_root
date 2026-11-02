"""Nearby things, possessions, pursuit, hiding and pressure."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'C1583':dict(words=['surround','surrounding','surroundings'],label='surround：旧波浪词如何变成围绕',note='surround 历史接 superundare 溢流，后来语义、拼写受 round 的声音联想影响；现代 surround + -ing → surrounding，再有 surroundings 周围环境。'),
 'B3069':dict(words=['belong','belonging','belongings'],label='belongings：属于自己的物品',note='belong 的 be- 有加强作用，旧 longen、langian 有关系、相属材料，更早连接不确定。belonging 可说归属感，belongings 常指私人物品。'),
 'B3768':dict(words=['earn','earning','earnings'],label='earn、earning、earnings：付出与所得',note='earn 接旧劳动、赢得报酬词族；earning 为动作或相应分词，earnings 常说收入。'),
 'B3527':dict(words=['crack','cracker','crackers'],label='crackers 的名词与英式俚语形容词',note='名词 crackers 是 cracker 复数；英式俚语形容词说疯狂、荒唐，与 cracked 等比喻材料有联系，不按饼干的复数直译。'),
 'B2839':dict(words=['catch','chase','chaser'],label='catch 与 chase：同源分途借入，抓到与追逐分工',note='catch、chase 同接法语与通俗拉丁试图抓取词族，借入形式、现代重点不同；chaser 为追逐者等。'),
 'C1594':dict(words=['abuse','abuser'],label='abuse 与 abuser：滥用或虐待的执行者',note='abuser 接动词 abuse，-er 指人，词干 /z/ 保留；名词 abuse 常读 /s/，不能按其读音造执行者词。'),
 'A1697':dict(words=['lurk','lurker','crush','crusher'],label='lurk 与 crush 先学动作，再看 -er 人或机器',note='lurker 是藏着观察的人，现代网络语境常指只看不发言者；crusher 是压碎者或破碎设备。'),
 'A1741':dict(words=['lurk','lurking'],label='lurking：藏在表面后面的动作或状态',note='lurk + -ing，既说隐蔽待着，也可说未显露的风险、疑虑；网络用法还可说只看不发言。'),
}
W('surrounding','/səˈraʊndɪŋ/','周围的；围绕、包围；surround 的 -ing 形式',
 '视线从一个中心向外扫，围在它四周的山、村庄、道路是 surrounding 的东西。',
 '现代 surround + -ing。surround 较早经法语接拉丁 superundare 溢流，后来在法语意义和英语 round 的声音联想影响下形成围住义，拼写也受影响。现代拆分有用，历史不能只按 sur + round 处理。',
 [['拉丁溢流词族 → 法语／英语 surround','较早溢流，后来发展为包围、环绕'],['surround + -ing → surrounding','周围的；围绕某物']],
 'the surrounding area 周边地区；surrounding villages 周围村庄；trees surrounding the house 围着房子的树；questions surrounding the decision 围绕决定的疑问。',
 'the surrounding countryside；surrounding conditions。','surrounding 是形容词或分词；surroundings 是周围环境的常用复数形名词。说周边地区 the surrounding area，说熟悉环境 get used to the surroundings。',
 ('The surrounding hills were covered in mist.','周围的山笼罩在薄雾里。'),('We explored the town and the surrounding villages.','我们游览了小镇和周围的村庄。'),sources=['https://www.etymonline.com/word/surround','https://en.wiktionary.org/wiki/surrounding#English'])
W('surroundings','/səˈraʊndɪŋz/','周围环境、四周的事物',
 '你站在一个地方，四面的房子、声音、景物合起来，就是 your surroundings。它常说人或物眼下所在的具体环境。',
 'surround + -ing + -s，名词化为围在周围的事物。上接 surround 的围住义；它更早的词族有溢流材料，后来语义发展和 round 的联想另需分层理解。',
 [['surround → surrounding','围绕；周围的'],['名词化并用复数 surroundings','围在四周的一切 → 周围环境']],
 'familiar surroundings 熟悉环境；beautiful surroundings 优美周边；new surroundings 新环境；blend into the surroundings 融入周围背景。',
 'get used to your surroundings；notice the surroundings。','surroundings 常指身边具体环境；environment 可以更广，说工作、社会、生态等条件体系。名词 surroundings 通常保留复数形式。',
 ('It took her a few days to get used to her new surroundings.','她花了几天才适应新环境。'),('The hotel stands in peaceful surroundings.','酒店周围环境安静。'),sources=['https://www.etymonline.com/word/surround','https://en.wiktionary.org/wiki/surroundings#English'])
W('belongings','英 /bɪˈlɒŋɪŋz/；美 /bɪˈlɔːŋɪŋz/ 或 /bɪˈlɑːŋɪŋz/','个人物品、随身财物',
 '收拾包时，把属于自己的衣服、书、钥匙等放进去，这些东西合起来叫 belongings。',
 'belong + -ing + -s，形成属于某人的物品这一名词。belong 较早为 be- 加 longen、langian 等相属、相关材料，更早词源连接有不确定性。',
 [['belong 的旧相属、相关词族','属于某人；与某处、群体相属'],['belonging + -s → belongings','属于自己的东西 → 个人物品']],
 'personal belongings 私人物品；collect your belongings 收拾个人物品；leave belongings behind 遗留东西；all her belongings 她的全部个人财物。',
 'pack one’s belongings；take one’s belongings。','a sense of belonging 是归属感；belongings 常是东西。表示某一件私人物品通常说 a personal item，不把 belongings 随手去 s 套同一意思。',
 ('Please take all your belongings when you leave the train.','下火车时，请带齐个人物品。'),('She packed her belongings into two boxes.','她把自己的东西装进了两个箱子。'),sources=['https://www.etymonline.com/word/belong','https://en.wiktionary.org/wiki/belongings#English'])
W('earning','英 /ˈɜːnɪŋ/；美 /ˈɝːnɪŋ/','赚钱、赢得；earn 的 -ing 形式；收入获取这一过程',
 '做事之后得到报酬，或靠表现赢得信任。earning 看的是正在取得、通过付出获取的过程。',
 'earn + -ing；earn 接古英语 earnian 劳动而获报、值得得到等词族，更早材料与劳动、收获相关。现代 earning 可作分词、动作名词或修饰成分。',
 [['古英语 earnian → earn','劳动、应得、赢得报酬'],['earn + -ing → earning','挣钱、赢得的过程或动作']],
 'earning money 赚钱；earning a living 谋生；earning trust 赢得信任；earning potential 收入潜力。earnings 常指挣得的钱。',
 'earning respect；an earning capacity。','earning 是过程或动作，earnings 通常是收入结果。earning someone’s respect 是通过表现赢得尊重，不必涉及金钱。',
 ('She is earning money by teaching music.','她靠教音乐赚钱。'),('The new team is slowly earning the community’s trust.','新团队正逐渐赢得社区的信任。'),sources=['https://www.etymonline.com/word/earn','https://en.wiktionary.org/wiki/earning#English'])
W('crackers','英 /ˈkrækəz/；美 /ˈkrækərz/','薄脆饼干等〔cracker 复数〕；英式口语形容词：疯狂、荒唐的',
 'cheese and crackers 是奶酪配薄脆饼；That’s crackers 却可能是“这太荒唐了”。形容词义通常放在表语位置，语气很口语。',
 '名词是 cracker + -s，cracker 与 crack 的破裂、爆响等词族相连。俚语形容词的具体来源有不同解释，常联系 cracked 等头脑失常的比喻和类似改形；现代按名词与形容词两类使用。',
 [['cracker + -s','薄脆饼、爆响用品等名词的复数'],['英式俚语改形、比喻 → crackers','疯狂、荒唐；具体旧桥梁有不同解释']],
 'cheese and crackers 奶酪和薄脆饼；Christmas crackers 圣诞拉炮；go crackers 发疯、变得失常；You must be crackers! 你准是疯了吧，可能是玩笑或斥责。',
 'completely crackers；a packet of crackers。','crackers 作形容词不按普通饼干复数理解。用来评价人的想法时可能带冒犯或玩笑，要按说话关系和语气读。',
 ('She put cheese and crackers on the table.','她把奶酪和薄脆饼摆到桌上。'),('You must be crackers to go swimming in that freezing water.','那么冰的水你都去游泳，真是疯了吧。'),sources=['https://www.collinsdictionary.com/dictionary/english/crackers','https://en.wiktionary.org/wiki/crackers#English'])
W('chase','/tʃeɪs/','追赶、追逐；追求；催办；追逐过程',
 '目标在前面跑，你在后面跟上去。追一只球、追机会，甚至追一份迟迟没回的文件，都有不放手地往前跟的感觉。',
 '经古法语 chacier 等追猎词，接通俗拉丁 *captiare，来自 capere 抓取词族。与 catch 是分途借入的同源词，现代 chase 更侧重追，catch 更侧重抓到。',
 [['拉丁 capere 相关材料 → 法语 chacier 等','试图抓取、追猎'],['英语 chase','追赶；追求目标、催办事情']],
 'chase a ball 追球；chase a dream 追求梦想；chase someone away 把人赶走；chase up a reply 催问答复，尤其英式常见。',
 'give chase；a car chase；chase after someone。','chase 不保证抓到，catch 常明确到手或接住。He chased the dog but couldn’t catch it 把追与抓到的差别说得很清楚。',
 ('The dog chased the ball across the garden.','狗追着球跑过花园。'),('I’ll chase up the missing paperwork tomorrow.','我明天会催问那份迟迟未到的文件。'),sources=['https://www.etymonline.com/word/chase','https://en.wiktionary.org/wiki/chase#English'])
W('chaser','英 /ˈtʃeɪsə/；美 /ˈtʃeɪsər/','追逐者；随后喝的饮品；其他追赶相关的人或物',
 '前一个对象走在前面，chaser 跟在后面。可以是追的人，也可以是紧接着前一杯喝的另一种饮品。',
 '现代对应 chase + -er；历史上也可能有法语 chaceor 猎人等借词材料，较早可指追猎用的马。后来的饮品名借了随后跟进的关系。',
 [['chase 与相关法语执行者材料 → chaser','追逐的人、追猎用马等'],['随后跟进的比喻 → 饮品 chaser','在较烈饮品之后喝的另一种饮品']],
 'a storm chaser 追风暴的人；a chaser in a race 比赛中的追赶者；water as a chaser 作为随后饮品的水。-er 取义要看整个搭配。',
 'a leading chaser；a drink with a chaser。','chaser 可以命名人，也可以命名跟在后面的东西；不能看到 -er 就只译追赶的人。',
 ('The documentary follows a group of storm chasers.','纪录片跟拍了一群追逐风暴的人。'),('He had a glass of water as a chaser.','他随后喝了一杯水，作为后续饮品。'),sources=['https://www.etymonline.com/word/chaser','https://en.wiktionary.org/wiki/chaser#English'])
W('abuser','英 /əˈbjuːzə/；美 /əˈbjuːzər/','虐待者；辱骂者；滥用某物的人',
 '把权力、信任用歪，或持续伤害、欺压别人，执行这种行为的人就是 abuser。具体伤害方式要由上下文说明。',
 'abuse 动词去词末 e 加 -er；动词经法语上接拉丁 abuti 用尽、滥用等，含 ab- 与 uti 使用。词干在动词和 abuser 中读 /z/。',
 [['拉丁 abuti → 法语／英语 abuse','用尽、滥用；发展出虐待、辱骂等'],['abuse + -er → abuser','实施滥用、虐待、辱骂的人']],
 'an abuser of power 滥用权力者；an emotional abuser 情感虐待者；a verbal abuser 用言语辱骂别人的人。',
 'identify an abuser；an abuser of trust。','abuser 接动词 abuse /əˈbjuːz/；名词 abuse 常读 /əˈbjuːs/。读音区别帮助看出执行者词到底从哪种词性派生。',
 ('The novel portrays him as an abuser of power.','小说把他描写成一个滥用权力的人。'),('The organization supports people who have left an abuser.','那个组织帮助已经离开虐待者的人。'),sources=['https://www.etymonline.com/word/abuse','https://en.wiktionary.org/wiki/abuser#English'])
W('lurk','英 /lɜːk/；美 /lɝːk/','潜伏、藏着待着；隐约存在；网络中只看不发言',
 '人藏在不显眼的地方，旁边的人没有马上注意到。网络里看讨论却不发言，也借这个不露面的画面。',
 '中古英语 lurken 躲藏等，可能与斯堪的纳维亚相关词相连，具体更早来源不确定。后来可说暗中移动、风险潜在，也用于网络旁观。',
 [['中古英语 lurken；可能接北欧相关材料','躲藏、藏而不露'],['现代 lurk','潜伏；疑虑隐存；在论坛只看不发言']],
 'lurk in the shadows 潜伏在阴影里；danger lurks 危险潜伏；lurk on a forum 在论坛潜水、只看不发言。',
 'lurk nearby；lurk in the background。','hide 直接说躲藏，lurk 常有不露面、还可能出现或行动的感觉。网络潜水用法并不自动带恶意，是不发言的参与方式。',
 ('A cat lurked behind the garden wall.','一只猫躲在花园围墙后面。'),('I usually lurk on the forum rather than post comments.','我通常在论坛只看，不发评论。'),sources=['https://www.etymonline.com/word/lurk','https://en.wiktionary.org/wiki/lurk#English'])
W('lurker','英 /ˈlɜːkə/；美 /ˈlɝːkər/','潜伏者；论坛或群组中只看不发言的人',
 '群里有人每天看消息，却很少开口；网络语境中这样的人常自称 a lurker。',
 'lurk + -er，早期指藏着、不露面的人；互联网发展后借来命名阅读但不发帖的参与者。',
 [['lurk + -er → lurker','保持隐蔽、躲着观察的人'],['现代互联网专门用法','只看讨论而不主动发言的人']],
 'a forum lurker 论坛潜水者；a longtime lurker 长期只看不发帖的人；a lurker in the shadows 藏在阴影里的人。',
 'a quiet lurker；from lurker to contributor。','lurker 在论坛自我介绍里常是中性或带自嘲的词；在悬疑故事里可能让人觉得可疑。具体色彩来自场景。',
 ('I have been a lurker here for years, but this is my first post.','我在这里潜水多年，这是第一次发帖。'),('The survey asked lurkers why they rarely commented.','调查询问只看不发言的用户为什么很少评论。'),sources=['https://www.etymonline.com/word/lurk','https://en.wiktionary.org/wiki/lurker#English'])
W('lurking','英 /ˈlɜːkɪŋ/；美 /ˈlɝːkɪŋ/','潜伏、暗藏；隐约存在的；lurk 的 -ing 形式',
 '表面看着平静，后面还藏着一个疑虑或风险。lurking 常让人感觉事情尚未明摆出来，但并没有消失。',
 'lurk + -ing，继承藏而不露的旧动词义，再用分词描写隐藏的人、危险、疑虑；网络中也可说正在潜水浏览。',
 [['lurk','躲藏、藏而不露'],['lurk + -ing → lurking','潜伏的动作；尚未显露的状态']],
 'a lurking danger 潜在危险；a lurking suspicion 隐约挥之不去的怀疑；lurking behind the door 藏在门后；lurking online 网上只看不发言。',
 'lurking in the background；a lurking doubt。','lurking 修饰 doubt、suspicion 时说疑虑隐存，读成背景中尚在、并未消失的感觉即可。',
 ('There was a lurking doubt in her mind.','她心里一直隐隐有个疑问。'),('We noticed a cat lurking behind the bins.','我们注意到一只猫藏在垃圾桶后面。'),sources=['https://www.etymonline.com/word/lurk','https://en.wiktionary.org/wiki/lurking#English'])
W('crush','/krʌʃ/','压扁、压碎；击垮；拥挤人群；迷恋、心仪的人',
 '手把易拉罐压瘪，是 crush；失败把信心压垮，也用这个压力画面。a crush on someone 则是后来固定的迷恋说法。',
 '经古法语 cruissir、croissir 等咬碎、撞碎词，可能接法兰克语相关材料。压碎、制服等比喻很早已有；拥挤人群和迷恋的名词义后来形成，迷恋这一分支的具体语义桥梁不完全明确。',
 [['古法语相关撞碎、咬碎材料 → crush','使破碎、用重压压扁；压倒'],['现代名词和比喻分支','挤在一起的人群；迷恋或心仪对象']],
 'crush a can 压扁罐子；crush garlic 压碎蒜；crush someone’s hopes 摧毁希望；have a crush on someone 迷恋某人；a crush of people 拥挤的人群。',
 'crush into small pieces；a secret crush。','crush 强调压力、挤压带来的破坏；break 只说明打破。a crush 常是强烈、可能短暂的迷恋，不自动表示已经建立恋爱关系。',
 ('He crushed the empty can with his hand.','他用手把空罐子压瘪了。'),('She had a crush on a colleague.','她曾迷恋一位同事。'),sources=['https://www.etymonline.com/word/crush','https://en.wiktionary.org/wiki/crush#English'])
W('crusher','英 /ˈkrʌʃə/；美 /ˈkrʌʃər/','破碎机、压碎设备；压碎者',
 '把大石头送进去，出来变成小碎块。crusher 把 crush 压碎这个动作变成执行动作的设备名称。',
 'crush + -er，-er 可指动作执行者，现代常命名机器；crush 本身经法语接压碎、撞碎词族。',
 [['crush','通过压力压扁、破碎'],['crush + -er → crusher','执行压碎动作的人或机器']],
 'a stone crusher 碎石机；an ice crusher 碎冰机；a can crusher 压罐器。前面的名词通常说明处理的对象。',
 'feed material into a crusher；a rock crusher。','crusher 以压碎、破碎功能命名；cutter 以切割命名，grinder 常以研磨命名。具体设备可能兼有作用，但读词先抓主要动作。',
 ('The stone crusher broke the rocks into smaller pieces.','碎石机把岩石破成了更小的块。'),('The café bought a small ice crusher.','咖啡馆买了一台小型碎冰机。'),sources=['https://www.etymonline.com/word/crush','https://en.wiktionary.org/wiki/crusher#English'])
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_un',ROOTS,WORDS)
 extend_lessons()
