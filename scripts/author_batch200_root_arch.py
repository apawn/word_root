# coding: utf-8
import json
from pathlib import Path
from author_batch200_root_arch_a import W as A
from author_batch200_root_arch_b import W as B
from author_batch200_root_arch_c import W as C
from author_batch200_root_arch_d import W as D
from author_batch200_root_arch_e import W as E
W=A+B+C+D+E;kept=[w['word'] for w in W]+['architect','architecture','architectural','archdiocese','archetype','archetypal','archenemy']
r=next(x for x in json.loads(Path('.cache/catalog.json').read_text()) if x['id']=='C0071')
EX={w:'较冷门的古代官职、政体术语或低收益派生，本轮暂略' for w in set(r['family'])|set(r['words']) if w not in kept and '-' not in w}
ROOT=dict(id='C0071',meaning='率先、开始；首要、统领、统治',core='ARCH = FIRST, CHIEF, RULE',image='先站到队伍前面，可以是率先开始，也可以是带领别人。architect 的古老画面是首席建造者；monarch 是一位君主；archrival 则是最主要的对手。',intro='希腊 arkhein 同时有开始、带头和统治的相关意义，arkhe 可表开端或统治，arkhi- 表首要。archetype 走最初模型这条线，-archy 走统治或组织方式这条线，不要只背成一个抽象的“统”。',forms='arch-、archi-、arche- 可在前，-arch 常指领导者，-archy 常指治理或组织方式。ch 在 monarch、architect、archangel 等词中读 /k/，在 archbishop、archrival 等词中读 /tʃ/。拼写相同也要逐词看音标。',branches=[['首席与首要地位','architect, architecture, architectural, architecturally, archbishop, archdiocese, archangel, archrival, archenemy'],['最初模型','archetype, archetypal'],['层级组织','hierarchy, hierarchical'],['君主及其制度、支持者','monarch, monarchy, monarchical, monarchist, monarchism'],['无统治权威与相关思想','anarchy, anarchist, anarchism, anarchic, anarchistic'],['家族与社会权力','patriarch, patriarchy, patriarchal, matriarch, matriarchy, matriarchal'],['少数人掌权','oligarch, oligarchy, oligarchic']],contrasts='monarch 是人，monarchy 是制度，monarchist 是支持者。anarchy 的混乱义不能代替 anarchism 的理论含义。patriarchy／matriarchy 说权力，父系／母系继承说亲属追溯。建筑的拱形 arch 来自另一条拉丁 arcus 路线。',practice='The chart shows a hierarchy, but it does not by itself tell us whether the organization is democratic or oligarchic.\n\n这张图展示了层级结构，但仅凭它，不能判断这个组织实行民主决策还是由少数人把持。',words=kept,exclude=EX)
if __name__=='__main__':
 for name,data in [('roots_arch',[ROOT]),('words_arch',W)]:Path('.cache/batch200/drafts/root/'+name+'.json').write_text(json.dumps(data,ensure_ascii=False,indent=2))
 print(len(W),sum(len(w['examples']) for w in W))
