"""Retail, wholesale, auctions, comparative bids and sellers."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
def S(word,base):
 return ['https://en.wiktionary.org/wiki/'+word+'#English','https://www.etymonline.com/word/'+base]
EXISTING_ROOT_ADDITIONS={
 'B3411':dict(words='retail retails retailed retailing'.split(),label='retail：按件零售与零售价',note='retail 接法语切下部分的名动材料，按件售卖的具体发展未全定；现代 retails for 常说零售价格，不能当成 re- 再次加英语 tail 尾巴。'),
 'B2786':dict(words='wholesale wholesales wholesaled wholesaling wholesaler wholesalers'.split(),label='wholesale：成批出售与批发商',note='whole 加 sale 构成成批销售材料，动词较晚出现；wholesaler 为 wholesale 去 e 加 -er。大批、全面的形容词义也有发展，但不是把所有义都译作卖完整物品。'),
 'C0097':dict(words='auction auctions auctioned auctioning auctioneer auctioneers'.split(),label='auction：加价拍卖的旧命名与拍卖者',note='auction 接拉丁 auctio、augere 增加的材料，动词由名词转用；auctioneer 加完整 -eer，主持拍卖的人与参与出价的 bidder 角色不同。'),
 'B2824':dict(words='underbid underbids underbidding overbid overbids overbidding'.split(),label='underbid、overbid：报价低、高于比较点',note='under- 低于、over- 超过加 bid。underbid 可指比对手报价低或报价不足；overbid 可指报价超过对手或过高。竞买还是供货投标，会影响低价、高价的作用。'),
 'C1615':dict(words='vend vends vended'.split(),label='vend：较正式的出售动词形式',note='vend 借拉丁 vendere，缩自 venum 出售相关材料加 dare 给；vends、vended 是现代屈折形式。普通说卖常用 sell，自动售货语境 vend 仍很直观。'),
 'B3382':dict(words='bargain bargainer'.split(),label='bargainer：谈条件的人',note='bargain 经法语议价材料，远源有日耳曼借贷等不同分析，未全定。现代 bargainer 为 bargain 加 -er，不能由含义直接认定与 bar 船或 gain 得到是现拼。'),
}
RETAIL=[['法语 retail、retaillier 等：切下的部分、切下','英语接按件销售的画面，具体传入发展有不同分析'],['英语 retail 名词、动词 → 现代形式','零售；retail for 某价表示以该零售价出售']]
WHOLE=[['whole 整批、整体 + sale 销售 → wholesale','与按小份零售相对的成批销售'],['较晚 wholesale 动词 → wholesaler 与现代屈折','批量供货的动作及批发商角色']]
AUCTION=[['拉丁 augere 增加 → auctio、auctionem','通过报价不断加高来卖出的旧命名'],['英语 auction 名词 → 动词；auction + -eer','拍卖活动、拍卖出售、主持拍卖者']]
BID=[['bid 出价接古英语 beodan 提供、宣布等材料','现代 bid 还合流另一请求、命令线，当前只取报价义'],['under- 低于、over- 超过 + bid','比某报价低、高，或低、高于合理、可支撑的水平']]
VEND=[['拉丁 venum 出售相关材料 + dare 给 → vendere','提供出售'],['拉丁动词 → 英语 vend → 现代词尾','出售；自动售货设备常用此动作']]
W('retails','/ˈriːteɪlz/','零售；以某零售价出售〔第三人称单数〕',
 '这台咖啡机在店里卖多少钱，英文常用 it retails for…。主语是商品时，是说它的零售价格，不是机器自己当店主。',
 'retail + -s，/l/ 后读 /z/；基础词接法语切下部分、切分材料，现代零售动词可及物说商家卖，也可不及物说商品售价。',RETAIL+[['retail + -s → retails','它零售货品，或该商品以某零售价出售']],
 'retails for fifty pounds 零售价五十英镑；retails at a higher price 以更高零售价出售。',
 'the shop retails local products；a model that retails for…。',
 'retails for 某价 是终端零售价，costs the shop 某价 是商家的成本；句中谁花钱、谁卖要分清。',
 ('The camera retails for about three hundred pounds.','这台相机零售价约三百英镑。'),('The shop retails products made by local craftspeople.','商店零售当地手艺人制作的产品。'),sources=S('retails','retail'))
W('retailed','/ˈriːteɪld/','零售了；以某零售价出售了；转述了',
 '当年这款机器在店里卖一百元，可以说 retailed for…。较书面的 retailed a story 则是把故事转述给别人，另按信息场景认。',
 'retail + 完整 -ed，/l/ 后读 /d/；零售之外，较早也有把信息分传、转述的动词分支。',RETAIL+[['retail + -ed → retailed','过去零售、以某价出售，或转述信息']],
 'retailed for a certain price 以某零售价出售；retailed through shops 通过商店零售。',
 'retailed stories 转述故事；retailed local goods 零售当地产品。',
 'retailed a story 是较书面的转述，told a story 更日常；不能在任何讲故事场景都优先换成 retail。',
 ('The model originally retailed for two hundred dollars.','这款产品最初零售价是二百美元。'),('The company retailed its products through small local shops.','公司通过本地小店零售产品。'),sources=S('retailed','retail'))
W('retailing','/ˈriːteɪlɪŋ/','零售活动、零售业；正在零售',
 '把商品卖到最终顾客手里，像社区小店、网上零售店做的事，整体就叫 retailing。它说的是销售环节，店面可大可小。',
 'retail + -ing；作为动作名词的形式很早已有，现代可谈行业、业务活动。',RETAIL+[['retail + -ing → retailing','零售过程或这一商业活动领域']],
 'online retailing 网上零售；food retailing 食品零售。',
 'a career in retailing 零售业工作；retailing directly to customers 直接零售给顾客。',
 'retailing 面向终端顾客，wholesaling 常把货批给再售卖的商家；关键是销售链条角色，不仅看店铺面积。',
 ('Online retailing has changed how many people shop.','网上零售改变了许多人的购物方式。'),('She began her career in food retailing.','她从食品零售行业开始职业生涯。'),sources=S('retailing','retail'))
W('wholesales','英 /ˈhəʊlseɪlz/；美 /ˈhoʊlseɪlz/','批发、成批出售〔第三人称单数〕',
 '一家公司把整箱食品卖给餐馆、商店，让他们再用或再卖，叫 wholesales。看见 whole，抓整批供货的画面。',
 'wholesale + -s，/l/ 后读 /z/；内层 whole + sale。动词从既有的批发材料转用，历史比早期形容词等用途更晚。',WHOLE+[['wholesale + -s → wholesales','它进行批发、成批供货']],
 'wholesales goods to shops 向商店批发货物；wholesales food 批发食品。',
 'wholesales in bulk；wholesales to restaurants。',
 'wholesales 常面向其他经营者供货，retails 常面向最终消费者；同一家公司可以同时做两种业务。',
 ('The company wholesales food to local restaurants.','公司向当地餐馆批发食品。'),('The supplier wholesales cleaning products in large packs.','供应商成大包装批发清洁用品。'),sources=S('wholesales','wholesale'))
W('wholesaled','英 /ˈhəʊlseɪld/；美 /ˈhoʊlseɪld/','批发、成批出售了',
 '工厂做好的桌布不是逐条卖给路人，而是一批批供给商店，过去的这项售货动作就是 wholesaled。',
 'wholesale 去 e 加完整 -ed，/l/ 后读 /d/；词基尾部原有的 sale 不当作独立时态尾。',WHOLE+[['wholesale + -ed → wholesaled','过去进行批发、成批供货']],
 'wholesaled goods to retailers 向零售商批发货物；wholesaled in bulk 成批出售。',
 'wholesaled through distributors；wholesaled to shops。',
 'wholesaled 说明批发出售，manufactured 说明制造；工厂制造商品后，可以自行批发，也可交给其他企业卖。',
 ('The company wholesaled its furniture to regional stores.','公司把家具批发给各地区商店。'),('They wholesaled fresh produce to hotels and restaurants.','他们向酒店和餐馆批发新鲜农产品。'),sources=S('wholesaled','wholesale'))
W('wholesaling','英 /ˈhəʊlseɪlɪŋ/；美 /ˈhoʊlseɪlɪŋ/','批发活动、批发业；正在批发',
 '从生产方拿成批商品，再分给商店、餐馆等经营者，这个销售环节可以叫 wholesaling。重点是成批供货的角色。',
 'wholesale 去 e 加 -ing；动作形式也可作名词谈批发业务，不等于把所有 wholesale 的大规模形容词义都转成买卖。',WHOLE+[['wholesale + -ing → wholesaling','批发过程、业务活动']],
 'food wholesaling 食品批发；a wholesaling business 批发业务。',
 'wholesaling to retailers；experience in wholesaling。',
 'wholesaling 与 retailing 关注渠道角色，warehousing 关注存储；同一企业可能两者都有，但词指的活动不同。',
 ('The family business specialises in food wholesaling.','这家家族企业专做食品批发。'),('They moved from wholesaling to selling directly to customers.','他们从批发转为直接向顾客销售。'),sources=S('wholesaling','wholesale'))
W('wholesaler','英 /ˈhəʊlseɪlə/；美 /ˈhoʊlseɪlɚ/','批发商',
 '把货成批供给商店、餐馆等经营者，而不是主要一件件卖给路过顾客，这种供货角色叫 wholesaler。',
 'wholesale 去不发音 e 加完整 -er，人物、机构尾；前面 whole + sale 的批量销售画面仍在。',WHOLE+[['wholesale + -er → wholesaler','进行成批供货的人或企业']],
 'a food wholesaler 食品批发商；a clothing wholesaler 服装批发商。',
 'buy from a wholesaler 向批发商进货；a local wholesaler。',
 'wholesaler 关注批量供货，retailer 关注面向最终消费者零售；一家企业也可能兼做两种业务。',
 ('The restaurant buys fresh vegetables from a local wholesaler.','餐馆向当地一家批发商采购新鲜蔬菜。'),('The wholesaler supplies small shops across the region.','这家批发商给整个地区的小店供货。'),sources=S('wholesaler','wholesale'))
W('wholesalers','英 /ˈhəʊlseɪləz/；美 /ˈhoʊlseɪlɚz/','批发商〔复数〕',
 '零售店要进一批货，不必一家家找生产工厂，可以找 wholesalers。这个词说的是向其他经营者成批供货的人、公司。',
 'wholesaler + -s，读 /z/；内层 wholesale 去 e 加 -er，人物、机构尾，再加复数。',WHOLE+[['wholesale + -er → wholesaler → wholesalers','批发角色名称及其复数']],
 'food wholesalers 食品批发商；local wholesalers 当地批发商。',
 'buy from wholesalers 向批发商进货；wholesalers and retailers。',
 'wholesalers 是供货、售货角色，manufacturers 是生产者；批发商未必自己造货，生产者也可能直接批发。',
 ('Small shops often buy their stock from wholesalers.','小店常从批发商那里进货。'),('Several food wholesalers supply the city’s restaurants.','几家食品批发商为这座城市的餐馆供货。'),sources=S('wholesalers','wholesale'))
W('auctions','英 /ˈɔːkʃənz/；美 /ˈɔkʃənz/','拍卖活动〔复数〕；拍卖出售〔第三人称单数〕',
 '一场场拍卖会，是 auctions；公司定期把旧设备拿去拍卖，动词也用 auctions。先看是在数活动，还是说谁在卖。',
 'auction + -s，/n/ 后读 /z/；拉丁 auctio 的旧名词连着报价增加，英语动词后来由名词转用。',AUCTION+[['auction + -s → auctions','多场拍卖，或它以拍卖方式出售']],
 'online auctions 网上拍卖；charity auctions 慈善拍卖。',
 'auctions off old equipment 拍卖旧设备；attend auctions 参加拍卖。',
 'auctions 指活动或拍卖出售的动作，bids 指报价；一场 auction 里可以出现许多 bids。',
 ('The charity holds two auctions each year.','这家慈善机构每年举行两场拍卖。'),('The council auctions off old vehicles.','市政部门拍卖旧车辆。'),sources=S('auctions','auction'))
W('auctioned','英 /ˈɔːkʃənd/；美 /ˈɔkʃənd/','拍卖出售了；被拍卖了',
 '画、旧设备拿到拍卖场，让竞买者报价，最后以拍卖方式卖掉，就是 auctioned。它是售出的方式，不只是有人看了看。',
 'auction + 完整 -ed，/n/ 后读 /d/；英语拍卖动词由较早名词转用，off 常补出卖出去的结果感。',AUCTION+[['auction + -ed → auctioned','过去以拍卖形式出售，或被这样出售']],
 'auctioned off 拍卖卖掉；auctioned for charity 为慈善拍卖。',
 'was auctioned online；auctioned at a high price。',
 'auctioned 通常说拿去拍卖出售，bid on 指作为买方出价；谁在卖、谁在买不要看成同一种动作。',
 ('The painting was auctioned to raise money for the school.','那幅画被拍卖，用来为学校筹款。'),('They auctioned off the old workshop equipment.','他们拍卖了旧车间设备。'),sources=S('auctioned','auction'))
W('auctioning','英 /ˈɔːkʃənɪŋ/；美 /ˈɔkʃənɪŋ/','正在拍卖出售；拍卖售卖活动',
 '把几件物品交给拍卖，作为售货方式来做，是 auctioning。不是坐在观众席举牌买，而是让物品通过拍卖卖出去。',
 'auction + -ing；名词转动词后形成的现代动作形式，通常与 off、objects 等具体搭配一起认。',AUCTION+[['auction + -ing → auctioning','以拍卖方式出售的过程、活动']],
 'auctioning off furniture 拍卖家具；auctioning items online 网上拍卖物品。',
 'auctioning a collection 拍卖一批收藏品；a plan for auctioning。',
 'auctioning 是拍卖出售，bidding 是参与出价；同一场活动里分属不同角色的动作。',
 ('The school is auctioning donated paintings to raise funds.','学校正在拍卖捐赠的画作筹款。'),('They considered auctioning off the remaining furniture.','他们考虑把剩余家具拍卖掉。'),sources=S('auctioning','auction'))
W('auctioneers','英 /ˌɔːkʃəˈnɪəz/；美 /ˌɔkʃəˈnɪrz/','拍卖师、主持拍卖者〔复数〕',
 '站在前面报出当前价、接受加价、最后落槌的人，是 auctioneers。不是所有来参加拍卖的人都算拍卖师。',
 'auctioneer + -s，读 /z/；内层 auction + 完整人物尾 -eer，不能只取 -er 而把剩下的 e 丢掉。',AUCTION+[['auction + -eer → auctioneer → auctioneers','主持拍卖的角色名及其复数']],
 'experienced auctioneers 有经验的拍卖师；auctioneers at the sale。',
 'a team of auctioneers；auctioneers and bidders。',
 'auctioneers 主持出售，bidders 竞相报价；seller 是卖方，未必亲自担任主持拍卖的角色。',
 ('The auctioneers explained the rules before the sale began.','拍卖开始前，拍卖师们说明了规则。'),('Experienced auctioneers keep track of bids quickly.','有经验的拍卖师能迅速跟上每次报价。'),sources=S('auctioneers','auction'))
W('underbid','英 /ˌʌndəˈbɪd/；美 /ˌʌndɚˈbɪd/','报价低于对手；出价不足、报得过低',
 '对手说一万元能做，你报九千元，同样的项目报价比他低，是 underbid him。也可能说价格报得太低，连自己要做的成本都撑不住。',
 'under- 低于 + bid 出价，清楚的现代组合。bid 的报价线接古英语提供、宣布等材料；常见过去式、分词也为 underbid。',BID+[['under- + bid → underbid','低于另一报价，或低于适当、可支撑的水平']],
 'underbid a rival 报价低于对手；underbid on a contract 对合同报低价。',
 'underbid by a large amount 大幅低于报价；underbid the job 把工作价报低。',
 'underbid a rival 在供货投标里常用低报价争取项目；在竞买里出价更低未必有优势，角色要放回句子看。',
 ('The smaller firm managed to underbid its larger rival.','小公司设法报出了比大对手更低的价格。'),('They worried that they had underbid the job.','他们担心这项工作报的价格过低。'),sources=S('underbid','underbid')+['https://www.merriam-webster.com/dictionary/underbid'])
W('underbids','英 /ˌʌndəˈbɪdz/；美 /ˌʌndɚˈbɪdz/','报价低于、报低价〔第三人称单数〕',
 '一家承包商每次都比别人报低一点，叫 it underbids the others。这里比较的是给出的价格，不是坐到谁的下面。',
 'underbid + -s，/d/ 后读 /z/；under- 给低于的比较方向，bid 给报价动作。',BID+[['underbid + -s → underbids','他或它给出较低、过低报价']],
 'underbids competitors 报价低于竞争者；underbids on projects 对项目报低价。',
 'consistently underbids us；underbids by ten percent。',
 'underbids 比报价低，undersells 通常比售价低；一次投标承诺的价格与实际零售商品价不是同一场景。',
 ('That contractor regularly underbids the competition.','那个承包商的报价经常低于对手。'),('The firm underbids on small projects to win new clients.','公司在小项目上报低价，以争取新客户。'),sources=S('underbids','underbid'))
W('underbidding','英 /ˌʌndəˈbɪdɪŋ/；美 /ˌʌndɚˈbɪdɪŋ/','正在报更低价格；报低、报价不足的做法',
 '两个商家轮流把承包报价往下压，是 underbidding each other。它可以只是竞争性低价，也可带报得不足的批评，取决于上下文。',
 'underbid 双写 d 加 -ing；内层 under- 低于 + bid。现代过程名词可谈这种报价方式。',BID+[['underbid + -ing → underbidding','报低价、报价低于另一方的过程或做法']],
 'underbidding rivals 报价压低于对手；underbidding each other 互相压低报价。',
 'a pattern of underbidding；underbidding on contracts。',
 'underbidding 不一定等于亏本；词可只比较另一报价，是否低于成本要有另外信息。',
 ('The two firms kept underbidding each other.','两家公司不断互相压低报价。'),('The report linked the losses to repeated underbidding on projects.','报告把亏损与项目反复报低价联系起来。'),sources=S('underbidding','underbid'))
W('overbid','英 /ˌəʊvəˈbɪd/；美 /ˌoʊvɚˈbɪd/','出价过高；报价超出某一水平；〔牌戏〕叫牌过高',
 '看中一件东西，越争越上头，报出的价超过自己认为值的钱，是 overbid。打牌时也能说叫得超出这手牌能支持的水平。',
 'over- 超过 + bid 出价、叫牌；常见过去式、过去分词也是 overbid。可以比较价值、前一报价或牌力，不能一律只认超过别人。',BID+[['over- + bid → overbid','报价超过比较点，常带过高义；牌戏也用']],
 'overbid at an auction 拍卖时出价过高；overbid on a hand 一手牌叫过高。',
 'try not to overbid；overbid by a large margin。',
 'outbid 明确比另一方报得高，overbid 常有超过价值、承受水平的感觉；提高报价压过别人，不自动意味着买贵。',
 ('I did not want to overbid just because I liked the painting.','我不想只因喜欢那幅画就报出过高价格。'),('He realised he had overbid after looking at his cards again.','再次看牌后，他意识到自己叫高了。'),sources=['https://en.wiktionary.org/wiki/overbid#English','https://www.merriam-webster.com/dictionary/overbid'])
W('overbids','英 /ˌəʊvəˈbɪdz/；美 /ˌoʊvɚˈbɪdz/','出价过高、叫牌过高〔第三人称单数〕；过高报价〔复数〕',
 '他一到竞价现场就容易喊得太高，可以说 he overbids。要是说一笔笔过高报价，名词复数也能是 overbids。',
 'overbid + -s，/d/ 后读 /z/；常用动词三单，名词复数也可同形。名词、动词的重音可能不同，这里先给动词常用读法。',BID+[['overbid + -s → overbids','他或它报价、叫牌过高；也可说多笔过高报价']],
 'overbids when excited 激动时出价过高；overbids a hand 叫牌超过牌力。',
 'frequently overbids；overbids at auctions。',
 'overbids 常评价报价超出适当水平，bids high 只说报得高；是否带过度评价有差别。',
 ('She overbids when she gets caught up in an auction.','她一投入竞拍，就容易出价过高。'),('The beginner often overbids in bridge.','那个初学者打桥牌时常叫得过高。'),sources=['https://en.wiktionary.org/wiki/overbids#English','https://www.merriam-webster.com/dictionary/overbid'])
W('overbidding','英 /ˌəʊvəˈbɪdɪŋ/；美 /ˌoʊvɚˈbɪdɪŋ/','正在出价过高；叫牌过高的做法',
 '随着竞争越喊越高，超过原来认为值的水平，这个过程可以叫 overbidding。牌戏里也能说一手牌叫得超出牌力。',
 'overbid 双写 d 加 -ing；over- 的超过要有具体比较点，不一定只指高于某个对手。',BID+[['overbid + -ing → overbidding','报价、叫牌超过适当水平的过程、做法']],
 'overbidding for a property 为房产出价过高；overbidding in bridge 桥牌叫牌过高。',
 'a habit of overbidding；avoid overbidding 避免报价、叫牌过高。',
 'overbidding 是报价行为，overpaying 是实际付得过多；报出过高价后未成交，不一定已经付了钱。',
 ('They blamed the loss on overbidding for the collection.','他们把亏损归因于为那批收藏品出价过高。'),('Her coach pointed out a pattern of overbidding in bridge.','她的教练指出，她打桥牌时有反复叫高的倾向。'),sources=['https://en.wiktionary.org/wiki/overbidding#English','https://www.merriam-webster.com/dictionary/overbid'])
W('vends','/vendz/','出售、自动售出〔第三人称单数〕',
 '投钱后机器出一瓶水，可以说 the machine vends drinks。vend 在售货设备里很直观，比日常随口说卖更正式。',
 'vend + -s，/d/ 后读 /z/；vend 借拉丁 vendere 出售，较远缩自出售相关材料与 dare 给的组合。',VEND+[['vend + -s → vends','他或它出售、售出货品']],
 'vends snacks 自动售出零食；vends tickets 售票。',
 'a machine that vends drinks；vends goods 出售货品。',
 'vends 在机器、正式售货语境常见，普通说我卖旧车多用 sell；不要为了显得高级到处替换。',
 ('The machine vends snacks and cold drinks.','这台机器售出零食和冷饮。'),('The kiosk vends tickets for local buses.','售票亭出售本地公交车票。'),sources=S('vends','vend'))
W('vended','/ˈvendɪd/','出售、售出了',
 '商品通过机器一件件售出，在较正式描述里可以写 was vended。这个词把东西放在出售环节，不是免费发放。',
 'vend + 完整 -ed，/d/ 后读 /ɪd/，多一个音节。前面的 vend 整体借拉丁动词，不把 ven、d 当作现代独立单词。',VEND+[['vend + -ed → vended','过去出售、售出，-ed 在 /d/ 后增加音节']],
 'vended by a machine 由机器售出；vended through kiosks 通过售货亭出售。',
 'vended goods 已售货物；vended in small quantities 小量出售。',
 'vended 明确有出售意思，dispensed 可说机器分出、配出物品，不必发生买卖；上下文决定是否付钱。',
 ('The drinks were vended through machines in the lobby.','饮料通过大厅里的机器售出。'),('The stall vended locally made crafts.','那个摊位出售当地制作的手工艺品。'),sources=S('vended','vend'))
W('bargainer','英 /ˈbɑːɡɪnə/；美 /ˈbɑrɡənɚ/','谈条件、讨价还价的人',
 '报价摆上桌后，能坚持自己的条件，又寻找对方肯接受的让步，这样的谈判者可以叫 bargainer。常见 hard bargainer，就是条件不好轻易压下来的人。',
 'bargain + -er。bargain 经古法语议价、交易材料，远源有日耳曼借贷等分析但未定；人物词这一层写进行议价的人。',
 [['古法语 bargaignier、bargaine 等 → bargain','交易、谈条件；远源分析不同'],['bargain + -er → bargainer','进行议价、谈条件的人']],
 'a hard bargainer 不轻易让步的谈判者；a skilled bargainer 谈条件的能手。',
 'a tough bargainer；an experienced bargainer。',
 'bargainer 指谈条件的人，bargain hunter 指找便宜货的人；后者可以买现成折扣商品而不与人谈条件。',
 ('She is a hard bargainer, but she keeps her word.','她谈条件不轻易让步，但说话算话。'),('An experienced bargainer knows when to compromise.','有经验的谈判者知道什么时候该妥协。'),sources=S('bargainer','bargain'))
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_zhe',ROOTS,WORDS)
 extend_lessons()
