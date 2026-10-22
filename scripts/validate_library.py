"""Check the generated artifact's coverage, references and structure."""
import collections
import csv
import hashlib
import json
import re
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import unquote
from explanatory import load_lessons,word_has_image,root_has_image,images_paused

B=Path(__file__).resolve().parents[1];O=B/'英语词根资料库'
R=json.loads((O/'data/条目清单.json').read_text())
S=json.loads((O/'data/统计.json').read_text())
errors=[]
def check(condition,message):
    if not condition:errors.append(message)
expected={r['file'] for r in R}
actual={str(p.relative_to(O)) for folder in ['01_古典词根','02_英语词基','03_词缀与组合形式'] for p in (O/folder).glob('*.md')}
check(expected==actual,'Root Markdown manifest mismatch')
check(len(R)==S['entries'],'Entry count mismatch')
check(len({r['id'] for r in R})==len(R),'Duplicate stable IDs')
check(all(R[i]['score']>=R[i+1]['score'] for i in range(len(R)-1)),'Ranking is not descending')
source_ids=[s for r in R for s in r['source_ids']]
check(len(source_ids)==1680 and len(set(source_ids))==1680,'Source rows not covered exactly once')
check(len({w for r in R for w in r['family']})==S['unique_words'],'Unique word count mismatch')
byid={r['id']:r for r in R}
check('receive' in byid['C0168']['family'],'cap family missing receive')
check('jury-rig' not in byid['C0627']['family'],'Unrelated jury sense leaked into law root')
check('case-sensitive' not in byid['C0153']['family'],'Unrelated case sense leaked into fall root')
hyphens=set('-\u00ad\u2010\u2011\u2012\u2013\u2014\u2212\ufe63\uff0d')
check(not any(set(w)&hyphens for r in R for w in r['family']),'Hyphenated vocabulary is still present')
lessons,authored=load_lessons()
P=json.loads((O/'data/精讲进度.json').read_text())
expected_digest=hashlib.sha256(json.dumps({'roots':lessons,'words':authored},ensure_ascii=False,sort_keys=True).encode()).hexdigest()
check(P.get('authored_sha256')==expected_digest,'Rendered lessons are stale relative to authored content')
used={w for r in R if r['id'] in lessons for w in r['family']}
check(set(P['completed_root_ids'])==set(lessons),'Completed lesson IDs mismatch')
check(P['root_pages']==len(lessons),'Completed root count mismatch')
check(P['unique_words']==len(used),'Completed word count mismatch')
check(P['examples']==sum(len(authored[w]['examples']) for w in used),'Authored example count mismatch')
for rid,lesson in lessons.items():
    r=byid[rid];body=(O/r['file']).read_text()
    check(set(r['family'])==set(lesson['words']),f'Lesson family mismatch: {rid}')
    check(len(re.findall(r'^### \d+\. ',body,re.M))==len(r['family']),f'Missing word explanations: {rid}')
    check(body.count('**先抓住这个画面**')==len(r['family']),f'Missing word mental picture: {rid}')
    check(body.count('../assets/evolution/')==sum(word_has_image(authored[w]) for w in r['family']),f'Word diagram availability mismatch: {rid}')
    check(body.count('**怎么变成今天的意思**')==len(r['family']),f'Missing evolution explanations: {rid}')
    check(len(re.findall(r'^> ',body,re.M))==sum(len(authored[w]['examples']) for w in r['family']),f'Missing examples: {rid}')
    check(not any(t in body for t in ['常用度代理分数','稳定编号','当前资料缺项','例句**：待补充','音标来源','本页归属依据','未逐词义进行人工对齐','## 来源与版本']),f'Unwanted metadata in lesson: {rid}')
    for w in r['family']:
        check(all(len(pair)==2 and all(isinstance(v,str) and v.strip() for v in pair) for pair in authored[w]['examples']),f'Incomplete bilingual example: {w}')
links=svgcount=pages=0
anchor_contents={}
for p in O.rglob('*.md'):
    pages+=1;text=p.read_text()
    check('data-lang=' not in text and '"terms" :' not in text,f'Template debris: {p.name}')
    for target in re.findall(r'(?<!\\)\]\(([^\n]*?)\)',text):
        if target.startswith(('http:','https:','mailto:')):continue
        links+=1
        part,_,anchor=target.partition('#')
        if part:
            dest=(p.parent/unquote(part)).resolve()
            check(dest.exists(),f'Broken local link: {p.relative_to(O)} -> {target}')
            if anchor and dest.exists() and dest.suffix=='.md':
                if dest not in anchor_contents:anchor_contents[dest]=dest.read_text()
                check(f'id="{anchor}"' in anchor_contents[dest],f'Broken cross-page anchor: {p.name} -> {target}')
        elif anchor:
            check(f'id="{anchor}"' in text,f'Broken local anchor: {p.name} -> {anchor}')
for p in (O/'assets').glob('*.svg'):
    svgcount+=1
    try:ET.parse(p)
    except Exception as e:errors.append(f'Invalid SVG {p.name}: {e}')
check(svgcount==len(R),'SVG count mismatch')
evolution_count=0
for p in (O/'assets/evolution').glob('*.svg'):
    evolution_count+=1
    try:ET.parse(p)
    except Exception as e:errors.append(f'Invalid evolution SVG {p.name}: {e}')
illustrated={w for w in used if word_has_image(authored[w])}
check(P['diagrams']==len(illustrated),'Referenced evolution diagram count mismatch')
check(P.get('pending_word_diagrams',0)==len(used-illustrated),'Pending evolution diagram count mismatch')
pending_roots={rid for rid in lessons if not root_has_image(byid[rid],lessons[rid])}
check(P.get('pending_root_diagrams',0)==len(pending_roots),'Pending root diagram count mismatch')
if images_paused():
    plan=json.loads((O/'data/待补图清单.json').read_text())
    check(set(plan['words'])==used-illustrated,'Pending image word list mismatch')
    check(set(plan['root_ids'])==pending_roots,'Pending image root list mismatch')
    baseline=B/'.cache/assets-at-image-pause.json'
    if baseline.exists():
        before=json.loads(baseline.read_text())
        now={str(p.relative_to(B)):[p.stat().st_size,p.stat().st_mtime_ns] for p in (O/'assets').rglob('*.svg')}
        check(before==now,'Images were changed while generation is paused')
else:
    check(evolution_count==P['diagrams']==len(used),'Evolution diagram count mismatch')
for row in csv.DictReader((O/'data/覆盖明细.csv').open()):
    for field in ['ipa','zh','etym','example','split']:
        check(int(row.get(field) or 0)<=int(row['words']),f'Invalid coverage: {row["id"]}/{field}')
report={'ok':not errors,'root_pages':len(R),'markdown_files':pages,'svg_files':svgcount,'evolution_svg_files':evolution_count,'completed_lessons':P['root_pages'],'fully_explained_words':P['unique_words'],'authored_bilingual_examples':P['examples'],'checked_local_links_and_anchors':links,'source_rows':len(source_ids),'unique_words':S['unique_words'],'errors':errors}
(O/'data/结构校验.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
print(json.dumps(report,ensure_ascii=False,indent=2))
raise SystemExit(bool(errors))
