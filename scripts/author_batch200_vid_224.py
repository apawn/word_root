# -*- coding: utf-8 -*-
"""C1181 pyrrh: modern reading meaning must pass through the proper name."""
import json
from pathlib import Path
from lesson_authoring import entry as E
BASE=Path(__file__).resolve().parents[1];OUT=BASE/'.cache/batch200/drafts/rewrite_vid'
W=[E('pyrrhic','/ˈpɪrɪk/','代价过于惨重、得不偿失的〔常写 Pyrrhic〕','官司赢了，巨额开支却把公司拖垮；争吵赢了，关系却毁了。赢的是眼前这一局，失去的东西却多到让胜利失去意义。','常用的 Pyrrhic victory 来自伊庇鲁斯国王 Pyrrhus 的名字：他虽击败罗马军队，自己也损失惨重。名字远接希腊 pyrrhos“火红的、红发的”，再接 pyr“火”。关键的语义转折是历史人物及其战事，不是“火红”直接等于“惨胜”。',[['希腊 pyr → pyrrhos','火 → 火红的、红发的'],['人名 Pyrrhos → 拉丁化 Pyrrhus','伊庇鲁斯国王皮洛士的名字'],['英语 Pyrrhic；Pyrrhic victory','像皮洛士那样付出惨重代价的胜利']],'它不只是“赢得很辛苦”，而是代价可能抵消甚至超过胜利的好处。小写 pyrrhic 另有古希腊战舞、双短音节音步等较专门用法，经希腊舞名和拉丁语传来，不能把那些诗律含义也解释成惨胜。','a Pyrrhic victory；a victory that proves Pyrrhic。这个胜利义常保留人名来源的大写 P，文章中也可见小写。','a narrow victory 是险胜，重点在差距小；a Pyrrhic victory 重点在代价太大，两者不必同时发生。',('Winning the lawsuit proved a Pyrrhic victory because the costs ruined the company.','赢下官司成了一场得不偿失的胜利，因为费用把公司拖垮了。'),('He won the argument, but the loss of their friendship made it a Pyrrhic victory.','他赢了争论，却失去了友谊，这场胜利反而得不偿失。'),sources=['https://www.etymonline.com/word/Pyrrhic','https://www.merriam-webster.com/dictionary/pyrrhic','https://www.collinsdictionary.com/dictionary/english/pyrrhic','https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Plutarch/Lives/Pyrrhus%2A.html'])]
ROOT=dict(id='C1181',meaning='火红色〔经人名形成的常见表达另看具体历史〕',core='pyrrh- 的远处是希腊“火红的”。但阅读里最值得记的 Pyrrhic victory，要先经过人名 Pyrrhus，再经过那场代价惨重的胜利。',image='火 → 火红、红发 → 人名 Pyrrhus → Pyrrhic victory 得不偿失的胜利。',intro='这是一个不能直接按词根翻译全词的例子。红色解释名字的远源，历史故事才解释现代的“惨胜”。',forms='Pyrrhic 的常用形容词义由 Pyrrhus 人名加 -ic 构成。小写 pyrrhic 的古代舞蹈和诗律义有另外的希腊、拉丁借入路线。',branches=[['胜利却付出过高代价','pyrrhic']],contrasts='惨胜与险胜不同：险胜看比分或实力差距，Pyrrhic victory 看损失和代价。不要把它记成“像火一样的胜利”。',practice='想一个“眼前赢了，整体却赔得更多”的场景，用 a Pyrrhic victory 描述。',words=['pyrrhic'],exclude={})
if __name__=='__main__':
 for kind,data in [('roots',[ROOT]),('words',W)]: (OUT/(kind+'_batch200_vid_224.json')).write_text(json.dumps(data,ensure_ascii=False,indent=2))
 print('pyrrh: 1 word; 2 examples')
