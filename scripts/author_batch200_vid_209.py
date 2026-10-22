# -*- coding: utf-8 -*-
"""C1110 potam: river in a place name and an animal name."""
import json
from pathlib import Path
from lesson_authoring import entry as E
BASE=Path(__file__).resolve().parents[1];OUT=BASE/'.cache/batch200/drafts/rewrite_vid'
W=[E('Mesopotamia','/ˌmesəpəˈteɪmiə/','美索不达米亚；两河流域','先在地图上放两条河：底格里斯河和幼发拉底河。这个地名的字面意思，就是河流之间的地方。','由希腊 mesos“中间”与 potamos“河”形成 mesopotamos“在河流之间的”，地名 Mesopotamia 原来可与 khōra“土地、地区”连用；经拉丁形式进入英语。它不是现代英语先有 meso 再拼出的地名。',[['希腊 mesos；potamos','中间；河——两种并列材料'],['希腊 Mesopotamia〔khōra〕','河流之间的地区'],['拉丁 Mesopotamia → 英语 Mesopotamia','沿用古典地名，今常称两河流域']],'历史书中的范围大体围绕两河及其周边，主要涉及今天的伊拉克，也包括邻近地区。它是地理和历史区域名，不是说几千年间这里始终只有同一个国家或同一种文明。','ancient Mesopotamia；the cities of Mesopotamia；writing in Mesopotamia。专名首字母大写。','Iraq 是现代国家名，Mesopotamia 是历史地理名称，两者范围并不完全重合；Sumer、Assyria 等则指其中不同时期的地区或政治文化实体。',('The map shows the Tigris and Euphrates rivers in ancient Mesopotamia.','地图展示了古代美索不达米亚的底格里斯河和幼发拉底河。'),('The exhibition explores urban life in Mesopotamia.','展览探讨了美索不达米亚的城市生活。'),sources=['https://www.etymonline.com/word/Mesopotamia','https://www.collinsdictionary.com/dictionary/english/mesopotamia','https://www.arch.cam.ac.uk/about-us/mesopotamia/mesopotamia-history','https://www.metmuseum.org/exhibitions/listings/2003/art-of-the-first-cities'])]
m=json.loads((BASE/'.cache/batch200/rewrite_vid.json').read_text());names=['hippopotamus','Mesopotamia']
cat=next(x for x in json.loads((BASE/'.cache/catalog.json').read_text()) if x['id']=='C1110')
EX={w:'冷门河流学、鱼类洄游或命名细分术语，按当前通用阅读范围暂略。' for w in cat['family'] if w not in names}
ROOT=dict(id='C1110',meaning='河流',core='potam- 接希腊 potamos“河”。放进动物名里是“河里的马”，放进地名里则是“两条河之间的地区”。',image='potamos 河 + hippos 马 → hippopotamus 河马；mesos 中间 + potamos 河 → Mesopotamia 两河流域。',intro='用动物和地图两幅画面记住这一根，比背河流学的长词更有用。两个常见名称都沿用古典组合，今天的实际含义还要看分类与历史语境。',forms='hippopotamus 经希腊合成名和拉丁形式传入；Mesopotamia 是希腊地名经拉丁流传。二者中的 potam- 都可靠地指河流。',branches=[['河里的动物名称','hippopotamus'],['河流之间的历史地区','Mesopotamia']],contrasts='河马并不是马科动物；Mesopotamia 也不是现代伊拉克国界的精确同义词。字面解释名称，不能替代现代分类和地理范围。',practice='分别用“河 + 马”和“中间 + 河”解释两个名称，再各补一句今天的准确含义。',words=names,exclude=EX)
if __name__=='__main__':
 assert {e['word'] for e in W}<=set(m['owned_words'])
 for kind,data in [('roots',[ROOT]),('words',W)]: (OUT/(kind+'_batch200_vid_209.json')).write_text(json.dumps(data,ensure_ascii=False,indent=2))
 print('potam:',len(W),'words;',sum(len(e['examples']) for e in W),'examples')
