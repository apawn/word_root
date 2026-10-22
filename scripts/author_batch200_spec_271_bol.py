# coding: utf-8
from pathlib import Path
import json
from lesson_authoring import entry as E
BASE=Path(__file__).resolve().parents[1];OUT=BASE/'.cache/batch200/drafts/rewrite_spec'
ID='C0126';TAG='271_bol';SHARED=[];EXCLUDE_REASON='embolism 来自希腊 embállein 投入一支，不是 bōlos 团块；已在 bal- 页独立精讲。'
W=[E('bolus','英 /ˈbəʊləs/；美 /ˈboʊləs/','团块；食团；一次给予的一份剂量','一小团聚在一起的东西，而不是均匀铺开的连续流。','经后期拉丁 bolus，来自希腊 bōlos“土块、团块”。医学中的一次给药份量由这种成团、集中一份的概念延伸，不表示药一定是固体。',[['希腊 bōlos〔土块、团块〕','一团聚在一起的物质'],['后期拉丁 bolus → 英语 bolus','丸、团块；咀嚼后形成的食团'],['医学剂量用法','一次集中给予的一份药物或液体']],'消化课里的 bolus 是嚼碎后混着唾液、准备吞下去的一团食物。医疗记录里的 a bolus 则可能是一份注入的药或液体；此时重点在给入方式，不是外形像丸子。','a food bolus；a bolus dose；a bolus injection；复数 boluses。','bolus 不是 blood clot“血凝块”的通用同义词；也不等于持续缓慢输入的 continuous infusion。',('Chewing forms the food into a soft bolus.','咀嚼把食物变成柔软的食团。'),('The report distinguishes a bolus dose from a continuous infusion.','报告区分了一次给入的剂量与持续输注。'),sources=['https://www.merriam-webster.com/dictionary/bolus','https://en.wiktionary.org/wiki/bolus']),
E('bole','英 /bəʊl/；美 /boʊl/','树干；〔另一来源〕含铁黏土','同一拼写有两条路：树的主干，或一种用于颜料等用途的黏土。','树干义经中古英语接古诺斯语 bolr；黏土义经拉丁 bolus、也有古法语 bol 的传播联系，远接希腊 bōlos“土块”。只有黏土义属于本页团块词根。',[['并列来源：古诺斯语 bolr；希腊 bōlos','前者是树干，后者是土块'],['树干：古诺斯语 → 中古英语；黏土：希腊语 → 拉丁 bolus／法语 bol','两条传播路线分别进入英语 bole，不是相互演变'],['现代语境区分','森林描写中的树干；颜料或传统镀金工艺中的黏土']],'读森林描写，a tree’s bole 就是从地面向上支撑树冠的主干。读传统工艺，red bole 可能是一种红黏土，可用于金箔下面的底层。不要为了凑词根，编成“土块长成树干”。','the bole of a tree；a massive bole；red bole。','日常说树干更常用 trunk；bole 带自然描写或林业色彩。黏土义是另一来源，和 bowl“碗”也不能混为同一词。',('Moss covered the lower part of the oak’s bole.','苔藓覆盖了橡树树干的下部。'),('The restorer applied a layer of red bole beneath the gold leaf.','修复师在金箔下面涂了一层红黏土底料。'),sources=['https://www.etymonline.com/word/bole','https://en.wiktionary.org/wiki/bole','https://www.collinsdictionary.com/dictionary/english/bole'])]
ROOT=dict(meaning='土块；团块',core='核心是一团聚拢的物质，食团和集中一份的剂量都能由此理解。',image='先想手里一小团土，再想嚼成一团的食物；医学剂量借用集中一份的概念。',intro='本组保留 bolus 与 bole 的相关义项。看起来相近的 embolism 来自“投入”词族；bole 的树干义也另有日耳曼来源，不能拼写相似就连成同一家。',forms='希腊 bōlos 进入后期拉丁 bolus，再进入英语；英语 bole 的黏土义也接这份希腊材料。',branches=[['团块与集中一份','bolus：食团、丸、一次给入的剂量'],['黏土名称','bole 的黏土义；树干义另源']],contrasts='团块 bōlos 与投入 bállein 要分清。embolism 已在 bal- 词族说明，不在这里重建错误谱系。',practice='在食物、给药记录、森林描写三个语境里，分别说明 bolus 或 bole 指什么。',sources=['https://www.merriam-webster.com/dictionary/bolus','https://www.etymonline.com/word/bole'])
m=json.loads((BASE/'.cache/batch200/rewrite_spec.json').read_text());r=next(x for x in m['roots']if x['id']==ID);c=next(x for x in json.loads((BASE/'.cache/catalog.json').read_text())if x['id']==ID);keep={w['word']for w in W}|set(SHARED);excluded={w:EXCLUDE_REASON for w in(set(r['family'])|set(c['family'])|set(c.get('unmatched',[])))-keep}
ROOT['id']=ID;ROOT['words']=list(dict.fromkeys([w for w in r['family']if w in keep]+[w for w in SHARED if w not in r['family']]));ROOT['exclude']=excluded
assert all(w['word']in m['owned_words']for w in W)
assert not(set(c['family'])|set(c.get('unmatched',[])))-set(ROOT['words'])-set(excluded)
assert {w['word']for w in W}<=set(ROOT['words'])
for w in W:assert len(w['examples'])>=2 and all(len(n)==2 and all(isinstance(x,str)and x for x in n)for n in w['history'])
for k,d in [('roots',[ROOT]),('words',W)]: (OUT/f'{k}_batch200_spec_{TAG}.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
print(ID,len(W),'new,',len(SHARED),'shared')
