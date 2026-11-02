"""Resume and everyday matching, determination, short forms and reactions."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
def S(word,base):
 urls=['https://en.wiktionary.org/wiki/'+word+'#English']
 urls.append('https://www.merriam-webster.com/dictionary/'+base if base in ['admin','lineup'] else 'https://www.etymonline.com/word/'+base)
 return urls
EXISTING_ROOT_ADDITIONS={
 'C1454':dict(words='resume resumes resumed resuming'.split(),label='resume：再拿起 → 恢复继续；另借法语概述义为简历',note='拉丁 re- 再次 + sumere 拿起 → resumere，经法语等进入英语动词。简历名词 resume、résumé 另借法语过去分词名词化的概述用法，两种现代词性读音不同；不能把简历当成现代英语动词加一个零后缀才有。'),
 'B2894':dict(words='match matching'.split(),label='match → matching：配成一对到相配、匹配过程',note='匹配接古英语 mæcca 同伴、一对中的一个，与更远配合材料相连；火柴 match 是另源。matching 是 match + -ing，不从火柴燃烧画面派生。'),
 'C1364':dict(words='resolve resolved'.split(),label='resolve → resolved：解开问题；想定之后的坚决',note='拉丁 re- 返回或加强 + solvere 松开 → resolvere；拆开、分析到解决与决定。resolved 可表示已解决，也可表示决意；后者不是又把人绑紧的独立相反词根。'),
 'B2805':dict(words='derby derbies'.split(),label='derby：赛事专名到同城、同地区对抗',note='与 race 比较比赛，不由 race 派生。Derby 赛马以德比伯爵名号命名，更远接德比地名；普通名词扩大到重大比赛，同城对抗等。不能误说赛马最初就在德比市举行。'),
 'C0755':dict(words='mod mods modded modding'.split(),label='mod：几种长词的短称；改造动词来自修改一支',note='mod 可分别缩略 modification、moderator、modern 等，较远多在 modus 方式、尺度词族附近。游戏模组、管理员、现代派不能全按同一个缩略全称解释；modded、modding 接修改动词。'),
 'C0743':dict(words='admin admins'.split(),label='administration、administrator → admin → admins',note='admin 可缩略管理事务、管理者等相关长词；名词可数性随含义变化。较远 administrator 等接拉丁服务、管理词族，不能从 admin 字面强拆成 ad + min 就把每个现代意思猜完。'),
 'C0675':dict(words='lineup lineups'.split(),label='line + up → lineup：排成队到阵容、名单',note='line up 的排队、安排关系形成名词 lineup，指上场名单、阵容、节目安排等；闭合名词通常前重音，动词短语通常强调 up。'),
 'A1760':dict(words='boo boos booed booing'.split(),label='boo：另源的喊声、嘘声与喝倒彩',note='和 shout 比较发声，不由 shout 派生。boo、boh 是能发出突然而响亮声音的呼声，后来作不赞同的声音名、喝倒彩动词；这里先学惊吓、嘘声两类常见用法。'),
}
RESUME=[['拉丁 re- 再次 + sumere 拿起 → resumere','sumere 更早有 sub- 从下 + emere 拿的分析'],['法语、拉丁相关形式 → 英语 resume 动词：重新拿起、恢复继续','法语 résumé 概述另作英语名词：摘要、简历；重音与动词不同']]
MATCH=[['古英语 mæcca：同伴、一对中的一个 → match','同伴、相配者 → 匹配、配对的动词'],['match + -ing → matching','相配的、对应的；匹配过程，和火柴另源']]
RESOLVED=[['拉丁 re- 返回或加强 + solvere 松开 → resolvere','解开、分成部分 → 分析、解决、决定'],['法语、拉丁相关形式 → 英语 resolve + -ed → resolved','问题已解决；分析后想定了 → 坚定、决意']]
DERBY=[['德比地名 → 德比伯爵名号 → Derby 赛马名','赛事在 Epsom 起源，不是以所在德比市直接命名'],['重大赛事名称扩大为普通 derby','现代也常见同城、同地区队伍对抗；名词另有圆顶硬礼帽用法']]
MOD=[['modification、moderator、modern 等 → 各自缩略 mod','不同场景要还原不同长词，不强迫全是模组'],['修改一支：mod 名词、动词 → modded、modding','现代游戏、设备等可作修改、改造；动词变化双写 d']]
ADMIN=[['administration 管理事务、administrator 管理者等 → admin','相关长词的缩略，并不都指同一个可数事物'],['admin：事务时常不可数；人员时可数 → admins','现代系统、群组等可有一个或多个管理者']]
LINEUP=[['line + up：排成一队、安排到位的短语关系','形成名词 lineup'],['队伍、上场名单 → 阵容、节目安排、产品系列','现代闭合名词与两个词的动词短语分开用']]
BOO=[['早期 boo、boh 等突然而响亮的呼声','可用于惊吓、引人注意，拟声式表达'],['不赞同的嘘声名词 → boo 喝倒彩动词','名词复数 boos；动词 booed、booing 保留 oo']]
W('resume','动词：英 /rɪˈzjuːm/、美 /rɪˈzum/；名词：英 /ˈrezjʊmeɪ/、美 /ˈrɛzəmeɪ/','恢复、继续；〔也写 résumé〕简历、摘要',
 '暂停的事情再拿起来，是 resume；把人生经历重新拢成一份概述，另一条法语借入线又形成名词 resume、résumé。外形相同，常见读音却不同。',
 '动词经法语、拉丁 resumere，re- 再 + sumere 拿起；简历名词另借法语 résumé 概述，是法语动词过去分词的名词化，不是英语动词读音直接拿来作简历。',RESUME,
 'resume work 是恢复工作；resume reading 是接着阅读；send a resume 是发简历。动词常在末节重读，名词常在前面重读、末尾读 /meɪ/。',
 'resume work；resume reading；send a resume；update a resume。',
 'resume、résumé 都可写简历；resume 也可作继续的动词。看句法还不够时，朗读必须分清两套读音。',
 ('We will resume the meeting after lunch.','午饭后我们继续开会。'),('You can resume reading whenever you are ready.','你准备好后，随时可以继续阅读。'),('Please attach a resume to your application.','请随申请附上简历。'),sources=S('resume','resume'))
W('resumes','动词：英 /rɪˈzjuːmz/、美 /rɪˈzumz/；名词：英 /ˈrezjʊmeɪz/、美 /ˈrɛzəmeɪz/','恢复、继续〔第三人称单数〕；简历〔复数〕',
 'the meeting resumes 是会议继续；several resumes 是几份简历。一个 s 既可接动词，也可接名词，两条现代读音随基础词保留。',
 'resume + -s → resumes，动词末音 /m/ 后加 /z/；简历名词末尾 /eɪ/ 后也加 /z/。两者都不因此增加额外 /ɪz/ 音节。',RESUME+[['resume + -s → resumes','单数主语继续；或多个简历；读音依词性分支']],
 'the session resumes 是活动继续；review resumes 是审阅简历。名词也常保留重音符号写 résumés。',
 'the meeting resumes；play resumes；review resumes。',
 'resumes 恢复与 resumes 简历不是同一读音；不能为了省重音符号，就把简历名词读成动词。',
 ('The meeting resumes at two o’clock.','会议两点继续。'),('The recruiter reviewed several resumes that morning.','招聘人员那天上午审阅了几份简历。'),sources=S('resumes','resume'))
W('resumed','英 /rɪˈzjuːmd/；美 /rɪˈzumd/','恢复了、继续了〔过去式、过去分词〕',
 '暂停后重新接上，是 resumed。前面已经做到一部分，现在拿回来继续，不一定从头重新开始。',
 'resume 去末尾 e + -ed → resumed；/m/ 后 -ed 读 /d/。这里是继续动词的变化，不是把简历名词变成过去式。',RESUME+[['动词 resume 去 e + -ed → resumed','过去式、过去分词；末节重音保留']],
 'resumed work 是恢复工作；resumed the discussion 是接着讨论；service resumed 是服务恢复了。',
 'resumed work；resumed the discussion；service resumed。',
 'resumed 常接上中断之处；restarted 也可能从头启动，具体上下文决定是否清零、重来。',
 ('They resumed work after the break.','休息后，他们继续工作。'),('Normal service resumed the following morning.','正常服务在第二天早上恢复。'),sources=S('resumed','resume'))
W('resuming','英 /rɪˈzjuːmɪŋ/；美 /rɪˈzumɪŋ/','正在恢复、继续；恢复这一过程',
 '暂停结束，事情正在重新接上，是 resuming。它把“再拿起”的动作展开成一个过程。',
 'resume 去末尾 e + -ing → resuming；不双写 m，基础动词词尾是带不发音 e 的拼写。',RESUME+[['动词 resume 去 e + -ing → resuming','现在分词、动名词；恢复、继续过程']],
 'resuming work 是恢复工作；before resuming 是恢复之前；be resuming a discussion 是正在接着讨论。',
 'resuming work；resuming the discussion；before resuming。',
 'resume 后可直接接名词或 -ing，如 resume reading；不是每次都接 to do。resuming 是它自身的分词变化。',
 ('They are resuming the discussion after a short break.','短暂休息后，他们正继续讨论。'),('Before resuming work, she checked the latest notes.','继续工作前，她检查了最新记录。'),sources=S('resuming','resume'))
W('matching','英 /ˈmætʃɪŋ/；美 /ˈmætʃɪŋ/','相配的、成套的；正在匹配、配对；匹配过程',
 '两只袜子颜色、样式对应，是 matching socks；把资料里的对应项找出来，也是 matching。核心是两边能对上，不是点火。',
 'match + -ing → matching。匹配动词接同伴、一对中的一个的旧名词线，和另源火柴 match 分开。',MATCH,
 'matching colours 是相配颜色；matching socks 是成对、款式相配的袜子；matching names to records 是把姓名与记录对应起来。',
 'matching socks；matching colours；matching names to records。',
 'matching 可以是相同款式，也可以是协调、对应；matching furniture 未必每件都长得完全一样。',
 ('She wore a scarf and matching gloves.','她戴着围巾和与之相配的手套。'),('We spent an hour matching names to records.','我们花了一小时把姓名和记录对应起来。'),sources=S('matching','match'))
W('resolved','英 /rɪˈzɒlvd/；美 /rɪˈzɑlvd/','已解决的；下定决心的；解决了、决定了〔过去式、过去分词〕',
 '一个结理清了，事情解决了，是 resolved；一个人想清楚、不再摇摆，也是 resolved。不是同一词突然相反，而是分别看问题和人的决定。',
 'resolve 去末尾 e + -ed → resolved，/v/ 后后缀读 /d/。较远拉丁 resolvere 松开、分析，经过问题解开、分析后决定等关系形成现代用法。',RESOLVED,
 'the issue is resolved 是问题已解决；be resolved to do 是决心做；resolved on a course of action 是决定采取某种做法。',
 'a resolved issue；resolved to continue；resolved on a plan。',
 'resolved to leave 是决意离开；the problem was resolved 是问题被解决。主语、to 和被动结构帮助辨认，不能一见 resolved 就都译成已解决。',
 ('The technical issue has been resolved.','技术问题已经解决。'),('She was resolved to finish the course.','她下定决心要完成这门课程。'),sources=S('resolved','resolve'))
W('derby','英 /ˈdɑːbi/；美 /ˈdɝbi/','赛马等重要赛事；同城、同地区队伍的比赛；圆顶硬礼帽',
 '体育报道里的 local derby，常是本地两支队伍的直接较量。名称起初借自一场有名的赛马，又扩大到更多比赛。',
 'Derby 赛马以德比伯爵名号命名，赛事起源地是 Epsom。名号更远接 Derby 地名，包含旧鹿名与北欧居住地材料；现代比赛义不能直接按鹿村来猜。',DERBY,
 'a local derby 是本地对抗赛；a football derby 是足球德比；美国语境 a derby 还可指圆顶硬礼帽。读音英式第一元音 /ɑː/，美式常见 /ɝ/。',
 'a local derby；a football derby；a derby race。',
 'Derby 作为赛事专名、地名可大写；普通一场 derby 可小写。不能因为赛马名带 Derby，就断定比赛发生在德比市。',
 ('The two local clubs meet in a derby on Saturday.','两家本地俱乐部周六将在德比战中交锋。'),('The costume included a dark derby and a long coat.','这套服装包括一顶深色圆顶硬礼帽和一件长外套。'),sources=S('derby','derby'))
W('derbies','英 /ˈdɑːbiz/；美 /ˈdɝbiz/','德比战、重要赛事；圆顶硬礼帽〔复数〕',
 '一个赛季有好几场本地对抗，这些比赛就是 derbies。复数也能数几顶 derby 礼帽，要看谈的是体育还是服装。',
 'derby 词尾辅音字母 b + y，变 y 为 i + -es → derbies；原词末尾 /i/ 保留，再接 /z/，不另加一个音节。',DERBY+[['derby 变 y 为 i + -es → derbies','多个赛事或帽子；词尾 /biz/']],
 'local derbies 是本地对抗赛；fierce derbies 是激烈德比战；bowler hats 在美式也可称 derbies。',
 'local derbies；football derbies；several derbies。',
 'derbies、abbeys 都以字母 y 收尾，但 derby 前是辅音 b，需要改 ies；abbey 前是元音 e，直接加 s。',
 ('Local derbies usually draw large crowds.','本地德比战通常吸引大批观众。'),('The shop displays several old derbies beside the coats.','店里在外套旁陈列着几顶旧圆顶硬礼帽。'),sources=S('derbies','derby'))
W('mod','英 /mɒd/；美 /mɑd/','修改、改造；游戏模组；管理员等长词的短称',
 '给游戏换一套玩法，是装一个 mod；群里帮忙管理的人，也可能叫 a mod。同一个短词，要先看它究竟把哪个长词截短了。',
 '修改一支缩略 modification、modify，管理员一支缩略 moderator；modern 的时尚文化短称也写 mod。不能把所有名词和动词都只还原为一种全称。',MOD,
 'a game mod 是游戏模组；mod a game 是修改游戏；ask a mod 是询问管理员。时尚史语境的 mod 则可能接现代派文化。',
 'a game mod；install a mod；ask a mod；mod a game。',
 'mod 的模组与管理员义在现代网络场景都常见。看 install、download、ask 等动词，通常很容易判断说的是内容还是人。',
 ('This mod adds new buildings to the game.','这个模组给游戏增加了新建筑。'),('Ask a mod if you need help with the forum rules.','如果不懂论坛规则，就问一位管理员。'),sources=S('mod','mod'))
W('mods','英 /mɒdz/；美 /mɑdz/','模组、修改项目；管理员〔复数〕；修改〔第三人称单数〕',
 '几个游戏模组是 mods，几位版主也是 mods。复数规则一样，缩略前的长词却不一定相同。',
 'mod + -s → mods，/d/ 后接 /z/。modification、moderator 等分别缩成 mod 后，都可以按相应可数名词加复数。',MOD+[['mod + -s → mods','多个模组、管理者；也可为修改动词单数']],
 'game mods 是游戏模组；forum mods 是论坛管理员；she mods games 是她修改游戏。上下文把词义分支分开。',
 'game mods；forum mods；mods a game。',
 'mods 不等于每次都在修改代码；作人员名词时是 moderators 的短称，与执行修改的动词不必混同。',
 ('The latest update works with most of the existing mods.','最新更新兼容大多数现有模组。'),('The mods removed the duplicate posts.','管理员删掉了重复帖子。'),sources=S('mods','mod'))
W('modded','英 /ˈmɒdɪd/；美 /ˈmɑdɪd/','修改过、改造过的；修改了〔过去式、过去分词〕',
 '原来的游戏、设备被动过，换了功能或外观，就是 modded。这里接的是修改一支，不是把管理员变成过去式。',
 'mod 双写 d + -ed → modded；短元音单音节词末双写，基础 /d/ 后 -ed 读 /ɪd/，增加音节。',MOD+[['mod 双写 d + -ed → modded','修改动词过去式、过去分词；末尾 /dɪd/']],
 'a modded game 是改过的游戏；a modded controller 是改造过的控制器。被改不自动意味着更好，只说明内容、功能、外形等发生变化。',
 'a modded game；a modded controller；heavily modded。',
 '本组例句的 modded 接修改一支；论坛语境中 mod 也能作管理动词，须连着宾语、情境还原，不能把短称的所有动作排除在外。',
 ('She played a heavily modded version of the game.','她玩的是一个大幅修改过的游戏版本。'),('He modded the controller to make the buttons easier to reach.','他改造了控制器，让按钮更容易够到。'),sources=S('modded','mod'))
W('modding','英 /ˈmɒdɪŋ/；美 /ˈmɑdɪŋ/','游戏、设备等的修改；正在改造',
 '给游戏添地图、换外观、改玩法，这类修改活动常叫 modding。它把单个 mod 背后的动手过程当成一项活动来讲。',
 'mod 双写 d + -ing → modding，接修改动词一支；现在分词、动名词可指具体过程或爱好、活动。',MOD+[['mod 双写 d + -ing → modding','现在分词、动名词；修改、改造活动']],
 'game modding 是游戏模组制作、修改；a modding community 是相关社群；be modding a game 是正在改游戏。',
 'game modding；a modding community；modding tools。',
 '这里先用制作、改动内容的 modding 记动词；管理员 mod 的缩略名词本身，并不要求每次管理动作也按这套含义解释。',
 ('She became interested in game modding at university.','她在大学时开始对游戏修改感兴趣。'),('The community shares tools for modding the game.','这个社群分享修改这款游戏的工具。'),sources=S('modding','mod'))
W('admin','英、美 /ˈædmɪn/','管理、行政事务；管理员；管理的〔非正式短称〕',
 '报销、登记、处理表格这些工作，可以统称 admin；负责系统、群组管理的人，也能叫 an admin。一个说事务，一个说人。',
 '分别缩略 administration 管理事务、administrator 管理者，及 administrative 的相关用法；这些长词有共同的服务、管理词族背景，但现代缩略后的可数性不同。',ADMIN,
 'do admin 是处理管理事务；an admin 是一名管理员；admin access 是管理权限。先看有没有 a、有没有在数人。',
 'do admin；an admin；admin access；admin work。',
 'admin work 通常说事务，不可数；an admin、two admins 数管理者。不能把所有 admin 都翻成管理员这个人。',
 ('I spent the morning doing admin.','我一上午都在处理行政杂务。'),('Ask an admin to update the group settings.','请一位管理员更新群组设置。'),sources=S('admin','admin'))
W('admins','英、美 /ˈædmɪnz/','管理员、行政人员〔复数〕',
 '一个群不只一位管理员，是 admins。这里数人，和一堆需要处理的 admin 事务不是同一个可数方式。',
 'admin + -s → admins，/n/ 后接 /z/；可数人员义通常接 administrator 等相关短称。',ADMIN+[['admin + -s → admins','多名管理者；词尾 /nz/']],
 'group admins 是群管理员；system admins 是系统管理员；contact the admins 是联系管理员们。',
 'group admins；system admins；contact the admins。',
 'two admins 数两个人；two admin tasks 数两项事务。事务数量要把 task、job 等单位说清楚。',
 ('The group has three admins.','这个群有三位管理员。'),('Only the admins can change these settings.','只有管理员能更改这些设置。'),sources=S('admins','admin'))
W('lineup','英、美 /ˈlaɪnʌp/','阵容；出场名单；节目安排；排成一列的人',
 '把将要出场的人排成一列，或写成一份名单，就是 lineup。即使他们还没真站成队，节目和球队也能先有一套阵容。',
 'line + up 形成 line up 排队、安排等短语，再有名词 lineup；闭合名词常前重音，动词短语常强调 up。',LINEUP,
 'the starting lineup 是首发阵容；a festival lineup 是演出阵容；a product lineup 是一系列产品。也可用于排成一列供辨认的人。',
 'the starting lineup；a festival lineup；a product lineup。',
 'lineup 是名词；line up 是动词短语。The lineup is strong 与 the players line up 不能只因为中文都像排队就写成同一种形式。',
 ('The coach announced the starting lineup.','教练公布了首发阵容。'),('The festival has an impressive lineup this year.','今年这个音乐节的演出阵容很强。'),sources=S('lineup','lineup'))
W('lineups','英、美 /ˈlaɪnʌps/','阵容、出场名单；节目安排〔复数〕',
 '不同球队各有一份首发名单，不同日期各有一套节目，这些组合就是 lineups。数的是成套安排，而不是名单里的每个人。',
 'lineup + -s → lineups，整个复合名词末尾加 s；/p/ 后后缀读 /s/。',LINEUP+[['lineup + -s → lineups','多套阵容、名单、安排；末尾 /ps/']],
 'different lineups 是不同阵容；starting lineups 是多队或多场的首发安排；compare lineups 是比较阵容。',
 'different lineups；starting lineups；compare the lineups。',
 'lineups 是名词复数；lines up 是 line up 动词短语的第三人称单数，s 的位置不同。',
 ('Both teams announced their starting lineups.','两队都公布了自己的首发阵容。'),('The two festivals have very different lineups.','这两个音乐节的演出阵容很不一样。'),sources=S('lineups','lineup'))
W('boo','英、美 /buː/','呜、哇〔突然吓人的喊声〕；嘘声；喝倒彩',
 '躲在门后突然喊一声 boo，是吓人；观众拖长同样的声音，又能表达不满，成了嘘声。声音先让人听见，态度由场景决定。',
 '早期 boo、boh 是适合突然大声喊出的呼声；后来用作不赞同的声音名，进一步形成喝倒彩的动词。不是从中文嘘的发音借来。',BOO,
 'shout boo 是突然喊一声；boo a performer 是向表演者喝倒彩；a boo 是一声嘘声。这里先掌握声音、态度这条用法线。',
 'shout boo；boo the decision；a loud boo。',
 'boo 的常见读音 /buː/ 与中文“嘘”的声音并不相同；翻译写嘘声，是在对应观众表达不满的功能。',
 ('“Boo!” he shouted from behind the door.','“哇！”他从门后突然喊了一声。'),('The audience began to boo the decision.','观众开始向这个决定喝倒彩。'),sources=S('boo','boo'))
W('boos','英、美 /buːz/','嘘声〔复数〕；喝倒彩〔第三人称单数〕',
 '几声、成片的不满喊声，是 boos；the crowd boos 则是人群正在或通常作出喝倒彩动作。声音与动词位置分开看。',
 'boo + -s → boos，元音后后缀读 /z/；名词复数与动词第三人称单数同形。',BOO+[['boo + -s → boos','多个嘘声；或单数主体喝倒彩']],
 'cheers and boos 是欢呼和嘘声；a chorus of boos 是一片嘘声；boos the announcement 是向宣布喝倒彩。',
 'cheers and boos；a chorus of boos；boos the decision。',
 'boos 与 booze 酒同音 /buːz/，来源和所指不同；观众反应里 boos 常是嘘声，不能按酒来解释。',
 ('The announcement was met with a chorus of boos.','宣布一出，就响起了一片嘘声。'),('Some cheers were drowned out by boos.','一些欢呼声被嘘声盖了过去。'),sources=S('boos','boo'))
W('booed','英、美 /buːd/','喝了倒彩；受到嘘声〔过去式、过去分词〕',
 '观众已经发出不赞同的嘘声，是 booed；表演者被嘘，则是 was booed。词尾变过去，声音仍是那一声 boo。',
 'boo + -ed → booed，保留 oo，元音后 -ed 读 /d/；不把 e 单独读成一个新音节。',BOO+[['boo + -ed → booed','过去式、过去分词；读 /buːd/']],
 'booed the decision 是向决定喝倒彩；was booed off the stage 是在嘘声中下台；语气通常明确表达反对、不满。',
 'booed the decision；was booed；booed off the stage。',
 'booed 不是 cheered 欢呼；两者同是观众出声，表达的态度不同。',
 ('The crowd booed the referee’s decision.','人群向裁判的判罚喝倒彩。'),('The performer was booed during the final act.','最后一幕表演时，演员受到了嘘声。'),sources=S('booed','boo'))
W('booing','英、美 /ˈbuːɪŋ/','正在喝倒彩；嘘声、喝倒彩的行为',
 '观众持续发出不满的声音，这个过程是 booing；把行为本身当一回事讨论，也能用这个 -ing 名词形式。',
 'boo + -ing → booing，保留 oo，再接 /ɪŋ/；两个元音部分都保留，不写成 boing。',BOO+[['boo + -ing → booing','现在分词、动名词；嘘声过程或行为']],
 'be booing 是正在喝倒彩；loud booing 是很响的嘘声；booing from the crowd 是人群传来的倒彩声。',
 'loud booing；booing from the crowd；start booing。',
 'boing 常拟弹簧弹起的声音；booing 是 boo 加 -ing 的正常形式，不能因为书写接近就少掉一个 o。',
 ('Loud booing came from the back of the hall.','大厅后方传来很响的嘘声。'),('The spectators started booing when the result was announced.','结果一公布，观众就开始喝倒彩。'),sources=S('booing','boo'))
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_ziq',ROOTS,WORDS)
 extend_lessons()
