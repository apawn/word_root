"""Useful cultural nouns, degrees and extensions of recently explained families."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
def S(word,base):return ['https://en.wiktionary.org/wiki/'+word+'#English','https://www.etymonline.com/word/'+base]
EXISTING_ROOT_ADDITIONS={
 'C1641':dict(words='triumph triumphant triumphantly'.split(),label='triumph → triumphant → triumphantly：胜利和胜利的样子',note='triumphant 接拉丁 triumphans、triumphant- 现在分词材料，不是现代英语 triumphing 随意换尾；英语再接 -ly 表示带着胜利、得意的样子。'),
 'B2955':dict(words='guild guilds'.split(),label='guild：旧缴纳、共同出资材料到行会',note='与 pay 比较缴纳，不是 pay 派生。guild 融合古英语 gegield 共同体、gield 缴纳等义，又受北欧 gildi 影响；较远与 yield 的缴纳、回报旧词族有关，联系共同出资、互助团体。'),
 'C1379':dict(words='specialty specialties'.split(),label='specialty → specialties：独特之处到专长、特色产品',note='specialty 经古法语 especialte 等名词借入，较远接拉丁 specialis 的特殊、特有材料及名词后缀；不能一律当成现代英语 special 临时加 -ty。专门领域与拿手特色顺着特有之处理解。'),
 'B3019':dict(words='shawl shawls'.split(),label='shawl：另源的披肩名',note='与 cloth 比较织物，不是 cloth 派生。shawl 经乌尔都等南亚语言接波斯 shal，作为衣物名称借入；具体地名命名说并不确定。'),
 'B2688':dict(words='grove groves'.split(),label='grove：另源的小树林、成片树木',note='与 wood 比较林木，不由 wood 派生。grove 接古英语 graf 小树林，较远来源不明；不能因为开头接近 grow 就直接断为其现代名词化。'),
 'B2561':dict(words='abbey abbeys'.split(),label='abbey：院长名衍生的修道院名',note='与 church 比较宗教建筑，不由 church 派生。abbey 经法语、拉丁 abbatia，接 abbas 院长，较远经希腊接阿拉姆语 abba 父亲的尊称；不是现代英语 father 的直接派生。'),
 'B3570':dict(words='exile exiles exiled exiling'.split(),label='exile：被驱离故土的人、状态与动作',note='与 out 比较离开、在外，不由英语 out 派生。名动词经法语接拉丁 exilium、exul 及相关动词，ex- 向外较清楚，后部究竟接行走、驱赶或其他材料仍有争论。'),
 'C1237':dict(words='rude ruder rudest'.split(),label='rude → ruder → rudest：更粗鲁、最粗鲁',note='rude 接法语、拉丁 rudis 粗糙、未受训练，表面未修整到行为不文雅。去末尾 e 后分别接完整后缀 -er、-est，不把后缀截成 -r、-st。'),
 'B2616':dict(words='lad lads'.split(),label='lad：另源的小伙子、男孩',note='与 boy 比较年龄、称呼，不由 boy 派生。中古英语 ladde 有年轻男仆、地位较低男子等旧义，来源可能接北欧但不确定；后来年轻男子义常变得熟络、亲切。'),
}
TRIUMPHANT=[['拉丁 triumphus 凯旋、成功 → triumphare 庆祝胜利','现在分词 triumphans、triumphant-：获胜、庆胜的'],['英语 triumphant：胜利的、得意的','英语接 -ly → triumphantly，描述带着这种姿态行动']]
GUILD=[['古英语 gegield 团体 + gield 缴纳、贡献等义融合','又受北欧 gildi 团体等词形影响'],['共同出资、互助的组织 → 行会、同业团体','较远与 yield 的缴纳、回报旧词族有联系']]
SPECIALTY=[['拉丁 specialis 特别、特有 → 特性名词材料','古法语 especialte 等 → 英语 specialty'],['特有之处 → 专门领域、专长 → 特色产品、拿手菜','英式也常见 speciality，形成相关用法对照']]
SHAWL=[['波斯 shal → 乌尔都等南亚语言 → 英语 shawl','衣物名随语言接触借入，更远地名命名说不确定'],['英语 shawl：披在肩部、上身的织物','现代按一条、几条披肩计数']]
GROVE=[['古英语 graf：小树林、树丛 → 英语 grove','更远来源不明，不按现代 grow 去 e 再加 v 解释'],['一片树木 → 自然小林或成片栽种的树','olive grove、orange grove 等用于果树片区']]
ABBEY=[['阿拉姆语 abba 父亲的尊称 → 希腊、拉丁 abbas 院长','拉丁 abbatia：由院长所领的修道院'],['法语 abaïe、abbeie 等 → 英语 abbey','修道院；一些旧建筑即使功能变化仍保留历史名称']]
EXILE=[['拉丁 exul 被放逐者、exilium 放逐等及相关动词','ex- 向外；后半远源有行走、驱离等不同分析'],['经古法语 exil、essillier 等 → 英语 exile 名动词','被迫在故土之外的人、处境；以及放逐的动作']]
RUDE=[['拉丁 rudis 粗糙、未受训练 → 法语 ruide、英语 rude','未修整的表面 → 未经教养、失礼的行为'],['rude 去 e 后接 -er、-est → ruder、rudest','现代英语比较等级，形容词词义不变']]
LAD=[['中古英语 ladde：年轻男仆、较低地位男子等旧称','可能联系北欧语材料，具体来路不确定'],['英语 lad：男孩、年轻男子','现代常见熟络、亲切的称呼；有历史词义改善']]
W('triumphant','英、美 /traɪˈʌmfənt/','胜利的；洋洋得意的、充满胜利喜悦的',
 '终于解决难题，抬头露出“我做到了”的笑，是 a triumphant smile。这个词既可说真的胜利，也可说脸上、声音里的得意。',
 '接拉丁 triumphare 凯旋、庆胜的现在分词 triumphans、triumphant-，-ant 延续分词形容词材料；与 triumph 同族，有自己的借入历史。',TRIUMPHANT,
 'a triumphant return 是凯旋、成功归来；a triumphant smile 是胜利般的笑；sound triumphant 是听起来很得意。',
 'a triumphant return；a triumphant smile；a triumphant shout。',
 'triumph 常见重音在第一节；triumphant 常见重音移到第二节 /ʌm/。triumphant 的得意未必都让旁人愉快，要看语气。',
 ('She gave a triumphant smile when the code finally worked.','代码终于跑通时，她露出了胜利般的笑容。'),('The team made a triumphant return home.','球队凯旋回家。'),sources=S('triumphant','triumphant'))
W('triumphantly','英、美 /traɪˈʌmfəntli/','得意地；带着胜利喜悦地',
 '把完成的作品举起来，带着“看，我成功了”的神情，这个动作的样子就是 triumphantly。',
 'triumphant + -ly → triumphantly，形容词接副词后缀；保持 triumphant 的常见重音，不回到 triumph 的第一节。',TRIUMPHANT+[['triumphant + -ly → triumphantly','描述胜利、得意的行动姿态']],
 'smile triumphantly 是得意地笑；announce triumphantly 是带着胜利口气宣布；hold something up triumphantly 是得意地举起。',
 'smile triumphantly；announce triumphantly；wave triumphantly。',
 'triumphant 修饰人、笑容等名词或作表语；triumphantly 常修饰说、笑、举起等动作，不能只按中文都带“得意”就互换。',
 ('He held up the finished model triumphantly.','他得意地举起做好的模型。'),('“I found it,” she announced triumphantly.','“我找到了。”她得意地宣布。'),sources=S('triumphantly','triumphant'))
W('guild','英、美 /ɡɪld/','行会；同业公会；〔游戏〕公会',
 '做同一行的人聚成团体，缴费、互助、维护共同利益，就是理解 guild 的好画面。今天一些职业组织、游戏团队也沿用这个名称。',
 '古英语 gegield 团体与 gield 缴纳、贡献等义融合，又受北欧 gildi 影响。较远与 yield 的缴纳、回报词线有关，不能只按今天 yield 让步来猜组织。',GUILD,
 'a craft guild 是手工业行会；a writers’ guild 是作家公会；join a guild 可以说加入同业或游戏公会。',
 'a craft guild；a writers’ guild；join a guild。',
 'guild 与 trade union 都可能涉及共同利益，但历史和组织类型不同；游戏里的 guild 也不因此具有同业组织的全部制度。',
 ('The museum explains how a medieval craft guild worked.','博物馆介绍中世纪手工业行会怎样运作。'),('She joined a guild to play the game with friends.','她加入了一个公会，和朋友们一起玩游戏。'),sources=S('guild','guild'))
W('guilds','英、美 /ɡɪldz/','行会、公会〔复数〕',
 '不同手艺各有团体，木匠、织工、金匠的几个行会，就是 guilds。现代也能数几个职业公会或游戏公会。',
 'guild + -s → guilds，末尾 /d/ 后接 /z/；整个组织名形成可数复数。',GUILD+[['guild + -s → guilds','多个行会、公会；词尾 /ldz/']],
 'medieval guilds 是中世纪行会；craft guilds 是手工业行会；rival guilds 是相互竞争的公会。',
 'medieval guilds；craft guilds；rival guilds。',
 'guilds 与 gilds 镀金的动词形式同音；前者是组织，后者是表面处理动作，拼写和来源不同。',
 ('Several guilds helped fund the old town hall.','几个行会共同资助了这座旧市政厅。'),('The game allows guilds to compete in weekly events.','游戏让各公会参加每周的比赛活动。'),sources=S('guilds','guild'))
W('specialty','英 /ˈspeʃəlti/；美 /ˈspɛʃəlti/','专长；专业领域；特色产品、拿手菜',
 '别人不一定会，但你特别擅长的，是 your specialty；一家店特别拿手的一道菜，也是 its specialty。把“它特有、它拿手的东西”抓住，就能贯通。',
 '经古法语 especialte 等名词借入，较远接拉丁 specialis 特别、特有及名词构词材料；英语 -ty 对应这类性质名词尾，不代表这个借词一定在现代英语现场由 special 造出。',SPECIALTY,
 'her specialty 是她的专长；a local specialty 是地方特色产品、菜；a medical specialty 是医学专业领域，这些都围着专门、特有展开。',
 'a local specialty；a house specialty；a field of specialty。',
 'specialty 在美式很常见；英式也常用 speciality。special 是形容词特别的，specialty 是那项专长、特产或专门领域。',
 ('Repairing old clocks is her specialty.','修理老钟表是她的专长。'),('The waiter recommended a local specialty.','服务员推荐了一道当地特色菜。'),sources=S('specialty','specialty'))
W('specialties','英 /ˈspeʃəltiz/；美 /ˈspɛʃəltiz/','专长；专业领域；特色菜、特产〔复数〕',
 '菜单上几道拿手菜，或一个机构涵盖的几项专门领域，都是 specialties。一个“特别拿手的项目”可以数成多个。',
 'specialty 的辅音字母 t + y 词尾，变 y 为 i + -es → specialties，原词末尾的 /i/ 保留，复数后缀读 /z/，不额外增加音节。',SPECIALTY+[['specialty 变 y 为 i + -es → specialties','多个专长、领域、特色产品；末尾 /tiz/']],
 'regional specialties 是地方特色食品；technical specialties 是技术专业方向；specialties of the house 是店里的拿手菜。',
 'regional specialties；local specialties；technical specialties。',
 'specialties 对应 specialty；specialities 对应 speciality。两套基础词拼写各有复数，不是把中间 i 随意加删。',
 ('The menu lists several regional specialties.','菜单列出了几道地方特色菜。'),('The team brings together people from different technical specialties.','团队集合了来自不同技术专业方向的人。'),sources=S('specialties','specialty'))
W('shawl','英 /ʃɔːl/；美 /ʃɔl/','披肩；围披织物',
 '一大片柔软织物搭在肩上，天凉时包住上身，就是 shawl。它通常比只围在脖子上的细长围巾更适合铺开披着。',
 '经乌尔都等南亚语言接波斯 shal，整个衣物名称借入英语；更远以某个地名命名的说法没有充分确定。',SHAWL,
 'a woollen shawl 是羊毛披肩；wrap a shawl around your shoulders 是把披肩裹在肩上。',
 'a woollen shawl；a silk shawl；wrap a shawl around your shoulders。',
 'scarf 常是围巾、丝巾；shawl 常是披在肩上的较大片织物。实际款式有重叠，要看大小和穿戴方式。',
 ('She wrapped a shawl around her shoulders.','她把一条披肩裹在肩上。'),('The woven shawl kept her warm during the journey.','旅途中，那条编织披肩让她暖和些。'),sources=S('shawl','shawl'))
W('shawls','英 /ʃɔːlz/；美 /ʃɔlz/','披肩〔复数〕',
 '店里挂着好几条披肩，是 shawls。把一大片肩上织物数成一条、几条，比中文只记“衣服”更具体。',
 'shawl + -s → shawls，末尾 /l/ 后接 /z/；衣物借词形成英语可数复数。',SHAWL+[['shawl + -s → shawls','多条披肩；词尾 /lz/']],
 'woven shawls 是编织披肩；silk shawls 是丝披肩；a collection of shawls 是一批披肩收藏。',
 'woven shawls；silk shawls；colourful shawls。',
 'shawls 指独立的几条披肩，shawl fabric 则按材料说披肩面料，作修饰语时通常仍用单数 shawl。',
 ('The market stall sells handwoven shawls.','集市摊位卖手工编织披肩。'),('They draped colourful shawls over the chairs.','他们把彩色披肩搭在椅子上。'),sources=S('shawls','shawl'))
W('grove','英 /ɡrəʊv/；美 /ɡroʊv/','小树林；成片树木、果树林',
 '走过一小片树，或看见一片橄榄树，英语可以说 a grove。它让你把一群树看成一处小林，而不是单独一棵树。',
 '接古英语 graf 小树林，与古英语树丛词形有联系；更远来源不明。现代拼写虽接近 grow，不能当作 grow 直接加一段形成。',GROVE,
 'an olive grove 是橄榄林；an orange grove 是橘园；a grove of trees 是一片树木。是否人工种植由具体语境决定。',
 'an olive grove；an orange grove；a grove of trees。',
 'forest 往往范围更大；grove 常指相对小、成片的林木。orchard 更明确是栽种果树的园地，词义范围不完全一样。',
 ('We walked through a small grove of pine trees.','我们走过一小片松树林。'),('The house overlooks an olive grove.','房子俯瞰着一片橄榄林。'),sources=S('grove','grove'))
W('groves','英 /ɡrəʊvz/；美 /ɡroʊvz/','小树林、果树林〔复数〕',
 '山坡这一片、那一片的橄榄林，是 olive groves。复数数的是几处成片的林，不是只把里面的每棵树数出来。',
 'grove + -s → groves，基础词保留 e 再加 s，/v/ 后后缀读 /z/。',GROVE+[['grove + -s → groves','多片小林；末尾 /vz/']],
 'olive groves 是多片橄榄林；groves of trees 是一片片树丛。名词 trees 数树，groves 数成片林木。',
 'olive groves；orange groves；groves of trees。',
 'groves 与 grooves 沟槽、凹槽拼写和读音不同：groves /ɡroʊvz/，grooves /ɡruːvz/。',
 ('Olive groves cover the lower slopes.','山坡低处遍布橄榄林。'),('The path winds between small groves of trees.','小路蜿蜒穿行在一片片小树林之间。'),sources=S('groves','grove'))
W('abbey','英、美 /ˈæbi/','修道院；保留修道院历史名称的教堂、建筑',
 '看到一处历史建筑名里的 Abbey，可以先想到由院长领导的修道院。后来机构变化了，有些教堂或建筑仍保留旧名称。',
 '法语 abaïe、abbeie 接晚期拉丁 abbatia，来自 abbas 院长；更远经希腊接阿拉姆语 abba 父亲的尊称。父亲称呼借给宗教领袖，再形成机构名。',ABBEY,
 'an abbey 是一处修道院；the ruins of an abbey 是修道院遗址。专名 Westminster Abbey 的 Abbey 延续其历史名称。',
 'an old abbey；abbey ruins；a medieval abbey。',
 'church 是较宽的教堂、教会词；abbey 特别联系修道院背景。名字带 Abbey 的现存建筑，不保证今天仍有相同修道团体。',
 ('We visited the ruins of a medieval abbey.','我们参观了一座中世纪修道院的遗址。'),('The abbey church stands beside the river.','这座修道院教堂立在河边。'),sources=S('abbey','abbey'))
W('abbeys','英、美 /ˈæbiz/','修道院〔复数〕；保留旧名的相关建筑〔复数〕',
 '地图上几处历史修道院，是 abbeys。这里末尾 y 前是元音字母 e，复数直接加 s，保留 ey。',
 'abbey + -s → abbeys，读 /ˈæbiz/；不是辅音字母 + y 的情况，不改成 abbies。',ABBEY+[['abbey + -s → abbeys','元音字母 e + y 保留，直接加 s']],
 'medieval abbeys 是中世纪修道院；ruined abbeys 是已成遗址的修道院。词尾 s 数多个场所。',
 'medieval abbeys；ruined abbeys；abbeys and churches。',
 'abbey → abbeys 保留 ey，specialty → specialties 改 y 为 ies。区别看 y 前是元音字母还是辅音字母。',
 ('The route passes two ruined abbeys.','这条路线经过两处修道院遗址。'),('The guide explains the history of the region’s abbeys.','导游介绍了这一带各修道院的历史。'),sources=S('abbeys','abbey'))
W('exile','英 /ˈeksaɪl/；美 /ˈɛɡzaɪl/','流放、放逐；流亡；流亡者；放逐某人',
 '人被迫离开自己的国家，长期在故土之外生活：这份处境可以是 exile，这个人也可以是 an exile。动作、状态和承受的人都围着“离开故土”展开。',
 '名词经法语 exil、essil 接拉丁 exilium、exul；动词经法语 essillier 等接拉丁相关动词。ex- 向外较清楚，后半与行走、驱赶等哪一线相连仍有争论。',EXILE,
 'live in exile 是流亡在外；an exile 是一名流亡者；exile someone from a country 是把某人放逐出某国。也可用于文学中的自我疏离比喻。',
 'live in exile；go into exile；an exile；exile someone from a country。',
 'travel abroad 只是出国旅行；exile 常带被迫、无法回乡或与故土断开的含义。self-imposed exile 才明确说自己选择的离开。',
 ('The writer spent many years in exile.','这位作家多年流亡在外。'),('The king threatened to exile anyone who opposed him.','国王威胁要放逐所有反对他的人。'),sources=S('exile','exile'))
W('exiles','英 /ˈeksaɪlz/；美 /ˈɛɡzaɪlz/','流亡者〔复数〕；放逐〔第三人称单数〕',
 '几位离乡难归的人，是 exiles；the ruler exiles opponents 则是统治者把对手放逐。看谁在句子里承受、谁在执行。',
 'exile + -s → exiles，基础末尾已有 e，直接加 s，后缀读 /z/；名词复数和动词第三人称单数同形。',EXILE+[['exile + -s → exiles','多名流亡者；或单数主语执行放逐']],
 'political exiles 是政治流亡者；a community of exiles 是流亡者社群；exiles someone from 是把人逐出某地。',
 'political exiles；a community of exiles；exiles his opponents。',
 'in exile 常按不可数状态说流亡；exiles 常按可数人物说流亡者。He is in exile 与 they are exiles 句型不同。',
 ('The city became a meeting place for exiles.','这座城市成了流亡者的聚集地。'),('In the novel, the ruler exiles his rivals to a distant island.','小说里，统治者把竞争对手放逐到一座遥远的岛上。'),sources=S('exiles','exile'))
W('exiled','英 /ˈeksaɪld/；美 /ˈɛɡzaɪld/','被放逐的、流亡的；放逐了〔过去式、过去分词〕',
 'a leader in exile 换成修饰名词的样子，可以说 an exiled leader。-ed 把被放逐、被迫离开的经历留在人物身上。',
 'exile 去末尾 e + -ed → exiled，后缀读 /d/；过去分词常用于被动或人物修饰语。',EXILE+[['exile 去 e + -ed → exiled','过去式、过去分词；已遭放逐的状态']],
 'an exiled writer 是流亡作家；was exiled to 是被放逐到；was exiled from 是被逐出某地。to 与 from 分别说明去向、离开的地方。',
 'an exiled writer；exiled to an island；exiled from his homeland。',
 'exiled 强调离开故土的经历；foreign 只是外国的，不能把所有外国居民都称为 exiled。',
 ('The exiled writer continued to publish abroad.','这位流亡作家继续在国外发表作品。'),('He was exiled to a remote island.','他被放逐到一座偏远岛屿。'),sources=S('exiled','exile'))
W('exiling','英 /ˈeksaɪlɪŋ/；美 /ˈɛɡzaɪlɪŋ/','正在放逐；放逐这一行为',
 '把人驱离故土的行为本身，是 exiling。-ing 可以把动作当作一件事来讨论，不一定每次都翻成“正在”。',
 'exile 去末尾 e + -ing → exiling；动词来自法语、拉丁放逐词线，再接英语分词后缀。',EXILE+[['exile 去 e + -ing → exiling','现在分词、动名词；放逐过程或行为']],
 'exiling an opponent 是放逐一名对手；by exiling someone 是通过放逐某人；exiling himself 则可说他主动远离某地、某种生活。',
 'exiling an opponent；by exiling someone；exiling himself abroad。',
 'exiling 通常把执行动作的一方放到前面；being exiled 才把承受放逐的一方作为过程中的主角。',
 ('The play shows a ruler exiling his closest adviser.','戏剧表现一位统治者放逐自己最亲近的顾问。'),('Exiling the poet did not silence his work.','放逐这位诗人，并没有让他的作品失去声音。'),sources=S('exiling','exile'))
W('ruder','英 /ˈruːdə/；美 /ˈrudɚ/','更粗鲁、更失礼的；更粗糙的',
 '一句话本来就不客气，换一种说法还更冲，就是 ruder。比较的是粗鲁程度，不是另一个独立的人或动作。',
 'rude 去末尾 e + -er → ruder；完整比较级后缀是 -er，表更。rude 接法语、拉丁粗糙、未受训练的旧材料，后来用于失礼行为。',RUDE+[['rude 去 e + -er → ruder','比较级；表程度更高，不是做某事的人']],
 'ruder than before 是比以前更无礼；sound ruder 是听上去更冲。旧义也可比较制作、表面的粗糙，现代日常先掌握礼貌义。',
 'ruder than before；sound ruder；a ruder reply。',
 '-er 在 ruder 里是比较级，不是 teacher 那种人物后缀。相同后缀外形要看基础词和句法。',
 ('His second reply was even ruder than the first.','他的第二次回复比第一次还不客气。'),('That wording sounds ruder than you probably intended.','那种措辞听起来比你原本想表达的更冲。'),sources=S('ruder','rude'))
W('rudest','英 /ˈruːdɪst/；美 /ˈrudɪst/','最粗鲁、最失礼的；最粗糙的',
 '在一组言行里，最不客气的那一个，是 the rudest。最高级需要一个比较范围，可以是今天见过的、这一群里的，或一直以来遇到的。',
 'rude 去 e + -est → rudest，完整最高级后缀是 -est，读 /ɪst/；不是只接字母 -st。',RUDE+[['rude 去 e + -est → rudest','最高级，比较一定范围中的最高程度']],
 'the rudest reply 是最粗鲁的回复；one of the rudest 是最无礼的之一，后面通常接复数名词。',
 'the rudest reply；the rudest person；one of the rudest comments。',
 'ruder 比两者或程度更高，rudest 在一个范围内达到最高。one of the rudest comments 里 comments 用复数，因为从一组里选一个。',
 ('That was the rudest reply I had received all week.','那是我这周收到的最不客气的回复。'),('It was one of the rudest comments in the discussion.','那是讨论里最无礼的评论之一。'),sources=S('rudest','rude'))
W('lad','英、美 /læd/','男孩；小伙子；〔熟络称呼〕伙计',
 '英国口语里，一个年轻小伙可以叫 a lad，朋友间也能带熟络意味。它今天可以亲切，历史上却未必一直是夸人的称呼。',
 '中古英语 ladde 有年轻男仆、地位较低男子等旧义；可能来自北欧语言，但具体来路不明。后来男孩、年轻男子义扩大，现代常有熟络、亲切语气。',LAD,
 'a young lad 是年轻小伙；a local lad 是本地小伙；good lad 可以是熟络地夸一句好小子、干得好。',
 'a young lad；a local lad；good lad。',
 'boy 是更宽的男孩名称；lad 的地区色彩和熟络语气更明显。是否显得亲切，也取决于说话双方的关系。',
 ('A young lad helped us carry the bags.','一个年轻小伙帮我们提了行李。'),('He is a local lad who knows the area well.','他是本地小伙，对这一带很熟。'),sources=S('lad','lad'))
W('lads','英、美 /lædz/','男孩们、小伙子们；〔口语〕伙计们',
 '招呼一群熟人，说 come on, lads，像中文的“走吧，伙计们”。字面可以数几个年轻男孩，也能在朋友、球队语境里泛说一伙人。',
 'lad + -s → lads，/d/ 后后缀读 /z/；普通可数名词复数，语气仍带 lad 的熟络和地区特点。',LAD+[['lad + -s → lads','多个男孩、小伙；也用来招呼熟悉的一群人']],
 'the local lads 是本地小伙们；the lads on the team 是队里那帮伙计；come on, lads 是招呼、鼓励。',
 'the local lads；a group of lads；come on, lads。',
 'lads 可以指熟识的成年男性群体，不必每次都译成幼小男孩；具体年龄看上下文。',
 ('The local lads were playing football in the park.','本地几个小伙正在公园踢足球。'),('“Come on, lads,” the captain called.','“加把劲，伙计们。”队长喊道。'),sources=S('lads','lad'))
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_zim',ROOTS,WORDS)
 extend_lessons()
