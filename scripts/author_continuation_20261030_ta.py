"""Backfill common words in existing teaching families."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'B2591':dict(words=['seen'],label='不规则过去分词',note='see → saw → seen；seen 是过去分词，常用于完成时和被动式。'),
 'B2891':dict(words=['lightning'],label='闪电这一固定名词',note='lightning 与 light、旧 lightnen 变亮词族相连；它与现代 lightening 的拼写、用法分开。'),
 'A1741':dict(words=['accord','according','awake','awaken','awakening','crave','craving'],label='固定搭配、觉醒与强烈渴望',note='according 常见于 according to；awaken + -ing → awakening；crave 去末尾 e 加 -ing → craving。'),
 'A1760':dict(words=['deceased'],label='分词形容词的正式称人用法',note='decease + -ed → deceased，形成已故的、死者等正式表达。'),
 'A1740':dict(words=['heaven','heavenly'],label='-ly 形容词：天空、天堂及极美好的感觉',note='heaven + -ly → heavenly；这里 -ly 主要形成形容词，不能只按副词尾理解。'),
 'B4327':dict(words=['grocer','grocery'],label='经法语批量交易材料形成的商店词族',note='grocer、grocery 经法语 grossier、grosserie 等与 gross 的大量、整批历史词族相连；不是由现代 gross 恶心义直接派生。'),
}
W('seen','/siːn/','see 的过去分词：看见、见过、被看见',
 'I have seen it 是我见过它；It was seen 是它被看见。意思沿着 see 走，语法位置由过去分词这个形式决定。',
 'see 的不规则过去分词，经古英语及中古英语分词形式延续；末尾 -n 保留旧强变化动词分词材料，现代保留不规则变化。',
 [['古英语、中古英语看见词族的分词形式','保留强变化分词的形态'],['现代 see → saw → seen','原形、过去式、过去分词各有位置']],
 'have seen 表已经见过；be seen 表被看见。seen 也常用于表示经历的说法，如 the best film I’ve ever seen 我看过最好的电影。',
 'have never seen；be seen as；the last time I saw her。','saw 可作一般过去时谓语：I saw her；seen 通常需要 have、be 等相应结构，标准英语不说 I seen her 来代替一般过去时。',
 ('I have seen this film before.','我以前看过这部电影。'),('The village can be seen from the hill.','从山上能看见这个村庄。'))
W('according','英 /əˈkɔːdɪŋ/；美 /əˈkɔːrdɪŋ/','常用于 according to：据……所说；按照、根据',
 'according to 像给信息、安排贴一个依据标签：据谁所说，或者按照什么来做。',
 'accord 协调、一致 + -ing 的分词形式，逐渐固定在 according to 等搭配中。accord 更早经法语接一致、同心的词族。',
 [['accord + -ing','相符、一致的分词关系'],['according to 的固定化','与某依据相符 → 据、按照']],
 'according to the report 据报告所说；according to the plan 按计划；according to size 按大小。根据信息来源和根据规则是两类常用场景。',
 'according to the instructions；according to the weather forecast。','表达自己的意见一般用 in my opinion，不通常说 according to me；according to 常用来指出外部来源或依据。',
 ('According to the forecast, it will rain tomorrow.','据天气预报说，明天会下雨。'),('Arrange the books according to size.','把书按大小排列。'))
W('lightning','/ˈlaɪtnɪŋ/','闪电；闪电般的',
 '雷雨中天空突然亮起的一道电光。光闪先到眼前，雷声随后传来；lightning 说的是这道闪电、相关放电现象。',
 '联系旧 lightnen 使亮与 -ing 名词形式，也有承接古英语 lighting、亮光词形的分析；与 light 光同族。现代 lightning 与 lightening 分开使用。',
 [['light 光及旧 lightnen 使亮的相关词族','亮光、闪亮的动作名词材料'],['lightning 固定为专门名称','闪电、相应电气现象']],
 'a flash of lightning 一道闪电；a lightning strike 雷击；lightning speed 闪电般的速度。通常不可数，数一道时用 a flash、a bolt 等。',
 'thunder and lightning；a bolt of lightning。','lightning 是闪电，thunder 是雷声；lightening 则常是 lighten 变亮、减轻的 -ing 形式，多一个 e，不能随意换拼写。',
 ('A flash of lightning lit up the sky.','一道闪电照亮了天空。'),('We saw lightning in the distance before hearing the thunder.','我们先看见远处的闪电，随后才听见雷声。'),sources=['https://www.etymonline.com/word/lightning','https://en.wiktionary.org/wiki/lightning#English'])
W('deceased','/dɪˈsiːst/','已故的；死者〔正式〕',
 '在正式记录中，平静、客观地指已经去世的人。作名词时常见 the deceased，指文中提到的死者。',
 'decease 去世 + -ed 的过去分词形容词；decease 经法语接拉丁 decessus 离去、decedere 离开的词族，以离去表达死亡。',
 [['拉丁离去词族 → 法语、英语 decease','离去 → 去世'],['decease + -ed → deceased','已故的；再作名词指死者']],
 'a deceased relative 已故亲属；the deceased 死者。可作形容词，也可在正式叙述里以 the deceased 指一人或相关死者。',
 'the deceased person；her deceased parents。','dead 更普通直接；deceased 更正式。late 放在人物身份前也可说已故，如 her late husband，但句法习惯不同。',
 ('The letter belonged to her deceased grandfather.','这封信是她已故祖父的。'),('The report identifies the deceased by name.','报告注明了死者的姓名。'),sources=['https://www.etymonline.com/word/deceased','https://en.wiktionary.org/wiki/deceased#English'])
W('awakening','/əˈweɪkənɪŋ/','醒来；觉醒；猛然意识到',
 '从睡着到清醒，也从没看明白到突然明白。awakening 把这个醒过来的变化当作一个过程、经历来谈。',
 'awaken 唤醒、醒来 + -ing；awaken 与 awake 的旧英语词族相连。由生理醒来到思想觉醒的比喻发展很自然。',
 [['awake、awaken 的旧英语词族','不再睡着、恢复清醒'],['awaken + -ing → awakening','醒来这一过程；认识、意识的觉醒']],
 'a rude awakening 常指突然、令人不快地认清现实；a political awakening 政治意识的觉醒。也可作动词 awaken 的 -ing 形式。',
 'an awakening of interest；a rude awakening。','awake 常作醒着的或醒来；awakening 把变化当名词，或表示正在唤醒的动作。a rude awakening 不必真的被粗暴叫醒。',
 ('Leaving home was a rude awakening for him.','离家生活让他猛然认识到现实并不轻松。'),('The book sparked an awakening of interest in local history.','这本书唤起了人们对当地历史的兴趣。'))
W('crave','/kreɪv/','强烈渴望、迫切想要',
 '不是随口觉得还不错，而是特别想得到某样东西：很想吃甜食，也可以特别渴望关注、安静或认可。',
 '经中古英语 craven 接古英语 crafian 请求、要求、恳求，属于日耳曼本族词。由要求、恳求发展为现代的强烈渴望。',
 [['古英语 crafian → 中古英语 craven','请求、要求、恳求'],['现代 crave','强烈想得到、渴望满足']],
 'crave chocolate 特别想吃巧克力；crave attention 渴望关注；crave peace 渴望安宁。常直接接宾语。',
 'crave approval；crave something sweet。','want 可以只是想要；crave 通常把欲望、需求说得更强。desire 较正式，crave 更容易让人感到迫切。',
 ('After the long hike, I craved something salty.','长途徒步后，我特别想吃点咸的。'),('The child craved attention from the adults.','孩子很渴望得到大人的关注。'))
W('craving','/ˈkreɪvɪŋ/','强烈渴望；特别想吃某物的欲望',
 '那股很想得到的劲头，可以被当作一个东西来讲：a craving。一阵突然想吃某样东西的感觉很典型。',
 'crave 去词末 e 加 -ing，形成名词、分词；更早中古英语、古英语已有同族的请求、要求动作名词。',
 [['古英语、中古英语的请求动作名词词族','要求、迫切需求'],['现代 crave → craving','强烈想要 → 这股渴望本身']],
 'a craving for chocolate 对巧克力的强烈渴望；satisfy a craving 满足渴望。动词 crave 直接接对象，名词 craving 常接 for。',
 'food cravings；a sudden craving for something sweet。','crave 是动词，craving 作名词时可数，常说 a craving for；也能表示 crave 的进行动作，要按句子位置区分。',
 ('I had a sudden craving for noodles.','我突然特别想吃面条。'),('A small snack satisfied her craving for something sweet.','一小份点心满足了她想吃甜食的欲望。'))
W('heaven','/ˈhevən/','天堂、天国；天空〔文学等用法〕；极乐之地、极美好体验',
 '宗教里的天堂、天国；日常则能把特别幸福、享受的处境叫 heaven，像终于进入理想中的地方。',
 '经中古英语 heven、hevene 等接古英语 heofon 天空、天堂，属于日耳曼词族。更远来源仍有不同分析，不强定唯一原始画面。',
 [['古英语 heofon → 中古英语 heven 等','天空、天国'],['现代 heaven 的宗教、比喻用法','天堂；无比美好的处境']],
 'go to heaven 去天堂；be in heaven 感觉幸福极了；the heavens 可用文学口吻指天空。不同信仰、故事里的 heaven 观念并不完全相同。',
 'a little piece of heaven；the heavens above。','sky 是日常看到的天空；heaven 常联系宗教或极美好体验。haven 则是避风港、庇护处，虽相像却是另一个词。',
 ('The old painting shows angels in heaven.','那幅旧画描绘了天堂里的天使。'),('With a good book and a quiet room, she was in heaven.','有好书和安静的房间，她感觉幸福极了。'))
W('heavenly','/ˈhevənli/','天堂的、天上的；美妙至极的',
 '先是属于 heaven 的，后来也能用天堂般的美好来夸味道、声音或享受。',
 '与古英语 heofonlic 天上的、天堂的形容词相连，经中古英语延续；现代对应 heaven + -ly。这里的 -ly 主要是形容词材料。',
 [['古英语 heaven 相关词 + -lic','天上的、天堂的'],['中古英语 hevenly → heavenly','天堂的；引申为美妙至极的']],
 'heavenly bodies 天体；a heavenly voice 天籁般的声音；a heavenly smell 美妙的香味。日常称赞往往带夸张。',
 'heavenly music；taste heavenly。','heavenly 主要是形容词，因此 The cake tastes heavenly 是说蛋糕味道美妙；不能看到 -ly 就一律判为副词。',
 ('The garden smelled heavenly after the rain.','雨后的花园香气美妙极了。'),('The choir sang with heavenly voices.','合唱团唱出了天籁般的声音。'))
W('grocer','英 /ˈɡrəʊsə/；美 /ˈɡroʊsər/','食品杂货商；食品杂货店',
 '卖日常食物、家庭杂货的人，或其店铺。今天像街角食品杂货店；历史上却从批量买卖的商人发展而来。',
 '经盎格鲁法语 grosser、古法语 grossier 批发商，接大量、整批交易的 gross 相关材料。后来用途转向零售食品等，拼写形成 grocer。',
 [['法语 gros、grossier 等整批交易词族','大批量交易的商人'],['英语 grocer','批发商 → 食品杂货零售商、商店']],
 'the local grocer 当地杂货商；at the grocer’s 在食品杂货店。grocer’s 的所有格形式常省略 shop。',
 'a corner grocer；buy bread at the grocer’s。','grocer 是商人、店铺，groceries 是买回来的食品杂货；前者不直接当作一袋食物的名称。gross 的恶心义不是这条历史的来源。',
 ('The local grocer knows many customers by name.','当地杂货商能叫出许多顾客的名字。'),('I bought some fruit at the grocer’s.','我在食品杂货店买了些水果。'),sources=['https://www.etymonline.com/word/grocer','https://en.wiktionary.org/wiki/grocer#English'])
W('grocery','英 /ˈɡrəʊsəri/；美 /ˈɡroʊsəri/，也读 /ˈɡroʊʃəri/','食品杂货店；食品杂货〔通常复数 groceries〕',
 'grocer 是卖这些东西的人，groceries 是你买回家的食物、日用杂货；grocery store 则是卖它们的店。',
 '经中古英语 grocerye，与古法语 grosserie、grossier 批量交易、批发商词族相连。现代可按 grocer + -y 认识词形，但来源也有较早法语对应。',
 [['法语批量交易、商人词族 → 中古英语 grocerye','商人出售的货物'],['grocery、groceries 的现代分工','商店；通常用复数指食品杂货']],
 'do the grocery shopping 买食品杂货；a grocery store 食品杂货店；carry the groceries 把采购的食品杂货提走。单数 grocery 作店铺名在美式尤常见。',
 'a grocery list；a bag of groceries。','a grocery 是一家店的用法，groceries 常是采购的东西。grocery list 里单数 grocery 作修饰语，不表示清单只列一样东西。',
 ('I stopped at the grocery store on my way home.','我回家途中在食品杂货店停了一下。'),('Could you help me carry the groceries?','你能帮我提一下买回来的食品杂货吗？'),sources=['https://www.etymonline.com/word/grocer','https://en.wiktionary.org/wiki/grocery#English'])
def extend_lessons():
    extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
    save('continuation_20261030_ta',ROOTS,WORDS)
    extend_lessons()
