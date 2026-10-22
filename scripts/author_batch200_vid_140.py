# -*- coding: utf-8 -*-
"""C0835 nox: harm and objectionability, linked to already authored noc words."""
import json
from pathlib import Path
BASE=Path(__file__).resolve().parents[1];OUT=BASE/'.cache/batch200/drafts/rewrite_vid'
W=[];SH={'noxious','obnoxious','obnoxiously','innocuous'};EX={}
ROOT=dict(id='C0835',meaning='损害、伤害',core='最初是伤害、损害这类实际后果。noxious 常说有害的物质；obnoxious 今天更常说一个人或行为特别惹人厌烦。',image='拉丁 noxa 损害，关联 nocere 伤害 → noxius → noxious；obnoxius 受制、易受害 → obnoxious 后来变为讨厌的；相关 nocuus 加否定 → innocuous 无害的。',intro='这一页最值得分清的是 noxious 和 obnoxious：有害烟气可以是 noxious fumes，粗鲁烦人的举止可以是 obnoxious behaviour。不能因为只差两个字母，就当作同程度的同义词。',forms='nox- 接拉丁名词 noxa“损害”，与 nocere“伤害”相连。obnoxious 的拉丁前身曾有受制于、暴露于损害的意思，英语后来转向令人反感的方向；innocuous 则沿相关 noc- 词干表示无害。',branches=[['造成损害与没有损害','noxious, innocuous'],['令人反感的态度和行为','obnoxious, obnoxiously']],contrasts='noxious 通常评价有害性，obnoxious 常评价令人反感的社交表现；两者也可有比喻用法。innocuous 是无害、不冒犯，含否定前缀；拉丁 nox“夜晚”是另一词，不属于这里的伤害词根。',practice='The fumes were noxious, and the visitor’s jokes were obnoxious. 烟气有害，那位访客的笑话则让人反感：一个着重损害，一个着重惹人讨厌。',words=[],exclude=EX)
if __name__=='__main__':
 m=json.loads((BASE/'.cache/batch200/rewrite_vid.json').read_text());r=next(x for x in m['roots'] if x['id']==ROOT['id']);ROOT['words']=[w for w in r['family'] if '-' not in w];ROOT['words']+=sorted(SH-set(ROOT['words']))
 assert set(ROOT['words'])==SH
 for kind,data in [('roots',[ROOT]),('words',W)]: (OUT/(kind+'_batch200_vid_140.json')).write_text(json.dumps(data,ensure_ascii=False,indent=2))
 print('nox:',len(ROOT['words']),'shared references')
