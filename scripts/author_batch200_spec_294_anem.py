# coding: utf-8
from pathlib import Path
import json
from lesson_authoring import entry as E
BASE=Path(__file__).resolve().parents[1];OUT=BASE/'.cache/batch200/drafts/rewrite_spec'
ID='C0054';TAG='294_anem';SHARED=['anemometer'];EXCLUDE_REASON='按当前通用阅读范围暂略冷门气象仪器、植物授粉细分及特殊恐惧名称。'
W=[E('anemone','/əˈneməni/','银莲花；海葵','陆地上是一类花，海里则是因外形像花而得名的动物。','经拉丁 anemone，并有法语中介的借入分析，接希腊 anemōnē。传统把它联系 ánemos“风”，解释成风之女；也有闪米特语植物名来源说，所以这一远源不作定论。',[['希腊 anemōnē','植物名；传统联系 ánemos“风”，也有其他远源分析'],['拉丁 anemone；法语 anemone → 英语 anemone','银莲花这一名称进入英语'],['英语 sea anemone，亦简称 anemone','海洋动物因展开时像花而获得相同名称']],'花园里的 anemones 是植物；岩池里的 anemones 则是海葵。海葵的触手展开后像一圈花瓣，但它是捕食小动物的动物，不能因为名字和外观就把它当海草。','wood anemones；plant anemones；a sea anemone；anemones in a rock pool。','anemone 末尾有 /ni/，不要漏掉最后一节。anemometer 的 anemo- 明确表示风；anemone 的远源联系则有争议，二者的确定程度不同。',('White anemones covered the woodland floor.','白色银莲花铺满了林地。'),('The anemone closed its tentacles around a small piece of food.','那只海葵用触手合拢包住了一小块食物。'),sources=['https://www.etymonline.com/word/anemone','https://www.oxfordlearnersdictionaries.com/definition/english/anemone','https://www.montereybayaquarium.org/animals/animals-a-to-z/giant-green-anemone'])]
ROOT=dict(meaning='风',core='anemo- 把“风”放进仪器或自然现象的名称里。',image='风吹动测量仪器，转动或其他信号被换算成风速。',intro='希腊 ánemos 就是“风”。anemometer 的构词很清楚：风＋测量仪。anemone 传统上也联系风，但植物名的更早来源存在其他解释，放在这里对照时要保留这条边界。',forms='anemo- 是常见连接形式；anemometer 中与 -meter 组合。anemone 是整词借入，不宜当成现代英语 anemo- 加一个自由使用的 -ne。',branches=[['风的测量','anemometer'],['传统联系风的植物名，远源有争议','anemone']],contrasts='sea anemone 是动物；anemometer 测风速，风向标主要显示风向。',practice='用两句话分别说明 anemometer 测什么，以及 sea anemone 为什么不是一种海草。',sources=['https://www.etymonline.com/word/anemone','https://www.merriam-webster.com/dictionary/anemometer'])
m=json.loads((BASE/'.cache/batch200/rewrite_spec.json').read_text());r=next(x for x in m['roots']if x['id']==ID);c=next(x for x in json.loads((BASE/'.cache/catalog.json').read_text())if x['id']==ID);keep={w['word']for w in W}|set(SHARED);excluded={w:EXCLUDE_REASON for w in(set(r['family'])|set(c['family'])|set(c.get('unmatched',[])))-keep}
ROOT['id']=ID;ROOT['words']=list(dict.fromkeys([w for w in r['family']if w in keep]+[w for w in SHARED if w not in r['family']]));ROOT['exclude']=excluded
assert all(w['word']in m['owned_words']for w in W)
assert not(set(c['family'])|set(c.get('unmatched',[])))-set(ROOT['words'])-set(excluded)
assert {w['word']for w in W}<=set(ROOT['words'])
for w in W:assert len(w['examples'])>=2 and all(len(n)==2 and all(isinstance(x,str)and x for x in n)for n in w['history'])
for k,d in [('roots',[ROOT]),('words',W)]: (OUT/f'{k}_batch200_spec_{TAG}.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
print(ID,len(W),'new,',len(SHARED),'shared')
