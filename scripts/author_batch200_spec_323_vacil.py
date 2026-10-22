# coding: utf-8
from pathlib import Path
import json
from lesson_authoring import entry as E
BASE=Path(__file__).resolve().parents[1];OUT=BASE/'.cache/batch200/drafts/rewrite_spec'
ID='C1599';TAG='323_vacil';SHARED=[];EXCLUDE_REASON='暂略罕见派生。'
V=[['拉丁 vacillāre','身体摇晃；意见摇摆'],['拉丁 vacillātus → 英语 vacillate','由摇晃转到拿不定主意']]
W=[E('vacillate','/ˈvæsɪleɪt/，也读 /ˈvæsəleɪt/','摇摆不定；犹豫不决','一会儿往这个选择靠，一会儿又往另一个选择靠。','借拉丁 vacillāre 的分词词干 vacillāt-；现代可认出 vacill-＋-ate，但没有必要把它再拆成 vac- 和其他英语零件。',V,'把决定想成一根左右晃动的指针：刚指向 A，又回到 B。vacillate 不只是停着没决定，还强调想法或态度来回变动。','vacillate between A and B；vacillate over a decision；stop vacillating。','hesitate 可以是短暂迟疑；vacillate 常有反复摇摆的过程。',('She vacillated between accepting the offer and staying where she was.','她一会儿想接受邀请，一会儿又想留在原地。'),('The committee continued to vacillate over the launch date.','委员会对发布日期继续摇摆不定。'),sources=['https://www.etymonline.com/word/vacillate','https://en.wiktionary.org/wiki/vacillate']),
E('vacillation','/ˌvæsɪˈleɪʃən/','犹豫不决；反复摇摆','决定或立场迟迟稳定不下来的过程。','英语名词早于现代动词 vacillate 的使用记录；中古英语 vacillacion 借拉丁 vacillātiō。现在可与 vacillate 对照记，不能把这种记法当成真实的先后次序。',[['拉丁 vacillāre → vacillātiō','摇晃、摇摆 → 相应状态名词'],['中古英语 vacillacion → 英语 vacillation','意见、行为的摇摆不定']],'vacillation 把一次次改变主意放在一起看。工作语境里它常带批评：问题不是没有想法，而是今天一个方向、明天另一个方向，让别人也无法行动。','after much vacillation；weeks of vacillation；vacillation between two options。','deliberation 是认真权衡，未必贬义；vacillation 更容易暗示缺少稳定判断。',('After weeks of vacillation, they finally signed the contract.','犹豫了几个星期后，他们终于签了合同。'),('His vacillation left the team unsure what to do next.','他反复摇摆，让团队不知道下一步该做什么。'),sources=['https://www.etymonline.com/word/vacillation','https://en.wiktionary.org/wiki/vacillation']),
E('vacillating','/ˈvæsɪleɪtɪŋ/','摇摆不定的','态度总在变，别人很难知道最终立场。','vacillate＋-ing；由现在分词作形容词，也可以是动词进行形式。',V+[['vacillate ＋ -ing → vacillating','正在摇摆；态度不稳定的']],'a vacillating leader 不是单纯思考得慢，而是决定一会儿朝东、一会儿朝西。它也可描述政策、态度或支持程度，突出不稳定。','a vacillating attitude；a vacillating leader；keep vacillating between…。','flexible 是会调整、能适应；vacillating 往往批评缺少定见，并非同一种赞许。',('The board lost patience with his vacillating leadership.','董事会对他摇摆不定的领导方式失去了耐心。'),('She is still vacillating between the two apartments.','她还在两套公寓之间拿不定主意。'),sources=['https://www.etymonline.com/word/vacillate','https://en.wiktionary.org/wiki/vacillating'])]
ROOT=dict(meaning='摇晃；摇摆',core='vacill- 的图像是身体左右晃，后来变成主意左右摇。',image='一个指针不停从 A 摆向 B，又从 B 摆回 A。',intro='拉丁 vacillāre 兼有身体不稳和意见不定的意思。英语里最实用的是决策场景：反复改变选择，迟迟不能站定。',forms='vacillate 是动词，vacillating 是现在分词或形容词。vacillation 是独立借入的拉丁名词支线，英语中并非由较晚的动词才造出。',branches=[['动作与态度','vacillate；vacillating'],['摇摆这一过程','vacillation']],contrasts='摇摆不定不等于认真权衡，也不等于灵活适应；vacillate 常带负面评价。',practice='用 vacillate between 说出两个让你反复改变主意的选项。',sources=['https://www.etymonline.com/word/vacillation','https://www.etymonline.com/word/vacillate'])
m=json.loads((BASE/'.cache/batch200/rewrite_spec.json').read_text());r=next(x for x in m['roots']if x['id']==ID);c=next(x for x in json.loads((BASE/'.cache/catalog.json').read_text())if x['id']==ID);keep={w['word']for w in W}|set(SHARED);excluded={w:EXCLUDE_REASON for w in(set(r['family'])|set(c['family'])|set(c.get('unmatched',[])))-keep}
ROOT['id']=ID;ROOT['words']=list(dict.fromkeys([w for w in r['family']if w in keep]+[w for w in SHARED if w not in r['family']]));ROOT['exclude']=excluded
assert all(w['word']in m['owned_words']for w in W)
assert not(set(c['family'])|set(c.get('unmatched',[])))-set(ROOT['words'])-set(excluded)
assert {w['word']for w in W}<=set(ROOT['words'])
for w in W:assert len(w['examples'])>=2 and all(len(n)==2 and all(isinstance(x,str)and x for x in n)for n in w['history'])
for k,d in [('roots',[ROOT]),('words',W)]: (OUT/f'{k}_batch200_spec_{TAG}.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
print(ID,len(W),'new,',len(SHARED),'shared')
