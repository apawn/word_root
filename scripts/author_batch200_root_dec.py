# coding: utf-8
import json
from pathlib import Path
from author_batch200_root_dec_a import W as A
from author_batch200_root_dec_b import W as B
W=A+B;kept=[x['word'] for x in W]
r=next(x for x in json.loads(Path('.cache/catalog.json').read_text()) if x['id']=='C0307')
EX={w:'较冷门的计量单位、专门结构词或少用词形，本轮暂略' for w in set(r['family'])|set(r['words']) if w not in kept and '-' not in w}
ROOT=dict(id='C0307',meaning='十；十个一组',core='DEC / DECA = TEN',image='把手指全部伸开，正好十个。十年是 decade，十个比赛项目是 decathlon，十条边是 decagon。后面的成分告诉你在数什么。',intro='希腊 deka 和拉丁 decem 都表示十，可追溯到更早的印欧语“十”这一共同来源。本页主要讲希腊 deca-，同时标出 decile 的拉丁支线，不把同源的两种语言串成互相借入。',forms='deca- 在复合词里也可表现为 dec-。deca- 表十；单位前缀 deci- 表十分之一，两者方向不同。decade 的 -ade 是历史词形的一部分，不是普遍表示年的后缀。',branches=[['十年尺度','decade, decadal'],['十项比赛与选手','decathlon, decathlete'],['十个角与十足','decagon, decapod'],['拉丁同源旁支：十等分','decile']],contrasts='decade 十年；decathlon 十项比赛；decathlete 比赛的人。decile 的 top 10% 指排在前一成的人或项目，不等于拥有总量的一成。decadent 接衰落的词源，与十无关。',practice='Over the past decade, the decathlete has improved in every event.\n\n过去十年里，这位十项全能选手在每个项目上都有进步。',words=kept,exclude=EX)
if __name__=='__main__':
 for name,data in [('roots_dec',[ROOT]),('words_dec',W)]:Path('.cache/batch200/drafts/root/'+name+'.json').write_text(json.dumps(data,ensure_ascii=False,indent=2))
 print(len(W),sum(len(x['examples']) for x in W))
