"""Vivid everyday -y words without invented etymological shortcuts."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'A1699':dict(words=['grit','gritty','chunk','chunky','louse','lousy','husk','husky','whack','wacky','grizzly','shabby'],label='颗粒、厚块、破旧与古怪：具体感觉如何成为评价',note='grit + -y → gritty；chunk + -y → chunky；louse + -y → lousy。husky 的声音、强壮义与 husk 相连，犬种名却另有历史；wacky 的更远形成有讨论。grizzly 接灰杂色材料，shabby 接旧 shab；不必把生僻旧基础词另当现代必背单词。'),
}
W('grit','/ɡrɪt/','沙粒、细砂；勇气、毅力',
 '鞋里一点沙，踩上去硌人，就是具体的 grit。形容人有 grit，则是碰到困难还能撑下去的韧劲。',
 '古英语 greot 沙、砂砾，经中古英语及元音变化发展。后来英语又用 grit 表示坚定、勇气，形成现代常见的精神品质义。',
 [['古英语 greot → 中古英语相关形式','沙粒、砂砾'],['现代 grit 的具体与性格义','细砂；遇到困难仍坚持的勇气、毅力']],
 'grit in your shoe 鞋里的沙粒；show grit 表现出毅力；grit your teeth 咬紧牙关，也常比喻硬撑着做。',
 'grit and determination；grit your teeth and carry on。','grit 的毅力义突出承受困难、坚持做；talent 是天赋。具体沙粒通常不可数，不能随意用 a grit 指一粒。',
 ('There was grit in the bottom of my shoe.','我的鞋底里有沙粒。'),('It took grit to start again after the failure.','失败后重新开始需要毅力。'))
W('gritty','/ˈɡrɪti/','有沙粒感的；坚韧的；真实粗粝的',
 '咬一口有细砂，粗粗地磨着，是 gritty；人有硬撑的韧劲也叫 gritty。作品 gritty，则常把艰难、粗粝的现实直接摆出来。',
 'grit + -y，短元音后双写 t。既承接沙粒的具体感觉，也与 grit 的坚定、毅力义以及粗粝现实的评价相连。',
 [['grit 沙粒 + -y → gritty','含砂、摸起来或吃起来有颗粒感'],['grit 的毅力义与 gritty 的评价义','坚韧；呈现粗粝、艰难现实的']],
 'gritty sand 粗砂；a gritty performance 顽强的表现；a gritty drama 真实而粗粝的戏剧。作品义常强调没有把现实修饰得温柔漂亮。',
 'a gritty texture；a gritty account of city life。','grainy 常说颗粒可见的纹理、影像；gritty 常让人想到磨人的粗颗粒，也有顽强、粗粝现实的比喻义。',
 ('The pears had a slightly gritty texture.','这些梨吃起来略有颗粒感。'),('The film gives a gritty picture of life in the city.','影片呈现了真实而粗粝的城市生活。'),('Her gritty performance helped the team recover.','她顽强的表现帮助球队扳回局面。'),sources=['https://www.etymonline.com/word/gritty','https://en.wiktionary.org/wiki/gritty#English'])
W('chunky','/ˈtʃʌŋki/','大块的、有明显块粒的；厚实的、粗厚的',
 '汤里看得见大块蔬菜，是 chunky；毛衣、鞋跟、首饰一块块粗厚，也可以这样形容。核心是块头明显、厚实。',
 'chunk 厚块、大块 + -y。由块的性质，扩展到有大块成分、外形厚重粗壮等描述。',
 [['chunk 大块 + -y','带着块状、厚块的性质'],['chunky 的食物与外观用法','有明显块粒；粗厚、厚实']],
 'chunky soup 大块食材的汤；chunky peanut butter 有花生颗粒的花生酱；a chunky sweater 粗线厚毛衣。',
 'chunky jewellery；chunky boots。','thick 可笼统说厚，chunky 往往还突出块感、粗厚的视觉或口感；smooth peanut butter 则没有明显花生颗粒。',
 ('She served a chunky vegetable soup.','她端上了一份带大块蔬菜的汤。'),('He wore a chunky wool sweater.','他穿着一件粗线厚羊毛衣。'),sources=['https://www.etymonline.com/word/chunky','https://en.wiktionary.org/wiki/chunky#English'])
W('louse','/laʊs/','虱子；讨厌、卑鄙的家伙〔骂人用语〕',
 '具体是寄生在毛发等处的小虫。用来叫人时，是带明显厌恶的贬称。',
 '古英语 lus 经中古英语 lous 等延续，属于很老的日耳曼昆虫名称。复数 lice 保留较早元音交替的结果。',
 [['古英语 lus → 中古英语 lous → louse','虱子这一寄生虫'],['louse 的旧复数与人物比喻','lice 虱子们；可鄙、讨厌的人']],
 'a head louse 一只头虱；head lice 头虱〔复数〕；call someone a louse 骂某人是卑鄙的家伙。',
 'a tiny louse；the plural lice。','单数 louse /laʊs/，复数 lice /laɪs/。人物义属于贬斥，不能当作普通、友好的“家伙”随意称呼别人。',
 ('The picture shows a single head louse.','图片展示了一只头虱。'),('In the novel, she calls the dishonest landlord a louse.','小说中，她骂那个不诚实的房东是个卑鄙的家伙。'))
W('lousy','/ˈlaʊzi/','糟糕的；感觉不舒服的；长虱子的〔本义〕',
 '最早是满身虱子、状况很差；日常评价已经扩大成糟透了。a lousy day 可能只是一天很不顺。',
 'louse 虱子 + -y，表示带有、满是。中古英语已有相应形式，贬义很早扩展到人、物、状况的糟糕。',
 [['louse + -y → lousy','有虱子、虱子滋生的'],['现代评价义扩大','很差、糟糕；身体感觉难受']],
 'a lousy excuse 蹩脚的借口；lousy weather 糟糕天气；feel lousy 感觉很不舒服；be lousy at something 某事做得很差。',
 'a lousy job；feel lousy today。','lousy 是较口语的强烈负面评价。feel lousy 可以是身体难受、精神状态差，具体原因不由这个词单独说明。',
 ('We had lousy weather all weekend.','整个周末天气都很糟。'),('I feel lousy, so I’m going home early.','我感觉很不舒服，准备早点回家。'),sources=['https://www.etymonline.com/word/lousy','https://en.wiktionary.org/wiki/lousy#English'])
W('husky','/ˈhʌski/','声音低沉沙哑的；粗壮的；哈士奇犬、北方雪橇犬',
 '声音 husky，像带着干涩、粗哑的摩擦感；体格 husky，常说粗壮。a husky 则通常是一只雪橇犬，需要换到另一条词源。',
 '形容词接 husk 外壳 + -y，声音义常联系干外壳般的干涩，强壮义联系坚韧。犬名来自北美旧族称相关形式的缩变，历史细节不能按 husk + -y 套。',
 [['husk + -y 的形容词支','有壳；声音粗哑、体格粗壮'],['北美旧称相关形式 → husky 犬名','成为北方雪橇犬的名称，与形容词分源']],
 'a husky voice 低沉沙哑的声音；a husky man 粗壮的男人；a Siberian husky 西伯利亚哈士奇。犬名复数 huskies。',
 'speak in a husky voice；a team of huskies。','husky voice 可以描述有吸引力的沙哑音色，也可以是暂时嗓音粗哑；犬名同形，不能据此断言这种狗因声音沙哑而得名。',
 ('She answered in a low, husky voice.','她用低沉沙哑的声音回答。'),('They saw a husky pulling a small sled.','他们看见一只哈士奇拉着小雪橇。'),sources=['https://www.etymonline.com/word/husky','https://en.wiktionary.org/wiki/husky#English'])
W('whack','/wæk/','猛击、重重敲一下；尝试〔常见于 have a whack at〕',
 '啪地给一下重击，是 whack；have a whack at a task 则像亲自上去试一把。名词、动词都带明显口语感。',
 '近代英语出现的拟声性击打词，确切形成未定。由一次敲打、动作又扩展出尝试等口语用法。',
 [['较早 whack 的击打动词、名词','啪地打、一次重击'],['口语搭配的扩展','试一把；out of whack 表示失调、不正常']],
 'whack a ball 猛击球；give it a whack 敲它一下，也可能依场景说试一把；out of whack 失调、不对劲。',
 'have a whack at the puzzle；knock something out of whack。','hit 很通用；whack 常突出猛地敲、打的感觉。out of whack 属固定口语表达，不必逐字翻成在敲打外面。',
 ('He whacked the ball over the fence.','他猛地把球打过了围栏。'),('Let me have a whack at that puzzle.','让我也来试试那道谜题。'))
W('wacky','/ˈwæki/','古怪的、离奇好笑的〔口语〕',
 '点子、衣服、人物行为怪得跳脱常规，可能让人觉得有趣。wacky 常带轻松、滑稽的语气。',
 '常与较早 whacky 等俚语形式相连，可能进一步联系 whack 击打的材料；确切形成仍有讨论。这里的联系只能作为词源线索。',
 [['较早 whacky 等俚语形式','傻气、古怪的相关称呼'],['现代 wacky','离奇、怪趣、出人意料的']],
 'a wacky idea 怪点子；a wacky comedy 古怪滑稽的喜剧；a wacky sense of humour 怪趣的幽默感。',
 'a wacky invention；a wonderfully wacky character。','wacky 常带玩笑、好玩的感觉，eccentric 较中性地说与众不同；具体赞赏还是嫌弃，要看说话语气。',
 ('He came up with a wacky idea for the party.','他为聚会想出了一个怪点子。'),('The film is full of wacky characters.','电影里满是古怪有趣的人物。'),sources=['https://www.etymonline.com/word/wacky','https://en.wiktionary.org/wiki/wacky#English'])
W('grizzly','/ˈɡrɪzli/','灰熊；灰杂色的〔形容词，较少见〕',
 '最容易遇到的是 grizzly bear 或 a grizzly：北美灰熊。名字里的颜色画面是毛中夹着灰白色、毛尖泛灰的样子。',
 'grizzle 灰杂色的 + -y；grizzle 又经法语 grisel 等灰色材料而来。用于 grizzly bear 后，形容词又可直接作名词称熊。',
 [['法语灰色材料 → grizzle + -y','带灰杂色、泛灰的'],['grizzly bear → 名词 grizzly','固定动物名灰熊']],
 'a grizzly bear 一头灰熊；a grizzly and her cubs 一头灰熊和它的幼崽。不是所有个体都呈明显灰色，名称是沿用的动物称呼。',
 'grizzly habitat；a young grizzly。','grisly /ˈɡrɪzli/ 是可怕、令人毛骨悚然的，和 grizzly 同音但拼写、来源不同。灰熊常用 grizzly。',
 ('A grizzly stood beside the river.','一头灰熊站在河边。'),('The documentary follows a grizzly and her cubs.','纪录片追踪一头灰熊和它的幼崽。'),sources=['https://www.etymonline.com/word/grizzly','https://en.wiktionary.org/wiki/grizzly#English'])
W('shabby','/ˈʃæbi/','破旧的、寒酸的；卑劣、不体面的',
 '衣服磨旧、家具失去光鲜，是 shabby；对人不厚道、做事不体面，也借这种不光彩的感觉来评价。',
 '较早 shab 的皮肤病、粗陋等材料 + -y，历史接中古英语 shabbe、古英语相关词。现代常用义已经集中在破旧外观和不体面的行为。',
 [['旧 shab 相关材料 + -y','外观不好、衣着寒酸等'],['现代 shabby 的物品与行为评价','破旧；待人卑劣、不厚道']],
 'a shabby coat 破旧外套；shabby furniture 破旧家具；shabby treatment 不厚道的对待。not too shabby 是口语“还不错”。',
 'a shabby hotel；a shabby excuse。','shabby 常强调旧、磨损、寒酸；dirty 强调脏，两者可以同时出现但不相同。not too shabby 常是带点轻松的肯定。',
 ('The chairs were shabby but comfortable.','那些椅子虽然破旧，却很舒服。'),('They complained about their shabby treatment.','他们抱怨自己受到了不厚道的对待。'),sources=['https://www.etymonline.com/word/shabby','https://en.wiktionary.org/wiki/shabby#English'])
def extend_lessons():
    extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
    save('continuation_20261030_tk',ROOTS,WORDS)
    extend_lessons()
