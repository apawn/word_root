# -*- coding: utf-8 -*-
"""C0859 od: an alternate hodos entry reusing the finished word lessons."""
import json
from pathlib import Path
BASE=Path(__file__).resolve().parents[1];OUT=BASE/'.cache/batch200/drafts/rewrite_vid'
W=[]
SH=['method','methodology','period','episode','odometer','anode','cathode','diode','triode','tetrode','pentode']
ROOT=dict(id='C0859',meaning='道路、通路；行程、途径',core='这与 hod- 是同一条希腊 hodos“道路”词源。路既能是走过的路程，也能变成做事的途径，近代科学又用它命名电流进出的路径。',image='hodos 路 → method 做事的途径／odometer 路程计；anodos 上行、kathodos 下行 → anode／cathode；electrode 的 -ode → diode、triode 等名称。',intro='不要把 od- 当成一个与 hod- 无关的新词根。拼写变化和不同借入年代，让同一“道路”概念藏在方法、里程表与电子元件里。',forms='希腊 hodos 的转写与组合形式可见 hod-、odo-、-ode。method、period 等经过古希腊已有词及拉丁、法语传播；电子元件名称多为近代构词，不能都画成古代完整单词。',branches=[['做事与研究的途径','method, methodology'],['绕行及插入的一段','period, episode'],['计量走过的路','odometer'],['电流路径与电极名称','anode, cathode'],['电极数量构成的器件名','diode, triode, tetrode, pentode']],contrasts='odometer 记录走了多远，speedometer 显示多快。anode/cathode 的电化学区别是氧化端与还原端，不能单凭历史的“上／下”推出今天永远是正极或负极。',practice='把 method 想成完成事情可走的一条路，把 odometer 想成数路程的表。看到 diode、triode，再转向近代器件的电极数量，别把所有 -ode 都硬译成一条实际道路。',words=SH,exclude={'parodos':'古希腊戏剧合唱入口或入场歌等专门术语，按当前常用范围暂略。'})
if __name__=='__main__':
 m=json.loads((BASE/'.cache/batch200/rewrite_vid.json').read_text());r=next(x for x in m['roots'] if x['id']==ROOT['id'])
 assert {w for w in r['family'] if '-' not in w}<=set(ROOT['words'])|set(ROOT['exclude'])
 for kind,data in [('roots',[ROOT]),('words',W)]: (OUT/(kind+'_batch200_vid_157.json')).write_text(json.dumps(data,ensure_ascii=False,indent=2))
 print('od:',len(SH),'shared references')
