# -*- coding: utf-8 -*-
from pathlib import Path
import json
BASE=Path(__file__).resolve().parents[1];OUT=BASE/'.cache/batch200/drafts/rewrite_spec'
m=json.loads((BASE/'.cache/batch200/rewrite_spec.json').read_text());r=next(x for x in m['roots']if x['id']=='C1220');c=next(x for x in json.loads((BASE/'.cache/catalog.json').read_text())if x['id']=='C1220');keep={'hemorrhage','haemorrhage','hemorrhagic'};excluded={w:'按用户当前范围暂略：更细分出血疾病名称、罕见植物学或撕裂病理术语。'for w in(set(r['family'])|set(c['family'])|set(c.get('unmatched',[])))-keep}
ROOT=[dict(id='C1220',meaning='破裂；撕开',core='rhag-/rheg- 的动作是冲破、裂开，像原本封闭的地方出现了缺口。',image='与“血”组合，变成血从血管里流出的 hemorrhage；比喻中又可变成钱、员工的大量流失。',intro='通用阅读最值得掌握的是 hemorrhage 及其英式拼写 haemorrhage。前半 hem-/haem- 表示血，后半保留“破开、涌出”的历史形象；合起来才是出血，单独 rhag- 并不表示血。',forms='希腊 rhēgnynai“破裂”与 rhagē“裂开、缺口”相关；医学复合词常见 -rrhage、-rrhagia，双 r 与古典构词和拼写有关。',branches=[['出血与大量流失','hemorrhage、haemorrhage'],['出血相关的性质','hemorrhagic']],contrasts='hemorrhage 不能拆成英语 hem 加 rage“愤怒”；它也不同于 hematoma“血肿”，后者强调局部积聚的血。',practice='先说明 hemorrhage 的“血”和“破裂”分别在哪里，再解释 a company hemorrhaging cash 为什么表示企业大量流失现金。',words=['hemorrhage','haemorrhage','hemorrhagic'],exclude=excluded,sources=['https://www.etymonline.com/word/hemorrhage','https://www.merriam-webster.com/dictionary/hemorrhagic'])]
assert not(set(c['family'])|set(c.get('unmatched',[])))-set(ROOT[0]['words'])-set(excluded)
for k,d in [('roots',ROOT),('words',[])]: (OUT/f'{k}_batch200_spec_235_rhag.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
print('C1220 0 new, 3 shared')
