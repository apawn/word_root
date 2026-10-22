# coding: utf-8
from pathlib import Path
import json
from lesson_authoring import entry as E
BASE=Path(__file__).resolve().parents[1];OUT=BASE/'.cache/batch200/drafts/rewrite_spec'
ID='C1560';TAG='326_truc';SHARED=[];EXCLUDE_REASON='暂略较少用的同义名词变体 truculency。'
T=[['拉丁 trux，词干 truc-','凶猛、粗暴'],['拉丁 truculentus','凶狠、好斗的'],['英语 truculent〔亦有中古法语中介分析〕','挑衅、蛮横、不愿配合的']]
W=[E('truculent','英 /ˈtrʌkjʊlənt/；美 /ˈtrʌkjələnt/','好斗的；蛮横的','摆出随时想吵架、不肯好好合作的架势。','来自拉丁 truculentus，接 trux〔凶猛〕的词干 truc-；有经中古法语借入的分析。不能按 truck“卡车”来拆。',T,'一个人不只是反对你的意见，而是语气带刺、处处顶撞，仿佛等着起冲突，就可以叫 truculent。它经常写态度，不要求真的发生身体打斗。','a truculent reply；a truculent attitude；a truculent opponent。','assertive 是明确维护立场，未必冒犯；truculent 突出敌意和挑衅。',('The passenger became truculent when asked to move his bag.','被要求挪开包时，这名乘客变得蛮横起来。'),('His truculent reply ended any hope of a calm discussion.','他那充满挑衅的回答，让平静讨论再无可能。'),sources=['https://www.etymonline.com/word/truculent','https://en.wiktionary.org/wiki/truculent']),
E('truculence','/ˈtrʌkjələns/','蛮横；好斗态度','那种动不动就顶撞、带敌意的劲头。','历史接拉丁 truculentia〔凶狠〕，也有法语 truculence 中介分析；现代可与 truculent 的 -ent／-ence 形式对应。',T[:2]+[['拉丁 truculentia；法语 truculence','凶狠、好斗的名词材料'],['英语 truculence','蛮横与挑衅的态度']],'truculent 说“这个人态度蛮横”，truculence 则把那股蛮横本身拿出来评价。它比简单的 disagreement 多了明显的敌对气氛。','a show of truculence；respond with truculence；truculence in his manner。','firmness 可以平静而坚决；truculence 通常含不好沟通、准备冲突的意味。',('The interviewer was surprised by the guest’s truculence.','采访者对嘉宾的蛮横态度感到意外。'),('Her calm response took the force out of his truculence.','她平静的回应让他的挑衅失了威力。'),sources=['https://www.etymonline.com/word/truculence','https://en.wiktionary.org/wiki/truculence']),
E('truculently','/ˈtrʌkjələntli/','蛮横地；挑衅地','说话或行动时带着“你能把我怎样”的架势。','truculent＋-ly，英语形容词转副词；前半部继承凶狠、好斗的历史材料。',T+[['truculent ＋ -ly → truculently','以蛮横、挑衅的方式']],'truculently 常跟 said、replied、demanded 等一起用，让读者听出一句话不是普通陈述，而是在顶撞。它描述说话方式，不是给内容判断真假。','reply truculently；say truculently；demand truculently。','loudly 只说音量；truculently 说敌意，声音不大也可以很蛮横。',('“I’m not moving,” he said truculently.','“我就不挪。”他蛮横地说。'),('She truculently demanded to know who had complained.','她咄咄逼人地追问是谁投诉的。'),sources=['https://www.merriam-webster.com/dictionary/truculent','https://dictionary.cambridge.org/pronunciation/english/truculently'])]
ROOT=dict(meaning='凶猛；蛮横',core='truc- 的感觉是粗暴而好斗，现代常用来写人的态度。',image='意见不同还没谈几句，对方就竖起刺，准备顶撞。',intro='拉丁 trux 的词干是 truc-，truculentus 表示凶猛、粗暴。现代 truculent 常指带挑衅的言行；不一定真的动手。',forms='truculent 是形容词；truculence 是对应名词支线；truculently 是英语副词派生。',branches=[['态度','truculent；truculence'],['做事和说话的方式','truculently']],contrasts='坚定不等于蛮横；truculent 通常是批评态度里的敌意。',practice='对比 a firm reply 与 a truculent reply：同样拒绝，为什么语气可能很不一样？',sources=['https://www.etymonline.com/word/truculent','https://www.etymonline.com/word/truculence'])
m=json.loads((BASE/'.cache/batch200/rewrite_spec.json').read_text());r=next(x for x in m['roots']if x['id']==ID);c=next(x for x in json.loads((BASE/'.cache/catalog.json').read_text())if x['id']==ID);keep={w['word']for w in W}|set(SHARED);excluded={w:EXCLUDE_REASON for w in(set(r['family'])|set(c['family'])|set(c.get('unmatched',[])))-keep}
ROOT['id']=ID;ROOT['words']=list(dict.fromkeys([w for w in r['family']if w in keep]+[w for w in SHARED if w not in r['family']]));ROOT['exclude']=excluded
assert all(w['word']in m['owned_words']for w in W)
assert not(set(c['family'])|set(c.get('unmatched',[])))-set(ROOT['words'])-set(excluded)
assert {w['word']for w in W}<=set(ROOT['words'])
for w in W:assert len(w['examples'])>=2 and all(len(n)==2 and all(isinstance(x,str)and x for x in n)for n in w['history'])
for k,d in [('roots',[ROOT]),('words',W)]: (OUT/f'{k}_batch200_spec_{TAG}.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
print(ID,len(W),'new,',len(SHARED),'shared')
