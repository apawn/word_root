"""Pick and the separate brine history of pickle."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
P=[['古英语、中古英语挑、啄、刺相关词 → pick','用尖端挑、摘取'],['现代 pick','从一堆里取出 → 挑选；摘、采及相应工具']]
def H(f,m):return P+[[f,m]]
W('pick','/pɪk/','挑选；摘、采；挑取；镐、拨片等工具',
 '从一堆东西里取一个，是挑选；把果子从枝头取下，是采摘。尖端挑取的画面还能用于工具。',
 '英语古老挑、啄、刺相关词形成现代 pick，与相邻日耳曼词有联系；具体远源不强作确定的拟声故事。',P,
 'pick a book 选一本书，pick apples 摘苹果，pick up 拿起、接人等；a guitar pick 吉他拨片，an ice pick 冰锥。',
 'pick a book；pick apples；take your pick；pick up。',
 'pick 不一定慢慢精挑，choose 更中性的选择；pick a flower 采花与 pick a flower pattern 选择花纹，宾语决定动作。',
 ('Pick any seat you like.','随便选一个你喜欢的座位。'),('We picked apples in the orchard.','我们在果园摘苹果。'))
W('picky','/ˈpɪki/','挑剔的；过分讲究选择的',
 '不是随便拿一个，而是这个不要、那个也不要，选起来要求很多。',
 'pick + -y，pick 保留 ck 后直接加 y，不写 pickky。取挑选义扩展为爱挑剔的性质。',H('pick + -y → picky','爱选择、筛选 → 挑剔的'),
 'a picky eater 挑食的人，picky about details 对细节挑剔；常有轻微批评语气。',
 'a picky eater；picky about；too picky。',
 'picky 挑剔，careful 谨慎；有要求未必不合理，具体语气由说话者评价给出。',
 ('He is a picky eater and dislikes many vegetables.','他很挑食，不喜欢许多蔬菜。'),('She is picky about the details of the design.','她对设计细节很讲究。'))
W('picker','英 /ˈpɪkə/；美 /ˈpɪkər/','采摘者；挑选器、选择控件',
 '可能是从树上摘果的人，也可能是软件里让你选颜色、日期的小工具。',
 'pick + -er，形成执行摘取、选择的人或工具名。现代用户界面的 picker 是功能名，不是屏幕里住着一个工人。',H('pick + -er → picker','摘取、选择的主体或工具'),
 'a fruit picker 采果工，a colour picker 颜色选择器，a date picker 日期选择控件。',
 'a fruit picker；a colour picker；a date picker。',
 '-er 不只人；colour picker 是选择工具，fruit picker 也可能按具体上下文指设备。',
 ('Fruit pickers started work early in the morning.','采果工清早就开始工作。'),('Use the colour picker to change the background.','用颜色选择器改变背景色。'))
W('toothpick','/ˈtuːθpɪk/','牙签',
 '一根细小工具，伸进牙齿缝隙挑出卡住的碎屑；名字直接按用途组合。',
 'tooth 牙 + pick 挑取工具。前部名词通常用单数 tooth，不是因为只允许碰一颗牙。',H('tooth + pick → toothpick','挑取牙间碎屑的工具 → 牙签'),
 'a wooden toothpick 木牙签，a box of toothpicks 一盒牙签。',
 'a wooden toothpick；a box of toothpicks；a cocktail toothpick。',
 'toothpick 细签工具，toothbrush 牙刷；两个词都与牙相关，工具结构与用途不同。',
 ('The waiter brought a small box of toothpicks.','服务员拿来一小盒牙签。'),('A toothpick held the sandwich pieces together.','一根牙签把几块三明治固定在一起。'))
W('pickpocket','英 /ˈpɪkpɒkɪt/；美 /ˈpɪkpɑːkɪt/','扒手；扒窃',
 '趁人不注意从口袋、随身物品中偷东西的人；固定词首先是一个人物角色。',
 'pick 掏取 + pocket 口袋，动词加宾语式成词，称执行这动作的人，也可再用作动词。',H('pick + pocket → pickpocket','掏口袋偷东西的人 → 扒手'),
 'watch out for pickpockets 小心扒手，a suspected pickpocket 可疑扒手；不展开具体盗窃手法。',
 'watch out for pickpockets；a suspected pickpocket；crowded places。',
 'pickpocket 是人物名，不是任意一个带口袋的东西；pocket 单独也可作把东西放进口袋的动词。',
 ('A sign at the station warned passengers about pickpockets.','车站标牌提醒乘客提防扒手。'),('The police arrested a suspected pickpocket.','警方逮捕了一名疑似扒手。'))
W('nitpick','/ˈnɪtpɪk/','吹毛求疵；挑小毛病',
 '对很细小的问题揪着不放，像一根根头发里找小虫卵一样仔细挑。',
 'nit 虱卵 + pick 挑，取细小、逐个挑取的画面，后来专门用于过分挑剔琐碎问题。',H('nit + pick → nitpick','细挑虱卵的画面 → 吹毛求疵'),
 'nitpick over details 为细节吹毛求疵，nitpick at someone’s work 挑工作的小毛病。',
 'nitpick over；nitpick at；stop nitpicking。',
 'nitpick 评价注意力过度放在小错，proofread 校对本来就是找字词错误，不能把细致校对一概说吹毛求疵。',
 ('We should solve the main problem instead of nitpicking over wording.','我们应解决主要问题，而不是对措辞吹毛求疵。'),('She felt he was nitpicking at every small decision.','她觉得他对每个小决定都在挑刺。'))
PI=[['中古荷兰语、低地德语 pekel 盐水 → 中古英语 pikel','腌渍用盐水、酱汁'],['现代 pickle','腌制物、泡菜 → 困境比喻']]
W('pickle','/ˈpɪkəl/','腌菜；腌制；困境',
 '把食物放入盐水、醋等腌渍环境；美式常见 a pickle 是一根腌黄瓜，in a pickle 则是陷入麻烦。',
 '主要腌菜义借低地地区 pekel 盐水词，不是英语 pick 挑选加表示小的 -le。另有较冷同形小份义可能与 pick 相关，本页不混讲。',PI,
 'pickled vegetables 腌蔬菜，a jar of pickles 一罐腌黄瓜或腌菜；be in a pickle 遇到难办局面。',
 'a jar of pickles；pickle vegetables；in a pickle。',
 'pickle 与 pick 看着像，不代表腌菜来自挑选的小东西；in a pickle 是固定比喻，不是人真的泡在罐里。',
 ('She makes pickles from the cucumbers in her garden.','她用自家花园的黄瓜做腌菜。'),('We are in a pickle now that the last bus has gone.','末班车已经走了，我们现在有麻烦了。'))
R('B3757','挑选、摘取与细小工具；腌菜另源','PICK：取出、选择；PICKLE 腌菜走盐水词源','pick → picky、picker 紧挨着，再按 toothpick、pickpocket、nitpick 各自对象理解；pickle 单列另源。',
 'pick 接挑、啄、刺的古老词，腌菜 pickle 则接低地地区盐水词。拼写相似不是充分同源证据。',
 'pick → picky、picker；tooth、pocket、nit 参与挑取组合；共享 pickup；pickle 腌渍另源。',
 [['基本动作与性质、主体','pick · picky · picker'],['工具、人物与琐碎批评','toothpick · pickpocket · nitpick · pickup'],['另源腌渍词','pickle']],
 'picky 挑剔，picker 选择者或工具；pickle 不拆 pick + -le；nitpick 带过分挑小错的评价。',
 'The picky customer used the colour picker to choose an exact shade.\n\n讲究的顾客用颜色选择器选定一个精确色调。',
 'pick picky picker toothpick pickpocket nitpick pickup pickle')
if __name__=='__main__':save('continuation_20261029_eq',ROOTS,WORDS)
