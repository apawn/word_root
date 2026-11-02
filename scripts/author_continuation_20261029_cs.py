"""Boy and son: age, kinship and familiar compound labels."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
def C(a,b,w,m):return [[a+'；'+b,'并列构词部分'],[w,m]]
BO=[['中古英语 boie、boye','年轻男仆、男孩等历史用法，更远来源有分歧'],['英语 boy','男孩；熟人、同伴等特定语境中的男性称呼']]
W('boy','/bɔɪ/','男孩；年轻男性；特定语境的男性同伴称呼',
 '通常是年纪小的男性；the boys 在熟人之间也可能说几个成年男性朋友，年龄靠场景判断。',
 '接中古英语 boie、boye，更远来源有多种解释，不把未证实的古英语或法语形式写成唯一确定起点。现代男孩义之外保留亲昵、角色称呼等用法。',BO,
 'a little boy 小男孩，a schoolboy 男学生；a boys’ night out 男性朋友一起外出。Oh boy! 是惊讶、兴奋或头疼的感叹，不是在喊一个男孩。对成年陌生人直接喊 boy 可能显得轻慢。',
 'a little boy；a teenage boy；the boys；Oh boy!。',
 'boy 常按年龄，son 按亲子关系；a fifty-year-old son 已五十岁，通常不是 a boy 的字面年龄。',
 ('A boy was reading under the tree.','一个男孩在树下看书。'),('Oh boy, we have a lot of work to do.','哎呀，我们还有好多工作要做。'),sources=['https://en.wiktionary.org/wiki/boy#English','https://www.etymonline.com/word/boy'])
W('boyhood','/ˈbɔɪhʊd/','男孩时期；童年、少年时代',
 '不是某一个男孩，而是一个男性回头看的那段小时候的生活。',
 'boy + -hood 表阶段、状态，形成男孩时期名词。-hood 不表示许多男孩组成一队。',BO+[['boy + -hood → boyhood','男孩 → 作为男孩的那段时期']],
 'a boyhood friend 少年时期的朋友，a boyhood dream 童年梦想；现在讲述者和朋友可能都已成年。',
 'a boyhood dream；a boyhood friend；boyhood memories。',
 'boyhood 特指男孩时期，childhood 范围更宽；boyish 形容像男孩的样子，不是那段时间。',
 ('He returned to the town where he had spent his boyhood.','他回到了度过童年的小镇。'),('Becoming a pilot had been his boyhood dream.','当飞行员是他儿时的梦想。'))
W('boyish','/ˈbɔɪɪʃ/','男孩般的；带少年气的',
 '已经长大，笑容、外表或兴奋劲却仍让人想到少年。',
 'boy + -ish 带……特点，形成形容词。这里强调男孩般特征，不自动是 childish 的幼稚批评。',BO+[['boy + -ish → boyish','男孩 → 带少年外表、神态的']],
 'a boyish smile 少年般的笑容，boyish enthusiasm 少年般的热情；经常形容成年人仍有少年气。',
 'a boyish smile；boyish charm；boyish enthusiasm。',
 'boyish 常说外表、神态的少年气；childish 常批评不成熟。两者都与孩子有关，却不带相同评价。',
 ('He still had a boyish smile.','他仍带着少年般的笑容。'),('She laughed at his boyish enthusiasm for the new gadget.','看他对新玩意儿那股少年般的兴奋，她笑了。'))
W('cowboy','/ˈkaʊbɔɪ/','牛仔；牧牛工；不靠谱的从业者〔英式贬义〕',
 '最初围绕放牧、赶牛的人，后来成为西部骑马形象；英式口语骂某人是 cowboy，还可能是说他做事不专业。',
 'cow 牛 + boy 男孩、年轻工人，固定为牧牛工作者称呼；现代可以是成年人。非正规、草率从业者义是后来引申，不等于所有真实牛仔都不专业。',C('cow 牛','boy 男孩、年轻工人旧用法','cowboy','牧牛工、西部牛仔 → 特定口语里的不专业者'),
 'a cowboy hat 牛仔帽，a cowboy film 西部牛仔电影；a cowboy builder 英式可贬称不靠谱施工者。',
 'a cowboy hat；a cowboy film；cowboy builders。',
 'cowboy 不是 cow 的儿子；worker 职业称谓里带 boy 不保证仍是未成年人。牛仔裤常说 jeans，不是每次都 cowboy trousers。',
 ('The film follows a cowboy travelling across the desert.','电影讲一位牛仔穿越沙漠的故事。'),('The report warned about cowboy builders offering suspiciously low prices.','报道提醒人们提防报价低得可疑、不靠谱的施工者。'))
W('fanboy','/ˈfænbɔɪ/','狂热男粉丝；过分追捧的人〔口语〕',
 '喜欢一个作品、品牌或人物，兴奋到处处维护、很难客观看待，就可能被叫 fanboy。',
 'fan 粉丝 + boy 男性，形成口语称呼；boy 不必字面指未成年。fan 这里是爱好者，不是风扇。',C('fan 粉丝','boy 男性称呼','fanboy','热衷追捧的男性粉丝、拥护者'),
 'a comic-book fanboy 漫画狂热粉丝，a brand fanboy 品牌死忠；可自嘲或贬义，也能作动词说激动追捧。',
 'a brand fanboy；a film fanboy；fanboy over something。',
 'fan 普通粉丝范围宽，fanboy 常带更狂热或失去客观的评价；实际语气要看说话者。',
 ('He jokingly called himself a fanboy of the series.','他开玩笑地称自己是这个系列的死忠粉丝。'),('The reviewer tried not to sound like a fanboy.','评论者努力避免显得像个只会追捧的狂热粉丝。'))
W('tomboy','英 /ˈtɒmbɔɪ/；美 /ˈtɑːmbɔɪ/','行为、打扮被认为像男孩的女孩',
 '传统上把某些运动、衣着或活泼方式归给男孩，于是给喜欢这些的女孩起了这个称呼。它反映的是社会分类。',
 'Tom 常见男性名的泛称 + boy。早期曾用于粗野、活泼人物等，后来固定到被视为像男孩的女孩；不是女孩的名字必须叫 Tom。',C('Tom 常见男性名的泛称','boy 男孩','tomboy','历史人物标签 → 被认为像男孩的女孩'),
 'a self-described tomboy 自称假小子的女孩；有时亲切、有时带刻板印象，不能据衣着或爱好推断性别认同、性取向。',
 'a tomboy as a child；a self-described tomboy；a tomboy character。',
 'tomboy 按传统性别印象描述风格，不是说一个人实际上是男孩；也不说明所有男孩都喜欢同一类活动。',
 ('She described herself as a tomboy who loved climbing trees.','她说自己小时候是个爱爬树的假小子。'),('The novel questions why the girl is labelled a tomboy.','小说质疑为何这个女孩被贴上假小子的标签。'))
W('paperboy','英 /ˈpeɪpəbɔɪ/；美 /ˈpeɪpərbɔɪ/','送报男孩；报童',
 '一大早把报纸送到订户门口的男孩，抓的是工作内容，不是纸做的小人。',
 'paper 报纸的缩略用法 + boy 男孩，形成送报角色称呼。旧时也可能关联卖报，具体看叙事。',C('paper 报纸','boy 男孩','paperboy','送报、卖报的男孩称谓'),
 'work as a paperboy 做送报童，a paperboy’s round 报童的送报路线；现代配送人员不都由男孩担任。',
 'work as a paperboy；the morning paperboy；a paperboy’s round。',
 'paperboy 强调送、卖报角色，newspaper 报纸；newsboy 也是旧报童称呼，二者常有交叠。',
 ('He worked as a paperboy during his school years.','他上学时做过送报童。'),('The paperboy left the newspaper by the front door.','送报童把报纸放在前门旁。'))
W('busboy','/ˈbʌsbɔɪ/','餐馆清台、协助服务的工作人员〔美〕',
 '客人走后收盘子、擦桌子，为下一桌准备；不是公交车上的男孩。',
 'bus 在餐馆用语中有清理桌面、收餐具义 + boy 人员称谓；这段餐饮用法与较早 omnibus 等服务称谓有关，具体远因解释不必硬编。现代常见更中性的 busser。',C('bus 餐馆清台用法','boy 人员称谓','busboy','协助收餐具、清台的餐馆工作人员'),
 'work as a busboy 在餐馆清台，a restaurant busboy 餐馆清台人员；不要求是未成年，工作范围按餐馆安排。',
 'work as a busboy；a restaurant busboy；the busboy cleared the table。',
 'busboy 不是 bus driver 公交司机；waiter 通常负责点单、上菜等服务，实际岗位可能交叠。',
 ('He worked as a busboy at a busy restaurant.','他在一家繁忙餐馆做清台工作。'),('The busboy cleared the plates after we finished eating.','我们吃完后，清台人员收走了盘子。'))
W('wonderboy','英 /ˈwʌndəbɔɪ/；美 /ˈwʌndərbɔɪ/','少年天才；年轻有为的红人',
 '年纪轻轻就表现惊人，让周围人觉得这孩子太神了；也可带对年轻红人过度追捧的调侃。',
 'wonder 惊奇、令人惊叹的人物特点 + boy 男孩、年轻男性，形成赞叹性人物称呼。也常分写 wonder boy。',C('wonder 令人惊叹','boy 男孩、年轻男性','wonderboy','表现惊人的少年、年轻红人'),
 'a sporting wonderboy 体育少年天才，the company’s wonderboy 公司里受追捧的年轻能人；可能真心夸，也可能反讽。',
 'a sporting wonderboy；a political wonderboy；the team’s wonderboy。',
 'wonderboy 强调年轻、突出并受关注，boyish 强调少年气；成年人一脸 boyish 不等于有天才表现。',
 ('The young pianist was hailed as a wonderboy.','年轻钢琴家被誉为少年天才。'),('The novel follows the rise and fall of a business wonderboy.','小说追踪一位商界年轻红人的兴衰。'))
W('loverboy','英 /ˈlʌvəbɔɪ/；美 /ˈlʌvərbɔɪ/','情郎；对恋爱中男性的戏谑称呼',
 '看到某个男人满心恋爱，就拿情郎这个称呼打趣他；语气比普通 boyfriend 更像绰号。',
 'lover 恋人 + boy 男性称呼，形成亲昵或调侃的固定组合，也常分写 lover boy。这里 boy 不必按儿童年龄理解。',C('lover 恋人','boy 男性称呼','loverboy','亲昵、戏谑的情郎称呼'),
 'Hey, loverboy! 嘿，大情圣！常作熟人间称呼；是否友善靠语气、关系。词本身不是正式亲属身份。',
 'Hey, loverboy!；call someone loverboy；a loverboy character。',
 'boyfriend 是较中性的男友关系称谓，loverboy 常是绰号、调侃；不能拿它替代所有正式场景的伴侣称谓。',
 ('His friends jokingly called him loverboy after he fell in love.','他恋爱后，朋友们开玩笑地叫他大情圣。'),('“Hey, loverboy,” his sister teased, “your phone is ringing.”','“喂，大情圣，”姐姐打趣道，“你手机响了。”'))
R('B2616','男孩；少年气与按角色命名的男性称呼','BOY：年龄、风格和固定角色分开看','boy 可以说男孩，但 cowboy、busboy 等固定角色未必未成年；boyish 是少年气，boyhood 才是少年时期。',
 'boy 接中古英语，更远来源不确定。后缀区分阶段与风格，复合词还会保留旧式工作人员称谓或社会标签，不能逐个机械翻男孩。',
 'boy → boyhood、boyish；cowboy、paperboy、busboy 按角色；fanboy、tomboy、wonderboy、loverboy 按各自固定标签理解。',
 [['男孩、时期与少年气','boy · boyhood · boyish · schoolboy'],['工作与角色','cowboy · paperboy · newsboy · busboy'],['粉丝、风格和评价','fanboy · tomboy · wonderboy'],['关系、绰号及旧学词','boyfriend · loverboy · playboy · superboy']],
 'boy 不等于 son；cowboy 不是牛的儿子；busboy 不是公交司机；tomboy 不直接说明身份、取向。',
 'The former paperboy recalled his boyhood dream of becoming a cowboy.\n\n这位从前的送报童回忆起儿时想当牛仔的梦想。',
 'boy boyhood boyish schoolboy cowboy paperboy newsboy busboy fanboy tomboy wonderboy boyfriend loverboy playboy superboy')
SO=[['古英语 sunu → 中古英语 sone、sunu 等','儿子'],['现代英语 son','亲子关系中的男性子女；其他固定称呼另看语境']]
W('son','/sʌn/','儿子；男性后代',
 '这个词先回答是谁的孩子，而不是现在几岁；儿子五岁、五十岁，都能说 son。',
 '由古英语 sunu 经中古英语延续，是古老亲属词。与 sun 太阳同音不是同源，也不是把太阳借来指儿子的词源故事。',SO,
 'their son 他们的儿子，an only son 独子；a son of the city 文学、报道里可指本地出身的男性。宗教专名另按文本理解。',
 'an only son；an eldest son；a native son；father and son。',
 'son 按家庭关系，boy 常按年龄；sons 是复数，son’s 是儿子的，别把撇号当复数标记。',
 ('Their son works in another city.','他们的儿子在另一座城市工作。'),('She introduced her two sons to the guests.','她向客人介绍了自己的两个儿子。'))
W('sonny','/ˈsʌni/','小子；对男孩、较年轻男性的称呼',
 '像叫一声小家伙或小子；可以亲近，也可能居高临下，完全看双方关系和语气。',
 'son + -y，双写 n，形成亲昵称呼。作为人名 Sonny 又是专名用法，不要求是说话者的亲生儿子。',SO+[['son + -y → sonny','儿子 → 亲昵或居高临下的男性称呼']],
 'Listen, sonny 听着，小子；较常在对白、较旧口吻里出现。不是正式介绍儿子身份时的必要表达。',
 'Hello, sonny；listen, sonny；a character called Sonny。',
 'sonny 与 sunny 晴朗的同音，来源和意义不同；sonny 作称呼不等于已经确认亲子关系。',
 ('“Hello, sonny,” the old man said with a smile.','老人笑着说：“你好，小家伙。”'),('The line “Listen, sonny” makes the speaker sound condescending.','“听着，小子”这句台词让说话者显得居高临下。'))
W('stepson','/ˈstepsʌn/','继子',
 '伴侣与别人的儿子，因为婚姻与你形成继亲关系。',
 'step- 继亲 + son 儿子，旧英语已有相关亲属称谓。step- 是继亲前缀，不是脚步。',SO[:1]+[['step- + son → stepson','继亲关系 → 继子']],
 'her stepson 她的继子；和 stepchild 相比，stepson 特别说明男性子女。',
 'a stepson；her stepson；a son and a stepson。',
 'stepson 继子，grandson 孙子、外孙，godson 教子；不是同一种亲属关系的三种说法。',
 ('Her stepson helped her move the furniture.','她的继子帮她搬家具。'),('He has a daughter and a stepson.','他有一个女儿和一个继子。'))
W('godson','英 /ˈɡɒdsʌn/；美 /ˈɡɑːdsʌn/','教子',
 '有人在宗教、家庭传统中成为孩子的教父或教母；这名男性孩子相对于他们就是教子。',
 'god 上帝 + son 儿子，古老基督教教亲属关系称谓。是教亲关系，不是对每个人都可字面译成上帝的儿子。',SO[:1]+[['god + son → godson','宗教教亲关系中的男性子女称谓']],
 'her godson 她的教子，a godfather and his godson 教父与教子。具体礼仪、责任随宗教传统与家庭而异。',
 'my godson；a godfather and his godson；become someone’s godson。',
 'godson 教子不同于 adopted son 养子；成为教父、教母不自动等于法律收养或监护。',
 ('She sent her godson a book for his birthday.','她给教子寄了一本生日礼物书。'),('The photograph shows a godfather with his godson.','照片里是一位教父和他的教子。'))
R('B2657','儿子；继子、教子及亲昵称呼','SON：亲子关系，和年龄分开','son 五十岁也还是儿子；stepson、grandson、godson 分别按继亲、代际、宗教关系来认。',
 'son 由古英语 sunu 延续，与 sun 同音但非同一个来源。sonny 是称呼形式，可能亲昵，也可能轻慢，不是正式年龄标签。',
 'son → sonny；step- 继亲 → stepson；grand- 跨一代 → grandson；god- 教亲关系 → godson。',
 [['儿子与亲昵称呼','son · sonny'],['继亲、代际和教亲关系','stepson · grandson · godson']],
 'son 不是 sun；sonny 不是 sunny；stepson 继子、godson 教子都不自动等于 adopted son 养子。',
 'Her adult son chose a birthday present for his godson.\n\n她已经成年的儿子，为自己的教子选了一份生日礼物。',
 'son sonny stepson grandson godson')
for item in WORDS:
    if item['word']=='busboy':item['sources'].append('https://www.etymonline.com/word/busboy')
if __name__=='__main__':save('continuation_20261029_cs',ROOTS,WORDS)
