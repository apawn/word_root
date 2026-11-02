"""Fall: physical descent, amounts, ruin and familiar compounds."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
def C(a,b,w,m):return [[a+'；'+b,'并列构词部分'],[w,m]]
FA=[['古英语 feallan → 中古英语 fallen → fall','掉落、倒下；失败、衰落等'],['现代英语 fall','落下、下降；进入某种状态；秋季等固定用法']]
W('fall','英 /fɔːl/；美 /fɔːl/，亦 /fɑːl/','落下；跌倒；下降；进入某种状态；秋天〔美〕',
 '从高处往下、从站着变成倒下，再把数量下降、地位衰落也放进同一画面。进入状态则要认固定搭配。',
 '由古英语 feallan 延续，变化 fall—fell—fallen。秋天的 fall 来自落叶季的命名习惯，不是英语所有季节都用动作当名字。',FA,
 'fall down 跌倒，prices fall 价格下跌；fall asleep 入睡，fall in love 爱上；in the fall 在秋天，美式常见。fall on a Monday 可说日期恰逢周一。',
 'fall asleep；fall in love；fall behind；in the fall。',
 'fall 不及物，说 The cup fell；drop 可说 I dropped the cup，我失手让杯子掉了。fell 也是另一个伐倒动词原形，依句子分。',
 ('The leaves began to fall.','树叶开始飘落。'),('The meeting falls on a Friday this year.','今年这次会议恰逢周五。'))
W('fallen','英 /ˈfɔːlən/；美 /ˈfɔːlən/，亦 /ˈfɑːlən/','已落下的；倒下的；阵亡的；失势、堕落的',
 '动作已经发生，东西落到了下面；说士兵阵亡或人物失势时，也借倒下的状态。',
 'fall 的过去分词，接古老不规则变化，并形成形容词。fall—fell—fallen 不是统一加 -ed。',FA+[['fall → fell → fallen','原形 → 过去式 → 过去分词；已倒下的状态']],
 'fallen leaves 落叶，a fallen tree 倒树，fallen soldiers 阵亡士兵；a fallen hero 失势、名誉受损的英雄。',
 'fallen leaves；a fallen tree；fallen soldiers；a fallen hero。',
 'falling 正在落，fallen 已经落；falling leaves 仍在空中飘，fallen leaves 常已落在地上。',
 ('The path was covered with fallen leaves.','小路上覆盖着落叶。'),('They placed flowers at the memorial to fallen soldiers.','他们在阵亡士兵纪念碑前献花。'))
W('rainfall','/ˈreɪnfɔːl/，美亦 /ˈreɪnfɑːl/','降雨；降雨量',
 '不仅说天上有雨，更常把某地某时段下了多少雨作为一个量来谈。',
 'rain 雨 + fall 落下，形成降雨现象、雨量名词。后半是下落，不是秋季。',C('rain 雨','fall 落下','rainfall','降雨现象及累计雨量'),
 'annual rainfall 年降雨量，heavy rainfall 强降雨；average rainfall 平均雨量需对应地点、时间范围。',
 'annual rainfall；heavy rainfall；average rainfall；low rainfall。',
 'rainfall 常强调降雨量，rain 泛指雨、水或下雨现象；a rainfall figure 是雨量数字，不是一滴雨。',
 ('Annual rainfall varies across the region.','该地区各处的年降雨量不同。'),('Heavy rainfall caused delays on several roads.','强降雨使几条道路上的行程延误。'))
W('downfall','/ˈdaʊnfɔːl/，美亦 /ˈdaʊnfɑːl/','垮台；衰败；导致失败的因素',
 '从原来较高、较稳的位置掉下来；也会把让人跌下来的弱点叫 downfall。',
 'down 向下 + fall 落下，强化下降画面，固定为地位、权势、事业等的崩落。',C('down 向下','fall 掉落','downfall','从地位或成功状态跌落；导致失败的因素'),
 'the downfall of a ruler 统治者垮台，pride was his downfall 骄傲让他失败；通常比普通小挫折重。',
 'lead to the downfall of；bring about someone’s downfall；be someone’s downfall。',
 'downfall 垮台或致败因素，setback 挫折可能是暂时的；fall down 是普通动作短语，不等于每次都事业失败。',
 ('The scandal led to the minister’s downfall in the novel.','小说里，这场丑闻导致大臣垮台。'),('His refusal to listen proved to be his downfall.','他不肯听取意见，最终成了失败的根源。'))
W('windfall','/ˈwɪndfɔːl/，美亦 /ˈwɪndfɑːl/','意外收获；意外之财；风落果',
 '果子本来还在树上，风一吹就掉到你面前；后来用来说没预料到、突然得到的好处。',
 'wind 风 + fall 落下，中古英语已有风吹落物的组合，后来引申为意外所得。wind 这里读 /wɪnd/，不是缠绕的 /waɪnd/。',C('wind 风','fall 落下','windfall','风吹落物 → 意外得来的利益、好处'),
 'an unexpected windfall 意外之财，a financial windfall 一笔意外收益；windfall apples 风落苹果仍是具体用法。',
 'a financial windfall；an unexpected windfall；windfall apples。',
 'windfall 意外所得，earnings 常指劳动、经营等收入；收到一笔钱是否意外，要看具体情境，不是所有收入都叫 windfall。',
 ('The unexpected refund was a welcome windfall.','意料之外的退款，是一笔令人高兴的意外收获。'),('They gathered windfall apples after the storm.','暴风雨后，他们捡拾了风落苹果。'))
W('befall','/bɪˈfɔːl/，美亦 /bɪˈfɑːl/','降临于；发生在……身上〔较正式〕',
 '某件事落到了某个人头上，通常是意外或不幸，叙事语气比 happen to 更书面。',
 '古英语 befeallan 等已有组合，be- + feallan，原有落在、发生于等义。不是 be 动词加 fall 就能照普通句式自由拼用。',FA[:1]+[['古英语 befeallan → befall','落在、发生于 → 降临某人身上']],
 'a disaster befell the town 灾难降临小镇；whatever may befall 无论发生什么。变化 befall—befell—befallen。',
 'befall someone；whatever may befall；the fate that befell。',
 'befall 直接接发生于谁，happen to someone 要 to；不通常说 befall to someone。',
 ('The story tells of the misfortune that befell the family.','故事讲述了降临这个家庭的不幸。'),('No one knew what had befallen the missing travellers.','没人知道失踪旅人遇到了什么事。'))
W('pitfall','/ˈpɪtfɔːl/，美亦 /ˈpɪtfɑːl/','陷阱；容易踩到的隐患、错误',
 '路面看着正常，脚下却藏着一个坑；做事时不容易预先看到的问题也像这种陷阱。',
 'pit 坑 + fall 掉落，形成坑式陷阱名称，再比喻隐藏风险、容易犯错之处。',C('pit 坑','fall 掉落','pitfall','会让人掉进去的坑式陷阱 → 隐患、易错处'),
 'avoid common pitfalls 避免常见错误、隐患，the pitfalls of a method 某方法的潜在问题；比普通 difficulty 更有容易没注意就踩中的感觉。',
 'avoid pitfalls；common pitfalls；the pitfalls of；a potential pitfall。',
 'pitfall 不是 pothole 路面坑洞的通用同义词；比喻里 pitfall 常指看似顺利时容易忽略的问题。',
 ('The guide explains common pitfalls for new learners.','指南解释了新手常踩的坑。'),('One pitfall of the plan is its dependence on a single supplier.','方案的一个隐患，是过度依赖单一供应商。'))
W('outfall','/ˈaʊtfɔːl/，美亦 /ˈaʊtfɑːl/','排水口；排放水流进入水体的出口',
 '管道或水道走到末端，把水排进河、海等地方的那个出口。',
 'out- 向外 + fall，联系水向外流落的画面，固定成排放出口、排水系统末端等名称。不是所有东西掉出箱子都用 outfall。',C('out- 向外','fall 水流落、排出的画面','outfall','排水系统向外排放的出口'),
 'a stormwater outfall 雨水排放口，a sewage outfall 污水排放口；词只说出口用途，不说明处理水平。',
 'a stormwater outfall；a sewage outfall；an outfall pipe。',
 'outfall 排放口，waterfall 瀑布；fallout 则是另一固定词，可指后果或放射性沉降物，不靠换顺序互译。',
 ('The map shows the location of the stormwater outfall.','地图标出了雨水排放口的位置。'),('Engineers inspected the outfall pipe after the storm.','工程师在暴风雨后检查了排水口管道。'))
W('offal','英 /ˈɒfəl/；美 /ˈɔːfəl/，亦 /ˈɑːfəl/','动物内脏等可食杂件；旧有废料义',
 '分割整只动物时，主肉块之外另分出的内脏等部分；现代菜单上常把这些作为食材一类来谈。',
 '中古英语 offal、offall，off 离开 + fall 落下，对应分切时落下、另分出的部分，较早有废料义。现代食用内脏不等于没有用途的垃圾。',
 [['off + fall → 中古英语 offall、offal','另分出、落下的边余料'],['现代 offal','内脏等食用杂件；某些语境仍指废料']],
 'cook with offal 用内脏食材做菜，liver and other offal 肝等内脏；具体包括哪些食材随烹饪习惯，不必每块碎肉都叫 offal。',
 'liver and other offal；offal dishes；cook with offal。',
 'offal 是食材、杂件名称，awful 糟糕的只是近音；不能因为不熟悉这种食材，就把词义译成难吃。',
 ('The cookbook includes several dishes made with offal.','食谱里有几道用内脏食材制作的菜。'),('Liver is one type of offal.','肝是内脏食材的一种。'),sources=['https://en.wiktionary.org/wiki/offal#English','https://www.etymonline.com/word/offal'])
R('B2609','落下、倒下、下降；状态变化与固定复合词','FALL：从原位落下，再到数量、地位和状态','falling 正落，fallen 已落；rainfall 雨落，windfall 风落物及意外收获；下坠画面在各词中有不同固定结果。',
 'fall 继承古英语 feallan，过去式 fell、分词 fallen。fall asleep、fall in love 按固定搭配理解，不能把所有状态变化都直译向下掉。offal 则保留分出、落下边余料的旧构词。',
 'fall → fallen、befall；rain、wind、night + fall 是不同事件；downfall 垮台，pitfall 隐患；outfall 排放口，offal 另分出的食材部分。',
 [['基础、完成与降临','fall · fallen · befall'],['自然现象及落地','rainfall · waterfall · windfall · nightfall · landfall'],['跌落及后果','downfall · pitfall · shortfall · fallout · freefall · footfall'],['排出及分出物','outfall · offal']],
 'falling 正在落，fallen 已落；windfall 意外收获，downfall 垮台；outfall 与 fallout 不同；offal 不是 awful。',
 'The fallen apples were a windfall, but the slippery path was a pitfall.\n\n落下的苹果是意外收获，湿滑小路却是个容易踩中的隐患。',
 'fall fallen befall rainfall waterfall windfall nightfall landfall downfall pitfall shortfall fallout freefall footfall outfall offal')
if __name__=='__main__':save('continuation_20261029_dd',ROOTS,WORDS)
