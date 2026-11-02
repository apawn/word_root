"""Squander, splurge, skimp and scrimp: how much, and with what judgement."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
def S(word,base):
 return ['https://en.wiktionary.org/wiki/'+word+'#English','https://www.etymonline.com/word/'+base]
EXISTING_ROOT_ADDITIONS={
 'A1760':dict(words='squander squanders squandered squandering splurge splurges splurged splurging'.split(),label='squander 与 splurge：浪费掉，或大花一笔',note='squander 来源未定，较早已有挥霍与散布材料，不能硬造现代前后缀。splurge 先有炫耀排场名词，动词后来有大花钱义；或受 splash、surge 启发，但未证实为确定混成。'),
 'A1699':dict(words='skimp skimps skimped skimping skimpy'.split(),label='skimp 与 skimpy：少到不够',note='skimp 可能由 skimpy 逆构，或是 scrimp 的变体。现代可对应 skimp 与 -y 认形，但不能把短动词先学排成确定历史；skip 加 skim 的解释可能只是俗词源。'),
 'B2508':dict(words='scrimp scrimps scrimped scrimping'.split(),label='scrimp：给得不足，到东省西省',note='scrimp 接苏格兰少、不足的旧性质词，有北欧或大陆日耳曼收缩、干瘪材料等近源分析；和 shrink 可比较，不是现代英语 shrink 换字母造出来。'),
 'B2991':dict(words='stingy stinginess'.split(),label='stinginess：舍不得给的吝啬性质',note='stinginess 对应 stingy 把 y 改 i 加完整 -ness；stingy 的远源分析另看基础词，不因为能联想到刺痛就把现代 sting 接成已证实唯一来历。'),
 'C0750':dict(words='miser misers'.split(),label='misers：把钱攥得很紧的人',note='miser 借拉丁 miser 不幸、可怜等材料，英语后来专指吝啬者；复数直接加 -s，不把结尾 -er 当英语比较级。'),
 'B2984':dict(words='spendthrift spendthrifts'.split(),label='spendthrifts：把财富花掉的人',note='spend 加 thrift，thrift 在旧组合里联系财富、所得；不是现代节俭义加 spend 得到节俭花钱者。现代指挥霍的人。'),
}
SQUANDER=[['较早英语 squander：挥霍、散布等材料','远源未定，不硬拆现代前后缀'],['现代浪费金钱、机会、时间、优势','具体句子写失去原本可用的价值']]
SPLURGE=[['较早 splurge 名词：炫耀、排场','来源未定，或受 splash、surge 启发'],['名词 → 动词；后来大花钱、尽情享用','现代一次犒赏也可这样说，不全是批评']]
SKIMP=[['skimpy 与 scrimp 等少、不足材料 → skimp 的不同分析','可能逆构，或为变体；不是确定的 skip、skim 混成'],['现代 skimp、skimpy 对应动作与性质','省得不够，与量少、覆盖少的性质']]
SCRIMP=[['苏格兰 scrimp 少、不足的性质材料 → 动词','可能接北欧或大陆日耳曼收缩材料'],['使不足 → 少花、东省西省','现代常见 scrimp and save 的搭配']]
W('squander','英 /ˈskwɒndə/；美 /ˈskwɑndɚ/','挥霍、浪费掉金钱、机会等',
 '机会摆在眼前，却没好好用，最后白白没了，是 squander。钱、时间、天分、比赛领先都可以成为被浪费的对象。',
 '较早已有挥霍、散布等英语材料，远源未定。可以用把好东西散掉的画面理解，但不能给未知词源编出确定的古词根拆分。',SQUANDER,
 'squander money 挥霍钱；squander an opportunity 浪费机会；squander a lead 丢掉领先优势。',
 'squander time；squander talent；squander resources。',
 'squander 明确带没好好利用、白白浪费的批评，spend 只说花费；花一笔钱不自动等于挥霍。',
 ('Do not squander this chance to learn from her.','别白白浪费这次向她学习的机会。'),('The team managed to squander a two-goal lead.','球队竟把两球的领先优势丢掉了。'),sources=S('squander','squander'))
W('squanders','英 /ˈskwɒndəz/；美 /ˈskwɑndɚz/','挥霍、浪费掉〔第三人称单数〕',
 '他一次次把好机会耗掉，或把宝贵时间花在没必要的争论上，可以说 squanders。说话人是在评价这些价值没被好好利用。',
 'squander + -s，读 /z/；末尾原有的 er 是基础动词的一部分，不是本句另外加出一个做事者。',SQUANDER+[['squander + -s → squanders','他或它浪费掉原本可用的价值']],
 'squanders opportunities 白白错过机会；squanders his time 浪费时间。',
 'squanders resources；squanders an advantage 浪费优势。',
 'squanders an opportunity 是有机会却浪费，lacks an opportunity 是没机会；有无机会与有没有用好不同。',
 ('He squanders his talent on work he does not care about.','他把才华浪费在自己不在乎的工作上。'),('The committee squanders time arguing over tiny details.','委员会把时间浪费在争论细枝末节上。'),sources=S('squanders','squander'))
W('squandered','英 /ˈskwɒndəd/；美 /ˈskwɑndɚd/','挥霍、浪费掉了',
 '回头看，好机会已经过去，钱也没留下想要的成果，就是 squandered。这个词常让人感到本来可以做得更好。',
 'squander + 完整 -ed，读 /d/；过去式、过去分词，不新增 /ɪd/ 音节。',SQUANDER+[['squander + -ed → squandered','过去已把价值白白耗掉']],
 'squandered a fortune 挥霍大笔财富；squandered an opportunity 浪费机会。',
 'squandered the lead 丢掉领先；squandered years 白白耗掉多年。',
 'squandered 带可惜、浪费的评价，lost 本身更中性；输了比赛不一定因为挥霍机会。',
 ('They squandered a rare opportunity to resolve the dispute.','他们浪费了一次解决争端的难得机会。'),('The character squandered his inheritance within a year.','那个角色一年内就挥霍掉了遗产。'),sources=S('squandered','squander'))
W('squandering','英 /ˈskwɒndərɪŋ/；美 /ˈskwɑndərɪŋ/','正在挥霍、浪费掉',
 '一边拥有机会、时间，一边不断把它耗散出去，是 squandering。它写浪费进行中，而不只是最后结算损失。',
 'squander + -ing；英式在元音开头后缀前读出 r，现代过程形式不改变远源未定这一点。',SQUANDER+[['squander + -ing → squandering','不断浪费可用价值的过程']],
 'squandering money 挥霍钱；squandering a chance 浪费机会。',
 'squandering resources；squandering time on arguments。',
 'squandering 常是否定评价，using resources 只说使用资源；有没有得到值得的效果，需要由实际内容支持。',
 ('The report accused the organisers of squandering resources.','报告指责组织者浪费资源。'),('She worried that she was squandering her best years.','她担心自己正在白白耗掉最好的年华。'),sources=S('squandering','squander'))
W('splurge','英 /splɜːdʒ/；美 /splɝdʒ/','大花一笔；尽情享用；一次较奢侈的花费',
 '平时省着，这次决定吃顿好饭、买件一直想要的东西，可以说 splurge。语气常是偶尔放开一点，不一定在责骂自己。',
 '较早名词说炫耀、排场，来源未定，可能受 splash、surge 启发；动词后来发展出大花钱、尽情享用义，不能把猜测当成确定混成。',SPLURGE,
 'splurge on dinner 在晚饭上大花一笔；a small splurge 一次小小的奢侈消费。',
 'splurge on a new coat 花钱买件好外套；an occasional splurge。',
 'splurge 常可说一次享受，squander 明确批评浪费；花得比平时多，不自动等于没有价值。',
 ('We decided to splurge on a really good dinner.','我们决定花一笔，吃顿真正好的晚饭。'),('The concert ticket was my one splurge that month.','那张音乐会门票是我那个月唯一一次较奢侈的消费。'),sources=S('splurge','splurge'))
W('splurges','英 /ˈsplɜːdʒɪz/；美 /ˈsplɝdʒɪz/','大花一笔〔第三人称单数〕；偶尔的奢侈消费〔复数〕',
 '他平常自己做饭，但生日那天肯花钱吃好一点，是 splurges on a meal；一年几次这种享受，也可数成 splurges。',
 'splurge + -s，拼写加 -s，/dʒ/ 后读 /ɪz/；动词三单和名词复数同形。',SPLURGE+[['splurge + -s → splurges','他或她大花一笔；多次这样的消费']],
 'splurges on holidays 度假时大花钱；occasional splurges 偶尔的奢侈消费。',
 'splurges on a meal；small splurges 小小的享受。',
 'splurges on books 说在书上花得较放开，buys books 只说买书；是否超出平时开销，后者不说明。',
 ('He splurges on a special meal for his birthday.','生日时，他会花一笔吃顿特别的饭。'),('She allows herself a few small splurges each year.','她每年允许自己享受几次小小的奢侈。'),sources=S('splurges','splurge'))
W('splurged','英 /splɜːdʒd/；美 /splɝdʒd/','大花一笔、尽情享用了一次',
 '终于决定买张好座位的票、住一晚好酒店，过去做了这次额外花费，就能说 splurged。它往往带一点犒赏感。',
 'splurge 去 e 加完整 -ed，/dʒ/ 后读 /d/，不另加 /ɪd/ 音节；现代消费义接既有动词的发展。',SPLURGE+[['splurge + -ed → splurged','过去大花一笔、放开享用']],
 'splurged on tickets 花钱买好票；splurged on a hotel 住酒店花了一笔。',
 'splurged for the occasion 为这次场合放开花钱；splurged on a treat。',
 'splurged 常写一次较特别的花费，overspent 明确超出预算、适当范围；两种评价不能机械等同。',
 ('We splurged on front-row tickets.','我们花了一笔，买了前排票。'),('She splurged on a comfortable hotel after weeks of camping.','露营几周后，她花一笔住了家舒服的酒店。'),sources=S('splurged','splurge'))
W('splurging','英 /ˈsplɜːdʒɪŋ/；美 /ˈsplɝdʒɪŋ/','正在大花钱、尽情享用；额外放开消费',
 '本来可以挑普通款，这次愿意为自己喜欢的东西多花一点，是 splurging。重点是相对平时放开，而非钱一定多到惊人。',
 'splurge 去 e 加 -ing；动作过程也可作名词讨论一次放开消费。',SPLURGE+[['splurge + -ing → splurging','大花一笔、尽情消费的过程']],
 'splurging on a holiday 度假时放开花；splurging on a gift 花钱买件好礼物。',
 'an excuse for splurging 放开花一次的理由；splurging a little。',
 'splurging 是消费上放开，saving 是留下钱；一个人平时 saving，也可能偶尔 splurging。',
 ('They celebrated by splurging on a weekend away.','他们花一笔出去过周末，庆祝了一番。'),('She felt like splurging a little after finishing the project.','完成项目后，她想稍微花点钱犒赏自己。'),sources=S('splurging','splurge'))
W('skimp','/skɪmp/','少给、少花到不足；对该投入的东西省得过头',
 '菜里少得几乎找不到配料，或做事连检查时间都不肯给够，是 skimp。常见 do not skimp on…，就是这件事别省得太少。',
 '动词可能由 skimpy 逆构，或是 scrimp 的变体；另有较早 skimp 性质材料。形成分析不同，不硬定现代短动词一定先于形容词。',SKIMP,
 'skimp on ingredients 配料给不足；skimp on preparation 准备投入不足。',
 'skimp on detail 细节处理不足；skimp on time 时间给不够。',
 'skimp 常暗示省掉了本该需要的部分，save 更中性；节约而保持足量、质量，不一定是 skimp。',
 ('Do not skimp on the ingredients if you want the sauce to taste rich.','想让酱汁味道浓郁，配料就别给得太少。'),('We cannot skimp on the time needed to check the details.','核对细节需要的时间，我们不能省得不足。'),sources=S('skimp','skimp'))
W('skimps','/skɪmps/','少给、投入不足〔第三人称单数〕',
 '每份沙拉配料都只放一点点，或每次检查都匆匆带过，可以说 skimps。说话人觉得对方给得、做得不够。',
 'skimp + -s，/p/ 后读 /s/；基础词与 skimpy、scrimp 的较早关系有不同分析，现代三单这层清楚。',SKIMP+[['skimp + -s → skimps','他或它给量、投入不足']],
 'skimps on toppings 浇头给不足；skimps on preparation 准备不充分。',
 'never skimps on detail 从不在细节上省工；skimps on portions 分量给得小。',
 'skimps on portions 在批评分量不足，serves small portions 只描述分量小；语气评价不同。',
 ('The café never skimps on the toppings.','那家咖啡馆的浇头从不吝啬。'),('He skimps on preparation and then has to redo the work.','他准备不足，后来只好返工。'),sources=S('skimps','skimp'))
W('skimped','/skɪmpt/','少给、少投入到不足了',
 '前面为省一点时间没检查，后面出了错，就可说 skimped on checking。重点是当时投入低于需要，不只是最后结果不好。',
 'skimp + 完整 -ed，/p/ 后读 /t/；规则过去式、过去分词。',SKIMP+[['skimp + -ed → skimped','过去给量、投入不足']],
 'skimped on materials 材料用不足；skimped on time 时间投入不足。',
 'skimped on detail；had skimped on preparation。',
 'skimped 明确带不足、偷省的意思，reduced 只说减少；把不必要的部分减少，不一定会降低到不够。',
 ('They skimped on the materials, and the shelves felt flimsy.','他们材料用得不足，架子显得很不结实。'),('I had skimped on preparation and felt unready.','我准备投入不够，觉得自己没准备好。'),sources=S('skimped','skimp'))
W('skimping','/ˈskɪmpɪŋ/','正在少给、投入不足；省得不够的做法',
 '做饭、写作、准备工作，该用的材料、注意力、时间一直给不够，是 skimping。这个词常提醒读者看清被省掉的是什么。',
 'skimp + -ing；现代动作形式。不能把它和 skim 浏览、掠过按声音近似就当成同一动作。',SKIMP+[['skimp + -ing → skimping','给得太少、投入不足的过程']],
 'skimping on detail 细节投入不足；skimping on portions 分量给不足。',
 'skimping on ingredients；accused of skimping 被指给得不足。',
 'skimping on research 是研究做得不足，skimming a text 是快速浏览文本；近音词关注的动作不同。',
 ('The chef was criticised for skimping on the portions.','厨师因分量给得不足受到批评。'),('Skimping on research made the article less convincing.','研究做得不足，让文章不那么有说服力。'),sources=S('skimping','skimp'))
W('skimpy','/ˈskɪmpi/','少得不足的；衣料少、覆盖很少的',
 '盘子大，食物却只一点点，是 a skimpy portion；衣服用料、覆盖面积很少，也能说 skimpy。共同点是给出的量很少。',
 '与较早 skimp 少、不足的性质词相接，再有 -y；skimp 动词近源另有逆构或 scrimp 变体等分析。现代把 skimp、skimpy 配着认，不一定动词先、形容词后。',SKIMP+[['旧 skimp 性质材料 + -y → skimpy','量少、覆盖少的性质，不以现代学习顺序定历史']],
 'a skimpy portion 分量太少；a skimpy explanation 解释太单薄。',
 'skimpy clothing 覆盖很少的衣服；skimpy details 少得不够的细节。',
 'skimpy explanation 常批评内容少到不够，concise explanation 是解释简洁；短不等于信息不足。',
 ('The restaurant served rather skimpy portions.','那家餐馆给的分量相当少。'),('The guide offered only a skimpy explanation of the process.','指南对过程的解释只有薄薄几句，不够充分。'),sources=S('skimpy','skimpy'))
W('scrimp','/skrɪmp/','东省西省、节衣缩食；把花费压得很少',
 '这边少花一点，那边再省一点，把钱挤出来，是 scrimp。常用 scrimp and save，像把每一项开支都捏紧。',
 '接苏格兰少、不足的旧性质材料，有北欧或大陆日耳曼收缩、干瘪词等来源分析；先有较早性质词，再有使不足、节省动词用法。',SCRIMP,
 'scrimp and save 东省西省攒钱；scrimp on expenses 紧缩开支。',
 'scrimp to afford something 东省西省才负担得起；had to scrimp。',
 'scrimp and save 常突出过得节省、攒钱不易，skimp on something 更常批评某一项给得不足；语气焦点不同。',
 ('They had to scrimp and save to buy the house.','他们得东省西省，才买得起那栋房子。'),('We did not want to scrimp on food during the trip.','旅行时，我们不想在吃饭上省得太紧。'),sources=S('scrimp','scrimp'))
W('scrimps','/skrɪmps/','东省西省、紧缩花费〔第三人称单数〕',
 '每一笔小开支都尽量挤少一点，把余钱存起来，是 scrimps。它能让人感到钱得一点点省出来。',
 'scrimp + -s，/p/ 后读 /s/；较早不足、收缩材料形成的动词，现代加三单尾。',SCRIMP+[['scrimp + -s → scrimps','他或她设法把花费压低']],
 'scrimps and saves 东省西省攒钱；scrimps on small expenses 省小开销。',
 'scrimps for a holiday 为假期旅行省钱；scrimps to get by。',
 'scrimps 更突出紧巴巴地省，budgets 可以只是安排预算；收入充足的人也会做 budget，不一定 scrimp。',
 ('She scrimps and saves for an annual trip to see her family.','她东省西省，为一年一次探亲旅行攒钱。'),('He scrimps on small expenses to keep the workshop open.','他从小开支上省，维持车间经营。'),sources=S('scrimps','scrimp'))
W('scrimped','/skrɪmpt/','东省西省、紧缩花费了',
 '攒学费、攒旅行费的那段日子，一项项少花，过去这样省过就是 scrimped。常和 saved 连着说，强调钱来得不容易。',
 'scrimp + 完整 -ed，/p/ 后读 /t/；过去式、过去分词。',SCRIMP+[['scrimp + -ed → scrimped','过去节省、紧缩了花费']],
 'scrimped and saved 东省西省攒了钱；scrimped for years 节省多年。',
 'scrimped on comforts 在享受上省；scrimped to afford the fees。',
 'scrimped 不等于生活毫无安排，常说明资源紧、为了目标节省；wasted 则是把资源没用好。',
 ('They scrimped and saved for years to pay the fees.','他们东省西省多年，才付得起那些费用。'),('We scrimped on little luxuries during the renovation.','装修期间，我们把一些小享受都省掉了。'),sources=S('scrimped','scrimp'))
W('scrimping','/ˈskrɪmpɪŋ/','正在东省西省；紧缩花费的生活、做法',
 '眼下每一项开支都要挤着省，整段过程就是 scrimping。它可以写为目标攒钱的辛苦，不只是批评小气。',
 'scrimp + -ing；现代过程形式或活动名词，保留紧缩、给得少的基本性质。',SCRIMP+[['scrimp + -ing → scrimping','紧缩花费、东省西省的过程']],
 'scrimping and saving 东省西省攒钱；years of scrimping 多年节省。',
 'scrimping on comforts；tired of scrimping 不想再过得紧巴巴。',
 'scrimping 常是在钱上费力省，stinginess 更常批评不愿给、不愿分享；是否自愿、是否有余力，语境很重要。',
 ('After years of scrimping, they finally took a holiday.','东省西省多年后，他们终于度了一次假。'),('She was tired of scrimping on every small purchase.','每次小购物都要省来省去，让她厌倦了。'),sources=S('scrimping','scrimp'))
W('stinginess','/ˈstɪndʒinəs/','吝啬、小气；给得过少的性质',
 '有能力给，却总不肯给够、也不愿分享，说话人可以批评这种态度是 stinginess。与单纯没钱、必须节省不是一回事。',
 'stingy 把 y 改 i，加完整 -ness。stingy 的远源未定，可能接尖刻、刺痛的方言性质词；这层名词后缀清楚，不把猜测当作定论。',
 [['stingy：吝啬，较早来源分析未全定','或联系刺痛、尖刻的方言性质材料'],['stingy + -ness → stinginess','y 改 i，写吝啬的性质、表现']],
 'stinginess with money 在钱上小气；stinginess with praise 舍不得夸人。',
 'criticise someone’s stinginess；a reputation for stinginess 以小气闻名。',
 'stinginess 是偏负面的不愿给，thrift 常是正面的节省、不过度花；同样花得少，评价与动机不同。',
 ('His stinginess with praise discouraged the team.','他舍不得夸人，让团队很泄气。'),('The character’s stinginess becomes a source of comedy.','那个角色的小气成了喜剧笑点。'),sources=S('stinginess','stingy'))
W('misers','英 /ˈmaɪzəz/；美 /ˈmaɪzɚz/','守财奴、吝啬鬼〔复数〕',
 '钱明明攒了不少，却像一点也花不起那样死死攥着，文学里常把这样的人叫 misers。词带强烈批评，不只是善于记账。',
 'miser + -s，读 /z/；miser 借拉丁不幸、可怜的人等材料，英语后来专指囤钱吝啬者。结尾 -er 不是现代更的比较级。',
 [['拉丁 miser 不幸、可怜 → 英语 miser','较早不幸者义，后来专指囤钱吝啬者'],['miser + -s → misers','多个守财奴、吝啬者']],
 'wealthy misers 有钱却吝啬的人；misers in literature 文学里的守财奴。',
 'portray people as misers；a pair of misers 两个吝啬鬼。',
 'misers 批评死守钱、不肯花，savers 只说储蓄的人；储蓄习惯本身不等于守财奴。',
 ('The play mocks two wealthy misers who refuse to spend a penny.','戏剧嘲讽了两个一分钱也不肯花的有钱守财奴。'),('The essay compares famous misers in literature.','文章比较了文学中著名的守财奴形象。'),sources=S('misers','miser'))
W('spendthrifts','/ˈspendθrɪfts/','挥霍者、花钱无度的人〔复数〕',
 '拿到钱就放开花，把积蓄、财富不断耗掉的人，是 spendthrifts。名字里虽有 thrift，却不是夸他们花钱节俭。',
 'spendthrift + -s，/t/ 后读 /s/；内层 spend 花掉 + thrift 旧义财富、积蓄。这个旧含义解释了看似矛盾的组合。',
 [['spend + thrift 财富、积蓄 → spendthrift','把积蓄花掉的人'],['spendthrift + -s → spendthrifts','多个挥霍者']],
 'reckless spendthrifts 鲁莽挥霍者；spendthrifts in the family 家里花钱无度的人。',
 'describe people as spendthrifts；misers and spendthrifts 守财奴与挥霍者。',
 'spendthrifts 挥霍，thrifty people 节俭；历史组合选择 thrift 的旧财富义，现代形容词 thrifty 的常用义不能直接倒灌进去。',
 ('The novel contrasts misers with reckless spendthrifts.','小说对照描写了守财奴和鲁莽的挥霍者。'),('The brothers were known as spendthrifts who never kept their savings.','兄弟俩以花钱无度、从来存不住积蓄闻名。'),sources=S('spendthrifts','spendthrift'))
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_zhj',ROOTS,WORDS)
 extend_lessons()
