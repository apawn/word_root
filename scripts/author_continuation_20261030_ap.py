"""Pack and spring: bundles and things that emerge or rebound."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
PA=[['中古英语 pak、pakke → pack','包、捆；与荷兰语等日耳曼同族词有关，直接传入路径有不同分析'],['现代 pack','一包、一群；装包、挤满；压紧']]
def P(f,m):return PA+[[f,m]]
W('pack','/pæk/','包、捆；一组、一群；打包、装满、挤满',
 '把东西收在一起成为一包；人、动物密密聚在一起，也能借这个整体感理解。',
 '接中古英语 pak、pakke，近源与低地日耳曼语同族词相连，也有承接本族旧形的分析。动词从包、捆名词发展；不要把所有群体都当成真装在袋里。',PA,
 'pack a bag 收拾包，a pack of cards 一副牌，a pack of wolves 一群狼，a packed train 挤满人的列车。',
 'pack a bag；a pack of cards；a pack of wolves；pack into。',
 'pack 收拾、密装，wrap 包裹外层；可以先 wrap a gift，再 pack it in a box。a pack of dogs 不能泛用于所有动物群。',
 ('I need to pack my bag before dinner.','我得在晚饭前收拾好包。'),('People packed into the small hall.','人们挤进了小礼堂。'))
W('packing','/ˈpækɪŋ/','打包、装箱；包装填料',
 '既可以说把东西往箱里收的过程，也可以说塞在空隙里保护物品的材料。',
 'pack + -ing，中古英语已有对应名词。活动和材料两种用法都接装包、装填。',P('pack + -ing → packing','装包过程；填塞、保护用的材料'),
 'finish the packing 收拾完行李，packing material 包装填料，a packing list 装箱清单。',
 'finish the packing；packing material；a packing list。',
 'packing 常着眼收拾、装填；packaging 常着眼产品包装及其材料、外观。范围重合，不是一条绝对边界。',
 ('The packing took longer than the journey.','收拾行李花的时间比旅程还长。'),('Keep the packing material in case you need to return the item.','保留包装填料，以防需要退货。'))
W('packer','英 /ˈpækə/；美 /ˈpækər/','打包、装箱工；包装者；打包设备',
 '做 pack 这个动作的人或机器：把货物收好、装入包装。',
 'pack + -er，中古英语已有相应人物词。后缀按执行动作命名，既可人也可设备。',P('pack + -er → packer','执行打包、装箱的人或机器'),
 'a warehouse packer 仓库包装工，a meat packer 肉类加工包装者、企业，an automatic packer 自动包装机。',
 'a warehouse packer；an automatic packer；work as a packer。',
 'packer 打包者，package 包裹或包装动作；a packer 不能直接当一件包裹的普通名称。',
 ('The packer checked each box before sealing it.','包装工封箱前检查了每个箱子。'),('An automatic packer handles the smaller products.','小件产品由一台自动包装机处理。'))
W('package','/ˈpækɪdʒ/','包裹；包装；一整套方案；把……包装',
 '一个外包装收着东西是一件 package；把几项服务一起卖，也是一套 package。',
 '现代可认作 pack + -age；历史形成可能受荷兰语 pakkage 或相关欧陆形式影响，不宜断言只在英语内临时造出。名词后来也作动词。',P('pack + -age；可能有欧陆同族形式影响 → package','包裹、整套事物；后作包装动词'),
 'a small package 小包裹，a holiday package 套装旅游产品，a software package 软件包，package the goods 包装货物。',
 'a small package；a holiday package；a software package；package the goods。',
 'package 是包裹或一套组合，pack 还常作装包、群体；parcel 在英式英语常指邮寄包裹，不涵盖所有方案组合义。',
 ('A package arrived for you this morning.','今天早上有个包裹寄给你。'),('The hotel offers a package that includes breakfast and parking.','酒店提供包含早餐和停车的一套服务。'))
W('packaging','/ˈpækɪdʒɪŋ/','包装过程；包装材料、外包装；形象包装',
 '产品外面那层保护、展示它的东西，以及把它做成这样的一整套过程。',
 'package 去末尾 e + -ing。由包装活动延伸到材料、设计，也可借指产品或人物被呈现出来的形象。',P('package + -ing → packaging','包装活动 → 材料、外观和呈现方式'),
 'recyclable packaging 可回收包装，excessive packaging 过度包装，product packaging 产品包装。',
 'recyclable packaging；excessive packaging；product packaging。',
 'packaging 常不可数，a package 是一件包裹或一套产品。Remove the packaging 说拆掉外包装，不一定丢掉产品本身。',
 ('The company reduced the amount of plastic packaging.','公司减少了塑料包装用量。'),('The simple packaging makes the product easy to recognize.','简洁的包装让产品很容易辨认。'))
W('unpack','/ʌnˈpæk/','拆包；取出行李；逐层分析、解释',
 '把装在一起的东西拿出来摊开；复杂想法也可以像开箱一样，一层层展开讲。',
 'un- 逆转 + pack，中古英语已有 unpakken。分析义借解除压缩、展开内容的形象，不表示每次必须有真实箱子。',P('un- + pack → unpack','解除装包 → 取出；展开分析'),
 'unpack a suitcase 打开行李箱取出东西，unpack an argument 拆开分析一个论点。',
 'unpack a suitcase；unpack the boxes；unpack an argument。',
 'unpack 是解包、展开，repack 是重新装回或重装。unpack an idea 常是解释内含假设、各层意思。',
 ('I unpacked my suitcase as soon as I got home.','一到家我就把行李箱里的东西拿了出来。'),('Let’s unpack what that claim actually means.','我们来逐层看看那个说法到底是什么意思。'))
W('repack','/ˌriːˈpæk/','重新打包、装箱',
 '已经装过一次，现在换箱、调整顺序或再收好一遍。',
 're- 再次 + pack，重音主要在 pack。词首 re- 在这里确实表示重新，不同于 rebar 的缩合来源。',P('re- + pack → repack','再次打包、重新装入'),
 'repack a suitcase 重新整理行李箱，repack the goods 重新包装货物。',
 'repack a suitcase；repack the goods；repack into smaller boxes。',
 'unpack 把东西取出，repack 再装；可以先 unpack 检查，再 repack 寄走。',
 ('She repacked her suitcase to make room for the books.','她重新整理行李箱，给书腾出空间。'),('The goods were repacked into smaller boxes.','货物被重新装进了较小的箱子。'))
W('wolfpack','/ˈwʊlfpæk/','狼群；像狼群般协同行动的一组〔比喻〕',
 '不是零散一只狼，而是一群一起生活、行动的狼；比喻也取成组协作或围攻。',
 'wolf 狼 + pack 群体。军事等领域有专门的群攻用法，先由动物和常见比喻理解，不展开冷门型号。',P('wolf + pack → wolfpack','狼群；引申成组协同行动'),
 'a wolfpack in the forest 林中的狼群；也常写成两词 a wolf pack。',
 'a wolfpack；a wolfpack moving together；wolfpack tactics。',
 'wolfpack 与 a wolf pack 常对应同一概念；pack 群体用法并非保证所有成员同时在猎食。',
 ('The camera recorded a wolfpack crossing the snow.','摄像机拍到一群狼穿过雪地。'),('The documentary follows a wolfpack through the winter.','纪录片跟拍一群狼度过冬天。'))
W('snowpack','/ˈsnəʊpæk/〔英〕；/ˈsnoʊpæk/〔美〕','积雪层；地面积雪',
 '多场雪叠在地面上，逐渐成为一整层积雪；关注的是累积起来的雪体。',
 'snow 雪 + pack 堆积、压在一起的整体。不是装雪用的背包。',P('snow + pack → snowpack','多层累积的地面积雪'),
 'mountain snowpack 山地积雪，a deep snowpack 厚积雪，melting snowpack 正在融化的积雪层。',
 'mountain snowpack；a deep snowpack；melting snowpack。',
 'snowfall 说下雪或降雪量，snowpack 说地上累积的雪体；一场新雪只是已有 snowpack 的一部分。',
 ('The mountain snowpack began to melt in April.','山地积雪在四月开始融化。'),('Researchers measured the depth of the snowpack.','研究人员测量了积雪层的厚度。'))
R('B3779','包成整体、装入和压紧；再到群体与积雪','PACK：收拢在一起成为一包、一组或一层','pack → packing、packer；package → packaging 连读；unpack/repack 分拆开和重装；backpack 已有精讲。',
 '核心是收在一起的整体。包裹、套装、动物群体和积雪并非同一个物品，但都能用整体感帮助认义。',
 'pack + -ing/-er/-age；package + -ing；un-/re- + pack；back/wolf/snow + pack。',
 [['打包与执行者','pack · packing · packer'],['包裹与包装','package · packaging'],['拆开与重装','unpack · repack'],['不同整体','backpack · wolfpack · snowpack']],
 'package 包裹、套装与 packaging 包装材料分清；unpack 也可展开分析；snowfall 下雪、snowpack 积雪。',
 'Unpack the package, keep the packaging, and repack it if necessary.\n\n拆开包裹，留好包装，必要时再装回去。',
 'pack packing packer package packaging unpack repack backpack wolfpack snowpack')
SP=[['古英语 springan → 中古英语 springen → spring','跳起、涌出、萌发'],['相关旧名词及后续发展','跳跃、泉源；植物萌发的季节与弹性构件等支线']]
W('spring','/sprɪŋ/','春天；泉水、泉源；弹簧；跳起、突然出现',
 '抓住往外冒、一下弹起来：水从地下涌出，芽从土里冒出，弹簧压下又回弹。',
 '动词接古英语 springan 跳、涌出、萌发；名词也有旧泉源、跳跃等形式，并非全是现代动词临时转成。春季名称联系萌发生长，后来独立为季节名。',SP,
 'in spring 在春天，a hot spring 温泉，a mattress spring 床垫弹簧，spring to your feet 一下站起来。动词常见 sprang、sprung。',
 'in spring；a hot spring；a mattress spring；spring to life。',
 'spring 春天、泉水、弹簧靠语境区分；spring water 泉水不等于只在春天生产的水。',
 ('She sprang to her feet when the bell rang.','铃一响，她一下站了起来。'),('The village gets its water from a natural spring.','村庄从一处天然泉眼取水。'),sources=['https://www.etymonline.com/word/spring','https://en.wiktionary.org/wiki/spring#English'])
W('springy','/ˈsprɪŋi/','有弹性的；轻快有劲的',
 '踩下去压得动，松开又弹回来；人的步子也可像装了弹簧一样轻快。',
 'spring + -y，常接弹簧、弹性义。另有较少见的春季、泉多等用法，先掌握材料弹性与动作轻快。',SP+[['spring + -y → springy','如弹簧般回弹；步态轻快']],
 'springy grass 有弹性的草地，springy cushions 回弹好的垫子，a springy step 轻快步子。',
 'springy grass；springy cushions；a springy step。',
 'springy 强调压过能弹回，soft 只说软；一团软泥 soft 却不一定 springy。',
 ('The grass felt soft and springy under our feet.','脚下的草又软又有弹性。'),('He walked into the room with a springy step.','他迈着轻快的步子走进房间。'))
W('offspring','英 /ˈɒfsprɪŋ/；美 /ˈɔːfsprɪŋ/','子女；后代；产物〔比喻〕',
 '从上一代生出来、延续下去的一代；重点是生命或成果的来源关系。',
 '古英语 ofspring 经中古英语延续，现代对应 off- + spring。spring 保留生出、涌出的联系；off- 不是坏掉的开关状态。',SP[:1]+[['古英语 ofspring → 中古英语 ofspring → offspring','从上一代生出的后代；后可比喻产物']],
 'their offspring 他们的子女，produce offspring 繁殖后代。单复数同形：one offspring、several offspring。',
 'their offspring；produce offspring；healthy offspring。',
 'offspring 是后代，spring 春季只是同族另一支；别把 offspring 拆成离开春天。descendant 后裔常着眼代际关系。',
 ('The birds worked together to feed their offspring.','两只鸟一起喂养幼鸟。'),('The study followed the animals and their offspring.','研究持续观察这些动物及其后代。'))
R('B2447','跳起、涌出、萌发；泉、春天、弹簧与后代','SPRING：向外涌出、向上弹起、生长出来','spring 分动作、泉源、季节、弹性几路；springy 接回弹，offspring 接后代；已有 springtime、springboard、wellspring 共享。',
 '同族名词与动词都有古老形式，不把所有名词强说成一条现代新造线；用冒出、弹起帮助理解即可。',
 'spring + -y；off- + spring 的旧组合；spring + time/board；well + spring。',
 [['基本动作与回弹','spring · springy'],['季节、泉源和借力点','springtime · wellspring · springboard'],['后代','offspring']],
 'spring water 泉水不是春水；springy 回弹不只软；offspring 单复数同形，off- 不接离开春天。',
 'In spring, the birds raise their offspring near a natural spring.\n\n春天，鸟儿在天然泉眼附近养育后代。',
 'spring springy springtime wellspring springboard offspring')
if __name__=='__main__':save('continuation_20261030_ap',ROOTS,WORDS)
