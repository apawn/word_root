"""Growth, leader and return: keep close extensions together."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
GR=[['古英语 grōwan → grow；相关旧名词 → growth','生长 → 生长过程、长出的东西'],['现代 growth 的方向、程度派生','低处长、向外长、重新长、长过量']]
def GH(f,m):return GR+[[f,m]]
W('undergrowth','英 /ˈʌndəɡrəʊθ/；美 /ˈʌndərɡroʊθ/','林下灌木、矮树与杂草',
 '高树撑在上面，下面还挤着一层灌木、蕨类等低矮植物，就是这层林下植被。',
 'under- 在下面 + growth 生长物，名称按林中层次，不是指这些植物营养不良。',GH('under- + growth → undergrowth','高树下较低层的植物'),
 'dense undergrowth 稠密林下植被，push through the undergrowth 从灌木杂草中穿过；通常作不可数总称。',
 'dense undergrowth；thick undergrowth；through the undergrowth。',
 'undergrowth 林下植物，underground 地下；低矮植物仍在地面上。',
 ('The path disappeared into dense undergrowth.','小路消失在稠密的林下灌丛里。'),('We heard an animal moving through the undergrowth.','我们听见一只动物在灌木杂草中移动。'))
W('outgrowth','英 /ˈaʊtɡrəʊθ/；美 /ˈaʊtɡroʊθ/','长出部分；自然发展出的结果、产物',
 '枝条从树上伸出去，一个新项目从旧项目中长出来，都可以是 outgrowth。',
 'out- 向外 + growth 生长物，由向外长出的部分延伸到后续发展成果。',GH('out- + growth → outgrowth','向外长出的部分 → 衍生结果'),
 'an outgrowth of earlier work 早期工作的自然延伸，a bony outgrowth 骨性突起；看实物还是抽象结果。',
 'an outgrowth of；a natural outgrowth；an outgrowth from。',
 'outgrowth 结果不一定是坏事；overgrowth 侧重过度生长。outgrow 又是另一动词，常说长大得不再适合。',
 ('The new course is an outgrowth of last year’s workshops.','新课程是去年工坊自然发展出的成果。'),('Small outgrowths appeared along the branch.','枝条上长出了小小的突起。'))
W('regrowth','英 /ˌriːˈɡrəʊθ/；美 /ˌriːˈɡroʊθ/','重新生长；再长出的部分',
 '剪掉、烧掉、脱落以后，又冒出一层新生长，重点在再来一次。',
 're- 再次 + growth。既可指再生的过程，也可指重新长出的植物、毛发等。',GH('re- + growth → regrowth','再次生长；新长出的部分'),
 'forest regrowth 森林再生，hair regrowth 毛发重新生长，signs of regrowth 再生迹象。',
 'forest regrowth；new regrowth；signs of regrowth。',
 'regrowth 表示再生，不自动表示回到原来的全部结构；recovery 恢复的范围更宽。',
 ('Fresh regrowth appeared after the first rains.','第一场雨后长出了新芽。'),('The study tracks forest regrowth after the fire.','研究跟踪火灾后的森林再生。'))
W('overgrowth','英 /ˈəʊvəɡrəʊθ/；美 /ˈoʊvərɡroʊθ/','过度生长；丛生、覆盖的植物',
 '枝蔓杂草长得太密，把小路、墙面都盖住，便形成 overgrowth。',
 'over- 过度、覆盖 + growth。可以强调长得过多，也可以指覆盖在别的东西上的茂密生长物。',GH('over- + growth → overgrowth','生长过量；茂密覆盖物'),
 'an overgrowth of weeds 杂草丛生，clear the overgrowth 清掉丛生植物；也用于别的生长语境。',
 'an overgrowth of weeds；clear the overgrowth；thick overgrowth。',
 'overgrowth 多少超过需要或覆盖别物；undergrowth 按林下位置叫，不一定过量。',
 ('An overgrowth of weeds hid the old steps.','丛生杂草遮住了旧台阶。'),('They cleared the overgrowth from the garden path.','他们清除了花园小路上丛生的植物。'))
R('B2459','生长与按位置、方向、次数、程度分化','GROWTH：长出来；前部决定怎样长','growth 已精讲，接 undergrowth 低层、outgrowth 向外结果、regrowth 再生、overgrowth 过度。',
 'growth 与 grow 有旧名词关系，不是每个动词都能任意加 -th。四个扩展都是现代很好理解的方向、程度组合。',
 'under-/out-/re-/over- + growth。',
 [['基本生长','growth'],['位置与衍生','undergrowth · outgrowth'],['再次与过量','regrowth · overgrowth']],
 'undergrowth 不等于 underground；outgrowth 可好可坏；regrowth 不保证完全复原；overgrowth 过量或覆盖。',
 'New regrowth soon covered the area where the overgrowth had been cleared.\n\n丛生植物清除后，那片地方很快又长出新芽。',
 'growth undergrowth outgrowth regrowth overgrowth')
LE=[['古英语 lædan → lead；lædere → leader','带领 → 带领者'],['现代 leader 的复合、派生','带领助威、团伙或乐队；没有带领者']]
def LH(f,m):return LE+[[f,m]]
W('cheerleader','英 /ˈtʃɪəliːdə/；美 /ˈtʃɪrliːdər/','啦啦队员；积极鼓吹、支持者',
 '在场边带着大家鼓劲，也可以比喻不断为某主张叫好的人。',
 'cheer 助威、欢呼 + leader，现代体育用语后来发展出积极支持者比喻。不是只指一支啦啦队的队长。',LH('cheer + leader → cheerleader','参与带动助威的人 → 积极支持者'),
 'a school cheerleader 校队啦啦队员，a cheerleader for reform 改革的积极支持者。不限性别。',
 'a school cheerleader；a cheerleader for；an enthusiastic cheerleader。',
 'cheerleader 可指普通啦啦队成员，captain 才更明确队长。比喻义有时暗示偏向叫好、缺少批判。',
 ('The cheerleaders performed before the match.','啦啦队员在赛前表演。'),('He became a vocal cheerleader for the new project.','他成为新项目积极发声的支持者。'),sources=['https://www.etymonline.com/word/cheerleader','https://en.wiktionary.org/wiki/cheerleader#English'])
W('ringleader','英 /ˈrɪŋliːdə/；美 /ˈrɪŋliːdər/','带头者；头目、首谋',
 '一群人闹事、捣乱，那个率先组织、带着别人做的人就是 ringleader。',
 'ring + leader；相关中古短语 lead the ring 表示群体中带头，更早可能联系环舞领舞。现代常带负面含义，不是戴戒指的领导。',LH('lead the ring 的旧短语 → ring + leader','群体带头者 → 尤指闹事、违法行为头目'),
 'the ringleader of a gang 团伙头目，the ringleader of the prank 恶作剧带头者。也可用于程度较轻的捣乱。',
 'the ringleader of；identify the ringleader；a suspected ringleader。',
 'leader 中性，ringleader 常负面；bandleader 则是乐队领队，不能因为都带一群人就随便互换。',
 ('The teacher asked who the ringleader of the prank was.','老师问谁是恶作剧的带头者。'),('The report identified him as the group’s ringleader.','报告指出他是这个团体的头目。'),sources=['https://www.etymonline.com/word/ringleader','https://en.wiktionary.org/wiki/ringleader#English'])
W('bandleader','英 /ˈbændliːdə/；美 /ˈbændliːdər/','乐队领队、带队演奏者',
 '负责把一支乐队组织、带动起来的人，可能自己也演奏或演唱。',
 'band 乐队 + leader，按领导的群体命名。这里 band 不是绑带。',LH('band + leader → bandleader','组织、带领乐队的人'),
 'a jazz bandleader 爵士乐队领队，a famous bandleader 著名乐队领队；职责依乐队而异。',
 'a jazz bandleader；a famous bandleader；the bandleader’s signal。',
 'bandleader 不必总拿指挥棒；conductor 常更直接说指挥。乐队组织、带演奏与具体指挥动作范围有差别。',
 ('The bandleader counted the musicians in.','乐队领队打拍子，带乐手们进入演奏。'),('She worked as a pianist and bandleader.','她从事钢琴演奏和乐队领队工作。'))
W('leaderless','英 /ˈliːdələs/；美 /ˈliːdərləs/','没有领导者的；无人带领的',
 '人还在一组里，但没有一个负责给方向或统筹的人。',
 'leader + -less，没有带领者；-less 否定的是角色存在，不评价所有成员能力差。',LH('leader + -less → leaderless','没有领导者或带领者'),
 'a leaderless team 无人带领的团队，a leaderless movement 没有单一领袖的运动。可能是暂时空缺，也可能是组织方式。',
 'a leaderless team；a leaderless group；remain leaderless。',
 'leaderless 无领导者不一定 disorganized 混乱；团队也可能通过分工协调。',
 ('The team was briefly leaderless after the manager resigned.','经理辞职后，团队一度无人带领。'),('The article describes a leaderless network of volunteers.','文章描写了一个没有单一领袖的志愿者网络。'))
R('B3164','带领者与领导不同群体的角色','LEADER：谁在带；前部说明带哪一群、做什么','leader、leadership 已精讲，补 cheerleader、ringleader、bandleader，再接 leaderless 和共享 leaderboard。',
 'leader 有古英语历史。复合词不全等于领导职位：cheerleader 可普通啦啦队员，ringleader 常负面。',
 'cheer/ring/band + leader；leader + -less/-ship；leader + board。',
 [['基本人物、能力与缺位','leader · leadership · leaderless'],['具体人物角色','cheerleader · ringleader · bandleader'],['已有名次记录','leaderboard']],
 'cheerleader 不只队长；ringleader 常负面；bandleader 不必总是持棒指挥；leaderless 不自动混乱。',
 'The bandleader thanked the team’s cheerleaders for their support.\n\n乐队领队感谢了团队的积极支持者。',
 'leader leadership leaderless cheerleader ringleader bandleader leaderboard')
RE=[['法语 retourner → 英语 return','转回来、回来；最终接拉丁旋转词族'],['return + -er／-ee','回来、返还或回击的人；特定返回群体成员']]
W('returner','英 /rɪˈtɜːnə/；美 /rɪˈtɜːrnər/','返回者；重返工作者；接球回击者',
 '按做返回这个动作称人；体育里是把球接过来再回击、回跑的人。',
 'return + -er，执行 return 某种动作的人。工作语境 returner 可说离开一段时间后重返岗位者。',RE,
 'a returner to work 重返工作者，a kick returner 接开球并回跑的球员，a good returner 网球等项目中善于接发球的人。',
 'a returner to work；a kick returner；an experienced returner。',
 'returner 与 returnee 含义可重合，不能只凭 -er/-ee 就断言前者主动、后者被动；returnee 也可以自己回来。',
 ('The programme supports returners to work after a career break.','项目支持职业中断后重新工作的人。'),('She is one of the strongest returners in the tournament.','她是本届比赛接发球最强的选手之一。'))
W('returnee','英 /rɪˌtɜːˈniː/；美 /rɪˌtɜːrˈniː/','归来者；回国、返乡或重返某领域的人',
 '把回来的人看成一个有共同经历的群体：海外回来的人、重新回到工作岗位的人。',
 'return + -ee，通常末尾重读。-ee 在此形成参与某过程的人，不必是被别人送回来，所以不机械等同于被动接受者。',RE+[['return + -ee → returnee','经历返回的人，尤某一返归群体成员']],
 'overseas returnees 海外归来者，returnees to the workforce 重返劳动力市场者。实际返到哪里由补语说明。',
 'overseas returnees；returnees to work；a group of returnees。',
 'returnee 不自带海归高学历等评价；只说返回经历。refugee、employee 等 -ee 词各自历史、角色不同，不一概套成被动。',
 ('The centre provides advice for overseas returnees.','中心为海外归来者提供咨询。'),('Several returnees joined the training after years away from work.','几位多年未工作的返岗者参加了培训。'))
R('B3950','返回动作与不同返回者称呼','RETURN：回来；RETURNER、RETURNEE：两种人物词','return 已有精讲，两个后缀相邻对照，避免套主动被动公式。',
 'return 来自法语转回词。returner 可体育回击或返岗者，returnee 常指某个返归群体，语义有重合。',
 'return + -er → returner；return + -ee → returnee。',
 [['基本动作与人物','return · returner · returnee']],
 '-ee 在 returnee 中不一定被动；具体返回工作、国家还是场地，要看上下文。',
 'The course welcomes both new workers and returnees.\n\n课程欢迎新入职者，也欢迎重返工作的人。',
 'return returner returnee')
if __name__=='__main__':save('continuation_20261030_w',ROOTS,WORDS)
