"""Broad and link: spatial breadth and connected parts."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
BR=[['古英语 brād → 中古英语 brood → broad','宽、开阔；更早来源未定'],['现代 broad','宽阔 → 范围广；粗略、概括']]
def BH(f,m):return BR+[[f,m]]
W('broad','/brɔːd/','宽阔的；广泛的；概括的',
 '一条路横向很宽，一门知识覆盖很多方面，一份概览只画大轮廓；都是宽的不同侧面。',
 '继承古英语 brād，经中古英语延续。范围、思路、轮廓等抽象义与空间宽度相连；更远来源不作定论。',BR,
 'broad shoulders 宽肩，a broad range 广泛范围，a broad overview 概览，in broad daylight 光天化日。',
 'a broad range；broad shoulders；a broad overview；in broad terms。',
 'broad 与 wide 许多场景重合，但固定搭配要学；a broad overview 不是精确列出所有细节。',
 ('The course covers a broad range of topics.','课程涵盖广泛主题。'),('She gave us a broad overview of the plan.','她给我们概括介绍了方案。'))
W('breadth','/bredθ/','宽度；广度、丰富范围',
 '从左到右有多宽，或知识、经验横跨多少方面。',
 '接古英语 brǣdu 的旧宽度名词，经中古英语 brede、bredthe，后来受 length 等 -th 名词影响。现代可联系 broad + -th，元音变化是历史结果。',BR[:1]+[['古英语 brǣdu → 中古英语 brede／bredthe → breadth','宽阔的性质 → 宽度、范围广度']],
 'the breadth of the river 河流宽度，breadth of experience 经验广度，breadth and depth 广度与深度。',
 'breadth of experience；breadth and depth；the breadth of a range。',
 'breadth 宽度、广度，breath 呼吸，少一个 d 就是另一词；depth 深度不等于覆盖方面多。',
 ('The project impressed us with its breadth and depth.','项目的广度和深度令我们印象深刻。'),('Her experience gives her an unusual breadth of knowledge.','她的经历让她拥有非同寻常的知识广度。'),sources=['https://www.etymonline.com/word/breadth','https://en.wiktionary.org/wiki/breadth#English'])
W('broaden','/ˈbrɔːdən/','扩大；拓宽；变宽',
 '把原先窄的范围往两边推开，可以是路，也可以是眼界、经验或调查范围。',
 'broad + -en，-en 表变得、使变得。这个词末 d 后不是过去式，整个 -en 在造新动词。',BH('broad + -en → broaden','使变宽、范围扩大'),
 'broaden your horizons 开阔眼界，broaden the search 扩大搜寻，broaden access 扩大可获得、可使用范围。',
 'broaden your horizons；broaden the search；broaden the scope。',
 'broad 是宽的状态，broaden 是变宽的动作；board 木板、登船是另词，不能漏掉 broad 的 r 后元音关系。',
 ('Travel can broaden your horizons.','旅行可以开阔眼界。'),('The team broadened the search to nearby towns.','团队把搜寻范围扩大到附近城镇。'))
W('broadly','/ˈbrɔːdli/','广泛地；大体上、概括地',
 '覆盖面铺得很开；讨论意见时，又表示看大方向，不计每个小细节。',
 'broad + -ly，既保留宽泛方式义，也形成 broadly speaking 概括来说等固定用法。',BH('broad + -ly → broadly','广泛地 → 大体上、概括地'),
 'broadly speaking 概括而言，broadly agree 大体同意，broadly similar 大体相似。',
 'broadly speaking；broadly agree；broadly similar。',
 'broadly agree 不等于完全每点都赞同；exactly 精确地强调细节一致，方向不同。',
 ('Broadly speaking, the two plans are similar.','大体说来，两项方案相似。'),('We broadly agree on the goals but differ on the details.','我们在目标上大体同意，但细节有分歧。'))
W('abroad','/əˈbrɔːd/','在国外；到国外；广为流传〔部分旧式用法〕',
 '从家里走到外面、远处，最后常用义扩大成走出本国的范围。',
 '中古英语 on brode、abrood，上接古英语 on brede，a- 这里接 on 的弱化。旧义有广散、在外，后来常指国外。不是不定冠词 a 加一个宽阔物。',BR[:1]+[['古英语 on brede → 中古英语 abrood','广开、散在外 → 在外、离家'],['英语 abroad','在国外、到国外']],
 'study abroad 留学，travel abroad 出国旅行，live abroad 住在国外。通常作副词，go abroad 不再加 to。',
 'study abroad；go abroad；live abroad；from abroad。',
 'abroad 国外，aboard 在船、飞机等交通工具上；拼写只差位置，句子场景不同。',
 ('She plans to study abroad next year.','她计划明年出国留学。'),('We received several applications from abroad.','我们收到了几份来自国外的申请。'),sources=['https://www.etymonline.com/word/abroad','https://en.wiktionary.org/wiki/abroad#English'])
W('broadband','/ˈbrɔːdbænd/','宽带；宽频带的',
 '技术上用较宽的一段频带传信号，日常最常指宽带网络接入。',
 'broad 宽 + band 频带，band 用带状范围作比喻。通信词后来成为家庭、办公室网络服务的通称。',BH('broad + band〔频带〕→ broadband','宽频带传输 → 宽带接入'),
 'broadband access 宽带接入，a broadband connection 宽带连接，broadband speed 宽带速度。不同技术、套餐能力要具体看。',
 'broadband access；a broadband connection；broadband speed。',
 'broadband 宽带不等于 Wi-Fi；前者常说接入服务或传输，后者是本地无线连接方式。bandwidth 带宽是相关度量词。',
 ('The village now has broadband access.','村庄现在接入了宽带。'),('Our broadband connection stopped working this morning.','今天早上我们的宽带连接断了。'))
W('broadsheet','/ˈbrɔːdʃiːt/','大幅纸张；大开张报纸；严肃报纸〔延伸用法〕',
 '展开是一大张纸，报业里常与小开张的 tabloid 相对；后来也可借来形容偏严肃的新闻风格。',
 'broad 宽 + sheet 纸张，从纸张尺寸、报纸版式发展出报纸类型的说法。版式与内容风格不能严格画等号。',BH('broad + sheet → broadsheet','大幅纸张 → 大开张报纸及相关风格称呼'),
 'a broadsheet newspaper 大开张报纸，a broadsheet format 大开张版式。即使报纸后来换版式，传统类别称呼也可能保留。',
 'a broadsheet newspaper；a broadsheet format；read a broadsheet。',
 'broadsheet 不是保证所有报道高质量的标签；tabloid 也既有尺寸义又有风格义，具体报道还得单独看。',
 ('He unfolded the broadsheet across the table.','他把大开张报纸铺展在桌上。'),('The article compares broadsheet and tabloid news styles.','文章比较大报与小报的新闻风格。'))
R('B3075','宽、广度、拓宽与国外、宽带','BROAD：横向宽，抽象范围也能宽','broad → breadth、broaden、broadly；abroad 讲在外到国外，broadband、broadsheet 说明后部。',
 '本族宽词，breadth 经旧名词改形，abroad 的 a- 接 on 的弱化。broadcast 已精讲，撒播到广播可一起复习。',
 'broad → breadth〔旧名词改形〕、broaden、broadly；on broad → abroad；broad + band/sheet/cast。',
 [['宽与广度、变化、方式','broad · breadth · broaden · broadly'],['国外与现代复合','abroad · broadband · broadsheet · broadcast · broadside']],
 'breadth 广度与 breath 呼吸分；abroad 国外与 aboard 登乘分；broadband 不等于 Wi-Fi。',
 'Studying abroad broadened her experience and the breadth of her knowledge.\n\n留学拓展了她的经历和知识广度。',
 'broad breadth broaden broadly abroad broadband broadsheet broadcast broadside')
LI=[['中古英语 linke、lenke','链环；可能有斯堪的纳维亚来源，旧本族联系亦有讨论'],['现代 link','连接的一环 → 联系、链路、网页链接；连接动作']]
def LH(f,m):return LI+[[f,m]]
W('link','/lɪŋk/','链环；联系、连接；网页链接',
 '一只金属环扣住下一只，就成了链；人与事件、网页与网页之间也能这样接起来。',
 '中古英语链环词，常联系斯堪的纳维亚来源，细节有讨论。连接动词与名词紧密相关，现代网站链接是新场景。',LI,
 'a link in a chain 链中的一环，a link between events 事件之间的联系，click a link 点链接，link A to B 把两者连接。',
 'a link between；link A to B；click a link；a weak link。',
 'a link between 两事有关联，不必证明因果。高尔夫 links、旧火把 link 等另有历史，不按网页链接强行合并。',
 ('The article includes a link to the original report.','文章有原始报告的链接。'),('The bridge links the two sides of the valley.','桥把山谷两侧连接起来。'),sources=['https://www.etymonline.com/word/link','https://en.wiktionary.org/wiki/link#English'])
W('linkage','/ˈlɪŋkɪdʒ/','联系、关联；连接机构、联动装置',
 '不是只盯一条线，而是看几个部分怎样连起来、相互带动；机器里也可以是真实的连杆结构。',
 'link + -age，形成连接关系或连接装置的名词，末段读 /ɪdʒ/。',LH('link + -age → linkage','连接关系；由连接件构成的机构'),
 'linkage between two factors 两因素的联系，a mechanical linkage 机械联动机构。遗传等学科还可能有专门定义。',
 'linkage between；a mechanical linkage；strengthen linkages。',
 'link 常具体一环、一条连接，linkage 侧重连接关系或结构整体；两者有重合，不只按长短判断正式程度。',
 ('The study explores the linkage between transport and employment.','研究探讨交通与就业之间的联系。'),('The handle operates a simple mechanical linkage.','手柄带动一个简单的机械联动机构。'))
W('linker','英 /ˈlɪŋkə/；美 /ˈlɪŋkər/','连接者、连接物；链接器〔编程〕',
 '把分开的部分接起来的主体；编程里，把编译后的片段及所需内容链接成程序等输出。',
 'link + -er，-er 可人也可工具。软件链接器是工具义的一种专门化。',LH('link + -er → linker','执行连接的主体 → 程序链接器等'),
 'a linker error 链接错误，the compiler and linker 编译器与链接器。语言学、化学等领域的 linker 也都需看具体对象。',
 'a linker error；the compiler and linker；a linker script。',
 'linker 不等于 browser 浏览器；一个参与程序构建，一个常用于打开网页，不能因都谈 link 就混。',
 ('The linker reported a missing symbol.','链接器报告缺少一个符号。'),('The build process runs the compiler before the linker.','构建过程先运行编译器，再运行链接器。'))
W('downlink','/ˈdaʊnlɪŋk/','下行链路；下行传输',
 '从卫星到地面，或从网络到用户，把这个方向叫下行；down 是系统中的相对方向。',
 'down- 下行 + link 链路，通信中与 uplink 上行配对。不是说传输电缆必须沿垂直方向。',LH('down- + link → downlink','从上层、远端系统到接收端的通信链路'),
 'a satellite downlink 卫星下行链路，downlink data 下行数据，downlink speed 下行速度。',
 'a satellite downlink；downlink data；downlink speed。',
 'downlink 下行链路与 download 下载相关但不完全同义；download 常指把文件等取到本地的动作。',
 ('The satellite downlink carries images to the ground station.','卫星下行链路把图像传到地面站。'),('The test measured uplink and downlink speeds.','测试测量了上行和下行速度。'))
W('permalink','英 /ˈpɜːməlɪŋk/；美 /ˈpɜːrməlɪŋk/','永久链接；指向单篇内容的稳定网址',
 '文章从首页往后翻走了，仍能用同一地址直接找到它；这种供长期引用的地址叫永久链接。',
 'perma- 来自 permanent 永久的缩短 + link，现代网络构词。perma- 不等于 per- 穿过再另加一个 m。',LH('perma〔permanent 缩短〕+ link → permalink','设计为稳定指向单篇内容的链接'),
 'copy the permalink 复制永久链接，a permalink to a post 某篇文章的永久链接。稳定是用途设计，不保证网站关闭后仍可访问。',
 'copy the permalink；a permalink to a post；a stable permalink。',
 'homepage 首页地址可能每次显示不同新内容；permalink 侧重直接指向一篇内容。页面删除或迁移后也可能失效。',
 ('Use the permalink when citing this post.','引用这篇文章时请用永久链接。'),('She copied the permalink into her notes.','她把永久链接复制进笔记。'))
R('B3202','链环、联系与数字、通信链路','LINK：一环扣一环，实体、关系和网址都能连接','link → linkage、linker；上下行 uplink/downlink 配对，permalink 接永久地址意图，其他网页链接共享。',
 '旧链环词发展为连接关系，现代软件、网络和通信赋予新对象。原来不同的同形词不能都从链环硬推。',
 'link + -age/-er；up-/down-/hyper-/back-/perma- + link；link + up。',
 [['基本连接与主体','link · linkage · linker'],['通信方向','uplink · downlink'],['网页与固定连接','hyperlink · backlink · permalink · linkup']],
 '联系不等于因果；linker 程序构建工具；downlink 不完全等于 download；permalink 是稳定地址设计而非永不失效。',
 'The permalink links directly to the report rather than the changing homepage.\n\n永久链接直接指向报告，而不是内容不断更新的首页。',
 'link linkage linker uplink downlink hyperlink backlink permalink linkup')
if __name__=='__main__':save('continuation_20261030_ah',ROOTS,WORDS)
