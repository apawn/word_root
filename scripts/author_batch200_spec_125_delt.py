# -*- coding: utf-8 -*-
from pathlib import Path
import json
from lesson_authoring import entry as E
BASE=Path(__file__).resolve().parents[1];OUT=BASE/'.cache/batch200/drafts/rewrite_spec'
D=['希腊语 delta；大写字母 Δ','第四个字母；三角形的字形']
W=[
E('delta','英美 /ˈdeltə/','希腊字母 Δ、δ；河口三角洲；差值或变化量','同一个字母名称，一条支线借它的形状，另一条借它作为符号的用途。','来自希腊字母 delta 的名称，更早联系腓尼基字母名。希腊人用大写 Δ 的三角形状称呼尼罗河河口，英语再把这个地理名称用于其他河流；数学的变化量义来自后来对符号 Δ 的约定。',[['腓尼基字母名 → 希腊语 delta','字母名称；更早字义联系门'],D,['英语 delta 的不同用法','字母名；河口三角洲；现代技术中的变化量']],'河流到河口减速，泥沙不断沉积，可以形成 delta；名称受三角形启发，但现代三角洲不必是整齐三角形。技术讨论里的 delta between two values 则可能只是两个数值的差，不是在说地形。','a river delta；the Nile Delta；delta T / ΔT；the delta between two values。','字母形状解释地理命名，不是所有现代用法的定义。河口只是 river mouth，有足够沉积形成相应地貌时才叫 delta。',('Several channels carry water across the river delta.','几条水道穿过这片河口三角洲。'),('In this formula, delta T represents the change in temperature.','在这个公式里，ΔT 表示温度变化量。'),sources=['https://www.etymonline.com/word/delta','https://www.oxfordlearnersdictionaries.com/definition/english/delta']),
E('deltoid','英美 /ˈdeltɔɪd/','三角肌；三角形的','形容像大写 Δ 的形状，最常见的具体对象是肩部三角肌。','接希腊 deltoeidēs“像 delta 字母的”，经拉丁 deltoideus 等解剖用语进入英语。现代可按 delt- + -oid“像……的”记；名词是 deltoid muscle 的缩略用法。',[D,['希腊语 deltoeidēs → 拉丁语 deltoideus','像 Δ 的、三角形的'],['英语 deltoid muscle → deltoid','肩部三角肌；名称取自整体形状']],'肩膀外侧鼓起的圆弧轮廓，有很大一部分来自 deltoid。名字看的是这块肌肉整体近似三角形的形状，而不是说肩膀外面长着一个平面三角形。','the deltoid muscle；the left deltoid；deltoid muscles；复数 deltoids。','deltoid 指具体肌肉或类似三角形的形状；delta 是字母名，也能指河口地形。不能看到 -oid 就把整个词理解成一种疾病。',('The anatomy model shows the deltoid covering the shoulder.','解剖模型展示了覆盖肩部的三角肌。'),('The trainer pointed to the deltoid on the diagram.','教练指了指图上的三角肌。'),sources=['https://www.etymonline.com/word/deltoid','https://www.collinsdictionary.com/us/dictionary/english/deltoid','https://en.wiktionary.org/wiki/deltoid'])
]
m=json.loads((BASE/'.cache/batch200/rewrite_spec.json').read_text());r=next(r for r in m['roots']if r['id']=='C0311');family=r['family'];keep={w['word']for w in W}
excluded={'deltahedron':'冷门几何多面体术语，按用户范围暂略。','delta-v':'用户暂略含连字符的组合词。'}
ROOT=[dict(id='C0311',meaning='希腊字母 Δ；三角形',core='delt-：先记住大写 Δ 这个三角形。',image='把大写 Δ 放在河口示意图和肩部肌肉轮廓旁，理解形状命名。',intro='这组的出发点是希腊字母 delta。河口三角洲和 deltoid 三角肌借用了字形；数学、工程里的 delta 则常借字母作变化量符号，属于另一种命名用途。',forms='delta 的词干形式 delt- 接 -oid“像……的”，形成 deltoid。不是每个含 delta 的技术词都直接从“河口”产生。',branches=[['字母与地理名称','delta'],['形状与肩部肌肉','deltoid']],contrasts='河口三角洲不一定是规则三角形；肌肉名称也只取整体近似形状。数学变化量 Δ 是符号约定，要按具体公式读。',practice='分别用一句话解释 river delta、delta T、deltoid muscle 中的核心意思。',words=[w for w in family if w in keep],exclude=excluded,sources=['https://www.etymonline.com/word/delta','https://www.etymonline.com/word/deltoid'])]
assert keep==set(family)-set(excluded)
assert all(w['word']in m['owned_words']for w in W)
for w in W:assert len(w['examples'])>=2 and all(len(n)==2 and all(isinstance(x,str)and x for x in n)for n in w['history']),w['word']
for k,d in [('roots',ROOT),('words',W)]: (OUT/f'{k}_batch200_spec_125_delt.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
print('C0311',len(W),'new',sum(len(w['examples'])for w in W),'examples')
