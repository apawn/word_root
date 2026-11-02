"""Choirmasters, scrubbing, readjustment, mosques, worthiness, margins and exploits."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()

Ch=[['choir 合唱团 + master 主持、掌管者','按职责指合唱团音乐负责人'],['参照德语 Chormeister → choirmaster','排练、指挥等职责的复合名称']]
W('choirmaster','英 /ˈkwaɪəmɑːstə/；美 /ˈkwaɪərmæstər/','合唱团指挥、合唱指导',
 'choir 是合唱团，choirmaster 是带大家排练、把各声部合到一起的音乐负责人。master 在这里看职责，不必按学校校长翻译。',
 'choir + master，参照德语 Chormeister 的复合结构。英语各部分本已有词，组合命名合唱团的音乐指导角色。',Ch,
 'the cathedral choirmaster 主教座堂合唱指挥；rehearse with the choirmaster 跟合唱指导排练。',
 'a choirmaster；the cathedral choirmaster。',
 'chorister 是合唱团成员，choirmaster 是音乐负责人；两者分工不同。',
 ('The choirmaster asked the singers to repeat the final phrase.','合唱指挥请歌手们重唱最后一句。'),('She worked as a choirmaster for many years.','她多年担任合唱指导。'))
R('B2533','合唱整体、歌唱成员与音乐负责人','CHOIR：许多声音合在一起，成员与指挥职责分开','choir → chorister、choirmaster；成员词、负责人词各看形成历史。',
 'choir 是整体，chorister 是唱的人，choirmaster 是带排练、指挥的人。拼写不完全对应现代机械相加，基础词条保留各自借入史。',
 'choir、chorister 同接合唱相关古典、法语材料；choir + master 参照德语 Chormeister。',
 [['合唱整体、成员与指导','choir · chorister · choirmaster']],
 'choir 开头读 /kw/，完整词有 /kwaɪə/ 等读法；按完整音标记，不拆字母逐个拼。',
 'The choirmaster gathered the choristers before the choir rehearsal.\n\n合唱指导在合唱团排练前召集歌手。','choir chorister choirmaster')

Sc=[['中古荷兰语 schrobben → 中古英语 scrobben → scrub 擦洗','用力摩擦、刷洗'],['古英语 scrybb 等 → shrub 的变体 scrub 灌木','擦洗与低矮灌木近源不同，各有派生']]
W('scrub','/skrʌb/','用力擦洗；取消、删去；低矮灌木丛；〔复数〕手术服',
 '顽固污渍不是轻轻冲掉，而是拿刷子来回用力刷，是 scrub。scrubland 的 scrub 却是低矮灌木；手术服 scrubs 则联系手术前清洁等医疗场景。',
 '擦洗义借中古荷兰语 schrobben，经中古英语 scrobben；删除、取消等借擦掉的动作扩展。灌木义承古英语相关形式，近接 shrub 的变体。两支不编成洗完地面只剩灌木。',Sc,
 'scrub the floor 刷地；scrub off a stain 擦掉污渍；scrub a launch 取消发射；wear scrubs 穿手术服。',
 'scrub the floor；scrub off；wear scrubs。',
 'scrub 强调摩擦力度，rinse 强调冲洗；scrub 的灌木义与 clean 清洁不是同一路线。',
 ('She scrubbed the muddy boots with a brush.','她用刷子用力刷洗沾泥的靴子。'),('Low scrub covered the dry hillside.','低矮灌木覆盖着干燥山坡。'),sources=['https://en.wiktionary.org/wiki/scrub#English','https://www.etymonline.com/word/scrub'])
W('scrubbing','/ˈskrʌbɪŋ/','用力擦洗；清洗、净化；scrub 的 -ing 形式',
 '一遍遍来回刷的活动叫 scrubbing。工业里把杂质从气体等介质中除去，也借清洗动作命名，具体设备不必像家用刷子。',
 'scrub 擦洗 + -ing，双写 b → scrubbing。动作名可用于表面清洁，也可用于去除杂质的专门过程。',Sc[:1]+[['scrub + -ing → scrubbing','擦洗活动；相应清理、净化过程']],
 'give something a good scrubbing 彻底刷洗；floor scrubbing 地板刷洗；gas scrubbing 气体净化。',
 'a good scrubbing；floor scrubbing。',
 'scrubbing 动作名与 scrubland 地名不同；后者接的是灌木支。',
 ('The pan needed a good scrubbing.','这口锅得好好刷一刷。'),('The machine reduced the time spent on floor scrubbing.','机器减少了刷地所花的时间。'))
W('scrubbed','/skrʌbd/','擦洗过的；删除、取消了的；scrub 的过去式、过去分词',
 'scrubbed floors 是已经刷洗的地板；a scrubbed plan 可以是被取消的计划。一个看刷洗结果，一个接擦掉、取消的比喻。',
 'scrub + -ed，双写 b → scrubbed，ed 读 /d/。常用过去、分词承擦洗及取消等动词用法；另有低矮生长的旧形容义，按具体语境另读。',Sc[:1]+[['scrub + -ed → scrubbed','刷洗过；删掉、取消的过去或结果']],
 'freshly scrubbed floors 刚刷净的地板；scrubbed from a list 从名单删去；the event was scrubbed 活动取消。',
 'freshly scrubbed；scrubbed from the list。',
 'scrubbed 不保证物件无菌，只说明经历了所说的擦洗或处理；sterile 是另一个性质。',
 ('The freshly scrubbed floor gleamed.','刚刷净的地板闪着光。'),('The old entry was scrubbed from the list.','旧条目被从名单中删掉了。'))
W('scrubber','英 /ˈskrʌbə/；美 /ˈskrʌbər/','擦洗工具、机器；清洗人员；气体净化装置',
 'scrub 是刷洗，scrubber 是负责刷、净化的人或工具。洗锅擦、地面洗刷机、去除气体杂质的设备，都按各自清理用途接上这层意思。',
 'scrub + -er，双写 b → scrubber。执行者、工具名从擦洗动作发展到工业净化设备等具体用途。',Sc[:1]+[['scrub + -er → scrubber','刷洗者、清理工具及净化设备']],
 'a floor scrubber 洗地机；a kitchen scrubber 厨房擦洗工具；an exhaust scrubber 废气净化装置。',
 'a floor scrubber；a kitchen scrubber。',
 'scrubber 不一定是刷毛工具；设备可按净化功能命名，结构依具体类型。',
 ('The floor scrubber moved slowly along the corridor.','洗地机沿走廊缓缓前进。'),('She used a soft scrubber on the pan.','她用柔软擦洗工具刷锅。'))
W('scrubby','/ˈskrʌbi/','灌木丛生的；矮小瘦弱的',
 'scrubby hillside 是长着低矮灌木的山坡。它主要接 scrub 灌木这支，再有生长矮小的评价，不是说山坡刚擦得干净。',
 'scrub 灌木 + -y，双写 b → scrubby。表示灌木覆盖、由灌木构成或矮小生长等性质；不能只套擦洗动词来猜。',Sc[1:]+[['scrub 灌木 + -y → scrubby','低矮灌木覆盖、矮小的']],
 'scrubby vegetation 低矮灌丛植被；scrubby hills 灌木山丘；a scrubby tree 矮小树。',
 'scrubby vegetation；a scrubby hillside。',
 'scrubby 是植被、长势描述；scrubbed 常是擦洗结果，两者同开头但分支不同。',
 ('Scrubby vegetation covered the ridge.','低矮灌丛覆盖着山脊。'),('A few scrubby trees grew beside the track.','路旁长着几棵矮小树。'))
W('scrubland','/ˈskrʌblænd/','灌丛地、矮灌木地带',
 'land 是土地，scrub 是低矮灌木。scrubland 就是以这种植被为特征的地带，不是一块被刷洗出来的空地。',
 'scrub 灌木 + land 土地，透明复合名词，按植被类型命名地域。草本、其他植物也可混生，并不要求只剩一种灌木。',Sc[1:]+[['scrub + land → scrubland','以低矮灌丛为主要特征的地带']],
 'dry scrubland 干旱灌丛地；an area of scrubland 一片灌丛地带。',
 'dry scrubland；an area of scrubland。',
 'scrubland 不是绝无生命的荒地；与 forest 等地带名称一样，看主要植被结构。',
 ('The path crossed an area of dry scrubland.','小路穿过一片干燥灌丛地。'),('Small birds sheltered in the scrubland.','小鸟在灌丛地里藏身。'))
R('B3168','用力擦洗与低矮灌木分源，派生词分别成组','SCRUB：刷洗一支，灌木一支，别把地名当擦净的地','scrubbing、scrubbed、scrubber 接擦洗；scrubby、scrubland 接灌木。',
 '刷锅的摩擦动作与山坡灌丛的植被结构互不相同。先分两组，再用后缀看活动、结果、工具、性质和地带。',
 'schrobben → scrobben → 擦洗 scrub；shrub 同族变体 → 灌木 scrub；双写 b 接 -ing、-ed、-er、-y；land 土地。',
 [['擦洗动作、活动、结果与工具','scrub · scrubbing · scrubbed · scrubber'],['灌木性质与地带','scrubby · scrubland']],
 'scrubbed floor 可能刷净，scrubby hillside 则长灌木；scrubber 工业设备按功能命名。',
 'After scrubbing the equipment, they drove across the scrubland.\n\n刷洗设备后，他们驶过低矮灌木丛生的地带。','scrub scrubbing scrubbed scrubber scrubby scrubland')

Ad=[['adjust 调整 → adjustment','调整动作或结果'],['re- 再 + adjustment → readjustment','重新调整，也可指重新适应']]
W('readjustment','/ˌriːəˈdʒʌstmənt/','重新调整；重新适应',
 '第一次调好，条件又变了，需要再调一次，是 readjustment。人回到旧环境却要重新习惯生活节奏，也可谈 readjustment。',
 're- 再 + adjustment，后者为 adjust + -ment。前缀加在整个调整名词前，也与 readjust 动词形成对应。',Ad,
 'a period of readjustment 重新适应期；a readjustment of the schedule 日程重新调整。',
 'a period of readjustment；a readjustment of。',
 'readjustment 不保证完全恢复原状；再调是为了适应现在条件，可能形成新的安排。',
 ('Returning home required a period of readjustment.','回家后需要一段重新适应期。'),('The delay forced a readjustment of the schedule.','延误迫使日程重新调整。'))
R('B2625','调整动作、结果与再调，重新适应也是改变配合','ADJUSTMENT：让安排合适，条件变了就再调','adjustment → readjustment，re- 加入再一次、重新适应的过程。',
 '器具位置、日程与生活方式都可调整。再调整常因条件改变，不等于把所有参数倒回最早版本。',
 'adjust + -ment → adjustment；re- + adjustment → readjustment。',
 [['调整与重新调整','adjustment · readjustment']],
 'readjustment 重新适应不必恢复旧样；adjustment 既可能动作，也可能具体改动。',
 'The first adjustment helped, but a later change required readjustment.\n\n第一次调整起了作用，但后来的变化又要求重新调整。','adjustment readjustment')

Mq=[['阿拉伯语 masjid，联系俯伏礼拜的动词词根','礼拜、叩拜之处的场所名'],['经欧洲语言 moschea、mosquée 等 → 英语 mosque','中介路线有不同阶段，整体是穆斯林礼拜场所名称']]
W('mosque','英 /mɒsk/；美 /mɑːsk/','清真寺',
 '穆斯林共同礼拜的场所是 mosque。最早名称抓住礼拜、俯伏之处，不要求每座建筑外观都必须长着相同的圆顶、尖塔。',
 '经法语 mosquée、意大利语 moschea 等形式，上溯阿拉伯语 masjid 礼拜之处，接与俯伏礼拜有关的词根。欧洲中介路线有不同阶段，不按现代英语 mos + que 硬拆。',Mq,
 'a local mosque 当地清真寺；the prayer hall of a mosque 清真寺礼拜厅。词尾 -que 在此读 /k/，不另起音节。',
 'a local mosque；a mosque’s prayer hall。',
 'mosque 是清真寺，church 常指基督教教堂；建筑圆顶、尖塔本身不能替代宗教场所的具体身份。',
 ('The mosque stands near the old market.','清真寺位于旧市场附近。'),('The book describes the mosque’s prayer hall.','书中描写了清真寺的礼拜厅。'),sources=['https://en.wiktionary.org/wiki/mosque#English','https://www.etymonline.com/word/mosque'])
R('B2723','礼拜场所名随语言传播，不按现代英语字母硬拆','MOSQUE：从礼拜之处的名称，借成清真寺','mosque 是整体借词，核心认用途与宗教场所身份。',
 '建筑外形有地区差异，词源则把注意力放到礼拜地点。阿拉伯语经欧洲语言的传播，使现代拼写与早期形式差别明显。',
 'masjid → 欧洲语言 moschea、mosquée 等 → mosque；词尾 -que 读 /k/。',
 [['礼拜场所与借词历史','mosque']],
 'mosque 不因外形有圆顶就可与任何庙、教堂互换。',
 'The guide explains how the mosque’s name travelled across languages.\n\n讲解说明清真寺这个名称怎样跨语言传播。','mosque')

Cw=[['cringe 尴尬、畏缩相关动作 + -worthy','足以让人产生相应反应'],['cringeworthy','尴尬到令人替别人缩起身子的评价']]
W('cringeworthy','英 /ˈkrɪndʒwɜːði/；美 /ˈkrɪndʒwɜːrði/','令人尴尬得想躲开的；让人替别人难堪的',
 '看别人讲了个全场冷掉的笑话，你自己都忍不住缩肩、别开脸，这种替人难堪的感觉就是 cringeworthy。',
 'cringe + -worthy，保留 e，表示足以使人 cringe。-worthy 在这里提供值得引发某种反应的结构，不是说尴尬内容值得称赞。',Cw,
 'a cringeworthy joke 尴尬笑话；a cringeworthy moment 令人替人难堪的一刻。也常见带连字符拼写。',
 'a cringeworthy joke；a cringeworthy moment。',
 'cringeworthy 带观看者的强烈尴尬评价；awkward 范围更宽，轻微不便也可 awkward。',
 ('The speech included a cringeworthy joke.','讲话里夹着一个让人尴尬的笑话。'),('It was a cringeworthy moment for everyone watching.','那一刻让所有观看的人都替他难堪。'))
R('A1847','值得、足以引发某事，或适合某用途，按词分别看','-WORTHY：值得注意，也能说足以尴尬、适于航海','noteworthy、praiseworthy 看值得的评价；seaworthy 看适合用途；cringeworthy 看引发反应。',
 'worthy 不是每次都褒义。前半指出被值得、可承担的事或引出的反应，组合后的具体含义需与真实用法连接。',
 'worth、worthy 词族 → -worthy；note 注意，news 新闻，praise 赞扬，sea 航海用途，cringe 尴尬反应。',
 [['值得、可靠与适用','trustworthy · noteworthy · newsworthy · praiseworthy · seaworthy'],['足以引起尴尬','cringeworthy']],
 'cringeworthy 不是夸有价值；seaworthy 主要说能适于航海，与值得航海的生硬翻译不同。',
 'The trustworthy report praised a praiseworthy effort and described one cringeworthy mistake.\n\n可信报告赞扬了一项值得称赞的努力，也描述了一个令人尴尬的错误。','trustworthy noteworthy newsworthy praiseworthy seaworthy cringeworthy')

Mg=[['margin 边缘 → marginal','边缘、临界或很小程度的性质'],['marginal + -ly → marginally','稍微、勉强地；较旧也可说在页边']]
W('marginally','英 /ˈmɑːdʒɪnəli/；美 /ˈmɑːrdʒɪnəli/','稍微、略微；勉强地',
 '只比另一项好出一点点，是 marginally better；只是刚过线，是 marginally acceptable。它让你把注意力放在很小的差距上。',
 'marginal + -ly，性质转为程度、方式副词。marginal 的边缘、临界意义走向差别很小、刚够程度等用法。',Mg,
 'marginally better 稍好一点；marginally cheaper 略便宜；marginally acceptable 勉强可接受。',
 'marginally better；marginally cheaper。',
 'marginally 通常小幅度，不是 greatly 大幅；是否重要还取决于场景，不能单凭小差值说没有意义。',
 ('The new model is marginally lighter.','新型号轻了一点。'),('Her second draft was marginally better than the first.','她的第二稿比第一稿稍好一些。'))
R('B4431','边缘与临界程度，副词常聚焦小幅差异','MARGINAL：靠边、刚够，或只差一点点','marginal → marginally；marginalize、marginalization 接使人或事被推到边缘的社会比喻。',
 '边缘位置是一种形象，小幅程度是一种数量判断；被边缘化则是参与、关注、权力等位置的变化。不要把所有 marginal 都译成同一句边缘的。',
 'margin → marginal；-ly 程度、方式；-ize 使处于边缘；-ization 相应过程；sub- 低于或不足的限定。',
 [['边缘性质、小幅程度与低于临界','marginal · marginally · submarginal'],['使边缘化与过程名词','marginalize · marginalization']],
 'marginally better 只说稍好；marginalization 则常说群体、事物被推离中心。',
 'The revised plan was marginally better but still risked marginalizing small groups.\n\n修改后的计划稍好一点，却仍可能把小群体推向边缘。','marginal marginally submarginal marginalize marginalization')

Le=[['拉丁 letum 死亡 → letalis；后有 lethalis 拼写 → lethal','th 拼写受与希腊遗忘词相联系的旧分析影响，不能据此说本来就是同源'],['lethal + -ly、-ity','致命的方式；致死性质、程度']]
W('lethal','/ˈliːθəl/','致命的；足以造成死亡的；〔比喻〕极具打击力的',
 '不是只让人不舒服，而是能导致死亡，是 lethal 的基本强度。体育评论里的 a lethal finisher 则夸选手把机会变成得分的能力，属于有力打击的比喻。',
 '借拉丁 letalis 致命的及后来的 lethalis 拼写，上接 letum 死亡。th 受错误关联希腊 lethe 遗忘的旧拼写分析影响；词义不能倒说成遗忘所以致命。',Le,
 'a lethal combination 致命组合，也可比喻危险组合；a lethal effect 致命作用；a lethal finisher 终结能力强的得分手。',
 'a lethal combination；a lethal effect。',
 'harmful 有害不一定致命；lethal 强调可致死，具体例子的风险仍需看完整条件。',
 ('The fumes can be lethal in an enclosed space.','这些烟气在封闭空间里可能致命。'),('The striker was a lethal finisher.','那位前锋把握得分机会的能力极强。'),sources=['https://en.wiktionary.org/wiki/lethal#English','https://www.etymonline.com/word/lethal'])
W('lethally','/ˈliːθəli/','致命地；〔比喻〕极具打击力地',
 'lethal 是性质，lethally 把致命效果放到动作、状态里。lethally efficient 可以是带夸张的高效打击，不必每次都在叙述死亡事件。',
 'lethal + -ly → lethally，原词末 l 再接 -ly，因此写 ll；读音里仍是正常副词结尾，不把双 l 念成两拍。',Le[:1]+[['lethal + -ly → lethally','以致命、极具打击力的方式']],
 'lethally injured 受致命伤；lethally efficient 高效得可怕、极具打击力，后者需看修辞场景。',
 'lethally injured；lethally efficient。',
 'lethally 不等于 merely severely 严重地；本义里带致死结果或能力，修辞用法另读。',
 ('The story describes a soldier who was lethally injured.','故事写到一名受了致命伤的士兵。'),('The commentator called the team lethally efficient.','评论员说这支队伍效率高得极具杀伤力。'))
W('lethality','/liˈθæləti/','致死能力、致命性；致死程度',
 'lethal 说能致命，lethality 把这种能力、程度单独拿出来比较。它不是直接数现场死了几个人，而是在谈产生致死效果的性质。',
 'lethal + -ity → lethality，重音由前面的 /liː/ 移到 /θæ/ 附近。性质名词在不同研究里可采用不同指标描述，不由词尾自动给定一个比率。',Le[:1]+[['lethal + -ity → lethality','致命的性质、程度或能力']],
 'the lethality of a substance 某物质的致命性；assess lethality 评估致死能力。',
 'the lethality of；assess lethality。',
 'lethality 与 severity 严重程度不完全相同；严重可以指疼痛、破坏等，不一定只看致死。',
 ('The report compares the lethality of the substances under specified conditions.','报告比较这些物质在给定条件下的致命性。'),('The glossary distinguishes lethality from general severity.','词汇表区分致命性与一般严重程度。'))
R('B4060','致死性质、方式与程度，修辞中的打击力另辨','LETHAL：本义达到能致死的强度，名词再谈致死能力','lethal → lethally、lethality，性质、方式、程度按顺序看。',
 '本义比有害、严重更明确地接死亡；体育、竞争中的修辞则借强大打击力。历史 th 拼写不等于最初来自遗忘词。',
 'letum → letalis、lethalis → lethal；-ly 写 ll；-ity 形成 lethality 并改变重音。',
 [['致命性质、方式与程度','lethal · lethally · lethality']],
 'lethal 不等于所有 harmful；lethality 不是脱离条件的固定数值。',
 'The lesson explains lethal effects before introducing the noun lethality.\n\n课程先解释致命作用，再介绍名词致命性。','lethal lethally lethality')

Ex=[['拉丁 explicitum，接 explicare 展开、完成 → 法语 esploit、esploitier','完成、成果、收益，再向利用发展'],['英语 exploit 名词、动词；+ -ative、-able','功绩、利用方法；利用、剥削；剥削性的、可利用的']]
W('exploit','名词 /ˈeksplɔɪt/；动词 /ɪkˈsplɔɪt/','功绩、壮举；利用、开发；剥削；漏洞利用方法',
 '动词 exploit 把资源、机会用起来；若把别人的处境拿来不公平获利，就成了剥削。名词 exploits 则常说精彩事迹，重音还前移；计算机名词又可指利用漏洞的方法、代码。',
 '借法语 esploit、esploitier，上接拉丁 explicitum 与 explicare 展开、完成的材料。成果、收益与完成动作发展为壮举、利用，再有不公平利用的负面支。',Ex,
 'exploit an opportunity 利用机会；exploit workers 剥削工人；heroic exploits 英勇事迹；a software exploit 软件漏洞利用方法。',
 'exploit an opportunity；heroic exploits。',
 '动词不永远贬义，资源、机会可中性利用；人物、弱势处境语境常突出不公平。名词与动词重音不同。',
 ('The team exploited the opportunity to improve the design.','团队利用这个机会改进了设计。'),('The book recounts the explorer’s remarkable exploits.','书中讲述探险家非凡的事迹。'),sources=['https://en.wiktionary.org/wiki/exploit#English','https://www.etymonline.com/word/exploit'])
W('exploitative','/ɪkˈsplɔɪtətɪv/，也读 /ɪksplɔɪˈteɪtɪv/','剥削性的；不公平利用人的',
 '一段安排把好处主要拿走，却让处境较弱的一方承担不公平代价，可以 exploitative。它常把 exploit 的负面支固定成性质评价。',
 'exploit + -ative → exploitative，与 exploitation 的性质形式相应；也见 exploitive。常用社会评价聚焦不公平利用，特定学科还可有专门意义。',Ex[:1]+[['exploit + -ative → exploitative','具有剥削、不公平利用性质的']],
 'exploitative practices 剥削性做法；an exploitative relationship 不公平利用的关系。',
 'exploitative practices；an exploitative relationship。',
 'exploitative 常带负面判断；exploitable 只说可以被利用，两词后缀和观察角度不同。',
 ('The article criticises exploitative working conditions.','文章批评带剥削性质的工作条件。'),('The novel portrays an exploitative relationship.','小说描写了一段不公平利用对方的关系。'))
W('exploitable','/ɪkˈsplɔɪtəbəl/','可利用的、可开发的；可乘之机的',
 '资源存在可以开发的价值，漏洞留下可以利用的机会，都可 exploitable。它先说能被用上，具体是好事还是危险，取决于谁利用什么。',
 '借法语对应形式或由 exploit + -able 形成，历史上有不同分析。-able 在这里表示可以被利用、开发的性质。',Ex[:1]+[['exploit + -able／法语对应形式 → exploitable','能被利用、开发的']],
 'exploitable resources 可开发资源；an exploitable weakness 可被利用的弱点；an exploitable opportunity 可利用机会。',
 'exploitable resources；an exploitable weakness。',
 'exploitable 可利用不等于已经被利用；exploited 才常是已利用、被剥削的过去分词状态。',
 ('The survey identified commercially exploitable resources.','调查识别了具有商业开发价值的资源。'),('The review found an exploitable weakness in the design.','审查发现设计中存在一个可被利用的弱点。'))
R('B3812','成果走向利用，公平与否决定常用语气，能力词另看','EXPLOIT：把机会、资源用上，也可能不公平地用别人','exploit → exploitative、exploitable；名词功绩与计算机方法另认重音、对象。',
 '利用不是处处负面，剥削也不是单纯能力强。exploitative 常评价不公平，exploitable 只说明可被利用，实际是否发生是另一层。',
 'explicitum、explicare → esploit、esploitier → exploit；名词前重音、动词后重音；-ative 性质，-able 可能性。',
 [['成果、利用与相应性质','exploit · exploitative · exploitable']],
 'exploitable 可利用与 exploitative 剥削性的不同；名词 exploits 常是事迹，不是所有例子都翻成剥削。',
 'The report distinguishes exploitable resources from exploitative practices.\n\n报告区分可开发资源与带剥削性质的做法。','exploit exploitative exploitable')

if __name__=='__main__':save('continuation_20261030_ny',ROOTS,WORDS)
