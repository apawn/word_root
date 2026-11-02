"""Common -ing forms: adding, changing, bringing, allowing and testing."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'B2502':dict(words=['add','adding'],label='add → adding：再放上一份与补充说明',note='addere 的历史是 ad- 向与 -dere 放、置相连；这里区别于表示给的拉丁 dare。'),
 'B3018':dict(words=['change','changing'],label='change → changing：更换、变动与变化中的',note='交换、更换的词族发展为改变；去末尾 e 加 ing。'),
 'C0268':dict(words=['create','creating'],label='create → creating：让新事物产生',note='拉丁创造、生育词族，现代既可说创作，也可说带来问题、条件。'),
 'C1635':dict(words=['provide','providing'],label='provide → providing：预先照顾到并拿出所需',note='向前看、预作准备的词族，发展为提供、供给。'),
 'B3560':dict(words=['bring','bringing'],label='bring → bringing：携带到参照点、带来结果',note='bring 继承古英语 bringan；bringing 直接加 ing，过去 brought 另有变化。'),
 'B2669':dict(words=['carry','carrying'],label='carry → carrying：把东西带在身上或承载着',note='用车运输的法语词族，扩大为携带、承载；加 ing 保留 y。'),
 'B2609':dict(words=['fall','falling'],label='fall → falling：往下、变少与进入某状态',note='fall 的落下词族，扩到下降、倒下与 falling asleep 等固定用法。'),
 'B3592':dict(words=['allow','allowing'],label='allow → allowing：许可与留出条件',note='分配、安排与赞同、认可两条较早来源在法语相近形式中汇合。'),
 'B2425':dict(words=['trade','trading'],label='trade → trading：惯常做事的路与交易',note='路径、惯常活动发展出行业、商贸；词源连接 tread，不是拉丁 trad 交付。'),
 'B3237':dict(words=['test','testing'],label='test → testing：检验，以及考验人的',note='检验容器的名词发展到检验动作；testing 也能形容费力、考验人的情况。'),
}
W('adding','/ˈædɪŋ/','正在添加、相加；补充说明；add 的 -ing 形式',
 '原来已经有一些，现在再放上一份，就是 adding；数学上把数量合起来，讲话时再补一句，也有加上去的感觉。',
 'add + -ing，保留原词已有的 dd。add 借拉丁 addere，ad- 向与 -dere 放、置相连，原来是放到、附加；这里的放置成分与表示给的 dare 不同。',
 [['拉丁 ad- + -dere → addere → 英语 add','放到原有东西上、附加'],['add + -ing → adding','添加过程；正在相加、补充']],
 'adding water 正在加水；adding numbers 正在相加；adding a note 补充注释；adding to the problem 让问题更严重。',
 'keep adding；without adding extra weight。','add something to something 是把前者加到后者。add to something 可直接说增加、加重某种情况；adding up 则常说合计，或前后说得通。',
 ('She is adding a few notes to the final page.','她正在最后一页加几条注释。'),('The extra packaging is adding to the weight.','额外包装正在增加重量。'),sources=['https://en.wiktionary.org/wiki/adding#English','https://www.etymonline.com/word/add','https://en.wiktionary.org/wiki/addo#Latin'])
W('changing','/ˈtʃeɪndʒɪŋ/','正在改变、更换；变化中的；change 的 -ing 形式',
 '原来的东西、状态换成另一种，或者自己逐渐变样，就是 changing。动作既可以有人主动去做，也可以是情况在变化。',
 'change 去掉末尾不发音 e，加 -ing → changing，保留 /dʒ/。change 经古法语 changier 接拉丁 cambīre、晚期拉丁 cambiāre 的交换、更换词族。',
 [['拉丁交换、更换词族 → 古法语 changier → change','交换、更换 → 改变'],['change 去 e + -ing → changing','进行中的改变；变化着的']],
 'changing the date 更改日期；changing clothes 换衣服；changing weather 变化的天气；changing trains 换乘火车。',
 'a changing situation；is changing quickly。','changing the plan 说主动改计划；the plan is changing 说计划在变。changing trains 常指换乘，changing a train 则可能按具体语境指更换列车本身。',
 ('The town is changing quickly.','这座小镇变化很快。'),('We are changing the date of the workshop.','我们正在更改研习活动的日期。'),sources=['https://en.wiktionary.org/wiki/changing#English','https://en.wiktionary.org/wiki/change#English'])
W('creating','/kriˈeɪtɪŋ/','正在创造、创作；产生、造成；create 的 -ing 形式',
 '让原来还没有的一种东西、安排或情况出现，就是 creating；可以创造图像，也可以造成麻烦。',
 'create 去掉末尾不发音 e，加 -ing → creating。create 接拉丁 creātus、creāre 使产生、创造、生育，更早与生长词族相连；现代 -ing 形式按英语规则变化。',
 [['拉丁 creāre、creātus → 中古英语、英语 create','使产生、创造'],['create 去 e + -ing → creating','正在创作、造成新情况']],
 'creating a design 创作设计；creating jobs 创造工作机会；creating problems 造成问题；creating space 腾出、创造空间。',
 'enjoy creating；creating something new。','create 可以产生好的或坏的情况，具体由宾语决定；creating problems 就是造成问题。make 范围更广，create 常把新事物、新状态的产生放在前面。',
 ('The children are creating a picture from coloured paper.','孩子们正在用彩纸创作一幅图画。'),('The extra meetings are creating more work for everyone.','额外的会议正在给每个人增加工作。'),sources=['https://en.wiktionary.org/wiki/creating#English','https://en.wiktionary.org/wiki/create#English'])
W('providing','/prəˈvaɪdɪŋ/','正在提供、供给；为需要作准备；provide 的 -ing 形式',
 '把别人需要的东西拿出来、安排好，就是 providing；提供空间、信息、食物都可以这样说。',
 'provide 去末尾不发音 e，加 -ing → providing。provide 接拉丁 prōvidēre，prō- 向前与 vidēre 看构成向前看、预先照顾，后来有备好所需、提供义。',
 [['拉丁 prō- + vidēre → prōvidēre → provide','向前看 → 预备、照顾所需'],['provide 去 e + -ing → providing','正在提供、供给']],
 'providing information 提供信息；providing food for visitors 为访客提供食物；providing someone with a map 给某人提供地图。',
 'thanks for providing ...；a way of providing support。','provide someone with something 与 provide something for someone 都常用。providing 后面的对象既可以是实物，也可以是机会、帮助、信息等。',
 ('The library is providing a quiet room for the workshop.','图书馆正在为研习活动提供一间安静的房间。'),('Thank you for providing us with the photographs.','谢谢你给我们提供这些照片。'),sources=['https://en.wiktionary.org/wiki/providing#English','https://en.wiktionary.org/wiki/provide#English'])
W('bringing','/ˈbrɪŋɪŋ/','正在带来、带到；引起、带来某种结果；bring 的 -ing 形式',
 '自己或别人朝某个参照点来，同时带着人、东西或结果，就是 bringing。参照点可以是说话人这里，也可以是双方正谈的目的地。',
 'bring + -ing，直接加；标准词尾 /ŋɪŋ/，中间通常不另加 /ɡ/。bring 继承古英语 bringan，过去式、过去分词 brought 是不规则形式。',
 [['古英语 bringan → 中古英语 → bring','在来到的过程中携带、送来'],['bring + -ing → bringing','正在带来；带来某种影响、结果']],
 'bringing a friend 带朋友来；bringing lunch 带午餐来；bringing people together 把人们聚在一起；bringing change 带来变化。',
 'thanks for bringing ...；bringing the books back。','bring 常向谈话参照点带来，take 常强调从参照点带走、带往别处；carry 更强调携带、承载的动作。具体参照点由对话决定。',
 ('Are you bringing a friend to the party?','你会带一位朋友来参加聚会吗？'),('The new path is bringing more visitors to the village.','新小路正在为村子带来更多访客。'),sources=['https://en.wiktionary.org/wiki/bringing#English','https://en.wiktionary.org/wiki/bring#English'])
W('carrying','英 /ˈkæriɪŋ/；美 /ˈkæriɪŋ/','正在携带、承载；输送、传播；carry 的 -ing 形式',
 '把东西带在身上、托住并运送，是 carrying；车承载旅客，声音、消息被传送，也能延伸这个画面。',
 'carry + -ing，直接保留 y，写 carrying。carry 经盎格鲁法语、古北法语运输动词接车的拉丁、高卢词族，原有用车运的背景，英语后来扩大到各种携带、承载。',
 [['车的拉丁、高卢词族 → 法语运输动词 → carry','用车运输 → 携带、承载、输送'],['carry + -ing → carrying','进行中的携带、运输；承担等']],
 'carrying a bag 提着包；carrying passengers 运载旅客；carrying out a plan 执行计划；carrying on with work 继续工作。',
 'carrying something heavy；carrying the message further。','carry 侧重把东西带着、承载着，bring 常交代朝参照点带来。carry out a task 是执行任务；carry on doing 是继续做，短语各按整体用法记。',
 ('She was carrying a large bag in each hand.','她两只手各提着一个大包。'),('The team is carrying out a survey of local buildings.','团队正在开展一项当地建筑调查。'),sources=['https://en.wiktionary.org/wiki/carrying#English','https://en.wiktionary.org/wiki/carry#English'])
W('falling','英 /ˈfɔːlɪŋ/；美 /ˈfɔːlɪŋ, ˈfɑːlɪŋ/','正在落下、下降；渐入某状态；fall 的 -ing 形式',
 '从高处往下落，是 falling；数量降低、身体倒下，或人慢慢进入睡眠，也可以借这个变化过程理解。',
 'fall + -ing，原有 ll 保留。fall 继承古英语 feallan，经中古英语延续；过去式 fell、过去分词 fallen 与规则的 falling 分开记。',
 [['古英语 feallan → 中古英语 → fall','落下、倒下、下降'],['fall + -ing → falling','下降过程；进入某状态的变化']],
 'falling leaves 落叶；falling prices 下降的价格；falling asleep 正在入睡；falling behind 落后；falling apart 散架、破裂。',
 'snow is falling；falling into place。','falling asleep 是逐渐入睡，sleeping 是已经在睡觉。falling behind 可说进度跟不上，falling into place 可说各部分终于对上、事情逐渐明朗。',
 ('Snow was falling as we left the station.','我们离开车站时，天正下着雪。'),('I was falling asleep when the phone rang.','我快睡着时，电话响了。'),sources=['https://en.wiktionary.org/wiki/falling#English','https://en.wiktionary.org/wiki/fall#English'])
W('allowing','/əˈlaʊɪŋ/','正在允许、让……能够；考虑、留出余地〔allowing for〕',
 '给别人做一件事的许可，或为事情留出足够空间、时间，是 allowing 的两组常见感觉。',
 'allow + -ing，直接加。allow 的法语来源汇合较早拉丁 allocāre 分配、安排与 allaudāre 赞同、认可两条词族，现代许可与留出等义保留了这些影响。',
 [['拉丁分配、赞同两条词族 → 法语相近形式 → allow','安排、认可 → 允许；留出条件'],['allow + -ing → allowing','正在许可；把某条件考虑进去']],
 'allowing visitors to enter 允许访客进入；allowing more time 留出更多时间；allowing for traffic 把交通状况考虑在内。',
 'a design allowing easy access；allowing for mistakes。','allow someone to do 是允许某人做；allow doing 说允许某种活动；allow for something 是把可能的影响、需要预先考虑进去。',
 ('The new door is wider, allowing people to enter more easily.','新门更宽，让人们更容易进入。'),('We left early, allowing for traffic on the way.','我们考虑到路上的交通状况，提前出发了。'),sources=['https://en.wiktionary.org/wiki/allowing#English','https://www.etymonline.com/word/allow'])
W('trading','/ˈtreɪdɪŋ/','交易、买卖；交换；trade 的 -ing 形式',
 '把自己有的东西换成别的，或通过买卖让东西流转，就是 trading；交换卡片和经营商品都有这个交换画面。',
 'trade 去末尾不发音 e，加 -ing → trading。trade 借中古低地德语、荷兰语路径、轨迹词，早期有做事途径、惯常行业等义，后来发展出商贸、交易；英语动词由名词发展。',
 [['低地德语、荷兰语路径词 → 英语 trade','惯常走的路、做法 → 行业、买卖'],['trade 去 e + -ing → trading','进行中的买卖、交换活动']],
 'trading goods 买卖商品；trading cards 交换卡片、供收集交换的卡牌；trading places 交换位置；a trading company 贸易公司。',
 'trading with neighbouring towns；trading one item for another。','trade A for B 是用 A 换 B；trade in something 常说经营某种商品，也可在相应消费语境说以旧换新。trading places 常是交换位置、处境。',
 ('The children spent the afternoon trading cards.','孩子们整个下午都在交换卡片。'),('The company began trading with nearby towns.','这家公司开始与附近城镇开展贸易。'),sources=['https://en.wiktionary.org/wiki/trading#English','https://www.etymonline.com/word/trade'])
W('testing','/ˈtestɪŋ/','测试、检验；正在测试；考验人的、费力的',
 '拿一个东西试试看是否合格，是 testing；如果一件事把人的耐心、能力都拿来考一遍，形容起来也可以是 testing。',
 'test + -ing，直接加。test 经法语接拉丁 testum 陶制容器，英语早有检验金属所用器皿的相关义，再扩到检验品质、能力的动作；testing 又可作形容词。',
 [['拉丁陶制容器词 → 法语、英语 test','检验用器皿 → 检验'],['test + -ing → testing；形容词用法','正在测试；像在考验人的、费力的']],
 'testing the equipment 测试设备；product testing 产品测试；a testing time 艰难、考验人的时期；a testing question 费思量的问题。',
 'careful testing；testing the new design。','testing a machine 是动作，a testing situation 是形容词说情况很考验人。testify 作证另属见证词族，不能只按 test 这些字母把两条来源混起来。',
 ('The team is testing the new design before building a full-size version.','团队正在测试新设计，再制作全尺寸版本。'),('It was a testing week for everyone involved.','对每个参与者来说，那都是充满考验的一周。'),sources=['https://en.wiktionary.org/wiki/testing#English','https://en.wiktionary.org/wiki/test#English'])
def extend_lessons():
 extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_xz',ROOTS,WORDS)
 extend_lessons()
