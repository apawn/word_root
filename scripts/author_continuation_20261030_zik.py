"""Edges, enclosures, weariness, success and return in common vocabulary."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
def S(word,base):return ['https://en.wiktionary.org/wiki/'+word+'#English','https://www.etymonline.com/word/'+base]
EXISTING_ROOT_ADDITIONS={
 'B4219':dict(words='fringe fringes fringed fringing'.split(),label='fringe：线穗边饰 → 外围、非主流',note='与 border 比较边缘，并非 border 派生。fringe 经法语 frenge 接拉丁 fimbriae 线、纤维、穗边，经历音位换位等变化；具体装饰边到一般边缘，再用于群体外围。'),
 'C1105':dict(words='bracket brackets bracketed bracketing'.split(),label='bracket：支架 → 括号、档次、归组',note='与 support 比较支撑，并非拉丁 portare 派生。bracket 可能经法语 braguette 等旧服饰材料，其确切形状桥梁有争论；建筑支架到成对印刷符号的借形较清楚，后来又用于归组和区间。'),
 'B3386':dict(words='fatigue fatigues fatigued fatiguing'.split(),label='fatigue：疲惫、使疲惫；军中杂务到工作服',note='与 tire 比较疲劳，并非 tire 派生。名动词借法语 fatigue、fatiguer 接拉丁 fatigare 使疲惫；较远常联系驱使到崩溃的材料。fatigues 军中杂务又借指工作服、作训服。'),
 'C1641':dict(words='triumph triumphs triumphed triumphing'.split(),label='triumph：凯旋庆典 → 大获成功',note='与 victory 比较胜利，不从拉丁 vincere 派生。triumph 名词与动词分别有法语、拉丁 triumphus、triumphare 借入背景；更远可能经伊特鲁里亚语接希腊 thriambos 赞歌，不按英语 tri- 三硬拆。'),
 'B2841':dict(words='comeback comebacks'.split(),label='come + back → comeback：复出、回升；回嘴',note='由 come back 相关短语形成闭合名词；回嘴、反驳义的早期记录在先，复出、恢复位置义在后。学习上可先记现代常见的复出，不把教学顺序当历史。'),
 'B3040':dict(words='threshold thresholds'.split(),label='threshold：门槛 → 界限、开端',note='与 door 比较入口，不由 door 派生。threshold 接古英语 þrescold 等，前部可能联系踩踏、打谷材料，后半来历和变形有争论；不能当作确定的 thresh + hold 挡谷物故事。'),
}
FRINGE=[['拉丁 fimbriae 纤维、线、穗边 → frimbia 等 → 古法语 frenge','音序变化后借入英语 fringe'],['装饰穗边 → 一般边缘、外围 → 群体或观念的边缘','动词由名词转来：加穗边、沿着边缘分布']]
BRACKET=[['法语 braguette 等旧服饰词可能影响英语 bracket','建筑支架的确切命名桥梁有不同解释，也受 arm 对应拉丁词影响'],['建筑支架 → 形似成对支架的括号 → 括在一起、归组','档次、区间等用法沿着被划在同一范围的关系理解']]
FATIGUE=[['拉丁 fatigare 使疲惫 → 法语 fatiguer、fatigue','更远常分析为驱使到衰竭的材料，细节并非全部确定'],['英语 fatigue：使人疲惫的事、疲劳；动词使疲惫','军中劳役、杂务 → fatigue dress → fatigues 工作服、作训服']]
TRIUMPH=[['希腊 thriambos 赞歌，可能经伊特鲁里亚语 → 拉丁 triumphus','较远借入路线带不确定；拉丁用于成功及凯旋庆典'],['法语 triumphe、triumpher 与拉丁 triumphus、triumphare → 英语名动词','凯旋、庆祝胜利 → 大获成功、胜过困难']]
COMEBACK=[['come + back：回来、作出回应的短语背景','闭合名词 comeback 形成'],['早期有言语反击、回嘴义；后来有复出、恢复位置义','现代常见事业重返、比赛追回劣势、时尚再次流行']]
THRESHOLD=[['古英语 þrescold、þærscwold 等 → 中古英语形式 → threshold','前部可能联系踩踏、打谷；后半来路有争论，后来受 hold 拼写影响'],['门槛、入口 → 边界、某种状态的开端','再用来理解超过某个程度才发生变化的界限']]
W('fringe','英、美 /frɪndʒ/','流苏、穗边；边缘、外围；〔英〕刘海；边缘的；沿边分布',
 '先看围巾边上一排散开的线穗，再看城市边缘、一个群体的外围。fringe 就把“主要部分外侧的那一圈”带到了不同场景。',
 '古法语 frenge 接拉丁 fimbriae 线、纤维、穗边，经 frimbia 等音序变化形式借入英语；名词边饰后来扩展为一般边缘，整体又转作动词。',FRINGE,
 'the fringe of a forest 是森林边缘；a fringe group 是边缘、小众团体；英式 a fringe 常是额前刘海；fringe benefits 是工资之外的福利。',
 'on the fringe；a fringe group；a fringe haircut；fringe benefits。',
 'fringe group 可能暗示不在主流，但不自动表示观点错误；刘海在美式常称 bangs，不能把一种地区用词当唯一说法。',
 ('A line of trees marks the fringe of the village.','一排树标出了村子的边缘。'),('She had her fringe trimmed before the interview.','面试前她修剪了刘海。'),sources=S('fringe','fringe'))
W('fringes','英、美 /ˈfrɪndʒɪz/','边缘、外围、流苏〔复数〕；沿边分布〔第三人称单数〕',
 '城市不止一个方向的外围，可以说 its fringes；几条围巾的穗边，也可以说 fringes。核心画面仍是主体外面那一圈。',
 'fringe + -s → fringes，原词已有 e，再加 s；/dʒ/ 后的后缀读 /ɪz/，多一个音节。',FRINGE+[['fringe + -s → fringes','名词复数或动词第三人称单数']],
 'on the fringes of society 是社会边缘；the fringes of the city 是城市外围；动词 a hedge fringes the garden 是树篱沿着花园边缘。',
 'on the fringes；the fringes of the city；decorative fringes。',
 'the fringes of a group 常指外围成员、活动；不是每次都表示地理上有一条实际边线。',
 ('They live on the fringes of the city.','他们住在城市外围。'),('The scarves have long decorative fringes.','这些围巾有长长的装饰流苏。'),sources=S('fringes','fringe'))
W('fringed','英、美 /frɪndʒd/','带流苏的；沿边围着的；加了穗边〔过去式、过去分词〕',
 '围巾边垂着一圈线穗，是 a fringed scarf；海岸边围着一圈树，也可借这个画面说 fringed with trees。',
 'fringe 去 e + -ed → fringed，/dʒ/ 后的 -ed 读 /d/。过去分词可描述已加边饰，也可描述被某物沿边围住的状态。',FRINGE+[['fringe 去 e + -ed → fringed','过去式、过去分词；也可作形容词修饰语']],
 'a fringed jacket 是带流苏的夹克；fringed with trees 是树木沿边环绕。植物不是装饰穗线，是借用了边缘分布的关系。',
 'a fringed scarf；a fringed jacket；fringed with trees。',
 'fringed 强调边缘上有一圈东西；covered 强调表面被覆盖，位置关系不同。',
 ('She wore a fringed jacket to the concert.','她穿着一件带流苏的夹克去听音乐会。'),('The lake was fringed with tall reeds.','湖边围着高高的芦苇。'),sources=S('fringed','fringe'))
W('fringing','英、美 /ˈfrɪndʒɪŋ/','沿边分布；加穗边；沿岸的',
 '一排树贴着海滩边缘长，或织物沿边添流苏，这样的过程与分布关系可以说 fringing。',
 'fringe 去 e + -ing → fringing；现在分词、动名词，也可在 fringing reef 沿岸礁等组合里作修饰语。',FRINGE+[['fringe 去 e + -ing → fringing','过程或沿边分布关系，不是新的独立词根']],
 'trees fringing a beach 是海滩边的树；fringing on a shawl 可以说披肩上的穗饰；fringing reef 的命名也抓沿岸分布。',
 'trees fringing the beach；fringing on a shawl；a fringing reef。',
 'fringing 不一定意味着额外人工装饰；自然生长的植物也能 fringe 一个地方的边缘。',
 ('The trees fringing the beach offered some shade.','海滩边的一排树提供了些阴凉。'),('The shawl has delicate fringing along its edges.','这条披肩边缘有精细的穗饰。'),sources=S('fringing','fringe'))
W('bracket','英、美 /ˈbrækɪt/','支架、托架；括号；档次、区间；用括号括起；归为一组',
 '墙上伸出一块托架，托住架板；纸上两只方括号，把中间内容夹起来。bracket 从支架借给符号，再把“放进同一范围”借给分类。',
 '英语早期建筑支架名可能经法语 braguette 等旧服饰词形而来，确切桥梁有争论，也受拉丁 brachium 手臂影响；印刷括号则以成对支架的外形命名。',BRACKET,
 'a shelf bracket 是层板托架；a square bracket 是方括号；an age bracket 是年龄段；bracket A with B 是把两者归作同类。',
 'a shelf bracket；a square bracket；an age bracket；bracket A with B。',
 'bracket 表示一组或区间时，重点是边界把内容圈在一起；不是说年龄本身有一块真的木托架。',
 ('A metal bracket supports the shelf.','一个金属托架支撑着架板。'),('Most applicants fall into the same age bracket.','多数申请人属于同一个年龄段。'),sources=S('bracket','bracket'))
W('brackets','英、美 /ˈbrækɪts/','括号；支架〔复数〕；归组、用括号括起〔第三人称单数〕',
 '把补充说明夹在一对符号里，是 in brackets；把板子固定在墙上的几块托架，也叫 brackets。外形与“夹在一组里”的关系串起这些义项。',
 'bracket + -s → brackets，/t/ 后接 /s/。可数名词形成复数，动词则形成第三人称单数。',BRACKET+[['bracket + -s → brackets','末尾 /ts/；名词复数或动词单数形式']],
 'in brackets 是放在括号中；square brackets 是方括号；wall brackets 是墙上托架。英式 brackets 也常泛指圆括号，具体名称看语境。',
 'in brackets；square brackets；wall brackets。',
 '美式常用 parentheses 特指圆括号、brackets 常指方括号；英式用 brackets 的范围可能更宽，不能只按一种地区习惯判断。',
 ('Put the extra information in brackets.','把补充信息放在括号里。'),('Two metal brackets hold the shelf in place.','两个金属托架把架板固定在原位。'),sources=S('brackets','bracket'))
W('bracketed','英、美 /ˈbrækɪtɪd/','用括号括起的；被归为一组的；括起了〔过去式、过去分词〕',
 '一段文字两侧加上括号，是 bracketed；两位作家被评论者放在同一类，也能说 bracketed together。',
 'bracket + -ed → bracketed，/t/ 后的 -ed 读 /ɪd/，增加音节；过去分词可表示被括起、被归组的状态。',BRACKET+[['bracket + -ed → bracketed','过去式、过去分词；词尾读 /ɪtɪd/']],
 'bracketed text 是括号内的文字；be bracketed with 是被与另一对象并列、归在一起。',
 'bracketed text；bracketed information；bracketed with another writer。',
 'bracketed with 可能只是归为同组，不保证两者所有方面都相同；这是说分类方式，不是下完整定义。',
 ('The bracketed text is an editorial note.','括号里的文字是编者注。'),('The two writers are often bracketed together.','这两位作家常被归为一类。'),sources=S('bracketed','bracket'))
W('bracketing','英、美 /ˈbrækɪtɪŋ/','用括号括起；归组；暂且搁置某项考虑',
 '先把某项圈起来，留在一边，再讨论其他内容。bracketing 除了真的加括号，也能借这个画面表示暂时搁置某个考虑因素。',
 'bracket + -ing → bracketing；词尾不双写 t。由支架、括号名词转成动词，再接 -ing 表过程。',BRACKET+[['bracket + -ing → bracketing','加括号、归组或暂且搁置的过程']],
 'bracketing a phrase 是给短语加括号；bracketing two groups together 是归组；bracketing a question 是在某次讨论中暂且放下它。',
 'bracketing a phrase；bracketing groups together；bracketing a question。',
 'bracketing 暂置一个问题，不一定是否认它重要；只是暂时把它划到当前分析范围之外。',
 ('The editor suggested bracketing the phrase.','编辑建议把这个短语加上括号。'),('Bracketing the cost question for a moment, is the design useful?','先暂且放下成本问题，这个设计有用吗？'),sources=S('bracketing','bracket'))
W('fatigue','英、美 /fəˈtiːɡ/','疲劳、疲惫；材料疲劳；使疲惫',
 '忙了一整天，精力像被耗空，是 fatigue。人会疲劳；金属反复承受力量后出现疲劳，也借用了“受累、撑不住”的关系。',
 '名词借法语 fatigue，动词接法语 fatiguer，较远同接拉丁 fatigare 使疲惫。更早常联系驱使到衰竭的材料；英语名动词各有借入背景，不全是现代名词才加零后缀。',FATIGUE,
 'mental fatigue 是精神疲劳；metal fatigue 是金属疲劳；repetition can fatigue an audience 是反复内容会让听众疲惫。',
 'mental fatigue；metal fatigue；fatigue an audience。',
 'fatigue 比 tiredness 往往更正式；作动词又可说使人疲惫。拼写 -gue 在这里读 /ɡ/，末尾 e 不单独发音。',
 ('By evening, fatigue was making it hard to concentrate.','到了晚上，疲劳让人很难集中注意力。'),('Engineers examined the part for signs of metal fatigue.','工程师检查了零件是否有金属疲劳的迹象。'),sources=S('fatigue','fatigue'))
W('fatigues','英、美 /fəˈtiːɡz/','军中杂务；军用工作服、作训服；使疲惫〔第三人称单数〕',
 'soldiers in fatigues 不是“士兵们在许多疲劳里”，而是穿着军用工作服、作训服。名称从需要做的杂务，借到了干这些活时穿的衣服。',
 'fatigue + -s → fatigues，后缀读 /z/。军中劳役、杂务的名词复数有自己的发展；服装义又与 fatigue dress 的缩略相关。',FATIGUE+[['fatigue + -s → fatigues','军中杂务 → 相关工作服；也可为动词第三人称单数']],
 'wear fatigues 是穿军用工作服；olive-green fatigues 是橄榄绿色作训服。动词 it fatigues me 才是它使我疲惫。',
 'wear fatigues；army fatigues；fatigues the audience。',
 'fatigue 疲劳通常不可数；常见服装义 fatigues 是固定复数用法，不能简单按“一件疲劳”去拆译。',
 ('The soldiers were wearing green fatigues.','士兵们穿着绿色作训服。'),('The repetitive soundtrack quickly fatigues the audience.','反复的配乐很快让观众听得疲惫。'),sources=S('fatigues','fatigue'))
W('fatigued','英、美 /fəˈtiːɡd/','疲惫的；使疲惫了〔过去式、过去分词〕',
 '长时间集中精力后，人已经累了，就是 fatigued。过去分词把“使累”转成了“已被耗累”的状态。',
 'fatigue 去掉末尾 e + -ed → fatigued，u 保留；/ɡ/ 后的 -ed 读 /d/。过去分词经常直接修饰疲惫的人。',FATIGUE+[['fatigue 去 e + -ed → fatigued','过去式、过去分词；形容词表示承受疲劳的一方']],
 'feel fatigued 是感觉疲惫；a fatigued crew 是疲惫的工作人员；the journey fatigued us 是旅途让我们累了。',
 'feel fatigued；a fatigued crew；physically fatigued。',
 'fatigued 是人被累到的状态；fatiguing 是某事让人累。The travellers were fatigued，the journey was fatiguing。',
 ('The crew felt fatigued after the long shift.','上完长班，工作人员感到很疲惫。'),('The journey had fatigued us more than we expected.','这趟旅程让我们比预想的更疲惫。'),sources=S('fatigued','fatigue'))
W('fatiguing','英、美 /fəˈtiːɡɪŋ/','使人疲惫的；正在使疲惫',
 '一项任务不停耗精力，本身就很 fatiguing。把注意力从“人累了”转到“这件事让人累”，就能分清它和 fatigued。',
 'fatigue 去末尾 e + -ing → fatiguing，保留 u 以延续硬音 /ɡ/；现在分词可转作形容词。',FATIGUE+[['fatigue 去 e + -ing → fatiguing','造成疲劳的事物、动作；或动词过程']],
 'a fatiguing journey 是累人的旅程；mentally fatiguing work 是消耗脑力的工作。',
 'a fatiguing journey；a fatiguing task；mentally fatiguing。',
 'a fatigued worker 是累了的工人；fatiguing work 是累人的工作。-ed 和 -ing 的差别要连着谁承受、谁造成这个关系记。',
 ('It was a long and fatiguing journey.','那是一趟漫长又累人的旅程。'),('Reading the tiny print was surprisingly fatiguing.','阅读那些小字出乎意料地费神。'),sources=S('fatiguing','fatigue'))
W('triumph','英、美 /ˈtraɪəmf/','重大胜利、成功；喜悦、得意；获胜、战胜',
 '打赢后凯旋、庆祝，后来不必真有战争：解决一个长期难题，也能是一场 triumph。词里常带“终于大获成功”的分量。',
 '名词经法语 triumphe、拉丁 triumphus，动词经法语 triumpher、拉丁 triumphare；拉丁词与凯旋、成功有关，更远可能经伊特鲁里亚语接希腊 thriambos 赞歌。',TRIUMPH,
 'a personal triumph 是个人的一次重大成功；triumph over difficulties 是战胜困难；in triumph 是带着胜利的喜悦。',
 'a personal triumph；triumph over difficulties；shout in triumph。',
 'success 范围较宽，triumph 往往更有重大胜利、克服阻力的感觉。开头虽然像 tri-，不能因此拆成英语“三 + 其他字母”。',
 ('Finishing the course was a personal triumph for her.','完成这门课程对她来说是一次重大的个人成功。'),('The story shows how patience can triumph over fear.','故事展示了耐心怎样战胜恐惧。'),sources=S('triumph','triumph'))
W('triumphs','英、美 /ˈtraɪəmfs/','重大胜利、成功〔复数〕；获胜、占上风〔第三人称单数〕',
 '几次值得庆祝的成功，是 triumphs；说 patience triumphs，是耐心最终占了上风。看它在句子里数成果，还是当谓语。',
 'triumph + -s → triumphs；ph 读 /f/，清音后复数或第三人称后缀读 /s/。',TRIUMPH+[['triumph + -s → triumphs','名词复数、动词第三人称单数；词尾 /mfs/']],
 'career triumphs 是事业上的重大成功；triumphs over 是胜过、战胜；不能把所有 triumphs 都当成名词胜利们。',
 'career triumphs；small triumphs；patience triumphs over anger。',
 'small triumphs 是说一件事虽小，但对当事人很值得庆祝，并不要求每场 triumph 都是全球性的重大事件。',
 ('The book recalls her greatest sporting triumphs.','这本书回顾了她最辉煌的体育成就。'),('In the final scene, hope triumphs over despair.','最后一幕中，希望战胜了绝望。'),sources=S('triumphs','triumph'))
W('triumphed','英、美 /ˈtraɪəmft/','获胜了；战胜了〔过去式、过去分词〕',
 '难题摆了很久，最后终于跨过去，就是 triumphed。句子常把克服的障碍放在 over 后面。',
 'triumph + -ed → triumphed；基础末音 /f/ 是清音，因此 -ed 读 /t/，不另加 /ɪd/ 音节。',TRIUMPH+[['triumph + -ed → triumphed','规则过去式、过去分词；词尾 /mft/']],
 'triumphed over opposition 是战胜了阻力；triumphed in the final 是在决赛中获胜。over 后突出对手、困难。',
 'triumphed over difficulties；triumphed in the final；finally triumphed。',
 'win 可直接接 a match；triumph 通常不直接说 triumph a match，而说 triumph in a match 或 triumph over an opponent。',
 ('The team triumphed in the final.','球队在决赛中获胜。'),('Her determination triumphed over a series of setbacks.','她靠决心克服了一连串挫折。'),sources=S('triumphed','triumph'))
W('triumphing','英、美 /ˈtraɪəmfɪŋ/','正在获胜；战胜的过程；庆祝胜利',
 '胜利正在发生，或正因胜利而欢欣，可以用 triumphing。它把 triumph 的动作展开成过程。',
 'triumph + -ing → triumphing，不删字母、不双写；动词来自较早的法语、拉丁凯旋词线，再形成英语分词。',TRIUMPH+[['triumph + -ing → triumphing','现在分词、动名词；在获胜、占上风或为胜利欢欣']],
 'triumphing over difficulties 是战胜困难；after triumphing 是获胜之后；观看语境判断是取得胜利还是庆祝得意。',
 'triumphing over adversity；after triumphing；triumphing in a competition。',
 'triumphing 是分词，triumphant 是有胜利、得意意味的形容词，分别有自己的构词和借入历史，不是改一个词尾随意互换。',
 ('The novel follows a young artist triumphing over adversity.','小说讲一位年轻艺术家战胜逆境的故事。'),('After triumphing in the competition, she thanked her coach.','在比赛中获胜后，她感谢了教练。'),sources=S('triumphing','triumph'))
W('comeback','英 /ˈkʌmbæk/；美 /ˈkʌmbæk/','复出；回升、重振；反驳、回嘴',
 '离开舞台的人重新站回台上，落后的球队把局面追回来，都可以叫 a comeback。话被别人抛过来，你回一句，也有“回到对方面前”的感觉。',
 'come + back 相关短语形成闭合名词 comeback；早期记录先有言语反击义，恢复原有地位、复出义在后。现代常用的复出可以先学，但不能倒写成唯一原义。',COMEBACK,
 'make a comeback 是复出、重振；a comeback win 是逆转获胜；a witty comeback 是机智的回嘴。',
 'make a comeback；a comeback win；a witty comeback。',
 'come back 两个词是动词短语；comeback 一个词是名词。He came back，he made a comeback，句型不同。',
 ('The singer made a successful comeback after ten years away.','离开十年后，这位歌手成功复出。'),('I could not think of a good comeback to her joke.','听到她的玩笑，我想不出一句巧妙的回嘴。'),sources=S('comeback','comeback'))
W('comebacks','英、美 /ˈkʌmbæks/','复出、回升、逆转〔复数〕；回嘴、反驳〔复数〕',
 '几次从低谷回来，或几句机智回嘴，都可以是 comebacks。复数数的是一次次回归，或者一句句回应。',
 'comeback + -s → comebacks；整体是闭合名词，在末尾加复数，/k/ 后后缀读 /s/。',COMEBACK+[['comeback + -s → comebacks','多个回归、逆转或言语反击']],
 'sporting comebacks 是体育比赛中的复出、逆转；quick comebacks 在谈话里常是反应很快的回嘴。',
 'memorable comebacks；sporting comebacks；witty comebacks。',
 'she comes back 的 s 加在动词 comes；her comebacks 的 s 加在名词整体末尾。分开写的动词短语与闭合名词，句法位置不同。',
 ('The documentary revisits several remarkable sporting comebacks.','纪录片回顾了几次了不起的体育逆转、复出。'),('She is known for her quick comebacks.','她以回嘴机敏出名。'),sources=S('comebacks','comeback'))
W('threshold','英 /ˈθreʃhəʊld/；美 /ˈθrɛʃhoʊld/','门槛；界限、阈值；开端',
 '跨过门槛，才算进入屋里。threshold 把“跨过去就进入另一状态”借给抽象事情：达到某个界限才触发变化，或正站在新阶段的入口。',
 '接古英语 þrescold、þærscwold 等门槛词形；前部可能与踩踏、打谷材料有关，后半来历有争论并受 hold 影响。现代不能当作确定的 thresh + hold 来讲。',THRESHOLD,
 'cross the threshold 是跨过门槛；a noise threshold 是噪声界限；on the threshold of a new era 是处于新时代的开端。',
 'cross the threshold；above a threshold；on the threshold of a new stage。',
 '把它讲成“门槛专门挡住地上的谷壳，所以 thresh + hold”是流行故事，缺少可靠证据。实际门槛到抽象界限的联系已经足够直观。',
 ('She paused on the threshold before entering the room.','她进屋前在门槛处停了一下。'),('The alert appears when the temperature exceeds a set threshold.','温度超过设定阈值时，就会出现提醒。'),sources=S('threshold','threshold'))
W('thresholds','英 /ˈθreʃhəʊldz/；美 /ˈθrɛʃhoʊldz/','门槛；界限、阈值〔复数〕',
 '不同报警规则各有一条触发线，这些线就是 thresholds。像好几道门槛，各自决定什么时候进入下一种状态。',
 'threshold + -s → thresholds，基础词末尾 /d/ 后加 /z/；复数接整个历史形成的名词。',THRESHOLD+[['threshold + -s → thresholds','多个门槛、界限；词尾 /ldz/']],
 'set thresholds 是设定阈值；different thresholds 是不同界限；门槛既可指实际入口，也可指抽象标准。',
 'set thresholds；different thresholds；cross several thresholds。',
 'thresholds 说明有多个界限，不意味着它们都一样高；比较指标时还要看各条界限具体对应什么。',
 ('The system uses different thresholds for different alerts.','系统为不同提醒设置了不同阈值。'),('Each sensor has its own warning thresholds.','每个传感器都有自己的预警阈值。'),sources=S('thresholds','threshold'))
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_zik',ROOTS,WORDS)
 extend_lessons()
