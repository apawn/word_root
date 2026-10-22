# -*- coding: utf-8 -*-
import json
from pathlib import Path
from author_batch200_root_terr_a import WA
from author_batch200_root_terr_b import WB
W=WA+WB
ROOT=dict(id='C1497',meaning='土地；大地；地球',core='TERR = EARTH / LAND',image='先看脚下那块土地：它可以起伏成地形，垒成台地，烧成陶器，也可以被圈成领地。把视角拉远，同一个“大地”又成了地球；往下看，则是地下。',intro='主要来源是拉丁 terra“土地、泥土、大地”。它经法语形成 terrain、terrace 等，也进入 terrestrial、subterranean 等学术词。territory 的直接来源 territorium 没有疑问，但 territorium 更早是否、怎样从 terra 构成仍有争论，本页保留常见关联解释，不把它当作已解决的事实。',forms='terra、terr-、terrestr- 是本族常见形式。inter 这个“安葬”动词含 in- 与 terra 的历史成分，不是 inter-“在……之间”；terrier 的狗名接“地洞、土”的支线。terrible、terror 的直接拉丁来源是 terrere“使害怕”，不要因为拼写相似就并入 terra。',branches=[['土地的形状与岩石区域','terrain, terrane, terrace, terraced, terracing'],['范围、地盘与制度','territory, territorial, territoriality, territorially, territorialism, territorialist, extraterritorial, extraterritoriality'],['陆地、地球和地下','terrestrial, terrestrially, subterranean, extraterrestrial, terrene, terra, Mediterranean'],['土地的材料与小环境','terracotta, terrazzo, terrarium, terrigenous'],['放入土中，再从土中取出','inter, interment, disinter, disinterment'],['与地洞有关的犬名','terrier'],['设想把另一星球改得像地球','terraform, terraforming']],contrasts='terrain 看地形，territory 看范围及归属；terracotta 是烧制陶土，terrazzo 是碎料复合材料。interment 是安葬，internment 是拘禁。terrigenous 说来自陆地，物质后来可以落在海底；terrestrial 的具体含义要看是在对比水域、天空还是地外环境。',practice='We crossed rough terrain before reaching the village. From the terrace, we could see the terraced fields spread across the hillside.\n\n我们穿过崎岖地形来到村庄。从露台上，可以看见山坡上一层层展开的梯田。',words=[w['word'] for w in W]+['extraterrestrial','extraterritorial','Mediterranean'])
if __name__=='__main__':
 assert len(W)==28 and len({w['word'] for w in W})==28
 for name,v in [('roots_terr',[ROOT]),('words_terr_a',WA),('words_terr_b',WB)]:Path('.cache/batch200/drafts/root/'+name+'.json').write_text(json.dumps(v,ensure_ascii=False,indent=2))
 print(len(W),'individually authored words',sum(len(w['examples']) for w in W),'examples')
