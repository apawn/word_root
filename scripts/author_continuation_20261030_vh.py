"""Everyday names: reanalysis, diminutives and useful plural forms."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'A1776':dict(words=['cherry','cherries','pea','peas','orange','oranges'],label='先看单数怎样形成，再看今天怎样变复数',note='cherry、pea 都经历过把旧词尾误当复数、再倒推出新单数的过程；今天 cherries、peas、oranges 又按现代规则组成复数。'),
 'B3543':dict(words=['pea','peas'],label='pea → peas：旧词重新分析后形成的新单复数',note='旧 pease 原可作单数或集合词，词尾后来被当成复数；现代 pea 是倒推得到的单数，peas 才是今天常用的复数。'),
 'A1779':dict(words=['napkin','napkins','apron'],label='napkin 与 apron：同一旧布词走出的两条路',note='napkin 的 -kin 是小称后缀；apron 供同源对照，经法语 naperon 和英语 a napron → an apron 形成，apron 自身没有 -kin。'),
 'B2431':dict(words=['name','nickname','nicknamed'],label='name → nickname → nicknamed',note='nickname 原是额外的名字，历史上 an eke name 的 n 被重新划到后面的词；现代可作名词，也可作动词给人起绰号。'),
 'B2451':dict(words=['orange','oranges'],label='orange → oranges：水果与颜色、单数与复数',note='orange 先是水果名，后来成为颜色名；oranges 在已有 e 的单数后加 s。更早 n 的消失发生在传入英语之前的罗曼语形式中。'),
}
W('cherry','/ˈtʃeri/','樱桃；樱桃树；樱桃红色的',
 '先想一颗有细梗、果肉包着硬核的樱桃。a cherry 是一颗，cherry juice 中 cherry 则说明果汁的种类。',
 '经中古英语、盎格鲁法语 cherise，往前接通俗拉丁 *ceresia 和希腊樱桃名称。中古英语使用者把旧词尾误当复数，去掉它，倒推出 cherry；现代不再拆成 cher + ry。',
 [['希腊樱桃名 → 拉丁、法语相关形式','树与果实的名称随语言接触传播'],['中古英语 cherise → cherry','旧词尾被误认成复数，倒推新单数'],['cherry → cherries','现代再按 y → ies 组成复数']],
 'a cherry 一颗樱桃；a cherry tree 樱桃树；cherry juice 樱桃汁；cherry red 樱桃红。单数可指果实或树，要看上下文。',
 'a bowl of cherries；cherry blossoms。','果实可数：three cherries。cherry juice、cherry trees 中前面的 cherry 作修饰语，通常保留单数。词源更早的树名来源仍有不确定处。',
 ('She placed a cherry on top of the cake.','她在蛋糕顶上放了一颗樱桃。'),('The cherry tree outside our window is in bloom.','窗外的樱桃树开花了。'),sources=['https://www.etymonline.com/word/cherry','https://en.wiktionary.org/wiki/cherry#English'])
W('cherries','/ˈtʃeriz/','樱桃〔复数〕；樱桃树〔复数〕',
 '一颗叫 a cherry，一碗里有许多颗，就是 cherries。它也可说多棵樱桃树，场景会告诉你是哪一种。',
 '现代 cherry 的复数：辅音字母 r 后的 y 改成 ies，结尾读 /iz/；这是 /i/ 元音接复数 /z/，全词两音节。历史上的 cherise 曾被误当复数，现代 cherries 是在新单数上重新组成的复数。',
 [['旧 cherise → cherry','历史上由误认复数倒推出单数'],['cherry 的 y → ies → cherries','现代规则复数，果实或树不止一个']],
 'fresh cherries 新鲜樱桃；a handful of cherries 一把樱桃；pick cherries 摘樱桃；cherries are ripe 樱桃熟了。',
 'a bowl of cherries；sweet cherries。','life is not a bowl of cherries 是生活并不总是轻松美好。先抓住碗里一颗颗甜樱桃的画面，再理解这个比喻。',
 ('We bought a small bag of cherries at the market.','我们在市场买了一小袋樱桃。'),('The children picked cherries from the lower branches.','孩子们从较低的树枝上摘樱桃。'),sources=['https://www.etymonline.com/word/cherry','https://en.wiktionary.org/wiki/cherries#English'])
W('peas','/piːz/','豌豆〔复数〕',
 '盘子里一粒粒圆圆的豌豆，通常不只一粒，所以吃饭时经常听到 peas。说其中一粒，才用 a pea。',
 'pea + 复数 -s，元音后读 /z/。更早的 pease 本来可表示单个或一类豌豆；末尾后来被理解成复数，倒推出 pea，再形成现代 peas。',
 [['古英语、拉丁语豌豆名 → pease','原可作单数、集合词'],['pease → pea → peas','先由重新分析得到单数，再加现代复数 s']],
 'green peas 青豌豆；frozen peas 冷冻豌豆；peas and carrots 豌豆和胡萝卜；shell peas 剥豌豆。pea soup 中 pea 作前置修饰语，用单数。',
 'a bag of frozen peas；a spoonful of peas。','peas 末尾有声 /z/，peace 和 piece 是 /piːs/。不要因为意思像集合食物就写 a peas：一粒应是 a pea。',
 ('Add the peas during the last few minutes of cooking.','快煮好时再把豌豆加进去。'),('One pea rolled off the plate, but the other peas stayed put.','一粒豌豆滚出了盘子，其他豌豆还在原处。'),sources=['https://www.etymonline.com/word/pea','https://en.wiktionary.org/wiki/peas#English'])
W('apron','/ˈeɪprən/','围裙',
 '做饭、木工或其他工作前，把一层布系在衣服前面，挡住油点、灰尘：这就是 apron。',
 '拉丁 mappa 布 → 古法语 nappe、指小形式 naperon → 中古英语 napron。连说 a napron 时，n 被重新划给前面的冠词，成了 an apron；今天 a 不是可拆的前缀。',
 [['拉丁 mappa → 法语 nappe、naperon','布 → 小块布、护在身前的布'],['中古英语 a napron → an apron','词与冠词的边界重新划分，n 转到冠词一边'],['英语 apron','围裙']],
 'put on an apron 穿上围裙；tie an apron 系好围裙；a kitchen apron 厨房围裙；an apron pocket 围裙口袋。',
 'wear an apron；a floury apron。','napkin 和 apron 接到同一旧布词，但走不同的小称、借入路线。napkin 有 -kin，apron 经法语 naperon；不能把 apron 解释成 napkin 直接变来的。',
 ('He put on an apron before he started baking.','开始烘焙前，他穿上了围裙。'),('She kept a pencil in the pocket of her apron.','她在围裙口袋里放了一支铅笔。'),sources=['https://www.etymonline.com/word/apron','https://www.etymonline.com/word/napkin','https://en.wiktionary.org/wiki/apron#English'])
W('nickname','/ˈnɪkneɪm/','昵称、绰号、别名；给……起绰号',
 '正式名字之外，大家又给你一个常叫的名字。这个额外的叫法可能亲昵，也可能带取笑意味，就是 nickname。',
 '历史上 eke 表示增加，eke name 是额外的名字。an eke name 被重新听成 a neke name，冠词的 n 进了后面的词，逐渐形成 nickname；现代可整体作动词。',
 [['古英语增加词 → 中古英语 eke name','额外增加的名字'],['an eke name → a neke name → nickname','n 从冠词一侧重新划入名词'],['名词 nickname → 动词 nickname','别名 → 给人或事物起别名']],
 'have a nickname 有绰号；go by a nickname 用昵称；give someone a nickname 给某人起绰号；nickname someone ... 给某人起名为……。',
 'a childhood nickname；be known by a nickname。','nickname 比 name 多一个额外叫法的角度；不保证友好。pen name 是笔名，screen name 是网络或屏幕显示名，范围各有侧重。',
 ('Most of her friends know her by her nickname.','她的大多数朋友都用昵称称呼她。'),('The team nicknamed their old van Rocket.','队员们给那辆旧面包车起了个绰号，叫“火箭”。'),sources=['https://www.etymonline.com/word/nickname','https://en.wiktionary.org/wiki/nickname#English'])
W('nicknamed','/ˈnɪkneɪmd/','给……起了绰号；被昵称为……；nickname 的过去式、过去分词',
 '先有一个额外的叫法，再说大家已经这么叫了：nicknamed。常见被动句把绰号直接接在后面。',
 'nickname 去末尾 e，加完整 -ed；词末 /m/ 后的 -ed 读 /d/。动词来自额外名字的名词 nickname，过去形式保留这一给出称呼的意思。',
 [['额外名字 → nickname','正式名称以外的叫法；也作动词'],['nickname 去 e + -ed → nicknamed','起了绰号；被起了绰号']],
 'be nicknamed ... 被昵称为……；a player nicknamed ... 一位绰号叫……的球员；nicknamed after something 因某物的名字、特点而得到绰号。',
 'a town nicknamed ...；they nicknamed him ...。','be nicknamed 可以直接接具体称呼；这个结构强调叫法，不等于正式改名的 be renamed。',
 ('Her classmates nicknamed her Sunny because she was always cheerful.','同学们给她起了个绰号叫 Sunny，因为她总是很开朗。'),('The tiny office was nicknamed the Cupboard.','那间很小的办公室被戏称为“小橱柜”。'),sources=['https://www.etymonline.com/word/nickname','https://en.wiktionary.org/wiki/nicknamed#English'])
W('oranges','英 /ˈɒrɪndʒɪz/；美常 /ˈɔːrɪndʒɪz/','橙子〔复数〕；多种橙色、橙色调〔特定语境〕',
 '购物袋里有好几个橙子，就是 oranges。画画时 oranges 也可能说几种橙色，要从水果还是颜色的语境判断。',
 'orange 已以 e 结尾，写法是 orange + s；因为单数末尾读 /dʒ/，复数词尾读 /ɪz/。水果名称经法语等传入，更早的 n 在进入英语前的罗曼语变化中消失。',
 [['亚洲语言的水果名 → 欧洲语言 → orange','水果名传入英语，后来也作颜色名'],['orange + -s → oranges','多个水果；在调色等场景也说多种橙色']],
 'peel oranges 剥橙子；a bag of oranges 一袋橙子；fresh oranges 新鲜橙子；warm oranges and reds 暖橙色和红色调。orange juice 的 orange 用单数作修饰。',
 'three oranges；oranges for breakfast。','a norange → an orange 不是已证实的英语演变故事。可比较 apron 的词界变化，但 orange 的相关变化发生在借入英语之前，且细节有不同解释。',
 ('We bought six oranges and a loaf of bread.','我们买了六个橙子和一条面包。'),('The painting is full of warm oranges and reds.','这幅画中有许多暖橙色和红色调。'),sources=['https://www.etymonline.com/word/orange','https://en.wiktionary.org/wiki/oranges#English'])
W('napkins','/ˈnæpkɪnz/','餐巾、餐巾纸〔复数〕',
 '餐桌上用来擦嘴、擦手或铺在膝上的小巾，可以是布的，也可以是纸的。多张、多块就用 napkins。',
 'napkin + -s，/n/ 后复数读 /z/。napkin 更早由旧 nape 布和表示小的 -kin 组成，后来成为固定的餐巾名称。',
 [['旧 nape 布 + -kin 小 → napkin','小布 → 用餐时使用的巾'],['napkin + -s → napkins','多张、块餐巾；材质由修饰语说明']],
 'paper napkins 餐巾纸；cloth napkins 布餐巾；fold the napkins 折餐巾；pass the napkins 把餐巾递过去。',
 'a stack of napkins；clean napkins。','tissues 常说抽取的面巾纸等，napkins 突出用餐用途。cloth napkins 是布，不宜把每个 napkin 都翻译成纸巾。',
 ('Could you put some napkins on the table?','能在桌上放些餐巾吗？'),('The restaurant uses cloth napkins instead of paper ones.','这家餐馆使用布餐巾，而不是餐巾纸。'),sources=['https://www.etymonline.com/word/napkin','https://en.wiktionary.org/wiki/napkins#English'])
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_vh',ROOTS,WORDS)
 extend_lessons()
