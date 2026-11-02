"""Useful objects and growth/fall extensions, without mechanical dictionary copying."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
def S(word,base):
 return ['https://en.wiktionary.org/wiki/'+word+'#English','https://www.etymonline.com/word/'+base]
EXISTING_ROOT_ADDITIONS={
 'A1697':dict(words='tumble tumbler tumblers'.split(),label='tumbler：翻腾者与杯子的旧命名',note='tumble 去 e 加 -er。早指翻腾艺人；杯义原联系圆底或尖底、容易翻倒的杯子，现代 tumbler 不要求仍会翻倒；锁内制动部件又是另一具体用法。'),
 'A2238':dict(words='tumble tumbleweed tumbleweeds'.split(),label='tumbleweed：被风吹得滚动的草团',note='tumble 翻滚 + weed 草构成 tumbleweed；不是所有被风吹动的杂草都这样叫，名称常指干后脱落、随风滚行的植物体。'),
 'C1077':dict(words='plunge plunger plungers plummet plummets plummeted plummeting'.split(),label='plunger 与 plummet：推动部件、皮搋子和急坠',note='plunger 是 plunge 加 -er，从人物名扩展到机构、疏通器具。plummet 原是经法语借来的小铅坠名词，后来转作动词，再有急坠、暴跌义；不能把两个词都当作现代 plunge 换词尾。'),
 'B4313':dict(words='rocket rocketed rocketing skyrocket skyrockets skyrocketed skyrocketing'.split(),label='rocket 与 skyrocket：像火箭般向上冲',note='rocket 火箭由意大利 rocchetto 线轴般形状的命名借入；另有蔬菜 rocket 的独立来源。skyrocket 是 sky 加火箭名词，后来作急升动词，现代用法不保证随后下跌。'),
 'C1583':dict(words='undulate undulates undulated undulating undulation undulations'.split(),label='undulate：像波浪起伏的形状与运动',note='undulate 动词可能由 undulation 逆构，也可能由较早的 undulate 形容词转用；上接拉丁 unda 波、undula 小波等。学习时短词先排，不代表短动词历史一定更早。'),
 'A1699':dict(words='billow billowy'.split(),label='billowy：像大浪般鼓起的性质',note='billow 名词加 -y；窗帘、衣服、云可以呈现波浪般饱满蓬松的形态，不要求此刻正在移动。'),
 'A1740':dict(words='gush gushing gusher gushers'.split(),label='gusher：涌出的来源与自喷油井',note='gush 加人物、事物尾 -er。gusher 写热情话多的人这一记录早于自喷油井；此处放在 gush 比较组，不把 -er 当作 -ly。'),
}
TUMBLER=[['tumble 翻滚 + -er → tumbler','早指表演翻腾的人'],['圆底、尖底易倒的杯子 → 饮用杯名；另用于锁内制动部件','现代杯子可以平底，不必照着旧形状造定义']]
PLUNGER=[['plunge 猛投入、插入 + -er → plunger','早指做动作的人'],['人物、动作名称 → 推杆等部件、疏通管道的器具','看设备区分按压件、柱塞与皮搋子']]
PLUMMET=[['法语小称 plomet ← plom 铅坠 ← 拉丁 plumbum 铅','英语先借名词：小铅坠'],['名词 → 测深动词 → 快速下坠、暴跌','现代动词带急速向下的感觉']]
ROCKET=[['意大利 rocchetto：小线轴，也用于火箭 → 英语 rocket','依据早期圆柱形状命名'],['sky 天空 + rocket 火箭 → skyrocket 名词 → 急升动词','像烟火火箭往高处窜；现代不必伴随跌回去']]
UND=[['拉丁 unda 波 → undula 小波 → undulatus 波浪状','波的材料经相关拉丁形式进入英语'],['undulation 早于英语 undulate 动词','动词可能由名词逆构或由较早形容词转用；之后加现代屈折尾']]
W('tumbler','英 /ˈtʌmblə/；美 /ˈtʌmblɚ/','平底无柄饮用杯；翻腾艺人；锁内制动部件',
 '餐桌上不用杯柄、也没有高脚的水杯，常叫 tumbler。名字里虽有翻滚，现代杯子照样可以稳稳站在桌上。',
 'tumble 去 e 加 -er，早指翻腾艺人；杯义原指底部圆或尖、易翻倒的杯子，之后名称留给这类饮用杯。锁内制动部件另是按具体运动、机构理解的用法。',TUMBLER,
 'a tumbler of water 一杯水；a glass tumbler 玻璃饮用杯；lock tumbler 锁内制动部件。',
 'fill a tumbler；an acrobatic tumbler 翻腾艺人。',
 'tumbler 常是无柄、无高脚杯，mug 常带柄；现代 travel tumbler 可用金属等材料，不能永远只认玻璃材质。',
 ('She poured water into a tall tumbler.','她往一个高饮用杯里倒了水。'),('The tumbler performed a series of flips across the stage.','那位翻腾艺人在舞台上连续翻了几个跟头。'),sources=S('tumbler','tumbler'))
W('tumblers','英 /ˈtʌmbləz/；美 /ˈtʌmblɚz/','饮用杯、翻腾艺人、锁内制动部件〔复数〕',
 '桌上摆着几个无柄水杯，可以说 tumblers；节目里几位翻腾艺人，也可以这么叫。杯子和人各按场景认。',
 'tumbler + -s，读 /z/；内层 tumble 去 e 加 -er。现代复数保留基础词的不同具体义。',TUMBLER+[['tumbler + -s → tumblers','多个杯子、艺人或锁内制动部件']],
 'a set of tumblers 一套饮用杯；acrobats and tumblers 杂技演员与翻腾艺人。',
 'glass tumblers；the tumblers inside a lock。',
 'tumblers 是这一类杯或部件、艺人，tumblings 则偏向翻滚活动的名词形式；不能只按字母多一个 s 就互换。',
 ('Six tumblers were arranged beside the jug.','水壶旁摆着六个饮用杯。'),('The show featured jugglers and tumblers.','表演包括杂耍演员和翻腾艺人。'),sources=S('tumblers','tumbler'))
W('tumbleweeds','/ˈtʌmbəlwiːdz/','风滚草、随风滚行的干草团〔复数〕',
 '荒地上几个干草团被风推着一路滚过去，就是 tumbleweeds。它把“草在翻滚”的画面直接拼进名字。',
 'tumble 翻滚 + weed 草 → tumbleweed，再加复数 -s 读 /z/。常说植物干后脱落、随风滚行的地上部分，不是一种唯一植物的学名。',
 [['tumble + weed → tumbleweed','翻滚的草的组合命名'],['tumbleweed + -s → tumbleweeds','多个随风滚动的干草团']],
 'tumbleweeds blow across the road 风滚草被吹过路面；dry tumbleweeds 干风滚草。',
 'tumbleweeds caught in a fence 卡在篱笆里的风滚草。',
 'tumbleweeds 的重点是会脱落滚行的草团；weeds 泛说不想让它长在那里的杂草，不必会滚。',
 ('Tumbleweeds rolled across the empty road.','风滚草滚过空旷的公路。'),('Dry tumbleweeds had gathered against the fence.','干风滚草堆积在篱笆边。'),sources=S('tumbleweeds','tumbleweed'))
W('plunger','英 /ˈplʌndʒə/；美 /ˈplʌndʒɚ/','皮搋子、管道疏通器；柱塞、推杆等部件',
 '握着长柄，把橡胶碗口压在排水口上推拉，那件工具叫 plunger；咖啡壶、针筒里推下去的部件，也可用这个词。',
 'plunge 去 e 加 -er，早指执行动作的人，后来用于推压机构、疏通工具。-er 可以指物，不能一见它就翻成某某人。',PLUNGER,
 'a toilet plunger 马桶皮搋子；press the plunger 按下柱塞、推杆。',
 'the plunger of a syringe 针筒活塞；a coffee press plunger 压滤咖啡壶的压杆。',
 'plunger 是工具或内部推动部件，plumber 是做管道工作的工人；两词较远同接铅材料，现代工作角色却不同。',
 ('He used a plunger to clear the blocked sink.','他用皮搋子疏通堵住的水槽。'),('Press the plunger down slowly to separate the coffee grounds.','慢慢压下压杆，把咖啡渣隔开。'),sources=S('plunger','plunger'))
W('plungers','英 /ˈplʌndʒəz/；美 /ˈplʌndʒɚz/','皮搋子、柱塞、推杆〔复数〕',
 '店里卖的几个皮搋子，或几套装置里可推压的部件，都能叫 plungers；要靠周围的设备名称判断是哪一种。',
 'plunger + -s，读 /z/；内层 plunge 去 e 加 -er，人物尾后来也用于执行相关动作的器具、机构。',PLUNGER+[['plunger + -s → plungers','多个疏通器具或推动部件']],
 'rubber plungers 橡胶皮搋子；syringe plungers 针筒活塞。',
 'replacement plungers 替换柱塞；different sizes of plungers。',
 'plungers 是可推压的部件或工具，handles 只泛说供手握的柄；一个装置里可能两者都有。',
 ('The shop sells plungers in several sizes.','这家店卖几种尺寸的皮搋子。'),('The syringe plungers moved smoothly inside the barrels.','针筒活塞在筒身里推动得很顺畅。'),sources=S('plungers','plunger'))
W('plummets','/ˈplʌmɪts/','骤降、急坠〔第三人称单数〕；铅坠〔复数〕',
 '看图表时，线条一下往下栽，可以说 it plummets。这里借的是重坠直落的感觉，程度比普通下降强。',
 'plummet + -s，/t/ 后读 /s/；这个词先有小铅坠名词，再转动词，不能把内部 -et 拆成现代下跌动作的时态尾。',PLUMMET+[['plummet + -s → plummets','它急坠、骤降；多个铅坠']],
 'temperature plummets 气温骤降；confidence plummets 信心骤减。',
 'plummets after sunset 日落后骤降；plummets to a low 跌至低点。',
 'plummets 表示很快地向下，decreases 只是减少；不由词本身规定下降百分比。',
 ('The temperature plummets after sunset.','日落后气温骤降。'),('His confidence plummets whenever someone laughs at his mistakes.','每当有人嘲笑他的错误，他的信心就骤减。'),sources=S('plummets','plummet'))
W('plummeted','/ˈplʌmɪtɪd/','急坠、骤降了',
 '销量前一周还很高，突然掉下去，叫 sales plummeted；它把下降说成一记明显的急落。',
 'plummet + 完整 -ed，/t/ 后读 /ɪd/，多出音节。词重音在前，现代通常不双写末尾 t。',PLUMMET+[['plummet + -ed → plummeted','过去急坠、暴跌，-ed 在 /t/ 后读 /ɪd/']],
 'sales plummeted 销量骤降；plummeted to the ground 急坠落地。',
 'plummeted overnight；plummeted from one level to another。',
 'plummeted 比 fell 更突出下降的急速、明显；数字已经跌落不等于之后必定反弹。',
 ('Ticket sales plummeted after the tour was postponed.','巡演延期后，票的销量骤降。'),('The damaged drone plummeted to the ground.','受损的无人机急坠落地。'),sources=S('plummeted','plummet'))
W('plummeting','/ˈplʌmɪtɪŋ/','正在急坠、骤降的',
 '价格曲线正在急速往下走，是 plummeting prices。它说的是跌落过程，比单说价格低多了一层变化。',
 'plummet + -ing；词重音在前，通常不双写末尾 t。名词小铅坠转动词后，再形成这些常用形式。',PLUMMET+[['plummet + -ing → plummeting','正在急速下坠或减少']],
 'plummeting temperatures 骤降的气温；plummeting sales 急跌的销量。',
 'send prices plummeting 使价格猛跌；a plummeting object 急坠物体。',
 'plummeting prices 是价格正在急跌，low prices 是水平低；价格可以从很高处急跌后仍不便宜。',
 ('Plummeting temperatures forced the climbers to turn back.','气温骤降，迫使登山者返回。'),('The new competitor sent prices plummeting.','新竞争者的出现让价格猛跌。'),sources=S('plummeting','plummet'))
W('skyrockets','英 /ˈskaɪrɒkɪts/；美 /ˈskaɪrɑkɪts/','猛增、飞涨〔第三人称单数〕；冲天烟火〔复数〕',
 '需求、成本一下蹿上去，像冲天烟火一样，就是 skyrockets。名词也确实可以说一枚枚冲上天的烟火。',
 'skyrocket + -s，/t/ 后读 /s/；内层 sky + rocket。先有烟火名词，后有猛涨动词，今天写上涨不保证接着跌落。',ROCKET+[['skyrocket + -s → skyrockets','它飞涨；多枚冲天烟火']],
 'demand skyrockets 需求猛增；the cost skyrockets 费用飞涨。',
 'skyrockets during the holidays；colourful skyrockets。',
 'skyrockets 用语气突出上涨猛，rises 更中性；不能推成 skyrocket 必须是航天器发射。',
 ('Demand for hotel rooms skyrockets during the festival.','节庆期间，酒店房间的需求猛增。'),('Colourful skyrockets lit up the night.','五彩冲天烟火照亮了夜空。'),sources=S('skyrockets','skyrocket'))
W('skyrocketed','英 /ˈskaɪrɒkɪtɪd/；美 /ˈskaɪrɑkɪtɪd/','猛增、飞涨了',
 '原来没多少人看，视频发出后浏览量一下蹿高，就能说 views skyrocketed；语气让人感到涨得又快又猛。',
 'skyrocket + 完整 -ed，/t/ 后读 /ɪd/；不是 sky 单独发生时态变化。',ROCKET+[['skyrocket + -ed → skyrocketed','过去发生明显、快速上涨']],
 'views skyrocketed 浏览量猛增；costs skyrocketed 费用飞涨。',
 'skyrocketed after the announcement；skyrocketed to a new high。',
 'skyrocketed 和 plummeted 方向相反，都比普通 rose、fell 更有急剧变化的感觉；不是专门的统计阈值术语。',
 ('Sales skyrocketed after the video went viral.','视频广泛传播后，销量猛增。'),('The price of the rare book skyrocketed at the auction.','那本珍本书的价格在拍卖会上飙升。'),sources=S('skyrocketed','skyrocket'))
W('skyrocketing','英 /ˈskaɪrɒkɪtɪŋ/；美 /ˈskaɪrɑkɪtɪŋ/','正在猛增、飞涨的',
 '工资还没变，房租却往上猛蹿，skyrocketing rents 把这种压力写得很直观；它说的是增长速度和势头。',
 'skyrocket + -ing；内层保留 sky、rocket 的合成。现代动作形式可直接修饰费用、需求等。',ROCKET+[['skyrocket + -ing → skyrocketing','正在飞涨的过程、性质']],
 'skyrocketing rents 飞涨的租金；skyrocketing demand 猛增的需求。',
 'skyrocketing costs；skyrocketing popularity 人气猛增。',
 'skyrocketing costs 突出费用猛涨，expensive 只评价贵；贵的东西可能近期根本没涨价。',
 ('Skyrocketing rents have made it harder to live near the station.','租金飞涨，让住在车站附近变得更困难。'),('The factory expanded to meet skyrocketing demand.','工厂扩大了规模，以满足猛增的需求。'),sources=S('skyrocketing','skyrocket'))
W('rocketed','英 /ˈrɒkɪtɪd/；美 /ˈrɑkɪtɪd/','迅速冲去、窜升了；使迅速升高了',
 '球猛地蹿进球门，或价格一下上冲，过去发生了都能用 rocketed。它借火箭的速度，不要求物体真装火箭。',
 'rocket 动词 + 完整 -ed，/t/ 后读 /ɪd/。动词由火箭名词发展；火箭名词上接意大利线轴形状命名，与蔬菜 rocket 分开。',ROCKET+[['rocket + -ed → rocketed','过去像火箭般冲去或迅速上升']],
 'rocketed into the net 猛射入网；prices rocketed 价格猛涨。',
 'rocketed past 从旁边飞快冲过；rocketed to fame 迅速成名。',
 'rocketed 可以写水平方向的飞冲，skyrocketed 作比喻时更常突出向上猛涨；别把所有 rocket 动词都限成垂直升空。',
 ('The ball rocketed into the back of the net.','球猛地射进球门。'),('Travel costs rocketed during the holiday period.','假期里出行费用猛涨。'),sources=S('rocketed','rocket'))
W('rocketing','英 /ˈrɒkɪtɪŋ/；美 /ˈrɑkɪtɪŋ/','正在飞冲、猛涨的',
 '车从眼前飞快冲过，或费用一节节急升，rocketing 把速度写得像火箭。既能说移动，也能修饰正在上涨的数量。',
 'rocket + -ing；现代动词由火箭名词转用。内部 rocket 不应因为也有 rock 石头，就硬拆成石头加小尾。',ROCKET+[['rocket + -ing → rocketing','飞快移动或急速上升的过程']],
 'rocketing prices 猛涨的价格；rocketing past 飞快冲过。',
 'rocketing demand；sent the ball rocketing 使球飞射出去。',
 'rocketing prices 写价格急涨，rising prices 可只是缓慢上行；速度感、强调程度不同。',
 ('Rocketing energy costs affected every household.','能源费用猛涨，影响了每一户人家。'),('The car came rocketing past us.','那辆车从我们身边飞驰而过。'),sources=S('rocketing','rocket'))
W('undulates','英 /ˈʌndjʊleɪts/；美 /ˈʌndʒəleɪts/','像波浪起伏〔第三人称单数〕',
 '一条路顺着低矮山丘缓缓上上下下，像波形线，就是 undulates。物体不一定在动，形状本身也可以起伏。',
 'undulate 动词 + -s，/t/ 后读 /s/；动词可能从 undulation 逆构或由较早形容词转用，远接 unda 波及小波材料。',UND+[['undulate + -s → undulates','它呈波浪状或作波浪式运动']],
 'the road undulates 道路起伏；fabric undulates 布料呈波浪般摆动。',
 'undulates gently 轻缓起伏；undulates through the hills。',
 'undulates 可以写静态地形的高低变化，waves 作动词常写挥动、摆动；“波浪”只是帮助理解的共同画面。',
 ('The road undulates through low hills.','道路顺着低矮的山丘上下起伏。'),('The fabric undulates gently in the breeze.','布料在微风中轻轻起伏。'),sources=S('undulates','undulate'))
W('undulated','英 /ˈʌndjʊleɪtɪd/；美 /ˈʌndʒəleɪtɪd/','呈波浪状起伏了',
 '麦田被风推过，一片高一片低地连续起伏，用 undulated 比只说 moved 更能看到那种波浪形。',
 'undulate 去 e 加完整 -ed，词干 /t/ 后读 /ɪd/；过去式、过去分词，不把 -lated 当成一个独立后缀。',UND+[['undulate + -ed → undulated','过去像波浪起伏或呈波浪状']],
 'undulated in the wind 在风中起伏；the land undulated 地面绵延起伏。',
 'undulated across the field；a surface that undulated。',
 'undulated 突出连续的波形起伏，shook 只说摇动、震动；后者未必是一峰一谷依次变化。',
 ('The wheat undulated in the wind.','麦子在风里呈波浪般起伏。'),('The land undulated gently beyond the village.','村庄外的地面绵延着缓缓起伏。'),sources=S('undulated','undulate'))
W('undulating','英 /ˈʌndjʊleɪtɪŋ/；美 /ˈʌndʒəleɪtɪŋ/','波浪般起伏的、绵延起伏的',
 '远处一丘接一丘，线条没有突然断开，而是平缓地高低相接，就是 undulating hills。蛇身移动、布料摆动也可呈现这种连续起伏。',
 'undulate 去 e 加 -ing；动作形式作修饰时，可写运动中的波形，也可写固定地形。',UND+[['undulate + -ing → undulating','波浪式运动的过程或形态']],
 'undulating hills 起伏丘陵；undulating movement 波浪式运动。',
 'undulating countryside 绵延起伏的乡野；an undulating line 起伏曲线。',
 'undulating hills 常突出平缓连绵的高低线条，steep hills 突出坡陡；不是所有山丘都给同一种感觉。',
 ('We cycled through undulating countryside.','我们骑车穿过绵延起伏的乡野。'),('The dancer moved her arms in an undulating motion.','舞者用双臂做出连续的波浪式动作。'),sources=S('undulating','undulate'))
W('undulations','英 /ˌʌndjʊˈleɪʃənz/；美 /ˌʌndʒəˈleɪʃənz/','一连串起伏、波浪形变化',
 '看地面的一道道高低，或布面的一层层波形，把这些起伏拿出来数、描述，就可以用 undulations。',
 'undulation + -s，读 /z/；名词上接拉丁波、小波、波浪状材料，比英语 undulate 动词记录更早，不能只说英语动词临时加 -ion 的历史。',UND+[['undulation + -s → undulations','多道波形起伏、多次波浪式变化']],
 'gentle undulations 平缓起伏；undulations in the surface 表面的起伏。',
 'the undulations of the landscape；small undulations。',
 'undulations 常强调连续波形；bumps 更像一个个凸起、颠簸点，两种地形感受不同。',
 ('The map shows the gentle undulations of the landscape.','地图显示了地形的缓缓起伏。'),('Light revealed small undulations in the fabric.','光线照出了布面细小的波形起伏。'),sources=S('undulations','undulation'))
W('billowy','英 /ˈbɪləʊi/；美 /ˈbɪloʊi/','大浪般鼓起、翻卷的；蓬松宽大的',
 '白云一团团鼓起，宽裙摆像浪一样蓬开，都可以用 billowy。重点在饱满、波浪般的形态，东西此刻可以静止。',
 'billow 大浪名词 + -y；比起 billowing 正在翻涌，这个形容词更容易直接说呈大浪般形态的性质。',
 [['古诺斯大浪材料 → 英语 billow 名词','大浪、翻卷物'],['billow + -y → billowy','像大浪般鼓起、蓬松宽大的性质']],
 'billowy clouds 团团鼓起的云；a billowy skirt 蓬松宽大的裙子。',
 'billowy sleeves 宽大蓬起的袖子；billowy fabric。',
 'billowy 描述蓬开、浪状的形态，baggy 常说衣服宽松肥大；同件衣服可以两者都适用，但画面不同。',
 ('Billowy clouds filled the afternoon sky.','一团团鼓起的云布满午后的天空。'),('She wore a billowy white blouse.','她穿着一件宽大蓬松的白衬衫。'),sources=S('billowy','billowy'))
W('gusher','英 /ˈɡʌʃə/；美 /ˈɡʌʃɚ/','自喷油井；大量涌出的来源；热情说个不停的人',
 '油不靠泵抽就能从井里涌出来，这种井叫 gusher；形容人时，则像赞美、热情的话一开口就往外冒。',
 'gush 涌出 + -er。热情话多的人这一义记录早于自喷油井义，所以不能把人物义全部说成由油井比喻而来。',
 [['gush + -er → gusher','做出涌出、热情倾诉动作的人或事物'],['热情话多人已有较早记录，后有自喷油井义','不同对象都联系大量涌出的画面']],
 'strike a gusher 打出自喷油井；a gusher of praise 赞美大量涌出的来源。',
 'an oil gusher 自喷油井；a real gusher 热情话特别多的人。',
 'gusher 是涌出的源头或做动作的人，gush 可以说一次涌出；不能把 an oil gusher 只译成一股油。',
 ('The drilling crew struck a gusher.','钻井队打出了一口自喷油井。'),('He is a real gusher when he talks about his grandchildren.','一说起孙辈，他就热情洋溢地讲个不停。'),sources=S('gusher','gusher'))
W('gushers','英 /ˈɡʌʃəz/；美 /ˈɡʌʃɚz/','自喷油井、涌出来源、热情话多的人〔复数〕',
 '纪录片里几口油井自己喷涌，便是 gushers；把人这样称呼时，重在情感、赞美像泉水一样涌出来。',
 'gusher + -s，读 /z/；内层 gush + -er 指人或物，复数并不改变这些不同具体用法。',
 [['gush + -er → gusher','涌出的源头、热情倾诉者'],['gusher + -s → gushers','多个自喷油井等来源，或多位热情话多者']],
 'oil gushers 自喷油井；early gushers 早期自喷井。',
 'famous gushers；wells that became gushers。',
 'gushers 不是所有油井的通称；oil wells 范围更广，是否能自行喷流要另外看。',
 ('The documentary shows early oil gushers in Texas.','纪录片展示了得克萨斯早期的自喷油井。'),('The history book describes several famous gushers.','那本历史书描述了几口著名的自喷油井。'),sources=S('gushers','gusher'))
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_zgy',ROOTS,WORDS)
 extend_lessons()
