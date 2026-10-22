# coding: utf-8
import json
from pathlib import Path
from author_batch200_root_hyper_a import W as A
from author_batch200_root_hyper_b import W as B
W=A+B
SHARED=['hypertension','hyperbolic','hyperbole','hyperactivity','hyperspace','hypertext','hypersensitive','hyperthermia','hypermarket','hyperbola']
EX={w:'专门或低收益术语暂略' for w in ['hyperplasia','hypertensive','hyperbaric','hyperloop','hypercube','hypertonic','hyperoxia','hyperpyrexia','Hyperion']}
ROOT=dict(id='C0583',meaning='超过；过量；在上',core='HYPER = OVER / BEYOND / EXCESSIVE',image='想象一个旋钮被拧过通常范围：活跃过头、反应过强、某项数值过高。另一些科技词把“超出”用来表示超出传统文本或普通空间的范围。',intro='来自希腊 hyper，表示在上、越过、超过。现代常见 hyper- 表过量，如 hyperactive；但 hyperlink、hypertext 等沿超文本概念发展，不能都硬译成“过度”。hyper 单独作口语形容词多缩自 hyperactive。',forms='hyper- 常表示过量或超出，hypo- 常表示不足或在下。hyperglycemia 中 -emia 表血液状态，hyperthyroidism 中 -ism 表状态；这些现代术语使用古典构词材料，不代表整词在古希腊时代已经存在。',branches=[['精力和反应过强','hyper, hyperactive, hyperactivity, hypersensitive, hypersensitivity'],['数值、组织或生理过程过度','hypertension, hypertrophy, hyperthyroidism, hyperglycemia, hyperpigmentation, hyperventilation, hyperventilate, hyperthermia'],['经济、速度与科技','hyperinflation, hypersonic, hyperlink, hypertext, hyperdrive, hyperspace, hypermarket'],['夸张及几何术语','hyperbole, hyperbolic, hyperbola']],contrasts='hyper- 与 hypo- 的方向常相反。hypersonic 说高速飞行，hyperdrive 通常是科幻驱动；hyperlink 的“超”不是过度。临床词的拆分帮助读懂名称，不单独构成诊断。',practice='The hyperactive character clicks every hyperlink and imagines a spaceship with a hyperdrive.\n\n这个精力过盛的角色点开每个超链接，脑中还想象着一艘装有超空间驱动的飞船。',words=[x['word'] for x in W]+SHARED,exclude=EX)
if __name__=='__main__':
 for name,data in [('roots_hyper',[ROOT]),('words_hyper',W)]:Path('.cache/batch200/drafts/root/'+name+'.json').write_text(json.dumps(data,ensure_ascii=False,indent=2))
 print(len(W),sum(len(x['examples']) for x in W))
