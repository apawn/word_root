# coding: utf-8
from pathlib import Path
import json
from lesson_authoring import entry as E
BASE=Path(__file__).resolve().parents[1];OUT=BASE/'.cache/batch200/drafts/rewrite_spec'
ID='C1613';TAG='281_ven';SHARED=[];EXCLUDE_REASON='按当前常用词范围暂略罕见狩猎旧词。'
W=[E('venison','/ˈvenɪsən/，也读 /ˈvenɪzən/','鹿肉','菜单上说的是肉，不是活着的鹿。','从古法语 venesoun／venoison 借入，接拉丁 vēnātiō 猎取、猎物，再接 vēnārī 打猎。不要把末尾拆成 son“儿子”。',[['拉丁 vēnārī → vēnātiō','打猎 → 狩猎活动及猎获之物'],['古法语 venesoun／venoison → 中古英语 venisoun','大型猎物的肉'],['现代英语 venison','常用范围缩到鹿肉']],'这条变化很具体：先说“打猎”，再说“打猎所得的肉”，后来主要指鹿肉。今天养殖鹿的肉也可叫 venison，不要求那块肉真的来自一次野外狩猎。','roast venison；venison stew；a venison steak；通常不可数。','deer 是动物，venison 是肉；game 作肉食名称时范围更大，可以包括其他猎物。',('The restaurant serves venison with roasted vegetables.','这家餐馆把鹿肉配烤蔬菜一起上桌。'),('She bought some venison for a winter stew.','她买了些鹿肉，准备做冬天吃的炖菜。'),sources=['https://www.etymonline.com/word/venison','https://www.oxfordlearnersdictionaries.com/definition/english/venison','https://en.wiktionary.org/wiki/venison'])]
ROOT=dict(meaning='打猎；追猎',core='从打猎的动作，转向打猎获得的肉。',image='猎人追逐猎物，后来餐桌上出现猎获的肉；名称最终主要留下鹿肉这个意思。',intro='这支 ven- 来自拉丁 vēnārī“打猎”，最实用的后代是菜单上的 venison。掌握这一个词，便能看见“行为 → 行为所得之物 → 特定食物”的变化。',forms='vēnārī → vēnātiō，再经法语及英语的发音、拼写变化成为 venison。不能凭 ven- 三个字母把所有近形词都塞进来。',branches=[['狩猎所得的肉','venison：现代通常指鹿肉']],contrasts='这不是来自 venīre“来”的那支 ven-，也不能把 vein“静脉”按此解释。',practice='在菜单中把 deer 与 venison 分别理解为动物名和肉名。',sources=['https://www.etymonline.com/word/venison'])
m=json.loads((BASE/'.cache/batch200/rewrite_spec.json').read_text());r=next(x for x in m['roots']if x['id']==ID);c=next(x for x in json.loads((BASE/'.cache/catalog.json').read_text())if x['id']==ID);keep={w['word']for w in W}|set(SHARED);excluded={w:EXCLUDE_REASON for w in(set(r['family'])|set(c['family'])|set(c.get('unmatched',[])))-keep}
ROOT['id']=ID;ROOT['words']=list(dict.fromkeys([w for w in r['family']if w in keep]+[w for w in SHARED if w not in r['family']]));ROOT['exclude']=excluded
assert all(w['word']in m['owned_words']for w in W)
assert not(set(c['family'])|set(c.get('unmatched',[])))-set(ROOT['words'])-set(excluded)
assert {w['word']for w in W}<=set(ROOT['words'])
for w in W:assert len(w['examples'])>=2 and all(len(n)==2 and all(isinstance(x,str)and x for x in n)for n in w['history'])
for k,d in [('roots',[ROOT]),('words',W)]: (OUT/f'{k}_batch200_spec_{TAG}.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
print(ID,len(W),'new,',len(SHARED),'shared')
