# coding: utf-8
from pathlib import Path
import json
from lesson_authoring import entry as E
BASE=Path(__file__).resolve().parents[1];OUT=BASE/'.cache/batch200/drafts/rewrite_spec'
ID='C1370';TAG='327_sopor';SHARED=[];EXCLUDE_REASON='暂略专业、少用的深睡或昏睡名词 sopor，保留常见阅读形容词。'
W=[E('soporific','英 /ˌsɒpəˈrɪfɪk/；美 /ˌsɑːpəˈrɪfɪk/','催眠的；令人昏昏欲睡的','让眼皮慢慢变重，注意力撑不住。','借法语 soporifique，取拉丁 sopor〔深睡〕加表示产生作用的 -fique 材料；英语形式对应 -fic。不是 sober“清醒的”的派生。',[['拉丁 sopor；产生、使成的 -fic 材料','深睡；造成某种效果'],['法语 soporifique','使人入睡的'],['英语 soporific','催眠的；也形容乏味得让人想睡']],'药物或声音可以有 soporific effect；演讲也可以 soporific，常是在说讲得太单调，让人直打瞌睡。它描述的是“令人睡”的效果，不等于讲的人自己睡着了。','a soporific effect；a soporific lecture；soporific music。','sleepy 常说人困了；soporific 说什么东西让人困。宁静的声音也可能 soporific，不必全是负面。',('The speaker’s flat delivery had a soporific effect on the audience.','演讲者平板的讲述让听众昏昏欲睡。'),('The gentle rocking of the train was pleasantly soporific.','火车轻轻的摇晃让人舒服得直想睡。'),sources=['https://www.etymonline.com/word/soporific','https://en.wiktionary.org/wiki/soporific'])]
ROOT=dict(meaning='深睡',core='sopor- 最实用的画面是越来越重的眼皮。',image='某种声音、节奏或冗长讲话，让人渐渐进入想睡的状态。',intro='拉丁 sopor 指深睡。英语最值得掌握的是 soporific：从使人睡着的作用，扩展到乏味得让人打瞌睡的描写。',forms='sopor- 提供深睡的概念；-fic 提供“造成、产生”的方向。整体经法语 soporifique 借入。',branches=[['让人想睡的效果','soporific']],contrasts='somnolent 偏昏昏欲睡的状态，soporific 偏造成这种状态的东西。',practice='用 soporific 描述一个单调的声音，再说明它是令人舒服还是令人厌倦。',sources=['https://www.etymonline.com/word/soporific'])
m=json.loads((BASE/'.cache/batch200/rewrite_spec.json').read_text());r=next(x for x in m['roots']if x['id']==ID);c=next(x for x in json.loads((BASE/'.cache/catalog.json').read_text())if x['id']==ID);keep={w['word']for w in W}|set(SHARED);excluded={w:EXCLUDE_REASON for w in(set(r['family'])|set(c['family'])|set(c.get('unmatched',[])))-keep}
ROOT['id']=ID;ROOT['words']=list(dict.fromkeys([w for w in r['family']if w in keep]+[w for w in SHARED if w not in r['family']]));ROOT['exclude']=excluded
assert all(w['word']in m['owned_words']for w in W)
assert not(set(c['family'])|set(c.get('unmatched',[])))-set(ROOT['words'])-set(excluded)
assert {w['word']for w in W}<=set(ROOT['words'])
for w in W:assert len(w['examples'])>=2 and all(len(n)==2 and all(isinstance(x,str)and x for x in n)for n in w['history'])
for k,d in [('roots',[ROOT]),('words',W)]: (OUT/f'{k}_batch200_spec_{TAG}.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
print(ID,len(W),'new,',len(SHARED),'shared')
