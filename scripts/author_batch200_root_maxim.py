# coding: utf-8
import json
from pathlib import Path
from author_batch200_root_maxim_a import W as A
from author_batch200_root_maxim_b import W as B
W=A+B
ROOT=dict(id='C0711',meaning='最大、最高；最重要的原则',core='MAXIM = GREATEST',image='把刻度拉到顶端，是 maximum；把某件事尽量做到大，是 maximize。另一条路把最重要的命题留下来，缩成一句可以指导行动的 maxim。',intro='拉丁 magnus 是大，maximus 是最大。maximum 直接走向最大量，maxim 则经过“最重要的命题”发展成格言。maximalist 和 maximalism 还可以谈繁复丰富的风格或追求全盘要求的立场。',forms='maximum 的 maxim- 接 -ize 成 maximize，再接 -ation 成 maximization；maximise 是常见英式拼写。maximal 接 -ly 成 maximally。maxim 虽然短，不是英语 maximum 的临时缩写，而有自己的借入路线。',branches=[['上限与最大程度','maximum, maximal, maximally'],['把目标尽量提高','maximize, maximise, maximization, maximized, maximizing'],['最重要的原则压成一句话','maxim'],['丰富的风格或完整的要求','maximalist, maximalism']],contrasts='maximum 是最大，optimal 是最合适；maximize 追求提高目标，optimize 追求合适的整体方案。maxim 是格言。数学中 maximal 与 maximum 可能有严格区别，普通近义不能覆盖专业定义。',practice='Our maxim is to use space wisely, not simply to maximize the number of objects in a room.\n\n我们的准则是合理利用空间，而不是单纯往房间里塞入最多的东西。',words=[w['word'] for w in W],exclude={'submaximal':'较专业的程度或运动生理学用语，本轮暂略'})
if __name__=='__main__':
 for name,data in [('roots_maxim',[ROOT]),('words_maxim',W)]:Path('.cache/batch200/drafts/root/'+name+'.json').write_text(json.dumps(data,ensure_ascii=False,indent=2))
 print(len(W),sum(len(w['examples']) for w in W))
