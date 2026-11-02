"""Common people, activities and outcomes in the plural."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'B2732':dict(words=['friend','friends'],label='friend → friends：朋友、好友；交朋友',note='friends 词尾是 /dz/；make friends with 是和……交朋友，be friends with 是已经有这层关系。'),
 'B3191':dict(words=['game','games'],label='game → games：游戏、比赛与花招',note='复数 games 可说多场活动，也可在 play games 中说耍花招；game 狩猎物的集合义一般不这样数。'),
 'B3630':dict(words=['member','members'],label='member → members：团体成员',note='member 接拉丁 membrum 身体的一部分，扩展为组织成员；members 可指会员、委员等。'),
 'C1325':dict(words=['service','services'],label='service → services：服务项目、系统与检修',note='service 经法语接拉丁 servitium；services 可数不同服务，也可在动词用法中说检修。'),
 'B3108':dict(words=['player','players'],label='play → player → players：参与者、演奏者和播放器',note='player 的 -er 可表人或设备；players 是其复数，不一律都译成玩家。'),
 'C1440':dict(words=['student','students'],label='student → students：用心学习的人们',note='student 经法语接拉丁 studens、studere；与 study 同族，但不是现代英语简单裁字加 -ent 的产物。'),
 'C1169':dict(words=['point','points'],label='point → points：点、要点、分数与指向',note='point 的点和尖端两路都与拉丁刺、戳词族相连；points 还可作指向的第三人称形式。'),
 'C1248':dict(words=['result','results'],label='result → results：结果、成绩与产生',note='result 接拉丁 resultare 反弹、回响一系，后来用于随之产生的结果；results from 表来源，results in 表后果。'),
 'B2977':dict(words=['show','shows'],label='show → shows：节目、展览；显示',note='show 的名词、动词在 shows 中同形；名词看多场节目，动词看单数主语显示了什么。'),
 'B3064':dict(words=['die','died'],label='die → died：死去；声音、光线等渐息',note='死亡动词 die 的过去形式是 died，词尾 /d/；与骰子名词 die 的法语来源分开。'),
 'B2552':dict(words=['kill','killed'],label='kill → killed：使死去；终止、消磨',note='killed 保留 kill 的双写 ll，再加 ed；既可指杀死，也可在固定语境说终止、消磨。'),
 'A1741':dict(words=['happen','happened'],label='happen → happened：发生过；碰巧',note='happened 的 -ed 读 /d/；事件自己发生，通常不用 be happened 这样的被动形式。'),
}
W('friends','/frendz/','朋友、好友〔复数〕；与……成为社交平台好友〔friend 的第三人称单数〕',
 '可以互相信任、愿意来往的人是 friends。这个词重在关系，认识对方、见过几面，还不一定已经算朋友。',
 'friend + -s；/d/ 后读 /z/，结尾 /ndz/，ie 仍读 /e/。friend 继承古英语 freond／friond，与爱、亲爱的人这一日耳曼词族相关。',
 [['古英语 freond／friond → friend','亲爱的人、朋友'],['friend + -s → friends','多个朋友；现代也有平台加好友的动词用法']],
 'make friends with 和……交朋友；be friends with 和……是朋友；close friends 亲密朋友；friends of mine 我的几位朋友。社交平台上的 friends 未必彼此熟悉。',
 'old friends；keep in touch with friends。','make friends 是建立关系，be friends 是已经存在关系。She is a friend of mine 中 a friend 是单数，不能照抄复数搭配变成 a friends。',
 ('We became friends while working on the same project.','我们一起做项目时成了朋友。'),('She still keeps in touch with friends from school.','她仍和上学时的朋友保持联系。'),sources=['https://en.wiktionary.org/wiki/friends#English','https://en.wiktionary.org/wiki/friend#English'])
W('games','/ɡeɪmz/','游戏、比赛〔复数〕；运动会；花招；game 的复数等',
 '有规则、有参与者的一场场活动可以叫 games。把本来应当认真、坦诚的事当成博弈，play games 就可能是在说耍花招。',
 'game 已有 e，加 s；/m/ 后读 /z/。古英语 gamen 有欢乐、娱乐义，后来发展为游戏、比赛等；games 是现代常见复数。',
 [['古英语 gamen → game','娱乐、欢乐 → 游戏、比赛'],['game + -s → games','多场游戏、比赛；另有花招等固定引申']],
 'board games 桌游；video games 电子游戏；ball games 球类运动；the Olympic Games 奥林匹克运动会；play games with someone 可说耍手段、故意不坦诚。',
 'win two games；games for children。','game 说野味、猎物时常是集合或不可数用法，如 wild game；不能把 games 一概拿来数猎物。sports 是运动类别，games 也能数某一项运动中的具体场次。',
 ('We played two board games after dinner.','晚饭后我们玩了两种桌游。'),('Please give me a clear answer and stop playing games.','请给我一个明确的答复，别再绕来绕去了。'),sources=['https://en.wiktionary.org/wiki/games#English','https://en.wiktionary.org/wiki/game#English'])
W('members','英 /ˈmembəz/；美 /ˈmembərz/','成员、会员、委员等；member 的复数',
 '把组织想成一个整体，每位参与者都是其中一部分。members 具体是会员、议员还是队员，要看他们属于什么组织。',
 'member + -s，词尾 /z/。经法语 membre 接拉丁 membrum 肢体、身体部分；成员义用部分与整体的关系作比喻。',
 [['拉丁 membrum → 法语 membre → member','肢体、部分 → 团体的一员'],['member + -s → members','一个组织中的多位成员']],
 'team members 团队成员；family members 家庭成员；committee members 委员会成员；club members 俱乐部会员；members of staff 工作人员。',
 'new members；members of the group。','a member of the team 是团队里的一员；the members of the team 是团队成员们。成员身份不等于领导身份，members 不自动说谁负责。',
 ('All members of the group can suggest changes.','组里的所有成员都可以提出修改建议。'),('The club welcomed five new members this month.','俱乐部这个月迎来了五位新会员。'),sources=['https://en.wiktionary.org/wiki/members#English','https://en.wiktionary.org/wiki/member#English'])
W('services','英 /ˈsɜːvɪsɪz/；美 /ˈsɜːrvɪsɪz/','服务项目、服务系统；仪式、礼拜等；检修〔service 的第三人称单数〕',
 '一项项能替人办事的安排是 services：送货、交通、网络等。给机器做保养也在替它保持可用，所以 service 又能作检修的动词。',
 'service + -s，原词结尾 /s/ 后，复数词尾读 /ɪz/。service 经法语 servise 接拉丁 servitium，与 servire 服侍、效力同族。',
 [['拉丁 servitium → 古法语 servise → service','服役、服务；后来有系统、保养、仪式等分支'],['service + -s → services','多项服务、仪式；单数主语检修']],
 'public services 公共服务；emergency services 应急服务；bus services 公交线路、班次或运营服务；services a car 检修汽车。宗教语境 services 还可指礼拜仪式。',
 'online services；provides several services。','good service 常说服务质量，通常不可数；different services 是不同服务项目，可数。The garage services cars 中 services 是动词，cars 才是被检修的对象。',
 ('The library offers several free online services.','图书馆提供几项免费的线上服务。'),('The garage services our car every year.','这家修车厂每年为我们的车做保养。'),sources=['https://en.wiktionary.org/wiki/services#English','https://en.wiktionary.org/wiki/service#English'])
W('players','英 /ˈpleɪəz/；美 /ˈpleɪərz/','球员、玩家；演奏者；参与方；播放器；player 的复数',
 '谁参与这场活动，谁就可能是 player。球场上是球员，乐团里是演奏者，商业竞争中是参与方；能播放内容的机器也叫 player。',
 'player + -s，词尾 /z/。player 与 play + 人物后缀 -er 对应，接古英语 plegere 等人物形式，后随活动与技术扩展用法。',
 [['古英语游戏、参与活动词族及 plegere → player','参加活动的人 → 球员、演奏者等'],['player + -s → players','多位参与者；多台播放设备']],
 'football players 足球运动员；chess players 棋手；key players 关键参与者；major players in an industry 行业的重要参与方；music players 音乐播放器。',
 'experienced players；one of the leading players。','team players 常说愿意配合团队的人，未必真在运动队。key players 也可能是公司或组织，不能见到 players 就一律译成玩家。',
 ('The younger players learned a lot from the captain.','年轻球员从队长身上学到了很多。'),('Several small companies have become major players in this market.','几家小公司已经成为这个市场的重要参与者。'),sources=['https://en.wiktionary.org/wiki/players#English','https://en.wiktionary.org/wiki/player#English'])
W('students','英 /ˈstjuːdənts/；美 /ˈstuːdənts/','学生；学习者、研究者；student 的复数',
 '正在认真学习、研究的人是 student。最常见是在校学生，也可以是长期钻研某个领域的人。',
 'student + -s，/t/ 后读 /s/，结尾 /nts/。拉丁 studens 是 studere 用心投入的现在分词，经古法语 estudiant 等形式进入英语，与 study 同族。',
 [['拉丁 studere → studens → 古法语 estudiant → student','用心投入 → 学习者'],['student + -s → students','多位学生、学习者']],
 'school students 在校学生；university students 大学生；international students 国际学生；students of history 学习、研究历史的人。',
 'a group of students；students in the class。','pupils 常说中小学生，students 范围更广；students of a subject 有时指认真研究该领域的人，不能仅凭这个词判断年龄或学历。',
 ('The students compared their answers in pairs.','学生们两人一组比较答案。'),('The museum welcomes students of local history.','这家博物馆欢迎研究当地历史的人来访。'),sources=['https://en.wiktionary.org/wiki/students#English','https://en.wiktionary.org/wiki/student#English'])
W('points','/pɔɪnts/','点、尖端、地点；要点、分数；指向〔point 的第三人称单数〕',
 '一个小点能标出位置，也能标出讨论里值得抓住的地方；计分时每一点又成为一分。作动词时，是把方向指给人看。',
 'point + -s，/t/ 后读 /s/。英语名词合并法语 point 小点与 pointe 尖端等路线，都接拉丁 pungere 刺、戳的 punct- 词族。',
 [['拉丁 punctum／puncta → 法语 point／pointe → point','刺出的点、尖端 → 位置、要点、分数等'],['point + -s → points','多个点、分数等；单数主语指向']],
 'main points 要点；scored ten points 得了十分；points of view 看法；points to ... 指向、提示……；points out ... 指出……。',
 'three key points；points in the same direction。','points to a problem 是指向、提示一个问题；points out a problem 是明确指出问题。前者给出线索，后者把问题说出来。',
 ('Write down the three main points of the talk.','记下这次讲话的三个要点。'),('The sign points towards the nearest exit.','标牌指向最近的出口。'),('Our team won by two points.','我们队以两分的优势获胜。'),sources=['https://en.wiktionary.org/wiki/points#English','https://en.wiktionary.org/wiki/point#English'])
W('results','/rɪˈzʌlts/','结果、成绩、成效〔复数〕；产生、导致〔result 的第三人称单数〕',
 '事情做下去，最后出现了什么，就是 results。它可以是考试分数、比赛结果，也可以是努力后看得见的成效。',
 'result + -s，/t/ 后读 /s/。上接拉丁 resultare 反弹、回响，经随之产生等义发展到英语动词 result；英语结果名词由相应动词发展。',
 [['拉丁 resultare → 英语 result 动词、名词','反弹、回响 → 随之产生；结果'],['result + -s → results','多项结果、成效；单数主语产生某后果']],
 'exam results 考试成绩；search results 搜索结果；get results 取得成效；results from ... 由……造成；results in ... 导致……。',
 'compare the results；results in a delay。','results from 后接原因，results in 后接后果：A results from B 是 B 导致 A；A results in B 是 A 导致 B。看清介词，就不会把因果方向读反。',
 ('The results will be available on Friday.','结果周五就能看到。'),('Changing the order often results in a different outcome.','改变顺序常会产生不同的结果。'),sources=['https://en.wiktionary.org/wiki/results#English','https://en.wiktionary.org/wiki/result#English'])
W('shows','英 /ʃəʊz/；美 /ʃoʊz/','演出、节目、展览〔复数〕；展示、表明、带路〔show 的第三人称单数〕',
 '让人看见，是 show 的共同画面：节目呈现给观众，图表把情况展现出来，路标把方向标出来。shows 要先看是名词还是动词。',
 'show + -s，元音后读 /z/。show 继承古英语 sceawian 看、察看一系，经中古英语形式延续，展示动作又与演出、展览等名词义相连。',
 [['古英语 sceawian → show','看、察看 → 使看见、展示'],['show 名词、动词 + -s → shows','多场演出、节目；单数主语展示、表明']],
 'TV shows 电视节目；trade shows 行业展览；shows how ... 展示如何……；shows interest 表现出兴趣；shows up 出现、到场；shows someone around 带人参观。',
 'comedy shows；shows the location。','The chart shows ... 中 shows 是单数主语的动词；The shows are ... 中 shows 是复数名词。showed 是过去式，shown 常作过去分词，shows 不表示过去。',
 ('The map shows two paths to the lake.','地图标出了两条通往湖边的路。'),('We watched several short shows at the festival.','我们在节庆活动中看了几场短演出。'),sources=['https://en.wiktionary.org/wiki/shows#English','https://en.wiktionary.org/wiki/show#English'])
W('died','/daɪd/','死了、去世了；逐渐消失、停止了；die 的过去式和过去分词',
 '生命结束是 died 的基本义；声音、火焰、希望渐渐没了，也可以沿着停止存在、停止活动的画面来理解。',
 'die 去末尾 e，加完整 -ed，读 /daɪd/，一个音节。死亡动词见中古英语 deyen 等，可能借自古诺尔斯语 deyja 等北欧形式；不接骰子名词 die 的法语路线。',
 [['中古英语 deyen 等，可能接古诺尔斯语 deyja → die','死去；具体借入关系保留不确定性'],['die 去 e + -ed → died','过去死去；声音、光等消失']],
 'died young 年轻时去世；died out 逐渐灭绝、消失；died down 逐渐减弱；the engine died 发动机熄火了。具体是完全没了还是减弱，要看整组搭配。',
 'died in the night；the noise died down。','died 是发生了死亡这个动作，dead 是已经死亡的状态。He died 是他去世了，He is dead 是他已去世；不能把两种结构直接混成 He is died。',
 ('The engine coughed twice and died.','发动机突突响了两下，就熄火了。'),('The applause slowly died down.','掌声慢慢平息了。'),sources=['https://en.wiktionary.org/wiki/died#English','https://en.wiktionary.org/wiki/die#English'])
W('killed','/kɪld/','杀死了；终止、破坏、消磨了；kill 的过去式和过去分词',
 '基本画面是让生命结束，后来也用来表达让声音、计划或等待的时间停下来。具体语境能从很严肃到口语夸张。',
 'kill + -ed，原有 ll 保留，/l/ 后词尾读 /d/。kill 接中古英语 killen、kyllen 等，较远来源有争议，不把某个推测古词当定论。',
 [['中古英语 killen／kyllen → kill','打击、杀死等，远源未定'],['kill + -ed → killed','过去杀死；使停止、破坏等引申']],
 'was killed in an accident 在事故中遇难；killed the engine 关掉发动机；killed the mood 破坏了气氛；killed time 消磨时间。',
 'killed the idea；killed half an hour。','die 通常说某人或某物自己死去，kill 通常带造成死亡或终止的对象。He died 与He was killed 的信息不同，后者有外力致死的意思。',
 ('The sudden noise killed the relaxed mood in the room.','突如其来的响声破坏了屋里轻松的气氛。'),('We killed half an hour by browsing the bookshop.','我们逛书店消磨了半个小时。'),sources=['https://en.wiktionary.org/wiki/killed#English','https://en.wiktionary.org/wiki/kill#English'])
W('happened','/ˈhæpənd/','发生了；碰巧；happen 的过去式和过去分词',
 '有件事出现了，或某个人碰巧做了某事，就可以用 happened。它本身不告诉你事情好坏，也不一定强调有人安排。',
 'happen + -ed，/n/ 后读 /d/；不双写 n。happen 通常接中古英语 hap 机缘、偶然事件与 -en 动词材料，更早形成细节有不同解释。',
 [['中古英语 hap 及相关动词材料 → happen','机缘、事件 → 发生、碰巧'],['happen + -ed → happened','过去发生；过去碰巧做了某事']],
 'What happened? 出什么事了？；happened to someone 发生在某人身上；happened to be there 碰巧在那里；happened upon ... 偶然发现……。',
 'happened last week；happened to notice。','happened 通常不及物：The accident happened，不说 was happened。What happened to the window? 问窗户怎么了；I happened to see it 是我碰巧看见了。',
 ('What happened after the meeting ended?','会议结束后发生了什么？'),('I happened to find the missing key in an old coat.','我碰巧在一件旧外套里找到了丢失的钥匙。'),sources=['https://en.wiktionary.org/wiki/happened#English','https://en.wiktionary.org/wiki/happen#English'])
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_wb',ROOTS,WORDS)
 extend_lessons()
