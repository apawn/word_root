"""Common plural families: seeds, allies, coaches and references to words."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'B3511':dict(words=['seed','seeds'],label='seed → seeds：播下的种子与后来生长的开端',note='古英语 seed 与 sow 同族，现代 s 数种子；体育种子选手是后来的比喻。'),
 'B4528':dict(words=['threat','threats'],label='threat → threats：逼近的危险与恐吓',note='古英语压力、困扰等材料，后来突出危险、威胁；现代复数 s。'),
 'C0672':dict(words=['ally','allies','alliance'],label='ally → allies：绑到同一阵线的人',note='拉丁 ad- 与 ligare，经法语到英语；名词、动词重音分别标。'),
 'B2561':dict(words=['church','churches'],label='church → churches：建筑与信众团体',note='日耳曼早期借入希腊属于主的建筑名称，再传古英语。'),
 'B4219':dict(words=['border','borders'],label='border → borders：围在外沿的边与界线',note='法语边缘词族借入，复数也可与动词三单同形。'),
 'B3679':dict(words=['coach','coaches'],label='coach → coaches：载人的车与带人进步的教练',note='车辆名称接匈牙利地名 Kocs；教练义由辅导学生的比喻发展。'),
 'C0287':dict(words=['coin','coins'],label='coin → coins：从压印工具到硬币',note='法语接拉丁 cuneus 楔子，工具、压印义转到钱币。'),
 'C0386':dict(words=['error','errors'],label='error → errors：从走偏到出错',note='拉丁 errare 到 error，法语借入；or 是历史名词材料而非犯错者后缀。'),
 'B3157':dict(words=['gain','gains'],label='gain → gains：得到的收益与取得进步',note='名词与北欧、法语背景相连，动词也接法语 gagner；保留不同路径。'),
 'B3605':dict(words=['guideline','guidelines'],label='guideline → guidelines：先画参照线，再定指导原则',note='guide 与 line 的英语组合，从实物操作参照线扩到做事指导。'),
 'C0751':dict(words=['promise','promises'],label='promise → promises：把将来要做的事先说出来',note='法语 promesse 接拉丁 promittere、promissum；s 的复数和三单分别读句子。'),
 'C1196':dict(words=['quote','quotes'],label='quote → quotes：引用原话与报出价格',note='拉丁编号、标注章节到法语、英语，再有引述与报价分支。'),
}
W('seeds','/siːdz/','种子；起因、萌芽；种子选手〔复数〕；播种〔第三人称单数〕',
 '一粒小东西，给它条件就会长成后来的大东西：seeds 可以是真种子，也可以是一件事情刚开始的苗头。体育里还指签表中的种子选手。',
 'seed + -s，/d/ 后读 /z/。seed 接古英语 sēd、sǣd，与 sow 播种同族。体育义把强手分散安排进签表，后有种子选手称呼。',
 [['古英语播种、种子材料 → seed','能播下并长出的东西'],['seed + -s → seeds','多粒种子；多个开端；多位种子选手；也可标动词三单']],
 'plant seeds 播种；the seeds of doubt 怀疑的萌芽；the top seeds 头号、领先的种子选手。',
 'sunflower seeds 葵花籽；sow the seeds of change 播下变革的种子。',
 'seeds 强调能发展出后果的起点；roots 常强调已经扎下去、支撑或形成问题的根。种子选手由比赛安排产生，并非年纪小的选手。',
 ('We planted the seeds in small pots.','我们把种子种进小花盆。'),('That conversation planted the seeds of a new idea.','那次谈话埋下了一个新想法的种子。'),sources=['https://en.wiktionary.org/wiki/seeds#English','https://en.wiktionary.org/wiki/seed#English'])
W('threats','/θrets/','威胁、危险；恐吓的话或行为〔复数〕',
 '有些危险正在逼近，有些人扬言要让坏事发生：两者都能叫 threats。前者不一定有人故意做，后者有明确的恐吓意味。',
 'threat + -s，/t/ 后读 /s/。古英语 þrēat 的人群、压力、困扰等旧义，经中古英语发展到现代的危险、恐吓。',
 [['古英语 þrēat → 中古英语 thret 等 → threat','压力、困扰 → 威胁、危险'],['threat + -s → threats','多种危险；多次、多个恐吓']],
 'threats to wildlife 对野生动物的威胁；make threats 发出恐吓；empty threats 虚张声势的威胁。',
 'potential threats 潜在威胁；take threats seriously 认真对待威胁。',
 'threats 是名词；threatens 是动词 threaten 的三单。threats to something 是对它的危险，threats from someone 说明威胁来自谁。',
 ('The report identifies several threats to the forest.','报告指出了森林面临的几种威胁。'),('The manager would not respond to empty threats.','经理不愿理会那些虚张声势的威胁。'),sources=['https://en.wiktionary.org/wiki/threats#English','https://en.wiktionary.org/wiki/threat#English'])
W('allies','名词 /ˈælaɪz/；动词常读 /əˈlaɪz/','盟友、支持者〔复数〕；与……结盟〔第三人称单数〕',
 '为了某个共同目标，愿意站到同一边的人，就是 allies。他们可能相处很好，也可能只在这一件事上需要彼此。',
 'ally 以辅音字母加 y 结尾，改 y 为 i 加 -es：allies，末尾读 /z/。历史接拉丁 ad- + ligare 绑 → alligare，经古法语 alier 到 ally。',
 [['拉丁 alligare → 古法语 alier → 英语 ally','绑在一起 → 联合、结盟'],['ally → allies','盟友不止一位；或动词主语为第三人称单数']],
 'close allies 关系密切的盟友；allies in a campaign 同一行动中的支持者；ally oneself with someone 与某人联合。',
 'find allies 找到支持者；work with allies 与盟友合作。',
 'allies 说明共同立场或合作关系；friends 更强调友谊。名词重音在前，动词常在后；拼写一样仍要看句中的角色。',
 ('The campaign gained allies among local teachers.','这项行动在当地教师中赢得了支持者。'),('The two countries remained allies despite their differences.','两国尽管存在分歧，仍然保持盟友关系。'),sources=['https://en.wiktionary.org/wiki/allies#English','https://en.wiktionary.org/wiki/ally#English'])
W('churches','英 /ˈtʃɜːtʃɪz/；美 /ˈtʃɜːrtʃɪz/','教堂；教会、教会团体〔复数〕',
 '数的是建筑时，churches 是几座教堂；数的是组织和信众共同体时，就是几个教会。墙与人群这两个焦点，需要从上下文分清。',
 'church + -es，/tʃ/ 后加一个 /ɪz/ 音节。church 由古英语 ċiriċe 等传下来，更早是日耳曼语言借入希腊 kuriakon 属于主的建筑相关名称。',
 [['希腊属于主的建筑名称 → 日耳曼语言 → 古英语 ċiriċe → church','建筑名称，也发展为信众组织名称'],['church + -es → churches','多座教堂；多个教会团体']],
 'village churches 村庄教堂；local churches 当地教堂、教会；different churches 不同教会。',
 'old stone churches 古老石教堂；churches in the town 镇上的教堂或教会。',
 'the churches were built 指建筑；the churches worked together 通常指组织或信众。不是每个出现 churches 的句子都只在谈房子。',
 ('Several old churches stand near the river.','河边有几座古老的教堂。'),('Local churches worked together to collect warm clothes.','当地几个教会合作募集保暖衣物。'),sources=['https://en.wiktionary.org/wiki/churches#English','https://en.wiktionary.org/wiki/church#English'])
W('borders','英 /ˈbɔːdəz/；美 /ˈbɔːrdərz/','边界、边缘、装饰边〔复数〕；与……接壤〔第三人称单数〕',
 '沿着外圈划一条线：地图上成了边界，布料或页面上成了装饰边。动词则说某地挨着另一处，边碰着边。',
 'border + -s，末尾读 /z/。border 经法语 bordeure、中古英语 bordure 等进入，属于边缘词族；现代 er 不表示某种职业。',
 [['法语边缘词 → 中古英语 bordure → border','物体外沿 → 地区界线；也作接壤动词'],['border + -s → borders','多条边界、装饰边；或某地与……接壤']],
 'cross borders 跨越边界；national borders 国界；decorative borders 装饰边。',
 'The town borders a lake. 这座镇子紧挨着一个湖。',
 'borders 在 national borders 中是名词，在 the town borders 中是动词。boundary 也指界线；border 常还可以指边界地带和外沿。',
 ('The quilt has colourful borders.','这条被子有彩色的边饰。'),('The park borders a quiet residential area.','公园与一片安静的住宅区相邻。'),sources=['https://en.wiktionary.org/wiki/borders#English','https://en.wiktionary.org/wiki/border#English'])
W('coaches','英 /ˈkəʊtʃɪz/；美 /ˈkoʊtʃɪz/','教练、辅导者；长途客车、车厢〔复数〕；指导、训练〔第三人称单数〕',
 'coach 最早载人从一处到另一处；后来学生把帮自己过考试的辅导者也比作一辆载人前进的车。coaches 就能数教练，也能数车辆。',
 'coach + -es，/tʃ/ 后读 /ɪz/。车辆名经法语、德语等语言接匈牙利 kocsi，名称联系地名 Kocs；教练义是英语后来的比喻。',
 [['匈牙利地名相关车辆名称 → 法语、德语等 → coach','载人的车'],['辅导过关的比喻 → 教练；coach + -es → coaches','多位教练、多辆车；也可表示某人指导']],
 'football coaches 足球教练；a line of coaches 一排长途客车；she coaches beginners 她指导初学者。',
 'experienced coaches 有经验的教练；coaches a school team 训练一支校队。',
 '现代教练并不一定开车；两义共享词史，不共享每个场景。车辆含义还会随英美用法和交通体系变化。',
 ('The coaches discussed the team’s training plan.','教练们讨论了队伍的训练计划。'),('Two coaches waited outside the hotel.','两辆长途客车等在酒店外。'),sources=['https://en.wiktionary.org/wiki/coaches#English','https://en.wiktionary.org/wiki/coach#English'])
W('coins','/kɔɪnz/','硬币〔复数〕；创造新词、新说法〔第三人称单数〕',
 '把金属压上统一的图案，成了一枚枚硬币；把一个新说法定出形来，也能用 coin。这是实体压印到语言创造的扩展。',
 'coin + -s，/n/ 后读 /z/。coin 经古法语 coing、coigne 接拉丁 cuneus 楔子，名称从压印工具转到钱币；英语动词再由名词发展。',
 [['拉丁 cuneus → 古法语 coing 等 → coin','楔子、压印工具 → 压出的金属钱币'],['coin + -s → coins','多枚硬币；也可标某人创造新词']],
 'collect coins 集硬币；a handful of coins 一把硬币；coin a phrase 创造、使用一个说法。',
 'old coins 旧硬币；coins a new term 创造一个新术语。',
 'coins 一般是金属货币；notes、bills 常指纸钞。动词 coin 的宾语若是 term、phrase，通常是在造词、造说法。',
 ('She put a few coins in the machine.','她往机器里投了几枚硬币。'),('The novelist often coins new words for imaginary objects.','这位小说家常为想象中的物品创造新词。'),sources=['https://en.wiktionary.org/wiki/coins#English','https://en.wiktionary.org/wiki/coin#English'])
W('errors','英 /ˈerəz/；美 /ˈerərz/','错误、差错；〔测量等〕误差〔复数〕',
 '原本有一个正确方向或正确结果，实际却偏开了：一处拼写错、一笔记录错、一次计算偏差，都能成为 errors。',
 'error + -s，末尾读 /z/。法语 error 接拉丁 error、errorem，与 errare 走偏相关；error 是错误这件事，不是犯错的人。',
 [['拉丁 errare → error → 法语、英语 error','走偏 → 判断、操作等偏离正确结果'],['error + -s → errors','多处错误；多项测量等误差']],
 'spelling errors 拼写错误；correct errors 改正错误；measurement errors 测量误差。',
 'check for errors 检查是否有错误；errors in the report 报告中的错误。',
 '日常 errors 与 mistakes 常有重叠；专业误差还可能有明确的测量、统计定义，不能一律理解为某人粗心。',
 ('Please check the names for spelling errors.','请检查姓名中有没有拼写错误。'),('The team corrected several errors in the table.','团队改正了表格里的几处错误。'),sources=['https://en.wiktionary.org/wiki/errors#English','https://en.wiktionary.org/wiki/error#English'])
W('gains','/ɡeɪnz/','收益、增加、进步〔复数〕；获得、增加〔第三人称单数〕',
 '原先少一点，现在多一点；原先做不到，现在更接近做到了。增加出来、进步出来的部分，就是 gains。动词则把“获得、增长”这件事说出来。',
 'gain + -s，/n/ 后读 /z/。gain 的名词有北欧 gagn 与法语相应名词的历史背景，取得动词也接法语 gagner 等；不把全部用法说成一条单一路线。',
 [['北欧、法语相关材料 → gain 的名词、动词路径','所得、好处；取得、增加'],['gain + -s → gains','多项所得、进步；或第三人称主语取得、增长']],
 'make gains 取得进步；small gains 小幅进展；gains in efficiency 效率提升。',
 'short term gains 短期收益；gains confidence 逐渐获得信心。',
 'gains 可以是钱，也可以是能力、效率、支持度的提升。看后面的 in、宾语或上下文，才知道增加的是什么。',
 ('The new design brought small gains in efficiency.','新设计带来了小幅的效率提升。'),('A beginner gains confidence through regular practice.','初学者通过经常练习逐渐建立信心。'),sources=['https://en.wiktionary.org/wiki/gains#English','https://en.wiktionary.org/wiki/gain#English'])
W('guidelines','/ˈɡaɪdlaɪnz/','指导原则、指南、操作指引〔复数〕',
 '做事前先有几条参照线，沿着它走就不容易偏。guidelines 把这幅实物画面搬到工作、写作和操作中，告诉你通常怎样做。',
 'guide + line → guideline，再加 -s → guidelines，末尾 /z/。较早 guideline 可指操作时的实体参照线，后扩为抽象指导原则。',
 [['guide + line → guideline','引导用的一条参照线'],['实体参照 → 做事指导；guideline + -s → guidelines','多条指导原则或一套操作指引']],
 'follow the guidelines 遵循指引；clear guidelines 清楚的指导原则；guidelines for authors 作者须知。',
 'design guidelines 设计指引；read the guidelines before starting 开始前阅读指南。',
 'guidelines 通常在指导怎样做；rules、requirements 更直接说规则、要求。具体文件是否必须遵守，仍要看它的明文规定。',
 ('The editor sent us the submission guidelines.','编辑把投稿须知发给了我们。'),('These guidelines help new staff prepare clear reports.','这些指引帮助新员工写出清楚的报告。'),sources=['https://en.wiktionary.org/wiki/guidelines#English','https://en.wiktionary.org/wiki/guideline#English'])
W('promises','英 /ˈprɒmɪsɪz/；美 /ˈprɑːmɪsɪz/','承诺〔复数〕；许诺；预示有希望〔第三人称单数〕',
 '事情还没有做，先把“我会做到”说出来，是一个 promise。promises 可以数这些承诺；也可以说某个人正在许诺，或某件事显出好的前景。',
 'promise + -s，原词末尾 /s/ 后读 /ɪz/，多一个音节。promise 借古法语 promesse，接拉丁 promittere 预先表示、承诺及 promissum 等。',
 [['拉丁 promittere、promissum → 古法语 promesse → promise','预先作出表示 → 承诺'],['promise + -s → promises','多项承诺；或某人许诺、某事预示有希望']],
 'keep promises 守信；break promises 违背承诺；promises to return 答应回来；promises well 预示前景不错。',
 'make promises 作承诺；empty promises 空头承诺。',
 'promises 在 he promises to help 中是动词，在 his promises 中是名词。许诺不等于事情已经完成；语法上先分清人在说什么。',
 ('She keeps her promises, even when it is inconvenient.','即使不方便，她也会守住承诺。'),('The new design promises to make the tool easier to use.','新设计有望让这个工具更好用。'),sources=['https://en.wiktionary.org/wiki/promises#English','https://en.wiktionary.org/wiki/promise#English'])
W('quotes','英 /kwəʊts/；美 /kwoʊts/','引文、引用的话；报价；引号〔复数〕；引用、报价〔第三人称单数〕',
 '把别人原来的一句话原样拿出来，是 quotes 的一支；把愿意收取的价格报出来，是另一支。写字时圈住引文的引号，也能口语叫 quotes。',
 'quote + -s，/t/ 后读 /s/。quote 接法语 coter、中世纪拉丁 quotare 编号、标注章节，更早 quotus 第几个；标出处再取用原话，后来也有报价等用法。',
 [['拉丁 quotare → 法语 coter → 英语 quote','编号、标注出处 → 引用；另发展报价'],['quote + -s → quotes','多条引文、多份报价、引号；也可标引用动词三单']],
 'quotes from a book 书中引文；get three quotes 取得三份报价；put a word in quotes 给一个词加引号。',
 'famous quotes 名言；she quotes a poem 她引用一首诗。',
 'quotes 若出现在供应商、维修等语境，可能是报价；出现在文章语境，多指引文。quotation 是对应的较完整名词。',
 ('The article includes two quotes from the interview.','文章引用了采访中的两段话。'),('We asked three firms for quotes on the repair work.','我们请三家公司为维修工作报价。'),sources=['https://en.wiktionary.org/wiki/quotes#English','https://en.wiktionary.org/wiki/quote#English'])
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_zw',ROOTS,WORDS)
 extend_lessons()
