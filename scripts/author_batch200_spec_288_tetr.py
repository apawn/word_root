# coding: utf-8
from pathlib import Path
import json
from lesson_authoring import entry as E
BASE=Path(__file__).resolve().parents[1];OUT=BASE/'.cache/batch200/drafts/rewrite_spec'
ID='C1501';TAG='288_tetr';SHARED=['tetrahedron','tetralogy','tetrapod'];EXCLUDE_REASON='按当前范围暂略低频几何别称、旧电子器件、特殊恐惧名称与古乐理术语，保留基础几何、生物、文艺用词。'
W=[E('tetrameter','英 /tetˈræmɪtə/；美 /tetˈræmətər/','四音步诗行；四音步格律','一行诗里的节奏单位走四步，不是只有四个字或四个音节。','借后期拉丁 tetrametrus，接希腊 tetrámetros／tetrámetron，由 tetra- 四 + métron 度量、韵律单位构成。现代可看 tetra- + meter，但不是简单从现代“米”造词。',[['希腊 tetra-〔四〕与 métron〔度量、韵律单位〕','计数与节奏单位两份材料并列'],['希腊 tetrámetros／tetrámetron → 后期拉丁 tetrametrus','有四个韵律单位的诗行'],['英语 tetrameter','现代英语格律通常指四音步诗行']],'以英语抑扬格为例，一个音步是“轻—重”，四音步就是把这个小节奏重复四次。所以完整的抑扬格四音步通常有八个音节，而不是四个。古典希腊、拉丁格律里的度量单位不总与现代英语音步一一对应。','iambic tetrameter；trochaic tetrameter；a line of tetrameter。','tetrameter 数音步，tetralogy 数作品；pentameter 是五音步，不是五行诗。',('The poet uses iambic tetrameter in the opening stanza.','诗人在开头一节用了抑扬格四音步。'),('We marked the four feet in each line of tetrameter.','我们标出了每行四音步诗中的四个音步。'),sources=['https://www.etymonline.com/word/tetrameter','https://dictionary.cambridge.org/us/dictionary/english/tetrameter','https://www.poetryfoundation.org/education/glossary/tetrameter','https://owl.purdue.edu/owl/subject_specific_writing/creative_writing/writers/poetry_basics/poetic_feet_and_line_length.html'])]
ROOT=dict(meaning='四',core='四这个数很稳定；先看后半，才知道数的是面、作品、肢体还是节奏单位。',image='四个面拼成体，四部作品连成系列，四个音步排成诗行。',intro='tetra- 是希腊来源的“四”。它特别适合拆词：不用背抽象口诀，只要把后面的东西数成四份。但生物分类有演化含义，不能永远只按现存外形数数。',forms='tetr- 在辅音前常以 tetra- 出现。tetrahedron 和 tetrameter 有古典词形借入史；现代看得出组合，不代表都是最近在英语中拼出来。',branches=[['面与肢体','tetrahedron：四面体；tetrapod：四足动物'],['作品与节奏','tetralogy：四部曲；tetrameter：四音步']],contrasts='tetrahedron 数面，不是底边；tetrapod 是演化类群，蛇仍属于其中；tetrameter 数音步，不是单个音节。',practice='遇到 tetra- 先答“四”，再明确后半告诉你四个什么。',sources=['https://www.etymonline.com/word/tetrahedron','https://www.etymonline.com/word/tetrameter','https://ucmp.berkeley.edu/vertebrates/tetrapods/tetraintro.html'])
m=json.loads((BASE/'.cache/batch200/rewrite_spec.json').read_text());r=next(x for x in m['roots']if x['id']==ID);c=next(x for x in json.loads((BASE/'.cache/catalog.json').read_text())if x['id']==ID);keep={w['word']for w in W}|set(SHARED);excluded={w:EXCLUDE_REASON for w in(set(r['family'])|set(c['family'])|set(c.get('unmatched',[])))-keep}
ROOT['id']=ID;ROOT['words']=list(dict.fromkeys([w for w in r['family']if w in keep]+[w for w in SHARED if w not in r['family']]));ROOT['exclude']=excluded
assert all(w['word']in m['owned_words']for w in W)
assert not(set(c['family'])|set(c.get('unmatched',[])))-set(ROOT['words'])-set(excluded)
assert {w['word']for w in W}<=set(ROOT['words'])
for w in W:assert len(w['examples'])>=2 and all(len(n)==2 and all(isinstance(x,str)and x for x in n)for n in w['history'])
for k,d in [('roots',[ROOT]),('words',W)]: (OUT/f'{k}_batch200_spec_{TAG}.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
print(ID,len(W),'new,',len(SHARED),'shared')
