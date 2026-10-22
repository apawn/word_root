# coding: utf-8
import json
from pathlib import Path
from author_batch200_root_per_a import W as A
from author_batch200_root_per_b import W as B
W=A+B
shared=['perfect','perfection','perfectionist','perfectionism','persistence','percent','percentage']
ROOT=dict(id='C1001',meaning='穿过；遍及；彻底',core='PER = THROUGH / THOROUGHLY',image='想一滴水穿过材料，再想它慢慢扩散到各处：从穿过变成遍及；把一件事做到头，又有彻底的意思。',intro='来自拉丁 per。严格说，本页讲的是前缀和介词，不是独立实义词根；它能把后面的动作改成穿过、遍及或完全做到。permeate 是穿过材料，pervade 是遍及各处，perfect 的历史意象是完全做成。',forms='per- 在部分古典组合中会发生辅音同化，出现 pel- 等形式。英语独立介词 per 常表示每或按照。peruse 的具体早期路线有不同分析，现代也确实有随意翻阅义，不能强行按彻底义限制它。',branches=[['穿过材料及其难易','permeate, permeable, impermeable, permeability, permeation'],['遍及各处','pervade, pervasive, pervasiveness'],['完成、坚持与严重程度','perfect, perfection, perfectionist, perfectionism, persistence, pernicious'],['查看与阅读','peruse, perusal, perusing'],['按单位计算','per, percent, percentage']],contrasts='permeation 是过程，permeability 是性质。pervade 强调遍及，permeate 更容易让人想到渗进内部。peruse 可以细读也可以翻阅，实际语境比词根联想更有决定作用。',practice='Water can permeate a permeable material, while an idea can pervade an entire organization.\n\n水能渗入可透水的材料，观念也能遍及整个组织。',words=shared+[x['word'] for x in W],exclude={'pellucid':'较罕见的文学形容词，先掌握 clear 与 transparent'})
if __name__=='__main__':
 for name,data in [('roots_per',[ROOT]),('words_per',W)]:Path('.cache/batch200/drafts/root/'+name+'.json').write_text(json.dumps(data,ensure_ascii=False,indent=2))
 print(len(W),sum(len(x['examples']) for x in W))
