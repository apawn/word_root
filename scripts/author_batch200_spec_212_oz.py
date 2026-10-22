# -*- coding: utf-8 -*-
from pathlib import Path
import json
from lesson_authoring import entry as E
BASE=Path(__file__).resolve().parents[1];OUT=BASE/'.cache/batch200/drafts/rewrite_spec'
W=[E('ozone','英 /ˈəʊzəʊn/；美 /ˈoʊzoʊn/','臭氧','名字抓住的是气味，现代讨论重点则是它处在大气的什么位置。','借德语 Ozon，由化学家 Schönbein 在 1840 年据希腊 ozein“发出气味”及分词 ozon 造词，以这种气体的刺激性气味命名。不要拆成字母 O 加英语 zone“区域”。',[['希腊 ozein / ozon','发出气味／有气味的'],['德语 Ozon','1840 年用气味特征命名这种气体'],['英语 ozone','臭氧；分子含三个氧原子']],'臭氧是 O₃，通常说的氧气是 O₂。高空平流层中的臭氧有助于吸收有害紫外线；近地面的臭氧却属于空气污染物。“保护臭氧层”和“减少臭氧污染”谈的是不同位置，并不矛盾。旧式海滨描写里 ozone 还可能泛指清新空气，不能当作现代化学判断。','the ozone layer；ozone depletion；ozone pollution；ozone levels。','ozone 与 oxygen 含同一种元素，但分子组成不同；它们的名称也分别从“气味”和“酸的产生”两条命名思路而来。',('The lesson explains why the ozone layer matters to life on Earth.','这堂课解释了臭氧层为什么对地球生命重要。'),('The report separates ozone pollution near the ground from ozone in the upper atmosphere.','报告区分了近地面的臭氧污染和高层大气中的臭氧。'),sources=['https://www.etymonline.com/word/ozone','https://www.oxfordlearnersdictionaries.com/definition/english/ozone','https://www.epa.gov/ground-level-ozone-pollution/ground-level-ozone-basics','https://en.wiktionary.org/wiki/ozone'])]
m=json.loads((BASE/'.cache/batch200/rewrite_spec.json').read_text());r=next(x for x in m['roots']if x['id']=='C0936');c=next(x for x in json.loads((BASE/'.cache/catalog.json').read_text())if x['id']=='C0936');keep={'ozone'};excluded={w:'按用户当前范围暂略：少见矿物名或动物结构术语，保留常见的臭氧词。'for w in(set(r['family'])|set(c['family'])|set(c.get('unmatched',[])))-keep}
ROOT=[dict(id='C0936',meaning='气味；发出气味',core='oz- 的原始线索是鼻子能闻到的气味。',image='先凭刺激性气味命名，再成为环境与大气科学中的常用词。',intro='这一小根最值得掌握的是 ozone。它保留了科学家当初命名时观察到的特征，却不意味着现代所有用法都在讨论气味。',forms='希腊 ozein“发出气味”、分词 ozon → 德语 Ozon → 英语 ozone。',branches=[['气味命名到大气科学','ozone']],contrasts='ozone 不是 O + zone。高空臭氧层与近地面臭氧污染的作用不同，阅读时先看位置。',practice='用两句话分别说明 ozone layer 和 ozone pollution，避免把二者混成同一环境问题。',words=['ozone'],exclude=excluded,sources=['https://www.etymonline.com/word/ozone'])]
assert all(w['word']in m['owned_words']for w in W)
assert not(set(c['family'])|set(c.get('unmatched',[])))-set(ROOT[0]['words'])-set(excluded)
for k,d in [('roots',ROOT),('words',W)]: (OUT/f'{k}_batch200_spec_212_oz.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
print('C0936',len(W),'new')
