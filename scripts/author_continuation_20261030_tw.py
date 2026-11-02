"""Common past forms: success, sending, change, leading and keeping."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'B2541':dict(words=['win','won'],label='win 到 won：过去赢得与已经赢得',note='win → won → won；动词 won 读 /wʌn/，与 one 常同音；货币名 won 的读音和来源另记。'),
 'B2495':dict(words=['send','sent'],label='发送、派遣的过去形式 sent',note='send → sent → sent；词尾 t 涉及较早过去词尾的变化，不是把 send 中的 d 简单替换成一个词根。'),
 'B2841':dict(words=['become','became'],label='become 到 became：进入新状态',note='become → became → become；与 come、came 的相应变位连着记，过去分词不是 became。'),
 'B2816':dict(words=['lead','led'],label='lead 与 led：读音也发生变化',note='引导动词 lead /liːd/ → led /led/ → led；金属名 lead /led/ 另有来源。'),
 'B2895':dict(words=['meet','met'],label='meet 到 met：相遇与满足条件',note='meet → met → met；meet 的长元音与 met 的短元音应一起辨认。'),
 'B2755':dict(words=['begin','began','begun'],label='开始的三种形式 begin、began、begun',note='begin → began → begun，分别读 /bɪˈɡɪn/、/bɪˈɡæn/、/bɪˈɡʌn/；has begun 与 began 的语法位置不同。'),
 'B2834':dict(words=['build','built'],label='build 与 built：建成与体格',note='build → built → built；built 可直接作分词，也可在体格描写中作形容词。'),
 'B2583':dict(words=['write','wrote','written'],label='write、wrote、written 的三式连读',note='wrote 是过去式，written 是过去分词；词形接较早写、刻痕动词的强变位传统。'),
 'B2882':dict(words=['keep','kept'],label='keep 与 kept：留住、守住、一直做',note='keep → kept → kept，元音由 /iː/ 变 /e/；kept 承接旧的带过去词尾形式。'),
}
W('won','动词 /wʌn/；货币名：英 /wɒn/、美 /wɑːn/','赢得了、获胜了〔win 的过去式、过去分词〕；韩元等货币名〔另源〕',
 '努力争取到比赛、支持或机会，过去可以说 won。遇到价格中的 won，则在说货币，读音和来源要换一支。',
 '动词 won 延续 win 的旧日耳曼变位，所属词族较早有努力、争取义。货币名另借自韩语 won，联系汉字圓的相关货币名称。',
 [['win 的努力争取词族与旧过去形式','赢得、获胜的过去与完成表达'],['韩语货币名 won → 英语名词','韩元等，另源且常另读']],
 'won the match 赢了比赛；won a prize 获奖；won their trust 赢得信任；five thousand won 五千韩元。',
 'has won several awards；won by a narrow margin。','动词 won 与 one 在常见读音中同音，但来源、词性不同。价格语境的 won 通常取货币名，不按 win 的变位解释。',
 ('Our team won the final match.','我们队赢了决赛。'),('She has won the trust of her colleagues.','她赢得了同事们的信任。'),('The notebook cost five thousand won.','那本笔记本售价五千韩元。'),sources=['https://www.etymonline.com/word/won','https://en.wiktionary.org/wiki/won#English'])
W('sent','/sent/','发送了、派出了、送到了；send 的过去式、过去分词',
 '把人、物、消息送出去的动作已经发生，常用 sent。A parcel was sent 是包裹被寄出，不一定已经收到。',
 'send 承接古英语 sendan 等使人或物前往的词族；sent 由较早带过去词尾的形式变化而来，词尾最终固定为 t。',
 [['古英语 sendan 等与旧过去形式','使人、物、消息前往某处'],['现代 send → sent → sent','发送、派遣的过去与过去分词']],
 'sent an email 发了邮件；sent for help 派人求助；was sent home 被送回家；sent to the wrong address 寄错地址。',
 'have sent the message；sent someone a letter。','sent 说送出的动作，received 说收到的动作；sent 不单独保证对方收到。send 后可接双宾语，sent her a message 很自然。',
 ('I sent her a message this morning.','我今天早上给她发了条消息。'),('The package was sent to the wrong address.','包裹被寄到了错误的地址。'),sources=['https://www.etymonline.com/word/send','https://www.etymonline.com/word/went','https://en.wiktionary.org/wiki/sent#English'])
W('became','/bɪˈkeɪm/','变成了、开始处于某种状态；become 的过去式',
 '事情跨过一个变化点：从不安静到安静，从学生到教师。became 描写过去进入了什么新状态。',
 'become 与较早 be-、come 的词族相连；became 跟随 come、came 的变位关系，用于整个复合动词的过去式。',
 [['较早 become 与 come 词族','来到、进入某种状态'],['现代 become → became → become','过去 became；过去分词 become']],
 'became quiet 安静下来；became a teacher 成为教师；became clear 变得清楚；became interested 产生兴趣。后面常接形容词或名词。',
 'became popular；became aware of something。','was 说过去处于某状态，became 更强调进入该状态的变化。She was a teacher 和 She became a teacher 关注点不同。',
 ('The room became quiet when she entered.','她进来时，房间安静下来。'),('He became a teacher after university.','大学毕业后，他成了一名教师。'),sources=['https://www.etymonline.com/word/came','https://en.wiktionary.org/wiki/became#English'])
W('led','/led/','带领了、引导了；导致了；lead 的过去式、过去分词',
 '过去带路、带队，或一件事把结果引出来，用 led。led to a change 把原因和变化连接起来。',
 '引导动词 lead 接古英语 lædan 使同行、领路等；较早过去形式经过变化形成现代 led，过去分词也采用 led。',
 [['古英语 lædan 与相应旧过去形式','使人同行、带领'],['现代 lead /liːd/ → led /led/ → led','带领、引致的过去与完成形式']],
 'led the team 带领了团队；led to a discovery 导致了发现；was led into the room 被领进房间。',
 'has led several projects；led by a guide。','引导的原形 lead 读 /liːd/，过去式 led 读 /led/。金属铅 lead 也读 /led/，却是另一来源的名词，不是引导动词的过去拼写。',
 ('The guide led us through the forest.','向导带着我们穿过森林。'),('The discussion led to a new idea.','讨论引出了一个新想法。'),sources=['https://www.etymonline.com/word/lead','https://en.wiktionary.org/wiki/led#English'])
W('met','/met/','见过、遇到了、满足了；meet 的过去式、过去分词',
 '人和人碰面，条件和要求对上，都可以从 meet 变为 met。句子里是谁遇到谁、什么达到了什么，要一起看。',
 'meet 经中古英语承接古英语 metan 等相遇词族；met 是其较早过去形式进一步变化、缩短后的现代形式。',
 [['较早英语 meet 词族及过去形式','相遇、碰到'],['现代 meet → met → met','见面、遇到；满足、符合的过去与完成表达']],
 'met a friend 遇见朋友；have met before 以前见过；met the requirements 满足了要求；met with approval 获得赞同。',
 'met at the station；the deadline was met。','met 不只表示第一次认识。We met yesterday 可能是昨天见面；meet the requirements 的 met 则说条件达到了。',
 ('We met at the station yesterday.','我们昨天在车站见了面。'),('The design met all the requirements.','这个设计满足了全部要求。'),sources=['https://www.etymonline.com/word/meet','https://en.wiktionary.org/wiki/met#English'])
W('began','/bɪˈɡæn/','开始了；begin 的过去式',
 '把过去的一个起点点出来：雨开始下、音乐开始响、人开始做事。began 说那一步开始发生了。',
 'begin 接古英语 beginnan 等开始词族，延续较早以词干元音变化标记过去的体系；began 是现代一般过去形式。',
 [['旧英语 begin 词族与相应变位','开始、着手及其过去表达'],['现代 begin → began → begun','一般过去 began；过去分词 begun']],
 'began to rain 开始下雨；began working 开始工作；the meeting began 会议开始了。begin 后可接不定式或 -ing 形式。',
 'began the journey；began with a question。','一般过去用 began；has、have、had 后用过去分词 begun。不要把 has began 当标准搭配。',
 ('It began to rain just after lunch.','午饭后不久开始下雨了。'),('The teacher began the lesson with a question.','老师用一个问题开始了这节课。'),sources=['https://www.etymonline.com/word/began','https://en.wiktionary.org/wiki/began#English'])
W('begun','/bɪˈɡʌn/','已经开始、被开始；begin 的过去分词',
 'has begun 把开始接到已经发生这层结构里。begun 最常与 has、have、had 连着出现。',
 '接 begin 的旧强变位分词材料，现代保留 -n 结尾，与原形 begin、过去式 began 对应。',
 [['较早 begin 词族的分词形式','开始这一动作的分词材料'],['现代 begin → began → begun','begun 用于完成结构等，不独立代替一般过去']],
 'has begun 已经开始；had begun 过去某时已经开始；have just begun 刚刚开始；the work has begun 工作已经开始。',
 'the show has begun；had already begun。','began /bɪˈɡæn/ 与 begun /bɪˈɡʌn/ 元音不同，语法位置也不同：The show began；The show has begun。',
 ('The performance has already begun.','演出已经开始了。'),('By the time we arrived, the meeting had begun.','我们到达时，会议已经开始了。'),sources=['https://www.etymonline.com/word/began','https://en.wiktionary.org/wiki/begun#English'])
W('built','/bɪlt/','建造了、被建造的；体格……的；build 的过去式、过去分词',
 '桥、房子被造起来是 built；a strongly built person 则把人的身体当成构造来描写，意思是体格健壮。',
 'build 接古英语 byldan 建屋等，较早带过去词尾的形式后来形成 built；-t 与旧过去尾变化有关，另由分词扩展出体格形容词。',
 [['较早 build 词族与过去词尾变化','建造、构成的过去形式'],['现代 build → built → built','建成、被建造；体格构造如何']],
 'built a house 盖了房子；was built in 1900 建于 1900 年；strongly built 体格健壮的；built on experience 建立在经验之上的。',
 'built from stone；built a reputation。','build 的 d 与 built 的 t 要听清，但不能把所有以 d 结尾的动词都照此变。was built 是被动表达，具体结构由整句判断。',
 ('The bridge was built from local stone.','这座桥用当地石材建成。'),('They built a good relationship over the years.','多年来，他们建立了良好的关系。'),('He is strongly built.','他体格健壮。'),sources=['https://www.etymonline.com/word/built','https://en.wiktionary.org/wiki/built#English'])
W('wrote','英 /rəʊt/；美 /roʊt/','写了、创作了；write 的过去式',
 '过去写下一封信、一句代码、一本书，都可以用 wrote。写什么、为谁写，通过宾语和搭配说明。',
 'write 接古英语 writan 刻痕、书写，过去式有 wrat 等；经中古英语和后续语音变化成为 wrote，保留旧强变位的不同元音。',
 [['古英语 writan、wrat 等','刻写、书写的原形与过去形式'],['现代 write → wrote → written','一般过去 wrote；过去分词 written']],
 'wrote a letter 写了封信；wrote a novel 创作了小说；wrote to someone 给某人写信；wrote down the address 记下了地址。',
 'wrote a reply；wrote the first chapter。','wrote 用一般过去；written 常跟 have、has 或被动结构：She wrote it；She has written it；It was written yesterday。',
 ('I wrote her a letter last week.','我上周给她写了一封信。'),('He wrote down the address before leaving.','离开前，他记下了地址。'),sources=['https://www.etymonline.com/word/write','https://en.wiktionary.org/wiki/wrote#English'])
W('kept','/kept/','保留了、遵守了、保持着；keep 的过去式、过去分词',
 '东西留住了，承诺守住了，某种动作一直持续着，都可在过去用 kept。',
 '接中古英语 kept、kepte 与古英语 cepte 等旧过去形式。keep 的旧词尾变化和元音变化共同留下现代 kept，并非所有不规则动词都属于同一种历史。',
 [['古英语 cepan、cepte → 中古英语相关形式','守住、保持及其过去表达'],['现代 keep → kept → kept','过去、过去分词同形；长短元音不同']],
 'kept the receipt 留着收据；kept a promise 遵守诺言；kept quiet 保持安静；kept asking 一直问。',
 'kept the door open；kept in touch。','kept doing 强调过去持续、反复做；kept something 常说留住某物。keep 的 /iː/ 到 kept 变为 /e/，两种读音一起记。',
 ('She kept her promise.','她遵守了诺言。'),('He kept asking the same question.','他一直在问同一个问题。'),sources=['https://www.etymonline.com/word/kept','https://en.wiktionary.org/wiki/kept#English'])
def extend_lessons():
    extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
    save('continuation_20261030_tw',ROOTS,WORDS)
    extend_lessons()
