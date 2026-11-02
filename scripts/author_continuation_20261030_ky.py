"""Freeze, sting and patch."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
F=[['古英语 frēosan → 中古英语 fresen → freeze','结冰、冷冻'],['不流动、不变化的比喻','人僵住、程序卡住；价格、账户等冻结'],['词形与派生','freeze → froze → frozen；freezing、freezer、unfreeze']]
W('freeze','/friːz/','结冰、冷冻；冻僵；僵住、卡住；冻结、暂停',
 '水冻成冰，不再流动；人突然一动不动、程序不响应，或某项变化被暂停，也借这幅冻结的画面。',
 '古英语 frēosan 经中古英语 fresen 传下。不规则词形 freeze → froze /frəʊz, froʊz/ → frozen，现代比喻从冷冻、停止活动扩出。',F[:2],
 'freeze water 把水冻住，freeze in fear 吓得僵住，the screen freezes 屏幕卡住，a hiring freeze 暂停招聘，freeze prices 冻结价格。',
 'freeze in fear；a hiring freeze；the screen freezes。',
 'freeze 可是结冰，也可是暂停变化；电脑 freeze 不一定温度过低。Freeze! 是站住、别动的命令。',
 ('The pond froze overnight.','池塘一夜之间结了冰。'),('The video froze just before the final scene.','视频在最后一幕前卡住了。'))
W('frozen','英 /ˈfrəʊzən/；美 /ˈfroʊzən/','冷冻、结冰的；僵住、冻结的',
 'freeze 是动作，frozen 看已经处在冻住、固定不动的状态。冷冻豌豆、结冰湖面、僵住的表情都能按对象理解。',
 'freeze 的不规则过去分词，由中古英语 frozen 等历史词形传下。元音变化和 -en 分词形式共同作用，不是现代把 freeze 原样再接普通 -ed。',F[:1]+[['freeze → froze → frozen','结冰、冻结 → 已冻结的状态']],
 'frozen vegetables 冷冻蔬菜，a frozen lake 结冰湖面，a frozen screen 卡住的屏幕，frozen in place 僵在原地。',
 'frozen vegetables；a frozen lake；frozen in place。',
 'frozen 常说已经形成的状态，freezing 可说正在结冰、很冷或冷冻过程。两者有不同句法作用。',
 ('The bag contains frozen peas.','袋子里装着冷冻豌豆。'),('She stood frozen in place when the door opened.','门打开时，她僵在原地。'))
W('freezing','/ˈfriːzɪŋ/','极冷的；冷冻、结冰；冰点〔相关表达〕',
 '天气冷得受不了，口语就说 freezing；科学或工艺里它也说液体变固体、食物冷冻的过程。',
 'freeze + -ing，去词尾 e。分词、行为名词及极冷的形容词在现代分别常用。',F[:1]+[['freeze + -ing → freezing','结冰、冷冻过程；极冷状态']],
 'It’s freezing. 冷极了。freezing cold 冰冷，below freezing 冰点以下，the freezing process 冷冻过程。气温表达中通常参照水的冰点。',
 'freezing cold；below freezing；the freezing process。',
 'I’m freezing 常夸张说很冷，不等于人已变成冰。各种物质的凝固温度不同，不宜把 freezing 在所有科学句里都当0度。',
 ('It is freezing outside, so I brought a thick coat.','外面冷极了，所以我带了厚外套。'),('The temperature fell below freezing during the night.','夜里气温降到冰点以下。'))
W('freezer','英 /ˈfriːzə/；美 /ˈfriːzər/','冷冻柜、冰柜；冰箱冷冻室',
 '把东西冻住、保持冷冻状态的设备或部分，是 freezer。家里可以是单独冰柜，也可以是冰箱中的冷冻室。',
 'freeze + -er，去词尾 e，按冷冻功能命名设备。',F[:1]+[['freeze + -er → freezer','使物品保持冷冻的设备、空间']],
 'put food in the freezer 把食物放进冷冻室，a chest freezer 卧式冰柜，the freezer compartment 冷冻隔室。',
 'in the freezer；a chest freezer。',
 'freezer 侧重冷冻；fridge 通常说冰箱、冷藏设备。实际一台 fridge freezer 可把冷藏与冷冻组合起来。',
 ('There is a bag of peas in the freezer.','冷冻室里有一袋豌豆。'),('They bought a small freezer for the garage.','他们买了一个小冰柜放在车库里。'))
W('unfreeze','/ˌʌnˈfriːz/','解冻；解除冻结、锁定；恢复活动',
 '把冻住、锁住、不再活动的状态解除，就是 unfreeze。实物可以解冻，账户、程序等则恢复可用、可变动。',
 'un- 撤销、逆转 + freeze。过去式、分词沿 freeze 变化：unfroze、unfrozen。',F[:2]+[['un- + freeze → unfreeze','解除冻结或固定不动的状态']],
 'unfreeze an account 解除账户冻结，unfreeze the screen 使屏幕恢复响应，unfreeze a process 恢复暂停过程。实物、食物解冻还常用 thaw、defrost。',
 'unfreeze an account；unfreeze the screen。',
 'unfreeze 强调撤销冻结状态；restart 是重启，某些情况可帮助恢复，但词义不相同。',
 ('The account was unfrozen after the error was corrected.','错误纠正后，账户解除了冻结。'),('Moving the mouse did not unfreeze the screen.','移动鼠标并没有让屏幕恢复响应。'))
R('B2867','从低温固化到暂停、固定不动，再解除该状态','FREEZE：流动、活动、变化被停住','freeze → frozen、freezing、freezer；unfreeze 撤销；antifreeze 用于防冻结。',
 '物理冷冻与比喻冻结可以共享停住的画面。完成状态、过程、设备和反向动作再用词尾、前缀区分。',
 'frēosan → freeze；froze、frozen 不规则词形；-ing 过程，-er 设备，un- 撤销，anti- 防止。',
 [['动作、状态与过程','freeze · frozen · freezing'],['设备、解除与防止','freezer · unfreeze · antifreeze']],
 'frozen 与 freezing 不同；电脑 freeze 不必冷；freezer 与冷藏设备侧重不同。',
 'The freezer keeps the vegetables frozen even when the kitchen is warm.\n\n即使厨房很暖，冷冻柜也让蔬菜保持冷冻。','freeze frozen freezing freezer unfreeze antifreeze')
S=[['古英语 sting、stingan → 中古英语 sting、stingen','尖物刺入、螫；刺痛'],['身体感受 → 情绪与话语','刺痛的感觉；尖刻批评、痛苦一击'],['派生与同形差异','stinging、stinger；stingy 吝啬义的确切来源有争议，读音与刺痛义不同']]
W('sting','/stɪŋ/','螫、刺痛；刺伤、螫针；情感上的刺痛；诱捕行动〔固定用法〕',
 '蜂螫一下、伤口碰到盐水时刺一下，是 sting；一句话像细针扎心，也可以 sting。动作与感受从身体伸向情绪。',
 '承古英语 sting、stingan 的尖刺、刺入用法，经中古英语传下。过去式、分词 stung /stʌŋ/，并有情绪、诱捕等固定现代用法。',S[:2],
 'a bee sting 蜂螫伤，My eyes sting. 眼睛刺痛，the sting of criticism 批评带来的刺痛，take the sting out of something 缓和某事的痛苦。a sting operation 诱捕行动。',
 'a bee sting；the sting of criticism；take the sting out。',
 'sting 重点是螫、尖锐刺痛；bite 重点是咬。刺痛的感觉可以没有一根实际的针存在。',
 ('Salt water stung the small cut.','盐水让小伤口刺痛。'),('Her careless words still stung.','她那句不经心的话仍让人刺痛。'))
W('stinging','/ˈstɪŋɪŋ/','螫人、刺痛的；尖刻、伤人的',
 '风刮在脸上像刺，批评扎在人心上，也都可 stinging。它抓住尖锐、伤人的感觉。',
 'sting + -ing，中古英语已有相应形式。由刺痛能力、正在刺痛，形成描述话语、打击的形容词。',S[:2]+[['sting + -ing → stinging','引起尖锐疼痛；批评等尖刻']],
 'a stinging sensation 刺痛感，stinging criticism 尖刻批评，a stinging defeat 沉重而令人难受的失败，stinging nettles 荨麻。',
 'a stinging sensation；stinging criticism。',
 'stinging criticism 强调伤人、尖锐，不保证批评正确或错误；描述的是力度和感受。',
 ('The cold wind brought a stinging sensation to his face.','冷风吹得他脸上刺痛。'),('The review delivered stinging criticism of the script.','评论对剧本作了尖刻批评。'))
W('stinger','英 /ˈstɪŋə/；美 /ˈstɪŋər/','螫针、刺；造成刺痛的东西、伤人的话',
 '蜂等用来螫的结构，可以 stinger；一个让人心里刺痛的讽刺、打击，也能按作用叫 stinger。',
 'sting + -er，命名执行螫刺的结构、对象。后缀不只指人。',S[:2]+[['sting + -er → stinger','螫刺结构；按效果命名的伤人事物']],
 'a bee’s stinger 蜂的螫针，a sharp stinger 锐利的刺；That remark was a stinger. 那句话够扎心。',
 'a bee’s stinger；a remark that is a stinger。',
 'stinger 可指造成螫刺的结构，sting 则还可说一次螫伤、疼痛。不同动物的结构不能只凭共同英文词认作完全相同。',
 ('The diagram labels the bee’s stinger.','图中标出了蜂的螫针。'),('His last remark was a real stinger.','他最后那句话真扎心。'))
W('stingy','常用吝啬义 /ˈstɪndʒi/；刺痛义 /ˈstɪŋi/','吝啬、小气的；给得少的；刺痛的〔另一读音〕',
 '不愿给钱、给帮助，是常用 stingy，读音里有 /dʒ/。读 /ŋ/ 的 stingy 则接 sting 刺痛义，两种用法不能只靠同拼写合并。',
 '吝啬义来源未定，可能由较早尖刻、刺痛的方言词变化而来；刺痛义可清楚对应 sting + -y。两者可能相关，具体语义历史不能编成花钱一定像蜂螫的事实。',S[:1]+[['stingy /ˈstɪŋi/','sting + -y：刺痛的'],['stingy /ˈstɪndʒi/','吝啬、给得少；与前义的历史联系尚有讨论']],
 'stingy with money 花钱小气，stingy with praise 不肯多表扬，a stingy portion 很少的一份。日常通常先掌握 /ˈstɪndʒi/。',
 'stingy with money；stingy with praise；a stingy portion。',
 'stingy 带负面小气评价，frugal 可中性或称赞节俭。钱不多、付不起，不自动等于不愿给。',
 ('The manager is stingy with praise.','经理很少肯表扬别人。'),('The café served a stingy portion of cake.','咖啡馆给的蛋糕小得可怜。'),sources=['https://en.wiktionary.org/wiki/stingy#English','https://www.etymonline.com/word/stingy'])
R('B2991','尖刺、螫痛到伤人的话，再辨 stingy 的读音和不确定历史','STING：尖锐的一下，既可在皮肤也可在感受里','sting → stinging、stinger；stingy 的刺痛义与吝啬义分开读；stingray 看相应动物的尾刺。',
 '刺痛感很直观，但不能因此给所有同形词编一个必然故事。吝啬义的远源仍保留不确定性。',
 'sting、stingan → sting；stung 不规则词形；-ing 性质、分词，-er 结构，-y 两种读音支线。',
 [['动作、感受与结构','sting · stinging · stinger · stingray'],['读音、意义分化','stingy']],
 'sting 与 bite 不同；stingy 吝啬 /dʒ/、刺痛 /ŋ/；普通 resting 是 rest + -ing，与本词族分开。',
 'The sting of that stinging remark faded by evening.\n\n到晚上，那句尖刻话带来的刺痛淡了。','sting stinging stinger stingray stingy')
ROOTS[-1]['exclude']['resting']='普通休息的 resting 来自 rest + -ing；罕见 re- + sting 同形词暂不展开。'
P=[['中古英语 patche','补片、斑块等；远源有不同分析'],['局部补片、区域的扩展','布补丁、软件补丁；地上、时间中的一块'],['patch + -y → patchy','一块块分布 → 不连续、不均匀']]
W('patch','/pætʃ/','补丁、补片；小块区域；修补、补缀',
 '衣服破了，用一小片布盖上修补，是 patch；软件针对局部问题的修正也像补片。草地、阳光露出一块块，也可叫 patches。',
 '中古英语 patche，远源可能联系更早 placche 斑块或法语 piece 的相关变体等，尚未确定。现代从局部布片扩到修补、区域和软件修改。',P[:2],
 'a patch on the sleeve 袖子上的补丁，a patch of grass 一小片草地，a software patch 软件补丁，patch things up 修复关系、暂作修补，a rough patch 一段难熬时期。',
 'a patch of；a software patch；patch things up；a rough patch。',
 'patch 既可临时应急，也可形成有效修复，不能一律当敷衍；patchwork 是用多片拼成的作品或拼凑结构。',
 ('She sewed a patch over the hole.','她缝上一块补丁，盖住破洞。'),('The update includes a patch for the display problem.','更新中包含修复显示问题的补丁。'))
W('patchy','/ˈpætʃi/','斑块状的；不均匀、断断续续的',
 '雾有一块没一块，信号时有时无，资料某些部分齐、某些部分缺，都像分成不连续的 patches，所以 patchy。',
 'patch + -y，由一块块、带斑块的形态，扩到分布、质量、记录的不均匀。',P[:2]+[['patch + -y → patchy','斑块状 → 不均匀、不连贯']],
 'patchy fog 零散雾区，patchy reception 不稳定的接收信号，a patchy record 不完整或表现不一的记录。',
 'patchy fog；patchy reception；patchy information。',
 'patchy 不是完全没有；重点是一部分有、一部分缺，或质量忽高忽低。poor 则更笼统地说差。',
 ('Mobile reception is patchy in the valley.','山谷里手机信号时有时无。'),('Our information about the early years is still patchy.','我们对早期年代掌握的资料仍不完整。'))
R('B3782','局部布片、补丁与区域，再到不均匀分布','PATCH：一小片，可以补洞，也可以是整体中的一块','patch → patchy；patchwork 看多片拼接。',
 '从一块补布走到一块草地、一个软件补丁，局部这层很好用；patchy 则把一块有、一块缺变成整体评价。',
 'patche → patch，远源未定；-y 性质；work 拼成的作品、结构等。',
 [['局部、修补与分布','patch · patchy'],['多片拼接的整体','patchwork']],
 'patch 不必永远临时；patchy 不等于完全缺失；a rough patch 是难熬的一段时期。',
 'The patchy grass showed several bare patches.\n\n长得稀稀落落的草地上露出几块光秃地方。','patch patchy patchwork')
if __name__=='__main__':save('continuation_20261030_ky',ROOTS,WORDS)
