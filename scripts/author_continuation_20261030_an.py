"""Statement, owner and minute: useful contrasts rather than dictionary lists."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
ST=[['state〔陈述〕+ -ment → statement','把事情说出来的陈述、说法'],['under-/over-/re- 与 statement 组合','说轻、说过头、重新表达']]
W('understatement','英 /ˌʌndəˈsteɪtmənt/；美 /ˌʌndərˈsteɪtmənt/','轻描淡写；保守、低于实际的说法',
 '已经累得站不住，却说有点累；说出口的分量比真实情况轻。',
 '可按 under- 不足 + statement 分析，也对应 understate + -ment。它既可指修辞上的有意说轻，也可指实际陈述不足，不能一律当故意撒谎。',ST+[['under- + statement → understatement','说得低于实际；轻描淡写']],
 'To say I was tired would be an understatement. 说我累了都算轻的。常用 understatement 强调实际程度远超那个形容词。',
 'a huge understatement；a masterpiece of understatement；would be an understatement。',
 'understatement 说轻；overstatement 说过头。underestimate 是估计偏低，未必已经向别人作了陈述。',
 ('Calling the journey difficult would be an understatement.','说这趟旅程艰难，都算轻描淡写。'),('Her calm description was a remarkable piece of understatement.','她平静的描述把事情说得格外轻。'))
W('overstatement','英 /ˌəʊvəˈsteɪtmənt/；美 /ˌoʊvərˈsteɪtmənt/','夸大；超过实际的陈述',
 '东西有点好，却说成全世界最好；陈述往实际之上抬得过高。',
 'overstate + -ment，也可看成 over- 过量 + statement。名词指夸大这个做法或具体那句话。',ST+[['overstate + -ment／over- + statement → overstatement','说过头、超过实际的表述']],
 'an overstatement of the benefits 夸大好处，without overstatement 不夸张地说。可谈数字、效果，也可谈人的评价。',
 'an overstatement of；a serious overstatement；without overstatement。',
 'overstatement 是说过头；overestimate 是估计偏高。一个估计如果被公开说出，也可能同时属于两者。',
 ('Calling it a complete failure is an overstatement.','说它彻底失败，有些夸大。'),('The report contains an overstatement of the likely benefits.','报告夸大了可能带来的好处。'))
W('restatement','/ˌriːˈsteɪtmənt/','重新表述；重申；重新编报的陈述',
 '意思再说一遍，可能换个更清楚的表达，也可能更正之前写下的内容。',
 're- 再次 + statement，也对应 restate + -ment。re- 说明重新做，不自动保证逐字重复或内容完全不变。',ST+[['re- + statement → restatement','再次陈述；重述、重申或更正后陈述']],
 'a restatement of the main idea 重新表述主旨，a restatement of policy 重申政策；财务语境也可指重编、更正报表。',
 'a restatement of；a clear restatement；a financial restatement。',
 'restatement 可换说法或更正，quotation 原话引用强调保留原来措辞。重述主旨不必把每个字照抄。',
 ('The final paragraph is a clear restatement of the main idea.','最后一段清楚地重述了主旨。'),('The company announced a restatement of its earlier figures.','公司宣布重新编报此前公布的数据。'))
R('B2917','陈述如何改变分量：说轻、说重、再说','STATEMENT：说出来的内容，可以不足、过量或再表述','先读已有 statement，再连续对照 understatement、overstatement、restatement。',
 '这一页延伸既有 state 陈述词族。前缀说明表述与实际的关系，不是把每个词重新拆成站立来死译。',
 'state + -ment；under-/over-/re- + statement；也有相应动词 + -ment 的分析。',
 [['基本陈述','statement'],['分量与重复','understatement · overstatement · restatement']],
 'understatement 说轻、overstatement 夸大；restatement 重述不必逐字照抄；estimate 估计与 state 陈述角度不同。',
 'Calling the delay inconvenient was an understatement, so she gave a clearer restatement.\n\n说延误只是不方便太轻了，于是她重新作了更清楚的表述。',
 'statement understatement overstatement restatement')
OW=[['古英语 āgnere → 中古英语 ouner → owner','拥有者'],['现代 own 与 owner 相互对应','own 拥有；owner 拥有者，旧词形成关系比表面拆分复杂']]
W('owner','英 /ˈəʊnə/；美 /ˈoʊnər/','所有者；主人；业主',
 '这件东西归谁？答案里那个人或机构就是 owner，不一定是现在拿着它、用着它的人。',
 '接中古英语 ouner、古英语 āgnere 等拥有者词。今天可直观对应 own + -er，但 own 动词历史还涉及旧形容词派生及后来的 owner 逆构影响，不宜把现代组合当唯一诞生过程。',OW,
 'the owner of the house 房屋所有者，a business owner 企业主，the previous owner 前任所有者。',
 'the owner of；a business owner；the previous owner；a pet owner。',
 'owner 是东西归谁，user 是谁使用，tenant 是租客，manager 是管理者。四种角色可以由不同人担任。',
 ('The owner of the café lives upstairs.','咖啡馆老板住在楼上。'),('Please return the keys to their owner.','请把钥匙还给它们的主人。'),sources=['https://www.oxfordlearnersdictionaries.com/definition/english/own_2','https://en.wiktionary.org/wiki/owner#English'])
W('ownership','英 /ˈəʊnəʃɪp/；美 /ˈoʊnərʃɪp/','所有权；拥有状态；对事情负责、主动承担',
 'owner 是那个人，ownership 是东西归他的这种关系；工作里也借来讲把事情接住、负责到底。',
 'owner + -ship，-ship 表身份、状态或关系，这里与船 ship 无关。责任义是对控制、承担的引申，不表示员工私自占有项目。',OW+[['owner + -ship → ownership','拥有关系；引申承担责任、掌控事情']],
 'transfer ownership 转移所有权，public ownership 公有，take ownership of a problem 主动负责处理问题。',
 'transfer ownership；in private ownership；take ownership of。',
 'ownership 拥有关系，possession 可只说实际占有、持有；take ownership 在团队里也常是负责，不一定取得财产权。',
 ('Ownership of the building changed last year.','这栋楼去年换了所有者。'),('She took ownership of the problem and kept the team informed.','她主动接手处理问题，并持续向团队说明进展。'))
R('B3925','拥有者与拥有关系；责任义的延伸','OWNER：东西归谁；OWNERSHIP：归属关系或主动负责','owner → ownership；homeowner、landowner、shipowner 按拥有对象分组共享。',
 '现代 own + -er 的认形很有用，历史却有旧拥有者词及动词再形成的关系，正文分开说明。',
 'owner 的历史本族词；owner + -ship；home/land/ship + owner。',
 [['人和关系','owner · ownership'],['拥有的对象','homeowner · landowner · shipowner']],
 'owner/user/tenant/manager 分角色；ownership/possession 分归属与持有；take ownership 可说负责。',
 'The new owner took ownership of the problem on the first day.\n\n新主人第一天就主动接手处理了这个问题。',
 'owner ownership homeowner landowner shipowner')
MI=[['拉丁 minuere → minūtus','使变小 → 小的、细小的'],['中世纪拉丁 minūta → 法语、英语 minute','小部分 → 分钟；短记等支线'],['拉丁 minūtus → 英语 minute〔形容词〕','微小、细致；与分钟读音不同']]
W('minute','分钟 /ˈmɪnɪt/；微小的：英 /maɪˈnjuːt/、美 /maɪˈnuːt/','分钟；片刻；会议记录〔复数〕；微小、细致的',
 '把一小时细分，得到分钟；把物体或观察分得很细，则是微小、细致。拼写一样，常用读法分两路。',
 '同接拉丁 minūtus 小的，来自 minuere 使变小。时间名词经中世纪拉丁 minūta、法语等传入；形容词另借拉丁。会议 minutes 接短记、摘要支线，不能说成记录每一分钟才得名。',MI,
 'ten minutes 十分钟，Wait a minute. 等一下；take the minutes 作会议记录。minute details 细微细节，minute quantities 极少量。',
 'in a minute；take the minutes；minute details；minute quantities。',
 '分钟重音在前、/ˈmɪnɪt/；微小的重音在后。两种意思同远源但不同借入与读音，不把时间读音套到形容词上。',
 ('Could you wait a minute while I find the file?','你能等一下，让我找找文件吗？'),('The camera recorded minute changes in the surface.','摄像机记录下表面极细微的变化。'),sources=['https://www.etymonline.com/word/minute','https://www.etymonline.com/word/minutes','https://en.wiktionary.org/wiki/minute#English'])
W('minutely','细致地：英 /maɪˈnjuːtli/、美 /maɪˈnuːtli/；每分钟 /ˈmɪnɪtli/','细致入微地；每分钟的、每分钟地〔较少用〕',
 '把注意力放到很小的地方，一点一点检查，就是 minutely；另一路才接分钟这个时间单位。',
 'minute + -ly，来源词取微小、细致义时形成常见副词；取时间名词义时可构成每分钟的等用法，发音随词基分开。',MI+[['minute + -ly → minutely','细致入微地；另有每分钟用法']],
 'examine minutely 细查，describe minutely 描述得很细。表示每分钟通常直接说 every minute 更直观，先熟悉细致这个常见阅读义。',
 'examine minutely；study minutely；describe minutely。',
 'minutely 细致地不同于 briefly 简短地；写得短也可能很细，二者不在同一条长短尺度上。注意别按分钟的读法读细查。',
 ('The engineer examined the crack minutely.','工程师极细致地检查了裂缝。'),('The room was minutely described in her notes.','她在笔记里极详细地描写了房间。'))
R('B2424','小部分、分钟与细微细致；同形分音','MINUTE：时间细分为分钟，观察细到微小处','minute 先分两种读音与词性，再接 minutely；会议记录放在短记支线。',
 '同一个拉丁小的来源走不同借入支线，不把分钟、微小、会议记录编成单线依次演变。',
 '拉丁 minuere → minūtus；名词 minūta 的时间、短记支线；minute + -ly。',
 [['时间、短记与微小〔分音〕','minute'],['方式〔也分音〕','minutely']],
 'minute 分钟 /ˈmɪnɪt/，微小 /maɪˈnjuːt/；minutes 会议记录不按会议分钟数命名。',
 'She spent a minute examining the minute marks minutely.\n\n她花了一分钟，极细致地查看那些微小痕迹。',
 'minute minutely')
if __name__=='__main__':save('continuation_20261030_an',ROOTS,WORDS)
