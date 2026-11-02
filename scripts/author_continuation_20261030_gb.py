"""Button and examine: small fastenings and weighing evidence."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
B=[['古法语 bouter 推、突出 → boton 芽、凸起、纽扣 → button','从凸出的小结到衣服扣子'],['器物用途扩展','按下控制的按钮；界面虚拟按钮'],['英语组合','unbutton 解纽扣；bellybutton 腹部纽扣样的肚脐']]
W('button','/ˈbʌtən/','纽扣、按钮；扣上纽扣',
 '衣服上一个小扣把两片衣料连住；机器和屏幕上一个小块，按一下让它做事，也叫 button。',
 '借古法语 boton，旧有芽、凸起材料，联系 bouter 推、突出；不是英语 butt + -on 的现代组合。',B,
 'sew on a button 缝纽扣，press a button 按按钮，button a coat 给外套扣扣子，push someone’s buttons 故意触动某人情绪。',
 'press a button；sew on a button；button a coat；push someone’s buttons。',
 'button 扣子和按钮按功能分；屏幕按钮不必真的向外凸。button up 扣好，也可说把细节收齐的比喻。',
 ('One button is missing from my shirt.','我的衬衫掉了一颗扣子。'),('Press the green button to start.','按绿色按钮开始。'),
 sources=['https://www.etymonline.com/word/button','https://en.wiktionary.org/wiki/button#English'])
W('unbutton','/ʌnˈbʌtən/','解开纽扣、松开扣合',
 '扣子原来从扣眼里穿过去，现在退出来，让衣料分开；un- 在这里撤销扣合动作。',
 'un- 反向动作 + button 扣纽扣，中古英语已有相应形式；不是 un- 永远否定一个物体存在。',B[:1]+[['un- + button → unbutton','解除纽扣扣合']],
 'unbutton a coat 解外套纽扣，unbutton a collar 解开领口扣，unbutton a shirt 解衬衫纽扣。',
 'unbutton a coat；unbutton a collar；unbutton a shirt。',
 'unbutton 解扣，unzip 拉开拉链；知道衣服开合方式，再选动词。',
 ('He unbuttoned his coat as he entered the warm room.','走进暖房间时，他解开了外套纽扣。'),('She unbuttoned the shirt cuffs and rolled up her sleeves.','她解开袖口扣子，卷起袖子。'))
W('bellybutton','/ˈbelibʌtən/','肚脐〔口语〕',
 '腹部中央留下的那一点像一枚小扣，便叫 bellybutton；有人向里凹，有人向外凸，不必每个都像凸扣。',
 'belly 肚子 + button 纽扣，形状比喻组成口语身体名称，不是腹部装了可按的控制开关。',B[:1]+[['belly + button → bellybutton','肚脐这一口语名称']],
 'an innie bellybutton 向内凹肚脐，an outie bellybutton 向外凸肚脐，a bellybutton on a drawing 图上的肚脐。',
 'bellybutton；an innie bellybutton；an outie bellybutton。',
 'bellybutton 口语，navel 常见正式名称；belly 肚子范围大，bellybutton 只是中间这一处。',
 ('The child drew a bellybutton on the cartoon figure.','孩子给卡通人物画上了肚脐。'),('He pointed to his bellybutton and laughed.','他指着自己的肚脐笑了。'))
R('B2945','凸起小结变纽扣，再到按一下的按钮','BUTTON：扣合与触发，按场景抓功能','button → unbutton 解除扣合；bellybutton 借形状称肚脐。',
 '衣扣和屏幕按钮都叫 button，功能已分；bellybutton 则只借外观称身体部位，不是按钮功能。',
 'bouter → boton → button；un- + button；belly + button。',
 [['纽扣、按钮与扣合动作','button · unbutton'],['形状比喻身体名','bellybutton']],
 'unbutton/unzip 解纽扣与解拉链；bellybutton/navel 口语与正式名称；button 不硬拆 butt + on。',
 'He unbuttoned his coat, then pressed the lift button.\n\n他解开外套纽扣，然后按了电梯按钮。','button unbutton bellybutton')
E=[['拉丁 exāmen、exāmināre','称量、检验、仔细考虑，较远与 exigere 等联系'],['法语 examiner、examinacion → 英语 examine、examination','检查、询问与检验过程分别借入'],['examine + -er → examiner','负责检查、考核的人']]
W('examine','/ɪɡˈzæmɪn/','仔细检查、审视；考核；询问',
 '像把东西放上秤，不急着凭第一眼下结论，先翻看、问清、检验；可以检查样本，也可以考核一个人。',
 '经法语 examiner 接拉丁 exāmināre，联系 exāmen 的称量、测试材料。不要把 ex- 出去 + mine 我的、矿山编成字面故事。',E[:2],
 'examine the evidence 审视证据，examine a sample 检查样本，examine a student 考核学生，examine a proposal 细看提案。',
 'examine the evidence；examine a sample；examine a proposal。',
 'look at 可以只是看一眼，examine 常强调为了判断而仔细看；考试只是它的一个常见场景。',
 ('The scientist examined the sample under a microscope.','科学家用显微镜仔细检查了样本。'),('We need to examine the proposal more closely.','我们需要更仔细地审视提案。'),
 sources=['https://www.etymonline.com/word/examine','https://en.wiktionary.org/wiki/examine#English'])
W('examination','/ɪɡˌzæmɪˈneɪʃən/','检查、审查；考试、考核',
 'examine 是做仔细检验，examination 把这次检验当一件事；试卷考试、身体检查、证据审查都可能用它。',
 '经法语 examinacion 接拉丁 exāminātiō 的动作名词，现代可对应 examine + -ation，但保留自己的借入链。exam 是它的常见缩短形式。',E[:2]+[['英语 examination 与缩短 exam','检验过程、考试']],
 'a written examination 笔试，a close examination 仔细检查，under examination 正被审查，a medical examination 体检。',
 'a written examination；close examination；under examination。',
 'examination 不只学校考试；exam 也可体检，但日常多见考试缩写。名词“考试”可数，抽象审查过程可不可数。',
 ('The documents are still under examination.','文件仍在审查中。'),('She passed the final examination.','她通过了期末考试。'),
 sources=['https://www.etymonline.com/word/examination','https://en.wiktionary.org/wiki/examination#English'])
W('exam','/ɪɡˈzæm/','考试；检查、体检〔examination 的缩写〕',
 '日常说考试，不必把 examination 一长串音节全说出来，就截成 exam；缩短后通常仍指一场正式检验。',
 '由 examination 缩短而来，不是 examination 必须先从英语 exam 加 -ination 生出。较短形式历史上反而晚。',
 E[:2]+[['examination → 缩短 exam','考试、检查的日常短名称']],
 'take an exam 参加考试，pass an exam 通过考试，a final exam 期末考试，an eye exam 眼部检查。',
 'take an exam；pass an exam；a final exam；an eye exam。',
 'exam 不只学校试卷，eye exam 是检查；examine 动词不从现代短名词 exam 新加一个 ine。',
 ('We have a history exam on Friday.','周五我们有一场历史考试。'),('She booked an eye exam for next week.','她预约了下周的眼部检查。'))
W('examiner','英 /ɪɡˈzæmɪnə/；美 /ɪɡˈzæmɪnər/','检查员、审查员；考官、阅卷人',
 '不是去接受考核的学生，而是拿着标准检查、提问或评卷的人；不同机构安排不同任务。',
 'examine + -er，去末尾不发音 e，人物后缀；不把 examiner 当作一次考试的另一种名词。',E[:2]+[['examine + -er → examiner','实施检查、考核或阅卷的人']],
 'a driving examiner 驾驶考试考官，an external examiner 校外考官、外审人员，a patent examiner 专利审查员。',
 'a driving examiner；an external examiner；a patent examiner。',
 'examiner 是实施者，examinee 是受考者；具体 examiner 负责出题、面试还是阅卷，需看考试安排。',
 ('The examiner asked her to explain the answer.','考官请她解释答案。'),('The patent examiner reviewed the application.','专利审查员审阅了申请。'))
R('B4204','先掂量、看细，再作判断','EXAMINE：仔细检验，不只写试卷','examine → examiner 人物；examination 历史名词支线，exam 是常见缩短。',
 'sample、evidence、student 不同宾语，让同一个动作落到实验、审查、考核中。名词、人物和动作集中对照。',
 'exāmen、exāmināre → examiner → examine；exāminātiō → examinacion → examination；examine + -er。',
 [['仔细检查动作','examine'],['检查过程、简称与实施者','examination · exam · examiner']],
 'examine/look at 仔细检验与泛看；examination/examiner 过程与人；名词借入链不只现代贴后缀。',
 'The examiner examined the answers after the examination.\n\n考试后，考官检查了答卷。','examine examination exam examiner')
if __name__=='__main__':save('continuation_20261030_gb',ROOTS,WORDS)
