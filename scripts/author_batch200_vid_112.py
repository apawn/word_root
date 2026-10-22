# -*- coding: utf-8 -*-
"""C1459 surg: shared lessons already authored under reg/rect."""
import json
from pathlib import Path
BASE=Path(__file__).resolve().parents[1];OUT=BASE/'.cache/batch200/drafts/rewrite_vid'
W=[]
SHARED=['surge','upsurge','resurgent','resurgence','insurgent','insurgency','insurrection','resurrection','resurrect','source','resource','resourceful','resourcefulness']
ROOT=dict(id='C1459',meaning='升起、挺起、重新出现',core='拉丁 surgere 是从低处起来。水往上涌是 surge；力量再次抬头是 resurgence；人群奋起反抗便接到 insurgent。',image='向上起来 → surgere；re- 再次 → resurgere；in- 奋起反对 → insurgere。法语声音变化又留下 source、resource。',intro='这一根还藏着两个很日常的词：source 原先连着涌起的泉源，resource 连着重新起来、恢复所需的办法和来源。记住它们的历史联系，再分别学现代搭配，不把 resource 硬拆成“再来一个 source”。',forms='surgere 缩自 surrigere，后者来自 sub- 从下向上 + regere 使直、引导。分词词干 surrect- 留在 resurrection、insurrection 一类名词中。英语 surge 的具体法语中介有分歧；surgeon、surgery 属于希腊“手工操作”支线，不因拼写相近混入本根。',branches=[['像浪一样涌起','surge, upsurge'],['再次恢复力量或生命','resurgent, resurgence, resurrection, resurrect'],['起来反抗','insurgent, insurgency, insurrection'],['涌起之处成为来源与资源','source, resource, resourceful, resourcefulness']],contrasts='resurgence 常说某种力量、兴趣重新活跃；resurrection 可说复活或旧事物恢复。英语 resurrection 早于 resurrect，后者由名词逆构。insurgency 强调持续反叛活动，insurrection 强调公开起事，不能仅凭共同词根把它们当完全同义。',practice='A surge in demand used up our resources, but the team remained resourceful. 需求猛增消耗了资源，但团队仍能想办法：涌起、可用条件、善用条件，是同族词的不同落点。',words=SHARED,exclude={})
if __name__=='__main__':
 m=json.loads((BASE/'.cache/batch200/rewrite_vid.json').read_text());r=next(x for x in m['roots'] if x['id']==ROOT['id']);assert set(r['family'])<=set(SHARED)
 for kind,data in [('roots',[ROOT]),('words',W)]: (OUT/(kind+'_batch200_vid_112.json')).write_text(json.dumps(data,ensure_ascii=False,indent=2))
 print('surg: 0 new words; 13 shared references')
