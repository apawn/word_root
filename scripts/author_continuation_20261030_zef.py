"""Common musical families: fitting sounds together, instruments and players."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'B3688':dict(words=['harmony','harmonies','harmonic','harmonize','harmonise','harmonized','harmonizing','harmonica','harmonicas'],label='harmony 的协调、和声与 harmonica 名称',note='共同核心是接合、配合。harmonica 早期指玻璃乐器，后来也命名口琴；共同名称不意味着玻璃乐器物理改造成口琴。'),
 'A1744':dict(words=['harmony','harmonies'],label='harmony → harmonies：和声的多种安排',note='辅音字母后 y 变 i 加 -es；复数常数和声部分、搭配，不把抽象协调强行拆成一个个对象。'),
 'A1697':dict(words=['trumpet','trumpets','trumpeter','trumpeters'],label='trumpet → trumpeter：小号到吹号者',note='trumpet 借古法语 trompette，其 -ette 原是小称材料；现代人物词再接完整 -er。'),
 'A1691':dict(words=['trombone','trombones','trombonist','clarinet','clarinets','clarinetist','clarinetists','flutist','flutists','flautist','flautists','saxophone','saxophones','saxophonist','saxophonists','viola','violas','cello','cellos','cellist','cellists','harp','harps','harpist','harpists'],label='管弦乐器与 -ist 演奏者名称',note='trombone、clarinet 等先有借词名称，再形成或借入演奏者名。viola 也是 violin、violoncello 的历史命名材料；不是 -ist 的直系派生词。'),
 'C0430':dict(words=['flute','flutes','flutist','flutists','flautist','flautists'],label='flute、flutist、flautist 的常用复数与不同借入路线',note='flute 接古法语等乐器名称，远接 flare 只是解释之一。flutist 可能经法语，flautist 经意大利语 flautista；并非后一词先在英语改写出前一词。'),
 'C0230':dict(words=['clarinet','clarinets','clarinetist','clarinetists'],label='clarus 的明亮、清晰进入 clarinet 乐器名',note='clarinet 经法语 clarinette 等路线接拉丁 clarus，意大利 clarinetto 也见于来源分析；乐器具体分类与名称中的明亮联想分开。'),
 'C1025':dict(words=['saxophone','saxophones','saxophonist','saxophonists'],label='Sax + 声音材料的乐器名及人物名',note='Sax 是发明者姓氏，-phone 给声音材料；saxophone 去 e 接 -ist 再变复数。'),
 'A1829':dict(words=['saxophone','saxophones'],label='saxophone → saxophones：数一支支萨克斯管',note='先认完整乐器名，再在词尾加 -s，不把 -phone 当成此处独立的电话。'),
 'A1987':dict(words=['saxophone','saxophones'],label='乐器组合名中的 -o- 与末尾复数',note='Sax、连接成分和声音材料组成器物名称，复数作用于整个名称。'),
}
HARM=[['希腊 harmonia 接合、配合 → 拉丁、法语相应词','声音合得上；人与事相协调'],['英语 harmony 及相关词','和声、和谐；相关音乐名称']]
W('harmonies','英 /ˈhɑːməniz/；美 /ˈhɑːrməniz/','和声、和声声部或搭配〔复数〕',
 '几个人唱不同的音，放在一起却合得上；这些互相配合的声音、和声安排，可以叫 harmonies。',
 'harmony 的辅音字母 n 后 y 改 i，加 -es。基础词经法语、拉丁语接希腊 harmonia 接合、配合。',HARM+[['harmony → harmonies','不同和声安排、和声部分']],
 'sing harmonies 常说唱和声部分；rich harmonies 说声音搭配丰富，不是每个人都唱同一条主旋律。',
 'vocal harmonies 人声和声；close harmonies 密集和声。',
 'melodies 是一条条先后流动的曲调，harmonies 更关注不同声音怎样配合；记住线条与搭配的区别。',
 ('The singers added soft harmonies to the chorus.','歌手们给副歌加上柔和的和声。'),('I love the rich harmonies in this song.','我喜欢这首歌里丰富的和声。'),sources=['https://en.wiktionary.org/wiki/harmonies#English','https://www.etymonline.com/word/harmony'])
W('harmonic','英 /hɑːˈmɒnɪk/；美 /hɑːrˈmɑːnɪk/','和声的；谐波的；泛音〔名词〕',
 '先抓住声音怎样配合的关系。harmonic 常给音乐的和声结构命名，也进入描述声音、波动的术语；名词可指泛音。',
 '借拉丁 harmonicus，接希腊 harmonikos，与 harmonia 同族。现代可认 harmon- + -ic，但不是在英语 harmony 后直接保留 y 拼成。',
 [['希腊 harmonia → harmonikos → 拉丁 harmonicus','与音乐、和声有关的'],['英语 harmonic；harmonic tone 缩为 harmonic','和声的；作为名词指相应音']],
 'harmonic structure 是和声结构；演奏中的 a harmonic 则是一个泛音。技术语境要看正在描述什么波或音。',
 'harmonic changes 和声变化；play a harmonic 奏一个泛音。',
 'harmonious 常说听起来悦耳、关系融洽，harmonic 更常说明属于和声、谐波的性质；technical harmonic 不等于好听。',
 ('The piece has a simple harmonic structure.','这首曲子的和声结构简单。'),('She played a clear harmonic on the violin.','她用小提琴奏出一个清亮的泛音。'),sources=['https://www.etymonline.com/word/harmonic','https://en.wiktionary.org/wiki/harmonic#English'])
W('harmonise','英 /ˈhɑːmənaɪz/；美 /ˈhɑːrmənaɪz/','唱和声；使协调〔harmonize 的拼写变体〕',
 '本来各唱各的，现在让声音搭得上；本来各用各的规则，现在让规则接得上。两种情形都能用 harmonise。',
 'harmonize 的 -ise 拼写，英式常见；近源与法语 harmoniser 相连，现代对应 harmony 去 y 加 -ise。',
 HARM+[['法语 harmoniser；英语 harmonize／harmonise','用和声配合；使安排、规则等协调']],
 'harmonise with 表示与……配合，harmonise two systems 是让两个系统的安排相协调。',
 'harmonise with the melody 与旋律配和声；harmonise standards 协调标准。',
 'harmonise 和 harmonize 读音、核心意义相同；使规则协调未必要求每条细节完全一致。',
 ('The two voices harmonise beautifully.','两个声音配合得很美。'),('We need to harmonise the two sets of instructions.','我们需要把两套说明协调起来。'),sources=['https://en.wiktionary.org/wiki/harmonise#English','https://en.wiktionary.org/wiki/harmonize#English'])
W('harmonized','英 /ˈhɑːmənaɪzd/；美 /ˈhɑːrmənaɪzd/','配了和声、协调了；协调一致的',
 '分开的声音、安排已经调到能配合的状态，是 harmonized。音乐里可以说曲调已经配上和声。',
 'harmonize 去词尾 e，加完整 -ed；末尾 /z/ 后读 /d/。不是把基础 harmony 直接加 -ed。',
 HARM+[['harmonize + -ed → harmonized〔去 e〕','过去配了和声、使协调；所得状态']],
 'harmonized procedures 是协调过的程序；harmonized a melody 是给旋律编配和声。',
 'harmonized standards 协调一致的标准；harmonized the tune 给曲调配了和声。',
 'harmonized 关注配合后的结果，standardized 更关注按标准统一；两种工作可以重叠。',
 ('She harmonized the melody for four voices.','她把旋律编配成四个声部。'),('The teams harmonized their reporting procedures.','各团队协调了汇报程序。'),sources=['https://en.wiktionary.org/wiki/harmonized#English','https://en.wiktionary.org/wiki/harmonize#English'])
W('harmonizing','英 /ˈhɑːmənaɪzɪŋ/；美 /ˈhɑːrmənaɪzɪŋ/','正在唱和声、使协调；配和声的活动',
 '一边听别人唱，一边把自己的声部放到合适的位置，是 harmonizing；让不同安排互相配合也沿用这个动词。',
 'harmonize 去末尾 e，加完整 -ing。词族的配合画面保留，后缀让你看正在进行的动作。',
 HARM+[['harmonize + -ing → harmonizing〔去 e〕','配和声、协调工作的进行']],
 'harmonizing with someone 是和某人唱和声；harmonizing procedures 则是协调程序。',
 'harmonizing with the lead singer 与主唱配和声；harmonizing rules 协调规则。',
 'singing in unison 是唱同一旋律、音高线，harmonizing 通常在不同声部间形成配合。',
 ('They were harmonizing with the lead singer.','他们正给主唱配和声。'),('We spent the meeting harmonizing the two schedules.','我们在会上协调了两份时间安排。'),sources=['https://en.wiktionary.org/wiki/harmonizing#English','https://en.wiktionary.org/wiki/harmonize#English'])
W('harmonica','英 /hɑːˈmɒnɪkə/；美 /hɑːrˈmɑːnɪkə/','口琴；玻璃琴〔历史上也用此名〕',
 '常见的是放在嘴边、吹气吸气奏响的小乐器。这个名字从协调的音乐材料来，并不是英语 mouth 加琴的直译。',
 'harmonica 接拉丁 harmonicus、希腊 harmonia 一族；Franklin 曾用相关意大利、拉丁形式为玻璃乐器命名，口琴义后来才出现。',
 [['希腊 harmonia → harmonicus 等相关形式','配合、音乐的材料'],['早期 harmonica 命名玻璃乐器 → 后有口琴义','名称后来也用于簧片口吹乐器，不是同一器物改造史']],
 'play the harmonica 通常说吹口琴；glass harmonica 则是靠玻璃部件摩擦发声的另一乐器。',
 'a blues harmonica 蓝调口琴；play the harmonica 吹口琴。',
 'harmonica 是乐器名，harmonic 常作和声、谐波相关的形容词；多出来的 a 不能随意忽略。',
 ('He played a short tune on the harmonica.','他用口琴吹了一小段曲子。'),('She keeps a harmonica in her coat pocket.','她把一把口琴放在外套口袋里。'),sources=['https://www.etymonline.com/word/harmonica','https://en.wiktionary.org/wiki/harmonica#English'])
W('harmonicas','英 /hɑːˈmɒnɪkəz/；美 /hɑːrˈmɑːnɪkəz/','口琴〔复数〕',
 '一把口琴是 a harmonica，盒子里几把口琴就是 harmonicas；词尾只是在数乐器。',
 'harmonica + -s，词末元音后读 /z/。名称接和声、音乐的古典语言材料，口琴用途比早期玻璃乐器命名晚。',
 [['harmonica 的玻璃乐器名称与后来口琴义','名称用途扩展，两个具体器物分开'],['harmonica + -s → harmonicas','多把口琴']],
 'harmonicas in different keys 常指不同调的口琴；用不同乐器配合不同曲子。',
 'a set of harmonicas 一套口琴；blues harmonicas 蓝调口琴。',
 'harmonicas 数口琴，harmonies 数和声部分、搭配；两者同族，却不是同一种东西。',
 ('The musician brought harmonicas in several keys.','乐手带来了几种不同调的口琴。'),('The shop keeps its harmonicas in a glass cabinet.','商店把口琴放在玻璃柜里。'),sources=['https://en.wiktionary.org/wiki/harmonicas#English','https://www.etymonline.com/word/harmonica'])
TRUMP=[['古法语 trompe + 小称 -ette → trompette','号、号角的相关乐器名；更远很可能有日耳曼拟声背景'],['中古英语 trompet → trumpet','小号、号角；后来又有高声宣扬等动词用法']]
W('trumpet','/ˈtrʌmpɪt/','小号、喇叭；高声宣扬；发出号角般声音',
 '先听一声响亮的号角：能召集人、让大家注意。名字后来既指乐器，也能说把消息大声宣传出去。',
 '经中古英语借古法语 trompette，是 trompe 号角的小称；更远很可能接日耳曼拟声形式。不是从英语 trump 王牌再加一个现代词尾得来。',TRUMP,
 'play the trumpet 是吹小号；trumpet a success 是大肆宣扬一次成功。大象等发出类似号角的声音，也可用这个动词。',
 'a trumpet solo 小号独奏；trumpet the news 大声宣扬消息。',
 'trump 王牌、胜过的常用义与 triumph 的截短有关；trumpet 的乐器名是另一近源路线。',
 ('She plays the trumpet in the school band.','她在学校乐队吹小号。'),('The company will trumpet its success in the next campaign.','公司会在下次宣传中大力宣扬这次成功。'),sources=['https://www.etymonline.com/word/trumpet','https://www.etymonline.com/word/trump','https://en.wiktionary.org/wiki/trumpet#English'])
W('trumpets','/ˈtrʌmpɪts/','小号、号角〔复数〕；大声宣扬、鸣叫〔第三人称单数〕',
 '一排响亮的小号是 trumpets；说谁把消息高声传开，也能说 trumpets the news。',
 'trumpet + -s，/t/ 后读 /s/。乐器名接古法语 trompette，动词由乐器名称发展，整个词再作数、人的变化。',
 TRUMP+[['trumpet + -s → trumpets','多把小号；它高声宣扬或发出号角声']],
 'the trumpets in the band 可以按乐器名借指小号声部；trumpets its achievements 则说大肆宣传成就。',
 'brass trumpets 铜制小号；trumpets the results 大力宣扬结果。',
 'trumpets 是乐器或动作，trumpeters 是演奏者；多出来的 -er 把注意力转到人。',
 ('The trumpets entered at the end of the passage.','这一段末尾小号声部加入。'),('The advertisement trumpets the product’s new design.','广告大肆宣扬产品的新设计。'),sources=['https://en.wiktionary.org/wiki/trumpets#English','https://www.etymonline.com/word/trumpet'])
W('trumpeter','英 /ˈtrʌmpɪtə/；美 /ˈtrʌmpɪtər/','小号手、吹号者；高声宣传者',
 '号角是 trumpet，吹号让声音传出去的人是 trumpeter。把消息高声传开的人，也能借这个称呼描述。',
 'trumpet + 完整 -er，形成做这件事的人。乐器名称更早经古法语进入英语，人物后缀接在完整基础词后。',
 TRUMP+[['trumpet + -er → trumpeter','吹小号的人；借指高声宣布的人']],
 'a jazz trumpeter 是爵士小号手；trumpeter swan 则是因叫声命名的一种天鹅。',
 'a solo trumpeter 小号独奏者；a skilled trumpeter 熟练的小号手。',
 'trumpeter 是人名角色，trumpet 是乐器、吹奏或宣扬动作；这里 -er 不表示比较级。',
 ('A lone trumpeter played from the balcony.','一位小号手独自在阳台上吹奏。'),('The band invited a guest trumpeter for the concert.','乐队邀请了一位客座小号手参加音乐会。'),sources=['https://www.etymonline.com/word/trumpeter','https://en.wiktionary.org/wiki/trumpeter#English'])
W('trumpeters','英 /ˈtrʌmpɪtəz/；美 /ˈtrʌmpɪtərz/','小号手、吹号者〔复数〕',
 '几位小号手并排举起乐器，叫 trumpeters。数的是吹奏的人，手里的乐器才叫 trumpets。',
 'trumpet + -er → trumpeter，再加 -s，末尾读 /z/；先变成人物名称，再数人。',
 [['trumpet + -er → trumpeter','吹号、吹小号的人'],['trumpeter + -s → trumpeters','多位演奏者']],
 'two trumpeters 是两位小号手；the trumpets 可指几把小号或整个小号声部，关注点不同。',
 'jazz trumpeters 爵士小号手；a line of trumpeters 一排吹号者。',
 'trumpeters 的重音仍在开头；复数 -s 接完整人物词，既不去 -er，也不把 trumpet 再变复数。',
 ('The trumpeters stood at the front of the band.','小号手们站在乐队前面。'),('Two trumpeters took turns playing the melody.','两位小号手轮流演奏旋律。'),sources=['https://en.wiktionary.org/wiki/trumpeters#English','https://en.wiktionary.org/wiki/trumpeter#English'])
TROMB=[['意大利 tromba 号 + 增大后缀 -one → trombone','名称字面为大号角；不是英语 bone 骨头'],['意大利 trombone → 英语 trombone','长号的乐器名称']]
W('trombone','英 /ˌtrɒmˈbəʊn/；美 /ˌtrɑːmˈboʊn/','长号',
 '长长的金属管子来回伸缩，音高随之改变：这是常见滑管长号的直观画面。名字里说的是“大号角”。',
 '借意大利 trombone：tromba 号角 + 增大后缀 -one。tromba 与 trumpet 的古法语近源属于相关号角名称，更远很可能有日耳曼背景。',TROMB,
 'play the trombone 是吹长号；常见滑管型用推拉改变管长，也有其他结构的长号。',
 'a trombone solo 长号独奏；a bass trombone 低音长号。',
 '结尾 -bone 在这个意大利借词里不是英语骨头 bone；整词读音也不要按骨头故事拆。',
 ('He plays the trombone in a brass band.','他在铜管乐队吹长号。'),('The trombone gave the passage a warm, low sound.','长号给这一段添上温暖低沉的声音。'),sources=['https://www.etymonline.com/word/trombone','https://en.wiktionary.org/wiki/trombone#English'])
W('trombones','英 /ˌtrɒmˈbəʊnz/；美 /ˌtrɑːmˈboʊnz/','长号〔复数〕',
 '几支长号一起加入，声音一下厚起来；这些乐器或相应声部可叫 trombones。',
 'trombone + -s，保留词尾 e，末尾 /n/ 后读 /z/。原名是意大利 tromba 与增大后缀 -one 的旧组合。',
 TROMB+[['trombone + -s → trombones','多支长号；借指长号声部']],
 'the trombones 可以让乐器名称代表演奏该部分的人、声音；两支实物则可直接说 two trombones。',
 'tenor trombones 次中音长号；the trombones enter 长号声部加入。',
 'trumpets 和 trombones 都属铜管乐器名称，但一个是小号，一个是长号，不按共同的号字混成同一种琴。',
 ('Three trombones joined the brass section.','三支长号加入了铜管声部。'),('The trombones rest during this passage.','这一段长号声部休止。'),sources=['https://en.wiktionary.org/wiki/trombones#English','https://www.etymonline.com/word/trombone'])
W('trombonist','英 /trɒmˈbəʊnɪst/；美 /trɑːmˈboʊnɪst/','长号手、长号演奏者',
 'trombone 是长号，trombonist 是吹它的人。认出乐器再认 -ist，就能把名称指向演奏者。',
 'trombone 去词末 e，加完整 -ist；不是 trombon 另有一个骨头词根。',
 TROMB+[['trombone + -ist → trombonist〔去 e〕','长号演奏者']],
 'a jazz trombonist 是爵士长号手；称呼按演奏乐器确定，和音乐风格可以组合。',
 'a solo trombonist 长号独奏者；a guest trombonist 客座长号手。',
 'trumpeter 对应 trumpet，trombonist 对应 trombone；人物后缀不同，记成整组比见乐器就一律加 -er 更稳。',
 ('The trombonist played a short solo.','长号手吹了一段短独奏。'),('A guest trombonist joined the band tonight.','今晚一位客座长号手加入了乐队。'),sources=['https://en.wiktionary.org/wiki/trombonist#English','https://www.etymonline.com/word/trombone'])
FLUTE=[['古普罗旺斯语 flaut → 古法语相关形式 → flute','笛类乐器名，更远来源未定；接 flare 吹只是解释之一'],['flute 的形状联想','后来也能命名细长酒杯、纵向凹槽']]
W('flutes','/fluːts/','长笛、细长香槟杯、纵向凹槽〔复数〕',
 '常见先想到几支长笛；看餐桌时可能是细长酒杯，看柱子时可能是竖直凹槽。共同外形联想帮助分支，场景决定是哪一种。',
 'flute + -s，/t/ 后读 /s/。乐器名经古法语等路线而来，远源未定；杯子、凹槽义从形状联想发展。',
 FLUTE+[['flute + -s → flutes','多支长笛、多只细长杯或多条凹槽']],
 'concert flutes 是音乐会长笛，champagne flutes 是细长香槟杯；后者不是装饮料的乐器。',
 'silver flutes 银制长笛；champagne flutes 香槟笛形杯。',
 'flutes 数器物，flutists 数演奏者；同形动词形式也存在，但最常见先按对象认这些名词义。',
 ('The flutes played a bright melody.','长笛声部奏出明亮的旋律。'),('They set six champagne flutes on the table.','他们在桌上摆了六只细长香槟杯。'),sources=['https://www.etymonline.com/word/flute','https://en.wiktionary.org/wiki/flutes#English'])
W('flutists','/ˈfluːtɪsts/','长笛演奏者〔复数，尤美式〕',
 'flute 是长笛，flutist 是吹长笛的人；几位演奏者一起出现，就是 flutists。',
 'flutist + -s。现代按 flute 去 e 加完整 -ist 认形；英语 flutist 也可能经法语 flûtiste 借入，出现早于另一常见形式 flautist。',
 [['法语 flûtiste 可能传入英语 flutist','也可按 flute + -ist 认形；长笛演奏者'],['flutist + -s → flutists','多位长笛演奏者']],
 '美式常用 flutists；英式常见 flautists，两者通常指同一种演奏者，不是水平不同。',
 'two flutists 两位长笛演奏者；professional flutists 职业长笛手。',
 'flutists 中元音常与 flute 的 /uː/ 对应；flautists 的常见读音另记，不按多一个 a 判断乐器不同。',
 ('Two flutists performed the duet.','两位长笛演奏者演奏了二重奏。'),('The workshop brought together young flutists.','工作坊把年轻长笛演奏者聚到一起。'),sources=['https://www.etymonline.com/word/flutist','https://en.wiktionary.org/wiki/flutists#English'])
W('flautists','/ˈflɔːtɪsts/，亦 /ˈflaʊtɪsts/','长笛演奏者〔复数，尤英式〕',
 '看着比 flutists 多一个 a，仍然是在说长笛手。这个拼写保留了另一条欧洲借词路线的样子。',
 'flautist + -s；flautist 借意大利 flautista，来自 flauto 长笛 + -ista 人物后缀，不是英语 flute 先传到意大利才形成。',
 [['意大利 flauto + -ista → flautista → 英语 flautist','长笛演奏者名称的借入'],['flautist + -s → flautists','多位长笛演奏者']],
 'British flautists 是英国长笛演奏者；拼写偏好之外，具体人物、曲目并无专属限制。',
 'young flautists 年轻长笛手；a group of flautists 一群长笛手。',
 'flutists 与 flautists 通常同义；分别保留不同形成历史，不能按字长排出基础与高级演奏者。',
 ('The orchestra invited two guest flautists.','乐团邀请了两位客座长笛演奏者。'),('The young flautists practised the passage together.','年轻的长笛手们一起练习这一段。'),sources=['https://www.etymonline.com/word/flautist','https://en.wiktionary.org/wiki/flautists#English'])
CLAR=[['拉丁 clarus 明亮、清晰 → 法语 clair、clarin、clarine 等','清亮声音、小铃、号角等相关名称'],['法语 clarinette 等路线 → clarinet','小称名称成为单簧管的乐器名；另有意大利 clarinetto 来源分析']]
W('clarinet','/ˌklærɪˈnet/','单簧管、黑管',
 '嘴边一片簧片振动，管身上的孔和按键改变音高：这是单簧管。名字的远处藏着“明亮、清晰”的声音联想。',
 '经法语 clarinette 等路线接拉丁 clarus 明亮、清晰；也有意大利 clarinetto、clarino 的来源分析。小称材料在借入前已有，不是英语把 clear 现场拼长。',CLAR,
 'play the clarinet 是吹单簧管；clarinet reed 是单簧管簧片。它属于木管乐器，名称里的号角联想不等于铜管分类。',
 'a clarinet solo 单簧管独奏；a bass clarinet 低音单簧管。',
 'clarinet 是单簧管，trumpet 是小号。历史名称有清亮、号角的联系，现代两件乐器仍要分清。',
 ('She plays the clarinet in the orchestra.','她在管弦乐团吹单簧管。'),('The clarinet carries the melody in this passage.','这一段由单簧管奏主旋律。'),sources=['https://www.etymonline.com/word/clarinet','https://en.wiktionary.org/wiki/clarinet#English'])
W('clarinets','/ˌklærɪˈnets/','单簧管〔复数〕',
 '几支单簧管放在一起叫 clarinets；乐谱里也能用这些乐器名指负责演奏的声部。',
 'clarinet + -s，/t/ 后读 /s/。基础名称经法语、意大利语相关路线，远接拉丁 clarus 明亮、清晰。',
 CLAR+[['clarinet + -s → clarinets','多支单簧管、相应声部']],
 'two clarinets 可说两支实物，也可说为两支单簧管写的乐曲编制。',
 'bass clarinets 低音单簧管；the clarinets enter 单簧管声部加入。',
 'clarinets 是乐器名称复数，clarinetists 是人物名称复数；-ist 放在复数 -s 前面。',
 ('The piece is written for two clarinets and a piano.','这首曲子为两支单簧管和一架钢琴而作。'),('The clarinets enter after the strings.','单簧管声部在弦乐之后加入。'),sources=['https://en.wiktionary.org/wiki/clarinets#English','https://www.etymonline.com/word/clarinet'])
W('clarinetist','/ˌklærɪˈnetɪst/','单簧管演奏者',
 '乐器 clarinet 后面接表示相关人物的 -ist，目光就从管子移到吹奏它的人。',
 'clarinet + -ist；也常拼 clarinettist，尤其英式。两种拼写的单双 t 不表示不同的乐器或演奏身份。',
 CLAR+[['clarinet + -ist → clarinetist','单簧管演奏者；与 clarinettist 对应']],
 'a jazz clarinetist 是爵士单簧管手，a solo clarinetist 是独奏演奏者；词尾指出活动相关人物。',
 'a guest clarinetist 客座单簧管手；a skilled clarinetist 熟练的单簧管演奏者。',
 'clarinet 是乐器，clarinetist 是人；一位演奏者带着两支乐器，是 one clarinetist with two clarinets。',
 ('The clarinetist tuned her instrument before the rehearsal.','单簧管演奏者在排练前给乐器调音。'),('A guest clarinetist joined the quartet.','一位客座单簧管手加入了四重奏。'),sources=['https://en.wiktionary.org/wiki/clarinetist#English','https://www.etymonline.com/word/clarinet'])
W('clarinetists','/ˌklærɪˈnetɪsts/','单簧管演奏者〔复数〕',
 '几位吹单簧管的人叫 clarinetists。先看 -ist 找到人，再看最后 -s 知道不止一位。',
 'clarinet + -ist → clarinetist，再加 -s；英式常见另拼 clarinettists，意义相同。',
 [['clarinet + -ist → clarinetist','演奏单簧管的人'],['clarinetist + -s → clarinetists','多位演奏者']],
 'young clarinetists、professional clarinetists 分别说年轻、职业演奏者，身份名称本身不说明具体水平。',
 'two clarinetists 两位单簧管手；a group of clarinetists 一群单簧管手。',
 'clarinets 可借指乐队的乐器声部，clarinetists 明确把演奏者作为人物来谈。',
 ('The clarinetists practised the difficult entry together.','单簧管手们一起练习那个难进的乐句开头。'),('The class includes six young clarinetists.','班上有六位年轻的单簧管演奏者。'),sources=['https://en.wiktionary.org/wiki/clarinetists#English','https://en.wiktionary.org/wiki/clarinetist#English'])
SAX=[['法语 Sax + 连接材料 -o- + -phone → saxophone','发明者 Adolphe Sax 的姓，加声音材料命名'],['法语借入英语 saxophone','萨克斯管；之后形成演奏者名称']]
W('saxophones','英 /ˈsæksəfəʊnz/；美 /ˈsæksəfoʊnz/','萨克斯管〔复数〕',
 '弯曲的管身、嘴边的簧片、常见明亮有力的声音，先把整件乐器认出来。saxophones 是几支萨克斯管。',
 'saxophone + -s，词末 /n/ 后读 /z/。原名在法语中用发明者 Sax 的姓与 -phone 声音材料组合，再借入英语。',
 SAX+[['saxophone + -s → saxophones','多支萨克斯管；相应声部']],
 'alto saxophones、tenor saxophones 分别指中音、次中音萨克斯管；不同种类有不同音域。',
 'two saxophones 两支萨克斯管；the saxophones in the band 乐队里的萨克斯声部。',
 '尽管常见管身是金属，saxophone 属于木管乐器，按发声方式等传统分类；不要只看外壳就归铜管。',
 ('The band uses two saxophones and a trumpet.','乐队使用两支萨克斯管和一把小号。'),('The saxophones take over the melody here.','这里萨克斯声部接过主旋律。'),sources=['https://en.wiktionary.org/wiki/saxophones#English','https://en.wiktionary.org/wiki/saxophone#English'])
W('saxophonists','英 /sækˈsɒfənɪsts/；美 /ˈsæksəfoʊnɪsts/','萨克斯管演奏者〔复数〕',
 'saxophones 数管子，saxophonists 数吹管子的人。名词里那个声音材料仍在，后面再标出人物身份。',
 'saxophone 去末尾 e，加 -ist → saxophonist；复数再加 -s。常见英美读音的重音、元音有差别。',
 SAX+[['saxophone + -ist → saxophonist → saxophonists〔去 e〕','萨克斯演奏者；多位演奏者']],
 'jazz saxophonists 是爵士萨克斯手，classical saxophonists 是古典萨克斯演奏者；两种音乐里都可出现。',
 'young saxophonists 年轻萨克斯手；two saxophonists 两位萨克斯演奏者。',
 '英式常重读 -soph- 这一段，美式也常保持靠前的重音；不要因拼写长就把每一段都重读。',
 ('Two saxophonists traded short solos.','两位萨克斯手轮流演奏短独奏。'),('The workshop attracted saxophonists from several cities.','工作坊吸引了几个城市的萨克斯演奏者。'),sources=['https://en.wiktionary.org/wiki/saxophonists#English','https://en.wiktionary.org/wiki/saxophonist#English'])
CELLO=[['意大利 viola → violone → violoncello','相关弦乐器名称，经增大、小称材料形成较长名称'],['violoncello 缩短 → cello','英语常用的大提琴名称']]
W('cellos','英 /ˈtʃeləʊz/；美 /ˈtʃeloʊz/','大提琴〔复数〕',
 '比小提琴大得多，演奏者坐着把它放在身前，常见低沉温暖的弦声。几把这样的乐器就是 cellos。',
 'cello + -s，直接写 cellos；cello 缩自意大利 violoncello，较长名称又接 violone 与小称材料。词首 c 保留 /tʃ/。',
 CELLO+[['cello + -s → cellos','多把大提琴、相应声部']],
 'the cellos in the orchestra 可以说大提琴声部；two cellos 则直接数乐器或演奏编制。',
 'two cellos 两把大提琴；the cellos enter 大提琴声部加入。',
 'cellos 不是 cell 细胞的复数；保留意大利借词的 /tʃ/，与 cells 的 /s/ 分开。',
 ('The piece opens with two cellos.','曲子以两把大提琴的演奏开场。'),('The cellos support the melody with a warm lower line.','大提琴声部以温暖的低声部托住旋律。'),sources=['https://en.wiktionary.org/wiki/cellos#English','https://en.wiktionary.org/wiki/cello#English'])
W('cellists','/ˈtʃelɪsts/','大提琴演奏者〔复数〕',
 'cello 是大提琴，cellist 是演奏者；几位坐在琴后的演奏者就是 cellists。词首仍跟着乐器名称读。',
 'cello 去末尾 o，加完整 -ist → cellist，再加 -s。基础名称缩自 violoncello；不是英语 cell 细胞加人物后缀。',
 CELLO+[['cello + -ist → cellist → cellists〔去 o〕','演奏大提琴的人；多位演奏者']],
 'two cellists 可只说两位演奏者；还可用 solo cellists、orchestral cellists 区分独奏、乐团演奏角色。',
 'young cellists 年轻大提琴手；a group of cellists 一群大提琴演奏者。',
 'cellists 读 /ˈtʃelɪsts/；cells 细胞以 /s/ 开头。相同的 cell 字母，在不同来源的词里读音不同。',
 ('The cellists sat behind the violins.','大提琴手们坐在小提琴声部后面。'),('Two cellists performed the opening duet.','两位大提琴演奏者演奏了开场二重奏。'),sources=['https://en.wiktionary.org/wiki/cellists#English','https://en.wiktionary.org/wiki/cellist#English'])
VIOLA=[['中古拉丁 vitula、古普罗旺斯 viola 等相关形式','弦乐器名称；更远来源及与日耳曼词的关系有不同分析'],['意大利 viola → 英语 viola〔乐器支〕','现代英语中的中提琴名称']]
W('viola','英 /viˈəʊlə/；美 /viˈoʊlə/','中提琴',
 '外形像小提琴而通常更大，音色、音域更低一些，夹在高低弦声之间：这是中提琴。',
 '乐器义借意大利 viola，接古普罗旺斯、拉丁等相关弦乐器名称；更远起源未定，不把女神命名等解释说成定论。',VIOLA,
 'play the viola 是拉中提琴；它常在弦乐组合中承担中间声部，也有独奏作品。',
 'a viola solo 中提琴独奏；viola and piano 中提琴与钢琴。',
 '同形 viola 还可指堇菜属植物，接拉丁花名，读音也可不同；本组乐器名不从紫花的颜色推来。',
 ('She switched from violin to viola.','她从拉小提琴改学中提琴。'),('The viola has a warm sound in this recording.','这段录音里的中提琴声音温暖。'),sources=['https://www.etymonline.com/word/viola','https://en.wiktionary.org/wiki/viola#English'])
W('violas','英 /viˈəʊləz/；美 /viˈoʊləz/〔乐器义〕','中提琴〔复数〕',
 '几把中提琴、或者乐队里的整个中提琴声部，都可叫 violas。先用音乐场景选出乐器这一支。',
 'viola + -s，末尾读 /z/。乐器名经意大利语来；同形花卉名属另一近源支，不能共用一个乐器故事。',
 VIOLA+[['viola + -s → violas〔乐器义〕','多把中提琴、相应声部']],
 'the violas in the orchestra 是乐团中提琴声部；数实物也能说 two violas。',
 'two violas 两把中提琴；the violas take over 中提琴声部接过演奏。',
 'violins 是小提琴，violas 是中提琴；虽然名称有关，两者的现代编制、音域不能互换。',
 ('The violas repeat the phrase an octave lower.','中提琴声部低一个八度重复这一乐句。'),('The school bought two new violas.','学校买了两把新中提琴。'),sources=['https://en.wiktionary.org/wiki/violas#English','https://www.etymonline.com/word/viola'])
HARP=[['古英语 hearpe、hearpian → harp','竖琴及演奏动作的本族词'],['harp 的现代用途；harp on','乐器、弹奏；反复谈同一件事']]
W('harps','英 /hɑːps/；美 /hɑːrps/','竖琴〔复数〕；反复唠叨〔第三人称单数，常接 on〕',
 '手指拨过竖起的一排琴弦，是竖琴的画面；话老在同一件事上拨来拨去，harps on 就有反复念叨的感觉。',
 'harp + -s，/p/ 后读 /s/。名词、动词有古英语 hearpe、hearpian 背景，反复谈论义是后来的延伸。',
 HARP+[['harp + -s → harps','多架竖琴；它反复谈某事']],
 'two harps 在数乐器；she harps on the mistake 是她老揪着那个错误说，常带说话人嫌烦的语气。',
 'concert harps 音乐会竖琴；harps on the same point 反复念叨同一点。',
 'harps on 强调重复得令人厌烦，mentions 只说提到；是否带嫌烦的意思，要看语气和场景。',
 ('Two harps accompanied the choir.','两架竖琴为合唱团伴奏。'),('He always harps on that one mistake.','他总是抓着那一个错误反复说。'),sources=['https://en.wiktionary.org/wiki/harps#English','https://www.etymonline.com/word/harp'])
W('harpists','英 /ˈhɑːpɪsts/；美 /ˈhɑːrpɪsts/','竖琴演奏者〔复数〕',
 'harp 是乐器，harpist 是用手指拨奏它的人，harpists 是多位竖琴演奏者。',
 'harp + -ist → harpist，再加 -s。这里取竖琴演奏义，人物后缀接在整个乐器名称后。',
 HARP+[['harp + -ist → harpist → harpists','竖琴手；多位竖琴演奏者']],
 'concert harpists 常参加音乐会演奏，folk harpists 可演奏民间竖琴；都是按乐器与角色描述人。',
 'two harpists 两位竖琴演奏者；young harpists 年轻竖琴手。',
 'harpists 是演奏者，不用 harp on 的唠叨义去猜人物词；形态相连的词也要选对基础义项。',
 ('The two harpists played on opposite sides of the stage.','两位竖琴演奏者在舞台两侧演奏。'),('The course welcomes harpists of different ages.','这门课欢迎不同年龄的竖琴演奏者。'),sources=['https://en.wiktionary.org/wiki/harpists#English','https://en.wiktionary.org/wiki/harpist#English'])

def extend_lessons():
    extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
    save('continuation_20261030_zef',ROOTS,WORDS)
    extend_lessons()
