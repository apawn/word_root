# coding: utf-8
import json
from pathlib import Path
from author_batch200_root_tem_a import W as A
from author_batch200_root_tem_b import W as B
from author_batch200_root_tem_c import W as C
from author_batch200_root_tem_d import W as D
W=A+B+C+D;kept=[x['word'] for x in W]+['entomology','subatomic']
r=next(x for x in json.loads(Path('.cache/catalog.json').read_text()) if x['id']=='C1483')
EX={w:'本轮暂略更细的生物、医学、化学及修辞术语' for w in set(r['family'])|set(r['words']) if w not in kept and '-' not in w}
ROOT=dict(id='C1483',meaning='切；分割；切分出来的一部分',core='TEM / TOM = CUT',image='一把想象中的刀，可以切开整体、分成两半、留下截面，也可以删短一篇文章。不同前缀告诉你怎样切，名词和比喻再沿各自的历史发展。',intro='希腊 temnein 表切，tom- 是同源词干形式。atom 的历史画面是“切不开”，anatomy 是“切开研究”，dichotomy 是“切成两份”，tome 是一卷，epitome 是删短后的摘要再引申为典型体现。',forms='tem-、tom-、tomo- 都与切分有关。-tomy 常用于切开相关名称；tomography 生成截面图像，不等于实际切开身体。a- 在 atom 中是否定，ana- 在 anatomy 中是切开这一历史组合的一部分。',branches=[['古代认为不可分的单位','atom, atomic, subatomic'],['切开研究结构','anatomy, anatomist, anatomical, anatomically'],['删短、浓缩和书卷','epitome, epitomize, epitomise, tome'],['分成两类','dichotomy, dichotomous'],['截面成像','tomography'],['昆虫的分节命名','entomology, entomologist, entomological']],contrasts='atom 的“不可分”是命名历史，现代已知原子有内部结构。epitome 末尾读 /mi/，tome 读 /təʊm/。entomology 研究昆虫，etymology 研究词源。',practice='The article offers an anatomy of the problem and challenges the false dichotomy at its centre.\n\n文章剖析了这个问题，并质疑其中非此即彼的错误分法。',words=kept,exclude=EX)
if __name__=='__main__':
 for name,data in [('roots_tem',[ROOT]),('words_tem',W)]:Path('.cache/batch200/drafts/root/'+name+'.json').write_text(json.dumps(data,ensure_ascii=False,indent=2))
 print(len(W),sum(len(x['examples']) for x in W))
