"""Frequent forms of listening, speaking, checking, reviewing and sharing."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'B2741':dict(words=['listen','listens','listened'],label='listen → listens／listened：主动留神听',note='listen 的 t 不发音；listens 词尾 /z/，listened 词尾 /d/；与 list 清单不是现代拼接关系。'),
 'B2914':dict(words=['speak','speaks'],label='speak → speaks：说话、讲语言',note='speaks 是单数主语后的现在式，词尾 /s/；过去 spoke、分词 spoken 已另讲，不按规则加 ed。'),
 'B3378':dict(words=['check','checks','checked'],label='check → checks／checked：核查、限制与检查事项',note='check 的棋局将军称呼远接波斯 shāh 国王，核查、限制、付款等现代分支有不同使用史。'),
 'C1635':dict(words=['review','reviews','reviewed'],label='review → reviews／reviewed：回头看、评估与评论',note='review 经法语 reveue 等再看词族传入，现代 re- 加 view 可认形；reviews 可数评论，也可作动词形式。'),
 'B3341':dict(words=['share','shares','shared'],label='share → shares／shared：分出的一份与共同使用',note='share 接古英语 sċearu 部分、切分词族；shares 可数份额，shared 可说共同使用、拥有或感受。'),
 'C1252':dict(words=['save','saved'],label='save → saved：保全、保存、节省',note='save 经法语 sauver 接拉丁 salvare、salvus 保护词族；saved 在 /v/ 后读 /d/。'),
}
W('listens','/ˈlɪsənz/','听、留神听、听取；listen 的第三人称单数',
 '耳朵接到声音是听见；主动把注意力放到声音或别人的话上，是 listens。这个动作常带着认真听的意图。',
 'listen + -s，/n/ 后读 /z/；t 不发音。listen 接古英语 hlysnan 等，经中古英语 listenen、listnen 延续。',
 [['古英语 hlysnan 等 → 中古英语 listenen／listnen → listen','留神听、听取'],['listen + -s → listens','单数主语现在听、听取']],
 'listens to music 听音乐；listens carefully 认真听；listens to advice 听取建议；listens for ... 留心听某种声音是否出现。',
 'listens to the radio；listens without interrupting。','listens to someone 有 to，hears someone 直接接对象。listen for a sound 侧重留神等那个声音，listen to a sound 侧重把注意力放到已有声音上。',
 ('She listens carefully before giving an answer.','她先认真听，再作回答。'),('He listens to the radio while cooking.','他做饭时听收音机。'),sources=['https://en.wiktionary.org/wiki/listens#English','https://en.wiktionary.org/wiki/listen#English'])
W('listened','/ˈlɪsənd/','听过、听取了；listen 的过去式和过去分词',
 '当时认真把别人的话或一段声音听进去，是 listened。它说做了倾听这个动作，不必已经赞同对方。',
 'listen + -ed，/n/ 后读 /d/；原词 t 仍不发音。词基接古英语 hlysnan 等留神听词，经中古英语延续。',
 [['古英语听的词族 → listen','主动留神听、听取'],['listen + -ed → listened','过去听；完成时中的倾听']],
 'listened to the explanation 听了解释；listened in silence 安静地听；listened for footsteps 留神听脚步声。',
 'listened carefully；has listened to ...。','listened to the idea 说听了这个想法，agreed with the idea 才说赞同。倾听动作与是否接受意见，是两层不同信息。',
 ('We listened to the whole story before asking questions.','我们听完了整个故事，才开始提问。'),('She listened for the sound of the train.','她留神听火车的声音。'),sources=['https://en.wiktionary.org/wiki/listened#English','https://en.wiktionary.org/wiki/listen#English'])
W('speaks','/spiːks/','说话、发言；讲某种语言；表明、传达〔speak 的第三人称单数〕',
 '把想法用话说出来，是 speaks；一份报告、某种表现明显传达了信息，也可以借说话来表达。',
 'speak + -s，/k/ 后读 /s/。speak 继承古英语 specan，经中古英语 speken 延续，更早与 sprecan 等形式的关系有不同分析。',
 [['古英语 specan 等 → 中古英语 speken → speak','说话、讲语言、发言'],['speak + -s → speaks','单数主语现在说、讲；显出、传达']],
 'speaks English 讲英语；speaks to the group 向小组讲话；speaks clearly 说得清楚；speaks for everyone 代表大家发言；speaks volumes 很能说明问题。',
 'speaks several languages；speaks about the project。','speaks a language 后直接接语言名，speaks to someone 用 to 引出听者。says ... 常引出说了什么，speak 则更关注说话、语言能力或发言。',
 ('She speaks three languages and is learning a fourth.','她会讲三种语言，还在学第四种。'),('His careful preparation speaks volumes about his commitment.','他细致的准备足以说明他有多投入。'),sources=['https://en.wiktionary.org/wiki/speaks#English','https://en.wiktionary.org/wiki/speak#English'])
W('checks','/tʃeks/','检查、核对事项；制约；支票〔美式〕；检查、制止〔动词形式〕',
 '把事情核一遍，看是否合适，是 checks；在前面挡一下、让速度停下来，也属于 check 的限制分支。支票则是另一个固定的付款用法。',
 'check + -s，/k/ 后读 /s/。经法语 eschec 等棋局中的将军称呼传入，远接波斯 shāh 国王；核验、制约、记号、付款等现代义各有使用史。',
 [['波斯 shāh → 经中介语言的法语 eschec → 英语 check','棋局将军、制约；后有核验等分支'],['check 名词、动词 + -s → checks','多项检查、制约、支票等；单数主语核查、制止']],
 'routine checks 常规检查；checks the address 核对地址；keeps costs in check 控制费用；writes checks 开支票〔美式〕。',
 'make several checks；checks the details。','checks 在美式可说支票，英式这层常拼 cheques；普通检查在英美都写 checks。check the address 是核对地址；check on someone 是看看某人的情况。',
 ('She checks the address before sending each parcel.','她每寄一个包裹前都会核对地址。'),('We made a few final checks before opening the doors.','开门前，我们作了最后几项检查。'),sources=['https://en.wiktionary.org/wiki/checks#English','https://en.wiktionary.org/wiki/check#English'])
W('checked','/tʃekt/','检查、核对了；制止、托运了；格子图案的；check 的过去式和过去分词等',
 '把信息核过一遍，是 checked；让东西受控制、办好托运行李等，也有固定 check 用法。衣服上的 checked 则说格子图案。',
 'check + -ed，/k/ 后读 /t/。check 的棋局、制约、核验词族远接波斯 shāh；格子纹样用法还与 chequer 等形式联系，分别看现代搭配。',
 [['法语棋局相关称呼及后续英语 check；另看 chequer 图案词关系','制约、核验等；格纹分支'],['check + -ed → checked','过去检查、托运等；格子纹样的']],
 'checked the facts 核实了事实；checked the luggage 托运行李；a checked shirt 格子衬衫；checked in 办理入住、报到、值机〔看场景〕。',
 'carefully checked；checked with the organiser。','checked a bag 在出行场景可说办了托运，checked a bag for damage 则是在检查有无损坏。checked shirt 的格纹义也要靠名词场景理解。',
 ('We checked the opening times before leaving.','出发前，我们核对了开放时间。'),('He wore a blue checked shirt to the picnic.','他穿着一件蓝色格子衬衫去野餐。'),sources=['https://en.wiktionary.org/wiki/checked#English','https://en.wiktionary.org/wiki/check#English'])
W('reviews','/rɪˈvjuːz/','评论、评述；审查、评估、回顾；回顾、评估〔动词形式〕',
 '把已经做过、看到过的东西再看一遍，作判断，是 reviews。电影评论、工作评估、计划复核，都能从回头看理解。',
 'review + -s，元音后读 /z/。历史经法语 reveue 等传入，远接再看词族；现代 re- 再 + view 看是帮助认形的对应，不代替借入史。',
 [['拉丁再看相关形式 → 法语 reveue 等 → review','回看、审视 → 评论、评估'],['review 名词、动词 + -s → reviews','多篇评论、多次评估；单数主语复核、回顾']],
 'book reviews 书评；film reviews 影评；performance reviews 工作表现评估；reviews the plan 复核计划；reviews the notes 回顾、复习笔记。',
 'read the reviews；reviews the draft。','reviews 常比 comments 更系统地评价一个对象，但两者范围会重叠。review 作复习的动词常见于美式等语境，具体学习场景也会用 revise 等词。',
 ('The book received several thoughtful reviews.','这本书收到了几篇认真深入的评论。'),('She reviews the notes before each meeting.','每次开会前，她都会回顾笔记。'),sources=['https://en.wiktionary.org/wiki/reviews#English','https://en.wiktionary.org/wiki/review#English'])
W('reviewed','/rɪˈvjuːd/','回顾、审查、评估了；评论了；review 的过去式和过去分词',
 '把内容再过一遍，检查、评价或回顾，是 reviewed。审了文件、评了书、复习过笔记，都可以按场景这么说。',
 'review + -ed，元音后读 /d/。review 历史经法语 reveue 等再看词族传入，现代可借 re- 再 + view 看来理解材料。',
 [['法语 reveue 等 → 英语 review','回头审视、再看'],['review + -ed → reviewed','过去回顾、审核、评论等']],
 'reviewed the evidence 审看证据；reviewed the plan 复核计划；reviewed a book 写了书评；reviewed the notes 回顾、复习笔记。',
 'carefully reviewed；has been reviewed。','reviewed 只说经过了审看、评价，不直接说通过。approved 才明确表示认可、批准；文件可以被 reviewed 后仍需修改。',
 ('The team reviewed the plan before sending it out.','团队把计划发出去前又检查了一遍。'),('She reviewed the book for a local magazine.','她为当地一本杂志写了这本书的书评。'),sources=['https://en.wiktionary.org/wiki/reviewed#English','https://en.wiktionary.org/wiki/review#English'])
W('shares','英 /ʃeəz/；美 /ʃerz/','份额、分得的部分；股份；分享、共同拥有使用〔动词形式〕',
 '从一个整体里分出来的一份，是 share；让几个人共同拥有、使用或知道某事，又是 share 的动作。shares 在两种词性中都很常见。',
 'share 已有 e，加 s，词尾 /z/。名词接古英语 sċearu 切分、部分，与剪切词族相关；现代分享、共同使用等动词用法按对象发展。',
 [['古英语 sċearu → 中古英语 schare → share','切分、分出的部分 → 份额等'],['share 名词、动词 + -s → shares','多份份额、股份；单数主语分享、共用']],
 'equal shares 相等的份额；shares in a company 公司股份；shares a room 共用房间；shares an idea 分享想法；shares an interest 有共同兴趣。',
 'shares with a friend；shares the work。','shares a room with someone 是和某人共用房间，不一定把房间实际分割。shares an opinion 可说持有同样意见，shares an idea with ... 可说向……交流想法。',
 ('She shares an office with two other people.','她和另外两个人共用一间办公室。'),('The prize money was divided into four equal shares.','奖金被分成了四等份。'),sources=['https://en.wiktionary.org/wiki/shares#English','https://en.wiktionary.org/wiki/share#English'])
W('shared','英 /ʃeəd/；美 /ʃerd/','分享了、共同使用了；共同的、共有的；share 的过去式和过去分词',
 '几个人一起用同一个东西，或一起有同一种经历、兴趣，是 shared。它可以是动作，也可以直接形容共同的事物。',
 'share 去末尾 e，加完整 -ed，词尾 /d/。share 接古英语 sċearu 分出的部分，现代 shared 把分给、共同使用等动作转为过去或完成状态。',
 [['古英语 sċearu 等 → share','一份、分给；共同使用'],['share 去 e + -ed → shared','过去分享、共用；共同拥有、经历的']],
 'shared a meal 一起吃了饭；a shared room 共用房间；shared interests 共同兴趣；a shared experience 共同经历；shared responsibility 共同责任。',
 'shared with the team；a shared space。','shared 可以是大家共同拥有或经历，不只是在网上转发。shared interests 说兴趣相同，不意味着一个人把兴趣送给另一个人。',
 ('We shared a table with another family.','我们和另一家人共用了一张桌子。'),('Their shared interest in music helped them become friends.','对音乐的共同兴趣让他们成了朋友。'),sources=['https://en.wiktionary.org/wiki/shared#English','https://en.wiktionary.org/wiki/share#English'])
W('saved','/seɪvd/','救了、保全了；保存了；节省了；save 的过去式和过去分词',
 '把人或东西保住，不让它失去；把钱、时间留住，不多耗费，都能用 saved。电脑里的文件被保留下来，也叫 saved。',
 'save 去末尾 e，加完整 -ed，/v/ 后读 /d/。经法语 sauver 接晚期拉丁 salvare 使安全、保全，关联 salvus 安然无恙；与 safe 是同源相关借入形式。',
 [['拉丁 salvus → salvare → 法语 sauver → save','安然无恙 → 使安全、保全'],['save 去 e + -ed → saved','过去救回、保留、保存、节省等']],
 'saved a file 保存文件；saved time 节省时间；saved a seat 留了座位；saved money 存了钱、节省了钱〔看场景〕；saved someone from ... 使某人免于……。',
 'safely saved；saved for later。','saved money 可能是把钱存下，也可能是少花了钱，靠上下文判断。saved a seat 通常是替人留座位；saved a file 是把文件保留下来，具体保全什么由对象交代。',
 ('I saved the document before shutting down the computer.','关电脑前，我保存了文档。'),('The new route saved us nearly half an hour.','新路线让我们省了差不多半个小时。'),sources=['https://en.wiktionary.org/wiki/saved#English','https://en.wiktionary.org/wiki/save#English'])
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_xf',ROOTS,WORDS)
 extend_lessons()
