# coding: utf-8
import json
from pathlib import Path
from author_batch200_root_pater_a import W as A
from author_batch200_root_pater_b import W as B
from author_batch200_root_pater_c import W as C
W=A+B+C
words=[w['word'] for w in W]+['patrilineal']
r=next(x for x in json.loads(Path('.cache/catalog.json').read_text()) if x['id']=='C0972')
EX={w:'较冷门的派生、专门用语或专名，本轮按学习优先级暂略' for w in r['family'] if w not in words and '-' not in w}
ROOT=dict(id='C0972',meaning='父亲；保护者、祖辈和故国',core='PATER / PATR = FATHER',image='先想父亲这个家庭角色，再看三种延伸：提供保护与支持，传承祖辈留下的东西，以及把祖辈的土地称作故国。每个词只走其中一条路。',intro='拉丁 pater“父亲”的词干常显为 patr-。paternal 保留父亲义，patron 走向保护者和赞助人，pattern 则保留同源法语词里的范本义。patria 表故国，连到 repatriate。patriot 通过希腊语中同源的父亲、故国一支进入英语，不能把所有词都画成从拉丁语单线演化。',forms='pater 的属格 patris 显出 patr-；paternal 中可见 patern-。patron 与 pattern 是历史上分化的同源词；patter 的快语义与祷词 Pater noster 有关，而轻拍声义另接 pat。patriot 的希腊支与 repatriate 的拉丁支需分开。',branches=[['父亲与父系传承','paternal, paternity, paternalism, paternalistic, patrilineal, patrimony, patrician, patricide'],['保护与支持，也可能摆出优越姿态','patron, patronage, patronize, patronizing, patronising'],['范本到可辨认的模式','pattern, patterned, patterning'],['快语与轻拍声：两条来源','patter'],['完成某事到实施坏事','perpetrate, perpetrator, perpetration'],['祖辈的土地与回国','repatriate, repatriation, patriot, patriotic, patriotism']],contrasts='paternal 是父亲的，parental 是父母的；patronize 商店可以是光顾，patronize 一个人却可能是屈尊相待。pattern 是模式，patter 可以是快语或轻拍声。perpetrate 是犯下坏事，不能与 perpetuate“使延续”混写。',practice='The patron supported a new exhibition, but the curator disliked his patronizing tone.\n\n这位赞助人支持了一场新展览，但策展人不喜欢他居高临下的语气。',words=words,exclude=EX)
if __name__=='__main__':
 for name,data in [('roots_pater',[ROOT]),('words_pater',W)]:Path('.cache/batch200/drafts/root/'+name+'.json').write_text(json.dumps(data,ensure_ascii=False,indent=2))
 print(len(W),sum(len(w['examples']) for w in W))
