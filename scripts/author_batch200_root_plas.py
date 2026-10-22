# coding: utf-8
import json
from pathlib import Path
from author_batch200_root_plas_a import W as A
from author_batch200_root_plas_b import W as B
W=A+B;kept=[w['word'] for w in W]+['protoplasm']
r=next(x for x in json.loads(Path('.cache/catalog.json').read_text()) if x['id']=='C1059')
EX={w:'较冷门的材料、细胞或医学术语，本轮暂略' for w in set(r['family'])|set(r['words']) if w not in kept and '-' not in w}
ROOT=dict(id='C1059',meaning='捏塑、塑成形；被形成的物质',core='PLAS / PLAST = MOLD, FORM',image='手里一团软泥被捏成新形状，是这一组最容易抓住的画面。plastic 保留可塑，plaster 保留涂抹覆盖；plasma 和 plasmid 则进入了需要单独学习的科学命名。',intro='希腊 plassein 表捏塑、使成形。plastos 是塑成的，plasma 是被形成之物。塑料只是 plastic 后来最常见的意思，不能拿现代塑料倒过来解释全部同源词。',forms='plas-、plast-、plasm- 对应相关的希腊词形。plastic 接 -ity 成 plasticity，neuro- 再限定为神经可塑性；plaster 的历史借入路线独立。plasmid 是现代术语，protoplasm 是原生质的科学名称。',branches=[['可塑与塑料','plastic, plasticity, thermoplastic, plasticine'],['神经系统能改变','neuroplasticity'],['涂抹、覆盖与贴满','plaster, plastered'],['专业命名的不同分支','plasma, plasmid, protoplasm']],contrasts='plasticity 不等于 elasticity；能留下新形状与会弹回原样是两回事。plasma 的血浆义和等离子体义必须看学科语境。plaster、plasticine、plastic 是不同材料名，不是拼写变体。',practice='The sculptor shaped a plasticine model before making a plaster cast.\n\n雕塑家先捏出橡皮泥模型，再制作石膏翻模。',words=kept,exclude=EX)
if __name__=='__main__':
 for name,data in [('roots_plas',[ROOT]),('words_plas',W)]:Path('.cache/batch200/drafts/root/'+name+'.json').write_text(json.dumps(data,ensure_ascii=False,indent=2))
 print(len(W),sum(len(w['examples']) for w in W))
