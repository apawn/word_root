# -*- coding: utf-8 -*-
"""C1673 zephyr: a classical west wind becomes a literary gentle breeze."""
import json
from pathlib import Path
from lesson_authoring import entry as E
BASE=Path(__file__).resolve().parents[1];OUT=BASE/'.cache/batch200/drafts/rewrite_vid'
W=[E('zephyr','英 /ˈzefə/；美 /ˈzefər/','和风；轻柔的微风；西风〔古典、文学语境〕','一阵风轻轻掀动窗帘、带走一点闷热，没有猛烈拍打门窗。这种柔和的风在文学描写中可以叫 zephyr。','远接希腊 Zephyros，既是西风的名称，也被拟人化为西风神；经拉丁 Zephyrus 进入英语。英语早期有 Zefferus、Zephirus 等形式，后来成为 zephyr，并扩展到一般轻柔的风。',[['希腊 Zephyros','西风；西风的神格化名称'],['拉丁 Zephyrus → 早期英语 Zefferus／Zephirus','古典西风名称传入英语'],['英语 zephyr','西风；后泛指轻柔的微风']],'现代诗文里的 a zephyr 主要让读者感到风轻、温柔，不必每次都精确来自正西方。若在神话里作人名使用，通常大写；小写常是普通名词。','a gentle zephyr；a summer zephyr；a zephyr stirred the leaves。属于文学、诗意用词。','breeze 是更日常的微风名称；zephyr 带古典与诗意色彩。它不是严格的风速等级。',('A zephyr stirred the curtains beside the open window.','一阵轻风拂动了敞开窗边的窗帘。'),('The poet describes the evening wind as a gentle zephyr.','诗人把晚风描写成轻柔的和风。'),sources=['https://www.etymonline.com/word/zephyr','https://www.oxfordlearnersdictionaries.com/definition/english/zephyr'])]
ROOT=dict(id='C1673',meaning='西风；和风',core='zephyr- 从希腊西风及西风神的名称而来。英语把古典名称带来的柔和意象，扩展为一般轻风。',image='希腊 Zephyros 西风／西风神 → 拉丁 Zephyrus → 英语 zephyr 轻柔微风。',intro='这组不靠长串派生词学习，记住一幅窗帘被风轻轻掀动的画面，再知道它带诗意就足够实用。',forms='zephyr 是古典名称经拉丁进入英语后的形式；开头 z 读 /z/，ph 读 /f/。不是现代英语一个常用词加后缀形成。',branches=[['诗文里的和风','zephyr']],contrasts='现代 zephyr 不要求风一定来自西方，也不表示任何固定风速；普通对话更常用 breeze。',practice='用 a zephyr 描述一阵轻风，体会它比 a strong wind 多出的柔和气氛。',words=['zephyr'],exclude={})
if __name__=='__main__':
 for kind,data in [('roots',[ROOT]),('words',W)]: (OUT/(kind+'_batch200_vid_230.json')).write_text(json.dumps(data,ensure_ascii=False,indent=2))
 print('zephyr: 1 word; 2 examples')
