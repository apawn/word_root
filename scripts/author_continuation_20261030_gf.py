"""Principal, deny, quote and finger: names, evidence and practical extensions."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
P=[['拉丁 prīnceps、词干 prīncip-','居首者、首领；材料与第一、取得有关'],['拉丁 prīncipālis → 法语 principal → 英语 principal','居首、主要的；主要人物、主要金额']]
W('principal','/ˈprɪnsəpəl/','主要的；校长、负责人；本金',
 '一堆原因里领头的那个是 principal reason；学校里领头的人可以是 principal；一笔生息的钱，原本那一大块是 principal。',
 '经法语接拉丁 prīncipālis，来自 prīnceps 首领、居首者。后者历史材料与 prīmus 第一、capere 取得有关，现代不能硬切成 prin + cip + al 后逐个照字面翻。',P,
 'the principal reason 主要原因，the school principal 校长，principal and interest 本金和利息。名词校长用法尤常见于美式英语。',
 'the principal reason；a principal investigator；the school principal；principal and interest。',
 'principal 主要的、负责人、本金；principle 原则。两者通常同音，拼写靠意思分，不靠听音分。',
 ('The principal reason for the delay was bad weather.','延误的主要原因是天气恶劣。'),('The payment covers interest but does not reduce the principal.','这笔付款偿付利息，但没有减少本金。'),sources=['https://www.etymonline.com/word/principal'])
W('principally','/ˈprɪnsəpəli/','主要地、以……为主',
 '不是说只有这一个原因，而是把分量最大、最居中的那项挑出来：主要是它。',
 'principal + -ly 的副词对应；中古英语已有相应形式。它接主要这支，不是校长本人做某事的专用副词。',P+[['principal + -ly → principally','以主要部分或原因而言 → 主要地']],
 'principally because 主要因为，principally concerned with 主要涉及，principally used for 主要用于。比 mainly 稍正式。',
 'principally because；principally concerned with；principally used for。',
 'principally 可换成 mainly 理解，in principle 是原则上；principally 不等于“根据原则地”。',
 ('The room is used principally for meetings.','这个房间主要用来开会。'),('The delay was principally caused by missing documents.','延误主要由文件缺失造成。'))
W('principality','/ˌprɪnsɪˈpæləti/','公国；君主、亲王统治的领地',
 '沿着首领、统治者那一支走：先是统治者的地位、权力，再拿来叫他统治的那片地方。',
 '经法语 principalité 等接晚期拉丁 prīncipālitās，由 prīncipālis + 状态名词后缀形成。现代可对照 principal + -ity，但不是校长地盘，也不是 principle 原则的名词。',P[:1]+[['晚期拉丁 prīncipālitās → 法语 principalité','居首地位、君主权力'],['英语 principality','统治权 → 相应领地、国家']],
 'a small principality 小公国，the ruler of a principality 公国统治者。具体中文爵位译名要看历史制度，不能拿英语 prince 一律译成某国王子。',
 'a small principality；the ruler of a principality。',
 'principality 是领地或国家名称类词，principal 是主要的或负责人；municipality 市镇、自治市另有来路。',
 ('The novel is set in a small mountain principality.','小说以一个山间小公国为背景。'),('The map shows the boundaries of the former principality.','地图标出了昔日公国的疆界。'),sources=['https://www.etymonline.com/word/principality'])
R('B3939','居首、主要；首领和主要部分','PRINCIPAL：把排在首位的那一个挑出来','主要原因 → principally 主要地；首领、统治地位 → principality；主要金额 → 本金。',
 '同一个居首画面，放在原因里说主要，放在人群里说负责人，放在钱里说本金。公国沿的是统治地位那条历史线。',
 'prīnceps/prīncip- → prīncipālis → principal；principal + -ly；prīncipālitās → principalité → principality。',
 [['主要与主要地','principal · principally'],['统治地位到领地','principality']],
 'principal/principle 通常同音，主要的、负责人、本金与原则靠拼写分；principality 不是校长办公室。',
 'The report is principally concerned with the principal causes of the crisis.\n\n报告主要讨论危机的主要原因。','principal principally principality')
W('deniability','/dɪˌnaɪəˈbɪləti/','可否认性；能够否认知情或参与的余地',
 '出了事，还能说“我不知道、我没参与”，而且一时难证明你说假话；这块回旋空间就是 deniability。',
 'deny → deniable → deniability；y 后接元音开头的派生材料改写 i，-able 对应 -ability 形成性质名词。不是说否认越大声就越有 deniability。',
 [['拉丁 dēnegāre → 法语 denier → deny','否定、拒绝承认'],['deny → deniable → deniability','能否认的 → 可否认性、否认余地']],
 'plausible deniability 是还能提出看似可信的“不知情、未参与”说法；maintain deniability 保留否认余地。常见于政治、组织责任、小说情节。',
 'plausible deniability；maintain deniability；a degree of deniability。',
 'denial 是否认这个行为或说法，deniability 是能否认的余地；plausible deniability 不证明一个人确实无辜。',
 ('The character avoids written orders to preserve deniability.','这个人物避免下书面命令，以保留否认的余地。'),('The emails left the director with little deniability.','这些邮件让主管几乎没有否认的余地。'))
R('B3524','否认、拒绝承认及否认余地','DENY：把某个说法挡回去，说不是这样','deny → denial 否认；undeniable → undeniably 无可否认；denier 否认者；deniability 否认空间。',
 '分清否认正在发生、否认者是谁、有没有可能否认。undeniable 则从另一面说：事实明摆着，难以挡回去。',
 'dēnegāre → denier → deny；deny/deniable 与 denial、deniability；un- + deniable → undeniable → undeniably。',
 [['否认与否认者','deny · denial · denier'],['可否认与难以否认','deniability · undeniable · undeniably']],
 'denial/deniability 行为与余地；undeniable 说难否认，不是没人曾经否认；denier 另有纺织计量同形词。',
 'He issued a denial, but the signed letter left little deniability.\n\n他发表了否认声明，但签了名的信几乎没给他留下否认余地。','deny denial denier deniability undeniable undeniably')
Q=[['拉丁 quotus → 中世纪拉丁 quotāre','第几个 → 编号、标出位置'],['法语 coter 等 → 英语 quote','标出处 → 引用原话；报出价格']]
W('quotable','英 /ˈkwəʊtəbəl/；美 /ˈkwoʊtəbəl/','值得引用的、适合摘引的',
 '一句话短、准、醒目，别人一听就想拿来复述；quotable 常夸这种容易被记住、被引用的特点。',
 'quote 去末尾 e + -able，可供、值得被引用。这里的值得引用不保证内容就真实。',Q+[['quote + -able → quotable','可以、适合或值得引用的']],
 'a quotable line 值得摘引的一句，highly quotable 很适合引用，quotable remarks 容易被摘引的话。',
 'a quotable line；a quotable phrase；highly quotable。',
 'quotable 是适合引用，quoted 是已经被引用；一句话可以很 quotable，却还没人真的 quoted it。',
 ('The speech contained several quotable lines.','演讲里有几句很值得摘引的话。'),('Her answer was brief, clear and highly quotable.','她的回答简短清楚，很适合被引用。'))
W('unquote','英 /ˈʌnkwəʊt/；美 /ˈʌnkwoʊt/','引文结束〔口头标记〕',
 '写字能画右引号，说话看不到标点，于是直接说 unquote：刚才引的那段到此为止。',
 'un- + quote，和电报、口述时把引号读出来的习惯有关。quote 开引，unquote 关引；现代 quote unquote 连着说还可带怀疑、讽刺。',Q+[['quote / unquote 口述标点','开始引用 / 引文到此结束']],
 'quote, ... unquote 把原话框起来；his quote unquote expert 可暗示所谓专家。讽刺来自语气和上下文，单纯标引文时不必有讽刺。',
 'quote, … unquote；quote unquote〔亦可带讽刺〕。',
 'unquote 结束引文，不是声称上一句话完全没发生；not quote 才是直接否定引用这个动作的普通结构。',
 ('She said, quote, I will be there, unquote.','她说，原话是“我会到场”，引文结束。'),('He described the delay as, quote, a minor inconvenience, unquote.','他把延误称为，原话是“一点小麻烦”。'),sources=['https://www.etymonline.com/word/quote','https://www.merriam-webster.com/dictionary/unquote'])
R('B3158','标出位置、引用与报价','QUOTE：先能指出原文在哪，再把原话拿出来','quote → quotation 引语、报价；quotable 值得引用；misquote 引错；unquote 关上口头引号。',
 '旧义从给章节编号、标出处起步，后来走到引原话；商用又能说报价格。不要把每个 quote 都当名人名言。',
 'quotus → quotāre → coter/quote；quote + -able；mis- + quote；un- + quote；quotation 是对应名词。',
 [['引用及可引用','quote · quotation · quotable'],['引用中的操作','misquote · unquote']],
 'quotable/quoted 值得引与已经引；quote/quotation 都可有报价义；unquote 是口头引文结束标记。',
 'The line is quotable, but please do not misquote it.\n\n这句话值得引用，不过请别引错。','quote quotation quotable misquote unquote')
F=[['古英语 finger → 中古英语 finger/fynger','手指，日耳曼语旧词'],['英语 finger','手指 → 用手指触摸、演奏、指出某人']]
W('finger','英 /ˈfɪŋɡə/；美 /ˈfɪŋɡər/','手指；用手指触摸；指出、指认',
 '手上能弯曲的一根指头；作动词就把手指的动作借出来：摸弄东西，或指着某人说就是他。',
 '接古英语 finger，是旧日耳曼语词。更远常被联系到表示五的印欧材料，但关系有不确定性；现代 -er 不是人后缀，不能拆成 fing + 做事的人。',F,
 'an index finger 食指，run your fingers through your hair 用手指梳过头发，finger a suspect 指认嫌疑人。日常有时把 thumb 拇指和其余 fingers 分开算。',
 'an index finger；run your fingers through；finger someone as。',
 'finger 常说手指，toe 是脚趾；digit 是更宽的指、趾及数字用词。finger someone 指认不自动等于已经证明有罪。',
 ('She ran her fingers through her hair.','她用手指梳了梳头发。'),('A witness fingered him as the man at the door.','一名证人指认他就是当时在门口的人。'),sources=['https://www.etymonline.com/word/finger'])
W('fingered','英 /ˈfɪŋɡəd/；美 /ˈfɪŋɡərd/','用手指摸过、指认了；有某种手指的',
 '先看结构：He fingered the fabric 是他用手指摸布；形容词里的 fingered 则可说长着某种手指。',
 '动词 finger + -ed 可成过去式、过去分词；另有 finger + -ed 具有……手指的形容词构造，常与前面描述一起出现。',F+[['finger + -ed','过去触摸、被指认；另一构造表有相应手指']],
 'fingered the material 摸了摸布料，was fingered as 被指认为；long-fingered hands 手指修长的双手。形容词构造不必表示过去发生。',
 'fingered the fabric；was fingered as；long-fingered hands。',
 '-ed 读 /d/；fingered 不像 needed 那样加出 /ɪd/ 音节。动词过去式与具有某种特征的形容词，要靠句子分。',
 ('He fingered the edge of the fabric while thinking.','他一边思考，一边用手指摸着布边。'),('Her long-fingered hands moved across the piano keys.','她修长的手指在钢琴键上移动。'))
W('fingernail','英 /ˈfɪŋɡəneɪl/；美 /ˈfɪŋɡərneɪl/','手指甲',
 '手指尖那片硬硬的甲；finger 先把部位限定在手上，再由 nail 说是哪种东西。',
 'finger + nail，中古英语已有组合。nail 在此是指甲，不是钉子；同一个 nail 的不同义靠搭配分。',F[:1]+[['finger + nail → fingernail','手指上的甲']],
 'trim your fingernails 修剪手指甲，a broken fingernail 断裂的指甲，under your fingernails 指甲缝里。',
 'trim your fingernails；a broken fingernail；under your fingernails。',
 'fingernail 手指甲，toenail 脚趾甲；fingertip 指尖还包括皮肤部位，不只那片甲。',
 ('There was paint under his fingernails.','他的指甲缝里有油漆。'),('She caught a broken fingernail on the wool.','她断裂的指甲勾住了毛线。'))
W('fingerless','英 /ˈfɪŋɡələs/；美 /ˈfɪŋɡərləs/','无手指的；露指的〔手套〕',
 '手套把手掌裹住，却把手指留在外面；fingerless gloves 是常见画面。说人时也可直接表示没有手指。',
 'finger + -less，没有。修饰手套时说手套没有完整覆盖手指的部分，不是穿手套的人没手指。',F[:1]+[['finger + -less → fingerless','没有手指；手套缺少完整指部覆盖']],
 'fingerless gloves 露指手套，常方便敲键盘、抓握等；有些款式留半截指套，也照样这样称呼。',
 'fingerless gloves；a pair of fingerless gloves。',
 'fingerless gloves 露着手指，mittens 连指手套是把多数手指放在同一袋里；两个设计关注点不同。',
 ('She wore fingerless gloves while typing in the cold room.','她在冷房间里戴着露指手套打字。'),('The shop sells both mittens and fingerless gloves.','店里既卖连指手套，也卖露指手套。'))
R('B2678','手指与触摸、指认；手指组成的名称','FINGER：先看一根手指，再看它做什么','finger → fingered；finger + nail/tip/print；forefinger 指前面的食指；fingerless 手套让手指出来。',
 '手指能摸、能指、能按弦，还会留下指纹。复合词大多很直观，但 finger 自己末尾的 -er 不表做事的人。',
 'finger 古英语旧词；finger + -ed/-less；finger + nail/tip/print/board；fore- + finger。',
 [['基本词与动作','finger · fingered'],['指的部位、编号与痕迹','fingernail · fingertip · forefinger · fingerprint'],['工具和衣物','fingerboard · fingerless']],
 'finger/toe 手指与脚趾；fingernail/fingertip 指甲与整个指尖；fingerless gloves 不等于 mittens。',
 'She touched the fingerboard with her fingertips, leaving faint fingerprints.\n\n她用指尖碰了指板，留下淡淡的指纹。','finger fingered fingernail fingertip forefinger fingerprint fingerboard fingerless')
if __name__=='__main__':save('continuation_20261030_gf',ROOTS,WORDS)
