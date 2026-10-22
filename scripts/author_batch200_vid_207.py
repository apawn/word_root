# -*- coding: utf-8 -*-
"""C1227 rhod: the rose as a flower and a colour."""
import json
from pathlib import Path
from lesson_authoring import entry as E
BASE=Path(__file__).resolve().parents[1];OUT=BASE/'.cache/batch200/drafts/rewrite_vid'
W=[E('rhodopsin','英 /rəʊˈdɒpsɪn/；美 /roʊˈdɑːpsɪn/','视紫红质','眼睛视杆细胞里的感光物质，帮助我们在较暗的环境中看见东西。名字说的是这种物质的颜色与视觉功能，不是“看玫瑰的能力”。','借自 19 世纪德语 Rhodopsin，用希腊 rhodon“玫瑰”相关的 rhod-“玫瑰色、红色”、opsis“视觉”和物质词尾 -in 命名。它也叫 visual purple“视紫质”；玫瑰色与紫色在历史命名里不是严格统一的色卡。',[['希腊 rhodon；opsis；物质词尾 -in','玫瑰／玫瑰色；视觉；物质'],['德语 Rhodopsin','近代以颜色和感光作用形成的名称'],['英语 rhodopsin','视杆细胞中的视紫红质']],'光照触发它所含的感光成分发生变化，随后启动细胞内一连串信号。在人眼里，它主要服务于弱光视觉；负责彩色视觉的视锥细胞另有感光系统，不能由名称的“红色”推成只负责看红。','rhodopsin in rod cells；rhodopsin activation；the visual pigment rhodopsin。','retina 是视网膜这一层组织，rhodopsin 是其中视杆细胞里的感光物质；不是两个部位名称。',('Rhodopsin helps rod cells respond to dim light.','视紫红质帮助视杆细胞对弱光作出反应。'),('The lesson explains how light activates rhodopsin.','这节课解释了光如何激活视紫红质。'),sources=['https://www.merriam-webster.com/dictionary/rhodopsin','https://www.collinsdictionary.com/dictionary/english/rhodopsin','https://medlineplus.gov/genetics/gene/rho/'])]
m=json.loads((BASE/'.cache/batch200/rewrite_vid.json').read_text());names=['rhododendron','rhodopsin']
cat=next(x for x in json.loads((BASE/'.cache/catalog.json').read_text()) if x['id']=='C1227')
EX={w:'较冷门的恐惧症或藻类分类称呼，按当前通用阅读范围暂略。' for w in cat['family'] if w not in names}
ROOT=dict(id='C1227',meaning='玫瑰；玫瑰色',core='rhod- 接希腊 rhodon“玫瑰”。有时借花来命名植物，有时借花的颜色来命名物质。',image='玫瑰 rhodon → rhododendron 植物名称；玫瑰色 + 视觉 → rhodopsin 视紫红质。',intro='同一个命名材料可以走花形、花色两条路。杜鹃不因此变成玫瑰，视紫红质也不因此只感受红色。',forms='rhododendron 经古代希腊、拉丁植物名与近代分类名转用；rhodopsin 是近代德语科学命名后借入英语。',branches=[['借花命名植物','rhododendron'],['借颜色命名感光物质','rhodopsin']],contrasts='历史字面与现代分类要分开：rhododendron 是杜鹃属植物，rhodopsin 是视觉感光物质；共同字母不代表两者是同一类东西。',practice='分别用“玫瑰 + 树”和“玫瑰色 + 视觉”解释两个名称，再说清它们今天各指什么。',words=names,exclude=EX)
if __name__=='__main__':
 assert {e['word'] for e in W}<=set(m['owned_words'])
 for kind,data in [('roots',[ROOT]),('words',W)]: (OUT/(kind+'_batch200_vid_207.json')).write_text(json.dumps(data,ensure_ascii=False,indent=2))
 print('rhod:',len(W),'words;',sum(len(e['examples']) for e in W),'examples')
