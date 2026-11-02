"""Relative and traditional: reference points, scientific terms and inherited practices."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
RE=[['拉丁 referre → relātus → 晚期拉丁 relātīvus','带回、联系、涉及 → 相联系的'],['法语 relatif → 英语 relative','相对、相关的；与自己有亲属关系的人']]
def E(f,m):return RE+[[f,m]]
W('relative','/ˈrelətɪv/','相对的；有关的；亲属',
 '别只孤零零看一个东西，拿它和另一个参照物相联系；名词则说与你有亲属关系的人。',
 '经法语接晚期拉丁 relātīvus，来自 referre 的分词词干 relāt-。现代可对应 relate 与 -ive 认形，但不是全在英语里新拼出来。',RE,
 'a relative advantage 相对优势，relative to the cost 相对于费用，a close relative 近亲，a relative clause 关系从句。',
 'a close relative；relative to；relative importance；a relative advantage。',
 'relative 相对不等于不真实，只是评价要看参照。a relative 是亲属，不是一个形容词比较级；relatively 是副词。',
 ('The relative importance of these factors has changed.','这些因素的相对重要性发生了变化。'),('Several relatives came to visit us.','几位亲戚来看我们。'),sources=['https://www.etymonline.com/word/relative','https://en.wiktionary.org/wiki/relative#English'])
W('relatively','/ˈrelətɪvli/','相对地；相比之下、还算',
 '说它便宜，不是世上最便宜，而是和眼前其他选项一比还算便宜。',
 'relative + -ly。常把比较参照留在上下文里，不一定每句都明说 compared with what。',E('relative + -ly → relatively','相对于参照物；相比之下'),
 'relatively small 相对较小，relatively easy 还算容易，relatively speaking 相对而言。',
 'relatively small；relatively easy；relatively speaking。',
 'relatively 依比较参照，absolutely 可完全、绝对；a relatively easy test 不保证所有人都觉得简单。',
 ('The hotel is relatively inexpensive for this area.','在这个地区，这家酒店还算便宜。'),('The instructions are relatively easy to follow.','这些说明还算容易照着做。'))
W('relativity','英 /ˌreləˈtɪvəti/；美 /ˌreləˈtɪvəti/','相对性；相对论〔物理学〕',
 '一般义是性质依赖参照；物理学相对论则是一套具体理论，不能简化成一切随你怎么看。',
 'relative + -ity，形成性质名词；物理学专名与德语 Relativität 等对应、翻译使用相关。科学用法有严格内容，不是普通态度词的任意放大。',E('relative + -ity → relativity','相对的性质；后用于特定物理理论名称'),
 'the theory of relativity 相对论，special relativity 狭义相对论，the relativity of judgments 判断的相对性。',
 'the theory of relativity；special relativity；the relativity of。',
 'relativity 物理学理论或相对性，relativism 哲学立场；学相对论不等于主张所有意见同样正确。',
 ('The course introduces the theory of relativity.','课程介绍相对论。'),('The essay explores the relativity of our judgments.','文章探讨我们判断的相对性。'),sources=['https://www.etymonline.com/word/relativity','https://en.wiktionary.org/wiki/relativity#English'])
W('relativistic','英 /ˌrelətɪˈvɪstɪk/；美 /ˌrelətəˈvɪstɪk/','相对论的；相对主义的〔随领域〕',
 '物理书里通常在说相对论效应、模型；哲学讨论里也可描述相对主义的看法。',
 '可从 relativist + -ic 或 relative + -istic 分析。现代相对论相关用法已固定，不能只按相对地这个副词来理解。',E('relativist + -ic／relative + -istic → relativistic','与相对论或相对主义相关，依领域分义'),
 'relativistic effects 相对论效应，relativistic physics 相对论物理学，a relativistic view 相对主义观点〔看哲学语境〕。',
 'relativistic effects；relativistic physics；a relativistic model。',
 'relativistic 技术形容词，relative 普通相对、相关形容词；relative speed 相对速度与 relativistic effects 不是同一个短语含义。',
 ('The model includes relativistic effects.','模型包含相对论效应。'),('The lecture compares classical and relativistic physics.','讲座比较经典物理学与相对论物理学。'),sources=['https://dictionary.cambridge.org/us/pronunciation/english/relativistic','https://en.wiktionary.org/wiki/relativistic#English'])
W('relativism','/ˈrelətɪvɪzəm/','相对主义',
 '讨论真理、知识或道德评价时，强调它们与所用标准、文化、框架等有关；具体主张要看是哪种相对主义。',
 'relative + -ism，形成立场、思想名词。不同领域的理论不相同，不能由一个后缀推成任何人说什么都对。',E('relative + -ism → relativism','关于判断、知识等依赖框架的思想立场'),
 'moral relativism 道德相对主义，cultural relativism 文化相对主义，debates about relativism 相对主义讨论。',
 'moral relativism；cultural relativism；debates about relativism。',
 'relativism 哲学、评价框架立场，relativity 相对性或物理理论；两词有词形联系，不代表两套理论互相证明。',
 ('The seminar discussed cultural relativism.','研讨课讨论了文化相对主义。'),('The author distinguishes several forms of relativism.','作者区分了几种相对主义。'))
R('B3719','联系、参照与亲属；物理学和哲学术语分开','RELATIVE：和谁比、和谁相关；名词也可亲属','relative → relatively；relativity/relativistic 接科学等专门用法，relativism 单独讲哲学立场；较专门 correlative 暂略。',
 '同一参照词系有普通、科学、哲学分支，不能把一个相对联想变成所有理论的通用解释。',
 '拉丁 relāt- + -īvus → relative；relative + -ly/-ity/-ism/-istic；relativist + -ic 的对应分析。',
 [['普通参照和关系','relative · relatively'],['科学与理论形容词','relativity · relativistic'],['哲学立场','relativism']],
 'relative 亲属或相对，relatively 副词；relativity 相对论不等于 relativism；相对不等于虚假。',
 'Relatively simple examples introduce relativity without turning it into relativism.\n\n相对简单的例子介绍了相对论，没有把它混成相对主义。',
 'relative relatively relativity relativistic relativism')
TD=[['tradition 传下来的惯例、观念 → traditional','按传统的'],['traditional 与人物、立场、否定成分组合','守传统的人、传统取向与非传统方式']]
W('traditionalist','/trəˈdɪʃənəlɪst/','传统主义者；重视、坚持传统的人',
 '面对新旧做法时，更想保留沿用下来的方式；可以说审美，也可以说生活、组织制度。',
 'traditional + -ist，按重视传统的立场、倾向称人。不能仅凭这个词判断他在每项政治、技术问题上的观点。',TD+[['traditional + -ist → traditionalist','倾向保留传统的人']],
 'a traditionalist in design 设计上偏传统的人，a committed traditionalist 坚定维护传统者。',
 'a committed traditionalist；a traditionalist approach；a traditionalist in。',
 'traditional 传统的修饰对象，traditionalist 人或相应取向；traditional food 传统食物不能因此叫一个 traditionalist。',
 ('He is a traditionalist when it comes to furniture design.','说到家具设计，他是个偏爱传统的人。'),('The traditionalists preferred the original ceremony.','重视传统的人更喜欢原来的仪式。'))
W('traditionalism','/trəˈdɪʃənəlɪzəm/','传统主义；守传统的取向',
 '这次不说哪个人，而说把传下来的做法当重要依据、倾向保留它们的态度。',
 'traditional + -ism，形成立场、取向名词。具体思想流派另有定义，日常可宽泛说对传统的坚持。',TD+[['traditional + -ism → traditionalism','偏重保留传统的思想、倾向']],
 'cultural traditionalism 文化传统取向，a tension between traditionalism and innovation 传统取向与创新之间的张力。',
 'cultural traditionalism；a form of traditionalism；traditionalism and innovation。',
 'traditionalism 取向，tradition 具体传统，traditionalist 持这种取向的人；不是三个都只译传统就能替换。',
 ('The essay examines traditionalism in architecture.','文章研究建筑中的传统主义取向。'),('The debate reflected a tension between traditionalism and innovation.','辩论反映了守传统与创新之间的张力。'))
W('nontraditional','英 /ˌnɒntrəˈdɪʃənəl/；美 /ˌnɑːntrəˈdɪʃənəl/','非传统的；不同于惯常模式的',
 '没有沿着通常传下来的那条路来；只说明与传统模式不同，不自动夸好或贬坏。',
 'non- 非、不属于 + traditional。前缀否定类别，不等于 anti- 必然主动反对传统。',TD+[['non- + traditional → nontraditional','不属于惯常、传统模式的']],
 'a nontraditional approach 非传统方法，nontraditional students 非典型学习路径的学生〔教育语境〕。后者范围按机构说明。',
 'a nontraditional approach；a nontraditional career；nontraditional students。',
 'nontraditional 不按传统，不等于 unprofessional 不专业；非传统方法也可很严谨，传统方法也需看实际效果。',
 ('The course uses a nontraditional approach to teaching history.','课程用非传统方式教授历史。'),('She followed a nontraditional path into the profession.','她走了一条非传统路径进入这个职业。'))
R('B4099','传统性质到持守者、立场和不同路径','TRADITIONAL：按传统；-ist 人，-ism 取向，non- 非传统','已有 traditional、traditionally 后，traditionalist/traditionalism 连读，nontraditional 最后作类别否定。',
 '传统与创新可以在不同方面并存；词形只提供倾向、类别，不代替对具体做法的评价。',
 'traditional + -ly/-ist/-ism；non- + traditional。',
 [['性质与方式','traditional · traditionally'],['人物、立场和非传统','traditionalist · traditionalism · nontraditional']],
 'traditionalism 取向、traditionalist 人、tradition 具体传统；non- 不属于不等于 anti- 主动反对。',
 'The traditionalist considered a nontraditional design without abandoning every tradition.\n\n这位重传统的人考虑了非传统设计，并没有因此抛弃所有传统。',
 'traditional traditionally traditionalist traditionalism nontraditional')
if __name__=='__main__':save('continuation_20261030_br',ROOTS,WORDS)
