"""Idempotently attach newly authored words to existing root lessons."""
import json
from pathlib import Path

def extend_existing_lessons(additions):
    folder = Path(__file__).resolve().parents[1] / 'content/精讲'
    found = {}
    documents = {}
    for path in folder.glob('roots*.json'):
        rows = json.loads(path.read_text())
        for row in rows:
            rid = row['id']
            if rid in additions:
                assert rid not in found, ('duplicate root', rid)
                found[rid] = (path, row)
                documents[path] = rows
    assert set(found) == set(additions), set(additions) - set(found)
    for rid, config in additions.items():
        path, lesson = found[rid]
        for word in config['words']:
            if word not in lesson['words']:
                lesson['words'].append(word)
            exclusions = lesson.get('exclude', {})
            if isinstance(exclusions, dict):
                exclusions.pop(word, None)
            elif isinstance(exclusions, list):
                lesson['exclude'] = [item for item in exclusions if item != word]
            else:
                raise TypeError(('unsupported exclusion format', rid, type(exclusions).__name__))
        label = config['label']
        branch = [label, ' · '.join(config['words'])]
        matches = [i for i, row in enumerate(lesson['branches']) if row[0] == label]
        assert len(matches) <= 1, (rid, label)
        if matches:
            lesson['branches'][matches[0]] = branch
        else:
            lesson['branches'].append(branch)
        note = config.get('note')
        if note and note not in lesson['forms']:
            lesson['forms'] += '\n\n' + note
    for path, rows in documents.items():
        path.write_text(json.dumps(rows, ensure_ascii=False, indent=2) + '\n')
