"""Extract a study-sized, traceable subset of the openly licensed Kaikki dump.

No spelling-substring matching is used to establish etymological relationships.
"""
import json
import re
import time
from pathlib import Path
from wordfreq import zipf_frequency

BASE = Path(__file__).resolve().parents[1]
CACHE = BASE / '.cache'
roots = json.loads((CACHE / 'classical-roots.json').read_text())
seeds = {w.lower() for r in roots for w in r['words']}
SIZE = 3335546346
affixes = {'prefix', 'suffix', 'infix', 'interfix', 'circumfix', 'combining-form', 'root'}
excluded = {'name', 'character', 'symbol', 'punct', 'romanization', 'proverb', 'phrase'}

def clean_etym(text):
    if text.startswith('Etymology tree\n'):
        # Tree labels form a graph, not a linear chain. Keep the following prose.
        lines = text.splitlines()
        for i, line in enumerate(lines):
            if i and re.match(r'(From |Borrowed |Inherited |By |Originally |Probably |Apparently |Uncertain |Unknown |Either |A |An |Blend |Compound |Clipping |Back-formation |Doublet |Named |Coined |Derived |Equivalent |Ultimately |First |Possibly |See |Of |Perhaps |Onomatopoeic)', line):
                return '\n'.join(lines[i:])
        return ''
    return text

total = kept = 0
with (CACHE / 'english.jsonl').open('rb') as src, (CACHE / 'lexicon.jsonl').open('w') as dst:
    while True:
        offset = src.tell()
        line = src.readline()
        if not line.endswith(b'\n'):
            src.seek(offset)
            if (CACHE / 'english.jsonl').stat().st_size >= SIZE:
                break
            time.sleep(0.5)
            continue
        total += 1
        d = json.loads(line)
        w = d.get('word', '')
        pos = d.get('pos', '')
        if d.get('lang_code') != 'en' or (pos in excluded and w.lower() not in seeds):
            continue
        if not re.fullmatch(r"[A-Za-z][A-Za-z'’ -]{0,65}|-[A-Za-z-]+|[A-Za-z]+-", w):
            continue
        z = zipf_frequency(w, 'en')
        if w.lower() not in seeds and pos not in affixes and z < 2.0:
            continue
        senses = []
        for s in d.get('senses', []):
            if 'form_of' in s or 'alt_of' in s:
                continue
            if set(s.get('tags', [])) & {'obsolete', 'archaic', 'historical', 'nonstandard', 'misspelling'} and w.lower() not in seeds:
                continue
            ss = {k: s[k] for k in ['glosses', 'tags', 'topics'] if k in s}
            ss['examples'] = [{k: ex[k] for k in ['text', 'translation', 'type', 'tags'] if k in ex}
                              for ex in s.get('examples', [])
                              if ex.get('type') == 'example' and len(ex.get('text', '')) < 600]
            if ss.get('glosses'):
                senses.append(ss)
        if not senses:
            continue
        templates = []
        for t in d.get('etymology_templates', []):
            t = dict(t)
            if t.get('name') == 'etymon':
                t.pop('expansion', None)
            templates.append(t)
        slim = dict(word=w, pos=pos, zipf=z, senses=senses,
                    etymology_number=d.get('etymology_number'),
                    etymology_text=clean_etym(d.get('etymology_text', '')),
                    etymology_templates=templates,
                    etymology_links=d.get('etymology_links', []),
                    sounds=[s for s in d.get('sounds', []) if 'ipa' in s],
                    translations=[t for t in d.get('translations', []) if t.get('code') in {'zh', 'cmn'}],
                    derived=[x['word'] for x in d.get('derived', []) if 'word' in x and zipf_frequency(x['word'], 'en') >= 2.0])
        dst.write(json.dumps(slim, ensure_ascii=False) + '\n')
        kept += 1
        if total % 10000 == 0:
            dst.flush()
            print(f'Processed {total:,}; retained {kept:,}; input {offset/1e9:.2f} GB', flush=True)
print(f'Done: {total:,} source entries; {kept:,} retained', flush=True)
(CACHE / 'extraction-done.json').write_text(json.dumps(dict(total=total, kept=kept)))
