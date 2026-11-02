"""Guess and trust: uncertainty, confidence and responsibility."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
GU=[['中古英语 gessen、gesse，可能与北欧猜测词有关','猜测、推想；具体借入关系不作定论'],['现代 guess','没有把握地作判断；也可委婉表示我想、大概']]
W('guess','/ɡes/','猜测；估计；我想、大概',
 '信息还不够，你先给出一个可能答案。日常 I guess 也可以只是把话说得不那么肯定。',
 '中古英语 gessen 等，通常联系北欧相关猜测词；具体远源不强作定论。u 在现代拼写里不单独读音，不是 /ɡwes/。',GU,
 'guess the answer 猜答案，take a guess 猜一下，I guess so 我想是吧。Guess what! 常用来引出有趣消息。',
 'guess the answer；take a guess；I guess so；Guess what!。',
 'guess 可以依据很少的信息，estimate 往往强调依据资料估算；educated guess 是有根据但仍未确定的判断。',
 ('Can you guess how old this building is?','你能猜出这栋楼有多少年了吗？'),('I guess we should leave before the traffic gets worse.','我想我们应该在交通更堵前离开。'))
W('guessing','/ˈɡesɪŋ/','猜测；正在猜的',
 '答案没公开，大家还在给出可能答案；或者故意不说，让别人一直摸不准。',
 'guess + -ing，规则构成动词形式，也用于 guessing game 等表达。保留 guess 的双 s，不再另加一个 s。',GU+[['guess + -ing → guessing','猜 → 正在猜、猜测活动']],
 'a guessing game 猜谜游戏，keep someone guessing 让人一直猜不透。后者常用于计划、去向、结果迟迟不明。',
 'a guessing game；keep someone guessing；stop guessing。',
 'guessing 指过程或动作，guesswork 更常概括靠猜来做事的方式；两者不能所有位置机械互换。',
 ('The children played a guessing game on the train.','孩子们在火车上玩猜谜游戏。'),('The manager kept us guessing about the new project.','经理一直没透露新项目的情况，让我们猜来猜去。'))
R('B3421','猜测、不确定的判断','GUESS：还不确定，先给一个可能答案','从 guess 到 guessing，再接已有 guesswork，看猜一个答案与靠猜做事的区别。',
 '中古英语已有猜测词形，可能接北欧相关形式。现代 I guess 经常弱化成我想、大概。',
 'guess → guessing；guess + work → guesswork。',
 [['基本判断与过程','guess · guessing · guesswork']],
 'guess /ɡes/ 不读出 u；I guess so 不是有把握保证；educated guess 是有根据的猜测。',
 'Stop guessing and check the timetable.\n\n别猜了，查一下时刻表吧。',
 'guess guessing guesswork')
TR=[['日耳曼语信心、支持词族 → 中古英语 trust、trost','信赖、保护；英语具体传承或北欧借入关系有争论'],['现代 trust','相信可靠 → 委托责任；另有信托、托拉斯等专门用法']]
W('trust','/trʌst/','信任；相信；托付；信托',
 '觉得对方靠得住，所以敢把事情、秘密或责任交给他。',
 '中古英语 trust、trost 属日耳曼语信心、支持词族。常见词源解释联系古诺尔斯语 traust，但具体借入或本族传承有争论，不把一条路线说死。',TR,
 'trust someone 信任某人，trust someone with a secret 把秘密托付某人；a trust 还可是按特定安排持有、管理资产的组织或法律关系。这里只帮助读词，不展开法律规则。',
 'trust someone；trust someone with；put your trust in；trust your judgement。',
 'believe someone 常是相信他这次说的话，trust someone 更偏觉得此人可靠；可能相信一句话，却仍不愿把钱托付给说话者。',
 ('I trust her to keep the information private.','我相信她会对这些信息保密。'),('You need to trust your own judgement.','你需要相信自己的判断。'))
W('trusting','/ˈtrʌstɪŋ/','信任他人的；容易相信人的',
 '把视角放在愿意相信别人的那个人；并不是在评价他自己值不值得信任。',
 'trust + -ing，动词进行形式也可成为描述性格、态度的形容词。',TR+[['trust + -ing → trusting','相信别人 → 愿意信任他人的']],
 'a trusting child 容易相信人的孩子，a trusting relationship 彼此有信任的关系，too trusting 过于轻信。',
 'a trusting nature；too trusting；a trusting relationship。',
 'trusting 相信别人，trustworthy 值得别人相信；一个人可以很轻信，但不一定可靠。',
 ('She has a warm and trusting nature.','她性格温暖，愿意相信别人。'),('He worried that he had been too trusting.','他担心自己之前太轻信别人了。'))
W('trustworthy','英 /ˈtrʌstwɜːði/；美 /ˈtrʌstwɜːrði/','值得信任的；可靠的',
 '把重要事情交给它，你有理由放心；这里重点是它配得上别人的信任。',
 'trust + worthy 值得的，组合成值得信任。worthy 读 /ˈwɜːði/ 等，th 是浊音 /ð/。',TR+[['trust + worthy → trustworthy','值得获得信任 → 可靠的']],
 'a trustworthy person 可靠的人，a trustworthy source 可信来源；也可用于系统、信息是否可靠。',
 'a trustworthy person；a trustworthy source；trustworthy information。',
 'trustworthy 说值得被信任，trusting 说愿意信任别人；不能互换方向。',
 ('We need a trustworthy source for this claim.','这个说法需要一个可信来源。'),('She proved herself to be a trustworthy colleague.','她证明了自己是个可靠的同事。'))
W('trusty','/ˈtrʌsti/','可靠、趁手的；忠实的',
 '常说用了很久、一直没掉链子的熟悉工具或伙伴，带一点亲切感。',
 'trust + -y，形成可靠、忠实的形容词。现代常见 my trusty... 这个略带亲昵的说法；另有特定名词义不在此展开。',TR+[['trust + -y → trusty','有信任基础 → 可靠、忠实的']],
 'my trusty bicycle 我的老可靠自行车，a trusty notebook 一直趁手的笔记本；用于工具时很自然。',
 'a trusty companion；my trusty bike；a trusty old notebook。',
 'trusty 比 trustworthy 更有老伙伴、老工具的亲切语感；正式评估信息来源时 trustworthy 更常见。',
 ('I took my trusty old camera on the trip.','我带着那台一直很可靠的老相机去旅行。'),('His trusty bicycle carried him to work every day.','他那辆可靠的自行车每天载着他去上班。'))
W('trustee','/trʌˈstiː/','受托人；基金会、机构等的理事',
 '别人把某项管理责任交过来，由这个人按职责替相关对象照管；不是泛指一个值得信任的朋友。',
 'trust + -ee，表示接受托付、承担相应角色的人。这里的 -ee 形成正式角色名词，现代也用于慈善、教育等机构理事。',TR+[['trust + -ee → trustee','接受托付的人 → 受托人、理事']],
 'a board of trustees 理事会，a museum trustee 博物馆理事，a trustee of a fund 基金受托人；具体权限看机构和法律安排。',
 'a board of trustees；a charity trustee；a museum trustee。',
 'trustee 是身份职责，trustworthy 是可靠这个评价；不能说一个人诚实就自动获得 trustee 身份。',
 ('She was appointed a trustee of the museum.','她被任命为博物馆理事。'),('The board of trustees approved the new education programme.','理事会批准了新的教育项目。'))
W('distrust','/dɪsˈtrʌst/','不信任；怀疑可靠性',
 '觉得可能靠不住，因此不愿轻易相信、交付或依赖。',
 'dis- 否定、相反 + trust，构成名词和动词。与 mistrust 用法大幅重叠，不硬分成一个有证据、一个绝无证据。',TR+[['dis- + trust → distrust','信任的反面 → 不信任']],
 'distrust the information 不信这些信息，distrust of authority 对权威的不信任；a deep distrust 深深的不信任。',
 'distrust of；deep distrust；distrust the source。',
 'distrust 与 mistrust 都可说不信任；dislike 是不喜欢，可能不喜欢某人却仍觉得他办事可靠。',
 ('Years of broken promises created deep distrust.','多年不兑现的承诺造成了深深的不信任。'),('She distrusted the figures in the report.','她不信任报告里的数字。'))
W('entrust','/ɪnˈtrʌst/','托付；委托保管、处理',
 '不只是心里相信，还真的把某样东西或某份责任交给对方。',
 'en- 与 trust 组合成托付动词，强调将某事交入对方负责范围。现代主要以两个固定句型记。',TR+[['en- + trust → entrust','把东西置于信任关系中 → 托付']],
 'entrust someone with something 把某事托付某人；entrust something to someone 把某物交托某人。',
 'entrust someone with；entrust something to；be entrusted with。',
 'trust 是信任，entrust 强调交付；entrust me with the keys 与 entrust the keys to me 表达同一方向。',
 ('She entrusted me with the keys to her flat.','她把公寓钥匙交给我保管。'),('The project was entrusted to an experienced team.','这个项目交给了一个有经验的团队。'))
W('trustful','/ˈtrʌstfəl/','充满信任的；信赖他人的',
 '态度里没有多少提防，带着信任看待对方；日常更常遇到近义 trusting。',
 'trust + -ful，充满信任，通常形容态度、表情或性情；不是值得被信任那个方向。',TR+[['trust + -ful → trustful','充满信任的']],
 'a trustful smile 信赖的笑容，a trustful attitude 信任的态度；学习重点是读懂，不必每次写作优先用这个较少见形式。',
 'a trustful smile；a trustful expression；a trustful attitude。',
 'trustful 与 trusting 都偏相信别人，trustworthy 则是值得别人相信；注意信任的方向。',
 ('The child gave her a trustful smile.','孩子向她露出信赖的笑容。'),('His trustful attitude surprised the suspicious guard.','他信任的态度让那位多疑的守卫感到意外。'))
R('B3427','信任、可靠与托付','TRUST：觉得靠得住，才敢交出去','先分谁在信、谁值得被信，再讲把责任交出去的 entrust 和接受职责的 trustee。',
 '属日耳曼语信心、支持词族，英语具体传承路线存在争论。现代重点是信任方向，而不是把每个后缀都翻成可信。',
 'trust → trusting、trustful；trust + worthy → trustworthy；trust + -y → trusty；dis- → distrust；en- → entrust；-ee → trustee。',
 [['核心与愿意相信','trust · trusting · trustful'],['值得相信、长期可靠','trustworthy · trusty'],['不信任','distrust · mistrust'],['交托与承担职责','entrust · trustee'],['专门社会经济用法','antitrust']],
 'trusting 愿意信人，trustworthy 值得被信；entrust 是交付，trustee 是职责名。antitrust 的 trust 接企业联合组织义，不是反对日常互信。',
 'She entrusted the records to a trustworthy colleague.\n\n她把记录托付给一位可靠的同事。',
 'trust trusting trustful trustworthy trusty distrust mistrust entrust trustee antitrust')
if __name__=='__main__':save('continuation_20261029_dr',ROOTS,WORDS)
