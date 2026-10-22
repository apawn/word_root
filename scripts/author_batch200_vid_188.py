# -*- coding: utf-8 -*-
"""C0141 brom: an element named for its smell, then a figurative sedative."""
import json
from pathlib import Path
from lesson_authoring import entry as E
BASE=Path(__file__).resolve().parents[1];OUT=BASE/'.cache/batch200/drafts/rewrite_vid'
W=[
E('bromine','英 /ˈbrəʊmiːn/；美 /ˈbroʊmiːn/','溴〔化学元素，符号 Br〕','这个元素的名字抓住了一个很直接的特征：气味刺鼻。常温下，单质溴呈深红棕色液体。','法语 brome 用希腊 brōmos“恶臭”命名这种物质，英语采用 brome 并加化学词尾 -ine，形成 bromine。不是所有有臭味的物质都叫 bromine。',[['希腊 brōmos','恶臭、刺鼻气味'],['法语 brome → 英语旧形 brome','以气味给新发现的元素命名'],['英语 brome + -ine → bromine','现代元素名称：溴']],'bromine 可以指溴这个元素，也能在具体语境中指溴单质。含溴化合物却不一定具有单质溴那种颜色、状态或气味；元素名字不能直接当成所有化合物的外观说明。','bromine compounds；the element bromine；bromine atoms。','bromine 是元素名；bromide 通常指溴化物或溴离子一类用法。bromance“兄弟情”来自 bro 与 romance，和恶臭词根无关。',('The periodic table gives bromine the symbol Br.','元素周期表用 Br 表示溴。'),('The textbook describes bromine as a dark red liquid at room temperature.','教材把溴描述为常温下呈深红色的液体。'),sources=['https://www.etymonline.com/word/bromine','https://www.oxfordlearnersdictionaries.com/definition/english/bromine','https://periodic-table.rsc.org/element/35/bromine','https://en.wiktionary.org/wiki/bromine#English']),
E('bromide','英 /ˈbrəʊmaɪd/；美 /ˈbroʊmaɪd/','溴化物；〔贬义〕老生常谈、陈词滥调','化学书里它是溴化物；评论文章里，它可能是那句听了无数遍、仿佛只为安慰人却没有帮助的话。','bromine 的 brom- + 化学后缀 -ide。某些溴化物过去用作镇静药，这引出“让人昏昏欲睡”的比喻：乏味的人，再到乏味的陈词滥调。这种比喻在 20 世纪初由作家 Gelett Burgess 推广。',[['英语 bromine → brom- + -ide → bromide','形成溴化物的名称'],['某些 bromides 曾作镇静药','带来镇静、昏沉的历史用药联想'],['比喻 bromide','乏味的人或说了等于没说的套话']],'有人用“保持积极，一切都会好”来回应具体困难，听者可能把这句话叫 a bromide：不一定每个字都错，但陈旧、空泛，帮不上忙。这个评价带贬义。化学语境的 bromide 没有这种态度，也不能概括成“所有溴化物都是镇静药”。','potassium bromide；silver bromide；a comforting bromide；political bromides。','cliché 强调表达被用滥；bromide 尤其适合批评那种听似安慰或智慧、实际空洞的老话。bromine 与 bromide 则是不同的化学名称。',('The chemistry chapter uses silver bromide as an example of a light-sensitive compound.','这章化学内容用溴化银举例说明感光化合物。'),('Instead of answering the question, he offered a bromide about staying positive.','他没有回答问题，只说了一句要保持积极的老生常谈。'),sources=['https://www.etymonline.com/word/bromide','https://www.merriam-webster.com/dictionary/bromide','https://www.oxfordlearnersdictionaries.com/definition/english/bromide','https://periodic-table.rsc.org/element/35/bromine']),
]
m=json.loads((BASE/'.cache/batch200/rewrite_vid.json').read_text());r=next(x for x in m['roots'] if x['id']=='C0141');names=[x['word'] for x in W]
EX={w:'冷门化学分类或皮肤反应术语，按当前通用阅读范围暂略。' for w in r['family'] if w not in names}
ROOT=dict(id='C0141',meaning='恶臭、刺鼻气味',core='brom- 接希腊 brōmos“恶臭”。先用气味给溴命名，再由元素名形成化合物名称。',image='brōmos 恶臭 → brome／bromine 溴 → bromide 溴化物；某些溴化物的镇静用途 → 让人昏昏欲睡的套话。',intro='这一组的意外收获是 bromide 的文学和评论用法：从镇静药联想到乏味套话，才是现代比喻的桥梁，不是说“套话闻起来很臭”。',forms='bromine 采用法语 brome 并加 -ine；bromide 用 brom- 加 -ide。现代化学意义与后来的贬义比喻需按语境分开。',branches=[['元素','bromine'],['化合物与陈词滥调','bromide']],contrasts='气味解释元素名称的由来，不保证所有含溴化合物气味相同。bromide 的套话义经由镇静用途产生联想，不是从“恶臭”直接推出来。',practice='先判断句子在谈化学物质还是说话内容，再决定 bromide 应读成“溴化物”还是“老生常谈”。',words=names,exclude=EX)
if __name__=='__main__':
 assert {e['word'] for e in W}<=set(m['owned_words'])
 for kind,data in [('roots',[ROOT]),('words',W)]: (OUT/(kind+'_batch200_vid_188.json')).write_text(json.dumps(data,ensure_ascii=False,indent=2))
 print('brom:',len(W),'words;',sum(len(e['examples']) for e in W),'examples')
