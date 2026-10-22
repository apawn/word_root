"""Build root families using source rows and explicit Wiktionary relations."""
import collections
import csv
import json
import re
import unicodedata
import itertools
from pathlib import Path
from wordfreq import zipf_frequency

BASE = Path(__file__).resolve().parents[1]
CACHE = BASE / '.cache'
OUT = BASE / '英语词根资料库'

def load_lexicon():
    lex = collections.defaultdict(list)
    inputs=[(CACHE / 'lexicon.jsonl')]
    if (CACHE/'supplemental-lexicon.jsonl').exists():inputs.append(CACHE/'supplemental-lexicon.jsonl')
    for line in itertools.chain.from_iterable(p.open() for p in inputs):
        d = json.loads(line)
        # Preserve case-sensitive lemmas; name-only records are not study words.
        for t in d['etymology_templates']:
            if t.get('expansion', '').startswith('Etymology tree'):
                t.pop('expansion', None)
        lex[d['word']].append(d)
    return dict(lex)

def clean_term(s):
    return re.sub(r'<[^>]*>', '', s).split('#')[0].strip()

def components(t):
    """Return English components, never cognates or string fragments."""
    name, a = t.get('name'), t.get('args', {})
    lang = a.get('1')
    start = 2
    operation=name
    if name == 'surf':
        lang = a.get('2'); start = 3
        operation={'suf':'suffix','pre':'prefix','con':'confix'}.get(a.get('1','').lstrip('+'),a.get('1','').lstrip('+'))
    elif name in {'ety', 'etymon'}:
        if a.get('2') not in {':af', ':affix', ':com', ':compound', ':suf', ':suffix', ':pre', ':prefix', ':con', ':confix'}:
            return []
        start = 3
        operation={'suf':'suffix','pre':'prefix','con':'confix'}.get(a.get('2','').lstrip(':'),a.get('2','').lstrip(':'))
    elif name not in {'af', 'affix', 'suffix', 'suf', 'prefix', 'pre', 'compound', 'com', 'confix'}:
        return []
    if lang != 'en':
        return []
    items = []
    for i in range(start, 12):
        if str(i) not in a:
            break
        value = clean_term(a[str(i)])
        if ':' in value:
            if value.startswith('en:'):
                value = value[3:]
            else:
                continue
        if not value or value in {'+', '-'}:
            continue
        if operation in {'suffix', 'suf'} and i > start:
            value = '-' + value.lstrip('-')
        if operation in {'prefix', 'pre'} and i == start:
            value = value.rstrip('-') + '-'
        if operation == 'confix':
            if i == start: value = value.rstrip('-') + '-'
            elif i == start+1: value = '-' + value.lstrip('-')
        items.append(value)
    return items

def aliases(root):
    root = re.sub(r'\([^)]*\)', '', root)
    return [x.strip() for x in root.split(',') if re.fullmatch(r'-?[A-Za-z]+-?', x.strip())]

def usable(w):
    return bool(re.fullmatch(r'[a-z][a-z-]*[a-z]', w)) and len(w) > 1

def make_graph(lex):
    graph = collections.defaultdict(dict)
    for w, ds in lex.items():
        if not usable(w):
            continue
        for d in ds:
            for t in d['etymology_templates']:
                for parent in components(t):
                    if parent != w:
                        graph[parent][w] = '词典构词模板'
            # The flattened derived lists contain heading/template leakage.
            # Only explicitly parsed English morphological components are used.
    return graph

PREFIXES = set('ab ad ambi ana ante anti apo bi circum cis co con contra de di dia dis dys e ec ecto en endo epi eu ex exo extra hemi hyper hypo in infra inter intra juxta meta mono multi non ob octo omni pan para per peri poly post pre pro pros proto pseudo re retro se semi sub super supra syn tele trans tri ultra uni'.split())
SUFFIXES = {'-itis','-oid','-oma','-cracy','-crat','-logy','-phile'}

