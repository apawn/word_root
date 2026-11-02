"""Common troubles, bunkers, grain, fish and complaints."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'A2238':dict(words=['hassle'],label='近代常用词：hassle 的来源仍有讨论',note='hassle 是近代英语麻烦、纠缠的常用词，更远来源未定；这里只说明常用词史，不把 haste + -le 的一种分析写成定论。'),
 'A1760':dict(words=['hassle','hassled'],label='受纠缠、被琐事缠住的状态',note='hassle + -ed → hassled；-ed 在 /l/ 后读 /d/。'),
 'A1697':dict(words=['bunk','bunker','crater'],label='看似 -er 的整词：掩体、铺位与坑口',note='bunker 的旧来源与苏格兰语相关器物名相连，bunk 铺位反而可能是 bunker 的缩短；crater 经拉丁语接希腊语调酒大碗名，不是普通英语人物尾。'),
 'A1740':dict(words=['barley'],label='旧 -lic 在谷物名中的遗迹：barley',note='barley 承接古英语 bere 大麦与 -lic 的旧组合；它是谷物名，词尾历史与 -ly 相关，但现代不是方式副词。'),
 'A1741':dict(words=['herring','moan','moaning'],label='旧鱼名与真正的 -ing 扩展',note='herring 承接古英语旧鱼名，更远来源未定，末尾不能作为现代分词拆；moaning 则清楚对应 moan + -ing。'),
}
W('hassle','/ˈhæsəl/','麻烦、烦人的琐事；纠缠、找麻烦',
 '本来想办件简单事，却被手续、等待、来回沟通缠住，这些令人烦的小折腾就是 hassle。作动词则说不停催烦、纠缠别人。',
 '近代美式英语中流行，可能与更早方言或其他骚扰词有关，确切来源未定。名词麻烦、烦扰又发展出动词纠缠。',
 [['较早方言等可能材料 → 近代 hassle','形成麻烦、烦扰的口语名词'],['现代名词与动词','烦人的折腾；纠缠、不断烦扰']],
 'avoid the hassle 避免麻烦；too much hassle 太折腾；hassle someone about something 为某事不断烦某人。',
 'save you the hassle；without any hassle。','problem 是很宽泛的问题；hassle 常突出事情烦、费事、反复折腾。小事也可能很有 hassle。',
 ('Booking online saved us a lot of hassle.','网上预订让我们省去了很多麻烦。'),('Stop hassling me about the deadline.','别再为截止时间不停地烦我了。'),sources=['https://www.etymonline.com/word/hassle','https://en.wiktionary.org/wiki/hassle#English'])
W('hassled','/ˈhæsəld/','受纠缠的、被琐事忙得焦头烂额的',
 '事情一件接一件地追着来，或有人不断打扰催促，显得疲惫烦躁，就可以说 hassled。',
 'hassle 去末尾 e 接 -ed；由被烦扰的过去分词，形成被琐事压得忙乱的状态描写。',
 [['hassle 纠缠、烦扰 + -ed','受过或受到烦扰'],['hassled 的状态形容词','疲惫烦躁、被琐事缠住的']],
 'a hassled parent 忙得焦头烂额的家长；look hassled 显得忙乱烦躁；feel hassled 感到不断受催扰。',
 'a hassled expression；hassled by repeated calls。','busy 只说忙；hassled 更常加上被打断、被催、被小事缠得烦的感觉。不是所有忙人都显得 hassled。',
 ('She looked tired and hassled after the long journey.','长途旅行后，她显得疲惫又烦躁。'),('He felt hassled by the repeated phone calls.','接二连三的电话让他觉得烦不胜烦。'))
W('bunk','/bʌŋk/','铺位、上下铺的一层；胡说、瞎话〔另源〕',
 '船上、宿舍里上下叠着的床，一层可叫 bunk。That’s bunk! 则是在说胡说八道，需要换到另一支。',
 '铺位义可能缩自苏格兰等语境的 bunker 座、箱凳等旧义；胡说义缩自 bunkum，而 bunkum 又与 Buncombe 地名及政治话语背景相连。',
 [['bunker 等座、箱凳材料 → bunk 铺位','具体传入细节未定'],['bunkum 缩短为 bunk','无意义的话、胡说']],
 'the top bunk 上铺；the bottom bunk 下铺；a bunk bed 上下铺；a load of bunk 一派胡言。',
 'sleep in a bunk；that’s complete bunk。','bunk 的床位义和胡说义分源。阅读上可与 bunker 连着记，但不能断言所有 bunk 都来自床。',
 ('He slept in the top bunk.','他睡在上铺。'),('She dismissed the story as complete bunk.','她认为那套说法完全是胡说。'),sources=['https://www.etymonline.com/word/bunk','https://en.wiktionary.org/wiki/bunk#English'])
W('bunker','英 /ˈbʌŋkə/；美 /ˈbʌŋkər/','掩体、地堡；高尔夫沙坑；燃料舱等',
 '常见的两幅画面：人躲进坚固掩体；高尔夫球掉进沙坑。具体指什么，要看军事、运动还是船舶语境。',
 '早期苏格兰语相关形式有箱凳、长凳等义，来源未定；后有沙坑、煤舱等发展。军事掩体义又涉及德语 Bunker 的传播。',
 [['苏格兰语 bunker 等器物名称','箱凳、座位等旧义，后来有沙坑、煤舱'],['近代军事等专门用法','掩体、地堡；沿用各领域的专门名称']],
 'an underground bunker 地下掩体；a golf bunker 高尔夫球沙坑；a coal bunker 煤舱、储煤处。',
 'take shelter in a bunker；hit the ball out of a bunker。','bunker 不应按 bunk + 做事的人 -er 解释。铺位 bunk 反而可能从它的旧义缩短而来，历史方向须分清。',
 ('The shelter was built inside an underground bunker.','避难处建在一座地下掩体里。'),('Her ball landed in a bunker beside the green.','她的球落进了果岭旁的沙坑。'),sources=['https://www.etymonline.com/word/bunker','https://en.wiktionary.org/wiki/bunker#English'])
W('crater','英 /ˈkreɪtə/；美 /ˈkreɪtər/','火山口；陨石坑、弹坑等碗状坑',
 '地表凹下一大块，边缘围着、里面像碗，就是 crater 的常见形状。火山口、撞击坑、爆炸坑都可能这样叫。',
 '拉丁语 crater 接希腊语 krater 调和酒水的大碗，后把碗状外形用于火山口，再扩大到其他坑。',
 [['希腊语 krater → 拉丁语 crater','调酒大碗，继而比喻火山口'],['现代 crater 的地形用法','火山口；撞击、爆炸等形成的坑']],
 'a volcanic crater 火山口；an impact crater 撞击坑；craters on the Moon 月面陨石坑；a bomb crater 弹坑。',
 'the rim of a crater；a deep crater。','crater 描写这类坑状地形，并不保证成因是火山。月面很多 crater 来自撞击，需看具体地质背景。',
 ('They walked around the rim of the volcanic crater.','他们沿着火山口边缘行走。'),('The photograph shows several craters on the Moon.','照片显示了月球上的几个陨石坑。'),sources=['https://www.etymonline.com/word/crater','https://en.wiktionary.org/wiki/crater#English'])
W('barley','英 /ˈbɑːli/；美 /ˈbɑːrli/','大麦',
 '一种结谷粒的农作物，可入汤、作麦芽等。词尾虽然像 -ly，现代整个词是植物和谷物名称。',
 '古英语 bærlic 通常分析为 bere 大麦 + -lic，与后来的 -ly 历史材料相连；原来像形容词的形式后来成为谷物名。',
 [['古英语 bere 大麦 + -lic','与大麦有关、像大麦的旧形式'],['bærlic → 中古英语 barli → barley','固定为大麦这一谷物名称']],
 'barley soup 大麦汤；a field of barley 一片大麦田；pearl barley 珍珠大麦、经磨制的大麦粒。名词通常不可数。',
 'grow barley；barley grains。','wheat 是小麦，barley 是大麦；barley 的末尾有旧构词史，但不能把现代 barley 当成方式副词。',
 ('The farmer grows barley in this field.','农民在这块田里种大麦。'),('She added barley to the soup.','她往汤里加了大麦。'),sources=['https://www.etymonline.com/word/barley','https://en.wiktionary.org/wiki/barley#English'])
W('herring','/ˈherɪŋ/','鲱鱼',
 '一种常见成群游动、也常被腌制或熏制食用的海鱼。red herring 还常比喻让人偏离主线的东西。',
 '中古英语 hering 承接古英语 hering、hæring 等鱼名，更远来源未定。有关灰色、鱼群或鱼骨等的分析各有讨论，不能当确定命名故事。',
 [['古英语 hering、hæring → 中古英语 hering','旧鱼名延续'],['现代 herring 与固定表达','鲱鱼；red herring 引开注意的线索、话题']],
 'pickled herring 腌鲱鱼；smoked herring 熏鲱鱼；a red herring 转移注意力的线索或话题。鱼名复数常保持 herring，也见 herrings。',
 'a shoal of herring；a red herring in the argument。','herring 的末尾不是现代动词加 -ing。red herring 可以出现在侦探故事或争论中，意义是干扰主线，不要求真有一条鱼。',
 ('They served pickled herring with bread.','他们端上腌鲱鱼配面包。'),('The question about his age was a red herring.','关于他年龄的问题把讨论引偏了。'),sources=['https://www.etymonline.com/word/herring','https://en.wiktionary.org/wiki/herring#English'])
W('moan','英 /məʊn/；美 /moʊn/','呻吟、低声哀叫；抱怨、发牢骚',
 '疼、难受时拖出一声低低的声音，是 moan；对小事不停说不满，也可以叫 moan。',
 '中古英语 mone、monen 等已有哀叹、悲伤、抱怨材料，可能承接更早英语相关词，细节有讨论。后来也常指低声、不成词的痛苦声。',
 [['中古英语 mone、monen 等','哀叹、抱怨、悲伤'],['现代 moan 名词与动词','低声呻吟；口语抱怨']],
 'moan in pain 痛得呻吟；moan about the weather 抱怨天气；have a moan 发发牢骚〔口语〕。',
 'let out a moan；stop moaning about it。','groan 也可说低沉呻吟、抱怨；moan 常让人想到拖长的哀声。抱怨义重在持续说不满，不需要真发出呻吟声。',
 ('He let out a low moan of pain.','他痛得低声呻吟。'),('They kept moaning about the weather.','他们一直在抱怨天气。'),sources=['https://www.etymonline.com/word/moan','https://en.wiktionary.org/wiki/moan#English'])
W('moaning','英 /ˈməʊnɪŋ/；美 /ˈmoʊnɪŋ/','呻吟；抱怨、发牢骚；moan 的 -ing 形式',
 '听到一阵阵痛苦低声，或听一个人反复抱怨，moaning 都可能出现。听场景，而不只听声音高低。',
 'moan + -ing；由动词形成进行形式、动作名称等。保留呻吟和抱怨两条常见分支。',
 [['moan 呻吟、抱怨 + -ing','持续进行该动作'],['moaning 的动作名词与分词','呻吟声、抱怨行为；正在呻吟或抱怨']],
 'moaning in pain 疼得呻吟；constant moaning 不停发牢骚；moaning about the delay 抱怨耽搁。',
 'a moaning sound；stop the moaning。','moaning 常对抱怨带一点不耐烦的评价；complaining 范围更广，正式提出问题也能用。',
 ('A moaning sound came from the next room.','隔壁传来呻吟声。'),('I’m tired of all this moaning about the food.','我听烦了这些关于饭菜的抱怨。'))
def extend_lessons():
    extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
    save('continuation_20261030_tp',ROOTS,WORDS)
    extend_lessons()
