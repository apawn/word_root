# -*- coding: utf-8 -*-
from pathlib import Path
import json
from lesson_authoring import entry as E
BASE=Path(__file__).resolve().parents[1];OUT=BASE/'.cache/batch200/drafts/rewrite_spec'
H=[['希腊 ouranos“天空”及神名 Ouranos → 拉丁化 Uranus','天空之神的名字'],['行星名 Uranus','天王星沿用这个神名'],['近代拉丁元素名 uranium → 英语 uranium','克拉普罗特以当时新发现的行星为新元素命名']]
W=[E('uranium','英美 /juˈreɪniəm/','铀','一种天然存在、具有放射性的金属元素；名字借了天王星的光。','近代拉丁 uranium 由行星名 Uranus 加元素名常见的 -ium 构成；行星名又接希腊天空之神 Ouranos。这里是纪念式命名，不是说铀来自天王星。',H,'化学符号是 U，原子序数是 92。它常出现在矿产、核燃料和放射性的文章里。1789 年克拉普罗特辨认出一种新元素并命名；真正分离出金属铀是后来的事，不要把两个发现步骤混成一次。','uranium ore；uranium deposits；natural uranium；uranium fuel。','Uranus 是行星专名，首字母大写；uranium 是元素名，通常小写。铀矿石不是一整块纯铀，ore 说明它是含铀的矿物材料。',('The museum label identifies uranium by the symbol U.','博物馆的说明牌用符号 U 标示铀。'),('The report examines the environmental impact of uranium mining.','报告研究了铀矿开采对环境的影响。'),sources=['https://www.etymonline.com/word/uranium','https://www.oxfordlearnersdictionaries.com/definition/english/uranium','https://periodic-table.rsc.org/element/92/uranium'])]
m=json.loads((BASE/'.cache/batch200/rewrite_spec.json').read_text());r=next(x for x in m['roots']if x['id']=='C1589');c=next(x for x in json.loads((BASE/'.cache/catalog.json').read_text())if x['id']=='C1589');keep={w['word']for w in W};excluded={w:'按用户要求暂略罕见矿物学、旧天文学术语及低频恐惧症名称。'for w in (set(r['family'])|set(c['family'])|set(c.get('unmatched',[])))-keep};excluded['Uranus']='行星专名已在 uranium 的词源中解释，暂不单列专名词条。'
ROOT=[dict(id='C1589',meaning='天空；天王星名称的来源',core='ouranos：天空；uranium 通过行星命名继承了这个名字。',image='天空之神的名字用于一颗行星，再被借来给新元素命名。',intro='这一组最值得先认识的是 uranium“铀”。它的来源是一条命名史：希腊天空之神名变成天王星名，化学家再以这颗行星为元素命名。名字能讲清历史，但并不说明金属的物理性质。',forms='Uranus 是天王星，uranium 是元素铀；-ium 是很多元素名称采用的词尾。',branches=[['从行星名到元素名','uranium']],contrasts='天王星并不是铀的产地解释。词源命名、元素发现与金属分离也是不同的事情。',practice='看到 uranium ore，先读懂“铀矿石”；再用一句话说明它为什么叫 uranium。',words=['uranium'],exclude=excluded,sources=['https://www.etymonline.com/word/uranium','https://periodic-table.rsc.org/element/92/uranium'])]
assert all(w['word']in m['owned_words']for w in W)
for w in W:assert len(w['examples'])>=2 and all(len(n)==2 and all(isinstance(x,str)and x for x in n)for n in w['history']),w['word']
for k,d in [('roots',ROOT),('words',W)]: (OUT/f'{k}_batch200_spec_167_uran.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
print('C1589',len(W),'new',sum(len(w['examples'])for w in W),'examples')
