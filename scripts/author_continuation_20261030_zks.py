"""Practical independent words, meaningful derivatives, and homonym distinctions."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
def S(word,base):
 return ['https://en.wiktionary.org/wiki/'+word+'#English','https://www.etymonline.com/word/'+base]
EXISTING_ROOT_ADDITIONS={
 'A1697':dict(words=['till','tiller','tillage'],label='till 耕作 → tiller 耕作者、耕作机；tillage 耕作',note='耕作 till 承古英语 tilian，tiller 的农业义对应 till+-er，tillage=till+-age。钱箱、收银机 till 来源不确定；舵柄 tiller 则经法语接拉丁织物、框架词族，不能都从耕地推出。'),
 'A1933':dict(words=['till','tillage'],label='till 耕地 + -age → tillage 耕作',note='tillage 加完整 -age，表示相应操作、过程；不把末尾拆成独立的年龄 age。'),
 'C1503':dict(words=['tiller'],label='织造框架词的另一条借入线：tiller 舵柄',note='tiller 的舵柄义经古法语 telier 工具柄、框架，接拉丁 tela、中世纪 telarium，与 texere 编织的词族相连。与 till+-er 耕作者、耕作机分源。'),
 'A1741':dict(words=['twitter','twittering','loom','looming','bicker','bickering'],label='twitter 鸟鸣；loom 隐约逼近；bicker 斗嘴〔三组分开〕',note='三组 -ing 都接完整词基。twitter 的鸟鸣词有拟声背景，不把其 -er 当作职业者后缀；bicker 的历史 -er 可能是反复动作材料。loom 织机承旧工具名，显得庞大、逼近的动词另源不定；looming 的逼近义接后者。'),
 'C1641':dict(words=['trump'],label='不同源对照词族：triumph → trump 王牌、胜过',note='triumph 本来作为 victory 的不同源对照词收录，不从 vincere 派生；trump 的牌类词常解释为 triumph 相关形式的缩变，再有胜过义。号角 trump 与 trumpet 另一路，不从 triumph 推出。'),
 'B3066':dict(words=['truce'],label='守信、承诺的同源支线 → truce 休战',note='truce 接中古英语 trewes 等旧承诺、协议名词的复数形式，远连 true 守信、可靠的词族。现代 a truce 按单数协议或休战期使用，不把词尾 ce 当作否定后缀。'),
 'C0619':dict(words=['gist'],label='事情所在之处 → gist 要点、主旨',note='gist 接古法语 gésir 躺、位于的第三人称词形，经法律表达事情、根据在于此而成为要点名词。直接路线是拉丁 iacere 躺、位于；与投掷的拉丁动词有更远联系，也不能跳过法语阶段直接按 throw 解释。'),
 'A1839':dict(words=['shrewd','shrewdness'],label='shrewd 判断精明 + -ness → shrewdness',note='shrewdness 承中古英语相应名词，现代对应 shrewd+-ness。shrewd 本身从早期负面的恶、狡黠评价，发展到判断敏锐，不把所有场景都说成品行邪恶。'),
 'A1699':dict(words=['seam','seamy'],label='seam 接缝 + -y → seamy；衣服里子 → 阴暗面',note='seamy 加完整 -y。衣服露出接缝的一面往往是里子，这个画面用于 the seamy side 社会、生活不体面的阴暗面。'),
 'A1776':dict(words=['tweezers'],label='成对工具的复数形式：tweezers 镊子',note='tweezers 的早期历史经法语 etui 小盒的借词、词形重新分析，名字从器具盒转移到里面的夹取工具。现代常用 a pair of tweezers；不是先有今天的动词 tweeze 再规则地添 -er、-s 的确定历史。'),
 'A1760':dict(words=['knackered'],label='knacker 使耗坏、使疲惫 + -ed → knackered',note='knackered 加完整 -ed，/r/ 后读 /d/；英式随意口语常说累坏、坏掉。knacker 的更早来源和行业名历史有不确定性，不硬拆出一个现代 knack。'),
}
W('till','英、美 /tɪl/','耕作、翻耕；收银机、钱箱〔不同来源〕',
 '农田里把土翻松，准备种植，是 till 的耕作义。商店里说钱进了 the till，又是收银机、钱箱；两个画面要分开。',
 '耕作动词承古英语 tilian 劳作、耕种。收银钱箱名词接中古英语 tylle 等，可能与法语隔间、容器词或旧拉、抽动作词有关，来源未定。',
 [['古英语 tilian 劳作、耕种 → 英语 till 动词','劳动逐渐集中到耕地、为种植整地'],['中古英语容器名称 → till 钱箱、收银机','这一路的远源有不同分析，不从耕地义直接推出']],
 'till the soil 是翻耕土壤；money in the till 是收银钱箱里的钱；at the till 是在收银处。先看农业还是商店场景。',
 'till the soil；till the land；at the till。',
 'till 的耕作义比 grow crops 种作物更突出土地处理；cash register 是收银机的另一常见说法。till Friday 中的 till 表直到，是另外的语法用法。',
 ('They till a small field behind the house.','他们在屋后耕种一小块田地。'),('She put the coins in the till.','她把硬币放进了收银钱箱。'),sources=S('till','till'))
W('tiller','英 /ˈtɪlə/；美 /ˈtɪlər/','耕作机；耕作者；舵柄〔最后一义另源〕',
 '花园里的翻土机可以叫 tiller，耕地的人也能这样称呼。船上的 tiller 却是一根用来转舵的柄，同形但来源另有一条线。',
 '农业义为 till 耕作 + 完整 -er，表示人或机器。舵柄义经古法语 telier 工具柄、织造框架，接中世纪拉丁 telarium、拉丁 tela 织物或织机词族。',
 [['英语 till + -er → tiller','执行翻耕的人、机器'],['拉丁 tela 相关材料 → 法语 telier → 英语 tiller 工具柄、舵柄','织造框架、工具柄的名称走向船舵的控制杆，与耕作词分源']],
 'a garden tiller 是园艺翻土机；a tiller of the soil 是耕作者，较书面；hold the tiller 是握住舵柄。',
 'a garden tiller；a tiller of the soil；hold the tiller。',
 'rudder 是船舵本身，tiller 通常是用来转动它的柄。农业机器义则与 till 耕地直接对应，不能把所有 -er 都翻成人。',
 ('A small tiller stood beside the garden shed.','一台小型翻土机放在园艺棚旁。'),('He held the tiller as the boat crossed the lake.','船横渡湖面时，他握着舵柄。'),('The poem praises the patient tiller of the soil.','这首诗赞颂耐心耕耘土地的人。'),sources=S('tiller','tiller'))
W('tillage','英、美 /ˈtɪlɪdʒ/','耕作；翻耕、整地',
 '把土翻动、整理成适合种植的状态，这种操作或做法可以叫 tillage。农事讨论里，它常把注意力放在怎样处理土地。',
 'till 耕作 + 完整 -age → tillage，中古英语已有相应形式。这里 -age 形成操作、过程名词，不是把年龄 age 接到耕地后。',
 [['古英语 tilian → till 耕作','劳动、种植、处理土地的动作词'],['till + -age → tillage','耕作的操作、过程；历史上也可说耕作过的土地']],
 'soil tillage 是土壤耕作；tillage methods 是耕作方式；reduced tillage 是减少翻耕的做法。具体效果取决于农事条件，词本身只是名称。',
 'soil tillage；tillage methods；reduced tillage。',
 'agriculture 是农业的总称，tillage 范围更窄，重点在土地耕作。planting 是种下种子、苗木等动作，不能与 tillage 处处互换。',
 ('The course compares several methods of tillage.','这门课程比较了几种耕作方式。'),('The report discusses how tillage changes the soil surface.','报告讨论了翻耕怎样改变土壤表面。'),sources=S('tillage','tillage'))
W('twitter','英 /ˈtwɪtə/；美 /ˈtwɪtər/','啁啾、连续细鸣；叽叽喳喳；细碎鸣声',
 '树枝上的小鸟发出一串轻细、颤动的叫声，可以用 twitter。人紧张、兴奋地轻声说个不停，也能借这个鸟鸣画面。',
 '接中古英语 twiteren 等，属于有拟声背景的日耳曼词族。现代整体认词，不把 -er 当作做某事的人，也不从社交平台名称反推鸟鸣词的来源。',
 [['有拟声背景的早期鸟鸣词 → 中古英语 twiteren → twitter','轻细、连续、颤动的叫声'],['鸟鸣 → 相似的人声、兴奋状态','既能作动词，也能作鸣声名词']],
 'birds twitter 是鸟儿啁啾；a twitter of birds 是一阵细碎鸟鸣；in a twitter 可说激动、忐忑的状态。',
 'birds twitter；a twitter of birds；in a twitter。',
 'tweet 可以是一声短促鸟叫，twitter 常让人想到一串细碎叫声。这里掌握普通词用法；专名的拼写大写与否还需看语境。',
 ('Small birds twitter in the branches outside my window.','小鸟在我窗外的树枝间啁啾。'),('A faint twitter of birds broke the silence.','轻细的鸟鸣打破了寂静。'),sources=S('twitter','twitter'))
W('twittering','英 /ˈtwɪtərɪŋ/；美 /ˈtwɪtərɪŋ/','细碎鸟鸣；啁啾的；叽叽喳喳的',
 '闭上眼，只听见一串接一串的小鸟细鸣，这种声音可以说 twittering。它也能修饰发出这种叫声的小鸟。',
 'twitter + 完整 -ing → twittering，原词保留。既可为动作形式，也可作为声音的名词或相关修饰语；twitter 本身有拟声背景。',
 [['早期鸟鸣词 → twitter 啁啾','原有连续细碎、颤动的声音意象'],['twitter + -ing → twittering','正在细鸣；或把这种声音作为整体来描述']],
 'the twittering of birds 是鸟儿的啁啾声；twittering birds 是啁啾的小鸟。形容人声时可带轻快、紧张或说个不停的感觉。',
 'the twittering of birds；twittering birds；soft twittering。',
 'roaring 是轰鸣、吼叫，twittering 通常轻细得多。读作普通声音描写时，不必套进网络发帖的用法。',
 ('We woke to the twittering of birds in the garden.','我们在花园里小鸟的啁啾声中醒来。'),('Twittering sparrows gathered on the roof.','啁啾的麻雀聚在屋顶上。'),sources=S('twittering','twitter'))
W('trump','英、美 /trʌmp/','王牌、将牌；胜过、压倒',
 '牌局里有一类牌，按规则能压过其他花色，这就是 trump。把这个优势搬到现实里，某种因素也能 trump 另一个因素，占上风。',
 '牌类名词通常解释为 triumph 胜利相关形式的缩变，法语 triomphe 也曾用于牌戏名称；动词从牌的优势义发展。号角 trump 另源，本词不由人名而来。',
 [['法语、英语 triumph 相关牌戏名称 → trump','牌局中占优势的花色、牌'],['trump 名词 → 动词 trump','用优势牌胜过 → 一般意义的胜过、压倒']],
 'a trump 是一张将牌；hearts are trumps 是红心为将牌；quality trumps quantity 是质量胜过数量。',
 'a trump；hearts are trumps；trump other considerations。',
 'triumph 常说成功、凯旋，trump 作动词通常直接接被胜过的对象。put one factor above another 的具体评价，仍看说话者的上下文。',
 ('I still have a trump in my hand.','我手里还留着一张将牌。'),('For this design, comfort should trump appearance.','对这个设计来说，舒适应当比外观更重要。'),sources=S('trump','trump'))
W('truce','英、美 /truːs/','休战；停战协议；暂停争吵',
 '双方先约好停手，暂时不打、不吵，就是 a truce。重点是冲突中的暂停，不表示所有分歧已经消失。',
 '接中古英语 trewes 等旧承诺、协议名词的复数形式，更早连古英语 treow 守信、承诺，与 true 的词族相连。现代 truce 已按单数词使用。',
 [['古英语守信、承诺名词 → 中古英语 trewe、复数 trewes','彼此作出的保证、协议'],['旧复数形式专化 → 现代 truce','约定暂停冲突；也用于日常争吵、竞争']],
 'call a truce 是提议休战、停止争吵；agree to a truce 是同意休战；an uneasy truce 是不稳固的暂时停战。',
 'call a truce；agree to a truce；an uneasy truce。',
 'peace 常说和平状态，truce 更突出暂停敌对活动的约定或时段。现代可以说 a truce、two truces，不能仍把它强当普通复数。',
 ('The two sides agreed to a temporary truce.','双方同意暂时休战。'),('After arguing all morning, the siblings called a truce.','争吵了一上午后，这对兄妹决定先停战。'),sources=S('truce','truce'))
W('gist','英、美 /dʒɪst/','要点；主旨；大意',
 '别人讲了五分钟，你没记住每个词，但抓到了他到底想说什么，这就是 the gist。先抓事情的中心，不求照着原话复述。',
 '经英法法律表达中的 gist，接古法语 gésir 躺、位于的第三人称形式，再接拉丁 iacere 躺、位于。事情的根据、关键在于哪里，逐渐变成主旨名词。',
 [['拉丁 iacere 躺、位于 → 古法语 gésir，词形 gist','在于此、依据在此的表达'],['法律表达里的关键所在 → 英语 gist','后来广泛指长篇话语、文章、复杂事情的要点']],
 'get the gist 是听懂、看懂大意；the gist of the argument 是论点的核心；give someone the gist 是把要点告诉某人。',
 'get the gist；the gist of it；give me the gist。',
 'a summary 是概括出来的一段摘要，the gist 是所抓到的核心内容。get the gist 不保证听懂了每个细节；g 在这个词里读 /dʒ/。',
 ('I missed a few words, but I got the gist.','我漏听了几个词，不过听懂了大意。'),('Can you give me the gist of the article?','你能把这篇文章的要点告诉我吗？'),sources=S('gist','gist'))
W('loom','英、美 /luːm/','织布机；隐约显出庞大轮廓；逼近〔动词另源〕',
 '名词 loom 是把线织成布的机器。动词 loom 则像雾中一座大楼慢慢显出来，又大又压人；不妙的事快要发生，也能说 loom。',
 '织布机名词承古英语 geloma 工具、器物，后来缩成 loom 并集中到织机义；heirloom 保留旧物件义。显得庞大、逼近的动词来源不确定，不能从织机直接推出。',
 [['古英语 geloma 工具、器物 → loom → 织布机义','同一旧物件义还保留在 heirloom 传家物中'],['另源不定的 loom 动词 → 庞大而模糊地出现、显得逼近','实体视觉画面用于事件将近、压力显著']],
 'a weaving loom 是织布机；loom out of the mist 是从雾里隐约显出庞大身影；loom large 是显得突出、重要，常带压力感。',
 'a weaving loom；loom out of the mist；loom large。',
 'appear 可以只是出现，loom 常带大、模糊、压近或令人担忧的感觉。名词机器和这个动词应分别记来源。',
 ('The museum displays a wooden loom.','博物馆里展出了一台木制织布机。'),('A stone tower began to loom out of the mist.','一座石塔开始从雾中隐约显出庞大轮廓。'),('The cost continued to loom large in their discussions.','费用问题在他们的讨论中始终十分突出。'),sources=S('loom','loom'))
W('looming','英、美 /ˈluːmɪŋ/','逼近、迫近的；隐约显出庞大身形的',
 '日历上的截止日越来越近，人也越来越有压力，就是 a looming deadline。它像一个越来越占据视野的大东西，不能忽视。',
 'loom 动词 + 完整 -ing → looming，词基保留。这里接显得庞大、逼近的动词，不是从织布机这个名词推导出截止日期。',
 [['另源不定的 loom 动词：庞大而模糊地显现','与织机同形，历史不确定而分开说明'],['loom + -ing → looming','可描述正在显现，也常修饰即将到来、令人有压力的事']],
 'a looming deadline 是逼近的截止日；a looming crisis 是迫近的危机；looming over the town 可说庞然俯临镇子上方。',
 'a looming deadline；a looming crisis；looming over the town。',
 'upcoming 较中性地说即将到来，looming 常多一层压迫、担忧或显著占据注意力的感觉。并不是任何开心的将来安排都自然用 looming。',
 ('The looming deadline made everyone work more carefully.','逼近的截止日期让大家工作得更加认真。'),('A dark shape was looming above the trees.','树木上方隐约显出一个庞大的暗色身影。'),sources=S('looming','loom'))
W('shrewdness','英、美 /ˈʃruːdnəs/','精明；敏锐的判断力；善于盘算',
 '别人只看到表面，他却能看出谁在让步、哪里有机会、价格有没有水分，这种看得准、算得清的本事，就是 shrewdness。',
 '承中古英语相应名词，现代可对应 shrewd + 完整 -ness。shrewd 早期有恶意、狡黠等负面评价，后来发展为判断敏锐、精明。',
 [['中古英语 shrewd 的早期形式及相应 -ness 名词','早期常带负面性格评价'],['词义逐渐转向机敏、精明 → 现代 shrewdness','可赞判断能力，也可暗示善于算计']],
 'business shrewdness 是商业判断的精明；political shrewdness 是政治眼光敏锐；show shrewdness 是显出精明判断。',
 'business shrewdness；political shrewdness；show shrewdness。',
 'intelligence 是更广的理解、思考能力，shrewdness 常看具体局面中能否判断得准。它不自动等于 dishonesty 不诚实。',
 ('Her shrewdness helped her spot a weakness in the proposal.','她判断敏锐，看出了提案里的一个弱点。'),('He combined practical shrewdness with a good sense of humour.','他既精明务实，也很有幽默感。'),sources=S('shrewdness','shrewd'))
W('seamy','英、美 /ˈsiːmi/','不体面的；阴暗、污秽的〔常用 the seamy side〕',
 '衣服外面光鲜，翻到里面却看得到一道道接缝。seamy side 借这个里子画面，说社会、生活不光彩、不愿示人的一面。',
 'seam 接缝 + 完整 -y → seamy。字面是有接缝、露出接缝；衣服里侧的形象用于较难看、不体面的事情。',
 [['古英语接缝词 → seam；seam + -y → seamy','具有或显露缝线的性质'],['衣服露接缝的一面 → the seamy side','由可见里子扩展为生活、社会不体面的阴暗面']],
 'the seamy side of city life 是城市生活的阴暗面；a seamy world 是不体面的圈子。现代常见重点是比喻，不一定谈衣服。',
 'the seamy side；seamy details；the seamy side of life。',
 'seamy 通常带道德、生活层面的不光彩，dark 还可以单说光线暗。它与 seem 看起来不是同一个词基。',
 ('The novel explores the seamy side of city life.','这部小说探究城市生活的阴暗面。'),('The investigation revealed some seamy details.','调查揭出了一些不光彩的细节。'),sources=S('seamy','seamy'))
W('tweezers','英 /ˈtwiːzəz/；美 /ˈtwiːzərz/','镊子',
 '两片细细的金属靠拢，夹起很小的东西，就是 tweezers。邮票、模型零件、细小毛发等场景里都可能见到。',
 '早期借法语 étui 小器具盒，英语有 etwee、etweese 等形式，经历缩短及复数重新分析，名称从盒子转移到里面的工具，形成 tweezers。不是先有现代动词 tweeze 再规则加 -er 的确定历史。',
 [['法语 étui 小盒 → 英语早期借词及缩短形式','名字原先联系收纳小器具的盒、匣'],['名称转移到夹取工具，词形重新分析 → tweezers','现代与 scissors、pliers 等一样，通常用复数形式称呼整件工具']],
 'a pair of tweezers 是一把镊子；these tweezers are… 接复数谓语；two pairs of tweezers 是两把镊子。',
 'a pair of tweezers；these tweezers are；pick up with tweezers。',
 'tweezers 是小型精细夹取工具，tongs 常指更大的夹具。a pair of tweezers is… 的中心是 pair；tweezers are… 的中心则是复数工具名。',
 ('She used tweezers to pick up the tiny model part.','她用镊子夹起了那个小模型零件。'),('These tweezers are too blunt for the delicate work.','这把镊子太钝，不适合做这种精细工作。'),sources=S('tweezers','tweezers'))
W('bicker','英 /ˈbɪkə/；美 /ˈbɪkər/','为小事斗嘴；争吵不休',
 '你一句我一句，为谁没关灯、谁又晚到之类的小事来回争，是 bicker。重点常在琐碎、反复，听着让人烦。',
 '接中古英语 bikere 争斗、小规模交战，可能与中古荷兰语 bicken 攻击及表示反复动作的 -er 有关。这里的历史 -er 不表示做事的人，现代整体认 bicker。',
 [['早期攻击、争斗材料 → 中古英语 bicker','具体远源有可能性分析，不当作确定的现代英语拼接'],['争斗 → 用言语反复争执','现代常说为小事斗嘴、挑嘴争吵']],
 'bicker about money 是为钱斗嘴；bicker over details 是为细节争执；bicker with someone 是与某人斗嘴。',
 'bicker about；bicker over；bicker with。',
 'argue 可以认真辩论或争论重大问题；bicker 常显得琐碎、没完没了。它通常带说话者嫌争执无益的评价。',
 ('They bicker about whose turn it is to wash up.','他们为轮到谁洗碗而斗嘴。'),('The committee should not bicker over every small detail.','委员会不该为每个小细节争吵不休。'),sources=S('bicker','bicker'))
W('bickering','英 /ˈbɪkərɪŋ/；美 /ˈbɪkərɪŋ/','斗嘴；为琐事反复争吵；爱争吵的',
 '一件小事翻来覆去吵，谁也不让谁，这种持续的斗嘴叫 bickering。把动作当成一整段令人厌烦的争执来看。',
 'bicker + 完整 -ing → bickering，词形保留。既可作动作形式，也可作争吵行为的名词，或修饰争吵中的人。',
 [['中古英语 bicker 争斗 → 言语上的斗嘴','从小规模交战转向琐碎反复的口角'],['bicker + -ing → bickering','现代可把反复斗嘴当作整体行为来谈']],
 'constant bickering 是不断斗嘴；bickering over money 是为钱争吵；bickering siblings 是吵个不停的兄弟姐妹。',
 'constant bickering；stop the bickering；bickering over details。',
 'a discussion 可以有建设性，bickering 常意味着反复口角、推进不大。作为行为名词时，常直接说 the bickering 或 constant bickering。',
 ('Their constant bickering spoiled the journey.','他们一路吵个不停，把旅行的兴致都搅坏了。'),('The bickering siblings finally agreed on a film.','吵个不停的兄弟姐妹终于就看哪部电影达成了一致。'),sources=S('bickering','bicker'))
W('knackered','英 /ˈnækəd/；美 /ˈnækərd/','累坏了、累瘫了；用坏、不能用了〔英式随意口语〕',
 '忙了一整天，瘫在沙发上连说话都嫌累，可以说 I’m knackered。旧机器彻底不行了，也能这样形容。',
 'knacker + 完整 -ed → knackered，词尾读 /d/。相关旧行业名涉及处理老病马等，动词后发展出使耗坏、使筋疲力尽；更早远源仍有不确定性。',
 [['旧 knacker 行业名 → 相应动词','早期具体行业词与后来的耗坏、使疲惫义相连，远源未定'],['knacker + -ed → knackered','过去分词形容词弱化为口语累坏、用坏']],
 'I’m knackered 是我累坏了；a knackered old car 是一辆用坏了的旧车。多见于熟人间随意聊天，语气比 tired 重。',
 'feel knackered；absolutely knackered；a knackered old car。',
 'tired 是中性常用词，knackered 更随意、更有累瘫的劲头。用于物品时，要按坏掉、磨损得不行理解。',
 ('I was completely knackered after moving all those boxes.','搬完那些箱子后，我彻底累瘫了。'),('Their knackered old van finally stopped working.','他们那辆破旧不堪的货车终于彻底开不动了。'),sources=S('knackered','knackered'))

def extend_lessons():
 extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_zks',ROOTS,WORDS)
 extend_lessons()
