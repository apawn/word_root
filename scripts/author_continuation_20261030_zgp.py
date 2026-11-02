"""Bustling places, hustle and the hurry family."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
def S(word,base):
 return ['https://en.wiktionary.org/wiki/'+word+'#English','https://www.etymonline.com/word/'+base]
EXISTING_ROOT_ADDITIONS={
 'A2238':dict(words='bustle bustles bustled bustling hustle hustles hustled hustling hustler hustlers'.split(),label='bustle 与 hustle：相近忙碌画面，不硬合词源',note='bustle 远源有 rush、prepare 等不同材料分析，仍未定；hustle 则接荷兰语摇动词的音位换位。两词现代可在 hustle and bustle 搭配中并列，不因此变成同一词根。'),
 'A1740':dict(words='hurry hurries hurried hurrying hurriedly unhurried unhurriedly'.split(),label='hurry → hurriedly：赶时间；unhurriedly：从容地',note='hurry 远源未定，有快速运动、嗡鸣材料或 harry 变体等分析；现代规则词尾和否定 un- 可以清楚拆解，不能因读音近就把全部假说定为事实。'),
}
BUSTLE=[['早期 bustlen、bustling 等忙乱材料 → bustle','远源未定，有 bresten、busk 等不同分析；不能只按现代短词顺序倒排年代'],['bustle 忙碌奔走 → 名词喧闹活动','另有服饰裙撑名词，其来路未定，不把它必然接成忙碌动词的产物']]
HUSTLE=[['荷兰语 hutselen、husseln 等摇动词 → hustle','经音位换位进入英语，不是英语直接加一个反复后缀就说完历史'],['摇动 → 推挤、催送；后有忙碌、拼力争取等用法','另有快速牟利、欺骗等分支；不把现代努力工作与骗钱画等号']]
HURRY=[['早期英语 hurry：赶快、催赶','远源未定，有快速运动、嗡鸣材料或 harry 变体等不同分析'],['hurry 动词 → 名词匆忙；英语规则变化','hurried 写匆忙，unhurried 否定匆忙，副词分别接 -ly']]
W('bustles','/ˈbʌsəlz/','忙碌奔走、热闹活动〔第三人称单数〕；裙撑〔复数，旧服饰〕',
 '店主在柜台、厨房之间忙前忙后，是 bustles about；城市满是行人、商贩，也可以 bustles with activity。服饰里的 bustles 则是历史裙撑复数。',
 'bustle + -s，读 /z/；忙碌动词远源未定，服饰名词也有独立的不确定来源，不能全归成一种忙碌。',BUSTLE+[['bustle + -s → bustles','他忙前忙后；另有服饰名词复数']],
 'bustles about 忙前忙后；bustles with shoppers 满是来往购物者、热闹非凡。',
 'bustles around the kitchen；a market that bustles。',
 'bustles 描写场所时常是有活力、热闹，is crowded 只说拥挤；未必都带烦躁的评价。',
 ('She bustles about the kitchen preparing lunch.','她在厨房里忙前忙后地准备午饭。'),('The market bustles with shoppers on Saturdays.','每到周六，市场里就挤满来往购物的人，热闹非凡。'),sources=S('bustles','bustle'))
W('bustled','/ˈbʌsəld/','忙碌奔走了；急忙张罗、引领了',
 '有人进来，主人赶忙把人领到桌旁，一面拿杯子一面招呼，是 bustled。这个词常让你看到忙前忙后的动作。',
 'bustle 去 e 加完整 -ed，读 /d/；远源未定的忙碌动词整体接过去词尾。',BUSTLE+[['bustle → bustled','过去忙前忙后，或急忙领人做某事']],
 'bustled around 忙来忙去；bustled someone into a room 忙着把人领进房间。',
 'bustled past；bustled about with trays。',
 'bustled 是活动繁忙、张罗的画面，ran 只说跑；用前者不一定说明人真的跑起来了。',
 ('The staff bustled around setting the tables.','员工们忙来忙去地摆桌子。'),('She bustled us into the dining room.','她忙着把我们领进餐厅。'),sources=S('bustled','bustle'))
W('bustling','/ˈbʌslɪŋ/','熙熙攘攘、热闹繁忙的；正在忙碌奔走',
 '小店开着，人来人往，叫卖、脚步、交谈都在动，叫 a bustling market。它常把地方写得有生气。',
 'bustle 去 e 加 -ing；早期英语已经很早见相关 bustling 形式，不用现代教学顺序断定必然所有短动词先出现。',BUSTLE+[['bustle → bustling〔现代构词对照〕','形容持续忙碌、热闹；不以这一箭头代替历史年代']],
 'a bustling city 繁忙城市；a bustling market 熙熙攘攘的市场。',
 'bustling with activity 热闹繁忙；bustling about the house。',
 'bustling 常偏活跃、热闹，chaotic 更突出无序；热闹繁忙不等于混乱失控。',
 ('We stopped at a bustling street market.','我们在一个热闹的街市停了下来。'),('The station was bustling with commuters.','车站里通勤者来来往往，一片繁忙。'),sources=S('bustling','bustle'))
W('hustle','/ˈhʌsəl/','催赶、推送；忙着争取、拼力做事；设局骗取；忙乱、骗局',
 '催着人快走，或自己积极跑动、抓机会，都可以 hustle；有时也指靠话术、设局弄到钱。共同画面是主动推动、快速争取，褒贬要看方法。',
 '接荷兰语 hutselen、husseln 摇动，经音位换位形成英语词。早期摇动，后有推挤、忙碌行动、快速牟利等多条意义支线。',HUSTLE,
 'hustle someone out 催着、推着某人出去；hustle for work 奔走找活；a hustle 一种骗局或积极奔忙。',
 'hustle and bustle 熙攘忙碌；side hustle 兼职副业。',
 'side hustle 在现代常中性说副业，a pool hustle 却可能是台球设局骗钱；不能看到 hustle 就一律赞成奋斗或一律译成骗局。',
 ('We had to hustle to catch the last train.','我们得赶紧行动，才能赶上末班车。'),('The guard tried to hustle us out of the building.','保安试图催着、推着我们离开大楼。'),sources=S('hustle','hustle'))
W('hustles','/ˈhʌsəlz/','催赶、拼力争取、设局骗取〔第三人称单数〕；副业、骗局等〔复数〕',
 '他每天四处找客户，是 hustles for work；几份副业可叫 side hustles；几个设局骗钱的套路也可能是 hustles。句中对象决定褒贬。',
 'hustle + -s，读 /z/；动词三单与名词复数同形，都是同一词族不同意义支线。',HUSTLE+[['hustle + -s → hustles','他催赶、争取或设局；多个副业、骗局等']],
 'hustles for clients 奔走找客户；side hustles 副业；street hustles 街头骗局。',
 'hustles everyone out；runs several side hustles。',
 'hustles for clients 不自动表示骗人；hustles people out of money 才明确朝骗取钱财走。看介词与宾语，不给整族贴单一褒贬。',
 ('She hustles for new clients between regular shifts.','她在正常轮班的空当四处争取新客户。'),('He runs two small side hustles from home.','他在家做两份小副业。'),sources=S('hustles','hustle'))
W('hustled','/ˈhʌsəld/','催赶、推送了；拼力争取了；设局骗了',
 '工作员一边催一边把大家领上车，是 hustled us onto the bus；自己赶着去找机会，也能用它的忙碌争取义。',
 'hustle 去 e 加完整 -ed，读 /d/；各种现代支线共用过去形式，不能只据词尾判断是努力还是欺骗。',HUSTLE+[['hustle → hustled','过去推送、催赶、积极奔忙或骗取']],
 'hustled into a taxi 被催着塞进出租车；hustled for work 奔走找工作。',
 'hustled past the crowd；hustled someone out of money。',
 'was hustled out 常说明被催赶、匆匆送出，left quietly 只说明自己安静离开；人的主动、被动方向不同。',
 ('The staff hustled us onto the waiting bus.','工作人员催着我们登上等候的巴士。'),('She hustled for freelance work during the summer.','她整个夏天都在奔走争取自由职业的工作。'),sources=S('hustled','hustle'))
W('hustling','/ˈhʌslɪŋ/','积极奔忙、争取机会；催赶；设局牟利等',
 '每天跑客户、找活、抓机会，可能是 hustling；街头缠着人要钱、设套赚钱，也会用同一个词。它写出强烈主动性，是否值得赞许看做法。',
 'hustle 去 e 加 -ing；动作形式与行为名词，常见读音中间收成 /sl/。',HUSTLE+[['hustle → hustling','持续奔忙、催赶或牟利的过程']],
 'hustling for work 四处找活；hustling people out 催人出去；street hustling 街头拉客或设局牟利。',
 'always hustling；hustling between meetings。',
 'hustling 和 bustling 都可写忙碌，但前者常更突出主动争取、快节奏推动，后者常描写热闹场面；来源也不必硬合。',
 ('He spent the summer hustling for small design jobs.','他整个夏天都在四处争取小型设计项目。'),('The staff were hustling everyone out before closing time.','关门前，工作人员正催着大家离开。'),sources=S('hustling','hustle'))
W('hustler','英 /ˈhʌslə/；美 /ˈhʌslər/','积极奔忙、善抓机会的人；设局骗钱的人；拉客者等〔依语境〕',
 '创业谈话里 a hustler 可能是能四处跑、把机会变成收入的人；台球厅里却可能是故意装弱再设局赢钱的人。-er 只命名角色，不替你决定褒贬。',
 'hustle 去 e 加完整 -er；早期已有盗贼等贬义人物用法，后来形成积极工作者义，并非所有贬义都由现代奋斗形象后来变坏而来。',HUSTLE+[['hustle + -er → hustler','实施不同 hustle 行为的人；具体角色依分支']],
 'a business hustler 善于跑生意、抓机会的人；a pool hustler 台球设局骗钱的人；street hustler 街头拉客、牟利者。',
 'a determined hustler；watch out for hustlers。',
 'hustler 也有性交易拉客、卖淫者等俚语义；脱离语境直接夸陌生人是 hustler 可能造成误解，学习时记住这族不是单纯的努力者。',
 ('She is a resourceful hustler who always finds new customers.','她是个办法多、善于争取机会的人，总能找到新客户。'),('The pool hustler pretended to be a beginner.','那个台球骗手故意装成新手。'),sources=S('hustler','hustler'))
W('hustlers','英 /ˈhʌsləz/；美 /ˈhʌslərz/','积极奔忙、抓机会的人；设局骗钱者、拉客者等〔复数〕',
 '一群人四处跑生意，也可以是 hustlers；如果句子说的是设套骗钱，则是骗子。先看他们到底在做什么。',
 'hustle 去 e 加 -er → hustler，再加 -s，读 /z/；不同语义角色共用复数。',HUSTLE+[['hustle → hustler → hustlers','多个积极奔忙者，或多个设局、拉客牟利者']],
 'young business hustlers 积极跑生意的年轻人；pool hustlers 台球骗手。',
 'street hustlers；a group of hustlers。',
 'hustlers 的褒义通常依靠 business、resourceful 等背景，贬义常由骗局对象、行为说明；不能只查一个中文词就决定全部句子。',
 ('The neighbourhood was full of young hustlers building small businesses.','这个街区里有许多积极奔忙、经营小生意的年轻人。'),('Tourists were warned about street hustlers selling fake tickets.','游客被提醒留意那些在街头卖假票的骗子。'),sources=S('hustlers','hustler'))
W('hurry','英 /ˈhʌri/；美 /ˈhɜːri/','赶快；催促；匆忙',
 '离开车只剩两分钟，动作得加快，是 hurry；别人慢，你催他，也用 hurry。名词 a hurry 就是时间压着人走的匆忙。',
 '基础来源未定，有快速运动、嗡鸣材料或 harry 变体等分析；现代动词发展出匆忙名词，不硬指定一条尚未证实的古代路线。',HURRY,
 'hurry up 快点；in a hurry 匆忙；hurry someone 催某人；hurry to the station 赶去车站。',
 'there is no hurry 不着急；don’t hurry me 别催我。',
 'hurry 强调时间紧、需要快，walk fast 只说走得快；人可以走得快而不着急，也可以着急但根本走不动。',
 ('We must hurry or we will miss the train.','我们得赶快，不然就赶不上火车了。'),('There is no hurry; take your time.','不着急，慢慢来。'),sources=S('hurry','hurry'))
W('hurries','英 /ˈhʌriz/；美 /ˈhɜːriz/','赶快、催促〔第三人称单数〕',
 '他每天赶着去车站，是 he hurries to the station；把别人催得也加快，后面则接人作宾语。',
 'hurry 的 y 变 i 加 -es → hurries，读 /z/ 结尾；常用为动词三单。',HURRY+[['hurry → hurries','他赶快行动，或催别人行动']],
 'hurries to work 匆忙去上班；hurries the children along 催孩子往前走。',
 'hurries out of the room；hurries to finish。',
 'hurries to finish 强调赶着完成，finishes early 只说明完成时间早；赶得急不保证真能更早完成。',
 ('He hurries to the station every morning.','他每天早上都匆匆赶去车站。'),('She hurries the children along when they stop to look at toys.','孩子们停下看玩具时，她就催他们往前走。'),sources=S('hurries','hurry'))
W('hurried','英 /ˈhʌrid/；美 /ˈhɜːrid/','赶紧、催促了；匆忙的',
 '没时间慢慢来，一边穿外套一边告别，是 a hurried goodbye；过去匆匆走掉，也是 hurried。',
 'hurry 的 y 变 i 加完整 -ed，读 /d/；过去分词作形容词，表示时间压迫下做得匆忙。',HURRY+[['hurry → hurried','过去赶快行动；或形容匆忙完成']],
 'a hurried meal 匆匆吃的一餐；a hurried explanation 匆忙的解释；hurried home 匆匆回家。',
 'hurried footsteps 急促脚步；a hurried glance 匆匆一瞥。',
 'hurried 不一定准确、充分，quick 也不一定草率；a quick but careful check 可以又快又仔细，a hurried check 常更带时间不够的感觉。',
 ('We ate a hurried breakfast before leaving.','出发前，我们匆匆吃了早餐。'),('She hurried home when the rain began.','开始下雨时，她匆匆赶回了家。'),sources=S('hurried','hurry'))
W('hurrying','英 /ˈhʌriɪŋ/；美 /ˈhɜːriɪŋ/','正在赶快、匆忙行动；催促',
 '低头看表、脚步加快，正赶着去某处，是 hurrying；也能写催着别人抓紧。',
 'hurry + -ing，保留 y → hurrying；与 hurries、hurried 的变 y 为 i 分开记。',HURRY+[['hurry + -ing → hurrying','赶时间、催促的过程正在发生']],
 'hurrying home 正匆匆回家；hurrying to catch a bus 正赶着乘公交。',
 'no point hurrying 赶也没意义；hurrying the children along。',
 'hurrying 说明正赶时间，running 才说明跑；人也可能骑车、坐车，心急地加快进程。',
 ('She was hurrying home before the storm.','暴风雨来前，她正匆匆往家赶。'),('There is no point hurrying; the train has already left.','赶也没用了，火车已经开走。'),sources=S('hurrying','hurry'))
W('hurriedly','英 /ˈhʌrɪdli/；美 /ˈhɜːrɪdli/','匆忙地；急急忙忙地',
 '话还没说完就拿上包往外走，东西都来不及检查，做事的样子是 hurriedly。副词把时间紧、来不及从容的方式写出来。',
 'hurried + -ly；内层 hurry 变 y 为 i 加完整 -ed，外层 -ly 写方式。-ed 在这里读 /d/，前面的元音来自 hurry 本身的词尾。',HURRY+[['hurry → hurried → hurriedly','匆忙的性质，转成做事时的方式']],
 'hurriedly packed 匆忙收拾；hurriedly left 匆匆离开；hurriedly explained 急忙解释。',
 'hurriedly written note 匆忙写下的便条；hurriedly gathered her things。',
 'hurriedly 常突出赶时间造成的匆忙，efficiently 强调做事有效率；快并不自动等于高效。',
 ('She hurriedly packed a bag and left.','她匆忙收拾了一个包就走了。'),('He hurriedly explained why he was late.','他急急忙忙地解释自己为何迟到。'),sources=S('hurriedly','hurry'))
W('unhurried','英 /ʌnˈhʌrid/；美 /ʌnˈhɜːrid/','从容、不匆忙的',
 '有时间慢慢吃、慢慢看，不被时钟推着走，是 unhurried；常让人感觉节奏稳、留有余地。',
 '否定 un- + hurried；内层 hurry 变 y 为 i 加 -ed，外层否定匆忙状态。',HURRY+[['hurry → hurried → unhurried','从赶时间的性质，到不匆忙、从容']],
 'an unhurried pace 从容的步调；an unhurried lunch 不慌不忙的一顿午餐。',
 'calm and unhurried；an unhurried conversation。',
 'unhurried 常带从容感，slow 只说速度慢；效率低、拖沓未必能用带欣赏意味的 unhurried 概括。',
 ('We enjoyed an unhurried lunch by the river.','我们在河边从从容容地吃了顿午餐。'),('She spoke in a calm, unhurried voice.','她说话平静而从容。'),sources=S('unhurried','hurry'))
W('unhurriedly','英 /ʌnˈhʌrɪdli/；美 /ʌnˈhɜːrɪdli/','从容地；不慌不忙地',
 '人一项项检查，做完再做下一项，不被催得乱套，叫 unhurriedly。它常写做事留有节奏。',
 'unhurried + -ly；内层 un- 否定 hurried，外层修饰动作方式。这里的 -ed 读 /d/，-ly 读 /li/。',HURRY+[['unhurried + -ly → unhurriedly','以从容、不匆忙的方式做事']],
 'walked unhurriedly 从容地走；unhurriedly checked 不慌不忙地检查。',
 'answered unhurriedly；unhurriedly finished his tea。',
 'unhurriedly 不慌忙，reluctantly 不情愿；动作慢可以因为从容，也可以因为不愿意，副词说明不同原因、态度。',
 ('He unhurriedly checked each item on the list.','他不慌不忙地核对清单上的每一项。'),('She walked unhurriedly through the empty station.','她从容地走过空荡荡的车站。'),sources=S('unhurriedly','hurry'))
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_zgp',ROOTS,WORDS)
 extend_lessons()
