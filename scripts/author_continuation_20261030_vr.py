"""Turn three remaining useful affix pages into readable linked lessons."""
from author_continuation_20261028_d import W,R,WORDS,ROOTS
from lesson_authoring import save
WORDS.clear();ROOTS.clear()
R('A1932','与某状态有关的；处于某状态的人〔依具体词〕',
 '-AC：先是有关某性质，部分词再用来称具有该状态的人',
 'insomnia 是失眠，insomniac 可以说失眠的，也可说失眠者。先记状态，再看这个词在句子里是形容性质，还是指人。',
 '相关词尾接希腊 -akos，经拉丁 -acus、法语等路径进入英语，与 -ic 的历史形式有联系。maniac 是较早整词借入；insomniac 等又体现英语后来的派生，路线并不完全相同。',
 '本页选 maniac、insomniac、amnesiac 三个已精讲的常见例子。-ac 有相关性质与人物名词用法，不能一见 ac 就当作一个新职业。另有药物命名中的同形词尾，来源不同。',
 [['状态与相应的人、性质','insomniac amnesiac'],['借入词与日常扩大用法','maniac']],
 'insomnia 是状态名，insomniac 可作相关形容词或人物名词；maniac 在口语还常说某方面极其热衷的人，具体语气与场景要看单词精讲。',
 'The novel follows an insomniac who writes at night.\n\n小说讲述了一位夜里写作的失眠者。',
 'maniac insomniac amnesiac')
R('A2027','具有某性质、与某物有关的〔形容词词尾〕',
 '-EOUS：把名称转到它具有什么性质',
 'gas 是气体，gaseous 是气态的。先看它是什么，再说它处于什么状态，这就是本页最实用的形式关系。',
 '-eous 不是只有一条来源。一组常与 -ous 及前面的元音一起形成、重新分析，也与拉丁 -eus 等形式有关；另一条较早路线联系 -wise 等日耳曼词尾。本页以现代常见 gaseous 为入口，不把全部同形结尾混成一个来源。',
 'gaseous 对应 gas 与形容词词尾，可按 gas + -eous 记忆；不同词典也会放在较宽的 -ous 形成规则下解释。字母相同不保证每个词都从一个现成英语底词直接构成。',
 [['基本名称','gas'],['状态、性质','gaseous']],
 'gas 是名词气体，gaseous 是形容词气态的。现代美国口语 gas 还可缩指汽油，那是 gasoline 的缩略义，不代表汽油在常温下就是气体。',
 'The substance changes from a liquid to a gaseous state.\n\n这种物质从液态变成气态。',
 'gas gaseous')
R('A2043','分开、裂开〔希腊组合形式〕',
 'SCHIZO-：分开；词根画面帮助看命名，完整词义仍要单独理解',
 '先记裂开、分开的核心。医学名 schizophrenia 采用这条历史命名材料，但完整病名的现代意思不能只靠把心智切成几份来想象。',
 '来自希腊 skhizein 分开、裂开，相关形式 skhizo- 带连接元音。schizophrenia 经德语 Schizophrenie 进入英语，是近代医学造词；schizophrenic 是相关形容词。',
 'schizo- + phren- 心智相关材料 + -ia 形成病名；schizophren- + -ic 形成形容词。schizo- 的分开是命名线索，phren- 的近代使用义也不能一律按古老身体部位硬译。',
 [['近代病名','schizophrenia'],['相关形容词','schizophrenic']],
 'schizophrenia 是精神分裂症；schizophrenic 说相关的、患该病的。精神分裂症与分离性身份障碍是不同概念，词源里的分开不能用来把病名解释成多重人格。',
 'The article explains the history of the word schizophrenia.\n\n这篇文章解释了 schizophrenia 这个词的历史。',
 'schizophrenia schizophrenic')
ROOTS[0]['checked_sources']=['https://www.merriam-webster.com/dictionary/-ac']
ROOTS[1]['checked_sources']=['https://en.wiktionary.org/wiki/-eous#English','https://www.etymonline.com/word/gaseous']
ROOTS[2]['checked_sources']=['https://www.etymonline.com/word/schizophrenia','https://www.nimh.nih.gov/health/publications/schizophrenia']
if __name__=='__main__':save('continuation_20261030_vr',ROOTS,WORDS)
