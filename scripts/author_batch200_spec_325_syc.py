# coding: utf-8
from pathlib import Path
import json
from lesson_authoring import entry as E
BASE=Path(__file__).resolve().parents[1];OUT=BASE/'.cache/batch200/drafts/rewrite_spec'
ID='C1461';TAG='325_syc';SHARED=['sycophant','sycophantic'];EXCLUDE_REASON='暂略罕见的无花果占卜术语。'
S=[['希腊 sýkon；phaínein','无花果；显示：并列材料，具体命名背景有争议'],['希腊 sykophántēs → 拉丁 sycophanta','诬告者、告密者等旧义'],['法语 sycophante，及拉丁直接借入','进入英语的路线'],['英语 sycophant','早有告密者义，后常指趋炎附势的奉承者']]
W=[
E('sycophancy','/ˈsɪkəfənsi/','阿谀奉承；趋炎附势','把一味讨好的做法当成一种行为来谈。','现代可由 sycophant 与抽象名词词尾 -cy 对应理解；也有拉丁 sycophantia←希腊 sykophantía〔诬告、奉承者行为〕的借入分析。两种路线并列保留。',[S[0],['希腊 sykophántēs；sykophantía','诬告者；相应行为名称'],['拉丁 sycophantia 借入；或英语 sycophant＋-cy','两种来源分析并列'],['英语 sycophancy','谄媚讨好的行为']],'办公室里如果每个人都只夸领导、不敢提出坏消息，这种风气可以叫 sycophancy。它不是一次恰巧说了好话，而是把取悦权力放在真实判断前面。','political sycophancy；a culture of sycophancy；reject sycophancy。','sycophant 是人，sycophantic 是形容词，sycophancy 是行为或风气。',('The review criticised the interview for its obvious sycophancy.','评论批评那次采访明显充满阿谀奉承。'),('A culture of sycophancy kept bad news from reaching the manager.','一味逢迎的风气让坏消息传不到经理耳中。'),sources=['https://www.etymonline.com/word/sycophancy','https://www.oxfordlearnersdictionaries.com/definition/english/sycophancy'])]
ROOT=dict(meaning='无花果〔保留在有争议的历史命名中〕',core='本组实用词讲的是奉承者；无花果是历史材料，不是现代意思的直译钥匙。',image='想一个总顺着权势说话的人：他只递好听的话，不递真实意见。',intro='希腊 sýkon 是无花果，sykophántēs 字面含“显示无花果”，古代却用于诬告者等人。具体命名背景有争议，后来的英语发展出趋炎附势的奉承义；不应编一个确定故事来填补中间环节。',forms='sycophant 指人，sycophantic 形容行为，sycophancy 指奉承这种做法。',branches=[['人','sycophant'],['行为与性质','sycophancy；sycophantic']],contrasts='礼貌、欣赏和赞美不必是谄媚；关键在是否为了讨好而放弃真实判断。',practice='分别用 sycophant、sycophantic、sycophancy 描述一个人、一段发言和一种办公室风气。',sources=['https://www.etymonline.com/word/sycophant','https://www.etymonline.com/word/sycophancy'])
m=json.loads((BASE/'.cache/batch200/rewrite_spec.json').read_text());r=next(x for x in m['roots']if x['id']==ID);c=next(x for x in json.loads((BASE/'.cache/catalog.json').read_text())if x['id']==ID);keep={w['word']for w in W}|set(SHARED);excluded={w:EXCLUDE_REASON for w in(set(r['family'])|set(c['family'])|set(c.get('unmatched',[])))-keep}
ROOT['id']=ID;ROOT['words']=list(dict.fromkeys([w for w in r['family']if w in keep]+[w for w in SHARED if w not in r['family']]));ROOT['exclude']=excluded
assert all(w['word']in m['owned_words']for w in W)
assert not(set(c['family'])|set(c.get('unmatched',[])))-set(ROOT['words'])-set(excluded)
assert {w['word']for w in W}<=set(ROOT['words'])
for w in W:assert len(w['examples'])>=2 and all(len(n)==2 and all(isinstance(x,str)and x for x in n)for n in w['history'])
for k,d in [('roots',[ROOT]),('words',W)]: (OUT/f'{k}_batch200_spec_{TAG}.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
print(ID,len(W),'new,',len(SHARED),'shared')
