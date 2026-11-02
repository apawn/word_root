"""Sports, laughter, direction and cash: useful common extensions."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
SP=[['sport〔活动、娱乐、运动〕→ sports','复数及运动类别修饰形式'],['sports 与人物、品格、衣着成分组合','运动参与者、体育风度、运动服装']]
W('sportsman','英 /ˈspɔːtsmən/；美 /ˈspɔːrtsmən/','男运动员；热爱体育活动的人',
 '按参与运动来称呼人，常指男性；传统用法还可包括钓鱼、狩猎等户外活动爱好者。',
 'sports + man，复数 sportsmen。不是每个词中的 s 都另有一层深奥词根，这里接运动类别形式。',SP+[['sports + man → sportsman','参与运动、户外体育活动的男性']],
 'a keen sportsman 热爱体育的人，a professional sportsman 职业男运动员。按地区、语境可有较宽或较窄范围。',
 'a keen sportsman；a professional sportsman；an accomplished sportsman。',
 'sportsman 带男性信息，sportsperson 不指定性别，athlete 常强调训练、竞技者；范围并非每处完全相同。',
 ('He was a keen sportsman throughout his school years.','上学那些年，他一直热爱体育。'),('The prize recognizes an outstanding young sportsman.','奖项表彰一名出色的青年男运动员。'))
W('sportsperson','英 /ˈspɔːtspɜːsn/；美 /ˈspɔːrtspɜːrsn/','运动员；体育活动参与者',
 '保留参与体育这个角色，把 man 换成 person，让称呼不预设性别。',
 'sports + person，复数 sportspeople 或 sportspersons。不是 sportsman 变成了另一个生物类别，而是人物称呼的选择。',SP+[['sports + person → sportsperson','不指定性别的体育参与者、运动员']],
 'a professional sportsperson 职业运动员，young sportspeople 年轻运动员。',
 'a professional sportsperson；young sportspeople；sportsperson of the year。',
 'sportsperson 不特指男性或女性，sportsman 通常男性，sportswoman 女性；具体选词随机构、地区习惯。',
 ('The school invited a professional sportsperson to speak.','学校邀请了一位职业运动员来演讲。'),('Young sportspeople need time for both training and study.','年轻运动员需要兼顾训练和学习。'))
W('sportsmanship','英 /ˈspɔːtsmənʃɪp/；美 /ˈspɔːrtsmənʃɪp/','体育风度；公平竞争、尊重对手的态度',
 '赢了不羞辱对手，输了也尊重规则；看的是怎样参与竞争，而不是只看比分。',
 'sports + -manship，也可对应 sportsman + -ship。人物技艺、品格名词后来突出公平、得体的体育态度，不只表示男性技术。',SP+[['sports + -manship／sportsman + -ship → sportsmanship','体育参与的品格、风度；现代常强调公平竞争']],
 'good sportsmanship 良好体育风度，show sportsmanship 展现公平竞争态度。可用于任何性别的参与者。',
 'good sportsmanship；show sportsmanship；an act of sportsmanship。',
 'sportsmanship 风度、行为，sporting skill 运动技术；球技很强也可能缺体育风度，二者不是同一个评价。',
 ('She shook hands with her opponent in a display of sportsmanship.','她与对手握手，展现了体育风度。'),('The coach valued sportsmanship as much as winning.','教练既重视获胜，也同样重视体育风度。'))
W('sportswear','英 /ˈspɔːtsweə/；美 /ˈspɔːrtswer/','运动服装；运动休闲服装',
 '按运动场景设计，或带运动休闲风的衣服这一类；不一定每件都只在比赛时穿。',
 'sports + wear 衣着用品。服装行业有时范围较宽，包括休闲搭配，不能从词形保证所有专业运动性能。',SP+[['sports + wear → sportswear','运动用途或运动休闲风格的服装类别']],
 'casual sportswear 运动休闲服装，a sportswear brand 运动服饰品牌。通常不可数。',
 'casual sportswear；a sportswear brand；a sportswear collection。',
 'sportswear 衣服，sports equipment 器材；球拍、球网不通常归进衣着这个词。',
 ('The shop specializes in sportswear.','这家店专卖运动服装。'),('She wore comfortable sportswear for the journey.','旅途中，她穿着舒适的运动休闲服。'))
R('B4542','运动类别到人物、体育风度和衣着','SPORTS：运动这一类；后面说明人、风度还是服装','已有 sport、sports 先读，sportsman/sportsperson 连着比较，sportsmanship 品格，sportswear 衣着。sportsbook 暂略较专门博彩义。',
 '复数形式常作类别修饰，别把每个 s 当独立新词根。人物称呼里的男性成分不限制 sportsmanship 只能用于男性。',
 'sport + -s；sports + man/person/wear；sports + -manship。',
 [['基本活动与人物','sport · sports · sportsman · sportsperson'],['品格和服装','sportsmanship · sportswear']],
 'sportsman 通常男性、sportsperson 不指定；sportsmanship 风度不只是技术；sportswear 服装不同于全部运动器材。',
 'The sportsperson showed good sportsmanship after losing the match.\n\n这位运动员输掉比赛后仍展现出良好体育风度。',
 'sport sports sportsman sportsperson sportsmanship sportswear')
LA=[['古英语 hliehhan、hlæhhan 等 → 中古英语 laughen → laugh','笑'],['古英语 hleahtor → 中古英语 laughter → laughter','笑、笑声的旧名词；不由现代 laugh + -er 人物后缀造出']]
W('laugh','英 /lɑːf/；美 /læf/','笑；笑声、好笑的人或事〔名词〕',
 '嘴角、气息和声音一起动起来；可以是高兴，也可能是嘲笑、紧张，要看语气和对象。',
 '继承古英语笑动词，现代 gh 读 /f/，不要把 laugh 的拼写当 cough 等词的统一发音公式。名词 a laugh 也可一次笑或好玩事。',LA[:1]+[['现代 laugh','笑动作；名词一次笑、好玩的人或事']],
 'laugh at a joke 听笑话笑，laugh at someone 嘲笑某人，have a laugh 乐一乐，laugh something off 一笑置之。',
 'laugh at；have a laugh；laugh out loud；laugh it off。',
 'laugh 常带笑声，smile 微笑不必出声；laugh at 既能对笑话发笑，也可嘲笑人，宾语和语气决定。',
 ('We laughed at the silly joke.','我们听了那个傻笑话都笑了。'),('She tried to laugh off the mistake.','她想对那个错误一笑置之。'))
W('laughing','英 /ˈlɑːfɪŋ/；美 /ˈlæfɪŋ/','正在笑的；笑这件事；laugh 的 -ing 形式',
 '描述笑的进行或把笑作为活动；laughing matter 则是可以当玩笑看的事。',
 'laugh + -ing，中古英语已有 laughynge 等形式。不是所有 -ing 结构都只有正在一种译法。',LA+[['laugh + -ing → laughing','笑的活动、分词；相关固定搭配']],
 'burst out laughing 突然笑起来，can’t stop laughing 笑个不停，no laughing matter 不是闹着玩的事。',
 'burst out laughing；can’t stop laughing；no laughing matter。',
 'laughing 正在笑或笑的活动，laughable 通常可笑得站不住脚；a laughing child 与 a laughable excuse 不能互换。',
 ('The children burst out laughing.','孩子们突然笑起来。'),('Losing the only copy is no laughing matter.','弄丢唯一一份副本可不是闹着玩的。'))
W('laughter','英 /ˈlɑːftə/；美 /ˈlæftər/','笑声；笑的活动',
 '把一阵阵笑当成整体声音、气氛来听；通常不像 a laugh 那样数一次。',
 '继承古英语 hleahtor 等旧名词，与 laugh 同族，但不是现代 laugh + 人物后缀 -er。laughter 不叫笑的人。',LA,
 'burst into laughter 突然大笑，a burst of laughter 一阵笑声，fill with laughter 充满笑声。',
 'burst into laughter；a burst of laughter；fill with laughter。',
 'laughter 通常不可数，a laugh 可数一次笑；laugher 才可按人名后缀说发笑者，但日常先掌握 laughter。',
 ('The room filled with laughter.','房间里充满了笑声。'),('A burst of laughter came from the next room.','隔壁传来一阵笑声。'))
W('laughable','英 /ˈlɑːfəbl/；美 /ˈlæfəbl/','可笑、荒唐得让人发笑的',
 '往往不是夸幽默，而是说借口、建议糟得没法认真当真。',
 'laugh + -able，可引人发笑；现代常带荒唐、滑稽、不值认真对待的批评语气。',LA+[['laugh + -able → laughable','可引人发笑；常转为荒唐可笑的评价']],
 'a laughable excuse 可笑借口，a laughable suggestion 荒唐建议。',
 'a laughable excuse；a laughable suggestion；seem laughable。',
 'funny 可以夸好笑，laughable 更常贬荒唐；称人的主张 laughable 比单说 I disagree 强得多。',
 ('The excuse was so weak that it was laughable.','借口太站不住脚，简直可笑。'),('What once seemed laughable later became possible.','曾经看似荒唐的事情，后来成为了可能。'))
R('B2586','笑动作与笑声；好玩和荒唐评价分开','LAUGH：笑出来；LAUGHTER：整体笑声','laugh → laughing，再 laughter 旧名词，laughable 现代常作贬义评价；冷门 laugher 暂略。',
 '笑不只高兴，也可能紧张或嘲讽；意思要连动作对象、语气一起读。laughter 的结尾不硬拆人物后缀。',
 'laugh + -ing/-able；旧 hleahtor → laughter；gh 在 laugh 中读 /f/。',
 [['动作、活动和声音','laugh · laughing · laughter'],['可笑评价','laughable']],
 'laugh 有笑声、smile 可无声；laughter 不可数不同于 a laugh；laughable 常贬荒唐，不是夸幽默。',
 'The laughable excuse made everyone burst out laughing.\n\n那个荒唐借口让大家突然笑了起来。',
 'laugh laughing laughter laughable')
DR=[['拉丁 dīrēctiō → 法语、中古英语 → direction','引导、方向、指导'],['direction + -less → directionless','没有方向、缺少目标']]
W('directionless','英 /dɪˈrekʃənləs/；美 /dɪˈrekʃənləs/〔词首亦可 /daɪ-/〕','没有方向的；缺乏目标、指导的',
 '走是一直走，却不知道往哪儿、为什么走；也可说项目、人生阶段缺少清楚目标。',
 'direction + -less，否定方向、目标或指引。不是说一个物体在空间完全不存在任何朝向。',DR,
 'feel directionless 感觉没目标，a directionless project 缺乏清晰方向的项目。',
 'feel directionless；a directionless project；seem directionless。',
 'directionless 没方向、目标，lost 可迷路、失去方向感；暂时不知道路不必人生整体 directionless。',
 ('After graduation, he felt directionless for a while.','毕业后，他有一阵子觉得没有目标。'),('The project became directionless without clear leadership.','没有清楚的带领，项目逐渐失去了方向。'))
R('B3559','引导与方向；没有目标、指引的扩展','DIRECTION：往哪儿去、怎样做；-less 缺少方向','已有 direction、directional 先读，directionless 否定；misdirection、redirection 继续比较错误引导与重新导向。',
 '方向也可抽象为目标、指导；无方向词不用几何学硬解。',
 'direction + -al/-less；mis-/re- + direction。',
 [['方向、性质和缺少方向','direction · directional · directionless'],['引导的变化','misdirection · redirection']],
 'directionless 没方向不同于 redirection 换方向；misdirection 误导；具体 direction 还可指导说明。',
 'A clear direction helped the directionless team move forward.\n\n清楚的方向帮助迷失目标的团队继续前进。',
 'direction directional directionless misdirection redirection')
CS=[['法语 caisse 等 → 英语 cash','钱箱 → 现金'],['cash + -less → cashless','不用实物现金的付款、交易环境']]
W('cashless','/ˈkæʃləs/','无现金支付的；不使用实物现金的',
 '不用掏纸币、硬币，用卡或其他电子方式完成付款；交易仍然有钱的转移。',
 'cash + -less，缺少的是实物现金这个支付形式。现代常用于支付方式、店铺、社会环境，而非一律说穷得没钱。',CS,
 'cashless payment 无现金支付，a cashless café 不收实物现金的咖啡馆，a cashless society 广泛采用非现金支付的社会。',
 'cashless payment；a cashless café；a cashless society。',
 'cashless 不用纸币硬币，free 免费；刷卡付费依然花钱。cashless 也不自动只允许一种手机应用。',
 ('The café accepts only cashless payments.','这家咖啡馆只接受非现金付款。'),('The festival introduced a cashless payment system.','节日活动引入了无现金支付系统。'))
R('B3300','现金与不用实物现金的付款方式','CASH：现金；CASHLESS：付款不用纸币硬币','已有 cash 先读，再 cashless，把现金形式与是否付费分清。',
 '钱箱到现金的历史已有基础词精讲。-less 此处多否定实物现金的使用，不否定交易金额。',
 'cash + -less。',
 [['现金和支付形式','cash · cashless']],
 'cashless 无现金形式、free 免费；电子付款仍有资金转移。',
 'The cashless café does not accept cash.\n\n这家采用无现金支付的咖啡馆不收实物现金。',
 'cash cashless')
if __name__=='__main__':save('continuation_20261030_bh',ROOTS,WORDS)
