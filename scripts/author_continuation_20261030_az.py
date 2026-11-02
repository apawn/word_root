"""Spot, floor and rise: places, support surfaces and upward changes."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
SP=[['中古英语 spot、spotte；与低地日耳曼同族及 splott 等形式有关','斑点、小块地方；具体词形关系较复杂'],['现代 spot','点、斑、地点、职位；发现、认出']]
def S(f,m):return SP+[[f,m]]
W('spot','英 /spɒt/；美 /spɑːt/','点、斑；地点、位置；名额；发现、认出',
 '在一大片里面圈出一个小点：污点、具体地方、某个位置；把它从背景里看出来就是 spot。',
 '中古英语 spot、spotte 与低地日耳曼同族词、旧 splott 等形式有关，词形关系并非单一路径。地点、职位及发现义逐步形成。',SP,
 'a spot on the shirt 衬衫污点，a quiet spot 安静地方，a spot on the team 队中名额，spot a mistake 看出错误，on the spot 当场。',
 'a quiet spot；a spot on the team；spot a mistake；on the spot。',
 'spot 发现常有从背景里认出的感觉，notice 注意到范围更广。on the spot 可当场，也可说某处，不总等于在污点上。',
 ('We found a quiet spot beside the lake.','我们在湖边找了个安静地方。'),('Can you spot the mistake in this sentence?','你能看出这句话里的错误吗？'))
W('spotless','英 /ˈspɒtləs/；美 /ˈspɑːtləs/','一尘不染的；毫无污点的',
 '连一个污点都没有；房间是干净，名声是没被什么丑事玷污。',
 'spot + -less，中古英语已有同族形式。后缀缺少接斑点、污点义，不是说地方完全不存在。',S('spot + -less → spotless','无污点 → 洁净、名誉清白'),
 'a spotless kitchen 一尘不染的厨房，a spotless record 清白记录，keep something spotless 保持非常干净。',
 'a spotless kitchen；a spotless record；keep spotless。',
 'spotless 常比 clean 更强调没有一点脏；spotless reputation 清白名誉是比喻，不是在擦洗一张简历。',
 ('Her kitchen was always spotless.','她的厨房总是一尘不染。'),('He had a spotless record throughout his career.','他整个职业生涯记录清白。'))
W('spotty','英 /ˈspɒti/；美 /ˈspɑːti/','有斑点的；长痘的；零散、不稳定的',
 '一处有一处没有，像斑点分布；服务、信号也可时有时无。',
 'spot + -y，中古英语已有同族形容词。间断、不稳定义接分布零散的形象，不必每次真看见圆斑。',S('spot + -y → spotty','多斑点；零散分布 → 不均、不稳定'),
 'a spotty face 长痘脸，spotty coverage 断续、不完整覆盖，spotty service 不稳定服务。',
 'a spotty face；spotty coverage；spotty service。',
 'spotted 有斑点，spotty 还常说不均匀、质量不稳定；a spotty record 可评价表现时好时坏，不只是有个污点。',
 ('The internet connection is spotty in this area.','这个地区网络连接时有时无。'),('The report relies on spotty historical evidence.','报告依靠的是零散、不完整的历史证据。'))
W('spotter','英 /ˈspɒtə/；美 /ˈspɑːtər/','观察、识别的人；辅助观察员；举重保护员',
 '专门盯着看、帮你认出东西或照看动作的人；健身时可在旁保护举重者。',
 'spot + -er，双写 t。接发现、观察和相应辅助动词用法，不只指往衣服上弄污点的人。',S('spot + -er → spotter','执行观察、识别或辅助照看的人'),
 'an aircraft spotter 飞机观察爱好者，a spotter at the gym 健身房举重保护员。',
 'an aircraft spotter；a gym spotter；a trained spotter。',
 'spotter 可观察员或举重辅助者，spectator 多是看比赛、演出的观众；不是所有旁观的人都承担 spotter 的工作。',
 ('The aircraft spotter recognized the plane immediately.','那位飞机观察爱好者立刻认出了机型。'),('She asked a spotter to stand behind the bench.','她请一位举重保护员站在卧推凳后面。'))
R('B3576','斑点、小处和具体位置；发现与分布品质','SPOT：从一大片背景里看一个小点、认一个位置','spot → spotless、spotty、spotter；spotlight、sunspot 既有共享，分光照与太阳斑点。',
 '小点能成为污点、地点或名额；spotty 的不稳定要从分布零散理解，不能只死记多斑点。',
 'spot + -less/-y/-er；spot + light；sun + spot。',
 [['基本点位及性质','spot · spotless · spotty'],['观察者与照明、天象','spotter · spotlight · sunspot']],
 'spotless 无污点可说名誉；spotty coverage 不均；spotter 可辅助角色，不等于一般观众。',
 'The spotter found a quiet spot where the view was clear.\n\n观察员找了个安静、视野清楚的地方。',
 'spot spotless spotty spotter spotlight sunspot')
FL=[['古英语 flōr → 中古英语 flor、floor → floor','地面、铺地、甲板等承托表面'],['现代 floor','地板、楼层；底面、下限；发言权；击倒、使惊呆']]
def F(f,m):return FL+[[f,m]]
W('floor','英 /flɔː/；美 /flɔːr/','地板；楼层；底部、下限；发言权；击倒、难倒',
 '脚下承托你的那一层；楼里一层层叠起来，数值也可设一个不能再低的底。',
 '继承古英语 flōr，已有地面、甲板等义。楼层、下限及会议发言权等分别发展；动词把人打倒到地上，也引申让人惊得不知如何反应。',FL,
 'on the floor 在地板上，the second floor 二层或三层须看地区计层习惯；have the floor 有发言权，a price floor 价格下限。',
 'on the floor；the second floor；have the floor；a price floor。',
 '美式 first floor 常是地面那层，英式通常叫 ground floor，first floor 为上一层。floor 地板不同于 roof 屋顶；动词 be floored 可惊呆、难倒。',
 ('Please put the box on the floor.','请把箱子放在地板上。'),('The question completely floored me.','那个问题把我彻底问住了。'))
W('floorboard','英 /ˈflɔːbɔːd/；美 /ˈflɔːrbɔːrd/','地板木条、地板板材；汽车脚部底板〔也见复数〕',
 '铺成地板的一条条板；车里也可按脚下那块底板称呼。',
 'floor + board 板。不是负责管理一层楼的董事会 board。',F('floor + board → floorboard','地板的板材；另有车辆底板用法'),
 'creaking floorboards 吱嘎响的地板板材，a loose floorboard 松动地板条，under the floorboards 在地板下面。',
 'creaking floorboards；a loose floorboard；under the floorboards。',
 'floor 整个地板、楼层，floorboard 构成它的一块板；board 在这里取材料板义，非委员会。',
 ('One of the floorboards creaked as she crossed the room.','她穿过房间时，一块地板条吱嘎响了一声。'),('They found the letter under a loose floorboard.','他们在一块松动地板下面找到了信。'))
W('underfloor','英 /ˈʌndəflɔː/；美 /ˈʌndərflɔːr/','地板下的',
 '把管线、供暖等放在脚下地板下面，按位置直接描述。',
 'under- 下面 + floor。常在名词前作形容修饰，尤其 underfloor heating 地暖。',F('under- + floor → underfloor','位于地板下面的'),
 'underfloor heating 地暖，underfloor space 地板下空间，underfloor pipes 地板下管道。',
 'underfloor heating；underfloor space；underfloor pipes。',
 'underfloor 地板下面，underground 地下；高层楼里的地暖也可 underfloor，不需要整栋房子在地底。',
 ('The apartment has underfloor heating.','这套公寓装有地暖。'),('The cables run through the underfloor space.','电缆从地板下面的空间穿过。'))
R('B3167','脚下承托表面；楼层、下限与地板下方','FLOOR：脚下的一层，既是表面也可成楼层或底线','floor 先讲常用多义；floorboard 板材、underfloor 位置；seafloor 既有共享。',
 '地板、海底、价格下限可借底面相连；发言权和动词难倒是固定用法，不能每次只靠物理地面猜。',
 'floor + board；under- + floor；sea + floor。',
 [['基本地板、楼层和固定用法','floor'],['材料和位置','floorboard · underfloor · seafloor']],
 '英美楼层计数不同；underfloor 不要求地下；floorboard 材料板；have the floor 正在或获准发言。',
 'Underfloor pipes run beneath the wooden floorboards.\n\n地板下的管道从木地板条下面穿过。',
 'floor floorboard underfloor seafloor')
RI=[['古英语 rīsan → 中古英语 risen → rise','站起、升起、出现'],['现代 rise','上升、上涨、起身；增长、上升等名词用法']]
def I(f,m):return RI+[[f,m]]
W('rise','/raɪz/','上升、上涨；起身；出现、增高；增长〔名词〕',
 '东西自己从低往高走：太阳升，水位涨，人站起来，数量也可以上去。',
 '继承古英语 rīsan，变化 rise—rose—risen。现代通常不及物，讲主语自身升起；相关 raise 使升高经另一同族借入形式，不是 rise 的过去式。',RI,
 'prices rise 价格上涨，rise from a chair 从椅子上起身，rise to the challenge 迎接挑战，a rise in costs 费用增加。',
 'prices rise；rise from；rise to the challenge；a rise in。',
 'The sun rises 太阳升起，raise your hand 举手。rise 通常自己升，raise 通常使某物升；rose 还可同形为玫瑰，按句子区分。',
 ('The water level rose after the rain.','雨后水位上升了。'),('She rose from her chair to greet us.','她从椅子上站起身迎接我们。'))
W('risen','/ˈrɪzn/','rise 的过去分词；已升起、上涨的',
 '不是说昨天升这个过去动作，而是放在 have、be 等结构里表达已经升起的结果或状态。',
 'rise 的历史不规则过去分词，元音变为 /ɪ/，末尾保留 -en 分词形式；过去式是 rose。',RI+[['rise → rose → risen','原形 → 过去式 → 过去分词']],
 'has risen 已经上涨，the sun has risen 太阳已经升起。较正式、宗教语境另可见 the risen ... 的形容用法。',
 'has risen；had risen；the sun has risen。',
 'rose 过去式，risen 分词，raised 则是 raise 的过去、分词。Prices have risen 不写 have rose。',
 ('The price has risen twice this year.','今年价格已经涨过两次。'),('By the time we left, the sun had risen.','我们出发时，太阳已经升起来了。'))
W('arise','/əˈraɪz/','出现、产生；由……引起；起身〔正式〕',
 '问题、机会从原来没有的位置冒出来；现代经常说事情产生，不只说人站起来。',
 '古英语 ārīsan，由旧 ā- + rīsan 组成，现代对应 a- + rise；前部不是希腊语否定。变化 arise—arose—arisen。',RI[:1]+[['古英语 ārīsan → arise','起身、升起 → 产生、出现；来源于']],
 'problems arise 问题出现，an opportunity arises 机会出现，arise from 由……引起。',
 'problems arise；an opportunity arises；arise from。',
 'rise 常上升，arise 常产生；a problem arose 出问题，不表示问题在高度上升。raise a problem 提出问题又是使动结构。',
 ('A new problem arose during testing.','测试时出现了一个新问题。'),('The misunderstanding arose from a vague instruction.','误会由一条含糊指令引起。'))
W('riser','英 /ˈraɪzə/；美 /ˈraɪzər/','早起、晚起的人〔搭配中〕；台阶立板；垫高平台',
 '一个人几点起床，可以叫哪种 riser；建筑、舞台里也用它说竖起或把高度垫起来的部分。',
 'rise + -er，中古英语已有对应形式。人物、构件同围绕升起、立高，但具体名称按行业固定。',I('rise + -er → riser','起身者；竖向、抬高用的构件'),
 'an early riser 早起者，a late riser 晚起者，stair risers 台阶立板，a stage riser 舞台垫高平台。',
 'an early riser；a late riser；stair risers；a stage riser。',
 'riser 单独不一定早起，early 才说明；楼梯 tread 常说踩的水平面，riser 说竖向那块。',
 ('I’m an early riser even at weekends.','即使周末，我也习惯早起。'),('The choir stood on a low riser.','合唱团站在一个低矮的垫高台上。'))
W('moonrise','/ˈmuːnraɪz/','月出；月亮升起的时刻',
 '从地面看，月亮从地平线升出来；前面的 moon 直接说明是谁在 rise。',
 'moon 月亮 + rise 升起，名词组合。不是人把月亮主动举上天。',I('moon + rise → moonrise','月亮升起；相应时刻'),
 'watch the moonrise 看月出，before moonrise 月出之前，the time of moonrise 月出时刻。',
 'watch the moonrise；before moonrise；the time of moonrise。',
 'moonrise 月出，sunrise 日出；这两个是所见天体升起，moonlight、sunlight 则说光。',
 ('We stayed on the beach to watch the moonrise.','我们留在海滩上看月出。'),('The guide listed the time of moonrise.','指南列出了月出时间。'))
R('B2963','从低到高、起身和产生；旧动词变化与使动分清','RISE：自己升起；ARISE：常说事情出现','rise → risen，再 arise → riser；moonrise、sunrise 按天体并列；例句对照 raise。',
 '本族升起动词元音变化保留至今。不要把 raise 当普通拼写变体，也不要把 arise 所有产生义都译成高度增加。',
 'rise—rose—risen；旧 a- + rise → arise—arose—arisen；rise + -er；moon/sun + rise。',
 [['基本升起和分词','rise · risen'],['出现、人物与构件','arise · riser'],['天体升起','moonrise · sunrise']],
 'rise 自升、raise 使升；arise 出现；risen 分词不是 rose；early riser 的 early 才说明早。',
 'A problem arose after the water level had risen.\n\n水位上涨后，出现了一个问题。',
 'rise risen arise riser moonrise sunrise')
if __name__=='__main__':save('continuation_20261030_az',ROOTS,WORDS)
