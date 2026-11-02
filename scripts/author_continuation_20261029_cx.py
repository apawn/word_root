"""Worth and king: value, dignity and authority in common word families."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
def C(a,b,w,m):return [[a+'；'+b,'并列构词部分'],[w,m]]
WO=[['古英语 weorþ → 中古英语 worth','有价值、相称、值得的'],['现代 worth 词族','金钱价值、实际用途；值得某种待遇、投入']]
W('worth','英 /wɜːθ/；美 /wɜːrθ/','值……；值得；价值',
 '拿花费、时间或代价来衡量，所得够不够抵得上；也可以直接说一个东西有什么价值。',
 '由古英语 weorþ 有价值、相称等义延续。不是现代 work 少了一个音；名词和后接金额、动作的常用结构分别记。',WO,
 'worth ten pounds 值十英镑，worth reading 值得读；the worth of an idea 想法的价值，a week’s worth of food 一周所需的食物量。',
 'be worth doing；be worth the effort；for what it’s worth；a day’s worth of。',
 '常说 The book is worth reading，不说 worth to read；worth it 是值得付出这份代价，不必每次指出具体金额。',
 ('The museum is worth visiting.','这家博物馆值得参观。'),('The repair cost more than the chair was worth.','修理费用比椅子本身的价值还高。'))
W('worthy','英 /ˈwɜːði/；美 /ˈwɜːrði/','值得尊重、注意等的；相称的；有价值的',
 '品质、表现或意义够得上某种对待：值得尊重、值得注意，或者配得上某个角色。',
 'worth + -y，与较早相应形式延续有关。th 在常用读音为 /ð/，不要照搬 worth 的 /θ/；它是固定词族读音差异，不是所有加 -y 都如此。',WO+[['worth + -y → worthy','有价值 → 值得某种待遇、相称的']],
 'worthy of attention 值得注意，a worthy cause 有意义、值得支持的事业，a worthy opponent 值得认真对待的对手。',
 'worthy of；a worthy cause；a worthy opponent；a worthy successor。',
 'worth 后常直接接金额、名词、doing；worthy 常用 of：worth reading，worthy of attention。worthy 不直接像金额结构那样说 worthy ten pounds。',
 ('The proposal is worthy of serious consideration.','这份提议值得认真考虑。'),('They raised money for a worthy cause.','他们为一项有意义的事业筹款。'))
W('worthless','英 /ˈwɜːθləs/；美 /ˈwɜːrθləs/','没有价值的；无用的',
 '按当前用途或交易情境看，派不上用场、值不了钱；不等于从宇宙中证明它永远毫无意义。',
 'worth 价值 + -less 没有，古英语已有 weorþlēas 等旧形式。它往往是一种语境中的评价，不能只按价格等同所有价值。',WO+[['worth + -less → worthless','价值 → 无价值、无用的']],
 'a worthless ticket 无效、无用的票，worthless information 毫无用处的信息；形容人时是很重的贬低，不是中性身份。',
 'worthless information；a worthless document；become worthless。',
 'worthless 无价值，priceless 无价、珍贵，虽然都带价格否定联想，常用意义相反。',
 ('Without the missing page, the instructions were almost worthless.','缺了那页，说明书几乎派不上用场。'),('The old ticket was now worthless.','那张旧票现在已经毫无用处。'))
W('worthwhile','英 /ˌwɜːθˈwaɪl/；美 /ˌwɜːrθˈwaɪl/','值得投入时间、精力的',
 '做完后回头看，这段时间和力气花得值；不只是在算能赚多少钱。',
 'worth 值得 + while 一段时间，形成值得花时间的组合，后来扩展到投入、努力是否有意义。',C('worth 值得','while 一段时间','worthwhile','值得投入时间、精力的'),
 'a worthwhile experience 值得的经历，make something worthwhile 让事情值得；It is worthwhile doing 或 to do 两种结构都可见。',
 'a worthwhile project；a worthwhile experience；make it worthwhile。',
 'worthwhile 值得做，worthy 值得尊重、符合某品质；a worthwhile trip 是值得花时间的旅行，不是在赞旅行道德高尚。',
 ('The long walk was tiring but worthwhile.','长距离步行很累，但很值得。'),('It is worthwhile to check the details before booking.','预订前核对细节是值得的。'))
W('worship','英 /ˈwɜːʃɪp/；美 /ˈwɜːrʃɪp/','敬拜；崇敬；过度崇拜',
 '把对象放在很高的位置，以敬意、仪式或近乎仰望的态度对待；既可宗教，也可比喻追星等。',
 '古英语 weorðsċipe，由 weorþ 有价值、尊贵 + -scipe 状态、身份形成，较早为尊荣、敬意，宗教敬拜义也很早已有。现代 th 不再保留原拼写，ship 是后缀，不是船。',
 [['古英语 weorþ + -scipe → weorðsċipe','尊贵、有价值 → 尊荣、敬意'],['中古英语 worshippe → worship','敬意、宗教敬拜；动词崇拜']],
 'a place of worship 宗教礼拜场所，worship a deity 敬拜神祇；worship a celebrity 可批评或夸张说过度崇拜名人。',
 'a place of worship；religious worship；hero worship；worship someone。',
 'worship 崇拜，warship 军舰；worship 中的 -ship 是抽象名词后缀，warship 的 ship 才是船。',
 ('The building is still used as a place of worship.','这座建筑仍用作宗教礼拜场所。'),('The novel shows how fans can come to worship a celebrity.','小说描写粉丝如何逐渐把名人奉若神明。'),sources=['https://en.wiktionary.org/wiki/worship#English','https://www.etymonline.com/word/worship'])
R('B4106','价值、值得；相称、尊荣与崇拜','WORTH：够不够抵得上，或配不配得上','worth 看价值和投入，worthy 看配得上怎样对待，worthwhile 看时间、精力花得值；worship 有尊荣的历史背景。',
 'worth 接古英语 weorþ。worship 旧构词里的 -scipe 是 -ship 后缀，不是船；现代不能把它写成 worthship，也别与 warship 混淆。',
 'worth → worthy、worthless；worth + while → worthwhile；古 worth 词族 + -ship → worship 的历史形式。',
 [['价值及值得','worth · worthy · worthwhile · worthless'],['尊荣与崇敬','worship']],
 'worth doing，worthy of；worthless 无价值，priceless 珍贵；worship 不是 warship。',
 'The visit was worthwhile, and the old place of worship was worth seeing.\n\n这趟参观很值得，古老的宗教礼拜场所值得一看。',
 'worth worthy worthwhile worthless worship')
KI=[['古英语 cyning 等 → 中古英语 king','君王，与 kin 亲族词族有历史关联，具体最初命名关系有争论'],['英语 king','国王；君王棋子、纸牌；比喻领军者、顶尖者']]
W('king','/kɪŋ/','国王；王；某领域的顶尖人物',
 '国家君王是本义；借它在等级顶端的位置，也叫某领域最出名、最强或最有影响的人。',
 '由古英语 cyning 等形式缩短延续。历史与 kin 亲族相关，但最初究竟怎样从亲族关系命名君王有争论，不把现代 king 说成今天 kin + -ing 的动名词。',KI,
 'a king and queen 国王与王后或女王，the king in chess 国际象棋的王；the king of comedy 喜剧之王。也可用于君王棋子、纸牌名称。',
 'a reigning king；a king of comedy；the king in chess；a king of hearts。',
 'king 国王，kingdom 王国，kingship 王位、君王身份；三者分别是人、领地或政治共同体、角色制度。',
 ('The king appears only in the final chapter of the story.','故事中的国王到最后一章才出现。'),('She moved her king to a safer square.','她把国际象棋中的王移到了更安全的格子。'))
W('kingdom','/ˈkɪŋdəm/','王国；领域；生物分类中的界',
 '不是国王本人，而是君主统治的国家、领域；也能用来谈动物界等分类范围。',
 'king + -dom 状态、领域，古英语 cyningdōm 已有对应组合。-dom 不是 dome 圆顶；生物分类义是后来专门用法。',KI+[['古英语 cyningdōm → kingdom','君王权力、领域 → 王国；其他领域义']],
 'a fictional kingdom 虚构王国，the animal kingdom 动物界；生物分类中的界如何划分依分类体系，不由这个英语词固定全部名单。',
 'a fictional kingdom；the animal kingdom；a kingdom in a fairy tale。',
 'kingdom 王国，kingship 君王身份、制度。a kingdom 不是国王的船，也不是只有男性居住的国家。',
 ('The fairy tale is set in a distant kingdom.','童话以一个遥远王国为背景。'),('The lesson introduces diversity in the animal kingdom.','课上介绍了动物界的多样性。'))
W('kingship','/ˈkɪŋʃɪp/','王位；君王身份、权力或制度',
 '讨论的重点是当国王这个角色以及相关权力，而不是一块土地。',
 'king + -ship 抽象身份、状态后缀。这里 ship 与 friendship、worship 的后缀同类，不是载国王的船。',KI+[['king + -ship → kingship','君王 → 君王身份、权力、制度']],
 'the nature of kingship 君权、王位制度的性质，claims to kingship 对王位的主张；历史学文本常见。',
 'the nature of kingship；a claim to kingship；medieval kingship。',
 'kingship 君王角色制度，kingdom 王国，kinship 亲属关系。kingship 里的 g 不能随便漏掉。',
 ('The historian studies ideas of kingship in medieval Europe.','历史学家研究中世纪欧洲的君王观念。'),('The play explores the responsibilities of kingship.','这部戏探讨了身为君王的责任。'))
W('kingly','/ˈkɪŋli/','国王般的；有王者气派的',
 '衣着、气度或作派让人想到国王，有庄严、威仪的感觉。',
 'king + -ly，形容词后缀，历史有中古英语等对应形式。此处不是见 -ly 就必定翻成副词。',KI+[['king + -ly → kingly','国王 → 如国王般的']],
 'a kingly manner 王者般的举止，kingly dignity 君王般威严；不要求对象真有王位。',
 'kingly dignity；a kingly manner；a kingly bearing。',
 'kingly 王者般，kingdom 王国；kingly 更偏气度、性质，royal 还常表示实际属于王室的。',
 ('The actor gave the character a kingly dignity.','演员赋予角色一种王者威严。'),('He entered with a kingly air.','他带着王者般的气派走了进来。'))
W('kingmaker','英 /ˈkɪŋmeɪkə/；美 /ˈkɪŋmeɪkər/','拥立君王者；能左右领袖人选的人或力量',
 '自己不一定坐上最高位置，却能把别人推上去，关键的一票或支持掌握在他手里。',
 'king 君王 + maker 促成者。历史称号里有著名用例，后来扩展到决定政治、组织领导人选的人或势力；不是制作一个国王玩偶的普通工匠。',C('king 君王','maker 促成者','kingmaker','促成谁当君王、领袖的人或力量'),
 'a political kingmaker 左右领袖人选的政治人物、团体；a party can act as kingmaker 某党可能凭支持决定谁掌权。',
 'a political kingmaker；act as kingmaker；a potential kingmaker。',
 'kingmaker 影响谁成为领袖，kingpin 是群体中的关键人物、头目；一个人可能兼具两者，但词的焦点不同。',
 ('The small party became a kingmaker after the close election.','选举结果接近，这个小党成了左右执政人选的关键力量。'),('The novel portrays an adviser who acts as a kingmaker.','小说描绘了一位左右王位人选的顾问。'))
W('kingpin','/ˈkɪŋpɪn/','关键人物；头目；机械主销等',
 '一个结构靠它稳住、一群人由它带动；人物义把关键、居中的作用借了过来。',
 'king 主要的、居首的 + pin 销、柱，历史有球戏主要柱和机械主销等用法。人物引申与这些中心部件的画面相关，具体分支先后不强编成唯一来源。',C('king 主要、居首的','pin 销、柱','kingpin','关键柱、主销 → 群体中的关键人物'),
 'a criminal kingpin 犯罪组织头目，an industry kingpin 行业重要人物；mechanical kingpin 则是机械部件名称。',
 'an industry kingpin；a criminal kingpin；a central kingpin。',
 'kingpin 常是实际掌握关键力量者，kingmaker 强调能决定谁上位；kingpin 本身不必有君主头衔。',
 ('The documentary examines the rise of an industry kingpin.','纪录片考察了一位行业大人物的崛起。'),('The mechanic inspected the vehicle’s kingpin.','机械师检查了车辆的主销。'),sources=['https://en.wiktionary.org/wiki/kingpin#English','https://www.etymonline.com/word/kingpin'])
W('kingfisher','英 /ˈkɪŋfɪʃə/；美 /ˈkɪŋfɪʃər/','翠鸟',
 '这是固定鸟名，fisher 很容易联想到捕鱼；king 为什么加进去，历史没有足够清楚的唯一解释。',
 '较早为 king’s fisher，后成 kingfisher。可认 king + fisher 捕鱼者，但不能编成捕鱼最强所以受封国王的确定词源；也不是所有翠鸟种类都只吃鱼。',
 [['中古英语 king’s fisher 一类形式','君王相关部分 + 捕鱼者；命名原因不明'],['kingfisher','固定鸟类名称翠鸟']],
 'a kingfisher by the river 河边的翠鸟；不同具体种类有自己的种名，中文常用翠鸟概括。',
 'a kingfisher；a kingfisher by the river；spot a kingfisher。',
 'kingfisher 翠鸟，fisherman 渔夫；不能因后半相似就把鸟名当成皇家渔夫这一职业。',
 ('A kingfisher perched above the stream.','一只翠鸟栖在溪流上方。'),('We saw a flash of colour as the kingfisher flew past.','翠鸟飞过时，我们看到一抹鲜亮颜色。'),sources=['https://en.wiktionary.org/wiki/kingfisher#English','https://www.etymonline.com/word/kingfisher'])
R('B2588','国王、王国；君王角色与关键人物','KING：居首的人，和相关角色、领域分开','king 是人，kingdom 是王国，kingship 是君王身份、权力制度，kingly 是气派；关键人物和鸟名另按固定用法学。',
 'king 延续古英语 cyning 等形式，与 kin 亲族词族有关，但最初意义联系有争论。kingfisher 命名原因也保留不明，不拿好记故事替代证据。',
 'king → kingdom、kingship、kingly；kingmaker 促成人上位，kingpin 关键人物、部件；kingfisher 固定鸟名。',
 [['君王、领域与角色','king · kingdom · kingship · kingly'],['影响人选及关键人物','kingmaker · kingpin'],['鸟类名称','kingfisher']],
 'kingship 君王角色，kinship 亲属关系；kingmaker 促成人上位，kingpin 核心人物；kingfisher 不是皇家渔夫。',
 'The kingmaker helped choose a new king for the kingdom.\n\n左右王位人选的人，帮助这个王国选出了新国王。',
 'king kingdom kingship kingly kingmaker kingpin kingfisher')
if __name__=='__main__':save('continuation_20261029_cx',ROOTS,WORDS)
