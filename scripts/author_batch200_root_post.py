# coding: utf-8
import json
from pathlib import Path
from author_batch200_root_post_a import W as A
from author_batch200_root_post_b import W as B
W=A+B
SHARED=['postseason','postgraduate','postmodern','postcolonial','postnatal','postpone','postponement']
ROOT=dict(id='C1107',meaning='之后；后面',core='POST = AFTER / BEHIND',image='画一条时间轴，给事件插上标记，再看标记后面的事；若换成空间，就表示某物的后部。',intro='来自拉丁 post，既可说时间上的之后，也可说位置上的后面。posterior、posterity、posthumous 通过各自的拉丁词形进入英语；postwar、postdoctoral 等则利用前缀组成现代英语词。看起来透明的现代拆分，不一定就是全部历史。',forms='post- 常加事件或阶段词：war 战争、doctoral 博士、operative 手术相关。postscript 接拉丁“写在后面”；posthumous 的 h 是后加的词源联想。postpaid 的手机义用“之后”前缀，邮寄义的 post 却是邮件，不可混解。',branches=[['空间后部、后世与身后','posterior, posterity, posthumous, posthumously'],['安排、写作与战争之后','postpone, postponement, postponed, postscript, postwar'],['教育阶段之后','postsecondary, postgraduate, postdoctoral, postdoc'],['手术、分娩及创伤之后','postoperative, postpartum, postnatal, posttraumatic'],['比赛、文化与付费','postgame, postseason, postmodern, postmodernism, postcolonial, postpaid']],contrasts='postsecondary 以中等教育为分界，postgraduate 通常以本科为分界，postdoctoral 以博士学位为分界。postgame 是单场赛后，postseason 是常规赛后的赛事阶段。',practice='The postdoctoral researcher added a postscript explaining why the lecture had been postponed.\n\n这位博士后研究人员在末尾加了附言，解释讲座为什么延期。',words=[x['word'] for x in W]+SHARED,exclude={'postmenopausal':'本轮暂略较专门的医学派生词','posteriorly':'低收益副词暂略','postsynaptic':'专门神经科学词暂略'})
if __name__=='__main__':
 for name,data in [('roots_post',[ROOT]),('words_post',W)]:Path('.cache/batch200/drafts/root/'+name+'.json').write_text(json.dumps(data,ensure_ascii=False,indent=2))
 print(len(W),sum(len(x['examples']) for x in W))
