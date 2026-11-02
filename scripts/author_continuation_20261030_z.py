"""Gun: common reading vocabulary and transparent compounds."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
GU=[['中古英语 gunne、gonne','战械、火炮；更早可能与人名 Gunilda 等相关，未完全确定'],['现代 gun','枪炮；按类似外形或作用命名的工具、设备']]
def H(f,m):return GU+[[f,m]]
W('gun','/ɡʌn/','枪；炮；枪状工具；给发动机加速〔口语动词〕',
 '日常泛指枪，军事、历史里也可说炮；喷胶、喷漆等工具因外形和工作方式，也可能带 gun。',
 '接中古英语 gunne、gonne，早期指战械、火炮。可能来自用于战械昵称的女性人名，也有别的来源解释，不把一种猜测当定论。',GU,
 'a gun in a museum 博物馆里的枪炮，a glue gun 胶枪，a starting gun 发令枪；jump the gun 比喻抢先行动、操之过急。',
 'a starting gun；a glue gun；jump the gun；under the gun。',
 'gun 的范围比 pistol 手枪宽；a glue gun 在工艺场景指工具。jump the gun 来自发令背景，不是字面跳过一支枪。',
 ('The museum displays guns from several different periods.','博物馆展示几个不同时期的枪炮。'),('We jumped the gun by announcing the result too early.','我们太早公布结果，操之过急了。'),sources=['https://www.etymonline.com/word/gun','https://en.wiktionary.org/wiki/gun#English'])
W('gunner','英 /ˈɡʌnə/；美 /ˈɡʌnər/','炮手；机枪等武器操作员',
 '按负责的工作称呼人，尤其是在一组人员里负责火炮、机枪等的人。',
 'gun + -er，中古英语已有相应人物名称；双写 n。gun 在这里可指炮等，并非只指手枪。',H('gun + -er → gunner','操作枪炮等设备的人'),
 'an army gunner 炮兵，a naval gunner 海军炮手。具体军衔和岗位名称按报道或历史背景理解。',
 'an army gunner；a naval gunner；the ship’s gunner。',
 'gunner 侧重操作岗位，gunman 更泛指持枪的人，常出现在事件报道中；两者不是固定互换。',
 ('His grandfather had served as a naval gunner.','他祖父曾担任海军炮手。'),('The memoir describes the life of a young gunner.','回忆录描写了一名年轻炮手的生活。'))
W('gunman','/ˈɡʌnmən/','持枪者；枪手',
 '事件报道把一个携枪、用枪的人按手里的武器称呼，常见于袭击或抢劫新闻。',
 'gun + man，末部 man 弱读 /mən/，复数 gunmen。词通常带具体事件色彩，单凭词形不能推定所有持枪者的身份。',H('gun + man → gunman','持枪者，尤新闻中的枪手'),
 'an armed gunman 持枪者，a lone gunman 单独行动的枪手，identify the gunman 识别枪手身份。',
 'a lone gunman；identify the gunman；an armed gunman。',
 'gunman 通常按持枪行为称呼，gunner 常按军事岗位称呼；前者复数 gunmen，后者 gunners。',
 ('The witness described the gunman’s clothing.','目击者描述了枪手的衣着。'),('The police said a lone gunman had entered the bank.','警方说，一名枪手独自进入了银行。'))
W('gunpowder','英 /ˈɡʌnpaʊdə/；美 /ˈɡʌnpaʊdər/','火药',
 '历史上与枪炮、烟火密切相关的一种火药材料，名字按用途叫枪炮之粉。',
 'gun + powder 粉末，现代固定为火药名称。不是任意粉末都能因放在枪旁就叫 gunpowder。',H('gun + powder → gunpowder','用于枪炮等的火药名称'),
 'the history of gunpowder 火药史，gunpowder technology 火药技术这一历史研究主题；通常不可数。',
 'the history of gunpowder；gunpowder technology；the introduction of gunpowder。',
 'powder 粉末范围很广，gunpowder 是特定材料名称；现代不同发射药名称也不能全按字面混为一种。',
 ('The exhibition traces the history of gunpowder.','展览追溯火药的历史。'),('The book discusses how gunpowder changed warfare.','书中讨论火药怎样改变战争。'))
W('gunpoint','/ˈɡʌnpɔɪnt/','枪口；枪口威胁〔多用于 at gunpoint〕',
 '人在枪口威胁下，被迫照别人说的做；最常用的是整个短语 at gunpoint。',
 'gun + point，字面枪口所指位置，固定短语扩展为以枪威胁的强迫。',H('gun + point → gunpoint','枪口所指 → 持枪胁迫'),
 'be held at gunpoint 被持枪劫持，be robbed at gunpoint 遭持枪抢劫；它讲强迫方式，不是普通指向。',
 'at gunpoint；be held at gunpoint；be robbed at gunpoint。',
 'at gunpoint 是固定搭配，通常不写 at a gunpoint 来表达被枪威胁；point 单独还有点、观点等其他义。',
 ('The cashier was held at gunpoint.','收银员遭持枪劫持。'),('The report said the driver had been forced out at gunpoint.','报道称司机被枪口威逼下车。'))
W('gunboat','英 /ˈɡʌnbəʊt/；美 /ˈɡʌnboʊt/','炮艇',
 '以搭载火炮等武器为特征的一类较小军用船，历史资料中常见。',
 'gun + boat，按装备与船型命名。gunboat diplomacy 又借炮艇威胁来形容以军事压力施压的外交。',H('gun + boat → gunboat','装备火炮的小型军用船 → 炮艇外交比喻'),
 'a naval gunboat 海军炮艇，gunboat diplomacy 炮舰外交、武力恫吓式外交。',
 'a naval gunboat；a river gunboat；gunboat diplomacy。',
 'gunboat 是船，gunship 在现代报道里也常是武装直升机或飞机；看到 ship 不一定只想海船。',
 ('A restored gunboat is moored beside the museum.','一艘修复的炮艇停泊在博物馆旁。'),('The chapter examines the history of gunboat diplomacy.','这一章研究炮舰外交的历史。'))
W('gunsmith','/ˈɡʌnsmɪθ/','枪械工匠；枪械制造、维修人员',
 'smith 是工匠，前面补上 gun，说明专门从事哪类器物的制造、维修。',
 'gun + smith，smith 在组合词里指从事相应金属或器物工作的工匠。并不是姓 Smith 的人都做这个行业。',H('gun + smith → gunsmith','制造、维修枪械的专业工匠'),
 'a gunsmith’s workshop 枪械工匠作坊，a skilled gunsmith 熟练枪械工。历史行业介绍中常见。',
 'a gunsmith’s workshop；a skilled gunsmith；a local gunsmith。',
 'gunsmith 说专业工匠，gunman 说持枪者，gunner 说操作岗位；三个词的后部决定角色。',
 ('The museum has recreated a gunsmith’s workshop.','博物馆复原了一间枪械工匠作坊。'),('The document names the local gunsmith who owned the building.','文件写出了曾拥有这座建筑的本地枪械工匠姓名。'))
R('B2711','枪炮与相关人物、材料、场景','GUN：枪炮名，后部说明人、物或场景','先 gun，再 gunner、gunman、gunsmith 区分角色；接火药、枪口、炮艇，已有常用枪类与报道词共享。',
 'gun 由中古英语战械名延续，更早人名来源等说法保留可能性。这里集中日常、历史和新闻阅读词，不扩展冷门枪型。',
 'gun + -er/man/smith/powder/point/boat；gun + fire/shot/fight/ship/play；hand + gun、shot + gun。',
 [['基本物与人物','gun · gunner · gunman · gunsmith'],['材料、场景与船机','gunpowder · gunpoint · gunboat · gunship'],['已有枪类和事件词','handgun · shotgun · gunfire · gunshot · gunfight · gunplay']],
 'gunner 岗位、gunman 持枪者、gunsmith 工匠；at gunpoint 整体记；gunship 也可飞机。',
 'The museum compares a gunboat with the aircraft called a gunship.\n\n博物馆对比炮艇与同样用 gunship 称呼的武装飞机。',
 'gun gunner gunman gunsmith gunpowder gunpoint gunboat gunship handgun shotgun gunfire gunshot gunfight gunplay')
if __name__=='__main__':save('continuation_20261030_z',ROOTS,WORDS)
