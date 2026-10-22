# coding: utf-8
from pathlib import Path
import json
from lesson_authoring import entry as E
BASE=Path(__file__).resolve().parents[1];OUT=BASE/'.cache/batch200/drafts/rewrite_spec'
ID='C0783';TAG='312_myo';SHARED=['muscle','muscular','myopathy','myositis','electromyography','electromyogram','cardiomyopathy','amyotrophic'];EXCLUDE_REASON='暂略罕见肌肉细分术语。'
W=[E('leiomyoma','美 /ˌlaɪoʊmaɪˈoʊmə/','平滑肌瘤','由平滑肌组织形成的良性肿瘤。','leio-〔平滑〕＋ myo-〔肌肉〕＋ -oma〔肿块、肿瘤〕；也可分 leio-＋myoma。是近代医学利用希腊材料组成的名称。',[['希腊 leîos；mŷs；-ōma','平滑；肌肉；肿块名称成分'],['近代医学构词 leiomyoma','平滑肌组织形成的肿瘤名称'],['英语 leiomyoma','平滑肌瘤；常见于子宫等部位']],'“平滑”说的是肌肉类别，不是医生摸到的表面手感。子宫肌瘤常属于这一类，因此一般健康阅读里可能先遇到 fibroid，再在更专业的说明里看到 leiomyoma。这个名称指良性肿瘤，不要一见 -oma 就译成癌。','a uterine leiomyoma；a benign leiomyoma；leiomyomas。','myoma 泛指肌瘤，leio- 进一步限定为平滑肌；-oma 是肿瘤成分，不能单靠它判断良恶性。',('The report describes the mass as a uterine leiomyoma.','报告把该肿块描述为子宫平滑肌瘤。'),('The textbook identifies leiomyoma as a benign smooth muscle tumour.','教科书指出，平滑肌瘤是良性平滑肌肿瘤。'),sources=['https://en.wiktionary.org/wiki/leiomyoma','https://www.merriam-webster.com/medical/leiomyoma','https://www.cancer.gov/publications/dictionaries/cancer-terms/def/leiomyoma'])]
ROOT=dict(meaning='肌肉',core='myo-：先把它替换成“肌肉”，再看后面的成分在说疾病、记录还是肿瘤。',image='肌肉是主体，后接的成分分别标出病变、炎症、记录或组织增生。',intro='希腊 mŷs 既曾指鼠，也指肌肉；现代医学 myo- 主要用肌肉义。这里把基本肌肉词和常见医学组合放在一起，muscle／muscular 是相关的拉丁来源词，供对照，不是 myo- 在英语里直接变出来的。',forms='myo- 接辅音成分时常保留 o；myopathy 的拼写和重音要整体记；myositis 的 s 来自沿用的构形，不另赋新义。',branches=[['日常肌肉表达','muscle；muscular'],['疾病及相关描述','myopathy；myositis；cardiomyopathy；amyotrophic'],['记录肌肉活动','electromyography；electromyogram'],['按组织命名的肿瘤','leiomyoma']],contrasts='肌病 myopathy 是较宽的类别，肌炎 myositis 点出炎症；myo- 只标肌肉，不会独自说明原因。',practice='把 electromyogram 拆成“电＋肌肉＋记录”，把 leiomyoma 拆成“平滑＋肌肉＋肿瘤”。',sources=['https://www.etymonline.com/word/muscle','https://www.merriam-webster.com/dictionary/myopathy','https://www.cancer.gov/publications/dictionaries/cancer-terms/def/leiomyoma'])
m=json.loads((BASE/'.cache/batch200/rewrite_spec.json').read_text());r=next(x for x in m['roots']if x['id']==ID);c=next(x for x in json.loads((BASE/'.cache/catalog.json').read_text())if x['id']==ID);keep={w['word']for w in W}|set(SHARED);excluded={w:EXCLUDE_REASON for w in(set(r['family'])|set(c['family'])|set(c.get('unmatched',[])))-keep}
ROOT['id']=ID;ROOT['words']=list(dict.fromkeys([w for w in r['family']if w in keep]+[w for w in SHARED if w not in r['family']]));ROOT['exclude']=excluded
assert all(w['word']in m['owned_words']for w in W)
assert not(set(c['family'])|set(c.get('unmatched',[])))-set(ROOT['words'])-set(excluded)
assert {w['word']for w in W}<=set(ROOT['words'])
for w in W:assert len(w['examples'])>=2 and all(len(n)==2 and all(isinstance(x,str)and x for x in n)for n in w['history'])
for k,d in [('roots',[ROOT]),('words',W)]: (OUT/f'{k}_batch200_spec_{TAG}.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
print(ID,len(W),'new,',len(SHARED),'shared')
