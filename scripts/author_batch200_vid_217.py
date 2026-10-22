# -*- coding: utf-8 -*-
"""C1363 solen: common technical entry through the existing solenoid lesson."""
import json
from pathlib import Path
BASE=Path(__file__).resolve().parents[1];OUT=BASE/'.cache/batch200/drafts/rewrite_vid'
W=[]; names=['solenoid'];cat=next(x for x in json.loads((BASE/'.cache/catalog.json').read_text()) if x['id']=='C1363')
EX={w:'较冷门的细胞形态或动物分类名称，按当前通用阅读范围暂略。' for w in cat['family'] if w not in names}
ROOT=dict(id='C1363',meaning='管；管道',core='solen- 接希腊 sōlēn“管”。把导线一圈一圈绕出管状外形，就能记住 solenoid 这个名称的出发点。',image='sōlēn 管 + 像……的形式 → 法语 solénoïde → 英语 solenoid 螺线管。',intro='在设备说明、阀门和电路文章里，这个词比同根的细分生物名称实用。先认出管形线圈，再结合上下文看它是否指整个电磁执行装置。',forms='solenoid 经法语 solénoïde 借入，结合“管”和“像……的”两种希腊来源材料。这里的 sol- 不接表示太阳或单独的其他词根。',branches=[['管状线圈与电磁装置','solenoid']],contrasts='名称说的是外形来源；装置的磁场来自通电。具体设备可能有铁芯、活动部件，但不是所有螺线管都必须带同一种铁芯。',practice='遇见 solenoid valve，先还原为“由电磁线圈控制的阀门”，再看说明里的具体用途。',words=names,exclude=EX)
if __name__=='__main__':
 for kind,data in [('roots',[ROOT]),('words',W)]: (OUT/(kind+'_batch200_vid_217.json')).write_text(json.dumps(data,ensure_ascii=False,indent=2))
 print('solen: 0 new; 1 shared')
