# coding: utf-8
import json
from pathlib import Path
from author_batch200_root_noc_a import W as A
from author_batch200_root_noc_b import W as B
W=A+B;kept=[w['word'] for w in W]
r=next(x for x in json.loads(Path('.cache/catalog.json').read_text()) if x['id']=='C0816')
EX={w:'较冷门的专业词或低收益派生词，本轮暂略' for w in set(r['family'])|set(r['words']) if w not in kept and '-' not in w}
ROOT=dict(id='C0816',meaning='伤害、损害；没有伤害则无害或无辜',core='NOC / NOX = HARM',image='围绕“有没有造成伤害”来记：innocent 可以是没有做坏事的人，innocuous 可以是无害的话，noxious 可以是有害烟气。伤害义变轻后，nuisance 就成了烦人的麻烦。',intro='拉丁 nocere 是伤害，相关词形有 nocens、nocuus、noxius 和 noxa。英语有些保留 noc- 或 nox-，nuisance 经法语变化后已经不容易一眼认出。obnoxious 的意义也经历过转向，不能用今天的形态直接倒推出全部历史。',forms='innocent 的 in- 是否定，nocent 接拉丁 nocens；innocuous 对应另一形容词 innocuus。noxious 与 nox- 同族，但这里的 nox- 不要与拉丁 nox“夜”混为一谈。nocebo 是拉丁动词的将来时形式。',branches=[['没有罪责、没有坏心','innocent, innocence, innocently'],['没有伤害或冒犯','innocuous'],['有害或令人反感','noxious, obnoxious, obnoxiously'],['伤害义减轻为烦扰','nuisance'],['专业心理与医学用法','nocebo']],contrasts='innocent 看责任或动机，innocuous 看是否无害。noxious 常形容有害物质，obnoxious 常形容讨厌的举止。nuisance 在日常可以是小麻烦，不必是严重危险。',practice='An innocent question may seem innocuous, yet still become a nuisance if it is asked repeatedly.\n\n一个没有恶意的问题可能看似无害，但反复追问，仍可能惹人厌烦。',words=kept,exclude=EX)
if __name__=='__main__':
 for name,data in [('roots_noc',[ROOT]),('words_noc',W)]:Path('.cache/batch200/drafts/root/'+name+'.json').write_text(json.dumps(data,ensure_ascii=False,indent=2))
 print(len(W),sum(len(w['examples']) for w in W))
