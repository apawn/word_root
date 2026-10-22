# -*- coding: utf-8 -*-
import json
from pathlib import Path
from author_batch200_root_fung_a import WA
from author_batch200_root_fung_b import WB
W=WA+WB
ROOT=dict(id='C0459',meaning='执行；履行职责；发挥作用',core='FUNG / FUNCT = PERFORM',image='一套系统像一组分工合作的人：每个部分都把自己的那份工作做起来。function 是它做什么；malfunction 是做错或做不动；defunct 是那段工作已经结束；perfunctory 则是心里只想赶紧交差。',intro='这一族接拉丁动词 fungi，词典第一人称形式是 fungor，表示履行、执行；它的分词词干是 funct-。先抓住“承担并完成一个作用”，就能把功能、职员、故障和敷衍几条支线连起来。',forms='funct- 常在 function、defunct、perfunctory 中出现；fung- 保留在 fungible，字母 g 在这里读 /dʒ/。拉丁动词 fungi 与英语 fungi“真菌的复数”不是同一个词源；看到一样的拼写也要看语言和语义。',branches=[['把自己的作用发挥出来','function, functional, functionality, functionally, functioning, multifunction'],['不能正常发挥作用','nonfunctional, functionless, dysfunction, dysfunctional, dysfunctionality, malfunction, malfunctioning'],['承担工作的人；已结束的工作','functionary, defunct'],['只求把流程走完','perfunctory, perfunctorily, perfunctoriness'],['同等的一份可以代行作用','fungible, fungibility, nonfungible'],['按功能解释与设计','functionalism, functionalist, functionalistic'],['赋予结构新的功能','functionalize, functionalization'],['物理中的函数名称','wavefunction']],contrasts='functional 是能起作用或与功能有关；perfunctory 是投入不足、敷衍了事。defunct 表示已结束运作，malfunctioning 表示出故障。fungible 的可互换性不是长得像就够，还要看用途、规格和价值能否等价。',practice='The device looked impressive, but one function was not working. A careful check found the malfunction; a perfunctory glance would have missed it.\n\n设备看起来很气派，但有一个功能不能用。认真检查发现了故障；如果只是敷衍地看一眼，就会漏掉。',words=[w['word'] for w in W]+['multifunction'])
if __name__=='__main__':
 assert len(W)==26
 for name,v in [('roots_fung',[ROOT]),('words_fung_a',WA),('words_fung_b',WB)]:Path('.cache/batch200/drafts/root/'+name+'.json').write_text(json.dumps(v,ensure_ascii=False,indent=2))
 print(len(W),'individually authored words',sum(len(w['examples']) for w in W),'examples')
