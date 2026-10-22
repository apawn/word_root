# -*- coding: utf-8 -*-
"""C0224 cirr: a curl of hair and a wispy cloud."""
import json
from pathlib import Path
from lesson_authoring import entry as E
BASE=Path(__file__).resolve().parents[1];OUT=BASE/'.cache/batch200/drafts/rewrite_vid'
W=[E('cirrus','/ˈsɪrəs/','卷云；〔生物〕卷须状的细长结构','抬头看高空那些细细白白、像散开的发丝或羽毛的云，便抓住了 cirrus 的命名画面：一绺卷发。','借自拉丁 cirrus“一绺头发、卷发、流苏”。英语先用于卷须或卷曲的细长结构，19 世纪初在云的分类中采用它，因云的外形像发丝而命名。',[['拉丁 cirrus','一绺头发、卷发、流苏'],['英语 cirrus','卷须或卷曲细长结构'],['19 世纪初气象用法 cirrus','借发丝状外观命名高空卷云']],'卷云主要由冰晶组成，常显得轻薄、纤细；这个名字说明形状，不是说云真的卷成一团头发。生物学也沿用“细长、卷曲”的画面，但普通天气阅读里通常就是卷云。','cirrus clouds；wisps of cirrus；high cirrus。专门语境中复数可用 cirri /ˈsɪraɪ/；天气描述常直接说 cirrus clouds。','cumulus 积云更像一堆棉花；cirrus 卷云更像纤细发丝。cirrhosis“肝硬化”接希腊黄褐色词，不能归成卷发的后代。',('Thin cirrus clouds stretched across the blue sky.','薄薄的卷云在蓝天中舒展开来。'),('The guide describes cirrus as high clouds made mainly of ice crystals.','指南把卷云介绍为主要由冰晶组成的高空云。'),sources=['https://www.etymonline.com/word/cirrus','https://www.oxfordlearnersdictionaries.com/definition/english/cirrus','https://weather.metoffice.gov.uk/learn-about/weather/types-of-weather/clouds/high-clouds','https://cloudatlas.wmo.int/en/observation-of-clouds-from-aircraft-descriptions-cirrus.html'])]
m=json.loads((BASE/'.cache/batch200/rewrite_vid.json').read_text())
ROOT=dict(id='C0224',meaning='卷发；细长卷曲物',core='拉丁 cirrus 是一绺卷发。看见高空像发丝一样的云，便能理解气象学为什么借它来命名。',image='拉丁 cirrus 卷发 → 卷须状结构 → 气象名称 cirrus 卷云。',intro='保留最常见的卷云义，并点出原来的形状意象。这里的 cirr- 与表示黄褐色的希腊支线分开。',forms='cirrus 是借入的拉丁名词；气象用法在近代云的分类中形成。cirri 是保留拉丁形式的复数。',branches=[['发丝般的高空云','cirrus']],contrasts='cirrus 的命名看发丝形状；cirrhosis 的命名看黄褐颜色，两者不是同一个词根。',practice='用“发丝”和“棉花堆”分别想象卷云与积云，不用把每种高空白云都叫 cirrus。',words=['cirrus'],exclude={})
if __name__=='__main__':
 assert {e['word'] for e in W}<=set(m['owned_words'])
 for kind,data in [('roots',[ROOT]),('words',W)]: (OUT/(kind+'_batch200_vid_206.json')).write_text(json.dumps(data,ensure_ascii=False,indent=2))
 print('cirr cloud:',len(W),'words;',sum(len(e['examples']) for e in W),'examples')
