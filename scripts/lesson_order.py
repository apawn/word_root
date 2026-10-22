"""Arrange lessons for reading: a base followed by its related extensions.

These are reading groups, not assertions that one English word historically
descends from another. Borrowed parallel forms can belong to the same group;
the individually authored histories remain the authority on actual descent.
"""
import collections
import re

from wordfreq import zipf_frequency
from build_catalog import components


# Common endings also cover the surface correspondence of parallel loans.
SUFFIXES = '''s es d ed ing er or ee ess ist ism ness ly ity ty al ial ical ic
ate iate ation ion ition ization isation ize ise able ible ance ence ant ent
ary ery ry ure ship hood dom let ling ette ous ious eous ive itive ful less
ish en y ian ium ify ification ment ential icle ity ward wards wise est'''.split()
PREFIXES = '''un non in im il ir dis re pre post anti counter over under inter intra
super sub semi multi micro macro hyper hypo pseudo neo de co out mis fore
trans ultra extra auto tele video bio geo photo radio electro'''.split()

# Spelling changes between related basic and extended forms. These are only
# used when both complete words occur in the same already authored root page.
ENDINGS = [
    ('y', 'ies'), ('y', 'ied'), ('y', 'ier'), ('y', 'iest'),
    ('y', 'ily'), ('y', 'iness'), ('y', 'ication'),
    ('able', 'ability'), ('ible', 'ibility'),
    ('ent', 'ence'), ('ant', 'ance'),
    ('ent', 'ential'), ('ence', 'ential'), ('ence', 'entiary'),
    ('ate', 'ation'), ('ate', 'ator'), ('ate', 'atory'),
    ('ic', 'ically'), ('ic', 'icity'), ('ic', 'icism'),
    ('al', 'ality'), ('ous', 'osity'),
    ('ive', 'ivity'), ('ive', 'ivism'),
    ('ize', 'ization'), ('ise', 'isation'),
    ('ify', 'ification'), ('fy', 'faction'),
    ('ceive', 'ception'), ('ceive', 'ceptive'), ('ceive', 'ceptible'),
    ('mit', 'mission'), ('mit', 'missive'), ('mit', 'missible'),
    ('duce', 'duction'), ('duce', 'ductive'), ('duce', 'duct'),
    ('scribe', 'scription'), ('scribe', 'scriptive'), ('scribe', 'script'),
    ('sume', 'sumption'), ('sume', 'sumptive'),
    ('solve', 'solution'), ('solve', 'soluble'),
    ('tain', 'tention'), ('tend', 'tension'),
    ('vert', 'version'), ('vert', 'versive'),
    ('clude', 'clusion'), ('clude', 'clusive'),
    ('pose', 'position'), ('pose', 'posite'),
    ('vive', 'vival'), ('prove', 'proof'),
    ('fy', 'fication'), ('tic', 'cy'), ('t', 'cy'),
    ('le', 'ular'), ('le', 'ulate'),
    ('logy', 'logical'), ('logy', 'logist'),
    ('graphy', 'graphic'), ('graphy', 'grapher'),
    ('metry', 'metric'), ('meter', 'metric'),
    ('nomy', 'nomic'), ('pathy', 'pathic'),
    ('phobia', 'phobic'), ('philia', 'philic'),
    ('logy', 'logous'), ('morphy', 'morphous'),
    ('scope', 'scopic'), ('scopy', 'scopic'),
    ('osis', 'otic'), ('esis', 'etic'),
    ('ism', 'ic'), ('ism', 'ist'),
]

