"""Update internal continuation metadata only after a successful full validation."""
import hashlib
import json
import sys
from datetime import datetime
from zoneinfo import ZoneInfo
from pathlib import Path

base = Path(__file__).resolve().parents[1]
result = json.loads((base / '.cache/continuation-validation.log').read_text())
assert result.get('ok') and not result.get('errors'), result
from explanatory import load_lessons
verified_roots, verified_words = load_lessons()
assert (result['completed_lessons'], result['fully_explained_words']) == (len(verified_roots), len(verified_words)), 'Validation counts do not match current content'
assert result['authored_bilingual_examples'] == sum(len(w['examples']) for w in verified_words.values()), 'Example counts do not match current content'
current_digest=hashlib.sha256(json.dumps({'roots':verified_roots,'words':verified_words},ensure_ascii=False,sort_keys=True).encode()).hexdigest()
assert result.get('authored_sha256') == current_digest, 'Validation does not match the current authored revision'
path = base / '.cache/continuation-active.json'
state = json.loads(path.read_text())
state['validated'] = {
    'root_pages': result['completed_lessons'],
    'unique_words': result['fully_explained_words'],
    'examples': result['authored_bilingual_examples'],
}
for key, metric in [('new_roots', 'root_pages'), ('new_words', 'unique_words'), ('new_examples', 'examples')]:
    state[key] = state['validated'][metric] - state['baseline'][metric]
for suffix in sys.argv[1].split(','):
    item = '20261030_' + suffix
    if item not in state['authored_batches']:
        state['authored_batches'].append(item)
state['next_author_script'] = 'scripts/author_continuation_20261030_' + sys.argv[2] + '.py'
state['next_roots'] = sys.argv[3:]
# Preserve the latest actual usage-tool reading; checkpointing does not refresh usage.
state['evidence'] = '.cache/continuation-20261031-jt-evidence.json'
state['verified_source_manifests'] = sorted(str(p.relative_to(base)) for p in (base / '.cache').glob('verified-kaikki-*/manifest.json'))
path.write_text(json.dumps(state, ensure_ascii=False, indent=2) + '\n')
notes = base / 'content/\u7cbe\u8bb2/\u7eed\u5199\u8bf4\u660e.md'
text = notes.read_text()
start = text.index('\u6700\u65b0\u5b8c\u6574\u6821\u9a8c')
end = text.index('\u8865\u5e93\u673a\u5236', start)
v = state['validated']
replacement = (
    f'最新完整校验（{datetime.now(ZoneInfo("Asia/Shanghai")).date().isoformat()}）：'
    f"{v['root_pages']} deep root pages, {v['unique_words']} unique explained words, "
    f"{v['examples']} original bilingual examples; errors=[]. "
    f"Author batches validated through {sys.argv[1].split(',')[-1]}. "
    f"Next: {state['next_author_script']}; {'; '.join(state['next_roots'])}. "
    f"Weekly used {state['weekly_used_percent_last_read']}% at last tool reading; continue toward approximately 98% used. "
    'No images, ZIP updates, site builds, resets, purchases or subagents. '
    'Read continuation-active.json for the complete current checkpoint.\n\n'
)
notes.write_text(text[:start] + replacement + text[end:])
print(json.dumps(state['validated']))
