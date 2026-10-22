# coding: utf-8
from pathlib import Path
import json
from lesson_authoring import entry as E
BASE=Path(__file__).resolve().parents[1];OUT=BASE/'.cache/batch200/drafts/rewrite_spec'
ID='C0152';TAG='284_cac';SHARED=['cacophony','cacophonous'];EXCLUDE_REASON='按当前范围暂略冷门病名、恐惧症名、旧修辞词、少用人物名和异拼，保留通用阅读较有用的三词。'
W=[E('kakistocracy','英 /ˌkækɪˈstɒkrəsi/；美 /ˌkækɪˈstɑːkrəsi/','劣人统治；最不适任者当政','讽刺权力落到了最差、最不该掌权的人手里。','使用希腊 kákistos“最坏的” + 英语 -cracy 统治；kákistos 是 kakós“坏”的最高级。整词是英语利用古典材料造的词，不必假设古希腊已有这个政体名称。',[['希腊 kakós → kákistos；另有 -kratia〔统治〕','坏 → 最坏；统治材料并列'],['英语 kakist- + -o- + -cracy → kakistocracy','用古典材料造出对最差统治者的批评称呼']],'它常见于尖锐的政治评论，既可骂无能，也可骂腐败或品行恶劣。这里不是一套中性的宪政分类，而是作者在评价“谁掌权、这些人有多不配”。','call a government a kakistocracy；a descent into kakistocracy。','aristocracy 字面原指最优秀者统治，现代通常指贵族阶层或其统治；kakistocracy 用“最差”形成讽刺性的反面。',('The columnist called the administration a kakistocracy.','那位专栏作者把这届政府批评为劣人当政。'),('The satire imagines a kakistocracy in which incompetence is rewarded.','这部讽刺作品想象了一种无能反获奖赏的劣人统治。'),sources=['https://www.merriam-webster.com/dictionary/kakistocracy','https://en.wiktionary.org/wiki/kakistocracy','https://www.etymonline.com/word/kakistocracy'])]
ROOT=dict(meaning='坏；不好；令人不快',core='先说“不好”，再看它评价的是声音还是掌权的人。',image='许多声音互相冲撞叫坏声音；把最不适任的人送上权位，则形成最差者统治的讽刺。',intro='希腊 kakós 意思是坏、不好。经拉丁字母传统可写成 caco-；最高级 kákistos 则给 kakistocracy 提供“最坏”的一层。',forms='caco-／kako- 是常见组合形式；kakist- 来自最高级，不是把 caco- 随意拉长。cacophonous 接古希腊形容词，不只是现代 cacophony 加 -ous。',branches=[['声音不协调','cacophony；cacophonous'],['对统治者的批评','kakistocracy']],contrasts='loud 只说响，cacophonous 说不悦耳、不协调；kakistocracy 带明显批判语气，不能当作完全中性的分类标签。',practice='见到 caco- 先判断“不好”落在什么对象上，而不是一律译成道德邪恶。',sources=['https://en.wiktionary.org/wiki/cacophony','https://www.merriam-webster.com/dictionary/kakistocracy'])
m=json.loads((BASE/'.cache/batch200/rewrite_spec.json').read_text());r=next(x for x in m['roots']if x['id']==ID);c=next(x for x in json.loads((BASE/'.cache/catalog.json').read_text())if x['id']==ID);keep={w['word']for w in W}|set(SHARED);excluded={w:EXCLUDE_REASON for w in(set(r['family'])|set(c['family'])|set(c.get('unmatched',[])))-keep}
ROOT['id']=ID;ROOT['words']=list(dict.fromkeys([w for w in r['family']if w in keep]+[w for w in SHARED if w not in r['family']]));ROOT['exclude']=excluded
assert all(w['word']in m['owned_words']for w in W)
assert not(set(c['family'])|set(c.get('unmatched',[])))-set(ROOT['words'])-set(excluded)
assert {w['word']for w in W}<=set(ROOT['words'])
for w in W:assert len(w['examples'])>=2 and all(len(n)==2 and all(isinstance(x,str)and x for x in n)for n in w['history'])
for k,d in [('roots',[ROOT]),('words',W)]: (OUT/f'{k}_batch200_spec_{TAG}.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
print(ID,len(W),'new,',len(SHARED),'shared')
