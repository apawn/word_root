"""Check every rendered root and word section; record borrowed function words for review."""
import collections
import json
import re
from pathlib import Path

from component_glosses import detailed_split, dictionary_notes, english_base_glosses, root_details
from explanatory import load_lessons


BASE = Path(__file__).resolve().parents[1]
OUT = BASE / '英语词根资料库'
HEADING = re.compile(r'^### \d+\. ([^\n]+)$', re.M)
FUNCTION_WORDS = {
    'fr':r"\b(?:à|de|du|des|la|le|les|en|se|par|au|aux)\b|\b[ld]’",
    'fro':r"\b(?:a|de|li|le|la|les|par|en)\b", 'frm':r"\b(?:a|de|la|le|les|en)\b",
    'xno':r"\b(?:a|de|la|le|les|en)\b", 'it':r"\b(?:a|alla|di|da|in)\b|\ball’",
    'roa-oit':r"\ball’", 'es':r"\b(?:el|de|la|con|las|los)\b",
    'la':r"\b(?:ad|ab|ante|ex|in|non|nōn|per|pro|prō|sine|sub|et)\b",
    'la-med':r"\b(?:ad|de|dē|ab|in|sub|cum|per|et)\b",
    'la-lat':r"\b(?:ad|ab|ante|de|in|et)\b",
}

def source_lines():
    for path in sorted((OUT/'data/词条来源').glob('part-*.jsonl')):
        with path.open() as part:
            yield from part

def source_inventory():
    entries = collections.defaultdict(list)
    grammatical = collections.defaultdict(set)
    for line in source_lines():
        entry = json.loads(line)
        word = entry['word']
        entries[word].append(entry)
        for t in entry.get('etymology_templates',()):
            if t['name'].rstrip('+') not in ('inh','der','bor','lbor','slbor','ubor'):
                continue
            args = t['args']
            lang = args.get('2')
            term = args.get('3','').replace("'",'’')
            match = FUNCTION_WORDS.get(lang)
            is_arabic = lang == 'ar' and re.search(r'(?:^|\s)ال|(?:^|\s)ا[َِ]?ل',term)
            if (match and re.search(match,term,re.I) and (' ' in term or '’' in term)) or is_arabic:
                grammatical[word].add((lang,term))
    return entries, grammatical

def check_examples(words,bases):
    # Protect the historical distinctions that motivated the corpus pass.
    cases = {
        'alert':('a + la','阴性单数定冠词','l’','erta','高处'),
        'alarm':('alle armi','阴性复数定冠词'),
        'algebra':('阿拉伯语 al-','jabr','补全'),
        'particle':('partis','-icula','-icle'),
        'denim':('serge','de','来自','Nîmes'),
        'arsenal':('dār','定冠词','同化'),
        'apron':('a napron','an apron','冠词'),
        'leatherette':('仿制品',),
        'ally':('ad-','同化','ligāre'),
    }
    for word,tokens in cases.items():
        explanation = detailed_split(words[word],bases.get(word,()))
        assert all(t in explanation for t in tokens), (word,tokens)
    for word,wrong in [('leatherette','-ette（指较小'),('lonely','把性质用来说明方式'),
                       ('ally','意大利语 a 是介词'),('icicle','拉丁语 pars 是词典')]:
        assert wrong not in detailed_split(words[word],bases.get(word,())), (word,wrong)

def inspect():
    catalog = json.loads((OUT/'data/条目清单.json').read_text())
    lessons, words = load_lessons()
    entries, grammatical = source_inventory()
    bases = english_base_glosses(words,entries)
    check_examples(words,bases)
    summary = collections.Counter()
    touched_heads = set()
    all_heads = set()
    extended_history = set()
    audit = {}
    changed_pages = []
    for root in catalog:
        file = OUT/root['file']
        body = file.read_text()
        matches = list(HEADING.finditer(body))
        header = body[:matches[0].start()] if matches else body
        lesson = lessons.get(root['id'])
        summary['root_pages_checked'] += 1
        if lesson:
            intro,forms = root_details(root,lesson)
            assert intro in header and forms in header, ('stale root', file)
            root_changed = (intro,forms) != (lesson['intro'],lesson['forms'])
        else:
            notes = dictionary_notes(root.get('origin',''),root['root'])
            assert all(n in header for n in notes), ('dictionary root',file)
            root_changed = bool(notes)
        summary['root_introductions_supplemented'] += root_changed
        seen = []
        changed = []
        for i,m in enumerate(matches):
            word = m[1].split(' — ',1)[0] if lesson else m[1]
            section = body[m.end():matches[i+1].start() if i+1<len(matches) else len(body)]
            seen.append(word)
            all_heads.add(word)
            summary['word_occurrences_checked'] += 1
            if lesson:
                original = words[word]
                rendered = detailed_split(original,bases.get(word,()))
                assert '\n**怎么拆**\n\n'+rendered+'\n' in section, (file,word)
                edited = rendered != original['split']
                if rendered.count('\n\n') > original['split'].count('\n\n'):
                    extended_history.add(word)
            else:
                gloss = re.search(r'^\*\*中文释义\*\*：(.*)$',section,re.M)
                formulas = re.search(r'^\*\*构词拆分\*\*：(.*)$',section,re.M)
                history = re.search(r'^\*\*词源与演化\*\*：\n\n([^\n]+)',section,re.M)
                splits = formulas[1].split('；') if formulas else []
                source = (history[1] if history else '')+'\n'+'\n'.join(splits)
                notes = dictionary_notes(source,word,splits,gloss[1] if gloss else '')
                assert all(n in section for n in notes), (file,word,'dictionary')
                edited = bool(notes)
                if dictionary_notes(source,word):
                    extended_history.add(word)
            if edited:
                changed.append(word)
                touched_heads.add(word)
                summary['word_occurrences_supplemented'] += 1
        assert seen == list(root['family']), (file, 'unexpected headings')
        if root_changed or changed:
            changed_pages.append(root['id'])
        audit[root['id']] = {'file':root['file'],'checked':len(seen),'root_note_added':root_changed,'words_supplemented':changed}
    assert all_heads==set(entries), ('archive and rendered inventory differ',len(all_heads),len(entries))
    stats = json.loads((OUT/'data/统计.json').read_text())
    assert (len(catalog),len(all_heads),summary['word_occurrences_checked']) == (stats['entries'],stats['unique_words'],stats['word_occurrences'])
    summary.update(distinct_words_checked=len(all_heads),distinct_words_with_historical_note=len(extended_history), pages_supplemented=len(changed_pages),distinct_words_supplemented=len(touched_heads))
    report = {
        'scope':'按当前条目清单逐页检查词根说明及每个已收词条。补注依据原文中的旧词形、明确构词式和词条专门说明。没有命中规则不代表逐词专家审定。',
        'counts':dict(summary),
        'source_phrases':{w:sorted(grammatical[w]) for w in sorted(grammatical)},
        'sense_review':{
            'corona':'西班牙语 La Corona 是雪茄品牌名。当前讲日冕等义，保留拉丁 corōna 的说明。',
            'dally':'西班牙语 dale la vuelta 属于另一条有争议的套索义来源，未用于本条“磨蹭、调情”。',
            'chagrin':'peau de sagrin 指粗糙皮革，与懊恼义的关系属于异说，保留不确定性。',
        },
        'pages':audit,
    }
    (OUT/'data/构词细读核查.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(dict(summary),ensure_ascii=False))

if __name__ == '__main__':
    inspect()
