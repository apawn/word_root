"""Communication, sugar and spell: familiar words with several semantic branches."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
C=[['拉丁 communicāre、communicātiō 等 → communication','分享、传达、建立共同理解'],['法语 télécommunication → 英语 telecommunication','远距离传送消息；英语可对照 tele- + communication']]
W('telecommunication','英 /ˌtelɪkəˌmjuːnɪˈkeɪʃən/；美 /ˌteləkəˌmjuːnɪˈkeɪʃən/','电信、远距离通信',
 '两端不在同一地方，用信号把消息送过去：电话、无线电、网络都在这个大范围里，tele- 说距离远。',
 '借法语 télécommunication，可对应 tele- 远 + communication 通信。行业、系统常用复数 telecommunications，不另造一个相同词义词头。',C,
 'telecommunication networks 电信网络，telecommunication services 电信服务，the telecommunications industry 电信业。',
 'telecommunication networks；telecommunication services；the telecommunications industry。',
 'telecommunication 侧重借技术远距离传递消息；communication 范围更大，面对面交流也算；tele- 不是只代表电视。',
 ('The storm damaged telecommunication networks.','风暴损坏了电信网络。'),('She works in the telecommunications industry.','她在电信业工作。'))
R('B4015','把消息、意思传给对方，建立共同理解','COMMUNICATION：消息送到，还要看对方是否理解','communication → miscommunication；telecommunication 接远距离技术通信。',
 '成功发出消息不一定等于成功理解；miscommunication 可以双方理解错，不必有人故意撒谎。',
 'communicāre、communicātiō → communication；mis- + communication；法语 télécommunication → 英语，tele- 表远。',
 [['交流与理解出错','communication · miscommunication'],['远距离通信','telecommunication']],
 'communication 广义交流；telecommunication 技术远传；miscommunication 理解、传递出了差错。',
 'Better communication reduced miscommunication between the teams.\n\n更充分的沟通减少了团队之间的误解。','communication miscommunication telecommunication')
S=[['梵语 śarkarā 等，经波斯语、阿拉伯语及欧洲语言 → sugar','砂粒状物、糖 → 糖'],['英语组合与形容','sugary 很甜、甜腻；sugared 加糖的；sugarcoat 包糖衣、粉饰']]
W('sugared','英 /ˈʃʊɡəd/；美 /ˈʃʊɡərd/','加糖的、裹糖的；甜言蜜语的〔比喻〕',
 '水果外面撒了糖，咖啡里加了糖，都可说 sugared；说话外面也撒一层好听的话，可产生甜言粉饰的比喻。',
 'sugar 作动词加糖 + -ed，过去分词作形容词。它说加糖处理或相似修饰，不保证原料本来就天然很甜。',S[:1]+[['sugar〔加糖动词〕+ -ed → sugared','经过加糖、裹糖的；再可形容甜言修饰']],
 'sugared almonds 糖衣杏仁，sugared coffee 加糖咖啡，sugared words 甜言蜜语。',
 'sugared almonds；sugared coffee；sugared words。',
 'sugared 往往强调加过糖，sugary 强调含糖、口感甜或过分甜腻；同一食品可两词都合适，但侧重点不同。',
 ('A bowl of sugared almonds stood on the table.','桌上放着一碗糖衣杏仁。'),('She preferred plain fruit to sugared fruit.','比起加糖的水果，她更喜欢原味水果。'))
W('sugarcoat','英 /ˈʃʊɡəkəʊt/；美 /ˈʃʊɡərkoʊt/','给……裹糖衣；把难听事实说得好听、粉饰',
 '苦药外面裹一层甜的糖，吃起来没那么苦；难听的消息外面裹一层好话，听起来也没那么刺耳。',
 'sugar 糖 + coat 覆上一层，组合为裹糖衣动词；比喻义借糖衣遮住苦味的做法，不是 coat 大衣被糖变出来。',S[:1]+[['sugar + coat → sugarcoat','外面覆糖层'],['苦味被甜层遮住的比喻','把坏消息、缺点修饰得更好听']],
 'sugarcoat the truth 粉饰事实，sugarcoat bad news 把坏消息说得好听，not sugarcoat anything 有话直说。',
 'sugarcoat the truth；sugarcoat bad news；not sugarcoat anything。',
 'sugarcoat 强调降低不好听、难接受的感觉；polite 礼貌不一定隐瞒事实，诚实也可以表达得体。',
 ('I will not sugarcoat it: the repairs will take weeks.','我就直说了：修理得花好几个星期。'),('The report tried to sugarcoat the poor results.','报告试图把糟糕的结果说得好听一些。'))
R('B3087','甜的糖，也能借来说好听的话','SUGAR：实物的甜可变成语言表面的甜','sugar → sugared、sugary；sugarcoat 把糖当一层外衣，再引申粉饰。',
 '糖衣和事实修饰可以用同一画面记；sugared 加过糖，sugary 含糖、甜腻，不能完全互换每个搭配。',
 'śarkarā 等经波斯、阿拉伯及欧洲语言 → sugar；sugar + -ed/-y；sugar + coat。',
 [['糖与加糖、甜的性质','sugar · sugared · sugary'],['糖衣与粉饰','sugarcoat']],
 'sugared/sugary 处理与性质；sugarcoat/polite 粉饰与礼貌，表达诚实不妨碍表达得体。',
 'Do not sugarcoat the results with sugary language.\n\n别用甜腻好听的话粉饰结果。','sugar sugared sugary sugarcoat')
ROOTS[-1]['exclude']['sugarman']='少见人物名词，先掌握 sugar、sugary、sugared 和 sugarcoat。'
SP=[['古英语 spell 及日耳曼语同族','话语、消息、故事 → 被认为有魔力的话、咒语'],['法语 espeler 等与日耳曼语讲说词族 → spell〔拼写〕','逐字说出、读写字母；与话语分支同族'],['古英语 spelian 等 → 另一路 spell','替人接班、轮值；一段时间义另有历史背景，非拼字一会儿']]
W('spell','/spel/','拼写；意味着、招致；咒语、迷人影响；一阵、一段时间；替人轮班',
 '拼名字是在把字母一个个说清；故事里的咒语是据说有魔力的一段话。a cold spell 一阵寒冷则要另记时间分支，不是天气在拼字。',
 '拼写动词经法语接日耳曼讲说词族，也与英语旧讲说词相关；咒语名词从古英语 spell 话语、消息发展。轮班、短时段另有旧替代、接班背景，不能把全部义项排成拼写到天气的单线。',SP,
 'spell your name 拼出姓名，spell out the plan 讲清计划，cast a spell 施咒，spell trouble 意味着麻烦，a dry spell 一段干旱。',
 'spell your name；spell out；cast a spell；spell trouble；a dry spell。',
 'spell out 除逐字拼出还可明确解释；spell 的英式过去式可 spelt，美式常 spelled，两种不是两个新词根。',
 ('Could you spell your surname for me?','能给我拼一下你的姓吗？'),('The fairy cast a spell on the castle.','仙女给城堡施了咒语。'),('The town enjoyed a spell of warm weather.','小镇迎来了一阵暖和天气。'),
 sources=['https://en.wiktionary.org/wiki/spell#English','https://www.etymonline.com/word/spell'])
W('spelling','/ˈspelɪŋ/','拼写、拼法；拼写能力',
 '一个词究竟由哪些字母、按什么顺序写出来，就是 spelling；读音听着相同，拼法也可能不同。',
 'spell 拼写 + -ing，形成过程、结果名词，也可作动词进行形式；双 l 已在基础词里，不是此处额外变来。',SP[1:2]+[['spell + -ing → spelling','拼写动作、具体拼法和能力']],
 'check the spelling 检查拼写，a spelling mistake 拼写错误，British spelling 英式拼法，correct spelling 正确拼写。',
 'check the spelling；a spelling mistake；British spelling；correct spelling。',
 'spelling 字母写法，pronunciation 读音；会读不保证会拼，同音词可有不同拼法。',
 ('Please check the spelling of my name.','请核对我的姓名拼写。'),('The two words have the same pronunciation but different spellings.','这两个词读音相同，拼写却不同。'))
W('speller','英 /ˈspelə/；美 /ˈspelər/','拼写者；拼写能力……的人；拼写练习书',
 '说一个人是 a good speller，就是他拼词很准；也可指教人拼写的练习书，语境决定是人还是教材。',
 'spell 拼写 + -er，常见人物后缀；教材义把工具用途接进同一名称，不是指施法者。',SP[1:2]+[['spell + -er → speller','拼写的人；用于教拼写的教材']],
 'a good speller 拼写好的人，a poor speller 拼写较弱的人，a spelling competition for young spellers 青少年拼写比赛。',
 'a good speller；a poor speller；young spellers。',
 'speller 拼写者；spellcaster 等才是施咒者的常见表达，不能仅因 spell 有咒语义就随意给 -er 套人物。',
 ('She is a good speller but a slow reader.','她拼写很准，不过读得慢。'),('The young spellers practised every afternoon.','这些参加拼写的孩子每天下午练习。'))
W('gospel','英 /ˈɡɒspəl/；美 /ˈɡɑːspəl/','福音、福音书；福音音乐；被当作绝对真理的话',
 '本来抓住“好消息”：宗教语境指福音、相关书卷；take it as gospel 则把某句话当成绝对可靠，像不再需要核实。',
 '古英语早期 good 好 + spel 消息，翻译福音的概念；后来词形又受 God 上帝的联想影响。spell 这里保留消息旧义，不是拼写练习或魔咒。',SP[:1]+[['古英语 gōd〔好〕+ spel〔消息〕→ godspel 等 → gospel','好消息 → 福音，后来又与 God 产生联想'],['现代领域扩展','福音书、福音音乐；不容置疑的真理比喻']],
 'the Gospel of Luke 路加福音，gospel music 福音音乐，take something as gospel 把某说法奉为绝对真理。',
 'gospel music；the Gospel of Luke；take it as gospel。',
 'gospel 历史成分不等于现代 go + spell；take it as gospel 常提醒不要对传闻照单全收。',
 ('The choir sang gospel music.','合唱团演唱了福音音乐。'),('Do not take every online claim as gospel.','别把网上每个说法都当成绝对真理。'),
 sources=['https://en.wiktionary.org/wiki/gospel#English','https://www.etymonline.com/word/gospel'])
W('spellbound','/ˈspelbaʊnd/','着迷的、看得入神的、被吸引得挪不开注意力的',
 '像中了咒被定住一样，故事太精彩，你暂时顾不上别的；现代多是强烈吸引的比喻，不是真的动不了。',
 'spell 咒语 + bound，bind 绑住的分词。被咒语束住的画面变成注意力被牢牢吸住。',SP[:1]+[['spell + bound〔bind 的分词〕→ spellbound','像被咒语绑住 → 入神、着迷']],
 'hold an audience spellbound 使观众入神，listen spellbound 听得入迷，be spellbound by 被……迷住。',
 'hold an audience spellbound；listen spellbound；be spellbound by。',
 'spellbound 常说人的受吸引状态，spellbinding 说让人入迷的人、作品或表演；像 interested/interesting 的方向区别。',
 ('The storyteller held the children spellbound.','讲故事的人让孩子们听得入了迷。'),('We were spellbound by the performance.','我们被演出深深吸引。'))
W('spellbinding','/ˈspelbaɪndɪŋ/','令人入迷的、扣人心弦的',
 '这东西抓住你的注意力，像会施一个让人坐着不动的咒；常用来夸故事、表演非常吸引人。',
 'spell 咒语 + binding 束住，对应 bind 的 -ing 形式。它侧重造成吸引的性质，spellbound 侧重被吸引的状态。',SP[:1]+[['spell + binding → spellbinding','如咒语般束住注意力 → 令人入迷']],
 'a spellbinding performance 令人入迷的演出，a spellbinding story 扣人心弦的故事，spellbinding music 迷人的音乐。',
 'a spellbinding performance；a spellbinding story；spellbinding music。',
 'a spellbinding story 让人着迷的故事，a spellbound audience 入神的观众，别把谁造成、谁感受到写反。',
 ('She gave a spellbinding performance.','她奉上了一场令人入迷的演出。'),('The novel opens with a spellbinding scene.','小说以一个扣人心弦的场景开篇。'))
R('B2909','话语、拼写与咒语；另辨轮班时段','SPELL：说出字母，也可是一段被认为有力量的话','spell → spelling、speller、misspell；gospel 保留消息旧义；spellbound → spellbinding 分人的状态与作品的吸引力。',
 '拼写和魔咒可以联系早期话语背景，但一段天气、一班替工另有旧路径；不把所有同拼写都硬压进一个故事。',
 '古英语 spell 话语、消息；法语 espeler 等 → 拼写 spell；good + spel → gospel；spell + bound/binding。',
 [['拼写动作、人物与错误','spell · spelling · speller · misspell'],['消息旧义的保留','gospel'],['咒语比喻与吸引力','spellbound · spellbinding']],
 'spelling/pronunciation 拼法读音；gospel 非 go+spell；spellbound 状态与 spellbinding 吸引性质；a cold spell 一阵冷天气。',
 'The spellbinding story held the audience spellbound.\n\n扣人心弦的故事让观众听得入神。','spell spelling speller misspell gospel spellbound spellbinding')
if __name__=='__main__':save('continuation_20261030_ej',ROOTS,WORDS)
