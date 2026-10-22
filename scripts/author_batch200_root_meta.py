# -*- coding: utf-8 -*-
import json
from pathlib import Path
from author_batch200_root_meta_a import WA
from author_batch200_root_meta_b import WB
W=WA+WB
ROOT=dict(id='C0731',meaning='在后、越过、转变；进一步谈论自身',core='META = CHANGE / BEYOND / ABOUT ITSELF',image='先想位置从这里转到另一边，再想形态和意义发生变化；现代又常把视角向后退一步，让我们观察数据、语言、思考本身。这里有几条相连但不同的路线，不能只背一个“超”。',intro='希腊 meta 原有在后、之间、共同等用法，在复合词里又常表示变化。英语既借入希腊旧词，也不断用 meta- 造新词。它严格说属于构词前缀；本页把最有用的词族放在一起学习。',forms='meta- 在元音等环境前可出现 met-，在 method 等词里还有历史音形变化。metaphor 的 phor 是搬运，metamorphosis 的 morph 是形态；两者不能看花。meteor 接希腊“悬在空中的”旧词，不要拿“关于自身”硬套。',branches=[['把意义搬到另一边','metaphor, metaphoric, metaphorical, metaphorically'],['空中现象及其现代分工','meteor, meteoroid, meteorite, meteoric, meteorology, meteorologist, meteorological'],['改变形态、结构或状态','metamorphosis, metamorphose, metamorphosed, metamorphic, metamorphism, metabolism, metabolite, metastatic'],['在后与阶段、路径的历史用法','metaphysics, metaphysical, metaphysician, metaphase, method, methodist, methodism'],['把对象本身拿来分析','meta, metadata, metacognition, metacognitive, metalanguage, metalinguistic, metalogic, metatheory'],['现代世界构想','metaverse']],contrasts='metaphysics 名称与《物理学》之后的著作有关，现代学科不等于神秘主义。metadata 是描述数据的数据。meteorology 是气象学，保留 meteor 较早的大气现象意义。metamorphism 通常说岩石变质，metamorphosis 常说生物或事物蜕变。',practice='After using a metaphor, the teacher asked us to explain why it helped. We moved from understanding the image to thinking about our own understanding.\n\n老师用了一个隐喻，然后请我们解释它为什么有帮助。我们从理解那个画面，转到了观察自己的理解过程。',words=[w['word'] for w in W]+['method','metabolism','methodist','metastatic','metabolite','methodism','meteorology','meteorologist','meteorological'])
if __name__=='__main__':
 for name,v in [('roots_meta',[ROOT]),('words_meta_a',WA),('words_meta_b',WB)]:Path('.cache/batch200/drafts/root/'+name+'.json').write_text(json.dumps(v,ensure_ascii=False,indent=2))
 print(len(W),'individually authored words')
