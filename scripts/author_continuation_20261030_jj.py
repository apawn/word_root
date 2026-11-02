"""Boot, biological, epic, shield and shed."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
B=[['古法语 bote → 中古英语 bote／boote → boot','靴子；更远来源未定'],['boot + strap → bootstrap','靴子提带；借给自行带起、逐步建立的过程'],['bootstrap 的计算机义缩短 → boot','启动计算机；再有 reboot、bootable']]
W('boot','/buːt/','靴子；踢、赶出；汽车后备厢〔英式〕；启动〔计算机〕',
 '从脚上的靴子，可以想到一脚踢开、赶走。电脑启动义却要绕过 bootstrap：不是踢电脑一脚，它就启动了。',
 '靴子义经古法语 bote 进入英语，远源不确定。计算机 boot 缩自 bootstrap 的启动义；to boot 此外、而且则另承古英语 bōt 好处等旧义，不能一条线全包。',B,
 'walking boots 徒步靴，the car boot 汽车后备厢〔美式 trunk〕，boot someone out 把某人赶出去，boot the computer 启动电脑。',
 'walking boots；the car boot；boot out；boot the computer。',
 'boot the computer 和 boot someone out 是不同扩展。to boot 而且是另一条旧词历史，不是又来一只靴子。',
 ('She put her walking boots in the car boot.','她把徒步靴放进汽车后备厢。'),('The computer takes a minute to boot.','这台电脑需要一分钟启动。'))
W('booted','/ˈbuːtɪd/','穿靴的；被踢出、赶出的；已启动〔boot 的词形〕',
 'a booted foot 是穿靴的脚；got booted out 是被赶走；系统 booted 则说它启动了。先看 boot 用的是哪条意思，再判断 -ed。',
 'boot + -ed。末尾 /t/ 后 -ed 读 /ɪd/；既可作过去式、过去分词，也可由名词形成穿着靴子的形容词。',B+[['boot + -ed → booted','穿靴的性质；踢出、启动等动词的过去形式']],
 'booted feet 穿靴的双脚，got booted from the game 被踢出游戏，the computer booted successfully 电脑成功启动。',
 'booted feet；got booted out；booted successfully。',
 'booted 不固定就是启动完毕。The booted figure stood at the door 的人影穿着靴子，与电脑无关。',
 ('His booted feet left muddy marks on the floor.','他穿靴的双脚在地板上留下泥印。'),('The computer booted successfully after the update.','更新后电脑成功启动了。'))
W('bootstrap','/ˈbuːtstræp/','靴子提带；靠已有资源逐步建立；启动、自举；自助重采样法',
 '本来是帮助穿靴子的提带。提着自己的靴带把自己抬起来原是办不到的画面，后来却借给自力起步、用小步骤带起大系统。',
 'boot 靴子 + strap 带。由 pull oneself up by one’s bootstraps 的比喻发展；计算机、统计、创业等领域各自固定术语，不把它们说成同一种具体操作。',B,
 'bootstrap a system 自举、逐步建立系统，bootstrap a business 靠自身资源起步经营，a bootstrap estimate 自助法估计。统计用法通常从观测数据反复有放回抽样，估计统计量的变化。',
 'bootstrap a system；bootstrap a business；a bootstrap estimate。',
 '计算机自举是由初始机制带起后续系统，不是凭空没有外部条件。统计 bootstrap 是特定抽样方法；大写 Bootstrap 还可作软件框架名称。',
 ('A small program helps bootstrap the rest of the system.','一段小程序帮助带起系统其余部分。'),('The researchers used a bootstrap method to estimate uncertainty.','研究人员用自助重采样法估计不确定性。'),sources=['https://en.wiktionary.org/wiki/bootstrap#English','https://www.etymonline.com/word/bootstrap'])
W('reboot','动词常 /ˌriːˈbuːt/；名词常 /ˈriːbuːt/','重新启动；重新开始；重启作品系列',
 '电脑已经启动过，再让启动过程走一遍，是 reboot。电影、剧集的故事体系重新开篇，也借这个重新起步的意思。',
 're- 再次 + boot 计算机启动义；再从系统重启扩到项目、作品重新开始。不同作品对是否沿用旧设定处理不一。',B[1:]+[['re- + boot → reboot','重新启动；重新组织开篇']],
 'reboot the computer 重启电脑，a system reboot 一次系统重启，a reboot of the series 系列作品重启版。',
 'reboot the computer；a system reboot；a reboot of the series。',
 'reboot 不等于 reinstall 重装，也不必擦除用户所有资料。作品 reboot 与续集 sequel 重点不同，但市场称法可能有交叠。',
 ('Please reboot the computer after the installation.','安装完成后请重启电脑。'),('The studio announced a reboot of the old series.','制片公司宣布重启那部老系列作品。'))
W('bootable','英 /ˈbuːtəbəl/；美 /ˈbuːtəbəl/','可启动的；可用于引导系统的',
 '普通U盘只是存文件，bootable USB drive 则具备让相应电脑从它开始加载系统的条件。词尾告诉你能不能用于启动。',
 'boot 启动 + -able 能够、可用于。不是拿得动、能穿上的靴子的常规形容词。',B[1:]+[['boot + -able → bootable','可启动；可以用作启动来源']],
 'a bootable USB drive 启动U盘，a bootable disk 可引导磁盘。是否能在某台机器启动，还涉及格式、内容与兼容性。',
 'a bootable USB drive；a bootable disk。',
 'bootable 不等于盘里随便有一个系统文件；bootable 说明可用于相应启动，portable 说明便携或可移植。',
 ('She created a bootable USB drive for the test computer.','她为测试电脑制作了一个启动U盘。'),('The installer checked whether the disk was bootable.','安装程序检查磁盘是否可用于启动。'))
R('B2924','靴子及踢出、后备厢等扩展，另经提带比喻形成电脑启动','BOOT：计算机启动要经过 bootstrap 这座桥','boot 靴子 → bootstrap 提带、借喻自举 → boot 电脑启动 → reboot、bootable。',
 '不要凭现代同形词编一脚踢开电脑的词源。booted 也要随上下文判断穿靴、被赶走还是启动。',
 '古法语 bote → boot；boot + strap；计算机 bootstrap 缩成 boot；re- 再次、-able 可用于。',
 [['基础和旧扩展','boot · booted · bootleg'],['自举与电脑启动','bootstrap · reboot · bootable']],
 'to boot 此外、而且另有来源；reboot 不等于重装全部系统。',
 'The computer can boot from the bootable drive and reboot after installation.\n\n电脑能从启动盘启动，并在安装后重启。','boot booted bootleg bootstrap reboot bootable')
W('neurobiological','英 /ˌnjʊərəʊˌbaɪəˈlɒdʒɪkəl/；美 /ˌnʊroʊˌbaɪəˈlɑːdʒɪkəl/','神经生物学的',
 '研究神经细胞、脑和神经系统怎样从生物层面工作，便是神经生物学视角。不是把所有行为都只归结为一个脑区。',
 'neuro- 神经 + biological 生物学的。neuro- 接希腊 neûron 的筋、神经相关来源，现代科学中固定表示神经。',
 [['希腊 neûron → neuro-','现代构词中的神经相关成分'],['neuro- + biological → neurobiological','从神经生物学研究的、与之有关的']],
 'neurobiological research 神经生物学研究，a neurobiological mechanism 神经生物学机制，neurobiological processes 神经生物过程。',
 'neurobiological research；a neurobiological mechanism。',
 'biological 范围广，neurobiological 把焦点放到神经系统。术语说明研究层面，本身并不宣称某个复杂现象只有一种原因。',
 ('The course introduces neurobiological research methods.','课程介绍神经生物学研究方法。'),('The paper discusses neurobiological mechanisms of learning.','论文讨论学习的神经生物学机制。'))
R('B3845','生物学相关性质，以及从领域进一步限定研究对象','BIOLOGICAL：与生命、生物学有关；前缀可进一步聚焦','biological → biologically；microbiological 聚焦微生物，neurobiological 聚焦神经系统。',
 '共同部分给出生命、生物学这一层，前面增加的成分再决定研究哪类对象。',
 'biology 的 bio- 生命、-logy 研究基础 → biological；neuro- 与 micro- 再作限定，-ly 形成副词。',
 [['基础性质与副词','biological · biologically'],['具体研究领域','microbiological · neurobiological']],
 'biological 不只表示天然、未加工；neurobiological 是研究对象、层面的限定。',
 'The book moves from biological principles to neurobiological explanations of learning.\n\n这本书从生物学原理讲到学习的神经生物学解释。','biological biologically microbiological neurobiological')
E=[['希腊 épos：话语、故事 → epikós','与史诗相关的'],['拉丁 epicus → 法语 épique → 英语 epic','史诗；史诗般宏大；口语中很震撼']]
W('epic','/ˈepɪk/','史诗；史诗般的、规模宏大的；超棒的、惊人的〔口语〕',
 '先想到讲英雄、重大冒险的长篇故事，再把它的宏大、震撼借给旅程、电影、比赛。朋友说 epic，也可能只是在夸太精彩了。',
 '经法语 épique、拉丁 epicus 接希腊 epikós、épos 话语、故事。常用史诗义不是 epi- 在上面 + -ic 的随意组合；数学另有同形术语。',E,
 'an epic poem 史诗，an epic journey 壮阔艰难的旅程，an epic film 史诗片，That was epic! 太精彩了！也有 epic failure 强烈夸张的惨败。',
 'an epic poem；an epic journey；an epic film；epic failure。',
 'epic 的宏大可以是赞叹，也可加强负面失败。不是所有 epic 都是一篇诗，口语的评价用法远比文学体裁宽。',
 ('The film tells an epic story of survival.','电影讲述了一个史诗般的求生故事。'),('That final match was epic.','那场决赛真是精彩绝伦。'))
W('epically','/ˈepɪkli/','史诗般地；极其、非常〔口语夸张〕',
 '把 epic 的宏大、惊人放到某个行为、结果上。epically wrong 不是像诗一样错，而是错得离谱。',
 'epic + -ally，或对应 epical + -ly。现代常压缩读成 /ˈepɪkli/，并不每个拼写字母都多占一个音节。',E+[['epic + -ally → epically','史诗般地；以强烈夸张方式评价程度']],
 'epically ambitious 极其雄心勃勃的，epically wrong 错得离谱，fail epically 败得很惨。较口语、夸张，正式报告常用更具体的描述。',
 'epically ambitious；epically wrong；fail epically。',
 'epically 是程度、方式评价，不等于 technically 技术上，也不自动含正面赞美。',
 ('The plan was epically ambitious.','这个计划雄心大得惊人。'),('Our prediction turned out to be epically wrong.','事实证明我们的预测错得离谱。'))
R('B4608','从史诗体裁到宏大、震撼与口语夸张','EPIC：先是大故事，再借来形容大场面和强烈效果','epic → epically。',
 '文学用法看作品类型，日常评价看震撼程度。两者有联系，不能因为某人说一顿饭 epic 就要求它讲英雄故事。',
 '希腊 épos、epikós → 拉丁 epicus → 法语 épique → epic；-ally 副词。',
 [['体裁、性质与副词','epic · epically']],
 '常用 epic 不靠 epi- 在上面解释；epic failure 可以强烈负面。',
 'The epic film was epically ambitious in scale.\n\n这部史诗片在规模上有着惊人的雄心。','epic epically')
W('shield','/ʃiːld/','盾；防护物、屏障；保护、遮挡',
 '把一块东西挡在伤害前面，保护后方的人或物，是 shield 的基本画面。后来可以挡热、挡辐射，也可以替人挡批评。',
 '名词接古英语 scield，经中古英语 scheld 等；动词也有古老对应形式。远源常联系切分材料，但现代不需要把每种屏障都想成切下的木板。',
 [['古英语 scield 盾、sċildan 保护 → 中古英语相关形式','防御器具与保护动作'],['现代 shield','实物屏障；保护、隔开不利影响']],
 'a heat shield 隔热罩，a face shield 面罩，shield someone from criticism 保护某人不受批评，shield your eyes from the sun 遮住眼睛避强光。',
 'a heat shield；a face shield；shield from。',
 'shield from 强调隔开威胁、影响；hide from 侧重藏起来。windshield 是汽车挡风玻璃〔美式〕，不是手持盾牌。',
 ('She used her hand to shield her eyes from the sun.','她用手遮眼，挡住阳光。'),('The equipment has a protective shield.','设备有一层防护罩。'))
R('B3913','挡在前面保护，以及按这种功能命名的物件','SHIELD：屏障在前，受保护的对象在后','shield → windshield 挡风玻璃；shield 本身也作动词。',
 '保护可以是实物阻挡，也可以是免受批评等抽象影响。看 from 后面要隔开的是什么。',
 '古英语 scield、sċildan → shield；wind + shield 按挡风功能组合。',
 [['屏障与具体器具','shield · windshield']],
 'shield 不必是军用盾牌；windshield 在英式英语常叫 windscreen。',
 'The windshield acts as a shield against wind and rain.\n\n挡风玻璃起着遮挡风雨的作用。','shield windshield')
W('shed','/ʃed/','脱落、脱去；流出、散发；棚、小屋',
 '蛇把旧皮脱离身体，树让叶子落下，人流下眼泪，都能用动词 shed。院子里的工具棚也叫 shed，却不能硬编成脱下来的房子。',
 '动词接古英语 scēadan 分开、分离，经中古英语 scheden 留传。棚屋名词通常联系 shade 遮蔽的方言变化，也可能受其他旧棚屋词影响，直接路线与动词不同。',
 [['古英语 scēadan → 中古英语 scheden → shed 动词','分开 → 脱落、流下、散出'],['棚屋名词的另线','可能联系 shade 的遮蔽义、方言形式；不是脱落动作的确定派生']],
 'shed skin 蜕皮，shed leaves 落叶，shed tears 流泪，shed light on 说明、使更清楚，a garden shed 花园工具棚。过去式、过去分词仍是 shed，shedding 双写 d。',
 'shed skin；shed tears；shed light on；a garden shed。',
 'bloodshed 的 shed 联系流出；woodshed 的 shed 是棚屋；watershed 保留分界的旧联系，不是水搭的小棚。',
 ('The snake shed its old skin.','蛇蜕去了旧皮。'),('The new evidence shed light on the mystery.','新证据使谜团更清楚了。'),sources=['https://en.wiktionary.org/wiki/shed#English','https://www.etymonline.com/word/shed'])
R('B2970','分离、脱落与流出；另辨棚屋的同形来源','SHED：动词抓分离、放出，棚屋名词另走一线','shed → bloodshed 流血；watershed 分界；woodshed 的后半是棚屋。',
 '今天一个拼写收下了几条历史。把各词放一起辨认，比用一个生硬画面全部串成假同源更稳。',
 '动词由 scēadan 分离演变；棚屋名词另联系 shade 等形式；过去式 shed 不变。',
 [['分离、流出及分界','shed · bloodshed · watershed'],['棚屋名词组合','woodshed']],
 'woodshed 不是木头脱落；watershed 也不是水棚。shed light on 是使问题更清楚。',
 'The lesson sheds light on why bloodshed and woodshed use different senses of shed.\n\n这课说明了 bloodshed 与 woodshed 为什么使用不同的 shed 义项。','shed bloodshed watershed woodshed')
if __name__=='__main__':save('continuation_20261030_jj',ROOTS,WORDS)
