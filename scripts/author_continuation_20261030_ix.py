"""Booms, fraud, survivalists and kneeling."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
B=[['响声路线：英语 boom，可能拟声','低沉而有回响的轰鸣'],['强劲增长和繁荣','boom、booming；具体比喻起点有不同解释'],['杆件路线：荷兰语 boom 树、长杆 → boom','帆杆、吊臂、话筒杆等；与轰鸣不是同一直接来源']]
W('boom','/buːm/','轰鸣、低沉巨响；激增、繁荣期；长杆、吊臂等〔另线〕',
 '雷声低沉轰隆是 boom，某行业一下子热闹增长也叫 boom；拍片时伸着话筒的 boom，却是长杆这一条来源。',
 '声音义可能拟低沉回响，增长义通常联系突然强劲扩张，也有其他历史分析。杆件义借荷兰语 boom 树、杆，不能说话筒杆因为总是轰响才得名。',B,
 'a loud boom 巨响，a housing boom 住房市场繁荣期，business is booming 生意兴隆，a microphone boom 话筒吊杆，a crane boom 起重机吊臂。',
 'a loud boom；a housing boom；business is booming；a microphone boom。',
 'boom 增长、繁荣不意味着一定长久；boom 与 bust 常说兴衰周期。吊臂义主要看杆件，不按爆炸理解。',
 ('A deep boom echoed across the valley.','低沉的轰鸣在山谷中回响。'),('The town experienced a tourism boom.','小镇经历了一阵旅游业繁荣。'),('The microphone was mounted on a boom.','话筒装在吊杆上。'),sources=['https://en.wiktionary.org/wiki/boom#English','https://www.etymonline.com/word/boom'])
W('booming','/ˈbuːmɪŋ/','低沉洪亮的；蓬勃发展的、兴旺的',
 'booming voice 是声音又深又响，booming business 是生意很兴旺。它们都有强劲的感觉，具体强在音量还是增长要看后面的名词。',
 'boom + -ing，动作形式和相应形容词。响声、增长跟随 boom 的各自用法，不把所有 booming 都译成正在爆炸。',B[:2]+[['boom + -ing → booming','声音洪亮有回响；事业、市场等强劲增长']],
 'a booming voice 洪亮的嗓音，a booming industry 蓬勃发展的行业，a booming business 兴旺生意。',
 'a booming voice；a booming industry；a booming business。',
 'booming 不保证利润、规模、长期表现每项都好；它是就声音或活动增长作描述。boom 杆件义不是这里一律使用的核心。',
 ('His booming voice filled the hall.','他洪亮的声音响彻大厅。'),('The city had a booming film industry.','这座城市的电影产业曾蓬勃发展。'))
W('boomer','英 /ˈbuːmə/；美 /ˈbuːmər/','婴儿潮一代成员〔常为 baby boomer 缩称〕；发出轰响的东西等',
 'baby boom 是出生人数明显增加的时期，baby boomer 是在这阵出生潮中出生的人。网络里 boomer 又可能被随意拿来嘲笑老派观念，不一定严格核对出生年份。',
 '一条是 boom + -er 的发声者等；常见世代义是 baby boomer 缩短。baby boom 的 boom 指出生数量激增，不是婴儿声音特别大。',B[:2]+[['baby boom → baby boomer → boomer','出生高峰 → 出生于相应世代的人 → 缩称'],['现代网络评价用法','也可能宽泛指观念老派的人，常有揶揄']],
 'the boomer generation 婴儿潮一代，baby boomers 婴儿潮世代成员。美国讨论通常指 1946—1964 年出生者，其他地区划分须看语境。',
 'baby boomers；the boomer generation。',
 'boomer 世代名不等于任何老年人的中性统称，也不能据出生年份判断每个人会不会用技术。boomerang 回旋镖又是另一借词，不按 boomer + ang 拆。',
 ('The report compares the spending habits of boomers and younger adults.','报告比较了婴儿潮一代与较年轻成年人的消费习惯。'),('She is a baby boomer, but she is comfortable with new technology.','她属于婴儿潮一代，却很熟悉新技术。'),sources=['https://en.wiktionary.org/wiki/boomer#English','https://www.census.gov/newsroom/press-releases/2025/birth-cohorts-geographic-mobility-report.html'])
W('kaboom','/kəˈbuːm/','轰隆！砰！〔夸张拟声〕；一声爆响',
 '漫画里一大团冲击旁写 KABOOM，像中文把砰、轰隆写得特别大。它首先模拟声音，也能戏剧化说事情突然炸开、发生。',
 '表达性前缀 ka- + boom 轰鸣，前面多一拍以加强效果；不是拉丁 ka 表示爆炸。',B[:1]+[['ka- + boom → kaboom','加强、铺垫一拍的爆响拟声']],
 'go kaboom 砰地爆响〔随意〕，a cartoon kaboom 漫画里的轰隆声，Kaboom! 轰隆！',
 'go kaboom；Kaboom!。',
 'kaboom 适合拟声、漫画或轻松叙述，正式报告通常用 explosion、a loud bang 等更具体表达；它不说明爆炸物或成因。',
 ('“Kaboom!” flashed across the comic panel.','漫画分格上赫然写着“轰隆！”'),('The balloon burst with a loud kaboom in the cartoon.','动画里的气球伴着夸张的一声轰响爆开了。'))
W('bumpkin','/ˈbʌmpkɪn/','乡巴佬、土包子〔贬义〕；短帆杆〔航海另用〕',
 '人物义是嫌别人笨拙、没见识的贬称，常见于乡村人进城的旧故事。但住在农村本身并不能证明一个人无知。',
 '通常联系荷兰语 boom 树、杆的小称形式 boomken、bommekijn 等，具体历史形式、贬称转义有不同说明；不按英语 bump 碰撞 + kin 亲属解释。航海短杆义又接较字面的路线。',B[2:]+[['荷兰语树、杆的小称形式 → bumpkin/bumkin','小木杆、短杆等；人物用法历史带贬低'],['英语固定人物义','笨拙、没见识的乡下人这一刻板称呼']],
 'a country bumpkin 乡巴佬，dismiss someone as a bumpkin 把某人轻视为土包子。现代中性描述农村背景通常直接用来自何处等具体说法。',
 'a country bumpkin；dismiss someone as a bumpkin。',
 'bumpkin 是评价标签，不是农村职业名称；和 boom 的关系主要看荷兰语杆件线，不能拿轰隆声编成吓傻的人。',
 ('The novel challenges the stereotype of the country bumpkin.','小说挑战了把乡村人看成土包子的刻板印象。'),('He disliked being treated as a bumpkin because of his accent.','他不喜欢别人因他的口音就把他当土包子。'),sources=['https://en.wiktionary.org/wiki/bumpkin#English','https://www.etymonline.com/word/bumpkin'])
R('B2643','轰鸣、强劲增长与荷兰语杆件的不同来源','BOOM：听声音、看增长；杆件另有来路','boom → booming / boomer / kaboom；bumpkin 联系荷兰语树、杆的小称一线。',
 '不要把一切都画成爆炸：话筒 boom 是杆，baby boom 是出生数量激增，bumpkin 的旧形象也从另一历史线来。',
 '拟声 boom；增长义比喻形成；荷兰 boom → 杆件 boom；boomken 等 → bumpkin；ka- 加强，-ing、-er 形成相应词。',
 [['响声与强劲增长','boom · booming · kaboom'],['世代与另一来源的人物词','boomer · bumpkin']],
 'boomer 世代名不等于所有老年人；bumpkin 有贬义；吊杆 boom 不是轰响才得名。',
 'The boomer spoke in a booming voice while a microphone boom hung overhead.\n\n那位婴儿潮世代成员洪亮地说着话，头顶悬着话筒吊杆。','boom booming kaboom boomer bumpkin')
F=[['拉丁 fraus，词干 fraud- → 法语 fraude → 英语 fraud','欺骗、损害等历史含义'],['英语名词分化','欺诈行为；虚假的东西或冒名、欺骗的人'],['fraud + -ster → fraudster','实施欺诈的人']]
W('fraud','英 /frɔːd/；美 /frɔːd/，部分口音 /frɑːd/','欺诈、诈骗；欺骗行为；骗子、冒牌货',
 '表面让你相信一回事，背后靠这层假象取得不应得的好处。说 He’s a fraud，又把行为评价落到了人：他那套身份、能力或说辞是假的。',
 '经法语 fraude 接拉丁 fraus 的 fraud- 词干。通常不可数说欺诈活动，可数 a fraud 则可指某个骗局、冒牌货或骗子。',F[:2],
 'insurance fraud 保险欺诈，identity fraud 身份欺诈，a suspected fraud 涉嫌骗局，feel like a fraud 觉得自己名不副实。',
 'insurance fraud；identity fraud；a fraud；feel like a fraud。',
 '普通词义常突出欺骗，不是所有错误、失约都叫 fraud。feel like a fraud 可是自我怀疑，并不自动承认实施诈骗；法律文本的具体认定又看其规则。',
 ('The report uncovered evidence of fraud.','报告揭露了欺诈的证据。'),('Despite her success, she sometimes felt like a fraud.','尽管成功，她有时仍觉得自己名不副实。'),sources=['https://en.wiktionary.org/wiki/fraud#English','https://www.law.cornell.edu/wex/fraud'])
W('fraudster','英 /ˈfrɔːdstə/；美 /ˈfrɔːdstər/，部分口音 /ˈfrɑːd-/','诈骗者、骗子',
 'fraud 是骗局、欺诈，fraudster 明确指做这种事的人。词尾把行为和实施者分开。',
 'fraud + 人物后缀 -ster，现代不限定性别；不能凭这段拼写把人当作一个 star 明星。',F[:2]+[['fraud + -ster → fraudster','实施欺诈的人']],
 'an online fraudster 网络诈骗者，a convicted fraudster 已被定罪的诈骗者，a fraudster posing as a supplier 冒充供应商的骗子。',
 'an online fraudster；a convicted fraudster。',
 'fraudster 是人，fraud 是行为或可数骗局、骗子的更宽用法；suspected fraudster 表怀疑身份，措辞不等于已经证实。',
 ('The novel follows a fraudster who invents a false identity.','小说讲述一个编造虚假身份的骗子。'),('The documentary explains how the fraudster deceived his victims.','纪录片解释了那名诈骗者如何欺骗受害者。'))
R('B4163','靠虚假取得好处，及实施者','FRAUD：表象骗人；FRAUDSTER：实施的人','fraud 行为、骗局或冒牌者 → fraudster 人物称呼。',
 '先看可数性和句子：evidence of fraud 说欺诈证据，a fraud 可能说骗子、骗局，feel like a fraud 又可只是觉得自己不配。',
 'fraus / fraud- → fraude → fraud；fraud + -ster。',
 [['欺诈与实施者','fraud · fraudster']],
 'fraud 不等于任何出错；feel like a fraud 不必是自认诈骗；suspected 不等于已证实。',
 'The article describes evidence of fraud linked to an alleged fraudster.\n\n文章描述了与一名被指控的诈骗者有关的欺诈证据。','fraud fraudster')
W('survivalist','英 /səˈvaɪvəlɪst/；美 /sərˈvaɪvəlɪst/','生存准备主义者；积极为未来紧急情况准备的人',
 '不只说自己想活下来，而是把可能出现的中断、紧急情况当作需要提前准备的生活重点。常见于应急自给、野外生存等讨论。',
 'survival 生存 + -ist，从事者、相应主张者。不是 survivor 幸存者再加几个字母：survivor 侧重已经活过某次经历的人。',
 [['survive → survival','活下来 → 生存状态或过程'],['survival + -ist → survivalist','主动为未来生存挑战作准备的人']],
 'a survivalist community 生存准备者社群，a survivalist character 有生存准备取向的角色，a documentary about survivalists 关于这类人群的纪录片。',
 'a survivalist community；a documentary about survivalists。',
 'survivalist 不等于任何事故幸存者，也不单凭词义断定一个人支持哪种政治立场。survival 是事，survivor、survivalist 说不同身份重点。',
 ('The documentary follows a community of survivalists.','纪录片追踪一个生存准备者社群。'),('The novel’s survivalist character expects a long disruption of normal services.','小说中那位生存准备者角色预想日常服务会长期中断。'))
R('B4565','活下来这一目标，及提前准备的人','SURVIVAL：活下来；SURVIVALIST：提前围绕生存作准备的人','survival → survivalist；survivor 幸存者另按经历理解。',
 '想活下去是一件事，把可能的紧急情况作为重点提前准备又是一种取向。词尾帮助区分身份，不把所有幸存者都归成同一群体。',
 'survive → survival；survival + -ist。',
 [['生存目标与准备者','survival · survivalist']],
 'survivalist 不是 survivor 的随意长拼写；词本身不规定统一政治立场。',
 'The survivalist discusses survival as a problem to prepare for.\n\n那位生存准备者把生存当成需要预先准备的问题来讨论。','survival survivalist')
K=[['古英语 cnēow → 中古英语 kne → knee','膝，开头的旧辅音后来不再发音'],['相关古英语 cnēowlian → kneel','以膝着地、跪'],['部位、动作与组合','kneecap 膝盖骨；knee 也可作以膝碰撞的动词']]
W('knee','/niː/','膝、膝部；衣裤膝部；用膝碰撞',
 '大腿与小腿之间弯曲的部位。裤子在这里磨破，便可说 the knee of the trousers；物件有类似弯角也能借这个形状命名。',
 '接古英语 cnēow，经中古英语 kne → knee。现代常见读音开头 k 不发音；不是 knee 少读一个音就变成 need 需要。',K,
 'bend your knees 屈膝，on one knee 单膝跪地，a hole at the knee 裤子膝部破洞，learn at someone’s knee 从小在某人身边学。',
 'bend your knees；on one knee；a hole at the knee。',
 'knee /niː/，复数 knees /niːz/。动物身体里俗称 knee 的部位不一定都和人膝关节严格同源，普通命名与精细解剖分开。',
 ('He rested the book on his knees.','他把书放在膝上。'),('There was a small hole at the knee of her jeans.','她牛仔裤膝部有个小洞。'),sources=['https://en.wiktionary.org/wiki/knee#English','https://www.etymonline.com/word/knee'])
W('kneel','/niːl/','跪、跪下；车辆降低车身方便上下客〔专门用法〕',
 '膝盖弯下、靠膝着地，是 kneel。常见日常场景是跪下来修东西、与孩子平视，并不每次都在表示臣服。',
 '接古英语 cnēowlian，经中古英语 knelen 延续，历史与 knee 同族。现代可按膝部词加旧动作词尾理解，不拿 -le 在所有词里统一译成小。',K[:2]+[['现代变化','kneel → knelt / kneeled；过去式、分词两种形式均见']],
 'kneel down 跪下，kneel beside someone 跪在某人旁，kneel on one knee 单膝跪；knelt /nelt/、kneeled /niːld/。',
 'kneel down；kneel beside；knelt；kneeled。',
 'kneel 与 bend the knees 屈膝不总相同：站着屈膝未必跪地。kneeling bus 可指降低车身让乘客更易登车的公交车，是拟人式技术用法。',
 ('She knelt beside the child to tie his shoelaces.','她跪在孩子身旁，帮他系鞋带。'),('He kneeled on the mat to examine the model.','他跪在垫子上查看模型。'))
R('B2771','膝部、以膝着地与相应部件','KNEE：开头 k 不读；KNEEL：靠膝着地','knee → kneel；kneecap 按盖在膝前的骨性部位命名。',
 '先区分站着屈膝和跪地。拼写保存旧开头，现代 knee、kneel、kneecap 都不能逐字读出 k。',
 'cnēow → knee；cnēowlian → kneel；knee + cap → kneecap；kneel 的过去式、分词 knelt / kneeled。',
 [['部位、动作与骨性名称','knee · kneel · kneecap']],
 'knee 开头 k 静音；knees 末尾 /z/；knelt 与 kneeled 都可用；kneeling 不只宗教或臣服。',
 'She knelt on one knee beside the model of a kneecap.\n\n她在膝盖骨模型旁单膝跪下。','knee kneel kneecap')
if __name__=='__main__':save('continuation_20261030_ix',ROOTS,WORDS)
