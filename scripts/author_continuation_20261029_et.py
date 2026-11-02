"""Cup, send and heavy: common concrete families."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
C=[['古英语 cuppe、copp → 中古英语 cuppe → cup','饮用容器；部分接晚期拉丁 cuppa'],['现代 cup','杯；杯形物、杯量；双手拢成杯形']]
W('cup','/kʌp/','杯子；一杯的量；杯赛、奖杯；双手拢起',
 '装饮料的杯是基本物件；一杯的量、杯状奖品和双手合拢的形状都能跟它连接。',
 '现代形式合流古英语 cuppe、copp 等，部分接晚期拉丁 cuppa，更远来历不全确定。现代不能只因杯子中空就硬拆一个 c- 前缀。',C,
 'a cup of tea 一杯茶，two cups of flour 两杯面粉，cup your hands 双手拢成杯形；World Cup 世界杯。测量用 cup 具体容量随体系而异。',
 'a cup of；a measuring cup；cup your hands；win the cup。',
 'cup of tea 字面一杯茶，not my cup of tea 比喻不是我的喜好；glass 常指玻璃杯但日常容器分类不绝对。',
 ('Would you like a cup of tea?','你想喝杯茶吗？'),('She cupped her hands around the tiny bird.','她把双手拢起来护着那只小鸟。'))
W('teacup','/ˈtiːkʌp/','茶杯',
 '用来喝茶的小杯子，名称说用途，不要求每次里面都装茶。',
 'tea 茶 + cup 杯，直接构成器物名。复合前部不加复数 teas。',C+[['tea + cup → teacup','喝茶用的杯 → 茶杯']],
 'a china teacup 瓷茶杯，a teacup and saucer 茶杯与茶碟；a storm in a teacup 小题大做的风波。',
 'a china teacup；a teacup and saucer；a storm in a teacup。',
 'teacup 物件，a cup of tea 装着茶的一杯饮料；空茶杯依然是 teacup。',
 ('She placed the teacup on its saucer.','她把茶杯放在茶碟上。'),('The shelf holds a collection of old teacups.','架子上摆着一组老茶杯收藏。'))
W('cupcake','/ˈkʌpkeɪk/','纸杯蛋糕；小杯状蛋糕',
 '一人一份的小蛋糕，形状和烤制容器都能让人想到小杯子。',
 'cup + cake，历史涉及杯中烘烤或以杯计量的蛋糕名称，现代通常指独立小蛋糕，不必把所有命名细节定成唯一来源。',C+[['cup + cake → cupcake','杯相关蛋糕名称 → 一份小蛋糕']],
 'a chocolate cupcake 巧克力纸杯蛋糕，decorate cupcakes 装饰小蛋糕。',
 'a chocolate cupcake；a tray of cupcakes；decorate cupcakes。',
 'cupcake 与 muffin 松饼在现代烘焙风格、配方和装饰上有常见差别，但不是靠有没有纸托就能绝对判断。',
 ('The bakery made cupcakes for the party.','面包店为派对做了纸杯蛋糕。'),('Each cupcake had a little flower on top.','每个小蛋糕顶上都有一朵小花。'))
W('buttercup','英 /ˈbʌtəkʌp/；美 /ˈbʌtərkʌp/','毛茛；金黄杯状花的植物俗称',
 '黄色像黄油，花瓣围成小杯形，两个具体外观放在一起帮助记花名。',
 'butter 黄油 + cup 杯，黄油色的花与杯状花形参与命名。不是杯子里装黄油，也不是所有黄色花都叫 buttercup。',C+[['butter + cup → buttercup','黄油色、杯状花的植物名']],
 'yellow buttercups 黄色毛茛花，a field of buttercups 一片毛茛；日常植物名不用于判断是否可食。',
 'yellow buttercups；a field of buttercups；buttercups in the grass。',
 'buttercup 植物名，a cup of butter 一杯黄油；一个复合词与一个数量短语是两回事。',
 ('Buttercups dotted the grass beside the path.','小路旁草地上点缀着毛茛花。'),('The children drew bright yellow buttercups.','孩子们画了明黄色毛茛花。'))
R('B3528','杯、杯形与小蛋糕、花名','CUP：器物、容量和形状三条直观路','cup 后接 teacup 器物、cupcake 蛋糕和 buttercup 花名，不靠颜色花形推食用性。',
 '古英语相关容器词合流，部分接晚期拉丁。现代杯量依测量体系而异，不能一个数替代全部地区食谱。',
 'cup → teacup、cupcake、buttercup；cup hands 动词按杯形。',
 [['杯与相关器物','cup · teacup'],['蛋糕与植物名','cupcake · buttercup']],
 'teacup 杯与 cup of tea 饮料不同；buttercup 花与 cup of butter 数量短语不同。',
 'She put down her teacup and chose a cupcake.\n\n她放下茶杯，选了一只纸杯蛋糕。',
 'cup teacup cupcake buttercup')
SE=[['古英语 sendan → 中古英语 senden → send','使前去、派送'],['现代 send','寄送人、物、消息；使进入某状态']]
W('send','/send/','发送；寄出；派遣；使进入某状态',
 '让人、物或消息从这里到那里；也能让某人进入睡眠、恐慌等状态。',
 '继承古英语 sendan，使前去、派送。现代不规则变化 send—sent—sent，不能写 sended。',SE,
 'send a message 发消息，send someone a letter 寄信，send for a doctor 派人请医生；send someone to sleep 使某人入睡。',
 'send a message；send something to；send for；send someone to sleep。',
 'send 发送不等于 receive 收到，发出去不自动说明收件人已读；send for 请人来与 send away 让人走也有方向差别。',
 ('Please send me the address.','请把地址发给我。'),('The long lecture nearly sent me to sleep.','漫长的讲座差点让我睡着。'))
W('sender','英 /ˈsendə/；美 /ˈsendər/','发送者；寄件人',
 '从谁那里发出来，就称谁 sender，可以是人、公司或系统。',
 'send + -er，执行发出动作的主体。不是只限纸信，也可用于消息、包裹等。',SE+[['send + -er → sender','发出者 → 发送者、寄件人']],
 'the sender’s address 寄件人地址，an unknown sender 未知发件人；return to sender 退回寄件人。',
 'the sender’s address；an unknown sender；return to sender。',
 'sender 发送方，receiver、recipient 接收方；同一人在不同消息里可以分别担任两端。',
 ('The envelope did not show the sender’s address.','信封上没有寄件人地址。'),('Check the sender before replying to the message.','回复消息前先核对发件人。'))
W('resend','/ˌriːˈsend/','重新发送；再次寄送',
 '原来发过，再发一次，常因为没收到、漏附件或需要提醒。',
 're- 再 + send，过去式、分词 resent /ˌriːˈsent/。与 resent 怨恨同形，但重音、来源和意思不同。',SE+[['re- + send → resend','再次发送；分词 resent']],
 'resend the email 重发邮件，resend the attachment 重发附件。',
 'resend an email；resend the attachment；resend the link。',
 'I resent the email /ˌriːˈsent/ 是重新发了邮件；I resent the criticism /rɪˈzent/ 是反感批评，不能只看拼写。',
 ('Could you resend the attachment, please?','能请你重新发送附件吗？'),('I resent the email to the correct address.','我把邮件重新发到了正确地址。'))
R('B2495','发送、发件人与重发','SEND：让人、物、消息前去','send → sender 主体、resend 再次动作，godsend 已有精讲共享。',
 '古英语使前去的动词，send—sent—sent；resend 的分词 resent 与怨恨动词同形不同读。',
 'send → sender；re- + send → resend；god + send → godsend。',
 [['基本动作、主体与重复','send · sender · resend'],['已有帮助比喻','godsend']],
 '发送不等于收到；resent 重发与 resent 怨恨分音义；send 不写 sended。',
 'The sender resent the missing attachment.\n\n发件人重发了漏掉的附件。',
 'send sender resend godsend')
HE=[['古英语 hefig → 中古英语 hevy → heavy','重；严肃、负担大等义也很早'],['现代 heavy','物重 → 量大、强烈、难负担；深沉等语境义']]
W('heavy','/ˈhevi/','重的；大量、强烈的；繁重的',
 '箱子压手是重，雨大、交通多、工作负担大，也像有很大的分量。',
 '继承古英语 hefig，关联 heave 举起词族；不把整个词说成今天才从 heave 改字母造出来。',HE,
 'a heavy bag 重包，heavy rain 大雨，heavy traffic 交通繁忙，a heavy workload 工作繁重。',
 'a heavy bag；heavy rain；heavy traffic；a heavy workload。',
 'heavy rain 大雨不用强行译 heavy 为重；strong wind 大风通常用 strong，不是所有大的自然现象都套 heavy。',
 ('The bag is too heavy for me to carry.','包太重了，我提不动。'),('Heavy traffic delayed the bus.','交通繁忙让公交车晚点了。'))
W('heavily','/ˈhevɪli/','大量地；严重地；重重地；很大程度上',
 '修饰动作、程度：雨下得大，受损严重，或很依赖某件事。',
 'heavy + -ly，y 改 i，成为 heavily；不是直接照抄 heavyly。不同搭配接 heavy 的强度、重量等义。',HE+[['heavy + -ly → heavily','程度大、重量大 → 大量地、严重地']],
 'rain heavily 下大雨，rely heavily on 高度依赖，heavily damaged 严重受损。',
 'rain heavily；rely heavily on；heavily damaged。',
 'heavy rain 名词前用形容词，rain heavily 动词后用副词；heavily 也不只说 physically 重。',
 ('It rained heavily throughout the night.','整夜都在下大雨。'),('The village relies heavily on tourism.','村庄高度依赖旅游业。'))
W('heaviness','/ˈhevinəs/','沉重；沉闷、沉重感',
 '把重的感觉单独提出来，可以是物品、身体部位或心情。',
 'heavy + -ness，y 改 i，成为 heaviness。抽象情绪义从沉重负担的感觉延伸。',HE+[['heavy + -ness → heaviness','重的性质、感觉 → 沉重感']],
 'the heaviness of the bag 包的沉重，a heaviness in the atmosphere 气氛的沉闷。',
 'a feeling of heaviness；the heaviness of；emotional heaviness。',
 'heaviness 是感觉或性质，weight 更可具体测量重量；某物体积大也不必重。',
 ('The heaviness of the curtains made the room feel formal.','厚重窗帘让房间显得庄重。'),('A heaviness settled over the room after the news.','消息传来后，房间气氛沉重起来。'))
W('heavyweight','/ˈheviweɪt/','重量级选手；重量级的；重要人物',
 '比赛中是按体重分级的一档；其他领域则借来说有大影响力的人或机构。',
 'heavy 重 + weight 重量，形成重量级名称，再比喻实力、地位重要。具体体重界限随运动、组织而变。',HE+[['heavy + weight → heavyweight','高体重级别 → 重量级、重要人物']],
 'a heavyweight boxer 重量级拳击手，a political heavyweight 政界重量级人物。',
 'a heavyweight boxer；a political heavyweight；an industry heavyweight。',
 'heavyweight industry figure 说影响大，不是评论该人物胖；lightweight 在对应领域也可作相反比喻。',
 ('She interviewed a political heavyweight.','她采访了一位政界重量级人物。'),('The heavyweight final was the last match of the evening.','重量级决赛是当晚最后一场比赛。'))
R('B3092','重量、强度与沉重负担','HEAVY：分量大，再问是物重、量多还是负担重','heavy → heavily 方式程度、heaviness 状态，再看 heavyweight 比赛级别与影响力比喻。',
 '古英语继承词，抽象负担、严肃义也古老，不把所有比喻都标成新英语发明。',
 'heavy → heavily、heaviness；heavy + weight → heavyweight。',
 [['性质、方式与状态','heavy · heavily · heaviness'],['体重级别与影响力','heavyweight']],
 'heavy rain 与 rain heavily 对照；strong wind 的搭配另记；heavyweight 可说影响大而非体重。',
 'Heavy rain fell throughout the night.\n\n大雨下了一整夜。',
 'heavy heavily heaviness heavyweight')
if __name__=='__main__':save('continuation_20261029_et',ROOTS,WORDS)
