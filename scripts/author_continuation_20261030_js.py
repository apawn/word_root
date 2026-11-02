"""Mate compounds, begging and education."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
W('inmate','/ˈɪnmeɪt/','囚犯；机构中的被收容者；同住者〔旧用〕',
 '旧时可以只是同住一处的人；现代常把镜头放到被关在监狱等机构里的人。不能因为 roommate 是室友，就把新室友随口叫 inmate。',
 'in 在里面 + mate 同伴，或前半原为 inn 住所，具体分析不完全一致。早期同住义后来收窄到机构收容、拘禁语境。',
 [['in／可能的 inn + mate','住在同一处的人、住户'],['现代 inmate 的常用收窄','监狱等机构中的被关押、收容者']],
 'a prison inmate 囚犯，inmates at the institution 该机构被收容者。现代谈医院普通病人通常用 patient，不因都住在机构里就自动叫 inmate。',
 'a prison inmate；inmates at the institution。',
 'inmate 与 roommate 现代常用义差别明显；cellmate 特别说同一牢房的人，inmate 不要求和另一人同住一间牢房。',
 ('The report includes interviews with prison inmates.','报告收录了对囚犯的访谈。'),('The novel follows an inmate adjusting to life inside the institution.','小说讲述一位被收容者适应机构内生活的经历。'),sources=['https://en.wiktionary.org/wiki/inmate#English','https://www.etymonline.com/word/inmate'])
W('stablemate','/ˈsteɪbəlmeɪt/','同马厩、同练马师旗下的马；同机构者',
 '两匹赛马归同一马厩、团队管理，是 stablemates；音乐人、产品同属一家公司，也能借这个同门关系来形容。',
 'stable 马厩 + -mate 同处、同属一组者。stable 在这里不是稳定的形容词，不把它译成稳定朋友。',
 [['stable 马厩 + mate 同伴 → stablemate','共同马厩、训练体系中的马'],['机构关系的扩展','同公司、组织等的成员或产品']],
 'a horse and its stablemate 一匹马及其同厩马，a singer’s label stablemate 与歌手同唱片公司的艺人。具体共同组织由上下文说明。',
 'a horse’s stablemate；a label stablemate。',
 'stablemate 不要求两匹马站在完全同一个小隔间，常看所属训练、经营团队；teammate 更直接说同队的人。',
 ('The horse finished just ahead of its stablemate.','那匹马刚好领先同厩马冲线。'),('The singer recorded a duet with a label stablemate.','这位歌手与同唱片公司的艺人录制了一首二重唱。'))
R('A2376','共享场所、活动或组织关系的人物与动物名称','-MATE：有共同处境或所属关系，不保证一定是好友','roommate 同住、teammate 同队、cellmate 同牢房；stablemate 同厩或同机构；inmate 已收窄常用义。',
 'mate 的同伴关系很有生产力，前半告诉你共享什么。但每个整词也有使用历史，inmate 就不能只按现在的自由拼词猜。',
 'mate 伙伴借自中古低地德语等形式，更早联系共同用餐；与地点、活动、组织词组合。',
 [['居住、学习与同行','roommate · housemate · flatmate · classmate · schoolmate · shipmate'],['团队、组织与特殊处境','teammate · bandmate · stablemate · cellmate · inmate']],
 '-mate 不自动等于亲密朋友；inmate 常说囚犯，stablemate 不取稳定的 stable。',
 'The bandmate and former roommate later became his label stablemate.\n\n那位乐队伙伴兼旧室友，后来又与他成为同唱片公司的艺人。','roommate housemate flatmate classmate schoolmate shipmate teammate bandmate stablemate cellmate inmate')
B=[['中古英语 beggen、beggere 等','乞求、乞讨与乞讨者'],['更早来源有不同分析','联系古英语请求词，或经法语、低地地区人物称呼发展；先后不完全确定'],['现代规则可帮助识别','beg → begging；beggar 现代可联系 beg，但不能把规则识别等同唯一历史']]
W('beg','/beɡ/','恳求、央求；乞讨；郑重、礼貌地请求',
 '普通 ask 是问、要；beg 把姿态放得更低、语气更迫切：求你了。它也可指向人讨生活所需，或用在固定礼貌表达里。',
 '中古英语 beggen 的更早来源有争议：有联系古英语请求词的分析，也有与法语人物称呼、倒构相关的分析。不要只选一个传说当定论。',B[:2],
 'beg for help 乞求帮助，beg someone to stay 恳求某人留下，beg for money 乞讨钱财，I beg your pardon 请再说一遍、请原谅〔依语调〕。',
 'beg for；beg someone to；I beg your pardon。',
 'beg the question 传统逻辑义是把待证明前提先当成真；现代也常用来表示引出问题。两种实际用法分语境，别只逐字译成乞求问题。',
 ('She begged him not to leave.','她恳求他别走。'),('I beg your pardon; I did not hear the last word.','请再说一遍，我没听清最后一个词。'),sources=['https://en.wiktionary.org/wiki/beg#English','https://www.etymonline.com/word/beg'])
W('begging','/ˈbeɡɪŋ/','乞讨、恳求；正在央求；无人认领、采用〔go begging〕',
 'begging 可以说反复或正在求人，也可以把乞讨这件事作为名词。go begging 却常反过来：有东西摆着，没人来要。',
 'beg + -ing，双写 g，中古英语已有 begging、beggynge 等。固定 go begging 用法不能只把进行词形逐字硬译。',B[:1]+[['beg + -ing → begging','恳求、乞讨行为；固定搭配另有无人问津义']],
 'begging for help 恳求帮助，street begging 街头乞讨，a chance going begging 一个无人抓住的机会。',
 'begging for help；street begging；go begging。',
 'an opportunity went begging 说机会没被利用，不是机会在街上乞讨。begging 是名词还是进行动作，由整句结构决定。',
 ('The child was begging for one more story.','孩子正央求再讲一个故事。'),('Several good opportunities went begging.','几个好机会白白错过了。'))
W('beggar','英 /ˈbeɡə/；美 /ˈbeɡər/','乞讨者；使贫困；超出想象、描述能力〔固定动词用法〕',
 '名词常指靠乞讨求助的人；It beggars belief 却不是让信仰乞讨，而是夸张说这件事超出人能相信的范围。',
 '中古英语 beggere、beggare 等；现代可联系 beg + 人物词尾 -ar，但历史上也有经法语 begart、低地地区人物称呼发展等分析。与 beg 的更早先后不能一句后缀规则定死。',B[:2]+[['beggar 名词转动词','使陷贫困；资源不够应付 → 超出理解、描述能力']],
 'a beggar in the story 故事中的乞讨者，beggar belief 难以置信，beggar description 难以形容。you lucky beggar 在某些英式口语里可带打趣语气，实际态度依场景。',
 'a beggar；beggar belief；beggar description。',
 'beggar 是人物名词时，与 all poor people 所有贫困者不等同；动词固定用法又不在说一群实际乞讨者。',
 ('The story opens with a beggar asking for food.','故事开头，一个乞讨者正在讨食物。'),('The scale of the mistake beggars belief.','错误严重得让人难以置信。'),sources=['https://en.wiktionary.org/wiki/beggar#English','https://www.etymonline.com/word/beggar'])
R('B2754','恳切请求、乞讨与人物名词，固定搭配又有自己的转折','BEG：请求更迫切；BEGGAR：人物或固定动词','beg → begging；beggar 与之关系清楚，远源和先后仍有争议。',
 '日常先学真实句型，再把不可靠的词源故事放下。go begging、beggar belief 不按每个字逐字翻。',
 '中古英语 beggen、beggere 等；更早来源有不同分析；-ing 前双写 g，beggar 拼写 -ar。',
 [['动作、过程与人物','beg · begging · beggar']],
 'go begging 是无人利用、认领；beggar belief 是难以置信；词源不能只凭后缀猜定。',
 'The child kept begging for another story about the beggar.\n\n孩子一直央求再讲一个关于乞讨者的故事。','beg begging beggar')
W('uneducated','英 /ʌnˈedʒʊkeɪtɪd/；美 /ʌnˈedʒəkeɪtɪd/','未受教育的；缺少某方面知识、训练的',
 '可能说没有机会接受系统教育，也可能说在某个领域没有学过、没训练过。看具体缺哪方面，别把它直接等同于智力差。',
 'un- 否定 + educated；educated 来自 educate + -ed，接拉丁 ēducāre 培养、教育。这里 un- 否定受教育、训练状态，不表示把已经学过的知识倒着拆掉。',
 [['拉丁 ēducāre → educate → educated','培养、教育 → 受过教育、训练的'],['un- + educated → uneducated','未受相应教育、缺乏相应知识训练']],
 'an uneducated person 未受教育者，to an uneducated ear 对未受相关训练的耳朵而言。后者常指音乐辨识能力，不代表听觉器官本身有故障。',
 'an uneducated person；to an uneducated ear。',
 'uneducated 不等于 unintelligent；正式学校经历、某领域训练和理解能力是不同评价。具体语境的称呼可能带贬义。',
 ('The memoir describes an uneducated farmer who taught himself to read.','回忆录讲述一位未受学校教育、却自学阅读的农民。'),('To my uneducated ear, the two versions sound similar.','在我这个没受过相关训练的人听来，两种演奏版本很像。'))
R('B4599','接受教育、训练的状态，以及缺少相应训练','EDUCATED：受过教育或相应训练；UNEDUCATED：缺少这一层','educated → uneducated。',
 '修饰 person、guess、ear 等对象时，要看实际评价的知识、训练范围。不要把一个标签扩大成全部能力。',
 'educate + -ed → educated；un- 形成相应否定状态。',
 [['状态与否定','educated · uneducated']],
 'uneducated 不自动等于愚笨；uneducated ear 常是音乐等方面缺少训练。',
 'The course gives students an educated understanding of sounds that an uneducated ear might miss.\n\n课程帮助学生理解未经训练的耳朵可能忽略的声音。','educated uneducated')
if __name__=='__main__':save('continuation_20261030_js',ROOTS,WORDS)
