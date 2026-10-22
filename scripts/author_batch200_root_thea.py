# coding: utf-8
import json
from pathlib import Path
from author_batch200_root_thea_a import W as A
from author_batch200_root_thea_b import W as B
W=A+B;kept=[x['word'] for x in W]
r=next(x for x in json.loads(Path('.cache/catalog.json').read_text()) if x['id']=='C1510')
EX={w:'较少用的形容词变体或戏剧理论术语，本轮暂略' for w in set(r['family'])|set(r['words']) if w not in kept and '-' not in w}
ROOT=dict(id='C1510',meaning='看、观看；供观看的地方',core='THEA = WATCH → A PLACE FOR WATCHING',image='一群人坐下，目光朝着舞台。观看的地方是 theatre；动作像专门演给观众看，就有 theatrical 的感觉。',intro='希腊 thea 表观看、景象，theaomai 表看，theatron 是供人观看的地方。经拉丁 theatrum、古法语 theatre 进入英语，词义从剧场扩展到戏剧艺术，也能把其他行动展开的区域比作舞台。',forms='theatre 与 theater 是常见英美拼写；amphi- 表两边、周围。theatrical、theatrically、theatricality、theatrics 的重音和词性不同，不能只认 theatre 的字母就忽略后缀。',branches=[['观看的场所与行业','theatre, theater'],['环绕观看的场所','amphitheatre, amphitheater'],['舞台感与夸张表现','theatrical, theatrically, theatricality, theatrics'],['坐在台下的人','theatergoer']],contrasts='theatrical production 是中性的舞台制作；theatrical behaviour 可能说行为夸张。theatrics 常带“做戏”的批评。operating theatre 是手术室，theater of war 是战区。thea- 观看与 theo- 神不能混。',practice='The theatergoers enjoyed the theatrical costumes, but the critic felt that the speech contained too much theatrics.\n\n观众喜欢那些富有舞台感的服装，但评论者觉得讲话中夸张作态太多。',words=kept,exclude=EX)
if __name__=='__main__':
 for name,data in [('roots_thea',[ROOT]),('words_thea',W)]:Path('.cache/batch200/drafts/root/'+name+'.json').write_text(json.dumps(data,ensure_ascii=False,indent=2))
 print(len(W),sum(len(x['examples']) for x in W))
