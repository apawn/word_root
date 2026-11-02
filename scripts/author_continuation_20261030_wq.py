"""Useful degree changes: easy, hard, safe and heavy."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'C0619':dict(words=['ease','easy','easier','easiest'],label='ease → easy → easier → easiest：更省力、更容易',note='easy 与 ease 有历史、现代形式联系，比较形式把 y 变 i；更早法语 aise 的源头仍有讨论。'),
 'B2795':dict(words=['hard','harder','hardest'],label='hard → harder → hardest：更硬、更难、更努力',note='hard 可作形容词、副词，harder／hardest 因此既可比难度，也可比努力程度。'),
 'C1252':dict(words=['safe','safer','safest'],label='safe → safer → safest：保护、风险程度的比较',note='safe 接拉丁 salvus 经法语的安然无恙词族；比较级、最高级都先去 e，再分别加完整 -er、-est。'),
 'B3092':dict(words=['heavy','heavier','heaviest'],label='heavy → heavier → heaviest：重量、强度与负担',note='heavy 接古英语 hefig，和举起的词族相关；现代比较形式 y 变 i，再加 -er／-est。'),
}
W('easier','英 /ˈiːziə/；美 /ˈiːziər/','更容易的；更轻松的；easy 的比较级',
 '原本费劲的事少费一点力，或处境让人轻松一点，就是 easier。它不必说完全不费力，只是在比较。',
 'easy 的 y 前是辅音字母 s，变 y 为 i 加 -er，写 easier。easy 与 ease 对应，历史还有古法语 aisié、盎格鲁法语 eisé 等舒服、自在的材料。',
 [['法语舒适、自在词及英语 ease 相关形式 → easy','舒服、自在 → 不费力、容易'],['easy 变 y 为 i + -er → easier','更容易、更轻松']],
 'easier to understand 更容易理解；make it easier 让它更容易；an easier way 更省力的方法；easier said than done 说来容易做来难。',
 'much easier；a little easier。','easier 已是比较级，不写 more easier。make something easier to do 说降低做事难度；easy to use 的物品也不一定功能简单，只是使用不费劲。',
 ('The larger labels make the boxes easier to identify.','大一点的标签让这些盒子更容易辨认。'),('It is easier to explain with a simple example.','用个简单例子更容易解释。'),sources=['https://en.wiktionary.org/wiki/easier#English','https://en.wiktionary.org/wiki/easy#English'])
W('easiest','/ˈiːziɪst/','最容易的；最轻松的；easy 的最高级',
 '在几种做法里，所需力气、步骤或理解难度最低的那种，是 easiest。比较范围由当前几种选择决定。',
 'easy 变末尾 y 为 i，再加 -est，写 easiest；常读三个音节，注意后面两个短元音的衔接。源头的 easy 与舒适、省力词族相连。',
 [['法语、英语相关舒适词族 → easy','自在、省力 → 容易'],['easy 变 y 为 i + -est → easiest','给定范围内最容易']],
 'the easiest way 最容易的方法；the easiest question 最简单的问题；one of the easiest tasks 最容易的任务之一；easiest to find 最容易找到。',
 'the easiest of the three；our easiest option。','the easiest way to do ... 后面的 to 引出要做的事。easiest 不自动等于 best：省力、用时短、结果好是不同的比较角度。',
 ('This is the easiest way to reach the museum from here.','从这里去博物馆，这样走最省事。'),('We started with the easiest question to build confidence.','我们从最容易的问题开始，先建立信心。'),sources=['https://en.wiktionary.org/wiki/easiest#English','https://en.wiktionary.org/wiki/easy#English','https://www.collinsdictionary.com/dictionary/english/easiest'])
W('harder','英 /ˈhɑːdə/；美 /ˈhɑːrdər/','更硬的；更困难的；更用力、更努力地；hard 的比较级',
 '东西更难压动，是更硬；任务更难克服，是更难；人拿出更多力气，是更努力。harder 把这些阻力、力度的比较放在一起。',
 'hard + -er。hard 继承古英语 heard，早有坚硬、强固、难克服等义；hard 本身也能作副词，所以比较级也可直接修饰动作。',
 [['古英语 heard → hard','坚硬、强固；困难；有力地'],['hard + -er → harder','更硬、更难；更努力、用力地']],
 'a harder surface 更硬的表面；a harder problem 更难的问题；work harder 更努力工作；push harder 更用力推；harder to explain 更难解释。',
 'try harder；much harder than ...。','work harder 是更努力，hardly work 是几乎不工作，hardly 不是把 hard 普通地变成努力地。harder 可修饰动作，也可修饰名词或出现在系动词后。',
 ('The second puzzle was harder than the first.','第二道谜题比第一道更难。'),('We had to push harder to move the heavy door.','我们得更用力推，才能挪动那扇沉重的门。'),sources=['https://en.wiktionary.org/wiki/harder#English','https://en.wiktionary.org/wiki/hard#English'])
W('hardest','英 /ˈhɑːdɪst/；美 /ˈhɑːrdɪst/','最硬的；最困难的；最努力、最用力地；hard 的最高级',
 '在一组里，阻力最大、最难克服，或使出的劲最多，都能说 hardest。是东西硬、任务难，还是人最卖力，要看句子。',
 'hard + -est，词尾读 /ɪst/。hard 的形容词、副词用法延续古英语 heard 的坚硬、强固等材料，最高级也保留两种词性用法。',
 [['古英语 heard → hard','硬、难；努力地、有力地'],['hard + -est → hardest','最硬、最难；最努力地']],
 'the hardest question 最难的问题；the hardest part 最难的部分；try your hardest 尽最大努力；works hardest 工作最卖力。',
 'the hardest thing to do；try our hardest。','the hardest part 常说整件事里最难的一环。try your hardest 强调已经使出最大的努力，不单凭这个短语判断结果有没有成功。',
 ('The hardest part was explaining why the plan had changed.','最难的部分是解释计划为什么变了。'),('Everyone tried their hardest to finish before sunset.','大家都尽最大努力，争取在日落前完成。'),sources=['https://en.wiktionary.org/wiki/hardest#English','https://en.wiktionary.org/wiki/hard#English'])
W('safer','英 /ˈseɪfə/；美 /ˈseɪfər/','更安全的；保护更充分、风险更低的；safe 的比较级',
 '比较两种处境，受到保护更多、出问题的可能更小的一种，可以叫 safer。它是在作相对比较。',
 'safe 去末尾 e，加完整比较级 -er，写 safer；/f/ 保留。safe 经古法语 sauf 接拉丁 salvus 安然无恙，与保存、保护词族相连。',
 [['拉丁 salvus → 法语 sauf → safe','安然无恙、得到保护 → 安全'],['safe 去 e + -er → safer','比较中更安全、风险更低']],
 'a safer route 更安全的路线；a safer place 更安全的地方；feel safer 感觉更安全；a safer choice 更稳妥的选择。',
 'much safer；safer than before。','safer 是相对程度，safe 是基本形容词。a safer choice 常说比较稳妥的做法，具体比较依据由上下文交代。',
 ('The new lights made the path feel safer after dark.','新装的灯让这条小路入夜后更有安全感。'),('They moved the fragile objects to a safer place.','他们把易碎物品移到了更稳妥的地方。'),sources=['https://en.wiktionary.org/wiki/safer#English','https://en.wiktionary.org/wiki/safe#English'])
W('safest','/ˈseɪfɪst/','最安全的；所比范围里最稳妥的；safe 的最高级',
 '把几个选项按受保护程度或出问题的可能来排，最稳妥的一项就是 safest。比较范围仍是关键。',
 'safe 去末尾 e，加完整最高级 -est，拼成 safest；词尾读 /ɪst/。词基经法语接拉丁 salvus，现代最高级按这个 e 结尾词的规则形成。',
 [['拉丁 salvus → 法语 sauf → safe','得到保护、安然无恙'],['safe 去 e + -est → safest','给定比较范围里最安全、最稳妥']],
 'the safest place 最安全的地方；the safest option 最稳妥的选项；the safest way to ... 做……最稳妥的方法。',
 'the safest of the three；our safest choice。','safest 说比较范围里排在最安全一端，不能脱离比较对象理解。比如 safest place in the room，范围明确是这个房间内。',
 ('The cupboard was the safest place to store the glass bowls during the move.','搬家时，那个柜子是存放玻璃碗最稳妥的地方。'),('They discussed which of the three routes was the safest.','他们讨论了三条路线中哪条最安全。'),sources=['https://en.wiktionary.org/wiki/safest#English','https://en.wiktionary.org/wiki/safe#English'])
W('heavier','英 /ˈheviə/；美 /ˈheviər/','更重的；量更大、强度更高、负担更重的；heavy 的比较级',
 '举起来更费劲，是 heavier；雨下得更猛、工作负担更大，也沿着更有分量的感觉来理解。',
 'heavy 的 y 前是辅音字母 v，变 y 为 i 加 -er。heavy 继承古英语 hefig，与 heave 举起词族相关，不是现代英语把 heave 临时改字母造出来。',
 [['古英语 hefig → 中古英语 hevy → heavy','重；负担大、强烈等'],['heavy 变 y 为 i + -er → heavier','重量更大；强度、负担更高']],
 'a heavier bag 更重的包；heavier rain 更大的雨；heavier traffic 更密集的交通；a heavier workload 更重的工作负担。',
 'much heavier；heavier than it looks。','heavier traffic 比的是拥挤程度，heavier rain 比的是雨势；a heavier bag 则通常直接比较重量。',
 ('The bag was heavier than it looked.','这个包比看起来重。'),('We expect heavier traffic near the stadium after the match.','我们预计比赛后体育场附近车流会更密集。'),sources=['https://en.wiktionary.org/wiki/heavier#English','https://en.wiktionary.org/wiki/heavy#English'])
W('heaviest','/ˈheviɪst/','最重的；强度、数量、负担最大的；heavy 的最高级',
 '在几件物品里最压手，或在几段时间里雨量、车流、负担最大，就是 heaviest。',
 'heavy 变末尾 y 为 i 加 -est；常读三个音节。词基 heavy 继承古英语 hefig，其重量、沉重负担的语义延续到现代。',
 [['古英语 hefig → heavy','重；沉重、强烈'],['heavy 变 y 为 i + -est → heaviest','所比范围内最重、强度最大']],
 'the heaviest box 最重的盒子；the heaviest rain 最大的雨；the heaviest traffic 最密集的车流；the heaviest workload 最重的工作量。',
 'the heaviest of the bags；at its heaviest。','heaviest 与 hardest 的尺度不同：heaviest workload 强调负担或工作量大，hardest task 强调任务困难。两者可能重叠，也可能不同。',
 ('Put the heaviest boxes on the bottom shelf.','把最重的盒子放在最下面那层架子上。'),('The heaviest rain came just before dawn.','黎明前那阵雨下得最大。'),sources=['https://en.wiktionary.org/wiki/heaviest#English','https://en.wiktionary.org/wiki/heavy#English','https://www.collinsdictionary.com/dictionary/english/heaviest'])
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_wq',ROOTS,WORDS)
 extend_lessons()
