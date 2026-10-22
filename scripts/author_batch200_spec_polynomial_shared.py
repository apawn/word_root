# -*- coding: utf-8 -*-
from pathlib import Path
import json
from lesson_authoring import entry as E
BASE=Path(__file__).resolve().parents[1];OUT=BASE/'.cache/batch200/drafts/rewrite_spec'
W=[E('polynomial','英 /ˌpɒlɪˈnəʊmiəl/；美 /ˌpɑːliˈnoʊmiəl/','多项式；多项式的','把有限个合乎规则的代数项相加，得到的一类式子。','poly-“多” + -nomial，仿照 binomial 构成。主流词源把 binomial 接到拉丁 nomen“名字、名目”；另有希腊 nomos“份额、部分”的分析，但不能因此直接并入 nomos“法则”词族。',[['拉丁语 nomen → binomius；英语 binomial','名字、名目 → 有两个名目；数学中指二项式'],['英语 poly- + -nomial → polynomial','仿二项式名称形成的多项式名称']],'例如 2x² + 3x + 1，有三项：2x²、3x、1。变量的指数必须是非负整数，项数有限；所以 1/x 不是关于 x 的 polynomial。英语数学定义也包括只有一项的情形，不能因为 poly 表“多”就硬性要求至少两项。','a polynomial in x；a quadratic polynomial；a polynomial function；factor a polynomial。','项数和次数不同：2x² + 3x + 1 有三项，但最高次数是 2。polynomial 是式子；把它设为零，例如 x² − 1 = 0，才得到相应的 polynomial equation。',('The polynomial x² + 2x + 1 can be written as (x + 1)².','多项式 x² + 2x + 1 可以写成 (x + 1)²。'),('A polynomial function can be used to model the curve over a limited interval.','可以用多项式函数来拟合有限区间内的那段曲线。'),sources=['https://www.etymonline.com/word/polynomial','https://www.collinsdictionary.com/dictionary/english/polynomial','https://mathworld.wolfram.com/Polynomial.html','https://en.wiktionary.org/wiki/polynomial'])]
assert len(W[0]['examples'])>=2
(OUT/'words_batch200_spec_polynomial_shared.json').write_text(json.dumps(W,ensure_ascii=False,indent=2)+'\n')
print('polynomial shared',len(W),'word')
