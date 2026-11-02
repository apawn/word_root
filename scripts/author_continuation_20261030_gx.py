"""Rub, climb, flower and gear: friction, upward movement, plant names and equipment."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
R0=[['中古英语 rubben → rub','擦、摩擦；更早具体来路不确定'],['英语 rub','擦动；摩擦的动作；妨碍、难处等比喻']]
W('rub','/rʌb/','擦、揉、摩擦；擦动；难处、障碍〔名词〕',
 '两个表面贴着来回动，手掌搓热、揉眼、擦污都抓这个动作；There’s the rub 则像事情卡在一个摩擦点。',
 '中古英语 rubben 延续为 rub，和一些日耳曼擦、刮词可能相关，更早来路不确定。现代加 -ing、-er 常双写 b。',R0,
 'rub your eyes 揉眼，rub your hands together 搓手，rub off 擦掉、沾染，rub it in 老拿痛处反复说；There’s the rub 问题就在这。',
 'rub your eyes；rub your hands together；rub off；rub it in。',
 'rub 强调表面接触摩擦，wipe 常是擦拭清掉，scrub 更用力刷洗；动作有重叠，力度、工具、目的不同。',
 ('He rubbed his hands together to warm them.','他搓了搓手取暖。'),('The job is interesting, but the long commute is the rub.','工作很有趣，可通勤太远就是难处。'))
W('rubbing','/ˈrʌbɪŋ/','擦揉、摩擦；拓印、拓片',
 '纸盖在有纹路的表面上，拿铅笔等在上面擦，底下凸纹就显出来；于是一次擦动还能得到一张 rubbing。',
 'rub 双写 b + -ing。既有普通动作形式，也有由擦印方法命名的拓片名词。',R0+[['rub + -ing → rubbing','擦的动作 → 通过擦拓得到的图像']],
 'rubbing his eyes 揉眼，make a rubbing 做拓片，a brass rubbing 铜碑、铜板拓印等。',
 'make a rubbing；a brass rubbing；rubbing his eyes。',
 'rubbing 拓印常靠纸上的摩擦显纹，drawing 直接绘画；同一作品看起来像图，不代表制作方式一样。',
 ('The children made leaf rubbings with crayons.','孩子们用蜡笔做了叶片拓印。'),('She was rubbing her eyes when the phone rang.','电话响时，她正在揉眼睛。'))
W('rubber','英 /ˈrʌbə/；美 /ˈrʌbər/','橡胶；橡皮〔英式〕；避孕套〔美式俚语〕；系列赛、局〔另源〕',
 '材料能把铅笔印擦掉，所以先按会擦的东西命名，后来 rubber 成了橡胶材料名；不是橡胶树自己天生就叫英语 rubbing tree。',
 '材料和橡皮义来自 rub + -er，名字与擦除用途有关，再扩展到制品。比赛中的 rubber 来路不明，别把三局赛说成橡胶比赛。',R0+[['rub + -er → rubber','能擦除的东西 → 橡皮、橡胶材料及制品'],['另一路 rubber 比赛用语','系列赛或其中一局等；更早来源不明']],
 'rubber gloves 橡胶手套，a rubber band 橡皮筋，an eraser 美式常说橡皮；美式 a rubber 可指避孕套。a rubber of bridge 桥牌一盘等。',
 'rubber gloves；a rubber band；a rubber〔地区义不同〕；a rubber of bridge。',
 '英式借 a rubber 常可借橡皮，美式可能听成避孕套；要说文具可用 eraser。rubber 比赛义不同来源，不强套擦除。',
 ('The gloves are made of rubber.','这副手套是橡胶做的。'),('She used a rubber to remove the pencil marks.','她用橡皮擦掉了铅笔印。'),sources=['https://www.etymonline.com/word/rubber','https://en.wiktionary.org/wiki/rubber#English'])
R('B3516','擦、揉及摩擦；擦除材料到橡胶','RUB：表面贴着动，能搓热、擦掉，也能显出纹路','rub → rubbing 擦揉、拓片；rubber 擦除物 → 橡胶及制品，比赛同形词另源。',
 'rubber 的材料义有实在用途来路，不必死背橡胶和擦为什么同族。rubbing 的拓片也把纸上擦、底纹显的过程讲清。',
 'rubben → rub；rub + -ing/-er 双写 b；比赛 rubber 更早来源不明。',
 [['擦揉动作与拓片','rub · rubbing'],['擦除物和材料','rubber']],
 'rub/wipe/scrub 摩擦、擦拭和用力刷洗；rubber/eraser 地区用法；比赛 rubber 不硬套橡胶。',
 'She rubbed the paper with a crayon to make a rubbing, then used a rubber on a stray pencil mark.\n\n她用蜡笔在纸上擦出拓印，再用橡皮擦掉一处多余的铅笔印。','rub rubbing rubber')
C=[['古英语 climban → 中古英语 climben → climb','抓着、攀着向上走'],['英语 climb','攀爬、爬升；数量、地位逐渐上升']]
W('climb','/klaɪm/','攀爬、爬升；上升；攀登过程',
 '手脚找支点，一步步往高处去；飞机、数字、事业也能沿上升画面用 climb。',
 '接古英语 climban，旧材料常与黏住、抓附等词族联系。现代 b 不发音，climbed、climbing、climber 中通常也不把 b 读回来。',C,
 'climb a tree 爬树，climb the stairs 爬楼梯，prices climb 价格上升，climb down 爬下来、放弃强硬立场；方向可用上下词指定。',
 'climb a tree；climb the stairs；prices climb；climb down。',
 'climb 常向上，但 climb down 明确往下，不能把所有用法硬译向上；rise 更泛上升，climb 常更有持续、费力的感觉。',
 ('The cat climbed the tree.','猫爬上了树。'),('Prices continued to climb throughout the year.','全年价格持续上升。'))
W('climber','英 /ˈklaɪmə/；美 /ˈklaɪmər/','攀登者；攀缘植物；向上攀附的人〔比喻〕',
 '人靠手脚攀，藤靠支撑向上长；社会上借关系往高位挤的人，也能用 social climber 批评。',
 'climb + -er，表执行者。b 仍不发音，-er 可指人，也可指会攀缘生长的植物。',C+[['climb + -er → climber','攀爬的人或植物；社会攀附比喻']],
 'a mountain climber 登山者，an experienced climber 有经验的攀登者，a vigorous climber 长势旺的攀缘植物，a social climber 钻营上流关系的人。',
 'a mountain climber；a climbing plant/climber；a social climber。',
 'climber 不是每次都是运动员；social climber 多带批评，不只是泛说努力上进的人。',
 ('The climber reached the ridge before noon.','攀登者在中午前到了山脊。'),('This rose is a vigorous climber.','这种蔷薇是一种长势旺盛的攀缘植物。'))
W('climbing','/ˈklaɪmɪŋ/','攀爬、攀登运动；攀缘的；climb 的 -ing 形式',
 '把一下一下往上攀的动作当活动说；放在 plant 前，则说植物靠支撑往上长。',
 'climb + -ing，不双写 b，也不读出 /b/。动作名词、形容词和动词形式取决于句中位置。',C+[['climb + -ing → climbing','攀爬过程、运动；攀缘生长的']],
 'rock climbing 攀岩，go climbing 去攀登，a climbing plant 攀缘植物，climbing prices 不断上升的价格。',
 'rock climbing；go climbing；a climbing plant。',
 'climbing 不是每次都在讲竞技或登山；a climbing rose 是攀缘蔷薇，不是有人正背着玫瑰爬山。',
 ('She took up rock climbing at university.','她在大学开始练攀岩。'),('A climbing plant covered the wall.','一株攀缘植物爬满了墙。'))
R('B3980','抓附着攀爬，及数量、地位的上升','CLIMB：有支点地攀上去，数值也能往上走','climb → climber 人、植物 → climbing 活动、攀缘性质。',
 '把人攀岩、藤爬墙和价格上涨放在一起。climb 的 b 在这些常用形式中都不读，方向却不永远只能向上。',
 'climban → climb；climb + -er/-ing，b 不读。',
 [['基本攀爬、执行者与活动','climb · climber · climbing']],
 'climb down 可以向下；climber 可是植物；social climber 不只是中性努力向上。',
 'The climber watched a climbing rose while climbing the garden steps.\n\n那位攀登者走上花园台阶时，看着一株攀缘蔷薇。','climb climber climbing')
W('mayflower','英 /ˈmeɪflaʊə/；美 /ˈmeɪflaʊər/','五月花〔多种春季开花植物的俗名〕',
 '按五月开花的印象给植物起俗名；地区不同，叫 mayflower 的植物也可能不同，不能只对应一个拉丁学名。',
 'May 五月 + flower 花，普通植物名常连写小写 mayflower。大写 Mayflower 也能是船名或其他专名，那时需按专名上下文理解。',
 [['May + flower → mayflower','以开花季节命名的俗称'],['不同地区与专名使用','可指不同花木；Mayflower 可作船名等']],
 'mayflower blossoms 五月花，the local mayflower 当地俗称五月花的植物；查具体植物时要确认地区、种名。',
 'mayflower blossoms；the local mayflower。',
 'mayflower 俗名不同地区可能不同，Mayflower 大写船名也不是每次都该按一株花译；flower 核心仍是花。',
 ('The guide explained which plant was called mayflower locally.','向导解释了当地把哪一种植物叫作五月花。'),('Mayflower blossoms appeared along the path.','小路边开出了当地称作五月花的花。'))
W('elderflower','英 /ˈeldəflaʊə/；美 /ˈeldərflaʊər/','接骨木花',
 '接骨木开的花，常见于带花香的饮品名称；elder 在这里是树名，不是年长的花。',
 'elder 接骨木 + flower 花。植物 elder 与表示年长者的 elder 是不同来源的同形词，不能借较老的花去讲命名。',
 [['植物 elder 接骨木','与年长者 elder 分来源'],['elder + flower → elderflower','接骨木的花；饮品等香味材料名']],
 'elderflower cordial 接骨木花浓缩饮，elderflower syrup 接骨木花糖浆，elderflower blossoms 接骨木花。',
 'elderflower cordial；elderflower syrup。',
 'elderflower 花和 elderberry 接骨木果是不同部位；同一树上两种材料也不把味道、用途直接当完全相同。',
 ('The café serves elderflower cordial with sparkling water.','咖啡馆把接骨木花浓缩饮兑气泡水供应。'),('The label lists elderflower syrup as an ingredient.','标签把接骨木花糖浆列为一种配料。'))
R('B2679','花和开花；花的环境、季节、植物种类命名','FLOWER：先看花，再看前面限定季节、地点或植物','flower → flowery；May/elder/sun/wild/wall/bell/corn + flower 选不同命名点。',
 '多数复合名能抓直观画面，但植物俗名不保证一名一物。elderflower 的 elder 是接骨木，不是更年长的；wallflower 还可借名形容社交中不显眼的人。',
 '法语 flor 等 → flower；flower + -y；May/elder/sun/wild/wall/bell/corn + flower。',
 [['基本花及样子','flower · flowery'],['季节、种类与环境花名','mayflower · elderflower · sunflower · wildflower · wallflower · bellflower · cornflower']],
 'elderflower/elderberry 花与果；mayflower 地区俗名需辨种；wallflower 的人物比喻别只按花盆猜。',
 'Wildflowers grew beside the elderflower bushes.\n\n接骨木花丛旁长着野花。','flower flowery mayflower elderflower sunflower wildflower wallflower bellflower cornflower')
G=[['古北欧 gervi → 中古英语 gere','装束、装备；准备好的东西'],['英语 gear','装备 → 机械装置、齿轮与挡位；动词准备、调适']]
W('gear','英 /ɡɪə/；美 /ɡɪr/','装备、器具；齿轮、挡位；使适合、准备',
 '先是一套准备办事的家伙什；机械里的传动装置后来也叫 gear。换挡是换传动关系，get into gear 又可说行动进入正轨。',
 '经中古英语借古北欧 gervi 等装备词，和准备好的材料相关。齿轮、挡位义是后来的机械专门化，不是所有 gear 都是有齿的圆轮。',G,
 'camping gear 露营装备，change gear 换挡，gear up for 为……作准备，be geared to 为……设计、适合。equipment 这支 gear 多不可数。',
 'camping gear；change gear；gear up for；be geared to。',
 'gear 装备义常不可数，two gears 多是两只齿轮、两个挡位等；gear up 准备不一定真穿装备。',
 ('We packed our camping gear into the car.','我们把露营装备装进车里。'),('The course is geared to beginners.','课程是为初学者设计的。'))
W('headgear','英 /ˈhedɡɪə/；美 /ˈhedɡɪr/','头部装备、帽盔等头戴物',
 '把 gear 装备的位置限定在头上，安全帽、护头装备、某些专用头戴装置都能归进来。',
 'head 头 + gear 装备，组合通常是集合、不可数类名词。不是头脑里的齿轮，也不只限一顶普通帽子。',G+[['head + gear → headgear','戴于头部的装备或装束']],
 'protective headgear 防护头具，special headgear 专用头戴设备，wear headgear 戴头部装备。',
 'protective headgear；special headgear；wear headgear。',
 'headgear 比 hat 宽，还可包括专门护具、装置；headphones 耳机只是特定音频设备，不是所有 headgear 都能听音乐。',
 ('Workers wore protective headgear at the site.','工人在现场戴着防护头具。'),('The display shows ceremonial headgear from different regions.','展览展示了不同地区的礼仪头饰。'))
R('B3334','准备办事的装备，再到机械传动和适配','GEAR：一套办事家伙什，机器里也有一套传动装置','gear 装备、齿轮、挡位 → headgear 头部装备；gearbox 齿轮箱；switchgear 开关设备。',
 '装备义更宽、更早。不要拿最熟的齿轮去硬解释头盔、露营器材，先看组合选装备还是机械那支。',
 'gervi → gere → gear；head + gear；gear + box；switch + gear。',
 [['装备及头戴物','gear · headgear'],['机械和电气设备','gearbox · switchgear']],
 'gear 装备义通常不可数；headgear 不一定帽子；gear up/be geared to 准备与针对、适配。',
 'The camping gear included protective headgear.\n\n露营装备里包括防护头具。','gear headgear gearbox switchgear')
if __name__=='__main__':save('continuation_20261030_gx',ROOTS,WORDS)
