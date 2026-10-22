# -*- coding: utf-8 -*-
"""C0328 dida: common lessons shared with auto family."""
import json
from pathlib import Path
BASE=Path(__file__).resolve().parents[1];OUT=BASE/'.cache/batch200/drafts/rewrite_vid';W=[]
names=['didactic','autodidact'];cat=next(x for x in json.loads((BASE/'.cache/catalog.json').read_text()) if x['id']=='C0328');EX={w:'较冷门的施教者称呼或早期基督教书名，按当前通用阅读范围暂略。' for w in cat['family'] if w not in names}
ROOT=dict(id='C0328',meaning='教；教会',core='dida-／didact- 接希腊“教”这一族。一个方向是把道理讲给别人，另一个方向是自己把自己教会。',image='didaskein 教 → didaktos 被教会的 → didactic 教导性的；autos 自己 + didaktos → autodidact 自学者。',intro='didactic 常出现在文学或影视评论里，autodidact 则说学习路径。记住“教会”这个动作，比把字母看成英语 did 更有帮助。',forms='didactic 接希腊 didaktikos，经拉丁化及法语背景借入；autodidact 的 auto- 是“自己”，结合被教会的 didaktos，形成自学这一意象。',branches=[['教别人、自己学','didactic, autodidact']],contrasts='didactic 可以中性表示教导目的，也可批评说教；autodidact 不等于业余人士，更不表示从未上过任何学校。',practice='用 didactic 描述一篇目的在于教道理的故事，用 autodidact 描述一个在特定领域主要靠自学的人。',words=names,exclude=EX)
if __name__=='__main__':
 for kind,data in [('roots',[ROOT]),('words',W)]: (OUT/(kind+'_batch200_vid_226.json')).write_text(json.dumps(data,ensure_ascii=False,indent=2))
 print('dida: 0 new; 2 shared')
