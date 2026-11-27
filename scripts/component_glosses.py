"""Explain attested expressions in their original language, at the point of use."""
import re
import unicodedata
from functools import lru_cache
from pathlib import Path

DATA = Path(__file__).resolve().parents[1] / 'content/精讲/构词细读'
# Keep Unicode letters (and combining marks) together, but allow adjacent Chinese.
LETTERS = "A-Za-zÀ-ɏΑ-Ͽἀ-῾Ḁ-ỿ\\u0300-\\u036fÞþÐð"
TOKEN = re.compile(rf'(?<![{LETTERS}-])-?[{LETTERS}]+-?(?![{LETTERS}-])')
CLAUSE = re.compile(r'[。；;！？!?\n]')
REJECT = re.compile(r'不是|不由|不宜拆|不拆|不必拆|不能|不要|不按|勿拆|并非|误拆|误认为|误解为|硬拆|错拆|不像|非由|别拆|别把|不等于|无关|不来自|无可靠|不可靠|未必|假词源|民间词源|并无|并不|不可拆')
UNCERTAIN = re.compile(r'也许|可能|说法|据说|一种解释|有争议|有争论|未定|推测|不确定|拟构|有时分析|传统')

def fold(value):
    return unicodedata.normalize('NFC', value).lower().replace("'", "’")

def rows(file):
    for line in (DATA/file).read_text().splitlines():
        if line.strip() and not line.startswith('#'):
            left, note = line.strip().split('\t')
            yield left.split('|'), note

PHRASES = {}
for variants, note in (*rows('短语.tsv'), *rows('旧词形.tsv')):
    for term in variants:
        PHRASES[fold(term)] = note
PHRASE = re.compile(rf'(?<![{LETTERS}-])(?:'+'|'.join(re.escape(t) for t in sorted(PHRASES,key=len,reverse=True))+rf')(?![{LETTERS}-])')

WORD_NOTES = {word: note for words, note in rows('逐词.tsv') for word in words}

PIECES = {}
for variants, note in rows('成分.tsv'):
    condition = variants.pop()[1:] if variants[-1].startswith('@') else ''
    for term in variants:
        PIECES.setdefault(term, []).append((condition,note))

CONTEXT_MARKERS = {
    'oldverb': ('第三人称','三单'), 'small': ('小称','指小'), 'chem': ('醇',),
     'smaller': ('指小','小称','小型'), 'mannered': ('方式','程度','在……方面'),
    'subbelow': ('下方','之下','下面','地下','水下','海底','次级','下级','低于'),
    'outof': ('向外','从中','抽出','取出','出去','向上'), 'together': ('共同','会合','合在','一起'),
    'apart': ('分开','分离','相反','逆转','相异'), 'adgoal': ('朝向','指向','趋向'),
    'record': ('图像','记录','图线'), 'discipline': ('研究','学科','学问'),
    'bodysome': ('soma','sōma','希腊的身体'), 'link': ('连接','结合元音','连缀'),
    'self': ('自身','自己','自动'), 'remove': ('去除','移除','解除','除去'),
    'make': ('使成为','使进入','使具有'), 'kin': ('亲属','祖父','祖母','父母','外孙','孙','继父','继母'),
    'field': ('学科','学名'), 'verb': ('使变','变得','使动','动词化'),
    'material': ('材料','……制成','制成的'), 'participle': ('过去分词',),
    'forward': ('向前','朝前'), 'through': ('从头到尾','贯穿','穿过'), 'throw': ('抛','投掷','扔'),
}

