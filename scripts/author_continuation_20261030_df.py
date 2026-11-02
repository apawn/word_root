"""Tea, jointed and limits; modern analysis distinguished from borrowing history."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
T=[['闽南语 茶 tê → 荷兰语 thee 等贸易传播路径','茶叶、茶饮的名称随商品传播'],['英语 tea，早有 tay、tey 等写法 → 现代 /tiː/','茶叶、茶饮；也可说一餐、一次茶点']]
W('tea','/tiː/','茶、茶叶、茶饮；茶点或一餐〔部分英式用法〕',
 '先是一种叶子和泡出的饮料，后来把喝茶时吃东西的那一餐也叫 tea；所以 What time is tea? 不一定只问何时端杯茶。',
 '现代形式主要经荷兰语 thee 接闽南语 茶 tê，传播中也涉及马来语 teh 等贸易接触。英语早期另有 cha 等形式，不能硬说全世界海路必是 te、陆路必是 cha。',T,
 'a cup of tea 一杯茶，tea leaves 茶叶，green tea 绿茶，herbal tea 花草浸泡饮品，have tea 喝茶或吃茶点、一餐，按地区和语境。',
 'a cup of tea；tea leaves；green tea；have tea；not my cup of tea。',
 'tea 泛用于饮品时包含 herbal tea，不都来自茶树；not my cup of tea 是不合我兴趣。spill the tea 八卦俚语有自己的传播背景，不只凭喝茶场景就认定来源。',
 ('Would you like a cup of tea?','你想喝杯茶吗？'),('Horror films are not really my cup of tea.','恐怖电影不太合我的兴趣。'),
 sources=['https://en.wiktionary.org/wiki/tea#English','https://www.etymonline.com/word/tea'])
W('teaspoon','/ˈtiːspuːn/','茶匙、小勺；一茶匙的量',
 '原来与茶杯配套的小勺，后来也当食谱里的小份量名称；说 teaspoon of sugar 时，重点是这么一份糖。',
 'tea + spoon 勺，按用途合成器具名，再借容器说其中的量。不是 tea 变音变成 spoon。',T[:1]+[['tea + spoon → teaspoon','茶用小勺 → 一茶匙的量']],
 'a teaspoon of sugar 一茶匙糖，stir with a teaspoon 用小勺搅，a level teaspoon 平平一茶匙。缩写常见 tsp。',
 'a teaspoon of；a level teaspoon；stir with a teaspoon；tsp。',
 'teaspoon 通常比 tablespoon 小；日常家用勺大小可能不同，食谱计量看量勺和采用的标准，不能仅凭名字认定手边所有小勺容量一样。',
 ('Add a teaspoon of sugar to the tea.','往茶里加一茶匙糖。'),('She stirred the drink with a teaspoon.','她用茶匙搅了搅饮料。'))
W('teapot','英 /ˈtiːpɒt/；美 /ˈtiːpɑːt/','茶壶',
 '放茶叶和热水来泡茶、再把茶倒进杯子的壶。pot 是容器，tea 说明它主要装什么、做什么用。',
 'tea + pot，英语内部复合词。相应壶名以用途限定容器，不是喝茶这个动作的过去式。',T[:1]+[['tea + pot → teapot','泡茶、盛茶的壶']],
 'a ceramic teapot 陶瓷茶壶，a pot of tea 一壶茶，pour from the teapot 从茶壶倒茶。',
 'a ceramic teapot；a pot of tea；pour from the teapot。',
 'teapot 常泡茶、盛茶，kettle 常烧水；二者日常用途不同，不能所有水壶都译为 teapot。',
 ('She poured the hot water into the teapot.','她把热水倒进茶壶。'),('The teapot was too small for six cups.','这把茶壶太小，泡不够六杯。'))
R('B3404','茶及饮用器具、场所与时间','TEA：叶子随贸易而来，名字再进入餐桌上的组合','tea → teaspoon、teapot、teacup、teabag；teatime、teahouse、tearoom 分别接时间、场所。',
 '从闽南语 tê 经贸易路径看现代读音，不用拼写瞎拆。器具名看实际用途，teapot 泡茶，kettle 烧水。',
 '闽南语 茶 tê → 荷兰语 thee → tea；tea 与 spoon/pot/cup/bag/time/house/room 并列合成。',
 [['基础与餐桌器具','tea · teaspoon · teapot · teacup · teabag'],['时间、场所','teatime · teahouse · tearoom']],
 'teaspoon/tablespoon 小勺与大勺；teapot/kettle 茶壶与烧水壶；tea 可说一餐；贸易读音不能用海陆绝对二分。',
 'She put the teapot and two teacups on the table at teatime.\n\n茶点时间，她把茶壶和两个茶杯放在桌上。','tea teaspoon teapot teacup teabag teatime teahouse tearoom')
J=[['拉丁 iungere → iunctus → 法语 joint 等 → joint','连接 → 接合的、接合处'],['joint + -ed → jointed','带有关节、接点的；也可为动词分词']]
W('jointed','/ˈdʒɔɪntɪd/','有关节、接头的；接合的；〔肉等〕切开成块的',
 '不是从头到尾一整根死硬杆，而是一段段接起来，可有活动关节；玩偶、机械臂、动物肢体都可这样描述。',
 '形容词 joint 接点 + -ed，表示具有这些接点；同形也可来自动词 joint 的过去式、过去分词，表示接合或按关节切分。',J,
 'jointed limbs 分节肢体，a jointed doll 有活动关节的玩偶，a jointed arm 有关节的臂。',
 'jointed limbs；a jointed doll；a jointed arm。',
 'jointed 有接点，joint 形容共同的、jointly 共同地；a jointed project 不能代替 a joint project 合作项目。',
 ('The doll has jointed arms and legs.','玩偶的手臂和腿都有关节。'),('The lamp has a jointed arm that bends easily.','这盏灯有能灵活弯动的关节灯臂。'))
R('B3906','相接、共同与有关节的','JOINT：连接点也能连接共同参与的人','joint → jointly；jointed 单列为具有接点的形状、结构。',
 '关节、连接处是看得见的接合；共同账户是几个人连在同一件事上。jointed 则不是共同地的新副词。',
 '拉丁 iunctus 经法语进入 joint；joint + -ly/-ed；不把 joint 末尾 t 当作现代英语过去式标记。',
 [['接点与共同参与','joint · jointly'],['具有接点的结构','jointed']],
 'joint account 共同账户，jointed arm 有接头的臂；jointly 是一起做，不是关节结构。',
 'The engineers jointly designed a jointed arm.\n\n工程师们共同设计了一只有关节的机械臂。','joint jointly jointed')
L=[['拉丁 līmes、līmit- → 古法语 limite → 中古英语 limit','田地间边界等 → 界限'],['拉丁 līmitāre → 法语 limiter → 英语 limit〔动词〕','划界、限定 → 使不超过某范围']]
def LH(f,m):return L+[[f,m]]
W('limit','/ˈlɪmɪt/','界限、限额；限制',
 '这里画一道线：走到、花到、做到这里就不能再过了。可以是外部规则，也可以是能力、资源到头。',
 '名词经法语接拉丁 līmes 的词干 līmit-，早期与边界有关；动词有拉丁 līmitāre、法语 limiter 的借入路径，不是一律现代英语名词临时转用。',L,
 'a speed limit 限速，a time limit 时限，within limits 在限度内，limit something to 把某物限于，push the limits 挑战极限。',
 'a speed limit；a time limit；within limits；limit something to。',
 'limit 可说界限、最高限额，limitation 更常说限制条件、局限；minimum 是最低值，不能把所有 limit 都默认最低或最高，须看限定。',
 ('The form has a limit of five hundred words.','这份表格最多填写五百字。'),('We limited the discussion to three topics.','我们把讨论限定在三个话题内。'))
W('limited','/ˈlɪmɪtɪd/','有限的、受限制的；限定的',
 '能用的时间、钱、位置只到这里，没有无限往外延伸；也可说特意只提供一部分。',
 'limit + -ed，动词过去分词发展为常见形容词。limit 末音 /t/，-ed 读 /ɪd/，不是只读成末尾一个 d。',LH('limit + -ed → limited','受到范围、数量限制的'),
 'limited time 时间有限，limited resources 资源有限，a limited edition 限量版，limited access 有限访问权限。',
 'limited time；limited resources；a limited edition；limited access。',
 'limited 数量、范围受限，不自动等于 useless 无用；limited edition 是限制发行量，不保证一定昂贵、质量更高。',
 ('We have limited time to finish the report.','我们完成报告的时间有限。'),('The service is available only in a limited area.','这项服务只在有限地区提供。'))
W('limiting','/ˈlɪmɪtɪŋ/','限制的、构成制约的；正在限制',
 '很多事情都备好了，却有一个条件卡住你，让你做不到更多；这就是 a limiting factor。',
 'limit + -ing，既可作动词分词，也常作形容词表示限制作用。末尾 t 不双写，因为这个双音节词重音在前。',LH('limit + -ing → limiting','在限制；起制约作用的'),
 'a limiting factor 制约因素，limiting beliefs 束缚自己的信念，limiting access 正在限制访问。',
 'a limiting factor；a limiting condition；limiting access。',
 'limited 已受到限制的，limiting 产生限制的；limited resources 资源少，a limiting resource 是卡住进展的资源条件。',
 ('Cost was the main limiting factor.','成本是主要制约因素。'),('The team is limiting access while repairs are underway.','维修进行期间，团队正在限制访问。'))
W('unlimited','/ʌnˈlɪmɪtɪd/','不受限制的、无限的',
 '原来那道数量、次数的上限不再设定；但广告里的无限往往针对某一项，不是所有使用条件都消失。',
 'un- 否定 + limited，形成不受限制的形容词。与动词逆转前缀不同，这里直接否定有限状态。',LH('un- + limited → unlimited','不受相应限制的'),
 'unlimited access 不限次数等的访问，unlimited possibilities 无限可能，unlimited data 不限量数据，具体服务范围看实际条款。',
 'unlimited access；unlimited possibilities；unlimited data。',
 'unlimited 常在指定维度说无限；limitless 也可比喻无穷，不能把一个广告词理解成绝无任何边界。',
 ('Members have unlimited access to the archive.','会员可以不限次数地查阅档案。'),('A child’s imagination can seem unlimited.','孩子的想象力有时仿佛无穷无尽。'))
W('limitation','/ˌlɪmɪˈteɪʃən/','限制、限制条件；局限、短处',
 '你能做到这里、做不到那里，那个卡住范围的条件就是 limitation；说人的、工具的 limitations，常是各自做不到的地方。',
 '经法语 limitacion、拉丁 līmitātiō 等接限制的动作名词；现代可对应 limit + -ation，但名词有独立借入史，不当成英语动词后来才生出来的唯一后代。',LH('拉丁 līmitātiō → 法语 limitacion → limitation','限制行为、条件；能力上的局限'),
 'a limitation of the method 方法的局限，time limitations 时间限制，recognize your limitations 认识自己的局限。',
 'a limitation of；time limitations；recognize your limitations。',
 'limit 常指边界、上限，limitation 可指造成边界的条件或短板。limitations 不一定是犯错，而是适用范围有限。',
 ('The study has several important limitations.','这项研究有几个重要局限。'),('We discussed the limitations of the new design.','我们讨论了新设计的局限。'),
 sources=['https://en.wiktionary.org/wiki/limitation#English','https://www.etymonline.com/word/limitation'])
W('limitless','/ˈlɪmɪtləs/','无穷的、没有界限的',
 '像眼前看不到边界一样，机会、耐心、空间显得多得没有尽头；常带形象、夸张表达。',
 'limit + -less 没有，构成无界限的形容词，不是副词后缀 -ly。',LH('limit + -less → limitless','没有可见界限、限制的'),
 'limitless possibilities 无限可能，limitless energy 无穷精力，seem limitless 看起来没有尽头。',
 'limitless possibilities；limitless energy；seem limitless。',
 'limitless 和 unlimited 常接近；limitless energy 常形容仿佛用不完，unlimited access 更像指定项目没有设限，区别不是绝对规则。',
 ('The project seemed full of limitless possibilities.','这个项目仿佛充满了无限可能。'),('The children appeared to have limitless energy.','孩子们看起来有用不完的精力。'))
W('limiter','英 /ˈlɪmɪtə/；美 /ˈlɪmɪtər/','限制器、限幅器；起限制作用的东西',
 '让速度、音量等到了某条线就压住、不再超过的装置或功能；-er 在这里常是东西，不是专门管限制的人。',
 'limit + -er，表示施加限制的装置、因素。电子、机械、软件语境可有不同具体对象。',LH('limit + -er → limiter','把某个量控制在限度内的装置'),
 'a speed limiter 限速器，an audio limiter 音频限幅器，adjust the limiter 调整限制器。',
 'a speed limiter；an audio limiter；adjust the limiter。',
 'limiter 是起限制作用的装置，limit 是边界、阈值；音频 limiter 与一般 compressor 功能相关，不凭词根就认定参数与行为完全相同。',
 ('The vehicle has a speed limiter.','这辆车有限速器。'),('The engineer adjusted the audio limiter before recording.','工程师在录音前调整了音频限幅器。'))
W('lintel','/ˈlɪntəl/','过梁、门楣或窗上方的横梁',
 '门窗洞口上面横跨过去、承住上方结构的那根梁，位置在头顶，不是脚下的门槛。',
 '中古英语 lyntel 接古法语 lintel。更早通常联系拉丁边界、门槛词，涉及重建形式与 līmen 等的影响，具体中间路线有不同分析；不硬拆成现代 limit 删 m 加 el。',
 [['古法语 lintel → 中古英语 lyntel → lintel','门、窗洞口上方横梁'],['更早拉丁边界、门槛词联系：路线有争议','与 līmes、līmen 等有关的分析，不能强定唯一链']],
 'a stone lintel 石过梁，above the doorway 在门洞上方，a carved lintel 雕刻门楣。',
 'a stone lintel；a carved lintel；the lintel above the doorway。',
 'lintel 在洞口上方，sill/threshold 常在下方；limit 的边界意象有历史联系分析，不意味着两词现代构词可随意互换。',
 ('A heavy stone lintel spans the doorway.','一根厚重的石过梁横跨门洞。'),('The date was carved into the lintel above the entrance.','日期刻在入口上方的门楣上。'),
 sources=['https://en.wiktionary.org/wiki/lintel#English','https://www.etymonline.com/word/lintel'])
R('B3923','界限、被限制与取消限制；门窗横梁旁支','LIMIT：画出的边线，变成数量、能力和用途的范围','limit → limited、limiting、unlimited；limitation、limitless、limiter 分过程、无界限和器具；lintel 以谨慎历史旁支另列。',
 'limited 是受限状态，limiting 是造成限制。名词 limitation 有独立法语、拉丁路径；lintel 不靠现代字母删改来冒充已证实历史。',
 '拉丁 līmes、līmit- → limit；līmitātiō → limitation；limit + -ed/-ing/-less/-er；un- + limited；lintel 的古法语近源可靠、深源分析不一。',
 [['界限与状态、作用','limit · limited · limiting · unlimited'],['过程、性质与器具','limitation · limitless · limiter'],['建筑名词历史旁支','lintel']],
 'limited/limiting 受限与制约；limit/limitation 边界与限制条件；limiter 不是只有人物；lintel 上横梁非下门槛。',
 'Limited space was the main limiting factor in the design.\n\n空间有限是设计中的主要制约因素。','limit limited limiting unlimited limitation limitless limiter lintel')
if __name__=='__main__':save('continuation_20261030_df',ROOTS,WORDS)
