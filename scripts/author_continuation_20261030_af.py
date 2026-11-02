"""Arm branches, battle and advance: avoid false modern splits."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
AR=[['古英语 earm → arm〔手臂〕；法语 armer → arm〔武装〕','身体部位与武器动词是不同传入历史'],['现代复合词','按身体位置、形状或携带武器区分']]
def AH(f,m):return AR+[[f,m]]
W('forearm','英名词 /ˈfɔːrɑːm/、动词 /ˌfɔːrˈɑːm/；美名词 /ˈfɔːrɑːrm/、动词 /ˌfɔːrˈɑːrm/','前臂；预先装备、准备〔动词〕',
 '身体上是手腕到肘的这一段；动词却是提前准备好，两者用了不同义的 arm。',
 '名词 fore- 前部 + arm 手臂；动词 fore- 预先 + arm 武装。动词反而有更早见证，不能把名词前臂当动词的来源。',AR+[['fore- + arm〔手臂〕；fore- + arm〔武装〕','两条独立组合：前臂；事先准备']],
 'rest your forearms 放松、搁下前臂；forewarned is forearmed 是有预警就能有准备的谚语。名词重音较前，动词较后。',
 'rest your forearms；a mark on the forearm；forewarned is forearmed。',
 'forearm 前臂不是整条胳膊；提前准备的动词义也不是把手臂伸到前面。',
 ('She rested her forearms on the table.','她把前臂搁在桌上。'),('Knowing the likely questions helped forearm her for the interview.','知道可能的问题，帮助她为面试预先做好准备。'),sources=['https://www.etymonline.com/word/forearm','https://en.wiktionary.org/wiki/forearm#English'])
W('armpit','英 /ˈɑːmpɪt/；美 /ˈɑːrmpɪt/','腋窝；令人厌恶的地方〔比喻〕',
 '手臂接到肩膀下面的凹处，像一个小坑，pit 就抓这个形状。',
 'arm 手臂 + pit 坑、凹处，中古英语已有对应组合；不把 pit 理解成水果核的那一个义项。',AH('arm + pit → armpit','手臂根部的凹处 → 腋窝'),
 'under the armpit 腋下，a sleeve tight at the armpit 腋下紧的袖子。把某地称 armpit 是带贬意的比喻。',
 'under the armpit；tight at the armpits；the armpit area。',
 'armpit 与 underarm 在部位上常重合；underarm 作产品修饰语较常见，armpit 是直接身体名称。',
 ('The jacket was tight around the armpits.','夹克腋下位置太紧。'),('He tucked the folder under his armpit.','他把文件夹夹在腋下。'))
W('underarm','英 /ˈʌndərɑːm/；美 /ˈʌndərɑːrm/','腋下；腋下用的；低手投掷的',
 '放到手臂下面看：身体部位是腋下，投球动作则是手臂从低处送出去。',
 'under- 在下方 + arm 手臂，名词、修饰语与投掷方式用法分别固定；腋下部位义是较晚的常用法。',AH('under- + arm → underarm','手臂下方 → 腋下；由低处投出的方式'),
 'underarm deodorant 腋下除味产品，an underarm throw 低手投掷，the underarm area 腋下部位。',
 'the underarm area；underarm deodorant；an underarm throw。',
 'underarm 这里不是装备不足的普通翻译；身体义与 arms 武器的动词组合要另分，较少用法本页不展开。',
 ('The shirt has extra fabric in the underarm area.','衬衫腋下部位多留了一些布料。'),('She made a gentle underarm throw.','她轻轻地做了一次低手投掷。'))
W('armband','英 /ˈɑːmbænd/；美 /ˈɑːrmbænd/','臂章、袖标；臂带',
 '围在胳膊上的一圈带，可以标身份、队长或表达纪念等。',
 'arm 手臂 + band 带、环，按佩戴位置命名；band 在这里不是乐队。',AH('arm + band → armband','佩戴在手臂上的带、标识'),
 'a captain’s armband 队长袖标，a black armband 黑纱臂章，a reflective armband 反光臂带。',
 'a captain’s armband；a black armband；a reflective armband。',
 'armband 戴臂上，wristband 戴腕部；具体佩戴范围不一样。',
 ('The captain wore a bright armband.','队长戴着醒目的袖标。'),('The runners wore reflective armbands at night.','跑步者夜间戴着反光臂带。'))
W('armless','英 /ˈɑːmləs/；美 /ˈɑːrmləs/','无臂的；没有扶手的',
 '没有身体手臂，或家具没有像胳膊一样伸出的扶手；-less 直接说明少了哪部分。',
 'arm + -less，中古英语已有对应形式。家具用法接 arm 的扶手比喻，不等于没有武器。',AH('arm + -less → armless','没有手臂；家具没有扶手'),
 'an armless chair 无扶手椅，an armless statue 缺臂雕像；描述结构或保存状态。',
 'an armless chair；an armless statue；an armless sofa。',
 'armless 没手臂或扶手，unarmed 没武装；两个词不能因都带 arm 就互换。',
 ('An armless chair fits more easily under the desk.','无扶手椅更容易收进书桌下面。'),('The museum displays an armless statue.','博物馆展示了一尊缺臂雕像。'))
W('sidearm','英 /ˈsaɪdɑːm/；美 /ˈsaɪdɑːrm/','随身佩带的武器；侧手投掷的〔体育用法〕',
 '名词说佩在身侧的个人武器；体育里也可说手臂从侧面送球的动作。',
 'side 侧边 + arm。武器名接 arms 武器支线，投球方式接身体手臂支线，属于同形组合里不同义项。',AH('side + arm〔武器；身体手臂〕→ sidearm','身侧佩带武器；侧手投掷方式'),
 'an officer’s sidearm 警员随身武器，a sidearm throw 侧手投掷；看名词对象还是体育动作。',
 'an officer’s sidearm；a sidearm throw；throw sidearm。',
 'sidearm 名词并非人身上侧面的手臂；forearm 前臂说具体部位，sidearm 体育用法说动作方向。',
 ('The display includes an officer’s historical sidearm.','展品包括一名军官的旧式随身武器。'),('The player returned the ball with a sidearm throw.','球员用侧手投掷把球传了回去。'))
R('B2635','手臂与另源武装词形；位置、家具和动作','ARM：身体部位；武装义要走另一条历史','arm 已分源精讲，前臂、腋窝、腋下、臂带和无扶手同组；sidearm、forearm 的武装用法另接。',
 '身体 arm 继承古英语 earm；武装 arm 接法语、拉丁武器词。不能把所有枪械含 arm 的词都说成胳膊伸出来。',
 'fore-/under- + arm〔手臂〕；arm + pit/band/-less/chair/rest；side + arm〔武器〕；fore- + arm〔武装〕。',
 [['身体位置与佩戴物','arm · forearm · armpit · underarm · armband'],['家具与结构','armchair · armrest · armless'],['另源武装支线','armed · firearm · sidearm · rearm']],
 'forearm 名词前臂与动词预先准备重音不同；armless 不等于 unarmed；armband 不等于 wristband。',
 'She rested her forearm on the armrest of the chair.\n\n她把前臂搁在椅子扶手上。',
 'arm forearm armpit underarm armband armchair armrest armless armed firearm sidearm rearm')
BA=[['拉丁 battuere〔击打〕→ 晚期拉丁 battualia','击打、格斗训练'],['法语 bataille、batailler → 英语 battle','战斗、交战 → 持续斗争、应对困难']]
W('battle','/ˈbætl/','战斗；争夺、斗争；奋力应对',
 '两边持续较量，不只军事作战；赢一场比赛、解决一项顽固问题，也可说在 battle。',
 '名词经法语 bataille 接晚期拉丁格斗训练词，最终接 battuere 击打；动词也有法语 batailler 的借入历史。',BA,
 'win a battle 赢一场战斗，a battle for attention 争夺注意，battle against delays 力争克服延误，an uphill battle 艰难斗争。',
 'win a battle；a battle for；battle against；an uphill battle。',
 'battle 常一场战斗或持续较量，war 战争范围通常更大；比喻 battle 不表示真的动武。',
 ('The campaign became a battle for public attention.','这场活动变成了争夺公众注意的较量。'),('The team battled against strong winds all afternoon.','团队整个下午都在奋力应对强风。'),sources=['https://www.etymonline.com/word/battle','https://en.wiktionary.org/wiki/battle#English'])
W('battling','/ˈbætlɪŋ/','正在战斗、奋力应对；顽强的',
 '困难还没过去，人还在一点点顶住、往前争取，是一个持续中的画面。',
 'battle 去末尾 e + -ing，动词形式也可修饰人、团队的拼搏状态。本页讲战斗词族，不混入另源的古老养肥义。',BA+[['battle + -ing → battling','正在战斗、应对；表现顽强']],
 'battling against the wind 与风抗争，a battling team 顽强拼搏的团队。具体困难要看后面的对象。',
 'battling against；battling to do；a battling performance。',
 'battling 强调还在进行、奋力应对，不等于已经 won 获胜；它有时也只是普通进行时的一部分。',
 ('They were still battling to keep the project on schedule.','他们仍在努力让项目按进度进行。'),('The team earned a draw with a battling performance.','球队凭顽强表现取得平局。'))
R('B3684','战斗、争夺与持续应对困难','BATTLE：有对抗的较量；BATTLING：正在顶住','补基本 battle 与 battling，战场、战舰、战线等常用词已有精讲共享。',
 '法语战斗词最终接拉丁击打、格斗训练材料。较冷的另源肥沃、养肥义不并入这个学习词族。',
 'battle → battling；battle + field/ground/front/ship。',
 [['基本较量与进行状态','battle · battling'],['地点、线和船','battlefield · battleground · battlefront · battleship']],
 'battle 可比喻，不必真打仗；battling 进行不代表已赢；war 通常更大范围。',
 'The team kept battling even when victory seemed unlikely.\n\n即使胜利似乎无望，团队仍坚持拼搏。',
 'battle battling battlefield battleground battlefront battleship')
AD=[['晚期拉丁 ab ante → 通俗拉丁 *abanteare','从前方、向前'],['法语 avancier → 英语 avauncen → advance','推进、前进；后来类推 ad- 加入字母 d']]
W('advance','英 /ədˈvɑːns/；美 /ədˈvæns/','前进、推进；进展；预付；事先的',
 '往前推进，是进度；把原本以后才做、才付的事提前，也像把它移到前面。',
 '借法语 avancier，最终接晚期拉丁 ab ante 前方。英语后来受 ad- 类推影响插入 d，不能按今天拼写硬拆成 ad + vance。',AD,
 'advance a plan 推进计划，advances in science 科学进展，pay in advance 预付，advance notice 事先通知。',
 'in advance；advance notice；advances in；advance a proposal。',
 'advance notice 是提前通知，advanced course 是高阶课程；二者不因为只差 d 就同义。advance 也可提出观点供讨论。',
 ('Please book your place in advance.','请提前预订名额。'),('The new method represents an important advance.','新方法代表一项重要进展。'),sources=['https://www.etymonline.com/word/advance','https://en.wiktionary.org/wiki/advance#English'])
W('advanced','英 /ədˈvɑːnst/；美 /ədˈvænst/','先进的；高阶的；进展到较后期的',
 '已经走在前面，可以是技术水平高、课程程度深，也可能只是时间进程较靠后。',
 'advance + -ed，/s/ 后的 -ed 读 /t/，形成分词、形容词。不同对象决定前面是先进程度，还是某过程更后期。',AD+[['advance + -ed → advanced','已前进 → 先进、高阶、较后期']],
 'advanced technology 先进技术，an advanced course 高阶课程，advanced age 高龄。advanced 不保证每个场景都是好评价。',
 'advanced technology；an advanced course；an advanced stage。',
 'advanced 高阶、先进；advance 作修饰语常预先，如 advance booking 提前预订。advanced booking 不宜机械当同义。',
 ('This course is designed for advanced learners.','课程为高阶学习者设计。'),('The project is now at an advanced stage.','项目现已进入较后期阶段。'))
W('advancement','英 /ədˈvɑːnsmənt/；美 /ədˈvænsmənt/','进步、发展；晋升',
 '技能、知识或职业位置向前走，把这种发展过程整体提出来说。',
 '接中古英语 avancement、法语 avancement，现代可对应 advance + -ment。保留自己的名词借入历史，不仅是现代随手加尾巴。',AD[:1]+[['法语 avancement → 英语 advancement','推进、发展；职位上的提升']],
 'career advancement 职业晋升，the advancement of knowledge 知识进步，technological advancement 技术发展。',
 'career advancement；the advancement of knowledge；technological advancement。',
 'advancement 常整体过程，an advance 可一项进展；advantage 优势是相关词族的另一词，不等于发展过程。',
 ('The job offers opportunities for career advancement.','这份工作提供职业晋升机会。'),('The institute supports the advancement of scientific knowledge.','研究所支持科学知识的发展。'))
R('B3580','向前推进与把时间提前','ADVANCE：向前；ADVANCED：已走到更深、更前阶段','advance → advanced，再接 advancement；特别分清提前通知与高阶课程。',
 '最终接 ab ante，英语字母 d 后来类推加入，不是真实原始 ad- 前缀。advance 同时可空间前进和时间提前。',
 '法语 avancier → advance；advance + -ed → advanced；法语名词 avancement → advancement。',
 [['推进、阶段与发展','advance · advanced · advancement']],
 'in advance 提前；advance notice 预先通知，advanced course 高阶课程；advancement 不等于 advantage 优势。',
 'The advanced course may help with career advancement, so book in advance.\n\n这门高阶课程可能有助于职业发展，请提前预订。',
 'advance advanced advancement')
if __name__=='__main__':save('continuation_20261030_af',ROOTS,WORDS)
