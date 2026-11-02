"""Two useful endings: recognisable adjective forms and phren- naming."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
from continuation_extensions import extend_existing_lessons
WORDS.clear();ROOTS.clear()
EXISTING_ROOT_ADDITIONS={
 'C0511':dict(words=['gymnast','gymnastic','gymnastics'],label='gymnast／gymnastic／gymnastics：人、形容词与活动名',note='gymnastic 借拉丁 gymnasticus，上接希腊 gymnastikos；gymnast + -ic 是现代认形对应，不取代真实借入历史。'),
 'B3250':dict(words=['school','scholar','scholastic'],label='school／scholar／scholastic：学校词族的不同借入路线',note='scholastic 经法语、拉丁接希腊 scholastikos；学校相关义和经院哲学义依具体语境判断。'),
}
W('gymnastic','/dʒɪmˈnæstɪk/','体操的；身体锻炼的',
 '让身体练出柔韧、平衡和协调，是 gymnastic 最常见的画面。它是形容词，用来描述训练、动作或相关能力。',
 '借拉丁 gymnasticus，接希腊 gymnastikos 与锻炼有关的；更早有 gymnazein 锻炼、gymnos 裸露。现代可联系 gymnast + -ic 认形，但英语形容词不是必定先由英语 gymnast 新造。',
 [['希腊 gymnos → gymnazein → gymnastikos','裸露 → 以古希腊训练背景形成锻炼用词'],['拉丁 gymnasticus → 英语 gymnastic','与体操、身体锻炼有关的']],
 'gymnastic exercises 体操练习；gymnastic training 体操训练；gymnastic skills 体操技能。词尾 -ic 在这里帮助识别形容词。',
 'a gymnastic routine；gymnastic ability。','gymnast 是人，gymnastic 是形容词，gymnastics 是体操活动名称。gymnastics 虽以 s 结尾，作为学科、运动名称时常按单数整体使用。',
 ('The warm-up includes several simple gymnastic exercises.','热身包括几个简单的体操练习。'),('Her gymnastic training helped her keep her balance.','体操训练帮助她保持平衡。'),sources=['https://en.wiktionary.org/wiki/gymnastic#English'])
W('scholastic','/skəˈlæstɪk/','学校、学业的；经院哲学的；经院哲学家〔名词〕',
 '先想到学校里的读书、学习。再到历史语境中，scholastic 又专门关联中世纪学校传统发展出的经院哲学。',
 '经中古法语 scholastique 借拉丁 scholasticus，接希腊 scholastikos，属于 schole 学习、闲暇词族，与 school 共同远源。不是现代 school 随手换拼写再加 -astic。',
 [['希腊 schole → scholastikos → 拉丁 scholasticus','学习、学问相关；后来有特定学术传统'],['中古法语 scholastique → 英语 scholastic','学校、学业的；经院哲学的；相应学者']],
 'scholastic achievement 学业成绩；scholastic ability 学习能力；scholastic philosophy 经院哲学。名词 a scholastic 在哲学史语境常指经院哲学家。',
 'scholastic success；a scholastic tradition。','scholarly 更常强调有学问、学术研究的品质；scholastic 可直接说学业，也可有特定哲学史含义。看到哲学史上下文时，不能只译成学校的。',
 ('The award recognises scholastic achievement and community service.','这个奖项表彰学业成就和社区服务。'),('The chapter introduces several scholastic philosophers.','这一章介绍了几位经院哲学家。'),sources=['https://en.wiktionary.org/wiki/scholastic#English'])
R('A2228','常见形容词尾部；与某种活动、性质有关','-ASTIC：先认出形容词，再查清前面的实际词干',
 '体操运动员在做动作，旁边的说明用 gymnastic 描述动作；活动、人、形容词彼此对应。',
 '读到 enthusiastic、gymnastic、scholastic，可以先认出形容词。词典把 -astic 概括为 -ast 与 -ic 的组合，但几个词的完整历史并不都等于英语词根加同一个尾巴：有的整词借自希腊、拉丁和法语形容词，有的经历英语类推。把这些词放在一页，是帮助看清相似结构，也看清不能硬拆的边界。',
 '-ic 常标记形容词；-ast 可出现在人物、活动相关词干中。gymnast／gymnastic 是好认的现代对应；enthusiastic 上接希腊 enthousiastikos；sarcastic 的英语形成与法语借入有不同分析。',
 [['体操：人、形容词、活动','gymnast · gymnastic · gymnastics'],['学校与学问','school · scholar · scholastic'],['热情与嘲讽的形容词对照','enthusiast · enthusiastic · sarcasm · sarcastic']],
 '相同尾部不保证相同词根。sarcastic 不拆成 sarc + 一个万能的英语 -astic；scholastic 与 school 同族，但不是英语 school 简单加字母而来。',
 'Her enthusiastic description made the gymnastic exercises sound less intimidating.\n\n她兴致勃勃地介绍了这些体操练习，让它们听起来没那么吓人。',
 'gymnast gymnastic gymnastics school scholar scholastic enthusiast enthusiastic sarcasm sarcastic')
ROOTS[-1]['checked_sources']=['https://en.wiktionary.org/wiki/-astic','https://en.wiktionary.org/wiki/gymnastic','https://en.wiktionary.org/wiki/scholastic']
R('A2298','与心智状态有关的医学命名尾部','PHREN-：历史上的心智词；-IA：状态名词材料',
 '把一个医学名称看作历史标签：标签的字面材料帮助认词，完整含义仍由现代医学用法决定。',
 '-phrenia 由希腊 phren- 心智词干与 -ia 状态名词材料组成。phren 一系古义也有膈膜，但这个命名尾部关注心智状态。最值得认的词是 schizophrenia：它经近代德语造词进入英语，不是古代已有同名现代诊断。这里保留常见词，冷门专科词先不展开。',
 'phren- + -ia → -phrenia；schizo- 分开 + phren- 心智形成历史命名。schizophrenic 是同一名称的形容词、人物称呼形式；涉及人时常用 person with schizophrenia。',
 [['心智状态名称','schizophrenia'],['相应形容词与人物称呼','schizophrenic']],
 'schizophrenia 不能按汉语字面理解成多重人格。现代用词指精神分裂症，与 dissociative identity disorder 是不同概念；不用词根字面替代完整术语含义。',
 'The glossary explains the word schizophrenia without relying on its literal parts alone.\n\n术语表解释 schizophrenia 时，没有只靠字面拆分来下定义。',
 'schizophrenia schizophrenic')
ROOTS[-1]['checked_sources']=['https://en.wiktionary.org/wiki/-phrenia','https://www.nimh.nih.gov/health/publications/schizophrenia']
def extend_lessons():extend_existing_lessons(EXISTING_ROOT_ADDITIONS)
if __name__=='__main__':
 save('continuation_20261030_wg',ROOTS,WORDS)
 extend_lessons()
