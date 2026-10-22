# coding: utf-8
from pathlib import Path
import json
from lesson_authoring import entry as E
BASE=Path(__file__).resolve().parents[1];OUT=BASE/'.cache/batch200/drafts/rewrite_spec'
ID='C1012';TAG='276_phalang';SHARED=[];EXCLUDE_REASON='aphalangia 为罕见临床名称；phalanges 是 phalanx 的解剖复数，已在该词内说明，不重复立条。'
W=[E('phalanx','英 /ˈfælæŋks/；美 /ˈfeɪlæŋks/；解剖复数 phalanges /fəˈlændʒiːz/','密集方阵；密集的一群人；指骨、趾骨','一边是人紧密排成阵，一边是骨头按节列在一起。','来自希腊 phálanx，也经拉丁 phalanx 传播。希腊词本身已有战阵和指趾骨等用法，不是英语先发明方阵，再另造一个形似的骨名。',[['希腊 phálanx，屈折词干 phalang-','密集战阵；也有指趾骨用法'],['拉丁及英语 phalanx','军事方阵与解剖名称'],['英语泛化和比喻','密集站在一起、共同形成屏障的一群人']],'a phalanx of reporters 像一堵挤在一起的记者墙，强调阵势密集。解剖里 a phalanx 则是一节指骨或趾骨；这些骨排列衔接的形象，与方阵的排列感能够互相帮助记忆。','a phalanx of guards；an infantry phalanx；a finger phalanx。人群复数常用 phalanxes，骨名复数常用 phalanges。','phalanx 不只是任何人群 crowd，它带紧密排列的画面；phalanges 指骨头，不是手指关节本身。',('A phalanx of photographers waited outside the building.','一大排摄影记者密集地守在楼外。'),('The soldiers advanced in a tightly packed phalanx.','士兵们排成密集方阵向前推进。'),('The thumb has two phalanges, while each other finger has three.','拇指有两节指骨，其余每个手指有三节。'),sources=['https://www.etymonline.com/word/phalanx','https://www.oxfordlearnersdictionaries.com/definition/english/phalanx','https://www.hopkinsmedicine.org/health/treatment-tests-and-therapies/anatomy-of-the-hand'])]
ROOT=dict(meaning='密集方阵；指骨、趾骨',core='把多个单位紧密排列起来，形成连贯的一列或一个阵势。',image='人紧密站成阵，骨头一节节相接；先抓排列的形象。',intro='phalanx 不只出现在古代战争中。现代报道也用它写记者、保镖等形成的人墙；解剖里则常见复数 phalanges。',forms='希腊 phálanx 的屈折词干为 phalang-；英语保留 phalanx，并在解剖复数中使用 phalanges。',branches=[['战阵与人群','phalanx；phalanxes'],['指骨、趾骨','phalanx；复数 phalanges']],contrasts='方阵不必在每次比喻中真的呈正方形；骨名也不是关节名称。',practice='把 a phalanx of guards 与 the phalanges of a finger 分别想成两个排列画面。',sources=['https://www.etymonline.com/word/phalanx','https://www.oxfordlearnersdictionaries.com/definition/english/phalanx'])
m=json.loads((BASE/'.cache/batch200/rewrite_spec.json').read_text());r=next(x for x in m['roots']if x['id']==ID);c=next(x for x in json.loads((BASE/'.cache/catalog.json').read_text())if x['id']==ID);keep={w['word']for w in W}|set(SHARED);excluded={w:EXCLUDE_REASON for w in(set(r['family'])|set(c['family'])|set(c.get('unmatched',[])))-keep}
ROOT['id']=ID;ROOT['words']=list(dict.fromkeys([w for w in r['family']if w in keep]+[w for w in SHARED if w not in r['family']]));ROOT['exclude']=excluded
assert all(w['word']in m['owned_words']for w in W)
assert not(set(c['family'])|set(c.get('unmatched',[])))-set(ROOT['words'])-set(excluded)
assert {w['word']for w in W}<=set(ROOT['words'])
for w in W:assert len(w['examples'])>=2 and all(len(n)==2 and all(isinstance(x,str)and x for x in n)for n in w['history'])
for k,d in [('roots',[ROOT]),('words',W)]: (OUT/f'{k}_batch200_spec_{TAG}.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
print(ID,len(W),'new,',len(SHARED),'shared')
