# coding: utf-8
import json
from pathlib import Path
from author_batch200_root_aer_a import W as A
from author_batch200_root_aer_b import W as B
from author_batch200_root_aer_c import W as C
from author_batch200_root_aer_d import W as D
W=A+B+C+D
SHARED=['aerospace','aerodynamic','anaerobic','aerodynamics','aerodrome','aerodynamically','airspace']
ROOT=dict(id='C0019',meaning='空气；空中',core='AER / AERO = AIR',image='同一团看不见的空气，可以充满房间、托住飞行器，也可以提供生物利用的氧；先分清是在讲空气本身、空中活动，还是现代有氧术语。',intro='来自希腊 aer，意为空气，经拉丁语与法语进入英语，日常形式是 air；近代学术词常保留 aer-、aero-。air 的空气义与相关合成词较清楚，但 air 表姿态、神情的历史另有争议，不强行全并成一条线。',forms='air 是日常词，aer- 常接元音，如 aerial、aerate；aero- 常见于 aeronautics、aerodynamics。aerobic 经近代法语术语进入英语，指需氧或有氧；anaerobic 的 an- 是否定，非 ana- 向上。',branches=[['房间、空气与流通','air, airy, airiness, airless, airflow, airtight'],['飞行与航空系统','airborne, aerial, airline, airport, aircraft, aeroplane, airplane, airliner, aircrew, airfare, airfield, airship, airlift, airway, airspace, aerodrome'],['航空技术与空气中悬浮物','aeronautics, aeronautical, aerospace, aerodynamic, aerodynamics, aerodynamically, aerosol'],['通气与有氧过程','aerate, aeration, aerobic, aerobics, aerobically, anaerobic, anaerobically']],contrasts='airline 是航空公司，airliner 是客机，aircraft 是航空器且单复数同形。aerosol 是气体中悬浮颗粒或液滴构成的体系，不能直接等同气体。aerobic 说氧的参与，不是只说空气。',practice='The airline replaced an older airliner with a more aerodynamic aircraft.\n\n这家航空公司用一架更符合空气动力学设计的飞机替换了旧客机。',words=[x['word'] for x in W]+SHARED,exclude={'aerotitis':'低频医学术语暂略','aerorrhachia':'低频医学术语暂略'})
if __name__=='__main__':
 for name,data in [('roots_aer',[ROOT]),('words_aer',W)]:Path('.cache/batch200/drafts/root/'+name+'.json').write_text(json.dumps(data,ensure_ascii=False,indent=2))
 print(len(W),sum(len(x['examples']) for x in W))
