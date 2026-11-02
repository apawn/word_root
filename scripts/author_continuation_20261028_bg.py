"""Job and site: tasks, employment, workplaces, and places on the web."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
def C(a,b,w,m):return [[f'{a}；{b}','并列构词部分'],[w,m]]
JOB=[['早期英语 jobbe of work 一类表达','一件、一份工作；更早来源不确定'],['英语 job','任务；有报酬的工作岗位']]
W('job','英 /dʒɒb/；美 /dʒɑːb/','工作；任务；岗位；一项处理作业',
 '既可以是长期靠它挣钱的职位，也可以是眼前这一件要做完的活。',
 '早期有 jobbe of work“一份工作”等表达，更早来源不确定。与一块、一团或戳、切等词的联系有不同假说，不选一个讲成定论。',JOB,
 'get a job 找到工作，do a good job 做得好，a repair job 一次修理活，a print job 一项打印作业。job 通常可数。',
 'get a job；do a good job；a repair job；a print job；job satisfaction。',
 'job 一份工作、任务通常可数；work 一般劳动、工作量常不可数。a lot of work 与 several jobs 可以同时成立。',
 ('She got a job at the local library.','她在当地图书馆找到了一份工作。'),('Cleaning the windows is my job today.','今天擦窗是我的任务。'))
W('jobless','英 /ˈdʒɒbləs/；美 /ˈdʒɑːbləs/','没有工作的；失业的',
 '眼下没有工作岗位；与只是今天休假、不用上班的状态分开。',
 'job + -less（没有），形容缺少工作、就业岗位的状态。',JOB+[['job + -less → jobless','没有工作、处于失业状态的']],
 'jobless workers 失业劳动者，the jobless 失业人群。新闻统计的具体口径由材料交代，不能从词本身推统一身份资格。',
 'jobless workers；the jobless；remain jobless。',
 'jobless 没工作，与 off work 休假、暂不工作不同；在放年假的人并不因此 jobless。',
 ('He remained jobless for several months.','他有几个月一直没找到工作。'),('The program helps jobless workers develop new skills.','项目帮助失业者培养新技能。'))
W('joblessness','英 /ˈdʒɒbləsnəs/；美 /ˈdʒɑːbləsnəs/','失业；无工作状态',
 '从某个人没工作，转到讨论一段时间、一个地区的无工作状态。',
 'jobless + -ness，链条 job → jobless → joblessness；不要把 -lessness 看成没有内部结构的一整块。',JOB+[['job → jobless → joblessness','工作 → 无工作的 → 无工作状态']],
 'long-term joblessness 长期失业，high joblessness 高失业水平。常见于社会、经济讨论；比率如何定义看相应数据。',
 'long-term joblessness；high joblessness；reduce joblessness。',
 'joblessness 状态名词，jobless 形容词或 the jobless 集合称呼；不是所有表示无工作的人、事都能用同一语法位置。',
 ('The report examines the effects of long-term joblessness.','报告考察长期失业的影响。'),('Joblessness remained high in the region.','该地区失业水平仍然很高。'))
W('jobseeker','英 /ˈdʒɒbsiːkə/；美 /ˈdʒɑːbsiːkər/','求职者',
 '不是已经没有工作这一状态，而是正在寻找工作的行动身份。',
 'job + seeker，seeker 是 seek + -er，表寻找的人；可与分写 job seeker 对照。',C('job','seeker〔seek + -er〕','jobseeker','正在寻找工作的人'),
 'advice for jobseekers 给求职者的建议，a first-time jobseeker 首次求职者。已经有工作、准备换岗位的人也可以求职。',
 'a first-time jobseeker；support for jobseekers；a jobseeker’s skills。',
 'jobseeker 求职者与 jobless 失业者不完全重合；一个说行动，一个说当前就业状态。',
 ('The workshop helps jobseekers prepare for interviews.','工作坊帮助求职者准备面试。'),('The fair attracted both new graduates and experienced jobseekers.','招聘会既吸引应届毕业生，也吸引有经验的求职者。'))
W('jobsite','英 /ˈdʒɒbsaɪt/；美 /ˈdʒɑːbsaɪt/','工作现场；施工工地',
 '不是公司注册在哪，而是这份施工、维修等工作实际发生的地方。',
 'job + site（场地），尤其常用于建筑、施工现场；site 在这里先取实体地点义。',C('job','site〔现场〕','jobsite','开展具体工作的场地、工地'),
 'on the jobsite 在工地、工作现场，jobsite equipment 现场设备。求职网站通常要从上下文另辨 jobs website 等，不把此词一律当网站。',
 'on the jobsite；jobsite equipment；a busy jobsite。',
 'jobsite 工作现场，jobseeker 求职者；一个说任务发生地点，一个说找工作的人。',
 ('The equipment arrived at the jobsite before sunrise.','设备天亮前运到了工地。'),('The manager visited the jobsite to check progress.','经理到现场查看进度。'))
W('blowjob','英 /ˈbləʊdʒɒb/；美 /ˈbloʊdʒɑːb/','口交〔特指对阴茎的口腔性刺激；粗俗口语〕',
 '整体是性行为的粗俗名称，不能照普通 blow“吹气”加 job“工作”猜成一项吹气任务。',
 '20世纪美国俚语，来自 blow off 的旧性俚语用法与 job 组合。普通 blow 的字面意义不足以解释整词，不编吹乐器之类的确定起源故事。',
 [['美国俚语 blow off 的相关性行为用法 + job','俚语组合背景'],['英语 blowjob','对阴茎的口交行为的粗俗称呼']],
 'give someone a blowjob 是常见结构。词的粗俗语域很明显，医学、正式性教育通常用 oral sex、fellatio 等更中性的术语。',
 'give someone a blowjob；a crude blowjob joke；the term blowjob。',
 'blowjob 属 oral sex 的一种具体指向；oral sex 范围更广，也不是普通工作任务 job。',
 ('In the adult comedy, he makes an awkward request for a blowjob.','成人喜剧里，他尴尬地提出了口交请求。'),('The editor removed a crude blowjob joke from the script.','编辑从剧本里删去了一则粗俗的口交笑话。'))
R('B3486','一件任务；工作、就业岗位','JOB：眼前要做的一件活，也可以是一份职业岗位','任务完成叫 do a job，失去岗位叫 jobless，正在找工作叫 jobseeker；现场则是 jobsite。',
 'job 早期见于一份工作之类表达，更早来源有争议。主线抓可数任务、岗位，不与泛指工作量的 work 混；粗俗固定复合词另说明语域与旧俚语来源。',
 'job → jobless → joblessness；job + seeker → jobseeker；jobsite 讲现场；blowjob 是词汇化俚语，不能按字面职业义硬译。',
 [['任务、岗位与无工作状态','job · jobless · joblessness'],['求职人与现场','jobseeker · jobsite'],['语域特殊的固定复合词','blowjob']],
 'work 常不可数、job 通常可数；jobseeker 与 jobless 不完全重合；jobsite 主要实体现场，俚语 blowjob 不取普通工作义。',
 'The jobseeker found a job coordinating equipment deliveries to the jobsite.\n\n求职者找到一份协调工地设备配送的工作。',
 'job jobless joblessness jobseeker jobsite blowjob')
SITE=[['拉丁 situs → 盎格鲁诺曼 site → 中古英语 site','放置位置、地点'],['英语 site','场地、地点；网站；把设施设在某处']]
W('site','/saɪt/','地点；场地；遗址；网站；选址、设置于',
 '某件事、某座设施落在的那块地方；互联网上也用它叫一个有地址、能访问的站点。',
 '经盎格鲁诺曼、中古英语接拉丁 situs“位置、地点”，与 sinere“放置”等旧义相关。不是 sight“视觉、景象”的缩写。',SITE,
 'a building site 建筑工地，an archaeological site 考古遗址，a website 网站。动词 site a building near the road 是把建筑设在路旁。',
 'a building site；an archaeological site；a historic site；site a building。',
 'site 地点，sight 视力、景象，cite 引用，三者常同音 /saɪt/，写法和来源不同。',
 ('The museum stands on the site of an old factory.','博物馆建在旧工厂原址。'),('The new station will be sited near the main road.','新车站将设在主路附近。'))
W('website','/ˈwebsaɪt/','网站',
 '同一个网络地址体系下，一组彼此关联、供访问的网页组成一个站。',
 'web（万维网）+ site（站点）→ website：把相关网页与功能组织在一起的网络站点。',C('web〔万维网〕','site','website','互相组织、关联的网页站点'),
 'visit a website 访问网站，the official website 官方网站。网站可能分布在多台服务器，不能把一个网站定义成必须只放在一台机器上。',
 'visit a website；the official website；a website address。',
 'website 网站整体，webpage 单个网页；一个 website 往往包含多个 webpages。',
 ('The museum’s website lists its opening hours.','博物馆网站列出了开放时间。'),('She built a website for the village history project.','她为村史项目建了一个网站。'))
W('onsite','英 /ˌɒnˈsaɪt/；美 /ˌɑːnˈsaɪt/','现场的；在现场',
 '人、服务或设备直接到了工作发生的地方，不是远程在别处处理。',
 'on + site，也常写 on-site，两种写法同义。site 这里通常取实体现场义。',C('on','site〔现场〕','onsite','在指定工作、活动现场'),
 'onsite support 现场支持，work onsite 到现场办公。网站上进行的活动通常说 online，不直接套 onsite。',
 'onsite support；an onsite visit；work onsite。',
 'onsite 在实体现场，与 online 在线不同；一次 onsite meeting 也可能同时有网络参会者，词先说明现场位置。',
 ('The company provides onsite technical support.','公司提供现场技术支持。'),('An engineer will inspect the equipment onsite.','工程师会到现场检查设备。'))
W('offsite','英 /ˌɒfˈsaɪt/；美 /ˌɔːfˈsaɪt/','在场外、外部地点的；离开主要现场地',
 '不在本部、当前工作场地，而是在另一个位置完成或保存。',
 'off-（离开、在外）+ site，另常写 off-site；实体位置离开原场地，不等于断网。',C('off-','site','offsite','离主要场地，在外部地点'),
 'offsite storage 场外存储，an offsite meeting 外部场所会议。数据备份在别处可叫 offsite，不自动说明是否联网。',
 'offsite storage；an offsite meeting；offsite backup。',
 'offsite 场外，offline 离线；一份远程云备份可 offsite 又 online，两个维度不同。',
 ('The records are kept in offsite storage.','记录存放在场外库房。'),('The team held an offsite meeting to plan the next project.','团队到外部场所开会规划下一个项目。'))
W('sitewide','/ˈsaɪtwaɪd/','全场地的；全站的；覆盖整个地点、站点地',
 '修改不是只动一个房间、一页，而是覆盖整个场地或网站。',
 'site + -wide（遍及……范围），site 可指实体场所或网站。wide 不是仅测网页横向宽度。',C('site','-wide','sitewide','覆盖整个场地或网站范围'),
 'a sitewide update 全站更新，sitewide rules 全场规则，apply sitewide 在全站应用。先看当前说的是哪种 site。',
 'a sitewide update；sitewide rules；apply sitewide。',
 'sitewide 整个站点，citywide 全市，countrywide 全国；范围由前面的名词决定。',
 ('The design change was applied sitewide.','设计修改应用到了全站。'),('The contractor introduced sitewide safety rules.','承包商推行了覆盖整个工地的安全规则。'))
W('fansite','/ˈfænsaɪt/','粉丝网站',
 '围绕某部作品、演员或球队聚资料、消息，让喜欢它的人有个集中看内容的地方。',
 'fan（粉丝）+ site（网站），常由粉丝建设、维护，但词的重点是面向粉丝、围绕喜爱对象。',C('fan〔粉丝〕','site〔网站〕','fansite','面向某对象粉丝的网站'),
 'a music fansite 音乐粉丝站，a fansite devoted to a series 某系列剧的粉丝站。可能包含档案、讨论、作品资料。',
 'a music fansite；run a fansite；a fansite devoted to。',
 'fansite 按对象、受众命名，不自动等于 official website 官方网站；是否获官方运营、授权看具体情况。',
 ('A fan built a fansite for the old television series.','一位粉丝为那部老剧建了粉丝网站。'),('The fansite collects interviews and production photographs.','粉丝站汇集了访谈和制作照片。'))
W('gravesite','/ˈɡreɪvsaɪt/','墓地位置；墓址',
 '重点是埋葬处所在的那个具体地点，不是泛指整片墓园。',
 'grave（坟墓）+ site（地点），grave 取名词义，不是严重、严肃的形容词。',C('grave〔坟墓〕','site','gravesite','坟墓所在位置、墓址'),
 'visit a gravesite 探访墓地，mark a gravesite 标出墓址；可以是墓园里的一处，也可能在其他地方。',
 'visit a gravesite；a marked gravesite；the family gravesite。',
 'gravesite 具体墓址，cemetery 常是整片墓园；一座 cemetery 可以有许多 gravesites。',
 ('They placed flowers at the gravesite.','他们在墓前放了花。'),('The map marks the location of the old gravesite.','地图标出了旧墓址的位置。'))
R('B4085','落在某处的地点；场地、站点','SITE：事物落在什么地方，实体与网络各有站点','在工地、在原址、在网站上，先认清 site 指哪种地方，再看 onsite、offsite、sitewide。',
 'site 经法语上接拉丁 situs“位置、地点”。website 借用站点概念；实体 onsite 与在线 online 不同，offsite 与 offline 也不是同一维度。',
 'site → website；onsite / offsite 相邻对照；sitewide 讲全范围，fansite 讲受众，gravesite 讲具体墓址。campsite、worksite、jobsite 各按用途集中。',
 [['地点与网络站点','site · website'],['在场内、场外和全范围','onsite · offsite · sitewide'],['受众与实体用途','fansite · gravesite · campsite · worksite · jobsite']],
 'site 地点、sight 视觉、cite 引用，同音不同词；onsite 现场、online 在线；offsite 场外、offline 离线。',
 'The onsite team checked the worksite while the offsite team updated the website.\n\n现场团队检查工作场地，异地团队则更新网站。',
 'site website onsite offsite sitewide fansite gravesite campsite worksite jobsite')
if __name__=='__main__':save('continuation_20261028_bg',ROOTS,WORDS)
