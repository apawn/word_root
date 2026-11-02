"""Complete common forms of walk, act, serve, offer, open, close and test."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'B3515':dict(words=['walk','walks','walked'],label='walk → walks → walked：步行与散步',note='中古英语移动、踩踏词族发展到步行，常见标准读音中 l 不单独发音。'),
 'C0023':dict(words=['act','acts','acted'],label='act → acts → acted：做出的行为与表演',note='拉丁做、执行的词族，动作、戏剧与法令分支分别看。'),
 'C1325':dict(words=['serve','serves'],label='serve → serves：服务、供餐与发挥作用',note='早期服侍、效力的词族，现代服务对象、任务和功能都可使用。'),
 'C0415':dict(words=['offer','offers'],label='offer → offers：主动带到面前的提议、东西',note='英语动词有古英语 offrian 和法语后续影响，名词也有法语借入分析。'),
 'B2487':dict(words=['open','opens'],label='open → opens：从封闭到能通过、能开始',note='本族敞开词的名词、动词等形式保留古老历史，opens 是规则第三人称。'),
 'C0232':dict(words=['close','closes'],label='close → closes：把开口关住、让事情结束',note='动词 close 通常以 z 结尾，closes 增加 iz；亲近的形容词 close 则常以 s 结尾。'),
 'B3237':dict(words=['test','tests','tested'],label='test → tests → tested：检验、考验与已试过',note='test 的检验动作和检验事项有相连的词族，tests 形成 sts 辅音连接，tested 则增加 id 音节。'),
}
W('walks','英 /wɔːks/；美 /wɔːks, wɑːks/','步行、散步；遛〔动物〕；散步活动、步行路线〔复数〕',
 '靠脚一步步走是 walks；一次次散步、适合步行的路线也能数成 walks。walks the dog 则是带狗出去走。',
 'walk + -s，/k/ 后读 /s/，常见标准读音中 l 不发音。walk 经中古英语承接古英语移动、转动、踩踏相关形式，再发展为步行。',
 [['古英语相关移动、踩踏词 → 中古英语 walken → walk','移动、踩踏 → 步行'],['walk + -s → walks','单数主语走路；多次散步、路线']],
 'walks to work 步行上班；walks the dog 遛狗；long walks 长距离散步；coastal walks 海岸步行路线。',
 'go for walks；walks along the river。','walks to school 把目的地接上，walks the dog 把被带去散步的动物接上。a walk 可以是散步这一活动，也可以是适合走的路线。',
 ('She walks to work whenever the weather is fine.','天气好时，她都会步行上班。'),('The guide describes several easy walks along the coast.','指南介绍了几条轻松的海岸步行路线。'),sources=['https://en.wiktionary.org/wiki/walks#English','https://en.wiktionary.org/wiki/walk#English'])
W('walked','英 /wɔːkt/；美 /wɔːkt, wɑːkt/','步行、散步了；带人走过；walk 的过去式和过去分词',
 '过去靠脚走过一段路，是 walked；陪人走到门口、带狗散步，也用这个动作。',
 'walk + -ed，/k/ 后词尾读 /t/，末尾是 /kt/。l 在常见标准读音中不发音；英语 walk 有较早本族移动、踩踏词的历史。',
 [['古英语相关形式 → 中古英语 walken → walk','移动、踩踏 → 步行'],['walk + -ed → walked','过去走过；陪着走、遛过']],
 'walked home 走回家；walked to the station 走到车站；walked me to the door 陪我走到门口；walked away 走开。',
 'had walked for hours；walked through the park。','walked home 通常直接接 home；walked to the house 用 to 接普通地点名词。walked someone somewhere 强调陪、带某人走到某处。',
 ('We walked home through the park.','我们穿过公园走回家。'),('She walked me to the station after lunch.','午饭后，她陪我走到了车站。'),sources=['https://en.wiktionary.org/wiki/walked#English','https://en.wiktionary.org/wiki/walk#English'])
W('acts','/ækts/','行为、举动；法令；戏剧的幕；行动、扮演、起作用',
 '做出来的一件事是 an act，多件就是 acts；人采取行动、扮演角色，也用同一个动词。法令和戏剧的一幕则各有专门用法。',
 'act + -s，形成 /kts/ 辅音连接。act 经法语等接拉丁 āctum、ācta 做成的事、法令，较早关联 agere 做、执行；英语名词与动词有相连的发展。',
 [['拉丁 agere、āctum／ācta → 法语、英语 act','做、做成的事 → 行为、法令等'],['act + -s → acts','多个行为、幕；单数主语行动、扮演']],
 'acts of kindness 善意举动；a play in three acts 三幕剧；acts as a guide 充当向导；acts on advice 按建议行动。',
 'acts quickly；small acts of generosity。','acts as 说明起什么作用、充当什么角色；acts on 说明根据什么行动。a play’s acts 是剧的幕，actors 是演员，两者都与做、演的词族相连。',
 ('Small acts of kindness made the newcomers feel welcome.','一个个小小的善意举动让新来的人感到受欢迎。'),('The old building now acts as a community centre.','那栋旧建筑现在用作社区中心。'),sources=['https://en.wiktionary.org/wiki/acts#English','https://en.wiktionary.org/wiki/act#English'])
W('acted','/ˈæktɪd/','行动了；扮演、表演过；起过作用；act 的过去式和过去分词',
 '事情真正做了出来，是 acted；在舞台上演出角色，或在某个场合担当一种作用，也能沿“做”的感觉理解。',
 'act + -ed，/t/ 后增加 /ɪd/。act 接拉丁 agere 的 āct- 词族，英语名词与动词分别发展，acted 是现代规则过去形式。',
 [['拉丁做、执行词族 → 法语、英语 act','行为、做事；后来也有表演等义'],['act + -ed → acted','过去行动、表演、发挥作用']],
 'acted quickly 迅速行动了；acted in a play 出演戏剧；acted as a guide 充当向导；acted on the advice 按建议行动了。',
 'had acted before；acted with care。','acted in 交代出演什么，acted as 交代担当什么角色、作用；acted on 交代依据什么行动。acted up 在口语中还可说孩子调皮、设备出毛病。',
 ('She acted in the school play last year.','她去年出演了学校的戏剧。'),('We acted on the advice of the local guide.','我们按照当地向导的建议行动。'),sources=['https://en.wiktionary.org/wiki/acted#English','https://en.wiktionary.org/wiki/act#English'])
W('serves','英 /sɜːvz/；美 /sɜːrvz/','服务；供应食物；起作用、用作；发球；serve 的第三人称单数',
 '为某个人、需要或任务做事，是 serves；餐馆供应饭菜、设备发挥用途、球员把球发出去，都要结合场景认。',
 'serve + -s，/v/ 后读 /z/。serve 经古法语 servir 接拉丁 servīre 服侍、效力，关联 servus 奴仆；现代服务、供应、发挥作用已有广泛普通用法。',
 [['拉丁 servus、servīre → 古法语 servir → serve','服侍、效力 → 服务、供应、起作用'],['serve + -s → serves','单数主语服务、供餐、发球等']],
 'serves lunch 供应午饭；serves customers 接待顾客；serves as a reminder 起提醒作用；serves the ball 发球。',
 'serves the local community；serves two purposes。','serves as ... 表示用作、起……作用；serves someone food 是给人端上食物。It serves two purposes 说同一个东西有两种用途，中文不必硬翻成服务两个目的。',
 ('The café serves lunch until three o’clock.','咖啡馆供应午饭到三点。'),('The photograph serves as a reminder of the trip.','这张照片让人想起那次旅行。'),sources=['https://en.wiktionary.org/wiki/serves#English','https://en.wiktionary.org/wiki/serve#English'])
W('offers','英 /ˈɒfəz/；美 /ˈɔːfərz, ˈɑːfərz/','提供、主动提出；提议、报价、优惠〔复数〕',
 '把别人可能需要的东西、提议带到面前，给对方选择，就是 offers；一项项这样的提议、优惠，也叫 offers。',
 'offer + -s，读 /z/。offer 动词有古英语 offrian 和法语影响，较早是拉丁 offerre，ob- 与 ferre 带、承载组成带到面前；名词也有法语 ofre 的借入分析。',
 [['拉丁 offerre → 古英语及法语相关路线 → offer','带到面前、呈献 → 提供、提议'],['offer + -s → offers','单数主语提出、提供；多个提议、优惠']],
 'offers help 主动提供帮助；offers to drive 主动提出开车；job offers 工作录用通知；special offers 特别优惠。',
 'offers a choice；compare the offers。','offers to do 是主动提出做，offers someone something 是给某人提供某物。an offer 往往还等待对方接受，不等于承诺内容已经兑现。',
 ('She offers to drive us to the station.','她主动提出开车送我们去车站。'),('The shop displays its special offers near the entrance.','商店在入口附近展示特别优惠。'),sources=['https://en.wiktionary.org/wiki/offers#English','https://en.wiktionary.org/wiki/offer#English'])
W('opens','英 /ˈəʊpənz/；美 /ˈoʊpənz/','打开；开始营业、开始活动；开放机会；open 的第三人称单数',
 '从关着、封着，变成能通过、能接触，是 opens；商店开始营业、故事展开、机会出现，也可以借这个开口的画面理解。',
 'open + -s，/n/ 后读 /z/。open 的形容词、相关动词有古英语 open 及早期动词形式的历史，不把结尾 en 当作现代临时拼上的使动尾。',
 [['古英语 open 及相关形式 → 中古英语、英语 open','敞开；打开、开放'],['open + -s → opens','单数主语打开；开始营业、展开']],
 'opens the door 开门；opens at nine 九点开始营业；opens with a question 以问题开场；opens up new possibilities 开辟新可能。',
 'opens easily；the shop opens tomorrow。','opens the shop 说有人开店门、经营开张等；the shop opens 说商店开门营业。opens with 交代开场内容，opens up 常强调让新的空间、机会出现。',
 ('The library opens at nine on weekdays.','图书馆工作日九点开门。'),('The story opens with a quiet scene beside the river.','故事以河边一个安静的场景开头。'),sources=['https://en.wiktionary.org/wiki/opens#English','https://en.wiktionary.org/wiki/open#English'])
W('closes','动词：英 /ˈkləʊzɪz/；美 /ˈkloʊzɪz/','关闭；结束；使距离缩小；close 的第三人称单数',
 '把开口合上，是 closes；活动到此收口、差距逐渐缩小，也沿这个合拢的感觉理解。',
 '动词 close + -s，原词以 /z/ 结尾，增加 /ɪz/，写作 closes。close 的关上词族经法语、拉丁 claudere／clausus 等传入，并有古英语相关动词影响。',
 [['拉丁关上词族及较早英语相关形式 → close 动词','关上、围住 → 结束、缩小间隔'],['close + -s → closes','单数主语关闭、结束；发音增加 /ɪz/']],
 'closes the window 关窗；closes at six 六点关门；closes the meeting 结束会议；closes the gap 缩小差距。',
 'closes slowly；the shop closes early。','关上这一动词 close 通常读 /kləʊz/，所以 closes 中有 /zɪz/；亲近的、距离近的形容词 close 常读 /kləʊs/。本条按关闭动词读。',
 ('The museum closes early on Sundays.','博物馆周日提早关门。'),('The new path closes the gap between the two routes.','新小路把两条路线连通了。'),sources=['https://en.wiktionary.org/wiki/closes#English','https://en.wiktionary.org/wiki/close#English'])
W('tests','/tests/','测试、考试；考验；检验、测试〔第三人称单数〕',
 '拿出一项检查，看看能力、品质或判断是否站得住，就是一个 test；多项检查是 tests，主动去检验也可用动词 tests。',
 'test + -s，末尾 /sts/ 连在一起，通常不加额外元音。test 的较早借词背景是法语及拉丁 testum 陶制容器，借词早期涉及检验金属用的器皿，后来扩大为一般检验。',
 [['拉丁陶器词 → 法语、英语 test；检验用器皿的用法','检验器皿 → 检验、考试'],['test + -s → tests','多项测试；单数主语检验']],
 'school tests 学校测验；quality tests 质量检验；tests a theory 检验理论；tests our patience 考验耐心。',
 'carry out tests；tests the equipment regularly。','tests 名词可以是题目测验，也可以是仪器、品质检验。动词 tests our patience 是把等待等情况比作对耐心的考验，语义比考试更宽。',
 ('The team carried out several tests on the new material.','团队对新材料做了几项测试。'),('The long wait tests everyone’s patience.','漫长的等待考验着每个人的耐心。'),sources=['https://en.wiktionary.org/wiki/tests#English','https://en.wiktionary.org/wiki/test#English'])
W('tested','/ˈtestɪd/','测试、检验过；经过检验的；经受考验的',
 '已经拿去试过、检查过，就是 tested；用来修饰方法、设计时，常强调经历过实际检验。',
 'test + -ed，/t/ 后增加 /ɪd/。test 从较早检验金属的器皿、检验名词发展到动词；tested 是英语规则过去形式和相应分词用法。',
 [['较早检验词族 → 英语 test 名词、动词','检验品质、能力或判断'],['test + -ed → tested','已经检验、试过；经历考验的']],
 'tested the equipment 测试过设备；a tested method 经过检验的方法；tested our patience 考验了耐心；tried and tested 久经考验的。',
 'carefully tested；has been tested。','tested 只说进行了检验，结果是否合格要看后文；a tried and tested method 常表达方法经过使用、比较可靠的评价。test results 则是检验结果。',
 ('We tested the equipment before the visitors arrived.','访客到来前，我们测试了设备。'),('The lesson uses a tried and tested method.','这节课采用了一种久经考验的方法。'),sources=['https://en.wiktionary.org/wiki/tested#English','https://en.wiktionary.org/wiki/test#English'])
def extend_lessons():
 extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_yb',ROOTS,WORDS)
 extend_lessons()
