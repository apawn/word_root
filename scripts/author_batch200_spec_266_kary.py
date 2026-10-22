# coding: utf-8
from pathlib import Path
import json
from lesson_authoring import entry as E
BASE=Path(__file__).resolve().parents[1];OUT=BASE/'.cache/batch200/drafts/rewrite_spec'
ID='C0631';TAG='266_kary';SHARED=['eukaryote','eukaryotic'];EXCLUDE_REASON='按当前范围暂略冷门细胞核专业术语。'
K=[['希腊 pró〔在前〕与 káryon〔果核、核〕','两个来源材料用于近代细胞分类'],['法语 procaryote／新拉丁分类名 Prokaryotes','为无膜包围细胞核的生物命名']]
W=[E('prokaryote','英 /prəʊˈkæriəʊt/；美 /proʊˈkærioʊt/','原核生物','有遗传物质，但没有用核膜单独围起来的细胞核。','近代名称使用 pro- 在前、kary- 核与 -ote；词典分别记法语 procaryote 和新拉丁分类名 Prokaryotes 的借入联系。名称保留早期分类观念，不表示今天每个原核细胞都在等待变成真核细胞。',K+[['英语 prokaryote','原核生物的名词']],'细菌和古菌属于原核生物。可以把关键区别想成“DNA 有没有住在核膜围出的独立房间”：没有这间房不等于没有 DNA，也不等于没有细胞膜。','a prokaryote；bacteria and other prokaryotes；prokaryotes and eukaryotes。','eukaryote 有具膜包围细胞核的细胞组织特征；prokaryote 没有这种细胞核。病毒不因此自动成为原核生物，病毒不是细胞。',('Bacteria and archaea are prokaryotes.','细菌和古菌属于原核生物。'),('The model of a prokaryote shows DNA but no membrane-bound nucleus.','这个原核生物模型显示了 DNA，却没有核膜包围的细胞核。'),sources=['https://www.merriam-webster.com/dictionary/prokaryote','https://www.etymonline.com/word/prokaryote','https://en.wiktionary.org/wiki/prokaryote']),
E('prokaryotic','美 /ˌproʊˌkæriˈɑːtɪk/','原核的；原核生物的','用形容词指出细胞属于“没有核膜独立围出细胞核”这一类型。','现代与 prokaryote 对应，可认出 prokaryot- 与 -ic。英语形容词的记录早于英语名词的常见记录，因此历史链从近代分类词干分出，不硬画成英语名词先出现。',K+[['近代分类词干 prokaryot- + -ic → prokaryotic','原核的；与英语名词形成对应']],'prokaryotic cell 是原核细胞，prokaryotic gene 则说原核生物中的基因。形容词不只描述细胞本体，也可以把后面的分子、过程或生物归到这一语境。','prokaryotic cells；prokaryotic organisms；prokaryotic DNA。','prokaryote 指生物，prokaryotic 是修饰语；kary- 的核指细胞核，不是原子核。',('The class compared prokaryotic and eukaryotic cells.','课堂上比较了原核细胞与真核细胞。'),('The diagram shows the cell membrane surrounding a prokaryotic cell.','示意图展示了包围原核细胞的细胞膜。'),sources=['https://www.merriam-webster.com/dictionary/prokaryotic','https://www.etymonline.com/word/prokaryote'])]
ROOT=dict(meaning='果核；细胞核',core='像果实里较集中的核一样，借“核”的形象给细胞内部结构命名。',image='先想果实中的核，再看细胞遗传物质是否被核膜围在独立区域里。',intro='这组是理解基础生物课的关键。原核与真核比较的是细胞组织方式，不能简单翻译成“没有基因”和“有基因”，也不是生物好坏或高低的评价。',forms='希腊 káryon“坚果、果核”进入近代 kary-／karyo-，表示细胞核。eu- 在这里给出真正、良好的核这一命名观念；pro- 保留在前的历史观念。',branches=[['有核膜围出的细胞核','eukaryote、eukaryotic'],['无膜包围的独立细胞核','prokaryote、prokaryotic']],contrasts='原核细胞仍有 DNA 和细胞膜。-ote 是生物名词的形式，-otic 是相应形容词，不能据形式关系断言英语名词必然先出现。',practice='用“有没有核膜围出的房间”解释两类细胞，并说明原核生物为什么不等于无遗传物质。',sources=['https://www.merriam-webster.com/dictionary/prokaryote','https://www.etymonline.com/word/prokaryote'])
m=json.loads((BASE/'.cache/batch200/rewrite_spec.json').read_text());r=next(x for x in m['roots']if x['id']==ID);c=next(x for x in json.loads((BASE/'.cache/catalog.json').read_text())if x['id']==ID);keep={w['word']for w in W}|set(SHARED);excluded={w:EXCLUDE_REASON for w in(set(r['family'])|set(c['family'])|set(c.get('unmatched',[])))-keep}
ROOT['id']=ID;ROOT['words']=list(dict.fromkeys([w for w in r['family']if w in keep]+[w for w in SHARED if w not in r['family']]));ROOT['exclude']=excluded
assert all(w['word']in m['owned_words']for w in W)
assert not(set(c['family'])|set(c.get('unmatched',[])))-set(ROOT['words'])-set(excluded)
assert {w['word']for w in W}<=set(ROOT['words'])
for w in W:assert len(w['examples'])>=2 and all(len(n)==2 and all(isinstance(x,str)and x for x in n)for n in w['history'])
for k,d in [('roots',[ROOT]),('words',W)]: (OUT/f'{k}_batch200_spec_{TAG}.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
print(ID,len(W),'new,',len(SHARED),'shared')
