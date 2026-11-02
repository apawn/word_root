"""Core vocabulary and clear grammatical extensions, attached to existing roots."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'C0189':dict(words=['exceed','exceeding'],label='越过某条界限',note='拉丁 ex- 向外 + cedere 走 → excedere 越过 → exceed → exceeding。'),
 'C0395':dict(words=['exercise','exercised'],label='经拉丁完整词发展出的练习、运用词族',note='exercise 经法语、拉丁训练词族借入；较深处含 ex- 与 arcere，但原始具体语义桥接未定，不能按现代拼写硬拆成 ex + ercise。'),
 'B2858':dict(words=['filter','filtered'],label='毛毡材料经借词形成过滤名称',note='filter 经法语、中世纪拉丁 filtrum 毛毡等与材料 felt 同族；与 feel 的过去式 felt 分开。filter + -ed → filtered。'),
 'A1693':dict(words=['ammunition','ammo'],label='借词中的名词尾与截短形式',note='ammunition 经法语 la munition 的重新切分形成，更早接拉丁 munitio 防御、加固词族；ammunition → ammo 是现代截短。'),
 'A1741':dict(words=['awake','awaken','awakening','rest','resting','collect','collecting','ban','banning','rent','renting','punch','punching','lower','lowering','last','lasting','upset','upsetting'],label='常见活动形式与固定形容词',note='resting、collecting、banning、renting、punching、lowering 是相应动词形式；lasting、upsetting 常作形容词。ban、upset 的末尾辅音在相应 -ing 拼写中双写。'),
 'A1776':dict(words=['narcotic','narcotics'],label='药物名复数及固定修饰用途',note='narcotic + -s → narcotics；narcotics division 等搭配中可作类别修饰语。'),
}
W('awaken','/əˈweɪkən/','醒来、唤醒；唤起意识、兴趣等',
 '人从睡眠中醒来，也能把一个人原来没注意的想法、兴趣唤起来。awaken 把从沉睡到有意识的变化说出来。',
 '经中古英语 awaknen 等延续，接古英语 awæcnan 苏醒的词族，并与 awake、wake 的相应形式相互影响。不是近代才简单拿现代 awake 临时加 -en。',
 [['古英语 awæcnan 及相邻醒觉词族','从睡眠、沉寂进入清醒'],['中古英语 → awaken','醒来、使醒来；再引申唤起兴趣、认识']],
 'awaken from sleep 从睡眠中醒来；awaken someone 叫醒某人；awaken an interest 唤起兴趣。具体醒觉与抽象认识都可用。',
 'awaken to a possibility；awaken someone’s curiosity。','awake 常可作形容词醒着的；awaken 通常是动词。日常叫醒也常用 wake up，awaken 往往较书面。',
 ('The sound of rain awakened me.','雨声把我唤醒了。'),('The visit awakened her interest in local history.','这次参观唤起了她对当地历史的兴趣。'),sources=['https://www.etymonline.com/word/awaken','https://en.wiktionary.org/wiki/awaken#English'])
W('exceed','/ɪkˈsiːd/','超过、超出',
 '把限额、预期、人数等想成一条线：实际结果走到了线外，就是 exceed。它很适合数量、标准、界限。',
 '经中古英语、古法语 exceder 接拉丁 excedere 走出、越过，由 ex- 向外 + cedere 走构成。现代拼写保留 -ceed 这一词族形式。',
 [['拉丁 ex- + cedere → excedere','向外走 → 越过'],['法语、中古英语相应形式 → exceed','超过数量、标准、预期等界限']],
 'exceed the limit 超过限额；exceed expectations 超出预期；exceed the available space 超过可用空间。通常直接接被超出的对象。',
 'exceed a target；exceed the maximum。','exceed 本身已是超过，不通常再加 than；比较级 bigger than 的结构不能直接套成 exceed than。',
 ('The cost exceeded our original estimate.','费用超过了我们最初的估算。'),('The result exceeded everyone’s expectations.','结果超出了所有人的预期。'))
W('exceeding','/ɪkˈsiːdɪŋ/','超过、超出；exceed 的 -ing 形式',
 '看到 a bag exceeding the limit，把后面理解成“超过限额的”：它给前面的东西补上一个超线的动作、状态。',
 'exceed + -ing，保留超过界限这一词义。作为分词可进入进行结构，也可跟在名词后面作说明。',
 [['exceed 超过 + -ing','形成相应分词'],['句子中的 exceeding','正在超出；对超限对象作补充说明']],
 'vehicles exceeding the limit 超过限值的车辆；avoid exceeding the budget 避免超预算。并不是只有正在发生的动作才能用分词形式。',
 'costs exceeding the estimate；without exceeding the limit。','exceeded 是过去式、过去分词；exceeding 是 -ing 形式。选择哪一个取决于句子结构，不取决于中文都能译成超过。',
 ('We finished the project without exceeding the budget.','我们完成了项目，没有超出预算。'),('The form flags entries exceeding the character limit.','表单会标出超过字符数限制的输入。'))
W('exercise','英 /ˈeksəsaɪz/；美 /ˈeksərsaɪz/','锻炼；练习、习题；运用、行使',
 '让身体、技能或权能真正动起来。身体活动叫 exercise；一道训练技能的题是 an exercise；把判断力用起来也是 exercise。',
 '经法语 exercice 接拉丁 exercitium 训练，再接 exercere 使忙碌、操练词族。较深材料含 ex- 与 arcere，但最初字面怎样发展为使忙碌并不清楚，可靠的语义链从操练、运用开始。',
 [['拉丁 exercere、exercitium → 法语 exercice','使忙碌、操练、训练'],['英语 exercise 的名词、动词发展','练习、锻炼；把能力、权力付诸使用']],
 'get some exercise 做点运动；do an exercise 做一道练习；exercise caution 谨慎行事；exercise judgment 运用判断力。活动名与具体一次练习的可数性不同。',
 'regular exercise；a grammar exercise；exercise a right。','exercise 作一般锻炼活动通常不可数，具体练习、习题可数。动词也不只用于身体：exercise caution 不是锻炼小心。',
 ('Walking is a simple form of exercise.','步行是一种简单的锻炼方式。'),('Please complete the first grammar exercise.','请完成第一道语法练习。'),('You need to exercise judgment when choosing a source.','选择资料来源时需要运用判断力。'),sources=['https://www.etymonline.com/word/exercise','https://en.wiktionary.org/wiki/exercise#English'])
W('exercised','英 /ˈeksəsaɪzd/；美 /ˈeksərsaɪzd/','锻炼过、运用过；感到忧虑、激动的〔部分形容词用法〕',
 '普通句子里说已经锻炼、运用了；在 get exercised about something 这种表达里，则常是为某事忧心、激动或烦恼起来。',
 'exercise 去词末 e 加 -ed。exercise 早期还有使忙碌、扰动等词义，分词形容词保留为某事激动、忧虑的用法。',
 [['exercise + -ed','过去的锻炼、操练或运用'],['部分形容词搭配','被某事牵动、烦扰 → 忧虑、激动']],
 'exercised regularly 经常锻炼〔过去叙述〕；exercised caution 曾谨慎行事；get exercised about an issue 为一个问题激动、忧虑。不同宾语、搭配决定意思。',
 'exercised his judgment；become exercised about something。','exercise 的过去式不一律是锻炼过；exercised a right 是行使过权利，exercised about 则可能是另一条形容词用法。',
 ('She exercised every morning during the holiday.','她假期里每天早晨锻炼。'),('He became very exercised about the sudden change.','他为突然的变化感到很忧虑。'))
W('filter','英 /ˈfɪltə/；美 /ˈfɪltər/','过滤器；筛选器；滤镜；过滤、筛选、慢慢传入',
 '让一些东西通过，把另一些留下：水里的杂质、列表里的记录、照片里的光线，都能借这个选择通过的画面理解。',
 '经法语、中世纪拉丁 filtrum 毛毡等借入，远接日耳曼 felt 毛毡词族。早期毛毡用来过滤液体，材料名转为过滤器、过滤动作。',
 [['毛毡材料词族 → filtrum 等','能让液体通过、截留杂质的材料'],['英语 filter 名词、动词','过滤器、过滤；再扩展到信息筛选、图像滤镜']],
 'a water filter 滤水器；filter the results 筛选结果；a camera filter 相机滤镜。Light filtered through the curtains 说光线从窗帘间慢慢透进来。',
 'filter out unwanted items；a search filter。','filter 与 fill 填满不是同一拆分；这里的 -er 也不能简单按英语人物后缀解成做某事的人，它有完整借词历史。',
 ('Use the filter to show only unread messages.','用筛选功能只显示未读消息。'),('Soft light filtered through the curtains.','柔和的光从窗帘间透进来。'),sources=['https://www.etymonline.com/word/filter','https://en.wiktionary.org/wiki/filter#English'])
W('filtered','英 /ˈfɪltəd/；美 /ˈfɪltərd/','经过过滤、筛选的；加过滤镜的；filter 的过去式、过去分词',
 '原来的东西先过一道筛选或过滤，再呈现在面前。可以是水、信息，也可以是经过滤镜处理的照片。',
 'filter + -ed，由过滤动作进入已经过滤的状态形容词。filter 自身来自毛毡、过滤材料的历史借词，不按现代 fill + -er 拆。',
 [['filter 过滤、筛选 + -ed','动作完成或被执行'],['分词形容词 filtered','经过选择、处理后留下或显示的']],
 'filtered water 过滤水；filtered results 筛选后的结果；a filtered photo 加过滤镜的照片。不同对象中的处理方式不同。',
 'filtered light；a filtered view of the data。','filtered 强调经过处理，不自动说明质量一定更高。filtered results 可能只是符合指定条件，不是所有记录。',
 ('The app displayed the filtered results.','应用显示了筛选后的结果。'),('Filtered sunlight filled the room.','透过遮挡物变得柔和的阳光洒满房间。'))
W('ammunition','/ˌæmjəˈnɪʃən/','弹药；供争论、批评使用的材料',
 '具体是武器使用的弹药；比喻时，能拿来支持论点、反击批评的事实、证据，也能叫 ammunition。',
 '经法语 amunition 借入，来自 la munition 被重新切分成 l’amunition。更早接拉丁 munitio 加固、防御，曾泛说军需品，后来主要限定为弹药。',
 [['拉丁防御、加固词族 → 法语 munition','防御所需物资、军需品'],['la munition 重新切分 → ammunition','名称改变、范围收窄为弹药；再有论争材料比喻']],
 'boxes of ammunition 一箱箱弹药；ammunition for an argument 支持争论的材料。通常不可数，数箱、种类时另外加相应名词。',
 'a supply of ammunition；give critics ammunition。','ammunition 与 weapon 不同：weapon 是武器，ammunition 是弹药等相关消耗物资。比喻中则是可用来支持、攻击某观点的材料。',
 ('The museum display includes old ammunition boxes.','博物馆展品中有旧弹药箱。'),('The report gave critics fresh ammunition.','这份报告给批评者提供了新的论据。'),sources=['https://www.etymonline.com/word/ammunition','https://en.wiktionary.org/wiki/ammunition#English'])
W('ammo','英 /ˈæməʊ/；美 /ˈæmoʊ/','弹药；论争材料〔ammunition 的非正式缩短〕',
 '聊天或简短叙述里，把长长的 ammunition 缩成 ammo；基本意思仍是弹药，也能沿用论争材料的比喻。',
 'ammunition 的近代口语截短形式，保留开头并形成结尾 -o 的短词。不是另一个不同物质、不同装备名称。',
 [['ammunition → ammo','把长名称截短为口语形式'],['ammo 的具体、比喻用法','弹药；可用来支撑论点、反击的材料']],
 'some ammo 一些弹药；more ammo for the debate 更多辩论材料。通常不可数，语气比 ammunition 随意。',
 'an ammo box；give someone more ammo。','ammo 与 ammunition 的主要差别是长度、语体；不能因为少了字母就按普通可数物说 an ammo。',
 ('The label reads “ammo box”.','标签上写着“弹药箱”。'),('The new figures gave her more ammo for the debate.','新的数据给她的辩论提供了更多论据。'),sources=['https://www.etymonline.com/word/ammunition','https://en.wiktionary.org/wiki/ammo#English'])
W('resting','/ˈrestɪŋ/','休息中的；静止时的；rest 的 -ing 形式',
 '活动暂时放下，身体或物体处在休息、静止的状态。resting 可以描述此刻动作，也可以给一个状态作修饰。',
 'rest + -ing。rest 的休息义接旧英语休息、停留词族，这一支与表示剩余部分的 the rest 不必强合为同一来源。',
 [['rest 休息、停留的词族','停止活动、处于安定位置'],['rest + -ing → resting','正在休息；与休息、静止状态相关']],
 'resting on a chair 坐在椅子上休息；resting heart rate 静息心率；a resting place 休息处，也可依语境婉说安葬处。',
 'a resting animal；resting on the table。','resting 不一律说明在睡觉。The book is resting on the table 可以只是书放在桌上；sleeping 明确是睡眠。',
 ('The dog was resting in the shade.','狗正在阴凉处休息。'),('She left her hand resting on the table.','她把手搁在桌上。'))
W('collecting','/kəˈlektɪŋ/','收集、收藏；collect 的 -ing 形式',
 '把分散的东西一件件聚拢；作为爱好时，collecting 还强调按兴趣、主题持续积累。',
 'collect + -ing；collect 的较早词族接拉丁 colligere 聚集，含一起与收拢的材料。动作名词把收集这件事当活动来谈。',
 [['collect 聚集、收集','让分散对象来到一起'],['collect + -ing → collecting','正在收集；收藏活动']],
 'stamp collecting 集邮；collecting data 收集数据；collecting donations 募集捐款。活动名与后接宾语的分词结构都常见。',
 'coin collecting；a collecting hobby。','collection 常是收集成的集合、藏品，也能说收集活动；collecting 更直接指做这件事。collector 则是人或相应装置。',
 ('Coin collecting became his favourite hobby.','收藏硬币成了他最喜欢的爱好。'),('The team is collecting data from several schools.','团队正在从几所学校收集数据。'))
W('banning','/ˈbænɪŋ/','禁止、禁用；ban 的 -ing 形式',
 '把某种行为、物品划到不准的一边。banning 可以说禁止这项行为本身，也可以进入正在禁止的句子。',
 'ban + -ing，单音节词末 n 在这个拼写中双写；发音仍是一段 /n/。ban 的旧宣布、命令词族发展出禁止义。',
 [['ban 宣布禁止的词族','以命令、规则排除某行为'],['ban + -ing → banning','禁止这件事；相应动词形式']],
 'banning smoking 禁止吸烟；banning single-use items 禁用一次性用品；a policy banning something 禁止某物的政策。主词仍需要看完整句子。',
 'a rule banning ...；consider banning ...。','ban 是原形，banning 是 -ing 形式；双写 n 是拼写变化，不表示多禁止一次或程度更强。',
 ('The museum introduced a rule banning flash photography.','博物馆出台了禁止闪光灯摄影的规定。'),('The article discusses banning cars from the square.','文章讨论了禁止汽车驶入广场这件事。'))
W('renting','/ˈrentɪŋ/','租用、出租；rent 的 -ing 形式',
 '一方付钱使用，一方提供房屋、设备等。renting 的方向由 from、to 或整句角色说清楚。',
 'rent 租用、出租的动词 + -ing；这一词族接租金、收益的法语借词材料。这里不是 rend 撕裂的过去式 rent 那条来源。',
 [['rent 租的相关动词','支付或收取租金来提供使用权'],['rent + -ing → renting','正在租用、出租；租赁活动']],
 'renting a flat from someone 向某人租房；renting a room to students 把房间租给学生。from 与 to 帮你判断谁租进、谁租出。',
 'renting a car；renting out a room。','renting 与 buying 的主要区别是按约定暂时使用、并非直接买下；句中 rent 可以从不同一方的视角使用。',
 ('We are renting a flat near the station.','我们正在租住车站附近的一套公寓。'),('She is renting a room to a student.','她正把一间房租给一个学生。'))
W('punching','/ˈpʌntʃɪŋ/','挥拳、拳打；打孔；punch 的 -ing 形式',
 '拳头击中目标，或者打孔器在纸上压出孔。这里都在说动作，具体是哪一种看后面的对象。',
 'punch 动作义 + -ing。punch 的打击、钻孔等旧词义有各自相关传入背景；饮料 punch 则属于另一来源，本页不拿饮料解释动作。',
 [['punch 的打击、打孔动词用法','击中或压穿某物'],['punch + -ing → punching','拳打、打孔的过程或正在做的动作']],
 'a punching bag 拳击沙袋；punching holes 打孔；punching numbers into a keypad 把数字按进键盘。宾语会限定用法。',
 'punching a bag；punching holes in paper。','punching bag 是拿来练拳的器材；punching holes 中的 punch 则是打孔，不能每次都译成殴打。',
 ('The boxer practised on a punching bag.','拳击手对着沙袋练习。'),('She was punching holes in the sheets for the binder.','她正给纸张打孔，准备装进活页夹。'))
W('lowering','英 /ˈləʊərɪŋ/；美 /ˈloʊərɪŋ/','降低、放下；lower 的 -ing 形式',
 '把音量、数量、位置往下调：声音小一点、手放低一点，或把某个数值降下来。',
 'lower 使降低、变低 + -ing；lower 的常用动词义由 low 的比较级 lower 更低发展。这里讲 /oʊ/ 这条常用词族。',
 [['low 低 → lower 更低','比较级提供向下的程度关系'],['lower 作动词 + -ing → lowering','正在降低；降低这一过程']],
 'lowering the volume 调低音量；lowering costs 降低成本；lowering a flag 降旗。可以是具体位置，也可以是抽象数值。',
 'a way of lowering costs；slowly lowering her hand。','lowering 是动作、过程；lower 作比较级则是更低的。lower prices 可以是更低价格，lowering prices 明确在说降价动作。',
 ('She was lowering the volume on the radio.','她正在把收音机的音量调低。'),('The team found a way of lowering production costs.','团队找到了降低生产成本的方法。'))
W('lasting','英 /ˈlɑːstɪŋ/；美 /ˈlæstɪŋ/','持久的、持续很久的；last 的 -ing 形式',
 '事情过去了，影响、记忆或关系还留着。lasting 把能持续、不容易消失这个性质突出出来。',
 'last 持续 + -ing。动词 last 接古英语 laestan 持续、完成等词族；表示最后的形容词 last 有另一条历史，不把持续义强从最后一位推出来。',
 [['last 的持续动词词族','维持、继续存在'],['last + -ing → lasting','持续的；固定形容词中常说持久的']],
 'a lasting impression 持久印象；lasting peace 持久和平；a friendship lasting many years 持续多年的友谊。形容词和分词结构都可用。',
 'a lasting effect；a lasting memory。','lasting 主要说持续时间长；last 作最后的形容词说顺序。a lasting memory 是长久记忆，不是最后一段记忆。',
 ('The visit left a lasting impression on her.','这次访问给她留下了持久印象。'),('They built a lasting friendship.','他们建立了长久的友谊。'),sources=['https://www.etymonline.com/word/last','https://en.wiktionary.org/wiki/lasting#English'])
W('upsetting','/ʌpˈsetɪŋ/','令人难过、不安的；打乱、弄翻；upset 的 -ing 形式',
 '消息把心情搅乱，事情让人难以平静，就可以叫 upsetting。前面的事物是引起不安的原因。',
 'upset + -ing，词末重读短元音后的 t 在这一形式中双写。upset 由较早的翻动、弄翻等物理用法，扩展到打乱情绪。',
 [['upset 的翻乱、扰动词族','使物理状态或心情不再平稳'],['upset + -ing → upsetting','令人不安的；正在扰乱、弄翻']],
 'upsetting news 令人难过的消息；an upsetting experience 令人不安的经历。作动词也可说 upsetting the balance 打破平衡。',
 'find something upsetting；deeply upsetting。','upset 常说人已经难过、不安；upsetting 常评价使人不安的事。I am upset 与 The news is upsetting 分别落在人和原因上。',
 ('The news was deeply upsetting.','这个消息令人十分难过。'),('She found the scene too upsetting to watch.','她觉得那一幕太令人难受，看不下去。'))
W('narcotics','英 /nɑːˈkɒtɪks/；美 /nɑːrˈkɑːtɪks/','麻醉性药物〔narcotic 复数〕；毒品相关的〔执法等语境〕',
 '医学、历史语境可用作 narcotic 的复数；警务小说里的 narcotics division 则通常是缉毒部门。先看文章属于哪种语境。',
 'narcotic + 复数 -s；narcotic 更早接麻木、昏睡的希腊词族。复数形式也固定用于毒品事务等类别修饰。',
 [['narcotic + -s','相应药物名的复数'],['narcotics 的固定类别用法','毒品事务、缉毒等语境的修饰材料']],
 'a narcotics detective 缉毒警探；the narcotics division 缉毒部门。这里的复数外形常给类别关系，不表示部门里有几种具体药物。',
 'a narcotics investigation；a narcotics case。','narcotics 的执法用法与 narcotic 的早期麻木词源不必逐字一致；不能只按让人困就推断所有相关类别。',
 ('The novel follows a detective in the narcotics division.','小说讲述一名缉毒部门警探的故事。'),('The article explains how the word narcotics is used in different contexts.','文章解释了 narcotics 在不同语境中的用法。'),sources=['https://en.wiktionary.org/wiki/narcotics#English'])
def extend_lessons():
    extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
    save('continuation_20261030_td',ROOTS,WORDS)
    extend_lessons()