def context_tag(tag, sense, local, term, word):
    if not tag:
        return True
    if tag == 'adverb':
        return word.lower().endswith('ly') and ('副词' in local or sense.split('；')[0].endswith('地')) and '形容词和副词' not in local
    if tag == 'lyadj':
        return word.lower().endswith('ly') and ('形容词' in local or sense.split('；')[0].endswith('的')) and '副词' not in local
    if tag == 'adjsome':
        return word.endswith('some') and '形容词' in local and '希腊' not in local
    if tag in CONTEXT_MARKERS:
        return any(marker in local for marker in CONTEXT_MARKERS[tag])
    if tag == 'latin':
        return '拉丁' in local
    if tag in ('past','ing','agent','third','both','plural','comparative','superlative','adj','noun'):
        if word and term.startswith('-') and not word.lower().endswith(term[1:]):
            return False
    plural = '复数' in sense
    third = '第三人称' in sense or '三单' in sense
    if tag == 'both':
        return plural and third
    if tag == 'third':
        return third and not plural
    if tag == 'plural':
        return plural and not third
    if tag == 'comparative':
        return '比较级' in sense or sense.startswith(('更','较'))
    if tag == 'superlative':
        return '最高级' in sense or sense.startswith('最')
    if tag == 'agent':
        return ('比较级' not in sense and not sense.startswith(('更','较')) and
                re.search(r'[者员师匠器机手]|的人',sense) is not None)
    if tag == 'past':
        return re.search('过去式|过去分词|过去时',local+sense) is not None
    if tag == 'ing':
        return re.search('现在分词|动名词|进行时|进行中的',local+sense) is not None
    if tag == 'adj':
        return ('形容词' in local or sense.split('；')[0].endswith('的')) and '名词和形容词' not in local
    if tag == 'noun':
        return '名词' in local and '形容词' not in local
    if tag == 'neg':
        return re.search(r'否定(?:前缀|成分)?[“「\s]*'+re.escape(term),local) is not None
    if tag == 'reverse':
        return '逆转' in local or '反向' in local or '撤销' in local
    if tag == 'into':
        return '向内' in local and '否定' not in local
    if tag == 'again':
        return '再次' in local or '重新' in local
    if tag == 'back':
        return ('向回' in local or '往回' in local) and '再次' not in local
    raise ValueError(tag)

def formula_tokens(clause):
    for m in TOKEN.finditer(clause):
        before, after = clause[:m.start()].rstrip(), clause[m.end():].lstrip()
        if not (before.endswith(('+','＋')) or after.startswith(('+','＋'))):
            continue
        # A gloss already follows this occurrence. Quoted or bracketed original
        # material and uncertain reconstructions should keep the author's wording.
        if after.startswith(('“','「','〔','（','(','[','即','指','表示','意为','是','意为')):
            continue
        if re.match(r'^[\u3400-\u9fff]', after) and not after.startswith(('形成','构成','组成','得到','演化成','演变为','组合成','变成','合成','相接','成为')):
            continue
        if before.endswith(('*','/','／','-')) or after.startswith(('/','／','-')):
            continue
        yield m

def annotated(prose, word='', sense='', bases=()):
    seen = set()
    # A definition elsewhere in this very explanation takes priority over a
    # general gloss even if the bare formula happens to occur first.
    for occurrence in TOKEN.finditer(prose):
        term = occurrence.group()
        tail = prose[occurrence.end():].lstrip()
        if (tail.startswith(('“','〔','「','（','表示','意思是','相当于','用于','在此','这里','在这里','在本词'))
                or re.match(r'^[一-龥]{1,8}[、＋+]',tail)):
            seen.add(term)
    def clause_edit(match):
        clause = match.group()
        if REJECT.search(clause) or UNCERTAIN.search(clause):
            return clause
        adds = []
        for m in formula_tokens(clause):
            term = m.group()
            if term in seen:
                continue
            choices = [note for tag,note in PIECES.get(term,()) if context_tag(tag,sense,clause,term,word)]
            if not choices and bases:
                gloss = dict(bases).get(term)
                if gloss:
                    choices = [gloss]
            if len(choices) == 1:
                adds.append((m.end(), '（'+choices[0]+'）'))
                seen.add(term)
        for i, insert in reversed(adds):
            clause = clause[:i]+insert+clause[i:]
        return clause
    return re.sub(r'[^。；;！？!?\n]+',clause_edit,prose)

# Very short modern English phrases or examples need a sense-specific context.
RESTRICT = {
    'all one': {'alone','lone','lonely','loneliness','lonesome'},
    'at one': {'atone','atonement','atoning'},
    'on side': {'aside'}, 'on life': {'alive'}, 'per cent': {'percent','percentage','percentile','percentages','per cent'},
    'lagarto': {'alligator','alligators'}, 'lieutenant': {'lieutenant','lieutenants','lieutenancy'},
    'scapegoat': {'scapegoat','scapegoats','scapegoating','scapegoated'},
}


def phrase_notes(prose, word='', *, allow_direct=True):
    found = [WORD_NOTES[word]] if allow_direct and word in WORD_NOTES else []
    for clause in CLAUSE.split(fold(prose)):
        for match in PHRASE.finditer(clause):
            term = match.group()
            if term in RESTRICT and word.lower().strip('-') not in RESTRICT[term]:
                continue
            if REJECT.search(clause[:match.start()]):
                continue
            note = PHRASES[term]
            if note not in found:
                found.append(note)
    return found

