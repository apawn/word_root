# -*- coding: utf-8 -*-
"""C0990 pend/pens: gather independently written lesson parts; no image output."""
import json
from pathlib import Path
from author_batch200_vid_74a import W as WA
from author_batch200_vid_74b import W as WB
from author_batch200_vid_74c import W as WC
BASE=Path(__file__).resolve().parents[1];OUT=BASE/'.cache/batch200/drafts/rewrite_vid'
W=WA+WB+WC
SHARED=['interdependence','interdependent']
EX={'prepense':'古旧或法律固定用语，通用阅读价值有限，按用户常用优先要求暂略。'}
ROOT=dict(id='C0990',meaning='悬挂；称量；权衡、支付',core='先想两幅相连的画面：东西从支点垂下来；天平把东西吊起来称重量。挂着可以变成未决、依赖，称量可以变成权衡、支付和分配。',image='挂住：pendant、suspend；悬而未决：pending、suspense；依靠支点：depend；称出资源：spend、expense；两边抵平：compensate；按份称出：dispense；心中掂量：pensive。',intro='这是一组能贯通日常与工作的词：订单 pending、结果 depend on 条件、花钱 spend、报销 expenses、损失 compensation。先看每个词的使用场景，再用悬挂或称量的老画面帮助理解。',forms='拉丁 pendēre 表示悬垂，相关 pendere 表示使悬挂、称量、支付；分词词干常见 pens-，pensare 是相应的反复式。不同英语词可能各自借入拉丁、法语名词或形容词，不能把每个 -ion、-er 都画成在现代英语动词之后新加。spend 在古英语时期已经进入，不是现代 expend 删掉 ex-；pension 的小旅馆义又是后来的法语借入。',branches=[['悬挂、未决与等待','pending, impending, suspend, suspended, suspension, suspense, suspenseful, suspender, suspenders, pendant, pendulum'],['倾向与附加','penchant, append, appended, appendage, appendix'],['依赖、可靠与自主','depend, dependent, dependence, dependency, dependable, dependably, dependability, independent, independence, independently, interdependence, interdependent'],['定期给付与养老金','pension, pensioner, pensionable'],['花钱、消耗与费用','spend, spent, spending, spender, overspend, overspending, spendthrift, expense, expenses, expensive, inexpensive, expensively, inexpensively, expend, expenditure, expendable'],['补足一边的损失','compensate, compensation, compensatory, uncompensated'],['分发与能否省去','dispense, dispenser, dispensary, indispensable, dispensable'],['心中的权衡与沉思','pensive, pensively, pensiveness']],contrasts='pending 是还没定，impending 是快发生；dependent 是要依靠别人，dependable 是别人能靠得住；suspense 是悬念，suspension 是暂停或悬挂。expense 是费用，expensive 是昂贵，expendable 是可消耗。dispense 是分发，dispense with 却常表示省去。',practice='The decision is pending because it depends on the expected expense. 决定还没定下来，因为它取决于预计的花费。',words=[],exclude=EX)
if __name__=='__main__':
 m=json.loads((BASE/'.cache/batch200/rewrite_vid.json').read_text());r=next(x for x in m['roots'] if x['id']==ROOT['id']);ROOT['words']=list(dict.fromkeys([w for w in r['family'] if '-' not in w and w not in EX]+SHARED))
 assert set(ROOT['words'])==set(SHARED)|{e['word'] for e in W}
 assert {e['word'] for e in W}<=set(m['owned_words'])
 assert len(W)==len({e['word'] for e in W}) and all(len(e['examples'])>=2 and len(e['history'])>=2 for e in W)
 for kind,data in [('roots',[ROOT]),('words',W)]: (OUT/(kind+'_batch200_vid_74.json')).write_text(json.dumps(data,ensure_ascii=False,indent=2))
 print('pend:',len(W),'words;',sum(len(e['examples']) for e in W),'examples;',len(ROOT['words']),'references')
