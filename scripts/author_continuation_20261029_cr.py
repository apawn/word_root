"""Road: roads, obstacles, vehicles and travelling workers."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
def C(a,b,w,m):return [[a+'；'+b,'并列构词部分'],[w,m]]
RO=[['古英语 rād → 中古英语 rode','骑行、行程、出行等'],['英语 road','由出行转到通行的路；现代还有旅途、途径比喻']]
W('road','英 /rəʊd/；美 /roʊd/','道路；旅途；达到目标的途径',
 '既是车、人实际走的路，也能把完成一件事想成一段要走过去的路程。',
 '由古英语 rād 骑行、行程等延续，与 ride 历史同族；现代道路义后来突出。不是现代 ride 换元音就能随意造所有道路名词。',RO,
 'cross the road 过马路，on the road 在旅途中或巡演中；the road to recovery 恢复之路，a long road ahead 前路漫长。',
 'cross the road；on the road；the road ahead；the road to success。',
 'road 泛指通行道路，street 常强调城镇里沿线有建筑的街道；实际名称有交叠，不能只由宽窄判断。',
 ('The road leads to a small village.','这条路通向一个小村庄。'),('There is still a long road ahead before the project is finished.','离项目完成还有很长一段路要走。'),sources=['https://en.wiktionary.org/wiki/road#English','https://www.etymonline.com/word/road'])
W('railroad','英 /ˈreɪlrəʊd/；美 /ˈreɪlroʊd/','铁路；铁路公司〔美〕；强迫仓促通过',
 '两条铁轨铺出固定线路，把车送往指定方向；动词引申时像不让人偏离或细想，就强推过去。',
 'rail 轨道 + road 路，形成铁路名称；动词由铁路式强力推进的比喻发展为迫使快速通过、接受等用法，不是对方真的被运到铁路上。',C('rail 轨道','road 路','railroad','铁路 → 比喻强推决定、程序'),
 'a railroad company 铁路公司，railroad tracks 铁轨；railroad someone into a decision 强迫某人仓促决定，语气批评。',
 'a railroad company；railroad tracks；railroad into；railroad through。',
 'railroad 在美式普遍，railway 英式常用；动词 railroad through 强调仓促强推，不是普通认真讨论后批准。',
 ('The town grew around the railroad station.','小镇围绕火车站发展起来。'),('They felt railroaded into accepting the plan.','他们觉得自己被强迫仓促接受了方案。'))
W('roadside','英 /ˈrəʊdsaɪd/；美 /ˈroʊdsaɪd/','路边；路旁的',
 '不在道路正中，而在道路边缘一带：停车处、花草或小摊都能在那里。',
 'road 道路 + side 侧边，复合为路旁地带，也能修饰名词。',C('road 道路','side 侧边','roadside','路边地带、路旁的'),
 'at the roadside 在路边，a roadside café 路边咖啡馆，roadside assistance 道路救援。',
 'at the roadside；a roadside stall；roadside assistance。',
 'roadside 位置在路边，roadway 车行道或路面范围；roadside café 不代表咖啡馆建在车道正中。',
 ('We stopped at a roadside café.','我们在一家路边咖啡馆停了下来。'),('Wildflowers grew along the roadside.','路边长着野花。'))
W('roadblock','英 /ˈrəʊdblɒk/；美 /ˈroʊdblɑːk/','路障；推进过程中的障碍',
 '车原来能继续向前，现在被拦住；计划碰到让进度停下来的问题，也借这个词。',
 'road 路 + block 阻挡物，先指交通障碍、检查封锁点等，再比喻阻碍进展的困难。',C('road 路','block 阻挡','roadblock','路上的阻拦 → 推进事项的障碍'),
 'a police roadblock 警方设置的路障、检查点；a roadblock to progress 进展障碍。不是所有小不便都严重到必须停下来。',
 'set up a roadblock；hit a roadblock；a roadblock to progress。',
 'roadblock 让行进受阻，roadmap 指示往哪里、怎样推进；项目有 roadmap 仍可能遇到 roadblocks。',
 ('A fallen tree created a roadblock.','一棵倒树挡住了道路。'),('The project hit a roadblock when the funding was delayed.','资金延迟到位，让项目推进遇到了障碍。'))
W('roadbed','英 /ˈrəʊdbed/；美 /ˈroʊdbed/','路基；铁路轨道下面的基础结构',
 '车跑在上面，但下面还得有一层稳定支撑，让路面或轨道不乱沉。',
 'road 路 + bed 基底、承托层。bed 使用床、底层的扩展义，不是司机睡觉的床。',C('road 路','bed 基底、承托层','roadbed','承托道路或轨道的基础结构'),
 'repair the roadbed 修路基，a railway roadbed 铁路路基；不同工程分类对具体包含层次有更细区分。',
 'a railway roadbed；repair the roadbed；damage to the roadbed。',
 'roadbed 在基础、承托结构，road surface 路表面；不能只把可见沥青表层都叫 roadbed。',
 ('Heavy rain damaged the railway roadbed.','大雨损坏了铁路路基。'),('Workers repaired the roadbed before laying new tracks.','工人铺设新轨道前先修复了路基。'))
W('roadster','英 /ˈrəʊdstə/；美 /ˈroʊdstər/','敞篷跑车；其他按用途命名的车辆旧称',
 '现代汽车语境里，常是一辆开放式车身、强调驾驶体验的跑车。',
 'road + -ster；-ster 形成有关人物、事物名称，这里已固定为车辆名称。历史还用于马、自行车等，不是见到 -ster 就必须译人。',RO+[['road + -ster → roadster','道路相关用途 → 固定车辆、敞篷跑车名称']],
 'a two-seater roadster 双座敞篷跑车，a classic roadster 经典敞篷跑车；不同年代、厂商名称用法有差异。',
 'a classic roadster；a two-seater roadster；an open-top roadster。',
 'roadster 是车型固定名，不是所有能上路的车；roadie 则通常是巡演工作人员。',
 ('The museum displayed a red roadster from the 1950s.','博物馆展出了一辆二十世纪五十年代的红色敞篷跑车。'),('They drove along the coast in a small roadster.','他们开着一辆小敞篷跑车沿海岸行驶。'))
W('roadie','英 /ˈrəʊdi/；美 /ˈroʊdi/','乐队巡演的器材、舞台等工作人员〔口语〕',
 '歌手在台上演，背后有人跟着巡演，搬运、安装和维护器材；这类工作人员常叫 roadie。',
 'road 巡演、在路上这一用法 + -ie，形成较随意的人物称呼。不是游客、卡车司机的通用名称。',RO+[['road + -ie → roadie','跟巡演在路上 → 巡演工作人员']],
 'a band’s roadie 乐队巡演工作人员，work as a roadie 做巡演器材、舞台等工作；不同职位可能专管音响、灯光、搬运等。',
 'work as a roadie；a band’s roadies；touring roadies。',
 'roadie 支持巡演的工作人员，performer 表演者；一个人也可兼任两种角色，但名称强调的工作不同。',
 ('He worked as a roadie before joining the band.','加入乐队前，他做过巡演工作人员。'),('The roadies packed the equipment after the show.','演出后，巡演工作人员收好了器材。'))
W('roadrunner','英 /ˈrəʊdrʌnə/；美 /ˈroʊdrʌnər/','走鹃；一种善于在地面奔跑的鸟',
 '看着像把公路当跑道的鸟，名字抓住它在地面奔跑的明显特点。',
 'road 路 + runner 跑者，可能对应西班牙语 correcaminos 的仿译。它是已经固定的鸟名，不是所有在路上跑的人。',C('road 路','runner 跑者','roadrunner','按地面奔跑特点命名的走鹃'),
 'a roadrunner in the desert 沙漠地区的走鹃；卡通形象使用这一鸟名，但不能从动画推断真实动物的速度、声音等特点。',
 'a roadrunner；a desert roadrunner；spot a roadrunner。',
 'roadrunner 是鸟名，runner 可泛指跑者；名字强调跑，不等于这种鸟完全不能飞。',
 ('We spotted a roadrunner near the desert trail.','我们在沙漠小径附近看见了一只走鹃。'),('The roadrunner disappeared into the scrub.','走鹃跑进灌木丛，不见了。'))
R('B2780','道路、旅途；路边、路障与巡演词','ROAD：实际走的路，也能是事情推进的路','先读道路结构，再看被挡住的 roadblock 与目标方向的 roadmap；roadie、roadster、roadrunner 是不同固定名称。',
 'road 来自古英语的骑行、出行词族，后来突出通行道路义。现代复合词通常透明，但 -ster、-ie 形成的名称要按固定使用对象认。',
 'road → railroad、roadway；roadside 路旁、roadbed 路基；roadblock 障碍、roadmap 路线图；roadster 车、roadie 巡演工作者、roadrunner 鸟。',
 [['道路及结构','road · railroad · roadway · roadside · roadbed · crossroad · roadwork'],['阻碍与计划','roadblock · roadmap'],['出行、巡演及固定名称','roadshow · roadhouse · roadster · roadie · roadrunner'],['动物道路伤亡','roadkill']],
 'roadside 路边，roadbed 路基；roadster 车，roadie 人，roadrunner 鸟；railroad 动词还能说强推。',
 'The roadies stopped at a roadside café after a roadblock delayed the journey.\n\n路障耽误行程后，巡演工作人员在路边咖啡馆停了下来。',
 'road railroad roadway roadside roadbed crossroad roadwork roadblock roadmap roadshow roadhouse roadster roadie roadrunner roadkill')
if __name__=='__main__':save('continuation_20261029_cr',ROOTS,WORDS)
