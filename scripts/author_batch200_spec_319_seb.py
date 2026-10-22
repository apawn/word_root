# coding: utf-8
from pathlib import Path
import json
from lesson_authoring import entry as E
BASE=Path(__file__).resolve().parents[1];OUT=BASE/'.cache/batch200/drafts/rewrite_spec'
ID='C1294';TAG='319_seb';SHARED=[];EXCLUDE_REASON='暂略更细分的皮肤病和化学派生词。'
A='https://openstax.org/books/anatomy-and-physiology-2e/pages/5-2-accessory-structures-of-the-skin'
W=[E('sebum','/ˈsiːbəm/','皮脂','皮脂腺分泌出来、润滑皮肤和毛发的油性物质。','学术借入拉丁 sēbum〔动物脂、油脂〕，在皮肤生理学中用于这一类分泌物。',[['拉丁 sēbum','动物脂、油脂'],['英语 sebum','皮脂腺分泌物的学术名称']],'想到皮肤自然分泌的那层油，就接近这个词的意思。sebum 是含多种脂质的混合物，不是汗水，也不是皮肤下面储存的那团脂肪组织。','sebum production；excess sebum；sebum on the skin。','sweat 主要是水性汗液；sebum 是油性皮脂，两者来自不同类型的腺体。',('Sebum helps lubricate the skin and hair.','皮脂帮助润滑皮肤和毛发。'),('The study measured sebum production on the forehead.','研究测量了额头的皮脂分泌量。'),sources=['https://en.wiktionary.org/wiki/sebum',A]),
E('sebaceous','/səˈbeɪʃəs/','皮脂的；分泌皮脂的；皮脂腺的','把“皮肤的油”这个概念用来修饰腺体、分泌物等。','来自拉丁 sēbāceus〔脂制的、油脂的〕，接 sēbum〔油脂〕；英语采用 -aceous 形态。不能把历史简化成英语 sebum 后来才加出这个词。',[['拉丁 sēbum → sēbāceus','油脂 → 油脂的'],['英语 sebaceous','皮脂或皮脂腺相关的']],'最常碰见 sebaceous glands，也就是皮脂腺：负责分泌 sebum 的“小油厂”。sebaceous 说的是这种油脂及相关腺体，不等于所有“看起来油腻”的东西。','sebaceous glands；sebaceous secretions；sebaceous activity。','sebum 是分泌出来的物质，sebaceous 是形容词；sweat glands 是汗腺。',('Sebaceous glands release oil onto the skin.','皮脂腺向皮肤释放油性物质。'),('The drawing shows a sebaceous gland beside a hair follicle.','图画显示毛囊旁边的一处皮脂腺。'),sources=['https://www.merriam-webster.com/dictionary/sebaceous','https://en.wiktionary.org/wiki/sebaceous',A])]
ROOT=dict(meaning='动物脂；油脂；皮脂',core='seb- 的实用画面是皮肤自然分泌的油。',image='皮脂腺像小油厂，分泌出的油性混合物叫 sebum。',intro='拉丁 sēbum 原指动物脂、油脂。英语 sebum 把它用于皮脂；sebaceous 则接拉丁已有的形容词材料，用来描述皮脂及分泌它的腺体。',forms='sebum 是物质名词；sebaceous 是形容词。两个词在现代意义上成对，但并非必须由英语名词先造出形容词。',branches=[['分泌的物质','sebum'],['腺体与相关性质','sebaceous']],contrasts='皮脂、汗液和皮下脂肪不是三个可互换的名称。',practice='把 sebaceous glands produce sebum 翻成一句话，并指出哪一个词说腺体、哪一个词说产物。',sources=['https://www.merriam-webster.com/dictionary/sebaceous',A])
m=json.loads((BASE/'.cache/batch200/rewrite_spec.json').read_text());r=next(x for x in m['roots']if x['id']==ID);c=next(x for x in json.loads((BASE/'.cache/catalog.json').read_text())if x['id']==ID);keep={w['word']for w in W}|set(SHARED);excluded={w:EXCLUDE_REASON for w in(set(r['family'])|set(c['family'])|set(c.get('unmatched',[])))-keep}
ROOT['id']=ID;ROOT['words']=list(dict.fromkeys([w for w in r['family']if w in keep]+[w for w in SHARED if w not in r['family']]));ROOT['exclude']=excluded
assert all(w['word']in m['owned_words']for w in W)
assert not(set(c['family'])|set(c.get('unmatched',[])))-set(ROOT['words'])-set(excluded)
assert {w['word']for w in W}<=set(ROOT['words'])
for w in W:assert len(w['examples'])>=2 and all(len(n)==2 and all(isinstance(x,str)and x for x in n)for n in w['history'])
for k,d in [('roots',[ROOT]),('words',W)]: (OUT/f'{k}_batch200_spec_{TAG}.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
print(ID,len(W),'new,',len(SHARED),'shared')
