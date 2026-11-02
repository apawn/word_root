"""Append actual Kaikki JSONL records for missing study lemmas; never invent entries."""
import hashlib
import json
import sys
import urllib.request
from urllib.parse import quote
from datetime import date
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
CACHE = BASE / '.cache'

def main(words, refresh=False):
    from build_catalog import load_lexicon
    existing = load_lexicon()
    stamp = date.today().isoformat()
    raw_dir = CACHE / ('verified-kaikki-' + stamp)
    raw_dir.mkdir(exist_ok=True)
    manifest_path = raw_dir / 'manifest.json'
    manifest = json.loads(manifest_path.read_text()) if manifest_path.exists() else []
    fetched = []
    for word in dict.fromkeys(words):
        if word in existing and not refresh:
            print(word, 'already present')
            continue
        if not word.isalpha():
            raise ValueError('This helper accepts letter-only lemmas, preserving capitalization and accents')
        url = ('https://kaikki.org/dictionary/English/meaning/'
               f'{quote(word[0], safe="")}/{quote(word[:2], safe="")}/{quote(word, safe="")}.jsonl')
        data = urllib.request.urlopen(url, timeout=30).read()
        rows = [json.loads(line) for line in data.decode('utf-8').splitlines() if line.strip()]
        assert rows and all(row.get('word') == word and row.get('lang_code') == 'en'
                            and row.get('senses') for row in rows), word
        raw_name = word + ('-' + hashlib.sha256(data).hexdigest()[:12] if refresh else '') + '.jsonl'
        raw_path = raw_dir / raw_name
        raw_path.write_bytes(data)
        # The loader expects this optional export field. Preserve the original bytes above.
        for row in rows:
            row.setdefault('etymology_templates', [])
            row['source_urls'] = list(dict.fromkeys(row.get('source_urls', []) + [url]))
        fetched.append((word, rows))
        manifest.append(dict(word=word, url=url, raw_path=str(raw_path),
                             sha256=hashlib.sha256(data).hexdigest(), records=len(rows),
                             retrieved=stamp))
    with (CACHE / 'supplemental-lexicon.jsonl').open('a') as out:
        for word, rows in fetched:
            for row in rows:
                out.write(json.dumps(row, ensure_ascii=False) + '\n')
            print(word, 'appended actual source records:', len(rows))
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')

if __name__ == '__main__':
    main([word for word in sys.argv[1:] if word != '--refresh'], refresh='--refresh' in sys.argv[1:])
