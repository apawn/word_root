"""Cell, cellular, raise and awesome: structures, causation and everyday praise."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
CE=[['拉丁 cella → 旧英语、法语等 → cell','小房间、隔间'],['现代 cell','牢房；细胞；电池单元；网络区域、组织小组等小单元']]
W('cell','/sel/','细胞；单人牢房、小室；电池单元；网络、组织的小单元',
 '先想到分出来的一个小房间，再看一个系统里分出来的小单元；身体、通信、电池各有专门用法。',
 '接拉丁 cella 小房间、隔间，英语旧形后来又受法语影响。生物学早期借微小隔间形象命名，其他领域也各自借用，不是牢房里的东西都变成细胞。',CE,
 'a prison cell 牢房，a blood cell 血细胞，a solar cell 太阳能电池单元，cell division 细胞分裂。',
 'a prison cell；a blood cell；a solar cell；cell division。',
 'cell 单元，battery 日常电池可包含一个或多个电化学单元；cell 和 sell 卖常同音，但来源不同。',
 ('The microscope revealed several living cells.','显微镜下可以看到几个活细胞。'),('The prisoner returned to his cell.','囚犯回到了牢房。'),sources=['https://www.etymonline.com/word/cell','https://en.wiktionary.org/wiki/cell#English'])
W('cellmate','/ˈselmeɪt/','同牢房的囚犯；狱友',
 '不只在同一座监狱，而是与另一个人共用同一间牢房。',
 'cell 牢房 + mate 同伴，按共同所在空间命名，和 roommate 室友结构相似。',CE+[['cell + mate → cellmate','共享牢房的人']],
 'his cellmate 他的同牢狱友，a former cellmate 曾经的同牢狱友。',
 'his cellmate；a former cellmate；share a cell with a cellmate。',
 'cellmate 具体共享牢房，fellow prisoner 只说明同为囚犯；这里 cell 不取生物细胞义。',
 ('He shared his food with his cellmate.','他与同牢房的狱友分享食物。'),('The memoir describes conversations with a former cellmate.','回忆录写到了与一位从前同牢狱友的谈话。'))
CU=[['拉丁 cella → cellula','小房间 → 小室的小称形式'],['新拉丁 cellulāris → cellular','细胞、小单元相关的；不是英语 cell 临时加 -ular 的唯一历史']]
W('cellular','英 /ˈseljələ/；美 /ˈseljələr/','细胞的；由小单元组成的；蜂窝移动通信的',
 '先看组成系统的小单元：生物里是细胞，移动通信里是分区覆盖的网络单元。',
 '借新拉丁 cellulāris，接 cellula 小室、细胞 + -āris。与 cell 同接拉丁小室词系，但借入链有别；通信义按网络划分成 cells 命名。',CU,
 'cellular structure 细胞结构，cellular activity 细胞活动，a cellular network 蜂窝移动网络，cellular data 移动数据。',
 'cellular structure；cellular activity；a cellular network；cellular data。',
 'cellular data 通常手机移动网络数据，不是手机里拍到的细胞照片；生物 cellular 与通信 cellular 由所指对象区分。',
 ('The course introduces basic cellular structures.','课程介绍基础细胞结构。'),('She turned off cellular data while using Wi-Fi.','连接 Wi-Fi 时，她关闭了移动数据。'),sources=['https://www.etymonline.com/word/cellular','https://en.wiktionary.org/wiki/cellular#English'])
R('B2953','小隔间与系统单元；牢房、细胞、电池与网络','CELL：分出来的小房间；也借指系统里的小单元','cell → cellmate 接牢房；cellular 同源旁支，supercell 既有精讲共享；celled 常带限定的组合形式暂略。',
 '各学科借用小单元形象，不把它们编成牢房依次变电池、再变身体细胞的单线。',
 'cell 接拉丁 cella；cell + mate；super- + cell；cellula → cellular 为同源旁支。',
 [['小室与同住者','cell · cellmate'],['相关小单元和既有词','cellular · supercell']],
 'cellmate 同牢房不只同监狱；cell/sell 同音不同源；cellular 生物与移动通信按场景分。',
 'The word cell can name a small room or a basic unit in a larger system.\n\ncell 既能指小房间，也能指较大系统中的基本单元。',
 'cell cellmate cellular supercell')
R('B4459','细胞、小单元的形容词；数量、内外和层次分组','CELLULAR：由细胞或小单元组成、与它们相关','cell、cellular 先读；unicellular/multicellular 比数量，intracellular/extracellular/intercellular 比位置，subcellular 比层级。',
 '大量已有细胞组合词复用精讲，按意义重新组织。不把肝细胞等偏专门扩展全塞进来。',
 'cellula + -āris → cellular；uni-/multi-/intra-/extra-/inter-/sub- + cellular。',
 [['基本形容词','cell · cellular'],['数量','unicellular · multicellular'],['位置与层次','intracellular · extracellular · intercellular · subcellular']],
 'intra- 内、extra- 外、inter- 之间；uni-/multi- 数量；sub- 低于细胞层级。hepatocellular 专门词暂略。',
 'The diagram contrasts intracellular structures with the extracellular space.\n\n图示对照了细胞内结构与细胞外空间。',
 'cell cellular unicellular multicellular intracellular extracellular intercellular subcellular')
RA=[['古诺尔斯语 reisa → 中古英语 raisen、reysen → raise','使升起；与 rise 的日耳曼使动同族形式相关'],['现代 raise','抬高、增加；提出；筹集；抚养、饲养']]
def A(f,m):return RA+[[f,m]]
W('raise','/reɪz/','举起、提高；提出；筹集；抚养、饲养',
 '让原来低的升高，或把问题带到大家眼前；把孩子养大、把资金凑起来也各有固定搭配。',
 '经中古英语借北欧 reisa，与 rise 的旧使动同族形式相连。现代规则变化 raised，不是 rise 的过去式；不是每个义都要逐字译成抬起来。',RA,
 'raise your hand 举手，raise prices 提价，raise a question 提出问题，raise money 筹款，raise children 养育孩子。',
 'raise your hand；raise prices；raise a question；raise money；raise children。',
 'Prices rise 自己上涨，The shop raises prices 店家提价。raise 常直接接被提升、提出、养育的对象；rose 是 rise 的过去式。',
 ('Please raise your hand if you have a question.','有问题请举手。'),('The event raised money for the local library.','活动为当地图书馆筹到了钱。'),sources=['https://www.etymonline.com/word/raise','https://en.wiktionary.org/wiki/raise#English'])
W('raising','/ˈreɪzɪŋ/','抬高、增加；筹集；养育；raise 的 -ing 形式',
 '把 raise 的动作看成过程；raise 什么，就决定是提价、筹钱还是养孩子。',
 'raise 去 e + -ing，中古英语已有 reysynge 等活动名词。拼写、词性改变不取消基础动词多种搭配。',A('raise + -ing → raising','提升、提出、筹集或养育的活动'),
 'raising children 养育孩子，raising funds 筹集资金，the raising of a flag 升旗。',
 'raising children；raising funds；the raising of a flag。',
 'raising 使对象增加、成长，rising 自己上升；raising prices 提价，rising prices 正在上涨的价格。',
 ('Raising children takes patience.','养育孩子需要耐心。'),('The team is raising funds for new equipment.','团队正为新设备筹集资金。'))
W('raiser','英 /ˈreɪzə/；美 /ˈreɪzər/','提升、筹集、饲养者或器具〔常在组合中〕',
 '按 raise 的动作称执行者：养某类动物的人，或把东西抬高的工具；通常需要前面的对象来讲清。',
 'raise + -er。单独 raiser 的信息常不完整，实际多见 cattle raiser 等组合和 fundraiser 复合词。',A('raise + -er → raiser','执行提高、养育或筹集的人、器具'),
 'a cattle raiser 养牛者，a sheep raiser 养羊者；fundraiser 已有精讲。',
 'a cattle raiser；a sheep raiser；a livestock raiser。',
 'raiser /reɪzə/ 动作者，razor /reɪzə/ 剃刀在许多口音同音但不是同一个词；raising 不同于 rising。',
 ('The cattle raiser checks the herd every morning.','养牛者每天早上查看牛群。'),('The region has many sheep raisers.','这个地区有许多养羊者。'))
R('B3727','使升高、提出、筹集和养育；与 rise 对照','RAISE：让对象上来、增加或成长','raise → raising、raiser；fundraise 已有共享，保留原词逆构说明；重点对照刚写的 rise。',
 '借入北欧使动形式，与本族 rise 有历史联系但现代句型不同。筹款、养育不能只靠中文提高猜宾语。',
 'raise—raised—raised；raise + -ing/-er；fundraise 可能由 fundraising 逆构。',
 [['动作、活动和执行者','raise · raising · raiser'],['筹集资金','fundraise']],
 'raise 使升、rise 自升；raising prices 提价、rising prices 涨价中的价格；raiser 与 razor 多口音同音不同词。',
 'Raising funds helped the school raise the standard of its equipment.\n\n筹集资金帮助学校提高了设备水平。',
 'raise raising raiser fundraise')
AW=[['awe 敬畏 + -some → awesome','让人敬畏、惊叹的'],['现代口语 awesome','太棒、非常好；旧敬畏义仍存在']]
W('awesomeness','英 /ˈɔːsəmnəs/；美 /ˈɔːsəmnəs/〔部分口音 /ˈɑː-/〕','惊人、了不起的特质；超棒之处〔口语〕',
 '把让人赞叹、觉得太棒的那一面作为名词来夸；现代常是轻松夸张。',
 'awesome + -ness。旧敬畏与现代超棒两路都可能，日常多数语境靠评价语气理解，不等于正式量化指标。',AW+[['awesome + -ness → awesomeness','令人赞叹、很棒的性质']],
 'the awesomeness of the view 景色的壮观，pure awesomeness 简直太棒了。用在正式报告中常显得口语化。',
 'the awesomeness of；pure awesomeness；an example of awesomeness。',
 'awesome 形容很棒，awesomeness 名词说很棒这个特点；不把 -ness 当新的赞叹程度比较级。',
 ('The children were amazed by the awesomeness of the waterfall.','孩子们被瀑布的壮观震撼了。'),('She described the whole concert as pure awesomeness.','她说整场音乐会简直棒极了。'))
W('awesomely','英 /ˈɔːsəmli/；美 /ˈɔːsəmli/〔部分口音 /ˈɑː-/〕','极其、令人惊叹地；特别棒地〔多口语〕',
 '把赞叹放到另一个特点前：极其厉害、壮观得惊人；也可夸事情做得很棒。',
 'awesome + -ly，形容词转副词。现代作程度加强时很口语，旧令人敬畏的感觉仍可存在。',AW+[['awesome + -ly → awesomely','令人敬畏、惊叹地；口语程度加强']],
 'awesomely powerful 极其强大，awesomely good 好得惊人，awesomely beautiful 美得惊人。',
 'awesomely powerful；awesomely good；awesomely beautiful。',
 'awesomely 常积极赞叹或强调震撼，awfully 常极其，也可非常糟地；同接 awe 的历史不保证现代语气一样。',
 ('The storm was awesomely powerful.','风暴的力量惊人。'),('The band played awesomely well.','乐队演奏得特别棒。'))
R('B4595','引人敬畏、惊叹到口语赞叹','AWESOME：原本令人敬畏，今天也常说太棒','已有 awesome → awesomeness、awesomely，按形容词、性质名词、方式程度副词连读。',
 '和 awful 同有 awe 背景，现代评价却常不同，不能只按同源就把两个词都译成糟糕或敬畏。',
 'awe + -some → awesome；awesome + -ness/-ly。',
 [['赞叹、性质与程度','awesome · awesomeness · awesomely']],
 'awesomeness 名词特点、awesomely 副词；awesome/awful 同有历史联系但现代语气不一。',
 'The awesome performance was awesomely energetic.\n\n那场精彩表演精力充沛得惊人。',
 'awesome awesomeness awesomely')
if __name__=='__main__':save('continuation_20261030_bj',ROOTS,WORDS)
