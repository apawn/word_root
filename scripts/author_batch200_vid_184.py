# -*- coding: utf-8 -*-
"""C0873 olig: few; politics, markets and a historical geological name."""
import json
from pathlib import Path
from lesson_authoring import entry as E
BASE=Path(__file__).resolve().parents[1];OUT=BASE/'.cache/batch200/drafts/rewrite_vid'
W=[
E('Oligocene','英 /ˈɒlɪɡəʊˌsiːn/；美 /ˈɑːlɪɡoʊˌsiːn/','渐新世；渐新世的','这个年代名里的“少”，说的是命名时观察到的、与现生类型相近的化石所占比例少，不是说当时地球上没多少生命。','德国地质学者贝里希用希腊 oligos“少”与 kainos“新的”对应的 -cene 构件，造出德语 Oligocän，后借入英语 Oligocene。现在德语通常拼 Oligozän。',[['希腊 oligos + kainos 对应的地质构件','少 + 新、近代的'],['德语 Oligocän〔贝里希命名〕','借少量现代型化石的观察命名地层时段'],['英语 Oligocene','渐新世这一正式年代名及相应形容词']],'渐新世大约在距今三千四百万至二千三百万年之间，位于始新世之后、中新世之前，属于古近纪。名称来自早期比较化石的分类方式；理解词源时，不要误读成“这个时期很短”或“物种总数很少”。英文通常大写。','the Oligocene；the Oligocene Epoch；Oligocene rocks；Oligocene mammals。','oligo- 在 oligarchy 中数掌权者，在 Oligocene 中涉及旧化石分类的相对比例；“少”的对象不同。年代名不能仅凭字面翻译推算其起止时间。',('The museum displays fossils from the Oligocene.','博物馆展出了渐新世的化石。'),('These Oligocene rocks preserve evidence of a cooler climate.','这些渐新世岩层保存了气候转凉的证据。'),sources=['https://www.etymonline.com/word/Oligocene','https://www.merriam-webster.com/dictionary/Oligocene','https://www.collinsdictionary.com/dictionary/english/oligocene','https://www.usgs.gov/youth-and-education-in-science/cenozoic']),
]
m=json.loads((BASE/'.cache/batch200/rewrite_vid.json').read_text());r=next(x for x in m['roots'] if x['id']=='C0873');SH=['oligarchy','oligarch','oligopoly','oligosaccharide'];names=SH+[x['word'] for x in W]
EX={w:'专门水域营养状态术语，按当前通用阅读范围暂略。' for w in r['family'] if w not in names}
ROOT=dict(id='C0873',meaning='少数、少量',core='olig-／oligo- 接希腊 oligos“少”。先问“少的是什么”，就能把政治上的少数人、市场中的少数卖方与分子中的少数单位分开。',image='少数人 + 掌权 → oligarchy；少数卖方 → oligopoly；少量糖单位 → oligosaccharide；少量现代型化石的旧命名 → Oligocene。',intro='这组的通用阅读价值主要在权力与市场：少数成员能控制大部分决定或交易。它们不是只按人数做简单点名，而是在描述权力或市场结构。',forms='oligarchy 与 oligarch 经希腊、拉丁化和法语路线借入；oligopoly 有拉丁型来源与仿 monopoly 的英语构词分析。Oligocene 先由德语地质学命名，再进入英语。',branches=[['少数人的权力','oligarchy, oligarch'],['少数卖方的市场','oligopoly'],['少量单位与地质命名','oligosaccharide, Oligocene']],contrasts='oligarchy 谈掌权，oligopoly 谈卖方市场，不是一个词的两个拼法。oligo- 不自动意味着“体积小”，更常是在数某一类成员或单位。',practice='给每个词补一句“少数的是……”：掌权者、卖方、糖单位，或地质命名时比较的现代型化石。',words=names,exclude=EX)
if __name__=='__main__':
 assert {e['word'] for e in W}<=set(m['owned_words'])
 for kind,data in [('roots',[ROOT]),('words',W)]: (OUT/(kind+'_batch200_vid_184.json')).write_text(json.dumps(data,ensure_ascii=False,indent=2))
 print('olig:',len(W),'words;',sum(len(e['examples']) for e in W),'examples')
