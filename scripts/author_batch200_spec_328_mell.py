# coding: utf-8
from pathlib import Path
import json
from lesson_authoring import entry as E
BASE=Path(__file__).resolve().parents[1];OUT=BASE/'.cache/batch200/drafts/rewrite_spec'
ID='C0719';TAG='328_mell';SHARED=[];EXCLUDE_REASON='暂略蜂蜜生产、食性及古雅修辞的冷门派生和同义变体。'
M=[['拉丁 mel／mell-；fluere','蜂蜜；流动：并列材料'],['后期拉丁 mellifluus','像蜜一样流淌'],['中古英语及现代英语 mellifluous','甜润流畅；常形容悦耳声音']]
W=[E('mellifluous','/məˈlɪfluəs/','甜美流畅的；悦耳动听的','声音像蜂蜜一样顺滑地流进耳朵。','来自后期拉丁 mellifluus；mell-〔蜂蜜〕＋ -fluus〔流动〕，英语采用 -ous 形容词形式。不能拆成英语 mellow 加 fluent。',M,'mellifluous voice 不一定音量大，也不一定音调高，重点是听起来甜润、平顺、有流动感。它是较书面的赞美，常见于音乐、朗读和声音描写。','a mellifluous voice；mellifluous tones；mellifluous prose。','fluent 强调表达流利；mellifluous 更在乎声音或文字读起来的悦耳质感。',('Her mellifluous voice made the poem a pleasure to hear.','她甜润流畅的嗓音让这首诗听起来格外悦耳。'),('The host introduced the programme in mellifluous tones.','主持人用柔美流畅的声调介绍节目。'),sources=['https://www.etymonline.com/word/mellifluous','https://en.wiktionary.org/wiki/mellifluous']),
E('mellifluously','/məˈlɪfluəsli/','甜美流畅地；悦耳地','让话语或歌声顺顺地流出来。','mellifluous＋-ly，英语形容词转副词；继续保留“蜜一样流动”的声音比喻。',M+[['mellifluous ＋ -ly → mellifluously','以甜润流畅的方式']],'形容词说 the voice is mellifluous，副词则说 someone speaks mellifluously：从评价声音，转到描述说话或演唱的方式。并不表示内容一定可信，只是听起来很顺耳。','speak mellifluously；sing mellifluously；mellifluously delivered lines。','persuasively 强调有说服力；mellifluously 强调悦耳，两种效果可以分开。',('The actor read the opening lines mellifluously.','演员把开场的几行台词读得甜润流畅。'),('She sang mellifluously, letting each phrase flow into the next.','她唱得柔美悦耳，让每个乐句自然接向下一句。'),sources=['https://www.collinsdictionary.com/dictionary/english/mellifluously','https://www.etymonline.com/word/mellifluous'])]
ROOT=dict(meaning='蜂蜜',core='mell- 在本组里把蜂蜜的甜与顺滑借给声音。',image='不是一块硬糖，而是一股慢慢流动的蜂蜜。',intro='拉丁 mel 的词干是 mell-。mellifluous 把它与流动的材料相接，形成“像蜜流淌”的画面；现代主要用来欣赏嗓音、声调和文字的悦耳感。',forms='melli- 是带连接元音的构词形式；mellifluously 由形容词加 -ly。',branches=[['声音的质感','mellifluous'],['发声的方式','mellifluously']],contrasts='悦耳不等于真实或有说服力；这个词主要评价表达的声音质感。',practice='挑一个你喜欢的朗读者，说明他的声音是否适合用 mellifluous。',sources=['https://www.etymonline.com/word/mellifluous'])
m=json.loads((BASE/'.cache/batch200/rewrite_spec.json').read_text());r=next(x for x in m['roots']if x['id']==ID);c=next(x for x in json.loads((BASE/'.cache/catalog.json').read_text())if x['id']==ID);keep={w['word']for w in W}|set(SHARED);excluded={w:EXCLUDE_REASON for w in(set(r['family'])|set(c['family'])|set(c.get('unmatched',[])))-keep}
ROOT['id']=ID;ROOT['words']=list(dict.fromkeys([w for w in r['family']if w in keep]+[w for w in SHARED if w not in r['family']]));ROOT['exclude']=excluded
assert all(w['word']in m['owned_words']for w in W)
assert not(set(c['family'])|set(c.get('unmatched',[])))-set(ROOT['words'])-set(excluded)
assert {w['word']for w in W}<=set(ROOT['words'])
for w in W:assert len(w['examples'])>=2 and all(len(n)==2 and all(isinstance(x,str)and x for x in n)for n in w['history'])
for k,d in [('roots',[ROOT]),('words',W)]: (OUT/f'{k}_batch200_spec_{TAG}.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
print(ID,len(W),'new,',len(SHARED),'shared')
