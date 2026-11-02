"""Purchase, combine and guilt with the genuine historical routes preserved."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
P=[['古法语 porchacier、盎格鲁法语 purchacer 等 → 中古英语 purchasen → purchase','追求、设法取得 → 获得'],['现代 purchase 的分支','花钱获得、所购物；也有抓牢、施力的支点']]
def PH(f,m):return P[:1]+[[f,m]]
W('purchase','英 /ˈpɜːtʃəs/；美 /ˈpɜːrtʃəs/，也见末节 /ɪs/','购买；所购物、购买行为；抓牢处、施力的支点',
 '日常先是花钱把东西买来；脚在湿滑石面找不到 purchase，则是找不到能抓住、使上力的位置，不是在山上找商店。',
 '借法语旧追求、设法取得的词，结构有 pur- 向前、加强等 + chacier 追逐。取得后来专化成花钱买；支点、抓牢义有航海牵引、施力背景，不能只译购物。',P,
 'purchase tickets 购票，make a purchase 买东西，proof of purchase 购买凭证，get a purchase on 找到抓牢、施力处。',
 'purchase tickets；make a purchase；proof of purchase；get a purchase on。',
 'purchase 比 buy 正式，作名词还可说买到的物品；后半常弱读，不照单独 chase /tʃeɪs/ 读。',
 ('You can purchase tickets at the entrance.','你可以在入口购票。'),('Keep your receipt as proof of purchase.','保留收据作为购买凭证。'),('Her boots could not get a purchase on the wet rock.','她的靴子在湿岩石上找不到着力处。'),
 sources=['https://en.wiktionary.org/wiki/purchase#English','https://www.etymonline.com/word/purchase'])
W('purchaser','英 /ˈpɜːtʃəsə/；美 /ˈpɜːrtʃəsər/','购买者、买方',
 '交易里掏钱取得东西的那一方，常见于正式通知、合同、购买凭证。',
 '现代对应 purchase + -er；旧英语已有 purchasour 等从盎格鲁法语人物名借入的形式，早期取得者范围比买者更宽，不只现代临时加 -er。',PH('法语 porchaceor 等人物名 → purchasour → purchaser','取得者 → 买方、购买者'),
 'the original purchaser 原购买者，a potential purchaser 潜在买家，the purchaser of the property 房产买方。',
 'the original purchaser；a potential purchaser；the purchaser of。',
 'purchaser 买方，seller 卖方；user 使用者不一定付了钱，购买者也不一定亲自使用。',
 ('The warranty applies to the original purchaser.','保修适用于原购买者。'),('Several potential purchasers viewed the property.','几位潜在买家看了这处房产。'),
 sources=['https://en.wiktionary.org/wiki/purchaser#English','https://www.etymonline.com/word/purchase'])
W('repurchase','英 /ˌriːˈpɜːtʃəs/；美 /ˌriːˈpɜːrtʃəs/','重新购买、回购；回购行为',
 '买过的东西再买一次，或把原来卖出去的东西买回来。re- 表再次、回头，方向由交易语境决定。',
 're- 再、回 + purchase，形成再次购买、买回的动词、名词。',PH('re- + purchase → repurchase','再次购买；买回'),
 'repurchase a product 再次购买产品，repurchase shares 回购股票，a repurchase agreement 回购协议〔术语〕。',
 'repurchase a product；repurchase shares；a repurchase agreement。',
 'repurchase 再买或买回，refund 退款；收到退款不等于又买了，词义不互换。金融固定术语有专门机制，先认名称。',
 ('She liked the product enough to repurchase it.','她很喜欢这款产品，愿意再次购买。'),('The report described the company’s plan to repurchase shares.','报告描述了公司回购股票的计划。'))
W('purchasable','英 /ˈpɜːtʃəsəbəl/；美 /ˈpɜːrtʃəsəbəl/','可购买的、可以买到的',
 '不是只能看、不能买，或只能靠做任务取得，而是提供了付钱获得的途径。',
 'purchase 去 e 加 -able，形成可被购买的形容词。保留原词重音，不读成 chase 的长元音。',PH('purchase + -able → purchasable〔去 e〕','可以通过购买得到的'),
 'purchasable items 可购买物品，purchasable content 可购买内容，make something purchasable 开放某物购买。',
 'purchasable items；purchasable content；make purchasable。',
 'purchasable 有购买途径，affordable 付得起；一款很贵的商品可以买到，却未必是你能负担的。',
 ('The game lists all purchasable items in one menu.','游戏在一个菜单中列出所有可购买物品。'),('The report is freely readable but not purchasable as a printed book.','报告可免费阅读，但没有纸质书可买。'))
R('B4069','设法取得到购买；人物、再次购买与可购买','PURCHASE：把想要的东西取得，现代多用正式“买”','purchase → purchaser、purchasable；repurchase 再买、买回。基础词保留着力点的另一常见阅读义。',
 '买方、使用者不一定同一个人。能买到与付得起也不同；get a purchase on 岩面着力不涉及购物。',
 '法语 pur- + chacier 等 → purchase；purchaser 有旧法语人物词路径；purchase 去 e 加 -able；re- + purchase。',
 [['购买、买方与可购买','purchase · purchaser · purchasable'],['再次或回头买','repurchase']],
 'purchase/buy 正式与日常；purchasable/affordable 买得到与负担得起；repurchase 非 refund；purchase 抓牢义另看。',
 'The purchaser kept the receipt as proof of purchase.\n\n买方保留了收据作为购买凭证。','purchase purchaser purchasable repurchase')
CO=[['拉丁 com- + bīnī → 晚期拉丁 combīnāre → 法语 combiner → combine','一起 + 两两 → 联结、合在一起'],['名词有独立分支','combīnātiō 等 → combination；combine harvester 等缩短 → 农机 combine']]
W('combine','动词 /kəmˈbaɪn/；农机名词：英 /ˈkɒmbaɪn/、美 /ˈkɑːmbaɪn/','组合、合并；兼有；联合收割机',
 '把本来分开的东西放到一起，共同形成效果；机器把收割、脱粒等工作合在一台上，也就叫 combine。',
 '经法语接晚期拉丁 combīnāre，com- 一起 + bīnī 两两。现代可以组合多于两件，不能把旧两两含义当所有句子的硬性数量限制。农机名词由 combine harvester 等短语缩短。',CO,
 'combine A with B 把 A 与 B 结合，combine work and study 兼顾工作学习，combine to do 共同促成，a combine 联合收割机。',
 'combine A with B；combine work and study；combine to do；a combine。',
 '动词后重音、农机名词前重音；combine 合在一起不保证每项永远保持原样，mix/blend/merge 的具体差别看场景。',
 ('The course combines theory with practical work.','课程把理论和实际操作结合起来。'),('A combine moved slowly across the field.','一台联合收割机缓慢驶过田野。'),
 sources=['https://en.wiktionary.org/wiki/combine#English','https://www.etymonline.com/word/combine'])
W('combination','英 /ˌkɒmbɪˈneɪʃən/；美 /ˌkɑːmbɪˈneɪʃən/','组合、结合；组合结果；密码组合',
 '不只问怎么合，还可以说合成的这一套是什么：衣服颜色搭配、几种因素共同作用、锁的数字序列，都能叫 combination。',
 '经法语 combination 接晚期拉丁 combīnātiō，名词有独立借入路线；现代对应 combine 去 e 加 -ation，但不是一定先有英语动词才新造名词。',
 CO[:1]+[['拉丁 combīnātiō → 法语 combination → combination','结合行为；形成的一套组合']],
 'a combination of A and B 两者组合，in combination with 与某物结合，a combination lock 密码锁，the combination to the safe 保险箱密码。',
 'a combination of；in combination with；a combination lock。',
 'combination 可组合结果也可行为；锁的 combination 常数字顺序也重要，不可仅按数学组合不计顺序的专义理解所有日常用法。',
 ('The dish uses a combination of sweet and sour flavours.','这道菜把甜味与酸味结合起来。'),('She forgot the combination to the lock.','她忘了锁的密码。'))
W('recombine','/ˌriːkəmˈbaɪn/','重新组合、重新结合',
 '已有材料拆开、换一换搭配，再合成新的安排；不是重新从零造出每个材料。',
 're- 再、重新 + combine，动词表示再次结合或形成新的组合。',CO[:1]+[['re- + combine → recombine','再次或以新方式组合']],
 'recombine the parts 重新组合部件，recombine ideas 重新组合想法，recombine elements 重新结合元素。',
 'recombine the parts；recombine ideas；recombine elements。',
 'recombine 改变组合，不等于原封不动 repeat 重复；rebuild 重建可有更大范围变化。',
 ('The artist recombined familiar shapes into a new design.','艺术家把熟悉的形状重新组合成新设计。'),('The program can recombine the fragments in different orders.','程序能把片段按不同顺序重新组合。'))
W('recombination','英 /ˌriːkɒmbɪˈneɪʃən/；美 /ˌriːkɑːmbɪˈneɪʃən/','重新组合；重组〔生物、物理等〕',
 '重新合在一起这件事或形成的新组合；进入生物、物理课本后，可是特定机制的名称，不只说随便拼东西。',
 're- + combination，也与 recombine 的动作名词相对应。保留前缀和名词的分层，不把 re- 误认成 combination 内部的原生字母。',
 CO[:1]+[['re- + combination → recombination','重新结合的过程；再有各学科专义']],
 'genetic recombination 遗传重组，electron-hole recombination 电子空穴复合，the recombination of ideas 想法的重新组合。',
 'genetic recombination；the recombination of；recombination processes。',
 'recombination 重组，不等于每次都 mutation 突变；技术名词不能仅由再加组合推断完整机制。',
 ('The chapter introduces genetic recombination.','这一章介绍遗传重组。'),('The design emerged from a recombination of older ideas.','这个设计来自对旧想法的重新组合。'))
R('B3672','一起联结、组合结果与重新组合','COMBINE：原来两两联结，现代能把多项合成一种效果','combine → combination；recombine、recombination 紧随看再次结合。combine 农机名词前重音，基础动词后重音。',
 '旧 bīnī 两两不限制现代只能合两个。组合锁的密码顺序重要，不能机械套数学 combination 的不计顺序含义。',
 'com- + bīnī → combīnāre 经法语 → combine；combīnātiō 经法语 → combination；re- + combine/combination；农机名缩短。',
 [['结合、结果与机器','combine · combination'],['重新组合与过程','recombine · recombination']],
 'combine 动词后重音、农机前重音；combination 独立借词史；recombination 非所有情形都基因突变。',
 'They recombined the parts to create a new combination.\n\n他们重新组合部件，创造出一种新组合。','combine combination recombine recombination')
G=[['古英语 gylt → 中古英语 gilt、gult → guilt','罪过、过错、责任；深源不确定'],['现代 guilt 的分层','客观有责、有罪；主观愧疚感']]
W('guilt','/ɡɪlt/','罪责、过错；内疚、愧疚感',
 '可以问这件错事是谁该负责，也可以说自己心里觉得对不起人。前者是责任，后者是感受，两者不保证一致。',
 '继承古英语 gylt，经中古英语 gilt 等，深源不明。与旧支付、债务词的联系有争论，不能硬编成欠债就是有罪。u 是历史拼写中的增入，现代不读 /ɡw/。',G,
 'a sense of guilt 内疚感，feel guilt 感到愧疚，admit guilt 承认罪责，guilt someone into doing 用愧疚感迫使人做〔口语动词〕。',
 'a sense of guilt；feel guilt；admit guilt；guilt someone into。',
 'feel guilt 有主观负疚，不自动证明法律有罪；guilt 与 gilt 镀金的、镀金同音，来源、意思不同。',
 ('She felt guilt about missing her friend’s wedding.','没能参加朋友的婚礼，她感到内疚。'),('The novel separates a character’s guilt from his feelings of guilt.','小说把一个角色的实际罪责与他的愧疚感分开描写。'),
 sources=['https://en.wiktionary.org/wiki/guilt#English','https://www.etymonline.com/word/guilt'])
W('guilty','/ˈɡɪlti/','有罪、有责任的；内疚的',
 '在法律或责任判断中可说确有过错；日常 I feel guilty 常只是觉得对不起，不是在正式认罪。',
 '古英语 gyltiġ → 中古英语 gilty 等 → guilty，现代对应 guilt + -y。这个形容词很早已存在，不是现代临时从感到内疚反推出来。',G[:1]+[['古英语 gyltiġ → guilty；对应 guilt + -y','有罪、有过错；后来也常说负疚感']],
 'feel guilty about 对某事内疚，guilty of a crime 犯有某罪，a guilty conscience 内疚的良心，a guilty pleasure 不好意思承认却喜欢的事。',
 'feel guilty about；guilty of；a guilty conscience；a guilty pleasure。',
 'guilty 法律身份与 guilty feeling 心理感受分开；guilty pleasure 常幽默说不好意思承认的爱好，不是必须违法的乐趣。',
 ('I felt guilty about forgetting her birthday.','忘了她的生日，我感到内疚。'),('The detective was determined to find the guilty person.','侦探决心找到真正有罪的人。'))
W('guiltily','/ˈɡɪltɪli/','内疚地、带着心虚地',
 '做了觉得不该做的事，语气、神情带着不好意思，像偷吃饼干后被问到那样心虚。',
 'guilty 的 y 变 i，再加 -ly；不拼成 guiltyly。副词写的是动作伴随的愧疚、心虚。',G[:1]+[['guilty + -ly → guiltily〔y 变 i〕','带着愧疚、心虚的方式']],
 'smile guiltily 心虚地笑，admit guiltily 内疚地承认，look away guiltily 心虚地移开目光。',
 'smile guiltily；admit guiltily；look away guiltily。',
 'guiltily 描写神态不等于证实有罪；a guilty smile 与 smile guiltily 分别用形容词修饰名词、副词修饰动作。',
 ('He smiled guiltily when she asked about the missing biscuits.','她问起不见的饼干时，他心虚地笑了。'),('She guiltily admitted that she had not read the report.','她有些内疚地承认自己还没看报告。'))
W('guiltless','/ˈɡɪltləs/','无罪、无过错的；无愧疚的〔视语境〕',
 '没有该承担的过错，或心里没有愧疚。-less 说没有 guilt，究竟是否在谈客观责任要看上下文。',
 '中古英语 giltles 等可确认，现代对应 guilt + -less；更早相应词形的记录、重建有差别，不强定某个唯一古拼写。',G[:1]+[['中古英语 giltles 等 → guiltless；对应 guilt + -less','没有罪责、过错或愧疚的']],
 'a guiltless person 无辜的人，guiltless of wrongdoing 没有过错，a guiltless conscience 无愧的良心。较书面，日常 innocent、not guilty 常更常见。',
 'a guiltless person；guiltless of；a guiltless conscience。',
 'guiltless 若说主观无愧，不自动证明客观没有责任；与 innocent 的重叠看具体搭配，避免用心理感受替代事实判断。',
 ('The story shows a guiltless child blamed for the accident.','故事描写一个无辜孩子为事故背了黑锅。'),('The narrator insists that she is guiltless of any wrongdoing.','叙述者坚称自己没有做错任何事。'))
R('B4374','罪责与内疚；人物性质和神态','GUILT：做错与觉得做错，是需要分开的两件事','guilt → guilty → guiltily；guiltless 加否定，责任与感受贯穿辨析。',
 '有人会为自己并无责任的事内疚，也有人有责任却不觉内疚。词源深处不确定，不把债务、支付猜想当事实。',
 'gylt → guilt；gyltiġ → guilty；guilty 的 y 变 i 加 -ly；guilt + -less。',
 [['罪责、状态和动作方式','guilt · guilty · guiltily'],['无罪责或无愧疚','guiltless']],
 '感到 guilty 不等于已定罪；guiltily 神态非事实证明；guilt/gilt 同音异词；guilty pleasure 常非违法。',
 'He felt guilty and smiled guiltily.\n\n他感到内疚，带着心虚笑了笑。','guilt guilty guiltily guiltless')
if __name__=='__main__':save('continuation_20261030_dt',ROOTS,WORDS)
