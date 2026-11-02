"""Bar: physical rods, counters and screen strips, with distinct pressure-unit origin."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
BA=[['古法语 barre → 中古英语 barre → bar','杆、横木、阻隔物；更远来源不确定'],['现代 bar','条杆、障碍；柜台和酒吧；屏幕条状区域等支线']]
def B(f,m):return BA+[[f,m]]
W('bar','英 /bɑː/；美 /bɑːr/','条、杆；酒吧、吧台；阻止、禁止；律师界〔the bar〕',
 '先看一根横着的杆：能拦住路，也能隔出柜台；巧克力和屏幕上的长条，也可叫 bar。',
 '条杆义经古法语 barre，远源不明。酒吧义联系售酒柜台、隔栏；法律 the bar 联系法庭隔栏。压力单位 bar 则来自希腊 báros 重量，是另一来源，不能全串成木棍。',BA+[['另源希腊 báros → 压力单位 bar','重量相关命名；与条杆、吧台分源']],
 'a chocolate bar 巧克力棒，at the bar 在吧台，bar someone from entering 禁止进入；raise the bar 比喻提高标准。',
 'a chocolate bar；at the bar；bar someone from；raise the bar。',
 'bar 动词阻止，ban 禁止，许多语境接近；a bar of soap 一块肥皂不一定细长。压力单位 bar 需单独记来源。',
 ('They met at a small bar near the station.','他们在车站附近一家小酒吧见面。'),('The rules bar visitors from entering this room.','规定禁止访客进入这个房间。'),sources=['https://www.etymonline.com/word/bar','https://en.wiktionary.org/wiki/bar#English'])
W('bartender','英 /ˈbɑːˌtendə/；美 /ˈbɑːrˌtendər/','酒吧服务员；调酒师',
 '站在吧台后照看客人、递酒调饮的人，重点是负责吧台服务。',
 'bar 酒吧、吧台 + tender 照料者，接 tend 照看。这里 tender 不是柔嫩，也不是投标文件。',B('bar + tender〔照料者〕→ bartender','负责酒吧柜台服务的人'),
 'work as a bartender 当酒吧服务员，ask the bartender 问吧台服务员。既可递啤酒，也可调鸡尾酒，不只指比赛级调酒师。',
 'work as a bartender；ask the bartender；an experienced bartender。',
 'bartender 是较通用的人物词；barman、barmaid 传统上带性别信息。bartender 可适用于任何性别。',
 ('The bartender recommended a drink without alcohol.','吧台服务员推荐了一款不含酒精的饮品。'),('She worked as a bartender while studying.','她上学时做过酒吧服务员。'))
W('bartending','英 /ˈbɑːˌtendɪŋ/；美 /ˈbɑːrˌtendɪŋ/','吧台服务；调酒工作',
 '从负责吧台的那个人，转到这份工作：接单、做饮品、服务客人。',
 'bar + tending，也与 bartend + -ing 对应。-ing 这里可把工作活动整体说成名词。',B('bar + tending／bartend + -ing → bartending','照管吧台、制作供应饮品的工作'),
 'a bartending course 吧台服务、调酒课程，bartending experience 吧台工作经验。',
 'a bartending course；bartending experience；learn bartending。',
 'bartender 是人，bartending 是工作活动；a bartending course 课程不只教顾客怎么喝酒。',
 ('He took a bartending course before starting the job.','他上岗前参加了吧台服务课程。'),('Her bartending experience helped her manage the busy café.','吧台工作经验帮助她管理忙碌的咖啡馆。'))
W('barman','英 /ˈbɑːmən/；美 /ˈbɑːrmən/','男酒吧服务员',
 '传统称呼里，把在吧台服务的男性叫 barman；角色和 bartender 大体相同。',
 'bar + man，后部说明男性工作人员，复数 barmen。连读时 man 常弱读，不必照独立 man 重读。',B('bar + man → barman','男性吧台服务人员'),
 'ask the barman 问男吧台服务员，the local barman 当地酒吧服务员。英式语境较常见。',
 'ask the barman；a friendly barman；the barman’s recommendation。',
 'barman 特别指男性；bartender 更通用。不要把 barman 理解为必然拥有整家酒吧的老板。',
 ('The barman brought us two glasses of water.','男吧台服务员给我们端来两杯水。'),('We asked the barman where to find a taxi.','我们问男吧台服务员哪里能打车。'))
W('barmaid','英 /ˈbɑːmeɪd/；美 /ˈbɑːrmeɪd/','女酒吧服务员〔传统称呼〕',
 '传统上按性别给吧台服务人员命名；今天很多场合直接用 bartender。',
 'bar + maid，maid 在旧职业词中可指女性服务人员；整个词已固定，不需要每次额外推断婚姻状态。',B('bar + maid → barmaid','女性吧台服务人员'),
 'work as a barmaid 做女酒吧服务员，the pub’s barmaid 酒馆女服务员。使用时留意说话人、年代和地区的习惯。',
 'work as a barmaid；the pub’s barmaid；a former barmaid。',
 'barmaid 是传统女性称呼，bartender 是通用称呼；maid 在此不等于顾客家的女佣。',
 ('The novel follows a barmaid working in a village pub.','小说讲述一位在乡村酒馆工作的女服务员。'),('The barmaid collected the empty glasses.','女酒吧服务员收走了空杯子。'))
W('minibar','英 /ˈmɪnibɑː/；美 /ˈmɪnibɑːr/','迷你酒吧；酒店房内饮料小冰箱、储柜',
 '把供应饮料的小区域缩到客房里，常见就是装饮料和零食的小冰箱。',
 'mini- 小型 + bar 酒吧。名称借供应饮品的功能，不要求里面有真人吧台服务员。',B('mini- + bar → minibar','小型饮料供应区；酒店客房饮料柜'),
 'the hotel minibar 酒店迷你吧，drinks from the minibar 迷你吧饮品。是否收费看酒店说明，不由词本身决定。',
 'the hotel minibar；a minibar in the room；minibar drinks。',
 'minibar 强调客房饮品供应功能；mini fridge 只说小冰箱，里面未必摆好饮品出售。',
 ('There is a minibar beneath the desk.','书桌下面有一个迷你吧。'),('She checked the minibar menu before opening a drink.','她开饮料前看了迷你吧价目单。'))
W('toolbar','英 /ˈtuːlbɑː/；美 /ˈtuːlbɑːr/','工具栏',
 '把常用工具按钮排成一条，方便随手点，就是界面上的工具栏。',
 'tool 工具 + bar 条状区域，软件界面借长条形状命名，不是真有一根金属杆放在屏幕里。',B('tool + bar → toolbar','排列工具按钮的界面区域'),
 'the editing toolbar 编辑工具栏，a toolbar button 工具栏按钮，hide the toolbar 隐藏工具栏。',
 'the editing toolbar；a toolbar button；hide the toolbar。',
 'toolbar 提供工具，taskbar 通常列出应用、任务等；不同软件具体排布可变化，不只由上下位置辨认。',
 ('Click the save button on the toolbar.','点击工具栏上的保存按钮。'),('You can hide the toolbar to gain more space.','你可以隐藏工具栏，腾出更多空间。'))
W('taskbar','英 /ˈtɑːskbɑː/；美 /ˈtæskbɑːr/','任务栏',
 '把应用和正在做的任务放成一条，便于切换、打开；常见于电脑桌面界面。',
 'task 任务 + bar 条状区域，按显示任务、应用的功能命名。具体系统功能和位置可不同。',B('task + bar → taskbar','显示任务、应用等的界面区域'),
 'pin an app to the taskbar 把应用固定到任务栏，a taskbar icon 任务栏图标。',
 'a taskbar icon；pin to the taskbar；hide the taskbar。',
 'taskbar 便于管理应用、任务；toolbar 多是当前程序的工具按钮。不要把所有带图标的横条都叫同一个名字。',
 ('The app’s icon appeared on the taskbar.','应用图标出现在任务栏上。'),('He pinned the browser to the taskbar.','他把浏览器固定到了任务栏。'))
W('soundbar','英 /ˈsaʊndbɑː/；美 /ˈsaʊndbɑːr/','条形音箱；回音壁音箱',
 '扬声器做成长条，常摆在电视下方；名字按声音功能和外形直接拼起来。',
 'sound 声音 + bar 条、杆状物。是音箱产品类别词，不是界面上的音量条。',B('sound + bar → soundbar','条形扬声器、音箱'),
 'a TV soundbar 电视条形音箱，connect a soundbar 连接条形音箱。',
 'a TV soundbar；connect a soundbar；a wireless soundbar。',
 'soundbar 是发声设备；volume bar 常是屏幕音量刻度。一个在发声，一个在显示设置。',
 ('The soundbar sits just below the television.','条形音箱就放在电视下方。'),('They connected the soundbar to improve the dialogue clarity.','他们接上条形音箱，让对白更清楚。'))
W('handlebar','英 /ˈhændəlbɑː/；美 /ˈhændəlbɑːr/','车把〔通常用复数 handlebars〕',
 '双手握住，靠它控制自行车等车辆方向的横杆。',
 'handle 手柄、把手 + bar 杆。日常说整副车把通常用 handlebars，词尾复数属于常见用法。',B('handle + bar → handlebar','用作操纵把手的杆 → 车把'),
 'hold the handlebars 握住车把，adjust the handlebars 调整车把，a handlebar moustache 形状像车把的翘胡须。',
 'hold the handlebars；adjust the handlebars；a handlebar moustache。',
 'handlebars 车把，steering wheel 方向盘；名称按结构不同，不是所有车的控制件都叫 handlebar。',
 ('Keep both hands on the handlebars.','双手都握住车把。'),('She adjusted the handlebars before the ride.','骑车前，她调整了车把。'))
W('crowbar','英 /ˈkrəʊbɑː/；美 /ˈkroʊbɑːr/','撬棍',
 '一根硬金属杆，端部常扁平或分叉，用来插进去撬开、撬起东西。',
 'crow 乌鸦，也有撬具旧义 + bar 杆；通常认为命名联系分叉端像鸟爪的形状。这个形象是来源解释的可能动机，不是拿乌鸦做工具。',B('crow〔鸟、旧撬具名〕+ bar → crowbar','常联系鸟爪形端部的金属撬杆'),
 'use a crowbar 用撬棍，pry open with a crowbar 用撬棍撬开。',
 'use a crowbar；a metal crowbar；pry open with a crowbar。',
 'crowbar 靠杠杆作用撬起，hammer 锤子靠敲击；同一维修场景可能用两种工具。',
 ('They used a crowbar to lift the heavy lid.','他们用撬棍抬起沉重的盖子。'),('The carpenter kept a crowbar in the toolbox.','木匠在工具箱里放了一根撬棍。'))
W('rebar','英 /ˈriːbɑː/；美 /ˈriːbɑːr/','钢筋；混凝土中的加强钢条',
 '混凝土里嵌入的钢条，形成骨架、帮助承受拉力；名字就是加强用的杆。',
 'reinforcing bar 缩合为 rebar。这个名词的 re- 取自 reinforcing，不是简单再次 + bar。另有再次加栏杆的动词 re-bar 分析，此处先学建筑名词。',B('reinforcing bar → rebar','加强杆的缩合 → 钢筋'),
 'steel rebar 钢筋，reinforced with rebar 用钢筋加强，a rebar cage 钢筋笼。',
 'steel rebar；a rebar cage；reinforced with rebar。',
 'rebar 常是混凝土中的钢筋，steel beam 是钢梁；二者都可属建筑钢材，形态、用途不相同。',
 ('Workers placed the rebar before pouring the concrete.','工人在浇混凝土前放好了钢筋。'),('Steel rebar was visible inside the damaged wall.','受损墙体里露出了钢筋。'))
W('sandbar','英 /ˈsændbɑː/；美 /ˈsændbɑːr/','沙洲；水中的沙坝',
 '水把沙堆成一道隆起，像横在水里的长条；可能露出水面，也可能藏在浅水下。',
 'sand 沙 + bar 条状隆起、障碍，按沉积形状命名。不是海边卖饮料的酒吧。',B('sand + bar → sandbar','沙形成的条状浅滩、沙洲'),
 'a sandbar near the shore 近岸沙洲，run aground on a sandbar 在沙洲搁浅。',
 'a sandbar near the shore；a submerged sandbar；run aground on a sandbar。',
 'sandbar 沙洲、浅滩，beach 海滩；沙洲不一定紧贴岸边，也不一定一直露在水上。',
 ('At low tide, a sandbar linked the island to the shore.','退潮时，一道沙洲把小岛与岸边连起来。'),('The boat became stuck on a sandbar.','船在沙洲上搁浅了。'))
R('B3335','杆、阻隔、柜台与长条形；压力单位分源','BAR：一根横杆能隔开空间，也能借指条状物','先条杆与阻止，再讲酒吧人员、客房迷你吧，接屏幕长条与实体工具；已有 sidebar、crossbar、barkeep 共享。',
 '常见多个意思通过横杆、隔栏、柜台联系，压力单位却来自希腊重量词，必须单独注明。',
 'bar + tender/man/maid；mini- + bar；tool/task/sound/handle/crow/sand + bar；rebar 缩自 reinforcing bar。',
 [['基本物与阻隔','bar · crossbar'],['酒吧与人员','bartender · bartending · barman · barmaid · barkeep · minibar'],['界面条与声音设备','toolbar · taskbar · sidebar · soundbar'],['杆具和自然条状物','handlebar · crowbar · rebar · sandbar']],
 'bar 条杆与压力单位分源；bartender 照料者不是柔嫩；rebar 是缩合；soundbar 音箱、toolbar 工具栏。',
 'The bartender used the toolbar to check the minibar order.\n\n吧台服务员用工具栏查看迷你吧订单。',
 'bar crossbar bartender bartending barman barmaid barkeep minibar toolbar taskbar sidebar soundbar handlebar crowbar rebar sandbar')
if __name__=='__main__':save('continuation_20261030_ao',ROOTS,WORDS)
