# -*- coding: utf-8 -*-
"""C1040 piez: pressure-related electrical response, reusing verified lessons."""
import json
from pathlib import Path
BASE=Path(__file__).resolve().parents[1];OUT=BASE/'.cache/batch200/drafts/rewrite_vid'
W=[];names=['piezoelectric','piezoelectricity'];cat=next(x for x in json.loads((BASE/'.cache/catalog.json').read_text()) if x['id']=='C1040');EX={w:'较专门的压力测量或材料性质术语，当前先保留常见的压电概念。' for w in cat['family'] if w not in names}
ROOT=dict(id='C1040',meaning='挤压；压力',core='希腊 piezein 是“挤紧、压”。想象按压某些材料时出现电响应，就能记住 piezoelectric 的“压电”联系。',image='piezein 挤压 + 电学命名材料 → 近代压电术语 → piezoelectric 压电的；piezoelectricity 压电性或现象。',intro='这组词常见于传感器、超声器件与精密执行器的介绍。学习重点是机械作用与电响应的联系，不必为理解这两个词先学一整套材料学。',forms='piezo- 是近代科学构词形式，来自希腊 piezein。压电名称经 19 世纪德语 Piezoelectricität 进入英语术语系统；不是古希腊已有现代电学名称。',branches=[['材料性质与相关现象','piezoelectric, piezoelectricity']],contrasts='piezoelectric 是形容词，piezoelectricity 是名词。压电材料可把机械作用与电响应联系起来；这不是凭空产生能量，也不是任何材料受压都具有的性质。',practice='a piezoelectric sensor 是一种传感器；the principle of piezoelectricity 说的是它利用的物理现象。',words=names,exclude=EX)
if __name__=='__main__':
 for kind,data in [('roots',[ROOT]),('words',W)]: (OUT/(kind+'_batch200_vid_240.json')).write_text(json.dumps(data,ensure_ascii=False,indent=2))
 print('piez: 0 new; 2 shared')
