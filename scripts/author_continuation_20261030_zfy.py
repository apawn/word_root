"""Following traces, retracing a route, retrieving and investigating."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
def S(word,base):
 return ['https://en.wiktionary.org/wiki/'+word+'#English','https://www.etymonline.com/word/'+base]
EXISTING_ROOT_ADDITIONS={
 'B4098':dict(words='track tracker trackers tracked untracked'.split(),label='track 的追踪者与未留下轨迹的状态',note='track 经法语 trac，较早来源未定，可能接日耳曼拖行材料。tracker 加 -er，untracked 中 un- 是否定，tracked 是加 -ed 的过去分词形容形式。'),
 'C1534':dict(words='trace traced tracing tracer tracers traceable untraceable traceless retrace retraces retraced retracing'.split(),label='trace：从描线、循迹到重走原路、查清来路',note='trace 经法语接拉丁 trahere、tractus 相关材料，部分早期词义顺序不清。retrace 经法语 retracer 等，内部为 re- 再、回加 trace 对应材料；描线与追查按场景区分。'),
 'C1208':dict(words='retrieve retrieves retrieved retrieving retriever retrievers retrieval retrievals retrace retraces retraced retracing'.split(),label='re-：取回、重新循迹，不只一律再做一次',note='retrieve 由法语 re- 加 trouver 找到一路借入，更远联系希腊 trop- 的分析有不确定性；retrieval 是去 e 加动作名词 -al。'),
 'B2613':dict(words='hunt hunts hunted hunting hunter hunters'.split(),label='hunt 的追猎和认真搜寻',note='承古英语 huntian，具体较远来路未定；与 hound 猎犬常搭配，但不把 hound 字母改动当作现代造 hunt 的规则。'),
 'C0221':dict(words='search searcher searchers research researched researching researcher researchers'.split(),label='search、research 的仔细查看与研究',note='search 经法语接晚期拉丁 circare，四处查看，联系 circus 圆；research 经法语 rechercher，re- 有加强、彻底的作用，现代研究不一定是别人研究过再研究一次。'),
}
TRACK=[['古法语 trac 痕迹 → 英语 track','较早可能联系日耳曼拖行词，但具体路线未定'],['track 名词痕迹 → track 动词追踪、记录','tracker 命名追踪者或装置；untracked 描述未被追踪或未留下轨迹']]
W('trackers','英 /ˈtrækəz/；美 /ˈtrækərz/','追踪者；追踪、记录装置或程序〔复数〕',
 '有人顺着脚印找动物，是 trackers；手环记录运动、装置记录物体位置，也可以是 trackers。共同点是沿着变化留下、读出记录。',
 'track + -er → tracker，再加复数 -s，词尾读 /z/；基础 track 经法语的痕迹词进入英语。',TRACK+[['track + -er + -s → trackers','多个循迹者、追踪记录装置或程序']],
 'animal trackers 动物踪迹追踪者；fitness trackers 运动记录设备；online trackers 网络追踪程序。',
 'experienced trackers；location trackers 位置追踪装置。',
 'tracker 只说追踪、记录角色，具体记录位置、活动还是网页访问，要看前面修饰词，不能一律译成定位器。',
 ('Experienced trackers followed the footprints through the mud.','有经验的追踪者顺着泥地里的脚印找了过去。'),('The study compared several fitness trackers.','这项研究比较了几种运动记录设备。'),sources=S('trackers','track'))
TRACE=[['拉丁 trahere 拉、拖 → tractus 等路线、拖出材料','经法语 tracier、trace 等进入英语；早期描线、追随义的具体发展并非全都清楚'],['沿线描、循迹找 → 描摹、追查、追溯','trace 的名词痕迹、微量义与动词用法并存，不只一种词性']]
W('traced','/treɪst/','追查、追溯了；描摹、沿线描出了',
 '把线索一段段接回去，查到源头，是 traced；把透明纸放在图上沿轮廓描，也叫 traced。两种场景都像沿着线走。',
 'trace 去 e 加完整 -ed，/s/ 后词尾读 /t/，结尾 /st/。基础词经法语接拉丁拖、描线材料。',TRACE+[['trace → traced','过去沿线描摹，或沿线索查清来路']],
 'traced the fault to a loose wire 把故障追查到一根松线；traced a map 描了一张地图；traced back to 追溯到。',
 'traced the source；traced the outline。',
 'tracked 更常跟踪位置、进展，traced 更容易强调循线查来源或描出轮廓；语境也有交叠。',
 ('We traced the noise to a loose panel on the door.','我们查出噪声来自门上一块松动的板。'),('She traced the outline of the leaf on thin paper.','她在薄纸上描出了叶子的轮廓。'),sources=S('traced','trace'))
W('tracers','英 /ˈtreɪsəz/；美 /ˈtreɪsərz/','示踪物、示踪剂；追踪装置、描摹者〔复数〕',
 '给本来难看清的流动放一个可追踪的标记，就像让它留下一条看得见的线；这些帮助循迹的东西叫 tracers。',
 'trace 去 e 加完整 -er → tracer，再加 -s；-er 可命名做描摹、追踪的人，也可命名帮助追踪的物质或装置。',TRACE+[['trace → tracer → tracers','循迹角色、材料或装置，再作复数']],
 'chemical tracers 化学示踪物；tracers in a flow experiment 流动实验中的示踪物；军事场景也可说曳光弹。',
 'use tracers to follow movement；fluorescent tracers 荧光示踪物。',
 'tracers 是用来追踪的对象、工具或标记，traces 是踪迹或微量本身；多一个 -er，角色就不同。',
 ('The researchers used tracers to study how the water moved.','研究人员用示踪物研究水怎样流动。'),('Tiny fluorescent tracers made the flow visible.','微小的荧光示踪物让流动变得可见。'),sources=S('tracers','trace'))
RETRACE=TRACE+[['法语 re- + tracer 等 → 英语 retrace','英语早期已有追溯源头义，后来也说沿原路返回；现代还能回顾经过']]
W('retrace','/ˌriːˈtreɪs/','沿原路返回；重走、重描；回顾经过',
 '东西丢了，先想自己走过哪儿，再沿刚才的路返回去找，这叫 retrace your steps。也能在脑里把事情经过重新走一遍。',
 '经法语 retracer 等借入，内部可对应 re- 再、回 + trace 沿线描、循迹；现代构词关系清楚，不把借入史略成英语当场拼造。',RETRACE,
 'retrace your steps 沿原路返回；retrace the route 重走路线；retrace the events 回顾事情经过。',
 'retrace the outline 重新描轮廓；retrace the journey 重走旅程。',
 'return 只说回来，retrace your steps 还明确沿先前经过的那段路返回，常用于寻找遗失物。',
 ('We had to retrace our steps to find the missing keys.','我们得沿原路返回，找丢失的钥匙。'),('The book helps readers retrace the events of that evening.','这本书帮助读者回顾那天晚上的事情经过。'),sources=S('retrace','retrace'))
W('retraces','/ˌriːˈtreɪsɪz/','沿原路返回、重走、回顾〔第三人称单数〕',
 '她从刚才走过的路往回找，或一段纪录片把一位人物的经历重新梳理出来，动词都可以用 retraces。',
 'retrace + -s，基础 /s/ 后词尾读 /ɪz/；前缀 re- 在这里保留 /riː/ 的再、回感觉。',RETRACE+[['retrace + -s → retraces','他、她重新沿先前路线或经过追寻']],
 'retraces her steps 沿她走过的路返回；retraces a journey 重走旅程；retraces the events 回顾经过。',
 'retraces the route on a map；retraces his early career。',
 'repeats 只说重复，retraces 通常保留路径、线条或先后经过的线索感。',
 ('She retraces her steps whenever she loses her keys.','她每次丢钥匙，都会沿走过的路返回寻找。'),('The documentary retraces his first journey across the country.','这部纪录片重走了他第一次穿越该国的旅程。'),sources=S('retraces','retrace'))
W('retraced','/ˌriːˈtreɪst/','沿原路返回了；重走、重描、回顾了',
 '找不到东西，沿刚才的脚步倒回去，再把经过查一遍；完成于过去时，就是 retraced。',
 'retrace 去 e 加完整 -ed，/s/ 后词尾读 /t/；/st/ 作为结尾，不读成 /sɪd/。',RETRACE+[['retrace → retraced','过去重新循原来的路径、线条或经过']],
 'retraced our steps 沿原路返回了；retraced the outline 重新描轮廓；retraced the sequence 回顾顺序。',
 'retraced the route；retraced the final hours。',
 'retraced the route 可以真走，也可以在地图上沿线查看；具体介质由句子说明。',
 ('We retraced our steps and found the scarf on a bench.','我们沿原路返回，在长椅上找到了围巾。'),('He retraced the route with his finger on the map.','他用手指在地图上重新沿着那条路线划了一遍。'),sources=S('retraced','retrace'))
W('retracing','/ˌriːˈtreɪsɪŋ/','正在沿原路返回、重走；回顾、重描',
 '人正一步步走回刚才经过的地方，或正顺着记忆梳理事情的前后，这段过程叫 retracing。',
 'retrace 去 e 加 -ing；re- 作用于 trace，外层 -ing 再把整个动作变成进行形式或过程名词。',RETRACE+[['retrace → retracing','沿先前路线、经过重新追寻的过程']],
 'retracing our steps 沿原路返回；retracing the history 回顾历史；retracing a line 重新描线。',
 'spend the morning retracing a route；retracing a family’s journey。',
 'retracing 通常指已有一条路线、经过可循；exploring 可以面对还不熟悉、未确定的地方。',
 ('We spent the morning retracing the route of our first walk.','我们上午重走了第一次散步的路线。'),('She was retracing the events in her mind.','她正在脑海里回顾事情经过。'),sources=S('retracing','retrace'))
W('untraceable','/ʌnˈtreɪsəbəl/','查不到来源、去向的；无法追踪的',
 '手里有一条线索，却怎么往回接都接不到源头，或怎么查也找不到人去了哪里，这种查不出的状态叫 untraceable。',
 '否定 un- + traceable；内层 trace + -able 保留 e，再加 un-。这里 un- 是否定，不是拉丁“一个”的词根。',TRACE+[['trace → traceable → untraceable','可追查的 → 不可追查、查不到的']],
 'an untraceable source 无法查明的来源；untraceable calls 查不清来源的电话；remain untraceable 仍然查不到。',
 'untraceable origins；become untraceable。',
 'untraceable 描述在相应条件下查不到，不是凭空断言任何时代、任何方法都永远查不到。',
 ('The quotation was copied so often that its original source became untraceable.','那句话被反复转抄，原始出处已经查不到了。'),('Several missing items remain untraceable.','几件丢失的物品仍然查不到去向。'),sources=S('untraceable','trace'))
W('traceless','/ˈtreɪsləs/','不留痕迹的；没有踪迹的',
 '东西曾在这里，后来拿走、擦掉，连一条能看出的痕迹都没留下，这种样子叫 traceless。这个词较偏书面描写。',
 'trace + 缺少、没有的 -less，保留基础 e；现代按痕迹名词来理解。',TRACE+[['trace + -less → traceless','缺少可见、可寻的痕迹']],
 'a traceless disappearance 消失得不留痕迹；leave a surface traceless 让表面不留痕迹，实际表达常用 leave no trace。',
 'traceless removal；a traceless vanishing act。',
 'traceless 突出没留痕迹，untraceable 突出查不出来源、去向；留下了一点线索，也仍可能暂时 untraceable。',
 ('In the story, the magician makes a traceless disappearance.','故事里，魔术师消失得不留痕迹。'),('The film turns on the seemingly traceless theft of a painting.','这部电影围绕一幅画看似未留痕迹的失窃展开。'),sources=S('traceless','trace'))
W('untracked','/ʌnˈtrækt/','未被追踪、记录的；未留下踩踏轨迹的',
 '这次活动没有被设备记下来，是 untracked；新雪上还没有滑雪留下的线，也叫 untracked snow。两种都是没有 track，但缺的不是同一种轨迹。',
 '否定 un- + tracked；track + -ed 的词尾在 /k/ 后读 /t/。现代不同场景借用踪迹、记录的不同义。',TRACK+[['track → tracked → untracked','已被追踪、留下轨迹的状态被否定']],
 'untracked snow 未留下滑行痕迹的新雪；an untracked change 没有被记录的变化；untracked files 在版本管理中未纳入跟踪的文件。',
 'an untracked activity；an untracked path。',
 'untracked 说目前没被追踪、记录；untraceable 说追查不出来。没有记录并不保证之后无法查出。',
 ('We found a stretch of untracked snow beyond the trees.','我们在树林那边发现一片还没有滑行痕迹的雪地。'),('The folder contains several untracked files.','这个文件夹里有几个尚未纳入版本跟踪的文件。'),sources=S('untracked','track'))
RETRIEVE=[['古法语 re- 再 + trouver、retreuver 等找到材料 → retrieve','早期英语用于再次找到、发现，包含狗寻找猎物的场景'],['找回 → 取回物品、唤回记忆、获取存储信息','更远联系希腊 trop- 的路线是一种分析，不作唯一确定起点']]
W('retrieves','/rɪˈtriːvz/','取回、找回；检索〔第三人称单数〕',
 '球扔出去，狗找到后带回；文件存在库里，程序把它调出来，都可以用 retrieves：目标是把要的东西重新拿到手。',
 'retrieve + -s，/v/ 后词尾读 /z/；e 不发音，声音落在 /triːv/。基础词经法语的再、找到材料借入。',RETRIEVE+[['retrieve + -s → retrieves','它、他、她取回实物或调出存储信息']],
 'retrieves the ball 把球捡回；retrieves a file 调出文件；retrieves information 检索信息。',
 'retrieves the latest record；retrieves luggage from storage。',
 'searches 查找，可以还没找到；retrieves 通常把取回、调出的结果带出来，两个动作在系统里也可前后相接。',
 ('The dog retrieves the ball and drops it at my feet.','狗把球捡回来，放在我脚边。'),('The program retrieves the latest record from the database.','程序从数据库中调出最新记录。'),sources=S('retrieves','retrieve'))
W('retrieved','/rɪˈtriːvd/','取回、找回了；检索、调出了',
 '东西落下了，后来去拿回来；资料存在系统里，后来调出来，这种已发生的取回动作叫 retrieved。',
 'retrieve 去不发音 e，加完整 -ed，词尾读 /d/；/vd/ 连着发，不增 /ɪd/。',RETRIEVE+[['retrieve → retrieved','过去重新得到实物，或取出存储内容']],
 'retrieved the keys 找回钥匙；retrieved the document 调出文件；retrieved from a database 从数据库检索得来。',
 'retrieved the bag；successfully retrieved 成功取回。',
 'retrieved 不自动等于修复损坏；从备份取回一份完好的文件可以说 retrieved，修好损坏的文件另需说明。',
 ('I retrieved my bag from the luggage room.','我从行李寄存室取回了包。'),('She retrieved an old email to check the date.','她调出一封旧邮件，核对日期。'),sources=S('retrieved','retrieve'))
W('retrieving','/rɪˈtriːvɪŋ/','正在取回、找回、检索',
 '东西还没回到手里，人正在去拿；结果还没显示，程序正在调数据，这个过程叫 retrieving。',
 'retrieve 去 e 加 -ing；保留 /v/，不把整个尾部误读成不发音。',RETRIEVE+[['retrieve → retrieving','取回实物或调出信息的过程']],
 'retrieving the ball 正在捡回球；retrieving data 正在检索数据；retrieving a memory 唤回记忆。',
 'a message saying retrieving files；help with retrieving lost items。',
 'retrieving 是取回过程；retrieval 是这个动作、过程的名词。动词句和过程名称各用自己的形式。',
 ('The dog is retrieving the stick from the water.','狗正在水里把木棍叼回来。'),('The screen says it is retrieving the saved files.','屏幕显示正在调取已保存的文件。'),sources=S('retrieving','retrieve'))
W('retrievers','/rɪˈtriːvəz/〔英〕；/rɪˈtriːvərz/〔美〕','寻回犬；取回者、检索装置或程序〔复数〕',
 '猎物落在远处，训练过的狗去找回来；现代大家熟悉的寻回犬就叫 retrievers。工作角色同样能扩到取回信息的程序。',
 'retrieve 去 e 加完整 -er → retriever，再加 -s；不要只写成加 -r，虽然最后拼写看起来只多了 r。',RETRIEVE+[['retrieve → retriever → retrievers','把取回动作变成行动者，常指训练取回物品的犬，再作复数']],
 'golden retrievers 金毛寻回犬；Labrador retrievers 拉布拉多寻回犬；data retrievers 信息检索工具，需看语境。',
 'trained retrievers；retrievers bringing back the ball。',
 'retrievers 是角色或犬类名词，retrieves 才是动词三单；retrievals 则是多次取回或检索过程。',
 ('Two golden retrievers were playing beside the lake.','两只金毛寻回犬在湖边玩。'),('The trainer teaches retrievers to bring objects back gently.','训练员教寻回犬轻轻地把物品叼回来。'),sources=S('retrievers','retrieve'))
W('retrievals','/rɪˈtriːvəlz/','取回、找回、检索〔多次、多个过程〕',
 '不是讨论一般的检索能力，而是数一笔、一笔实际发生的取回操作，比如一天调取了多少次记录，就可以用 retrievals。',
 'retrieve 去 e 加动作名词 -al → retrieval，再加复数 -s；名词后缀 -al 在这里指过程，不是形容词的“与……有关”。',RETRIEVE+[['retrieve → retrieval → retrievals','取回过程名词，再数作多次检索、取回']],
 'successful retrievals 成功取回、检索的次数；document retrievals 文档调取操作。一般说信息检索领域时多用 information retrieval 单数形式。',
 'repeated retrievals；count the retrievals。',
 'retrieval 常作过程总称，retrievals 把具体操作一项项数出来；不是所有不可数用法都需要加 s。',
 ('The log records how many document retrievals were completed.','日志记录了完成多少次文档调取。'),('Repeated retrievals of the same file slowed the system.','反复调取同一个文件拖慢了系统。'),sources=S('retrievals','retrieve'))
HUNT=[['古英语 huntian → hunt','打猎、追猎；与抓取等旧词的较远关系有讨论'],['追猎 → 努力寻找某人、某物','现代也 hunt for a flat、hunt for keys；不是只用于动物']]
W('hunts','/hʌnts/','追猎、努力寻找〔第三人称单数〕；搜寻、狩猎活动〔复数〕',
 '猫在草里找猎物，是 hunts；人翻箱倒柜找钥匙，也有 hunt 的认真搜寻感。几次搜寻活动则能作名词 hunts。',
 'hunt + -s，/t/ 后读 /s/，结尾 /nts/；动词三单和名词复数同形。',HUNT+[['hunt + -s → hunts','它、他、她追猎或搜寻；多次寻找活动']],
 'hunts for food 觅食；hunts for a job 找工作；treasure hunts 寻宝活动。',
 'hunts at night；hunts through the drawer 翻抽屉寻找。',
 'hunts for 后接要找的目标；hunts through 后接翻找的范围。for keys、through the bag，关注点不同。',
 ('The owl hunts for mice at night.','猫头鹰夜里捕食老鼠。'),('The children love treasure hunts in the garden.','孩子们喜欢在花园里玩寻宝游戏。'),sources=S('hunts','hunt'))
W('hunted','/ˈhʌntɪd/','追猎、努力寻找了；被追捕的；惊惶不安的',
 '过去认真找了一圈，是 hunted；人像一直被追着、没有安全感，神情也可以叫 a hunted look。',
 'hunt + 完整 -ed，基础 /t/ 后词尾读 /ɪd/；既可作过去式、被动形式，也有惊惶神态的形容用法。',HUNT+[['hunt + -ed → hunted','过去追猎、搜寻；被追逐状态又可形容紧张惊惶']],
 'hunted for the keys 到处找钥匙；hunted animals 被追猎的动物；a hunted expression 惊惶的神情。',
 'hunted through the cupboard；looked tired and hunted。',
 'hunted look 是神态比喻，不要求真有猎人在身后；普通 looked for 只说找，不突出费力翻找的过程。',
 ('We hunted for the missing key for an hour.','我们到处找那把丢失的钥匙，找了一个小时。'),('He had a tired, hunted look on his face.','他脸上带着疲倦、惊惶不安的神情。'),sources=S('hunted','hunt'))
SEARCH=[['拉丁 circus 圆 → 晚期拉丁 circare 四处查看','经古法语 cerchier 等 → 英语 search 仔细查找'],['search + -er → searcher；法语 recercher → research','research 中 re- 可加强仔细、彻底的意思，不能一律解释成再次搜索']]
W('searchers','英 /ˈsɜːtʃəz/；美 /ˈsɝːtʃərz/','搜寻者、查找者〔复数〕',
 '人分头在树林、街道或文件堆里找目标，把这些正在寻找的人当成一组，就叫 searchers。',
 'search + -er → searcher，再加复数 -s；-er 点名进行查找的人，基础 search 经法语接四处查看材料。',SEARCH+[['search + -er + -s → searchers','多个正在搜寻、查找的行动者']],
 'searchers looking for a missing walker 寻找失踪徒步者的搜寻人员；online searchers 在网上查资料的人。',
 'a team of searchers；searchers combing the woods。',
 'searchers 进行查找，researchers 通常做系统研究；两者有相关词族联系，现代角色并不完全相同。',
 ('The searchers found fresh footprints near the river.','搜寻人员在河边发现了新脚印。'),('Several searchers checked the empty buildings.','几名搜寻人员检查了那些空建筑。'),sources=S('searchers','search'))
W('researched','英 /rɪˈsɜːtʃt/；美 /rɪˈsɝːtʃt/，美式也常重读首音节','研究、调查了；经过查证的',
 '写文章前查书、访谈、核对资料，把题目认真弄清楚，过去这个过程叫 researched。它不要求以前有人研究过，自己再做第二遍。',
 'research + 完整 -ed，/tʃ/ 后词尾读 /t/；基础词经法语 recercher 借入，re- 在这里可有加强作用。',SEARCH+[['research + -ed → researched','过去仔细调查、研究；也可形容内容经过研究']],
 'researched the topic 研究了这个题目；a carefully researched article 一篇认真查证的文章。',
 'well researched 资料查证充分的；researched the history of the building。',
 'researched 比 searched 更常强调围绕题目收集、分析资料；searched a room 则是检查房间找东西。',
 ('She researched the history of the house before writing the article.','写文章前，她研究了这栋房子的历史。'),('The book is clearly written and thoroughly researched.','这本书写得清楚，资料也查证得很充分。'),sources=S('researched','research'))
W('researching','英 /rɪˈsɜːtʃɪŋ/；美 /rɪˈsɝːtʃɪŋ/，美式也常重读首音节','正在研究、调查；作研究',
 '题目还在一点点查清，资料还在继续收集、比较、核对，这段进行中的工作就叫 researching。',
 'research + -ing；research 的名词、动词分别有法语背景，现代动词可直接加这个动作词尾。',SEARCH+[['research + -ing → researching','仔细调查、研究正在进行；也可作为研究过程的表达']],
 'researching a topic 研究题目；researching into a question 调查某问题；spend time researching 花时间作研究。',
 'researching the family history；researching a new book 为新书查资料。',
 'researching a book 常是为写书查资料，不一定是在研究一本已出版的书；宾语的具体关系需结合上下文。',
 ('I am researching the history of this neighbourhood.','我正在研究这一带的历史。'),('She spent months researching her new book.','她为写新书花了几个月查资料。'),sources=S('researching','research'))
def extend_lessons():
 extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_zfy',ROOTS,WORDS)
 extend_lessons()
