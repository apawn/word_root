"""Everyday short nouns: counting, shapes, measures and context-dependent readings."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'C0110':dict(words=['ball','balls'],label='ball → balls：球与舞会的两条来源',note='球的日耳曼词族与舞会的法语、拉丁词族分开，球不因为能扔就来自 ballein。'),
 'B3264':dict(words=['bill','bills'],label='bill → bills：文书、账单与鸟嘴',note='文书词族与本族鸟嘴词分开追溯，现代多义由具体场景判断。'),
 'B2733':dict(words=['kind','kinds'],label='kind → kinds：本性、类别与多种',note='本族种类名词，和形容词友善的历史相关而现代用途不同。'),
 'B3620':dict(words=['yard','yards'],label='yard → yards：院地与杆长单位',note='院子与码来自不同古英语词，现代同形同音。'),
 'C1488':dict(words=['attempt','attempts'],label='attempt → attempts：试着做与一次次尝试',note='拉丁试探、尝试词族经法语借入，不与 attend 直接互相派生。'),
 'C0163':dict(words=['champion','champions'],label='champion → champions：战士、胜者与支持者',note='法语、后期拉丁战斗者名称借入，现代另有积极支持的动词。'),
 'B3169':dict(words=['mark','marks'],label='mark → marks：界标、痕迹与分数',note='本族边界标记词发展，旧货币马克另有计重背景。'),
 'B2751':dict(words=['tear','tears'],label='tear → tears：眼泪与撕裂的不同读音',note='古英语流泪词与撕开词不同，两个现代同形词分别读。'),
 'B2828':dict(words=['break','breaks'],label='break → breaks：打断、破裂与休息间隔',note='本族打破词延续，暂停是把连续活动断开。'),
 'C0245':dict(words=['color','colors'],label='color → colors：颜色与给理解染上色彩',note='美式拼写，英式 colour、colours；拉丁、法语名动词有相应借入线。'),
 'C0570':dict(words=['court','courts'],label='court → courts：围地、宫廷与法院、球场',note='拉丁围地材料经法语借入，不同场所按用途发展。'),
 'B3801':dict(words=['hill','hills'],label='hill → hills：山丘与起伏地形',note='本族山丘名延续，按地形和位置形成组合。'),
 'B3474':dict(words=['ton','tons'],label='ton → tons：大桶、计量与大量',note='与 tun 大桶相关并受法语形式影响，重量与容量有历史发展。'),
 'B3335':dict(words=['bar','bars'],label='bar → bars：条杆、柜台、小节；压力单位另源',note='条杆词经法语借入，压力单位则来自希腊重量词。'),
 'C0425':dict(words=['final','finals'],label='final → finals：终点、最后一轮与期末考试',note='拉丁终点材料形成形容词，英语名词化后数最终场次、考试。'),
}
W('balls','英 /bɔːlz/；美 /bɔːlz/、/bɑːlz/','球、球状物；舞会〔复数，来源分支不同〕',
 '圆圆、能滚动或用于运动的物体，是 balls 的球义；正式跳舞聚会也叫 balls，但历史要走另一条舞蹈词线。',
 'ball + -s，/l/ 后读 /z/。球名接日耳曼语的圆物词族，可能经古英语或古诺尔斯语相关形式；舞会名经法语 bal、晚期拉丁 ballāre 跳舞，较远联系希腊舞蹈词。',
 [['古英语、古诺尔斯等日耳曼圆物词 → 球 ball','圆形物体、游戏用球'],['法语 bal 等舞蹈词 → 舞会 ball；各加 -s → balls','舞会与球是不同借入历史']],
 'tennis balls 网球；balls of wool 毛线团；formal balls 正式舞会。',
 'balls rolling across the floor；balls held in the hall。','运动和圆物语境是球、团块；历史社交场景的 balls 可能是舞会。不能只因球会被投出，就把球的词源直接接到希腊 ballein 投掷。',
 ('The children collected the balls after the game.','比赛后，孩子们收起了球。'),('The old hall was once used for formal balls.','这个老大厅曾用来举办正式舞会。'),sources=['https://en.wiktionary.org/wiki/balls#English','https://www.etymonline.com/word/ball'])
W('bills','/bɪlz/','账单、拟议法案、钞票；鸟嘴〔复数，分支不同〕；开账单〔第三人称单数〕',
 '把要付什么、要提出什么写在一份文书上，是 bills 的文书分支；鸟伸出来的嘴也叫 bills，却是另一条本族词。',
 'bill + -s，/l/ 后读 /z/。文书 bill 经法语 bille、相关拉丁 billa 接中世纪拉丁 bulla 印封文书；鸟嘴 bill 继承古英语相关嘴、刃器词。英语再有寄送账单的动词。',
 [['法语、拉丁印封文件词 → bill','文书 → 账单、法案、纸币'],['古英语鸟嘴词 → 另一 bill；各加 -s → bills','鸟嘴；或多份文书、单数主语收费开单']],
 'pay the bills 付账；electricity bills 电费单；dollar bills 美元纸币；birds with long bills 长嘴的鸟。',
 'bills waiting to be paid；bills discussed by the committee。','bills 在议事语境常是提出审议的法案，在日常付款语境是账单；纸币义在美式常见。鸟类语境则按鸟嘴另读这条来源。',
 ('She keeps the household bills in a folder.','她把家里的账单放在文件夹里。'),('The birds have long, narrow bills.','这些鸟有细长的嘴。'),sources=['https://en.wiktionary.org/wiki/bills#English','https://www.etymonline.com/word/bill'])
W('kinds','/kaɪndz/','种类、类型〔kind 的复数〕',
 '把相似的东西放在同一类，就有 kinds；不同材料、做法、性格都可以按共同特点分成几种。',
 'kind + -s，/d/ 后读 /z/。名词接古英语 cynd、ġecynd 本性、种类；友善的形容词 kind 与相关旧形相连，但 kinds 在这里数类别。',
 [['古英语 cynd、ġecynd → kind 名词','本性、性质 → 一类事物'],['kind + -s → kinds','多个种类、不同类型']],
 'different kinds 不同种类；all kinds of 各种各样；two kinds of material 两种材料。',
 'kinds of music；kinds of questions。','kinds of 后接正在分类的对象，如 kinds of music；music 不可数，仍保留原形。种类 kinds 与友善 kind 的形容词语法不同。',
 ('The shop sells several kinds of bread.','这家店出售几种面包。'),('The lesson introduces different kinds of questions.','这节课介绍不同类型的问题。'),sources=['https://en.wiktionary.org/wiki/kinds#English','https://en.wiktionary.org/wiki/kind#English'])
W('yards','英 /jɑːdz/；美 /jɑːrdz/','院子、场地；码〔复数，来源分支不同〕',
 '房子周围圈出的一块地，是 yards 的院地义；按一段杆长计量，后来固定的长度单位也写 yards。今天同形，较早是两个词。',
 'yard + -s，/d/ 后读 /z/。院地接古英语 ġeard；码接另一古英语 ġierd 杆、杖。长度单位的一码是三英尺，不从庭院大小推算。',
 [['古英语 ġeard → 院地 yard','围出的地 → 院子、场地'],['古英语 ġierd → 杆、码 yard；各加 -s → yards','杆长 → 长度单位；多个场地或若干码']],
 'school yards 学校院地；back yards 后院；ten yards 十码；yards of fabric 几码布。',
 'yards behind the houses；yards measured along the path。','yards 在数字、测距、布料语境常是码，在房屋、操场等语境常是院地。一码三英尺是单位关系，院子的实际大小各不相同。',
 ('The children played in the yards behind the houses.','孩子们在房后的院子里玩。'),('The gate is only a few yards from the road.','大门离道路只有几码远。'),sources=['https://en.wiktionary.org/wiki/yards#English','https://en.wiktionary.org/wiki/yard#English'])
W('attempts','/əˈtempts/','尝试、努力〔复数〕；试图〔第三人称单数〕',
 '朝目标做一次努力，不论最后成没成，都是 an attempt；多次努力是 attempts，单数主语试图做也写 attempts。',
 'attempt + -s，/t/ 后读 /s/，词尾 /mpts/ 连在一起。拉丁 ad- 与 temptāre 试探、尝试形成 attemptāre，经古法语 atempter 进入英语。',
 [['拉丁 attemptāre → 古法语 → attempt','试探、尝试 → 向目标作努力'],['attempt + -s → attempts','多次尝试；单数主语试图做']],
 'make attempts 作尝试；attempts to improve 改进的尝试；attempts to explain 试图解释〔看句法〕。',
 'attempts at solving the problem；attempts a new approach。','名词常用 an attempt to do、attempts at doing；动词 attempt to do 直接说明试图做什么。attempt 通常比 try 更正式。',
 ('Several attempts were needed before the lock opened.','尝试几次后，锁才打开。'),('The report attempts to explain the change.','报告试图解释这项变化。'),sources=['https://en.wiktionary.org/wiki/attempts#English','https://en.wiktionary.org/wiki/attempt#English'])
W('champions','/ˈtʃæmpiənz/','冠军、优胜者；积极支持者〔复数〕；积极支持〔第三人称单数〕',
 '在竞争场上胜出的人，是 champions；站出来为一种主张争取支持，也像替它上场，于是有支持者、倡导的意思。',
 'champion + -s，/n/ 后读 /z/。古法语 champion 接后期拉丁 campiō、campiōnem 战斗者，联系 campus 战场等材料；更早是否有日耳曼回借的步骤存在不同分析。',
 [['后期拉丁战斗者名称 → 古法语 → champion','上场战斗的人 → 竞赛胜者、替人出力者'],['champion + -s → champions；英语动词用途','多位冠军、支持者；单数主语积极倡导']],
 'world champions 世界冠军；champions of reform 改革支持者；champions local artists 积极支持当地艺术家。',
 'champions celebrating after the match；champions a cause。','champions 不限拿奖杯的人；champions of a cause 说为某主张出力的支持者。作动词时，后面直接接所支持的人或事情。',
 ('The champions returned home after the tournament.','冠军们在锦标赛后返回家乡。'),('The gallery champions young local artists.','这家画廊积极支持当地年轻艺术家。'),sources=['https://en.wiktionary.org/wiki/champions#English','https://en.wiktionary.org/wiki/champion#English'])
W('marks','英 /mɑːks/；美 /mɑːrks/','标记、痕迹；分数〔复数〕；标明、标志着〔第三人称单数〕',
 '留一个记号，让人知道位置、发生过什么，是 marks；考试给出的分数也像一份表现标记。',
 'mark + -s，/k/ 后读 /s/。mark 继承古英语 mearc 边界、界标、记号，后来发展出痕迹、评分、目标等用途；旧货币马克有另外计重、货币背景。',
 [['古英语 mearc → mark','边界、界标 → 记号、痕迹'],['mark + -s → marks；评分与标识发展','多个痕迹、分数；单数主语标明或标志着']],
 'full marks 满分；marks on the wall 墙上的痕迹；marks the entrance 标明入口；marks a new stage 标志着新阶段。',
 'marks made in pencil；marks the end of the course。','marks 作分数在英式尤其常见，grades 在美式也常用于成绩。marks a change、marks the end 则是动词，用一个事件标示变化、结束。',
 ('There were pencil marks on the wall.','墙上有铅笔印。'),('The ceremony marks the end of the course.','这场典礼标志着课程结束。'),sources=['https://en.wiktionary.org/wiki/marks#English','https://en.wiktionary.org/wiki/mark#English'])
W('tears','眼泪：英 /tɪəz/、美 /tɪrz/；裂口、撕裂：英 /teəz/、美 /terz/','眼泪〔复数〕；裂口〔复数〕；撕裂〔第三人称单数〕',
 '眼里流出的泪和布上撕开的口子，都写 tears，却读不同元音、来自不同旧词。两组画面和读音分别记清。',
 '两条 tear 都加 -s，词尾 /z/。眼泪支接古英语 tear、teor，与拉丁 lacrima 远同源；撕开支接古英语 teran，裂口名词由撕裂动作发展。',
 [['古英语流泪词 → tear → tears /tɪəz/ 等','眼里的泪；与 lacrima 是远同源，非直接借词'],['古英语 teran → 撕裂 tear → tears /teəz/ 等','撕开、裂口；与眼泪支分开']],
 'in tears 在流泪；tears of joy 喜悦的泪；tears in the fabric 布上的裂口；tears the paper 撕纸。',
 'tears filled her eyes；tears near the edge of the cloth。','看见 tears，先根据眼睛、哭泣或布纸、撕裂等语境选择元音。撕裂动词的过去式 tore，过去分词 torn；流泪词不沿这套变化。',
 ('Tears filled her eyes when she read the letter.','她读信时，眼里涌出了泪水。'),('The fabric has two small tears near the edge.','这块布边缘附近有两道小裂口。'),('She tears the paper into narrow strips.','她把纸撕成细条。'),sources=['https://en.wiktionary.org/wiki/tears#English','https://www.etymonline.com/word/tear'])
W('breaks','/breɪks/','休息、间隔；断裂〔复数〕；打破、中断〔第三人称单数〕',
 '连续的东西断开了，是 breaks；工作连着做，被短暂打断的一段时间，就成为一次休息。',
 'break + -s，/k/ 后读 /s/。break 继承古英语 brecan，经中古英语 breken 等发展；现代断开动作、断口与活动暂停等名词相互关联。',
 [['古英语 brecan → break','打破、断开 → 实物破裂或连续活动中断'],['break + -s → breaks','多次休息、断裂；单数主语打破、打断']],
 'short breaks 短暂休息；coffee breaks 喝咖啡的休息时间；breaks the rules 违反规则；breaks into pieces 碎成片。',
 'breaks between lessons；breaks the silence。','breaks 与 brakes 刹车常同音，拼写和当代含义不同。breaks the silence 是让沉默中断，breaks the rules 是越过规则，不必都译成砸坏。',
 ('The course includes short breaks between sessions.','课程在各节之间安排了短暂休息。'),('A sudden noise breaks the silence.','一声突如其来的响动打破了寂静。'),sources=['https://en.wiktionary.org/wiki/breaks#English','https://en.wiktionary.org/wiki/break#English'])
W('colors','英 /ˈkʌləz/；美 /ˈkʌlərz/','颜色〔复数〕；给……上色、影响〔第三人称单数；英式 colours〕',
 '红、蓝等一个个颜色，是 colors；把颜色加到物体上是动词上色，把情绪、经历的色彩加到判断上，则可说影响。',
 'color + -s，词尾读 /z/。拉丁 color 经古法语、英法语进入英语；动词也有拉丁 colorāre、法语 colorer 的借入历史。英式常写 colour、colours。',
 [['拉丁 color、colorāre → 法语等 → color 名动词','颜色、使有颜色；名动词有相应旧路线'],['color + -s → colors；比喻影响','多个颜色；单数主语上色、影响看法']],
 'bright colors 鲜艳颜色；mix colors 调色；colors her judgment 影响她的判断；true colors 真面目〔比喻〕。',
 'colors used in the painting；colors the way we see things。','color 的 o 常读 /ʌ/。colors a picture 是涂色；colors a judgment 则像给判断染上某种色彩，表达它受到影响。',
 ('The artist used bright colors in the painting.','画家在画中用了鲜艳的颜色。'),('Our experience colors the way we understand the story.','我们的经历影响着我们理解故事的方式。'),sources=['https://en.wiktionary.org/wiki/colors#English','https://en.wiktionary.org/wiki/color#English'])
W('courts','英 /kɔːts/；美 /kɔːrts/','法院、法庭；球场；宫廷〔复数〕；争取青睐、招致等〔第三人称单数〕',
 '围起来活动的一片地方，是 court 的老空间画面；王室聚会的宫廷、审理事情的法庭、打球的场地，沿不同用途发展。',
 'court + -s，/t/ 后读 /s/。古法语 cort 接拉丁 cohors 的缩约形式 cors、cortem，含共同与围地材料；宫廷、司法及球场义分支发展，英语又形成争取青睐的动词。',
 [['拉丁 cohors、cortem → 古法语 cort → court','围地、在此聚集的人 → 宫廷、院地'],['司法、运动等用途；court + -s → courts','多个法庭、球场；单数主语争取青睐等']],
 'tennis courts 网球场；law courts 法院、法庭；royal courts 王室宫廷；courts attention 争取注意。',
 'courts beside the sports hall；courts dealing with different cases。','court 的边界、用途随场景改变；sports centre 里常说球场，case、judge 等司法词旁常说法庭。动词 courts 常有主动争取某种关注、结果的意思。',
 ('The sports centre has four tennis courts.','这个体育中心有四个网球场。'),('The museum display compares life at different royal courts.','博物馆展陈比较了不同王室宫廷的生活。'),sources=['https://en.wiktionary.org/wiki/courts#English','https://www.etymonline.com/word/court'])
W('hills','/hɪlz/','山丘、小山〔hill 的复数〕',
 '地面鼓起、需要上坡再下坡的一座座小山，是 hills；它常让人想到起伏地形，而不是高耸山峰。',
 'hill + -s，/l/ 后读 /z/。hill 继承古英语 hyll，经中古英语延续；现代 uphill、downhill、hillside 等按山丘的方向、部位命名。',
 [['古英语 hyll → 中古英语 → hill','山丘、小山'],['hill + -s → hills','多个山丘、起伏山区']],
 'rolling hills 连绵起伏的山丘；hills in the distance 远处的小山；over the hills 翻过山丘。',
 'hills covered with trees；a path through the hills。','hills 常比 mountains 给人更低、较缓的感觉，但地名也受地方传统影响。the hills 还可整体说一片丘陵地带。',
 ('Trees covered the hills behind the village.','村后山丘上长满了树。'),('We could see the sea beyond the hills.','我们能看到山丘另一边的大海。'),sources=['https://en.wiktionary.org/wiki/hills#English','https://en.wiktionary.org/wiki/hill#English'])
W('tons','/tʌnz/','吨类重量、容量单位〔复数〕；大量、许多〔口语〕',
 '大到按桶装货、再按大重量计算，是 tons 的计量背景；口语里把量夸张说得很重、很多，就有 tons of 大量。',
 'ton + -s，/n/ 后读 /z/。ton 与 tun 大桶的词形相关，受法语 tonne 等形式影响；从容器到装载量、重量，具体单位逐渐固定。',
 [['大桶 tun／ton 等历史形式 → ton','装满大桶的量 → 大宗货物计量'],['ton + -s → tons；口语夸张','若干吨；很多、大量']],
 'tons of material 吨计的材料或大量材料〔视语境〕；tons of books 很多书；tons of time 很多时间〔口语〕。',
 'tons of stone；tons of useful information。','计量语境要看采用哪种 ton 体系，metric ton 是公吨，英式也常写 tonne。口语 tons of information 常只是在说很多，不是在称信息重量。',
 ('The project used several tons of stone.','这个项目用了几吨石料。'),('The archive contains tons of useful information.','档案里有大量有用资料。'),sources=['https://en.wiktionary.org/wiki/tons#English','https://www.etymonline.com/word/ton'])
W('bars','英 /bɑːz/；美 /bɑːrz/','条、杆、栅栏；酒吧；音乐小节；巴〔复数〕；阻止〔第三人称单数〕',
 '长条挡在前面，是 bars 的杆、栏画面；柜台后的饮品场所、图中的条形、音乐分隔出来的小节都各有扩展。压力单位巴则另有来源。',
 'bar + -s，元音或 /r/ 后读 /z/。条杆义经古法语 barre，远源未定；酒吧接售饮品的柜台、隔栏，音乐小节接分隔线。压力单位 bar 来自希腊 báros 重量，另源。',
 [['古法语 barre → 条杆 bar；不同用途扩展','杆栏、柜台、条形 → 酒吧、音乐分段等'],['另支希腊 báros → 压力 bar；各加 -s → bars','多个条杆、场所、小节、单位；单数主语阻挡']],
 'iron bars 铁栏杆；bars of soap 一块块肥皂；bars in a chart 图中的条形；bars entry 禁止进入。',
 'bars across the window；bars along the street。','a bar of soap 按条块形状数肥皂；a few bars of music 说几小节音乐。bars somebody from doing something 则是动词，像用栏杆挡住行动。',
 ('The windows were protected by iron bars.','窗户用铁栏杆保护着。'),('She bought two bars of soap.','她买了两块肥皂。'),('The chart uses blue bars to show the figures.','图表用蓝色条形展示数值。'),sources=['https://en.wiktionary.org/wiki/bars#English','https://www.etymonline.com/word/bar'])
W('finals','/ˈfaɪnəlz/','决赛阶段、总决赛；期末或毕业考试〔final 的名词复数〕',
 '比赛一路筛到最后的阶段，是 finals；一轮课程学到最后，要考最终掌握情况，也可以叫 finals。两者都抓住最后这一层。',
 'final + -s，/l/ 后读 /z/。拉丁 fīnis 终点形成 fīnālis 最后的，经法语进入英语；英语把形容词名词化，省略 match、examination 等所指活动后形成不同名称。',
 [['拉丁 fīnis → fīnālis → 法语、英语 final','终点 → 最后的'],['final 名词化 + -s → finals','最终比赛阶段；课程或学业末段考试']],
 'reach the finals 进入决赛阶段；prepare for finals 准备期末考试；university finals 大学毕业阶段考试〔具体看学校用法〕。',
 'finals held in the main stadium；revising for her finals。','体育语境的 finals 可说多场最终比赛或最终阶段；学校语境多说最终考试。单场决赛也常用 the final，按赛事格式与句子判断。',
 ('The team reached the finals of the tournament.','球队进入了锦标赛决赛阶段。'),('She is preparing for her finals at the library.','她正在图书馆准备期末考试。'),sources=['https://en.wiktionary.org/wiki/finals#English','https://en.wiktionary.org/wiki/final#English'])
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_za',ROOTS,WORDS)
 extend_lessons()
