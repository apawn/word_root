"""Sad, fresh and sister: emotions, renewal and family bonds."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
SA=[['古英语 sæd','饱足、满足，也有厌倦等联系'],['中古英语 sad','沉实、严肃等义；悲伤义逐步突出，具体转义路径有不同解释'],['现代 sad','伤心、令人难过；另有可悲、差劲等评价']]
def D(f,m):return SA+[[f,m]]
W('sad','/sæd/','伤心的；令人难过的；可悲、差劲的〔口语〕',
 '心往下沉、提不起快乐，是今天的中心；消息本身也能叫 sad，因为它让人难过。',
 '古英语 sæd 原有饱足、厌倦等义，中古英语有沉实、严肃，再到悲伤的变化。具体可能经沉重疲倦或严肃沉郁等路径，不能编成吃饱就一定悲伤。',SA,
 'feel sad 觉得难过，sad news 坏消息、令人难过的消息，a sad ending 悲伤结局；a sad excuse 可贬可怜的借口。',
 'feel sad；sad news；a sad ending；sad to hear。',
 'sad 是难过的感受或引发难过；sorry 常表达歉意、遗憾、同情。I’m sorry to hear that 常比 I’m sad to hear that 更习惯用于回应坏消息。',
 ('She felt sad when her friend moved away.','朋友搬走后，她感到难过。'),('The film has a sad ending.','这部电影的结尾很伤感。'),sources=['https://www.etymonline.com/word/sad','https://en.wiktionary.org/wiki/sad#English'])
W('sadly','/ˈsædli/','悲伤地；可惜、遗憾的是；严重地〔某些搭配〕',
 '既能描写人难过的神情，也能放在句首说可惜事情是这样。',
 'sad + -ly，中古英语已有对应形式。sadly lacking、sadly mistaken 等固定搭配还可加强程度，不一定在说情绪。',D('sad + -ly → sadly','悲伤地；说话人表示遗憾；某些搭配加强程度'),
 'smile sadly 伤感地笑，Sadly, ... 遗憾的是……；sadly lacking 严重缺乏。',
 'smile sadly；Sadly, ...；sadly lacking；sadly mistaken。',
 'sadly 可评论整句话，sad 形容词通常修饰人、事情；Sadly, we lost 不是说 lost 这个动作做得很悲伤。',
 ('He smiled sadly and closed the letter.','他伤感地笑了笑，合上信。'),('Sadly, the museum is no longer open.','遗憾的是，博物馆已经不再开放。'))
W('sadness','/ˈsædnəs/','悲伤；难过的情绪',
 '把心里那份难过拿出来说，可以很淡，也可以长久地留着。',
 'sad + -ness，中古英语 sadnesse 等形式延续。现代主要接悲伤义，不用旧词源把它解释成吃饱状态。',D('sad + -ness → sadness','难过的性质、情绪'),
 'a feeling of sadness 悲伤感，a touch of sadness 一丝伤感，deep sadness 深深悲伤。',
 'a feeling of sadness；a touch of sadness；deep sadness。',
 'sadness 是情绪名词，sadden 是使人难过的动作；sadness 不自动等于某种临床疾病诊断。',
 ('There was a touch of sadness in her voice.','她的声音里有一丝伤感。'),('He felt sadness at the thought of leaving.','想到要离开，他感到难过。'))
W('sadden','/ˈsædən/','使难过；变得悲伤',
 '一件事进入心里，让原本平静、快乐的人难过起来。',
 'sad + -en，有中古英语相关形式。更早相关动词还接严肃、坚实等旧义，现代常用的是使伤心。',D('sad + -en → sadden','使变成 sad；现代使悲伤'),
 'be saddened by 因……难过，It saddens me to ... ……让我难过。',
 'be saddened by；deeply saddened；it saddens me。',
 'sad 状态难过，sadden 导致难过；The news saddened her 与 She was sad about the news 观察角度不同。',
 ('The news saddened everyone in the village.','消息让村里每个人都难过。'),('I was saddened by the closure of the old theatre.','老剧院关闭让我感到伤心。'))
R('B3656','今天的伤心；旧饱足到沉实、严肃等中间义','SAD：心情低落；也说让人难过的事情','sad → sadly、sadness、sadden，按状态、方式评论、情绪名词、引发变化连读。',
 '旧饱足义到现代悲伤的转折有多种解释，保留分寸；学习场景用心往下沉帮助理解，不当历史事实。',
 'sad + -ly/-ness/-en；sadder、saddest 为比较变化。',
 [['状态及表达方式','sad · sadly'],['情绪和引发情绪','sadness · sadden']],
 'sad/sorry 感受与道歉、遗憾有分工；sadly lacking 严重缺乏不讲难过；sadden 动词不等于 sadness。',
 'The sad news saddened her, and a trace of sadness remained in her voice.\n\n坏消息让她难过，声音里也一直带着一丝伤感。',
 'sad sadly sadness sadden')
FR=[['古英语 fersċ → 中古英语 fressh → fresh','淡而不咸、清新；同族法语形式影响词形和用法'],['现代 fresh','新鲜、新近、未用过；清新、有精神；另源无礼义单列']]
def F(f,m):return FR+[[f,m]]
W('fresh','/freʃ/','新鲜的；新近、另一个的；清新、有精神的；无礼的〔另源〕',
 '食物没放老，空气不闷，人休息后有精神，问题换个新角度；都抓住没陈旧、重新有活力。',
 '本族古英语 fersċ 经词音换位等走向 fresh，同族法语形式也有影响。无礼、放肆义通常另联系德语 frech，不强说所有义都由新鲜长出。',FR+[['另支可能接德语 frech','无礼、放肆的 fresh']],
 'fresh bread 新鲜面包，fresh air 新鲜空气，a fresh start 新开始，fresh evidence 新证据；Don’t get fresh. 别放肆、无礼。',
 'fresh bread；fresh air；a fresh start；fresh evidence。',
 'fresh 强调新近、未陈旧、恢复活力；new 可泛指新。fresh water 淡水不必是刚打来的水，已是固定不咸义。',
 ('We opened the windows to let in some fresh air.','我们打开窗户，让新鲜空气进来。'),('Let’s look at the problem with fresh eyes.','我们换个新眼光看看这个问题。'),sources=['https://www.etymonline.com/word/fresh','https://en.wiktionary.org/wiki/fresh#English'])
W('freshly','/ˈfreʃli/','刚刚、新近地；清新地',
 '强调东西刚经历某个处理过程，状态还新：刚烤好、刚刷好。',
 'fresh + -ly，中古英语已有对应形式。常修饰分词，说明动作新近完成。',F('fresh + -ly → freshly','新近、刚刚；以清新方式'),
 'freshly baked bread 刚烤的面包，freshly painted walls 刚刷好的墙，freshly squeezed juice 鲜榨果汁。',
 'freshly baked；freshly painted；freshly squeezed。',
 'fresh bread 新鲜面包，freshly baked bread 明说刚烤出来；新鲜与某个处理刚完成并非每次完全同义。',
 ('The kitchen smelled of freshly baked bread.','厨房里飘着刚烤好面包的香气。'),('The room had freshly painted walls.','房间的墙刚刷过。'))
W('freshness','/ˈfreʃnəs/','新鲜；清新感；新意、活力',
 '食物尝起来不陈，空气闻着清爽，作品看着有新意，都是 fresh 这种特点。',
 'fresh + -ness。性质名词随对象分味道、空气、表达风格等，不是一种统一可数物品。',F('fresh + -ness → freshness','新鲜、清新、有新意的性质'),
 'the freshness of the ingredients 食材新鲜度，a sense of freshness 清新感。',
 'the freshness of；retain freshness；a sense of freshness。',
 'freshness 强调新鲜、新意，novelty 可说新奇性、新鲜感；一个作品有 freshness 不一定每个细节都前所未有。',
 ('The freshness of the ingredients makes a real difference.','食材的新鲜程度确实很影响效果。'),('The performance had a freshness that delighted the audience.','表演带着让观众喜欢的清新感。'))
W('freshen','/ˈfreʃən/','使清新、变新鲜；梳洗整顿〔freshen up〕',
 '开窗让空气清爽，洗把脸整理衣服让人精神些，都是把状态往 fresh 调。',
 'fresh + -en，中古英语已有相应动词。freshen up 既可清理环境，也可说人简单梳洗。',F('fresh + -en → freshen','使清新、恢复精神；变清新'),
 'freshen the room 让房间清新，freshen up 梳洗、整理一下，freshen your breath 清新口气。',
 'freshen the room；freshen up；freshen your breath。',
 'freshen 常直接让气味、外观、精神更清爽；refresh 还常说刷新网页、唤起记忆，不能所有搭配机械互换。',
 ('I’ll freshen up before dinner.','晚饭前我去梳洗一下。'),('Opening the window helped freshen the room.','打开窗户让房间清爽了些。'))
W('afresh','/əˈfreʃ/','重新；从头再来',
 '前面那版先放下，像拿到一张干净纸一样重新开始。',
 '中古英语 a-fresche 等，a- + fresh，可能有 anew 等类推。a- 此处不是希腊语否定前缀。',F('a- + fresh → afresh','以新的状态 → 重新、再来'),
 'start afresh 重新开始，begin afresh 从头来，look afresh at 以新眼光看。',
 'start afresh；begin afresh；look afresh at。',
 'again 单纯再一次，afresh 更有放下旧进程、从新起点开始的感觉；不是每次 again 都适合换成 afresh。',
 ('After the first plan failed, we decided to start afresh.','第一个计划失败后，我们决定重新开始。'),('The move gave her a chance to begin afresh.','搬家让她有机会重新开始。'))
W('refresh','/rɪˈfreʃ/','使恢复精神；刷新；唤起、更新记忆',
 '让原本疲倦、旧了或模糊的状态重新有活力、变清楚；网页也重新取回显示内容。',
 '经中古英语 refreshen 等接古法语 refreschier，现代可对应 re- + fresh。不是仅在现代英语把两个现成片段临时拼起来。',FR[:1]+[['古法语 refreschier → 中古英语 refreshen → refresh','使恢复、更新、使如新']],
 'refresh the page 刷新页面，refresh your memory 唤起记忆，feel refreshed 感到恢复精神。',
 'refresh the page；refresh your memory；feel refreshed。',
 'refresh 更新、恢复，restart 重新启动；refresh a page 不一定重启浏览器。refresh your memory 是帮想起，不是抹除旧记忆。',
 ('Refresh the page to see the latest results.','刷新页面，查看最新结果。'),('The notes helped refresh my memory before the meeting.','会前，这些笔记帮我重新想起了相关内容。'))
W('refreshing','/rɪˈfreʃɪŋ/','使人清爽、振奋的；令人耳目一新的',
 '喝一口、听一番，感觉精神一振，或终于碰到一种新鲜、坦率的方式。',
 'refresh + -ing，形成描述造成效果的分词形容词。形容东西让人清爽，不是直接说人已经清爽。',FR+[['refresh + -ing → refreshing','引起清爽、振奋或耳目一新感觉的']],
 'a refreshing drink 清爽饮品，a refreshing change 令人耳目一新的变化，refreshing honesty 让人感觉清新的坦诚。',
 'a refreshing drink；a refreshing change；refreshing honesty。',
 'refreshing 造成效果，refreshed 感到已恢复精神；The drink is refreshing，I feel refreshed。',
 ('The cold drink was wonderfully refreshing.','冷饮喝起来格外清爽。'),('It was refreshing to hear such an honest answer.','听到这么坦诚的回答，让人耳目一新。'))
W('refreshingly','/rɪˈfreʃɪŋli/','令人耳目一新地；清爽、振奋地',
 '不是只夸好，而是夸这种简单、坦诚等特点和以前不一样，让人舒一口气。',
 'refreshing + -ly，把令人清新、振奋的评价用来修饰形容词或表达方式。',FR+[['refresh → refreshing + -ly → refreshingly','以令人清新、耳目一新的方式']],
 'refreshingly simple 简单得让人耳目一新，refreshingly honest 坦诚得令人舒服。',
 'refreshingly simple；refreshingly honest；refreshingly direct。',
 'refreshingly 常带积极评价，surprisingly 只明确出乎意料；refreshingly honest 既惊喜又觉得这种坦诚可贵。',
 ('The instructions were refreshingly simple.','说明简单明了，让人耳目一新。'),('She was refreshingly honest about the project’s problems.','她坦诚地谈了项目的问题，让人觉得很难得。'))
W('refreshment','/rɪˈfreʃmənt/','恢复精神、提神；茶点、饮料〔常用复数〕',
 '休息时给你喝点、吃点，让精神回来；活动通知里的 refreshments 常就是茶点饮料。',
 '对应 refresh + -ment，历史与法语及较早相关名词、动词形式相连。恢复活动再借指提供这种恢复的食物饮品。',FR[:1]+[['法语 refreschier 及相关形式 → refreshment','恢复精神；后借指补充精神体力的饮食']],
 'light refreshments 简单茶点，refreshments will be served 将提供茶点饮料。通常不保证是完整正餐。',
 'light refreshments；serve refreshments；a moment of refreshment。',
 'refreshment 茶点或提神，refresh 刷新动词；网页刷新一般不说 a refreshment of the page。',
 ('Light refreshments will be served after the talk.','讲座后将提供简单茶点。'),('We stopped for rest and refreshment.','我们停下来休息，吃喝一点恢复精神。'))
R('B2674','新鲜、不陈旧；恢复活力、重新开始与刷新','FRESH：没陈旧，有清新、新起点的感觉','fresh → freshly、freshness、freshen、afresh；refresh → refreshing → refreshingly，与 refreshment 同组；freshman、freshwater 共享。',
 '新鲜、淡水、清新有旧联系；无礼义通常另接德语形式。refresh 是借入旧动词，不仅是现代 re+fresh。',
 'fresh + -ly/-ness/-en；a- + fresh；refresh + -ing/-ment，refreshing + -ly；fresh + man/water。',
 [['基本性质与新的开始','fresh · freshly · freshness · freshen · afresh'],['恢复、刷新及感受','refresh · refreshing · refreshingly · refreshment'],['已有固定组合','freshman · freshwater']],
 'freshly baked 刚烤，fresh bread 新鲜；refreshing 让人清爽、refreshed 已清爽；refreshment 茶点不指网页刷新。',
 'After some refreshments, we felt ready to start afresh.\n\n吃喝了一些茶点后，我们觉得又能重新开始了。',
 'fresh freshly freshness freshen afresh refresh refreshing refreshingly refreshment freshman freshwater')
SI=[['古英语 sweostor、相关北欧 systir 等 → 中古英语 suster → sister','姐妹；现代词形受同族形式影响'],['现代 sister','姐姐妹妹；团体姐妹；修女等称呼；平行机构的形容用法']]
W('sister','英 /ˈsɪstə/；美 /ˈsɪstər/','姐姐、妹妹；姐妹；修女；同系的〔修饰用法〕',
 '英语只说女性同胞，不在这个词里分姐姐还是妹妹；共同团体的人也能借姐妹关系称呼。',
 '古英语 sweostor 等亲属词延续，现代元音等词形也受北欧同族形式影响。不能拆成 sis + 职业后缀 -ter。',SI,
 'an older sister 姐姐，a younger sister 妹妹，a sister company 同系公司，Sister Mary 修女玛丽。',
 'an older sister；a younger sister；a sister company；sisters and brothers。',
 'sister 不自带长幼，older/younger 说明；sister company 常是同集团、同系关系，未必就是子公司 subsidiary。',
 ('My younger sister lives in another city.','我妹妹住在另一个城市。'),('The two firms are sister companies.','这两家公司是同系公司。'),sources=['https://www.etymonline.com/word/sister','https://en.wiktionary.org/wiki/sister#English'])
W('sisterly','英 /ˈsɪstəli/；美 /ˈsɪstərli/','姐妹般的；像姐姐妹妹那样关切的',
 '带着姐妹之间那种亲近、照顾或坦率，不要求两个人真有血缘。',
 'sister + 形容词 -ly，也有较少见副词用法；这里最常见并非动词方式副词。',SI+[['sister + -ly → sisterly','有姐妹关系特点、像姐妹的']],
 'sisterly advice 姐妹般关切的建议，sisterly affection 姐妹般的亲情。',
 'sisterly advice；sisterly affection；a sisterly hug。',
 'sisterly 常是形容词，friendly、motherly 也可如此；不要见 -ly 就把 a sisterly hug 判作语法错。',
 ('She gave me some sisterly advice before the interview.','面试前，她像姐妹一样关切地给了我些建议。'),('They shared a warm sisterly hug.','她们像姐妹般温暖地拥抱了一下。'))
W('sisterhood','英 /ˈsɪstəhʊd/；美 /ˈsɪstərhʊd/','姐妹关系；女性团结、情谊；女性团体',
 '把彼此当姐妹，互相支持的一种关系；也可指按这种关系组成的一群人。',
 'sister + -hood，中古英语已有对应 susterhede 等形式。后缀表关系、状态或群体，与 hood 兜帽不是同一现代功能。',SI+[['sister + -hood → sisterhood','姐妹关系；女性共同体、情谊']],
 'a sense of sisterhood 姐妹般的团结感，a religious sisterhood 女性宗教团体。',
 'a sense of sisterhood；a bond of sisterhood；a religious sisterhood。',
 'sisterhood 关系、团体，sisterly 形容这种关切。women 女性这个类别本身不自动保证彼此有 sisterhood 的情谊。',
 ('The project created a strong sense of sisterhood.','这个项目让大家产生了强烈的姐妹情谊。'),('The novel explores friendship and sisterhood.','小说探讨友谊与姐妹情谊。'))
W('stepsister','英 /ˈstepsɪstə/；美 /ˈstepsɪstər/','继姐妹',
 '父母再婚后，继父或继母原有的女儿与你成为家庭里的姐妹；不靠共同生父母这条关系。',
 'step- 继亲关系 + sister。step- 接古英语丧亲、继亲相关旧成分，不是脚步 step，所以不是踩一步才变姐妹。',SI+[['step-〔继亲关系〕+ sister → stepsister','由父母的婚姻建立的姐妹关系']],
 'my stepsister 我的继姐妹。要分长幼仍可加 older、younger。',
 'my stepsister；an older stepsister；meet a stepsister。',
 'stepsister 继姐妹，half-sister 同父异母或同母异父姐妹；后者有一位共同生父母，两个关系不同。',
 ('My stepsister moved in after our parents married.','父母结婚后，我的继姐妹搬来一起住。'),('She and her stepsister became close friends.','她和继姐妹成了亲密朋友。'))
R('B2655','女性同胞与姐妹般关系；长幼、继亲另说明','SISTER：同胞姐妹；关系也能借来讲团体、机构','sister → sisterly、sisterhood；stepsister 单讲继亲，避免与同父异母、同母异父混淆。',
 '古老亲属词延续至今，现代词形有同族语言影响；本词没有自带姐姐、妹妹的年龄差。',
 'sister + -ly/-hood；step- + sister；older/younger sister 分长幼。',
 [['基本关系与相处方式','sister · sisterly · sisterhood'],['继亲关系','stepsister']],
 'sister 无长幼；sisterly 可形容词；stepsister 继姐妹不同于 half-sister；sister company 同系不必是子公司。',
 'Her stepsister offered sisterly advice and a warm hug.\n\n她的继姐妹像姐妹般关切地给她建议，并温暖地抱了抱她。',
 'sister sisterly sisterhood stepsister')
if __name__=='__main__':save('continuation_20261030_aw',ROOTS,WORDS)
