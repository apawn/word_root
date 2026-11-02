"""Activities: banking, gaming, scoring, planning and changing things."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'B2484':dict(words=['bank','banking'],label='bank → banking：银行业务；堆积、倾斜另看搭配',note='金融银行来自钱币柜台的词史，河岸、堆起支线分开说明。'),
 'B3191':dict(words=['game','gaming'],label='game → gaming：游戏活动与利用规则',note='本族娱乐词和英语动词用途，电脑游戏是现代扩展。'),
 'B3367':dict(words=['score','scoring'],label='score → scoring：刻记到记分、得分',note='北欧刻痕词相关，音乐配器、写总谱另有专业用途。'),
 'C0351':dict(words=['reduce','reducing'],label='reduce → reducing：带到较低数量或状态',note='拉丁往回与带领的组合，现代主要表达减少。'),
 'B3774':dict(words=['represent','representing'],label='represent → representing：使某人某事在场',note='拉丁展现词经法语等借入，现代代表、描绘、构成分开学。'),
 'C0415':dict(words=['refer','referring'],label='refer → referring：把注意带回某处',note='拉丁 re 与 ferre，英语末音节重读，ing 前双写 r。'),
 'C0958':dict(words=['prepare','preparing'],label='prepare → preparing：提前把事情备好',note='拉丁提前与备好词，经法语及 preparation 逆构影响形成英语动词。'),
 'C0156':dict(words=['claim','claiming'],label='claim → claiming：把要求或说法提出来',note='拉丁呼喊词经法语借入，声称与认领根据宾语区分。'),
 'C0278':dict(words=['cross','crossed','crossing'],label='cross → crossed → crossing：横过与交汇处',note='十字词的后续动词与 ing 名词，物理穿过和过街设施分别看。'),
 'C0305':dict(words=['defend','defending'],label='defend → defending：把攻击挡开',note='拉丁离开与击推词，经法语及拉丁借入。'),
 'B3633':dict(words=['drop','drops','dropping'],label='drop → drops → dropping：滴、掉落、减少',note='本族滴与滴落词，名词计数和动词变化相邻。'),
 'B2552':dict(words=['kill','kills'],label='kill → kills：使生命或运转停止',note='中古英语 killen 延续，更远来源未定；固定比喻用途另看搭配。'),
 'B3220':dict(words=['kick','kicked'],label='kick → kicked：用脚踢、启动与戒除',note='中古英语踢词，其他意思沿固定搭配学习。'),
 'B3067':dict(words=['list','lists'],label='list → lists：条状记录到清单',note='本族、法语条带材料与目录义相连；倾斜义另有历史。'),
}
W('banking','/ˈbæŋkɪŋ/','银行业务、银行业；存款；堆积、倾斜转弯〔现在分词等〕',
 '把存取、支付等与银行有关的事放在一起，就是常见的 banking。另有把东西堆起、飞机侧倾等动词用途，要按具体场景分支理解。',
 'bank + -ing → banking。金融 bank 经法语 banque、意大利 banca 柜台、桌凳的词史；土堆、河岸等有另一日耳曼借入路线，不能把金融银行直接当成河岸的比喻。',
 [['意大利钱币柜台词 → 法语 → bank 金融义','兑换钱的柜台 → 银行'],['bank + -ing → banking；另支动词也同形','银行业务；堆起或使倾斜的过程']],
 'online banking 网上银行业务；banking services 银行服务；banking on help 指望得到帮助。',
 'mobile banking 手机银行；the plane banking to the left 飞机向左侧倾转弯。','banking on something 是指望、依赖某事；banking the plane 是使飞机倾斜转弯。banking 作行业活动名词通常不可数。',
 ('She uses online banking to pay her bills.','她用网上银行支付账单。'),('The plane was banking gently to the left.','飞机正缓缓向左倾斜转弯。'),sources=['https://en.wiktionary.org/wiki/banking#English','https://en.wiktionary.org/wiki/bank#English'])
W('gaming','/ˈɡeɪmɪŋ/','玩游戏、游戏活动；博彩；利用规则谋利〔现在分词等〕',
 '参与游戏是 gaming 的直接理解。现代常说电脑游戏；有些行业、规章语境则指博彩，而 gaming a system 是钻制度的空子。',
 'game 去 e + -ing → gaming。game 名词接古英语 gamen 娱乐，古英语也有 gamenian 游戏、说笑的动词；现代动词用途有重新从名词构成的发展，电脑游戏义更晚。',
 [['古英语 gamen、相关游戏动词 → game','娱乐、游戏 → 现代不同游戏活动'],['game 去 e + -ing → gaming','游戏活动、博彩；为有利结果操弄规则']],
 'computer gaming 电脑游戏活动；a gaming community 游戏玩家社群；gaming the system 钻制度空子。',
 'a gaming session 一段游戏时间；gaming equipment 游戏设备。','gaming 不能只凭字面决定是否含钱：电脑游戏、博彩都可能使用这个词。game the system 则强调利用规则漏洞取得好处。',
 ('He enjoys gaming with friends at the weekend.','他喜欢周末和朋友一起玩游戏。'),('The new rules aim to stop people gaming the system.','新规则旨在防止人们钻制度空子。'),sources=['https://en.wiktionary.org/wiki/gaming#English','https://www.etymonline.com/word/game'])
W('scoring','英 /ˈskɔːrɪŋ/；美 /ˈskɔːrɪŋ/','得分、记分、评分；刻划；谱写总谱〔现在分词、动名词〕',
 '把表现记成一道道可累计的分数，是 scoring 的计分画面。比赛中拿到分、评审时给分，都接这个记录与计算。',
 'score 去 e + -ing → scoring。score 与古诺尔斯 skor 刻痕、刻记相连，英语有计数、账目、分数等发展；音乐总谱及刻划也各有用途。',
 [['北欧刻痕、刻记词 → score','刻记数量 → 记分、得分；划线'],['score 去 e + -ing → scoring','得分、打分或记录的过程']],
 'a scoring system 评分系统；scoring a goal 进球得分；scoring the test 给测验评分。',
 'high-scoring games 高比分比赛；rules for scoring 记分规则。','scoring 可以是选手得分，也可以是裁判记分、评委评分，行动者不同。音乐里 scoring 还可涉及为哪些乐器写作、配器。',
 ('The teacher explained the scoring system before the test.','老师在测验前解释了评分办法。'),('She is scoring more goals this season.','她本赛季进球更多了。'),sources=['https://en.wiktionary.org/wiki/scoring#English','https://www.etymonline.com/word/score'])
W('reducing','英 /rɪˈdjuːsɪŋ/；美 /rɪˈduːsɪŋ/','减少、降低；使变成某种状态〔现在分词、动名词〕',
 '把数量、程度往下带，就是 reducing 的常见画面。也可以把东西带到更简化、更基本的样子。',
 'reduce 去 e + -ing → reducing，c 在 i 前仍读 /s/。拉丁 re- 往回 + dūcere 带领 → redūcere 带回，英语后来扩展到降低、简化等状态变化。',
 [['拉丁 redūcere → reduce','带回、带到另一状态 → 减少、简化'],['reduce 去 e + -ing → reducing','正在降低；使变到某状态的过程']],
 'reducing waste 减少浪费；reducing the price 降价；reducing the problem to a simple question 把问题简化为一个简单提问。',
 'reducing energy use 减少能源使用；reducing costs by ten per cent 降低百分之十的成本。','reduce by 给减少的幅度，reduce to 给剩下的数值。reducing a price by ten 是少十，reducing it to ten 是降到十。',
 ('The team is reducing waste in the workshop.','团队正在减少车间浪费。'),('Walking to work is one way of reducing car use.','步行上班是减少用车的一种办法。'),sources=['https://en.wiktionary.org/wiki/reducing#English','https://en.wiktionary.org/wiki/reduce#English'])
W('representing','/ˌreprɪˈzentɪŋ/','代表、描绘、表示；构成〔现在分词、动名词〕',
 '让一个人、一件事通过另一个人、符号或图像出现在眼前，是 representing 的线索：代表发言、图像描绘、符号表示，都能接起来。',
 'represent + -ing → representing。底词经法语 représenter 接拉丁 repraesentāre 使呈现、展示，与 praesens 在场的词族相连；不是每次现代 represent 都表示重复提交。',
 [['拉丁 repraesentāre → 法语 → represent','使呈现、展示 → 代表、描绘、表示'],['represent + -ing → representing','正在代表；展示、表示某内容的过程']],
 'representing the team 代表团队；a drawing representing the town 描绘城镇的画；symbols representing sounds 表示声音的符号。',
 'representing different views 代表不同意见；representing half the total 占总数的一半。','代表人时关注替谁出面；符号、图像的 representing 则关注显示什么。表示比例时可译成占、构成。',
 ('She is representing the team at the conference.','她正代表团队参加会议。'),('The map uses symbols representing different types of buildings.','地图用符号表示不同类型的建筑。'),sources=['https://en.wiktionary.org/wiki/representing#English','https://en.wiktionary.org/wiki/represent#English'])
W('referring','英 /rɪˈfɜːrɪŋ/；美 /rɪˈfɜːrɪŋ/','提到、指的是；查阅；转介〔现在分词、动名词〕',
 '把注意力带回某个人、某份资料或另一个处理者那里，是 referring 的线索。说的是谁、查的是哪页、把问题交给谁，都能接这个指向。',
 'refer 双写 r + -ing → referring，末音节重读。拉丁 re- 回 + ferre 带 → referre，经法语及直接拉丁借入路线进入英语。',
 [['拉丁 referre → 法语、英语 refer','带回、交回 → 提及、查阅、转交'],['refer 双写 r + -ing → referring','正在提及、查阅；把人或问题转交']],
 'referring to the report 查阅或提到报告；referring to you 指的是你；referring a patient 转介病人。',
 'Who are you referring to? 你指的是谁？；referring the matter to the manager 把事情交给经理处理。','refer to something 有提及、指的是、查阅等意思；refer somebody to somebody 则把人转给另一位处理者。不要只记一个中文译词。',
 ('Which part of the report are you referring to?','你指的是报告的哪一部分？'),('She answered the questions without referring to her notes.','她没有查看笔记就回答了问题。'),sources=['https://en.wiktionary.org/wiki/referring#English','https://en.wiktionary.org/wiki/refer#English'])
W('preparing','英 /prɪˈpeərɪŋ/；美 /prɪˈperɪŋ/','准备、预备；备餐、编写〔现在分词、动名词〕',
 '事情还没正式到来，先把需要的人、物、内容安排好，就是 preparing。准备一顿饭、一次考试、一场报告，做法不同，提前备好相同。',
 'prepare 去 e + -ing → preparing。较早拉丁 prae- 提前 + parāre 备好 → praeparāre；英语 prepare 有从 preparation 逆构及部分借法语 preparer 的来源分析。',
 [['拉丁 praeparāre → 法语／preparation 逆构 → prepare','预先备好、安排到位'],['prepare 去 e + -ing → preparing','正在准备；把内容、食物等备好']],
 'preparing a meal 备餐；preparing for an exam 备考；preparing to leave 准备离开。',
 'preparing a report 编写报告；preparing students for work 帮学生为工作作准备。','prepare something 是把某物备好，prepare for something 是为某事准备，prepare to do 是准备做。宾语和介词把准备的对象、目标区分开。',
 ('She is preparing a meal for the family.','她正为一家人准备饭菜。'),('The students are preparing for their final exams.','学生正在准备期末考试。'),sources=['https://en.wiktionary.org/wiki/preparing#English','https://www.etymonline.com/word/prepare'])
W('claiming','/ˈkleɪmɪŋ/','声称；要求、认领、申领〔现在分词、动名词〕',
 '把自己的说法或要求摆出来，希望别人认可，是 claiming。可以说某事是真的，也可以说某样东西、某项权益应归自己。',
 'claim + -ing → claiming。动词经古法语 clamer 接拉丁 clāmāre 呼喊、宣告，后来有基于权利要求、声称的用途；名词另经法语 claime 借入。',
 [['拉丁 clāmāre → 古法语 clamer → claim','呼喊、宣告 → 提出权利要求、声称'],['claim + -ing → claiming','正在主张、认领或申请取得']],
 'claiming that... 声称……；claiming a prize 领取奖品；claiming expenses 申报费用报销。',
 'claiming ownership 主张所有权；claiming the lost bag 认领遗失的包。','claiming 是某人提出说法或要求，单凭这个词不能知道说法已证实、要求已获准。认领、申领还是声称，按后面的内容判断。',
 ('He is claiming that the painting belongs to his family.','他正声称这幅画属于他的家族。'),('The form explains the process for claiming travel expenses.','表格说明了申报差旅费的流程。'),sources=['https://en.wiktionary.org/wiki/claiming#English','https://www.etymonline.com/word/claim'])
W('crossing','英 /ˈkrɒsɪŋ/；美 /ˈkrɔːsɪŋ/','横过、交叉〔现在分词、动名词〕；过街处、交叉口、横渡',
 '从这一边走到另一边是 crossing；人们经常这样过去的地方，也可叫 a crossing。两条路线相交，则形成交叉。',
 'cross + -ing → crossing。cross 的十字词源接拉丁 crux，经早期爱尔兰语、北欧等借入路线传到英语；英语后来的横过动词加 ing，可表达过程或给通行处命名。',
 [['十字名词 cross → 横过、交叉动词','两线交叉的形状 → 从一边通过到另一边'],['cross + -ing → crossing','横过的过程；过街点、交汇处或横渡行程']],
 'crossing the road 过马路；a pedestrian crossing 人行横道；a sea crossing 一次海上横渡。',
 'crossing the bridge 过桥；a safe crossing 安全的过街处、横渡。','a crossing 可以是一个地点，也可以是一段横渡行程；crossing the road 里的 crossing 则直接带动作对象。按是否有冠词和宾语判断。',
 ('Use the pedestrian crossing near the school.','请走学校附近的人行横道。'),('We saw deer crossing the road ahead.','我们看见前方有鹿穿过马路。'),sources=['https://en.wiktionary.org/wiki/crossing#English','https://en.wiktionary.org/wiki/cross#English'])
W('defending','/dɪˈfendɪŋ/','保护、防守；为……辩护〔现在分词、动名词〕',
 '有攻击过来，就把它挡开，让人、地方或说法守得住，是 defending。攻击可以是实体进攻，也可以是对观点的质疑。',
 'defend + -ing → defending。拉丁 dē- 离开 + -fendere 击、推 → defendere 挡开，经法语及拉丁路线借入；英语直接在 defend 上加 ing。',
 [['拉丁 defendere → 法语及英语 defend','把攻击挡开 → 保护、防守、辩护'],['defend + -ing → defending','正在保护、防守；为某方提出理由']],
 'defending the goal 守球门；defending her decision 为她的决定辩护；defending champion 卫冕冠军。',
 'defending the town 保卫城镇；defending a viewpoint 维护一种观点。','defending champion 是上届冠军来守住冠军头衔，不是任意参加防守位置的运动员。defend a decision 要为决定提供理由。',
 ('The team is defending its lead in the final minutes.','球队正在最后几分钟守住领先优势。'),('She gave clear reasons for defending the decision.','她为维护这项决定给出了清楚的理由。'),sources=['https://en.wiktionary.org/wiki/defending#English','https://en.wiktionary.org/wiki/defend#English'])
W('drops','英 /drɒps/；美 /drɑːps/','滴、少量液体；下降〔复数〕；落下、下降、放弃〔第三人称单数〕',
 '一小团液体脱离开来往下落，是 drops 的基本画面。名词数一滴滴，动词可说物体掉落、数值降低或把某事放下不做。',
 'drop + -s，/p/ 后读 /s/。drop 继承古英语滴的名词及相关滴落动词，经中古英语延续；现代掉落、数量下降、停止参与等用途逐渐展开。',
 [['古英语滴、滴落词 → drop','小滴落下 → 落下、减少、放下'],['drop + -s → drops','多滴液体；单数主语掉落、降低或停止']],
 'drops of rain 雨滴；eye drops 滴眼液；the temperature drops 温度下降；drops the subject 不再谈这个话题。',
 'a few drops of water 几滴水；drops the keys 掉了钥匙。','drops 作液滴是可数名词，a drop、two drops。眼药水常叫 eye drops；数值 drops 是下降，不一定包含从某个实体上滴下来。',
 ('Add a few drops of water to the paint.','往颜料里加几滴水。'),('The temperature drops quickly after sunset.','日落后温度迅速下降。'),sources=['https://en.wiktionary.org/wiki/drops#English','https://en.wiktionary.org/wiki/drop#English'])
W('dropping','英 /ˈdrɒpɪŋ/；美 /ˈdrɑːpɪŋ/','落下、降低、放下；停止、放弃〔现在分词、动名词〕',
 '原来在上面、手里或计划里的东西，现在往下落、被放下，是 dropping。可以掉钥匙、降低声音，也可以退出一门课。',
 'drop 双写 p + -ing → dropping，短元音后单辅音结尾的重读词遵循此拼写。drop 接本族滴、滴落词，现代抽象停止、减少义建立在这个落下、放下的线索上。',
 [['本族 drop 滴、滴落 → 现代 drop','往下落 → 降低；从安排中放下、移除'],['drop 双写 p + -ing → dropping','正在落、减、放弃的过程']],
 'dropping prices 降价；dropping a course 退选一门课；dropping somebody off 让某人下车。',
 'dropping the subject 不再谈这个话题；dropping her voice 压低声音。','drop out of 是退出活动、学业等；drop somebody off 是顺路送到某处让人下车。小词 out、off 会改变整个表达的用途。',
 ('Prices are dropping as more shops offer the product.','随着更多商店供应这种产品，价格正在下降。'),('She is dropping the children off at school.','她正开车把孩子们送到学校。'),sources=['https://en.wiktionary.org/wiki/dropping#English','https://en.wiktionary.org/wiki/drop#English'])
W('kills','/kɪlz/','杀死、使死亡；终止、使失效〔第三人称单数〕；击杀等〔复数〕',
 '让生命或持续活动停止，是 kills 的基本线索。用于声音、灯、时间等对象时，要按固定的停止、消磨等搭配理解。',
 'kill + -s，/l/ 后读 /z/。kill 接中古英语 killen 杀死、打击等，更远来源有争议；名词 kills 是动作或结果名词的复数，不把某个猜测旧形式当确定起点。',
 [['中古英语 killen → kill','杀死 → 使活动、作用停止的扩展'],['kill + -s → kills','单数主语使停止；名词可数击杀等结果']],
 'kills the weeds 杀死杂草；kills the engine 关掉发动机；kills time 消磨时间。',
 'kills the sound 关闭声音；a cold that kills plants 使植物冻死的寒冷。','kill time 是打发、消磨时间；kill the engine 是关掉发动机，不是破坏发动机。不同宾语下的固定用途要连着宾语记。',
 ('A hard frost kills these young plants.','严重霜冻会使这些幼苗冻死。'),('He kills time by reading while he waits.','他等候时通过读书消磨时间。'),sources=['https://en.wiktionary.org/wiki/kills#English','https://en.wiktionary.org/wiki/kill#English'])
W('kicked','/kɪkt/','踢了；戒除了〔过去式、过去分词〕',
 '用脚施力，把东西踢开，是 kicked。比喻把不想要的习惯踢出生活，也会说 kicked a habit。',
 'kick + -ed，/k/ 后读 /t/。kick 接中古英语 kyken 等踢词，较远与北欧词的联系有不同分析；现代过去变化很规则，名词的刺激等义另由动作扩展。',
 [['中古英语 kyken 等 → kick','用脚踢 → 在固定搭配中表示启动、戒除等'],['kick + -ed → kicked','过去踢了；已经摆脱某习惯']],
 'kicked the ball 踢了球；kicked off the meeting 开始会议；kicked the habit 戒掉习惯。',
 'kicked the door 用脚踢门；kicked into action 被促使行动起来。','kicked off 可说比赛开球，也可说活动开始；kicked out 是踢出、逐出。过去词尾 /kt/ 连读，不另读 /ɪd/。',
 ('She kicked the ball across the field.','她把球踢过球场。'),('The workshop kicked off with a short introduction.','工作坊以简短介绍开始。'),sources=['https://en.wiktionary.org/wiki/kicked#English','https://en.wiktionary.org/wiki/kick#English'])
W('lists','/lɪsts/','清单、目录〔复数〕；列出〔第三人称单数〕；倾斜〔另一动词用途〕',
 '把项目排成可逐项查看的一列，就是 lists 的清单画面。名词数几份清单，动词说某个资料把内容列出来。',
 'list + -s，/t/ 后读 /s/。清单 list 联系本族、法语条带、边条词，后来发展条状记录和目录；船体倾斜动词 list 的来源未定，另支解释。',
 [['条带、边条相关词 → 清单 list','条状记录 → 项目目录'],['list + -s → lists；倾斜动词另支同形','多份清单；单数主语列出，或船向一边倾斜']],
 'shopping lists 购物清单；lists of names 名单；lists the ingredients 列出配料。',
 'make lists 列清单；lists all the options 列出所有选项。','The guide lists... 中 lists 是动词，直接接列出的东西。船 lists to one side 是倾斜，不能硬套成一张清单。',
 ('The guide lists all the museums in the area.','指南列出了这一地区的所有博物馆。'),('She keeps separate lists for work and home.','她把工作和家里的事项分别列成清单。'),sources=['https://en.wiktionary.org/wiki/lists#English','https://en.wiktionary.org/wiki/list#English'])
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_zl',ROOTS,WORDS)
 extend_lessons()
