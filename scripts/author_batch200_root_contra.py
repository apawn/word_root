# coding: utf-8
import json
from pathlib import Path
from author_batch200_root_contra_a import W as A
from author_batch200_root_contra_b import W as B
W=A+B
SH=['contrast','contradictory','contrasting','contradict','contrasted','contravene','contrastive','controversy','controversial']
ROOT=dict(id='C0250',meaning='对面、相反、反对',core='CONTRA = AGAINST, OPPOSITE',image='把两个方向相对摆开：话说反了是 contradict，事物的差别相对显出来是 contrast，身体相反一侧是 contralateral。到了规则和医学语境，则出现违反禁令或不宜采用的含义。',intro='拉丁 contra 原本表示在对面、相反，也可表示反对。英语中一部分词沿法语、意大利语等路线借入，一部分是现代用 contra- 重新组合；不能把同一词头都想成同一种动作。',forms='contra- 较完整地出现在 contraception、contralateral、contraindication 中；contrast、controversy 等词里的形式经历了各自的借入历史。con- 通常与 together 一支有关，不能见到 contr- 就删成 con- 再解释。',branches=[['话或观点相冲','contradict, contradictory, controversy, controversial'],['通过相对照显出差别','contrast, contrasting, contrasted, contrastive'],['与规则相抵触','contravene, contraband'],['预防受孕','contraception, contraceptive'],['位置在相反一侧','contralateral'],['有理由不采用某治疗','contraindicate, contraindication']],contrasts='contrast 不一定是矛盾，contradict 才是话或证据相抵触。contraband 不等于假货。contraindication 是治疗决策中的禁忌理由，不能与 side effect 混为一谈。',practice='The two reports contrast sharply, but a difference in emphasis does not always mean they contradict each other.\n\n这两份报告形成鲜明对比，但侧重点不同并不总意味着它们相互矛盾。',words=[w['word'] for w in W]+SH,exclude={})
if __name__=='__main__':
 for name,data in [('roots_contra',[ROOT]),('words_contra',W)]:Path('.cache/batch200/drafts/root/'+name+'.json').write_text(json.dumps(data,ensure_ascii=False,indent=2))
 print(len(W),sum(len(w['examples']) for w in W))
