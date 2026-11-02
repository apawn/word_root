"""Abandon and bake: letting go and working with dry heat."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
A=[['古法语 à bandon、abandoner 等','交由支配、任其处置；放开控制'],['中古英语 abandounen → abandon','交出、放弃；后来抛下不管'],['不同派生或借入支线','abandoned 被遗弃、荒废；法语 abandonnement → abandonment']]
W('abandon','/əˈbændən/','放弃、抛弃、离弃；放纵、尽情〔名词〕',
 '原来抓在手里的东西，彻底松手不再管：可以放弃计划、离开危险船只，也可以把人丢下。with abandon 则像把自我约束也松开。',
 '借古法语 abandoner，联系 à bandon“任其处置、交由支配”，bandon 是权力、管辖词，不是英语 band 乐队；放开控制后发展出放弃、遗弃等义。名词放纵另有法语借入。',A,
 'abandon a plan 放弃计划，abandon ship 弃船，abandon someone 抛下某人，with abandon 无拘无束、放开地。',
 'abandon a plan；abandon ship；abandon hope；with abandon。',
 'abandon 常比 leave 更有彻底放手、不再继续或不顾照料的感觉；with abandon 的名词用法未必贬义。',
 ('They abandoned the plan after the test failed.','测试失败后，他们放弃了计划。'),('The children danced with abandon.','孩子们无拘无束地跳着舞。'),
 sources=['https://www.etymonline.com/word/abandon','https://en.wiktionary.org/wiki/abandon#English'])
W('abandoned','/əˈbændənd/','被抛弃的、荒废的；放纵的〔较旧或文学〕',
 '以前有人住、有人照管，现在不再管，门窗任风雨侵蚀，就是 abandoned building；-ed 把镜头放到被留下的对象。',
 'abandon + -ed 的分词形容词，已有较早对应形式；也保留放任自己、放纵的文学支线。不是每座空楼都必然永久废弃。',A[:2]+[['abandon + -ed → abandoned','被遗弃、无人照管；另有放纵支线']],
 'an abandoned factory 废弃工厂，an abandoned vehicle 被弃车辆，an abandoned project 被放弃项目。',
 'an abandoned factory；an abandoned vehicle；an abandoned project。',
 'empty 只说空，abandoned 更说被不再使用、照管；暂时没人在的房子可能 empty，却不是 abandoned。',
 ('The film was shot in an abandoned factory.','电影在一家废弃工厂里拍摄。'),('They found an abandoned bicycle beside the path.','他们在小径旁发现了一辆被丢下的自行车。'))
W('abandonment','/əˈbændənmənt/','放弃、遗弃；被遗弃的状态',
 '把松手不管这件事或它留下的处境当名词谈：项目被放弃，或人感到自己被抛下。',
 '借法语 abandonnement，接 abandonner 的同一交出、放弃词族；现代可对应 abandon + -ment，但历史不只是在英语里新贴后缀。',A[:1]+[['法语 abandonner → abandonnement → 英语 abandonment','放弃、遗弃行为或相应状态']],
 'the abandonment of a plan 放弃计划，a sense of abandonment 被抛下的感觉，years of abandonment 多年无人照管。',
 'the abandonment of；a sense of abandonment；years of abandonment。',
 'abandonment 行为或处境，abandoned 描述对象；词尾 -ment 不是每次都指一件可数实体。',
 ('The storm led to the abandonment of the expedition.','风暴导致考察行动被放弃。'),('The novel explores the child’s sense of abandonment.','小说探讨了孩子感到被抛下的心情。'))
R('B2432','原先控制、坚持的，后来彻底松手','ABANDON：放开控制，可能是不再管','abandon → abandoned；abandonment 经法语名词支线。with abandon 借松开自我约束的感觉。',
 '放弃计划、弃船、遗弃他人和尽情跳舞，选的对象不同；不能只记一个永远负面的抛弃。',
 'à bandon、abandoner → abandon；abandon + -ed → abandoned；abandonnement → abandonment。',
 [['放手动作和尽情状态','abandon'],['被放弃的对象与遗弃过程','abandoned · abandonment']],
 'abandoned/empty 不再照管与只是空着；abandonment/abandoned 名词与性质；bandon 不等于英语乐队。',
 'The abandoned building showed signs of years of abandonment.\n\n废弃建筑显露出多年无人照管的痕迹。','abandon abandoned abandonment')
B=[['古英语 bacan → 中古英语 baken → bake','用干热把食物烘熟、烤熟'],['古老人物词及现代相关派生','bæcere → baker；bake + -ing → baking；bake + -ery → bakery'],['热感引申','天气 baking 像在烤箱里一样热']]
W('bake','/beɪk/','烘烤、烤；烤成；晒得炙热',
 '把面团、土豆放进干热环境，让里外慢慢熟；太阳晒得人像进了烤箱，也能说 bake。',
 '继承古英语 bacan，属于古老日耳曼烘烤词族；现代动词不只用于蛋糕，也可烤土豆、加工材料。',B,
 'bake a cake 烤蛋糕，bake bread 烤面包，bake in the sun 在太阳下烤得难受，bake until golden 烤至金黄。',
 'bake a cake；bake bread；bake potatoes；bake in the sun。',
 'bake 常用烤箱或干热，steam 用蒸汽，fry 用油煎炸；roast 与 bake 在烤制用法上有重叠，不用一个绝对的食材表硬划。',
 ('She baked a loaf of bread.','她烤了一条面包。'),('The clay figures baked in the hot sun.','黏土小像在烈日下晒得干硬。'))
W('baking','/ˈbeɪkɪŋ/','烘焙、烘烤；烘烤用的；酷热的',
 '把烤东西的整套动作叫 baking；a baking tray 是用来烤的盘；It is baking 则像说天气开了烤箱。',
 'bake + -ing，去末尾 e，中古英语已有相关形式。过程名词、用途修饰与酷热形容词是不同句法场景。',B[:1]+[['bake + -ing → baking','烘烤过程；烘烤用途、酷热性质']],
 'home baking 家庭烘焙，a baking tray 烤盘，baking powder 泡打粉，baking hot 酷热。',
 'home baking；a baking tray；baking powder；baking hot。',
 'baking powder 泡打粉与 baking soda 小苏打不是同一个配方名称；此处知道名称区别，不靠词根判断替换用量。',
 ('She spends Sunday mornings baking.','她常在周日早晨烘焙。'),('It was baking hot in the car.','车里热得像烤箱。'))
W('baker','英 /ˈbeɪkə/；美 /ˈbeɪkər/','面包师、烘焙师',
 '常做面包、糕点等烘焙食品的人；这是职业、技能角色，不保证只做一种面包。',
 '现代对应 bake + -er，但人物词古英语 bæcere 已有，不是现代人第一次把 -er 贴在 bake 上。',B[:1]+[['古英语 bæcere → 中古英语 bakere → baker','对应 bake + -er 的烘焙从业者']],
 'a skilled baker 熟练面包师，a local baker 当地面包师，an apprentice baker 学徒面包师。',
 'a skilled baker；a local baker；an apprentice baker。',
 'baker 是人，bakery 是地方或业务；go to the baker’s 常省说去面包师的店，不是店本身变成人。',
 ('The baker starts work before dawn.','面包师天亮前就开工。'),('She trained as a baker after leaving school.','离校后，她受训成为烘焙师。'))
W('bakery','/ˈbeɪkəri/','面包房、烘焙店；烘焙业务',
 '把烘焙集中起来做、卖的地方；可以看到后厨，也可以只是买面包糕点的店面。',
 'bake + -ery，-ery 命名从事活动的场所、业务；容易和 baker 并排理解，但不是 baker + y 才是唯一构词层级。',B[:1]+[['bake + -ery → bakery','烘焙场所、售卖店和相应业务']],
 'a local bakery 当地烘焙店，a bakery counter 烘焙柜台，fresh from the bakery 刚从面包房做出或买来。',
 'a local bakery；a bakery counter；fresh from the bakery。',
 'bakery 地方或业务，baker 人；café 可卖糕点，但核心名称说咖啡馆，不保证店内自己烘焙。',
 ('A new bakery opened on our street.','我们街上新开了一家烘焙店。'),('The bakery sells bread and small cakes.','这家面包房卖面包和小蛋糕。'))
R('B3770','干热烘熟，再分动作、从业者与场所','BAKE：烤；BAKER：做烤食的人；BAKERY：做卖烤食的地方','bake → baking；baker 古老人物形式；bakery 接 -ery 场所业务后缀。',
 '人、店和过程放在一块，词尾用途就清楚。baking 的酷热义还可借烤箱感受来理解。',
 'bacan → bake；bæcere → baker；bake + -ing/-ery → baking、bakery。',
 [['烘烤动作与过程','bake · baking'],['人物与场所','baker · bakery']],
 'baker/bakery 人与场所；bake/steam/fry 干热、蒸汽与油烹；bakery 的 -ery 不漏拆。',
 'The baker was baking bread in the bakery.\n\n面包师正在面包房里烤面包。','bake baking baker bakery')
if __name__=='__main__':save('continuation_20261030_fu',ROOTS,WORDS)
