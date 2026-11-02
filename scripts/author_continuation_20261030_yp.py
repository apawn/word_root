"""Useful abstract nouns: solutions, choices, circumstances and consequences."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'C1364':dict(words=['solution','solutions'],label='solution → solutions：解开与解决办法、溶液',note='拉丁松开、解开词族发展出不同专门义，名词有独立借入路线。'),
 'C1478':dict(words=['technique','techniques'],label='technique → techniques：技艺与具体做法',note='希腊技艺词经法语借入，现代常说完成任务的具体方法。'),
 'C1379':dict(words=['aspect','aspects'],label='aspect → aspects：朝向、样子与方面',note='观看词族发展为从不同方向看到的样子、方面。'),
 'B3762':dict(words=['purpose','purposes'],label='purpose → purposes：意图与用途',note='法语提出、放到面前相关材料发展为意图，词形有历史重塑。'),
 'B2917':dict(words=['statement','statements'],label='statement → statements：说出的内容与文字记录',note='state 陈述加 ment，现代可数不同说法、正式声明或报表记录。'),
 'C1211':dict(words=['regulation','regulations'],label='regulation → regulations：调节与一条条规定',note='英语从 regulate 形成动作名词，再有具体规章义。'),
 'C0720':dict(words=['memory','memories'],label='memory → memories：记忆与一次次回忆',note='拉丁记忆词经法语借入，现代总体能力与具体回忆分开。'),
 'C0159':dict(words=['challenge','challenges'],label='challenge → challenges：质疑、挑战与难题',note='旧指控、争辩词族发展为挑战，现代不带原来诬告义的必然含义。'),
 'C0153':dict(words=['chance','chances'],label='chance → chances：发生、偶然与机会',note='落下、发生词族经法语发展，机会与可能性按语境区分。'),
 'B3613':dict(words=['choice','choices'],label='choice → choices：选择、选项与决定',note='法语借入和本族相关形式共同参与发展，与 choose 不是简单改字母关系。'),
 'C1317':dict(words=['consequence','consequences'],label='consequence → consequences：跟在后面的结果',note='跟随词族的名词借入，结果本身未必不利。'),
 'A1771':dict(words=['situation','situations'],label='situation → situations：所处位置与具体情境',note='拉丁位置材料经法语借入，现代 situate 与名词互相对应。'),
 'B2632':dict(words=['answer','answers'],label='answer → answers：回应与答案',note='本族回应词延续，现代 w 通常不发音。'),
}
W('solutions','/səˈluːʃənz/','解决办法、答案；溶液〔solution 的复数〕',
 '把难题的结解开，得到的办法是 solutions；把物质溶开形成的均匀体系，也叫 solutions。两种用法都接在较早松开、解开的词族里。',
 'solution + -s，/n/ 后读 /z/。拉丁 solvere 的分词词干 solūt- 形成 solūtiō，经古法语及拉丁借入英语，名词不是现代 solve 临时换尾才第一次出现。',
 [['拉丁 solvere → solūt-、solūtiō → 法语、英语 solution','松开、解开 → 解法、溶解等义'],['solution + -s → solutions','多个办法、答案；多份或多种溶液']],
 'possible solutions 可能的解决办法；solutions to a problem 问题的解法；salt solutions 盐溶液。',
 'solutions discussed by the team；solutions prepared for the experiment。','问题的解决办法常接 to。实验语境的 solutions 指溶液，题目、讨论语境则常是解法，不能只靠一个中文义处理。',
 ('The team discussed several possible solutions.','团队讨论了几种可能的解决办法。'),('The students compared two salt solutions.','学生们比较了两份盐溶液。'),sources=['https://en.wiktionary.org/wiki/solutions#English','https://en.wiktionary.org/wiki/solution#English'])
W('techniques','/tekˈniːks/','技法、技巧；具体方法〔technique 的复数〕',
 '把一件事做好所用的具体招法，是 techniques；绘画怎样下笔、采访怎样提问，都可以各有一套技法。',
 'technique + -s，/k/ 后读 /s/。technique 借自法语，其名词来自技术性的形容词，较早接希腊 tekhnikos、tekhnē 技艺；不是 technology 的缩写。',
 [['希腊 tekhnē、tekhnikos → 法语 technique','技艺、技术性的 → 技法名称'],['technique + -s → techniques','多种具体操作方法']],
 'painting techniques 绘画技法；teaching techniques 教学方法；techniques for remembering names 记名字的技巧。',
 'techniques used by experienced teachers；learn new techniques。','techniques 常落到怎么做的具体方法上；technology 常说技术体系、应用。发音重心在 /niːk/，词尾 que 读 /k/。',
 ('The course introduces several painting techniques.','这门课介绍几种绘画技法。'),('She uses simple techniques to help students remember names.','她用简单的技巧帮助学生记住名字。'),sources=['https://en.wiktionary.org/wiki/techniques#English','https://en.wiktionary.org/wiki/technique#English'])
W('aspects','/ˈæspekts/','方面；外观、朝向等〔aspect 的复数〕',
 '同一件事，换一个方向去看，就显出另一个方面；把这些不同的观察面分开谈，就是 aspects。',
 'aspect + -s，/t/ 后读 /s/。拉丁 ad- 朝向与 specere 看形成 aspicere，再有 aspectus 观看、样子；经法语或拉丁借入英语。',
 [['拉丁看词族 → aspicere、aspectus → aspect','朝向看、样子 → 所见的一个方面'],['aspect + -s → aspects','多个方面、不同外观或朝向']],
 'different aspects 不同方面；practical aspects 实际操作方面；aspects of the problem 问题的各方面。',
 'aspects considered in the report；aspects of daily life。','aspect 常是分析时选取的某一面，part 更容易说整体的一部分。aspects of something 的 of 后交代正在看哪件事。',
 ('The report considers several aspects of the problem.','报告考虑了这个问题的几个方面。'),('The course explores different aspects of daily life in the past.','课程探讨过去日常生活的不同方面。'),sources=['https://en.wiktionary.org/wiki/aspects#English','https://en.wiktionary.org/wiki/aspect#English'])
W('purposes','英 /ˈpɜːpəsɪz/；美 /ˈpɜːrpəsɪz/','目的；用途〔purpose 的复数〕',
 '想把事情做向哪里，是目的；某样东西拿来做什么，是用途。purposes 把这些目标或使用方向一项项数出来。',
 'purpose + -s，/s/ 后增加 /ɪz/。purpose 经法语 purpos、porpos 意图等词借入，与 por- 向前、poser 放置等历史形式相连；现代 pur 不是可随意拆用的万能前缀。',
 [['法语 purpos、porpos 等 → purpose','提出、放到面前的概念 → 意图、目标'],['purpose + -s → purposes','多个目的、用途']],
 'for different purposes 为不同用途；for educational purposes 用于教育；serve several purposes 有几种用途。',
 'purposes of the visit；equipment used for many purposes。','for...purposes 常说明用途或做这件事的范围。on purpose 是故意的固定短语，通常用单数 purpose，别机械套上这里的复数。',
 ('The room is used for several different purposes.','这个房间有几种不同用途。'),('The photographs are kept for educational purposes.','这些照片留作教学用途。'),sources=['https://en.wiktionary.org/wiki/purposes#English','https://en.wiktionary.org/wiki/purpose#English'])
W('statements','/ˈsteɪtmənts/','说法、陈述；声明；账单、报表；程序语句〔复数〕',
 '把内容明确说出来或写下来，就得到一条 statement；正式声明、账户往来记录、程序中的一条指令，各自在陈述、列明的用途上发展。',
 'statement + -s，/t/ 后读 /s/。state 陈述 + -ment 行为或结果 → statement；再加普通复数。不同领域把说出、列明的结果固定成专门名称。',
 [['state + -ment → statement','陈述动作 → 说出的内容、写下的说明'],['专门用法发展；statement + -s → statements','多个说法、声明、报表或程序语句']],
 'official statements 正式声明；bank statements 银行账户对账单；false statements 虚假陈述；program statements 程序语句。',
 'statements made at the meeting；statements printed each month。','statement 不自动保证内容真实，事实判断还看证据。bank statements 是列明账户往来的记录，不能只译成银行发布的声明。',
 ('The report compares statements made by several witnesses.','报告比较了几位证人的陈述。'),('She keeps her bank statements in a folder.','她把银行对账单放在一个文件夹里。'),sources=['https://en.wiktionary.org/wiki/statements#English','https://en.wiktionary.org/wiki/statement#English'])
W('regulations','/ˌreɡjəˈleɪʃənz/','规章、规定〔regulation 的复数〕',
 '为了让大家按同一套要求做事，订出一条条规定，就是 regulations。老词里的尺、规则画面能帮你把握按规矩调整的意思。',
 'regulation + -s，/n/ 后读 /z/。regulate 接晚期拉丁 regulāre 按规则指导，联系 rēgula 尺、规则；英语由 regulate 形成 regulation，再发展出具体规定义。',
 [['拉丁 rēgula、regulāre → regulate → regulation','尺、规则 → 调整、按规则管理'],['具体规章义 + -s → regulations','一条条管理规定']],
 'safety regulations 安全规定；follow the regulations 遵守规定；regulations for the competition 比赛规章。',
 'regulations displayed at the entrance；regulations governing the event。','regulation 单数或不可数用法还可说调节、管理过程；regulations 常是一条条可列出的规定。这里学一般词义，具体内容要看对应组织文本。',
 ('The competition regulations are posted at the entrance.','比赛规章张贴在入口处。'),('The team read the regulations before entering the event.','团队参赛前阅读了规章。'),sources=['https://en.wiktionary.org/wiki/regulations#English','https://www.etymonline.com/word/regulation'])
W('memories','/ˈmeməriz/','回忆；记忆中的事情〔memory 的复数〕',
 '过去经历过的事，能在脑中重新浮现的一幅幅画面，是 memories；这里数的是具体回忆，和记忆能力总体不同。',
 'memory 的 y 前是辅音 r，变 y 为 i，加 -es → memories，词尾读 /z/。memory 经法语 memoire、memorie 接拉丁 memoria，联系 memor 记着的。',
 [['拉丁 memor、memoria → 法语 → memory','记得 → 记忆、回忆'],['memory → memories','变 y 为 i 加 es；多段具体回忆']],
 'childhood memories 童年回忆；happy memories 快乐回忆；bring back memories 勾起回忆。',
 'memories of the old house；memories recorded in a diary。','a good memory 常说记性好；good memories 常说美好回忆。memory 的计算机存储义还有专门语境，这里先掌握人的具体回忆。',
 ('The song brought back memories of school.','这首歌勾起了上学时的回忆。'),('She wrote down her childhood memories.','她写下了童年的回忆。'),sources=['https://en.wiktionary.org/wiki/memories#English','https://en.wiktionary.org/wiki/memory#English'])
W('challenges','/ˈtʃælɪndʒɪz/','挑战、难题；质疑〔复数〕；向……挑战、质疑〔第三人称单数〕',
 '一件事要求你拿出能力来应对，是 challenges 的难题义；面对一个说法，要求它经得起检验，则是质疑。',
 'challenge + -s，/dʒ/ 后增加 /ɪz/。拉丁 calumnia、calumniārī 指控、诬告等材料，经法语指控、争辩词族进入英语，后来发展到挑战、困难任务，旧诬告色彩逐渐淡出。',
 [['拉丁指控词族 → 法语 → challenge','指控、争辩 → 提出质疑、要求交锋'],['challenge + -s → challenges；任务义扩展','多项挑战；单数主语质疑、发起挑战']],
 'face challenges 面对挑战；technical challenges 技术难题；challenges the idea 质疑这个想法。',
 'challenges facing the team；challenges the usual explanation。','challenges 可以是困难，也可以是有助于成长的任务，不自动等于坏事。动词 challenges a claim 是要求这个主张经得起检验。',
 ('The team faces several technical challenges.','团队面临几个技术难题。'),('The study challenges the usual explanation.','这项研究对通常的解释提出了质疑。'),sources=['https://en.wiktionary.org/wiki/challenges#English','https://www.etymonline.com/word/challenge'])
W('chances','英 /ˈtʃɑːnsɪz/；美 /ˈtʃænsɪz/','机会；可能性〔复数〕；碰巧〔第三人称单数〕',
 '事情有可能这样发生，是 chances 的可能性义；一个可以采取行动的空当，则是机会。两者都和事情会不会发生有关。',
 'chance + -s，/s/ 后增加 /ɪz/。chance 经古法语 cheance 追到重建通俗拉丁 *cadentia，联系 cadere 落下、发生；星号表示重建形式。',
 [['拉丁 cadere → *cadentia → 古法语 cheance → chance','落下、发生 → 偶然、可能与机会'],['chance + -s → chances','多个机会；可能性；单数主语碰巧']],
 'chances of success 成功的可能性；get chances 获得机会；take chances 冒险；chances upon 偶然发现。',
 'chances to practise；chances of rain。','chances to do 常说做事机会；chances of something 常说发生的可能性。take chances 是冒风险的固定表达，不总是把机会抓住。',
 ('The course gives students more chances to practise speaking.','这门课给学生更多练习口语的机会。'),('The chances of finding an empty seat were small.','找到空座位的可能性很小。'),sources=['https://en.wiktionary.org/wiki/chances#English','https://en.wiktionary.org/wiki/chance#English'])
W('choices','/ˈtʃɔɪsɪz/','选择、选项；作出的决定〔choice 的复数〕',
 '摆在面前可挑的几条路，是 choices；实际挑了哪一条，也可以称为你的 choice。因此复数可说选项，也可说一次次决定。',
 'choice + -s，/s/ 后增加 /ɪz/。choice 经法语 chois 等选择词借入，并与英语本族相关形容词材料交汇；较早与 choose 同属选择词族，不是现代把 choose 改字母直接造名词。',
 [['法语 chois 等；英语本族相关形式 → choice','选择动作、选中者；优选的性质共同参与发展'],['choice + -s → choices','多个选项；作出的不同选择']],
 'make choices 作选择；different choices 不同选项；personal choices 个人选择。',
 'choices available on the menu；choices made in the past。','available choices 侧重还能选哪些；past choices 侧重以前作过什么决定。have no choice 是没得选的固定表达，常用单数。',
 ('The menu offers several vegetarian choices.','菜单提供几种素食选项。'),('Our choices today will shape the next stage of the project.','我们今天的选择会影响项目的下一阶段。'),sources=['https://en.wiktionary.org/wiki/choices#English','https://www.etymonline.com/word/choice'])
W('consequences','英 /ˈkɒnsɪkwənsɪz/；美 /ˈkɑːnsɪkwənsɪz/','结果、后果〔consequence 的复数〕',
 '一件事做了之后，跟着出现的事情，就是 consequences。先抓跟在后面的结果，比只背有点吓人的后果更准确。',
 'consequence + -s，/s/ 后增加 /ɪz/。拉丁 cōnsequī 跟随形成 consequentia，经法语进入英语；现代复数把多个后续影响分别数出。',
 [['拉丁 cōnsequī → consequentia → 法语 → consequence','跟随 → 随后出现的结果'],['consequence + -s → consequences','多项后续结果、影响']],
 'unexpected consequences 意外后果；positive consequences 积极结果；consider the consequences 考虑后果。',
 'consequences of the change；consequences that appeared later。','consequences 常在提醒不利结果时出现，但也可明确说 positive consequences。词本身不保证好坏，通常强调结果由前面的事情带来。',
 ('The change had several unexpected consequences.','这项改变带来了一些意料之外的后果。'),('We should consider the consequences before choosing a plan.','选方案前，我们应考虑它可能带来的结果。'),sources=['https://en.wiktionary.org/wiki/consequences#English','https://en.wiktionary.org/wiki/consequence#English'])
W('situations','/ˌsɪtʃuˈeɪʃənz/','情况、情境；处境〔situation 的复数〕',
 '人或事情处在什么条件、什么场合里面，就是 situations 的情境义；像把一个人放进一幅具体场景，再看他面临什么。',
 'situation + -s，/n/ 后读 /z/。经法语接拉丁 situātio、situāre、situs 等位置材料；现代与 situate 使处于对应，但不拆成英语 sit 加一个任意尾巴。',
 [['拉丁位置、安置词族 → 法语 → situation','所处位置、安置 → 所处情境'],['situation + -s → situations','多种情况、不同处境']],
 'difficult situations 困难处境；everyday situations 日常情境；in similar situations 在相似情况下。',
 'situations described in the lesson；situations that require patience。','situation 常把所处的一整个具体局面框出来；circumstances 更容易展开看围着它的各项条件。二者会重叠，读句子时看作者关注点。',
 ('The lessons use everyday situations to teach new words.','课程用日常情境来教新词。'),('She remains calm in difficult situations.','她在困难情况下仍能保持冷静。'),sources=['https://en.wiktionary.org/wiki/situations#English','https://en.wiktionary.org/wiki/situation#English'])
W('answers','英 /ˈɑːnsəz/；美 /ˈænsərz/','回答、答案；解决办法〔复数〕；回答、接听〔第三人称单数〕',
 '有人问了问题，给回去的内容是 answers；电话响了接起来，也用 answer，像对来电作出回应。',
 'answer + -s，词尾 /ə/ 或 /ər/ 后读 /z/。answer 继承古英语 andswaru、andswarian，较早构词与针对性的郑重表态、宣誓答复背景有关；现代普通回应义已很宽。',
 [['古英语 andswaru、andswarian → answer','针对性的答复 → 普通回答、回应'],['answer + -s → answers','多个回答、答案；单数主语回答或接听']],
 'answers to the questions 问题的答案；correct answers 正确答案；answers the phone 接电话；answers a question 回答问题。',
 'answers written on the page；answers the door。','answer 中 w 通常不发音。answers the door 是听见敲门后去开门，抓回应来访这个画面；answers to a question 中 answers 则是名词。',
 ('The answers are printed at the back of the book.','答案印在书的后面。'),('She answers the phone while I speak to the visitor.','我和来访者说话时，她来接电话。'),sources=['https://en.wiktionary.org/wiki/answers#English','https://en.wiktionary.org/wiki/answer#English'])
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_yp',ROOTS,WORDS)
 extend_lessons()
