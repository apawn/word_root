"""Ship: vessels, transport, crews and a Dutch cousin."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
S=[['古英语 sċip → 中古英语 schip 等 → ship','船；更远来源的劈木解释不作定论'],['动词 ship 及现代复合词','用船运输 → 不限交通方式的发运；船舶类型与人员']]
def H(f,m):return S+[[f,m]]
W('ship','/ʃɪp/','船；发运、运送；交付产品',
 '名词先想一艘船，动词再想把货发出去；今天 ship a parcel 不要求包裹真的坐船。',
 '船名词继承古英语 sċip，运输动词也有古老历史。现代发运义扩大到陆路、航空，软件里还借为交付发布。粉丝语境 ship 某对人物是 relationship 截短形成的另一用法，后缀 -ship 也另有来源。',S,
 'a cargo ship 货船，ship an order 发出订单货物，ship a product 交付产品；名词 ship 与船的大小没有一条能覆盖所有语境的简单分界。',
 'a cargo ship；ship an order；ship overseas；ship a product。',
 'ship 运输动词不限定海运，sail 更直接说船航行；friendship 的 -ship 不是朋友组成的一艘船。',
 ('The shop ships orders within two days.','商店在两天内发出订单货物。'),('A large ship entered the harbour at dawn.','一艘大船在黎明时驶入港口。'))
W('shipping','/ˈʃɪpɪŋ/','运输、发货；运费；航运业',
 '买东西时常指把货送到你手里的过程、服务或费用；行业报道中也可说整个航运。',
 'ship 双写 p + -ing，形成运输活动名词、动词形式。运输方式扩大后，电商 shipping 同样不限定船运。',H('ship + -ing → shipping','发运活动 → 发货、运输、运费；航运业'),
 'free shipping 免运费，shipping costs 运费，the shipping industry 航运业；不同搭配范围不同。',
 'free shipping；shipping costs；shipping address；the shipping industry。',
 'shipping 常含发运、运输过程，delivery 更聚焦送达；两词在商店说明中也有重合，不硬定所有店铺的费用范围。',
 ('The price includes free shipping.','价格包含免运费服务。'),('Please check the shipping address before paying.','付款前请核对收货地址。'))
W('shipment','/ˈʃɪpmənt/','一批货；装运、发货',
 '把一起发出的一批货看成一个整体；也可以说安排发货这件事。',
 'ship + -ment，形成行为、结果名词。现代可数 a shipment 常指一批运送的货物。',H('ship + -ment → shipment','装运 → 装运行为或一批发运货物'),
 'a shipment of books 一批书，a delayed shipment 延误的货，prepare for shipment 准备装运。',
 'a shipment of；a large shipment；ready for shipment。',
 'shipping 常指运输服务、活动或费用，a shipment 常是具体一批货；不能一律按中文运输替换。',
 ('A new shipment of books arrived this morning.','今天早上新到了一批书。'),('The goods are packed and ready for shipment.','货已打包，随时可以发运。'))
W('shipper','英 /ˈʃɪpə/；美 /ˈʃɪpər/','发货人；托运人；运输业务机构',
 '站在货物这一边，负责把货交出去发运的人或机构；不一定是开船、开车的人。',
 'ship 双写 p + -er，按发运主体形成名词。行业合同与普通商业介绍的范围可能不同，读具体角色。',H('ship + -er → shipper','执行、安排发运的主体 → 发货人、托运方'),
 'the shipper’s address 发货人地址，a major shipper 大型发运客户或运输业务机构；具体意思看行业上下文。',
 'the shipper’s address；a major shipper；the shipper and receiver。',
 'shipper 托运方与 carrier 承运方通常是不同角色；skipper 船长是另一借词，不是 shipper 拼错。',
 ('The label lists the shipper and the receiver.','标签上列有发货人和收货人。'),('The shipper arranged collection from the warehouse.','托运方安排从仓库提货。'))
W('dropship','/ˈdrɒpʃɪp/；美 /ˈdrɑːpʃɪp/','代发货；直接从供应方发给顾客',
 '店家接到订单，货不用先到店家手里，而由供应方直接发给顾客。',
 'drop + ship，组合为直接发运的商业动词。游戏里 dropship 也可指运送、投放人员的飞行载具，需按上下文分义。',H('drop + ship → dropship','直接发运 → 供应方代发；另有载具名词'),
 'dropship products 代发商品，a dropshipping business 代发货业务；这里只讲物流关系，不把它当保证赚钱的方法。',
 'dropship products；dropship orders；a dropshipping supplier。',
 'dropship 说供应方直发的履约方式，不等于所有网上卖货；shipping 是更宽泛的发运服务。',
 ('The supplier dropships the orders directly to customers.','供应商把订单商品直接发给顾客。'),('The retailer chose to dropship some larger items.','零售商选择让供应方直接发运部分大件商品。'))
W('shipyard','英 /ˈʃɪpjɑːd/；美 /ˈʃɪpjɑːrd/','船厂',
 '造船、修船的作业场地，不是船上供人散步的院子。',
 'ship + yard 作业场、场地，按造修船用途组合。yard 在这里不取相当于三英尺的长度单位义。',H('ship + yard → shipyard','船舶作业场 → 船厂'),
 'a naval shipyard 海军船厂，work at a shipyard 在船厂工作；造船和维修都可涉及。',
 'a shipyard worker；a naval shipyard；work at a shipyard。',
 'shipyard 造修船场地，harbour 港湾、港口水域；船会在港口停靠，但不是每个港口都有船厂。',
 ('The vessel is being repaired at a local shipyard.','这艘船正在当地船厂维修。'),('The shipyard employs hundreds of skilled workers.','这家船厂雇用数百名技术工人。'))
W('shipbuilder','英 /ˈʃɪpbɪldə/；美 /ˈʃɪpbɪldər/','造船工；造船商、造船企业',
 '把船造出来的人或公司；-er 可以是一整个企业，不只站在现场的一个工人。',
 'ship + builder 建造者，按造船职责组合；与 shipbuilding 造船业、造船活动一起学。',H('ship + builder → shipbuilder','建造船舶的主体 → 造船者、造船商'),
 'a major shipbuilder 大型造船商，a skilled shipbuilder 熟练造船工；先看所说对象是人还是企业。',
 'a major shipbuilder；a skilled shipbuilder；a commercial shipbuilder。',
 'shipbuilder 造船，shipowner 拥有船，skipper 指船长；同一人可能兼任，但词义分工清楚。',
 ('The shipbuilder received an order for two ferries.','这家造船商接到了两艘渡轮的订单。'),('Her grandfather worked as a shipbuilder.','她的祖父曾是一名造船工。'))
W('shipowner','英 /ˈʃɪpəʊnə/；美 /ˈʃɪpoʊnər/','船主；船舶所有者',
 '这艘船归谁所有，就从所有权角度称谁 shipowner；可能是个人，也可能是公司。',
 'ship + owner 所有者，形成船主名词。日常意义与具体登记、经营安排要分开，词本身不交代全部法律关系。',H('ship + owner → shipowner','船的所有者 → 船主'),
 'a private shipowner 私人船主，the shipowners’ association 船主协会。',
 'a private shipowner；a commercial shipowner；a shipowners’ association。',
 'shipowner 是拥有船的主体，captain 或 skipper 是负责指挥船的人；船长不一定拥有船。',
 ('The shipowner approved the repairs.','船主批准了维修。'),('The association represents local shipowners.','协会代表本地船主。'))
W('shipmate','/ˈʃɪpmeɪt/','同船伙伴；同船船员',
 '在同一艘船上一起工作、航行的人，强调彼此是船上的伙伴。',
 'ship + mate 伙伴，组合成同船伙伴。mate 在航海里也有具体副手职务，但 shipmate 本身不自动指定军衔或岗位。',H('ship + mate → shipmate','同船的伙伴 → 同船船员'),
 'an old shipmate 旧日同船伙伴，former shipmates 曾经同船的人；也可用于船友之间的称呼。',
 'an old shipmate；former shipmates；help a shipmate。',
 'shipmate 同船伙伴，roommate 同住伙伴；mate 作为职务时可能是大副等，但整词不能直接译大副。',
 ('He kept in touch with his old shipmates.','他一直与从前的同船伙伴保持联系。'),('A shipmate helped her secure the equipment.','一位同船伙伴帮她固定好设备。'))
W('skipper','英 /ˈskɪpə/；美 /ˈskɪpər/','船长；队长；担任船长、队长',
 '带着一条船或一支队伍前进的人；体育报道里也常用来叫队长。',
 '船长义借中古荷兰语 scipper、schipper，其 ship 对应词加人物后缀，与英语 shipper 是同源构词的不同进入路线。另有从 skip 跳跃形成的同形词，不拿来解释船长。',S[:1]+[['中古荷兰语 scipper、schipper → 英语 skipper','船相关的人物名 → 船长；扩展队长']],
 'the boat’s skipper 船长，the team skipper 队长；skipper a yacht 可作动词说驾驶、指挥游艇。',
 'the boat’s skipper；the team skipper；skipper a yacht。',
 'skipper 船长、队长，shipper 发货人；发音和词形都不同。体育中 skipper 不必指教练。',
 ('The skipper decided to return to harbour.','船长决定返港。'),('The team’s skipper scored the winning goal.','球队队长打进了制胜球。'))
W('flagship','/ˈflæɡʃɪp/','旗舰；最具代表性的主打产品、机构',
 '舰队里，指挥官所在的船有识别旗；商业里就借它说最拿得出手、代表实力的那一个。',
 'flag 旗 + ship 船，先指舰队指挥官所在、悬挂相应标志的船，再引申为同类中的主力代表。',H('flag + ship → flagship','指挥官所在的舰船 → 主打代表'),
 'a flagship store 旗舰店，a flagship product 主打产品，a flagship programme 重点项目；产品是比喻，不必真有船。',
 'a flagship store；a flagship product；a flagship programme。',
 'flagship 重点是最具代表性，不自动保证销量最高或价格最低；在海军语境有实际指挥舰含义。',
 ('The company opened a flagship store in the city centre.','公司在市中心开了一家旗舰店。'),('The new phone is the brand’s flagship product.','这款新手机是该品牌的主打产品。'))
W('battleship','/ˈbætəlʃɪp/','战列舰',
 '不是任何能打仗的船，而是以重炮、厚装甲著称的一类大型军舰，历史海战中很重要。',
 'battle 战斗 + ship，现代作为具体军舰类型成词；名字可按战斗船帮助记忆，但分类比字面更窄。',H('battle + ship → battleship','战斗舰船名称 → 战列舰类型'),
 'a historic battleship 历史战列舰，a battleship museum 战列舰博物馆；同名棋盘游戏也常见。',
 'a historic battleship；a battleship museum；a naval battleship。',
 'warship 军舰是大类，battleship 战列舰是其中一种；航空母舰、驱逐舰不是都叫 battleship。',
 ('The old battleship is now open to the public as a museum.','这艘旧战列舰如今作为博物馆对公众开放。'),('The book compares battleships with other types of warship.','这本书比较了战列舰与其他种类的军舰。'))
W('gunship','/ˈɡʌnʃɪp/','武装直升机、武装飞机；炮艇',
 '按搭载武器的火力用途来叫载具；现代新闻里常是直升机或飞机，并非一看到 ship 就一定是海船。',
 'gun 火炮、枪 + ship 载具，先有武装船艇等义，后来用于配备火力的航空载具。具体是哪一类要看 helicopter、aircraft 等上下文。',H('gun + ship → gunship','武装载具 → 炮艇；武装航空载具'),
 'a helicopter gunship 武装直升机，an aircraft gunship 武装飞机；学习识别载具名，不从词义推出具体型号。',
 'a helicopter gunship；an aircraft gunship；a gunship in a museum。',
 'gunship 不能一概译炮舰，现代常见航空义；battleship 则是特定海军舰船类型。',
 ('The documentary shows a helicopter gunship from that period.','纪录片展示了那个时期的一架武装直升机。'),('The museum has a retired gunship on display.','博物馆展出了一架退役武装飞机。'))
W('steamship','/ˈstiːmʃɪp/','蒸汽船；轮船',
 '用蒸汽机推动的船，名字抓动力来源，不是船上做饭时冒了一点蒸汽。',
 'steam 蒸汽 + ship 船，按蒸汽动力组合。中文轮船有时泛指机动大船，英文 steamship 的蒸汽动力更具体。',H('steam + ship → steamship','蒸汽动力的船 → 蒸汽船'),
 'an ocean steamship 远洋蒸汽船，a historic steamship 历史蒸汽船；现代各种动力货轮不要都叫 steamship。',
 'a historic steamship；an ocean steamship；steamship travel。',
 'steamship 按动力命名，cargo ship 按运输用途命名；同一艘船可能同时属于两种描述。',
 ('The steamship carried passengers across the ocean.','这艘蒸汽船载着乘客横渡大洋。'),('The restored steamship now offers short harbour trips.','这艘修复后的蒸汽船如今提供港内短途游览。'))
W('shipwreck','/ˈʃɪprek/','海难；失事船只、沉船残骸；使船失事',
 '既可以说船遭难这件事，也可以说留下来的失事船体、残骸；上下文决定是哪一个。',
 'ship + wreck 失事、毁坏物，组合有事件与结果两种名词义，也作动词。不要把 wreck 当一段没有意义的尾巴。',H('ship + wreck → shipwreck','船失事 → 海难；失事船及残骸'),
 'survive a shipwreck 在海难中幸存，explore a shipwreck 探查沉船；be shipwrecked 是遭遇船难、船只失事。',
 'survive a shipwreck；a historic shipwreck；a shipwreck site。',
 'a shipwreck 不一定只指完整沉在水下的船，也可说失事事件或残骸；wreck 的范围还包括车等。',
 ('The divers photographed an old shipwreck near the coast.','潜水员拍摄了近岸的一艘旧沉船。'),('The story follows two people who survive a shipwreck.','故事讲述两名海难幸存者的经历。'))
R('B3315','船舶、运输与船上人员','SHIP：从船到发运，再分用途、动力和职责','先把 ship、shipping、shipment、shipper 的动作与角色排在一起，再看造船、船主、船长与各种船名。',
 '船舶词继承古英语 sċip，现代发运义不限定海运。skipper 船长经荷兰语相关形式借入；relationship 截短的粉丝 ship 和 -ship 后缀分别另源。',
 'ship → shipping、shipment、shipper；drop + ship；ship + yard、builder、owner、mate；flag、battle、steam、war、air、space、star + ship；ship + wreck。',
 [['发运过程、货物与主体','ship · shipping · shipment · shipper · dropship'],['造船与船上职责','shipbuilding · shipyard · shipbuilder · shipowner · shipmate · skipper · shipboard'],['代表、用途与动力','flagship · battleship · warship · gunship · steamship · airship'],['航天载具与事故','spaceship · starship · shipwreck']],
 'shipper 不是 skipper；shipping 不限海运；battleship 是战列舰，不是全部军舰；gunship 现代可指航空载具。',
 'The shipbuilder delivered the vessel to its new shipowner.\n\n造船商把船交付给新船主。',
 'ship shipping shipment shipper dropship shipbuilding shipyard shipbuilder shipowner shipmate skipper shipboard flagship battleship warship gunship steamship airship spaceship starship shipwreck')
if __name__=='__main__':save('continuation_20261029_dz',ROOTS,WORDS)
