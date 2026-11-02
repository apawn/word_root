"""Zero/cipher doublets and Italian diminutives in familiar loans."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'C0305':dict(words=['zero','cipher','decipher'],label='cipher → decipher；zero 作同源对照',note='de- 在 decipher 中表示解开、去除编码。cipher 与 zero 同接阿拉伯语 sifr 空、零，但借入路线不同；zero、cipher 自身没有 de-。'),
 'B3695':dict(words=['cap','cape','cappuccino'],label='从披风、兜帽到咖啡名称：cappuccino',note='cappuccino 接意大利语兜帽、戴兜帽修士名称，通常把咖啡色联系到其衣帽颜色；这是历史命名链，cape 并非它的现代英语构词底词。'),
}
R('A1985','意大利语小称词尾；英语借词中的 -ino；另有专业领域借用',
 '-INO：在来源语言里把名称缩小、变亲近，再随整词进入英语',
 '小屋可以是 casino 的旧画面；neutrino 的名称有小中性者的意味。借入英语以后，它们各自成为完整名称，现代意思不必仍然小。',
 '意大利语 -ino 是常见小称词尾，往前联系拉丁 -inus。英语常从整词借入认识它；英语物理学还有按 neutrino 等名称类推形成的专业 -ino，本页先学常见借词。',
 'casino 来自 casa 小屋的指小形式；cappuccino 经兜帽、修士名到饮料名，有额外的命名步骤；neutrino 是科学命名。它们并非英语现造的同一种机械拼接。',
 [['生活场所与饮品名称','casino cappuccino'],['科学命名中保留的小称意味','neutrino']],
 '词尾线索需要和真实来源合看。casino 今天通常是赌场，不表示规模一定小；neutrino 不是缩小的 neutron。',
 'We ordered a cappuccino and read an article about neutrinos.\n\n我们点了一杯卡布奇诺，读了一篇关于中微子的文章。',
 'casino cappuccino neutrino')
W('zero','英 /ˈzɪərəʊ/；美 /ˈzɪroʊ/、/ˈziroʊ/','零、零点；没有数量的；把……归零；集中瞄准〔zero in on〕',
 '计数到一个都没有时写 0；刻度从哪里开始，也常标 zero。因此它既能说数量是零，也能说某个量表的零点。',
 '经法语 zéro 或意大利语 zero，往前接中古拉丁 zephirum、阿拉伯语 sifr 空、零。阿拉伯术语承接了梵语空、零的概念翻译；它与 cipher 通过不同路线借入英语。',
 [['梵语空、零概念 → 阿拉伯语 sifr','术语的意义翻译，不是同一声音直接变形'],['阿拉伯 sifr → 中古拉丁 zephirum → 意大利、法语 → zero','数词零的不同语言形式'],['zero 的扩展','数量零；刻度零点；归零、聚焦']],
 'zero degrees 零度；zero errors 零错误；start from zero 从零开始；zero in on a detail 集中注意某细节。zero 后修饰可数名词常用复数。',
 'below zero；zero in on the problem。','温度 zero degrees 是某温标的零刻度，不是完全没有热能。电话读数字时 0 也可能读字母 O 的音，要看惯例和清晰度。',
 ('The temperature dropped below zero overnight.','夜里温度降到了零度以下。'),('The discussion quickly zeroed in on the main problem.','讨论很快聚焦到主要问题上。'),sources=['https://www.etymonline.com/word/zero','https://en.wiktionary.org/wiki/zero#English'])
W('cipher','英 /ˈsaɪfə/；美 /ˈsaɪfər/','密码、秘密编码方式；零〔历史用法〕；无足轻重的人〔贬义〕',
 '把正常文字按一套规则换成别人看不懂的符号，这套秘密写法可以叫 cipher。它最早却是数字零的名称。',
 '经古法语 cifre、中古拉丁 cifra 接阿拉伯语 sifr 空、零。零的符号扩大为数字，早期保密写法常拿数字代字母，因而发展为密码、编码方式；zero 是不同借入路线的同源词。',
 [['阿拉伯 sifr → 中古拉丁 cifra → 古法语 cifre → cipher','空、零 → 零符号、数字'],['数字替代文字的编码 → cipher 的密码义','秘密写法、编码规则；另有零价值的比喻']],
 'a substitution cipher 替换密码；a secret cipher 秘密编码；break a cipher 破解密码；write in cipher 用密码书写。',
 'decode a cipher；an encrypted message。','password 通常是用于验证身份的口令；cipher 常说把信息变得不可直接读懂的规则或写法。a mere cipher 形容人无足轻重，带贬义。',
 ('The children invented a simple cipher for their secret notes.','孩子们为秘密纸条编了一套简单密码。'),('Each letter was replaced by a number in the cipher.','在这套编码中，每个字母都被一个数字替代。'),sources=['https://www.etymonline.com/word/cipher','https://en.wiktionary.org/wiki/cipher#English'])
W('decipher','英 /dɪˈsaɪfə/；美 /dɪˈsaɪfər/','破译；辨认、读懂〔难认的字或难懂的信息〕',
 '纸上有字，但你一时认不出来；或看见了符号，却不知道它说什么。把这层难读懂的障碍解开，就是 decipher。',
 'de- 解开、反向 + cipher 密码、编码，可能也受到法语 déchiffrer 的影响。由解出编码扩大到认出潦草字迹、弄懂难解的信息。',
 [['cipher 密码、编码','以替换等规则隐藏文字意义'],['de- + cipher → decipher','解开编码 → 辨认难读字迹、读懂难解信息']],
 'decipher a message 破译信息；decipher handwriting 辨认笔迹；decipher a faded inscription 辨认褪色铭文。',
 'hard to decipher；try to decipher the note。','decipher 强调原先难以读懂；translate 把一种语言转成另一种语言。字迹太潦草时，即便没有外语和密码，也可以用 decipher。',
 ('Can you decipher the handwriting on this old postcard?','你能辨认这张旧明信片上的笔迹吗？'),('They used the key to decipher the message.','他们用密钥破译了那条信息。'),sources=['https://www.etymonline.com/word/decipher','https://en.wiktionary.org/wiki/decipher#English'])
W('casino','英 /kəˈsiːnəʊ/；美 /kəˈsiːnoʊ/','赌场；娱乐场所〔较早或特定用法〕',
 '今天看到 a casino，通常会想到有赌博设施的娱乐场所。它的旧名称却很朴素：一所小房子。',
 '意大利语 casa 房屋 + 小称 -ino → casino 小屋；随后可指供聚会、音乐、娱乐使用的场所。英语借入后，赌场成为主要意思，实际规模可以很大。',
 [['拉丁 casa → 意大利 casa + -ino → casino','房屋 → 小屋'],['娱乐场所名称 → 英语 casino','聚会娱乐的场所 → 常指赌场']],
 'a casino hotel 赌场酒店；a casino floor 赌场营业大厅；work at a casino 在赌场工作；a large casino 大赌场。',
 'a hotel with a casino；a casino entrance。','-ino 提供旧词源线索，不限制现代建筑大小。casino 接 casa 房屋；cabin、cabinet 接 capanna 小屋，更远关系不明，不能仅凭意思相近就认定同源。',
 ('The hotel has a restaurant, a theatre and a casino.','这家酒店有餐厅、剧院和赌场。'),('The old casino building is now used for concerts.','旧娱乐场所的那栋楼现在用来办音乐会。'),sources=['https://www.etymonline.com/word/casino','https://en.wiktionary.org/wiki/casino#English'])
W('cappuccino','英 /ˌkæpʊˈtʃiːnəʊ/；美 /ˌkæpəˈtʃiːnoʊ/','卡布奇诺咖啡〔浓缩咖啡加蒸奶和奶泡〕',
 '杯里有浓缩咖啡，加入蒸奶，再盖上奶泡，就是常见的 cappuccino。点单时 a cappuccino 是一杯这种咖啡。',
 '借自意大利 cappuccino，名称经嘉布遣会修士的称呼，通常解释为饮料颜色类似其棕色衣帽。往前 cappuccio 是兜帽，-ino 为小称词尾；不是咖啡直接加一个表示小杯的英语词尾。',
 [['披风、兜帽词族 → 意大利 cappuccio、cappuccino','兜帽 → 与戴兜帽修士有关的称呼'],['修士衣帽颜色的命名联系 → 咖啡 cappuccino','通常以棕色相似解释饮料名称']],
 'a cappuccino 一杯卡布奇诺；two cappuccinos 两杯卡布奇诺；a cup of cappuccino 一杯这种咖啡。重音落在 /tʃiː/ 一节。',
 'order a cappuccino；a cappuccino with breakfast。','espresso 是浓缩咖啡；cappuccino 加入蒸奶、奶泡。与 latte 比较时可先抓住奶泡较明显的常见特点，各店的配方会有差异。',
 ('I ordered a cappuccino and a slice of cake.','我点了一杯卡布奇诺和一块蛋糕。'),('The cappuccino had a thick layer of foam on top.','那杯卡布奇诺上面有一层厚奶泡。'),sources=['https://www.etymonline.com/word/cappuccino','https://en.wiktionary.org/wiki/cappuccino#English'])
W('neutrino','英 /njuːˈtriːnəʊ/；美 /nuːˈtriːnoʊ/','中微子',
 '它是一种不带电、质量极小、很少与普通物质发生作用的基本粒子。名字可以先记作小小的中性者，再与中文中微子对应。',
 '意大利语科学名称，接中性相关的 neutr- 和小称词尾 -ino；费米推广了这一名称。词名有小中性者的意味，帮助与 neutron 中子区分；不能据名称推断它是缩小的中子。',
 [['意大利中性词干 + 小称 -ino → neutrino','用于命名轻微、不带电的粒子'],['科学名称进入英语 neutrino','中微子；可数名词']],
 'a neutrino detector 中微子探测器；solar neutrinos 太阳中微子；detect neutrinos 探测中微子。英语常用复数 neutrinos，意大利语复数形式另有 neutrini。',
 'a neutrino experiment；neutrino research。','neutral 是中性、不带电的性质；neutron 是中子；neutrino 是中微子。共同的命名线索不意味着它们的结构或作用相同。',
 ('The exhibition explains how scientists detect neutrinos.','展览解释了科学家怎样探测中微子。'),('Neutrinos have no electric charge.','中微子不带电荷。'),sources=['https://neutrinos.fnal.gov/whats-a-neutrino/','https://en.wiktionary.org/wiki/neutrino#English'])
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_vk',ROOTS,WORDS)
 extend_lessons()
