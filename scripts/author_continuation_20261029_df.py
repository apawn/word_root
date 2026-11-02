"""Deep, teach and exact: simple bases followed by useful extensions."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
def C(a,b,w,m):return [[a+'；'+b,'并列构词部分'],[w,m]]
DE=[['古英语 dēop → 中古英语 deep、depe → deep','深，也已有严肃、强烈等抽象用法'],['现代 deep 词族','从表面往内部的距离；感情、理解等程度深']]
W('deep','/diːp/','深的；深沉的；深刻的；向深处',
 '不是停在表面，而是往里面、往下面走了很远；理解、感情也借深入的画面。',
 '继承古英语 dēop，既有具体深度，也早有严肃、强烈等抽象用法。',DE,
 'deep water 深水，a deep voice 低沉嗓音，deep understanding 深刻理解；dig deep 深挖，也可比喻更努力、调动资源。',
 'deep water；a deep breath；a deep voice；deep in thought。',
 'deep 可以形容深，也可直接作副词到深处；deeply 常表达感情、程度，不能见中文地就一律加 -ly。',
 ('The lake is very deep in the middle.','湖中央很深。'),('She was deep in thought when I arrived.','我到时，她正陷入沉思。'))
W('depth','/depθ/','深度；深刻程度；纵深',
 'deep 是深，depth 把到底有多深拿出来当一个量或特点说。',
 '与 deep + -th 抽象名词后缀对应，中古英语 depthe 等延续旧词族。元音由 /iː/ 对应短 /e/ 是固定历史形式，不是今天所有形容词加 -th 都删一个字母。',DE+[['deep 的历史名词形式 → depth','深 → 深度、深刻性']],
 'at a depth of ten metres 在十米深处，depth of knowledge 知识深度；in depth 深入地、详尽地。',
 'the depth of；at a depth of；in depth；depth of knowledge。',
 'depth 是名词，deep 是形容词或副词：the depth of the lake，a deep lake。depth 与 death 死亡拼写相近但不同。',
 ('The chart shows the depth of the water.','图表显示水深。'),('We discussed the problem in depth.','我们深入讨论了这个问题。'))
W('deepen','/ˈdiːpən/','加深；变得更深、强烈',
 '原来有一定深度，现在再往里走；关系、理解、危机的程度也可随之加强。',
 'deep + -en 使成为、变得，形成动词。这里 -en 不是过去分词标记，deepen 的过去式是 deepened。',DE+[['deep + -en → deepen','深 → 使更深、变得更深']],
 'deepen a channel 挖深水道，deepen understanding 加深理解；a crisis deepens 危机加重，既可主动使之，也可自己发展。',
 'deepen understanding；deepen a relationship；the crisis deepens。',
 'deepen 加深，deeply 深深地；deepen understanding 是动词动作，deep understanding 是名词短语。',
 ('The visit deepened her understanding of local history.','这次参观加深了她对当地历史的了解。'),('The discussion deepened as more people shared their experiences.','更多人分享经历后，讨论变得更加深入。'))
W('deeply','/ˈdiːpli/','深深地；强烈地；深入地',
 '感受、关心或思考不是浅浅碰一下，而是进入很深、影响很大。',
 'deep + -ly 成副词，与旧有相应副词形式有历史联系。现代常修饰情绪、程度及思考等。',DE+[['deep + -ly → deeply','深、强烈的 → 深深地、强烈地']],
 'deeply worried 深感担忧，deeply moved 深受感动，think deeply 深入思考；deeply 是程度和方式，不必物理往下。',
 'deeply worried；deeply grateful；deeply moved；think deeply。',
 'dig deep 常说往深处挖，deeply moved 常说深受感动；两种副词形式的搭配不能机械按中文互换。',
 ('I am deeply grateful for your help.','我深深感激你的帮助。'),('The film made us think deeply about friendship.','电影让我们深入思考友谊。'))
W('deepwater','英 /ˈdiːpwɔːtə/；美 /ˈdiːpwɔːtər/','深水的；深水区域使用的',
 '把地点、设施或作业说明为位于水较深的地方，而不是浅滩附近。',
 'deep 深 + water 水，形成名词前修饰语；也常写 deep-water。不是 deep 加一个名叫 water 的后缀。',C('deep 深','water 水','deepwater','深水区域的、在深水使用的'),
 'a deepwater port 深水港，deepwater exploration 深水勘探。水深的具体标准依领域和设施需求。',
 'a deepwater port；deepwater operations；deepwater exploration。',
 'deepwater 常修饰实际水域、设施；in deep water 两词固定也可说陷入麻烦，不能看到它就都想成航海工程。',
 ('The city built a deepwater port for larger ships.','城市为较大型船舶建了深水港。'),('The article describes deepwater exploration.','文章介绍了深水勘探。'))
R('B3043','深、深度；深入、加深','DEEP：从表面往内部走，而非只碰表层','水有物理深度，理解、感情也有深入程度；depth 把深拿来量，deepen 把深变成变化动作。',
 'deep 接古英语 dēop，古早已有具体和抽象用法。depth 是历史 -th 名词对应，deepen 的 -en 则形成动词，不能把后缀一概而论。',
 'deep → depth；deep → deepen；deep → deeply；deep + water → deepwater。',
 [['性质、深度与变化','deep · depth · deepen · deeply'],['深水用途','deepwater']],
 'depth 名词，deepen 动词，deeply 副词；deepwater port 深水港，in deep water 可比喻陷入麻烦。',
 'The in-depth discussion deepened our understanding.\n\n深入讨论加深了我们的理解。',
 'deep depth deepen deeply deepwater')
TE=[['古英语 tǣċan → 中古英语 techen → teach','指示、展示、指导、教导'],['现代 teach 词族','让人学会；教学者、活动及可教性']]
W('teach','/tiːtʃ/','教；教会；使人懂得',
 '把方向、做法或道理展示、解释给别人，让他有机会学会；不只课堂里站着讲。',
 '接古英语 tǣċan，已有指示、展示、教导等用法。变化 teach—taught—taught，不能按现代拼写随意拆 tea 茶 + ch。',TE,
 'teach English 教英语，teach someone to swim 教某人游泳，teach someone how to do something 教人怎样做；经验也能 teach us a lesson。',
 'teach someone something；teach someone to；teach at a school；teach a lesson。',
 'teach 教，learn 学；She teaches me French 是她教我法语，I learn French from her 是我向她学法语。',
 ('My uncle taught me to swim.','叔叔教会了我游泳。'),('The experience taught us to prepare more carefully.','这次经历让我们懂得应更认真地准备。'))
W('teacher','英 /ˈtiːtʃə/；美 /ˈtiːtʃər/','教师；教授技能、知识的人',
 '把 teach 这个动作换成做这件事的人；可以教学校课程，也可以教音乐、运动等。',
 'teach + -er 人物后缀，有较早历史对应形式。职业称谓 teacher 不要求每次都在一所学校内工作。',TE+[['teach + -er → teacher','教导 → 从事教导的人']],
 'a schoolteacher 学校教师，a piano teacher 钢琴老师，a driving teacher 驾驶教师；后者也常用 driving instructor。',
 'a language teacher；a piano teacher；a teacher of history。',
 'teacher 教的人，student、learner 学的人；professor 是特定高等教育头衔、职位用词，不是所有 teacher 都叫 professor。',
 ('Our history teacher encouraged us to ask questions.','历史老师鼓励我们提问。'),('She works as a piano teacher.','她是一位钢琴老师。'))
W('teaching','/ˈtiːtʃɪŋ/','教学；教导；学说、教义〔常用复数〕',
 '教人这项工作是一层；把某个人长期教的那些道理作为内容，也可以叫 teachings。',
 'teach + -ing，形成活动名词、动词形式；teachings 复数可集合指所教的道理。不是 teacher 的复数。',TE+[['teach + -ing → teaching','教导活动 → 所教的内容、道理']],
 'teaching experience 教学经验，a teaching method 教学方法；the teachings of a philosopher 某哲学家的学说、教导。',
 'teaching experience；teaching methods；language teaching；the teachings of。',
 'teaching 方法、活动或内容，teacher 是人；a teaching assistant 是助教，不是单纯把两名教师合并成一个词。',
 ('She has ten years of teaching experience.','她有十年教学经验。'),('The book examines the philosopher’s teachings.','书中考察了这位哲学家的学说。'))
W('teachable','/ˈtiːtʃəbəl/','可教会的；愿意学习的；适于教学的',
 '技能能通过教来掌握；人愿意听、愿意改；一个时机又恰好适合把道理讲明白。',
 'teach + -able 可……的，形成可教、易受教的形容词。a teachable moment 是值得把握的教学契机，不是这一分钟自己在听课。',TE+[['teach + -able → teachable','能教 → 技能可教授、人愿学或时机适教']],
 'a teachable skill 可教会的技能，a teachable student 愿意学习的学生，a teachable moment 教育契机。',
 'a teachable skill；remain teachable；a teachable moment。',
 'teachable 可教、愿学，与 talented 有天赋不同；愿受教不说明起点一定更聪明。',
 ('Clear writing is a teachable skill.','清晰写作是一项可以教会的技能。'),('The mistake became a teachable moment for the whole team.','这个错误成了全团队的一次学习契机。'))
R('B2999','教导、展示；教师、教学和可教性','TEACH：指给人看、讲给人懂，再让人学会','teach 是动作，teacher 是人，teaching 是活动或内容，teachable 是能教、愿学或适合教的特点。',
 'teach 继承古英语指示、展示、教导词，过去式、分词 taught。现代 -er、-ing、-able 改变句法角色，不改变教与学两端的方向。',
 'teach → teacher、teaching、teachable；teach—taught—taught 单独记不规则变化。',
 [['动作、人物、活动、性质','teach · teacher · teaching · teachable']],
 'teach 教，learn 学；teaching 不是教师复数；teachable moment 教育契机，不是会学习的一分钟。',
 'The teacher used a teachable moment to teach a useful lesson.\n\n老师抓住一次教育契机，教了一个有用的道理。',
 'teach teacher teaching teachable')
EX=[['拉丁 exigere → 分词 exactus → 英语 exact','驱出、索取；检查、按标准测定等历史用法'],['现代 exact 的分支','精确无差的；动词要求、索取；exacting 要求高']]
W('exact','/ɪɡˈzækt/','准确、精确的；索取、要求付出',
 '形容词是丝毫不偏；动词则把要求落实到对方身上，要他付出代价或回报。',
 '接拉丁 exāctus，exigere 的过去分词；更远 ex- 向外 + agere 驱动。经检查、标准测量等用法有精确义，也保留索取义，不按现代 ex + act 演戏来拆。',EX,
 'the exact time 准确时间，an exact copy 完全一致的复制品；exact revenge 报复，exact a heavy price 使人付出沉重代价，动词更正式。',
 'the exact time；an exact copy；exact revenge；exact a price。',
 'exact 精确、毫无偏差，accurate 准确，precise 精密、明确，搭配有交叠；exact 作动词时不能仍译精确地。',
 ('Tell me the exact time of the meeting.','告诉我会议的准确时间。'),('The long delay exacted a heavy price from the small business.','漫长延误让这家小企业付出了沉重代价。'))
W('exactly','/ɪɡˈzæktli/','恰好；准确地；正是；完全地',
 '把位置、数量、说法对得刚刚好；单独回应时，就是你说得正对。',
 'exact 精确的 + -ly 成副词。not exactly 在委婉语气里又常说不太算、并不怎么，不止数学上的没有完全相等。',EX+[['exact + -ly → exactly','精确、正好 → 准确地、正是']],
 'exactly ten minutes 恰好十分钟，exactly what I mean 正是我的意思；Exactly! 完全正确；not exactly cheap 不算便宜，常暗示挺贵。',
 'exactly the same；exactly right；exactly what；not exactly。',
 'exact 形容词，exactly 副词：the exact number，exactly ten。I don’t know exactly 不完全清楚，I know exactly 明明白白。',
 ('That is exactly what I meant.','那正是我的意思。'),('The journey took exactly thirty minutes.','旅程恰好花了三十分钟。'))
W('exacting','/ɪɡˈzæktɪŋ/','要求高的；苛求的；费心力的',
 '工作把注意力、技能和耐心都要得很多；人则可能对细节、标准要求很高。',
 'exact 的索取、要求义 + -ing，形成形容词。不是说东西正在变得准确，而是它不断提出高要求。',EX+[['exact 的要求义 + -ing → exacting','要求、索取 → 对人要求高、费力的']],
 'an exacting task 要求很高的任务，an exacting teacher 要求严格的老师，exacting standards 严格标准；可以是必要的精细要求，也可能让人觉得苛刻。',
 'an exacting task；exacting standards；an exacting role。',
 'exacting 要求高，exact 精确；a task is exacting 是任务费心力，不是任务这个东西本身准确。',
 ('Restoring the painting was slow and exacting work.','修复这幅画是一项缓慢而要求精细的工作。'),('The role demands patience and an ability to meet exacting standards.','这个岗位需要耐心，以及达到严格标准的能力。'))
R('B4028','精确无差；要求、索取与严格标准','EXACT：按标准核得准，也能要求对方付出','形容词 exact 准确，exactly 正好；动词 exact 索取、要求，exacting 由这一支说任务、人要求高。',
 'exact 接拉丁 exigere 的分词 exactus，历史有驱动、要求、检查测量等用法。现代按两支读，比把所有词义都硬塞进精确好懂。',
 'exact 精确 → exactly；exact 要求、索取 → exacting。',
 [['精确、正好','exact · exactly'],['要求高与费心力','exacting']],
 'exact time 准确时间；exact a price 要求付出代价；exacting work 要求高，不是正在精确。',
 'The exacting task required us to follow the instructions exactly.\n\n这项要求很高的任务，需要我们准确遵照说明。',
 'exact exactly exacting')
if __name__=='__main__':save('continuation_20261029_df',ROOTS,WORDS)
