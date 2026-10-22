# -*- coding: utf-8 -*-
"""C1121 preter: pass beyond a point, in time or degree."""
import json
from pathlib import Path
from lesson_authoring import entry as E
BASE=Path(__file__).resolve().parents[1];OUT=BASE/'.cache/batch200/drafts/rewrite_vid'
W=[E('preterite','英 /ˈpretərɪt/；美 /ˈpretərət/〔也写 preterit〕','过去时；过去时形式；过去时的','把视线移到已经过去的时间：went、saw、worked 这类过去时形式，可以在语法书里叫 preterite forms。','经古法语 preterit／盎格鲁法语及拉丁语来源进入中古英语；拉丁 praeteritum、praeteritus 是 praeterire“走过、经过”的分词形式。更里面是 praeter“越过”加 ire“去”：时间已经从眼前走过去了。',[['拉丁 praeter；ire','越过、经过；去'],['praeterire → praeteritus／praeteritum','走过去 → 已过去的；用于过去时间名称'],['古法语／盎格鲁法语 preterit；拉丁直接借入路线','过去、过去时'],['中古英语 preterit → 英语 preterite／preterit','过去时或其形式，也作形容词']],'这是语法标签，不表示事情一定发生在很遥远的年代。不同语言教材对 preterite 的使用范围不完全相同；英语讨论里常指简单过去形式。它也不等于过去分词：go 的 preterite 是 went，过去分词是 gone。','the preterite of a verb；the preterite tense；preterite forms。名词可用 the preterite，形容词直接修饰 tense 或 form。','past participle 是过去分词；preterite 是过去时名称或形式。也不要把词头误认成表示“在……之前”的普通 pre- 后随意拆剩下部分。',('The preterite of go is went.','go 的过去时形式是 went。'),('The exercise asks students to identify the preterite forms in the passage.','这道练习要求学生找出文中的过去时形式。'),sources=['https://www.etymonline.com/word/preterite','https://www.merriam-webster.com/dictionary/preterite','https://www.collinsdictionary.com/dictionary/english/preterite'])]
names=['preternatural','preterite'];cat=next(x for x in json.loads((BASE/'.cache/catalog.json').read_text()) if x['id']=='C1121')
EX={w:'较罕见的省略、搁置名词，按当前通用阅读范围暂略。' for w in cat['family'] if w not in names}
ROOT=dict(id='C1121',meaning='经过；越过；超出',core='preter- 接拉丁 praeter。想象越过一个位置：时间越过去，成为过去；超出通常自然状态，则显得异乎寻常。',image='praeter 越过 → praeterire 走过 → preterite 过去时；praeter naturam 超出自然 → preternatural 超乎寻常。',intro='这里的“过去”不是只靠 pre- 猜出来的。完整的拉丁动作 praeterire“走过去”才把语法名称和空间画面接起来。',forms='preterite 经过拉丁分词及法语借入路线；preternatural 接中世纪拉丁 preternaturalis，与拉丁短语 praeter naturam 相连。',branches=[['超出通常程度','preternatural'],['时间已经经过','preterite']],contrasts='preternatural 不必真的涉及鬼神，也可形容惊人的镇定；preterite 不等于过去分词，且各语言的语法用法须看具体体系。',practice='把 preterite 与 went 联系，把 preternatural calm 与“镇定得超出预期”联系，分别抓住时间和程度。',words=names,exclude=EX)
if __name__=='__main__':
 for kind,data in [('roots',[ROOT]),('words',W)]: (OUT/(kind+'_batch200_vid_221.json')).write_text(json.dumps(data,ensure_ascii=False,indent=2))
 print('preter: 1 new; 2 examples; 1 shared')
