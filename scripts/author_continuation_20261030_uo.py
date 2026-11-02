"""Negative participles and everyday time/place compounds."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'B2740':dict(words=['hear','heard','unheard'],label='unheard：没有被听见、没有被倾听',note='un- 否定 + heard；unheard of 表从未听说、极不寻常，与声音没被听见的意思分别看搭配。'),
 'B3000':dict(words=['tell','told','untold'],label='untold：数不清与没讲出的两条旧义',note='tell 旧有计数、计算义，所以 untold 的未计数支线很早就存在；未讲述也是另一常用支线，不能只按今天 tell a story 来解释全部。'),
 'B2738':dict(words=['beat','beaten','unbeaten'],label='unbeaten：没有被击败',note='un- + beaten；比赛不败是没有输，不一定每场都赢。打蛋、击打等其他分支的未被处理义按具体对象看。'),
 'B2558':dict(words=['forgive','forgiven','unforgiven','unforgiving'],label='unforgiven 与 unforgiving：谁没被原谅，谁不肯宽容',note='unforgiven 表没被原谅的；unforgiving 常说人不肯宽恕或条件严酷，不是同一状态的随意替换。'),
 'A1793':dict(words=['after','afterward','afterwards'],label='afterward 与 afterwards：时间线上的后方',note='方向 -ward 与 after 的旧后方材料结合，现代指之后；afterwards 的 s 承接旧副词属格，现代两种形式意义基本相同。'),
 'B2422':dict(words=['day','nowadays','someday'],label='day 的两条时间组合：现如今与将来某天',note='nowadays 接 now 与旧 adayes 等时间副词材料，末尾 s 含旧副词属格历史；someday 是 some + day 的不定未来日期表达。'),
 'B3040':dict(words=['door','indoor','indoors','outdoors'],label='indoor 与 indoors：名词前限定和句中位置',note='indoors 接旧 in doors、within doors 等在门内的表达；现代通常作副词，indoor 常在名词前说室内的。'),
 'B2921':dict(words=['where','else','elsewhere','nowhere'],label='where 的范围：别处与无处',note='elsewhere 接 else + where，nowhere 接 no + where；else 本身接古英语 elles，通常放在疑问词、不定代词等后面。'),
 'B3246':dict(words=['no','nobody','nowhere'],label='nobody 与 nowhere：把人、地点归到没有',note='nobody 是没有人，nowhere 是没有地方；两者本身已有否定意义，常用标准表达无需再加一个 not 才能否定。'),
}
W('unheard','英 /ʌnˈhɜːd/；美 /ʌnˈhɝːd/','未被听见的、未获倾听的；unheard of：闻所未闻的',
 '话已经说出口，却没有人听到，或没有人认真听进去。unheard 既可说声音漏过耳朵，也可说意见没得到关注。',
 'un- 不 + heard，hear 的过去分词；相关否定形式有悠久历史。未被听到与未曾听说两支并存，后者现代常配 of。',
 [['hear → heard；加否定 un-','听见 → 未被听见'],['unheard；unheard of','未获倾听；未听说过、极不寻常']],
 'go unheard 没有被听见或理会；an unheard voice 没获倾听的声音；unheard of success 前所未有的成功；be unheard of 闻所未闻。',
 'leave concerns unheard；almost unheard of。','unheard 直接说没听见、没获倾听；unheard of 是未听说过、极罕见的常用搭配。of 不能机械当作可有可无。',
 ('Her warning went unheard in the noisy room.','房间太吵，她的警告没有被听见。'),('Snow in summer is almost unheard of here.','这里夏天下雪几乎闻所未闻。'),sources=['https://www.etymonline.com/word/unheard','https://en.wiktionary.org/wiki/unheard#English'])
W('untold','英 /ˌʌnˈtəʊld/；美 /ˌʌnˈtoʊld/','无数的、难以估量的；未讲述的',
 'untold stories 是还没讲出来的故事；untold damage 却常说损失大得难以估量。后一个意思要想起 tell 很早也有数、算的意思。',
 'un- + told；古英语 unteald 已有未计数、未估量义，接 tell 的旧计数分支。未讲述、未披露义后来也见于英语，不能把全部历史按今天讲故事义倒推。',
 [['古英语 unteald；tell 的旧计数分支','未计数、未估量'],['现代 untold 的两支','无数、难估量；未说出的']],
 'untold suffering 难以计量的苦难；untold damage 难估量的损失；an untold story 未讲述的故事；leave something untold 留着没说。',
 'untold numbers；a story still untold。','untold 在数量、程度前往往是很多、极大；在 story、secret 等前更可能是未被讲出。名词决定该沿哪条支线理解。',
 ('The storm caused untold damage to the old town.','风暴给古镇造成了难以估量的损失。'),('The documentary tells previously untold stories.','纪录片讲述了此前未被讲出的故事。'),sources=['https://www.etymonline.com/word/untold','https://en.wiktionary.org/wiki/untold#English'])
W('unbeaten','/ʌnˈbiːtən/','未被击败的、不败的；未被打过、搅打过的',
 '对手还没有赢过这支队伍，它就保持 unbeaten。重点是没输过，其中也可能有平局。',
 'un- 不 + beaten，beat 的过去分词。beaten 有被打、被击败等不同分支，否定后具体意思随名词和场景变化。',
 [['beat → beaten','击打、击败等 → 相应分词'],['un- + beaten → unbeaten','未被打过、击败或相应处理过的']],
 'an unbeaten team 不败的队伍；an unbeaten run 一段不败纪录；remain unbeaten 保持不败；unbeaten eggs 未搅打的蛋。',
 'unbeaten this season；an unbeaten record。','unbeaten 是没有输，不等于 all wins 全胜；平局也可以保持不败。unbeaten eggs 又接搅打分支，不能按比赛胜负翻译。',
 ('The team remained unbeaten throughout the season.','那支队伍整个赛季保持不败。'),('The draw extended their unbeaten run to ten games.','那场平局把他们的不败纪录延长到了十场。'),sources=['https://en.wiktionary.org/wiki/unbeaten#English'])
W('unforgiven','英 /ˌʌnfəˈɡɪvən/；美 /ˌʌnfərˈɡɪvən/','未被原谅的；尚未宽免的',
 '道歉说了，旧怨却还没有放下；过错仍没有得到宽恕，就是 unforgiven。它描述得到原谅这一结果还没有发生。',
 'un- 否定 + forgiven，forgive 的过去分词。forgive 接古英语给予、宽免词族，现代 unforgiven 否定其被宽恕、被宽免的结果。',
 [['forgive → forgiven','宽恕 → 被原谅、已原谅的分词'],['un- + forgiven → unforgiven','未被原谅的状态']],
 'an unforgiven mistake 未被原谅的错误；remain unforgiven 仍未获宽恕；feel unforgiven 感到未得到原谅。常见于叙述、较书面的情感表达。',
 'still unforgiven；leave an offense unforgiven。','unforgiven 描述未获原谅的人或事；unforgiving 描述不愿宽容的人、严酷的条件。一个看结果，一个看态度或作用。',
 ('He apologized, but still felt unforgiven.','他道了歉，却仍觉得没有得到原谅。'),('Her cruel remark remained unforgiven for years.','她那句刻薄话多年都未获原谅。'),sources=['https://en.wiktionary.org/wiki/unforgiven#English','https://www.etymonline.com/word/forgive'])
W('afterward','英 /ˈɑːftəwəd/；美 /ˈæftərwərd/','后来、之后',
 '先放一个事件作参照，再把下一件事放到它后面。We ate, and afterward ... 就是在接着往后讲。',
 '接古英语表示后方的 æfterwearde 等形式，含旧后方材料与方向 -weard，后受 after 等影响。现代常对应 after + -ward，空间后方的关系也用于时间。',
 [['古英语后方材料 + -weard','在后面、朝后方'],['现代 afterward','某件事之后；后来']],
 'shortly afterward 不久之后；soon afterward 随后不久；long afterward 很久以后。可独立在句中指向前面已说明的事件。',
 'a few days afterward；what happened afterward。','afterward 与 afterwards 意义基本相同，美式较偏好无 s 形式；after 作介词可接名词，afterward 通常不直接接名词当宾语。',
 ('We watched the film and discussed it afterward.','我们看完电影，随后讨论了它。'),('She called me a few days afterward.','几天后，她给我打了电话。'),sources=['https://www.etymonline.com/word/afterward','https://en.wiktionary.org/wiki/afterward#English'])
W('afterwards','英 /ˈɑːftəwədz/；美 /ˈæftərwərdz/','后来、之后〔与 afterward 基本同义〕',
 '前一件事已经有了时间位置，afterwards 把视线移到它后面。a week afterwards 就是那件事一周以后。',
 '接较早 afterward 加旧副词属格 -s 的形式；现代也能表面分析为 after + -wards。这里 s 是历史副词材料，不表示多个之后。',
 [['较早 afterward + 旧副词 -s','在后方、在后来'],['现代 afterwards','之后；与 afterward 并用']],
 'soon afterwards 随后不久；immediately afterwards 紧接其后；a month afterwards 一个月以后；years afterwards 多年以后。',
 'shortly afterwards；meet again afterwards。','afterward、afterwards 的选择有地区和编辑偏好，不靠 s 区分发生一次还是多次。afterword 是书后的后记，另是 after + word。',
 ('We went for a walk and had coffee afterwards.','我们散了步，之后喝了咖啡。'),('A week afterwards, a letter arrived.','一周之后，一封信到了。'),sources=['https://www.etymonline.com/word/afterward','https://en.wiktionary.org/wiki/afterwards#English'])
W('nowadays','/ˈnaʊədeɪz/','如今、现今',
 '以前常是另一种样子，现在这个时期变了。nowadays 常让人把如今的生活方式与过去作比较。',
 '由中古英语 nou adayes 等缩合，now 加旧 adayes 在这些日子里；adayes 接 a-〔旧 on、在〕、day 与旧副词属格 -s。现代写为一个固定时间副词。',
 [['中古英语 now + adayes','现在这段日子里'],['缩合为 nowadays','如今、现今；常与过去对照']],
 'nowadays people often ... 如今人们常……；rare nowadays 如今少见；more common nowadays 如今更普遍。说当前时代或阶段，不只此时这一秒。',
 'much easier nowadays；nowadays compared with the past。','now 可指眼下这一刻，也可指当前阶段；nowadays 通常更偏当前这些日子、这个时代。常见用法是概括当前的生活、做法。',
 ('Nowadays, many people read the news on their phones.','如今，很多人用手机看新闻。'),('It is easier to keep in touch nowadays than it used to be.','如今保持联系比过去容易。'),sources=['https://www.etymonline.com/word/nowadays','https://en.wiktionary.org/wiki/nowadays#English'])
W('indoors','英 /ɪnˈdɔːz/；美 /ɪnˈdɔːrz/','在室内；到室内',
 '从院子进到房子里，或一直待在房子里面，都可以是 indoors。这个副词把位置落在建筑物内部。',
 '接旧 in doors、within doors 等在门内的表达，后来合写。doors 的形式留在固定词里；现代 indoors 通常作地点、方向副词。',
 [['in doors；更早相关 within doors 表达','在门内、建筑物内部'],['合写 indoors','在室内、进入室内的副词']],
 'stay indoors 待在室内；go indoors 进屋；bring the plants indoors 把植物搬进室内；work indoors 在室内工作。',
 'play indoors；spend the day indoors。','indoor 常放名词前：indoor activities 室内活动；indoors 常修饰动作、位置：play indoors。在普通表达里不写 indoors activities。',
 ('It was raining, so we stayed indoors.','下雨了，所以我们待在室内。'),('She brought the chairs indoors before the storm.','暴风雨来前，她把椅子搬进了屋。'),sources=['https://en.wiktionary.org/wiki/indoors#English'])
W('else','/els/','其他、别的、另外',
 '眼前这个已经提到，再问还有什么、还有谁。else 把范围推到当前对象以外。',
 '接古英语 elles 以另一方式、其他等，属于旧另一个、别的词族；现代常跟在不定代词、疑问词等后面。更早的结尾有旧副词形式历史，现代整体认读。',
 [['古英语 elles','其他、另外、以另一方式'],['现代 else','放在 someone、what 等后面，指除此以外']],
 'someone else 别人；anything else 其他东西；what else 还有什么；who else 还有谁；somebody else’s bag 别人的包。',
 'nothing else；everyone else；where else。','通常 someone else，不说 else someone。所有格跟在整个短语后：someone else’s，常见结构不是 someone’s else。',
 ('Would you like anything else?','你还想要点别的吗？'),('I thought the bag belonged to someone else.','我原以为那个包是别人的。'),sources=['https://www.etymonline.com/word/else','https://en.wiktionary.org/wiki/else#English'])
W('elsewhere','英 /ˌelsˈweə/；美 /ˌelsˈwer/','在别处；到其他地方',
 '眼下这个地方不合适，视线转到另一个地方。look elsewhere 就是去别处找。',
 'else + where，接古英语 elles hwær 等在其他地方的表达，后合写。where 提供地点，else 把地点排到当前这一处之外。',
 [['古英语 elles hwær 等','在另一个地方'],['现代 else + where → elsewhere','在别处、到别处']],
 'look elsewhere 去别处找；live elsewhere 住在其他地方；available elsewhere 在别处能得到；elsewhere in the book 在书的其他地方。',
 'seek help elsewhere；move elsewhere。','elsewhere 本身就是地点副词，普通表达直接说 look elsewhere。somewhere else 也常表示别的地方，elsewhere 往往稍紧凑、书面。',
 ('We could not find a table, so we ate elsewhere.','我们找不到座位，就去别处吃了。'),('The same idea appears elsewhere in the book.','同一个想法也出现在书的其他地方。'),sources=['https://www.etymonline.com/word/elsewhere','https://en.wiktionary.org/wiki/elsewhere#English'])
W('someday','/ˈsʌmdeɪ/','将来某一天、总有一天',
 '日历上还没有圈出具体日期，但相信未来会有那么一天。someday 常放希望、计划或未定的愿望。',
 'some + day，由分写的时间短语发展成常见合写副词。现代主要指不确定的未来日期；更早同类表达也有不同时间指向，不能只用现代形式倒推每个旧用例。',
 [['some + day 的较早短语','某一天；具体时间指向随语境'],['现代合写副词 someday','未来某个未定日期']],
 'maybe someday 或许将来某天；someday I’ll ... 总有一天我会……；hope to do something someday 希望将来某天做某事。分写 some day 在相应用法中也会见到。',
 'someday in the future；someday soon。','someday 指一天还未确定，sometime 可泛说某个时候；some days 则是有些日子，不能因为多一个 s 就仍按总有一天翻译。',
 ('Someday, I hope to write a novel.','我希望总有一天能写一部小说。'),('Maybe we will meet again someday.','或许我们将来某天还会见面。'),sources=['https://www.etymonline.com/word/someday','https://en.wiktionary.org/wiki/someday#English'])
W('nowhere','英 /ˈnəʊweə/；美 /ˈnoʊwer/','无处；哪儿也没有；偏远地方；毫无进展',
 '一个个地方都找过，仍没有可去、可找到的地点，就是 nowhere。get nowhere 又把没有到达地点比喻成事情没进展。',
 'no + where，接古英语 nahwær 无处、全无等。后来名词用法可指偏远、难到达的地方，并形成 middle of nowhere 等表达。',
 [['古英语 nahwær；no 与 where 的结合','没有地方、无处'],['现代 nowhere 的地点与比喻用法','无处；偏远地方；无进展']],
 'nowhere to go 无处可去；nowhere near 远远没达到；get nowhere 毫无进展；in the middle of nowhere 在偏远荒僻处。',
 'nowhere to be found；lead nowhere。','I have nowhere to go 与 I don’t have anywhere to go 意思相近；nowhere 本身已有否定。nowhere near finished 是远没做完，不能只按地理位置读。',
 ('We had nowhere to sit.','我们没有地方坐。'),('The discussion was getting nowhere.','讨论毫无进展。'),sources=['https://www.etymonline.com/word/nowhere','https://en.wiktionary.org/wiki/nowhere#English'])
W('nobody','英 /ˈnəʊbədi/；美 /ˈnoʊbədi/，也有末音节较清晰读法','没有人；无名小卒、无足轻重的人',
 '把在场的人都数进去，却没有一个符合条件：Nobody answered。名词 a nobody 则把人按社会地位看，带轻视意味。',
 'no + body，body 从身体很早也能代指一个人。中古英语已有 no bodi 等表达，后经历分写、连字符和合写；无足轻重的人这一名词义后来发展。',
 [['no + body〔人〕→ 中古英语 no bodi 等','没有任何人'],['现代 nobody；a nobody','没有人；被看作不重要的人']],
 'nobody knows 没有人知道；nobody else 其他任何人都不；nobody at home 家里没人；feel like a nobody 感觉自己无足轻重。',
 'nobody was there；nobody can tell。','nobody 作代词时通常配单数动词：Nobody is ready。a nobody 是可数名词，评价地位，和没有一个人在场是不同用法。',
 ('Nobody answered the door.','没有人来应门。'),('She refused to treat him as a nobody.','她不愿把他当作无足轻重的人。'),sources=['https://www.etymonline.com/word/nobody','https://en.wiktionary.org/wiki/nobody#English'])
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_uo',ROOTS,WORDS)
 extend_lessons()
