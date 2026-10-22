# -*- coding: utf-8 -*-
"""C0107 axon: an axis-shaped extension of a neuron."""
import json
from pathlib import Path
from lesson_authoring import entry as E
BASE=Path(__file__).resolve().parents[1];OUT=BASE/'.cache/batch200/drafts/rewrite_vid'
W=[
E('axon','英 /ˈæksɒn/；美 /ˈæksɑːn/','轴突','从神经元细胞体伸出去的一段细长结构，可以把神经信号传向其他细胞。把它先想成这个细胞向外铺出的线路。','接希腊 axōn“轴、轴线”，经新拉丁解剖用语进入英语。早期英语也用 axon 表身体的轴线，19 世纪末用于神经元的这段伸长结构；名称借用了轴状的形象。',[['希腊 axōn','轴、轴线'],['新拉丁／英语解剖用语 axon','先有轴线的命名背景'],['英语神经科学 axon','神经元伸出的轴突']],'轴突是一个细胞的一部分，不是一整根肉眼可见的神经。许多轴突可以集合成神经束，外围还会有其他组织；有些轴突外面包有髓鞘。线路只是比喻，实际信号传递依靠细胞的电化学活动。','an axon；axon terminals；a myelinated axon；axon growth。','neuron 是整个神经元，axon 是它的轴突。dendrites 是树突，通常更像接收信息的分枝；轴突通常承担向外传递信号的角色。',('The signal travels along the axon toward its terminals.','信号沿着轴突向它的末端传去。'),('The model shows an axon extending from the cell body.','模型展示了一条从细胞体伸出的轴突。'),sources=['https://www.merriam-webster.com/dictionary/axon','https://www.oxfordlearnersdictionaries.com/definition/english/axon','https://www.etymonline.com/word/axon','https://www.nichd.nih.gov/health/topics/neuro/conditioninfo/Pages/parts.aspx']),
E('axonal','/ˈæksənəl/','轴突的；与轴突有关的','把注意力缩到神经元的轴突这一部分。axonal damage 就是轴突受损；axonal transport 则是物质沿轴突内部运输。','英语 axon“轴突”加形容词后缀 -al。axon 远接希腊 axōn“轴”，而 axonal 是以英语解剖名词为词基形成的形容词。',[['希腊 axōn → 解剖用语 axon','轴线 → 神经元的轴突'],['英语 axon + -al','轴突 + 有关的'],['英语 axonal','描述轴突的结构、功能或变化']],'axonal transport 像在细长通道里搬运蛋白质、细胞器等材料，和神经冲动的快速传递不是同一个过程。axonal 这个词帮助文章说明：讨论的具体位置是轴突，而不是整个脑或整条神经。','axonal transport；axonal damage；axonal growth；axonal degeneration。另有把重音放在第二音节的读法。','neural 泛指神经系统相关；axonal 更具体，限定在轴突。axial 是“轴向的、轴线的”，也不能随意替换 axonal。',('The study examined axonal growth in cultured neurons.','这项研究观察了培养的神经元中轴突的生长。'),('Axonal transport moves materials along the length of the axon.','轴突运输把物质沿轴突内部送往不同位置。'),sources=['https://www.merriam-webster.com/dictionary/axonal','https://www.collinsdictionary.com/dictionary/english/axonal','https://en.wiktionary.org/wiki/axonal#English','https://www.ncbi.nlm.nih.gov/books/NBK26930/']),
]
m=json.loads((BASE/'.cache/batch200/rewrite_vid.json').read_text());names=[x['word'] for x in W]
cat=next(x for x in json.loads((BASE/'.cache/catalog.json').read_text()) if x['id']=='C0107')
EX={w:'较冷门的投影方法、纤维描记或神经损伤分型词，按当前通用阅读范围暂略。' for w in cat['family'] if w not in names}
ROOT=dict(id='C0107',meaning='轴；轴线',core='希腊 axōn 是轴。解剖学把这个轴状、伸长的画面用到神经元上，形成 axon 轴突。',image='轴、轴线 axōn → 解剖词 axon 轴突 → axonal 轴突的。',intro='这一页先分清大小层级：整个细胞叫 neuron，伸出的轴突叫 axon，讨论轴突的性质时用 axonal。',forms='axon 接希腊 axōn，经学术解剖用语传入；axonal 是英语 axon + -al。不要把词尾 -on 误当成每个神经词共有的独立词根。',branches=[['轴状的神经元结构','axon, axonal']],contrasts='axon 是细胞的一部分，nerve 常是许多神经纤维组成的束状结构。axonal transport 运输细胞材料，不等同于神经冲动的传播。',practice='用一幅脑中的画面区分细胞体、树突和轴突，再用 axonal transport 说一句物质沿轴突运输的例子。',words=names,exclude=EX)
if __name__=='__main__':
 assert {e['word'] for e in W}<=set(m['owned_words'])
 for kind,data in [('roots',[ROOT]),('words',W)]: (OUT/(kind+'_batch200_vid_204.json')).write_text(json.dumps(data,ensure_ascii=False,indent=2))
 print('axon:',len(W),'words;',sum(len(e['examples']) for e in W),'examples')
