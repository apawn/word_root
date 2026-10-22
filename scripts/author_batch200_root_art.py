# coding: utf-8
import json
from pathlib import Path
from author_batch200_root_art_a import W as A
from author_batch200_root_art_b import W as B
from author_batch200_root_art_c import W as C
from author_batch200_root_art_d import W as D
W=A+B+C+D;kept=[x['word'] for x in W]+['artifact','artifice']
ROOT=dict(id='C0083',meaning='技艺；技巧；艺术',core='ART = SKILL',image='一双熟练的手把东西做出来：作品是 art，做东西的人可叫 artisan。技巧用来精心设计是 artful；人为做出来是 artificial；不加心机修饰又能成为 artless。',intro='来自拉丁 ars，变格形式 artis、artem 保留 art-。古义是技艺、学问和做事能力，比今天想到的绘画雕塑更宽。英语词族既谈艺术，也谈制作、手段与人为痕迹。',forms='art-、arti- 是主要形式。artifact、artifice、artificial 还接 facere“做”一族；artist、artistic 各有法语等借入路线。inert、inertia 的 inert- 则是拉丁 in- 与 ars 结合后变形，不能按现代拼写强拆为 in + ert。',branches=[['艺术与表现','art, artist, artistic, artistically, artistry, artwork'],['技巧与不做作','artful, artfully, artless, artifice'],['显眼的文艺气质','arty, artsy'],['人工制作与工匠','artificial, artificially, artificiality, artisan, artisanal, artifact, artefact'],['从不活跃到惯性','inert, inertia, inertial']],contrasts='artistic 是艺术的；artful 可能是有心计的；artless 可说天真自然；artificial 是人为制造或不自然。artist 与 artisan 有交集，不能把其中一个简单判为高级、另一个低级。',practice='The artisan’s artistry was clear, but the artificial flowers were arranged so artfully that visitors barely noticed they were not real.\n\n工匠的技艺显而易见，而人造花又摆放得如此巧妙，参观者几乎没看出它们不是真花。',words=kept,exclude={})
if __name__=='__main__':
 for name,data in [('roots_art',[ROOT]),('words_art',W)]:Path('.cache/batch200/drafts/root/'+name+'.json').write_text(json.dumps(data,ensure_ascii=False,indent=2))
 print(len(W),sum(len(x['examples']) for x in W))
