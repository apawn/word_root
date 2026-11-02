"""External, comedy and grab: boundaries, performance and holding on."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
E=[['拉丁 exter、externus','外面、外部的'],['中古英语 external','外部的；来自系统、组织之外的']]
W('external','英 /ɪkˈstɜːnəl/；美 /ɪkˈstɜːrnəl/','外部的、外面的；外来的',
 '先画一个圈：公司、身体、电脑都是圈；在圈外、从圈外来的，就可以叫 external。',
 '借拉丁 externus 等外部词族，并带 -al 形容词形式。可认外部材料 extern-，但不是把现代 turn 转动塞进 ex + turn + al。',E,
 'external walls 外墙，an external drive 外接硬盘，external funding 外部资金，external factors 外部因素；圈画在哪，外部就相对哪说。',
 'external walls；an external drive；external funding；external factors。',
 'external/internal 外部与内部；external 不自动等于 foreign 外国的。同城另一家组织也可能是 external partner。',
 ('We copied the files to an external drive.','我们把文件复制到了外接硬盘。'),('The project depends on external funding.','这个项目依赖外部资金。'))
W('externally','英 /ɪkˈstɜːnəli/；美 /ɪkˈstɜːrnəli/','在外部、从外部；外表上',
 '东西从外面检查、资金从圈外进来，或者只看表面的样子；都是把观察或动作的位置放到外边。',
 'external + -ly，形成副词；保留外部这一相对关系，并不一定表示动作向外运动。',E+[['external + -ly → externally','在外面、从外面、就外表而言']],
 'externally funded 由外部资助，externally visible 从外部可见，look identical externally 外表看着一样。',
 'externally funded；externally visible；externally identical。',
 'externally 说明在外部或从外部，outwardly 常强调外表表现；externally funded 不译成“往外资助”。',
 ('The study was funded externally.','这项研究由外部机构资助。'),('The two boxes look identical externally.','两个盒子从外面看一模一样。'))
W('externality','英 /ˌekstəˈnæləti/；美 /ˌekstərˈnæləti/','外部性；某活动带给旁人的未计入交易的成本或收益',
 '工厂和顾客做交易，噪声却让旁边没参与交易的居民承担；旁人接到了影响，这就是负外部性的典型画面。也可能是额外好处。',
 'external + -ity，先能说外部这一性质，经济学用法进一步说经济活动溢到交易或决策之外的影响。词根给出外部，具体定义靠学科约定。',E+[['external + -ity → externality','外部性质、外在事物'],['经济学专门化','未充分反映在相应交易、决策里的第三方成本或收益']],
 'a negative externality 负外部性，a positive externality 正外部性；噪声影响旁人和带来未收费的周边好处，分别帮助理解两端。',
 'a negative externality；a positive externality；environmental externalities。',
 'externality 不只是任何发生在室外的事，也不只坏处；external cost 比较具体指外部成本，externality 还包括好处。',
 ('Noise from the factory is a negative externality for nearby residents.','工厂噪声是附近居民承受的一项负外部性。'),('The course uses a public garden to illustrate a positive externality.','课程用一座公共花园来说明正外部性。'),sources=['https://en.wiktionary.org/wiki/externality#English','https://www.merriam-webster.com/dictionary/externality'])
R('B4254','圈外、外表、从外部而来','EXTERNAL：先划定范围，再判断什么在外面','external 外部的 → externally 从外部、就外表而言 → externality 外部性质、经济学外部性。',
 '外部总是相对于一个范围：公司之外未必国家之外。externality 则把视线移到活动旁边，看看谁没参与却受到了影响。',
 'exter/externus → external；external + -ly/-ity。',
 [['外部关系与观察位置','external · externally'],['溢到第三方的影响','externality']],
 'external/foreign 外部不必外国；externally 不一定向外；externality 可好可坏。',
 'An externally funded study examined the factory’s negative externalities.\n\n一项由外部资助的研究考察了工厂的负外部性。','external externally externality')
C=[['希腊 kōmos 与歌唱相关材料 → kōmōidia','欢庆、狂欢中的歌唱和表演'],['拉丁 cōmoedia → 法语 comédie → 英语 comedy','喜剧；历史也包括以圆满结束的叙事']]
W('comedy','英 /ˈkɒmədi/；美 /ˈkɑːmədi/','喜剧；喜剧表演、幽默效果',
 '现代先想让人发笑的故事、舞台表演；历史上的 comedy 有时更看结局走向圆满，不保证通篇都是笑话。',
 '经法语、拉丁语接希腊 kōmōidia，关联 kōmos 欢庆、狂欢与歌唱、歌者材料。不是 com- 一起 + edy；也不把古老村庄说当确定来源。',C,
 'a romantic comedy 爱情喜剧，stand-up comedy 单口喜剧，a comedy series 喜剧剧集，comic timing 对笑点节奏的掌握。',
 'a romantic comedy；stand-up comedy；a comedy series；a sense of comedy。',
 'comedy 是类型、作品或喜剧性，joke 是一条笑话；历史作品名里的 Comedy 不能自动按现代搞笑片理解。',
 ('We watched a romantic comedy on the train.','我们在火车上看了一部爱情喜剧。'),('Much of the comedy comes from the characters misunderstanding each other.','很多笑点来自人物之间的相互误解。'),sources=['https://www.etymonline.com/word/comedy'])
W('comedic','/kəˈmiːdɪk/','喜剧的、制造喜剧效果的',
 '说的是喜剧表演那套效果或本领：一句话什么时候停、什么时候接，都是 comedic timing 的一部分。',
 'comedy 对应 -ic 形容词，词尾 y 不保留，重音、元音也变为 comedic。不是在 comedy 全词后读一个额外 /ɪk/ 就结束。',C+[['comedy → comedic','与喜剧或喜剧效果有关的']],
 'comedic timing 喜剧节奏感，comedic talent 喜剧天赋，a comedic role 喜剧角色。',
 'comedic timing；comedic talent；a comedic role。',
 'comedic 常侧重喜剧艺术、效果；comic 也能表示滑稽、喜剧的，名词还可指漫画。二者很多场合重叠，不必造绝对界线。',
 ('Her comedic timing made the simple line hilarious.','她对喜剧节奏的把握，让一句简单台词变得极好笑。'),('He wanted to try a comedic role after years of serious drama.','演了多年严肃戏剧后，他想试试喜剧角色。'))
W('comedienne','/kəˌmiːdiˈen/','女喜剧演员〔较传统称呼〕',
 'comedian 可以称喜剧演员，comedienne 是特意把性别标出来的传统说法。今天不必见到女演员就换成这个词。',
 '借法语 comédienne，是相应人物名称的阴性形式；可与 comedy、comedian 对照，-ienne 是这里的女性人物形式材料。',C+[['法语 comédienne → 英语 comedienne','女性喜剧演员的称呼']],
 'a talented comedienne 有才华的女喜剧演员，a stage comedienne 舞台女喜剧演员；现代 comedian 也广泛用于女性。',
 'a talented comedienne；a stage comedienne。',
 'comedienne 指演员，不是女性观众；comedian 通常不必限定男性。comedy 是表演类型，comedic 是形容词。',
 ('The review praised her as a gifted comedienne.','评论称赞她是一位有天赋的女喜剧演员。'),('She prefers to be called a comedian rather than a comedienne.','她更喜欢别人称她为 comedian，而不是特意标明女性的 comedienne。'))
R('B4294','欢庆表演的历史，现代喜剧的类型与效果','COMEDY：让人发笑的表演，也有历史上的圆满结局义','comedy 类型、作品 → comedic 相关本领、效果；comedienne 传统女性演员称呼。',
 '先分作品、性质、演员三个位置。早期喜剧传统和今天的笑点有联系，但并不是每个历史 Comedy 标题都等于现代搞笑作品。',
 'kōmos 与歌唱材料 → kōmōidia → cōmoedia/comédie → comedy；comedic 形容词；comédienne 借入人物名。',
 [['作品与效果','comedy · comedic'],['演员称呼','comedienne']],
 'comedy/joke 类型或作品与一条笑话；comedic/comic 常重叠；comedian 可泛指不同性别演员。',
 'The comedienne’s comedic timing lifted the whole comedy.\n\n这位女喜剧演员对节奏的把握，让整部喜剧更加出彩。','comedy comedic comedienne')
G=[['中古荷兰语、低地德语 grabben 等','抓住、攫取'],['英语 grab','突然抓取 → 抓机会、吸引注意；随手取、赶紧吃喝']]
W('grab','/ɡræb/','抓住、抢到；匆忙取用；吸引注意',
 '手一下伸过去把东西拿住；机会也能像东西一样抓，注意力也能被一个画面抓住。',
 '接荷兰语、低地德语等抓取词，具体借入路线有不同说法。现代 grab 是整体；加后缀常双写 b，如 grabbing、grabber、grabby。',G,
 'grab my hand 抓住我的手，grab a coffee 赶紧喝杯咖啡，grab an opportunity 抓住机会，grab attention 抓眼球。',
 'grab my hand；grab a bite；grab an opportunity；grab attention。',
 'grab 比普通 take 更有快速、突然的感觉，但 grab lunch 不必狼吞虎咽或抢别人饭；那是日常赶紧吃个午饭。',
 ('She grabbed my hand before I stepped into the road.','我迈上马路前，她一把抓住了我的手。'),('Let’s grab a coffee before the meeting.','开会前我们赶紧喝杯咖啡吧。'))
W('grabber','英 /ˈɡræbə/；美 /ˈɡræbər/','抓取者、抓取工具；吸引注意的东西',
 '谁在抓、什么工具能抓，都能接 -er；标题一眼就把人抓住，也可以叫 attention grabber。',
 'grab 双写 b + -er，表执行动作的人或物。不是所有 -er 都必须是人，也不一定说抢劫者。',G+[['grab + -er → grabber','抓取的人、工具；抓住注意的事物']],
 'a litter grabber 拾垃圾夹，an attention grabber 吸引注意的东西，a screen grabber 屏幕抓取工具。',
 'a litter grabber；an attention grabber；a screen grabber。',
 'grabber 是人、物名词，grabby 是形容词；一个东西是 attention grabber，不表示它会用实体爪子抢。',
 ('The bright title is an effective attention grabber.','这个醒目的标题很能吸引注意。'),('He used a litter grabber to pick up the can.','他用拾物夹捡起了罐子。'))
W('grabby','/ˈɡræbi/','爱乱抓、爱抢的；贪心的；抢眼的〔口语〕',
 '想拿什么就伸手抓，常带没礼貌、太想占有的感觉；广告很抢眼时也可借来形容抓注意。',
 'grab 双写 b + -y，形成爱抓、带抓取特点的形容词。不是 grabber 抓取者的复数。',G+[['grab + -y → grabby','爱伸手抓取的 → 贪心、强抢注意的']],
 'grabby hands 乱伸的手，a grabby child 爱抢东西的小孩，a grabby headline 很抓眼球的标题。人物义通常带批评。',
 'grabby hands；a grabby child；a grabby headline。',
 'grabby 人物义常指爱占、乱抓，greedy 更直接说贪；grubby 则是脏兮兮，拼写只差一个字母但别混。',
 ('The toddler gets grabby when she is tired.','小女孩累了就爱伸手乱抓东西。'),('The editor wanted a grabby headline.','编辑想要一个抓眼球的标题。'))
W('grapple','/ˈɡræpəl/','扭打、搏斗；努力应对、设法理解；抓钩',
 '两个人近身抓着较劲，谁也没轻松脱开；难题也像这样缠住你，所以 grapple with a problem 是费力处理它。',
 '抓取动词支与 grab 等日耳曼抓握词有联系；抓钩名词经古法语 grapil，名词动词又相互影响。词源资料对动词直接路线处理不同，不硬定为现代 grab 加 -le，也不从 grape 葡萄编故事。',
 [['古法语 grapil → grapple 名词','抓住船等用的钩具'],['抓握动词相关材料与名词作用交汇','抓住、近身扭打'],['英语 grapple with','与困难较劲 → 努力处理、理解']],
 'grapple with a problem 努力处理难题，grapple with the meaning 努力理解意思，grappling hook 抓钩。应对可以正在进行，未必已解决。',
 'grapple with a problem；grapple with the meaning；a grappling hook。',
 'grab 常是一把抓，grapple 突出抓住后较劲；grapple with 不自动等于 solve 已解决。',
 ('The two wrestlers grappled in the centre of the mat.','两名摔跤手在垫子中央扭打。'),('We are still grappling with the meaning of the results.','我们仍在费力理解这些结果的意义。'),sources=['https://www.etymonline.com/word/grapple','https://en.wiktionary.org/wiki/grapple#English'])
R('B3641','迅速抓住；抓人注意；抓着较劲','GRAB：先伸手拿住，再看抓住的是东西还是注意','grab → grabber 抓取的人或物 → grabby 爱抓抢的；grapple 抓握、抓钩历史交汇，现代常说与难题较劲。',
 '抓咖啡是日常赶紧取用，抓注意是比喻。grapple 与 grab 的画面相近，但它的历史路线更复杂，不能只按现代字母硬拼。',
 'grabben 等 → grab；grab + -er/-y 双写 b；grapple 有抓钩借词与抓握动词材料的交汇。',
 [['基本动作和派生','grab · grabber · grabby'],['抓住后较劲','grapple']],
 'grab/take 快速抓与一般取；grabby/grubby 爱抢与脏；grapple with/solve 费力应对与已经解决。',
 'The headline grabbed our attention, but the article grappled with a serious problem.\n\n标题抓住了我们的注意，文章则认真探讨了一个难题。','grab grabber grabby grapple')
if __name__=='__main__':save('continuation_20261030_gi',ROOTS,WORDS)
