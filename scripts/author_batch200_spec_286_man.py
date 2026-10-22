# coding: utf-8
from pathlib import Path
import json
from lesson_authoring import entry as E
BASE=Path(__file__).resolve().parents[1];OUT=BASE/'.cache/batch200/drafts/rewrite_spec'
ID='C0704';TAG='286_man';SHARED=[];EXCLUDE_REASON='按当前范围暂略罕见形容词与哲学、神学低频派生，保留 emanate 和 emanation。'
M=[['拉丁 mānāre〔流〕','液体流动的基本画面'],['拉丁 ē-〔向外〕+ mānāre → ēmānāre','流出；引申为出自某个来源']]
W=[E('emanate','/ˈeməneɪt/','散发；发出；源自','声音、气味、气场或想法，像从一个源头向外流。','接拉丁 ēmānāre 及其分词 ēmānātus；ē- 是 ex- 向外的形式，mānāre 是流。不要把其中的 man 理解为人或手。',M+[['拉丁 ēmānātus → 英语 emanate','散发；出自某个源头']],'Music emanates from a room，把声音放在主语位置，房间是来源。She emanates calm，则把人放在主语位置，说她散发平静的气场。抽象的 ideas emanating from a committee 也是同一幅“从源头出来”的画面。','emanate from something；emanate confidence；emanate warmth。','emit 常用于光、热、气体等的发出；emanate 更容易突出来源，也常用于气质和想法。它的语气比 come from 正式。',('A warm smell of bread emanated from the kitchen.','厨房里飘出了热面包的香味。'),('The speaker emanated calm and confidence.','演讲者散发着沉着自信的气场。'),sources=['https://www.etymonline.com/word/emanate','https://www.etymonline.com/word/emanation','https://www.oxfordlearnersdictionaries.com/definition/english/emanate']),
E('emanation','/ˌeməˈneɪʃən/','散发；散发出的东西；源出物','把“从源头往外出来”这个过程，或出来的东西，作为名词来谈。','借后期拉丁 ēmānātiō，来自 ēmānāre。虽然现代可对应 emanate + -ion，但英语名词记录早于动词，不宜写成由英语 emanate 首次造出。',M+[['后期拉丁 ēmānātiō → 英语 emanation','流出、散发；散发出的东西']],'an emanation of light 是散出的光；emanations from the factory 可指工厂排散出的气体等。这个词较正式，也常见于文学或哲学文章；核心仍是某个来源向外给出东西。','an emanation of light；emanations from a source；a direct emanation of something。','emission 常用于具体排放或发射；emanation 的范围还包括抽象影响与思想产物，读起来往往更书面。',('A faint emanation of light appeared beneath the door.','门下透出了一丝微光。'),('The writer presents the poem as an emanation of grief.','作者把这首诗描述为悲痛自然流露出的产物。'),sources=['https://www.etymonline.com/word/emanation','https://www.oxfordlearnersdictionaries.com/definition/english/emanation'])]
ROOT=dict(meaning='流；流动',core='某种东西从内部或源头向外流出。',image='门缝里透出光，厨房里飘出香味，人的举止里流露出自信。',intro='这里的 man- 接拉丁 mānāre“流”。加上 ē- 向外，得到 ēmānāre；借入英语后，具体的光、气味和抽象的气场、想法都能沿这条路线理解。',forms='emanate 接拉丁动词及分词形式；emanation 有独立的后期拉丁名词路线，英语中反而先出现名词。',branches=[['散发、出自','emanate'],['散发的过程或产物','emanation']],contrasts='这支 man- 不是 mānus“手”，也不是英语 man“人”。不用表面相同的三个字母强串来源。',practice='把 emanate from 的主语想成流出来的东西，把 from 后面想成源头。',sources=['https://www.etymonline.com/word/emanation','https://www.etymonline.com/word/emanate'])
m=json.loads((BASE/'.cache/batch200/rewrite_spec.json').read_text());r=next(x for x in m['roots']if x['id']==ID);c=next(x for x in json.loads((BASE/'.cache/catalog.json').read_text())if x['id']==ID);keep={w['word']for w in W}|set(SHARED);excluded={w:EXCLUDE_REASON for w in(set(r['family'])|set(c['family'])|set(c.get('unmatched',[])))-keep}
ROOT['id']=ID;ROOT['words']=list(dict.fromkeys([w for w in r['family']if w in keep]+[w for w in SHARED if w not in r['family']]));ROOT['exclude']=excluded
assert all(w['word']in m['owned_words']for w in W)
assert not(set(c['family'])|set(c.get('unmatched',[])))-set(ROOT['words'])-set(excluded)
assert {w['word']for w in W}<=set(ROOT['words'])
for w in W:assert len(w['examples'])>=2 and all(len(n)==2 and all(isinstance(x,str)and x for x in n)for n in w['history'])
for k,d in [('roots',[ROOT]),('words',W)]: (OUT/f'{k}_batch200_spec_{TAG}.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
print(ID,len(W),'new,',len(SHARED),'shared')
