"""Everyday words whose uncertain or borrowed histories resist forced splitting."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'A1760':dict(words=['fake','faked'],label='伪造、装出与完成的动作',note='fake 的更远来源不确定；faked 清楚对应 fake + -ed。不能因为 fake 与 make 意义近似就断言它必出自拉丁 FAC。'),
 'A2238':dict(words=['barrel'],label='词尾相似的借词对照：barrel',note='barrel 经法语 baril 借入，更远来源未定。即使有与承载、容器材料相连的分析，也不能把它写成现代英语 bear + -le 的确定构词。'),
 'A1699':dict(words=['monkey','jolly'],label='词尾 y 不等于可自由拼接：monkey、jolly',note='monkey 的更早来源有争论，jolly 经法语 jolif、joli 传入，更远来源也未定；本组作为同形词尾对照，不虚构现代 mon、joll 基础词。'),
 'A1839':dict(words=['lame','lameness'],label='步态与说服力：lame 的性质名词',note='lame 的普通跛、蹩脚义承接古英语 lama，lameness 是 lame + -ness。与拉丁 lamina 薄片相关的同形借词另源。'),
 'A1740':dict(words=['lame','lamely'],label='蹩脚、不自信地解释：lame 到 lamely',note='lame + -ly → lamely，常形容说话、辩解显得无力、尴尬；词源取古英语 lama 的那一支。'),
 'A1697':dict(words=['supper'],label='同形词尾对照：supper 的法语来源',note='supper 借自古法语 soper、souper 等晚餐名；不能按 sup + 人物 -er 理解成喝汤的人。'),
}
W('fake','/feɪk/','假的、伪造的；假货、假冒者；伪造、装出',
 '外表像真的，实际上不是。fake ID 是假证件，fake a smile 是装出一个笑，a fake 则可以直接说假货。',
 '较早见于英语俚语的伪造、作假等用法，确切来源不定。有人联系修饰外观、擦亮等词，也有其他说法，不能把某一种猜测写成定论。',
 [['较早英语俚语 fake','假冒、作假相关的使用'],['现代名词、形容词、动词发展','假的；假货或假冒者；伪造、装出']],
 'fake fur 人造仿毛皮；a fake passport 假护照；fake an illness 装病；fake a smile 强装笑容。',
 'a fake painting；fake enthusiasm。','false 范围广，可指事实不真；fake 常突出仿冒、装出来、冒充真的。fake 与 make 意义上的联系不能证明词源必然相同。',
 ('The expert discovered that the painting was a fake.','专家发现那幅画是假货。'),('He faked a smile for the photograph.','拍照时，他强装笑容。'),sources=['https://www.etymonline.com/word/fake','https://en.wiktionary.org/wiki/fake#English'])
W('faked','/feɪkt/','伪造、装出了；伪造的、装出来的',
 'fake 的动作已经发生：笑容是装的，照片是伪造的，具体真假对象由名词决定。',
 'fake 去末尾 e 再接 -ed；末尾 /k/ 后的 -ed 读 /t/。用于一般过去或过去分词，也可修饰伪造的东西。',
 [['fake 作假 + -ed','形成过去式、过去分词'],['faked 的动作与状态用法','伪造了、装出了；被伪造的']],
 'faked documents 伪造文件；a faked photograph 伪造照片；faked surprise 装出的惊讶。',
 'faked evidence；faked an injury。','fake photo 和 faked photo 都可能说假照片；faked 更显出经过作假处理的动作。不能仅凭语法形式判断具体用了什么处理方法。',
 ('The documents had been faked.','这些文件被伪造了。'),('She faked surprise when she saw the present.','看到礼物时，她装出惊讶的样子。'))
W('barrel','/ˈbærəl/','桶；枪管等圆筒部件；快速冲行〔动词〕',
 '先想中间鼓起的大木桶，再看圆筒状的器件。作动词时，barrel down the road 常画出一股劲往前冲的样子。',
 '中古英语 barel 接古法语 baril 桶，更远来源有争议。由容器名发展出装入桶的动词，又有圆筒部件、快速移动等扩展。',
 [['古法语 baril → 中古英语 barel → barrel','圆桶、容器，也可用作容量名称'],['barrel 的形状与动作扩展','枪管等圆筒；装桶；快速冲行']],
 'a wooden barrel 木桶；the barrel of a gun 枪管；barrel down a hill 冲下山坡。容量单位 barrel 的具体大小随用途而异。',
 'a barrel of water；a barrel of laughs。','barrel 常指桶形容器，bucket 常指带提手、上方开口的桶。barrel 的法语借入史不应简化成今天的 bear 加后缀。',
 ('Rainwater was collected in a wooden barrel.','雨水被收集到一个木桶里。'),('A truck came barreling down the road.','一辆卡车沿公路疾冲而来。'),sources=['https://www.etymonline.com/word/barrel','https://en.wiktionary.org/wiki/barrel#English'])
W('monkey','/ˈmʌŋki/','猴子；调皮鬼〔对孩子的昵称〕；乱动、瞎摆弄',
 '动物义最直接；You little monkey! 可以是在打趣调皮孩子。monkey with the controls 则是没个正经地乱摆弄控制装置。',
 '近代英语早期出现 monkey 等形式，可能经欧洲大陆的猴类称呼、故事人物名称传播，确切路径未定。后来动物名发展出调皮的人与胡乱摆弄的动词义。',
 [['较早大陆猴类名称、人物名称等可能线索','英语 monkey 的传入细节有争论'],['现代动物名与行为比喻','猴子；调皮孩子；胡乱摆弄']],
 'a troop of monkeys 一群猴子；a cheeky little monkey 调皮的小家伙；monkey around 胡闹；monkey with something 乱动某物。',
 'a monkey in a tree；stop monkeying around。','monkey 的末尾不能简单拆成一个现代常用基础词 mon 加 -y。对小孩的昵称取决于亲近语境，不是所有称人用法都亲切。',
 ('A monkey climbed onto the branch.','一只猴子爬上树枝。'),('Please don’t monkey with the controls.','请别乱摆弄控制装置。'),sources=['https://www.etymonline.com/word/monkey','https://en.wiktionary.org/wiki/monkey#English'])
W('lame','/leɪm/','跛的、行动不便的；蹩脚的、站不住脚的',
 '动物走路不利索，是具体的 lame；借口缺少支撑、说服不了人，也被说成 a lame excuse。',
 '普通形容词接古英语 lama，经中古英语延续。由肢体行动受限扩展到论证、解释等不够有力；与法语金属薄片、金丝织物的同形词分源。',
 [['古英语 lama → 中古英语 lame','肢体不健全、行动不便'],['形容质量、论证的比喻','无力、蹩脚、不能令人信服']],
 'a lame horse 跛脚的马；a lame excuse 蹩脚借口；a lame attempt 无力的尝试。描述人的残障时，lame 带旧式、可能冒犯的语感。',
 'a lame explanation；go lame。','lamé /læˈmeɪ/ 常指金银线织物，另接法语、拉丁语薄片材料；lame /leɪm/ 的跛、蹩脚义不从 lamina 来。',
 ('The horse went lame during the journey.','那匹马在旅途中跛了。'),('He offered a lame excuse for being late.','他为迟到找了一个蹩脚的借口。'),sources=['https://www.etymonline.com/word/lame','https://en.wiktionary.org/wiki/lame#English'])
W('lamely','/ˈleɪmli/','无力地、蹩脚地；一瘸一拐地',
 '话说出来却连自己都觉得不太站得住，常可用 lamely 描写。它也保留步态不利索的具体义。',
 'lame + -ly，形成方式副词。既能接行动不便的具体义，也能接解释、尝试缺少力量的比喻。',
 [['lame 的跛、无力词义 + -ly','以相应方式行动、表达'],['lamely 的常见叙述用法','无力、尴尬地说；步履不利索地']],
 'explain lamely 无力地解释；say lamely 底气不足地说；walk lamely 一瘸一拐地走。小说对话后常见 lamely。',
 'protest lamely；smile lamely。','quietly 是声音轻，lamely 侧重话语或举止欠有力、不自然。一个人可以说得很响却依然解释得 lamely。',
 ('“I forgot,” he said lamely.','“我忘了。”他底气不足地说。'),('She tried lamely to explain the broken vase.','她试着解释花瓶为何打碎了，却说得很牵强。'))
W('lameness','/ˈleɪmnəs/','跛行、行动不便；蹩脚、缺乏说服力',
 '把 lame 从形容某个对象，变成可以讨论的一种状态：马的跛行，或借口的不可信。',
 'lame + -ness；性质后缀把行动不便、无力的形容词变成抽象名词。不是一种新的动作。',
 [['lame + -ness','把跛、蹩脚的性质名词化'],['lameness 的具体、比喻用法','跛行状态；解释等的无力']],
 'lameness in a horse 马的跛行；the lameness of an excuse 借口的蹩脚；show signs of lameness 表现出跛行。',
 'the cause of lameness；obvious lameness。','lame 是形容词，lameness 是性质名词。步态义常见于动物描述；不是泛指一切运动障碍的精确专业分类。',
 ('The report describes lameness in one of the horses.','报告描述了其中一匹马的跛行情况。'),('The lameness of his excuse was obvious.','他的借口有多蹩脚，一听就知道。'))
W('jolly','英 /ˈdʒɒli/；美 /ˈdʒɑːli/','愉快、乐呵呵的；很、相当〔英式口语〕',
 '人笑呵呵，聚会热闹愉快，常可叫 jolly。英式口语中 jolly good 又把它当程度词说“真不错”。',
 '中古英语 joli、jolif 接古法语 joli、jolif 欢乐、节庆等义，更远来源未定。现代副词程度用法来自较早强烈、令人赞赏等表达。',
 [['古法语 joli、jolif → 中古英语相关形式','欢快、令人愉悦'],['现代 jolly 的形容词与程度词','乐呵呵的；英式口语很、相当']],
 'a jolly person 乐呵呵的人；a jolly evening 愉快的夜晚；jolly good 真不错。部分表达带传统英式语气。',
 'a jolly laugh；jolly well。','jolly 不能只凭末尾 y 拆成现代 joll + -y；它有法语整词借入史。happy 更通用，jolly 常更显外露、热闹的愉快。',
 ('He greeted us with a jolly laugh.','他笑呵呵地向我们打招呼。'),('We had a jolly evening together.','我们一起度过了一个愉快的夜晚。'),sources=['https://www.etymonline.com/word/jolly','https://en.wiktionary.org/wiki/jolly#English'])
W('supper','英 /ˈsʌpə/；美 /ˈsʌpər/','晚饭；晚间较简单的一餐、夜宵〔随习惯而异〕',
 '一天晚些时候吃的一餐。有人把正常晚饭叫 supper，有人用它指更晚、更轻便的一餐，要跟着家庭、地区习惯理解。',
 '中古英语 soper 接古法语 soper、souper 晚餐，较早是吃晚饭动词的名词用法，与汤、浸食等旧词族相连。不是现代 sup 加人物 -er。',
 [['古法语 soper、souper 的吃晚餐、晚餐用法','动词不定式也用作餐名'],['英语 supper 的地区、家庭习惯','晚饭；晚间较简单或更晚的一餐']],
 'have supper 吃晚饭；come over for supper 过来吃晚饭；a light supper 一顿清淡的晚餐。通常不在普通餐名之前随意加 the。',
 'supper is ready；after supper。','dinner 常指一天的主餐，很多人用来叫晚餐；supper 常较家常。两者并没有适用于所有地区、家庭的固定钟点界线。',
 ('Supper will be ready in ten minutes.','晚饭再过十分钟就好了。'),('Would you like to stay for supper?','你愿意留下吃晚饭吗？'),sources=['https://www.etymonline.com/word/supper','https://en.wiktionary.org/wiki/supper#English'])
def extend_lessons():
    extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
    save('continuation_20261030_to',ROOTS,WORDS)
    extend_lessons()
