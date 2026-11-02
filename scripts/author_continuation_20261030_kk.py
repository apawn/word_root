"""Thunder, celebrity and spider."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
T=[['古英语 þunor、þunrian → 中古英语 thunder 等','雷声、打雷'],['现代声音与力量的比喻','雷鸣般的响声；轰隆行进、大声说话'],['复合词、后缀与受震撼的形象','thunderbolt、thunderclap；thunderous、thundering；thunderstruck']]
W('thunder','英 /ˈθʌndə/；美 /ˈθʌndər/','雷、雷声；轰隆响、轰隆行进；大声说',
 '闪电使周围空气迅速受热膨胀，产生听到的雷声。人群鼓掌、重物滚动或人大声怒斥，也能借雷声的音量和力量来形容。',
 '名词承古英语 þunor，动词有 þunrian 等形式；经中古英语传下。现代字母 th 表 /θ/，首音不是 /t/。',T[:2],
 'a rumble of thunder 隆隆雷声，thunder and lightning 雷和闪电，trucks thunder past 卡车轰隆驶过，thunder a warning 大声发出警告。',
 'a rumble of thunder；thunder and lightning；thunder past。',
 'thunder 是声音，lightning 是闪电。steal someone’s thunder 是抢走本该属于对方的关注、风头。',
 ('We heard thunder in the distance.','我们听见远处的雷声。'),('Heavy trucks thundered past the house.','重型卡车轰隆隆驶过房子。'),sources=['https://en.wiktionary.org/wiki/thunder#English','https://www.weather.gov/safety/lightning-science-thunder'])
W('thunderbolt','英 /ˈθʌndəbəʊlt/；美 /ˈθʌndərboʊlt/','雷电、霹雳；突如其来的震撼消息、事件',
 '像一道伴着巨响打下来的闪电，thunderbolt 也能比喻突然击中人心、让人震惊的事。',
 'thunder + bolt，后者有箭、快速射出之物等旧义，借来描绘雷电的一击。不是现代紧固螺栓把雷固定住。',T[:2]+[['thunder + bolt → thunderbolt','雷电的一击 → 猝然的震撼事件']],
 'a thunderbolt struck 一道霹雳击下，hit like a thunderbolt 像晴天霹雳一样震动人。体育中也可比喻强力一脚、一击。',
 'a thunderbolt；hit like a thunderbolt。',
 'thunder 单说雷声；thunderbolt 常把闪电、雷击的一击作为整体形象，语境不总是在严格区分气象参数。',
 ('A thunderbolt struck the old tree.','一道雷电击中了老树。'),('The announcement hit the team like a thunderbolt.','这项宣布像晴天霹雳一样震动了团队。'))
W('thunderclap','英 /ˈθʌndəklæp/；美 /ˈθʌndərklæp/','一声霹雳、突然的一声雷鸣',
 '持续滚动的是隆隆雷声；突然炸开、啪轰一下的响雷，可以叫 a thunderclap。',
 'thunder + clap 突然的拍击、爆响。clap 不只指人的鼓掌动作，也可指短促响亮的一声。',T[:2]+[['thunder + clap → thunderclap','突然爆响的一声雷']],
 'a sudden thunderclap 突然的一声雷，a loud thunderclap 一声巨雷。也可借喻突然造成强烈影响的事。',
 'a sudden thunderclap；a loud thunderclap。',
 'thunderclap 强调一下突然巨响；a rumble of thunder 强调滚动、延续的隆隆声。',
 ('A thunderclap shook the windows.','一声霹雳震得窗户发颤。'),('The speech ended just as a thunderclap sounded outside.','演讲刚结束，外面就响起一声霹雳。'))
W('thunderous','英 /ˈθʌndərəs/；美 /ˈθʌndərəs/','雷鸣般的、轰响的',
 '掌声一起涌来，大得像打雷，就说 thunderous applause。用雷声给声音的强度、震撼感打比方。',
 'thunder + -ous，形成有雷声般性质的形容词。词尾通常读 /ərəs/，不是照 thunder 的词尾再把每个字母念开。',T[:2]+[['thunder + -ous → thunderous','雷鸣般响亮、强烈的性质']],
 'thunderous applause 雷鸣般掌声，a thunderous roar 巨大的吼声、轰鸣。',
 'thunderous applause；a thunderous roar。',
 'thunderous applause 不表示天气在打雷。loud 只说响，thunderous 还带雷鸣般的气势。',
 ('The audience greeted her with thunderous applause.','观众以雷鸣般的掌声欢迎她。'),('A thunderous roar rose from the crowd.','人群中响起震耳欲聋的欢呼。'))
W('thundering','英 /ˈθʌndərɪŋ/；美 /ˈθʌndərɪŋ/','轰鸣、雷鸣般的；极大的〔强调〕',
 '奔跑的马群轰隆响，thundering hooves 把动作和声音一并带出来；a thundering success 又借这个力量夸事情大获成功。',
 'thunder + -ing，中古英语已有相应形式。既可作分词，也形成描述声音、巨大程度的形容词。',T[:2]+[['thunder + -ing → thundering','发出轰鸣；巨大的程度']],
 'thundering hooves 轰隆马蹄声，a thundering voice 洪亮声音，a thundering success 巨大成功。',
 'thundering hooves；a thundering success。',
 'thundering 与 thunderous 在雷鸣般的形容上有重叠；前者更容易带出正在轰隆的动作，或用来强烈强调。',
 ('We heard thundering hooves on the road.','我们听见路上轰隆的马蹄声。'),('The concert was a thundering success.','音乐会大获成功。'))
W('thunderstruck','英 /ˈθʌndəstrʌk/；美 /ˈθʌndərstrʌk/','惊呆的、震惊得说不出话的',
 '突然听到消息，整个人像被一声霹雳定住，愣在那里；thunderstruck 借的是这一瞬间的强烈惊讶。',
 'thunder + struck，struck 是 strike 的过去分词。由被雷击的形象固定为惊呆的情绪词。',T[:2]+[['thunder + struck → thunderstruck','仿佛被雷击中 → 惊呆、震惊']],
 'be thunderstruck 惊呆了，thunderstruck by the news 被消息震住。惊讶既可能由坏消息，也可能由意外发现引起。',
 'be thunderstruck；thunderstruck by the news。',
 'thunderstruck 常是情绪比喻，不应据此判断一个人真遭雷击；惊讶的原因要另看语境。',
 ('She was thunderstruck when her name was announced.','宣布到她的名字时，她惊呆了。'),('He stood thunderstruck at the unexpected news.','听到意外消息，他愣在原地。'))
R('B2916','雷声与轰鸣、力量的比喻，再到突发震撼','THUNDER：先听雷声，再借它的响亮和冲击力','thunder → thunderous、thundering；thunderbolt、thunderclap、thunderstruck 分别看一击、爆响、惊呆。',
 '声音、雷电、人的情绪不能全叫同一件事。雷的共同形象，把这些固定用法串起来，却不取消各词的分工。',
 'þunor → thunder；-ous 性质，-ing 分词；bolt 一击，clap 爆响，struck 被击中。',
 [['基础与响亮性质','thunder · thunderous · thundering'],['雷电、爆响与震撼','thunderbolt · thunderclap · thunderstruck'],['其他复合名称','thunderstorm · thunderbird']],
 'thunder 是声音，lightning 是闪电；thunderstruck 通常说惊呆；thunderous applause 是比喻。',
 'A thunderclap interrupted the speech, but the audience soon answered with thunderous applause.\n\n一声霹雳打断了演讲，但观众很快以雷鸣般的掌声回应。','thunder thunderous thundering thunderbolt thunderclap thunderstruck thunderstorm thunderbird')
C=[['拉丁 celeber、celēbritās','人多、常有人来；名声、盛会等相关意义'],['法语 célébrité 等 → 英语 celebrity','仪式等旧义；名气 → 有名的人'],['celebrity → celeb','名人义的口语截短']]
W('celebrity','/səˈlebrəti/，也读 /sɪˈlebrɪti/','名人；名气、名声',
 '一大群人知道、谈论某个人，他可能成了 a celebrity。这个词也能抽象地说成名的状态：celebrity can change a life。',
 '中古英语经法语相关形式，上接拉丁 celēbritās、celeber 人多、常有人来、著名等词义。英语先有仪式、名声等用法，后以名气转称有名的人；不是直接从现代 celebrate 删几个字母加 -ity。',C[:2],
 'a celebrity chef 名人厨师，a local celebrity 当地名人，celebrity culture 名人文化，achieve celebrity 获得名气。',
 'a local celebrity；a celebrity chef；celebrity culture。',
 'celebrity 只说明知名度，不自动保证成就、品德；可数 a celebrity 是人，不可数 celebrity 可说成名状态。',
 ('The baker became a local celebrity.','那位面包师成了当地名人。'),('The novel explores the pressures of celebrity.','小说探讨成名带来的压力。'),sources=['https://en.wiktionary.org/wiki/celebrity#English','https://www.etymonline.com/word/celebrity'])
W('celeb','/səˈleb/','名人〔口语〕',
 '把 celebrity 缩短，日常聊天、娱乐报道就有了 celeb。意思仍是名人，语体更轻松。',
 'celebrity 的截短词，取前面一部分重新形成短名词。重音落在 /leb/。',C[1:]+[['celebrity → celeb','名人义的口语短形式']],
 'a TV celeb 电视名人，celeb gossip 名人八卦。正式写作若无特殊语气，通常用 celebrity。',
 'a TV celeb；celeb gossip。',
 'celeb 是人，不是 celebration 庆祝活动的常用简称。它是截短，不是缩写字母逐个读。',
 ('A TV celeb visited the small café.','一位电视名人来过这家小咖啡馆。'),('The magazine is full of celeb gossip.','杂志里满是名人八卦。'))
R('B4003','名气转称有名的人，再截短为口语名称','CELEBRITY：从被许多人知道，到指那个有名的人','celebrity → celeb。',
 'celebrity 可以数一个人，也能说抽象名气。celebrate 与它有词源联系，但不宜只按现代英语拼装来代替历史。',
 'celeber／celēbritās → 法语相关形式 → celebrity；截短 → celeb。',
 [['名人与口语短形式','celebrity · celeb']],
 'a celebrity 是人，celebrity 可说名气；celeb 语体更口语；知名不保证品德。',
 'The local celebrity joked that he had never expected to become a celeb.\n\n那位当地名人开玩笑说，自己从没想过会成名。','celebrity celeb')
P=[['日耳曼语纺、纺丝的词族','按纺丝行为给动物命名'],['古英语 spīþra 等 → 中古英语 spithre、spider → spider','原来类似纺丝者的名称，音变后成为现代词形'],['网的比喻用于计算机','沿网页链接爬行、收集信息的程序']]
W('spider','英 /ˈspaɪdə/；美 /ˈspaɪdər/','蜘蛛；网络爬虫程序',
 '蜘蛛会产丝，名称历史上就联系纺丝。网络程序沿着网页链接到处搜集信息，也借蜘蛛在网上活动的形象叫 spider。',
 '承古英语 spīþra 等，经中古英语 spithre、spider。更早联系 spin 纺丝的日耳曼词族；历经音变，不是现代英语直接把 spin + -er 原样拼成 spider。',P,
 'a spider’s web／spiderweb 蜘蛛网，a web spider 网页爬虫。蜘蛛属于蛛形类，不能因为中文都说虫，就在英语分类里都称 insect。',
 'a spider’s web；a web spider。',
 '蜘蛛不是六足昆虫；不同蜘蛛捕食方式不同，不能把所有蜘蛛都说成靠同样的捕猎网抓食。程序 spider 是比喻名称。',
 ('A spider had built a web across the window.','一只蜘蛛在窗前结了网。'),('The search engine uses a spider to discover pages.','搜索引擎使用爬虫发现网页。'),sources=['https://en.wiktionary.org/wiki/spider#English','https://www.etymonline.com/word/spider'])
R('B3212','按纺丝行为形成的动物名，再借网形成技术比喻','SPIDER：历史上可理解为纺丝的动物','spider → spiderweb；计算机 spider 借网页链接之网。',
 '历史解释负责说明名称来历，现代分类、动物行为要分别理解；有产丝能力，不代表所有蜘蛛都织同样的捕猎网。',
 'spin 相关旧词族 → spīþra 等 → spider；web 网形成 spiderweb。',
 [['动物、网与技术比喻','spider · spiderweb']],
 'spider 不属于 insect；名称和 spin 有历史联系，但现代不能直接按规则变词形。',
 'The spider waited beside its spiderweb.\n\n蜘蛛待在它结的网旁边。','spider spiderweb')
if __name__=='__main__':save('continuation_20261030_kk',ROOTS,WORDS)
