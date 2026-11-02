"""Comparisons in width, scope and completeness."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'B3073':dict(words=['wide','wider','widest'],label='wide → wider → widest：宽度与覆盖范围',note='wide 继承古英语 wīd；比较级、最高级都先去 e，再分别加完整 -er、-est，空间宽度和抽象范围都可比较。'),
 'B3075':dict(words=['broad','broader','broadest'],label='broad → broader → broadest：宽、广与概括层次',note='broad 接古英语 brād，现代既说空间宽，也说观点、问题范围广；不按字母强凑更早词根。'),
 'B3117':dict(words=['full','fuller','fullest'],label='full → fuller → fullest：饱满、完整与充分程度',note='fuller／fullest 常比较装满、描述完整或程度充分；保留原有 ll，直接加 -er／-est。'),
}
W('wider','英 /ˈwaɪdə/；美 /ˈwaɪdər/','更宽的；范围更广的；更宽地；wide 的比较级',
 '把左右两边拉开，是 wider；把参与的人、选择或影响扩展出去，也能说 wider。',
 'wide 去末尾 e，加完整比较级 -er。wide 继承古英语 wīd 宽、远、大等义，现代形容词、副词都可用，比较形式也按场景承担相应功能。',
 [['古英语 wīd → wide','宽阔；范围大、远'],['wide 去 e + -er → wider','更宽；覆盖更多人、事物或范围']],
 'a wider road 更宽的路；a wider range 更广的范围；a wider audience 更多、更广泛的受众；open wider 开得更大。',
 'much wider；a wider choice。','a wider audience 常更强调受众覆盖广，a larger audience 更直接强调人数多，二者可能重叠。wider than ... 比较宽度或范围，longer than ... 常比较长度、时间。',
 ('The new doorway is wider than the old one.','新门口比旧门口宽。'),('The online event reached a wider audience.','这场线上活动触达了更广泛的受众。'),sources=['https://en.wiktionary.org/wiki/wider#English','https://en.wiktionary.org/wiki/wide#English'])
W('widest','/ˈwaɪdɪst/','最宽的；覆盖范围最广的；wide 的最高级',
 '左右展开到最宽，或选择、覆盖范围最大的一项，是 widest。比较的是实际宽度还是抽象范围，要看名词。',
 'wide 去末尾 e，加完整最高级 -est，写 widest。wide 延续古英语 wīd，现代最高级直接比较空间或范围的宽广程度。',
 [['古英语 wīd → wide','宽阔、范围大'],['wide 去 e + -est → widest','所比范围内最宽、最广']],
 'the widest road 最宽的路；the widest range 最广的范围；the widest possible audience 尽可能广泛的受众；at its widest 在最宽处。',
 'the widest part；the widest of the three。','at its widest 可以说同一物体最宽的位置；the widest range 比较的是覆盖种类、选择的范围，不必是一个能拿尺测的东西。',
 ('Measure the table at its widest point.','测量桌子最宽的地方。'),('This shop has the widest range of notebooks in the town.','这家店的笔记本种类在镇上最齐全。'),sources=['https://en.wiktionary.org/wiki/widest#English','https://en.wiktionary.org/wiki/wide#English'])
W('broader','英 /ˈbrɔːdə/；美 /ˈbrɔːdər/','更宽阔的；范围更广、更全面的；broad 的比较级',
 '把视线从一个小点向旁边展开，是 broader。肩膀可以更宽，问题、背景和视角也可以看得更广。',
 'broad + -er，直接加，不改变 oa。broad 继承古英语 brād，经中古英语 brood 等延续；抽象范围义沿空间宽阔感展开。',
 [['古英语 brād → 中古英语 brood → broad','宽、开阔 → 范围广、概括的'],['broad + -er → broader','更宽；讨论、视角等更广']],
 'broader shoulders 更宽的肩膀；the broader context 更大的背景；a broader view 更全面的看法；broader implications 更广泛的影响。',
 'a broader range；a broader understanding。','broader context 是把事情放到更大背景看，不等于加入更多琐碎细节。broader 与 wider 有重叠，但具体搭配有习惯，像 broader context 很常用。',
 ('We need to consider the broader context before deciding.','作决定前，我们得考虑更大的背景。'),('The course gave me a broader understanding of the subject.','这门课让我对这个领域有了更全面的理解。'),sources=['https://en.wiktionary.org/wiki/broader#English','https://en.wiktionary.org/wiki/broad#English'])
W('broadest','/ˈbrɔːdɪst/','最宽阔的；范围最广的；最概括的；broad 的最高级',
 '把范围展开到最大，或把解释放到最宽的层面，就是 broadest。in the broadest sense 常是先按最宽泛的意思来谈。',
 'broad + -est，词尾 /ɪst/。broad 接古英语 brād，空间宽阔与抽象范围广的联系延续到现代最高级。',
 [['古英语 brād → broad','宽、开阔；范围广、概括'],['broad + -est → broadest','给定范围里最宽、最广、最概括']],
 'the broadest shoulders 最宽的肩膀；the broadest range 最广的范围；in the broadest sense 在最广泛的意义上；the broadest terms 最概括的说法。',
 'the broadest view；the broadest possible definition。','in the broadest sense 说明正在放宽词的适用范围，不等于已经给出最精细、最严格的定义。broadest 说覆盖面，most detailed 说细节多。',
 ('In the broadest sense, the project is about helping people share knowledge.','从最广泛的意义上说，这个项目是在帮助人们分享知识。'),('The guide starts with the broadest overview before discussing individual examples.','指南先作最概括的介绍，再讨论具体例子。'),sources=['https://en.wiktionary.org/wiki/broadest#English','https://en.wiktionary.org/wiki/broad#English'])
W('fuller','英 /ˈfʊlə/；美 /ˈfʊlər/','更满的；更饱满、更充分、更完整的；full 的比较级',
 '容器里的东西更多，说明里的信息更完整，声音更饱满，都可以用 fuller。它常比较接近满、充实到什么程度。',
 'full + -er，保留原有 ll，不再加第三个 l。full 继承古英语 full、中古英语 ful；这里讲比较级，描述装满、饱满或内容充分的程度。',
 [['古英语 full → 中古英语 ful → full','装满、完整、充分'],['full + -er → fuller','更满；内容更完整、音色更饱满等']],
 'a fuller account 更完整的叙述；a fuller explanation 更充分的解释；a fuller sound 更饱满的声音；feel fuller 感觉更饱。',
 'a fuller picture；fuller details。','full 虽常译满，实际还可说程度接近满、内容充分，所以 fuller 很常用。a fuller account 说信息更完整，不一定篇幅更长。',
 ('The second report gives a fuller picture of what happened.','第二份报告更完整地呈现了事情经过。'),('They changed the arrangement to give the song a fuller sound.','他们调整了编曲，让这首歌听起来更饱满。'),sources=['https://en.wiktionary.org/wiki/fuller#English','https://en.wiktionary.org/wiki/full#English'])
W('fullest','/ˈfʊlɪst/','最满的；最充分、最完整的；full 的最高级',
 '把内容、程度或充实感推到所比范围里最充分的一端，就是 fullest。to the fullest 常说尽可能充分地。',
 'full + -est，保留原有 ll，词尾 /ɪst/。full 继承古英语 full，装满、完整、充分这些现代用法形成最高级时仍按语境区分。',
 [['古英语 full → full','满、完整、充分'],['full + -est → fullest','最满；程度最充分、信息最完整']],
 'the fullest account 最完整的叙述；the fullest possible explanation 尽可能充分的解释；to the fullest 充分地、尽情地；to the fullest extent 在最大程度上。',
 'enjoy it to the fullest；the fullest details available。','fullest 可比较内容是否完整，不只是数容器里装了多少。to the fullest 是整组表达，通常不把 fullest 单独当一般副词使用。',
 ('The archive contains the fullest account of the expedition we could find.','档案里有我们能找到的关于那次考察最完整的记录。'),('They wanted to enjoy their short visit to the fullest.','他们希望充分利用这次短暂的来访，尽情体验。'),sources=['https://en.wiktionary.org/wiki/fullest#English','https://en.wiktionary.org/wiki/full#English'])
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_ws',ROOTS,WORDS)
 extend_lessons()
