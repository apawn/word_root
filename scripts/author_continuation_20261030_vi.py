"""Common states: motivation, conviction, orientation and connection."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'C0769':dict(words=['motive','motivate','motivated','motivating'],label='motive → motivate → motivated／motivating',note='从推动身体到推动行动：动机促使人去做；motivated 说受到推动、有动力的一方，motivating 说能带来动力的作用。'),
 'C1641':dict(words=['convince','convinced','convincing'],label='convince → convinced／convincing',note='拉丁 vincere 战胜，经论证使人信服；convinced 说确信的状态，convincing 说使人信服的力量。'),
 'C0918':dict(words=['orient','oriented','orientation'],label='orient → oriented：找到方向，也形成取向',note='较早东方、面向东方的词义，扩大为按方向安置、熟悉环境；oriented 也说以某事为重点，不能每次都直译朝东。'),
 'C1209':dict(words=['dress','dressed','dressing'],label='dress → dressed：整理、装扮后处于某种状态',note='dress 接法语整理、摆正的词，衣着是其中一条常见发展；get dressed 是穿好衣服。'),
 'B3904':dict(words=['wrap','wrapped','wrapping'],label='wrap → wrapped：包裹以及注意力被占住',note='保留包在一层东西里的画面；wrapped 双写 p，词尾读 t，更早来源有不同解释。'),
 'A1833':dict(words=['attach','attached','attachment'],label='attach → attached／attachment：连接、依恋与附件',note='attach 经法语系住、固定词；attachment 是相关 -ment 名词，借入时间早，不能把所有现代义项排成一条单线。物理连接与情感联系都是重要分支。'),
 'A1760':dict(words=['attach','attached','dress','dressed','wrap','wrapped','motivate','motivated','convince','convinced'],label='常见完成、受到影响状态的 -ed',note='wrapped、dressed、attached 尾音 t，motivated 有额外的 id 音节；拼写 -ed 不意味着读音相同。'),
}
W('motivated','英 /ˈməʊtɪveɪtɪd/；美 /ˈmoʊtɪveɪtɪd/','有动力的、积极想做的；受……驱动的；motivate 的过去式、过去分词',
 '同样一件事，有人需要不断催促，有人自己就很想推进。后者做事有内在或外在的推动力，可以说 motivated。',
 'motivate 去 e 加 -ed。motive 经法语、拉丁 motivus、motus 接 movere 移动；推动身体的移动，延伸为推动行动的动机。英语 motivate 由 motive 加动词词尾形成。',
 [['拉丁 movere、motus → motive','移动 → 促使行动的动机'],['motive → motivate → motivated','提供动力 → 已受驱动、有动力']],
 'highly motivated 很有积极性；motivated to learn 有动力学习；motivated by curiosity 受到好奇心驱动；a motivated team 有干劲的团队。',
 'stay motivated；feel motivated to do something。','motivated 说受到推动的一方，motivating 说能给动力的事物或行为。动机也可能是恐惧、利益等，不自带高尚的评价。',
 ('Small improvements help me stay motivated.','一点点进步能帮助我保持动力。'),('She was motivated by a desire to understand the problem.','她想弄明白问题，这份愿望给了她动力。'),sources=['https://www.etymonline.com/word/motivate','https://en.wiktionary.org/wiki/motivated#English'])
W('motivating','英 /ˈməʊtɪveɪtɪŋ/；美 /ˈmoʊtɪveɪtɪŋ/','能激发动力的；正在激励；motivate 的 -ing 形式',
 '看见自己的进步，就更想继续练下去。这种让人愿意行动的效果，是 motivating。',
 'motivate 去词末 e 加 -ing。继承 motive 动机、movere 移动的词族，表示推动人去行动，也可作形容词说具有激励作用。',
 [['motive → motivate','行动的推动力 → 激发行动'],['motivate 去 e + -ing → motivating','正在激励；有激发动力的作用']],
 'a motivating factor 激励因素；a motivating goal 能带来动力的目标；find something motivating 觉得某事能激发积极性。',
 'a motivating experience；motivating students。','The teacher is motivating the class 是老师正在激励全班；a motivating teacher 是很能激发学生积极性的老师。-ing 既能作动词形式，也能说性质。',
 ('Seeing my progress was very motivating.','看到自己的进步，很能激发我的动力。'),('A clear goal can be more motivating than a vague promise.','明确的目标往往比含糊的承诺更能激发积极性。'),sources=['https://www.etymonline.com/word/motivate','https://en.wiktionary.org/wiki/motivating#English'])
W('convinced','/kənˈvɪnst/','确信的、深信的；被说服的；convince 的过去式、过去分词',
 '看过理由和证据之后，心里从可能是这样变成我相信就是这样。这个已经信服的状态叫 convinced。',
 'convince 去 e 加 -ed，词末 /s/ 后读 /t/。拉丁 convincere 由加强性的 con- 和 vincere 战胜组成，英语较早说在论证中胜过，后来常说使人相信。',
 [['拉丁 con- + vincere → convincere','彻底战胜；在论证中使对方信服'],['convince → convinced','使确信 → 已经相信、深信']],
 'be convinced that ... 确信……；be convinced of someone’s honesty 确信某人诚实；not entirely convinced 并不完全信服。',
 'remain convinced；a convinced supporter。','convinced 描写人的信念，不保证观点客观上正确。convincing 描写证据、说法等令人信服；someone is convinced 与 something is convincing 角度不同。',
 ('I am convinced that we can solve this together.','我确信我们能一起解决这件事。'),('The explanation sounded reasonable, but I was not entirely convinced.','解释听起来有道理，但我还没有完全信服。'),sources=['https://www.etymonline.com/word/convince','https://en.wiktionary.org/wiki/convinced#English'])
W('oriented','英 /ˈɔːrientɪd/；美 /ˈɔːrientɪd/〔美 r 发音〕','按方向安置的；熟悉方位、情况的；以……为导向的；orient 的过去式、过去分词',
 '先辨清自己在哪、要朝哪走，再把行动对准那个方向。oriented 可以说实际朝向，也可以说工作、设计把什么放在中心。',
 'orient + -ed，末尾 /t/ 后读 /ɪd/。orient 往前接拉丁 oriens 正在升起的、东方，与 oriri 升起相关；从面向日出方向，扩大到定位、熟悉新情况和形成取向。',
 [['拉丁 oriri → oriens → orient','升起 → 日出的东方 → 东方、确定朝向'],['orient + -ed → oriented','已定方向；熟悉环境；按某目标组织']],
 'get oriented 熟悉方位、情况；oriented toward a goal 朝向某目标；a course oriented toward beginners 面向初学者的课程。',
 'properly oriented；oriented toward practical work。','-oriented 作后接组合形式时常需连字符，如目标导向的形容词；这里保留 oriented 自身的精讲。现代 orient 可指任意方向，不能都译为向东。',
 ('It took me a day to get oriented in the new office.','我花了一天才熟悉新办公室的布局和情况。'),('The course is oriented toward practical skills.','这门课侧重实用技能。'),sources=['https://www.etymonline.com/word/orient','https://en.wiktionary.org/wiki/oriented#English'])
W('dressed','/drest/','穿好衣服的、穿着……的；dress 的过去式、过去分词',
 '从还没换好衣服，到已经能出门，常说 get dressed。再接 in，就可以说明身上穿的是什么。',
 'dress + -ed，/s/ 后读 /t/。dress 经法语 dresser 整理、摆正，接拉丁 directus 笔直、摆正；整理身体外观发展出穿衣、装扮。',
 [['拉丁直、摆正词族 → 法语 dresser → dress','摆正、整理 → 装扮、穿衣'],['dress + -ed → dressed','已经穿好、整理好；也作过去动作']],
 'get dressed 穿好衣服；be dressed in black 穿着黑衣服；fully dressed 穿戴整齐的；dressed for the weather 按天气穿好衣服。',
 'get dressed quickly；dressed in a blue coat。','wear 常描述穿着状态，dress 强调穿衣、给某人穿衣或装扮。dressed 不只与连衣裙 dress 有关，任何合适衣着都可这样说。',
 ('Get dressed and come downstairs for breakfast.','穿好衣服，下楼吃早饭。'),('He was dressed in a dark coat and a woollen scarf.','他穿着深色外套，围着羊毛围巾。'),sources=['https://www.etymonline.com/word/dress','https://en.wiktionary.org/wiki/dressed#English'])
W('wrapped','/ræpt/','包裹好的；全神贯注、沉浸其中的〔常与 up 连用〕；wrap 的过去式、过去分词',
 '把礼物用纸包住，或把自己裹进毯子，里面的东西就被一层外物围住了。注意力全被某件事占住，也可以借用这种包在里面的画面。',
 'wrap 双写 p 加 -ed；w 不发音，词尾读 /t/。中古英语 wrappen 已有包裹、围住义，更早来源不确定，不能把某一推测写成定论。',
 [['中古英语 wrappen → wrap','包住、围住、折裹'],['wrap 双写 p + -ed → wrapped','已经包好；比喻被某件事占满注意力']],
 'wrapped in paper 用纸包着；wrapped in a blanket 裹着毯子；wrapped up in a book 全神贯注看书；wrapped up the meeting 结束了会议。',
 'a carefully wrapped gift；wrapped around a pole。','wrap up 可以包好、结束，也能在 be wrapped up in 中表示沉浸。wrapped 与 rapped 同音，拼写和动作不同。',
 ('The gift was wrapped in plain brown paper.','礼物用普通棕色纸包着。'),('She was so wrapped up in her book that she missed the announcement.','她看书太入迷，没听见通知。'),sources=['https://www.etymonline.com/word/wrap','https://en.wiktionary.org/wiki/wrapped#English'])
W('attach','/əˈtætʃ/','系上、装上、连接；附上；赋予〔重要性等〕',
 '把标签系到行李上，把文件附到邮件里，都是让一件东西连到另一件上。这个连上去的动作，是 attach 的核心。',
 '经古法语 atachier、estachier 系住、固定等形式，较早在英语法律记录中也有扣押义。法语词基可能接日耳曼桩、柱词，与 stake 词族有关；更深路径带有不确定性。',
 [['古法语 atachier 等 → 英语 attach','系住、固定；较早英语也用于扣押'],['物理连接 → 文件附带、赋予重要性','把一件东西或一种评价加到对象上']],
 'attach a label to a bag 把标签系到包上；attach a file to an email 给邮件附文件；attach importance to something 重视某事；attach a condition 附加条件。',
 'attach something to something；attach great importance to。','attach 是连接、附上；attachment 是附件或联系。attach importance to 是赋予重要性，后面的 to 是介词。',
 ('Please attach the receipt to your message.','请在消息中附上收据。'),('We attach great importance to clear instructions.','我们非常重视清楚的说明。'),sources=['https://www.etymonline.com/word/attach','https://en.wiktionary.org/wiki/attach#English'])
W('attached','/əˈtætʃt/','附着、连接着的；随附的；依恋、有感情的；attach 的过去式、过去分词',
 '一张标签连在箱子上，是 attached；一个人对住了多年的地方舍不得离开，也是 attached。连接可以在物体之间，也可以在感情里。',
 'attach + -ed；/tʃ/ 后的词尾读 /t/，没有多一个 id 音节。从系住、连接的动词形成分词，并发展出感情上紧密相连的形容词义。',
 [['法语连接、固定词 → attach','把事物连起来'],['attach + -ed → attached','连着、附上的；感情上依恋']],
 'the attached file 随附文件；attached to the wall 固定在墙上；become attached to a place 对某地方产生感情；deeply attached to someone 深深依恋某人。',
 'Please see the attached ...；emotionally attached。','I attached the file 说做了附文件的动作；the attached file 说随附的文件。be attached to a person 可是感情联系，要结合对象理解。',
 ('The instructions are in the attached document.','说明在随附的文档里。'),('I have become quite attached to this old house.','我已经对这栋老房子很有感情了。'),sources=['https://www.etymonline.com/word/attach','https://en.wiktionary.org/wiki/attached#English'])
W('attachment','/əˈtætʃmənt/','附件、附加装置；依恋、感情联系；连接、附着',
 '邮件后面带着的文件，吸尘器上接着的小刷头，心里舍不得的人或物，都有连在一起的共同画面。attachment 说连上的东西、状态或感情。',
 '可对应 attach + 名词词尾 -ment。英语早期形式经法语 attachement 借入，较早法律义、后来的感情义和附加物义有各自的使用历史；电子邮件附件是在附加物义上的现代应用。',
 [['法语 attacher、attachement → 英语相关词','连接、固定；相关动作名词'],['attachment 的不同分支','感情联系；装接的部件、附带的文件']],
 'an email attachment 邮件附件；open the attachment 打开附件；an attachment for a vacuum cleaner 吸尘器配件；a strong attachment to home 对家的深厚感情。',
 'send something as an attachment；an emotional attachment。','文件、附加装置可数：two attachments。依恋常作抽象名词，也可说 a strong attachment to ... 这种明确的感情联系。',
 ('I sent the photos as an attachment.','我把照片作为附件发了过去。'),('She still feels a strong attachment to her hometown.','她对家乡仍有深厚的感情。'),sources=['https://www.etymonline.com/word/attachment','https://en.wiktionary.org/wiki/attachment#English'])
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_vi',ROOTS,WORDS)
 extend_lessons()
