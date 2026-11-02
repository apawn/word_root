"""Common homographic and irregular forms: posture, placing, hanging, winding."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'B2885':dict(words=['lay','laid'],label='lay 与 laid：把东西放好',note='放置动词 lay → laid → laid；躺卧动词 lie 的过去式也是 lay，需按整句辨认。'),
 'B2890':dict(words=['lie','lay','lain','lied'],label='lie 的两条来源与两套过去形式',note='躺卧 lie → lay → lain；说谎 lie → lied → lied。两条古英语来源不同，不能共用一套过去式。'),
 'B3848':dict(words=['hang','hung','hanged'],label='hung 与 hanged 的常用分工',note='挂衣服、悬挂等通常用 hung；以绞刑处死人通常用 hanged。现代用法是历史上多种挂、悬动词形式合流后的分工。'),
 'B3011':dict(words=['wind','wound'],label='wind 与 wound：缠绕动词的换形',note='缠绕 wind /waɪnd/ → wound /waʊnd/；伤口 wound /wuːnd/ 是另一来源；空气流动的 wind /wɪnd/ 也要按读音与语境区分。'),
 'A1760':dict(words=['wound','wounded'],label='wound 与 wounded：伤口、使受伤',note='使受伤的 wound /wuːnd/ 加 -ed 得 wounded /ˈwuːndɪd/；它不接缠绕的过去形式 wound /waʊnd/。'),
}
W('laid','/leɪd/','放下了、铺设了；下了蛋；lay 的过去式、过去分词',
 '把钥匙放到桌上、把地毯铺到地面，都有让某物落到一个位置的画面。laid 把这个动作放到过去，或接在 have 后表示已经做过。',
 '放置动词 lay 接古英语 lecgan，历史上与躺卧 lie 所接的 licgan 构成使动关系：让某物躺下、处于某位置。laid 由旧过去形式经后续音变与缩合发展而来，不是按普通 played 模式拼出。',
 [['古英语 lecgan 及其过去形式','使处于某位置；放下'],['现代 lay → laid → laid','放置、铺设、产卵的过去与过去分词']],
 'laid the keys on the table 放下钥匙；laid the carpet 铺好地毯；laid an egg 下了一个蛋；laid out a plan 把计划展开、安排清楚。',
 'laid the foundation；laid it flat。','lay the book down → laid the book down；lie down → lay down → have lain down。先看是在放某物，还是人自己躺下，再选形式。',
 ('She laid the keys on the kitchen table.','她把钥匙放在厨房桌上。'),('The hen laid an egg this morning.','那只母鸡今天早上下了一个蛋。'),sources=['https://www.etymonline.com/word/lay','https://en.wiktionary.org/wiki/laid#English'])
W('lain','/leɪn/','躺着、位于等；lie〔躺卧〕的过去分词',
 '人平躺着，或一本书一直搁在那里。have lain 把这种持续过的状态接到现在；had lain 则接到过去某个时点。',
 '躺卧 lie 接古英语 licgan，旧强变化形式包括过去式 læg、分词 legen 等。经过中古英语及后续变化，现代分工固定为 lie、lay、lain。',
 [['古英语 licgan 及 læg、legen 等形式','躺着、处于某位置及其旧变位'],['现代 lie → lay → lain','原形、过去式、过去分词']],
 'had lain awake 曾一直醒着躺在床上；has lain unused 一直闲置；had lain untouched 一直未被动过。这里 lie 可以说人，也可以说东西所在的状态。',
 'have lain there for years；had lain on the floor。','lain 通常接 have、has、had 等，或出现在相应分词结构里。说谎的过去与过去分词都是 lied。',
 ('She had lain awake for hours before falling asleep.','她醒着躺了好几个小时才睡着。'),('The letter had lain unopened on his desk for a week.','那封信在他桌上搁了一周，一直没拆。'),sources=['https://www.etymonline.com/word/lain','https://www.etymonline.com/word/lie','https://en.wiktionary.org/wiki/lain#English'])
W('lied','/laɪd/','说了谎；lie〔说谎〕的过去式、过去分词',
 '知道事情是一回事，却有意说成另一回事。lied 讲的是过去说了假话；lied about his age 是在年龄这件事上说谎。',
 '说谎 lie 接古英语 leogan，与躺卧的 licgan 来源不同。它较早也有强变化形式，后来改用规则的 lied；现代拼写为 lie 去词末 e 再加 -ed。',
 [['古英语 leogan 等说谎词族','说假话；旧变位与躺卧词不同'],['现代 lie + -ed → lied','说谎的规则过去式、过去分词']],
 'lied to someone 对某人说谎；lied about something 在某事上说谎；lied to avoid trouble 为躲麻烦说了谎。',
 'lie → lied → lied；have lied before。','lied to me 是对我说谎；lay beside me 是躺在我身边。这两个 lie 虽然原形同音同形，过去形式与搭配不同。',
 ('He lied about where he had been.','他在自己去过哪里这件事上说了谎。'),('She admitted that she had lied to avoid trouble.','她承认自己为躲麻烦说了谎。'),sources=['https://www.etymonline.com/word/lie','https://en.wiktionary.org/wiki/lied#English'])
W('hung','/hʌŋ/','挂起了、悬着；hang 的常用过去式、过去分词',
 '外套搭上衣钩、画框悬在墙上：东西有个支点，下面垂下来。过去挂了、已经挂好，通常用 hung。',
 '现代 hang 合流了古英语 hon 等使某物悬挂的强变化动词与 hangian 等处于悬挂状态的动词材料；还受其他日耳曼语形式影响。hung 是后来发展并普及的过去形式。',
 [['古英语 hon、hangian 等挂、悬词族','使悬挂；处于悬挂状态'],['后来 hung → 现代 hang、hung、hung','一般悬挂等义的常用变位']],
 'hung a coat 挂了外套；hung a picture 挂了画；hung up the phone 挂了电话；hung out with friends 和朋友待在一起、消磨时间。',
 'hung on the wall；hung from the ceiling。','普通挂东西通常用 hung；说历史人物遭绞刑处死，通常用 hanged。这是常见的用法分工，读旧文献时还会遇到变化。',
 ('He hung his coat by the door.','他把外套挂在门边。'),('A small lamp hung above the table.','桌子上方悬着一盏小灯。'),sources=['https://www.etymonline.com/word/hang','https://en.wiktionary.org/wiki/hung#English'])
W('hanged','/hæŋd/','以绞刑处死；hang 在这一用法中的过去式、过去分词',
 '历史叙述里说某人被判绞刑并处死，常见 was hanged。这个词形把特定的处刑含义标出来。',
 'hang 的历史合流了不同变位的旧动词；带词尾的 hanged 与换元音的 hung 后来形成用法分工。现代 hanged 在绞刑处死义中保留得尤其明显。',
 [['较早 hang 的带词尾过去形式','挂、悬等动作的过去表达'],['现代 hanged 的常见专门分工','用于以绞刑处死的叙述']],
 'was hanged 被施以绞刑；hanged for a crime 因某罪被处以绞刑。普通衣物、画框等的悬挂过去通常用 hung。',
 'hang → hanged → hanged〔常见于绞刑义〕。','hanged 是一个音节，-ed 读 /d/。the picture was hung 与 the prisoner was hanged 中，名词和词形一起帮助确定意思。',
 ('The history book says that the prisoner was hanged.','历史书说那名囚犯被处以绞刑。'),('In the novel, the man was hanged for a crime he did not commit.','在那部小说中，男子因一项自己未犯的罪被处以绞刑。'),sources=['https://www.etymonline.com/word/hang','https://en.wiktionary.org/wiki/hanged#English'])
W('wound','伤口、使受伤 /wuːnd/；缠绕的过去形式 /waʊnd/','伤口；使受伤、伤害感情；另源 wind〔缠绕〕的过去式、过去分词',
 '看到 wound，先听读音、看句子：a wound 是一处伤口；wound the string 则可能是把线绕了起来。同一拼写在这里藏着两条历史。',
 '伤口 wound /wuːnd/ 接古英语 wund，动词与旧 wundian 使受伤相承。缠绕的 wound /waʊnd/ 则接 wind /waɪnd/，上溯古英语 windan 及 wand、wunden 等过去材料。两条来源不能串成同一个意思的发展。',
 [['古英语 wund、wundian → wound /wuːnd/','伤口、使受伤；后来也说感情受伤'],['古英语 windan 及旧过去材料 → wound /waʊnd/','wind〔缠绕〕的过去式、过去分词']],
 'a small wound 一处小伤口；wound someone’s pride 伤害某人的自尊；wound the string around a spool 把线绕在线轴上。最后一处读 /waʊnd/。',
 'a wound on the arm；a deeply wounded person；wind → wound → wound。','风 wind /wɪnd/、缠绕 wind /waɪnd/、伤口 wound /wuːnd/ 要分开记。have wound up the clock 是给钟上好了发条，wound 在这里读 /waʊnd/。',
 ('He had a small wound on his arm.','他手臂上有一处小伤口。'),('The remark wounded her pride.','那句话伤了她的自尊。'),('She wound the string around a wooden spool.','她把线绕在一个木线轴上。'),sources=['https://www.etymonline.com/word/wound','https://www.etymonline.com/word/wind','https://en.wiktionary.org/wiki/wound#English'])
W('wounded','/ˈwuːndɪd/','受伤的；感情受到伤害的；wound〔使受伤〕的过去式、过去分词',
 '身体留下伤，或一句话让人觉得自尊被刺痛，都能用 wounded。作形容词时，重点是受伤后的状态。',
 '伤口词族 wound /wuːnd/ + -ed。词干末尾 /d/ 后的 -ed 读 /ɪd/，全词两个音节；继承古英语 wund、wundian 相关的伤害分支。',
 [['古英语 wund、wundian → wound /wuːnd/','伤口；使受伤'],['wound + -ed → wounded','受伤；感情或自尊受到伤害']],
 'a wounded animal 受伤的动物；wounded pride 受伤的自尊；a wounded look 受伤、委屈的神情；was wounded 受了伤。',
 'slightly wounded；look deeply wounded。','wounded 来自使受伤的 wound /wuːnd/。缠绕 wind 的过去式 wound /waʊnd/ 本身已经是过去形式；winded /ˈwɪndɪd/ 又常说喘不过气。',
 ('They found a wounded bird near the fence.','他们在围栏附近发现了一只受伤的鸟。'),('He tried to hide his wounded pride behind a smile.','他试图用微笑掩饰受伤的自尊。'),sources=['https://www.etymonline.com/word/wound','https://en.wiktionary.org/wiki/wounded#English'])
def extend_lessons():
    extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
    save('continuation_20261030_ua',ROOTS,WORDS)
    extend_lessons()
