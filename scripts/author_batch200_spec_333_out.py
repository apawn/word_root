# coding: utf-8
from pathlib import Path
import json
from author_batch200_spec_333_out_a import W as A
from author_batch200_spec_333_out_b import W as B
BASE=Path(__file__).resolve().parents[1];OUT=BASE/'.cache/batch200/drafts/rewrite_spec'
ID='B3570';TAG='333_out';SHARED=['outgoing','timeout','outnumber','outperform','outsource','outdo'];EXCLUDE_REASON='暂略连字符复合项；but 以连词用法为主，按当前范围不展开；wideout 是细分体育位置，freakout 为本轮暂略的边缘口语名词。'
W=A+B
ROOT=dict(meaning='向外、在外；超过；显露或到达结果',core='先画出里面和外面的边界，再看动作是在跨出、超过，还是完全显露。',image='走出房门、伸向外面、跑过对手；也可以是流程最终送出的结果。',intro='out 继承古英语 ūt、ūte，是英语自己的日耳曼语材料。outside、outdoor 等保留空间意义；outweigh、outlast 等用来比较；output、outcome 等把目光带到产出或结果。about、outer、utmost 保留更早的组合或语法变化，不能完全照现代拼写拆。',forms='out /aʊt/；旧形式另留在 utmost /ˈʌtməʊst/ 中。outward／outwards／outwardly 用法不同；outdoor 是形容词，outdoors 常作副词或名词。',branches=[['外部、方向和范围','out；about；outside；throughout；outer；outward；outwards；outwardly；outbound；utmost'],['户外、外围及地点','outdoor；outdoors；outback；outing；outskirts；outsider；hangout；hideout；cookout；outbuilding'],['结果、显露与表达','output；outcome；outlook；outline；outright；fallout；outbreak；outage；outlet；outfit；outreach；outspoken'],['超过、偏离与状态','outstanding；outlier；outdated；outlaw；outweigh；outlast；outgrow；outnumber；outperform；outdo；outsource；outgoing；timeout']],contrasts='out 的意义要与具体搭配一起看。outstanding 可以是杰出，也可以是未完成；output 是产出，outcome 是结果。outlaw 经斯堪的纳维亚语借入，outbound 的 bound 接“准备、前往”一支，不是把人绑在外面。',practice='想出四个场景：走到室外、比别人坚持更久、程序吐出结果、旧问题还未解决。分别用 outdoors、outlast、output、outstanding 描述。',sources=['https://www.etymonline.com/word/out','https://www.etymonline.com/word/about','https://www.etymonline.com/word/utmost','https://www.etymonline.com/word/outlaw','https://www.etymonline.com/word/outstanding'])
m=json.loads((BASE/'.cache/batch200/rewrite_spec.json').read_text());r=next(x for x in m['roots']if x['id']==ID);c=next(x for x in json.loads((BASE/'.cache/catalog.json').read_text())if x['id']==ID);keep={w['word']for w in W}|set(SHARED);excluded={w:EXCLUDE_REASON for w in(set(r['family'])|set(c['family'])|set(c.get('unmatched',[])))-keep}
for w in excluded:
 if '-' in w:excluded[w]='按用户要求暂略连字符复合词条。'
 elif w=='but':excluded[w]='以连词学习为主，按用户当前要求暂略；真实词源与古英语 būtan 及外部、排除义有关，并非误归。'
 elif w=='wideout':excluded[w]='暂略美式橄榄球细分球员位置名称。'
 elif w=='freakout':excluded[w]='暂略较边缘的口语名词及常见连字符变体。'
ROOT['id']=ID;ROOT['words']=list(dict.fromkeys([w for w in r['family']if w in keep]+[w for w in SHARED if w not in r['family']]));ROOT['exclude']=excluded
assert len(W)==39
assert all(w['word']in m['owned_words']for w in W)
assert not(set(c['family'])|set(c.get('unmatched',[])))-set(ROOT['words'])-set(excluded)
assert {w['word']for w in W}<=set(ROOT['words'])
for w in W:assert len(w['examples'])>=2 and all(len(n)==2 and all(isinstance(x,str)and x for x in n)for n in w['history'])
for k,d in [('roots',[ROOT]),('words',W)]: (OUT/f'{k}_batch200_spec_{TAG}.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
print(ID,len(W),'new,',len(SHARED),'shared,',sum(len(w['examples'])for w in W),'examples')
