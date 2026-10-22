# coding: utf-8
import json
from pathlib import Path
from author_batch200_root_chron_a import W as A
from author_batch200_root_chron_b import W as B
from author_batch200_root_chron_c import W as C
W=A+B+C
SHARED='chronological chronology synchronous asynchronous synchronize synchronicity synchronously geosynchronous chronostasis'.split()
kept=[x['word'] for x in W]+SHARED
r=next(x for x in json.loads(Path('.cache/catalog.json').read_text()) if x['id']=='C0216')
EX={w:'本轮先略过地质、生理、数学等更专门的词' for w in set(r['family'])|set(r['words']) if w not in kept and '-' not in w}
ROOT=dict(id='C0216',meaning='时间',core='CHRON = TIME',image='想象一条时间线：沿线记事是 chronicle；在同一刻对齐是 synchronize；把东西放错年代是 anachronism；一个问题沿线拖很久，就是 chronic。',intro='来自希腊 khronos“时间”。更早来源尚不确定，不必编造故事。它与表示颜色的 chrom- 不同；chronic 里的 n 和 chromatic 里的 m，差一个字母就换了词根。',forms='chron-、chrono- 是同一时间成分。syn- 把事放到一起，dia- 看贯穿时间的变化，ana- 在 anachronism 里进入“放错时间”的历史组合，不能只按一个固定中文义机械相加。',branches=[['持续很久','chronic, chronically'],['按时间记录和排列','chronicle, chronicler, chronology, chronological'],['同步或不同步','synchronize, synchronise, synchronization, synchronisation, synchronous, asynchronous, synchronously, synchronicity, geosynchronous'],['时代错位','anachronism, anachronistic'],['看一个时期或跨时期','synchronic, diachronic'],['测量与感知时间','chronograph, chronometer, chronostasis']],contrasts='chronic 不是一般的“时间的”，而偏长期或反复。chronology 重顺序，chronicle 重记事。synchronic 在研究中常指共时，synchronous 多指同步。',practice='A chronology puts the events in order; a chronicle tells us what happened along the way.\n\n时间表把事件排出先后；记事作品讲出这一路发生了什么。',words=kept,exclude=EX)
if __name__=='__main__':
 for name,data in [('roots_chron',[ROOT]),('words_chron',W)]:Path('.cache/batch200/drafts/root/'+name+'.json').write_text(json.dumps(data,ensure_ascii=False,indent=2))
 print(len(W),sum(len(x['examples']) for x in W))
