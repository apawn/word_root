"""Bird names by sound, activity and mythology; teaching's two noun uses."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
B=[['古英语 bridd、bird 等 → 中古英语 brid、bird → bird','幼鸟等旧义；更早来源不定，词形有音序差别'],['英语 bird 的范围扩大','幼鸟称呼逐渐成为鸟的通称；与较早通称 fowl 的范围变化相伴']]
def BH(f,m):return B+[[f,m]]
W('bird','英 /bɜːd/；美 /bɜːrd/','鸟；某类人〔口语比喻〕',
 '今天是鸟类的普通称呼，历史上却较偏幼鸟；范围从小鸟扩大到各种鸟，不是现代每个 bird 都必须会飞。',
 '古英语 bridd、bird 等接中古英语 brid、bird，深源未定。常见 r 与元音位置变化，但旧变体的先后不强排成唯一链；语义后来扩大，部分替代 fowl 的旧通称用途。',B,
 'a bird in flight 飞行的鸟，feed the birds 喂鸟，an early bird 早起者、提前行动者，a little bird told me 有人私下告诉我。',
 'feed the birds；an early bird；a little bird told me；birds of a feather。',
 'bird 生物类别不等于会飞的所有动物，蝙蝠不是鸟，鸵鸟不会飞也仍是鸟；early bird 是人的比喻。',
 ('A small bird landed on the fence.','一只小鸟落在篱笆上。'),('She is an early bird and starts work before sunrise.','她起得早，日出前就开始工作。'),
 sources=['https://en.wiktionary.org/wiki/bird#English','https://www.etymonline.com/word/birdie'])
W('birdie','英 /ˈbɜːdi/；美 /ˈbɜːrdi/','小鸟〔儿语、爱称〕；小鸟球〔高尔夫，低于标准杆一杆〕',
 '孩子指一只小鸟，birdie 带亲昵语气；高尔夫里，一洞比标准杆少用一杆也叫 birdie，是好成绩。',
 'bird + 亲昵、小称 -ie。高尔夫用法可能接 bird 表出色事物的旧美式俚义，不把某位球手一次击球的故事当唯一确定来源。',BH('bird + -ie → birdie；后有高尔夫分数用法','小鸟爱称；低于标准杆一杆的成绩'),
 'a little birdie 一只小鸟，make a birdie 打出小鸟球，a birdie on the last hole 最后一洞低于标准杆一杆。',
 'a little birdie；make a birdie；a birdie on the last hole。',
 'birdie 高尔夫比标准杆少一杆，eagle 少两杆；这里少用杆数更好，不把鸟的大小当现实物种排名。',
 ('“Look at the birdie,” she said to the child.','她对孩子说：“看那只小鸟。”'),('He made a birdie on the final hole.','他在最后一洞打出了小鸟球。'),
 sources=['https://en.wiktionary.org/wiki/birdie#English','https://www.etymonline.com/word/birdie'])
W('birding','英 /ˈbɜːdɪŋ/；美 /ˈbɜːrdɪŋ/','观鸟、识鸟活动',
 '出门看鸟、听叫声、辨认种类、记录见闻，作为一种兴趣来做；不是指所有鸟正在飞。',
 'bird + -ing，现代常作观鸟活动名。旧时 bird 动词还可猎鸟等，不能把旧活动与现代观鸟兴趣混成同一目的。',BH('bird + -ing → birding','与鸟有关的活动名；现代常观鸟'),
 'go birding 去观鸟，a birding trip 观鸟行程，a birding group 观鸟小组。',
 'go birding；a birding trip；a birding group。',
 'birding 与 birdwatching 常近义，birding 也自然包含听声辨识、记录；不强定只有专业人士才可叫 birding。',
 ('We went birding in the wetlands.','我们去湿地观鸟。'),('Birding has helped her notice the sounds around her.','观鸟让她更留意身边的声音。'))
W('birdwatching','英 /ˈbɜːdwɒtʃɪŋ/；美 /ˈbɜːrdwɑːtʃɪŋ/','观鸟',
 '把观察、辨认野外鸟类当作兴趣；watching 说观察过程，常与听声、记录一起发生。',
 'bird + watching，现代复合活动名。这里 bird 限定观察对象，不是鸟来观察人类的反向主语。',BH('bird + watching → birdwatching','以观察鸟类为兴趣的活动'),
 'go birdwatching 去观鸟，birdwatching binoculars 观鸟望远镜，birdwatching in the park 在公园观鸟。',
 'go birdwatching；birdwatching binoculars；a birdwatching group。',
 'birdwatching 与 birding 大体同义；活动名通常不可数，不按看过三只鸟就说 three birdwatchings。',
 ('She takes binoculars when she goes birdwatching.','她去观鸟时带望远镜。'),('The park is a good place for birdwatching.','公园是观鸟的好地方。'))
W('birdcage','英 /ˈbɜːdkeɪdʒ/；美 /ˈbɜːrdkeɪdʒ/','鸟笼',
 '用来容纳鸟的笼子；cage 的栏格把鸟与外面隔开，不是鸟自己搭的巢。',
 'bird + cage，按容纳对象合成器物名。两个材料并列，不是 bird 发音变化成 cage。',BH('bird + cage → birdcage','用于容纳鸟的笼子'),
 'a large birdcage 大鸟笼，an empty birdcage 空鸟笼，clean the birdcage 清洁鸟笼。',
 'a large birdcage；an empty birdcage；clean the birdcage。',
 'birdcage 人造笼，nest 鸟巢；birdhouse 常人工供栖息、繁殖的小屋，不一定把鸟关住。',
 ('An empty birdcage hung by the window.','窗边挂着一只空鸟笼。'),('The child drew a birdcage with an open door.','孩子画了一只笼门打开的鸟笼。'))
W('mockingbird','英 /ˈmɒkɪŋbɜːd/；美 /ˈmɑːkɪŋbɜːrd/','嘲鸫、模仿鸟〔鸟类名〕',
 '叫声里会模仿其他鸟或环境声音，mocking 抓住模仿这层；不是鸟一定在嘲笑你。',
 'mocking 模仿的 + bird，mock 有模仿、仿效的旧用法，也有嘲弄义。按声音能力命名，不把每种鸣唱都当语言上的讥讽。',BH('mocking + bird → mockingbird','会模仿声音的鸟名'),
 'a mockingbird singing 嘲鸫鸣唱，a northern mockingbird 北美嘲鸫，hear a mockingbird 听见嘲鸫。',
 'a northern mockingbird；hear a mockingbird；a mockingbird singing。',
 'mockingbird 模仿鸣声，hummingbird 的 humming 主要指快速翅动的嗡声，两个鸟名里的声音来源不同。',
 ('A mockingbird sang from the top of the fence.','一只嘲鸫在篱笆顶鸣唱。'),('The guide explained how the mockingbird imitates other sounds.','向导解释了嘲鸫怎样模仿其他声音。'))
W('hummingbird','英 /ˈhʌmɪŋbɜːd/；美 /ˈhʌmɪŋbɜːrd/','蜂鸟',
 '小鸟翅膀快速扇动会发出嗡嗡声，像 hum；得名重点在翼声，不是因为它会像人一样哼流行歌。',
 'humming 嗡鸣 + bird，按快速翅动的声音合成鸟名。',BH('humming + bird → hummingbird','翅动嗡鸣的鸟 → 蜂鸟'),
 'a tiny hummingbird 一只小蜂鸟，a hummingbird hovering 悬停的蜂鸟，hummingbirds near the flowers 花旁的蜂鸟。',
 'a tiny hummingbird；a hummingbird hovering；hummingbirds near flowers。',
 'hummingbird 是鸟，bumblebee 是蜂；中文都带蜂字，不能因此混成同一种动物。',
 ('A hummingbird hovered beside the flower.','一只蜂鸟悬停在花旁。'),('We watched the hummingbird’s rapidly moving wings.','我们看着蜂鸟快速扇动的翅膀。'))
W('thunderbird','英 /ˈθʌndəbɜːd/；美 /ˈθʌndərbɜːrd/','雷鸟〔北美部分原住民传统中的超自然鸟形存在〕',
 '传统叙事中与雷霆、风暴联系的强大鸟形存在，常有振翼带来雷声的形象；不同群体的故事并不完全一样。',
 'thunder 雷 + bird，英语词用来翻译若干北美原住民语言中的相应称呼，不只是有人看见下雨时飞过一只普通鸟便随手起名。',BH('thunder + bird，翻译相应原住民称呼 → thunderbird','与雷霆联系的传统鸟形形象'),
 'the thunderbird in a story 故事中的雷鸟，a thunderbird design 雷鸟图案；具体文化背景要看作品或讲述者。',
 'a thunderbird design；the thunderbird in a story；a thunderbird image。',
 'thunderbird 主要是传统形象，不是所有雷雨天气的鸟；现代软件、车辆等也可借名，专名语境另看。',
 ('The museum label explains the thunderbird design.','博物馆标签解释了雷鸟图案。'),('The storyteller described the thunderbird’s powerful wings.','讲述者描写了雷鸟强有力的翅膀。'),
 sources=['https://en.wiktionary.org/wiki/thunderbird#English','https://www.etymonline.com/word/thunderbird'])
W('firebird','英 /ˈfaɪəbɜːd/；美 /ˈfaɪərbɜːrd/','火鸟；火焰色鸟类的俗名；童话中的神奇火鸟',
 '火红、橙红或像发光火焰的鸟形象都能借这个名字；童话、芭蕾中常是带魔力的火鸟，不是普通鸟被烧着。',
 'fire 火、火焰形象 + bird，可按羽色、光辉命名，也用于俄罗斯等故事中的神奇鸟及《火鸟》作品名。不同用法各按传统，不把所有火鸟强套同一重生剧情。',BH('fire + bird → firebird','火焰羽色、光辉形象 → 鸟名及童话形象'),
 'the Firebird ballet 《火鸟》芭蕾，a firebird in a fairy tale 童话火鸟，a firebird’s feather 火鸟羽毛。',
 'the Firebird ballet；a firebird in a fairy tale；a firebird’s feather。',
 'firebird 不自动等于 phoenix 凤凰，传统、作品情节各有背景；小说里的发光羽毛不当真实生物机制。',
 ('The fairy tale centres on a magical firebird.','童话围绕一只神奇火鸟展开。'),('The dancers rehearsed The Firebird.','舞者们排练《火鸟》。'),
 sources=['https://en.wiktionary.org/wiki/firebird#English','https://www.mariinsky.ru/en/playbill/repertoire/ballet/jarpt/'])
R('B2627','幼鸟旧称到通称；声音、活动与传统形象命名','BIRD：先是较小的幼鸟称呼，后来成了鸟类常用总名','bird → birdie；birding、birdwatching 观鸟；birdcage、birdhouse 等设施；声音、颜色、传统中的各类鸟名分组。',
 'mockingbird 取模仿声音，hummingbird 取翅动声；thunderbird、firebird 是各自传统形象，不能套成同一种普通鸟。',
 'bridd、bird 等 → bird；bird + -ie/-ing；bird + watching/cage/house/song 等；mocking/humming/thunder/fire 等 + bird。',
 [['基础与兴趣活动','bird · birdie · birding · birdwatching'],['设施、鸣声与环境','birdcage · birdhouse · birdsong · birdlife · seabird · snowbird'],['声音、颜色与其他鸟名','mockingbird · hummingbird · blackbird · bluebird · songbird · ladybird'],['传统中的鸟形象','thunderbird · firebird']],
 'bird 不等于会飞动物；birdie 高尔夫少一杆；mockingbird 模仿鸣声、hummingbird 翼声；birdcage 笼与 nest 巢；ladybird 实为甲虫。',
 'We went birdwatching and saw a hummingbird near the flowers.\n\n我们去观鸟，在花旁看到一只蜂鸟。','bird birdie birding birdwatching birdcage birdhouse birdsong birdlife seabird snowbird mockingbird hummingbird blackbird bluebird songbird ladybird thunderbird firebird')
R('B3900','教学活动与教导、教义内容','TEACHING：可说怎样教，也可说传下来的观点是什么','teaching 作为教学过程常不可数；teachings 复数可说某人的教导、学说。',
 'teaching methods 是教学方法，the teachings of a philosopher 是哲人的教导。别只因同形都译成正在上课。',
 'teach + -ing → teaching；动作名词与内容名词分义。',
 [['过程与内容','teaching']],
 'teaching 活动，teachings 常教导内容；teacher 人，不等于 teaching 这项活动。',
 'Her teaching helped us understand the philosopher’s teachings.\n\n她的教学帮助我们理解了那位哲人的教导。','teaching')
if __name__=='__main__':save('continuation_20261030_ed',ROOTS,WORDS)
