"""Solitude versus loneliness, sin vocabulary and spinning threads."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
A=[['古英语 eall ān → 中古英语 all one/allone → alone','完全、独自一人，原来的 all 与 one 缩合'],['alone → lone；lone/alonely → lonely','截短形式；孤独、孤单的性质'],['lone + -some/-er','感到孤单；习惯独处的人']]
W('alone','英 /əˈləʊn/；美 /əˈloʊn/','独自、单独；仅仅、只有',
 '身边没有其他人，这是位置或参与情况；你可能享受安静，也可能难过，alone 本身不替你决定。',
 '来自早期 all one 的缩合，接古英语 eall ān 完全独自。现代不能按字母拆成否定 a- + 某个 lone；较短 lone 反而由 alone 截短。',A[:2],
 'live alone 独居，do it alone 独立做，leave someone alone 别打扰某人，you alone 只有你，the cost alone 光费用这一项。',
 'live alone；leave someone alone；you alone；the cost alone。',
 'alone 通常放表语、状语或名词后；a lone traveller 而非通常的 an alone traveller。alone 说独自，lonely 说孤独感，两者可分开。',
 ('I enjoy walking alone in the morning.','我喜欢早晨独自散步。'),('The rent alone would use half my income.','光房租就会花掉我一半收入。'))
W('lone','英 /ləʊn/；美 /loʊn/','单独的、孤身的；唯一的',
 '画面里只有一个旅人、一棵树或一票反对票；lone 把“就这一个”放在名词前面。',
 '由 alone 截去起首部分而来，不是由 lonely 删掉尾巴。现在常作定语，和 alone 的句法分工不同。',A[:2],
 'a lone traveller 独行旅人，a lone tree 孤零零一棵树，a lone voice 唯一发出不同意见的人，a lone parent 单亲家长。',
 'a lone traveller；a lone tree；a lone voice；a lone parent。',
 'lone 可以仅指一个、独自，不表示人际失败。lone parent 是家庭结构说法，不说明这个家长一定感到寂寞。',
 ('A lone tree stood in the middle of the field.','田野中央孤零零地立着一棵树。'),('She was the lone voice opposing the plan.','她是唯一反对这项计划的人。'))
W('lonely','英 /ˈləʊnli/；美 /ˈloʊnli/','感到孤独的；偏僻、少人的',
 '你想有人理解、陪伴，却感觉联系不上，这才是最常见的 lonely；即使在人群里，也可能这样。',
 '可联系 lone + -ly，也有从旧 alonely 截短的解释；这里 -ly 形成形容词。描述地方时把无人陪伴的画面扩展为偏僻、荒凉。',A+[['lonely 的常见用法','人的孤独感；地方少有人来']],
 'feel lonely 感到孤独，a lonely child 孤独的孩子，a lonely road 偏僻道路，lonely in a crowd 人群中仍孤独。',
 'feel lonely；a lonely child；a lonely road。',
 'alone 独自不一定 lonely；lonely 也不要求身边没人。a lonely place 可以说地方荒凉，不是在说地方有人的情绪。',
 ('She felt lonely even in the crowded room.','即使屋里挤满了人，她仍感到孤独。'),('We followed a lonely road through the hills.','我们沿着一条偏僻山路前行。'))
W('lonesome','英 /ˈləʊnsəm/；美 /ˈloʊnsəm/','孤单寂寞的；独自〔固定表达〕',
 '多半带一点缺人陪伴的寂寞味道；歌曲里听起来尤其容易让人想到一个人守着空荡地方。',
 'lone + -some，-some 表带某种性质、容易造成某种感觉，不是 some 几个。独自一人的固定说法 on one’s lonesome 又把这个形式名词化使用。',A+[['lone + -some → lonesome','孤单寂寞的；on one’s lonesome 独自']],
 'feel lonesome 感到寂寞，a lonesome night 寂寞夜晚，all on my lonesome 我独自一个人〔随意、略带诙谐〕。',
 'feel lonesome；a lonesome night；on my lonesome。',
 'lonesome 与 lonely 有重叠，lonesome 在美式和歌曲中较常见；on my lonesome 不等于 on some 几个东西上。',
 ('The house felt lonesome after everyone had left.','大家走后，屋子显得空荡寂寞。'),('I cooked dinner all on my lonesome.','我独自一个人做了晚饭。'))
W('loner','英 /ˈləʊnə/；美 /ˈloʊnər/','习惯独处、较少与人来往的人',
 '说的是一个人的日常交往方式：经常自己活动，较少加入群体。可能出于偏好，也可能是处境所致。',
 'lone + -er，-er 把独处特征落到人物身上。不是 lone 的比较级；也不能从词尾就推出他的内心感受。',A+[['lone + -er → loner','常独自活动、缺少或避开陪伴的人']],
 'a bit of a loner 有点独来独往的人，a natural loner 天性较爱独处的人，describe someone as a loner 形容某人独来独往。',
 'a bit of a loner；a natural loner；describe someone as a loner。',
 'loner 不必 lonely：爱独处的人可能很自在。这个标签也不自动等于 shy 害羞或 unfriendly 不友善。',
 ('He is a bit of a loner but always friendly when we talk.','他有点独来独往，但每次交谈都很友好。'),('She described herself as a loner who enjoys long walks.','她说自己喜欢独处，爱走很长的路。'))
R('B3663','独自的状态、孤独的感受和习惯独处的人','ALONE / LONELY：身边几个人，和心里缺不缺陪伴分开','alone → lone；lonely/lonesome 常谈感受；loner 谈习惯或交往状态。',
 '人群里可以孤独，独处时也可以满足。先分事实、感受、人物习惯三层，再记词就不容易混。',
 'eall ān → all one/allone → alone → lone；lone + -ly/-some/-er，lonely 另有旧 alonely 截短解释。',
 [['独自状态与唯一者','alone · lone'],['感受与地方气氛','lonely · lonesome'],['交往习惯的人物','loner']],
 'alone 多作表语、状语，lone 放名词前；-ly 这里不是副词；loner 不一定 lonely，也不必不友好。',
 'The lone traveller enjoyed being alone and did not feel lonely.\n\n那位独行旅人享受独处，并不觉得孤独。','alone lone lonely lonesome loner')
S=[['古英语 synn → 中古英语 sinne → sin','违背宗教、道德规范的罪、过错'],['英语 sin 的相关形式','犯罪过的人；有罪的、无罪的；一般过失和夸张用法']]
W('sin','/sɪn/','罪、罪过；过错；犯宗教或道德上的罪',
 '重点不是法条编号，而是违反某种宗教、道德要求；日常还会夸张说把好东西浪费掉真是罪过。',
 '接古英语 synn。更深与真实、有罪等词族的联系是一种词源解释，不必把它误学成现代 true 的变体；名词和动词在英语里都有历史。',S,
 'commit a sin 犯罪过，confess one’s sins 忏悔罪过，a sin against 对……的违背，It’s a sin to waste it 浪费了真可惜〔夸张〕。',
 'commit a sin；confess one’s sins；a sin against；a sin to waste。',
 'sin 不等于 crime：宗教罪过未必违法，违法也未必被不同信仰用同一方式描述。数学缩写 sin 对应 sine，读音和来源另看。',
 ('The story explores sin, forgiveness, and responsibility.','故事探讨罪过、宽恕与责任。'),('It would be a sin to waste such good food.','这么好的食物浪费掉真可惜。'),sources=['https://en.wiktionary.org/wiki/sin#English','https://www.etymonline.com/word/sin'])
W('sinner','英 /ˈsɪnə/；美 /ˈsɪnər/','有罪过的人、罪人〔宗教、道德评价〕',
 '把 sin 这个动作或状态放到人身上：犯过罪过的人。文学里也可自嘲，语气不能只靠中文罪犯来猜。',
 'sin + -er，双写 n；接中古英语相应人物词。-er 标承担行为的人，不是比较级，更不直接标法律定罪身份。',S+[['sin + -er → sinner','犯罪过、被认为有罪的人']],
 'a repentant sinner 忏悔的罪人，saints and sinners 圣徒与罪人，a sinner in the story 故事里的有罪者。',
 'a repentant sinner；saints and sinners。',
 'sinner 常置于宗教道德框架；criminal 说犯罪者。称呼别人 sinner 可能是在施加自己的道德判断，不是一个中性职业标签。',
 ('The sermon offered hope to every repentant sinner.','讲道给每个悔罪的人带来希望。'),('The novel refuses to divide people neatly into saints and sinners.','小说没有把人简单分成圣徒与罪人。'))
W('sinful','/ˈsɪnfəl/','有罪的、罪恶的；奢靡得像有罪一般的〔夸张〕',
 '认真语境里评价违反宗教道德；甜点广告里却可能夸张说好吃得太放纵，像做了坏事一样。',
 'sin + -ful，已有古英语 synful 等形式。-ful 表带有、充满；现代夸张用法借放纵的联想，不是给食物作真实神学判决。',S+[['sin + -ful → sinful','有罪、构成罪过的；比喻奢华放纵']],
 'sinful behaviour 有罪行为，a sinful life 被评价为有罪的生活，sinful indulgence 放纵享受，a sinful dessert 令人放纵的甜点〔宣传式夸张〕。',
 'sinful behaviour；a sinful life；sinful indulgence。',
 'sinful 可以评价人，也可评价行为；sinfully rich dessert 中的 rich 指浓郁，通常不是犯法或人很有钱。',
 ('The character struggles with what he believes are sinful thoughts.','那个人物为自己认定有罪的念头而挣扎。'),('The menu described the chocolate cake as a sinful indulgence.','菜单把巧克力蛋糕夸成令人放纵的享受。'))
W('sinless','/ˈsɪnləs/','无罪的、未犯过罪过的〔宗教道德义〕',
 '在所采用的宗教道德框架下，没有罪过；范围比没把题做错大得多。',
 'sin + -less，接古英语 synlēas 等历史形式。-less 表没有，与 sinful 的有罪性质形成一对。',S+[['sin + -less → sinless','没有罪过、未曾犯下罪过']],
 'a sinless life 无罪的一生，sinless perfection 无罪的完美状态；多在宗教、神学和相关文学里出现。',
 'a sinless life；sinless perfection；believed to be sinless。',
 'sinless 不等于 error-free 没有操作错误，也不同于法律判决的 not guilty。用词框架要跟文本一致。',
 ('The poem presents an ideal of a sinless life.','诗中呈现了一种无罪生活的理想。'),('The theologian discussed whether a human being could be sinless.','神学家讨论了人能否没有罪过。'))
R('B2934','宗教、道德框架中的罪过，以及人物和性质','SIN：违背所奉行的规范，先问是哪种规范','sin → sinner；sinful 有罪，sinless 无罪；日常比喻可能只是说太可惜、太放纵。',
 '中文罪字容易把法律、道德、宗教混成一团。英语这些词也要放进具体框架，不能只靠一个字互换。',
 'synn → sin；sin + -er〔双写 n〕；sin + -ful/-less。',
 [['罪过及人物','sin · sinner'],['性质两面','sinful · sinless']],
 'sin/crime 不完全重合；sinner/criminal 不机械互换；sinful 甜点常是夸张；sinless 不等于零笔误。',
 'The novel asks whether its sinner can leave a sinful life behind.\n\n小说追问，这位有罪的人能否告别过去被视为罪恶的生活。','sin sinner sinful sinless')
P=[['古英语 spinnan → 中古英语 spinnen → spin','把纤维捻成线 → 旋转、纺织相关动作'],['英语组合与引申','旋转器、纺锤、纺线者；故事和宣传的加工说法']]
W('spin','/spɪn/','旋转；纺线、吐丝结网；编造叙事、作倾向性解读；短途兜风',
 '把纤维捻成一股线，和东西绕轴转，都能想到旋转成形；把事实纺成对自己有利的故事，又是引申。',
 '接古英语 spinnan 纺线，后来扩展为旋转及多种相关用法。不规则过去式、分词常用 spun；spinning 加词尾双写 n。',P,
 'spin a wheel 转轮子，spin wool 纺羊毛，spin a web 结网，put a positive spin on 作有利解读，go for a spin 兜一圈。',
 'spin a wheel；spin a web；put a positive spin on；go for a spin。',
 'spin 宣传义不必凭空捏造，也可以只挑选、强调对自己有利的角度；turn 更广，spin 往往强调绕转。',
 ('The wheel spun faster and faster.','轮子越转越快。'),('The statement put a positive spin on the disappointing results.','声明从有利角度解读了令人失望的结果。'))
W('spinner','英 /ˈspɪnə/；美 /ˈspɪnər/','纺线者；旋转器、转盘；加载旋转标识等',
 '谁在纺、什么在转，都可能由 -er 命名；网页里不停转的小圈，也是把旋转这件事变成了可见标识。',
 'spin + -er，双写 n，已有中古英语人物名词。-er 既能给人命名，也能给装置、显示控件命名。',P+[['spin + -er → spinner','纺线者；旋转装置、旋转型界面标识']],
 'a wool spinner 羊毛纺线者，a game spinner 游戏转盘，a loading spinner 加载旋转标识，a fidget spinner 指尖陀螺。',
 'a game spinner；a loading spinner；a fidget spinner。',
 'loading spinner 转着通常表示处理中，不证明任务真的在取得进展。spinner 板球投手等专门义也要按运动语境看。',
 ('The children used a spinner to choose the next colour.','孩子们用转盘决定下一个颜色。'),('A loading spinner appeared while the page opened.','页面打开时出现了加载旋转标识。'))
W('spindle','/ˈspɪndəl/','纺锤、纺锭；旋转轴、机床主轴',
 '一根细长的轴，转着把线捻出来或绕上去；再把类似旋转轴的结构借给机器。',
 '接古英语 spindle/spindel，更早有 spinel 等形式，联系 spin 和旧器具名后缀 -le。d 是历史形态的一部分，不应发明现代 -dle 后缀。',P+[['spinel 等 → spindel/spindle','纺线用轴、纺锤'],['旋转轴扩展','机器旋转主轴及类似细长结构']],
 'a spinning spindle 纺锭，a machine spindle 机器主轴，a spindle shaft 主轴；a spindle-shaped object 是中间较粗、两端渐细的形状描述。',
 'a spinning spindle；a machine spindle；spindle speed。',
 'spinner 可指纺的人或旋转装置，spindle 通常是那根轴、纺锭本身。现代不能把 -dle 当万能纺织后缀。',
 ('The thread wound around the spindle.','线绕在纺锭上。'),('The display shows the machine’s spindle speed.','显示屏显示机器的主轴转速。'))
W('spinster','英 /ˈspɪnstə/；美 /ˈspɪnstər/','未婚女性，尤指被视为过通常婚龄者〔旧式，常含贬义〕；纺线者〔历史义〕',
 '最初是纺线的职业称谓，后来社会记录把它用作未婚女性身份。今天拿来称呼人，容易带着过时的婚龄评判。',
 'spin + -ster，后缀历史上常形成女性职业名，但使用中并非永远限女性。纺织与未婚女性的社会角色联系，推动它转成婚姻身份称谓。',P+[['spin + -ster → spinster','纺线者，早期尤其说女性'],['职业与婚姻记录中的社会背景','未婚女性称谓 → 常带婚龄成见的旧式词']],
 'a spinster in an old novel 老小说中的未婚女性称谓，recorded as a spinster 旧档案记为未婚女子。现在中性说法通常直接 unmarried woman 或 single woman。',
 'an old-fashioned term；recorded as a spinster；a spinster in the novel。',
 'spinster 不应现代直译成职业纺织工；它对婚姻身份的旧式语气也不同于通常更中性的 bachelor。读档案和称呼真人要区别。',
 ('The old marriage record described her as a spinster.','旧婚姻登记把她的身份记作未婚女子。'),('The novel challenges the stereotype attached to the word spinster.','小说挑战了 spinster 一词附带的刻板印象。'),sources=['https://en.wiktionary.org/wiki/spinster#English','https://www.etymonline.com/word/spinster'])
R('B2985','纺线、旋转及相关人物、器具和叙事比喻','SPIN：捻成线、绕轴转，故事也能被加工出角度','spin → spinner/spindle；spinster 保留职业转身份的社会历史；tailspin 是旋转失控相关的另一组合。',
 '把动作、做事的人和那根轴分开，再看文字宣传的倾向性加工。spinster 的社会意义不是只用词根就能推出来的。',
 'spinnan → spin；spin + -er/-ster；spinel → spindle〔旧器具形式〕；tail + spin。',
 [['动作、执行者与器具','spin · spinner · spindle'],['社会身份与失控画面','spinster · tailspin']],
 'spin 宣传可只是选择性解读；spinner 不一定是人；spindle 没有现代万能 -dle；spinster 婚姻称谓有旧式色彩。',
 'The spinner watched the spindle turn as the thread formed.\n\n纺线者看着纺锭转动，纤维渐渐成线。','spin spinner spindle spinster tailspin')
if __name__=='__main__':save('continuation_20261030_hs',ROOTS,WORDS)
