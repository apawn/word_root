# coding: utf-8
import json
from pathlib import Path
from lesson_authoring import entry as E
W=[E('arable','/ˈærəbəl/','适合耕种的；种植作物的','能翻土、播种、收庄稼的那种土地。','拉丁 arare 耕地 + 表示能够的 -bilis → arabilis 可耕种的，经古法语 arable 进入英语。',[['拉丁 arare → arabilis','耕地 → 适合耕种的'],['古法语 arable → 英语 arable','可耕的；种植作物的']],'arable land 通常指适于种植作物的土地，或农业分类中的耕地；它与一直作牧场、林地的土地相对。arable farming 重点是种庄稼。这个词不保证土地特别肥沃，更不表示每一寸地此刻都长着作物。','arable land；arable farming；arable crops。','fertile 强调肥沃、利于生长；arable 强调耕种用途或条件。两个性质相关，但不是同一个意思。',('Most of the arable land around the village is used to grow wheat.','村子周围的大部分耕地用来种小麦。'),('The steep, rocky slopes leave little arable land on the island.','岛上山坡陡峭、多岩石，能耕种的土地很少。'),sources=['https://www.etymonline.com/word/arable','https://en.wiktionary.org/wiki/arable#English'])]
ROOT=dict(id='C0067',meaning='犁地；耕种',core='ARA = PLOUGH',image='犁头翻开泥土，准备播下庄稼；arable 就是能进行这件事的。',intro='拉丁 arare 表示犁地、耕种。最实用的后代是 arable，可从土地能否用于种庄稼来理解。',forms='arare → arabilis → 古法语 arable → 英语 arable。-able 对应更早拉丁语中的可……形式，整个词经法语借入。',branches=[['可耕种的土地','arable']],contrasts='arable 是耕种这一特定用途；agricultural 涉及农业整体，也可包括畜牧业。不要把所有农业用地都自动等同于 arable land。',practice='The farm has both arable land and pasture.\n\n这个农场既有耕地，也有牧场。',words=['arable'],exclude={w:'低频派生或古旧术语，本轮略过。' for w in ['arability','aration','exarate','exaration','inarable','nonarable','aratory']})
if __name__=='__main__':
 for name,data in [('roots_ara',[ROOT]),('words_ara',W)]:Path('.cache/batch200/drafts/root/'+name+'.json').write_text(json.dumps(data,ensure_ascii=False,indent=2))
 print(len(W),sum(len(x['examples']) for x in W))
