# -*- coding: utf-8 -*-
from pathlib import Path
import json
from lesson_authoring import entry as E
BASE=Path(__file__).resolve().parents[1];OUT=BASE/'.cache/batch200/drafts/rewrite_spec'
F=['拉丁语 ficus','无花果树、无花果']
W=[
E('fig','英美 /fɪɡ/','无花果；无花果树','日常常指柔软、甜、内部带许多细小颗粒的无花果。','中古英语 fig 来自法语 figue，经奥克语 figa 等形式接拉丁 ficus。古英语也曾借入 fīc，但现代常用形式经过法语影响；更远来源不确定，不必硬接一个已知印欧词根。',[F,['奥克语 figa → 法语 figue','无花果'],['中古英语 fige → 英语 fig','无花果及其树']],'fresh figs 是鲜无花果，dried figs 是无花果干。中文叫“无花果”，不代表植物没有花：花藏在肉质的内部结构中，外面不容易看见。词根解释的是名称，不能拿中文名字代替植物结构。','a ripe fig；fresh figs；dried figs；a fig tree。','论文里的 Fig. 2 通常是 figure 2“图 2”的缩写，与水果 fig 不同源；缩写常带句点。',('She sliced a ripe fig and added it to the salad.','她切开一个成熟的无花果，放进沙拉里。'),('A fig tree grows beside the old stone wall.','旧石墙旁长着一棵无花果树。'),sources=['https://www.etymonline.com/word/fig','https://en.wiktionary.org/wiki/fig','https://www.kew.org/plants/fig']),
E('ficus','英美 /ˈfaɪkəs/','榕属植物；榕属观叶植物','保留拉丁名称的一类植物，室内植物语境常指其中用作观叶盆栽的种类。','直接借拉丁 ficus。现代植物分类把 Ficus 用作榕属的属名，小写 ficus 也进入日常英语，表示这一属的植物；它和经法语变化后的 fig 是两条传入路线。',[F,['植物分类名 Ficus','包含无花果及许多榕树的属'],['英语普通名词 ficus','榕属植物；常见于盆栽和园艺语境']],'花店里说 a ficus，往往指垂叶榕等观叶植物，而不一定是水果摊上的无花果树。这个属里有乔木、灌木等多种形态，ficus 不是只对应一种固定长相的盆栽。','a potted ficus；a ficus tree；the genus Ficus。','fig 常让人想到果实或结果的无花果树；ficus 更常用于植物分类、园艺名称。正式属名 Ficus 首字母大写，普通名词可小写。',('A tall potted ficus stands beside the office window.','办公室窗边摆着一盆高大的榕属观叶植物。'),('The label gives the ficus its full botanical name.','标签写出了这株榕属植物完整的植物学名称。'),sources=['https://en.wiktionary.org/wiki/ficus','https://www.fws.gov/species/fig-ficus','https://animals.sandiegozoo.org/plants/ficus-fig'])
]
m=json.loads((BASE/'.cache/batch200/rewrite_spec.json').read_text());r=next(r for r in m['roots']if r['id']=='C0420');family=r['family'];keep={w['word']for w in W}
ROOT=[dict(id='C0420',meaning='无花果、无花果树',core='fic-：这是植物名称，不是一个到处都能套的抽象动作。',image='一边是切开的无花果，一边是保留拉丁名称的榕属盆栽。',intro='拉丁 ficus 经法语等形式进入英语，变成常见的 fig；植物分类与园艺用语则保留 ficus。理解这两条路线，就能把水果和榕属植物联系起来。',forms='fig 的 g 是传入变化后的形式，ficus 保留拉丁外形。不要把英语单词里所有 -fic 都归到无花果；许多 -fic 另有“做、造成”的来源。',branches=[['日常水果和树名','fig'],['分类与园艺名称','ficus']],contrasts='Fig. 作为 figure 的缩写，与水果 fig 不同源。Ficus 作为植物属名，覆盖的范围也比日常某一种观叶盆栽更宽。',practice='解释 fresh figs、a potted ficus、Fig. 2 三处的不同意思。',words=list(family),exclude={},sources=['https://www.etymonline.com/word/fig','https://www.fws.gov/species/fig-ficus'])]
assert keep==set(family)
assert all(w['word']in m['owned_words']for w in W)
for w in W:assert len(w['examples'])>=2 and all(len(n)==2 and all(isinstance(x,str)and x for x in n)for n in w['history']),w['word']
for k,d in [('roots',ROOT),('words',W)]: (OUT/f'{k}_batch200_spec_126_fic.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
print('C0420',len(W),'new',sum(len(w['examples'])for w in W),'examples')