# Irregular spelling, related loans and grammar forms need an explicit bridge.
# Parentage here describes teaching order, not historical derivation.
RELATED = {
    'be': 'am is are was were been being'.split(),
    'have': 'has had'.split(), 'do': 'does did done'.split(),
    'go': 'went gone'.split(), 'see': 'saw seen sight'.split(),
    'take': ['taken', 'takeover'], 'give': ['given'], 'make': ['made'],
    'say': ['said'], 'think': ['thought'], 'know': ['knew', 'known', 'knowledge'],
    'good': ['better', 'best', 'goodbye', 'goodnight', 'goodwill'], 'better': ['betterment'],
    'bad': ['worse', 'worst'], 'little': ['less', 'least'],
    'many': ['more', 'most'], 'much': ['more', 'most'],
    'will': ['would'], 'can': ['could'], 'may': ['might'],
    'shall': ['should'], 'buy': ['bought'], 'bring': ['brought'],
    'catch': ['caught'], 'teach': ['taught'], 'find': ['found'],
    'feel': ['felt'], 'keep': ['kept'], 'leave': ['left'],
    'lose': ['lost', 'loss'], 'choose': ['chose', 'chosen', 'choice'],
    'speak': ['spoke', 'spoken', 'speech'], 'write': ['wrote', 'written'],
    'break': ['broke', 'broken', 'breach'], 'bear': ['bore', 'borne', 'born', 'birth'],
    'sell': ['sold', 'sale'], 'tell': ['told', 'tale'],
    'feed': ['fed', 'food'], 'bleed': ['bled', 'blood'],
    'bind': ['bound', 'bond'], 'long': ['length'], 'strong': ['strength'],
    'wide': ['width'], 'deep': ['depth'], 'high': ['height'],
    'broad': ['breadth'], 'dead': ['death'], 'die': ['dead'],
    'succeed': ['success', 'succession'], 'exceed': ['excess'],
    'proceed': ['process', 'procession'], 'precede': ['precedence'],
    'recede': ['recession'], 'concede': ['concession'],
    'decide': ['decision', 'decisive'], 'divide': ['division', 'divisive'],
    'provide': ['provision', 'proviso'], 'revise': ['revision'],
    'supervise': ['supervision'], 'advise': ['advice'],
    'devise': ['device'], 'practise': ['practice'],
    'offend': ['offence', 'offense'], 'defend': ['defence', 'defense'],
    'respond': ['response'], 'expand': ['expansion'],
    'receive': ['receipt', 'recipient', 'receptive'], 'deceive': ['deceit'],
    'explain': ['explanation'], 'pronounce': ['pronunciation'],
    'pronunciation': ['pronunciatory'], 'announce': ['announcement'],
    'pronoun': ['pronominal'], 'noun': ['nominal'],
    'destroy': ['destruction'], 'construct': ['construction'],
    'repeat': ['repetition'], 'compete': ['competition', 'competitive'],
    'compose': ['composition', 'composite'],
    'oppose': ['opposition', 'opponent'], 'propose': ['proposal', 'proposition'],
    'acquire': ['acquisition'], 'require': ['requisite', 'requisition'],
    'inquire': ['inquiry', 'inquisition'], 'enquire': ['enquiry'],
    'enter': ['entrance', 'entry'], 'permit': ['permission'],
    'depart': ['departure', 'department'], 'apartment': ['apartments'],
    'special': ['especial'], 'especial': ['especially'],
    'species': ['speciation'],
    'suspect': ['suspicion', 'suspicious'],
    'despise': ['despite', 'despicable'], 'despite': ['spite'],
    'video': ['videography'],
    'envy': ['envious', 'enviable'], 'prudent': ['prudence'],
    'college': ['collegiate', 'collegial', 'collegium', 'collegian'],
    'intellect': ['intellectual'], 'intelligent': ['intelligence'],
    'religion': ['religious'], 'negligent': ['negligence', 'negligible'],
    'diligent': ['diligence'], 'legume': ['leguminous'],
    'differ': ['different'], 'different': ['differentiate', 'differential', 'difference'],
    'indifferent': ['indifference'], 'defer': ['deference'],
    'conifer': ['coniferous'], 'Lucifer': ['luciferin', 'luciferase'],
    'ferocious': ['ferocity'], 'fertile': ['fertility', 'fertilize'],
    'suffice': ['sufficient'], 'efficient': ['efficiency'],
    'efficacy': ['efficacious'], 'benefit': ['beneficial', 'benefactor', 'benefice'],
    'office': ['official', 'officiate', 'officious'],
    'fact': ['factual'], 'face': ['facial'],
    'facile': ['facility', 'facilitate'], 'feasible': ['feasibility'],
    'qualify': ['qualification'], 'unify': ['unification'],
    'stable': ['stability', 'stabilize'],
    'distance': ['distant', 'distal'], 'instant': ['instance'],
    'substance': ['substantial', 'substantive', 'substantiate'],
    'statue': ['statuesque'], 'statistic': ['statistics'],
    'supersede': ['supersession'], 'superstition': ['superstitious'],
    'science': ['scientific'], 'history': ['historic', 'historical'],
    'economy': ['economic', 'economics'], 'politics': ['political'],
    'physics': ['physical'], 'theory': ['theoretic', 'theoretical'],
    'analysis': ['analytic', 'analyze', 'analyse'],
    'diagnosis': ['diagnostic', 'diagnose'],
    'hypothesis': ['hypothetical', 'hypothesize', 'hypothesise'],
    'synthesis': ['synthetic', 'synthesize', 'synthesise'],
    'metamorphosis': ['metamorphic', 'metamorphose'],
    'psychology': ['psychologist', 'psychological'],
    'biology': ['biologist', 'biological'], 'geology': ['geologist', 'geological'],
    'technology': ['technologist', 'technological'],
    'photograph': ['photography', 'photographic', 'photographer'],
    'democracy': ['democrat', 'democratic'], 'aristocracy': ['aristocrat', 'aristocratic'],
    'bureaucracy': ['bureaucrat', 'bureaucratic'],
    'monarchy': ['monarch', 'monarchical'],
    'energy': ['energetic'], 'strategy': ['strategic'], 'allergy': ['allergic'],
    'number': ['numeral', 'numerous', 'numerical'],
    'maternal': ['maternity'], 'paternal': ['paternity'],
    'fraternal': ['fraternity'], 'sororal': ['sorority'],
    'evident': ['evidence', 'evidential', 'evidentiary'],
    'attention': ['attentive', 'attentional'],
    'attend': ['attention'], 'extend': ['extensive', 'extensible', 'extensor'],
    'tend': ['tendency'], 'contend': ['contention', 'contentious'],
    'pretend': ['pretence', 'pretense', 'pretentious'],
    'intend': ['intent'], 'tentacle': ['tentacular'],
    'ostensible': ['ostensive'], 'ostent': ['ostentation', 'ostentatious'],
    'legion': ['legionnaire'], 'neglect': ['negligent', 'negligible'],
    'eligible': ['ineligible'], 'collect': ['uncollected'],
    'unable': ['inability'], 'unstable': ['instability'],
    'specific': ['specification'], 'spectacle': ['spectacular'],
    'prospect': ['prospectus'], 'retrospect': ['retrospection', 'retrospective'],
    'introspect': ['introspection', 'introspective'],
    'introspection': ['introspective'], 'retrospection': ['retrospective'],
    'constable': ['constabulary'], 'constant': ['inconstant'],
}

