"""Common past forms of handling, combining, recording and choosing."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'C1534':dict(words=['treat','treated'],label='treat → treated：处理、对待与款待',note='从拉、反复用手处理的词族，发展出怎样对人、对物行事。'),
 'B3672':dict(words=['combine','combined'],label='combine → combined：把几部分合起来',note='com- 一起与 bini 两两的旧组合，现代并不限于两个对象。'),
 'C0443':dict(words=['form','formed'],label='form → formed：成为某个形状或整体',note='拉丁 forma 的形状、样式词族，继续用于实体、群体、判断的形成。'),
 'C1404':dict(words=['state','stated'],label='state → stated：把情况明白说出来',note='state 的状态名词有拉丁、法语背景，陈述动词说把内容明确表达。'),
 'B4208':dict(words=['issue','issued'],label='issue → issued：向外发出、签发与发行',note='向外走的早期词族，经发出用于票据、文件、声明与出版物。'),
 'C0254':dict(words=['record','recorded'],label='record → recorded：回放到记忆与把信息留下',note='回想、记住的词族，经记录扩展到文字、声音、影像；动词后重。'),
 'C0437':dict(words=['focus','focused'],label='focus → focused：会聚点与集中注意',note='炉灶词被近代科学借用为会聚点，后用于注意力中心；focused、focussed 都存在。'),
 'B3367':dict(words=['score','scored'],label='score → scored：刻痕、计数与得分',note='刻记用来记录数量的历史，连接分数、取得成绩；刻线义仍存在。'),
 'C1660':dict(words=['vote','voted'],label='vote → voted：正式表达选择',note='拉丁誓愿、愿望词族发展为正式表达选择的名词与动词。'),
 'C0659':dict(words=['elect','elected'],label='elect → elected：挑选出来与经投票选出',note='ex- 的 e- 形式与 legere 选相连，现代可与 select 比较读。'),
}
W('treated','/ˈtriːtɪd/','对待、处理过；治疗过；款待、请客了；处理过的',
 '面对一个人或东西，你怎样处理、怎样对它，就是 treated 的共同线索；治疗是处理病情，款待则是好好招待。',
 'treat + -ed，/t/ 后增加 /ɪd/。treat 经古法语 traitier、tretier 接拉丁 tractāre 处理、管理，较早联系 trahere 拉、拖的词族。',
 [['拉丁 trahere、tractāre → 法语 → treat','拉、反复处理 → 处理、对待等'],['treat + -ed → treated','对待过、处理过；受处理的']],
 'treated us kindly 友好对待我们；treated the wood 处理过木材；treated the patient 给病人治疗；treated me to lunch 请我吃午饭。',
 'was treated as an equal；treated with respect。','treated as ... 是被当作……对待；treated with ... 说明用何种态度或材料处理；treated someone to something 是请人享用某物。',
 ('They treated every visitor with respect.','他们尊重地对待每位访客。'),('She treated me to lunch after the exam.','考试后，她请我吃了午饭。'),sources=['https://en.wiktionary.org/wiki/treated#English','https://en.wiktionary.org/wiki/treat#English'])
W('combined','/kəmˈbaɪnd/','结合、合并了；共同的、合计的；combine 的过去式和过去分词',
 '把分开的几部分放在一起，让它们共同起作用，是 combined；合起来算的数量、力量，也可这样修饰。',
 'combine 末尾已有 e，加 -d，/n/ 后读 /d/。combine 经法语接晚期拉丁 combīnāre，com- 一起与 bīnī 两两组成；现代可以合并多于两项。',
 [['拉丁 com- + bīnī → combīnāre → 法语、英语 combine','一起、两两 → 联结、合在一起'],['combine 去 e + -ed → combined','已经结合；共同、合计的']],
 'combined the two lists 合并了两份清单；combined efforts 共同努力；combined total 合计总数；combined with ... 与……结合。',
 'a combined approach；were combined into one。','combined with 说明和什么结合，combined into 说明合成了什么。combined total 是合计，不必表示各部分物理上混成一个东西。',
 ('We combined the two lists into a single document.','我们把两份清单合并成了一份文档。'),('Their combined efforts made the event possible.','他们共同的努力让活动得以举行。'),sources=['https://en.wiktionary.org/wiki/combined#English','https://en.wiktionary.org/wiki/combine#English'])
W('formed','英 /fɔːmd/；美 /fɔːrmd/','形成、组成了；建立、产生了；form 的过去式和过去分词',
 '原来的部分逐渐有了一个形状、一个整体，就是 formed；水滴形成、团队组成、看法产生都能沿这个形成的感觉理解。',
 'form + -ed，/m/ 后读 /d/。form 经古法语 forme 接拉丁 fōrma 形状、样式、模子，英语名词和动词有相连的用法发展。',
 [['拉丁 fōrma → 法语、英语 form','形状、样式 → 形成某种样子'],['form + -ed → formed','已形成、组成；被建立的']],
 'formed a circle 围成一圈；formed a team 组成团队；formed an opinion 形成看法；newly formed 新形成的。',
 'was formed in ...；formed from several parts。','formed a group 说主动组成群体，a group formed 说群体形成。formed from 看用什么材料、部分组成，formed into 看被塑成什么形态。',
 ('The children formed a circle around the teacher.','孩子们围着老师站成一圈。'),('Small drops formed on the cold window.','冰冷的窗户上凝成了小水珠。'),sources=['https://en.wiktionary.org/wiki/formed#English','https://en.wiktionary.org/wiki/form#English'])
W('stated','/ˈsteɪtɪd/','陈述、声明了；明确写出的、规定的；state 的过去式和过去分词',
 '把自己的意思、具体情况明白地说出来或写出来，就是 stated；文件上明确列出的条件，也常被称为 stated。',
 'state 末尾已有 e，加 -d，/t/ 后增加 /ɪd/。state 名词经法语等接拉丁 status 状态，关联 stāre 站立；陈述动词在英语中形成明确表达的用法。',
 [['拉丁 status → 法语、英语 state；英语陈述动词用法','状态、情况；把情况明确说出'],['state 去 e + -ed → stated','已经说明；明确列出的']],
 'stated her reasons 陈述理由；stated that ... 声明……；the stated purpose 明示目的；the stated time 指定、列明的时间。',
 'as stated above；clearly stated。','stated 比 said 常更正式、明确；stated purpose 是所明示的目的，实际动机是否相同还需上下文。as stated above 是如上所述。',
 ('She stated her reasons clearly.','她清楚地陈述了自己的理由。'),('Please return the equipment by the stated time.','请在规定时间前归还设备。'),sources=['https://en.wiktionary.org/wiki/stated#English','https://en.wiktionary.org/wiki/state#English'])
W('issued','英 /ˈɪʃuːd, ˈɪsjuːd/；美 /ˈɪʃuːd/','发出、签发了；发行了；流出；issue 的过去式和过去分词',
 '把文件、声明、票据正式向外发出去，是 issued；报刊、货币等发行，或水、声音流出，也属于这个向外的分支。',
 'issue 末尾已有 e，加 -d，元音后读 /d/。issue 经法语 issir、issue 接拉丁 exīre，ex- 向外与 īre 走组成；动词发出、发行与向外的早期画面相连。',
 [['拉丁 ex- + īre → exīre → 法语、英语 issue','向外走、流出 → 发出、签发'],['issue 去 e + -ed → issued','过去发出、签发、发行']],
 'issued a statement 发表声明；issued tickets 签发、发售票券；issued a warning 发出警告；water issued from ... 水从……流出〔较正式〕。',
 'was issued yesterday；issued to all members。','issue 作名词可以是议题、问题，但 issued the tickets 中是发出票券的动词。issued to 交代发给谁，issued by 交代由谁签发。',
 ('The museum issued new tickets for the evening event.','博物馆为晚间活动发放了新票。'),('The office issued a short statement after the meeting.','办公室在会后发表了一份简短声明。'),sources=['https://en.wiktionary.org/wiki/issued#English','https://en.wiktionary.org/wiki/issue#English'])
W('recorded','英 /rɪˈkɔːdɪd/；美 /rɪˈkɔːrdɪd/','记录下了；录音、录像了；已录制的',
 '让信息不只停在当时，而是能留下来再看、再听，就是 recorded；写记录、录声音、拍下过程都可用。',
 'record + -ed，/d/ 后增加 /ɪd/。这里来自后面重读的动词 record，经法语 recorder 接拉丁 recordārī 回想、记住，较早含 re- 与 cor／cord- 心，记忆被联系到心。',
 [['拉丁 cor／cord-、recordārī → 法语 recorder → record','心、记忆 → 回想、记录'],['record + -ed → recorded','记录过；录制、保存下来的']],
 'recorded the temperature 记录温度；recorded a song 录了一首歌；a recorded message 预录信息；recorded history 有文字记录的历史。',
 'was recorded live；previously recorded。','动词 recorded 保留后重的 /rɪˈkɔːd/ 词基，名词 record 常前重。recorded live 可以说现场录制；录下的内容以后播放时，仍是已经录制的材料。',
 ('She recorded the temperature every hour.','她每小时记录一次温度。'),('The concert was recorded for later broadcast.','音乐会录制了下来，供之后播放。'),sources=['https://en.wiktionary.org/wiki/recorded#English','https://en.wiktionary.org/wiki/record#English'])
W('focused','英 /ˈfəʊkəst/；美 /ˈfoʊkəst/','集中、聚焦了；专注的；对焦的',
 '光线聚到一点，是 focused 的光学画面；把注意力聚到一件事上，就是专注。这两个画面很容易连起来记。',
 'focus + -ed → focused，/s/ 后词尾读 /t/；focussed 也是存在的拼写。focus 是拉丁炉灶词，近代科学将它用于会聚点，英语又发展出注意中心义和聚焦动词。',
 [['拉丁 focus 炉灶 → 近代科学会聚点 → 英语 focus','会聚的一点 → 注意中心'],['focus + -ed → focused','已经聚焦；专注的、对焦后的']],
 'focused on the task 专注任务；a focused discussion 集中的、有明确重点的讨论；a sharply focused image 清晰对焦的图像。',
 'stay focused；focused attention。','focused on 交代注意、镜头对着什么；focused discussion 说明讨论有明确重点。focus 可以物理地调焦，也可以抽象地集中精力。',
 ('She stayed focused on the final question.','她一直专注于最后那个问题。'),('The camera was focused on the bird near the window.','相机对准了窗边的鸟，对好了焦。'),sources=['https://en.wiktionary.org/wiki/focused#English','https://en.wiktionary.org/wiki/focus#English'])
W('scored','英 /skɔːd/；美 /skɔːrd/','得分了；取得成绩；刻线、划出痕迹；score 的过去式和过去分词',
 '以前刻下一个记号来记数，后来就能用 score 说分数、得分；scored 也保留把表面划出一道痕的用法。',
 'score 末尾已有 e，加 -d，词尾读 /d/。score 经中古英语相关词形接古诺尔斯语 skor、skora 等刻痕、刻记词族，由刻记计数发展出得分等义。',
 [['古诺尔斯语刻痕、刻记词族 → 中古英语 → score','刻记数量 → 分数、得分'],['score 去 e + -ed → scored','过去得分、取得；表面刻过线']],
 'scored a goal 进球得分；scored highly 得高分；scored a success 取得成功；scored the surface 在表面划了线。',
 'scored twice；scored full marks。','scored a goal 常说在相应球类比赛中进球；scored ten points 说得十分。刻线的 scored 和计分义有历史联系，是否在谈数字要看宾语。',
 ('She scored the winning goal near the end of the match.','她在比赛接近结束时打进了制胜球。'),('He scored a line across the cardboard before folding it.','折纸板前，他先在上面划出了一道线。'),sources=['https://en.wiktionary.org/wiki/scored#English','https://en.wiktionary.org/wiki/score#English'])
W('voted','英 /ˈvəʊtɪd/；美 /ˈvoʊtɪd/','投票了；表决决定了；vote 的过去式和过去分词',
 '把支持、反对或想选谁正式表达出来，就是 voted；大家把这些选择合起来，能决定做什么。',
 'vote 末尾已有 e，加 -d，/t/ 后增加 /ɪd/。vote 接拉丁 vōtum 誓愿、愿望，与 vovēre 郑重许诺同族，英语名词、动词用于正式表达选择。',
 [['拉丁 vovēre、vōtum → 欧洲语言、英语 vote','誓愿、愿望 → 正式表达的选择'],['vote 去 e + -ed → voted','投过票；用表决作出决定']],
 'voted for the plan 投票支持计划；voted against it 投票反对；voted to postpone 表决决定推迟；voted someone chair 选某人为主席。',
 'unanimously voted；had already voted。','voted for、voted against 分别交代支持、反对。voted to do 表示投票决定某种行动；elected someone 则常直接说选出了某个人。',
 ('The members voted to postpone the meeting.','成员们投票决定推迟会议。'),('She voted against the proposed change.','她投票反对那项拟议中的变更。'),sources=['https://en.wiktionary.org/wiki/voted#English','https://en.wiktionary.org/wiki/vote#English'])
W('elected','/ɪˈlektɪd/','选举、选出了；选择了〔较正式〕；经选举产生的',
 '从候选者中正式挑出担任某个角色的人，就是 elected；较正式文字里也可以说选择某个做法。',
 'elect + -ed，/t/ 后增加 /ɪd/。elect 接拉丁 ēlēctus 被挑选出的，来自 ēligere，较早 ē- 是向外、出来与 legere 选的组合。',
 [['拉丁 ē- + legere → ēligere、ēlēctus → elect','挑选出来 → 选中的、选举'],['elect + -ed → elected','选出过；经选举产生的']],
 'elected a chair 选出主席；elected representatives 民选代表；was elected to the committee 当选进入委员会；elected to stay 选择留下〔较正式〕。',
 'newly elected；elected by the members。','elected someone chair 可直接接职务，elected someone as chair 也可见。elected to do 在正式语境是选择做；selected 通常更广地表示挑选，不一定有投票。',
 ('The members elected her chair of the club.','成员们选她担任俱乐部主席。'),('The newly elected representatives met for the first time.','新当选的代表们举行了首次会面。'),sources=['https://en.wiktionary.org/wiki/elected#English','https://en.wiktionary.org/wiki/elect#English'])
def extend_lessons():
 extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_xy',ROOTS,WORDS)
 extend_lessons()
