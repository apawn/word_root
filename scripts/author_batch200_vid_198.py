# -*- coding: utf-8 -*-
"""C1559 troph: nourishment, food webs, and tissue changes."""
import json
from pathlib import Path
from lesson_authoring import entry as E
BASE=Path(__file__).resolve().parents[1];OUT=BASE/'.cache/batch200/drafts/rewrite_vid'
W=[]  # All four retained words already have authored records.
m=json.loads((BASE/'.cache/batch200/rewrite_vid.json').read_text());names=['trophic','dystrophy','atrophy','hypertrophy']
cat=next(x for x in json.loads((BASE/'.cache/catalog.json').read_text()) if x['id']=='C1559')
EX={w:'罕见胡须养护或生长术语，按当前通用阅读范围暂略。' for w in cat['family'] if w not in names}
ROOT=dict(id='C1559',meaning='食物、滋养、使生长',core='troph- 接希腊 trophē“食物、滋养”，关联 trephein“养育、使生长”。从谁给谁提供营养，延伸到组织怎样维持和生长。',image='trophē 滋养 → trophic 营养关系；a- + trophia → atrophy 萎缩；dys- + trophia → dystrophy 异常退变；hyper- + trophia → hypertrophy 肥大。',intro='生态学用它看食物网，医学用它命名组织变化。词根帮助理解命名视角，却不能单凭“营养”两个字推断病因。',forms='trophic 接希腊 trophikos，也有法语 trophique 借入路线；dystrophy 接现代拉丁 dystrophia；atrophy、hypertrophy 各保留独立借入和构词历史。',branches=[['食物与滋养关系','trophic'],['组织异常、缩小与增大','dystrophy, atrophy, hypertrophy']],contrasts='muscular dystrophy 不是普通饮食不足。英语 trophy“奖杯”接另一套“转向、战利品”的历史，不是营养词根的独立名词。',practice='用食物网理解 trophic level，再分别区分 atrophy 的缩小、hypertrophy 的肥大与 dystrophy 的异常退变。',words=names,exclude=EX)
if __name__=='__main__':
 assert {e['word'] for e in W}<=set(m['owned_words'])
 for kind,data in [('roots',[ROOT]),('words',W)]: (OUT/(kind+'_batch200_vid_198.json')).write_text(json.dumps(data,ensure_ascii=False,indent=2))
 print('troph:',len(W),'words;',sum(len(e['examples']) for e in W),'examples')
