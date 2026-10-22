"""Index reusable examples with explicit sentence/source attribution."""
import bz2
import collections
import json
import re
from pathlib import Path

P=Path('.cache')
C=json.loads((P/'catalog.json').read_text())
words={w.lower() for r in C for w in r['family']}
examples=collections.defaultdict(list)
wn=P/'wordnet'/'wordnet'
for pos in ['noun','verb','adj','adv']:
    for line in (wn/('data.'+pos)).open():
        if not line[:1].isdigit() or ' | ' not in line:continue
        body,gloss=line.split(' | ',1)
        fields=body.split();n=int(fields[3],16)
        lemmas={fields[4+2*i].replace('_',' ').removesuffix('(a)').removesuffix('(p)').removesuffix('(ip)') for i in range(n)}
        definition=gloss.split('; "')[0].strip()
        for s in re.findall(r'"([^"\n]+)"',gloss):
            if not 4<=len(s.split())<=40:continue
            for w in lemmas & words:
                if re.search(r'(?<![a-z])'+re.escape(w)+r'(?![a-z])',s.lower()):
                    text=s[0].upper()+s[1:]
                    if text[-1]not in '.!?':text+='.'
                    examples[w].append(dict(text=text,source='WordNet 3.0',pos=pos,gloss=definition,ref=f'{pos}:{fields[0]}',url='https://wordnet.princeton.edu/'))
f=P/'tatoeba-english.tsv.bz2'
if f.exists():
    best={}
    with bz2.open(f,'rt') as src:
        for line in src:
            parts=line.rstrip('\n').split('\t')
            if len(parts)<4:continue
            sid,lang,s,author=parts[:4]
            if lang!='eng' or not 6<=len(s.split())<=24 or len(s)>180 or s[-1:]not in '.!?':continue
            if not author or author=='\\N':continue
            tokens=set(re.findall(r"[a-z]+(?:-[a-z]+)*",s.lower()))
            score=-abs(len(s.split())-12)
            for w in tokens & words:
                if w not in best or score>best[w][0]:
                    best[w]=(score,dict(text=s,source='Tatoeba',author=author,ref=sid,url='https://tatoeba.org/en/sentences/show/'+sid))
    for w,(_,e) in best.items():examples[w].append(e)
(P/'examples-index.json').write_text(json.dumps(examples,ensure_ascii=False))
print('Words with supplemental examples',len(examples),'Tatoeba',sum(any(x['source']=='Tatoeba' for x in es)for es in examples.values()))
