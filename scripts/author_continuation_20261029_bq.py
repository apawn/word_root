"""Bit and bite: morsels, binary digits, and sharp sensations."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
def C(a,b,w,m):return [[a+'；'+b,'并列构词部分'],[w,m]]
BT=[['古英语 bita / bite → 中古英语 bitte / bite','一口、一小块；与咬的旧词族相关'],['另一路：binary digit → bit','二进制数字的现代缩合名称'],['英语 bit','一点、一小块；另有比特；还是 bite 的过去式形式']]
W('bit','/bɪt/','一点；一小块；比特；bite 的过去式',
 '日常先想一点点、一小块；电脑语境另想一个二进制位。',
 '小块义接古英语 bita、bite 等旧形式，与 bite 的咬、切有关。计算机 bit 来自 binary digit 缩合，Shannon 1948年论文把名称归于 Tukey。动词 bit 则是 bite 的过去式，三种用法要看句子。',BT,
 'a bit of cake 一点蛋糕，a bit tired 有点累，bits and pieces 零碎物品。a bit 在特定语气下可以是委婉表达，并不总是精确地很少。电脑中 bit 是可取0或1的二进制位。',
 'a bit of；a little bit；bit by bit；do one’s bit；eight bits。',
 'a bit of water 一点水，a bit tired 有点累；不要写 a bit of tired。bit 比特与 byte 字节不同，通常一个字节含8比特。',
 ('I need a bit of time to think.','我需要一点时间考虑。'),('We repaired the old house bit by bit.','我们一点一点修好了老房子。'),('Each position in this binary number holds one bit.','这个二进制数的每一位存放一个比特。'),sources=['https://en.wiktionary.org/wiki/bit#English','https://academicweb.nd.edu/~powers/ame.20231/shannon1948a.pdf'])
W('bitty','/ˈbɪti/','零碎的；不连贯的；很小的',
 '像一块块小碎片，单独都有，但没有顺畅地接起来。',
 'bit 小块 + -y。由很多小块构成，发展出零碎、不连贯义；另有很小的非正式用法。',BT[:1]+[['bit + -y → bitty','小块 → 零碎的；很小的']],
 'a bitty account 零散的叙述，a bitty film 情节连接不畅的电影。英式口语常用来评价组织、结构不够完整。',
 'a bitty report；a bitty structure；feel rather bitty。',
 'bitty 不只是 short 简短；一个短报告也可以结构清楚，一个很长的报告也可能零碎不连贯。',
 ('The report feels bitty because the sections do not connect.','报告各部分衔接不上，读起来很零散。'),('The film has some lovely scenes, but its story is rather bitty.','电影有一些漂亮场景，但故事较为支离破碎。'),sources=['https://en.wiktionary.org/wiki/bitty#English','https://dictionary.cambridge.org/dictionary/english/bitty'])
W('tidbit','/ˈtɪdbɪt/','少量美味；趣闻、小消息',
 '本来是一小口好吃的；再借说一小条让人感兴趣的消息。',
 'tid 是表示讨喜、美好等意思的旧词，bit 是小块；组合先说小口美味，再引申为有趣的信息碎片。英式也常写 titbit。',C('tid 旧义：讨喜、美好','bit 一小块','tidbit','小口美味 → 有趣的小消息'),
 'a tidbit of information 一点有趣消息；historical tidbits 历史趣闻。往往小而有吸引力，不是完整长篇报告。',
 'a juicy tidbit；tidbits of information；historical tidbits。',
 'tidbit 与 bit 都可说一小点，但 tidbit 通常额外带好吃或有趣的意味；它不一定是未经证实的八卦。',
 ('The guide shared a few historical tidbits about the theatre.','导游分享了几则关于剧院的历史趣闻。'),('The chef offered us a tidbit of the new dessert.','厨师让我们尝了一小口新甜点。'))
W('gigabit','/ˈɡɪɡəbɪt/','吉比特；十亿比特',
 '把一个个比特按十亿个一组来计数。',
 'giga- 国际单位制中的十亿倍前缀 + bit 比特。这里的 bit 来自 binary digit，而不是把食物小块放大。',C('giga- 十亿倍','bit 比特','gigabit','十亿比特的数据量单位'),
 'one gigabit 是十亿比特；a gigabit per second 是每秒十亿比特，常见缩写 Gbit/s 或 Gbps。网络标称速率与实际应用传输速度不必完全相同。',
 'gigabits per second；a gigabit connection；gigabit Ethernet。',
 'gigabit 的 b 是 bit，gigabyte 是字节；不要把广告里的1 Gbps 直接理解成每秒1 GB。',
 ('The brochure advertises a gigabit connection.','宣传册介绍了一种吉比特连接。'),('The diagram labels the link in gigabits per second.','图中把链路速率标成每秒多少吉比特。'))
W('bitrate','/ˈbɪtreɪt/','比特率；码率',
 '看一秒钟用了、传了多少个比特；不是只看一共有多少文件。',
 'bit 比特 + rate 速率，也常分写 bit rate。组合表示单位时间传送或处理的数据比特数。',C('bit 比特','rate 速率','bitrate','单位时间内的比特数量'),
 'audio bitrate 音频码率，video bitrate 视频码率。相同时长下，码率越高通常需要更多数据；画质还受编码方法、内容等影响。',
 'audio bitrate；video bitrate；a variable bitrate；increase the bitrate。',
 'bitrate 说每秒多少数据，不等于画面分辨率，也不只凭它就能比较不同编码视频的质量。',
 ('The app lets you choose the audio bitrate before exporting.','应用允许你在导出前选择音频码率。'),('A lower bitrate made the recording file smaller.','较低的码率让录音文件变小了。'))
R('B2466','一点、小块；另一路为比特','BIT：小块与二进制位分开记','日常小块可以来自咬下一口的旧画面；计算机比特则是现代 binary digit 的缩合词。',
 '普通 bit 接古英语小块词；技术 bit 在20世纪形成新命名。不要把所有计算机词都编成古人咬食物的连续历史。',
 'bit → bitty、tidbit；技术 bit → gigabit、bitrate、bitmap、bitcoin。bite 的过去式 bit 回到咬这一组理解。',
 [['少量、碎片与趣闻','bit · bitty · tidbit'],['二进制位与技术组合','gigabit · bitrate · bitmap · bitcoin']],
 'bit 比特与 byte 字节不同；bitty 零碎不等于只是简短；tidbit 带好吃或有趣的小片段意味。',
 'The guide gave us a few tidbits of information, bit by bit.\n\n导游一点一点地给我们讲了几则有趣的小消息。',
 'bit bitty tidbit gigabit bitrate bitmap bitcoin')
BI=[['古英语 bītan → 中古英语 biten','咬；有用牙切开的旧意象'],['英语 bite；过去式 bit，过去分词 bitten','咬；叮；刺痛；产生影响']]
W('bite','/baɪt/','咬；叮；刺痛；一口；产生明显影响',
 '用牙压住、切下一点；寒风或尖刻的话也可以像牙一样让人感到刺痛。',
 '继承古英语 bītan，经中古英语 biten 发展。过去式 bit /bɪt/，过去分词 bitten /ˈbɪtən/；不用 bited。',BI,
 'bite an apple 咬苹果；an insect bite 虫叮；a bite to eat 一点吃的。The new rules are starting to bite 是新规则开始产生明显影响。',
 'take a bite；a bite to eat；bite into；bite one’s lip；begin to bite。',
 'bite 指咬、叮，不等于所有昆虫蜇刺的 sting；a bite 一口是动作或份量，a bit 常是一点、小块。',
 ('She took a bite of the sandwich.','她咬了一口三明治。'),('The cold wind bit into our faces.','寒风吹得我们的脸刺痛。'),('The higher costs are beginning to bite.','成本上涨开始让人明显感到压力。'))
W('bitten','/ˈbɪtən/','被咬的；bite 的过去分词',
 '动作已经落在对象身上：它被咬过了。',
 'bite 的不规则过去分词，现代形式是 bit + -en；其中元音变化来自旧强变化动词传统，不是另一个咬的小词根。',BI+[['bite → bit → bitten','原形 → 过去式 → 过去分词']],
 'have been bitten 被咬过；bitten by the travel bug 是被旅行热情感染的比喻。once bitten, twice shy 表示吃过亏就会格外小心。',
 'be bitten by；have bitten；once bitten, twice shy。',
 '过去式用 bit：the dog bit me；完成或被动结构用 bitten：has bitten、was bitten。',
 ('The corner of the biscuit had already been bitten off.','饼干的一角已经被咬掉了。'),('After her first trip abroad, she was bitten by the travel bug.','第一次出国后，她就迷上了旅行。'))
W('biting','/ˈbaɪtɪŋ/','刺骨的；尖刻的；正在咬的',
 '寒冷或批评都像咬了一口，感觉尖、疼、直接。',
 'bite 去 e 加 -ing。除动词分词，还形成形容词，用于寒冷和言辞的强烈刺激感。',BI+[['bite → biting','咬 → 像咬一样刺人的']],
 'a biting wind 刺骨寒风，biting criticism 尖刻批评；形容词不必指实际牙齿动作。',
 'biting cold；a biting wind；biting satire；biting criticism。',
 'biting cold 与 bitter cold 都可说严寒；biting 尤其容易带刺人的触感，biting remarks 则是尖刻话。',
 ('A biting wind blew across the empty platform.','刺骨寒风吹过空荡荡的站台。'),('The review contained some biting criticism of the script.','评论中有一些针对剧本的尖刻批评。'))
W('biter','英 /ˈbaɪtə/；美 /ˈbaɪtər/','会咬的人或动物；咬人的家伙',
 '谁在咬、谁容易咬，就把那个动作贴到行动者身上。',
 'bite 去 e 加 -er；中古英语已有相应人名词。这里选常用的咬这一义，不混入冷门的比特计数等同形词。',BI+[['bite + -er → biter','咬 → 会咬、咬东西的人或动物']],
 'a biter 可用于描述爱咬东西的宠物或人；a nail biter 是咬指甲的人。带连字符的 nail-biter 另常比喻让人紧张的比赛。',
 'a persistent biter；a nail biter；be known as a biter。',
 'biter /aɪ/ 与 bitter /ɪ/ 不同；biter 是咬的人或动物，bitter 通常是苦的、怨恨的。',
 ('The shelter warned us that the rabbit was a biter.','收容所提醒我们，那只兔子会咬人。'),('I used to be a nail biter when I was nervous.','我以前紧张时会咬指甲。'))
BR=[['古英语 biter / bitter → 中古英语 bitter','苦的；与 bite 咬的古老词族有关'],['英语 bitter','味苦；让人痛苦、怨恨；严寒、激烈']]
W('bitter','英 /ˈbɪtə/；美 /ˈbɪtər/','苦的；痛苦而怨恨的；激烈的；刺骨的',
 '味道像刺激着舌头；情绪上则像心里被刺了一下，留下难受或怨意。',
 '接古英语 biter、bitter，与 bite 有古老词族联系。是继承下来的老形容词，不是现代 bit 一点 + -er 比较级，更不能把 bitter 读成 biter。',BR,
 'bitter coffee 苦咖啡；feel bitter about a decision 对某决定深感不满、怨恨；a bitter dispute 激烈而充满敌意的争执；bitter cold 严寒。',
 'a bitter taste；bitter disappointment；a bitter argument；be bitter about something。',
 'bitter 苦，不等于 sour 酸；bitter 形容情绪时常比单纯 sad 多一层失望、不平或怨恨。',
 ('The tea tasted bitter because I left the leaves in too long.','茶叶泡太久，茶喝起来发苦。'),('He still feels bitter about being left out of the team.','没能入选队伍，他至今仍耿耿于怀。'),('The two groups were locked in a bitter dispute.','两组人陷入了激烈而充满敌意的争执。'))
W('bitterly','英 /ˈbɪtəli/；美 /ˈbɪtərli/','痛苦地；满怀怨恨地；极其',
 '把苦涩的感受加到动作或情绪上，也常强化失望、寒冷等负面程度。',
 'bitter + -ly；古英语已有对应副词形式。现代常用于苦恼地抱怨、深感失望或严寒等搭配。',BR+[['bitter → bitterly','苦涩、怨恨的 → 苦恼地；极其']],
 'bitterly disappointed 极其失望，complain bitterly 满腹怨气地抱怨；bitterly cold 冷得刺骨。不是所有形容词都能随意接 bitterly。',
 'bitterly disappointed；bitterly cold；cry bitterly；complain bitterly。',
 'bitterly 在固定搭配中可加强程度，但通常带负面感受；不用 bitterly happy 作为很开心的普通表达。',
 ('She was bitterly disappointed by the cancellation.','活动取消让她极其失望。'),('We waited outside on a bitterly cold morning.','我们在一个严寒的早晨等在外面。'))
W('bitterness','英 /ˈbɪtənəs/；美 /ˈbɪtərnəs/','苦味；苦涩、怨恨',
 '可以是舌头上的苦，也可以是心里挥不去的怨与痛。',
 'bitter + -ness；古英语已有 biternes 等名词形式。把苦的性质、苦涩情绪作为一件事来谈。',BR+[['bitter → bitterness','苦的、怨恨的 → 苦味、怨恨状态']],
 'the bitterness of coffee 咖啡的苦味；feel no bitterness 没有怨恨；with bitterness 带着怨意。',
 'a hint of bitterness；lasting bitterness；without bitterness；the bitterness of defeat。',
 'bitterness 不只是 sadness 悲伤；谈人的情绪时常包含不甘、受了不公的感觉或怨恨。',
 ('A little sugar softened the bitterness of the coffee.','一点糖缓和了咖啡的苦味。'),('She spoke about the defeat without bitterness.','她谈起那次失败时没有怨恨。'))
R('B2743','咬；刺痛；苦与苦涩的历史亲缘','BITE：用牙切开，再借说刺激和痛感','真实咬下去是基本动作；寒风、批评像咬一样刺人。bitter 与它有古老亲缘，但现代是独立形容词。',
 'bite 接古英语 bītan；bit、bitten 保留不规则变化。bitter 接古英语 biter、bitter，与咬的词族相关，并非现代 bit + 比较级后缀。',
 'bite → bit、bitten、biting、biter；再看历史相关词 bitter → bitterly、bitterness。普通小块名词 bit 在另一页对照。',
 [['咬的动作、形式和行动者','bite · bitten · biting · biter'],['苦味、怨意与程度','bitter · bitterly · bitterness']],
 'bite /baɪt/，bit /bɪt/，bitten /ˈbɪtən/；biter /aɪ/ 与 bitter /ɪ/ 分清。',
 'A biting comment can leave more bitterness than the speaker expects.\n\n一句尖刻的话，可能留下超出说话人预料的怨意。',
 'bite bitten biting biter bitter bitterly bitterness')
for item in WORDS:
 if item['word'] in {'bit','gigabit','bitrate'}:
  item['sources'].append('https://physics.nist.gov/cuu/Units/binary.html')
if __name__ == '__main__':save('continuation_20261029_bq',ROOTS,WORDS)
