# coding: utf-8
from pathlib import Path
import json
from lesson_authoring import entry as E
BASE=Path(__file__).resolve().parents[1];OUT=BASE/'.cache/batch200/drafts/rewrite_spec'
ID='C0016';TAG='304_aden';SHARED=['adenoma','adenocarcinoma'];EXCLUDE_REASON='按当前基础阅读范围暂略细分疾病、手术和少用学科名称。'
W=[E('adenoid','英 /ˈædɪnɔɪd/；美 /ˈædənɔɪd/','腺样的；腺样体的；〔名词通常复数 adenoids〕腺样体','名字说“像腺”，日常最常指鼻子后方那片免疫组织。','希腊 adēn“腺”＋ -oeidēs“形似”组成 adenoeidēs，经医学拉丁，并有法语 adénoïde 中介的分析，进入英语。名词 adenoids 由腺样组织的称呼发展而来，不是所有腺体的统称。',[['希腊 adēn〔腺〕＋ -oeidēs〔形似〕→ adenoeidēs','腺样的'],['医学拉丁 adenoideus／adenoides；法语 adénoïde → 英语 adenoid','形似腺的形容词'],['英语名词 adenoids','通常指鼻咽部的腺样体组织']],'儿童健康资料常写 enlarged adenoids“腺样体肥大”。腺样体位于鼻后、咽部上方，属于淋巴组织；名字里的“腺样”描述外观，不能直接把它理解为分泌激素的腺体。','enlarged adenoids；adenoid tissue；adenoid enlargement。','adenoma 是腺瘤，adenoids 是一种正常解剖组织的名称，出现这个词不等于有肿瘤。单数 adenoid 也常放在 tissue 等名词前作定语。',('The diagram locates the adenoids behind the nose.','这幅图标出了鼻后方的腺样体。'),('The leaflet explains how enlarged adenoids can affect breathing through the nose.','宣传册解释了肥大的腺样体会怎样影响经鼻呼吸。'),sources=['https://www.etymonline.com/word/adenoid','https://en.wiktionary.org/wiki/adenoid#English','https://medlineplus.gov/adenoids.html'])]
ROOT=dict(meaning='腺；腺样组织',core='aden- 先指出组织像腺或具有腺的特征，后半部分再说明是什么情况。',image='先标出组织类型，再区分正常组织、良性生长物与癌。',intro='希腊 adēn 表示腺。adenoid 的 -oid 表示形似；adenoma 是腺瘤；adenocarcinoma 是腺癌。共享同一个前半，不代表三者是同一种东西。',forms='adēn，属格 adēnos → aden-／adeno-；adenoids 在日常健康阅读里常用复数形式指腺样体。',branches=[['正常组织及其形容词','adenoid'],['良性与恶性肿瘤名称','adenoma；adenocarcinoma']],contrasts='腺样体属于淋巴组织，名称不表示它就是一处肿瘤。adenoma 与 adenocarcinoma 也不能只凭都有 -oma 就混为一谈。',practice='用自己的话区分 adenoids、adenoma、adenocarcinoma，先说组织，再说是否为肿瘤。',sources=['https://www.etymonline.com/word/adenoid','https://medlineplus.gov/adenoids.html','https://www.cancer.gov/publications/dictionaries/cancer-terms/def/adenoma'])
m=json.loads((BASE/'.cache/batch200/rewrite_spec.json').read_text());r=next(x for x in m['roots']if x['id']==ID);c=next(x for x in json.loads((BASE/'.cache/catalog.json').read_text())if x['id']==ID);keep={w['word']for w in W}|set(SHARED);excluded={w:EXCLUDE_REASON for w in(set(r['family'])|set(c['family'])|set(c.get('unmatched',[])))-keep}
ROOT['id']=ID;ROOT['words']=list(dict.fromkeys([w for w in r['family']if w in keep]+[w for w in SHARED if w not in r['family']]));ROOT['exclude']=excluded
assert all(w['word']in m['owned_words']for w in W)
assert not(set(c['family'])|set(c.get('unmatched',[])))-set(ROOT['words'])-set(excluded)
assert {w['word']for w in W}<=set(ROOT['words'])
for w in W:assert len(w['examples'])>=2 and all(len(n)==2 and all(isinstance(x,str)and x for x in n)for n in w['history'])
for k,d in [('roots',[ROOT]),('words',W)]: (OUT/f'{k}_batch200_spec_{TAG}.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
print(ID,len(W),'new,',len(SHARED),'shared')
