"""Intimidation, minor irritation and emphatic frustration."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
def S(word,base):
 return ['https://en.wiktionary.org/wiki/'+word+'#English','https://www.etymonline.com/word/'+base]
EXISTING_ROOT_ADDITIONS={
 'B3977':dict(words='brow browbeat browbeats browbeaten browbeating'.split(),label='browbeat：用严厉脸色、声势压人',note='brow 加 beat；早期是用严厉、傲慢的目光压倒对方，眉眼属于施压的人，不是殴打受害者的眉毛。'),
 'C1521':dict(words='timid intimidate intimidates intimidated intimidating intimidatingly intimidator intimidators intimidation'.split(),label='intimidate：使人进入胆怯状态',note='接中世纪拉丁 in- 加 timidus 的材料；in- 在此不是否定。可以是故意恐吓，也可以是陌生、庞大的事物让人感到压力。'),
 'A1760':dict(words='bully bullies bullied bullying bother bothered unbothered'.split(),label='bully 的不同历史与 unbothered 的否定状态',note='bully 早期有亲昵称呼，后来贬化为欺凌者并转动词；unbothered 则是 un- 加 bothered，表示没受困扰，不能把相似结尾都当成同一词源。'),
 'A2238':dict(words='hassle hassles hassled hassling'.split(),label='hassle：麻烦折腾与不断烦人',note='现代常用的 hassle 名词先见于动词，远源未定；后接英语规则词尾，不能只凭 -le 就断定确切古代构词。'),
 'A1849':dict(words='irk irks irked irking irksome irksomely'.split(),label='irk：不大不小却一直碍心的烦',note='irk 有古老疲倦、不愿、困扰材料，远源未定，早期相关形容词也很早；不把与 work 或其他语言的可能联系硬写成定论。'),
 'C0088':dict(words='exasperate exasperates exasperated exasperating exasperatingly exasperation'.split(),label='exasperate：把耐心磨粗、磨掉的恼火',note='拉丁 ex- 加 asper 粗糙形成 exasperare，已有激怒义；磨粗耐心是记忆画面，不能当作英语实际字面构词。'),
 'A1904':dict(words='infuriate infuriates infuriated infuriating infuriatingly'.split(),label='infuriate：使人进入怒火',note='接中世纪拉丁 infuriare、infuriatus，亦有意大利语中介分析，内层为 in furia 在怒火中；in- 不是否定。'),
}
BROWBEAT=[['brow 眉眼、脸色 + beat 打、压倒 → browbeat','早期写以严厉或傲慢的目光压人，施压者自己的眉眼是关键'],['以脸色压人 → 以威势、严厉话语迫使屈服','现代可写把人逼得答应，不要求真的动手打人']]
BULLY=[['早期 bully：亲昵称呼、好伙伴','来源未定，可能联系荷兰语相关词'],['逞威风者 → 欺凌者；名词再转动词','词义逐渐贬化，不能因现代指欺负弱者，就倒说最初已经是贬义']]
INTIMIDATE=[['拉丁 timidus 胆怯 + in- → 中世纪拉丁 intimidare','使害怕，in- 在这里参与表示使进入的状态'],['intimidatus → 英语 intimidate','恐吓、吓阻；也能写能力、环境等让人有压力，不一定有人故意威胁']]
BOTHER=[['bauther、bather 等相关英语形式 → bother','远源未定，爱尔兰语、苏格兰语等相关解释尚不能化为唯一确定路线'],['bother → bothered → unbothered','使困扰到感到困扰，再用否定 un- 写没有因此烦恼']]
HASSLE=[['现代 hassle：麻烦、折腾、烦扰','更早材料有方言喘气声、骚扰动词等不同分析，来源未定'],['hassle 名词 → 动词','不断烦人、催逼；英语再接规则词尾']]
IRK=[['早期 irk 相关疲倦、不愿、困扰材料','相关形容词出现也很早，远源未定，不能只按短词顺序倒推年代'],['irk 惹烦 → irksome → irksomely','让人不快、感到繁琐；不是任何时候都达到强烈愤怒']]
EXASPERATE=[['拉丁 ex- + asper 粗糙 → exasperare、exasperatus','使变粗糙，并有激怒、使烦躁的抽象义'],['英语 exasperate','使恼火、失去耐心；不是英语先说磨粗物体才突然发明情绪义']]
INFURIATE=[['拉丁 in furia 在怒火中 → 中世纪拉丁 infuriare、infuriatus','使狂怒；亦有意大利语 infuriato 中介分析'],['英语 infuriate → infuriating、infuriatingly','使火冒三丈；再形容令人恼火的性质与程度']]
W('browbeat','/ˈbraʊbiːt/','以威势、严厉言语吓住、逼迫',
 '不靠讲道理，而是板着脸、摆出强硬架势，一句句压得对方不敢拒绝，就是 browbeat。画面里的眉眼是施压者的脸色。',
 'brow 眉眼、脸色 + beat 打、压倒；最早用法写严厉目光压人，具体眉部动作的细节仍有不同理解。常用变化 browbeat—browbeat—browbeaten。',BROWBEAT,
 'browbeat someone into agreeing 以威势逼人答应；refuse to be browbeaten 不肯被吓服。',
 'try to browbeat a witness；browbeat someone into silence。',
 'persuade 靠说服使人同意，browbeat 突出以威势、严厉态度压人；不能把被迫屈服译成心悦诚服。',
 ('He tried to browbeat us into accepting the deal.','他企图用威势逼我们接受交易。'),('She would not let them browbeat her into silence.','她不肯让他们用威势逼得自己不敢开口。'),sources=S('browbeat','browbeat'))
W('browbeats','/ˈbraʊbiːts/','以威势、严厉言语逼迫〔第三人称单数〕',
 '老板不容人解释，板着脸、提高声势逼每个人同意，叫 he browbeats his staff。',
 'browbeat + -s，/t/ 后读 /s/；内层 brow + beat 的固定动词整体再加三单词尾。',BROWBEAT+[['browbeat + -s → browbeats','他用强硬态度压服对方']],
 'browbeats his staff 以威势压员工；browbeats people into agreeing 逼人同意。',
 'constantly browbeats；browbeats anyone who questions him。',
 'leads a team 只说带领团队，browbeats a team 则评价其方法是强硬施压；不是中性的管理词。',
 ('He browbeats his staff instead of listening to them.','他总以威势压员工，不听他们的意见。'),('She browbeats everyone into following her plan.','她用强硬态度逼所有人按她的计划做。'),sources=S('browbeats','browbeat'))
W('browbeaten','/ˈbraʊbiːtən/','被威势压住、吓服的；饱受严厉对待的',
 '长期被吼、被压着说话，渐渐不敢开口，人会显得 browbeaten。不是眉毛受伤，而是气势被压下去。',
 'browbeat 的过去分词 browbeaten；末部沿 beat—beat—beaten 的变化，不能机械加 -ed。',BROWBEAT+[['browbeat → browbeaten','受强硬施压后的状态；也作过去分词']],
 'looked browbeaten 显得被压得抬不起头；refused to be browbeaten 拒绝被吓服。',
 'a browbeaten employee；browbeaten into agreement。',
 'quiet 可以本来就安静，browbeaten 则暗示受到强硬对待后畏缩、被压制的处境。',
 ('The browbeaten assistant barely spoke during the meeting.','那位饱受严厉对待的助理在会上几乎没说话。'),('I refuse to be browbeaten into signing something I do not understand.','我不肯因对方威逼就签下自己不懂的东西。'),sources=S('browbeaten','browbeat'))
W('browbeating','/ˈbraʊbiːtɪŋ/','以威势、严厉言语逼迫；这种施压行为',
 '不给人讨论余地，一轮轮摆威风、逼同意，整个行为叫 browbeating；它常带批评这种做法的口气。',
 'browbeat + -ing，beat 的 ea 是两个元音字母，不按单个短元音字母后双写 t；动作形式也可作名词。',BROWBEAT+[['browbeat + -ing → browbeating','施压正在进行；或把这种威逼行为整体命名']],
 'stop browbeating someone 停止以威势压人；constant browbeating 不断威逼。',
 'browbeating people into compliance；a session of browbeating。',
 'browbeating 突出压人屈服，debating 是讨论争辩；声音大不自动构成前者，要看是否以威势压制。',
 ('Stop browbeating him and let him explain.','别再用威势压他了，让他解释。'),('Constant browbeating will not build a strong team.','不停威逼压人，建不起一支强大的团队。'),sources=S('browbeating','browbeat'))
W('bullies','/ˈbʊliz/','欺凌者〔复数〕；欺负、胁迫〔第三人称单数〕',
 '几个人专挑比自己弱、不敢反抗的人下手，是 bullies；一个人总这样做，动词也用 bullies。',
 'bully 的 y 变 i 加 -es；名词复数、动词三单同形。早期 bully 曾是亲昵称呼，后来贬化为欺凌者，再转动词。',BULLY+[['bully → bullies','多个欺凌者；他欺负、以强压弱']],
 'stand up to bullies 勇敢面对欺凌者；bullies younger children 欺负更小的孩子。',
 'school bullies；bullies people into giving in。',
 'argues with someone 不一定有强弱压迫，bullies someone 则明确带欺负、胁迫意味；不是普通意见不合的中性词。',
 ('The teacher made it clear that bullies would not control the classroom.','老师明确表示，不能让欺凌者在班上横行。'),('He bullies younger children into giving him their snacks.','他欺负更小的孩子，逼他们把零食交给他。'),sources=S('bullies','bully'))
W('intimidates','/ɪnˈtɪmɪdeɪts/','恐吓、使胆怯；使望而生畏〔第三人称单数〕',
 '体格、声势、权力让你不敢反驳，叫 intimidates you；庞大的任务让新手不知如何下手，也可以这样说。',
 'intimidate + -s，/t/ 后读 /s/；内层中世纪拉丁 in- + timidus 胆怯，in- 参与使进入状态，不是否定。',INTIMIDATE+[['intimidate + -s → intimidates','他或它使人害怕、退缩']],
 'intimidates beginners 让初学者望而生畏；intimidates witnesses 恐吓证人。',
 'intimidates everyone in the room；a task that intimidates me。',
 'intimidates 可以来自人有意威胁，也可来自任务本身的难度；不要在手册、考试作主语时强译成故意恐吓。',
 ('The thick manual intimidates many beginners.','厚厚的手册让许多初学者望而生畏。'),('He intimidates people by shouting over them.','他靠大声压过别人来吓住他们。'),sources=S('intimidates','intimidate'))
W('intimidated','/ɪnˈtɪmɪdeɪtɪd/','被吓住、感到压力而退缩的；恐吓了',
 '面对满屋专家，你本来有问题却不敢举手，这种被气场、难度压住的感觉就是 intimidated。',
 'intimidate 去 e 加完整 -ed；/t/ 后读 /ɪd/。过去分词可作形容词，写承受压力、胆怯的一方。',INTIMIDATE+[['intimidate → intimidated','已经使胆怯；或人受到影响而退缩']],
 'intimidated by experts 被专家的气场吓住；feel intimidated 感到压力、不敢行动。',
 'refuse to be intimidated；a little intimidated。',
 'intimidated 是自己的感受，intimidating 是引起这份感受的性质：an intimidated student 面对 an intimidating task。',
 ('I felt intimidated by the room full of experts.','面对满屋专家，我有些怯场。'),('She refused to be intimidated by his threats.','她不肯被他的威胁吓住。'),sources=S('intimidated','intimidate'))
W('intimidatingly','/ɪnˈtɪmɪdeɪtɪŋli/','令人望而生畏地；带威吓意味地',
 '任务大到让人不敢开始，是 intimidatingly large；人朝你逼近、让你害怕，也能用它描写方式。',
 'intimidating + -ly；内层 intimidate 去 e 加 -ing，外层修饰令人胆怯的程度或动作方式。',INTIMIDATE+[['intimidate → intimidating → intimidatingly','使胆怯的性质，转成程度或方式']],
 'intimidatingly large 大得令人望而生畏；stood intimidatingly close 站得逼人、令人害怕。',
 'intimidatingly complex；intimidatingly high standards。',
 'impressively large 侧重令人赞叹，intimidatingly large 多了一层让人不敢下手的压力；两种感觉可能同时存在。',
 ('The list of requirements looked intimidatingly long.','要求清单长得让人望而生畏。'),('He stood intimidatingly close to the receptionist.','他逼近前台接待员，站得让人害怕。'),sources=S('intimidatingly','intimidate'))
W('unbothered','英 /ʌnˈbɒðəd/；美 /ʌnˈbɑðərd/','不烦恼、不受影响的；不在意的',
 '周围吵，对方仍安心读书；别人说闲话，他也不往心里去，这种没被搅动的状态是 unbothered。',
 '否定 un- + bothered；bother 加完整 -ed 得到受到困扰的状态，外层 un- 把它否定。',BOTHER+[['un- + bothered → unbothered','没有受困扰、不因此烦恼']],
 'unbothered by criticism 不因批评烦恼；seem unbothered 显得不在意。',
 'remain unbothered；perfectly unbothered by the noise。',
 'unbothered 可以是从容，不一定是冷漠；indifferent 更侧重不关心、不偏好，是否在乎事情与是否感到烦是两回事。',
 ('She seemed unbothered by the criticism.','她似乎没因那些批评烦恼。'),('The cat lay unbothered beside the noisy washing machine.','洗衣机很吵，猫却毫不受影响地躺在旁边。'),sources=S('unbothered','bother'))
W('hassles','/ˈhæsəlz/','麻烦、折腾人的事〔复数〕；不断烦扰〔第三人称单数〕',
 '手续来回补、电话打不通，这一串让人折腾的麻烦叫 hassles；一个人不停来催，也能用动词 hassles。',
 'hassle + -s，读 /z/；名词复数和动词三单同形。现代烦扰动词由麻烦名词发展，远源未定。',HASSLE+[['hassle + -s → hassles','多件折腾人的麻烦；他不断烦扰']],
 'avoid unnecessary hassles 避免没必要的折腾；travel hassles 旅途中的麻烦。',
 'hassles me about the paperwork；without any hassles。',
 'hassles 口语里突出折腾、烦人，不一定是严重故障；a challenge 可以中性甚至积极，hassle 通常偏负面。',
 ('Booking online saved us a lot of travel hassles.','网上预订让我们少了许多旅途中的折腾。'),('He hassles me about the paperwork every morning.','他每天早上都来催那些材料，烦得很。'),sources=S('hassles','hassle'))
W('hassling','/ˈhæslɪŋ/','正在烦扰、纠缠、催逼',
 '你已经说会处理，对方还是一遍遍来催，口语里可以说 stop hassling me。重点是被烦得没法清静。',
 'hassle 去 e 加 -ing；基础名词麻烦转动词烦扰，再表示动作正在发生。',HASSLE+[['hassle → hassling','正在反复烦人、催逼']],
 'stop hassling me 别再烦我；hassling someone for payment 追着催付款。',
 'kept hassling；hassling visitors at the entrance。',
 'hassling 常用口语，harassing 通常更有持续侵扰的重量；具体语气仍取决于行为、对象与场景。',
 ('Stop hassling me; I said I would send it tonight.','别再催我了，我说过今晚会发。'),('Street sellers were hassling tourists outside the station.','街头摊贩在车站外纠缠游客。'),sources=S('hassling','hassle'))
W('irks','英 /ɜːks/；美 /ɝks/','使烦恼、不快〔第三人称单数〕',
 '并非惊天大事，但某个习惯每次出现都会让你心里一硌，可以说 it irks me。',
 'irk + -s，/k/ 后读 /s/；irk 更早来源未定，不能把与工作、疲倦材料的可能联系当成定论。',IRK+[['irk + -s → irks','它使人觉得烦、不快']],
 'what irks me is 让我不快的是；really irks her 真让她烦。',
 'irks the neighbours；irks me every time。',
 'irks 常写某件事令人在意、不舒服；enrages 更明确写激起强烈怒火，别把所有心里一烦都译成暴怒。',
 ('It irks me when people leave dirty cups on my desk.','别人把脏杯子留在我桌上，真让我烦。'),('What irks her most is the lack of an explanation.','最让她不快的是根本没人解释。'),sources=S('irks','irk'))
W('irked','英 /ɜːkt/；美 /ɝkt/','被惹得不快、心烦的；使不快了',
 '一直被小事绊着，心里不舒服但未必大发脾气，可以说 felt irked。它常写一层甩不掉的烦。',
 'irk + 完整 -ed，/k/ 后读 /t/；可作过去形式，也可形容感到不快的状态。',IRK+[['irk + -ed → irked','过去惹烦；或受到影响而不快']],
 'irked by the delay 因拖延不快；irked at the suggestion 因这个提议感到不悦。',
 'slightly irked；visibly irked。',
 'irked 表示不快，不要求表现为大吼；visibly irked 才额外说明情绪已显露出来。',
 ('She was irked by the repeated delays.','一再拖延让她心烦。'),('His casual dismissal of the problem irked me.','他满不在乎地把问题带过，让我很不快。'),sources=S('irked','irk'))
W('irking','英 /ˈɜːkɪŋ/；美 /ˈɝkɪŋ/','正在使烦恼、不快',
 '小噪声还在持续，你越听越心烦，就是 it is irking you。它写的是不快正在被引起。',
 'irk + -ing；词尾 rk 是两个辅音字母，直接加 -ing，不双写 k。',IRK+[['irk + -ing → irking','使人觉得烦、不舒服的过程']],
 'irking me 让我烦；kept irking her 一直惹得她不快。',
 'what is irking him；the detail that was irking me。',
 'irking 说事物在惹烦，irritably 说人自己烦躁地做事；不是看见相近中文就换同一个句法位置。',
 ('The tapping sound was irking everyone in the room.','敲击声正让屋里每个人都心烦。'),('What was irking her was his refusal to listen.','让她心烦的是他拒绝倾听。'),sources=S('irking','irk'))
W('irksomely','英 /ˈɜːksəmli/；美 /ˈɝksəmli/','烦人地；令人厌烦地',
 '手续重复得没意义，让人一遍遍耗耐心，是 irksomely repetitive；这个副词给描述加上繁琐、烦人的感受。',
 'irksome + -ly，保留 e；内层 irk + -some 形容会令人烦的性质，外层再作副词。',IRK+[['irk → irksome → irksomely','使烦 → 令人烦的 → 烦人地']],
 'irksomely slow 慢得烦人；irksomely repetitive 烦人地重复。',
 'irksomely detailed；irksomely familiar excuses。',
 'detailed 只说详细，irksomely detailed 则从读者角度评价细到令人烦；不是所有细节充分的说明都带负面。',
 ('The process was irksomely slow.','这个流程慢得让人烦。'),('The instructions were irksomely repetitive.','说明重复得令人厌烦。'),sources=S('irksomely','irk'))
W('exasperates','/ɪɡˈzæspəreɪts/','使恼火、失去耐心〔第三人称单数〕',
 '讲了几遍还被同样的借口挡回来，人终于想说“够了”，这种把耐心磨掉的作用就是 exasperates。',
 'exasperate + -s，/t/ 后读 /s/；基础词接拉丁 ex- 加 asper 粗糙的材料，拉丁语里已有激怒义。',EXASPERATE+[['exasperate + -s → exasperates','它使人恼火、越来越没耐心']],
 'exasperates me 让我烦透了；exasperates everyone 让大家失去耐心。',
 'what exasperates her；constantly exasperates。',
 'exasperates 常写反复受阻后的不耐烦，infuriates 更直接写激起强烈怒火；二者可交叠，不必硬定所有语境的等级。',
 ('His refusal to give a straight answer exasperates me.','他不肯直接回答，让我烦透了。'),('The printer exasperates everyone by jamming every few pages.','打印机每打几页就卡纸，把大家的耐心都磨光了。'),sources=S('exasperates','exasperate'))
W('exasperatingly','/ɪɡˈzæspəreɪtɪŋli/','令人恼火、失去耐心地',
 '按钮明明按了，屏幕却慢吞吞没反应，一次又一次，叫 exasperatingly slow。描述的是某种程度把耐心耗掉。',
 'exasperating + -ly；内层 exasperate 去 e 加 -ing，外层多修饰慢、含糊等性质的程度。',EXASPERATE+[['exasperate → exasperating → exasperatingly','使恼火的性质，转成程度或方式']],
 'exasperatingly slow 慢得令人抓狂；exasperatingly vague 含糊得让人没耐心。',
 'exasperatingly difficult；exasperatingly inconsistent。',
 'exasperatingly 是事物让人恼火；in exasperation 常写人自己失去耐心后的反应，例如 sighed in exasperation。',
 ('The machine responded exasperatingly slowly.','机器反应慢得让人失去耐心。'),('His explanation was exasperatingly vague.','他的解释含糊得让人烦透了。'),sources=S('exasperatingly','exasperate'))
W('infuriates','/ɪnˈfjʊərieɪts/','使大怒、火冒三丈〔第三人称单数〕',
 '已经不是轻轻皱眉，而是被不公、轻慢等直接点起怒火，叫 infuriates me。',
 'infuriate + -s，/t/ 后读 /s/；内层来自拉丁 in furia 在怒火中一类材料，经中世纪拉丁、可能的意大利语中介进入英语。',INFURIATE+[['infuriate + -s → infuriates','它使人愤怒、怒火上来']],
 'infuriates me 让我火大；infuriates the fans 激怒球迷。',
 'what infuriates her；absolutely infuriates。',
 'infuriates 是使人愤怒，infuriated 是已经愤怒的人，infuriating 是令人愤怒的事；先分作用方向，再记中文。',
 ('It infuriates me when people take credit for someone else’s work.','有人把别人的成果据为己有，这让我非常愤怒。'),('The unfair decision infuriates the supporters.','这个不公的决定激怒了支持者。'),sources=S('infuriates','infuriate'))
W('infuriatingly','/ɪnˈfjʊərieɪtɪŋli/','令人恼怒、火大地',
 '别人偏不把关键点说清，含糊到让你火大，可以叫 infuriatingly vague。它把描述中的强烈不满点出来。',
 'infuriating + -ly；内层 infuriate 去 e 加 -ing，外层修饰令人愤怒的程度或方式。',INFURIATE+[['infuriate → infuriating → infuriatingly','使大怒 → 令人愤怒的 → 令人火大地']],
 'infuriatingly slow 慢得令人火大；infuriatingly vague 含糊得令人恼怒。',
 'infuriatingly calm；infuriatingly elusive。',
 'infuriatingly calm 可以说对方过分镇定，反而让自己更生气；不是说对方正平静地发怒。',
 ('He remained infuriatingly calm throughout the argument.','争论中他始终镇定得让人火大。'),('The answer was infuriatingly vague.','这个答案含糊得令人恼怒。'),sources=S('infuriatingly','infuriate'))
W('intimidator','英 /ɪnˈtɪmɪdeɪtə/；美 /ɪnˈtɪmɪdeɪtər/','恐吓者；靠威势吓住别人的人',
 '有人不靠论据，专靠声势、威胁让别人不敢反对，可以称为 an intimidator。这个名词把使人害怕的动作落实到人。',
 'intimidate 去 e 加 -or → intimidator；-or 是实施者后缀，接在 intimidat- 上，不把整个 -ator 都随意看作同一个根。',INTIMIDATE+[['intimidate + -or → intimidator','实施恐吓、靠威势压人的人']],
 'a workplace intimidator 在工作中靠威势压人的人；a skilled intimidator 善于吓住别人的人。',
 'confront an intimidator；known as an intimidator。',
 'an intimidating task 可以无意让人有压力；an intimidator 通常明确命名有恐吓、压人行为的人，不把手册叫成这个人物名词。',
 ('He had a reputation as an intimidator who shouted down objections.','他以大声压下异议、靠威势吓人而出名。'),('The witness refused to give in to the intimidator.','目击者不肯向那个恐吓者屈服。'),sources=S('intimidator','intimidate'))
W('intimidators','英 /ɪnˈtɪmɪdeɪtəz/；美 /ɪnˈtɪmɪdeɪtərz/','恐吓者；靠威势压人的人〔复数〕',
 '一群人用威胁让别人不敢站出来，这些人是 intimidators；名字说明他们造成畏惧的作用。',
 'intimidate 去 e 加 -or → intimidator，再加复数 -s，读 /z/。',INTIMIDATE+[['intimidate → intimidator → intimidators','从使胆怯的动作，到多个恐吓者']],
 'stand up to intimidators 面对恐吓者不退缩；identify the intimidators 认出恐吓者。',
 'protect witnesses from intimidators；refuse to yield to intimidators。',
 'intimidators 命名靠恐吓压人的实施者，intimidation 命名恐吓行为；多个实施者用复数人名词，不把行为名词直接代作人。',
 ('The volunteers refused to be silenced by the intimidators.','志愿者不肯因那些恐吓者就闭口不言。'),('Witnesses helped identify the intimidators.','目击者帮助认出了那些恐吓者。'),sources=S('intimidators','intimidate'))
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_zgl',ROOTS,WORDS)
 extend_lessons()
