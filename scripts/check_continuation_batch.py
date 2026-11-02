"""Read-only checks for a fresh authored batch before any library mutation."""
import ast
import importlib
import json
import sys
from collections import Counter
from pathlib import Path
from explanatory import load_lessons
from build_catalog import load_lexicon

base=Path(__file__).resolve().parents[1]
module_name=Path(sys.argv[1]).stem
roots,words=load_lessons()
m=importlib.import_module(module_name)
new_words=[x['word'] for x in m.WORDS]
new_roots=[x['id'] for x in m.ROOTS]
additions=getattr(m,'EXISTING_ROOT_ADDITIONS',{})
refs={w for r in [*m.ROOTS,*additions.values()] for w in r['words']}
lex=load_lexicon()
errors={
 'duplicate_new_words':[w for w,n in Counter(new_words).items() if n>1],
 'duplicate_new_roots':[r for r,n in Counter(new_roots).items() if n>1],
 'existing_words':sorted(set(new_words)&words.keys()),
 'existing_roots':sorted(set(new_roots)&roots.keys()),
 'missing_parent_entries':sorted(refs-set(new_words)-words.keys()),
 'missing_source_entries':sorted(set(new_words)-lex.keys()),
 'missing_extension_roots':sorted(set(additions)-roots.keys()),
 'unreferenced_words':sorted(set(new_words)-refs),
}
for node in ast.walk(ast.parse((base/'scripts/lesson_order.py').read_text())):
 if isinstance(node,ast.Dict):
  keys=[k.value for k in node.keys if isinstance(k,ast.Constant)]
  dup=[str(k) for k,n in Counter(keys).items() if n>1]
  if dup:errors.setdefault('duplicate_reading_order_keys',[]).extend(dup)
errors={k:v for k,v in errors.items() if v}
print(json.dumps(dict(roots=len(new_roots),words=len(new_words),errors=errors),ensure_ascii=False))
if errors:raise SystemExit(1)
