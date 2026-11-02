"""Common short words: gestures, legal pursuit, engines, profiles and money names."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EU='https://european-union.europa.eu/institutions-law-budget/euro/design_en'
def S(word,base):
 urls=['https://en.wiktionary.org/wiki/'+word+'#English']
 if base=='intel':urls.append('https://www.merriam-webster.com/dictionary/intel')
 elif base=='euro':urls.append(EU)
 else:urls.append('https://www.etymonline.com/word/'+base)
 return urls
EXISTING_ROOT_ADDITIONS={
 'B3350':dict(words='pat pats patted patting'.split(),label='pat：另源的轻拍、鼓励；恰到好处与过于现成',note='与 tap 比较轻触，不由 tap 派生。pat 旧击打名词可能拟声，动词后来常指轻拍；pat of butter 是成形小块，a pat on the back 也借给鼓励。pat 回答现成、过顺另有命中要点到恰当等用法发展。'),
 'C1317':dict(words='sue sues sued suing'.split(),label='sue：跟随、追求一条线到法律追究',note='经法语 suer、suivre 等词线接拉丁 sequi 跟随；跟着一件事追下去的画面联系法律追究。现代 sue someone for damages 中，直接对象是被起诉的一方，for 后是索求等内容。'),
 'B4181':dict(words='rev revs revved revving'.split(),label='revolution → rev → revved、revving：转动到提高转速',note='rev 先缩略 revolution 一转、转数相关名词，再形成提高引擎转速的动词；不是现代 re- 再次加 v。短元音单音节词尾 v 接 -ed、-ing 时双写。'),
 'C0122':dict(words='bio bios'.split(),label='biography → bio → bios：传记到个人简介',note='bio 在简介语境缩略 biography，而 biography 接希腊 bios 生命 + graphia 记录等材料；现代简介复数 bios 是 bio + -s，不能只因字母相同就等同古希腊 bios 原词。'),
 'C0659':dict(words='intel'.split(),label='intelligence → intel：信息、情报的短称',note='intel 缩略 intelligence 的情报、信息一义，较远同接拉丁理解、分辨等词族；不把 intelligence 的智力、聪明等全部意思搬给缩略词。'),
 'B2538':dict(words='euro euros'.split(),label='euro → euros：欧洲货币名称及其英语复数',note='与 money 比较货币，不从 money 派生。euro 与 Europe、European 的名称材料相关，1995 年马德里会议确定名称；英语日常常用复数 euros，正式文件中也可见不变形式。'),
 'B2571':dict(words='sterling'.split(),label='sterling：银币、足值 → 英镑、优良可靠',note='与 silver 比较银和钱币，不从 silver 派生。sterling 早期指英国银便士，远源有星形币图加小称 -ling 等分析但不确定；足值、符合标准再引申为出色、可靠。'),
 'B2627':dict(words='phoenix phoenixes'.split(),label='phoenix：不死鸟 → 浴火重生的比喻',note='和 bird 比较神话鸟类，并非 bird 派生。英语经拉丁 phoenix、phenix 及希腊 phoinix 等，古英语、法语也见 fenix。灰烬中重生的传说形象借给事业、组织重新兴起。'),
}
PAT=[['英语 pat 旧击打名词，可能拟声 → 动词击打、轻拍','现代先学轻轻拍下的动作，不能倒写成最早只表示温柔轻拍'],['轻拍背部 → 鼓励；拍成的小块 → pat of butter','另有命中、恰当相关用法，pat answer 可表示过于现成的答案']]
SUE=[['拉丁 sequi 跟随 → 通俗拉丁、古法语相关形式','法语 suer、suivre 等含追随、继续及法律追究用法'],['英语 sue：旧时跟随、追求 → 现代起诉、请求','现代先掌握起诉义，不等于远源是英语 court']]
REV=[['revolution 转动、一转等名词 → 缩略 rev','这里缩的是机械转动一义，不把政治革命的含义整体搬来'],['rev 名词 → rev 动词：提高引擎转速','rev up 再比喻活动、需求等升温、加强']]
BIO=[['希腊 bios 生命 + graphia 记录等 → biography','描述一个人的一生'],['biography → bio：传记、个人简介','短称进入作者介绍、社交账号简介等现代场景']]
EURO=[['Europe、European 的名称材料 → euro 货币名','1995 年在马德里会议确定名称'],['英语 euro → 复数 euros','现代英语日常数量用法，不据旧词源猜实时汇率']]
PHOENIX=[['希腊 phoinix → 拉丁 phoenix、phenix；古英语、法语 fenix 等','后来英语 ph、oe 等拼写向古典形式靠拢'],['神话中灰烬重生的不死鸟 → 重建、复兴的比喻','不同神话传统有差别，不与中文凤凰的全部传统硬等同']]
W('pat','英、美 /pæt/','轻拍；轻拍动作；小块；〔答案等〕过于现成的',
 '手掌在肩上、狗头上轻轻拍一下，是 pat。a pat on the back 也能是口头鼓励，像不用真的拍背，也给对方一点肯定。',
 '旧名词 pat 表击打，可能拟声；动词由名词形成，后来轻拍义变常见。pat of butter 是拍成的小块，形容词 pat 的恰当、过于现成又有自己的用法发展。',PAT,
 'pat a dog 是轻拍狗；a pat on the back 是鼓励；a pat of butter 是一小块黄油；a pat answer 有时嫌回答太顺、太现成，未认真思考。',
 'pat a dog；a pat on the back；a pat of butter；a pat answer。',
 'pat 通常比 slap 轻；pet a dog 常是抚摸、爱抚，pat 则更突出一下下轻拍的动作。',
 ('She gave the dog a gentle pat.','她轻轻拍了拍狗。'),('Everyone deserves a pat on the back for finishing on time.','大家按时完成了，值得得到一点肯定。'),('His explanation sounded a little too pat.','他的解释显得有点过于现成、顺口了。'),sources=S('pat','pat'))
W('pats','英、美 /pæts/','轻拍〔第三人称单数〕；轻拍动作、小块〔复数〕',
 '她轻拍狗头，是 she pats the dog；几下轻拍，或几小块黄油，也能是 pats。按宾语和搭配判断数的是动作还是小块。',
 'pat + -s → pats，/t/ 后后缀读 /s/；名词复数与动词第三人称单数同形。',PAT+[['pat + -s → pats','单数主体轻拍；或多个轻拍动作、小块']],
 'pats the dog 是轻拍狗；gentle pats 是轻拍动作；pats of butter 是几小块黄油。',
 'pats the dog；gentle pats；pats of butter。',
 'pats 不是 patted 的过去形式；单数主语现在时用 pats，过去动作则用 patted。',
 ('He pats the dog before leaving for work.','他上班前轻轻拍拍狗。'),('The waiter brought bread and two small pats of butter.','服务员端来面包和两小块黄油。'),sources=S('pats','pat'))
W('patted','英、美 /ˈpætɪd/','轻拍了；拍平了〔过去式、过去分词〕',
 '肩上轻轻落下一只手，拍了两下，是 patted。手掌也能把软材料拍平、拍到位，动作仍是轻拍施压。',
 'pat 双写 t + -ed → patted，短元音单音节后双写；/t/ 后 -ed 读 /ɪd/，多一个音节。',PAT+[['pat 双写 t + -ed → patted','过去式、过去分词；读 /ˈpætɪd/']],
 'patted someone on the shoulder 是拍拍肩；patted the dough flat 是把面团拍平。flat 说明轻拍后的结果。',
 'patted his shoulder；patted the dough flat；patted the dog。',
 'pat someone on the shoulder 中 on 后通常用 the shoulder；也能直接说 pat someone’s shoulder，结构不同但动作相近。',
 ('She patted him on the shoulder.','她轻轻拍了拍他的肩膀。'),('He patted the dough flat with his hands.','他用手把面团拍平了。'),sources=S('patted','pat'))
W('patting','英、美 /ˈpætɪŋ/','正在轻拍；拍平的过程',
 '手掌轻轻起落，给人安慰或把软材料压到位，是 patting。动作不是持续摩擦，而是一下下接触。',
 'pat 双写 t + -ing → patting；分词、动名词保留基础短元音的拼写关系。',PAT+[['pat 双写 t + -ing → patting','现在分词、动名词；轻拍过程']],
 'patting a dog 是轻拍狗；patting someone’s back 是拍拍背；patting a surface dry 是轻拍吸干表面水分。',
 'patting the dog；patting his shoulder；patting the dough flat。',
 'patting 是拍，rubbing 是来回摩擦；两者手部动作不同，不能只因为都碰到表面就互换。',
 ('She sat beside him, patting his shoulder.','她坐在他身边，轻轻拍着他的肩膀。'),('He was patting the dough into a round shape.','他正把面团拍成圆形。'),sources=S('patting','pat'))
W('sue','英 /suː/，也可 /sjuː/；美 /suː/','起诉、控告；〔sue for〕请求、寻求',
 '一件事不肯就此放下，转去法院继续追究，可以说 sue。词源里的“跟下去、追下去”，帮助理解这个法律动作。',
 '经古法语 suer、suivre 等词线接拉丁 sequi 跟随；英语旧义包括跟随、追求，法律义沿追究一件事的关系发展。',SUE,
 'sue a company 是起诉一家公司；sue someone for damages 是起诉某人要求赔偿；sue for peace 是请求和平，后者保留寻求、请求义。',
 'sue a company；sue for damages；sue for peace。',
 'sue someone 直接接被起诉的一方，不写 sue against someone；for 后可接索赔、原因等。Sue 大写也可为人名，另有来源。',
 ('The company threatened to sue the publisher.','公司威胁要起诉出版商。'),('The novel describes a defeated ruler trying to sue for peace.','小说描写一位战败统治者试图请求和平。'),sources=S('sue','sue'))
W('sues','英 /suːz/，也可 /sjuːz/；美 /suːz/','起诉；请求〔第三人称单数〕',
 '报道说某公司起诉另一方，主语单数时可以用 sues。它把一个正在叙述、经常发生或标题概述的动作放到现在形式。',
 'sue + -s → sues，基础词已有 e，再加 s；元音后后缀读 /z/，没有额外 /ɪz/ 音节。',SUE+[['sue + -s → sues','第三人称单数；末尾 /uːz/']],
 'sues the company 是起诉公司；sues for damages 是起诉索赔。标题里现在时可概述刚发生的事件，具体时间看正文。',
 'sues the publisher；sues for damages；sues her former employer。',
 'sues 不是苏这个人名的所有格；Sue’s 才带撇号表示相应所有格或缩写，虽然读音可能相同。',
 ('In the film, she sues the company that copied her design.','电影里，她起诉了抄袭自己设计的公司。'),('The company sues competitors over copied designs.','公司因设计被抄袭而起诉竞争对手。'),sources=S('sues','sue'))
W('sued','英 /suːd/，也可 /sjuːd/；美 /suːd/','起诉了；被起诉〔过去式、过去分词〕',
 '已经把争议带去法院追究，是 sued；被对方起诉，则说 was sued。形式相同，主动和被动把双方位置换开。',
 'sue 去末尾 e + -ed → sued，元音后 -ed 读 /d/；不是在读音里额外加 /ɪd/。',SUE+[['sue 去 e + -ed → sued','规则过去式、过去分词；后缀 /d/']],
 'sued the company 是起诉了公司；was sued by 是被某方起诉；sued for damages 是起诉索赔。',
 'sued the company；was sued by；sued for damages。',
 'sued 说明起诉发生，不表示已经胜诉。won the case 才说明在诉讼结果上赢了，两个动词关注阶段不同。',
 ('The designer sued the retailer over an unpaid bill.','设计师因一笔未付账款起诉了零售商。'),('The newspaper reported that the company had been sued.','报纸报道该公司已经被起诉。'),sources=S('sued','sue'))
W('suing','英 /ˈsuːɪŋ/，也可 /ˈsjuːɪŋ/；美 /ˈsuɪŋ/','正在起诉；起诉行为',
 '谈当前正发生的起诉，或把起诉当成一件事讨论，用 suing。它不是“赢官司”的分词，仍只说追究这一行为。',
 'sue 去末尾 e + -ing → suing，u 与后面的 i 分属读音部分；不写 sueing。',SUE+[['sue 去 e + -ing → suing','现在分词、动名词，读音保留 /uː/ 加 /ɪŋ/']],
 'be suing someone 是正在起诉某人；suing for damages 是起诉索赔；by suing 是通过提起诉讼。',
 'suing the company；suing for damages；the cost of suing。',
 'suing someone 是主动；being sued 是被动。-ing 本身没有决定谁起诉谁，需要连着主语和被动结构看。',
 ('The artist is suing a dealer over a missing painting.','艺术家正因一幅失踪画作起诉经销商。'),('The documentary examines the cost of suing a large corporation.','纪录片讨论了起诉大型公司的成本。'),sources=S('suing','sue'))
W('rev','英、美 /rev/','提高引擎转速；转数、转速〔常见于 revs〕',
 '车还没往前走，引擎已经嗡地转快，是 rev the engine。这个短词抓的是“转”，不直接等于车速一定变快。',
 '先缩略 revolution 的一转、转数相关名词，再形成 rev 动词。更远 revolution 接拉丁回转词族；缩略词没有保留政治革命的全部含义。',REV,
 'rev the engine 是提高引擎转速；rev up 也可比喻把活动、热情加强。高转速不保证车辆当时就在高速移动。',
 'rev the engine；rev up；engine revs。',
 'Rev. 放在人名前可缩略 Reverend 牧师等尊称；本词机械意义的 rev 是 revolution 缩略，来源与用法分开。',
 ('There is no need to rev the engine while the car is parked.','车停着时，没必要让引擎高速空转。'),('The organisers hope to rev up interest in the event.','组织者希望让大家对活动的兴趣升温。'),sources=S('rev','rev'))
W('revs','英、美 /revz/','引擎转数、转速；提高转速〔第三人称单数〕',
 '看仪表上的引擎转速，日常可说 the revs。它数的是机械转动，不是车在路上行驶了多远。',
 'rev + -s → revs，/v/ 后后缀读 /z/；名词复数常用于转速说法，也可作动词第三人称单数。',REV+[['rev + -s → revs','转数、转速相关复数；或单数主体提高转速']],
 'high revs 是高转速；the revs rise 是转速升高；she revs the engine 是她让引擎转快。',
 'high revs；engine revs；revs the engine。',
 'revs 和 road speed 不是同一个量；车辆静止、空挡等语境里，引擎转数也可能增加。这里先区分词义，不靠声音猜车速。',
 ('The engine runs smoothly at low revs.','引擎在低转速时运转平稳。'),('He revs the engine before pulling away.','起步前，他让引擎转快。'),sources=S('revs','rev'))
W('revved','英、美 /revd/','提高转速了；加强了〔过去式、过去分词〕',
 '引擎刚才嗡地转快了，是 revved；a revved-up crowd 也可以说情绪被调动起来的人群。速度、力度向上是共同关系。',
 'rev 双写 v + -ed → revved；短元音单音节词尾 v 接后缀时双写，-ed 读 /d/。',REV+[['rev 双写 v + -ed → revved','过去式、过去分词；末尾 /vd/']],
 'revved the engine 是提高了引擎转速；revved up a campaign 是让活动升温、加力；形容词组合 revved-up 依语境说兴奋、激发起来。',
 'revved the engine；revved up interest；revved up the campaign。',
 'revved 表示转速提高，不自动等于车辆已经开动；rolled forward 才说车向前滚动了。',
 ('The driver revved the engine, but the car did not move.','司机让引擎转快了，车却没动。'),('The publicity campaign revved up interest in the exhibition.','宣传活动提高了人们对展览的兴趣。'),sources=S('revved','rev'))
W('revving','英、美 /ˈrevɪŋ/','正在提高引擎转速；加力、升温的过程',
 '听见引擎转速不断往上，是 revving；活动前不断把气氛热起来，也能用 revving up 的画面。',
 'rev 双写 v + -ing → revving；一个 v 的基础短词接后缀后保留短元音读法。',REV+[['rev 双写 v + -ing → revving','现在分词、动名词；转速或活动强度上升']],
 'be revving the engine 是正在提高引擎转速；revving up for an event 是为活动加劲准备、进入兴奋状态。',
 'revving the engine；revving up interest；revving up for a launch。',
 'revving 里的双 v 是拼写变化，常见读音仍只有一个 /v/ 音，不读两个独立音节。',
 ('A motorbike was revving outside the window.','窗外有辆摩托车在轰着引擎。'),('The team is revving up for the launch.','团队正为发布加紧准备、鼓足劲头。'),sources=S('revving','rev'))
W('bio','英 /ˈbaɪəʊ/；美 /ˈbaɪoʊ/','个人简介；传记〔口语缩略〕',
 '社交账号里几行“我是谁、做什么”的介绍，是 a bio。它把 biography 写一个人的一生，缩成今天也能很短的个人介绍。',
 '简介语境中，biography → bio。biography 较远接希腊 bios 生命 + graphia 记录；短称保留 bio 的读音形式，重音与长词不必完全一样。',BIO,
 'a short bio 是简短介绍；an author bio 是作者简介；update your bio 是更新个人简介。不同页面长度可以很不一样。',
 'a short bio；an author bio；update your bio。',
 '简介 bio 是可独立使用的名词；bio- 生命、生物组合形式通常接其他部分构词。两者有远源联系，现代使用位置不同。',
 ('Please send us a short bio for the event page.','请发一份简短个人介绍，用在活动页面上。'),('She added a link to her portfolio in her bio.','她在个人简介中加了作品集链接。'),sources=S('bio','bio'))
W('bios','英 /ˈbaɪəʊz/；美 /ˈbaɪoʊz/','个人简介；传记〔bio 的复数〕',
 '一场活动有五位嘉宾，各写一份简介，这些介绍就是 bios。数的是一份份人物介绍，不是生命有了英语复数。',
 'bio + -s → bios，元音后后缀读 /z/，直接加 s；这里不是把古希腊 bios 生命原词直接搬来作现代复数。',BIO+[['bio + -s → bios','多个简介；末尾读 /əʊz/、/oʊz/']],
 'speaker bios 是讲者简介；author bios 是作者简介；short bios 是简短人物介绍。',
 'speaker bios；author bios；short bios。',
 '现代简介复数 bios 的构词是英语 bio 加 s；古希腊词源资料里的 bios 本身是生命的词，不是相同的英语复数分析。',
 ('The programme includes short bios of all the speakers.','节目册里有所有讲者的简短介绍。'),('We updated the author bios on the website.','我们更新了网站上的作者简介。'),sources=S('bios','bio'))
W('intel','英、美 /ˈɪntel/','情报；有用的内部消息、信息〔非正式〕',
 '你手里有别人还不知道、又能帮忙判断情况的消息，口语可以叫 intel。它从 intelligence 里留下的是“情报、信息”这一支。',
 'intelligence 截短为 intel；较远 intelligence 接拉丁理解、分辨等词族。缩略词专注有用信息，不把长词的智力等全部义项都一并保留。',
 [['intelligence 的情报、信息义 → intel','缩略保留部分词义，不等于每个长词义都能移植'],['军事等情报语境 → 日常内部消息、有用信息','现代口语可说关于地点、计划等的消息']],
 'gather intel 是搜集情报；intel on a subject 是关于某事的有用信息；good intel 是有价值的消息，通常不可数。',
 'gather intel；useful intel；intel on a project。',
 'intelligence 可以谈智力，intel 通常谈信息。称一个人聪明不能机械说 he has high intel。',
 ('Do you have any intel on the new project?','你有那个新项目的什么消息吗？'),('The team gathered useful intel before the meeting.','开会前，团队搜集到了一些有用信息。'),sources=S('intel','intel'))
W('euro','英 /ˈjʊərəʊ/；美 /ˈjʊroʊ/','欧元；一欧元',
 '价格标签里的 € 对应 euro。这个货币名让人联系 Europe 欧洲，不需要从更远的古代神话拆出今天的币值。',
 '名称取欧洲相关词形材料，1995 年马德里欧洲理事会会议确定 euro 为货币名。它是现代命名，不是英语 money 的派生。',EURO,
 'a euro 是一欧元；euro coins 是欧元硬币；a euro banknote 是欧元纸币。价格修饰语可说 a five-euro ticket。',
 'a euro；euro coins；a euro banknote。',
 'euro 常见读音以辅音 /j/ 起头，所以一欧元说 a euro，不能只看字母 e 就机械套 an。',
 ('The locker takes a euro coin.','这个储物柜需要投入一枚欧元硬币。'),('She found a euro in her coat pocket.','她在外套口袋里发现了一欧元。'),sources=S('euro','euro'))
W('euros','英 /ˈjʊərəʊz/；美 /ˈjʊroʊz/','欧元〔复数〕',
 '三欧元、十欧元，日常英语常说 three euros、ten euros。货币名变成可数单位，按金额数出多个。',
 'euro + -s → euros，元音后后缀读 /z/；普通英语日常复数常加 s，部分正式文件、固定表示中也可见不变形式 euro。',EURO+[['euro + -s → euros','日常英语常见复数，末尾 /əʊz/、/oʊz/']],
 'ten euros 是十欧元；pay in euros 是用欧元支付；a ten-euro note 中前置金额修饰语通常不用 euros。',
 'ten euros；pay in euros；a few euros。',
 'ten euros 与 a ten-euro note 分属名词数量、前置复合修饰两种结构；多出或省掉 s 有句法原因。',
 ('The ticket costs twelve euros.','票价是十二欧元。'),('We paid for the meal in euros.','我们用欧元付了餐费。'),sources=S('euros','euro'))
W('sterling','英 /ˈstɜːlɪŋ/；美 /ˈstɝlɪŋ/','英镑；标准成色的；优良可靠的、出色的',
 '一枚硬币成色足、经得住检验，后来也能夸人、夸工作“品质过硬”。这条关系把 sterling 的银、钱币和出色连在一起。',
 '早期指英国银便士，远源有 sterre 星 + 小称 -ling 等分析，但仍有争论；后来泛指英国货币，并由足值、符合成色标准引申为品格、工作优良可靠。',
 [['sterling：早期英国银便士，名称远源有争论','星形币图加 -ling 是一种解释，不是定论'],['足值、标准成色 → 英国货币；再比喻优良、可靠','现代 sterling work 是出色的工作']],
 'pounds sterling 是英镑；sterling silver 是符合相应成色标准的银；sterling work 是出色工作。后两者都是形容词修饰。',
 'pounds sterling；sterling silver；sterling work。',
 'sterling silver 不等于字面百分之百纯银；sterling work 也不表示工作用银完成，夸的是质量经得起认可。',
 ('The invoice gives the total in pounds sterling.','发票用英镑列出总额。'),('The team has done sterling work under pressure.','团队在压力下做出了出色的工作。'),('The bracelet is made of sterling silver.','手链由标准成色银制成。'),sources=S('sterling','sterling'))
W('phoenix','英 /ˈfiːnɪks/；美 /ˈfinɪks/','不死鸟；浴火重生的人、事物',
 '旧事物烧成灰，新的生命又从中起来，这就是英语 phoenix 最常借用的画面。失败后重建的公司、城市，也能被比作它。',
 '经拉丁 phoenix、phenix 接希腊 phoinix，古英语、古法语也见 fenix；后来 ph、oe 拼写向古典形式靠拢。英语不死鸟传说发展出灰烬重生的比喻。',PHOENIX,
 'rise like a phoenix 是像不死鸟般重新崛起；a phoenix from the ashes 是从毁灭中重生的形象。ph 读 /f/，oe 在常见发音里读 /iː/。',
 'a phoenix；rise like a phoenix；a phoenix from the ashes。',
 '中文常译凤凰，但中西神鸟传统并不完全相同；理解英语比喻时，重点抓灰烬中重生，别把中文凤凰所有象征一并搬入。',
 ('The mural shows a phoenix rising from the ashes.','壁画画着一只从灰烬中升起的不死鸟。'),('After the closure, the theatre returned like a phoenix.','关门后，这家剧院又像不死鸟般重获新生。'),sources=S('phoenix','phoenix'))
W('phoenixes','英 /ˈfiːnɪksɪz/；美 /ˈfinɪksɪz/','不死鸟；重生的事物〔复数〕',
 '奇幻作品或图案里出现几只不死鸟，可以说 phoenixes。某些传统说只有唯一一只，不妨碍现代英语在别的设定里把它数成复数。',
 'phoenix + -es → phoenixes，末音 /s/ 后的复数后缀读 /ɪz/，增加音节；整个借入神鸟名称形成英语常见复数。',PHOENIX+[['phoenix + -es → phoenixes','多个神鸟形象；词尾 /ksɪz/']],
 'painted phoenixes 是画出的不死鸟；phoenixes in a fantasy world 是奇幻世界中的不死鸟。其他更古典复数先不作为常用学习重点。',
 'painted phoenixes；phoenixes in a fantasy novel；two phoenixes。',
 'phoenixes 的末尾读 /ɪz/，和 euro → euros 的 /z/ 不同；判断复数读音看基础词末音，不只看最后几字母。',
 ('Two phoenixes face each other in the design.','图案中两只不死鸟相向而立。'),('The fantasy novel describes phoenixes with golden feathers.','奇幻小说描写了长着金色羽毛的不死鸟。'),sources=S('phoenixes','phoenix'))
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_zip',ROOTS,WORDS)
 extend_lessons()
