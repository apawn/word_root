# -*- coding: utf-8 -*-
from pathlib import Path
import json
from lesson_authoring import entry as E
BASE=Path(__file__).resolve().parents[1];OUT=BASE/'.cache/batch200/drafts/rewrite_spec'
ID='C1027';TAG='250_phrag';SHARED=[];EXCLUDE_REASON='按用户当前范围暂略：低频隔膜或围挡相关术语。'
W=[E('diaphragm','/ˈdaɪəfræm/','膈肌；隔膜、振膜；光圈装置；避孕隔膜','先想成横在中间的一层，再看它是在身体里还是设备里。','经后期拉丁 diaphragma 接希腊 diáphragma“隔开物”，来自 dia- 横过与 phrássein“围住、隔开”的组合动词，再形成结果名词。英语借入完整词，词末 gm 中的 g 不发音。',[['希腊 dia-〔横过〕与 phrássein〔围住、隔开〕','两种构词材料结合'],['希腊 diáphragma → 后期拉丁 diaphragma','隔开物；胸腹之间的膈'],['中古英语 diafragma → 英语 diaphragm','膈肌；后来也用于不同设备的薄膜或隔开装置']],'身体里它主要指胸腔与腹腔之间的膈肌，参与呼吸。麦克风里的 diaphragm 是能振动的薄膜；镜头里则是限制通光口大小的装置。它还可以指一种屏障式避孕器具。共同线索是分隔、覆盖或控制开口的一层，功能随场景改变。','the diaphragm；a microphone diaphragm；an iris diaphragm。不要把它一律译成膈肌。','aperture 指通光口及其大小；diaphragm 可指控制这个口的装置。声学中的 diaphragm 则是振膜，不能硬套成光圈。',('The model shows the diaphragm between the chest and abdomen.','模型展示了胸部与腹部之间的膈肌。'),('Sound waves make the microphone’s diaphragm vibrate.','声波使麦克风的振膜振动。'),('The lens diaphragm controls the size of the opening.','镜头的光圈装置控制通光口的大小。'),sources=['https://www.etymonline.com/word/diaphragm','https://www.merriam-webster.com/dictionary/diaphragm'])]
ROOT=dict(meaning='围住；隔开',core='phrag- 的画面是设一道隔层，diaphragm 把这个画面带进身体和器材。',image='横在中间的一层：身体里分隔胸腹，设备里可用于分隔、振动或控制开口。',intro='本组最值得先学的是 diaphragm。理解一道隔层，就能在医学、摄影、音响三个场景里认出它，而不必把几种中文译法分开硬背。',forms='希腊 phrássein 的相关词干有 phrag-/phrak-；diáphragma 是已经在古希腊语中形成的名词。',branches=[['身体结构','diaphragm：膈肌'],['设备与器具','diaphragm：隔膜、振膜、光圈装置']],contrasts='phrag- 表示围隔，不要与 phag-“吃”少一个 r 的词族混淆。diaphragm 词末的 g 不单独发音。',practice='分别在呼吸、麦克风和镜头三个场景中解释 diaphragm，找出“一层隔开物”的共同画面。',sources=['https://www.etymonline.com/word/diaphragm'])
m=json.loads((BASE/'.cache/batch200/rewrite_spec.json').read_text());r=next(x for x in m['roots']if x['id']==ID);c=next(x for x in json.loads((BASE/'.cache/catalog.json').read_text())if x['id']==ID);keep={w['word']for w in W}|set(SHARED);excluded={w:EXCLUDE_REASON for w in(set(r['family'])|set(c['family'])|set(c.get('unmatched',[])))-keep}
ROOT['id']=ID;ROOT['words']=list(dict.fromkeys([w for w in r['family']if w in keep]+[w for w in SHARED if w not in r['family']]));ROOT['exclude']=excluded
assert all(w['word']in m['owned_words']for w in W)
assert not(set(c['family'])|set(c.get('unmatched',[])))-set(ROOT['words'])-set(excluded)
assert {w['word']for w in W}<=set(ROOT['words'])
for w in W:assert len(w['examples'])>=2 and all(len(n)==2 and all(isinstance(x,str)and x for x in n)for n in w['history'])
for k,d in [('roots',[ROOT]),('words',W)]: (OUT/f'{k}_batch200_spec_{TAG}.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
print(ID,len(W),'new,',len(SHARED),'shared')
