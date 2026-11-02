"""Stock, sort and definite: practical meanings and close derivatives."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
ST=[['古英语 stocc → 中古英语 stok','树干、树桩；支撑主体'],['英语 stock 的后续多支','基础、来源；储备、资本 → 库存、股票、原料、汤底']]
def SH(f,m):return ST+[[f,m]]
W('stock','英 /stɒk/；美 /stɑːk/','库存、储备；股票；原料；汤底；备货',
 '现代很多义都可先抓“备着、从中取用的一份基础”：商店的货、工厂的料、煮汤的底。股票则走资本份额的分支。',
 '继承古英语 stocc 树干、树桩。储备、资本等义有多条历史发展，具体中间关系未全确定；基础画面能帮记，不能当每义都证实直接由树干产生。',ST,
 'in stock 有货，out of stock 缺货，take stock 盘点或审视，vegetable stock 蔬菜汤底，company stock 公司股票。',
 'in stock；out of stock；take stock；vegetable stock。',
 'stock 作库存常不可数，stocks 可各只股票、不同储备；stock 汤底与 soup 成品汤不同，但实际烹饪可有交叉。',
 ('The shop has this model in stock.','店里这款有现货。'),('Add a little vegetable stock to the pan.','往锅里加一点蔬菜汤底。'),sources=['https://www.etymonline.com/word/stock','https://en.wiktionary.org/wiki/stock#English'])
W('restock','英 /ˌriːˈstɒk/；美 /ˌriːˈstɑːk/','补货；重新储备',
 '架子卖空了或存量不够，把货再补进去。',
 're- 再次 + stock 备货，动词强调库存的补充，不只表示把旧东西重新数一遍。',SH('re- + stock → restock','再次备货、补足存量'),
 'restock the shelves 补满货架，restock supplies 补充用品，restock with fresh goods 补入新货。',
 'restock the shelves；restock supplies；restock with。',
 'restock 补货，take stock 盘点；盘点发现不够后可能再补，但不是一个动作。',
 ('The staff restock the shelves every morning.','员工每天早上补货。'),('We need to restock our supply of printer paper.','我们需要补充打印纸。'))
W('overstock','英 /ˌəʊvəˈstɒk/；美 /ˌoʊvərˈstɑːk/〔动词〕','备货过多；库存过剩',
 '备的货比能卖、能用的多，东西堆在那里占空间。',
 'over- 过度 + stock 备货；名词也可指多出来的库存。分别看动作还是多余货品。',SH('over- + stock → overstock','备货过量；过剩存货'),
 'overstock a store 备货过多，be overstocked with coats 外套库存过多，sell overstock 出售过剩库存。',
 'overstocked with；overstock a store；excess overstock。',
 'overstock 库存多，不等于 oversell 卖出超过供应；前者货压多，后者承诺卖得超过可供。',
 ('The shop overstocked winter coats after a mild autumn.','秋季温和，店里冬外套备多了。'),('The warehouse is overstocked with last year’s models.','仓库积压了过多的去年型号。'))
W('stockbroker','英 /ˈstɒkbrəʊkə/；美 /ˈstɑːkbroʊkər/','股票经纪人',
 '在股票交易中，替客户办理买卖的经纪服务人员；这里 stock 取股票义。',
 'stock 股票 + broker 经纪人，按经纪业务对象形成名称。不是负责商店库存盘点的人。',SH('stock + broker → stockbroker','办理股票买卖经纪业务的人'),
 'a licensed stockbroker 有相应资格的股票经纪人，work as a stockbroker 做股票经纪人。具体服务依业务而异。',
 'a stockbroker’s office；work as a stockbroker；contact a stockbroker。',
 'stockbroker 提供交易等经纪服务，stockholder 持有股票；同一个人可以兼有身份，但词义不同。',
 ('She worked as a stockbroker before changing careers.','转行前，她做股票经纪人。'),('The novel’s main character is a retired stockbroker.','小说主角是一名退休股票经纪人。'))
W('stockholder','英 /ˈstɒkhəʊldə/；美 /ˈstɑːkhoʊldər/','股东；股票持有人',
 '持有公司股票的人或机构，按持有关系而非工作岗位命名。',
 'stock 股票 + holder 持有人，holder 来自 hold + -er。常与 shareholder 同义。',SH('stock + hold + -er → stockholder','持有公司股票的主体'),
 'a major stockholder 大股东，stockholders’ meeting 股东会议。数量、权利等具体信息需看相应安排。',
 'a major stockholder；a stockholders’ meeting；stockholder approval。',
 'stockholder 股东，stakeholder 利益相关者范围更宽；员工、顾客等可以是利益相关者而不持股。',
 ('The company sent a report to its stockholders.','公司向股东发送报告。'),('A major stockholder attended the meeting.','一位大股东出席了会议。'))
W('feedstock','英 /ˈfiːdstɒk/；美 /ˈfiːdstɑːk/','工业原料；加工过程的主要投入料',
 '不断送进机器或工艺流程里的原始材料，像给流程喂进去的那一批料。',
 'feed 喂入、供给 + stock 原料储备，工业复合词。feed 在这里不只指给动物喂食。',SH('feed + stock → feedstock','投入生产流程的成批原料'),
 'chemical feedstock 化工原料，biomass feedstock 生物质原料，feedstock supply 原料供应。',
 'chemical feedstock；biomass feedstock；feedstock supply。',
 'feedstock 是加工投入原料，livestock 是活家畜；两个词后部相同，前部决定完全不同类别。',
 ('The plant uses wood waste as feedstock.','工厂用木材废料作原料。'),('The report examines the availability of biomass feedstock.','报告研究生物质原料的供应情况。'))
W('stocky','英 /ˈstɒki/；美 /ˈstɑːki/','矮壮的；敦实的',
 '身形不是细长，而是短一些、结实紧凑，像一截粗壮树干。',
 'stock + -y，接树干、结实主体的形象，固定用于敦实、粗壮的体形。不是库存很多的普通说法。',SH('stock + -y → stocky','树干般粗实 → 身材敦实'),
 'a stocky build 敦实体格，a short, stocky man 个子较矮、身材壮实的人。',
 'a stocky build；short and stocky；a stocky figure。',
 'stocky 强调整体短实，不等于只说 fat 胖；stocky 与 skinny 瘦削是不同身体描述。',
 ('He has a short, stocky build.','他身材较矮、敦实。'),('The drawing shows a stocky figure in a heavy coat.','画里是一个穿厚外套的敦实身影。'))
W('stocking','英 /ˈstɒkɪŋ/；美 /ˈstɑːkɪŋ/','长袜；圣诞袜；备货〔另一词形用法〕',
 '衣物义是套住脚和小腿的一只长袜；商店在 stocking shelves，才是在往架上备货。',
 '长袜名接旧 stock 腿部覆盖物，与更早 stocu 袖等词形有关，和 stocc 木干词族的联系、命名动机有讨论。不是库存 stock 加 -ing 就直接长出袜子。',
 [['旧 stock〔腿部覆盖物〕，更早联系 stocu〔袖〕等','与树干词族的深层关系及具体动机有讨论'],['stocking〔衣物名〕；另有 stock 动词 + -ing','长袜；另一用法是正在备货']],
 'a pair of stockings 一双长袜，a Christmas stocking 圣诞袜，in stocking feet 只穿袜子没穿鞋。',
 'a pair of stockings；a Christmas stocking；in stocking feet。',
 'stocking 一只可数，stockings 一双或多只；tights 常连腰裤袜，与两只分开的长袜不完全相同。',
 ('The children hung their stockings beside the fireplace.','孩子们把圣诞袜挂在壁炉旁。'),('She walked across the room in stocking feet.','她只穿袜子，走过房间。'),sources=['https://www.etymonline.com/word/stocking','https://en.wiktionary.org/wiki/stocking#English'])
R('B2475','树干旧义与基础、储备、库存、资本分支','STOCK：备着的一份基础；不同复合选不同支线','stock → restock、overstock；股票接 broker、holder；原料接 feed，身材 stocky 与衣物 stocking 另说明历史。',
 '旧树干词发展出支撑、来源、储备等多义，具体中间线索并非全确定。stocking 是旧衣物词演变，不强当库存动作。冷门职业、机械部件先略。',
 're-/over- + stock；stock + broker/holder/-y；feed/live + stock；stocking 旧衣物支线；stockpile、stockroom 已精讲。',
 [['基本库存与补货','stock · restock · overstock · stockroom · stockpile'],['资本与原料、动物','stockbroker · stockholder · feedstock · livestock'],['形象与旧衣物支线','stocky · stocking']],
 'restock 补货、take stock 盘点；overstock 不等于 oversell；stockholder 股东与 stakeholder 利益相关者；stocking 长袜不能按库存猜。',
 'The shop took stock before deciding what to restock.\n\n商店先盘点，再决定补哪些货。',
 'stock restock overstock stockroom stockpile stockbroker stockholder feedstock livestock stocky stocking')
SO=[['拉丁 sors、sortem；sortīrī','分配到的一份、类别；分配、抽签、选择'],['法语 sorte、sortir → 英语 sort','种类；按类别安排 → 整理、排序、处理好']]
W('sort','英 /sɔːt/；美 /sɔːrt/','种类；分类、排序；整理、解决',
 '先分清是哪个类，再把同类放一起、按顺序排；乱事也像把一堆东西理顺。',
 '名词借法语 sorte，动词有法语 sortir 的历史，最终接拉丁份额、类别词族。现代 sort out 把问题理顺，不只是排数字。',SO,
 'a sort of cake 一种蛋糕，sort by date 按日期排，sort clothes 分类衣物，sort out a problem 解决问题；sort of 口语还可有点、大概。',
 'a sort of；sort by；sort out；sort of。',
 'sort 分类与 arrange 排布有重合；sort of tired 是有点累，不是在分类疲劳。resort 度假地、求助等另有历史，不能按 re- + sort 直接猜。',
 ('Sort the files by date.','按日期给文件排序。'),('We need to sort out the misunderstanding.','我们需要把误会澄清。'),sources=['https://www.etymonline.com/word/sort','https://en.wiktionary.org/wiki/sort#English'])
W('sorter','英 /ˈsɔːtə/；美 /ˈsɔːrtər/','分类者；分拣机、分类工具',
 '把混在一起的信、包裹、硬币等按条件分开的主体，可以是人，也可以是机器、算法。',
 'sort + -er，按执行分类的功能命名。不是比较级更种类。',SO+[['sort + -er → sorter','做分拣、分类或排序的主体']],
 'a mail sorter 邮件分拣员或机，a coin sorter 硬币分类器，a parcel sorter 包裹分拣机。',
 'a mail sorter；a coin sorter；a parcel sorter。',
 'sorter 是主体、工具，sorting 是过程；不因 -er 就限定必须是人。',
 ('The coin sorter separates coins by size.','硬币分类器按尺寸分开硬币。'),('She worked as a mail sorter during the holidays.','假期里她做邮件分拣员。'))
R('B3402','类别、归类与把事情理顺','SORT：知道哪一类，再把同类和顺序排清','sort 先名词、动词、口语结构，再接 sorter 的人或工具。',
 '法语类别、分配词借入，最终有拉丁份额背景。现代 sort out 解决和 sort of 程度口语各有固定结构。',
 'sort → sorter；sort out、sort of 是短语结构。',
 [['类别、动作与主体','sort · sorter']],
 'sort by 按某条件排序；sort out 理顺；sort of 有点；sorter 不只人。',
 'The sorter helps sort the letters into different groups.\n\n分拣工具帮助把信件分成不同类别。',
 'sort sorter')
DE=[['拉丁 dēfīnīre → dēfīnītus','划定界线 → 已界定、确定'],['英语 definite','明确、确定 → 副词 definitely；否定 indefinite']]
W('definite','/ˈdefɪnɪt/','明确的；确定的；有清楚界限的',
 '原来模模糊糊，现在边界或答案定下来了：哪个时间、哪个计划，能说清。',
 '借拉丁 dēfīnītus，dēfīnīre 的分词，与 define 同族。根意像把边界画清，不把 -ite 套成所有矿物名后缀。',DE,
 'a definite answer 明确答复，a definite date 确定日期，a definite improvement 明显改善；the definite article 语法定冠词。',
 'a definite answer；a definite date；a definite improvement。',
 'definite 确定、明确，definitive 常最终权威、定论性的；拼写相近但语气和搭配不同。',
 ('We need a definite date for the move.','我们需要确定搬迁日期。'),('There has been a definite improvement in the writing.','写作有了明显进步。'))
W('definitely','/ˈdefɪnɪtli/','肯定地；明确地；当然',
 '不是也许，而是说话者明确表态“确定，就是这样”。',
 'definite + -ly，保持 definite 的拼写。日常加强肯定语气，也可单独回答 Definitely!。',DE+[['definite + -ly → definitely','明确、毫无疑问地']],
 'definitely agree 完全肯定同意，definitely not 肯定不，I will definitely come 我一定来。',
 'definitely agree；definitely not；Definitely!。',
 'definitely 肯定与 defiantly 反抗地不是同词；避免拼成 definately。说话肯定不自动使内容成为事实。',
 ('I will definitely call you tomorrow.','我明天一定打给你。'),('That is definitely not the file I sent.','那肯定不是我发的文件。'))
W('indefinite','/ɪnˈdefɪnɪt/','不确定的；未限定的；期限未定的',
 '边界、时间或具体对象还没划清，有时就是不知道要持续到什么时候。',
 '接晚期拉丁 indēfīnītus，现代可分析 in- 不 + definite。它否定确定界限，不等于每次都是无限、永远。',DE[:1]+[['晚期拉丁 in- + dēfīnītus → indefinite','没有被明确界定、确定的']],
 'an indefinite period 一段期限未定的时间，indefinite leave 期限未定的离开，an indefinite article 语法不定冠词。',
 'an indefinite period；for an indefinite time；the indefinite article。',
 'indefinite 未规定终点，不保证 infinite 无限；计划尚未定可稍后确定。语法 indefinite article 是 a/an 的类别称呼。',
 ('The event was postponed for an indefinite period.','活动延期，期限未定。'),('They have only an indefinite idea of the cost.','他们对费用只有个模糊概念。'))
R('B3579','界定、确定与未定；明确肯定的副词','DEFINITE：边界答案定下；INDEFINITE：还没明确','define 已精讲，接 definite → definitely，再对照 indefinite；冷门缩略 deffo 先略。',
 '拉丁界定动词分词形成 definite，否定形容词也有自己的拉丁借入支线。明确界线的画面同时帮助学时间和语法术语。',
 'define 相关拉丁分词 → definite → definitely；拉丁否定 indēfīnītus → indefinite。',
 [['界定与确定','define · definite · definitely'],['未界定、未确定','indefinite']],
 'definitely 非 defiantly；indefinite 非必然 infinite；definite 与 definitive 有别。',
 'We definitely need a definite answer rather than an indefinite delay.\n\n我们确实需要明确答复，而不是期限未定的拖延。',
 'define definite definitely indefinite')
if __name__=='__main__':save('continuation_20261030_aj',ROOTS,WORDS)
