"""Busy, business, stop, numb: everyday words with important source distinctions."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
def C(a,b,name,meaning):return [[f'英语 {a}；{b}','并列组合的两部分'],[f'{a} + {b} → {name}',meaning]]
BUSY=[['古英语 bisiġ → 中古英语 bisy / busie','忙碌、勤勉、被事务占住'],['英语 busy','忙；繁忙的；使忙于']]
W('busy','/ˈbɪzi/','忙碌的；繁忙的；使忙于',
 '时间、注意力被事情占着；街道也可以被人车活动占得热闹。',
 '接古英语 bisiġ，经中古英语不同地区形式延续。拼写 u 与现代读音 /ɪ/ 来自不同历史方言影响，不读成普通 bus“公交车”再加 y。',BUSY,
 'busy with work 是忙于工作，busy doing something 是忙着做事；a busy road 是繁忙道路。busy oneself with something 可说让自己忙于某事，较书面。',
 'busy with；busy doing；a busy street；keep someone busy。',
 'busy 忙碌，business 商业事务，busyness 忙碌状态；把事情排得很满，不自动说明都在做生意。',
 ('I’m busy preparing for tomorrow’s meeting.','我正忙着准备明天的会议。'),('The café is on a busy street.','咖啡馆位于繁忙街道上。'))
W('busily','/ˈbɪzɪli/','忙碌地；积极不停地',
 '看他手里的活一直没停，动作接着动作。',
 'busy 的 y 变 i 后加 -ly，接中古英语 busily、bisili 等形式；读音保留 busy 的 /ˈbɪzi/ 这一词族基础。',BUSY+[['busy → busi- + -ly → busily','以忙碌方式做事']],
 'busily preparing 是忙着准备，busily writing 是不停地写；重点是动作状态，不保证事情有效率或价值高。',
 'busily preparing；busily writing；busily working。',
 'busily 修饰动作，busy 修饰人、地方或用在系动词后。She is busy 与 She is working busily 结构不同。',
 ('The volunteers were busily arranging the chairs.','志愿者正忙着摆椅子。'),('She typed busily while the others discussed the plan.','别人讨论计划时，她忙着打字。'))
W('busyness','/ˈbɪzinəs/','忙碌状态；繁忙',
 '不是在谈一家公司赚什么钱，而是在谈日程有多满、事务有多少。',
 'busy + -ness，现代特意保留 y 来区别已分化的 business。两者历史材料相关，现代 busyness 仍读出 busy 的两个音节，再加 -ness。',BUSY+[['busy + -ness → busyness','忙碌、事务繁多的状态']],
 'the busyness of daily life 是日常生活的繁忙，constant busyness 是持续忙碌。常用于反思生活节奏，不是 business 的任意换拼。',
 'the busyness of life；constant busyness；escape the busyness。',
 'busyness /ˈbɪzinəs/ 忙碌，business /ˈbɪznəs/ 生意、事务；中间音节和含义都要分清。',
 ('She needed a break from the busyness of city life.','她需要暂时离开城市生活的繁忙。'),('Constant busyness left little time for reflection.','一直忙碌让人几乎没时间思考。'))
W('business','/ˈbɪznəs/，也 /ˈbɪznɪs/','商业；生意；企业；事务；职责范围',
 '最早是人忙着处理的事情，现代很大一支专指经营、交易及为此成立的企业。',
 '接古英语 bisiġnes、中古英语 businesse 等，历史对应 busy + -ness。后来商业、事务义独立发展，读音压缩；现代普通忙碌另写 busyness。',BUSY[:1]+[['古英语 bisiġnes → 中古英语 businesse → business','忙碌、事务 → 商业、企业等']],
 'start a business 是创业，do business with 是与人做生意，on business 是出差办事；none of your business 是与你无关，语气可能生硬。',
 'start a business；do business with；on business；mind one’s own business。',
 'business 泛指商业时常不可数，a business 是一家企业。business hours 是营业时间，不是只说员工忙了多少小时。',
 ('She runs a small business from home.','她在家经营一家小企业。'),('He is in London on business.','他在伦敦办事出差。'),('Let’s get down to business.','我们开始谈正事吧。'))
W('businessman','/ˈbɪznəsmən/','商人；商界男性人士',
 '把一个人的主要工作放在经营和商业活动这一边来介绍。',
 'business + man，后半常弱读 /mən/，复数 businessmen。business 本身读音已压缩，不逐个念成 busy + ness + man。',C('business','man','businessman','从事商业活动的男性'),
 'a local businessman 是当地商人，a successful businessman 是事业有成的商人；不保证每个人都是公司唯一老板。',
 'a local businessman；a successful businessman；a retired businessman。',
 'businessman 偏商界身份，entrepreneur 常突出创办、开拓事业；businessperson 是不限定性别的对应称呼。',
 ('A local businessman donated books to the school.','当地一位商人向学校捐了书。'),('Her father was a businessman who travelled frequently.','她父亲是位经常出差的商人。'))
W('businesswoman','/ˈbɪznəswʊmən/','女商人；商界女性人士',
 '职业在商业经营领域，称呼同时说明这是一位女性。',
 'business + woman，复数 businesswomen，后半 woman /ˈwʊmən/ 与 women /ˈwɪmɪn/ 的元音不同。',C('business','woman','businesswoman','从事商业活动的女性'),
 'a successful businesswoman 是事业有成的商界女性，a local businesswoman 是当地女商人；具体行业、职位须另说明。',
 'a successful businesswoman；a local businesswoman；an experienced businesswoman。',
 'businesswoman 是商业身份，working woman 是有工作、在职女性更泛；学校教师也可能是 working woman，却不因此就是商人。',
 ('She became a successful businesswoman in the fashion industry.','她在时装行业成为事业有成的商界女性。'),('The panel included businesswomen from several cities.','小组嘉宾包括来自几个城市的商界女性。'))
W('businesslike','/ˈbɪznəslaɪk/','务实高效的；公事公办的',
 '先抓正事和安排，少绕弯、少闲聊，让事务顺畅完成。',
 'business + -like，-like 表像某种做事方式。强调专业、务实态度，不一定真在公司里做商业交易。',C('business','-like','businesslike','像处理正事一样务实、有条理'),
 'a businesslike manner 是干练的态度，a businesslike approach 是务实处理方式。可以友好，也可能显得冷静直接，不等于不礼貌。',
 'a businesslike manner；a businesslike approach；brisk and businesslike。',
 'businesslike 评价做事方式，busy 说忙不忙；一个人忙得团团转，也可能缺少条理。',
 ('She handled the discussion in a calm, businesslike manner.','她以冷静务实的方式处理讨论。'),('The meeting was short and businesslike.','会议简短而高效。'))
R('B3433','忙碌；被事务占据','BUSY：时间和注意力正在被事情占着','人忙着做，街上忙着来来往往；讲忙碌状态与商业活动时，拼写和读音会分开。',
 'busy 接古英语 bisiġ；现代拼写 u 不按 bus 的元音来读。business 与 busyness 虽同源相关，却已成为两个不同常用名词。',
 'busy → busily → busyness 先讲普通忙碌；business 的商业、事务义单列比较，busybody 为已讲的爱管闲事人物词。',
 [['忙碌状态及方式','busy · busily · busyness'],['分化后的事务与人物','business · busybody']],
 'busy /ˈbɪzi/，busyness /ˈbɪzinəs/；business /ˈbɪznəs/ 已压缩。busybody 不只是忙碌的人。',
 'She was busily arranging her schedule, trying to reduce unnecessary busyness.\n\n她忙着安排日程，想减少无谓的忙碌。','busy busily busyness business busybody')
R('B2930','商业；企业；事务与正事','BUSINESS：把经营或需要处理的事务组织起来','一家店是 a business，谈正事是 get down to business；不只用赚钱一个画面解释所有用法。',
 'business 历史接 busy + -ness 的旧形式，现代商业、企业、事务义与普通 busyness 分化。读音中间通常压缩。',
 'business 先讲经营、企业和事务，再按人物 businessman、businesswoman、businessperson 与方式 businesslike 展开；agribusiness 为共享讲解。',
 [['商业与人物','business · businessman · businesswoman · businessperson'],['方式与行业组合','businesslike · agribusiness']],
 'businesslike 干练不等于很忙；a business 企业可数，泛商业通常不可数。businessperson 不限定性别。',
 'The businesswoman ran her business in a friendly but businesslike way.\n\n那位女商人以友好而务实的方式经营企业。','business businessman businesswoman businessperson businesslike agribusiness')
STOP=[['古英语 stoppian → 中古英语 stoppen','堵住、封闭；停止'],['英语 stop','停下；阻止；堵塞；停靠点']]
W('stop','英 /stɒp/；美 /stɑːp/','停止；阻止；停靠站；堵住',
 '流动、行进、继续做事的过程，在这里被截住。',
 '接古英语 stoppian、中古英语 stoppen，早有堵、封闭等义；更远来源有不同分析，不把它拆成 s + top“顶”。',STOP,
 'stop the car 是让车停，stop talking 是停止说话，stop to talk 是停下别的事去说话；a bus stop 是公交站，stop a leak 是堵漏。',
 'stop doing；stop to do；stop someone from doing；a bus stop。',
 'stop doing 停止这个动作，stop to do 为了做这个动作而停；I stopped reading 与 I stopped to read 意思不同。',
 ('Please stop talking for a moment.','请暂时停止说话。'),('We stopped to look at the view.','我们停下来欣赏景色。'),('The bus stop is opposite the library.','公交站在图书馆对面。'))
W('stopped','英 /stɒpt/；美 /stɑːpt/','停止了；停着的；被堵住的',
 '动作已经停下来，或者结果是处在不再运动的状态。',
 'stop + -ed，双写 p，-ed 在此读 /t/，不是多加一个 /ɪd/ 音节。既可过去式、过去分词，也可形容停止后的状态。',STOP+[['stop + -ed → stopped','停下的动作或其结果状态']],
 'a stopped car 可说停住的车，a stopped clock 是停了的钟；stopped up 在一些语境说被堵住。是否正式停放、故障或临时停下须看上下文。',
 'a stopped clock；a stopped car；have stopped；stopped up。',
 'stopped 只是停下的状态，parked 通常是停放车辆；车辆在红灯前 stopped，不一定是 parked。',
 ('The clock stopped during the night.','钟在夜里停了。'),('The stopped car blocked the narrow entrance.','停住的车挡住了狭窄入口。'))
W('stoppage','英 /ˈstɒpɪdʒ/；美 /ˈstɑːpɪdʒ/','停顿；中断；阻塞',
 '原本连续的工作、比赛或流动，中间断开一段。',
 'stop + -age，双写 p，-age 表动作、结果等名词；不是停了多少岁 age。',STOP+[['stop + -age → stoppage','停止、中断或堵塞的情况']],
 'a work stoppage 是停工，a stoppage in play 是比赛中断，stoppage time 是足球补时这一名称。不同场景不必都有人罢工。',
 'a work stoppage；a stoppage in play；stoppage time。',
 'stop 可以是动词或某次停靠，stoppage 更突出过程被中断的情况；station 是设施地点，不是中断本身。',
 ('A machine fault caused a brief stoppage.','机器故障导致短暂停工。'),('There were several stoppages during the match.','比赛期间出现了几次中断。'))
W('stopper','英 /ˈstɒpə/；美 /ˈstɑːpər/','塞子；阻止某事的人或物',
 '塞在开口处，让里面的液体不流出、外面的东西不进来。',
 'stop + -er，双写 p；既可执行停止作用的人，也可器具，常见容器塞子义。',STOP+[['stop + -er → stopper','阻止者、堵口物 → 塞子']],
 'a bottle stopper 是瓶塞，a glass stopper 是玻璃塞；a showstopper 已有表演精彩或阻断项目等固定用法，不能只按一只塞子理解。',
 'a bottle stopper；a glass stopper；remove the stopper。',
 'stopper 按封口作用命名，cork 先是软木材料，也常指软木塞；玻璃做的塞子可叫 stopper，不会因此变成软木。',
 ('She removed the glass stopper from the bottle.','她从瓶口取下玻璃塞。'),('The rubber stopper fitted tightly.','橡胶塞塞得很紧。'))
W('stopwatch','英 /ˈstɒpwɒtʃ/；美 /ˈstɑːpwɑːtʃ/','秒表；计时器',
 '从一个起点开始计数，动作结束再按停，读出持续了多久。',
 'stop + watch（表、计时器），按可启停计时的用途命名；不是停了不走的坏表。',C('stop','watch〔计时表〕','stopwatch','可启停以测持续时长的计时器'),
 'start a stopwatch 是开始计时，stop the stopwatch 是停止计时；实体表、手机软件都可实现这一类功能。',
 'start a stopwatch；use a stopwatch；a digital stopwatch。',
 'stopwatch 测已过去多久，countdown timer 倒数还剩多久；一个应用可以都有，但功能方向不同。',
 ('The coach timed the run with a stopwatch.','教练用秒表给跑步计时。'),('She started the stopwatch as the experiment began.','实验开始时，她启动了秒表。'))
W('stopgap','英 /ˈstɒpɡæp/；美 /ˈstɑːpɡæp/','权宜之计；临时填补空缺的',
 '缺口先塞上一块，让事情能运转，之后还要找长期办法。',
 'stop（堵住）+ gap（缺口），从堵缺口的表达形成名词，再作修饰语；不是先停下来制造一个空隙。',C('stop〔堵住〕','gap','stopgap','填住空缺 → 临时措施'),
 'a stopgap solution 是暂时解决办法，a stopgap appointment 是临时任命。词通常暗含这不是最终安排。',
 'a stopgap solution；a stopgap measure；as a stopgap。',
 'stopgap 临时顶上，permanent solution 长久解决；临时措施也可能有用，不等于完全无效的办法。',
 ('The extra bus service was introduced as a stopgap.','增加的巴士服务是作为临时措施推出的。'),('They need a lasting plan, not just a stopgap solution.','他们需要长久计划，不能只有权宜之计。'))
W('stoplight','英 /ˈstɒplaɪt/；美 /ˈstɑːplaɪt/','交通信号灯〔尤美〕；刹车灯〔另用法〕',
 '道路上的灯给车辆传达停走信号；车辆上的灯也可显示正在制动。',
 'stop + light，按停止信号的用途命名，不是说灯泡本身不再发光。',C('stop','light','stoplight','指示停行的交通灯；制动信号灯'),
 'at the stoplight 常是交通灯路口，美式常见；汽车维修语境里可能是刹车灯。traffic light 也是交通信号灯常见称呼。',
 'at the stoplight；a red stoplight；a broken stoplight。',
 'stoplight 的交通灯义与 headlight 前照灯不同；听到灯坏了，要按车辆部位或路口场景辨认。',
 ('We met at the café beside the stoplight.','我们在交通灯旁的咖啡馆见面。'),('The driver pointed out a broken rear stoplight.','司机指出了一盏坏掉的后刹车灯。'))
W('doorstop','英 /ˈdɔːstɒp/；美 /ˈdɔːrstɑːp/','门挡；很厚重的书〔比喻〕',
 '一块楔子或固定挡块，限制门移动；很厚的大书也被玩笑说能拿来挡门。',
 'door + stop，按阻止门运动的作用命名。可以挡开门、避免撞墙等，不只某一种放在地上的重物。',C('door','stop','doorstop','限制门移动的装置；厚重大书的比喻'),
 'a rubber doorstop 是橡胶门挡，a wedge doorstop 是楔形门挡；a doorstop of a novel 是一本厚得像砖的小说。',
 'a rubber doorstop；a wedge doorstop；use something as a doorstop。',
 'doorstop 挡门移动，door lock 锁门，door handle 开关门的把手；同在门上，功能不同。',
 ('She used a rubber doorstop to keep the door open.','她用橡胶门挡让门保持敞开。'),('The novel is a real doorstop, with more than a thousand pages.','小说真像块挡门砖，有一千多页。'))
W('shortstop','英 /ˈʃɔːtstɒp/；美 /ˈʃɔːrtstɑːp/','游击手〔棒球〕',
 '棒球内野里，有一个负责相应区域防守的固定位置，中文叫游击手。',
 'short + stop，是棒球位置的历史固定名称，通常在二垒与三垒之间一带防守。不是所有短暂停留都用这个连写词。',C('short','stop','shortstop','棒球中特定内野防守位置'),
 'play shortstop 是担任游击手，the team’s shortstop 是队里的游击手；名称不表示运动员必须身材矮小。',
 'play shortstop；the team’s shortstop；a skilled shortstop。',
 'shortstop 是球员位置，short stop 分开才可能说短暂停留；空格和固定命名会改变理解。',
 ('She played shortstop on the school baseball team.','她在校棒球队担任游击手。'),('The shortstop made an excellent catch.','游击手完成了一次精彩接球。'))
R('B3132','停止、堵住；截断继续过程','STOP：让正在进行的运动、活动或流动停住','车停下，话停下，洞口堵住；不同对象都在讲截住继续这一动作。',
 'stop 接古英语 stoppian、中古英语 stoppen，早有堵塞、封闭义。更远来源有不同分析，不因拼写里有 top 就归顶部词族。',
 'stop → stopped → stoppage → stopper，先讲动作、结果、中断和堵口物；stopwatch、stopgap、stoplight、doorstop 按用途展开，shortstop 作为棒球固定位置单列。nonstop、backstop 为共享讲解。',
 [['动作、状态、中断与器具','stop · stopped · stoppage · stopper'],['计时、过渡、信号和挡门','stopwatch · stopgap · stoplight · doorstop'],['固定组合及运动位置','shortstop · nonstop · backstop']],
 'stop doing 停止做，stop to do 停下去做；stopped 的 -ed 读 /t/。stopwatch 是正常计时器，不是坏表；stopgap 临时填空。',
 'We stopped to check the stopwatch, then used a stopgap plan to finish on time.\n\n我们停下来查看秒表，再用临时方案按时完成。','stop stopped stoppage stopper stopwatch stopgap stoplight doorstop shortstop nonstop backstop')
NUMB=[['古英语 niman → 中古英语 nimen 的分词 nome 等','拿取、攫住；分词形容失去感觉、活动能力'],['英语 numb','麻木、失去感觉；使感觉减弱']]
W('numb','/nʌm/','麻木的；失去知觉、情感反应的；使麻木',
 '手冷得像感觉暂时被拿走，突来的消息也可能让人心里一片空白。',
 '接古英语 niman“拿、取”经中古英语 nimen 的过去分词 nome 等，后指感觉迟钝、麻木；末尾 b 是后添拼写，现代不发音。数字 number 另经法语、拉丁语进入英语，不能按现代 numb + -er 解释。',NUMB,
 'numb fingers 是麻木的手指，feel numb 可说身体感觉或情绪反应减弱；numb the senses 是使感官迟钝。具体原因不能只从这个词判断。',
 'feel numb；go numb；numb with shock；numb fingers。',
 'numb 麻木，dumb 在部分用法说说不出话或愚蠢，不能因同样末尾 b 不发音就混用。数字 number 接法语、拉丁语词源，另行理解。',
 ('My fingers were numb after the cold walk.','冒冷走了一段路后，我手指都麻木了。'),('She felt numb when she heard the unexpected news.','听到意外消息时，她一时麻木，反应不过来。'),sources=['https://en.wiktionary.org/wiki/numb','https://www.etymonline.com/word/numb','https://www.ahdictionary.com/word/search.html?q=numb'])
W('numbness','/ˈnʌmnəs/','麻木；感觉减弱；情感迟钝',
 '把摸不太出来、心里没反应的这种状态，单独拿出来描述。',
 'numb + -ness，b 仍不发音；相接的 m、n 自然衔接，不插入一个 b 音。',NUMB+[['numb + -ness → numbness','麻木或反应减弱的状态']],
 'numbness in the fingers 是手指麻木，a sense of numbness 是一阵麻木感。身体与情感语境都可用，不能由词义代替判断原因。',
 'numbness in；a feeling of numbness；emotional numbness。',
 'numbness 偏感受迟钝，weakness 偏力量、能力不足；没有力气和感觉减弱可以并存，但不是一个词义。',
 ('He described numbness in his fingers.','他描述手指有麻木感。'),('The novel captures the numbness that followed the shock.','小说写出了打击之后那种麻木。'))
R('B3203','感觉像被拿走；麻木','NUMB：身体或情绪的感觉变弱，像暂时空了一块','手指冷得没感觉，心里受打击后也可能一时反应不过来。',
 'numb 的旧词形与 nim“拿取”的过去分词有关，感觉仿佛被夺去是理解联系；末尾 b 后添且不发音。数字 number 的常用词源另接法语、拉丁语，不按 numb + -er 解释。',
 '先 numb 看形容词、动词，再 numbness 看状态；原表 number 的普通数字义不并入此族，少见比较级同形用法不单列。',
 [['基本状态与名词','numb · numbness']],
 'numb /nʌm/，numbness /ˈnʌmnəs/，b 不发音。麻木不等于无力，身体描述也不直接说明原因。',
 'His fingers felt numb, but the numbness faded once he was indoors.\n\n他的手指感到麻木，进屋后这种感觉逐渐消退。','numb numbness')
ROOTS[-1]['exclude']['number']='普通数字 number 接法语 nombre、拉丁 numerus，不是 numb 的派生；少用比较级同形不另列。'
if __name__=='__main__':save('continuation_20261028_ag',ROOTS,WORDS)
