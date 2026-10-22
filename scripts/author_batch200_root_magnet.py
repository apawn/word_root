# coding: utf-8
import json
from pathlib import Path
from author_batch200_root_magnet_a import W as A
from author_batch200_root_magnet_b import W as B
from author_batch200_root_magnet_c import W as C
W=A+B+C;kept=[x['word'] for x in W]+'electromagnet electromagnetic electromagnetism geomagnetic'.split()
r=next(x for x in json.loads(Path('.cache/catalog.json').read_text()) if x['id']=='C0699')
EX={w:'本轮暂略更细的材料物理、生物物理和电子器件术语' for w in set(r['family'])|set(r['words']) if w not in kept and '-' not in w}
ROOT=dict(id='C0699',meaning='磁石、磁；由此产生的吸引力比喻',core='MAGNET = MAGNET / ATTRACTION',image='一块磁铁把回形针吸过来；一个有魅力的人把注意力吸过来。先把真实磁性和比喻吸引力分开，再看它们如何相通。',intro='来自希腊与 Magnesia 地名有关的磁石名称，经拉丁 magnes、magnet- 与法语进入英语。具体对应哪个古代同名地区有不同说法，不必把地理细节讲死。magnesium 和 manganese 经旧矿物名的不同支线发展，不能都解释成磁铁。',forms='magnet 是磁铁；magnetic 表性质；magnetism 表现象或魅力；magnetize 表使磁化；magneto- 是复合词中的形式。-ite 可构成矿物名，-meter 表测量仪器。',branches=[['磁铁和吸引力','magnet, magnetic, magnetism, magnetically'],['磁化和测量','magnetize, magnetization, magnetometer'],['电磁与地磁','electromagnet, electromagnetic, electromagnetism, geomagnetic'],['矿物和元素名称支线','magnetite, magnesium, manganese']],contrasts='magnet 的吸引力比喻适用于人和地点。magnesium、manganese 是镁和锰，既不是同一元素，也不等于 magnetite 磁铁矿。',practice='Her magnetic personality made the small bookshop a magnet for local readers.\n\n她富有吸引力的个性，让这家小书店成了吸引本地读者的地方。',words=kept,exclude=EX)
if __name__=='__main__':
 for name,data in [('roots_magnet',[ROOT]),('words_magnet',W)]:Path('.cache/batch200/drafts/root/'+name+'.json').write_text(json.dumps(data,ensure_ascii=False,indent=2))
 print(len(W),sum(len(x['examples']) for x in W))
