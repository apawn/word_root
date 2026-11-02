"""Raffles, punts, chance, pay-outs and pooled resources."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
def S(word,base):
 return ['https://en.wiktionary.org/wiki/'+word+'#English','https://www.etymonline.com/word/'+base]
def P(word):return S(word,'punt')+['https://www.merriam-webster.com/dictionary/punt']
EXISTING_ROOT_ADDITIONS={
 'A1760':dict(words='raffle raffles raffled raffling'.split(),label='raffle：卖抽奖券、抽签分配奖品',note='raffle 接法语骰子游戏材料，更远来源未定；现代抽奖名词发展出以抽奖方式送出奖品的动词。不是 -le 反复动作尾在现代英语里现拼。'),
 'A1697':dict(words='punt punts punted punting punter punters'.split(),label='punt：踢球、撑船、押注要分来源',note='踢球 punt 远源未定，撑船动词由平底船名转用，下注线接法语 ponter 等游戏材料；punter 的顾客口语义又由参与者用途扩展。人物 -er 相同，不代表基础动词只有一个祖先。'),
 'B4061':dict(words='lottery lotteries lotto'.split(),label='lottery 与 lotto：分份、抽签的旧材料',note='lottery 经意大利 lotteria 等接日耳曼分份、签的材料；lotto 经法语、意大利相应词进入英语。lotteries 是 y 变 ies 的复数，不把 lotto 当成 lottery 的简单现代缩写。'),
 'B2600':dict(words='jackpot jackpots'.split(),label='jackpots：从牌局底池到大奖、巨大收获',note='jack 选纸牌 J 的具体义，pot 选合起的赌注；旧牌局命名扩到大额奖金、巨大成功。现代 jackpots 不要求每个奖都与 J 牌规则有关。'),
 'B2955':dict(words='payout payouts payoff payoffs payday paydays'.split(),label='payout、payoff、payday：给出去的钱、所得效果、付薪日',note='payout 对应 pay out 的付出，payoff 对应 pay off 的给付、回报等用途，payday 为 pay 名词加 day。连写名词与分写动词短语各按语法认。'),
 'B2609':dict(words='windfall windfalls'.split(),label='windfalls：风吹落物与意外所得',note='wind 风加 fall 落下，早指风吹落的木、果等，后写意外利益；wind 在这里读 /wɪnd/。不必每笔意外所得都巨大。'),
 'B3441':dict(words='pool pooled pooling'.split(),label='pool 的水体与合资线分别加词尾',note='水体 pool 接古英语 pol，汇集资金等线接法语 poule 赌注材料，远源未定；现代 pooled、pooling 既可写积水，也可写合力，不把所有抽象义都当英语水池的新比喻。'),
}
RAFFLE=[['法语 rafle 骰子游戏 → 英语 raffle','更远来源未定'],['抽奖名词 → 以抽奖方式分配的动词','现代 -s、-ed、-ing 各说明语法角色']]
PUNT=[['同形三线：踢球来源未定；船名接拉丁 ponto；下注接法语 ponter 等','现代不能混成一种动作的所有比喻'],['相应动词 + 现代词尾、人物 -er','顾客 punter 属相关口语扩展，按场景认']]
LOT=[['日耳曼分份、签的材料 → 意大利 lotto、lotteria 等','和英语旧 lot 的材料相关'],['lottery、lotto 分别借入','抽签分奖；游戏名称及现代复数']]
PAY=[['pay 的支付动作 + out、off 等小词','组成不同的动作短语'],['相关短语 → payout、payoff；pay + day → payday','连写名词写支付、回报、付薪日，各有具体发展']]
POOL=[['水体 pool 接古英语 pol；合资 pool 接法语 poule 等','两条来源区分，远源未全定'],['各线动词 + 现代词尾','水积起来、资源合起来，可用共同画面辅助理解']]
W('raffle','/ˈræfəl/','抽奖；以卖券抽签方式分配奖品',
 '大家各买一张券，把号码放一起抽，抽中谁就拿奖品，这种活动叫 raffle。学校、社区筹款场景里很常见。',
 '经法语 rafle 骰子游戏材料，远源未定；后来发展出卖券抽签分奖的现代名词义，再有以这种方式送出物品的动词。',RAFFLE,
 'a raffle ticket 抽奖券；hold a raffle 举行抽奖；raffle off a bicycle 把自行车作为抽奖奖品送出。',
 'enter a raffle 参加抽奖；a charity raffle 慈善抽奖。',
 'raffle 常让人想到卖券后抽实物奖，lottery 范围更广；实际组织方式看上下文，不靠词本身判断规模、规则。',
 ('The school held a raffle to raise money for new books.','学校举行抽奖，为购买新书筹款。'),('They decided to raffle off a donated bicycle.','他们决定把捐来的自行车作为抽奖奖品送出。'),sources=S('raffle','raffle'))
W('raffles','/ˈræfəlz/','抽奖活动〔复数〕；以抽奖方式分配〔第三人称单数〕',
 '一年办几场抽奖，是 raffles；社团每年抽送一件奖品，也可说 it raffles off a prize。一个数活动，一个说怎么把东西送出。',
 'raffle + -s，/l/ 后读 /z/；动词三单与名词复数同形，基础词整体经法语相关材料而来。',RAFFLE+[['raffle + -s → raffles','多场抽奖；它以抽奖方式分配']],
 'charity raffles 慈善抽奖；raffles off a prize 抽奖送出奖品。',
 'organise raffles；raffles a donated item。',
 'raffles off a bicycle 是抽奖决定谁得到自行车，auctions it 是竞价决定买方；参与者做的事不同。',
 ('Local groups organise raffles throughout the year.','当地团体一年里会举办多场抽奖。'),('The club raffles off a donated painting each spring.','俱乐部每年春天会把一幅捐赠画作作为抽奖奖品送出。'),sources=S('raffles','raffle'))
W('raffled','/ˈræfəld/','以抽奖方式送出、分配了',
 '并非把那件物品直接卖给某一个人，而是卖券后抽出获得者，过去这样送出，就是 raffled off。',
 'raffle 去 e 加完整 -ed，/l/ 后读 /d/；通常与 off 一起突出把物品抽奖送出。',RAFFLE+[['raffle + -ed → raffled','过去以抽奖方式分配物品']],
 'raffled off a hamper 把礼篮抽奖送出；was raffled for charity 为慈善被用作抽奖奖品。',
 'raffled a donated watch；raffled off at the event。',
 'raffled 说明通过抽奖送出，donated 说明捐出；一件东西可以先被 donated，再被组织者 raffled off。',
 ('The organisers raffled off a basket of local food.','组织者把一篮当地食品作为抽奖奖品送出。'),('The signed shirt was raffled to raise money for the club.','那件签名球衣被用作抽奖奖品，为俱乐部筹款。'),sources=S('raffled','raffle'))
W('raffling','/ˈræflɪŋ/','正在以抽奖方式分配；卖券抽奖活动',
 '把一件捐赠物放进抽奖活动，通过卖券筹款，再抽出得主，整段安排可以叫 raffling。',
 'raffle 去 e 加 -ing，常读 /ˈræflɪŋ/；动作形式、活动名词都依 raffling off something 这类搭配理解。',RAFFLE+[['raffle + -ing → raffling','以抽奖方式分配物品的过程、活动']],
 'raffling off prizes 抽奖送出奖品；raffling a donated item 用捐赠物作抽奖奖品。',
 'raise money by raffling；a plan for raffling off equipment。',
 'raffling 重点在用抽奖分配物品，drawing 是抽签动作本身；一次活动可能既有售券、筹款，也有最后的 drawing。',
 ('The club is raffling off a guitar donated by a local musician.','俱乐部正把本地音乐家捐赠的吉他作为抽奖奖品送出。'),('They raised money by raffling a weekend holiday.','他们以抽奖送出周末度假的方式筹款。'),sources=S('raffling','raffle'))
W('punt','/pʌnt/','手放球凌空踢；撑平底船；下注、试一把〔英口语〕；平底船',
 '一手把球放下、落地前用脚踢出去，是 punt；剑桥河上用长杆撑的平底船也叫 punt。英口语 take a punt 则像说试一把、押个结果。',
 '这些同形义来源不同：踢球远源未定；船名接拉丁 ponto 等平底船材料，再转撑船动词；下注线接法语 ponter、西班牙 punto 等游戏术语。不把球踢出去编成赌钱来历。',PUNT,
 'punt the ball 把手放球凌空踢出；go for a punt 撑船游玩；take a punt on something 押一把、试某个选择。',
 'punt down the river 撑船顺河走；punt on the issue 延后作决定。',
 'punt 是手放球、落地前踢的动作，drop-kick 则在球触地弹起时踢；船、下注和拖延用法各看语境。',
 ('The player prepared to punt the ball downfield.','球员准备把手中放下的球凌空踢向前场。'),('We hired a punt for a quiet trip along the river.','我们租了一条平底船，沿河悠游。'),sources=P('punt'))
W('punts','/pʌnts/','凌空踢、撑船、下注〔第三人称单数〕；平底船、凌空踢〔复数〕',
 '河上停着几条撑杆平底船，是 punts；球员把球放下、落地前踢出，动词也可用 punts。相同结尾并没有把两条来历合并。',
 'punt + -s，/t/ 后读 /s/；可接不同来源的同形名词、动词。当前常见船、踢球、英式下注义须各按对象判断。',PUNT+[['punt + -s → punts','相应名词复数，或动词三单']],
 'punts along the river 河上的平底船；punts the ball 凌空踢球。',
 'a row of punts；punts on the outcome 押结果。',
 'punts 名词可能是船，也可能是踢球次数；前后出现 river、football 等词，通常比单看结尾更能帮助判断。',
 ('Several punts were tied up beside the river.','几条平底船拴在河边。'),('The player punts the ball before it touches the ground.','球员在球触地前把它凌空踢出。'),sources=P('punts'))
W('punted','/ˈpʌntɪd/','凌空踢出、撑船了；把问题推后、转交了',
 '把球往前场踢远是 punted；把棘手问题“踢”给下次会议处理，也可说 punted the decision。后者常暗示暂时不面对。',
 'punt + 完整 -ed，/t/ 后读 /ɪd/。体育的拖延、转交比喻与撑船、下注同形线分开，不能都认成同一来源。',PUNT+[['punt + -ed → punted','过去相应动作；踢球线还有转交、推后问题的比喻']],
 'punted the ball downfield 把球踢向前场；punted the decision 推迟决定。',
 'punted along the river；punted the issue to another committee。',
 'punted a decision 常带把难题踢开的口气，postponed 更中性；不是每次合理延期都要用 punted。',
 ('The player punted the ball far downfield.','球员把球凌空踢向远处前场。'),('The committee punted the decision to the next meeting.','委员会把决定推到了下次会议。'),sources=P('punted'))
W('punting','/ˈpʌntɪŋ/','撑平底船；凌空踢球；下注、暂缓处理〔依语境〕',
 '长杆顶住河底，身体一推，船往前滑，这种游河方式叫 punting。体育和英式下注场景里，同形词又选别的动作。',
 'punt + -ing；撑船动词来自船名，踢球动词远源未定，下注线接法语等游戏术语。-ing 只把当前动作写成过程、活动。',PUNT+[['punt + -ing → punting','相应动作的过程、活动名词']],
 'go punting 去撑船游玩；punting practice 凌空踢球训练。',
 'punting on a result 押结果；punting on a decision 暂缓作决定。',
 'punting on the river 通常是撑杆，rowing 通常是划桨；两种船行进方式不同。',
 ('We spent the afternoon punting on the river.','我们下午在河上撑船游玩。'),('The coach added extra punting practice before the match.','比赛前，教练增加了凌空踢球训练。'),sources=P('punting'))
W('punter','英 /ˈpʌntə/；美 /ˈpʌntɚ/','凌空踢球手、撑船者；下注者；顾客〔英口语〕',
 '美式橄榄球里的 punter 是负责相应踢球的人；英式口语里的 ordinary punter 却可能只是普通顾客、观众。先看他正在做什么、处在什么场景。',
 '相应 punt + -er 人物尾；踢球、撑船、下注各接不同的基础词源。顾客、观众义从相关参与者称呼扩展，不能拿球员一条词源解释全部。',PUNT+[['punt + -er → punter','做对应动作的人；英口语也泛指顾客、参与者']],
 'a team’s punter 球队的凌空踢球手；the average punter 普通顾客。',
 'a skilled punter 熟练撑船者或踢球者，须看语境；an ordinary punter。',
 'punter 在英式商业、演出语境可能近于 customer、audience member；并不保证对方正在下注。',
 ('The team signed a new punter before the season.','赛季前，球队签下一位新的凌空踢球手。'),('The owner wanted to know what the average punter thought of the café.','店主想知道普通顾客怎么看这家咖啡馆。'),sources=P('punter'))
W('punters','英 /ˈpʌntəz/；美 /ˈpʌntɚz/','凌空踢球手、撑船者、下注者〔复数〕；顾客、观众〔英口语〕',
 '店里来来往往的顾客，酒吧里掏钱消费的人，英口语常叫 punters。体育报道里的同形词，又可能是专门踢球的队员。',
 'punter + -s，读 /z/；内层 punt + -er 依相应动作来源区分，顾客义属于既定口语用法。',PUNT+[['punter + -s → punters','多位相应角色；英口语顾客等']],
 'regular punters 常客；punters at a racecourse 赛马场下注者。',
 'attract punters 吸引顾客；punters in the team 球队踢球手。',
 'punters 可能是顾客、下注者或球员，不能只看到前面的 sports 就忽略完整句子；动作、地点、角色共同决定。',
 ('The pub was full of regular punters on Friday night.','周五晚上，酒吧里满是常客。'),('The coach watched the punters practise on the field.','教练看着凌空踢球手在场上训练。'),sources=P('punters'))
W('lotteries','英 /ˈlɒtəriz/；美 /ˈlɑtəriz/','彩票、抽签分奖活动〔复数〕',
 '不是比谁表现好，而是抽签、抽号码决定获奖者，这类活动可以叫 lotteries。多个地区、不同类型的活动，就用这个复数。',
 'lottery 末尾辅音加 y，复数变 y 为 ies。基础词经意大利 lotteria 等连着较早分份、抽签材料，不是现代英语 lot 临时加一个随意的 -tery。',LOT+[['lottery → lotteries','y 变 ies，指多项抽签分奖活动']],
 'national lotteries 各国、各地区彩票；state lotteries 州级或地区彩票。',
 'prizes in lotteries；lotteries and raffles 彩票与抽奖活动。',
 'lotteries 按机会抽取结果，competitions 可以靠技巧、成绩评选；不能把所有有奖活动都叫彩票。',
 ('The article compared lotteries in several countries.','文章比较了几个国家的彩票活动。'),('The museum displayed old tickets from local lotteries.','博物馆展示了当地旧时彩票票券。'),sources=S('lotteries','lottery'))
W('lotto','英 /ˈlɒtəʊ/；美 /ˈlɑtoʊ/','数字抽奖游戏、彩票；类似宾果的配号游戏',
 '手里有一张数字卡，抽出号码后对照、标记，看哪些数字被抽中，便是 lotto 这一类游戏的直观画面。不同地区也用它叫彩票。',
 '经法语 loto、意大利 lotto 等进入英语，接分份、签的日耳曼材料。不是英语 lottery 直接截尾的唯一历史解释。',LOT+[['法语 loto、意大利 lotto → 英语 lotto','相应的配号游戏、彩票名称']],
 'a lotto game 数字配号游戏；lotto tickets 彩票券。',
 'play lotto 玩数字配号游戏；a game of lotto。',
 'lotto 是特定游戏、彩票名称，lot 泛指签、份额、批次等；不因字母相近就把现代用法全互换。',
 ('The children played a simple picture lotto game.','孩子们玩了一个简单的图卡配对抽取游戏。'),('The novel mentions a character who buys a lotto ticket every week.','小说提到一个每周买张彩票的人物。'),sources=S('lotto','lottery'))
W('jackpots','英 /ˈdʒækpɒts/；美 /ˈdʒækpɑts/','大额奖金、累积头奖；巨大收获〔复数〕',
 '机器、彩票宣传里的一笔笔头奖，是 jackpots；比喻时，也可以指某个项目带来的巨大收获。',
 'jackpot + -s，/t/ 后读 /s/；内层 jack 是纸牌 J，pot 是合起的赌注。旧牌局名称后来扩到大额奖金，并非一只叫 Jack 的锅。',
 [['纸牌 jack + pot 赌注池 → jackpot','较早牌局命名，后扩到大额奖金'],['jackpot + -s → jackpots','多个头奖或巨大收获']],
 'large jackpots 高额头奖；lottery jackpots 彩票头奖。',
 'record jackpots 创纪录的头奖；potential jackpots 可能的巨大收获。',
 'jackpots 强调特别大的奖、成功，prizes 可泛说各类奖品；一个小纪念奖通常不会叫 jackpot。',
 ('The report listed some of the largest lottery jackpots.','报告列出了一些金额最高的彩票头奖。'),('The documentary traced the stories behind several famous jackpots.','纪录片追溯了几笔著名头奖背后的故事。'),sources=S('jackpots','jackpot'))
W('payout','/ˈpeɪaʊt/','支付款；赔付款、奖金等一笔给付',
 '一方按约把一笔钱付给另一方，这笔给出去、拿到手的款可以叫 payout。保险、奖金、补偿等场景要由前面的词说清是什么钱。',
 '由 pay out 付出钱等短语形成连写名词。早期名词记录有油井产出足以抵成本的用法，现代常用来谈一笔给付；不把每次 payout 都解释成油井。',PAY+[['pay out → payout','较早短语形成名词，现代指支付款等给付']],
 'an insurance payout 保险赔付款；a large payout 大笔给付。',
 'receive a payout 收到一笔款；a one-off payout 一次性给付。',
 'payout 侧重实际给付的一笔款，payoff 还常说努力的回报、故事的收束效果；二者不是任何场景都可换。',
 ('The family received an insurance payout after the fire.','火灾后，这家人收到了保险赔付款。'),('The winner received the payout a week later.','获奖者一周后收到了奖金。'),sources=S('payout','payout'))
W('payouts','/ˈpeɪaʊts/','支付款、赔付款、奖金等〔复数〕',
 '不止一笔款项，或付给好几个人、分好几次给的钱，可以合称 payouts。词强调钱被付出，具体性质还看语境。',
 'payout + -s，/t/ 后读 /s/；内层名词对应 pay out，动词短语通常仍分写。',PAY+[['payout + -s → payouts','多笔给付、支付款']],
 'insurance payouts 保险赔付款；cash payouts 现金给付。',
 'large payouts；annual payouts 年度给付。',
 'payouts 是给付的钱，payments 范围更广，可包括买东西的普通付款；有时能接近，但搭配习惯不同。',
 ('The company listed the payouts in its annual report.','公司在年报中列出了各笔给付。'),('The article compared insurance payouts after different storms.','文章比较了不同风暴后的保险赔付。'),sources=S('payouts','payout'))
W('payoff','英 /ˈpeɪɒf/；美 /ˈpeɪɔf/','回报、所得结果；行贿款；故事或笑话的收束效果',
 '前面花的力气，最后终于得到一个“值了”的结果，就是 payoff。故事铺垫很久，结尾那一下给出满足感，也能叫 payoff。',
 'pay + off，与较早 pay off 付清、给付等短语相连。名词较早有赌赢所得、后来有行贿款等用法；现代回报、叙事效果分别按搭配学，不硬画成一个确定顺序。',PAY+[['pay off 相关短语 → payoff 名词','得到的钱、回报等，再有不同现代具体用途']],
 'a big payoff 丰厚回报、强烈效果；an emotional payoff 情感上的满足收束；a secret payoff 秘密行贿款。',
 'the payoff for years of work 多年工作的回报；the final payoff 最后的效果、回报。',
 'payoff 可以是金钱，也可只是结果、情感效果；payout 通常更直接是一笔实际给付。',
 ('The payoff for months of practice was a confident performance.','几个月练习的回报，是一场自信的演出。'),('The final scene provides a powerful emotional payoff.','最后一幕带来了强烈的情感收束效果。'),sources=S('payoff','payoff'))
W('payoffs','英 /ˈpeɪɒfs/；美 /ˈpeɪɔfs/','回报、所得效果〔复数〕；行贿款〔依语境〕',
 '做不同选择，会换来不同收益、效果，这些是 payoffs；新闻里若说 secret payoffs，又可能是一笔笔秘密行贿款。',
 'payoff + -s，/f/ 后读 /s/；内层 pay + off 相关名词。复数并不把所有义都变成合法回报或贿赂，须看搭配。',PAY+[['payoff + -s → payoffs','多个回报、效果，或多笔相应款项']],
 'long-term payoffs 长期回报；emotional payoffs 情感回报；secret payoffs 秘密行贿款。',
 'the payoffs of different choices；risks and payoffs 风险与回报。',
 'payoffs 可以是努力换来的非金钱效果；profits 主要指盈利，不能把故事结尾的 emotional payoffs 都翻成利润。',
 ('The report compared the costs and payoffs of the two plans.','报告比较了两个方案的成本与回报。'),('The investigation uncovered a series of secret payoffs.','调查揭露了一连串秘密行贿款。'),sources=S('payoffs','payoff'))
W('paydays','/ˈpeɪdeɪz/','发薪日、付款日〔复数〕；获得一大笔钱的机会',
 '日历上每次工资到账的那天，是 paydays；新闻里的 big paydays 也可借指赚到大钱的一次次机会。',
 'payday + -s，/eɪ/ 后读 /z/；内层 pay 工资、付款 + day 日子，较早也可说还款、付钱的日子。',PAY+[['pay + day → payday → paydays','付款、发薪的日子及其复数，后来也可比喻大笔收入']],
 'monthly paydays 每月发薪日；big paydays 大笔收入的机会。',
 'between paydays 两次发薪日之间；regular paydays 固定发薪日。',
 'paydays 是何时拿钱、拿到大笔收入的机会，paychecks 通常是工资款、工资支票；时间点和款项不是同一东西。',
 ('She marked the paydays on her calendar.','她在日历上标出了发薪日。'),('The novel follows actors hoping for bigger paydays.','小说讲述演员们盼着赚到更多钱的经历。'),sources=S('paydays','payday'))
W('windfalls','/ˈwɪndfɔːlz/','风落果、风吹落物〔复数〕；意外所得、意外好处',
 '风把苹果吹落，你不用爬树就捡到，是 windfalls；意料之外收到一笔钱、得到好处，也像天上掉到眼前。',
 'windfall + -s，/l/ 后读 /z/；内层 wind 风 /wɪnd/ + fall 落下。旧风落物义后来发展出意外获得的利益，不是缠绕动词 wind /waɪnd/。',
 [['wind + fall → windfall','风吹落的木、果等'],['意外所得义与现代复数 windfalls','多个风落物，或意外到手的好处']],
 'windfall apples 风落苹果；unexpected windfalls 意外所得；financial windfalls 意外钱财。',
 'collect windfalls 捡风落物；occasional windfalls 偶尔的意外好处。',
 'windfalls 强调意外到手，不保证数额巨大；earnings 更常强调工作、经营所得。',
 ('We collected the windfalls beneath the apple trees.','我们捡起苹果树下的风落果。'),('The family used occasional windfalls to repair the house.','这家人用偶尔的意外收入修房子。'),sources=S('windfalls','windfall'))
W('pooled','/puːld/','汇集、合用了；积成一滩了',
 '几个人把各自的钱放一起，凑够租车费，是 pooled their money；水流到低处积成一滩，也叫 pooled。共同画面是聚到一处。',
 'pool + 完整 -ed，/l/ 后读 /d/。水体动词接古英语水潭线；合资、资源动词接法语共同赌注材料，不能都定为英语水池的新比喻。',POOL+[['pool + -ed → pooled','过去合起资源，或液体积成滩']],
 'pooled resources 合起来的资源；pooled their money 凑钱；water pooled 水积成滩。',
 'pooled knowledge 汇集知识；pooled beneath the window 积在窗下。',
 'pooled money 是各自的钱合用，saved money 只说省下或攒下；一个人也能 save，不一定有人共同参与。',
 ('We pooled our money to hire a van.','我们凑钱租了一辆厢式车。'),('Rainwater pooled in the low corner of the yard.','雨水积在院子低洼的一角。'),sources=S('pooled','pool'))
W('pooling','/ˈpuːlɪŋ/','正在汇集、合用；液体积聚',
 '各队不再各存一套信息，而是把知识汇在一起，就是 pooling knowledge；地面不平，水正积成滩，也能用 pooling。',
 'pool + -ing；现代过程形式。水体、共同资金资源的两条历史仍分开，只借汇到一起的画面帮助记现代用法。',POOL+[['pool + -ing → pooling','汇集资源或积水的过程、活动']],
 'pooling resources 汇集资源；pooling knowledge 汇集知识。',
 'pooling money 凑钱；water pooling on the floor 地板积水。',
 'pooling resources 强调各方拿出来合用，collecting resources 可能只是搜集；汇集共同使用这一层未必相同。',
 ('Pooling our skills helped us finish the project.','把各自技能合起来，帮助我们完成了项目。'),('Water was pooling on the uneven floor.','水正在不平的地板上积成一滩。'),sources=S('pooling','pool'))
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_zhg',ROOTS,WORDS)
 extend_lessons()
