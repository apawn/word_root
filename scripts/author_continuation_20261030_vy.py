"""Calendar vocabulary and the Latin seven root, with honest comparisons."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'B2421':dict(words=['month','months','January','February','March','April','May','June','July','August','September','October','November','December'],label='日历语境对照：month 与十二个月份名〔月份名并非 month 的派生词〕',note='本组仅为日历词汇阅读对照：month 是本族的月亮计时词，月份名分别借入拉丁、法语等命名传统，不能把它们都拆成 month 加后缀。每个月份按各自真实来源解释。'),
 'B2437':dict(words=['week','weeks'],label='week → weeks：一周与多周',note='weeks 直接加 s，词尾读 ks；两周和两周的写法按句型分别说明。'),
 'B2463':dict(words=['year','years'],label='year → years：年份、年龄与持续时间',note='years 作名词复数，年龄、时长、所有关系等常见结构放在一起理解。'),
 'C0307':dict(words=['December'],label='decem 十 → December：旧序号保留在月份名中',note='December 接拉丁 decem 十，对应旧月份序号；今天是公历十二月，名称并非按现代次序重新造出。'),
}
R('C1311','七；拉丁语数字词的组合材料',
 'SEPT-：七；月份名保留旧排序，英语本族数字另走自己的历史',
 'September 今天是九月，里面却留着拉丁七的线索。它像一张没有随新排法改名的旧编号，帮助记住数字词根。',
 '拉丁 septem 意为七；September 的名称保留了旧罗马日历以三月起算时的第七月序号。英语 seven 也是远层同源词，但经日耳曼语、古英语继承，不是直接从拉丁 septem 借入。',
 '本页把 September 与已精讲的 seven、seventh、seventeen、seventy 对照。前者是拉丁月份名的借词，后面一组是英语本族数字及其形式；相同概念和远层词源联系，不等于现代互相换字母。',
 [['月份借词','September'],['远层同源比较：英语数字词族','seven seventh seventeen seventy']],
 'September 的七是旧命名信息，现代月份仍为第九。拼写相同的 sept- 还可能属于隔开、围隔的另一个词族，学习时分别看来源。',
 'September is the ninth month today, although its name preserves an older seven.\n\nSeptember 今天是第九个月，名称却保留了更早的七。',
 'September seven seventh seventeen seventy')
W('February','英 /ˈfebruəri/；美 /ˈfebrueri/〔另有第一个 r 弱化、省略的常见读法〕','二月',
 '给 February 一个净化仪式的旧画面：它的拉丁名称和古罗马的净化活动有关。今天就是公历的二月。',
 '拉丁 februarius mensis 净化之月，接 februa 净化仪式、februare 净化。英语先经法语借入相关形式，后来按拉丁拼写调整为 February；更早 febru- 的来源不确定。',
 [['拉丁 februa、februarius mensis','净化仪式 → 净化之月'],['法语相关形式 → 中古英语 → February','借入后受拉丁拼写影响形成现代名称']],
 'in February 在二月；early February 二月初；late February 二月下旬；February 12 二月十二日〔美式日期顺序〕；Feb. 常见缩写。',
 'a February morning；next February。','拼写有两个 r，第二个在 ary 一段。月份前常用 in；具体到某一天常用 on。读音中第一个 r 的保留、弱化有常见变体，不把一种读法当唯一标准。',
 ('The course starts in February.','课程二月开始。'),('We met on a cold February morning.','我们在二月一个寒冷的早上见了面。'),sources=['https://www.etymonline.com/word/February','https://en.wiktionary.org/wiki/February#English'])
W('March','英 /mɑːtʃ/；美 /mɑːrtʃ/','三月',
 'March 的月份名与罗马神 Mars 有关。它今天排第三，旧罗马月份排列却曾从这一月起算。',
 '经法语相关形式接拉丁 Martius mensis，意为 Mars 之月。小写 march 行进、行军经法语 marcher，近源不同，不能因为战神名称就把两个词简单当成一条变化链。',
 [['拉丁 Mars、Martius mensis','神名 → 相应月份名'],['法语相关形式 → 英语 March','成为现代公历三月的名称']],
 'in March 在三月；early March 三月初；March 5 三月五日〔美式顺序〕；Mar. 常见缩写；March weather 三月天气。',
 'next March；a March afternoon。','月份 March 首字母大写；动词、普通名词 march 通常小写。月份命名来自 Mars，行军义不能只凭现代字形反推同一个直接来源。',
 ('The exhibition runs from March to May.','展览从三月持续到五月。'),('We plan to move in early March.','我们计划三月初搬家。'),sources=['https://www.etymonline.com/word/march','https://en.wiktionary.org/wiki/March#English'])
W('April','/ˈeɪprəl/','四月',
 'April 是公历四月。可以用春花开放作联想来记，但这个联想与确证的历史来源要分清。',
 '经古法语 avril 接拉丁 Aprilis，英语拼写又受拉丁形式影响。Aprilis 更早来源不定；与打开、花开相连是旧解释，还有其他分析，不能当成已证实的唯一构词。',
 [['拉丁 Aprilis → 法语 avril','古罗马月份名称'],['法语、拉丁影响 → 英语 April','进入英语并形成现代拼写；更早来源不定']],
 'in April 在四月；April showers 四月阵雨；April 1 四月一日〔美式顺序〕；Apr. 常见缩写。',
 'an April morning；the end of April。','April 通常两音节，第一节重读；不要按字母把末尾 il 一律读成 /ɪl/。月份名和人名 April 可同形，依上下文判断。',
 ('The garden opens to visitors in April.','花园四月向访客开放。'),('We hope to finish the repairs by the end of April.','我们希望最迟四月底完成维修。'),sources=['https://www.etymonline.com/word/April','https://en.wiktionary.org/wiki/April#English'])
W('May','/meɪ/','五月',
 'May 是公历五月。它和可能、允许的 may 同音同拼写，但月份名是另外一条拉丁命名来源。',
 '经古法语 mai 及拉丁 Maius mensis 进入英语，常解释为可能与罗马女神 Maia 有关，细节仍有不确定处。小写情态动词 may 则接古英语能够的词族。',
 [['拉丁 Maius mensis → 法语 mai → May','五月名称；更早命名常联系 Maia，但并非完全确定'],['现代月份名 May','首字母大写，与 may 情态动词分来源']],
 'in May 在五月；early May 五月初；May 20 五月二十日〔美式顺序〕；May Day 五月一日、五朔节等〔依语境〕。',
 'a May wedding；next May。','May 是月份，也可以是人名；may 作情态动词常见于 may go、may be 等结构。月份 May 通常不再缩写。',
 ('We are planning a short trip in May.','我们计划五月去短途旅行。'),('The trees were covered in fresh leaves by early May.','到五月初，树上已经长满新叶。'),sources=['https://www.etymonline.com/word/may','https://en.wiktionary.org/wiki/May#English'])
W('June','/dʒuːn/','六月',
 'June 是公历六月，读起来是一个音节。它的古罗马月份名通常与女神 Juno 联系起来理解。',
 '英语接拉丁 Iunius mensis 等月份形式，通常解释为与 Juno 有关，也有经法语形式的影响。现代 June 不是由英语 young 或 junior 直接改造出来的。',
 [['拉丁 Iunius mensis','六月的月份名，通常联系 Juno'],['拉丁、法语相关形式 → 英语 June','成为现代公历六月名称']],
 'in June 在六月；June 10 六月十日〔美式顺序〕；early June 六月初；a June wedding 六月举行的婚礼。',
 'the end of June；next June。','June /dʒuːn/ 与 July /dʒuˈlaɪ/ 的音节数、重音都不同。月份前常用 in，具体日期前常用 on。',
 ('The school exhibition takes place in June.','学校的展览六月举行。'),('We must finish the work before the end of June.','我们必须在六月结束前完成工作。'),sources=['https://www.etymonline.com/word/June','https://en.wiktionary.org/wiki/June#English'])
W('July','/dʒuˈlaɪ/','七月',
 'July 的名称纪念 Julius Caesar。可以把 Julius 的人名线索记在前面，再单独记今天后半节重读的发音。',
 '经法语相关形式及拉丁 Iulius 的月份名进入英语，旧月份名 Quintilis 有第五的意思，后来改名纪念 Julius Caesar。现代 July 的重音、读音有自己的英语演变。',
 [['旧月份名 Quintilis → 拉丁 Iulius','旧序号名称改为纪念 Julius Caesar 的名称'],['法语、拉丁相关形式 → July','进入英语并形成现代读音 /dʒuˈlaɪ/']],
 'in July 在七月；July 15 七月十五日〔美式顺序〕；the beginning of July 七月初；a July afternoon 七月的一个下午。',
 'late July；this July。','July 后半节重读，June 是一个音节；拼写、重音一起记。旧称第五记录旧排序，今天 July 是现代公历第七个月。',
 ('The new gallery is due to open in July.','新画廊预计七月开放。'),('We spent two weeks by the sea last July.','去年七月，我们在海边待了两周。'),sources=['https://www.etymonline.com/word/July','https://en.wiktionary.org/wiki/July#English'])
W('September','英 /sepˈtembə/；美 /sepˈtembər/','九月',
 'September 里的 septem 是拉丁七。它像保留旧编号的月份名：从三月起算时排第七，今天的公历却排第九。',
 '英语经古法语 septembre 等形式及拉丁 September 继承，接拉丁 septem 七。结尾是拉丁月份名称的一部分，具体早期构词有不同分析，不把 ber 当成英语里能随意加的月后缀。',
 [['拉丁 septem 七 → September','保留旧日历第七月的序号'],['拉丁、法语 → 英语 September','现代公历九月名称']],
 'in September 在九月；early September 九月初；September 3 九月三日〔美式顺序〕；Sep.、Sept. 常见缩写。',
 'the end of September；next September。','sept- 七与现代月份第九并不冲突，词名记录的是旧排序。英语 seven 与拉丁 septem 可作远层同源比较，近代英语没有按两词互换字母造出月份。',
 ('The new term starts in September.','新学期九月开始。'),('We spent the first week of September in the mountains.','九月的第一个星期，我们在山里度过。'),sources=['https://www.etymonline.com/word/September','https://en.wiktionary.org/wiki/September#English'])
W('December','英 /dɪˈsembə/；美 /dɪˈsembər/','十二月',
 'December 保留拉丁 decem 十。它与 September、October、November 一样，名称里的数字是旧排序的痕迹。',
 '经古法语 decembre 接拉丁 December，由 decem 十形成的月份名。旧罗马排列从三月起算时它排第十，现代公历为第十二。',
 [['拉丁 decem 十 → December','旧序号第十的月份名'],['法语等形式 → 英语 December','现代十二月，名称保留旧数字']],
 'in December 在十二月；early December 十二月初；December 31 十二月三十一日〔美式顺序〕；Dec. 常见缩写。',
 'the end of December；a December evening。','decem 的十可与 decimal 十进制等同族材料联系，但月份要按现代顺序使用。首字母 c 在 December 中读 /s/，重音在第二节。',
 ('The project should be finished by the end of December.','项目应在十二月底前完成。'),('She was born on a December evening.','她出生在十二月的一个晚上。'),sources=['https://www.etymonline.com/word/December','https://en.wiktionary.org/wiki/December#English'])
W('weeks','/wiːks/','周、星期〔week 的复数〕',
 '一周通常用 a week，几周便是 weeks。长元音 /iː/ 后接 /ks/，是一个音节。',
 'week + -s，词末 /k/ 后读 /s/。week 从古英语 wice、wucu 等周期词延续；复数只是现代数量形式。',
 [['古英语 wice、wucu → week','一周、周期'],['week + -s → weeks','多个星期，读 /wiːks/']],
 'two weeks 两周；a few weeks 几周；for several weeks 持续几周；in two weeks 两周后；two weeks’ time 两周之后这一时间点。',
 'weeks later；three weeks ago。','for two weeks 常说持续两周，in two weeks 常说两周后，也可能按语境说在两周内完成。weeks 与 weak 的复数、变形无关；week、weak 本来只是同音词。',
 ('We stayed there for three weeks.','我们在那里住了三个星期。'),('The course starts in two weeks.','课程两周后开始。'),sources=['https://en.wiktionary.org/wiki/weeks#English','https://en.wiktionary.org/wiki/week#English'])
W('months','/mʌnθs/','月、月份；多个月的时间〔month 的复数〕',
 '日历翻过一页又一页，就过了 months。它可以数具体月份，也可以量一段持续多久的时间。',
 'month + -s，标准形式尾部是 /nθs/，整个词一个音节。month 接古英语 monath 等，与 moon 月亮是历史同族；现代历法月份并不要求等于一个精确月相周期。',
 [['古英语月亮计时词族 → month','按月亮周期计时的旧背景 → 月份单位'],['month + -s → months','多个日历月或多个月的时长']],
 'three months 三个月；for six months 持续六个月；every two months 每两个月；the summer months 夏季几个月；months later 几个月后。',
 'in a few months；many months of work。','every two months 是每隔两个月，不是每月两次。标准尾音保留 /θs/，连读有实际弱化；书写仍是 months。',
 ('I have been learning English for six months.','我学英语已经六个月了。'),('The group meets every two months.','这个小组每两个月见面一次。'),sources=['https://en.wiktionary.org/wiki/months#English','https://en.wiktionary.org/wiki/month#English'])
W('years','英 /jɪəz/；美 /jɪrz/','年；年份；岁数；多年〔year 的复数〕',
 '一年又一年是 years。说年龄、经验、持续时间时，它都是把年份作为计量单位数出来。',
 'year + -s，词尾读 /z/。year 接古英语 gear、经中古英语 yer 等延续，属于日耳曼语旧年词；现代 y 对应较早该词开头的音变。',
 [['古英语 gear → 中古英语 yer → year','年度、年的计时单位'],['year + -s → years','多年；年龄、持续时长的常用单位']],
 'five years 五年；ten years old 十岁；for years 多年来；over the years 这些年来；two years’ experience 两年经验。',
 'years ago；in recent years。','She is ten years old 中 years 是复数，不带所有格。two years’ work 则用复数所有格表示两年的工作；this year’s report 是这一年的报告。',
 ('She has worked here for five years.','她已经在这里工作五年了。'),('The book represents many years’ work.','这本书凝结了多年的工作。'),sources=['https://en.wiktionary.org/wiki/years#English','https://en.wiktionary.org/wiki/year#English'])
ROOTS[-1]['checked_sources']=['https://www.etymonline.com/word/September','https://www.etymonline.com/word/seven']
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_vy',ROOTS,WORDS)
 extend_lessons()
