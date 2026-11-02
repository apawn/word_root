"""Wish and bank: desire, customary wishbone and distinct bank histories."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
WISH=[['古英语 wȳsċan → 中古英语 wisshen → wish','希望、想要'],['现代 wish','愿望、祝愿；也可说与事实相反的期待']]
W('wish','/wɪʃ/','希望；但愿；祝愿；愿望',
 '心里想让某件事变成真的；可以是生日祝愿，也可以是明知现实不同、还是忍不住盼它另一种样子。',
 '继承古英语 wȳsċan 希望。现代名词、动词都常用，wish 从愿望发展出祝愿、遗憾等固定句型。',WISH,
 'make a wish 许愿，wish you luck 祝你好运；I wish I knew 是现在不知道但希望知道。wish to do 较正式地说想做。',
 'make a wish；wish you luck；wish to do；I wish I could。',
 'hope 常期待有可能实现的事，wish 常用于祝愿或与事实不同的想法；I wish I knew 中 knew 不必说过去某天知道。',
 ('Close your eyes and make a wish.','闭上眼睛，许个愿吧。'),('I wish I had more time to read.','但愿我有更多时间看书。'))
W('wishful','/ˈwɪʃfəl/','抱有愿望的；一厢情愿的',
 '很想结果如自己所愿，甚至可能把想要当成了会发生。最常见在 wishful thinking。',
 'wish + -ful，充满愿望。现代固定搭配 wishful thinking 尤其突出受愿望驱动、缺乏现实依据的想法。',WISH+[['wish + -ful → wishful','满怀愿望 → 一厢情愿的']],
 'wishful thinking 一厢情愿，a wishful look 渴望的眼神；并不是所有 wishful 都必须译成愚蠢。',
 'wishful thinking；a wishful look；mere wishful thinking。',
 'hopeful 有希望或抱希望，wishful thinking 往往批评把愿望当事实；语气不能简单等同乐观。',
 ('Expecting the project to finish tomorrow is wishful thinking.','指望项目明天完成，只是一厢情愿。'),('He gave the last piece of cake a wishful look.','他渴望地望了一眼最后那块蛋糕。'))
W('wishbone','/ˈwɪʃbəʊn/；美 /ˈwɪʃboʊn/','鸟类叉骨；叉形结构',
 '鸡、火鸡等胸前一块像 Y 的骨头；名字来自两个人拉断它、借此许愿的习俗。',
 'wish 许愿 + bone 骨头，按拉叉骨许愿的习俗命名。相似形状也借用于机械结构，不是骨头自己产生愿望。',WISH+[['wish + bone → wishbone','许愿习俗中的叉骨 → 叉形物']],
 'a chicken wishbone 鸡叉骨，break the wishbone 拉断叉骨；a wishbone suspension 是汽车悬架的叉臂式结构名称。',
 'a chicken wishbone；break the wishbone；a wishbone shape。',
 'wishbone 是骨头的特定名称，backbone 是脊骨；两者形状、部位都不同。',
 ('They saved the turkey’s wishbone after dinner.','晚饭后，他们留下了火鸡的叉骨。'),('The metal support has a wishbone shape.','这个金属支架呈叉骨形。'),sources=['https://www.etymonline.com/word/wishbone','https://en.wiktionary.org/wiki/wishbone#English'])
R('B3949','愿望、祝愿与一厢情愿','WISH：心里想让它成真','先分愿望与祝愿，再读 wishful thinking 的一厢情愿；wishbone 连接真实民俗。',
 'wish 是古英语继承词。现代句型里与事实相反的愿望很常用，别只停在希望这个中文词。',
 'wish → wishful；wish + list → wishlist；wish + bone → wishbone。',
 [['基本愿望与态度','wish · wishful'],['清单与习俗物件','wishlist · wishbone']],
 'I wish I knew 表现在不知道；wishful thinking 通常含缺少现实根据的评价。',
 'I wish I could finish everything on my wishlist this year.\n\n但愿我今年能完成心愿清单上的所有事情。',
 'wish wishful wishlist wishbone')
BA=[['法语 banque ← 意大利语 banca 等','兑换钱的柜台、桌凳 → 银行'],['英语 bank 的另一路地形词','河岸、土坡、堆积；属日耳曼相关词族，路线与金融义分开'],['现代 bank','金融机构；河岸；储存资源的库等']]
W('bank','/bæŋk/','银行；河岸；资源库；把钱存入；依赖',
 '先把银行和河岸分开。银行接收、管理钱，后来储存别的资源的库也借它命名；河岸不是银行搬到河边才来的意思。',
 '金融义经法语 banque 接意大利语 banca 柜台、桌凳，联系兑换钱的工作台。地形义接另一日耳曼词族路线，历史上彼此可能有远缘联系，但英语中不能把河岸说成金融义的直接扩展。',BA,
 'a bank account 银行账户，the river bank 河岸，a blood bank 血库；bank on someone 指依靠、指望某人，bank money 是存钱。',
 'a bank account；on the river bank；a blood bank；bank on。',
 'bank 金融机构与 bank 河岸须按上下文选；bank on 不按字面译成在银行上面。',
 ('We sat on the bank and watched the boats.','我们坐在岸边看船。'),('You can bank on her to keep her promise.','你可以相信她会信守承诺。'))
W('banker','英 /ˈbæŋkə/；美 /ˈbæŋkər/','银行家；银行业从业者',
 '以银行业务为职业的人；具体可以是经营、管理或专业服务，不只银行的所有者。',
 '金融 bank + -er，历史也受法语 banquier 对应词影响。另有地形等同形用法，先掌握银行从业者义。',BA[:1]+[['bank + -er → banker','从事银行工作的人']],
 'an investment banker 投资银行从业者，a private banker 私人银行业务人员；实际职位再由修饰语限定。',
 'an investment banker；a private banker；a former banker。',
 'banker 不等于每一位坐柜台的 cashier 出纳、收银员，也不自动是银行老板。',
 ('She worked as an investment banker before starting her company.','她创办公司前曾在投资银行业工作。'),('The banker explained the available account options.','银行工作人员解释了可选的账户类型。'))
W('bankable','/ˈbæŋkəbəl/','有赚钱把握、能带来收入的；银行可接受的',
 '觉得这名字、项目或东西有足够把握带来钱，所以商业上敢依赖它。',
 'bank + -able，可被银行接受、承兑等金融用法在先，再扩展为能保证商业收益、票房的评价。',BA[:1]+[['bank + -able → bankable','银行可接受 → 商业上有收入把握的']],
 'a bankable star 有票房号召力的明星，a bankable idea 有商业前景的点子；这是商业评价，不是绝对盈利保证。',
 'a bankable star；a bankable name；a bankable project。',
 'bankable 常说卖得动、能吸引资金，talented 说有才华；有才华与商业号召力不是同一个判断。',
 ('The studio wanted a bankable star for the leading role.','制片公司想请一位有票房号召力的明星担任主演。'),('They needed to turn the idea into a bankable project.','他们需要把想法变成一个有商业吸引力的项目。'))
W('banknote','英 /ˈbæŋknəʊt/；美 /ˈbæŋknoʊt/','钞票；纸币',
 '手里那张代表一定金额的票子；note 在这里是有金额、承诺或价值凭据背景的票据。',
 'bank 银行 + note 票据，按银行发行的票据命名，现代泛指钞票。不是银行工作人员记的一张便签。',BA[:1]+[['bank + note → banknote','银行票据 → 钞票']],
 'a ten-pound banknote 十英镑钞票，a counterfeit banknote 假钞；不同地区也常直接说 note 或美式 bill。',
 'a ten-pound banknote；a counterfeit banknote；a damaged banknote。',
 'banknote 是钞票，bank statement 银行对账单；两者都是纸张或记录，却不是同一种金融物件。',
 ('The machine rejected the damaged banknote.','机器拒收了那张破损钞票。'),('The exhibition includes banknotes from different countries.','展览包含不同国家的钞票。'))
W('databank','/ˈdeɪtəbæŋk/，data 的读音可有口音差别','数据库；数据资料库',
 '把数据集中存放起来，像银行集中保管钱，方便以后查找、使用。',
 'data 数据 + bank 储存资源的库。这里 bank 是资源储存的扩展义，不要求由银行机构经营。',BA[:1]+[['data + bank → databank','集中储存数据的库 → 数据资料库']],
 'a research databank 研究数据资料库，a genetic databank 遗传数据资料库；data bank 分写也可见。',
 'a research databank；a national databank；a central databank。',
 'databank 与 database 常有重合，databank 更突出集中资料储存；名字本身不规定具体数据库软件或数据模型。',
 ('The researchers added the results to a shared databank.','研究人员把结果加入共享数据资料库。'),('The databank contains records from several decades.','这个资料库收录了数十年的记录。'))
W('riverbank','英 /ˈrɪvəbæŋk/；美 /ˈrɪvərbæŋk/','河岸',
 '沿着河水两边的陆地边缘，可以坐在上面看水流过去。',
 'river 河 + bank 岸、土坡。bank 在这里接地形词族，不是存钱的银行。',BA[1:2]+[['river + bank → riverbank','河的岸边 → 河岸']],
 'on the riverbank 在河岸上，along the riverbank 沿河岸；river bank 分写也常见。',
 'on the riverbank；along the riverbank；a steep riverbank。',
 'riverbank 陆地岸边，riverbed 河床是承载水流的底部；bank branch 则是银行分行。',
 ('We followed a path along the riverbank.','我们沿着河岸小路前行。'),('Children watched ducks from the riverbank.','孩子们在河岸上看鸭子。'))
W('sandbank','/ˈsændbæŋk/','沙洲；水中的沙坝、沙脊',
 '水里或岸边积起来的一片沙，形成比周围高的区域；水位低时可能露出来。',
 'sand 沙 + bank 堆积的地形，组合成沙洲、沙坝。bank 这一路有堆积、高起之地的画面。',BA[1:2]+[['sand + bank → sandbank','沙的堆积高地 → 沙洲、沙坝']],
 'a sandbank in the river 河中沙洲，run aground on a sandbank 在沙洲搁浅；不一定每座沙洲都常年高出水面。',
 'a shifting sandbank；a river sandbank；run aground on a sandbank。',
 'sandbank 是沙堆积的地形，riverbank 是河两边陆地；沙洲可以位于河道中央。',
 ('A sandbank appeared as the tide went out.','退潮时，一片沙洲露了出来。'),('The boat ran aground on a sandbank.','船在一片沙洲上搁浅了。'))
R('B2484','银行、资源库；另一路的河岸与堆积地形','BANK：先分金融柜台与地形岸坡','银行词族从兑换钱的柜台讲起，河岸词族按地形讲；同形并不要求同一条直接演化链。',
 '金融义经法语、意大利语的柜台词进入英语；河岸义走日耳曼地形词族路线。现代资源库借银行的集中储存功能。',
 'bank → banker、bankable；bank + note → banknote；data + bank → databank；river、sand + 地形 bank → riverbank、sandbank；共享 interbank。',
 [['金融机构与从业者','bank · banker · bankable · banknote · interbank'],['储存资源的扩展','databank'],['地形分支','riverbank · sandbank']],
 'bankable 商业上有吸引力不等于绝对保证盈利；bank on 是依靠；riverbank 河岸与 banknote 钞票分历史来源读。',
 'The old bank building stands near the riverbank.\n\n那座旧银行建筑位于河岸附近。',
 'bank banker bankable banknote interbank databank riverbank sandbank')
if __name__=='__main__':save('continuation_20261029_dw',ROOTS,WORDS)
