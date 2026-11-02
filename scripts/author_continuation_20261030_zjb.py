"""Familiar animal names: borrowing routes, historical naming and ordinary plurals."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
KANGAROO='https://history.cass.anu.edu.au/centres/andc/borrowings-australian-aboriginal-languages'
KOALA='https://bayala.sl.nsw.gov.au/word/koala-2'
MUSEUM='https://australian.museum/learn/animals/mammals/koala/'
def S(word,base):
 a=['https://en.wiktionary.org/wiki/'+word+'#English','https://www.etymonline.com/word/'+base]
 if base=='kangaroo':a.append(KANGAROO)
 if base=='koala':a+=[KOALA,MUSEUM]
 return a
EXISTING_ROOT_ADDITIONS={
 'C0055':dict(words='panda pandas koala koalas kangaroo kangaroos giraffe giraffes cheetah cheetahs jaguar jaguars'.split(),label='常见动物名称的不同借词路线',note='本支与 animal 对照动物名称，各词不由拉丁 anim- 派生。panda 经法语接喜马拉雅地区名称；koala、kangaroo 接不同澳洲原住民语言；giraffe 经欧洲语言接阿拉伯语；cheetah 经印地语接有斑点的梵语材料；jaguar 经葡萄牙语接图皮语。名称不强行归成一条词源。'),
 'B2627':dict(words='penguin penguins'.split(),label='penguin → penguins：从大海雀到企鹅的鸟名转用',note='与 bird 比较鸟类，不由 bird 派生。penguin 原先用于北大西洋大海雀，后来转给外形相似的南方企鹅；威尔士语头加白的分析等尚非定论。'),
 'B4597':dict(words='zebra zebras'.split(),label='zebra → zebras：与马比较的斑马名',note='与 horse 比较外形、动物类别，不认定直接同源。zebra 经欧洲语言传入，意大利语、葡萄牙语形式相关；更远有拉丁野马等不同分析，来源仍不确定。'),
 'C0665':dict(words='leopard leopards'.split(),label='leopard：狮与豹的古老复合名称',note='leopard 经法语、拉丁语接希腊 leon 狮 + pardos 豹的复合名称；背后有古人误认杂交关系的想象，不是现代生物学认定。'),
 'C0556':dict(words='hippo hippos'.split(),label='hippopotamus → hippo → hippos：河马的短称',note='长词来自希腊马与河流材料，河马是命名画面；现代 hippo 是完整长词的缩略，复数 hippos 直接加 s，不因希腊 hippos 本来表示马而译错。'),
 'C1224':dict(words='rhino rhinos'.split(),label='rhinoceros → rhino → rhinos：鼻角动物的短称',note='rhinoceros 经拉丁语接希腊鼻与角的复合名称；现代 rhino 缩略整个动物名，rhinos 是英语复数，不等于古希腊单词的格变化。'),
}
PANDA=[['法语 panda → 英语 panda，早期指小熊猫','更远通常联系尼泊尔等喜马拉雅地区名称，具体形式解释不完全确定'],['名称后来也用于大熊猫 → panda、pandas 的现代常见用法','red panda 与 giant panda 用修饰词分清，不由名称相同推断同一物种']]
KOALA_H=[['澳洲 Dharug 语言的 gula 等动物名形式 → 英语 koala','历史词表记录当地动物称呼，不根据英语字母硬拆'],['koala 树袋熊 → koalas','有袋类动物，常见 koala bear 称呼不改变它不是熊类的事实']]
KANGAROO_H=[['Guugu Yimidhirr 语言 gangurru 等形式','原用于当地一种大型袋鼠的名称'],['借入英语 kangaroo → kangaroos','英语逐渐用于较宽范围的袋鼠；听不懂的词源传说不成立']]
PENGUIN=[['英语 penguin 先用于大海雀','更远来源不定，威尔士语头、白等分析仍是提议'],['鸟名转用于外形相似的南方企鹅 → penguins','名称转用不是说大海雀演化成了现代企鹅']]
GIRAFFE=[['阿拉伯语 zarāfa 等 → 意大利语 giraffa、法语 girafe 等','阿拉伯语更远可能借自非洲语言'],['英语曾有多种借入拼写，现代 giraffe 与法语形式有关','giraffe → giraffes；多路传播，不把所有中间形式当唯一单线']]
ZEBRA=[['意大利语 zebra、葡萄牙语等相关动物名称 → 英语 zebra','更远来源不定，曾有野驴、拉丁野马等不同分析'],['英语 zebra 斑马 → zebras','现代条纹的画面帮助记动物，不是按英语零碎字母造出的词']]
CHEETAH=[['印地语 cītā 等 → 英语 cheetah','更远接梵语 citraka 等，有斑点、杂色的命名背景'],['cheetah 猎豹 → cheetahs','斑点是词源线索；现代可另外用细长体形、奔跑姿态辨认']]
LEOPARD=[['希腊 leon 狮 + pardos 豹 → leopardos → 拉丁 leopardus','古人对动物关系的旧想象，不是实际杂交结论'],['古法语 leupart、lebard 等 → 英语 leopard → leopards','现代整词通常读 /ˈlepəd/、/ˈlɛpɚd/，不按 leon 分音朗读']]
JAGUAR=[['图皮语 jaguara 等 → 葡萄牙语 jaguar → 英语 jaguar','旧来源中的本地动物词范围可能比现代单一物种更宽'],['英语主要用作美洲豹名 → jaguars','名称整体借入，现代英语再按普通名词加复数']]
W('panda','英 /ˈpændə/；美 /ˈpændə/','熊猫；〔giant panda〕大熊猫；〔red panda〕小熊猫',
 '黑白毛色、常抱着竹子的大熊猫，今天单说 panda 很容易让人想到它。词的历史却先接小熊猫名称。',
 '英语经法语借 panda，早期用于小熊猫，后来也用于大熊猫；更远通常联系尼泊尔等地区的动物名称，具体拆分不确定。',PANDA,
 'a giant panda 是大熊猫；a red panda 是小熊猫；a baby panda 是熊猫幼崽。',
 'a giant panda；a red panda；a baby panda。',
 'giant panda 和 red panda 是不同动物名称；现代不要因为都叫 panda，就把红毛、长尾的小熊猫当大熊猫幼崽。',
 ('A panda was eating bamboo beside the tree.','一只熊猫在树旁吃竹子。'),('The red panda curled up on a branch.','小熊猫蜷在一根树枝上。'),sources=S('panda','panda'))
W('pandas','英、美 /ˈpændəz/','熊猫〔复数〕',
 '几只熊猫，可以说 pandas；加 giant 或 red，便把大熊猫、小熊猫区分得更清楚。',
 'panda + -s → pandas，末尾 /ə/ 后接 /z/；完整借入的动物名照英语规则形成复数。',PANDA+[['panda + -s → pandas','多只熊猫，词尾 /əz/']],
 'giant pandas 是大熊猫；red pandas 是小熊猫；two pandas 是两只熊猫。',
 'giant pandas；red pandas；two pandas。',
 'pandas 不说明年龄；baby pandas 才明确说幼崽，red pandas 则是小熊猫这个动物名。',
 ('The children watched two pandas playing.','孩子们看着两只熊猫玩耍。'),('The sign describes the habits of red pandas.','说明牌介绍了小熊猫的习性。'),sources=S('pandas','panda'))
W('koala','英 /kəʊˈɑːlə/；美 /koʊˈɑlə/','树袋熊、考拉',
 '灰毛、圆耳朵，常抱着树干休息的树袋熊，就是 koala。英语名字借自澳洲当地动物称呼。',
 '接 Dharug 语言的 gula 等记录形式，经借入和拼写变化成为 koala；作为一个完整借词来记即可。',KOALA_H,
 'a koala in a tree 是树上的树袋熊；a baby koala 是树袋熊幼崽；koala habitat 是树袋熊栖息地。',
 'a baby koala；a koala in a tree；koala habitat。',
 'koala bear 是常见俗称，但 koala 是有袋类动物，不属于熊类；称呼相似不等于生物分类相同。',
 ('A koala rested in the fork of a tree.','一只树袋熊在树杈间休息。'),('The child pointed to a koala in the picture.','孩子指着画里的树袋熊。'),sources=S('koala','koala'))
W('koalas','英 /kəʊˈɑːləz/；美 /koʊˈɑləz/','树袋熊、考拉〔复数〕',
 '树上几只抱着枝干的树袋熊，就是 koalas。复数仍保留原来中间的重音。',
 'koala + -s → koalas，末尾 /ə/ 后接 /z/；不需要改变这个借词的基础拼写。',KOALA_H+[['koala + -s → koalas','规则复数，读音重心仍在 /ɑː/、/ɑ/']],
 'koalas in the trees 是树上的树袋熊；young koalas 是幼年树袋熊；pictures of koalas 是树袋熊图片。',
 'koalas in the trees；young koalas；pictures of koalas。',
 'koalas 是复数名词；koala habitat 的 koala 作前部修饰，通常保持单数。',
 ('We spotted two koalas high in the trees.','我们发现高高的树上有两只树袋熊。'),('The book has photographs of koalas and kangaroos.','书里有树袋熊和袋鼠的照片。'),sources=S('koalas','koala'))
W('kangaroo','英 /ˌkæŋɡəˈruː/；美 /ˌkæŋɡəˈru/','袋鼠',
 '长后腿、一跳一跳往前走的大袋鼠，是 kangaroo。名字来自澳洲一种当地语言里的动物名。',
 'Guugu Yimidhirr 语言 gangurru 等形式借入英语，原指当地一种大型袋鼠，英语后来把名称用于更宽范围。不是当地人回答“我听不懂”而产生的词。',KANGAROO_H,
 'a kangaroo hopping 是正在跳的袋鼠；a young kangaroo 是幼年袋鼠；a kangaroo’s tail 是袋鼠尾巴。',
 'a young kangaroo；a kangaroo hopping；a kangaroo’s tail。',
 '袋鼠名的来路有原语言记录支持；听不懂的故事便于传播，却不能代替这种语言证据。',
 ('A kangaroo hopped across the track.','一只袋鼠跳过了小路。'),('The kangaroo balanced itself with its long tail.','袋鼠用长尾巴保持平衡。'),sources=S('kangaroo','kangaroo'))
W('kangaroos','英 /ˌkæŋɡəˈruːz/；美 /ˌkæŋɡəˈruz/','袋鼠〔复数〕',
 '草地上几只大袋鼠，是 kangaroos。词尾虽然写 oo，复数直接加 s，不另加 es。',
 'kangaroo + -s → kangaroos，元音 /uː/、/u/ 后读 /z/；英语规则复数加在借词整体后。',KANGAROO_H+[['kangaroo + -s → kangaroos','多只袋鼠，词尾 /ruːz/、/ruz/']],
 'a group of kangaroos 是一群袋鼠；kangaroos grazing 是袋鼠在吃草；wild kangaroos 是野生袋鼠。',
 'wild kangaroos；a group of kangaroos；kangaroos grazing。',
 'kangaroos 说多只动物；a kangaroo enclosure 的前部 kangaroo 作修饰，通常仍用单数形式。',
 ('A group of kangaroos grazed near the trees.','一群袋鼠在树边吃草。'),('We saw kangaroos from the train window.','我们从火车窗里看到了袋鼠。'),sources=S('kangaroos','kangaroo'))
W('penguin','英、美 /ˈpeŋɡwɪn/','企鹅',
 '站着像穿了深色外套、游泳很灵活的企鹅，是 penguin。词名先用于另一种外形相似的海鸟，后来才转到企鹅身上。',
 '早期英语 penguin 指大海雀，后来转用于南方企鹅；更远来源不确定。威尔士语 pen 头 + gwyn 白是常见提议，不应写成已证实的拆分。',PENGUIN,
 'an emperor penguin 是帝企鹅；a penguin chick 是企鹅雏鸟；a penguin swimming 是游泳的企鹅。',
 'an emperor penguin；a penguin chick；a penguin colony。',
 '名称从大海雀转用，不是在说大海雀这个物种变成了企鹅；词的演变与生物的演化要分开。',
 ('A penguin waddled towards the water.','一只企鹅摇摇摆摆地朝水边走去。'),('The penguin dived beneath the surface.','企鹅潜到了水面下。'),sources=S('penguin','penguin'))
W('penguins','英、美 /ˈpeŋɡwɪnz/','企鹅〔复数〕',
 '一群企鹅站在岸边，是 penguins。把名字作为整体借用，再按普通英语加复数即可。',
 'penguin + -s → penguins，/n/ 后读 /z/；基础词的鸟名转用史保留，不必把提议中的威尔士语词块重新逐个变化。',PENGUIN+[['penguin + -s → penguins','多只企鹅，词尾 /nz/']],
 'a colony of penguins 是一群聚居企鹅；penguins swimming 是游泳的企鹅；young penguins 是幼年企鹅。',
 'a colony of penguins；penguins swimming；young penguins。',
 'penguins 是鸟类名称，即使擅长游泳也不是 fish 鱼；学习时把岸上姿态和水中动作放在同一幅画面里。',
 ('The penguins stood together on the shore.','企鹅们聚在岸边。'),('We watched the penguins swim through the water.','我们看着企鹅在水中游动。'),sources=S('penguins','penguin'))
W('giraffe','英 /dʒɪˈrɑːf/；美 /dʒəˈræf/','长颈鹿',
 '伸着长脖子从高处取叶子的长颈鹿，是 giraffe。这个名字经历了几种语言的接力。',
 '阿拉伯语 zarāfa 等进入意大利语 giraffa、法语 girafe 等；英语历史上多路借入、拼写不一，现代 giraffe 与法语形式相关，更远可能来自非洲语言。',GIRAFFE,
 'a tall giraffe 是高大的长颈鹿；a baby giraffe 是幼年长颈鹿；a giraffe’s neck 是长颈鹿的脖子。',
 'a tall giraffe；a baby giraffe；a giraffe’s neck。',
 'giraffe 末尾 ff 读 /f/、e 不发音；读音重心在后一个音节，别把末尾另读成 /fi/。',
 ('A giraffe reached for leaves high in the tree.','一只长颈鹿伸向树上高处的叶子。'),('The baby giraffe stood close to its mother.','小长颈鹿紧挨着妈妈站着。'),sources=S('giraffe','giraffe'))
W('giraffes','英 /dʒɪˈrɑːfs/；美 /dʒəˈræfs/','长颈鹿〔复数〕',
 '几只长颈鹿站在一起，是 giraffes。词尾虽然写着 f，复数并不改成 v。',
 'giraffe + -s → giraffes，基础词末尾已有 e，直接加 s；/f/ 后读 /s/，结尾 /fs/。',GIRAFFE+[['giraffe + -s → giraffes','规则复数；保留 f 音，词尾 /fs/']],
 'a group of giraffes 是一群长颈鹿；young giraffes 是幼年长颈鹿；giraffes feeding 是长颈鹿正在进食。',
 'a group of giraffes；young giraffes；giraffes feeding。',
 '有些 f、fe 词复数变 -ves，但 giraffes 不套那条变化；这里直接加 s。',
 ('Three giraffes walked slowly across the grass.','三只长颈鹿缓缓走过草地。'),('The children drew giraffes with very long necks.','孩子们画了脖子很长的长颈鹿。'),sources=S('giraffes','giraffe'))
W('zebra','英 /ˈzebrə/；美 /ˈziːbrə/','斑马',
 '马样的身体上布着黑白条纹，是 zebra。先用条纹认动物，再把名字当一个传入英语的整体来记。',
 '经意大利语、葡萄牙语等相关名称传入英语，更远来源不定；拉丁 equiferus 野马等只是其中分析，不能当作已证明的唯一祖先。',ZEBRA,
 'a zebra’s stripes 是斑马的条纹；a zebra foal 是斑马幼崽；英式 zebra crossing 借条纹说斑马线。',
 'a zebra’s stripes；a zebra foal；a zebra crossing。',
 '英式常读 /ˈzebrə/，美式常读 /ˈziːbrə/，首元音可不同；两个都指同一种常见动物名称。',
 ('A zebra stood beside the waterhole.','一只斑马站在水坑旁。'),('We crossed the road at the zebra crossing.','我们从斑马线过了马路。'),sources=S('zebra','zebra'))
W('zebras','英 /ˈzebrəz/；美 /ˈziːbrəz/','斑马〔复数〕',
 '一群黑白条纹的斑马，可以说 zebras。动物名复数直接加 s。',
 'zebra + -s → zebras，末尾 /ə/ 后接 /z/；首元音仍随常见英美读法有所不同。',ZEBRA+[['zebra + -s → zebras','多只斑马，词尾 /brəz/']],
 'a herd of zebras 是一群斑马；zebras grazing 是斑马吃草；zebras and horses 是斑马与马。',
 'a herd of zebras；zebras grazing；young zebras。',
 'zebra crossing 前部通常用单数 zebra 修饰；zebras 是在直接数多只动物，两个语法位置不同。',
 ('A herd of zebras crossed the plain.','一群斑马穿过平原。'),('We watched zebras grazing beside the road.','我们看着斑马在路旁吃草。'),sources=S('zebras','zebra'))
W('cheetah','英 /ˈtʃiːtə/；美 /ˈtʃitə/','猎豹',
 '身体细长、脸上常见深色泪痕、善于奔跑的猎豹，是 cheetah。名字更远的线索则是身上的斑点、杂色。',
 '印地语 cītā 等动物名借入英语，向前接梵语 citraka 等有斑点、杂色的材料；现代英语把 cheetah 当一个完整动物名使用。',CHEETAH,
 'a cheetah running 是奔跑的猎豹；a cheetah cub 是猎豹幼崽；a cheetah’s spots 是猎豹的斑点。',
 'a cheetah cub；a cheetah running；a cheetah’s spots。',
 'cheetah 是猎豹，leopard 是豹；两者都有斑纹，不能只凭中文名字都带豹就当同一个英文词。',
 ('A cheetah rested in the shade.','一只猎豹在阴凉处休息。'),('The photograph shows a cheetah running across the grass.','照片中是一只跑过草地的猎豹。'),sources=S('cheetah','cheetah'))
W('cheetahs','英 /ˈtʃiːtəz/；美 /ˈtʃitəz/','猎豹〔复数〕',
 '几只细长体形、满身斑点的猎豹，是 cheetahs。复数的 s 接在听起来为 /ə/ 的结尾之后。',
 'cheetah + -s → cheetahs，词尾字母 h 不单独发音，后缀读 /z/；不能按字母 h 猜成 /s/。',CHEETAH+[['cheetah + -s → cheetahs','多只猎豹，末尾 /təz/']],
 'young cheetahs 是幼年猎豹；cheetahs running 是猎豹在奔跑；photographs of cheetahs 是猎豹照片。',
 'young cheetahs；cheetahs running；photographs of cheetahs。',
 '判断复数读音看基础词的末音；cheetahs 的末尾来自 /ə/ 加 /z/，拼写没有额外音节。',
 ('Two cheetahs lay beneath a tree.','两只猎豹躺在树下。'),('The documentary follows a family of cheetahs.','纪录片跟拍了一个猎豹家庭。'),sources=S('cheetahs','cheetah'))
W('leopard','英 /ˈlepəd/；美 /ˈlɛpɚd/','豹、花豹',
 '一只身上有玫瑰状斑纹的大猫，是 leopard。名字里虽然有“狮”的旧材料，现代说的就是豹。',
 '希腊 leon 狮 + pardos 豹的复合词，经拉丁 leopardus、古法语 leupart 等传入英语；古人曾想象它与两种动物的杂交有关，这是命名史，不是现代生物学结论。',LEOPARD,
 'a leopard’s spots 是豹的斑点；a leopard cub 是豹崽；a snow leopard 是雪豹这个完整动物名。',
 'a leopard’s spots；a leopard cub；a snow leopard。',
 'leopard 的 eo 在现代读音里并不分成两个清楚的元音音节；常见读法近 /ˈlepəd/、/ˈlɛpɚd/，不照词源零件拼读。',
 ('A leopard rested on a thick branch.','一只豹伏在粗树枝上休息。'),('The leopard disappeared into the long grass.','豹消失在高草丛里。'),sources=S('leopard','leopard'))
W('leopards','英 /ˈlepədz/；美 /ˈlɛpɚdz/','豹〔复数〕',
 '几只豹，是 leopards。它的拼写保留古老名称，现代发音却已经压缩成常见的两音节。',
 'leopard + -s → leopards，/d/ 后读 /z/，词尾 /dz/；不要像 -ed 那样另添 /ɪd/。',LEOPARD+[['leopard + -s → leopards','多只豹，末尾 /dz/']],
 'young leopards 是幼豹；snow leopards 是雪豹；photographs of leopards 是豹的照片。',
 'young leopards；snow leopards；photographs of leopards。',
 'leopards 和 cheetahs 是不同常见动物名；snow leopards 又是由整个 snow leopard 名称形成的复数。',
 ('The book compares leopards with cheetahs.','这本书比较豹与猎豹。'),('The photographer waited for the leopards to appear.','摄影师等着豹出现。'),sources=S('leopards','leopard'))
W('jaguar','英 /ˈdʒæɡjʊə/；美 /ˈdʒæɡwɑr/','美洲豹、美洲虎',
 '美洲森林里体格结实、身上有斑纹的大型猫科动物，是 jaguar。中文既常叫美洲豹，也叫美洲虎。',
 '经葡萄牙语 jaguar 接图皮语 jaguara 等；旧记录里的原语言词可能泛说较大的捕食兽，英语后来主要指美洲豹。',JAGUAR,
 'a jaguar in the forest 是森林里的美洲豹；a jaguar cub 是美洲豹幼崽；a jaguar’s coat 是美洲豹的皮毛。',
 'a jaguar cub；a jaguar in the forest；a jaguar’s coat。',
 'jaguar 与 leopard 是不同动物名；大写 Jaguar 还可见于借动物名命名的汽车品牌，要按上下文判断。',
 ('A jaguar moved quietly through the forest.','一只美洲豹悄悄穿过森林。'),('The photograph shows a jaguar beside a river.','照片里是一只河边的美洲豹。'),sources=S('jaguar','jaguar'))
W('jaguars','英 /ˈdʒæɡjʊəz/；美 /ˈdʒæɡwɑrz/','美洲豹、美洲虎〔复数〕',
 '几只美洲豹，是 jaguars。名字经南美语言、葡萄牙语传来，现代在英语里照常数复数。',
 'jaguar + -s → jaguars，后缀读 /z/；英式常见 /jʊə/ 与美式常见 /wɑr/ 的差别随基础词保留。',JAGUAR+[['jaguar + -s → jaguars','多只美洲豹，英美部分音节读法可不同']],
 'jaguars in the forest 是森林里的美洲豹；photographs of jaguars 是美洲豹照片；young jaguars 是幼年美洲豹。',
 'young jaguars；photographs of jaguars；jaguars in the forest。',
 '谈动物时 jaguars 是普通复数名词；大写 Jaguars 在特定上下文也可能是队名，不能只靠 s 判断是在数动物。',
 ('The film follows two jaguars in the forest.','影片跟拍森林里的两只美洲豹。'),('The book compares jaguars and leopards.','这本书比较美洲豹与豹。'),sources=S('jaguars','jaguar'))
W('hippos','英 /ˈhɪpəʊz/；美 /ˈhɪpoʊz/','河马〔hippo 的复数短称〕',
 '几只圆胖的大河马在水里露出头，口语可以说 hippos。短词听起来轻松，背后还有“河里的马”这个古老名称。',
 'hippopotamus 经拉丁语接希腊 hipp- 马 + potam- 河的材料；现代英语缩成 hippo，再加 -s → hippos，元音后读 /z/。',
 [['希腊马、河流材料 → hippopotamos → 拉丁、英语 hippopotamus','河马是命名画面，不是现代马的一个水中品种'],['hippopotamus → hippo → hippos','短称的现代复数直接加 s']],
 'hippos in the river 是河里的河马；a group of hippos 是一群河马；young hippos 是幼年河马。',
 'hippos in the river；a group of hippos；young hippos。',
 '希腊 hippos 表示马，现代英语 hippos 在这里却是 hippo 河马的复数；先认清是哪种语言、哪一步变化。',
 ('Several hippos rested in the shallow water.','几只河马在浅水里休息。'),('The children watched the hippos from the viewing platform.','孩子们在观景台上看河马。'),sources=S('hippos','hippo'))
W('rhinos','英 /ˈraɪnəʊz/；美 /ˈraɪnoʊz/','犀牛〔rhino 的复数短称〕',
 '厚皮、鼻部有角的犀牛，口语常缩成 rhino；几只就是 rhinos。“鼻＋角”的命名画面留在它的长词里。',
 '希腊 rhin- 鼻 + 角的材料 → rhinokerōs，经拉丁语进入英语 rhinoceros；现代缩成 rhino，再加 -s → rhinos，词尾 /z/。',
 [['希腊鼻、角词族 → 拉丁、英语 rhinoceros','鼻部有角的动物名称'],['rhinoceros → rhino → rhinos','英语短称及其复数；不把相同拼写当古希腊格变化']],
 'two rhinos 是两只犀牛；rhinos in the distance 是远处的犀牛；photographs of rhinos 是犀牛照片。',
 'two rhinos；young rhinos；photographs of rhinos。',
 'rhino 是完整长词 rhinoceros 的短称；现代 rhinos 数犀牛，不是看到 rhin- 鼻就把整个短词译成鼻子。',
 ('The guide pointed out two rhinos in the distance.','向导指给我们看远处的两只犀牛。'),('The book has photographs of rhinos and elephants.','书里有犀牛和大象的照片。'),sources=S('rhinos','rhino'))
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_zjb',ROOTS,WORDS)
 extend_lessons()
