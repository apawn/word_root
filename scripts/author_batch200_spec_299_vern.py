# coding: utf-8
from pathlib import Path
import json
from lesson_authoring import entry as E
BASE=Path(__file__).resolve().parents[1];OUT=BASE/'.cache/batch200/drafts/rewrite_spec'
ID='C1623';TAG='299_vern';SHARED=[];EXCLUDE_REASON='按当前范围暂略低频春季相关派生。'
W=[E('vernal','英 /ˈvɜːnəl/；美 /ˈvɜːrnəl/','春天的；春季的；带有春天气息的','把季节刚转暖、万物重新生长的画面压成一个形容词。','借拉丁 vernalis，接 vernus“春天的”，再接 ver“春天”。不是从 vernacular“本地话、本地的”截取而来。',[['拉丁 ver〔春天〕→ vernus → vernalis','春天 → 属于春天的'],['英语 vernal','正式或文学性的春季形容词']],'最常见的固定搭配是 the vernal equinox“春分”。文学里 vernal flowers、vernal freshness 也能描写春日的花和清新感。这个词比 spring 作定语更正式，不必把日常的 spring weather 都改得很书面。','the vernal equinox；vernal flowers；vernal freshness。','vernal 对应春季，autumnal 对应秋季。春分属于当地半球的春天，不能把“春分总在三月”套到全球。',('The calendar marks the vernal equinox as the start of astronomical spring.','日历把春分标为天文学意义上春季的开始。'),('The poem celebrates the vernal freshness of the countryside.','这首诗赞美乡野的春日清新气息。'),sources=['https://www.oxfordlearnersdictionaries.com/definition/english/vernal','https://www.etymonline.com/word/vernal'])]
ROOT=dict(meaning='春天',core='vern- 在这一支里就是春季，尤其常见于 vernal equinox“春分”。',image='冬天过去，新的生长季开始。',intro='拉丁 ver“春天”先形成 vernus、vernalis，再进入英语成为 vernal。它是季节词的一支，最适合和 autumnal“秋季的”对着记。',forms='ver → vernus → vernalis → vernal；不要把拉丁形容词阶段省略后，误当成现代英语直接加几段字母。',branches=[['春季及春天气息','vernal']],contrasts='vernacular 接拉丁 verna 一支，含本地、本土的含义，与 ver“春天”不同源。',practice='把 vernal equinox 与 autumnal equinox 对照，并用一句话解释两者分别进入什么季节。',sources=['https://www.oxfordlearnersdictionaries.com/definition/english/vernal','https://www.etymonline.com/word/vernal'])
m=json.loads((BASE/'.cache/batch200/rewrite_spec.json').read_text());r=next(x for x in m['roots']if x['id']==ID);c=next(x for x in json.loads((BASE/'.cache/catalog.json').read_text())if x['id']==ID);keep={w['word']for w in W}|set(SHARED);excluded={w:EXCLUDE_REASON for w in(set(r['family'])|set(c['family'])|set(c.get('unmatched',[])))-keep}
ROOT['id']=ID;ROOT['words']=list(dict.fromkeys([w for w in r['family']if w in keep]+[w for w in SHARED if w not in r['family']]));ROOT['exclude']=excluded
assert all(w['word']in m['owned_words']for w in W)
assert not(set(c['family'])|set(c.get('unmatched',[])))-set(ROOT['words'])-set(excluded)
assert {w['word']for w in W}<=set(ROOT['words'])
for w in W:assert len(w['examples'])>=2 and all(len(n)==2 and all(isinstance(x,str)and x for x in n)for n in w['history'])
for k,d in [('roots',[ROOT]),('words',W)]: (OUT/f'{k}_batch200_spec_{TAG}.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
print(ID,len(W),'new,',len(SHARED),'shared')
