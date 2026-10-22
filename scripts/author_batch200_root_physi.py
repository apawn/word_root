# coding: utf-8
import json
from pathlib import Path
from author_batch200_root_physi_a import W as A
from author_batch200_root_physi_b import W as B
W=A+B;words=[w['word'] for w in W]+['biophysics','physiology','physiological','physiotherapy','physiotherapist']
r=next(x for x in json.loads(Path('.cache/catalog.json').read_text()) if x['id']=='C1035');EX={w:'专名或较冷门的派生，本轮暂略' for w in r['family'] if w not in words and '-' not in w}
ROOT=dict(id='C1035',meaning='生长、自然、本性；物质与身体',core='PHYSI = NATURE',image='先看自然中的东西如何生长、如何存在和运转。历史上的自然知识很宽，后来分出物理学、医学和生理学；今天相似的词头不再意味着同一门学科。',intro='希腊 physis 表自然、本性，接生长、产生的动词。physics 逐渐专指物理学，physician 保留医术一支，physical 则常指身体或实体。physiology 关注生命功能，physiotherapy 关注身体功能相关的治疗。',forms='phys-、physi-、physio- 都可能出现。ph 读 /f/，physic 的 s 在这些常见词中多读 /z/。physics、physicist 与 physician 的后半段不同，不能把 -ist 和 -ician 当成任何场合都能互换的职业后缀。',branches=[['物理学及研究者','physics, physicist'],['研究天体、地球与生命中的物理问题','astrophysics, geophysics, biophysics'],['身体与实体','physical, physically'],['医学、生理学与治疗','physician, physiology, physiological, physiologist, physiotherapy, physiotherapist']],contrasts='physician 是医生，physicist 是物理学家，physiologist 是生理学家。physical copy 是实体副本，physical exercise 是身体锻炼；physical 不能只译成物理的。',practice='The physician treated patients, while the physicist studied light and the physiologist studied how the body works.\n\n医生为病人诊治，物理学家研究光，生理学家研究身体如何运作。',words=words,exclude=EX)
if __name__=='__main__':
 for name,data in [('roots_physi',[ROOT]),('words_physi',W)]:Path('.cache/batch200/drafts/root/'+name+'.json').write_text(json.dumps(data,ensure_ascii=False,indent=2))
 print(len(W),sum(len(w['examples']) for w in W))
