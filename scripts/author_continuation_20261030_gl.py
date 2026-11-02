"""Pipe, raw and off: conduits, unfinished states and disconnection."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
P=[['古英语 pīpe → 中古英语 pipe','管状吹奏乐器、管道；与拉丁拟声词材料有关'],['英语 pipe','中空管；吹奏、通过管路输送等动作']]
W('pipe','/paɪp/','管子、管道；管乐器；烟斗；用管输送、吹奏',
 '一根中间空的管，气、水能从里面过；拿来吹可以发声，拿来输送就变管道。烟斗也接管状器物这一家。',
 '古英语 pīpe 已有乐器、通道义，和拉丁 pīpa、pipāre 鸣叫等拟声材料相关，借入、影响路线较早。现代 pipe 不是 pi + pe。',P,
 'a water pipe 水管，organ pipes 管风琴音管，pipe water into a building 把水经管道引入，pipe up 突然开口说话。',
 'a water pipe；organ pipes；pipe water into；pipe up。',
 'pipe 常是输送或发声用的管，tube 更泛指中空管状物；实际器材命名有重叠，不用材质硬分绝对界线。',
 ('A water pipe burst beneath the road.','路下一根水管爆裂了。'),('A child at the back suddenly piped up with a question.','后排一个孩子突然开口问了个问题。'))
W('pipeline','/ˈpaɪplaɪn/','输送管线；处理流程；筹备中的项目渠道',
 '把一段段管接成一条长路，东西沿它流动；信息、任务也能像这样逐步进入下一环。',
 'pipe 管道 + line 线路，先是管线，再借给信息处理、项目准备等连续流程。现代计算中的每一阶段不一定真有管子。',P+[['pipe + line → pipeline','相连的管线 → 连续传送、处理的流程']],
 'an oil pipeline 输油管道，a data pipeline 数据处理流程，in the pipeline 正在筹备、进行中；不保证所有筹备项目最后都会发布。',
 'an oil pipeline；a data pipeline；in the pipeline。',
 'pipeline 是连贯输送或分阶段处理的路，deadline 是截止时间；in the pipeline 不是已经完成。',
 ('The pipeline carries water to the coast.','这条管线把水输送到沿海。'),('Several new products are in the pipeline.','有几款新产品正在筹备中。'))
W('piper','英 /ˈpaɪpə/；美 /ˈpaɪpər/','吹笛、吹管乐器的人；风笛手',
 'pipe 在这里选吹奏乐器那一支，-er 接人：拿着笛或风笛吹的人。',
 'pipe 去末尾 e + -er，中古英语已有 piper。不是安装水管的工人，那常叫 plumber。',P+[['pipe 乐器、吹奏 + -er → piper','吹管乐器或风笛的人']],
 'a Scottish piper 苏格兰风笛手，a lone piper 一位独奏风笛手；pay the piper 可比喻承担代价。',
 'a Scottish piper；a lone piper；pay the piper。',
 'piper 音乐表演者，plumber 管道工；同一个 pipe 有两支义，人物词按习惯选，不是所有做管道工作的人都 piper。',
 ('A lone piper played outside the hall.','一位风笛手在大厅外独奏。'),('The piper led the procession through the town.','风笛手领着队伍穿过小镇。'))
W('drainpipe','/ˈdreɪnpaɪp/','排水管、落水管',
 '把屋顶、地面等积水引走的管；drain 先告诉你它的任务是排水。',
 'drain 排走液体 + pipe 管。英式常可指外墙把屋顶水槽的雨水往下带的管，范围也可更一般。',P+[['drain + pipe → drainpipe','排出雨水等液体的管道']],
 'a blocked drainpipe 堵住的排水管，a leaking drainpipe 漏水的落水管；drainpipe trousers 借管子形状说窄直裤腿。',
 'a blocked drainpipe；a leaking drainpipe；drainpipe trousers。',
 'drainpipe 排水，water supply pipe 供水；pipe 都是管，前半段告诉你水往哪类用途去。',
 ('Leaves had blocked the drainpipe.','树叶堵住了排水管。'),('Rainwater ran down the drainpipe beside the window.','雨水沿窗边的落水管流下。'))
W('stovepipe','英 /ˈstəʊvpaɪp/；美 /ˈstoʊvpaɪp/','炉烟管；信息各自封闭的渠道〔比喻〕',
 '一根烟管直直向上，烟只在自己的管里走；组织中的信息若也只在一条竖道里流、不横向共享，就有 stovepipe 的比喻。',
 'stove 炉子 + pipe 管，先指炉烟管；直筒形状还能修饰帽子，隔离通道画面又扩展到组织信息。',P+[['stove + pipe → stovepipe','炉子的烟管'],['形状、通道比喻','直筒帽；封闭分隔的信息渠道']],
 'a metal stovepipe 金属炉烟管，a stovepipe hat 高筒礼帽，stovepiped information 被分隔、不共享的信息。',
 'a metal stovepipe；a stovepipe hat；stovepiped information。',
 'pipeline 常强调连续传送、阶段相接；stovepipe 的组织比喻常批评各走各路，缺少横向联系。',
 ('Smoke rose through the metal stovepipe.','烟沿金属炉烟管升起。'),('The report criticizes the stovepiping of information between departments.','报告批评部门之间信息各自封闭、不相互共享。'))
R('B3181','中空管、管状乐器；输送与流通','PIPE：留出一条空道，让水、气、声音通过','pipe → piper 吹乐器的人；pipeline 连贯管线；drainpipe 排水；stovepipe 炉烟管、隔离渠道。',
 '一类管负责输送，一类管用来发声。再把流动搬到信息里，就能理解 pipeline 和 stovepipe 的不同感觉。',
 'pīpe → pipe；pipe + -er；pipe + line/work；drain/stove/wind/tail + pipe。',
 [['基本管和演奏者','pipe · piper'],['输送与系统','pipeline · pipework'],['不同用途的管','drainpipe · stovepipe · windpipe · tailpipe']],
 'piper/plumber 音乐表演与管道工；pipeline/stovepipe 连贯流程与隔离渠道；drainpipe 任务是排水。',
 'The piper waited while workers repaired a pipe beside the drainpipe.\n\n风笛手在一旁等着，工人正在落水管旁修一根管子。','pipe piper pipeline pipework drainpipe stovepipe windpipe tailpipe')
R0=[['古英语 hrēaw → 中古英语 raw → raw','生的、未煮熟的'],['英语扩展','未加工、未经训练；皮肤磨破、情绪未平复']]
W('raw','英 /rɔː/；美 /rɔː/，部分美式 /rɑː/','生的、未加工的；未经训练的；磨痛的、情绪刺痛的',
 '食物还没煮、材料还没加工；再把没经过处理搬到数据、新手、刚发生的伤痛上。皮肤被磨得失去保护，也会觉得 raw。',
 '接古英语 hrēaw，开头旧辅音后来简化；与 crude 等词有更远同源关系。现代 raw 不拆成 r + aw。',R0,
 'raw vegetables 生蔬菜，raw materials 原材料，raw data 原始数据，a raw recruit 新兵，raw emotion 未加掩饰或尚未平复的情绪。',
 'raw materials；raw data；raw talent；raw emotion。',
 'raw data 是尚未充分处理的数据，不等于假数据；raw talent 是尚待训练的天赋，不是没有能力。',
 ('The report includes both raw data and a summary.','报告同时包含原始数据和摘要。'),('His voice was raw after hours of shouting.','喊了几个小时后，他的嗓音嘶哑发涩。'))
W('rawness','英 /ˈrɔːnəs/；美 /ˈrɔːnəs/','生、未经加工的状态；粗粝感；刺痛、情绪未平复的状态',
 '不把表面磨光、不把感情修饰平顺，保留刚出来的棱角和刺痛感；评论表演时也可能正是欣赏这种真实劲。',
 'raw + -ness，形成状态、性质名词。具体是材料未处理还是情绪直露，要跟着修饰对象读。',R0+[['raw + -ness → rawness','生、未经处理、刺痛或直接袒露的性质']],
 'the rawness of his voice 嗓音的嘶哑粗粝，emotional rawness 情绪尚敏感、未平复，the rawness of the performance 表演的原生、粗粝感。',
 'emotional rawness；the rawness of the voice；the rawness of the performance。',
 'rawness 可以是未打磨，也可有直接、真切的艺术评价；不是所有场合都译成缺点、粗制滥造。',
 ('The rawness of her voice suited the song.','她嗓音里的粗粝感很适合这首歌。'),('The memoir preserves the emotional rawness of that year.','回忆录保留了那一年感情仍未平复的刺痛感。'))
R('B3437','生、未加工；尚未经处理或保护的状态','RAW：还没煮熟、打磨、整理，感觉直接露在外面','raw → rawness 状态；rawhide 接未鞣制兽皮的材料义。',
 '从生食走到原材料、原始数据很自然。磨痛的嗓子、刚受冲击的情绪，则让你想到保护和缓冲还没恢复。',
 'hrēaw → raw；raw + -ness → rawness；raw + hide → rawhide。',
 [['基本状态与性质','raw · rawness'],['材料组合','rawhide']],
 'raw/rawness 形容词与性质名词；raw data 不是假数据；rawhide 未鞣制不等于完全未清理。',
 'The raw recording preserves the rawness of her voice.\n\n未经处理的录音保留了她嗓音的粗粝感。','raw rawness rawhide')
W('offline','英 /ˌɒfˈlaɪn/；美 /ˌɔːfˈlaɪn/','离线的、离线地；线下的；会后另谈的',
 '原来接在一条线上，现在从线上脱开；电脑不联网，活动不在网上，会议里暂不公开展开的讨论，都能用不同层面的 offline。',
 'off- 脱开、不在 + line 线路。通信、计算中的离线后来扩展到实体活动；会议口语又借它说另找时间或小范围谈。',
 [['off + line → offline','不接线路、不在网络上'],['英语延伸','实体线下；把讨论移出当前会议']],
 'work offline 离线工作，an offline event 线下活动，take it offline 会后另谈。最后一句在开会时未必真要断网。',
 'work offline；an offline event；take the discussion offline。',
 'offline 可表示离线状态，也可指线下场景；offline map 离线地图仍可能显示在屏幕上，不一定是纸质。',
 ('Download the map so you can use it offline.','把地图下载下来，就能离线使用。'),('Let’s take this discussion offline after the meeting.','这个话题我们会后另谈吧。'))
R('A2124','离开、脱开、不在正常位置或状态','OFF-：从原来的接触、位置或路线离开','offline 脱开线路；offshore 离岸；offload 卸下；offbeat 偏离常规节拍或方式。',
 'off 的离开关系会落在空间、连接、节拍或工作负担上。复合词保留具体历史，offspring、offal 等也不能只逐字翻两个零件。',
 '古英语 of 等与现代 off 的关系 → off-；接 line/shore/site/load/hand/beat/side/shoot/spring 等形成不同组合。',
 [['位置、连接和场地','offline · offshore · offsite · offside'],['移开、卸下与偏开','offload · offhand · offbeat · offset'],['结果和旧组合','offspring · offshoot · offal']],
 'offline 会议口语未必断网；offhand 可随口、不客气；offspring 子女后代不当作弹簧。',
 'The offshore team downloaded the files to work offline.\n\n离岸团队下载了文件，准备离线工作。','offline offshore offsite offside offload offhand offbeat offset offspring offshoot offal')
if __name__=='__main__':save('continuation_20261030_gl',ROOTS,WORDS)
