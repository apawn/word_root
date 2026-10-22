# -*- coding: utf-8 -*-
"""C1419 steth: reuse the fully authored stethoscope lesson."""
import json
from pathlib import Path
BASE=Path(__file__).resolve().parents[1];OUT=BASE/'.cache/batch200/drafts/rewrite_vid'
W=[]
ROOT=dict(id='C1419',meaning='胸部',core='steth- 接希腊 stēthos“胸部”。stethoscope 的命名画面，就是借工具检查胸部。',image='希腊 stēthos 胸部 + 检查、观察成分 → 法语 stéthoscope → 英语 stethoscope。',intro='听诊器让医生听见胸内的声音。-scope 的“观察、检查”不必只理解成用眼看，声音同样可以提供信息。',forms='stethoscope 是法语先形成的医学工具名，再借入英语；steth- 与 -scope 是命名材料，不是把两个现成英语单词直接连接。',branches=[['用于检查身体声音的工具','stethoscope']],contrasts='名称从胸部检查来，现代听诊器也可用于其他部位；instrument 的实际用途可以比最初名称更广。',practice='把 stethoscope 解释成“检查胸部的工具”，再补一句：这种检查是借助听到的声音。',words=['stethoscope'],exclude={})
if __name__=='__main__':
 for kind,data in [('roots',[ROOT]),('words',W)]: (OUT/(kind+'_batch200_vid_212.json')).write_text(json.dumps(data,ensure_ascii=False,indent=2))
 print('steth: 0 new words; 1 shared')
