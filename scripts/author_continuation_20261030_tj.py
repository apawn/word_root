"""Agents and things: raids, roosts, sport, troops and harvests."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'A1697':dict(words=['raid','raider','roost','rooster','camp','camper','cricket','cricketer','troop','trooper','reap','reaper'],label='突袭、露营、球手与收割：-er 的具体角色',note='-er 的对象由基础词决定：camper 可以是人或露营车，reaper 可以是人或机器；rooster 已固定为公鸡，不泛指一切栖息者。cricketer 接板球运动义，不能从蟋蟀义推出。'),
}
W('raid','/reɪd/','突袭、突然搜查；突袭式取走〔口语〕',
 '一群人突然冲到某处，快速攻击或搜查。口语 raid the fridge 则像突然向冰箱出击，翻找东西吃。',
 '接苏格兰和英格兰北部 raid、rade 等骑行、出征词，向前追到古英语 rad，与 road 同族。现代突袭义不要求骑马。',
 [['古英语 rad → 北部、苏格兰语 raid','骑行出征、袭击'],['现代 raid 的扩大用法','军事突袭、突然搜查；口语突然翻找取用']],
 'a police raid 警方突查；an air raid 空袭；raid a warehouse 突袭仓库；raid the fridge 翻冰箱找吃的。名词和动词都常见。',
 'carry out a raid；a raid on a building。','attack 范围较广；raid 常突出突然、快速进入某处的一次行动。raid 也可能用于查缉，并非只指军队攻击。',
 ('Police carried out a raid on the warehouse.','警方对仓库进行了突击搜查。'),('The children raided the fridge after school.','孩子们放学后翻冰箱找东西吃。'),sources=['https://www.etymonline.com/word/raid','https://en.wiktionary.org/wiki/raid#English'])
W('raider','英 /ˈreɪdə/；美 /ˈreɪdər/','突袭者、劫掠者；进行突袭式行动的人',
 'raid 是那次突然闯入，raider 是参加行动的人。旧的军事、劫掠画面也被借到商业、游戏等语境。',
 'raid + -er，动作后加人物后缀。随着 raid 扩展到不同场景，raider 也能称不同类型的突袭行动者。',
 [['raid 突袭 + -er','执行突袭的人'],['raider 的具体与比喻用法','劫掠者、突袭者；突袭式收购等行动者']],
 'armed raiders 持械突袭者；a corporate raider 进行突袭式企业收购的人；raiders from the sea 从海上来的劫掠者。',
 'a band of raiders；the raiders retreated。','rider 是 ride 骑乘的人，raider 则接 raid 突袭。两词只差一个 a，常用读音也不同：/ˈraɪdə/ 与 /ˈreɪdə/。',
 ('The raiders escaped before dawn.','突袭者们在黎明前逃走了。'),('The fort was built to defend the coast against raiders.','这座堡垒是为抵御劫掠者、保卫海岸而建的。'))
W('roost','/ruːst/','鸟的栖息处、栖架；栖息、归栖',
 '天黑后，鸡、鸟停在一根架子或固定地方休息。roost 可以叫那处地方，也可以说回那里歇下。',
 '古英语 hrost 有木构架、鸟栖架等义，经中古英语 roste 延续。作为栖架的东西，进一步联系鸟栖息的动作。',
 [['古英语 hrost → 中古英语 roste','木架；家禽歇息的栖架'],['现代 roost 的名词、动词','栖息处；鸟在固定地方栖息']],
 'birds roost in trees 鸟在树上歇息；return to the roost 回栖处。rule the roost 是当家做主、掌控局面。',
 'a communal roost；come home to roost。','nest 通常是筑巢、产卵育雏的巢；roost 侧重休息的地方。come home to roost 也可说先前的行为终于带来不良后果。',
 ('The birds roost in the old oak tree.','这些鸟在那棵老橡树上栖息。'),('The chickens returned to their roost at sunset.','日落时，鸡回到了栖架上。'))
W('rooster','英 /ˈruːstə/；美 /ˈruːstər/','公鸡',
 '构词上是 roost 加 -er，现代意思却已经收窄成公鸡。记住这个固定名称，就能把动物和夜里上架歇息的习性连起来。',
 'roost 栖息 + -er，较早也有 roost cock 这类表达。rooster 后来尤其在美式英语中普及为公鸡名。',
 [['roost 的栖息动作与旧相关名称','栖架上歇息的家禽'],['rooster 的固定动物名称','公鸡，尤常见于美式表达']],
 'a rooster crows 公鸡啼叫；a rooster and several hens 一只公鸡和几只母鸡。复数 roosters。',
 'a crowing rooster；the farm’s rooster。','hen 是母鸡，rooster 是公鸡；chicken 可泛指鸡。rooster 的 -er 虽能看出构词联系，词义已固定，不能泛指所有栖息的鸟。',
 ('The rooster crowed before sunrise.','公鸡在日出前啼叫。'),('A rooster stood beside the hens in the yard.','院子里，一只公鸡站在母鸡旁边。'),sources=['https://www.etymonline.com/word/rooster','https://en.wiktionary.org/wiki/rooster#English'])
W('camper','英 /ˈkæmpə/；美 /ˈkæmpər/','露营者；露营车、宿营车',
 'camp 说扎营，camper 最容易想到住帐篷、参加营地活动的人；另一支把能住的露营车辆也叫 camper。',
 'camp 动词 + -er。人物义指进行露营的人，车辆义则把为露营提供居住空间的设备纳入名称。',
 [['camp 扎营 + -er','露营活动的参与者'],['camper 的车辆用法','可供露营居住的车辆或相应装置']],
 'a group of campers 一群露营者；a camper van 露营车。单独 camper 是人还是车，要看动词和场景。',
 'summer campers；travel in a camper。','camp 是营地、露营等基础词，camper 指参与者或车辆。a happy camper 还常口语说满意的人，尤其见于 not a happy camper。',
 ('The campers put up their tents before dark.','露营者们在天黑前搭好了帐篷。'),('They travelled along the coast in a camper.','他们开着露营车沿海岸旅行。'))
W('cricket','/ˈkrɪkɪt/','板球运动；蟋蟀',
 '球场上的 cricket 是板球；草丛里叫的 cricket 是蟋蟀。两个常用意思同形同音，却应分开追词源。',
 '蟋蟀名经古法语 criquet，与吱叫、咯吱声的拟声材料相连；板球名可能接古法语或荷兰语方言中木棍、球门柱等材料，细节未定。',
 [['蟋蟀这一支：古法语 criquet 等','从鸣声相关材料称呼昆虫'],['板球这一支：早期棍棒、球门材料的可能联系','形成球类运动名称，确切路径有讨论']],
 'play cricket 打板球；a cricket match 板球比赛；hear a cricket 听见一只蟋蟀叫。运动义通常不可数，昆虫义可数。',
 'a cricket bat；the chirping of crickets。','cricketer 是板球运动员，接运动义。用同一个 spelling 记住两义可以，但不要编造蟋蟀变成板球的故事。',
 ('They play cricket in the park on Saturdays.','他们星期六在公园打板球。'),('A cricket was chirping outside the window.','窗外有只蟋蟀在叫。'),sources=['https://www.etymonline.com/word/cricket','https://en.wiktionary.org/wiki/cricket#English'])
W('cricketer','英 /ˈkrɪkɪtə/；美 /ˈkrɪkɪtər/','板球运动员、打板球的人',
 'cricket 取板球运动这一义，再加人物后缀，就是上场打板球的人。职业、业余球手都能用。',
 'cricket 板球 + -er，构成参与运动的人物名词。加后缀时采用的是运动义，不能跨到同形的昆虫义。',
 [['cricket 板球运动 + -er','由运动形成参与者名称'],['cricketer 的现代使用','板球运动员、板球爱好者']],
 'a professional cricketer 职业板球运动员；a young cricketer 年轻板球球手；an amateur cricketer 业余板球球手。',
 'an outstanding cricketer；a team of cricketers。','cricketer 是人；cricket 是运动或昆虫。其他球类通常有各自习惯称呼，不能把 cricketer 当所有持拍球手的总称。',
 ('She became a professional cricketer at a young age.','她很年轻就成了职业板球运动员。'),('The young cricketer spent hours practising his bowling.','那位年轻板球球手花了数小时练习投球。'))
W('troop','/truːp/','一队、一群；军队、士兵〔常用复数 troops〕；成群行进',
 '一批人、动物聚成一队，是 troop；作为动词，就是一群人一道走过去。军事语境里 troops 常指士兵们。',
 '从法语 troupe 人群、队伍借入，更远来源仍有不同分析。由集体名词发展出成群行进的动词。',
 [['法语 troupe → 英语 troop','一群人、一个队伍'],['troop 的集体、军事与动词用法','一队；troops 士兵；成群前往']],
 'a troop of monkeys 一群猴子；a scout troop 一队童子军；troops stationed nearby 驻扎附近的军队；troop into a room 成群走进房间。',
 'a cavalry troop；send troops。','troupe 常说演员、舞者等演出团体；troop 常说军队、童子军、动物群等。两词同源、同音，现代拼写分工不同。',
 ('A troop of monkeys crossed the path.','一群猴子穿过小路。'),('The children trooped into the dining room.','孩子们成群走进餐厅。'))
W('trooper','英 /ˈtruːpə/；美 /ˈtruːpər/','骑兵、某些部队的士兵；州警；能吃苦坚持的人〔口语〕',
 '本来是 troop 队伍里的士兵，后来也用于某些警察称呼。夸人撑得住、肯坚持时，口语也常见 a real trooper。',
 'troop + -er，早期常指骑兵。州警等义随后发展；能吃苦的人这一口语义，又与 trouper 演员、不畏困难的人发生拼写和词义交汇。',
 [['troop 队伍 + -er','骑兵、队伍中的士兵'],['警察称呼及口语发展','州警等；与 trouper 交汇的坚持、能吃苦义']],
 'a state trooper 美国某些州的州警；a cavalry trooper 骑兵；You’re a real trooper. 你真能扛、真肯坚持。具体军衔、组织称呼随语境而定。',
 'a young trooper；carry on like a trooper。','trouper 原指演出团体的演员，也发展出吃苦、敬业义。夸人能撑住常见两种拼写，不能把这一支只编成士兵勇敢的单一路径。',
 ('A state trooper helped the stranded driver.','一名州警帮助了那位被困的司机。'),('You were a real trooper through that long rehearsal.','那次漫长排练中，你真能坚持。'),sources=['https://www.etymonline.com/word/trooper','https://en.wiktionary.org/wiki/trooper#English'])
W('reap','/riːp/','收割；获得、收获〔成果、好处，也可指恶果〕',
 '把田里长成的谷物割下来带走，是 reap；先前付出或行为的结果落到自己身上，也像到了收获的时候。',
 '中古英语 repen 接古英语收割词族。由收取庄稼的动作转到收取劳动、行为带来的结果，比喻用法也有很长历史。',
 [['古英语收割词族 → 中古英语 repen','割下、收取成熟庄稼'],['现代 reap 的具体与比喻义','收割；得到先前努力、行为的结果']],
 'reap a harvest 收获庄稼；reap the benefits 获得好处；reap the rewards 得到回报；reap what you sow 自食其果、种什么得什么。',
 'reap the benefits of practice；reap a rich harvest。','reap 强调到了收取结果的一步；sow 是播种。reap 常见于好处、回报，但结果也可能负面，不能一概译成赚到。',
 ('The farmers reaped the wheat before the rain.','农民们在下雨前收割了小麦。'),('She is now reaping the benefits of years of practice.','她现在正收获多年练习带来的好处。'),sources=['https://www.etymonline.com/word/reap','https://en.wiktionary.org/wiki/reap#English'])
W('reaper','英 /ˈriːpə/；美 /ˈriːpər/','收割者；收割机；死神〔常见于 the Grim Reaper〕',
 'reap 是收割，reaper 是做收割工作的人或机器。死神形象拿着镰刀、像收割生命，因此也借用 Reaper 这个名字。',
 '中古英语人物词接较早古英语 ripere 等形式，与 reap + -er 对应。后来机器接手收割，名称也转到机器；文学中另有死神拟人用法。',
 [['reap 词族与旧人物名词','实施收割的人'],['reaper 的机器与拟人扩展','收割机；镰刀死神形象']],
 'a mechanical reaper 机械收割机；reapers in the field 田间收割者；the Grim Reaper 常见的死神名称。',
 'a grain reaper；the figure of the Reaper。','reaper 可以只负责收割；combine 常指把收割、脱粒等工序合在一起的联合收割机。两词不是所有场景都可互换。',
 ('The reapers worked in the field until sunset.','收割者们一直在田里干到日落。'),('The old reaper is displayed in the farming museum.','那台老式收割机陈列在农业博物馆里。'))
def extend_lessons():
    extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
    save('continuation_20261030_tj',ROOTS,WORDS)
    extend_lessons()
