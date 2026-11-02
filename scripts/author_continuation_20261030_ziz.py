"""Familiar blends, borrowed names and common humanlike-machine vocabulary."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
JACUZZI='https://www.jacuzzi.com/our-brand/heritage.html'
def S(word,base):
 a=['https://en.wiktionary.org/wiki/'+word+'#English']
 if base=='Jacuzzi':a+=['https://www.merriam-webster.com/dictionary/Jacuzzi',JACUZZI]
 else:a.append('https://www.etymonline.com/word/'+base)
 return a
EXISTING_ROOT_ADDITIONS={
 'B3305':dict(words='brunch'.split(),label='breakfast + lunch → brunch：早午餐',note='brunch 缩合早餐 breakfast 与午餐 lunch，两顿合在一起的画面也在词里合在一起；不是另有一个独立的 br- 早晨词根。'),
 'C0571':dict(words='motel motels'.split(),label='motor + hotel → motel → motels：汽车旅馆',note='motel 缩合 motor 汽车相关材料 + hotel 旅馆，原本面向汽车旅行者；hotel 远接接待、住宿的词族，复数直接加 s。'),
 'C0443':dict(words='infotainment'.split(),label='information + entertainment → infotainment：信息加娱乐',note='infotainment 以 information 的 info- 和 entertainment 材料缩合，表示兼有信息、娱乐功能的内容；车载系统搭配也常见，不把 -tainment 当一个独立古典词根。'),
 'B3108':dict(words='cosplay'.split(),label='costume + play 经日语再进入英语：角色扮演',note='costume 服装 + play 扮演等英语材料先用于日语缩合 kosupure，英语再借入 cosplay；不能把中间的日语传播环节完全略掉。'),
 'B3219':dict(words='Jacuzzi'.split(),label='Jacuzzi：家族姓氏成为按摩浴缸品牌称呼',note='与 bath 比较沐浴设施，Jacuzzi 本来是家族姓氏，成为喷流按摩浴缸等产品的品牌；现代口语也常用来指这类浴缸。此处不用 bath 的词源解释姓氏。'),
 'B2997':dict(words='bikini bikinis'.split(),label='bikini → bikinis：借环礁地名的泳装名称',note='与 swim 比较泳装名称，bikini 经法语借 Bikini 环礁地名命名，相关历史背景是当时核试验引发的关注。最初 bi- 不是两的前缀，后来单基尼等名称则重新利用了这种联想。'),
 'A1692':dict(words='hooligan hooligans'.split(),label='hooligan → hooligans：闹事者与姓名来路',note='hooligan 通常联系爱尔兰姓氏 Houlihan 等变体，以及旧娱乐、新闻中的人物名称；究竟归于哪一位人物不确定。hooliganism 指滋事行为，hooligans 则数闹事者。'),
 'A1834':dict(words='vandal vandals'.split(),label='vandal → vandals：族名到故意毁坏者',note='现代普通名词 vandal 毁坏者借历史 Vandals 汪达尔人族名的贬损印象发展；这种语义转用不等于族名本身已证明对全族的历史评价。vandals 是复数，vandalize 是同词族动词。'),
 'B2912':dict(words='sabotage'.split(),label='sabotage：木鞋词族中的乱做、破坏',note='与 shoe 比较木鞋材料，sabotage 来自法语，向前接 saboter 乱做、笨拙地做及 sabot 木鞋。流传的把木鞋扔进机器故事不能当作已经证实的词源；现代动词由名词形成，表示故意破坏。'),
 'C0053':dict(words='android androids'.split(),label='android → androids：形状像人的机器',note='android 经近代拉丁语，接希腊 andro- 人、男性材料与 -oid 像……的形状；现代常说人形机器人，复数直接加 s。'),
 'C0917':dict(words='cyborg cyborgs'.split(),label='cybernetic + organism → cyborg：生物与技术装置结合',note='cyborg 缩合 cybernetic 控制论相关的 + organism 生物体，不是只有硬件机器人。早期理论中的生物—技术系统与科幻里的半机械人有关，但不要求恰好各占一半。'),
 'C0870':dict(words='humanoid humanoids'.split(),label='human + -oid → humanoid → humanoids：类人生物、形体',note='human 人的 + -oid 像……的 → humanoid，既可形容类人的，也可名词化为类人生物、类人机器。-oid 表相似，不保证本体就是人。'),
 'C0561':dict(words='hologram holograms'.split(),label='hologram → holograms：全息记录及其图像',note='holo- 整体 + -gram 记录、所写画之物 → hologram，现代光学名词；复数加 s。这里的完整记录是命名关系，不把所有看似悬浮的普通图像都当作技术上相同的东西。'),
 'A1858':dict(words='bot bots'.split(),label='robot → bot → bots：软件自动执行者的短称',note='现代网络 bot 缩略 robot；bots 是多个自动程序、软件代理。词形与老虫名 bot 相同，不表示网络程序从虫名直接演变，现代任务也可能有益或有害。'),
}
MOTEL=[['motor 汽车相关材料 + hotel 旅馆 → motel','面向驾车旅行者的旅馆名称'],['motel → motels','现代规则复数，更多旅馆而不是更多汽车']]
BIKINI=[['Bikini 环礁地名 → 法语泳装名称 bikini','命名与当时环礁核试验等公众关注背景相连'],['英语借入 bikini → bikinis','地名借为服装名；词首 bi 不是最初用来表示两的前缀']]
CYBORG=[['cybernetic 控制论相关的 + organism 生物体 → cyborg','现代缩合名词，强调生物体与外部技术装置的结合'],['早期人—技术系统讨论 → 科幻等语境中的半机械人形象','cyborg + -s → cyborgs；不是精确一半人一半机器的比例词']]
W('brunch','英、美 /brʌntʃ/','早午餐',
 '睡得晚，上午接近中午吃一顿，把早餐、午餐合在一起，这顿饭就是 brunch。两顿合并，两个词也合并。',
 'breakfast 早餐 + lunch 午餐缩合 → brunch，取前者开头和后者较后的材料；不像普通复合词那样把两个完整单词并排放。',
 [['breakfast 早餐 + lunch 午餐','两顿合在一起的饮食安排'],['两个词的部分缩合 → brunch','英语名词早午餐，也可按语境用作动词']],
 'have brunch 是吃早午餐；a Sunday brunch 是周日早午餐；meet for brunch 是约着吃早午餐。',
 'have brunch；Sunday brunch；meet for brunch。',
 'brunch 往往兼代早餐、午餐；late breakfast 只说早餐吃得晚，不一定说明午餐也省并了。',
 ('We met for brunch on Sunday.','我们周日约着吃了早午餐。'),('The café serves brunch until two.','这家咖啡馆的早午餐供应到两点。'),sources=S('brunch','brunch'))
W('motel','英 /məʊˈtel/；美 /moʊˈtɛl/','汽车旅馆',
 '开车旅行，在路边找个便于停车过夜的旅馆，常会遇到 motel。名字本来就是为汽车旅行者住店这个场景造的。',
 'motor 汽车相关材料 + hotel 旅馆缩合 → motel；motor 的前部与 hotel 的尾部拼合，重音常在后一个音节。',MOTEL,
 'a roadside motel 是路边汽车旅馆；a motel room 是汽车旅馆房间；stay at a motel 是住汽车旅馆。',
 'a roadside motel；a motel room；stay at a motel。',
 'motel 的历史典型是面向驾车旅客的住宿；hotel 更宽泛，不能仅凭房价高低区分两者。',
 ('We stayed at a motel outside the town.','我们住在镇外一家汽车旅馆。'),('The motel has parking spaces beside the rooms.','这家汽车旅馆在客房旁设有停车位。'),sources=S('motel','motel'))
W('motels','英 /məʊˈtelz/；美 /moʊˈtɛlz/','汽车旅馆〔复数〕',
 '公路边一家接一家的汽车旅馆，是 motels。名字虽然是缩合词，复数并不特殊。',
 'motel + -s → motels，/l/ 后读 /z/；给整个汽车旅馆名词加 s。',MOTEL+[['motel + -s → motels','多家汽车旅馆，词尾 /lz/']],
 'roadside motels 是路边汽车旅馆；several motels 是几家汽车旅馆；rooms in local motels 是当地汽车旅馆的房间。',
 'roadside motels；several motels；local motels。',
 'motels 数旅馆，motel rooms 数房间；一家 motel 可以有许多 rooms。',
 ('Several motels line the highway.','几家汽车旅馆沿公路排列。'),('We compared two motels before booking a room.','订房前，我们比较了两家汽车旅馆。'),sources=S('motels','motel'))
W('infotainment','英 /ˌɪnfəʊˈteɪnmənt/；美 /ˌɪnfoʊˈteɪnmənt/','资讯娱乐；信息与娱乐结合的内容、功能',
 '一边告诉你东西，一边让你觉得好看、好玩，是 infotainment。把信息和娱乐混合，是这个词最容易抓住的核心。',
 'information 的短材料 info- + entertainment 的部分缩合 → infotainment；前者保留信息，后者保留娱乐，不把 -tainment 另认成一个完整古典词根。',
 [['information 信息 → info-；entertainment 娱乐','两个现代英语词的材料提供意义'],['缩合 → infotainment','兼具信息、娱乐的内容；也用于车载信息娱乐系统搭配']],
 'an infotainment show 是资讯娱乐节目；an infotainment system 常说信息娱乐系统；the line between news and infotainment 是新闻与资讯娱乐的界线。',
 'infotainment shows；an infotainment system；news and infotainment。',
 'infotainment 强调信息与娱乐的结合；语境可能赞其有趣，也可能批评过度娱乐化，词本身不只固定为一种褒贬。',
 ('The programme mixes serious interviews with infotainment.','节目把严肃访谈与资讯娱乐内容混合在一起。'),('The car has a touchscreen infotainment system.','这辆车配有触屏信息娱乐系统。'),sources=S('infotainment','infotainment'))
W('cosplay','英 /ˈkɒzpleɪ/；美 /ˈkɑzpleɪ/','角色扮演、装扮成作品人物；进行这种装扮',
 '穿上喜欢角色的衣服、模仿角色形象，去展会或拍照，就是 cosplay。名字里的衣装与扮演都还看得出来。',
 'costume 服装 + play 扮演等英语材料先在日语里缩合为 kosupure，英语再借入 cosplay；不仅是两个英语词直接在英语中首次拼接。',
 [['英语 costume + play 的材料 → 日语 kosupure','日语把长材料压缩为角色装扮活动名'],['借回英语 cosplay','可作活动名词，也可作进行角色装扮的动词']],
 'a cosplay event 是角色扮演活动；cosplay as a character 是装扮成某角色；a cosplay costume 是角色装扮服装。',
 'a cosplay event；cosplay as a character；a cosplay costume。',
 'wearing a costume 只说穿装束；cosplay 往往进一步联系特定人物、作品和扮演活动。',
 ('She enjoys cosplay and makes her own costumes.','她喜欢角色扮演，还自己制作服装。'),('He plans to cosplay as a character from his favourite game.','他打算装扮成最喜欢的游戏中的一个角色。'),sources=S('cosplay','cosplay'))
W('Jacuzzi','英、美 /dʒəˈkuːzi/','按摩浴缸、水流按摩池〔品牌名称及其常见称呼〕',
 '浴缸、池里有喷流按摩，旅行介绍里可能写 Jacuzzi。它先是一个家族、品牌的名字，再让人想到这种浴缸。',
 'Jacuzzi 家族姓氏 → 浴缸、水疗设备品牌 Jacuzzi；词典把它收为品牌称呼。现代口语也常用它说类似的喷流按摩浴缸，名称本身不按普通英语小词拆。',
 [['Jacuzzi 家族姓氏 → 相关设备的品牌名称','家族产品发展留下了这个姓氏'],['品牌名称用于喷流按摩浴缸等的称呼','正式写法通常保留大写 J']],
 'a Jacuzzi bath 是按摩浴缸；an outdoor Jacuzzi 是室外按摩池；a room with a Jacuzzi 是带按摩浴缸的房间。',
 'a Jacuzzi bath；an outdoor Jacuzzi；a room with a Jacuzzi。',
 'hot tub 是更通用的热水浴池称呼，Jacuzzi 有品牌背景；实际产品介绍里，两种词不宜完全无条件互换。',
 ('The room has a large Jacuzzi bath.','这个房间配有一个大按摩浴缸。'),('The brochure shows an outdoor Jacuzzi beside the pool.','宣传册上展示了泳池旁的室外按摩池。'),sources=S('Jacuzzi','Jacuzzi'))
W('bikini','英、美 /bɪˈkiːni/','比基尼、两件式泳装',
 '上、下分开的两件式泳装，常叫 bikini。虽然刚好有两件，名字最初并不是按 bi- 表示二来造的。',
 '法语泳装名借 Bikini 环礁地名，再进入英语；命名与当时核试验引发的公众关注相关，具体宣传联想有不同解释，不必编成确定的单一故事。',BIKINI,
 'a blue bikini 是蓝色比基尼；a bikini top 是比基尼上衣；a bikini bottom 是下装。',
 'a blue bikini；a bikini top；a bikini bottom。',
 '后来 monokini 等名称借用了 bi- 像二的联想；后来的重新分析，不能倒过来证明 bikini 最初就是二加后缀。',
 ('She packed a bikini for the beach holiday.','她为海边假期带了一套比基尼。'),('The shop window displayed a blue bikini.','商店橱窗里展示了一套蓝色比基尼。'),sources=S('bikini','bikini'))
W('bikinis','英、美 /bɪˈkiːniz/','比基尼泳装〔复数〕',
 '几套不同颜色、款式的比基尼，是 bikinis。这里数的是完整泳装套装，不是把上、下两片各算一套。',
 'bikini + -s → bikinis，/i/ 后接 /z/；来自地名的借词进入英语后，直接用规则复数。',BIKINI+[['bikini + -s → bikinis','多套或多款比基尼，词尾 /iz/']],
 'colourful bikinis 是色彩鲜艳的比基尼；two bikinis 是两套；bikinis and swimsuits 是比基尼和其他泳装。',
 'colourful bikinis；two bikinis；bikinis on display。',
 'two bikinis 通常是两套泳装；两套里的上衣要说 two bikini tops，前部 bikini 仍用单数作修饰。',
 ('The shop sells bikinis in several colours.','这家商店出售几种颜色的比基尼。'),('She packed two bikinis for the trip.','她为旅行装了两套比基尼。'),sources=S('bikinis','bikini'))
W('hooligans','英 /ˈhuːlɪɡənz/；美 /ˈhulɪɡənz/','流氓、闹事者〔复数〕',
 '一群惹事、打闹、破坏秩序的人，常被叫 hooligans。这个词本身就是批评性的称呼。',
 'hooligan 通常联系爱尔兰姓氏 Houlihan 等变体，旧歌曲、漫画、新闻中的人物名也参与传播；无法确定归功于哪一个真人。加 -s → hooligans，词尾 /z/。',
 [['姓氏 Houlihan 等变体与娱乐、新闻中的 Hooligan 名称','现代闹事者称呼的背景；具体人物来历有争论'],['hooligan + -s → hooligans','复数人物名词，常带批评意味']],
 'football hooligans 是足球流氓；a gang of hooligans 是一伙闹事者；hooligans outside the stadium 是体育场外闹事的人。',
 'football hooligans；a gang of hooligans；hooligans outside the stadium。',
 'football fans 是球迷，football hooligans 特指其中闹事的一类；不能把所有热情球迷都这样称呼。',
 ('Hooligans damaged the bus shelter after the match.','比赛后，闹事者破坏了公交候车亭。'),('The article distinguishes ordinary fans from hooligans.','文章把普通球迷和足球流氓区分开来。'),sources=S('hooligans','hooligan'))
W('vandals','英、美 /ˈvændəlz/','故意毁坏财物者〔复数〕',
 '把公共设施砸坏、故意毁坏别人东西的人，是 vandals。重点是蓄意毁坏，不只是东西意外坏了。',
 '普通名词 vandal 从历史 Vandals 汪达尔人族名的贬损印象发展；现代加 -s → vandals，词尾 /z/。名称的这种转用，不等于对历史族群的全部评价都是事实。',
 [['历史 Vandals 族名 → 英语 vandal 故意毁坏者','借旧时历史印象形成普通名词'],['vandal + -s → vandals','现代复数；小写常用于普通毁坏者称呼']],
 'vandals damaged something 是有人蓄意破坏某物；damage by vandals 是人为蓄意损坏；protect against vandals 是防止遭破坏。',
 'damage by vandals；vandals broke the windows；protect against vandals。',
 'vandalism 说破坏行为，vandals 说实施者；Vandals 大写还可能指历史汪达尔人，靠上下文辨别。',
 ('Vandals broke the windows of the empty building.','有人蓄意打碎了那栋空楼的窗户。'),('The statue had been damaged by vandals.','雕像遭到了蓄意毁坏。'),sources=S('vandals','vandal'))
W('sabotage','英 /ˈsæbətɑːʒ/；美 /ˈsæbəˌtɑʒ/','蓄意破坏；故意妨碍',
 '不是不小心弄坏，而是有意让事情做不成，sabotage 就有这种“从里面使坏、拖垮”的感觉。',
 '法语 sabotage 接 saboter 乱做、笨拙地做等，向前有 sabot 木鞋材料；英语动词再由名词形成。工人把木鞋扔进机器的流行故事，不是已经证实的词源解释。',
 [['法语 sabot 木鞋 → saboter 有乱做、做坏等用法 → sabotage','木鞋词族与破坏语义相关，具体不能靠扔鞋故事补证'],['英语借名词 sabotage → 动词 sabotage','从蓄意破坏物件，也扩大到故意妨碍计划、合作']],
 'an act of sabotage 是一次蓄意破坏；sabotage a plan 是故意破坏计划；suspected sabotage 是怀疑有人蓄意破坏。',
 'an act of sabotage；sabotage a plan；suspected sabotage。',
 'damage 可以是意外或故意的损坏；sabotage 通常把蓄意妨碍、破坏的意图也说出来。',
 ('The novel centres on an act of sabotage.','小说围绕一次蓄意破坏事件展开。'),('Their constant arguments threatened to sabotage the project.','他们不断争吵，眼看要把项目搅黄了。'),sources=S('sabotage','sabotage'))
W('androids','英、美 /ˈændrɔɪdz/','人形机器人〔复数〕',
 '科幻片里那些外形、动作像人的人工角色，常叫 androids。名字抓住的是“像人的形状”。',
 'android 经近代拉丁语，接希腊 andro- 人、男性材料 + -oid 像……的形状；再加 -s → androids，/d/ 后读 /z/。',
 [['希腊 andro- + 形状相似材料 → 近代拉丁 androides → android','现代人形机器的名称，科幻帮助扩大使用'],['android + -s → androids','复数以人形机器为典型，词尾 /dz/']],
 'lifelike androids 是逼真的人形机器人；androids in a film 是电影中的人形机器人；androids and humans 是机器人与人类。',
 'lifelike androids；androids in a film；androids and humans。',
 'androids 这类普通名词不等于 Android 手机系统名称；cyborgs 则强调生物体与技术结合，具体作品设定可能有差别。',
 ('The film imagines a city where androids live among humans.','电影设想一座人形机器人与人类共同生活的城市。'),('The museum displayed two lifelike androids.','博物馆展出了两个逼真的人形机器人。'),sources=S('androids','android'))
W('cyborg','英 /ˈsaɪbɔːɡ/；美 /ˈsaɪbɔrɡ/','赛博格、半机械人；生物与技术装置结合的个体',
 '一个生物体把技术装置整合进自身，组成共同工作的系统，可以叫 cyborg。科幻中常画成半人半机器。',
 'cybernetic 控制论相关的 + organism 生物体的开头材料缩合 → cyborg；最初用于人和外加技术装置组成的系统，不要求恰好各占一半。',CYBORG,
 'a cyborg character 是半机械人角色；a cyborg in a novel 是小说中的赛博格；a fictional cyborg 是虚构的生物机械结合体。',
 'a cyborg character；a fictional cyborg；human and cyborg。',
 'robot 范围更广；cyborg 特别保留生物与技术结合这一点。android 主要强调像人的人工形体，三词在作品中也可能被作者重新设定。',
 ('The novel’s hero becomes a cyborg after the accident.','小说主人公在事故后变成了半机械人。'),('She designed a cyborg character for the game.','她为游戏设计了一个赛博格角色。'),sources=S('cyborg','cyborg'))
W('cyborgs','英 /ˈsaɪbɔːɡz/；美 /ˈsaɪbɔrɡz/','赛博格、半机械人〔复数〕',
 '故事里不止一个生物与机械结合的角色，就用 cyborgs。现代画面常是半机械人，但名称本来强调系统结合。',
 'cyborg + -s → cyborgs，/ɡ/ 后读 /z/；原来的 cybernetic + organism 缩合不变。',CYBORG+[['cyborg + -s → cyborgs','多名或多个生物—技术结合体，词尾 /ɡz/']],
 'cyborgs in science fiction 是科幻中的半机械人；a world of cyborgs 是有许多赛博格的世界。',
 'cyborgs in science fiction；a group of cyborgs；humans and cyborgs。',
 '不能只因机器人有人的外形，就一定叫 cyborgs；是否强调生物与技术融合，要看词义与作品设定。',
 ('The story follows a group of cyborgs on a distant planet.','故事追随一群生活在遥远星球上的半机械人。'),('The essay compares robots, androids and cyborgs.','文章比较机器人、人形机器人和赛博格。'),sources=S('cyborgs','cyborg'))
W('humanoids','英 /ˈhjuːmənɔɪdz/；美 /ˈhjuməˌnɔɪdz/','类人生物；类人机器〔复数〕',
 '有头、躯干、四肢，整体外形像人，却未必是人，可以称 humanoids。它首先说“长得像人”。',
 'human 人的 + -oid 像……的 → humanoid；形容词可转作类人生物、类人机器的名词，再加 -s → humanoids，词尾 /dz/。',
 [['human + -oid → humanoid 类人的','-oid 提供形状、性质相似的构词关系'],['名词化为类人生物等 + -s → humanoids','既可能是想象中的生物，也可能是类人机器']],
 'alien humanoids 是外星类人生物；robotic humanoids 是类人机器；humanoids in a story 是故事中的类人个体。',
 'alien humanoids；robotic humanoids；humanoids in the story。',
 'humans 直接指人；humanoid 可作形容词，如 humanoid robots，humanoids 单独作名词时则数这些类人个体。',
 ('The explorers meet strange humanoids in the story.','故事里，探险者遇见了奇怪的类人生物。'),('The exhibition included several robotic humanoids.','展览里有几个类人机器人。'),sources=S('humanoids','humanoid'))
W('holograms','英 /ˈhɒləɡræmz/；美 /ˈhɑləˌɡræmz/','全息图、全息影像〔复数〕',
 '全息图记录、重现物体的立体光学信息，常让人换个角度看见不同细节。holograms 的 holo- 是整体，-gram 是记录、图像。',
 'holo- 接希腊 holos 整体 + -gram 所记录、画出的东西 → hologram，近代光学命名；加 -s → holograms，/m/ 后读 /z/。',
 [['希腊 holos 整体 + -gram 记录材料 → hologram','现代光学名词，借完整记录的关系命名'],['hologram + -s → holograms','多幅全息图、全息影像，词尾 /mz/']],
 'holograms on cards 是卡片上的全息图；display holograms 是展示全息图；colour holograms 是彩色全息图。',
 'colour holograms；holograms on cards；an exhibition of holograms。',
 '日常宣传可能把多种立体显示都叫 holograms；词源里的整体记录不能证明任意悬浮效果都使用同一种光学技术。',
 ('The exhibition shows several colour holograms.','展览展示了几幅彩色全息图。'),('Some cards use holograms as visual security features.','有些卡片使用全息图作为视觉防伪特征。'),sources=S('holograms','hologram'))
W('bots','英 /bɒts/；美 /bɑts/','自动程序、机器人账号；软件机器人〔复数〕',
 '自动回答、抓取或执行任务的程序，常叫 bots。它们可以没有手脚，只是在软件里代人反复做事。',
 '现代网络 bot 缩略 robot；bot + -s → bots，/t/ 后读 /s/。老词 bot 还有虫类等不同来源，网络义不靠那条虫名路线解释。',
 [['robot → 缩略 bot','机器人形象借给自动执行任务的软件'],['bot + -s → bots','多个自动程序、软件代理；作用可能不同']],
 'chat bots 是聊天机器人；search bots 是搜索自动程序；automated bots 是自动化程序；social media bots 是社交平台机器人账号。',
 'chat bots；search bots；social media bots。',
 'bots 不自动等于骗子账号：有的提供服务，有的制造垃圾内容。是否有害要看具体行为，词本身先说明自动执行。',
 ('The website uses bots to answer simple questions.','网站用机器人程序回答简单问题。'),('Some comments were posted by bots.','有些评论是机器人账号发布的。'),sources=S('bots','bot'))
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_ziz',ROOTS,WORDS)
 extend_lessons()
