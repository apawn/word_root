"""Plant, journal and shape: growth, daily records and making form."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
PL=[['拉丁 planta、plantāre → 古英语 plante、plantian','幼芽、栽种；后又受法语同族形式影响'],['现代 plant','植物、种植；安置、埋设；工厂设备等延伸']]
def P(f,m):return PL+[[f,m]]
W('plant','英 /plɑːnt/；美 /plænt/','植物；种植；安放、植入；工厂、工业设备',
 '把幼苗安进土里让它扎根；想法、人员、设备也能借安置、建立的动作来理解。',
 '拉丁 planta 幼芽、plantāre 栽种很早进入英语，后又受法语影响。工厂义联系设立、安置的设备和场所，不是因为工厂会光合作用。',PL,
 'water the plants 浇植物，plant a tree 种树，plant an idea 植入想法，a power plant 发电厂。plant evidence 可指偷偷放入假证据。',
 'water the plants；plant a tree；plant an idea；a power plant。',
 'plant 工厂常着眼工业设施，factory 工厂更常着眼制造生产场所；a plant 名词是植物或工厂，按上下文认。',
 ('They planted three trees beside the school.','他们在学校旁种了三棵树。'),('The old power plant has been converted into a museum.','旧发电厂被改造成了博物馆。'),sources=['https://www.etymonline.com/word/plant','https://en.wiktionary.org/wiki/plant#English'])
W('planter','英 /ˈplɑːntə/；美 /ˈplæntər/','种植者；种植园经营者；花盆、种植容器',
 '做种植的人能叫 planter，放土栽花的大容器也能这样叫；后缀不只命名人。',
 'plant + -er，按执行种植或承载栽种命名。历史种植园经营者用法按相应社会背景理解。',P('plant + -er → planter','种植的人；栽种容器、相关设备'),
 'a wooden planter 木制种植箱，a window planter 窗边花槽，a tea planter 茶园经营者。',
 'a wooden planter；a window planter；a tea planter。',
 'planter 花盆容器与 plant 植物分清；flowerpot 更直接说花盆，planter 常也涵盖大花槽、种植箱。',
 ('She filled the wooden planter with soil.','她往木制种植箱里填了土。'),('The book describes the life of a tea planter.','这本书描写一位茶园经营者的生活。'))
W('replant','英 /ˌriːˈplɑːnt/；美 /ˌriːˈplænt/','重新栽种；补种',
 '原来的种植被移走、毁了或位置不合适，于是再种一次。',
 're- 再次 + plant，动词重音通常在 plant。重复的是栽种动作，不要求把完全同一棵树放回原洞。',P('re- + plant → replant','再次种植、重新安排栽种'),
 'replant the garden 重新栽种花园，replant trees 补种或重新栽树。',
 'replant the garden；replant trees；replant in spring。',
 'replant 再种，transplant 从一处移到另一处；同一个移栽过程可以包含重新栽下这一步，但着眼点不同。',
 ('They replanted the garden after the storm.','风暴后，他们重新栽种了花园。'),('The seedlings will be replanted in larger pots.','幼苗将被重新栽进较大的盆里。'))
W('eggplant','英 /ˈeɡplɑːnt/；美 /ˈeɡplænt/','茄子〔美式常用〕',
 '今天常见紫色长茄子，名字却保留了某些白色、像鸡蛋的品种的外形。',
 'egg 鸡蛋 + plant 植物，起初指白色、卵形品种，后来扩展成常用茄子名称。不是所有茄子都必须白且圆。',P('egg + plant → eggplant','按白色卵形品种命名 → 茄子的通称'),
 'roasted eggplant 烤茄子，an eggplant dish 茄子菜肴。英式常用 aubergine。',
 'roasted eggplant；grilled eggplant；an eggplant dish。',
 'eggplant 与 aubergine 常指同一种蔬菜，地区习惯不同；词形中的 egg 不表示菜里一定加了鸡蛋。',
 ('We grilled eggplant with a little olive oil.','我们用少许橄榄油烤了茄子。'),('The recipe lists eggplant as aubergine.','食谱把茄子写作 aubergine。'))
R('B2557','幼芽、栽种到安置；设备场所与外形命名','PLANT：安置幼苗让它生长；也借指建立、设置','plant → planter、replant，再 eggplant 讲命名品种；transplant、houseplant 共享。',
 '古老拉丁借词进入英语后继续扩展。工厂和间谍安插等联系安置、设置，不把一切死译成绿色植物。',
 'plant + -er；re- + plant；egg/house + plant；trans- + plant 的借入同族关系。',
 [['基本词、人物容器与再种','plant · planter · replant · transplant'],['植物类别','houseplant · eggplant']],
 'plant 名词植物/工厂靠语境；planter 人或容器；eggplant 白卵形旧品种得名，现代不只那一种外观。',
 'She put the houseplant in a larger planter before replanting the garden.\n\n她把室内植物放进较大花盆后，又去重新栽种花园。',
 'plant planter replant transplant houseplant eggplant')
JO=[['拉丁 diurnālis、diurnus〔每日的〕→ 法语 jornel、journal','一天、每日事项、记录'],['经中古英语及后续法语借入 → journal','日记、账簿、刊物；不同用法有不同传入阶段']]
def J(f,m):return JO+[[f,m]]
W('journal','英 /ˈdʒɜːnl/；美 /ˈdʒɜːrnl/','日记、日志；期刊；记录〔动词〕',
 '每天记下发生的事，可以是自己的心情，也可以是业务记录；刊物则把内容持续刊行。',
 '经法语等接拉丁每日的词，英语有中古及后来借入阶段。现代 academic journal 可以每月、每季出版，不要拿每日的旧来源强定发行频率。',JO,
 'keep a journal 写日记，a travel journal 旅行日志，an academic journal 学术期刊，journal about your day 记录一天。',
 'keep a journal；a travel journal；an academic journal；a journal article。',
 'diary 常个人按日记录，journal 范围更宽，也可日志、学术期刊；magazine 杂志多给普通读者，范围仍可重合。',
 ('She keeps a journal of her travels.','她写旅行日志。'),('The study appeared in an academic journal.','研究发表在一本学术期刊上。'),sources=['https://www.etymonline.com/word/journal','https://en.wiktionary.org/wiki/journal#English'])
W('journalist','英 /ˈdʒɜːnəlɪst/；美 /ˈdʒɜːrnəlɪst/','新闻工作者；记者',
 '为公众采集、核实、撰写或报道新闻的人；不是所有写私人日记的人都叫记者。',
 'journal + -ist，形成与法语同族职业词相关。这里接刊物、公共报道的 journal 支线，不接私人日记才是唯一工作。',J('journal + -ist → journalist','从事刊物、新闻报道的人'),
 'a local journalist 当地记者，an investigative journalist 调查记者，a freelance journalist 自由新闻工作者。',
 'a local journalist；an investigative journalist；a freelance journalist。',
 'journalist 范围可涵盖多种新闻工作，reporter 更直接强调采访报道者；写个人 journal 不自动成为职业 journalist。',
 ('The journalist interviewed several local residents.','记者采访了几位当地居民。'),('She works as a freelance journalist.','她是一名自由新闻工作者。'))
W('journalism','英 /ˈdʒɜːnəlɪzəm/；美 /ˈdʒɜːrnəlɪzəm/','新闻业；新闻报道工作、实践',
 '从那个记者，转到整个采访、核实、编辑、发布新闻的工作和行业。',
 '借法语 journalisme，现代对应 journal + -ism；不是 -ism 都表示某种信仰主义，这里是职业活动、行业。',JO+[['法语 journalisme → journalism','新闻报道的工作、行业；现代对应 journal + -ism']],
 'investigative journalism 调查性报道，study journalism 学新闻，a career in journalism 新闻职业生涯。',
 'investigative journalism；study journalism；a career in journalism。',
 'journalist 人，journalism 行业和工作，journalistic 相关性质。journalism 不是每个人写日记的总称。',
 ('He studied journalism at university.','他大学学的是新闻专业。'),('The award recognizes outstanding investigative journalism.','这个奖项表彰出色的调查性报道。'))
W('journalistic','英 /ˌdʒɜːnəˈlɪstɪk/；美 /ˌdʒɜːrnəˈlɪstɪk/','新闻工作的；新闻报道风格的',
 '用来说明记者工作遵循的规范、使用的手法和写作风格。',
 'journal + -istic，也可从 journalist + -ic 认形，表示职业、活动相关。不是自动夸文章有权威，而是说明所属范围或风格。',J('journal + -istic／journalist + -ic → journalistic','与新闻工作、报道方式有关'),
 'journalistic standards 新闻专业规范，journalistic ethics 新闻伦理，a journalistic style 新闻报道文风。',
 'journalistic standards；journalistic ethics；a journalistic style。',
 'journalistic 相关新闻工作，academic 学术的；journal article 学术期刊文章也未必是 journalistic writing。',
 ('The editor insisted on high journalistic standards.','编辑坚持较高的新闻专业规范。'),('The book combines research with a clear journalistic style.','这本书把研究与清楚的新闻报道文风结合起来。'))
R('B4280','每日记录背景到日记、期刊与新闻工作','JOURNAL：把事情记录下来；刊物支线长出新闻职业','journal → journalist → journalistic，journalism 与职业群一起读；私人日志与新闻行业分清。',
 '来源有每日之意，现代学术期刊却不一定日报。不同借入阶段与用法分支不必编成一条现代后缀流水线。',
 'journal + -ist/-istic；法语 journalisme → journalism，现代对应 -ism。',
 [['记录和刊物','journal'],['新闻职业、工作与规范','journalist · journalism · journalistic']],
 'journal 私人日志或期刊；journalist 记者不是所有写日记的人；-ism 此处职业；academic journal 不保证 journalistic 文风。',
 'The journalist kept a travel journal while studying local journalism.\n\n记者研究当地新闻业时，也写着旅行日志。',
 'journal journalist journalism journalistic')
SH=[['古英语 ġesceap〔名词〕、scieppan 等〔动词〕→ shape','形态、所造之物；塑造、创造'],['现代 shape','形状、状态；塑造外形、影响发展']]
def S(f,m):return SH+[[f,m]]
W('shape','/ʃeɪp/','形状；体形、状态；塑造、影响；使成形',
 '橡皮泥能捏出一个轮廓，经历也能慢慢捏出人的性格和选择。',
 '名词与动词分别有古英语旧形式，接创造、成形背景。今天 shaped 是规则过去、分词，旧 shapen 仍留在 misshapen 等词里。',SH,
 'the shape of the box 箱子形状，in good shape 状态好，take shape 逐渐成形，shape the future 影响未来走向。',
 'in good shape；take shape；shape the future；all shapes and sizes。',
 'shape 常外形、轮廓或状态，form 范围更广且可指结构、形式；in shape 可体能好，不只外表轮廓漂亮。',
 ('The idea is beginning to take shape.','这个想法开始逐渐成形。'),('Her early experiences shaped the way she thinks.','早年的经历塑造了她的思考方式。'))
W('shaped','/ʃeɪpt/','有某种形状的；被塑造的；shape 的过去式、分词',
 '一方面看成形后的样子，一方面看是什么把它塑成这样。',
 'shape + -ed，末尾在 /p/ 后读 /t/。历史有中古英语相应形式；前有形状修饰时常组成复合形容词，本页不另列连字符词头。',S('shape + -ed → shaped','已经成形；具有某种形状、受某事塑造'),
 'beautifully shaped 造型优美的，shaped by experience 被经历塑造；前面加具体外形可进一步限定。',
 'beautifully shaped；shaped by experience；carefully shaped。',
 'shaped 是形成、被塑造后的状态，shapely 是外形匀称漂亮；某物 shaped 不自动表示漂亮。',
 ('The bowl was carefully shaped by hand.','这个碗经过手工仔细塑形。'),('Her outlook was shaped by years of travel.','她的观念受到多年旅行经历的塑造。'))
W('shaping','/ˈʃeɪpɪŋ/','塑形、塑造过程；shape 的 -ing 形式',
 '关注轮廓和走向正在怎样被做出来，而不是只看最后成品。',
 'shape 去 e + -ing，中古英语已有活动名词 schapynge 等形式。也接影响、决定走向的抽象用法。',S('shape + -ing → shaping','使成形的过程；影响发展'),
 'the shaping of policy 政策形成过程，shaping the future 塑造未来，a shaping tool 塑形工具。',
 'the shaping of；shaping the future；a shaping tool。',
 'shaping 过程，shape 形状或塑造动词；the shaping of the bowl 是做形状的过程，不只是 the shape of the bowl 那个轮廓。',
 ('The course teaches cutting and shaping wood.','课程教授木材切割和塑形。'),('Many groups took part in the shaping of the policy.','许多团体参与了政策的形成。'))
W('shaper','英 /ˈʃeɪpə/；美 /ˈʃeɪpər/','塑造者；成形工具、机床',
 '谁在决定样子、方向，或哪种工具把材料加工成形，就按角色叫 shaper。',
 '现代对应 shape + -er，中古英语有 schapere 等形式，还与更旧创造者词及北欧同族形式相关，不必断言单在现代新造。',S('中古英语 schapere 等 → shaper','塑造者、创造者；现代也指成形工具'),
 'a shaper of opinion 舆论塑造者，a wood shaper 木工成形机。',
 'a shaper of opinion；a wood shaper；a key shaper of。',
 'shaper 是执行者、器具，shape 是结果形状或动作；人物 shaper 常是影响者，不必真用手捏材料。',
 ('The editor became an important shaper of public opinion.','这位编辑成了影响舆论的重要人物。'),('The workshop uses a shaper to form the wooden edges.','工坊用成形机加工木材边缘。'))
W('shapely','/ˈʃeɪpli/','外形优美、匀称的',
 '不是单纯有一个形状，而是轮廓匀称、看起来好看；常描述身体、物体造型。',
 'shape + 形容词 -ly，中古英语已有 schaply 等形式，更早联系有不确定处。这个 -ly 常作形容词，不强当副词。',S('shape + -ly → shapely','形态合宜、优美匀称'),
 'a shapely vase 造型优美的花瓶，shapely legs 匀称的腿。描述人时带外貌审视的语气，按交流场合选用。',
 'a shapely vase；shapely legs；a shapely design。',
 'shapely 好看、匀称，shaped 只是成某形、被塑造；beautifully shaped 与 shapely 有时意思接近。',
 ('The potter made a shapely vase.','陶工做了一个造型优美的花瓶。'),('The chair has a simple, shapely design.','椅子设计简洁、线条优美。'))
W('shapeless','/ˈʃeɪpləs/','没有明确形状的；松垮、不成形的',
 '看不出清楚轮廓，或东西塌塌地失去该有的样子；不是真完全没有物理形状。',
 'shape + -less，中古英语 schaples 等旧形延续。常否定清楚、合宜的形态，而不是数学意义上一点边界都没有。',S('shape + -less → shapeless','缺少明确、规整或合宜形态'),
 'a shapeless mass 一团不成形的东西，a shapeless sweater 松垮毛衣，a shapeless draft 结构未成形的初稿。',
 'a shapeless mass；a shapeless sweater；a shapeless draft。',
 'shapeless 轮廓、结构不成形，misshapen 形状歪曲、畸变；一个模糊松垮，一个更强调形态不正常。',
 ('The old sweater had become shapeless.','旧毛衣已经变得松垮没形。'),('The clay lay in a shapeless mass on the table.','黏土在桌上摊成一团，没有明确形状。'))
W('reshape','/ˌriːˈʃeɪp/','重新塑形；改变格局、走向',
 '已有一个样子，再把它改成另一个样子；行业、城市也可以重新形成格局。',
 're- 再次、重新 + shape。既可实体重新造型，也可抽象改变结构、发展方式。',S('re- + shape → reshape','重新成形；改造结构与走向'),
 'reshape the clay 重塑黏土，reshape an industry 改变行业格局，reshape the future 改变未来。',
 'reshape the clay；reshape an industry；reshape the future。',
 'reshape 改变形态、格局，replace 替换成另一个对象；改造现有制度不一定就是完全换掉。',
 ('She softened the clay and reshaped the bowl.','她把黏土弄软，重新给碗塑形。'),('The new technology is reshaping the industry.','新技术正在改变行业格局。'))
W('shapeshifter','英 /ˈʃeɪpʃɪftə/；美 /ˈʃeɪpʃɪftər/','变形者；能变化形态的角色',
 '故事里人一转身变成动物、另一副面孔，按变换外形这种能力命名。',
 'shape 形态 + shifter 变换者。是幻想、神话及比喻里的常见称呼，不是现实生物学类别。',S('shape + shifter → shapeshifter','能变换外形、身份表现的角色'),
 'a mythical shapeshifter 神话变形者，a shapeshifter in the story 故事里的变形角色。',
 'a mythical shapeshifter；a powerful shapeshifter；a shapeshifter character。',
 'shapeshifter 变化形态，shaper 塑造者；shaper 可木工工具，通常不是小说中的变形生物。',
 ('The legend features a shapeshifter who becomes a wolf.','传说里有个能变成狼的变形者。'),('The game lets you play as a shapeshifter.','游戏让你扮演变形者。'))
W('shapewear','英 /ˈʃeɪpweə/；美 /ˈʃeɪpwer/','塑身衣；塑形内衣',
 '穿在衣服里面，靠包裹、支撑改变外面看见的轮廓；名字直接是塑形用途的衣着。',
 'shape 塑形 + wear 衣着、穿着用品。现代商品类别名，不由名称保证永久改变身体。',S('shape + wear〔衣着〕→ shapewear','用于修饰、塑造身体轮廓的衣着'),
 'comfortable shapewear 舒适塑身衣，wear shapewear 穿塑身衣。通常不可数，具体一件可说 a piece of shapewear。',
 'wear shapewear；comfortable shapewear；a piece of shapewear。',
 'shapewear 塑形衣，sportswear 运动服；用途可能交叉，但不能只见紧身就当同一类别。',
 ('The shop sells underwear and shapewear.','店里出售内衣和塑身衣。'),('She chose comfortable shapewear for the fitted dress.','她为修身连衣裙选了舒适的塑身衣。'))
R('B3012','成形、轮廓到状态和发展走向；创造的本族词','SHAPE：把东西做成一个样子，也能塑造人生、格局','shape → shaped、shaping、shaper；shapely/shapeless 对照形态；reshape 再塑；shapeshifter、shapewear 固定组合。misshapen 已有共享。',
 '实体捏形最直观，经历影响想法也可借塑造理解。旧 shapen 留在 misshapen，现代 shaped 却是规则变化。',
 'shape + -ed/-ing/-er/-ly/-less；re- + shape；shape + shifter/wear；mis- + 旧 shapen。',
 [['基本形态、过程和执行者','shape · shaped · shaping · shaper'],['形态评价和改造','shapely · shapeless · misshapen · reshape'],['固定用途和角色','shapeshifter · shapewear']],
 'shapely 形容词优美，shaped 成形不保证美；shapeless 模糊不成形、misshapen 歪曲；reshape 改造不同于 replace 替换。',
 'The shaper reshaped the shapeless clay into a shapely bowl.\n\n塑形者把不成形的黏土重新塑成一个匀称的碗。',
 'shape shaped shaping shaper shapely shapeless misshapen reshape shapeshifter shapewear')
if __name__=='__main__':save('continuation_20261030_bb',ROOTS,WORDS)
