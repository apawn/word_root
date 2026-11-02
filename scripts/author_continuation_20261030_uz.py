"""Warning, woven structures, boundaries and the vessel family."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'A1741':dict(words=['warn','warning'],label='warning：提前提醒的动作和信号',note='warn 接古英语 warnian，warning 旧英语已有相应动作名词；现代可认 warn + -ing，但不是最近才临时造的名词。'),
 'C1503':dict(words=['texture','textile','tissue'],label='tissue：织物、细胞组织与纸巾',note='tissue 经法语 tissu 织成的材料接拉丁 texere 编织；生物组织和纸类用法各有历史，不把纸巾误说成细胞组织的碎片。'),
 'B4431':dict(words=['margin','marginal'],label='margin：边缘、留白与余地',note='margin 接拉丁 margo、margin- 边缘，与 marginal 共享词干；空白、差距及余地是现代常用扩展。'),
 'B3106':dict(words=['float','fleet','fleeting'],label='fleet：漂浮材料中的船队与快速性质',note='fleet 的船、船队义接古英语 fleot，较早联系漂浮、流动词族；快速形容词接北欧语相关材料，不能只以船多就推导快速。'),
 'B2496':dict(words=['food','feed','foster'],label='foster：供食、养育到培养发展',note='foster 承接古英语 fostor 营养、养育等，与 food、feed 的更早喂养材料同族；养育、培养感情能力等现代用法各举例。'),
 'C0603':dict(words=['inner'],label='日耳曼同源比较：inner 的里面',note='inner 承接古英语 inne 的比较形式，英语 in 与拉丁 in 有更远同源关系，但 inner 不是拉丁 in- 直接借成的现代派生；也不同于否定 in-。'),
 'C1404':dict(words=['stem'],label='远层同源比较：直立支撑的 stem 名词',note='stem 名词接古英语 stemn，常联系更早站立、稳固材料，与拉丁 stare 仅作远层同源比较；阻止液体流动的 stem 另接北欧语，不硬并入此来源。'),
}
R('A1890','容器、脉管；vaso- 在现代医学中常指血管','VAS：能盛放的器物，也能发展为输送液体的管道',
 '花瓶盛水，船承载人货，血管输送血液。vase、vessel、vascular 的近源不同，但都能追到拉丁 vas 这个容器词族。',
 '拉丁 vas，复数 vasa，意为容器。vasculum 是相应小称形式；较后 vascellum 经法语形成 vessel。现代组合形式 vaso- 则把 vas 与连接元音 -o- 组合，常用于血管相关的医学词。',
 'vase 经法语借入；vessel 经更长的小称、法语变化链借入；vascular 接 vasculum、vascul- 等性质词材料。它们是同族的不同路径，不是现代英语把 vase 加各种任意字尾。',
 [['日常容器','vase'],['容器、船与身体脉管','vessel'],['脉管的性质','vascular']],
 'vase 通常是花瓶、装饰器皿；vessel 可说容器、船或脉管；vascular 是脉管的形容词。现代 vaso- 常特指血管，不能把每个专业复合词都按花瓶理解。',
 'The diagram shows blood vessels and other vascular structures.\n\n示意图展示了血管及其他脉管结构。',
 'vase vessel vascular')
W('warn','英 /wɔːn/；美 /wɔːrn/','警告；提醒提防、事先告知',
 '危险还没发生，先让别人注意：前面路滑、动作会带来后果。warn 把话指向需要提防的风险。',
 '接古英语 warnian 留意、警告，经中古英语 warnen 延续。更早日耳曼语材料有留心、防备的意思；今天常说预先提醒危险或不利后果。',
 [['古英语 warnian → 中古英语 warnen','留意、防备；提前告知危险'],['现代 warn','提醒提防；警告某人或不要做某事']],
 'warn someone about a risk 提醒某人注意风险；warn someone not to do 警告不要做；warn of danger 提醒危险；warn against doing 告诫不要做。',
 'warn someone in advance；I warned you。','warn of／about 提醒某种风险；warn against doing 告诫不要做某事。remind 更广地说提醒记起，不一定涉及危险。',
 ('The sign warns drivers about the sharp bend.','路牌提醒司机注意急弯。'),('She warned me not to touch the wet paint.','她提醒我不要碰未干的油漆。'),sources=['https://www.etymonline.com/word/warn','https://en.wiktionary.org/wiki/warn#English'])
W('warning','英 /ˈwɔːnɪŋ/；美 /ˈwɔːrnɪŋ/','警告、预警；警示信号；warn 的 -ing 形式',
 '可能出问题的提示已经亮起：一声警报、一块牌子、一次提醒，都能是 a warning。它把 warn 的动作变成可接收的信号或通知。',
 'warn + -ing 的现代关系清楚；古英语已有 warnung 一类动词名词，故英语名词有更早历史。后来也指预兆、警示、提前通知。',
 [['古英语 warnian → warnung 等','警告 → 警告动作、通知'],['现代 warning','警告；预先提示风险的信号；正在警告']],
 'a warning sign 警示牌、危险征兆；a weather warning 天气预警；without warning 毫无预兆；a warning light 警示灯；give a warning 发出警告。',
 'an early warning；take a warning seriously。','warning 可以是文字、声音，也可以是显示问题的迹象，不一定有人开口。a warning sign 既可能是实体牌子，也可能是抽象征兆。',
 ('A warning light appeared on the dashboard.','仪表盘上亮起了警示灯。'),('The lights went out without warning.','毫无预兆地，灯全灭了。'),sources=['https://www.etymonline.com/word/warn','https://en.wiktionary.org/wiki/warning#English'])
W('tissue','英 /ˈtɪʃuː/、/ˈtɪsjuː/；美 /ˈtɪʃuː/','纸巾；薄纸；组织〔生物〕；织物〔历史用法等〕',
 '老画面是细线织成一片。身体里细胞形成有结构的组织，也借这个织物名称；薄纸、纸巾则沿另一条与细薄织物相关的用法发展。',
 '经法语 tissu 织成的、织物，接拉丁 texere 编织。生物组织义经法语发展；纸类义来自 tissue paper 的缩短，其名称常联系保护细织物所用薄纸。两条线不能直接画成身体组织变成纸巾。',
 [['拉丁 texere → 法语 tissu → tissue','编织 → 织成的细织物'],['并行分支：生物组织；tissue paper 的缩短','细胞结构的组织；薄纸、纸巾']],
 'a paper tissue 一张纸巾；a box of tissues 一盒纸巾；tissue paper 薄包装纸；muscle tissue 肌肉组织；plant tissue 植物组织。',
 'a tissue sample；wrap something in tissue paper。','a tissue 通常能数一张纸巾，muscle tissue 通常把组织当材料、结构说。a tissue sample 是一份组织样本，不能照日常纸巾义猜。',
 ('She took a tissue from the box.','她从盒里抽了一张纸巾。'),('The textbook explains how muscle tissue works.','教材解释了肌肉组织怎样发挥作用。'),sources=['https://www.etymonline.com/word/tissue','https://en.wiktionary.org/wiki/tissue#English'])
W('margin','英 /ˈmɑːdʒɪn/；美 /ˈmɑːrdʒɪn/','页边空白、边缘；余地；差距；利润幅度等',
 '纸上正文旁留一圈空白，是 margin；时间和预算也能留一圈余量；两边结果相差多少，又可以说 margin。',
 '经法语或直接接拉丁 margo、margin- 边缘、边界。英语由实际边缘到页边空白，再发展出缓冲余地、差距等；商业语境另有利润幅度等专门义。',
 [['拉丁 margo／margin- → margin','边缘、界限；页边空白'],['英语抽象扩展','留出的余地；胜负差距、利润幅度等']],
 'write in the margin 写在页边；leave a margin 留出余地；a margin of error 误差范围；win by a narrow margin 险胜；profit margin 利润率、利润幅度等按指标看。',
 'wide margins；a safety margin。','margin 不全是纸边。by a large margin 说相差很多；a small margin for error 说可出错余地很小。不要把数值差距和预留空间都死译成边缘。',
 ('She wrote a question in the margin.','她在页边写了一个问题。'),('Leave a little margin in the schedule for delays.','日程中给延误留一点余量。'),('The team won by a narrow margin.','球队以微弱优势获胜。'),sources=['https://www.etymonline.com/word/margin','https://en.wiktionary.org/wiki/margin#English'])
W('vase','英 /vɑːz/；美常 /veɪs/，亦有其他读法','花瓶；装饰性瓶、器皿',
 '放在桌上用来插花或装饰的器皿，是 vase；可以装花，也可以本身就是展品。',
 '经法语 vas、vase 接拉丁 vas 容器，复数 vasa，更远来源不明。现代常用于花瓶、装饰器皿，不必给 vas 再硬编一个更古老来源。',
 [['拉丁 vas → 法语 vas／vase','容器、器皿'],['英语 vase','花瓶；装饰性器皿']],
 'a vase of flowers 一瓶花；put flowers in a vase 把花插进花瓶；a glass vase 玻璃花瓶；an antique vase 古董瓶。',
 'a ceramic vase；a vase on the table。','vase 有多种实际读音，常见英式 /vɑːz/、美式 /veɪs/；这不改变词义。vessel 范围更广，也能说船和脉管，不能处处换成 vase。',
 ('She put the flowers in a tall glass vase.','她把花插进一只高玻璃花瓶。'),('The museum displayed a painted ceramic vase.','博物馆展出了一只彩绘陶瓶。'),sources=['https://www.etymonline.com/word/vase','https://en.wiktionary.org/wiki/vase#English'])
W('vessel','/ˈvesəl/','容器、器皿；船舶；血管等脉管',
 '一个中空结构，能盛东西、承载人货或让液体通过。碗罐、船舶、血管这几个意思，都保留承载或输送的联系。',
 '经法语 vessel 等接晚期拉丁 vascellum 小容器，较早接 vasculum、vas 容器的小称材料。英语容器、船和身体管道义在较早时期已并存，不是现代从英语 vase 临时变来。',
 [['拉丁 vas → vasculum／vascellum','容器 → 小容器及相应名称'],['法语 → 英语 vessel','容器；船；输送体液的脉管']],
 'a drinking vessel 饮用器皿；a fishing vessel 渔船；a cargo vessel 货船；a blood vessel 血管；a reaction vessel 反应容器。',
 'a small vessel；blood vessels。','a blood vessel 是输血液的管道；a fishing vessel 是船。vessel 比 boat 正式、范围也不同，不要每项船名都按小船想象。',
 ('The vessel carried food and medical supplies to the island.','船把食品和医疗用品运到了岛上。'),('The diagram shows the blood vessels in the arm.','示意图展示了手臂里的血管。'),('The liquid was heated in a sealed vessel.','液体在一个密闭容器中被加热。'),sources=['https://www.etymonline.com/word/vessel','https://en.wiktionary.org/wiki/vessel#English'])
W('fleet','/fliːt/','舰队、船队；车队、机队；迅捷的〔较文学〕',
 '一批在水上航行的船，组成 a fleet；管理对象换成车辆、飞机，这个成组交通工具的名称也跟着扩大。',
 '船队名词承接古英语 fleot 船、浮动器物，较早接漂浮、流动词族，与 float 同族。形容词迅捷的则联系北欧语快速、流动相关材料，不是英语名词船队直接推出的单一路线。',
 [['古英语 fleot 与漂浮词族','浮动器物、船 → 船队'],['现代名词扩展；另有同族速度形容词','车队、机队；迅捷的']],
 'a fishing fleet 渔船队；a fleet of buses 一支公交车队；an airline’s fleet 航空公司机队；fleet feet 轻快的脚步，较文学。',
 'manage a fleet；a fleet of delivery vans。','fleet 名词是同一管理、用途等联系下的一批交通工具，不必都是军舰。a fleet of taxis 是出租车队；Fleet Street 则是专名，另有河道地名历史。',
 ('The company operates a fleet of electric vans.','公司运营着一支电动货车车队。'),('The fishing fleet returned before the storm.','渔船队在风暴前返航了。'),sources=['https://www.etymonline.com/word/fleet','https://en.wiktionary.org/wiki/fleet#English'])
W('fleeting','/ˈfliːtɪŋ/','短暂的、转瞬即逝的；fleet 的 -ing 形式',
 '像一阵水流从眼前掠过，还没抓住就过去了。a fleeting moment 是很快就消失的一瞬。',
 'fleet + -ing，接旧动词漂浮、流动，后来流逝、消失的分支。这个常用形容词不是把现代 fleet 船队直接加 -ing，就得出船队正在开动。',
 [['旧动词 fleet','漂浮、流动 → 流逝、消失'],['fleet + -ing → fleeting','流逝得很快；短暂的']],
 'a fleeting glimpse 短暂的一瞥；a fleeting thought 一闪而过的念头；a fleeting smile 转瞬即逝的微笑；a fleeting moment 短暂瞬间。',
 'a fleeting impression；a fleeting visit。','fleeting 强调时间短、很快过去；temporary 强调暂时而非永久，可以持续更长一段时间。a fleeting thought 不只是被暂时安排的想法。',
 ('A fleeting smile crossed her face.','她脸上掠过一丝微笑。'),('I caught a fleeting glimpse of the sea between the trees.','透过树木间隙，我短暂地瞥见了大海。'),sources=['https://www.etymonline.com/word/fleet','https://en.wiktionary.org/wiki/fleeting#English'])
W('foster','英 /ˈfɒstə/；美 /ˈfɑːstər/','培养、促进；寄养、抚养；寄养的',
 '先给食物和照料，让生命长起来；再给条件、鼓励，让信任、兴趣、能力长起来。这是 foster 的养育到培养的主线。',
 '接古英语 fostor 食物、养育及相应养育动词，较早属于喂养词族，与 food、feed 有历史联系。现代既保留照养儿童的用法，也常说促进某种事物发展。',
 [['古英语 fostor 及养育动词','食物、营养、养育；与 food／feed 同族'],['现代 foster','抚养、寄养；培养、促进发展']],
 'foster trust 培养信任；foster creativity 培养创造力；foster cooperation 促进合作；foster parents 寄养父母；foster children 寄养儿童。',
 'foster a sense of belonging；foster understanding。','foster 不只用于好事，也能说 foster resentment 滋长怨恨。foster children 与 adopted children 不是同一个关系名称，不宜都笼统译成已收养的孩子。',
 ('The course aims to foster curiosity and independent thinking.','课程旨在培养好奇心和独立思考。'),('They have fostered several children over the years.','这些年来，他们寄养照料过几名儿童。'),sources=['https://www.etymonline.com/word/foster','https://en.wiktionary.org/wiki/foster#English'])
W('inner','英 /ˈɪnə/；美 /ˈɪnər/','内部的、里面的；内心的；核心圈内的',
 '一层外壳里面还有一层，是 inner layer；一个人不直接给外界看的感受，是 inner feelings。先从外层向内看。',
 '承接古英语 inne 在里面的比较形式 inra、innera。与现代 in 同族；虽有旧比较来源，现代通常作为内部的性质词，不像普通比较级接 than。英语 in 与拉丁 in 远层同源，不表示 inner 借自拉丁。',
 [['古英语 inne → inra／innera','在里面 → 较里面的'],['现代 inner','内部的；内心的；较核心的']],
 'the inner wall 内墙、里面一层墙；an inner pocket 内袋；inner peace 内心平静；the inner circle 核心圈；inner city 中心城区。',
 'an inner layer；inner thoughts。','inner 与 outer 对照说内、外层。inner 有历史比较词尾，但现代通常不说 inner than this one 来当更里面的标准比较；可改为 further inside 等。',
 ('Keep the passport in an inner pocket.','把护照放在内袋里。'),('The novel explores the character’s inner life.','小说探讨了这个人物的内心世界。'),sources=['https://www.etymonline.com/word/inner','https://en.wiktionary.org/wiki/inner#English'])
W('stem','/stem/','茎、柄；词干；起源于〔stem from〕；另源：遏止',
 '花朵、叶子从一条支撑主干长出，这是 stem；问题也可以从某个来源长出，于是 stem from 表起因。另一个 stem the flow 则是挡住流动，要分开认。',
 '名词接古英语 stemn、stefn 树干、船端木柱，通常联系更早站立、支撑材料；与拉丁 stare 为远层同源比较。stem from 接主干、来源的动词扩展；阻挡流动的动词另借北欧语 stemma。',
 [['古英语 stemn／stefn → stem 名词','树干、支撑主干 → 茎、柄、词干；来源关系'],['另源北欧语 stemma → stem 动词','挡住、堵住 → 遏止流动或发展']],
 'a flower stem 花茎；the stem of a glass 杯脚、杯柄；a word stem 词干；stem from a misunderstanding 起因于误会；stem the flow 遏止流动。',
 'cut the stem；stem from several causes。','词干不一定是最小词根：teachers 去复数 -s 后，词干 teacher 还能拆 teach + -er。stem from 是起源于；stem the tide 是遏止趋势，两种结构的方向不同。',
 ('Cut the flower stems before putting them in water.','把花放进水里前，先修剪花茎。'),('Most of the problems stem from poor communication.','大多数问题起因于沟通不畅。'),('The changes helped stem the decline in visitor numbers.','这些改变帮助遏止了游客数量下降的趋势。'),sources=['https://www.etymonline.com/word/stem','https://en.wiktionary.org/wiki/stem#English'])
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_uz',ROOTS,WORDS)
 extend_lessons()
