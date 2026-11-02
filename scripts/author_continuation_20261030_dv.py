"""Rough surfaces and approximate work; cheap from a good bargain."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
RUF=[['古英语 rūh、rūg → 中古英语 rough 等 → rough','粗糙、多毛、不平整等'],['现代形象扩展','摸着不平 → 动作粗暴、经历艰难；未经精修 → 大概、粗略']]
W('rough','/rʌf/','粗糙的、崎岖的；粗暴的；艰难的；粗略的',
 '手摸上去不顺，路走起来不顺，日子过起来也不顺；写作还没打磨光滑，就可以是 rough draft 草稿。',
 '继承古英语 rūh、rūg，经中古英语多种拼写到 rough。原来粗糙、多毛等形象扩展到动作、天气、经历与未精修的估计；现代 gh 在这里读 /f/。',RUF,
 'a rough surface 粗糙表面，rough weather 恶劣天气，a rough time 艰难时期，a rough estimate 粗略估计，sleep rough 露宿〔英式〕。',
 'a rough surface；a rough time；a rough estimate；a rough draft。',
 'rough estimate 是大概估计，不等于故意错误；rough/smooth 粗糙与光滑，rough/gentle 粗暴与温和，反义由场景决定。',
 ('The wood still feels rough.','木头摸起来还很粗糙。'),('She gave us a rough estimate of the cost.','她给了我们一个大概的费用估计。'),('He had a rough week at work.','他工作上经历了艰难的一周。'))
W('roughly','/ˈrʌfli/','粗暴地、粗糙地；大约、粗略地',
 '处理人或物时不轻柔，可以是 roughly；估计只划个大致范围，也叫 roughly，两个义项别都翻成大约。',
 'rough + -ly，随着基础形容词分出动作粗暴与估计不精确的副词。',RUF+[['rough + -ly → roughly','粗暴地；以大致而非精确方式']],
 'roughly ten people 大约十人，roughly speaking 大体说来，handle roughly 粗暴处理，roughly equal 大致相等。',
 'roughly ten；roughly speaking；handle roughly；roughly equal。',
 'roughly 用作大约时接近 approximately；handle roughly 却说处理方式粗暴，不能套成大约处理。',
 ('The walk takes roughly an hour.','这段路走完大约需要一小时。'),('The parcel had been handled roughly.','包裹曾被粗暴搬运。'))
W('roughshod','英 /ˈrʌfʃɒd/；美 /ˈrʌfʃɑːd/','装有凸钉等防滑蹄铁的〔原义〕；蛮横践踏、不顾他人的〔习语〕',
 '马蹄铁留着凸点，踩过更有抓地力；借到人身上，ride roughshod over 就像不管别人感受、权利，一路强压过去。',
 'rough + shod；shod 是 shoe 给穿鞋、钉蹄铁的过去分词。原来可说马钉了带凸钉、防滑点的蹄铁，后有强横压过的比喻。不是 rough + 英语单词 shot。',
 RUF[:1]+[['rough + shod〔shoe 的分词〕→ roughshod','防滑蹄铁 → 比喻无视、强压他人']],
 'ride roughshod over someone’s wishes 不顾某人的意愿，ride roughshod over objections 蛮横无视反对。现代先记这一整组搭配。',
 'ride roughshod over；ride roughshod over objections；ride roughshod over rights。',
 'roughshod 常随 ride…over，批评强势无视；ride smoothly 骑得平稳谈动作，不能只凭粗糙与平滑互换习语。',
 ('The manager rode roughshod over the team’s objections.','经理蛮横地无视了团队的反对。'),('The review accused the plan of riding roughshod over local wishes.','评论批评该计划强行无视当地人的意愿。'),
 sources=['https://en.wiktionary.org/wiki/roughshod#English','https://www.etymonline.com/word/roughshod'])
R('B3099','粗糙、不顺与未经精修的大概','ROUGH：表面没磨平，后来也说行动、日子和估计不顺不精','rough → roughly；roughshod 保留蹄铁与蛮横践踏的旧形象。',
 'roughly 大约和粗暴地要靠修饰对象判断；roughshod 的 shod 是 shoe 的分词，不是枪声 shot。',
 'rūh、rūg → rough；rough + -ly；rough + shod → roughshod。',
 [['性质与方式、估计','rough · roughly'],['蹄铁到强压的习语','roughshod']],
 'rough draft 草稿非坏文章定论；roughly an hour 大约，handled roughly 粗暴；ride roughshod over 不顾强压。',
 'The rough draft was roughly five pages long.\n\n草稿大约五页长。','rough roughly roughshod')
CH=[['古英语 cēap → 中古英语 chep 等','贸易、买卖、价钱'],['good cheap 等旧短语 → cheap〔形容词〕','划算的买卖 → 价格低'],['现代评价分支','价低 → 有时也暗示低劣、吝啬或不体面']]
def CHP(f,m):return CH[:2]+[[f,m]]
W('cheap','/tʃiːp/','便宜的；廉价低劣的；小气的〔口语，批评〕',
 '钱花得少，可以是优点；若上下文批评用料、格调，就变成廉价感。说人 cheap，有时是小气，不是给人的标价。',
 '从旧买卖、价钱名词 cēap 的词族，经 good cheap 划算买卖等说法发展出低价形容词。现代 cheap 并非从一开始就只含质量差。',CH,
 'cheap tickets 便宜票，cheap plastic 廉价塑料，on the cheap 尽量省钱地，a cheap shot 卑鄙攻击、暗箭〔习语〕。',
 'cheap tickets；cheap materials；on the cheap；a cheap shot。',
 'cheap 低价可以中性，inexpensive 更少暗示低劣；affordable 与支付能力相对，cheap 与价低相关，cheapskate 则批评人吝啬。',
 ('We found cheap train tickets online.','我们在网上找到了便宜火车票。'),('The handle was made of cheap plastic.','把手用的是廉价塑料。'))
W('cheaply','/ˈtʃiːpli/','廉价地、花钱少地；粗劣地',
 '买得便宜、做得省钱，可以只是成本低；cheaply made 若在批评成品，也常指做得粗糙低劣。',
 'cheap + -ly，副词同时承接低成本与低质量的不同评价。',CHP('cheap + -ly → cheaply','成本少地；有时强调粗劣'),
 'buy cheaply 低价买，travel cheaply 省钱旅行，cheaply made 制作廉价、粗劣的。',
 'buy cheaply；travel cheaply；cheaply made。',
 'cheaply 不自动低质，cheaply made 常带批评；a cheap hotel 形容词，stay cheaply 副词，不混词性。',
 ('You can travel quite cheaply outside the busy season.','避开旺季，旅行可以省不少钱。'),('The toy looked cheaply made.','玩具看起来做得很粗劣。'))
W('cheapness','/ˈtʃiːpnəs/','便宜、低价；廉价感、低劣',
 '把价钱低或格调低作为一个性质来谈。the cheapness of the tickets 是票便宜，不一定说票本身印得烂。',
 'cheap + -ness，性质名词随语境分低价格与低质量感。',CHP('cheap + -ness → cheapness','价格低的性质；廉价、粗劣感'),
 'the cheapness of the tickets 票价便宜，cheapness of materials 材料廉价、低劣，a sense of cheapness 廉价感。',
 'the cheapness of；cheapness of materials；a sense of cheapness。',
 'cheapness 低价、廉价感，affordability 可负担程度；同一个很便宜的物件，对某人仍可能买不起。',
 ('The cheapness of the tickets attracted students.','票价便宜，吸引了学生。'),('The reviewer criticized the cheapness of the materials.','评论者批评了材料的廉价低劣。'))
W('cheapen','/ˈtʃiːpən/','使便宜；贬低、使显得不值钱',
 '可以让价格下降，也可把本来值得尊重、珍惜的事物说得掉价，让它显得廉价。',
 'cheap + -en，使变得便宜、低廉。比喻多接价值、尊重下降，不必真贴上更低的价签。',CHP('cheap + -en → cheapen','使价格、价值或格调降低'),
 'cheapen a product 降低产品价或价值，cheapen an achievement 贬低成就，cheapen the experience 让体验显得廉价。',
 'cheapen an achievement；cheapen the experience；cheapen the effect。',
 'cheapen 常有贬值、损格调的批评，discount 明确说价格折扣；给出优惠未必 cheapen 产品价值。',
 ('The joke cheapened a serious discussion.','那个笑话拉低了严肃讨论的格调。'),('The critic felt that the ending cheapened the whole story.','评论者觉得结尾让整个故事显得掉价。'))
W('cheapskate','/ˈtʃiːpskeɪt/','吝啬鬼、小气鬼〔口语，贬义〕',
 '该正常花点钱也舍不得，别人觉得他抠过头；省钱本身不是问题，称呼是在批评这种作派。',
 'cheap + 后项 skate、skite 一类俚语人物称呼，具体来源分析不同。不是一个只买便宜溜冰鞋的人，也不从海里的鳐鱼直接推吝啬。',CHP('cheap + skate/skite 类俚语人物词 → cheapskate','过度小气的贬义人物称呼；后项深源不定'),
 'Don’t be a cheapskate 别这么小气，call someone a cheapskate 叫某人吝啬鬼。可玩笑也可侮辱，取决于关系语气。',
 'be a cheapskate；call someone a cheapskate；Don’t be a cheapskate。',
 'cheapskate 贬义，frugal 节俭常正面；会找便宜货不自动等于待人小气。',
 ('He called himself a cheapskate and refused to pay for delivery.','他自称是个小气鬼，不肯付运费。'),('Being careful with money does not make someone a cheapskate.','花钱谨慎不等于一个人就是吝啬鬼。'),
 sources=['https://en.wiktionary.org/wiki/cheapskate#English','https://www.etymonline.com/word/cheapskate'])
R('B2935','价低与低劣感；省钱和吝啬要分开','CHEAP：先是划算买卖，后来有时带“掉价”的评价','cheap → cheaply、cheapness、cheapen；cheapskate 命名被批评过于小气的人。',
 '低价可以是好事，廉价感、吝啬则是评价。看对象和语气，不能把所有 cheap 一概译成质量差。',
 'cēap 买卖、价钱 → good cheap 划算 → cheap；cheap + -ly/-ness/-en；cheapskate 后项俚语来源不定。',
 [['低价、方式、性质与贬低','cheap · cheaply · cheapness · cheapen'],['人物贬称','cheapskate']],
 'cheap/inexpensive 低价与可能的低质暗示；cheapen 非每次 discount；frugal 节俭与 cheapskate 小气鬼；后项非溜冰故事。',
 'The tickets were cheap, so we could travel cheaply.\n\n票便宜，我们就能省钱出行。','cheap cheaply cheapness cheapen cheapskate')
if __name__=='__main__':save('continuation_20261030_dv',ROOTS,WORDS)
