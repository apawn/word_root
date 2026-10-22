# coding: utf-8
import json
from pathlib import Path
from author_batch200_root_pass_a import W as A
from author_batch200_root_pass_b import W as B
W=A+B
SH=['pace','passage','pass','past','passing','passenger','passport','surpass','bypass','compass','encompass','impassable','impasse']
ROOT=dict(id='C0966',meaning='一步、迈步；经过、通过',core='PASS = STEP, PASS',image='先跨出一步，再从某处经过。能走的地方是 passage，过得去的路是 passable；时间经过形成 past，主动找点事让时间愉快过去就是 pastime。',intro='拉丁 passus 表一步、步幅，与 pandere“伸展、展开”相连。本页专门展开迈步与通过这一支；pace 经法语 pas，pass 经 passer，拼写不同却能追到相近源头。',forms='passus 是本组的一步，不是 patior“承受”所出的另一个 passus；passion、passive 不能直接归为迈步。past 历史上是 passed 的变体，现代语法已经分工。passenger 的 n 是历史后添音，不是独立词根。',branches=[['步速和节奏','pace, pacing, outpace'],['经过、通过、已经过去','pass, passed, past, passing'],['道路与通行条件','passage, passageway, passable, impassable, impasse'],['通行的人与证件','passenger, passerby, passport'],['超越、绕过或越界','surpass, bypass, trespass'],['度过时间与测量范围','pastime, compass, encompass']],contrasts='passed 常是动词，past 通常不是；passable 只是尚可，不等于优秀。passageway 指通道，passage 还可以是文章段落。impassable 无法通行与 impassive 面无表情是不同来源。',practice='A passerby showed us a passable route through the hills, so we slowed our pace and passed the time talking.\n\n一位路人给我们指了一条可以穿过山地的路线，于是我们放慢脚步，一路聊天消磨时间。',words=SH+[w['word'] for w in W],exclude={})
if __name__=='__main__':
 for name,data in [('roots_pass',[ROOT]),('words_pass',W)]:Path('.cache/batch200/drafts/root/'+name+'.json').write_text(json.dumps(data,ensure_ascii=False,indent=2))
 print(len(W),sum(len(w['examples']) for w in W))
