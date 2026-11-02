"""People, organised work, nations and classes in frequent reading."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'B3164':dict(words=['leader','leaders'],label='leader → leaders：带领者的常用复数',note='leader 可指负责人，也可指非正式带头人或比赛领先者；复数的 /z/ 加在人物名词之后。'),
 'B2816':dict(words=['lead','leader','leaders'],label='lead → leader → leaders：带领与带领者',note='lead 带领读 /liːd/，leader、leaders 保留这个元音；人物后缀 -er 不把金属铅名词的 /led/ 带进来。'),
 'B4148':dict(words=['employ','employee','employees'],label='employ／employee → employees：受雇人员',note='employee 借法语 employé 的分词人物用法，现代也可用 -ee 记接受动作的人；employees 是英语复数。'),
 'C0325':dict(words=['individual','individuals'],label='individual → individuals：一个个独立个体',note='individual 接中世纪拉丁 individualis 与不可分材料；现代指一个个人、个体，不能逐字只译成不可分的。'),
 'C0620':dict(words=['project','projects'],label='project → projects：向前提出的方案、投射',note='project 名词、动词借入路线相关但不同，projects 在两种词性里通常靠重音分辨。'),
 'C0795':dict(words=['nation','nations'],label='nation → nations：出生、出身词族的人群名称',note='nation 经法语接拉丁 nātiō，较早联系出生、出身人群；现代国家、民族等称谓要按政治、文化场景理解。'),
 'C0156':dict(words=['class','classes'],label='class → classes：班级、类别、阶层与归类',note='class 接法语 classe、拉丁 classis；与召集 calare 的传统联系有不确定性，不把两者画成已证实的逐步变化。'),
}
W('leaders','英 /ˈliːdəz/；美 /ˈliːdərz/','领导者、负责人；领先者、带头人；leader 的复数',
 '把方向指出来、带着别人走的人，是 leaders；比赛或行业里走在前面的，也能被叫作 leaders。',
 'leader + -s，词尾 /z/。leader 现代可认作 lead 带领 + -er，接古英语 lǣdere、中古英语 ledere 等人物形式；词干元音是 /iː/。',
 [['古英语 lǣdere → 中古英语 ledere → leader；与 lead 带领相连','带领、引导的人'],['leader + -s → leaders','多位负责人、带头人、领先者']],
 'team leaders 团队负责人；community leaders 社区带头人；industry leaders 行业领先者；the race leaders 比赛领先者。',
 'leaders of the group；future leaders。','leaders 不一定都是正式经理，也可指带头、影响别人或排名领先的人。leader 的 lead 读 /liːd/，金属铅 lead /led/ 是另一个同形词。',
 ('The team leaders met to compare their plans.','各团队负责人见面交流了计划。'),('The race leaders passed the village just before noon.','比赛领先者在中午前不久经过了村庄。'),sources=['https://en.wiktionary.org/wiki/leaders#English','https://en.wiktionary.org/wiki/leader#English'])
W('employees','/ɪmˈplɔɪiːz, ˌemplɔɪˈiːz/','雇员、员工；employee 的复数',
 '和雇主构成受雇关系的人，是 employees。这个词突出受雇身份，不按在工厂还是在办公室来划分。',
 'employee + -s，词尾 /z/。employee 借法语 employé 受雇的人，本是 法语动词 employer 雇用的过去分词名词用法；现代可用 employ + -ee 作认形。',
 [['法语 employér → employe → 英语 employee','雇用 → 受雇的人；历史先有借入人物形式'],['employee + -s → employees','多位雇员、员工']],
 'new employees 新员工；employees of the company 公司员工；employees and employers 雇员和雇主；employee training 员工培训。',
 'the company’s employees；several employees。','employees 突出受雇关系，workers 更广地说做工作的人。employers 是雇主，employees 是受雇的人，词尾不同就改变了关系方向。',
 ('New employees attend a brief introduction session on their first day.','新员工第一天会参加简短的入职介绍。'),('The company asked its employees for ideas about improving the office.','公司向员工征求了改善办公室的想法。'),sources=['https://en.wiktionary.org/wiki/employees#English','https://en.wiktionary.org/wiki/employee#English'])
W('individuals','/ˌɪndɪˈvɪdʒuəlz/','个人、个体；individual 的名词复数',
 '先把一个人、一个生物看成独立的一整个体，再说很多这样的个体，就是 individuals。它常把注意力从群体转到一位位成员。',
 'individual + -s，/l/ 后读 /z/。中世纪拉丁 individualis 接 in- 不 + dividuus 可分的材料，历史不可分的整体发展为单独、独立个体等用法。',
 [['拉丁 in- + dividuus → individualis → individual','不可分的整体 → 单独的、个体'],['individual 名词 + -s → individuals','多个个人、个体']],
 'groups and individuals 团体和个人；different individuals 不同个体；private individuals 私人、普通个人〔依场景〕。',
 'several individuals；the needs of individuals。','individuals 作名词数人或个体；individual 作形容词不随人数加 s：individual needs 是个人的需要，individuals’ needs 是这些个人的需要。',
 ('The room can be booked by groups or individuals.','团体或个人都可以预订这个房间。'),('The study followed several individuals over time.','这项研究长期追踪了几个个体。'),sources=['https://en.wiktionary.org/wiki/individuals#English','https://en.wiktionary.org/wiki/individual#English'])
W('projects','名词：英 /ˈprɒdʒekts/、美 /ˈprɑːdʒekts/；动词 /prəˈdʒekts/','项目、课题、工程；投射、预计、呈现〔动词形式〕',
 '把一个方案朝未来推出去，是 project 的好记画面；把图像投到墙上、把声音或印象传出去，也用相关动词。',
 'project + -s。名词常重读第一音节，动词常重读第二音节。名词接中世纪拉丁 proiectum 提出的方案，动词另连后期拉丁 projectare，远源拉丁 proicere 向前投。',
 [['拉丁 pro- + iacere → proicere；proiectum／projectare 等 → project','向前投；提出的方案与投射动作各有借入支线'],['project 名词、动词 + -s → projects','多个项目；单数主语投射、预计、呈现']],
 'research projects 研究项目；school projects 学校课题；projects an image 投射图像；projects confidence 显得自信、传达自信印象。',
 'finish projects；projects onto the wall。','projects 名词说几项工作，动词说投射等动作，重音通常不同。projects confidence 强调给别人的印象，不直接证明本人内心有同样感受。',
 ('The students presented their projects at the end of the course.','课程结束时，学生们展示了各自的项目。'),('The small machine projects a map onto the wall.','这台小机器把地图投到墙上。'),sources=['https://en.wiktionary.org/wiki/projects#English','https://en.wiktionary.org/wiki/project#English'])
W('nations','/ˈneɪʃənz/','国家；民族、国民共同体等；nation 的复数',
 '把一群有历史、文化或政治联系的人看作一个共同体，可以叫 nation；很多日常语境里又直接用来指国家。',
 'nation + -s，词尾 /z/。拉丁 nātiō 较早联系出生、出身人群，经法语 nacion 进入英语；现代国家、民族用法不能只按生物出生来限定。',
 [['拉丁 nātiō → 法语 nacion → nation','出生、出身相连的人群 → 民族、国家等共同体称谓'],['nation + -s → nations','多个国家、民族等']],
 'neighbouring nations 邻国；relations between nations 国家间关系；the United Nations 联合国；nations with different histories 历史不同的国家、民族。',
 'several nations；nations around the world。','nation 常强调人群、历史文化或政治共同体，state 常强调国家组织、政治实体，country 常强调国家地域等，日常会重叠。具体称谓需要按语境译成国家还是民族。',
 ('The exhibition brings together artists from several nations.','这次展览汇集了几个国家的艺术家。'),('The book explores how nations tell stories about their past.','这本书探讨了各国如何讲述自己的历史。'),sources=['https://en.wiktionary.org/wiki/nations#English','https://en.wiktionary.org/wiki/nation#English'])
W('classes','/ˈklɑːsɪz/〔英〕；/ˈklæsɪz/〔美〕','班级、课程；类别、等级、阶层；归类〔class 的第三人称单数〕',
 '把人、东西按某种标准分成几组，是 classes 的共同画面。学校里是班级、课，分类里是类别，社会讨论里又可能是阶层。',
 'class + -es，/s/ 后读 /ɪz/。经法语 classe 接拉丁 classis 人群、组别等；传统词源解释与 calare 召集相联系，但具体更深联系未完全确定。',
 [['拉丁 classis → 法语 classe → class','分组的人群、等级 → 班级、类别等'],['class + -es → classes','多个班级、课程、类别；单数主语归类']],
 'evening classes 夜课；art classes 美术课；different classes of objects 不同类别的对象；social classes 社会阶层；classes something as ... 把……归为……。',
 'attend classes；classes the item as fragile。','class 常说一个教学班或一次、若干次课，course 常说系统的一门课程，具体地区用法会重叠。classes as 的 as 引出被归入的类别。',
 ('The centre offers evening classes in drawing and photography.','中心开设绘画和摄影夜课。'),('The system classes these files as temporary.','系统把这些文件归为临时文件。'),sources=['https://en.wiktionary.org/wiki/classes#English','https://en.wiktionary.org/wiki/class#English'])
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_xc',ROOTS,WORDS)
 extend_lessons()
