"""Track, choice, consider and close common extensions."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
T=[['法语 trac 踪迹 → 中古英语 trak → track','足迹、行经路线；更早可能日耳曼来源，路线未定'],['现代 track','轨迹、跑道、轨道 → 追踪；音乐录音的一轨、一首']]
def TH(f,m):return T+[[f,m]]
W('track','/træk/','踪迹；轨道、跑道；曲目；追踪、记录',
 '地上留下的脚印、车走的轨道都能看出走过哪里；持续记一件事的变化，也像沿着踪迹跟下去。',
 '经法语 trac 接中古英语，较早来源可能日耳曼语但具体路线不定。录音轨与曲目义按记录、播放通路的发展理解。',T,
 'animal tracks 动物足迹，a railway track 铁轨，a running track 跑道，track an order 跟踪订单；keep track of 持续掌握。',
 'keep track of；on track；track an order；an album track。',
 'track 与 trace 踪迹相关意义有重合，但不按两者相近就当现代同词；lose track of 是不再掌握情况。',
 ('We followed the animal tracks through the snow.','我们循着雪中的动物足迹前行。'),('You can track your order online.','你可以在线跟踪订单。'))
W('tracker','英 /ˈtrækə/；美 /ˈtrækər/','追踪者；跟踪器、记录工具',
 '可能是沿足迹追的人，也可能是自动记录位置、活动、任务进度的设备或软件。',
 'track + -er，执行追踪的主体；人物、仪器、软件功能都能用。',TH('track + -er → tracker','追踪者或追踪工具'),
 'a fitness tracker 运动记录器，a task tracker 任务跟踪工具，a skilled tracker 熟练追踪者。',
 'a fitness tracker；a task tracker；a skilled tracker。',
 'tracker 不必偷偷追踪，合法公开的包裹查询功能也可用；tracking 是活动，tracker 是执行主体。',
 ('Her fitness tracker records the number of steps she takes.','她的运动记录器记录步数。'),('The tracker found fresh footprints near the river.','追踪者在河边发现了新鲜脚印。'))
W('tracksuit','/ˈtræksuːt/','运动套装',
 '上衣、裤子成套，适合运动前后穿的衣服；名字来自跑道、田径场的使用背景。',
 'track 跑道、田径 + suit 套装，按运动场景命名。不是穿着铁路轨道做的衣服。',TH('track + suit → tracksuit','运动跑道使用的套装 → 运动服'),
 'a cotton tracksuit 棉质运动套装，tracksuit bottoms 运动裤，a tracksuit top 运动上衣。',
 'a tracksuit top；tracksuit bottoms；a matching tracksuit。',
 'tracksuit 常是成套休闲运动服，uniform 制服不一定同类；suit 单独也可正式西装。',
 ('He changed into a tracksuit after work.','下班后，他换上运动套装。'),('The team wore matching tracksuits on the journey.','旅途中，队员穿着统一运动套装。'))
W('trackpad','/ˈtrækpæd/','触控板',
 '手指在小面板上滑动，屏幕指针跟着走；常见于笔记本电脑。',
 'track 跟踪移动 + pad 面板，按感知手指运动的功能形成设备名。',TH('track + pad → trackpad','跟踪移动的面板 → 触控板'),
 'a laptop trackpad 笔记本触控板，a wireless trackpad 无线触控板；touchpad 常是同类通称。',
 'a laptop trackpad；use a trackpad；a wireless trackpad。',
 'trackpad 输入触控面板，mousepad 鼠标垫是承放鼠标的垫，不一定有感知功能。',
 ('She moved the cursor with the trackpad.','她用触控板移动光标。'),('The laptop’s trackpad supports several gestures.','笔记本触控板支持多种手势。'))
W('trackside','/ˈtræksaɪd/','轨道旁；跑道、赛道旁的',
 '站在跑道、铁轨或赛道的边上，side 说明相对位置。',
 'track + side，现代既可名词性指边旁地带，也可作修饰语，具体哪种轨道要看语境。',TH('track + side → trackside','轨道或赛道的边旁'),
 'trackside signals 铁路轨旁信号，trackside spectators 赛道旁观众。',
 'trackside signals；trackside spectators；a trackside camera。',
 'trackside 在旁边，on track 在轨道上或比喻进展正常；两个位置关系不同。',
 ('A trackside camera recorded the finish.','赛道旁摄像机记录了冲线。'),('Engineers checked the trackside signals.','工程师检查了轨旁信号。'))
W('trackless','/ˈtrækləs/','无路迹的；无轨的',
 '没有现成足迹、小路可循，或者设备不依赖铁轨运行。',
 'track + -less 没有；缺的是踪迹、路，还是轨道，要看对象。',TH('track + -less → trackless','没有路径、轨道的'),
 'a trackless forest 无路森林，trackless transport 无轨运输。',
 'a trackless forest；trackless land；a trackless vehicle。',
 'trackless 无轨、无路，traceless 不留痕迹是另词；不用仅凭 -less 抹掉前部差别。',
 ('The hikers crossed a stretch of trackless forest.','徒步者穿过一片无路可循的森林。'),('The exhibit compares rail systems with trackless vehicles.','展览比较轨道系统与无轨车辆。'))
R('B4098','踪迹、通路与持续追踪','TRACK：从留下的轨迹到记录变化','track 后接 tracker 执行者，再按运动服、触控板、轨旁、无轨分具体后部。',
 '法语踪迹词借入英语，更远来源有争论。录音曲目、软件跟踪不是都由实体铁路直接造出来。',
 'track → tracker、trackless；track + suit、pad、side；共享 soundtrack、racetrack、backtrack、tracklist。',
 [['基本轨迹与记录主体','track · tracker'],['运动与设备、位置','tracksuit · trackpad · trackside · trackless'],['已有复合词','soundtrack · racetrack · backtrack · tracklist']],
 'tracker 可人可设备；trackpad 触控板不同于 mousepad；trackside 在边旁。',
 'The tracker kept track of the team’s progress.\n\n跟踪工具持续记录了团队进展。',
 'track tracker tracksuit trackpad trackside trackless soundtrack racetrack backtrack tracklist')
C=[['法语 chois、choisir → 中古英语 chois → choice','选择；与 choose 的日耳曼词族有历史关系'],['现代 choice','选择行为、选项；精选、上好的']]
W('choice','/tʃɔɪs/','选择；选项；精选、上好的',
 '可以是做决定这件事，也可以是摆在面前可选的那一个；choice food 则强调选得好、品质上佳。',
 '名词借法语 chois，历史与 choose 词族有关，但不是现代 choose 换字母自动变出的名词。形容词还受到英语本族相关旧形式影响。',C,
 'make a choice 作选择，have no choice 别无选择，a good choice 好选择，choice cuts 精选肉块。',
 'make a choice；have no choice；a choice between；choice cuts。',
 'choose 动词，choice 名词；I choose this 与 This is my choice。choosy 挑剔是另一个形容词。',
 ('We have a choice between two routes.','我们有两条路线可选。'),('Choosing the earlier train was a good choice.','选择较早的火车是个好决定。'))
R('B3613','选择行为、可选项与精选性质','CHOICE：是选择本身，也是可选的那一个','把 choice 与已写 choose、chosen、choosy 放一起，对照动作、结果、选项与选择习惯。',
 'choice 借法语选择词，和 choose 有历史亲缘，不是现代临时改字母规则。',
 'choose → chosen、choosy；相关借词 choice。',
 [['相关动作、人物习惯与名词','choose · chosen · choosy · choice']],
 'choose 动词、choice 名词；choice 作精选形容词不等于 choosy 挑剔。',
 'The choosy customer made her choice.\n\n讲究的顾客作出了选择。',
 'choose chosen choosy choice')
CO=[['拉丁 considerare → 法语 considerer → 英语 consider','仔细察看、思量；更深的星辰词解释不作确定事实'],['现代 consider','考虑、斟酌 → 认为、看作；顾及']]
W('consider','英 /kənˈsɪdə/；美 /kənˈsɪdər/','考虑；认为；顾及',
 '先把一件事放在心里认真看一看，再决定怎么做；也可以表达你的判断、把它看成什么。',
 '借法语接拉丁 considerare 仔细察看、思量。常见与 sidus 星辰相联系的深层解释有讨论，不把仰望星空就想明白的故事当定论。',CO,
 'consider moving 考虑搬家，consider someone reliable 认为某人可靠，consider the cost 顾及成本。',
 'consider doing；consider someone to be；consider the cost；consider whether。',
 'consider doing 不通常说 consider to do 来表示考虑去做；be considered to be 则是另一被动判断结构。',
 ('We are considering moving to a smaller office.','我们在考虑搬到更小的办公室。'),('The plan must consider the needs of older residents.','方案必须顾及年长居民的需求。'))
W('considerable','英 /kənˈsɪdərəbl/；美 /kənˈsɪdərəbl/','相当大的；可观的；值得重视的',
 '量、程度大到不能当小事忽略，常是可观的一笔钱、明显的努力或差距。',
 'consider + -able，早有值得考虑、重视义，现代最常见固定为数量、程度相当大。不要机械只翻成能被考虑。',CO+[['consider + -able → considerable','值得重视 → 数量、程度可观']],
 'considerable effort 相当大的努力，considerable damage 严重损失，a considerable amount 可观数量。',
 'considerable effort；considerable damage；a considerable amount。',
 'considerable 可观，considerate 体贴是另一个常见词；拼写近不等于都在说替人着想。',
 ('The repairs required considerable effort.','维修需要相当大的努力。'),('There is a considerable difference between the two estimates.','两项估算差距很大。'))
R('B3929','认真思量与值得重视的数量','CONSIDER：认真看进心里；CONSIDERABLE：大到值得重视','基本 consider 后接 considerable 固定常用义，reconsider 已精讲共享。',
 '拉丁思量词经法语进入英语，更远的星辰说保留不确定。后缀可帮助记忆，不能替代实际固定词义。',
 'consider → considerable；re- + consider → reconsider。',
 [['思量、程度与重复','consider · considerable · reconsider']],
 'consider doing；considerable 相当大而非仅可考虑；considerate 体贴另词。',
 'After considerable discussion, we reconsidered the plan.\n\n经过充分讨论，我们重新考虑了方案。',
 'consider considerable reconsider')
ST=[['stretch 旧过去分词 → straight','被拉直、绷直 → 直的'],['现代 straight 派生','直线方向 → 明白、直接；使变直']]
W('straightforward','英 /ˌstreɪtˈfɔːwəd/；美 /ˌstreɪtˈfɔːrwərd/','简单明了的；坦率直接的',
 '路线直直向前，不绕圈；步骤容易明白，人说话也不拐弯。',
 'straight 直 + forward 向前，组合成不曲折、直接的形容词。现代常用于任务难度和表达态度。',ST+[['straight + forward → straightforward','直向前 → 简单明了、坦率']],
 'a straightforward task 简明任务，a straightforward answer 直截了当回答，straightforward instructions 清楚说明。',
 'a straightforward task；a straightforward answer；straightforward instructions。',
 'straightforward 不一定 rude 无礼；清楚坦率仍可礼貌。straightforward task 通常步骤不复杂，不保证完全不费时间。',
 ('The instructions are clear and straightforward.','说明清楚明了。'),('She gave me a straightforward answer.','她给了我一个直截了当的答复。'))
W('straighten','/ˈstreɪtən/','使变直；整理；理顺',
 '弯的拉直，歪的扶正，散乱的摆整齐；问题也可以像乱线一样理顺。',
 'straight + -en，使变得、变得，形成动词。现代字母 gh 不发音，读 /ˈstreɪtən/。',ST+[['straight + -en → straighten','变直 → 扶正、整理']],
 'straighten your back 挺直背，straighten a picture 扶正画，straighten things out 把事情理顺。',
 'straighten your back；straighten a picture；straighten out。',
 'straighten 变化动作，straight 直的状态；straighten out a misunderstanding 是澄清，不必实体拉伸。',
 ('He stopped to straighten the picture on the wall.','他停下来扶正墙上的画。'),('We need to straighten out the misunderstanding.','我们需要澄清误会。'))
R('B2915','直、直接与使变直','STRAIGHT：不弯；STRAIGHTFORWARD：不绕；STRAIGHTEN：理直','straight 已在 stretch 家族精讲，本页接简单坦率与变直、理顺动作。',
 'straight 为伸展词旧分词分化，现代形容词再派生动词 straighten 和复合 straightforward。',
 'straight → straightforward、straighten。',
 [['状态、表达与变化','straight · straightforward · straighten']],
 'straightforward 直接不等于无礼；straighten out 也可澄清；straight 的历史不替代现代词性。',
 'A straightforward conversation helped straighten things out.\n\n一次坦率交谈帮助把事情理顺。',
 'straight straightforward straighten')
FO=[['古英语 forgietan → 英语 forget','忘记；保留 forgot、forgotten 等不规则变化'],['forget + -able → forgettable','容易被忘 → 不值得记住、平庸']]
W('forgettable','英 /fəˈɡetəbl/；美 /fərˈɡetəbl/','容易被忘的；平淡、不值得记住的',
 '经历完没留下印象，通常是在说作品、表演平平，而不是说某人爱忘事。',
 'forget + -able，双写 t，形成容易被忘的评价形容词。unforgettable 难忘已精讲，同族放一起读。',FO,
 'a forgettable film 平淡电影，a forgettable performance 不出彩表演。',
 'a forgettable film；a forgettable performance；a forgettable season。',
 'forgettable 让别人记不住，forgetful 自己容易忘事；一个形容作品，一个常形容记性。',
 ('The film was pleasant but forgettable.','电影还算愉快，但没留下什么印象。'),('The team ended a forgettable season with a draw.','球队以一场平局结束了平淡的赛季。'))
R('B2866','忘记、易忘事与难忘','FORGET：先分谁忘、什么被忘','已有 forget、forgetful、unforgettable，共享加入 forgettable，区分记性与作品印象。',
 '古英语忘记动词，forget + -able 是被忘的可能性，不是记忆动作主体。',
 'forget → forgetful、forgettable → unforgettable。',
 [['动作、人物记性与对象印象','forget · forgetful · forgettable · unforgettable']],
 'forgetful 容易忘事，forgettable 不出彩容易被忘；unforgettable 难以忘记。',
 'The forgetful reviewer could not recall the forgettable film.\n\n那位健忘的评论者想不起那部平淡电影。',
 'forget forgetful forgettable unforgettable')
LO=[['lose 词族 → loss','失去、损失'],['loss + -less / -y → lossless、lossy','无信息损失与有信息损失的技术修饰语']]
W('lossless','英 /ˈlɒsləs/；美 /ˈlɔːsləs/','无损的；信息可完整还原的',
 '压缩后文件更小，但还能把原来的数据一项不差地还原回来。',
 'loss 损失 + -less 没有，技术语境强调在约定转换中信息不丢失，保留两个 s 再接 -less。',LO,
 'lossless compression 无损压缩，lossless audio 无损音频。具体能否完整还原要看整个流程，不只看格式标签。',
 'lossless compression；lossless audio；a lossless format。',
 'lossless 无损不等于文件绝不会坏；文件损坏、录音原始质量与压缩有无信息损失是不同问题。',
 ('The archive uses lossless compression to preserve the original data.','档案采用无损压缩保留原始数据。'),('The application can export a lossless audio file.','应用能导出无损音频文件。'))
W('lossy','英 /ˈlɒsi/；美 /ˈlɔːsi/','有损的；会舍弃部分信息的',
 '为了让文件更小，主动舍弃一些原始信息，之后通常不能逐项完整找回。',
 'loss + -y，形成有信息损失的技术形容词。不是 loose 松的加后缀。',LO,
 'lossy compression 有损压缩，lossy encoding 有损编码；选择舍弃什么由算法和参数决定。',
 'lossy compression；lossy encoding；a lossy format。',
 'lossy 有损不等于肉眼、耳朵一定马上察觉；感知质量、文件大小与可逆性需要分别看。',
 ('The image was saved with lossy compression to reduce its size.','图像采用有损压缩保存，以减小文件。'),('Repeated lossy conversion can discard more information.','反复有损转换可能丢掉更多信息。'))
R('B3079','失去与压缩中的信息损失','LOSS：损失；LOSSLESS、LOSSY：看原数据能否完整还原','loss 已精讲，本页将无损、有损配对讲清，不混淆文件故障与编码损失。',
 'loss 来自 lose 词族，技术后缀 -less、-y 分别表示无损和有损性质。',
 'loss → lossless、lossy。',
 [['基本损失与技术属性','loss · lossless · lossy']],
 'lossless 无损不保证存储永不损坏；lossy 不保证感知上明显差；loose 松是别词。',
 'Lossless and lossy compression make different trade-offs.\n\n无损与有损压缩采用不同取舍。',
 'loss lossless lossy')
if __name__=='__main__':save('continuation_20261030_j',ROOTS,WORDS)
