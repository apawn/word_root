# -*- coding: utf-8 -*-
"""C1658 vom: distinguish feeling sick, the action, and what comes out."""
import json
from pathlib import Path
from lesson_authoring import entry as E
BASE=Path(__file__).resolve().parents[1];OUT=BASE/'.cache/batch200/drafts/rewrite_vid'
H=[['拉丁 vomere；相关 vomitus、vomitare','吐出；相应名词／分词形式与表示反复动作的动词'],['法语 vomite 与拉丁动词路线 → 中古英语 vomit／vomiten','呕吐物、呕吐这一行为；动词表示吐出'],['现代英语 vomit','既可作呕吐的动词，也可作呕吐物的名词']]
W=[
E('vomit','英 /ˈvɒmɪt/；美 /ˈvɑːmɪt/','呕吐；呕吐物','胃里的东西反向从嘴里出来。动词说发生这个动作，名词说吐出来的东西。','远源是拉丁 vomere“吐出”。名词与拉丁 vomitus、法语 vomite 相连；动词也有接拉丁 vomitare“反复吐出”的分析。vomitus 与 vomitare 同族，但不能把 vomitus 错当成 vomitare 的过去分词。',H,'He vomited 是“他吐了”；There was vomit on the floor 里的 vomit 是呕吐物。日常聊天也常说 throw up；vomit 更直接、较常用于病情描述和正式记录。','feel like vomiting；vomit after a meal；vomit something up；vomit on the floor。名词呕吐物通常不可数。','nausea 是恶心、想吐的感觉，未必真的 vomit。spit 是把口腔里的东西吐出，通常不涉及把胃内容物反向排出来。',('She felt nauseous during the journey but did not vomit.','她在旅途中觉得恶心，但没有吐。'),('The cleaner found vomit near the back door.','清洁工在后门附近发现了呕吐物。'),sources=['https://www.merriam-webster.com/dictionary/vomit','https://www.oxfordlearnersdictionaries.com/definition/english/vomit_1','https://en.wiktionary.org/wiki/vomit','https://en.wiktionary.org/wiki/vomitus']),
E('vomiting','英 /ˈvɒmɪtɪŋ/；美 /ˈvɑːmɪtɪŋ/','呕吐这一过程；vomit 的 -ing 形式','把“吐”看成正在发生的动作，或把反复发生的呕吐当成一个症状、过程来谈。','英语 vomit + -ing。可作现在分词，如 was vomiting；也可把动作名词化，如 nausea and vomiting。重音在首音节，拼写不把末尾 t 双写。',H+[['英语 vomit + -ing → vomiting','正在呕吐；把动作作为一个过程来谈']],'The vomiting stopped 是呕吐停止了，重点在动作不再发生。a vomiting episode 是一次呕吐发作；nausea and vomiting 把“恶心感”和“实际呕吐”并列写清楚。','nausea and vomiting；an episode of vomiting；repeated vomiting；stop vomiting。','名词 vomit 常是吐出的东西，vomiting 是吐的过程。若说 clean up the vomit，就是清理呕吐物；record the vomiting episodes，则是在记录发生次数。',('The form asks whether there has been any nausea or vomiting.','表格询问是否出现过恶心或呕吐。'),('The nurse recorded two episodes of vomiting during the night.','护士记录了夜间发生的两次呕吐。'),sources=['https://www.oxfordlearnersdictionaries.com/definition/english/vomit_1','https://www.merriam-webster.com/dictionary/vomit']),
]
SH=set();EX={w:'较冷门的医学旧称或建筑专门术语，本轮优先保留常用 vomit 和 vomiting。' for w in ['vomitus','vomition','vomitory']}
ROOT=dict(id='C1658',meaning='吐出、排出',core='本组的核心动作是把里面的东西吐到外面。常用英语主要集中在呕吐这个身体动作，以及动作和呕吐物的区别。',image='拉丁 vomere 吐出 → vomitus、vomitare 等相关形式 → 英语 vomit 呕吐／呕吐物 → vomiting 呕吐过程。',intro='先分三件事：nausea 是想吐的感觉，vomit 作动词是实际吐出来，vomit 作名词常是吐出来的东西。vomiting 再把动作变成可讨论、可记录的过程。',forms='拉丁 vomere 有相关的 vomitus 形式和反复动作动词 vomitare；英语名词与法语 vomite、拉丁名词相连，动词也有拉丁动词路线。现代 vomiting 是规则的英语 -ing 形式。',branches=[['动作与呕吐物','vomit'],['过程与记录','vomiting']],contrasts='不要把 nausea 一律译成已经呕吐，也不要把名词 vomit 与过程名词 vomiting 混用。日常 throw up 较随意，vomit 较直接。',practice='The vomiting stopped, but there was vomit on the floor. 呕吐停了，地板上却还有呕吐物：前者是过程，后者是已经吐出来的东西。',words=[],exclude=EX)
if __name__=='__main__':
 m=json.loads((BASE/'.cache/batch200/rewrite_vid.json').read_text());r=next(x for x in m['roots'] if x['id']==ROOT['id']);ROOT['words']=[w for w in r['family'] if '-' not in w and w not in EX]
 assert set(ROOT['words'])=={e['word'] for e in W}
 assert {e['word'] for e in W}<=set(m['owned_words'])
 for kind,data in [('roots',[ROOT]),('words',W)]: (OUT/(kind+'_batch200_vid_139.json')).write_text(json.dumps(data,ensure_ascii=False,indent=2))
 print('vom:',len(W),'words;',sum(len(e['examples']) for e in W),'examples')
