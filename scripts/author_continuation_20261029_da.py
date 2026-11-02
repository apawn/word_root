"""Mark: signs, observations and familiar historical metaphors."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
def C(a,b,w,m):return [[a+'；'+b,'并列构词部分'],[w,m]]
MA=[['古英语 mearc → 中古英语 mark、merk','边界、界标、记号'],['英语 mark','痕迹、标记、目标、分数；做记号、批改等']]
W('mark','英 /mɑːk/；美 /mɑːrk/','记号；痕迹；分数；标记；批改；标志着',
 '留下一个能认出来的位置、痕迹或分数，让人知道这里有什么、事情到了哪一步。',
 '继承古英语 mearc，已有边界、界标、记号等义。由标识、痕迹扩展到分数、目标、特点；旧货币马克另有计重、货币背景，不把它说成现代英语标记动作的临时名词。',MA,
 'a mark on the wall 墙上痕迹，full marks 满分；mark the date 标出日期，mark an essay 批改作文；mark the beginning of 标志着……开始。',
 'leave a mark；full marks；mark the beginning；make your mark。',
 'mark 做记号也可说批改、标志，不是每次都画一个勾；a question mark 是问号，checkmark 是对勾。',
 ('The cup left a mark on the table.','杯子在桌上留下了痕迹。'),('The ceremony marks the beginning of the festival.','典礼标志着节庆开始。'))
W('marked','英 /mɑːkt/；美 /mɑːrkt/','有标记的；明显的；被标出的',
 '一种是真的做过记号；另一种是差异大到像被特别标出来，一眼就看得出。',
 'mark + -ed，过去分词并形成形容词。明显这一义来自显著可辨的特征；常用读音末尾 /t/，不是一律读成独立 /ɪd/ 音节。',MA+[['mark + -ed → marked','做过标记 → 有标记的；显著的']],
 'a marked change 明显变化，a marked improvement 显著改善，a clearly marked exit 清楚标出的出口。',
 'a marked difference；a marked improvement；clearly marked。',
 'marked difference 是明显差异，不是必须有人拿笔圈过；marked papers 则可真指批改过的试卷。',
 ('There was a marked improvement in her confidence.','她的自信有了明显提升。'),('Please use the clearly marked exit.','请使用清楚标出的出口。'))
W('marking','英 /ˈmɑːkɪŋ/；美 /ˈmɑːrkɪŋ/','标记、批改；斑纹、地面标线等',
 '可以是做标记的过程，也可以是留下的一条条线、一块块特征花纹。',
 'mark + -ing，有较早历史动作名词对应形式；markings 复数常指物体、动物身上的特征纹样。',MA+[['mark + -ing → marking','标记动作、批改 → 各种标线、斑纹']],
 'road markings 道路标线，a bird’s markings 鸟的斑纹；exam marking 阅卷、批改。',
 'road markings；distinctive markings；exam marking。',
 'marking 可能指过程，markings 常是一项项具体标线、花纹；不是每个 marking 都是评分。',
 ('The bird has distinctive markings on its wings.','这只鸟的翅膀上有鲜明斑纹。'),('The teacher spent the evening marking essays.','老师晚上在批改作文。'))
W('marker','英 /ˈmɑːkə/；美 /ˈmɑːrkər/','标记物；记号笔；标志、指标；批改者',
 '让你看得出位置、特征或变化的东西；最常见的小工具就是记号笔。',
 'mark + -er，按用途形成工具、人物或指示物名称。并不是结尾 -er 就只能指人。',MA+[['mark + -er → marker','做记号 → 标记物、笔、指标或执行者']],
 'a permanent marker 油性、永久性记号笔，a route marker 路线标记；a marker of change 变化的标志。',
 'a permanent marker；a route marker；a marker of；an exam marker。',
 'marker 工具、标志或批改者，marking 标记过程、图案；marker of success 是成功指标，不是一支成功牌的笔。',
 ('Write your name with a marker.','用记号笔写下名字。'),('The stone served as a marker beside the path.','那块石头立在路旁作标记。'))
RE=[['法语 remarquer → 英语 remark','重新标出、注意；后来评论、指出'],['现代 remark 词族','评论、说到；值得注意的、显著的']]
W('remark','英 /rɪˈmɑːk/；美 /rɪˈmɑːrk/','评论；话语；说到、指出',
 '注意到一件事，把它点出来说一句；那句话也就是 a remark。',
 '经法语 remarquer，re- 再、强调 + marquer 标记、注意；与 mark 词族相关。现代 remark 常是评论，不应只按 again + mark 译成再打一个记号。',RE,
 'make a remark 作出评论，remark on the weather 谈到天气；remark that 指出某事。passing remark 随口一说，不一定是正式评议。',
 'make a remark；a passing remark；remark on；remark that。',
 'remark 评论，comment 也可评论且范围广；remarkable 取值得注意的，不是所有被随口评论过的事。',
 ('Her remark made everyone laugh.','她的一句话把大家都逗笑了。'),('He remarked on how quiet the town had become.','他说到小镇如今变得多么安静。'))
W('remarkable','英 /rɪˈmɑːkəbəl/；美 /rɪˈmɑːrkəbəl/','非凡的；值得注意的；显著的',
 '普通的事看过就过，这件事却让你停下来：这点真值得提一句。',
 '联系法语 remarquable，认形 remark + -able 值得、能够被注意到。现代常带非凡、突出的评价，不只是任何可写评语的东西。',RE+[['remark + -able；法语 remarquable → remarkable','值得注意、提到的 → 非凡、显著的']],
 'a remarkable achievement 非凡成就，a remarkable similarity 惊人的相似；不一定只夸好，a remarkable lack of detail 也可批评细节少得惊人。',
 'a remarkable achievement；a remarkable change；a remarkable similarity。',
 'remarkable 值得注意、突出，ordinary 普通；remarkable 不保证一定美好，具体评价看后面名词。',
 ('She made remarkable progress in a short time.','她在短时间内取得了显著进步。'),('There is a remarkable similarity between the two designs.','这两个设计有惊人的相似之处。'))
W('remarkably','英 /rɪˈmɑːkəbli/；美 /rɪˈmɑːrkəbli/','显著地；惊人地；不同寻常地',
 '把值得注意的那股程度感放到后面的特点上：好得惊人，或者相似得让人注意。',
 'remarkable + -ly，-able 词尾变成 -ably，形成副词。不是 remarkablely 的完整拼接写法。',RE+[['remarkable → remarkably','非凡、显著的 → 显著地、不同寻常地']],
 'remarkably similar 惊人相似，remarkably well 好得出乎意料；句首 Remarkably 也可评整个事情不寻常。',
 'remarkably similar；remarkably well；remarkably calm。',
 'remarkably 是副词，remarkable 是形容词：remarkable progress，progressed remarkably；不要只按中文显著混用。',
 ('The two accounts are remarkably similar.','两份叙述惊人地相似。'),('She remained remarkably calm during the delay.','延误期间，她镇定得出人意料。'))
W('birthmark','英 /ˈbɜːθmɑːk/；美 /ˈbɜːrθmɑːrk/','胎记',
 '出生时或出生后不久出现的皮肤颜色、外观标记，名字抓住它与出生早期的联系。',
 'birth 出生 + mark 标记，形成身体外观特征名；词源不说明每一种胎记的具体生物成因。',C('birth 出生','mark 标记','birthmark','与出生早期相关的皮肤标记'),
 'a birthmark on the cheek 脸颊上的胎记；不同胎记的颜色、形状有差异。这里只解释词义。',
 'a birthmark on；a small birthmark；a distinctive birthmark。',
 'birthmark 胎记，scar 疤痕常由损伤等留下；两个都可能是 mark，但来源不同。',
 ('He has a small birthmark on his shoulder.','他肩上有一小块胎记。'),('The portrait includes the woman’s distinctive birthmark.','画像保留了那位女性很有辨识度的胎记。'))
W('earmark','英 /ˈɪəmɑːk/；美 /ˈɪrmɑːrk/','指定用途；预留；耳记',
 '把一笔钱或一块地方圈出来：这是专门留给这件事的，不能随手当作普通剩余资源。',
 'ear 耳 + mark 标记，旧名词指牲畜耳上识别所属的记号；动词由识别、标出发展为预留、指定用途。不是在耳边提醒一句。',
 [['ear + mark → earmark','牲畜耳上的识别记号'],['动词 earmark','标出归属 → 为特定用途预留']],
 'earmark money for repairs 为修缮专留资金，land earmarked for housing 指定用于住宅建设的土地。常见被动结构 be earmarked for。',
 'earmark funds for；be earmarked for；earmark land for。',
 'earmark 指定用途不保证款项已经支付；spend 是已经花或正在花，earmark 还可能只是安排。',
 ('The council earmarked funds for library repairs.','议会为图书馆修缮预留了资金。'),('The site has been earmarked for a new school.','这块地已被指定用于建设新学校。'),sources=['https://en.wiktionary.org/wiki/earmark#English','https://www.etymonline.com/word/earmark'])
W('trademark','英 /ˈtreɪdmɑːk/；美 /ˈtreɪdmɑːrk/','商标；招牌式特点',
 '让顾客认出商品、服务来自谁的标识；人物也可有一眼就认出的招牌动作、风格。',
 'trade 商业、行业 + mark 标记，形成商业来源识别词。个人特点义是识别度的比喻，不表示每个习惯都已注册为商标。',C('trade 商业','mark 标识','trademark','商业来源标识 → 某人的鲜明特点'),
 'a registered trademark 注册商标，a trademark smile 招牌笑容；具体法律保护范围另按制度和事实，词本身不交代所有权。',
 'a registered trademark；a company trademark；a trademark smile。',
 'trademark 商标不同于 copyright 著作权、patent 专利，不能只因都涉及知识产权就当同词；比喻 trademark 强调辨识度。',
 ('The company’s trademark appears on every box.','公司的商标出现在每个盒子上。'),('He greeted us with his trademark smile.','他带着招牌笑容向我们问好。'))
W('benchmark','英 /ˈbentʃmɑːk/；美 /ˈbentʃmɑːrk/','基准；比较标准；基准测试',
 '没有参照，只能说好像变快了；先定一个共同标尺，再把结果放上去比。',
 'bench 在测量术语中有支撑、托架相关义 + mark 标记，历史是测量参照点，再引申为比较标准、测试。不是先坐长凳上做记号才有标准。',
 [['测量用 bench 支撑相关术语 + mark','测量高程等的参照标记'],['benchmark 的现代引申','比较标准、基准测试；以基准作比较']],
 'set a benchmark 建立基准，benchmark performance 对性能作基准比较；a benchmark test 基准测试。结果必须结合任务、条件才有比较意义。',
 'set a benchmark；a benchmark test；benchmark against；a performance benchmark。',
 'benchmark 是参照、比较测试，hallmark 是鲜明特点、检验印记；一个产品有 hallmark，不自动代表它跑赢 benchmark。',
 ('The result sets a new benchmark for the team.','这个结果为团队树立了新的比较基准。'),('We benchmarked the two systems under the same conditions.','我们在相同条件下对两套系统进行了基准比较。'),sources=['https://en.wiktionary.org/wiki/benchmark#English','https://www.etymonline.com/word/benchmark'])
W('hallmark','英 /ˈhɔːlmɑːk/；美 /ˈhɔːlmɑːrk/','贵金属检验印记；典型特点、标志',
 '印记让人知道金银器经过检验；比喻时，就是某人、某种事物很有辨识度的特征。',
 'hall + mark，历史联系伦敦 Goldsmiths’ Hall 及金银检验印记，不是所有大厅墙上记号的泛称。后来从质量识别印记发展为显著特征。',
 [['Goldsmiths’ Hall 相关名称 + mark','贵金属检验的印记名称'],['hallmark 的现代比喻','质量或其他性质的鲜明标志、特点']],
 'a hallmark on silver 银器检验印记，a hallmark of good teaching 好教学的典型特点；比喻也可用于坏事的显著特征，不必一律译优点。',
 'a hallmark of；bear a hallmark；the hallmark of quality。',
 'hallmark 检验印记、特点，trademark 商业来源标识或招牌特点；两者比喻有交叠，实际制度用途不同。',
 ('The silver spoon bears a small hallmark.','银勺上有一个小小的检验印记。'),('Clarity is a hallmark of her writing.','清晰是她文章的一大特点。'),sources=['https://en.wiktionary.org/wiki/hallmark#English','https://www.assayofficelondon.co.uk/hallmarking/what-is-a-hallmark'])
R('B3169','记号、痕迹、分数；注意、评论与各种标识','MARK：留下能识别的痕迹，再到注意和标准','从一条标线、一道分数开始，再读 remark 评论、remarkable 值得注意；benchmark、hallmark、earmark 各有自己的历史场景。',
 'mark 继承古英语边界、界标词族。remark 经法语的重新标出、注意等用法发展；不是现代所有 re- 都只译再次。各类标识按功能归组。',
 'mark → marked、marking、marker；remark → remarkable → remarkably；birthmark、earmark 看身体旧场景；trade、bench、hall + mark 看固定制度或功能。',
 [['记号与工具','mark · marked · marking · marker · checkmark'],['注意、评论及显著','remark · remarkable · remarkably'],['身体与专门用途','birthmark · earmark'],['商标、标准和特征','trademark · benchmark · hallmark'],['已学相关标记词','landmark · bookmark · watermark · postmark · marksman']],
 'remarkable 非凡不只是被评论过；earmark 预留不等于已支出；benchmark 标准，hallmark 特点、检验印记。',
 'The editor remarked on the remarkably clear wording and called clarity the writer’s hallmark.\n\n编辑谈到措辞清晰得出色，并称清晰是这位作者的标志特点。',
 'mark marked marking marker checkmark remark remarkable remarkably birthmark earmark trademark benchmark hallmark landmark bookmark watermark postmark marksman')
if __name__=='__main__':save('continuation_20261029_da',ROOTS,WORDS)
