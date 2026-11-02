"""Tape, cart and battery: strips, transport, grouped force and false splits."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
T=[['古英语 tæppa/tæppe → 中古英语 tape','狭长的带子、带状材料'],['英语 tape','胶带、磁带；用胶带粘、录音录像']]
W('tape','/teɪp/','带子、胶带、磁带；用胶带粘；录音录像',
 '一条长而窄的柔性材料：一面有胶能粘，覆磁性材料能记录，带刻度又能量长度。先抓带状，再选用途。',
 '接古英语 tæppa 等带子词，具体更早来源不清。胶带、录制介质都是旧带状物名称的新用途，tape 作动词跟着相应器物义走。',T,
 'adhesive tape 胶带，magnetic tape 磁带，a tape measure 卷尺，tape the box shut 用胶带封箱；tape a show 录节目。',
 'adhesive tape；magnetic tape；a tape measure；tape the box shut。',
 'tape 不都带胶，也不都装在盒里；record 录制不限定磁带，现代 tape 作录制动词有时仍保留旧名称。',
 ('She taped the box shut.','她用胶带把箱子封好。'),('He found an old tape of the concert.','他找到了那场音乐会的一盒旧录音带。'))
W('mixtape','/ˈmɪksteɪp/','自选混录曲集；以混音带名义发行的音乐作品',
 '把喜欢的歌按自己的顺序录到一盘带上，送人或传听；后来即使只发数字文件，也能沿用 mixtape 这个名字。',
 'mix 混合、选编 + tape 磁带，早期也写 mix tape。音乐文化中的用法后来扩展，不要求有实体磁带，也不总是多位歌手的精选。',T+[['mix + tape → mixtape','自制、选编的磁带曲集'],['数字和音乐发行扩展','仍叫 mixtape 的歌单、音乐项目']],
 'make a mixtape 做一份混录曲集，release a mixtape 发行一张 mixtape，a digital mixtape 数字混音曲集。',
 'make a mixtape；release a mixtape；a digital mixtape。',
 'mixtape 可是歌单式汇编，也可是艺人自己的音乐项目；album 专辑与它的边界依发行传统，不用有没有磁带作唯一判断。',
 ('He made a mixtape of songs from their road trip.','他把公路旅行时听的歌做成了一份混录曲集。'),('The artist released the mixtape online.','这位音乐人在网上发布了这张 mixtape。'))
W('tapeworm','英 /ˈteɪpwɜːm/；美 /ˈteɪpwɜːrm/','绦虫',
 '身体扁长、像一条带子而得名的一类寄生虫；tape 描外形，不是吞了录音磁带。',
 'tape 带状物 + worm 虫，按形态形成动物名。worm 在这种名称里比日常蚯蚓范围宽。',T+[['tape + worm → tapeworm','像带子一样扁长的寄生虫']],
 'a tapeworm 绦虫，tapeworm segments 绦虫节片，the life cycle of a tapeworm 绦虫生活史。',
 'a tapeworm；tapeworm segments；the life cycle of a tapeworm。',
 'tapeworm 与 earthworm 蚯蚓是不同动物；名称中的 worm 只是宽泛虫类材料，不保证生物分类相同。',
 ('The diagram shows the segments of a tapeworm.','图示出了绦虫的节片。'),('The students compared a tapeworm with an earthworm.','学生们比较了绦虫和蚯蚓。'))
W('taper','英 /ˈteɪpə/；美 /ˈteɪpər/','逐渐变细、减少；细蜡烛；锥度',
 '一支细长蜡烛，或火焰向上收成尖头；把这种慢慢收拢的轮廓搬到雨声、数量上，就成逐渐减弱。',
 '常用渐细义接古英语 tapor 蜡烛、灯芯等旧词，具体更早来源不确定，不是 tape + -er。另有 tape + -er 指录制者，但不拿罕见人物义替常用渐细义作词源。',
 [['古英语 tapor → taper','蜡烛、灯芯，后尤指细蜡烛'],['形状比喻与动词','向尖端收拢 → 逐渐变细、减少']],
 'taper toward the end 向末端渐细，taper off 逐渐减弱、停止，tapered legs 渐细的桌椅腿。',
 'taper toward the end；taper off；tapered legs。',
 'taper 强调逐渐收小，cut 可突然截断；taper off 不等于已经完全停止，只看当前逐渐减弱过程。',
 ('The chair legs taper toward the floor.','椅子腿越靠近地面越细。'),('The rain tapered off during the afternoon.','下午雨逐渐小了下来。'),sources=['https://www.etymonline.com/word/taper'])
R('B3567','狭长带状物及胶粘、记录；taper 常用义另源','TAPE：同一条带，能粘、能量、也能记录','tape → mixtape、videotape、audiotape；tapeworm 取带状外形；taper 渐细义另走蜡烛、火焰形状线。',
 '把用途和形态分开，扩展就好懂。尤其 taper 的拼写看似 tape 加 r，最常用的渐细义却不是录制者。',
 'tæppa → tape；mix/video/audio + tape；tape + worm；古英语 tapor 蜡烛旧词 → taper，与 tape 另分来路。',
 [['基本带状材料及录制','tape · mixtape · videotape · audiotape'],['动物外形','tapeworm'],['同形分路：渐细','taper']],
 'tape 不都粘，也不都录音；mixtape 可数字发布；taper 渐细不是 tape + -er 的普通人物义。',
 'The tape marks where the wooden pole begins to taper.\n\n胶带标出了木杆开始逐渐变细的位置。','tape mixtape videotape audiotape tapeworm taper')
C=[['古北欧 kartr 与古英语 cræt 等合流','载物车、推拉车'],['中古英语 cart → cart','载物车 → 用车运、费力搬运']]
W('cart','英 /kɑːt/；美 /kɑːrt/','推拉载物车、购物车；用车运、搬运',
 '把重东西装上轮子，推或拉着走；网上购物车也借装待购物品的容器画面。动词还能带费力搬来搬去的感觉。',
 '中古英语 cart 与古北欧 kartr、本族古英语 cræt 等车名有合流关系。游戏卡带的 cart 则可由 cartridge 截短，不把那个义当车。',C,
 'a shopping cart 购物车，a handcart 手推车，cart goods away 把货运走，cart boxes upstairs 把箱子费力搬上楼。',
 'a shopping cart；cart away；cart boxes upstairs。',
 'cart 主要是推拉、载物等车名，car 常说汽车；一个 online shopping cart 可以是界面，不是实体车辆。',
 ('She pushed the shopping cart toward the checkout.','她把购物车推向收银台。'),('We had to cart the boxes up three flights of stairs.','我们得把箱子费力搬上三层楼梯。'))
W('carter','英 /ˈkɑːtə/；美 /ˈkɑːrtər/','赶货车的人、车运工〔传统职业〕',
 '过去用牲口拉车运货，赶着车、把货运到的人就是 carter；今天也常在姓氏、历史材料里遇到。',
 'cart + -er；中古英语相应形式还与盎格鲁法语赶车人名称合流。职业名后来也成为 Carter 这样的姓氏，姓氏不能倒过来证明某人的现职。',C+[['cart + -er 等对应形式 → carter','驾货车运输的人；再用于姓氏']],
 'a carter delivering coal 运煤车夫，work as a carter 当车运工；历史运输画面中较常见。',
 'work as a carter；a carter delivering coal。',
 'carter 历史货车工，不等于任何汽车司机；cartographer 制图师来自地图材料，不能按 carter 加长拆。',
 ('The carter delivered coal to the village.','车夫把煤运到了村里。'),('His grandfather had worked as a carter before the railway arrived.','铁路通来前，他祖父曾当过车运工。'))
W('carting','英 /ˈkɑːtɪŋ/；美 /ˈkɑːrtɪŋ/','用车运输；搬运；cart 的 -ing 形式',
 '一趟趟把东西装走、搬走；比起简单 carry，carting 常让人感到货多、路远或搬运麻烦。',
 'cart + -ing，动词形式和动作名词。它不是 karting 卡丁车运动；两者有时同音，拼写与活动不同。',C+[['cart + -ing → carting','运输货物这一过程；正在搬运']],
 'carting boxes around 把箱子搬来搬去，the cost of carting 运输费用，carting goods to market 运货赶集。',
 'carting boxes around；the cost of carting；carting goods。',
 'carting 搬货、运输，karting 常指驾驶卡丁车运动。别因为读音相同就把搬货车当赛车。',
 ('I spent the morning carting boxes around the office.','我一上午都在办公室里搬来搬去地挪箱子。'),('The price includes the cost of carting the materials to the site.','价格包含把材料运到现场的费用。'))
W('pushcart','英 /ˈpʊʃkɑːt/；美 /ˈpʊʃkɑːrt/','手推车、流动售货推车',
 '人站后面推，货在前面跟轮子走；街头卖水果、搬小批货的车都能有这个画面。',
 'push 推 + cart 载物车，按推动方式命名。不要求每辆车都有完全相同轮数或用途。',C+[['push + cart → pushcart','靠人推动的小载物车']],
 'a fruit seller’s pushcart 水果摊推车，push a pushcart 推手推车，a street vendor’s pushcart 街头商贩推车。',
 'a fruit seller’s pushcart；a street vendor’s pushcart。',
 'pushcart 按手推方式、载物用途命名，wheelbarrow 常是独轮手推斗车；具体轮子和车斗结构看实物。',
 ('The vendor sold fruit from a pushcart.','小贩推着手推车卖水果。'),('They loaded the books onto a small pushcart.','他们把书装上了一辆小手推车。'))
R('B3520','载物车与搬运；人物、过程、推动方式','CART：把货放上轮子，再推拉运走','cart → carter 运货人 → carting 运输过程；pushcart 按推动方式命名；cartwheel 车轮与侧手翻比喻。',
 '基本名词、动作、职业按一条运输线排。常用电子购物车是借名，carting 和卡丁车 karting 的拼写也要分清。',
 'kartr/cræt → cart；cart + -er/-ing/wheel；push + cart。',
 [['基本车、搬运动作和职业','cart · carter · carting'],['具体器物与外形比喻','pushcart · cartwheel']],
 'cart/car 载物推拉车与汽车常用名；carting/karting 搬运与卡丁车运动；Carter 姓氏不保证现职。',
 'The carter was carting boxes from a pushcart into the shop.\n\n运货工正在把箱子从手推车上搬进店里。','cart carter carting pushcart cartwheel')
W('battery','英 /ˈbætəri/；美 /ˈbætəri/','电池、电池组；炮组、炮兵连；一系列；殴打〔法律等语境〕',
 '最初抓连续击打，再到集中开火的一组炮；电学又借那种成组释放力量的名称。今天的小电池可以只有一个电化学单元。',
 '借法语 batterie，来自 battre 打击，再接拉丁 battuere。炮组义后来启发早期成组电学装置命名，最终覆盖现代电池；不是 bat 蝙蝠 + tery。',
 [['拉丁 battuere → 法语 batterie','打击、敲打'],['炮火、炮组等义','多件器具形成的一组'],['电学借名及现代扩展','早期电装置组 → 电池；一连串测试、问题']],
 'a rechargeable battery 充电电池，battery life 续航、使用寿命，a battery of tests 一系列测试，an artillery battery 炮组、炮兵单位。',
 'a rechargeable battery；battery life；a battery of tests；an artillery battery。',
 'battery 现代可包含一个或多个电化学单元，不把历史成组义当今天必须多节的硬规则；a battery of questions 是接连的问题，不是带电的问题。',
 ('The phone’s battery ran out before we arrived.','我们到达前，手机就没电了。'),('The device went through a battery of tests.','这个设备经过了一系列测试。'),sources=['https://www.etymonline.com/word/battery','https://en.wiktionary.org/wiki/battery#English'])
R('B3546','击打、炮组，电学借名与成组的一系列','BATTERY：从一连串打击，走到成组器具和电学装置','battery 打击、炮组 → 早期电装置组 → 电池；a battery of tests 保留一整组的感觉。',
 '今天最熟的电池义并非最早。掌握炮组、电装置的借名关系，就不必把击打、电池、一系列测试背成互不相干的中文清单。',
 'battuere → battre/batterie → battery；词源同族可联系 batter，但不是每个义都在现代英语临时加 -y 形成。',
 [['击打、成组与电池的多义词','battery']],
 'battery 现代可只有单个电化学单元；battery life 依语境是续航或寿命；a battery of 一系列。',
 'A battery of tests measured the battery’s performance.\n\n一系列测试测量了电池性能。','battery')
if __name__=='__main__':save('continuation_20261030_gr',ROOTS,WORDS)
