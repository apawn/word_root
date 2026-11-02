"""Common movements and visible metaphors: evade, press, hail, crane, balloon."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
def S(word,base):return ['https://en.wiktionary.org/wiki/'+word+'#English','https://www.etymonline.com/word/'+base]
EXISTING_ROOT_ADDITIONS={
 'B4404':dict(words='dodge dodges dodged dodging'.split(),label='dodge → dodges、dodged、dodging：闪开与绕开',note='dodge 旧义在言语、行动上左右转移，较远来源不明，可能联系方言 dodd；字面闪避与抽象回避都很早，不硬排成先身体后所有比喻。去 e 后接 -ed、-ing，-ed 在 /dʒ/ 后读 /d/。'),
 'C0986':dict(words='thrust thrusts thrusting'.split(),label='thrust：有力地往前推、塞',note='与 push 比较动作，不从拉丁 pulsare 派生。thrust 借北欧语推压一族，较远是否与 threat 同源有争论；现代过去式、过去分词仍为 thrust。'),
 'B3667':dict(words='hail hails hailed hailing'.split(),label='hail：祝好、招呼一支；冰雹另支',note='招呼用 hail 接北欧 heill 等健康、安好材料；冰雹 hail 接古英语 hægl、hagol，是另一来源。hails、hailed、hailing 能承接不同词线，不能全用冰雹解释。'),
 'B2627':dict(words='crane cranes craned craning'.split(),label='crane：鹤 → 长臂起重机；伸长脖子',note='和 bird 比较鸟类；crane 接古英语 cran，较远可能与嘶哑叫声相关。鸟的长颈、长嘴形象借给起重机；动词既有用起重机吊，也有伸颈看，吊运用法记载更早。'),
 'C0110':dict(words='balloon balloons ballooned ballooning'.split(),label='balloon：大球 → 气球 → 膨胀增长',note='意大利 palla 球 + 增大材料 -one → pallone 大球，经法语 ballon 等借入。由大充气球的游戏与球体名称到飞行气球、玩具气球，英语整体又转作上升、膨胀动词。'),
 'B2504':dict(words='workout workouts'.split(),label='workout → workouts：一场锻炼',note='work + out 的动词短语与名词化组成 workout，常见意义是一场锻炼，早期记录联系拳击训练。不能把 work out 的算出、顺利发展等所有意思都搬给闭合名词 workout。'),
}
DODGE=[['英语 dodge：言语、行动左右转移','较远来源不明，可能联系方言 dodd 等'],['闪身避开；也有抽象回避、耍花招等旧用法','现代可用躲开球、绕开问题的画面一起记，不硬定所有义项先后']]
THRUST=[['北欧语推、压材料 → 中古英语 thristen、thruste 等','对应古诺尔斯 þrysta；更远词族分析仍有争论'],['thrust：推、塞；名词推力、推进的重点','动作推动 → 推进力；论述的 thrust 是主要指向']]
HAIL=[['招呼一支：北欧 heill、古英语安好祝愿等 → hail','祝对方安好 → 打招呼、远处呼叫；称赞、宣称某人为'],['冰雹一支：古英语 hægl、hagol → hail','冰粒降落；另源的天气名词及动词，不从招呼词派生']]
CRANE=[['古英语 cran 鹤 → 英语 crane','更远可能与鸟的嘶哑叫声相连'],['鹤的长颈、长嘴轮廓 → 长臂起重机；再有吊运动词','另借鸟伸颈形象说人伸长脖子看；不要把两种动词用法硬并成一项']]
BALLOON=[['意大利 palla 球 + -one 增大 → pallone 大球','法语 ballon 等影响英语借入形式'],['英语 balloon：大充气球及其游戏 → 飞行气球、玩具气球','整体转作动词：乘气球上升、膨胀；再喻规模迅速变大']]
WORKOUT=[['work + out：动词短语的用法发展','体育训练是其中一条用法，另有算出、实现、顺利发展等'],['闭合名词 workout：训练、一场锻炼','早期记录联系拳击训练，后来扩大到一般体育锻炼']]
W('dodges','英 /ˈdɒdʒɪz/；美 /ˈdɑdʒɪz/','躲开；回避〔第三人称单数〕；闪避动作、花招〔复数〕',
 '球飞过来，他一侧身；难题抛过来，他换个话题。He dodges 可以同时抓住这两种“绕开”。',
 'dodge + -s → dodges，基础词已有 e，只再加 s；词尾 /dʒ/ 后的后缀读 /ɪz/，增加一个音节。',DODGE+[['dodge + -s → dodges','单数主语的动词；也可作名词复数']],
 'dodges a question 是回避问题；dodges a ball 是闪开球。若是名词 dodges，则可指闪躲动作或耍的花招。',
 'dodges a question；dodges a ball；clever dodges。',
 'avoid 范围较宽；dodge 常带迅速闪开、灵活绕开的感觉，回答问题时还容易带回避的批评意味。',
 ('She dodges the question and changes the subject.','她避开问题，换了话题。'),('The player dodges the ball at the last moment.','球员在最后一刻闪开了球。'),sources=S('dodges','dodge'))
W('dodged','英 /dɒdʒd/；美 /dɑdʒd/','躲开了；回避了〔过去式、过去分词〕',
 '球擦身而过，已经躲开，是 dodged；问题被绕过去，也能说 dodged。动作从正在面对变成已经避过。',
 'dodge 去掉末尾 e + -ed → dodged；/dʒ/ 后的 -ed 读 /d/，不额外读一个 /ɪd/ 音节。',DODGE+[['dodge 去 e + -ed → dodged','规则过去式、过去分词；后缀 /d/']],
 'dodged a question 是当时回避了问题；have dodged 说明已经躲过、避开。dodged a bullet 也常比喻侥幸躲过麻烦。',
 'dodged a question；dodged the ball；dodged a bullet。',
 'dodged a bullet 既可字面，也可比喻。谈拒绝一份后来问题很多的工作时，通常不涉及真的子弹。',
 ('He dodged a falling branch.','他闪开了一根掉下来的树枝。'),('We dodged a bullet by cancelling that booking.','我们取消了那次预订，算是侥幸躲过一场麻烦。'),sources=S('dodged','dodge'))
W('dodging','英 /ˈdɒdʒɪŋ/；美 /ˈdɑdʒɪŋ/','正在躲避；回避；闪避行为',
 '在人群里左闪右绕，或谈话里始终不接一个问题，这个持续过程是 dodging。',
 'dodge 去末尾 e + -ing → dodging；g 前的软音环境仍使 dg 读 /dʒ/，末尾接 /ɪŋ/。',DODGE+[['dodge 去 e + -ing → dodging','现在分词、动名词，描写过程或行为']],
 'be dodging 是正在闪避、回避；stop dodging the issue 是别再绕着这个问题走。',
 'dodging traffic；dodging questions；stop dodging the issue。',
 'dodging 可以描述身体动作，也可描述言语策略；具体语境决定“躲车”还是“躲问题”，不必换一套词根。',
 ('She crossed the street, dodging puddles.','她绕着水洼穿过街道。'),('Stop dodging the issue and tell us what happened.','别再回避问题，告诉我们发生了什么。'),sources=S('dodging','dodge'))
W('thrust','英、美 /θrʌst/','猛推、塞；推力；要旨、主要方向',
 '把一张纸用力塞到别人手里，是 thrust。力量向一个方向顶出去；同一幅画面也能帮你理解引擎推力、论述的主要指向。',
 '借自北欧语推、压材料，对应古诺尔斯 þrysta；中古英语 thristen、thruste 等发展为 thrust。现代原形、过去式、过去分词都常写 thrust。',THRUST,
 'thrust something into 是往里面猛塞；engine thrust 是引擎推力；the main thrust of an argument 是论述的主要观点。',
 'thrust a note into a hand；engine thrust；the main thrust of the argument。',
 'push 可以是普通推；thrust 常突出有力、突然向前。名词要旨是在说论述往哪儿推进，不必理解为内容带有攻击性。',
 ('She thrust the letter into my hand.','她把信一下塞到我手里。'),('The main thrust of the report is that training needs to improve.','报告的核心意思是培训需要改进。'),sources=S('thrust','thrust'))
W('thrusts','英、美 /θrʌsts/','猛推、塞〔第三人称单数〕；猛推动作、主要方向〔复数〕',
 '他把手伸进口袋、一下塞进去，可以说 he thrusts his hand into his pocket。作名词时，几次有力前推也可以数成 thrusts。',
 'thrust + -s → thrusts，词尾 /t/ 后的后缀读 /s/；名词复数与动词第三人称单数同形。',THRUST+[['thrust + -s → thrusts','末尾 /sts/；不用额外加 /ɪz/']],
 'she thrusts 是单数主语配动词；the thrusts of a campaign 可以说一场行动的几条推进方向，取决于语境。',
 'thrusts a hand into a pocket；thrusts a note forward；several thrusts。',
 'thrusts 不是过去式；现代常见过去式仍是 thrust。He thrusts 说现在，he thrust 说过去。',
 ('He thrusts his hands into his pockets whenever he feels awkward.','他一觉得尴尬，就把双手插进口袋。'),('The engine thrusts the small craft forward.','引擎推动小艇向前。'),sources=S('thrusts','thrust'))
W('thrusting','英、美 /ˈθrʌstɪŋ/','正在猛推、塞；前推动作',
 '把东西往前猛塞的过程，就是 thrusting。动作有方向、有力度，和轻轻挪一挪的画面不同。',
 'thrust + -ing → thrusting；不删字母、不双写 t。现代基础词末尾是辅音群 /st/，直接接 -ing。',THRUST+[['thrust + -ing → thrusting','现在分词、动名词，表示动作过程']],
 'be thrusting 是正在猛推、塞；thrusting a hand into 描写手一下伸进某处。抽象事物也能被比喻性地推到面前。',
 'thrusting a hand into a pocket；thrusting a note forward；thrusting into view。',
 'thrusting 是现在分词；过去分词通常是 thrust。has thrust 与 is thrusting 表示的时间、过程不同。',
 ('She was thrusting papers into a bag when the phone rang.','电话响时，她正把文件往包里塞。'),('The child kept thrusting the drawing towards me.','孩子不停把画往我面前递。'),sources=S('thrusting','thrust'))
W('hail','英、美 /heɪl/','冰雹；下冰雹；招呼、招手叫；称赞为；来自',
 'hail 有两幅来自不同旧词的画面：冰粒从天上砸下；向远处的人喊一声招呼。认清两支后，叫出租车、称赞某人、来自某地就不会全挤到天气里。',
 '冰雹名词接古英语 hægl、hagol，天气动词也有古英语 hagalian。招呼、呼叫一支接北欧 heill 等安好祝愿；由问候扩展到远处呼叫、欢迎和称赞。',HAIL,
 'hail a taxi 是招手叫车；hail someone as a hero 是称某人为英雄；hail from 是来自某地。a hail of questions 借密集冰粒说一连串问题。',
 'hail a taxi；hail someone as a hero；hail from a town；heavy hail。',
 'hail 冰雹和 hail 招呼是同形不同源。hail from 也不是说人像冰雹一样掉下来，而是呼叫、通报来处等语境发展出的用法。',
 ('We waited inside until the hail stopped.','我们一直在屋里等到冰雹停下。'),('She raised her arm to hail a taxi.','她抬起手臂招出租车。'),('The two musicians hail from the same town.','这两位音乐家来自同一个镇。'),sources=S('hail','hail'))
W('hails','英、美 /heɪlz/','招呼、称赞；来自；下冰雹〔第三人称单数〕',
 '一句 she hails from Leeds，是说她来自利兹；it hails 是下冰雹。前面主语和后面搭配把两条词线分得很清楚。',
 'hail + -s → hails，/l/ 后的后缀读 /z/；不同来源的 hail 动词都可形成这一拼写。',HAIL+[['hail + -s → hails','动词第三人称单数，不把不同来源合成一个历史词']],
 'hails from 是来自；hails someone as 是称赞某人为；it hails 的 it 是天气句主语。',
 'hails from London；hails the result as a success；it hails。',
 'hail 作冰雹材料名词通常不可数，不需要靠 hails 表示很多冰粒；常见 hails 应先检查动词用法。',
 ('The singer hails from a small coastal town.','这位歌手来自一个海边小镇。'),('The review hails the film as a masterpiece.','评论盛赞这部电影是杰作。'),sources=S('hails','hail'))
W('hailed','英、美 /heɪld/','招呼了；被称赞为；下过冰雹〔过去式、过去分词〕',
 'hailed a taxi 是已经招到、招呼过出租车；was hailed as a hero 是被大家当作英雄称赞。先抓具体搭配，再判断属于哪条词线。',
 'hail + -ed → hailed，后缀读 /d/。招呼动词与冰雹天气动词的过去形式恰好相同。',HAIL+[['hail + -ed → hailed','过去式、过去分词；末尾 /ld/']],
 'hailed a taxi 说主动招呼；was hailed as 是被称为、被赞为；it hailed 说当时下冰雹。',
 'hailed a taxi；hailed as a breakthrough；it hailed。',
 'hail from 常说明出身、来源，通常用一般现在时；过去的称赞不靠 from，而常用 hailed as。',
 ('We hailed a taxi outside the station.','我们在车站外招了一辆出租车。'),('The discovery was hailed as a breakthrough.','这项发现被誉为一次突破。'),sources=S('hailed','hail'))
W('hailing','英、美 /ˈheɪlɪŋ/','正在招呼、叫车；称赞；正在下冰雹',
 '站在路边挥手叫车，是 hailing a taxi；窗外噼里啪啦落冰粒，是 it is hailing。同一个形式，背后有两条不同来历。',
 'hail + -ing → hailing，基础词直接接 -ing；读 /ˈheɪlɪŋ/。',HAIL+[['hail + -ing → hailing','现在分词、动名词；保留对应基础动词的意义']],
 'be hailing a taxi 是正在叫车；be hailing a result as a success 是正称赞成果；it is hailing 是正在下冰雹。',
 'hailing a taxi；hailing the decision；it is hailing。',
 'hailing 与 healing 治愈读音不同：前者 /heɪ/，后者 /hiː/。招呼词较远与安好词族有关，也不能把现代两词直接互换。',
 ('She stood by the road, hailing a taxi.','她站在路边挥手叫出租车。'),('It was hailing when we reached the hotel.','我们到旅馆时正在下冰雹。'),sources=S('hailing','hail'))
W('crane','英、美 /kreɪn/','鹤；起重机；伸长脖子看；用起重机吊运',
 '先看一只长颈、长嘴的鹤，再看工地上伸着长臂的起重机，就能明白 crane 怎样把名字借给机器。人伸脖子看，也借同一鸟的姿态。',
 '古英语 cran 延续日耳曼语鸟名，较远可能接嘶哑叫声材料。机器名和动词是后来的英语扩展；用机器吊运的动词记录，比伸脖子看的记录更早。',CRANE,
 'a crane 可以是一只鹤或一台起重机；crane your neck 是伸长脖子看。craning 不意味着使用机器，要看宾语。',
 'a crane at a building site；a crane by the water；crane your neck。',
 'crane your neck 的画面是努力把脖子伸长；turn your head 只是转头，动作重点不同。',
 ('A crane stood in the shallow water.','一只鹤站在浅水里。'),('The crane lifted a steel beam over the wall.','起重机把一根钢梁吊过了墙。'),('People had to crane their necks to see the stage.','大家得伸长脖子才能看到舞台。'),sources=S('crane','crane'))
W('cranes','英、美 /kreɪnz/','鹤、起重机〔复数〕；伸长脖子看〔第三人称单数〕',
 '水边几只鹤和工地几台起重机，都可以叫 cranes。长颈鸟到长臂机器的形状联想，复数后仍然看得见。',
 'crane + -s → cranes，基础词末尾已有 e，再加 s，后缀读 /z/；也能是动词第三人称单数。',CRANE+[['crane + -s → cranes','多个鸟、机器；或单数主语的伸颈动作']],
 'construction cranes 是建筑起重机；a flock of cranes 是一群鹤；she cranes her neck 是她伸长脖子。',
 'construction cranes；a flock of cranes；cranes her neck。',
 'cranes 与 crane’s 同音，前者可以是复数，后者通常是所有格或缩写；是否有撇号会改变句法。',
 ('Two cranes stood beside the unfinished tower.','两台起重机立在尚未建成的高楼旁。'),('She cranes her neck whenever a bus approaches.','每逢公交车驶来，她就伸长脖子看。'),sources=S('cranes','crane'))
W('craned','英、美 /kreɪnd/','伸长脖子看了；吊运了〔过去式、过去分词〕',
 '前面有人挡着，他把脖子伸出去看，是 craned his neck。若句子说钢梁被 craned into place，则是用起重机吊到位。',
 'crane 去末尾 e + -ed → craned，后缀读 /d/；鸟姿态与机器吊运两个动词用法都能形成这个过去形式。',CRANE+[['crane 去 e + -ed → craned','过去式、过去分词；末尾 /nd/']],
 'craned her neck 说伸颈动作；was craned into position 说借机器吊到位置。注意主动身体动作与被动吊运句的区别。',
 'craned his neck；craned over the crowd；craned into position。',
 'craned the neck 中通常会说明谁的脖子，如 craned her neck；机器用法则常让重物成为宾语或被动主语。',
 ('He craned his neck to read the notice.','他伸长脖子看告示。'),('The new roof section was craned into position.','新的屋顶构件被吊装到位。'),sources=S('craned','crane'))
W('craning','英、美 /ˈkreɪnɪŋ/','正在伸长脖子看；吊运过程',
 '人群后面，大家一直伸着脖子找舞台，就是 craning their necks。它把鹤伸颈的姿态转成了人的动作。',
 'crane 去末尾 e + -ing → craning；不把 e 留成 craneing。整个名词转成动词后，再形成分词。',CRANE+[['crane 去 e + -ing → craning','现在分词、动名词；伸颈或吊运过程']],
 'be craning your neck 是正在伸长脖子；craning the load 则可说用起重机吊负载，语境决定所指。',
 'craning her neck；craning to see；craning a load into place。',
 'craning to see 强调努力伸颈去看，不必真的看到；seeing 只说明看见，没有这层动作。',
 ('She kept craning her neck to look over the fence.','她不停伸长脖子，想越过围栏往里看。'),('We saw workers craning a large tank into place.','我们看见工人用起重机把一个大罐吊装到位。'),sources=S('craning','crane'))
W('balloon','英 /bəˈluːn/；美 /bəˈlun/','气球；热气球等飞行气球；迅速膨胀、激增',
 '气球一点点鼓大，给了 balloon 两层直观意思：那只鼓鼓的球，以及像它一样越涨越大的过程。预算、债务也能这样“鼓起来”。',
 '意大利 palla 球 + 增大材料 -one → pallone 大球，法语 ballon 等影响英语形式。早期指大充气球及球戏，后来指飞行气球、玩具气球，再有膨胀动词。',BALLOON,
 'a balloon 是一只气球；a hot-air balloon 是热气球；costs balloon 是费用大涨。动词并非每次都与飞行有关。',
 'a red balloon；a hot-air balloon；costs balloon。',
 'balloon 作动词突出鼓起、膨胀；fly 只说飞。名词的第二音节重读，前面读轻音 /bə/。',
 ('A red balloon floated above the table.','一只红气球飘在桌子上方。'),('Costs can balloon if the project keeps expanding.','项目若不断扩张，费用可能大幅膨胀。'),sources=S('balloon','balloon'))
W('balloons','英 /bəˈluːnz/；美 /bəˈlunz/','气球〔复数〕；膨胀、激增〔第三人称单数〕',
 '房间里挂着几只 balloons，是气球；the budget balloons 则是预算像气球一样鼓大。句子位置把名词和动词分开。',
 'balloon + -s → balloons，词尾 /n/ 后加 /z/；名词复数与动词第三人称单数同形。',BALLOON+[['balloon + -s → balloons','多个气球；或单数主语发生膨胀']],
 'party balloons 是派对气球；the budget balloons 是预算暴涨。不要看到 s 就一律按名词复数读句子。',
 'party balloons；colourful balloons；the budget balloons。',
 'balloons are 表示气球们怎样；the budget balloons 中 balloons 是谓语，不再另加 is 来凑动词。',
 ('The children decorated the room with balloons.','孩子们用气球装饰了房间。'),('The budget balloons whenever another feature is added.','每多加一个功能，预算就大涨一截。'),sources=S('balloons','balloon'))
W('ballooned','英 /bəˈluːnd/；美 /bəˈlund/','膨胀了；激增了〔过去式、过去分词〕',
 '原来一小笔费用，后来涨成一大笔，可以说 ballooned。像气球被吹大一样，变化本身就是重点。',
 'balloon + -ed → ballooned，后缀 /d/；整个气球名先转成膨胀动词，现代再接过去式后缀。',BALLOON+[['balloon + -ed → ballooned','过去式、过去分词；词尾 /nd/']],
 'costs ballooned 是费用激增；ballooned from A to B 说从一个数涨到另一个数；ballooned into 说膨胀成某种规模。',
 'costs ballooned；ballooned from A to B；ballooned into a major expense。',
 'increased 只是增加；ballooned 通常更形象，也更容易暗示增长很大、很难控制。',
 ('The repair bill ballooned from fifty pounds to two hundred.','修理费从五十英镑猛涨到了两百英镑。'),('The small project ballooned into a year-long undertaking.','这个小项目越做越大，成了持续一年的工程。'),sources=S('ballooned','balloon'))
W('ballooning','英 /bəˈluːnɪŋ/；美 /bəˈlunɪŋ/','正在膨胀、激增；气球飞行活动',
 'ballooning costs 是费用越来越鼓，hot-air ballooning 则是乘热气球飞行。这两个常见用法都保留 balloon 的气球背景。',
 'balloon + -ing → ballooning。动词的膨胀用法形成分词；飞行活动也可用 -ing 名词形式，不能把所有 -ing 都只译成“正在”。',BALLOON+[['balloon + -ing → ballooning','膨胀过程、分词修饰语；也用作气球飞行活动名']],
 'ballooning costs 描述不断膨胀的费用；go ballooning 是去体验气球飞行。具体名词和句型区分两义。',
 'ballooning costs；ballooning demand；hot-air ballooning。',
 'ballooning demand 常说需求迅速增长；hot-air ballooning 才明确说飞行活动，前者不能按字面译成气球需求。',
 ('The team struggled to control ballooning costs.','团队费力控制不断膨胀的费用。'),('We tried hot-air ballooning during the holiday.','假期里我们体验了热气球飞行。'),sources=S('ballooning','balloon'))
W('workout','英 /ˈwɜːkaʊt/；美 /ˈwɝkaʊt/','一场锻炼；训练',
 '换上运动鞋，专门练上二十分钟，这一场运动可以叫 a workout。它把 work out 的训练用法打包成一次可数活动。',
 'work + out 的动词短语相关形式名词化为 workout；早期英语名词记录联系拳击训练，后来用于一般体育锻炼。具体记录并非要求现代每次短语义都先于所有名词义。',WORKOUT,
 'a quick workout 是短时间锻炼；a full-body workout 是全身训练；after a workout 是锻炼后。名词常在前面重读。',
 'a morning workout；a quick workout；after a workout。',
 'workout 是一个词的名词；work out 是两个词的动词短语。work out a problem 还能说解题，不能把这个意思随便套给 a workout。',
 ('I fitted in a quick workout before breakfast.','早饭前我挤时间锻炼了一会儿。'),('That long climb gave my legs a good workout.','那段长长的攀登让我的双腿好好活动了一番。'),sources=S('workout','workout'))
W('workouts','英 /ˈwɜːkaʊts/；美 /ˈwɝkaʊts/','多次锻炼；训练课、训练安排〔复数〕',
 '周一一场、周三一场，几次锻炼就是 workouts。数的是一场场活动，也可以按内容谈不同训练。',
 'workout + -s → workouts，末尾 /t/ 后读 /s/；复合名词在整体末尾加复数。',WORKOUT+[['workout + -s → workouts','多次锻炼，后缀接整个名词']],
 'home workouts 是居家锻炼；short workouts 是短时训练；three workouts a week 数每周三次。',
 'home workouts；short workouts；three workouts a week。',
 'she works out 的 s 加在动词 work 上；her workouts 的 s 加在闭合名词 workout 上。词与短语的句法位置不同。',
 ('She prefers short workouts at home.','她更喜欢在家做短时间锻炼。'),('We planned three workouts for the week.','我们为这一周安排了三次锻炼。'),sources=S('workouts','workout'))
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_zij',ROOTS,WORDS)
 extend_lessons()
