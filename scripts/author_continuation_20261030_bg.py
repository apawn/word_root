"""Flow and cook, correcting the false flower and cookie derivations."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
FL=[['古英语 flōwan → 中古英语 flowen → flow','流动、流淌'],['现代 flow','液体、气体流动；过程、话语顺畅；流量、心流等名词']]
def F(f,m):return FL+[[f,m]]
W('flow','英 /fləʊ/；美 /floʊ/','流动；流淌；顺畅进行；流量、流动',
 '水一路往前走，没有被卡住；话、工作、想法顺着接下去，也能说 flow。',
 '继承古英语 flōwan，名词由相应流动动作发展。心理学 flow 的心流是后来的专门用法；flower 花不来自 flow + -er。',FL,
 'water flows 水流动，the flow of traffic 车流，ideas flow 想法不断涌来，go with the flow 顺势而为。',
 'water flows；the flow of traffic；ideas flow；go with the flow。',
 'flow 流动过程，flood 可大量水涌入、洪水；flow 不必水量很大。flower 另接法语、拉丁花词，不拿拼写判同源。',
 ('The river flows through the town.','河流穿过小镇。'),('The conversation flowed naturally.','交谈自然顺畅地进行着。'))
W('flowing','英 /ˈfləʊɪŋ/；美 /ˈfloʊɪŋ/','流动的；飘逸、连贯流畅的',
 '水在流，长裙、长发也像顺着气流滑下去；文字连贯也能借流畅的感觉。',
 'flow + -ing，中古英语已有 flowyng 等形式。分词形容词从实际流动延伸到衣料、线条、表达。',F('flow + -ing → flowing','正在流；像流动般飘逸、连贯'),
 'flowing water 流水，a flowing dress 飘逸长裙，flowing handwriting 流畅字迹。',
 'flowing water；a flowing dress；flowing handwriting。',
 'flowing 流动、飘逸，不必是盛水的液体；flowering 开花的接 flower 是另一个词基。',
 ('They rested beside the flowing stream.','他们在流水边休息。'),('She wore a long, flowing dress.','她穿着一条飘逸长裙。'))
W('inflow','英 /ˈɪnfləʊ/；美 /ˈɪnfloʊ/','流入；流入量、流入物',
 '先画一个边界，再看什么从外面进来；钱、人、水都可按进入方向描述。',
 'in- 向内 + flow，有中古英语相关动词形式，名词说流入过程、数量或所流入的东西。',F('in- + flow → inflow','向边界内流动；流入量'),
 'an inflow of water 水流入，an inflow of visitors 游客流入，cash inflow 现金流入。',
 'an inflow of；water inflow；cash inflow。',
 'inflow 流入，outflow 流出；参照边界是谁，决定同一笔流动从哪个角度命名。',
 ('Heavy rain increased the inflow of water into the reservoir.','大雨增加了流入水库的水量。'),('The festival brought a large inflow of visitors.','节日活动吸引了大量游客涌入。'))
W('outflow','英 /ˈaʊtfləʊ/；美 /ˈaʊtfloʊ/','流出；流出量、流出物',
 '仍看同一个边界，这次东西离开内部往外走；不一定是事故或损失。',
 'out- 向外 + flow，旧英语已有相关动词形式，名词由流出动作形成。',F('旧 ūtflōwan 等 → outflow','向外流动；现代对应 out- + flow'),
 'the outflow of water 水流出，control the outflow 控制流出，an outflow of funds 资金流出。',
 'the outflow of；control the outflow；water outflow。',
 'outflow 流出与 leak 泄漏不同；从设计出口正常排水也叫 outflow，不必有破洞。',
 ('A narrow channel controls the outflow from the lake.','一条窄水道控制着湖水流出。'),('The chart compares inflows and outflows each month.','图表比较每月的流入和流出。'))
W('overflow','动词：英 /ˌəʊvəˈfləʊ/、美 /ˌoʊvərˈfloʊ/；名词常重音在前','溢出；挤满；溢流、额外容纳部分',
 '容器满了还继续来，于是越过边缘；人群、情绪太多也可以 overflow。',
 'over- 超出 + flow，古英语 oferflōwan 等旧组合延续。名词与动词重音常有差别，具体连读也受语境影响。',F('古英语 oferflōwan → overflow','流出边缘；现代满溢、过量及备用容纳部分'),
 'the bath overflows 浴缸溢水，overflow with joy 喜悦满溢，overflow parking 额外停车区域。',
 'overflow with；the bath overflows；overflow parking；an overflow pipe。',
 'overflow 超出原容纳范围，outflow 只说流出；正常管道排水 outflow 不必先漫过边缘。',
 ('The bath overflowed while he was answering the phone.','他接电话时，浴缸水溢出来了。'),('The hall was overflowing with people.','大厅里挤满了人。'))
R('B3109','流动、顺畅；流入、流出和超出边缘','FLOW：连续往前流；边界方向和容量分别看','flow → flowing；inflow/outflow 按方向对照，overflow 按容量超出；workflow、airflow 共享。',
 '原自动词族里的 flower 花是误归组，本页排除。flowing 与 flowering 也不能只看相近拼写互推。',
 'flow + -ing；in-/out-/over- + flow；work/air + flow。',
 [['基本流动与连贯','flow · flowing'],['方向和容量','inflow · outflow · overflow'],['具体流动过程','workflow · airflow']],
 'inflow/outflow 依参照边界；outflow 不等于泄漏；overflow 超容量；flower 不来自 flow。',
 'The inflow exceeded the outflow, and the tank began to overflow.\n\n流入量超过流出量，水箱开始溢水。',
 'flow flowing inflow outflow overflow workflow airflow')
ROOTS[-1]['exclude']['flower']='花义及其动词来自 flower 名词，接法语、拉丁花词，不是 flow + -er。'
CO=[['拉丁 cocus、coquus 等 → 古英语 cōc → cook','厨师；相关烹调动词也很早进入日耳曼语、英语'],['现代 cook','做饭、烹调；厨师；加工编造等比喻']]
def C(f,m):return CO+[[f,m]]
W('cook','/kʊk/','烹调、做饭；厨师；编造、篡改〔特定搭配〕',
 '把食材加热、处理成能吃的一餐；按这个工作也把做饭的人叫 cook。',
 '很早借入的拉丁厨师、烹调词系，古英语有 cōc 等形式；不能当现代 cook 就是无来源的拟声。cook the books 后来比喻篡改账目。',CO,
 'cook dinner 做晚饭，a good cook 手艺好的做饭者，cook through 完全熟透，cook the books 做假账。',
 'cook dinner；a good cook；cook through；cook the books。',
 'cook 人或动作，cooker 常是器具；chef 常指专业厨师、主厨，a good cook 可以只是家里做饭好的人。',
 ('I’ll cook dinner tonight.','今晚我来做饭。'),('My father is a very good cook.','我父亲做饭很拿手。'))
W('cooking','/ˈkʊkɪŋ/','烹饪、做饭；烹饪风格；烹调用的',
 '说做饭这件事，也说做出来的手艺、风格；cooking oil 则按用途叫烹调用油。',
 'cook + -ing，名词、形容修饰接烹调活动。看组合结构，不要把 cooking oil 读成油正在做饭。',C('cook + -ing → cooking','烹饪活动、手艺；烹调用途'),
 'home cooking 家常烹饪，cooking oil 烹调用油，a cooking class 烹饪课，do the cooking 负责做饭。',
 'home cooking；cooking oil；a cooking class；do the cooking。',
 'cooking 活动、手艺，cooker 器具；a cooking class 是教烹饪的课，不是教如何当 cooking 这个人。',
 ('He enjoys home cooking more than restaurant food.','他比起餐馆菜更喜欢家常饭菜。'),('We signed up for a cooking class.','我们报名参加了烹饪课。'))
W('cooker','英 /ˈkʊkə/；美 /ˈkʊkər/','炉灶、炊具；某类烹饪器具',
 '人是 cook，用来做饭的装置常是 cooker；前面加 rice、pressure，就知道主要怎么用。',
 'cook + -er，常作器具名。英式 cooker 可指炉灶整机；复合词里广泛用于电饭煲、压力锅等。',C('cook + -er → cooker','烹调器具、炉灶'),
 'a gas cooker 燃气灶，a rice cooker 电饭煲，a pressure cooker 压力锅。',
 'a gas cooker；a rice cooker；a pressure cooker。',
 'cook 做饭的人，cooker 常是器具；称赞厨艺通常说 a good cook，不机械说 a good cooker。',
 ('The kitchen has a gas cooker.','厨房里有一台燃气灶。'),('The rice cooker keeps the rice warm.','电饭煲让米饭保持温热。'))
W('cookery','/ˈkʊkəri/','烹饪；烹调技艺〔英式较常见〕',
 '把做饭当一门技艺来学、来谈；常见于课程、书名。',
 'cook + -ery，中古英语已有 cokerie 等形式。后缀这里说活动、技艺，不是每个 -ery 都是某种店铺。',C('中古英语 cokerie → cookery','烹调活动与技艺'),
 'a cookery course 烹饪课程，a cookery book 烹饪书，learn cookery 学烹饪。',
 'a cookery course；a cookery book；a school of cookery。',
 'cookery 与 cooking 常有重合，cookery 在英式课程、书籍名称里较常见；都不是厨房房间的普通名称。',
 ('She took a cookery course at the local college.','她在当地学院上了烹饪课。'),('The book introduces basic cookery techniques.','书里介绍基础烹调技法。'))
W('cookware','英 /ˈkʊkweə/；美 /ˈkʊkwer/','炊具；锅具等烹饪器皿',
 '做饭用的锅、煎锅等这一整类器物；ware 把它们归成用品。',
 'cook + -ware 制品、器物。通常不可数，不等于所有拿来吃饭的盘、叉、杯。',C('cook + ware → cookware','烹饪用的器物、炊具'),
 'nonstick cookware 不粘锅具，stainless steel cookware 不锈钢炊具，a set of cookware 一套锅具。',
 'nonstick cookware；stainless steel cookware；a set of cookware。',
 'cookware 做饭用，tableware 摆桌吃饭用，cutlery 刀叉匙等餐具；用途不同，实际范围可能相交。',
 ('The shop sells stainless steel cookware.','店里出售不锈钢炊具。'),('They bought a new set of cookware for the kitchen.','他们给厨房买了一套新锅具。'))
W('overcook','英 /ˌəʊvəˈkʊk/；美 /ˌoʊvərˈkʊk/','煮过头；烹调过度',
 '该停的时候没停，食材煮得太软、肉太干；关注超过合适程度。',
 'over- 过量、超过 + cook。并非必然烧焦，也可能只是质地、口感过了。',C('over- + cook → overcook','烹调超过合适时间、程度'),
 'overcook the pasta 把意面煮过头，overcooked vegetables 煮太烂的蔬菜。',
 'overcook the pasta；overcooked vegetables；avoid overcooking。',
 'overcook 过熟、煮过头，burn 烧焦；一份意面过软可 overcooked，却没有焦黑。',
 ('Be careful not to overcook the pasta.','注意别把意面煮过头。'),('The vegetables were overcooked and mushy.','蔬菜煮过头，软烂了。'))
W('cookie','/ˈkʊki/','曲奇、甜饼〔美式〕；网站小型数据记录',
 '吃的是小甜饼，浏览器里的 cookie 则是网站保存、读取的一小份数据；两种场景先分清。',
 '借荷兰语 koekie、koekje 等 cake 小称形式，不能拆成英语 cook + -ie。计算机义接 magic cookie 等既有技术比喻，不由烤饼工序直接推到网页。',
 [['荷兰语 koek〔饼〕+ 小称形式 → cookie','小饼；不是英语 cook 加后缀'],['技术比喻 magic cookie 等 → 网络 cookie','小型数据记录的专门名称']],
 'a chocolate chip cookie 巧克力豆曲奇，accept cookies 接受网站 cookie，delete cookies 删除相关浏览数据。',
 'a chocolate chip cookie；accept cookies；delete cookies。',
 'cookie 在本页是形似辨析，不是 cook 后代。网络 cookie 不是程序、病毒的统一名称，也不保证每份都只记录同一种信息。',
 ('She offered me a chocolate chip cookie.','她给了我一块巧克力豆曲奇。'),('The website uses a cookie to remember your language choice.','网站用一份 cookie 记住你的语言选择。'))
R('B3013','烹调与厨师、器具；cookie 单作形似辨析','COOK：做饭、做饭的人；COOKIE 不能硬拆进来','cook → cooking、cooker、cookery、cookware；cookbook 共享，cookout 户外，overcook 过度；cookie 明确是不同来源的辨析参照。',
 '烹调词系很早借入，后缀有活动、人、器具区别。cookie 源自荷兰小饼词，不为了凑词族把拼写相近当同源。',
 'cook + -ing/-er/-ery/-ware/book/out；over- + cook；另源 Dutch koek 小称 → cookie。',
 [['动作、活动、器具和手艺','cook · cooking · cooker · cookery · cookware · cookbook'],['户外聚会与煮过头','cookout · overcook'],['形似辨析：不是 cook 后代','cookie']],
 'cook 人、cooker 器具；cookware 炊具、tableware 餐具；cookout 现场户外做饭、picnic 可带现成食物；cookie 不能 cook+-ie。',
 'The cook checked the cooker and cookware before the cookout.\n\n厨师在户外聚餐前检查了炉灶和锅具。',
 'cook cooking cooker cookery cookware cookbook cookout overcook cookie')
if __name__=='__main__':save('continuation_20261030_bg',ROOTS,WORDS)
