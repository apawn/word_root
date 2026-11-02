"""-ium: common elements, a cation, a fungal body and a fictional material."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
I=[['拉丁 -ium 等中性名词、名词化形式 → 英语借词','事物、场所等名词；不能给所有词统一译成金属'],['近代科学沿用拉丁化命名','元素、物质名称常用 -ium；命名线索来自矿物、性质、地名、神话等'],['现代不同类别','ammonium 是离子名，mycelium 是菌丝体，adamantium 是虚构材料']]
W('sodium','英 /ˈsəʊdiəm/；美 /ˈsoʊdiəm/','钠',
 '元素名里的 sod- 联系 soda 苏打等旧物质名；食物标签的 sodium 常在说钠含量，不是食物里藏着一块金属。',
 'soda 的词基 + -ium，经近代科学命名形成 sodium。名称来源的苏打与元素钠并不是同一物质。',I[:2]+[['soda + -ium → sodium','从苏打相关物质名形成的元素名称']],
 'sodium content 钠含量，sodium chloride 氯化钠，a sodium atom 钠原子。',
 'sodium content；sodium chloride；a sodium atom。',
 'sodium 钠元素，sodium chloride 是氯化钠化合物；盐的 sodium 含量不等于整份盐的总质量。',
 ('The label shows the sodium content per serving.','标签标明了每份的钠含量。'),('The class drew a sodium atom.','班里画了一个钠原子示意图。'))
W('aluminium','英 /ˌæljəˈmɪniəm/；美式对应 aluminum /əˈluːmɪnəm/','铝〔aluminium、aluminum 为常见对应拼法〕',
 '同一种轻金属，英式常写 aluminium，美式常写 aluminum；拼写和音节数有区别，不是两种不同元素。',
 '沿拉丁 alūmen 明矾、近代 alumina 氧化铝等命名背景，早有 alumium、aluminum、aluminium 的调整。-ium 形式更贴近许多元素的命名模式。',I[:2]+[['alūmen → alumina 等 → alumium、aluminum、aluminium 的近代名称调整','明矾、氧化铝相关词基 → 元素铝名称'],['英美常见拼法差异','aluminium / aluminum，同一元素']],
 'aluminium foil 铝箔，an aluminium frame 铝框，an aluminum can 铝罐〔美式〕。',
 'aluminium foil；an aluminium frame；an aluminum can。',
 'aluminium/aluminum 是同物对应拼法，alumina 氧化铝是不同化学对象；不要把多一段字母一概当同种词尾变体。',
 ('The bicycle has an aluminium frame.','自行车有一个铝制车架。'),('The American label reads aluminum foil.','美式标签上写着 aluminum foil。'),
 sources=['https://en.wiktionary.org/wiki/aluminium#English','https://en.wiktionary.org/wiki/aluminum#English','https://www.etymonline.com/word/aluminium'])
W('potassium','/pəˈtæsiəm/','钾',
 '名字往前追到 potash 草木灰制碱的历史；它不是一口锅 pot 变成新金属，而是从含钾物质的旧名接出元素名。',
 'potash 的拉丁化 potassa + -ium → potassium。potash 原与锅里处理灰的工艺相关，现代又是含钾肥料等宽泛物质名称。',I[:2]+[['potash → 拉丁化 potassa + -ium → potassium','草木灰制碱相关名 → 元素钾']],
 'potassium content 钾含量，potassium salts 钾盐，a potassium atom 钾原子。',
 'potassium content；potassium salts；a potassium atom。',
 'potassium 元素钾，potash 是另一物质类别、工业名称；与 sodium 钠也不同，不能只因都是类似元素尾音而互换。',
 ('The table lists the potassium content of the samples.','表格列出了样本的钾含量。'),('The lesson compared potassium with sodium.','课程比较了钾与钠。'))
W('ammonium','英 /əˈməʊniəm/；美 /əˈmoʊniəm/','铵、铵离子',
 '先想 ammonia 氨再接上一个氢离子，形成常见铵离子；它是一种带电组合，不是周期表里另一种金属元素。',
 '新拉丁 ammōnium，现代可对应 ammonia 词基 + -ium。命名沿物质词形模式，但类别需要具体化学知识判断。',I[:2]+[['ammonia 的词基 + -ium → ammōnium → ammonium','与氨相关的铵离子名称']],
 'the ammonium ion 铵离子，ammonium salts 铵盐，ammonium chloride 氯化铵。',
 'the ammonium ion；ammonium salts；ammonium chloride。',
 'ammonia 氨与 ammonium 铵不同；-ium 常见于元素名，也不保证本词就是元素。',
 ('The diagram showed an ammonium ion.','示意图画出了一个铵离子。'),('The glossary distinguished ammonia from ammonium.','词汇表区分了氨与铵。'))
W('radium','/ˈreɪdiəm/','镭',
 '名称抓住射线、放射性这个研究特征；不是 radio 收音机后来变出来的金属，二者只是能联系到较早的射线词族。',
 '借法语 radium，接 radioactif 等射线、放射性的命名材料与 -ium；较远可联系拉丁 radius 光线、辐条。',I[:2]+[['射线、放射性词基 + -ium → 法语 radium → radium','以放射特征形成的元素名']],
 'radium research 镭研究，radium compounds 镭化合物，the discovery of radium 镭的发现。',
 'the discovery of radium；radium compounds；radium research。',
 'radium 镭，radiation 辐射是现象总称；不是只有镭能产生辐射，词名联系不能替代科学类别。',
 ('The exhibition described the discovery of radium.','展览介绍了镭的发现。'),('The archive contains early papers on radium.','档案中保存着早期镭研究论文。'))
W('thorium','英 /ˈθɔːriəm/；美 /ˈθɔːriəm/','钍',
 '名称借了北欧神话 Thor 雷神的名字；是命名者的纪念、联想方式，不是说这种元素会制造神话闪电。',
 'Thor 人名 + -ium，形成科学元素名。来自神话不代表物质虚构，thorium 与 adamantium 的现实地位不同。',I[:2]+[['Thor + -ium → thorium','借北欧雷神名形成的真实元素名']],
 'thorium minerals 含钍矿物，thorium research 钍研究，a thorium sample 钍样本。',
 'thorium minerals；thorium research；a thorium sample。',
 'thorium 是真实元素名，Thor 神话名是命名来源；不能用故事判断物质是否存在。',
 ('The mineral sample contained thorium.','矿物样本中含有钍。'),('The teacher explained why thorium was named after Thor.','老师解释了钍为何借雷神 Thor 得名。'))
W('iridium','/ɪˈrɪdiəm/','铱',
 '名称抓住某些化合物的多彩外观，联系“彩虹”；不是说金属本身必须像彩虹一样每处变色。',
 '经新拉丁 iridium，接希腊、拉丁 iris 彩虹及其词干 irid- + -ium；命名背景在多种盐呈现的颜色。',I[:2]+[['iris、irid-〔彩虹〕+ -ium → iridium','按相关盐类的多彩外观命名元素']],
 'iridium alloys 铱合金，an iridium layer 含铱层、铱层，iridium compounds 铱化合物。',
 'iridium alloys；iridium compounds；an iridium layer。',
 'iridium 铱和 iris 虹膜、彩虹等共享较早命名材料，不代表虹膜由铱金属组成。',
 ('The display showed an iridium sample.','展柜里陈列着一个铱样本。'),('The article explained the colourful origin of the name iridium.','文章解释了 iridium 这个名字与多彩外观的联系。'))
W('barium','英 /ˈbeəriəm/；美 /ˈberiəm/','钡',
 '名字抓住“重”，但最初是相关矿物很沉的命名背景，不能只凭名字断言金属钡比所有其他金属都重。',
 'baryta、barytes 等矿物名称词基 + -ium，更早接希腊 barýs 重。由矿物名称接出元素名称。',I[:2]+[['希腊 barýs〔重〕→ baryta、barytes 等 + -ium → barium','重的矿物命名背景 → 元素钡']],
 'barium compounds 钡化合物，barium sulfate 硫酸钡，a barium sample 钡样本。',
 'barium compounds；barium sulfate；a barium sample。',
 'barium 元素名，barium sulfate 是特定化合物；名字里重的来源说矿物历史，不直接规定所有现代性质。',
 ('The lesson traced barium back to a word meaning heavy.','课程把 barium 追溯到表示重的词。'),('The table compared several barium compounds.','表格比较了几种钡化合物。'),
 sources=['https://en.wiktionary.org/wiki/barium#English','https://www.etymonline.com/word/barium'])
W('mycelium','/maɪˈsiːliəm/','菌丝体',
 '一根根细丝分支、交连成真菌的营养生长部分，像一张细网；可见蘑菇常只是某些真菌长出的繁殖结构，不是整个真菌的全部。',
 '借新拉丁 mycelium，myc- 接真菌词基，-ium 为名词形式；中间 -el- 的具体由来不明，可能受其他科学词重新分析影响，不硬说成已确定的小称。',I[:1]+[['myc-〔真菌〕+ -el-〔来源不定〕+ -ium → mycelium','新拉丁真菌结构名']],
 'a network of mycelium 菌丝体网络，mycelium in the soil 土壤中的菌丝体，fungal mycelium 真菌菌丝体。',
 'a network of mycelium；mycelium in the soil；fungal mycelium。',
 'hypha 单根菌丝，mycelium 菌丝组成的生长体；不因 -ium 结尾便是矿物、金属。',
 ('The diagram showed mycelium spreading through the soil.','示意图显示菌丝体在土壤中蔓延。'),('The sample contained a dense network of mycelium.','样本里有一张密集的菌丝体网络。'))
W('adamantium','/ˌædəˈmæntiəm/','艾德曼金属等虚构坚硬金属名称',
 '听起来像周期表元素，是故意借科学命名的口气；在小说、漫画等设定里可极坚硬，现实并无因此就出现一种对应元素。',
 'adamant 坚不可摧之物、金刚等旧词基 + -ium，造出具有科学物质感的虚构名称。不同作品设定可能不同，词源不保证统一配方。',I[:2]+[['adamant + -ium → adamantium','坚硬、金刚的联想 + 科学命名词尾'],['现代虚构材料名','故事中的超硬金属，非独立真实元素']],
 'a fictional metal called adamantium 名为 adamantium 的虚构金属，adamantium claws 艾德曼金属爪〔作品语境〕，an adamantium weapon 虚构材料武器。',
 'adamantium claws；a fictional metal called adamantium；an adamantium weapon。',
 'adamantium 虚构金属，thorium 神话名借来的真实元素；名称像不像科学不能代替判断存在与否。',
 ('The character’s claws were made of adamantium.','角色的爪由虚构的艾德曼金属制成。'),('The glossary marked adamantium as a fictional material.','词汇表把 adamantium 标为虚构材料。'))
R('A1768','拉丁名词形式和科学名称传统，具体类别看整词','-IUM：名字像科学，不代表全是金属、元素或真实物质','常用元素按来源线索记；ammonium 铵离子、mycelium 菌丝体、adamantium 虚构金属另外分；auditorium、colloquium 是另一类拉丁名词借词。',
 'sodium 联系 soda，potassium 联系 potash，radium 联系射线，iridium 联系彩虹，thorium 借神名。-ium 是命名形式，不能代替物质类别。',
 '拉丁 -ium 等名词形式进入英语借词；近代科学沿用拉丁化命名 → 大量元素、物质名；现代也用来造虚构科学感名称。',
 [['常用元素与矿物、性质线索','sodium · aluminium · potassium · calcium · barium · radium · iridium · osmium'],['神话、天体、放射性等名称','thorium · uranium · plutonium · helium'],['离子、同位素与菌丝结构','ammonium · deuterium · mycelium'],['拉丁活动、场所名词','auditorium · colloquium'],['虚构科学材料','adamantium']],
 'aluminium/aluminum 英美对应，alumina 氧化铝另物；ammonium 非元素；helium 非金属；mycelium 真菌；adamantium 虚构。',
 'The list included real elements, an ammonium ion and the fictional metal adamantium.\n\n列表包括真实元素、铵离子，以及虚构金属 adamantium。','sodium aluminium potassium calcium barium radium iridium osmium thorium uranium plutonium helium ammonium deuterium mycelium auditorium colloquium adamantium')
if __name__=='__main__':save('continuation_20261030_ey',ROOTS,WORDS)
