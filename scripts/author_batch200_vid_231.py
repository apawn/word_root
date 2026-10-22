# -*- coding: utf-8 -*-
"""C0354 dy: two entities considered as a pair, especially in interaction."""
import json
from pathlib import Path
from lesson_authoring import entry as E
BASE=Path(__file__).resolve().parents[1];OUT=BASE/'.cache/batch200/drafts/rewrite_vid'
W=[
E('dyad','/ˈdaɪæd/','二元组；一对相互关联的人或事物','研究两个人怎样互相影响时，把这两个人当成一个关系单位，而不是只单独观察其中一个。这一对就可以叫 dyad。','经晚期拉丁 dyas、词干 dyad- 接希腊 dyas“两个、一对”，再接 dyo／duo“两”。英语借入的是一对这一名词，不是 dye“染色”去掉 e。',[['希腊 dyo／duo → dyas〔词干 dyad-〕','两 → 一对、两个组成的单位'],['晚期拉丁 dyas／dyad-','一对的学术名称'],['英语 dyad','一对；常用于两者之间的关系分析']],'在社会科学里，医生和病人、父母一方和孩子、一起完成任务的两个人，都可作为 dyad 来研究。这个词并不要求两人是恋人，也不保证关系亲密；重要的是分析时把两者及其联系放在一起。','a dyad of participants；study dyads；interaction within a dyad。复数 dyads。','pair 是日常的一对；dyad 偏学术，常突出两者共同构成的关系单位。其他数学、生物学专门义需要另看该领域定义。',('The researchers observed each dyad during a short conversation.','研究人员观察了每一对参与者在简短交谈中的表现。'),('Each dyad consisted of a parent and a child.','每个二人组由一位家长和一个孩子组成。'),sources=['https://www.etymonline.com/word/dyad','https://www.merriam-webster.com/dictionary/dyad','https://en.wiktionary.org/wiki/dyad#English']),
E('dyadic','/daɪˈædɪk/','二元的；两者之间的；由一对构成的','研究不是只问“甲是什么样的人”，而是看“甲和乙怎样相互回应”。这种以两者及其联系为单位的关系或互动就是 dyadic。','与 dyad 对应，现代可按 dyad + -ic 理解。历史词源也接希腊 dyadikos“二的、一对的”，本身来自 dyas、dyad-；不能只把希腊形容词的路线省掉，认定全是英语后来现拼。',[['希腊 dyo／duo → dyas、dyad-','两 → 一对'],['希腊 dyadikos；现代对应 dyad + -ic','与两个、成对关系有关的'],['英语 dyadic','二元的、两者之间的；用于关系或结构描述']],'dyadic communication 是两者之间的交流，dyadic relationship 是两者的关系。它和“两个阵营互相对立”没有必然联系；两者可以合作，也可以冲突。数学、逻辑里的二元用法同样重视涉及两个项，但具体规则由该领域决定。','dyadic communication；dyadic interaction；a dyadic relationship；dyadic analysis。','dyad 是那一对，dyadic 修饰互动、关系或分析方式。binary 常强调两种值或类别，dyadic 在人际研究中更突出双方的相互联系。',('The study focuses on dyadic communication between friends.','这项研究关注朋友之间的双人交流。'),('The task was designed to encourage dyadic interaction rather than individual work.','这项任务旨在鼓励两人互动，而不是各自单独完成。'),sources=['https://www.collinsdictionary.com/dictionary/english/dyadic','https://www.merriam-webster.com/dictionary/dyad','https://en.wiktionary.org/wiki/dyadic#English']),
]
ROOT=dict(id='C0354',meaning='两；一对',core='dy- 在这组里接希腊“两”。把两个成员圈成一个关系单位，先问他们之间发生了什么，就抓住 dyad 的常见学术用法。',image='两 dyo／duo → 一对 dyas、dyad- → dyad；形容词 dyadikos → dyadic 两者之间的。',intro='这组适合读心理、教育和社会研究文章。先用亲子、同伴两人交谈这些场景理解，再遇到二元分析就不至于只记抽象汉语。',forms='dyad 经晚期拉丁接希腊名词；dyadic 与希腊形容词及现代 dyad + -ic 对应。重音分别在 /ˈdaɪæd/ 和 /daɪˈædɪk/。',branches=[['一对及双方的互动','dyad, dyadic']],contrasts='dyad 不限情侣，也不保证相互友好；dyadic 不是所有含数字二的东西都必须使用的日常形容词。',practice='先把两名参与者称为 a dyad，再把他们的交谈称为 dyadic communication。',words=[x['word'] for x in W],exclude={})
if __name__=='__main__':
 for kind,data in [('roots',[ROOT]),('words',W)]: (OUT/(kind+'_batch200_vid_231.json')).write_text(json.dumps(data,ensure_ascii=False,indent=2))
 print('dy: 2 words; 4 examples')
