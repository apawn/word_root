"""Monthly, spoken, belief and fortunate: grouped forms and common missing bases."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
R('B2693','按月的频率，及 bi- 带来的两种读法','MONTHLY：每月；加 bi- 后频率可能含混','monthly 每月一次；bimonthly 可隔月一次，也可每月两次。',
 'monthly 可以修饰账单，也能作副词说付款频率。bimonthly 的两种约定用法不能靠前缀一个双字就消除，实际安排最好写明。',
 'month + -ly → monthly；bi- + monthly → bimonthly。',
 [['基本按月及双频读法','monthly · bimonthly']],
 'bimonthly 要看是 every two months 还是 twice a month；monthly 本身通常每月，不是每两月。',
 'We pay monthly, but the newsletter comes every two months; its editor calls it bimonthly.\n\n我们每月付款，通讯则每两月发行一次；编辑称它为 bimonthly。','monthly bimonthly')
S=[['古英语 sprecan 等 → speak','说话'],['英语不规则词形 speak/spoke/spoken','原形、过去式、过去分词'],['分词形容词 spoken','说出来的、口头的；以某种方式说话的']]
W('spoken','英 /ˈspəʊkən/；美 /ˈspoʊkən/','口头的、说出的；speak 的过去分词',
 '纸上写的是 written English，嘴里说出来的是 spoken English。词形带过去分词身份，不表示所有搭配都发生在昨天。',
 'speak 的不规则过去分词，与 spoke 过去式对照；可从变化后的词干加 -n/-en 观察旧强变化材料，不是现代英语每个动词都换元音加 n。',S,
 'spoken English 英语口语，the spoken word 口头语言，have spoken 已经说过；soft-spoken 说话温和，well-spoken 谈吐好的。',
 'spoken English；the spoken word；have spoken。',
 'spoke 过去式：She spoke；spoken 分词：She has spoken。口头英语用 spoken English，不写 spoke English 来作同一种定语。',
 ('Her spoken English improved during the trip.','旅行期间，她的英语口语提高了。'),('We have already spoken about the problem.','我们已经谈过这个问题。'))
W('unspoken','英 /ʌnˈspəʊkən/；美 /ʌnˈspoʊkən/','没说出口的；不言而喻、心照不宣的',
 '话没从嘴里出来，但双方可能都知道；也可能只是想说又咽回去，不能见 unspoken 就保证人人心领神会。',
 'un- 不、未 + spoken 说出的，否定是否说出口的状态；不是说语言永远无法表达。',S+[['un- + spoken → unspoken','未说出口 → 默契、隐含等语境义']],
 'an unspoken agreement 默契，an unspoken rule 不成文、默认的规则，unspoken fears 没说出口的恐惧。',
 'an unspoken agreement；an unspoken rule；unspoken fears。',
 'unspoken 未说出口，unspeakable 无法形容、难以启齿等；前者有可能很普通，只是没人明说。',
 ('They had an unspoken agreement not to discuss the past.','他们心照不宣地不谈过去。'),('Her unspoken fears kept her awake.','那些没说出口的恐惧让她无法入睡。'))
R('B2982','说出的口语和没说出口的内容','SPOKEN：先分 speak、spoke、spoken，再看是否说出口','speak → spoken；unspoken 没说出口；outspoken 直言不讳。',
 '分词能描述口头语言，不只用于完成时。un- 否定说出口，outspoken 则说人敢把意见直说，两种方向摆在一起容易记。',
 'speak/spoke/spoken 是不规则词形；un- + spoken；out- + spoken。',
 [['说话与口头形式','speak · spoken'],['没明说与敢直说','unspoken · outspoken']],
 'spoke/spoken 过去式与过去分词；unspoken/unspeakable 没说与难以启齿；spoken English 口语。',
 'The outspoken speaker explained the unspoken rule in clear spoken English.\n\n那位直言不讳的发言者用清楚的英语口语解释了默认规则。','speak spoken unspoken outspoken')
B=[['古英语 gelēafa 等信任、信仰词 → 中古英语 bileve 等','信任、相信；词形受 believe 影响'],['英语 belief / believe','名词 /f/ 与动词 /v/ 的对应形成']]
W('belief','/bɪˈliːf/','相信、信念、信仰',
 '把一件事认作真的，或者把信任放在一个人、价值、信仰上；belief 可以谈相信这件事，也可以谈具体相信的内容。',
 '承接古英语 gelēafa 等旧信任词，中古形式的前段受 believe 类比影响。后来名词末音变成 /f/，和动词 believe /v/ 分开；不是 belief + -e 就必然能造任何动词。',B,
 'belief in someone 对某人的信任，the belief that 相信……的看法，religious beliefs 宗教信仰，beyond belief 难以置信。',
 'belief in；the belief that；religious beliefs；beyond belief。',
 'belief 名词、believe 动词；believe someone 可相信某人的话，belief in someone 更自然对应对其能力、为人等有信任。',
 ('She never lost her belief in the team.','她从未失去对团队的信任。'),('The decision was based on the belief that demand would grow.','决定基于需求会增长的看法。'),sources=['https://www.etymonline.com/word/belief'])
W('disbelief','/ˌdɪsbɪˈliːf/','不相信、难以置信、惊愕',
 '听完消息，第一反应是“怎么可能？”；不一定已做理性反驳，也可能只是惊讶到一下不敢相信。',
 'dis- 否定、反向 + belief 相信，形成不信的状态名词。很多常用搭配突出意外消息带来的震惊。',B+[['dis- + belief → disbelief','不相信；难以相信的惊愕']],
 'in disbelief 难以置信地，stare in disbelief 惊愕地盯着看，suspend disbelief 暂时接受虚构设定。',
 'in disbelief；stare in disbelief；suspend disbelief。',
 'disbelief 常见震惊、不信；doubt 是怀疑、没把握，不必吃惊。suspend disbelief 是进入作品的约定，不等于证明设定真实。',
 ('She stared at the result in disbelief.','她难以置信地盯着结果。'),('The fantasy asks readers to suspend disbelief.','这部幻想作品需要读者暂时接受虚构设定。'))
W('unbelief','/ˌʌnbɪˈliːf/','不信、缺乏信仰〔尤宗教或较正式语境〕',
 '重点可以是没有相信、拒绝某项信仰，而不只是听到消息后一瞬间的惊愕。日常词频不如 disbelief 高，但宗教讨论里有它的位置。',
 'un- 不、无 + belief，已有中古英语对应形式。un- 和 dis- 都可否定，常用语境却分出不同倾向，不能只因中文都叫不信就忽略。',B+[['un- + belief → unbelief','缺乏、拒绝信仰或相信']],
 'religious unbelief 宗教上的不信，faith and unbelief 信与不信，a state of unbelief 不信状态。',
 'faith and unbelief；religious unbelief。',
 'unbelief 常见宗教、较正式的不信状态；disbelief 更常是对某个消息的不信和惊愕。两者不是绝对互斥。',
 ('The essay explores the boundary between faith and unbelief.','文章探讨信仰与不信之间的界线。'),('The character struggles with periods of unbelief.','这个人物挣扎于一段段失去信仰的时期。'))
R('B2927','信任、信仰和认为某事为真；否定各有常见语境','BELIEF：心里接受它是真的，或者把信任放在它上面','believe 动词 ↔ belief 名词；disbelief 不敢信；unbelief 尤常说缺乏信仰。',
 '先分动词、名词，再分两种不信。belief 末尾 /f/，believe 末尾 /v/，拼写和声音一起记。',
 'gelēafa 等旧词 → belief，词形受 believe 影响；dis-/un- + belief。',
 [['相信动作与信念名词','believe · belief'],['不相信的两类常见语境','disbelief · unbelief']],
 'belief/believe 名词与动词，/f/ 与 /v/；disbelief/unbelief 惊愕不信与常见宗教不信倾向。',
 'Her belief was strong, but she listened to the news in disbelief.\n\n她信念坚定，但听到消息时仍难以置信。','believe belief disbelief unbelief')
F=[['拉丁 fortūna → 法语 fortune → 英语 fortune','机遇、命运、运气；后来有财产财富义'],['拉丁 fortūnātus → fortunate','受好运眷顾、幸运的']]
W('fortune','英 /ˈfɔːtʃuːn/；美 /ˈfɔːrtʃən/','运气、命运；大笔财富',
 '命运把怎样的处境带给你，是 fortune；处境又常和财产连着，后来 a fortune 还能是一大笔钱。',
 '经法语接拉丁 fortūna，来自机会、运气相关词。财产义从人的境遇、社会地位等逐渐发展，不是因为幸运的人一定有钱。',F[:1]+[['英语 fortune 的扩展','人生境况、地位 → 财富；a fortune 大笔钱']],
 'good fortune 好运，make a fortune 赚大钱，cost a fortune 贵得要命，tell someone’s fortune 算命、预言命运。',
 'good fortune；make a fortune；cost a fortune；tell someone’s fortune。',
 'fortune 可说运气也可说财富；fortunate 是幸运，不保证富有，wealthy 则直接说有钱。',
 ('It was good fortune that we met that day.','那天能碰上真是好运。'),('The repairs cost a fortune.','维修花了一大笔钱。'))
W('fortunate','英 /ˈfɔːtʃənət/；美 /ˈfɔːrtʃənət/','幸运的、有幸的；带来好结果的',
 '事情恰好朝有利方向发展，自己受了好运照顾；be fortunate to do 就是有幸做成、遇到某事。',
 '接拉丁 fortūnātus 幸运、兴旺的，来自 fortūna。现代可对应 fortune + -ate，但 -ate 此处是形容词末尾，读弱化 /ət/，不按动词 /eɪt/。',F,
 'be fortunate to do 有幸做，fortunate enough to 足够幸运得以，a fortunate coincidence 幸运巧合，fortunate in having 有幸拥有。',
 'be fortunate to do；fortunate enough to；a fortunate coincidence。',
 'fortunate lucky 大量场合相近，fortunate 稍正式；wealthy 是富有，不等于所有幸运的人。',
 ('We were fortunate to find a room at short notice.','我们很幸运，临时还能找到房间。'),('A fortunate coincidence brought them together again.','一个幸运的巧合让他们再次相遇。'))
W('fortunately','英 /ˈfɔːtʃənətli/；美 /ˈfɔːrtʃənətli/','幸运的是、幸好',
 '先告诉听者，接下来这个事实让人松一口气：坏事可能发生，幸好结果没那么糟。',
 'fortunate + -ly，常作整句评价副词。不是说幸运的人做得很幸运，而是说整个结果值得庆幸。',F+[['fortunate + -ly → fortunately','以好运而言；幸好某件事如此']],
 'Fortunately, ... 幸好……，fortunately for us 对我们来说幸运的是，fortunately enough 碰巧幸运地。',
 'Fortunately, …；fortunately for us。',
 'fortunately 幸好，luckily 也常用；fortunate 是形容词，不能直接照副词位置写 Fortunate, we arrived。',
 ('Fortunately, no one was hurt.','幸好没人受伤。'),('Fortunately for us, the last bus was late.','对我们来说幸运的是，末班车晚点了。'))
W('unfortunate','英 /ʌnˈfɔːtʃənət/；美 /ʌnˈfɔːrtʃənət/','不幸的、倒霉的；令人遗憾的、不恰当的',
 '一次坏巧合把事情推向不利；评价某句话 unfortunate，也可能是在委婉说它说得不合适。',
 'un- 不 + fortunate 幸运的，否定好运；具体发展到令人遗憾、选择失当，并非每次都指惨剧。',F+[['un- + fortunate → unfortunate','不幸、不利；不妥、令人遗憾']],
 'an unfortunate accident 不幸事故，an unfortunate choice of words 不恰当的措辞，It is unfortunate that 令人遗憾的是。',
 'an unfortunate accident；an unfortunate choice of words；It is unfortunate that。',
 'unfortunate 可以委婉批评措辞，不一定本人非常倒霉；unlucky 更直接强调运气不佳。',
 ('It was an unfortunate choice of words.','那番措辞很不妥。'),('An unfortunate accident delayed the opening.','一次不幸事故推迟了开幕。'))
W('unfortunately','英 /ʌnˈfɔːtʃənətli/；美 /ʌnˈfɔːrtʃənətli/','遗憾的是、不幸的是',
 '给接下来的坏消息先标一个遗憾态度；常用于礼貌拒绝、说明不利结果，并不总是重大灾难。',
 'unfortunate + -ly，把不利、令人遗憾的性质转为整句评价。也可对照 unfortunately 与 fortunately 的否定关系。',F+[['unfortunate + -ly → unfortunately','遗憾地说，事情不利或不能如愿']],
 'Unfortunately, ... 遗憾的是……，unfortunately for him 对他不幸的是；委婉说明没有名额、无法出席等也常用。',
 'Unfortunately, …；unfortunately for someone。',
 'unfortunately 表遗憾，不是 unfortunately 必须用过去时；Unfortunately, I can’t come 是现在无法来的消息。',
 ('Unfortunately, the tickets are sold out.','遗憾的是，票已经卖完了。'),('I would love to help, but unfortunately I am away that week.','我很想帮忙，可惜那周我不在。'))
R('B4113','运气眷顾及不利、遗憾；形容词和整句评价','FORTUNATE：命运刚好把事情推向好的一边','fortune → fortunate → fortunately；unfortunate → unfortunately 放在否定支一起。',
 '先看运气，不把幸运误解成富有。两个副词常给整句加庆幸或遗憾态度；unfortunate 的措辞不妥义也很实用。',
 'fortūna → fortune；fortūnātus → fortunate；fortunate + -ly；un- + fortunate → unfortunate → unfortunately。',
 [['运气、幸运与庆幸评价','fortune · fortunate · fortunately'],['不利与遗憾评价','unfortunate · unfortunately']],
 'fortunate/wealthy 幸运与富有；fortunate -ate 在此读弱化音；unfortunate words 可说措辞不妥。',
 'Fortunately, the unfortunate delay did not cost us a fortune.\n\n幸好，这次倒霉的延误没有让我们损失一大笔钱。','fortune fortunate fortunately unfortunate unfortunately')
if __name__=='__main__':save('continuation_20261030_gu',ROOTS,WORDS)
