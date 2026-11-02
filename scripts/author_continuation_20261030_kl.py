"""Side compounds, lazy and buzz."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
S=[['古英语 sīde → side','侧边、旁边等位置'],['名词 + side 的地点组合','dockside 码头边；graveside 墓旁；其他词各自固定范围']]
W('dockside','英 /ˈdɒksaɪd/；美 /ˈdɑːksaɪd/','码头边、船坞旁的区域；码头边的',
 '货物从船上卸下，在码头边堆放、转运，那一片近码头的区域可以叫 dockside。',
 'dock 码头、船坞 + side 旁边，按位置形成复合词，也可放在另一名词前修饰。',S,
 'at the dockside 在码头边，dockside warehouses 码头仓库，dockside workers 码头工人。',
 'at the dockside；dockside warehouses。',
 'dock 是船停靠等设施，dockside 重点是它旁边的区域；两者在具体地点中可能重叠，侧重点不同。',
 ('The cargo waited at the dockside.','货物等在码头边。'),('The old dockside warehouses became studios.','码头边的旧仓库改成了工作室。'))
W('graveside','/ˈɡreɪvsaɪd/','墓旁、墓边；墓边举行的',
 '人站在墓边悼念、举行仪式，那个紧邻坟墓的位置就是 graveside。grave 取坟墓义。',
 'grave 坟墓 + side 旁边。组合后常见于葬礼、悼念的地点或修饰语。',S[:1]+[['grave + side → graveside','坟墓旁边的位置、在那里进行的活动']],
 'at the graveside 在墓旁，a graveside service 墓边葬礼仪式。',
 'at the graveside；a graveside service。',
 'graveside 是一座墓旁的区域，graveyard 是墓地。grave 作形容词的严重、严肃义，在这里不是构词基础。',
 ('The family gathered at the graveside.','家人聚在墓旁。'),('A short graveside service followed.','随后举行了一场简短的墓边仪式。'))
R('A2220','在某物旁边、某一地带或一侧，形成地点名称','SIDE：以一个对象为参照，指出旁边或相应地带','dockside、graveside 与 roadside、bedside 等同样从参照物找位置；countryside 等再记固定范围。',
 'side 是能独立使用的词，也常作复合词后部。多数位置直观，已经固定的词仍要看实际用法。',
 'side 承古英语 sīde；dock 码头、grave 坟墓、road 路、bed 床等作前部参照物。',
 [['路、码头、场地等旁边','roadside · dockside · curbside · trackside · ringside · courtside'],['生活、悼念与水域位置','bedside · graveside · lakeside · poolside · oceanside · waterside'],['固定地带与地区视角','countryside · stateside']],
 'countryside 固定说乡村、乡野，不只是国家某一边；stateside 常从海外视角说在美国、回美国等。',
 'We left the roadside and walked toward the dockside warehouses.\n\n我们离开路边，走向码头旁的仓库。','roadside dockside curbside trackside ringside courtside bedside graveside lakeside poolside oceanside waterside countryside stateside')
L=[['16世纪英语 lazy；更早来源未定','有低地德语松散、无力相关词等分析'],['lazy 的不同评价','不愿费力；悠闲、缓慢；草率不用心'],['后缀与逆构','lazily、laziness；lazy → laze']]
W('lazy','/ˈleɪzi/','懒惰的；悠闲的、缓慢的；不用心的',
 '有事却不愿费力，是 lazy；一个没安排任务、慢慢过的下午，也可叫 a lazy afternoon。前者常批评，后者可以舒服。',
 '英语16世纪已见，远源不确定，可能联系低地德语等表示松散、无力的形式。不能把每个 -y 结尾词都假定有一个确定英语词干。',L[:2],
 'a lazy worker 懒散的人，a lazy afternoon 悠闲下午，lazy thinking 不用心的思考，a lazy river 缓缓流动的河。技术中 lazy evaluation 指需要时才计算的策略。',
 'a lazy afternoon；lazy thinking；lazy evaluation。',
 'lazy afternoon 可以称赞闲适，lazy excuse 常批评敷衍。疲惫 tired 与不愿努力的评价不同，不能只凭不动就判断懒。',
 ('We spent a lazy afternoon by the lake.','我们在湖边悠闲地过了一个下午。'),('The report relies on lazy assumptions.','报告依赖一些未经认真思考的假设。'))
W('lazily','/ˈleɪzɪli/','懒散地；悠闲、缓慢地',
 '人慢慢躺着翻书，云缓缓飘过，lazily 都能描写一种不急、不费劲的动作感。',
 'lazy + -ly，y 变 i。由性质形容词形成方式副词。',L[:2]+[['lazy + -ly → lazily','懒散、悠闲或缓慢地']],
 'stretch lazily 懒洋洋伸展，drift lazily 缓缓飘动，wave lazily 懒洋洋挥手。',
 'stretch lazily；drift lazily。',
 'lazily 可以只是描写慢、闲适的方式，不一定批评道德；carelessly 更明确强调没留意、粗心。',
 ('The cat stretched lazily in the sun.','猫在阳光下懒洋洋地伸展身体。'),('Clouds drifted lazily across the sky.','云缓缓飘过天空。'))
W('laziness','/ˈleɪzinəs/','懒惰、懒散；不用心',
 '把不愿费力、做事敷衍这种状态拿出来谈，就说 laziness。它常带批评语气。',
 'lazy + -ness，y 变 i。-ness 把性质变成名词，不是在说一个懒的人。',L[:2]+[['lazy + -ness → laziness','懒惰、懒散等状态、性质']],
 'sheer laziness 纯粹是懒，intellectual laziness 思想上不肯用功，out of laziness 因为懒。',
 'sheer laziness；intellectual laziness。',
 'laziness 是对不愿努力的描述、评价；lack of energy 只是缺少精力，原因可能不同。',
 ('He blamed his untidy desk on laziness.','他把桌子凌乱归因于自己懒。'),('The teacher challenged the class’s intellectual laziness.','老师批评全班不愿认真思考。'))
W('laze','/leɪz/','懒散度日、悠闲休息',
 '没有赶任务，躺着、坐着慢慢消磨时间，可以说 laze around、laze in the sun。',
 '从 lazy 逆构出的动词。表面能按 laze → lazy 学习，但真实历史上 lazy 先有，laze 后来才形成。另有 lava + haze 的专业同形混成词，本页不混入休息义。',L[:2]+[['lazy → laze〔逆构〕','形成懒散、悠闲休息的动词']],
 'laze around 悠闲待着，laze in the sun 晒太阳休息，laze on the sofa 懒洋洋躺在沙发上。',
 'laze around；laze in the sun。',
 'laze 是动作，lazy 是性质。laze around 可以是度假享受，也可按语气批评游手好闲。',
 ('They lazed in the sun after lunch.','午饭后，他们悠闲地晒太阳。'),('I spent Sunday lazing on the sofa with a book.','周日我拿着书，懒洋洋地窝在沙发上。'))
R('B3979','不愿费力与悠闲缓慢，两类语气要看对象','LAZY：动作慢、少费力，可以是批评也可以是闲适','lazy → lazily、laziness；laze 是后来逆构的休息动词。',
 '不要只记懒一个字。悠闲下午、缓流、草率思考，分别在说生活节奏、运动速度、投入程度。',
 'lazy 远源未定；-ly 副词，-ness 名词，均 y 变 i；逆构动词 laze。',
 [['性质、方式与状态','lazy · lazily · laziness'],['悠闲休息的动作','laze']],
 '疲惫不自动等于懒；lazy afternoon 可舒服；laze 的历史顺序晚于 lazy。',
 'We lazed by the lake and watched the clouds move lazily.\n\n我们在湖边悠闲休息，看云缓缓移动。','lazy lazily laziness laze')
B=[['拟声来源，中古英语已有相关形式','嗡嗡声，像蜂、机器的连续低响'],['群体谈话与兴奋的比喻','热议、活跃气氛；兴奋感'],['派生词','buzzing、buzzer、buzzy、abuzz']]
W('buzz','/bʌz/','嗡嗡声、嗡嗡响；热议、兴奋感；用蜂鸣器叫人',
 '蜂或机器嗡嗡响，人群低声又兴奋地议论，也像一片嗡嗡声。于是 buzz 从声音走向热度、活跃气氛和兴奋感。',
 '拟声词，中古英语已有相应嗡响形式。声音义再扩到谈话、传闻、兴奋；不是由一个表示昆虫的古典词根借来。',B[:2],
 'the buzz of bees 蜂的嗡嗡声，create a buzz 引发热议，get a buzz from something 因某事感到兴奋，Give me a buzz. 给我打个电话〔口语〕。',
 'create a buzz；get a buzz；give someone a buzz。',
 'buzz 可指话题热度，不保证是赞美，也不保证传闻属实。声响上常比 hum 更带嗡嗡、振动感，实际有重叠。',
 ('A bee buzzed past the window.','一只蜂嗡嗡飞过窗边。'),('The preview created a buzz among fans.','预告片在粉丝间引起热议。'))
W('buzzing','/ˈbʌzɪŋ/','嗡嗡声；嗡响、忙碌热闹的；兴奋的〔口语〕',
 '手机在桌上嗡嗡振动，现场热闹得像一窝蜂，或者人刚经历好事还兴奋着，都可能用 buzzing。',
 'buzz + -ing。分词可描述正在嗡响、活跃，也形成声音名词和兴奋的口语形容词。',B[:2]+[['buzz + -ing → buzzing','嗡响的声音、状态；兴奋活跃']],
 'a buzzing sound 嗡嗡声，buzzing with activity 忙碌热闹，I’m still buzzing. 我还兴奋着呢。',
 'a buzzing sound；buzzing with activity；still buzzing。',
 'buzzing phone 通常是声响、振动，buzzing fans 可以是兴奋状态。不要见 -ing 就全译成正在叫。',
 ('A buzzing sound came from the light.','灯那里传来嗡嗡声。'),('She was still buzzing after the performance.','演出结束后，她还兴奋着。'))
W('buzzer','英 /ˈbʌzə/；美 /ˈbʌzər/','蜂鸣器、蜂鸣装置；按响的呼叫按钮',
 '按一下，发出嗡鸣提醒或呼叫的装置，就是 buzzer；门禁、比赛计时都可能用它。',
 'buzz + -er，按发出声响的功能命名器具。',B[:1]+[['buzz + -er → buzzer','发出嗡鸣、提示声的装置']],
 'press the buzzer 按呼叫按钮，the buzzer sounded 蜂鸣器响了，at the buzzer 在终场蜂鸣响起时。',
 'press the buzzer；the buzzer sounded。',
 'buzzer 可说发声装置，也可按场景说按响它的按钮；bell 常是铃、钟类装置，不总能逐物替换。',
 ('Press the buzzer and someone will let you in.','按呼叫按钮，就会有人让你进去。'),('The buzzer sounded at the end of the round.','这一轮结束时，蜂鸣器响了。'))
W('buzzy','/ˈbʌzi/','带嗡鸣声的；热门、受到热议的',
 '音色有明显嗡鸣，可以 buzzy；新店、电影被很多人议论，也可叫 buzzy，借 buzz 的话题热度义。',
 'buzz + -y，形成带嗡声或具有讨论热度的性质词；也可按语境批评充满流行术语。',B[:2]+[['buzz + -y → buzzy','嗡鸣的性质；受到热议的']],
 'a buzzy sound 嗡嗡的声音，a buzzy new restaurant 热门新餐厅，a buzzy film 受到热议的电影。',
 'a buzzy sound；a buzzy new restaurant。',
 'buzzy 说热度、声音等性质；busy 说忙碌。拼写与发音不同，也不能保证热门东西一定好。',
 ('The guitar has a bright, buzzy tone.','这把吉他音色明亮，带着嗡鸣感。'),('They booked a table at a buzzy new restaurant.','他们在一家热门新餐厅订了位。'))
W('abuzz','/əˈbʌz/','充满热议、忙碌或兴奋的',
 '整间屋子都在议论一个消息，像响着一片嗡嗡声，可以说 the room is abuzz。',
 'a- 表处于某种状态 + buzz。常作表语，后面用 with 引出热闹、议论的内容或来源。',B[:2]+[['a- + buzz → abuzz','处于嗡响、活跃热议的状态']],
 'abuzz with excitement 充满兴奋，abuzz with rumors 议论着传闻，set the town abuzz 让全城议论起来。',
 'abuzz with excitement；abuzz with rumors。',
 '通常说 the room was abuzz，不照一般前置形容词随意说 an abuzz room。充满传闻也不代表传闻真实。',
 ('The office was abuzz with rumors of a move.','办公室里都在议论搬迁的传闻。'),('The hall was abuzz with excitement before the show.','演出前，大厅里洋溢着兴奋的气氛。'))
R('B4010','从嗡嗡声到群体议论、热度和兴奋状态','BUZZ：声音像一片嗡鸣，话题也能嗡嗡传开','buzz → buzzing、buzzer、buzzy；a- + buzz → abuzz；buzzword、buzzkill 看固定组合。',
 '声音、话题与情绪三条用法可以相互联想。讨论多不是自动好评，热闹也不是事实核验。',
 '拟声 buzz；-ing 声音、状态，-er 器具，-y 性质，a- 处于状态；word 术语，kill 扫兴形象。',
 [['基础与声音、器具','buzz · buzzing · buzzer'],['热度与充满热议','buzzy · abuzz'],['固定组合','buzzword · buzzkill']],
 'buzzy 不等于 busy；abuzz 常作表语；buzz 的热度可有褒贬。',
 'The buzzy film set the room abuzz, and everyone was still buzzing afterward.\n\n那部热门电影让满屋人议论起来，结束后大家仍很兴奋。','buzz buzzing buzzer buzzy abuzz buzzword buzzkill')
if __name__=='__main__':save('continuation_20261030_kl',ROOTS,WORDS)
