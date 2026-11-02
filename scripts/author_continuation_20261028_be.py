"""Post: a beam, a relay station, an assigned position, and public notices."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
def C(a,b,w,m):return [[f'{a}；{b}','并列构词部分'],[w,m]]
POST=[['拉丁 postis → 古英语、古法语 post；另一路意大利 posta → 法语 poste','柱子；另有驿站、安置位置等词源'],['英语 post','柱、张贴；邮递；岗位、驻点等同形用法']]
W('post','英 /pəʊst/；美 /poʊst/','柱；张贴、帖子；邮递；岗位、驻点',
 '路边一根柱，墙上一张告示，邮局里一封信，工作中的一个岗位——拼写相同，要分来源、分场景。',
 '柱义经古英语、古法语接拉丁 postis；邮递义经法语 poste 接意大利 posta 驿站，岗位、驻点义也与法语 poste 相关。张贴与在显眼柱面等公布告示的用法相连。不要统统解释成 post- 在后。',POST,
 'a fence post 篱笆柱，post a notice 张贴告示，post a letter 邮寄信件，a job post 工作岗位；a social media post 社交平台帖子从公开发布用法扩展。',
 'a fence post；post a notice；post a letter；a teaching post；a social media post。',
 'post 名词、动词的多义要看宾语和场景；post- 在 postwar 等词里表示战后，是另一个前缀用法，不能套到 postman 说成后面的人。',
 ('She posted a notice on the door.','她在门上贴了张告示。'),('I need to post this letter today.','我今天要把信寄出去。'),('He accepted a teaching post at the local school.','他接受了当地学校的一个教学岗位。'),('A wooden post supports the fence.','一根木柱撑着篱笆。'))
W('poster','英 /ˈpəʊstə/；美 /ˈpoʊstər/','海报；招贴；发帖者〔另义〕',
 '把一幅大图、一张告示贴出来给人看；网络里也可说是谁发了那条帖子。',
 'post（张贴、发布）+ -er；名词可指供张贴的东西，也可指执行发帖的人。不是所有 -er 都只指人。',POST+[['post + -er → poster','招贴、海报；发帖的人']],
 'a movie poster 电影海报，put up a poster 贴海报，the original poster 原发帖者。按指物还是指人分义。',
 'a movie poster；put up a poster；the original poster。',
 'poster 海报或发帖者，postcard 邮寄卡片；同样纸片或图像，用途不同。',
 ('A concert poster hung beside the entrance.','入口旁挂着一张音乐会海报。'),('The original poster later added more details.','原发帖者后来补充了更多细节。'))
W('posting','英 /ˈpəʊstɪŋ/；美 /ˈpoʊstɪŋ/','发布、帖子；派驻、工作安排；入账等〔依语境〕',
 '一条内容被放上平台，或一个人被安排到某岗位；都要先看用了哪个 post。',
 'post + -ing；发布、派驻、记入记录等源自 post 的不同动词用法，并非一条网络帖子演变成一个工作岗位。',POST+[['post + -ing → posting','发布的内容、活动；岗位派驻；记入记录等']],
 'a job posting 招聘启事，an overseas posting 海外派驻，an online posting 网帖；财务材料也可指记入账簿。',
 'a job posting；an overseas posting；an online posting。',
 'job posting 是发布出来的职位消息，job post 可以是职位本身；an overseas posting 则更常是一段外派安排。',
 ('The job posting lists the skills required.','招聘启事列出了所需技能。'),('She accepted a two-year overseas posting.','她接受了两年的海外派驻。'))
W('repost','动词英 /ˌriːˈpəʊst/、美 /ˌriːˈpoʊst/；名词英 /ˈriːpəʊst/、美 /ˈriːpoʊst/','重新发布；转发；重发内容',
 '内容已经发过一次，再把它放出来，可能同一平台，也可能另一个地方。',
 're-（再次）+ post（发布）；现代网络用法常见，不是把一个柱子反过来插。',POST+[['re- + post → repost','再次发布；重发内容']],
 'repost a photo 再发、转发照片，a repost of a message 一条消息的转发。是否保留原文、链接等因平台功能而异。',
 'repost a photo；repost a message；a repost of。',
 'repost 再发布，reply 回复；转发内容不一定附上对原作者的回答。',
 ('The museum reposted the photo with a clearer caption.','博物馆配上更清楚的说明，重新发了照片。'),('The announcement was a repost of last week’s message.','这则通知是上周消息的重发。'))
W('postal','英 /ˈpəʊstəl/；美 /ˈpoʊstəl/','邮政的；邮递的',
 '把信件、包裹从收取到分拣再送达的服务体系，用 postal 来修饰。',
 'post（邮递）+ -al，构词受法语 postal 等对应形式影响。al 形成相关形容词，不是表示所有字母。',POST+[['post + -al → postal','与邮政、邮递相关的']],
 'the postal service 邮政服务，a postal address 邮寄地址，postal workers 邮政工作人员。并非一切在线消息都算邮政。',
 'the postal service；a postal address；postal workers；postal delivery。',
 'postal address 是邮寄地址，email address 电子邮箱地址；发信方式不同，不凭 address 相同就混写。',
 ('Please include your full postal address.','请填写完整邮寄地址。'),('The postal service delivers to the village twice a week.','邮政服务每周向村里投递两次。'))
W('postage','英 /ˈpəʊstɪdʒ/；美 /ˈpoʊstɪdʒ/','邮资；邮费',
 '把东西寄出去要支付的费用，不是信里写了多少字。',
 'post + -age，-age 在这里形成与服务、费用等有关的名词；不是 post“岗位”的年龄。',POST+[['post + -age → postage','邮递服务费用']],
 'pay the postage 支付邮资，postage included 含邮费，a postage stamp 邮票。具体费用随服务而变，词里不带固定金额。',
 'pay the postage；postage included；a postage stamp；postage costs。',
 'postage 是邮寄费用，stamp 邮票是传统支付、标示邮资的形式之一；有 postage 不一定手贴一张纸邮票。',
 ('The price includes postage.','价格包含邮费。'),('I forgot to check the postage before sending the parcel.','寄包裹前，我忘了查邮费。'))
W('postcard','英 /ˈpəʊstkɑːd/；美 /ˈpoʊstkɑːrd/','明信片',
 '一张可以写地址、写短消息直接寄走的卡片，常一面有风景图。',
 'post（邮递）+ card；按邮寄形式命名，不是贴在柱上的海报。',C('post〔邮递〕','card','postcard','通常不用信封寄送短消息的卡片'),
 'send a postcard 寄明信片，a picture postcard 风景明信片。图案常见但不由 card 一词保证一定有摄影作品。',
 'send a postcard；a picture postcard；write a postcard。',
 'postcard 可直接写地址寄送，poster 招贴用于张贴展示；都可有大图，但通常尺寸、用途不同。',
 ('She sent us a postcard from the mountains.','她从山区给我们寄来一张明信片。'),('I wrote a short message on the back of the postcard.','我在明信片背面写了一条短消息。'))
W('postmark','英 /ˈpəʊstmɑːk/；美 /ˈpoʊstmɑːrk/','邮戳；盖邮戳',
 '信件走过邮政系统，留下处理日期、地点等印记，像它旅途中的一个时间章。',
 'post（邮政）+ mark（标记），可名词也可动词。传统邮戳还常用于注销邮票，不让同一邮票反复使用。',C('post〔邮政〕','mark','postmark','邮政处理留下的戳记；盖这种戳'),
 'a clear postmark 清楚的邮戳，an envelope postmarked in May 五月盖邮戳的信封。邮戳日期不是所有语境下都等于写信日期。',
 'a clear postmark；a dated postmark；an envelope postmarked。',
 'postmark 邮政处理印记，watermark 水印；同叫 mark，形成方式、作用不同。',
 ('The postmark showed that the letter had been sent from Paris.','邮戳显示信是从巴黎寄出的。'),('The envelope was postmarked two days before it arrived.','信封上的邮戳日期比到达日期早两天。'))
W('postcode','英 /ˈpəʊstkəʊd/；美 /ˈpoʊstkoʊd/','邮政编码〔尤英式〕',
 '地址不只靠整段文字，还用一组代码帮助系统分区、分拣、投递。',
 'post（邮政）+ code（代码），不是电脑程序 post 的源代码。',C('post〔邮政〕','code','postcode','帮助邮政分拣、定位地址区域的编码'),
 'enter your postcode 输入邮编，a postcode area 邮编区；各国编码结构不同。美国日常通常说 ZIP code。',
 'enter a postcode；a postcode area；a full postcode。',
 'postcode 邮政编码，area code 电话区号；都像几位字符，但所属系统与用途不同。',
 ('Please enter your postcode below the address.','请在地址下面填写邮编。'),('The search tool finds nearby branches by postcode.','搜索工具按邮编查找附近网点。'))
W('postman','英 /ˈpəʊstmən/；美 /ˈpoʊstmən/','邮递员〔传统男性称谓，也可泛用〕',
 '不是只坐在邮局里的人，而是把邮件送到住户、单位的人。',
 'post（邮件投递）+ man；现代不指定性别可说 postal worker、mail carrier，具体岗位仍按职责。',C('post〔邮件、投递〕','man','postman','从事邮件收取、投递的人'),
 'the local postman 当地邮递员，the postman delivers letters 邮递员送信；英式很常见。',
 'the local postman；the postman’s bag；wait for the postman。',
 'postman 投递员，postmaster 邮局负责人；不是每一位邮递员都管理整个邮局。',
 ('The postman delivered a parcel this morning.','邮递员今早送来一个包裹。'),('Our postman knows every lane in the village.','我们的邮递员熟悉村里每条小路。'))
W('postmaster','英 /ˈpəʊstmɑːstə/；美 /ˈpoʊstmæstər/','邮局负责人；邮件系统管理员〔技术语境〕',
 '有人负责整个邮局、邮务安排；电子邮件系统也借这个名字称管理角色。',
 'post + master（负责人、管理者），不是邮递员一定比别人更有学历。',C('post〔邮务〕','master〔负责人〕','postmaster','邮局负责人；电子邮件系统管理角色'),
 'the village postmaster 村邮局负责人，contact the postmaster 联系邮件系统管理者；技术语境里的 postmaster 还可能是管理联系地址、账号名称。',
 'the village postmaster；contact the postmaster；the local postmaster。',
 'postmaster 管理邮务，postman 常负责投递；互联网 postmaster 也不等于普通新闻发帖者 poster。',
 ('The postmaster explained the new collection times.','邮局负责人解释了新的收件时间。'),('The error message suggested contacting the postmaster.','错误消息建议联系邮件系统管理员。'))
W('blogpost','英 /ˈblɒɡpəʊst/；美 /ˈblɑːɡpoʊst/','博客文章；博文',
 '博客不是只有一个总页面，其中每一篇发出来的文章是一篇 blogpost。',
 'blog + post（发布的内容），也常分写 blog post；不是书信 postal 的普通同义词。',C('blog','post〔帖子、发布内容〕','blogpost','发布在博客上的一篇文章'),
 'write a blogpost 写博文，a blogpost about travel 旅行主题博文。长短、文体不限于私人日记。',
 'write a blogpost；publish a blogpost；a blogpost about。',
 'blog 博客整体或写博客的活动，blogpost 一篇具体内容；a blog can contain many blogposts。',
 ('She wrote a blogpost about restoring old furniture.','她写了一篇修复旧家具的博文。'),('The blogpost links to the original research.','博文链接到了原始研究。'))
W('outpost','英 /ˈaʊtpəʊst/；美 /ˈaʊtpoʊst/','前哨；偏远站点；外围分支',
 '主体在别处，这里是伸出去、离核心较远的一个据点。',
 'out-（在外、外围）+ post（驻点），由前沿或远处驻点扩到偏远研究站、业务分支等。',C('out-','post〔驻点〕','outpost','外围前哨、远处站点或分支'),
 'a remote outpost 偏远据点，a research outpost 研究站点，a company’s outpost 某公司的外设分支。不是每一个都承担军事任务。',
 'a remote outpost；a research outpost；an outpost of。',
 'outpost 外围驻点，output 输出；都有 out，后半选的词义完全不同。',
 ('The researchers worked at a remote outpost in the mountains.','研究人员在山里一个偏远站点工作。'),('The small gallery became an outpost of the city’s art scene.','这家小画廊成了城市艺术圈向外延伸的一个据点。'))
W('goalpost','英 /ˈɡəʊlpəʊst/；美 /ˈɡoʊlpoʊst/','球门柱；球门架相关立柱',
 '球门两边竖起的柱子标出得分目标；若总挪它，别人就没法按原规则射门。',
 'goal + post（柱），不是邮寄一个目标；体育结构因项目不同，常见复数 goalposts。',C('goal','post〔柱〕','goalpost','标出球门、得分目标的立柱'),
 'hit the goalpost 球击中门柱；move the goalposts 比喻临时更改标准、规则，让别人更难达标。',
 'hit the goalpost；the goalposts；move the goalposts。',
 'goalpost 柱、goalkeeper 守门员；move the goalposts 的比喻不是指每次维护场地都在耍赖。',
 ('The ball struck the goalpost and bounced away.','球撞上门柱，弹了出去。'),('We cannot finish if you keep moving the goalposts.','你若不断改标准，我们就没法做完。'))
R('B4199','柱与张贴；邮递；驻点、岗位','POST：同形几条来路，先问它在说柱、信、帖子还是岗位','柱上贴告示成为公开发布；驿站联系邮递；安置的位置联系驻点岗位。不要用一个在后来包所有意思。',
 '柱义上接拉丁 postis，经古英语、古法语；邮递、驻点岗位接法语 poste、意大利 posta 等。post- 表在后的前缀另看，不能把 postman 解释成后面的人。',
 'post → poster、posting、repost 讲发布；postal → postage、postcard、postmark、postcode、postman、postmaster 讲邮务；blogpost 讲内容；outpost、goalpost 与已有 signpost 等分清位置和柱。',
 [['柱、发布、派驻的基本词','post · poster · posting · repost'],['邮政与费用、载体、印记、编码','postal · postage · postcard · postmark · postcode'],['邮政人员和数字内容','postman · postmaster · blogpost'],['驻点和柱形物','outpost · goalpost · signpost · lamppost · milepost']],
 'poster 海报、发帖者；postcard 明信片；postage 邮资、postmark 邮戳、postcode 邮编；postmaster 管理者，不是所有 post 都等于在后。',
 'The postman brought a postcard with a clear postmark, while I reposted a photo of the old goalposts.\n\n邮递员带来一张邮戳清晰的明信片，我则重发了一张旧门柱照片。',
 'post poster posting repost postal postage postcard postmark postcode postman postmaster blogpost outpost goalpost signpost lamppost milepost')
if __name__=='__main__':save('continuation_20261028_be',ROOTS,WORDS)
