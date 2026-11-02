"""Everyday objects: lights, keys, pens, phones, dishes and glasses."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'B2891':dict(words=['light','lights'],label='light → lights：光源、灯与点亮',note='本组讲光的 light 词族；轻的 light 有另一条较早来源。'),
 'C0647':dict(words=['lamp','lamps'],label='lamp → lamps：火炬、灯与发光',note='希腊灯、火炬词经拉丁、法语借入，lamp 整体保留借词历史。'),
 'B3120':dict(words=['key','keys'],label='key → keys：开锁工具、按键与答案关键',note='本族钥匙词与音乐语境的拉丁 clavis 影响共同参与相关意义发展。'),
 'C0992':dict(words=['pen','pens'],label='pen → pens：羽毛、笔与写作；畜栏另源',note='写字的 pen 接拉丁 penna 羽毛；动物栏 pen 接古英语另一旧词。'),
 'B2477':dict(words=['pencil','pencils'],label='pencil → pencils：小尾巴、画笔到石墨笔',note='拉丁小尾巴、画笔词经法语传入，工具改变而名称延续。'),
 'C1025':dict(words=['phone','phones'],label='telephone → phone → phones：电话缩短与打电话',note='本组采用日常电话义，phone 缩短自 telephone，并可作动词。'),
 'B3528':dict(words=['cup','cups'],label='cup → cups：杯子、杯中量与杯形容器',note='较早英语和拉丁相关容器词合流，现代可数杯子也可用来量一杯。'),
 'B3060':dict(words=['plate','plates'],label='plate → plates：薄平片、盘子与牌板',note='金属薄片等旧义，经平面形状扩展到餐盘、牌板等。'),
 'B2808':dict(words=['dish','dishes'],label='dish → dishes：盛食物的器物与盘中菜',note='希腊、拉丁盘器词很早借入日耳曼语成为 dish，与 desk、disk 各走不同后续路线。'),
 'B3358':dict(words=['glass','glasses'],label='glass → glasses：玻璃器皿与眼镜',note='材料名扩展到杯子、镜片与眼镜，glass 材料总体与 glasses 可数、固定复数用法分开。'),
 'B3016':dict(words=['bottle','bottles'],label='bottle → bottles：桶的小称与装瓶',note='较早法语、拉丁小容器名称借入；英语现代可作装瓶、压住情绪等动词。'),
 'B3021':dict(words=['box','boxes'],label='box → boxes：盒与装盒；拳击另有词族',note='容器词接古英语及拉丁相关木盒词，拳击动词的旧一击词来源另辨。'),
}
W('lights','/laɪts/','灯、光源〔复数〕；点亮、照亮、点燃〔第三人称单数〕',
 '一盏盏发光、让人看清东西的灯，是 lights；把灯点亮、让火燃起来，也可以用动词 lights。',
 'light + -s，/t/ 后读 /s/。光的 light 词族继承古英语 lēoht 等；名词、形容词、相关动词发展出照明、点燃用法。重量轻的 light 是另一条来源。',
 [['古英语光的词族 → light','光、明亮；照明、点亮'],['light + -s → lights','多盏灯、多个光源；单数主语点亮']],
 'traffic lights 交通信号灯；street lights 路灯；switch off the lights 关灯；lights a candle 点燃蜡烛。',
 'lights in the window；the lamp lights the room。','light 不可数地说光，lights 常数一个个灯、光源。lights a fire 中是动词点燃，The lights are on 中则是复数名词。',
 ('The lights in the hall came on as we entered.','我们进去时，礼堂里的灯亮了起来。'),('She lights a candle on the table.','她点燃了桌上的一支蜡烛。'),sources=['https://en.wiktionary.org/wiki/lights#English','https://en.wiktionary.org/wiki/light#English'])
W('lamps','/læmps/','灯；照明灯具〔lamp 的复数〕',
 '一件专门用来发光、照明的器具，是 lamp；桌灯、落地灯、旧油灯都是具体画面，多件就是 lamps。',
 'lamp + -s，/p/ 后读 /s/。lamp 经古法语 lampe、拉丁 lampas 接希腊 lampás 火炬、灯，与 lámpein 发光相连。',
 [['希腊 lampás、lámpein → 拉丁、法语 → lamp','火炬、发光 → 灯具'],['lamp + -s → lamps','多件照明器具']],
 'table lamps 台灯；oil lamps 油灯；reading lamps 阅读灯；floor lamps 落地灯。',
 'lamps beside the beds；lamps with adjustable arms。','lamp 更侧重灯具本身，light 可说光或灯。table lamps 是摆在桌面的灯，floor lamps 是立在地上的灯，前面的名词说明使用位置。',
 ('Small lamps stood beside both beds.','两张床旁都摆着小灯。'),('The museum displays old oil lamps from the region.','博物馆展示着这个地区的老油灯。'),sources=['https://en.wiktionary.org/wiki/lamps#English','https://en.wiktionary.org/wiki/lamp#English'])
W('keys','/kiːz/','钥匙；键；调；答案、关键〔复数〕；键入〔第三人称单数〕',
 '能把锁打开的是 keys；能把问题打开的答案、关键，也沿用钥匙的形象。键盘的键和音乐的调则有各自的专业发展。',
 'key + -s，元音后读 /z/；y 前是元音 e，保留 y。key 继承古英语 cǣġ，远源不定；音乐相关义还受拉丁 clāvis 钥匙及相关传统影响，不只是一条现代开门比喻。',
 [['古英语 cǣġ → key；音乐传统另有 clāvis 影响','钥匙 → 关键、按键；调等专门义'],['key + -s → keys','多把钥匙、多个键或答案；单数主语键入']],
 'house keys 房门钥匙；piano keys 钢琴键；answer keys 参考答案；keys in the number 键入数字。',
 'the keys to the cupboard；press the keys。','keys 的复数直接加 s，与 valleys 相同；reply 的 y 前是辅音，复数 replies。answer keys 是列出答案的材料，the key to something 常说某事的关键。',
 ('She left her keys on the kitchen table.','她把钥匙落在了厨房桌上。'),('The answer keys are printed at the back of the book.','参考答案印在书的后面。'),sources=['https://en.wiktionary.org/wiki/keys#English','https://en.wiktionary.org/wiki/key#English'])
W('pens','/penz/','笔；动物围栏〔复数，另源〕；写作〔第三人称单数〕',
 '拿来写字的笔是 pens；把动物围住的一间间栏也叫 pens，但这是另一条来源。动词 pens 则常说写下一篇作品、文字。',
 'pen + -s，/n/ 后读 /z/。写字 pen 经法语 penne 接拉丁 penna 羽毛，晚期拉丁已有笔义；动物栏 pen 接古英语 penn，较远来源不定；写作动词由笔的名词发展。',
 [['拉丁 penna → 法语 → 英语 pen','羽毛 → 写字笔；写作'],['另一来源：古英语 penn → pen','动物围栏'],['pen + -s → pens','多支笔、多间栏；单数主语写作']],
 'fountain pens 钢笔；ballpoint pens 圆珠笔；sheep pens 羊栏；pens a letter 写一封信〔偏书面〕。',
 'pens on the desk；animals in separate pens。','pen 的笔义与 pencil 的铅笔义有不同来源；pens 在农场、动物场景可能说围栏，不能只看拼写就译成笔。',
 ('She keeps spare pens in the top drawer.','她把备用笔放在最上层抽屉里。'),('The sheep were moved into separate pens.','羊被赶进了不同的围栏。'),sources=['https://en.wiktionary.org/wiki/pens#English','https://en.wiktionary.org/wiki/pen#English'])
W('pencils','/ˈpensəlz/','铅笔；用铅笔写画、暂记〔第三人称单数〕',
 '能写、能画，普通石墨痕迹也较容易擦掉的笔，是 pencils；暂时先把安排记上，常用 pencils in 来表达。名字的更早画面却是一支细毛笔。',
 'pencil + -s，/l/ 后读 /z/。较早拉丁 pēnis 尾巴，经小称 pēniculus 刷子、再小称 pēnicillus 细画笔，后来经法语 pincel 或相关中世纪拉丁形式进入英语；工具从毛笔转到石墨笔，名称延续。',
 [['拉丁尾巴词的小称 → pēniculus、pēnicillus','小尾巴、毛束 → 刷子、细画笔'],['法语 pincel 等 → 英语 pencil → pencils','画笔 → 石墨笔；再加复数或第三人称词尾']],
 'coloured pencils 彩色铅笔；sharpen pencils 削铅笔；pencils in a date 暂定一个日期。',
 'pencils for sketching；a box of pencils。','pen 的笔义接羽毛词，pencil 接尾巴、刷子的小称词族。pencil in 暂定，利用铅笔记录可修改的用途；日常铅笔芯主要是石墨材料。',
 ('The children used coloured pencils to draw the garden.','孩子们用彩色铅笔画花园。'),('She pencils in a meeting for the following week.','她暂时把会议安排在下一周。'),sources=['https://en.wiktionary.org/wiki/pencils#English','https://www.etymonline.com/word/pencil'])
W('phones','英 /fəʊnz/；美 /foʊnz/','电话、手机〔复数〕；打电话〔第三人称单数〕',
 '拿来远距离通话的设备，是 phones；今天经常直接指手机。一个人给别人打电话，也能用动词 phones。',
 'phone + -s，/n/ 后读 /z/。日常电话义 phone 缩短自 telephone，后可用作打电话的动词；telephone 较早含 tele- 远与希腊 phōnḗ 声音的材料。',
 [['tele- + phōnḗ 的近代组合 → telephone → phone','远处的声音 → 电话；缩短形式'],['phone + -s → phones','多部电话、手机；单数主语打电话']],
 'mobile phones 手机；phones on silent 静音的手机；phones her parents 给父母打电话；phones the office 给办公室打电话。',
 'answer the phones；phones every Sunday。','phones 作动词常直接接人、机构，如 phones her sister。mobile phone、cell phone 都可说手机，地区习惯不同，phone 单独用时靠语境判断设备。',
 ('Please keep your phones silent during the talk.','讲座期间，请把手机调成静音。'),('She phones her grandparents every Sunday.','她每周日都会给祖父母打电话。'),sources=['https://en.wiktionary.org/wiki/phones#English','https://en.wiktionary.org/wiki/phone#English'])
W('cups','/kʌps/','杯子；若干杯的量；杯形物〔复数〕',
 '能盛饮料的一只只小容器，是 cups；里面装的一杯东西，也可以直接用 cup 计数。奖杯、杯形容器借用相似形状。',
 'cup + -s，/p/ 后读 /s/。cup 的较早英语形式有 cuppe、copp 等，并涉及晚期拉丁 cuppa 等容器名称，更远的各支关系不全确定。',
 [['较早英语及拉丁相关容器词 → cup','盛饮料等的小容器'],['cup + -s → cups','多只杯子；多杯的量、杯形物']],
 'cups of tea 几杯茶；measuring cups 量杯；paper cups 纸杯；cups on the shelf 架上的杯子。',
 'two cups of water；wash the cups。','two cups 可以数两只杯，也可说两杯容量，后接 of 常说明装什么。配方里的 cup 作为计量单位，具体容量按所用体系看，不只按杯子外形猜。',
 ('She placed two cups of tea on the table.','她把两杯茶放在桌上。'),('The cups were stacked beside the sink.','杯子摞在水槽旁。'),sources=['https://en.wiktionary.org/wiki/cups#English','https://en.wiktionary.org/wiki/cup#English'])
W('plates','/pleɪts/','盘子；薄片、板；牌照；板块〔复数〕',
 '一块比较薄、平的东西，是 plate 的形状线索；餐盘、金属板、车牌、地球构造的板块，都各自发展出专门用法。',
 'plate + -s，/t/ 后读 /s/。plate 经古法语接中世纪拉丁 plata 金属薄片，较早通常联系 *plattus 及希腊 platýs 宽、平；星号表示重建形式。',
 [['较早宽、平词族 → 拉丁、法语相关形式 → plate','薄平片、板 → 盘等器物'],['plate + -s → plates','多个盘子、牌板或板块']],
 'dinner plates 餐盘；metal plates 金属板；number plates 车牌；tectonic plates 构造板块。',
 'plates on the table；plates fitted together。','plate 常指较平的盘或板，bowl 通常更深、适合盛汤等。dish 范围更广，也可说一道菜；The plates are empty 说盘子空了，The dishes are delicious 说菜好吃。',
 ('She set the plates around the table.','她沿桌边摆好了盘子。'),('The sign was made from two thin metal plates.','这块标牌用两块薄金属板做成。'),sources=['https://en.wiktionary.org/wiki/plates#English','https://en.wiktionary.org/wiki/plate#English','https://www.etymonline.com/word/plate'])
W('dishes','/ˈdɪʃɪz/','盘、碟等餐具；菜肴〔复数〕；分发食物等〔dishes out〕',
 '装食物的器具是 dishes；里面做好的那一道道食物，也可以叫 dishes。日常 do the dishes 就是清洗吃饭用过的餐具。',
 'dish + -es，/ʃ/ 后增加 /ɪz/。dish 继承古英语 disc，经中古英语 dissh、disch 发展，较早是拉丁 discus、希腊 dískos 盘的借词背景；容器名再用于盘中菜肴。',
 [['希腊 dískos、拉丁 discus → 日耳曼借词、古英语 disc → dish','盘类器物'],['dish + -es → dishes；容器与内容的扩展','多件餐具；多道菜；动词分发等用法']],
 'wash the dishes 洗餐具；local dishes 当地菜肴；side dishes 配菜；dishes out the food 分发食物。',
 'do the dishes；a choice of hot dishes。','dishes 在厨房收拾语境常指餐具，在菜单里通常是菜肴。desk、disk 与 dish 有较早词源联系，但现代已各有自己的用法。',
 ('I will wash the dishes after dinner.','晚饭后我来洗餐具。'),('The restaurant serves several local dishes.','这家餐馆供应几道当地菜。'),sources=['https://en.wiktionary.org/wiki/dishes#English','https://en.wiktionary.org/wiki/dish#English'])
W('glasses','英 /ˈɡlɑːsɪz/；美 /ˈɡlæsɪz/','玻璃杯〔复数〕；眼镜〔常用复数形式〕',
 '玻璃做成的一只只杯子，叫 glasses；把镜片装成帮助看清的器具，也叫 glasses。具体说喝水还是看东西，语境通常很清楚。',
 'glass + -es，/s/ 后增加 /ɪz/。glass 继承古英语 glæs 的玻璃词，器皿、镜片、眼镜的名称由材料与用途扩展；更远词源不强作确定解释。',
 [['古英语 glæs → glass','玻璃材料；由材料扩到杯子、光学器具'],['glass + -es → glasses','多个玻璃杯；眼镜的固定复数用法']],
 'drinking glasses 玻璃饮水杯；two glasses of water 两杯水；wear glasses 戴眼镜；reading glasses 阅读眼镜。',
 'a pair of glasses；glasses on the table。','glass 作材料通常不可数；a glass 可说一只杯子，glasses 是多只杯子。眼镜通常用复数 glasses，一副可说 a pair of glasses。',
 ('She put two clean glasses beside the bottle.','她把两个干净玻璃杯放在瓶子旁。'),('He needs his glasses to read the small print.','他需要戴眼镜才能看清小字。'),sources=['https://en.wiktionary.org/wiki/glasses#English','https://en.wiktionary.org/wiki/glass#English'])
W('bottles','英 /ˈbɒtəlz/；美 /ˈbɑːtəlz/','瓶子；装瓶〔第三人称单数〕；压住不说〔bottles up〕',
 '细口、能装液体的容器，是 bottles；把饮料装进瓶子，动词也用 bottle。把情绪一直关在里面不表达，便有 bottles up 的比喻。',
 'bottle + -s，/l/ 后读 /z/。bottle 经古法语 boteille，较早常重建为通俗拉丁 *butticula，接 buttis 桶的小称；星号表示重建形式。英语由名词又发展出装瓶、封存等动词。',
 [['较早 buttis、*butticula → 法语 boteille → bottle','桶、小容器 → 瓶子'],['bottle + -s → bottles；名词转动词','多个瓶子；装瓶；将感受封在里面的比喻']],
 'water bottles 水瓶；glass bottles 玻璃瓶；bottles the juice 把果汁装瓶；bottles up his feelings 把感受憋在心里。',
 'empty bottles；bottles of water。','bottles of water 是一瓶瓶水，water bottles 可以说用来装水的瓶子。bottles up 在感受语境常说把情绪压在心里、没有表达出来。',
 ('We filled the bottles before leaving the house.','出门前，我们把瓶子装满了。'),('He bottles up his feelings when he is upset.','他不高兴时常把感受憋在心里。'),sources=['https://en.wiktionary.org/wiki/bottles#English','https://www.etymonline.com/word/bottle'])
W('boxes','英 /ˈbɒksɪz/；美 /ˈbɑːksɪz/','盒、箱；框、格〔复数〕；装盒；练拳击〔第三人称单数，另一支〕',
 '把东西装进有边框的容器，是 boxes 的盒、箱分支；界面上圈出的框、格也用这个形象。拳击动词另接较早的一击词义，历史要分开读。',
 'box + -es，/s/ 前还有 /k/，整体增加 /ɪz/。容器词古英语已有 box，较早接拉丁 buxis、希腊相关黄杨木、木盒名称；装盒动词由容器名发展。拳击动词则接旧名词 box 一击，更远来源及其与容器词的关系未定。',
 [['古英语 box；更早希腊、拉丁木盒相关词 → box','容器、木盒 → 箱、框；装盒'],['另一支：中古英语 box 一击 → 拳击动词','拳头击打；更远关系不定'],['box + -es → boxes','多个盒、框；单数主语装盒、练拳击等']],
 'cardboard boxes 纸箱；tick the boxes 勾选方框；boxes the books 把书装箱；boxes at a sports club 在体育俱乐部练拳击。',
 'boxes stacked by the door；boxes on the form。','box 的容器、界面框沿相连的分支发展，拳击有另一条直接历史线索。boxes 的 /ksɪz/ 增加音节，和 books /bʊks/ 的结尾不同。',
 ('The books were packed in three cardboard boxes.','这些书装在三个纸箱里。'),('Please tick the boxes beside the items you need.','请在所需项目旁的方框里打勾。'),('He boxes at the local sports club twice a week.','他每周两次在当地体育俱乐部练拳击。'),sources=['https://en.wiktionary.org/wiki/boxes#English','https://www.etymonline.com/word/box'])
def extend_lessons():
 extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_yg',ROOTS,WORDS)
 extend_lessons()
