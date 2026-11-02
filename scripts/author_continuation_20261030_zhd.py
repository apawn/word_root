"""Selling vocabulary: peddle, hawker, price marking and reselling."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
def S(word,base):
 return ['https://en.wiktionary.org/wiki/'+word+'#English','https://www.etymonline.com/word/'+base]
def M(word):
 return ['https://en.wiktionary.org/wiki/'+word+'#English','https://www.merriam-webster.com/dictionary/'+word.rstrip('s')]
EXISTING_ROOT_ADDITIONS={
 'C0980':dict(words='peddle peddles peddled peddling peddler peddlers'.split(),label='peddler 与 peddle：人物词比短动词更早',note='peddle 由较早 peddler 逆构；人物名经 pedelere、pedder 等材料，更远有接拉丁 pedarius 步行者等分析，也有篮筐词关系的不同分析。foot 线索只作可能分析，不把每一步都定死。'),
 'B3430':dict(words='hawk hawked hawking hawker hawkers'.split(),label='hawk 的叫卖线独立于鹰名',note='叫卖 hawk 由 hawker 逆构，人物词接低地德语叫卖、背负等材料；猎鹰 hawk 动词来自鹰名，清嗓 hawk 另多作拟声。现代同形不等于都由鹰抓猎物推来。'),
 'B3169':dict(words='mark markup markups markdown markdowns'.split(),label='markup、markdown：价格标高、标低形成的名词',note='markup 连着 mark up，写加价额，也有文本标记等用法；markdown 连着 mark down，写降价、降幅。分写短语的动词性与连写名词分开认，软件名 Markdown 另按专名理解。'),
 'B2967':dict(words='resell resells resold reselling reseller resellers'.split(),label='resell：再卖、转售及出售者',note='re- 再次 + sell，过去式、分词随 sell → sold 变 resold；reseller 加人物、机构尾 -er，不表示重新推销同一句话。'),
 'C1615':dict(words='vendor vendors'.split(),label='vendors：商贩，也可指供货公司',note='vendor 经盎格鲁法语接 vendre、拉丁 vendere 出售，人物词比英语 vend 更早；vendors 是复数，不把所有人物名都当现代英语现加 -or。'),
}
PEDDLE=[['较早 pedder、pedelere 等人物名 → peddler','走动卖小货的人；远源有步行者、篮筐材料等不同分析'],['较早人物词 → 逆构 peddle 动词','把小贩活动理解为叫卖、兜售；现代也比喻散布说法']]
HAWK=[['低地德语等叫卖、背负材料 → hawker','流动叫卖者的人物词'],['hawker → 逆构 hawk 叫卖动词','鹰名、猎鹰动词和清嗓同形材料另走各自的线']]
MARKUP=[['mark up、mark down：给价格、文字作相应标记','价格向上或向下调整；文本注记依对象认'],['短语相关名词 → markup、markdown','连写名词写加价、降价等；文本 markup 也有独立的具体发展']]
RESELL=[['古英语 sellan → sell','较早可说给予、交付，后来出售意义固定'],['re- 再次 + sell → resell','重新卖出、转售；sell → sold 的变化保留在 resold']]
W('peddle','/ˈpedəl/','沿路、到处兜售；散布某种说法',
 '带着小货，换个街角再找下一位顾客，是 peddle。把不可靠说法到处推，也能像兜售商品一样叫 peddle。',
 '从较早 peddler 小贩人物词逆构而来，人物词的远源有不同分析。现代先学较短 peddle 方便，但历史不是先有英语短动词才造 peddler。',PEDDLE,
 'peddle fruit 兜售水果；peddle stories 到处散布说法；peddle goods 卖小货。',
 'peddle from door to door 挨门兜售；peddle false claims 散布不实说法。',
 'peddle 是兜售，pedal 是踏自行车脚踏；读音接近，却不是同一现代动词，拼写要按动作认。',
 ('They peddle fruit near the station.','他们在车站附近兜售水果。'),('Some websites peddle stories that have never been checked.','有些网站到处散布未经核实的说法。'),sources=S('peddle','peddle'))
W('peddles','/ˈpedəlz/','兜售、散布〔第三人称单数〕',
 '他推着小车，走到哪儿卖到哪儿，叫 he peddles；某个账号一直推不可靠故事，也可用这个词表达批评。',
 'peddle + -s，/l/ 后读 /z/；现代屈折加在逆构而来的动词后，不能反过来推人物词一定更晚。',PEDDLE+[['peddle + -s → peddles','他或它兜售、散布']],
 'peddles snacks 兜售零食；peddles misinformation 散布错误信息。',
 'peddles handmade goods；peddles promises 到处推销承诺。',
 'peddles false stories 带散布、兜售的批评意味，reports a story 只说报道；评价色彩不同。',
 ('He peddles snacks from a small cart.','他推着小车兜售零食。'),('The account peddles false stories for attention.','那个账号为了博关注散布不实故事。'),sources=S('peddles','peddle'))
W('peddled','/ˈpedəld/','兜售、散布了',
 '沿街把带来的小货卖给路人，过去做过就是 peddled；宣传一种被怀疑的故事、承诺，也能用它。',
 'peddle 去 e 加完整 -ed，/l/ 后读 /d/；不另加 /ɪd/ 音节。',PEDDLE+[['peddle + -ed → peddled','过去流动兜售，或到处推某种说法']],
 'peddled fruit 卖水果；peddled rumours 散布传言。',
 'peddled from house to house；peddled goods in the market。',
 'peddled 常带流动卖小货、到处推销的感觉，sold 范围更广；大宗正式交易不一定适合突出 peddled 的画面。',
 ('As a student, he peddled fruit to earn extra money.','学生时代，他靠卖水果赚些外快。'),('The brochure peddled an unrealistic picture of village life.','那本宣传册推销了一幅不切实际的乡村生活图景。'),sources=S('peddled','peddle'))
W('peddling','/ˈpedlɪŋ/','正在兜售、散布；流动售货活动',
 '街头来回卖货的过程，是 peddling；把观点当商品到处推，也用这个词。它常让人注意卖的人在不断找听众、买家。',
 'peddle 去 e 加 -ing，常读 /ˈpedlɪŋ/；可作动作形式，也作活动名词。',PEDDLE+[['peddle + -ing → peddling','兜售活动，或正在推销、散布']],
 'street peddling 街头兜售；peddling souvenirs 卖纪念品。',
 'peddling rumours 散布传言；peddling goods on the pavement。',
 'peddling 是兜售，pedalling、pedaling 是踩踏板；两种拼写对应不同动作，即使读音很像。',
 ('She earned money by peddling handmade bracelets.','她靠兜售手工手链赚钱。'),('The article accused him of peddling rumours.','文章指责他散布传言。'),sources=S('peddling','peddle'))
W('peddler','英 /ˈpedlə/；美 /ˈpedlɚ/','流动小贩；散布、兜售某种说法的人',
 '带着一包小货，走街串巷寻找顾客的人，是 peddler。peddler of rumours 则把传言看成他到处兜售的货。',
 '较早有 pedder、pedelere 等人物形式，远源有步行者、篮筐材料等分析；后来反而由人物词逆构 peddle。现代可用 peddle 对应 -er 认形，不把这种学习拆法当成确切历史先后。',PEDDLE+[['较早 peddler → peddle；现代对应动作与做事者','学习可以从动作到人物，历史人物名更早']],
 'a street peddler 街头小贩；a peddler of lies 谎言散布者。',
 'a fruit peddler 水果小贩；a travelling peddler 流动小贩。',
 'peddler 常是流动兜售小货的人，shopkeeper 是经营店铺的人；角色和售货方式不相同。',
 ('A peddler was selling combs and ribbons near the gate.','一位小贩在门口附近卖梳子和丝带。'),('The newspaper called him a peddler of false hope.','报纸称他是虚假希望的兜售者。'),sources=S('peddler','peddler'))
W('peddlers','英 /ˈpedləz/；美 /ˈpedlɚz/','流动小贩；某类说法的兜售者〔复数〕',
 '市场附近带货行走、四处找顾客的小贩，是 peddlers。商品可以是看得见的小物，也能在比喻里是传言、空头希望。',
 'peddler + -s，读 /z/；人物词比 peddle 动词更早，复数是现代英语正常加出的这一层。',PEDDLE+[['peddler + -s → peddlers','多位流动小贩，或比喻的兜售者']],
 'street peddlers 街头小贩；peddlers of misinformation 错误信息散布者。',
 'fruit peddlers 水果小贩；travelling peddlers。',
 'peddlers 可以泛说流动卖小货的人，不一定都在卖假货；商品是否可靠须看语境，不能从词本身断定。',
 ('Street peddlers lined the road outside the station.','车站外的路边排着街头小贩。'),('The article criticised peddlers of false promises.','文章批评了那些到处兜售虚假承诺的人。'),sources=S('peddlers','peddler'))
W('hawked','英 /hɔːkt/；美 /hɔkt/','叫卖、兜售了；〔另一词义〕放鹰捕猎、清嗓了',
 '商贩在人群中喊着卖报纸，是 hawked newspapers。这里跟鹰捕猎没有必然联系，是另一个来源的叫卖动词。',
 'hawk + 完整 -ed，/k/ 后读 /t/。叫卖义由 hawker 逆构；同形词还可指放鹰捕猎或清嗓，分别来自鹰名、拟声等材料。',HAWK+[['hawk + -ed → hawked','过去叫卖、兜售；其他同形动词依语境另认']],
 'hawked newspapers 叫卖报纸；hawked goods in the street 沿街叫卖。',
 'hawked fruit at the market；hawked his ideas 到处推销想法。',
 'hawked newspapers 是卖报，hunted with a hawk 是放鹰捕猎；不能见到 hawk 就自动翻成鸟类动作。',
 ('Vendors hawked cold drinks outside the stadium.','商贩在体育场外叫卖冷饮。'),('He hawked newspapers as a boy.','他小时候叫卖过报纸。'),sources=S('hawked','hawk'))
W('hawking','英 /ˈhɔːkɪŋ/；美 /ˈhɔkɪŋ/','正在叫卖、兜售；〔另一词义〕放鹰捕猎、清嗓',
 '在公交车站来回招呼乘客买水、零食，是 hawking。若读到 hawking 的野外狩猎场景，才按放鹰捕猎理解。',
 'hawk + -ing。叫卖动词由 hawker 逆构，不从鹰名直接产生；放鹰捕猎同形动词、清嗓同形动词另有来源。',HAWK+[['hawk + -ing → hawking','相应动词的过程形式，先看具体义项']],
 'hawking souvenirs 叫卖纪念品；hawking goods 兜售货物。',
 'hawking food outside the station；hawking products online 网上卖力推销产品。',
 'hawking 常让人想到沿街叫卖、卖力推销，selling 更中性广泛；网店也可被形容为 hawking，但语气会更有推销感。',
 ('A man was hawking umbrellas outside the station.','一个男人在车站外叫卖雨伞。'),('She disliked the constant hawking of products during the show.','她不喜欢节目里没完没了地推销产品。'),sources=S('hawking','hawk'))
W('hawker','英 /ˈhɔːkə/；美 /ˈhɔkɚ/','沿街叫卖者、流动摊贩',
 '在街边、市场或车站附近招呼顾客买货的人，可以叫 hawker。它突出流动售货、叫卖的角色，不是鹰的饲养者的唯一解释。',
 '售货人物 hawker 接低地德语等叫卖、背负材料，早于英语 hawk 叫卖动词；现代可对应 hawk 与 -er 认形，但不能把历史顺序倒过来。',HAWK+[['较早 hawker → 英语 hawk 叫卖动词','人物词在前，短动词由它逆构']],
 'a street hawker 街头商贩；a food hawker 叫卖食品的人。',
 'a hawker selling fruit；hawker stalls 小贩摊位。',
 'hawker 和 peddler 日常可接近；部分旧定义区分是否用车，但现代句子别凭它断定对方一定有马车、货车。',
 ('A hawker offered us fresh mangoes near the market.','市场附近，一位商贩向我们兜售新鲜芒果。'),('The street hawker packed up his stall at sunset.','日落时，那位街头商贩收起了摊位。'),sources=S('hawker','hawk'))
W('hawkers','英 /ˈhɔːkəz/；美 /ˈhɔkɚz/','沿街叫卖者、流动摊贩〔复数〕',
 '街头几位商贩一边招呼一边卖小货，是 hawkers。词里的角色感来自他们售货，不是因为都像鹰一样叫。',
 'hawker + -s，读 /z/；售货人物词较早接低地德语材料，不把 hawk 鸟名加人物尾当作这条词源。',HAWK+[['hawker + -s → hawkers','多位沿街、流动售货者']],
 'street hawkers 街头商贩；food hawkers 食品摊贩。',
 'hawkers near the station；licensed hawkers 有许可的商贩。',
 'hawkers 是卖东西的人，customers 是买东西的人；vendor 也可指公司，hawkers 通常更像具体街头售货者。',
 ('Hawkers were selling flowers outside the theatre.','商贩们在剧院外卖花。'),('The market was crowded with hawkers and shoppers.','市场里挤满商贩和购物的人。'),sources=S('hawkers','hawk'))
W('markup','英 /ˈmɑːkʌp/；美 /ˈmɑrkʌp/','加价额、加价幅度；文本标记',
 '货进来花十元，定价时再往上加三元，这多出的三元是 markup。文本里的 markup 则是给文字加的结构、显示标记，换了对象也要换理解。',
 '与短语 mark up 相连形成名词。价格义是把标价抬高；文本义是给文字内容加标记，两条具体用法分别认，不把技术文本里的 up 硬译成涨价。',MARKUP,
 'a retail markup 零售加价；a markup on goods 商品加价；markup language 标记语言。',
 'a small markup；remove markup from text 去掉文本中的标记。',
 'markup 是加在成本上的金额或比例，profit 还需看其他费用；在语言学习里先别把所有售价与进价之差直接叫最终净利润。',
 ('The shop adds a small markup to the wholesale price.','商店在批发价上加一小部分作为售价。'),('The tool removes markup and leaves only the plain text.','工具去掉标记，只留下纯文本。'),sources=['https://en.wiktionary.org/wiki/markup#English','https://www.merriam-webster.com/dictionary/markup'])
W('markups','英 /ˈmɑːkʌps/；美 /ˈmɑrkʌps/','加价额、加价幅度〔复数〕；多套标记等',
 '不同店、不同商品各加一截价格，把这些加价拿来比较，就用 markups。别把这里连写的名词看成动词 marks up。',
 'markup + -s，/p/ 后读 /s/；内层名词来自 mark up 短语。文本标记义常作集合概念，这里先抓最常见的价格复数。',MARKUP+[['markup + -s → markups','多笔、不同商品或不同商家的加价']],
 'high markups 高加价；retail markups 零售加价幅度。',
 'compare markups 比较加价；markups on accessories 配件的加价。',
 'markups 向上加价，markdowns 向下降价；都是连写名词，动作一般分写 mark up、mark down。',
 ('The report compared markups on everyday goods.','报告比较了日常商品的加价幅度。'),('Luxury shops often charge higher markups on accessories.','奢侈品店的配件往往有较高加价。'),sources=['https://en.wiktionary.org/wiki/markups#English','https://www.merriam-webster.com/dictionary/markup'])
W('markdown','英 /ˈmɑːkdaʊn/；美 /ˈmɑrkdaʊn/','降价；降价额、降幅',
 '价签原来写一百，现在划掉改成八十，这次往下调的价格就是 markdown。重点是从原来的售价降下来。',
 '与 mark down 把标价调低的短语相连形成名词，名词记录晚于短语。另有 Markdown 文本格式专名，不是购物降价的意思。',MARKUP+[['mark down → markdown','把价格标低的动作形成降价名词；专名另按文本语境识别']],
 'a markdown on coats 外套降价；a substantial markdown 大幅降价。',
 'a seasonal markdown 换季降价；a markdown from the original price。',
 'a markdown 是降价这件事或降价幅度，mark down 分写时是动词短语；句子 The shop will mark down the price 不能把动词直接连写。',
 ('The coat was available at a substantial markdown.','那件外套大幅降价出售。'),('The markdown reduced the price from eighty dollars to sixty.','这次降价把价格从八十美元降到了六十。'),sources=['https://en.wiktionary.org/wiki/markdown#English','https://www.merriam-webster.com/dictionary/markdown'])
W('markdowns','英 /ˈmɑːkdaʊnz/；美 /ˈmɑrkdaʊnz/','多次、各类商品的降价；各项降幅',
 '店里不只一件打折，而是鞋、衣服等各自降价，把这些降价活动或降幅一起说，就是 markdowns。',
 'markdown + -s，读 /z/；内层名词对应 mark down 短语，现代复数把各次、各项降价数出来。',MARKUP+[['markdown + -s → markdowns','多次降价、多项降价幅度']],
 'seasonal markdowns 换季降价；deep markdowns 大幅降价。',
 'markdowns on winter clothing 冬装降价；further markdowns 进一步降价。',
 'markdowns 只说明价格下调，sales 在促销语境可说降价活动，在其他语境又是销售额；看清它出现在什么句子。',
 ('The store announced markdowns on winter clothing.','商店宣布冬装降价。'),('Further markdowns helped clear the remaining stock.','进一步降价帮助清掉了剩余库存。'),sources=['https://en.wiktionary.org/wiki/markdowns#English','https://www.merriam-webster.com/dictionary/markdown'])
W('resells','/ˌriːˈselz/','再卖、转售〔第三人称单数〕',
 '买来的旧自行车修好，再卖给下一位买家，是 resells。re- 的再次落在出售动作上，不要求原卖家把同一辆车收回。',
 'resell + -s，/l/ 后读 /z/；内层 re- 再次 + sell 出售。sell 的较早给予、交付材料后来发展出出售义。',RESELL+[['resell + -s → resells','他或它再次卖出、转售']],
 'resells used bikes 转售旧自行车；resells goods online 网上转售商品。',
 'resells refurbished equipment 转售翻新设备；resells to customers。',
 'resells 是再卖出去，resale 是转售名词；They resell bikes 与 bikes for resale 的语法位置不同。',
 ('The shop repairs old bicycles and resells them.','店里修好旧自行车，再把它们卖出去。'),('She resells second-hand furniture online.','她在网上转售二手家具。'),sources=S('resells','resell'))
W('resold','英 /ˌriːˈsəʊld/；美 /ˌriːˈsoʊld/','转售、再次卖出了',
 '一张票、一本旧书从原买家手里又卖给别人，就是 was resold。词只交代再卖，不保证卖得比以前贵。',
 'resell 的过去式、过去分词，保留 sell → sold 的内部变化，前面的 re- 不变；不是现代 resell 加 -ed。',RESELL+[['resell → resold','随 sell → sold 变化的过去式、分词']],
 'resold at a profit 转售获利；resold at a loss 转售亏损。',
 'was resold online；resold to another buyer。',
 'resold 只说再卖，returned 是退回；把货退给商家不自动等于自己转售给了下一位买家。',
 ('The book was resold to a collector a year later.','一年后，那本书被转售给一位收藏者。'),('He resold the bicycle for less than he had paid.','他转卖自行车时，价格比买入时低。'),sources=S('resold','resell'))
W('reselling','/ˌriːˈselɪŋ/','正在转售；转售活动',
 '把已经买来、拿到的东西再卖出去，整项活动就叫 reselling。它可以是二手货，也可以是为转卖而买入的新货。',
 'resell + -ing；内层 re- 再次 + sell，词基原有的 ll 保留。',RESELL+[['resell + -ing → reselling','再次出售的过程、业务活动']],
 'reselling used equipment 转售二手设备；reselling online 网上转售。',
 'a business of reselling books；reselling new products 转售新品。',
 'reselling 不一定只卖二手货；second-hand goods 通常突出别人拥有、用过的货品，reselling 则突出再次销售的动作。',
 ('She started a small business reselling used cameras.','她开始做转售二手相机的小生意。'),('The company buys surplus stock for reselling online.','公司买入积压库存，用于网上转售。'),sources=S('reselling','resell'))
W('reseller','英 /ˌriːˈselə/；美 /ˌriːˈselɚ/','转售者；经销商、转售商',
 '从上游拿到产品，再卖给客户的人或公司，是 reseller。可以卖旧货，也可以按授权卖全新的设备、软件。',
 'resell + -er；人物、机构尾把再次出售的动作变成角色名称。可以对应 resale 转售名词一起认。',RESELL+[['resell + -er → reseller','做转售的人或机构']],
 'an authorised reseller 授权转售商；a software reseller 软件经销商。',
 'buy from a reseller 向转售商购买；an online reseller 网上转售商。',
 'reseller 强调从别处取得产品再销售，manufacturer 强调制造产品；同一企业可能兼有角色，但词关注点不同。',
 ('We bought the equipment from an authorised reseller.','我们向一家授权经销商购买了设备。'),('The reseller offers several brands of refurbished laptops.','这家转售商提供几个品牌的翻新笔记本电脑。'),sources=S('reseller','resell'))
W('resellers','英 /ˌriːˈseləz/；美 /ˌriːˈselɚz/','转售者、经销商〔复数〕',
 '厂商自己不直接面对所有客户，而是把货交给多家经销商再卖，这些公司就是 resellers。',
 'reseller + -s，读 /z/；内层 resell 再卖 + -er 人物、机构尾，再加复数。',RESELL+[['reseller + -s → resellers','多家转售商、多个转售者']],
 'authorised resellers 授权经销商；independent resellers 独立转售商。',
 'a network of resellers 转售商网络；online resellers。',
 'resellers 不自动等于 scalpers 黄牛；是否有抬价囤货等行为须看语境，正规的产品经销也可用 resellers。',
 ('The manufacturer supplies products to resellers across the country.','制造商向全国各地的经销商供货。'),('Customers can compare prices from several resellers.','顾客可以比较几家转售商的价格。'),sources=S('resellers','resell'))
W('vendors','英 /ˈvendəz/；美 /ˈvendɚz/','商贩、卖方；供应商、供货公司〔复数〕',
 '街边卖水果的人可以是 vendors，给企业提供软件的公司也可以是 vendors。共同点是站在出售、供货这一边，规模可以差很多。',
 'vendor + -s，读 /z/；vendor 经盎格鲁法语接 vendre、拉丁 vendere，人物词记录早于英语 vend，不能只讲现代 vend 加 -or 的先后。',
 [['拉丁 vendere 出售 → 盎格鲁法语 vendor 等 → vendor','卖方人物名称先于英语 vend 的较晚记录'],['vendor + -s → vendors','多位商贩、多家供货公司']],
 'street vendors 街头商贩；software vendors 软件供应商；approved vendors 获认可的供应商。',
 'compare vendors 比较供应商；local food vendors 本地食品商贩。',
 'vendors 指卖方、供货方，buyers 指买方；vendor 不要求有固定商店，也不要求只是一个人。',
 ('Street vendors sold fruit and hot snacks near the station.','街头商贩在车站附近卖水果和热食。'),('The team compared proposals from three software vendors.','团队比较了三家软件供应商的方案。'),sources=S('vendors','vendor'))
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_zhd',ROOTS,WORDS)
 extend_lessons()
