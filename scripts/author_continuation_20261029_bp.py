"""Bear: animal and carrying verb kept as separate historical branches."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
def C(a,b,w,m):return [[a+'；'+b,'并列构词部分'],[w,m]]
B=[['不同旧词：古英语 bera；古英语 beran','前者是熊；后者是承载、带来、生育'],['英语同形 bear','熊；另有承受、携带、产生等动词义']]
V=[['古英语 beran → 中古英语 beren','承载、带来；生育；忍受'],['英语 bear；过去式 bore，过去分词通常 borne','承受、携带、产生；出生表达中使用 born']]
W('bear','英 /beə/；美 /ber/','熊；承受、忍受；携带；产生、生育',
 '名词先想熊这个动物；动词另想肩上承着东西，再扩展为承担责任、忍受压力、结出结果。',
 '熊接古英语 bera，动词接 beran，两条来路分开。熊名常被联系到棕色者的古老称呼，但更远解释并非无争议。动词过去式 bore，通常过去分词 borne；be born 出生另用 born。',B,
 'bear the cost 承担成本，bear a name 带有某个名字，bear fruit 结果、产生效果；can’t bear something 受不了。bear in mind 是记在心里。',
 'bear responsibility；bear the cost；bear fruit；bear in mind；can’t bear to do something。',
 'bear 忍受多强调承受艰难、烦扰；wear 穿戴不是 bear 的普通替换。熊是名词另一源，不能把生孩子解释成像熊一样。',
 ('The tree finally began to bear fruit.','这棵树终于开始结果了。'),('I can’t bear the constant noise upstairs.','我受不了楼上持续不断的噪声。'),('We saw a bear near the edge of the forest.','我们在森林边缘附近看见了一头熊。'),sources=['https://en.wiktionary.org/wiki/bear#English','https://blog.oup.com/2014/09/brown-etymology-word-origin-part-1/','https://dictionary.cambridge.org/grammar/british-grammar/born-or-borne'])
W('bearer','英 /ˈbeərə/；美 /ˈberər/','携带者；持有者；传递者',
 '带着某样东西的人：手里拿着文件，或把消息带到你面前。',
 'bear 携带 + -er；旧英语已有相应的人名词，现代构词关系依然清楚。',V+[['bear → bearer','携带 → 携带、持有或传递的人']],
 'the bearer of good news 带来好消息的人；the bearer of a ticket 票券持有人。banner bearer 可指实际举旗者，也可比喻代表某项事业的人。',
 'the bearer of bad news；a ticket bearer；a standard bearer。',
 'bearer 强调带着、持有，不必是物主；owner 才明确说拥有者。带来坏消息的人也不一定制造了坏事。',
 ('I’m happy to be the bearer of good news today.','我很高兴今天能给大家带来好消息。'),('The pass allows the bearer to enter the exhibition twice.','持这张通行证可以进入展览两次。'))
W('bearing','英 /ˈbeərɪŋ/；美 /ˈberɪŋ/','举止、姿态；关系、影响；轴承；方位',
 '先从承着、带着来想：一个人怎样持身是一种姿态，机器承托转轴的部件是轴承；方向一义则来自朝向。',
 'bear + -ing。bearing 名词从承载、持身、朝某方向等动词用法发展出多个固定意思，不是所有语境都能译为承受中。',V+[['bear 的承托、持身、朝向用法 → bearing','轴承；举止；关系；方位']],
 'a calm bearing 镇定的举止；have a bearing on 与……有关、对……有影响；get one’s bearings 弄清方位，也可指熟悉新环境。',
 'a ball bearing；have no bearing on；get one’s bearings；a confident bearing。',
 'bearings 可能是多个轴承，也可能是方向定位；要看谈机器维修还是找路。have a bearing on 不是把某物放在轴承上。',
 ('Her confident bearing helped put the audience at ease.','她自信的举止让听众放松下来。'),('This detail has no bearing on the final decision.','这个细节与最后的决定无关。'),('I needed a few minutes to get my bearings in the new building.','我花了几分钟才弄清这座新楼里的方位。'))
W('bearable','英 /ˈbeərəbəl/；美 /ˈberəbəl/','可以忍受的',
 '虽不好受，但还在撑得住的范围里。',
 'bear 忍受 + -able 可以……的；表示某种处境能被承受。',V+[['bear + -able → bearable','承受 → 可以忍受的']],
 'make something bearable 让某事变得能忍受；just bearable 勉强能承受。它不一定好，只是没超过承受线。',
 'make life bearable；barely bearable；more bearable。',
 'bearable 可忍受，comfortable 舒服；酷热稍缓后 bearable，仍未必称得上 comfortable。',
 ('A small fan made the crowded room more bearable.','一台小风扇让拥挤的房间稍微好受一些。'),('The long wait was bearable because we had books to read.','我们有书可读，所以漫长的等待还算能忍受。'))
W('unbearable','英 /ʌnˈbeərəbəl/；美 /ʌnˈberəbəl/','无法忍受的；难以承受的',
 '难受或烦扰越过了能撑住的那条线。',
 'un- 不 + bearable 可承受的；核心仍是 bear 承受，与动物熊无关。',V+[['bear → bearable → unbearable','承受 → 能承受 → 难以承受']],
 'unbearable heat 难以忍受的炎热；unbearable noise 难以忍受的噪声。也可以是主观夸张，表达实在受不了了。',
 'unbearable heat；an unbearable smell；become unbearable。',
 'unbearable 不自动等于物理上绝无可能活下来；日常抱怨也会用它加强语气。',
 ('The heat in the attic became unbearable by noon.','到中午，阁楼里的炎热变得难以忍受。'),('The loud music made conversation almost unbearable.','音乐声太大，让交谈几乎成了折磨。'))
W('unbearably','英 /ʌnˈbeərəbli/；美 /ʌnˈberəbli/','难以忍受地；极其',
 '把难以忍受这个强度放在某种状态前面。',
 'unbearable + -ly，-able 的形容词转成 -ably 的副词形式。',V+[['unbearable → unbearably','难以忍受的 → 以难以忍受的程度']],
 'unbearably hot 热得受不了，unbearably slow 慢得让人难忍。通常修饰形容词或副词，强调人的强烈感受。',
 'unbearably hot；unbearably loud；unbearably slowly。',
 'unbearable 修饰名词，unbearably 常修饰程度：unbearable heat，unbearably hot。',
 ('The bus was unbearably crowded.','公交车挤得让人受不了。'),('The clock seemed to move unbearably slowly.','时钟好像走得慢得令人难以忍受。'))
W('forbear','英 /fɔːˈbeə/；美 /fɔːrˈber/','克制；忍住不做',
 '冲动已经上来了，但自己把它按住，不付诸行动。',
 '接古英语 forberan；旧前缀 for- + beran，发展出忍住、克制、容忍等用法。这里不能按现代 for 为了硬译。',V+[['古英语 forberan → forbear','克制、忍住、容忍']],
 'forbear from commenting 忍住不作评论，较正式或文学。过去式 forbore，过去分词 forborne。',
 'forbear from doing something；forbear to comment。',
 'forbear 动词是克制；forebear 常指祖先，常见复数 forebears。祖先这个名词不要按克制义理解。',
 ('She chose to forbear from criticizing the unfinished work.','她选择忍住不批评那份尚未完成的作品。'),('He could not forbear to smile at the child’s remark.','听到孩子的话，他忍不住笑了。'))
W('forbearance','英 /fɔːˈbeərəns/；美 /fɔːrˈberəns/','耐心；宽容；克制',
 '不是没有不满，而是压住冲动，给别人或困难留一点余地。',
 'forbear 克制、容忍 + -ance，形成状态、品质名词；不是 forebear 祖先加后缀。',V+[['forbear → forbearance','忍住、容忍 → 克制、宽容这一品质']],
 'show forbearance 表现出克制、宽容；thank someone for their forbearance 感谢对方耐心包容。通常比 patience 更正式。',
 'show great forbearance；patience and forbearance；test someone’s forbearance。',
 'forbearance 常含面对烦扰仍克制的意思；patience 范围更广，也可只是耐心等待。金融语境另有暂缓执行、暂缓还款等专业用法。',
 ('She showed remarkable forbearance during the heated discussion.','在激烈讨论中，她表现出了难得的克制。'),('Thank you for your forbearance while we reorganize the office.','办公室调整期间，感谢大家耐心包容。'),sources=['https://en.wiktionary.org/wiki/forbearance#English','https://dictionary.cambridge.org/us/dictionary/english/forbearance'])
W('born','英 /bɔːn/；美 /bɔːrn/','出生的；天生的；由……产生的',
 '一个生命被带到世界上；比喻上，一个想法也可以在某种处境中诞生。',
 '来自 bear 承载、生育的旧过去分词，古英语 boren。现代 be born 用于出生；其他承载、忍受等常用 borne。主动表示生育也可用 borne，如 has borne two children。',V+[['古英语 boren → born','被生下、出生；出生相关用法固定拼作 born']],
 'be born in a city 出生在某城，be born in 2000 出生于2000年；a born leader 天生的领袖；an idea born of frustration 因挫折而产生的想法。',
 'be born in；be born into a family；a born storyteller；born of necessity。',
 '说某人出生用 was born，不用 he born。borne 强调被承载、承担；born 主要固定在出生及其比喻用法中。',
 ('She was born in a small town by the sea.','她出生在一个海边小镇。'),('The project was born of a simple question.','这个项目源于一个简单的问题。'),sources=['https://en.wiktionary.org/wiki/born#English','https://dictionary.cambridge.org/grammar/british-grammar/born-or-borne'])
W('reborn','英 /ˌriːˈbɔːn/；美 /ˌriːˈbɔːrn/','重生的；焕然一新的',
 '好像又出生一次：可以是信仰里的再生，也可以比喻恢复活力。',
 're- 再、重新 + born 出生。用再次出生的画面表达精神转变或事物重新焕发生机。',V+[['born → re- + born → reborn','出生 → 再生、焕然新生']],
 'feel reborn 感到焕然一新；a theatre reborn as a community centre 剧院改造后以社区中心的面貌重获新生。',
 'feel reborn；be reborn as；a city reborn。',
 'reborn 可以比喻恢复生机，并不每次都在陈述转世信仰；rebuild 重点是重建这个动作。',
 ('After a week of rest, I felt reborn.','休息一周后，我感觉焕然一新。'),('The old factory was reborn as an arts centre.','旧工厂改造为艺术中心，重获新生。'))
BIRTH=[['古诺斯语 burðr 等形式；相应古英语 ġebyrd','出生；二者都有更早的承载、生育词族背景'],['中古英语 birthe → 英语 birth','出生、诞生；与 bear 承载、生育有历史亲缘']]
W('birth','英 /bɜːθ/；美 /bɜːrθ/','出生；诞生；出身',
 '生命来到世上的那个过程；想法、组织的开始，也借用诞生来表达。',
 '现代形式经中古英语 birthe，受到古诺斯语出生名词的影响，对应更早古英语 ġebyrd。远源属于 bear 承载、生育词族；不是现代把 bear 随意改成 bir 再加 th。',BIRTH,
 'give birth 生育；the birth of an idea 一个想法的诞生；from birth 自出生起。by birth 可说出身、出生所属背景。',
 'give birth to；at birth；from birth；the birth of a movement。',
 'birth 是出生这件事，born 常放在 be born 中描述某人出生；birthday 才是生日这个日期或周年。',
 ('The photograph was taken soon after the baby’s birth.','这张照片拍摄于宝宝出生后不久。'),('The small meeting marked the birth of a new organization.','那次小型会议标志着一个新组织的诞生。'))
W('childbirth','英 /ˈtʃaɪldbɜːθ/；美 /ˈtʃaɪldbɜːrθ/','分娩；生孩子',
 '专门说把孩子生下来的过程，而不是每年庆祝的生日。',
 'child 孩子 + birth 出生；中古英语已有相应复合词。',C('child 孩子','birth 出生','childbirth','分娩这一过程'),
 'during childbirth 分娩期间，experiences of childbirth 分娩经历。通常不可数，不用 a childbirth 来说某人的生日。',
 'during childbirth；after childbirth；a book about childbirth。',
 'childbirth 强调分娩过程；birth 范围更广，还能说一个城市、想法的诞生；birthday 是生日。',
 ('The book describes different personal experiences of childbirth.','这本书描述了不同个人的分娩经历。'),('The documentary explores how families prepare for childbirth.','纪录片探讨家庭如何为孩子出生作准备。'))
W('birthrate','英 /ˈbɜːθreɪt/；美 /ˈbɜːrθreɪt/','出生率',
 '把出生人数放到一定人口和时间范围里比较，而不只看一共出生几个孩子。',
 'birth 出生 + rate 比率；也常分写 birth rate。',C('birth 出生','rate 比率','birthrate','一定人口、时期中的出生比例指标'),
 'a rising birthrate 上升的出生率，a declining birthrate 下降的出生率。阅读统计时还要看它使用的时间和人口口径。',
 'the national birthrate；a falling birthrate；changes in the birthrate。',
 'birthrate 是出生率，不是总出生人数；也不应直接与 fertility rate 生育率当成处处完全相同的指标。',
 ('The chart compares birthrates in three regions.','图表比较了三个地区的出生率。'),('The report examines the reasons for the falling birthrate.','报告探讨出生率下降的原因。'))
W('bearish','英 /ˈbeərɪʃ/；美 /ˈberɪʃ/','像熊的；看跌的；对前景悲观的',
 '动物义是像熊；财经报道里则常表示认为价格或前景会往下走。',
 'bear 熊 + -ish 像……的。金融用法接 bear 的市场看跌者义；这属于动物名词的另一种引申，不是 bear 忍受加后缀。',B+[['bear 动物及市场看跌者义 + -ish → bearish','像熊的；认为价格会跌或前景欠佳的']],
 'be bearish on a market 对某市场看跌，a bearish outlook 悲观的前景判断。它说的是判断，不保证之后价格真的下降。',
 'a bearish forecast；turn bearish；be bearish on something。',
 'bearish 看跌，bullish 看涨；不要把熊掌往下、牛角往上当成已证实的金融词源故事。',
 ('The article takes a bearish view of demand for the product.','文章对这种产品的需求前景持悲观看法。'),('Some analysts remained bearish despite the recent price rise.','尽管近期价格上涨，一些分析人士仍然看跌。'),sources=['https://en.wiktionary.org/wiki/bearish#English','https://dictionary.cambridge.org/dictionary/english/bearish'])
W('bugbear','英 /ˈbʌɡbeə/；美 /ˈbʌɡber/','令人烦恼或害怕的事；老大难',
 '有件事像个老在眼前晃的怪物，让你一想到就烦或担心。',
 'bug 在这里是吓人之物的旧义，不是现代昆虫或程序漏洞义；加 bear 熊，早期指吓人的怪物，后来成为反复困扰人的事情。',C('bug 旧义：吓人之物','bear 熊','bugbear','吓人的怪物 → 令人反复烦恼的事'),
 'a particular bugbear 特别让人烦的一件事；my biggest bugbear 我最烦的事。英式表达中很常见，也可指难解决的担忧。',
 'a major bugbear；a particular bugbear of mine；a longstanding bugbear。',
 'bugbear 不是昆虫和熊杂交的动物，也不是特指软件 bug；要从吓人、烦人的旧意象理解。',
 ('Unclear instructions are a particular bugbear of mine.','说明写得不清楚，是我特别烦的一件事。'),('Parking remains a major bugbear for local residents.','停车问题仍是当地居民的一大烦心事。'))
W('bearskin','英 /ˈbeəskɪn/；美 /ˈberskɪn/','熊皮；熊皮制品；熊皮高帽',
 'bear 指材料来源，skin 指皮；仪仗语境里，材料名还可以代指那顶高帽。',
 'bear 熊 + skin 皮，形成复合名词；再以材料代称传统使用该材料的高帽。',C('bear 熊','skin 皮','bearskin','熊皮；由这种材料命名的服饰'),
 'a bearskin rug 熊皮地毯；a bearskin cap 熊皮高帽，省略后也能说 a bearskin。具体实物是否使用传统材料，还要看说明。',
 'a bearskin cap；a bearskin rug；guards in bearskins。',
 'bearskin 是动物熊的分支，不是承受皮肤；cap 的意思来自约定的服饰名称，不能把所有熊皮制品都叫帽子。',
 ('The museum label described the old bearskin cap.','博物馆标签介绍了那顶旧熊皮高帽。'),('An antique bearskin rug appeared in the catalogue.','目录中出现了一张古董熊皮地毯。'))
R('B2812','熊；另源的承载、忍受、生育','BEAR：熊与承载分两条来路','动物一支独立看；动词一支用肩上承着东西，串起承担、忍受、带来结果与生育。',
 '名词来自古英语 bera，动词来自 beran。born 是旧过去分词分化出的出生形式；birth 与生育词族有历史亲缘，不是熊生孩子的联想。',
 'bear → bearer、bearing、bearable → unbearable → unbearably；forbear → forbearance；born → reborn；birth → childbirth、birthday、birthplace、birthright、birthrate。动物支 bearish、bugbear、bearskin 另放一组。',
 [['承载、忍受与克制','bear · bearer · bearing · bearable · unbearable · unbearably · forbear · forbearance'],['出生及其相关词','born · reborn · birth · childbirth · birthday · birthplace · birthright · birthrate'],['动物名的复合与比喻','bearish · bugbear · bearskin']],
 'be born 出生，通常其他承载用 borne；bearing 可说举止或关系；bearish 看跌来自市场中 bear 的名词义。',
 'Bear in mind that a small change can make the wait more bearable.\n\n记住，小小的改变也能让等待更容易忍受。',
 'bear bearer bearing bearable unbearable unbearably forbear forbearance born reborn birth childbirth birthday birthplace birthright birthrate bearish bugbear bearskin')
if __name__ == '__main__':save('continuation_20261029_bp',ROOTS,WORDS)
