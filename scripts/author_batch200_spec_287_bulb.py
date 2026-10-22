# coding: utf-8
from pathlib import Path
import json
from lesson_authoring import entry as E
BASE=Path(__file__).resolve().parents[1];OUT=BASE/'.cache/batch200/drafts/rewrite_spec'
ID='C0146';TAG='287_bulb';SHARED=[];EXCLUDE_REASON='按当前范围暂略罕见形状派生及生殖、解剖细分术语。'
B=[['希腊 bolbós → 拉丁 bulbus','植物地下圆鼓鼓的部分；洋葱、鳞茎']]
W=[E('bulb','/bʌlb/','鳞茎；球茎状部分；灯泡','先想一颗圆鼓鼓的洋葱，再把外形联想到灯泡。','经法语 bulbe 或拉丁 bulbus 传入，远接希腊 bolbós。现代英语里作为整体词使用。',B+[['法语 bulbe／拉丁 bulbus → 英语 bulb','洋葱、植物鳞茎'],['英语按外形扩展','圆鼓的部分；玻璃泡；灯泡']],'植物的 bulb 是储存养分的结构，洋葱、郁金香都有典型鳞茎；它不是种子，也不能把所有地下块状器官都叫 bulb。灯泡和滴管上可挤压的橡胶球，则借用了圆鼓外形。','a tulip bulb；plant bulbs；replace a bulb；a rubber bulb。','seed 是种子；bulb 是已有植物组织形成的储藏结构。灯具是 lamp，里面可替换的发光部件可以叫 bulb。',('She planted tulip bulbs along the path.','她沿着小路种下了郁金香鳞茎。'),('The lamp needs a new bulb.','这盏灯需要换一个新灯泡。'),sources=['https://www.etymonline.com/word/bulb','https://en.wiktionary.org/wiki/bulb','https://www.oxfordlearnersdictionaries.com/definition/english/bulb','https://www.rhs.org.uk/plants/types/bulbs']),
E('bulbous','/ˈbʌlbəs/','圆鼓鼓的；鳞茎状的；有鳞茎的','一处明显鼓起来，像洋葱或灯泡那样圆而饱满。','可接拉丁 bulbōsus，也有英语 bulb + -ous 的派生分析；不是所有词典都把它只当英语内部新造词。',B+[['拉丁 bulbōsus；或英语 bulb + -ous','有鳞茎的、像鳞茎的两种构词分析'],['英语 bulbous','后来广泛形容圆鼓外形']],'a bulbous vase 是肚子圆鼓的花瓶；a bulbous nose 描写圆大突出的鼻子，通常不算赞美。植物学里的 bulbous plants 则可以只是客观地说植物有鳞茎。','a bulbous nose；a bulbous shape；bulbous plants。','round 只说圆，bulbous 更强调某处膨大、鼓出；不是所有圆形物都适合这样形容。',('The glass vase has a narrow neck and a bulbous base.','玻璃花瓶的颈部细长，底部圆鼓。'),('The garden includes several bulbous plants that flower in spring.','花园里有几种春天开花的鳞茎植物。'),sources=['https://www.etymonline.com/word/bulbous','https://www.oxfordlearnersdictionaries.com/definition/english/bulbous'])]
ROOT=dict(meaning='鳞茎；圆鼓的部分',core='抓住洋葱式的圆鼓外形，再区分植物结构与借形命名的物件。',image='洋葱的圆鼓部分，联想到灯泡、滴管橡胶球和鼓肚花瓶。',intro='bulb 的旧名称来自植物地下膨大的部分，后来按外形用于玻璃泡和灯泡。bulbous 则把这种圆鼓形状变成形容词。',forms='希腊 bolbós → 拉丁 bulbus，之后经拉丁或法语进入英语。bulbous 有拉丁形容词借入和英语派生两种分析。',branches=[['具体物件和结构','bulb：鳞茎；灯泡；圆鼓部分'],['外形与性质','bulbous：圆鼓的；有鳞茎的']],contrasts='植物的 bulb 不是 seed；球形的 potato tuber 也不因圆就成为严格植物学意义的 bulb。',practice='用“圆鼓”解释灯泡与鳞茎为何共用 bulb，再记住它们不是同一种物体。',sources=['https://www.etymonline.com/word/bulb','https://www.etymonline.com/word/bulbous'])
m=json.loads((BASE/'.cache/batch200/rewrite_spec.json').read_text());r=next(x for x in m['roots']if x['id']==ID);c=next(x for x in json.loads((BASE/'.cache/catalog.json').read_text())if x['id']==ID);keep={w['word']for w in W}|set(SHARED);excluded={w:EXCLUDE_REASON for w in(set(r['family'])|set(c['family'])|set(c.get('unmatched',[])))-keep}
ROOT['id']=ID;ROOT['words']=list(dict.fromkeys([w for w in r['family']if w in keep]+[w for w in SHARED if w not in r['family']]));ROOT['exclude']=excluded
assert all(w['word']in m['owned_words']for w in W)
assert not(set(c['family'])|set(c.get('unmatched',[])))-set(ROOT['words'])-set(excluded)
assert {w['word']for w in W}<=set(ROOT['words'])
for w in W:assert len(w['examples'])>=2 and all(len(n)==2 and all(isinstance(x,str)and x for x in n)for n in w['history'])
for k,d in [('roots',[ROOT]),('words',W)]: (OUT/f'{k}_batch200_spec_{TAG}.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
print(ID,len(W),'new,',len(SHARED),'shared')
