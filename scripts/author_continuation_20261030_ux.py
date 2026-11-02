"""Everyday bases behind existing adjective and compound lessons."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'B4514':dict(words=['charity','charities','charitable'],label='charity：善意、施助与慈善机构',note='charity 经法语接拉丁 caritas 珍视、关爱等材料；可数机构义用 charities，charitable 为同族性质词。'),
 'A1699':dict(words=['mood','moody'],label='mood 与 moody：心境和情绪性质',note='情绪 mood 承接古英语 mod 心志、精神，moody 承接 modig 等旧形容词；语法语气 mood 另由 mode 改形，不与情绪词混成一个近源。'),
 'B2631':dict(words=['anger','angry'],label='anger 与 angry：不满痛苦到愤怒',note='anger 借古诺斯语痛苦、烦恼词族，现代愤怒义突出；angry 与 anger 加性质后缀的历史对应，不能硬拆现代不存在的 ry。'),
 'B2808':dict(words=['dish','desk','desktop','disk','disc'],label='discus 的多次借入：盘、圆片与书桌',note='dish、desk、disk、disc 共享更早拉丁 discus、希腊 diskos 材料，但分别经不同年代和路径进入英语；desktop 是现代 desk + top，不能把所有词画成 dish 的现代派生。'),
 'C0265':dict(words=['bureau','bureaucracy','bureaucrat'],label='bureau：桌布、办公桌与机构',note='bureau 借法语，名称由桌面覆盖物转到桌子和办公室、部门；bureaucracy 等再结合希腊权力材料。bureau 本身不是希腊词。'),
 'A1771':dict(words=['palace','palatial','fiscal'],label='借入的 -al 形容词：palatial 与 fiscal',note='palatial 接 palace 同族的拉丁宫殿材料，fiscal 接 fiscus 国库及 fiscalis；均需保留法语、拉丁借入历史，不能全当现代英语加后缀。'),
 'C1364':dict(words=['resolve','resolution'],label='resolution：解开问题、确定主意与分辨细部',note='resolution 经法语、拉丁 resolutio 借入，接 resolvere 松开、解开；解决、决心及分辨能力各有语义分支。'),
}
W('charity','/ˈtʃærəti/','慈善、施助；慈善机构；善意、宽厚',
 '看见别人困难，愿意帮助，是 charity；判断别人时先给一点善意，也可以叫 charity。做这类帮助的机构便是一家 a charity。',
 '经法语 charite 等接拉丁 caritas 珍视、关爱，来自 carus 珍贵、受喜爱的。宗教中的关爱、对困难者施助及判断宽厚等历史意义，后来在现代不同用法中保留。',
 [['拉丁 carus → caritas → 法语 charite','珍视、关爱、善意'],['英语 charity','施助、慈善事业；慈善机构；宽厚判断']],
 'give to charity 捐助慈善事业；a children’s charity 儿童慈善机构；a charity shop 慈善商店；show charity in judging others 评价别人时保持宽厚。',
 'raise money for charity；an act of charity。','charity 不可数时说施助或慈善活动，可数时可指一家机构。help a charity 是帮助机构，give to charity 说把钱物捐给慈善事业。',
 ('The concert raised money for charity.','音乐会为慈善事业筹集了款项。'),('She works for a charity that supports older people.','她在一家帮助老年人的慈善机构工作。'),sources=['https://www.etymonline.com/word/charity','https://en.wiktionary.org/wiki/charity#English'])
W('charities','/ˈtʃærətiz/','慈善机构〔charity 的常见复数义〕',
 '不是把善意数成几份，而是在数提供帮助的不同机构：two charities，两家慈善机构。',
 'charity 词末辅音加 y，复数把 y 换 i 再加 -es。单数从关爱、施助扩展出可数机构义，复数 charities 承接这一分支。',
 [['charity 的可数机构义','从施助事业转指承担事业的机构'],['charity → charities','多家慈善机构；y 变 i 加 -es']],
 'local charities 当地慈善机构；support several charities 支持几家慈善机构；donations to charities 捐给慈善机构的钱物。',
 'work with charities；two independent charities。','charities 常在数机构；一般的慈善事业仍用不可数 charity。charities’ funds 中撇号在复数 s 后，表示多家机构的资金。',
 ('The shop donates part of its profits to local charities.','商店把部分利润捐给当地慈善机构。'),('Several charities worked together on the project.','几家慈善机构合作开展了这个项目。'),sources=['https://www.etymonline.com/word/charity','https://en.wiktionary.org/wiki/charities#English'])
W('mood','/muːd/','心情、情绪；氛围；另源：语气〔语法〕',
 '今天同样一件小事，心情好时不在意，心情差时就烦。mood 看这段时间笼罩着你的情绪底色，也能说作品营造的氛围。',
 '情绪义接古英语 mod 心志、精神、勇气等，后来心情义突出，更远来源有争议。语法的 mood 则由 mode 方式改形，接法语、拉丁 modus，不来自情绪词。',
 [['古英语 mod → 情绪 mood','心志、精神 → 情绪状态、心境、氛围'],['另源 mode → 语法 mood','方式、形式 → 动词语气类别']],
 'in a good mood 心情好；in the mood for music 想听音乐；not in the mood to talk 没心情说话；set the mood 营造气氛；the subjunctive mood 虚拟语气。',
 'a cheerful mood；the mood of the film。','mood 可说暂时的心情，character 更常说较稳定的性格。语法语气是另源术语，不能拿高兴、难过解释虚拟、祈使等语气。',
 ('The walk put me in a better mood.','散步让我心情好了一些。'),('The lighting creates a calm mood in the room.','灯光让房间有一种宁静的氛围。'),('This chapter introduces the imperative mood.','这一章介绍祈使语气。'),sources=['https://www.etymonline.com/word/mood','https://en.wiktionary.org/wiki/mood#English'])
W('anger','英 /ˈæŋɡə/；美 /ˈæŋɡər/','愤怒、怒气；使生气、激怒',
 '觉得受到冒犯、不公平对待，心里升起强烈的不满，就是 anger。它既能作情绪名词，也能作让人生气的动词。',
 '名词、动词分别联系古诺斯语 angr 痛苦、烦恼与 angra 使难受等同族词，更远接紧、受挤压、痛苦的旧材料。英语后来愤怒、激怒义突出。',
 [['古诺斯语 angr／angra','痛苦、烦恼；使难受'],['英语 anger','愤怒、怒气；使愤怒']],
 'in anger 愤怒地；anger at a decision 对决定的愤怒；express anger 表达愤怒；be angered by something 被某事激怒。',
 'a flash of anger；control one’s anger。','anger 是名词或动词，angry 是形容词：I felt anger；I was angry。That angered me 则是那件事让我生气，动作方向不同。',
 ('There was anger in her voice.','她的声音里带着怒气。'),('The unfair decision angered many people.','这个不公平的决定激怒了许多人。'),sources=['https://www.etymonline.com/word/anger','https://en.wiktionary.org/wiki/anger#English'])
W('desk','/desk/','书桌、办公桌；服务台；负责某业务的部门',
 '有人坐在后面读写、办公或接待的那张桌子，是 desk。桌子再代指坐在那里处理一类业务的岗位或部门。',
 '经中世纪拉丁 desca 写字桌，可能经意大利语 desco，最终接拉丁 discus、希腊 diskos 盘、圆片。它与 dish 是多次借入后的分支，不是今天把 dish 发音一改就变桌子。',
 [['拉丁 discus → 后来的桌面、桌子词 → desca','盘、平面器物 → 写字桌'],['英语 desk','书桌、办公桌；接待台、业务部门']],
 'at a desk 在书桌前；a reception desk 接待台；the news desk 新闻编辑部、新闻台；a desk job 办公室工作；desk space 桌面办公空间。',
 'sit at a desk；leave something on the desk。','table 泛说桌子；desk 通常更适合读写、办公。the travel desk 可能是处理旅行业务的服务台，不能每次只译一张旅行桌子。',
 ('I left the notebook on your desk.','我把笔记本放在你桌上了。'),('Please ask at the reception desk.','请到接待台询问。'),sources=['https://www.etymonline.com/word/desk','https://en.wiktionary.org/wiki/desk#English'])
W('disk','/dɪsk/','圆片、圆盘；磁盘等存储盘',
 '薄而近圆的一片东西，先是盘片的形状；用这种盘片记录数据，就有了存储磁盘的用法。',
 '接拉丁 discus，来自希腊 diskos 圆片、掷盘等。与 dish、desk 共享更早材料，但 disk 是较后重新借入的形式；现代技术义随盘片用途扩展。',
 [['希腊 diskos → 拉丁 discus → disk','圆片、盘、掷盘'],['英语 disk 的技术用法','圆盘状物；用于记录信息的磁盘等']],
 'a flat disk 扁平圆片；a hard disk 硬盘；disk space 磁盘空间；a disk drive 磁盘驱动器。设备名称会保留历史用语，不必推断内部每项技术都一样。',
 'free disk space；a disk of metal。','disk 与 disc 常是同源拼写变体，但技术搭配有惯例：hard disk 常用 k，compact disc 常用 c。不能简单认定美式所有场合只用 k、英式所有场合只用 c。',
 ('The machine cut the metal into small disks.','机器把金属切成小圆片。'),('There is not enough free disk space for the file.','磁盘可用空间不够存放这个文件。'),sources=['https://www.etymonline.com/word/desk','https://en.wiktionary.org/wiki/disk#English'])
W('disc','/dɪsk/','圆片、圆盘；光盘；椎间盘等盘状结构',
 '仍抓住薄圆片的形状：一张光盘、身体里盘状的结构，都可以用 disc。它与 disk 同音、同源。',
 '接拉丁 discus、希腊 diskos，与 disk 是相应的借入、拼写形式。现代常用于英式一般圆片义及若干专业搭配，光盘、解剖等词汇有各自惯例。',
 [['希腊 diskos → 拉丁 discus → disc','圆片、盘状器物'],['现代 disc 的应用','圆盘；光盘；盘状解剖结构等']],
 'a compact disc 激光唱片、光盘；a music disc 音乐光盘；a spinal disc 椎间盘；disc brakes 盘式制动器。',
 'a disc-shaped object；put a disc in the player。','disc 和 disk 并非一个永远指光学、一个永远指磁性；这是部分技术搭配的常见选择，不能扩大成全部词义的硬规则。',
 ('She put the disc back in its case.','她把光盘放回盒里。'),('The diagram shows the discs between the vertebrae.','示意图显示了椎骨之间的椎间盘。'),sources=['https://www.etymonline.com/word/desk','https://en.wiktionary.org/wiki/disc#English'])
W('bureau','英 /ˈbjʊərəʊ/；美 /ˈbjʊroʊ/','局、处、署；办事处；有抽屉的家具、写字柜等',
 '桌面上铺的布，名字转到办公桌，再转到坐在桌后处理事务的办公室或部门。这条线能把 bureau 的几个常用意思接起来。',
 '借法语 bureau 办公桌、办公室，较早说桌面覆盖物，接 burel 粗毛织物等。更远布名来源有不同解释；英语另发展出有抽屉的衣柜、柜桌等家具义。',
 [['法语 burel 等 → bureau','桌布、覆盖物 → 书桌、办公室'],['英语 bureau','办事处、政府部门；某些带抽屉家具']],
 'a news bureau 新闻分社；a government bureau 政府局处；a travel bureau 旅行服务机构；a bureau drawer 抽屉柜的抽屉。复数 bureaus、bureaux 都可见。',
 'the local bureau；a bureau chief。','bureau 在机构名里常指办事部门；家具义因地区有差异。bureaucracy 在此基础上结合权力、治理材料，bureau 本身不是官僚主义这个抽象性质。',
 ('The newspaper opened a bureau in the capital.','报社在首都设立了分社。'),('She kept the letters in a bureau drawer.','她把信保存在抽屉柜的一个抽屉里。'),sources=['https://www.etymonline.com/word/bureau','https://en.wiktionary.org/wiki/bureau#English'])
W('palace','/ˈpæləs/','宫殿；豪华的大宅、建筑',
 '不是普通住处，而是统治者或重要人物的宏伟住所。后来也可夸张地说一座特别豪华的大宅。',
 '经法语 palais、中世纪拉丁 palacium 接拉丁 Palatium 罗马帕拉蒂尼山，那里有皇帝居所。地名转成宫殿通名；山名更远来源有不同解释，不强行指定唯一词根。',
 [['罗马地名 Palatium','帕拉蒂尼山，皇帝居所所在'],['拉丁宫殿名 → 法语 palais → palace','由特定地点转为宫殿、豪华住所的名称']],
 'a royal palace 王宫；the palace gardens 宫殿花园；a palace museum 以宫殿为馆舍的博物馆；a palace of glass 玻璃构成的宏伟建筑等。',
 'visit a palace；a former palace。','palace 重点是宫殿、豪华住所，castle 往往让人想到城防结构；真实建筑功能可以重叠，不能只凭外观大小互换名称。',
 ('The old palace is now open to visitors.','旧宫殿如今向游客开放。'),('They spent the afternoon exploring the palace gardens.','他们下午在宫殿花园里游览。'),sources=['https://www.etymonline.com/word/palace','https://en.wiktionary.org/wiki/palace#English'])
W('palatial','/pəˈleɪʃəl/','宫殿般豪华、宏伟的；宫殿的',
 '房子不一定真是王宫，但宽敞、华丽得像宫殿，就可以形容为 palatial。',
 '经法语 palatial 或相应拉丁材料接 palatium 宫殿的词干与形容词后缀。与 palace 同族；词干保留 palat-，不是在现代 palace 拼写后直接添 ial。',
 [['拉丁 palatium 及相应形容词材料','宫殿 → 宫殿相关的'],['英语 palatial','宫殿的；像宫殿一样宽敞豪华的']],
 'a palatial house 宫殿般的大宅；palatial surroundings 豪华环境；a palatial hotel 宏伟豪华的酒店。',
 'a palatial residence；palatial rooms。','palatial 常带夸张、赞叹色彩，不等于这座房子具有真实王室身份。palace 是建筑名词，palatial 通常是性质形容词。',
 ('They stayed in a palatial hotel by the lake.','他们住在湖边一家宫殿般豪华的酒店。'),('The entrance hall was palatial, with a sweeping staircase.','入口大厅宏伟华丽，有一道宽大的曲线楼梯。'),sources=['https://en.wiktionary.org/wiki/palatial#English','https://www.etymonline.com/word/palace'])
W('fiscal','/ˈfɪskəl/','财政的；财务年度等用语中的财务的',
 '把政府的钱想成一个公共钱袋：钱怎样收进来、怎样花出去，是 fiscal 常关心的范围。',
 '经法语 fiscal 接晚期拉丁 fiscalis 国库的，来自 fiscus 国库，原指篮子、钱袋等。词根来源更远不明；-alis 是相应形容词材料。',
 [['拉丁 fiscus → fiscalis','钱篮、国库 → 国库相关的'],['法语 → 英语 fiscal','财政的；后扩到一些财务用语']],
 'fiscal policy 财政政策；fiscal year 财政年度、会计年度；fiscal revenue 财政收入；fiscal measures 财政措施。',
 'the end of the fiscal year；fiscal spending。','fiscal policy 常关心政府收入、支出，monetary policy 常关心货币与利率等政策。这里只辨词义；fiscal year 的起止日并非全球统一。',
 ('The report covers the last fiscal year.','报告涵盖上一个财政年度。'),('The lecture compared fiscal policy with monetary policy.','讲座比较了财政政策与货币政策。'),sources=['https://www.etymonline.com/word/fiscal','https://en.wiktionary.org/wiki/fiscal#English'])
W('resolution','/ˌrezəˈluːʃən/','解决；决心、决议；分辨率、分辨能力',
 '把纠缠的问题拆开弄清，可以得到解决；把主意定清，可以形成决心或决议；把靠近的细部看开、分清，就接到分辨能力。',
 '经法语 resolution 或拉丁 resolutio 借入，来自 resolvere 松开、解开、分解，含 re- 与 solvere 松开等材料。解决、确定主意、光学分辨等分支陆续形成，不是一项现代定义覆盖全部历史。',
 [['拉丁 resolvere → resolutio','松开、分解 → 分解、解开过程'],['英语 resolution 的不同分支','解决；确定的主意、决议；分清细部的能力']],
 'the resolution of a dispute 争议的解决；a New Year’s resolution 新年决心；pass a resolution 通过决议；high resolution 高分辨率；image resolution 图像分辨率。',
 'a peaceful resolution；screen resolution。','a resolution 可以是一项决议或决心，resolution 也可说坚定、解决过程或分辨能力。高分辨率主要关心能呈现、分清多少细部，不等于颜色一定更鲜艳。',
 ('The talks led to a peaceful resolution of the dispute.','谈判促成了争议的和平解决。'),('She made a New Year’s resolution to read more.','她下定新年决心，要多读书。'),('At higher resolution, the small letters are easier to read.','分辨率更高时，小字更容易看清。'),sources=['https://www.etymonline.com/word/resolution','https://en.wiktionary.org/wiki/resolution#English'])
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_ux',ROOTS,WORDS)
 extend_lessons()
