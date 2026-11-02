"""Persistent interference: heckling, pestering, badgering and nagging."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
def S(word,base):
 return ['https://en.wiktionary.org/wiki/'+word+'#English','https://www.etymonline.com/word/'+base]
EXISTING_ROOT_ADDITIONS={
 'A1741':dict(words='nag nags nagged nagging naggingly'.split(),label='nag：不断啃扰人的唠叨与疑虑',note='nag 动词大概接斯堪的纳维亚啃咬材料，与 gnaw 同族；老马名词另源。nagging 可以写不停唠叨，也能写疼痛、疑虑挥之不去。'),
 'B3261':dict(words='hook heckle heckles heckled heckling heckler hecklers'.split(),label='heckle：带齿的梳麻工具与尖锐追问',note='heckle 的工具名接古老钩、齿材料，动词从工具名或相关荷兰语形式发展。由粗厉梳理到反复尖锐提问是词义扩展，不是把现代 hook 换字母。'),
 'C0964':dict(words='pester pesters pestered pestering'.split(),label='pester：从缠住、绊住到不停烦人',note='经法语 empestrer 等接牧人拴牲畜的绳索材料；现代烦扰义受 pest 影响，不能只拆成 pest 加 -er 就说完历史。'),
 'A1938':dict(words='badger badgers badgered badgering'.split(),label='badger：动物名转出穷追不舍的纠缠',note='动物名可能联系 badge 与旧 -ard，尚非定论；纠缠动词联系历史上犬围攻獾的活动，不能讲成獾天生爱烦人。'),
 'A1833':dict(words='harass harasses harassed harassing harasser harassers harassment'.split(),label='harass：反复侵扰与实施者',note='harass 借法语 harasser，远源未定；-er 命名骚扰者，-ment 命名骚扰行为、状态。现代词尾可明拆，词根远源仍要保留不确定性。'),
}
HECKLE=[['heckle 工具名：梳理麻纤维的齿梳','可能接未记录的古英语 *hecel 或同源日耳曼词，远源联系钩、齿材料'],['heckle 动词：梳理 → 尖锐追问、插话起哄','工具名转动词或相关荷兰语形式进入；现代常说打断公开讲话、表演']]
PESTER=[['牧人拴牲畜的绳索材料 → 重建 *impastoriare','绊住、拴住；连接词形有重建成分'],['法语 empestrer → 英语 pester','纠缠、妨碍到反复烦扰，现代烦人义还受 pest 影响']]
BADGER=[['动物名 badger','可能由 badge 旧形加 -ard 材料形成，联系斑纹，尚非定论'],['动物名 → 动词 badger','联系犬反复围攻獾的历史活动，转写持续纠缠、逼问别人']]
HARASS=[['法语 harasser → 英语 harass','使疲惫、反复侵扰；更早来源有不同分析'],['harass 加英语词尾','不断骚扰、烦扰；harasser 命名实施者，harassment 命名行为、状态']]
NAG=[['方言啃咬材料 → nag 动词','大概接斯堪的纳维亚语言相关形式，与 gnaw 同族；并非现代 gnaw 直接换拼写'],['一点点啃咬 → 不断挑错、唠叨；也可写疑虑挥之不去','nag 老马名词是另源词，更早来路未定，不能把唠叨义全从马推出来']]
W('heckle','/ˈhekəl/','对演讲、表演插话起哄、刁难；梳理麻纤维〔旧工具义〕',
 '台上的人还在讲，台下有人不断喊问题、喊讽刺的话打断，让他难以继续，这叫 heckle。可以想象一把带齿的梳子反复刮过：它的确有梳麻的旧义。',
 '动词来自 heckle 齿梳名词，或相关荷兰语 hekelen；工具的更早材料联系钩、齿。现代先把 heckle 视作整体，再分析它后接的规则词尾。',HECKLE,
 'heckle a speaker 对演讲者插话起哄；heckle a comedian 打断、刁难喜剧演员。',
 'begin to heckle；refuse to heckle。',
 'ask a question 可以是正常问答；heckle 突出打断、挑衅或反复尖锐追问的方式，不能把所有提问者都叫 hecklers。',
 ('A few people began to heckle the speaker.','有几个人开始对演讲者插话起哄。'),('Please don’t heckle the performers during the show.','演出时请不要对表演者插话起哄。'),sources=S('heckle','heckle'))
W('heckles','/ˈhekəlz/','插话起哄、刁难〔第三人称单数〕；梳麻齿梳〔复数〕',
 '某个观众总等台上刚开口就插话、讥讽，叫 he heckles the speaker。词史里还有梳麻工具的同形复数，但日常优先看动词。',
 'heckle + -s，读 /z/；工具名复数与动词三单同形，现代起哄义接旧梳理动词的比喻扩展。',HECKLE+[['heckle + -s → heckles','他不断插话、挑衅；工具名也能有复数']],
 'heckles the speaker 对演讲者起哄；heckles from the back 从后面不断插话。',
 'regularly heckles；heckles every performer。',
 'interrupts 可以无意打断，heckles 通常含有刻意插话、嘲弄或刁难的方向。',
 ('He heckles every speaker who disagrees with him.','只要演讲者与他意见不同，他就插话刁难。'),('One man heckles from the back whenever she pauses.','她每次停顿，后面就有个男人插话起哄。'),sources=S('heckles','heckle'))
W('heckled','/ˈhekəld/','插话起哄、刁难了；被起哄打断的',
 '讲话几次被台下的尖刻喊话打断，演讲者 was heckled。常见被动是因为报道重点在受到干扰的人。',
 'heckle 去 e 加完整 -ed，读 /d/；动作过去形式，也用于被动。',HECKLE+[['heckle → heckled','过去对公开讲话、表演反复插话刁难']],
 'heckled by the crowd 遭人群起哄；heckled throughout the speech 整场演说都被插话干扰。',
 'was loudly heckled；heckled the candidate。',
 'questioned 可中性表示被问问题，heckled 则通常说明过程带干扰、刁难或敌意。',
 ('The candidate was heckled throughout the speech.','那名候选人在整个演说过程中都被插话起哄。'),('A small group heckled the comedian, who calmly carried on.','一小群人打断那位喜剧演员起哄，他则镇定地继续表演。'),sources=S('heckled','heckle'))
W('heckling','/ˈheklɪŋ/','插话起哄、反复刁难；正在这样干扰',
 '台下一次次喊话打断，台上的话总接不下去，这种行为整体叫 heckling；写动作过程也用同形。',
 'heckle 去 e 加 -ing；可作动作形式、行为名词，常见读音中间收成 /kl/。',HECKLE+[['heckle → heckling','正在插话刁难；或命名这种干扰行为']],
 'stop the heckling 制止插话起哄；heckling from the audience 来自观众的起哄。',
 'persistent heckling；heckling the speaker。',
 'a lively discussion 是热烈讨论，heckling 则通常把对方难以继续讲话作为显著特征；大声不等于必然 heckling。',
 ('The host asked for the heckling to stop.','主持人要求停止插话起哄。'),('They were heckling the speaker rather than listening to her.','他们一直对演讲者插话刁难，没有听她讲。'),sources=S('heckling','heckle'))
W('heckler','英 /ˈheklə/；美 /ˈheklər/','对演讲、表演插话起哄、刁难的人',
 '你在台上讲，他在台下一遍遍喊话、让你难以继续，这个人叫 a heckler。-er 把行为落实到做事的人。',
 'heckle 去 e 加完整 -er；早期也可指用齿梳梳麻的人，后来用于起哄、反复刁难公开讲话的观众。',HECKLE+[['heckle + -er → heckler','使用工具者的旧义，后来转写插话刁难者']],
 'deal with a heckler 应付起哄者；a persistent heckler 不断插话刁难的人。',
 'respond to a heckler；ignore the heckler。',
 'a questioner 只是提问者，a heckler 还带干扰、挑衅的行为特征；不能只凭一个尖锐问题就把人归为后者。',
 ('The comedian answered the heckler with a quick joke.','喜剧演员用一个机敏的笑话回应了那个起哄者。'),('A heckler kept interrupting the opening speech.','一个起哄者不停打断开场演说。'),sources=S('heckler','heckler'))
W('hecklers','英 /ˈhekləz/；美 /ˈheklərz/','插话起哄、刁难者〔复数〕',
 '不是一人，而是几个观众不断对着台上喊话、打断，这些人就是 hecklers。',
 'heckle 去 e 加 -er → heckler，再加复数 -s，词尾读 /z/；名词旧义、现代起哄者义共用这一形态。',HECKLE+[['heckle → heckler → hecklers','多个实施插话、嘲弄、反复刁难的人']],
 'a group of hecklers 一群起哄者；silence the hecklers 让起哄者安静下来。',
 'deal with hecklers；hecklers in the audience。',
 'hecklers 讲他们如何干扰，不必然说明人数占多数；a few hecklers 也可能制造很大声音。',
 ('A few hecklers tried to drown out the speech.','几个起哄者试图用声音盖过演说。'),('She paused until the hecklers were quiet.','她停下来，等那些起哄者安静。'),sources=S('hecklers','heckler'))
W('pesters','英 /ˈpestəz/；美 /ˈpestərz/','不断烦扰、纠缠〔第三人称单数〕',
 '已经回答过，过一会儿又来问，追着你不放，这个人 pesters you。关键是烦扰一再回来。',
 'pester + -s，读 /z/；pester 常经法语的缠住、绊住材料而来，现代烦扰义受 pest 影响，并非简单的“害虫加 -er”。',PESTER+[['pester + -s → pesters','他反复纠缠、烦扰']],
 'pesters someone for something 缠着某人要某物；pesters someone with questions 不停提问来烦人。',
 'pesters me for an answer；pesters her to buy a toy。',
 'asks 只说提出请求，pesters 额外说请求反复到让对方烦；重点在频度、纠缠感。',
 ('The child pesters his father for a puppy.','孩子缠着爸爸，非要养一只小狗。'),('She pesters me with questions while I am trying to work.','我想专心工作时，她不停提问来烦我。'),sources=S('pesters','pester'))
W('pestered','英 /ˈpestəd/；美 /ˈpestərd/','反复烦扰、纠缠了；被纠缠的',
 '对方不停来催、来要，你很难脱身，就可以说 you were pestered。像被一串要求缠住了。',
 'pester + 完整 -ed，词尾读 /d/；这是 pester 整体接过去词尾，主语可以是纠缠者，被动句则以受到纠缠的人为主语。',PESTER+[['pester + -ed → pestered','过去反复烦扰；或受到不停纠缠']],
 'pestered for money 被缠着要钱；pestered with questions 被没完没了地问。',
 'was constantly pestered；pestered her for a reply。',
 'reminded 可以是一次有帮助的提醒，pestered 突出让人烦的反复催促；同一行为会因频率、场景变成不同感受。',
 ('He pestered me for an answer all afternoon.','他整个下午都缠着我要一个答复。'),('We were pestered with sales calls during dinner.','吃晚饭时，推销电话没完没了地打来烦我们。'),sources=S('pestered','pester'))
W('pestering','英 /ˈpestərɪŋ/；美 /ˈpestərɪŋ/','正在纠缠、不断烦扰',
 '这会儿还在追着问、追着要，让人没法清静，就是 pestering。常带“别再缠着我了”的不耐烦。',
 'pester + -ing；规则动作形式，承缠住到烦扰的词义历史。',PESTER+[['pester + -ing → pestering','反复纠缠正在发生']],
 'stop pestering me 别再缠着我；pestering someone for a reply 缠着要答复。',
 'pestering her with messages；keep pestering。',
 'pestering 说明反复到令人烦，persuading 是试图说服；不停纠缠不表示已经给出更有力的理由。',
 ('Stop pestering me while I am on the phone.','我打电话时别再缠着我。'),('They kept pestering her for details about the trip.','他们不停缠着她打听旅途细节。'),sources=S('pestering','pester'))
W('badgers','英 /ˈbædʒəz/；美 /ˈbædʒərz/','獾〔复数〕；不断纠缠、逼问〔第三人称单数〕',
 '名词是几只獾；动词却可以是有人不断逼问、催你答应。纠缠义接的是围攻獾的旧活动意象，不是说獾喜欢唠叨。',
 'badger + -s，读 /z/；动物名复数与动词三单同形。动物名可能联系 badge 的斑纹命名说，尚未确定。',BADGER+[['badger + -s → badgers','多只獾；他持续纠缠、逼问']],
 'badgers emerge at night 獾在夜间出没；badgers someone for an answer 追着要答复。',
 'watch for badgers；badgers his parents to buy it。',
 'badgers 是动物名复数时不含烦扰评价；先看是名词主语，还是后面接人作动词宾语。',
 ('Badgers usually leave their setts after dark.','獾通常在天黑后离开洞穴。'),('He badgers me for an answer before I have the facts.','我还没掌握事实，他就不断逼我给答复。'),sources=S('badgers','badger'))
W('badgered','英 /ˈbædʒəd/；美 /ˈbædʒərd/','不断纠缠、逼问了；被逼问的',
 '你说还没决定，对方却一轮又一轮催你答应，这就是被 badgered。它比问了一次更有围着人不放的感觉。',
 'badger + 完整 -ed，读 /d/；动词由动物名转用，纠缠义联系围攻獾的旧活动。',BADGER+[['badger + -ed → badgered','过去反复逼问、纠缠']],
 'badgered into agreeing 被缠得答应；badgered for details 被追问细节。',
 'felt badgered；badgered by reporters。',
 'agreed willingly 是自愿答应，was badgered into agreeing 却说反复施压促成了答应；语气与原因不同。',
 ('They badgered him into joining the committee.','他们反复劝逼，终于让他答应加入委员会。'),('She felt badgered by the constant requests for updates.','不停被催问进度，让她觉得被缠得受不了。'),sources=S('badgered','badger'))
W('badgering','英 /ˈbædʒərɪŋ/；美 /ˈbædʒərɪŋ/','不断纠缠、逼问；正在这样施压',
 '不给人留思考空间，问题或请求一轮轮追上来，是 badgering。也能把这种穷追不舍的行为当一个整体来讲。',
 'badger + -ing；动词规则变化；名词化时，把反复逼问、施压的行为作为整体来谈。',BADGER+[['badger + -ing → badgering','正在反复逼问；也可命名纠缠行为']],
 'stop badgering me 别再逼问我；badgering someone to agree 反复缠着要人答应。',
 'constant badgering；badgering her with questions。',
 'badgering 强调不放过对方的持续施压；heckling 更常针对公开讲话、表演的插话干扰，场景不同。',
 ('Please stop badgering me about the deadline.','请别再没完没了地追问我截止日期的事。'),('The constant badgering made it hard for her to think.','不停被纠缠逼问，让她难以思考。'),sources=S('badgering','badger'))
W('harasses','/ˈhærəsɪz/，也读 /həˈræsɪz/','反复骚扰、侵扰〔第三人称单数〕',
 '对方不想再接触，却不停被堵着、收到攻击信息或遭威胁，施扰者 harasses someone。它通常比一次让人不高兴更有持续侵扰的重量。',
 'harass + -es；/s/ 后读 /ɪz/。基础词借法语 harasser 使疲惫、侵扰，更早来源未定。',HARASS+[['harass + -es → harasses','他反复骚扰、侵扰']],
 'harasses someone online 在网上骚扰某人；harasses the staff 骚扰员工。',
 'repeatedly harasses；harasses people with threats。',
 'annoys 可以是无意的噪声让人心烦；harasses 更常写针对人的持续侵扰。这里讲日常用法，不把所有小烦恼都等同于骚扰。',
 ('The anonymous account harasses her with threatening messages.','那个匿名账号不断发威胁信息骚扰她。'),('He harasses the staff whenever they refuse his demands.','员工只要拒绝他的要求，他就不断骚扰他们。'),sources=S('harasses','harass'))
W('harassing','/ˈhærəsɪŋ/，也读 /həˈræsɪŋ/','正在骚扰；构成反复侵扰的',
 '一条攻击信息还没消停，下一条又追来，harassing messages 把这种侵扰性质点出来；动词形式则写骚扰正在发生。',
 'harass + -ing；词尾双 s 本来就有，直接接 -ing，不再多加一个 s。',HARASS+[['harass + -ing → harassing','正在反复侵扰；也形容骚扰性信息、行为']],
 'harassing messages 骚扰信息；harassing phone calls 骚扰电话；stop harassing someone 停止骚扰。',
 'kept harassing；reported the harassing calls。',
 'harassing 来电指对人的侵扰，frequent calls 只说来得多；频度和意图、内容、对方反应要放回场景看。',
 ('She saved the harassing messages as evidence of what happened.','她保存了那些骚扰信息，记录发生过的事。'),('The man kept harassing passengers at the station.','那个男人一直在车站骚扰乘客。'),sources=S('harassing','harass'))
W('harasser','英 /ˈhærəsə/、/həˈræsə/；美 /ˈhærəsər/、/həˈræsər/','骚扰者；反复侵扰他人的人',
 '不只命名一种行为，还把实施反复侵扰的人指出来，就是 a harasser。',
 'harass + -er，-er 命名实施动作的人；harass 接法语侵扰、使疲惫的材料，远源未定。',HARASS+[['harass + -er → harasser','实施骚扰、持续侵扰的人']],
 'an online harasser 网络骚扰者；identify the harasser 认出骚扰者。',
 'block the harasser；report a harasser。',
 'harasser 指实施侵扰的人，victim 指受害者；读被动句时留意动作方向，别把两种角色混在一起。',
 ('She blocked the harasser after receiving more threats.','又收到威胁后，她屏蔽了那个骚扰者。'),('The witness helped identify the harasser.','目击者帮助认出了骚扰者。'),sources=S('harasser','harass'))
W('harassers','英 /ˈhærəsəz/、/həˈræsəz/；美 /ˈhærəsərz/、/həˈræsərz/','骚扰者〔复数〕',
 '几个人不断发攻击信息、追着别人不放，这些施扰者可以合称 harassers。',
 'harass + -er → harasser，再加复数 -s，读 /z/；-er 先命名人，-s 再给人数。',HARASS+[['harass → harasser → harassers','多个实施反复侵扰的人']],
 'online harassers 网络骚扰者；block harassers 屏蔽骚扰者。',
 'identify the harassers；protect staff from harassers。',
 'harassers 是人的称呼，harassment 是行为、处境的名词；不能把多个骚扰者写成 several harassment。',
 ('The platform removed accounts used by the harassers.','平台移除了那些骚扰者使用的账号。'),('Staff were trained to document repeated contact from harassers.','员工接受了培训，学习记录骚扰者反复联系的情况。'),sources=S('harassers','harass'))
W('nag','/næɡ/','唠叨、不断催促或挑错；使人一直不安；爱唠叨的人；老马',
 '同一件事一遍遍念叨，像一点点啃着你的耐心，就是 nag；一个疑问也能 nag at you，在心里咬住不放。老马那个名词是另一来源。',
 '动词大概来自斯堪的纳维亚啃咬材料，与 gnaw 同族；唠叨者名词由动词发展。nag 老马、原来的小骑乘马名词更早、来源未定，不与唠叨动词硬合。',NAG,
 'nag someone to do something 唠叨着催某人做事；nag at someone 不断唠叨或困扰某人；an old nag 一匹老马。',
 'stop nagging 的基础动词；don’t mean to nag。',
 'remind 可以只是提醒一次；nag 带反复、令对方烦的视角。说 don’t nag me 常是在表达被催烦了，不必因此断定提醒内容无理。',
 ('I don’t want to nag, but the bins still need emptying.','我不想一直唠叨，不过垃圾桶还是得倒。'),('One unanswered question continued to nag at me.','一个没得到回答的问题一直让我放不下。'),sources=S('nag','nag'))
W('nags','/næɡz/','唠叨、不断困扰〔第三人称单数〕；爱唠叨的人、老马〔复数〕',
 '小问题总冒出来，让人没法完全放心，是 a doubt nags at me；有人反复催别人做事，也用 nags。',
 'nag + -s，/ɡ/ 后读 /z/；动词三单与名词复数同形，但老马名词另源。',NAG+[['nag + -s → nags','他反复催、挑错；疑虑不断困扰；名词也可有复数']],
 'nags at me 一直让我不安；nags someone about chores 因家务不停唠叨某人。',
 'a doubt that nags；nags him to tidy up。',
 'a doubt nags at me 常是挥之不去，不一定达到恐惧；terrifies me 才强调让我极其害怕。',
 ('A small doubt nags at me whenever I read the report.','每次读这份报告，总有一点疑虑让我放不下。'),('He nags his housemate about the washing-up.','他总因洗碗的事唠叨室友。'),sources=S('nags','nag'))
W('nagged','/næɡd/','唠叨、催促了；一直困扰了',
 '过去被同一要求念了很多遍，或一个念头一直没法放下，都可用 nagged。人的话可以唠叨，心里的问题可以啃扰。',
 'nag 双写 g 加完整 -ed，读 /d/；单音节重读短元音后接一个辅音字母时，这里按规则双写。',NAG+[['nag + -ed → nagged','过去反复催促；或持续留在心里使不安']],
 'nagged about money 因钱的事被唠叨；a question nagged at me 一个问题一直困扰我。',
 'nagged him to finish；nagged at the back of her mind。',
 'nagged 是持续反复，asked once 是问一次；故事里用了 nagged，通常已带被催烦或甩不开的感觉。',
 ('She nagged him to finish the repair before winter.','她反复催他在冬天前修好。'),('The possibility of an error nagged at me all night.','可能出了错这个念头整晚都让我放不下。'),sources=S('nagged','nag'))
W('nagging','/ˈnæɡɪŋ/','唠叨、不断催促；挥之不去的；持续隐隐作痛的',
 'nagging doubt 不是疑虑在说话，而是它像唠叨一样，隔一会儿就冒出来；nagging pain 也多是持续烦扰、难甩开的痛。',
 'nag 双写 g 加 -ing；动作形式可作行为名词，也能形容不断啃扰注意力的疑虑、疼痛等。',NAG+[['nag → nagging','持续唠叨；进一步写不断回来、让人放不下']],
 'a nagging doubt 挥之不去的疑虑；nagging pain 持续隐痛；constant nagging 不停唠叨。',
 'stop nagging；a nagging feeling that something is wrong。',
 'nagging pain 侧重持续烦扰，不表示必然剧烈；sharp pain 侧重尖锐疼痛的性质。这里是用词区别，具体疼痛强弱看情境。',
 ('I had a nagging doubt about the figures.','我对那些数字总有一丝挥之不去的疑虑。'),('The nagging pain in his shoulder made it hard to concentrate.','肩膀持续的隐痛让他难以集中注意力。'),sources=S('nagging','nag'))
W('naggingly','/ˈnæɡɪŋli/','持续烦扰地；让人挥之不去地；唠叨地',
 '一件事没大到让你立刻停下，却总在脑海里冒出来，叫 naggingly。它写的是像小刺一样不断提醒你的感觉。',
 'nagging + -ly；内层 nag 双写 g 加 -ing，外层把不断烦扰的性质用于方式、程度。',NAG+[['nag → nagging → naggingly','不断啃扰的性质，转成持续烦扰的方式']],
 'naggingly familiar 熟悉得让人老想追问在哪里见过；naggingly uncertain 持续让人放不下的不确定。',
 'remained naggingly incomplete；naggingly aware of a problem。',
 'naggingly familiar 常是熟悉却暂时想不起在哪里见过，instantly recognizable 则是一下就认得出；前者带着没解决的小疑问。',
 ('His face looked naggingly familiar.','他的脸让我总觉得在哪儿见过，却想不起来。'),('The explanation remained naggingly incomplete.','这个解释始终缺着一块，让人难以释怀。'),sources=S('naggingly','nag'))
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_zgk',ROOTS,WORDS)
 extend_lessons()
