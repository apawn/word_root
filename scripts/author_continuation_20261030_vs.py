"""Frequent f/fe plurals and leaves/lives homographs."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'B3083':dict(words=['knife','knives'],label='knife → knives：刀具的复数',note='名词复数写 knives，f 对应 v，开头 k 仍不发音；与动词 knifes 分开看。'),
 'B3448':dict(words=['leaf','leaves'],label='leaf → leaves：叶、书页的复数',note='普通名词复数 leaves；同形的 leaves 还能是另一个底词 leave 的动词形式，精讲分别说明。'),
 'B2888':dict(words=['leave','leaves'],label='leave → leaves：单数主语的离开、留下',note='leaves 既可为 leaf 叶子的复数，也可为 leave 的第三人称单数，二者常同音但词法不同。'),
 'B2799':dict(words=['wife','wives'],label='wife → wives：妻子的复数',note='fe 改成 ves，读 /waɪvz/；复数、单数所有格与复数所有格的写法分别说明。'),
 'B2454':dict(words=['wolf','wolves'],label='wolf → wolves：狼的复数',note='f 对应 v，名词狼的复数 wolves 与动词 wolf 的第三人称单数 wolfs 分开。'),
 'B3406':dict(words=['shelf','shelves'],label='shelf → shelves：架板的复数与动词搁置',note='shelves 也是 shelve 的第三人称单数；单个 shelf 常是一层架板，多个层板构成一组架子。'),
 'B3257':dict(words=['half','halves'],label='half → halves：一半、多份一半与减半',note='名词 half 复数写 halves，l 常不发音；halves 也可对应动词 halve 的第三人称单数。'),
 'B3076':dict(words=['life','lives'],label='life → lives：生命、生活的复数',note='名词 lives 读 /laɪvz/，动词 live 的第三人称单数 lives 读 /lɪvz/。'),
 'B3101':dict(words=['live','lives'],label='live → lives：居住、生活的单数主语动作',note='动词 lives 读 /lɪvz/，与 life 生命的复数 /laɪvz/ 同拼写、不同读音。'),
 'A1788':dict(words=['thief','thieves'],label='thief → thieves：窃贼的复数',note='名词 thief 复数的 f 对应 v；与 theft 盗窃名词是相关词，不把 theft 当成现代复数。'),
 'B3628':dict(words=['roof','roofs'],label='roof → roofs：f 结尾的对照',note='标准复数拼写 roofs；常读 /ruːfs/，也有词典记录的 /ruːvz/ 等读音差异。拼写与读音须分别看，不能一律改成 rooves。'),
}
W('knives','/naɪvz/','刀、刀具〔复数〕',
 '一把是 a knife，餐桌或抽屉里好几把刀就是 knives。开头 k 不发音，结尾由单数的 /f/ 变成 /vz/。',
 'knife 的名词复数，词尾 -fe 改为 -ves；保留较早英语、北欧语相关刀具名的形式关系。这类变化有历史语音和后来的类推背景，现代要按具体词记。',
 [['较早英语、北欧语相关词 → knife','刀具名称'],['knife 的 -fe → -ves → knives','名词复数；读 /naɪvz/']],
 'kitchen knives 厨房刀具；knives and forks 刀叉；sharp knives 锋利的刀；a set of knives 一套刀具。',
 'put the knives away；two knives。','knives 是名词复数。knife 作动词时的第三人称单数通常写 knifes，不能把所有语法位置都换成 knives。',
 ('The knives and forks are in the top drawer.','刀叉在最上面的抽屉里。'),('This set includes three different kitchen knives.','这套刀具包括三种不同的厨房刀。'),sources=['https://www.merriam-webster.com/dictionary/knife','https://en.wiktionary.org/wiki/knives#English'])
W('leaves','/liːvz/','叶子、书页等〔leaf 的复数〕；离开、留下等〔leave 的第三人称单数〕',
 'The leaves fall 里的 leaves 是一片片叶子；She leaves at six 里的 leaves 是她六点离开。拼写、读音相同，句中作用完全不同。',
 '名词 leaf 的 f 改成 ves；动词 leave 末尾已有 e，只加 s。leaf 接古英语叶词 lēaf，leave 的离开、留下动词接另一旧词 lǣfan，不能因现代字形合并来源。',
 [['leaf → leaves','叶子、书页等的名词复数'],['leave + -s → leaves','单数主语的离开、留下等动作']],
 'fallen leaves 落叶；tea leaves 茶叶；the leaves of a book 书页；She leaves tomorrow 她明天离开。',
 'green leaves；leaves a message。','书的一张 leaf 通常有正反两个 page。普通叶子复数用 leaves；leaf 作翻页等动词，第三人称写 leafs，另有专名等特殊拼写。',
 ('Dry leaves covered the path.','干叶铺满了小路。'),('She leaves a note on the table before she goes out.','她出门前会在桌上留张便条。'),sources=['https://www.merriam-webster.com/dictionary/leaf','https://en.wiktionary.org/wiki/leaves#English','https://en.wiktionary.org/wiki/leave#English'])
W('wives','/waɪvz/','妻子〔复数〕',
 '一位的称呼是 wife，说好几位妻子时是 wives。比如两兄弟各自的妻子，可以说 their wives。',
 'wife 的 -fe 改为 -ves，单数 /f/ 与复数 /v/ 对应。wife 由古英语 wif 延续，较早还可泛指女性，现代主要用于婚姻中的妻子。',
 [['古英语 wif → wife','较早女性、妻子；现代主要妻子'],['wife 的 -fe → -ves → wives','不止一位妻子']],
 'their wives 他们各自的妻子；husbands and wives 夫妻双方；wives’ names 妻子们的名字。',
 'the two wives；their wives and children。','wife’s 是一位妻子的；wives 是复数；wives’ 是多位妻子的。wives 本身不带所有关系，不能和 wife’s 混写。',
 ('The two brothers arrived with their wives.','两兄弟和各自的妻子一起到了。'),('The forms asked for the husbands’ and wives’ names.','表格要求填写丈夫和妻子双方的姓名。'),sources=['https://www.merriam-webster.com/dictionary/wife','https://en.wiktionary.org/wiki/wives#English'])
W('wolves','/wʊlvz/','狼〔复数〕',
 '一只狼是 a wolf，一群狼里的多只就是 wolves。单数结尾 /f/，复数结尾 /vz/，中间的 /ʊ/ 保持不变。',
 'wolf 的名词复数，f 改成 ves；wolf 接古英语 wulf 等日耳曼语词。现代名词复数的变形与动词词尾规则要分开。',
 [['古英语 wulf → wolf','狼的名称'],['wolf 的 f → ves → wolves','多个狼；词尾读 /vz/']],
 'a pack of wolves 一群狼；wild wolves 野狼；wolves in the forest 森林里的狼；keep the wolves at bay 抵挡威胁〔比喻用法等〕。',
 'grey wolves；a story about wolves。','wolf 作狼吞虎咽的动词时，第三人称通常 wolfs：He wolfs down his food。wolves 是这里的名词复数。',
 ('The documentary follows a pack of wolves.','这部纪录片跟拍了一群狼。'),('We heard wolves howling in the distance.','我们听到远处有狼在嚎叫。'),sources=['https://en.wiktionary.org/wiki/wolves#English','https://en.wiktionary.org/wiki/wolf#English'])
W('shelves','/ʃelvz/','架板、搁板〔复数〕；把……上架、搁置〔shelve 的第三人称单数〕',
 '书架上横着的一层层板叫 shelves。动词 shelve 可以把书放上架，也能把计划先搁到一边。',
 '名词 shelf 的 f 改成 ves，形成 shelves；动词 shelve 末尾已有 e，加 s 后也写 shelves。shelf 接较早英语架板词，shelve 则由相应名词转用。',
 [['shelf → shelves','一层搁板 → 多层或多块搁板'],['shelf → shelve → shelves','放上架、搁置 → 单数主语的相应动作']],
 'wooden shelves 木搁板；empty shelves 空货架；put books on the shelves 把书放到架上；shelves a plan 暂时搁置计划。',
 'shelves full of books；on the top shelves。','shelf 常指一块横板、一个层面，整个家具可以是 bookcase 或 shelving unit。shelves 后面直接接宾语时，也要考虑它是不是动词。',
 ('The shelves are full of old maps and books.','架子上摆满了旧地图和书。'),('She shelves the returned books every morning.','她每天早上把归还的书放回架上。'),sources=['https://en.wiktionary.org/wiki/shelves#English','https://en.wiktionary.org/wiki/shelf#English','https://en.wiktionary.org/wiki/shelve#English'])
W('halves','英 /hɑːvz/；美 /hævz/','一半〔复数〕；把……减半、平分〔halve 的第三人称单数〕',
 '把一个苹果平均切成两块，得到 two halves。halve 是把它变成两半或减到一半；动词遇到单数主语也会写 halves。',
 '名词 half 的 f 改成 ves，l 在常见标准读音里不发音。half 承接古英语 healf；相应动词 halve 的第三人称也是 halves。',
 [['half → halves','一半 → 多个一半、两个半份'],['half → halve → halves','减半、分成两半 → 单数主语的动作']],
 'two equal halves 两个相等的半份；cut into halves 切成两半；the first and second halves 上下半场；halves the cost 把费用减半。',
 'both halves；divide into halves。','two halves 指整体的两个半份；two and a half hours 中 a half 仍是单数。halves 作动词可说减半，double 才是加倍。',
 ('Cut the apple into two equal halves.','把苹果切成相等的两半。'),('Sharing the equipment halves the cost for each person.','共用设备让每个人的费用减半。'),sources=['https://en.wiktionary.org/wiki/halves#English','https://en.wiktionary.org/wiki/half#English','https://en.wiktionary.org/wiki/halve#English'])
W('lives','名词 /laɪvz/；动词 /lɪvz/','生命、生活、人生〔life 的复数〕；居住、生活等〔live 的第三人称单数〕',
 'save lives 是挽救生命，She lives here 是她住这里。看见同一个 lives，要先判断它是名词还是谓语动词，再决定读音。',
 'life 的 -fe 改为 -ves，名词读 /laɪvz/；动词 live + s，读 /lɪvz/。两者接古英语同族的生命名词、生活动词，但现代不是互相随意换读音。',
 [['life → lives /laɪvz/','生命、人生、生活的复数'],['live + -s → lives /lɪvz/','单数主语的生活、居住动作']],
 'save lives 救命；change our lives 改变我们的生活；private lives 私人生活；She lives alone 她独居；lives in a village 住在村里。',
 'ordinary lives；lives near the station。','形容词 live 也读 /laɪv/，如 live music，但 She lives ... 是动词 /lɪvz/。不能只凭看到 live 的字母就定一种发音。',
 ('The new crossing could save lives.','新设的人行横道可能挽救生命。'),('She lives in a quiet village near the coast.','她住在海边附近的一个安静村庄。'),sources=['https://en.wiktionary.org/wiki/lives#English','https://en.wiktionary.org/wiki/life#English','https://en.wiktionary.org/wiki/live#English'])
W('thieves','/θiːvz/','小偷、窃贼〔复数〕',
 '一个偷东西的人是 a thief；不止一个就是 thieves。长元音 /iː/ 保留，词尾由 /f/ 变成 /vz/。',
 'thief 的 f 改成 ves。thief 承接古英语 theof 等日耳曼语窃贼词；theft 是盗窃行为的另一个相关名词，不是 thief 的复数。',
 [['古英语 theof → thief','偷窃的人'],['thief 的 f → ves → thieves','多个窃贼；发 /θiːvz/']],
 'car thieves 偷车贼；a gang of thieves 一伙窃贼；thieves stole ... 窃贼偷走……；thieves and robbers 小偷和强盗。',
 'catch the thieves；a story about thieves。','thief 着重偷窃者；robber 常与抢劫有关。thieves 是人，thefts 是多起盗窃事件，不要只因中文都有偷就混用。',
 ('The thieves escaped before anyone noticed the missing box.','还没人发现箱子不见，窃贼就逃走了。'),('The story is about two thieves who try to change their lives.','故事讲的是两个试图改变人生的窃贼。'),sources=['https://en.wiktionary.org/wiki/thieves#English','https://en.wiktionary.org/wiki/thief#English'])
W('roofs','常 /ruːfs/；亦有 /ruːvz/ 等读法','屋顶、顶篷等〔复数〕；给……盖屋顶〔roof 的第三人称单数〕',
 '从山上看下去，一栋栋房子的顶连成一片，就是 roofs。它很适合与 knives、wives 对照：不是所有 f 结尾词的复数都改写 ves。',
 'roof + -s，标准复数拼写 roofs；常读 /ruːfs/，词典也记录 /ruːvz/ 及元音变体。roof 从古英语 hrof 延续，名词和动词都可加 s。',
 [['古英语 hrof → roof','建筑物的覆盖顶部'],['roof + -s → roofs','多个顶部；也可作盖屋顶动词形式']],
 'red roofs 红屋顶；the roofs of houses 房子的屋顶；sloping roofs 斜屋顶；snow on the roofs 屋顶上的雪。',
 'the roofs of cars；repair the roofs。','标准拼写 roofs 保留 f，即便某些说话者发 /v/，也不要据发音一概改写成 rooves。ceiling 通常是室内头顶的内表面，与屋顶的侧重点不同。',
 ('Snow covered the roofs of the village houses.','雪覆盖了村中房屋的屋顶。'),('From the hill, we could see rows of red roofs.','从山上，我们能看见一排排红屋顶。'),sources=['https://www.merriam-webster.com/dictionary/roof','https://en.wiktionary.org/wiki/roofs#English'])
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_vs',ROOTS,WORDS)
 extend_lessons()
