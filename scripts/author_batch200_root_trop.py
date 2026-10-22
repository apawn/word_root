# coding: utf-8
import json
from pathlib import Path
from author_batch200_root_trop_a import W as A
from author_batch200_root_trop_b import W as B
from author_batch200_root_trop_c import W as C
from author_batch200_root_trop_d import W as D,EXTRA
from author_batch200_root_trop_e import W as E
from author_batch200_root_trop_f import W as F
W=A+B+C+D+EXTRA+E+F
cat=json.loads(Path('.cache/catalog.json').read_text())
common=[x['word'] for x in A+B+C+D]+['subtropical'];science=[x['word'] for x in A+D+EXTRA+E+F]+['subtropical']
R=[]
for rid,kept in [('C1558',common),('C1544',science)]:
 r=next(x for x in cat if x['id']==rid)
 ex={w:'本轮暂略更专门的医学、生物学或材料分类术语' for w in set(r['family'])|set(r['words']) if w not in kept and '-' not in w}
 if rid=='C1544':ex['trove']='远源未定的法语寻找支线在 trop- 页单独说明，此页聚焦可明确连接的转变与方向术语'
 R.append(dict(id=rid,meaning='转；方向；方式；转变',core='TROP / TREP = TURN',image='转个方向，可以是太阳直射点折返、植物转向光，也可以是话语从字面转为比喻。科学还借它命名变化、方向和同一元素的不同形态。',intro='来自希腊 trepein“转”、tropos“方向、方式”及 tropē“转变”。词形变化不意味着每个现代词都直接从英语 trope 派生。retrieve、trove 一族的法语来源清楚，更远的希腊联系仍有争议。',forms='trop-、tropo-、trep- 保留不同形式；tropic 里的“转”关联至日，trophy 关联敌人转身败退。现代 entropy、isotropic、allotropy 是科学造词，旧根义只能帮助记忆，不能替代科学定义。',branches=([['语言与胜利','trope, trophy'],['回归线、热带与向性','tropic, tropical, subtropical, tropism'],['低层大气的变化','troposphere, tropospheric'],['法语找到、取回支线：更远来源未定','retrieve, retrieval, retriever, retrievable, irretrievable, irretrievably, trove'],['想出与创作的历史联系','contrive, contrived, contrivance, troubadour']] if rid=='C1558' else [['转向与地理','trope, trophy, tropic, tropical, subtropical, tropism'],['大气层及其边界','troposphere, tropospheric, tropopause'],['转变与状态的科学量','entropy, entropic'],['比较不同方向','isotropic, anisotropic'],['同一元素的不同结构方式','allotropy, allotrope']]),contrasts='tropical 是热带的，tropospheric 是对流层的。trope 不一定是陈词滥调；trophy 是奖品或胜利纪念物。科学里的熵、各向同性和同素异形，都要结合实际概念理解，不能只翻译词根。',practice='The class discussed tropical weather, the troposphere, and the turning point behind the word tropic.\n\n全班讨论了热带天气、对流层，以及 tropic 一词背后的折返含义。',words=kept,exclude=ex))
if __name__=='__main__':
 for name,data in [('roots_trop',R),('words_trop',W)]:Path('.cache/batch200/drafts/root/'+name+'.json').write_text(json.dumps(data,ensure_ascii=False,indent=2))
 print(len(R),len(W),sum(len(x['examples']) for x in W))
