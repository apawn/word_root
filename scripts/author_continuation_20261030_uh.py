"""Representative pieces, temporary support, grass cutting, and keeping too much."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'C0369':dict(words=['example','sample','sampler'],label='example 与 sample：拿出一部分给人看',note='sample 与 example 共同接拉丁 exemplum 等材料，经法语、中古英语发生缩短等变化；不是现代 English example 随手删掉 ex- 的造词规则。sampler 较早已是样板、绣样，不能全部说成人。'),
 'A1741':dict(words=['scaffold','scaffolding','hoard','hoarding'],label='scaffolding 与 hoarding：固定名词和动作名词',note='scaffolding 常统称脚手架、临时支持体系；hoarding 囤积接 hoard。英式围挡、广告牌 hoarding 另接旧 hoard 木围构筑物材料，不能说由囤东西产生。'),
 'A1697':dict(words=['mow','mower'],label='mow 与 mower：割草的人或机器',note='mower 的 -er 可指人，后来也常指机器；mow 保留割草、刈割的古英语词族。'),
}
W('sample','/ˈsɑːmpəl/〔英常见〕；/ˈsæmpəl/〔美常见〕','样品、样本；抽样；尝试、取样',
 '整块布太大，先拿一小片看看；整锅汤很多，先舀一点尝尝。sample 是拿出一部分，让人了解更多。',
 '与 example 同接拉丁 exemplum；经古法语 essample、盎格鲁法语 saumple 或中古英语相关缩短形式进入英语。后来重点落在代表整体的小部分，动词再表取样、尝试。',
 [['拉丁 exemplum → 法语／中古英语相关形式','例子、样本；缩短等形成 sample'],['现代 sample 名词与动词','代表整体的一部分；取样、试尝']],
 'a free sample 免费试用品；a blood sample 血液样本；a random sample 随机样本；sample the local food 尝尝当地食物。',
 'take a sample；a sample of the material。','example 常说举出的例子，sample 常说从整体中取出的样品、样本。一个样本是否代表整体，要看取样方式，单凭 sample 一词并不保证。',
 ('The shop gave us a small sample of the cheese.','商店给了我们一小块奶酪试吃。'),('The researchers collected a sample of water from the river.','研究人员从河里采集了一份水样。'),sources=['https://www.etymonline.com/word/sample','https://en.wiktionary.org/wiki/sample#English'])
W('sampler','英 /ˈsɑːmplə/；美 /ˈsæmplər/','样品组合、选集；取样者或取样设备；绣样',
 '每种茶各放一点，凑成一盒让人试，是 tea sampler；把几段声音录下来再播放、加工的设备，也叫 sampler。',
 '对应 sample + -er，但历史上早有样板、可仿照的式样，后来有绣样、样品集合等。取样的人、器具又按现代 sample 动词发挥 -er 用法；各义不能只译成某个人。',
 [['较早 sample 相关材料 → sampler','样板、供仿照的绣样等'],['现代 sampler 的多条固定用法','样品集合；取样的人或设备、音乐采样器']],
 'a tea sampler 茶叶试饮组合；a music sampler 音乐选辑或采样设备，按场景判断；an embroidery sampler 刺绣样片；a water sampler 水样采集器。',
 'a sampler of local food；an electronic sampler。','sample 是一份样本，sampler 可是供试的组合，也可指采样器。-er 在这里不能只记成“人”，要看被命名的具体物件。',
 ('The gift box contains a sampler of six different teas.','礼盒里装着六种不同茶叶的试饮组合。'),('The musician recorded the sound into a sampler.','音乐人把那段声音录进了采样器。'),('The museum displayed an old embroidery sampler.','博物馆展出了一块旧刺绣样片。'),sources=['https://www.etymonline.com/word/sampler','https://en.wiktionary.org/wiki/sampler#English'])
W('scaffold','英 /ˈskæfəʊld/；美 /ˈskæfoʊld/','脚手架、临时支撑架；高台；搭支架',
 '修墙时，先在外侧搭个能站人、放工具的架子，帮工人够到高处。这是 scaffold 的核心实物画面。',
 '经古北法语、古法语 eschafaut 等平台、支架词借入；通常上溯重构的通俗拉丁 *catafalicum 等材料，但部分改形路径有不确定性。现代英语不宜靠字面硬拆各音节。',
 [['法语 eschafaut 等；更早路径含重构材料','高台、临时支撑架'],['英语 scaffold','施工支架；平台；比喻提供结构支持']],
 'a scaffold around the building 楼外脚手架；a wooden scaffold 木制高架；scaffold a task 为任务提供分步支持。历史叙述中也可指刑台。',
 'put up a scaffold；a temporary scaffold。','scaffold 可数，说一座支架；scaffolding 常统称整个支架体系或材料。用作比喻时，抓住先搭支持、让事情够得着的画面。',
 ('Workers stood on a scaffold beside the wall.','工人站在墙边的脚手架上。'),('The tutor used questions to scaffold the discussion.','辅导老师用一连串问题为讨论搭起思路支架。'),sources=['https://www.etymonline.com/word/scaffold','https://en.wiktionary.org/wiki/scaffold#English'])
W('scaffolding','英 /ˈskæfəʊldɪŋ/；美 /ˈskæfoʊldɪŋ/','脚手架体系、脚手架材料；临时支持框架',
 '架子把人托到暂时够不着的地方。学习时，提示、示范、分步骤也像临时脚手架，帮助人逐渐独立完成。',
 '与 scaffold 同属法语借词支架、平台词族，现代可对应 scaffold + -ing；脚手架的名词用法很早已有。后来又把临时支撑比喻用于学习、写作、系统等。',
 [['法语支架材料 → scaffold／scaffolding','临时高架及支架体系'],['现代比喻 scaffolding','为学习或建设过程提供结构支持']],
 'covered in scaffolding 外面搭满脚手架；erect scaffolding 搭脚手架；learning scaffolding 学习支架、阶段性支持。常作不可数统称。',
 'remove the scaffolding；temporary scaffolding。','some scaffolding 指一套或一些支架材料；a scaffold 可指一座具体架子。教育比喻中的支架，重点是先提供结构帮助。',
 ('The building was covered in scaffolding.','那栋楼外面搭满了脚手架。'),('The worksheet provides scaffolding for students writing their first essay.','练习纸为第一次写作文的学生提供分步支持。'),sources=['https://www.etymonline.com/word/scaffolding','https://en.wiktionary.org/wiki/scaffolding#English'])
W('mow','英 /məʊ/；美 /moʊ/','割草；刈割作物',
 '把一片草的顶部割下来，让地面变整齐，就是 mow。它关注成片割过，不只是剪掉单独一根枝条。',
 '接古英语 mawan，用镰刀等割草、谷物；属于古老割草词族。现代过去式 mowed，过去分词 mowed 或 mown，保留不同历史形式。',
 [['古英语 mawan → 中古英语相关形式','用刃具割下草、作物'],['现代 mow、mowed、mown／mowed','割草；现代机器也执行此动作']],
 'mow the lawn 修剪草坪；mow the grass 割草；freshly mown grass 新割过的草。mow down 还能比喻一下扫倒、击倒，需按上下文理解。',
 'mow regularly；the lawn needs mowing。','mow 多说成片草地、作物的割切；trim 可说修整边缘、枝条等。注意动词 mow 的常见读音与 go 押韵。',
 ('I need to mow the lawn this weekend.','我这周末需要修剪草坪。'),('The field had been freshly mown.','那片地刚刚割过草。'),sources=['https://www.etymonline.com/word/mow','https://en.wiktionary.org/wiki/mow#English'])
W('mower','英 /ˈməʊə/；美 /ˈmoʊər/','割草机；割草的人',
 '以前是挥镰刀割草的人，后来机器接手了这个动作，名字也能落到机器上。日常说 the mower 多半是割草机。',
 'mow + -er，较早指割草的人；机械割草设备出现后，同一动作执行者词尾也用于机器。',
 [['mow + -er → mower','执行割草动作的人'],['机械化之后的常见用法','割草机；lawn mower 是草坪割草机']],
 'a lawn mower 草坪割草机；an electric mower 电动割草机；a ride-on mower 乘坐式割草机。',
 'push the mower；start the mower。','mower 的 -er 不保证一定指人；机器名里同样常见。mower 的发音随 mow 走，别读成 mouse 的 /maʊ/。',
 ('He pushed the mower across the lawn.','他推着割草机穿过草坪。'),('Our electric mower is much quieter than the old one.','我们的电动割草机比旧机器安静得多。'),sources=['https://www.etymonline.com/word/mower','https://en.wiktionary.org/wiki/mower#English'])
W('hoard','英 /hɔːd/；美 /hɔːrd/','囤积、珍藏；储藏的一批物品',
 '把东西一件件收起来留着，常带不想放手、还要继续积攒的感觉；藏起来的一批硬币也可叫 a hoard。',
 '名词接古英语 hord 宝藏、珍贵储备；动词接同族 hordian 收集存放。更远材料与遮藏的词根相连，现代可说珍藏，也可带过度囤积的批评意味。',
 [['古英语 hord、hordian','宝藏、储备；收集并存放'],['现代 hoard 名词、动词','储藏的一批；囤积、珍藏']],
 'hoard food 囤积食物；hoard old magazines 舍不得丢旧杂志而大量积存；a hoard of coins 一批窖藏硬币；hoard information 把信息攥在手里。',
 'a secret hoard；hoard things for later。','hoard 与 horde 常同音。hoard 是囤积或储藏物，horde 是一大群人等；a hoard of coins 与 a horde of tourists 不能混拼。',
 ('Archaeologists found a hoard of silver coins.','考古学家发现了一批窖藏银币。'),('He tends to hoard old notebooks instead of throwing them away.','他总爱把旧笔记本攒着，不舍得扔。'),sources=['https://www.etymonline.com/word/hoard','https://en.wiktionary.org/wiki/hoard#English'])
W('hoarding','英 /ˈhɔːdɪŋ/；美 /ˈhɔːrdɪŋ/','囤积；另源英式名词：工地围挡、广告牌',
 'hoarding food 是把食物囤起来；a hoarding beside the road 却可能是路边广告牌。同形词需要按是否在说动作、具体构筑物来分。',
 '囤积义是 hoard + -ing，接古英语 hord 宝藏词族。围挡、广告牌义另接旧 hoard 木围、支架等，与法语 hourd 等构筑物材料有关，不能从存东西推出所有义项。',
 [['hoard 储藏 + -ing → hoarding','囤积行为、正在囤积'],['另一旧 hoard〔木围构筑物〕→ hoarding','英式围挡、用于展示广告的大牌面']],
 'food hoarding 囤积食品；hoarding old papers 囤积旧纸张；a construction hoarding 施工围挡；an advertising hoarding 广告牌。',
 'hoarding supplies；a large roadside hoarding。','囤积这一过程通常不可数；广告牌、围挡可以说 a hoarding、several hoardings。冠词和复数能帮你辨别两条来源。',
 ('She was hoarding cardboard boxes for the move.','她在为搬家攒纸箱。'),('A large advertising hoarding stood beside the road.','路边立着一块大广告牌。'),sources=['https://www.etymonline.com/word/hoard','https://en.wiktionary.org/wiki/hoarding#English'])
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_uh',ROOTS,WORDS)
 extend_lessons()
