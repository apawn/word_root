# coding: utf-8
import json
from pathlib import Path
from author_batch200_root_cav_a import W as A
from author_batch200_root_cav_b import W as B
W=A+B;kept=[x['word'] for x in W]
r=next(x for x in json.loads(Path('.cache/catalog.json').read_text()) if x['id']=='C0188')
EX={w:'本轮暂略更专门的流体空化术语' for w in set(r['family'])|set(r['words']) if w not in kept and '-' not in w}
ROOT=dict(id='C0188',meaning='空；凹；洞',core='CAV = HOLLOW',image='岩壁里空出一块是 cave，牙里形成的洞可叫 cavity；汤匙内面向下凹是 concave，把土挖出去留下空间是 excavate。共同点是“空出来或凹进去”。',intro='来自拉丁 cavus“空的、凹的”，有 cava 空洞、caverna 洞穴、cavare 挖空等派生。英语通过拉丁和法语借入不同词形，不是所有词都先从英语 cave 加后缀形成。',forms='cav-、cavi- 保留空腔意象；ex- 在 excavate 中表示往外；con- 在 concave 中主要加强，不能机械译成一起。cavity、concavity、excavation 都有历史名词来源。',branches=[['天然洞穴与探索','cave, cavern, cavernous, caving'],['空腔与凹面','cavity, concave, concavity'],['把东西挖出去','excavate, excavation, excavator']],contrasts='cave 是洞穴；cavity 是空腔；concave 是表面向内弯曲。cavernous 常形容空间巨大空旷，不等于真的在洞穴里。',practice='The excavator dug beside the rock, revealing a cavity that led into a small cave.\n\n挖掘机在岩石旁挖掘，露出一个通往小洞穴的空洞。',words=kept,exclude=EX)
if __name__=='__main__':
 for name,data in [('roots_cav',[ROOT]),('words_cav',W)]:Path('.cache/batch200/drafts/root/'+name+'.json').write_text(json.dumps(data,ensure_ascii=False,indent=2))
 print(len(W),sum(len(x['examples']) for x in W))
