"""River, weigh and short high-value extensions."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
RV=[['拉丁 rīpa 河岸 → rīpārius → rīpāria','河岸的、岸边地带'],['法语 rivere／riviere → 英语 river','河岸、河边 → 河流']]
def RH(f,m):return RV+[[f,m]]
W('river','英 /ˈrɪvə/；美 /ˈrɪvər/','河流',
 '水沿着固定河道流，名字的历史却先从旁边的河岸说起。',
 '经中古英语、盎格鲁法语接拉丁 rīpāria 河岸地带，最终是 rīpa 河岸。不能因 river 与 Latin rīvus 小溪相似就混成同一个来源。',RV,
 'a wide river 宽阔河流，cross the river 过河，the mouth of a river 河口；rivers of tears 可比喻眼泪流得很多。',
 'cross a river；along the river；a river flows；the mouth of a river。',
 'river 常较 stream 大，但日常命名并无一个通用尺寸分界；river 是河道水流，lake 是湖。',
 ('The river flows through the centre of the city.','河流穿过市中心。'),('We crossed the river on a small wooden bridge.','我们从一座小木桥上过了河。'),sources=['https://www.etymonline.com/word/river','https://en.wiktionary.org/wiki/river#English'])
W('upriver','英 /ˌʌpˈrɪvə/；美 /ˌʌpˈrɪvər/','向上游；在上游的',
 '沿着河道往水来的方向走，朝河源那边，通常是逆着水流。',
 'up- 向上 + river，up 按河流上下游关系理解，不按地图纸面上方理解。',RH('up- + river → upriver','朝源头方向；在较上游位置'),
 'travel upriver 沿河向上游行进，an upriver village 上游村庄，five miles upriver 往上游五英里。',
 'travel upriver；an upriver village；farther upriver。',
 'upriver 不是一定向北；水可以向各种方向流。upstream 也表示上游，还更常有流程前端的比喻义。',
 ('We travelled upriver to a small village.','我们沿河向上游来到一个小村庄。'),('The new bridge is two kilometres upriver.','新桥在上游两公里处。'))
W('downriver','英 /ˌdaʊnˈrɪvə/；美 /ˌdaʊnˈrɪvər/','向下游；在下游的',
 '沿水往它流去的方向走，朝河口那边。',
 'down- 向下 + river，描述相对河源与河口的方向、位置。与 upriver 成对记。',RH('down- + river → downriver','沿水流方向；在较下游位置'),
 'float downriver 顺流漂下，a downriver town 下游城镇，farther downriver 更往下游。',
 'float downriver；travel downriver；a town downriver。',
 'downriver 按水流判断，不按地名在地图上方还是下方；downstream 同样可说下游，也可比喻后续流程。',
 ('The boat drifted slowly downriver.','船缓缓向下游漂去。'),('Another town lies ten miles downriver.','另一座城镇在下游十英里处。'))
W('riverboat','英 /ˈrɪvəˌbəʊt/；美 /ˈrɪvərˌboʊt/','内河船；河上游船',
 '主要沿河行驶的船，旅游照片里常见，但名称不限于观光船。',
 'river + boat，按航行水域命名。合成词保留两部分的常用意思。',RH('river + boat → riverboat','在河流上运行的船'),
 'a riverboat cruise 内河游船旅行，a riverboat captain 内河船船长。具体大小、动力和用途要另外说。',
 'a riverboat cruise；a riverboat captain；board a riverboat。',
 'riverboat 强调河上航行，ferry 强调摆渡运输；一艘船可以同时符合两种描述。',
 ('We boarded a riverboat for a tour of the city.','我们登上游船，沿河游览城市。'),('The riverboat carried supplies to villages along the bank.','内河船把物资送到沿岸村庄。'))
W('riverine','英 /ˈrɪvəraɪn/；美 /ˈrɪvəriːn/ 或 /ˈrɪvərɪn/','河流的；河岸地区的；栖居河流的',
 '把河流及其沿岸当作一个环境来描述，常见于生态、地理等文字。',
 'river + -ine，形成关系形容词；-ine 这里表与之有关，不是数字 nine 的一部分。读音有地区、个人差异。',RH('river + -ine → riverine','与河流及其周边环境相关'),
 'riverine habitats 河流生境，riverine ecosystems 河流生态系统，riverine communities 可指沿河居民群体。',
 'riverine habitats；riverine ecosystems；riverine communities。',
 'riverside 更日常地说河边位置，riverine 更像地理、生态描述；rival 对手另接 rīvus，不按相近拼写归这条历史。',
 ('The project aims to protect riverine habitats.','项目旨在保护河流生境。'),('Several riverine communities depend on boats for transport.','几个沿河社区依靠船只出行。'))
R('B3100','河流、上下游与河边环境','RIVER：名称来自河岸，方向跟着水流看','river 为起点，上下游成对；接船与环境形容词，河岸、河床等已有词一起复习。',
 '法语河流词最终接拉丁河岸 rīpa，不与 rīvus 小溪混同。少见地名式和专名式复合先略。',
 'up-/down- + river；river + boat/-ine；已有 river + side/bank/front/bed/walk。',
 [['河流与上下游','river · upriver · downriver'],['河边位置','riverside · riverbank · riverfront · riverbed · riverwalk'],['船只与环境','riverboat · riverine']],
 'upriver 朝源头，downriver 朝河口，与南北无固定关系；riverine 偏环境描述。',
 'The riverboat travelled upriver past several riverside villages.\n\n内河船驶向上游，经过几个河边村庄。',
 'river upriver downriver riverside riverbank riverfront riverbed riverwalk riverboat riverine')
WE=[['古英语 wegan → 中古英语 weien','举起、搬动；称量、具有重量'],['英语 weigh','称重；重达；权衡考虑']]
W('weigh','/weɪ/','称重；重达；权衡',
 '把东西放在秤上看多重；考虑方案时，也像把好处、坏处放到两边掂量。',
 '继承古英语 wegan，旧义包括举、承载与称量。思想上的权衡是中古时期已有的延伸。gh 今天不发音，weigh 与 way 同音。',WE,
 'weigh the bag 给包称重，The bag weighs five kilos 包重五公斤，weigh the options 权衡选项。weigh anchor 是起锚，保留举起的旧义。',
 'weigh five kilos；weigh the options；weigh the evidence；weigh anchor。',
 'weigh 是动词，weight 通常作重量名词；How much does it weigh? 对应 What is its weight?。weigh the options 不涉及实际天平。',
 ('The suitcase weighs twelve kilos.','行李箱重十二公斤。'),('We need to weigh the benefits against the cost.','我们需要权衡收益与成本。'),sources=['https://www.etymonline.com/word/weigh','https://en.wiktionary.org/wiki/weigh#English'])
R('B3585','称重与权衡','WEIGH：放上秤，或在心里掂量','补上动作 weigh，再共享 weight 重量与 outweigh 更有分量。',
 '古英语动词兼有举起与称量义。weight 为同源旧名词，不是今天 weigh 临时加 t 的通用规则。',
 'weigh／weight 同族；out- + weigh → outweigh。',
 [['动作、名词与比较','weigh · weight · outweigh']],
 'weigh 动词与 weight 名词区分；weigh anchor 起锚保留举起旧义。',
 'We weighed the options and decided the benefits outweighed the risks.\n\n我们权衡选项后，认为收益大于风险。',
 'weigh weight outweigh')
UT=[['古英语 untrēowþ 等形式 → 中古英语 untreuth','不忠实；虚假'],['现代 untruth','不实之言、谎话']]
W('untruth','/ʌnˈtruːθ/','不实之言；谎话；不真实',
 '说出来的话与事实对不上；有时委婉地说“这不是实话”。',
 'un- 不 + truth 真实，已有古英语对应形式。旧词族涉及忠诚、真实，现代常用在不实陈述上。',UT,
 'tell an untruth 说不实之言，spread untruths 散播虚假说法；复数 untruths 可强调多条不实陈述。',
 'tell an untruth；spread untruths；a deliberate untruth。',
 'lie 常明确指故意说假话；untruth 有时较委婉、只强调内容不实，但也可直指谎话。不能仅凭换词断定说话者动机。',
 ('The article repeated several untruths about the event.','文章重复了几条关于事件的不实说法。'),('He admitted that he had told an untruth.','他承认自己说了不实之言。'))
R('B3270','真实与不实之言','TRUTH：真相；UNTRUTH：说法与事实不符','已有 truth → truthful，本页接 untruth；较专门的 truther 暂略。',
 'truth 与 untruth 都有古英语历史，现代 un- 帮助识别否定，但不需要把每个旧词都当现代新造。',
 'truth → truthful；un- + truth → untruth。',
 [['真实、诚实与不实','truth · truthful · untruth']],
 'truth 真相、真实性；truthful 诚实的；untruth 不实陈述。',
 'A truthful account should correct the untruths in the report.\n\n一份如实的叙述应纠正报告中的不实之言。',
 'truth truthful untruth')
SI=[['sir 的旧形 sirly','像有身份的老爷 → 高傲、专横'],['sirly → surly','态度粗暴、阴沉、不友好']]
W('surly','英 /ˈsɜːli/；美 /ˈsɜːrli/','脾气暴躁的；粗鲁、不友好的',
 '问一句只得到冷冰冰、没好气的回应，像摆着架子不愿理人。',
 'sir + -ly 的旧形 sirly 原有老爷派头、专横义，后来变成 surly，侧重粗暴、阴沉的态度。这里 -ly 构成形容词。',SI,
 'a surly reply 没好气的答复，a surly waiter 态度不友好的服务员。常形容人的举止和语气。',
 'a surly reply；a surly expression；a surly manner。',
 'surly 是形容词，不能因 -ly 就当副词；shy 害羞可能少说话，surly 则明显有不友好或坏脾气。',
 ('He gave a surly reply and shut the door.','他没好气地答了一句，关上了门。'),('The waiter seemed surly at first, but later became friendly.','服务员起初显得态度冷硬，后来友好了起来。'),sources=['https://www.etymonline.com/word/surly','https://en.wiktionary.org/wiki/surly#English'])
W('yessir','英 /ˈjesɜː/；美 /ˈjesər/','是的，先生；当然、没错〔口语〕',
 '一句 yes, sir 连着说，可以是恭敬回答，也可以带夸张、轻松的肯定语气。',
 'yes + sir，两个常用词连写成感叹词。与 sir 的称呼义直接相关，不与 surly 的坏脾气义相连。',
 [['yes 肯定；sir 尊称','两个并列成分'],['yes + sir → yessir','恭敬应答；强调肯定']],
 '独立回答 Yessir!，常带口语或表演色彩。写正式对白时也可保留 Yes, sir 两词和逗号。',
 'Yessir!；Yessir, I will；an emphatic yessir。',
 'yessir 的态度由场景和语调决定，可能真恭敬，也可能打趣；一般日常回应 yes 就够。',
 ('“Will you be ready at six?” “Yessir!”','“六点能准备好吗？”“没问题，先生！”'),('Yessir, that was the best meal I had all week.','没错，那是我这周吃得最好的一顿。'))
R('B3227','先生尊称与派生态度','SIR：尊称；SURLY：从老爷派头变成没好气','sir 已精讲，接 surly 的贬化，再看 yes + sir 的口语应答。',
 'sir 是历史尊称形式；surly 的旧形 sirly 先说老爷派头，后来侧重粗暴不友好。yessir 则只是肯定回答与尊称结合。',
 'sir + -ly → sirly → surly；yes + sir → yessir。',
 [['尊称及应答','sir · yessir'],['态度贬化','surly']],
 'surly 的 -ly 是形容词后缀；yessir 不保证态度恭敬，需看语调。',
 'His surly reply was far from a polite “Yes, sir.”\n\n他没好气的回答，和礼貌的一句“是的，先生”相去甚远。',
 'sir yessir surly')
WS=[['古英语 west 及 west方向词族','西方、西边'],['western 的现代派生','西部的 → 西部居民、最西边、西方化']]
def WH(f,m):return WS+[[f,m]]
W('midwestern','英 /ˌmɪdˈwestən/；美 /ˌmɪdˈwestərn/','中西部的；美国中西部的',
 '在叫作中西部的地区，英语中尤其常指美国 Midwest 这个传统区域。',
 'mid- 中间 + western 西部的，对应地区名 Midwest。美国地区名是历史地理名称，不要求它今天位于全国最西侧。',WH('mid- + western → midwestern','中西部地区的'),
 'a midwestern town 中西部小镇，midwestern states 中西部各州；指专名地区时常写 Midwestern。',
 'a Midwestern town；Midwestern states；Midwestern life。',
 'midwestern 与 middle of the western part 不总能逐字对应；美国 Midwest 是约定地区名。',
 ('She grew up in a small Midwestern town.','她在美国中西部的一个小镇长大。'),('The novel describes life in several Midwestern states.','小说描写了美国中西部几个州的生活。'))
W('westerner','英 /ˈwestənə/；美 /ˈwestərnər/','西部居民；西方人',
 '从西部地区来的人；参照范围可以是一个国家，也可以是文化意义上的西方。',
 'western + -er，形成人物名词。Westerner 常指西方文化背景的人，具体范围依语境而定。',WH('western + -er → westerner','西部或西方地区的人'),
 'a westerner by birth 生于西部的人，Westerners visiting the region 到访该地区的西方人。先确认句子在比较哪一片地方。',
 'a westerner by birth；Westerners visiting the region；a local westerner。',
 'westerner 不是任何往西走的旅客，通常说来源、居住或文化背景；western 形容词，westerner 人物名词。',
 ('As a westerner, he was used to the dry climate of his home state.','作为本国西部居民，他习惯了家乡州的干燥气候。'),('The museum provides background information for Westerners unfamiliar with the tradition.','博物馆为不熟悉这一传统的西方访客提供背景介绍。'))
W('westernmost','英 /ˈwestənməʊst/；美 /ˈwestərnmoʊst/','最西边的',
 '把几个地点按东西位置排开，站在最靠西那个点上。',
 'western + -most，-most 表在某方向、范围达到最远。不是问大多数西部地区。',WH('western + -most → westernmost','给定范围内最靠西的'),
 'the westernmost island 最西端岛屿，the westernmost point 最西端地点；通常要有明确比较范围。',
 'the westernmost point；the westernmost island；the westernmost edge。',
 'western 西边的，westernmost 最靠西的；范围改变，哪个点最西也可能改变。',
 ('The lighthouse stands on the island’s westernmost point.','灯塔坐落在岛的最西端。'),('We visited the westernmost village in the valley.','我们去了山谷里最西边的村庄。'))
W('westernization','英 /ˌwestənaɪˈzeɪʃən/；美 /ˌwestərnəˈzeɪʃən/','西方化',
 '某地的制度、生活方式或文化做法，逐渐采用通常被认为来自西方的形式。',
 'western + -ization，-ize 表使成为、-ation 表过程；英式也拼 westernisation。具体变化必须按对象说明。',WH('western + -ize + -ation → westernization','采用西方相关做法的过程'),
 'cultural westernization 文化西方化，the westernization of education 教育的西方化。描述历史、社会过程时常见，可用大写 Westernization。',
 'cultural westernization；the westernization of education；a process of westernization。',
 'westernization 不是 modernization 现代化的必然同义词；一句具体说明比笼统说都变西方更有信息。',
 ('The chapter examines the westernization of education during that period.','这一章研究该时期教育的西方化。'),('The author distinguishes westernization from modernization.','作者区分了西方化和现代化。'))
R('B4239','西部的、居民、位置与变化过程','WESTERN：先定参照范围，再看人、最西端或变化','western 已有精讲，相关西北西南形式共享；补中西部、人名词、最西端与西方化。',
 '西方可以是地理方位，也可以是约定地区、文化范围。后缀解释词性，具体所指仍要看上下文。',
 'mid-/north-/south- + western；western + -er/-most/-ization。',
 [['地区形容词','western · northwestern · southwestern · midwestern'],['居民、极端位置与过程','westerner · westernmost · westernization']],
 'Midwest 是历史地区名；westerner 的参照范围要明确；westernmost 是最靠西；西方化与现代化不简单等同。',
 'The westerner travelled to the westernmost village in the region.\n\n这位西部居民来到该地区最西边的村庄。',
 'western northwestern southwestern midwestern westerner westernmost westernization')
if __name__=='__main__':save('continuation_20261030_o',ROOTS,WORDS)
