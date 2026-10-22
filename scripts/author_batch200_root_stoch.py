# coding: utf-8
import json
from pathlib import Path
from lesson_authoring import entry as E
W=[E('stochastic','/stəˈkæstɪk/','随机的；包含随机因素的','结果有波动，但这些波动可以放进概率模型里讨论。','来自希腊 stokhastikos 善于猜测的，源于 stokhazesthai 瞄准、推测与 stokhos 目标。英语早期说推测，现代统计学用义又受到德语相关术语影响。',[['希腊 stokhos → stokhazesthai → stokhastikos','目标 → 瞄准、推测 → 善于推测的'],['早期英语 stochastic；后来统计学专门用法','关于推测 → 涉及随机性和概率的']],'stochastic model 会把某些变化当成随机变量处理，例如顾客何时到达、一天有多少订单。随机不等于没有规律：单次结果可能难确定，但平均值、分布或概率仍可以研究。不要直接按古义译成瞎猜的。','a stochastic process；a stochastic model；stochastic variation；stochastic simulation。','deterministic 在模型中由给定条件和规则确定结果；stochastic 模型还包含随机成分。它不自动意味着模型更好或更差。',('The researchers used a stochastic model of customer arrivals.','研究人员用一个随机模型描述顾客到达的情况。'),('The simulation includes stochastic variation in daily demand.','这项模拟考虑了每日需求的随机变化。'),sources=['https://www.etymonline.com/word/stochastic','https://en.wiktionary.org/wiki/stochastic#English','https://itl.nist.gov/div898/handbook/pmd/section2/pmd211.htm'])]
ROOT=dict(id='C1428',meaning='瞄准；推测；现代随机模型用义',core='STOCH = AIM / CONJECTURE',image='早期从瞄准目标联想到推测；现代数学把不确定变化写成概率模型。',intro='希腊 stokhos 可指目标，相关动词有瞄准、推测的意思。stochastic 的现代随机义经过学科发展形成，不是所有带这个历史材料的词都天然等于随机。',forms='stokhos → stokhazesthai → stokhastikos → stochastic。英语早期推测义与后来统计学用义分阶段理解。',branches=[['带随机性的模型和过程','stochastic']],contrasts='stochastic 不是胡乱，也不是绝对无法分析。一个过程有随机波动，并不妨碍我们研究它的概率规律。',practice='A stochastic model describes uncertainty instead of assuming that every outcome is fixed.\n\n随机模型描述不确定性，而不预设每个结果都固定不变。',words=['stochastic'],exclude={})
if __name__=='__main__':
 for name,data in [('roots_stoch',[ROOT]),('words_stoch',W)]:Path('.cache/batch200/drafts/root/'+name+'.json').write_text(json.dumps(data,ensure_ascii=False,indent=2))
 print(len(W),sum(len(x['examples']) for x in W))
