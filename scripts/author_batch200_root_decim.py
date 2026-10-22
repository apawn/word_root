# coding: utf-8
import json
from pathlib import Path
from author_batch200_root_decim_a import W as A
from author_batch200_root_decim_b import W as B
W=A+B;kept=[x['word'] for x in W]
r=next(x for x in json.loads(Path('.cache/catalog.json').read_text()) if x['id']=='C0308')
EX={w:'较冷门的施事名词或古典形容词，本轮暂略' for w in set(r['family'])|set(r['words']) if w not in kept and '-' not in w}
ROOT=dict(id='C0308',meaning='第十；十分之一',core='DECIM = TENTH / ONE TENTH',image='把一个整体切成十份：其中一份可以是一角钱，也可以成为小数位值的基础；古代取走一成的制度，则留下另一条词义路线。',intro='拉丁 decem 表十，decimus 表第十，decima pars 表十分之一。decimal 和 dime 保留数量关系；decimate、decimation 经过语义扩大，今天通常强调大量损失，不能只按古义限定现代用法。',forms='decim- 在 decimal、decimate 中较明显，经法语变化后成为 dime。hexadecimal 是 hexa- 六与 decimal 的现代组合，用来命名十六进制。',branches=[['记数与小数','decimal, hexadecimal'],['十分之一美元','dime'],['取走一成的旧义与严重损失的新义','decimate, decimation']],contrasts='decimal 是十进制／小数，decimation 是严重损失。dime 是0.10美元。decimate 的现代严重破坏义并非刚出现的误用；词源不是限制现代词义的规定。',practice='The old coin was worth a dime, or 0.10 dollars in decimal notation.\n\n这枚旧硬币面值一角美元，用小数写就是0.10美元。',words=kept,exclude=EX)
if __name__=='__main__':
 for name,data in [('roots_decim',[ROOT]),('words_decim',W)]:Path('.cache/batch200/drafts/root/'+name+'.json').write_text(json.dumps(data,ensure_ascii=False,indent=2))
 print(len(W),sum(len(x['examples']) for x in W))
