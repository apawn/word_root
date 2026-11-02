"""Far and story: distance, perspective, narrative, and visual planning."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
def C(a,b,w,m):return [[f'{a}；{b}','并列构词部分'],[w,m]]
FAR=[['古英语 feor / feorr → 中古英语 fer / ferre','远；相隔距离大'],['英语 far','远；时间、程度上相差大']]
W('far','英 /fɑː/；美 /fɑːr/','远的；远；很、远远〔加强比较〕',
 '不只路很长，时间、差距也能拉得很开。',
 '接古英语 feor、feorr，经中古英语 fer、ferre 等延续。现代常见比较形式 farther / further、最高级 farthest / furthest；这些有各自旧形式、类推变化，不是随意造 farer。',FAR,
 'How far? 问多远，far away 很远，far better 好得多，so far 到目前为止。日常肯定句常说 a long way，疑问和否定中 far 很自然。',
 'how far；far away；far better；so far；far from。',
 'far 空间、程度都可远；far from perfect 是远非完美。进一步讨论常用 further，不能把所有 further 都当额外路程。',
 ('How far is the station from here?','车站离这里多远？'),('The second plan is far better.','第二个方案好得多。'))
W('afar','英 /əˈfɑː/；美 /əˈfɑːr/','在远处；从远处',
 '人没走近，只远远望着、听着或传来消息。',
 '中古英语 afer，现代对应旧前置成分 a- + far；a- 不表示一个数量。整体较书面、文学化。',FAR+[['a- + far → afar','在远处；由远处而来']],
 'from afar 从远处，watch from afar 远远看。比普通 far away 更带叙事、文学语气。',
 'from afar；watch from afar；admire from afar。',
 'afar 常见 from afar，faraway 常作形容词放名词前；a faraway village 正常，不机械写 an afar village。',
 ('We could hear music from afar.','我们能听见远处传来的音乐。'),('She admired the castle from afar.','她远远欣赏那座城堡。'))
W('faraway','英 /ˈfɑːrəweɪ/；美 /ˈfɑːrəweɪ/','遥远的；心不在焉、若有所思的',
 '地方离得远，人的目光也可能像思绪已经跑到很远的地方。',
 'far + away 连写，形成常用形容词；同样意思的短语作表语、副词时常分写 far away。',C('far','away','faraway','距离遥远；神情像思绪远去'),
 'a faraway place 遥远地方，a faraway look 心不在焉的目光。The village is far away 常分写，名词前 a faraway village 常连写。',
 'a faraway place；a faraway land；a faraway look。',
 'faraway look 是人的神情，眼睛本身不必看着极远的实物；literal 与比喻要按对象选。',
 ('The book describes a journey to a faraway island.','书描写了一次前往遥远岛屿的旅程。'),('He had a faraway look as he remembered his childhood.','回忆童年时，他露出若有所思的神情。'))
W('farsighted','英 /ˌfɑːˈsaɪtɪd/；美 /ˈfɑːrˌsaɪtɪd/','有远见的；远视的〔尤美式〕',
 '想事时不只盯眼前，而看见以后需要什么；医学用法另说远视，不能把两种优劣混在一起。',
 'far + sighted，sighted 对应 sight + -ed“有某种视力、眼光的”。有远见是看得长远的比喻；眼科词义不等于比常人看得无限远。',C('far','sighted〔sight + -ed〕','farsighted','眼光长远；远视的'),
 'a farsighted decision 有远见的决定，a farsighted planner 看得长远的规划者；美式视力语境可说远视，英式常用 long-sighted。',
 'a farsighted decision；a farsighted policy；a farsighted planner。',
 'farsighted 有远见，不是远处真实视力越好就判断力必然更好；医学远视与年龄相关的老视概念也不应全按一个中文老人眼来混。',
 ('It was a farsighted decision to preserve the old railway route.','保留旧铁路路线，是有远见的决定。'),('In American English, someone described as farsighted may have difficulty focusing on nearby objects.','美式英语中，说某人 farsighted，也可能是在说他远视、近处物体不易对焦。'),
 sources=['https://en.wiktionary.org/wiki/farsighted#English','https://dictionary.cambridge.org/dictionary/english/far-sighted'])
R('B3093','远；程度差距大；长远眼光','FAR：把距离、时间或差距拉开','道路远、相差远、眼光远，画面对象不同；afar、faraway 再分副词与形容词。',
 'far 接古英语 feor、feorr；现代比较级形式有各自历史，不造 farer。farsighted 的视力与远见用法分别说清，不把原词典里简单等同老视的说法照搬。',
 'far → afar、faraway；far + sighted → farsighted。比较级、最高级在 far 里说明，不单独堆普通词形。',
 [['距离、位置及神情','far · afar · faraway'],['眼光与视力语境','farsighted']],
 'from afar 远远地、a faraway village 遥远村庄；far better 好得多；farsighted 有远见不等于视力诊断。',
 'From afar, the faraway island looked like a dark line on the sea.\n\n从远处望去，那座遥远岛屿像海上的一道暗线。',
 'far afar faraway farsighted')
STORY=[['古希腊 historiā → 拉丁 historia → 盎格鲁诺曼 estorie','研究、记述、历史叙事'],['中古英语 storie → 英语 story〔叙事义〕','故事、叙述；与 history 是相关借词形式']]
W('story','英 /ˈstɔːri/；美 /ˈstɔːri/','故事；叙述；新闻报道；楼层〔美式〕',
 '一连串事件讲给人听，是 story；建筑有几层的美式 story 则先单独记，别硬画成书页堆成楼。',
 '叙事义经盎格鲁诺曼 estorie 脱落开头元音，经中古英语 storie 接拉丁 historia、古希腊 historiā。层义也有中古英语、中世纪拉丁的历史，常联系 historia 的图像等旧用法，具体语义桥梁不宜说成定论。',
 [['叙事路径：historiā → historia → estorie → storie；另有楼层义的中世纪形式','相关但具体语义发展不能只靠现代字面串成单线'],['现代 story','故事、报道；美式楼层，英式常写 storey']],
 'tell a story 讲故事，a news story 新闻报道，a house with three stories 三层房子。故事可以真实，也可以虚构；story 本身不等于谎话。',
 'tell a story；a true story；a news story；the story behind。',
 'story 叙事，history 历史、历史研究，词源相关但现代用途不同。story 层在英式常写 storey，复数 stories / storeys 各随拼写。',
 ('She told us a story about her childhood.','她给我们讲了一个童年故事。'),('The newspaper published a story about the restored bridge.','报纸发表了关于修复桥梁的报道。'),('The building has four stories.','这座楼有四层。'),
 sources=['https://en.wiktionary.org/wiki/story#English','https://www.etymonline.com/word/story'])
W('storyline','/ˈstɔːrilaɪn/','故事情节；叙事线',
 '事件不只是散点，顺着一条线发展，人物的处境也沿线变化。',
 'story + line，line 取发展脉络，不是印在纸上的单独一行字。',C('story','line','storyline','故事事件的发展脉络、情节线'),
 'a main storyline 主情节，a romantic storyline 爱情线。复杂作品可同时有多条，不必每一条都从第一章出现。',
 'the main storyline；a romantic storyline；follow the storyline。',
 'storyline 看情节推进，backstory 看主线开始前的人物、事件背景；背景可以影响主线，但不就是同一时间段。',
 ('The film has a simple but effective storyline.','电影情节简单，却很有效。'),('I found the secondary storyline more interesting.','我觉得副线更有意思。'))
W('storyteller','英 /ˈstɔːritelə/；美 /ˈstɔːritelər/','讲故事的人；叙事者；编瞎话者〔依语境〕',
 '把事件选出来、排起来、讲给别人听的人，不限于坐着口头讲。',
 'story + teller，teller 是 tell + -er；这里不是银行柜员 teller 那个职业义。',C('story','teller〔tell + -er〕','storyteller','通过口头、文字、影像等讲故事的人'),
 'a gifted storyteller 会讲故事的人，a visual storyteller 用图像叙事的人。部分语境也可说爱编瞎话者，是否贬义看上下文。',
 'a gifted storyteller；a visual storyteller；a natural storyteller。',
 'storyteller 负责叙事，不一定等于作品里的 narrator 叙述角色；作者、导演和虚构叙述者可以是不同层次。',
 ('My grandfather was a wonderful storyteller.','我祖父很会讲故事。'),('The photographer is a gifted visual storyteller.','这位摄影师很擅长用画面讲故事。'))
W('storytelling','/ˈstɔːritelɪŋ/','讲故事；叙事技巧',
 '把观众带进事件、让他愿意继续听下去，这个过程和本领就是 storytelling。',
 'story + telling，telling 是 tell + -ing；与 storyteller 对照，一个看活动、技法，一个看人。',C('story','telling〔tell + -ing〕','storytelling','叙述故事的活动和技巧'),
 'the art of storytelling 叙事艺术，visual storytelling 视觉叙事，oral storytelling 口头讲述。并非所有技巧都只服务虚构故事，真实报道也要组织叙述。',
 'the art of storytelling；visual storytelling；oral storytelling。',
 'storytelling 活动、技法，storyline 情节脉络；同样情节可以被讲得精彩，也可以讲得平淡。',
 ('The film combines simple animation with strong storytelling.','电影把简单动画与有力叙事结合起来。'),('The workshop explores oral storytelling.','工作坊探讨口头讲故事。'))
W('backstory','/ˈbækstɔːri/','背景故事；人物前史',
 '镜头开始时，人物已经活过许多年；之前发生什么，解释了他今天为什么这样。',
 'back-（过去、背后背景）+ story，不是把书从后往前读一遍。',C('back-〔以前、背后〕','story','backstory','主线之前、背后的故事背景'),
 'a character’s backstory 人物前史，reveal the backstory 揭开背景。可在正文、对话里慢慢透露，不要求一定先整段讲完。',
 'a character’s backstory；reveal the backstory；a detailed backstory。',
 'backstory 背景前史，sequel 后续作品；一个往当前故事之前看，一个继续往后写。',
 ('The flashback reveals the character’s backstory.','闪回揭示了角色的前史。'),('The game gives each main character a detailed backstory.','游戏为每位主要角色设置了详细背景故事。'))
W('storied','/ˈstɔːrid/','历史丰富、广为传说的；有某些楼层的〔另义〕',
 '一个地方、人物经历过太多事，关于它的故事到处有人讲；这是最值得先记的形容词义。',
 'story（故事）+ -ed，形成有丰富事迹、广为传述的形容词；另有 story（层）+ -ed，见于说明楼层的组合。两种 story 义分别参与，不把多层建筑都说成传奇建筑。',C('story〔叙事；另有层义〕','-ed','storied','故事丰富、历史悠久；另可参与楼层描述'),
 'a storied career 经历丰富、著名的生涯，a storied club 历史显赫的俱乐部。往往含声望、传奇感，不只是昨天发生过一件小事。',
 'a storied career；a storied past；a storied institution。',
 'storied 常强调有值得传述的经历；old 只说年代久，老并不保证一定声名显赫。',
 ('The museum celebrates the team’s storied past.','博物馆纪念球队辉煌丰富的往昔。'),('She joined a storied institution with a long artistic tradition.','她加入了一家历史显赫、艺术传统悠久的机构。'))
W('storyboard','英 /ˈstɔːribɔːd/；美 /ˈstɔːribɔːrd/','分镜图；故事板；绘制分镜',
 '还没正式拍，就用一格格图把镜头、事件顺序摆出来，让大家看到同一部“预想中的片子”。',
 'story + board（板），从排布故事画面的工具、图组名发展为动词。不是董事会 board 负责讲故事。',C('story','board〔排图板〕','storyboard','按场景、步骤排列的图组；绘制这种图组'),
 'draw a storyboard 画分镜，storyboard a scene 给一场戏做分镜。也可用于产品流程、事件示意，不限电影。',
 'draw a storyboard；a storyboard panel；storyboard a scene。',
 'storyboard 用图预排顺序，script 剧本通常用文字、对白、动作说明；两者可配合，但不是同一材料形式。',
 ('The director showed us the storyboard before filming.','开拍前，导演给我们看了分镜图。'),('The team storyboarded the user’s first visit to the app.','团队用故事板画出了用户第一次使用应用的流程。'))
R('B3772','叙事、故事及故事呈现；同形楼层义另看','STORY：把事件组织成一段可跟随的叙述','主线是 storyline，谁讲是 storyteller，怎么讲是 storytelling，之前经历是 backstory，预先画出来是 storyboard。',
 '叙事 story 经法语上接拉丁、希腊 historia，与 history 相关。美式层义常与英式 storey 对照，具体早期语义桥梁不要用图画故事简单说死；understory 等选层义的专门词本组先不展开。',
 'story → storyline；story → storyteller / storytelling；backstory 讲前史，storied 讲传奇经历，storyboard 讲图示预排。storybook、storytime 已精讲复用。',
 [['故事、主线与叙事者、技法','story · storyline · storyteller · storytelling'],['背景、声望和图示','backstory · storied · storyboard'],['既有读物与活动','storybook · storytime']],
 'story 不一定虚构；history 与 story 同源但不同用；backstory 前史、storyline 主线；storied 丰富著名经历不只等于 old。',
 'The storyteller used a storyboard to explain how the backstory shaped the main storyline.\n\n叙事者用故事板解释前史怎样影响主线。',
 'story storyline storyteller storytelling backstory storied storyboard storybook storytime')
if __name__=='__main__':save('continuation_20261028_bd',ROOTS,WORDS)
