"""Exchanging, bargaining, bidding and negotiating, with practical examples."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
def S(word,base):
 return ['https://en.wiktionary.org/wiki/'+word+'#English','https://www.etymonline.com/word/'+base]
EXISTING_ROOT_ADDITIONS={
 'A1677':dict(words='swap swaps swapped swapping swappable'.split(),label='swap：互换，以及可以替换的 swappable',note='swap 早有打击义，达成交易、交换义可能接拍手成交的画面，但这个具体语义桥只是分析。swappable 双写 p 加完整 -able，表示可以换的。'),
 'A1760':dict(words='barter barters bartered bartering'.split(),label='barter：不直接付钱，以物或服务换取',note='barter 借古法语 barater 等材料，远源未定。现代 -er 已是借入词的一部分，不能误拆为英语 bar 加做事的人。'),
 'B2685':dict(words='haggle haggles haggled haggling haggler hagglers'.split(),label='haggle：像一点点削价一样讨价还价',note='haggle 接旧 haggen 砍的反复动作材料，与 hack 的旧砍切材料相连；较早指笨拙切砍，后有议价义。人物 haggler 较早也有拙工义，不把一切人物用法都当新近价格动词的产物。'),
 'B2824':dict(words='bid bidding bidder bidders outbid outbids outbidding'.split(),label='bid：出价、指令与超过别人的报价',note='bid 合流古英语 biddan 请求、命令与 beodan 提供、宣布等材料；出价主要接后一线，at your bidding 服从指令接另一线。outbid 的 out- 表超过，常见过去式、分词仍 outbid。'),
 'B4342':dict(words='negotiate negotiates negotiated negotiating negotiator negotiators'.split(),label='negotiate：谈条件，也设法通过难处',note='negotiate 可由 negotiation 逆构，或接拉丁 negotiatus；再接 negotiari 做生意、negotium 事务，其材料为否定成分 neg- 与 otium 闲暇。现代协商、谈妥与设法通过障碍要看宾语，不能一律机械翻成不休息。'),
}
SWAP=[['中古英语 swappen：打击、拍打，远源未定','可能模仿拍击声'],['达成交易 → 交换','可能借拍手成交的画面衔接，但具体过程只是分析']]
BARTER=[['古法语 barater 等 → 英语 barter','交易、议价材料，远源未定；旧语境还可带欺骗义'],['英语 barter 动词 → 以物易物名词','现代常说物品、服务相换，不直接用钱购买']]
HAGGLE=[['旧 haggen 砍的反复动作材料 → haggle','较早指不整齐、笨拙地砍切，比较 hack 同族'],['一点点砍削的画面 → 讨价还价','这座语义桥通常作可能的理解，不把价格谈判说成真的动刀']]
BID=[['古英语 biddan 请求、命令与 beodan 提供、宣布等合流','出价和命令不是单一现代词义互相硬变'],['出价 → bidder；out- 超过 + bid → outbid','bidding 也可接指令、吩咐的一支']]
NEG=[['拉丁 neg- 不 + otium 闲暇 → negotium 事务 → negotiari 做生意','事务、业务的旧命名，协商意义也已在拉丁发展'],['英语 negotiate 可由 negotiation 逆构，或接拉丁分词 negotiatus','名词比英语动词更早；后来另有设法通过障碍义']]
W('swap','英 /swɒp/；美 /swɑp/','交换、互换；换用；一次互换',
 '你坐我的位置，我坐你的，两边互换，是 swap。它很适合日常换座位、换班、换东西，也能说把一种东西换成另一种。',
 '旧 swappen 曾说打击、拍打，来源未定；后来达成交易、交换义可能通过拍手成交联系，但那条具体桥只是分析。现代使用直接抓双方互换或替换的动作。',SWAP,
 'swap seats 交换座位；swap shifts 换班；swap A for B 用 A 换 B。',
 'swap stories 交流各自经历；a book swap 图书交换活动。',
 'swap 常是互换或以一种换另一种，buy 明确购买；交换故事不是把其中一个人的故事永久交出去。',
 ('Can we swap seats so I can sit by the window?','我们能换个座位，让我坐窗边吗？'),('I want to swap this heavy bag for a lighter one.','我想把这个重包换成轻一点的。'),sources=S('swap','swap'))
W('swaps','英 /swɒps/；美 /swɑps/','交换、换用〔第三人称单数〕；互换、交换活动〔复数〕',
 '她每周和同事换一次班，动词用 swaps；社区办的几场图书交换活动，名词也可用 swaps。',
 'swap + -s，/p/ 后读 /s/；动词三单与名词复数同形。金融中的 swaps 则是互换合约的特定用法。',SWAP+[['swap + -s → swaps','他或它交换；多次交换、交换活动等']],
 'swaps shifts with a colleague 和同事换班；book swaps 图书交换活动。',
 'swaps one thing for another；clothes swaps 衣物交换活动。',
 'swaps 说双方交换，gives away 说赠送出去；一场 clothes swap 通常不只是一方向外捐衣服。',
 ('She swaps shifts with a colleague once a month.','她每月和一位同事换一次班。'),('The library hosts book swaps for local families.','图书馆为本地家庭举办图书交换活动。'),sources=S('swaps','swap'))
W('swapped','英 /swɒpt/；美 /swɑpt/','交换、换用、替换了',
 '原来用纸杯，后来改用可重复用的杯子，是 swapped paper cups for reusable ones。它把原先和后来两边清楚摆出来。',
 'swap 双写 p 加完整 -ed，/p/ 后读 /t/；过去式、过去分词。',SWAP+[['swap + -ed → swapped','过去完成互换或替换，双写末尾 p']],
 'swapped seats 交换了座位；swapped A for B 用 B 替掉 A。',
 'swapped stories over dinner 晚饭时交流经历；swapped the old battery。',
 'swapped A for B 中，A 是拿去换、被替下的，B 是换来的；方向不要只看中文一个换字。',
 ('We swapped seats halfway through the journey.','旅途中途我们换了座位。'),('The café swapped plastic straws for paper ones.','咖啡馆把塑料吸管换成了纸吸管。'),sources=S('swapped','swap'))
W('swapping','英 /ˈswɒpɪŋ/；美 /ˈswɑpɪŋ/','正在交换、换用；交换活动',
 '几个人坐着轮流讲自己的经历，是 swapping stories；把旧部件换成新部件，也能用 swapping。',
 'swap 双写 p 加 -ing；动作形式可作名词谈交换活动，内部的现代意义不靠旧打击义逐字推。',SWAP+[['swap + -ing → swapping','互换、替换的过程或活动']],
 'swapping stories 交流经历；swapping shifts 换班。',
 'swapping one item for another；swapping contact details 交换联系方式。',
 'swapping contact details 通常是彼此提供，不是删除自己原有资料；具体交换常只是双方都获得信息。',
 ('The neighbours spent the evening swapping stories.','邻居们一晚上都在交流各自的经历。'),('Swapping the old bulb for an LED one was easy.','把旧灯泡换成 LED 灯泡很容易。'),sources=S('swapping','swap'))
W('swappable','英 /ˈswɒpəbəl/；美 /ˈswɑpəbəl/','可以互换、替换的',
 '电池用完，不必把整台设备丢掉，取下来换一块就行，这块电池就是 swappable。重点是设计上能换。',
 'swap 双写 p 加完整 -able；-able 写可以进行相应动作的性质，不是单独用一个 -ble 解释。',SWAP+[['swap + -able → swappable','可以交换、替换，双写末尾 p']],
 'a swappable battery 可更换电池；swappable parts 可替换部件。',
 'easily swappable 容易换的；a swappable cover 可更换外壳。',
 'swappable 说能换，removable 只说能取下；某个盖子可以取下清洗，却未必提供别的盖子供替换。',
 ('The device comes with a swappable battery.','这台设备配有可更换电池。'),('The keyboard has swappable keycaps.','这把键盘的键帽可以更换。'),sources=S('swappable','swap'))
W('barter','英 /ˈbɑːtə/；美 /ˈbɑrtɚ/','以物易物；用物品、服务交换',
 '你修我的自行车，我给你几箱苹果，双方不用先算成现金购买，这种交换就是 barter。核心是拿自己有的东西或服务来换。',
 '借古法语 barater 等交易、议价材料，远源未定；旧法语有欺骗义，不表示现代每次 barter 都含诈骗。英语常把借入动词整体理解，-er 不是此词的人物后缀。',BARTER,
 'barter goods 交换货物；barter A for B 用 A 换 B；a barter system 以物易物体系。',
 'barter for food 用物品、服务换食物；barter with neighbours。',
 'barter 重点在以物或服务交换，haggle 重点在争取价格、条件；现金购物也可 haggle，不必是 barter。',
 ('They agreed to barter fresh vegetables for repair work.','他们同意用新鲜蔬菜交换维修服务。'),('Barter was common in the village when cash was scarce.','现金少的时候，村里常以物易物。'),sources=S('barter','barter'))
W('barters','英 /ˈbɑːtəz/；美 /ˈbɑrtɚz/','以物或服务交换〔第三人称单数〕；交换交易〔复数〕',
 '她把自制面包拿去换鸡蛋，是 she barters；不在于东西贵不贵，而在于用自己提供的东西换对方的。',
 'barter + -s，读 /z/；通常为动词三单，也可在具体语境中数一笔笔交换。基础 barter 整体经法语借入。',BARTER+[['barter + -s → barters','他或她以物易物，或多笔交换']],
 'barters bread for eggs 用面包换鸡蛋；barters with local farmers。',
 'barters services 换服务；barters for supplies 换取补给。',
 'barters 不要求双方交换完全相同的东西；swaps seats 才是很典型的同类位置互换。',
 ('She barters homemade bread for fresh eggs.','她用自制面包换新鲜鸡蛋。'),('The mechanic barters repair work for vegetables.','那位修理工用维修服务换蔬菜。'),sources=S('barters','barter'))
W('bartered','英 /ˈbɑːtəd/；美 /ˈbɑrtɚd/','以物、服务换取了；交换了',
 '旅途中把多余工具换成食物，这个交换过去完成了，就用 bartered。句子把拿出去的东西和换回的东西对应起来。',
 'barter + 完整 -ed，读 /d/；普通规则过去式、过去分词，没有另加 /ɪd/ 音节。',BARTER+[['barter + -ed → bartered','过去用物品、服务换取所需']],
 'bartered A for B 用 A 换了 B；bartered with traders 与商贩交换。',
 'bartered for food；bartered away valuables 拿贵重物换走别的东西。',
 'bartered 是以物或服务交换，bought 通常是付钱买；具体故事若用了钱和物混合交换，应看句子交代。',
 ('The travellers bartered spare tools for food.','旅人们用多余工具换食物。'),('We bartered a day of painting for help with the garden.','我们用一天刷漆的活，换来别人帮忙打理花园。'),sources=S('bartered','barter'))
W('bartering','英 /ˈbɑːtərɪŋ/；美 /ˈbɑrtərɪŋ/','正在以物易物；物品、服务交换活动',
 '不用先把每件东西卖成钱，而是把彼此需要的物品、技能直接对换，这项活动就是 bartering。',
 'barter + -ing；英式在元音词尾前可读出 r。作为动作名词，可以谈以物易物这种方式。',BARTER+[['barter + -ing → bartering','以物或服务交换的过程、活动']],
 'bartering skills 交换技能；bartering for supplies 交换获得补给。',
 'a system of bartering；bartering goods and services。',
 'bartering 描写交换方式，bargaining 描写谈条件的活动；人可以先谈条件，再按谈好的方式以物交换。',
 ('Bartering allowed the neighbours to exchange skills without using cash.','以物易物让邻居们不用现金就能交换技能。'),('They spent the morning bartering for supplies.','他们一上午都在用物品交换补给。'),sources=S('bartering','barter'))
W('haggles','/ˈhæɡəlz/','讨价还价、争论条件〔第三人称单数〕',
 '标价十元，他还八元，对方说九元，来回磨价就是 haggles。动作像一点点往下削，但现代不是真砍东西。',
 'haggle + -s，/l/ 后读 /z/；haggle 接旧砍切词的反复动作材料，后有议价义。',HAGGLE+[['haggle + -s → haggles','他或她反复议价、争论条件']],
 'haggles over the price 为价格讨价还价；haggles with sellers 和卖家讲价。',
 'haggles for a better deal；haggles over every detail。',
 'haggles 常强调来回磨条件，asks for a discount 可能只是问一次能否打折；反复程度不同。',
 ('He always haggles over the price at the market.','他在市场买东西总爱讲价。'),('She haggles with the seller until they agree on a price.','她和卖家来回议价，直到双方谈妥。'),sources=S('haggles','haggle'))
W('haggled','/ˈhæɡəld/','讨价还价、反复争论条件了',
 '谈了半天，一方再让一点，另一方再添一点，过去这段磨条件的过程就是 haggled。它不预先保证最后成交。',
 'haggle 去 e 加完整 -ed，/l/ 后读 /d/；词干本有的 /əl/ 仍保留，不是 -ed 另起一个音节。',HAGGLE+[['haggle + -ed → haggled','过去反复议价、争论条件']],
 'haggled over the price 为价格来回讲；haggled for an hour 讲价一小时。',
 'haggled with the owner；haggled over the terms。',
 'haggled over the price 只说议价，agreed on the price 才明确谈妥价格；过程与结果分开。',
 ('We haggled over the price for twenty minutes.','我们为价格来回讲了二十分钟。'),('They haggled with the owner but left without buying anything.','他们和店主讨价还价，最后什么也没买就走了。'),sources=S('haggled','haggle'))
W('haggling','/ˈhæɡlɪŋ/','正在讨价还价；反复议价、磨条件',
 '双方你一句我一句，不断改价格、磨条件，整段过程就叫 haggling。比普通讨论更有互相拉扯的感觉。',
 'haggle 去 e 加 -ing，常读 /ˈhæɡlɪŋ/；可作动作形式，也可作活动名词。',HAGGLE+[['haggle + -ing → haggling','反复议价、争论条件的过程']],
 'haggling over prices 为价格反复讲；no haggling 不讲价。',
 'hours of haggling 好几小时讨价还价；haggling with a dealer。',
 'haggling 常聚焦价格、细节上的来回磨，negotiating 范围更广，也可严肃协商政策、和平等事务。',
 ('After an hour of haggling, we finally agreed on a price.','讲价一小时后，我们终于谈妥了价格。'),('The shop has fixed prices, so there is no haggling.','这家店明码定价，不讲价。'),sources=S('haggling','haggle'))
W('haggler','英 /ˈhæɡlə/；美 /ˈhæɡlɚ/','讨价还价的人',
 '看到标价不立刻付钱，总要问能不能再少一点、来回磨条件的人，是 a haggler。词指习惯或角色，不说明他一定不讲理。',
 '现代可拆 haggle 去 e 加 -er。较早 haggler 还有笨拙切砍的工人义，因此这个人物词的所有历史不能只从现代价格动词临时派生来讲。',HAGGLE+[['haggle + -er → haggler','现代常指反复议价的人；更早人物义还保留砍切背景']],
 'a skilled haggler 讲价能手；a persistent haggler 总爱磨价的人。',
 'a good haggler；an experienced haggler。',
 'haggler 说爱讲价或会讲价的人，bargain hunter 说爱找便宜货的人；后者可能只看打折，不跟卖家议价。',
 ('My aunt is a skilled haggler at street markets.','我姑姑在街市上很会讲价。'),('The seller smiled when he realised he was dealing with an experienced haggler.','卖家发现面前是个讲价老手，笑了起来。'),sources=S('haggler','haggle'))
W('hagglers','英 /ˈhæɡləz/；美 /ˈhæɡlɚz/','讨价还价的人〔复数〕',
 '市场里一群人围着摊位，你来我往地讲价，便可以把他们叫 hagglers。最后的 -s 只把讲价者变成多个。',
 'haggler + -s，读 /z/；内层 haggle 去 e 加 -er。现代通常按价格、条件场景理解人物义。',HAGGLE+[['haggler + -s → hagglers','多位讨价还价的人']],
 'experienced hagglers 讲价老手；persistent hagglers 一直磨价的人。',
 'hagglers at the market；a group of hagglers。',
 'hagglers 在争取条件，bidders 在报出愿付价格；拍卖者可能不断出价，却未必和卖家一对一讨价还价。',
 ('Experienced hagglers knew which stalls offered room for bargaining.','讲价老手知道哪些摊位留有还价余地。'),('The seller stayed patient with the persistent hagglers.','面对一直磨价的顾客，卖家保持着耐心。'),sources=S('hagglers','haggle'))
W('bidding','/ˈbɪdɪŋ/','正在出价；竞价；〔at someone’s bidding〕依某人吩咐',
 '拍卖时大家一轮轮报价格，是 bidding；at her bidding 则是按她的吩咐。两种现代义接 bid 合流的不同旧材料。',
 'bid 双写 d 加 -ing。出价线接古英语 beodan 提供、宣布等；吩咐线接 biddan 请求、命令等，不能全拿价钱解释。',BID+[['bid + -ing → bidding','竞价过程；另一支可说吩咐、指令']],
 'competitive bidding 竞争性投标；bidding for a painting 竞拍画作；at his bidding 依他吩咐。',
 'open the bidding 开始竞价；a bidding war 竞价争夺。',
 'bidding 是出价过程，a bid 是一次报价；at your bidding 属于较正式的吩咐搭配，场景要另外识别。',
 ('Bidding for the painting started at five hundred pounds.','这幅画的起拍价是五百英镑。'),('He expected everyone to act at his bidding.','他指望每个人都按他的吩咐行动。'),sources=S('bidding','bid'))
W('bidders','英 /ˈbɪdəz/；美 /ˈbɪdɚz/','竞价者、投标者〔复数〕',
 '拍卖场里愿意报价格的人，或争取承包项目的公司，都可以叫 bidders。可能是个人，也可能是机构。',
 'bidder + -s，读 /z/；内层 bid 双写 d 加 -er，人物、角色尾在此也可指参与投标的公司。',BID+[['bid + -er → bidder → bidders','多个出价者、投标者']],
 'potential bidders 潜在竞买者；successful bidders 中标者、竞得者。',
 'several bidders；invite bidders 邀请投标者。',
 'bidders 是正在或准备出价的一方，buyers 是买家；参与竞价的人不一定最终买到。',
 ('Several bidders competed for the old clock.','几位竞买者争相竞拍那座旧钟。'),('The company invited bids from qualified bidders.','公司邀请符合资格的投标者报价。'),sources=S('bidders','bid'))
W('outbids','/ˌaʊtˈbɪdz/','出价高于、压过〔第三人称单数〕',
 '你报一百，对方报一百一十，他就 outbids you。out- 在这里给出“比你更高、更胜一筹”的方向。',
 'out- 超过 + bid 出价，再加 -s；/d/ 后读 /z/。宾语常是被超过报价的人或机构。',BID+[['out- + bid + -s → outbids','他或它报出比另一方更高的价']],
 'outbids everyone 出价高过所有人；outbids a rival 出价压过对手。',
 'consistently outbids us 总比我们出价高；outbids other buyers。',
 'outbids us 比的是报价高，outsells us 比的是卖得多；角色、衡量方向不同。',
 ('That collector always outbids us at auctions.','那位收藏家在拍卖时总比我们出价高。'),('The larger company outbids smaller rivals for prime locations.','大公司为拿下黄金地段，出价压过较小的对手。'),sources=S('outbids','outbid'))
W('outbidding','/ˌaʊtˈbɪdɪŋ/','正在出更高价格、压过别人的报价',
 '别人刚加价，你又加一点，一次次报得比对方高，是 outbidding。强调比较，不是单独报了一个高价就自动适用。',
 'outbid 双写 d 加 -ing；外层 out- 表超过，bid 出价。过去式、过去分词常为 outbid，与 -ing 的规则不相同。',BID+[['outbid + -ing → outbidding','通过更高报价压过另一方的过程']],
 'outbidding other buyers 出价压过其他买家；keep outbidding each other 不断互相抬价。',
 'outbidding a rival；a strategy of outbidding competitors。',
 'outbidding 强调相对另一方更高，overpaying 强调付得超过价值；出价高过别人不必然等于买贵。',
 ('The two collectors kept outbidding each other.','两位收藏家不断互相抬价。'),('The broadcaster secured the rights by outbidding its rivals.','那家广播公司出价压过对手，拿到了相关权利。'),sources=S('outbidding','outbid'))
W('negotiates','英 /nɪˈɡəʊʃieɪts/；美 /nɪˈɡoʊʃieɪts/','协商、谈妥；设法通过〔第三人称单数〕',
 '她和供应商谈条件，是 negotiates with suppliers；车慢慢绕过急弯，也可说 negotiates a bend。后者是把难处处理过去。',
 'negotiate + -s，/t/ 后读 /s/。基础词可能由 negotiation 逆构，或接拉丁相应分词；现代短动词不一定历史先出现。',NEG+[['negotiate + -s → negotiates','他或它协商、谈成，或设法通过难处']],
 'negotiates with suppliers 与供应商协商；negotiates a contract 谈成合同。',
 'negotiates a sharp bend 设法通过急弯；negotiates terms 协商条件。',
 'negotiate with 后接交涉对象，negotiate a bend 的宾语是要通过的难处；同一中文谈判不能套遍。',
 ('She negotiates prices with suppliers every month.','她每月都和供应商协商价格。'),('The bus negotiates the narrow bend slowly.','公交车慢慢通过那个狭窄弯道。'),sources=S('negotiates','negotiate'))
W('negotiated','英 /nɪˈɡəʊʃieɪtɪd/；美 /nɪˈɡoʊʃieɪtɪd/','协商、谈妥了；设法通过了；经协商达成的',
 '双方坐下来谈，终于得到可接受的条件，是 negotiated a deal；走路小心越过难处，也可用 negotiated。看清宾语最省力。',
 'negotiate 去 e 加完整 -ed，/t/ 后读 /ɪd/，增加音节。分词也可写 negotiated agreement 经协商达成的协议。',NEG+[['negotiate + -ed → negotiated','过去协商、谈成或通过难处；也写谈成后的性质']],
 'negotiated a lower price 谈到更低价格；a negotiated settlement 协商达成的和解。',
 'negotiated the stairs 设法走过楼梯；negotiated with the owner。',
 'negotiated with someone 只说曾交涉，negotiated an agreement 通常明确谈出协议；有没有结果要看整个搭配。',
 ('They negotiated a lower price for the equipment.','他们把设备价格谈低了。'),('We carefully negotiated the narrow steps with our bags.','我们拎着包，小心走过狭窄台阶。'),sources=S('negotiated','negotiate'))
W('negotiating','英 /nɪˈɡəʊʃieɪtɪŋ/；美 /nɪˈɡoʊʃieɪtɪŋ/','正在协商、谈条件；设法通过；协商用的',
 '合同还没定，双方在谈细节，是 negotiating；带着自行车绕过人群，也是在设法处理眼前的通行难处。',
 'negotiate 去 e 加 -ing。可说协商过程，也可在 negotiating team 谈判团队等组合里说明用途、角色。',NEG+[['negotiate + -ing → negotiating','协商或设法通过的过程；相关角色修饰']],
 'negotiating terms 协商条件；a negotiating team 谈判团队。',
 'negotiating with the landlord；negotiating a difficult path 设法走过难行小路。',
 'negotiating 指过程，signing an agreement 指签下协议；谈着并不等于已经签好。',
 ('We are still negotiating the terms of the contract.','我们仍在协商合同条款。'),('She had trouble negotiating the crowded street with a bicycle.','她推着自行车穿过拥挤街道时有些吃力。'),sources=S('negotiating','negotiate'))
W('negotiators','英 /nɪˈɡəʊʃieɪtəz/；美 /nɪˈɡoʊʃieɪtɚz/','谈判者、协商代表〔复数〕',
 '坐到桌前，代表各方提条件、找共同方案的人，是 negotiators。他们不一定亲自拥有争议中的物品，也可以代表公司、团队。',
 'negotiator + -s，读 /z/；人物词借拉丁 negotiator 商务人物名，现代可与 negotiate 去 e 加 -or 对应认形，不能把词史只讲成英语现拼。',NEG+[['拉丁 negotiator → 英语 negotiator → negotiators','商务人物名发展为谈判者，再加现代复数']],
 'skilled negotiators 谈判高手；peace negotiators 和平谈判代表。',
 'negotiators from both sides；a team of negotiators。',
 'negotiators 代表各方谈条件，mediators 常从中帮助各方沟通；角色不同，不能只因都坐在谈判桌前就一律翻成代表。',
 ('Negotiators from both sides met again on Monday.','双方谈判代表周一再次会面。'),('Skilled negotiators listen carefully before making an offer.','有经验的谈判者会先认真听，再提出条件。'),sources=S('negotiators','negotiate'))
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_zhc',ROOTS,WORDS)
 extend_lessons()
