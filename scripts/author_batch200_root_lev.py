# -*- coding: utf-8 -*-
import json
from pathlib import Path
from author_batch200_root_lev_a import WA
from author_batch200_root_lev_b import WB
from author_batch200_root_lev_c import WC
W=WA+WB+WC
ROOT=dict(id='C0669',meaning='轻；抬起；减轻负担',core='LEV = LIGHT / LIFT',image='你把朋友肩上的重箱子托起来：箱子升高了，朋友也轻松了。“抬起”和“变轻”就这样连在一起。再往外想：抬高地位、筹起一笔钱、把面团发起，都可以沿各自的历史支线理解。',intro='这一族主要接拉丁 levis“轻”和 levare“抬起、减轻”。英语有直接借来的拉丁词，也有经过法语、意大利语的词，还有近代新造词。先抓住“轻—抬起—卸下负担”的画面，再看每个词具体走了哪条路。',forms='lev- 保留在 elevate、levity 等词中；法语中又发展出 lever、léger 一类形式，分别进入杠杆、轻捷等支线。relief 与 relieve 的末尾 /f/、/v/ 不同；relevant 的相关义接历史上的帮助、适用用法。level 来自另一条拉丁 libella 词源，不能看到 lev 就硬归进本页。',branches=[['把重担抬走','relieve, relief, relieved, relieving, reliever, alleviate, alleviation'],['对当前事情有帮助、适用','relevant, relevance, relevancy, irrelevant, irrelevance'],['抬高位置、程度或装置','elevate, elevated, elevator, elevation, levator, superelevation'],['借一个支点发力','lever, leverage, leveraged, deleverage, deleveraging'],['筹起款项；筑起堤岸；起床接见','levy, leviable, levee'],['轻到悬起；让面团鼓起','levitate, levitation, maglev, leaven, leavening, unleavened'],['态度轻松或轻率；动作轻快','levity, legerity, legerdemain'],['日出方向与古旧抬举用语','Levant, sublevation']],contrasts='relief 的缓解义和浮雕义有不同借入支线，最终都可接“抬起”；levy 是征收，levee 是堤岸或历史上的接见。levitation 的名词记录早于 levitate 的动词记录，不能把方便记忆的拆分当成出生顺序。lever 是杠杆，levator 是按抬举功能命名的肌肉。',practice='The volunteers used a lever to raise the heavy cover. When the pressure was relieved, everyone gave a sigh of relief.\n\n志愿者用杠杆抬起沉重的盖子。压力解除后，大家都松了一口气。',words=[w['word'] for w in W])
if __name__=='__main__':
 assert len(W)==37 and len({w['word'] for w in W})==37
 for name,v in [('roots_lev',[ROOT]),('words_lev_a',WA),('words_lev_b',WB),('words_lev_c',WC)]:Path('.cache/batch200/drafts/root/'+name+'.json').write_text(json.dumps(v,ensure_ascii=False,indent=2))
 print(len(W),'individually authored words',sum(len(w['examples']) for w in W),'examples')
