# coding: utf-8
import json
from pathlib import Path
from author_batch200_root_optim_a import W as A
from author_batch200_root_optim_b import W as B
W=A+B
ROOT=dict(id='C0907',meaning='最好；最佳',core='OPTIM = BEST',image='想象一排温度旋钮，圈出最适合当前任务的那个档位：最佳不是无限调高。另一条支线把“最好”放进看世界的态度里，形成乐观。',intro='可靠的共同来源是拉丁 optimus“最好”，其中性形式是 optimum。“最佳状态”进入科学用语；近代关于“最佳可能世界”的哲学讨论，经法语 optimisme、optimiste，发展成英语的乐观词族。两条支线同源，但不是每个英语词都由另一个英语词直接派生。',forms='optimal 是最佳的，optimum 可作名词或形容词；optimize/optimise 是优化。optimism 是乐观态度，optimist 是人，optimistic 是形容词。-ize/-ise 及 -ization/-isation 属拼写变体。opt- 选择与 optic 视觉不要因字母接近就混入本组。',branches=[['最佳点与最佳状态','optimum, optimal, optimally, optimality, suboptimal'],['调到更合适','optimize, optimise, optimization, optimisation, optimized, optimised, optimizer'],['倾向相信好结果','optimism, optimist, optimistic, optimistically']],contrasts='最佳必须有参照目标：最省时间的方案可能更费钱。optimized 只说经过优化，optimal 才说最佳；optimistic 则是乐观的，不是最佳的。optimize 的早期词史联系乐观词族，不能简单画成较晚的 optimal 直接生出 optimize。',practice='The optimist believes we can optimize the plan, but we still need evidence that the result is optimal.\n\n这个乐观的人相信我们能优化方案，但我们仍需要证据，说明结果确实是最佳的。',words=[x['word'] for x in W]+['suboptimal'],exclude={})
if __name__=='__main__':
 for name,data in [('roots_optim',[ROOT]),('words_optim',W)]:Path('.cache/batch200/drafts/root/'+name+'.json').write_text(json.dumps(data,ensure_ascii=False,indent=2))
 print(len(W),sum(len(x['examples']) for x in W))
