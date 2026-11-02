"""Bid, dust and meal: offers, two-way dusting and two different meals."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
B=[['古英语 biddan 与 bēodan','请求、要求；提供、宣布，两套旧动词'],['中古英语至现代 bid 的合流','出价；吩咐；致问候等不同用法']]
W('bid','/bɪd/','出价、投标；努力争取；吩咐、致意〔较正式〕',
 '拍卖场上报一个愿付的数，叫 bid；争取一项机会也能说 make a bid。较正式的 bid farewell 则是致告别，不是在拍卖再见。',
 '古英语 biddan 请求、要求与 bēodan 提供、宣布在后来合流，所以今天既有出价，也有吩咐、致意。不能把所有义都倒推成竞拍。',B,
 'bid for a contract 投标争取合同，bid fifty pounds 出价五十英镑，a bid to win 力图取胜；bid farewell 致告别。竞价常用 bid/bid/bid，正式旧义也见 bade、bidden。',
 'bid for；make a bid；a bid to do；bid farewell。',
 'bid 可是报价也可是尝试；an attempt 和 a bid 语义重叠，但 a bid of fifty pounds 是一个报价，不能直接换成 attempt。',
 ('She bid fifty pounds for the painting.','她为这幅画出价五十英镑。'),('The team made a final bid to save the project.','团队作了最后一次挽救项目的努力。'))
W('bidder','英 /ˈbɪdə/；美 /ˈbɪdər/','出价者、竞标者',
 '正在报价格、争取成交或合同的人、公司；-er 给动作 bid 配一个做这件事的角色。',
 'bid 双写 d + -er，中古英语已有相应人物名。现代常用义跟随拍卖、招标中的出价，不只指个人买家。',B+[['bid + -er → bidder','报价、竞标的人或机构']],
 'the highest bidder 最高出价者，a successful bidder 中标方，a rival bidder 竞争出价方。',
 'the highest bidder；a successful bidder；a rival bidder。',
 'bidder 是参与报价者，buyer 是买方；还没成交时可能有很多 bidders，最后只有一个买方。',
 ('The painting went to the highest bidder.','画作由出价最高的人拍得。'),('Three bidders competed for the contract.','三家竞标方竞争这份合同。'))
W('outbid','/ˌaʊtˈbɪd/','出价超过、以更高价压过',
 '对方报五十，你报六十，把对方价格越过去；out- 这里表示胜过，不是站在屋外出价。',
 'out- 超过 + bid 出价。常用过去式、过去分词也为 outbid，和竞价义 bid 一样不必加 -ed。',B+[['out- + bid → outbid','在出价上超过另一方']],
 'outbid a rival 出价超过对手，be outbid 被别人以更高价格超过；常直接接竞争者作宾语。',
 'outbid a rival；be outbid；outbid someone for something。',
 'outbid 说价格报得更高，不自动等于最终成功成交；outdo 更泛说表现胜过，未必涉及报价。',
 ('Another buyer outbid us for the painting.','另一位买家对这幅画的报价超过了我们。'),('She was willing to raise her offer but was outbid again.','她愿意加价，却再次被别人以更高价超过。'))
W('forbid','英 /fəˈbɪd/；美 /fərˈbɪd/','禁止、不准',
 '有权管这件事的人明确说不能做；不是没人邀请，而是把行为挡住。',
 '古英语 forbēodan，for- 是旧的阻止、排拒等方向材料，加 bēodan 宣布、命令；现代可联系 bid 的命令支，不按 for 为了 + 拍卖解释。',B[:1]+[['古英语 forbēodan → forbid','明令禁止；过去 forbade，过去分词 forbidden']],
 'forbid someone to do 禁止某人做，forbid doing 禁止某种行为，strictly forbidden 严禁。常见词形 forbid/forbade/forbidden。',
 'forbid someone to do；forbid doing；strictly forbidden。',
 'forbid 明令不许，prevent 是阻止结果发生，未必靠命令；不让做和实际阻止成功是两个角度。',
 ('The rules forbid visitors to feed the animals.','规则禁止游客喂动物。'),('Photography is forbidden inside the gallery.','画廊内禁止摄影。'))
R('B2824','请求、宣布两套旧词合流，现代出价与命令分支','BID：报出意愿、价格或要求；旧义不能只按拍卖猜','bid → bidder → outbid；forbid 接旧命令支，表示禁止。',
 '把拍卖中的报价链放一起，再单独看禁止。biddan、bēodan 的历史合流，解释了为什么这个短词用途比表面复杂。',
 'biddan/bēodan → bid；bid + -er 双写 d；out- + bid；forbēodan → forbid。',
 [['出价者和超过出价','bid · bidder · outbid'],['旧命令支的禁止','forbid']],
 'bid/buyer 报价动作与买方角色；outbid 不保证成交；forbid/prevent 不许与阻止。',
 'A rival bidder outbid us, but the rules forbid further bids.\n\n另一名竞标者的出价超过了我们，而规则不准再报价。','bid bidder outbid forbid')
D=[['古英语 dūst → 中古英语 dust → dust','干燥细粉、灰尘'],['英语动词 dust','去掉灰尘；也可撒上一层细粉']]
W('dust','/dʌst/','灰尘、细粉；掸灰；薄撒粉末',
 '细小颗粒飘着、落在桌上，是 dust；动词要看目标：dust the shelf 掸掉，dust the cake with sugar 却是撒上。',
 '接古英语 dūst，日耳曼旧词里有细尘、烟雾等关联。去掉和撒上两个动词方向，都是围绕粉尘形成，不能只背一种。',D,
 'a layer of dust 一层灰，dust the shelves 掸架子，dust with flour 撒上一点面粉，let the dust settle 等风波平息。',
 'a layer of dust；dust the shelves；dust with flour；let the dust settle。',
 'dust 通常是细颗粒，dirt 更泛是污垢、泥土；dust 作动词的方向需看清洁对象及 with 后面撒的材料。',
 ('She dusted the shelves before opening the shop.','开店前，她掸去了架子上的灰。'),('Dust the cake with a little sugar.','在蛋糕上薄薄撒一点糖粉。'))
W('dusty','/ˈdʌsti/','满是灰尘的、尘土飞扬的；灰柔色调的',
 '书放久了，封面落一层灰；路太干，一走就扬尘，都能说 dusty。颜色名里还能带有灰蒙、柔和的色调。',
 'dust + -y 的现代对应，古英语已有相应形容词形式。不是 thirsty 口渴的，尽管尘土路会让人口渴。',D+[['dust + -y → dusty','有灰、扬尘；像蒙灰般的颜色']],
 'a dusty road 尘土路，dusty shelves 落灰架子，dusty pink 灰粉色；a dusty old book 常带久放、少翻的画面。',
 'a dusty road；dusty shelves；dusty pink。',
 'dusty 直接描述灰或粉尘感，dirty 泛指脏；dusty pink 是色名，不表示衣服真脏。',
 ('We followed a dusty road into the village.','我们沿尘土飞扬的路进村。'),('She chose a dusty pink cover for the notebook.','她给笔记本选了灰粉色封皮。'))
W('duster','英 /ˈdʌstə/；美 /ˈdʌstər/','掸子、抹尘布；防尘长外套〔另一常见器物义〕',
 '常见是把灰拿掉的工具；也可指挡灰的长外衣，保护人不被路上的尘土弄脏。具体是哪一件，要看场景。',
 'dust + -er，表做清洁的人、工具；防尘外套等器物名称也沿防尘用途发展。-er 在这里不限人。',D+[['dust + -er → duster','除尘工具、做除尘的人；防尘外衣']],
 'a feather duster 鸡毛掸子，a soft duster 软抹尘布，a long duster coat 长防尘外套。',
 'a feather duster；a soft duster；a duster coat。',
 'duster 清灰工具，dustbin 收垃圾的桶；dusty 形容落灰，duster 是物品名词。',
 ('He brushed the shelf with a feather duster.','他用鸡毛掸子掸了掸架子。'),('She wore a long duster coat over her clothes.','她在衣服外套了一件长防尘外套。'))
W('dustbin','/ˈdʌstbɪn/','垃圾桶〔英式常见〕',
 '名字说收灰的桶，实际已经收一般垃圾；不是只能倒灰尘、其他东西都不准放。',
 'dust + bin，旧生活里收家用炉灰等废物的用途，扩展到普通垃圾容器。现代搭配比字面范围宽。',D+[['dust + bin → dustbin','收灰、废物的桶 → 垃圾桶']],
 'put it in the dustbin 把它扔进垃圾桶，empty the dustbin 清空垃圾桶，the dustbin of history 历史垃圾堆〔比喻〕。',
 'put in the dustbin；empty the dustbin；the dustbin of history。',
 'dustbin 英式常见，garbage can/trash can 美式常见；recycling bin 强调回收用途，不把所有桶的用途混掉。',
 ('Please put the wrapper in the dustbin.','请把包装纸扔进垃圾桶。'),('The old plan was sent to the dustbin of history.','那个旧方案被扔进了历史垃圾堆。'))
W('sawdust','/ˈsɔːdʌst/','锯末、锯屑',
 '锯子把木头锯开时落下的细碎粉屑；saw 在这里是工具锯，不是 see 的过去式。',
 'saw 锯 + dust 细粉。常指锯木形成的粉屑，也能描述像锯末一样干粉、难吃的食物口感。',D+[['saw + dust → sawdust','锯切留下的细屑']],
 'a pile of sawdust 一堆锯末，covered in sawdust 满是锯屑，smell of sawdust 锯木屑的气味。',
 'a pile of sawdust；covered in sawdust；smell of sawdust。',
 'sawdust 细锯屑，wood chips 常是较大木片；saw 不是本词里看到的过去动作。',
 ('Sawdust covered the workshop floor.','作坊地上满是锯末。'),('The carpenter brushed sawdust from the table.','木匠把桌上的锯屑刷掉。'))
R('B3110','细尘、粉屑；掸掉与撒上要看搭配','DUST：一层细粉，既能清掉，也能撒上','dust → dusty 落灰；duster 除尘工具；dustbin 垃圾桶；sawdust 锯末；stardust 星尘及比喻。',
 '最值得注意的是动词方向。掸架子是把灰拿掉，给糕点 dust with sugar 却把细粉加上；对象和介词告诉你怎么做。',
 'dūst → dust；dust + -y/-er/bin；saw/star + dust。',
 [['基本细尘与形容词','dust · dusty'],['清理工具和容器','duster · dustbin'],['粉尘来源与比喻','sawdust · stardust']],
 'dust 掸掉还是撒上看搭配；dusty pink 只是颜色；sawdust 的 saw 是锯。',
 'She used a duster to remove sawdust from the dusty shelf.\n\n她用抹尘布清掉了落灰架子上的锯末。','dust dusty duster dustbin sawdust stardust')
W('oatmeal','英 /ˈəʊtmiːl/；美 /ˈoʊtmiːl/','燕麦粉、燕麦片原料；燕麦粥〔尤美式〕',
 '这里 meal 先抓磨碎谷物，不是随便一顿饭；燕麦磨、压、加工成材料，再能指用它煮出来的粥。',
 'oat 燕麦 + meal 谷粉、粗磨谷物，已有中古英语组合。美式常用 oatmeal 说煮好的燕麦粥；材料和做好的食物要看句子。',
 [['谷粉 meal 与 oat 燕麦','meal 是磨碎谷物这一同形词支'],['oat + meal → oatmeal','燕麦材料 → 燕麦粥']],
 'a bowl of oatmeal 一碗燕麦粥，oatmeal cookies 燕麦饼干，an oatmeal sweater 燕麦色毛衣〔灰米色比喻〕。',
 'a bowl of oatmeal；oatmeal cookies；an oatmeal sweater。',
 'oatmeal 的 meal 不是一餐，而 meal 名词确有一餐的另一来源；porridge 是更泛的粥类，不只燕麦。',
 ('He ate a bowl of oatmeal with fruit.','他吃了一碗配水果的燕麦粥。'),('She baked oatmeal cookies for the class.','她给班里烤了燕麦饼干。'))
W('mealy','/ˈmiːli/','粉质的、粉沙口感的；像谷粉的',
 '苹果咬下去不脆、不多汁，像散成一颗颗干粉；mealy 就能形容这种粉沙口感。',
 'meal 谷粉 + -y，像粉、带粉质的。不是每一餐都得吃的、也不是 mealtime 用餐时间的形容词。',
 [['meal 谷粉','接磨碎谷物的旧词支'],['meal + -y → mealy','粉状、粉质口感的']],
 'a mealy apple 粉沙口感的苹果，a mealy texture 粉质口感，mealy potatoes 粉面土豆。好不好吃取决于食物、个人偏好。',
 'a mealy apple；a mealy texture；mealy potatoes。',
 'mealy 常是粉、沙、缺乏脆汁感；mushy 更突出软烂。两种口感可能同现，但不完全一样。',
 ('The apple looked fresh but tasted mealy.','苹果看着新鲜，吃起来却粉沙沙的。'),('This variety of potato has a mealy texture when cooked.','这个品种的土豆煮熟后口感粉面。'))
R('B3304','一餐与谷粉是不同旧词支，派生分别跟着走','MEAL：一顿饭和磨碎谷物，分两条线记','meal 一餐 → mealtime；谷粉 meal → cornmeal、wholemeal、oatmeal、mealy。',
 '中文翻成餐和粉差别很大，英语却同形。组合里先选对是哪支：用餐时间是一餐，燕麦粉、玉米粉用磨谷物那支。',
 '古英语 mǣl 时刻、一餐 → meal；古英语 melu 谷粉 → meal；后者与磨碎词族相关；oat/corn/whole + meal；meal + -y。',
 [['一餐和时间','meal · mealtime'],['谷粉、食物和口感','oatmeal · cornmeal · wholemeal · mealy']],
 'meal 一餐与谷粉分来源；oatmeal/porridge 燕麦特定用法与更宽粥类；mealy/mushy 粉沙与软烂。',
 'At mealtime, he chose oatmeal instead of the mealy apple.\n\n吃饭时，他选了燕麦粥，没有吃那只粉沙口感的苹果。','meal mealtime oatmeal cornmeal wholemeal mealy')
if __name__=='__main__':save('continuation_20261030_gp',ROOTS,WORDS)
