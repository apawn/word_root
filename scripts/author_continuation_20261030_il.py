"""Hack branches, masking, a place-name sport and ducks."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
H=[['中古英语 hacken，联系古英语 tohaccian 等','用力砍、粗切'],['现代技术、技巧义的扩展','动手巧做、临时修补、巧妙办法；也指未经授权入侵'],['另线 hackney 截短为 hack','受雇马匹、出租车；受雇写手等，不全从砍木头而来']]
W('hack','/hæk/','砍、劈；巧妙办法、临时补丁；入侵；受雇写手〔另线〕',
 '树林里 hack 是粗砍，代码里 a hack 可是先把问题弄通的办法，生活里 a useful hack 是实用小窍门。但新闻说账号被 hacked，通常是遭入侵。',
 '砍义接中古英语 hacken 等。技术用法经现代工程、编程文化发展，不能把整个过程编成拿斧子劈开电脑。另有 hackney 截短的受雇写手、出租车等同形义；咳嗽义来源又不确定。',H,
 'hack at a branch 砍树枝，a quick hack 临时解决办法，a useful cooking hack 烹饪小窍门，hack into an account 入侵账号，a hack writer 应付差事的写手。can’t hack it 是应付不来。',
 'hack at；a quick hack；a useful hack；hack into；can’t hack it。',
 'a hack 可能巧妙，也可能粗糙难维护，要看评价。a political hack、a hack writer 的 hack 不能一律当电脑黑客；不同同形词有交汇，不强接一条砍树故事。',
 ('The team used a quick hack to keep the demo running.','团队用了一个临时办法，让演示先运行起来。'),('The article shares a useful hack for folding a fitted sheet.','文章分享了一个折叠床笠的实用小窍门。'),sources=['https://en.wiktionary.org/wiki/hack#English','https://www.etymonline.com/word/hack','https://tmrc.mit.edu/old/hackers-ref.html'])
W('hacking','/ˈhækɪŋ/','动手探索技术；入侵行为；反复干咳的〔依语境〕',
 '同一个 hacking，在技术社群可能是兴致勃勃拆解、试做，在安全新闻可能是入侵；a hacking cough 则是短促反复的干咳。',
 'hack + -ing，行为过程或形容性质。不同含义跟随 hack 的相应分支；咳嗽来源不确定，不能说人在咳出代码。',H[:2]+[['hack + -ing → hacking','相应活动或反复、断续的性质'],['另看咳嗽分支','a hacking cough，短促反复的干咳']],
 'creative hacking 创意技术探索，a hacking incident 入侵事件，a hacking cough 断续干咳。MIT 的校园 hacks 还可指富有巧思的恶作剧、创作。',
 'creative hacking；a hacking incident；a hacking cough。',
 '单凭 hacking 一词不能判断整件事是违法入侵还是技术探索，要读对象和描述；咳嗽搭配是形容词用法。',
 ('The report describes a hacking incident that affected the website.','报告描述了一次影响网站的入侵事件。'),('A hacking cough interrupted his speech.','一阵反复的干咳打断了他的发言。'),sources=['https://en.wiktionary.org/wiki/hacking#English','https://handbook.mit.edu/hacking/'])
W('hacker','英 /ˈhækə/；美 /ˈhækər/','擅长动手探索、编程的人；计算机入侵者；砍削者等',
 '先别只想蒙脸入侵的人。某些技术社群把 hacker 当褒义，指能深入理解系统、用巧办法做东西的人；新闻里又常指入侵者。',
 'hack + -er 的砍削者用法很早。现代技术称呼有自身社群发展史，与巧做、实验的 hack 相连；不能说今天每个 hacker 都由一个砍木工直线变来。',H[:2]+[['hack + -er；现代技术社群扩展','进行相应活动的人；编程、技术能手或入侵者']],
 'a skilled hacker 技术高手〔需看上下文〕，an ethical hacker 从事授权安全测试的人，a hacker community 黑客技术社群。',
 'a hacker community；an ethical hacker；a hacker targeted the website。',
 'hacker 的褒贬因语境不同；ethical hacker 不用入侵新闻里的恶意含义理解。早期砍削者、少见出租车司机同形义，也不能拿来解释所有现代头衔。',
 ('The documentary interviews hackers who build their own tools.','纪录片采访了自行制作工具的技术爱好者。'),('A hacker gained access to the company’s website.','一名入侵者进入了公司的网站。'),sources=['https://en.wiktionary.org/wiki/hacker#English','https://tmrc.mit.edu/old/hackers-ref.html'])
W('hackathon','英 /ˈhækəθɒn/；美 /ˈhækəθɑːn/','黑客马拉松；集中协作开发活动',
 '把一群人聚到一起，在有限时间里集中做出原型、产品或方案。重心是动手协作，不是比谁入侵的网站多。',
 'hack 技术动手探索 + -athon，后者由 marathon 马拉松抽出的持续活动构词成分。不是古希腊单独有个 athon 表示编程比赛。',H[1:2]+[['marathon → -athon','借长时间持续活动的意象构词'],['hack + -athon → hackathon','集中协作、开发和展示成果的活动']],
 'join a hackathon 参加黑客马拉松，a weekend hackathon 周末集中开发活动，a hackathon prototype 活动中做出的原型。',
 'join a hackathon；a weekend hackathon；a hackathon prototype。',
 'hackathon 常有主题、时限、展示或比赛，但不必每场规则相同，也不只允许程序员参与。名字没有要求恶意入侵。',
 ('Our team built a simple map app at the hackathon.','我们团队在黑客马拉松上做出了一个简单地图应用。'),('Designers and programmers worked together during the weekend hackathon.','设计师和程序员在周末的集中开发活动中一起协作。'),sources=['https://en.wiktionary.org/wiki/hackathon#English','https://www.merriam-webster.com/dictionary/hackathon'])
W('hacky','/ˈhæki/','靠临时补丁凑成的；不够规整、取巧的〔口语〕',
 '东西倒是能跑，可做法像东补一块、西绕一下，缺少干净稳妥的结构；程序员说 hacky 常是这个意思。',
 '技术义 hack 临时解决办法 + -y，形成性质形容词。另有从 hackneyed 改来的陈旧俗套义，不把所有同形用法硬归为电脑补丁。',H[1:2]+[['hack + -y → hacky','临时拼补、取巧而欠规整的'],['另一路 hackneyed 的改形','陈旧、俗套的同形用法']],
 'a hacky solution 不够规整的临时方案，a hacky workaround 取巧绕过问题的做法，look a bit hacky 看起来有点东拼西凑。',
 'a hacky solution；a hacky workaround；look a bit hacky。',
 'hacky 通常评价方案结构、做法，不等于已经遭到黑客攻击。quick 快也不一定 hacky，干净方案同样可以做得很快。',
 ('It is a hacky solution, but it will let us test the idea.','这是个不够规整的临时方案，不过能让我们先测试想法。'),('We replaced the hacky workaround with a simpler design.','我们用更简洁的设计替换了那个东拼西凑的变通办法。'))
W('hacksaw','英 /ˈhæksɔː/；美 /ˈhæksɔː/，部分美式口音 /ˈhæksɑː/','钢锯、弓形锯；用钢锯锯',
 '一个框架绷住一条细锯条，是常见的手工钢锯。这里 hack 回到切削，不是在锯上装电脑系统。',
 'hack 砍、切削 + saw 锯。工具名按切削用途组合，不是 saw 看见的过去式参与构词。',H[:1]+[['hack + saw → hacksaw','带绷紧锯条的切削工具']],
 'a hacksaw blade 钢锯条，a small hacksaw 小钢锯，a hacksaw frame 钢锯架。常见用途是切金属等材料，具体适用范围还看锯条。',
 'a hacksaw blade；a small hacksaw；a hacksaw frame。',
 'saw 锯这个名词与 see 的过去式 saw 同形，不能据此拆成看见黑客。hacksaw 是具体工具名，不是所有锯的总称。',
 ('The workshop display includes a hacksaw and several spare blades.','工坊展台放着一把钢锯和几条备用锯条。'),('The drawing labels the frame and blade of the hacksaw.','图中标出了钢锯的锯架和锯条。'))
W('haggle','/ˈhæɡəl/','讨价还价；为条件反复争论',
 '卖家报一个数，买家再削一点，来来回回磨价格。这个一点点砍的画面能帮你记讨价还价。',
 '来自 hack 的旧变体 haggen 砍，加表示反复动作的词尾，早义粗切、不齐地切；价格争论义可能由反复削去的画面发展，不是现代英语直接把 hack 拼错。',
 [['中古英语 haggen，联系 hacken','砍、粗切'],['反复动作形式 → haggle','反复砍、切得不齐'],['可能由一点点削去的比喻发展','为价格或条款来回讨价还价']],
 'haggle over the price 为价格讨价还价，haggle with a seller 与卖家讲价，haggle over details 为细节反复争论。',
 'haggle over；haggle with；haggle over details。',
 'haggle 强调来回争取，negotiate 范围更广、更中性；barter 是以物易物，不是所有讲价都在交换物品。',
 ('They haggled over the price for ten minutes.','他们为价格来回讲了十分钟。'),('The two sides are still haggling over the final details.','双方还在为最后的细节反复争论。'),sources=['https://en.wiktionary.org/wiki/haggle#English','https://www.etymonline.com/word/haggle'])
R('B2685','砍削、反复削价，与技术探索的现代分支','HACK：动手弄通是一条线，受雇写手又有别的来路','hack → hacking / hacker / hackathon / hacky；hacksaw 回到工具，haggle 接旧变体的反复动作。',
 '技术探索、临时补丁和入侵都是现代常见义，靠上下文分开。不要为了一个统一故事，把出租车、写手、干咳全硬塞到砍木头里。',
 'hacken → hack；hack + -ing/-er/-y/-athon/saw；haggen + 反复动作词尾 → haggle；hackney 截短是另线。',
 [['技术探索、参与者与方案','hack · hacking · hacker · hackathon · hacky'],['切削工具与价格争论','hacksaw · haggle']],
 'hacker 不只指入侵者；hackathon 是集中开发活动；haggle 不等于以物易物。',
 'The hacker built a prototype at the hackathon, then replaced its hacky parts.\n\n那位技术爱好者在集中开发活动中做出了原型，随后替换了其中东拼西凑的部分。','hack hacking hacker hackathon hacky hacksaw haggle')
M=[['法语 masque ← 意大利语 maschera、拉丁 masca 等','遮住脸的物件；更深来源有争议'],['具体遮盖 → 抽象掩盖、技术遮罩','掩饰感受；选择哪些画面、数据受到作用'],['相关词形','mask + -ed → masked；un- 逆转 + mask → unmask']]
W('mask','英 /mɑːsk/；美 /mæsk/','面具、口罩；掩饰；遮罩、掩码；遮盖',
 '面前挡一层，别人看不全；把表情、信息挡住也可以 mask。图像里的 mask 则像模板，规定哪里显、哪里藏或哪里允许编辑。',
 '面具义借法语 masque，接意大利语、拉丁词形，更深来源有争议。由实体遮盖扩到掩饰和技术遮罩；不能把所有旧同形网、麦芽浸泡词都按面具解释。',M,
 'wear a mask 戴面具或口罩，mask disappointment 掩饰失望，an image mask 图像遮罩，a bit mask 位掩码。位掩码以位模式选择、控制对应位，不是给数字画一张脸。',
 'wear a mask；mask disappointment；an image mask；a bit mask。',
 'mask 可以遮身份，也可用于防护；不是每个 mask 都为了欺骗。图像遮罩控制可见性或作用区域，也不保证原数据已被删除。',
 ('The actor removed his mask after the performance.','演员在演出后摘下了面具。'),('She smiled to mask her disappointment.','她用微笑掩饰失望。'),sources=['https://en.wiktionary.org/wiki/mask#English','https://www.etymonline.com/word/mask'])
W('masked','英 /mɑːskt/；美 /mæskt/','戴面具、口罩的；被掩盖、隐藏的',
 '人脸前有东西挡着，是 masked；问题被表面好成绩遮住，也可以说 masked。要看遮的是脸、事实还是技术处理的某部分。',
 'mask + -ed，过去分词或相应形容词。词尾在 /sk/ 后读 /t/，通常一个音节，不额外读 /ɪd/。',M[:2]+[['mask + -ed → masked','已遮盖的、戴面具的，或被遮蔽的']],
 'a masked performer 戴面具的表演者，masked data 经掩蔽处理的数据，a problem masked by success 被成功掩盖的问题。',
 'a masked performer；masked data；masked by。',
 'masked 说呈现、处理后的状态，不自动保证信息不可恢复；与 mask 的具体防护性能也不是同一个问题。',
 ('A masked performer stepped onto the stage.','一位戴面具的表演者走上舞台。'),('The underlying problem was masked by a temporary rise in sales.','短期销量上升掩盖了潜在问题。'))
W('unmask','英 /ʌnˈmɑːsk/；美 /ʌnˈmæsk/','揭下面具；揭露、使真面目显露；解除掩蔽',
 '原来盖着，现在拿掉，于是看见原貌。既可真的摘面具，也可揭穿伪装、让隐藏的东西显现。',
 '逆转动作的 un- + mask。这里 un- 更像解除原动作，不是简单的形容词否定不戴面具的。',M[:2]+[['un- + mask → unmask','解除遮盖 → 揭露真相、身份等']],
 'unmask a fraud 揭露骗子，unmask the truth 揭开真相，unmask a character 揭下角色的面具。技术文本也可说解除相应掩蔽、屏蔽。',
 'unmask a fraud；unmask the truth；unmask a character。',
 'unmask 与 remove a mask 可在字面义交叠；抽象揭露要有上下文，不是所有让东西可见的 reveal 都必带伪装、隐瞒。',
 ('The detective finally unmasked the impostor.','侦探终于揭穿了冒名者。'),('The performer unmasked at the end of the dance.','表演者在舞蹈结束时摘下了面具。'))
R('B3183','遮住一层，再看是否解除遮盖','MASK：脸、感受、信息，都可能被挡住','mask → masked；unmask 把遮盖撤掉。',
 '实体面具是最直观的入口，抽象掩饰和技术遮罩各补清作用对象。masked 不等于原信息从世界上消失。',
 'masque → mask；接 -ed，前接逆转 un-。',
 [['遮盖、状态与揭开','mask · masked · unmask']],
 'masked 的 -ed 读 /t/；unmask 中 un- 撤销动作；技术遮罩不等于永久删除。',
 'The masked character finally unmasks.\n\n那个戴面具的角色终于摘下面具。','mask masked unmask')
Y=[['古诺尔斯语 býr → 英国许多地名中的 -by','聚落、村镇'],['Rugby 地名 → Rugby School → rugby football → rugby','运动经学校名称命名；地名自身有更早拼写、来源讨论']]
W('rugby','/ˈrʌɡbi/','英式橄榄球；相应运动',
 '不是 rug 毯子旁边放个球。这项运动用英国 Rugby School 的名字命名，校名又来自所在地 Rugby。',
 'Rugby 地名 → 学校名 → rugby football，再省称 rugby。英国地名常见 -by 联系北欧村镇，但 Rugby 更早名称及 -by、旧堡镇成分的关系有不同分析，不编成 rug + by 的现代复合词。',Y,
 'play rugby 打英式橄榄球，a rugby club 橄榄球俱乐部，rugby union、rugby league 是不同分支的名称。',
 'play rugby；a rugby club；rugby union；rugby league。',
 'rugby 与 American football 是不同运动，中文都可能被笼统说成橄榄球，英语不能直接互换。命名来自学校，不必把单人突然抱球的流行传说当全部起源定论。',
 ('She plays rugby for a local club.','她在当地一家俱乐部打英式橄榄球。'),('The school has separate teams for rugby and football.','学校分别设有英式橄榄球队和足球队。'),sources=['https://en.wiktionary.org/wiki/rugby#English','https://www.rugbyschool.co.uk/about-us/our-history'])
R('A2236','北欧聚落地名成分，及学校名称转成运动名','-BY：许多英国地名里的村镇；RUGBY 要经校名理解','býr → 地名 -by；Rugby → Rugby School → rugby football → rugby。',
 '这是历史地名成分，不是现代随手造运动名的通用词尾。Rugby 的整条历史还涉及更早地名拼写，不能只看现在字母切一刀。',
 '古诺尔斯 býr 聚落 → 地名成分 -by；学校命名的运动另经专名转普通名词。',
 [['地名、学校与运动','rugby']],
 '-by 不等于介词 by 的在旁边；rugby 也不由 rug 地毯 + by 组成。',
 'Rugby takes its name from Rugby School.\n\nrugby 这项运动以拉格比学校得名。','rugby')
D=[['古英语潜入、下潜动词路线 → 中古英语 ducken → duck','低头、潜下；旧动词部分形式由相关词重建'],['古英语 duce → duck 鸭','通常联系会潜水的鸟；duckling 是幼鸭'],['另源布料及称呼用法','荷兰 doek 布 → duck 帆布；亲昵称呼的具体来源另有讨论']]
W('duck','/dʌk/','鸭、鸭肉；迅速低头躲开；回避；厚帆布〔另源〕',
 '鸭子把头扎到水下，人在横梁前迅速低头，也有往下一缩的动作。回避问题则把这个躲开的动作借到抽象事情上。',
 '鸟名接古英语 duce，通常联系潜下、下潜的旧动词；现代 duck 动词接中古英语 ducken 等。布料 duck 则借荷兰 doek 布，不能说是鸭毛做的。',D,
 'feed the ducks 喂鸭，duck under a branch 低头从树枝下躲过，duck a question 回避问题，cotton duck 厚棉帆布。鸭的规则复数是 ducks /dʌks/。',
 'feed the ducks；duck under；duck a question；cotton duck。',
 'duck 鸟可泛指鸭，具体雌雄语境也可与 drake 雄鸭对照。a duck 在板球可指零分出局，联系 duck’s egg 鸭蛋的零形，不是球场上出现鸭子。',
 ('The ducks swam towards the bank.','鸭子游向岸边。'),('He ducked under the low branch.','他低头从低矮的树枝下躲了过去。'),sources=['https://en.wiktionary.org/wiki/duck#English','https://www.etymonline.com/word/duck'])
W('duckling','/ˈdʌklɪŋ/','小鸭、幼鸭',
 '跟在母鸭后面、小小一团的幼鸭。-ling 在这里标幼小个体，不是某种叫 ling 的鸟。',
 'duck 鸭 + -ling 幼小个体，接中古英语 dokeling、dukling 等形式。the ugly duckling 又常比喻起初不起眼、后来显出美好或潜力的人。',D[:2]+[['duck + -ling → duckling','幼鸭；丑小鸭故事形成相应比喻']],
 'a newly hatched duckling 刚孵出的小鸭，a group of ducklings 一群幼鸭，an ugly duckling 丑小鸭或相应比喻。',
 'a newly hatched duckling；a group of ducklings；an ugly duckling。',
 'duckling 说年龄，不专指某个鸭种，也不单凭词形断定雌雄；童话的丑小鸭形象和真实鸟类分类分开理解。',
 ('A line of ducklings followed their mother across the path.','一列小鸭跟着母鸭穿过小路。'),('The children drew a newly hatched duckling.','孩子们画了一只刚孵出的小鸭。'))
W('ducky','/ˈdʌki/','小鸭、玩具鸭；亲爱的〔昵称〕；好极了的〔口语，也可反讽〕',
 '洗澡玩具里的 rubber ducky 是可爱小鸭；别人说 Everything is just ducky，可能真说一切挺好，也可能语气一转是在抱怨。',
 '鸟名 duck + 小称 -y 可造小鸭。另有亲昵称呼 duck 加 -y 的分支，好极了义联系亲昵、讨喜用法；称呼和鸟名的远源关系并不确定。',D[1:]+[['duck + -y → ducky','小鸭、玩具鸭；另一称呼分支亲爱的、讨喜的']],
 'a rubber ducky 橡皮玩具鸭，just ducky 好极了〔须听语气〕。亲昵称呼 ducky 带旧式、地域或玩笑色彩。',
 'a rubber ducky；just ducky。',
 'ducky 不只表示像鸭的；口语 just ducky 可以反讽，不能遇见 good 的感觉就断定说话人满意。',
 ('A yellow rubber ducky floated in the bath.','一只黄色橡皮玩具鸭浮在浴缸里。'),('“Another delay? Just ducky,” she said with a sigh.','“又延期？可真好啊。”她叹着气说。'))
R('B2684','鸭与低头潜下的动作，另分布料和昵称','DUCK：鸟名和下潜动作相连，帆布不是鸭毛布','duck → duckling / ducky；ducks 的常规复数放在基础词里理解。',
 '让动作帮助记忆：低头避树枝、回避问题。遇见棉帆布、亲昵称呼时再分来源，不把所有同形用法都讲成鸭子的故事。',
 'duce、ducken 等 → duck；接 -ling、-y。另线荷兰 doek → 布料 duck。',
 [['鸟、幼鸟与小称','duck · duckling · ducky']],
 'duck a question 是回避；cotton duck 不是鸭毛；ducky 的称呼分支远源不定，just ducky 可能反讽。',
 'The child watched the ducklings while holding a rubber ducky.\n\n孩子拿着橡皮玩具鸭，看着那群小鸭。','duck duckling ducky')
if __name__=='__main__':save('continuation_20261030_il',ROOTS,WORDS)
