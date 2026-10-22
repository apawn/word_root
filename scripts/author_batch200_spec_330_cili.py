# coding: utf-8
from pathlib import Path
import json
from lesson_authoring import entry as E
BASE=Path(__file__).resolve().parents[1];OUT=BASE/'.cache/batch200/drafts/rewrite_spec'
ID='C0218';TAG='330_cili';SHARED=['supercilious'];EXCLUDE_REASON='暂略细分形态词和冷门派生。'
C=[['拉丁 cilium，复数 cilia','眼睑、睫毛相关名称'],['新拉丁及英语生物学 cilium／cilia','借毛发般的外形命名细胞突起']]
S=[['拉丁 supercilium','眉毛；已有傲慢神态的比喻'],['拉丁 superciliōsus','傲慢、目中无人的'],['英语 supercilious','自视高人一等、轻蔑的']]
N='https://nigms.nih.gov/biobeat/2019/07/cilia-tiny-cell-structures-with-mighty-functions'
W=[E('cilium','/ˈsɪliəm/','纤毛〔单数〕；睫毛〔学术义〕','细胞表面像一根细毛的小突起。','借新拉丁 cilium，接拉丁眼睑、睫毛相关名称；生物学借它的细毛外形命名。单数结尾 -um，复数是 cilia。',C,'先看一根细细伸出细胞表面的“小毛”。有些纤毛会摆动来推动液体，有些更像感受周围信号的天线；“长得像毛”不表示它就是皮肤上的毛发。','a single cilium；a primary cilium；the structure of a cilium。','cilium 是一个，cilia 是多个；不要把 cilia 再当普通单数随意加 -s。',('The image shows a single cilium projecting from the cell.','图像显示一根从细胞表面伸出的纤毛。'),('A primary cilium can help a cell sense its surroundings.','一根初级纤毛可以帮助细胞感知周围环境。'),sources=['https://www.merriam-webster.com/dictionary/cilium',N]),
E('cilia','/ˈsɪliə/','纤毛〔复数〕；睫毛〔学术义〕','细胞表面一根根细毛状的结构。','cilium 的拉丁式复数，-um 变 -a。英语也曾直接使用拉丁复数 cilia 指睫毛，后来扩展到细胞结构；不是一个词根 cilia 加零后缀。',C+[['英语 cilia','保留拉丁复数形式，常用于一组纤毛']],'一排能摆动的 cilia 可以像许多小桨协同工作，把表面物质往同一方向送。也有不靠摆动工作的感受型纤毛，所以不要把所有 cilia 都想成清扫刷。','motile cilia；cilia on cells；the movement of cilia；cilia are…。','cilia 是复数，搭配 are；a cilium 才是单数。cilia 与整根头发在结构尺度上不同。',('Cilia in the airways help move mucus along the surface.','气道中的纤毛帮助黏液沿表面移动。'),('The researchers compared motile cilia with sensory cilia.','研究人员比较了运动型纤毛与感受型纤毛。'),sources=['https://www.etymonline.com/word/cilia','https://www.merriam-webster.com/dictionary/cilium',N]),
E('superciliously','英 /ˌsuːpəˈsɪliəsli/；美 /ˌsuːpərˈsɪliəsli/','傲慢地；轻蔑地','用一副居高临下的样子对待别人。','supercilious＋-ly，英语副词派生；前半部继承拉丁眉毛到傲慢神态的比喻。',S+[['supercilious ＋ -ly → superciliously','以轻蔑、居高临下的方式']],'它常修饰 smile、look、remark 等动作。不是一定要真的挑眉，而是让读者从动作和说话方式感到：这个人觉得对方低自己一等。','smile superciliously；look at someone superciliously；remark superciliously。','politely 可以礼貌而平等；superciliously 即使声音很轻，也会显得看不起人。',('He smiled superciliously at my suggestion.','他对我的建议轻蔑地笑了笑。'),('“You clearly haven’t read the report,” she remarked superciliously.','“显然你没读过报告。”她居高临下地说。'),sources=['https://www.oxfordlearnersdictionaries.com/definition/english/superciliously','https://www.etymonline.com/word/supercilious'])]
ROOT=dict(meaning='眼睑、睫毛相关材料；纤毛',core='一条支线取细毛的外形，另一条取眉毛表现出的神态。',image='纤毛像细小毛发；轻抬眉毛又能让人联想到高高在上的表情。',intro='拉丁 cilium 与 supercilium 属于眼睑、睫毛、眉毛这一命名群。cilium／cilia 进入生物学成为纤毛；supercilium 已在拉丁语中比喻傲慢，形成 supercilious。更早的构词先后存在争议，不把两个现代词写成彼此派生。',forms='cilium 是单数，cilia 是复数；supercilious 接拉丁形容词，superciliously 再在英语中加 -ly。',branches=[['像睫毛的细胞结构','cilium；cilia'],['眉毛神态的比喻','supercilious；superciliously']],contrasts='supercilious 不是“超级有纤毛的”；它是已有的傲慢比喻。cilia 也不一律是会摆动的刷子。',practice='分别用一根天线、一排小桨和一副轻蔑表情，帮助记住本页的两个分支。',sources=['https://www.etymonline.com/word/cilia','https://www.etymonline.com/word/supercilious',N])
m=json.loads((BASE/'.cache/batch200/rewrite_spec.json').read_text());r=next(x for x in m['roots']if x['id']==ID);c=next(x for x in json.loads((BASE/'.cache/catalog.json').read_text())if x['id']==ID);keep={w['word']for w in W}|set(SHARED);excluded={w:EXCLUDE_REASON for w in(set(r['family'])|set(c['family'])|set(c.get('unmatched',[])))-keep}
ROOT['id']=ID;ROOT['words']=list(dict.fromkeys([w for w in r['family']if w in keep]+[w for w in SHARED if w not in r['family']]));ROOT['exclude']=excluded
assert all(w['word']in m['owned_words']for w in W)
assert not(set(c['family'])|set(c.get('unmatched',[])))-set(ROOT['words'])-set(excluded)
assert {w['word']for w in W}<=set(ROOT['words'])
for w in W:assert len(w['examples'])>=2 and all(len(n)==2 and all(isinstance(x,str)and x for x in n)for n in w['history'])
for k,d in [('roots',[ROOT]),('words',W)]: (OUT/f'{k}_batch200_spec_{TAG}.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
print(ID,len(W),'new,',len(SHARED),'shared')
