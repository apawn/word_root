"""Bond, empty, plot and shift: ties, vacancy, plans and changes."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
B=[['古英语绑定、带子词族 → band、bond 等','系住、连接、限制的东西'],['英语关系与承诺引申','感情纽带、化学键；约束付款等义务的文书'],['另一路古北欧居住、农户词族','旧 bond 身份称呼与束缚词发生联想，不把历史全混成一条']]
W('bond','英 /bɒnd/；美 /bɑːnd/','纽带、联系；黏合、结合；化学键；债券、保证文书',
 '像有条看不见的带子把两边连住：胶把材料连住，感情把人连住，文书把承诺和责任连住。',
 '连接、约束义与 band、bind 同一旧词族；债券等是义务受约束文书的专门发展。旧 bond 的农户、役属身份称呼还涉及另一北欧居住词族。',B,
 'a close bond 亲密纽带，bond with a child 和孩子建立亲近关系，a chemical bond 化学键，a government bond 政府债券，bond two surfaces 黏合两面。',
 'a bond between；bond with；a chemical bond；a government bond。',
 'bond 可连接感情、物质或义务，不是所有 bond 都等于“债”；金融债券 bond 与股票 share 也不是同一种所有权名称。',
 ('The shared experience created a strong bond between them.','共同经历在他们之间建立了牢固纽带。'),('The glue bonds the two surfaces together.','胶把两个表面黏合起来。'),
 sources=['https://www.etymonline.com/word/bond','https://en.wiktionary.org/wiki/bond#English'])
W('bondsman','英 /ˈbɒndzmən/；美 /ˈbɑːndzmən/','保证人、担保人；役属男子、男奴〔旧〕',
 '现代文书场景里，是站出来承担保证责任的人；旧故事里却可能是受役属的人，同一个称呼要看历史语境。',
 '担保义可按 bond 保证文书 + 连接 -s- + man 理解；旧役属义与 bondman、bond 的农户到役属身份史相关，不把担保人都讲成奴隶。',B[1:]+[['bond + -s- + man → bondsman〔保证〕','为他人义务提供保证的人；与旧身份义分辨']],
 'a bail bondsman 保释保证人〔某些制度语境〕，act as a bondsman 担任保证人；历史文学里的 bondsman 另可能是受役属者。',
 'a bail bondsman；act as a bondsman；the king’s bondsman〔旧语境〕。',
 'bondsman 是角色称呼，bondholder 是债券持有人；不能看到 bond 就把担保人译成买债券的投资者。',
 ('The novel introduces a bondsman who provides bail for the suspect.','小说介绍了一名为嫌疑人提供保释担保的保证人。'),('The historical passage describes a bondsman working on the estate.','这段历史文字写到一名受役属男子在庄园劳作。'),
 sources=['https://www.etymonline.com/word/bondsman','https://en.wiktionary.org/wiki/bondsman#English'])
R('B4201','像带子系住：人、材料、责任','BOND：连接，也可形成约束','bond 感情、化学、黏合、义务文书；bondsman 担保人与旧身份义分开。',
 '旧农户、役属身份词有另一条居住来源，不把所有义都从绳子捆奴隶一线编出。担保人和债券持有人也不同。',
 '旧绑定词族 → band、bond；关系、文书义扩展；bond + -s- + man → bondsman 保证人；另有旧身份路径。',
 [['连接与约束基础','bond'],['保证人与旧身份词','bondsman']],
 'bond/share 债券与股份；bondsman/bondholder 保证人与债券持有人；连接义与旧役属身份分历史。',
 'The film follows a bondsman whose family bonds are being tested.\n\n电影讲述一位保证人的家庭纽带受到考验的故事。','bond bondsman')
E=[['古英语 ǣmettig、ǣmetta 等','空闲、未占用等词族；也有容器没有东西的旧义'],['中古英语 emty 等 → empty','p 在词形发展中插入，成为现代拼写'],['英语状态与动作','空的；把里面倒空、清空']]
W('empty','/ˈempti/','空的、空着的；空洞的；倒空、清空',
 '杯子里没有饮料、座位上没人，是 empty；承诺里没有真内容，也像一个只剩外壳的空杯子。',
 '继承古英语 ǣmettig 等空闲、未占用词族；中古形式中后来插入 p。现代不能按 em- + pty 拆；动词也承接并取代过旧的倒空形式。',E,
 'an empty bottle 空瓶，an empty seat 空位，empty promises 空头承诺，empty a bag 把包倒空。比较级 emptier、最高级 emptiest 可说相对更空。',
 'an empty seat；empty promises；empty the bin；empty into。',
 'empty 说没有内容，vacant 常说座位、房间、职位空着；名词 emptier 倒空的人或设备较冷门，日常 emptier 常只是比较级。',
 ('The room was completely empty.','房间里完全空了。'),('She emptied the bag onto the table.','她把包里的东西倒到桌上。'),
 sources=['https://www.etymonline.com/word/empty','https://en.wiktionary.org/wiki/empty#English'])
R('B3485','里面没内容、地方没人，或把它变空','EMPTY：看的是空着的状态','empty 状态与清空动作一起学；emptier、emptiest 常见于程度比较。',
 '绝对空和日常“比刚才更空”不矛盾，后者按剩余内容、占用程度来比。empty promises 则说承诺没有实质。',
 'ǣmettig → emty 等 → empty；p 是历史插入；empty 可转动词，y 变 i 对应 emptied、emptier 等。',
 [['基础状态与动作','empty']],
 'empty/vacant 内容空与位置空；emptier 比较级与较冷门倒空者名词辨语境；empty promises 空头承诺。',
 'She emptied the bottle and put the empty bottle aside.\n\n她把瓶子倒空，把空瓶放到一旁。','empty')
ROOTS[-1]['exclude']['emptier']='日常比较级 emptier 已解释；本词条独立名词“倒空者、设备”较冷门，暂不单列。'
P=[['晚期古英语 plot → 英语 plot〔地块〕','有边界的小块土地，更远源未定'],['地面图、图示与计划等扩展','标在图上，安排事件；阴谋义还受 complot 等相近词影响'],['故事事件与直接派生','plot 情节；plotline 情节线；plotter 设计者、绘图设备、密谋者']]
W('plot','英 /plɒt/；美 /plɑːt/','地块；图、图示；情节；密谋；绘制、标点',
 '地块先在图上有位置，计划也能像图一样安排；故事 plot 是事件怎样铺开，秘密 plot 则是暗中安排。不同发展还有词形相互影响。',
 '地块义接晚期古英语 plot，深源不定；地图、计划等义后来发展，密谋义可能受 complot 影响。不把所有 plot 都当成最初有人在菜地谋反。',P,
 'a plot of land 一小块地，the plot of a novel 小说情节，plot the data 绘出数据图，plot against 暗中谋害、谋划对抗。',
 'a plot of land；the plot of a novel；plot the data；plot against。',
 'plot 故事事件组织，theme 主题；plot 图示与 plot 阴谋读音相同，作图本身不带犯罪意思。',
 ('The novel has a complicated plot.','小说的情节很复杂。'),('We plotted the results on a graph.','我们把结果绘在图表上。'),('They bought a small plot of land.','他们买了一小块地。'),
 sources=['https://www.etymonline.com/word/plot','https://en.wiktionary.org/wiki/plot#English'])
W('plotline','英 /ˈplɒtlaɪn/；美 /ˈplɑːtlaɪn/','情节线、故事发展线索',
 '人物和事件一环接一环，好像连出一条线；一部剧也能同时牵着几条人物情节线走。',
 'plot 故事情节 + line 线，借线性延展关系命名，不接 plot 的土地义。',P[1:]+[['plot + line → plotline','故事事件的发展线']],
 'a central plotline 主线情节，a romantic plotline 爱情情节线，an unresolved plotline 尚未交代完的情节线。',
 'a central plotline；a romantic plotline；an unresolved plotline。',
 'plotline 一条事件发展线，subplot 常是相对主线的次要情节；不是每条 plotline 都必然是副线。',
 ('The film follows three connected plotlines.','影片沿着三条相互关联的情节线展开。'),('The final episode resolves the main plotline.','最后一集交代完了主线情节。'))
W('plotter','英 /ˈplɒtə/；美 /ˈplɑːtər/','绘图仪；谋划者、密谋者；按提纲写作的作者',
 'plot 是画图，plotter 就能是画图设备；plot 是密谋，它就能是密谋的人。先挑动词那一义。',
 'plot + -er，双写 t。工具与人物后缀沿不同 plot 用法派生，不能一律译成阴谋家。',P[1:]+[['plot + -er → plotter','作图设备；设计、密谋等主体']],
 'a pen plotter 笔式绘图仪，a group of plotters 一伙密谋者，a novelist who is a plotter 按提纲安排小说的作者。',
 'a pen plotter；a large-format plotter；a group of plotters。',
 'plotter 工具或主体，plotline 故事线；现代大幅面设备叫 plotter 时也未必全是老式机械画笔结构。',
 ('The architect printed the drawing on a large-format plotter.','建筑师用大幅面绘图设备输出了图纸。'),('The story reveals the plotters in the final chapter.','故事到最后一章才揭出密谋者。'))
R('B3877','地块、图示与事件安排，后来分出几路','PLOT：画在图上，或把事情排成线','plot → plotline、subplot 接故事；plotter 可作图也可密谋，依据 plot 所选义分。',
 '现代可以借“安排事件”连接含义，但历史密谋义还受相近词影响，不能把理解图像当成所有义的唯一起源。',
 '旧 plot 地块 → 图示、安排等义；complot 等影响密谋义；plot + line/-er；sub- + plot。',
 [['多义基础','plot'],['故事主次线','plotline · subplot'],['执行主体或工具','plotter']],
 'plot/theme 事件与主题；plotline/subplot 发展线与副情节；plotter 人物工具需选对动词义。',
 'The novelist plotted a new plotline around a secret group of plotters.\n\n小说家围绕一伙秘密密谋者，构思了一条新情节线。','plot plotline subplot plotter')
S=[['古英语 sċiftan → 中古英语 schiften → shift','分配、安排、分开等旧动作'],['英语转移、更换用法','挪位置、换挡、观点变化；轮换工作的一班'],['派生','shifter 换挡等工具；shifty 看似躲闪、不可靠']]
W('shift','/ʃɪft/','移动、转移、改变；换挡；班次；转变',
 '原来重心在这边，稍一挪到了那边；换班则是这一组下去，另一组接上。',
 '继承古英语 sċiftan 的分配、安排等用法，后发展更换、移动。shift 也有衣物名词的旧支线；不能把它当现代 s- + hift。',S,
 'shift your weight 转移身体重心，shift gears 换挡，a night shift 夜班，a shift in attitude 态度转变。',
 'shift gears；shift the focus；a night shift；a shift in。',
 'shift 强调位置、重心、状态换过去，switch 常突出改道或两状态切换，具体搭配有交叉；work a shift 不是工作时搬东西。',
 ('She shifted her weight to the other foot.','她把重心移到另一只脚上。'),('He works the night shift at the hospital.','他在医院上夜班。'),
 sources=['https://www.etymonline.com/word/shift','https://en.wiktionary.org/wiki/shift#English'])
W('shifter','英 /ˈʃɪftə/；美 /ˈʃɪftər/','换挡器、变速控制器；改变、转移的人或物',
 '让挡位从这档换到那档的控制件；更广地也可说执行某种转移、改变的主体。',
 'shift + -er，工具或人物后缀，汽车、自行车中常指换挡杆、控制件，不只指一个负责换班的人。',S[:2]+[['shift + -er → shifter','执行改变的主体；换挡装置']],
 'a gear shifter 换挡器，a bicycle shifter 自行车变速控制器，a paddle shifter 换挡拨片。',
 'a gear shifter；a bicycle shifter；a paddle shifter。',
 'shifter 操纵换挡的部分，gearbox 是变速箱等整套机构；一块拨片不等于完整变速箱。',
 ('The bicycle’s shifter is mounted on the handlebar.','自行车的变速控制器装在车把上。'),('He reached for the gear shifter.','他伸手去摸换挡杆。'))
W('shifty','/ˈʃɪfti/','眼神躲闪的；看着不老实、不可靠的',
 '目光一会儿这边一会儿那边，话也转来转去，让人觉得在躲；词表达的是给人的印象，不等于已经有证据证明违法。',
 'shift 的变化、权宜手段等用法 + -y，早期还可说有办法、会应变，现代常带不可靠的贬义。',S[:2]+[['shift + -y → shifty','善变、躲闪，进而可疑不可靠']],
 'shifty eyes 躲闪眼神，a shifty character 看着不可靠的人，look shifty 显得鬼祟。',
 'shifty eyes；a shifty character；look shifty。',
 'shifty 贬躲闪、不可信，flexible 可正面说灵活；不要把所有容易改变的人都骂成 shifty。',
 ('The villain is described as a shifty character.','反派被描写成一个看着不可靠的人。'),('He gave me a shifty look and changed the subject.','他躲闪地看了我一眼，换了话题。'))
R('B4141','挪过去、换一班，重心和状态改变','SHIFT：从这里转到那里','shift → shifter、shifty；redshift 借光谱向红端移的专门含义。',
 '夜班、换挡、态度转变分别选时间、机械、心理的移动。shifty 则接躲闪、不可靠评价，不等于赞灵活。',
 'sċiftan 分配安排 → shift 移换；shift + -er/-y；red + shift → redshift。',
 [['移换与班次基础','shift'],['操作工具与人物印象','shifter · shifty'],['光谱专门组合','redshift']],
 'shift/switch 搭配有交叉；shifter/gearbox 控制件与变速机构；shifty/flexible 躲闪与灵活。',
 'After his night shift, he shifted his plans and went straight home.\n\n上完夜班后，他改了安排，直接回家。','shift shifter shifty redshift')
if __name__=='__main__':save('continuation_20261030_fo',ROOTS,WORDS)
