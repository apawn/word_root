"""Fare, jump, massively and reaction: everyday meanings without forced splits."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
F=[['古英语 faran〔行进〕，fær、faru〔行程等〕→ 中古英语 fare','行进、路程；相关名词形式汇合'],['英语 fare 的分支','旅途、运送 → 乘车费；也有食物、生活供给的旧分支；动词进展如何']]
W('fare','英 /feə/；美 /fer/','车船费、票价；饭菜、供应内容；进展、过得如何',
 '名词可说这趟车要付多少钱；饭菜义则是端给人吃的东西。动词 How did you fare? 问的是这回过得、表现得怎么样。',
 '旧行进动词 faran 与行程名词 fær、faru 经中古英语接现代形式。车费由运送、乘坐发展；食物有较早的供给、生活资料分支，不编成先买票再吃饭的必然故事。',F,
 'a bus fare 公交车费，pay the fare 付车费，traditional fare 传统饭菜，fare well 表现、过得好，How did you fare? 你这回怎么样？',
 'a bus fare；pay the fare；traditional fare；fare well。',
 'fare 票价金额，ticket 票；fair 公平的发音相同但拼写、来源不同。farewell 与 fare well 的祝愿相关，fare 动词不自动是支付票价。',
 ('The bus fare has increased again.','公交票价又涨了。'),('How did you fare in the interview?','你面试表现得怎么样？'),('The café serves simple local fare.','这家咖啡馆供应简单的本地饭菜。'))
W('thoroughfare','英 /ˈθʌrəfeə/；美 /ˈθɜːrəfer/','通行道路、街道；交通干道',
 '能从这里穿过去到别处的路，常指车辆、人来往通行的街道，而非封死不通的角落。',
 '中古英语 thurghfare，前项是 through 的旧形式，与 fare 行进、通行组合；现代 thorough 常说彻底，但此词不能按彻底票价硬译。',
 F[:1]+[['thorough-〔旧 through〕+ fare → thurghfare → thoroughfare','穿行通过的路']],
 'a busy thoroughfare 繁忙交通干道，a major thoroughfare 主要干道，No thoroughfare 禁止通行、此路不通的标示。',
 'a busy thoroughfare；a major thoroughfare；No thoroughfare。',
 'thoroughfare 通行路，dead end 死胡同；No thoroughfare 在具体标牌可限制穿行，不只说明正在收通行费。',
 ('The hotel stands on a busy thoroughfare.','旅馆位于一条繁忙的交通干道上。'),('A sign at the gate read “No thoroughfare.”','门口的牌子写着“禁止通行”。'))
R('B3398','行进、行程、票价与生活状态','FARE：原来问如何行进，后来也问这趟花多少、事情过得怎样','fare → airfare；thoroughfare 说通行道路，farewell 祝一路顺遂，welfare、warfare 保留不同的旧组合。',
 'fare 的食物义有较早的供给背景，不从现代车票随意推出。thoroughfare 里的前项保留 through 的旧形。',
 '古英语 faran、fær、faru → fare；air + fare；thorough- + fare；well/war + fare；fare well → farewell。',
 [['基础与费用','fare · airfare'],['道路与祝愿','thoroughfare · farewell'],['生活与战争旧组合','welfare · warfare']],
 'fare 价钱、ticket 票；fare/fair 同音不同词；thoroughfare 非彻底票价，warfare 不等于交战税。',
 'We paid the fare and travelled along the city’s main thoroughfare.\n\n我们付了车费，沿城市的主干道行进。','fare airfare thoroughfare farewell welfare warfare')
J=[['英语 jump 的跳跃、蹦起用法','来源不完全确定，拟声及其他语言联系有不同分析'],['现代动作比喻','一下离地 → 突然变动、越过步骤、猛地受惊']]
W('jump','/dʒʌmp/','跳、跳跃；猛增、骤变；突然受惊',
 '脚用力把身体送离地面，中间不是一步步走过去。价格、思路突然跨过一大截，也借 jump 来说。',
 '早期英语已有相应形式，深源存在拟声、日耳曼语或其他语言联系的不同分析。先从可靠的跳跃动作与现代比喻学，不把某条猜想写成定论。',J,
 'jump over a fence 跳过围栏，jump to conclusions 仓促下结论，prices jump 价格猛涨，jump at a chance 欣然抓住机会，jump in 插话、加入。',
 'jump over；jump to conclusions；prices jump；jump at a chance；jump in。',
 'jump 常强调突然离开原位置、状态，rise 上升不一定突然；jump to conclusions 不是推理很快的中性赞美，常批评证据未足就下判断。',
 ('The dog jumped over the fence.','狗跳过了围栏。'),('Do not jump to conclusions before hearing her explanation.','听她解释前，别急着下结论。'))
W('jumper','英 /ˈdʒʌmpə/；美 /ˈdʒʌmpər/','跳跃者；毛衣〔英式〕；无袖套裙〔美式〕；跳线',
 '运动里可以是跳的人；英式穿衣语境却常是一件毛衣。不能把买毛衣误听成去买一个跳高者。',
 '跳跃者为 jump + -er；衣物义接较早 jump 短上衣等词，可能涉及法语 jupe 等，深源不定，不能硬说因为穿着跳得高。电路跳线则借跨接两点的功能。',
 J[:1]+[['jump + -er → jumper〔跳跃者等〕','跳跃者、跨接物'],['旧 jump〔衣物〕→ jumper〔衣物〕，深源不定','毛衣、套裙等地区用法']],
 'a high jumper 跳高运动员，a woollen jumper 羊毛毛衣，a jumper wire 跳线。美式 a jumper 可说穿在上衣外的无袖套裙。',
 'a high jumper；a woollen jumper；a jumper wire。',
 '英式 jumper 常近 sweater，美式衣物义常不同；jumping 动作不能解释每件 jumper 衣服的历史。',
 ('She wore a warm woollen jumper.','她穿着一件暖和的羊毛毛衣。'),('He was the best high jumper on the team.','他是队里最好的跳高运动员。'),
 sources=['https://en.wiktionary.org/wiki/jumper#English','https://www.etymonline.com/word/jumper'])
W('jumpy','/ˈdʒʌmpi/','神经紧张、容易受惊的；跳动不稳的',
 '一点声音就让人猛地一缩，像随时会跳起来；也可以说画面、动作不平稳，一格一格地跳。',
 'jump + -y，表示带跳动、易惊跳特点的形容词。y 不表示过去发生了一次跳。',J+[['jump + -y → jumpy','易惊跳、紧张；跳动不稳']],
 'feel jumpy 感到紧张，a bit jumpy 有点神经紧绷，jumpy footage 跳动不稳的影像。',
 'feel jumpy；a bit jumpy；jumpy footage。',
 'jumpy 常暂时紧张、易惊，不自动是医学诊断；excited 高兴兴奋不一定 jumpy，jumping 则是跳的动作。',
 ('The loud noises made the cat jumpy.','那些巨响让猫变得很容易受惊。'),('I felt jumpy while waiting for the results.','等结果时，我感到神经紧绷。'))
W('jumble','/ˈdʒʌmbəl/','混杂成一团；乱堆、杂乱的一堆',
 '东西本来可以分门别类，碰来碰去后都挤成一堆；思绪、声音也能乱作一团。',
 '早期英语 jumbelen、jumble 等有混乱移动义；有与 jump 的反复动作形式相连的分析，也有拟声、仿 tumble 等形式的解释，不能把现代 jump + -le 当唯一确定路线。',
 [['早期英语 jumble、jumbelen 等','杂乱移动、搅混；更早路线有不同分析'],['动词 jumble → 名词 jumble','混在一起 → 杂乱混合物']],
 'a jumble of wires 乱作一团的电线，jumble things together 把东西混在一起，jumbled thoughts 杂乱思绪，a jumble sale 旧物义卖〔英式〕。',
 'a jumble of；jumble together；jumbled thoughts；a jumble sale。',
 'jumble 强调混乱，mix 只是混合未必乱；jump 跳可帮联想乱动，但历史联系不作为已证实的直接变形。',
 ('The drawer was a jumble of cables and old keys.','抽屉里电缆和旧钥匙乱成一团。'),('Do not jumble the receipts together.','别把收据全混在一起。'),
 sources=['https://en.wiktionary.org/wiki/jumble#English','https://www.etymonline.com/word/jumble'])
R('B2686','跳起、突变、易惊与混乱移动','JUMP：从原位置一下跨出去，动作也能借给价格和思路','jump → jumper、jumpy；jumpsuit 衣物名复用；jumble 保留混动的形象与不确定历史。',
 'jumper 衣服有旧衣物词路径，不编成毛衣适合跳跃；jumble 与 jump 的联系有不同分析，直观联想不冒充确定词源。',
 'jump 深源不定；jump + -er/-y；jump + suit；jumper 衣物接旧 jump；jumble 早期混动词形另说明。',
 [['动作、人物与紧张状态','jump · jumper · jumpy'],['衣物与混动旁支','jumpsuit · jumble']],
 'jump/rise 突然与上升；jumpy/excited 易惊与兴奋；jumper 毛衣非跳跃者义直接推；jumble 不一定现代 jump 加后缀。',
 'The jumpy cat jumped over a jumble of cables.\n\n那只容易受惊的猫跳过了一团乱电缆。','jump jumper jumpy jumpsuit jumble')
W('massively','/ˈmæsɪvli/','非常、极大程度地；以巨大规模地',
 '把影响、差异说得很大，不一定真有一块巨大物体。massively popular 就是非常受欢迎。',
 'massive + -ly，副词接庞大、程度很强的形容词义。massive 经法语接 mass 等实体、团块词的历史，现代副词可脱离实物质量。',
 [['法语 massif 等 → massive','实体、成块的 → 庞大、强烈的'],['massive + -ly → massively','规模、程度非常大地']],
 'massively popular 非常受欢迎，massively improve 极大改善，massively multiplayer 大规模多人参与的〔游戏等〕。',
 'massively popular；massively improve；massively multiplayer。',
 'massively 强调程度或规模，massive 是形容词；massively useful 口语很有用，不说物理上重多少千克。',
 ('The festival has become massively popular.','这个节庆活动已经变得非常受欢迎。'),('The new layout massively improved the flow of people.','新布局大大改善了人流通行。'))
R('B4372','巨大的体量、程度与副词加强','MASSIVE：大到有分量，现代也能形容影响、成功和程度','massive → massively；supermassive 作为体量特别巨大的常见科学扩展另看。',
 'massively popular 说受欢迎程度，不称量人的重量。supermassive 的科学搭配保留既有解释。',
 '法语 massif → massive；massive + -ly；super- + massive。',
 [['形容与程度','massive · massively'],['更大体量','supermassive']],
 'massive 形容词，massively 副词；巨大影响不一定巨大重量。',
 'The event was a massive success and became massively popular.\n\n活动大获成功，变得非常受欢迎。','massive massively supermassive')
RE=[['法语 réaction、拉丁相关反作用构词 → reaction','对动作、刺激的回应'],['现代英语以 reaction 继续派生、复合','反应；程度过大；特定政治立场的历史支线']]
W('overreaction','英 /ˌəʊvəriˈækʃən/；美 /ˌoʊvəriˈækʃən/','反应过度',
 '事情只需要一点回应，却用了很大情绪、措施；over- 评的是反应相对于事情过了头。',
 'over- 过度 + reaction 反应，名词命名过强回应；不是接在 act 后表示在上面再次行动。',RE[:1]+[['over- + reaction → overreaction','超出合适程度的反应']],
 'an overreaction to criticism 对批评的过激反应，call it an overreaction 认为反应过度，avoid an overreaction 避免反应过度。',
 'an overreaction to；call it an overreaction；avoid an overreaction。',
 'overreaction 带程度不恰当的判断，不是所有强烈反应都过度；reaction 可以完全合理。',
 ('She later admitted that cancelling the trip was an overreaction.','她后来承认，取消旅行有些反应过度。'),('He described the response as an overreaction to a minor mistake.','他认为，对一个小错误作出这样的回应太过头了。'))
W('reactionary','英 /riˈækʃənəri/；美 /riˈækʃəneri/','反动的、主张恢复旧秩序的；持这种立场的人',
 '不只是对事情有反应，而是反对某种社会、政治变化，想把秩序拉回较早状态；常带批评色彩。',
 '借法语 réactionnaire，有法国革命后反对革命、恢复旧秩序等政治背景。现代可对应 reaction + -ary，但不是任何反应都能加后缀变成政治反动。',
 RE[:1]+[['法语 réactionnaire → reactionary','反对革命、变革等 → 主张恢复旧秩序的立场']],
 'reactionary views 反动、主张倒退的观点，a reactionary politician 反动政治人物，a reactionary 反动派。评价要结合作者立场与具体主张。',
 'reactionary views；reactionary politics；a reactionary。',
 'reactionary 不等于 reactive 反应性的；conservative 保守与 reactionary 有范围重叠，但通常后者更强调恢复旧状态，不能无条件互换。',
 ('The historian examined reactionary movements after the revolution.','历史学者研究了革命后的反动运动。'),('The reviewer criticized the novel’s reactionary view of social change.','评论者批评了小说对社会变革所持的倒退立场。'))
R('B3895','回应、反应过度与恢复旧秩序的立场','REACTION：回应某个动作，但政治词有自己的历史背景','reaction → overreaction；reactionary 以独立法语政治词路径另列。',
 '反应过强看 over-，恢复旧秩序看 reactionary 的历史语境；不是反应快的人就叫 reactionary。',
 'reaction 的反作用、回应历史；over- + reaction；法语 réactionnaire → reactionary。',
 [['反应及程度','reaction · overreaction'],['政治历史支线','reactionary']],
 'reactionary/reactive 特定政治立场与反应性的区别；overreaction 是程度评价，不是任意负面情绪。',
 'The article distinguishes a reaction from an overreaction.\n\n文章区分了正常反应与反应过度。','reaction overreaction reactionary')
if __name__=='__main__':save('continuation_20261030_dk',ROOTS,WORDS)
