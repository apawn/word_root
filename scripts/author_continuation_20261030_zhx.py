"""Common lexical gaps: harassment, notches and useful everyday clippings."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
def S(word,base):
 return ['https://en.wiktionary.org/wiki/'+word+'#English','https://www.etymonline.com/word/'+base]
EXISTING_ROOT_ADDITIONS={
 'B4146':dict(words='harry harries harried harrying'.split(),label='harry：从侵扰到接连催逼',note='和 worry 比较烦扰的场景，不是 worry 的派生。harry 承古英语 hergian 侵扰、劫掠，与古日耳曼军队材料相关；人名 Harry 另源。'),
 'B2844':dict(words='notch notches notched notching'.split(),label='notch：缺口、刻度，到记下一次成绩',note='与 cut、nick 比较刻口，不把形近当作同源证明。notch 可能经 an otch 被重新分成 a notch，早期材料接法语 oche 刻口；更远来历未定。'),
 'C1447':dict(words='sub subs subbed subbing'.split(),label='sub：不同完整词的口语缩短',note='独立词 sub 常分别截短 substitute、submarine、subtitle、subscription 等；几个完整词含 sub-，但短词的意思须回到各自原词。三明治义再接 submarine sandwich 的形状命名。'),
 'C0743':dict(words='mini minis'.split(),label='mini：小型形式与短裙',note='和 minimum 比较小的程度；mini- 主要从 miniature 截出，小义可能受 minimum 等影响。miniature 更早接拉丁 minium 红铅颜料，不是把所有 mini 都直接拆成拉丁 minus。'),
 'C0333':dict(words='doc docs'.split(),label='doc：医生、文件、纪录片的不同缩短',note='doctor、document、documentary 可以分别缩成 doc，复数 docs；都可接 docere 教导词族，却不是先从医生变成文件，再变成纪录片。'),
 'B3774':dict(words='rep reps'.split(),label='rep：代表，以及其他完整词的缩写',note='代表义缩自 representative；健身的一次缩自 repetition，名声义缩自 reputation。放在代表词旁比较缩略方法，不把这三个原词当成同一条派生链。'),
 'C1007':dict(words='rep reps'.split(),label='rep：repetition 缩短后数一次动作',note='健身 rep、reps 从 repetition 截短，接 repeat 的再做一遍词族；代表、名声等另有完整原词，不从 petere 一条线包办。'),
 'B3637':dict(words='eve eves'.split(),label='eve：傍晚，到节日前夕、事件前夕',note='eve 与 evening 同接古英语 æfen 傍晚，eve 后来丢失末尾 n；平整、相等的 even 是另一近源。人名 Eve 也另源，不能只按大小写相似硬串。'),
}
HARRY=[['古英语 hergian：作战侵扰、劫掠','与日耳曼军队的词相关'],['harry：反复侵扰 → 接连催逼、烦扰','现代常见 harried 被各种事催得团团转']]
NOTCH=[['法语 oche 刻口等材料 → otch','更远来源未定'],['可能 an otch → a notch，词界重新划分','刻口记分的使用，再接 notch up 取得成绩']]
SUB=[['substitute、submarine 等分别截成 sub','同样的缩短结果，不表示原词的意思都相同'],['substitute 一支 → 动词 sub 代班、替换','其他支要看潜艇、食物、字幕或订阅语境']]
MINI=[['拉丁 minium 红铅 → 手稿彩绘的意大利 miniatura','小画面的传统，再发展为 miniature 微型物'],['miniature → mini-；mini 也作小型的或短裙等简称','小义可能受 minimum 等影响，不能把红颜料史删掉']]
DOC=[['拉丁 docere 教导词族 → doctor、document 等','学者、教人知道情况的材料，各自发展'],['doctor、document、documentary 分别截成 doc','口语同形词，不是一种东西不断变成另一种']]
REP=[['representative、repetition、reputation 分别截短','不同原词汇到同一个 rep 拼写'],['代表；一次重复动作；名声等','意思靠搭配辨认，不把三支硬拆成同一个现代词根']]
EVE=[['古英语 æfen 傍晚 → eve，丢失末尾 n','同源形式 evening 保留了 n'],['傍晚 → 节日前一天、前夜 → 重大事件前夕','有即将到来、临近一个节点的感觉']]
W('harry','英 /ˈhæri/；美 /ˈheri/','接连烦扰、催逼；反复侵扰',
 '刚处理完一件事，又有人催下一件，没完没了地追着你，这种持续折腾就是 harry。它比问一次、提醒一次更有压力。',
 '古英语 hergian 原有侵扰、劫掠义，接日耳曼军队材料；后来从武力反复侵扰，发展为不断烦扰、催逼。人名 Harry 是另一来源。',HARRY,
 '用在催问、追赶、骚扰的动作，重点是反复、不给人喘息；现代日常更常碰到形容词 harried。',
 'harry someone with questions；harry a retreating army。',
 'hurry 是赶快、使加快，harry 是反复烦扰；催得人快一点可能造成烦扰，但两个动词不互换。',
 ('The reporters continued to harry him with questions.','记者们继续追着他不断发问。'),('The opposing team tried to harry the defender into a mistake.','对方球队想靠不断逼抢让那名后卫出错。'),sources=S('harry','harry'))
W('harries','英 /ˈhæriz/；美 /ˈheriz/','接连烦扰、催逼〔第三人称单数〕',
 '不是问完就走，而是他一直催、一直缠：he harries someone。这个形式把反复烦扰放在某个人身上。',
 'harry 的辅音字母 r 后的 y 改 i 加 -es → harries；词尾读 /z/，不是另加一个 /ɪz/ 音节。',HARRY+[['harry → harries','y 改 i 加 -es，第三人称单数']],
 '常与 with questions、into doing something 等搭配，写把对方追问、催逼到某种地步。',
 'harries the staff；harries someone into a decision。',
 'harries 是动作，harried 是已经被催得疲于应付的状态；主语和受影响的人要分开。',
 ('In the novel, the editor harries the writer for the next chapter.','小说里，编辑不停催作者交下一章。'),('The manager harries the staff with constant demands.','经理接二连三地提要求，让员工疲于应付。'),sources=S('harries','harry'))
W('harried','英 /ˈhærid/；美 /ˈherid/','被催得团团转的；疲于应付的；烦扰了',
 '一边接电话，一边找钥匙，旁边还不断有人问事，那副忙乱又被催着走的样子，就是 harried。',
 'harry 的 y 改 i 加完整 -ed → harried，词尾读 /d/。过去分词常作形容词，强调被一堆要求追着跑。',HARRY+[['harry → harried','过去烦扰；或呈现被接连催逼后的状态']],
 'a harried parent、a harried expression 都是被事情围住的感觉，既有忙也有心理压力。',
 'a harried assistant；look harried；a harried morning。',
 'hurried 是匆忙的，harried 是被事情、要求烦扰得忙乱的；忙得快和被追着催是不同重点。',
 ('The harried receptionist answered three calls at once.','那位忙得团团转的前台同时接了三个电话。'),('He gave me a harried smile and hurried back to work.','他带着疲于应付的神情朝我笑了笑，赶回去继续工作。'),sources=S('harried','harry'))
W('harrying','英 /ˈhæriɪŋ/；美 /ˈheriɪŋ/','正在反复烦扰、催逼、侵扰',
 '一次次追问、催促，还在继续，这个正在折腾对方的过程就是 harrying。',
 'harry + -ing，保留 y；基础末尾 /i/ 与 -ing 的 /ɪŋ/ 相接，不按 harried 改成 i 后再加后缀。',HARRY+[['harry + -ing → harrying','持续烦扰、逼迫的过程']],
 '可用于人际催逼，也用于不断袭扰的历史、军事叙述；动作都带持续纠缠的感觉。',
 'harrying someone with questions；stop harrying the staff。',
 'harrying 写施压过程，worrying 可以是自己担心，也可以令人担心；不能只看到中文烦就直接替换。',
 ('She asked the callers to stop harrying her for an answer.','她请来电者别再不停催她给答案。'),('The novel describes small units harrying the retreating force.','小说描写了小队反复袭扰撤退部队的情形。'),sources=S('harrying','harry'))
W('notch','英 /nɒtʃ/；美 /nɑtʃ/','V 形等缺口、刻痕；一档、一筹；刻下缺口、取得成绩',
 '木棒上每成功一次就刻一道痕，notch 能把小缺口、计数、成绩串起来。把音量降一档，也可说 down a notch。',
 '可能由 an otch 被重新听成 a notch，接法语 oche 刻口材料；远源未定。刻痕用于记分，后来有 notch up 记下一次成功的说法。',NOTCH,
 '名词说切口、一级程度；动词说刻口或取得。a notch above 比某人某物高一筹，不是一定真有刻度。',
 'a notch in the wood；turn it down a notch；notch up a win。',
 'nick 常是轻碰出的小口子，notch 常让人想到有形状的凹口、刻度；近义、形近不等于已证实同源。',
 ('There is a small notch in the wooden handle.','木柄上有一个小凹口。'),('The team hopes to notch up another win.','球队希望再取得一场胜利。'),sources=S('notch','notch'))
W('notches','英 /ˈnɒtʃɪz/；美 /ˈnɑtʃɪz/','缺口、刻痕；几档、几级；取得〔第三人称单数〕',
 '腰带不同位置的几个口子，或温度、水平往上挪了几档，都能用 notches。',
 'notch + -es，/tʃ/ 后读 /ɪz/；名词复数、动词三单同形。',NOTCH+[['notch + -es → notches','多个刻口、等级；或他、她记下一次成绩']],
 '数真实凹口，也能数比喻中的程度变化；动词常接 up 与胜利、纪录等对象。',
 'several notches；a few notches higher；notches up a victory。',
 'notches higher 不保证有统一单位，只说高了几档；degrees 则可能是精确角度、温度单位。',
 ('The stick has three notches cut into it.','那根木棒上刻着三个凹口。'),('The argument raised the tension a few notches.','那场争论让气氛又紧张了几分。'),sources=S('notches','notch'))
W('notched','英 /nɒtʃt/；美 /nɑtʃt/','刻出缺口了；有缺口的；取得了成绩',
 '木头边缘已经切出一个凹口，是 notched；球队已经拿下一场胜利，也能说 notched up a win。',
 'notch + 完整 -ed，/tʃ/ 后读 /t/；过去式、过去分词也可作有缺口的形容词。',NOTCH+[['notch + -ed → notched','切出刻口；或记下一次成绩']],
 'notched the wood 描写实物加工，notched up a victory 描写成绩；读对象就能换画面。',
 'a notched edge；notched up a record；notched the handle。',
 'notched 是凹口、刻痕，scratched 可以只是表面划痕；不是每条浅划线都有明显凹缺。',
 ('The carpenter notched the end of the board.','木匠在木板末端切出一个缺口。'),('The team notched up its fifth win of the season.','球队拿下了本赛季第五场胜利。'),sources=S('notched','notch'))
W('notching','英 /ˈnɒtʃɪŋ/；美 /ˈnɑtʃɪŋ/','正在刻下缺口；取得、记下成绩',
 '一刀刀切出凹口，或把新成绩记入自己的记录，都是 notching 对应的过程。',
 'notch + -ing，保留 ch；词尾不需要再添辅音字母。',NOTCH+[['notch + -ing → notching','刻口或取得成绩的过程']],
 'notching up achievements 常写持续积累成绩；实际木工中则按切口动作理解。',
 'notching the wood；notching up victories。',
 'notching up 强调取得并记下一次成绩，scoring 也可直接说得分；赢一场和得一分不是同一种计数。',
 ('He was notching the wooden posts before fitting the rails.','安装横栏前，他正在木柱上切出凹口。'),('She ended the season by notching up another victory.','她又拿下一场胜利，结束了这个赛季。'),sources=S('notching','notch'))
W('sub','/sʌb/','替补、代课者；潜艇；长面包三明治；字幕、订阅等的简称；代班',
 '比赛里上场顶人的，是 sub；午餐点 a sub，通常却是长面包三明治。几个长词都被省成了 sub，不能见这个词就一律理解成在下面。',
 '分别截短 substitute、submarine、subtitle、subscription 等。submarine sandwich 因外形像潜艇得名，再缩为 sub。动词代班、替换主要接 substitute 这支。',SUB,
 'sub for someone 是替某人代班；a sub 可是替补或潜艇、三明治。电影、视频里的 subs 常指字幕，频道里的 subs 又可能指数订阅者。',
 'a substitute teacher → a sub；sub for a colleague；a meatball sub。',
 '独立词 sub 需要还原具体原词；sub- 前缀只是构词材料，两者不能在句中直接互换。',
 ('Could you sub for me on Friday?','周五你能替我代班吗？'),('I ordered a cheese sub for lunch.','午饭我点了一份奶酪长面包三明治。'),('The sub remained below the surface.','那艘潜艇一直待在水面以下。'),sources=S('sub','sub'))
W('subs','/sʌbz/','替补、潜艇、长面包三明治〔复数〕；字幕、订阅等〔口语〕；代班〔第三人称单数〕',
 '教练派上几个替补，叫 subs；看原声片打开 subs，又是字幕。先看场景，再找它省略了哪个完整词。',
 'sub + -s，/b/ 后读 /z/；名词复数与动词三单同形。字幕接 subtitles 的缩短，订阅、会员费等另接 subscription 一支。',SUB+[['sub + -s → subs','不同缩略名词的复数；或他、她代班']],
 'sports subs 是替补；English subs 是英语字幕；pay your subs 在英式社团语境可说缴会费。',
 'bring on the subs；English subs；club subs。',
 'subs 不是任何场景都指订阅者：a film with subs 谈字幕，two subs for lunch 谈食物。',
 ('The coach brought on two subs after the break.','中场休息后，教练换上了两名替补。'),('We watched the film with English subs.','我们开着英语字幕看了那部电影。'),sources=S('subs','sub'))
W('subbed','/sʌbd/','代班了；被换下、被替换了；加了字幕的〔口语〕',
 '球员踢到一半被换下，是 was subbed off；视频写 English-subbed，则在说配了英语字幕。这里仍然是不同完整词缩短后的分支。',
 'sub 双写 b 加完整 -ed → subbed，读 /d/。代班、替换接 substitute；加字幕接 subtitle，不把两个动作说成同一事件。',SUB+[['sub → subbed','双写 b 加 -ed，按原词分支理解']],
 'subbed for a teacher 是代课过；subbed off 是被换下，subbed on 是被换上。字幕义多见视频交流语境。',
 'subbed for a colleague；was subbed off；a subbed version。',
 'subbed off 与 subbed on 方向相反；off 离场，on 上场，只看 subbed 无法判断换入还是换出。',
 ('She subbed for the regular teacher on Monday.','周一她替正式任课老师代了课。'),('He was subbed off shortly after half-time.','下半场开始没多久，他就被换下了。'),sources=S('subbed','sub'))
W('subbing','/ˈsʌbɪŋ/','正在代班、代课、替换；添加字幕〔口语〕',
 '临时替老师上课，这份工作进行中，是 subbing；字幕组给视频配文字，也可在口语里用 subbing。',
 'sub 双写 b 加 -ing → subbing。不同缩略动词共享这个拼写，代班接 substitute，加字幕接 subtitle。',SUB+[['sub → subbing','双写 b 加 -ing，代班或配字幕的过程']],
 'subbing for someone 交代替谁顶班；subbing a video 交代给视频配字幕。',
 'subbing at a school；subbing for a colleague；subbing the video。',
 'subbing 不一定有翻译：把原语对白写成同语字幕也属于字幕工作；dubbing 则是替换或加入配音。',
 ('I am subbing for a colleague this week.','这周我在替一位同事代班。'),('The volunteers are subbing the video in English.','志愿者正在给视频配英语字幕。'),sources=S('subbing','sub'))
W('mini','/ˈmɪni/','迷你的、小型的；迷你裙等的简称',
 '把常见尺寸缩成一个小版本，就是 mini 的直观感觉：mini cakes 是小蛋糕。说 a mini 时，还可能省略了裙子、模型等具体对象。',
 '表示小的 mini- 主要从 miniature 截出；后者经意大利手稿彩绘词接拉丁 minium 红铅，因小画面发展出微型义，小义又可能受 minimum 等影响。名词 mini 可缩自 miniskirt。',MINI,
 'mini 作修饰语常表示小型版本；a mini 在服装语境常指超短裙。大写 Mini 另可能是汽车名称，要看上下文。',
 'a mini cake；a mini fridge；wear a mini。',
 'mini 侧重尺寸、篇幅或规模小，minimum 是最低数量、程度；迷你冰箱不等于某个法定最低标准。',
 ('Each guest received a mini cake.','每位客人都拿到一个迷你蛋糕。'),('She chose a black mini for the party.','她挑了一条黑色迷你裙去参加聚会。'),sources=S('mini','mini')+['https://www.etymonline.com/word/mini-'])
W('minis','/ˈmɪniz/','迷你裙、小模型等〔mini 的名词复数〕',
 '服装店里几条超短裙，可以叫 minis；桌游玩家桌上几个人物小模型，也能叫 minis。数的是什么，靠被省掉的名词补回来。',
 'mini + -s，读 /z/；这里是名词复数。小模型义缩自 miniature，短裙义缩自 miniskirt，并非形容词见到复数名词就要加 s。',MINI+[['mini + -s → minis','多件被简称为 mini 的具体物品']],
 'minis 适合上下文已清楚具体物品的交流；第一次提及，可用 miniskirts、miniatures 等完整词。',
 'skirts from minis to maxis；paint the minis；collect minis。',
 'mini cakes 的 mini 是修饰语，不随 cakes 变成 minis；minis 能数几件，是因为它已经作名词。',
 ('The shop sells skirts ranging from minis to long evening styles.','那家店卖的裙子，从迷你裙到晚装长裙都有。'),('The players painted their minis before the game.','玩家们在游戏前给各自的小模型上了色。'),sources=S('minis','mini')+['https://www.etymonline.com/word/mini-'])
W('doc','英 /dɒk/；美 /dɑk/','医生；文档、文件；纪录片〔非正式简称〕',
 '说 Thanks, doc，通常在谢医生；同事发来 a doc，通常是文件。不是医生变成了文件，而是几个完整词刚好都省成 doc。',
 '分别截短 doctor、document、documentary。doctor 从教师、学者发展出医生称谓；document 接教人知道情况的凭据、文件词族；缩短发生在各自完整词之后。',DOC,
 'doc 称医生有熟悉、随意的语气；工作交流里的 a shared doc 是共享文档；影视交流里的 a nature doc 是自然纪录片。',
 'Thanks, doc；a shared doc；a nature doc。',
 'doc 的文件义与 dock 码头同音，但拼写、词源不同；文件名的 .doc 又是格式扩展名，不能把所有文档都认成同一文件格式。',
 ('The doc asked me how I was feeling.','医生问我感觉怎么样。'),('I added my comments to the shared doc.','我把意见补进了共享文档。'),('We watched a doc about coral reefs.','我们看了一部讲珊瑚礁的纪录片。'),sources=S('doc','doc'))
W('docs','英 /dɒks/；美 /dɑks/','医生；文档资料、文件；纪录片〔复数，非正式〕',
 '开发者让你 read the docs，意思是看文档资料；纪录片节里的 docs，则是一部部纪录片。前后的话会告诉你是哪种简称。',
 'doc + -s，/k/ 后读 /s/。doctor、document、documentary 各支都可有此复数；技术文档里 docs 常把一套说明材料整体说出来。',DOC+[['doc + -s → docs','多个医生、文件、纪录片，或成套文档资料']],
 'the docs 在软件语境常是使用说明、技术资料；send the docs 可是发送文件，仍按具体场景判断。',
 'read the docs；technical docs；historical docs〔纪录片语境〕。',
 'docs 是非正式说法，正式标题可用 documentation、documents、documentaries；要换回哪个词，取决于实际所指。',
 ('Please read the docs before changing the settings.','改设置前请先读文档说明。'),('The festival includes several short docs about city life.','电影节里有几部讲城市生活的纪录短片。'),sources=S('docs','doc'))
W('rep','/rep/','代表、销售代表；一次重复动作；名声〔口语简称〕',
 '公司派来跟你沟通的人，是 a rep；健身抬起、放下一整次，也是 a rep。两个意思很远，是因为它们省略的完整词不同。',
 '代表缩自 representative，一次重复缩自 repetition，名声缩自 reputation。三种缩短各有历史，学习时分别接回原词。',REP,
 'a sales rep 是销售代表；one rep 是一遍完整训练动作；a bad rep 是坏名声。演员、剧团语境还有 repertory 的简称，先认识常用三支。',
 'a union rep；one more rep；have a bad rep。',
 '健身 rep 数完整重复次数，set 是一组，里面可含多个 reps；不能把 ten reps 直接理解成十组。',
 ('A sales rep will call you tomorrow.','明天会有一位销售代表给你打电话。'),('Try to complete one more rep.','争取再完整做一次。'),('The café has a good rep among local students.','那家咖啡馆在本地学生中口碑不错。'),sources=S('rep','rep'))
W('reps','/reps/','代表们；重复次数、几次完整动作〔rep 的复数〕',
 '两位销售代表是 two reps；健身的 ten reps 是同一个动作完整做十次，通常不是做十组。',
 'rep + -s，/p/ 后读 /s/；代表接 representative，一次重复接 repetition，复数拼写一样，所数的东西不同。',REP+[['rep + -s → reps','多个代表，或多次完整重复动作']],
 'three sets of ten reps 是三组、每组十次；union reps 是工会代表，两者由搭配即可分开。',
 'sales reps；union reps；eight reps per set。',
 'reps 是每组里的次数，sets 是组数；two sets of ten reps 合起来通常二十次，不是十二次。',
 ('The union reps met the management team.','工会代表们与管理团队见了面。'),('Start with two sets of eight reps.','先做两组，每组八次。'),sources=S('reps','rep'))
W('eve','/iːv/','节日前一天、前夜；某事发生前夕；傍晚〔文学用法〕',
 '事情还没正式开始，却已经站在门口了，这就是 on the eve of 的感觉。节日将到的前一天、前夜，也叫 eve。',
 '承古英语 æfen 傍晚，后来丢失末尾 n；节日前一晚再扩到前一天、重大事件前夕。与 evening 同支，与平整、相等的 even 近源不同。',EVE,
 'Christmas Eve 是圣诞前夕；on the eve of the election 是选举前夕，不一定只精确指前一晚那几个小时。',
 'New Year’s Eve；on the eve of departure；the eve of a new era。',
 'eve 通常依附一个将来的节点；evening 日常说傍晚、晚上。人名 Eve 则是另一来源。',
 ('We arrived on the eve of the festival.','我们在节日前一天到达。'),('The country stood on the eve of a major change.','这个国家正处在一场重大变革的前夕。'),sources=S('eve','eve'))
W('eves','/iːvz/','节日前夜、前夕〔复数〕',
 '回忆好几年的节日前夜，就可能说 eves。它确实能按一个个前夕来数，不过日常使用仍以单数搭配具体节日更常见。',
 'eve + -s，读 /z/；保留末尾不发音 e，不另加音节。复数用于多次、多种节日或事件的前夕。',EVE+[['eve + -s → eves','多个节日前夕、事件前夕']],
 '适合比较不同年份、不同节日前夜；普通叙述一次事件，仍用 the eve of。',
 'festival eves；Christmas Eves；on the eves of major festivals。',
 'eves 是前夕，eaves 是屋檐，二者同音；屋檐下用 under the eaves，别漏掉 a。',
 ('Shops often stay open late on the eves of major festivals.','重大节日前夜，商店往往营业到很晚。'),('She remembered the quiet Christmas Eves of her childhood.','她想起了童年那些安静的圣诞前夜。'),sources=S('eves','eve'))
def extend_lessons():
 extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_zhx',ROOTS,WORDS)
 extend_lessons()
