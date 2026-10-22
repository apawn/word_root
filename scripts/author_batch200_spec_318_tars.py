# coding: utf-8
from pathlib import Path
import json
from lesson_authoring import entry as E
BASE=Path(__file__).resolve().parents[1];OUT=BASE/'.cache/batch200/drafts/rewrite_spec'
ID='C1473';TAG='318_tars';SHARED=[];EXCLUDE_REASON='暂略专门的足部手术、鸟类骨骼和重复整体术语，保留基本人体部位词。'
A='https://openstax.org/books/anatomy-and-physiology-2e/pages/8-4-bones-of-the-lower-limb'
T=[['希腊 tarsós','平展的框架、平面；也用于脚底等部位'],['新拉丁 tarsus','解剖学的跗部名称'],['英语 tarsus','人体足部的一组跗骨及相应区域']]
W=[E('tarsus','英 /ˈtɑːsəs/；美 /ˈtɑːrsəs/','跗；跗部','人体脚后半部那组相互连接的骨头及其区域。','借新拉丁 tarsus，接希腊 tarsós；古词可指平展框架、平面，也指脚底。这里保留可见的形状联系，不把更早词源的争议当定论。',T,'把脚骨想成前后几段：靠后的一组块状骨是 tarsus，向前接长一些的跖骨，再向前是脚趾骨。成人一足的跗骨通常有七块，所以这个词不是某一块脚踝骨的专名。','the bones of the tarsus；the human tarsus；复数 tarsi。','ankle 通常指踝部或踝关节；tarsus 是更具体的骨群名称。生物学中它也可指昆虫腿末端的跗节，需看对象。',('The diagram labels the seven bones of the human tarsus.','图示标出了人足的七块跗骨。'),('The metatarsal bones lie in front of the tarsus.','跖骨位于跗部前方。'),sources=['https://www.etymonline.com/word/tarsus','https://en.wiktionary.org/wiki/tarsus',A]),
E('tarsal','英 /ˈtɑːsəl/；美 /ˈtɑːrsəl/','跗的；跗骨','给跗部作形容词，也能指其中一块骨头。','可由 tarsus 的词干 tars-＋ -al〔与……有关〕形成，也有借医学拉丁 tarsalis 的分析；现代可直接与 tarsus 成对记。',T[:-1]+[['英语 tarsus ＋ -al，或医学拉丁 tarsalis 借入','两种词源分析并列'],['英语 tarsal','跗部的；转作跗骨名称']],'tarsal bones 是跗骨，单说 a tarsal 也可指其中一块。它并非整个 foot 的形容词，而是把范围收在跗部；其他生物或眼部语境中的专门用法要另看上下文。','tarsal bones；a tarsal joint；the tarsals。','tarsus 是整体区域或骨群，tarsal 是相关形容词，也可作单块骨的名词。',('The heel bone is the largest tarsal bone.','跟骨是最大的一块跗骨。'),('The model separates the tarsals from the long metatarsal bones.','模型把跗骨与较长的跖骨分开显示。'),sources=['https://www.etymonline.com/word/tarsal','https://en.wiktionary.org/wiki/tarsal',A]),
E('metatarsal','英 /ˌmetəˈtɑːsəl/；美 /ˌmetəˈtɑːrsəl/','跖骨的；跖骨','脚中连着跗骨与脚趾骨的五根长骨之一。','可按 meta-〔在后、接着〕＋ tarsal 理解；历史上也接已有的 metatarsus〔跖部〕加 -al，metatarsus 源自中世纪拉丁 meta-＋tarsus。',[['希腊 meta；tarsós','接着、在后；跗部相关材料：并列'],['中世纪拉丁 metatarsus → 英语 metatarsus','跗部之后的足部区域名称'],['metatarsus 对应的 metatarsal','跖部的；跖骨']],'顺着脚从后向前看：过了跗骨，就到五根较长的跖骨，随后才是脚趾。体育报道说 broken metatarsal，通常就是某根跖骨骨折，不是把脚趾和脚踝统称为一块骨。','a metatarsal fracture；the fifth metatarsal；metatarsal bones。','metacarpal 在手掌，metatarsal 在脚；carp- 与 tars- 的部位不同。',('The footballer fractured a metatarsal in his left foot.','这名足球运动员左脚的一根跖骨骨折了。'),('Each human foot normally has five metatarsal bones.','每只人足通常有五根跖骨。'),sources=['https://www.etymonline.com/word/metatarsal','https://www.merriam-webster.com/dictionary/metatarsal','https://en.wiktionary.org/wiki/metatarsal',A])]
ROOT=dict(meaning='平展框架；跗部',core='tars- 在常见解剖词中指向脚后半部的跗部。',image='把脚骨从后向前排成跗骨、跖骨、趾骨三段。',intro='希腊 tarsós 曾用于多种平展物，也指脚底；后来的解剖学借它形成 tarsus。学习时抓住脚的结构，比把每个词都硬译成“平板”有用。',forms='tarsus 是整体名词；tarsal 是形容词或单块骨；metatarsal 接到前方的跖骨。',branches=[['整体区域','tarsus'],['跗部与单块骨','tarsal'],['向前相接的长骨','metatarsal']],contrasts='七块跗骨与五根跖骨是不同骨群；tarsus 不等于任意一块踝骨。',practice='从脚跟向脚趾的方向，排出 tarsal bones、metatarsal bones、toe bones。',sources=['https://www.etymonline.com/word/tarsus',A])
m=json.loads((BASE/'.cache/batch200/rewrite_spec.json').read_text());r=next(x for x in m['roots']if x['id']==ID);c=next(x for x in json.loads((BASE/'.cache/catalog.json').read_text())if x['id']==ID);keep={w['word']for w in W}|set(SHARED);excluded={w:EXCLUDE_REASON for w in(set(r['family'])|set(c['family'])|set(c.get('unmatched',[])))-keep}
ROOT['id']=ID;ROOT['words']=list(dict.fromkeys([w for w in r['family']if w in keep]+[w for w in SHARED if w not in r['family']]));ROOT['exclude']=excluded
assert all(w['word']in m['owned_words']for w in W)
assert not(set(c['family'])|set(c.get('unmatched',[])))-set(ROOT['words'])-set(excluded)
assert {w['word']for w in W}<=set(ROOT['words'])
for w in W:assert len(w['examples'])>=2 and all(len(n)==2 and all(isinstance(x,str)and x for x in n)for n in w['history'])
for k,d in [('roots',[ROOT]),('words',W)]: (OUT/f'{k}_batch200_spec_{TAG}.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
print(ID,len(W),'new,',len(SHARED),'shared')
