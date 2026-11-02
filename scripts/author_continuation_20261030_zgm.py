"""Vexation, nettle-like irritation, friction and goading."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
def S(word,base):
 return ['https://en.wiktionary.org/wiki/'+word+'#English','https://www.etymonline.com/word/'+base]
EXISTING_ROOT_ADDITIONS={
 'C1607':dict(words='vex vexes vexed vexing vexingly vexation vexations vexatious'.split(),label='vex：从颠簸、扰动到令人烦恼',note='拉丁 vexare 接 vehere 搬运的分词相关材料，有猛烈摇动、侵扰等义，经法语入英语。抽象烦扰义在借入前已有，不能说现代英语从 vehicle 车辆造出了 vex。'),
 'A1849':dict(words='nettle nettles nettled nettling nettlesome'.split(),label='nettle：荨麻扎人到言语惹人不快',note='植物名承古英语 netele，远源未定，纤维与捆绑材料的联系只是可能分析；动词由植物名发展，很早也有激怒义，nettlesome 接 -some。'),
 'C0157':dict(words='chafe chafes chafed chafing'.split(),label='chafe：发热、磨擦与不耐烦分支',note='经法语 chaufer 接拉丁 calefacere 使热；英语抽象激起、不快的部分记录很早，不能一律排成先磨伤皮肤再有烦躁。'),
 'B3316':dict(words='needle needles needled needling'.split(),label='needle：针刺意象与反复挖苦',note='针名词承古英语，动词由名词发展；挑衅、挖苦义可能经过讨价还价、咬住不放的旧用法，不把现代画面写成唯一确定演变步骤。'),
 'A1741':dict(words='goad goads goaded goading'.split(),label='goad：像尖棒催牛一样刺激、逼出行动',note='古英语 gad 是尖头器物、赶牛棒；英语动词由名词转用，最早动词记录已是刺激行动的抽象义，字面动词记录反而较晚。'),
}
VEX=[['拉丁 vehere 搬运的分词相关形式 vexus 等 → vexare','猛烈摇动、颠簸，并有烦扰、侵扰的抽象义'],['法语 vexer → 英语 vex','使不快、使困扰；vexed question 后来也指争论不休、棘手的问题']]
VEXATION=[['拉丁 vexare → vexatio、vexationem','烦扰、困苦等动作、状态名词'],['法语 vexacion 或直接拉丁借入 → vexation','早期有侵扰、烦恼，后来也命名令人烦恼的事；不是现代英语 vex 加完整 -ation 的唯一历史']]
NETTLE=[['古英语 netele → 中古英语 netle → nettle','带刺毛的荨麻，远源未定，纤维、捆绑材料联系尚不确定'],['植物名 → 动词 nettle','用荨麻刺打，也很早用于激怒、惹不快；nettlesome 进一步写烦人的性质']]
CHAFE=[['拉丁 calere 热 + facere 做 → calefacere；法语 chaufer','使热、暖起来，连接俗拉丁形式含重建材料'],['中古英语 chaufen → chafe','发热、激起情绪与摩擦等支线，磨伤皮肤义后来明确；不能把所有抽象义都放到最后']]
NEEDLE=[['古英语 nædl → needle','缝纫针，联系缝、纺的旧词族，外形再命名松针、指针等'],['针名词 → needle 动词 → 挑衅、挖苦','戳刺意象有助理解；现代激怒义可能经过讨价还价等旧用法']]
GOAD=[['古英语 gad → goad 名词','尖头器物，尤其赶牛的尖棒；远源比较材料有不确定性'],['名词 → goad 动词','最早动词记录已有煽动、刺激行动义，字面用棒赶的动词记录较晚']]
W('vex','/veks/','使烦恼、不快；使困扰',
 '一件事一直没解决，越想越让人烦，它会 vex you。更早的词义有猛烈摇动、侵扰，像把平静的心绪颠得不安生。',
 '经古法语 vexer 来自拉丁 vexare；与 vehere 搬运的分词相关形式相连，抽象烦扰义在拉丁语中已有。现代不用 vehicle 逐字改造出 vex。',VEX,
 'vex someone 使某人不快；a question that continues to vex experts 继续困扰专家的问题。',
 'do not let it vex you；vex the authorities。',
 'vex 比日常 annoy 常显得更书面，可以是恼人，也可以是难题持续困扰；不只等于让人大发雷霆。',
 ('Don’t let a small delay vex you.','别让一点耽搁把自己弄得心烦。'),('The question continues to vex researchers.','这个问题仍然困扰着研究者。'),sources=S('vex','vex'))
W('vexes','/ˈveksɪz/','使烦恼、使困扰〔第三人称单数〕',
 '拖延一直没说明白，问题总压在心里，叫 it vexes me。它可以写恼火，也可以写难题带来的持续困扰。',
 'vex + -es，/s/ 后读 /ɪz/；x 在词里读 /ks/，整体末尾为 /ksɪz/。',VEX+[['vex + -es → vexes','它使人烦恼；问题使人持续困扰']],
 'vexes me 使我烦恼；vexes policymakers 困扰决策者。',
 'a problem that vexes us；what vexes her most。',
 'vexes 和 puzzles 可以交叠，前者更容易带烦扰、不快；puzzles 也可只是让人好奇地琢磨。',
 ('What vexes her most is the lack of a clear answer.','最让她烦恼的是没有明确答复。'),('The problem vexes even experienced engineers.','这个问题连经验丰富的工程师也感到棘手。'),sources=S('vexes','vex'))
W('vexed','/vekst/','烦恼、不快的；棘手、争论不休的；使烦恼了',
 '人可以因反复受阻而 vexed；a vexed question 则常是各方争来争去、一直难解决的问题，不是问题自己在生气。',
 'vex + 完整 -ed，/s/ 后读 /t/，合成 /kst/ 结尾；分词形容词可写人的烦恼，也发展出问题棘手、争论不休的用法。',VEX+[['vex + -ed → vexed','感到烦恼；或问题长期未解决、引发争论']],
 'a vexed question 争论不休的难题；vexed by delays 因拖延烦恼。',
 'looked vexed；the vexed issue of funding。',
 'a vexed question 不只说明题目难做，还常指意见分歧、反复讨论；a difficult calculation 可以只是计算复杂。',
 ('She looked vexed by the repeated interruptions.','反复被打断，让她显得很不快。'),('They returned to the vexed question of who should pay.','他们又回到那个争论不休的问题：到底该谁付钱。'),sources=S('vexed','vex'))
W('vexing','/ˈveksɪŋ/','令人烦恼、棘手的；正在使困扰',
 '事情卡住，既费神又不好解决，就可以叫 a vexing problem。它写的是问题带给人的烦扰。',
 'vex + -ing；动作形式也作形容词。x 已表示 /ks/，直接接 -ing，不双写 x。',VEX+[['vex + -ing → vexing','使困扰的过程；或令人烦恼的性质']],
 'a vexing problem 棘手问题；a vexing delay 恼人的耽搁。',
 'particularly vexing；a vexing inconsistency。',
 'vexing 多写事情让人烦，vexed 可写人感到烦；但 vexed question 是问题引争议的固定用法，不能套成人才用 -ed 的绝对规则。',
 ('The team faced a vexing problem with no obvious solution.','团队遇到一个棘手问题，看不出明显解法。'),('The repeated failures were vexing everyone.','接连失败正让每个人心烦。'),sources=S('vexing','vex'))
W('vexingly','/ˈveksɪŋli/','令人烦恼、不快地',
 '原本只想要个清楚答复，却偏偏含糊得让人烦，是 vexingly unclear。副词把听者受到的烦扰加进描述。',
 'vexing + -ly；内层 vex + -ing，外层把令人烦的性质用于程度、方式。',VEX+[['vex → vexing → vexingly','使不快的性质，转成令人烦的程度、方式']],
 'vexingly unclear 不清楚得令人烦恼；vexingly difficult 难得让人烦。',
 'vexingly incomplete；vexingly slow。',
 'vexingly 说事情造成烦扰，in vexation 说人自己带着烦恼做出反应；两种表达的视角不同。',
 ('The instructions were vexingly unclear.','说明不清不楚，令人烦恼。'),('The answer remained vexingly out of reach.','答案始终找不到，令人心烦。'),sources=S('vexingly','vex'))
W('vexation','/vekˈseɪʃən/','烦恼、不快；烦心事',
 '事情一再不顺，人心里那份恼意叫 vexation；把造成这份恼意的事单独指出来，也可说 a vexation。',
 '接法语 vexacion 或直接拉丁 vexatio、vexationem；和 vex 同族，但名词有独立借入历史，不能只按现代 vex + -ation 推出全部过程。',VEXATION,
 'in vexation 烦恼、不快地；to my vexation 让我烦恼的是；a source of vexation 烦恼的来源。',
 'a look of vexation；a constant vexation。',
 'vexation 是较书面的烦恼、不快，anger 范围更广、更直接；日常小烦恼用 annoyance 也常自然。',
 ('She sighed in vexation when the screen froze again.','屏幕又卡住，她烦恼地叹了口气。'),('The broken latch was a constant vexation.','坏掉的门闩一直让人烦心。'),sources=S('vexation','vexation'))
W('vexations','/vekˈseɪʃənz/','烦心事；令人不快的问题〔复数〕',
 '一件件小事绊住生活，单独拿出来数，是 vexations；情绪整体通常还是不可数 vexation。',
 'vexation + 复数 -s，读 /z/；借入名词发展出可数的烦恼来源，再有复数。',VEXATION+[['vexation + -s → vexations','多个导致烦扰、不快的事物']],
 'minor vexations 小烦恼；daily vexations 日常烦心事；a series of vexations 一连串烦心事。',
 'the vexations of travel；small domestic vexations。',
 'vexations 在现代通常较书面；日常也可说 annoyances、hassles，但 hassles 更有来回折腾的口语感。',
 ('She tried to laugh off the small vexations of the journey.','她试着一笑置之，不计较旅途中的小烦恼。'),('The diary records the daily vexations of running the shop.','日记记下了经营这家店的日常烦心事。'),sources=S('vexations','vexation'))
W('vexatious','/vekˈseɪʃəs/','令人烦恼、麻烦不断的；带滋扰性的',
 '事情反复纠缠、耗神，却不把问题解决，便可形容为 vexatious。它比简单说 difficult 更突出烦扰、折腾。',
 '联系 vexation + -ous，形成 vexatious，-ation 与 -atious 是同族名词、形容词的对应外形；不把整个词机械拆成 vex + 一个随处可用的 -atious。',VEXATION+[['vexation 的同族基底 + -ous → vexatious','带烦扰、造成麻烦的性质']],
 'a vexatious problem 烦人的难题；vexatious demands 纠缠不休的要求；vexatious complaints 带滋扰性的投诉。',
 'a vexatious delay；vexatious correspondence。',
 'vexatious 用在投诉、诉讼语境还可能带滋扰、滥用程序等专门含义；普通阅读先看它是否在评价令人烦扰，不能把任何投诉都这样叫。',
 ('The new rule created a series of vexatious problems.','新规则带来了一连串烦人的问题。'),('The committee spent hours dealing with vexatious demands.','委员会花了几个小时处理那些纠缠不休的要求。'),sources=S('vexatious','vexatious'))
W('nettle','/ˈnetəl/','荨麻；刺痛；惹恼、刺得人不快',
 '荨麻有会扎人的刺毛，所以 nettle 作动词很形象：一句话像小刺扎来，把人惹得不舒服。植物名和惹恼义确实属于同一词族。',
 '植物名承古英语 netele，远源未定；动词由名词转用，很早已有刺打与惹恼义。可能的纤维、捆绑联系不当定论。',NETTLE,
 'a stinging nettle 刺人的荨麻；nettle someone with a remark 一句话刺得某人不快。',
 'nettle leaves 荨麻叶；grasp the nettle 勇敢处理棘手问题。',
 'nettle 作动词常像一句小刺话激出不快，encourage 则是鼓励；同样谈刺激行动，前者通常带不舒服的感觉。',
 ('A nettle brushed against my ankle.','一棵荨麻擦到了我的脚踝。'),('Such dismissive remarks are bound to nettle him.','这种轻慢的话肯定会让他不快。'),sources=S('nettle','nettle'))
W('nettles','/ˈnetəlz/','荨麻〔复数〕；刺痛、惹恼〔第三人称单数〕',
 '路边一丛扎人的植物是 nettles；一句轻慢的话戳得人心里不舒服，动词也可用 nettles。',
 'nettle + -s，读 /z/；植物名复数、动词三单同形。先看句中是植物，还是造成情绪反应的动作。',NETTLE+[['nettle + -s → nettles','多棵荨麻；它让人刺痛、不快']],
 'stinging nettles 荨麻；nettles him 惹他不快；nettles the audience 让听众不舒服。',
 'nettles beside the path；a comment that nettles her。',
 'nettles 的 s 不是动词一定标记；the nettles grow 中它是植物复数，his tone nettles me 中才是三单动词。',
 ('Nettles grew thickly beside the path.','小路旁荨麻长得很密。'),('His superior tone nettles me.','他那高人一等的口气让我不快。'),sources=S('nettles','nettle'))
W('nettled','/ˈnetəld/','被惹得不快、有些恼火的；刺痛、惹恼了',
 '对方一句轻慢话扎到自己，嘴上反驳，心里有点火，人就是 nettled。不是每次都到暴怒的程度。',
 'nettle 去 e 加完整 -ed，读 /d/；分词形容词很早用于感到不快的人，接植物刺毛的动词意象。',NETTLE+[['nettle → nettled','受到刺激而不快；也作动作过去形式']],
 'nettled by the remark 被那句话惹得不快；slightly nettled 有些恼火。',
 'looked nettled；nettled at the suggestion。',
 'nettled 带被话或事刺了一下的反应，hurt 更广，可指伤心或身体受伤；不能所有受伤都译成 nettled。',
 ('He looked nettled by the suggestion that he needed help.','一听说自己需要帮忙，他显得有些恼火。'),('Her casual insult nettled him.','她随口的冒犯让他不快。'),sources=S('nettled','nettle'))
W('nettling','/ˈnetlɪŋ/','正在惹恼、刺得人不快；令人恼火的',
 '挖苦话一再刺过来，正在把人惹烦，是 nettling；也可说 a nettling remark，话本身带让人不舒服的小刺。',
 'nettle 去 e 加 -ing；动作形式也可作形容词，常见读音中间收成 /tl/。',NETTLE+[['nettle → nettling','惹恼正在发生；或形容会刺人的话、行为']],
 'a nettling question 刺得人不快的问题；nettling him with jokes 用玩笑惹他烦。',
 'nettling comments；keep nettling someone。',
 'a nettling question 重点是令人不快，a searching question 可以是深入追问；不能把问得深一律当成故意刺人。',
 ('She kept nettling him with remarks about his lateness.','她不断拿他迟到的事刺他，让他心烦。'),('It was a nettling question, but he answered calmly.','这个问题让人有点不快，他却平静地回答了。'),sources=S('nettling','nettle'))
W('nettlesome','/ˈnetəlsəm/','烦人的；难缠、棘手的',
 '不是大到完全做不了，却像荨麻小刺一样总扎着你、让你不省心的问题，可以叫 nettlesome。现代尤其可见于美式书面表达。',
 'nettle + -some；-some 写容易造成某种影响、带某种性质，保留基底 e。旧记录也有易怒义，现代常用来形容烦人、棘手的事。',NETTLE+[['nettle + -some → nettlesome','从植物、刺人的意象到烦人、难缠的性质']],
 'a nettlesome issue 棘手、烦人的问题；nettlesome details 让人费神的细节。',
 'a nettlesome problem；a nettlesome dispute。',
 'nettlesome problem 说问题让人烦，nettled person 说人已感到不快；不要只凭 nettl- 就忽略词尾改变的作用方向。',
 ('The team finally solved a nettlesome scheduling problem.','团队终于解决了一个难缠的排期问题。'),('A few nettlesome details remained unresolved.','还有几处让人费神的细节没解决。'),sources=S('nettlesome','nettle'))
W('chafes','/tʃeɪfs/','磨痛、擦伤；感到不耐烦〔第三人称单数〕',
 '鞋边一直蹭脚，叫 it chafes；人被限制得不舒服、总想摆脱，也能说 chafes at the restrictions。摩擦和情绪不是同一件事，却共享不舒服的意象。',
 'chafe + -s，/f/ 后读 /s/；经法语 chaufer 接拉丁使热材料，英语情绪、发热等支线都很早，不把摩擦磨伤说成所有义的唯一开端。',CHAFE+[['chafe + -s → chafes','它磨痛皮肤；他对限制感到烦躁']],
 'the collar chafes the neck 衣领磨脖子；chafes at restrictions 对限制感到不耐烦。',
 'chafes against the skin；chafes under the rules。',
 'chafes at the rules 说约束让人憋得慌，breaks the rules 才明确违反；不耐烦不等于已经违规。',
 ('The stiff collar chafes my neck.','硬衣领磨得我的脖子不舒服。'),('He chafes at rules that limit his freedom.','那些限制自由的规定让他很不耐烦。'),sources=S('chafes','chafe'))
W('chafed','/tʃeɪft/','磨痛、擦伤了；烦躁、不耐烦了',
 '鞋跟磨了很久，皮肤痛，是 chafed；等得不耐烦、对束缚憋得难受，也可用同形过去式。',
 'chafe 去 e 加完整 -ed；/f/ 后词尾读 /t/，合成 /ft/。',CHAFE+[['chafe → chafed','过去摩擦磨痛；或过去对限制感到烦躁']],
 'chafed skin 磨红、磨痛的皮肤；chafed at the delay 因拖延不耐烦。',
 'boots chafed his heels；chafed under restrictions。',
 'chafed skin 常是摩擦造成的不适，sunburned skin 是日晒灼伤；都是皮肤不舒服，原因不能混为一谈。',
 ('The new boots chafed his heels.','新靴子磨痛了他的脚跟。'),('She chafed at the endless restrictions.','没完没了的限制让她憋得难受。'),sources=S('chafed','chafe'))
W('needled','/ˈniːdəld/','用话挖苦、刺激了；用针刺、处理了',
 '一直拿某人的短处开小刺玩笑，想看他发火，是 needled him。像拿针轻轻扎一下又一下，但现代惹恼义的历史可能还经过讨价还价的旧用法。',
 'needle 去 e 加完整 -ed，读 /d/；动词由针名词转用，后来有挑衅、惹恼义。',NEEDLE+[['needle → needled','过去用针刺、处理；或反复挖苦、挑衅']],
 'needled about his mistake 因错误被反复挖苦；needled him until he snapped 一直刺他，直到他发火。',
 'gently needled；needled someone over a defeat。',
 'teased 可以是温和打趣，needled 更常强调用小刺话试着惹出反应；但程度仍由具体场景决定。',
 ('They needled him about losing the match.','他们不停拿输掉比赛的事挖苦他。'),('She needled her brother until he finally reacted.','她一直用话刺哥哥，直到他终于有了反应。'),sources=S('needled','needle'))
W('goad','英 /ɡəʊd/；美 /ɡoʊd/','刺激、激将、驱使；赶牛尖棒；刺激因素',
 '赶牛的尖棒戳一下，逼动物往前；goad 人则常用挖苦、挑战把人激得做出反应。尖棒名词很古老，但英语动词最早已有抽象刺激义。',
 '名词承古英语 gad 尖头器物、赶牛棒，后来转动词。不要因为意象直观，就把字面用棒赶的动词记录排在抽象煽动动词之前。',GOAD,
 'goad someone into doing something 激将某人去做；goad someone on 不断刺激、煽动。',
 'a goad to action 行动的刺激因素；refuse to be goaded。',
 'encourage 常带支持、鼓励，goad 则更像戳、激、逼，可能让人做本来不愿做的事；作用方向相似，态度不同。',
 ('Don’t let them goad you into an argument.','别让他们用激将法把你拽进争吵。'),('The farmer carried a goad beside the cattle.','农夫在牛群旁拿着一根赶牛尖棒。'),sources=S('goad','goad'))
W('goads','英 /ɡəʊdz/；美 /ɡoʊdz/','刺激、激将〔第三人称单数〕；赶牛尖棒、刺激因素〔复数〕',
 '他故意笑你不敢，想逼你出手，是 he goads you；不止一根赶牛尖棒，名词复数也是 goads。',
 'goad + -s，/d/ 后读 /z/；名词复数和动词三单同形，尖棒名词转出刺激行动的动词。',GOAD+[['goad + -s → goads','他用挑衅刺激；多根尖棒或多个刺激因素']],
 'goads him into replying 激他回应；goads the crowd on 煽动人群。',
 'goads his rival；goads them into action。',
 'goads someone into a fight 强调被刺激着卷入冲突；invites someone to talk 则可以是友好邀请，不能都简化成叫人做事。',
 ('He goads his rival with remarks about the last defeat.','他拿上次失败的事刺激对手。'),('Her impatience goads the team into rushing the work.','她的不耐烦逼得团队匆忙赶工。'),sources=S('goads','goad'))
W('goaded','英 /ˈɡəʊdɪd/；美 /ˈɡoʊdɪd/','刺激、激将了；被逼得、激得去做的',
 '本来不想争，被对方一句句刺得终于回嘴，就是 was goaded into responding。into 后面点被激出来的动作。',
 'goad + 完整 -ed，/d/ 后读 /ɪd/；过去形式和被动形式，来自尖棒名词转用的动词。',GOAD+[['goad + -ed → goaded','过去刺激、激将；或已被激得行动']],
 'goaded into a fight 被激得打架；goaded into replying 被激得回应。',
 'goaded by insults；goaded him on。',
 'goaded into agreeing 更带受刺激、受逼的成分，gladly agreed 才明确高兴地同意；不要漏掉被动句的压力来源。',
 ('He was goaded into replying by their insults.','他们的辱骂激得他终于回了嘴。'),('The crowd goaded the players on with shouts and taunts.','人群用喊叫和挖苦不断刺激球员。'),sources=S('goaded','goad'))
W('goading','英 /ˈɡəʊdɪŋ/；美 /ˈɡoʊdɪŋ/','不断刺激、激将；这种挑衅行为',
 '一句句刺你，等着你忍不住做出反应，这种过程是 goading；还可以把它当作整场挑衅行为来讲。',
 'goad + -ing；动作形式也可作行为名词，承尖棒催促到刺激行动的用法。',GOAD+[['goad + -ing → goading','正在刺激、激将；或命名这类行为']],
 'stop goading someone 别再激某人；goading him into a reaction 刺激他做出反应。',
 'constant goading；ignore the goading。',
 'goading 往往试图激出具体反应，mocking 可以只是取笑；一句话可以两者兼有，但重点不同。',
 ('Stop goading him into losing his temper.','别再刺激他发脾气了。'),('She refused to react to his constant goading.','面对他不停激将，她不肯作出反应。'),sources=S('goading','goad'))
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_zgm',ROOTS,WORDS)
 extend_lessons()
