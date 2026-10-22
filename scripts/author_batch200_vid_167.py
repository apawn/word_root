# -*- coding: utf-8 -*-
"""C0388 eso: inside an intellectual circle."""
import json
from pathlib import Path
from lesson_authoring import entry as E
BASE=Path(__file__).resolve().parents[1];OUT=BASE/'.cache/batch200/drafts/rewrite_vid'
W=[
E('esoteric','英 /ˌiːsəˈterɪk/ 或 /ˌesəˈterɪk/；美 /ˌesəˈterɪk/','只有少数内行懂的；小圈子秘传的','想象房间里只有几位行家，一句话不用解释，他们就都懂了；门外的人却听得满头雾水。esoteric 说的就是这种“内圈才懂”的内容。','来自希腊 esōterikos“属于内部的”，经拉丁化形式进入英语。esōterō 是“更往里面”，接 esō“在内”。现代学习可认 eso-“内部”，但不要把这个借词当作随意拼出的英语缩写。',[['希腊 esō → esōterō','在内 → 更往里面'],['希腊 esōterikos → 拉丁化借入英语 esoteric','属于内圈的；只向内圈传授的'],['英语中的专业、小众用法','只有少数掌握相关知识的人容易理解']],'古老用法可指只传给内圈学生的学说。今天更常见的情形是某门专业的冷知识、难懂术语或小众兴趣：内容可以公开放在网上，仍然很 esoteric，因为需要背景知识才能懂。这个词有时带“未免太偏、太难懂”的评价，不一定在称赞高深。','esoteric knowledge；esoteric terminology；an esoteric interest；too esoteric for a general audience。','secret 强调不让别人知道；esoteric 强调只有少数人理解或接触。一本公开出售的专业书也可以很 esoteric。',('Their conversation turned to an esoteric feature of an old programming language.','他们聊起了一种老编程语言里只有少数内行熟悉的特性。'),('The museum explains these once esoteric rituals in everyday language.','博物馆用日常语言解释这些过去只在内圈传授的仪式。'),sources=['https://www.etymonline.com/word/esoteric','https://www.oxfordlearnersdictionaries.com/definition/english/esoteric']),
E('esotericism','美 /ˌesəˈterəˌsɪzəm/','秘传学说或实践；小众难懂的性质','esoteric 描述“内圈才懂”，esotericism 则把它当成一种现象来谈：可能是一批秘传的学说，也可能是一篇文章过于晦涩的特点。','英语 esoteric + -ism。这里 -ism 可以把相关学说、实践或某种性质概括成名词；不是每个 -ism 都意味着有一个统一组织或正式教派。',[['希腊 esōterikos → 英语 esoteric','内圈的；少数人懂的'],['英语 esoteric + -ism → esotericism','这类学说、实践，或这种难懂的性质']],'在宗教史、思想史文章中，esotericism 可以概括强调内圈传授或隐秘知识的传统；它不是所有相关人都属于同一宗教的证明。放在文风评价里，则可能是在说作者把内容写得过于圈内化，一般读者很难进入。先看上下文是在谈思想内容，还是在评价表达方式。','Western esotericism；the study of esotericism；the esotericism of a text。多用于较正式的文化、宗教史或文学讨论。','mysticism 通常侧重直接的精神或神秘体验；esotericism 更突出隐秘知识、内圈传统或小众性质，两者可有交集而不完全重合。',('Her research examines esotericism in Renaissance Europe.','她的研究探讨文艺复兴时期欧洲的秘传思想。'),('The reviewer admired the argument but criticized the book’s esotericism.','评论者欣赏书中的论证，却批评它写得过于晦涩、只有少数内行能懂。'),sources=['https://www.merriam-webster.com/dictionary/esotericism','https://www.collinsdictionary.com/dictionary/english/esotericism']),
]
m=json.loads((BASE/'.cache/batch200/rewrite_vid.json').read_text());r=next(x for x in m['roots'] if x['id']=='C0388')
EX={w:'眼科眼位的专门术语，按当前通用阅读范围暂略。' for w in r['family'] if w not in {e['word'] for e in W}}
ROOT=dict(id='C0388',meaning='里面、内部',core='eso- 的原始方向是“往里面”。在本组阅读词里，空间上的内外变成知识圈子的内外：谁在圈内、谁听得懂。',image='esō 在内 → esōterō 更往里 → esōterikos 内圈的 → esoteric → esotericism。',intro='记住一场行家之间的对话：每个人都懂，旁听者却接不上话。这个画面能解释现代 esoteric，而“仅向内圈传授”能解释它更早的用法。',forms='eso- 源自希腊“在内”；esoteric 是希腊形容词的拉丁化借入形式，esotericism 是英语后加 -ism 的名词。',branches=[['内圈知识与小众性质','esoteric, esotericism']],contrasts='公开与秘密是一条线，内行与外行是另一条线。现代 esoteric 可以很公开，却仍需要专业背景才懂。',practice='遇到 esoteric，先问“是不让别人看，还是看了也不容易懂？”现代语境经常是后者。',words=[e['word'] for e in W],exclude=EX)
if __name__=='__main__':
 assert {e['word'] for e in W}<=set(m['owned_words'])
 for kind,data in [('roots',[ROOT]),('words',W)]: (OUT/(kind+'_batch200_vid_167.json')).write_text(json.dumps(data,ensure_ascii=False,indent=2))
 print('eso:',len(W),'words;',sum(len(e['examples']) for e in W),'examples')
