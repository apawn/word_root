"""Sleep states and training roles."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
S=[['古英语 slēpan、slǣp → 中古英语 slepen、slepe','睡觉；睡眠'],['现代 sleep','动作、睡眠状态 → 困意、睡眠者和相关物件']]
W('sleep','/sliːp/','睡觉；睡眠',
 '动词说睡这件事，名词说睡眠本身；也可以用 a sleep 说一次睡眠。',
 '继承古英语睡觉词族，动词、名词都古老。现代不规则变化 sleep—slept—slept，元音随形式变化。',S,
 'go to sleep 开始入睡，get some sleep 睡一会儿，sleep well 睡得好；sleep on it 是先睡一晚、之后再作决定。',
 'get some sleep；go to sleep；sleep well；sleep on it。',
 'go to bed 上床不保证已经睡着，go to sleep 才是入睡；sleep /sliːp/ 与 slip /slɪp/ 滑倒分开。',
 ('I slept badly last night.','我昨晚睡得不好。'),('It is a big decision. Let me sleep on it.','这是个大决定，让我过一晚再想想。'))
W('sleepy','/ˈsliːpi/','困倦的；安静、没多少活动的',
 '眼皮发沉、想去睡，但还没真正睡着；小镇也可以借这个感觉说安静、慢悠悠。',
 'sleep + -y，形成有睡意的形容词。sleepy town 等把人的低活动状态借给地方。',S+[['sleep + -y → sleepy','有睡意 → 困倦；安静少活动的']],
 'feel sleepy 感到困，a sleepy child 困倦的孩子，a sleepy village 安静的小村庄。',
 'feel sleepy；a sleepy child；a sleepy village。',
 'sleepy 想睡，asleep 已睡着，sleepless 没睡着或没睡够；同是 sleep 词族，阶段不同。',
 ('I felt sleepy after the long journey.','长途旅行后，我觉得很困。'),('The road led to a sleepy village by the river.','道路通向河边一个安静的小村庄。'))
W('asleep','/əˈsliːp/','睡着的',
 '已经进入睡眠，不只是觉得困。',
 '中古英语 aslepe，对应 a- 在某状态 + sleep。这里 a- 不是否定前缀，不是无睡眠。',S+[['a- + sleep → asleep','处在睡眠中 → 睡着的']],
 'fall asleep 睡着，be fast asleep 熟睡，stay asleep 保持睡眠；通常在系动词后，而非直接放普通名词前。',
 'fall asleep；fast asleep；stay asleep。',
 'an asleep child 通常不用，改 a sleeping child；The child is asleep 很自然。sleepy child 是困倦但未必睡着。',
 ('The baby fell asleep in the car.','宝宝在车里睡着了。'),('By midnight, everyone was fast asleep.','到午夜时，大家都已熟睡。'))
W('sleepless','/ˈsliːpləs/','无眠的；睡不着的',
 '该睡的时间过去了，睡眠却没来；可以描述一夜，也可以描述那个人。',
 'sleep + -less 没有，形成没有睡眠的状态形容词。常见 sleepless night。',S+[['sleep + -less → sleepless','没有睡眠 → 无眠、睡不着']],
 'a sleepless night 不眠之夜，sleepless with worry 担心得睡不着；不从单个词就诊断具体睡眠疾病。',
 'a sleepless night；sleepless with worry；sleepless hours。',
 'sleepless 没睡，sleepy 有困意；一个人熬过 sleepless night，第二天很可能 sleepy。',
 ('She spent a sleepless night worrying about the interview.','她因担心面试而一夜未眠。'),('The noise left us sleepless until dawn.','噪声让我们直到天亮都没睡着。'))
W('sleeper','英 /ˈsliːpə/；美 /ˈsliːpər/','睡觉的人；卧铺车、卧铺；枕木；意外走红的作品',
 '最直观是睡的人；也可指供人睡的卧铺。看起来没动静、后来突然成功的作品又借来叫 sleeper。',
 'sleep + -er 可解释睡者与睡眠用品等义；铁路枕木的历史还有与北欧木料词联系的解释，不把每个同形义都强说成木头在睡觉。',S+[['sleep + -er → sleeper','睡的人；与睡眠有关的设施'],['其他 sleeper 用法','意外成功者的比喻；枕木另有词源讨论']],
 'a light sleeper 容易醒的人，a heavy sleeper 睡得沉的人，a sleeper train 卧铺列车；a sleeper hit 起初不显眼后来走红的作品。',
 'a light sleeper；a heavy sleeper；a sleeper train；a sleeper hit。',
 'light sleeper 容易醒，不是体重轻的睡者；railway sleeper 是枕木，不是躺在轨道旁的人。',
 ('I am a light sleeper, so even quiet noises wake me.','我睡得浅，很小的声音也会把我吵醒。'),('We took a sleeper train to the coast.','我们乘卧铺列车去了海边。'))
W('sleepwear','英 /ˈsliːpweə/；美 /ˈsliːpwer/','睡衣；睡眠时穿的衣物',
 '专为睡觉穿的那类衣物，像商店里一个服装类别名。',
 'sleep + wear 穿着、衣物，组成集合名词。wear 在这里接衣物类构词用法，不是磨损。',S+[['sleep + wear → sleepwear','睡眠穿着 → 睡衣类']],
 'cotton sleepwear 棉质睡衣，children’s sleepwear 儿童睡衣；通常不可数，不靠加 s 说好几件。',
 'cotton sleepwear；children’s sleepwear；comfortable sleepwear。',
 'sleepwear 是大类，pyjamas、nightdress 是具体样式；不等于所有在家穿的 loungewear 家居服。',
 ('The shop sells cotton sleepwear for children.','这家店卖儿童棉质睡衣。'),('She packed comfortable sleepwear for the trip.','她为旅行装好了舒适的睡衣。'))
R('B2954','睡眠、困意、睡着与无眠','SLEEP：先判断是想睡、已睡，还是没睡','sleep 基本动作之后对照 sleepy、asleep、sleepless，再看 sleeper 人物设施和 sleepwear 衣物。',
 'sleep 是古英语继承词。asleep 的 a- 表处于状态，不是否定；sleeper 枕木的历史不全用睡觉民间故事解释。',
 'sleep → sleepy、sleeper、sleepless；a- + sleep → asleep；sleep + wear、over、walk、walker。',
 [['动作与不同状态','sleep · sleepy · asleep · sleepless'],['人物、设施与衣物','sleeper · sleepwear'],['其他常见活动','sleepover · sleepwalk · sleepwalker']],
 'sleepy 想睡，asleep 已睡着；asleep 常作表语，名词前用 sleeping；sleep—slept—slept。',
 'After a sleepless night, I felt sleepy but could not fall asleep.\n\n一夜未眠后，我很困，却还是睡不着。',
 'sleep sleepy asleep sleepless sleeper sleepwear sleepover sleepwalk sleepwalker')
T=[['拉丁 trahere 拉 → 法语 traîner、train → 英语 train','拉出、延伸；一串随行之物'],['现代 train','火车；引导、培养 → 训练与培训']]
W('trained','/treɪnd/','训练过、受过培训的',
 '不是天生就会，而是经过练习、教导，具备了某种能力。',
 'train + -ed，过去分词兼形容词，末尾读 /d/。培训义在 train 历史中接引导、培养，不是受训者乘了火车。',T+[['train + -ed → trained','培养、训练 → 已受训练的']],
 'a trained nurse 受过专业训练的护士，a trained dog 训练过的狗，a trained eye 内行的眼光。',
 'a trained professional；a trained eye；highly trained。',
 'trained 经过训练，talented 有天分；二者可同时具备。trained 不保证对所有任务都合适。',
 ('A trained guide led us through the cave.','一位受过训练的向导带我们穿过洞穴。'),('To a trained eye, the difference is obvious.','在内行眼里，区别很明显。'))
W('trainer','英 /ˈtreɪnə/；美 /ˈtreɪnər/','教练；培训师；英式运动鞋',
 '教人练习、帮助提升能力的人；英国口语里复数 trainers 也常是运动鞋。',
 'train + -er，执行训练的人或器物。鞋的用法来自训练鞋的用途，不是鞋子在给人上课。',T+[['train + -er → trainer','训练者 → 教练、培训师；训练鞋']],
 'a personal trainer 私人健身教练，a staff trainer 员工培训师；a pair of trainers 一双运动鞋。',
 'a personal trainer；a staff trainer；a pair of trainers。',
 'trainer 培训者，trainee 受训者；trainers 复数在英式可指鞋，不能所有句子都译成多个教练。',
 ('The trainer explained the new booking system.','培训师讲解了新预订系统。'),('She wore trainers for the walk.','她穿运动鞋去散步。'))
W('trainee','/ˌtreɪˈniː/','受训者；见习人员',
 '正在学岗位技能的人，身份仍处于培训、见习阶段。',
 'train + -ee，后缀表示接受训练的一方。-ee 在这里与 trainer 的 -er 形成执行方、接受方的对照。',T+[['train + -ee → trainee','接受培训的人']],
 'a trainee teacher 见习教师，a management trainee 管理培训生；a trainee 不意味着永久初学者。',
 'a trainee teacher；a trainee nurse；a management trainee。',
 'trainee 受训身份，intern 实习身份；制度安排可能重叠，但不是所有 trainee 都是学生实习。',
 ('Each trainee works with an experienced colleague.','每位受训者都与一位有经验的同事一起工作。'),('She joined the company as a management trainee.','她以管理培训生身份加入公司。'))
W('retrain','/ˌriːˈtreɪn/','重新培训；转学新职业技能',
 '原来学过一套能力，现在为了新要求再训练，或换一种职业重新学。',
 're- 再、重新 + train，可以培训别人，也可以自己转训。不是再次乘火车。',T+[['re- + train → retrain','重新培养技能 → 再培训、转训']],
 'retrain staff 重新培训员工，retrain as a teacher 转训做教师，retrain for a new career 为新职业再培训。',
 'retrain staff；retrain as；retrain for。',
 'retrain 重新学习技能，retire 退休；字形有点像，过程和意思不同。',
 ('The company retrained staff to use the new equipment.','公司重新培训员工使用新设备。'),('He decided to retrain as a teacher.','他决定重新学习技能，转行做教师。'))
W('trainable','/ˈtreɪnəbəl/','可训练的；能接受培训的',
 '有可能通过练习学会、改善；先说能够学，不是说已经学会。',
 'train + -able，构成能被训练、可以培训的形容词。对象可以是人、动物，也可以是机器学习模型。',T+[['train + -able → trainable','可以被训练的']],
 'a trainable dog 易训练的狗，trainable staff 可培养的员工；trainable parameters 可训练参数。',
 'a trainable dog；trainable skills；trainable parameters。',
 'trainable 能训练，trained 已经训练；可训练不意味着训练结果必然完美。',
 ('The breed is known for being intelligent and trainable.','这个犬种以聪明、易训练著称。'),('The model has several trainable parameters.','模型有若干可训练参数。'))
R('B2801','训练、培训与受训角色','TRAIN：引导、培养；火车名词在相关历史分支','train 已精讲，本页把 trained、trainer、trainee 紧挨着，再看 retrain 与 trainable。',
 '经法语接拉丁拉、牵引词族。训练与引导培养有关，不能解释成坐火车才能学技能；powertrain、drivetrain 为已有机械词族共享内容。',
 'train → trained、trainer、trainee、trainable；re- + train → retrain；power、drive + train。',
 [['基本词与训练结果','train · trained'],['培训双方','trainer · trainee'],['重新训练与可训练性','retrain · trainable'],['机械传动词','powertrain · drivetrain']],
 'trainer 教练，trainee 学员；trained 已训练，trainable 能训练；英式 trainers 还指运动鞋。',
 'The trainer retrained the trainees to use the new equipment.\n\n培训师重新培训学员使用新设备。',
 'train trained trainer trainee retrain trainable powertrain drivetrain')
if __name__=='__main__':save('continuation_20261029_ed',ROOTS,WORDS)
