"""Burn: old verbs coalescing, regular/irregular forms and heat metaphors."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
B=[['古英语 bærnan、beornan 等；古诺尔斯语 brenna、brinna 等','使燃烧与自己燃烧的旧动词在英语中合流'],['中古英语 brennen、brinnen、birnen 等 → burn','读音次序变化；烧、燃、热痛、炽热情感等']]
def H(f,m):return B+[[f,m]]
W('burn','英 /bɜːn/；美 /bɜːrn/','燃烧、烧毁；烧伤、烫着；灼热；烧伤痕；〔另源方言〕小溪',
 '火吃掉木头，是燃烧；热锅碰着手，是烫着；脸发热、心里热切，也能借烧的感觉表达。',
 '现代形式受北欧旧动词和本族使燃、燃着的旧形式合流影响，中古英语还发生音序调整。苏格兰等语境 burn 小溪另接古英语 burna、burne 的泉、水流词，不把流水解释成着火。',B+[['另一来源：古英语 burna、burne → 方言 burn','泉、小溪；与常见燃烧义分源']],
 'burn wood 烧木头，burn your hand 烫到手，burn with excitement 兴奋得发热，burn a hole 烧个洞；burn money 比喻挥霍，burn a disc 刻录光盘。',
 'burn wood；burn your hand；burn with；burn a disc。',
 'burn—burned/burnt—burned/burnt；burn 火或热作用，boil 通常液体煮沸，不是所有热都互换。小溪义按地区语境分开。',
 ('The wood burned slowly in the fireplace.','木头在壁炉里慢慢燃烧。'),('I burned my hand on the hot pan.','我碰到热锅，把手烫了。'),
 sources=['https://en.wiktionary.org/wiki/burn#English','https://www.etymonline.com/word/burn'])
W('burning','英 /ˈbɜːnɪŋ/；美 /ˈbɜːrnɪŋ/','燃烧、灼热的；强烈、迫切的',
 '火在烧是字面；想问一个问题、想做一件事，心里像有火催着，也可说 burning。',
 'burn + -ing，相应分词形容词在中古英语和更早阶段已有。现代强烈、迫切义接灼热情感比喻，不表示问题真会冒烟。',H('burn + -ing → burning','正在烧、灼热；欲望、问题等强烈迫切'),
 'a burning candle 点燃的蜡烛，a burning desire 强烈愿望，a burning question 迫切待解的问题，a burning smell 焦糊味。',
 'a burning candle；a burning desire；a burning question；a burning smell。',
 'burning 进行、灼热或强烈，burnt 常已经烧焦结果；a burning question 不等于物理起火提问。',
 ('A burning candle stood on the table.','桌上立着一支点燃的蜡烛。'),('She had a burning desire to see the world.','她强烈渴望看看世界。'))
W('burned','英 /bɜːnd/；美 /bɜːrnd/','烧了、烧伤了；被烧过、烧焦的',
 '动作已经发生或留下结果。东西 burned 可能只是燃烧过，也可能烧坏、烧伤，要看对象与程度。',
 'burn + -ed，对应中古英语 burnede、burned 等旧形。末尾 -ed 常读 /d/，不是 /ɪd/；burnt 是另一常见过去、分词形式。',H('burn + -ed → burned','过去的烧；被火、热作用过的结果'),
 'burned wood 烧过的木头，a burned hand 烫伤的手，burned the toast 把吐司烤焦。美式常用 burned，但 burnt 也常见。',
 'burned wood；burned the toast；a burned surface。',
 'burned 与 burnt 多处可替换，不硬定一个只动词、一个只形容词；burned-out 等固定复合另看惯用法。',
 ('He burned the toast while answering the phone.','他接电话时把吐司烤焦了。'),('The fire left a pile of burned wood.','火过后留下一堆烧过的木头。'))
W('burnt','英 /bɜːnt/；美 /bɜːrnt/','烧焦、烧过的；burn 的过去式、分词变体',
 '吐司边缘黑了，闻到焦味，常见 burnt toast；它不是一种和 burned 完全不同的燃烧方式。',
 '接中古英语 brent、brynt 等旧形式，现代可对照 burn 与 -t 过去、分词结尾认识。不能说所有带 r 的动词都可换成这种 -t。',B+[['中古英语 brent、brynt 等 → burnt','旧过去、分词形演变；与 burned 并存']],
 'burnt toast 焦吐司，a burnt smell 焦味，burnt wood 烧过的木头。英式较常用，但美式形容词也常见。',
 'burnt toast；a burnt smell；burnt wood。',
 'burnt/burned 是同一动词常见变体，受地区、搭配影响；burning 仍在烧、burnt 结果，不完全同义。',
 ('The kitchen smelled of burnt toast.','厨房里有焦吐司味。'),('They removed the burnt wood from the fireplace.','他们把烧过的木头从壁炉里清了出来。'))
W('burner','英 /ˈbɜːnə/；美 /ˈbɜːrnər/','炉头、燃烧器；刻录机；其他以燃烧、刻录命名的器具',
 '煤气在灶上某个小部件燃烧，是 burner；刻录光盘的设备也接 burn 刻录这一现代动作义。',
 'burn + -er，器具、执行者派生，与较早 brennere 等词形式合流。-er 不保证一定是人。',H('burn + -er → burner','产生燃烧或执行刻录等动作的器具、人物'),
 'a gas burner 燃气炉头，a CD burner 光盘刻录机；put something on the back burner 暂把某事放到次要位置。',
 'a gas burner；a CD burner；on the back burner。',
 'burner 炉头、设备，burning 过程；back burner 比喻降低优先级，不要求真把文件放炉灶上。',
 ('She moved the pot to the smaller burner.','她把锅挪到了较小的炉头上。'),('We put the project on the back burner until next month.','我们把项目暂时放后，等下个月再处理。'))
W('brimstone','英 /ˈbrɪmstəʊn/；美 /ˈbrɪmstoʊn/','硫磺〔旧称，常文学、宗教语境〕',
 '旧名把硫磺当作会燃烧的石头来叫；今天最常碰到 fire and brimstone 这类严厉讲地狱惩罚的表达。',
 '古英语 brynstān 等为燃烧词干 + stān 石头，经中古英语 brinston、brimston 等变形。不是现代 brim 边缘 + stone 石头来解释物质。',
 [['古英语 brynstān 等 → 中古英语 brinston、brimston → brimstone','燃烧词干 + 石头的旧组合'],['现代 brimstone','硫磺旧称；文学宗教中的火与惩罚意象']],
 'fire and brimstone 地狱烈火、严厉宗教警告语气，a fire-and-brimstone sermon 严厉宣讲惩罚的布道。一般科学场景用 sulfur 或 sulphur。',
 'fire and brimstone；a sermon about fire and brimstone；an old label reading brimstone。',
 'brimstone 旧化学名称与文化用法，brim 边缘不能说明其词源；不把所有强烈讲话都字面理解成硫磺实验。',
 ('The old bottle was labelled “brimstone.”','旧瓶子上标着“硫磺”。'),('The novel describes a sermon full of fire and brimstone.','小说描写了一场严厉宣讲地狱惩罚的布道。'))
R('B2835','燃烧、热痛和炽烈感受；过程、结果和器具','BURN：火在作用，热在刺激，也借来讲热烈情绪','burn → burning → burned、burnt 两种结果形式相邻；burner 器具；sunburn、heartburn 已有；brimstone 接旧燃石名。',
 '北欧与古英语动词合流，名词小溪另源。brimstone 旧名不从现代 brim 乱拆；burnt、burned 不设绝对地域词性禁令。',
 'burn + -ing/-ed/-er；burnt 旧 -t 形式；sun/heart + burn；brimstone 接旧 burning + stone。',
 [['基本动作、过程和结果','burn · burning · burned · burnt'],['器具和感觉相关','burner · sunburn · heartburn'],['旧物质名','brimstone']],
 'burning 过程、burned/burnt 过去结果；burner 器具不只人；burn 小溪另源；heartburn 不能按心真的起火理解。',
 'The burner was still on, and the toast was burnt.\n\n炉头还开着，吐司已经焦了。','burn burning burned burnt burner sunburn heartburn brimstone')
if __name__=='__main__':save('continuation_20261030_cw',ROOTS,WORDS)
