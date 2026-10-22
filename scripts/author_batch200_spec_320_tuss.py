# coding: utf-8
from pathlib import Path
import json
from lesson_authoring import entry as E
BASE=Path(__file__).resolve().parents[1];OUT=BASE/'.cache/batch200/drafts/rewrite_spec'
ID='C1566';TAG='320_tuss';SHARED=[];EXCLUDE_REASON='暂略不常单独使用的 tussive，保留常见病名与药物作用词。'
W=[E('pertussis','英 /pəˈtʌsɪs/；美 /pərˈtʌsɪs/','百日咳','通常也叫 whooping cough 的一种细菌性呼吸道感染。','借新拉丁 pertussis：拉丁 per-〔加强语气〕＋ tussis〔咳嗽〕。名称抓住强烈咳嗽的表现，现代却是一个具体疾病名。',[['拉丁 per-；tussis','加强；咳嗽：并列材料'],['新拉丁 pertussis','由强烈咳嗽画面形成病名'],['英语 pertussis','百日咳']],'看到 per-＋tussis 可以记住“咳得厉害”的命名画面，但不能把所有严重咳嗽都叫 pertussis。它在公共卫生报道中指百日咳这种感染，通俗英语名称是 whooping cough。','pertussis cases；a pertussis outbreak；pertussis vaccination。','cough 是症状或动作，pertussis 是具体疾病；中文名也不要求每次病程都恰好一百天。',('The report lists the number of pertussis cases recorded that year.','报告列出了当年记录的百日咳病例数。'),('The leaflet explains that pertussis is another name for whooping cough.','传单解释说，pertussis 是 whooping cough 的另一名称。'),sources=['https://www.merriam-webster.com/dictionary/pertussis','https://en.wiktionary.org/wiki/pertussis','https://www.cdc.gov/pertussis/about/index.html']),
E('antitussive','/ˌæntiˈtʌsɪv/，也读 /ˌæntaɪˈtʌsɪv/','镇咳的；镇咳药','作用是抑制咳嗽。','anti-〔对抗〕＋ tussive〔咳嗽相关的〕；tussive 接拉丁 tussis〔咳嗽〕和形容词词尾 -ive。这是现代组合，不是完整古拉丁词直接借入。',[['拉丁 tussis','咳嗽'],['英语 tussive','咳嗽相关的'],['anti- ＋ tussive → antitussive','镇咳的；作名词指镇咳药']],'把 anti- 看成朝相反方向用力：咳嗽想发生，antitussive 的作用是压低它。它说的是作用类别，不等于“消除一切引起咳嗽的原因”，也不是某一个药品的专名。','an antitussive；antitussive effects；an antitussive medicine。','expectorant 指帮助排痰的药物或作用；antitussive 指抑制咳嗽，两个词描述的功能不同。',('The label describes the ingredient as an antitussive.','标签把这种成分列为镇咳成分。'),('The paper compares antitussive and expectorant effects.','论文比较了镇咳作用与祛痰作用。'),sources=['https://www.merriam-webster.com/dictionary/antitussive','https://en.wiktionary.org/wiki/antitussive'])]
ROOT=dict(meaning='咳嗽',core='tuss- 抓住“咳”这个动作。',image='前面加不同材料，或成为某个疾病名，或表示抑制咳嗽的作用。',intro='拉丁 tussis 是咳嗽。pertussis 借新拉丁疾病名称进入英语；antitussive 则用 anti- 把意思转成镇咳。词根帮助认方向，整个词决定是在说病名还是作用。',forms='tuss- 出现在 pertussis；tussive 是相关形容词材料，组成 antitussive。',branches=[['具体疾病名称','pertussis'],['抑制咳嗽的作用','antitussive']],contrasts='pertussis 不等于任意咳嗽；antitussive 不等于抗感染或祛痰。',practice='区分 a pertussis outbreak 与 an antitussive ingredient，说明哪一个是疾病、哪一个是作用分类。',sources=['https://www.merriam-webster.com/dictionary/pertussis','https://www.merriam-webster.com/dictionary/antitussive'])
m=json.loads((BASE/'.cache/batch200/rewrite_spec.json').read_text());r=next(x for x in m['roots']if x['id']==ID);c=next(x for x in json.loads((BASE/'.cache/catalog.json').read_text())if x['id']==ID);keep={w['word']for w in W}|set(SHARED);excluded={w:EXCLUDE_REASON for w in(set(r['family'])|set(c['family'])|set(c.get('unmatched',[])))-keep}
ROOT['id']=ID;ROOT['words']=list(dict.fromkeys([w for w in r['family']if w in keep]+[w for w in SHARED if w not in r['family']]));ROOT['exclude']=excluded
assert all(w['word']in m['owned_words']for w in W)
assert not(set(c['family'])|set(c.get('unmatched',[])))-set(ROOT['words'])-set(excluded)
assert {w['word']for w in W}<=set(ROOT['words'])
for w in W:assert len(w['examples'])>=2 and all(len(n)==2 and all(isinstance(x,str)and x for x in n)for n in w['history'])
for k,d in [('roots',[ROOT]),('words',W)]: (OUT/f'{k}_batch200_spec_{TAG}.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
print(ID,len(W),'new,',len(SHARED),'shared')
