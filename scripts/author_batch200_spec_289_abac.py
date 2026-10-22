# coding: utf-8
from pathlib import Path
import json
from lesson_authoring import entry as E
BASE=Path(__file__).resolve().parents[1];OUT=BASE/'.cache/batch200/drafts/rewrite_spec'
ID='C0002';TAG='289_abac';SHARED=[];EXCLUDE_REASON='按当前范围暂略罕见建筑细分和另写形式，主要掌握 abacus。'
W=[E('abacus','/ˈæbəkəs/','算盘；计算板；柱顶板〔建筑〕','通常是一框可以拨动的珠子，用它的位置表示数。','经拉丁 abacus 借入，接希腊 ábax、词干 abak-：板、计算台。更早词源有争议，不能把“来自某个表示尘土的词”当成定论。',[['希腊 ábax／abak-〔板、计算台〕','可以承托、绘写或计算的平板'],['拉丁 abacus → 英语 abacus','板与计算工具的名称；建筑另保留柱顶板义'],['现代常见算盘义','用框架中可移动的珠子表示数']],'古代名称并不限于今天熟悉的珠算盘，也可说用来计算的台板。现代 an abacus 通常让人想到拨珠算数；看建筑书时，它可能是柱头最上面的平板，与算术无关。两种意思都能追到“板、台”的旧义。','use an abacus；calculate on an abacus；复数 abacuses，也有 abaci。','calculator 泛指计算器；abacus 是靠移动珠子等实物表示数的工具，不是电子机器。柱顶板义要靠建筑上下文辨认。',('The child used an abacus to add the two numbers.','孩子用算盘把两个数相加。'),('The diagram shows the abacus above the rounded part of the column’s capital.','图中柱顶板位于柱头圆曲部分的上方。'),sources=['https://www.etymonline.com/word/abacus','https://www.merriam-webster.com/dictionary/abacus','https://en.wiktionary.org/wiki/abacus'])]
ROOT=dict(meaning='板；台板',core='从一块可承托、绘写或计算的板，认识算盘名称的来历。',image='平板用于计算，后来框中的珠子把数字变成可移动的位置；建筑中也保留顶板这个意思。',intro='abac- 不是现代英语里可以到处拼接的常用零件，但 abacus 本身值得掌握。希腊 ábax 的其他词形带 abak-，经拉丁变成 abacus。',forms='ábax／abak- 是希腊词形关系，不是两个无关词。英语常见复数 abacuses，也保留拉丁式 abaci。',branches=[['计算工具','abacus：算盘；历史计算板'],['建筑旁支','abacus：柱头上的顶板']],contrasts='今天的珠算盘不是这个旧名称唯一指过的东西；不要把词源里的计算板狭化成某一种现代算盘的发明史。',practice='读到 abacus 时，先判断文章在谈算术还是柱式建筑。',sources=['https://www.etymonline.com/word/abacus','https://www.merriam-webster.com/dictionary/abacus'])
m=json.loads((BASE/'.cache/batch200/rewrite_spec.json').read_text());r=next(x for x in m['roots']if x['id']==ID);c=next(x for x in json.loads((BASE/'.cache/catalog.json').read_text())if x['id']==ID);keep={w['word']for w in W}|set(SHARED);excluded={w:EXCLUDE_REASON for w in(set(r['family'])|set(c['family'])|set(c.get('unmatched',[])))-keep}
ROOT['id']=ID;ROOT['words']=list(dict.fromkeys([w for w in r['family']if w in keep]+[w for w in SHARED if w not in r['family']]));ROOT['exclude']=excluded
assert all(w['word']in m['owned_words']for w in W)
assert not(set(c['family'])|set(c.get('unmatched',[])))-set(ROOT['words'])-set(excluded)
assert {w['word']for w in W}<=set(ROOT['words'])
for w in W:assert len(w['examples'])>=2 and all(len(n)==2 and all(isinstance(x,str)and x for x in n)for n in w['history'])
for k,d in [('roots',[ROOT]),('words',W)]: (OUT/f'{k}_batch200_spec_{TAG}.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
print(ID,len(W),'new,',len(SHARED),'shared')
