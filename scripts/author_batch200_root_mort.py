# coding: utf-8
import json
from pathlib import Path
from author_batch200_root_mort_a import W as A
from author_batch200_root_mort_b import W as B
from author_batch200_root_mort_c import W as C
W=A+B+C;kept=[x['word'] for x in W]
r=next(x for x in json.loads(Path('.cache/catalog.json').read_text()) if x['id']=='C0768')
EX={w:'本轮暂略法医等专门语境或极低频词' for w in set(r['family'])|set(r['words']) if w not in kept and '-' not in w}
ROOT=dict(id='C0768',meaning='死；生命的终点',core='MORT = DEATH',image='一条生命线走到终点，是 mortal；加否定前缀后，immortal 把终点拿掉。作品让名字仿佛一直活着；mortified 则把尊严受挫说得像被击垮。',intro='来自拉丁 mors“死亡”，变格词干 mort-；同族还有 mori“死”、mortuus“死去的”。有的词直接谈生命终点，有的转向名声、羞耻等比喻；mortgage 还保留了一段古法语法律命名史。',forms='mort-、mortal-、mortu- 是相关形式。im- 在 immortal 中是否定；-ify 在 mortify 中追溯到 facere“使”；mortgage 的 gage 是抵押，不能拆成现代英语 age。',branches=[['生命有限与死亡统计','mortal, mortality, mortally'],['长生与被长久记住','immortal, immortality, immortalize, immortalise'],['尊严仿佛被击垮','mortify, mortified, mortifying, mortification'],['与逝者有关的设施和工作','mortuary, mortician'],['保留古代命名的抵押贷款','mortgage']],contrasts='mortal 与 moral“道德的”不同；mortality 关注死亡，morbidity 关注疾病。mortified 通常是羞窘，不是身体已经死亡。mortgage 的现代含义要整体掌握，历史比喻不是现代合同规则。',practice='The mortal artist hoped that her paintings would immortalize the people she loved.\n\n这位终有一死的艺术家，希望自己的画能让所爱之人的形象长久流传。',words=kept,exclude=EX)
if __name__=='__main__':
 for name,data in [('roots_mort',[ROOT]),('words_mort',W)]:Path('.cache/batch200/drafts/root/'+name+'.json').write_text(json.dumps(data,ensure_ascii=False,indent=2))
 print(len(W),sum(len(x['examples']) for x in W))
