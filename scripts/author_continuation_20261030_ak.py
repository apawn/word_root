"""Quick and throw: historical meanings still visible in familiar words."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
QU=[['古英语 cwic → 中古英语 quik','活着的、有生命的；敏捷的'],['现代 quick','有活力、反应灵 → 快、耗时短']]
def QH(f,m):return QU+[[f,m]]
W('quick','/kwɪk/','快的；迅速的；反应灵敏的；活的〔旧义〕',
 '人一有反应就马上动起来，一件事没多久就做完；快是今天的中心，活着是旧起点。',
 '继承古英语 cwic 活着、有生命，后来活跃、敏捷义走向迅速。旧活义还留在 quicksand、quicksilver 等组合里。',QU,
 'a quick reply 迅速回复，a quick learner 学得快的人，a quick look 快速看一眼，be quick to do 很快就做。',
 'a quick reply；a quick learner；a quick look；quick to do。',
 'quick 常强调响应快、耗时短，fast 更常说持续运动速度高；用法有重合，不能每句机械互换。',
 ('Thanks for your quick reply.','谢谢你迅速回复。'),('She is quick to notice changes in tone.','她很快就能注意到语气变化。'),sources=['https://www.etymonline.com/word/quick','https://en.wiktionary.org/wiki/quick#English'])
W('quickly','/ˈkwɪkli/','迅速地；很快地',
 '动作做得快，或某种变化很短时间内发生；是用来描述过程的副词。',
 'quick + -ly，中古英语已有同族形式。后缀让快这个性质去修饰动作、变化等。',QH('quick + -ly → quickly','迅速地；短时间内发生'),
 'reply quickly 快速回复，quickly realize 很快意识到，as quickly as possible 尽快。',
 'reply quickly；quickly realize；as quickly as possible。',
 'a quick reply 形容词修饰名词，reply quickly 副词修饰动词。口语 Come quick! 可见，但一般写作 quickly 更通用。',
 ('The weather changed quickly in the mountains.','山区天气变化很快。'),('Please reply as quickly as possible.','请尽快回复。'))
W('quicken','/ˈkwɪkən/','加快；变快；使活跃〔也有旧活化义〕',
 '心跳节奏加快、脚步越来越急，都可以说 quicken；也可使兴趣更活跃。',
 'quick + -en，中古英语已有，较早可说赋予生命、活过来，后来常用加速义。不是 quick 的过去式。',QH('quick + -en → quicken','使有生命、活跃 → 加快、变快'),
 'quicken your pace 加快脚步，one’s pulse quickens 心跳加快，quicken interest 激起兴趣。',
 'quicken your pace；the pulse quickens；quicken interest。',
 'quicken 动作变化，quick 状态快；The pace quickened 不等于更快这个形容词比较级 quicker。',
 ('They quickened their pace as the rain began.','开始下雨时，他们加快了脚步。'),('Her pulse quickened when she heard the announcement.','听见公告时，她心跳加快了。'))
W('quickness','/ˈkwɪknəs/','迅速；敏捷；反应快',
 '把做事快、反应灵这个特点拿出来说，而不是指某一次动作。',
 'quick + -ness，中古英语已有对应名词。常用作不可数的性质、能力描述。',QH('quick + -ness → quickness','快速、敏捷的性质'),
 'quickness of thought 思维敏捷，quickness of movement 动作敏捷，mental quickness 反应灵活。',
 'quickness of thought；mental quickness；quickness of movement。',
 'quickness 性质名词，quickly 方式副词；with great quickness 与 acted quickly 是两种表达结构。',
 ('Her quickness of thought helped solve the puzzle.','她思维敏捷，帮助解开了难题。'),('The player is known for his quickness around the court.','这位球员以场上移动敏捷闻名。'))
W('quicksand','/ˈkwɪksænd/','流沙；让人越陷越深的困境〔比喻〕',
 '表面像地面，里面却松软、会流动，物体容易陷下去；名字叫的其实是活沙。',
 'quick 的旧义活的、会动的 + sand 沙，接中古英语同族组合。不是保证沉得特别快，更不能拿电影夸张当真实物理过程。',QU[:1]+[['quick〔活、会动〕+ sand → quicksand','不稳定、易下陷的湿沙；后有困境比喻']],
 'a patch of quicksand 一片流沙，the quicksand of bureaucracy 官僚程序中越陷越深的困境。',
 'a patch of quicksand；sink into quicksand；the quicksand of。',
 'quicksand 的 quick 保留活义；quick sand 不能简单按快速的沙解释。比喻义重点是难脱身、进展被困住。',
 ('The guide pointed out a patch of quicksand near the river.','向导指出河边有一片流沙。'),('The project became stuck in the quicksand of endless reviews.','项目陷入了无休止审查的困境。'),sources=['https://www.etymonline.com/word/quicksand','https://en.wiktionary.org/wiki/quicksand#English'])
W('quicksilver','英 /ˈkwɪksɪlvə/；美 /ˈkwɪksɪlvər/','水银、汞；变化莫测的〔比喻形容词〕',
 '银亮的液态金属一动就滑走，像活的银；比喻里也说人反应灵动、性情多变。',
 '古英语 cwicseolfor，quick 旧活义 + silver 银，可能有拉丁 living silver 相应名称的翻译影响。不是指某种高速固态白银。',QU[:1]+[['古英语 cwic + seolfor → quicksilver','活的银 → 水银；另有灵动、多变比喻']],
 'the old name quicksilver 水银旧名，quicksilver changes 瞬息变化，a quicksilver mind 灵动多变的头脑。现代化学名通常 mercury。',
 'quicksilver changes；a quicksilver mind；the metal quicksilver。',
 'silver 银是另一元素，quicksilver 是 mercury 汞的传统名称；共享颜色形象不意味着同一种物质。',
 ('The old text refers to mercury as quicksilver.','旧文献把汞称为水银。'),('Her quicksilver changes of mood kept everyone guessing.','她情绪变幻莫测，让大家难以捉摸。'))
R('B3271','活着、灵动到迅速；保留旧义的流沙、水银','QUICK：旧义活，常用义快','quick → quickly、quickness、quicken；quicksand、quicksilver 接活的旧义，quickstep 已有精讲。',
 '本族生命词发展出敏捷、耗时短。活的旧义虽不再日常独立使用，却能解释几个熟悉复合词。',
 'quick + -ly/-ness/-en；quick〔活〕+ sand/silver；quick + step。',
 [['速度、方式、性质与变化','quick · quickly · quickness · quicken'],['旧活义与既有舞步','quicksand · quicksilver · quickstep']],
 'quick 耗时短与 fast 高速度有侧重；quicksand 活沙不等于一定飞快下沉；quicksilver 汞不同于银。',
 'Her quickness of thought helped her respond quickly.\n\n她思维敏捷，能迅速作出回应。',
 'quick quickly quickness quicken quicksand quicksilver quickstep')
TH=[['古英语 þrāwan → 中古英语 throwen','转动、扭转'],['现代 throw','抛、掷；旧转动义保留于制陶等用法']]
def HH(f,m):return TH+[[f,m]]
W('throw','英 /θrəʊ/；美 /θroʊ/','扔、投掷；使陷入；举办〔聚会〕；拉坯制陶',
 '今天最直观是把东西抛出去；旧义是扭转、旋转，所以陶轮上做陶器也能叫 throw。',
 '继承古英语 þrāwan 转、扭，后来投掷义成为中心，可能经过转动后抛出的动作联系。具体历史动机保留可能性。变化 throw—threw—thrown。',TH,
 'throw a ball 扔球，throw away 丢掉，throw a party 办聚会，throw a pot 在陶轮上拉坯制陶。',
 'throw a ball；throw away；throw a party；throw a pot。',
 'throw 常主动使物体飞出，drop 常放落、失手落下；throw a party 是固定举办表达，不是真的扔一个聚会。',
 ('Throw the ball to me.','把球扔给我。'),('They threw a small party to celebrate.','他们办了个小聚会庆祝。'),sources=['https://www.etymonline.com/word/throw','https://en.wiktionary.org/wiki/throw#English'])
W('thrown','英 /θrəʊn/；美 /θroʊn/','throw 的过去分词；被抛出的；拉坯制的',
 '东西已经被扔出，或陶器已经在轮上拉坯成形；具体对象接 throw 的不同义。',
 'throw 的历史过去分词，现代可见末尾 -n 的分词标记，不是过去式。过去式另是 threw。',TH+[['throw → threw → thrown','原形、过去式、过去分词；保留旧不规则变化']],
 'has thrown 已经投出，be thrown away 被丢掉，a thrown pot 拉坯陶器。',
 'has thrown；be thrown away；a thrown pot。',
 'threw 过去式、thrown 分词；throne 王座常与 thrown 同音，拼写、意义都不同。',
 ('Someone has thrown away my notes.','有人把我的笔记扔掉了。'),('The ball was thrown over the wall.','球被扔过了墙。'))
W('thrower','英 /ˈθrəʊə/；美 /ˈθroʊər/','投掷者；投掷器；拉坯陶工',
 '按 throw 的动作称呼执行者：体育里投掷的人，陶艺里也可指做拉坯的人。',
 'throw + -er，中古英语已有对应形式；人和工具都可能用这个后缀。陶工义保留 throw 转动制陶的支线。',HH('throw + -er → thrower','执行投掷或转动制陶的人、器具'),
 'a discus thrower 铁饼运动员，a javelin thrower 标枪运动员；具体项目由前面的名词说明。',
 'a discus thrower；a javelin thrower；a skilled thrower。',
 'thrower 投掷者，catcher 接球者；thrower 不表示投出去的物本身。',
 ('The discus thrower improved her personal best.','铁饼运动员刷新了个人最好成绩。'),('The workshop is taught by an experienced pottery thrower.','工坊由一位经验丰富的拉坯陶工教授。'))
W('overthrow','英 /ˌəʊvəˈθrəʊ/；美 /ˌoʊvərˈθroʊ/〔动词〕','推翻、打倒；投得过远〔另一路用法〕',
 '把原来立着的地位翻倒；体育里也可以单纯说球投过了该到的位置。',
 'over- + throw，中古英语已有推翻相关形式；现代政治、制度语境固定为推翻。体育过远义则直接取 over 过量、超过。',HH('over- + throw → overthrow','翻倒、使失去地位；另有超过目标的投掷'),
 'overthrow a ruler 推翻统治者，the overthrow of a government 政权被推翻。变化 overthrew、overthrown；名词重音常靠前。',
 'overthrow a ruler；the overthrow of；overthrow the target。',
 'overthrow 推翻不同于普通 oppose 反对；overthrow the target 体育中可投过头，不需要政治解释。',
 ('The book describes the overthrow of the old regime.','书中描写旧政权被推翻的过程。'),('The player overthrew his teammate by several metres.','球员投球超过队友位置好几米。'))
R('B3002','扭转旧义与投掷、举办、拉坯、推翻','THROW：今天抛出去，旧的转动义仍有痕迹','throw → thrown、thrower，再接 overthrow；把动词不规则变化和后缀人物分开。',
 '古英语先转、扭，投掷义后来成为中心。拉坯还见旧旋转动作，举办聚会等则是固定搭配。',
 'throw—threw—thrown；throw + -er；over- + throw → overthrew／overthrown。',
 [['基本动作、分词与人物','throw · thrown · thrower'],['翻倒与过远','overthrow']],
 'threw 过去、thrown 分词；throw a party 固定举办；陶工 thrower 不在扔陶罐；overthrow 体育还可过远。',
 'The thrower had thrown the ball farther than expected.\n\n投掷者把球投得比预想更远。',
 'throw thrown thrower overthrow')
if __name__=='__main__':save('continuation_20261030_ak',ROOTS,WORDS)
