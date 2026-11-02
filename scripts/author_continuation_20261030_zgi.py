"""Teasing, taunting and mockery, with their distinct histories."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
def S(word,base):
 return ['https://en.wiktionary.org/wiki/'+word+'#English','https://www.etymonline.com/word/'+base]
EXISTING_ROOT_ADDITIONS={
 'B4182':dict(words='tease teases teased teasing teasingly teaser teasers'.split(),label='tease：从梳开纤维到逗弄、吊起兴趣',note='古英语 tæsan 有拉扯、梳理纤维义，后来用于反复招惹、逗弄。teaser 由动词加 -er，早期可指梳理纤维者，预告片是后来的用途。'),
 'B3162':dict(words='mock mocks mocked mocking mockingly mocker mockers mockery mockeries'.split(),label='mock：取笑、模仿与模拟；taunt、jeer 作近义比较',note='mock 经法语 mocquer 等，远源未定。mockery 还有法语名词独立借入的历史，不能只按现代短词在前的顺序倒排年代。taunt、jeer 另源，放在这里比较嘲弄方式，不主张它们由 mock 派生。'),
 'C1230':dict(words='deride derides derided deriding derision derisive'.split(),label='deride：带贬低意味地笑某人',note='de- 加拉丁 ridere 笑形成 deridere，再经借入成为 deride。derides、derided、deriding 是英语中的规则变化，不用它们解释独立借入的 derision 全部历史。'),
 'A1760':dict(words='taunt taunts taunted taunting tauntingly jeer jeers jeered jeering jeeringly'.split(),label='taunt、jeer：挖苦、起哄及各自词尾',note='taunt 与 jeer 的更早来源都未完全确定；不能把 taunt 硬接 taut，也不能把 jeer 肯定写成 cheer 的变形。词尾 -ed、-ing、-ly 则可以按现代构词清楚分析。'),
}
TEASE=[['古英语 tæsan → 中古英语 tesen → tease','拉扯、梳开羊毛、麻等纤维'],['反复拉扯 → 招惹、逗弄；后来还可吊起兴趣','这是有记录的用法扩展；是否友善要看对象的感受与场景']]
TAUNT=[['早期英语 tant 等：机锋回应、挖苦','更早来源未定，有法语挑衅、试探动词或以牙还牙短语等不同分析'],['taunt 动词 → taunt 名词及现代变化','用刺人的话挖苦、挑衅；名词指这种话']]
MOCK=[['古法语 mocquer 等 → 中古英语 mokken → mock','嘲弄、愚弄，远源有不同分析'],['嘲讽性的模仿 → 仿效、模拟等用法','形容词 mock 可描述演练、仿制；不必都有嘲笑意图']]
DERIDE=[['拉丁 de- + ridere 笑 → deridere','带贬低意味地笑、嘲弄；不是把笑停止'],['经法语或直接拉丁借入 → 英语 deride','以轻蔑、嘲笑的态度对待']]
JEER=[['早期英语 gyr 等 → jeer','远源未定，荷兰语等比较材料和 cheer 反讽变形说均不能当定论'],['jeer 动词 → 名词及规则变化','带嘲弄、轻蔑地喊叫、发笑；名词指挖苦、起哄的话声']]
W('teases','/ˈtiːzɪz/','逗弄、取笑、吊胃口〔第三人称单数〕；逗弄者〔复数〕',
 '他老拿我的习惯开玩笑，是 he teases me；预告只给一点线索，让人想继续看，也叫 teases。',
 'tease + -s，/z/ 后词尾读 /ɪz/；同形也可作名词 tease 的复数。',TEASE+[['tease + -s → teases','他逗弄、招惹；也可说某物吊起兴趣']],
 'teases someone about something 拿某事逗某人；teases a new release 提前透露一点新作品消息。',
 'teases his sister；teases the audience with a glimpse。',
 'teases 可以是亲近的玩笑，也可能伤人；taunts 更常明确带挖苦、羞辱和挑衅的味道。',
 ('He teases me about my enormous collection of mugs.','他拿我那一大堆马克杯开玩笑。'),('The short clip teases the next episode without revealing the ending.','短片吊起了观众对下一集的兴趣，却没有泄露结局。'),sources=S('teases','tease'))
W('teased','/tiːzd/','逗弄、取笑、吊胃口了；被梳蓬松的',
 '有人拿你的小习惯打趣，是被 teased；头发朝发根倒梳、弄蓬松，也沿用 tease 的梳理纤维那一路。',
 'tease 去 e 加完整 -ed，读 /d/；梳理义与逗弄义共用同一过去形式。',TEASE+[['tease → teased','逗弄、吊兴趣的过去形式；也可指倒梳过的头发']],
 'teased about his accent 被拿口音取笑；teased hair 倒梳蓬松的头发。',
 'gently teased someone；teased a few details of the story。',
 'teased out the answer 中 out 表示逐步理出来，不能理解成把答案嘲笑走；搭配会选择基础动词的不同用法。',
 ('They teased him about arriving with three umbrellas.','他们拿他带了三把伞来这件事打趣。'),('The stylist teased her hair to give it more volume.','造型师把她的头发倒梳，使它看起来更蓬松。'),sources=S('teased','tease'))
W('teasingly','/ˈtiːzɪŋli/','逗弄地；带打趣、吊人胃口的意味地',
 '同样一句“你可真早”，带着笑、故意轻轻逗一下对方，可以说 teasingly。副词告诉你这句话的口气。',
 'teasing + -ly；内层 tease 去 e 加 -ing，外层把逗弄的性质用于说话、动作的方式。',TEASE+[['teasing + -ly → teasingly','以打趣、逗弄或吊起期待的方式']],
 'said teasingly 打趣地说；smiled teasingly 带逗弄意味地笑。',
 'asked teasingly；held the gift teasingly out of reach。',
 'teasingly 常有玩笑感，但是否让人舒服仍要看语境；sarcastically 更明确带讥讽，不能直接互换所有句子。',
 ('“Another cup?” she asked teasingly.','“还要一杯？”她打趣地问。'),('He smiled teasingly but refused to reveal the surprise.','他吊人胃口地笑了笑，却不肯透露那个惊喜。'),sources=S('teasingly','tease'))
W('teasers','英 /ˈtiːzəz/；美 /ˈtiːzərz/','预告片、预告信息；逗弄者；难题〔复数〕',
 '先给一点，够你感兴趣，又没把全貌讲完，这些宣传片段叫 teasers；把人思路勾住的难题也能这样称呼。',
 'tease 去 e 加 -er → teaser，再加 -s。-er 早期可指梳理纤维的人，后来也命名招惹、吊起兴趣的东西。',TEASE+[['tease → teaser → teasers','多个逗弄者、预告或让人动脑的难题']],
 'movie teasers 电影先导预告；release a series of teasers 发布一系列预告；logic teasers 逻辑难题。',
 'short teasers；teasers for the new series。',
 'teasers 通常着重少量信息吊起兴趣，完整 trailers 往往展示更多情节；实际宣传命名仍可能交叠。',
 ('The studio released three short teasers for the new film.','制片公司为新电影发布了三支简短的先导预告。'),('The puzzle page contains a few difficult teasers.','谜题那一页里有几道挺难的题。'),sources=S('teasers','teaser'))
W('taunt','英 /tɔːnt/；美 /tɔnt/','挖苦、嘲弄、挑衅；挖苦的话',
 '故意戳人失败、短处，等着看他难堪或发火，这种带刺的招惹叫 taunt。它通常比朋友间随口逗一逗更敌对。',
 '早期有机锋回应、挖苦义，更早来源未定；法语试探、挑衅动词和以牙还牙短语等都有分析。名词挖苦的话大概由动词发展。',TAUNT,
 'taunt someone about a mistake 拿错误挖苦某人；taunt someone with insults 用辱骂挑衅。',
 'ignore a taunt；taunt the opposing players。',
 'taunt 强调用话刺激、羞辱或挑衅；tease 可以很亲近、无恶意，但也可能让人受伤，不能单靠字词保证玩笑友善。',
 ('They tried to taunt him about his missed shot.','他们试着拿他投失的那一球挖苦他。'),('She ignored the taunt and kept walking.','她没理会那句挖苦，继续往前走。'),sources=S('taunt','taunt'))
W('taunts','英 /tɔːnts/；美 /tɔnts/','挖苦的话〔复数〕；挖苦、挑衅〔第三人称单数〕',
 '一句句冲人短处去的嘲弄，是 taunts；某人惯常这样招惹别人，动词也用 taunts。',
 'taunt + -s，/t/ 后读 /s/，形成 /nts/ 结尾；名词复数和动词三单同形。',TAUNT+[['taunt + -s → taunts','多句嘲弄、挑衅的话；他挖苦、挑衅']],
 'ignore the taunts 不理挖苦声；angry taunts 愤怒的嘲弄；taunts his opponents 挑衅对手。',
 'a stream of taunts；respond to taunts。',
 'chants 是反复喊的口号，不一定带敌意；taunts 已经说明话里带着挖苦、挑衅。',
 ('She refused to respond to the crowd’s taunts.','她不肯回应人群的挖苦。'),('He taunts his opponents whenever he scores.','他每次得分都会挑衅对手。'),sources=S('taunts','taunt'))
W('taunted','英 /ˈtɔːntɪd/；美 /ˈtɔntɪd/','挖苦、嘲弄、挑衅了；被挖苦的',
 '有人把对方不想提的失败当武器，故意说出来刺他一下，过去发生了就是 taunted。',
 'taunt + 完整 -ed；/t/ 后词尾读 /ɪd/，多出一个音节。作被动时说明谁受到嘲弄。',TAUNT+[['taunt + -ed → taunted','过去用言语挖苦、挑衅；或受到这种对待']],
 'taunted about his clothes 因穿着被挖苦；taunted with cruel remarks 被刻薄话嘲弄。',
 'was repeatedly taunted；taunted the goalkeeper。',
 'criticized 可以针对做法提出批评；taunted 更突出拿话刺激人、让人难堪，未必在认真讨论事情。',
 ('The spectators taunted the goalkeeper after the mistake.','失误后，观众对着守门员挖苦起哄。'),('He was taunted about his old shoes.','有人拿他那双旧鞋嘲弄他。'),sources=S('taunted','taunt'))
W('taunting','英 /ˈtɔːntɪŋ/；美 /ˈtɔntɪŋ/','挖苦、挑衅的；正在嘲弄',
 '“你就这点本事？”这类话专门刺人、激人，口气就是 taunting。也可以用来命名这种嘲弄行为。',
 'taunt + -ing；动作形式可作形容词，描述带羞辱、挑衅意味的话语、声音。',TAUNT+[['taunt + -ing → taunting','正在挖苦；也写嘲弄、挑衅的性质或行为']],
 'a taunting voice 挑衅的声音；taunting remarks 挖苦的话；stop the taunting 制止嘲弄。',
 'taunting the players；a taunting smile。',
 'teasing smile 可能只是亲昵地逗一下；taunting smile 更容易被理解为得意地看人出丑，带敌意。',
 ('A taunting voice called out from the back of the room.','房间后面传来一个挖苦的声音。'),('The referee warned the player to stop taunting his opponent.','裁判警告那名球员停止挑衅对手。'),sources=S('taunting','taunt'))
W('tauntingly','英 /ˈtɔːntɪŋli/；美 /ˈtɔntɪŋli/','挖苦地；带挑衅意味地',
 '一句“怎么，不敢了？”若是专门激人、等着看对方丢脸，就是 tauntingly。它把言语背后的刺人态度写出来。',
 'taunting + -ly；内层 taunt + -ing 描述嘲弄、挑衅，外层修饰说话或动作方式。',TAUNT+[['taunting + -ly → tauntingly','以挖苦、刺激对方的方式']],
 'said tauntingly 挖苦地说；laughed tauntingly 挑衅地笑。',
 'asked tauntingly；smiled tauntingly at his rival。',
 'tauntingly 针对的是刺激、羞辱别人；confidently 只说自信，不一定拿别人当靶子。',
 ('“Is that all?” he asked tauntingly.','“就这点本事？”他挑衅地问。'),('She smiled tauntingly at the rival who had doubted her.','她朝那个曾怀疑她的对手挑衅地一笑。'),sources=S('tauntingly','taunt'))
W('mocks','英 /mɒks/；美 /mɑks/','嘲笑、模仿取笑〔第三人称单数〕；模拟考试〔复数，英式口语〕',
 '故意学别人的腔调、动作来取笑，是 mocks；英国学生说 mocks，也常是在说正式考试前的模拟考。后者接 mock“模拟的”这一用法。',
 'mock + -s，/k/ 后读 /s/；动词三单与名词复数同形。模拟考名词是 mock examination 等的省略，不是考试在嘲笑学生。',MOCK+[['mock + -s → mocks','他取笑；模拟考试等名词的复数']],
 'mocks someone’s accent 模仿、取笑口音；sit your mocks 参加模拟考；revise for the mocks 复习准备模拟考。',
 'mocks the proposal；results from the mocks。',
 'mock exam 是为练习而模拟的考试，不是假成绩骗局；mock 可以从嘲讽模仿发展到中性的演练。',
 ('He mocks the villain’s dramatic voice.','他模仿反派夸张的腔调来逗笑。'),('Our mocks start next Monday.','我们的模拟考试下周一开始。'),sources=S('mocks','mock'))
W('mocked','英 /mɒkt/；美 /mɑkt/','嘲笑、模仿取笑了；被嘲弄的',
 '别人把你的想法当笑话，或夸张模仿你的动作让你出丑，过去发生了就用 mocked。',
 'mock + 完整 -ed；/k/ 后词尾读 /t/。基础词借自法语嘲弄动词，更早来路未定。',MOCK+[['mock + -ed → mocked','过去嘲弄；或受到嘲弄']],
 'mocked for his accent 因口音被嘲笑；mocked the idea 嘲笑那个想法。',
 'openly mocked；felt mocked by the remark。',
 'mimicked 说明模仿，不一定有轻蔑；mocked someone 更常把取笑、看不起一起带进去。',
 ('They mocked his suggestion before they understood it.','他们还没弄懂他的建议，就先嘲笑起来。'),('She felt mocked when he repeated her words in a silly voice.','他用滑稽的声音重复她的话，让她觉得受到了嘲弄。'),sources=S('mocked','mock'))
W('mocking','英 /ˈmɒkɪŋ/；美 /ˈmɑkɪŋ/','嘲弄、讥笑的；正在取笑、模仿',
 '笑声里带着“这也配”的轻蔑，叫 mocking laughter；不是所有笑都 mocking，关键是把对方放在被取笑的位置。',
 'mock + -ing；动词的动作形式也作形容词，描述嘲弄、模仿的性质。',MOCK+[['mock + -ing → mocking','正在取笑；也形容带讥笑意味']],
 'a mocking tone 嘲弄的口气；mocking laughter 讥笑声；mocking his gestures 模仿动作来取笑。',
 'a mocking smile；stop mocking me。',
 'a mock interview 是模拟面试，a mocking interviewer 却是嘲弄人的面试官；mock 的中性模拟义不能照搬到 mocking 的常用评价义。',
 ('There was a mocking note in his voice.','他的声音里带着嘲弄。'),('She asked them to stop mocking her pronunciation.','她让他们别再取笑她的发音。'),sources=S('mocking','mock'))
W('mockingly','英 /ˈmɒkɪŋli/；美 /ˈmɑkɪŋli/','嘲弄地；带讥笑意味地',
 '同样是重复别人的一句话，拖长腔调、等着看人难堪，就是 repeating it mockingly。它描写动作中的嘲笑态度。',
 'mocking + 副词 -ly；内层 mock + -ing，外层描述说、笑、模仿时的方式。',MOCK+[['mocking + -ly → mockingly','带着嘲笑、轻蔑的态度做事']],
 'laughed mockingly 讥笑；repeated mockingly 嘲弄地重复；bowed mockingly 故意作揖来取笑。',
 'smiled mockingly；spoke mockingly of the plan。',
 'jokingly 可以只是开玩笑，mockingly 更突出把别人或某事当笑话的态度。',
 ('He repeated the excuse mockingly.','他带着嘲弄重复了一遍那个借口。'),('“What a genius,” she said mockingly.','“可真是个天才。”她讥讽地说。'),sources=S('mockingly','mock'))
W('mocker','英 /ˈmɒkə/；美 /ˈmɑkər/','嘲弄者；模仿取笑别人的人',
 '不是只说“有人笑了”，而是把那种拿别人当笑话的人点出来：a mocker。',
 'mock + -er，-er 命名做这种事的人；基础词接法语 mocquer 等，更早来源未定。',MOCK+[['mock + -er → mocker','实施嘲弄、模仿取笑的人']],
 'a cruel mocker 刻薄的嘲弄者；ignore the mocker 不理那个取笑人的人。',
 'a habitual mocker；turn from mocker to supporter。',
 'a critic 可以提出认真、具体的批评；a mocker 强调拿人取笑，不表示他已经给出有用意见。',
 ('The loudest mocker had never tried the task himself.','笑得最起劲的那个人自己从来没试过这项任务。'),('She refused to let one mocker silence her.','她不肯让一个嘲弄她的人把她吓得不敢开口。'),sources=S('mocker','mock'))
W('mockers','英 /ˈmɒkəz/；美 /ˈmɑkərz/','嘲弄者〔复数〕',
 '一群人围着取笑别人的努力，可以称为 mockers。-er 先把动作落实到做事的人，-s 再说明不止一个。',
 'mock + -er → mocker，再加复数 -s，读 /z/；这里讲普通的嘲弄者复数。',MOCK+[['mock → mocker → mockers','从嘲弄动作到多个嘲弄者']],
 'ignore the mockers 不理嘲弄者；prove the mockers wrong 用结果证明那些取笑自己的人错了。',
 'a crowd of mockers；former mockers became supporters。',
 'mockers 是取笑人的人；supporters 是支持者。是否同一群人后来改变态度，要看上下文，而不是词形自带历史。',
 ('The mockers fell silent when the experiment worked.','实验成功后，那些嘲弄者不说话了。'),('She kept practising despite the mockers.','尽管有人取笑，她还是一直练习。'),sources=S('mockers','mock'))
W('mockeries','英 /ˈmɒkəriz/；美 /ˈmɑkəriz/','嘲弄行为；有名无实、可笑的仿制品或做法〔复数〕',
 '东西挂着“公正”的招牌，做出来却把公正变成笑话；这些空有样子、反而损害原意的做法可以叫 mockeries。',
 'mockery 变 y 为 i 加 -es。现代可联系 mock + -ery 理解，但 mockery 有法语 mocquerie 等名词独立借入的历史，并非一定晚于英语 mock 才造出。',
 [['法语 mocquerie 等 → 英语 mockery','嘲弄、作假、虚有其表等意义，属于 mock 的借词词族'],['mockery → mockeries','多个嘲弄行为，或多个空有形式、使原意成笑话的东西']],
 'mockeries of justice 对公正的践踏、把公正当笑话的做法；crude mockeries 粗劣可笑的仿制。',
 'empty mockeries of reform；mockeries of the original。',
 'copies 中性说复制品，mockeries 通常强烈贬低：不仅不像样，还让本来宣称的价值变得可笑。抽象嘲弄一般仍用不可数 mockery。',
 ('The sham hearings were mockeries of justice.','那些走过场的听证会简直把公正当成了笑话。'),('The cheap decorations were crude mockeries of the originals.','这些廉价装饰品是原作粗劣得可笑的仿制品。'),sources=S('mockeries','mockery'))
W('derides','/dɪˈraɪdz/','嘲弄、轻蔑地取笑〔第三人称单数〕',
 '把别人的建议当成不值一提的笑话，口气里带“这也值得认真？”的轻蔑，是 derides。它比普通 laugh at 更正式，也更明确带贬低。',
 'deride + -s，读 /z/；基础词接拉丁 de- + ridere 笑，不把 de- 机械译成停止。',DERIDE+[['deride + -s → derides','他以轻蔑的态度嘲弄']],
 'derides the idea 嘲笑那个想法；derides something as pointless 嘲讽某事毫无意义。',
 'openly derides；derides anyone who disagrees。',
 'criticizes 可以理性指出问题；derides 强调轻蔑地笑、挖苦，未必提供论据。',
 ('He derides any proposal that comes from a newcomer.','只要是新人提出的建议，他都会嘲弄。'),('The article derides the plan as an expensive fantasy.','那篇文章嘲讽这个计划是一场耗资巨大的幻想。'),sources=S('derides','deride'))
W('derided','/dɪˈraɪdɪd/','嘲弄、讥笑了；被嘲弄的',
 '一开始所有人都拿这个想法当笑话，说它根本不值得试，那个想法就是 widely derided。',
 'deride 去 e 加完整 -ed；/d/ 后读 /ɪd/。过去形式也常用于被动，表示受轻蔑嘲弄。',DERIDE+[['deride → derided','过去嘲弄；或描述被人看轻、取笑']],
 'widely derided 被广泛嘲讽；derided as naïve 被讥笑为天真。',
 'once derided 曾被嘲笑；derided by critics 遭批评者嘲讽。',
 'derided 是被取笑、轻视，disproved 才是被证据证伪；一个想法遭嘲笑不等于已经证明它错了。',
 ('The idea was derided as impossible when it first appeared.','这个想法刚提出时，被人讥笑为不可能实现。'),('She derided the excuse as absurd.','她嘲讽这个借口荒唐可笑。'),sources=S('derided','deride'))
W('deriding','/dɪˈraɪdɪŋ/','正在嘲弄、轻蔑地取笑',
 '别人还没把话说完，他就带着轻蔑笑起来；用 deriding 写的是这种正在把人或想法当笑话的行为。',
 'deride 去 e 加 -ing；规则动作形式，承拉丁 deridere 的轻蔑取笑义。',DERIDE+[['deride → deriding','正在以嘲弄态度对待；也可名词化指这种行为']],
 'deriding the proposal 嘲弄建议；deriding someone for a mistake 因一个错误嘲讽某人。',
 'stop deriding；rather than deriding the effort。',
 'deriding 不是 disagreeing 的必然后果；可以持不同意见而认真回应，不带轻蔑。',
 ('They spent the meeting deriding each other’s ideas.','他们把开会的时间都花在互相嘲弄想法上。'),('Instead of deriding the attempt, explain how it could improve.','别光嘲笑这次尝试，说说它可以怎样改进。'),sources=S('deriding','deride'))
W('jeer','英 /dʒɪə/；美 /dʒɪr/','嘲笑、挖苦、起哄；嘲弄的话声',
 '有人一上场，观众就带着看不起的口气喊话、发笑，这叫 jeer。它很适合写有声音的嘲弄，尤其一群人起哄。',
 '早期英语 gyr 等到 jeer，远源未定；荷兰语大笑、嘲弄等材料是分析之一，不能把它确定写成 cheer 的反义变形。名词由动词发展。',JEER,
 'jeer at someone 对某人嘲笑起哄；a loud jeer 一声响亮的嘲弄。',
 'jeer from the crowd；ignore the jeer。',
 'cheer 是欢呼、鼓劲，jeer 是嘲弄起哄；这个对比方便记态度，不能因此认定两词有确定的派生关系。',
 ('Some spectators began to jeer at the referee.','一些观众开始对裁判挖苦起哄。'),('A loud jeer came from the back of the crowd.','人群后面传来一声响亮的嘲弄。'),sources=S('jeer','jeer'))
W('jeers','英 /dʒɪəz/；美 /dʒɪrz/','嘲弄、起哄声〔复数〕；嘲笑起哄〔第三人称单数〕',
 '台下不是鼓掌，而是一阵阵挖苦、讥笑的声音，这些是 jeers。与 cheers 放在同一句里时，一个是喝倒彩，一个是欢呼。',
 'jeer + -s，读 /z/；名词复数和动词三单同形，基础词远源未定。',JEER+[['jeer + -s → jeers','多声嘲弄；他嘲笑起哄']],
 'cheers and jeers 欢呼与嘲弄声；a chorus of jeers 一片起哄声。',
 'jeers from the crowd；jeers at every mistake。',
 'boos 常直接指“嘘”的喝倒彩声，jeers 可以含挖苦话、讥笑和其他嘲弄声，范围稍广。',
 ('His answer was met with jeers from the crowd.','他的回答招来人群的阵阵嘲弄。'),('One spectator jeers whenever the opposing team scores.','对方球队一得分，就有个观众挖苦起哄。'),sources=S('jeers','jeer'))
W('jeered','英 /dʒɪəd/；美 /dʒɪrd/','嘲笑、起哄、挖苦了',
 '人群对着某人喊出嘲弄的话，过去发生了就是 jeered；通常写出了不友好的声音反应。',
 'jeer + 完整 -ed，词尾读 /d/；不另造一个带贬低义的 jeer 后缀。',JEER+[['jeer + -ed → jeered','过去带嘲弄意味地喊、笑']],
 'jeered at the speaker 对演讲者起哄；jeered by spectators 被观众嘲弄。',
 'openly jeered；jeered from the sidelines。',
 'jeered 和 cheered 拼写接近，反应方向却相反；前者嘲弄，后者通常欢呼或鼓励，读句子时注意主场、客场等背景。',
 ('The crowd jeered when the player missed an easy shot.','球员错失一个轻松的投篮机会，人群挖苦起哄。'),('They jeered at his costume, but he kept smiling.','他们嘲笑他的装扮，他却仍然笑着。'),sources=S('jeered','jeer'))
W('jeering','英 /ˈdʒɪərɪŋ/；美 /ˈdʒɪrɪŋ/','嘲弄、起哄；带嘲弄意味的',
 '一阵起哄声裹着挖苦、讥笑传过来，是 jeering；这个词既能写行为，也能形容声音、人群。',
 'jeer + -ing；动作形式作名词描述嘲弄行为，作形容词描述带嘲弄意味。',JEER+[['jeer + -ing → jeering','正在嘲弄；嘲弄行为或声音性质']],
 'a jeering crowd 起哄的人群；loud jeering 响亮的嘲弄声；jeering at the speaker 对演讲者起哄。',
 'a jeering voice；stop the jeering。',
 'jeering crowd 带敌对嘲弄，noisy crowd 只说吵；人群吵闹也可能是在热烈欢迎。',
 ('She walked past the jeering crowd without looking down.','她走过起哄的人群，没有低下头。'),('The jeering stopped when he began to sing.','他开始唱歌时，起哄声停了。'),sources=S('jeering','jeer'))
W('jeeringly','英 /ˈdʒɪərɪŋli/；美 /ˈdʒɪrɪŋli/','嘲弄地；带挖苦起哄的口气地',
 '一句话特意朝别人喊过去，带着看笑话的口气，叫 jeeringly。比一般 said 多写出声音里的轻蔑。',
 'jeering + -ly；内层 jeer + -ing，外层把嘲弄性质用于说话、笑的方式。',JEER+[['jeering + -ly → jeeringly','以带挖苦、起哄的态度发声']],
 'shouted jeeringly 挖苦起哄地喊；laughed jeeringly 嘲弄地笑。',
 'called out jeeringly；spoke jeeringly。',
 'jeeringly 常用于喊话、讥笑的口气；mockingly 范围更广，还可以修饰故意模仿的动作，例如 mockingly bowed。',
 ('“Try again!” someone shouted jeeringly from the back.','“再试一次啊！”后面有人挖苦起哄地喊。'),('They laughed jeeringly as he searched for an answer.','他苦苦想答案时，他们发出嘲弄的笑声。'),sources=S('jeeringly','jeer'))
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_zgi',ROOTS,WORDS)
 extend_lessons()
