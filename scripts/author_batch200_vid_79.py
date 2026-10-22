# -*- coding: utf-8 -*-
"""C0971 Greek pater/patr: father, ancestors, homeland; reuse shared lessons."""
import json
from pathlib import Path
from lesson_authoring import entry as E
BASE=Path(__file__).resolve().parents[1];OUT=BASE/'.cache/batch200/drafts/rewrite_vid'
def S(w):return 'https://www.etymonline.com/word/'+w
def K(w):return 'https://en.wiktionary.org/wiki/'+w
def O(w):return 'https://www.oxfordlearnersdictionaries.com/definition/english/'+w
W=[
E('unpatriotic','英 /ˌʌnˌpætriˈɒtɪk/，也读 /ˌʌnˌpeɪtriˈɒtɪk/；美 /ˌʌnˌpeɪtriˈɑːtɪk/','不爱国的；被认为缺乏爱国心的','patriotic 是对自己的国家有认同、关切或支持；unpatriotic 则否定这种态度，常作为一种批评标签出现。','英语 un-“不”+ patriotic。patriotic 经法语 patriotique 或晚期拉丁 patrioticus，接希腊 patriotikos，远接 patēr“父亲”、patris“故国”。这里“父亲”已延伸到祖辈所属的国家，不是说不爱自己的父亲。',[['希腊 patēr → patris／patriōtēs → patriotikos','父亲、祖辈 → 故国、同胞 → 故国相关的'],['法语 patriotique／晚期拉丁 patrioticus → 英语 patriotic','与本国有关的 → 爱国的'],['英语 un- + patriotic → unpatriotic','不爱国的；常用于评价或指责']],'call something unpatriotic 是把某种行为称为不爱国。这个词往往表达说话人的判断，阅读时要分清是谁在评价，以及评价依据是什么。','unpatriotic behaviour；an unpatriotic attitude；label someone unpatriotic。','unpatriotic 不等于 foreign“外国的”，也不直接等于 illegal“违法的”。批评某项政策与对国家缺乏关切不是同一个概念。',('The critic described the film as unpatriotic.','这位评论者称这部电影不爱国。'),('She objected when her questions were labelled unpatriotic.','当她提出的问题被贴上“不爱国”的标签时，她表示反对。'),sources=[K('unpatriotic'),O('unpatriotic'),S('patriotic')]),
E('patronymic','英、美 /ˌpætrəˈnɪmɪk/','源自父名或父系祖先名的名字；父名式的','一个人的名字里留着父亲或父系祖先的名字，好像在名字上加一句“某某的孩子”。','patr- 接希腊 patēr／patros“父亲”，-onym- 接 onyma“名字”。英语名词经晚期拉丁 patronymicum，形容词对应 patronymicus；背后是希腊 patrōnymos 等词形，并非先有现代英语 patron 再加 -ymic。',[['希腊 patēr／patr- + onyma','父亲 + 名字'],['希腊 patrōnymos；晚期拉丁 patronymicus／patronymicum','由父亲名字形成的；相应名称'],['英语 patronymic 名词与形容词','父名式名称；按这种方法形成的']],'Peterson 这类姓有“Peter 的儿子”的历史来源，但今天固定传承的姓不表示每个人的父亲都叫 Peter。有些命名习惯则仍按实际父名生成 patronymic，并另有一个姓。','a patronymic name；a patronymic surname；use a patronymic；a patronymic naming system。','surname 是家族姓氏，patronymic 强调名称来自父亲或父系祖先。两者可能重合，也可能在全名里分别占不同位置。',('The guide explains the patronymic origin of names such as Peterson.','指南解释了 Peterson 等名字源自父名的历史。'),('The form has separate spaces for a surname and a patronymic.','表格把姓氏和父名式名字分成了两个填写栏。'),sources=[S('patronymic'),K('patronymic'),'https://www.merriam-webster.com/dictionary/patronymic']),
]
SHARED=['patriotic','patriot','patriotism','patriarch','patriarchal','patriarchy']
EX={w:'主要用于专门生物地理、教父学或古代社会分类，按用户常用阅读优先要求暂略。' for w in ['sympatric','allopatric','sympatry','allopatry','patrology','eupatrides']}
EX['patronym']='与 patronymic 的名词义接近，较少用；常见命名概念已在 patronymic 同条解释。'
ROOT=dict(id='C0971',meaning='父亲；父系、祖辈；故国',core='希腊 patēr 是父亲，屈折词干是 patr-。从父亲想到家族和祖辈，再想到祖辈生活的土地，便能理解家长、父名和爱国这一组词。',image='父亲、家族 → patriarch 家长、族长；男性家长掌权 → patriarchy；祖辈之地 → patriot 爱国者；由父亲的名字命名 → patronymic。',intro='不要把 patri- 一概翻译成父亲：patriot 指向国家，patriarch 指向家族或权威角色，patronymic 指向命名方式。三条支线都从家族、祖辈的观念发展出来。',forms='希腊 patēr 的属格是 patros，因此出现 patr-。patria 可指家系、氏族，patris 指故国；patriōtēs 原来重在同乡、同胞。拉丁 pater 与希腊 patēr 是历史同源的近亲，不表示每个 pater-/patr- 词都通过同一条语言路线进入英语。',branches=[['故国与爱国情感','patriot, patriotic, patriotism, unpatriotic'],['家长、宗教称号与父权结构','patriarch, patriarchal, patriarchy'],['父名式命名','patronymic']],contrasts='patriot 是爱国者，patriarch 是家族长者或宗教称号；patriarchy 是一种权力结构，patronymic 是命名方式。patriotic 与 unpatriotic 常带评价，需要结合说话人和语境。',practice='A patriot cares about the homeland; a patronymic records a father’s or ancestor’s name. patriot 关乎故国，patronymic 关乎父亲或祖先留下的名字。',words=[],exclude=EX)
if __name__=='__main__':
 m=json.loads((BASE/'.cache/batch200/rewrite_vid.json').read_text());r=next(x for x in m['roots'] if x['id']==ROOT['id']);ROOT['words']=list(dict.fromkeys([w for w in r['family'] if '-' not in w and w not in EX]+SHARED))
 assert set(ROOT['words'])==set(SHARED)|{e['word'] for e in W}
 assert {e['word'] for e in W}<=set(m['owned_words'])
 assert len(W)==len({e['word'] for e in W}) and all(len(e['examples'])>=2 and len(e['history'])>=2 for e in W)
 for kind,data in [('roots',[ROOT]),('words',W)]: (OUT/(kind+'_batch200_vid_79.json')).write_text(json.dumps(data,ensure_ascii=False,indent=2))
 print('pater Greek:',len(W),'words;',sum(len(e['examples']) for e in W),'examples;',len(ROOT['words']),'references')
