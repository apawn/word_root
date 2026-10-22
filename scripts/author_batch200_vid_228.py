# -*- coding: utf-8 -*-
"""C1322 ser: an evening, through French, becomes a party."""
import json
from pathlib import Path
from lesson_authoring import entry as E
BASE=Path(__file__).resolve().parents[1];OUT=BASE/'.cache/batch200/drafts/rewrite_vid'
W=[E('soiree','英 /ˈswɑːreɪ/；美 /swɑːˈreɪ/〔也写 soirée〕','晚间社交聚会；晚会','晚上邀请一些人来聊天、听音乐、看表演，这种带一点正式或文雅气氛的聚会可以叫 soiree。','借法语 soirée，由 soir“晚上”加法语 -ée 形成。soir 经古法语接拉丁 sero“在晚些时候”，与 serus“晚的”相关；英语借入的是法语整词，不是英语 so 加 ree。',[['拉丁 serus；sero','晚的；在晚些时候'],['古法语／法语 soir → soirée','晚上 → 一晚、晚间活动'],['英语 soiree／soirée','晚间社交聚会、晚会']],'它比 party 更带法语式的正式、艺术社交色彩，常见 a musical soiree。也有人故意用它把普通聚会说得文雅或带点幽默。核心是晚间聚会，不要求一定有盛装、舞会或大型宴席。','host a soiree；a musical soiree；an invitation to a soiree。法语重音符号可保留，英文也常省去。','party 是很广的聚会名称；soiree 把时间和社交气氛说得更具体。它不等于“迟到的聚会”，late 是词源里的晚间时间线索。',('They hosted a small musical soiree for friends.','他们为朋友们举办了一场小型晚间音乐聚会。'),('The invitation described the gathering as an informal soiree.','请柬把这次聚会称为一场轻松的晚间聚会。'),sources=['https://www.etymonline.com/word/soiree','https://www.oxfordlearnersdictionaries.com/definition/english/soiree'])]
cat=next(x for x in json.loads((BASE/'.cache/catalog.json').read_text()) if x['id']=='C1322');EX={w:'较冷门的蝙蝠名称、晚熟形态或植物迟开裂术语，按当前通用阅读范围暂略。' for w in cat['family'] if w!='soiree'}
ROOT=dict(id='C1322',meaning='晚；在晚些时候',core='这一条 ser- 接拉丁 serus“晚的”。通过法语 soir“晚上”，就走到了今天的 soiree“晚间聚会”。',image='serus／sero 晚 → 法语 soir 晚上 → soirée → 英语 soiree 晚间聚会。',intro='这里最实用的词已经看不见 ser- 的原样。沿法语的变化走一遍，才能知道为什么一个晚会名称属于“晚”这一族。',forms='soiree 是法语整词借入，常保留 soirée 的拼写。不要把它归到表示串联、系列或血清的其他 ser- 来源。',branches=[['晚间聚会','soiree']],contrasts='“晚”表示一天中的时段，不是聚会迟到；soiree 也不自动等于正式舞会。',practice='想象一场小型晚间音乐聚会，用 musical soiree 把时间和气氛一起表达出来。',words=['soiree'],exclude=EX)
if __name__=='__main__':
 for kind,data in [('roots',[ROOT]),('words',W)]: (OUT/(kind+'_batch200_vid_228.json')).write_text(json.dumps(data,ensure_ascii=False,indent=2))
 print('ser: 1 word; 2 examples')
