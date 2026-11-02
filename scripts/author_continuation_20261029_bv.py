"""Wrong, nice and simple: everyday words with non-obvious histories."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
WR=[['古诺斯语 rangr / vrangr；英语早期 wrang 等形式','歪的、扭曲的；不对的'],['中古英语 wrong → 英语 wrong','不正确、不合适、不公正；出毛病']]
W('wrong','英 /rɒŋ/；美 /rɔːŋ/','错误的；不合适的；不公正的；出问题的',
 '从歪了、不正这个旧画面，理解答案不对、路走错、待遇不公等现代用法。',
 '经古诺斯语 rangr、vrangr 和英语早期相关形式发展，旧义含歪曲、不对。现代 w 不发音；不是把 write 写改几个字母得到 wrong。',WR,
 'the wrong answer 错误答案，the wrong size 不合适的尺寸；go wrong 出岔子，wrong someone 是不公正地对待某人。What’s wrong? 可是怎么了，不一定在责怪谁做错。',
 'be wrong about；go wrong；the wrong way；nothing wrong with；do someone wrong。',
 'wrong 不只表示事实判断错误，也可说不合适或不道德；incorrect 更偏不正确，不总能替代所有 wrong。',
 ('I think we took the wrong bus.','我想我们坐错公交车了。'),('There is nothing wrong with asking for help.','求助没有什么不对。'),('Something went wrong during the upload.','上传时出了点问题。'))
W('wrongly','英 /ˈrɒŋli/；美 /ˈrɔːŋli/','错误地；不公正地',
 '动作或判断朝了不对的方向，也可能让别人受了冤屈。',
 'wrong + -ly，把不正确、不公正的性质用来修饰动作、判断。',WR+[['wrong → wrongly','不对的 → 错误地、不公正地']],
 'wrongly assume 错误地以为；wrongly blamed 被错怪。两者一个偏判断错误，一个偏不公待遇。',
 'wrongly assume；wrongly believe；be wrongly accused；be wrongly labelled。',
 'wrong 自己也可在某些固定结构中作副词，如 spell it wrong；wrongly 常直接修饰动词、分词，不能认为所有副词必须 -ly。',
 ('I had wrongly assumed that the museum was free.','我原先误以为博物馆免费。'),('The parcel was wrongly labelled as fragile.','包裹被错误地标为易碎品。'))
W('wrongful','英 /ˈrɒŋfəl/；美 /ˈrɔːŋfəl/','不正当的；不公正的；法律语境中非法或侵权的',
 '不是简单算错一道题，而是某种行为不应这样做，侵犯了正当利益。',
 'wrong + -ful，形成描述不正当、不公行为的形容词；-ful 不是在这里按容器里装满错误逐字理解。',WR+[['wrong + -ful → wrongful','不公、不当 → 不正当的、不合法的']],
 'wrongful dismissal 不当解雇，wrongful conviction 错判。常见于正式、法律相关文字，具体法律认定还依所用制度和案件。',
 'wrongful dismissal；wrongful conviction；a wrongful act。',
 'wrong answer 普通错误答案，不用 wrongful answer；wrongful 更关注行为不当、不公或侵害权利。',
 ('The documentary follows a campaign against a wrongful conviction.','纪录片跟拍了一场反对错判的行动。'),('The article discusses the meaning of wrongful dismissal.','文章讨论不当解雇这个说法的含义。'))
W('wrongness','英 /ˈrɒŋnəs/；美 /ˈrɔːŋnəs/','错误；不当、不公的性质；不对劲的感觉',
 '先不点名是哪件错事，而是把它哪里不对、为什么不当拿出来看。',
 'wrong + -ness，性质名词；可谈事实错误、道德不当，也可表达直觉中的不对劲。',WR+[['wrong → wrongness','不对的 → 不对、不当这种性质']],
 'the wrongness of an action 行为的不当；a sense of wrongness 一种不对劲的感觉。比 a mistake 更抽象，不主要用来数犯了几个错。',
 'the wrongness of something；a sense of wrongness；recognize the wrongness。',
 'wrongness 是性质，wrongdoing 是不当行为；一份报告的 factual errors 常比 a list of wrongnesses 自然。',
 ('She immediately sensed the wrongness of the arrangement.','她立刻感到这个安排不对劲。'),('The essay examines the moral wrongness of deception.','文章探讨欺骗在道德上的不当。'))
R('B2580','错误；不合适；不公；不对劲','WRONG：从不正到不正确、不公正','旧的歪曲意象帮助记忆；现代一定看语境，答案错、尺寸不合、行为不公不是同一个层面。',
 'wrong 有古诺斯语 rangr、vrangr 背景，经英语早期形式发展；开头 w 不发音。',
 'wrong → wrongly、wrongful、wrongness；wrongdoing 是已经形成的不当行为名词。',
 [['基本判断与方式','wrong · wrongly'],['行为不当及其性质','wrongful · wrongness · wrongdoing']],
 'wrong answer 是答案错；wrongful act 是行为不当；What’s wrong? 常只是问怎么了。',
 'I wrongly assumed that choosing the wrong size was the only thing that could go wrong.\n\n我原先误以为，唯一可能出的问题就是尺寸选错。',
 'wrong wrongly wrongful wrongness wrongdoing')
N=[['拉丁语 nescius → 古法语 nice → 中古英语 nice / nyce','不知情、无知；愚笨等旧义'],['英语 nice 的多阶段词义变化','曾含挑剔、精细等义；后来发展出令人愉快、友善等常用义']]
W('nice','/naɪs/','不错的；令人愉快的；友善的；精细、微妙的',
 '现代最常见是让人觉得舒服、满意；但它的历史起点居然是不知道、无知。',
 '拉丁语 nescius 不知道的，由 ne- 不与知道的词干构成，经古法语进入英语。几个世纪里经过愚笨、挑剔、精细等多种用法，后来出现愉快、友善义；不是一次突然反义转换。',N,
 'a nice day 愉快的一天，be nice to someone 对人友善。a nice distinction 在正式语境却是细微而精确的区别；nice and warm 常说暖和得挺舒服。',
 'nice to meet you；be nice to；have a nice time；nice and quiet；a nice distinction。',
 'nice 是宽泛、常用的肯定词，不一定赞到惊人。a nice distinction 也不是讨人喜欢的区别，而是精细区别。',
 ('It was nice of you to help us move.','你帮我们搬家，真是太好了。'),('We had a nice quiet evening at home.','我们在家度过了一个安静愉快的晚上。'),('The argument turns on a nice distinction between the two terms.','论证的关键在于这两个词之间一个细微而精确的区别。'),sources=['https://en.wiktionary.org/wiki/nice#English','https://www.etymonline.com/word/nice','https://www.ahdictionary.com/word/search.html?q=nice'])
W('nicely','/ˈnaɪsli/','友好地；漂亮地、妥当地；进展顺利地',
 '做出来让人满意，或者对人说得好听、友善。',
 'nice + -ly。现代 e 保留为 nicely；副词继承 pleasant、satisfactory 等现代常用义，也可用于精细、恰当的程度。',N+[['nice → nicely','令人满意、友善的 → 妥当、友善地']],
 'ask nicely 好好地请求；fit nicely 很合适，come along nicely 进展顺利。不是只用来形容人漂亮。',
 'ask nicely；work nicely；fit nicely；come along nicely；nicely done。',
 'nice 形容人或事物，nicely 说明动作怎样进行；speak nicely 是友善地说，look nice 是看起来不错。',
 ('If you ask nicely, she may lend you the book.','如果你好好开口，她也许会把书借给你。'),('The new shelf fits nicely into the corner.','新架子放在角落里很合适。'))
W('niceness','/ˈnaɪsnəs/','友善；和气；令人愉快的性质',
 '把一个人待人舒服、体贴和气这一点，作为一种品质来谈。',
 'nice + -ness，形成抽象名词。现代常接友善、和气义，不是回到拉丁语无知义。',N+[['nice → niceness','友善、令人愉快 → 友善、和气这一性质']],
 'her genuine niceness 她真诚的友善；an appearance of niceness 表面的和气。这个词描述给人的友好感，不必等于所有深层道德品质。',
 'genuine niceness；simple niceness；a reputation for niceness。',
 'niceness 强调和气、友善；kindness 更容易强调关心他人、愿意帮助。两者可重叠，不能只靠微笑就证明所有品德。',
 ('People remembered her for her patience and niceness.','人们记得她的耐心和友善。'),('His niceness made it easy for new students to ask questions.','他的和气让新生敢于开口提问。'))
R('B3345','不错；愉快；友善；另有精细义','NICE：今天的友善、愉快，不能只靠最古老词义理解','这个词能提醒我们：知道来源有助理解，却不能拿古义替代现代义。',
 'nice 经法语来自拉丁语 nescius 不知情的。英语史上有挑剔、精细等多种用法，愉快、友善是后来发展的常用义。',
 'nice → nicely、niceness；精细义在 a nice distinction 等搭配中还能看见。',
 [['现代常用评价','nice'],['动作方式与品质','nicely · niceness']],
 'look nice 看起来不错；ask nicely 好好开口；a nice distinction 是细微精确的区别。',
 'She asked nicely, and he found a solution that worked nicely for everyone.\n\n她好好提出请求，他找到了一种让所有人都满意的解决办法。',
 'nice nicely niceness')
SI=[['拉丁语 simplex → 古法语 simple → 中古英语 symple','一重、一层；不复杂'],['英语 simple','简单、朴素、不加修饰；某些语境也可贬称头脑简单']]
W('simple','/ˈsɪmpəl/','简单的；朴素的；单纯的',
 '从只有一层、没有很多层交织，去想结构不复杂、容易明白或不加装饰。',
 '经法语来自拉丁语 simplex 一重的，对照 duplex 两重的。历史构词含一与折叠、重数的部分；不是现代英语 sim + ple 两个独立词。',SI,
 'a simple explanation 易懂解释，a simple meal 朴素的一餐，a simple design 简洁设计。说 a simple person 可能是在贬人头脑简单，要看语境。',
 'a simple solution；keep it simple；a simple meal；plain and simple。',
 'simple 常肯定简洁，simplistic 却常批评把复杂问题想得过于简单。结构简单的任务也未必实际做起来 easy。',
 ('The instructions are simple and easy to follow.','说明简单明了，容易照着做。'),('We had a simple meal of bread, soup and fruit.','我们简单吃了面包、汤和水果。'))
W('simply','/ˈsɪmpli/','简单地；仅仅；简直；朴素地',
 '可以说表达没绕圈，也可以把多余解释拿走：事情就只是这样，或者实在就是这样。',
 'simple + -ly，历史上较长的 -lely 形式简化成 -ly，现代拼 simply。副词不只有动作简单这一义，还发展出仅仅、强调等用法。',SI+[['simple → simply','简单的 → 简单地、仅仅、强调程度']],
 'explain simply 简单讲明白；simply because 仅仅因为；simply wonderful 简直太棒。put simply 相当于简单说来。',
 'put simply；live simply；simply because；simply not possible。',
 'simply 可以加强语气，不总能译简单地。The view is simply beautiful 是景色实在太美，不是景色美得简单。',
 ('Could you explain the idea more simply?','能把这个想法讲得更简单些吗？'),('I stayed home simply because I was tired.','我待在家里，只是因为累了。'),('The final result was simply wonderful.','最后的结果简直太棒了。'))
W('simplify','/ˈsɪmplɪfaɪ/','简化；使容易理解',
 '把不必要的环节、层次或说法减少，让事情更容易处理。',
 '借自法语 simplifier；现代可对应 simple 的词干 simpl- + -ify 使变成。历史借入与现代可分析的构词关系同时存在。',SI+[['法语 simplifier → 英语 simplify','使简单、简化']],
 'simplify a process 简化流程；simplify an explanation 简化说明。过去式 simplified，动词 -fy 变 -fied。简化可以合理，也可能丢掉关键条件。',
 'simplify the process；simplify the rules；simplify something for beginners。',
 'simplify 是做简化的动作，simple 是简单这一性质；把关键条件也删掉，可能得到 simplistic 那样过分简单化的结论。',
 ('The new form simplifies the registration process.','新表格简化了注册流程。'),('She simplified the explanation without losing the main point.','她简化了解释，同时保留了要点。'))
W('simplistic','/sɪmˈplɪstɪk/','过分简单化的',
 '问题有好几层，却硬说只有一个原因；简单过头，漏掉了该考虑的东西。',
 'simple 的词干 simpl- + -istic，形成现代形容词。常带批评，不只是更长一点的 simple。',SI+[['simple + -istic → simplistic','简单 → 忽视复杂性的过度简单化']],
 'a simplistic explanation 过分简单化的解释；a simplistic solution 把问题看得太简单的解决办法。通常质疑其省掉了关键因素。',
 'a simplistic view；a simplistic explanation；overly simplistic。',
 'simple 可以是优点，simplistic 常是缺点。语言讲得简单清楚，不等于内容肤浅。',
 ('Blaming one person is a simplistic explanation for the failure.','把失败全怪在一个人身上，是过分简单化的解释。'),('The article rejects a simplistic division between good and bad technology.','文章反对把技术简单分成好坏两类。'))
W('simpleton','英 /ˈsɪmpəltən/；美 /ˈsɪmpəltən/','傻瓜；头脑简单的人，贬称',
 '把 simple 的头脑简单义变成人物称呼，有瞧不起人的意味。',
 'simple + 类似人名、姓氏构形的 -ton，形成固定人物称呼。不是 simple + tonne 吨，也不是可自由给所有形容词加的常用人名词规则。',SI+[['simple + -ton → simpleton','头脑简单 → 傻瓜这一贬称']],
 'treat someone like a simpleton 把某人当傻子；小说人物可能这样骂人。不是称赞一个人生活朴素。',
 'treat someone like a simpleton；be mistaken for a simpleton。',
 'simpleton 是带贬义的人物名词；a person with simple tastes 是品味朴素，意思完全不同。',
 ('Don’t treat me like a simpleton; I understand the problem.','别把我当傻子，我明白这个问题。'),('The story shows that the supposed simpleton is the wisest person in the village.','故事说明，那个被认为是傻子的人，其实是村里最有智慧的。'))
R('B2940','简单；朴素；简化与过分简单化','SIMPLE：层次不复杂，表达可以清楚','只有一重的旧构词画面，帮助理解不复杂；是否简化得好，还得看有没有保住关键内容。',
 'simple 经法语来自拉丁语 simplex 一重的。simply 是副词，simplify 是简化，simplistic 常是批评简化过度。',
 'simple → simply、simplify；再对照 simplistic；simpleton 是带贬义的人物称呼。',
 [['简单、表达方式与简化动作','simple · simply · simplify'],['简化过度与人物贬称','simplistic · simpleton']],
 'simple 常肯定，simplistic 常批评；simply wonderful 是简直太棒，不能逐字理解成简单地棒。',
 'Explain it simply, but avoid a simplistic explanation.\n\n把它讲简单些，但别为了简单而漏掉关键复杂因素。',
 'simple simply simplify simplistic simpleton')
if __name__ == '__main__':save('continuation_20261029_bv',ROOTS,WORDS)
