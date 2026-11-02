"""Master and sing: basic senses, close derivatives and common compounds."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
MA=[['拉丁 magister → 古英语 mægester 等；古法语 maistre','负责人、老师；两条传入形式在中古英语汇合'],['现代 master','主人、师傅、高手、硕士；掌握；主版本、母版']]
def MH(f,m):return MA+[[f,m]]
W('master','英 /ˈmɑːstə/；美 /ˈmæstər/','主人、师傅、高手；硕士；掌握；主版本、母版',
 '可以管得住一件事的人，或者手艺练到能带别人的人；把技能学到熟练，也叫 master。',
 '古英语早借拉丁 magister 负责人、老师，中古阶段又受法语 maistre 影响。学位、熟练者和母版等义各自发展，不是 modern mass + -ter。',MA,
 'master a skill 掌握技能，a master of painting 绘画大师，a master’s degree 硕士学位，a master copy 主版本。历史文字里 master 还可指奴隶主等控制者。',
 'master a skill；a master of；a master’s degree；a master copy。',
 'master 动词通常暗示熟练控制，learn 学习不保证已掌握；master 也不总指男性人物，现代具体称谓按场景。',
 ('It takes practice to master a new skill.','掌握新技能需要练习。'),('Keep the master copy in a safe place.','把主版本保存在安全地方。'),sources=['https://www.etymonline.com/word/master','https://en.wiktionary.org/wiki/master#English'])
W('mastery','英 /ˈmɑːstəri/；美 /ˈmæstəri/','精通、熟练掌握；控制',
 '不是刚会一点，而是遇到变化也能稳稳应付；那种掌握程度就是 mastery。',
 '经中古英语借古法语 maistrie，现代可对应 master + -y 的名词关系。不要把 -y 一律当形容词后缀。',MA[:1]+[['古法语 maistrie → 英语 mastery','主导、控制 → 精通、熟练掌握']],
 'mastery of a language 精通一门语言，technical mastery 技术上的娴熟，gain mastery over 控制住。',
 'mastery of；technical mastery；gain mastery over。',
 'a master 可以说人，mastery 说掌握程度、能力状态；熟悉 familiarity 往往还未到 mastery。',
 ('The performance showed her mastery of rhythm.','这场表演展现了她对节奏的娴熟掌握。'),('Real mastery comes from applying the skill in different situations.','真正的精通来自在不同情境中运用技能。'))
W('masterful','英 /ˈmɑːstəfl/；美 /ˈmæstərfl/','技艺高超的；有支配力、强势的',
 '一面是像高手一样把事情做得漂亮，一面是像主人一样强力控制局面；上下文决定褒贬。',
 'master + -ful，中古英语已有相应形式。早有专横、主导义，高超、娴熟义也有长期历史，不能用旧规范否认现代实际用法。',MH('master + -ful → masterful','有主人式控制力；有大师技艺'),
 'a masterful performance 精湛表演，masterful handling 高明处理，a masterful manner 强势作风。看修饰的是技能还是控制态度。',
 'a masterful performance；masterful handling；a masterful manner。',
 'masterful 与 masterly 在高超义上可重合；masterful 还可强势、专横。不能按 -ful 永远负面、-ly 永远正面的死规则判断。',
 ('She gave a masterful performance of the concerto.','她精湛地演奏了这首协奏曲。'),('His masterful manner left little room for disagreement.','他强势的作风几乎不容别人提出异议。'),sources=['https://www.etymonline.com/word/masterful','https://en.wiktionary.org/wiki/masterful#English'])
W('masterly','英 /ˈmɑːstəli/；美 /ˈmæstərli/','娴熟高明的；大师级的',
 '看一场表演、一次处理，觉得每一步都拿捏得很熟，像高手出手。',
 'master + 形容词 -ly，中古英语已有相应形式。这里 -ly 主要构成形容词，并非看到 -ly 就一定副词。',MH('master + -ly → masterly','以大师水准完成的、技艺高明的'),
 'a masterly analysis 高明分析，masterly control 娴熟控制，a masterly performance 大师级表演。语体较书面。',
 'a masterly analysis；masterly control；a masterly performance。',
 'masterly 常偏夸技艺，masterful 在同义用法之外还可指强势；二者并非所有场景都能互换。',
 ('The book offers a masterly analysis of the evidence.','书中对证据作了高明的分析。'),('The musician showed masterly control of tone.','音乐家展现了对音色的娴熟控制。'))
W('grandmaster','英 /ˈɡrænmɑːstə/；美 /ˈɡrænmæstər/','特级大师；某领域的顶尖高手',
 '已经是高手，还在高手之上；国际象棋里尤其常作正式头衔。',
 'grand 伟大的、重要的 + master 高手，合成更高等级称号。实际头衔条件由具体组织、领域规定。',MH('grand + master → grandmaster','高阶大师称号；尤国际象棋特级大师'),
 'a chess grandmaster 国际象棋特级大师，an international grandmaster 国际特级大师；其他活动也可用这个名称。',
 'a chess grandmaster；an international grandmaster；become a grandmaster。',
 'grandmaster 不是 grandfather 祖父；grand 在这里提升称号等级。称某人为顶尖高手也不必然授予正式棋类头衔。',
 ('The young player trained with a chess grandmaster.','年轻棋手跟一位国际象棋特级大师训练。'),('The interview explores the grandmaster’s approach to practice.','访谈探讨了这位特级大师的训练方法。'))
W('remaster','英 /ˌriːˈmɑːstə/；美 /ˌriːˈmæstər/〔动词〕','重新制作母版；重新处理旧录音、影像；复刻改良版本',
 '拿旧录音、旧影像的材料，重新处理制作发布用的母版；常希望声音、画面更适合新版本。',
 're- 再次 + master 的母版、制作母版义。不是要求大师重新把技能学一遍。游戏语境也扩展到重制改良版本。',MH('re- + master〔制作母版〕→ remaster','重新处理并制作发布母版、版本'),
 'remaster an album 重新制作专辑母版，a remastered film 修复重制影片；不同项目改动程度有差异。',
 'remaster an album；a remastered recording；a digital remaster。',
 'remaster 常基于既有材料再处理，remake 常重新制作作品，remix 常重新混音；实际发行标签不保证改动程度或效果完全一致。',
 ('The studio remastered the album from the original tapes.','录音室用原始磁带重新制作了专辑母版。'),('A remastered version of the film was released.','影片推出了重新处理音画的版本。'))
R('B3955','控制、熟练与大师；母版的现代用途','MASTER：人可以是高手，动作可以是掌握，版本可以是母版','master → mastery、masterful、masterly；grandmaster 人物称号，remaster 则接母版义。',
 '拉丁负责人、教师词经古英语和法语传入。熟练、控制、学位和母版等分支要各自抓场景，已有常用复合词共享。',
 'master → mastery〔法语名词支线〕、masterful、masterly；grand- + master；re- + master〔母版〕。',
 [['基本能力与性质','master · mastery · masterful · masterly'],['人物与作品','grandmaster · masterpiece · mastermind · headmaster · postmaster · quartermaster · schoolmaster · paymaster'],['母版与作品词','remaster · masterwork']],
 'masterful 今可高超也可强势；masterly 主要形容词；grandmaster 不等于祖父；remaster 接母版义。',
 'The remastered recording preserves a masterful performance.\n\n重新制作的录音母版保留了一场精湛演奏。',
 'master mastery masterful masterly grandmaster masterpiece mastermind headmaster postmaster quartermaster schoolmaster paymaster remaster masterwork')
SI=[['古英语 singan → 中古英语 singen','唱、用声音形成旋律'],['英语 sing—sang—sung','保留不规则元音变化；singing、singer 继续派生']]
def IH(f,m):return SI+[[f,m]]
W('sing','/sɪŋ/','唱歌；鸣唱；发出悦耳或持续的声音',
 '用嗓音把旋律唱出来；鸟儿鸣唱，风或金属发出像歌一样的声音，也可以借用。',
 '继承古英语 singan，经中古英语延续。变化 sing—sang—sung 保留旧元音交替，不是普通加 -ed。末尾 ng 读 /ŋ/。',SI,
 'sing a song 唱歌，sing along 跟着唱，sing in a choir 在合唱团唱；sing someone’s praises 大力称赞。',
 'sing a song；sing along；sing in a choir；sing someone’s praises。',
 'sing 唱与 song 歌是同族词，song 并非英语任意把 i 改 o 的名词规则；singe /sɪndʒ/ 燎焦是另词。',
 ('She sang softly while making breakfast.','她做早餐时轻声唱歌。'),('The birds began to sing at dawn.','鸟儿在黎明时开始鸣唱。'))
W('singing','/ˈsɪŋɪŋ/','唱歌、歌唱；鸣唱',
 '把唱这个动作看成一项活动、技能或正在持续的声音。',
 'sing + -ing，中古英语已有相应形式。原词的 /ŋ/ 保留，末尾 -ing 又读 /ɪŋ/，不要额外添 /ɡ/。',IH('sing + -ing → singing','歌唱活动；正在唱、鸣唱'),
 'singing lessons 声乐课，choral singing 合唱，hear singing 听到歌声。可作活动名词或进行时部分。',
 'singing lessons；choral singing；hear singing。',
 'singing 说声音活动，singer 说人，song 说作品；三者在句子里承担不同角色。',
 ('She takes singing lessons every Tuesday.','她每周二上声乐课。'),('We could hear singing from the room upstairs.','我们能听到楼上房间传来歌声。'))
W('singer','英 /ˈsɪŋə/；美 /ˈsɪŋər/','歌手；唱歌的人',
 '做唱歌这件事的人，可能是职业表演者，也可能只是合唱团普通成员。',
 'sing + -er，接中古英语同族人物词。常用歌手义保留 /ŋ/，与 finger 的 /ŋɡ/ 不同；另有来自 singe 的罕见同形词不在本页扩写。',IH('sing + -er → singer','从事或参与唱歌的人'),
 'a lead singer 主唱，a backing singer 伴唱，an opera singer 歌剧演唱者。不是只有明星才叫 singer。',
 'a lead singer；a backing singer；an opera singer。',
 'singer 唱歌者，songwriter 写歌者；一个人可以两者兼任。读音辨清 singer /ŋ/，不用照字母给 g 单独加音。',
 ('The band is looking for a new lead singer.','乐队在寻找新主唱。'),('Several singers joined the choir this year.','今年有几位歌唱者加入合唱团。'))
W('singalong','英 /ˈsɪŋəlɒŋ/；美 /ˈsɪŋəlɔːŋ/ 或 /ˈsɪŋəlɑːŋ/','合唱活动；让大家跟着唱的',
 '有人起个头、放一首熟歌，大家一起跟着唱，不一定排练成正式合唱演出。',
 'sing + along，来自 sing along 跟唱的短语，连写可作名词、形容词。也有分写、连字符拼法，本文只设连写词条。',IH('sing along → singalong','跟着唱 → 大家参与的跟唱活动'),
 'a family singalong 家庭合唱活动，a singalong song 适合大家跟唱的歌；常重参与、熟悉和热闹。',
 'a family singalong；a singalong song；join a singalong。',
 'singalong 关注大家跟唱，choir 合唱团是组织或演唱群体；一群人合唱不必就组成正式 choir。',
 ('The evening ended with a cheerful singalong.','晚上最后以一场欢乐的合唱活动结束。'),('They chose familiar songs for the family singalong.','他们给家庭合唱活动选了熟悉的歌。'))
R('B2750','唱、歌唱活动、歌唱者与跟唱','SING：动作；SINGING：活动；SINGER：人物','sing 后接 singing、singer，再看 singalong 把跟唱活动变成名称。',
 '古英语唱歌动词延续，sing—sang—sung 保留不规则变化。后缀词形规则与元音变化分别认识。',
 'sing—sang—sung；sing + -ing/-er；sing along → singalong。',
 [['动作、活动与人物','sing · singing · singer'],['共同参与','singalong']],
 'sing/singing/singer 的 ng 常读 /ŋ/；singe 燎焦另词；singalong 不必正式合唱团。',
 'The singer encouraged everyone to join the singalong.\n\n歌手鼓励大家一起跟唱。',
 'sing singing singer singalong')
if __name__=='__main__':save('continuation_20261030_ab',ROOTS,WORDS)
