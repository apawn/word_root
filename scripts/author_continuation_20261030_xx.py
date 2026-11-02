"""Common past forms and considering: granting, revealing, affecting and directing."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'A1756':dict(words=['grant','granted'],label='grant → granted：准予与承认',note='准许、给予的借词形成 granted，也常有承认某点的表达。'),
 'C1608':dict(words=['reveal','revealed'],label='reveal → revealed：撤去帷幕、显露',note='re- 在这个旧组合里是撤去遮盖的作用，不按再盖一次理解。'),
 'C0401':dict(words=['affect','affected'],label='affect → affected：受到作用；装出的样子另分支',note='影响义接 afficere；装出姿态义另经 affectare 相关路线，保留分支区别。'),
 'C1131':dict(words=['approve','approved'],label='approve → approved：检验、认可与批准',note='好的、可靠的词族与检验、认可相连，过去词尾读 d。'),
 'C1404':dict(words=['arrest','arrested'],label='arrest → arrested：使停住、扣留',note='站立、停留的词族，经使停住发展为逮捕与阻止继续。'),
 'B3432':dict(words=['identify','identified'],label='identify → identified：认出同一个、确定身份',note='相同词族经法语进入英语，identified 把 y 变 i 加 ed。'),
 'C0415':dict(words=['refer','referred'],label='refer → referred：提到、查阅与转交',note='带回、报告的词族扩展为指称、参考、提交处理；重读后双写 r 加 ed。'),
 'C1488':dict(words=['extend','extended'],label='extend → extended：向外伸展、延长',note='空间、时间、范围均可扩展，extended 也常描述较长、扩大的。'),
 'C0351':dict(words=['reduce','reduced'],label='reduce → reduced：带回、降到较小状态',note='由较早带回、转到另一状态的意义，发展为减少、降低。'),
 'C0705':dict(words=['remain','remained'],label='remain → remained：留下与继续保持',note='停留词族延伸到状态一直不变，常接形容词。'),
 'C1209':dict(words=['direct','directed'],label='direct → directed：给方向与组织行动',note='摆直、定向词族发展为引导、指向、导演。'),
 'B3929':dict(words=['consider','considering'],label='consider → considering：把事情放进考虑',note='considering 常说正在权衡，也能在 considering the weather 等结构里把一个条件纳入判断。'),
}
W('granted','英 /ˈɡrɑːntɪd/；美 /ˈɡræntɪd/','准许、给予了；承认；grant 的过去式和过去分词',
 '把别人请求的许可、机会、资源正式给出去，是 granted；讨论中把某一点承认下来，也可以用 grant。',
 'grant + -ed，/t/ 后增加 /ɪd/。grant 经盎格鲁法语 granter、graunter 等准予、保证词形进入英语，更早形式的来源分析不完全一致。',
 [['盎格鲁法语相关词形 → 中古英语 grant','准许、保证、给予'],['grant + -ed → granted','过去准予、给予；被承认的']],
 'granted permission 获准、准予许可；granted a request 答应请求；granted an extension 准许延期；take something for granted 视为理所当然。',
 'permission was granted；had been granted access。','granted 常有正式准许、给予的语气。take someone for granted 可以说把某人的付出当成当然；take something for granted 也可以说未经质疑便认定它是真的。',
 ('The school granted permission to use the hall.','学校准许使用礼堂。'),('She realized that she had taken her friend’s help for granted.','她意识到自己一直把朋友的帮助当成了理所当然。'),sources=['https://en.wiktionary.org/wiki/granted#English','https://en.wiktionary.org/wiki/grant#English'])
W('revealed','/rɪˈviːld/','揭示、透露了；显露出来；reveal 的过去式和过去分词',
 '把遮住的东西揭开，让别人看见原来隐藏的情况，就是 revealed；揭开帷幕与透露消息共享显露的感觉。',
 'reveal + -ed，/l/ 后读 /d/。reveal 经古法语 reveler 接拉丁 revēlāre，re- 撤回遮盖与 vēlāre 遮盖相连，较早 vēlum 是帷幕、遮盖物等。',
 [['拉丁 vēlum、vēlāre → revēlāre → 法语、英语 reveal','帷幕、遮盖 → 撤去遮盖、揭示'],['reveal + -ed → revealed','已显露、已透露；被揭开的']],
 'revealed a secret 透露秘密；revealed the pattern 揭示规律；revealed that ... 显示……；newly revealed 新披露的。',
 'was revealed later；revealed by the records。','reveal 看使隐藏的东西显露出来；discover 看某人发现原先不知道的事。The test revealed ... 是检测让某情况显现，someone discovered ... 则把发现者放在主语位置。',
 ('The old photographs revealed how much the street had changed.','旧照片显示出这条街变化有多大。'),('She revealed the surprise only when everyone had arrived.','直到大家都到了，她才揭晓那个惊喜。'),sources=['https://en.wiktionary.org/wiki/revealed#English','https://en.wiktionary.org/wiki/reveal#English'])
W('affected','/əˈfektɪd/','受到影响、触动；做作的、刻意装出的〔另分支〕',
 '外面的事在一个人或东西身上留下作用，是 affected；说一种语气、姿态 affected，则常是在说它像装出来的，需要另认这一分支。',
 'affect + -ed，/t/ 后增加 /ɪd/。影响义关联拉丁 afficere、affectus，由 ad- 与 facere 做的词族形成；装出姿态义另经拉丁 affectāre、法语 affecter 的路线发展。',
 [['拉丁 afficere、affectus → affect 影响义 → affected','作用于、触动 → 受到影响'],['拉丁 affectāre、法语相关路线 → affect 装出义 → affected','刻意采取姿态 → 做作的']],
 'affected by the weather 受天气影响；deeply affected 深受触动；affected areas 受影响地区；an affected manner 做作的举止。',
 'has affected the result；seemed affected。','affected 影响了与 effected 实现了不同，后者来自 effect 作动词。a person affected by the news 说受到消息触动，an affected smile 则常说笑得不自然、刻意。',
 ('The weather affected the timing of the event.','天气影响了活动的时间安排。'),('His overly formal manner seemed affected.','他过分正式的举止显得有些做作。'),sources=['https://en.wiktionary.org/wiki/affected#English','https://en.wiktionary.org/wiki/affect#English'])
W('approved','/əˈpruːvd/','批准、认可了；经过批准的；approve 的过去式和过去分词',
 '检查或考虑后说“可以、合格、同意”，就是 approved；一个方案得到正式许可，也常用这个词。',
 'approve 末尾已有 e，加 -d，/v/ 后读 /d/。approve 经古法语接拉丁 approbāre，由 ad- 与 probāre 检验、认可组成，较早 probus 表好的、可靠的。',
 [['拉丁 probus、probāre → approbāre → 法语、英语 approve','合格、可靠 → 检验、认可'],['approve 去 e + -ed → approved','认可过、批准了；获准的']],
 'approved the plan 批准计划；approved of the idea 赞同想法；an approved design 获准的设计；was approved by the committee 获委员会批准。',
 'officially approved；has been approved。','approved a plan 常说正式批准；approved of a plan 常说觉得好、赞同。获得许可与个人评价可以有关联，但两种结构表达的重点不同。',
 ('The committee approved the revised design.','委员会批准了修改后的设计。'),('Her parents approved of her decision to study art.','她的父母赞同她学习艺术的决定。'),sources=['https://en.wiktionary.org/wiki/approved#English','https://en.wiktionary.org/wiki/approve#English'])
W('arrested','/əˈrestɪd/','逮捕、扣留了；阻止了继续发展；arrest 的过去式和过去分词',
 '让某个人不能继续走、被扣留，是 arrested 的逮捕义；让锈蚀、破坏等进程停住，也保留使停下的词源画面。',
 'arrest + -ed，/t/ 后增加 /ɪd/。arrest 经古法语 arester 接重建的通俗拉丁 *arrestāre，含 ad- 与 restāre 留下、停住，较早联系 stāre 站立。星号表示重建形式。',
 [['拉丁站立、停留词族 → *arrestāre → 法语 arester → arrest','使停住、扣留 → 逮捕、阻止继续'],['arrest + -ed → arrested','过去扣留；被阻止继续的']],
 'was arrested 被逮捕；arrested the spread 阻止蔓延；arrested development 停滞的发育、发展〔具体语境〕。',
 'arrested later that day；the process was arrested。','arrested 在警务语境常说逮捕，在材料、发展等语境可说被阻止、停住。arrest 的使停下义比日常逮捕义更宽，读时靠对象判断。',
 ('The man was arrested outside the station.','那名男子在车站外被逮捕了。'),('The coating arrested the spread of rust.','这层涂层阻止了锈蚀继续蔓延。'),sources=['https://en.wiktionary.org/wiki/arrested#English','https://en.wiktionary.org/wiki/arrest#English'])
W('identified','/aɪˈdentɪfaɪd/','认出、确定了；鉴定、查明了；认同、产生共鸣〔相应结构〕',
 '把眼前的人、物与一个身份对上号，是 identified；把问题从复杂情况里找出来，也可以说查明、识别出了。',
 'identify 的 y 变 i，加 -ed → identified，末尾元音后读 /d/。identify 借法语 identifier，接 identité、identique 的相同词族，较早是拉丁 idem 同一个；-ify 是使成为、建立关系的动词形式。',
 [['拉丁 idem → 法语相同、身份词族 → identify','同一个 → 认出身份、确定相同关系'],['identify 变 y 为 i + -ed → identified','认出、查明；相应认同结构的过去形式']],
 'identified the bird 认出了鸟的种类；identified the problem 查明了问题；identified as ... 被确定为……；identified with the character 对角色有共鸣。',
 'was later identified；identified by its markings。','identified someone as ... 是把某人确定为某个身份；identified with someone 是认同、共鸣。identify the cause 侧重把原因找准，explain the cause 侧重把原因讲明白。',
 ('She identified the bird by its call.','她根据叫声认出了那种鸟。'),('Many readers identified with the main character.','许多读者对主人公产生了共鸣。'),sources=['https://en.wiktionary.org/wiki/identified#English','https://en.wiktionary.org/wiki/identify#English'])
W('referred','英 /rɪˈfɜːd/；美 /rɪˈfɜːrd/','提到、指称了；查阅了；转交、推荐了；refer 的过去式和过去分词',
 '把话、问题或人带向另一个对象，是理解 referred 的线索：话指向什么、资料去哪里查、问题交给谁处理，都可以由后面的结构说明。',
 'refer 末尾重读，双写 r 再加 -ed → referred，词尾读 /d/。refer 经法语及直接拉丁路线接 referre，re- 回与 ferre 带、承载组成带回、报告、提交等意义。',
 [['拉丁 re- + ferre → referre → 法语、英语 refer','带回、报告、提交 → 提及、参考、转交'],['refer 双写 r + -ed → referred','过去提到、查阅；被转交、称为']],
 'referred to the report 查阅了、提到了报告〔依语境〕；referred to her as an expert 称她为专家；referred the question to the team 把问题交给团队。',
 'the matter was referred；referred back to earlier notes。','refer to 后的报告可能是提及对象，也可能是查阅资料，靠动词周围的信息区分。refer to someone as ... 是把某人称作……；refer something to someone 是交给别人处理。',
 ('She referred to her notes before answering.','回答前，她查阅了笔记。'),('The question was referred to the design team.','这个问题被交给了设计团队处理。'),sources=['https://en.wiktionary.org/wiki/referred#English','https://en.wiktionary.org/wiki/refer#English'])
W('extended','/ɪkˈstendɪd/','延长、扩大了；延伸的、较长的；extend 的过去式和过去分词',
 '让原来的长度、时间或范围向外多伸一段，就是 extended。可以拉长一张桌子，也可以延长一场旅行。',
 'extend + -ed，/d/ 后增加 /ɪd/。extend 经法语等接拉丁 extendere，ex- 向外与 tendere 伸展构成；英语过去形式规则变化。',
 [['拉丁 ex- + tendere → extendere → 法语、英语 extend','向外伸展、展开'],['extend + -ed → extended','已延长、已扩大；延长的、较广的']],
 'extended the deadline 延长截止时间；an extended stay 较长的停留；extended the table 把桌子拉长；extended family 大家庭、较广的亲属圈。',
 'an extended period；has been extended。','extended 的扩大可以在空间、时间，也可以在群体范围。extended family 把父母、孩子之外的其他亲属也纳入范围；extended stay 常说停留时间较长。',
 ('They extended their stay by two days.','他们把停留时间延长了两天。'),('The path was extended to reach the lake.','小路被延长，一直通到湖边。'),sources=['https://en.wiktionary.org/wiki/extended#English','https://en.wiktionary.org/wiki/extend#English'])
W('reduced','英 /rɪˈdjuːst/；美 /rɪˈduːst/','减少、降低了；缩减的、优惠的；reduce 的过去式和过去分词',
 '把数量、程度往较小的位置带，是 reduced；票价降下来、噪声低下来，都能这样说。',
 'reduce 末尾已有 e，加 -d，/s/ 后词尾读 /t/。reduce 经法语等接拉丁 redūcere，re- 往回与 dūcere 带领组成带回、转到某状态，后来常用于使更少、更低。',
 [['拉丁 re- + dūcere → redūcere → 法语、英语 reduce','带回、转变状态 → 减少、降低'],['reduce 去 e + -ed → reduced','已经降低；较低、缩减后的']],
 'reduced the noise 降低噪声；reduced prices 优惠价格、降价后的价格；reduced to ten 降到十；reduced by ten 减少十。',
 'greatly reduced；a reduced ticket price。','reduced to 指最后降到的数，reduced by 指减少的量。reduced a problem to two questions 则是把复杂问题归结、化简成两个问题。',
 ('The new windows reduced the noise from the street.','新窗户降低了街上传来的噪声。'),('The price was reduced from fifty pounds to forty.','价格从五十英镑降到了四十英镑。'),sources=['https://en.wiktionary.org/wiki/reduced#English','https://en.wiktionary.org/wiki/reduce#English'])
W('remained','/rɪˈmeɪnd/','留下了；仍然保持某状态；remain 的过去式和过去分词',
 '别人走了，自己还在；情况变了，某个状态还没变，都可以说 remained。',
 'remain + -ed，/n/ 后读 /d/。remain 经古法语 remanoir 的 remain- 词干接拉丁 remanēre，re- 留在后面与 manēre 停留相连。',
 [['拉丁 manēre、remanēre → 法语 → remain','停留、留在后面'],['remain + -ed → remained','过去留下；某状态仍持续']],
 'remained silent 仍保持沉默；remained open 仍然开放；remained at home 留在家；little remained 几乎没剩下什么。',
 'remained unchanged；the question remained unanswered。','remained 后可直接接形容词描述状态，如 remained calm。remained to be done 表示还留待完成；remained unanswered 表示问题仍未得到回答。',
 ('The door remained open throughout the meeting.','会议期间，门一直开着。'),('Only a few people remained after the concert.','音乐会后，只有几个人留了下来。'),sources=['https://en.wiktionary.org/wiki/remained#English','https://en.wiktionary.org/wiki/remain#English'])
W('directed','/dɪˈrektɪd/，也读 /daɪˈrektɪd/','指引、指向了；指导、导演了；按要求安排的',
 '给人或事情一个方向，让行动朝目标走，就是 directed；告诉别人怎么走、带领演出、把镜头对准一个方向都能用。',
 'direct + -ed，/t/ 后增加 /ɪd/。direct 接拉丁 dīrigere、dīrectus 的摆直、定向词族，较早联系 regere 引导、使直；动词也有拉丁形式的借入背景。',
 [['拉丁 regere → dīrigere、dīrectus → 英语 direct','引导、摆直 → 指向、指导'],['direct + -ed → directed','过去指引、导演；被引向某处的']],
 'directed us to the entrance 指引我们去入口；directed the film 执导电影；directed at children 面向儿童；as directed 按照指示。',
 'directed by ...；attention directed toward the screen。','directed a film 说组织、指导影片创作；acted in a film 说出演。directed someone to a place 常说指路，directed someone to do something 则常说指示其行动。',
 ('The volunteer directed us to the side entrance.','志愿者指引我们去侧门。'),('She directed the school play last year.','她去年导演了学校的戏剧演出。'),sources=['https://en.wiktionary.org/wiki/directed#English','https://en.wiktionary.org/wiki/direct#English'])
W('considering','/kənˈsɪdərɪŋ/','正在考虑、认为；考虑到、鉴于〔相应结构〕',
 '把一种可能拿来认真权衡，是 considering；说 considering the weather，则是先把天气这个条件放进判断，再看事情做得怎样。',
 'consider + -ing，直接加。consider 经法语接拉丁 cōnsīderāre 仔细察看、思量，更远与星辰 sidus 相连的解释有讨论，不把观星故事当成确定词源。',
 [['拉丁 cōnsīderāre → 法语、英语 consider','仔细察看、思量'],['consider + -ing → considering','进行中的考虑；把某条件纳入判断']],
 'considering a move 正考虑搬家；considering changing the date 考虑改日期；considering the cost 考虑到费用；all things considered 综合考虑〔相关形式〕。',
 'is considering the offer；quite good considering the circumstances。','consider doing 是考虑做某事，通常不写 consider to do；consider someone to be ... 是另一种结构，表示认为某人是……。considering the weather 可在整句里交代判断背景。',
 ('We are considering changing the meeting date.','我们正考虑更改会议日期。'),('Considering the weather, the event went very well.','考虑到当时的天气，活动办得很顺利。'),sources=['https://en.wiktionary.org/wiki/considering#English','https://en.wiktionary.org/wiki/consider#English'])
def extend_lessons():
 extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_xx',ROOTS,WORDS)
 extend_lessons()
