"""Fret homonyms, worry and brooding, kept on separate histories."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
def S(word,base):
 return ['https://en.wiktionary.org/wiki/'+word+'#English','https://www.etymonline.com/word/'+base]
EXISTING_ROOT_ADDITIONS={
 'B2854':dict(words='eat fret frets fretted fretting fretful fretfully fretfulness'.split(),label='fret：吃尽、磨耗到焦虑；同形品、纹样另源',note='焦虑动词承古英语 fretan 吞吃，与 eat 的吃材料同族，磨耗义也可能受法语摩擦词影响。吉他品、交织装饰纹样是另源 fret，列同形说明时不把它们接进吞吃历史。'),
 'A1782':dict(words='fret fretless'.split(),label='fretless：乐器没有品',note='fretless 现代常是乐器 fret 品加 -less，历史上另有无烦恼的旧义；两个 fret 不同来源，不能从不焦虑推出无品贝司。'),
 'B2504':dict(words='work fretwork'.split(),label='fretwork：交织纹样、镂空雕饰工艺',note='fretwork 接装饰纹样的 fret 加 work，不是焦虑动词加工作，也不是吉他品的同一来源；work 命名工艺及做成的制品。'),
 'B4146':dict(words='worry worrying worryingly worrier worriers worrisome worrisomely worried unworried'.split(),label='worry：从旧揪扼材料到担心；两种令人担忧副词',note='现代担忧来自旧烦扰、心理困扰材料；worryingly 与 worrisomely 基底分别是 worrying、worrisome，worrier 旧义与现代易担心者义也要分开年代。'),
 'B2831':dict(words='breed brood brooding broodingly brooder brooders'.split(),label='brood：守着孵育，到把心事久久留着',note='brood 和 breed 接孵育、温热的旧词族；broodingly 写忧思、沉郁的样子，brooder 还可指保温育雏箱。'),
 'A1699':dict(words='mope mopey'.split(),label='mopey：闷闷不乐、提不起精神',note='mopey 是 mope 加 -y，保留 e；mope 远源未定，只能说有低地德语、北欧等相关分析，不能断言来自拖把。'),
}
FRET=[['古英语 fretan：吞吃、吃尽 → 焦虑一支 fret','包含与 eat 同族的吃材料；磨耗义也可能受法语摩擦词影响'],['啃耗、磨耗 → 心绪被折磨 → 自己焦虑','像担忧啃着人，有真实词义联系，但具体比喻可经吃或磨的不同路径'],['另源 fret：交织纹样；乐器指板上的品','分别接法语装饰、圈箍等材料的不同分析，不能全部归进吞吃义']]
FRETFUL=[['焦虑 fret 动词及相关名词','接吞吃、磨耗到烦扰的旧材料'],['fret 名词 + -ful → fretful','旧烦扰性质；现代形容焦躁、烦闷、不安稳']]
WORRY=[['古英语 wyrgan；中古英语咬扼、撕扯等材料','后来有反复烦扰、困扰的抽象用法'],['现代 worry：使担忧、自己担心','学习可想象心事揪住人，现代不要求字面暴力动作']]
BROOD=[['古英语 brod → brood 名词','同窝幼鸟等，与 breed 的孵育、温热材料同族'],['brood 名词 → 孵育动词 → 久久忧思','像守着蛋孵，不断把愤怒、担忧留在心里；不是正常思考一律带消极']]
MOPE=[['早期 mope 的无精神、闷闷不乐材料','远源未定，有低地德语、北欧相关比较分析'],['mope + -y → mopey','把闷着、没精神的表现变成形容词，保留 e']]
W('fret','/fret/','焦虑、烦躁；磨耗；乐器上的品；交织纹样',
 '焦虑像一点点啃掉心情，叫 fret；吉他指板上一道道定位音高的金属条也叫 frets，却属于另一来源，学习时把同形词分开。',
 '焦虑动词承古英语 fretan 吞吃，与 eat 同族；磨耗可能受法语摩擦词影响。乐器品与装饰纹样 fret 分别有法语圈箍、交织材料等来路，不合成一根。',FRET,
 'fret about the future 为未来焦虑；don’t fret 别烦心；the fifth fret 吉他第五品。',
 'fret over a mistake；press behind a fret。',
 'fret 常写心里反复绕、焦躁，plan 是主动安排下一步；fret about tomorrow 不等于已经为明天作好准备。',
 ('Don’t fret about a mistake you can still fix.','还能补救的错误，别一直为它烦心。'),('Place your finger just behind the fifth fret.','把手指放在第五品后面一点的位置。'),sources=S('fret','fret'))
W('frets','/frets/','焦虑、烦躁〔第三人称单数〕；乐器品、装饰纹样〔复数〕',
 '一个人老为细节操心，是 he frets；吉他上许多道品条，是 frets。同形的 s 不说明它们共享焦虑词源。',
 'fret + -s，/t/ 后读 /s/；焦虑动词三单、另源乐器名词复数同形。',FRET+[['fret + -s → frets','他不断烦心；多个乐器品、装饰纹样']],
 'frets over details 为细节焦虑；guitar frets 吉他品；worn frets 磨损的品条。',
 'frets about the weather；check the frets。',
 'frets over the guitar 说人因为吉他烦心，frets on the guitar 则常是在说吉他上的品条；介词和句法帮你判断是哪一路。',
 ('He frets over details that nobody else notices.','他总为别人根本没注意的细节烦心。'),('The guitar’s frets were worn smooth.','吉他上的品条磨得很光滑了。'),sources=S('frets','fret'))
W('fretted','/ˈfretɪd/','焦虑、烦躁了；磨耗了；有品的；有交织装饰的',
 '整晚担忧是 fretted 的动词用法；a fretted instrument 则是带品的弦乐器。前者是情绪，后者说结构，来源分开。',
 '焦虑 fret 双写 t 加完整 -ed，/t/ 后读 /ɪd/；另源 fret 品也可加表示配备特征的 -ed，指有品。',FRET+[['fret → fretted','焦虑动词的过去式；另源名词可接 -ed 形成有品等性质']],
 'fretted all night 整晚焦虑；a fretted bass 有品贝司；fretted woodwork 有镂空交织装饰的木作。',
 'fretted about the result；a fretted instrument。',
 'fretted instrument 的 -ed 不一定表示已经被做了焦虑动作；英语 -ed 也能接名词，表示具有某种特征。',
 ('She fretted all night about the result.','她整晚都为结果焦虑。'),('He switched from a fretted bass to a fretless one.','他从有品贝司改用了无品贝司。'),sources=S('fretted','fret'))
W('fretting','/ˈfretɪŋ/','焦虑、烦躁；磨耗；按弦定音等〔依词源分支〕',
 '同一个问题翻来覆去想，越想越不安，是 fretting；乐器上的按弦、品相关活动和材料摩擦磨耗，也能见到这个词。',
 'fret 双写 t 加 -ing。焦虑、磨耗一支接旧吞吃材料与可能的摩擦影响；乐器品的一支另源，不能把三种场景都当焦虑。',FRET+[['fret → fretting','动作、过程名词；具体是哪一支，要看宾语、场景']],
 'fretting over the details 为细节焦虑；fretting about tomorrow 为明天烦心；fretting wear 接触面微动磨损，工程语境。',
 'stop fretting；all this fretting。',
 'fretting 常带焦虑在原地打转的感觉，thinking 只是中性思考；但工程里的 fretting 说材料磨耗，不能译成零件在担忧。',
 ('Stop fretting over things you cannot control.','别再为你控制不了的事反复烦心。'),('All this fretting is keeping me awake.','这样反复担忧，弄得我睡不着。'),sources=S('fretting','fret'))
W('fretful','/ˈfretfəl/','烦躁不安的；焦虑、难以安稳的',
 '宝宝困了却睡不踏实，一会儿动一会儿哼；大人心事重重，也安静不下来，都可以叫 fretful。',
 '焦虑、烦扰一支的 fret 名词 + -ful；表示带着这类烦躁性质。这里只接焦虑词族，不接乐器品名词。',FRETFUL,
 'a fretful baby 烦躁不安的宝宝；fretful sleep 不安稳的睡眠。',
 'feel fretful；a fretful night。',
 'fretful 着重烦躁、难安稳，thoughtful 可以是平静思考或体贴；不是想得多就必然 fretful。',
 ('The baby became fretful before bedtime.','睡前，宝宝变得烦躁不安。'),('She had a fretful night before the interview.','面试前一晚，她焦虑得睡不安稳。'),sources=S('fretful','fretful'))
W('fretfully','/ˈfretfəli/','烦躁不安地；焦虑地',
 '人躺下又翻身，心里还在纠结，或者带着不安一遍遍问进展，可以用 fretfully 写动作的样子。',
 'fretful + -ly；-ful 写烦躁性质，-ly 再写这种性质如何体现在动作里。',FRETFUL+[['fretful + -ly → fretfully','带着烦躁、不安做出动作']],
 'slept fretfully 睡得不安稳；asked fretfully 焦虑地问。',
 'tossed fretfully；waited fretfully。',
 'fretfully 描写不安的表现，worriedly 偏担忧地；两者可以接近，但 fretfully 更容易让人想到难安稳、烦躁。',
 ('The child slept fretfully through the noisy afternoon.','那个吵闹的下午，孩子睡得很不安稳。'),('“Are they here yet?” he asked fretfully.','“他们到了没有？”他焦虑地问。'),sources=S('fretfully','fretful'))
W('fretfulness','/ˈfretfəlnəs/','烦躁不安；难以安稳的状态',
 '把那种坐不定、睡不稳、心里老在拧着的烦躁当一个整体来说，就是 fretfulness。',
 'fretful + -ness；先有带烦躁性质的形容词，再把这种性质、状态名词化。',FRETFUL+[['fretful + -ness → fretfulness','烦躁不安的状态、程度']],
 'a mood of fretfulness 烦躁不安的情绪；increased fretfulness 更明显的烦躁。',
 'a trace of fretfulness；fretfulness before a journey。',
 'fretfulness 命名不安稳的状态，a worry 可以指一件具体担心事；状态与引起状态的对象不是同一种东西。',
 ('Lack of sleep added to his fretfulness.','睡眠不足让他更加烦躁不安。'),('There was a trace of fretfulness in her voice.','她的声音里带着一丝焦躁。'),sources=S('fretfulness','fretful'))
W('fretless','/ˈfretləs/','无品的〔弦乐器〕；无烦恼的〔较旧用法〕',
 '有些贝司指板没有一道道凸起的品条，手指靠位置、耳朵控制音高，叫 fretless bass。现代音乐语境优先这样理解。',
 '乐器名词 fret 品 + -less 无；历史还见焦虑一支 fret + -less 的无烦恼义，两个同形基底不能混成同一个来源。',
 [['另源 fret：乐器指板上的品','来路未定，有法语圈箍等材料的联系分析，与焦虑 fret 分路'],['fret + -less → fretless','现代多说无品乐器；另有较早无烦恼的同形用法']],
 'a fretless bass 无品贝司；a fretless fingerboard 无品指板。',
 'play a fretless instrument；switch to fretless bass。',
 'fretless bass 没有品，不等于没有弦、不能定音；stringless 才是没有弦，两个名词基底决定所缺的东西。',
 ('She plays a fretless bass in the band.','她在乐队里弹无品贝司。'),('A fretless fingerboard allows smooth slides between notes.','无品指板让音与音之间能够平滑滑动。'),sources=S('fretless','fretless'))
W('fretwork','英 /ˈfretwɜːk/；美 /ˈfretwɝk/','镂空雕饰；交织纹样的装饰工艺或制品',
 '木板、金属板被做成细密相交、带孔隙的花纹，像门廊、屏风上的镂空雕饰，这类工艺或制品叫 fretwork。',
 '装饰纹样 fret + work。这里的 fret 接古法语 frete 交织、格状工艺，不接焦虑动词；work 命名工艺及做成的东西。',
 [['古法语 frete → 英语 fret 装饰纹样','更早可能联系日耳曼捆束材料，仍有不确定性'],['装饰 fret + work → fretwork','交织装饰、镂空雕饰的工艺或制品']],
 'wooden fretwork 木质镂空雕饰；decorative fretwork 装饰镂空工艺。',
 'delicate fretwork；fretwork around a window。',
 'fretwork 常突出交织、镂空或细密纹样，woodwork 是更宽泛的木工或木制部分；不能把所有木作都叫 fretwork。',
 ('Delicate wooden fretwork decorated the balcony.','精细的木质镂空雕饰装点着阳台。'),('The old screen had intricate fretwork along its upper edge.','旧屏风的上缘有复杂精细的镂空雕饰。'),sources=S('fretwork','fretwork'))
W('worryingly','英 /ˈwʌriɪŋli/；美 /ˈwɜːriɪŋli/','令人担忧地；让人不放心地',
 '水位低得反常，让人担心会缺水，叫 worryingly low。副词不是说水位自己担忧，而是这个程度引起人的担忧。',
 'worrying + -ly；worry 加 -ing 保留 y，外层再把令人担忧的性质用于程度。',WORRY+[['worry → worrying → worryingly','使担忧的性质，转成令人不放心的程度']],
 'worryingly low 低得令人担忧；worryingly high 高得令人不安。',
 'worryingly little progress；worryingly familiar pattern。',
 'worriedly 多写人担心地看、问；worryingly 多写事情到让人担心的程度。例如 asked worriedly 是人担心地问，worryingly low 是程度低得让人担忧。',
 ('The water level was worryingly low.','水位低得令人担忧。'),('The project had made worryingly little progress.','项目进展少得让人担心。'),sources=S('worryingly','worry'))
W('worriers','英 /ˈwʌriəz/；美 /ˈwɜːriərz/','爱担心、容易焦虑的人〔复数〕',
 '事情还没发生，就先想好几种坏结果，像这样常把心事揪在自己身上的人是 worriers。',
 'worry 的 y 变 i 加 -er → worrier，再加复数 -s。-er 早期接旧 worry 可指咬袭别的动物者；现代爱担心者义后来形成，不能倒说最初已是焦虑的人。',WORRY+[['worry → worrier → worriers','现代指多个容易自我担忧的人；旧动作实施者义另记年代']],
 'natural worriers 天生爱操心的人；a family of worriers 一家子爱担心的人。',
 'worriers rather than risk takers；help the worriers relax。',
 'worriers 是担忧的人，warriors 是战士；拼写读音都不同，/wʌri/ 一支不读成 war 的元音。',
 ('We are both worriers, so we checked the tickets twice.','我们俩都爱操心，所以把票检查了两遍。'),('The guide reassured the worriers before the hike.','徒步前，向导安抚了那些容易担心的人。'),sources=S('worriers','worry'))
W('worrisomely','英 /ˈwʌrisəmli/；美 /ˈwɜːrisəmli/','令人担忧、不放心地',
 '看起来安静得不正常，让你觉得“是不是出了问题”，可说 worrisomely quiet。它也常把让人担忧的评价加进程度。',
 'worrisome + -ly，保留 e；内层 worry 名词变 y 为 i 加 -some → worrisome，再接副词词尾。',WORRY+[['worry → worrisome → worrisomely','担忧 → 令人担忧的 → 令人不放心地']],
 'worrisomely quiet 安静得令人担心；worrisomely high 高得让人不安。',
 'worrisomely little information；worrisomely slow recovery。',
 'worrisomely 和 worryingly 很多语境能近义替换，前者基底 worrisome，后者基底 worrying；不是为凑区别而硬分成两种情绪。',
 ('The room was worrisomely quiet after the crash.','撞击声后，房间安静得令人担心。'),('The costs were rising worrisomely fast.','成本涨得快，令人担忧。'),sources=S('worrisomely','worry'))
W('unworried','英 /ʌnˈwʌrid/；美 /ʌnˈwɜːrid/','不担心的；没有忧虑的',
 '别人还在担心结果，他知道自己准备充分，心里很安稳，是 unworried。否定的是担忧状态，不等于他根本不关心事情。',
 'un- + worried；内层 worry 变 y 为 i 加 -ed，外层 un- 否定已形成的担忧状态。',WORRY+[['worry → worried → unworried','担心的状态，被 un- 否定成不担心']],
 'unworried about the result 不担心结果；seemed unworried 显得不担心。',
 'calm and unworried；remained unworried。',
 'unworried 不焦虑，uncaring 不关心、缺乏关怀；可以很在意比赛，同时因为准备充分而 unworried。',
 ('She seemed unworried about the delay.','她似乎不担心这次耽搁。'),('He remained calm and unworried before the exam.','考试前，他始终平静，没有忧虑。'),sources=S('unworried','worry'))
W('broodingly','/ˈbruːdɪŋli/','忧思地；闷闷地、带沉郁神情地',
 '人不说话，心里反复绕着一件不快，久久盯着远处，可以写 stared broodingly。像一直守着心事，把它留着不放。',
 'brooding + -ly；brood 的孵育材料先有长久惦念的比喻，外层再描述这种沉郁忧思的方式。',BROOD+[['brood → brooding → broodingly','久久忧思的性质，转成动作里的沉郁样子']],
 'stared broodingly 忧思地凝视；sat broodingly 闷闷地坐着。',
 'looked broodingly into the fire；gazed broodingly out of the window。',
 'thoughtfully 可以平静、建设性地思考，broodingly 更常带沉郁、把不快翻来覆去放在心上的感觉。',
 ('He stared broodingly into the fire.','他满腹心事地凝视着火。'),('She sat broodingly by the window after the argument.','争论过后，她闷闷地坐在窗边。'),sources=S('broodingly','brood'))
W('brooder','英 /ˈbruːdə/；美 /ˈbruːdər/','爱闷着反复想心事的人；保温育雏箱',
 'brood 可以是守着蛋孵育，也可以是守着心事反复想；brooder 便能命名爱忧思的人，也能命名给幼雏保温的设备。',
 'brood + -er；-er 能命名做事的人，也能命名起相应作用的设备。两义接 brood 的不同支线，不靠额外拼凑词根。',BROOD+[['brood + -er → brooder','忧思者；提供孵育、保温作用的设备']],
 'a quiet brooder 安静而爱想心事的人；a heated brooder 加热育雏箱。',
 'chicks in a brooder；a brooder with a heat source。',
 'brooder 养雏语境是保温设备，不是一个在生闷气的人；看 chicks、heat 等词能迅速确定分支。',
 ('He is a quiet brooder who rarely shares his worries.','他是个爱默默想心事的人，很少说出自己的烦恼。'),('The chicks stayed warm inside the brooder.','小鸡待在育雏箱里保暖。'),sources=S('brooder','brood'))
W('brooders','英 /ˈbruːdəz/；美 /ˈbruːdərz/','爱忧思的人；育雏保温箱〔复数〕',
 '一群人把心事闷在肚里，是 brooders；养殖场的几台幼雏保温设备，也叫 brooders。',
 'brood + -er → brooder，再加复数 -s，读 /z/；人和设备都是 -er 常能命名的角色。',BROOD+[['brood → brooder → brooders','多个忧思者，或多个保温育雏设备']],
 'heated brooders 加热育雏箱；two brooders 两台育雏保温设备。',
 'natural brooders；clean the brooders。',
 'brooders 的人义侧重爱闷着忧思，worriers 更直接说爱担心；养雏设备义则与这两类人的情绪都无关。',
 ('The farm installed two new brooders for the chicks.','农场为小鸡装了两台新的育雏保温设备。'),('Both brothers were brooders who kept their troubles to themselves.','兄弟俩都爱闷着想心事，把烦恼留在自己心里。'),sources=S('brooders','brood'))
W('mopey','英 /ˈməʊpi/；美 /ˈmoʊpi/','闷闷不乐、提不起精神的',
 '事情没如愿，人就耷拉着，做什么都没劲，像一直在原地闷着，这种样子叫 mopey。日常常带一点口语、轻描淡写的感觉。',
 'mope + -y，保留 e → mopey；另见 mopy 拼法。mope 的远源有不同分析，现代先按闷着、无精打采的整体动词理解。',MOPE,
 'feel mopey 感到闷闷不乐；look mopey 看起来没精神；a mopey afternoon 闷闷度过的下午。',
 'a little mopey；mopey after a disappointment。',
 'mopey 写低落、没精神的样子，sleepy 写困倦；人可以不困却因失望而 mopey。',
 ('He felt mopey after the trip was cancelled.','旅行取消后，他感到闷闷不乐。'),('She looked a little mopey all afternoon.','整个下午她看起来都有点没精打采。'),sources=S('mopey','mope'))
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_zgn',ROOTS,WORDS)
 extend_lessons()
