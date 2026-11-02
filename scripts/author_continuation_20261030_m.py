"""Crazy, awe and super: common semantic shifts in plain language."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
CR=[['中古英语 crasen','打碎、弄裂；更早可能日耳曼来源，借入路径有讨论'],['craze 与 crazy','破损、失常 → 失去常态；强烈热衷、流行热潮']]
def CH(f,m):return CR+[[f,m]]
W('craze','/kreɪz/','一时狂热、风潮；使表面产生细裂纹',
 '一大群人突然迷上同一件东西，一阵热劲席卷而来；陶器语境则是釉面出现细细裂纹。',
 '接中古英语 crasen 打碎、弄裂，更早的日耳曼来源和借入路径有讨论。心智失常、狂热义是后来的延伸，名词热潮义通常最实用。',CR,
 'the latest craze 最新风潮，a craze for something 对某物的狂热。陶瓷专业语境 craze/crazing 保留裂纹义。',
 'the latest craze；a craze for fitness；a passing craze。',
 'craze 比 trend 趋势更突出一阵强烈追捧，常带暂时性；craze 是名词风潮，crazy 是形容词。',
 ('The new toy became the latest craze at school.','这种新玩具成了学校里最新的风潮。'),('The glaze had crazed into a network of fine cracks.','釉面裂成了细密的裂纹网。'))
W('crazy','/ˈkreɪzi/','疯狂的；荒唐的；着迷的；惊人的〔口语〕',
 '事情超出平常范围，可能是太离谱，也可能是太兴奋、太喜欢；要听整句话的语气。',
 'craze + -y，早有破损、虚弱等义，后来用来形容失常，再扩展出狂热、惊人等口语义。历史画面不能当作对人的医学解释。',CH('craze + -y → crazy','破损、失常 → 荒唐、狂热、惊人'),
 'be crazy about music 对音乐着迷，drive someone crazy 让某人烦透或受不了，like crazy 拼命地。a crazy idea 可说荒唐点子，也可能是大胆点子。',
 'crazy about；drive someone crazy；like crazy；a crazy idea。',
 'crazy about 通常是喜爱，crazy to do 常评价做某事不理智。用 crazy 评价人可能冒犯；日常更稳妥地讲具体行为。',
 ('She is crazy about old films.','她特别迷老电影。'),('The constant noise is driving me crazy.','这持续的噪声快让我受不了了。'),sources=['https://www.etymonline.com/word/crazy','https://en.wiktionary.org/wiki/crazy#English'])
W('crazed','/kreɪzd/','失去理智的；狂热的；布满细裂纹的',
 '被某种情绪推到失常的地步；形容瓷器时则真的是表面裂出细纹。',
 'craze + -ed，保留动词造成的结果；形容人和形容材料连接的是不同的既有义项。',CH('craze + -ed → crazed','失常、狂热的结果；表面裂纹状态'),
 'a crazed expression 狂乱神情，crazed porcelain 釉面开裂的瓷器。语气通常比普通 excited 强得多。',
 'a crazed expression；a crazed look；crazed porcelain。',
 'crazy 可轻松夸一句惊人，crazed 常强调狂乱、失控；crazed pottery 与情绪无关。',
 ('He gave a crazed laugh and ran out of the room.','他狂乱地笑了一声，跑出了房间。'),('Fine lines covered the crazed surface of the old bowl.','旧碗开裂的表面布满了细纹。'))
W('craziness','/ˈkreɪzinəs/','疯狂、荒唐；混乱热闹的状况',
 '把 crazy 那种离谱、失控或乱成一团的状态，作为一件事来谈。',
 'crazy + -ness，y 改 i，-ness 把性质变成状态名词。旧义包括破损，今天日常常说荒唐或混乱。',CH('crazy + -ness → craziness','疯狂、荒唐或混乱的状态'),
 'the craziness of the plan 方案的荒唐，the craziness of the holiday season 节日期间忙乱的状况。',
 'the craziness of life；escape the craziness；the craziness of the idea。',
 'craziness 多为口语评价，不能只凭它判断疾病；chaos 混乱更直接说秩序状态。',
 ('We needed a quiet weekend away from all the craziness.','我们需要一个远离各种忙乱的安静周末。'),('She laughed at the craziness of the idea.','她笑这个想法太离谱。'))
W('crazily','/ˈkreɪzɪli/','疯狂地；失常地；极其〔口语〕',
 '动作、变化像失去平常节奏，或者只是把程度说得特别强。',
 'crazy + -ly，y 改 i 再接 -ly。副词形容做事方式或程度，与状态名词 craziness 分开。',CH('crazy + -ly → crazily','以疯狂、失常的方式；极其'),
 'laugh crazily 狂笑，spin crazily 疯狂旋转，crazily expensive 贵得离谱。口语修饰程度时不一定真有失控。',
 'spin crazily；laugh crazily；crazily expensive。',
 'crazy 修饰人或事的性质；crazily 修饰动作或形容词。a crazy price 与 crazily expensive 对应两种结构。',
 ('The loose wheel spun crazily.','松脱的轮子疯狂旋转。'),('Hotels were crazily expensive that weekend.','那个周末旅馆贵得离谱。'))
R('B3245','裂开、失常与狂热口语','CRAZE／CRAZY：从裂损的旧义，走向失常和强烈热情','先分 craze 风潮和 crazy 形容词，再看 crazed 结果、craziness 状态、crazily 方式。',
 '中古英语破碎词发展出失常和热衷义，具体深层路线有不确定。现代常用搭配远比机械翻成碎裂有效。',
 'craze → crazy、crazed；crazy → craziness、crazily，后两者 y 改 i。',
 [['基础与状态结果','craze · crazy · crazed'],['名词与副词','craziness · crazily']],
 'craze 一阵风潮，crazy about 迷上；crazed 通常更强；这些是日常用语，不作为诊断。',
 'The latest craze made those shoes crazily expensive.\n\n最新风潮让那种鞋贵得离谱。',
 'craze crazy crazed craziness crazily')
AW=[['古诺尔斯语 agi → 中古英语 awe','惧怕、敬畏，与本族相关旧词汇合'],['英语 awe','面对强大、壮观之物的敬畏与惊叹']]
def AH(f,m):return AW+[[f,m]]
W('awe','英 /ɔː/；美 /ɔː/ 或 /ɑː/','敬畏；惊叹；使震撼',
 '站在巨大瀑布、满天星河前，一时说不出话：既惊叹，又觉得自己很渺小。',
 '中古英语接斯堪的纳维亚来源，如古诺尔斯语 agi 惧怕；后来敬意、惊叹更突出。词尾 e 不发音。',AW,
 'in awe 敬畏、惊叹地，in awe of someone 对某人深感敬佩；作动词 be awed by 被震撼。',
 'in awe；in awe of；stand in awe；be awed by。',
 'awe 不是单纯 fear 害怕，也不是随口的 like 喜欢，通常有被力量、规模或才华震住的感觉。',
 ('We stood in awe beneath the enormous night sky.','在广阔的夜空下，我们满怀惊叹地站着。'),('Her skill left the audience in awe.','她的技艺让观众惊叹不已。'),sources=['https://www.etymonline.com/word/awe','https://en.wiktionary.org/wiki/awe#English'])
W('awesome','英 /ˈɔːsəm/；美 /ˈɔːsəm/ 或 /ˈɑːsəm/','令人敬畏、惊叹的；棒极了的〔口语〕',
 '本来是强到让你震住，后来口语把这股惊叹用成一句“太棒了”。',
 'awe + -some，-some 表引起这种感受或带有这种性质。早期敬畏义仍在，口语夸赞义后来普及。',AH('awe + -some → awesome','令人敬畏 → 令人赞叹、棒极了'),
 'awesome power 令人敬畏的力量，an awesome view 壮观景色，That’s awesome! 太棒了。口语褒义不能盖过所有正式语境。',
 'awesome power；an awesome view；That’s awesome!。',
 'awesome 今日常夸好，awful 常说糟糕；同出 awe，却经历不同方向的语义变化，不能只按后缀猜褒贬。',
 ('The storm showed the awesome power of nature.','风暴展现了大自然令人敬畏的力量。'),('Thanks for helping us—that was awesome.','谢谢你帮我们，真是太棒了。'))
W('awful','英 /ˈɔːfl/；美 /ˈɔːfl/ 或 /ˈɑːfl/','糟糕的；可怕的；极大的〔部分搭配〕',
 '历史上也是令人敬畏，后来负面的可怕感越来越突出，日常就成了“真糟”。',
 'awe + -ful，经中古英语相应形式。早期有引起敬畏、恐惧义，后来常用义贬化为很坏；不是今天直接把 awe 翻出来就够。',AH('awe + -ful → awful','令人敬畏、可怕 → 很糟糕'),
 'awful weather 糟糕天气，feel awful 身体难受或心里很不好受，an awful lot 非常多，是加强程度。',
 'awful weather；feel awful；an awful smell；an awful lot。',
 'awful 与 awesome 今天通常褒贬相反；an awful lot of help 则只强调帮助很多，不是在批评帮助糟。',
 ('The weather was awful throughout the trip.','旅途中天气一直很糟。'),('I felt awful about forgetting her birthday.','忘了她的生日，我心里很过意不去。'),sources=['https://www.etymonline.com/word/awful','https://en.wiktionary.org/wiki/awful#English'])
W('awfully','英 /ˈɔːfəli/；美 /ˈɔːfəli/ 或 /ˈɑːfəli/','极其、非常；糟糕地',
 '强到令人吃惊的程度，慢慢弱化成“很、非常”；也能保留表现很糟的意思。',
 'awful + -ly，副词从令人敬畏、可怕的方式义，发展出单纯加强程度的用法。',AH('awful + -ly → awfully','可怕地、很糟地 → 非常'),
 'awfully sorry 非常抱歉，awfully kind 非常好心。She sang awfully 才更像说唱得糟；看它修饰什么。',
 'awfully sorry；awfully kind；awfully difficult。',
 'awfully nice 是夸很好，不是糟糕地好；副词作程度加强时不保留原来负面评价。',
 ('That was awfully kind of you.','你真是太好心了。'),('I am awfully sorry for keeping you waiting.','让你久等了，我非常抱歉。'))
W('awestruck','/ˈɔːstrʌk/〔美式也 /ˈɑːstrʌk/〕','惊叹不已的；肃然起敬的',
 '像被壮观景象或惊人才华一下击中，整个人愣在那里。',
 'awe 敬畏 + struck〔strike 的过去分词〕，表示被敬畏、惊叹击中的状态。',AH('awe + struck → awestruck','被惊叹击中 → 震撼得说不出话'),
 'an awestruck audience 惊叹不已的观众，be awestruck by 被某物深深震撼；重点在人的感受。',
 'be awestruck by；an awestruck audience；an awestruck silence。',
 'awesome 常描述引起震撼的事物，awestruck 常描述感到震撼的人：an awesome view left us awestruck。',
 ('The children were awestruck by the size of the dinosaur skeleton.','恐龙骨架的巨大体积让孩子们惊叹不已。'),('An awestruck silence followed the final note.','最后一个音符落下后，全场惊叹得一片寂静。'))
R('B3420','敬畏、惊叹及褒贬分化','AWE：面对强大事物，惊叹又敬畏','awe → awesome、awful → awfully；awestruck 则讲感受震撼的人。',
 '旧义带惧怕，后来惊叹与敬意更突出。awesome 与 awful 的现代方向不同，是词义演变的好例子。',
 'awe + -some/-ful；awful + -ly；awe + struck。awe 接后缀时通常去末尾 e。',
 [['核心感受与正面惊叹','awe · awesome · awestruck'],['负面评价与程度弱化','awful · awfully']],
 'awesome 棒、awful 糟；awfully kind 又是非常好心。分清事物令人震撼与人感到震撼。',
 'The awesome landscape left us awestruck despite the awful weather.\n\n尽管天气糟糕，壮丽景色仍让我们惊叹不已。',
 'awe awesome awestruck awful awfully')
SU=[['拉丁 super','在上方、超过'],['英语 super- 与独立用法 super','超出普通水平 → 极好的；非常']]
W('super','英 /ˈsuːpə/；美 /ˈsuːpər/','极好的；非常〔口语〕；管理员等的缩略称呼',
 '超过平常水平，口语就可以夸“真棒”；放在形容词前又能加强成“特别”。',
 '形容词、副词接 super-，最终来自拉丁 super 在上、超过；名词 super 有多种独立缩略来源，如 superintendent，不把所有名词义归到一句太棒了。',SU,
 'a super idea 好点子，super easy 特别简单。美式 apartment super 常指公寓管理员，是 superintendent 的缩略。',
 'a super idea；super easy；the building super。',
 'super 常是轻松口语；正式说程度可以选 very 或更具体的词。supreme 等相关词各有自己的借入历史。',
 ('Thanks—we had a super time.','谢谢，我们玩得很开心。'),('The building super came to check the leak.','公寓管理员来查看漏水情况。'))
W('superego','英 /ˌsuːpərˈiːɡəʊ/；美 /ˌsuːpərˈiːɡoʊ/','超我〔精神分析概念〕',
 '在精神分析模型里，像心中管规矩、作自我评判的声音：这样做合不合标准。',
 'super 在上 + ego 自我，是德语 Über-Ich 的仿译词，属于精神分析术语。不是超能力自我，也不是解剖学的一块脑组织。',SU[:1]+[['德语 Über-Ich → 英语 super + ego','在自我之上的规范、评判功能 → 超我']],
 'the superego 在讨论弗洛伊德模型时，常与 id 本我、ego 自我并列；借这一模型理解术语，不把它当作所有心理学的统一结论。',
 'the ego and superego；a strict superego；the concept of the superego。',
 'ego 日常还可说自尊、自负，superego 是特定理论概念；super ego 两个随意分开的词不必然是同一术语。',
 ('The lecture explained the roles of the id, ego and superego.','讲座解释了本我、自我和超我的作用。'),('In this model, the superego reflects internalized standards.','在这一模型里，超我体现内化的规范。'))
R('B3716','上方、超过与口语强化','SUPER：高出普通水平；术语还要看具体造法','独立 super 先讲夸赞、程度和缩略用法，再讲 super + ego 的仿译术语。',
 '拉丁 super 表在上、超过。独立 super 和前缀关系紧密，superego 按德语理论名称仿译，不能只凭前缀编现代故事。',
 'super- → super；super + ego → superego；superintendent 的缩略也可为 super。',
 [['口语与缩略','super'],['理论仿译','superego']],
 'super 夸好、加强程度或缩略身份，看词性与语境；superego 是特定理论术语。',
 'The teacher gave a super clear explanation of the superego.\n\n老师把超我这个概念解释得特别清楚。',
 'super superego')
if __name__=='__main__':save('continuation_20261030_m',ROOTS,WORDS)
