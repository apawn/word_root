# coding: utf-8
import json
from pathlib import Path
from author_batch200_root_par_a import W as A
from author_batch200_root_par_b import W as B
W=A+B
ROOT=dict(id='C0957',meaning='相等、相称；同辈、配对与比较',core='PAR = EQUAL / MATCHED',image='把两个东西放在同一条水平线上：可以相等、成对，也可以一比较就发现差距。',intro='拉丁 par 表示相等、相称。peer 经法语变成同等者，pair 经拉丁复数及法语变成一对，compare 把东西放在一起比较。这个源头更远的历史并不确定，也要与 parare“准备”以及希腊 para-“旁边”等分开。',forms='par 保留短词形；peer、pair 经法语发生拼写和读音变化。comparison、comparable、comparative 各有拉丁及法语借入路线，并非全由现代英语 compare 直接加后缀产生。parity 与 disparity 对应同等与差距。',branches=[['同等与成对','par, peer, peerless, pair, parity, subpar'],['比较、相当与无法匹敌','compare, comparison, comparable, comparative, comparatively, incomparable'],['不相等与压低价值','disparity, disparage, disparaging, disparagement']],contrasts='peer 的“同辈”与“凝视”不是同一来源；parity 的生育相关同形词也要分开。comparable 是可比或相当，comparative 是比较性的。disparity 说差距，disparage 说贬低。',practice='Compare the results fairly: a disparity in performance is no reason to disparage your peers.\n\n公平地比较结果：表现上的差距不是贬低同伴的理由。',words=[w['word'] for w in W]+['subpar'],exclude={})
if __name__=='__main__':
 for name,data in [('roots_par',[ROOT]),('words_par_a',A),('words_par_b',B)]:Path('.cache/batch200/drafts/root/'+name+'.json').write_text(json.dumps(data,ensure_ascii=False,indent=2))
 print(len(W),sum(len(w['examples']) for w in W))
