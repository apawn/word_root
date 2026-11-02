"""Steadfastness, cringing, wavering and recoil."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
def S(word,base):
 return ['https://en.wiktionary.org/wiki/'+word+'#English','https://www.etymonline.com/word/'+base]
EXISTING_ROOT_ADDITIONS={
 'B3202':dict(words='flinch flinching unflinching unflinchingly'.split(),label='unflinching：不退缩，也不回避难看真相',note='flinch 接旧弯、转开材料，与 link 的更远弯转词族可比较；un- 否定退缩，-ly 写态度、方式，不等于没有感情。'),
 'B4447':dict(words='cringe cringes cringed cringing'.split(),label='cringe：身体畏缩，到心里尴尬得想躲',note='接旧英语、中古英语弯曲、屈服材料；现代尴尬反应不一定真弯腰，cringing 也可能在特定搭配中写卑屈。'),
 'A1740':dict(words='stagger staggering staggeringly'.split(),label='staggeringly：程度大到令人站不稳似的',note='stagger 的旧不稳、推撞材料扩到使人震惊，staggering 再接 -ly；惊人的程度可好可坏，不只夸赞。'),
 'B3706':dict(words='wave waver wavers wavered wavering unwavering unwaveringly'.split(),label='waver：来回动，也在选择、信念上摇摆',note='waver 与 wave 的旧来回摆材料相关，近源有北欧、古英语等分析差别。英语早期犹豫义记录很早，不能把一张摆动意象图当成全部历史先后。'),
 'C1208':dict(words='recoil recoils recoiled recoiling'.split(),label='recoil：向后缩、退，与枪械后坐',note='经法语 reculer，接拉丁 re- 向后与 culus 后部材料，完整俗拉丁连接词形为重建；不是英语 re- 加 coil 卷绕。名词也有法语 recul 的借入背景。'),
}
FLINCH=[['中古英语 flecche 等；法语 flechir、flenchir 弯、转开材料 → flinch','有鼻音形式变化，远源可能接日耳曼弯转词族'],['flinch → flinching → unflinching','受痛、受惊的一缩，也写心理退缩；否定后可描述勇敢面对或坦然直视']]
CRINGE=[['古英语 cringan 及相关使弯形式 → 中古英语 crenge、crenche','弯、屈服、退让的旧材料'],['cringe：畏缩、卑屈 → 尴尬得想躲','现代心理反应借身体收缩的意象，不要求总有可见动作']]
STAGGER=[['北欧不稳、推撞材料 → stakeren 等 → stagger','走不稳、踉跄；更早细节不能只靠现代字形猜'],['使人震惊 → staggering → staggeringly','像震惊得站不稳；现代副词多写程度大得惊人']]
WAVER=[['中古英语 wayveren 等，与 wave 的旧摆动词族相关','有北欧、古英语材料等近源分析差别，旧 -er 属反复动作背景'],['英语犹豫、信念不稳，以及声音、物体摇摆的用法','抽象犹豫的记录很早；学习画面能并列串联，不硬排为所有物理义先于抽象义']]
RECOIL=[['拉丁 re- 向后 + culus 后部；重建 *reculare → 法语 reculer','往后走、退让，不是把现代英语 coil 卷起来'],['法语动词 reculer、名词 recul → 英语 recoil','后退、缩回；后来枪械发射时向后跳的后坐用法发展']]
W('unflinching','/ʌnˈflɪntʃɪŋ/','坚定不退缩的；毫不回避的',
 '痛、压力、难看的事实摆在面前，仍正面看、不缩开，叫 unflinching。既能夸勇气，也能写作品不回避残酷事实。',
 'un- + flinching；内层 flinch + -ing，外层否定退缩。基础词接旧弯、转开材料，不用现代字母随意拼根。',FLINCH,
 'unflinching courage 不退缩的勇气；an unflinching account 毫不回避事实的叙述。',
 'unflinching honesty 毫不闪躲的诚实；unflinching support 坚定支持。',
 'unflinching 不是 unfeeling 无情；一个人可以很难过，却仍愿意直视事实、履行职责。',
 ('She showed unflinching courage under pressure.','压力之下，她表现出毫不退缩的勇气。'),('The film offers an unflinching account of the disaster.','影片对那场灾难作了毫不回避的呈现。'),sources=S('unflinching','flinch'))
W('unflinchingly','/ʌnˈflɪntʃɪŋli/','坚定不退缩地；毫不回避地',
 '面对难题不躲开，面对真相不删掉难看的部分，做事带这种态度就是 unflinchingly。',
 'unflinching + -ly；先用 un- 否定 flinching 退缩性质，再把它写成做事方式。',FLINCH+[['unflinching + -ly → unflinchingly','带不退缩、不回避的态度行动']],
 'looked unflinchingly 毫不退缩地直视；unflinchingly honest 坦诚得毫不闪躲。',
 'faced the truth unflinchingly；unflinchingly described。',
 'unflinchingly 侧重敢于面对，accurately 侧重准确；作品敢呈现不保证细节自动都正确，两个评价要分开。',
 ('She faced the truth unflinchingly.','她毫不回避地面对真相。'),('The writer describes the consequences unflinchingly.','作者毫不回避地写出了后果。'),sources=S('unflinchingly','flinch'))
W('cringes','/ˈkrɪndʒɪz/','畏缩；尴尬、厌恶得想躲〔第三人称单数〕',
 '听见自己年轻时夸张的话，尴尬得恨不得缩进椅子里，是 cringes；不必真的把身体缩起来，心理反应也能这样说。',
 'cringe + -s，/dʒ/ 后词尾读 /ɪz/；基础词接旧弯、屈服材料，现代扩到难堪反应。',CRINGE+[['cringe + -s → cringes','他畏缩，或尴尬、厌恶得想躲']],
 'cringes at old photos 看旧照片觉得尴尬；cringes with embarrassment 尴尬得不自在。',
 'cringes whenever he hears it；cringes at the memory。',
 'cringes 重点在当事人的难堪反应，blushes 是脸红；可以想躲却没脸红，也可以脸红却未必尴尬。',
 ('He cringes whenever he hears his old speeches.','他每次听到自己以前的演讲，都尴尬得想躲。'),('She cringes at the memory of that joke.','她一想到那个笑话就觉得难堪。'),sources=S('cringes','cringe'))
W('cringed','/krɪndʒd/','畏缩了；尴尬、厌恶得不自在了',
 '一句场合不对的话出来，你忍不住替人尴尬，心里缩一下，就是 cringed。旧身体畏缩义与现代心理反应同族相连。',
 'cringe 去 e 加完整 -ed，/dʒ/ 后读 /d/；末尾连读为 /dʒd/，不额外加一个 /ɪd/ 音节。',CRINGE+[['cringe → cringed','过去畏缩，或感到强烈尴尬不适']],
 'cringed at the remark 听到那句话觉得尴尬；cringed with embarrassment 尴尬得缩起来似的。',
 'cringed when he watched it；cringed at his own words。',
 'cringed 不一定是恐惧，也可能是替人尴尬、厌恶或后悔当年的表现；场景决定反应来源。',
 ('I cringed when I watched the old video.','看那段旧视频时，我尴尬得不行。'),('She cringed at how rude her comment had sounded.','想到自己那句话听起来那么粗鲁，她觉得很难堪。'),sources=S('cringed','cringe'))
W('cringing','/ˈkrɪndʒɪŋ/','正在畏缩、感到尴尬；卑屈讨好的',
 '看见尴尬场面，自己也跟着不自在，是 cringing；a cringing apology 在某些语境里则是低声下气、过分卑屈的道歉。',
 'cringe 去 e 加 -ing；现代动作形式，作形容词时也保留旧畏缩、卑屈支线，不只有网络上觉得尴尬的意思。',CRINGE+[['cringe → cringing','畏缩、尴尬的过程；或带卑屈的性质']],
 'cringing with embarrassment 尴尬得不自在；a cringing manner 卑屈的举止。',
 'watching and cringing；cringing at every word。',
 'cringing apology 带过分低声下气的评价，sincere apology 只说诚恳；不一定所有真心道歉都卑屈。',
 ('I was cringing throughout the awkward interview.','那场采访太尴尬，我看得一直不自在。'),('His cringing manner made the conversation uncomfortable.','他那低声下气的举止让谈话变得不舒服。'),sources=S('cringing','cringe'))
W('staggeringly','英 /ˈstæɡərɪŋli/；美 /ˈstæɡərɪŋli/','惊人地；大得、高得令人震惊地',
 '价格高到让你听完一愣，叫 staggeringly expensive；像消息把人冲得站不稳，现代副词用来强调超出预期的程度。',
 'staggering + -ly；内层 stagger + -ing，从使人震惊的性质发展，外层多修饰大、高、低等程度。',STAGGER+[['stagger → staggering → staggeringly','震惊得站不稳似的性质，转成惊人的程度']],
 'staggeringly expensive 贵得惊人；staggeringly large 大得令人震惊。',
 'staggeringly simple 简单得惊人；staggeringly low 低得惊人。',
 'staggeringly 不只表示多、好，也能修饰 low、wasteful；核心是程度令人震惊，褒贬看后面的性质。',
 ('The repair turned out to be staggeringly expensive.','维修费原来贵得惊人。'),('Only a staggeringly small proportion of the money reached the project.','只有少得惊人的一小部分资金真正到了项目上。'),sources=S('staggeringly','stagger'))
W('wavers','英 /ˈweɪvəz/；美 /ˈweɪvərz/','摇摆、颤动；犹豫、动摇〔第三人称单数〕',
 '一边想选这个，一边又想选那个，主意不稳，是 wavers；灯火、声音、信心在稳定与不稳间摇，也能用它。',
 'waver + -s，读 /z/；基底与 wave 的旧摆动材料有关，-er 有旧反复动作背景，不是命名挥手的人。',WAVER+[['waver + -s → wavers','它不稳地波动；人或信心出现动摇']],
 'wavers between choices 在选项间犹豫；her confidence wavers 她的信心动摇。',
 'a flame wavers；never wavers in his support 支持从不动摇。',
 'wavers between A and B 表示未稳在一边，chooses A 则已经选择；犹豫不等于拒绝所有选项。',
 ('He wavers between staying and leaving.','他在留下与离开之间犹豫。'),('Her confidence wavers when the questions become difficult.','问题变难时，她的信心会动摇。'),sources=S('wavers','waver'))
W('wavered','英 /ˈweɪvəd/；美 /ˈweɪvərd/','摇摆、发颤了；犹豫、动摇了',
 '原先很坚定，听到新情况却停了一下、拿不准，是 wavered；声音在一句话中微微不稳，也能这样写。',
 'waver + 完整 -ed，读 /d/；旧摆动、犹豫材料在现代共用过去形式，不把所有抽象义都排成最后才产生。',WAVER+[['waver + -ed → wavered','过去摇摆、不稳，或在决定中犹豫']],
 'wavered for a moment 犹豫片刻；his voice wavered 他的声音发颤。',
 'never wavered in her support 支持从未动摇；wavered between two plans。',
 'wavered for a moment 可以后来仍做原决定，changed his mind 才明确改了主意；中间动摇不保证结局改变。',
 ('She wavered for a moment, then agreed to go.','她犹豫了一下，随后答应去。'),('His voice wavered when he said goodbye.','道别时，他的声音有些发颤。'),sources=S('wavered','waver'))
W('wavering','英 /ˈweɪvərɪŋ/；美 /ˈweɪvərɪŋ/','正在摇摆、发颤；犹豫、不坚定的',
 '态度一会儿往这边、一会儿往那边，叫 wavering support；火苗或声音不稳，也可以 wavering。都抓住没稳在一处的画面。',
 'waver + -ing；动作形式可形容不坚定的性质，-er 是基底旧构词的一部分，不拆成现代实施者。',WAVER+[['waver + -ing → wavering','摇摆、犹豫的过程，或不坚定的性质']],
 'wavering support 动摇的支持；a wavering voice 不稳的声音。',
 'wavering between two choices 在两选项间犹豫；a wavering flame 摇曳火苗。',
 'wavering support 表示支持不稳，不一定已变反对；opposition 才明确站在反对的一边。',
 ('The proposal is losing its wavering supporters.','提案正在失去那些态度不坚定的支持者。'),('A wavering flame lit the room.','一簇摇曳的火苗照亮了房间。'),sources=S('wavering','waver'))
W('unwavering','英 /ʌnˈweɪvərɪŋ/；美 /ʌnˈweɪvərɪŋ/','坚定不移、不动摇的',
 '外面意见变来变去，他的支持仍然稳稳在这里，叫 unwavering support。像不被推得左右摇摆。',
 '否定 un- + wavering；内层 waver + -ing，外层否定动摇、不稳的性质。',WAVER+[['un- + wavering → unwavering','态度、支持、决心不摇摆']],
 'unwavering support 坚定支持；unwavering determination 坚定决心。',
 'unwavering commitment 坚定承诺；an unwavering gaze 坚定、不移开的目光。',
 'unwavering 描述坚持程度，不自动表示观点正确；a mistaken belief 也可能被人 unwaveringly 持有。',
 ('Her unwavering support helped him continue.','她坚定的支持帮助他坚持下去。'),('He showed unwavering commitment to the project.','他始终坚定投入这个项目。'),sources=S('unwavering','waver'))
W('unwaveringly','英 /ʌnˈweɪvərɪŋli/；美 /ʌnˈweɪvərɪŋli/','坚定不移地；始终不动摇地',
 '支持不是说一次就算，而是外界变化时仍然站在同一立场，可以说 supported someone unwaveringly。',
 'unwavering + -ly；内层 un- 否定 wavering，外层修饰支持、坚持、相信等方式。',WAVER+[['unwavering + -ly → unwaveringly','以坚定、不随外界摇摆的方式行动']],
 'unwaveringly loyal 始终忠诚；unwaveringly committed 始终坚定投入。',
 'supported her unwaveringly；believed unwaveringly。',
 'unwaveringly 说坚持不变，unflinchingly 更突出面对压力、痛苦、真相时不退缩；两者可一起描述同一个人，侧面不同。',
 ('She supported her friend unwaveringly through the difficult year.','艰难的一年里，她始终坚定支持朋友。'),('He remained unwaveringly committed to finishing the work.','他始终坚定地要完成这项工作。'),sources=S('unwaveringly','waver'))
W('recoil','动词 /rɪˈkɔɪl/；名词 /ˈriːkɔɪl/','突然退缩、向后弹；反感地避开；后坐力',
 '手碰到烫物，一下往回缩，是 recoil；听到让人反感的提议，心理上也像往后退。枪械发射向后顶的 recoil 是同族的后坐用法。',
 '经法语 reculer，接拉丁 re- 向后 + culus 后部，完整俗拉丁连接词形 *reculare 为重建。名词还接法语 recul；不是英语 re- 加 coil 卷绕。',RECOIL,
 'recoil from the heat 遇热向后缩；recoil at the suggestion 对提议反感地退避；feel the recoil 感到后坐力。',
 'recoil in horror 惊恐地后退；recoil from violence 对暴力反感。',
 'recoil from a proposal 是本能反感、想避开，carefully reject a proposal 可以是审慎否决；结果可能同为不接受，反应方式不同。',
 ('She began to recoil from the intense heat.','她开始躲避那股强热，向后退。'),('The rifle’s recoil pushed against his shoulder.','步枪的后坐力顶在他的肩上。'),sources=S('recoil','recoil'))
W('recoils','动词 /rɪˈkɔɪlz/；名词 /ˈriːkɔɪlz/','突然退缩、向后弹〔第三人称单数〕；后坐、反弹动作〔复数〕',
 '碰到不愿接受的东西，他本能地往回退，是 he recoils；一件器械每次动作向后跳，也可描述为 recoils。',
 'recoil + -s，读 /z/；动词三单、名词复数同形，但常见重音分开：动作动词重后，名词常重前。',RECOIL+[['recoil + -s → recoils','他或它向后缩、反弹；多个后坐动作']],
 'recoils from the idea 一想到就反感；recoils in disgust 厌恶地退缩。',
 'the weapon recoils 器械向后坐动；recoils at the sight 看见便往后缩。',
 'recoils from the idea 不只是不理解，还带本能的排斥；is puzzled by the idea 则主要说想不明白。',
 ('He recoils from the idea of deceiving his friends.','一想到要欺骗朋友，他就本能地反感。'),('The rifle recoils each time it is fired.','步枪每次发射都会向后坐动。'),sources=S('recoils','recoil'))
W('recoiled','/rɪˈkɔɪld/','突然后退、退缩了；反感地避开了',
 '看见、碰到不愿接近的东西，身体一下退回去，或心里强烈排斥，就是 recoiled。',
 'recoil + 完整 -ed，读 /d/；动词重音在后，末尾 /l/ 与 /d/ 连读。',RECOIL+[['recoil + -ed → recoiled','过去向后缩、反弹，或对某事产生排斥']],
 'recoiled from the touch 因接触而缩回；recoiled in horror 惊恐地退后。',
 'recoiled at the suggestion；recoiled from the heat。',
 'recoiled 强调突然退回、本能抗拒，stepped back 可以只是平静地后退一步；不要把所有退步都加上惊恐。',
 ('She recoiled when the cold hand touched her arm.','冰冷的手碰到她的胳膊时，她猛地缩了回去。'),('He recoiled at the suggestion that they should cheat.','听到他们该作弊的提议，他本能地反感。'),sources=S('recoiled','recoil'))
W('recoiling','/rɪˈkɔɪlɪŋ/','正在向后弹、突然退缩；反感地避开',
 '受到刺激后向后缩的动作正发生，是 recoiling；叙事里也可写人一边听一边本能地想避开某个想法。',
 'recoil + -ing；动词规则变化，承法语后退材料，不因后接 -ing 就改接英语 coil 卷绕。',RECOIL+[['recoil + -ing → recoiling','后退、反弹或心理排斥的过程']],
 'recoiling from the heat 正躲避强热；recoiling in disgust 正厌恶地缩开。',
 'a recoiling mechanism 向后坐动的机构；recoiling at the thought。',
 'recoiling from 写退避，reaching towards 写接近；看介词方向能把身体、心理动作都读清楚。',
 ('He found himself recoiling from the proposed plan.','他发现自己正本能地排斥那个提议。'),('The startled child stepped back, recoiling from the sudden touch.','孩子被突然的触碰吓了一跳，退了一步、缩开身体。'),sources=S('recoiling','recoil'))
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_zgu',ROOTS,WORDS)
 extend_lessons()
