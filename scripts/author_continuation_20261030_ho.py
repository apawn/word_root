"""Pans, managed servers, breast compounds and two different hops."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
W('pan','/pæn/','平底锅、盘状容器；淘洗；严厉批评；摇镜头〔另一路〕',
 '厨房里是宽口容器，淘金时用浅盘淘洗；镜头 pan across 却是转向扫过景物，来自 panorama 全景的缩短。',
 '锅义接古英语 panne，远源有拉丁借词等解释，细节不全确定。严厉批评常联系把人放锅上煎烤的旧俚语画面；镜头动作 pan 则缩短自 panorama，来源另分。',
 [['古英语 panne → pan','锅、浅盘类容器 → 淘洗等用法'],['批评义的俚语扩展','被煎烤般挨批的形象，具体联系带推测性'],['panorama → pan','全景名词截短 → 镜头扫过、视图平移']],
 'a frying pan 煎锅，pan for gold 用浅盘淘金，critics panned the film 评论者猛烈批评影片，pan across the room 镜头扫过房间。pan out 也常说事情最后有何结果。',
 'a frying pan；pan for gold；pan a film；pan across；pan out。',
 'pan 锅不等于希腊组合成分 pan- 全部；拍摄时 pan 通常是转动视线方向，zoom 改变画面取景尺度。电脑视图 pan 是平移，不是缩放。',
 ('Heat the oil in a large frying pan.','在大煎锅里把油加热。'),('The camera panned across the crowded square.','镜头扫过拥挤的广场。'),('The critics panned the film, but audiences enjoyed it.','影评人把电影批得很厉害，观众却很喜欢。'),sources=['https://en.wiktionary.org/wiki/pan#English','https://www.etymonline.com/word/pan'])
R('B4598','锅、盘状容器，和镜头全景动作的同形词','PAN：先辨厨房的盘，还是 panorama 缩出来的镜头动作','pan/pancake/saucepan 保留器皿；panhandle、deadpan 各有固定比喻；镜头 pan 来自另一缩短路线。',
 '相同字母不必把全部意思搅进一只锅。锅的实物组合容易看，俚语和截短要分别追来源。',
 'panne → pan；pan + cake/handle；sauce + pan；dead + pan〔脸的俚语〕；panorama → pan。',
 [['容器与相关食物','pan · saucepan · pancake'],['形状和表情的固定词','panhandle · deadpan']],
 'panorama 缩短的 pan 与锅分支分开；deadpan 是面无表情，不是坏掉的锅；panhandle 的地形、乞讨用法须按上下文分。',
 'The camera panned across the kitchen as she lifted the pan.\n\n她拿起锅时，镜头扫过厨房。','pan saucepan pancake panhandle deadpan')
W('serverless','英 /ˈsɜːvələs/；美 /ˈsɜːrvərləs/','无服务器的〔常指开发者无需管理底层服务器的计算模式〕',
 '像租用已经有人维护的厨房：你提交要做的工作，平台安排机器来跑。叫 serverless，不代表世界上真没有服务器。',
 'server 服务器 + -less 无、无需。云计算用法把镜头放在开发者体验：底层服务器管理交给提供方；某些其他场景也可字面说没有中央服务器。',
 [['serve + -er → server','提供服务者 → 计算机服务端'],['server + -less → serverless','无服务器；云语境常指无需自己管理底层服务器']],
 'serverless computing 无服务器计算，a serverless function 无服务器函数，a serverless application 无服务器应用。具体能力、计费和运行限制随服务而异。',
 'serverless computing；a serverless function；a serverless application。',
 'serverless 不等于免费、不用运维任何应用问题；也不等于所有代码都只能是小函数。它说明基础设施责任如何分配，不说明代码功能。',
 ('The team used a serverless function to process uploaded images.','团队用无服务器函数处理上传的图片。'),('In this serverless setup, the provider manages the underlying servers.','在这套无服务器方案里，提供方管理底层服务器。'),sources=['https://en.wiktionary.org/wiki/serverless#English','https://aws.amazon.com/serverless/faqs/','https://cloud.google.com/discover/what-is-serverless-computing'])
R('B4082','提供服务的服务器，与无需自行管理服务器的模式','SERVERLESS：服务还在，底层机器管理交给提供方','server 提供服务；serverless 的云语境强调开发者不用自己配置、维护底层服务器。',
 '后缀 -less 在这里不能脱离使用视角。机器仍在运行，只是责任分工变了；这比逐字记无服务器更容易理解。',
 'serve + -er → server；server + -less → serverless。',
 [['服务提供与管理视角','server · serverless']],
 'serverless 不是没有物理机器，不保证免费，也不免除应用自身的设计和维护工作。',
 'A serverless application still runs on servers managed by someone.\n\n无服务器应用仍运行在有人管理的服务器上。','server serverless')
B=[['古英语 brēost → 中古英语 brest → breast','胸部、身体前侧；乳房'],['英语组合和比喻','胸前、喂养、并排向前及游泳动作']]
W('breast','/brest/','乳房；胸部、胸前；禽类胸肉',
 '核心位置在身体前上方。人身上可具体说乳房，也可广说胸前；鸡肉柜台上的 chicken breast 则是胸肉。',
 '接古英语 brēost、日耳曼语胸部词族，不是 breathe 呼吸的过去式。旧的胸部前侧含义保留在盔甲、衣服、并排等组合里。',B,
 'breast milk 母乳，breast cancer 乳腺癌，chicken breast 鸡胸肉，a breast pocket 胸前口袋。文学里胸中也可承载感情。',
 'breast milk；chicken breast；a breast pocket；breast cancer。',
 'chest 通常广指胸部、胸腔；breast 在现代人体语境常更具体指乳房，但不能把所有组合都这样译。breast pocket 是胸袋。',
 ('The jacket has a small breast pocket.','夹克胸前有一个小口袋。'),('She sliced the chicken breast for the salad.','她把鸡胸肉切片放进沙拉。'))
W('breastfeeding','/ˈbrestfiːdɪŋ/','母乳喂养、哺乳',
 'breast 提供乳汁，feeding 是喂养过程；合在一起指用乳房分泌的乳汁喂养孩子这一方式。',
 '对应 breast + feeding，也可看作 breastfeed 的 -ing 形式。feeding 来自 feed，不是 eating 吃饭直接加前半。',B+[['breast + feed → breastfeed','以母乳喂养'],['breastfeed + -ing → breastfeeding','哺乳的活动、过程；也作相关定语']],
 'breastfeeding support 母乳喂养支持，a breastfeeding mother 正在哺乳的母亲，during breastfeeding 哺乳期间。',
 'breastfeeding support；a breastfeeding mother；during breastfeeding。',
 'breastfeeding 通常说喂养方式或过程；breast milk 是乳汁本身。婴儿 feeding 还可有其他方式，不能一概译母乳喂养。',
 ('The centre offers breastfeeding support to new parents.','中心为新手父母提供母乳喂养支持。'),('The article discusses returning to work during breastfeeding.','文章讨论了哺乳期间重返工作的问题。'))
W('breasted','/ˈbrestɪd/','有某种胸部、胸前覆盖形态的',
 '看胸前长什么样或怎么覆盖：鸟胸是什么颜色、外套前襟怎么排扣，都能借这个部位命名。',
 'breast + -ed，-ed 表具有。通常接在描述成分后组成修饰语；词尾读 /ɪd/，和 breast 末尾的 /t/ 分开成音节。',B+[['breast + -ed → breasted','具有某种胸部或胸前覆盖形式的']],
 'a red-breasted bird 红胸鸟，a single-breasted jacket 单排扣夹克，a double-breasted coat 双排扣外套。服装义抓前襟结构，不是人体数量。',
 'a red-breasted bird；a single-breasted jacket；a double-breasted coat。',
 'breasted 一般不独立夸人有胸；服装 single/double-breasted 说前襟、扣列样式，不能按乳房的个数理解。',
 ('He wore a single-breasted jacket to the interview.','他穿了一件单排扣夹克去面试。'),('A red-breasted bird landed on the fence.','一只红胸鸟落在围栏上。'))
W('abreast','/əˈbrest/','并排向前；与……齐平；及时了解、不落后于',
 '几个人胸前齐在一条线上，并肩往前走；知识也能这样跟上新变化，不让自己落到后面。',
 '接中古英语 abrest，可对应 a- 在、处于 + breast 胸部，胸前齐平。a- 在这里不是否定；从位置齐平扩展到信息跟得上。',B+[['a- + breast → abreast','胸部齐在一线 → 并排、齐平'],['keep abreast of','与新情况齐步 → 及时掌握']],
 'walk two abreast 两人并排走，keep abreast of developments 随时掌握进展，stay abreast of the news 跟上新闻。',
 'two abreast；keep abreast of；stay abreast of developments。',
 'abreast 是并排、齐平或信息跟上，不是拥抱；keep abreast of 比单纯知道一点更强调持续跟进。',
 ('The path was wide enough for us to walk two abreast.','小路够宽，我们能两人并排走。'),('She reads the reports to keep abreast of developments.','她阅读报告，以便随时掌握进展。'))
W('breaststroke','英 /ˈbreststrəʊk/；美 /ˈbreststroʊk/','蛙泳',
 '泳姿名称抓胸朝水面这一侧、手臂在身体前方划开的动作；中文则抓腿部像青蛙的画面，两种语言取的角度不同。',
 'breast 胸部 + stroke 一次划动、泳式。stroke 在这里不是中风；这个词是泳姿名称，不能靠拆词替代规范动作教学。',B+[['breast + stroke → breaststroke','胸部朝下的传统泳式命名 → 蛙泳']],
 'swim breaststroke 游蛙泳，the 100 metres breaststroke 百米蛙泳，a breaststroke event 蛙泳项目。',
 'swim breaststroke；the 100 metres breaststroke；a breaststroke event。',
 'breaststroke 译蛙泳；backstroke 是仰泳。freestyle 是自由泳项目名称，不等于 breaststroke 的反义词。',
 ('She usually swims breaststroke at the pool.','她在泳池通常游蛙泳。'),('He entered the 100 metres breaststroke.','他报名参加了百米蛙泳。'))
R('B3204','胸部、身体前上方，以及由这个位置形成的组合','BREAST：先定位胸前，再看喂养、衣襟、并排和泳姿','breast → breastfeed/breastfeeding；breasted 看胸前形态；abreast 胸前齐平；breaststroke 是泳式名。',
 '现代人体义常说乳房，但较广的胸部位置仍活在组合里。胸袋、胸甲、双排扣都应回到物体结构理解。',
 'brēost → breast；breast + feed/-ed/stroke/plate；a- + breast → abreast。',
 [['部位与保护、喂养','breast · breastplate · breastfeed · breastfeeding'],['外形、齐平和泳式','breasted · abreast · breaststroke']],
 'breast/chest 范围不同；single-breasted 不说人体数量；abreast 的 a- 不是否定；stroke 在泳式里是划动。',
 'They walked two abreast to watch the breaststroke event.\n\n他们两人并排走去看蛙泳比赛。',
 'breast breastplate breastfeed breastfeeding breasted abreast breaststroke')
H=[['古英语 hoppian → hop','短跳、单脚跳 → 快速短途移动'],['另一路中古荷兰语 hoppe → 英语 hop','啤酒花植物及其花，不从跳跃义变来']]
W('hop','英 /hɒp/；美 /hɑːp/','短跳、单脚跳；快速去、短程移动；啤酒花〔另源〕',
 '小鸟一跳一跳，或人很快从这里到隔壁，是跳跃那一路；配料表里的 hops 却是啤酒花，不是会跳的花。',
 '跳跃接古英语 hoppian；植物义借中古荷兰语 hoppe。两条来源分开。动词过去式 hopped、-ing 形式 hopping 双写 p，与 hope/hoped/hoping 不同。',H,
 'hop on one foot 单脚跳，hop on a bus 赶快上公交，a short hop 很短一段行程，hops used in brewing 酿造用啤酒花。',
 'hop on one foot；hop on a bus；a short hop；hops。',
 'hop 和 hope 希望元音、拼写变化不同；hops 植物配料不能只按跳跃复数理解。hop 网络一跳也是一步转发的比喻。',
 ('The child hopped across the room on one foot.','孩子单脚跳着穿过房间。'),('The brewery grows some of its own hops.','这家酿酒厂自己种了一部分啤酒花。'))
W('hopper','英 /ˈhɒpə/；美 /ˈhɑːpər/','跳跃者、跳跃昆虫；料斗、漏斗形储料装置；斯里兰卡碗形薄饼〔另源〕',
 '人物或昆虫可以一跳一跳；机器里的 hopper 常是上面装料、下面逐渐放料的容器。餐馆 hoppers 又可能是一种薄饼。',
 '跳跃、料斗词对应 hop + -er，历史有早期跳跃者形式；料斗名称常联系旧装置进料时跳动的形象。斯里兰卡食物名借当地语言，远接泰米尔语 appam，分源。',H[:1]+[['hop + -er 等相应旧形式 → hopper','跳跃者；进料、储料容器'],['僧伽罗语 āppa 等 → 食物 hopper','碗形薄饼，独立借词']],
 'a grain hopper 谷物料斗，fill the hopper 把料斗装满，a hopper window 下边铰接、向内倾开的窗；食品场景则看餐单。',
 'a grain hopper；fill the hopper；a hopper window。',
 '机器 hopper 是容器或装置，不是操作者；food hopper 也可能是食品加工机料斗，不能看到 food 就默认斯里兰卡薄饼。',
 ('The machine feeds grain from a hopper into the mill.','机器把谷物从料斗送进磨机。'),('The operator checked that the hopper was empty.','操作员检查确认料斗已经空了。'))
W('hoppy','英 /ˈhɒpi/；美 /ˈhɑːpi/','啤酒花风味明显的；跳跳蹦蹦的〔另一义〕',
 '饮品描述里说 hoppy，是啤酒花的香气、苦味等特征比较突出；描述动作时才可能是一跳一跳。',
 'hop + -y，双写 p；但 hop 本来有植物和跳跃两条来源，所以同样的后缀形式也有两支。',H+[['hop + -y → hoppy','啤酒花性质明显；或有跳跃动作的']],
 'a hoppy beer 啤酒花味明显的啤酒，a hoppy aroma 啤酒花香；具体风味还取决于品种、加工和配方。',
 'a hoppy beer；a hoppy aroma；a hoppy character。',
 'hoppy 不只是 bitter 苦：也可突出花、果或草本等香气；hoppy 与 happy 开心的只有一个字母之差，读音不同。',
 ('The menu describes this beer as light and hoppy.','菜单把这款啤酒描述为口感轻、啤酒花风味明显。'),('He noticed a hoppy aroma before taking a sip.','他喝之前就闻到了明显的啤酒花香。'))
W('hopscotch','英 /ˈhɒpskɒtʃ/；美 /ˈhɑːpskɑːtʃ/','跳房子游戏；跳来跳去地移动',
 '地上画格子，单脚或双脚按规则跳；hop 是跳，后半是画出的格线，不是喝一口苏格兰酒再跳。',
 'hop 跳 + scotch 划痕、划线的旧义。游戏因在地面划出的格子里跳而得名，不是由 Scottish 苏格兰的直接拼接。',H[:1]+[['hop + scotch〔划线、划痕〕→ hopscotch','在划出的格子中跳的游戏']],
 'play hopscotch 玩跳房子，a hopscotch grid 跳房子格子；动词也可比喻在相邻地点间跳来跳去。',
 'play hopscotch；a hopscotch grid；a game of hopscotch。',
 'scotch 在这个合成词里取划线旧义；和 Scotch whisky 苏格兰威士忌的专名用法分开。游戏规则可有不同版本。',
 ('The children drew a hopscotch grid in chalk.','孩子们用粉笔画了跳房子的格子。'),('We played hopscotch in the school playground.','我们在学校操场玩跳房子。'))
R('B3499','跳跃和啤酒花两条同形词路线','HOP：会跳的动作，与酿造的植物分开','hop → hopper/hopscotch 抓跳跃；hops → hoppy 抓植物风味；食物 hopper 是又一路借词。',
 '先看动作还是材料。hoppy 在两条来源上都能加 -y，不能因为拼法一致就画出跳跃变成啤酒花的假路线。',
 'hoppian → hop；hop + -er/scotch；另线 hoppe → 植物 hop；hop + -y。',
 [['跳跃、装置与游戏','hop · hopper · hopscotch'],['植物风味','hoppy']],
 'hop/hope 读音和加词尾规则不同；hopper 料斗不是操作员；hoppy 不只说苦；hopscotch 不由苏格兰酒命名。',
 'The children played hopscotch while the guide explained how the grain hopper worked.\n\n孩子们玩跳房子时，讲解员正在介绍谷物料斗如何工作。',
 'hop hopper hoppy hopscotch')
if __name__=='__main__':save('continuation_20261030_ho',ROOTS,WORDS)
