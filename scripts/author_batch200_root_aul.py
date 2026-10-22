# coding: utf-8
import json
from pathlib import Path
ROOT=dict(id='C0098',meaning='管；管状乐器',core='AUL = PIPE',image='一根空心管让空气或液体沿着固定路线移动。hydraulic 的后半段就藏着这个管的意象。',intro='希腊 aulos 表示管或管状乐器。这个小词族最实用的是 hydraulic 一组：名称在古代与水力风琴相关，后来扩展到水力、液体流动及液压技术。',forms='hydr- 水 + aulos 管，形成希腊 hydraulikos，经过拉丁 hydraulicus、法语 hydraulique 进入英语 hydraulic。hydraulics 与 hydraulically 再分别说明技术领域和运作方式。',branches=[['设备或作用的性质','hydraulic'],['学科与实际系统','hydraulics'],['动作怎样完成','hydraulically']],contrasts='词源里的水不限定现代系统只能用水，液压油也可传递压力。hydraulic 也不等于设备放在水里；pneumatic 主要借气体工作，与液压分开。古代乐器名称帮助说明借入历史，不必把现代液压机械想成在演奏音乐。',practice='The engineer studies hydraulics and designs hydraulically operated doors.\n\n这位工程师研究液压技术，并设计由液压装置操作的门。',words=['hydraulic','hydraulics','hydraulically'],exclude={w:'古代乐器及其演奏者的专门名称，本轮先保留常见 hydraulic 一组。' for w in ['aulos','aulete','hydraulus']})
if __name__=='__main__':
 Path('.cache/batch200/drafts/root/roots_aul.json').write_text(json.dumps([ROOT],ensure_ascii=False,indent=2))
 print('1 root; 3 shared words')
