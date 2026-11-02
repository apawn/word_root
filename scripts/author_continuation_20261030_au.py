"""Physical, meaning and coach: abstract words made concrete."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
PH=[['希腊 phúsis〔自然〕→ 相关 physikḗ → 拉丁 physica、physicālis','自然、研究自然 → 自然、物理相关的'],['英语 physical','身体的、实体的、物理学的；按场景分义']]
W('physicality','/ˌfɪzɪˈkæləti/','身体性；体力、身体对抗特征；实体存在感',
 '同样一场表演，除了说了什么，还看身体怎样动、怎样占据空间；运动里也常看体力和对抗这一面。',
 'physical + -ity，把身体、实体方面的特点名词化。不是 physics 物理学再加一个城市 city。',PH+[['physical + -ity → physicality','身体、实体方面的性质和表现']],
 'the physicality of the role 角色表演对身体的要求或身体表现，the physicality of the game 比赛的身体对抗性。',
 'the physicality of；the actor’s physicality；the game’s physicality。',
 'physicality 说身体表现、实体性，physics 是物理学。一个演员的 physicality 可以强，未必在讨论他的物理知识。',
 ('The role demands both emotional depth and physicality.','这个角色既需要情感深度，也需要强烈的身体表现。'),('The coach prepared the team for the physicality of the match.','教练让队伍为比赛中的身体对抗做好准备。'))
W('astrophysical','英 /ˌæstrəʊˈfɪzɪkəl/；美 /ˌæstroʊˈfɪzɪkəl/','天体物理学的',
 '研究恒星、星系等时，追问它们怎样发光、运动、变化；重点落在天体背后的物理过程。',
 'astro- 星、天体 + physical 物理的，形成学科相关形容词；不是 astro 变成了 physical，而是两个成分组合。',
 [['希腊 ástron〔星〕→ astro-；physical〔物理的〕','两个来源成分并列组合'],['astro- + physical → astrophysical','与天体物理过程、研究相关的']],
 'astrophysical research 天体物理研究，astrophysical processes 天体物理过程。',
 'astrophysical research；astrophysical processes；an astrophysical model。',
 'astronomical 广义天文学的，astrophysical 特别着眼物理性质、机制；二者学科范围有大量交叉。',
 ('The telescope provides data for astrophysical research.','望远镜为天体物理研究提供数据。'),('The model describes astrophysical processes inside stars.','模型描述恒星内部的天体物理过程。'))
R('B3886','身体、实体和自然物理；先看对象再定义','PHYSICAL：身体这一面，或物质和自然规律这一面','既有 physical、physically 先读；physicality 把身体特征名词化，astrophysical 与既有 geophysical、biophysical 按研究对象并列。',
 'physical 的身体和物理学含义同有自然背景，却在现代句子里分工很清楚，不把身体对抗读成物理课。',
 'physical + -ly/-ity；astro-/geo-/bio- + physical。',
 [['基本形容词、副词与性质','physical · physically · physicality'],['研究对象的组合','astrophysical · geophysical · biophysical']],
 'physicality 身体表现或实体性不同于 physics 学科；astro- 天体、geo- 地球、bio- 生命并列说明对象。',
 'The lecture moved from physical observations to an astrophysical model.\n\n讲座从物理观测讲到了天体物理模型。',
 'physical physically physicality astrophysical geophysical biophysical')
ME=[['古英语 mǣnan → 中古英语 menen → mean','意指、打算、表示'],['中古英语 mening → meaning','所指、意图 → 含义、意义、重要性']]
W('meaning','/ˈmiːnɪŋ/','含义；意思、意图；意义、价值',
 '别人说出一串声音，你想知道他到底指什么；人生有 meaning，则在问这件事为何值得做。',
 'mean 意指、打算 + -ing，有中古英语 mening 等旧名词。这里接意指的 mean，不接平均数，也不接刻薄的同形词。',ME,
 'the meaning of a word 词义，What’s the meaning of this? 这是什么意思，find meaning in work 从工作中找到意义。',
 'the meaning of；the intended meaning；full of meaning；find meaning in。',
 'meaning 常说所指内容或价值，definition 是对词、概念作出的定义。知道一个定义不代表理解了某段话的全部意思。',
 ('What is the meaning of this word?','这个词是什么意思？'),('She found new meaning in helping others.','她从帮助别人中找到了新的意义。'))
W('meaningful','/ˈmiːnɪŋfəl/','有意义的；重要、有价值的；意味深长的',
 '不是表面走个过场，而是真有内容、能产生作用；一个眼神也能不说话却带意思。',
 'meaning + -ful，表示有意义、充满所指内容。后缀只有一个 l，不写成 meaningfull。',ME+[['meaning + -ful → meaningful','有含义、内容或价值；意味深长']],
 'a meaningful conversation 有内容的交谈，meaningful progress 有实质价值的进展，a meaningful look 意味深长的一眼。',
 'a meaningful conversation；meaningful progress；a meaningful look。',
 'meaningful 不只代表语法能解析；a meaningful change 强调变化真有分量。significant 常也说重要，但搭配、语气不总相同。',
 ('We had a meaningful conversation about our plans.','我们认真聊了各自的打算，谈得很有内容。'),('She gave him a meaningful look before leaving.','离开前，她意味深长地看了他一眼。'))
W('meaningless','/ˈmiːnɪŋləs/','无含义的；没有价值、作用的',
 '要么看不出到底在说什么，要么说得通却觉得做了也没用；这两种空要分开。',
 'meaning + -less，缺少意义。可否定可理解内容，也可否定价值、效果，不能一律当语言乱码。',ME+[['meaning + -less → meaningless','没有可理解含义，或没有价值、作用']],
 'a meaningless string of letters 无意义字母串，a meaningless gesture 没有实际作用的姿态，seem meaningless 显得没有意义。',
 'a meaningless gesture；meaningless words；seem meaningless。',
 'meaningless 没内容或没价值，unclear 只是意思不清楚；暂时不懂的专业句不因此就客观无意义。',
 ('To me, the code was a meaningless string of symbols.','在我看来，那段代码就是一串看不懂的符号。'),('Without action, the promise would be meaningless.','没有行动，这个承诺就没有意义。'))
R('B3647','所指内容、意图和价值；有无意义分两路','MEANING：到底指什么，又为什么值得在意','meaning → meaningful → meaningless；先分语言含义和人生、行动价值，例句各落具体场景。',
 'mean 意指的旧名词延续至今。平均数、刻薄的同形 mean 不拿来硬连这一组。',
 'mean〔意指〕+ -ing；meaning + -ful/-less。',
 [['内容与价值','meaning'],['有意义和缺少意义','meaningful · meaningless']],
 'definition 是定义，meaning 是所指和价值；meaningless 不等于只是 unclear；-ful 只有一个 l。',
 'A meaningful promise needs action, or its words may become meaningless.\n\n有意义的承诺需要行动，否则那些话可能失去价值。',
 'meaning meaningful meaningless')
CO=[['匈牙利地名 Kocs → kocsi〔来自 Kocs 的车〕','以制车闻名的地方 → 相应车辆名称'],['经德语 Kutsche、法语 coche 等 → coach','马车；客车、车厢'],['英语辅导者比喻 → coach','带人过考试关 → 辅导者、教练；也作指导动词']]
W('coach','英 /kəʊtʃ/；美 /koʊtʃ/','教练；辅导者；长途客车、车厢；指导训练',
 '车把人带到目的地，教练把人带过一道关；这是能把两个常见意思接起来的历史比喻。',
 '车辆词经法语、德语等接匈牙利 kocsi，与地名 Kocs 有关。英语学生俚语把辅导过考的人比作载人前进的车，后来用于体育等教练。',CO,
 'a football coach 足球教练，a life coach 人生指导者，travel by coach 坐长途客车，coach a team 指导队伍。美式 fly coach 常说坐经济舱。',
 'a football coach；travel by coach；coach a team；fly coach。',
 'coach 教练、客车不同于 couch 沙发，只差一个字母但读音、来源都不同。train 强调训练，coach 强调指导者带着提高的过程。',
 ('The coach helped her improve her technique.','教练帮助她改进技术。'),('We travelled to the city by coach.','我们乘长途客车去了城里。'),sources=['https://en.wiktionary.org/wiki/coach#English','https://www.etymonline.com/word/coach'])
W('coachman','英 /ˈkəʊtʃmən/；美 /ˈkoʊtʃmən/','马车夫',
 '旧时坐在马车上，握缰绳驾车的人；这个词接车辆那一路，不是男教练的普通名称。',
 'coach 马车 + man，复数 coachmen。固定职业名称保留旧马车场景。',CO[:2]+[['coach + man → coachman','驾马车的人']],
 'the coachman’s seat 马车夫座位，a coachman holding the reins 握缰绳的马车夫。常见于历史、小说、老照片。',
 'the coachman’s seat；the coachman held the reins；an old coachman。',
 'coachman 马车夫，coach driver 现代常说客车司机；male coach 才可直接说男性教练。',
 ('The coachman pulled on the reins and stopped the horses.','马车夫拉住缰绳，让马停下。'),('The passengers waited while the coachman loaded the luggage.','马车夫装行李时，乘客们等着。'))
R('B3679','车辆载人到目的地；辅导者带人过关','COACH：车载人前进，教练带人进步','coach 一词分交通和指导两路；coachman 接旧马车，不接教练。',
 '名称可追到匈牙利地名 Kocs；从车到辅导者的英语比喻有历史依据，不能把现代所有教练都画成马车夫演变。',
 '地名 Kocs → kocsi → 欧洲语言车辆词 → coach；coach + man。',
 [['车与辅导者','coach'],['旧车辆职业','coachman']],
 'coach 教练、客车与 couch 沙发不同；coachman 马车夫不等于男教练；fly coach 美式经济舱。',
 'The coach travelled by coach to meet the team.\n\n教练乘长途客车去与队伍会合。',
 'coach coachman')
if __name__=='__main__':save('continuation_20261030_au',ROOTS,WORDS)
