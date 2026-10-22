# coding: utf-8
import json
from pathlib import Path
from author_batch200_root_can_a import W as A
from author_batch200_root_can_b import W as B
W=A+B
ROOT=dict(id='C0165',meaning='芦苇；杆、管〔标准一支远源有争议〕',core='CAN = REED / TUBE',image='一根芦苇可以拿来做杆、编篮，也让人联想到管道。另想一根用作量尺的直杆：从量尺到标准，再到公认经典。',intro='主要从希腊 kanna、拉丁 canna 的芦苇与细管意象出发。cane 保留植物茎与杖的形象；canal、channel 转向流通路径；cannon 让管子变成炮身。canon 确定来自希腊 kanon 量尺、标准，但 kanon 是否由 kanna 而来有争议，本页把它作为传统相关分支，不能说已经证实。',forms='can-、cann- 以及 channel 中的 chan- 是不同语言传入后的形式，不能按同一套英语拼写规则硬拆。can 表示能，或名词罐子，都不是本页 canna 的直接派生；canister 的金属罐义受过罐子义 can 的影响。',branches=[['植物茎、杖和容器','cane, sugarcane, canister'],['管道与流通路线','canal, channel, channeling, channelling'],['大管形象','cannon, cannonball, canyon, cannelloni'],['量尺到标准〔远源联系有争议〕','canon, canonical, canonically, canonize, canonise, canonization, canonisation']],contrasts='canon 是规范或正典，cannon 是大炮，两词同音。canal 多指人工水道，channel 可指天然水道、频道和抽象渠道。canon 一支不要把“传统关联”写成已证实的同源关系。',practice='Water flows through a canal, information travels through a channel, and a canon tells us what a tradition accepts as authoritative.\n\n水流过运河，信息经渠道传递，而一套正典告诉我们某个传统承认哪些内容具有权威。',words=[x['word'] for x in W],exclude={'canonic':'较少见的形容词形式，先掌握 canonical'})
if __name__=='__main__':
 for name,data in [('roots_can',[ROOT]),('words_can',W)]:Path('.cache/batch200/drafts/root/'+name+'.json').write_text(json.dumps(data,ensure_ascii=False,indent=2))
 meta=[]
 for w,pos,gloss,etym in [('cannelloni','noun','Large pasta tubes often filled and baked.','Borrowed from Italian cannelloni, plural of cannellone, from cannello, ultimately canna.'),('canonisation','noun','The act of recognizing a saint or establishing canonical status.','Alternative spelling of canonization; Medieval Latin canonizatio.'),('canonise','verb','To recognize as a saint or confer canonical status.','Alternative spelling of canonize; from Latin canonizare via Latin and French routes.'),('canonize','verb','To recognize as a saint or confer canonical status.','From Old French canonisier and Medieval Latin canonizare.'),('channeling','verb','Directing something along a route or toward a purpose.','Channel + -ing; usual American spelling.'),('sugarcane','noun','A tall grass grown for its sweet stems.','English sugar + cane.')]:
  x=next(x for x in W if x['word']==w);meta.append(dict(word=w,pos=pos,ipa=x['ipa'],gloss=gloss,meaning_zh=x['meaning'],etymology_text=etym,sources=x['sources']))
 Path('.cache/batch200/root_can_supplement_request.json').write_text(json.dumps(meta,ensure_ascii=False,indent=2))
 print(len(W),sum(len(x['examples']) for x in W))
