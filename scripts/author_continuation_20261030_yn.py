"""Frequent past verbs: replacement, invitation, statements, and recognition."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'B4159':dict(words=['replace','replaced'],label='replace → replaced：放回、换上与接替',note='re- 与 place 组合，现代替换义既可接被换下者，也可说明换上者。'),
 'A2077':dict(words=['update','updated'],label='update → updated：推进到当前状态',note='up 与 date 组合，信息、软件等语境共享更新到当前的画面。'),
 'B4054':dict(words=['invite','invited'],label='invite → invited：邀请与招致',note='法语借入或从 invitation 反构的历史可能并存，更早构成不强拆。'),
 'C1404':dict(words=['stay','stayed'],label='stay → stayed：停留与保持状态',note='停留、支撑旧词支线有不同分析，本组先掌握普通停留义。'),
 'B3774':dict(words=['represent','represented'],label='represent → represented：使呈现与代表',note='拉丁、法语呈现词族借入，代表义不等于每次重复提交。'),
 'B4004':dict(words=['refuse','refused'],label='refuse → refused：拒绝与不接受',note='古法语 refuser 的较早拉丁来源存在不同分析，保留分歧。'),
 'B3768':dict(words=['earn','earned'],label='earn → earned：以付出换得',note='古英语取得回报词延续，可说钱也可说信任、尊重。'),
 'C0305':dict(words=['declare','declared'],label='declare → declared：清楚说出与正式宣布',note='清楚的拉丁词族形成公开说清楚的动词。'),
 'B2923':dict(words=['attack','attacked'],label='attack → attacked：接战与攻击',note='意大利接合、接战表达经法语发展，与 attach 同族但非现代改字母派生。'),
 'C1119':dict(words=['express','expressed'],label='express → expressed：压出与表达',note='向外压的拉丁材料发展出把内容显露、表达的用法。'),
 'C0496':dict(words=['recognize','recognized'],label='recognize → recognized：认出与认可',note='较早认识词族经多种可能路线进入英语，现代识别与承认分开解释。'),
}
W('replaced','/rɪˈpleɪst/','替换、接替；放回〔replace 的过去式、过去分词〕',
 '把旧东西拿下、把另一个放到它的位置，是 replaced 的替换义；把原来的东西重新放回去，也保留重新放置的画面。',
 'replace 已有 e，加 -d，清音 /s/ 后读 /t/。re- 再、回与 place 放置组合，英语从重新放置发展出用另一物接替原来位置的用法。',
 [['re- + place → replace','重新、放回 → 替换位置'],['replace 去 e + -ed → replaced','换掉了、被接替；重新放回']],
 'replaced the battery 更换电池；replaced by 被……替代；replaced it with a new one 用新的换掉它。',
 'replaced the broken chair；replaced the lid。','She replaced A with B 是用 B 换下 A；A was replaced by B 同样是 B 接替 A。replaced the lid 在开关容器语境里常是把盖子盖回去。',
 ('She replaced the broken chair with a new one.','她用一把新椅子换掉了坏椅子。'),('He replaced the lid and put the jar away.','他把盖子盖回去，将罐子收了起来。'),sources=['https://en.wiktionary.org/wiki/replaced#English','https://en.wiktionary.org/wiki/replace#English'])
W('updated','/ˌʌpˈdeɪtɪd/','更新；告知最新情况〔过去式、过去分词〕；更新后的',
 '原来的信息、版本落后了，把它补到当前这一步，就是 updated；把最新进展告诉别人，也是在更新对方知道的情况。',
 'update 已有 e，加 -d，/t/ 后读 /ɪd/。up- 与 date 日期、使具当前日期的材料组成近代 update，先有动词，再有更新消息、软件等名词用法。',
 [['up- + date → update','把内容推进到当前日期、当前情况'],['update 去 e + -ed → updated','更新过；已获得最新信息']],
 'updated the file 更新文件；updated information 更新后的信息；updated us on progress 告知我们最新进展。',
 'updated every morning；an updated version。','updated somebody on something 常是告知某人某方面的最新情况。动词 update 重音常在后，名词 update 常在前，updated 延续动词构成。',
 ('She updated the address in the file.','她更新了文件里的地址。'),('The manager updated us on the progress of the project.','经理向我们通报了项目的最新进展。'),sources=['https://en.wiktionary.org/wiki/updated#English','https://en.wiktionary.org/wiki/update#English'])
W('invited','/ɪnˈvaɪtɪd/','邀请；招致〔invite 的过去式、过去分词〕',
 '主动请别人来参加、请对方做某事，就是 invited；一种做法像把麻烦请过来，也能比喻成招致。',
 'invite 已有 e，加 -d，/t/ 后读 /ɪd/。invite 可能经法语 inviter 接拉丁 invitāre，也可能从英语更早的 invitation 反构；拉丁词更早构成未定。',
 [['拉丁 invitāre → 法语 inviter；或 invitation 反构 → invite','邀请、招待、召来'],['invite 去 e + -ed → invited','邀请过、被邀请；招致了']],
 'invited us to dinner 请我们吃饭；invited her to speak 邀请她发言；invited criticism 招致批评。',
 'invited to the meeting；invited guests。','invite somebody to a place 或 an event 中 to 后接地点、活动；invite somebody to do something 中后接动作。invited guests 常说受邀来宾。',
 ('They invited us to dinner on Saturday.','他们请我们周六去吃晚饭。'),('She was invited to speak at the meeting.','她受邀在会上发言。'),sources=['https://en.wiktionary.org/wiki/invited#English','https://www.etymonline.com/word/invite'])
W('stayed','/steɪd/','停留、暂住；保持〔stay 的过去式、过去分词〕',
 '人没有离开原来的地方，是 stayed；状态没有改变，也可以说 stayed，如一直醒着、保持安静。',
 'stay + -ed，元音 /eɪ/ 后读 /d/；y 前是元音 a，保留 y。普通停留义涉及法语 estare、estai- 等形式，常接拉丁 stāre 站；支撑义等另有日耳曼、法语支线与不同分析。',
 [['法语停留、站立相关形式 → stay','停住、留下；与支撑等同形支线分别看'],['stay + -ed → stayed','留下了、暂住过；保持某种状态']],
 'stayed at home 留在家；stayed with friends 借住朋友家；stayed awake 一直醒着；stayed calm 保持冷静。',
 'stayed for a week；stayed open until ten。','stayed 后可直接接形容词表示保持，如 stayed calm、stayed open；表示住在哪里常用 at、in、with 等。和 carry 不同，stayed 保留 y。',
 ('We stayed with friends for the weekend.','我们周末住在朋友家。'),('The shop stayed open until ten.','这家店一直营业到十点。'),sources=['https://en.wiktionary.org/wiki/stayed#English','https://www.etymonline.com/word/stay'])
W('represented','/ˌreprɪˈzentɪd/','代表；表现、描绘；构成〔represent 的过去式、过去分词〕',
 '让一个人、一幅图或一个数字把另一件事呈现出来，是 represented 的理解线索：人代表团体，画描绘场面，数字表示数量。',
 'represent + -ed，/t/ 后读 /ɪd/。法语 représenter 接拉丁 repraesentāre 展现、使呈现，与 praesent- 在场的词族相连；这里 re- 的历史用法不能一概翻成现代再做一次。',
 [['拉丁 repraesentāre → 法语 représenter → represent','使呈现、展现 → 代表、描绘'],['represent + -ed → represented','代表过、被表现；表示、构成了']],
 'represented the team 代表团队；represented in the diagram 在图中表示；represented a major change 构成重大变化。',
 'represented by a symbol；represented the group at the meeting。','represented by 在图示里常是由某符号表示，在团体里可说由某人代表。represented a change 不一定有人代理，而是这件事本身意味着一种变化。',
 ('She represented the team at the meeting.','她代表团队参加了会议。'),('Each village was represented by a small dot on the map.','地图上每个村庄都用一个小圆点表示。'),sources=['https://en.wiktionary.org/wiki/represented#English','https://en.wiktionary.org/wiki/represent#English'])
W('refused','/rɪˈfjuːzd/','拒绝〔refuse 的过去式、过去分词〕',
 '别人提出请求、给出东西，你明确不接受或不去做，就是 refused；它强调把这个请求或选择挡在外面。',
 '动词 refuse 已有 e，加 -d，/z/ 后读 /d/。近源是古法语 refuser；更早有接拉丁 refundere 倒回的分析，也有拉丁其他拒绝词混合的分析，不能强定唯一链。',
 [['古法语 refuser → 英语动词 refuse','拒绝；较早拉丁来源分析有分歧'],['refuse 去 e + -ed → refused','拒绝过、被拒绝']],
 'refused the offer 拒绝提议；refused to answer 拒绝回答；refused entry 被拒绝进入。',
 'refused to leave；a request that was refused。','拒绝做某事常用 refused to do。动词 refuse 的 s 读 /z/；垃圾名词 refuse 常前重音、末尾 /s/，与本词形区分。',
 ('He refused to answer the question.','他拒绝回答这个问题。'),('The request was refused because the room was already booked.','因为房间已被预订，这项请求遭到拒绝。'),sources=['https://en.wiktionary.org/wiki/refused#English','https://en.wiktionary.org/wiki/refuse#English','https://www.etymonline.com/word/refuse'])
W('earned','英 /ɜːnd/；美 /ɜːrnd/','挣得；赢得、获得应有回报〔earn 的过去式、过去分词〕',
 '做了工作得到钱，或者付出努力、表现出品质而得到信任、尊重，是 earned。它常让人注意回报是怎样凭付出得来的。',
 'earn + -ed，/n/ 后读 /d/。earn 继承古英语 earnian，较早常联系收获等材料；现代既可接金钱，也可接尊重、认可等结果。',
 [['古英语 earnian → earn','以劳动、付出等取得回报'],['earn + -ed → earned','挣到了、赢得了']],
 'earned money 挣钱；earned respect 赢得尊重；earned a place 赢得位置、名额；earned a reputation 赢得名声。',
 'earned through hard work；earned the trust of the team。','earned 常强调获得的过程或资格；received 主要说收到了。earned respect 是行动换来尊重，可以用同一个回报画面记住。',
 ('She earned extra money by helping at the shop.','她在店里帮忙，挣了一些额外的钱。'),('His careful work earned the trust of the team.','他做事认真，赢得了团队的信任。'),sources=['https://en.wiktionary.org/wiki/earned#English','https://en.wiktionary.org/wiki/earn#English'])
W('declared','英 /dɪˈkleəd/；美 /dɪˈklerd/','宣布、声明；申报〔declare 的过去式、过去分词〕',
 '把某件事清楚、正式地说出来，让别人知道，就是 declared；过关时把应申报的物品报出来，也用 declare。',
 'declare 已有 e，加 -d，词尾读 /d/。法语 declarer 接拉丁 dēclārāre，联系 clārus 清楚、明亮，dē- 在这里常起加强作用，整词是使清楚、公开说明。',
 [['拉丁 clārus、dēclārāre → 法语 → declare','清楚 → 公开讲清、宣布'],['declare 去 e + -ed → declared','宣布了、声明过、申报过']],
 'declared the event open 宣布活动开始；declared that... 声明……；declared the goods 申报物品。',
 'declared in a statement；declared at customs。','declared something open、safe 等结构里，后面的形容词说明正式认定的状态。海关语境的 declared 则是按要求报出物品等信息。',
 ('The organiser declared the festival open.','组织者宣布节日活动开始。'),('She declared the goods at customs.','她在海关申报了这些物品。'),sources=['https://en.wiktionary.org/wiki/declared#English','https://en.wiktionary.org/wiki/declare#English'])
W('attacked','/əˈtækt/','攻击、袭击；抨击〔attack 的过去式、过去分词〕',
 '冲着一个目标施加伤害或强烈反对，是 attacked；可以攻击人、系统，也可以用语言抨击一个方案。',
 'attack + -ed，/k/ 后读 /t/，整体两个音节。attack 经法语 attaquer 接意大利语 attaccare 接合、贴上等用法，接战表达参与攻击义的发展；与 attach 同族，但非现代英语改字母而来。',
 [['意大利语 attaccare、接战表达 → 法语 attaquer → attack','接合、接战 → 攻击'],['attack + -ed → attacked','攻击过、被袭击或被抨击']],
 'attacked the proposal 抨击提案；attacked by an animal 被动物袭击；attacked the problem 着手解决难题〔比喻〕。',
 'attacked in the debate；attacked from several directions。','attacked a proposal 常是强烈批评；attacked a problem 则可以是主动着手解决，抓住朝目标用力的比喻。具体对象会改变中文表达。',
 ('Several speakers attacked the proposal during the debate.','辩论中，几位发言者猛烈批评了这项提案。'),('The castle was attacked from two directions.','这座城堡遭到了来自两个方向的进攻。'),sources=['https://en.wiktionary.org/wiki/attacked#English','https://en.wiktionary.org/wiki/attack#English'])
W('expressed','/ɪkˈsprest/','表达、表示；挤出〔express 的过去式、过去分词〕',
 '把心里原来没显露的意思、感受表现出来，是 expressed；词根更具体的画面是向外压出，今天字面挤出与抽象表达各有用法。',
 'express + -ed，/s/ 后读 /t/。拉丁 ex- 向外与 premere 压形成 exprimere，经法语等进入英语；expressed 的 -ed 接在英语动词上。',
 [['拉丁 ex- + premere → exprimere → 法语等 → express','向外压 → 显露、表达'],['express + -ed → expressed','表达过、被表示；挤出过']],
 'expressed concern 表达担忧；expressed thanks 表示感谢；expressed in words 用语言表达；expressed as a percentage 表示为百分比。',
 'expressed her opinion；expressed in a different way。','expressed 可说感情、观点，也可说数值、关系的表示方式。be expressed as 常用来说明把同一内容写成哪种形式。',
 ('She expressed her thanks in a short letter.','她在一封短信里表达了感谢。'),('The results were expressed as percentages.','结果用百分比表示。'),sources=['https://en.wiktionary.org/wiki/expressed#English','https://en.wiktionary.org/wiki/express#English'])
W('recognized','/ˈrekəɡnaɪzd/','认出、识别；承认、认可〔recognize 的过去式、过去分词〕',
 '看到、听到之后知道这是原来熟悉的谁或什么，是 recognized；进一步承认某种价值、身份，也能用这个词。',
 'recognize 已有 e，加 -d，/z/ 后读 /d/。较早接拉丁 recognōscere，re- 再与 cognōscere 认识；英语可能经法语相关词干或从 recognizance 反构。英式还常写 recognised。',
 [['拉丁 recognōscere → 法语相关形式等 → recognize','再认识、认清；直接进入英语的路线有不同分析'],['recognize 去 e + -ed → recognized','认出了；承认、正式认可了']],
 'recognized her voice 认出她的声音；recognized as 被公认为；recognized the need 承认、认识到需要。',
 'recognized by the team；recognized the person at once。','recognized somebody 是辨认出某人；recognized somebody as... 还可说认可某人的身份、地位。仅凭识别到脸不一定等于熟悉这个人的全部情况。',
 ('I recognized her voice before I saw her.','我还没看到她，就认出了她的声音。'),('The team recognized the need for a simpler plan.','团队认识到需要一个更简单的计划。'),sources=['https://en.wiktionary.org/wiki/recognized#English','https://en.wiktionary.org/wiki/recognize#English'])
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_yn',ROOTS,WORDS)
 extend_lessons()