# Complete words can coincide with an affix pattern without being useful
# simple-to-expanded reading pairs. Keep these branches independent.
BLOCKED = {('state', 'station'), ('statist', 'statistic'),
           ('stance', 'substance'), ('specie', 'species'),
           ('specie', 'special'), ('specie', 'specious'),
           ('facile', 'difficulty'), ('basis', 'base'),
           ('vape', 'vapor'), ('cane', 'canal'), ('ball', 'ballism'),
           ('amphibole', 'amphiboly'), ('copy', 'copious')}

SIBLING_ORDER = {'good': ['goodness', 'goods', 'goodwill', 'goodbye',
                          'goodnight', 'goody', 'goodie', 'better', 'best']}


def frequency(word):
    return zipf_frequency(word, 'en')


def normal(word):
    return word.lower().replace(' ', '')


def make_relations(words, lexicon):
    """Collect plausible reading links once; each page selects local links."""
    names = set(words)
    lookup = {normal(w): w for w in sorted(names, reverse=True)}
    candidates = collections.defaultdict(dict)

    def add(parent, child, strength, reason):
        if (parent == child or parent not in names or child not in names
                or (parent, child) in BLOCKED):
            return
        # When both readings work, finish the complete prefixed word's own
        # extensions first: recollect / recollection, preselect / preselection.
        # A dictionary can analyse the same noun as re- + collection instead.
        p, c = normal(parent), normal(child)
        if c.endswith(p) and not c.startswith(p) and c[:-len(p)] in PREFIXES:
            strength -= 25
        old = candidates[child].get(parent)
        if old is None or strength > old[0]:
            candidates[child][parent] = (strength, reason)

    for parent in sorted(names):
        base = normal(parent)
        if len(base) < 3:
            continue
        for suffix in SUFFIXES:
            forms = {base + suffix}
            if base.endswith('e') and suffix[0] in 'aeiouy':
                forms.add(base[:-1] + suffix)
            if base.endswith('y') and len(base) > 2 and base[-2] not in 'aeiou':
                forms.add(base[:-1] + 'i' + suffix)
            if (len(base) > 2 and base[-1] not in 'aeiouwxy'
                    and base[-2] in 'aeiou' and base[-3] not in 'aeiou'):
                forms.add(base + base[-1] + suffix)
            for form in forms:
                if form in lookup:
                    add(parent, lookup[form], 50, '词尾扩展或对应形式')
        for before, after in ENDINGS:
            if base.endswith(before) and len(base) > len(before) + 1:
                child = lookup.get(base[:-len(before)] + after)
                if child and len(normal(child)) >= len(base):
                    add(parent, child, 50, '相关词尾形式')
        for prefix in PREFIXES:
            child = lookup.get(prefix + base)
            if child:
                add(parent, child, 40, '前缀扩展')
        # A negative may wrap an inflected form absent from the page,
        # e.g. supervise -> unsupervised.
        for prefix in ['un', 'non', 'in', 'im', 'il', 'ir']:
            for suffix in ['ed', 'd', 'ing', 'able', 'ible']:
                forms = {prefix + base + suffix}
                if base.endswith('e'):
                    forms.add(prefix + base[:-1] + suffix)
                for form in forms:
                    if form in lookup:
                        add(parent, lookup[form], 35, '否定形式扩展')

    for child, authored in words.items():
        # Complete-word English components in the local dictionary evidence.
        # Foreign-language operands and mere "related terms" are not used.
        for entry in lexicon.get(child, []):
            for template in entry.get('etymology_templates', []):
                if any(k.startswith('lang') and v != 'en'
                       for k, v in template.get('args', {}).items()):
                    continue
                for parent in components(template):
                    parent = re.sub(r'<[^>]*>', '', parent)
                    if not parent.startswith('-') and not parent.endswith('-'):
                        add(parent, child, 70, '英语构词记录')
        # The author explicitly names a visible base in the decomposition.
        # Restrict this to already plausible links so comparison/negation prose
        # cannot fabricate a parent merely because it mentions another word.
        split_tokens = set(re.findall(r'[A-Za-z]+', authored['split']))
        for parent, (strength, reason) in list(candidates[child].items()):
            if parent in split_tokens and '+' in authored['split']:
                add(parent, child, max(strength, 85), '正文拆分与词形对应')

    for parent, children in RELATED.items():
        for child in children:
            add(parent, child, 100, '补充学习对应')
    return candidates


