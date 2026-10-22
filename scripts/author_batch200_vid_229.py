# -*- coding: utf-8 -*-
"""C1073 plinth: the supporting block beneath an object."""
import json
from pathlib import Path
from lesson_authoring import entry as E
BASE=Path(__file__).resolve().parents[1];OUT=BASE/'.cache/batch200/drafts/rewrite_vid'
W=[E('plinth','/plɪnθ/','底座；柱基；承放雕塑的基台','看雕像时，把目光往下移：托住它、把它从地面抬起来的那块基台，常叫 plinth。它是支撑物，不是雕像本身。','经法语 plinthe 或直接由拉丁 plinthus 借入，远接希腊 plinthos“砖、方石”。早期建筑用法尤其指柱基下的方形板块，后来广用于其他底座。',[['希腊 plinthos','砖、方石'],['拉丁 plinthus → 法语 plinthe','建筑底部的板块、基座'],['英语 plinth〔也有直接拉丁借入背景〕','柱基、雕像或展示物的底座']],'博物馆里 a sculpture on a plinth 说的是雕塑立在基台上。建筑语境也可指墙、柱等底部的基座或凸出部分。虽然旧词义含方砖，现代展示用的 plinth 不要求一定用砖或石头制成。','a stone plinth；a statue on a plinth；mount a sculpture on a plinth；an empty plinth。','pedestal 与 plinth 在雕塑底座语境中常重叠；plinth 往往突出底部的块状基台，具体形状仍看对象。',('The bronze statue stands on a stone plinth.','这尊铜像立在石制基座上。'),('Only the empty plinth remained after the sculpture was removed.','雕塑搬走后，只留下空空的底座。'),sources=['https://www.etymonline.com/word/plinth','https://www.oxfordlearnersdictionaries.com/definition/english/plinth','https://en.wiktionary.org/wiki/plinth#English'])]
ROOT=dict(id='C1073',meaning='砖；方石；基座',core='plinth- 接希腊 plinthos“砖、方石”。一块平整的材料放在底下托住上方物体，这个位置关系比背“基座”二字更容易记。',image='砖、方石 plinthos → 拉丁 plinthus／法语 plinthe → 英语 plinth 底座。',intro='在博物馆、公共雕塑和建筑说明中，先找“上面的物体”和“下面托住它的块体”，就能认出这个词。',forms='plinth 是借入的整词，末尾 th 读 /θ/。它不是现代英语把某个名词加 -th 构成的抽象名词。',branches=[['雕塑与建筑的底座','plinth']],contrasts='底座不是展品本身；现代 plinth 也不必用砖或石头制作。',practice='描述一尊雕像时，分别用 statue 和 plinth 说出上面的形象与下面的基台。',words=['plinth'],exclude={})
if __name__=='__main__':
 for kind,data in [('roots',[ROOT]),('words',W)]: (OUT/(kind+'_batch200_vid_229.json')).write_text(json.dumps(data,ensure_ascii=False,indent=2))
 print('plinth: 1 word; 2 examples')
