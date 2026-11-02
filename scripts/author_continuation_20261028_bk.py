"""Half, happy, buy: quantity, fortune and feeling, purchase and acquisition."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
def C(a,b,w,m):return [[f'{a}；{b}','并列构词部分'],[w,m]]
HALF=[['古英语 healf → 中古英语 half / halfe','一半；一边、一侧'],['英语 half','二分之一；部分、不完全的程度']]
W('half','英 /hɑːf/；美 /hæf/','一半；半的；部分地、不完全地',
 '把整体分成两份，取其中一份；口语也用半来说某种状态没到满格。',
 '接古英语 healf，旧名词也有一边、一侧义。l 在常见标准读音里不发音；复数 halves 英 /hɑːvz/、美 /hævz/，f 变 /v/。',HALF,
 'half an hour 半小时，half the cake 半个蛋糕，half asleep 半睡半醒；the first half 可是比赛上半场。程度用法未必在精密量出50%。',
 'half an hour；half of；cut in half；half asleep；the first half。',
 'half 可作名词、形容词，halve 是动词。half an hour、half the cake 是常用结构；名词复数 halves 与动词 halve 分开记。',
 ('We shared the cake, taking half each.','我们分了蛋糕，每人一半。'),('I was still half asleep when the phone rang.','电话响时，我还半睡半醒。'))
W('halve','英 /hɑːv/；美 /hæv/','分成两半；减半',
 '可以把一块东西切开平分，也可以把原本的数量降到一半。',
 '接古英语 hilfan、helfan 等、中古英语 halven，属于 half 的旧词族；现代拼写把 f 与 /v/ 的历史交替保留下来。不是 halve 读成 half 加 /e/。',
 [['古英语相关分半动词 → 中古英语 halven','分两份、减半'],['英语 halve；与 half 对应','把数量减到一半；一分为二']],
 'halve an apple 把苹果分两半，halve the time 时间减半。过去式 halved 的 -ed 读 /d/。',
 'halve the cost；halve the time；halve an apple。',
 'halve 减到原来一半，不是减少原数的一半以外任意程度；double 则是变成两倍。',
 ('The new process halved the waiting time.','新流程把等待时间减半了。'),('She halved the sandwich and shared it with me.','她把三明治分成两半，与我分享。'))
W('behalf','英 /bɪˈhɑːf/；美 /bɪˈhæf/','代表、为了某人〔常见于 on behalf of〕',
 '站到某人这一边、替他出面，或为他的利益做事。',
 '接中古英语 bihalve，古英语 bī healfe 原意在某人旁边；healfe 是 healf 的一侧、一边旧义，不是今天 become half“变成一半”。',
 [['古英语 bī healfe → 中古英语 bihalve','在某人的一侧、旁边'],['英语 behalf；固定表达 on behalf of 等','代表；为了某人的利益']],
 'on behalf of the team 代表团队，speak on someone’s behalf 代人发言；也可指为某人的利益做事。通常不单独用 behalf 作万能代替名词。',
 'on behalf of；speak on someone’s behalf；on my behalf。',
 'on behalf of 代表、为其利益，instead of 代替某人某事的范围更广；代买面包不必每次用正式的代表措辞。',
 ('I am writing on behalf of the whole team.','我代表整个团队写这封信。'),('Could you collect the parcel on my behalf?','你能代我取一下包裹吗？'))
R('B3257','二分之一；旧义还有一侧','HALF：整体的一半，也曾表示站在哪一边','half 一半，halve 动手分半，behalf 则要走回一侧、旁边的旧义才能理解代表。',
 'half 接古英语 healf，l 常不发音；halves /v/ 与 halve 的 /v/ 对照。behalf 来自 bī healfe 在某人一侧，不按现代一半义硬拼。',
 'half ↔ halve；halfway、halftime 分路程与比赛时段；behalf 单列一侧旧义的历史。',
 [['半与减半','half · halve'],['进程、时段和代表关系','halfway · halftime · behalf']],
 'half 名词、形容词，halve 动词；half asleep 是半睡半醒，不一定测出50%睡着；on behalf of 代表某人，不是代他一半。',
 'On behalf of the team, she asked to halve the meeting time.\n\n她代表团队请求把会议时间减半。',
 'half halve halfway halftime behalf')
HAPPY=[['中古英语 happy / happyn 等幸运相关形式；与 hap 好运等词相关','幸运、处境顺遂'],['英语 happy','高兴、满意、乐意；合宜、幸运等义']]
W('happy','/ˈhæpi/','高兴的；满意的；乐意的；幸运、合宜的',
 '事情顺心，心里舒服；从运气好到心情好，是理解这个词的一条直观路。',
 '中古英语 happy 早有幸运义，与 hap“运气”及相关北欧形式有关。现代可对照 hap + -y，历史具体形成有不同分析，不等同今天新拼出一个词。',HAPPY,
 'feel happy 高兴，happy with the result 对结果满意，happy to help 乐意帮忙，a happy accident 幸运巧合。比较级 happier、最高级 happiest。',
 'happy with；happy to；happy about；a happy accident。',
 'happy to help 常是乐意帮，不一定说正在欢笑；lucky 幸运与 happy 高兴相关但现代不总能替换。',
 ('I am happy with the result.','我对结果很满意。'),('I would be happy to explain it again.','我很乐意再解释一遍。'))
W('happiness','/ˈhæpinəs/','快乐；幸福；满足感',
 '不只这一秒笑了，也可以是觉得生活安稳、值得、心里满足的整体感受。',
 'happy + -ness，y 变 i；-ness 把高兴、幸福的性质变成名词，不是 happy 的普通复数。',HAPPY+[['happy + -ness → happiness','高兴、幸福、满足的状态']],
 'bring happiness 带来快乐，a source of happiness 快乐来源，lasting happiness 持续幸福感。通常不可数。',
 'bring happiness；a source of happiness；lasting happiness。',
 'happiness 幸福、快乐感，a happy event 快乐的事件；一个说感受状态，一个说使人有感受的事情。',
 ('Music has always been a source of happiness for her.','音乐一直是她快乐的来源。'),('Their faces showed genuine happiness.','他们脸上流露出真切喜悦。'))
W('happily','/ˈhæpɪli/，也读 /ˈhæpəli/','高兴地；乐意地；幸好、幸运地',
 '可以是开心地做，也可以像回头感叹“还好事情这样发展”。',
 'happy + -ly，y 变 i；中古英语有 happyly 等相应副词。幸运义与 happy 的好运旧背景相连。',HAPPY+[['happy + -ly → happily','高兴、乐意地；幸运地']],
 'smile happily 开心微笑，happily agree 乐意同意，Happily, no one was hurt 幸好无人受伤。happily married 说婚姻幸福。',
 'smile happily；happily agree；happily married；Happily, ...。',
 'happily 可以表达乐意，不只笑着；hopefully 但愿面向愿望，happily 的幸好常评论已知好结果。',
 ('The children played happily in the garden.','孩子们在花园开心玩耍。'),('I would happily help you move the boxes.','我很乐意帮你搬箱子。'))
W('unhappy','/ʌnˈhæpi/','不开心的；不满意的；不幸、令人不快的',
 '可能心情低落，也可能不认可某个安排；不开心与不满意要看对象。',
 'un-（不）+ happy，中古英语已有 unhappy。不是 hap 加 py 后再随意改音，也不是所有 un- 都表示主动撤销。',HAPPY+[['un- + happy → unhappy','不高兴、不满意；不幸的']],
 'unhappy about a decision 对决定不满，unhappy with the service 对服务不满意，an unhappy childhood 不幸福的童年。',
 'unhappy about；unhappy with；an unhappy childhood。',
 'unhappy 不开心或不满，unlucky 不走运；运气很好的人也可能对某事 unhappy。',
 ('She was unhappy with the proposed schedule.','她对拟定日程不满意。'),('The ending left me feeling unhappy.','结尾让我感到难过。'))
W('unhappily','/ʌnˈhæpɪli/','不开心地；不幸地、遗憾地',
 '人闷闷不乐地行动，或说话人替整个结果加上一声遗憾。',
 'unhappy + -ly，y 变 i；也可对照 un- + happily，历史有中古英语 unhappily 等形式。',HAPPY+[['unhappy + -ly → unhappily','不高兴地；不幸、遗憾地']],
 'sit unhappily 闷闷不乐坐着，Unhappily, ... 较正式地说不幸的是。与 happily 一样，可能评论全句。',
 'sit unhappily；live unhappily；Unhappily, ...。',
 'unhappily 修饰动作、整句，unhappy 形容人、情况；She looked unhappy 是她显得不开心，不必改成副词。',
 ('He stared unhappily at the broken model.','他闷闷不乐地盯着坏模型。'),('Unhappily, the original photographs have been lost.','遗憾的是，原始照片已遗失。'))
W('unhappiness','/ʌnˈhæpinəs/','不快乐；不满；不幸福感',
 '把一段时间心里不舒服、对处境不满意的状态，作为整体感受来谈。',
 'unhappy + -ness，y 变 i；也可对照 un- + happiness 的否定关系。',HAPPY+[['happy → unhappy → unhappiness','高兴的 → 不高兴的 → 不快乐、不满的状态']],
 'a source of unhappiness 不快乐的来源，express unhappiness 表达不满。可能是情绪低落，也可能是对某项具体安排的不满意。',
 'a source of unhappiness；express unhappiness；deep unhappiness。',
 'unhappiness 普通不快乐、不满，不单凭这个词就等于某种医学诊断；一篇投诉里的 unhappiness 可能只是服务不满意。',
 ('She expressed unhappiness about the sudden change.','她对突然变更表达了不满。'),('The novel explores the family’s hidden unhappiness.','小说探讨一家人隐藏的不幸福感。'))
R('B3186','高兴、满意、乐意；幸运旧背景','HAPPY：从处境顺遂到心里舒服','笑着高兴、对结果满意、乐意帮忙，都是常见现代用法；unhappy 则不一定只说伤心。',
 'happy 早期有幸运义，与 hap 好运及相关旧形式有关。happily 仍可说幸好；名词和副词接后缀时 y 常变 i。',
 'happy → happily、happiness；unhappy → unhappily、unhappiness，正反两组各自相邻。',
 [['高兴、乐意、幸福感','happy · happily · happiness'],['不开心、不满及其方式、状态','unhappy · unhappily · unhappiness']],
 'happy to help 乐意帮；unhappy with 对……不满意；happily 可评论幸运结果，hopefully 常表达但愿。',
 'She was happy to help, but unhappy with the lack of planning.\n\n她乐意帮忙，却对缺乏规划不满意。',
 'happy happily happiness unhappy unhappily unhappiness')
BUY=[['古英语 bycġan → 中古英语 byen','购买'],['英语 buy；过去式、过去分词 bought','买；也可比喻接受说法、换取时间']]
W('buy','/baɪ/','买；相信、接受某种说法',
 '拿钱换来东西；口语把接受解释也说成买账。',
 '继承古英语 bycġan，经中古英语形式变成 buy；现代不再拆成更小的有意义部分。过去式、过去分词都是 bought /bɔːt/，美音也常 /bɑːt/。',BUY,
 'buy a ticket 买票，buy someone lunch 请某人吃午饭；I don’t buy it 表示我不信。buy time 是采取行动争取更多时间，并非真的购买钟表。',
 'buy something for someone；buy someone something；buy time；buy into an idea。',
 'buy 是买入，sell 是卖出；pay 强调付钱，不一定把所买的东西作为直接宾语。',
 ('I bought a secondhand desk for my room.','我给房间买了一张二手书桌。'),('I don’t buy his explanation for the missing files.','我不相信他对文件丢失的解释。'),('The temporary repair bought us a little time.','临时修补为我们争取了一点时间。'))
W('buying','/ˈbaɪɪŋ/','购买行为；采购',
 '把买东西这件事当成一个过程或一种行为来谈。',
 'buy + -ing。既可作动词现在分词，也可作名词，表示购买、采购活动。',BUY+[['buy → buying','买 → 购买这一行为']],
 'online buying 网上购物，panic buying 恐慌性抢购；buying habits 是一个人平时怎么买东西。作名词时常说整体活动，不是一个个买家。',
 'buying habits；impulse buying；panic buying；buying power。',
 'buying 是购买活动，shopping 可包含逛店、比较商品而还没买；buyer 才是买的人。',
 ('The survey asks about students’ online buying habits.','调查询问学生的网购习惯。'),('She made a list to avoid impulse buying.','她列了清单，避免冲动购物。'))
W('buyer','英 /ˈbaɪə/；美 /ˈbaɪər/','买家；采购员',
 '站在交易中掏钱买入的那一边。',
 'buy + -er，表示进行购买的人；职业语境也可指替商店或企业挑选、采购商品的人。',BUY+[['buy → buyer','购买 → 买的人；负责采购的人']],
 'a potential buyer 潜在买家，a first-time buyer 首次购房者等首次购买者，具体看语境。零售企业的 buyer 是为企业进货，未必为自己使用。',
 'a potential buyer；a buyer for a department store；find a buyer。',
 'buyer 买入方，seller 卖出方；customer 更宽泛地强调与商家的顾客关系。',
 ('The owner has found a buyer for the old house.','房主为老房子找到了买家。'),('She works as a clothing buyer for a department store.','她在一家百货商店担任服装采购员。'))
W('buyback','/ˈbaɪbæk/','回购；买回',
 '原来卖出去或发行出去的东西，又花钱收回来。',
 '由短语 buy back 合写成名词：buy 买 + back 回来。这里的 back 表示回到原来的持有方。',C('buy 购买','back 回来','buyback','把东西买回的行为、安排'),
 'a share buyback 是公司回购自己的股份；book buyback 可以是书店回收购入旧教材的安排。先抓住买回，再根据对象理解具体内容。',
 'a share buyback；a book buyback program；announce a buyback。',
 'buyback 强调买回；refund 是把钱退回，两者交易方向不同。回购这个词本身没有承诺价格一定上涨。',
 ('The company announced a share buyback.','公司宣布了一项股份回购计划。'),('The campus bookstore runs a textbook buyback each spring.','校园书店每年春天都会开展旧教材回购。'))
W('buyout','/ˈbaɪaʊt/','收购；买断他人权益',
 '把别人手里的企业或持有权益买过来，让所有权或控制关系发生变化。',
 '由 buy out 名词化合写；out 在这个短语中带有通过付款让原持有人退出其权益位置的意思。',C('buy 购买','out 在 buy out 中指买走他人权益','buyout','收购企业或买断权益'),
 'a management buyout 是管理层收购企业。理解重点是所有权、权益的转移，不是普通顾客把商店货架买空。',
 'a management buyout；a proposed buyout；complete a buyout。',
 'buyout 说收购、买断权益；buyback 说把原来出售或发行的东西买回；sell out 才可说商品售罄。',
 ('The managers are discussing a buyout of the family business.','管理人员正在讨论收购这家家族企业。'),('After the buyout, the factory had a new owner.','收购后，工厂有了新主人。'))
R('B2553','买；买账；买回或买断权益','BUY：付出代价，把东西换过来','先想付钱换物，再理解用行动换时间、在心里接受说法这两种比喻。',
 'buy 接古英语 bycġan。buying、buyer 保留这个动作；buy back、buy out 合写成名词后，分别强调买回与收购权益。',
 'buy → buying、buyer；buy back → buyback；buy out → buyout。',
 [['购买及参与者','buy · buying · buyer'],['回购与收购','buyback · buyout']],
 'I don’t buy it 是不信；buy time 是争取时间。buyback 买回，buyout 买下企业或权益。',
 'The buyer asked for more time, but the seller didn’t buy his explanation.\n\n买家要求更多时间，但卖家不相信他的解释。',
 'buy buying buyer buyback buyout')
if __name__ == '__main__':save('continuation_20261028_bk',ROOTS,WORDS)
