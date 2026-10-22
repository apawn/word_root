"""Save hand-written lesson records; this helper only serializes content."""
import json
from pathlib import Path
from urllib.parse import quote
TARGET=Path(__file__).resolve().parents[1]/'content/精讲'

def entry(word,ipa,meaning,sense,split,history,explanation,usage,contrast,*examples,sources=None):
    return dict(word=word,ipa=ipa,meaning=meaning,sense=sense,split=split,history=history,
                explanation=explanation,usage=usage,contrast=contrast,examples=examples,
                sources=sources or ['https://en.wiktionary.org/wiki/'+quote(word)+'#English'])

def save(name,roots,words):
    TARGET.mkdir(parents=True,exist_ok=True)
    (TARGET/f'roots_{name}.json').write_text(json.dumps(roots,ensure_ascii=False,indent=2))
    (TARGET/f'words_{name}.json').write_text(json.dumps(words,ensure_ascii=False,indent=2))
    print(name,len(roots),'roots',len(words),'words')
