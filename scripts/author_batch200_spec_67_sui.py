# -*- coding: utf-8 -*-
from pathlib import Path
import json
BASE=Path(__file__).resolve().parents[1];OUT=BASE/'.cache/batch200/drafts/rewrite_spec'
m=json.loads((BASE/'.cache/batch200/rewrite_spec.json').read_text());family=next(r['family'] for r in m['roots'] if r['id']=='C1451')
ROOT=[dict(id='C1451',meaning='自己的；指回自己',core='sui-：把动作的对象指回自己，而不是另一个人。',image='拉丁 sui 是“自己的”；与表示杀害的 -cide 结合，构成 suicide，再加 -al 得 suicidal。',intro='sui 原是拉丁反身代词 sē 的属格形式，意思是“自己的”。它不像 auto- 那样在现代英语里广泛造词，但 suicide 及其形容词是新闻与公共健康阅读中需要准确理解的常用词。',forms='suicide 是近代用拉丁构件形成的词，英语与近代拉丁 suicidium 的先后有不同分析；不能把它当作古罗马时代原封不动传下来的单词。suicidal 是英语 suicide 加 -al。',branches=[['行为名词','suicide'],['相关形容词','suicidal']],contrasts='suicidal thoughts 指自杀想法，不等于必然行动。political suicide 等是比喻说法，不应直接据此判断一个人有真实自杀意图。suit、suite 不属于 sui 这条来源。',practice='在新闻中分清 suicide prevention 的实际公共健康含义，与 political suicide 的比喻义；再辨别名词 suicide 和形容词 suicidal 的句中位置。',words=list(family),exclude={'sui generis':'含空格的拉丁短语，按当前单词范围暂略。'},sources=['https://www.etymonline.com/word/suicide','https://www.etymonline.com/word/suicidal'])]
assert set(family)=={'suicide','suicidal'}
for k,d in [('roots',ROOT),('words',[])]: (OUT/f'{k}_batch200_spec_67_sui.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
print('C1451 0 new 2 shared')
