"""Bust homographs, communist and leaf."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
B=[['burst 的方言、口语变化 → bust','破开、弄坏；再有查获、失败等口语义'],['法语 buste、意大利 busto → bust 名词','躯干、半身像；胸部、胸围'],['两条词源的派生','busted、buster 多接破坏、查获；busty 接胸部']]
W('bust','/bʌst/','弄坏；查获、逮捕〔口语〕；失败；半身像；胸部、胸围',
 'bust a machine 是弄坏机器，a police bust 是一次查获行动；博物馆里的 a bust 却是半身像，服装尺寸里的 bust 则是胸围。先分破坏动作和身体名词。',
 '弄坏的动词是 burst 的方言、口语变化形式；半身像、胸部名词借法语 buste、意大利 busto，更远来源有争议。不是每种意义都从打破东西长出来。',B,
 'bust a myth 破除迷思，a police bust 查获行动，go bust 破产、倒闭，a marble bust 大理石半身像，bust measurement 胸围尺寸。',
 'bust a myth；go bust；a marble bust；bust measurement。',
 'a bust 的失败、雕像两义靠上下文分；bust measurement 不是身体被打坏。bust 与 burst 有历史联系，但现代固定搭配不全部互换。',
 ('The museum displays a marble bust of the poet.','博物馆展出那位诗人的大理石半身像。'),('The small company went bust after losing its main customer.','失去主要客户后，小公司倒闭了。'))
W('busted','/ˈbʌstɪd/','坏掉的；被逮住、被抓现行的〔口语〕',
 '手机坏了可以说 busted；偷偷做事被发现，也会说 Busted! 露馅了！它强调出问题或被识破的结果。',
 'bust + -ed；/t/ 后 -ed 读 /ɪd/。形容破损、被抓住常接破坏或查获那条来源；带胸部限定的另类用法则接身体名词。',B[:1]+[['bust + -ed → busted','弄坏、查获后的结果状态']],
 'a busted phone 坏手机，get busted 被抓、露馅，busted for cheating 因作弊被逮个正着。口语语气强，正式文字可按具体事件改用 broken、caught 等。',
 'a busted phone；get busted；busted for。',
 'busted 不总是被警方逮捕，家庭、学校里的抓现行也能用；设备 busted 则是坏了。',
 ('I cannot call you because my phone is busted.','我手机坏了，没法给你打电话。'),('He got busted sneaking biscuits before dinner.','晚饭前他偷吃饼干，被逮了个正着。'))
W('buster','英 /ˈbʌstə/；美 /ˈbʌstər/','破除、消灭、制服某物的人或东西；家伙〔称呼〕',
 '把某种麻烦打掉、压住的东西，可以用 buster 作名称成分。它可是真工具，也可是去压力、破迷思的活动。',
 '原与 burster 的方言变化有关，后也按 bust + -er 理解；-er 可以指人、工具、行动。称呼人的 Buster 则另有口语语气。',B[:1]+[['burster 的变化、bust + -er 的重分析 → buster','破除、制服者；口语人物称呼']],
 'a stress buster 减压的活动或东西，a myth buster 破除迷思的人或节目，Listen, buster! 喂，你听着！〔可带警告、戏谑〕。',
 'a stress buster；a myth buster；Listen, buster!。',
 'buster 不一定是暴力破坏者；stress buster 是帮忙缓解压力。直接称人 buster 要看语气，不是任何场合都友好。',
 ('A short walk can be a useful stress buster.','短暂散步可以是有效的减压方式。'),('The programme presents its host as a myth buster.','节目把主持人塑造成破除迷思的人。'))
W('busty','/ˈbʌsti/','胸部丰满的',
 '这是描述成年女性体形的词，具体说胸部丰满。它比较直白，不是泛指整个人体格高大或衣服宽松。',
 'bust 胸部名词 + -y 性质后缀；接身体名词那条来源，不接 bust 弄坏。',B[1:2]+[['bust 胸部 + -y → busty','胸部丰满的体形描述']],
 'a busty character 胸部丰满的角色，clothing for busty women 面向胸部丰满女性的服装。常见于人物描写、服装版型，语境决定是否合适。',
 'a busty character；clothing for busty women。',
 'busty 只说胸部特征，不等于 overweight 超重；busted 坏掉、被逮住也不是同一个形容词。',
 ('The novel describes the adult character as busty.','小说把那位成年角色描写为胸部丰满。'),('The designer adjusted the jacket for busty customers.','设计师为胸部丰满的顾客调整了夹克版型。'))
R('B2837','破坏、查获的动作线，与半身像、胸部的独立名词线','BUST：破坏这一线与身体这一线分开','bust → busted、buster 多看破坏、查获；busty 接胸部名词。',
 '短短四个字母有多种用途。用 go bust、marble bust、bust measurement 等搭配先定意思，再看词尾。',
 'burst 的变化 → 动作 bust；buste／busto → 半身像、胸部 bust；再各自派生。',
 [['基础的两条来源','bust'],['破坏、查获与执行者','busted · buster'],['体形性质','busty']],
 'busty 不等于 busted；半身像 bust 与弄坏东西的动词直接来源不同。',
 'The exhibit explains the difference between a marble bust and the phrase go bust.\n\n展览说明大理石半身像与 go bust 倒闭这个说法的区别。','bust busted buster busty')
C=[['法语 commun 共同的 + -iste → communiste','与共同所有、共产主义相关的支持者称呼'],['英语 communist','共产主义者；共产主义相关的形容词'],['communist + -ic → communistic','具有相应思想、制度特征的']]
W('communist','英 /ˈkɒmjʊnɪst/；美 /ˈkɑːmjənɪst/','共产主义者；共产主义的；共产党成员或党的〔依语境〕',
 '它可以指支持共产主义思想的人，也可以修饰相关政治运动、制度。核心涉及生产资料、阶级与社会安排，并非简单说个人所有物都随便共用。',
 '借法语 communiste，由 commun 共同的 + -iste 人物、立场形成；英语现代对应 commune／common 相关词族与 -ist。名词、形容词并用。',C[:2],
 'a communist thinker 共产主义思想家，communist theory 共产主义理论，a Communist Party 共产党。具体党派名称常大写，泛指思想、人物类别常小写，风格依文本。',
 'a communist thinker；communist theory；a Communist Party。',
 'communist 的思想支持者与某个特定党的正式成员并非每次都相同；community 社区、communal 公共共享的也不自动带同样政治身份。',
 ('The course examines communist theory in historical context.','课程在历史背景中考察共产主义理论。'),('The memoir describes the writer’s years as a communist.','回忆录描述了作者身为共产主义者的那些年。'))
W('communistic','英 /ˌkɒmjʊˈnɪstɪk/；美 /ˌkɑːmjəˈnɪstɪk/','共产主义性质的；具有共同所有等相应特征的',
 'communist 可直接命名人物、政治属性；communistic 更常把某个安排、理想当成具有这类特征来描述。是否赞同、批评，仍看上下文。',
 'communist + -ic，形容相应性质，也会与 communism 一组理解。重音移向 /nɪs/，不只在原词尾轻轻添个音节。',C,
 'communistic ideals 共产主义理想，a communistic arrangement 具有相应共同所有特征的安排。这个形容词相较 communist 在日常表达中更少见。',
 'communistic ideals；a communistic arrangement。',
 'communistic 是性质形容词，不能用 a communistic 当共产主义者的普通人物名词。只是共同生活，也不充分等于完整政治思想。',
 ('The historian discusses the group’s communistic ideals.','历史学家讨论了该团体的共产主义理想。'),('The essay describes the arrangement as communistic.','文章把这种安排描述为具有共产主义性质。'))
R('B3127','共产主义思想、人物与相应性质的形容词','COMMUNIST：人物、政治属性；COMMUNISTIC：相应性质','communist → communistic。',
 '思想、组织身份和某种安排的特征要按文本区分。共同拥有、公共使用的普通意思不自动形成同样政治标签。',
 '法语 communiste → communist；再接 -ic 形成 communistic。',
 [['人物、属性与性质','communist · communistic']],
 'communistic 不是通常人物名词；communist 思想支持与某党成员身份也不总相同。',
 'The chapter compares communist theory with arrangements described as communistic.\n\n这一章比较了共产主义理论与被描述为具有相应性质的安排。','communist communistic')
L=[['古英语 lēaf → 中古英语 lef／leef → leaf','植物叶片'],['片状外形的扩展','书中一张纸、金箔等薄片；翻动纸页'],['组合与后缀','leafy 多叶、leafless 无叶、leaflet 小叶或单页印品']]
W('leaf','/liːf/','叶子；纸张、薄片；长叶、翻页〔动词〕',
 '树上一片叶子薄而平，书里的一张纸、打得很薄的金箔也能借 leaf 命名。翻书就像翻这些薄片，形成 leaf through。',
 '承接古英语 lēaf，经中古英语 lef、leef 留传。普通复数 leaves /liːvz/，/f/ 变 /v/；动词 leafed、leafing 则保留 f。',L,
 'a green leaf 绿叶，gold leaf 金箔，leaf through a book 翻看一本书，turn over a new leaf 翻开新篇、改过自新。一本书的一 leaf 是一张纸，正反可有两个 page。',
 'a green leaf；gold leaf；leaf through；turn over a new leaf。',
 'leaf 纸张与 page 页面对照，一张纸有两面。leaves 也可能是 leave 离开的第三人称词形，需由句子分辨。',
 ('A yellow leaf fell onto the path.','一片黄叶落在小路上。'),('She leafed through the catalogue while waiting.','等候时她翻看了目录。'))
W('leafy','/ˈliːfi/','多叶的、枝叶繁茂的；绿树成荫的',
 '一片街区两旁树多叶密，看着满眼绿意，就可以说 leafy。它描述叶子、植被带来的外观。',
 'leaf + -y，保留 f；不是把复数 leaves 再加后缀。也可用于 leafy vegetables 叶菜类这一用途分类。',L+[['leaf + -y → leafy','叶多；具有叶片特征']],
 'a leafy street 绿树成荫的街道，a leafy neighbourhood 绿树多的社区，leafy vegetables 叶菜类蔬菜。英国报道中 leafy 地区有时还暗含较富裕住宅区印象，具体看语境。',
 'a leafy street；a leafy neighbourhood；leafy vegetables。',
 'leafy 不等于所有 green：绿色墙壁未必 leafy。leafy vegetables 则按主要食用叶片等特点称呼。',
 ('They walked along a quiet, leafy street.','他们沿着一条安静、绿树成荫的街道走。'),('The basket contained several leafy vegetables.','篮子里放着几种叶菜。'))
W('leaflet','/ˈliːflɪt/','传单、小册页；小叶、复叶中的小叶片',
 'leaf 加一个小的词尾，先是小叶、叶片单位；把书纸张那条 leaf 变小，又得到一张说明、宣传用的 leaflet。',
 'leaf + -let，小称后缀。植物与印刷品两条都能从 leaf 的常用意义理解，不必只认其中一个。',L+[['leaf + -let → leaflet','小叶、复叶小叶片；单页或折页信息印品']],
 'an information leaflet 说明折页，a travel leaflet 旅游宣传册页，leaflets of a compound leaf 复叶的小叶片。leaflet 作动词可说发传单。',
 'an information leaflet；a travel leaflet；distribute leaflets。',
 'leaflet 通常较薄、篇幅较短，与 brochure 用法有交叠，不用硬定每种只能多少页。植物义 leaflet 不等于所有叶芽。',
 ('The museum provides an information leaflet at the entrance.','博物馆在入口提供说明折页。'),('The compound leaf has several small leaflets.','这片复叶有几片小叶。'))
W('broadleaf','英 /ˈbrɔːdliːf/；美 /ˈbrɔːdliːf/','阔叶的；阔叶树等〔名词用法〕',
 '拿较宽平的叶片与针形叶相比，broadleaf 抓住的是叶形。常见 broadleaf trees 就是阔叶树。',
 'broad 宽的 + leaf 叶。相近形容词 broadleaved、broadleafed 也会出现；具体树名的俗称可有更窄指向。',L[:1]+[['broad + leaf → broadleaf','按宽平叶片特征形成的形容词、名称']],
 'broadleaf trees 阔叶树，broadleaf woodland 阔叶林。某些地方名词 broadleaf 还是特定植物的俗称，要看当地完整名称。',
 'broadleaf trees；broadleaf woodland。',
 'broadleaf 不等于 deciduous 落叶的：阔叶树中也有常绿种类。叶片形状与是否季节落叶是两种分类角度。',
 ('The path passes through broadleaf woodland.','小路穿过一片阔叶林。'),('The survey recorded both broadleaf trees and conifers.','调查记录了阔叶树和针叶树。'))
W('leafless','/ˈliːfləs/','无叶的；叶落光的',
 '树枝上看不到叶子，是 leafless 的直接画面。可能是季节落叶，也可能是其他情况，词本身不指定原因。',
 'leaf + -less，没有叶；中古英语有 leveles 等形式。现代形态保留 leaf 的 f，不按复数 leaves 接词尾。',L+[['leaf + -less → leafless','没有叶片的状态']],
 'leafless branches 光秃无叶的枝条，a leafless tree 无叶的树。描写外观，也可用于植物特征说明。',
 'leafless branches；a leafless tree。',
 'leafless 不自动等于 dead 死亡，冬天暂时落叶的树仍可以健康存活。',
 ('The birds rested on the leafless branches.','鸟停在光秃无叶的枝条上。'),('The tree was leafless in winter.','这棵树冬天没有叶子。'))
W('cloverleaf','英 /ˈkləʊvəliːf/；美 /ˈkloʊvərliːf/','三叶草叶；苜蓿叶形、四叶式立交桥',
 '先看三叶草一组分开的小叶，再看高速公路立交的几个环形匝道，平面轮廓像一团叶片，于是也叫 cloverleaf。',
 'clover 三叶草 + leaf 叶。道路用法是 cloverleaf interchange 的省称，按形状命名；不表示道路里种了三叶草。',L[:1]+[['clover + leaf → cloverleaf','三叶草叶形'],['按形状借给道路交叉结构','环形匝道形成的四叶式立交']],
 'a cloverleaf interchange 四叶式立交，a cloverleaf junction 苜蓿叶形交叉。不同道路设计会有变形，普通名称看总体布局。',
 'a cloverleaf interchange；a cloverleaf junction。',
 'cloverleaf 的道路名借形状，不是每个入口都可以直接左转。这个名称也不要求自然界每片 clover 都有四片小叶。',
 ('The road reaches a cloverleaf interchange near the city.','道路在城边通向一座四叶式立交。'),('The child drew a cloverleaf shape on the paper.','孩子在纸上画了一个三叶草叶形。'))
R('B3448','植物叶片、纸张薄片及其形态、数量和图形命名','LEAF：薄片的形象，连起树叶、纸张、金箔与折页','leaf → leafy、leafless；leaflet 小叶、印品；broadleaf 看叶宽，cloverleaf 借叶形。',
 '先分实体植物叶和片状扩展，再看后缀、前半修饰的对象。复数 leaves 与派生词保留 f 的变化也一起记。',
 'lēaf → leaf；复数 leaves；-y 性质、-less 没有、-let 小称；broad、clover 说明形状、对象。',
 [['基础与叶片状态','leaf · leafy · leafless'],['大小、叶形与图形','leaflet · broadleaf · cloverleaf']],
 '一 leaf 纸张可有两面 page；broadleaf 不等于落叶；leafless 不等于死树。',
 'The leaflet explains how a broadleaf tree can be leafy in summer and leafless in winter.\n\n这份说明折页解释了阔叶树怎样夏季叶茂、冬季无叶。','leaf leafy leafless leaflet broadleaf cloverleaf')
if __name__=='__main__':save('continuation_20261030_jx',ROOTS,WORDS)
