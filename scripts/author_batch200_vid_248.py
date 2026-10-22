# -*- coding: utf-8 -*-
"""C0730 mes: different kinds of middle, reusing existing entries."""
import json
from pathlib import Path
BASE=Path(__file__).resolve().parents[1];OUT=BASE/'.cache/batch200/drafts/rewrite_vid'
W=[];names=['mesosphere','Mesolithic'];cat=next(x for x in json.loads((BASE/'.cache/catalog.json').read_text()) if x['id']=='C0730');EX={w:'较专门的尺度或微生物生长条件术语，按当前通用阅读范围暂略。' for w in cat['family'] if w not in names}
ROOT=dict(id='C0730',meaning='中间的',core='希腊 mesos 表示“在中间”。它不会告诉你是哪一种中间：大气分层有上下位置，考古分期有先后顺序，必须把后半个词一起读。',image='meso- 中间 + sphere 层、圈 → mesosphere 大气中间层；meso- 中间 + lithic 石的 → Mesolithic 中石器时代的。',intro='同样的“中间”，放进不同分类系统就是不同概念。不要把两个词都只记成模糊的“中等”。',forms='mes-／meso- 接希腊 mesos；mesosphere 与 Mesolithic 都是后来的科学、学术命名，分别把希腊构词材料重新组合。',branches=[['大气的层次','mesosphere'],['考古时代分期','Mesolithic']],contrasts='mesosphere 位于平流层之上、热层之下；Mesolithic 指使用这套分期的地区中，旧石器与新石器之间的阶段。后者不等于所有地区时间长度的正中点。',practice='给两个词各补一句“中间是相对于什么而言”：大气层的位置，还是考古分期的顺序？',words=names,exclude=EX)
if __name__=='__main__':
 for kind,data in [('roots',[ROOT]),('words',W)]: (OUT/(kind+'_batch200_vid_248.json')).write_text(json.dumps(data,ensure_ascii=False,indent=2))
 print('mes: 0 new; 2 shared')
