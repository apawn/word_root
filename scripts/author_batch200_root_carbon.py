# coding: utf-8
import json
from pathlib import Path
from author_batch200_root_carbon_a import W as A
from author_batch200_root_carbon_b import W as B
from author_batch200_root_carbon_c import W as C
W=A+B+C;kept=[x['word'] for x in W]
r=next(x for x in json.loads(Path('.cache/catalog.json').read_text()) if x['id']=='C0173')
EX={w:'专门化学词、矿物名或较冷门词，本轮暂略' for w in set(r['family'])|set(r['words']) if w not in kept and '-' not in w}
ROOT=dict(id='C0173',meaning='炭、煤；现代化学元素碳',core='CARBON = CHARCOAL → CARBON',image='从一块木炭出发，认出碳这种元素：它能进入岩石、生命分子和燃料，也能组成二氧化碳。词族由此通向化学、饮料、考古和减排。',intro='拉丁 carbo 指炭、煤，词干 carbon- 经法语 carbone 进入英语 carbon。名字来自具体的炭，现代意义扩大为元素，不要把所有同源词都想成黑色、燃烧或有毒。',forms='carbon- 是主形。carbonate 中 -ate 有名词与动词用法；carbonic 的 -ic 构成形容词；carboniferous 的 -ferous 是携带、含有；decarbonize 的 de- 表去除或减少。',branches=[['元素与碳氢组成','carbon, hydrocarbon'],['碳酸、碳酸盐与饮料','carbonic, carbonate, bicarbonate, carbonation, carbonated'],['煤层与年代','carboniferous, radiocarbon'],['减少排放','decarbonize, decarbonise, decarbonization'],['菜名旁支','carbonara']],contrasts='hydrocarbon 中 hydro- 指氢；bicarbonate 不是含两个碳的离子。carbonated 饮料含气，decarbonize 产业减排，carbonization 是炭化。carbonara 的词形与煤有关，但菜名由来的具体故事不能当定论。',practice='The museum used radiocarbon dating on an ancient wooden bowl; at lunch, we ordered carbonara and carbonated water.\n\n博物馆用放射性碳测年法研究了一只古代木碗；午饭时，我们点了卡博纳拉意面和气泡水。',words=kept,exclude=EX)
if __name__=='__main__':
 for name,data in [('roots_carbon',[ROOT]),('words_carbon',W)]:Path('.cache/batch200/drafts/root/'+name+'.json').write_text(json.dumps(data,ensure_ascii=False,indent=2))
 print(len(W),sum(len(x['examples']) for x in W))
