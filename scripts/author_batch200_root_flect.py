# -*- coding: utf-8 -*-
import json
from pathlib import Path
from author_batch200_root_flect_a import WA
from author_batch200_root_flect_b import WB
from author_batch200_root_flect_c import WC
from author_batch200_root_flect_d import WD
W=WA+WB+WC+WD
ROOT=dict(id='C0433',meaning='弯曲、转向；折回、偏转、变通',core='FLECT / FLEX = BEND',image='想象一根可弯的细条：向后弯，方向折回；向旁边弯，路线偏开；能随需要弯，便有调整余地。光线、身体、词形和思考都可以借这个画面来理解。',intro='这一组来自拉丁 flectere“弯曲、使转向”，分词 flexus 形成 flex- 词干；更早来源并不确定。reflect、deflect、inflect 对应不同的拉丁前缀组合。许多名词和形容词各自经拉丁或法语进入英语，不能把现代能拆开的词形一概当成真实历史顺序。',forms='flect- 与 flex- 是同一拉丁动词体系的不同词干，不是看到 c 就在英语里统一改成 x。re- 可表示折回，de- 可表示偏开，in- 在 inflect 中不是否定，但在 inflexible 中是否定。flexible、flexibility 等借入词与现代 flex 的关系，要区别构词理解和来源分析。',branches=[['光与思考向后折回','reflect, reflection, reflective, reflected, reflecting, reflectively, unreflective, reflector, reflectance, reflectivity'],['能够弯曲，也能够变通','flex, flexible, flexibility, flexibly, inflexible, inflexibility, inflexibly, flexed, flexing, flexile, flexitime, flextime'],['使来物或注意力偏开','deflect, deflection, deflected, deflecting, deflector'],['词形、语调与曲线改变','inflect, inflection, inflected, inflecting, inflectionless, inflectional'],['指回自身与反射反应','reflex, reflexive, reflexively, reflexivity, reflexology'],['身体、结构和方向的弯曲','flexion, flexor, flexure, flexural, circumflex, retroflex, retroflexion'],['弯膝的礼仪与比喻','genuflection, genuflect']],contrasts='reflective 是沉思、反思的，reflexive 可指下意识的或指回自身的。reflect 反射，deflect 偏转，refract 折射。flexible 说能弯、能调整，不等于 elastic 的受力后恢复。inflection 的词形变化不能与 derivation 的派生构词混为一谈；genuflect 也不是在英语中先于 genuflection。',practice='After reflecting on the problem, the team chose a more flexible schedule. They answered the difficult questions directly instead of deflecting them.\n\n认真想过问题后，团队选择了更灵活的时间安排。他们直接回答了难题，没有把问题岔开。',words=[x['word'] for x in W])
if __name__=='__main__':
 assert len(W)==47 and len({x['word'] for x in W})==47
 for name,data in [('roots_flect',[ROOT]),('words_flect_a',WA),('words_flect_b',WB),('words_flect_c',WC),('words_flect_d',WD)]:Path('.cache/batch200/drafts/root/'+name+'.json').write_text(json.dumps(data,ensure_ascii=False,indent=2))
 print(len(W),'individually authored words',sum(len(x['examples']) for x in W),'examples')
