# -*- coding: utf-8 -*-
"""C0062 apo: moving away, removing, and historically changed meanings."""
import json
from pathlib import Path
BASE=Path(__file__).resolve().parents[1];OUT=BASE/'.cache/batch200/drafts/rewrite_vid'
W=[]
SH=['apology','apologize','apostle','apocalypse','apocalyptic','apocryphal','apostasy','apostate','apogee','aphelion']
EX={w:'专门生化、解剖或旧病理术语，按当前常用阅读范围暂略。' for w in ['apolipoprotein','apocrine','aporrhinosis']}
ROOT=dict(id='C0062',meaning='从、离开、远离；分开、除去',core='apo- 最好先想成“从原处离开”。它可以把人派出去、让某人脱离原来的信仰，也能把覆盖物拿走；具体意义要看它和什么词组合。',image='向外派出 → apostle 使徒；脱离原来位置 → apostasy；拿走覆盖 → apocalypse；远离地球／太阳 → apogee／aphelion。',intro='这不是一个能机械替换成“离开”的密码。apology 的历史走向申辩再到道歉，apocalypse 从揭示发展出末世与灾难义，都需要跟着完整词的使用历史理解。',forms='希腊 apo 在元音前常为 ap-；与不同音结合还可能见 aph-，如 aphelion 的历史构词。它有离开、来源等多种用法。英语既借入古代完整词，也用其构件创造近代科学名称。',branches=[['回应与申辩的历史','apology, apologize'],['向外派出的使者','apostle'],['揭示、隐秘与文本','apocalypse, apocalyptic, apocryphal'],['脱离原先信仰或立场','apostasy, apostate'],['轨道的远点','apogee, aphelion']],contrasts='apocalypse 原本是揭开，不是 apo- 自带“世界末日”。apocryphal 现代常说故事真实性存疑，也不能只凭 hidden 的历史义译成保密。apogee 与 aphelion 分别围绕地球和太阳，参照对象不同。',practice='把使者派走、把覆盖拿开、把距离拉远，分别帮助记 apostle、apocalypse 和 apogee。再看 apology 的完整历史，接受有些词的现代意思不能只靠逐字相加猜出。',words=SH,exclude=EX)
if __name__=='__main__':
 m=json.loads((BASE/'.cache/batch200/rewrite_vid.json').read_text());r=next(x for x in m['roots'] if x['id']==ROOT['id'])
 assert {w for w in r['family'] if '-' not in w}<=set(ROOT['words'])|set(EX)
 for kind,data in [('roots',[ROOT]),('words',W)]: (OUT/(kind+'_batch200_vid_159.json')).write_text(json.dumps(data,ensure_ascii=False,indent=2))
 print('apo:',len(SH),'shared references')
