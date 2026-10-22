# coding: utf-8
from pathlib import Path
import json
from lesson_authoring import entry as E
BASE=Path(__file__).resolve().parents[1];OUT=BASE/'.cache/batch200/drafts/rewrite_spec'
ID='C0017';TAG='303_adip';SHARED=[];EXCLUDE_REASON='按当前基础科普范围暂略冷门组织学组合形容词。'
W=[E('adipose','英 /ˈædɪpəʊs/；美 /ˈædɪpoʊs/','脂肪的；脂肪组织的','把身体里的脂肪看成一种有细胞、有功能的组织。','借自新拉丁 adiposus，来自拉丁 adeps，属格 adipis“脂肪”。现代可认 adip- 和形容词结尾 -ose；这里的 -ose 不像 glucose 那样表示糖名。',[['拉丁 adeps，属格 adipis','动物脂肪'],['新拉丁 adiposus → 英语 adipose','脂肪的；脂肪组织的']],'最常见搭配是 adipose tissue“脂肪组织”，主要由储存脂质的脂肪细胞组成。它不是一袋没有生命的油，也不等于“这个人太胖”：这个形容词首先是在辨认组织种类。','adipose tissue；adipose cells；subcutaneous adipose tissue。','fat 是日常用词，adipose 是正式的组织描述。adipose tissue 与 muscle tissue 是不同组织，不是给一个人的外形贴标签。',('The sample contained both muscle and adipose tissue.','样本里同时有肌肉组织和脂肪组织。'),('The diagram shows a layer of adipose tissue beneath the skin.','图中显示皮肤下方有一层脂肪组织。'),sources=['https://www.etymonline.com/word/adipose','https://en.wiktionary.org/wiki/adipose#English','https://evsexplore.semantics.cancer.gov/evsexplore/concept/ncit/C12472'])]
ROOT=dict(meaning='脂肪',core='adip- 指脂肪，最实用的搭配是 adipose tissue。',image='在显微镜下，脂肪是一群细胞组成的组织，不是一袋游离的油。',intro='拉丁 adeps 的属格 adipis 提供了 adip- 形式。新拉丁 adiposus 传入英语成为 adipose，常用于身体组织的客观描述。',forms='adeps／adipis → adip-；adipose 中 -ose 形成形容词，不表示糖。',branches=[['脂肪组织','adipose']],contrasts='adipose 与 glucose 虽都以 -ose 结尾，但词尾在两类词里的历史和作用不同，不能套一个解释。',practice='把 adipose tissue 和 muscle tissue 放在同一句里，说明它们是不同的组织。',sources=['https://www.etymonline.com/word/adipose','https://evsexplore.semantics.cancer.gov/evsexplore/concept/ncit/C12472'])
m=json.loads((BASE/'.cache/batch200/rewrite_spec.json').read_text());r=next(x for x in m['roots']if x['id']==ID);c=next(x for x in json.loads((BASE/'.cache/catalog.json').read_text())if x['id']==ID);keep={w['word']for w in W}|set(SHARED);excluded={w:EXCLUDE_REASON for w in(set(r['family'])|set(c['family'])|set(c.get('unmatched',[])))-keep}
ROOT['id']=ID;ROOT['words']=list(dict.fromkeys([w for w in r['family']if w in keep]+[w for w in SHARED if w not in r['family']]));ROOT['exclude']=excluded
assert all(w['word']in m['owned_words']for w in W)
assert not(set(c['family'])|set(c.get('unmatched',[])))-set(ROOT['words'])-set(excluded)
assert {w['word']for w in W}<=set(ROOT['words'])
for w in W:assert len(w['examples'])>=2 and all(len(n)==2 and all(isinstance(x,str)and x for x in n)for n in w['history'])
for k,d in [('roots',[ROOT]),('words',W)]: (OUT/f'{k}_batch200_spec_{TAG}.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
print(ID,len(W),'new,',len(SHARED),'shared')
