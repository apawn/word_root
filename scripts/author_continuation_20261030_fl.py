"""Identify, newspaper, scared and trend: recognition, reporters, fear and direction."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
I=[['拉丁 idem 这一“相同”词族 → 法语 identité、identifier 等','把对象认作同一个；确定身份'],['法语 identifier → 英语 identify','认出、鉴定；认同'],['英语派生','identifiable 可识别；identifier 识别者、标识符']]
W('identify','/aɪˈdentɪfaɪ/','认出、确认身份；鉴定；找出；认同',
 '照片里的人和眼前这个人对上了，或给未知植物找到了名字：把“这是谁、这是什么”确认下来。',
 '借法语 identifier，接 identité、identique 等相同词族，远连拉丁 idem“同一个”。-ify 对应使成某种关系的动词材料，不是英文 identify = idea 想法 + 某个尾巴。',I[:2],
 'identify a person 认出某人，identify a problem 找出问题，identify as 认同自己是某身份，identify with a character 对角色有共鸣。',
 'identify the cause；identify as；identify with；identify someone by。',
 'identify with 是把自己和别人经历对上、产生共鸣；identify someone 则是认出身份，with 有无会改变句法和意思。',
 ('Can you identify the bird in this photograph?','你能认出照片里的鸟是什么鸟吗？'),('Many readers identify with the main character.','许多读者对主角有共鸣。'),
 sources=['https://www.etymonline.com/word/identify','https://en.wiktionary.org/wiki/identify#English'])
W('identifiable','/aɪˌdentɪˈfaɪəbəl/','可辨认的、能确认身份的',
 '虽换了衣服、画面有点模糊，仍能看出是谁；也可说某个规律、特征清楚到能认出来。',
 'identify + -able，y 在后缀前变 i，形成 identifi-able；表示能被识别，不是已经辨认完的 identified。',I[:2]+[['identify + -able → identifiable','能够被认出、区分']],
 'easily identifiable 容易识别，an identifiable pattern 可辨认规律，personally identifiable information 可识别个人身份的信息。',
 'easily identifiable；an identifiable pattern；an identifiable feature。',
 'identifiable 是能辨认，identical 是相同；两件 identical 的制服可能反而让不同人难以 identifiable，意思不互换。',
 ('The building is easily identifiable by its red roof.','这栋楼凭红屋顶很容易认出来。'),('The study found no identifiable pattern.','研究没有发现可辨认的规律。'))
W('identifier','英 /aɪˈdentɪfaɪə/；美 /aɪˈdentɪfaɪər/','标识符、识别码；识别者、识别工具',
 '一串号码或名字，像给对象挂上名牌，让系统知道正在说哪一个；不一定是身份证号码。',
 'identify + -er，y 变 i，命名做识别的人、工具或用于识别的信息。计算机中的 identifier 常就是程序里某个名称。',I[:2]+[['identify + -er → identifier','识别的人、东西；标识符']],
 'a unique identifier 唯一标识符，a user identifier 用户标识，an identifier in code 代码里的标识符。',
 'a unique identifier；a user identifier；a valid identifier。',
 'identifier 是用来识别的符号或主体，identity 是身份、同一性；有编号不等于这个编号在所有系统中都唯一。',
 ('Each order has a unique identifier.','每笔订单都有一个唯一标识符。'),('Choose a clear identifier for the variable.','给变量选一个清楚的标识符。'))
R('B3432','把对象和某个身份、名称对上','IDENTIFY：这一个，到底是谁、是什么','identify → identifiable 能被识别；identifier 用于识别。identify with 还能说经历对上、产生共鸣。',
 '“同一个”的旧核心能连接认出身份与认同；但 identify a problem 也常只是找出问题，未必在查一个人的证件。',
 'idem 同一个 → 法语 identité、identifier 等 → identify；identify + -able/-er，y 变 i。',
 [['识别与认同动作','identify'],['识别可能与识别依据','identifiable · identifier']],
 'identify/identify with 认出与共鸣；identifiable/identical 能认出与相同；identifier/identity 标识与身份。',
 'The identifier makes each record identifiable.\n\n标识符让每条记录都能被区分出来。','identify identifiable identifier')
W('newspaperman','英 /ˈnjuːzpeɪpəmæn/；美 /ˈnuːzpeɪpərmæn/','报人、报社男记者或编辑',
 '在报业里写新闻、编辑报道的人；man 在这里接从业者，不是只负责把报纸递到门口的那个人。',
 'newspaper 报纸 + man，报业人物称呼。newspaper 本身是 news 消息 + paper 纸、报刊的组合。',
 [['news + paper → newspaper','报载新闻的刊物'],['newspaper + man → newspaperman','报业中的男性从业者']],
 'a veteran newspaperman 资深报人，a local newspaperman 当地报人。可用于旧报业回忆、人物介绍，不一定仅指外出采访记者。',
 'a veteran newspaperman；a local newspaperman；an experienced newspaperman。',
 'newspaperman 报业从业者，paperboy 送报男孩等称呼侧重递送；journalist 范围更广，也不突出性别。',
 ('The veteran newspaperman knew everyone in town.','这位资深报人认识镇上每个人。'),('He began his career as a local newspaperman.','他最初在地方报业开始职业生涯。'))
R('B3357','把新闻放进刊物，再命名报业从业者','NEWSPAPER：新闻刊物；NEWSPAPERMAN：报业人物','news + paper → newspaper；newspaper + man → newspaperman。',
 '现代 newspaper 可以有网络版，不是离开纸张就绝不能这样叫。报人和送报者的工作角色也要分。',
 'news + paper → newspaper；newspaper + man → newspaperman。',
 [['刊物','newspaper'],['报业人物','newspaperman']],
 'newspaperman/paperboy 报业采编等与递送；newspaper/journalist 刊物与更广的新闻从业者。',
 'The newspaperman wrote for a local newspaper.\n\n这位报人为一家地方报纸撰稿。','newspaper newspaperman')
S=[['古诺尔斯语 skirra → 中古英语 skerren 等 → scare','使害怕、避开等旧义，进入吓唬词族'],['scare + -ed → scared','被吓到；处于害怕状态']]
W('scare','英 /skeə/；美 /sker/','吓、使害怕；惊吓、恐慌',
 '突然一声响，把人心里吓一跳；做动作是 scare，受到这一下的感觉是一场 scare。',
 '来自中古英语 skerren 等，接古诺尔斯语 skirra 的惊吓、避开相关用法。现代词形经历变化，不是 s- + care“去关心”。',S[:1]+[['英语 scare 名词、动词','吓人；一次惊吓或恐慌']],
 'scare someone 吓某人，scare away 吓跑，give someone a scare 吓某人一跳，a health scare 健康疑虑引起的惊慌。',
 'scare away；give someone a scare；scare easily；a false scare。',
 'scare 可突然吓，也可借担忧施压；care 关心和 scare 不按现代加字母构成反义词。',
 ('The loud bang scared the dog.','巨响吓到了狗。'),('You gave me quite a scare!','你真把我吓了一大跳！'),
 sources=['https://www.etymonline.com/word/scare','https://en.wiktionary.org/wiki/scare#English'])
W('scared','英 /skeəd/；美 /skerd/','害怕的、受惊的',
 '吓人的东西在外面，害怕的感受落到你身上；scared 站在那个“被吓到的人”的角度。',
 'scare + -ed，分词发展为常用形容词；末尾 /d/，不是再添一个完整 /ɪd/ 音节。',S,
 'scared of the dark 怕黑，scared to ask 不敢问，scared that… 担心会……，scared stiff 吓呆了。',
 'scared of；scared to；scared that；scared stiff。',
 'scared 是感到害怕，scary 通常说令人害怕；a scared child 是怕了的孩子，a scary story 是吓人的故事。',
 ('The child was scared of the dark.','孩子怕黑。'),('I was scared to ask another question.','我不敢再问一个问题。'))
R('B4512','吓人的动作，落到人的害怕状态','SCARE → SCARED：吓到了，所以害怕','scare 动作、一次惊吓 → scared 受惊、害怕；和 scary 吓人的角度对照。',
 '别把两种形容词都只背“害怕”：scared 是里面的感受，scary 是让人产生这种感受的性质。',
 'skirra → skerren 等 → scare；scare + -ed → scared。',
 [['吓与惊吓','scare'],['感到害怕','scared']],
 'scared/scary 感受者与造成感受的事物；scare/care 不按加 s 构成反义。',
 'The sudden noise scared me, and I was too scared to move.\n\n突然的响声吓到了我，我怕得不敢动。','scare scared')
T=[['古英语 trendan → 中古英语 trenden','转、滚动等旧动作'],['英语方向、走势用法 → trend','河道等朝某方向延伸，再借到事情发展倾向'],['流行与趋势组合','trendy 时髦；trending 正热；trendsetter 带起潮流；uptrend、downtrend 走势方向']]
W('trend','/trend/','趋势、倾向；流行风尚；朝某方向发展',
 '把一段时间里的点连起来，看大体往哪走；流行也是人群偏好朝某方向移动，不只是今天一件孤立小事。',
 '接古英语 trendan、中古英语 trenden 的转、滚等旧动作，再发展出朝某方向延伸、事情走势。现代含义不能只按“滚圈”逐字翻。',T,
 'an upward trend 上升趋势，a trend towards… 朝向……的趋势，fashion trends 时尚趋势，prices trend upward 价格趋升。',
 'a trend towards；follow a trend；a growing trend；trend upward。',
 'trend 指方向、倾向，不保证一路没有起伏，也不保证将来一定延续；fad 常突出一阵短时风潮。',
 ('The figures show a clear downward trend.','这些数字显示出清楚的下降趋势。'),('There is a growing trend towards remote work.','远程办公正成为越来越明显的趋势。'),
 sources=['https://www.etymonline.com/word/trend','https://en.wiktionary.org/wiki/trend#English'])
W('trending','/ˈtrendɪŋ/','正在成为热门的、热议中的；呈某种趋势的',
 '大家这会儿正往这个话题聚，讨论度往上走；网上热榜常用它，不是表示这个话题永远最重要。',
 'trend + -ing，由正在发展、形成趋势的分词用法扩展到热门话题形容词。',T[:2]+[['trend + -ing → trending','正在呈趋势；网络上正热议']],
 'a trending topic 热议话题，trending searches 热门搜索，trending upward 呈上升趋势。',
 'a trending topic；trending searches；trending upward。',
 'trending 说此刻走热，trendy 说符合时髦风尚；一个 trending 灾害话题不该因此翻成时髦灾害。',
 ('The interview became a trending topic overnight.','这段采访一夜之间成了热议话题。'),('Searches for the song are trending upward.','这首歌的搜索量呈上升趋势。'))
W('trendy','/ˈtrendi/','时髦的、追逐潮流的',
 '穿着、店铺、说法正合眼下流行的那一套；可以赞时新，也可以暗示只是跟风。',
 'trend 流行趋势 + -y，形成符合当下潮流的性质。',T[:2]+[['trend + -y → trendy','时髦、随潮流的']],
 'a trendy café 时髦咖啡馆，trendy clothes 时髦衣服，a trendy neighbourhood 新潮街区。',
 'a trendy café；trendy clothes；a trendy neighbourhood。',
 'trendy 符合潮流，stylish 可说品味好而不必追当季；trending 说正在走热，两者不能只因同根就互换。',
 ('They opened a trendy café near the station.','他们在车站附近开了家时髦咖啡馆。'),('She prefers comfortable clothes to trendy ones.','比起时髦衣服，她更喜欢穿着舒服的。'))
W('trendsetter','英 /ˈtrendˌsetə/；美 /ˈtrendˌsetər/','潮流引领者、开风气者',
 '别人还没开始，你先带起一种穿法、做法，后来大家跟上；setter 在这里是把风尚立起来的角色。',
 'trend 趋势 + setter〔set + -er〕，命名建立、推动某种风尚的人或事物，不是只会观察趋势的人。',T[:2]+[['trend + setter → trendsetter','带起风尚、让别人跟随的主体']],
 'a fashion trendsetter 时尚引领者，a cultural trendsetter 文化风尚引领者，become a trendsetter 成为开风气者。',
 'a fashion trendsetter；a cultural trendsetter；become a trendsetter。',
 'trendsetter 带起潮流，follower 跟随；trendy 只说符合时尚，不证明自己首创。',
 ('The designer became a trendsetter in street fashion.','这位设计师成了街头时尚的引领者。'),('The small studio has proved to be a cultural trendsetter.','这家小工作室已经显示出引领文化风尚的作用。'))
W('uptrend','/ˈʌptrend/','上升趋势、向上走势',
 '点线上下晃，但把一段时间放在一起看，大体往上走；不要求每一步都比上一步高。',
 'up 向上 + trend 趋势，方向组合名词。说用户数、价格、需求等都可以，不限金融。',T[:2]+[['up + trend → uptrend','总体向上的走势']],
 'an uptrend in demand 需求上升走势，a steady uptrend 稳定上升趋势，a continuing uptrend 持续上升走势。',
 'an uptrend in；a steady uptrend；a continuing uptrend。',
 'uptrend 一段时间总体向上，an increase 可以只说一次增加；uptrend 本身不保证下一次仍上升。',
 ('The survey shows an uptrend in public transport use.','调查显示公共交通使用量呈上升趋势。'),('The uptrend continued despite a small decline in May.','虽然五月小幅下降，总体上升趋势仍在继续。'))
W('downtrend','/ˈdaʊntrend/','下降趋势、向下走势',
 '与 uptrend 相反，整体朝低处走；中间偶尔反弹不一定就改变总体方向。',
 'down 向下 + trend 趋势，与 uptrend 对称组合，不把 down 当情绪低落的唯一意思。',T[:2]+[['down + trend → downtrend','总体向下的走势']],
 'a downtrend in sales 销量下降趋势，a long downtrend 长期下行走势，reverse a downtrend 扭转下降趋势。',
 'a downtrend in；a long downtrend；reverse a downtrend。',
 'downtrend 是方向，low 是水平；数值很高也可以处于 downtrend，数值很低也可能正处于 uptrend。',
 ('The chart shows a downtrend in paper consumption.','图表显示纸张用量呈下降趋势。'),('The recent increase did not end the longer downtrend.','最近的增加并没有结束更长期的下降趋势。'))
R('B4101','像沿一条路走，观察总体方向','TREND：看一串变化，不只看一个点','trend → trending、trendy、trendsetter；uptrend/downtrend 用上下标方向。',
 '正热议不等于时髦，时髦不等于首创；走势向上也不等于数值本来就高。把方向、热度、风尚角色分别理解。',
 'trendan、trenden 转动等 → 朝某方向延伸 → trend 趋势；+ -ing/-y；trend + setter；up/down + trend。',
 [['基础与流行状态','trend · trending · trendy'],['带起潮流的角色','trendsetter'],['总体方向','uptrend · downtrend']],
 'trending/trendy 热议与时髦；trendsetter/follower 引领与跟随；uptrend/high 方向与水平。',
 'The trendy café became a trending topic, and its visitor numbers showed an uptrend.\n\n这家时髦咖啡馆成了热门话题，到访人数也呈上升趋势。','trend trending trendy trendsetter uptrend downtrend')
if __name__=='__main__':save('continuation_20261030_fl',ROOTS,WORDS)
