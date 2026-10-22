# coding: utf-8
from pathlib import Path
import json
from lesson_authoring import entry as E
BASE=Path(__file__).resolve().parents[1];OUT=BASE/'.cache/batch200/drafts/rewrite_spec'
ID='C0239';TAG='268_cochl';SHARED=[];EXCLUDE_REASON='按当前范围暂略冷门耳部细分术语。'
C=[['希腊 kokhlías〔有螺旋壳的蜗牛〕','一个盘旋的外形'],['拉丁 cochlea〔蜗牛、蜗牛壳〕','后用于解剖命名'],['英语 cochlea','耳蜗：内耳里盘成螺旋的结构']]
W=[E('cochlea','英 /ˈkɒkliə/；美 /ˈkoʊkliə/','耳蜗','内耳里像蜗牛壳一样盘起来、参与听觉的结构。','经拉丁 cochlea 借入，远源是希腊 kokhlías“有螺旋壳的蜗牛”。按形状起名，比把 co- 当作共同来拆更可靠。',C,'先用蜗牛壳记外形，再理解作用：声音带来的振动传到耳蜗，内部液体和感觉细胞参与把机械振动变成电信号，随后由听觉神经传向大脑。它藏在内耳，不是我们从外面能看见的耳郭。','the cochlea of the inner ear；hair cells in the cochlea；复数 cochleae 或 cochleas。','耳蜗参与声音处理；附近的前庭、半规管与平衡功能密切相关，不能把内耳整个区域都叫 cochlea。',('The cochlea is shaped like a small spiral shell.','耳蜗的形状像一个小小的螺旋贝壳。'),('Hair cells inside the cochlea help turn vibrations into electrical signals.','耳蜗内的毛细胞帮助把振动转换成电信号。'),sources=['https://www.etymonline.com/word/cochlea','https://en.wiktionary.org/wiki/cochlea','https://www.nidcd.nih.gov/health/how-do-we-hear']),
E('cochlear','英 /ˈkɒkliə/；美 /ˈkoʊkliər/','耳蜗的；与耳蜗有关的','给后面的结构、细胞或装置标上“耳蜗相关”。','cochlea 耳蜗 + -ar 形容词后缀；词尾变成 cochlear，不是另外一种器官。',C+[['cochlea + -ar → cochlear','耳蜗相关的形容词']],'最常见搭配是 cochlear implant“人工耳蜗”。它把声音处理为用于刺激听觉神经的电信号，工作方式不同于主要放大声音的普通助听器。单词本身也可修饰 hair cells、nerve 等结构。','a cochlear implant；cochlear hair cells；the cochlear nerve。','cochlea 是器官名词，cochlear 是形容词；不少英式口音里两词听起来相同，要靠句中位置判断。',('The article explains how a cochlear implant processes sound.','这篇文章解释了人工耳蜗如何处理声音。'),('The image shows rows of cochlear hair cells.','图像显示了一排排耳蜗毛细胞。'),sources=['https://en.wiktionary.org/wiki/cochlear','https://www.nidcd.nih.gov/health/cochlear-implants'])]
ROOT=dict(meaning='蜗牛；螺旋壳；耳蜗',core='从蜗牛壳盘旋的外形，认识内耳中的耳蜗。',image='一个小螺旋壳藏在内耳，外形给它取名，内部结构参与把振动转为听觉信号。',intro='这组词不需要死记长医学定义。先抓形状：cochlea 像蜗牛壳；再抓位置和作用：在内耳，与听觉有关。',forms='希腊 kokhlías 经拉丁 cochlea 进入英语；cochlear 加上表示相关的 -ar。',branches=[['器官名称','cochlea'],['耳蜗相关','cochlear；常见于 cochlear implant']],contrasts='耳蜗不是耳郭；cochlear implant 也不是把声音单纯调大的同义说法。',practice='用“形状、位置、作用”三点解释 cochlea，再把它变成形容词。',sources=['https://www.etymonline.com/word/cochlea','https://www.nidcd.nih.gov/health/how-do-we-hear'])
m=json.loads((BASE/'.cache/batch200/rewrite_spec.json').read_text());r=next(x for x in m['roots']if x['id']==ID);c=next(x for x in json.loads((BASE/'.cache/catalog.json').read_text())if x['id']==ID);keep={w['word']for w in W}|set(SHARED);excluded={w:EXCLUDE_REASON for w in(set(r['family'])|set(c['family'])|set(c.get('unmatched',[])))-keep}
ROOT['id']=ID;ROOT['words']=list(dict.fromkeys([w for w in r['family']if w in keep]+[w for w in SHARED if w not in r['family']]));ROOT['exclude']=excluded
assert all(w['word']in m['owned_words']for w in W)
assert not(set(c['family'])|set(c.get('unmatched',[])))-set(ROOT['words'])-set(excluded)
assert {w['word']for w in W}<=set(ROOT['words'])
for w in W:assert len(w['examples'])>=2 and all(len(n)==2 and all(isinstance(x,str)and x for x in n)for n in w['history'])
for k,d in [('roots',[ROOT]),('words',W)]: (OUT/f'{k}_batch200_spec_{TAG}.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
print(ID,len(W),'new,',len(SHARED),'shared')