def get_family(seeds, graph, lex, depth=1, skip_parents=None):
    found = {}
    queue = collections.deque((s, 0) for s in seeds)
    visited = set(seeds)
    for s in seeds:
        if s in lex and re.fullmatch(r'[A-Za-z][A-Za-z -]*[A-Za-z]',s):
            found[s] = dict(via=None, depth=0, evidence='根表例词／词基本身')
    while queue:
        parent, level = queue.popleft()
        if level >= depth:
            continue
        if skip_parents and parent in skip_parents:
            continue
        for child, evidence in graph.get(parent, {}).items():
            if child in visited or zipf_frequency(child, 'en') < 2.0:
                continue
            visited.add(child)
            found[child] = dict(via=parent, depth=level+1, evidence=evidence)
            queue.append((child, level+1))
    return found

def main():
    lex = load_lexicon()
    print('Lexicon loaded', len(lex), flush=True)
    graph = make_graph(lex)
    ambiguous_lemmas={w for w,ds in lex.items() if len({str(d.get('etymology_number')) for d in ds if d.get('etymology_number') is not None})>1}
    print('Graph',len(graph),sum(map(len,graph.values())),flush=True)
    rows = json.loads((CACHE / 'classical-roots.json').read_text())
    original = json.loads((CACHE / 'classical-roots.json').read_text())
    # Merge clear repeats in the source table. Retain source-row identifiers.
    mergers = {'C0113':'C0108', 'C0125':'C0110', 'C1092':'C1095',
               'C1148':'C1147', 'C1286':'C1276', 'C1438':'C1433'}
    byid = {r['id']:r for r in rows}
    for r in rows:
        r['source_ids']=[r['id']]
    for old, new in mergers.items():
        byid[new]['source_ids'].append(old)
        byid[new]['words'] += byid[old]['words']
        byid[new]['root'] += ', ' + byid[old]['root']
    rows = [r for r in rows if r['id'] not in mergers]
    alias_counts=collections.Counter(a for r in rows for a in set(aliases(r['root'])))
    extra = {
        'C0011':['acid','acidic'], 'C0066':['aquatic','aquarium','aqueduct'],
        'C0168':['receive','reception','perceive','perception','conceive','conception','deceive','deception'],
        'C0268':['create','creation','creative'], 'C0502':['graph','graphic','graphics'],
        'C0697':['macrocosm','macroeconomics','macroscopic'],
        'C0966':['pace','passage'], 'C1005':['peach'], 'C1113':['prairie'],
        'C1122':['price','precious','appreciate','depreciate'],
        'C1299':['segetal'], 'C1591':['demiurge'],
    }
    if (CACHE/'extra-seeds.json').exists():
        for k,v in json.loads((CACHE/'extra-seeds.json').read_text()).items():extra.setdefault(k,[]).extend(v)
    covered_aliases=set()
    covered_seeds=set()
    roots=[]
    for r in rows:
        r['aliases']=list(dict.fromkeys(aliases(r['root'])))
        r['root']=', '.join(dict.fromkeys(x.strip() for x in r['root'].split(',')))
        r['kind']='古典词根／组合形式'
        if any(a.rstrip('-') in PREFIXES for a in r['aliases']) and len(r['aliases'][0].strip('-')) <= 6:
            r['kind']='古典前缀'
        if r['aliases'] and r['aliases'][0] in SUFFIXES:
            r['kind']='古典后缀／后置组合形式'
        if r['id'] in {'C0602','C0823'}:r['kind']='古典词根／组合形式'
        if r['id']=='C0051':r['kind']='古典前缀'
        r['group']='01_古典词根' if '词根' in r['kind'] else '03_词缀与组合形式'
        seed_words=[]
        for w in r['words'] + extra.get(r['id'],[]):
            w=re.sub(r'\[[^]]*\]', '', w).strip()
            if w in lex: seed_words.append(w)
            elif w.lower() in lex: seed_words.append(w.lower())
            elif re.fullmatch(r'[a-z-]+',w):seed_words.append(w)
        seed_words=list(dict.fromkeys(seed_words))
        r['seeds']=seed_words
        r['added_seeds']=extra.get(r['id'],[])
        # Short and homographic classical strings can represent unrelated roots.
        # Never use them as unqualified dictionary graph pivots.
        safe_aliases=[a for a in r['aliases'] if alias_counts[a]==1 and len(a.strip('-'))>=3]
        r['family']=get_family(seed_words+safe_aliases,graph,lex,skip_parents=ambiguous_lemmas)
        r['unmatched']=list(dict.fromkeys(w for w in r['words'] if w not in lex and w.lower() not in lex))
        r['headword']=None
        r['origin_note']='词根表记录的是历史来源词；它们可能包括同一词的屈折形。英语借入路线按下方各单词的词源记录分别阅读。'
        covered_aliases.update(r['aliases']);covered_seeds.update(seed_words)
        roots.append(r)
    # All recorded English affixes/combining forms with at least one useful,
    # explicitly linked derivative; skip aliases already represented above.
    for w,ds in lex.items():
        aff = next((d for d in ds if d['pos'] in {'prefix','suffix','infix','interfix','circumfix','combining-form','root'}),None)
        if not aff or w in covered_aliases or not re.fullmatch(r'-?[a-z]+-?',w):
            continue
        family=get_family([w],graph,lex)
        if not family:
            continue
        rid=f'A{len(roots):04d}'
        roots.append(dict(id=rid,source_ids=[],root=w,aliases=[w],meaning=aff['senses'][0]['glosses'][-1],meaning_zh='',language='见词源记录',origin=aff['etymology_text'],words=[],seeds=[w],family=family,unmatched=[],headword=w,kind='词缀／组合形式',group='03_词缀与组合形式',source='https://en.wiktionary.org/wiki/'+w,origin_note='词典标为构词成分；它可能是语法词缀，也可能是保留词汇意义的组合形式。'))
    # Free bases: words with a documented history, Zipf >= 3.5, and at least
    # two direct lexical derivatives; no assertion that all are Germanic.
    for w,ds in lex.items():
        if not re.fullmatch(r'[a-z]{2,}',w) or w in covered_seeds or zipf_frequency(w,'en')<3.5 or ds[0]['pos'] not in {'noun','verb','adj','adv'}:
            continue
        direct=[x for x in graph.get(w,{}) if zipf_frequency(x,'en')>=2.0]
        if len(direct)<2:
            continue
        d=next((x for x in ds if x['etymology_text'] and x['pos'] in {'noun','verb','adj','adv'}),None)
        if not d:
            continue
        # Inflected or compound free words are not automatically roots.
        # The supplemental section explicitly calls them free bases.
        family=get_family([w],graph,lex)
        rid=f'B{len(roots):04d}'
        roots.append(dict(id=rid,source_ids=[],root=w,aliases=[w],meaning=d['senses'][0]['glosses'][-1],meaning_zh='',language='见词源记录',origin=d['etymology_text'],words=[],seeds=[w],family=family,unmatched=[],headword=w,kind='英语自由词基',group='02_英语词基',source='https://en.wiktionary.org/wiki/'+w,origin_note='这是现代英语中的自由词基，可继续构词；“词基”不等于历史上不可再分析的最终词根。来源包含日耳曼语本源词和其他语言借词。'))
    for r in roots:
        r['family']=dict(sorted(r['family'].items(),key=lambda kv:(-zipf_frequency(kv[0],'en'),kv[0])))
        rates=[10**(zipf_frequency(w,'en')-9) for w in r['family'] if re.fullmatch('[a-z]+',w)][:20]
        import math
        r['score']=round(math.log10(sum(rates))+9,3) if rates else 0
        r['best_zipf']=max((zipf_frequency(w,'en') for w in r['family']),default=0)
    roots.sort(key=lambda r:(-r['score'],r['root'],r['id']))
    for i,r in enumerate(roots,1):
        slug=re.sub(r'[^a-z0-9]+','-',r['aliases'][0].lower() if r['aliases'] else r['root'].lower()).strip('-') or r['id']
        r['rank']=i
        r['file']=f"{r['group']}/{i:04d}_{slug}_{r['id']}.md"
    (CACHE/'catalog.json').write_text(json.dumps(roots,ensure_ascii=False,indent=2))
    (CACHE/'graph.json').write_text(json.dumps(graph,ensure_ascii=False))
    print('Roots',len(roots),'groups',collections.Counter(r['group'] for r in roots),'word occurrences',sum(len(r['family']) for r in roots),flush=True)
    print('Unique words',len({w for r in roots for w in r['family']}),flush=True)
    print('Empty families',[(r['id'],r['root']) for r in roots if not r['family']],flush=True)

if __name__=='__main__':main()
