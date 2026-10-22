# coding: utf-8
import json
from pathlib import Path
from lesson_authoring import entry as E
W=[E('myriad','/ˈmɪriəd/','无数；大量；数不清的','眼前的东西多得像一片星空，不必真的一颗颗数完。','希腊 myrios 有无数的意思，也用于一万这个确定数目；其名词 myrias 经拉丁语、法语进入英语，英语又发展出形容词用法。',[['希腊 myrios → myrias','无数；一万 → 一万之数、大量'],['晚期拉丁 myrias；法语 myriade → 英语 myriad','一万；大量'],['英语名词 myriad → 形容词 myriad','大量 → 数不清的']],'现代文章里的 myriad 通常不是精确的一万个，而是数量非常多，有时还带种类丰富的感觉。a myriad of choices 把它当名词：大量选择；myriad choices 把它当形容词：无数选择。两种结构都成立，不必把 a myriad of 判成语法错误。','a myriad of + 复数名词；myriad + 复数名词；myriads of stars。语气比 many 更有画面感，也更偏书面。','many 只说多；myriad 更强调大量、繁多。今天的普通语境通常不取一万这个古老的精确数义。',('The app offers a myriad of ways to organize your notes.','这个应用提供了许多不同的笔记整理方式。'),('Myriad tiny lights glittered across the hillside.','山坡上闪着无数微小的灯光。'),sources=['https://www.etymonline.com/word/myriad','https://www.merriam-webster.com/dictionary/myriad'])]
ROOT=dict(id='C0784',meaning='无数；一万',core='MYRI = COUNTLESS / TEN THOUSAND',image='满眼都是细小的点，数量多得让人放弃一个个去数。',intro='希腊 myrios 可表示无数，也用于一万这个数。现代英语最值得掌握的是 myriad：普通阅读里多半表示大量，而不是精确计数。原词的两个意思都要知道，但不必硬编成先有一万、后来才有无数的单线故事。',forms='myriad 的来源是希腊名词 myrias，其词干有 myriad-。现代英语常用名词与形容词两种词性，不是把 my 和 riad 拆成英语成分。',branches=[['数量多得数不过来','myriad']],contrasts='a myriad of choices 与 myriad choices 都可以。把前一种结构说成错误，会把本来正常的名词用法误删。',practice='A myriad of possibilities and myriad possibilities both mean that there are many possibilities.\n\n两种搭配都在说：可能性很多。',words=['myriad'],exclude={w:'较冷门的动物分类或旧单位词，先略过' for w in ['myriapod','myriagon','myriagram','myriapodology']})
if __name__=='__main__':
 for name,data in [('roots_myri',[ROOT]),('words_myri',W)]:Path('.cache/batch200/drafts/root/'+name+'.json').write_text(json.dumps(data,ensure_ascii=False,indent=2))
 print(len(W),sum(len(x['examples']) for x in W))
