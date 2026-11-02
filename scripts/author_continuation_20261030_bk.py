"""Hill, murder and purpose: terrain, crime vocabulary and intention."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
HI=[['古英语 hyll → 中古英语 hil → hill','隆起地形、丘陵、小山'],['现代 hill','山丘；按位置、形态、土堆命名，也用于难易与走下坡路比喻']]
def H(f,m):return HI+[[f,m]]
W('hill','/hɪl/','小山、山丘；丘陵',
 '地面隆起成一座山包；通常让人想到比 mountain 小、缓一些的高地，实际地名不总按严格高度切分。',
 '继承古英语 hyll。现代复合词常从山的上、下、顶、侧面命名，也可借上坡的费力、下坡的趋势理解比喻。',HI,
 'climb a hill 爬小山，at the top of the hill 在山顶，over the hill 可翻过山，也可俚语说过了巅峰。',
 'climb a hill；at the top of the hill；over the hill。',
 'hill 小山、mountain 山的日常区别有尺度、陡峭感觉，但没有全世界统一的词义高度线；地名可能保留传统。',
 ('The village stands on a low hill.','村庄坐落在一座低矮山丘上。'),('We climbed the hill to watch the sunset.','我们爬上小山看日落。'))
W('hilly','/ˈhɪli/','多山丘、丘陵起伏的',
 '路走一会儿就要上上下下，不是一座孤零零的小山，而是整片地面起伏。',
 'hill + -y，中古英语已有 hilly、hylly 等形式。形容区域多丘陵，不等于一定高山险峻。',H('hill + -y → hilly','有许多小山丘、地势起伏'),
 'a hilly area 丘陵地区，hilly roads 起伏的道路，hilly countryside 丘陵乡野。',
 'a hilly area；hilly roads；hilly countryside。',
 'hilly 多山丘，mountainous 多高山、山地；两者不是仅仅一个褒义一个贬义。',
 ('Cycling is harder in this hilly area.','在这片丘陵地区骑车更费劲。'),('The road winds through hilly countryside.','道路蜿蜒穿过丘陵乡野。'))
W('downhill','/ˌdaʊnˈhɪl/','下坡、向山下；每况愈下；下坡比赛项目',
 '实际下坡是往低处走；比喻 go downhill 常说状态开始变差，all downhill 则有时说后面轻松了。',
 'down- 向下 + hill。方向、运动项目和比喻分别固定，不能只按轻松就说每个 downhill 都好。',H('down + hill → downhill','向山下 → 下坡运动；恶化或进程更轻松等比喻'),
 'walk downhill 下坡走，downhill skiing 高山滑雪、下坡滑雪，go downhill 走下坡路；all downhill from here 要看语境是轻松还是恶化。',
 'walk downhill；downhill skiing；go downhill；all downhill from here。',
 'uphill battle 艰难努力，go downhill 状态恶化，两者都可能负面；空间相反不保证抽象评价简单相反。',
 ('The path runs downhill towards the river.','小路向下坡通往河边。'),('The service has gone downhill in recent years.','近几年服务质量每况愈下。'))
W('hillock','/ˈhɪlək/','小丘、小土岗',
 '比普通山丘更小的一处隆起，像地面鼓起一个小包；常见于描写景物。',
 'hill + 小称 -ock，中古英语 hillok 等形式延续。末尾不是独立 rock 岩石缩写。',H('hill + -ock → hillock','较小的丘、小土岗'),
 'a grassy hillock 长草小丘，a low hillock 低矮土岗。',
 'a grassy hillock；a low hillock；sit on a hillock。',
 'hillock 小丘，hilltop 是山顶位置；小山本身和山的顶部不是同一概念。',
 ('They sat on a grassy hillock above the path.','他们坐在小路上方一座长草小丘上。'),('A low hillock hid the cottage from view.','一座低矮小丘挡住了那间小屋。'))
W('molehill','英 /ˈməʊlhɪl/；美 /ˈmoʊlhɪl/','鼹鼠丘；鼹鼠掘出的土堆',
 '鼹鼠在地下挖，土被顶到地面堆成小丘；成语里就拿这点小土堆和大山作对照。',
 'mole 鼹鼠 + hill 小丘。固定 make a mountain out of a molehill 用小丘变大山比喻小题大做。',H('mole + hill → molehill','鼹鼠掘出的土丘；小事的成语形象'),
 'a molehill in the lawn 草坪鼹鼠丘，make a mountain out of a molehill 小题大做。',
 'a molehill in the lawn；make a mountain out of a molehill。',
 'molehill 的 mole 是鼹鼠，不接皮肤痣或化学摩尔；用成语批评别人小题大做，语气会显得否定其担心。',
 ('Several molehills appeared in the lawn overnight.','一夜之间，草坪上冒出了几个鼹鼠丘。'),('It was a small mistake, so don’t make a mountain out of a molehill.','只是个小错误，别小题大做。'))
W('anthill','/ˈænthɪl/','蚁丘；蚂蚁筑起的土堆、巢丘',
 '蚂蚁搬土、筑巢，在地面形成一座小丘；不是人专门给蚂蚁造的小山。',
 'ant 蚂蚁 + hill，古英语已有相应组合 ǣmethyll。今天按两种普通成分认形即可，巢穴结构不只局限于露出的土堆。',HI[:1]+[['古英语 ǣmethyll 等 → anthill','蚂蚁巢相关土丘；现代 ant + hill']],
 'an anthill beside the path 小路旁的蚁丘，ants around an anthill 蚁丘周围的蚂蚁。',
 'an anthill beside the path；a large anthill；ants around an anthill。',
 'anthill 蚂蚁丘，molehill 鼹鼠丘；前部动物决定是谁造的，不要因都是土堆就混成同一巢穴。',
 ('We watched ants moving around the anthill.','我们看着蚂蚁在蚁丘周围活动。'),('A large anthill stood beside the path.','小路旁有一座大蚁丘。'))
W('hillbilly','/ˈhɪlbɪli/','美国偏远乡村、山地居民的称呼〔常贬义或自嘲〕',
 '影视对白里有时借它嘲笑人土气、没见过世面；也有人拿来自称，语气、身份不同会改变效果。',
 'hill 山地 + billy 家伙等人称成分。细究成名的具体故事有不同说法，本文不编成某个名叫 Billy 的人的唯一来源。',H('hill + billy〔家伙等人称〕→ hillbilly','山地、乡村居民称呼；后有土气的刻板评价'),
 'a hillbilly character 山乡居民形象角色，hillbilly music 某些旧式乡村音乐称呼。直接称人可能冒犯。',
 'a hillbilly character；hillbilly music；call oneself a hillbilly。',
 'hillbilly 文化、地域和语气信息较强，rural resident 乡村居民更中性；不能把所有住山里的人都这样叫。',
 ('The film relies on an old hillbilly stereotype.','电影借用了老套的山乡人刻板形象。'),('He jokingly called himself a hillbilly.','他开玩笑地自称乡巴佬。'))
R('B3801','山丘地形；位置、起伏、土堆与文化称呼','HILL：地面鼓起的小山；前后成分说明哪部分、什么特点','hill → hilly、hillock；uphill/downhill 对照方向和比喻；已有 hillside、hilltop、hillcrest、foothill 分位置；动物土丘连读。',
 '冷门职业、姓氏式复合词暂略。hillbilly 是带社会评价的称呼，不能只按山+人中性翻译。',
 'hill + -y/-ock/side/top/crest；up/down/foot/mole/ant + hill；hill + billy。',
 [['基本丘陵与大小','hill · hilly · hillock'],['方向和位置','uphill · downhill · hillside · hilltop · hillcrest · foothill'],['动物土堆和居民称呼','molehill · anthill · hillbilly']],
 'hill/mountain 不靠全世界统一高度线；uphill 艰难、downhill 可恶化；molehill 鼹鼠、anthill 蚂蚁。',
 'The hilly path led downhill past a small anthill.\n\n起伏的小路向下延伸，经过一座小蚁丘。',
 'hill hilly hillock uphill downhill hillside hilltop hillcrest foothill molehill anthill hillbilly')
MU=[['古英语 morþor、myrþra 等 → 中古英语 murdre → murder','秘密、非法杀人等旧义；d 形可能受法语同族形式影响'],['现代 murder','谋杀；把表演做坏、把事情说得极难等夸张用法']]
def M(f,m):return MU+[[f,m]]
W('murder','英 /ˈmɜːdə/；美 /ˈmɜːrdər/','谋杀；谋杀某人；糟蹋作品、把某事做坏〔夸张〕',
 '核心是严重的非法杀人；日常夸张里把一首歌唱毁了，也会说 murder a song。',
 '接古英语 morþor 等旧杀人词，现代 d 形式可能受法语同族拼写影响。现代法律细节依制度，学习先掌握谋杀与 kill 更宽泛的区别。',MU,
 'a murder case 谋杀案，commit murder 犯谋杀罪，murder a song 把歌唱毁了；The traffic was murder. 交通糟透了。',
 'a murder case；commit murder；murder a song；the traffic was murder。',
 'kill 可杀死细菌、关掉进程等，murder 基本义更具体、评价更重；bad singing 的 murder 是夸张，不能照字面读成真实杀人。',
 ('The novel begins with a murder in a quiet village.','小说从宁静村庄里的一桩谋杀案写起。'),('He joked that the singer had murdered his favourite song.','他开玩笑说，歌手把他最喜欢的歌唱毁了。'),sources=['https://www.etymonline.com/word/murder','https://en.wiktionary.org/wiki/murder#English'])
W('murderer','英 /ˈmɜːdərə/；美 /ˈmɜːrdərər/','谋杀者；凶手',
 '从那件谋杀，转到实施谋杀的那个人；不是泛指所有故事里看着可疑的人。',
 'murder + -er，中古英语已有 murderere 等对应形式。人物后缀与基础词末尾 er 是不同层次，读起来有重复音节。',M('murder + -er → murderer','实施谋杀的人'),
 'the murderer in the novel 小说中的凶手，identify the murderer 确认凶手。',
 'identify the murderer；the murderer in the novel；a convicted murderer。',
 'suspect 嫌疑人不等于已确定的 murderer；在推理小说里，这正是开头猜测与结尾揭晓的区别。',
 ('The detective finally identified the murderer.','侦探终于确认了凶手。'),('The reader does not discover who the murderer is until the final chapter.','读者直到最后一章才知道谁是凶手。'))
W('murderous','英 /ˈmɜːdərəs/；美 /ˈmɜːrdərəs/','凶狠、意欲杀人的；极难忍受、危险的〔夸张〕',
 '一个眼神像要杀人，或一段攀登难得让人招架不住；常比 murder 基本行为义宽。',
 'murder + -ous，形成具有相关性质的形容词。凶狠、致命与极其艰难的夸张用法要按对象分清。',M('murder + -ous → murderous','杀人般凶狠；极其危险、难熬的'),
 'a murderous look 凶狠眼神，murderous heat 难熬酷热，a murderous pace 极难承受的速度。',
 'a murderous look；murderous heat；a murderous pace。',
 'murderous 有凶狠、强烈危险或夸张程度，murderer 是人；a murderous look 不自动证明某人实际有犯罪意图。',
 ('She gave him a murderous look.','她狠狠瞪了他一眼。'),('The runners struggled to maintain the murderous pace.','跑者努力维持那种难以承受的速度。'))
R('B3509','谋杀行为与执行者、凶狠性质；夸张用法分开','MURDER：严重杀人词，也有把作品做毁、极难受的夸张','murder → murderer → murderous；基本名动词、人物、性质按顺序。',
 '旧英语词形后来可能受法语影响。词义学习不代替具体法律分类；故事里的嫌疑人与已揭晓凶手要分清。',
 'murder + -er/-ous；基础词内的 er 与人物后缀另加 -er 不同层次。',
 [['行为、人物与性质','murder · murderer · murderous']],
 'kill 广于 murder；suspect 不等于 murderer；murderous look 凶狠眼神是描述不自动证明实际杀人意图。',
 'The detective recognized the murderer despite his harmless appearance.\n\n尽管外表无害，侦探还是认出了凶手。',
 'murder murderer murderous')
PU=[['古法语 porposer、purposer → porpos、purpos','提出、打算 → 意图、目标；词形受 poser 等影响'],['中古英语 purpos → purpose','目标、意图、用途；动词意欲'],['远源比较','对应拉丁提出概念，但法语词形经过改造，不是一条字形原样直借线']]
def P(f,m):return PU+[[f,m]]
W('purpose','英 /ˈpɜːpəs/；美 /ˈpɜːrpəs/','目的；用途；意图；决心、目标感',
 '你做这件事到底为了什么？工具做出来拿来干什么？答案就是它的 purpose。',
 '经法语 purpos、porpos 意图等进入中古英语，与 por- 向前、poser 放置等形式相联，背后对应提出、放到面前的概念。法语词形有改造，不能直接把现代 pur 当万能前缀。',PU,
 'the purpose of the visit 来访目的，serve a purpose 起到作用，on purpose 故意，a sense of purpose 目标感。',
 'the purpose of；serve a purpose；on purpose；a sense of purpose。',
 'purpose 目的、用途，reason 原因、理由。What is it for? 常问用途，不只是追究它为什么存在。',
 ('What is the purpose of this meeting?','这次会议的目的是什么？'),('I didn’t break it on purpose.','我不是故意弄坏它的。'),sources=['https://www.etymonline.com/word/purpose','https://en.wiktionary.org/wiki/purpose#English'])
W('purposely','英 /ˈpɜːpəsli/；美 /ˈpɜːrpəsli/','故意地；特意地',
 '不是手滑、碰巧，而是你本来就打算这样做。',
 'purpose + -ly，中古英语已有 purposly 等形式。这个副词接意图，不保证动机好坏。',P('purpose + -ly → purposely','有意图地、故意地'),
 'purposely leave 故意留下、离开，purposely avoid 特意避开，not purposely 不是故意的。',
 'purposely avoid；purposely leave；purposely designed。',
 'purposely 通常相当于 on purpose；purposefully 常更强调有目标、坚定地做，两者用法有重合，别把后者所有句子都判错。',
 ('She purposely left the last page blank.','她特意把最后一页留白。'),('He purposely avoided the crowded street.','他特意避开了拥挤街道。'))
W('purposeful','英 /ˈpɜːpəsfəl/；美 /ˈpɜːrpəsfəl/','有明确目标的；坚定有效的；有意图的',
 '知道下一步要往哪走，动作不漫无目的；脚步、讨论、工作都可带这种劲头。',
 'purpose + -ful，表示有目的、目标感；不是简单比 purposely 更长，所以只能当副词。',P('purpose + -ful → purposeful','有目标、意图；行动坚定'),
 'a purposeful walk 目标明确、坚定的步伐，purposeful activity 有目的的活动，a purposeful discussion 有明确目标的讨论。',
 'a purposeful walk；purposeful activity；a purposeful discussion。',
 'purposeful 有目标，useful 有用；目标明确的行动未必对每个人有用，评价维度不同。',
 ('She crossed the room with a purposeful stride.','她迈着坚定步子穿过房间。'),('The meeting became more purposeful once we set an agenda.','定好议程后，会议更有明确目标了。'))
W('purposefully','英 /ˈpɜːpəsfəli/；美 /ˈpɜːrpəsfəli/','有明确目标、坚定地；故意地〔亦有此用法〕',
 '人知道自己要做什么，于是动作果断地朝着目标去；也可能单纯说有意。',
 'purposeful + -ly。现代常见坚定、有目标义，也有人用来表示故意，因此实际句子需看动词和场景。',P('purposeful + -ly → purposefully','有目标、果断地；亦可有意地'),
 'walk purposefully 坚定有目标地走，work purposefully 有目的地工作。',
 'walk purposefully；work purposefully；move purposefully。',
 'purposely leave a gap 故意留空，walk purposefully 朝目标坚定走；这是常见分工，不是两个副词绝对不许重合的硬规则。',
 ('He walked purposefully towards the exit.','他目标明确地朝出口走去。'),('The group worked purposefully through the agenda.','小组按着议程有条不紊、目标明确地推进工作。'))
W('purposeless','英 /ˈpɜːpəsləs/；美 /ˈpɜːrpəsləs/','无目的的；无意义、无作用的',
 '不知道为什么做、要走向哪儿，或做了也看不出用途；强调缺少目的和方向。',
 'purpose + -less，否定目的、用途。描述感受时不等于客观证明人的生活没有价值。',P('purpose + -less → purposeless','缺少目的、用途或目标感'),
 'purposeless wandering 漫无目的游荡，feel purposeless 觉得失去目标。',
 'purposeless wandering；feel purposeless；a purposeless activity。',
 'purposeless 没目的，unplanned 没事先计划；临时决定的活动也可以很有明确目的。',
 ('He spent the afternoon in purposeless wandering.','他漫无目的地游荡了一下午。'),('Without a clear goal, the work began to feel purposeless.','没有清楚目标，工作开始让人觉得没了意义。'))
W('repurpose','英 /ˌriːˈpɜːpəs/；美 /ˌriːˈpɜːrpəs/','改作他用；改变用途',
 '旧东西不一定扔掉，换个用处继续工作：仓库变图书馆，旧盒子变收纳。',
 're- 重新 + purpose，用途改变的动词。这里重点是新用途，不只是原样再用一次。',P('re- + purpose → repurpose','重新指定用途、改作他用'),
 'repurpose a building 改变建筑用途，repurpose old materials 旧材料改作他用。',
 'repurpose a building；repurpose old materials；repurpose for。',
 'reuse 再用可以用途不变，repurpose 强调换用途；recycle 常更强调材料回收再加工，做法不必相同。',
 ('The warehouse was repurposed as a community library.','仓库被改作社区图书馆。'),('She repurposed old jars as flower vases.','她把旧罐子改成了花瓶。'))
R('B3762','为什么做、用来做什么；有意、目标明确与改变用途','PURPOSE：摆在心里的目标；行动为了什么、东西拿来干什么','purpose → purposely；purposeful → purposefully 连着读，purposeless 否定，repurpose 改用途，multipurpose 共享。',
 '法语意图词进入英语，词形有 poser 相关改造，不能只从现代字母发明 pur 的含义。常见副词分工也不写成绝对语言禁令。',
 'purpose + -ly/-ful/-less；purposeful + -ly；re-/multi- + purpose。',
 [['意图和行动方式','purpose · purposely · purposeful · purposefully'],['缺少、变更和多用途','purposeless · repurpose · multipurpose']],
 'purposely 常故意、purposefully 常坚定有目标，亦可重合；purposeful 不等于 useful；repurpose 换用途，reuse 可原样再用。',
 'They purposefully repurposed the room for a clear new purpose.\n\n他们目标明确地把房间改作他用，赋予它清楚的新用途。',
 'purpose purposely purposeful purposefully purposeless repurpose multipurpose')
if __name__=='__main__':save('continuation_20261030_bk',ROOTS,WORDS)
