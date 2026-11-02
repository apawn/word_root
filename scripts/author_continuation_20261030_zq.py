"""Common past forms: responding, arranging and carrying things through."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'B2632':dict(words=['answer','answered'],label='answer → answered：回应、作答',note='本族回应词有郑重表态的构成背景，现代是普通回复。'),
 'C0254':dict(words=['encourage','encouraged'],label='encourage → encouraged：把勇气放进去',note='法语 en 与 corage 胆量，连到拉丁心的词族。'),
 'C0751':dict(words=['submit','submitted'],label='submit → submitted：交付、服从',note='拉丁在下与送出组成，现代末音节重读使 t 双写。'),
 'C1653':dict(words=['survive','survived'],label='survive → survived：经历以后仍活着、仍存在',note='拉丁超过与活的组合经法语借入。'),
 'B3958':dict(words=['arrange','arranged'],label='arrange → arranged：排成行、安排好',note='法语排入行列词，较早接日耳曼环、行列材料。'),
 'C1534':dict(words=['attract','attracted'],label='attract → attracted：把注意、事物拉过来',note='拉丁 ad 与 trahere 结合，不只说人的外貌。'),
 'B3767':dict(words=['block','blocked'],label='block → blocked：挡住、通不过',note='块状物名词发展出阻挡动词，实体和信息通路都可用。'),
 'C1550':dict(words=['distribute','distributed'],label='distribute → distributed：分开给到各处',note='拉丁 dis 与 tribuere，英语接分词词干。'),
 'B3892':dict(words=['edit','edited'],label='edit → edited：整理、修改到可用',note='editor 逆构、法语及拉丁词干等来源分析均保留。'),
 'B3779':dict(words=['pack','packed'],label='pack → packed：装进包、挤满',note='日耳曼包、捆材料，现代装包、紧密聚集与打包义各有用途。'),
 'C1635':dict(words=['view','viewed'],label='view → viewed：看见、看待',note='法语看见的景象名词接拉丁看词，英语动词后续发展。'),
 'B3138':dict(words=['rate','rated'],label='rate → rated：核定、评分',note='拉丁核定份额词族经法语借入，与斥责的旧 rate 分开。'),
 'C1211':dict(words=['rule','ruled'],label='rule → ruled：准则到统治、判定',note='拉丁直尺、准则及管理动词经不同法语形式借入。'),
 'C1293':dict(words=['separate','separated'],label='separate → separated：把一处变成两处',note='拉丁 se 与 parare，英语名词式形容词与动词读音分化。'),
 'C0226':dict(words=['cite','cited'],label='cite → cited：把材料或理由叫出来',note='拉丁召唤词经法语借入，现代引用、举证据常见。'),
 'C1439':dict(words=['construct','constructed'],label='construct → constructed：把部分搭起来',note='拉丁 con 与 struere，英语动词接 constructus 分词词干。'),
}
W('answered','英 /ˈɑːnsəd/；美 /ˈænsərd/','回答了、回复了；接听了〔过去式、过去分词〕',
 '问题、消息或呼叫来到自己这里，再给它一个回应，就是 answered。回答一道题、回复邮件、接起电话，都接回应的方向。',
 'answer + -ed，结尾读 /d/，w 不发音。answer 继承古英语 andswaru、answarian 等，较早 and- 对着与郑重表态、宣誓词族相连，常有针对指控答复的历史解释。',
 [['古英语回应名词、动词 → answer','针对地表态 → 普通回答、回应'],['answer + -ed → answered','过去回复、作答；回应了呼叫']],
 'answered the question 回答了问题；answered the phone 接了电话；answered an email 回复邮件。',
 'answered correctly 答对了；answered the door 应门、去开门。','answer 通常直接接问题、电话、邮件；reply 常用 reply to。answered the door 是有人敲门后去应门。',
 ('She answered all the questions clearly.','她清楚地回答了所有问题。'),('He answered the phone on the third ring.','电话响到第三声时，他接了起来。'),sources=['https://en.wiktionary.org/wiki/answered#English','https://www.etymonline.com/word/answer'])
W('encouraged','英 /ɪnˈkʌrɪdʒd/；美 /ɪnˈkɜːrɪdʒd/','鼓励了；促使了；受到鼓舞的〔过去式、过去分词〕',
 '让一个人多一些敢做的心气，就是 encouraged。看到好进展，人也会觉得心里有底、更有信心。',
 'encourage + -d，/dʒ/ 后读 /d/。古法语 encoragier 含 en- 与 corage 胆量，后者接心的拉丁词族；英语借入后作规则过去变化。',
 [['法语 en + corage → encourage','使有胆量、心气 → 鼓励、促进'],['encourage 去 e + -ed → encouraged','过去鼓励；受到鼓舞、信心增加']],
 'encouraged her to try 鼓励她尝试；encouraged by the results 因结果而受鼓舞；encouraged discussion 促进讨论。',
 'felt encouraged 受到鼓舞；encouraged participation 鼓励参与。','encourage somebody to do 是鼓励某人做；was encouraged by something 则说明什么让人获得信心。也可说政策、条件促成某种活动。',
 ('The teacher encouraged her to ask more questions.','老师鼓励她多提问。'),('We were encouraged by the early results.','初步结果让我们受到鼓舞。'),sources=['https://en.wiktionary.org/wiki/encouraged#English','https://en.wiktionary.org/wiki/encourage#English'])
W('submitted','/səbˈmɪtɪd/','提交了、呈交了；服从了〔过去式、过去分词〕',
 '把材料交到另一个有权处理、评审的人或机构手里，是 submitted 的提交画面；把自己的行动放到某种权威下，则是服从。',
 'submit 双写 t + -ed → submitted，/t/ 后读 /ɪd/。拉丁 sub- 在下 + mittere 送、放 → submittere，英语借入后，末音节重读影响加词尾时的双写。',
 [['拉丁 submittere → submit','放在下面、交付 → 提交、服从'],['submit 双写 t + -ed → submitted','已经呈交材料；过去服从']],
 'submitted an application 提交申请；submitted the report to the committee 向委员会呈交报告；submitted to the decision 服从决定。',
 'submitted on time 按时提交；submitted for review 已交送审。','submit something to somebody 是把东西提交给谁；submit to something 是服从、接受某种约束。提交不自动代表已经获批。',
 ('She submitted the application before the deadline.','她在截止日期前提交了申请。'),('The report was submitted to the committee for review.','报告已交委员会审查。'),sources=['https://en.wiktionary.org/wiki/submitted#English','https://en.wiktionary.org/wiki/submit#English'])
W('survived','英 /səˈvaɪvd/；美 /sərˈvaɪvd/','幸存了、存活了；保留下来了；比……活得久〔过去式、过去分词〕',
 '一个事件、变化或很长时间已经过去，某人、某物还在，就是 survived。生命可以幸存，文件、建筑、习惯也能保存下来。',
 'survive + -d，/v/ 后读 /d/。经法语 survivre 等接晚期拉丁 supervivere，super- 超过 + vīvere 活；现代既可不及物说活下来，也可直接接经历的事或比谁活得久。',
 [['拉丁 supervivere → 法语 → survive','活得更久、活过某时点 → 幸存、存留'],['survive 去 e + -ed → survived','过去活下来；在变化后仍存在']],
 'survived the storm 经历风暴后幸存；survived for years 存活多年；the records survived 记录保存下来。',
 'survived into the present 延续到今天；survived her husband 比丈夫活得久。','survive an event 直接接事件；survive for ten years 用 for 给持续时间。survived somebody 在人物生平里常指比某人晚去世。',
 ('The old tree survived the storm.','老树挺过了风暴。'),('Only a few letters from that period have survived.','那个时期只有几封信保存下来。'),sources=['https://en.wiktionary.org/wiki/survived#English','https://www.etymonline.com/word/survive'])
W('arranged','/əˈreɪndʒd/','安排了、布置了；改编了〔过去式、过去分词〕',
 '把东西放到合适位置，让顺序、时间或角色搭配起来，是 arranged。椅子排好、会议约好、曲子改成适合另一种乐器，都在安排。',
 'arrange + -d，/dʒ/ 后读 /d/。经古法语 arengier 等，a- 朝向 + rangier 排入行列，较早接日耳曼环、行列的材料；普通整理和商定用途后来广泛发展。',
 [['古法语排入行列词 → arrange','列队、排成行 → 安排、整理'],['arrange 去 e + -ed → arranged','已经布置、约定；为另一演奏形式改编']],
 'arranged the chairs 摆好椅子；arranged a meeting 安排会议；arranged for her to attend 安排她出席。',
 'arranged in rows 排成行；arranged for piano 改编为钢琴曲。','arrange for somebody to do 是安排某人做；arrange to do 是安排自己做。音乐中的 arranged for 某乐器，是为该乐器改编。',
 ('They arranged the chairs in a circle.','他们把椅子摆成一圈。'),('She arranged for a colleague to cover the meeting.','她安排一位同事代为参加会议。'),sources=['https://en.wiktionary.org/wiki/arranged#English','https://www.etymonline.com/word/arrange'])
W('attracted','/əˈtræktɪd/','吸引了；受到吸引的〔过去式、过去分词〕',
 '把东西、注意或人拉到自己这边，是 attracted。磁铁可以吸引铁块，一个活动、想法也能把人的兴趣拉过来。',
 'attract + -ed，/t/ 后读 /ɪd/。拉丁 ad- 朝向在 t 前同化 + trahere 拉 → attrahere，分词 attractus 等接到英语词族。',
 [['拉丁 attrahere、attractus → attract','朝这边拉 → 吸引事物、注意或兴趣'],['attract + -ed → attracted','过去吸引；被某种特征吸引']],
 'attracted attention 引起注意；attracted visitors 吸引游客；attracted to the idea 被这个想法吸引。',
 'attracted by the design 被设计吸引；attracted a large audience 吸引大量观众。','attracted 不只说恋爱或外貌，也常说活动、工作机会、物理吸引。be attracted to something 说明对什么感兴趣、受到什么吸引。',
 ('The exhibition attracted visitors from nearby towns.','展览吸引了附近城镇的游客。'),('She was attracted to the job by the chance to learn.','她因学习机会而对这份工作产生兴趣。'),sources=['https://en.wiktionary.org/wiki/attracted#English','https://en.wiktionary.org/wiki/attract#English'])
W('blocked','英 /blɒkt/；美 /blɑːkt/','挡住了、堵塞了；被阻断的〔过去式、过去分词〕',
 '路上横着一块东西，让后面的东西过不去，就是 blocked。道路、水管、信息、账户访问，都能按通路受阻理解。',
 'block + -ed，/k/ 后读 /t/。block 的块状物名词经法语 bloc 等接日耳曼木块材料，英语后来用作挡住的动词；过去变化再加 ed。',
 [['日耳曼块状物词 → 法语 → block','块状物 → 挡住通路'],['block + -ed → blocked','已经堵住；处于无法通过的状态']],
 'blocked the road 堵住道路；a blocked pipe 堵塞的管道；blocked access 阻止访问。',
 'blocked by a fallen tree 被倒树堵住；blocked the view 挡住视线。','blocked 可以是物理阻挡，也可以是规则、软件阻止。The road is blocked 说明状态；has blocked 则把 block 放进完成式。',
 ('A fallen tree blocked the road.','倒下的树堵住了道路。'),('The tall fence blocked our view of the garden.','高篱笆挡住了我们看花园的视线。'),sources=['https://en.wiktionary.org/wiki/blocked#English','https://en.wiktionary.org/wiki/block#English'])
W('distributed','英 /dɪˈstrɪbjuːtɪd/；美 /dɪˈstrɪbjuːtɪd/','分发了、分配了；分布的〔过去式、过去分词〕',
 '把一整份东西分开，让不同人、地点各拿到一份，是 distributed。若说物体分散在各处，也可描述为 distributed。',
 'distribute + -d，/t/ 后读 /ɪd/。拉丁 dis- 分开 + tribuere 分给 → distribuere，英语接 distribūtus 分词词干；现代过去形式再加 d。',
 [['拉丁 distribuere、distribūtus → distribute','分开给出 → 分发、分配'],['distribute 去 e + -ed → distributed','已经发到各处；在不同地点分布']],
 'distributed the leaflets 分发传单；evenly distributed 均匀分布；distributed among the teams 分给各团队。',
 'distributed across the region 分布于整个地区；widely distributed 广泛分布。','distributed 可以说动作已做，也可以说分布状态。distribute among 强调分给哪些对象，across 强调覆盖哪些地方。',
 ('The volunteers distributed maps to the visitors.','志愿者向访客分发地图。'),('The lights are evenly distributed across the ceiling.','灯均匀分布在天花板上。'),sources=['https://en.wiktionary.org/wiki/distributed#English','https://en.wiktionary.org/wiki/distribute#English'])
W('edited','/ˈedɪtɪd/','编辑了、修改了；剪辑过的〔过去式、过去分词〕',
 '把已有内容删、改、调整，让它更适合阅读、播放或使用，是 edited。可以编辑文章，也可以剪辑影像、修改文件。',
 'edit + -ed，/t/ 后读 /ɪd/，不双写 t，重音不在末音节。edit 有从 editor 逆构、接法语 éditer 或拉丁 editus 的分析；英语较早出版义后扩到修订内容。',
 [['editor 逆构／法语、拉丁相关形式 → edit','出版、整理以便出版 → 修改、剪辑'],['edit + -ed → edited','已经编辑、修订过的']],
 'edited the article 编辑了文章；an edited version 修改版；edited the video 剪辑了视频。',
 'carefully edited 仔细编辑过的；edited for clarity 为更清楚而修改。','edited 是内容做过处理，不能只凭这个词知道删改了多少。editor、edition 较早已有记录，词史不只按现代 edit 加后缀的方向理解。',
 ('She edited the article to make the argument clearer.','她修改了文章，让论证更清楚。'),('We watched an edited version of the interview.','我们看了经过剪辑的访谈版本。'),sources=['https://en.wiktionary.org/wiki/edited#English','https://www.etymonline.com/word/edit'])
W('packed','/pækt/','装好了、打包了；挤满的、紧密的〔过去式、过去分词〕',
 '把东西一件件装进一个包或空间，装得很紧，就成 packed。于是既能说行李装好了，也能说房间里挤满了人。',
 'pack + -ed，/k/ 后读 /t/。pack 接中古英语 pak、pakke，与低地日耳曼包、捆词相连，也有本族旧形承接分析；动词从包、捆等名词用途发展。',
 [['中古英语及日耳曼包、捆词 → pack','包、捆 → 把东西装到一起'],['pack + -ed → packed','已经装好；紧密装满、挤满']],
 'packed her bag 收好了包；a packed room 挤满人的房间；packed with useful ideas 满是有用想法。',
 'packed lunch 自带便当；tightly packed 装得很紧密。','packed with 强调装满某内容，可实可虚；packed a bag 强调收拾行李。be packed for a trip 是已经收拾好准备出行。',
 ('She packed her bag the night before the trip.','她在出发前一晚收拾好了包。'),('The hall was packed with people.','大厅里挤满了人。'),sources=['https://en.wiktionary.org/wiki/packed#English','https://en.wiktionary.org/wiki/pack#English'])
W('viewed','/vjuːd/','观看了、查看了；被看作〔过去式、过去分词〕',
 '把目光放到某件东西上，是 viewed 的看；从某个角度给它一个判断，则是 viewed as 把它看作什么。',
 'view + -ed，/uː/ 后读 /d/。名词经古法语 veue 看见的景象，较早接拉丁 vidēre 看；英语动词在相关名词基础上发展看、看待的用途。',
 [['拉丁 vidēre → 法语 veue → view','看见的景象 → 看、查看'],['view + -ed → viewed','过去观看；被从某种角度看待']],
 'viewed the exhibition 看了展览；viewed as useful 被看作有用；viewed from above 从上方观看。',
 'viewed the document 查看文件；widely viewed as... 普遍被看作……。','viewed as 引出判断身份、性质；viewed from 引出观察位置或角度。两者都接看，但一个侧重评价，一个侧重视点。',
 ('The visitors viewed the drawings in the main hall.','访客在主厅观看了那些画。'),('The change was viewed as a step forward.','这项变化被看作向前迈出的一步。'),sources=['https://en.wiktionary.org/wiki/viewed#English','https://en.wiktionary.org/wiki/view#English'])
W('rated','/ˈreɪtɪd/','评分了、评定为；有某种额定值的〔过去式、过去分词〕',
 '把东西放到一个标准或分值上，判断它处在哪一级，就是 rated。产品评分、电影级别、设备额定能力，都涉及一个核定尺度。',
 'rate + -d，/t/ 后读 /ɪd/。rate 的核定数值词族经法语等接拉丁 rāta 规定份额，关联 rērī 计算、判断；评分、等级等动词用途随之发展。',
 [['拉丁核定份额词 → 法语等 → rate','计算、核定 → 评估、划定等级'],['rate 去 e + -ed → rated','已经打分、评定；按某标准核定']],
 'rated highly 评价很高；rated as excellent 评为优秀；rated for outdoor use 核定可供户外使用。',
 'rated five stars 评为五星；rated by readers 由读者评分。','rated 是按特定尺度评定，不同评分者、用途的标准可能不同。设备 rated power 是额定功率，和用户给的好评不是同一尺度。',
 ('Readers rated the guide highly for its clear explanations.','读者因解释清楚而给这本指南很高评价。'),('The film was rated suitable for all ages.','这部影片被评定为适合所有年龄观看。'),sources=['https://en.wiktionary.org/wiki/rated#English','https://en.wiktionary.org/wiki/rate#English'])
W('ruled','/ruːld/','统治了、管理了；裁定了；划了线〔过去式、过去分词〕',
 '让事情沿着一条准则走，是 ruled 的管理、裁定线索；把纸上的线划直，则更直接接到尺子的历史画面。',
 'rule + -d，/l/ 后读 /d/。名词经法语 riule、reule 接拉丁 rēgula 直尺、准则；动词经法语 riuler 接拉丁 rēgulāre 管理，两条相关借入路线分别看。',
 [['拉丁 rēgula、rēgulāre → 法语 → rule','直尺、准则；按准则管理'],['rule 去 e + -ed → ruled','过去统治、裁定；画有直线的']],
 'ruled the country 统治国家；ruled that... 裁定……；ruled paper 横线纸；ruled out 排除。',
 'ruled in favour of... 裁定支持……；ruled out the option 排除这一选项。','ruled out 是排除，和 ruled the country 的统治义不同。裁判、法院 ruled that 引出决定；ruled paper 则描述有线格的纸。',
 ('The referee ruled that the goal did not count.','裁判判定进球无效。'),('We ruled out the longer route because of the weather.','由于天气原因，我们排除了较长的路线。'),sources=['https://en.wiktionary.org/wiki/ruled#English','https://en.wiktionary.org/wiki/rule#English'])
W('separated','/ˈsepəreɪtɪd/','分开了、分离的；分居的〔过去式、过去分词〕',
 '原来在一处、连着或混在一起的东西，现在各自到了不同位置，是 separated。人、材料、想法，都可以这样分开。',
 'separate + -d，动词 /ˈsepəreɪt/ 的 /t/ 后读 /ɪd/。拉丁 sē- 分开 + parāre 安排 → sēparāre，分词 sēparātus 接英语词族；这里用动词的强读尾。',
 [['拉丁 sēparāre、sēparātus → separate','分开安排 → 使分离'],['separate 去 e + -ed → separated','已经分开；相互分离的状态']],
 'separated by a wall 被墙隔开；separated the papers 把文件分开；separated from the group 与团队走散、分离。',
 'separated into groups 分成几组；a separated couple 分居的伴侣。','separate 作形容词时末尾常弱读 /ət/，separated 按动词 /eɪt/ 加词尾。说关系中的 separated 常是分居，是否已离婚要看具体情况。',
 ('The garden is separated from the road by a low wall.','花园与道路之间隔着一堵矮墙。'),('She separated the papers into three groups.','她把文件分成三组。'),sources=['https://en.wiktionary.org/wiki/separated#English','https://en.wiktionary.org/wiki/separate#English'])
W('cited','/ˈsaɪtɪd/','引用了、引证了；举为理由〔过去式、过去分词〕',
 '把一份材料或一个理由叫到读者面前，让它支持正在说的事，是 cited。论文引用、报告举证、解释原因，都常见。',
 'cite + -d，/t/ 后读 /ɪd/。cite 经法语 citer 接拉丁 citāre 召唤、唤起，是 ciēre 使动起来词族的加强形式；英语再有引用、列举用途。',
 [['拉丁 citāre → 法语 citer → cite','召唤、叫到面前 → 引用、举出材料'],['cite 去 e + -ed → cited','已经引用；作为依据或原因提及']],
 'cited a study 引用一项研究；cited as an example 被举为例子；cited lack of time as a reason 以没时间为理由。',
 'frequently cited 经常被引用；sources cited in the article 文中引用的来源。','cited 说明拿来作为依据、例子或理由，不能只凭引用知道材料一定正确。cite、site、sight 常同音，拼写和词义分别记。',
 ('The article cited three earlier studies.','文章引用了三项较早的研究。'),('She cited the weather as the reason for the delay.','她把天气列为延误的原因。'),sources=['https://en.wiktionary.org/wiki/cited#English','https://en.wiktionary.org/wiki/cite#English'])
W('constructed','/kənˈstrʌktɪd/','建造了、构建了；搭建的〔过去式、过去分词〕',
 '把分散的部分按照一种结构放到一起，搭出一个整体，就是 constructed。可以是桥，也可以是论证、模型、故事。',
 'construct + -ed，/t/ 后读 /ɪd/。拉丁 con- 一起 + struere 堆叠、建造 → construere，分词 constructus 的词干进入英语动词，现代过去变化再加 ed。',
 [['拉丁 construere、constructus → construct','一起堆叠、搭建 → 建造、构成'],['construct + -ed → constructed','已经搭建；按结构构成的']],
 'constructed a bridge 建了一座桥；constructed an argument 构建论证；constructed from wood 用木材建造。',
 'carefully constructed 精心构建的；constructed a model 制作模型。','constructed 重点在部分怎样组织成整体。an argument constructed from evidence 是用证据搭起的论证，材料和结构都需要判断。',
 ('The bridge was constructed from local stone.','桥用当地石材建造。'),('The students constructed a model of the building.','学生制作了这座建筑的模型。'),sources=['https://en.wiktionary.org/wiki/constructed#English','https://en.wiktionary.org/wiki/construct#English'])
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_zq',ROOTS,WORDS)
 extend_lessons()
