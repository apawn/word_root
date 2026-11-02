"""Conservative, engage and bob: cautious continuity, involvement and short motions."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
C=[['拉丁 conservāre、conservātīvus → 法语 conservatif → conservative','保存、守护 → 倾向保留'],['政治与一般做事风格','保守思想；谨慎、不激进的估计和穿着'],['派生','conservatism 保守主义、保守倾向；conservatively 保守地、谨慎地']]
W('conservatism','英 /kənˈsɜːvətɪzəm/；美 /kənˈsɜːrvətɪzəm/','保守主义、保守思想；谨慎保守的倾向',
 '先把已有的做法、秩序守住，再谨慎看变化；政治里是一大类传统，普通工作里也可说不愿冒进的态度。',
 '通常对应 conservative + -ism，词形调整为 conservatism，历史也有其他相近构词分析。较早 conservāre 是保存、守护，不是 conserve 果酱才生出政治。',C[:2]+[['conservative 对应 -ism → conservatism','保守思想；一般谨慎保守倾向']],
 'political conservatism 政治保守主义，cultural conservatism 文化保守倾向，financial conservatism 财务上的谨慎态度。',
 'political conservatism；cultural conservatism；a tendency towards conservatism。',
 'conservatism 政治含义因历史传统不同，不自动等于每个国家某个政党；日常谨慎态度也不保证政治立场相同。',
 ('The book traces the history of political conservatism.','这本书追溯政治保守主义的历史。'),('The company’s conservatism slowed the adoption of new methods.','公司的保守态度拖慢了新方法的采用。'),
 sources=['https://en.wiktionary.org/wiki/conservatism#English','https://www.etymonline.com/word/conservatism'])
W('conservatively','英 /kənˈsɜːvətɪvli/；美 /kənˈsɜːrvətɪvli/','保守地；谨慎地、往稳妥方向地',
 '穿得保守不张扬，估计不把结果说得太满，都可 conservatively；不一定每次在谈政治。',
 'conservative + -ly，副词修饰做事、估算、穿着等方式，接的是整个形容词而非只接 con-。',C[:2]+[['conservative + -ly → conservatively','以保守、谨慎方式']],
 'dress conservatively 穿着保守，estimate conservatively 保守估计，act conservatively 谨慎行事。',
 'dress conservatively；estimate conservatively；act conservatively。',
 'conservatively estimated 常是避免夸大的估法，但保守方向要看对象；收入低估、成本留余量等不必都对应同一数字方向。',
 ('She dressed conservatively for the interview.','她为面试穿得比较保守。'),('The repairs were conservatively estimated to take a month.','保守估计，修理需要一个月。'))
R('B3775','保留、守护的倾向及谨慎做事风格','CONSERVATIVE：先守住已有，再谨慎对待改变','conservative → conservatism、conservatively；neoconservative 接特定政治思想背景。',
 '政治传统与一般谨慎估计分语境，穿得保守也不等于已经声明政治立场。',
 'conservāre、conservātīvus 经法语 → conservative；conservative 对应 conservatism；conservative + -ly；neo- + conservative。',
 [['基础、思想与做事方式','conservative · conservatism · conservatively'],['特定思想名称','neoconservative']],
 'conservatism 政治与一般态度；conservatively 数字方向依对象；neoconservative 不能只按所有新的保守者直译。',
 'The conservatively dressed speaker discussed the history of conservatism.\n\n那位穿着保守的讲者讨论了保守主义历史。','conservative conservatism conservatively neoconservative')
E=[['法语 en gage、engagier → engage','在担保、承诺之下 → 使受约束、参与'],['多场景的联系与投入','吸引注意、雇请、订婚；机械接合；参与行动'],['派生与独立借词','engaged、engaging；法语 engagement → engagement；disengage 脱开']]
W('engage','/ɪnˈɡeɪdʒ/','参与、使投入；吸引注意；雇请；使接合',
 '把人、注意力或部件接进一件事里：学生投入讨论，故事抓住读者，齿轮接上工作，都可以 engage。',
 '经法语 engagier，en- 在……中 + gage 担保、承诺，先有承诺绑定背景，后来进入投入、雇请、订婚和机械接合等义。',E,
 'engage in discussion 参加讨论，engage with an idea 认真回应观点，engage the audience 吸引观众，engage the gears 使齿轮接合。',
 'engage in；engage with；engage the audience；engage the gears。',
 'engage in 常参加活动，engage with 强调与对象互动、认真处理；engage the audience 直接接被吸引的人。',
 ('The activity engaged every student in the class.','活动让全班学生都投入其中。'),('The article engages with several opposing views.','文章认真回应了几种相反观点。'),
 sources=['https://en.wiktionary.org/wiki/engage#English','https://www.etymonline.com/word/engage'])
W('engaged','/ɪnˈɡeɪdʒd/','已订婚的；投入的、忙于某事的；占线的〔英式〕；接合的',
 '承诺把两个人联系起来，是订婚；注意力被事情占住，是投入、忙着；电话线已被占用，英式也说 engaged。',
 'engage + -ed，过去分词作状态形容词，保留不同接合、占用、承诺分支。词尾 /dʒd/ 不另加 /ɪd/ 音节。',E[:2]+[['engage + -ed → engaged','已承诺、已接上、注意力或线路被占用的状态']],
 'engaged to someone 与某人订婚，engaged in work 忙于工作，an engaged audience 投入的观众，the line is engaged 电话占线。',
 'engaged to；engaged in；an engaged audience；the line is engaged。',
 'engaged to 订婚对象常用 to；engaged in 忙于活动用 in；be engaged 不一定订婚，还要看后续搭配。',
 ('They got engaged last spring.','他们去年春天订婚了。'),('The students were fully engaged in the discussion.','学生们全身心投入了讨论。'))
W('engaging','/ɪnˈɡeɪdʒɪŋ/','吸引人的、有趣迷人的；正在参与、吸引',
 '故事、笑容、讲法让人愿意继续听、继续看，是 engaging；它说能抓住别人，而不是自己已经订婚。',
 'engage 去 e + -ing，分词也作吸引人的性质形容词。与 engaged 的受吸引、参与状态方向分开。',E[:2]+[['engage + -ing → engaging','正在吸引、参与；能吸引人的性质']],
 'an engaging story 引人入胜的故事，an engaging speaker 讲得吸引人的讲者，an engaging smile 迷人微笑。',
 'an engaging story；an engaging speaker；an engaging smile。',
 'engaging 造成吸引，engaged 观众已投入；engaging smile 不是订婚笑容，订婚状态在 engaged 分支。',
 ('She is an engaging speaker.','她讲话很吸引人。'),('The book tells an engaging story about the town.','书里讲了一个有关小镇的动人故事。'))
W('engagement','/ɪnˈɡeɪdʒmənt/','订婚；约定活动；参与、投入、互动；交战、接合〔按语境〕',
 '可以是一项婚约、早已约好的活动，也可以是人与内容持续接上、互动的程度；social media engagement 常说互动，不是平台在办婚礼。',
 '借法语 engagement，现代对应 engage + -ment。承诺、接合、投入的不同分支进入名词，不只在英语里单一订婚义后造其他义。',E[:2]+[['法语 engagement → engagement；对应 engage + -ment','承诺、约定、订婚；投入、交战、接合等名词']],
 'an engagement ring 订婚戒指，a speaking engagement 演讲约定，student engagement 学生投入，audience engagement 观众互动。',
 'an engagement ring；a speaking engagement；student engagement；audience engagement。',
 'engagement 指标在不同平台有不同口径，别只凭一个词就假定完全相同；appointment 常具体预约，engagement 可较正式既定活动。',
 ('She wore a simple engagement ring.','她戴着一枚简洁的订婚戒指。'),('The teacher used stories to improve student engagement.','老师用故事提高学生的投入程度。'))
W('disengage','/ˌdɪsɪnˈɡeɪdʒ/','脱开、解除接合；抽身、退出互动',
 '原来接着、投入着，现在把连接松开：零件脱开、人停止争执、注意力离开，都可沿这个画面。',
 '接法语 désengager 等，现代可拆 dis- 分开、解除 + engage；不是把 engage 内的 en- 换成否定。',E[:1]+[['法语 désengager → disengage；dis- + engage','解除接合、约束 → 抽身退出']],
 'disengage the clutch 使离合器分离，disengage from an argument 从争论中抽身，disengage the mechanism 脱开机构。',
 'disengage from；disengage the clutch；disengage the mechanism。',
 'disengage 退出联系，disagree 不同意；可以仍积极讨论而不同意，也可以不表态就抽身离开。',
 ('He disengaged from the argument and went outside.','他退出争论，走到外面。'),('The device disengages automatically when the cycle ends.','周期结束时，装置会自动脱开。'))
R('B4315','承诺把关系接上，到注意力投入、零件接合','ENGAGE：把某人某物接进一件事里','engage → engaged、engaging、engagement；disengage 是脱开、抽身。',
 '订婚、观众互动、机械接合都要按对象选义；engaging 作品吸引人，engaged 观众已经投入，方向别倒。',
 'en gage、engagier → engage；engage + -ed/-ing；法语 engagement → engagement；désengager → disengage。',
 [['动作与两种分词性质','engage · engaged · engaging'],['承诺、互动名词与脱开','engagement · disengage']],
 'engaged to/in 订婚对象与忙于活动；engaging/engaged 造成吸引与投入状态；engagement 非只订婚；disengage/disagree 抽身不同意。',
 'The engaging story kept the audience engaged.\n\n引人入胜的故事让观众一直很投入。','engage engaged engaging engagement disengage')
B=[['中古英语 bobben → bob〔短促上下动〕','上下轻跳、浮动；更远来源不定'],['bobbe 等团簇、短截名词 → bob 的相关名称','短发、短尾、悬垂块；不同形式历史交织'],['bobble、bobsled 等组合','反复小动、小毛球；短滑橇背景的雪车名']]
W('bob','英 /bɒb/；美 /bɑːb/','上下浮动、轻点头；波波头；悬垂小块、摆锤等',
 '浮标在水面一上一下是 bob；头轻点一下也可。a bob 发型则是整齐短发，不能只因为发丝会动就说发型从浮标产生。',
 '动词接中古英语 bobben，远源不明；发型、悬垂块等名词联系 bobbe 团簇、短截等旧形式，历史相互纠缠。Bob 人名是 Robert 变形，另看专名。',B,
 'bob up and down 上下浮动，bob your head 轻点头，a short bob 短波波头，a pendulum bob 摆锤。',
 'bob up and down；bob your head；a short bob；a pendulum bob。',
 'bob 动作短促上下，nod 常点头表达回应；Bob 大写人名不由一位爱点头的人被正式命名而来。',
 ('The little boat bobbed on the water.','小船在水上上下浮动。'),('She had her hair cut into a short bob.','她把头发剪成了短波波头。'),
 sources=['https://en.wiktionary.org/wiki/bob#English','https://www.etymonline.com/word/bob'])
W('bobble','英 /ˈbɒbl/；美 /ˈbɑːbl/','小毛球、绒球；起球；晃动；接球失误〔美式体育语境〕',
 '帽顶挂一团小毛球，或毛衣表面起小球，都叫 bobble；动词还有小幅晃动、球没接稳弹了一下的用法。',
 'bob + -le，名词词尾可小称、动词词尾可反复小动作。不是名词 bobble 每个义都从一次点头直接变来。',B[:2]+[['bob + 名词小称 -le → bobble','小团、绒球等'],['bob + 动词反复 -le → bobble','小幅晃动、处理不稳等']],
 'a bobble hat 毛球帽，bobbles on a sweater 毛衣起的小球，bobble a catch 没接稳球。',
 'a bobble hat；bobbles on a sweater；bobble a catch。',
 'bobble 毛球或不稳动作，bubble 气泡是另一词；拼写、元音不同，不是一个发音的随意变体。',
 ('He wore a woollen bobble hat.','他戴着一顶有毛球的羊毛帽。'),('The player bobbled the ball before catching it.','球员接球时先没接稳，随后才抓住。'))
W('bobsled','英 /ˈbɒbsled/；美 /ˈbɑːbsled/','有舵雪车、比赛雪车；乘这种雪车滑行',
 '今天常见的是冰道上滑行的比赛雪车；词在这项运动以前已有运输雪橇用法，别把运动员上下摇身加速的传说当唯一词源。',
 'bob + sled，早期联系短橇、前后相接的短滑行支架等，具体更早由来不全清楚。bobsleigh /ˈbɒbsleɪ/〔英〕、/ˈbɑːbsleɪ/〔美〕是常见对应名称。',B[1:2]+[['bob〔短橇等旧材料〕+ sled → bobsled','早期运输雪橇组合，先于现代比赛'],['现代常见运动用法','有舵比赛雪车；与 bobsleigh 对应']],
 'a bobsled team 雪车队，a bobsled race 雪车比赛，a two person bobsled 双人雪车。',
 'a bobsled team；a bobsled race；a two person bobsled。',
 'bobsled 特定雪车，普通儿童小雪橇常 sled；bobcat 接短尾动物名，不能因都有 bob 就属于同一类雪上运动。',
 ('The bobsled team practised on the ice track.','雪车队在冰道上训练。'),('The museum displayed an early wooden bobsled.','博物馆展出了一辆早期木制雪橇。'),
 sources=['https://en.wiktionary.org/wiki/bobsled#English','https://www.etymonline.com/word/bobsled'])
R('B3648','短促上下动，与短截、悬垂团块的旧名词分支','BOB：浮动一点点，短发、短尾、毛球则另看旧材料','bob → bobble；bobsled 早有短橇运输背景；bobcat 取短尾名称。',
 'bob 系列远源多处不定，能记住常见画面而不编唯一祖先。Bob 人名从 Robert，雪车不只从运动员点头故事来。',
 'bobben → bob 动词；bobbe 等 → 团簇、短截名词；bob + -le；bob + sled/cat。',
 [['基础动作、名词与毛球','bob · bobble'],['雪车与短尾动物','bobsled · bobcat']],
 'bob/Bob 普通词专名；bobble/bubble 毛球气泡；bobsled/sled 专用比赛与一般雪橇；bobsleigh 为对应名称。',
 'The bobble on his hat bobbed as he watched the bobsled race.\n\n他看雪车比赛时，帽顶毛球上下晃动。','bob bobble bobsled bobcat')
if __name__=='__main__':save('continuation_20261030_ex',ROOTS,WORDS)
