"""Pin, clock and killer: fixing points, support, time and familiar compounds."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
P=[['古英语 pinn 等 → pin','销、钉、别针等细小固定件'],['英语 pin','针状固定物 → 钉住、置顶、把希望寄托其上等']]
W('pinned','/pɪnd/','钉住、别住、固定了；已置顶的；有销、针的',
 '把便条别在板上，它就固定不乱跑；聊天里把重要消息固定在上面，也叫 pinned。',
 'pin 双写 n + -ed，过去式、过去分词及状态形容词。/n/ 后 -ed 读 /d/，不另加 /ɪd/ 音节；具备某种销针的形容词构造也存在。',P+[['pin + -ed → pinned','被固定、固定了；数字界面已置顶']],
 'pinned to the board 钉在板上，a pinned message 置顶消息，pinned her hopes on 把希望寄托在。固定动作借到位置、心理依靠。',
 'pinned to；a pinned message；pin your hopes on。',
 'pinned 已固定或置顶，不是所有 highlighted 高亮都等于置顶；数字界面颜色醒目与位置固定可以分开。',
 ('The note was pinned to the board.','便条被别在板上。'),('Check the pinned message for the meeting time.','查看置顶消息里的开会时间。'))
W('pinball','英 /ˈpɪnbɔːl/；美 /ˈpɪnbɔːl/','弹球游戏；快速乱弹、穿梭',
 '一颗球在斜台上撞障碍、打目标、弹回来，像在销钉和挡块间不停改道；人、物穿梭时也可借它说东撞西弹。',
 'pin 销、钉等障碍材料 + ball 球，名字保留早期弹球装置特征；后来有对应动词、比喻用法。',P+[['pin + ball → pinball','球在带钉、障碍的台面上弹动的游戏'],['动作比喻','快速来回弹跳、穿梭']],
 'a pinball machine 弹球机，play pinball 玩弹球，pinball around 到处快速弹动、穿梭。',
 'a pinball machine；play pinball；pinball around。',
 'pinball 通常指特定弹球游戏，bowling 保龄球是另一种球戏；不要看见 pin 和 ball 就把不同装置当一样。',
 ('They played pinball at the arcade.','他们在游乐厅玩弹球。'),('Ideas pinballed around the room during the meeting.','开会时，各种想法在屋里飞来飞去。'))
W('underpin','英 /ˌʌndəˈpɪn/；美 /ˌʌndərˈpɪn/','从下面支撑、加固；构成……的基础',
 '上面一座房，下面加支撑；理论、判断也需要下面有证据托住。证据 underpin a claim，就是给说法打基础。',
 'under- 在下面 + pin 固定、支撑的动词支。历史上字面、比喻用法都很早，不能武断地说一定先修地基才有所有抽象义。',P+[['under- + pin → underpin','从下方固定支撑；为观点、系统提供基础']],
 'underpin a theory 支撑理论，underpin an argument 构成论证依据，values that underpin a system 体系的基础价值观。过去 underpin → underpinned。',
 'underpin a theory；underpin an argument；values that underpin。',
 'underpin 不是只把针放在下面；abstract support 是基础作用，不保证单条证据就最终证明所有结论。',
 ('Several studies underpin the theory.','几项研究为理论提供了基础。'),('Trust underpins their working relationship.','信任是他们工作关系的基础。'),sources=['https://www.etymonline.com/word/underpin'])
W('pinstripe','/ˈpɪnstraɪp/','细条纹；细条纹布料',
 '像别针那么细的一道线，许多平行线排在西装布上；pin 在这儿用来把条纹说细。',
 'pin 细小、针样 + stripe 条纹，不是把实物别针钉成整排。布料名、服装定语再沿纹样发展。',P+[['pin + stripe → pinstripe','针样细线 → 细条纹、相应布料']],
 'a pinstripe suit 细条纹西装，white pinstripes 白色细条纹，pinstripe fabric 细条纹布。',
 'a pinstripe suit；white pinstripes；pinstripe fabric。',
 'pinstripe 细条纹，stripe 泛指条纹；条纹宽到一大块时，未必还自然叫 pinstripe。',
 ('He wore a dark pinstripe suit.','他穿着深色细条纹西装。'),('The fabric has narrow white pinstripes.','布料上有细细的白条纹。'))
W('pinhead','/ˈpɪnhed/','针头、别针顶端；笨蛋〔贬称〕',
 '别针顶端那颗小帽，常用来比非常小的面积；拿它叫人，则是在骂对方脑子小、愚蠢。',
 'pin + head，head 取器物顶部义；人物贬称借小头、少见识的夸张，并非任何实际头围判断。',P+[['pin + head → pinhead','针的顶端小头'],['人物侮辱','愚蠢者的贬称']],
 'the size of a pinhead 针头大小，on the head of a pin/on a pinhead 针尖小地方；call someone a pinhead 骂某人笨蛋。',
 'the size of a pinhead；on a pinhead；a pinhead〔贬称〕。',
 'pinhead 器物义中性，称人则冒犯；不是医学或智力测量术语。针尖尖端也不一定是 head 指的钝顶端，按实物分。',
 ('The spot was no bigger than a pinhead.','那个斑点还没有针头大。'),('He regretted calling his colleague a pinhead.','他后悔骂同事笨蛋。'))
W('pincushion','/ˈpɪnkʊʃən/','针插、插针垫；针垫状物',
 '一只填得鼓鼓的小垫子，把缝衣针、别针插在上面收好；密密插起的外观还能给植物、形状借名。',
 'pin + cushion 小垫，按储针用途命名。现代也有磁性等储针器具沿用名，不保证都得像沙发靠垫。',P+[['pin + cushion → pincushion','放针的小垫子'],['外形借名','像针垫的植物、形状或表面']],
 'a sewing pincushion 缝纫针插，a magnetic pincushion 磁性针座，pincushion distortion 枕形、针垫形畸变。',
 'a sewing pincushion；a magnetic pincushion；pincushion distortion。',
 'pincushion 存针的小器物，cushion 更宽指垫子；pincushion distortion 是外形比喻，不是针把镜头戳坏的字面故事。',
 ('She kept spare pins in a red pincushion.','她把备用别针插在红色针垫上。'),('The sewing kit includes a small pincushion.','针线包里有一个小针插。'))
R('B2804','针销的固定、细小形状，以及基础支撑','PIN：小针能固定东西，也能把位置和希望钉在一点上','pin → pinned；underpin 下方支撑；pinstripe 细线；pinhead 小头；pinball、pincushion 按用途组合。',
 '基本针销、数字置顶、理论基础放进不同分支。细小和固定是两种主要联想，球机、条纹、针头分别取不同特点。',
 'pinn → pin；pin + -ed 双写 n；under- + pin；pin + ball/stripe/head/cushion/point/hole；king/hair + pin。',
 [['固定动作与基础','pin · pinned · underpin'],['细小形态和位置','pinstripe · pinhead · pinpoint · pinhole'],['游戏、针具及其他组合','pinball · pincushion · hairpin · kingpin']],
 'pinned/highlighted 置顶与高亮；underpin 不必实物针；pinhead 人物义冒犯；pinball 不等于保龄球。',
 'The pinned note explains how to store pins in the pincushion.\n\n钉住的便条说明了怎样把别针收在针插上。','pin pinned underpin pinstripe pinhead pinpoint pinhole pinball pincushion hairpin kingpin')
C=[['中世纪拉丁 clocca 及法语、荷兰语相关钟铃词','铃、钟；更远常联系拟声和凯尔特词'],['中古英语 clokke → clock','报时钟 → 各种时钟、计时；动词记录时间、速度']]
W('clock','英 /klɒk/；美 /klɑːk/','钟、时钟；计时、测得速度；打卡等习语',
 '旧名称从报时的钟铃走来；今天屏幕上没铃、没指针，也能叫 clock。动词则用时间标准把表现记下来。',
 '经中古英语借荷兰语 clocke 等钟铃材料，往上接中世纪拉丁 clocca 一族。更早传播方向有讨论，常联系拟声；不是英语 click 轻轻改元音就确定造出 clock。',C,
 'a wall clock 挂钟，set the clock 调时，clock in/out 打上下班卡，clock a speed 测得速度，around the clock 全天候。',
 'a wall clock；set the clock；clock in/out；around the clock。',
 'clock 一般钟，watch 常是戴在身上的表；clock 电子义不必有机械轮、钟铃，电脑时钟也能作运行节拍。',
 ('The clock on the wall had stopped.','墙上的钟停了。'),('The runner was clocked at under eleven seconds.','跑步者被计时为不到十一秒。'),sources=['https://www.etymonline.com/word/clock'])
W('clockwise','英 /ˈklɒkwaɪz/；美 /ˈklɑːkwaɪz/','顺时针地、顺时针的',
 '面向普通钟面，指针从 12 走到 3、6、9 的方向；把这份转动方向借到旋钮、队伍、图形。',
 'clock + -wise，-wise 表按某种方式、方向，不是聪明的 wise。整体可作副词，也可作形容词。',C+[['clock + -wise → clockwise','按普通钟面指针方向转动']],
 'turn clockwise 顺时针转，a clockwise direction 顺时针方向，move clockwise around 绕着顺时针移动。',
 'turn clockwise；a clockwise direction；move clockwise。',
 'clockwise 顺时针，counterclockwise/anticlockwise 逆时针；观察哪一面会影响看见的转向，先确定视角。',
 ('Turn the dial clockwise.','顺时针转动刻度盘。'),('The dancers moved clockwise around the circle.','舞者沿圆圈顺时针移动。'))
W('counterclockwise','英 /ˌkaʊntəˈklɒkwaɪz/；美 /ˌkaʊntərˈklɑːkwaɪz/','逆时针地、逆时针的〔美式常见〕',
 '面向普通钟面，从 12 向 9、6、3 的方向转；和通常指针方向反过来。',
 'counter- 相反、逆向 + clockwise 顺时针，前缀作用于整个方向词。counter 在此不是柜台或计数器。',C+[['counter- + clockwise → counterclockwise','与顺时针相反的方向']],
 'turn counterclockwise 逆时针转，a counterclockwise rotation 逆时针旋转。美式常见，也通用于其他英语语境。',
 'turn counterclockwise；a counterclockwise rotation。',
 'counterclockwise 与 anticlockwise 意思相同、地区偏好不同；方向先确定面对哪一面，不凭词长短决定速度。',
 ('The arrow points counterclockwise around the circle.','箭头沿圆圈指向逆时针方向。'),('The wheel began to rotate counterclockwise.','轮子开始逆时针转动。'))
W('anticlockwise','英 /ˌæntiˈklɒkwaɪz/；美 /ˌæntiˈklɑːkwaɪz/','逆时针地、逆时针的〔英式常见〕',
 '把顺时针方向反过来，anti- 在这里就是方向相逆；不是讨厌时钟的人在表达态度。',
 'anti- 相反、反向 + clockwise。现代和 counterclockwise 是常用方向词对应，不必再造一种不同转法。',C+[['anti- + clockwise → anticlockwise','与钟面指针通常转向相反']],
 'move anticlockwise 逆时针移动，an anticlockwise direction 逆时针方向；英式英语里很常见。',
 'move anticlockwise；an anticlockwise direction。',
 'anticlockwise/counterclockwise 同义，前者英式常见、后者美式常见；不是两个国家的钟本来转向不同。',
 ('The players moved anticlockwise around the table.','玩家沿桌子逆时针移动。'),('Follow the marked path in an anticlockwise direction.','沿标出的路径逆时针走。'))
W('clockwork','英 /ˈklɒkwɜːk/；美 /ˈklɑːkwɜːrk/','钟表式机械机构、发条装置；精确有序的运行',
 '发条储力、齿轮咬着转，动作一环带一环；事情 run like clockwork 就是该谁做、何时做都顺顺当当。',
 'clock + work，work 在器械名里说运作机构。先指机械钟、玩具等内部机构，再借作精密有序的比喻。',C+[['clock + work → clockwork','钟表机械、发条运作机构'],['英语比喻','像精密机械般准时、有序']],
 'a clockwork toy 发条玩具，run like clockwork 运转井然有序，with clockwork regularity 极有规律地。',
 'a clockwork toy；run like clockwork；with clockwork regularity。',
 'clockwork 机械机构或相应比喻，所有 digital clocks 数字时钟不必都内有发条；clockwise 是方向，完全不同词尾。',
 ('The little clockwork bird moved across the table.','小发条鸟在桌上移动。'),('The whole event ran like clockwork.','整个活动进行得井井有条。'))
W('overclock','英 /ˌəʊvəˈklɒk/；美 /ˌoʊvərˈklɑːk/','使超频、超频运行',
 '电脑部件按时钟节拍工作，overclock 把节拍频率调到高于标定值；不是把墙上时钟拨快来骗电脑。',
 'over- 超出 + clock 电子时钟、时钟频率，合成计算机动词，也有名词用法。时钟在这里是运行节拍来源，不只是显示几点。',C+[['电子 clock 时钟频率 + over- → overclock','高于标定时钟频率运行']],
 'overclock a processor 让处理器超频，an overclocked chip 超频芯片，a factory overclock 出厂超频设置。',
 'overclock a processor；an overclocked chip；a factory overclock。',
 'overclock 改时钟频率，change the system time 改系统显示时间；两者不能按都有 clock 就当同件事。',
 ('The review compares the chip at its normal speed and when overclocked.','评测比较了芯片正常频率和超频时的表现。'),('The article explains what it means to overclock a processor.','文章解释了处理器超频是什么意思。'))
R('B2464','钟铃、时钟和运行节拍；方向和机械机构','CLOCK：从报时钟到计时，再到电子运行节拍','clock → clockwise 方向、clockwork 机构；overclock 在电子节拍上超出标定频率。',
 '钟面、钟内部机构、电子时钟是不同层面。顺时针不等于发条机构，超频也不等于改显示时间。',
 'clocca/clocke → clock；clock + -wise/work；counter-/anti- + clockwise；over- + clock。',
 [['计时及转动方向','clock · clockwise · counterclockwise · anticlockwise'],['机械机构和电子频率','clockwork · overclock']],
 'clock/watch 钟与随身表；clockwise/clockwork 方向与机构；overclock 不改变同一意义的系统日期时间。',
 'The clockwork toy turned clockwise while the wall clock ticked.\n\n墙上时钟滴答响时，发条玩具顺时针转动。','clock clockwise counterclockwise anticlockwise clockwork overclock')
R('B3455','杀死者、致命物，以及很强烈、很出色的比喻','KILLER：造成死亡，也能夸张说强烈、厉害','killer 杀手、致命物；killer performance 出色表演；painkiller 是镇痛药的组合名。',
 '同词可是真实伤害，也可是强调强度的夸张。painkiller 按减轻疼痛的药物理解，不把杀这个字当永久根治所有病因。',
 'kill + -er → killer；pain + killer → painkiller。',
 [['施事、致命性和强度比喻','killer'],['镇痛药物组合','painkiller']],
 'killer 的出色、强烈义看搭配；painkiller 名称不说明适合谁、剂量多少或是否根治病因。',
 'The review called her final song a killer performance.\n\n评论称她最后那首歌的表演十分出色。','killer painkiller')
if __name__=='__main__':save('continuation_20261030_hg',ROOTS,WORDS)
