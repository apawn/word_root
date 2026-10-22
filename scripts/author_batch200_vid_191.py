# -*- coding: utf-8 -*-
"""C1301 selen: the moon in the element name selenium."""
import json
from pathlib import Path
from lesson_authoring import entry as E
BASE=Path(__file__).resolve().parents[1];OUT=BASE/'.cache/batch200/drafts/rewrite_vid'
W=[E('selenium','/səˈliːniəm/，也读 /sɪˈliːniəm/','硒〔化学元素，符号 Se〕','它的名字来自“月亮”，原因却在地球上：发现者最初把它与碲混淆，碲的名称接“地球”，于是给相似的新元素取了一个“月亮”名字。','现代拉丁 selenium 采用希腊 selēnē“月亮”与元素名词尾 -ium，英语沿用这一科学名称；资料也有经法语 sélénium 借入的分析。名称与 tellurium“碲”的地球词源形成对应。',[['希腊 selēnē','月亮，也用于月亮女神 Selene 之名'],['现代拉丁 selenium／法语 sélénium','19 世纪科学命名，与接“地球”的 tellurium 对应'],['英语 selenium','元素硒，符号 Se']],'selenium 会出现在玻璃材料、电子材料和营养成分的文章里。这里的“月亮”说明命名背景，并不表示硒是从月球采来的。词尾 -ium 也不能用来保证元素一定是金属，硒通常归为非金属。','the element selenium；selenium compounds；trace amounts of selenium。','selenium 与 tellurium 是不同元素，命名时相互参照不等于两者相同。Selene 是神话中的名字；selenium 是元素名称，通常小写。',('The periodic table lists selenium under the symbol Se.','元素周期表以 Se 为符号列出硒。'),('The article discusses the use of selenium compounds in glass production.','这篇文章讨论了硒化合物在玻璃生产中的用途。'),sources=['https://www.etymonline.com/word/selenium','https://www.oxfordlearnersdictionaries.com/definition/english/selenium','https://periodic-table.rsc.org/element/34/selenium','https://en.wiktionary.org/wiki/selenium#English'])]
m=json.loads((BASE/'.cache/batch200/rewrite_vid.json').read_text());names=[x['word'] for x in W]
cat=next(x for x in json.loads((BASE/'.cache/catalog.json').read_text()) if x['id']=='C1301')
EX={w:'月亮神名或较冷门天文、恐惧症细分词，按当前通用阅读范围暂略。' for w in cat['family'] if w not in names}
if 'selaphobia' in EX:EX['selaphobia']='罕见恐惧症称呼，直接接光亮一系而非简单由月亮构成；按当前范围暂略，不据字母强连。'
ROOT=dict(id='C1301',meaning='月亮',core='selen- 接希腊 selēnē“月亮”。最实用的入口是 selenium：元素名字借用月亮，呼应另一个接“地球”的元素名称。',image='selēnē 月亮 → 科学命名 selenium 硒；与 tellurium 碲的“地球”命名相呼应。',intro='这个名称需要记住一小段发现史：相似物质引起混淆，命名者借地球与月亮的关系给新元素命名。它不是硒的产地说明。',forms='selenium 是现代拉丁科学名称，英语也有经法语 sélénium 借入的分析；selen- 接希腊 selēnē，-ium 为元素命名词尾。',branches=[['以月亮命名的元素','selenium']],contrasts='词源提供命名故事，不能替代化学性质。带 -ium 不保证是金属，接“月亮”也不说明这种元素只在月球上存在。',practice='从“碲的名字接地球，硒的名字接月亮”记住 selenium，而不要把它误解成月球专有物质。',words=names,exclude=EX)
if __name__=='__main__':
 assert {e['word'] for e in W}<=set(m['owned_words'])
 for kind,data in [('roots',[ROOT]),('words',W)]: (OUT/(kind+'_batch200_vid_191.json')).write_text(json.dumps(data,ensure_ascii=False,indent=2))
 print('selen:',len(W),'words;',sum(len(e['examples']) for e in W),'examples')
