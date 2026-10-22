# -*- coding: utf-8 -*-
import json
from pathlib import Path
from author_batch200_root_joc_a import WA
from author_batch200_root_joc_b import WB
W=WA+WB
ROOT=dict(id='C0622',meaning='玩笑、游戏、消遣',core='JOC = JOKE / PLAY',image='一句话把人逗笑，一场表演让人放松。这个“玩、逗乐”的中心，既能走向笑话，也能走向杂耍；游戏胜负未定的局面，还能引出风险。',intro='本组的确定核心是拉丁 iocus／jocus“玩笑、游戏、消遣”。joke 较直接保留玩笑义，jocular 是较正式的诙谐，juggle 通过表演和手上技巧发展出“同时兼顾”。jewel 的近层法语来源明确，但更早是否与 jocus 相连有争议，相关词在下文会保留这一界限。',forms='词形不会总是原样保留 joc：joke 是后来的英语形式，juggle 经法语演化，jeopardy 中的 jeu 是法语“游戏”。英语中 juggler 的前身比 juggle 更早，现代能拆成动词加 -er，不代表历史上一定按这个顺序产生。jewel／jewelry 这一支不能当作已证实的 joc 同源关系。',branches=[['说笑和语气','joke, joking, jokingly, joker, jokester, jocular'],['表演与兼顾','juggle, juggler, juggling'],['胜负未定到处境危险','jeopardy, jeopardize'],['可能相关，但更早词源有争议','jewel, jewelry, jewellery, jeweler, jeweller']],contrasts='joking 是在说笑，不保证别人觉得 funny。juggle 强调同时协调，常带时间紧、事情多的感觉。jeopardy 已是危险处境，不能只译成游戏。jewelry／jewellery 一般不可数，jeweler／jeweller 指人或经营者。',practice='He joked about juggling three jobs, but the situation was no joke. One more delay could jeopardize the project.\n\n他打趣说自己像在同时应付三份工作，但实际处境一点也不轻松。再延误一次就可能危及整个项目。',words=[x['word'] for x in W],exclude={w:'按用户要求，罕见古词或低收益书面派生词先略过。' for w in ['jocularity','jongleur','jocose','jocosity']})
if __name__=='__main__':
 assert len(W)==16 and len({x['word'] for x in W})==16
 for name,data in [('roots_joc',[ROOT]),('words_joc_a',WA),('words_joc_b',WB)]:Path('.cache/batch200/drafts/root/'+name+'.json').write_text(json.dumps(data,ensure_ascii=False,indent=2))
 x=next(x for x in W if x['word']=='jeweller');request=[dict(word=x['word'],pos='noun',ipa=x['ipa'],gloss='A person who makes, repairs or sells jewelry; chiefly British spelling of jeweler.',meaning_zh=x['meaning'],etymology_text='From Middle English forms borrowed from Anglo-French jueler and related Old French forms; modern spelling variant of jeweler.',sources=x['sources'])]
 Path('.cache/batch200/root_joc_supplement_request.json').write_text(json.dumps(request,ensure_ascii=False,indent=2))
 print(len(W),'authored words',sum(len(x['examples']) for x in W),'examples')
