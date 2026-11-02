"""Common verb forms: support reading through spelling, sound and sentence roles."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'B3103':dict(words=['suck','sucks'],label='suck → sucks：吸入与糟糕的口语评价',note='古英语吸吮动词，负面口语评价为后起用法。'),
 'B2880':dict(words=['hurt','hurts'],label='hurt → hurts：受到伤害与感到疼',note='与古法语撞击词有关，s 标三单；过去式、分词仍是 hurt。'),
 'B3717':dict(words=['regard','regarded'],label='regard → regarded：留意、看作与评价',note='法语 regarder、regard 等借入，re- 在旧词中可加强；ed 在 d 后读 id。'),
 'A1833':dict(words=['equip','equipped','equipment'],label='equip → equipped：把所需东西配齐',note='法语 équiper 的船只配备词，双写 p 加 ed，与名词 equipment 放同族。'),
 'C0955':dict(words=['expand','expanded'],label='expand → expanded：向外展开、变大',note='ex- 向外与拉丁 pandere 展开；d 后的 ed 多一个音节。'),
 'B2496':dict(words=['feed','feeding','food'],label='feed → feeding：把所需的食物、材料送进去',note='feed 接古英语 fedan，与 food 旧同族；持续供给也延伸到机器和内容。'),
 'C0498':dict(words=['grade','grades'],label='grade → grades：一级一级的等级与评定',note='拉丁 gradus 经法语借入，s 可标复数等级、成绩，也可标评分动词三单。'),
 'B3074':dict(words=['highlight','highlights'],label='highlight → highlights：亮出来的重点、精彩片段',note='英语 high 与 light 组合，明亮部分到重点、强调；名词复数与动词三单同形。'),
 'B3843':dict(words=['hope','hopes','hoped','hoping'],label='hope → hoped：希望与期待的过去',note='古英语 hopian 的本族希望词；保留词尾 e 加 d，与 hop 双写 p 的 hopped 分开。'),
 'C1130':dict(words=['promote','promoting','promotion'],label='promote → promoting：往前推动',note='拉丁 pro- 与 movere、promot- 材料，英语去 e 加 ing。'),
 'C1072':dict(words=['reply','replied'],label='reply → replied：把回答送回去',note='法语 replier 接拉丁 replicare 折回、回应，过去式改 y 为 i 加 ed。'),
 'C1189':dict(words=['request','requests'],label='request → requests：提出需要对方做的事',note='名词法语 requeste 接拉丁 requisita；动词有名词转用与法语借入分析。'),
}
W('sucks','/sʌks/','吸、吮；糟透了〔第三人称单数；后义为口语〕',
 '吸管把水吸上来、机器把空气吸进去，是 sucks 的动作义。口语说某事 sucks，则是在直接抱怨它糟糕、令人不满。',
 'suck + -s，/k/ 后读 /s/。suck 接古英语 sucan 等吸吮材料；糟糕的评价义是后来的口语发展，不能按每个字面场景硬译。',
 [['古英语吸吮词 → suck','吸入、吮吸'],['suck + -s → sucks；另有后起俚语义','某物吸入；某件事很糟']],
 'sucks air in 把空气吸入；sucks up water 吸水；This sucks. 这真糟糕。',
 'The pump sucks water through a pipe. 泵把水从管里吸过来。口语评价较直白，正式表达可按语境改用 disappointing、unpleasant 等。',
 'sucks at something 是不擅长某事的随意说法；sucks something in 是吸进去。句中结构不同，不把负面评价套到机械动作里。',
 ('The machine sucks dust into a container.','机器把灰尘吸进容器。'),('It sucks that the concert was cancelled.','音乐会取消了，真让人扫兴。'),sources=['https://en.wiktionary.org/wiki/sucks#English','https://en.wiktionary.org/wiki/suck#English'])
W('hurts','英 /hɜːts/；美 /hɜːrts/','疼；使疼痛；伤害、损害〔第三人称单数〕',
 '可以是身体某处疼，也可以是一句话刺痛人，或一个变化损害某种利益。hurts 都在说某种伤害正在产生。',
 'hurt + -s，/t/ 后读 /s/。hurt 与中古英语 hurten、古法语 hurter 撞击有关；更早是否有本族词影响存在不同看法。',
 [['古法语撞击等材料 → 中古英语 hurten → hurt','撞伤 → 使疼、受到伤害'],['hurt + -s → hurts','某处疼；某人、某事造成伤害']],
 'My arm hurts. 我的手臂疼。That hurts her feelings. 那伤了她的感情。',
 'hurts the business 损害生意；it hurts to lose 输了让人难受。',
 'My foot hurts 是脚疼；He hurts his foot 是他伤到了脚。过去式仍是 hurt，不能因词尾 t 再造 hurted。',
 ('My shoulder hurts when I lift this bag.','我提这个包时肩膀疼。'),('It hurts to hear that they do not trust us.','听到他们不信任我们，心里很难受。'),sources=['https://en.wiktionary.org/wiki/hurts#English','https://en.wiktionary.org/wiki/hurt#English'])
W('regarded','英 /rɪˈɡɑːdɪd/；美 /rɪˈɡɑːrdɪd/','看待、认为；注视了〔过去式、过去分词〕',
 '目光放到某人身上，心里也给出一个判断：“我把他看成什么样的人。”regarded 常把这样的看待放到过去或被动结构里。',
 'regard + -ed，原词末尾 /d/ 后读 /ɪd/。regard 经法语 regard、regarder 等路径接看守、留意的日耳曼背景；re- 在旧构形中可加强。',
 [['法语 regard、regarder 等 → regard','留意看 → 以某种态度看待'],['regard + -ed → regarded','看待、注视发生了；be regarded as 被认为是']],
 'be regarded as 被看作；highly regarded 备受推崇；widely regarded as 普遍被认为是。',
 'regarded him as a friend 把他当作朋友；a highly regarded teacher 一位受人尊敬的教师。',
 'regarded as 后接身份、性质等判断；regarded with 后可接怀疑、尊敬等态度。regarded 不保证评价一定是正面的。',
 ('She is widely regarded as an excellent teacher.','大家普遍认为她是一位出色的教师。'),('He regarded the new plan with some suspicion.','他有些怀疑地看待这个新计划。'),sources=['https://en.wiktionary.org/wiki/regarded#English','https://en.wiktionary.org/wiki/regard#English'])
W('equipped','/ɪˈkwɪpt/','配备了；具备所需条件的〔过去式、过去分词及分词形容词〕',
 '出发或开工之前，把要用的东西准备在手边：equipped 就是已经配齐了。也可以把知识、技能当作做事所需的装备。',
 'equip 重读末音节、末尾为单个元音字母加 p，双写 p 加 -ed：equipped。/p/ 后 ed 读 /t/。equip 借法语 équiper，早期常说船只的配员、配备。',
 [['法语 équiper → equip','配备船只等 → 为人、场所等准备所需东西'],['equip → equipped','双写 p 加 ed；已经配备或有能力应对']],
 'equipped with 配有……；equipped to do 有条件、能力做……；well equipped 配备齐全的。',
 'equipped with a projector 配有投影仪；better equipped to solve problems 更有能力解决问题。',
 'equipped with 常介绍配了什么；equipped to 后常介绍能做什么。equipment 是不可数的设备名词，不是 equipped 的另一种时态。',
 ('The room is equipped with a large screen.','房间配有一块大屏幕。'),('The training left us better equipped to handle unexpected problems.','培训让我们更有能力处理突发问题。'),sources=['https://en.wiktionary.org/wiki/equipped#English','https://en.wiktionary.org/wiki/equip#English'])
W('expanded','/ɪkˈspændɪd/','扩大、扩展了；展开的、扩充的〔过去式、过去分词〕',
 '原来卷着、占地小或范围窄，现在向外摊开、铺大了：expanded 把这个变化说成已经发生，或把扩充后的版本拿出来。',
 'expand + -ed，/d/ 后 ed 读 /ɪd/。较早 ex- 向外 + 拉丁 pandere 展开，经法语、拉丁相关路径到英语。',
 [['拉丁 ex- 与 pandere → expand','向外展开 → 扩大范围、体积等'],['expand + -ed → expanded','范围已经变大；内容已经增补']],
 'an expanded edition 扩充版；expanded services 扩大的服务范围；expanded into another area 扩展到另一领域。',
 'expanded the discussion 展开讨论；expanded its range 扩充产品范围。',
 'expanded 可以是不及物“自己变大了”，也可以是及物“把某物扩展了”。例如 the service expanded 与 they expanded the service，主语角色不同。',
 ('The library expanded its collection of children’s books.','图书馆扩充了儿童图书收藏。'),('The article appeared in an expanded edition of the book.','这篇文章收入了该书的扩充版。'),sources=['https://en.wiktionary.org/wiki/expanded#English','https://en.wiktionary.org/wiki/expand#English'])
W('feeding','/ˈfiːdɪŋ/','喂食、供给、送入；喂养这件事〔现在分词、动名词及相关名词〕',
 '把食物一口口、材料一份份送进去，是 feeding 的画面。对象可以是动物、机器，也可以是不断需要内容的系统。',
 'feed + -ing，直接接 ing。feed 接古英语 fedan，与 food 食物是旧同族关系，不是现代临时改变 food 的元音造词。',
 [['古英语 fedan → feed','给食物、供养 → 提供所需材料等'],['feed + -ing → feeding','正在供给；也能把喂养活动作为名词谈']],
 'feeding the birds 喂鸟；feeding paper into a printer 把纸送进打印机；feeding time 喂食时间。',
 'The birds are feeding. 鸟在进食。feeding something to someone 与 feeding someone，宾语关系不同。',
 'feeding the birds 通常是人喂鸟；the birds are feeding 通常是鸟自己吃东西。动词能及物，也能不及物，不能只凭中文“喂”判断主语。',
 ('She was feeding the birds in the garden.','她正在花园里喂鸟。'),('The operator is feeding paper into the machine.','操作员正在往机器里送纸。'),sources=['https://en.wiktionary.org/wiki/feeding#English','https://en.wiktionary.org/wiki/feed#English'])
W('grades','/ɡreɪdz/','成绩、等级、年级；坡度〔复数〕；评分、分级〔第三人称单数〕',
 '一格一格分出层次：学生得到成绩等级，材料有质量等级，学校有年级。grades 可以数这些格，也可以说某人给作品评分。',
 'grade + -s，/d/ 后读 /z/。grade 借法语 grade 接拉丁 gradus 步、级；英语评分、分级动词再由名词发展。',
 [['拉丁 gradus → 法语 grade → 英语 grade','台阶、级别 → 等级、成绩、年级等'],['grade + -s → grades','多个等级、成绩等；或某人评分']],
 'good grades 好成绩；different grades 不同等级；students in different grades 不同年级的学生。',
 'grades the essays 给作文评分；grades of timber 不同等级的木材。',
 'grades 常说评定结果；scores 常说得分数值。学校制度不同，两者的具体对应不固定。道路 grade 的坡度义也接上升、台阶的空间概念。',
 ('Her grades improved during the year.','她这一年的成绩有所提高。'),('The teacher grades the essays over the weekend.','老师在周末给作文评分。'),sources=['https://en.wiktionary.org/wiki/grades#English','https://en.wiktionary.org/wiki/grade#English'])
W('highlights','/ˈhaɪlaɪts/','亮点、最精彩的部分；高光部位〔复数〕；突出、强调〔第三人称单数〕',
 '整幅画里最亮的一块最容易抓住目光；一场比赛、一天经历里最值得记住的部分，也就成了 highlights。动词则是主动把重点照亮。',
 'high + light → highlight，再加 -s，/t/ 后读 /s/。从画面明亮部分扩到重要、精彩内容；动词用来使某处显眼、强调某点。',
 [['high + light → highlight','亮处 → 显眼、精彩之处'],['highlight + -s → highlights','多个亮点；某人、某材料突出重点']],
 'match highlights 比赛集锦；the highlights of the trip 旅程中最精彩的部分；highlights a problem 突出一个问题。',
 'watch the highlights 看精彩片段；highlights in the hair 头发上挑染的较浅发束。',
 'highlights 可以是剪辑出的精彩片段，也可以只是事情本身的亮点。动词 highlights 不保证在夸奖，也能强调一个严重问题。',
 ('We watched the highlights after the match.','比赛结束后，我们看了精彩集锦。'),('The report highlights a gap in the current plan.','报告指出了现有计划中的一个缺口。'),sources=['https://en.wiktionary.org/wiki/highlights#English','https://en.wiktionary.org/wiki/highlight#English'])
W('hoped','英 /həʊpt/；美 /hoʊpt/','希望、期待过〔过去式、过去分词〕',
 '在过去某一刻，心里朝着一个想要的结果看去，这就是 hoped。它只说当时抱着希望，结果是否实现还要继续读。',
 'hope 去 e + -ed → hoped，原词有 e，只加 d；/p/ 后读 /t/。hope 接古英语 hopian 等希望词。',
 [['古英语 hopian → hope','希望、期待'],['hope 去 e + -ed → hoped','过去希望；或与 have、had 等组成完成结构']],
 'hoped to do 希望能做；hoped that 希望某事；had hoped 原本希望，常为后面的情况作铺垫。',
 'as we had hoped 如我们原先所希望的；hoped for better weather 盼望天气好些。',
 'hoped 一个 p，是希望的过去；hopped 双写 p，是 hop 跳跃的过去。had hoped 常暗示后来不如愿，但也可以接一切确实如愿的句子。',
 ('We hoped to finish before dark.','我们希望天黑前完成。'),('The event went just as we had hoped.','活动进行得正如我们原先所希望的那样。'),sources=['https://en.wiktionary.org/wiki/hoped#English','https://en.wiktionary.org/wiki/hope#English'])
W('promoting','英 /prəˈməʊtɪŋ/；美 /prəˈmoʊtɪŋ/','推广、促进；晋升、提升〔现在分词、动名词〕',
 '把一件事往前推，让它更容易发生、让更多人知道；或把一个人往职位的前面推。promoting 把这几个方向放在进行中的动作里。',
 'promote 去不发音 e 加 -ing。历史接拉丁 pro- 向前 + movere 移动，相关词干 promot- 进入英语。',
 [['拉丁 pro- 与 movere → promot- → promote','往前推动 → 促进、推广、提升'],['promote 去 e 加 -ing → promoting','正在推进；或推广、促进这一活动']],
 'promoting a new book 推广一本新书；promoting cooperation 促进合作；promoting an employee 提拔员工。',
 'a campaign promoting reading 一项推广阅读的活动；promoting someone to manager 把某人提拔为经理。',
 'promoting a product 是推广产品；promoting a person 可指提拔人。宣传、促进、晋升都从向前推扩展，实际宾语决定是哪种推。',
 ('The library is promoting reading through a series of free events.','图书馆正通过一系列免费活动推广阅读。'),('The manager is promoting an experienced colleague to team leader.','经理正把一位有经验的同事提拔为组长。'),sources=['https://en.wiktionary.org/wiki/promoting#English','https://en.wiktionary.org/wiki/promote#English'])
W('replied','/rɪˈplaɪd/','回答、回复了〔过去式、过去分词〕',
 '话传过来了，我把一句话回过去：replied 说这个回应已经发生。',
 'reply 末尾辅音字母加 y，改 y 为 i 加 -ed → replied，末尾 /aɪ/ 后接 /d/。reply 借古法语 replier，接拉丁 replicare 折回、重复、回应。',
 [['拉丁 replicare → 古法语 replier → reply','折回 → 把回应送回去'],['reply → replied','改 y 为 i 加 ed；回答发生了']],
 'replied to an email 回复了一封邮件；replied that 回答说……；replied with a smile 微笑作答。',
 'He replied, “Tomorrow.” 他回答说：“明天。”直接引语可以跟在 replied 后。',
 'reply to a question 中 to 常保留；answer a question 直接接问题。replied 后直接接引语、that 从句，与直接接名词问题不是同一种结构。',
 ('She replied to my message that evening.','她当晚回复了我的消息。'),('He replied that the room was already booked.','他回答说房间已经被预订了。'),sources=['https://en.wiktionary.org/wiki/replied#English','https://en.wiktionary.org/wiki/reply#English'])
W('requests','/rɪˈkwests/','请求、申请；点播要求〔复数〕；请求、要求〔第三人称单数〕',
 '把想让对方做的事提出去，请对方回应：这是 request。requests 可以数几项请求，也可以说某人正在正式提出需要。',
 'request + -s，/t/ 后读 /s/。名词借古法语 requeste，接拉丁 requisita 等材料；动词有英语名词转用和法语 requester 借入的分析。',
 [['拉丁相关索求材料 → 古法语 requeste → request','提出需要、请求'],['request + -s → requests','多项请求；或第三人称主语提出请求']],
 'requests for information 索取信息的请求；handle requests 处理请求；requests a meeting 请求会面。',
 'song requests 点歌；requests that everyone arrive early 要求大家早到。',
 'requests 常比 asks 更正式。a request for something 中 for 接想要的东西；request something 作动词时可直接接所请求的东西。',
 ('The office received several requests for more information.','办公室收到了几项索取更多信息的请求。'),('The form requests a contact number.','表格要求填写一个联系电话。'),sources=['https://en.wiktionary.org/wiki/requests#English','https://en.wiktionary.org/wiki/request#English'])
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_zx',ROOTS,WORDS)
 extend_lessons()
