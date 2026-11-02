"""Useful adverbs, resolve versus certainty, and the defy family."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'A1740':dict(words=['wholehearted','wholeheartedly','unconditional','unconditionally','furious','furiously','mathematical','mathematically','definite','definitely','definitive','definitively','defy','defiant','defiantly'],label='全力、无条件、猛烈与确定结论：常用副词扩展',note='wholeheartedly、unconditionally 等取相应形容词加 -ly。definitely 是肯定、一定，definitively 是决定性地、足以定论地；defiantly 接 defiant，表示公然不服，三者读音和意思都须区分。'),
}
W('wholeheartedly','英 /ˌhəʊlˈhɑːtɪdli/；美 /ˌhoʊlˈhɑːrtɪdli/','全心全意地；完全赞同地',
 '把整颗心都投进去，没有一半赞成、一半保留的感觉。支持、同意、投入都可以用。',
 'wholehearted 全心投入的 + -ly；whole + hearted 把完整的心作为投入程度的比喻。',
 [['whole + hearted → wholehearted','全心投入、毫无保留的'],['wholehearted + -ly','全心全意地；完全、由衷地赞同']],
 'wholeheartedly agree 完全赞同；wholeheartedly support 全心支持；embrace something wholeheartedly 全心接受某事。',
 'wholeheartedly recommend；throw yourself wholeheartedly into something。','wholehearted 是形容词，wholeheartedly 是副词：wholehearted support 是全心的支持，wholeheartedly support someone 是全心支持某人。',
 ('I wholeheartedly agree with your suggestion.','我完全赞同你的建议。'),('She threw herself wholeheartedly into the project.','她全心投入了这个项目。'),sources=['https://www.etymonline.com/word/wholehearted','https://en.wiktionary.org/wiki/wholeheartedly#English'])
W('unconditionally','/ˌʌnkənˈdɪʃənəli/','无条件地、不附带条件地',
 '不是先谈好“你得先做到某事，我才给你”，而是不附加这样的前提。常说无条件支持、接受或投降。',
 'unconditional 无条件的 + -ly；un- 否定 conditional 有条件的，conditional 又与 condition 条件同族。',
 [['un- + conditional → unconditional','没有附加条件的'],['unconditional + -ly','以不附带条件的方式']],
 'love someone unconditionally 无条件地爱某人；accept unconditionally 无条件接受；surrender unconditionally 无条件投降。',
 'support unconditionally；agree unconditionally。','unconditionally 说没有所要求的条件；wholeheartedly 说全心投入、真诚赞同。全力支持仍可能针对特定前提，两词侧重点不同。',
 ('Her parents supported her unconditionally.','她父母无条件地支持她。'),('The army agreed to surrender unconditionally.','那支军队同意无条件投降。'),sources=['https://www.etymonline.com/word/unconditional','https://en.wiktionary.org/wiki/unconditionally#English'])
W('furiously','英 /ˈfjʊəriəsli/；美 /ˈfjʊriəsli/','愤怒地；猛烈地、飞快而拼命地',
 '既可能是气得厉害，也可能只是动作像一股猛劲冲出来。typing furiously 常说飞快敲键盘，未必正在生气。',
 'furious + -ly；furious 经法语接拉丁语 furiosus 狂怒的，与 furia 狂怒相连。狂烈的情绪进一步扩展为动作强烈、快速。',
 [['furious 狂怒、猛烈的 + -ly','以相应强烈方式'],['furiously 的情绪与动作分支','怒气冲冲；猛烈、飞快地']],
 'shout furiously 愤怒地喊；work furiously 拼命干活；pedal furiously 拼命蹬车；type furiously 飞快敲键盘。',
 'blush furiously；wave furiously。','angrily 直接说愤怒；furiously 有时只强调动作强度、速度。看动作和上下文，别把每个 furiously 都译成生气地。',
 ('He shouted furiously at the locked door.','他对着锁住的门愤怒地喊叫。'),('She was typing furiously to finish before lunch.','她飞快地敲着键盘，想在午饭前完成。'),sources=['https://www.etymonline.com/word/furious','https://en.wiktionary.org/wiki/furiously#English'])
W('mathematically','/ˌmæθəˈmætɪkli/','在数学上、按数学方法、从数字计算来看',
 '先不谈感觉，按数字、公式和规则来算，这个角度就是 mathematically。',
 'mathematical 数学的 + -ly，-ical + -ly 常形成书写 -ically，读音里的相关弱音节常合并。更早 mathematics 与学习、数学知识的希腊语词族相连。',
 [['mathematics、mathematical 的数学词族','数学；数学的'],['mathematical + -ly → mathematically','从数学角度、按数学方法']],
 'mathematically possible 数学上可能；mathematically prove 用数学方法证明；mathematically equivalent 数学上等价。',
 'mathematically impossible；mathematically precise。','mathematically possible 只说明按相关数学模型、规则可以，实际做得到还受其他条件影响；不要把可能性和现实可行性混成一件事。',
 ('The two expressions are mathematically equivalent.','这两个表达式在数学上等价。'),('She showed mathematically why the method works.','她用数学方法说明了这个方法为何有效。'),sources=['https://en.wiktionary.org/wiki/mathematically#English'])
W('definitive','/dɪˈfɪnɪtɪv/','足以定论的、决定性的；权威完备的',
 '争了很久，需要一个能把问题定下来的答案，这个答案就可能是 definitive。说一本书 definitive，常是在赞它权威、全面，足以当重要依据。',
 '经法语 definitif 接拉丁语 definitivus，与 definire 划界、确定相连。明确边界的材料，发展出把事情作出最后确定的意味。',
 [['拉丁语 definire、definitivus → 法语 definitif','划定、确定、作出结论'],['现代 definitive','足以定论；权威而完备的']],
 'a definitive answer 决定性的答案；definitive evidence 足以定论的证据；the definitive guide 权威指南。',
 'a definitive account；a definitive statement。','definite 是明确、确定；definitive 更强调最终解决问题、具有定论或权威性。a definite date 是明确日期，不必用 definitive。',
 ('We still don’t have a definitive answer.','我们仍没有一个足以定论的答案。'),('The book is regarded as a definitive guide to the subject.','这本书被视为该领域的权威指南。'),sources=['https://www.etymonline.com/word/definitive','https://en.wiktionary.org/wiki/definitive#English'])
W('definitively','/dɪˈfɪnɪtɪvli/','决定性地、足以定论地；最终明确地',
 '问题本来还悬着，证据、测试或决定把它定下来了。definitively 的重心是把疑问关上、给出可定论的结果。',
 'definitive + -ly，把足以定论、最终明确的性质转成方式或判断程度的副词。',
 [['definitive 足以定论的 + -ly','以能够最终确定的方式'],['definitively 的研究、判断用法','决定性地证实、解决或排除']],
 'definitively prove 决定性地证明；definitively establish 明确而最终地确立；not definitively known 尚无定论。',
 'settle the question definitively；rule something out definitively。','definitely 是一定、肯定；definitively 是足以定论地。I’ll definitely come 是我一定来，不是把 come 改配 definitively。',
 ('The experiment did not definitively resolve the question.','这次实验没有最终解决这个问题。'),('The new evidence definitively established the date of the letter.','新证据最终确定了那封信的日期。'))
W('defy','/dɪˈfaɪ/','违抗、蔑视；使难以做到、无法……',
 '面对要求偏不照做，是 defy an order；某种现象怎么都解释不通，是 defy explanation，像它不肯服从现有解释。',
 '中古英语经古法语 defier、desfier 借入，与放弃忠诚、挑战的历史材料相连；更早接拉丁语 dis- 与信任、忠诚词族。',
 [['古法语 defier、desfier → 中古英语 defien','放弃效忠；挑战、违抗'],['现代 defy 的行为与抽象用法','公然不服从；难以解释、描写等']],
 'defy an order 违抗命令；defy convention 挑战惯例；defy description 难以形容；defy expectations 出乎预料。',
 'defy gravity；defy belief。','deny 是否认，defy 是违抗、挑战；defy explanation 是难以解释，不是拒绝解释。过去式、过去分词 defied。',
 ('She defied the order to remain silent.','她违抗了保持沉默的命令。'),('The beauty of the landscape defies description.','这片风景美得难以形容。'),sources=['https://www.etymonline.com/word/defiant','https://en.wiktionary.org/wiki/defy#English'])
W('defiant','/dɪˈfaɪənt/','公然不服的、挑衅的；坚决反抗的',
 '别人让他低头，他偏抬着头不服从。defiant 描写把反抗摆在态度、表情或行动上的样子。',
 '借自法语 défiant，与 défier 挑战、违抗的动词分词相连。现代英语中可与 defy 的词干变化和 -ant 对应着认识。',
 [['法语 défier → défiant → 英语 defiant','挑战、违抗 → 带反抗态度的'],['defiant 的现代态度描写','公然不服、坚决抵抗、带挑衅意味']],
 'a defiant look 不服气的神情；a defiant response 强硬不服的回应；remain defiant 仍不肯屈服。',
 'a defiant gesture；a defiant tone。','defiant 强调对压力、要求的反抗；confident 是有信心，可以完全不涉及违抗。具体勇敢还是无礼，要看情境。',
 ('He gave her a defiant look.','他向她投去不服气的目光。'),('The team remained defiant after the defeat.','失利后，这支队伍仍不肯服输。'),sources=['https://www.etymonline.com/word/defiant','https://en.wiktionary.org/wiki/defiant#English'])
W('defiantly','/dɪˈfaɪəntli/','公然违抗地、不服气地、挑衅地',
 '态度直接摆出来：我不听、我不退。这种表达反抗的做法可以用 defiantly。',
 'defiant + -ly，把不服从、敢于反抗的形容词转成方式副词。',
 [['defy、defiant 的挑战词族','违抗；带反抗态度的'],['defiant + -ly → defiantly','公然不服从地、带挑衅态度地']],
 'stare defiantly 不服气地盯着；reply defiantly 强硬地回答；stand defiantly 坚决不退地站着。',
 'look defiantly at someone；refuse defiantly。','defiantly /dɪˈfaɪəntli/ 是不服气地；definitely /ˈdefɪnətli/ 是肯定、一定。相近拼写常被混淆，读音和意思差别很大。',
 ('She folded her arms and stared defiantly at him.','她抱起双臂，不服气地盯着他。'),('“I’m staying,” he replied defiantly.','“我要留下。”他不肯退让地回答。'))
def extend_lessons():
    extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
    save('continuation_20261030_tr',ROOTS,WORDS)
    extend_lessons()