def order_family(family, relations):
    """A cycle-free reading forest, with every subtree kept contiguous."""
    names = set(family)
    original = {w: i for i, w in enumerate(family)}
    parents = {}
    evidence = {}
    links = []
    for child in names:
        for parent, (strength, reason) in relations.get(child, {}).items():
            if parent in names:
                # Prefer a nearby complete base over a shorter remote stem.
                links.append((-strength, -len(parent), len(child), parent, child, reason))
    for negative_strength, _, _, parent, child, reason in sorted(links):
        if child in parents:
            continue
        node = parent
        while node in parents and node != child:
            node = parents[node]
        if node == child:
            continue
        parents[child] = parent
        evidence[child] = reason

    children = collections.defaultdict(list)
    for child, parent in parents.items():
        children[parent].append(child)

    def child_key(word):
        parent = parents[word]
        # Keep suffix extensions before a new prefixed/compound subfamily.
        prefix = normal(word).endswith(normal(parent)) and not normal(word).startswith(normal(parent))
        custom = SIBLING_ORDER.get(parent, [])
        sibling = custom.index(word) if word in custom else len(custom)
        return (prefix, sibling, -frequency(word), len(word), original[word], word)

    for siblings in children.values():
        siblings.sort(key=child_key)

    def walk(word):
        yield word
        for child in children[word]:
            yield from walk(child)

    groups = [list(walk(w)) for w in family if w not in parents]
    groups.sort(key=lambda group: (-max(map(frequency, group)), -frequency(group[0]),
                                   original[group[0]], group[0]))
    ordered = [w for group in groups for w in group]
    assert len(ordered) == len(family) and set(ordered) == names
    return ordered, groups, {w: {'base': parents[w], 'basis': evidence[w]} for w in ordered if w in parents}
