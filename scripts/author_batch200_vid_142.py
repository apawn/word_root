# -*- coding: utf-8 -*-
"""C1339 sigm: a letter name, its mathematical uses, and its shapes."""
import json
from pathlib import Path
from lesson_authoring import entry as E
BASE=Path(__file__).resolve().parents[1];OUT=BASE/'.cache/batch200/drafts/rewrite_vid'
W=[E('sigma','/ˈsɪɡmə/','希腊字母 sigma；常见求和、标准差符号的名称','先把它看成一个字母名，就像英语里的 S 有自己的名称。数学再借这个字母来当符号；大小写不同，约定的用途也不同。','英语借入希腊字母名 sigma。更早的字母名称来源有不同分析，这里从可靠的希腊字母名讲起，不把它硬拆成英语小词。',[['希腊字母名 sigma','现代希腊字母表的第十八个字母，常见大写 Σ、小写 σ'],['英语 sigma','用来称呼这个字母；也用于读出数学中的相应符号']],'大写 Σ 常表示“把这些项加起来”；小写 σ 在统计学里常表示总体标准差，也就是一组数围着平均值分散得有多开。这些是约定用途，不能见到任何 σ 都不看定义就认定是标准差。','capital sigma；lowercase sigma；sigma notation。sigma notation 是用 Σ 来简写连加式的记法。','Σ 和 σ 是同一字母的大写、小写，但不能在公式里随意互换。sigmoid 则借用了字形相似的意思，现代常说 S 形，并不表示“求和形”。',('The capital sigma tells us to add all the terms in the list.','大写 sigma 告诉我们把表中的各项加起来。'),('In this formula, lowercase sigma represents the population standard deviation.','在这个公式里，小写 sigma 表示总体标准差。'),sources=['https://www.oxfordlearnersdictionaries.com/definition/english/sigma','https://www.etymonline.com/word/sigma','https://mathworld.wolfram.com/SigmaNotation.html','https://www.nist.gov/calibrations/upload/exp_meas.pdf'])]
SH={'sigmoid'};EX={w:'专门的语音障碍、化学反应或内镜检查名称，本轮优先保留字母及常见数学形状用法。' for w in ['sigmatism','sigmatropic','sigmoidoscopy']}
ROOT=dict(id='C1339',meaning='希腊字母 sigma；由字形联想到弯曲形状',core='这一组先是一个字母名，不是一项抽象动作。数学借它做符号，形态命名又借它的某些历史字形来形容弯曲。',image='希腊 sigma 字母名 → 英语 sigma；sigma 的历史字形 + 像……的 → sigmoid，现代常说 S 形。',intro='学会 sigma 后，能听懂公式里的“西格玛”，也能理解 sigmoid 为什么与曲线形状有关。求和与标准差是符号约定，S 形则是外观联想，是两种不同用法。',forms='sigma 是字母名；组合形式可见 sigm-、sigmat-。sigmoid 与希腊 sigmoeidēs“像 sigma 的”相连；字母曾有 C 状等写法，不能只拿现代印刷体大写 Σ 去硬比。',branches=[['字母与数学符号','sigma'],['形状与常用专门表达','sigmoid']],contrasts='大写 Σ 常作求和号，小写 σ 常作标准差符号，但每个公式仍以自己的定义为准。sigmoid 的形状义与这些数学符号用途不是同一条词义变化。',practice='Read the capital sigma as a summation sign; describe the S-shaped graph as a sigmoid curve. 一个是运算符号，一个是外形。',words=[],exclude=EX)
if __name__=='__main__':
 m=json.loads((BASE/'.cache/batch200/rewrite_vid.json').read_text());r=next(x for x in m['roots'] if x['id']==ROOT['id']);ROOT['words']=[w for w in r['family'] if '-' not in w and w not in EX]
 assert set(ROOT['words'])=={e['word'] for e in W}|SH
 assert {e['word'] for e in W}<=set(m['owned_words'])
 for kind,data in [('roots',[ROOT]),('words',W)]: (OUT/(kind+'_batch200_vid_142.json')).write_text(json.dumps(data,ensure_ascii=False,indent=2))
 print('sigm:',len(W),'words;',sum(len(e['examples']) for e in W),'examples')