# These base words have a reviewed, sense-specific explanation of an absorbed
# function word. Show it one layer down when the author actually named the base.
BASE_EXPRESSIONS = {
    'alert':'all’erta', 'alarm':'all’arme', 'algebra':'al-jabr',
    'alcohol':'al-kuḥl', 'alchemy':'al-kīmiyā', 'algorithm':'al-khwarizmi',
    'alligator':'el lagarto', 'dandelion':'dent de lion', 'denim':'serge de nîmes',
    'pedigree':'pe de gru', 'suede':'gants de suède', 'camera':'camera obscura',
    'particle':'particula', 'republic':'res publica', 'lieutenant':'lieu tenant',
    'percent':'per centum', 'nonplus':'non plus', 'apart':'ad partem',
    'affair':'à faire', 'agree':'a gré', 'abandon':'à bandon', 'sinecure':'sine cūrā',
}
BASE_WORD = re.compile(r'(?<![a-zA-Z-])(?:'+'|'.join(BASE_EXPRESSIONS)+r')(?![a-zA-Z-])')

def inner_notes(split, known):
    notes = []
    for clause in CLAUSE.split(split):
        if REJECT.search(clause) or UNCERTAIN.search(clause):
            continue
        for m in BASE_WORD.finditer(clause):
            left, right = clause[:m.start()].rstrip(), clause[m.end():]
            if not (left.endswith(('+','＋')) or re.match(r'^[^a-zA-Z。；，+＋]{0,18}[+＋]',right)):
                continue
            note = PHRASES[BASE_EXPRESSIONS[m.group()]]
            if note not in known:
                notes.append(note)
                known.add(note)
    return notes

def join_notes(notes):
    return '\n\n'.join(notes)

@lru_cache(maxsize=40000)
def word_detail(word,sense,split,history,bases):
    note = phrase_notes(split+'\n'+history,word)
    note.extend(inner_notes(split,set(note)))
    return join_notes([annotated(split,word,sense,bases), *note])

def detailed_split(entry,bases=()):
    history = '\n'.join(label+'，'+gloss for label,gloss in entry['history'])
    return word_detail(entry['word'],entry['meaning'],entry['split'],history,tuple(bases))

def root_details(root, lesson):
    seen = set()
    def expand(text):
        result = []
        for paragraph in text.split('\n\n'):
            notes = [n for n in phrase_notes(paragraph,root['root']) if n not in seen]
            result.append(annotated(paragraph,root['root']))
            result.extend(notes)
            seen.update(notes)
        return join_notes(result)
    return expand(lesson['intro']), expand(lesson['forms'])

def dictionary_notes(text,word,splits=(),sense=''):
    # A dictionary page can select a secondary homograph (e.g. ounce the
    # animal). Match the selected etymology, not a note keyed to the spelling.
    text = re.split(r'[.\n]\s*(?:Compare|Cognates?|Doublet|See also)\b',text,maxsplit=1)[0]
    notes = phrase_notes(text,word,allow_direct=False)
    for formula in splits:
        # Keep the attributed dictionary text verbatim. Add a separate gloss
        # only for a clean, explicit decomposition, with no markup or branches.
        if re.fullmatch(rf'[-{LETTERS}]+(?: *[+＋] *[-{LETTERS}]+)+', formula):
            detail = annotated(formula,word,sense)
            if detail != formula and detail not in notes:
                notes.append(detail)
    return notes

def english_base_glosses(words, lexicon):
    """Use only documented English parents whose Chinese sense fits this word."""
    from build_catalog import components
    bases = {}
    bracket = re.compile(r'〔[^〕]*〕|（[^）]*）')
    senses = {w: re.split('[；，、／/]',bracket.sub('',e['meaning'])) for w,e in words.items()}
    for w, entry in words.items():
        if '+' not in entry['split'] and '＋' not in entry['split']:
            continue
        parents = set()
        for d in lexicon.get(w,()):
            for t in d.get('etymology_templates',()):
                if not any(k.startswith('lang') and v and v != 'en' for k,v in t['args'].items()):
                    parents.update(components(t))
            for sense in d.get('senses',()):
                parents.update(x['word'] for x in sense.get('form_of',()) if 'word' in x)
        matches = []
        for parent in sorted(parents):
            if parent == w or parent not in senses or len(parent)<2:
                continue
            # Cross-check both sides. Never take the first dictionary gloss for
            # a homograph (e.g. the financial institution in riverbank).
            for gloss in senses[parent]:
                gloss = gloss.strip().removesuffix('的')
                if (2 <= len(gloss) <= 7 and re.fullmatch('[一-龥]+',gloss)
                        and any(gloss in s for s in senses[w])):
                    matches.append((parent,gloss))
                    break
        if matches:
            bases[w] = tuple(matches)
    return bases
