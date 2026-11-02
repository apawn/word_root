"""Criminal and lock: labels, criminalization; fastening, reversal and gridlock."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
C=[['拉丁语 crīmen、crīmin- → crīminālis','指控、罪等 → 与罪有关的'],['法语 criminal、criminel → 中古英语 cryminal → criminal','犯罪的、刑事的；名词罪犯']]
def CH(f,m):return C+[[f,m]]
W('criminal','/ˈkrɪmɪnəl/','犯罪的、刑事的；罪犯；严重得离谱的〔夸张〕',
 '可以标记行为、法律程序与犯罪有关，也可名词指犯罪的人。a criminal trial 是刑事审理，不是在说审理本身犯罪。',
 '经法语和晚期拉丁语 crīminālis，接 crīmen、crīmin- 罪、指控等。名词由人物性质称呼发展，现代可对照 crime 但保留拉丁词干的 n。',C,
 'criminal law 刑法，a criminal investigation 刑事调查，a convicted criminal 已定罪的罪犯；criminal waste 可夸张说严重浪费，不自动说明已有定罪。',
 'criminal law；a criminal investigation；a criminal offence；a convicted criminal。',
 'criminal 形容法律领域不等于每位涉及者已经有罪；suspect 嫌疑人、defendant 被告与 criminal 罪犯不能无条件互换。',
 ('She specializes in criminal law.','她专门研究刑法。'),('The detective interviewed the suspect during the criminal investigation.','侦探在刑事调查中询问了嫌疑人。'))
W('criminally','/ˈkrɪmɪnəli/','以犯罪方式；刑事上；严重得离谱地〔夸张〕',
 'criminally responsible 在谈刑事责任；criminally underrated 则常夸张说好得不该被忽视，并没有一条低估作品罪。',
 'criminal + -ly，副词随基础词分法律、犯罪和夸张评价。',CH('criminal + -ly → criminally','与犯罪、刑事有关地；比喻严重得离谱地'),
 'criminally responsible 负刑事责任的，criminally liable 承担刑事责任的，criminally underrated 被严重低估的。',
 'criminally responsible；criminally liable；criminally underrated。',
 'criminally underrated 是口语强评，不自动表示违法；正式法律搭配则应按具体语境，不能套用夸张义。',
 ('The report asks whether anyone was criminally responsible.','报告提出是否有人负刑事责任的问题。'),('The reviewer called the film criminally underrated.','评论者说这部电影被严重低估了。'))
W('criminalize','/ˈkrɪmɪnəlaɪz/','将某行为规定为犯罪、使犯罪化',
 '原来不作为刑事犯罪处理的行为，被规则、立法纳入犯罪范围；是在改变分类，不只是骂它不好。',
 'criminal + -ize，形成使成为犯罪、按犯罪处理的动词。英式也见 criminalise，不另设词头。',CH('criminal + -ize → criminalize','把某种行为归入犯罪处理范围'),
 'criminalize an activity 将某活动规定为犯罪，criminalize behaviour 将某行为犯罪化。具体何种行为在哪儿违法，要另查适用规则。',
 'criminalize an activity；criminalize behaviour；a law criminalizing。',
 'criminalize 设为犯罪、decriminalize 去犯罪化；criticize 批评不是同一个动作，反对行为不等于已将它入刑。',
 ('The article debates whether the activity should be criminalized.','文章讨论是否应把那项活动规定为犯罪。'),('The historian compared laws that criminalized the same behaviour in different periods.','历史学者比较了不同时期把同一行为规定为犯罪的法律。'))
W('criminalization','/ˌkrɪmɪnəlaɪˈzeɪʃən/','犯罪化、入罪化的过程或政策',
 '把某种行为纳入犯罪范围这件事，作为一个过程、问题来讨论，而不是在数有几个罪犯。',
 'criminalize 去 e 加 -ation，也可从 criminal + -ization 认识。名词命名使犯罪化过程。',CH('criminalize + -ation → criminalization','把行为归入犯罪的过程、做法'),
 'the criminalization of an activity 某活动的犯罪化，debate over criminalization 对入罪化的争论。',
 'the criminalization of；debate over criminalization；a policy of criminalization。',
 'criminalization 入罪过程，crime 犯罪、criminal 罪犯或刑事性质；名词不是犯罪人数的简称。',
 ('The lecture examined the history of criminalization.','讲座研究了犯罪化做法的历史。'),('The essay distinguishes social disapproval from criminalization.','文章区分了社会反对与把行为规定为犯罪。'))
R('B2906','与犯罪有关；人物、方式与行为分类变化','CRIMINAL：与罪相关，派生时分性质、人物和入罪过程','criminal → criminally；criminalize → criminalization 相邻；criminology 已有精讲，作为研究领域另列。',
 '不把刑事程序中的人都叫已犯罪者。法律搭配与口语严重得离谱的夸张分开，例句不替某地现行法律下判断。',
 '拉丁 crīmin- + -ālis → criminal；criminal + -ly/-ize；criminalize + -ation；crimin- + -ology。',
 [['性质、人物与方式','criminal · criminally'],['入罪变化和过程','criminalize · criminalization'],['研究领域','criminology']],
 'criminal trial 非违法审理；suspect/defendant/criminal 身份不同；criminally underrated 夸张；criminalization 非批评本身。',
 'The essay examines criminal law and the criminalization of certain activities.\n\n文章研究刑法，以及把某些活动规定为犯罪的做法。','criminal criminally criminalize criminalization criminology')
L=[['古英语 loc〔闩、闭合装置等〕、lūcan〔关〕→ 中古英语 lok 等','闭住、固定；现代锁与上锁动作'],['另一旧名词：古英语 locc → lock','一绺头发、卷发；更远关系有不同分析'],['现代锁的扩展','固定、船闸、擒抱；僵局、相扣等']]
def LH(f,m):return L[:1]+[[f,m]]
W('lock','英 /lɒk/；美 /lɑːk/','锁、上锁；固定；船闸；一绺头发〔另旧词形〕',
 '锁把原来能开的地方固定住；船闸控制水位与通行，也从闭合、围住来理解。a lock of hair 却是一绺头发，不是头发被锁上了。',
 '锁和关闭接古英语 loc、lūcan 等，现代名词、动词形式相互影响。头发接古英语 locc，直接祖先不同，更远是否相关不强定。',L,
 'lock the door 锁门，a door lock 门锁，lock into place 卡到固定位置，a canal lock 运河船闸，a lock of hair 一绺头发。',
 'lock the door；under lock and key；a canal lock；a lock of hair。',
 'close 关上、lock 锁住：门可已经关上却没锁。lock 发式义与门锁不能只按一个动作硬推。',
 ('Please lock the door before you leave.','离开前请锁门。'),('She kept a lock of her baby’s hair in a small box.','她把宝宝的一绺头发保存在小盒子里。'))
W('locker','英 /ˈlɒkə/；美 /ˈlɑːkər/','可上锁储物柜；锁定装置等',
 '每个人放包、衣服的那一小格柜子，通常能锁上。-er 在这里并非一个专门替你锁门的人。',
 'lock + -er，可表可锁容器或执行锁定的器具等。日常先掌握学校、健身房、车站储物柜。',LH('lock + -er → locker','可上锁存物的柜、格等'),
 'a school locker 学校储物柜，a locker room 更衣室，a station locker 车站寄存柜。',
 'a school locker；a locker room；put it in a locker。',
 'locker 储物柜，locksmith 锁匠；-er 常人物但不能对 locker 强套。locker room 是带柜、更衣等功能场所，不是锁匠工作室。',
 ('He left his bag in a station locker.','他把包存在车站储物柜里。'),('The players returned to the locker room.','队员们回到了更衣室。'))
W('locking','英 /ˈlɒkɪŋ/；美 /ˈlɑːkɪŋ/','锁定、上锁；可锁、用于锁定的',
 '动作在发生，或在说明一种部件能把东西固定住；locking mechanism 是负责锁定的结构。',
 'lock + -ing，分词、动作名词和修饰用途。k 后直接接 -ing，不再多写一个 k。',LH('lock + -ing → locking','上锁过程；能锁定、用于锁定的'),
 'a locking mechanism 锁定机构，locking wheels 可锁定脚轮，automatic locking 自动上锁。',
 'a locking mechanism；automatic locking；locking wheels。',
 'locking 上锁、锁定功能，locked 已锁的状态；a locking wheel 可设锁，并不保证此时已经 locked。',
 ('The case has a secure locking mechanism.','箱子有牢靠的锁闭机构。'),('She was locking the door when the phone rang.','电话响时，她正在锁门。'))
W('unlock','英 /ʌnˈlɒk/；美 /ʌnˈlɑːk/','开锁、解锁；开启潜能、使可用〔比喻〕',
 '把阻止开启的锁解除，东西就能用了；潜力、信息、机会原来取不到，后来能释放，也借这个动作说。',
 '有古英语 onlūcan、中古英语 unloken 等旧形，现代对应 un- 逆转 + lock。不是形容某东西不叫锁，而是把锁住状态解除。',LH('旧 onlūcan、unloken → unlock；现代对应 un- + lock','解除闭锁 → 使机会、能力等可发挥'),
 'unlock the door 开门锁，unlock a phone 解锁手机，unlock potential 发挥潜能，unlock new opportunities 开启新机会。',
 'unlock the door；unlock a phone；unlock potential；unlock opportunities。',
 'unlock 解除锁定、open 打开，先 unlock 后门仍可能没被推开；潜能比喻也不表示已经完成所有目标。',
 ('She unlocked the door but did not open it yet.','她开了门锁，但还没有推开门。'),('The course helped unlock his interest in science.','课程帮助激发了他对科学的兴趣。'))
W('lockable','英 /ˈlɒkəbəl/；美 /ˈlɑːkəbəl/','可上锁、可锁定的',
 '设计上能锁，可能现在开着，也可能没放钥匙进去。-able 说能力，不说当前状态。',
 'lock + -able，形成能上锁的形容词。',LH('lock + -able → lockable','可以上锁、锁定的'),
 'a lockable cabinet 可锁柜，lockable wheels 可锁脚轮，a lockable box 可锁盒子。',
 'a lockable cabinet；a lockable box；lockable wheels。',
 'lockable 能锁、locked 已锁、locking 锁定功能或过程；可锁并非当前一定锁好。',
 ('Keep the documents in a lockable cabinet.','把文件放在可上锁的柜子里。'),('The desk has a lockable drawer.','这张桌子有个可上锁抽屉。'))
W('gridlock','英 /ˈɡrɪdlɒk/；美 /ˈɡrɪdlɑːk/','交通瘫痪；相互牵制的僵局',
 '路网几个交叉口互相堵住，谁都没法往前；组织里的各方互相挡住，也借称 gridlock。',
 'grid 网格、路网 + lock 锁住，合成名词，也可动词表示陷入此种堵塞。政治、制度僵局是后来的相近比喻。',LH('grid + lock → gridlock','路网相互堵死；比喻彼此阻挡而停滞'),
 'traffic gridlock 交通瘫痪，political gridlock 政治僵局，bring a city to gridlock 使城市交通瘫痪。',
 'traffic gridlock；political gridlock；escape the gridlock。',
 'gridlock 比普通 traffic jam 常更强调路网互堵、难动；比喻不一定有道路，而是各方卡住。',
 ('Roadworks caused gridlock in the city centre.','道路施工让市中心交通瘫痪。'),('The negotiations remained stuck in gridlock.','谈判仍陷在各方互相牵制的僵局中。'))
R('B3384','闭合、固定和解锁；头发另旧名词，堵塞为比喻','LOCK：把可动、可开的东西固定住，再看能否解除','lock → locker、locking、lockable；unlock 逆转；deadlock、gridlock 僵局；其他锁匠、气闸、相扣、擒抱和步调复用。',
 'close 与 lock 分开，lockable/locking/locked 可能性、功能过程、状态分清。头发 lock 直接旧形另讲，冷门火器和医学病名暂略。',
 'lock + -er/-ing/-able；un- + lock；dead/grid/air/head + lock；lock + smith/step/box；inter- + lock。',
 [['锁与器具、功能、能力','lock · locker · locking · lockable · lockbox · locksmith'],['解除与互扣','unlock · interlock'],['堵塞、闸与擒抱步调','deadlock · gridlock · airlock · headlock · lockstep']],
 '关上不等于锁住；unlock 不等于已推开；lockable 不等于 locked；gridlock 互堵；头发不从上锁硬推。',
 'The locker is lockable, but someone forgot to lock it.\n\n柜子可以上锁，但有人忘了锁。','lock locker locking lockable lockbox locksmith unlock interlock deadlock gridlock airlock headlock lockstep')
if __name__=='__main__':save('continuation_20261030_cz',ROOTS,WORDS)
