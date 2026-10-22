# coding: utf-8
import json
from pathlib import Path
from author_batch200_root_calc_a import W as A
from author_batch200_root_calc_b import W as B
from author_batch200_root_calc_c import W as C
from author_batch200_root_calc_d import W as D
W=A+B+C+D;kept=[x['word'] for x in W]+['miscalculation']
r=next(x for x in json.loads(Path('.cache/catalog.json').read_text()) if x['id']=='C0158')
EX={w:'较冷门古生物名称，本轮暂略' for w in set(r['family'])|set(r['words']) if w not in kept and '-' not in w}
for w in ['calcitrant','recalcitrant']:EX[w]='来自另一个 calx“脚跟”，不是石灰、石头这一词根，纠正原表误归'
ROOT=dict(id='C0158',meaning='石灰、石灰石；小石子 → 计数',core='CALC = STONE → COUNTING WITH PEBBLES',image='桌上摆几颗小石子，每颗代表一件东西。石子一边仍是石灰石、白垩，一边作为筹码进入了计算的世界。',intro='拉丁 calx 的石灰义与希腊 khalix“小石子”有历史联系；更早来源不强行定论。拉丁 calculus 是小石子，又能指计数筹码，随后 calculare 表计算。不是先有现代微积分，才有 calculate。',forms='calc- 保留在 calcium、calcite、calcify 中；calcul- 走计算支线。chalk 经日耳曼语和古英语传下来，外形改变较大。calculation、calculator 是各自借入的历史词，现代后缀分析不等于借入先后。',branches=[['计算、工具与学科','calculate, calculation, calculator, calculus'],['估算、重算与算错','calculated, calculating, calculable, incalculable, recalculate, miscalculate, miscalculation'],['白垩与书写','chalk, chalkboard, chalky'],['钙与矿物','calcium, calcite, calcify, calcification']],contrasts='calculate 算，calculating 作性格词是算计，calculated risk 是权衡后的冒险。calculation 是计算，calcification 是钙化。recalcitrant“不服管的”来自另一个 calx“脚跟”：像马向后踢，而非石头太硬；因此不混入本词族。',practice='She used a calculator to check the calculation, then wrote the answer in chalk on the chalkboard.\n\n她用计算器核对了计算结果，然后用粉笔把答案写在黑板上。',words=kept,exclude=EX)
if __name__=='__main__':
 for name,data in [('roots_calc',[ROOT]),('words_calc',W)]:Path('.cache/batch200/drafts/root/'+name+'.json').write_text(json.dumps(data,ensure_ascii=False,indent=2))
 print(len(W),sum(len(x['examples']) for x in W))
