# coding: utf-8
from pathlib import Path
import json
from lesson_authoring import entry as E
BASE=Path(__file__).resolve().parents[1];OUT=BASE/'.cache/batch200/drafts/rewrite_spec'
ID='C0193';TAG='296_cen';SHARED=[];EXCLUDE_REASON='按当前通用阅读范围暂略细分基督教神学概念。'
W=[E('cenotaph','英 /ˈsenətɑːf/；美 /ˈsenətæf/','衣冠冢式纪念碑；纪念死者的空墓','这里留着纪念的位置，死者的遗体却不在里面。','希腊 kenos“空”＋ taphos“墓”组成 kenotaphion，经后期拉丁 cenotaphium、法语 cénotaphe 传入英语。中文“衣冠冢”有助记忆，但这个英语词不要求里面真的放着衣冠。',[['希腊 kenos〔空〕＋ taphos〔墓〕→ kenotaphion','空墓'],['后期拉丁 cenotaphium → 法语 cénotaphe → 英语 cenotaph','为葬在别处或遗体未寻获的死者而建的纪念物']],'纪念战死者的 cenotaph 可以让人献花、默哀，但不是说那些人都埋在碑下。它的重点是“纪念在这里，遗体不在这里”，所以外观像墓或碑，都不改变这个核心区别。','lay a wreath at a cenotaph；a war cenotaph；gather around the cenotaph。','tomb 通常是实际安葬遗体的墓；cenotaph 是空墓式纪念物。memorial 范围更广，不一定采用墓碑形式。',('Residents laid wreaths at the cenotaph in the town square.','居民们在镇广场的阵亡者纪念碑前敬献花圈。'),('The guide explained that no one was buried beneath the cenotaph.','导游解释说，这座纪念碑下面并没有安葬任何人。'),sources=['https://www.etymonline.com/word/cenotaph','https://www.oxfordlearnersdictionaries.com/definition/english/cenotaph'])]
ROOT=dict(meaning='空的',core='cen- 在这里表示里面没有所纪念之人的遗体。',image='一座供人献花的墓形纪念物，遗体却在别处。',intro='这一组来自希腊 kenos“空”。最值得在历史、纪念活动报道里认识的是 cenotaph，字面“空墓”，实际强调纪念与安葬地点分开。',forms='希腊 k 在部分经拉丁传入的词里写为 c；cenotaph 开头读 /sen/，不读 /ken/。',branches=[['纪念与安葬分开','cenotaph']],contrasts='cen- 不是 cent-“百”；也不能把所有以 cen 开头的词都解释成空。',practice='用一句话说明为什么人们可以在 cenotaph 前献花，而死者却不葬在那里。',sources=['https://www.etymonline.com/word/cenotaph'])
m=json.loads((BASE/'.cache/batch200/rewrite_spec.json').read_text());r=next(x for x in m['roots']if x['id']==ID);c=next(x for x in json.loads((BASE/'.cache/catalog.json').read_text())if x['id']==ID);keep={w['word']for w in W}|set(SHARED);excluded={w:EXCLUDE_REASON for w in(set(r['family'])|set(c['family'])|set(c.get('unmatched',[])))-keep}
ROOT['id']=ID;ROOT['words']=list(dict.fromkeys([w for w in r['family']if w in keep]+[w for w in SHARED if w not in r['family']]));ROOT['exclude']=excluded
assert all(w['word']in m['owned_words']for w in W)
assert not(set(c['family'])|set(c.get('unmatched',[])))-set(ROOT['words'])-set(excluded)
assert {w['word']for w in W}<=set(ROOT['words'])
for w in W:assert len(w['examples'])>=2 and all(len(n)==2 and all(isinstance(x,str)and x for x in n)for n in w['history'])
for k,d in [('roots',[ROOT]),('words',W)]: (OUT/f'{k}_batch200_spec_{TAG}.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
print(ID,len(W),'new,',len(SHARED),'shared')
