# -*- coding: utf-8 -*-
from pathlib import Path
import json
from lesson_authoring import entry as E
BASE=Path(__file__).resolve().parents[1];OUT=BASE/'.cache/batch200/drafts/rewrite_spec'
H=[['希腊 ana- + ienai → anienai','向上 + 走 → 上行'],['希腊 anion','上行之物'],['19 世纪英语电化学术语 anion','与 anode 配套命名；现代定义为负离子']]
W=[
E('anion','英 /ˈænaɪən/，亦 /ˈænaɪɒn/；美 /ˈænaɪən/','阴离子；负离子','整体带负电的原子或原子团。','19 世纪电化学命名借希腊 anion“上行之物”，来自 ana-“向上” + ienai“走”，与 anode“阳极”配套。这里的 an- 不是表示“没有”的否定前缀。',H,'Cl⁻ 是氯离子，整体带一个单位负电；SO₄²⁻ 是多个原子组成的硫酸根离子，整体带两个单位负电。现代定义看电荷，不是看它是否真的朝上移动。','a chloride anion；a sulfate anion；anion exchange。','anion 是带负电的离子，anode 是阳极这一电极名称。两者一个是粒子，一个是电极；电解时阴离子趋向阳极。',('A chlorine atom forms an anion when it gains an electron.','一个氯原子获得一个电子时会形成阴离子。'),('The sulfate anion contains one sulfur atom and four oxygen atoms.','硫酸根阴离子含有一个硫原子和四个氧原子。'),sources=['https://www.merriam-webster.com/dictionary/anion','https://dictionary.cambridge.org/dictionary/english/anion','https://goldbook.iupac.org/terms/view/A00358']),
E('anionic','美 /ˌænaɪˈɑːnɪk/，亦 /ˌæniˈɑːnɪk/','阴离子的；阴离子型的','用于描述带负电的粒子、基团，或以阴离子为活性成分的物质。','英语 anion + -ic，构成形容词。更早的 anion 来自希腊“上行之物”，不是 a- 否定 ionic，所以 anionic 绝非“不是离子的”。',H+[['英语 anion + -ic → anionic','与阴离子有关的；阴离子型的']],'anionic group 说的是带负电的基团；anionic surfactant 则按活性部分的电荷分类。词里多出来的 -ic 只是让名词能修饰其他词，不改变负电这个核心。','anionic groups；anionic surfactants；anionic dyes。','anionic 与 cationic 分别是阴离子型、阳离子型；nonionic 才是不属于离子型的。不要把 anionic 误解成 nonionic。',('The diagram marks the negatively charged group as anionic.','图中把带负电的基团标为阴离子型。'),('The researcher compared anionic and nonionic surfactants.','研究人员比较了阴离子型与非离子型表面活性剂。'),sources=['https://www.merriam-webster.com/dictionary/anionic','https://en.wiktionary.org/wiki/anionic#English'])
]
m=json.loads((BASE/'.cache/batch200/rewrite_spec.json').read_text());assert all(x['word'] in m['owned_words'] for x in W)
assert all(len(x['examples'])>=2 and all(len(n)==2 and all(isinstance(v,str) and v for v in n) for n in x['history']) for x in W)
(OUT/'words_batch200_spec_ana_ions.json').write_text(json.dumps(W,ensure_ascii=False,indent=2)+'\n')
print('ana standalone',len(W),'words',sum(len(x['examples']) for x in W),'examples')
