import json
from pathlib import Path
from author_batch200_root_acid_a import W as A
from author_batch200_root_acid_b import W as B
W=A+B;kept=[x['word'] for x in W]
r=next(x for x in json.loads(Path('.cache/catalog.json').read_text()) if x['id']=='C0011')
EX={w:'本轮先略过冷门或更专门的词，保留常用酸性词族' for w in set(r['family'])|set(r['words']) if w not in kept and '-' not in w}
ROOT=dict(id='C0011',meaning='酸；酸味般尖锐',core='ACID = SOUR / SHARP',image='一口酸醋让舌头一激灵。一句话也能让人心里一刺：酸味 → 刺激感 → 尖刻的语气。化学支线则把“酸”发展成更精确的物质概念。',intro='来自拉丁 acidus“酸的、尖锐的”，接 acere“发酸”。英语经法语 acide 或直接从拉丁借入 acid，后来长出描述性质、变化和医学状态的词。',forms='acid 是核心词；-ic 说性质，-ity 把性质名词化，-ify 说使变化，-ification 说变化过程。部分名词是独立从法语借来的，学习拆分不等于真实借词顺序。',branches=[['酸与酸性','acid, acidic, acidity'],['向更酸变化','acidify, acidification'],['尖刻语气','acidly'],['医学中的酸','antacid, acidosis']],contrasts='acidic 是状态，acidify 是变化，acidification 是过程。antacid 作用于胃酸，acidosis 涉及体内酸碱失衡，不能当成同一件事。',practice='The soil is already acidic, and the study examines whether it is continuing to acidify.\n\n土壤已经呈酸性，这项研究检查它是否还在继续酸化。',words=kept,exclude=EX)
if __name__=='__main__':
 for name,data in [('roots_acid',[ROOT]),('words_acid',W)]:Path('.cache/batch200/drafts/root/'+name+'.json').write_text(json.dumps(data,ensure_ascii=False,indent=2))
 print(len(W),sum(len(x['examples']) for x in W))
