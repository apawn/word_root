"""Common informal forms, stark contrasts and familiar fantasy names."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
def S(word,base):
 a=['https://en.wiktionary.org/wiki/'+word+'#English','https://www.etymonline.com/word/'+base]
 if base=='freak':a.append('https://www.merriam-webster.com/dictionary/freak')
 if word=='freaking':a.append('https://www.merriam-webster.com/dictionary/freaking')
 if base=='sprite':a.append('https://www.merriam-webster.com/dictionary/sprite')
 if base=='perk':a.append('https://www.etymonline.com/word/perquisite')
 return a
EXISTING_ROOT_ADDITIONS={
 'B2552':dict(words='massacre massacres massacred'.split(),label='massacre：另源的大规模屠杀称呼',note='与 kill 比较词义，不由 kill 派生。massacre 名词、动词经法语借入，古法语有屠场、屠杀相关义；更远与拉丁肉铺名等的联系不确定。现代也有惨败、糟蹋的强烈比喻。'),
 'B2849':dict(words='firearm firearms'.split(),label='firearm → firearms：火药发射的武器名称',note='fire 火、燃烧 + arm 武器 → firearm；arm 在这里接法语、拉丁 arma 武器，不是现代胳膊义。整个复合名词末尾加 s，通常汉译枪械、火器。'),
 'C0503':dict(words='congratulations congrats'.split(),label='congratulations → congrats：祝贺的口语短称',note='congrats 缩略 congratulations，保留祝贺表达；更远接拉丁一起欢喜的词族，不把缩略后 -ts 误当成一个新的祝贺后缀。'),
 'B3813':dict(words='bro bros'.split(),label='bro → bros：兄弟称呼的短形式与朋友',note='bro 缩略 brother，既可说亲兄弟，也可为亲昵的哥们称呼；复数直接加 s → bros，词尾 /z/，不照搬 brother 的完整拼写。'),
 'B4038':dict(words='freak freaks freaked freaking'.split(),label='freak：奇异、着迷、失控与程度加强',note='freak 更远来源不明，早有突然奇想、异常事物等义，后来也说对某事着迷的人；freak out 是现代惊慌、失控表达。freaking 作加强语气词又是更粗俗词的委婉替代，不能只靠 -ing 解释完。'),
 'C1189':dict(words='perk perks'.split(),label='perks：额外福利；振作动词另有词线',note='福利 perk 缩略 perquisite，远接拉丁 perquirere 寻求、perquisitum 获得之物；perk up 振作的动词可能联系栖鸟、抬起等另一条词线，不由福利名词直接派生。'),
 'B3700':dict(words='stark'.split(),label='stark：硬、严厉到光秃、鲜明强烈',note='stark 接古英语 stearc，远处与 stern 严厉形容词同族，不是船尾 stern 那条线。现代常用 stark contrast 强烈反差、stark reality 严酷现实；光秃义也强调毫无遮掩。'),
 'B3940':dict(words='gnome gnomes'.split(),label='gnome：与 dwarf 比较的民间小精灵名',note='与 dwarf 比较传说形象，不从 dwarf 派生。gnome 经法语接近代拉丁 gnomus，曾用于地之精灵；可能有希腊居于地下的构词背景但不确定，现代常见花园装饰小矮人。'),
 'B3228':dict(words='goblin goblins'.split(),label='goblin：与 elf 比较的小妖精名',note='与 elf 比较传说角色，不由 elf 派生。goblin 接诺曼法语 gobelin，更远有不同分析，不能把形似词、现代游戏设定拼成确定历史。'),
 'C1395':dict(words='sprite sprites'.split(),label='sprite → sprites：精灵与图像精灵',note='sprite 与 spirit 来自同一古法语、拉丁 spiritus 气息、精神词族，是不同传入、变化的形式；现代计算机里用 sprite 指能独立显示、移动的图像对象，名称借来精灵的形象。'),
 'C0257':dict(words='unicorn unicorns'.split(),label='unicorn → unicorns：一只角的传说动物',note='经法语接拉丁 unicornis 有一只角的，uni- 一 + cornu 角的材料；corn- 在这里是角，不是玉米词义。复数给整个名称加 s。'),
}
MASSACRE=[['古法语 macacre、macecle 等：屠场、屠杀 → 法语 massacre、massacrer','更远来源不明，可能联系拉丁屠场、肉铺材料'],['英语借入名词、动词 massacre → massacres、massacred','主要为大规模、残酷杀戮；也有强烈比喻用法']]
FREAK=[['英语 freak 早有突然奇想、反常事物的用法','更远来源不确定，不把一个可能祖先当已证实'],['后来有人物称呼、对某事着迷用法，以及 freak out 惊慌、失控','freaking 加强语气时还有委婉替代粗俗词的来源']]
GNOME=[['法语 gnome ← 近代拉丁 gnomus，曾用于地之精灵','可能接希腊居于地中的构词材料，但分析不确定'],['传说精灵名进入儿童故事 → 花园小矮人雕像','现代 gnome 的开头 g 不读；复数 gnomes']]
GOBLIN=[['诺曼法语 gobelin 等 → 英语 goblin','更远有多种分析，缺乏可确定的单一路线'],['小妖精、淘气或可怕的传说生灵 → 现代故事、游戏角色名','goblins 是规则复数；不同作品对外形、性格有不同设定']]
SPRITE=[['拉丁 spiritus 气息、精神 → 古法语 espirit、esprit 等','英语 sprite 与 spirit 是同源的不同形式'],['sprite 用于精灵、幽灵等 → 现代图形计算中的图像对象名','现代 sprites 是复数；图像精灵的具体显示行为由程序决定']]
W('massacre','英 /ˈmæsəkə/；美 /ˈmæsəkɚ/','大屠杀；屠杀；惨败、糟蹋〔强烈比喻〕',
 'massacre 比普通 kill 强烈，常说许多无法有效抵抗的人或动物遭到残酷杀害。写历史、新闻时会遇见这个词。',
 '名词、动词经法语 massacre、massacrer 借入；古法语有屠场、屠杀相关义。更远来路不定，不能把它简单拆成现代 mass 大量加一个后缀。',MASSACRE,
 'a massacre 是一次屠杀；survivors of a massacre 是屠杀幸存者；比喻用法可夸张说被打得惨败，或把作品演坏。',
 'a massacre；survivors of a massacre；an account of a massacre。',
 'massacre 有强烈的残酷、大量杀戮意味，不是每次单个 kill 都能直接换成它；比喻用法要由上下文判断。',
 ('The chapter describes a massacre and its aftermath.','这一章描写一次屠杀及其后果。'),('The museum records the names of those who died in the massacre.','博物馆记录了那次屠杀中遇难者的名字。'),sources=S('massacre','massacre'))
W('massacres','英 /ˈmæsəkəz/；美 /ˈmæsəkɚz/','屠杀〔复数〕；屠杀、使惨败〔第三人称单数〕',
 '文章谈到多次屠杀，可以用 massacres。这个词按一次次事件来数，语气仍很强烈。',
 'massacre 词尾已有 e，直接加 -s → massacres，读音后缀 /z/；也与第三人称单数动词同形。',MASSACRE+[['massacre + -s → massacres','多次屠杀或单数主语的动词，词尾 /z/']],
 'accounts of massacres 是屠杀记述；survivors of massacres 是屠杀幸存者；historical massacres 是历史上的屠杀事件。',
 'historical massacres；accounts of massacres；survivors of massacres。',
 'massacres 不是在数每个死者，而是通常把事件按一次次来谈；具体人数要另外表达。',
 ('The book examines several historical massacres.','这本书研究了几次历史上的屠杀。'),('The archive contains accounts of massacres from different periods.','档案中保存了不同时期的屠杀记述。'),sources=S('massacres','massacre'))
W('massacred','英 /ˈmæsəkəd/；美 /ˈmæsəkɚd/','遭到屠杀；屠杀了；被打得惨败〔比喻〕',
 'were massacred 常说一群人遭到屠杀；比赛里夸张说被打得毫无还手之力，也可能借这个强烈词。',
 'massacre 去词尾不发音 e + -ed → massacred，实际拼写只新增 d，但后缀仍是 -ed；末尾读 /d/。',MASSACRE+[['massacre 去 e + -ed → massacred','动词过去式、过去分词，保留强烈语气']],
 'were massacred 是遭屠杀；massacred in a match 可夸张说比赛惨败；用被动式时，主语是遭遇这一结果的一方。',
 'were massacred；massacred in the conflict；massacred in the final。',
 '历史、新闻中的字面义非常沉重；体育中的同形用法可能是夸张比喻，要靠完整语境判断。',
 ('The memorial names the villagers who were massacred.','纪念碑上刻着遭屠杀村民的名字。'),('The article recounts how the prisoners were massacred.','文章讲述了那些俘虏如何遭到屠杀。'),sources=S('massacred','massacre'))
W('firearms','英 /ˈfaɪərɑːmz/；美 /ˈfaɪrɑrmz/','枪械、火器〔复数〕',
 'firearms 把枪械按件、按类来谈。名字里的 fire 是发射所用的燃烧力量，arm 在这里是武器。',
 'fire + arm 武器 → firearm，再加 -s → firearms。arm 的武器义接法语、拉丁 arma，不能把这里的 arms 解释成胳膊。',
 [['英语 fire + arm 武器 → firearm','复合词以燃烧、发射的武器为命名关系'],['firearm + -s → firearms','整个名词末尾加复数，词尾 /mz/']],
 'antique firearms 是古董火器；a collection of firearms 是一批枪械收藏；firearms in a museum 是博物馆里的火器。',
 'antique firearms；a collection of firearms；firearms on display。',
 'arms 泛说武器，firearms 是其中火器这一类；不能因为都写 arm，就把 bows 等一概叫 firearms。',
 ('The museum has a collection of antique firearms.','博物馆收藏了一批古董火器。'),('The catalogue describes the firearms on display.','目录介绍了展出的火器。'),sources=S('firearms','firearm'))
W('congrats','英、美 /kənˈɡræts/','祝贺、恭喜〔非正式〕',
 '朋友拿到新工作，你随手发一句 Congrats!，就是“恭喜！”比完整 congratulations 更轻松简短。',
 'congratulations 的口语缩略 → congrats，保留祝贺语气和复数样貌；不是在英语里另造一个表示祝贺的 -ts 后缀。',
 [['congratulation 祝贺 → congratulations 祝贺表达','名词复数常被独立用于向人道喜'],['congratulations 缩略 → congrats','日常消息、口头祝贺的简短形式']],
 'Congrats on your new job! 是恭喜获得新工作；Congrats to the team! 是祝贺这支团队。',
 'Congrats on your new job!；Congrats to you both!；Many congrats!。',
 'congrats 很适合熟人消息；更正式的贺信可用 congratulations。说祝贺某事时常接 on。',
 ('Congrats on your new job!','恭喜你获得新工作！'),('She sent a card that simply said, “Congrats!”','她寄来一张卡片，上面只写着：“恭喜！”'),sources=S('congrats','congrats'))
W('bros','英 /brəʊz/；美 /broʊz/','兄弟们；哥们、男性朋友〔口语复数〕',
 '跟几个熟悉的男性朋友一起玩，口语可以叫他们 bros。不一定是同父母的亲兄弟。',
 'bro 缩略 brother，进入亲昵称呼后加 -s → bros；元音后读 /z/，拼写只加 s。',
 [['brother 兄弟 → 缩略 bro','亲属称呼也能借给熟悉的男性朋友'],['bro + -s → bros','口语复数，读 /brəʊz/、/broʊz/']],
 'my bros 是我的哥们；two bros 可能是两位兄弟或两位哥们；hang out with his bros 是和他的哥们一起玩。',
 'my bros；two bros；hang out with the bros。',
 'bro、bros 语气随意，称呼关系也有群体差异；给不熟悉的人正式介绍身份时，friends、brothers 通常更明确。',
 ('He spent the weekend with his bros.','他周末和哥们一起过。'),('The two bros opened a small café together.','那两位哥们合开了一家小咖啡馆。'),sources=S('bros','bro'))
W('freaks','英、美 /friːks/','怪人〔可能冒犯〕；……迷；使惊慌、失控',
 'fitness freaks 是健身特别上心的人；it freaks me out 则是它把我吓坏了。先看是在说人，还是说心理反应。',
 'freak + -s → freaks，/k/ 后读 /s/；作复数人物名词或第三人称单数动词。freak 早有奇想、反常事物义，现代又有着迷的人、失控反应等用法。',FREAK+[['freak + -s → freaks','名词复数和第三人称单数同形，词尾 /ks/']],
 'fitness freaks 是健身迷；control freaks 是控制欲很强的人；freaks someone out 是把某人吓坏、弄得不知所措。',
 'fitness freaks；control freaks；freaks me out。',
 '直接把别人叫 freaks 可能是侮辱；自称或熟人说 fitness freaks 有时是夸张自嘲。搭配会改变语气。',
 ('We are both fitness freaks.','我们俩都是健身迷。'),('That strange noise freaks me out.','那阵怪声把我吓得不行。'),sources=S('freaks','freak'))
W('freaked','英、美 /friːkt/','吓坏了、惊慌失控了〔常接 out〕',
 '突然发现东西不见了，人一下慌起来，就可以说 freaked out。不是冷静地觉得有点奇怪。',
 'freak + -ed → freaked，原来已有元音字母组合 ea 和末尾 k，直接加 -ed；/k/ 后后缀读 /t/。',FREAK+[['freak + -ed → freaked','现代过去式、过去分词；常见 freaked out']],
 'freaked out 是惊慌、失控；freaked someone out 是吓坏、弄慌某人；a little freaked out 可说有点被吓住。',
 'freaked out；freaked me out；a little freaked out。',
 'I freaked out 是我慌了；it freaked me out 是它把我吓慌了，谁是反应者要看宾语。',
 ('I freaked out when I could not find my passport.','找不到护照时，我一下就慌了。'),('The sudden noise freaked the cat out.','突然的声响把猫吓坏了。'),sources=S('freaked','freak'))
W('freaking','英、美 /ˈfriːkɪŋ/','正在惊慌、使失控〔常接 out〕；非常、真是〔非正式加强语气〕',
 'I’m freaking out 是我快慌坏了；that’s freaking amazing 是那真是太棒了。第二个不是在说某人正在做一个动作。',
 '动词形式是 freak + -ing → freaking；加强语气的 freaking 则有替代更粗俗加强词的委婉表达背景，不能只用动词加 -ing 概括全部用法。',FREAK+[['freak + -ing：正在失控；另有委婉加强词 freaking','现代同形，两种句法和语气分开掌握']],
 'freaking out 是惊慌；freaking someone out 是使某人慌乱；freaking brilliant、freaking cold 分别是特别棒、冷得要命。',
 'freaking out；freaking me out；freaking brilliant。',
 '加强词 freaking 仍带随意、情绪化语气；正式陈述用 very、extremely 等通常更合适。',
 ('You are freaking me out with that story.','你那个故事说得我都发毛了。'),('That was freaking brilliant!','那真是太棒了！'),sources=S('freaking','freak'))
W('perks','英 /pɜːks/；美 /pɝks/','额外福利、附带好处；振作、竖起〔动词常接 up〕',
 '工作除了工资，还有免费午餐、灵活时间，这些附带好处可以叫 perks。它把“正餐之外的小甜头”说出来。',
 '福利名词 perk 缩略 perquisite，远接拉丁 perquirere 寻求及 perquisitum 获得之物；perk + -s → perks，/k/ 后 /s/。perk up 动词另有抬起、振作词线，不能从福利直接推出。',
 [['拉丁 perquirere 寻求 → perquisitum 获得之物 → perquisite 额外收益','perquisite 缩略为福利名词 perk'],['perk + -s → perks；另有 perk up 振作动词','福利复数与第三人称单数同形，来源不完全相同']],
 'job perks 是工作福利；one of the perks 是附带好处之一；perks up 是振作起来、变精神。',
 'job perks；one of the perks；perks up。',
 'perks 常突出工资、主要所得之外的额外好处；perk up the room 还可说让房间更有生气，不是发福利给房间。',
 ('Flexible hours are one of the perks of the job.','灵活工时是这份工作的福利之一。'),('The dog perks up when it hears the door open.','狗一听见开门声就来了精神。'),sources=S('perks','perk'))
W('stark','英 /stɑːk/；美 /stɑrk/','鲜明强烈的；严酷的；光秃、简陋的；完全的',
 '两种颜色、两种处境摆在一起，反差硬邦邦地撞进眼里，就是 a stark contrast。光秃房间、严酷现实也有这种无遮掩的感觉。',
 '古英语 stearc 有坚硬、强壮、严厉等义；后来有完全、光秃等用法。与 stern 严厉的形容词远同族，不同于船尾 stern。',
 [['古英语 stearc：坚硬、强壮、严厉等 → 英语 stark','更远接僵硬的古老词族，与 stern 严厉义相关'],['stark 有完全、光秃等发展；现代常见强烈反差、严酷现实','用旧义的硬、严峻帮助理解，不把现代搭配都编成唯一时间链']],
 'a stark contrast 是强烈反差；stark reality 是严酷现实；a stark room 是光秃简陋的房间；stark naked 是一丝不挂。',
 'a stark contrast；stark reality；a stark room。',
 'stark contrast 强调差别鲜明、显眼；ordinary difference 只说有差别，没有同样强烈的视觉、情绪效果。',
 ('The two photographs show a stark contrast.','这两张照片呈现出鲜明反差。'),('The room was stark, with only a bed and a chair.','房间很简陋，只有一张床和一把椅子。'),sources=S('stark','stark'))
W('gnome','英 /nəʊm/；美 /noʊm/','传说中的小矮人、地精；花园小矮人雕像',
 '花园里戴尖帽子的小矮人摆件，常叫 a garden gnome。名字先来自传说精灵，后来才借给它的装饰像。',
 '经法语 gnome 接近代拉丁 gnomus，曾用于地之精灵；可能有希腊居于地中的构词背景，但分析不确定。现代开头 gn 读 /n/，g 不单独发音。',GNOME,
 'a garden gnome 是花园小矮人雕像；a woodland gnome 是故事中的林间小精灵；a ceramic gnome 是陶瓷小矮人摆件。',
 'a garden gnome；a ceramic gnome；a gnome in a story。',
 'gnome 可说传说角色，也可说它的雕像；garden gnome 常是装饰物，不必理解成园子里住着真人。',
 ('A painted gnome stood beside the flowerpot.','花盆旁摆着一个彩绘小矮人。'),('The story begins with a gnome living under a hill.','故事从一个住在山丘下的小地精讲起。'),sources=S('gnome','gnome'))
W('gnomes','英 /nəʊmz/；美 /noʊmz/','小地精；花园小矮人雕像〔复数〕',
 '门前摆了一排尖帽子小矮人，是 garden gnomes；童话里的几个小地精，也用这个复数。',
 'gnome + -s → gnomes，原词末尾 e 不发音，/m/ 后后缀读 /z/；开头 g 依旧不读。',GNOME+[['gnome + -s → gnomes','多名传说精灵、多个小矮人摆件，读 /nəʊmz/、/noʊmz/']],
 'garden gnomes 是花园小矮人摆件；painted gnomes 是彩绘小矮人；gnomes in a fairy tale 是童话中的地精。',
 'garden gnomes；painted gnomes；a row of gnomes。',
 'gnomes 是普通复数名词；不同作品对精灵的身高、性格、能力可能各有设定，不能把一个游戏的设定当作词的全部含义。',
 ('Three garden gnomes stood near the gate.','门边摆着三个花园小矮人。'),('The children drew gnomes with bright red hats.','孩子们画了戴鲜红帽子的小地精。'),sources=S('gnomes','gnome'))
W('goblin','英 /ˈɡɒblɪn/；美 /ˈɡɑblɪn/','小妖精、哥布林〔民间故事、奇幻作品中的角色〕',
 '故事里淘气、阴森或惹麻烦的小妖怪，常会叫 goblin。现代奇幻作品又给它画出各种不同形象。',
 '英语借诺曼法语 gobelin 等形式，更远来路有不同分析；不宜把 -lin 当成现代英语通用的小妖怪后缀。',GOBLIN,
 'a goblin in a fairy tale 是童话里的小妖精；a goblin king 是哥布林王；a mischievous goblin 是淘气的小妖精。',
 'a mischievous goblin；a goblin king；a goblin in a story。',
 'goblin、elf、gnome 在作品里可能被分为不同族类；日常学习先认常见形象，不把某一种设定当作所有英语故事的规则。',
 ('A goblin appeared at the mouth of the cave.','洞口出现了一个小妖精。'),('The child dressed as a goblin for the play.','孩子在戏里装扮成一个小妖精。'),sources=S('goblin','goblin'))
W('goblins','英 /ˈɡɒblɪnz/；美 /ˈɡɑblɪnz/','小妖精、哥布林〔复数〕',
 '洞里、森林里不止一个 goblin，就用 goblins。复数只管数量，角色长什么样仍看具体故事。',
 'goblin + -s → goblins，/n/ 后读 /z/；基础词是经法语借入的精灵名，直接加现代英语复数。',GOBLIN+[['goblin + -s → goblins','多名小妖精，词尾 /nz/']],
 'a band of goblins 是一伙小妖精；goblins in the forest 是森林里的小妖精；stories about goblins 是小妖精故事。',
 'a band of goblins；goblins in the forest；stories about goblins。',
 'goblins 是同一类名称的复数；goblin king 的 goblin 通常仍用单数形态作前部修饰。',
 ('The tale describes goblins hiding in the forest.','故事描写小妖精藏在森林里。'),('A band of goblins guarded the bridge in the game.','游戏中有一伙哥布林守着桥。'),sources=S('goblins','goblin'))
W('sprite','英、美 /spraɪt/','精灵、小仙子；图像精灵〔计算机图形〕',
 '童话里轻巧的小精灵是 a sprite；游戏屏幕上能单独显示、移动的小图像，也叫 sprite，中文常译“精灵”。',
 '经古法语 espirit、esprit 等接拉丁 spiritus 气息、精神；sprite 与 spirit 同源，是不同形式。现代图形领域把名称借给独立图像对象，不是从现代 spirit 随手删字母造出的词。',SPRITE,
 'a woodland sprite 是林间精灵；a character sprite 是角色图像精灵；a sprite animation 是精灵动画。',
 'a woodland sprite；a character sprite；sprite animation。',
 '计算机 sprite 是图像对象，可能表现一个角色或别的物件；不是每幅普通背景图都自动叫 sprite。',
 ('A woodland sprite guides the traveller in the tale.','故事里，一位林间精灵为旅人引路。'),('The sprite moves across the screen when the key is pressed.','按下按键时，图像精灵就在屏幕上移动。'),sources=S('sprite','sprite'))
W('sprites','英、美 /spraɪts/','精灵；图像精灵〔复数〕',
 '童话里的几个精灵，或游戏画面里几个分开活动的图像对象，都能是 sprites。先看场景再翻译。',
 'sprite + -s → sprites；基础词末尾 e 不发音，末音 /t/ 后加 /s/，词尾 /ts/。',SPRITE+[['sprite + -s → sprites','多名故事精灵或多个图像对象']],
 'forest sprites 是森林精灵；animated sprites 是动画精灵图像；character sprites 是角色精灵图像。',
 'forest sprites；animated sprites；character sprites。',
 'sprite 的 i 在这里读 /aɪ/，和 spirit 的首元音不同；同源不表示现代每个音、每个意思都相同。',
 ('The book is full of sprites and talking animals.','这本书里满是精灵和会说话的动物。'),('The artist drew several sprites for the game.','画师为游戏画了几个精灵图像。'),sources=S('sprites','sprite'))
W('unicorns','英 /ˈjuːnɪkɔːnz/；美 /ˈjunɪkɔrnz/','独角兽〔复数〕',
 '故事里额上长着一根角、现代图画常画成马样的传说动物，是 unicorns。名字最直观的部分就是“一只角”。',
 '法语 unicorne 接拉丁 unicornis 有一只角的，uni- 一 + cornu 角的材料；英语 unicorn 加 -s → unicorns，/n/ 后读 /z/。',
 [['拉丁 uni- 一 + 角词族 → unicornis 有一只角的','经晚期拉丁语、法语相关形式进入英语 unicorn'],['unicorn + -s → unicorns','多只独角兽；古代形象不必与现代白马图画完全一样']],
 'pictures of unicorns 是独角兽图画；stories about unicorns 是独角兽故事；toy unicorns 是独角兽玩具。',
 'pictures of unicorns；stories about unicorns；toy unicorns。',
 '这里的 uni- 是一，corn- 接角，不能看成否定 un- 或把 corn 理解为玉米；外形相似的字母块要按来源区分。',
 ('The notebook cover is decorated with unicorns.','笔记本封面上装饰着独角兽图案。'),('She loves stories about dragons and unicorns.','她喜欢有关龙和独角兽的故事。'),sources=S('unicorns','unicorn'))
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_zix',ROOTS,WORDS)
 extend_lessons()
