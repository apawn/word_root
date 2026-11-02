"""Doll, tan, beam and selected useful ol chemical names."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
D=[['Dorothy 的昵称 Doll','女性名字、亲昵称呼'],['称呼 → doll 玩具人偶','小人形玩具；再有亲昵人物称呼、打扮等'],['doll + -y → dolly','儿语娃娃；又借人名式词形给设备命名']]
W('doll','英 /dɒl/；美 /dɑːl/','玩偶、娃娃；亲昵称呼；〔doll up〕打扮',
 '像人的小玩具是 doll；You’re a doll 在熟悉语境也可能夸你真贴心。doll someone up 则像把人偶装扮漂亮一样，说精心打扮。',
 '来自 Dorothy 的昵称 Doll。亲昵人物称呼后来转为玩具娃娃，再有不同人物称呼和打扮动作；不是原先就有一个表示娃娃的小后缀。',D[:2],
 'a toy doll 玩具娃娃，a rag doll 布娃娃，doll up for a party 为聚会精心打扮，You’re a doll 你真贴心〔熟悉的亲昵称呼〕。',
 'a toy doll；doll up。',
 'doll 指真人时可能亲昵，也可能轻慢、过分熟络，须看关系；dollar 美元不从 doll 娃娃加后缀来。',
 ('The child tucked her doll into a tiny bed.','孩子把娃娃安置进小床。'),('They got dolled up for the party.','他们为聚会精心打扮了一番。'),sources=['https://en.wiktionary.org/wiki/doll#English','https://www.etymonline.com/word/doll'])
W('dolly','英 /ˈdɒli/；美 /ˈdɑːli/','娃娃〔儿语〕；搬运小车、摄影移动台等',
 '孩子的 dolly 可以是娃娃；搬家工人的 dolly 是推重物的小车；摄影场景里则是让相机平稳移动的台车。由场景换画面。',
 'Doll 昵称加亲昵 -y，联系 Dorothy。名称后来也用于多类工具、设备，类似其他人名给器具命名；具体为何每种设备叫 dolly，并非都已确定。',D,
 'a child’s dolly 孩子的娃娃，a furniture dolly 家具搬运小车，a camera dolly 摄影移动台，dolly towards a subject 用移动台向对象靠近。',
 'a furniture dolly；a camera dolly。',
 '摄影里 dolly 通常指相机位置实际移动，zoom 则调整镜头视角，画面效果和几何关系不完全相同。',
 ('She carried her dolly everywhere.','她到哪儿都带着娃娃。'),('The crew moved the camera on a dolly.','摄制组用移动台移动摄影机。'))
R('B3846','人名昵称转为娃娃，又形成亲昵称呼和设备名','DOLL：像一个小人，名字也能借给小装置','doll → dolly；doll up 是打扮的常用短语。',
 '人名、玩具、设备不必是毫无联系的三个死词。昵称的传播路线能帮助理解，但每种机械命名细节不硬编。',
 'Dorothy → Doll → doll；-y 亲昵形式 dolly；up 参与打扮短语。',
 [['玩偶、昵称与设备','doll · dolly']],
 'dolly 摄影移动与 zoom 不同；doll 指真人语气看关系；dollar 另有来历。',
 'The child put her dolly beside the larger doll.\n\n孩子把小娃娃放在较大的玩偶旁。','doll dolly')
T=[['法语 tan、相关拉丁 tannum、tannāre','制革用树皮及用它处理皮革，通常联系凯尔特语树名'],['鞣制皮革 → 皮肤变棕、黄褐色','tan、suntan 的现代颜色分支'],['职业、场所与另源比较','tanner 制革者；tannery 制革厂；mistletoe 里的旧 tān 是枝条']]
W('tan','/tæn/','鞣制皮革；晒成棕褐色、晒黑；棕褐色、浅黄褐色',
 '处理兽皮让它成为皮革，旧动作叫 tan。皮革带棕黄色，人的皮肤被晒成棕褐色也借同词说；衣服的 tan 则直接是颜色。',
 '联系法语 tan 树皮及 tannum、tannāre 等制革词，通常追到凯尔特语树名。英语制革、颜色分支互相关联，不是 tan 原先只说日晒。',T[:2],
 'tan leather 鞣制皮革，get a tan 晒成棕褐色，tan trousers 黄褐色裤子，a deep tan 较深的晒后肤色。',
 'get a tan；tan leather；tan trousers。',
 'tan 制革与 tan 颜色按对象区分；suntan 把 sun 太阳加出来，tanned 也可说已鞣制或已晒黑。',
 ('She wore a tan coat with dark boots.','她穿着黄褐色外套，配深色靴子。'),('The workshop once tanned animal hides into leather.','这间作坊过去把兽皮鞣制成皮革。'),sources=['https://en.wiktionary.org/wiki/tan#English','https://www.etymonline.com/word/tan'])
W('tanner','英 /ˈtænə/；美 /ˈtænər/','制革工、鞣皮工；使皮肤呈棕褐色的人或产品等',
 'tan 可以把兽皮处理成革，tanner 就是做这项工作的人。现代美容语境也可从皮肤着色义命名相应人员、产品，先看行业。',
 '承中古英语、古法语相关职业词，现代对应 tan + -er，双写 n。皮革职业义和着色用品义各取 tan 的相关动作。',T[:2]+[['tan + -er → tanner','负责鞣皮、相应着色的人或物']],
 'a leather tanner 制革工，a master tanner 制革师傅；self tanner 可说仿晒着色产品，常也有分写、连字符形式。',
 'a leather tanner；a master tanner。',
 'tanner 职业义不是泛指所有晒黑的人；另有较旧货币同形词，日常不必一并展开。',
 ('The tanner worked with hides from nearby farms.','制革工处理附近农场送来的兽皮。'),('The museum restored the tanner’s workshop.','博物馆修复了制革工的作坊。'))
W('tannery','/ˈtænəri/','制革厂、鞣革作坊；制革业',
 'tanner 是干活的人，tannery 是干这项工作的厂、作坊，也可说这门业务。把职业和场所摆在一起就不难记。',
 'tan + -ery，形成工作场所、行业名词，并联系法语 tannerie。双写 n，里面不是一个意思叫 nery 的词根。',T,
 'a leather tannery 制革厂，an old tannery 旧鞣革作坊，work at a tannery 在制革厂工作。',
 'an old tannery；work at a tannery。',
 'tannery 不是一个工人；tanner 是人，tanning 是过程，tannery 是场所或业务。',
 ('The old tannery has been converted into a museum.','旧制革厂已改成博物馆。'),('Workers delivered the hides to the tannery.','工人把兽皮运到制革厂。'))
Mi=[['古英语 mistel + tān 枝条 → misteltān','槲寄生的枝条、植株名称'],['中古英语 mistelto 等 → mistletoe','词尾受 toe 等熟悉形式影响'],['现代用法','槲寄生植株及作为圣诞装饰的一枝']]
W('mistletoe','英 /ˈmɪsəltəʊ/；美 /ˈmɪsəltoʊ/','槲寄生；槲寄生装饰枝',
 '这种植物长在其他树木上，传统圣诞装饰中常见一小枝带叶、白果的槲寄生。英文末尾看着像脚趾，历史却是枝条。',
 '承古英语 misteltān，mistel 槲寄生 + tān 枝条；后来词尾受熟悉拼写、形式影响成 toe。这里的 tān 不是制革、晒黑的 tan。',Mi,
 'a sprig of mistletoe 一枝槲寄生，hang mistletoe 悬挂槲寄生装饰，under the mistletoe 在槲寄生枝下，联系传统节日亲吻习俗。',
 'a sprig of mistletoe；under the mistletoe。',
 '拼写里的 t 在常见读法中不单独发出；toe 不是这株植物长脚趾的证据。不同槲寄生植物、装饰传统有差异。',
 ('They hung a sprig of mistletoe above the doorway.','他们在门口上方挂了一枝槲寄生。'),('Mistletoe grew high in the old tree.','槲寄生长在老树高处。'))
R('B2702','制革树皮到鞣皮、棕色，另辨旧枝条 tān','TAN：先把皮鞣成革，再借它说棕褐色','tan → tanner、tannery、suntan；mistletoe 单列旧枝条来源。',
 '制革工在制革厂处理皮革，颜色再延伸到晒后肤色。mistletoe 看似也接 tan，实际上是另一个表示枝条的旧词。',
 'tan、tannāre 等制革词族；-er 人物，-ery 场所，sun 太阳；mistel + tān → mistletoe。',
 [['动作、人物与场所','tan · tanner · tannery'],['日晒颜色','suntan'],['同形旧词的比较','mistletoe']],
 'tanner 人、tannery 场所；tan 也作颜色；mistletoe 不来自晒黑或脚趾。',
 'The tanner worked in a tannery beside the river.\n\n制革工在河边的制革厂工作。','tan tanner tannery suntan mistletoe')
Be=[['古英语 bēam','树木、柱、横梁等'],['柱状形象 → 光柱、光束','古英语已有光义，具体桥接常联系拉丁光柱的译法'],['发光 → 笑容明亮；定向传播','beam 作动词发光、喜笑颜开、传送']]
W('beam','/biːm/','梁、横梁；光束；喜笑颜开；定向传送',
 '屋顶一根长梁是 beam；黑屋里一束光也像亮着的长柱。笑得整张脸亮起来，可以 beam；电视信号向某处传，也可用这个定向发出的词。',
 '承古英语 bēam，先有树、木材、柱梁义，光柱义也很早，常被联系到翻译中的光柱形象。动词从发光扩到灿烂笑容、定向传送。',Be,
 'a wooden beam 木梁，a beam of light 一束光，beam with pride 骄傲得喜笑颜开，beam a signal 发射、传送信号。',
 'a beam of light；beam with pride；a wooden beam。',
 'beam 是一束有方向的光，也可说梁；动词笑容义不是照字面发射光子。结构梁的材料也不只木头。',
 ('A beam of sunlight crossed the wooden floor.','一束阳光斜穿木地板。'),('She beamed with pride when her son received the prize.','儿子领奖时，她骄傲得满脸笑容。'),sources=['https://en.wiktionary.org/wiki/beam#English','https://www.etymonline.com/word/beam'])
R('B4007','树木、梁柱到光束，再到笑容和传送','BEAM：一根长梁、一束长光，笑容也能亮起来','beam → sunbeam、moonbeam。',
 '阳光、月光在前项说明来源；beam 自身还保留梁和动词笑容、传送义。用形状、光亮串起来，再看对象。',
 'bēam → beam；sun 太阳、moon 月亮 + beam；更远树名来源有讨论。',
 [['梁、光与光源复合','beam · sunbeam · moonbeam']],
 '梁不只木制；beam with pride 是笑容；beamish、部分 beamer 行业用法先略过。',
 'A moonbeam fell across the old roof beam.\n\n一束月光落在旧屋顶梁上。','beam sunbeam moonbeam')
M=[['methane 甲烷的命名词干','meth- 相关命名历史还联系木醇、methylene 等旧术语'],['methane 去 e + -ol → methanol','含一个碳的 CH₃OH；-ol 指向醇类官能团命名']]
W('methanol','英 /ˈmeθənɒl/；美 /ˈmeθənɔːl/','甲醇',
 '先看名字给的两层：meth- 是一碳骨架的命名线索，-ol 说明醇的相关结构。甲醇的分子式是 CH₃OH，不把所有名字带醇的物质都混成饮料酒。',
 'methane 去词尾 e + -ol。更早 meth- 命名史联系木醇、methylene 等术语，现代名称已经形成一碳系列的规则。',M,
 'methanol as a solvent 甲醇作溶剂，a methanol sample 甲醇样品，methanol production 甲醇生产。此处学习名称、结构和常见语境。',
 'methanol as a solvent；a methanol sample。',
 'methanol 甲醇与 ethanol 乙醇名称相近，但碳骨架和性质不同；-ol 是化学命名线索，不表示可饮用。',
 ('The laboratory used methanol as a solvent.','实验室用甲醇作溶剂。'),('The sample contained methanol and water.','样品含甲醇和水。'),sources=['https://en.wiktionary.org/wiki/methanol#English','https://www.affixes.org/-ol.html'])
G=[['希腊 glykys 甜的 + -ol','glycol 旧命名联系乙二醇的味觉描述'],['现代化学分类与常见简称','可说一类二元醇；单用时常指 ethylene glycol 乙二醇']]
W('glycol','英 /ˈɡlaɪkɒl/；美 /ˈɡlaɪkɔːl/','二元醇；〔常指〕乙二醇',
 '一个分子里有两个醇羟基的这类结构，可以见到 glycol 名称；不带前项时常说乙二醇。看 ethylene glycol、propylene glycol 等完整名，才能分清具体化合物。',
 '希腊 glykys 甜的相关词干 + -ol，历史按相应物质特点命名。现代术语中 glycols 通常说两羟基位于不同碳原子的二元醇。',G,
 'ethylene glycol 乙二醇，propylene glycol 丙二醇，a glycol solution 二元醇溶液。名称中的甜来自命名史，学习不靠尝味道辨物。',
 'ethylene glycol；propylene glycol。',
 'glycol 可是类别，也可是乙二醇简称；diol 范围按含两羟基定义更宽，读专业文本要看是否采用更具体分类。',
 ('The label identifies the liquid as ethylene glycol.','标签标明液体是乙二醇。'),('The report compares several glycol mixtures.','报告比较了几种二元醇混合物。'),sources=['https://en.wiktionary.org/wiki/glycol#English','https://goldbook.iupac.org/terms/view/G02654/pdf'])
Di=[['di- 两 + -ol 羟基命名形式','diol：有两个羟基的有机化合物'],['类别名称','二元醇类名称；两个羟基的位置还需完整名称说明']]
W('diol','英 /ˈdaɪɒl/；美 /ˈdaɪɔːl/','二醇、含两个羟基的有机化合物',
 '把分子当骨架，数出两处 —OH，di- 两就有了落点。diol 是结构类别，不是一瓶混了两种酒精的液体。',
 'di- 两 + -ol，两个羟基这一命名特征形成类别词。专业定义的羟基不一定都属于严格醇类的那种连接环境。',Di,
 'a diol molecule 二醇分子，a diol group of compounds 二醇类化合物；系统名称还会标明骨架、羟基位置。',
 'a diol molecule；a diol compound。',
 'diol 数分子结构中的羟基，不是数杯数或不同物质的种数；glycol 常作为某类二元醇名称，范围定义要看文献。',
 ('The diagram shows a diol with two hydroxy groups.','图中是一种带两个羟基的二醇。'),('The chemist selected a diol for the polymer study.','化学家为聚合物研究选用了一种二醇。'),sources=['https://en.wiktionary.org/wiki/diol#English','https://goldbook.iupac.org/terms/view/D01748/pdf'])
Th=[['thio- 硫 + -ol 醇的命名形式','用硫对应氧的结构类比'],['thiol','R—SH 类型的有机化合物，中文硫醇']]
W('thiol','英 /ˈθaɪɒl/；美 /ˈθaɪɔːl/','硫醇',
 '普通醇的图里常看到 —OH；硫醇对应看 —SH，像把那个位置的氧换成硫。thio- 就把硫这条线说出来了。',
 'thio- 硫 + -ol，形成与醇作结构类比的名称。类别通常写作 R—SH，其中 R 不是单独一个氢；不是所有含硫物质都叫 thiol。',Th,
 'a thiol compound 硫醇化合物，a thiol group 硫醇相关官能团，thiol chemistry 硫醇化学。具体物质仍由完整名称确定。',
 'a thiol compound；a thiol group。',
 'thio- 让类别转到硫的对应结构，不能只看词尾 -ol 就认定一定是 —OH；词中 th 读 /θ/。',
 ('The molecule contains a thiol group.','这个分子含有硫醇官能团。'),('The experiment compared two thiol compounds.','实验比较了两种硫醇化合物。'),sources=['https://en.wiktionary.org/wiki/thiol#English','https://goldbook.iupac.org/terms/view/T06359/pdf'])
R('A1912','化学名称中的醇、羟基线索，也要看完整组合','-OL：认出结构线索，再看碳骨架、数量和其他前项','methanol、ethanol；glycol、diol、glycerol；menthol、retinol、cortisol；thiol 另看硫的对应。',
 '这里的词尾帮助读名称，不让所有词变成同一种酒精。di- 可数两个羟基，thio- 则把结构类比引到硫；复杂保留名称仍须按整词识别。',
 '-ol 从 alcohol 的末段形成化学命名后缀；meth-、eth- 联系碳骨架系列，di- 两，thio- 硫。',
 [['基础醇与羟基数量','methanol · ethanol · glycol · diol · glycerol'],['常见复杂保留名称','menthol · retinol · cortisol'],['硫的对应结构','thiol']],
 '带 -ol 不表示可饮用；thiol 看 —SH；glycol 与 diol 的类别范围有细分；gasoline 不按本后缀解释成某种醇。',
 'The report distinguishes methanol, ethanol and several diols.\n\n报告区分甲醇、乙醇及几种二醇。','methanol ethanol glycol diol glycerol menthol retinol cortisol thiol')
ROOTS[-1]['exclude']['gasoline']='汽油名称及其历史构成另见该词，不以醇类 -ol 后缀归为一种醇。'
if __name__=='__main__':save('continuation_20261030_lv',ROOTS,WORDS)
