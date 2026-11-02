"""Exchange and lake: reciprocal giving and the geography around a lake."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
X=[['通俗拉丁语重建形 *excambiāre → 法语 eschanger、eschange','交换、更换；有 ex- 与交换词基背景'],['中古英语 eschaungen、eschaunge → exchange','词形后来向 ex- 调整；交换、兑换和交易场所等']]
def XH(f,m):return X+[[f,m]]
W('exchange','/ɪksˈtʃeɪndʒ/ 或 /eksˈtʃeɪndʒ/','交换、兑换；交流；交易所',
 '我把一样东西给你，你把另一样东西给我。交换物品、货币、意见，核心都有往来，而不只是单方面改变。',
 '名词、动词经法语 eschange、eschanger 等进入中古英语，后来拼写调整成 ex-。现代可对照 change 认识，但不能只说现代英语 ex + change 临时造出全部历史。',X,
 'exchange gifts 交换礼物，exchange ideas 交流想法，exchange dollars for euros 把美元兑换成欧元，a stock exchange 证券交易所。',
 'exchange A for B；exchange ideas；an exchange student；the exchange rate。',
 'change 改变，exchange 交换、更换；exchange A for B 是拿出 A 换得 B，别把方向倒过来。',
 ('We exchanged phone numbers after the meeting.','会后我们交换了电话号码。'),('She exchanged the shirt for a larger size.','她把衬衫换成了大一号的。'))
W('exchangeable','/ɪksˈtʃeɪndʒəbəl/','可交换、可兑换、可更换的',
 '可以拿它去换别的东西。具体能换什么、按什么规则换，要看后面的 for 和实际语境。',
 'exchange + -able，形成能被交换的形容词，保留 e；并非所有以 e 结尾的词接后缀都去 e。',XH('exchange + -able → exchangeable','可以交换、换取其他东西的'),
 'exchangeable for cash 可兑现金，exchangeable tickets 可更换的票券；具体限制由票券条款说明。',
 'exchangeable for；freely exchangeable；exchangeable goods。',
 'exchangeable 可交换，interchangeable 可互换使用；两种零件能互相顶替使用，通常说 interchangeable，不只是可以买卖换手。',
 ('These vouchers are exchangeable for meals.','这些券可换餐食。'),('The item is exchangeable for another size.','这件商品可以换其他尺码。'))
W('exchanger','英 /ɪksˈtʃeɪndʒə/；美 /ɪksˈtʃeɪndʒər/','交换者；交换器',
 '把交换这个动作交给一个人或设备来做。技术里常见 heat exchanger，让热量从一边传给另一边。',
 'exchange + -er，形成执行、实现交换的人或设备名。词尾 e 与 -er 衔接，不额外再写一个 e。',XH('exchange + -er → exchanger','实现交换的人或设备'),
 'a heat exchanger 换热器，a currency exchanger 货币兑换者或兑换机构。设备交换的可以是能量，不一定是两个盒子来回搬。',
 'a heat exchanger；a currency exchanger；an industrial exchanger。',
 'exchanger 设备、参与者，exchange 交换过程或场所；heat exchanger 不是加热器 heater 的完全同义词。',
 ('The engineer inspected the heat exchanger.','工程师检查了换热器。'),('The exchanger transfers heat between the two fluids.','换热器在两种流体之间传递热量。'))
R('B3639','彼此交换；兑换、更换和交流','EXCHANGE：拿出一物，换来另一物；双方有往来','exchange → exchangeable → exchanger，按动作、可能性、实现者排序。',
 '保留法语借入和拼写调整背景。交换礼物、意见、货币以具体例子联系；交换器按技术常见搭配理解。',
 'exchange + -able/-er；exchange A for B；exchange something with someone。',
 [['交换及派生','exchange · exchangeable · exchanger']],
 'exchange 与 change 不完全同义；exchangeable 可换、interchangeable 可互换使用；exchanger 不只人物。',
 'We exchanged the vouchers for food.\n\n我们拿那些券换了食物。','exchange exchangeable exchanger')
L=[['古英语 lacu〔溪流、水池等〕；法语 lac〔接拉丁语 lacus〕','本族与借入的水体名词背景'],['中古英语 lake、lac → lake','形式、意义相互影响或合流，现代常指湖']]
def LH(f,m):return L+[[f,m]]
W('lake','/leɪk/','湖、湖泊',
 '陆地中间聚着一大片水，先抓内陆水体的画面。英语 lakeside、lakeshore 等都围绕它定位。',
 '现代水体义涉及古英语 lacu 与法语 lac〔拉丁语 lacus〕两条背景，在中古英语阶段相互影响、合流。词典对各条贡献的表述不同，不把路线压成只有一个借词祖先。另有颜料、方言玩耍等同形词，此处暂略。',L,
 'a freshwater lake 淡水湖，by the lake 在湖边，a frozen lake 冻结的湖。Lake Victoria 等名称常把 Lake 放前，the Great Lakes 则是另一种固定名称。',
 'by the lake；a freshwater lake；a frozen lake；the lakeshore。',
 'lake 湖，pond 池塘通常较小，但不存在一条词义自己规定、处处通用的面积界线；river 河流更突出水沿河道流动。',
 ('We walked around the lake before breakfast.','早饭前我们绕湖散了步。'),('The lake was completely frozen in winter.','冬天湖面完全冻结了。'),
 sources=['https://en.wiktionary.org/wiki/lake#English','https://www.etymonline.com/word/lake'])
W('lakeside','/ˈleɪksaɪd/','湖边、湖畔；湖边的',
 '不在水中央，而在湖的边上；可以说地点，也可以形容建在那个位置的房屋。',
 'lake 湖 + side 边，形成名词、形容词。',LH('lake + side → lakeside','湖边；位于湖边的'),
 'a lakeside cottage 湖边小屋，a lakeside walk 湖畔散步，at the lakeside 在湖边。',
 'a lakeside cottage；a lakeside village；at the lakeside。',
 'lakeside 湖边位置，lakeview 强调看得见湖；一间能看见湖的房间未必紧挨岸边。',
 ('They rented a lakeside cottage for the summer.','他们租了一间湖边小屋过夏天。'),('We had lunch at a lakeside café.','我们在湖畔咖啡馆吃了午饭。'))
W('lakeshore','英 /ˈleɪkʃɔː/；美 /ˈleɪkʃɔːr/','湖岸、湖滨',
 '把视线放在湖水碰到陆地的那条岸上。可以沿着它走，也可以有石头、芦苇和村镇。',
 'lake 湖 + shore 岸，合成湖泊岸边的名词。',LH('lake + shore → lakeshore','湖水与陆地相接的岸边'),
 'along the lakeshore 沿湖岸，a rocky lakeshore 多石湖岸，lakeshore development 湖滨开发。',
 'along the lakeshore；a rocky lakeshore；on the lakeshore。',
 'lakeshore 强调岸地带，lakeside 范围较宽地说湖边；seashore 海岸，前一成分决定水体。',
 ('A narrow path runs along the lakeshore.','一条窄路沿湖岸延伸。'),('Reeds grow near the quiet lakeshore.','宁静的湖岸附近长着芦苇。'))
W('lakeland','/ˈleɪklənd/','多湖地区、湖区',
 '一片地方以许多湖泊为特色，就把湖和陆地合在一起叫它。',
 'lake 湖 + land 地区，形成多湖地带的名称、描述。大写 Lakeland 还可作具体地名，不能每次都按同一城市理解。',LH('lake + land → lakeland','多湖泊的地区、湖区'),
 'a lakeland landscape 湖区景观，lakeland scenery 湖区风光；英语英国语境大写用法常联系湖区，但仍须看具体上下文。',
 'lakeland scenery；a lakeland landscape；a lakeland village。',
 'lakeland 以湖泊为特色的地区，lakeshore 某个湖的岸；lakefront 更常说临湖前沿位置、地段。',
 ('The painting captures the quiet beauty of the lakeland landscape.','这幅画表现了湖区景色的宁静之美。'),('They explored several small lakeland villages.','他们游览了几个湖区小村庄。'))
R('B3037','内陆湖泊；湖边、湖岸与多湖地区','LAKE：一片内陆水体，周围地点按相对位置命名','lake → lakeside、lakeshore、lakefront、lakeview、lakeland，按边、岸、前沿、景观、地区区分。',
 '水体义有本族与法语借词合流背景。laker 还有不同来源和专门用法，本轮先略；已有湖景、临湖精讲复用。',
 'lake + side/shore/front/view/land。',
 [['水体与周边位置','lake · lakeside · lakeshore · lakefront · lakeview'],['湖区','lakeland']],
 'lakeside 在湖边，lakeview 看得见湖，未必同一位置；lakeshore 湖岸；lakeland 地区不是一个湖本身。',
 'Our lakeside room had a beautiful view of the lake.\n\n我们的湖边房间能清楚地看见湖景。','lake lakeside lakeshore lakefront lakeview lakeland')
if __name__=='__main__':save('continuation_20261030_cb',ROOTS,WORDS)
