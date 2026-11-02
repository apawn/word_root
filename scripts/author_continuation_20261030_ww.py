"""Very frequent reading words: kids, issues, rights and changes."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'B3555':dict(words=['kid','kids'],label='kid → kids：小孩；小山羊；开玩笑',note='kid 的小山羊义接古诺尔斯语 kið，后来小孩与开玩笑的口语用法常见；现代多义并不等于每条语义过渡都有定论。'),
 'B2868':dict(words=['get','gets'],label='get → gets：得到、变得、理解',note='gets 读 /ɡets/，get 接北欧 geta 及本族同源材料的历史；现代一组 get 短语按搭配理解。'),
 'B4208':dict(words=['issue','issues'],label='issue → issues：议题、问题、刊物期次；发出',note='issue 接拉丁 exire 向外走的法语路线；议题义经过争点等历史发展，不把所有义逐字译成出口。'),
 'C0110':dict(words=['problem','problems'],label='problem → problems：摆在面前的问题',note='problem 接希腊 pro- 在前加 ballein 放、投的词族，经拉丁、法语借入；problems 是现代复数。'),
 'B2649':dict(words=['right','rights'],label='right → rights：权利；纠正、扶正',note='right 继承古英语 riht 直、正、合宜等；rights 常作权利复数，动词也可说扶正。'),
 'B2617':dict(words=['girl','girls'],label='girl → girls：女孩；熟人群体称呼',note='girl 的中古英语材料早期年轻人义不只限女性；现代 girls 以女孩复数为核心，成年人称呼按语体判断。'),
 'B3018':dict(words=['change','changes'],label='change → changes：变化、更换；改变',note='changes 的 /dʒ/ 后增加 /ɪz/，与 changed 的 /d/ 变化分开；零钱义通常不可数，不直接照搬复数。'),
 'A2029':dict(words=['one','ones'],label='one → ones：一个代替词与多个代替词',note='ones 可以代替已知类别的可数复数名词；这是 one 的形式变化，与 one- 的复合构词用法分别理解。'),
 'C0232':dict(words=['include','included'],label='include → included：已经算在里面',note='included 在 /d/ 后读 /ɪd/；included in 说包括在某范围内，费用或名单里算入均可。'),
 'C0739':dict(words=['mile','miles'],label='mile → miles：英里与很远的距离',note='mile 经早期借入接拉丁千步记距材料，miles 是现代复数，也常口语概括很远距离。'),
}
W('kids','/kɪdz/','小孩、孩子们〔口语〕；小山羊；开玩笑〔kid 的第三人称单数〕',
 '日常聊天里 kids 很常指孩子们；农场语境里也可能是小山羊。kid 作动词则说逗弄、开玩笑，单数主语后同样写 kids。',
 'kid + -s，/d/ 后读 /z/。小山羊名 kid 借古诺尔斯语 kið；小孩义后来常见，再有逗弄、开玩笑等口语动词用法。',
 [['古诺尔斯语 kið → 中古英语 kide → kid','小山羊；后来扩展到小孩的口语称呼'],['kid 名词、动词 + -s → kids','多个孩子、小山羊；单数主语开玩笑']],
 'the kids 孩子们；school kids 上学的孩子；kids and adults 孩子和成年人；kids around 开玩笑、闹着玩。',
 'kids playing outside；takes the kids to school。','kids 比 children 更口语。若 farm、goat 等语境明确，kids 也可指小山羊；He kids around 中是动词，不能按孩子们去翻译。',
 ('The kids made a small tent from blankets.','孩子们用毯子搭了一个小帐篷。'),('The goat stayed close to her two kids.','那只母山羊一直靠近它的两只小羊。'),sources=['https://en.wiktionary.org/wiki/kids#English','https://en.wiktionary.org/wiki/kid#English'])
W('gets','/ɡets/','得到、收到；变得；到达；理解等；get 的第三人称单数',
 '东西到了你手里，身体进入新状态，或者想法终于到了脑中，都可以是 gets。它很常用，具体意思常靠后面的词补出来。',
 'get + -s，/t/ 后读 /s/。get 主要接古诺尔斯语 geta，经中古英语 geten 延续；古英语也有同源 gietan，保存在其他旧复合词里。',
 [['古诺尔斯语 geta 等 → 中古英语 geten → get','取得、得到；形成到达、变得、理解等用法'],['get + -s → gets','单数主语现在得到、变得等']],
 'gets tired 变累；gets home 到家；gets a message 收到消息；gets the joke 听懂笑话；gets on with ... 与……相处、继续做〔看结构〕。',
 'gets better；gets to the station。','gets home 通常不加 to，gets to the station 需要 to。gets better 说变好，is better 说处于更好的状态，前者突出变化。',
 ('The room gets very warm in the afternoon.','下午这个房间会变得很暖和。'),('She usually gets home before six.','她通常六点前到家。'),sources=['https://en.wiktionary.org/wiki/gets#English','https://en.wiktionary.org/wiki/get#English'])
W('issues','英 /ˈɪʃuːz, ˈɪsjuːz/；美 /ˈɪʃuːz/','议题、问题；刊物期次；发出、签发、发行〔issue 的第三人称单数〕',
 '会议里要讨论的事是 issues，杂志按期发出的几本也叫 issues。作动词时，则说某机构把通知、证件或刊物发出来。',
 'issue + -s，元音后读 /z/。issue 经法语接拉丁 exire 向外走；发出、发行物与向外较好联系，议题义另经历待解决争点等语义发展。',
 [['拉丁 exire → 法语 issir／issue → 英语 issue','向外走、结果；发出、发行等'],['issue 名词、动词 + -s → issues','多个议题、问题、期次；单数主语发出']],
 'technical issues 技术问题；social issues 社会议题；back issues 过刊；issues a notice 发通知；issues tickets 出票。',
 'discuss the issues；three issues of the magazine。','issues 有时是待讨论的议题，不一定已是严重故障。problem 更直接说需要解决的困难；magazine issues 则是期刊的期次，不能只认问题这一义。',
 ('We discussed the main issues before choosing a plan.','选方案前，我们讨论了几个主要问题。'),('The library keeps the last twelve issues of the magazine.','图书馆保存这本杂志最近十二期。'),sources=['https://en.wiktionary.org/wiki/issues#English','https://en.wiktionary.org/wiki/issue#English'])
W('problems','英 /ˈprɒbləmz/；美 /ˈprɑːbləmz/','问题、困难、难题；problem 的复数',
 '摆在面前、需要想办法处理的事情，是 problems。可以是数学题，也可以是设备不工作、安排有冲突等实际困难。',
 'problem + -s，/m/ 后读 /z/。希腊 pro- 在前 + ballein 放、投的词族形成 problema，早有摆在前面的障碍、问题义，经拉丁、法语借入英语。',
 [['希腊 pro- + ballein 词族 → problema','放到前面 → 障碍、提出的问题'],['拉丁、法语相关形式 → problem；再加 -s → problems','现代需处理的难题、困难']],
 'solve problems 解决问题；technical problems 技术故障；maths problems 数学题；problems with ... ……方面的问题。',
 'a series of problems；problems to solve。','questions 常需要回答，problems 常需要解决。技术语境的 technical problems 通常是故障、运行困难；课堂里的 maths problems 常是练习题。',
 ('We solved the smaller problems before tackling the main one.','我们先解决了小问题，再处理主要问题。'),('The old printer caused problems whenever we needed it most.','每到最需要用的时候，那台旧打印机就出毛病。'),sources=['https://en.wiktionary.org/wiki/problems#English','https://en.wiktionary.org/wiki/problem#English'])
W('rights','/raɪts/','权利；使用、出版等授权权益；纠正、扶正〔right 的第三人称单数〕',
 '一个人能够正当享有、主张的东西，是 rights；出版、演出等语境又可说相应使用权益。right 作动词时，还可以把倒下、偏离的东西扶正。',
 'right + -s，/t/ 后读 /s/，gh 不发音。right 继承古英语 riht 直、正、合宜等材料，权利、正确、右侧等现代义分别发展；rights 的用法看词性。',
 [['古英语 riht → right','直、正、适当等；后来有权利等分支'],['right 名词、动词 + -s → rights','多项权利、授权权益；单数主语纠正、扶正']],
 'rights and responsibilities 权利与责任；human rights 人权；publishing rights 出版权益；film rights 影视改编等相关权利；rights a fallen chair 扶正倒下的椅子。',
 'protect rights；the rights to a story。','rights 作权利时常用复数；right 作形容词说正确时不靠加 s 表复数。The right answers 是多个正确答案，the rights in question 则是这里讨论的权利。',
 ('The poster explains the members’ rights and responsibilities.','海报说明了成员的权利和责任。'),('The publisher bought the rights to the novel.','出版社买下了这本小说的相关出版权利。'),sources=['https://en.wiktionary.org/wiki/rights#English','https://en.wiktionary.org/wiki/right#English'])
W('girls','英 /ɡɜːlz/；美 /ɡɜːrlz/','女孩、少女；女性朋友群体等〔非正式〕；girl 的复数',
 '最常见是多位女孩。熟人说 the girls，也可能指一群女性朋友，具体年龄要靠场景判断。',
 'girl + -s，/l/ 后读 /z/。接中古英语 gerle、girle、gyrle 等，早期年轻人义不只指女性，更早来源未定，后来女孩义成为常用。',
 [['中古英语 gerle／girle／gyrle → girl','年轻人；后来常指女孩、少女'],['girl + -s → girls','多个女孩；部分熟人群体称呼']],
 'boys and girls 男孩女孩；the girls in the class 班里的女孩；a group of girls 一群女孩；a night out with the girls 和女性朋友聚会的一晚。',
 'young girls；the girls on the team。','girls 是复数，girl’s 是一位女孩的，girls’ 是多位女孩的。熟人称成年女性为 girls 有非正式语气，正式说明成年身份时 women 常更合适。',
 ('The girls built the model together after class.','女孩们课后一起搭好了模型。'),('The girls’ team practises on Tuesday evenings.','女子队周二晚上训练。'),sources=['https://en.wiktionary.org/wiki/girls#English','https://en.wiktionary.org/wiki/girl#English'])
W('changes','/ˈtʃeɪndʒɪz/','变化、改动、更换〔复数〕；改变、更换〔change 的第三人称单数〕',
 '原来的样子变了，或安排换了一项，是 changes。一个个改动可以数，单数主语后也可以说它会改变某事。',
 'change 已有 e，加 s；原词末尾 /dʒ/ 后增加 /ɪz/。经法语相关名词、动词形式接拉丁 cambire／cambiare 交换、更换词族。',
 [['拉丁交换词族 → 法语 change／changier 等 → 英语 change','交换、更换 → 改变、变化'],['change 名词、动词 + -s → changes','多项改动；单数主语改变、更换']],
 'make changes 作修改；small changes 小改动；changes to the plan 对计划的改动；changes her mind 改变主意；changes trains 换乘火车。',
 'the latest changes；changes over time。','changes 常数一项项变化；零钱、找零义通常用不可数 change。some changes 是一些改动，some change 在购物语境可能是一些零钱。',
 ('Please highlight the changes you made to the document.','请标出你对文档作出的改动。'),('The colour changes when the paint dries.','颜料干了以后，颜色会变化。'),sources=['https://en.wiktionary.org/wiki/changes#English','https://en.wiktionary.org/wiki/change#English'])
W('ones','/wʌnz/','用来代替复数可数人或物的形式；一的复数、数字 1 等〔看语境〕',
 '前面已经说过一类东西，不想重复名词，可以用 ones：the red ones 就是那些红的。它代替哪类东西，要从上下文找。',
 'one + -s，/n/ 后读 /z/。one 继承古英语 ān，经中古英语 on、oon 等延续；现代起首 /w/ 是后来的读音发展，ones 延伸其同类名词替代用法。',
 [['古英语 ān → 中古英语 on／oon → one','一、单一；后来有替代同类名词的用法'],['one + -s → ones','代替多个同类可数人、物；也可数数字 1 等']],
 'the blue ones 那些蓝的；new ones 新的那些；the ones on the shelf 架子上那些；loved ones 所爱的人、亲人。',
 'these small ones；the ones we chose。','ones 不等于 one’s：ones 是复数形式，one’s 可是泛指一个人的所有格。代替不可数物时，也不能一律用 ones；例如谈水常用 some、that 等适合语境的表达。',
 ('These cups are too small; can we use the larger ones?','这些杯子太小了，我们能用大一点的那些吗？'),('The ones on the top shelf are already labelled.','最上层架子上的那些已经贴好标签了。'),sources=['https://en.wiktionary.org/wiki/ones#English','https://en.wiktionary.org/wiki/one#English'])
W('included','/ɪnˈkluːdɪd/','包括了、算入了；包含在内的；include 的过去式和过去分词',
 '把某项内容放进范围里，已经算进去，就是 included。名单、课程、费用或包装里有什么，都能沿着包含在里面来理解。',
 'include 去末尾 e，加完整 -ed；/d/ 后过去词尾读 /ɪd/。拉丁 in- 在内 + claudere 围、关形成 includere，再借入英语。',
 [['拉丁 in- + claudere → includere → include','围在里面 → 包括、算入'],['include 去 e + -ed → included','过去包括；已经包含的状态']],
 'included in the price 已包含在价格中；included in the list 列在名单里；breakfast included 包括早餐；everyone included 每个人都算在内。',
 'tax included；was included in the report。','The price included breakfast 是价格里已经包含早餐；Breakfast was included in the price 把早餐放到主语位置。两句关系相同，叙述起点不同。',
 ('Breakfast is included in the room price.','房价包含早餐。'),('We included a map with the invitation.','我们随邀请附上了一张地图。'),sources=['https://en.wiktionary.org/wiki/included#English','https://en.wiktionary.org/wiki/include#English'])
W('miles','/maɪlz/','英里〔复数〕；很远的距离；远远地〔口语加强比较等〕',
 '实际路程能用 miles 来量；口语里把距离拉得很远，又能强调远得很，或某方面好出一大截。',
 'mile 已有 e，加 s，/l/ 后读 /z/。mile 经早期日耳曼语借入接拉丁 mille、milia 与千步记距材料，形成古英语 mīl 后延续；古代记距背景与现代单位精确长度分开。',
 [['拉丁 mille／milia 及千步表达 → 早期日耳曼语 → 古英语 mīl → mile','千步记距材料 → 英里单位名'],['mile + -s → miles','若干英里；很远距离；程度很大等引申']],
 'three miles 三英里；miles away 很远，也可说心不在焉；miles better 好得多；miles from anywhere 远离人烟、偏远。现代常见英里约为 1.6 公里。',
 'a few miles；miles better than before。','miles 可真数英里，也可口语夸张说相差很远。three miles away 在数距离，miles better 在加强比较，不能拿距离数值逐字换算成更好。',
 ('The village is about three miles from the station.','村庄离车站大约三英里。'),('The new instructions are miles better than the old ones.','新说明比旧说明好太多了。'),sources=['https://en.wiktionary.org/wiki/miles#English','https://en.wiktionary.org/wiki/mile#English'])
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_ww',ROOTS,WORDS)
 extend_lessons()
