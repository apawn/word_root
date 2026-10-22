# -*- coding: utf-8 -*-
from pathlib import Path
import json
from lesson_authoring import entry as E
BASE=Path(__file__).resolve().parents[1];OUT=BASE/'.cache/batch200/drafts/rewrite_spec'
R=[['拉丁 rūs，属格 rūris','乡野、农村、开阔田地']]
RU=R+[['拉丁 rūrālis → 法语 rural / 英语 rural','乡村的']]
W=[
E('rural','英 /ˈrʊərəl/；美 /ˈrʊrəl/','农村的；乡村的','把场景放在城市之外的乡村地区。','经法语 rural 或拉丁 rūrālis，接拉丁 rūs 的 rur- 词干加 -alis。这里的 rur- 不是英语 rule，也不表示统治。',RU,'rural roads 是乡村道路；rural population 是农村人口。它主要说明地域、生活环境，不意味着落后、贫穷或自然风光一定优美。','rural areas；rural communities；rural development；rural life。','urban 是城市的；rural 是乡村的；rustic 常进一步谈乡村式的质朴外观或风格。',('The programme improves internet access in rural areas.','这个项目改善农村地区的互联网接入。'),('She grew up in a rural community surrounded by farmland.','她在一个被农田环绕的乡村社区长大。'),sources=['https://www.oxfordlearnersdictionaries.com/definition/english/rural','https://www.etymonline.com/word/rural']),
E('rustic','/ˈrʌstɪk/','乡村式的；质朴粗犷的；乡下人','看着像未经精细雕琢的乡间生活：木头、石头和简单的做法。','借拉丁 rūsticus“乡村的、质朴的”，同样接 rūs“乡野”。它与 rural 是不同拉丁派生词进入英语，不是 rustic 从 rural 改几个字母造出。',R+[['拉丁 rūsticus → 英语 rustic','乡村的；质朴、未精细修饰的']],'a rustic table 常指带乡村质朴风格的桌子，即使放在城市公寓里也可以这样叫。旧文里 a rustic 可指乡下人，可能带居高临下的语气。','rustic charm；rustic furniture；a rustic cottage；rustic bread。','rural 主要说地点；rustic 主要说风格或特质。评价人的 manners 为 rustic 时，可能是在说粗俗而非赞美。',('The restaurant has wooden beams and a rustic interior.','餐厅有木梁和质朴的乡村风格内饰。'),('A rough stone path adds to the garden’s rustic charm.','一条粗石小径给花园增添了乡野韵味。'),sources=['https://www.etymonline.com/word/rustic']),
E('rurally','英 /ˈrʊərəli/；美 /ˈrʊrəli/','在农村；具有乡村特点地','说明地点处在乡村，或生活方式带有乡村特点。','rural 加 -ly，形成副词。多个 r 和弱读音节连在一起，读时保持 rural 的重音，不必把每个音节都拉得很长。',RU+[['英语 rural + -ly → rurally','在农村；以乡村方式']],'常见于较正式的地点说明，如 rurally located“位于农村的”。日常交流说 live in the countryside 通常更自然，没必要为使用副词而硬写 rurally。','rurally located；rurally based；live rurally。','rural 修饰名词，如 rural schools；rurally 可修饰 located、based 等，说明所在环境。',('The study compares urban and rurally located schools.','研究比较城市学校与位于农村的学校。'),('The service supports people who live rurally and have limited transport options.','这项服务帮助住在农村、交通选择有限的人。'),sources=['https://en.wiktionary.org/wiki/rurally#English','https://www.merriam-webster.com/dictionary/rurally'])
]
m=json.loads((BASE/'.cache/batch200/rewrite_spec.json').read_text());family=next(r['family'] for r in m['roots'] if r['id']=='C1241');shared=set()
excluded={w:'按用户最新范围暂略：较罕见的抽象派生、历史喧闹义或专门的停学、建筑术语。' for w in ['rusticity','rustication','roister','rusticate','nonrural','roisterous']}
ROOT=[dict(id='C1241',meaning='乡野；农村',core='rur-/rus-：城市之外的乡野，再延伸出质朴的乡村风格。',image='rural school 说学校在哪里；rustic furniture 说家具是什么风格。',intro='拉丁 rūs 的属格是 rūris，因此同一来源在派生词里可出现 rur- 和 rus-/rust-。农村地点与质朴风格是相关却不同的两条意思。',forms='rural 接拉丁 ruralis；rustic 接拉丁 rusticus。rurally 是英语 rural 加 -ly，主要用于较正式的地点或生活环境描述。',branches=[['地域环境','rural、rurally'],['乡村风格','rustic']],contrasts='一间城市餐厅也能有 rustic décor；rural 地区也可以有现代建筑。词源中的乡村联想不等于给居民贴落后或粗俗标签。',practice='用 rural 描述一个地区，再用 rustic 描述一件家具，分别突出地点和风格。',words=[w for w in family if w not in excluded],exclude=excluded,sources=['https://www.etymonline.com/word/rural','https://www.etymonline.com/word/rustic'])]
assert {x['word'] for x in W}==set(family)-shared-set(excluded)
assert len(W)==len({x['word'] for x in W}) and all(x['word'] in m['owned_words'] for x in W)
for x in W:
 assert len(x['examples'])>=2 and x['ipa'] and len(x['history'])>=2,x['word']
 assert all(len(n)==2 and all(isinstance(v,str) and v for v in n) for n in x['history']),x['word']
for k,d in [('roots',ROOT),('words',W)]: (OUT/f'{k}_batch200_spec_75_rur.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
print('C1241',len(W),'new',len(ROOT[0]['words']),'references',sum(len(x['examples']) for x in W),'examples')
