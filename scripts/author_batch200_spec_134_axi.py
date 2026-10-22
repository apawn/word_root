# -*- coding: utf-8 -*-
from pathlib import Path
import json
from lesson_authoring import entry as E
BASE=Path(__file__).resolve().parents[1];OUT=BASE/'.cache/batch200/drafts/rewrite_spec'
A=[['拉丁语 axis','车轴、枢轴'],['英语 axis','转动轴线；坐标轴；中心方向']]
W=[
E('axis','英美 /ˈæksɪs/；复数 axes /ˈæksiːz/','轴；轴线；坐标轴','先找出一条中心线，再看物体怎样绕它转或怎样以它为参照。','直接借拉丁 axis“车轴、枢轴”。英语 axis 是整词借入；它与 axle 有更早的同源关系，但不是现代 axle 的缩写。',A,'地球绕自己的 axis 转，这条轴是想象的线，不是穿过地球的铁杆。图表上的 axis 是定位数据的参照线。谈政治时也能比喻结盟的中心关系；具体含义都要看语境。','an axis of rotation；the horizontal axis；the vertical axis；an axis of symmetry。','axis 可以是抽象线；axle 通常是实际机械轴。axis 的复数 axes 读 /ˈæksiːz/，与 axe“斧头”的复数 axes /ˈæksɪz/ 不同。',('The globe spins smoothly around its tilted axis.','地球仪绕着倾斜的轴平稳转动。'),('Label the horizontal axis with the months of the year.','在横轴上标出一年中的各个月份。'),sources=['https://www.etymonline.com/word/axis','https://www.oxfordlearnersdictionaries.com/definition/english/axis']),
E('axial','英美 /ˈæksiəl/','轴的；轴向的；围绕轴的','把方向或性质与某条轴线联系起来。','英语 axis 去 -is，加 -al，形成形容词 axial。不是把 axis 的最后一个 s 读丢了，而是换成了形容词形式。',A+[['英语 axis + -al → axial','与轴有关；沿轴或绕轴的']],'axial movement 可以是沿轴线前后移动；axial rotation 是绕轴自转。两个搭配都与轴有关，但动作不同，因此不要把 axial 一律翻成“沿着轴移动”。','axial movement；axial rotation；axial tilt；axial direction。','radial 通常从中心向外像半径展开，axial 围绕或沿轴来说明。具体是在“沿轴”还是“绕轴”，由后面的名词决定。',('The diagram shows the planet’s axial tilt.','示意图展示了这颗行星的自转轴倾角。'),('The bearing allows a small amount of axial movement.','这个轴承允许少量轴向移动。'),sources=['https://www.etymonline.com/word/axial','https://www.oxfordlearnersdictionaries.com/definition/english/axial'])
]
m=json.loads((BASE/'.cache/batch200/rewrite_spec.json').read_text());r=next(r for r in m['roots']if r['id']=='C0106');family=r['family'];keep={w['word']for w in W}
excluded={'axion':'按用户范围暂略理论粒子物理中的专业名称。','axisymmetry':'按用户范围暂略专门的对称性名词；常用 axis 与 axial 已保留。'}
ROOT=[dict(id='C0106',meaning='轴；中心线',core='axi-：作为转动中心或定位参照的一条线。',image='旋转地球仪的中心线，或图表中标出数值的参照线。',intro='拉丁 axis 表示车轴、枢轴。英语把它用来描述旋转的中心线，也用在图表与几何中；axial 则是说明事物怎样与轴相关的形容词。',forms='axis 是借入的完整名词；axial 用 axis 的词基加 -al。名词复数 axes 保留古典词形变化，读音也不同于斧头 axe 的复数。',branches=[['中心线与参照线','axis'],['轴的方向或关系','axial']],contrasts='axis 不一定是一根真实杆件，axle 通常是实际机械轴。axial 的“沿轴”与“绕轴”要看具体搭配。',practice='说明地球仪的 axis 与图表的 axis 怎样都起参照作用，再比较 axial movement 与 axial rotation。',words=[w for w in family if w in keep],exclude=excluded,sources=['https://www.etymonline.com/word/axis','https://www.etymonline.com/word/axial'])]
assert keep==set(family)-set(excluded)
assert all(w['word']in m['owned_words']for w in W)
for w in W:assert len(w['examples'])>=2 and all(len(n)==2 and all(isinstance(x,str)and x for x in n)for n in w['history']),w['word']
for k,d in [('roots',ROOT),('words',W)]: (OUT/f'{k}_batch200_spec_134_axi.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
print('C0106',len(W),'new',sum(len(w['examples'])for w in W),'examples')
