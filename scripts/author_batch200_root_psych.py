# -*- coding: utf-8 -*-
import json
from pathlib import Path
from author_batch200_root_psych_a import WA
from author_batch200_root_psych_b import WB
from author_batch200_root_psych_c import WC
W=WA+WB+WC
ROOT=dict(id='C1154',meaning='心灵、精神；心理活动；古代的生命与灵魂观念',core='PSYCH = MIND / SOUL',image='同一个人，外面看见的是身体，里面还有感受、想法、记忆和欲望。psych- 把注意力带进这层内在世界：可以研究它、测量它，也可以讨论如何帮助它；在古代思想和神话里，则常说灵魂。',intro='来源是希腊 psyche（ψυχή），含生命、灵魂、心灵等义。它常被联系到 psykhein“吹气、呼吸”等词，但更远的来源存在争议。后世借用 psych-／psycho- 造出大量学术词；不能把现代心理学、医学、哲学和通灵说法当成同一套知识。',forms='psych- 开头的 p 在这些英语常用词里通常不发音；psyche 读 /ˈsaɪki/，psych 读 /saɪk/。复合构词常用 psycho-；它不是独立俚语 psycho 的贬义。-logy 侧重研究，-iatry 接医学照护，-therapy 指治疗，-metrics 指测量；后半部分决定具体分支。',branches=[['内心世界与日常心理状态','psyche, psychologically, psych, psyched, psyching'],['心理研究及身心、社会联系','psychology, psychological, psychologist, neuropsychology, psychosomatic, psychomotor, psychosocial'],['精神医学与心理治疗','psychiatry, psychiatrist, psychiatric, psychotherapy, psychotherapist'],['精神分析传统','psychoanalysis, psychoanalyst, psychoanalytic, psychoanalytical'],['必须分清的症状与人格词','psychosis, psychotic, antipsychotic, psychopathy, psychopathic, psychopath, psychopathology, psychoticism, psycho'],['心灵主张与测量','psychic, psychical, psychically, parapsychology, psychometry, psychometric, psychometrics'],['感知变化与艺术风格','psychoactive, psychedelic, psychedelia'],['哲学、灵魂与神话','panpsychism, panpsychist, metempsychosis, psychopomp']],contrasts='psychiatrist 是精神科医生，psychologist 是心理学专业人员。psychosis、psychopathy、psychoticism 分别涉及症状状态、人格特质构念和特定人格模型维度。psychometric 测量心理属性，psychic 在常用语境中可能说超感知主张。psychoanalysis 是特定理论传统，不等于全部心理学或心理治疗。',practice='A psychologist and a psychiatrist joined the discussion. They explained how psychometric tests are used and why a psychological description should be read in context.\n\n一位心理学家和一位精神科医生参加了讨论。他们解释了心理测验的用途，以及为什么心理方面的描述需要结合语境阅读。',words=[x['word'] for x in W]+['psychology','psychological','psychologist','neuropsychology','parapsychology','psychoanalytic','psychomotor','psychosocial'])
if __name__=='__main__':
 assert len(W)==36 and len({x['word'] for x in W})==36
 for name,data in [('roots_psych',[ROOT]),('words_psych_a',WA),('words_psych_b',WB),('words_psych_c',WC)]:Path('.cache/batch200/drafts/root/'+name+'.json').write_text(json.dumps(data,ensure_ascii=False,indent=2))
 print(len(W),'individually authored words',sum(len(x['examples']) for x in W),'examples')
