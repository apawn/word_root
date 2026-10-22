# -*- coding: utf-8 -*-
"""C0516 hadr: a historical image, not a modern classification rule."""
import json
from pathlib import Path
from lesson_authoring import entry as E
BASE=Path(__file__).resolve().parents[1]; OUT=BASE/'.cache/batch200/drafts/rewrite_vid'
W=[
E('hadron','英 /ˈhædrɒn/；美 /ˈhædrɑːn/','强子〔如质子、中子等由夸克组成的粒子〕','把几个夸克组成的微观系统看作一个粒子，其中的夸克由强相互作用束缚。质子、中子就是你最容易遇到的 hadrons。','名称采用希腊 hadros“粗厚、强壮、硕大”的材料，加粒子名常用的 -on。20 世纪物理学造词，词源资料记有俄语 adron 的命名路线；它不是英语 had 加上 ron。',[['希腊 hadros；粒子名后缀 -on','粗厚、强壮；粒子名称的形式'],['20 世纪俄语 adron／国际物理学命名','为参与强相互作用的这类粒子命名'],['英语 hadron','强子，包括质子、中子等']],'这里“强”帮助你联想到强相互作用，却不是说测出某个粒子很重、很有力，它就自动属于强子。强子有内部结构；电子属于另一类粒子。Large Hadron Collider 中的 hadron 指它用于碰撞的这类粒子，不是说对撞机本身是一颗巨大粒子。','a hadron；hadrons such as protons and neutrons；the Large Hadron Collider〔大型强子对撞机〕。','proton 是一种具体的强子；hadron 是大类名称。不要把 hadron 当成“原子”的别名，原子还包括电子等部分。',('Protons and neutrons are both hadrons.','质子和中子都属于强子。'),('The lesson explains why an electron is not a hadron.','这节课解释了为什么电子不是强子。'),sources=['https://www.etymonline.com/word/hadron','https://www.merriam-webster.com/dictionary/hadron','https://www.collinsdictionary.com/dictionary/english/hadron','https://alicepublic.web.cern.ch/physics-primer','https://www.energy.gov/science/doe-explainsprotons']),
E('hadrosaur','美 /ˈhædrəˌsɔːr/','鸭嘴龙；鸭嘴龙类恐龙','先看头骨：嘴的前端形成较宽的喙，后面排列着用来磨碎植物的许多牙齿。“鸭嘴”说的是外形，不是说它是一种鸭。','接新拉丁属名 Hadrosaurus，由希腊 hadros“粗大、硕大”与 sauros“蜥蜴”组成。英语把这一属名及相关科名背景中的形式用于鸭嘴龙类；不是从物理词 hadron 变化出来。',[['希腊 hadros；sauros','粗大、硕大；蜥蜴'],['新拉丁 Hadrosaurus','按“硕大的蜥蜴”这一意象命名恐龙属'],['英语 hadrosaur','该属及相关鸭嘴龙类恐龙的通称']],'名字中的“硕大”是命名线索，今天认定某只恐龙是不是 hadrosaur，依据的是分类和身体特征，并非只看它够不够大。这一类以植物为食；有些有明显的头冠，不能把某一种的头冠套到全部成员身上。','a hadrosaur fossil；a hadrosaur skull；duck-billed dinosaurs。Hadrosaurus 是正式属名，普通名 hadrosaur 用小写。','dinosaur 范围更大，hadrosaur 是其中一类；sauros 虽本义为蜥蜴，复合名称不表示恐龙就是今天的蜥蜴。',('The museum displays the skull of a hadrosaur.','博物馆展出了一具鸭嘴龙的头骨。'),('Rows of teeth helped the hadrosaur grind plant material.','成排的牙齿帮助这只鸭嘴龙磨碎植物。'),sources=['https://www.merriam-webster.com/dictionary/hadrosaur','https://www.nhm.ac.uk/discover/dino-directory/hadrosaurus.html']),
]
cat=next(x for x in json.loads((BASE/'.cache/catalog.json').read_text()) if x['id']=='C0516');names=[w['word'] for w in W]
EX={w:'较冷门的动物属名或分类形容词，按当前通用阅读范围暂略。' for w in cat['family'] if w not in names}
ROOT=dict(id='C0516',meaning='粗厚；强壮；硕大',core='hadr- 接希腊 hadros。先想一件粗厚、结实、块头大的东西，再看科学家把这个形容用在了什么对象上。',image='hadros 粗厚、强壮 → hadron 强子；hadros + sauros → Hadrosaurus → hadrosaur 鸭嘴龙。',intro='物理学和古生物学借用了同一份希腊材料，但后来的分类规则不同。词源能帮你记名字，不能替代现代定义。',forms='hadron 结合粒子名后缀 -on，经近代国际物理命名进入英语；hadrosaur 接拉丁化的恐龙属名 Hadrosaurus，其中 -saur 来自“蜥蜴”。',branches=[['微观粒子','hadron'],['恐龙名称','hadrosaur']],contrasts='hadron 不等于一切大质量粒子；hadrosaur 也不等于一切大型恐龙。两个名字各自有独立命名路线。',practice='分别用一句话解释 hadron 和 hadrosaur，先说现代对象，再说名字借用了什么旧意象。',words=names,exclude=EX)
if __name__=='__main__':
 m=json.loads((BASE/'.cache/batch200/rewrite_vid.json').read_text()); assert set(names)<=set(m['owned_words'])
 for kind,data in [('roots',[ROOT]),('words',W)]: (OUT/(kind+'_batch200_vid_216.json')).write_text(json.dumps(data,ensure_ascii=False,indent=2))
 print('hadr:',len(W),'words;',sum(len(x['examples']) for x in W),'examples')
