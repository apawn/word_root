"""Merit, petty, polite, flame, thumb and diary."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
M=[['拉丁 merere、mereri → meritum','挣得、应得 → 值得奖惩的表现、价值'],['法语 merite 等 → 英语 merit','优点、长处、价值；动词说值得、应得到']]
W('merit','/ˈmerɪt/','优点、价值；功绩；值得、应得到',
 '不用先看身份，单看这件事本身值不值得肯定，就是看 merit。动词也能说某事值得认真讨论，或某行为应受批评。',
 '经法语 merite 等接拉丁 meritum，来自挣得、应得的 merere 一族；早期可说应得奖惩，英语名词常偏正面的价值、功绩。',M,
 'on merit 凭能力、表现，the merits of a plan 计划的优点，merit consideration 值得考虑，merit criticism 应受批评。',
 'on merit；the merits of；merit consideration。',
 'merit 名词常正面，动词的应得却能接 criticism 等负面结果；merits 还可谈事情实质，具体看结构。',
 ('The idea has merit and deserves a closer look.','这个想法有可取之处，值得进一步考察。'),('Candidates were selected on merit.','候选人依据能力和表现被选出。'),('The decision merits serious criticism.','这个决定应受到严肃批评。'),sources=['https://en.wiktionary.org/wiki/merit#English','https://www.etymonline.com/word/merit'])
W('meritocratic','英 /ˌmerɪtəˈkrætɪk/；美 /ˌmerɪtəˈkrætɪk/','按能力、成绩、功绩选拔分配的；精英治理相关的',
 '职位、机会按表现和能力分配，而不是只看出身、关系，这种原则叫 meritocratic。现实中怎样衡量能力，是另一个需要讨论的问题。',
 'merit + 连接元音 -o- + -cratic，或 meritocrat + -ic；与 meritocracy 的 -cracy／-cratic 名词、形容词对应。-cratic 通向治理、权力词族。',M+[['merit + -o- + -cratic → meritocratic','以能力、功绩为依据的制度性质']],
 'a meritocratic system 按能力、功绩选拔的制度，a meritocratic ideal 任人唯贤的理想，meritocratic selection 按能力表现选拔。',
 'a meritocratic system；meritocratic selection。',
 'meritocratic 是制度原则、性质的描述，不单凭这个标签就能证明衡量标准已经公平。',
 ('The organisation aimed to make promotion more meritocratic.','机构希望晋升更依据能力和表现。'),('The essay questions whether the system is truly meritocratic.','文章质疑这个制度是否真正按能力、功绩运行。'))
R('B4109','应得的价值、表现，到依据功绩选拔的制度词','MERIT：看表现值不值得，再看怎样据此分配机会','merit → meritocracy、meritocratic。',
 '从一个人的表现、一个方案的优点，走到制度用什么标准选人。词源说明应得的概念，具体标准仍要由实际制度来定。',
 'merere 应得 → meritum → 法语、英语 merit；-cracy 治理、制度，-cratic 相应形容词。',
 [['价值、表现与选拔制度','merit · meritocracy · meritocratic']],
 'merit 动词可接负面应得结果；meritocratic 标签不自动证明标准公平。',
 'A meritocratic process should assess candidates on merit.\n\n按能力、功绩运行的程序，应据实际表现评价候选人。','merit meritocracy meritocratic')
P=[['古法语 petit → 中古英语 peti、pety → petty','小、次要；更远来源未定'],['规模小 → 不重要 → 小心眼','小额款项可中性，行为评价则常带贬意']]
W('petty','/ˈpeti/','小的、次要的；琐碎的；小心眼、斤斤计较的',
 '事情本来很小，却有人一直抓住不放，petty 就从小事走到小心眼。petty cash 只是小额备用金，并没有骂钱的意思。',
 '借法语 petit 小，经中古英语 peti、pety 等发展，现代 y 是借词拼写演变，不是 pet 宠物加 -y。',P,
 'petty cash 小额备用金，petty details 琐碎细节，petty jealousy 小心眼的嫉妒，a petty argument 为小事的争吵。',
 'petty cash；petty jealousy。',
 'petty 的小额、低级别义可中性；说人 petty 通常批评目光狭窄、为小事计较。',
 ('The office keeps petty cash for small expenses.','办公室备有小额现金，用于零星开销。'),('They stopped arguing over petty details.','他们不再为琐碎细节争吵。'),sources=['https://en.wiktionary.org/wiki/petty#English','https://www.etymonline.com/word/petty'])
W('pettiness','/ˈpetinəs/','小心眼、斤斤计较；琐碎狭隘的态度',
 '不是一件东西体积小，而是心思一直困在一点点不快、小利益里；这种狭隘、计较的状态就是 pettiness。',
 'petty + -ness，y 变 i，形成性质名词；常接 petty 对人或行为的负面评价。',P+[['petty + -ness → pettiness','琐碎狭隘、小心眼的性质']],
 'petty behaviour 的性质可说 pettiness，rise above pettiness 不受小心眼、琐碎计较影响。',
 'rise above pettiness；an act of pettiness。',
 'pettiness 不等于普通 smallness 体积小；它通常评价态度和行为。',
 ('She was tired of the pettiness in the office.','她厌倦了办公室里的小心眼和琐碎计较。'),('They tried to rise above personal pettiness.','他们试图摆脱个人之间的小心眼。'))
R('B3784','小、次要的旧义与现代小心眼评价','PETTY：事情小是一层，心思只容得下小事又是一层','petty → pettiness；petticoat 保留旧的小外衣词义。',
 '备用小钱不带贬意，小心眼却带评价。petticoat 的 petti- 保存旧小义，不能把衬裙解释成小气的外套。',
 'petit → petty；y 变 i 接 -ness；旧 petty + coat 形成 petticoat。',
 [['小、琐碎与态度性质','petty · pettiness'],['旧小义的衣物复合','petticoat']],
 'petty cash 中性；pettiness 通常负面；petticoat 看历史衣物名。',
 'A petty disagreement revealed unnecessary pettiness.\n\n一场小争执暴露了不必要的斤斤计较。','petty pettiness petticoat')
Po=[['拉丁 polire 打磨 → politus','磨光、精细、文雅'],['英语 polite','由文雅、修养扩展为待人有礼、考虑他人'],['后缀与否定','politely 方式；politeness 性质；impolite 不礼貌']]
W('polite','/pəˈlaɪt/','有礼貌、得体的',
 '像把粗糙边角磨平，说话、举止不扎人，懂得顾及对方，这就是 polite。今天不是说人的皮肤真被抛光了。',
 '借拉丁 politus 磨光的，是 polire 打磨的过去分词；从文雅、受过修养发展为待人得体、有礼。',Po[:2],
 'be polite to someone 对某人有礼貌，a polite reply 得体回复，polite conversation 礼貌交谈，a polite refusal 客气拒绝。',
 'be polite to；a polite reply。',
 'polite 不一定表示内心同意；人可以礼貌地拒绝，也可以只是维持客气。',
 ('She was polite to everyone she met.','她对见到的每个人都很有礼貌。'),('He gave a polite refusal.','他客气地拒绝了。'),sources=['https://en.wiktionary.org/wiki/polite#English','https://www.etymonline.com/word/polite'])
W('politely','/pəˈlaɪtli/','有礼貌、客气地',
 '意思可能很坚决，表达方式却照顾对方感受，就是 politely。礼貌说不，仍然是说不。',
 'polite + -ly，形成方式副词，末尾 e 保留。',Po[:2]+[['polite + -ly → politely','以礼貌、得体的方式']],
 'ask politely 礼貌询问，decline politely 客气谢绝，smile politely 礼貌微笑。',
 'ask politely；decline politely。',
 'politely 评价表达方式，不自动说明态度亲密、意见一致；a polite smile 也可能保持距离。',
 ('She politely declined the invitation.','她客气地谢绝了邀请。'),('He asked politely whether the seat was free.','他礼貌地问这个座位有没有人。'))
W('politeness','/pəˈlaɪtnəs/','礼貌、客气；礼貌举动',
 'polite 是人或话语得体，politeness 是这种待人方式本身。out of politeness 就是出于礼貌。',
 'polite + -ness，形成性质名词，通常不可数；具体礼节、客套行为有时也可用可数相关表达。',Po[:2]+[['polite + -ness → politeness','礼貌、客气的性质']],
 'out of politeness 出于礼貌，common politeness 基本礼貌，a matter of politeness 礼貌问题。',
 'out of politeness；common politeness。',
 'politeness 不等于承诺；别人出于礼貌倾听，不能只据此判断对方已经答应。',
 ('I stayed for a few minutes out of politeness.','我出于礼貌又待了几分钟。'),('A little politeness made the conversation easier.','稍微客气一点，谈话就顺畅多了。'))
W('impolite','/ˌɪmpəˈlaɪt/','不礼貌、失礼的',
 '话说得冒犯、举止不顾别人感受，就是 impolite；它针对礼貌规范，不一定说明一个人所有方面都坏。',
 '借拉丁 impolitus 未磨光、不文雅的，现代对应 im- + polite；im- 是否定 in- 在 p 前的同化形式。',Po[:1]+[['in- 否定 + politus → impolitus → impolite','未磨光、不文雅 → 不礼貌']],
 'an impolite remark 失礼的话，be impolite to someone 对某人失礼，It is impolite to ... 做某事失礼。',
 'an impolite remark；be impolite to。',
 'impolite 的 im- 是否定，不是表示进入；rude 往往语气更直接，也可有其他粗野、粗糙义。',
 ('It is impolite to interrupt someone repeatedly.','一再打断别人讲话很失礼。'),('He apologised for his impolite remark.','他为自己失礼的话道了歉。'))
R('B3946','打磨光滑的旧形象，进入得体言行与礼貌规范','POLITE：把粗糙边角磨掉，让相处不扎人','polite → politely、politeness；impolite 是否定。',
 '动作磨光变成修养文雅，再落到考虑别人、表达得体。性质、方式和抽象礼貌连着看，否定词仍保留旧未磨光的背景。',
 'polire → politus → polite；-ly 方式，-ness 性质；in- 在 p 前同化为 im-。',
 [['礼貌性质、方式及抽象状态','polite · politely · politeness'],['失礼性质','impolite']],
 '礼貌不保证同意；out of politeness 出于客气；impolite 否定的是礼貌。',
 'She politely explained why the remark had sounded impolite.\n\n她礼貌地解释了那句话为什么听着失礼。','polite politely politeness impolite')
Fl=[['拉丁 flamma、指小 flammula','火焰、小火焰'],['法语 flame、flambe 等 → 中古英语相关形式 → flame','火焰；热情、恋爱和争吵等借火的形象'],['复合与状态形式','flamethrower 喷火装置；aflame 燃烧、情绪激烈']]
W('flame','/fleɪm/','火焰；燃烧；旧情人；激烈辱骂、抨击',
 '火中看得见、发光的那一部分是 flame；热情像火、恋情像火，网上骂战也像火气往外喷，所以形成几条常用比喻。',
 '经法语 flame、flambe 等相关形式接拉丁 flamma 与指小 flammula。由实体火焰扩展情感热烈、恋爱对象及激烈攻击。',Fl[:2],
 'a candle flame 烛焰，burst into flames 突然燃起，an old flame 旧情人，flame someone on a forum 在论坛上辱骂、激烈攻击某人。',
 'burst into flames；an old flame。',
 'fire 可说整体燃烧现象、火灾，flame 更具体说可见火焰；an old flame 是人物比喻。',
 ('The candle flame flickered in the draught.','烛焰在穿堂风里摇曳。'),('He met an old flame at the reunion.','他在聚会上遇见一位旧情人。'))
W('flamethrower','英 /ˈfleɪmθrəʊə/；美 /ˈfleɪmθroʊər/','火焰喷射器、喷火装置',
 '把火焰向前喷出的装置，就是 flame + thrower。英语用扔出去的动作形象命名，不代表真的像手抛一个固体。',
 'flame 火焰 + thrower 投射者、装置，仿译德语 Flammenwerfer；名词可以用于武器或特定工具名称。',Fl[:2]+[['flame + thrower，仿译德语相应词','向外喷射火焰的装置']],
 'a flamethrower 火焰喷射器，a flamethrower in a museum 博物馆里的喷火器；这里只按名称认识装置用途。',
 'a flamethrower；an old flamethrower。',
 'thrower 在器具名里指能投射、喷出相应对象的装置，不必是执行动作的人。',
 ('The museum displayed an old flamethrower.','博物馆展出了一具旧火焰喷射器。'),('The film showed a soldier carrying a flamethrower.','影片中出现了一名携带喷火器的士兵。'))
W('aflame','/əˈfleɪm/','燃烧着的；情绪、色彩如火般的',
 '房子陷在火中是 aflame；天空一片火红、内心激动得像燃烧，也能借它描述强烈状态。',
 '形容词、副词常分析为 a- 处于、在……中 + flame 火焰；由处于火中扩展为颜色、情绪炽烈。',Fl[:2]+[['a- 在……中 + flame → aflame','着火；色彩、情绪如火']],
 'be aflame 燃烧，set aflame 点燃，aflame with excitement 因兴奋而炽热；常在系动词后或作补充状态。',
 'be aflame；set aflame；aflame with。',
 'aflame 通常不是任意放在名词前的普通前置形容词；a burning house 比 an aflame house 更自然。',
 ('The building was already aflame when they arrived.','他们到时，大楼已经燃烧起来。'),('The western sky was aflame with orange and red.','西边天空橙红一片，像燃烧着。'),sources=['https://en.wiktionary.org/wiki/aflame#English','https://www.etymonline.com/word/aflame'])
R('B3115','可见火焰与热烈情感，装置和状态各按后部读','FLAME：有形的火焰，也能照见热情与火气','flame → flamethrower、aflame。',
 '实体火焰提供光、热和激烈感；现代旧情人、骂战等用法都按具体场景识别。装置名是投射火，状态词是处于火中。',
 'flamma、flammula 经法语 → flame；thrower 投射装置；a- 在某状态中。',
 [['火焰及情感、交流比喻','flame'],['装置与燃烧状态','flamethrower · aflame']],
 'flame 与 fire 观察范围不同；aflame 常作表语状态；old flame 是旧情人。',
 'The flames spread, and soon the shed was aflame.\n\n火焰蔓延，很快棚子也烧了起来。','flame flamethrower aflame')
Th=[['古英语 þūma → 中古英语 thome、thombe → thumb','拇指；更远常联系粗壮、膨起'],['旧工具名 þȳmel → thimble','拇指词族 + 工具后缀；后有元音变化及 b 拼写'],['现代复合','thumbnail 拇指甲、缩略图；thumbprint 拇指印']]
W('thumb','/θʌm/','拇指；用拇指翻动、示意',
 '手上能与其他指尖相对的粗短那根，是 thumb；翻书时拇指哗哗拨页，就 thumb through。',
 '承古英语 þūma，经中古英语形式延续；更远通常联系粗壮、膨起。b 是历史拼写发展，现代常用读音不发 /b/。',Th[:1]+[['中古英语 thombe → thumb','拼写出现 b，现代读音保留 /θʌm/']],
 'thumbs up 赞成手势，thumb through a book 快速翻书，under someone’s thumb 受某人控制，a rule of thumb 经验性准则。',
 'thumbs up；thumb through；a rule of thumb。',
 'thumb 的 th 读 /θ/，b 不发音；rule of thumb 是大致经验准则，不自动等于精密、无例外的规则。',
 ('She gave us a thumbs up.','她向我们竖起拇指表示赞成。'),('He thumbed through the magazine while waiting.','等候时，他快速翻了翻杂志。'))
W('thimble','/ˈθɪmbəl/','顶针、缝纫指套',
 '缝衣时手指顶住针尾，把针推过布，需要一个小硬套保护、受力，这个套就是 thimble。它的名字确实与拇指词族有关。',
 '承古英语 þȳmel，联系 þūma 拇指 + 旧工具名后缀 -el；经中古英语 thimel 等到 thimble，b 后来进入拼写。与 thumb 的元音、b 发音都不同。',Th[:1]+Th[1:2],
 'a sewing thimble 缝纫顶针，a metal thimble 金属顶针；现代实际戴在哪根手指取决于使用习惯，不受旧名字限制。',
 'a sewing thimble；a metal thimble。',
 'thumb /θʌm/ 的 b 不发音，thimble /ˈθɪmbəl/ 的 b 发音；旧工具后缀不能一概翻成小。',
 ('She wore a thimble while sewing the thick fabric.','缝厚布料时，她戴着顶针。'),('An old silver thimble lay in the sewing box.','针线盒里放着一枚旧银顶针。'),sources=['https://en.wiktionary.org/wiki/thimble#English','https://www.etymonline.com/word/thimble'])
R('B2683','粗短拇指及相关指套、印记和缩略图','THUMB：用最灵活的粗短指，留下印记也帮着翻页','thumb → thumbnail、thumbprint；thimble 保存旧工具构词。',
 '拇指甲、拇指印看复合前项，缩略图借拇指甲小尺寸命名。顶针则有更早的工具后缀与音形变化。',
 'þūma → thumb；nail 指甲，print 印记；þȳmel 工具名 → thimble。',
 [['拇指及印记、图像复合','thumb · thumbprint · thumbnail'],['旧指套工具名','thimble']],
 'thumb 与 thimble 的元音、b 发音不同；thumbnail 不都是指甲，也可缩略图。',
 'She used her thumb to turn the page showing a picture of a thimble.\n\n她用拇指翻到印着顶针图片的那一页。','thumb thumbprint thumbnail thimble')
D=[['拉丁 dies 日 → diarius 每日的 → diarium','每日供给，后也用于每日记录'],['英语 diary','个人每日记录；再指有日期的记事本、日程本'],['diary + -ist → diarist','写日记的人']]
W('diary','英 /ˈdaɪəri/；美 /ˈdaɪəri/','日记；日记本、日程本',
 '一天一天写下经历，是 diary；把未来哪天约了谁记进去，也可以 diary。一个记录过去，一个安排日程。',
 '借拉丁 diarium，底层 diarius 每日的、dies 日；旧词有每日供给、后来每日记录的意义，英语再用来称相应本册。',D[:2],
 'keep a diary 写日记，a diary entry 一则日记，check one’s diary 查看日程本，put a meeting in the diary 把会议记入日程。',
 'keep a diary；a diary entry；check one’s diary。',
 'diary 与 dairy 乳品只换了字母顺序，词源、读音却不同；日记、日程义由上下文判断。',
 ('She has kept a diary since she was a teenager.','她从十几岁起就一直写日记。'),('Let me check my diary before choosing a date.','定日期前，让我查一下日程本。'),sources=['https://en.wiktionary.org/wiki/diary#English','https://www.etymonline.com/word/diary'])
W('diarist','/ˈdaɪərɪst/','日记作者、写日记的人',
 '不是写任何文章都叫 diarist，而是以写日记这一种记录方式来称人。历史上著名日记作者尤其常被这样介绍。',
 'diary 去末尾 y 加 -ist，形成从事相应活动的人名；真正拼成 diarist，不保留完整 diary 再叠加。',D[:2]+[['diary → diar- + -ist → diarist','写日记的人']],
 'a famous diarist 著名日记作者，a wartime diarist 战时日记作者，the diarist’s observations 日记作者的观察。',
 'a famous diarist；a wartime diarist。',
 'diarist 不表示每天从不间断写作的资格证明；它主要按日记这一文体、记录习惯命名。',
 ('The historian quoted a diarist who lived in the city.','历史学家引用了一位住在城里的日记作者的记录。'),('As a diarist, she paid close attention to everyday details.','作为日记作者，她很留心日常细节。'))
R('B4281','每日记录与有日期的本册，作者加人物后缀','DIARY：按一天一天组织记录，也能安排未来','diary → diarist。',
 '日记条目、个人日程都与日期排列相连。作者词去掉 y 接 -ist，日记本和写日记的人分清。',
 'dies 日 → diarius 每日 → diarium → diary；diar- + -ist → diarist。',
 [['记录、本册与作者','diary · diarist']],
 'diary 与 dairy 不同；check my diary 常是查日程，不一定在翻私人回忆。',
 'The diarist recorded the meeting in her diary.\n\n日记作者把那次会面记进日记。','diary diarist')
if __name__=='__main__':save('continuation_20261030_mp',ROOTS,WORDS)
