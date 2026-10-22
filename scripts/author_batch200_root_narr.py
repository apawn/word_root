# coding: utf-8
import json
from pathlib import Path
from author_batch200_root_narr_a import W as A
from author_batch200_root_narr_b import W as B
W=A+B;kept=[x['word'] for x in W]
r=next(x for x in json.loads(Path('.cache/catalog.json').read_text()) if x['id']=='C0793')
EX={w:'极少用的书面形容词，本轮暂略' for w in set(r['family'])|set(r['words']) if w not in kept and '-' not in w}
ROOT=dict(id='C0793',meaning='讲述、使人知道',core='NARR = TELL / MAKE KNOWN',image='你知道一段经历，别人不知道；你把事情按顺序讲出来，让对方在脑中拼成一幅图。这就是 narr- 最有用的画面。',intro='拉丁 narrare 表讲述、叙述，与 gnarus“知道、熟悉”相连。向上可以联系更早表示知道的词源，但现代学习先抓住“把事情讲给别人知道”。讲述可以真实，也可以虚构，词根不替内容保证真假。',forms='narrat- 出现在 narrative、narrator、narration 的历史词干里。英语 narrate 较晚，可能由 narration 逆构或借拉丁分词形成；不要把更早出现的几个名词都画成它的后代。',branches=[['讲述动作','narrate'],['讲述者','narrator'],['过程与旁白','narration'],['故事及解释框架','narrative, narratively, counternarrative']],contrasts='narrator 不必等于 author；narration 不必等于影片全部故事；narrative 不必等于虚假宣传。counter- 接 narrative 是对既有叙事提出另一种解释。',practice='The narrator presents a clear narrative, but another character offers a different account.\n\n叙述者给出了一套清晰的故事，但另一个人物提出了不同的讲法。',words=kept,exclude=EX)
if __name__=='__main__':
 for name,data in [('roots_narr',[ROOT]),('words_narr',W)]:Path('.cache/batch200/drafts/root/'+name+'.json').write_text(json.dumps(data,ensure_ascii=False,indent=2))
 print(len(W),sum(len(x['examples']) for x in W))
