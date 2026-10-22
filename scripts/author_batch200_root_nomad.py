# coding: utf-8
import json
from pathlib import Path
ROOT=dict(id='C0820',meaning='为寻找牧场而移动；游牧',core='NOMAD = ROAM FOR PASTURE',image='随着水草和季节移动，生活地点会变，但迁移本身可以有稳定的路线。',intro='希腊 nomas、词干 nomad- 与寻找牧场的移动生活有关，经拉丁和法语形成 nomad。现代还借来形容经常换地方居住的人。游牧不等于漫无目的漂泊，词源的移动画面不应变成对人的刻板判断。',forms='nomad 的 nomad- 是希腊词干，不是英语 no 加 mad。nomadic 是对应形容词，来源可分析为英语派生或希腊已有形容词的影响；两者都与游牧词族相连。',branches=[['过迁移生活的人','nomad'],['这种生活方式的性质','nomadic']],contrasts='nomad 是人，nomadic 是性质；traveller 只说明旅行。digital nomad 借的是变换居住地的生活方式，不表示真的放牧。',practice='A nomadic way of life can follow familiar seasonal routes.\n\n游牧生活也可以沿着熟悉的季节性路线进行。',words=['nomad','nomadic'],exclude={'nomadism':'抽象派生先不另列，优先掌握 nomad 和 nomadic','nomadize':'较冷门动词，先略过'})
if __name__=='__main__':
 Path('.cache/batch200/drafts/root/roots_nomad.json').write_text(json.dumps([ROOT],ensure_ascii=False,indent=2))
 print('1 root; 2 shared words')
