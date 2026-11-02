"""Traffic and trip: movement, trade, stumbling and altered impressions."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
TR=[['意大利 traffico、trafficare → 法语 trafique → traffic','贸易、往来；更远来源不确定'],['现代 traffic','交通流、网络流量；贩运、非法交易等动词用法']]
def T(f,m):return TR+[[f,m]]
W('traffic','/ˈtræfɪk/','交通、车流；流量；交易、贩运〔动词〕',
 '原来是货物、商人来往，今天可以是车在路上来往，也可以是数据在网络上来往。',
 '经法语接意大利贸易词系，更远来源有多种说法，不把 tra- 与现代某个英语片段强拼。车流、访问流量是后来专门化。',TR,
 'heavy traffic 交通拥堵、车多，website traffic 网站访问流量，traffic in stolen goods 交易赃物。名词车流通常不可数。',
 'heavy traffic；traffic lights；website traffic；traffic in。',
 'traffic 交通流、交易往来，不等于一个交通工具 vehicle；普通表达不说 three traffics 表三辆车。',
 ('We were late because of heavy traffic.','车太多、交通拥堵，我们迟到了。'),('The new article brought more traffic to the website.','新文章给网站带来了更多访问流量。'))
W('trafficking','/ˈtræfɪkɪŋ/','贩运、非法交易；traffic 的 -ing 形式',
 '现代常见新闻里不是说正常开车，而是组织贩运人、毒品、野生动物等。',
 'traffic 加 k 再接 -ing，保留 /k/ 音。名词接贸易、贩运这条支线，不接单纯车流增加。',T('traffic + k + -ing → trafficking','交易、贩运活动；现代常偏非法贩运'),
 'human trafficking 人口贩运，drug trafficking 毒品贩运，wildlife trafficking 野生动物非法贸易。',
 'human trafficking；drug trafficking；wildlife trafficking。',
 'traffic jam 交通堵塞，trafficking 常贩运行为；同族但不能因为都是移动，就把早高峰叫 trafficking。',
 ('The report examines wildlife trafficking.','报告研究野生动物非法贸易。'),('The novel follows an investigation into human trafficking.','小说围绕一宗人口贩运调查展开。'))
W('trafficker','英 /ˈtræfɪkə/；美 /ˈtræfɪkər/','贩运者；从事非法交易的人',
 '这次说的是组织、实施贩运的人，前面的词说明贩运对象。',
 'traffic 加 k + -er，形成执行者词，现代通常接非法交易义。不是 traffic controller 交通管制员的简写。',T('traffic + k + -er → trafficker','从事贩运、非法交易的人'),
 'a drug trafficker 毒贩，a wildlife trafficker 野生动物贩运者，a human trafficker 人口贩运者。',
 'a drug trafficker；a wildlife trafficker；a human trafficker。',
 'trafficker 贩运者，trader 贸易者可中性合法；不要把普通商人或所有司机都这样称呼。',
 ('The story centres on a police officer pursuing a drug trafficker.','故事围绕一位追查毒贩的警员展开。'),('The article describes how wildlife traffickers were identified.','文章描述了野生动物贩运者如何被查明。'))
W('trafficked','/ˈtræfɪkt/','被贩运的；traffic 的过去式、过去分词',
 '从贩运者转到被当成交易对象的人或动物，突出他们、它们经历了贩运。',
 'traffic 加 k + -ed，/k/ 后 -ed 读 /t/，末尾不多一个 /ɪd/ 音节。分词修饰接现代贩运义。',T('traffic + k + -ed → trafficked','经历贩运的；相关过去、分词形式'),
 'trafficked animals 被贩运动物，trafficked workers 遭人口贩运的劳工；具体情形由上下文说明。',
 'trafficked animals；trafficked workers；were trafficked。',
 'trafficker 是实施者，trafficked 描述被贩运对象或过去动作；不要看到类似拼写就把受害者和行为者对调。',
 ('The trafficked animals were taken to a rescue centre.','被贩运的动物被送往救助中心。'),('The documentary tells the stories of trafficked workers.','纪录片讲述遭人口贩运劳工的经历。'))
R('B2782','贸易往来到车流、网络流量；贩运支线分角色','TRAFFIC：来往的流；TRAFFICKING：现代常说非法贩运','traffic 基本词先分交通、网络、交易；trafficking 行为，trafficker 人，trafficked 被贩运状态按顺序。',
 '意大利、法语贸易词远源不定，现代几条支线同源却不能互相硬译。尤其贩运词不是日常交通的普通变形。',
 'traffic + k + -ing/-er/-ed；k 帮助保留 /k/，trafficked 末尾读 /kt/。',
 [['流量和往来','traffic'],['行为、执行者和经历','trafficking · trafficker · trafficked']],
 'traffic 通常不可数；trafficking 贩运不是车流；trafficker 执行者、trafficked 经历者；trader 可中性。',
 'The report distinguishes ordinary trade from illegal trafficking.\n\n报告区分普通贸易与非法贩运。',
 'traffic trafficking trafficker trafficked')
TI=[['中古英语 trippen；可能经法语或低地日耳曼同族形式','轻快迈步、跳舞、踏步；直接路线有不同分析'],['现代 trip','绊一下、绊倒；一趟行程；启动开关；特殊精神体验等分支']]
W('trip','/trɪp/','一趟行程、旅行；绊倒、失足；触发、跳闸；特殊体验〔特定用法〕',
 '先抓脚步：出门走一趟，脚被东西绊一下；开关被触发则是另一固定用法。',
 '中古英语 trippen 有轻快迈步、跳舞等义，近源可能涉及法语或低地日耳曼形式。行程名词、绊倒和触发等分别发展，不是一条现代新造词义线。',TI,
 'a business trip 出差，a trip to the shops 去商店一趟，trip over a cable 被线绊倒，trip a switch 触发开关。',
 'a business trip；a trip to；trip over；trip a switch。',
 'trip 常看一趟出行，journey 常着眼途中过程；trip over 失足不保证一定摔到地上。travel 更宽泛地说旅行。',
 ('We took a short trip to the coast.','我们去海边短途旅行了一趟。'),('She tripped over a bag left on the floor.','她被地板上留下的包绊了一下。'))
W('trippy','/ˈtrɪpi/','迷幻的；奇异、像特殊意识体验的〔口语〕',
 '颜色、声音、剪辑奇异得像意识飘进另一个世界；不表示观看的人真的用了药物。',
 'trip 的迷幻体验义 + -y，双写 p。后来广用于梦幻、离奇的艺术感受，不接普通出差的行程义。',TI+[['trip〔迷幻体验〕+ -y → trippy','像迷幻体验；引申奇异梦幻风格']],
 'trippy visuals 迷幻画面，a trippy film 迷幻、离奇的电影，trippy music 迷幻音乐。',
 'trippy visuals；a trippy film；trippy music。',
 'trippy 不是只是旅游相关的，travel-related 才明确旅行相关；dreamlike 如梦也可能重合，但 trippy 更有迷幻、怪异口语色彩。',
 ('The video uses bright colours and trippy visuals.','视频用了鲜艳色彩和迷幻画面。'),('The film becomes increasingly trippy near the end.','电影接近结尾时越来越离奇、迷幻。'))
W('tripwire','英 /ˈtrɪpwaɪə/；美 /ˈtrɪpwaɪər/','绊线；触发警报或后续反应的界线〔比喻〕',
 '一根线被碰动，就触发后面的装置；抽象里也可说一旦碰到就启动应对的信号。',
 'trip 绊动、触发 + wire 线。名字按触发机制概括，具体可用于警报、陷阱或比喻，不必每次都让人绊倒。',TI+[['trip + wire → tripwire','受触碰触发装置的线；引申触发后续行动的信号']],
 'a tripwire alarm 绊线警报，a warning tripwire 预警触发点，act as a tripwire 起触发信号作用。',
 'a tripwire alarm；act as a tripwire；a warning tripwire。',
 'tripwire 重点触发反应，deadline 截止时间重点最晚完成时刻；一个期限也可被设计成触发行动的条件，但词义不是一样。',
 ('The alarm was triggered when the tripwire moved.','绊线移动时触发了警报。'),('The threshold acts as a tripwire for a closer review.','这个阈值一旦触及，就会触发进一步审查。'))
R('B4114','脚步、行程、失足与触发；迷幻体验另一路','TRIP：走一趟、脚绊一下；装置也可被触发','trip 多义按场景先讲，再 trippy 迷幻体验、tripwire 触发结构；较少独立使用 tripper 暂略。',
 '旧轻快踏步词的传入路线有不同分析。现代出差、绊线和迷幻都常见，但不能把一个意思套到每个派生上。',
 'trip → tripped、tripping；trip + -y → trippy；trip + wire。',
 [['脚步、行程和体验','trip · trippy'],['触发结构与比喻','tripwire']],
 'trip 一趟、journey 途中；trip over 不保证摔倒；trippy 接迷幻体验不是普通旅行；tripwire 触发点。',
 'On the trip, they watched a trippy film about a strange journey.\n\n旅行途中，他们看了一部关于奇异旅程的迷幻电影。',
 'trip trippy tripwire')
if __name__=='__main__':save('continuation_20261030_bp',ROOTS,WORDS)
