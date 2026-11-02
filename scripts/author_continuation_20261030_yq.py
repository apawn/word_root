"""Common past forms with useful argument patterns and historical word families."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'C0415':dict(words=['suffer','suffered'],label='suffer → suffered：承受与遭遇',note='在下方承担的拉丁词族经法语借入，现代按承受对象区分。'),
 'C1635':dict(words=['visit','visited'],label='visit → visited：去看与访问',note='拉丁看、反复看的词族发展为探访。'),
 'C0751':dict(words=['promise','promised','admit','admitted'],label='promise／admit：提出承诺与准许进入',note='同属拉丁 mittere 及其分词词干的不同前缀支线，不把两个现代词互相派生。'),
 'C1488':dict(words=['attend','attended'],label='attend → attended：把注意伸向与到场',note='朝向伸展的拉丁词族，经法语发展到注意、照料、参加。'),
 'C1487':dict(words=['obtain','obtained'],label='obtain → obtained：取得与持有',note='拉丁持有词族经法语借入，现代核心是取得。'),
 'B3157':dict(words=['gain','gained'],label='gain → gained：获得与增加',note='名动词有北欧、法语等相关历史，现代不强压成唯一来路。'),
 'C0423':dict(words=['file','filed'],label='file → filed：穿线存档、排队；锉磨另源',note='文档与队列接线的词族，锉磨动词另接本族旧词。'),
 'C1131':dict(words=['prove','proved'],label='prove → proved：检验与证实',note='拉丁检验、认可词族经法语等借入，现代还可说结果证明是。'),
 'B4069':dict(words=['purchase','purchased'],label='purchase → purchased：追求取得与购买',note='法国旧追逐、设法取得词义后来专化成花钱买。'),
 'C1188':dict(words=['discuss','discussed'],label='discuss → discussed：打散、细察与讨论',note='历史语义先有打散、考察，再有通过争论检视。'),
 'C0456':dict(words=['found','founded'],label='found → founded：打基础与建立',note='本组讲拉丁 fundare 建立；与 find 的过去式 found、铸造动词分开。'),
}
W('suffered','英 /ˈsʌfəd/；美 /ˈsʌfərd/','遭受、承受；变差、受损〔suffer 的过去式、过去分词〕',
 '有负担压在身上、事情让人不好受，是 suffered 的承受画面；服务质量、表现等变差，也能说 suffered。',
 'suffer + -ed，词尾读 /d/。拉丁 sub- 在下与 ferre 承载形成 sufferre，sub- 在 f 前变为 suf-；经法语 suffrir 等与中古英语借入。',
 [['拉丁 sub- + ferre → sufferre → 法语、英语 suffer','在下方承载 → 忍受、遭受'],['suffer + -ed → suffered','承受过；遭到损害、变差']],
 'suffered a loss 遭受损失；suffered from delays 受延误影响；quality suffered 质量变差。',
 'suffered during the storm；suffered from a lack of time。','suffered a loss 可以直接接损失；suffered from something 常引出使它不好受、受影响的原因。质量作主语时不必想成人的痛感。',
 ('The roof suffered damage during the storm.','屋顶在暴风雨中受损了。'),('The quality of the work suffered because there was too little time.','由于时间太少，工作质量受到了影响。'),sources=['https://en.wiktionary.org/wiki/suffered#English','https://en.wiktionary.org/wiki/suffer#English'])
W('visited','/ˈvɪzɪtɪd/','拜访、探望；参观、访问〔visit 的过去式、过去分词〕',
 '亲自去看看一个人、一个地方，是 visited；今天的网站访问，也借用了去到某处看内容的画面。',
 'visit + -ed，/t/ 后读 /ɪd/。经法语 visiter 接拉丁 vīsitāre，它是看词族的反复或加强形式，与 vidēre 看相连。',
 [['拉丁 vidēre 词族、vīsitāre → 法语 → visit','看、去看 → 探访、参观'],['visit + -ed → visited；现代用途扩展','探望过、访问过；访问网络页面']],
 'visited friends 拜访朋友；visited a museum 参观博物馆；visited the website 访问网站。',
 'visited last summer；places visited on the trip。','visited 通常直接接人或地点：visited the museum。名词 visit 才常用 a visit to the museum 这类结构，别把 to 硬插在动词后。',
 ('We visited our grandparents last Sunday.','我们上周日去看望了祖父母。'),('She visited the website to check the opening times.','她访问网站查看开放时间。'),sources=['https://en.wiktionary.org/wiki/visited#English','https://en.wiktionary.org/wiki/visit#English'])
W('promised','英 /ˈprɒmɪst/；美 /ˈprɑːmɪst/','答应、承诺；预示可能〔promise 的过去式、过去分词〕',
 '把将来要做的事先明确交代给别人，是 promised 的承诺义；某种迹象让人期待好结果，也可用 promise。',
 'promise 已有 e，加 -d，/s/ 后读 /t/，通常两个音节。经古法语 promesse 等接拉丁 prōmittere、prōmissum，历史材料为 prō- 向前与 mittere 送出。',
 [['拉丁 prōmittere、prōmissum → 法语、英语 promise','向前提出、预先表示 → 承诺'],['promise 去 e + -ed → promised','承诺过、被答应；显出某种前景']],
 'promised to help 答应帮忙；promised a reply 答应回复；as promised 如先前承诺的。',
 'promised us a visit；promised to return the book。','promised to do 说明答应做什么；promised somebody something 说明答应给某人什么。词尾 /st/ 连读，别额外加一个 /ɪd/ 音节。',
 ('He promised to return the book on Monday.','他答应周一归还这本书。'),('As promised, she sent us the photographs.','她如约把照片发给了我们。'),sources=['https://en.wiktionary.org/wiki/promised#English','https://en.wiktionary.org/wiki/promise#English'])
W('attended','/əˈtendɪd/','参加、出席；照料、处理〔attend 的过去式、过去分词〕',
 '把人和注意力带到某件事面前，是 attended 的理解线索：人到了会议上，是出席；注意力放到需要上，是处理、照料。',
 'attend + -ed，/d/ 后读 /ɪd/。拉丁 ad- 朝向与 tendere 伸形成 attendere，经法语 atendre 等借入，发展出注意、等候、到场等支线。',
 [['拉丁 ad- + tendere → attendere → 法语 → attend','朝向伸展 → 注意、照料、出席'],['attend + -ed → attended','出席过；已照料、已处理']],
 'attended the meeting 出席会议；attended a course 参加课程；attended to a request 处理请求。',
 'attended by many people；attended to the details。','attended a meeting 直接接活动；attended to something 带 to 时常是留心、处理。有没有 to，会帮助你判断句中是哪一支。',
 ('She attended the meeting on behalf of the team.','她代表团队出席了会议。'),('The receptionist attended to our request at once.','接待员立刻处理了我们的请求。'),sources=['https://en.wiktionary.org/wiki/attended#English','https://en.wiktionary.org/wiki/attend#English'])
W('admitted','/ədˈmɪtɪd/','承认；准许进入、接收〔admit 的过去式、过去分词〕',
 '把一个人放进门，是 admitted 的准入义；把一个事实也接进自己认可的范围，就有承认的用法。后者是帮助理解的画面，实际按搭配来用。',
 'admit 末音节重读，双写 t 加 -ed → admitted；/t/ 后读 /ɪd/。拉丁 ad- 到与 mittere 让去、送组成 admittere，经法语、中古英语发展。',
 [['拉丁 ad- + mittere → admittere → 法语、英语 admit','准许进入、接纳；承认等意义发展'],['admit → admitted','双写 t；承认过、被准许进入']],
 'admitted the mistake 承认错误；admitted that... 承认……；admitted to the college 被学校录取。',
 'admitted being wrong；admitted through the gate。','admitted doing something 可说承认做过某事。be admitted to a place 则多是获准进入、被接收；别把所有 admitted to 都按同一种结构死记。',
 ('He admitted that he had made a mistake.','他承认自己犯了一个错误。'),('Visitors were admitted through the side gate.','参观者获准从侧门进入。'),sources=['https://en.wiktionary.org/wiki/admitted#English','https://en.wiktionary.org/wiki/admit#English'])
W('obtained','英 /əbˈteɪnd/；美 /əbˈteɪnd/','取得、获得〔obtain 的过去式、过去分词〕',
 '原来没有的许可、资料、结果，经过申请、查找或处理拿到了，就是 obtained。重点是取得了所需的东西。',
 'obtain + -ed，/n/ 后读 /d/。法语 obtenir 接拉丁 obtinēre，含 ob- 与 tenēre 持有，历史有取得、占有、实现等义。',
 [['拉丁 ob- + tenēre → obtinēre → 法语 → obtain','持有、占有 → 取得'],['obtain + -ed → obtained','取得过、被获得']],
 'obtained permission 获得许可；obtained information 得到资料；results obtained 获得的结果。',
 'obtained from the archive；obtained through careful testing。','obtained 比 got 通常更正式，常见于报告、申请和研究说明。obtained from 引出资料、物品的来源，obtained by 可引出取得方法。',
 ('They obtained permission to enter the archive.','他们获得了进入档案馆的许可。'),('The information was obtained from old letters.','这些资料来自旧信件。'),sources=['https://en.wiktionary.org/wiki/obtained#English','https://en.wiktionary.org/wiki/obtain#English'])
W('gained','/ɡeɪnd/','获得；增加、增长〔gain 的过去式、过去分词〕',
 '经验、支持、速度比原来多了一些，是 gained 的获得、增加画面；所增加的不一定是钱，也不一定都是好事。',
 'gain + -ed，/n/ 后读 /d/。英语名词有北欧 gagn 与法语相应名词背景，现代动词也接法语 gagner 等；不同词支不压成一条确定来源。',
 [['北欧、法语相关名词与法语 gagner 等 → gain 词族','收益、取得 → 获得、增加'],['gain + -ed → gained','得到了；数量、程度增长了']],
 'gained experience 获得经验；gained support 得到支持；gained speed 加速；gained access 获得进入权限。',
 'gained confidence；gained through practice。','gained experience 说积累了经验，gained speed 说速度增加。gain 接什么宾语，决定增加的是能力、数量、支持还是别的东西。',
 ('She gained confidence through regular practice.','她通过规律练习增强了信心。'),('The train gained speed after leaving the station.','火车驶出车站后加快了速度。'),sources=['https://en.wiktionary.org/wiki/gained#English','https://en.wiktionary.org/wiki/gain#English'])
W('filed','/faɪld/','归档、提交；排成一列行进；锉磨〔过去式、过去分词，分支不同〕',
 '把文件按顺序保存，是 filed 的归档义；人一列列走，也用 file。老方法曾把文件串在线上；用锉刀磨东西则是另一条旧词来源。',
 'file 已有 e，加 -d，/l/ 后读 /d/。文档、队列支经法语 filer 等接拉丁 fīlum 线；古法语已有把文件穿在线上保存的用法。锉磨支接古英语 fīlian、锉刀 fēol。',
 [['拉丁 fīlum → 法语 fil、filer → file','线、串联文书 → 存档、提交；成列行进'],['另一支：古英语锉磨词 → file；各加 -d → filed','锉磨过；或已归档、已列队走过']],
 'filed the documents 归档文件；filed a report 提交报告；filed into the hall 列队走进大厅；filed her nails 锉指甲。',
 'filed under a name；filed through the doorway。','filed a report 常是向机构正式提交或记者发稿，不能总译成放入文件夹。filed into 后接地点时，多看作一列列走进去。',
 ('She filed the letters under the writer’s name.','她按写信人的姓名把信件归档。'),('The students filed into the hall.','学生们列队走进礼堂。'),sources=['https://en.wiktionary.org/wiki/filed#English','https://www.etymonline.com/word/file'])
W('proved','/pruːvd/','证明、证实；结果表明是〔prove 的过去式、过去分词〕',
 '经过证据或实际检验，能看出一件事确实如此，是 proved；事情最后显出某种性质，也可说 proved useful 等。',
 'prove 已有 e，加 -d，/v/ 后读 /d/。拉丁 probāre 检验、认可经古法语 prover 等进入英语，古英语也有相关早期借词；现代分词可见 proved、proven 两形。',
 [['拉丁 probāre → 法语 prover 等 → prove','检验是否可靠、够好 → 证明'],['prove 去 e + -ed → proved','证明了；经过实际情况显出某性质']],
 'proved the claim 证实主张；proved useful 证明有用；proved to be... 结果表明是……。',
 'proved by the evidence；proved harder than expected。','proved 作过去式很常用；过去分词也可用 proven，地区和搭配偏好有差异。proved difficult 后接形容词时，是后来显出困难这个性质。',
 ('The extra time proved useful during the final check.','额外的时间在最后检查时派上了用场。'),('The experiment proved that the method could work.','实验表明这个方法能够奏效。'),sources=['https://en.wiktionary.org/wiki/proved#English','https://en.wiktionary.org/wiki/prove#English'])
W('purchased','英 /ˈpɜːtʃəst/；美 /ˈpɜːrtʃəst/','购买〔purchase 的过去式、过去分词〕',
 '花钱把需要的东西取得，是 purchased。它比 bought 通常更正式，常见于订单、设备、票证等书面说明。',
 'purchase 已有 e，加 -d，/s/ 后读 /t/。盎格鲁法语 purchaser、古法语 porchacier 等含 pur- 向前或加强与 chacier 追逐；设法取得后来专化出购买义。',
 [['法语 pur- + chacier 等 → purchase','追求、设法取得 → 花钱取得'],['purchase 去 e + -ed → purchased','买过、已购得']],
 'purchased online 网上购买；purchased from a shop 从商店购买；newly purchased equipment 新购设备。',
 'tickets purchased in advance；purchased for the project。','purchased 与 bought 在一般购买语境可相近，正式程度不同。名词 purchase 另有抓牢、支点等用法，此处的过去动词先掌握购买即可。',
 ('The tickets were purchased online.','这些票是在网上购买的。'),('The school purchased new equipment for the workshop.','学校为实作课购置了新设备。'),sources=['https://en.wiktionary.org/wiki/purchased#English','https://www.etymonline.com/word/purchase'])
W('discussed','/dɪˈskʌst/','讨论、商议〔discuss 的过去式、过去分词〕',
 '把一件事摊开，从不同角度仔细谈，就是 discussed 的直观画面。历史词义确实经过打散、细察、辩论的发展，今天重点是交换看法。',
 'discuss + -ed，/s/ 后读 /t/。拉丁 dis- 分开与 quatere 摇形成 discutere，分词词干 discuss-；打散义经后期拉丁的考察、研究等发展为讨论，再进入英语。',
 [['拉丁 discutere、discuss- → 后期考察义 → discuss','打散、震散 → 细察、讨论'],['discuss + -ed → discussed','讨论过、被商议过']],
 'discussed the plan 讨论计划；discussed with colleagues 和同事商议；discussed how to proceed 讨论如何继续。',
 'discussed at the meeting；discussed the problem in detail。','discuss 通常直接接主题，如 discussed the problem；with 引出一起讨论的人。the discussion about... 是名词结构，别把 about 机械带进动词后。',
 ('We discussed the plan after lunch.','我们午饭后讨论了这个计划。'),('She discussed the problem with her colleagues.','她和同事们商议了这个问题。'),sources=['https://en.wiktionary.org/wiki/discussed#English','https://www.etymonline.com/word/discuss'])
W('founded','/ˈfaʊndɪd/','建立、创办；以……为基础〔found 的过去式、过去分词〕',
 '先打好基础，再把组织、学校等建立起来，是 founded；一个判断有依据，也可以说 founded on evidence。',
 '建立义 found + -ed，/d/ 后读 /ɪd/。拉丁 fundāre 打基础、建立，经法语借入。find 的过去式 found 是另一条日耳曼历史，其过去分词仍是 found；铸造 found 又另接 fundere。',
 [['拉丁 fundāre → 法语 → 建立义 found','打基础 → 建立、创办'],['found + -ed → founded','创办了；建立在某依据之上']],
 'founded a school 创办学校；founded in 1990 创办于 1990 年；founded on evidence 以证据为基础。',
 'an organisation founded by teachers；a view founded on experience。','find—found—found 是找到；found—founded—founded 是建立。be founded on something 说判断、组织原则等以什么为基础。',
 ('The school was founded by local teachers.','这所学校由当地教师创办。'),('Her view was founded on years of practical experience.','她的看法建立在多年的实践经验之上。'),sources=['https://en.wiktionary.org/wiki/founded#English','https://en.wiktionary.org/wiki/found#English'])
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_yq',ROOTS,WORDS)
 extend_lessons()
