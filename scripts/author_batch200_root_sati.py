# coding: utf-8
import json
from pathlib import Path
from author_batch200_root_sati_a import W as A
from author_batch200_root_sati_b import W as B
W=A+B
ROOT=dict(id='C1262',meaning='足够、填满、满足',core='SATI = ENOUGH / FULL',image='一只空碗不断添东西：够用了是 satisfy，填到满是 saturate，怎么填都不够是 insatiable。这个画面帮助理解意义，不能替代每个词实际走过的历史路线。',intro='从拉丁 satis“足够”出发，最实用的问题是“谁觉得够了，什么东西被填满了”。人满意、条件达标、胃口饱足和市场饱和，是不同对象上的够与满。asset 看不出这几个字母，却通过法语“足够的财产”与这一族相连；sate 的英语继承路线则不同。',forms='satisfy 的历史结构是 satis + facere“做”：做得足够。satisfaction、satisfactory 保留 satisfact- 一支。satiate 接 satiare“填满”，saturate 接 satur“满的”。asset 从 assets 反推单数，不是 as + set。sate 要另看日耳曼继承与后来受拉丁同义词影响的路线。',branches=[['满足需求、达到标准','satisfy, satisfied, satisfying, satisfaction, satisfactory, satisfactorily'],['不满与尚未满足','dissatisfied, dissatisfaction, unsatisfied, unsatisfactory'],['把胃口填够','sate, satiate, satiated, satiety, insatiable'],['浸透与饱和','saturate, saturated, saturation, unsaturated'],['足够清偿义务的家底','asset']],contrasts='satisfying 让人有满足感，satisfactory 达到要求；dissatisfied 多强调对结果不满，unsatisfied 多强调需要还没被满足，二者并非绝对互斥。insatiable 是很难填满的胃口。saturate 可以用海绵记，但脂肪的饱和要按化学结构理解。',practice='The result was satisfactory, but the work itself was not satisfying. Her curiosity remained unsatisfied.\n\n结果达到了要求，但工作本身没有带来多少满足感。她的好奇心仍未得到解答。',words=[w['word'] for w in W],exclude={})
if __name__=='__main__':
 for name,data in [('roots_sati',[ROOT]),('words_sati',W)]:Path('.cache/batch200/drafts/root/'+name+'.json').write_text(json.dumps(data,ensure_ascii=False,indent=2))
 print(len(W),sum(len(w['examples']) for w in W))
