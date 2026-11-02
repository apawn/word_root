"""Piece, wall and risk: portions, barriers and uncertain outcomes."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
P=[['晚期拉丁 pecia、petia → 法语 piece → 中古英语 pece → piece','碎块、一部分；更远来源不确定'],['现代 piece','一份、一件；作品、器具部件；拼接']]
def PH(f,m):return P+[[f,m]]
W('piece','/piːs/','一块、一片；一件作品、物品；拼接',
 '把整体分出一部分是 piece；音乐、文章、艺术作品也能按一件成品来数。',
 '经法语接晚期拉丁部分、碎片词，更远可能的凯尔特语联系不作定论。与 peace 和平同音，来源不同。',P,
 'a piece of cake 一块蛋糕，也可比喻小菜一碟；a piece of advice 一条建议，piece together 拼凑信息。',
 'a piece of；a piece of music；piece together；in one piece。',
 'piece 可帮助数 advice、information 等不可数名词；不是说这些信息真能像饼干一样掰开。',
 ('Could I have a piece of cake?','我能吃一块蛋糕吗？'),('The team pieced together the story from old letters.','团队从旧信里拼出了故事的经过。'))
W('masterpiece','英 /ˈmɑːstəpiːs/；美 /ˈmæstərpiːs/','杰作；代表作',
 '最初是证明自己达到大师、师傅水平的作品，后来是水准非常高、令人称道的作品。',
 'master 大师、行会师傅 + piece 作品，仿荷兰语或德语相应大师作品词而成。不是主人的一小块身体。',PH('master + piece → masterpiece','证明大师水平的作品 → 杰作'),
 'a literary masterpiece 文学杰作，a masterpiece of design 设计杰作。',
 'a literary masterpiece；a masterpiece of design；an early masterpiece。',
 'masterpiece 强评价作品水准，bestseller 说畅销；卖得多与艺术杰作不是同一个维度。',
 ('The painting is widely regarded as a masterpiece.','这幅画被广泛视为杰作。'),('The bridge is a masterpiece of engineering.','这座桥是一项工程杰作。'))
W('mouthpiece','/ˈmaʊθpiːs/','吹嘴、口含部件；传声筒、代言者',
 '器物中靠嘴使用的那一块是 mouthpiece；人替某机构发声，也可像传话部件一样被这样称呼。',
 'mouth 嘴 + piece 部件，器物义包括乐器吹嘴等，后有组织发言工具、传声筒的比喻。',PH('mouth + piece → mouthpiece','与嘴接触的部件 → 替人发声者'),
 'a trumpet mouthpiece 小号吹嘴，a mouthpiece for a party 某党派传声筒；人物义常带缺乏独立性的评价。',
 'a trumpet mouthpiece；a mouthpiece for；a political mouthpiece。',
 'mouthpiece 可负面说只替人传话，spokesperson 发言人更常是中性职务；不能一律互换语气。',
 ('The musician cleaned the trumpet mouthpiece.','乐手清洁了小号吹嘴。'),('Critics called the newspaper a mouthpiece for the party.','批评者称报纸是该党派的传声筒。'))
W('earpiece','英 /ˈɪəpiːs/；美 /ˈɪrpiːs/','耳机部件；耳塞式接收器',
 '声音要送到耳朵，就把贴耳、入耳的那部分装置叫 earpiece；不是耳朵切下来的一片。',
 'ear 耳 + piece 部件，按器物贴耳用途组合。可指一侧耳机，也可是一整个小接收器。',PH('ear + piece → earpiece','耳部用的器件 → 耳机、接收器'),
 'a wireless earpiece 无线耳机，wear an earpiece 戴耳机接收器。',
 'a wireless earpiece；wear an earpiece；adjust an earpiece。',
 'earpiece 常聚焦贴耳部件，headset 通常说戴头上的整套耳机、麦克风装置；具体产品有交叠。',
 ('The presenter heard instructions through an earpiece.','主持人通过耳机听取指示。'),('She adjusted the earpiece before going onstage.','她上台前调整了耳机。'))
W('mantelpiece','英 /ˈmæntəlpiːs/；美 /ˈmæntəlpiːs/','壁炉架；壁炉周围装饰结构',
 '壁炉开口上方和周围的装饰框、架子，家居描写里常放钟、相框。',
 'mantel 壁炉罩、架 + piece，成词指整个壁炉装饰结构，日常也常特指顶部架面。',PH('mantel + piece → mantelpiece','壁炉装饰部件 → 壁炉架'),
 'on the mantelpiece 在壁炉架上，a stone mantelpiece 石壁炉架。',
 'on the mantelpiece；a stone mantelpiece；a mantelpiece clock。',
 'mantel 壁炉架与 mantle 披风、地幔等是相关但不同现代词形；不是 mental 精神的 + piece。',
 ('A family photograph stood on the mantelpiece.','壁炉架上摆着一张全家福。'),('The old room has an ornate stone mantelpiece.','老房间里有一座装饰华丽的石壁炉架。'))
W('altarpiece','英 /ˈɔːltəpiːs/；美 /ˈɔːltərpiːs/','祭坛画；祭坛装饰作品',
 '摆在祭坛上或后面的宗教绘画、雕塑等装饰作品，重点是它的场所和用途。',
 'altar 祭坛 + piece 作品，形成艺术品类别名，不只限定一种绘画材料。',PH('altar + piece → altarpiece','祭坛上的作品 → 祭坛画、装饰艺术'),
 'a painted altarpiece 祭坛画，a carved altarpiece 雕刻祭坛装饰。',
 'a painted altarpiece；a carved altarpiece；restore an altarpiece。',
 'altarpiece 接祭坛 altar，不是 alter 改变后的碎片；博物馆里展出的作品也可保留原用途名。',
 ('The museum restored a wooden altarpiece.','博物馆修复了一件木制祭坛装饰。'),('The chapel’s altarpiece depicts a religious scene.','礼拜堂的祭坛画描绘了一个宗教场景。'))
W('piecemeal','/ˈpiːsmiːl/','零碎地；逐个、逐步地；零敲碎打的',
 '不是一次做成完整整体，而是一块块处理；有时中性说分批，有时批评缺乏统筹。',
 'piece + 历史 -meal 每次、逐次，接古英语 mǣlum 等时间、度量形式。不是现代 meal 一顿饭的普通组合。',PH('piece + -meal → piecemeal','每次一块 → 逐块、零碎'),
 'a piecemeal approach 零碎处理方式，introduced piecemeal 分批引入。可作形容词、副词。',
 'a piecemeal approach；piecemeal changes；introduce piecemeal。',
 'piecemeal 可批评无整体计划，但分批实施不自动不好；stepwise 常更强调有序步骤。',
 ('The changes were introduced piecemeal over several years.','改动在几年内分批引入。'),('The report criticizes the piecemeal approach to the problem.','报告批评了对问题零敲碎打的处理方式。'))
W('piecewise','/ˈpiːswaɪz/','分段的；按部分分别地',
 '把整体切成几段，每段用自己的规则处理；数学里的分段函数是最典型例子。',
 'piece 部分 + -wise 按某方式，形成技术形容词、副词；不是每一块都很聪明。',PH('piece + -wise → piecewise','按部分分别 → 分段的'),
 'a piecewise function 分段函数，piecewise linear 分段线性的。',
 'a piecewise function；piecewise linear；defined piecewise。',
 'piecewise 技术上分段描述，不带 piecemeal 缺乏统筹的常见批评语气。',
 ('The curve is represented by a piecewise linear model.','曲线用一个分段线性模型表示。'),('The function is defined piecewise on three intervals.','函数在三个区间上分段定义。'))
R('B2759','一份、一件作品与部件','PIECE：整体的一部分，也能数成一件作品','piece 基本量词后读 masterpiece 杰作，再将 mouthpiece、earpiece、mantelpiece、altarpiece 按用途归组，最后对照 piecemeal、piecewise。',
 '经法语接部分、碎块词，更远来历不确定。-meal 是历史逐次成分，不能只看现代饭的常用义。',
 'piece → masterpiece、mouthpiece、earpiece、mantelpiece、altarpiece；piece + -meal、-wise；已有部件、作品词共享。',
 [['基本部分与作品','piece · masterpiece · workpiece · showpiece · centrepiece'],['身体、器具与艺术部件','mouthpiece · earpiece · eyepiece · headpiece · hairpiece · timepiece · mantelpiece · altarpiece'],['按块与按段','piecemeal · piecewise']],
 'piece 与 peace 同音；mouthpiece 可有负面传声筒义；piecemeal 零碎、piecewise 分段技术描述。',
 'The curator pieced together the history of the masterpiece.\n\n策展人拼出了这件杰作的历史。',
 'piece masterpiece workpiece showpiece centrepiece mouthpiece earpiece eyepiece headpiece hairpiece timepiece mantelpiece altarpiece piecemeal piecewise')
WA=[['拉丁 vallum 防御墙 → 日耳曼借词 → 古英语 weall → wall','墙、防御土垒'],['现代 wall','隔开空间的墙 → 障碍、阻挡信息与交流的比喻']]
W('wall','英 /wɔːl/；美 /wɔːl/','墙；隔障；用墙围住',
 '把空间隔开，既能承托、保护，也能挡住通行；交流中的障碍同样会像一堵墙。',
 '继承古英语 weall，较早借入拉丁 vallum 防御工事词，现代室内外墙义扩展。少见沸腾同形词不混进墙的来历。',WA,
 'a brick wall 砖墙，a garden wall 园墙，a wall of silence 一片不肯开口的沉默；wall off an area 围开一片区域。',
 'a brick wall；a wall of silence；wall off；hit a wall。',
 'wall 墙与 fence 栅栏有功能重合但结构常不同；hit a wall 可比喻遇到瓶颈，不一定撞伤。',
 ('They hung the map on the wall.','他们把地图挂在墙上。'),('The investigation met a wall of silence.','调查遭遇了一片不肯开口的沉默。'))
W('stonewall','英 /ˈstəʊnwɔːl/；美 /ˈstoʊnwɔːl/','石墙；阻挠、拒绝提供信息',
 '石墙挡在那里推不动，某人反复不答、拖着不给信息，也像在你面前竖了一堵墙。',
 'stone 石 + wall，实体石墙的组合很早；现代动词借坚硬障碍表示拖延、阻挠。',WA+[['stone + wall → stonewall','石墙 → 以不合作阻挠']],
 'stonewall an inquiry 阻挠调查，stonewall reporters 对记者拒不开口；动词重在态度和过程。',
 'stonewall an inquiry；stonewall reporters；continue to stonewall。',
 'stonewall 不只是慎重思考、暂时不知道，通常评价有意不合作；实体石墙也常分写 stone wall。',
 ('The officials were accused of stonewalling the inquiry.','官员被指阻挠调查。'),('She said the company had stonewalled her requests for information.','她说公司对她索取信息的请求一直推托。'))
W('drywall','英 /ˈdraɪwɔːl/；美 /ˈdraɪwɔːl/','干式墙板；石膏板墙面',
 '用预制板材拼装墙面，区别于现场大量湿抹的方式；不是所有干燥墙壁都叫 drywall。',
 'dry 干式 + wall 墙，按施工方式、材料形成类别名。现代常指纸面石膏板及相应墙面系统。',WA+[['dry + wall → drywall','干式墙面工法 → 墙板、石膏板墙']],
 'install drywall 安装石膏板墙，a drywall panel 墙板，drywall repair 修补板墙。',
 'install drywall；a drywall panel；drywall repair。',
 'drywall 是通用材料、墙面类别，Sheetrock 是相关品牌名；不是字面不潮的任意石墙。',
 ('The builders installed drywall in the new rooms.','工人在新房间安装了石膏板墙。'),('The leak damaged a section of drywall.','漏水损坏了一片石膏板墙面。'))
W('wallflower','英 /ˈwɔːlflaʊə/；美 /ˈwɔːlflaʊər/','桂竹香等花名；聚会中被冷落、拘谨的人',
 '花可以在墙边生长；舞会里靠墙站着、不参与的人，也被比喻成墙边的花。',
 'wall + flower，植物名之后有人物比喻。具体植物名不泛指墙边所有花，人物义也不指外貌像植物。',WA+[['wall + flower → wallflower','墙边植物名 → 聚会旁观、被冷落的人']],
 'a shy wallflower 害羞的旁观者，be a wallflower at a party 聚会中靠边、很少参与。',
 'a shy wallflower；a wallflower at a party；yellow wallflowers。',
 'wallflower 人物义可以带同情、玩笑，并不等于天生不爱交际的人都被排斥；看现场参与情况。',
 ('She used to be a wallflower at school dances.','她以前在学校舞会上常是站在一旁的人。'),('Yellow wallflowers grew beside the old wall.','旧墙旁长着黄色桂竹香。'))
R('B2493','墙面、障碍与靠边站的人','WALL：把空间隔开，也能把信息挡住','wall 后接 stonewall 不合作的障碍、drywall 工法和 wallflower 靠墙者；已有 firewall、paywall、seawall 等共享。',
 '墙词接古英语与更早拉丁防御工事借词。现代复合词可技术类别或行为比喻，不能只按空间物理墙解释。',
 'wall → stonewall、drywall、wallflower；wall + paper；fire/pay/sea/side + wall。',
 [['基本墙与工法','wall · stonewall · drywall'],['人物与已有复合词','wallflower · wallpaper · firewall · paywall · seawall · sidewall']],
 'stonewall 动词可拒绝合作；drywall 非任意干墙；wallflower 人物义看聚会情境。',
 'The company stonewalled questions about the damaged wall.\n\n公司对受损墙壁的问题拒不答复。',
 'wall stonewall drywall wallflower wallpaper firewall paywall seawall sidewall')
RI=[['意大利语 risco、rischio → 法语 risque → risk','危险、冒险；更远词源存在争论'],['现代 risk','坏结果的可能性；使暴露于这种可能']]
W('risk','/rɪsk/','风险；冒险；使面临损失可能',
 '坏事还没一定发生，但存在可能；risk 动词就是把人、物、结果放到这个可能里。',
 '经法语接意大利语危险、冒险词。更远有航海礁石、切割等不同解释，不能把一条有趣故事写成已确定来源。',RI,
 'a risk of delay 延误风险，take a risk 冒险，risk losing 冒着失去的风险，at risk 面临危险。',
 'a risk of；at risk；take a risk；risk doing。',
 'risk 是可能性，不等于已发生的 damage 损害；risk doing 接动名词，不按 want to do 套成 risk to lose。',
 ('There is a risk of delay if the weather worsens.','天气变坏的话，有延误风险。'),('We cannot risk losing the only copy.','我们不能冒险丢失唯一副本。'))
W('risky','/ˈrɪski/','有风险的；冒险的',
 '这件事有较明显的坏结果可能，需要考虑能否承担，而不是一见这个词就认定必败。',
 'risk + -y，表示具有风险的形容词，保留 sk 后加 y。',RI+[['risk + -y → risky','有风险的']],
 'a risky plan 冒险计划，a risky shortcut 有风险的捷径；too risky 风险过高。',
 'a risky plan；a risky shortcut；too risky。',
 'risky 有失败可能，impossible 不可能成功；riskier 比较级也不代表能从词本身算出概率。',
 ('Crossing the river at night would be risky.','夜间过河会有风险。'),('They rejected the plan because it was too risky.','他们因计划风险过高而否决了它。'))
R('B3338','坏结果的可能与承担风险','RISK：还没发生，但可能损失','risk 名词、动词后接 risky 形容词，强调可能性而非已成事实。',
 '借法语接意大利语风险词，更深历史不定。保留确定借入路线，不用礁石故事替代不确定性。',
 'risk → risky；take a risk、risk doing 为常用搭配。',
 [['基本风险与性质','risk · risky']],
 'risk doing 不机械套 to do；risky 不等于 impossible；at risk 不是已经受损。',
 'Taking a risky shortcut could put the whole project at risk.\n\n走一条冒险捷径，可能让整个项目面临风险。',
 'risk risky')
if __name__=='__main__':save('continuation_20261030_i',ROOTS,WORDS)
