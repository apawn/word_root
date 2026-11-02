"""Movie, sport, production and director extensions."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
MO=[['moving picture 活动画面 → movie','moving 的缩短昵称式表达'],['现代 movie','电影、影片；美式尤常见']]
W('movie','/ˈmuːvi/','电影；影片',
 '一张张画面连起来像在动，moving picture 的活动画面就被缩短叫 movie。',
 '从 moving picture 的 moving 缩短，再加昵称式 -ie 形成，先在美式英语常见。不是 move 加表示人的后缀。',MO,
 'watch a movie 看电影，go to the movies 去看电影，a movie star 电影明星；英式 film 也很常见。',
 'watch a movie；go to the movies；a movie star；a movie theatre。',
 'movie 与 film 很多场景可互换，film 还能指胶片、薄膜；movie 不泛指一切会动的东西。',
 ('We watched a movie after dinner.','晚饭后，我们看了一部电影。'),('Do you want to go to the movies this weekend?','你这周末想去看电影吗？'))
R('B3326','活动画面缩短成电影称呼','MOVIE：moving picture 的日常短称','把活动画面缩短成电影称呼，先掌握 watch a movie 与 go to the movies。',
 '现代名词由 moving picture 相关缩短形式构成，昵称式 -ie 不是现代拉丁词根。较冷的 telemovie 暂留词典版。',
 'moving picture → movie；movie star、movie theatre 为常用短语。',
 [['常用基本词','movie']],
 'movie 多指电影，film 另有胶片、薄膜义；不是所有运动都叫 movie。',
 'The movie tells the story of a young filmmaker.\n\n电影讲述了一位年轻电影制作者的故事。',
 'movie')
SP=[['古法语 desporter 消遣 → 中古英语 disport、sport','让心情离开正事 → 娱乐、玩乐'],['现代 sport','娱乐活动 → 体育运动；也保留玩乐、展示等义']]
W('sport','英 /spɔːt/；美 /spɔːrt/','体育运动；消遣；有风度的人；展示、穿戴',
 '现代主要先想体育运动；旧的娱乐玩乐还留在一些表达里，动词 sport 则可说显眼地穿着、留着某种外观。',
 '中古英语 disport 的前部脱落成 sport，上接法语 desporter 消遣，历史有让心情离开严肃事务的画面。不是 s- 加 port 港口。',SP,
 'play sport 参加体育运动，a team sport 团队运动，be a good sport 输赢、玩笑中有风度；sport a beard 留着胡须。',
 'a team sport；competitive sport；a good sport；sport a beard。',
 'sport 不仅是竞技比赛，语境也可说娱乐；a good sport 评价人有风度，不是说一项运动规则好。',
 ('Swimming is her favourite sport.','游泳是她最喜欢的运动。'),('He was a good sport about losing the game.','他输了比赛也很有风度。'))
W('sports','英 /spɔːts/；美 /spɔːrts/','体育运动；体育相关的修饰形式',
 '可以是多种运动，也能在名词前组成体育新闻、运动装备等固定说法。',
 'sport + -s，复数形式及体育类名词前的惯用修饰形式。美式总说体育时尤其常用 sports，英式单数集合 sport 也很常见。',SP+[['sport + -s → sports','多种运动；体育类别修饰形式']],
 'sports news 体育新闻，sports equipment 运动器材，a sports car 跑车；不因有 s 就把后面名词都变复数。',
 'sports news；sports equipment；sports day；a sports car。',
 'a sports car 是一辆跑车，sports 的 s 不表示有很多车；news、equipment 也有各自的不可数规则。',
 ('She writes sports news for the local paper.','她为当地报纸写体育新闻。'),('The school bought new sports equipment.','学校买了新运动器材。'))
W('sporty','英 /ˈspɔːti/；美 /ˈspɔːrti/','爱运动的；有运动风格的',
 '说人时常是喜欢运动，说衣服、汽车时则是看着有运动感，不是物件真的去比赛。',
 'sport + -y，具有体育、运动特点。现代性格爱好与设计外观都可用。',SP+[['sport + -y → sporty','有运动特点 → 爱运动、运动风的']],
 'a sporty person 爱运动的人，a sporty jacket 运动风夹克，a sporty car 运动感强的汽车。',
 'a sporty person；sporty clothes；a sporty car。',
 'sporty 是爱好或风格，athletic 常更强调身体运动能力、体型；穿 sporty clothes 不保证很会运动。',
 ('She comes from a sporty family.','她来自一个爱运动的家庭。'),('The jacket has a sporty look.','这件夹克很有运动风。'))
R('B3966','从消遣到体育与运动风格','SPORT：娱乐玩乐的历史，体育运动的现代重点','sport、sports、sporty 紧挨着读，分清活动、惯用修饰和设计风格。',
 'sport 从 disport 缩短，经法语接消遣词；名词前 sports 是实际搭配，不按单复数一条规则乱推。',
 'sport → sports、sporty；motor、super + sport 为已有相关词。',
 [['基本词与形式、风格','sport · sports · sporty'],['相关复合词','motorsport · supersport']],
 'a good sport 是有风度的人；a sports car 一辆车；sporty 衣着不等于具备运动能力。',
 'She likes sport and often wears sporty clothes.\n\n她喜欢运动，也经常穿运动风衣服。',
 'sport sports sporty motorsport supersport')
P=[['拉丁 producere 引出、带出 → 法语及英语 produce','产出、制造、产生'],['英语 production 及派生','生产、制作 → 复制；生产过量']]
W('reproduction','英 /ˌriːprəˈdʌkʃən/；美 /ˌriːprəˈdʌkʃən/','复制、复制品；再现；繁殖',
 '让另一份相同或相近的东西产生出来：可以是印画复制，也可以是生物产生后代。',
 're- 再 + production 产出，历史也经法语及 reproduce 对应名词形成。不同语境抓再产生，不把生物繁殖只翻成复印。',P+[['re- + production → reproduction','再次产出 → 复制、再现；繁殖']],
 'a reproduction of a painting 画作复制品，sound reproduction 声音重现，plant reproduction 植物繁殖。',
 'a reproduction of；sound reproduction；plant reproduction。',
 'reproduction 复制不保证原作身份；original 原作与 reproduction 复制品要分开。',
 ('The museum shop sells reproductions of famous paintings.','博物馆商店出售名画复制品。'),('The lesson explains how plant reproduction works.','这节课解释植物如何繁殖。'))
W('overproduction','英 /ˌəʊvəprəˈdʌkʃən/；美 /ˌoʊvərprəˈdʌkʃən/','生产过剩；产出过量',
 '生产的量超过实际需要、需求或适当程度；不只是产量很大。',
 'over- 过度 + production 生产、产生。可谈工业库存，也可在其他领域说某物产生过量。',P+[['over- + production → overproduction','产出超过需要 → 生产过剩']],
 'overproduction of goods 商品生产过剩，reduce overproduction 减少过量生产；影视评论也可指制作加工过头。',
 'overproduction of；industrial overproduction；reduce overproduction。',
 'mass production 大规模生产，overproduction 超过需求；前者规模大并不自动后者过剩。',
 ('Overproduction left the company with unsold stock.','生产过剩让公司积压了卖不掉的库存。'),('The report links waste to the overproduction of goods.','报告把浪费与商品生产过量联系起来。'))
R('B4288','复制、再现与产出过量','PRODUCTION：产出；RE- 再产出，OVER- 产出过头','基本词 production 与 preproduction 已精讲，这里接复制、繁殖和过剩。',
 'production 的历史接引出、产出的拉丁词族；reproduction 有多条应用语境，overproduction 明确过量。',
 'production → preproduction、reproduction、overproduction。',
 [['基本生产与准备','production · preproduction'],['再次产出与产出过量','reproduction · overproduction']],
 'reproduction 也可生物繁殖，不只复印；overproduction 不是一切大规模生产。',
 'The company reduced production to avoid overproduction.\n\n公司削减产量，避免生产过剩。',
 'production preproduction reproduction overproduction')
D=[['拉丁 dirigere、directus → 英语 direct、director','指引、使朝某方向 → 指导、管理的人'],['现代 director 派生','管理机构；担任董事、主管的职务与任期']]
W('directorate','英 /dəˈrektərət/；美 /dəˈrektərət/','管理局；处、司等主管机构；董事会',
 '不是一名主管，而是承担某方面管理职能的部门，或由董事组成的管理机构。',
 'director + -ate，形成机构、群体等名词。各机构正式中文译名可能是局、司、处，不能只靠后缀确定行政级别。',D+[['director + -ate → directorate','管理者群体或其机构']],
 'the finance directorate 财务主管部门，a government directorate 政府主管机构；先看该组织自己的名称和层级。',
 'a finance directorate；a government directorate；the directorate’s staff。',
 'director 人，directorate 机构群体；directory 名录是另一个词，不要只按前半字母猜。',
 ('The finance directorate reviewed the budget.','财务主管部门审核了预算。'),('The directorate published its annual report.','管理机构发布了年度报告。'))
W('directorship','英 /dəˈrektəʃɪp/；美 /dəˈrektərʃɪp/','董事、主管职务；担任该职的期间',
 '谈的是这个职位、这份任职，不是泛指指导别人这个动作。',
 'director + -ship，后缀表示身份、职务、任期；-ship 不是船。',D+[['director + -ship → directorship','主管身份 → 董事、主管职务及任期']],
 'hold a directorship 担任董事，resign a directorship 辞去董事职务，under her directorship 在她主管期间。',
 'hold a directorship；accept a directorship；under her directorship。',
 'directorship 职务，direction 方向、指导；directorate 则是管理机构，不是同一个名词换尾巴。',
 ('She accepted a directorship at the company.','她接受了这家公司的董事职务。'),('The museum expanded under his directorship.','博物馆在他担任主管期间扩大了规模。'))
R('B4166','管理者的机构与职务','DIRECTOR：人；DIRECTORATE：机构；DIRECTORSHIP：职务','以已有 director 为基础，接机构群体与职位任期两种名词扩展。',
 'director 词族接引导方向、管理的历史词。后缀分别标明机构与身份，不只是笼统多一个名词。',
 'director → directorate、directorship。',
 [['个人、机构、职位','director · directorate · directorship']],
 'directorate 不是 directory 名录；directorship 不是 direction 方向；-ship 此处不指船。',
 'The directorate approved her appointment to the directorship.\n\n管理机构批准她出任主管。',
 'director directorate directorship')
if __name__=='__main__':save('continuation_20261029_ef',ROOTS,WORDS)
