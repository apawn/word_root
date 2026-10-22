# coding: utf-8
from pathlib import Path
import json
from lesson_authoring import entry as E
BASE=Path(__file__).resolve().parents[1];OUT=BASE/'.cache/batch200/drafts/rewrite_spec'
ID='C1284';TAG='308_scoli';SHARED=[];EXCLUDE_REASON='暂略脊柱弯曲的复合细分术语，保留一般科普中最常见的基础词。'
W=[E('scoliosis','英 /ˌskəʊliˈəʊsɪs/；美 /ˌskoʊliˈoʊsɪs/','脊柱侧弯','从背后看，脊柱向身体一侧弯，而不是沿中线排列。','希腊 skoliós〔弯曲的〕形成 skolíōsis〔弯曲、扭曲〕，经拉丁进入英语。现代可按 scolio-〔弯曲〕＋ -osis〔状态〕识记，但完整名词在古语中已经存在。',[['希腊 skoliós → skolíōsis','弯曲的 → 弯曲、扭曲的状态'],['拉丁 scoliosis → 英语 scoliosis','沿用为脊柱侧弯的医学名称']],'最直观的图像是从背后看的一条中线，向左或向右弯成 C 形或 S 形。脊柱本来就有正常的前后曲线，因此这个词的重点是“向侧面弯”，不能把所有弯腰、驼背都叫 scoliosis。','have scoliosis；a case of scoliosis；scoliosis screening。','curvature 是泛指弯曲；scoliosis 限定到脊柱侧向弯曲这个概念。',('The model shows the sideways curve associated with scoliosis.','模型展示了脊柱侧弯所表现出的侧向曲线。'),('The article explains scoliosis in language that teenagers can understand.','这篇文章用青少年能理解的语言介绍脊柱侧弯。'),sources=['https://en.wiktionary.org/wiki/scoliosis','https://www.merriam-webster.com/dictionary/scoliosis','https://www.niams.nih.gov/health-topics/scoliosis'])]
ROOT=dict(meaning='弯曲；偏斜',core='scoli-／scolio-：从直线向一旁弯开。',image='从背后看，原本居中的脊柱线向一侧弯成 C 或 S。',intro='这一小组最值得认的是 scoliosis。希腊 skoliós 是“弯曲的”，进入这个医学名词后，意思具体到脊柱的侧向弯曲。用方向抓住概念，比只背“异常”两个字更清楚。',forms='scolio- 连接 -osis，形成 scoliosis；-osis 在这里标状态。',branches=[['基础医学阅读','scoliosis']],contrasts='这里要分清侧向弯曲与脊柱正常的前后曲线。scoli- 本身是弯曲，不是某一种具体病因。',practice='用一句话解释 scoliosis 中的“弯”是向哪个方向弯。',sources=['https://www.merriam-webster.com/dictionary/scoliosis','https://www.niams.nih.gov/health-topics/scoliosis'])
m=json.loads((BASE/'.cache/batch200/rewrite_spec.json').read_text());r=next(x for x in m['roots']if x['id']==ID);c=next(x for x in json.loads((BASE/'.cache/catalog.json').read_text())if x['id']==ID);keep={w['word']for w in W}|set(SHARED);excluded={w:EXCLUDE_REASON for w in(set(r['family'])|set(c['family'])|set(c.get('unmatched',[])))-keep}
ROOT['id']=ID;ROOT['words']=list(dict.fromkeys([w for w in r['family']if w in keep]+[w for w in SHARED if w not in r['family']]));ROOT['exclude']=excluded
assert all(w['word']in m['owned_words']for w in W)
assert not(set(c['family'])|set(c.get('unmatched',[])))-set(ROOT['words'])-set(excluded)
assert {w['word']for w in W}<=set(ROOT['words'])
for w in W:assert len(w['examples'])>=2 and all(len(n)==2 and all(isinstance(x,str)and x for x in n)for n in w['history'])
for k,d in [('roots',[ROOT]),('words',W)]: (OUT/f'{k}_batch200_spec_{TAG}.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
print(ID,len(W),'new,',len(SHARED),'shared')
