# coding: utf-8
import json
from pathlib import Path
from author_batch200_root_organ_a import W as A
from author_batch200_root_organ_b import W as B
W=A+B
SHARED='organ organist organize organizer organized reorganize organic organically inorganic organism microorganism organelle'.split()
kept=SHARED+[x['word'] for x in W]
r=next(x for x in json.loads(Path('.cache/catalog.json').read_text()) if x['id']=='C0917')
EX={w:'本页先略过更专门的胚胎发育术语' for w in set(r['family'])|set(r['words']) if w not in kept and '-' not in w}
ROOT=dict(id='C0917',meaning='工具；承担功能的器官；配合运作的整体',core='ORGAN = INSTRUMENT / FUNCTIONAL PART',image='身体里，心脏和肺各做自己的工作，又共同维持生命。一个组织也靠不同的人和部门分工配合。这是器官到组织的一条直观联系。',intro='希腊 organon 表工具、乐器和身体器官，核心是“用来发挥某种作用的东西”。经拉丁 organum 分出乐器、身体器官和组织构造等支线；organ 还可指管风琴。',forms='organ 是器官或乐器，organism 是生物体，organic 的含义随生物、化学、食品等场景变化。organization 有独立的拉丁／法语名词来源；现代虽对应 organize + -ation，历史借入不能简单倒推。',branches=[['器官与乐器','organ, organist, organelle'],['生命与物质','organism, microorganism, organic, organically, inorganic'],['把部分组织起来','organize, organise, reorganize, organizer, organized, organised'],['组织整体和组织工作','organization, organisation, organizational, organisational']],contrasts='organ 是承担功能的部分，organism 是生物体，organization 是组织或安排。organic 不在所有场景都译成“有机食品”，先看语境。',practice='A good organization depends on people who can organize work and cooperate with one another.\n\n一个良好的组织需要有人把工作安排好，也需要大家相互配合。',words=kept,exclude=EX)
if __name__=='__main__':
 for name,data in [('roots_organ',[ROOT]),('words_organ',W)]:Path('.cache/batch200/drafts/root/'+name+'.json').write_text(json.dumps(data,ensure_ascii=False,indent=2))
 print(len(W),sum(len(x['examples']) for x in W))
