"""Bread, pitch and chest: basic objects and several non-obvious histories."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
B=[['古英语 brēad → 中古英语 bred → bread','碎块、食物；面包'],['英语 bread','面包 → 生计、钱；也可作动词裹面包屑']]
W('bread','/bred/','面包；生计、钱〔比喻、俚语〕；裹面包屑',
 '最基本的主食拿来代表吃饭、生计：挣钱养家不是只买面包。做菜时 bread 作动词，还能说给食物裹面包屑。',
 '古英语 brēad 经中古英语延续，早期有碎块等义；更远与发酵还是掰碎材料相连，有不同解释，不硬定为 break 的现代派生。',B,
 'a slice of bread 一片面包，a loaf of bread 一条面包，earn your bread 谋生，bread the fish 给鱼裹面包屑。',
 'a slice of bread；a loaf of bread；earn your bread；bread the fish。',
 '普通 bread 多不可数，买两个面包通常说 two loaves 或具体品名；breads 也可在种类语境出现，不是永远不能加 s。',
 ('She cut three slices of bread.','她切了三片面包。'),('He breaded the fish before cooking it.','他烹鱼之前给鱼裹了面包屑。'))
W('breadcrumb','/ˈbredkrʌm/','面包屑；路径导航中的层级链接、线索',
 '一小碎屑落在路上，连成一串就像回头找路的记号；网页里的面包屑导航也把你所在的层级一路标出来。',
 'bread + crumb，crumb 里的 b 不发音。计算和线索比喻常借《韩塞尔与葛蕾特》撒面包屑找路的故事。',B+[['bread + crumb → breadcrumb','面包小碎屑'],['故事画面 → 界面、线索比喻','一串标记帮助知道路径或追踪']],
 'breadcrumbs 面包屑常用复数，breadcrumb navigation 面包屑导航，leave breadcrumbs 留下可追踪线索。',
 'breadcrumbs；breadcrumb navigation；leave breadcrumbs。',
 'breadcrumbs 导航通常表当前所在的层级路径，不一定是浏览器真实访问历史；crumb 和 crumble 碎裂相近但不是同一词形。',
 ('Sprinkle breadcrumbs over the dish.','在菜上撒些面包屑。'),('The breadcrumbs show that this page is inside the help section.','面包屑导航显示，这一页位于帮助栏目之内。'))
W('breadwinner','英 /ˈbredwɪnə/；美 /ˈbredwɪnər/','家庭主要收入来源者、养家的人',
 '把一家人的饭挣回来；winner 在这里抓的是挣得、取得，不是赢了一场吃面包比赛。',
 'bread 生计 + winner，后者来自 win 挣得、取得 + -er。组合通常指家庭主要经济支柱，性别不限定。',B+[['bread + winner → breadwinner','挣得生计的人 → 家庭主要挣钱者']],
 'the main breadwinner 主要养家人，the sole breadwinner 唯一经济来源者，two breadwinners 两名共同挣钱者。',
 'the main breadwinner；the sole breadwinner；a family’s breadwinner。',
 'breadwinner 是家庭收入角色，不是工作头衔，也不专指父亲；homemaker 常说操持家庭者，两种角色可以由同一人兼任。',
 ('She became the family’s main breadwinner.','她成了家里的主要经济支柱。'),('Both parents are breadwinners in this household.','这个家庭的父母双方都挣钱养家。'))
W('breadboard','英 /ˈbredbɔːd/；美 /ˈbredbɔːrd/','切面包板；电路实验面包板',
 '厨房里是一块切面包的板；电子实验里则是先把元件接起来试的底板，现代常见的是带连接孔的免焊板。',
 'bread + board 的器具名先指切面包板，后来进入试装电路的技术用法。板子不必仍是木头，更不能只因为像吐司就断定所有技术词源细节。',B[:1]+[['bread + board → breadboard','切面包的板'],['电子实验用法','临时搭建、测试电路的实验平台']],
 'a wooden breadboard 木制面包板，a solderless breadboard 免焊面包板，build a circuit on a breadboard 在实验板上搭电路。',
 'a wooden breadboard；a solderless breadboard；build a circuit on a breadboard。',
 'breadboard 实验搭接平台，printed circuit board 印制电路板是另一种结构；厨房板和电子板靠上下文辨。',
 ('She sliced the loaf on a wooden breadboard.','她在木制面包板上切面包。'),('The students tested the circuit on a solderless breadboard.','学生们在免焊面包板上测试电路。'))
W('gingerbread','英 /ˈdʒɪndʒəbred/；美 /ˈdʒɪndʒərbred/','姜饼、姜味糕点；繁复花饰〔比喻〕',
 '今天想姜味糕点，节日里还能拼成小人、小屋；但这个词最初是蜜饯姜一类名称，尾巴后来才被听成 bread。',
 '经古法语 ginginbrat 等接中世纪拉丁姜制品词，英语早形 gingerbrar 等后来受 bread 影响改造。现代可以按 ginger + bread 认形，历史却不是从头就这样直接拼。',
 [['古法语 ginginbrat 等 → 中古英语早形','蜜饯姜、姜制品'],['民间词源改造为 gingerbread','尾部被理解成 bread'],['英语词义发展','姜味糕点；花哨装饰']],
 'a gingerbread house 姜饼屋，a gingerbread man 姜饼人，gingerbread trim 建筑繁复花饰。食品形态有软糕、饼干等地区差异。',
 'a gingerbread house；a gingerbread man；gingerbread trim。',
 'gingerbread 不必是切片吐司式面包；bread 的现代形状不能倒推这个词最早就等于姜加面包。',
 ('The children decorated a gingerbread house.','孩子们装饰了一座姜饼屋。'),('The old house has elaborate gingerbread trim.','老房子上有繁复的花饰。'),sources=['https://www.etymonline.com/word/gingerbread'])
R('B2946','面包、碎屑和以饭代表生计；旧词的重新分析','BREAD：一口主食能代表整份生计','bread → breadcrumb、breadboard；breadwinner 挣饭钱的人；gingerbread 的 bread 是历史重分析，不只现代直拼。',
 '食物名称、用品、生活比喻放在一起。技术里的面包板和导航里的面包屑都有具体画面，姜饼却要特别说明旧词怎样改形。',
 'brēad → bread；bread + crumb/board/winner/basket；short/flat + bread；gingerbread 受 bread 影响改造。',
 [['基本食物与碎屑','bread · breadcrumb'],['挣钱与器具','breadwinner · breadboard · breadbasket'],['糕点、饼形与旧词改造','shortbread · flatbread · gingerbread']],
 'bread 常不可数，loaf/slice 计量；breadwinner 不限性别；gingerbread 不能只讲现代表面拆分。',
 'The breadwinner brought bread and gingerbread home.\n\n家里主要挣钱的人带回了面包和姜饼。','bread breadcrumb breadwinner breadboard breadbasket shortbread flatbread gingerbread')
W('pitch','/pɪtʃ/','投、投球；搭帐篷；推介；音高；球场；沥青状物',
 '先分几幅画：投出去的球、钉立起来的帐篷、向人推过去的方案；音高是在高低轴上定位。黑黏的 pitch 则另有老来源。',
 '投、钉立等义接中古英语 picchen；搭帐篷与钉牢、立起有关，后有投掷、推介等扩展。音高常与高度、程度支联系，但细节不全明。黑黏材料义经古英语 piċ 接拉丁 pix，另分一支。',
 [['中古英语 picchen → pitch','钉入、固定、立起 → 搭建、投掷'],['高度、投掷等扩展','音高、俯仰、推介等；各义联系部分不明'],['另一来源：拉丁 pix → 古英语 piċ → pitch','黑黏的沥青状、焦油状材料']],
 'pitch a tent 搭帐篷，pitch an idea 推介想法，a sales pitch 推销说辞，a football pitch 足球场，high pitch 高音。',
 'pitch a tent；pitch an idea；a sales pitch；a football pitch；high pitch。',
 'pitch 音高与 volume 音量不同：小声也可唱高音。pitch 黑黏材料和投球义不要编成同一字面动作。',
 ('We pitched our tent beside the lake.','我们在湖边搭起了帐篷。'),('She pitched the idea to the editor in two minutes.','她用两分钟向编辑推介了这个想法。'),sources=['https://www.etymonline.com/word/pitch'])
W('pitcher','英 /ˈpɪtʃə/；美 /ˈpɪtʃər/','投手；大水壶、带把倒水容器〔另源〕',
 '球场上是把球投向击球手的人；餐桌上可能是装水的壶。壶不会投球，这两个义不是一个 -er 人物规则包办。',
 '投手是 pitch 投球 + -er。水壶接中古英语 picher、古法语 pichier，再到更早容器名称，与 beaker 有历史关系；现代碰巧同形。',
 [['pitch + -er → pitcher','投球的人'],['古法语 pichier → 中古英语 picher → pitcher','带把、有倒水口的容器']],
 'a baseball pitcher 棒球投手，a pitcher of water 一壶水，a glass pitcher 玻璃水壶；pitcher plant 猪笼草等壶状捕虫植物按外形命名。',
 'a baseball pitcher；a pitcher of water；a glass pitcher；a pitcher plant。',
 'pitcher 投手和壶分来源；picture /ˈpɪktʃər/ 图片多一个 /k/，拼写也不同。',
 ('The pitcher threw the ball toward the batter.','投手把球投向击球手。'),('A pitcher of water stood in the middle of the table.','桌子中央放着一壶水。'))
R('B3214','投掷、钉立、推介等多义；另有黑黏材料和容器同形词','PITCH：多幅画分开看，不把所有意思硬塞一个动作','pitch 投球 → pitcher 投手；pitcher 水壶另源；pitchfork 叉起投放的农具；音高不等于音量。',
 '这个词尤其适合分支学习。能解释的中间环节讲清，历史不明处保留，不用万能的扔把球场、沥青、水壶全部串成故事。',
 'picchen → pitch；pitch + -er/fork；pix → piċ → 材料 pitch；pichier → 容器 pitcher。',
 [['基本多义词与投手','pitch · pitcher'],['农具组合','pitchfork']],
 'pitch/volume 音高与音量；pitcher 投手和容器不同来路；pitcher/picture 注意 /k/。',
 'The pitcher drank from a pitcher of water after pitching.\n\n投球后，投手倒了一壶里的水来喝。','pitch pitcher pitchfork')
C=[['希腊 kistē → 拉丁 cista → 古英语 ċest/ċist','箱子、篮、储物容器'],['中古英语 chest → 英语胸部义','箱子 → 肋骨包住内部器官的胸腔、胸部']]
W('chest','/tʃest/','胸部、胸膛；箱子；抽屉柜〔固定搭配〕',
 '一只箱子把东西装在里面；肋骨围着心肺，也像人体的一只保护箱。这个箱到胸的历史，比只背两个中文义直观。',
 '古英语 ċest、ċist 接较早借入的拉丁 cista，后接希腊容器词。胸部义是后来按箱式包裹结构扩展，不是 chestnut 栗子中的 chest 再拆开。',C,
 'a wooden chest 木箱，a treasure chest 宝箱，chest muscles 胸部肌肉，a chest of drawers 抽屉柜；get something off your chest 把憋着的话说出来。',
 'a treasure chest；a chest of drawers；chest muscles；get it off your chest。',
 'chest 胸部或容器；breast 可有胸、乳房等用法，不能见中文胸就无差别替换；chestnut 的前段是旧栗子名，不是胸。',
 ('They found an old chest in the attic.','他们在阁楼里发现了一个旧箱子。'),('He held the book against his chest.','他把书抱在胸前。'),sources=['https://www.etymonline.com/word/chest'])
W('chested','/ˈtʃestɪd/','有某种胸部特征的〔通常接在描述词后〕',
 'broad-chested 就是胸膛宽阔；这里 -ed 说长着怎样的胸，不是在过去做了一个胸的动作。',
 'chest 胸部 + -ed 具有……的，通常前面还有 broad、flat 等说明特征，组成修饰语。',C+[['chest + -ed → chested','具有某种胸部形态的']],
 'broad-chested 胸膛宽阔的，flat-chested 胸部平坦的。chested 单独作描述较少，连着前面的特征一起理解最实用。',
 'broad-chested；flat-chested；a broad-chested athlete。',
 'chested 的 -ed 表具有，不必有过去时间；chest 作运动动作动词也能有过去式，但句子结构会不同。',
 ('A broad-chested athlete stood beside the door.','一位胸膛宽阔的运动员站在门边。'),('The costume made him look broad-chested.','这套服装让他看起来胸膛宽阔。'))
W('chesty','/ˈtʃesti/','胸部有痰的〔咳嗽等〕；胸部丰满的；自负的〔部分口语〕',
 '先看搭配：chesty cough 听起来从胸里带着痰；描述体形则突出胸部。另有挺着胸、自我膨胀般的自负用法。',
 'chest + -y，带胸部特点的形容词；不同搭配分别发展出身体症状、体形、态度义，不能用一个丰满包办。',C+[['chest + -y → chesty','胸部突出的或涉及胸部的；再有态度用法']],
 'a chesty cough 带痰的咳嗽，a chesty voice 胸腔感较重的嗓音；人物体形、态度用法按语域判断。',
 'a chesty cough；a chesty voice。',
 'chesty cough 常与 dry cough 干咳对照，是语言用法区别；chesty 不等于一般胸部的标准形容词，chest 作定语也很常见。',
 ('He spoke with a deep, chesty voice.','他说话嗓音低沉，胸腔共鸣很重。'),('The character’s chesty cough interrupts every conversation.','这个人物每次说话都被一阵带痰的咳嗽打断。'))
R('B3521','箱子与胸部；胸部形态、声音等特征','CHEST：箱子装东西，肋骨像箱子包住器官','chest 箱、胸 → chested 具有某种胸部 → chesty 接具体搭配。',
 '箱子到胸部有真实的历史比喻。两个形容词也要看用法：chested 多跟在体形描述后，chesty 可以描述咳嗽、声音。',
 'kistē → cista → ċest → chest；chest + -ed/-y；chest of drawers 固定组合。',
 [['箱与胸的基本词','chest'],['形态与相关特征','chested · chesty']],
 'chest/chestnut 不能按现代字母误拆；chested -ed 表具有；chesty cough 不是胸部丰满。',
 'The broad-chested actor spoke in a deep, chesty voice.\n\n胸膛宽阔的演员用低沉、胸腔共鸣重的声音说话。','chest chested chesty')
if __name__=='__main__':save('continuation_20261030_gm',ROOTS,WORDS)
