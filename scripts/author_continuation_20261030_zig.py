"""Useful everyday gaps: ditch, gauge, slim, scatter and slant."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
def S(word,base):
 return ['https://en.wiktionary.org/wiki/'+word+'#English','https://www.etymonline.com/word/'+base]
EXISTING_ROOT_ADDITIONS={
 'B2845':dict(words='ditch ditches ditched ditching'.split(),label='ditch：沟渠，到丢弃、放弃',note='ditch 承古英语 dic，和 dike 是历史地域变体；与 dig 有同源、借入等分析，不是现代 dig 自由改音。先沟渠名词，再挖沟、扔沟里与弃置动词，水上迫降是另一专门引申。'),
 'C0725':dict(words='gauge gauges gauged gauging'.split(),label='gauge：另源的量尺、仪表与估量',note='与 measure 比较测量，不从拉丁 mensurare 派生。gauge 经法语量杆、测量词，较远可能接法兰克杆子材料，来源未定；读 /ɡeɪdʒ/，不按每个字母分别读。'),
 'B2547':dict(words='slim slims slimmed slimming'.split(),label='slim：另源的纤细、微小机会与精简',note='和 thin 比较细薄，不是 thin 派生。slim 借荷兰语，相应旧词有倾斜、坏、狡黠等义，英语发展出纤细与数量小；动词精简、使变苗条各有后起用法。'),
 'B2989':dict(words='scatter scatters scattered scattering'.split(),label='scatter：另源的散开、散落',note='和 spread 比较分布，不是 spread 派生。scatter 承中古英语 scateren，较早可说挥霍、驱散，可能与 shatter 的旧形相关并受北欧影响，不把 shatter 今天碎裂义硬定为每一支的起点。'),
 'B2886':dict(words='slant slants slanted slanting'.split(),label='slant：斜着，到偏向某一边',note='与 lean 比较倾斜，不是 lean 派生。slant 改自中古英语 slenten 侧滑等材料，可能接北欧同族；实体倾斜后来引申为叙述偏向、看问题的角度。'),
}
DITCH=[['古英语 dic 沟、土工设施 → 中古英语 diche → ditch','和 dike 是历史地域变体，沟与挖出的土堤曾共用名称'],['沟 → 挖沟、扔进沟 → 丢弃、放弃','现代飞机水上迫降义另按具体技术语境理解']]
GAUGE=[['法语量杆 gauge、测量 gauger 等 → 英语 gauge','较远可能接法兰克杆子材料，未定'],['量的标准、测量工具 → 仪表；动词测量、估量','从读尺度扩到判断人的反应、程度']]
SLIM=[['荷兰 slim 与更早倾斜、歪斜材料','另一条旧义走向狡黠、坏，不直接等同现代英语'],['英语纤细、少量 → slim chance；动词精简、变细','现代 slim down 也说减少篇幅、规模']]
SCATTER=[['中古英语 scateren：挥霍、驱散等','可能与 shatter 的旧形相关，受北欧影响'],['撒开、四散 → 分散分布、注意力散乱','不是一见散落就保证东西先被打碎']]
SLANT=[['中古英语 slenten 侧滑等 → slant','可能接北欧材料，远源未定'],['实体斜向、倾斜 → 名词角度、偏向','报道的斜向看法借空间方向说立场']]
W('ditch','/dɪtʃ/','沟渠；挖沟；丢弃、放弃；水上迫降〔专门用法〕',
 '路边挖出一条低沟，常为排水，是 a ditch。把不用的东西像扔沟里一样丢开，现代口语就有 ditch a plan 放弃计划。',
 '承古英语 dic，与 dike 是旧地域变体，沟和挖出土堤曾共用名称。名词后有挖沟、扔进沟，再引申弃置；飞机水上迫降又是后来的专门用法。',DITCH,
 'a drainage ditch 是排水沟；ditch an old plan 是放弃旧计划；ditch class 是逃课，偏口语。',
 'dig a ditch；a drainage ditch；ditch the plan；ditch an old habit。',
 'ditch 作放弃义很口语、常显得干脆；postpone 是推迟，事情仍可能以后做，不能自动译成彻底不干。',
 ('Water collected in the ditch beside the road.','水积在路旁的沟里。'),('We decided to ditch the old plan and start again.','我们决定放弃旧计划，重新开始。'),sources=S('ditch','ditch'))
W('ditches','/ˈdɪtʃɪz/','沟渠〔复数〕；丢弃、放弃、挖沟〔第三人称单数〕',
 '田边一条条排水沟，是 ditches；某个角色总临时抛下朋友，也可说 ditches his friends。',
 'ditch + -es，/tʃ/ 后读 /ɪz/；名词复数与动词三单同形。',DITCH+[['ditch + -es → ditches','多条沟；或某人放弃、抛下、挖沟']],
 'drainage ditches 说排水设施；ditches a plan 写放弃计划；ditches someone 写抛下某人，常有不负责任的语气。',
 'roadside ditches；drainage ditches；ditches the old approach。',
 'ditches 在地理场景数沟渠，在人物动作场景可能是抛下、放弃；先看主语、宾语，不只看词尾。',
 ('The fields are divided by narrow ditches.','狭窄的沟渠把田地分开了。'),('In the story, he ditches his friends whenever a better offer appears.','故事里，只要出现更好的邀请，他就抛下朋友。'),sources=S('ditches','ditch'))
W('ditched','/dɪtʃt/','丢弃、放弃了；挖沟了；水上迫降了〔依语境〕',
 '计划已经决定不用，是 ditched the plan；一件旧外套不再要，也可以用 ditched。若主语是飞机，再考虑水上迫降。',
 'ditch + 完整 -ed，/tʃ/ 后读 /t/；过去式、过去分词，不额外增加音节。',DITCH+[['ditch + -ed → ditched','过去弃置、挖沟；专门语境水上迫降']],
 'ditched the old approach 是改掉旧做法；was ditched by a friend 是被朋友抛下，通常带失望。',
 'ditched the plan；ditched the old coat；was ditched。',
 'ditched 是放弃、抛下等动作过去式，switched 是换到另一种；两者可能先后发生，意思不完全一样。',
 ('They ditched the original design after the test.','测试后，他们弃用了原来的设计。'),('She finally ditched the coat with the broken zip.','她终于把那件拉链坏掉的外套丢掉了。'),sources=S('ditched','ditch'))
W('ditching','/ˈdɪtʃɪŋ/','正在丢弃、放弃、挖沟；水上迫降〔依语境〕',
 '正在把老办法放到一边，准备换新路，是 ditching the old approach；词尾告诉你过程，具体动作仍取决于对象。',
 'ditch + -ing，基础 ch 保留；可作过程形式，也可作相应活动名词。',DITCH+[['ditch + -ing → ditching','弃置、挖沟等过程；技术语境另看']],
 'ditching old equipment 是淘汰旧设备；ditching class 是逃课；在航空叙述里才按水上迫降理解。',
 'ditching the plan；ditching old equipment；ditching class。',
 'ditching a method 通常意味着不再采用，testing a method 仍在评估；开始尝试新方法不保证旧方法已被抛弃。',
 ('The team is ditching the old filing system.','团队正在弃用旧的归档系统。'),('The article discusses ditching unnecessary meetings.','文章讨论了取消不必要的会议。'),sources=S('ditching','ditch'))
W('gauge','/ɡeɪdʒ/','测量仪表、量规；规格、尺度；测量、估量判断',
 '看一眼刻度，知道里面还剩多少，是 gauge 的直观画面。没有实体刻度时，也能凭人的表情、反应来 gauge how they feel。',
 '经法语量杆、测量词借入，较远可能接法兰克杆子材料，来源未定。标准、量具、测量动作逐步发展，再借给抽象的估量、判断。',GAUGE,
 'a fuel gauge 是油量表；a pressure gauge 是压力表；gauge someone’s reaction 是估量某人的反应；rail gauge 指轨距规格。',
 'a fuel gauge；a pressure gauge；gauge the mood；gauge the distance。',
 'gauge 可以用工具精量，也可以依据迹象估量；guess 可以缺少足够依据，二者不是每次都同样随意。',
 ('The fuel gauge showed that the tank was almost empty.','油量表显示油箱快空了。'),('It was difficult to gauge her reaction.','很难判断她的反应。'),sources=S('gauge','gauge'))
W('gauges','/ˈɡeɪdʒɪz/','仪表、量规、规格〔复数〕；测量、估量〔第三人称单数〕',
 '面板上一排显示温度、压力等的仪表，是 gauges；一个人先观察全场反应，再开口，则可以说 gauges the mood。',
 'gauge + -s，/dʒ/ 后后缀读 /ɪz/；保留基础末尾 e。名词复数与动词三单同形。',GAUGE+[['gauge + -s → gauges','多种仪表、尺度；或某人测量、估量']],
 'pressure gauges 数测量装置；gauges the audience’s reaction 是对反应作判断。',
 'check the gauges；pressure gauges；gauges the mood。',
 'gauges 可以是工具复数，measurements 是测量得到的数值、尺寸；仪表和读数是不同对象。',
 ('The engineer checked the gauges on the control panel.','工程师查看了控制面板上的仪表。'),('She gauges the audience’s mood before choosing a story.','她先判断听众的情绪，再选择要讲的故事。'),sources=S('gauges','gauge'))
W('gauged','/ɡeɪdʒd/','测量过；估量、判断过',
 '实际量过距离，或根据听众神情估过反应，过去都可说 gauged。它关注通过尺度、迹象得出判断。',
 'gauge 去末尾 e，加完整 -ed → gauged，/dʒ/ 后读 /d/；基础 gau- 保留，不能因读音简单就随意删 u。',GAUGE+[['gauge 去 e + -ed → gauged','过去测量、判断；词尾读 /d/']],
 'gauged the distance 是估量距离；gauged public reaction 是判断公众反应；具体精度看方法，不由词本身保证。',
 'gauged the distance；gauged her mood；gauged the depth。',
 'gauged the distance 可是凭观察估量，measured with a ruler 则明确用尺量；具体精度取决于方法。',
 ('He gauged the distance before taking the photograph.','拍照前，他估量了一下距离。'),('The organisers gauged interest through a short survey.','组织者通过一份简短问卷判断大家的兴趣。'),sources=S('gauged','gauge'))
W('gauging','/ˈɡeɪdʒɪŋ/','正在测量、估量、判断；测量过程',
 '一边观察、一边试着判断大概到什么程度，是 gauging。对象可以是实际深浅，也可以是人们的兴趣、反应。',
 'gauge 去末尾 e，加完整 -ing → gauging；保留 u，g 的读音仍是 /dʒ/。',GAUGE+[['gauge 去 e + -ing → gauging','依据尺度、迹象作判断的过程']],
 'gauging interest 常见于活动、内容策划，意为先了解大家感不感兴趣；gauging depth 是判断深度。',
 'gauging public reaction；gauging interest；gauging the distance。',
 'gauging interest 是了解兴趣程度，generating interest 是激起兴趣；先探反应与主动制造吸引力不是同一动作。',
 ('We are gauging interest in a weekend reading group.','我们正在了解大家是否有兴趣参加周末读书小组。'),('The photographer paused, gauging the distance to the subject.','摄影师停了停，估量与拍摄对象的距离。'),sources=S('gauging','gauge'))
W('slim','/slɪm/','纤细的、薄的；机会很小的；精简、使变细',
 '一本薄册、一台薄电脑，都可叫 slim；机会少到只剩细细一点，是 a slim chance。作动词，则把篇幅、规模等变得更精简。',
 '借荷兰语 slim，较早同族有倾斜、歪斜、狡黠等材料，英语发展出纤细、少量。现代动词使变细、精简与后来的体重用法，不能只按一个身体外形解释所有词义。',SLIM,
 'a slim laptop 是薄型电脑；a slim chance 是机会渺茫；slim down a report 是精简报告。',
 'a slim volume；a slim laptop；a slim chance；slim down the report。',
 'slim 描述人时常偏纤细，thin 更中性或依语境带消瘦评价；谈 chance 时，slim 只是概率小，不涉及身材。',
 ('She carried a slim notebook in her bag.','她包里带着一本薄薄的笔记本。'),('There is only a slim chance of finishing today.','今天完成的可能性很小。'),sources=S('slim','slim'))
W('slims','/slɪmz/','精简、使变薄、缩减〔第三人称单数〕',
 '编辑把一篇长文章删到更紧凑，是 slims it down；这里减掉的是文字、体量，不是在谈身体。',
 'slim + -s，/m/ 后读 /z/；这里优先学动词三单，不把基础形容词当作每个场景都能直接加复数。',SLIM+[['slim + -s → slims','某人、某个办法精简或缩减']],
 'slims down the text 是精简文字；slims the design 可以是让设计更细薄、简洁，需看实际对象。',
 'slims down the report；slims the design；slims down the list。',
 'slims down 常关注减少体量、让它更紧凑，simplifies 强调变简单；两件事可以一起发生，也可以不同。',
 ('The editor slims down the report before publication.','出版前，编辑会精简那份报告。'),('The new layout slims the design without removing useful controls.','新布局让设计更紧凑，同时保留了有用的控件。'),sources=S('slims','slim'))
W('slimmed','/slɪmd/','精简了、缩减了；变细了',
 '长报告已经去掉重复内容，留下紧凑版本，是 slimmed down。它强调体量比以前小，核心可能仍保留。',
 'slim 双写 m，加完整 -ed → slimmed，词尾读 /d/；过去式、过去分词。',SLIM+[['slim → slimmed','双写 m 加 -ed，体量已缩小、变精简']],
 'slimmed down the text 是精简过文字；a slimmed-down version 是缩减版，常作为整体修饰语。',
 'slimmed down the report；a slimmed-down version；slimmed the outline。',
 'slimmed down 通常是减少体量，stripped of detail 强调细节被去掉；精简是否仍保留关键内容，要看实际结果。',
 ('We slimmed down the guide to twenty pages.','我们把指南精简到二十页。'),('The team presented a slimmed-down version of the plan.','团队展示了计划的精简版。'),sources=S('slimmed','slim'))
W('slimming','/ˈslɪmɪŋ/','正在精简、缩减；显得纤细的；减重活动〔依语境〕',
 '给长文去掉赘余，是 slimming down the text；衣服线条让轮廓显得更细，也可以说 a slimming effect。两个场景都借“更细、更少”的核心。',
 'slim 双写 m 加 -ing → slimming；过程形式也有显得纤细的形容词用法，另可指减重活动。按对象选择，不能只认一个身体含义。',SLIM+[['slim → slimming','双写 m 加 -ing，缩减过程或显细的性质']],
 'slimming down a document 说文字；a slimming effect 说视觉效果；语境不同，不把外观变化当成实际体重变化。',
 'slimming down the text；a slimming effect；slimming the document。',
 'slimming effect 可以只是视觉轮廓，weight loss 才明确体重变化；衣服显得线条细，不等于穿着者真的改变了体重。',
 ('The editor is slimming down the introduction.','编辑正在精简引言。'),('The jacket’s vertical lines create a slimming effect.','夹克的竖向线条让轮廓显得更修长。'),sources=S('slimming','slim'))
W('scatter','英 /ˈskætə/；美 /ˈskætər/','撒开、使散落；四散、分散',
 '原来聚在一处的小东西，手一撒落到各处，是 scatter；人、鸟受惊各往不同方向跑，也能自己 scatter。',
 '承中古英语 scateren，较早可说挥霍、驱散，后来常见撒开、四散。可能与 shatter 的旧形相关并受北欧影响，不意味着今天每次散落都先经历打碎。',SCATTER,
 'scatter seeds 是撒种子；scatter papers over the floor 是让纸散落一地；the crowd scattered 是人群四散。',
 'scatter seeds；scatter cushions；scatter in all directions。',
 'scatter 强调分到各处、聚不拢，spread 可以有意均匀铺开；撒一地与抹均匀不是完全相同的动作。',
 ('Scatter the seeds over the soil.','把种子撒在土上。'),('The birds began to scatter when the dog approached.','狗一靠近，鸟儿就开始四散飞开。'),sources=S('scatter','scatter'))
W('scatters','英 /ˈskætəz/；美 /ˈskætərz/','撒开、使散落、四散〔第三人称单数〕',
 '风把叶子吹到各处，是 scatters the leaves；一个人边走边撒种，也是 scatters seeds。共同的是从一处散到多处。',
 'scatter + -s，读 /z/；基础词已有 /ə/、美式 /ər/，词尾 -s 本身不再添音节，本页优先掌握动词三单。',SCATTER+[['scatter + -s → scatters','它、他、她使东西散开或自己散去']],
 'scatters crumbs 是撒碎屑，scatters the crowd 是驱散人群；具体有没有施力、有没有意图，看主语。',
 'scatters leaves；scatters seeds；scatters in all directions。',
 'scatters 不保证分得整齐、均匀，distributes 也可说按计划分配；给每人一份不是必然“撒得到处都是”。',
 ('The wind scatters leaves across the path.','风把叶子吹得小路上到处都是。'),('She scatters seeds over the prepared soil.','她把种子撒在整理好的土上。'),sources=S('scatters','scatter'))
W('scattered','英 /ˈskætəd/；美 /ˈskætərd/','散落、分散的；零星的；思绪不集中的',
 '纸一张东一张西，是 scattered papers；村庄隔得很开，也是 scattered villages。脑中注意力像撒开收不回来，可说 feel scattered。',
 'scatter + 完整 -ed，词尾读 /d/；过程的结果变成分散状态形容词，又可比喻思路不集中。',SCATTER+[['scatter + -ed → scattered','已散开、分布零星；再说注意力散乱']],
 'scattered clouds 是零星云朵，scattered villages 是分散村庄，scattered thoughts 是零乱思绪。',
 'scattered papers；scattered showers；scattered villages；feel scattered。',
 'scattered 不等于 shattered 碎裂、崩溃：纸可以完整地散落各处，杯子 shattered 才明确破碎。二者词史相关分析不抹掉现代区别。',
 ('Books lay scattered across the floor.','书散落在地板各处。'),('A few scattered houses stood along the hillside.','山坡上零零星星坐落着几户房子。'),sources=S('scattered','scatter'))
W('scattering','英 /ˈskætərɪŋ/；美 /ˈskætərɪŋ/','正在撒开、四散；散布；稀疏零星的一些',
 '叶子正一片片飞散，是 scattering；远处稀稀落落几户房子，像被撒在地面上，可说 a scattering of houses。',
 'scatter + -ing，保留完整词干；既能表示过程，也可名词化说散布或零星的一些。',SCATTER+[['scatter + -ing → scattering','散布过程；a scattering of 又指稀疏分布的少量事物']],
 'scattering seeds 是撒种；a scattering of houses 不是一大排整齐房屋；光的 scattering 又称散射，借传播方向分开的画面。',
 'scattering seeds；a scattering of cottages；the scattering of light。',
 'a scattering of 关注零星分布，a row of 是排成一排；少量和队形是两种不同观察角度。',
 ('The wind was scattering petals across the lawn.','风正把花瓣吹散到草坪各处。'),('There was a scattering of cottages near the river.','河边零星分布着几间小屋。'),sources=S('scattering','scatter'))
W('slant','/slɑːnt/〔英〕；/slænt/〔美〕','倾斜、斜向；看问题的角度、偏向；使带倾向',
 '一束光斜着照进来，是 slant 的具体画面。报道不正面展示全貌，而向某一方偏，也借“斜向”的感觉说 slant。',
 '改自中古英语 slenten 侧滑等，可能接北欧材料；实体倾斜、斜向到名词角度，后来又说看法、报道的倾向。不是从现代 lean 直接派生。',SLANT,
 'at a slant 是斜着；a new slant on the story 是新的观察角度；slant a report 是让报道带偏向。',
 'at a slant；a new slant on something；a political slant。',
 'slant 可以只是一个角度，也可以带偏见，视语境而定；bias 更直接强调倾向失衡，不是所有 new slant 都在骂偏见。',
 ('The letters were written at a slight slant.','那些字写得略微倾斜。'),('Her research offers a new slant on the old story.','她的研究为那个老故事提供了新角度。'),sources=S('slant','slant'))
W('slants','/slɑːnts/〔英〕；/slænts/〔美〕','倾斜、偏向〔第三人称单数〕；角度、倾向〔复数〕',
 '日光斜穿过窗户，可以说 slants through the window；不同人讲同一件事，有不同 slants，是从不同角度看。',
 'slant + -s，/t/ 后读 /s/；名词复数与动词三单同形。基础 nt 保留，不增加音节。',SLANT+[['slant + -s → slants','它斜向、某人让叙述偏向；或多个角度']],
 'different slants on the issue 是议题的不同角度；light slants in 是光斜照进来。',
 'different slants；slants across the room；slants the account。',
 'slants 作看法复数可包含角度差异，不保证每个都失实；facts 是事实本身，presentation 可用不同角度组织它。',
 ('The sunlight slants across the floor.','阳光斜斜地照过地板。'),('The two books offer different slants on the same event.','两本书从不同角度讲述同一件事。'),sources=S('slants','slant'))
W('slanted','/ˈslɑːntɪd/〔英〕；/ˈslæntɪd/〔美〕','倾斜的；带偏向、偏袒的；倾斜了',
 '屋顶是斜的，可说 slanted；报道明显偏向一方，也叫 slanted。一个是实际角度，一个是对待事实的倾斜。',
 'slant + 完整 -ed，/t/ 后读 /ɪd/，增加音节；过去分词常作形容词，包含实体与叙述倾向两支。',SLANT+[['slant + -ed → slanted','斜着的状态；或内容偏向某一方']],
 'a slanted roof 是斜顶；slanted coverage 是有偏向的报道；slanted in favour of someone 是偏袒某人。',
 'a slanted roof；slanted handwriting；a slanted account。',
 'slanted account 带评价，detailed account 只说细；报道详细并不自动客观，偏向也不等于完全没有细节。',
 ('The attic has a slanted roof.','阁楼的屋顶是斜的。'),('The review was criticised for giving a slanted account of the debate.','那篇评论因偏向性地叙述辩论而受到批评。'),sources=S('slanted','slant'))
W('slanting','/ˈslɑːntɪŋ/〔英〕；/ˈslæntɪŋ/〔美〕','斜向的；斜照、倾斜的过程',
 '夕阳不是从头顶直下，而是斜穿过窗户，这种方向可以写 slanting sunlight。-ing 可以描写形态，不一定表示东西在移动。',
 'slant + -ing；基础 nt 直接保留，不双写 t。过程形式也作倾斜、斜向的形容词。',SLANT+[['slant + -ing → slanting','斜向照射、延伸；或倾斜的性质']],
 'slanting rays 是斜照光线，slanting handwriting 是倾斜字迹；具体角度由修饰语补充。',
 'slanting sunlight；slanting lines；a slanting roof。',
 'slanting 和 sloping 都能写斜向，sloping 更常用于坡地、连续斜面，slanting 很适合光线、线条；两者有重叠。',
 ('Slanting sunlight reached the back of the room.','斜照的阳光一直伸到房间深处。'),('He drew a series of slanting lines.','他画了一组斜线。'),sources=S('slanting','slant'))
def extend_lessons():
 extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_zig',ROOTS,WORDS)
 extend_lessons()
