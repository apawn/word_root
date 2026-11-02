"""Fit: suitability, fitness, installation and the separate fitful branch."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
F=[['中古英语 fit 适合、相称相关形式 → 现代 fit','合适、相配；更远来历不确定'],['现代适合词族','大小相合、适宜 → 身体状态良好；装配'],['另一路名词 fit','突然一阵、发作；来源也不明确，fitful 接这一路']]
W('fit','/fɪt/','合适；合身；健康强健的；装上；另有一阵、发作义',
 '大小、条件或状态刚好对得上：衣服合身，人能胜任任务，零件装得进去。',
 '适合义在中古英语有相关形式，更远来源有争论，不把部署军队等某个推测讲成确定起点。名词 fit 一阵、发作走另一路不明词源，不能说是适合过头。',F,
 'The shoes fit 鞋合脚，fit for purpose 适合用途，keep fit 保持身体状态；fit a shelf 安装搁板。a fit of laughter 一阵大笑属于另一名词分支。',
 'fit for；fit into；keep fit；a fit of laughter。',
 'fit 衣服尺寸合适，suit 可说颜色、风格适合；This coat fits me but the colour does not suit me。',
 ('The lid does not fit this box.','这个盖子和这个盒子不配套。'),('She goes swimming to keep fit.','她靠游泳保持身体状态。'))
W('fitness','/ˈfɪtnəs/','身体健康、体能；适合程度',
 '日常多说身体能不能有力、持久地活动；更广也能说某人、某物是否适合特定用途。',
 'fit + -ness，把合适或身体状态良好这项性质变成名词。体育、健康语境特别常见，但不是唯一用法。',F[:2]+[['fit + -ness → fitness','身体状态好、适合 → 体能、适合程度']],
 'physical fitness 身体素质，a fitness class 健身课；fitness for a role 对某角色的适合程度。',
 'physical fitness；fitness training；a fitness class；fitness for。',
 'fitness 侧重身体活动能力或适合程度，health 健康范围更广；不是看起来健壮就能从单词推出所有身体指标正常。',
 ('The course aims to improve general fitness.','课程旨在提高整体体能。'),('The committee questioned his fitness for the role.','委员会质疑他是否适合这个职位。'))
W('fitter','英 /ˈfɪtə/；美 /ˈfɪtər/','更强健、更合适的；装配工',
 '可能是在比较身体状态，也可能是负责安装、装配的人；同一个结尾，要看句子结构。',
 'fit 双写 t + -er：比较级表示更强健、更合适，职业名词则表示安装配件的人。两种 -er 功能不同。',F[:2]+[['fit + -er → fitter','比较级更适合、强健；另为装配工']],
 'feel fitter 感到体能更好，a kitchen fitter 厨房设备安装工，a pipe fitter 管道安装工。',
 'feel fitter；get fitter；a kitchen fitter；a pipe fitter。',
 'She is fitter 中是比较级，She is a fitter 中 a 后面是职业名词；冠词让结构很清楚。',
 ('I feel fitter after cycling to work for a month.','骑车上班一个月后，我感觉体能更好了。'),('The kitchen fitter installed the new cabinets.','厨房安装工装好了新橱柜。'))
W('unfit','/ʌnˈfɪt/','不适合的；不健康、体能差的',
 '达不到眼下需要的条件：可能是身体不适合某任务，也可能是物品不适用。',
 'un- 不 + fit。按对象和搭配取不适合、身体状态差等义，不是只说衣服不合身。',F[:2]+[['un- + fit → unfit','适合、身体状态好的反面']],
 'unfit for use 不适于使用，unfit to drive 不适合开车，physically unfit 体能差；判定什么任务由上下文说明。',
 'unfit for use；unfit to drive；physically unfit。',
 'unfit for this task 是对某任务不适合，不自动是否定这个人所有能力；ill 生病与 unfit 体能差也不完全一样。',
 ('The damaged building was declared unfit for use.','这座受损建筑被认定不适合使用。'),('After months without exercise, he felt physically unfit.','几个月没运动后，他觉得自己体能很差。'))
W('fitting','/ˈfɪtɪŋ/','合宜的；安装配件；试衣',
 '三种常见场景：表达与场合相称，零件装配得上，或试穿衣服看尺寸对不对。',
 'fit 双写 t + -ing，形成动作名词、分词与形容词。常用名词 fittings 多指安装在房间、设备等上的配件。',F[:2]+[['fit + -ing → fitting','适合、装配 → 合宜；配件；试衣']],
 'a fitting tribute 恰如其分的致敬，a dress fitting 试礼服，light fittings 灯具配件。',
 'a fitting tribute；a dress fitting；light fittings。',
 'fitting 作合宜形容词不等于 fitful 断断续续；fittings 配件也不同于 clothes outfit 一身穿搭。',
 ('The concert was a fitting tribute to the composer.','这场音乐会是对作曲家恰如其分的致敬。'),('She has a dress fitting on Friday.','她周五要去试礼服、调整尺寸。'))
W('refit','动词 /ˌriːˈfɪt/；名词常 /ˈriːfɪt/','重新装备；整修、改装',
 '原来的船、房间或设备还在，把里面的部件、装备重新配好。',
 're- 重新 + fit 安装、装备。动词也可接成名词，表示一次改装、整修工作。',F[:2]+[['re- + fit → refit','重新安装装备 → 整修、改装']],
 'refit a ship 改装船，refit a kitchen 重新安装厨房设备；undergo a refit 接受整修。',
 'refit a ship；a kitchen refit；undergo a refit。',
 'refit 强调重新装备或内装，repair 修理损坏处；一次 refit 可能包含 repair，但不只修破损。',
 ('The ship returned to port for a major refit.','船返回港口接受大规模改装。'),('They refitted the kitchen with new cabinets.','他们给厨房换装了新橱柜。'))
W('befit','/bɪˈfɪt/','与……相称；适合',
 '某种行为、安排，配得上某人的身份、场合或事情的重要性。语气比 fit 正式。',
 'be- + fit，形成与……相称的及物动词。现代常见 as befits... 正如……应有的样子。',F[:2]+[['be- + fit → befit','与对象相称、适宜']],
 'as befits a champion 正如冠军应有的样子；behaviour that befits the occasion 与场合相称的行为。直接接宾语，不必仿 fit for 加 for。',
 'as befits；befit the occasion；befit someone’s status。',
 'befit 更偏场合、身份相称，fit 可直接说尺寸合身；The hat fits 不必改成帽子 befits 头。',
 ('She spoke with the confidence that befits an experienced leader.','她讲话时展现出一位资深领导者应有的自信。'),('The hall was decorated as befits a grand celebration.','大厅装点得与盛大庆典相称。'))
W('fitful','/ˈfɪtfəl/','断断续续的；一阵阵的',
 '睡一会儿醒一会儿，风吹一阵停一阵；重点是不连续、不稳定。',
 'fit 一阵、发作 + -ful，接另一路名词 fit，不是 fit 合适加后缀。成词后表示一阵一阵出现。',F[2:]+[['fit（一阵）+ -ful → fitful','多次阵发 → 断续、不稳定的']],
 'fitful sleep 断续不安的睡眠，fitful progress 时断时续的进展；通常不是在夸状态很适合。',
 'fitful sleep；fitful progress；a fitful breeze。',
 'fitful 断续，fitting 合宜；睡得 fitfully 是时睡时醒，不是十分健康地睡。',
 ('He managed only a few hours of fitful sleep.','他只断断续续睡了几个小时。'),('The project made fitful progress during the winter.','项目整个冬天进展时断时续。'))
R('B2861','合适、强健、装配；另源阵发','FIT：对得上条件；另一路 fitful 说一阵一阵','先看衣服合身、物件合用和身体状态，再按安装装备读 fitting、refit；fitful 单列阵发词源。',
 '适合义更远来源不明，发作、一阵义也不确定；不能把未知处编成确定故事。fitness 与 fitful 的 fit 在这里不走同一条语义路。',
 'fit → fitness、fitter、unfit、fitting、befit、refit；共享 outfit、misfit、retrofit、crossfit；名词 fit 阵发 → fitful。',
 [['基本性质与比较、否定','fit · fitness · fitter · unfit'],['合宜与安装装备','fitting · befit · refit · retrofit · outfit · misfit'],['特定运动词','crossfit'],['另源的一阵阵','fitful']],
 'fitter 比较级与职业名分开；fitting 合宜，fitful 断续；fit 与 suit 衣物搭配看尺寸与风格。',
 'The fitter checked whether the new shelf would fit.\n\n安装工检查新搁板是否装得下。',
 'fit fitness fitter unfit fitting befit refit retrofit outfit misfit crossfit fitful')
if __name__=='__main__':save('continuation_20261029_dy',ROOTS,WORDS)
