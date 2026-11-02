"""Reasonableness, rents and what resources let us afford."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
RE=[['拉丁 ratiōnābilis → 古法语 resnable → 中古英语 resonable → reasonable','合乎理性、道理；可理解、合情理'],['现代 reasonable','讲理、公道；价格不离谱；程度尚可']]
def RH(f,m):return RE[:1]+[[f,m]]
W('reasonable','/ˈriːzənəbəl/，也见 /ˈriːznəbəl/','合理、公道的；通情达理的；尚可的、不太贵的',
 '把理由、条件摆出来，多数人觉得说得过去，没有要求到离谱。说价格时常是付得不冤，而非保证全城最低。',
 '经古法语 resnable 接拉丁 ratiōnābilis，现代对应 reason + -able。-able 在这里不只机械说可被推理，而是合乎道理的旧形容词意义。',RE,
 'a reasonable price 公道价格，a reasonable request 合理要求，a reasonable person 通情达理的人，a reasonable chance 有相当机会。',
 'a reasonable price；a reasonable request；a reasonable person；a reasonable chance。',
 'reasonable price 公道，cheap 便宜，二者不必相同；reasonable person 强调讲理，不是这个人永远判断正确。',
 ('The hotel offered a reasonable price.','旅馆给出了公道的价格。'),('It is reasonable to ask for more information.','要求提供更多信息是合理的。'))
W('reasonably','/ˈriːzənəbli/','合理地、公道地；相当地、还算',
 'reasonably priced 是价格公道；reasonably good 则往往是还不错、有一定程度，语气未必像 extremely 那么满。',
 'reasonable + -ly，对应 -ble → -bly；中古英语已有 resonably。不能拼成 reasonablely。',RH('reasonable + -ly → reasonably','合乎道理地；程度相当地'),
 'reasonably priced 定价公道，reasonably good 还不错，reasonably sure 相当确信，reasonably expect 合理地预期。',
 'reasonably priced；reasonably good；reasonably sure；reasonably expect。',
 'reasonably 作程度副词常有所保留，reasonably good 不一定是 excellent；修饰 priced 时也可强调公道，而不只是数字小。',
 ('The restaurant is reasonably priced.','这家餐馆的价格还算公道。'),('I am reasonably sure that this is the right address.','我相当确定这是正确地址。'))
W('unreasonable','/ʌnˈriːzənəbəl/','不合理的、过分的；不讲道理的',
 '要求与条件不相称，或根本不肯听合理解释，让别人觉得这也太过分了。',
 'un- 不 + reasonable；中古英语已有相应形式，早期也受拉丁否定词对应影响。现代直接按否定合理来理解。',RH('un- + reasonable → unreasonable','不合情理、过分、不讲理的'),
 'an unreasonable demand 无理要求，unreasonable costs 过高而不合理的成本，be unreasonable 不讲道理。',
 'an unreasonable demand；unreasonable costs；be unreasonable。',
 'unreasonable 不合理常带评价，不等于 illegal 违法；要求令人不喜欢，也不自动证明它无理。',
 ('Asking everyone to work all night was unreasonable.','要求所有人通宵工作很不合理。'),('She refused to accept the unreasonable demand.','她拒绝接受那个无理要求。'))
W('reasonableness','/ˈriːzənəbəlnəs/','合理性、公道；通情达理的程度',
 '不问这是什么要求，而是问这个要求到底有多讲理、是否与条件相称。',
 'reasonable + -ness，中古英语已有 resonabilnes 等形式。保留 reasonable 的词尾再加 -ness，不像 reasonably 要把 -ble 改成 -bly。',RH('reasonable + -ness → reasonableness','合理、公道这一性质'),
 'the reasonableness of a request 请求的合理性，question the reasonableness 质疑合理性，assess the reasonableness 评估是否合理。',
 'the reasonableness of；question the reasonableness；assess the reasonableness。',
 'reasonableness 是性质评价，reason 原因、理由；给出一个 reason 不保证结论就有 reasonableness。',
 ('We discussed the reasonableness of the deadline.','我们讨论了这个截止日期是否合理。'),('The review questioned the reasonableness of the extra charges.','评论质疑额外收费是否公道。'))
R('B4321','讲理、公道与程度适中','REASONABLE：理由和要求摆在一起，觉得过得去','reasonable → reasonably、reasonableness；unreasonable 加否定。',
 '价格公道不一定最便宜，还算好不一定顶级。合理性要结合条件，不是只要能说出一个理由就算合理。',
 'ratiōnābilis 经法语、中古英语 → reasonable；-ble → -bly；reasonable + -ness；un- + reasonable。',
 [['性质、方式与抽象评价','reasonable · reasonably · reasonableness'],['否定合理','unreasonable']],
 'reasonably good 语气可能有所保留；reasonable/cheap 公道与便宜；unreasonable 不自动违法；reason/reasonableness 理由与合理性。',
 'A reasonable request should be discussed reasonably.\n\n合理的请求应当得到讲道理的讨论。','reasonable reasonably reasonableness unreasonable')
RNT=[['古法语 rente、renter，相关中世纪拉丁形式 → rent〔租用词族〕','收入、应付款 → 租金、租用'],['另一路：古英语 rendan → rend，过去形式 rent 等','撕裂 → rent〔裂口、撕裂形式〕']]
W('rent','/rent/','租金；租入、出租；裂口、撕裂〔另源〕',
 '用一段时间的房子、车或工具，按约给钱，就是租用。动词从哪一边看都可成立，要用 from、to 等把双方关系说清。',
 '租金、租用经法语 rente、renter 与相关拉丁收入、交付词接入。裂口和撕裂的 rent 另接本族 rend，不是付不起租金所以把衣服撕破的词源故事。',RNT,
 'pay rent 付租金，rent a flat 租公寓，rent something from someone 向某人租入，rent something to someone 租给某人；a rent in the fabric 布上的裂口〔较书面〕。',
 'pay rent；rent a flat；rent from；rent to；for rent。',
 'rent 可租入也可出租，rent out 更明确出租；rent 租金，rental 可说租用、出租物或相关的。裂口义另源看上下文。',
 ('We rent a small flat from a local family.','我们向当地一户人家租了一套小公寓。'),('She rents her spare room to a student.','她把空余房间租给一名学生。'),('There was a small rent in the curtain.','窗帘上有一道小裂口。'),
 sources=['https://en.wiktionary.org/wiki/rent#English','https://www.etymonline.com/word/rent'])
W('rental','/ˈrentəl/','租用、租赁；出租物；租赁的',
 'car rental 可以是租车服务、租车这件事；a rental 又可以是那辆租来的车或一处出租房。',
 '现代对应 rent + -al；历史有盎格鲁法语 rental、中世纪拉丁 rentale 等名词路径，早期还说租金簿、租金收入，不能只当现代英语临时加后缀。',
 RNT[:1]+[['盎格鲁法语 rental 等 → 英语 rental','租金记录、收入 → 租赁、出租物；相关形容词']],
 'car rental 租车，rental income 租金收入，a rental property 出租物业，a holiday rental 度假出租房。',
 'car rental；rental income；a rental property；a holiday rental。',
 'rental 作名词、形容词都可，-al 不只形成形容词；rental income 收到租金的一方收入，rent payment 常是支付方付款。',
 ('The price includes car rental for three days.','价格包括三天租车费用。'),('They found a small holiday rental near the beach.','他们在海滩附近找到一处小度假出租房。'),
 sources=['https://en.wiktionary.org/wiki/rental#English','https://www.etymonline.com/word/rental'])
W('renter','英 /ˈrentə/；美 /ˈrentər/','租用者、租客',
 '常指付租金来使用房屋、物品的人，和自己持有房产的 owner 对看。',
 'rent + -er，人物名词。因为 rent 本身有租入、出租两向，历史与个别用法也可能指提供出租者；普通住房语境优先理解租客。',RNT[:1]+[['rent + -er → renter','租用的人；具体方向看语境']],
 'a long-term renter 长期租客，first-time renters 首次租房者，renters and homeowners 租客与房主。',
 'a long-term renter；first-time renters；renters and homeowners。',
 'renter 常租用者，landlord 出租房屋者；tenant 更强调占用、承租某处房屋土地的关系。不要只见 -er 就断定是收租一方。',
 ('The survey asked renters about housing costs.','调查询问了租客的住房成本。'),('The building is popular with young renters.','这栋楼很受年轻租客欢迎。'))
R('B3563','付费暂用与出租；裂口另源','RENT：给钱换一段时间的使用权，双方方向要说清','rent → rental、renter；renting 在基础词的动作变化里理解。裂口、rend 形式在 rent 内作为另源辨析。',
 'rent from 向别人租，rent to 租给别人。裂口义不是租金历史自然变来的现代比喻。',
 '法语 rente、renter 等 → rent；rental 有独立旧名词路径；rent + -er；rend 的 rent 另接本族撕裂。',
 [['租金、租用、租客','rent · rental · renter']],
 'rent/rent out 租入出租方向；rental 可名词也可形容；renter 常租客；a rent in cloth 裂口另源。',
 'The renter paid the rent for the rental flat.\n\n租客付了出租公寓的租金。','rent rental renter')
ROOTS[-1]['exclude']['renting']='rent 的规则 -ing 变化，可说租赁活动；基础词已说明租入、出租方向，不另立重复词头。'
A=[['古英语 ġeforþian → 中古英语 aforth 等 → afford','促进、完成、提供等旧义'],['现代 afford 的两条常见分支','资源足够承担；事物能够提供某种机会、景观等']]
W('afford','英 /əˈfɔːd/；美 /əˈfɔːrd/','负担得起；有余力、承受得住；提供〔较正式〕',
 '钱、时间、精力够不够把这件事做成？够，才 afford 得起。窗户、位置能给你一片好景，也可正式说它 affords a view。',
 '继承古英语 ġeforþian，旧意有推进、完成等，接 forth 向前，不是纯拉丁 ad- + 一个 ford。中古 aforth 后拼写变化成 afford，词形也曾受被当作拉丁借词的观念影响。',A,
 'can afford a car 买得起车，cannot afford to wait 不能再耗时间等，afford an opportunity 提供机会，afford a view 提供景观。常与 can、could 等连用。',
 'can afford；cannot afford to；afford an opportunity；afford a view。',
 'afford 不只经济条件：cannot afford to fail 可说失败代价承受不起；afford to do 接不定式，通常不说 afford doing 来表示有能力做。',
 ('We cannot afford to buy a new car yet.','我们现在还买不起新车。'),('The balcony affords a clear view of the river.','阳台可以清楚地望见河景。'),
 sources=['https://en.wiktionary.org/wiki/afford#English','https://www.etymonline.com/word/afford'])
W('affordable','英 /əˈfɔːdəbəl/；美 /əˈfɔːrdəbəl/','负担得起的、价格可承受的',
 '相对于某个人、群体的收入与资源，买了还承受得住。不是只看商品标价小不小。',
 'afford + -able，表示能够承担花费的。词义随 afford 负担得起分支，不是这个房子能够主动提供什么。',A+[['afford + -able → affordable','花费可被相应人群承担的']],
 'affordable housing 可负担住房，affordable prices 可承受价格，an affordable option 负担得起的选择。',
 'affordable housing；affordable prices；an affordable option。',
 'affordable 相对支付能力，cheap 价格低；对高收入者 affordable 的东西，对另一人未必 affordable。',
 ('We are looking for an affordable place to stay.','我们在找负担得起的住宿。'),('The shop offers affordable school supplies.','商店提供价格可承受的学习用品。'))
W('affordability','英 /əˌfɔːdəˈbɪləti/；美 /əˌfɔːrdəˈbɪləti/','可负担性、支付得起的程度',
 '把买得起这件事拿出来比较：价格与收入、开销放一起，到底有多少人能承受。',
 'afford + -ability，也可对应 affordable 的 -able → -ability。词尾变化形成性质名词，不是 affordable 原样直接加 ity。',A+[['affordable 对应 -ability → affordability','价格相对资源可承受的程度']],
 'housing affordability 住房可负担性，improve affordability 提升可负担性，concerns about affordability 对负担能力的担忧。',
 'housing affordability；improve affordability；concerns about affordability。',
 'affordability 付得起，availability 能否获得、是否有货；有货但贵，两个指标可能一高一低。',
 ('The report examines housing affordability in the city.','报告考察了这座城市的住房可负担性。'),('Affordability was an important factor in their decision.','能否负担是他们作决定时的重要因素。'))
R('B3581','资源是否足够承担；能提供什么','AFFORD：能拿出资源做成，或能够给出某种好处','afford → affordable → affordability 相邻。基础动词的提供义与支付能力义分开用例句看。',
 '钱不是唯一资源，时间、失败代价也可以负担不起。支付得起与有没有货不同，不按 a + ford 字面乱拆。',
 '古英语 ġeforþian 经中古 aforth → afford；afford + -able/-ability；-able → -ability。',
 [['动词、形容词与性质','afford · affordable · affordability']],
 'affordable/cheap 相对负担与低价；affordability/availability 付得起与可获得；cannot afford to fail 不是只说钱包。',
 'The lower price made the car more affordable.\n\n价格降低后，这辆车更容易负担得起了。','afford affordable affordability')
if __name__=='__main__':save('continuation_20261030_dn',ROOTS,WORDS)
