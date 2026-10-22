# -*- coding: utf-8 -*-
from pathlib import Path
import json
from lesson_authoring import entry as E
BASE=Path(__file__).resolve().parents[1];OUT=BASE/'.cache/batch200/drafts/rewrite_spec'
X=['希腊语 exo','在外面、外部']
EHist=[X,['希腊语 exotikos → 拉丁 exoticus','来自外部的、外来的'],['法语 exotique；亦有直接拉丁借入','外来的'],['英语 exotic','异域的；少见而特别的']]
W=[
E('exotic','英 /ɪɡˈzɒtɪk/；美 /ɪɡˈzɑːtɪk/','异域的；外来的；新奇少见的','对眼前这个地方或人来说，来自熟悉范围之外，显得不寻常。','经法语 exotique 或拉丁 exoticus，接希腊 exotikos“外来的”，再接 exo“在外”。这是借入的整体形容词，不是现代英语 ex- 表示“前任”。',EHist,'exotic plants 可以说本地少见的外来植物。这个感觉取决于观察位置：一种水果在某地新奇，在原产地却可能很普通。技术文章里的 exotic materials 则常只强调材料特殊、不常用。','exotic plants；exotic fruit；exotic materials；an exotic destination。','foreign 主要说明来自别国，exotic 往往还带陌生、新奇的感受。外来不等于危险，也不等于稀有或昂贵。',('The greenhouse contains exotic plants that cannot survive the local winter outdoors.','温室里种着一些无法在当地户外越冬的外来植物。'),('The design works without expensive or exotic materials.','这个设计无需昂贵或少见的特殊材料也能实现。'),sources=['https://www.etymonline.com/word/exotic','https://en.wiktionary.org/wiki/exotic']),
E('exoskeleton','英 /ˌeksəʊˈskelɪtən/；美 /ˌeksoʊˈskelɪtən/','外骨骼；穿戴式外骨骼装置','支撑、保护身体的结构在外面，像把骨架穿在身外。','英语 exo-“外部” + skeleton“骨架”。skeleton 更早经拉丁接希腊 skeleton“干枯的身体”；组合成 exoskeleton 是近代科学构词，不是古希腊已有的整词直接搬来。',[X,['近代英语 exo- + skeleton','外部 + 支撑骨架'],['英语 exoskeleton','动物体外的支撑保护结构；后扩展到穿戴设备']],'螃蟹的硬壳是典型外骨骼，不必由人的骨头那种材料构成。工程中把穿在身体外、帮助支撑或运动的装置也叫 exoskeleton，借的是位置和功能。','a crab’s exoskeleton；shed an exoskeleton；a powered exoskeleton；wear an exoskeleton。','endoskeleton 是内骨骼，exo- 把位置移到外面。工程装置是否有动力要另看说明，名称本身不保证一定带电机。',('The crab sheds its exoskeleton as it grows.','螃蟹生长时会蜕去外骨骼。'),('The engineers tested an exoskeleton designed to support a worker’s arms.','工程师测试了一套用于支撑工人手臂的外骨骼装置。'),sources=['https://www.etymonline.com/word/exoskeleton','https://www.oxfordlearnersdictionaries.com/definition/english/exoskeleton','https://www.collinsdictionary.com/dictionary/english/exoskeleton']),
E('exoticism','英 /ɪɡˈzɒtɪsɪzəm/；美 /ɪɡˈzɑːtɪsɪzəm/','异域情调；对异域特色的表现或追求','谈一种作品或体验如何营造“来自远方、不同于日常”的感觉。','英语 exotic + -ism，把异域感变成可讨论的性质或审美倾向。这里 -ism 不必指一个政治主义。',EHist+[['英语 exotic + -ism → exoticism','异域情调；表现、追求异域特色的倾向']],'在评论小说、音乐或设计时，exoticism 常是作者赋予远方事物的陌生感。它不等于对某个地方的准确介绍；有时艺术家是在营造想象中的远方。','the exoticism of a setting；musical exoticism；an air of exoticism；a taste for exoticism。','exotic 是形容词，exoticism 是这种感觉或表现方式的名词。authenticity 强调真实可靠，exoticism 强调观看者感到陌生新奇，二者不是同一标准。',('The novel relies on the exoticism of its setting to attract readers.','这部小说借助背景的异域情调吸引读者。'),('The exhibition examines exoticism in nineteenth-century painting.','这场展览探讨十九世纪绘画中的异域情调。'),sources=['https://www.etymonline.com/word/exoticism','https://www.oxfordlearnersdictionaries.com/definition/english/exoticism'])
]
m=json.loads((BASE/'.cache/batch200/rewrite_spec.json').read_text());r=next(r for r in m['roots']if r['id']=='C0396');family=r['family'];keep={w['word']for w in W}|{'exogenous','exoplanet','exothermic','exosphere'}
excluded={w:'按用户范围暂略细分专业术语和少见书面派生词。'for w in set(family)-keep}
for w in ['exo-ocean','exo-isomer','exo-steric']:excluded[w]='按用户要求暂略带连字符的词条。'
ROOT=[dict(id='C0396',meaning='外面；外部',core='exo-：在某个范围或结构之外；先弄清楚“相对于什么在外”。',image='把骨架放到身体外，把目光移到熟悉范围之外。',intro='希腊 exo 表示在外面。exotic 是很早整体借入的形容词；exoskeleton、exoplanet 等则利用 exo- 组合出近代科学词。外面可以是身体外、系统外，也可以是太阳系外，不能把所有外部都理解成国外。',forms='exo- 是希腊来源的组合形式，常与其他词干组成科学词；exotic 经过希腊、拉丁和法语借入，不能套成“前任”的 ex-。',branches=[['熟悉范围之外','exotic、exoticism'],['身体或系统之外','exoskeleton、exogenous'],['天文与能量方向','exoplanet、exosphere、exothermic']],contrasts='exotic 带观察者的陌生感，不等于每个外来事物都稀奇。科学词中的 exo- 必须结合后半部分判断外部范围。',practice='比较 exotic plants 与 exoskeleton：一个说熟悉范围之外，另一个说身体结构在外部。',words=[w for w in family if w in keep],exclude=excluded,sources=['https://www.etymonline.com/word/exotic','https://www.etymonline.com/word/exoskeleton'])]
assert keep==set(family)-set(excluded)
assert all(w['word']in m['owned_words']for w in W)
for w in W:assert len(w['examples'])>=2 and all(len(n)==2 and all(isinstance(x,str)and x for x in n)for n in w['history']),w['word']
for k,d in [('roots',ROOT),('words',W)]: (OUT/f'{k}_batch200_spec_142_exo.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
print('C0396',len(W),'new',sum(len(w['examples'])for w in W),'examples')
