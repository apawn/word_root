"""Common animal plurals and familiar verb meanings."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'B2412':dict(words=['cat','cats'],label='cat → cats：猫的普通复数',note='cats 词尾读 /ts/；动物名称与计算机 cat 命令的缩短来源分开。'),
 'B4609':dict(words=['dog','dogs'],label='dog → dogs：狗；困扰、紧跟',note='dogs 的 /ɡ/ 发音保留，词尾 /z/；动词 dog 用紧跟的画面表达持续困扰。'),
 'B2627':dict(words=['bird','birds'],label='bird → birds：鸟的普通复数',note='birds 词尾 /dz/；旧 bird、brid 等形式有元音和 r 位置变体，不能机械反推所有英语词都有这种换位规则。'),
 'B2684':dict(words=['duck','ducks'],label='duck → ducks：鸭；低头躲开',note='鸭名通常联系潜下的旧动作词，现代 duck 动词也说低头避开；布料 duck 来自荷兰 doek，另源。'),
 'B2718':dict(words=['egg','eggs'],label='egg → eggs：蛋；eggs on 的怂恿另源',note='现代蛋名 egg 接北欧形式，egg on 怂恿接古北欧 eggja 刺激，两支分开看。'),
 'B4597':dict(words=['horse','horses'],label='horse → horses：马；horse around 的胡闹',note='horses 在 /s/ 后增加 /ɪz/；horse 是古英语 hors 的延续，现代动词搭配另按语境理解。'),
}
W('cats','/kæts/','猫；cat 的复数',
 '一只 cat，多只 cats。cat 常泛指家猫；讨论动物分类时，也可以把狮、虎等放进更广的猫科范围里。',
 'cat + -s，/t/ 后读 /s/，结尾 /ts/。接古英语 catt、catte 等猫名，与晚期拉丁 cattus 等欧洲猫名有关，更远来源未定。',
 [['古英语 catt／catte 等 → cat','猫；欧洲相关猫名的远源仍有讨论'],['cat + -s → cats','多只猫；语境可扩展到猫科动物']],
 'pet cats 宠物猫；wild cats 野猫、野生猫科动物；big cats 狮虎等大型猫科动物；cats and dogs 猫和狗。',
 'two cats；cats sleeping in the sun。','cats 是复数，cat’s 可是单数所有格，cats’ 是复数所有格。计算机命令 cat 则是 concatenate 的缩短，不能拿动物词源来解释它。',
 ('The cats were sleeping in a patch of sunlight.','猫们在一块阳光下睡觉。'),('The sanctuary cares for several species of big cats.','这处保护机构照料几种大型猫科动物。'),sources=['https://en.wiktionary.org/wiki/cats#English','https://en.wiktionary.org/wiki/cat#English'])
W('dogs','英 /dɒɡz/；美 /dɔːɡz, dɑːɡz/','狗；持续困扰、紧跟〔dog 的第三人称单数〕',
 '动物是 dogs；麻烦像甩不掉的东西一直跟着人，也能用 dog 作动词，写成 dogs。',
 'dog + -s，/ɡ/ 后读 /z/。dog 接古英语 docga 等形式，更远来源未定；后来成为狗的通称，逐渐取代 hound 的较宽旧用法。',
 [['古英语 docga → dog','犬类名称 → 狗的常用通称；又有紧跟等动词引申'],['dog 名词、动词 + -s → dogs','多只狗；单数主语持续困扰、紧跟']],
 'guide dogs 导盲犬；working dogs 工作犬；dogs on leads 牵着绳的狗〔英式〕；a problem dogs someone 某个问题持续困扰某人。',
 'dogs in the park；dogs her every step。','The dogs follow him 是狗跟着他；The problem dogs him 是问题一直缠着他。后一句 dogs 是动词，不是复数狗。',
 ('Please keep dogs on a lead near the sheep.','靠近羊群时，请用牵引绳牵住狗。'),('The same technical problem dogs every attempt to finish the project.','同一个技术问题一直妨碍项目收尾的每次尝试。'),sources=['https://en.wiktionary.org/wiki/dogs#English','https://en.wiktionary.org/wiki/dog#English'])
W('birds','英 /bɜːdz/；美 /bɜːrdz/','鸟；bird 的复数',
 '多只鸟就是 birds。观察它们的叫声、羽毛、迁徙行为时，前面的修饰语会帮你把是哪类鸟说具体。',
 'bird + -s，/d/ 后读 /z/。古英语有 bridd、bird 等材料，中古英语也有 brid、bird 变体，现代通称延续为 bird；更远来源未定。',
 [['古英语 bridd／bird 等 → 中古英语变体 → bird','较早的鸟类名称 → 鸟的通称'],['bird + -s → birds','多只鸟']],
 'wild birds 野鸟；migratory birds 候鸟；birds of prey 猛禽；feed the birds 喂鸟。鸟的通称与更具体类别可以一起学。',
 'a flock of birds；birds singing outside。','a flock of birds 是一群鸟，birds 本身只表复数，不一定聚成同一群。两只不同地点的鸟，也可合说 two birds。',
 ('We heard birds singing before sunrise.','日出前，我们听见鸟在鸣叫。'),('The lake attracts many migratory birds in winter.','冬季，这片湖吸引很多候鸟。'),sources=['https://en.wiktionary.org/wiki/birds#English','https://en.wiktionary.org/wiki/bird#English'])
W('ducks','/dʌks/','鸭〔复数〕；低头躲避、避开〔duck 的第三人称单数〕',
 '鸭子会把头和身子往水下压；人迅速低头避开障碍，也叫 duck。ducks 在句中可能是几只鸭，也可能是某人躲了一下的现在动作。',
 'duck + -s，/k/ 后读 /s/。鸟名接古英语 duce，通常联系潜下的旧动作词；现代低头动词经中古英语 ducken 等形式延续。帆布义 duck 则另借荷兰 doek 布。',
 [['古英语 duce 及潜下动词的历史关系 → 鸭名 duck；中古英语 ducken → 动词 duck','鸭；潜下、低头避开，具体路线分别看'],['duck 名词、动词 + -s → ducks','多只鸭；单数主语低头避开、回避']],
 'ducks on the pond 池塘里的鸭；ducks under the branch 低头从树枝下过去；ducks the question 回避问题；get your ducks in a row 把事情安排妥当。',
 'feed the ducks；ducks out of the way。','The ducks swim 中是复数名词；She ducks under the doorframe 中是单数主语后的动词。dodge 也能说躲避，但不一定有低头的动作。',
 ('The ducks gathered near the edge of the pond.','鸭子聚到了池塘边。'),('He ducks under the low beam every time he enters.','他每次进门都要低头避开那根低矮的梁。'),sources=['https://en.wiktionary.org/wiki/ducks#English','https://en.wiktionary.org/wiki/duck#English'])
W('eggs','/eɡz/','蛋、卵〔复数〕；eggs someone on 表怂恿某人〔另源动词〕',
 '早餐里的鸡蛋、鸟巢里的蛋，都可以叫 eggs。eggs someone on 则是催人、激人继续做某事，要把它作为另一条动词路线记。',
 'egg + -s，/ɡ/ 后读 /z/。现代蛋名经中古英语接古北欧 egg；怂恿动词接古北欧 eggja 刺激、催促等，通常联系刃、尖的词族，与蛋名不同源。',
 [['古北欧 egg → 中古英语 egg → 蛋名 egg；另路 eggja → 怂恿动词 egg','蛋、卵；催促、刺激，两支分开'],['egg 名词、动词 + -s → eggs','多个蛋；单数主语在 egg on 中怂恿']],
 'boiled eggs 煮蛋；fried eggs 煎蛋；lay eggs 下蛋；eggs someone on 怂恿某人；put all your eggs in one basket 把所有希望押在一处。',
 'a box of eggs；the eggs in the nest。','eggs 读 /eɡz/，/ɡ/ 和复数词尾 /z/ 都保留。egg someone on 要连 on 一起记，常含怂恿对方去做冲动、冒险事情的语气。',
 ('The bird laid three eggs in the nest.','这只鸟在巢里下了三个蛋。'),('The others cheer, and one friend eggs him on to try again.','其他人欢呼，一位朋友又怂恿他再试一次。'),sources=['https://en.wiktionary.org/wiki/eggs#English','https://en.wiktionary.org/wiki/egg#English'])
W('horses','英 /ˈhɔːsɪz/；美 /ˈhɔːrsɪz/','马〔复数〕；horse 的第三人称单数形式〔如 horses around 胡闹〕',
 '多匹马是 horses；horse around 是粗野、打闹式地玩，常出现在提醒别人别闹的场景里。',
 'horse 已有 e，加 s；原词 /s/ 后增加 /ɪz/ 一个音节。horse 继承古英语 hors，更远来源有不同解释，不强定一个未证实的跑步词根。',
 [['古英语 hors → horse','马；后来有与力量、体型等相关的引申'],['horse 名词、动词 + -s → horses','多匹马；在特定动词搭配中说胡闹等']],
 'ride horses 骑马；wild horses 野马；horses in a stable 马厩里的马；hold your horses 口语说先等等、别着急；horses around 到处打闹。',
 'a pair of horses；horses grazing in a field。','horses 的复数多一个 /ɪz/ 音节，因为单数以 /s/ 收尾；cats、ducks 没有这个音节。hold your horses 常是劝人等一等，不一定真的有人牵马。',
 ('The horses were grazing quietly in the field.','马在田野里安静地吃草。'),('The guide asked us to wait while she checked the horses.','向导让我们等一等，她先检查马匹。'),sources=['https://en.wiktionary.org/wiki/horses#English','https://en.wiktionary.org/wiki/horse#English'])
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_wk',ROOTS,WORDS)
 extend_lessons()
