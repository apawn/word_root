# -*- coding: utf-8 -*-
"""C0635 klept: shared lessons, keeping political metaphor separate from diagnosis."""
import json
from pathlib import Path
BASE=Path(__file__).resolve().parents[1];OUT=BASE/'.cache/batch200/drafts/rewrite_vid'
W=[]
cat=next(x for x in json.loads((BASE/'.cache/catalog.json').read_text()) if x['id']=='C0635');names=['kleptocracy','kleptomania']
EX={w:'较冷门的恐惧症名称或细胞器借用现象术语，按当前通用阅读范围暂略。' for w in cat['family'] if w not in names}
ROOT=dict(id='C0635',meaning='偷窃；盗取',core='klept-／klepto- 接希腊 kleptein“偷”。接上统治，形容公权力被用来掠夺财富；接上冲动问题的命名成分，便进入另一个医学语境。',image='偷窃 kleptein → klepto- + -cracy 盗贼统治；klepto- + -mania 偷窃癖。',intro='这两个常见阅读词共享“偷”的材料，但一个是政治批评，一个是临床概念。不能用其中一个替另一个下判断。',forms='kleptocracy 与 kleptomania 都是近代借希腊来源的成分构成；前者结合权力、治理，后者结合 -mania。不是古希腊时代已有现代政治或临床分类。',branches=[['把公权力用于掠夺财富','kleptocracy'],['反复偷窃冲动的临床名称','kleptomania']],contrasts='kleptocracy 是对统治方式的批评，不是统治者患某种病的诊断。kleptomania 也不是任何偷窃行为都适用的标签。',practice='先判断语境是在谈公共财富和统治，还是在谈一种特定冲动问题，再选择对应词。',words=names,exclude=EX)
if __name__=='__main__':
 for kind,data in [('roots',[ROOT]),('words',W)]: (OUT/(kind+'_batch200_vid_215.json')).write_text(json.dumps(data,ensure_ascii=False,indent=2))
 print('klept: 0 new words; 2 shared')
