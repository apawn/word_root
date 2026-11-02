"""High-frequency y/ies plurals in ordinary reading and conversation."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'B2944':dict(words=['body','bodies'],label='body → bodies：身体、整体与机构',note='bodies 是规则 y 改 ies 的名词复数；新闻中的机构是有组织整体的 body 义。'),
 'B2713':dict(words=['city','cities'],label='city → cities：城市的复数',note='city 经法语接拉丁公民、城市共同体词族；复数只按现代拼写 y 改 ies。'),
 'B3155':dict(words=['party','parties'],label='party → parties：聚会、政党与参与各方',note='party 从一部分、一方走向团体等分支；parties 也可能是参加聚会的动词形式。'),
 'B2482':dict(words=['country','countries'],label='country → countries：国家、地区的复数',note='复数常说多个国家、地区；乡村和乡村音乐的 country 义有不同可数性、修饰结构。'),
 'C0404':dict(words=['family','families'],label='family → families：家庭、家族与类别',note='family 接拉丁 familia 家内人员词族；现代也按共同特点说语言家族、物种科等集合。'),
 'C0954':dict(words=['company','companies'],label='company → companies：结伴、团体到公司',note='company 经法语接共同吃面包的同伴词族；companies 常指公司、团体，陪伴义通常不这样数。'),
 'B3772':dict(words=['story','stories'],label='story → stories：叙事与楼层分别理解',note='故事、报道的 stories 与美式楼层 stories 同形；楼层的英式 storeys 拼写另列于用法，语义来源桥梁有不确定处。'),
 'B2544':dict(words=['baby','babies'],label='baby → babies：婴儿的复数与动词',note='名词 baby 和把人过分当婴儿照顾的动词都能形成 babies，靠句法区分。'),
 'B3477':dict(words=['lady','ladies'],label='lady → ladies：女士与称呼',note='lady 延续古英语女主人名称，复数 ladies；更早与面包、和面者的传统解释有过质疑，不夸成唯一命名故事。'),
}
W('bodies','英 /ˈbɒdiz/；美 /ˈbɑːdiz/','身体、躯体；有组织的机构、团体；物体、主体等〔body 的复数〕',
 '一个完整的身体是 body；多个有组织、能一起行动的机构，也像一个个整体，可以叫 bodies。读新闻时别只想到人的身体。',
 'body 的辅音字母加 y 改成 ies；body 接古英语 bodig 等身体名。由完整有组织的整体，扩展到机构、物体等；复数沿用这些不同义项。',
 [['古英语 bodig → body','身体；完整的整体'],['body 的 y → ies → bodies','多个身体、物体或机构']],
 'human bodies 人体〔复数〕；public bodies 公共机构；regulatory bodies 监管机构；celestial bodies 天体；bodies of water 水体。',
 'different bodies；the main bodies of the texts。','a body 可以按语境指尸体，也可以是活人的身体、机构或物体，不能只凭复数 bodies 先定成尸体。机构义的复数通常搭配复数动词。',
 ('The report was reviewed by several independent bodies.','报告经几个独立机构审阅。'),('The lesson explains how our bodies use energy.','这节课解释我们的身体怎样利用能量。'),sources=['https://en.wiktionary.org/wiki/bodies#English','https://en.wiktionary.org/wiki/body#English'])
W('cities','/ˈsɪtiz/','城市〔city 的复数〕',
 '把几座城市放到地图上比较，或旅行时先后去了几座城，就用 cities。这个词数的是一座座城市。',
 'city 的 y 改为 ies，末尾读 /iz/，是 /i/ 接复数 /z/。city 经法语 cite、拉丁 civitas 城市共同体、公民身份等材料进入英语。',
 [['拉丁 civitas → 法语 cite → city','公民共同体、城市'],['city 的 y → ies → cities','多个城市']],
 'major cities 主要城市；coastal cities 沿海城市；in several cities 在几座城市；between two cities 两城之间。',
 'large cities；cities around the world。','country 是国家、地区，city 是城市，county 常是县等行政单位。含义层级和具体制度不同，不能因为拼写相近而互换。',
 ('The train connects the two largest cities in the region.','这班列车连接该地区最大的两座城市。'),('We visited three cities during the trip.','旅途中，我们游览了三座城市。'),sources=['https://en.wiktionary.org/wiki/cities#English','https://en.wiktionary.org/wiki/city#English'])
W('parties','英 /ˈpɑːtiz/；美 /ˈpɑːrtiz/','聚会；政党；参与各方、当事方〔复数〕；参加聚会、玩乐〔party 的第三人称单数〕',
 '生日场景里是几场聚会；讨论协议时是参加协商的各方；选举报道里又可能是政党。共同点是分出来、站在一起的一群人或一方。',
 'party 的 y 改成 ies，可作名词复数，也可作动词第三人称。party 经古法语 partie 一部分、一方接拉丁 part 词族，之后分化出团体、聚会等常见义。',
 [['法语 partie → party','一部分、一方 → 团体、聚会等'],['party 的 y → ies → parties','多个团体、聚会、参与方；或单数主语的玩乐动作']],
 'birthday parties 生日聚会；political parties 政党；both parties 双方；all parties involved 所有参与方；She parties on weekends 她周末参加聚会玩乐。',
 'organize parties；talks between the parties。','party 不一定是派对。both parties agreed 是双方同意，常见于协商语境；具体是两个人、两个团体还是其他主体，要看上下文。',
 ('Both parties agreed to meet again the following week.','双方同意下一周再见面。'),('The children went to two birthday parties that month.','那个月，孩子们参加了两场生日聚会。'),sources=['https://en.wiktionary.org/wiki/parties#English','https://en.wiktionary.org/wiki/party#English'])
W('countries','/ˈkʌntriz/','国家、国土、地区〔country 的复数〕',
 '一张地图上标出多个国家，或说活动有几个国家参加，就用 countries。它把一个个国家、地区作为可数单位来谈。',
 'country 的 y 改成 ies。country 经古法语 contree，通常追到表示面对的土地的晚期拉丁重建形式，与 contra 面对、相对有关；现代复数不需要重新拆出那些旧成分。',
 [['法语 contree → country','土地、地区 → 国家、国土等'],['country 的 y → ies → countries','多个国家、地区']],
 'different countries 不同国家；neighbouring countries 邻国；countries around the world 世界各国；travel between countries 跨国旅行。',
 'several countries；people from many countries。','the country 还常说乡村，country music 是乡村音乐，不能把 countries 的多个国家义随意搬到这些固定结构里。',
 ('Students from several countries joined the workshop.','来自几个国家的学生参加了工作坊。'),('The exhibition includes photographs from different countries.','展览收录了来自不同国家的照片。'),sources=['https://en.wiktionary.org/wiki/countries#English','https://en.wiktionary.org/wiki/country#English'])
W('families','/ˈfæməliz/〔常有缩读〕','家庭、家族；同类组、语系等〔family 的复数〕',
 '一家人是一组，几家人就是 families。语言或事物有相近来源、共同特点，也可以按家族分成 families。',
 'family 的 y 改成 ies。family 接拉丁 familia 家内人员、家庭词，现代又以亲属、共同来源的画面扩展到相关类别。',
 [['拉丁 familia → family','家内人员、家庭 → 亲属与共同特点的集合'],['family 的 y → ies → families','多个家庭、家族或相关类别']],
 'young families 有年幼孩子的家庭；families with children 有孩子的家庭；language families 语系；families of related plants 相关植物的类别、科〔依分类语境〕。',
 'help local families；different families of languages。','three families 是三个家庭，不是三位家人；家人个体可说 family members。科学分类里的 family 有专门层级，按领域译为科等。',
 ('Several families shared the picnic area.','几个家庭共用了野餐区。'),('The chart groups the languages into families.','图表按语系对这些语言进行归组。'),sources=['https://en.wiktionary.org/wiki/families#English','https://en.wiktionary.org/wiki/family#English'])
W('companies','英 /ˈkʌmpəniz/；美 /ˈkʌmpəniz/','公司；剧团、舞团、连队等〔company 的复数〕',
 '一群人为共同目标组成一个团体，可以发展为商业公司、演出团体或军队单位。companies 把这些一组组有组织的团体数出来。',
 'company 的 y 改成 ies。经古法语 compagnie 接共同结伴词族，最终与 com- 一起、panis 面包相连：共同吃饭的伙伴发展为团体，商业公司是其中一支。',
 [['共同吃面包的同伴词族 → 法语 compagnie → company','同伴、共同体 → 有组织团体'],['company 的 y → ies → companies','多个公司、演出团体或相应单位']],
 'small companies 小公司；technology companies 科技公司；dance companies 舞团；the companies in the group 集团里的公司。',
 'work with several companies；local companies。','company 的陪伴义通常不可数：I enjoy your company。companies 多个公司、团体，不能直接拿来表示有许多陪伴。',
 ('Several local companies helped organize the event.','几家当地公司协助组织了活动。'),('The festival invited dance companies from different regions.','艺术节邀请了来自不同地区的舞团。'),sources=['https://www.etymonline.com/word/company','https://en.wiktionary.org/wiki/companies#English'])
W('stories','英 /ˈstɔːriz/；美 /ˈstɔːriz/〔r 发音〕','故事、报道、说法；楼层〔美式〕；story 的复数',
 '你讲了几个故事，是 stories；新闻里的几篇报道也可这样说。美国英语里楼有几层，还可以用 stories，靠上下文区分。',
 'story 的 y 改成 ies。叙事义接法语 estorie、拉丁 historia；楼层义也有较早的相应材料，常以建筑叙事图像等解释，但中间命名过程不完全确定。',
 [['拉丁、法语叙事词 → story','历史叙述 → 故事、报道等'],['story → stories；另有楼层的同形用法','多个故事、报道；美式多个楼层']],
 'short stories 短篇小说；news stories 新闻报道；tell stories 讲故事，也可能说编造说法；three stories high 三层高〔美式〕。',
 'bedtime stories；different versions of the stories。','英式楼层通常写 storey／storeys，美式常写 story／stories。叙事、报道的 stories 可真可虚，不能把所有 story 都当虚构童话。',
 ('She reads the children stories before bed.','她睡前给孩子们读故事。'),('The newspaper published several stories about the festival.','报纸刊登了几篇有关艺术节的报道。'),('The old house is three stories high.','那栋老房子有三层高。'),sources=['https://www.etymonline.com/word/story','https://en.wiktionary.org/wiki/stories#English'])
W('babies','/ˈbeɪbiz/','婴儿、幼小动物等〔复数〕；过分呵护〔baby 的第三人称单数〕',
 '几个小婴儿叫 babies。若说成年人总把别人当小婴儿照顾，baby 还可作动词，单数主语后也写 babies。',
 'baby 的 y 改成 ies，既用于名词复数，也用于动词第三人称。baby 来自中古英语 babe 的亲昵、指小形式；动词由婴儿名转用。',
 [['babe → baby','较早婴儿名 → 亲昵、小称形式'],['baby → babies','多个婴儿；也可说某人把对象当婴儿照顾']],
 'newborn babies 新生婴儿；sleeping babies 睡着的婴儿；animal babies 幼小动物；babies him 过分照顾他、把他当小孩。',
 'two babies；babies in prams。','a baby’s toy 是一个婴儿的玩具；babies’ toys 是多个婴儿的玩具。把 baby 用作爱称、形容稚嫩时，还要结合具体语气。',
 ('The two babies fell asleep at the same time.','两个婴儿同时睡着了。'),('She says her family still babies her even though she is grown up.','她说，尽管自己已经长大，家人仍把她当小孩照顾。'),sources=['https://en.wiktionary.org/wiki/babies#English','https://en.wiktionary.org/wiki/baby#English'])
W('ladies','/ˈleɪdiz/','女士们；lady 的复数；女洗手间〔the ladies，英式〕',
 '正式招呼一群女士，可以用 ladies。商店、活动或礼貌交谈中，它也常是 women 的一种称呼方式，具体语气由场景决定。',
 'lady 的 y 改成 ies。lady 接古英语女主人名称，后来用于身份称呼、女士；更早与面包、和面者相关的传统构词解释存在争议，复数形式本身不包含那些社会意义。',
 [['古英语女主人称呼 → lady','身份称呼 → 女士等较广用法'],['lady 的 y → ies → ladies','多位女士；部分固定结构另有约定用法']],
 'Ladies and gentlemen 女士们、先生们；the ladies at the table 桌旁的女士们；ladies’ coats 女式外套；the ladies 女洗手间〔英式〕。',
 'two ladies；Good evening, ladies。','ladies 是复数，lady’s 是单数所有格，ladies’ 是复数所有格。普通陈述可用 women，礼貌称呼、标题中常见 ladies，两者语气并非处处一样。',
 ('Good evening, ladies and gentlemen.','女士们、先生们，晚上好。'),('The two ladies at the next table were discussing a book.','邻桌的两位女士正在讨论一本书。'),sources=['https://www.etymonline.com/word/lady','https://en.wiktionary.org/wiki/ladies#English'])
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_vu',ROOTS,WORDS)
 extend_lessons()
