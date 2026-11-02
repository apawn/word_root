"""Sell and sale: connected actions, amounts and sales techniques."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
SE=[['古英语 sellan → 中古英语 sellen','交给、给予；已发展为收钱转让'],['英语 sell','出售 → 推销商品、让别人接受主意']]
def SH(f,m):return SE+[[f,m]]
W('sell','/sel/','出售；卖得；推销、说服接受',
 '把东西给对方、换回钱是卖；把一个想法讲得让别人愿意接受，也可借卖来表达。',
 '继承古英语 sellan，旧义比今天宽，包括给予、交付；收钱转让义在古英语已出现。变化 sell—sold—sold。',SE,
 'sell a car 卖车，sell well 卖得好，sell an idea to someone 向某人推销想法，sell out 售罄或出卖原则。',
 'sell something to someone；sell well；sell out；sell an idea。',
 'sell 动词，sale 名词；The book sells well 是主动形式表达卖得好，不用硬改成 is sold well。',
 ('They sell fresh bread every morning.','他们每天早上卖鲜面包。'),('She sold the idea to the team with a clear demonstration.','她用清楚的演示让团队接受了这个想法。'),sources=['https://www.etymonline.com/word/sell','https://en.wiktionary.org/wiki/sell#English'])
W('sold','英 /səʊld/；美 /soʊld/','sell 的过去式、过去分词；已售出的；被说服的',
 '东西已经卖出去了；口语 I’m sold 又像说这个主意已经成功卖给我，我接受了。',
 'sell 的不规则过去式、分词，接古英语 salde 等旧形式演变。不是 sell + 普通 -ed 的现代拼法。',SH('sell → sold','已出售；比喻已被说服、认可'),
 'sold out 已售罄，sold to a buyer 已卖给买家；I’m sold on the idea 我认同这个主意。',
 'sold out；sold to；be sold on an idea。',
 'sold out 常说票或货没了；sellout 是可数名词，可说满座演出或为利益妥协者。sold 与 sale 也不是同一词性。',
 ('All the tickets were sold within an hour.','所有票一小时内卖光了。'),('After the demonstration, I was sold on the idea.','看完演示，我就认同这个主意了。'))
W('selling','/ˈselɪŋ/','销售、推销活动；正在出售',
 '把卖这件事作为过程来看，包含介绍、说明、成交等活动。',
 'sell + -ing，保留两个 l。可以是进行时、活动名词或修饰语，selling point 则指吸引人购买的优点。',SH('sell + -ing → selling','销售活动、销售中的状态'),
 'direct selling 直销，online selling 网络销售，a selling point 卖点。The shop is selling 是在出售，不一定整家店要被卖掉。',
 'direct selling；online selling；a key selling point。',
 'selling 活动、seller 卖家；sales 可说销售额或销售部门。a selling point 是吸引购买的优点，不是实体销售网点。',
 ('The company is selling its products online.','公司在网上销售产品。'),('The long battery life is the device’s main selling point.','电池续航长是这台设备的主要卖点。'))
W('seller','英 /ˈselə/；美 /ˈselər/','卖家；卖方；畅销程度某种的商品',
 '可以是卖东西的人或公司，也可以说某件东西卖得怎么样：a good seller 是好卖的产品。',
 'sell + -er，中古英语已有同族人物名词。-er 在商品用法里指被卖得怎样的对象，不只主动卖东西者。',SH('sell + -er → seller','出售者；某种销售表现的商品'),
 'a private seller 私人卖家，an online seller 网络卖家，a good seller 好卖的商品。',
 'a private seller；an online seller；a good seller。',
 'seller 卖方，buyer 买方；a good seller 看语境可说优秀销售者，也可说畅销货，不能全译成卖货能手。',
 ('Contact the seller if the package does not arrive.','包裹没到的话，请联系卖家。'),('The smaller model has been a good seller.','小型号一直卖得不错。'))
W('bestseller','英 /ˌbestˈselə/；美 /ˌbestˈselər/','畅销书；畅销产品',
 '卖得特别好的那一本书、那件产品；核心是销量表现。',
 'best 最好 + seller〔销售表现某种的商品〕，现代固定作畅销品名词。并不必然是全球第一名。',SH('best + seller → bestseller','卖得很好的书或产品'),
 'an international bestseller 国际畅销书，a bestseller list 畅销榜。一个商店的 bestseller 也可只在该店销量突出。',
 'an international bestseller；a bestseller list；become a bestseller。',
 'bestseller 说畅销，masterpiece 说杰作；销量好不自动证明质量最好。',
 ('Her first novel became an international bestseller.','她的首部小说成为国际畅销书。'),('The guide is still one of the shop’s bestsellers.','这本指南仍是店里的畅销书之一。'))
W('resell','/ˌriːˈsel/','转售；再次出售',
 '先买到或取得一件东西，再把它卖给下一位。',
 're- 再次 + sell，动词沿 sell 变化为 resold、resold。不是把原商品一定重新制造一遍。',SH('re- + sell → resell','再次卖出、转售'),
 'resell a ticket 转售票，resell used equipment 转售二手设备，resell at a profit 转卖获利。',
 'resell a ticket；resell used equipment；resell at a profit。',
 'resell 动作，resale 名词；转售对象可能没被实际使用过，所以 resale 不必等于 used 二手使用状态。',
 ('He bought the desk cheaply and resold it a year later.','他低价买下书桌，一年后转卖了。'),('The company buys used equipment to resell.','公司购入二手设备用于转售。'))
W('outsell','/ˌaʊtˈsel/','比……卖得多；销量超过',
 '把两种商品销量摆在一起比，一种卖的数量超过另一种。',
 'out- 胜过、超过 + sell。常见变化 outsold、outsold；这里 out- 不是卖到外面去。',SH('out- + sell → outsell','销售表现超过对方'),
 'outsell a rival 销量超过竞争对手，A outsells B by two to one A的销量是B的两倍。',
 'outsell a rival；outsell the previous model；outsell by two to one。',
 'outsell 比较销量，oversell 说卖过量或夸大；前缀 out- 与 over- 不是都能翻成外面卖。',
 ('The cheaper model outsold the premium version.','便宜型号的销量超过高配版。'),('Her new album outsold the previous one in its first week.','她的新专辑首周销量超过了上一张。'))
W('upsell','/ˌʌpˈsel/〔动词〕','劝顾客买更高价、更多或升级版本的产品',
 '顾客本来想买基础款，销售人员介绍升级版，让这笔购买往更高金额走。',
 'up- 向上、提高 + sell；商业上固定用于提高一次交易的价值，也可作名词，名词重音常更靠前。',SH('up- + sell → upsell','把顾客购买引向更高金额或升级方案'),
 'upsell a customer to a premium plan 引导顾客升级高价方案，an upsell offer 升级购买建议。',
 'upsell a customer；upsell to a premium plan；an upsell offer。',
 'upsell 侧重提高当前购买价值，cross-sell 常说搭配推销另一种商品；两个场景可重叠但重点不同。',
 ('The agent tried to upsell us to a larger room.','客服试着劝我们升级到更大的房间。'),('The app offers an upsell to the premium plan.','应用提供升级到高级方案的购买选项。'))
W('oversell','英 /ˌəʊvəˈsel/；美 /ˌoʊvərˈsel/','超卖；过度吹捧、推销',
 '座位只有一百个却卖了一百一十张，卖过量了；把效果夸得超过实际，也算说过头。',
 'over- 过度 + sell，分别发展出超过供应量、过度推销和夸大价值的用法。变化 oversold、oversold。',SH('over- + sell → oversell','卖出超过供应；推销或描述得过头'),
 'oversell a flight 超售航班座位，oversell an idea 过度吹捧想法，do not oversell your results 不要夸大成果。',
 'oversell a flight；oversell an idea；oversell the benefits。',
 'oversell 不等于 outsell 销量胜过；一个是超过适当界线，一个是比另一方卖得多。',
 ('The hotel had oversold its rooms for the weekend.','酒店把周末客房超售了。'),('The presentation oversold the benefits of the new system.','演示夸大了新系统的好处。'))
W('sellout','/ˈselaʊt/','售罄、满座的活动；为利益背弃原则的人或行为',
 '票全卖完是一种 sellout；把原则拿去换利益，也可被人批评为 sellout。',
 '动词短语 sell out 名词化连写。卖空与背弃原则两种固定用法，分别看库存和价值立场。',SH('sell out → sellout','售罄活动；另指为利妥协、出卖者'),
 'The concert was a sellout 演唱会票售罄，call someone a sellout 批评某人出卖原则。后一义带强烈评价。',
 'a complete sellout；a sellout concert；call someone a sellout。',
 'sell out 动词短语，sellout 一个词常作名词或修饰语；音乐人变得商业化也不自动事实性地等于出卖者。',
 ('The concert was a sellout within minutes.','演唱会几分钟内就售罄了。'),('Some fans called him a sellout after he changed his style.','他改变风格后，一些粉丝指责他为利益背弃原则。'),sources=['https://www.etymonline.com/word/sellout','https://en.wiktionary.org/wiki/sellout#English'])
SA=[['晚期古英语 sala；可能有古诺尔斯语 sala 影响','售卖行为，与 sell 同属旧日耳曼词族'],['现代 sale','销售、出售；降价促销，复数 sales 另有集合用法']]
def AH(f,m):return SA+[[f,m]]
W('sale','/seɪl/','出售、销售；促销、降价销售',
 'sell 是去卖的动作，sale 可以是一笔成交、一次出售，或商店打折卖货的活动。',
 '接中古英语 sale、晚期古英语 sala，可能受古诺尔斯语同形词影响。与 sell 是历史同族，不是今天 sell 随意换元音的名词规则。',SA,
 'for sale 待售，on sale 上市出售或打折促销，a summer sale 夏季促销。a sale of land 土地出售，未必降价。',
 'for sale；on sale；a summer sale；make a sale。',
 'for sale 表可买；on sale 英美、场景不同，可能只是开售，也可能降价。看到 sale 不都等于便宜。',
 ('The house next door is for sale.','隔壁房子在出售。'),('I bought the jacket in the summer sale.','我在夏季促销时买了这件夹克。'),sources=['https://www.etymonline.com/word/sale','https://en.wiktionary.org/wiki/sale#English'])
W('sales','/seɪlz/','销售活动；销售量、销售额；销售部门；多场促销',
 '把卖货工作、卖出的业绩作为一整块来看；也可以只是多笔 sale 的复数。',
 'sale + -s，复数形式又形成固定的行业、业绩集合用法。末尾读 /z/，不是另一个独立词根。',AH('sale + -s → sales','多笔销售 → 销售工作、总业绩、部门'),
 'work in sales 做销售，sales figures 销售数据，annual sales 年销售额，sales manager 销售经理。说金额还是件数要看单位。',
 'work in sales；sales figures；annual sales；a sales team。',
 'sales 通常说卖出金额或数量，不等于 profit 利润；销售收入再减成本等才涉及利润。',
 ('She works in sales for a software company.','她在一家软件公司做销售。'),('Sales rose by ten percent last quarter.','上季度销售额增长了百分之十。'))
W('resale','/ˈriːseɪl/','转售；再次出售',
 '上一位买家买入后，又卖给下一位的这一笔交易或行为。',
 're- 再次 + sale 名词，与动词 resell 对照。不是要求先修理、翻新才算转售。',AH('re- + sale → resale','再次出售的行为或交易'),
 'resale value 转售价值，for resale 供转售，the resale market 转售市场。未使用过的票也可能转售。',
 'resale value；for resale；the resale market。',
 'resale 名词、resell 动词；The car has good resale value 与 They resell cars 是两种结构。',
 ('The car has a strong resale value.','这款车转售时比较保值。'),('The tickets were bought for resale.','这些票买来是为了转售。'))
W('saleable','/ˈseɪləbl/','好卖的；具备出售条件的',
 '有人愿意买，或者整理到适合拿出去卖的状态；不是说已经卖完。',
 'sale + -able，另有 salable 拼写，尤见美式。后缀说可出售、适销，不自动说明销量已经很好。',AH('sale + -able → saleable〔也拼 salable〕','能找到买家、适合出售的'),
 'a saleable product 适销产品，a saleable condition 可出售状态，saleable skills 有市场价值的技能。',
 'a saleable product；saleable condition；saleable skills。',
 'saleable 能卖、适合卖，sold 已卖；bestselling 已体现畅销表现，不只是有可能卖掉。',
 ('The repair put the furniture back into saleable condition.','修理使家具恢复到可出售的状态。'),('The course aims to teach saleable skills.','课程旨在教授有市场需求的技能。'))
R('B2967','出售、推销与不同销售方向','SELL：交出去换钱；前缀说明再卖、胜过或过头','sell → sold、selling、seller → bestseller；再接 resell、outsell、upsell、oversell、sellout，关联名词 sale。',
 '古英语 sellan 早有给予、交付，收钱转让义后来成为中心。sale 是同族旧名词，比较字母能帮记，不能当现代随意换元音规则。',
 'sell—sold—sold；sell + -ing/-er；best + seller；re-/out-/up-/over- + sell；sell out → sellout。',
 [['动作、词形与人物','sell · sold · selling · seller · bestseller'],['再售与销售方向','resell · outsell · upsell · oversell · sellout'],['相关名词','sale · sales · resale · saleable']],
 'outsell 比对方卖得多，oversell 超量或夸大；upsell 提高购买金额；resell 动词与 resale 名词。',
 'The seller resold the book after it became a bestseller.\n\n这位卖家在那本书成为畅销书后又把它转售了。',
 'sell sold selling seller bestseller resell outsell upsell oversell sellout sale sales resale saleable')
R('B2786','出售行为、销售业绩与再售','SALE：卖这件事；SALES：销售工作和业绩','先关联动作 sell，再 sale → sales → resale、saleable；批发和预售已有精讲。',
 'sale 和 sell 同属旧日耳曼词族。sale 可指一般出售或降价活动，sales 的业绩义还需看数量、金额单位。',
 'sale → sales、saleable；re- + sale → resale；whole/pre- + sale → wholesale、presale。',
 [['动词与出售名词','sell · sale · sales'],['再售、可售与交易方式','resell · resale · saleable · wholesale · presale']],
 'for sale 待售；on sale 看地区与场景；sales 销售额不等于 profit；saleable 不等于已经 sold。',
 'The shop buys saleable used books for resale.\n\n店里购入适合出售的二手书来转售。',
 'sell sale sales resell resale saleable wholesale presale')
if __name__=='__main__':save('continuation_20261030_v',ROOTS,WORDS)
